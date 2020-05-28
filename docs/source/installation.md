## Installing the _labscript suite_

We're excited to announce that accompanying the recent migration to GitHub, _labscript suite_ components are now distributed as Python packages on [PyPI](https://pypi.org/user/labscript-suite) and [Anaconda Cloud](https://anaconda.org/labscript-suite).

This makes it far easier to get started using the _labscript suite_, as you no longer require a Mercurial or Git installation (or any knowledge of version control software); components can be installed and upgraded using:

* [`pip`](https://packaging.python.org/tutorials/installing-packages): the standard package manager common to all Python distributions; or 
* [`conda`](https://anaconda.org/anaconda/conda): a binary package and environment manager, part of the [Anaconda Python](https://www.anaconda.com) distribution.


### Virtual environments

We recommend installing labscript (regular or developer mode) in a [virtual environment](https://packaging.python.org/tutorials/installing-packages/#creating-virtual-environments). This helps sandbox the codebase without interfering with (or being interfered with) your system Python installation, or Python environments used for other purposes. There are a number of ways to configure a virtual environment. If you are unfamiliar with doing so, we recommend using the [venv module](https://docs.python.org/3/library/venv.html), part of the Python Standard Library. Here's an example (on Windows):


#### Quick start

```
C:\> mkdir labscript-suite
C:\> cd labscript-suite
C:\labscript-suite> python -m venv .venv
C:\labscript-suite> .venv\Scripts\activate
(.venv) C:\labscript-suite> python -m pip install --upgrade pip setuptools wheel
```
Once activated, the name of the virtual environment (in this case, `.venv`) will prefix the command line.


#### Detailed instructions

1. From a new terminal, create the installation directory and enter it. Here we use `C:\labscript-suite` but this can be whatever you like:

    ```
    C:\> mkdir labscript-suite
    C:\> cd labscript-suite
    ```

2. Create a virtual environment. Here we name it `.venv`, located inside the installation directory (name and location are also variable but these are conventional choices).

    ```
    C:\labscript-suite> python -m venv .venv
    ```

3. Activate the virtual environment:

    ```
    C:\labscript-suite> .venv\Scripts\activate
    ```

    _Note:_ This step is OS specific, e.g. on Linux it's `source .venv/bin/activate`.

4. Update the Python package installer and other installation packages of your virtual environment.

    ```
    (.venv) C:\labscript-suite> python -m pip install --upgrade pip setuptools wheel
    ```


### Regular installation from the Python Package Index

If you are using a virtual environment ([above](#virtual-environments)), activate it before executing the following commands. In this example, we will use the installation directory `C:\labscript-suite` with an existing virtual environment, not yet activated (skip the first two lines/steps if continuing on from above).


#### Quick start

```
C:\labscript-suite> .venv\Scripts\activate
(.venv) C:\labscript-suite> python -m pip install --upgrade pip setuptools wheel
(.venv) C:\labscript-suite> pip install labscript-suite
(.venv) C:\labscript-suite> pip install PyQt5
(.venv) C:\labscript-suite> labscript-profile-create
(.venv) C:\labscript-suite> desktop-app install blacs lyse runmanager runviewer
```


#### Detailed instructions

1. Activate the virtual environment (this step is OS specific, e.g. on Linux it's `source .venv/bin/activate`).

    ```
    C:\labscript-suite> .venv\Scripts\activate
    ```

2. Update the Python package installer and other installation packages of your virtual environment.

    ```
    (.venv) C:\labscript-suite> python -m pip install --upgrade pip setuptools wheel
    ```

3. Install the meta-package from PyPI. This will install blacs, labscript, labscript-devices, labscript-utils, lyse, runmanager, runviewer, and all dependencies (except the bindings to the GUI toolkit and device-driver specific packages):

    ```
    (.venv) C:\labscript-suite> pip install labscript-suite
    ```

4. Install PyQt5, the bindings to the GUI toolkit (not installed above for licensing reasons):

    ```
    (.venv) C:\labscript-suite> pip install PyQt5
    ```

5. Create a profile directory in your home directory (the new location of user data; more [below](#changes-to-profile-directories)):

    ```
    (.venv) C:\labscript-suite> labscript-profile-create
    ```

6. (Optional) Create shortcuts for the GUI applications (blacs, lyse, runmanager, and runviewer) and place them in the start-menu (or non-Windows OS equivalent).

    ```
    (.venv) C:\labscript-suite> desktop-app install blacs lyse runmanager runviewer
    ```

    These will be named, e.g. ‘runmanager – the labcript suite’ which when clicked on will:

   * Launch the application without a terminal window, using the virtual environment the above command was called in.
   * Display the application with an application-specific shortcut in the taskbar (which can be pinned, like any other desktop application).

    Virtual environments named anything other than `.venv` will be included in the name of the shortcut, e.g. ‘runmanager – the labscript suite (py38)’ for a virtual environment named `py38`.

Alternatively, you can launch the applications from a terminal, e.g. 

```
(.venv) C:\> runmanager
```

This will print debugging information to the console.

To launch the applications detached from the console, suffix the application name with `-gui`, e.g.

```
(.venv) C:\> runmanager-gui
```

_Note:_ You must have activated the virtual environment in which the _labscript suite_ was installed to use these commands.


#### Updating a regular installation

Individual components of the labscript suite can be updated using the `--upgrade` (`-U`) flag of `pip`. For example:

```
(.venv) C:\labscript-suite> pip install -U runmanager
```

To upgrade to a pre-release version, you can use the `--pre` (pre-relase) flag:

```
(.venv) C:\labscript-suite> pip install -U --pre runmanager
```

If updating multiple components, use a single pip install command for this to ensure dependency resolution is best dealt with:

```
(.venv) C:\labscript-suite> pip install -U labscript lyse runmanager
```

You can also update (or downgrade) to a specific version:

```
(.venv) C:\labscript-suite> pip install runmanager==2.5.0
```

Development versions will be suffixed with `devN`, i.e.

```
(.venv) C:\labscript-suite> pip install runmanager==2.6.0dev3
```


### Developer installation (for those who want to customize the _labscript suite_)

_Note:_ You do not necessarily need not fork, clone, and install editable versions of all _labscript suite_ repositories to customise your installation and/or contribute these changes back to the base repositories. For example, if you only want to develop custom labscript device drivers, you might only fork and clone the labscript-devices repository. Moreover, there is now an option to write and use custom labscript device drivers outside of the labscript-devices installation directory.


#### Quick start

_Coming soon!_


#### Detailed instructions

1. Fork the labscript-suite repositories you want to develop using the [GitHub online](https://help.github.com/en/github/getting-started-with-github/fork-a-repo). Below we will include all repositories (except the labscript-suite metapackage).

2. Use `pip` to both clone these forks locally and install them into your environment. In this example (on Linux), the forks are owned by the (non-existent) GitHub user wkheisenberg.

    ```
    $ pip install \
    --src . -e git+https://github.com/wkheisenberg/blacs#egg=blacs \
    --src . -e git+https://github.com/wkheisenberg/labscript#egg=labscript \
    --src . -e git+https://github.com/wkheisenberg/labscript-devices#egg=labscript-devices \
    --src . -e git+https://github.com/wkheisenberg/labscript-utils#egg=labscript-utils \
    --src . -e git+https://github.com/wkheisenberg/runmanager#egg=runmanager \
    --src . -e git+https://github.com/wkheisenberg/runviewer#egg=runviewer \
    --src . -e git+https://github.com/wkheisenberg/lyse#egg=lyse
    ```

    _Notes:_

    *   This will set your forked repository(ies) to be the ‘origin’ remote.
    *   On Windows the line continuation character is `^` rather than `\`.

    Alternatively, manually clone the repositories using <code>[git clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)</code> and then install them using `pip` by running the following from the common parent directory:

    ```
    $ pip install -e blacs -e labscript -e labscript-devices -e labscript-utils \
        -e lyse -e runmanager -e runviewer
    ```

    For a single package, this would look like:

    ```
    $ git clone https://github.com/wkheisenberg/runmanager.git
    $ pip install -e runmanager
    ```

3. For each repository, set the upstream remote to the base labscript-suite repository:


    ```
    $ cd blacs
    $ git remote add upstream https://github.com/labscript-suite/blacs.git
    $ cd ..
    ```

    Repeat for the other repositories.

4. Continue from step 4 (install PyQt5) in the [regular installation instructions](#regular-installation-from-the-python-package-index).


#### Updating a developer installation

This assumes you have already completed the developer installation above and have:

*   Forked a _labscript suite_ repository on GitHub;
*   Cloned the repository;
*   Set your fork to be the ‘origin’ remote; and
*   Set the labscript-suite base repository to be the ‘upstream’ remote.

1. Use one of the following to keep your repository (and feature branches) up-to-date:

    [Fetch changes, and merge](https://help.github.com/en/github/using-git/getting-changes-from-a-remote-repository#fetching-changes-from-a-remote-repository) with your local master branch.

    ```
    $ git checkout master
    $ git fetch upstream master --tags
    $ git merge upstream/master
    ```

    Or using [Git Pull](https://help.github.com/en/github/using-git/getting-changes-from-a-remote-repository#pulling-changes-from-a-remote-repository):

    ```
    $ git checkout master
    $ git pull upstream master --tags
    ```

    Or using [hub sync](https://hub.github.com/) command-line extension (does not require current local working branch to be master):

    ```
    $ hub sync
    ```

2. Update your feature branches by merging them with master or rebasing them to master:

    ```
    $ git checkout your-feature-name
    $ git merge master <OR> git rebase master --autostash
    ```

3. Update your fork by [pushing](https://help.github.com/en/github/using-git/pushing-commits-to-a-remote-repository) any changes resulting from steps 1–2 and/or subsequent local development:

    ```
    $ git checkout master
    $ git push origin master --tags
    $ git checkout your-feature-name
    $ git push origin your-feature-name master
    ```

    _Note:_ If the feature branch has not yet been created on your fork, you need to include `-u` above, i.e.

    ```
    $ git push -u origin your-feature-name
    ```

4. Checkout the commit you want to install. This might be a specific release version (which can be specified by tag):

    ```
    $ git checkout v0.3.2
    ```

    ... or using the commit SHA:

    ```
    $ git checkout 59651b5
    ```

5. (Optional) Update the package using (from within the root of a repository):

    ```
    $ pip install -e .
    ```

    As the installations are in editable mode and the version is being introspected at runtime, this step is not always necessary, but is required for any change requiring setup.py to be run to take effect, e.g. dependency changes, console entry points, etc.