Setting up the environment
==========================

The build environment generally requires a full **labscript-suite** installation, with a few extra dependencies.
The simplest method is to use the environment of an existing, functioning installation and install the build dependencies.
If you do not want to install the docs dependencies into a working environment of an experiment, 
or wish the develop docs on a system that does not control an experiment,
you can create a new environment.

.. note::

	These instructions assume you have generally followed the installation instructions for a developer **labscript-suite** installation,
	using either the :doc:`pip </installation/developer-pypi>` or :doc:`anaconda </installation/developer-anaconda>` method.

Install build dependencies
--------------------------

If you have an existing, functioning environment for using the **labscript-suite**, you can configure it to build docs by simply installing the docs dependencies found in the `setup.cfg` file of each repository. 
For a functioning **labscript** environment, the only additional dependencies should be `sphinx`, `sphinx-rtd-theme`, `recommonmark`, and `m2r`.

The versions pinned in the `setup.cfg` file will be the versions of these packages that are used by Read the Docs when building the documentation.
In order to get an accurate reproduction of what the online docs look like, you should ensure the versions you install match the pins.

Once these dependencies are installed in your **labscript** environment, you are ready to build the docs.

Using a cloned environment
--------------------------

If you have an existing, functioning **labscript** environment, but do not want to install the many build dependecies into it, you can instead build the docs using a cloned copy of the functioning environment.
You clone a conda enviroment using

.. code-block:: bash

	conda create -n labscript-sphinx -c labscript

Here we clone an existing `labscript` conda environment into a new environment `labscript-sphinx`.
This new enviroment will be an exact duplicate of the original at the time of cloning.
Changes in one environment will not affect the other.

Once the new environment is created, you can activate it then install the dependencies for the docs as described above.

When using this method, both enviroments will use the same installation of the **labscript-suite**.

Using a new environment
-----------------------

If you desire to build the docs on a computer without an existing **labscript-suite** installation, you will need to first install the suite using one of the developer installation methods described :doc:`here </installation/index>`.
Once installed, follow the directions above to install the docs dependencies into the environment.

.. note::

	The normal installation steps to create a labscript profile and the launcher shortcuts should not be necessary when only building docs.

This installation method should also be used if you desire to develop documentation in local repositories separate from an existing installation (i.e. having two environments using different installations of the **labscript-suite**).
This can be desirable if you want to avoid docs dependencies in a function environment *and* want to isolate local changes for a functioning experiment from documentation developement.