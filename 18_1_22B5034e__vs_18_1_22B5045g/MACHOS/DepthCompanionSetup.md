## DepthCompanionSetup

> `/System/Library/NanoPreferenceBundles/SetupBundles/DepthCompanionSetup.bundle/DepthCompanionSetup`

```diff

-248.0.0.0.0
-  __TEXT.__text: 0x11e8
-  __TEXT.__auth_stubs: 0x1a0
-  __TEXT.__objc_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x1f0
-  __TEXT.__cstring: 0x213
-  __TEXT.__objc_methname: 0x9f6
+248.2.0.0.0
+  __TEXT.__text: 0x15a8
+  __TEXT.__auth_stubs: 0x220
+  __TEXT.__objc_stubs: 0x820
+  __TEXT.__objc_methlist: 0x1f8
+  __TEXT.__cstring: 0x251
+  __TEXT.__objc_methname: 0xa22
   __TEXT.__objc_classname: 0xab
   __TEXT.__objc_methtype: 0x2f5
-  __TEXT.__const: 0x8
-  __TEXT.__unwind_info: 0xd0
-  __DATA_CONST.__auth_got: 0xd8
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x68
-  __DATA_CONST.__cfstring: 0x300
+  __TEXT.__const: 0x10
+  __TEXT.__oslogstring: 0x155
+  __TEXT.__unwind_info: 0xe0
+  __DATA_CONST.__auth_got: 0x118
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0xa8
+  __DATA_CONST.__cfstring: 0x340
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA.__objc_const: 0x938
-  __DATA.__objc_selrefs: 0x298
+  __DATA.__objc_selrefs: 0x2b0
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x180
+  __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 40
-  Symbols:   63
-  CStrings:  191
+  Functions: 44
+  Symbols:   73
+  CStrings:  203
 
Symbols:
+ _os_log_create
+ _dispatch_once
+ _os_log_type_enabled
+ ___stack_chk_guard
+ __os_log_error_impl
+ _objc_release_x1
+ __os_log_impl
+ _NRDevicePropertyAbsoluteDepthLimit
+ _objc_release_x25
+ ___stack_chk_fail
CStrings:
+ "intValue"
+ "Localizable-Sundrift"
+ "DepthFirstSetupController: Scuba device, presenting safety setup controller"
+ "DepthSetupFirstController: detailString: Shallow use device"
+ "v8@?0"
+ "DepthSetupFirstController: Depth limit of current device is %!@(MISSING)"
+ "DepthSetupFirstController: Unable to retrieve the current device"
+ "DepthFirstSetupController: Hiding scuba safety screen for shallow use device"
+ "deviceDepthLimit"
+ "valueForProperty:"
+ "setup"
+ "CHARON_MAX_DEPTH_SUNDRIFT_%!@(MISSING)"

```
