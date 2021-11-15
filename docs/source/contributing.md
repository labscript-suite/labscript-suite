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


### Pull requests

We will continue the same feature-branch workflow as before.

1. **[Fork](https://guides.github.com/activities/forking/) one or more of the labscript suite repositories.**
2. **Create a named branch on your fork for a new feature.**
   It is good practice to use a unique, brief, yet descriptive, name for this branch.
3. **Check out this branch and commit code to it.**
   It is good practice to commit often to this branch to avoid very large diffs in a single commit that are hard to analyse.
   Ideally, your commits should accomplish a single thing at a time.
   It is also good to include detailed commit messages that explain the intended purpose of the commit and details of any specific usage changes, if necessary.
4. **Once you feel your changes are complete, please ensure they are well tested**.
   This includes ensuring your proposed changes actually do what you think they should.
   It also includes ensuring other components are not negatively affected by your changes.
5. **Push your commits to your fork.**
   This can be done at any time in this process, but it must be done at least once at the end to ensure your changes are made available on GitHub for the PR. 
6. **With changes complete, tested and pushed to your fork, you create the PR**.
   This can be done in a few ways, but here we describe (briefly) how this is done via the web interface.
   Detailed documenation of this process is available at the links below.

   1. When you go the home page of your fork, you will see a notice that there are new changes to a branch on your fork, do you want to merge?
      You can also access the PR creation menu by going to the original **labscript-suite** component and selecting Pull Request.
   2. You next select which branch of your fork you would like to merge into which branch of the upstream fork.
      Ensure you select your fork that you wish to commit and the master branch of of the upstream **labscript-suite** component repository.
   3. Fill in a descriptive title for your proposed changes and a description of the changes you have made.
   4. Select "Create Pull Request".
      Your PR is now created and the **labscript-suite** core developers will be notified.

7. **The core dev team will review the changes, and often ask for changes.**
   By pushing new commits to the same branch as that used by the PR, those changes will automatically be added to the PR.
8. **Once all concerns are addressed, the PR can be merged by the core dev team.**
   Note that the dev team may decide that your PR should not be merged, and ultimately reject it.
   We will do our best to explain the rationale behind this decision.
   You are obviously welcome to use your code within your own installation of the **labscript-suite**, even if it is not merged into the upstream mainline.
   Please do not take a rejected PR personally.

The official GitHub documentation outlining this process is available [here](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).
These steps are broadly covered in the GitHub [Hello World](https://guides.github.com/activities/hello-world/) guide, and in detail on the [NumPy development workflow](https://numpy.org/doc/stable/dev/development_workflow.html).


### Branching model/strategy

The move to GitHub for source control and PyPI for distribution is accompanied by a slight change in the branching strategy, to improve deployment and stability of the _labscript suite_. Whereas before all versions corresponded to single commits on the master branch; dedicated branches will be used to release and service minor versions. For example, releasing v0.1.0 would see the creation of a branch named maintenance/0.1.x, used to service all 0.1 versions. As we adhere to [semantic versioning](https://semver.org/), bug-fixes would be applied in this branch, bumping the minor (final) version number each time, e.g. 0.1.1, 0.1.2, etc. No development will occur in these branches; new features are merged into master, and bug-fixes are cherry-picked from master.

You can learn more about this branching model at:

* [releaseflow.org](http://releaseflow.org/)
* [NumPy development workflow](https://numpy.org/doc/stable/dev/development_workflow.html)
* [Release Flow – Azure DevOps](https://docs.microsoft.com/en-us/azure/devops/learn/devops-at-microsoft/release-flow)


### Learning Git

As our former development, installation, and upgrading practices involved Mercurial revision-control, some of you may not be familiar with Git. While you no longer need to use _any_ revision control system to use the _labscript suite_, those of you wanting to contribute to development who aren't acquainted with Git may benefit from these resources:

* NumPy: [Getting started with Git development](https://numpy.org/doc/stable/dev/gitwash/development_setup.html)
* [GitHub Guides](https://guides.github.com/): Very cogent information for beginners. We recommend starting with:
    * [Hello World](https://guides.github.com/activities/hello-world/)
    * [Git Handbook](https://guides.github.com/introduction/git-handbook/)
    	_Note:_ You may notice references to 'GitHub Flow' in these guides (and 'Git Flow' elsewhere). These share some aspects of the Release Flow branching-workflow we use, but are distinct.
* [Atliassian Git Tutorials](https://www.atlassian.com/git/tutorials): Despite the many references to BitBucket (ignore these); there is a wealth of excellent beginner information for using Git at the command line here; and finally
* [Oh Shit, Git!?!](https://ohshitgit.com/) Mistakes happen. This is a good place to start fixing them. ([Censored version](https://dangitgit.com/).)
