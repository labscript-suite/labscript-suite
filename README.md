labscript suite installer
=========================

A script to install the labscript suite onto a system.

You will need to install a mercurial client and Python distribution prior 
to running this installer. On windows, we recommend [TortoiseHg](http://tortoisehg.bitbucket.org/) and the 
[Annaconda Python Distribution](http://continuum.io/downloads).

Check out this repository (https://bitbucket.org/labscript_suite/installer) locally on your PC and follow the below instructions to install the labscript_suite. Depending on your Python distribution, you may be prompted to upgrade or install dependencies manually.

([view on Bitbucket](https://bitbucket.org/labscript_suite/installer))

usage:
    python setup.py (install | uninstall | build | dist | clean)



Note: If on unix, and installing using the system Python, install with sudo.
You should install to a user folder (default is $HOME/labscript_suite), but
the installer will require root privileges in order to add the install
directory to the Python search path. However if your Python installation is
somewhere that does not require root access (such as if you are using anaconda
isntalled to your home directory), sudo is not required.


Warning: if you are installing to a conda environment, ensure you do 'conda
install pip' and restart the terminal before installing the dependencies that
require pip. Otherwise the existing system pip (if any) will be used instead,
which won't install packages to your current environment.


install
-------

Runs 'build' if it has not already run. Copies the labscript suite packages to
a chosen install directory, adds them to Python's search path, and creates
application shortcuts. Checks that dependencies are satisfied and list missing
ones.


uninstall [<path>]
--------------------

Removes labscript directories from Python's search path, removes application
shortcuts and deletes the contents of the install directory, except for the
userlib directory and config files. Install directory will be automatically
detected by looking in Python's search path, or it can be provided as an
argument if this fails.

The installer also copies also itself into the install directory as
'uninstall.py', and can used from there to uninstall the labscript suite.


build
-----------------

Clones the labscript repositories from bitbucket into the current directory
Which revisions are used can be set in setup.py, but defaults to

    max(branch(default) and tag())

which means the most recent tagged revision in the default branch. Since we
use tags for version numbers only, this will use the latest stable release of
each package.


dist
----

Creates a zip file of the installer.


clean
-----

Removes build files and zip file, if any.