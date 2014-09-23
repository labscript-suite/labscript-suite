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
    
if sys.version < '3':
    input = raw_input

this_folder = os.path.realpath(os.path.dirname(__file__))
os.chdir(this_folder)

usage = """
usage:
  python setup.py install
  python setup.py uninstall [<path>]
  python setup.py build [--keep-hg]
  python setup.py dist
  python setup.py clean
"""

__version__ = '2.0.0-dev'

bitbucket_page = 'https://bitbucket.org/labscript_suite/'

# Can specify the specific tags or changesets to be used, should be 'branch(default) and max(tag())'
# for stable releases.
repos = {
         # 'labscript': 'branch(default) and max(tag())',
         'runmanager': 'Qt',
         'runviewer': 'gated-clocks',
         # 'blacs': 'branch(default) and max(tag())',
         # 'lyse': 'branch(default) and max(tag())',
         # 'mise': 'branch(default) and max(tag())',
         'labscript_utils': '1.1.0-dev', #'branch(default) and max(tag())',
         # 'labscript_devices': 'branch(default) and max(tag())',
        }

# Which programs should have application shortcuts made for them:
gui_programs = ['runmanager', 'runviewer', 'blacs', 'lyse', 'mise']

# The name of the readme file:
README = 'README.txt'

# These folders, which contain user code and settings,
# will not be deleted during uninstallation or overwritten
# during installation:
do_not_delete = ['userlib', 'config']

output_base = 'labscript_suite_' + __version__
output_file = output_base + '.zip'

if os.name == 'nt':
    default_install_folder = r'C:\labscript_suite'
else:
    default_install_folder = os.path.join(os.getenv('HOME'), 'labscript_suite')

IS_LABSCRIPT_SUITE = '.is_labscript_suite_install_dir'
IS_BUILD = '.is_labscript_suite_build_dir'

def get_all_files_and_folders(path):
    import itertools
    yield path
    if os.path.isdir(path):
        for root, folders, files in os.walk(path):
            for entry in itertools.chain(folders, files):
                yield os.path.join(root, entry)
                
def exclude_from_copying(path):
    if os.path.relpath(path, this_folder).startswith('.'):
        return True
    elif os.path.abspath(path) == os.path.abspath(output_file):
        return True
    return False
    
def build(keep_hg = None):
    if keep_hg == '--keep-hg':
        keep_hg = True
    elif keep_hg is not None:
        raise TypeError('Invalid argument %s'%keep_hg)
    else:
        keep_hg = False
    if os.path.exists(IS_BUILD):
        sys.stderr.write('Previous build exists, run \'clean\' command first.\n'+usage)
        sys.exit(1)
    for repo in repos:
        subprocess.check_call(['hg', 'clone', bitbucket_page+repo])
        os.chdir(repo)
        subprocess.check_call(['hg', 'update', '-r', repos[repo]])
        if not keep_hg:
            try:
                shutil.rmtree('.hg')
            except OSError:
                pass
            try:
                os.unlink('.hgtags')
            except OSError:
                pass
            try:
                os.unlink('.hgignore')
            except OSError:
                pass
        os.chdir(this_folder)
    # Add file that marks this as a labscript suite install dir:
    with open(IS_BUILD, 'w'):
        pass
        
def dist():
    if not os.path.exists(IS_BUILD):
        build()
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
    try:
        os.unlink(output_file)
        print('deleted', output_file)
    except OSError:
        pass
    for repo in repos:
        try:
            shutil.rmtree(repo)
            print('deleted', repo)
        except OSError:
            pass
    
def getinput(prompt, default):
    try:
        result = input(prompt + '\n(%s): '%default)
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

    
def install():
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
    if not os.path.exists(IS_BUILD):
        build()    
    print('Copying files')
    if not os.path.exists(install_folder):
        try:
            os.mkdir(install_folder)
        except OSError as e:
            sys.stderr.write('Could not create to install directory:\n %s'%str(e))
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
        sys.stderr.write('Could not write to install directory:\n %s'%str(e))
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
    # Add libs to python's search path:
    site_packages_dir = site.getsitepackages()[0]
    pth_file = os.path.join(site_packages_dir, 'labscript_suite.pth')
    print('Adding to Python search path (%s)'%pth_file)
    with open(pth_file, 'w') as f:
        f.write(install_folder + '\n')
        f.write(os.path.join(install_folder, 'userlib') + '\n')
        f.write(os.path.join(install_folder, 'userlib', 'pythonlib') + '\n')
    print('adding application shortcuts')
    if os.name == 'nt':
        from labscript_utils.winshell import appids, app_descriptions, make_shortcut, add_to_start_menu
        for program in gui_programs:
            path = os.path.join(install_folder, '%s.lnk'%program)
            target = sys.executable.lower().replace('.exe', 'w.exe')
            arguments = os.path.join(install_folder, program, '__main__.py')
            working_directory = os.path.join(install_folder, program)
            icon_path = os.path.join(install_folder, program, '%s.ico'%program)
            description = app_descriptions[program]
            appid = appids[program]
            make_shortcut(path, target, arguments, working_directory, icon_path, description, appid)
            add_to_start_menu(path)
    print('done')
    
def uninstall(*args, **kwargs):
    confirm = kwargs.pop('confirm', True)
    if kwargs:
        raise TypeError('uninstall() got unexpected keyword argument \'%s\''%kwargs.popitem()[0])
    if len(args) > 1:
        raise TypeError('uninstall() takes at most one positional argument (%s given)'%len(args))
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
    print('Removing application shortcuts')
    if os.name == 'nt':
        from labscript_utils.winshell import remove_from_start_menu
        for program in gui_programs:
            remove_from_start_menu('%s.lnk'%program)   
    site_packages_dir = site.getsitepackages()[0]
    pth_file = os.path.join(site_packages_dir, 'labscript_suite.pth')
    print('Removing from Python search path (%s)'%pth_file)
    if os.path.exists(pth_file):
        os.unlink(pth_file)
    print('Deleting files')
    # So we can use relative paths, helps reduce the risk of deleting stuff elsewhere:
    os.chdir(uninstall_folder)
    for entry in os.listdir('.'):
        if os.path.isdir(entry):
            delete = shutil.rmtree
        else:
            delete = os.unlink
        if entry not in do_not_delete:
            delete(entry)
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
        
