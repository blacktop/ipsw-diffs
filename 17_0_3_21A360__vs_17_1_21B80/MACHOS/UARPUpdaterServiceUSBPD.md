## UARPUpdaterServiceUSBPD

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/UARPUpdaterServiceUSBPD`

```diff

-916.0.46.0.0
-  __TEXT.__text: 0x2201c
-  __TEXT.__auth_stubs: 0x790
-  __TEXT.__objc_stubs: 0x3480
-  __TEXT.__objc_methlist: 0x12c0
-  __TEXT.__oslogstring: 0x23f9
-  __TEXT.__cstring: 0x24b8
-  __TEXT.__objc_classname: 0x202
-  __TEXT.__objc_methname: 0x4281
+916.40.22.0.2
+  __TEXT.__text: 0x2285c
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_stubs: 0x3540
+  __TEXT.__objc_methlist: 0x12f0
+  __TEXT.__oslogstring: 0x25ba
+  __TEXT.__cstring: 0x25cc
+  __TEXT.__objc_classname: 0x203
+  __TEXT.__objc_methname: 0x4365
   __TEXT.__objc_methtype: 0x3029
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x6fc
-  __DATA_CONST.__auth_got: 0x3d8
+  __TEXT.__unwind_info: 0x710
+  __DATA_CONST.__auth_got: 0x3e8
   __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x538
-  __DATA_CONST.__cfstring: 0x6c0
+  __DATA_CONST.__const: 0x588
+  __DATA_CONST.__cfstring: 0x700
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x3f40
-  __DATA.__objc_selrefs: 0xeb8
+  __DATA.__objc_const: 0x3f90
+  __DATA.__objc_selrefs: 0xee8
   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x150
   __DATA.__objc_superrefs: 0x58
-  __DATA.__objc_ivar: 0x21c
+  __DATA.__objc_ivar: 0x224
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x383
   __DATA.__bss: 0x38c

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1082
-  Symbols:   536
-  CStrings:  1443
+  Functions: 1099
+  Symbols:   540
+  CStrings:  1468
 
Symbols:
+ _IOPMAssertionCreateWithName
+ _IOPMAssertionRelease
+ _createPowerAssertion
+ _releasePowerAssertion
CStrings:
+ "\b\x11\x11"
+ "%s: Already released power assertion for USBPD"
+ "%s: Failed to create power assertion %@ with error %d"
+ "%s: Failed to create power assertion for %@"
+ "%s: Failed to release power assertion for USBPD"
+ "%s: Failed to release power assertion with error %d"
+ "%s: Invalid powerAssertionID received from caller"
+ "%s: Power assertion held for %@"
+ "%s: Power assertion released for USBPD"
+ "%s: usbpd = %@, requires power assertion"
+ "-[UARPUSBPDUpdater holdPowerAssertionForAccessory]"
+ "-[UARPUSBPDUpdater releasePowerAssertionForAccessory]"
+ "Already holding power assertion for USBPD"
+ "BOOL createPowerAssertion(NSString *__strong, IOPMAssertionID *)"
+ "BOOL releasePowerAssertion(IOPMAssertionID)"
+ "PreventUserIdleSystemSleep"
+ "TB,V_requiresPowerAssertion"
+ "_powerAssertionID"
+ "_requiresPowerAssertion"
+ "com.apple.UARPPowerAssertion-USBPD"
+ "dataWithData:"
+ "holdPowerAssertionForAccessory"
+ "releasePowerAssertionForAccessory"
+ "requiresPowerAssertion"
+ "setRequiresPowerAssertion:"
+ "updateRequiresPowerAssertion"
- "\b\x12"

```
