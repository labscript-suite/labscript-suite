# Contributing to the Documentation

Author: (Enrique Mendez --  e q m at mit dot edu)

We could use your help! If you find some use case that's not covered yet in the 
documentations please add! This section is designed to be a tutorial on how to 
help add documentation.

## Get access to something you can Edit.

### 1. Fork all the Repositories.

Forking is the process of generating a copy of the labscript code base on your
own github account. This prevents accidental changes on the working code.

* To fork a github, login to your own account on github.
* Head to the repo you want to fork (https://github.com/labscript-suite/labscript-suite)
* Hit the fork button on the top right! That's it.

You now have your own personlal copy of the repository. This is where you can make
your own contributions!

### 2. Pull all your forks to your PC.

Now you just need to pull the git repositories (repos) to your PC for editing. 
Git management is easiest with (Sublime Merge)[https://www.sublimemerge.com]. I 
also recommend their text editor (Sublime Text 3)[https://www.sublimetext.com]. 
It's beautiful, runs fast, and has a community run set of packages for adding 
functionality that you find helpful 
(like (elastic-tabstops)[http://nickgravgaard.com/elastic-tabstops/]).

In Sublime Merge, (you might also need to login to your github account)

* Copy the https URL for the git, i.e. `https://github.com/labscript-suite/labscript-suite`
* Hit File > Clone Repository...
* Paste it into the Clone Repository > Source URL
* Adjust the source destination to your liking.
* Hit Clone!

You know have a local copy of your fork, and a Git Manager for keeping track of 
changes in a nice graphical way.

### 3. Create your own branch

* Click on the command bar at the top center of the window.
* Erase everything.
* Type `create` and hit Enter.
* Now type the name of your branch. In this case, `tut-contributing-docs` as
I'm planning on adding documentation on how to contribute documentation.
* Click on the command bar.
* Type `tut-contributing-docs` as `Checkout Branch` is the default command.


### 4. Commit often. Push/Pull occasionaly

* Login. Here you definitely need to log into a Git account, and one that has 
push pull privileges. 
* Be sure to commit any files you add or changes you make with helpful comments
on what you did.
* Pushing and Pulling synchronizes changes with the website version of your git.
* They shouldn't be done as often as commits as they are harder to undo if you make
a mistake. 

## Create an Editable Install of Labscript.

Sphinx requires the ability to import all the code to be documented. So we must
create a virtual environment to work in, and install labscript. So follow the 
developer install instructions for either Python Package Index or Anaconda Installation.

The Anaconda instructions are repeated here for explicitness and reproducibility.

### MacOS/Linux (Anaconda Installation) Instructions:

#### Create the Virtual Environment 

`conda create -n lsdocs python=3.8`
`conda activate lsdocs`

#### Removing the Virtual Environment

If you make a mistake

`conda deactivate`
`conda remove --name lsdocs --all`
#### Clone your Forked Repositories

First, make a location for storing your forks. Here I'll simply store it in the 
home directory.

`cd ~`

Then clone from your forked location. Your links will change. The formula is

`git clone <git-url-to-forked-repo>`

Installation Usage:

`git clone https://github.com/vvybclock/labscript-suite`
`cd ./labscript-suite/`
`git clone https://github.com/vvybclock/runmanager`
`git clone https://github.com/vvybclock/runviewer`
`git clone https://github.com/vvybclock/labscript`
`git clone https://github.com/vvybclock/lyse`
`git clone https://github.com/vvybclock/blacs`
`git clone https://github.com/vvybclock/labscript-devices`
`git clone https://github.com/vvybclock/labscript-utils`

Now, we need to edit the `.gitignore` that way it ignores all the imported sub
repos. 

Add the following lines to the `.gitignore` anywhere.

`#ignore labscript sub-gits
/labscript
/labscript-devices
/labscript-utils
/lyse
/runmanager
/runviewer
/blacs
`
`#ignore installed labscript files
/labconfig
/userlib
/app_saved_configs
`
`#ignore mac files
.DS_Store
`
#### Setup the Editable Install

`conda activate lsdocs`

##### Configure Anaconda.

First we istall all the requirements for labscript via piggy backing on the published
version of labscript.
`conda config --env --add channels labscript-suite`
`conda install setuptools-conda pyqt pip desktop-app`
`setuptools-conda install-requirements labscript runmanager blacs lyse runviewer
 labscript-devices labscript-utils `

Now, we install our local version of labscript via the editable install `-e` option.
So it's important to be in the folder that holds our clones.
`pip install --no-build-isolation --no-deps
 -e labscript -e runmanager -e blacs -e lyse
 -e runviewer -e labscript-devices -e labscript-utils`

Now we complete the installation.
`labscript-profile-create`

(Optional): We don't need this for documentation editing, and it might clutter your
experimental setup. It also doesnt seem to work on Mac.
`desktop-app install blacs lyse runmanager runviewer`

## Build and Test the Docs.

Before we can contribute, we need a working knowledge of the file structure and 
syntax of the documentation. If we know how to build the docs, we have access to 
a compiler than can check our syntax for us, which eliminates the need for finding
tutorials on how the docs work if you're more of an experimental coder.

Follow these (instructions)[https://www.sphinx-doc.org/en/master/usage/installation.html]
for installing sphinx.

Install the other modules needed:

* `pip install sphinx==3.0.1 sphinx-rtd-theme==0.4.3 recommonmark==0.6.0 m2r==0.2.1`
#### On MacOS, and (presumably) Linux:

* Mac Install: `brew install sphinx-doc`
* `cd ../forked-gits/labscript-suite/docs/`
* `make html`

On Mac, this pulled up a notification asking about python3.8 accepting incoming 
network connections. I allowed this. Why does it need network connection? pip?

* Make sure to clone the subrepos into `/labscript-suite/`. If you cloned into the
wrong location, just drag and drop the folders, and reopen them in Sublime Merge.
* Add these subrepo locations to the `.gitignore` file. So git doesn't bother 
you about keeping track of them.


## Contribute your own Edits.



## Push your Edits to the Main Repo.