Setting up a Python environment
===============================

We recommend installing labscript (regular or developer mode) in a `virtual environment <https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments>`_.
This helps sandbox the codebase without interfering with (or being interfered with) your system Python installation, or Python environments used for other purposes.
We'll show the most common ways below for each of the Python installation options we've previously suggested.


Anaconda Python
---------------
Anaconda Python includes a virtual environment manager as part of the `conda` executable.
Here is an example (on Windows):

.. note:: Make sure you have opened the "Anaconda Prompt" on Windows (available in your start menu). 
         `conda` is not available from the standard terminal by default.
         Launching "Anaconda Prompt" will activate the `base` conda environment.

.. warning:: While the `base` conda environment is technically a Python environment, we do not recommend using it for any project (labscript suite or otherwise).
            It is possible (although unlikely) to break your base Anaconda install by pulling in packages from 3rd party channels (such as conda-forge), requiring a complete reinstallation of Anaconda Python.
            Working in a separate virtual environment ensures damage from such events (however unlikely) are limited to one virtual environment.

Quickstart
**********

.. code-block:: console

    (base) C:\> mkdir labscript-suite
    (base) C:\> cd labscript-suite
    (base) C:\labscript-suite> conda create -n labscript_suite_py38 python=3.8 
    (base) C:\labscript-suite> conda activate labscript_suite_py38
    (labscript_suite_py38) C:\labscript-suite> 

Once activated, the name of the virtual environment (in this case, `labscript_suite_py38` ) will prefix the command line.


Detailed Instructions
*********************

1. From a new terminal, create the installation directory and enter it. Here we use `C:\labscript-suite` but this can be whatever you like:

  .. code-block:: console

    (base) C:\> mkdir labscript-suite
    (base) C:\> cd labscript-suite


2. Create a virtual environment. 
   Here we name it `labscript_suite_py38` and ask conda to use Python 3.8 within the virtual environment (name and python version are also variable but these are conventional choices):

  .. code-block:: console

    (base) C:\labscript-suite> conda create -n labscript_suite_py38 python=3.8 
    

3. Activate the virtual environment:

  .. code-block:: console

    (base) C:\labscript-suite> conda activate labscript_suite_py38
    (labscript_suite_py38) C:\labscript-suite> 


Regular Python
--------------

There are a number of ways to configure a virtual environment.
If you are unfamiliar with doing so, we recommend using the `venv module <https://docs.python.org/3/library/venv.html>`_, part of the Python Standard Library.
Here's an example (on Windows):


Quickstart
**********

.. code-block:: console

    C:\> mkdir labscript-suite
    C:\> cd labscript-suite
    C:\labscript-suite> python -m venv .venv
    C:\labscript-suite> .venv\Scripts\activate
    (.venv) C:\labscript-suite> python -m pip install --upgrade pip setuptools wheel

Once activated, the name of the virtual environment (in this case, `.venv` ) will prefix the command line.

Detailed Instructions
*********************

1. From a new terminal, create the installation directory and enter it. Here we use `C:\labscript-suite` but this can be whatever you like:

  .. code-block:: console

    C:\> mkdir labscript-suite
    C:\> cd labscript-suite
    

2. Create a virtual environment. 
   Here we name it `.venv`, located inside the installation directory (name and location are also variable but these are conventional choices).

  .. code-block:: console

    C:\labscript-suite> python -m venv .venv
    

3. Activate the virtual environment:

  .. code-block:: console

    C:\labscript-suite> .venv\Scripts\activate

  .. note:: This step is OS specific, e.g. on Linux it's `source .venv/bin/activate`.

4. Update the Python package installer and other installation packages of your virtual environment.

  .. code-block:: console

    (.venv) C:\labscript-suite> python -m pip install --upgrade pip setuptools wheel

Choosing an installation method
-------------------------------
Once you have a virtual environment up and running, choose from one of the following 4 installation methods:

1. :doc:`regular-pypi`,
2. :doc:`regular-anaconda`,
3. :doc:`developer-pypi`, or
4. :doc:`developer-anaconda`.
