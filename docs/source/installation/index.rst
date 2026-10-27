Installing the *labscript suite*
================================

The *labscript suite* components are Python packages on `PyPI <https://pypi.org/user/labscript-suite>`_ and on the `labscript-suite channel <https://anaconda.org/labscript-suite>`_ of Anaconda Cloud.

Choosing an installation method
-------------------------------

We recommend installing the *labscript suite* from PyPI into a virtual environment, with `uv <https://docs.astral.sh/uv/>`_ or `pip`.
uv installs Python itself as well as the packages, so it is the quickest way to start; pip works with any Python installation.
This is the installation method with which the *labscript suite* is tested, on Windows and Linux, for every supported Python version and Qt binding.

* A **regular installation** installs the released packages. Use it to run an experiment: :doc:`regular-pypi`.
* A **developer installation** installs editable copies of the repositories that you have cloned with git. Use it to change the code of the *labscript suite*, or to contribute changes: :doc:`developer-pypi`.
  A regular installation can be converted to a developer installation one component at a time: :doc:`regular-to-developer`.

The *labscript suite* can also be installed with conda: :doc:`regular-anaconda` and :doc:`developer-anaconda`.
Conda installations need more care:

* The environment must take its packages from conda-forge. On Windows, the `pyzmq` package of Anaconda's default channels is built without the CurveZMQ support that the *labscript suite* uses for encrypted communication, and on macOS on Intel processors the default channels have neither PySide6 nor PyQt6.
* On Windows, Python 3.15 cannot be used with conda yet: conda-forge has no Python 3.15 package of `windows-curses`, which zprocess requires on Windows.
* The `desktop-app` package on conda-forge is older than the one on the labscript-suite channel, so the labscript-suite channel must have a higher priority than conda-forge.

.. toctree::
    :maxdepth: 2

    setting-up-an-environment
    regular-pypi
    developer-pypi
    regular-to-developer

Installing with conda
---------------------

.. toctree::
    :maxdepth: 2

    regular-anaconda
    developer-anaconda
