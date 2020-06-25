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
from pathlib import Path
import sys
from m2r import MdInclude
from recommonmark.transform import AutoStructify
from jinja2 import FileSystemLoader, Environment

# -- Project information (unique to each project) -------------------------------------

project = "the labscript suite"
copyright = "2020, labscript suite"
author = "labscript suite contributors"

sys.path.insert(0, os.path.abspath("../.."))
from labscript_suite import __version__ as version  # noqa: E402

release = version

# HTML icons
img_path = "../../art"
html_logo = img_path + "/labscript-suite-rectangular-transparent_276x140.svg"
html_favicon = img_path + "/labscript.ico"

# -- General configuration (should be identical across all projects) ------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_rtd_theme",
    "recommonmark",
]

autodoc_typehints = 'description'

# Prefix each autosectionlabel with the name of the document it is in and a colon
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# intersphinx allows us to link directly to other repos sphinxdocs.
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference/', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'qtutils': ('https://qtutils.readthedocs.io/en/stable/', None),
    'pyqtgraph': (
        'https://pyqtgraph.readthedocs.io/en/latest/',
        None,
    ),  # change to stable once v0.11 is published
    'matplotlib': ('https://matplotlib.org/', None),
    'h5py': ('http://docs.h5py.org/en/stable/', None),
    'pydaqmx': ('https://pythonhosted.org/PyDAQmx/', None),
    'qt': (
        '',
        'pyqt5-modified-objects.inv',
    )  # from https://github.com/MSLNZ/msl-qt/blob/master/docs/create_pyqt_objects.py
    # under MIT License
    # TODO
    # desktop-app
    # spinapi/pynivision/etc
}

# list of all labscript suite components that have docs
labscript_suite_programs = {
    'labscript': {
        'desc': 'Expressive composition of hardware-timed experiments',
        'icon': 'labscript_32nx32n.svg',
        'type': 'lib',
    },
    'labscript-devices': {
        'desc': 'Plugin architecture for controlling experiment hardware',
        'icon': 'labscript_32nx32n.svg',
        'type': 'lib',
    },
    'labscript-utils': {
        'desc': 'Shared modules used by the *labscript suite*',
        'icon': 'labscript_32nx32n.svg',
        'type': 'lib',
    },
    'runmanager': {
        'desc': 'Graphical and remote interface to parameterized experiments',
        'icon': 'runmanager_32nx32n.svg',
        'type': 'gui',
    },
    'blacs': {
        'desc': 'Graphical interface to scientific instruments and experiment supervision',
        'icon': 'blacs_32nx32n.svg',
        'type': 'gui',
    },
    'lyse': {
        'desc': 'Online analysis of live experiment data',
        'icon': 'lyse_32nx32n.svg',
        'type': 'gui',
    },
    'runviewer': {
        'desc': 'Visualize hardware-timed experiment instructions',
        'icon': 'runviewer_32nx32n.svg',
        'type': 'gui',
    },
}

# whether to use stable or latest version
labscript_suite_doc_version = os.environ.get('READTHEDOCS_VERSION', 'latest')
if '.' in labscript_suite_doc_version:
    labscript_suite_doc_version = 'stable'
elif labscript_suite_doc_version not in ['stable', 'latest']:
    labscript_suite_doc_version = 'latest'

# add intersphinx references for each component
for ls_prog in labscript_suite_programs:
    intersphinx_mapping[ls_prog] = (
        'https://docs.labscriptsuite.org/projects/{}/en/{}/'.format(
            ls_prog, labscript_suite_doc_version
        ),
        None,
    )

# add intersphinx reference for the metapackage
if project != "the labscript suite":
    intersphinx_mapping['labscript-suite'] = (
        'https://docs.labscriptsuite.org/en/{}/'.format(labscript_suite_doc_version),
        None,
    )

# Make `some code` equivalent to :code:`some code`
default_role = 'code'

# hide todo notes if on readthedocs and not building the latest
if os.environ.get('READTHEDOCS') and (
    os.environ.get('READTHEDOCS_VERSION') != 'latest'
    or (
        os.environ.get('READTHEDOCS_PROJECT') == project
        or os.environ.get('READTHEDOCS_PROJECT') == 'labscriptsuite'
    )
):
    todo_include_todos = False
else:
    todo_include_todos = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_title = "labscript suite | {project}".format(
    project=project
    if project != "labscript-suite"
    else "experiment control and automation"
)
html_short_title = "labscript suite"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Customize the html_theme
html_theme_options = {'navigation_depth': 3}

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
    app.add_css_file('custom.css')

    # generate the components.rst file dynamically so it points to stable/latest
    # of subprojects correctly
    loader = FileSystemLoader(Path(__file__).resolve().parent / templates_path[0])
    env = Environment(loader=loader)
    template = env.get_template('components.rst')
    with open(Path(__file__).resolve().parent / 'components.rst', 'w') as f:
        f.write(
            template.render(
                intersphinx_mapping=intersphinx_mapping,
                programs=labscript_suite_programs,
                current_project=project,
                img_path=img_path
            )
        )
