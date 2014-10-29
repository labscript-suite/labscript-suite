#####################################################################
#                                                                   #
# /setup.py                                                         #
#                                                                   #
# Copyright 2014, Monash University                                 #
#                                                                   #
# This file is part of the installer for the  labscript             #
# suite (see http://labscriptsuite.org), and is licensed under the  #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################

from __future__ import division, unicode_literals, print_function, absolute_import
import os
import sys
import errno
import subprocess
import shutil
import zipfile
import traceback
import site
import imp
from collections import OrderedDict
import ast
import textwrap
import contextlib

if sys.version < '3':
    input = raw_input
else:
    from importlib import reload

this_folder = os.path.realpath(os.path.dirname(__file__))
os.chdir(this_folder)

devnull = open(os.devnull, 'w')

usage = """
usage:
  python setup.py install
  python setup.py uninstall [<path>]
  python setup.py build
  python setup.py dist
  python setup.py clean
"""

__version__ = '2.0.0'

bitbucket_page = 'https://bitbucket.org/labscript_suite/'

# Can specify the specific tags or changesets to be used, should be 'branch(default) and max(tag())'
# for stable releases.
repos = {
    'labscript': 'branch(default) and max(tag())',
    'runmanager': 'branch(default) and max(tag())',
    'runviewer': 'branch(default) and max(tag())',
    'blacs': 'branch(default) and max(tag())',
    'lyse': 'gtk',
    'mise': 'default',
    'labscript_utils': 'branch(default) and max(tag())',
    'labscript_devices': 'branch(default) and max(tag())',
}

# Which programs should have application shortcuts made for them:
gui_programs = ['runmanager', 'runviewer', 'blacs', 'lyse', 'mise']

# The name of the readme file:
README = 'README.txt'

# The name of the dependencies file:
DEPENDENCIES = 'dependencies.txt'

# These folders, which contain user code and settings,
# will not be deleted during uninstallation or overwritten
# during installation:
do_not_delete = ['userlib', 'labconfig']

output_base = 'labscript_suite_' + __version__
output_file = output_base + '.zip'

# What will the shortcuts be called on Windows?
shortcut_format = 'labscript suite - %s.lnk'

if os.name == 'nt':
    default_install_folder = r'C:\labscript_suite'
else:
    default_install_folder = os.path.join(os.getenv('HOME'), 'labscript_suite')

IS_LABSCRIPT_SUITE = '.is_labscript_suite_install_dir'
IS_BUILD = '.is_labscript_suite_build_dir'

SUDO = False
if os.name == 'posix':
    sudo_uid = os.getenv('SUDO_UID')
    if sudo_uid is not None:
        SUDO = True
        SUDO_UID = int(sudo_uid)
        # Remove root privileges until we need them:
        os.seteuid(SUDO_UID)

@contextlib.contextmanager
def escalated_privileges():
    # Temporarily regain root privileges
    if SUDO:
        os.seteuid(0)
    try:
        yield
    finally:
        # Back to normal permissions
        if SUDO:
            os.seteuid(SUDO_UID)


def get_all_files_and_folders(path):
    import itertools
    yield path
    if os.path.isdir(path):
        for root, folders, files in os.walk(path):
            for entry in itertools.chain(folders, files):
                yield os.path.join(root, entry)


def exclude_from_copying(path):
    # Ignore dotfiles in the top level of the installer folder:
    if os.path.relpath(path, this_folder).startswith('.'):
        return True
    # Ignore the output zip file itself:
    elif os.path.abspath(path) == os.path.abspath(output_file):
        return True
    return False


def runcommand(args, check_retcode=True, print_command=True, input=None):
    import pipes
    command = ' '.join(pipes.quote(arg) for arg in args)
    if print_command:
        print('    ' + command)
    child = subprocess.Popen(args, stdin=subprocess.PIPE)
    stdout, stderr = child.communicate(input)
    if check_retcode and child.returncode != 0:
        raise OSError('Error running %s' % command)


