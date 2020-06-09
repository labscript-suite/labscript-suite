Setting up a Python environment
===============================

We recommend installing the *labscript suite* (regular or developer mode) in a `virtual environment <https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments>`_.
This helps sandbox the codebase without interfering with (or being interfered with) your system Python installation, or Python environments used for other purposes.
Below we outline how to create and activate a virtual environment for Anaconda Python and other CPython distributions (which we call 'Regular' Python here).


Anaconda Python
---------------
Anaconda Python includes a `virtual environment manager <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_ as part of the `conda` executable.
Here's an example (on Windows):

.. note::

    Make sure you have opened the `Anaconda Prompt <https://docs.anaconda.com/anaconda/user-guide/getting-started/#open-anaconda-prompt>`_ on Windows (available from the Start menu).
    `conda` is not available from the standard terminal by default.
    Launching 'Anaconda Prompt' will activate the `base` conda environment.

.. warning::

    We do not recommend using the `base` conda environment for any project (*labscript suite* or otherwise).
    Working in a separate conda environment ensures any package resolution or update errors (however unlikely) are limited to that environment, and `base` is not compromised.


Quickstart
**********

.. code-block:: console

    (base) C:\> conda create -n py38 python=3.8
    (base) C:\> conda activate py38
    (py38) C:\>

Once activated, the name of the virtual environment (in this case, `py38` ) will prefix the command line.


Detailed Instructions
*********************

1. Create a virtual (conda) environment.
   Here we name it `py38` and ask conda to use Python 3.8 within the virtual environment (name and Python version are variable but these are conventional choices):

  .. code-block:: console

    (base) C:\> conda create -n py38 python=3.8


2. Activate the virtual (conda) environment:

  .. code-block:: console

    (base) C:\> conda activate py38
    (py38) C:\>


Regular Python
--------------

There are a number of ways to configure a virtual environment.
If you are unfamiliar with doing so, we recommend using the `venv module <https://docs.python.org/3/library/venv.html>`_, part of the Python Standard Library.
Here's an example (on Windows):


Quickstart
**********

.. code-block:: console

    C:\Users\wkheisenberg> mkdir labscript-suite
    C:\Users\wkheisenberg> cd labscript-suite
    C:\Users\wkheisenberg\labscript-suite> python -m venv .venv
    C:\Users\wkheisenberg\labscript-suite> .venv\Scripts\activate
    (.venv) C:\Users\wkheisenberg\labscript-suite> python -m pip install --upgrade pip setuptools wheel

Once activated, the name of the virtual environment (in this case, `.venv` ) will prefix the command line.


Detailed Instructions
*********************

1. From a new terminal, create a directory for the virtual environment and enter it. Here we use a directory named `labscript-suite` in the user's home directory, also the location of the labscript suite profile directory. You need create the virtual environment here, but it is a convenient choice.

  .. code-block:: console

    C:\Users\wkheisenberg> mkdir labscript-suite
    C:\Users\wkheisenberg> cd labscript-suite


2. Create a virtual environment.
   Here we name it `.venv`, located inside the labscript suite profile directory.

  .. code-block:: console

    C:\Users\wkheisenberg\labscript-suite> python -m venv .venv


3. Activate the virtual environment:

  .. code-block:: console

    C:\Users\wkheisenberg\labscript-suite> .venv\Scripts\activate

  .. note:: This step is OS specific, e.g. on Linux it's `source .venv/bin/activate`.

4. Update the Python package installer and other installation packages of your virtual environment.

  .. code-block:: console

    (.venv) C:\Users\wkheisenberg\labscript-suite> python -m pip install --upgrade pip setuptools wheel


Choosing an installation method
-------------------------------
Once you have a virtual environment up and running, choose from one of the following 4 installation methods:

1. :doc:`regular-pypi`;
2. :doc:`regular-anaconda`;
3. :doc:`developer-pypi`; or
4. :doc:`developer-anaconda`.
