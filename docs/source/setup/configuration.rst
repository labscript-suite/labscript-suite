Configuring the *labscript suite* for first run
===============================================

Once installed, the **labscript suite** requires some manual configuration.
The following sections detail the required steps necessary for all components of the suite to run for the first time.
Further details on how to use each component can be found in the documentation for that component via the :doc:`*labscript suite* components <../components>` link in the left side bar.

.. note::

   The `labscript-profile-create` command can perform the following mandatory configurations automatically.
   The `-n/--apparatus_name` argument allows you to set your apparatus name (which governs many install locations).
   The `-c/--compile` flag will compile the example connection table (which only defines dummy instruments and will always run).
   Using both of these arguments will allow all suite components to load with a minimal configuration that is readily customised.

The *labconfig.ini* File
------------------------

Before running any **labscript-suite** components after a fresh installation, you should first open the automatically generated labconfig file and modify some of its default settings to match your needs.
This file is found in the user space `labscript-suite/labconfig` directory created by the `labscript-profile-create` command of the installation process.
This directory is, by default, located at the top level of the user's directory.
The labconfig file is named after the computer's host name, which on macOS is the output of `scutil --get LocalHostName`.
So if your system hostname is `heisenberg`, the labconfig file will be named `heisenberg.ini`.
This directory will also contain a copy of the default labconfig file as `example.ini`.
Only changes made to the labconfig file named after your system will have any effect.

The :doc:`labconfig page of labscript-utils <labscript-utils:labconfig>` shows the default labconfig file and describes every key.

Configuration
*************

Many of the options in this file do not need to be changed, but a few things should be changed before running any **labscript-suite** module the first time.
Once the appropriate changes have been made, save the file.
The keys are described in the :ref:`list of keys <labscript-utils:labconfig:keys>` of the labconfig page.

* `[DEFAULT]` `apparatus_name`: the name of the experiment.
  `labscript-profile-create` sets it to the value of its `-n/--apparatus_name` argument, or to `example_apparatus` without that argument.
  The paths of the experiment scripts, analysis routines and shot files contain it.
  `labscript-profile-create` creates the `userlib/labscriptlib/<apparatus_name>` and `userlib/analysislib/<apparatus_name>` directories for the name that it is given.
  To change the apparatus name later, create these directories for the new name, with an `__init__.py` file in each, and restart the **labscript-suite** components.

* `[DEFAULT]` `shared_drive`: the directory that holds the shot files.
  In an installation that spans several computers, it is a network location that all of the computers can access.

* `[servers]` `zlock`: in an installation that spans several computers, the host name of the computer that runs the zlock server.

* `[servers]` `runmanager`: the host name of the computer that runs runmanager, to which the `runmanager.remote` client connects.

* `[programs]` `text_editor` and `hdf5_viewer`: the programs that open experiment scripts, analysis routines, the connection table and shot files.
  On Windows, the default labconfig file gives the paths of `VS Code <https://code.visualstudio.com/>`_ and `HDFView <https://github.com/HDFGroup/hdfview/releases>`_ that their installers use.
  Install VS Code with its user installer, and HDFView with the `HDFView-<version>-Windows.msi` file of the latest HDFView release on GitHub, or set the keys to the paths of other programs.
  If a key is empty, files are opened in the operating system's default program for the file type.

* `[security]` `shared_secret`: in an installation that spans several computers, the path of a copy of the same key file on each computer.
  `labscript-profile-create` creates a key file and sets this key.

With these configurations made, you should now be able to run any module of the **labscript-suite**, except BLACS which requires more configuration.


Initial Compile of the Connection Table
---------------------------------------

Once your installation is configured, you will need to compile a connection table for the first start-up of BLACS.
A general description of the connection table can be found :doc:`here <labscript:connection_table>`.
In short, the connection table defines the hardware devices connected to BLACS and are available for use in an experiment shot.
The connection table should be considered a super-set of devices for use in experiment shots (i.e. not all devices connected to BLACS must be used in an experiment shot run by that BLACS).

The connection table is defined by writing a `connection_table.py` file that is essentially an experiment run without any instructions.
This involves importing the specific device code and instantiating each device you wish to connect to.
At the end of the file, you will call the **labscript** functions `start` and `stop`, without any actual instructions commanded to any device in the shot.
This file must be saved as the name defined and at the location specified by the `connection_table_py` key of the labconfig file.
The default location is the `userlib/labscriptlib/<apparatus_name>` directory of the profile.

.. note::

   The `labscript-profile-create` command can be used to automatically compile the example connection table (which only populates dummy devices),
   allowing BLACS to open immediately upon install. Simply pass the `-c/--compile` flag.

A very simple connection table that defines a PrawnBlaster pseudoclock and an NI DAQ with two named channels is as follows.

.. code-block:: python

   from labscript import start, stop, AnalogOut

   # Import classes needed for the devices which will be used
   from labscript_devices.PrawnBlaster.labscript_devices import PrawnBlaster
   from labscript_devices.NI_DAQmx.models.NI_USB_6363 import NI_USB_6363

   # Create a PrawnBlaster, saved to the variable 'prawn', 
   # It will be used as the single pseudoclock that triggers other devices
   PrawnBlaster(name='prawn', com_port='COM6', num_pseudoclocks=1)

   # Create a NI USB-6363 multifunction I/O device, clocked by the PrawnBlaster
   NI_USB_6363(name='daq', MAX_name='Dev1',
               parent_device=prawn.clocklines[0], clock_terminal='/Dev1/PFI0',
               acquisition_rate=100e3)

   # Add analog output channels to the USB-6363
   AnalogOut('ao0', daq, 'ao0')
   AnalogOut('ao1', daq, 'ao1')

   # The following is standard boilerplate necessary for the file to compile
   if __name__ == '__main__':

      start()

      stop(1)

More specific examples of connection tables can be found in the **labscript-devices** repository :doc:`here <labscript-devices:ex_conn_tables>`.

.. note:: 

	BLACS will instantiate a control for all available hardware channels on a device, even if they are not specifically named in the connection table.
	However, connection tables with identical devices but different names for the attached channels are considered unique by **labscript**.
	Remember that the connection table used by an individual shot must be a subset of the connection table used by BLACS, so changing channel names will require re-compiling the connection table.

With the `connection_table.py` file written, you will then need to compile it using runmanager.
Take the output compiled file and save it by the name and in the location specified by the `connection_table_h5` key of the labconfig file.
The default name of the file is `connection_table.h5` and it is located in the experiment shot storage for `apparatus_name`.

With the connection table in place, you can now open BLACS.
Changes to `connection_table.py` will now be recognized by BLACS, and BLACS will prompt you to recompile the connection table using a prompt within BLACS itself.

Generating a new zprocess secret key
-------------------------------------------------------

To generate a zprocess secret key, navigate to the `labconfig` directory and run 

.. code-block:: console

    C:\Users\wkheisenberg\labscript-suite\labconfig> python -m zprocess.makesecret

then update the `[security]` section of the `labconfig.ini` to use the new file.