def check_dependencies():
    deps = OrderedDict()
    print('Checking dependencies...\n')
    try:
        print('  checking for mercurial...', end='')
        subprocess.check_call(['hg'], stdout=devnull, stderr=devnull)
        print('yes')
    except OSError:
        print('no')
        sys.stderr.write('Please install mercurial (tortoisehg recommended) before continuing\n' +
                         'You will have to restart this terminal after installation for the installer to find it.\n')
        sys.exit(1)
    with open(DEPENDENCIES) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.strip() and not line.startswith('#'):
                package_name, module_name, optional, install_methods = line.split()
                optional = ast.literal_eval(optional)
                if optional:
                    comment = ''
                    j = 1
                    while lines[i - j].strip().startswith('#'):
                        comment = lines[i - j].strip().strip('#').strip() + ' ' + comment
                        j += 1
                else:
                    comment = None
                deps[module_name] = package_name, optional, install_methods, comment
    nonoptional_missing = False
    optional_missing = False
    output_lines = []
    for module_name in deps:
        package_name, optional, install_methods, comment = deps[module_name]
        # Don't bother checking pywin32 if we are not on Windows:
        if package_name == 'pywin32' and not os.name == 'nt':
            continue
        try:
            print('  checking for %s...' % package_name, end='')
            imp.find_module(module_name)
            print('yes')
        except ImportError:
            print('no')
            if optional:
                optional_missing = True
            else:
                nonoptional_missing = True
            if optional:
                output_lines.append('')
                for line in textwrap.wrap(comment):
                    output_lines.append('  # ' + line)
                output_lines.append('  [OPTIONAL] %s not found, installable via %s' % (package_name, install_methods))
            else:
                output_lines.append('  %s not found, installable via %s' % (package_name, install_methods))
    if nonoptional_missing or optional_missing:
        print('\nMissing dependencies:\n')
    for line in output_lines:
        print(line)

    if nonoptional_missing:
        sys.stderr.write('\nNon-optional dependencies are missing.\nPlease install dependencies and run again.\n')
        sys.exit(1)
    elif optional_missing:
        print('\nAll not-optional dependencies satisfied.')
        sys.stderr.write('\nSome optional dependencies were not satisfied.' +
                         'Please review the above and decide whether you require these packages.\n')
        if not yn_choice('Continue without these optional packages?', default='n'):
            sys.exit(1)
    else:
        print('\nAll dependencies satisfied')


def build():
    if os.path.exists(IS_BUILD):
        sys.stderr.write('Previous build exists, run \'clean\' command first.\n' + usage)
        sys.exit(1)
    for repo in repos:
        print('cloning %s' % repo)
        runcommand(['hg', 'clone', bitbucket_page + repo])
        os.chdir(repo)
        print('updating to %s' % repos[repo])
        runcommand(['hg', 'update', '-r', repos[repo]])
        os.chdir(this_folder)
    # Add file that marks this as a labscript suite install dir:
    with open(IS_BUILD, 'w'):
        pass


def dist():
    if os.path.exists(IS_BUILD):
        sys.stderr.write('Build exists, run \'clean\' command first.\n' + usage)
        sys.exit(1)
    print('Writing %s...' % output_file)
    with zipfile.ZipFile(output_file, 'w') as f:
        for entry in get_all_files_and_folders('.'):
            if not exclude_from_copying(entry):
                f.write(entry, os.path.join(output_base, entry))
    print('done')


def sdist():
    dist()


def bdist():
    dist()


def clean():
    try:
        os.unlink(IS_BUILD)
        print('deleted', IS_BUILD)
    except OSError:
        pass
    if os.path.exists(output_file):
        try:
            os.unlink(output_file)
            print('deleted', output_file)
        except OSError as e:
            sys.stderr.write('Could not delete %s:\n%s\n' % (output_file, str(e)))
    for repo in repos:
        if os.path.exists(repo):
            try:
                shutil.rmtree(repo)
                print('deleted', repo)
            except OSError as e:
                sys.stderr.write('Could not delete %s:\n%s\n' % (repo, str(e)))


def getinput(prompt, default):
    try:
        result = input(prompt + '\n(%s): ' % default)
        return result or default
    except KeyboardInterrupt, EOFError:
        sys.exit(1)


def yn_choice(message, default='y'):
    try:
        choices = 'Y/n' if default.lower() in ('y', 'yes') else 'y/N'
        choice = raw_input("%s\n(%s): " % (message, choices))
        values = ('y', 'yes', '') if default == 'y' else ('y', 'yes')
        return choice.strip().lower() in values
    except KeyboardInterrupt, EOFError:
        sys.exit(1)


