## com.apple.driver.AppleUSBXDCIARM

> `com.apple.driver.AppleUSBXDCIARM`

```diff

-847.0.5.0.0
+847.40.2.0.0
   __TEXT.__const: 0x38
-  __TEXT.__cstring: 0x3bca
-  __TEXT.__os_log: 0x638f
-  __TEXT_EXEC.__text: 0x39df4
+  __TEXT.__cstring: 0x3bff
+  __TEXT.__os_log: 0x63dd
+  __TEXT_EXEC.__text: 0x39ffc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x1c8

   __DATA_CONST.__mod_term_func: 0x50
   __DATA_CONST.__const: 0x6130
   __DATA_CONST.__kalloc_type: 0x280
-  UUID: C70AD62A-380E-36FD-9FDF-9C6DE5827C2C
-  Functions: 345
+  UUID: 3C2DAF3E-1E4A-35D0-901B-A855DEC9E207
+  Functions: 346
   Symbols:   0
-  CStrings:  325
+  CStrings:  327
 
Functions:
~ __ZN15AppleUSBXDCIARM5startEP9IOService : 8296 -> 8336
~ __ZN15AppleUSBXDCIARM19cableChangeOccurredEP18IOTimerEventSource : 1920 -> 1936
~ __ZN15AppleUSBXDCIARM17hardwareExceptionEiPKc : 1028 -> 1448
CStrings:
+ "%s@%s: %s::%s: cable detect disabled: _cableConnected usb2 %d usb3 %d\n"
+ "%s@%s: %s::%s: force-usb2-device set in boot-args, forcing usb2 device mode\n"
+ "%s@%s: %s::%s: kXDCIExceptionPowerOnErr (%s). Reinitializing the device controller.\n"
+ "force-usb2-device"
- "%s@%s: %s::%s: AppleEmbeddedUSBArbitrator-force-usbdevice set in boot-args, forcing device mode\n"
- "%s@%s: %s::%s: cable detect disabled: _cableConnected %d\n"
- "AppleEmbeddedUSBArbitrator-force-usbdevice"

```
