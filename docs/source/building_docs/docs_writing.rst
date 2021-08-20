Writing Docs
============

Top-Level
---------

Higher level documentation that outlines the general usage of the **labscript-suite** components are found in the `docs` folder of each project repository.
These documents can be written in either ReStructuredText (rst) or MarkDown (md).
Specific details for writing documentation in both formats is given below.

The navigational structure of the documentation is governed by `toctree` rst directives, where each file included in a `toctree` forms the basis of a new page.
It is considered good practice to organise documentation logically by subject into individual files and sub-directories.
Examples of documentation sources can be readily found by clicking the `View page source` link at the top right corner of any page in the on-line html documentation.

ReStructuredText
****************

ReStructuredText is the native language for writting documention is a sphinx-based system.
As such, most documentation should be written in rst.
Examples and syntax guides are available via links :doc:`here <docs_minutia>`.

An important note when creating new rst doc files is to try to use unique filenames within a single repository.
These filenames are ultimately used in the html page paths and are used when cross-referencing pages within the documentation.
Files in a single project with identical names can be difficult to uniquely reference.

MarkDown
********

Markdown syntax documentation can also be used within the **labscript-suite** via the `m2r` package.
Given markdowns simpler syntax, it can be an ideal choice for long prose documentation.
Note that, unlike rst files, markdown files cannot be used indepently to form a new page.
Instead, markdown source files must be included directly into a parent rst file via an `mdinclude` rst directive.
An example of how this is done is found in the homepage of each project (i.e. the `index.rst` and `main.md` files in the `docs` root directory).
Documentation that requires higher level features (particularly cross-referencing) are often better written in rst directly.

API/Docstrings
--------------

Docstrings are written within the source code itself.
Their purpose is to document the inputs, outputs, and usage of the classes, functions, and attributes in the API.
The **labscript-suite** uses Google style formatting for the docstrings.
A detailed example of the syntax is `here <https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html>`_ and details can be found in other places on-line.

Docstring Coverage
******************

As part of the build process, a rough estimation of the API coverage is reported to the command line.
It counts the number of documentated objects relative to the total number of objects processed.
This report is only accurate when starting from a clean build, as sphinx does not re-process items that are already documented.
Note that an object is counted documented if it's docstring is not empty, so incomplete docstrings are not caught.
