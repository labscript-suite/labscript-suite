# Contributing to the *documentation*

We could use your help! If you find some use case that's not covered yet in the 
documentations please add! This section is designed to be a tutorial on how to 
help add documentation.

## Get access to something you can Edit

### 1. Fork all the Repositories.

Forking is the process of generating a copy of the labscript code base on your
own github account. This prevents accidental changes on the working code.

* To fork a github, login to your own account on github.
* Head to the repo you want to fork, i.e., [labscript-suite]
(https://github.com/labscript-suite/labscript-suite)
* Hit the fork button on the top right! That's it.

You now have your own personal copy of the repository. This is where you can make
your own contributions!

### 2. Pull all your forks to your PC.

Now you just need to pull the git repositories (repos) to your PC for editing. 
Git management is easiest with [Sublime Merge](https://www.sublimemerge.com). I 
also recommend their text editor [Sublime Text 3](https://www.sublimetext.com). 
It's beautiful, runs fast, and has a community run set of packages for adding 
functionality that you find helpful 
(like [elastic-tabstops](http://nickgravgaard.com/elastic-tabstops/)).

In Sublime Merge, (you might also need to login to your github account)

* Copy the https URL for the git, i.e. `https://github.com/labscript-suite/labscript-suite`
* Hit File > Clone Repository...
* Paste it into the Clone Repository > Source URL
* Adjust the source destination to your liking.
* Hit Clone!

You now have a local copy of your fork, and a Git Manager for keeping track of 
changes in a nice graphical way.

### 3. Create your own branch.

* Click on the command bar at the top center of the window.
* Erase everything.
* Type `create` and hit Enter.
* Now type the name of your branch. In this case, `tut-contributing-docs` as
I'm planning on adding documentation on how to contribute documentation.
* Click on the command bar.
* Type `tut-contributing-docs` as `Checkout Branch` is the default command.


### 4. Commit often. Push/Pull occasionally.

* Login. Here you definitely need to log into a Git account, and one that has 
push pull privileges. 
* Be sure to commit any files you add or changes you make with helpful comments
on what you did.
* Pushing and Pulling synchronizes changes with the website version of your git.
* They shouldn't be done as often as commits as they are harder to undo if you make
a mistake. 

## Create an Editable Install of Labscript

Sphinx requires the ability to import all the code to be documented. So we must
create a virtual environment to work in, and install labscript. So follow the 
developer install instructions for either Python Package Index or Anaconda Installation.
This editable install allows us to edit the labscript-code in a way that is also
executable and improvable. Necessary for documenting, if not also improving the 
code base.

The Anaconda instructions are repeated here for explicitness and reproducibility.

### (Anaconda Installation) Instructions

#### Create the Virtual Environment.

Create our environment for the sole purpose of documentation `lsdocs`.

```
conda create -n lsdocs python=3.8
conda activate lsdocs
```

#### Removing the Virtual Environment.

If you make a mistake

```
conda deactivate
conda remove --name lsdocs --all
```

#### Clone your Forked Repositories.

If you haven't already, make a location for storing your forks. Here I'll simply
store it in the home directory.

`cd ~`

Then clone from your forked location. Your links will change. The formula is

`git clone <git-url-to-forked-repo>`

Installation Usage:

If you haven't already clone the suite repo into the directory of your choice.
```
git clone https://github.com/vvybclock/labscript-suite
cd ./labscript-suite/
```

If you're using Sublime Merge as recommended clone these repos into the labscript-
suite folder.

```
git clone https://github.com/vvybclock/runmanager
git clone https://github.com/vvybclock/runviewer
git clone https://github.com/vvybclock/labscript
git clone https://github.com/vvybclock/lyse
git clone https://github.com/vvybclock/blacs
git clone https://github.com/vvybclock/labscript-devices
git clone https://github.com/vvybclock/labscript-utils
```
Now, we need to edit the `.gitignore` that way it ignores all the imported sub
repos. This is assuming the `.gitignore` hasn't updated by now.

Add the following lines to the `.gitignore` anywhere. This prevents git from 
hounding you on 'untracked' changes that are tracked by their respective 
repositories.

```
#ignore labscript sub-gits
/labscript
/labscript-devices
/labscript-utils
/lyse
/runmanager
/runviewer
/blacs

#ignore installed labscript files
/labconfig
/userlib
/app_saved_configs

#ignore mac files
.DS_Store
```
#### Setup the Editable Install

Activate the virtual environment.

`conda activate lsdocs`

##### Configure Anaconda.

First, we install all the requirements for labscript via piggy backing on the published
version of labscript.

```
conda config --env --add channels labscript-suite
conda install setuptools-conda pyqt pip desktop-app
setuptools-conda install-requirements labscript runmanager blacs lyse runviewer
 labscript-devices labscript-utils 
```

Now, we install our local version of labscript via the editable install `-e` option.
So it's important to be in the folder that holds our clones.
```
pip install --no-build-isolation --no-deps
 -e labscript -e runmanager -e blacs -e lyse
 -e runviewer -e labscript-devices -e labscript-utils
```

Now we complete the installation.
`labscript-profile-create`

(Optional): We don't need this for documentation editing, and it might clutter your
experimental setup. It also doesnt seem to work on Mac.
`desktop-app install blacs lyse runmanager runviewer`

## Build and Test the Docs

Before we can contribute, we need a working knowledge of the file structure and 
syntax of the documentation. If we know how to build the docs, we have access to 
a compiler than can check our syntax for us, which eliminates the need for finding
tutorials on how the docs work if you're more of an experimental coder.

Follow these [instructions](https://www.sphinx-doc.org/en/master/usage/installation.html)
for installing sphinx if what's written here isn't sufficient for you.

Install the other modules needed:

* `pip install sphinx==3.0.1 sphinx-rtd-theme==0.4.3 recommonmark==0.6.0 m2r==0.2.1`

#### On MacOS and Linux

* Mac Install: `brew install sphinx-doc`
* Ubuntu/Debian (untested): `apt-get install python3-sphinx`
* `cd ~/labscript-suite/docs/`
* `conda activate lsdocs`
* `make html`

On Mac, this pulled up a notification asking about python3.8 accepting incoming 
network connections. I allowed this. Why does it need network connection? pip?

* Make sure to clone the subrepos into `/labscript-suite/`. If you cloned into the
wrong location, just drag and drop the folders, and reopen them in Sublime Merge.
* Add these subrepo locations to the `.gitignore` file. So git doesn't bother 
you about keeping track of them.

### Changing the makefile.

*To be completed*

## Contribute your own Edits

Hopefully, you were welcomed with a successful build of the documentation.
Sphinx builds upon the reStructuredText language (.rst). A fully fledge tutorial
[can be found here](https://www.sphinx-doc.org/en/master/usage/quickstart.html).

It's easy to write documentation in markdown language. It's basically fancy plain
text. A quick google will easily get you well on your way. 

Essentially the docs are just made of `.rst` files and `.md` (markdown). You are
free to choose either language to write up your documentation. The hearts are
the `index.rst` and the `conf.py` files. The `conf.py` file specifies how the
docs will be built.

The menus are defined via these `.. toctree::` commands held in the `index.rst`
files. Note that one needs only the root of the filename to the list to have 
it show up in the docs!

You can use what ever folders or filenames you see fit for helping organize the 
documentation.

Build to see your beautiful contribution to the labscript suite! If you wish to 
see how someone implemented the docs that exist already just hit the `View page source`
button that exists in the top right of each docs page.


## Push your Edits to the Main Repo

Once you're happy with the progress in your branch, ensure it is pushed to your 
remote fork.

Once that's the case, you can easily make a pull request on the website.
You just need to select the branch you wish to merge on the main page. For us, 
it's `tut-contributing-docs`. Just underneath the branch selector, a message will
appear: `This branch is 4 commits ahead of labscript-suite:master.` Select `Pull
request`.

Title and document your pull request! The syntax is also in markdown. Be sure to
merge with `master` on the parent labscript-repo.

Congratulations, you helped make the world a better place!