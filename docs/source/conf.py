# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme
from m2r import MdInclude
from recommonmark.transform import AutoStructify

sys.path.insert(0, os.path.abspath('../..'))
from labscript_suite.__version__ import __version__


# -- Project information -----------------------------------------------------

project = 'the labscript suite'
copyright = '2020, labscript suite'
author = 'labscript suite contributors'

version = __version__
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "recommonmark",
]

autodoc_typehints = 'description'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# Custom parsers of source files.
# source_parsers = {'.md': 'recommonmark.parser.CommonMarkParser'}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# intersphinx allows us to link directly to other repos sphinxdocs.
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    # 'numpy': ('https://numpy.org/doc/stable/', None),
    # 'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    # 'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None)
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_logo = "img/suite_logo_transparent.png"
html_favicon = "img/labscript.ico"
html_title = "labscript suite | experiment control and automation"
html_short_title = "labscript suite"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = "sphinx"

# Use m2r only for mdinclude and recommonmark for everything else
# https://github.com/readthedocs/recommonmark/issues/191#issuecomment-622369992
def setup(app):
    config = {
        # 'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
        'enable_eval_rst': True,
    }
    app.add_config_value('recommonmark_config', config, True)
    app.add_transform(AutoStructify)

    # from m2r to make `mdinclude` work
    app.add_config_value('no_underscore_emphasis', False, 'env')
    app.add_config_value('m2r_parse_relative_links', False, 'env')
    app.add_config_value('m2r_anonymous_references', False, 'env')
    app.add_config_value('m2r_disable_inline_math', False, 'env')
    app.add_directive('mdinclude', MdInclude)
