Building the Docs
=================

The **labscript-suite** documentation is built one repository at a time.
To build the documentation for a single repository:

#. Activate the environment where the **labscript-suite** and sphinx dependencies are installed.
#. Change directories to the `docs` subfolder of the repository.
#. Run the appropriate `make` command, described below.

Assuming the appropriate dependencies are installed, the documentation will be built and placed in a subfolder of `docs/build` corresponding to the build command used.

html
----

The web-based documentation, which is what is hosted at `<https://docs.labscriptsuite.org/en/latest/>`_ by Read the Docs, is built locally using the command

.. code-block:: bash

	make html

The home page is found at `docs/build/html/index.html`.
Repeated calls of this (and the other) build commands will introspect which source files have changed and only update the corresponding build outputs.

Note that the build on Read the Docs uses the closely related `make dirhtml` command.
This build command organizes the html documentation in a way suitable for web hosting.
For locally inspecting the documentation, the `make html` command is preferred to preserve normal inter-page links.

.. note::

	Some cross-referencing used in the markdown files is not cross-compatible between the `html` and `dirthtml` build commands.
	When using markdown source files, please ensure cross-references actually work when built on Read the Docs.

latexpdf
--------

Building the pdf documentation is a bit more complicated than the other builds.
Normally it would be done by running the command

.. code-block:: bash

	make latexpdf

This would create latex source files which are automatically compiled using an existing, local installation of latex.
The latex compilation requires `perl` and the `latexmk` latex package. 
It also requires a great many other latex dependencies.
Successfully building the pdf documentation locally is made easier if your latex installation can install dependencies as required.

Unfortunately, this simple build command :ref:`does not succeed <building_docs/docs_minutia:latexpdf local builds>` for **labscript-suite** documentation.
To build the pdf docs locally, you will need to instead build using the `make latex` command followed by the latex compiling command used on Read the Docs.

.. code-block:: bash

	latexmk -r latexmkrc -pdf -f -dvi- -ps- -jobname=repository-name -interaction=nonstopmode

This command is run from within the `docs/build/latex` directory where the `latexmkrc` file resides.

epub
----

This builds the documentation in the EPUB format, for use with e-readers.
It is built using the command

.. code-block:: bash

	make epub

clean
-----

This make target will clean the entire `build` directory.
It ensures that a fresh build can be made.
It is helpful when stale build files are interfering with new changes or you wish to see the :ref:`coverage <building_docs/docs_writing:docstring coverage>`.
The command is

.. code-block:: bash

	make clean