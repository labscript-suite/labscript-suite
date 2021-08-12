Building the Docs
=================

The **labscript-suite** documentation is built one repository at a time.
To build the documentation for a single repository:

#. Activate the environment where the **labscript-suite** and the sphinx dependencies are installed.
#. Change directories to the `docs` subfolder of the repository.
#. Run the appropriate `make` command, described below.

Assuming the appropriate dependencies are installed, the documentation will be build and placed in the `docs/build` folder corresponding to the build command used.

html
----

The web-based documentation, which is what is hosted at `<https://docs.labscriptsuite.org/en/latest/>`_ by Read the Docs, is built using the command

.. code-block:: bash

	make html

The home page is found at `docs/build/html/index.html`.

Note that the build on Read the Docs uses the closely related `make dirhtml` command.
This build command organizes the html documentation in a way suitable for web hosting.
For locally inspecting the documentation, the `make html` command is preferred to preserve normal inter-page links.

latexpdf
--------

Building the pdf documentation is a bit more complicated than the other builds.
Normally it would be done by running the command

.. code-block:: bash

	make latexpdf

This would build latex source files which are compiled using a local installation of latex.
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

Read the Docs
-------------

Whenever a pull request is created or merged on GitHub, the documentation is automatically built by Read the Docs.
The result of this build can be viewed online by looking at the details of the automated checks.
If the build is completed, this link will take you directly to the home page of your built documentation.
If the build is still in progress, this link will take you to the build progress which shows the commands being run and their outputs.
If you wish to see this progress after the build succeeds, you can find it by clicking the bottom left corner of the Read the Docs page.
This will bring up a small window pane.
Selecting builds will bring up the build logs for all of the online builds.

Note that Read the Docs will only build the html documentation for a pull request.
When the pull request is merged, Read the Docs will build the html documentation again, as well as downloadable pdf and epub versions.
