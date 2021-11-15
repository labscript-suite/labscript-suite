Writing Docs
============

Documentation for the **labscript-suite** is generally written at two levels: manually created top-level narrative docs and automatically introspected API docstrings.
These two types of documentation live in different places within the code repository and have different purposes, as described in the following sections.

As a general guideline for writing documentation, please ensure no more than one sentence is on a line in the source file.
This ensures diffs will only highlight the changed senstences of the paragraph, instead of large blocks of text.
Note that paragraph breaks require a blank line between lines of text.

Top-Level
---------

Higher level documentation that outlines the general usage of the **labscript-suite** components are found in the `docs` folder of each project repository.
These documents can be written in either ReStructuredText (rst) or MarkDown (md).
Specific details for writing documentation in both formats is given below.

The navigational structure of the documentation is governed by `toctree` rst directives, where each file included in a `toctree` forms the basis of a new page.
It is considered good practice to organise documentation logically by subject into individual files and sub-directories.
Examples of documentation sources can be readily found by clicking the `Edit on GitHub` link at the top right corner of any page in the on-line html documentation.

ReStructuredText
****************

ReStructuredText is the native language for writting documention in a sphinx-based system.
As such, most documentation should be written in rst.
Examples and syntax guides are available via links :doc:`here <docs_resources>`.

An important note when creating new rst doc files is to try to use unique filenames within a single repository.
These filenames are ultimately used in the html page paths and are used when cross-referencing pages within the documentation.
Files in a single project with identical names can be difficult to uniquely reference.

MarkDown
********

Markdown syntax documentation can also be used within the **labscript-suite** via the `m2r <https://pypi.org/project/m2r/>`_ package.
Given markdown's simpler syntax, it can be an ideal choice for long prose documentation.
Note that, unlike rst files, markdown files cannot be used indepently to form a new page.
Instead, markdown source files must be included directly into a parent rst file via an `mdinclude` rst directive.
An example of how this is done is found in the homepage of each project (i.e. the `index.rst` and `main.md` files in the `docs` root directory).
Documentation that requires higher level features (particularly cross-referencing) are often better written in rst directly.

API/Docstrings
--------------

Docstrings are written within the source code itself.
Their purpose is to document the inputs, outputs, and usage details of the classes, functions, and attributes in the API.
The **labscript-suite** uses Google style formatting for the docstrings.
A detailed example of the syntax is `here <https://www.sphinx-doc.org/en/master/usage/extensions/example_google.html>`_ and further details can be found in other places on-line.

Docstring Coverage
******************

As part of the build process, a rough estimation of the API coverage is reported to the command line at the end of the build.
It counts the number of documentated objects relative to the total number of objects processed.
This report is only approximately accurate when starting from a clean build, as sphinx does not re-process items that are unchanged from a prior build.
Note that an object is counted documented if it's docstring is not empty, so incomplete docstrings are not caught.
