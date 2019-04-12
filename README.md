labscript suite installer
=========================

A script to install the labscript suite onto a system.

Contents
========

[TOC]

Installation instructions
=========================

1. Install prerequisites
------------------------
You will need to install Python and Mercurial prior to running the labscript suite
installer. Mercurial—also known as 'hg'—is a 'version control system', which the
installer uses to download the latest versions of the labscript suite components from
bitbucket.org, and which you can use to update those components to newer versions in the
future.

On Windows, we recommend you obtain Mercurial by installing
[TortoiseHg](http://tortoisehg.bitbucket.io/) and Python from the [Anaconda Python
Distribution](https://www.anaconda.com/download/). For new setups, we recommend using
Python 3. The labscript suite is compatible with Python 2.7, but Python 2.7 is nearing
end of life and the labscript suite will eventually drop support for it.

If you are using the Anaconda Python distribution, we recommend that you install it
"just for me" (not "for all users"), and that you do not check the "add Anaconda to the
PATH" checkbox in the installer. Then, to use Anaconda Python from the command line,
open the "Anaconda Prompt" start menu shortcut instead of `cmd.exe`. From there you can
use the `python`, `conda` and `pip` commands as required below. If using Anaconda Python
on Unix, you will need to follow Anaconda's instructions for your operating system and
shell to activate the conda environment before running commands. You may use Anaconda
environments to install multiple copies of the labscript suite if you like—if so the
start menu shortcuts will contain the conda environment name.


2. Clone this repository
------------------------
Use mercurial to download ('clone') the latest version of the installer from bitbucket.
You can do this using TortoiseHg's graphical interface by right clicking in your file
manager and selecting Tortoisehg > Clone. Then, enter the address of this repository,
`https://bitbucket.org/labscript_suite/installer` in the 'source' field and click
'clone'. Alternately, you can clone this repository from the command line using the
following command:
```
hg clone https://bitbucket.org/labscript_suite/installer
```
Whichever method is used, a folder called 'installer' will be created in the current
directory. TortoiseHg, if you used it, may open 'hg workbench' showing the revision
history of the installer itself. You can close that for now.

3. Run the installer
--------------------
Open the command prompt (the Anaconda Prompt if using Anaconda) and navigate to the
freshly-cloned 'installer' folder using `cd`. To quickly navigate to a particular folder
in Windows, you can press Ctrl-L in the file explorer to highlight the current
directory, and copy it to the clipboard with Ctrl-C. Then, in the command prompt type
`cd` and a space followed by Ctrl-V, and press enter. Once in the installer directory
run the installer by typing
```
python setup.py install
```
and follow the prompts.

Note: if on Unix, you may need to specify `python3` instead of just `python` to ensure
the suite is installed with Python 3 instead of Python 2. If on Unix and using system
Python (i.e. not Anaconda), you should also run the above command with `sudo`. Even
though the installer will by default install the labscript suite to your home directory,
in order to add that directory to the Python search path, it may need root privileges.

During installation, the installer will check if the required Python packages are
installed, and will list any that are not. If using Anaconda, most packages are
available in the conda repositories and can be installed by typing:
```
conda install <package>
```
from the Anaconda prompt. Some packages are not available in the conda repositories
however, and these should be installed using pip, the standard Python package manager,
by typing:
```
pip install <package>
```
As a general rule, always prefer using conda, where possible, and use pip only to
install packages not available from conda. If you are on Windows and not using Anaconda,
you can install all packages using `pip`. If you are on Unix and not using Anaconda, you
may have another package manager that you prefer installing packages with, only using
pip for the packages not available from your package manager.

Once all required (and desired optional) Python packages are installed, the installer
will copy the labscript suite components to the chosen install directory, add that
directory (as well as the 'userlib' and 'userlib/pythonlib' subdirectories—more on these
later) to the Python search path, and if on Windows, will create start menu shortcuts
for the applications.

If you encounter a problem during installation, you may wish to try running
```
python setup.py clean
```
to clear temporary files from the installer and begin installation from scratch. Do not
hesitate to ask for help or report a problem with the installer (or any labscript suite
component) by filing an issue here on the installer's Bitbucket repository, or by
sending a message to the [mailing list](http://groups.google.com/group/labscriptsuite).

4. Install a text editor
------------------------
To use the labscript suite, you will need at the very least, a text editor to write
labscript experiment scripts. [Notepad++](https://notepad-plus-plus.org/) and [Sublime
Text](https://www.sublimetext.com/) are great options, but any text editor or Python IDE
will do, including [Spyder](https://www.spyder-ide.org/) which comes with Anaconda and
is geared toward those familiar with MatLab. The single most important issue when
setting up a text editor to write Python code is that you configure it to insert four
spaces—and not a tab character—when you hit the tab key. Almost all Python code is
written with four spaces used for indentation, and you will run into difficult-to-debug
issues if your code contains tab characters. So whichever text editor you install, if it
does not already insert four spaces (Spyder already does for example), check its
documentation for how to configure it to do so.

5. Install HDFview
------------------
Labscript shot files are in the HDF5 format, and can be viewed using the [HDFview
tool](https://www.hdfgroup.org/downloads/hdfview/). Although you don't need HDFview to
use the labscript suite, it can be informative to quickly inspect shot files to see
their contents without writing Python code.

6. Edit your labconfig file
---------------------------
The installer creates a file `labscript_suite/labconfig/<your_computer's_hostname>.ini`,
which contains configuration settings for the labscript suite. The reason the filename
is your computer's hostname is that the labscript suite can be run over multiple
computers, and these computers may need to have configuration files that are in sync
with each other in order for the labscript suite components to communicate with each
other. As such, you may wish to keep all the configuration files for a laboratory in one
folder under version control. The filename being the hostname means labscript suite
programs know which file to read even if several config files are present.

Most of the settings in labconfig do not need to be modified. Exceptions are:

`[DEFAULT]/experiment_name`: this is the name of the experiment, or laboratory, as a
whole. This name determines the names of subfolders where shot files are saved,
subfolders where saved settings from labscript suite applications are stored, and
default locations where labscript suite programs expect experiment scripts and analysis
scripts to be located. It should be short, and a valid Python module name, i.e. contain
only alphanumeric characters and underscores, and not begin with a numerical digit (this
ensures that code stored in subfolders with this name can be imported by other Python
code). As with the labconfig file being specific to each computer, experiment names
being unique to different experiments allows experiment scripts and other data from
multiple experiments to be stored in the same version control repository without
interference.

`[DEFAULT]/shared_drive`: this is the drive letter or mount path of the drive that shot
files (and some other files) will be stored on. If running the labscript suite on
multiple computers, this is how the programs share shot files - by passing filepaths to
each other that refer to files on the shared drive. If using the labscript suite on a
single computer, you can leave this as `C:\` or `~/labscript_shared` on Windows or Unix
respectively. Then shot files will be saved in `C:\Experiments` or
`~/labscript_shared/Experiments`. Otherwise, set it to the drive letter of a network
drive that will be accessible to all computers running labscript suite programs (it is
OK if each computer has the shared drive mounted as a different drive letter or at a
different mount point, so long as this setting in each computer's labconfig file points
to the right location).

`[servers]/zlock` This is the hostname or IP address of the computer that will be
running a 'zlock' server. Zlock is a program that tracks which other program has a file
open at any time. By asking zlock server for permission before opening a file, labscript
suite programs ensure that they do not write to a file at the same time as another
labscript suite program is reading or writing, which could cause data corruption. If you
are running the labscript suite on a single computer, you can leave this as 'localhost'
and not take any further action. Otherwise, choose one of your computers—preferably one
that is likely to be reliably on all the time and not under very high load—and enter its
IP address or hostname here. All computers that might access the same shot files (i.e.
all that have been configured to use the same shared drive for shot files) must be
configured to use the same zlock server, otherwise there is a risk of data corruption.
See below for how to start the zlock server on the computer in question

`[programs]/text_editor` This is the command or path to the text editor that will be
launched when you click buttons in labscript suite programs to edit labscript experiment
files or your connection table. For example, you might set it to `C:\Program
Files\Sublime Text 3\sublime_text.exe` on windows or `subl` on Unix. You normally don't
need to modify `text_editor_arguments`, but you can if you wish to pass additional
command line arguments to the text editor when it is launched.

`[programs]/hdf5_viewer` This is the command or path to the HDF viewer executable. You
might set it to for example
`C:\Users\<your_username>\AppData\Local\HDF_Group\HDFView\3.1.0\hdfview.bat` on windows,
or `hdfview` or `hdfview.bat` on Unix, depending on how/where you installed HDFview to
(the above path is the default install location for HDFview 3.1.0 on Windows). This will
be used to open a HDF5 file for viewing when, for example, double clicking a shot file
in `lyse`.

7. Start the zlock server
-------------------------
On the computer that you have decided to run the zlock server, from the command prompt
(or Anaconda Prompt), run:
```
python -m labscript_utils.zlock
```
That's it! A zlock server is now running on that computer. You may wish to automate
starting the zlock server when the computer starts, and/or create a batch file to run
the above. In either case, if using anaconda on Windows, the batch file will need to
activate the conda environment first, which will look something like this:
```
CALL C:\Users\<your_user_name>\AppData\Local\Continuum\anaconda3\condabin\conda.bat activate
start cmd /k python -m labscript_utils.zlock
```
where `<your_user_name>` is replaced with your username. The above method of activating
conda from within a batch file is current as of conda 4.6.11 (April 2019), but may
change in the future, so if it does not work, you may wish to search for instructions
specific to your version of conda.

Note: if a labscript program runs and sees that the zlock server is supposed to be on
that computer, but that the server is not running, it will start a zlock server running
in the background (this is why you do not need to start zlock manually if only using one
computer). So if you forget to start the zlock server before starting other programs,
but then remember and start the zlock server manually, you may get an error that 'the
port is already in use'. You can just ignore this and rest assured that zlock is already
running. However, if you want to have a visible terminal for zlock, you will need to
kill the background one using the task manager, or reboot.

A general note about task management: All labscript suite processes will appear in
Windows' task manager as "Python". To see which is which, if you need to end them, in
Windows 8 or 10, go to the 'details' tab of the Task manager, right click on one of the
column headers and click "Select Columns". Select the "Command line" column. Then you
will be able to see in this column which Python process corresponds to which labscript
suite component. In Windows 7, you can view this information in a tooltip when hovering
over the task.

8. Create and compile a connection table
----------------------------------------

In your labconfig file, one of the configuration settings is
`[paths]/connection_table_py`. This is the location of the python file containing your
'connection table'. A connection table is an experiment script, written in Python,
containing a description of the devices in use in your experiment and how they are
connected to each other. It is a valid experiment script, and in principle could
compiled and run just like any other labscript experiment script. Instead of actually
running it however, when this experiment script is compiled, the resulting HDF5 file is
used by BLACS to know what hardware is in use in the experiment so that it can set up
the appropriate device tabs in its user interface and initialise communication with the
devices in question.

If you did not change the labconfig setting, then labscript suite programs will expect
your connection table .py file to be called `connectiontable.py`, and to be located
within your experiment-specific 'labscriptlib' folder:
`<labscript_suite_directory>/userlib/labscriptlib/<experiment_name>/`. Create this file,
including the `<experiment_name>` parent directory, and edit it to make your first
connection table. Here is a minimal connection table .py file that can get you started,
though describing how to make a complete and realistic connection table is outside the
scope of this getting-started guide:

```python
from labscript import *
from labscript_devices.PulseBlaster import PulseBlaster

PulseBlaster('pulseblaster_0')

if __name__ == '__main__':
    start()
    stop(1)
```

This connection table imports the PulseBlaster labscript device class from the
`labscript_devices` Python package, creates an instance of it, specifying its name, and
then calls `start()` and `stop()`, which are functions from the `labscript` Python
package. Calling these two functions is necessary to tell the `labscript` module to save
the details of this experiment script to a HDF5 file, even though that file will only be
used for the description of devices contained within it, and not for running any
experiment (which in this case would be an experiment of duration 1 second, that does
nothing). By wrapping the `start()` and `stop()` functions in the `if __name__ ==
'__main'__` check, we ensure that those functions only run if this code is executed
directly by Python, and not if this code is imported by another Python script. This is
useful since you may wish to import this connection table file in other experiment
scripts. 

Note: there are at present two common practices among labscript users as to whether to
have a single connection table .py file that all experiment scripts import, or whether
to duplicate, within each experiment script, the bits of the connection table that are
relevant to that specific script. Both practices have their pros and cons. Using a
common connection table means that one need not duplicate code, which can be
time-consuming and prone to human error. However, duplicating the code into each
experiment script means that each script has a self-contained record of the devices it
requires and their configuration, and any devices that are in your lab but not in use by
a specific script will not need to functional in order for the script to run (BLACS will
simply skip over these devices when it comes time to run an experiment). The choice is
yours, but if you do decide to use a common connection table that is imported from other
scripts, instead of importing it normally, you will need to use the function
`labscript_utils.import_or_reload`, like so:

```python
from labscript_utils import import_or_reload
import_or_reload('labscriptlib.<experiment_name>.connectiontable')

# other imports and experiment script continue here
```

This is because, when runmanager compiles shots, it runs the experiment script file
multiple times within the same Python process. Python caches imports, such that if you
import a module twice, the second time the imported code does not actually run. Because
of the way labscript works, the code in the connection table must run ever time a shot
file runs. The `import_or_reload()` function ensures this. Readers familiar with Python
may realise that one could achieve the same result by putting the connection table code
within a function, and calling that function within the `if __name__ == '__main__'` of
`connectiontable.py` block as well as at the top of experiment scripts. This will work
too.

Once you have created your connection table .py file, it needs to be compiled to produce
the connection table HDF5 file. You could do this using runmanager, and then manually
rename the resulting shot file and move it to the correct location, however a quicker
way is using BLACS. Start BLACS from the start menu shortcut (or with `python -m blacs`
from a terminal if on unix). BLACS will complain with an error that it cannot open the
connection table HDF5 file. Dismiss this error, and from the 'connection table' menu,
select 'recompile'. This will open a dialog box from which you can compile your
connection table. Once it has successfully compiled, click the button to restart BLACS.
BLACS will then restart and load the device interfaces appropriate for the set of
hardware described by your connection table.

If your connection table requires 'globals' in order to compile—for example, calibration
quantities used for unit conversion (so that one can use custom units to control devices
in BLACS in manual mode), you may configure BLACS to compile the connection table using
specified globals files, settable by going to connection table > select globals in
BLACS. It is a good idea to store globals required by the connection table in a separate
file than those used in the rest of the experiment, and to compile the connection table
with your 'connection table globals' file, and to compile regular shots with both this
file and another file (or several files) containing globals used in the experiment
logic. This allows BLACS to prompt you to recompile the connection table if the relevant
globals change, without the prompt giving false positives whenever unrelated globals are
modified.
 

9. General advice
-----------------

The labscript suite is now installed and configured on your computer/computers. You may
launch programs from the start menu items in Windows, or from a terminal (on any
operating system) using `python -m <program_name>`, where `<program_name>` is `blacs`,
`runmanager`, `lyse`, or `runviewer`. Launching from a terminal can be useful to see
additional output if something is going wrong, such as a program crashing.

The labscript suite installer creates a number of folders that it adds to the Python
search path, and as such, python code placed in these folders may be imported by other
Python code, whether it is an experiment script, an analysis routine, or something else.
These folders are the `userlib` folder within the labscript suite installation
directory, and the `pythonlib` folder within that. Typical usage is to place code that
you wish to re-use in experiment scripts within
`userlib/labscriptlib/<experiment_name>`, or, if the code is not specific to one
experiment, within `userlib/labscriptlib/common/`. Then such code may be imported as:

```python
from labscriptlib.common.some_module import some_function
from labscriptlib.<experiment_name>.some_other_module import some_experiment_specific_function
```

Similarly, code re-used by analysis routines can be placed in the analysislib subfolder,
following the same pattern of an experiment-specific subdirectory and a 'common'
subdirectory.

The labscriptlib and analysislib subdirectories are also the default locations for new
experiment scripts and analysis routines respectively.

The `pythonlib` subfolder is added directly to the Python search path, so code within it
can be imported by name without the `pythonlib` prefix. This is a place to put modules
used perhaps both by experiment scripts and analysis routines, or by other code
altogether that happens to run in your laboratory.

When code is organised in this way, a laboratory or research group with multiple
experiments may have a single `userlib` folder, under version control or synchronised
across computers using Google drive or similar, without conflict, whilst still sharing
common components. It takes some discipline to keep things organised in this way, but is
worth learning how to use version control (for example mercurial or git) for the benefit
it provides in synchronising and tracking the history of changes to your experiment code
over time.

10. Before you go...
--------------------
The labscript suite is an open-source, community project. Please contribute back! The
open-source nature of the project is what makes it viable in the long run, but this
relies on fixes and other work being shared. 'Upstreaming' (contributing back) your
changes also means that other work on the labscript suite will be building on top of
code that already contains your changes, avoiding a situation in which the code changes
to a point where it is difficult to update to a newer version of the labscript suite
whilst retaining custom changes you have made. Upstreaming your changes is the best way
to avoid being stuck on a 'legacy' version of the labscript suite as it continues to
improve in the future.

If you find a bug, please report it to the relevant subproject here on bitbucket, or if
you are not sure, send an email on the [mailing
list](http://groups.google.com/group/labscriptsuite). We may also make announcements on
the mailing list from time to time, and it is a good way to be informed of issues others
are having and their solutions, so you may wish to subscribe to the mailing list
regardless.

If you fix an issue in the labscript suite, enhance it in a way that might be generally
useful, or implement support for a device others might use, the best way to contribute
it back is by making a 'pull request' on bitbucket to the relevant subproject. If you
are having trouble working out how to do this, ask for help on the mailing list and we
will try to help.

Finally, if you use the labscript suite in work leading to a scientific publication, do
not forget to cite our article, *A scripted control system for autonomous hardware-timed
experiments*, [Review of Scientific Instruments 84,
085111](http://aip.scitation.org/doi/10.1063/1.4817213) (2013).
[arXiv:1303.0080](http://arxiv.org/abs/1303.0080). Whilst it is not necessary to cite
the software in every publication resulting from an apparatus that uses the labscript
suite, it is reasonable to cite it in any context where you are otherwise describing the
technical details of your apparatus.


Other commands
==============

The above instructions should be used to install the labscript suite.
However, the install script can also be used to uninstall a previously made
installation, and other less-commonly-needed functionality. 

usage:
    python setup.py (install | uninstall | build | dist | clean)


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
