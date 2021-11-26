Developer installation (Anaconda Cloud)
=======================================

Developer installations are useful for those who want to customise the *labscript suite*.

.. note:: You need not fork, clone, and install editable versions of all *labscript suite* repositories to customise your installation and/or contribute changes back to the base repositories.
    For example, if you only want to develop custom labscript device drivers, you might only fork and clone the labscript-devices repository.
    Moreover, there is now an option to write and use custom labscript device drivers outside of the labscript-devices installation directory.


In this example, we will use an existing conda environment named `py38`.
Skip the first line/step if continuing on from the instructions to :ref:`set up this environment <installation/setting-up-an-environment:Anaconda Python>`.

.. attention:: 
    For the following to work correctly on Windows, you need to use the Anaconda Powershell Prompt, not the Anaconda Prompt.
    This will be the case until the following bugs are fixed:

    * `conda-build#3813 <https://github.com/conda/conda-build/issues/3813>`_
    * `conda#9445 <https://github.com/conda/conda/issues/9445>`_

Quick start
-----------

.. note:: After the first line, the current directory is ommited from the command prompt
    for brevity.

.. code-block:: console

    (base) C:\Users\wkheisenberg> mkdir labscript-suite
    (base) > cd labscript-suite
    (base) > git clone https://github.com/wkheisenberg/labscript
    (base) > git clone https://github.com/wkheisenberg/runmanager
    (base) > git clone https://github.com/wkheisenberg/blacs
    (base) > git clone https://github.com/wkheisenberg/lyse
    (base) > git clone https://github.com/wkheisenberg/runviewer
    (base) > git clone https://github.com/wkheisenberg/labscript-devices
    (base) > git clone https://github.com/wkheisenberg/labscript-utils
    (base) > conda activate py38
    (py38) > conda config --env --add channels labscript-suite
    (py38) > conda install setuptools-conda pyqt pip desktop-app
    (py38) > setuptools-conda install-requirements ^ 
             labscript runmanager blacs lyse runviewer labscript-devices labscript-utils
    (py38) > pip install --no-build-isolation --no-deps ^
             -e labscript -e runmanager -e blacs -e lyse ^
             -e runviewer -e labscript-devices -e labscript-utils
    (py38) > labscript-profile-create
    (py38) > desktop-app install blacs lyse runmanager runviewer

Detailed instructions
---------------------

The following is a detailed explanation of the steps provided in the Quick start section above.

#. Fork the labscript-suite repositories you want to develop using the `GitHub online interface <https://help.github.com/en/github/getting-started-with-github/fork-a-repo>`_. 
   Below we will include all repositories (except the labscript-suite metapackage).

#. Manually clone the forked repositories using |GitClone|_.

   .. note::
        This will set your forked repository(ies) to be the 'origin' remote.

#. Use the `setuptools-conda install-requirements` command to introspect the dependencies from the cloned repositories.

#. Now use `pip` to install the cloned repositories in develop mode without build isolation or installing dependencies via `pip`:

   .. code-block:: console

      C:\Users\wkheisenberg\labscript-suite> pip install --no-build-isolation --no-deps ^
      -e labscript -e runmanager -e blacs -e lyse -e runviewer -e labscript-devices -e labscript-utils

   .. note::
        On Linux / macOS the line continuation character is ``\`` rather than `^`.

#. For each repository, set the upstream remote to the base labscript-suite repository:

   .. code-block:: console

        C:\Users\wkheisenberg\labscript-suite> cd blacs
        C:\Users\wkheisenberg\labscript-suite> git remote add upstream https://github.com/labscript-suite/blacs.git
        C:\Users\wkheisenberg\labscript-suite> cd ..


   Repeat for the other repositories.

#. Continue from step 4 (create the labscript profile) in the :doc:`regular-anaconda` instructions.

#. (Optional, but Recommended) Remove `conda` and its dependencies from the `py38` environment.
   This will allow you to use the standard Anaconda Prompt again with this environment without issues.
   The particular issue being addressed is that `setuptools-conda` installs the `conda` package in a non-base environment, which can cause issues.
   Once the installation is complete, `setuptools-conda` and its dependices are no longer needed and can be safely removed using:

   .. code-block:: console

       conda remove conda

   Note that this command will only work if you use the Anaconda Powershell Prompt and have installed the labscript suite into a non-base environment as described above.

Updating a developer installation
---------------------------------

This assumes you have already completed the developer installation above and have:

*   Forked a *labscript suite* repository on GitHub;
*   Cloned the repository;
*   Set your fork to be the 'origin' remote; and
*   Set the labscript-suite base repository to be the 'upstream' remote.

All instructions for updating the labscript developer installation are identical to those for 
a :ref:`pip developer installation <installation/developer-pypi:Updating a developer installation>`.


.. The below is a hack in order to make a code block also a hyperlink, see https://docutils.sourceforge.io/docs/ref/rst/directives.html#replace

.. |GitClone| replace:: `git clone`
.. _GitClone: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository