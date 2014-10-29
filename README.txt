labscript suite installer
=========================

A script to install the labscript suite onto a system.

([view on Bitbucket](https://bitbucket.org/labscript_suite/installer))

usage:
    python setup.py (install | uninstall | build | dist | clean)



Note: If on unix, run the installer with sudo. You should install to a user folder
(default is $HOME/labscript_suite), but the installer requires root privileges
in order to add the install directory to the Python search path.


Warning: if you are installing to a conda environment, ensure you do 'conda install pip'
and restart the terminal before installing the dependencies that require pip. Otherwise the
existing system pip (if any) will be used instead, which is not what you want.


install
-------

If running from a distributed bundle, having been extracted from a zip file,
copies the bundled labscript suite packages and directories to a chosen install
directory, adds them to Python's search path, and creates application shortcuts.
If running from a clean (not built) working copy of the installer, performs 'build'
first, and then the above.


uninstall [<path>]
--------------------

Removes labscript directories from Python's search path, removes application shortcuts and
deletes the contents of the install directory, except for the userlib directory and non-default
config files. Install directory will be automatically detected by looking in Python's search
path, or it can be provided as an argument if this fails.

The installer also copies also itself into the install directory as 'uninstall.py', and can used
from there to uninstall the labscript suite.


build
-----------------

Clones the labscript repositories from bitbucket into the current directory
Which revisions are used can be set in setup.py, but defaults to

    max(branch(default) and tag())

which means the most recent tagged revision in the default branch. Since we use tags
for version numbers only, this will use the latest stable release of each package.
The --keep-hg option does not remove repository information before bundling packages
into the output zip files. This means the resulting install will contain mercurial
repositories - this could be useful for developers.


dist
----

Performs 'build' if not already done, and bundles everything into a zip file for distribution of specific versions.


clean
-----

Removed build files and zip file, if any.
