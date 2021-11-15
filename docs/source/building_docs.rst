Building the *labscript suite* docs
===================================

The **labscript-suite** documentation is hosted online at `<https://docs.labscriptsuite.org/en/latest/>`_.
It is composed from documentation for each module of the **labscript-suite**.
If you desire to build the documentation for a module locally, either for off-line usage or to test changes to the documentation, you will need to apply extra configuration beyond a normal installation.
This is because our documentation building pipeline relies on `sphinx <https://www.sphinx-doc.org/en/master/>`_, which introspects documentation from inline docstrings from the source code.
This introspection process requires that the code to be documented is importable and the necessary `sphinx` dependencies are installed.

The below sections describe how to configure your environment for building docs as well as some guidance for writing and contributing documentation.

.. toctree::
    :maxdepth: 2

    building_docs/docs_install
    building_docs/docs_build
    building_docs/docs_writing
    building_docs/docs_comitting
    building_docs/docs_resources
    building_docs/docs_minutia

    