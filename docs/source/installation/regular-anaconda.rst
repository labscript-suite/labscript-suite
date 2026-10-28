Regular installation (Anaconda Cloud)
=====================================

We recommend a :doc:`regular installation from PyPI <regular-pypi>` instead; read the conda caveats in :doc:`index` first.

In this example, we will use an existing conda environment named `labscript`.
Skip the first line/step if continuing on from the instructions to :ref:`set up this environment <installation/setting-up-an-environment:Anaconda Python>`.


Quick start
-----------

.. code-block:: console

    (base) C:\> conda activate labscript
    (labscript) C:\> conda config --env --add channels conda-forge
    (labscript) C:\> conda config --env --add channels labscript-suite
    (labscript) C:\> conda config --env --set channel_priority strict
    (labscript) C:\> conda install labscript-suite pyside6
    (labscript) C:\> labscript-profile-create [-n my_apparatus_name] [-c]
    (labscript) C:\> desktop-app install blacs lyse runmanager runviewer


Detailed instructions
---------------------

1. Activate the conda environment from the `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_.

  .. code-block:: console

    (base) C:\> conda activate labscript

2. Add the conda-forge channel and then the `labscript-suite` channel on `Anaconda Cloud <https://anaconda.org/labscript-suite>`_ to the current conda environment, and set strict channel priority:

  .. code-block:: console

    (labscript) C:\> conda config --env --add channels conda-forge
    (labscript) C:\> conda config --env --add channels labscript-suite
    (labscript) C:\> conda config --env --set channel_priority strict

  Conda then installs the *labscript suite* packages from the `labscript-suite` channel and every other package from conda-forge.
  On Windows, the `pyzmq` package of Anaconda's default channels is built without CurveZMQ support, which the *labscript suite* uses to encrypt and authenticate communication between its programs; with that package, `labscript-profile-create` fails with the error ``CurveNotSupported``.
  conda-forge also has an older `desktop-app` package than the `labscript-suite` channel, so the `labscript-suite` channel must be added last, which gives it the highest priority.
  A conda installation that uses only conda-forge, such as `Miniforge <https://conda-forge.org/download/>`_, needs the same three commands.

3. Install the meta-package (`labscript-suite`) and PySide6 (`pyside6`), the Python bindings for the Qt GUI toolkit.
   This will install blacs, labscript, labscript-devices, labscript-utils, lyse, runmanager, runviewer, and all dependencies:

  .. code-block:: console

    (labscript) C:\> conda install labscript-suite pyside6

  The *labscript suite* also works with the PyQt6 and PyQt5 bindings instead of PySide6, which are the conda-forge packages `pyqt6` and `pyqt`.
  If more than one binding is installed, the applications use PyQt5, then PySide6, then PyQt6, unless the environment variable `QT_ENV` is set to `PyQt5`, `PySide6` or `PyQt6`.


4. Create (or populate) a profile directory in your home directory (the location of user data; see :doc:`/reference/changes`).
   Optional arguments allow for minimal control of default installation parameters to allow for all components to load.
   `-n/--apparatus_name` allows for setting a custom apparatus name for the experiment.
   The apparatus name must be a valid Python identifier (letters, digits and underscores, not starting with a digit), because it becomes the name of an importable package under `labscriptlib`.
   `-c/--compile` compiles the example connection table (with dummy devices) so BLACS will launch.
   Using these arguments makes :doc:`initial configuration </setup/configuration>` of the suite much simpler.

  .. code-block:: console

    (labscript) C:\> labscript-profile-create [-n my_apparatus_name] [-c]


5. (Optional) Create shortcuts for the GUI applications (blacs, lyse, runmanager, and runviewer) and place them in the start-menu (or non-Windows OS equivalent).

   .. code-block:: console

       (labscript) C:\> desktop-app install blacs lyse runmanager runviewer


   These will be named, e.g. 'runmanager – the labcript suite (labscript)' which when clicked on will:

   * Launch the application without a terminal window, using the virtual environment the above command was called in.
   * Display the application with an application-specific shortcut in the taskbar (which can be pinned, like any other desktop application).

.. note::

   Conda environments named anything other than `base` will be included in the name of the shortcut, e.g. 'runmanager – the labscript suite (labscript)' for a conda environment named `labscript`.

Alternatively, you can launch the applications from the Anaconda Prompt in the , e.g.

.. code-block:: console

    (labscript) C:\> runmanager


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

    (labscript) C:\> conda update -c labscript-suite runmanager


To upgrade to a pre-release version, you can use the test label:

.. code-block:: console

    (labscript) C:\> conda update -c labscript-suite/label/test runmanager


If updating multiple components, use a single |conda-update|_ command to assist dependency resolution:

.. code-block:: console

    (labscript) C:\> conda update -c labscript-suite labscript lyse runmanager


You can also update (or downgrade) to a specific version:

.. code-block:: console

    (labscript) C:\> conda update runmanager==2.5.0


.. |conda-update| replace:: ``conda update``
.. _conda-update: https://docs.conda.io/projects/conda/en/latest/commands/update.html
