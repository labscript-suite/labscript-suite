Developer installation (Python Package Index)
=============================================

Developer installations are useful for those who want to customise the *labscript suite*.

.. note:: You need not fork, clone, and install editable versions of all *labscript suite* repositories to customise your installation and/or contribute changes back to the base repositories.
    For example, if you only want to develop custom labscript device drivers, you might only fork and clone the labscript-devices repository.
    Moreover, there is now an option to write and use custom labscript device drivers outside of the labscript-devices installation directory.


Quick start
-----------

.. code-block:: console

    C:\Users\wkheisenberg\labscript-suite> .venv\Scripts\activate
    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install \
            --src . -e git+https://github.com/wkheisenberg/blacs#egg=blacs \
            --src . -e git+https://github.com/wkheisenberg/labscript#egg=labscript \
            --src . -e git+https://github.com/wkheisenberg/labscript-devices#egg=labscript-devices \
            --src . -e git+https://github.com/wkheisenberg/labscript-utils#egg=labscript-utils \
            --src . -e git+https://github.com/wkheisenberg/runmanager#egg=runmanager \
            --src . -e git+https://github.com/wkheisenberg/runviewer#egg=runviewer \
            --src . -e git+https://github.com/wkheisenberg/lyse#egg=lyse
    (.venv) C:\Users\wkheisenberg\labscript-suite> pip install PyQt5
    (.venv) C:\Users\wkheisenberg\labscript-suite> labscript-profile-create
    (.venv) C:\Users\wkheisenberg\labscript-suite> desktop-app install blacs lyse runmanager runviewer


Detailed instructions
---------------------

1. Fork the labscript-suite repositories you want to develop using the `GitHub online interface <https://help.github.com/en/github/getting-started-with-github/fork-a-repo>`_. Below we will include all repositories (except the labscript-suite metapackage).


.. The below is a hack in order to make a code block also a hyperlink, see https://docutils.sourceforge.io/docs/ref/rst/directives.html#replace

.. |GitClone| replace:: `git clone`
.. _GitClone: https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository


2. Use `pip` to both clone these forks locally and install them into your environment. In this example (on Windows), the forks are owned by the (non-existent) GitHub user wkheisenberg.

   .. code-block:: console

        C:\Users\wkheisenberg\labscript-suite> pip install ^
        --src . -e git+https://github.com/wkheisenberg/blacs#egg=blacs ^
        --src . -e git+https://github.com/wkheisenberg/labscript#egg=labscript ^
        --src . -e git+https://github.com/wkheisenberg/labscript-devices#egg=labscript-devices ^
        --src . -e git+https://github.com/wkheisenberg/labscript-utils#egg=labscript-utils ^
        --src . -e git+https://github.com/wkheisenberg/runmanager#egg=runmanager ^
        --src . -e git+https://github.com/wkheisenberg/runviewer#egg=runviewer ^
        --src . -e git+https://github.com/wkheisenberg/lyse#egg=lyse


   .. note::
        * This will set your forked repository(ies) to be the 'origin' remote.
        * On Linux / macOS the line continuation character is ``\`` rather than `^`.

   Alternatively, manually clone the repositories using |GitClone|_ and then install them using `pip` by running the following from the common parent directory:

   .. code-block:: console

        C:\Users\wkheisenberg\labscript-suite> pip install -e blacs -e labscript \ 
            -e labscript-devices -e labscript-utils -e lyse -e runmanager -e runviewer


   For a single package, this would look like:

   .. code-block:: console

        C:\Users\wkheisenberg\labscript-suite> git clone https://github.com/wkheisenberg/runmanager.git
        C:\Users\wkheisenberg\labscript-suite> pip install -e runmanager


3. For each repository, set the upstream remote to the base labscript-suite repository:


   .. code-block:: console

        C:\Users\wkheisenberg\labscript-suite> cd blacs
        C:\Users\wkheisenberg\labscript-suite> git remote add upstream https://github.com/labscript-suite/blacs.git
        C:\Users\wkheisenberg\labscript-suite> cd ..


   Repeat for the other repositories.

4. Continue from step 4 (install PyQt5) in the :doc:`regular-pypi` instructions.


Updating a developer installation
---------------------------------

This assumes you have already completed the developer installation above and have:

*   Forked a *labscript suite* repository on GitHub;
*   Cloned the repository;
*   Set your fork to be the 'origin' remote; and
*   Set the labscript-suite base repository to be the 'upstream' remote.

1. Use one of the following to keep your repository (and feature branches) up-to-date:

   `Fetch changes, and merge <https://help.github.com/en/github/using-git/getting-changes-from-a-remote-repository#fetching-changes-from-a-remote-repository>`_ with your local master branch.

   .. code-block:: console

        > git checkout master
        > git fetch upstream master --tags
        > git merge upstream/master


   Or using `Git Pull <https://help.github.com/en/github/using-git/getting-changes-from-a-remote-repository#pulling-changes-from-a-remote-repository>`_:

   .. code-block:: console

        > git checkout master
        > git pull upstream master --tags


   Or using `hub sync <https://hub.github.com/>`_ command-line extension (does not require current local working branch to be master):

   .. code-block:: console

        > hub sync


2. Update your feature branches by merging them with master or rebasing them to master:

   .. code-block:: console

        > git checkout your-feature-name
        > git merge master <OR> git rebase master --autostash


3. Update your fork by `pushing <https://help.github.com/en/github/using-git/pushing-commits-to-a-remote-repository>`_ any changes resulting from steps 1–2 and/or subsequent local development:

   .. code-block:: console

        > git checkout master
        > git push origin master --tags
        > git checkout your-feature-name
        > git push origin your-feature-name master


   .. note:: If the feature branch has not yet been created on your fork, you need to include `-u` above, i.e.

        .. code-block:: console

            > git push -u origin your-feature-name


4. Checkout the commit you want to install. This might be a specific release version (which can be specified by tag):

   .. code-block:: console

        > git checkout v0.3.2


   or using the commit SHA:

   .. code-block:: console

        > git checkout 59651b5


5. (Optional) Update the package using (from within the root of a repository):

   .. code-block:: console

        > pip install -e .


   As the installations are in editable mode and the version is being introspected at runtime, this step is not always necessary, but is required for any change requiring setup.py to be run to take effect, e.g. dependency changes, console entry points, etc.