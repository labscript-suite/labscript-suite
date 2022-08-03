Troubleshooting
===============

This section contains general tips for troubleshooting issues with the **labscript-suite**.
Other good places to look for help include the `list serve <https://groups.google.com/g/labscriptsuite?pli=1>`_
as well as open/closed issues and pull requests on `github <https://github.com/labscript-suite>`_.
If you cannot find the help you need, feel free to send a message on the list serve or create a github issue in the relevant repository.

I clicked the launch icon for *component* and nothing happened!
---------------------------------------------------------------

This occurs when there is a stopping error that prevents the GUI from loading (when standard error handling would take over).
In order to see the error that is preventing the component from launching, you should launch the program from the command line.
To do so, run the following command in the python environment you installed the **labscript-suite** into.

.. code-block:: shell

    python -m <component>

Replace `<component>` with the name of the module you wish to run (i.e. `runmanager`, `blacs`, `lyse`, or `runviewer`).
The blocking error should print to the console you ran the command in.
You can then use that error to isolate the problem and find the appropriate solution.

`zlock`/ `zlog` is preventing *component* from loading!
-------------------------------------------------------

:mod:`zlock <labscript-utils:labscript_utils.zlock>` and :mod:`zlog <labscript-utils:labscript_utils.zlog>` are the **labscript-suite** utilities that handle file locking and log files for the suite.
They are built on the `zprocess <https://github.com/chrisjbillington/zprocess>`_ package.
Generally, they are run as background processes; automatically launched when any **labscript-suite** component first launches and left running in perpetuity.
If their :doc:`configuration <labscript-utils:labconfig>` changes or the labscript-utils/zprocess packages are updated while the background processes are running, errors often ensue.
These problems can often be fixed by restarting the background processes.
You can stop the these processes by either:

 - Restarting the host computer.
 - Killing the processes running `zlock` and `zlog` manually using a task manager.
   The processes display as a python executable.
   You can determine which python processes are running these components by inspecting their command line arguments.
 
 You restart the two processes by either starting a **labscript-suite** component or starting them by hand at the command line as described in the API documentation in *labscript-utils*.