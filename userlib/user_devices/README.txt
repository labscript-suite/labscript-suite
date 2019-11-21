This is a location that you can put custom labscript device drivers, following
the same layout as device drivers in the labscript_devices module. To import them,
import from `user_devices` instead of `labscript_devices`.

In this way, you can work on device support separately from the main labscript devices
package. However, if you write support for a generally available device, please do
contribute it back and we will include it in the main labscript_devices module.

If you prefer to store custom device code elsewhere, you may modify the `user_devices`
configuration setting in labconfig to be an import path (ie 'module.submodule' format,
not a filepath) to another Python package.