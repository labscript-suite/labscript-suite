# This repository. PyPI and Anaconda test and release package uploads are only done if
# the repository the workflow is running in matches this (i.e. is not a fork). Optional,
# if not set, package uploads are skipped.
export RELEASE_REPO="labscript-suite/labscript-suite"

# Username with which to upload conda packages. If not given, anaconda uploads are
# skipped.
export ANACONDA_USER="labscript-suite"

# Whether (true or false) to upload releases to PyPI, non-releases to Test PyPI,
# releases to Anaconda, non-releases to Anaconda test label. Only used if the repository
# the workflow is running in matches RELEASE_REPO, otherwise uploads are skipped.
# Anaconda uploads require ANACONDA_USER be specified and ANACONDA_API_TOKEN secret be
# set. Optional, all default to true.
export PYPI_UPLOAD=""
export TESTPYPI_UPLOAD=""
export ANACONDA_UPLOAD=""
export TEST_ANACONDA_UPLOAD=""

# Which Python version to use for pure wheel builds, sdists, and as the host Python for
# cibuildwheel. Optional, defaults to the second-most recent minor Python version.
export DEFAULT_PYTHON=""

# Comma-separated list of Python versions to build conda packages for. Only used if
# HAS_ENV_MARKERS=true or PURE=false, otherwise a noarch conda package is built instead.
# Optional, defaults to all non-end-of-life stable Python minor versions.
export CONDA_PYTHONS=""

# Environment variable set in the envionment that `cibuildwheel` runs in instructing it
# which Pythons to build for, as a space-separated list of specifiers in the format
# specified by `cibuildwheel`. Only used if PURE=false. Optional, defaults to all
# non-end-of-life stable CPython versions.
export CIBW_BUILD=""

# Name of Python package. Optional, defaults to name from the package metadata
export PKGNAME=""

# Version of Python package. Optional, defaults to version from the package metadata
export PKGVER=""

# Whether the Python package is pure (true) or impure (false). Optional, defaults to
# false if the setuptools package has extension modules or libraries, otherwise true.
export PURE=""

# Whether (true or false) the Python package has dependencies that vary by platform or
# Python version. Optional, Defaults to presence of env markers in package metadata.
export HAS_ENV_MARKERS=""
