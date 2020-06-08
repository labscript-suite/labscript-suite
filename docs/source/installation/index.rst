Installing the *labscript suite*
================================

.. todo:: discussion on python vs. conda and regular vs. developer install

We're excited to announce that accompanying the recent migration of the codebase from BitBucket to GitHub, *labscript suite* components are now distributed as Python packages on `PyPI <https://pypi.org/user/labscript-suite>`_ and `Anaconda Cloud <https://anaconda.org/labscript-suite>`_.

This makes it far easier to get started using the *labscript suite*, as you no longer require a Mercurial or Git installation (or any knowledge of version control software); components can be installed and upgraded using:

* |pip|_: the standard package manager common to all Python distributions; or
* |conda|_: a binary package and environment manager, part of the `Anaconda Python <https://www.anaconda.com>`_ distribution.


.. toctree::
    :maxdepth: 2

    setting-up-an-environment
    regular-pypi
    regular-anaconda
    developer-pypi
    developer-anaconda
    .. regular-to-developer

.. |pip| replace:: ``pip``
.. _pip: https://packaging.python.org/tutorials/installing-packages

.. |conda| replace:: ``conda``
.. _conda: https://anaconda.org/anaconda/conda