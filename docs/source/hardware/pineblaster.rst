Pineblaster
===========

.. note::

    The Pineblaster is generally deprecated in favor of the :doc:`Prawnblaster <prawnblaster>`/:doc:`PrawnDO <prawndo>`,
    which is cheaper and has higher resolution and more instructions.

The PineBlaster is a microcontroller-based pseudoclock,
built on the `Digilent chipKIT Max32™ Prototyping Platform <http://www.digilentinc.com/Products/Detail.cfm?Prod=CHIPKIT-MAX32>`__.

The source code for the PineBlaster is available from our `github repository <https://github.com/labscript-suite/pineblaster>`__.
We currently have several versions of code,
depending on which version of MPIDE you use to compile and flash the ChipKIT MAX32 board.
The version in the default branch currently only compiles with `MPIDE v0023-20120903 <https://chipkit.s3.amazonaws.com/builds/mpide-0023-windows-20120903.zip>`__.
There is a version in the `MPIDE_v0150-20150820 <https://bitbucket.org/labscript_suite/pineblaster/src/tip/?at=MPIDE_v0150-20150820>`__ branch of the repository which works with the latest version of MPIDE
(of the same name as the branch).
However, this version has a lower instruction limit of 7450 (compared to 15000 on the earlier version)
and a slower 4us response time to triggers (compared to 1us on the earlier version).
These changes have not been incorporated into the labscript class yet,
and so will need to be done manually on your local install if you use the new version
(contact us on the mailing list if you run into trouble with this).

**As such, we recommend using the version in the default branch compiled and flashed with MPIDE v0023-20120903.**
