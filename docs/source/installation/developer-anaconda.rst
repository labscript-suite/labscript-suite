Developer installation (Anaconda Cloud)
=======================================

Developer installations are useful for those who want to customise the *labscript suite*.

.. note:: You need not fork, clone, and install editable versions of all *labscript suite* repositories to customise your installation and/or contribute changes back to the base repositories.
    For example, if you only want to develop custom labscript device drivers, you might only fork and clone the labscript-devices repository.
    Moreover, there is now an option to write and use custom labscript device drivers outside of the labscript-devices installation directory.


In this example, we will use an existing conda environment named `py38`.
Skip the first line/step if continuing on from the instructions to :ref:`set up this environment <installation/setting-up-an-environment:Anaconda Python>`.


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

* Under construction*
