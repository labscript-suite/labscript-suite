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

if sys.version < '3':
    input = raw_input

this_folder = os.path.realpath(os.path.dirname(__file__))
os.chdir(this_folder)

usage = 'usage: python setup.py (install | uninstall | build [--keep-hg] | clean)\n'

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
other_includes = [__file__,
                  'README.txt',
                  'config',
                  'userlib']

build_folder = os.path.join(this_folder, 'build')
output_file = os.path.join(build_folder, 'labscript_suite_%s.zip'%__version__)

if os.name == 'nt':
    default_install_dir = r'C:\labscript_suite'
else:
    default_install_dir = os.path.join(os.getenv('HOME'), 'labscript_suite')

    
def get_all_files_and_folders(path):
    yield path
    if os.path.isdir(path):
        for root, folders, files in os.walk(path):
            for folder in folders:
                yield os.path.join(root, folder)
            for file in files:
                yield os.path.join(root, file)
                
    
def build(keep_hg = None):
    if keep_hg == '--keep-hg':
        keep_hg = True
    elif keep_hg is not None:
        raise TypeError('Invalid argument %s'%keep_hg)
    else:
        keep_hg = False
    if os.path.exists(build_folder):
        sys.stderr.write('Previous build exists, run \'clean\' command first.\n'+usage)
        sys.exit(1)
    os.mkdir(build_folder)
    for repo in repos:
        os.chdir(build_folder)
        subprocess.check_call(['hg', 'clone', bitbucket_page+repo])
        os.chdir(os.path.join(build_folder, repo))
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
    print('Writing %s...' % output_file)
    with zipfile.ZipFile(output_file, 'w') as f:
        os.chdir(build_folder)
        for repo in repos:
            for entry in get_all_files_and_folders(repo):
                f.write(entry)
            shutil.rmtree(repo)
        os.chdir(this_folder)
        for path in other_includes:
            for entry in get_all_files_and_folders(path):
                f.write(entry)
    print('done')


def clean():
    if os.path.exists(build_folder):
        shutil.rmtree(build_folder)
    
def getinput(prompt, default):
    result = input(prompt + ' (%s): '%default)
    return result or default 
    
def yn_choice(message, default='y'):
    choices = 'Y/n' if default.lower() in ('y', 'yes') else 'y/N'
    choice = raw_input("%s (%s) " % (message, choices))
    values = ('y', 'yes', '') if default == 'y' else ('y', 'yes')
    return choice.strip().lower() in values

def install():
    install_folder = getinput('Enter custom installation directory', default_install_dir)
    if os.path.exists(install_folder):
    if yn_choice('Install directory %s already exists, overwrite?'%install_folder, default='n'):
        shutil.rmtree(install_folder)
    try:
        os.mkdir(install_dir)
    except OSError as e:
        sys.stderr.write('Could not create install directory:\n %s'%str(e))
        import IPython
        IPython.embed()
        
def uninstall():
    pass
    
if __name__ == '__main__':
    actions = {'install': install,
               'uninstall': uninstall,
               'build': build,
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
        
