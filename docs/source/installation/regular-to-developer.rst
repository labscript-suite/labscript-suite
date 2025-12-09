Migrating a Regular Installation to a Developer Installation
=================================================================

If you are using a regular installation of labscript and would like to make edits to a component,
you will need to convert that component to a developer installation.
Converting a regular installation (pip or anaconda) to a developer installation is fairly simple.
This document will assume you have a functioning regular installation
and would like to install `labscript-devices` in developer mode to make edits.
The following procedure applies to any labscript component,
so converting the entire installation to developer mode means repeating these steps for each component.

Clone the repository
--------------------

For either type of installation, you must first create a local copy of the source code that you would like to edit.
This is done by following the first two steps of the :doc:`Anaconda developer installation <developer-anaconda>`.
If brief, you should create a fork of the labscript-suite repository that you want to develop (done online through github),
then use git to clone a local copy to your computer.
In this document, it is assumed you have cloned the repository to the `C:\\wkheisenberg\\labscript-suite\\` directory.

.. attention:: 

     Recent `changes in Github's online interface <https://github.blog/changelog/2022-07-27-you-can-now-fork-a-repo-and-copy-only-the-default-branch/>`_
     mean that version tags are not copied into new forks by default.
     These tags are necessary to properly resolve component versions when installing from your fork.
     To override this behavior, ensure the `Copy master branch only` checkbox is **unchecked**.

     .. image:: Copymasterbranchonly.png
          :width: 400
          :align: center
          :alt: Unselect this option to copy version tags too 

Converting a Python Package Index installation
----------------------------------------------

This section assumes you followed the :doc:`regular installation directions using pip <regular-pypi>`.

#. Activate the virtual enviornment with your labscript installation (this step is OS specific)

   .. code-block:: console

        C:\Users\wkheisenberg\labscript-suite> .venv\Scripts\activate

#. Install the local editable copy of the component.

   .. code-block:: console

        C:\Users\wkheisenberg\labscript-suite> pip install -e labscript-devices

   Note that packages installed in editable mode do not typically need to be re-installed when the source code is updated.
   In other words, updating the component is as simple as pulling changes into the local repository.

   .. tip::

        Multiple components can be updated to a developer installation at the same time by joining their installation commands,
        as is done in the developer installation instructions.

        .. code-block:: console

            pip install -e labscript-devices -e labscript

Converting an Anaconda Installation
-----------------------------------

This section assumes you followed the :doc:`regular installation directions using conda <regular-anaconda>`.

#. Activate the conda environment with your labscript installation from the Anaconda Prompt.

   .. code-block:: console

        (base) C:\Users\wkheisenberg> conda activate labscript

#. Force remove the conda package of the component.

   .. code-block:: console

        (labscript) C:\Users\wkheisenberg> conda remove --force labscript-devices

#. Install the local editable copy of the component.

   .. code-block:: console

        (labscript) C:\Users\wkheisenberg> pip install -e labscript-devices

   Note that packages installed in editable mode do not typically need to be re-installed when the source code is updated.
   In other words, updating the component is as simple as pulling changes into the local repository.

   .. tip::

        This can be an effective method to perform a developer installation in a conda environment without needed `setuptools-conda`.
        In short, the regular install will capture all dependencies via the meta-package installation,
        allowing for sensible developer installation via pip following the conversion steps above.

   .. warning::

        Mixing pip and conda installed packages requires some care.
        In particular, you will want to ensure that all dependencies are already installed via conda before doing the editable installation,
        otherwise unmet dependencies will be installed with pip
        which makes installing other conda packages much more difficult.
        In general, these dependencies should have been installed during a regular installation,
        but updated dependencies in the working branch that haven't been released can lead to this behavior.

