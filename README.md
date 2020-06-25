# the _labscript suite_

<a href="https://github.com/labscript-suite/labscript"><img src="https://raw.githubusercontent.com/labscript-suite/labscript-suite/master/art/labscript_32nx32n.svg" height="64" alt="the labscript suite – labscript"></a> <a href="https://github.com/labscript-suite/runmanager"><img src="https://raw.githubusercontent.com/labscript-suite/labscript-suite/master/art/runmanager_32nx32n.svg" height="64" alt="the labscript suite – runmanager"></a> <a href="https://github.com/labscript-suite/blacs"><img src="https://raw.githubusercontent.com/labscript-suite/labscript-suite/master/art/blacs_32nx32n.svg" height="64" alt="the labscript suite – blacs"></a> <a href="https://github.com/labscript-suite/lyse"><img src="https://raw.githubusercontent.com/labscript-suite/labscript-suite/master/art/lyse_32nx32n.svg" height="64" alt="the labscript suite – lyse"></a> <a href="https://github.com/labscript-suite/runviewer"><img src="https://raw.githubusercontent.com/labscript-suite/labscript-suite/master/art/runviewer_32nx32n.svg" height="64" alt="the labscript suite – runviewer"></a>

### Experiment control and automation system

[![Actions Status](https://github.com/labscript-suite/labscript-suite/workflows/Build%20and%20Release/badge.svg?branch=maintenance%2F3.0.x)](https://github.com/labscript-suite/labscript-suite/actions)
[![Documentation Status](https://readthedocs.org/projects/labscriptsuite/badge/?version=latest)](https://docs.labscriptsuite.org)
[![License](https://img.shields.io/pypi/l/labscript-suite.svg)](https://github.com/labscript-suite/labscript-suite/raw/master/LICENSE.txt)
[![Python Version](https://img.shields.io/pypi/pyversions/labscript-suite.svg)](https://python.org)
[![PyPI](https://img.shields.io/pypi/v/labscript-suite.svg)](https://pypi.org/project/labscript-suite)
[![Conda Version](https://img.shields.io/conda/v/labscript-suite/labscript-suite)](https://anaconda.org/labscript-suite/labscript-suite)
[![Google Group](https://img.shields.io/badge/Google%20Group-labscriptsuite-blue.svg)](https://groups.google.com/forum/#!forum/labscriptsuite)
[![DOI](https://img.shields.io/badge/DOI-10.1063%2F1.4817213-0F79D0.svg)](https://doi.org/10.1063/1.4817213)


The _labscript suite_ is a powerful and extensible framework for experiment [composition](https://github.com/labscript-suite/labscript), [control](https://github.com/labscript-suite/runmanager), [execution](https://github.com/labscript-suite/blacs), and [analysis](https://github.com/labscript-suite/lyse). Developed for quantum science and quantum engineering; deployable in laboratory and in-field devices. Also applicable to optics, microscopy, materials engineering, biophysics, and any application predicated on the repetition of parameterised, hardware-timed experiments.

This is a metapackage for the _labscript suite_. Formerly the _labscript suite_ installer repository, prior to the packages being installable via [PyPI](https://pypi.org/user/labscript-suite) and [Anaconda Cloud](https://anaconda.org/labscript-suite).


#### Features:
- Flexible and automated oversight of heterogeneous hardware.
- The most mature and widely used open-source control system in quantum science.
- Multiple analysis-based feedback modes.
- Extensible plugin architecture (e.g. machine learning online optimisation).
- Readily integrates with other software, including image acquisition, analysis, and even other control systems.
- Compose experiments as human-readable Python code, leveraging modularity, revision control and re-use.
- Dynamic visualisation of experiment composition and results.
- Remote operation: different modules can run on physically separate hosts / single modules can be run on multiple hosts (including hardware supervisor, [blacs](https://github.com/labscript-suite/blacs)).
- Auto-generating user-interfaces.
- High-level scripting: user-interface interaction can be programatically synthesised.

## Table of contents

- [Installing the _labscript suite_](#installing-the-labscript-suite)
- [Recent changes to the _labscript suite_](#recent-changes-to-the-labscript-suite)
  - [Profile directories](#profile-directories)
  - [Secure communication](#secure-communication)
  - [Application shortcuts](#application-shortcuts)
  - [Source code structure (developer installation)](#source-code-structure-developer-installation)
  - [Versioning (developer installation)](#versioning-developer-installation)
- [BitBucket archive](#bitbucket-archive)
- [Contributing to the _labscript suite_](#contributing-to-the-labscript-suite)
  - [Issue tracking](#issue-tracking)
  - [Request for developers](#request-for-developers)
- [Citing the _labscript suite_](#citing-the-labscript-suite)

## Installing the _labscript suite_

We're excited to announce that accompanying the recent migration to GitHub, _labscript suite_ components are now distributed as Python packages on [PyPI](https://pypi.org/user/labscript-suite) and [Anaconda Cloud](https://anaconda.org/labscript-suite).

This makes it far easier to get started using the _labscript suite_, as you no longer require a Mercurial or Git installation (or any knowledge of version control software); components can be installed and upgraded using:

* [`pip`](https://packaging.python.org/tutorials/installing-packages): the standard package manager common to all Python distributions; or
* [`conda`](https://anaconda.org/anaconda/conda): a binary package and environment manager, part of the [Anaconda Python](https://www.anaconda.com) distribution.

For further information, please see the [documentation](http://docs.labscriptsuite.org/en/latest/installation), which includes information about both regular and developer (editable) installations of the *labscript suite*.

## Recent changes to the _labscript suite_

Upon migrating the code base to GitHub and publishing distributions on PyPI in April–May 2020, existing users should be aware of the following recent changes.

### Profile directories

The _labscript suite_ profile directory, containing application configurations, logs, and user-side code, is now located by default in the current user's home directory, e.g. for a local user named `wkheisenberg` this is:

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

This structure is created by calling the command `labscript-profile-create` in a terminal after installing `labscript-utils` (per the [installation instructions](http://docs.labscriptsuite.org/en/latest/installation#regular-installation-from-the-python-package-index)).

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

Aside from the maintenance branches documented [here](http://docs.labscriptsuite.org/en/latest/contributing/#branching-model-strategy), versions of the labscript suite packages are introspected at run-time using either the [importlib.metadata](importlib.metadata) library (regular installations) or [setuptools_scm](https://github.com/pypa/setuptools_scm) (developer installations). Thus any changes to an editable install will be traceable by local version numbers, e.g. editing the released version of a package with version 2.4.0 will result in 2.4.0dev1+gc28fe94, for example. This will help us diagnose issues users have with their editable installations.


## BitBucket archive

In April–May 2020 the _labscript suite_ code base was migrated from BitBucket to GitHub. All commit history and issues was preserved, however some repository metadata (such as pull request discussions) could not be migrated directly. As such, we have created an archived copy of everything that was on BitBucket. This includes:

* Issues (as they appear on BitBucket);
* Pull requests discussions;
* Commit comments for every labscript suite repository; and
* Every public fork (as of 1st February, 2020).

This archive can be found at [bitbucket-archive.labscriptsuite.org](https://bitbucket-archive.labscriptsuite.org/) (this page can take some time to load for the first time). Copies of every public fork of our repositories are at [github.com/labscript-suite-bitbucket-archive](https://github.com/labscript-suite-bitbucket-archive). As this is an archive, we will not be transferring ownership of these repositories back to their original owners. However, should you wish to continue development on one of those repositories you can fork it into your own account through the GitHub web interface. Should you have uncommitted changes (or changes made after 1st February, 2020) that you wish to have archived, please contact us to discuss the best approach to including these. Please note that we are not recommending continuing development in such forks long term, due to the changes in package structure outlined above.

Further information about migrating your own customisations of the labscript suite can be found [here](https://docs.labscriptsuite.org/en/latest/archive/).


## Contributing to the _labscript suite_

We are very grateful for all the contributions users have made in the past decade to make the _labscript suite_ the most widely used open-source experiment control and automation system in quantum science. These include development, suggestions, and feedback, and we look forward to this continuing on GitHub.


### Issue tracking

The issue tracking on GitHub is very similar to BitBucket, with the added advantage that you can add inter-repository issue references, e.g. referring to [labscript-suite/runmanager#68](https://github.com/labscript-suite/runmanager/issues/68) in any issue or pull request will link to the corresponding issue. We have imported all issues from the BitBucket repositories into the GitHub repositories. This import is not perfect (as each comment is now posted by Phil Starkey) but the comments have been modified to contain the original author attribution. We have also updated all links to files, pull requests, issues, and commits so that they point to the equivalent GitHub location and/or the archived copy of the data (as discussed above).

Please use the issue tracker of the relevant GitHub repository for:

* Reporting **bugs** (when something doesn't work or works in a way you didn't expect);
* Suggesting **enhancements**: new features or requests;
* Issues relating to **installation**, **performance**, or **documentation**.

For advice on _how_ to use the existing functionality of the _labscript suite_, please use our [mailing list](http://groups.google.com/group/labscriptsuite).


### Request for developers

We would like to reaffirm our invitation for users to directly contribute toward developing the _labscript suite_. We have established a separate discussion forum on Zulip for discussing development direction and design. If you are interested in being a part of these discussions, and/or testing and merging pull requests, please [reach out to us](mailto:labscriptsuite@gmail.com).

Further guidance on contributing—including the branching model we use, and the procedure for issuing pull requests—can be found in the [documentation](http://docs.labscriptsuite.org/en/latest/contributing).


## Citing the _labscript suite_

If you use the _labscript suite_ to control your experiment or perform analysis, please cite one or more of the following publications:

<!-- 1. _A scripted control system for autonomous hardware-timed experiments,_ [Review of Scientific Instruments **84**, 085111 (2013)](https://doi.org/10.1063/1.4817213). arXiv: [1303.0080](http://arxiv.org/abs/1303.0080). -->

<details>
  <summary>P. T. Starkey, <em><a href="https://doi.org/10.26180/5d1db8ffe29ef">A software framework for control and automation of precisely timed experiments</a>.</em>  PhD thesis, Monash University (2019).</summary>

  ```bibtex
    @phdthesis{starkey_phd_2019,
      title = {State-dependent forces in cold quantum gases},
      author = {Starkey, P. T.},
      year = {2019},
      url = {https://doi.org/10.26180/5d1db8ffe29ef},
      doi = {10.26180/5d1db8ffe29ef},
      school = {Monash University},
    }
  ```
</details>

<details>
  <summary>C. J. Billington, <em><a href="https://doi.org/10.26180/5bd68acaf0696">State-dependent forces in cold quantum gases</a>.</em>  PhD thesis, Monash University (2018).</summary>

  ```bibtex
    @phdthesis{billington_phd_2018,
      title = {State-dependent forces in cold quantum gases},
      author = {Billington, C. J.},
      year = {2018},
      url = {https://doi.org/10.26180/5bd68acaf0696},
      doi = {10.26180/5bd68acaf0696},
      school = {Monash University},
    }
  ```
</details>

<details>
  <summary><em><a href="https://doi.org/10.1063/1.4817213">A scripted control system for autonomous hardware-timed experiments</a>,</em> Review of Scientific Instruments <b>84</b>, 085111 (2013). arXiv:<a href="http://arxiv.org/abs/1303.0080">1303.0080</a>.</summary>

  ```bibtex
    @article{labscript_2013,
      author = {Starkey, P. T. and Billington, C. J. and Johnstone, S. P. and
                Jasperse, M. and Helmerson, K. and Turner, L. D. and Anderson, R. P.},
      title = {A scripted control system for autonomous hardware-timed experiments},
      journal = {Review of Scientific Instruments},
      volume = {84},
      number = {8},
      pages = {085111},
      year = {2013},
      doi = {10.1063/1.4817213},
      url = {https://doi.org/10.1063/1.4817213},
      eprint = {https://doi.org/10.1063/1.4817213}
    }
  ```
</details>
