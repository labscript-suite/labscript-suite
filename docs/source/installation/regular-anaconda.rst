Regular installation (Anaconda Cloud)
=====================================

In this example, we will use an existing conda environment named `py38`.
Skip the first line/step if continuing on from the instructions to :ref:`set up this environment <installation/setting-up-an-environment:Anaconda Python>`.


Quick start
-----------

.. code-block:: console

    (base) C:\> conda activate py38
    (base) C:\> conda config --env --add channels labscript-suite
    (py38) C:\> conda install labscript-suite pyqt
    (py38) C:\> labscript-profile-create
    (py38) C:\> desktop-app install blacs lyse runmanager runviewer


Detailed instructions
---------------------

1. Activate the conda environment from the `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_.

  .. code-block:: console

    (base) C:\> conda activate py38

2. Add the `labscript-suite` channel on `Anaconda Cloud <https://anaconda.org/labscript-suite>`_ to the current conda environment:

  .. code-block:: console

    (py38) C:\> conda config --env --add channels labscript-suite

3. Install the meta-package (`labscript-suite`) and bindings to the GUI toolkit (`pyqt`) from Anaconda Cloud.
   This will install blacs, labscript, labscript-devices, labscript-utils, lyse, runmanager, runviewer, and all dependencies:

  .. code-block:: console

    (py38) C:\> conda install labscript-suite pyqt


4. Create a profile directory in your home directory (the location of user data; see :doc:`/changes`):

  .. code-block:: console

    (py38) C:\> labscript-profile-create


5. (Optional) Create shortcuts for the GUI applications (blacs, lyse, runmanager, and runviewer) and place them in the start-menu (or non-Windows OS equivalent).

   .. code-block:: console

       (py38) C:\> desktop-app install blacs lyse runmanager runviewer


   These will be named, e.g. 'runmanager – the labcript suite (py38)' which when clicked on will:

   * Launch the application without a terminal window, using the virtual environment the above command was called in.
   * Display the application with an application-specific shortcut in the taskbar (which can be pinned, like any other desktop application).

.. note::

   Conda environments named anything other than `base` will be included in the name of the shortcut, e.g. 'runmanager – the labscript suite (py38)' for a conda environment named `py38`.

Alternatively, you can launch the applications from the Anaconda Prompt in the , e.g.

.. code-block:: console

    (py38) C:\> runmanager


This will print debugging information to the console.

To launch the applications detached from the console, suffix the application name with `-gui`, e.g.

.. code-block:: console

    (.venv) C:\> runmanager-gui


.. note::

    * You must have activated the conda environment in which the *labscript suite* was installed to use these commands.
    * For the `-gui` entry points to function in Anaconda Python, Step 5 (above) must be completed.


Updating a regular installation
-------------------------------

Individual components of the labscript suite can be updated using the |conda-update|_ command. For example:

.. code-block:: console

    (py38) C:\> conda update -c labscript-suite runmanager


To upgrade to a pre-release version, you can use the test label:

.. code-block:: console

    (py38) C:\> conda upadte -c labscript-suite/label/test runmanager


If updating multiple components, use a single |conda-update|_ command to assist dependency resolution:

.. code-block:: console

    (py38) C:\> conda update -c labscript-suite labscript lyse runmanager


You can also update (or downgrade) to a specific version:

.. code-block:: console

    (py38) C:\> conda update runmanager==2.5.0


.. |conda-update| replace:: ``conda update``
.. _conda-update: https://docs.conda.io/projects/conda/en/latest/commands/update.html
