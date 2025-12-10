from pathlib import Path
try:
    import importlib.metadata as importlib_metadata
except ImportError:
    import importlib_metadata

root = Path(__file__).parent.parent
if (root / '.git').is_dir():
    try:
        from setuptools_scm import get_version
        VERSION_SCHEME = {
            "version_scheme": "release-branch-semver",
            "local_scheme": "node-and-date",
        }
        scm_version = get_version(root, **VERSION_SCHEME)
    except ImportError:
        scm_version = None
else:
    scm_version = None

if scm_version is not None:
    __version__ = scm_version
else:
    try:
        __version__ = importlib_metadata.version(__package__)
    except importlib_metadata.PackageNotFoundError:
        __version__ = None
