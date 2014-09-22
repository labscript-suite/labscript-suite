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

usage = 'usage:\npython setup.py (install | uninstall [<path>] | build [--keep-hg] | clean)\n'

__version__ = '2.0.0-dev'

bitbucket_page = 'https://bitbucket.org/labscript_suite/'

# Can specify the specific tags or changesets to be used, otherwise will use the most
# recent tag in the default branch:
repos = {
         # 'labscript': 'branch(default) and max(tag())',
         'runmanager': 'max(branch(default) and tag())',
         # 'runviewer': 'branch(default) and max(tag())',
         # 'blacs': 'branch(default) and max(tag())',
         # 'lyse': 'branch(default) and max(tag())',
         # 'mise': 'branch(default) and max(tag())',
         # 'labscript_utils': 'branch(default) and max(tag())',
         # 'labscript_devices': 'branch(default) and max(tag())',
        }

# Non repository files to be included:
other_includes = ['setup.py',
                  'README.md',
                  'config',
                  'userlib']

# Which of the above files pertain to the installer itself. They will be
# installed in an 'uninstall' directory, as the same setip.py script can
# be used for uninstalling.            
installer_files = ['setup.py',
                   'README.md']

# These folders, which contain user code and settings,
# will not be deleted during uninstallation or overwritten
# during installation:
do_not_delete = ['userlib', 'config']

# Although we won't delete the above folders, we will
# overwrite specific files within them if installing over the top:
files_to_overwrite = [os.path.join('config', 'default.ini')]

output_base = 'labscript_suite_' + __version__
output_file = output_base + '.zip'

if os.name == 'nt':
    default_install_folder = r'C:\labscript_suite'
else:
    default_install_folder = os.path.join(os.getenv('HOME'), 'labscript_suite')

IS_LABSCRIPT_SUITE = '.is_labscript_suite_install_dir'
IS_BUILD = '.is_labscript_suite_build'

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
    # Add file that marks this as a labscript suite install dir:
    os.chdir(this_folder)
    with open(IS_BUILD, 'w') as f:
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
    except OSError:
        pass
    try:
        os.unlink(output_file)
    except OSError:
        pass
    for repo in repos:
        try:
            shutil.rmtree(repo)
        except OSError:
            pass
    
def getinput(prompt, default):
    try:
        result = input(prompt + ' (%s): '%default)
        return result or default 
    except KeyboardInterrupt, EOFError:
        sys.exit(1)
    
    
def yn_choice(message, default='y'):
    try:
        choices = 'Y/n' if default.lower() in ('y', 'yes') else 'y/N'
        choice = raw_input("%s (%s) " % (message, choices))
        values = ('y', 'yes', '') if default == 'y' else ('y', 'yes')
        return choice.strip().lower() in values
    except KeyBoardInterrupt, EOFError:
        sys.exit(1)

    
def install():
    if not os.path.exists(IS_BUILD):
        build()
    # Copy files:
    install_folder = getinput('Enter custom installation directory or press enter', default_install_folder)
    install_folder = os.path.abspath(install_folder)
    if os.path.exists(install_folder):
        if yn_choice('Install directory %s already exists, ' % install_folder + 
                     'Replace existing installation? userlib and non-default config settings ' +
                     'will be kept, but backing them up is recommended.', default='n'):
            uninstall()
            
    print('Copying files...')
    if not os.path.exists(install_folder):
        try:
            os.mkdir(install_folder)
        except OSError as e:
            sys.stderr.write('Could not write to install directory:\n %s'%str(e))
            sys.exit(1)
    try:
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
        for entry in files_to_overwrite:
            dest = os.path.join(install_folder, entry)
            if os.path.exists(dest):
                os.unlink(dest)
            shutil.copy(entry, dest)
    except OSError as e:
        sys.stderr.write('Could not write to install directory:\n %s'%str(e))
        sys.exit(1)
    # Copy the readme and setup script itself to an "uninstall" directory:
    uninstall_folder = os.path.join(install_folder, "uninstall")
    os.mkdir(uninstall_folder)
    for entry in installer_files:
        shutil.move(os.path.join(install_folder, entry), uninstall_folder)
    # Add file that marks this as a labscript suite install dir:
    with open(os.path.join(install_folder), IS_LABSCRIPT_SUITE, 'w'):
        pass
    shutil.move(os.path.join(install_folder, entry), uninstall_folder)
    # Add libs to python's search path:
    site_packages_dir = site.getsitepackages()[0]
    pth_file = os.path.join(site_packages_dir, 'labscript_suite.pth')
    print('Adding install directories to PYTHONPATH by writing (%s)'%pth_file)
    with open(pth_file, 'w') as f:
        f.write(install_folder + '\n')
        f.write(os.path.join(install_folder, 'userlib') + '\n')
        f.write(os.path.join(install_folder, 'userlib', 'pythonlib') + '\n')
        
    
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
            if not os.path.exists(default_install_folder):
                sys.stderr.write('ERROR: Cannot find a labscript suite installation on this system\n'
                                 'Please provide the install directory')
                sys.stderr.write(usage)
                sys.exit(1)
            uninstall_folder = default_install_folder
    if confirm:
        if not yn_choice('Uninstall the labscript suite from %s? ' % uninstall_folder + 
                         'userlib and non-default config settings ' +
                         'will be kept, but backing them up is recommended.', default='n'):
            sys.exit(1)
    if not os.path.exists(os.path.join(uninstall_folder, IS_LABSCRIPT_SUITE)):
        sys.stderr.write(
            'ERROR: %s does not appear to be a labscript suite installation directory. ' % uninstall_folder +
            'If you really want it gone, please delete it manually.\n')
        sys.exit(1)
    if 'pythonlib' in uninstall_folder:
        class BeMoreCareful(ValueError): pass
        raise BeMoreCareful("Don't delete your working directory, stupid")
        
    print(uninstall_folder)
    # def ignore(folder, entries):
        # entries = set(entries)
        # if folder == install_folder:
            # for folder_to_keep in do_not_delete:
                # if os.path.join(install_folder
            # if os.path.exists(os.path.)
            # return [f for f in files if f not in ]
    # Be careful implementing this that you don't delete the code you're working on like an idiot.

    
if __name__ == '__main__':
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
        
