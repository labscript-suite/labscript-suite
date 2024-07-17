Supported Hardware
==================

The labscript suite supports a range of commercial and open-source hardware,
and is modular by design. Adding support for new devices involves writing Python functions for a well-defined set of primitives to program instructions,
and transition between buffered I/O and manual states.
See the :doc:`documentation <labscript-devices:adding_devices>` for more details on adding new devices.

Below is a list of devices that are directly supported by the *labscript suite* via :doc:`labscript-devices <labscript-devices:index>`.
Hardware on this list do not constitute an endorsement.

- `AlazarTech <https://www.alazartech.com/>`__ PCI Express Digitizers (e.g. `ATS9462 <https://www.alazartech.com/Product/ATS9462>`__)
- `LightCrafter DMD <http://www.ti.com/tool/DLPLCR4500EVM>`__ Digital Micro-mirror Device
- `National Instruments Data Acquisition <http://www.ni.com/data-acquisition/>`__ (`DAQmx <https://knowledge.ni.com/KnowledgeArticleDetails?id=kA00Z000000P8baSAC>`__) devices:
  
  - Can :doc:`auto-generate a labscript device class <labscript-devices:devices/ni_daqs>` for *any* NI-DAQmx device
  - Pre-generated devices include:
    
    -  `cDAQ-9184 <https://www.ni.com/en-us/support/model.cdaq-9184.html>`__ CompactDAQ Chassis
    -  `PCI 6251 <https://www.ni.com/en-au/support/model.pci-6251.html>`__ Multifunction I/O Device
    -  `PCI 6533/6534 <http://www.ni.com/pdf/manuals/371464d.pdf>`__ High-Speed Digital Pattern I/O
    -  `PCI-6713 <https://www.ni.com/en-au/support/model.pci-6713.html>`__ Analog Output Device
    -  `PCI-6733 <https://www.ni.com/en-au/support/model.pci-6733.html>`__ Analog Output Device
    -  PCI-DIO-32HS High-Speed Digital I/O
    -  `PCIe-6363 <https://www.ni.com/en-us/support/model.pcie-6363.html>`__ Multifunction I/O Device
    -  `PCIe-6738 <https://www.ni.com/en-us/support/model.pcie-6738.html>`__ Analog Output Device
    -  `PXI-6733 <https://www.ni.com/en-au/support/model.pxi-6733.html>`__ PXI Analog Output Module
    -  `PXIe-6361 <https://www.ni.com/en-au/support/model.pxie-6361.html>`__ PXI Multifunction I/O Module
    -  `PXIe-6535 <https://www.ni.com/en-ie/support/model.pxie-6535.html>`__ PXI Digital I/O Module
    -  `PXIe-6738 <https://www.ni.com/en-au/support/model.pxie-6738.html>`__ PXI Analog Output Module
    -  `USB-6008 <https://www.ni.com/en-au/support/model.usb-6008.html>`__ Multifunction I/O Device
    -  `USB-6229 <https://www.ni.com/en-my/support/model.usb-6229.html>`__ Multifunction I/O Device
    -  `USB-6343 <https://www.ni.com/en-us/support/model.usb-6343.html>`__ Multifunction I/O Device

- `Quicksyn FSW-0010 <http://ni-microwavecomponents.com/quicksyn-full>`__ Microwave Synthesizer (formerly PhaseMatrix)
-  `NovaTech DDS9m <http://www.novatechsales.com/PDF_files/dds9mds_lr.pdf>`__ 170MHz Four Channel Direct Digital Synthesized Signal Generator
   (see `blog post <https://labscriptsuite.org/blog/tag/novatech-dds9m/>`__)
-  `OpalKelly XEM3001 <https://opalkelly.com/products/xem3001/>`__ FPGA Boards used by the Cicero control system
-  `PineBlaster <https://labscriptsuite.org/hardware/pineblaster/>`__ Open-source Digital Pattern Generator
-  `SpinCore <https://www.spincore.com/products/#pulsegeneration>`__ Programmable Pulse Generators and Direct Digital Synthesis

    -  `PulseBlasterDDS-II-300-AWG <http://www.spincore.com/products/PulseBlasterDDS-II-300/>`__
    -  `PulseBlasterESR-PRO <https://www.spincore.com/products/PulseBlasterESR-PRO/>`__
    -  `PulseBlasterESR-CompactPCI <https://www.spincore.com/products/PulseBlasterESR-CompactPCI/>`__
    -  `PulseBlaster <https://www.spincore.com/products/PulseBlaster/>`__ e.g. SP2 Model: PB24-100-32k
    -  `PulseBlasterUSB <https://www.spincore.com/products/PulseBlasterUSB/>`__

-  `PineBlaster <http://labscriptsuite.org/hardware/pineblaster>`_ Open-source Digital Pattern Generator
-  `PrawnBlaster <https://github.com/labscript-suite/prawnblaster/>`_ Open-source psuedoclock generator based on the $4 Raspberry Pi Pico
-  `Tektronix oscilloscopes <https://www.tek.com/oscilloscope>`__
-  `Zaber <https://www.zaber.com/>`__ Motion Controllers, e.g. linear translation stages
-  `FLIR <https://www.flir.com/>`__ cameras using the free `Spinnaker SDK <https://www.flir.com.au/products/spinnaker-sdk/>`__
-  Andor SDK2 Cameras
-  Basler pypylon cameras
-  Any camera compatible with National Instruments `GigE Vision <https://en.wikipedia.org/wiki/GigE_Vision>`__
   
   - Includes most cameras compliant with the GigE Vision interface standard, such as `Allied Vision <https://www.alliedvision.com/en/products/cameras.html>`__ cameras

The Monash labs where the *labscript suite* was
initially developed have used an `Adnaco PCI/PCIe fiber expansion system <http://www.adnaco.com/products/>`__,
which allows devices to be located close to the
experiment independently from the control PC (which
can reside, for example, in a different room) without
introducing ground loops.

Custom Developed Hardware
=========================

.. toctree::
    :maxdepth: 2
    
    pineblaster
    prawnblaster
    prawndo