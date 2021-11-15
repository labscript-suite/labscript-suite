Committing Docs
===============

Committing documentation updates/fixes is an important way to contribute to the **labscript-suite** community.
Increasing the amount of technical details in the documentation that are necessary to use the suite but are not obvious from the source is of particular value.

The mechanics of committing documentation to a **labscript-suite** component is nearly identical to committing general code updates/fixes:
:doc:`a pull request needs to be created </contributing>`.
The main difference is that documentation changes necessitate checking the read the docs builds to confirm what was desired actually makes it into the on-line documentation as intended.

Making a PR
-----------

The general steps for creating the PR are outlined in :doc:`here <contributing>`. 
When making PRs with documentation changes, a few extra checks are required.
In particular, it is a good idea to locally build the documentation as described :doc:`here <docs_build>`.
If you cannot build locally, the docs will be built automatically for your PR by Read the Docs and can be viewed there (described below).

Checking the RTD Builds
-----------------------

When a PR is created or updated with new commits, an automated check of the documentation build is performed by Read the Docs.
The result of this build can be viewed online by looking at the details of the automated checks.
If the build is completed, this link will take you directly to the home page of your built documentation.
If the build is still in progress, this link will take you to the build progress which shows the commands being run and their outputs.
If you wish to see this progress after the build succeeds, you can find it by clicking the bottom left corner of the Read the Docs page.
This will bring up a small window pane.
Selecting 'Builds' will bring up the build logs for all of the online builds.
If the build did not succeed, this link takes you to the build progress stage with the failing command and corresponding outputs displayed.

Note that Read the Docs will only build the html documentation for a pull request.
When the pull request is merged, Read the Docs will build the html documentation again, as well as downloadable pdf and epub versions.
These downloads are available via the 'Downloads' link next to the 'Builds' link in the bottom left corner pop-up pane on-line.