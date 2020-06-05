## BitBucket archive

In April–May 2020 the _labscript suite_ code base was migrated from BitBucket to GitHub. All commit history and issues was preserved, however some repository metadata (such as pull request discussions) could not be migrated directly. As such, we have created an archived copy of everything that was on BitBucket. This includes:

* Issues (as they appear on BitBucket);
* Pull requests discussions;
* Commit comments for every labscript suite repository; and
* Every public fork (as of 1st February, 2020).

This archive can be found at [bitbucket-archive.labscriptsuite.org](https://bitbucket-archive.labscriptsuite.org/) (this page can take some time to load for the first time). Copies of every public fork of our repositories are at [github.com/labscript-suite-bitbucket-archive](https://github.com/labscript-suite-bitbucket-archive). As this is an archive, we will not be transferring ownership of these repositories back to their original owners. However, should you wish to continue development on one of those repositories you can fork it into your own account through the GitHub web interface. Should you have uncommitted changes (or changes made after 1st February, 2020) that you wish to have archived, please contact us to discuss the best approach to including these. Please note that we are not recommending continuing development in such forks long term, due to the changes in package structure outlined above.


### What to do if you had custom code in a fork on BitBucket

labscript experiment scripts and lyse analysis scripts can be copied or moved to the new labscriptlib/analysislib folders. We deem these user-side code as they are not within the codebase of the labcript suite programs, and thus do not require a [developer (editable) installation](../installation).

Customisations of the labscript suite will need to be reintegrated into the new package structure, using a developer installation. For example, to include your own custom labscript devices, you should undertake the developer installation procedure for the [labscript-devices](https://github.com/labscript-suite/labscript-devices) repository, and copy your custom or modified device files into the labscript_devices folder alongside the existing device files. Please also consider contributing these back to the main project by pushing them to your fork and [issuing a pull request](../contributing/#pull-requests).

The procedure for migrating customisations of other components will depend on how up-to-date your fork is. Please open a thread on the [mailing list](http://groups.google.com/group/labscriptsuite) to discuss with us how to migrate your custom features and/or how to contribute them back to the base _labscript suite_ repositories.


### Migrating other repositories to GitHub

Should you have other repositories on BitBucket such as labscriptlib, analysislib, userlib, or labconfig (or any project unrelated to the _labscript suite_) we strongly suggest using the tools we developed to migrate the _labscript suite_ to GitHub. These are [philipstarkey/bitbucket-hg-exporter](https://github.com/philipstarkey/bitbucket-hg-exporter) and [chrisjbillington/hg-export-tool](https://github.com/chrisjbillington/hg-export-tool) which can be used together. See the documentation of those projects for further details.
