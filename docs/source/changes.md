## Recent changes to the _labscript suite_

Upon migrating the code base to GitHub and publishing distributions on PyPI in April–May 2020, the following changes have been undertaken.

### Changes to profile directories

The _labscript suite_ profile directory, containing application configurations, logs, and user-side code, is now located by default in the current user’s home directory, e.g.

* `C:\Users\wkheisenberg\labscript-suite` on Windows.
* `~/labscript-suite` or `/home/wkheisenberg/labscript-suite` on Linux and Mac OS X.

A typical structure is:

```
    ~/labscript-suite/
    ├── app_saved_configs/
    │   ├── default_experiment/
    ├── labconfig/
    ├── logs/
    └── userlib/
        ├── analysislib/
        ├── labscriptlib/
        ├── pythonlib/
        └── user_devices/
```

This structure is created by calling the command `labscript-profile-create`.

in a terminal after installing `labscript-utils` (per the [installation instructions](#regular-installation-from-the-python-package-index)).

_Note:_ As of [labscript-suite/labscript-utils#37](https://github.com/labscript-suite/labscript-utils/issues/37) this can be the same directory as an editable installation.


### Changes to application shortcuts

Operating-system menu shortcuts, correct taskbar behaviour, and environment activation for the Python GUI applications (blacs, lyse, runmanager, and runviewer) is now handled by a standalone Python package [desktop-app](https://github.com/chrisjbillington/desktop-app) (per installation instructions above). This currently supports Windows and Linux (Mac OS X support is forthcoming).


### Changes to source code structure

Existing users who move to a developer (editable) installation, please note the following structural changes to the _labscript suite_ source code:

* Each package has a top-level folder containing setup.py and setup.cfg used to build a distribution from source. The functional code base now resides in a subfolder corresponding to the name of the Python module, e.g. an editable installation might contain folders:

    ```
    <path-to-your-labscript-installation>/
    ├── blacs/
    │   └── blacs/
    ├── labscript/
    │   └── labscript/
    ├── labscript-devices/
    │   └── labscript_devices/
    ├── labscript-utils/
    │   └── labscript_utils/
    ├── lyse/
    │   ├── lyse/
    ├── runmanager/
    │   └── runmanager/
    └── runviewer/
        └── runviewer/
    ```


* Package names (shared by repositories and top-level folders) are now hyphenated, e.g. labscript-devices and labscript-utils.
* Module names remain underscored, i.e. labscript_devices and labscript_utils.
* The mixing of hyphen and underscores is inelegant but conventional.
* All references to blacs are now lowercase.
* As installation no longer requires a separate package, the repository formerly named ‘installer’ has been renamed to ‘[labscript-suite](https://github.com/labscript-suite/labscript-suite/issues)’, and will be used as a metapackage for the labscript suite.


### Changes to versioning

Aside from the maintenance branches described [below](#branching-modelstrategy), versions of the labscript suite packages are introspected at run-time using either the [importlib.metadata](importlib.metadata) library (regular installations) or [setuptools_scm](https://github.com/pypa/setuptools_scm) (developer installations). Thus any changes to an editable install will be traceable by local version numbers, e.g. editing the released version of a package with version  2.4.0 will result in 2.4.0dev1+gc28fe94, for example. This will help us diagnose issues users have with their editable installations.
