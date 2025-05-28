## DigitalSeparationUI

> `/System/Library/PrivateFrameworks/DigitalSeparationUI.framework/DigitalSeparationUI`

```diff

-345.0.2.0.0
-  __TEXT.__text: 0x2ba5c
+345.0.15.0.0
+  __TEXT.__text: 0x2baa4
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x29f8
+  __TEXT.__objc_methlist: 0x2a10
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x2ace
   __TEXT.__oslogstring: 0x123b
   __TEXT.__gcc_except_tab: 0x38c
   __TEXT.__dlopen_cstrs: 0x104
-  __TEXT.__unwind_info: 0xb24
+  __TEXT.__unwind_info: 0xb2c
   __TEXT.__objc_classname: 0x6a9
-  __TEXT.__objc_methname: 0xa065
+  __TEXT.__objc_methname: 0xa0a7
   __TEXT.__objc_methtype: 0x1fdf
-  __TEXT.__objc_stubs: 0x74e0
+  __TEXT.__objc_stubs: 0x7500
   __DATA_CONST.__got: 0x198
   __DATA_CONST.__const: 0xad0
   __DATA_CONST.__objc_classlist: 0x120

   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xc578
-  __DATA_CONST.__objc_selrefs: 0x21e0
+  __DATA_CONST.__objc_selrefs: 0x21f0
   __DATA_CONST.__objc_arraydata: 0x90
   __AUTH_CONST.__objc_const: 0xfd8
   __AUTH_CONST.__cfstring: 0x3440

   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
+  - /System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI
   - /System/Library/Frameworks/SafariServices.framework/SafariServices
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration

   - /System/Library/PrivateFrameworks/AppleAccountUI.framework/AppleAccountUI
   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/ContactsUICore.framework/ContactsUICore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1106
-  Symbols:   4428
-  CStrings:  2420
+  Functions: 1108
+  Symbols:   4433
+  CStrings:  2422
 
Symbols:
+ +[DSSafetyCheck startWithPresentingViewController:withURL:]
+ -[DSPasscodeController passcodeChangePressed]
+ ___46-[DSNavigationController willEnterForeground:]_block_invoke.433
+ ___46-[DSNavigationController willEnterForeground:]_block_invoke.433.cold.1
+ ___46-[DSNavigationController willEnterForeground:]_block_invoke.434
+ ___block_literal_global.436
+ _objc_msgSend$displayPasscodeChangeSheet
- ___46-[DSNavigationController willEnterForeground:]_block_invoke.431
- ___46-[DSNavigationController willEnterForeground:]_block_invoke.431.cold.1
- ___46-[DSNavigationController willEnterForeground:]_block_invoke.432
- ___block_literal_global.434
CStrings:
+ "passcodeChangePressed"
+ "startWithPresentingViewController:withURL:"

```
