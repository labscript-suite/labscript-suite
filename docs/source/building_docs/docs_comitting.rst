Committing Docs
===============

Committing documentation updates/fixes is an important way to contribute to the **labscript-suite** community.
Increasing the amount of technical details in the documentation that are necessary to use the suite but are not obvious from the source is of particular value.

The mechanics of committing documentation to a **labscript-suite** component is nearly identical to committing general code updates/fixes:
:doc:`a pull request needs to be created </contributing>`.
The main difference is that documentation changes necessitate checking the read the docs builds to confirm what was desired actually makes it into the on-line documentation as intended.

Making a PR
-----------

The process of making a pull request (PR) on GitHub is thoroughly documented in many places online.
The **labscript-suite** PR process uses a fork collaboration model.
The official GitHub documentation outlining this process is available `here <https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork>`_.

The general steps are:

#. **Create a fork of the repository you intend to work on** (if you do not already have one).
#. **Create a named branch off of the current master branch.**
   It is good practice to use a unique, brief, yet descriptive, name for this branch.
#. **Check out this branch and commit code to it.**
   It is good practice to commit often to this branch to avoid very large diffs in a single commit that are hard to analyse.
   Ideally, your commits should accomplish a single thing at a time.
   It is also good to include detailed commit messages that explain the intended purpose of the commit and details of any specific usage changes, if necessary.
#. **Once you feel your changes are complete, please ensure they are well tested**.
   This includes ensuring your proposed changes actually do what you think they should.
   It also includes ensuring other components are not negatively affected by your changes.
   When making changes to documentation, it is a good idea to locally build the documentation as described :doc:`here <docs_build>`.
   If you cannot build locally, the docs will be built automatically for your PR by Read the Docs and can be viewed there (described below).
#. **Push your commits to your fork.**
   This can be done at any time in this process, but it must be done at least once at the end to ensure your changes are made available on GitHub for the PR.
#. **With changes complete, tested and pushed to your fork, you create the PR**.
   This can be done in a few ways, but here we describe (briefly) how this is done via the web interface.
   Detailed documenation of this process is available at the link above.

   #. When you go the home page of your fork, you will see a notice that there are new changes to a branch on your fork, do you want to merge?
      You can also access the PR creation menu by going to the original **labscript-suite** component and selecting Pull Request.
   #. You next select which branch of your fork you would like to merge into which branch of the upstream fork.
      Ensure you select your fork you wish to commit and the master branch of of the upstream **labscript-suite** component repository.
   #. Fill in a descriptive title for your proposed changes and a description of the changes you have made.
   #. Select "Create Pull Request".
      Your PR is now created and the **labscript-suite** core developers will be notified.

#. **The core dev team will review the changes, and often ask for changes.**
   By pushing new commits to the same branch as that used by the PR, those changes will automatically be added to the PR.
#. **Once all concerns are addressed, the PR can be merged by the core dev team.**
   Note that the dev team may decide that your PR should not be merged, and ultimately reject it.
   We will do our best to explain the rationale behind this decision.
   You are obviously welcome to use your code within your own installation of the **labscript-suite**, even if it is not merged into the upstream mainline.
   Please do not take a rejected PR personally.

Checking the RTD Builds
-----------------------

When a PR is created or updated with new commits, an automated check of the documentation build is performed by Read The Docs.
The result of this build can be viewed online by looking at the details of the automated checks.
If the build is completed, this link will take you directly to the home page of your built documentation.
If the build is still in progress, this link will take you to the build progress which shows the commands being run and their outputs.
If you wish to see this progress after the build succeeds, you can find it by clicking the bottom left corner of the Read the Docs page.
This will bring up a small window pane.
Selecting builds will bring up the build logs for all of the online builds.

Note that Read the Docs will only build the html documentation for a pull request.
When the pull request is merged, Read the Docs will build the html documentation again, as well as downloadable pdf and epub versions.
These downloads are available via the 'Downloads' link next to the 'Builds' link in the bottom left corner pop-up pane on-line.