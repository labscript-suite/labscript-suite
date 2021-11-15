Configuring the *labscript suite* for first run
===============================================

Once installed, the **labscript suite** requires some manual configuration.
The following sections detail the required steps necessary for all components of the suite to run for the first time.
Further details on how to use each component can be found in the documentation for that component via the :doc:`*labscript suite* components <components>` link in the left side bar.

The *labconfig.ini* File
------------------------

Before running any **labscript-suite** components after a fresh installation, you should first open the automatically generated labconfig file and modify some of its default settings to match your needs.
This file is found in the user space `labscript-suite/labconfig` directory created by the `labscript-profile-create` command of the installation process.
This directory is, by default, located at the top level of the user's directory.
The labconfig file will be named after your system's name.
So if your system hostname is `heisenberg`, the labconfig file will be named `heisenberg.ini`.
This directory will also contain a copy of the default labconfig file as `example.ini`.
Only changes made to the labconfig file named after your system will have any effect.

The current contents of the default labconfig file are available :doc:`here <labscript-utils:labconfig>`.

Configuration
*************

Many of the options in this file do not need to be changed, but a few things should be changed before running any **labscript-suite** module the first time.
Once the appropriate changes have been made, save the file.

* `[DEFAULT]`

  * `apparatus_name` should be set to a name describing the experiment.
     It should not have spaces.
     This name is used to create sub-directories within the various **labscript-suite** directories where the various shots and scripts will be stored.
     If these sub-directories do not exist, the suite will create them and populate them with the bare minimum of requirements to function.
     The relative paths for the items are described by the other keys in the `DEFAULT` section, and can be modified if desired.
     Note that while multiple apparatus names can exist for the same installation, only one can be used at a time.
     In order for a changed `apparatus_name` to take effect, you will need to reload **labscript-suite** components.
  * `shared_drive` is the path to where the individual shots are stored and accessed by the **labscript-suite** components.
     If your installation spreads the **labscript-suite** components across multiple separate computers, set this value to the path to the common network location where shots are stored.
     This allows all components seamless access to the same shots.

* `[servers]`
  
  * `zlock` should be set to the network address of the computer that runs the common zlock server.
     In an installation spanning multiple computers, only one computer runs the zlock server.
     This ensures only one device can access files at a time.
     At least one computer in an installation must be set to `localhost`, indicating it is the zlock server.
  * `runmanager` should be set to the network address of the computer that runs a common runmanager server for compiling shots.
     Rules to set it are the same as `zlock`.
     It can be the same computer as the zlock server.

* `[security]`

  * `shared_secret` should be set to the full path to the zprocess secret key for encryption.
     The default installation will create this file for you, place it in the correct folder, and update the reference in the config file to reflect its automatically generated name.
     In a multi-computer installation, all computers will need access to the same secret key in order to commuicate with encryption.
     Each computer's labconfig file will need to be updated to point to the same key file.
  * `allow_insecure` can be added to this section and set to `True` to disable secure communications.
     This value will need to be the same across all computers in a multi-computer setup.

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
The defaul location is in the `apparatus_name/labscriptlib` sub-folder of the userlib.

A very simple connection table that defines a PrawnBlaster pseudoclock and an NI DAQ with two named channels is as follows.

.. code-block:: python

   from labscript import *

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

      start(0)

      stop(1)

More specific examples of connection tables can be fould in the **labscript-devices** repository :doc:`here <labscript-devices:ex_conn_tables>`.

.. note:: 

	BLACS will instantiate a control for all available hardware channels on a device, even if they are not specifically named in the connection table.
	However, connection tables with identical devices but different names for the attached channels are considered unique by **labscript**.
	Remember that the connection table used by an individual shot must be a subset of the connection table used by BLACS, so chaning channel names will require re-compiling the connection table.

With the `connection_table.py` file written, you will then need to compile it using runmanager.
Take the output compiled file and save it by the name and in the location specified by the `connection_table_h5` key of the labconfig file.
The default name of the file is `connection_table.h5` and it is located in the experiment shot storage for `apparatus_name`.

With the connection table in place, you can now open BLACS.
Changes to `connection_table.py` will now be recognized by BLACS, and BLACS will prompt you to recompile the connection table using a prompt within BLACS itself.
 