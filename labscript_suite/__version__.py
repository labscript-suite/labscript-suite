from pathlib import Path
import importlib.metadata

root = Path(__file__).parent.parent
if (root / '.git').is_dir():
    try:
        from setuptools_scm import get_version
        VERSION_SCHEME = {
            "version_scheme": "semver-pep440-release-branch",
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
        __version__ = importlib.metadata.version(__package__)
    except importlib.metadata.PackageNotFoundError:
        __version__ = None
