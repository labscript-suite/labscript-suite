-*- markdown -*-

# labscript suite installer

A script to install the labscript suite onto a system.

([view on Bitbucket](https://bitbucket.org/labscript_suite/installer))

## usage:
    python setup.py (install | uninstall | build [--keep-hg] | dist | clean)

## `install`
If running from a distributed bundle, having been extracted from a zip file, 
copies the bundled labscript suite packages and directories to a chosen install
directory, adds them to Python's search path, and creates application shortcuts.
If running from a clean (not built) working copy of the installer, performs 'build'
first, and then the above. 
        
## `uninstall [<path>]`
The installer copies itself into the install directory as well, and can be used
to later uninstall the labscript suite. Removes labscript directories from Python's
search path, removes application shortcuts and deletes the contents of the install
directory, except for the userlib directory and non-default config files. Install directory
will be automatically detected by looking in Python's search path, or it can be provided 
as an argument if this fails.
        
## `build [--keep-hg]`
Clones the labscript repositories from bitbucket, deletes .hg* files
Which revisions are used can be set in setup.py, but defaults to
`max(branch(default) and tag())`
which means the most recent tagged revision in the default branch. Since we use tags
for version numbers only, this will use the latest stable release of each package.
The `--keep-hg` option does not remove repository information before bundling packages
into the output zip files. This means the resulting install will contain mercurial
repositories - this could be useful for developers.

## `dist`
Performs 'build' if not already done, and bundles everything into a zip file for distribution.

## `clean`
Removed build files and zip file, if any.