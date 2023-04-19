import os
from setuptools import setup

VERSION_SCHEME = {
    "version_scheme": "release-branch-semver",
    "local_scheme": os.getenv("SCM_LOCAL_SCHEME", "node-and-date"),
}

setup(use_scm_version=VERSION_SCHEME)