def make_labconfig_file(install_folder):
    from labscript_utils.labconfig import LabConfig, default_config_path
    source_path = os.path.join(install_folder, 'labconfig', 'example.ini')
    target_path = default_config_path
    if os.path.exists(target_path):
        # Don't modify it, leave their config as it is:
        return
    print('making default labconfig file')
    with open(source_path) as infile, open(target_path, 'w') as outfile:
        data = infile.read()
        data = data.replace('\\', os.path.sep)
        outfile.write(data)
    # Now change some things about it:
    config = LabConfig()
    config.set('DEFAULT', 'labscript_suite', install_folder)
    if sys.platform == 'linux2':
        config.set('programs', 'text_editor', 'gedit')
    elif sys.platform == 'darwin':
        config.set('programs', 'text_editor', 'open')
        config.set('programs', 'text_editor_arguments', '-a TextEdit {file}')
    if sys.platform != 'win32':
        config.set('programs', 'hdf5_viewer', 'hdfview')


def install():
    check_dependencies()
    if not os.path.exists(IS_BUILD):
        build()
    install_folder = getinput('\nEnter custom installation directory or press enter', default_install_folder)
    install_folder = os.path.abspath(install_folder)

    if os.path.exists(install_folder) and os.path.exists(os.path.join(install_folder, IS_LABSCRIPT_SUITE)):
        if not yn_choice('\nReplace existing installation? in %s? ' % install_folder +
                         'userlib and configuration ' +
                         'will be kept, but backing them up is recommended.', default='n'):
            print('Cancelled')
            sys.exit(1)
        uninstall(confirm=False)
        os.chdir(this_folder)

    # Add libs to python's search path:
    site_packages_dir = site.getsitepackages()[0]
    pth_file = os.path.join(site_packages_dir, 'labscript_suite.pth')
    print('Adding to Python search path (%s)' % pth_file)
    # temporarily escalate privileges so we can create the .pth file:
    with escalated_privileges():
        with open(pth_file, 'w') as f:
            f.write(install_folder + '\n')
            f.write(os.path.join(install_folder, 'userlib') + '\n')
            f.write(os.path.join(install_folder, 'userlib', 'pythonlib') + '\n')

    print('Copying files')
    if not os.path.exists(install_folder):
        try:
            os.mkdir(install_folder)
        except OSError as e:
            sys.stderr.write('Could not create to install directory:\n %s' % str(e))
            sys.exit(1)
    try:
        # Add file that marks this as a labscript suite install dir:
        with open(os.path.join(install_folder, IS_LABSCRIPT_SUITE), 'w'):
            pass
        for entry in os.listdir('.'):
            if not exclude_from_copying(entry):
                if os.path.isdir(entry):
                    dest = os.path.join(install_folder, entry)
                    copy = shutil.copytree
                else:
                    dest = install_folder
                    copy = shutil.copy
                if entry in do_not_delete:
                    if os.path.exists(dest):
                        continue
                copy(entry, dest)
    except OSError as e:
        sys.stderr.write('Could not write to install directory:\n %s' % str(e))
        sys.exit(1)
    # Rename setup.py to uninstall.py, as it will function only as an uninstaller from within the
    # labscript install directory:
    shutil.move(os.path.join(install_folder, 'setup.py'), os.path.join(install_folder, 'uninstall.py'))
    # Replace the readme file with one with instructions for uninstalling only
    os.unlink(os.path.join(install_folder, README))
    with open(os.path.join(install_folder, 'README_uninstall.txt'), 'w') as f:
        f.write('To uninstall, run: \n\n' +
                '    python uninstall.py\n\n' +
                'in this directory.\n' +
                'userlib and configuration ' +
                'will be kept, but backing them up is recommended.\n')
    # Remove the dependencies.txt file:
    os.unlink(os.path.join(install_folder, DEPENDENCIES))
    # Reload the site module so later code sees these paths:
    reload(site)
    make_labconfig_file(install_folder)
    if os.name == 'nt':
        print('adding application shortcuts')
        # TODO make this work on linux!
    if os.name == 'nt':
        from labscript_utils.winshell import appids, app_descriptions, make_shortcut, add_to_start_menu
        for program in gui_programs:
            path = os.path.join(install_folder, shortcut_format % program)
            executable = sys.executable.lower()
            if not executable.endswith('w.exe'):
                executable = executable.replace('.exe', 'w.exe')
            target = executable
            arguments = os.path.join(install_folder, program, '__main__.py')
            working_directory = os.path.join(install_folder, program)
            icon_path = os.path.join(install_folder, program, '%s.ico' % program)
            description = app_descriptions[program]
            appid = appids[program]
            make_shortcut(path, target, arguments, working_directory, icon_path, description, appid)
            add_to_start_menu(path)
        # Clear the icon cache so Windows gets the shortcut icons right even if they were previously broken:
        try:
            subprocess.Popen(['ie4uinit.exe', '-ClearIconCache'])
        except Exception:
            sys.stderr.write('failed to clear icon cache, icons might be blank\n')
    print('done')


