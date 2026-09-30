## ARKitCore

> `/System/Library/PrivateFrameworks/ARKitCore.framework/ARKitCore`

```diff

-738.0.7.0.0
-  __TEXT.__text: 0x194ee8
+738.0.11.0.0
+  __TEXT.__text: 0x194fb0
   __TEXT.__auth_stubs: 0x3c80
   __TEXT.__objc_methlist: 0x11124
   __TEXT.__const: 0x2c118

   __TEXT.__cstring: 0x1d931
   __TEXT.__ustring: 0xe6
   __TEXT.__unwind_info: 0x6720
-  __TEXT.__objc_classname: 0x2027
-  __TEXT.__objc_methname: 0x2a46c
+  __TEXT.__objc_classname: 0x2029
+  __TEXT.__objc_methname: 0x2a4a1
   __TEXT.__objc_methtype: 0xa641
   __TEXT.__objc_stubs: 0x1ac80
   __DATA_CONST.__got: 0x1680

   __AUTH_CONST.__auth_got: 0x1e58
   __AUTH_CONST.__const: 0x3cb8
   __AUTH_CONST.__cfstring: 0x104a0
-  __AUTH_CONST.__objc_const: 0x3ceb0
+  __AUTH_CONST.__objc_const: 0x3cef0
   __AUTH_CONST.__objc_intobj: 0x3240
   __AUTH_CONST.__objc_arrayobj: 0x600
   __AUTH_CONST.__objc_doubleobj: 0x380
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH.__objc_data: 0x3660
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x2004
+  __DATA.__objc_ivar: 0x200c
   __DATA.__data: 0x1ca0
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1dd8

   - /usr/lib/libchannel.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/librealtime_safety.dylib
-  UUID: 8F3CFFB5-8F69-336C-9CD9-20F9F17A8A93
-  Functions: 7774
-  Symbols:   30088
-  CStrings:  14431
+  UUID: AFF4117E-CBE1-3963-9470-AF83AF55AB32
+  Functions: 7775
+  Symbols:   30091
+  CStrings:  14432
 
Symbols:
+ _ARMatrix3x3IsIdentity
+ _OBJC_IVAR_$_ARImageSensor._lastIntrinsicsImageResolution
+ _OBJC_IVAR_$_ARImageSensor._lastIntrinsicsMatrix
+ ___block_literal_global.523
- GCC_except_table80
- ___block_literal_global.513
- ___block_literal_global.519
Functions:
~ -[ARImageSensor initWithSettings:captureSession:captureQueue:] : 620 -> 656
~ -[ARImageSensor captureOutput:didFinishProcessingPhoto:error:] : 1040 -> 1008
~ -[ARImageSensor captureOutput:didOutputSampleBuffer:fromConnection:] : 260 -> 316
~ -[ARImageSensor dataOutputSynchronizer:didOutputSynchronizedDataCollection:] : 592 -> 648
~ -[ARVideoFormat defaultColorSpace] : 88 -> 100
+ _ARMatrix3x3IsIdentity
CStrings:
+ "_lastIntrinsicsImageResolution"
+ "_lastIntrinsicsMatrix"
- "\x82"

```
