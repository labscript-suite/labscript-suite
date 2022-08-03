Documentation Resources
=======================

A list of links to relevant resources used by our sphinx configuration.

Relevant Sphinx Docs
--------------------

* `autodoc Extension <https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html>`__

  * Used extensively to automatically introspect the API documentation.

* `autosummary Extension <https://www.sphinx-doc.org/en/master/usage/extensions/autosummary.html>`__

  * Used to automatically generate stubs for the API documentation for all modules except *labscript-devices*.

* `intersphinx Extension <https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html>`__

  * Used to generate cross references between repositories. The cross-reference syntax is described
    better `here <https://docs.readthedocs.io/en/stable/guides/intersphinx.html>`__.

* `sphinx-apidoc <https://www.sphinx-doc.org/en/master/man/sphinx-apidoc.html>`__

  * Used in *labscript-devices* to generate stubs for the NI-DAQmx models subclasses.

Syntax Cheatsheets
------------------

* `Read the Docs Example project <https://sphinx-rtd-theme.readthedocs.io/en/stable/index.html>`__

  * Shows a built project that uses many rst and sphinx features. 
    Go to the associated github repo to see the source that produces it.

* `Google-style Docstring Example <https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html>`__

  * Example that contains most of the syntax necessary to write docstrings.

    .. note:: You must follow this syntax for correctly formatted docstrings.

* `RST cheatsheet <https://bashtage.github.io/sphinx-material/rst-cheatsheet/rst-cheatsheet.html>`__

  * Cheatsheet for RST directives, with a focus on use with Sphinx.

* `A ReStructuredText Primer <https://docutils.sourceforge.io/docs/user/rst/quickstart.html>`__

  * Authoritative summary reference for full RST sytanx.