def uninstall(*args, **kwargs):
    confirm = kwargs.pop('confirm', True)
    if kwargs:
        raise TypeError('uninstall() got unexpected keyword argument \'%s\'' % kwargs.popitem()[0])
    if len(args) > 1:
        raise TypeError('uninstall() takes at most one positional argument (%s given)' % len(args))
    elif args:
        uninstall_folder = args[0]
    else:
        for path in sys.path:
            if os.path.exists(os.path.join(path, IS_LABSCRIPT_SUITE)):
                uninstall_folder = path
                break
        else:
            if not os.path.exists(os.path.join(default_install_folder, IS_LABSCRIPT_SUITE)):
                sys.stderr.write('\nERROR: Cannot find a labscript suite installation on this system\n'
                                 'Please provide the install directory')
                sys.stderr.write(usage)
                sys.exit(1)
            uninstall_folder = default_install_folder
    if confirm:
        if not yn_choice('\nUninstall the labscript suite from %s? ' % uninstall_folder +
                         'userlib and configuration ' +
                         'will be kept, but backing them up is recommended.', default='n'):
            print('Cancelled')
            sys.exit(1)
    if not os.path.exists(os.path.join(uninstall_folder, IS_LABSCRIPT_SUITE)):
        sys.stderr.write(
            '\nERROR: %s does not appear to be a labscript suite installation directory. ' % uninstall_folder +
            'If you really want it gone, please delete it manually.\n')
        sys.exit(1)
    if os.name == 'nt':
        print('Removing application shortcuts')  # TODO unix
        from labscript_utils.winshell import remove_from_start_menu
        for program in gui_programs:
            remove_from_start_menu(shortcut_format % program)
    site_packages_dir = site.getsitepackages()[0]
    pth_file = os.path.join(site_packages_dir, 'labscript_suite.pth')
    print('Removing from Python search path (%s)' % pth_file)
    if os.path.exists(pth_file):
        with escalated_privileges():
            os.unlink(pth_file)
    print('Deleting files')
    # So we can use relative paths, helps reduce the risk of deleting stuff elsewhere:
    os.chdir(uninstall_folder)
    for entry in os.listdir('.'):
        if os.path.isdir(entry):
            delete = shutil.rmtree
        else:
            delete = os.unlink
        if entry not in do_not_delete and entry != IS_LABSCRIPT_SUITE:
            delete(entry)
    os.unlink(IS_LABSCRIPT_SUITE)
    print('done')


if __name__ == '__main__':
    if os.path.exists(IS_LABSCRIPT_SUITE):
        # Once copied into the labscript install directory at install time,
        # this script will function as an uninstaller only.
        uninstall()
        sys.exit(0)
    else:
        actions = {'install': install,
                   'uninstall': uninstall,
                   'build': build,
                   'dist': dist,
                   'clean': clean,
                   'check_dependencies': check_dependencies
                   }

        if len(sys.argv) < 2:
            sys.stderr.write(usage)
            sys.exit(1)
        action = sys.argv[1]
        try:
            function = actions[action]
        except KeyError:
            sys.stderr.write(usage)
            sys.exit(1)
        else:
            args = sys.argv[2:]
            try:
                function(*args)
            except Exception:
                sys.stderr.write(traceback.format_exc())
                sys.stderr.write(usage)
                sys.exit(1)
