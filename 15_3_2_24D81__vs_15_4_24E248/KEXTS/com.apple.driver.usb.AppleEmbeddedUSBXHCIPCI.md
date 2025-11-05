## com.apple.driver.usb.AppleEmbeddedUSBXHCIPCI

> `com.apple.driver.usb.AppleEmbeddedUSBXHCIPCI`

```diff

-647.60.6.0.0
+651.100.4.0.0
   __TEXT.__cstring: 0x1234
   __TEXT.__os_log: 0xa9d
   __TEXT.__const: 0x8
-  __TEXT_EXEC.__text: 0x9a44
+  __TEXT_EXEC.__text: 0x9a00
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x88

   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__mod_init_func: 0x18
   __DATA_CONST.__mod_term_func: 0x18
-  __DATA_CONST.__const: 0x2768
+  __DATA_CONST.__const: 0x2750
   __DATA_CONST.__kalloc_type: 0xc0
-  UUID: 9C025D11-2F0C-30B9-A312-9830ED79881D
+  UUID: FA8E4FA7-2AD6-3560-B8AD-623080F7F1C6
   Functions: 121
   Symbols:   729
   CStrings:  156
Functions:
~ __ZN30AppleEmbeddedUSBXHCIFL1100Init5probeEP9IOServicePi : 3220 -> 3232
~ __ZN26AppleEmbeddedUSBXHCIFL11005startEP9IOService : 1932 -> 1920
~ __ZN26AppleEmbeddedUSBXHCIFL11004freeEv : 120 -> 124
~ __ZN26AppleEmbeddedUSBXHCIFL110015registerServiceEj : 368 -> 376
~ __ZN26AppleEmbeddedUSBXHCIFL110010createPortEPN15StandardUSBXHCI33StandardUSBXHCIProtocolCapabilityEjj : 3048 -> 3044
~ __ZN26AppleEmbeddedUSBXHCIFL110020raiseOnePowerStateToEm : 828 -> 824
~ __ZN26AppleEmbeddedUSBXHCIFL110016getCompanionPortEP16AppleUSBHostPortj : 2812 -> 2800
~ __ZN26AppleEmbeddedUSBXHCIFL110027getCompanionControllerGatedEjhRP22AppleUSBHostController : 2104 -> 2136
~ ____ZN26AppleEmbeddedUSBXHCIFL110013powerOnFL1100Ev_block_invoke : 2548 -> 2532
~ ____ZN26AppleEmbeddedUSBXHCIFL110014powerOffFL1100Ev_block_invoke : 2544 -> 2528
~ __ZN31AppleEmbeddedUSBXHCIASMedia31425startEP9IOService : 2208 -> 2196
~ __ZN31AppleEmbeddedUSBXHCIASMedia31424freeEv : 120 -> 124
~ __ZN31AppleEmbeddedUSBXHCIASMedia314220raiseOnePowerStateToEm : 1232 -> 1240
~ __ZN31AppleEmbeddedUSBXHCIASMedia314222powerStateWillChangeToEmmP9IOService : 612 -> 608
~ __ZN31AppleEmbeddedUSBXHCIASMedia314221powerStateDidChangeToEmmP9IOService : 580 -> 576
~ __ZN31AppleEmbeddedUSBXHCIASMedia314214enablePCIePortEb : 1828 -> 1808
~ __ZN31AppleEmbeddedUSBXHCIASMedia314215powerPCIeDeviceEb : 1560 -> 1544
~ __ZN31AppleEmbeddedUSBXHCIASMedia314224pciWakeInterruptOccurredEP22IOInterruptEventSourcei : 856 -> 860
~ __ZN31AppleEmbeddedUSBXHCIASMedia31425resetEv : 664 -> 660
~ __ZN31AppleEmbeddedUSBXHCIASMedia314220applyASMediaTunablesEP6OSData : 1920 -> 1904

```
