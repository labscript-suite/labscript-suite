## Recent changes to the _labscript suite_

Upon migrating the code base to GitHub and publishing distributions on PyPI in April–May 2020, existing users should be aware of the following recent changes.

### Profile directories

The _labscript suite_ profile directory, containing application configurations, logs, and user-side code, is now located by default in the current user’s home directory, e.g. for a local user named `wkheisenberg` this is:

* `C:\Users\wkheisenberg\labscript-suite` on Windows.
* `~/labscript-suite` or `/home/wkheisenberg/labscript-suite` on Linux and Mac OS X.

A typical structure of the profile directory is:

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

This structure is created by calling the command `labscript-profile-create` in a terminal after installing `labscript-utils` (per the [installation instructions](../installation)).

_Note:_ As of [labscript-suite/labscript-utils#37](https://github.com/labscript-suite/labscript-utils/issues/37) an editable installation can be located within the labscript-suite profile directory.


### Secure communication

Interprocess communication between components of the *labscript suite* is based on the [ZeroMQ](https://zeromq.org) (ZMQ) messaging protocol. We have supported secure interprocess communication via encrypted ZMQ messaging since February 2019 (labscript-utils 2.11.0).

As of labscript-utils 2.16.0, **encryted interprocess communication will be the default**. If you haven't already, this means you'll need to create a new shared secret (or [pre-shared key](https://en.wikipedia.org/wiki/Pre-shared_key)) as follows:

1. Run `python -m zprocess.makesecret` from the labconfig directory.

2. Specify the path of the resulting `shared_secret` in your labconfig. For example:

    ```ini
    [security]
    shared_secret = %(labscript_suite)s/labconfig/zpsecret-09f6dfa0.key
    ```

3. Copy the same pre-shared key to all computers running the *labscript suite* that need to communicate with each other, repeating step 2 for each of them.

Treat this file like a password; it allows anyone on the same network access to *labscript suite* programs.

If you are on a trusted network and don't want to use secure communication, you may instead set:

```ini
[security]
allow_insecure = True
```

*Notes*:

* Steps 1 and 2 are executed automatically as part of the `labscript-profile-create` command. However, for multiple hosts, step 3 above must still be followed to ensure the same public-key is used by all hosts running *labscript suite* programs.

* There is an outstanding issue with the ZMQ Python bindings on Windows ([zeromq/pyzmq#1148](https://github.com/zeromq/pyzmq/issues/1148)), whereby encryption is significantly slower for Python distributions other than [Anaconda](https://www.anaconda.com). Until this issue is resolved, we recommend that Windows users on an untrusted network use the Anaconda Python distribution (and install `pyzmq` using `conda install pyzmq`).


### Application shortcuts

Operating-system menu shortcuts, correct taskbar behaviour, and environment activation for the Python GUI applications (blacs, lyse, runmanager, and runviewer) is now handled by a standalone Python package [desktop-app](https://github.com/chrisjbillington/desktop-app) (per installation instructions above). This currently supports Windows and Linux (Mac OS X support is forthcoming).


### Lab configuration

The `experiment_name` item has been renamed to `apparatus_name` in the labconfig (.ini) file, to better reflect the distinciton between the infrasturcture that experiment shots are executed on. The old keyword can still be used for this item, but a [warning](https://docs.python.org/3/library/exceptions.html#FutureWarning) will be issued to remind you to update your labconfig.


### Source code structure (developer installation)

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
* Module names remain underscored, e.g. labscript_devices and labscript_utils.
* The mixing of hyphen and underscores is inelegant but conventional.
* All references to blacs are now lowercase.
* As installation no longer requires a separate package, the repository formerly named ‘installer’ has been renamed to ‘[labscript-suite](https://github.com/labscript-suite/labscript-suite/issues)’, and is a metapackage for the *labscript suite* (installing it via `pip`/`conda` installs the suite).


### Versioning (developer installation)

Aside from the maintenance branches described [here](../contributing/#branching-model-strategy), versions of the labscript suite packages are introspected at run-time using either the [importlib.metadata](importlib.metadata) library (regular installations) or [setuptools_scm](https://github.com/pypa/setuptools_scm) (developer installations). Thus any changes to an editable install will be traceable by local version numbers, e.g. editing the released version of a package with version 2.4.0 will result in 2.4.0dev1+gc28fe94, for example. This will help us diagnose issues users have with their editable installations.
