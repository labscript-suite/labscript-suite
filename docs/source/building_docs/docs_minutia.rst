Minutia
=======

Here is a list of minor details that come up when dealing with our docs that are not well documented in the Sphinx docs or are very unique to our project.

autosummary can't find a module
-------------------------------

When you get an error while building the docs stating autosummary could not find a module, it could be due to one of two things:

1. The module actually cannot be found, due to a typo in the `autosummary` command.
2. The much more likely reason, the module is actually found, but cannot be imported.

In order to see the actual error to diagnose the problem properly, temporarily remove that module from the `autosummary` directive and do an explicit `automodule` directive.
Once the import error is fixed, you can move the module back into the `autosummary` directive.

*labscript-devices* API
-----------------------

Unlike the rest of the **labscript-suite**, **labscript-devices** does NOT use recursive `autosummary` calls to generate the API documentation. 
This means that, unlike other modules, adding a new device to **labscript-devices** will NOT automatically be captured in the docs build.
When adding a new device, you are expected to make a top-level rst document that implements the necessary `autodoc` calls to document the device. 

.. note:: 

	In all modules, adding a sub-module at the top-level likely will not be automatically caught either.
	It will need to be added to the relevant `autosummary` directive manually.

latexPDF local builds
---------------------

Local builds of the latexPDF version of the documentation will not work using the standard `make latexpdf` command.
This is because the **labscript-suite** uses svg figure icons that latex cannot process.
This build **does** work on RTD because they do not use the `latexpdf` make target, but instead call `latexmk` with customized options that ignore these little errors.
In order to build the PDF documentation locally, you will need to use the same call as RTD uses.

Note that the RTD latex build is fairly stable, if really ugly, so long as the html docs build. 
That said, if there is an error unique to the latex build, discovering its origin can be very difficult since the build process has to ignore errors to complete normally anyway.

One specific error already encounted is when an API documentated value is too long for latex to parse as a single line (a raw bitmap image saved as a class attribute).
This specific error can be overcome by instructing sphinx to not publish the value in the docs using the `:meta hide-value:` rst key for the offending object.

intersphinx references won't link
---------------------------------

Using intersphinx links to reference documentation in other packages (or even the same package) can be tricky.
This is because the exact convention for referring to things is not guaranteed between projects.
The best way to determine the exact reference label to use is to introspect the intersphinx object inventory for that project (the `objects.inv` file).
This can be done by calling, for example,

.. code-block:: shell

	python -m sphinx.ext.intersphinx https://www.sphinx-doc.org/en/master/objects.inv

See `this <https://stackoverflow.com/a/30981554>`__ SO post for many details.

This file is typically stored at the top level directory of a project, but not always. 
If the above command does not work to obtain the objects inventory for online docs, it can be run on a local copy of the file without issue.
Obtaining the file for online published docs amounts to guessing the correct location and pointing your browser there. 
To run the introspection locally, use

.. code-block:: shell

	python -m sphinx.ext.intersphinx objects.inv > objects.txt

In this call, we redirect the output to a text file for easier inspection.