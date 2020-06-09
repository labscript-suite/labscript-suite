Regular installation (Python Package Index)
===========================================

In this example, we will use an existing virtual environment named `.venv` located in `C:\Users\wkheisenberg\labscript-suite`.
Skip the first two lines/steps if continuing on from the instructions to :ref:`set up this environment <installation/setting-up-an-environment:Regular Python>`.


Quick start
-----------

.. code-block:: console

    C:\Users\wkheisenberg\labscript-suite> .venv\Scripts\activate
    (.venv) C:\Users\wkheisenberg\labscript-suite> python -m pip install --upgrade pip setuptools wheel
    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install labscript-suite
    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install PyQt5
    (.venv) C:\Users\wkheisenberg\labscript-suite> labscript-profile-create
    (.venv) C:\Users\wkheisenberg\labscript-suite> desktop-app install blacs lyse runmanager runviewer


Detailed instructions
---------------------

1. Activate the virtual environment (this step is OS specific, e.g. on Linux it's `source .venv/bin/activate`).

  .. code-block:: console

    C:\Users\wkheisenberg\labscript-suite> .venv\Scripts\activate


2. Update the Python package installer and other installation packages of your virtual environment.

  .. code-block:: console

    (.venv) C:\Users\wkheisenberg\labscript-suite> python -m pip install --upgrade pip setuptools wheel


3. Install the meta-package (`labscript-suite`) from PyPI.
   This will install blacs, labscript, labscript-devices, labscript-utils, lyse, runmanager, runviewer, and all dependencies:

  .. code-block:: console

    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install labscript-suite


4. Install PyQt5, the bindings to the GUI toolkit (not installed above for licensing reasons):

  .. code-block:: console

    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install PyQt5


5. Create (or populate) a profile directory in your home directory (the location of user data; see :doc:`/changes`):

  .. code-block:: console

    (.venv) C:\Users\wkheisenberg\labscript-suite> labscript-profile-create


6. (Optional) Create shortcuts for the GUI applications (blacs, lyse, runmanager, and runviewer) and place them in the start-menu (or non-Windows OS equivalent).

   .. code-block:: console

       (.venv) C:\Users\wkheisenberg\labscript-suite> desktop-app install blacs lyse runmanager runviewer


   These will be named, e.g. 'runmanager – the labcript suite' which when clicked on will:

   * Launch the application without a terminal window, using the virtual environment the above command was called in.
   * Display the application with an application-specific shortcut in the taskbar (which can be pinned, like any other desktop application).

.. note::

    Virtual environments named anything other than `.venv` will be included in the name of the shortcut, e.g. 'runmanager – the labscript suite (py38)' for a virtual environment named `py38`.

Alternatively, you can launch the applications from a terminal, e.g.

.. code-block:: console

    (.venv) C:\> runmanager


This will print debugging information to the console.

To launch the applications detached from the console, suffix the application name with `-gui`, e.g.

.. code-block:: console

    (.venv) C:\> runmanager-gui


.. note:: You must have activated the virtual environment in which the *labscript suite* was installed to use these commands.


Updating a regular installation
-------------------------------

Individual components of the labscript suite can be updated using the `--upgrade` (`-U`) flag of `pip`. For example:

.. code-block:: console

    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install -U runmanager


To upgrade to a pre-release version, you can use the `--pre` (pre-relase) flag:

.. code-block:: console

    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install -U --pre runmanager


If updating multiple components, use a single `pip install` command to assist dependency resolution:

.. code-block:: console

    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install -U labscript lyse runmanager


You can also update (or downgrade) to a specific version:

.. code-block:: console

    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install runmanager==2.5.0


.. TODO::

    Development versions will be suffixed with `devN`, i.e.

    .. code-block:: console

        (.venv) C:\Users\wkheisenberg\labscript-suite> pip install -i https://test.pypi.org/simple runmanager==2.6.0dev3
