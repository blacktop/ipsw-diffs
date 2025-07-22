## LocalAuthenticationEmbeddedUI

> `/System/Library/Frameworks/LocalAuthenticationEmbeddedUI.framework/LocalAuthenticationEmbeddedUI`

```diff

-1394.40.33.0.0
-  __TEXT.__text: 0x1c9f8
+1394.62.1.0.0
+  __TEXT.__text: 0x1cd68
   __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x2830
+  __TEXT.__objc_methlist: 0x2848
   __TEXT.__const: 0x240
-  __TEXT.__cstring: 0x1fc0
+  __TEXT.__cstring: 0x2008
   __TEXT.__gcc_except_tab: 0x31c
-  __TEXT.__oslogstring: 0x488
+  __TEXT.__oslogstring: 0x4bd
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__unwind_info: 0xac0
+  __TEXT.__unwind_info: 0xad0
   __TEXT.__objc_classname: 0xaef
-  __TEXT.__objc_methname: 0x6b06
-  __TEXT.__objc_methtype: 0x1d23
+  __TEXT.__objc_methname: 0x6b5a
+  __TEXT.__objc_methtype: 0x1d70
   __TEXT.__objc_stubs: 0x5680
   __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0xe58

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x9290
-  __DATA_CONST.__objc_selrefs: 0x17f0
+  __DATA_CONST.__objc_const: 0x92d0
+  __DATA_CONST.__objc_selrefs: 0x1808
   __DATA_CONST.__objc_arraydata: 0x28
   __AUTH_CONST.__objc_const: 0x1550
-  __AUTH_CONST.__cfstring: 0xf80
-  __AUTH_CONST.__const: 0x300
+  __AUTH_CONST.__cfstring: 0xfe0
+  __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x60

   __DATA.__objc_superrefs: 0x150
   __DATA.__objc_ivar: 0x318
   __DATA.__data: 0xa20
-  __DATA.__bss: 0xc8
+  __DATA.__bss: 0xd8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
+  - /System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 56A004D9-2D57-3771-9B9F-E065870CB28D
-  Functions: 1016
-  Symbols:   4029
-  CStrings:  1811
+  UUID: 03743BF8-7E6A-392D-9637-0B328887C7A2
+  Functions: 1022
+  Symbols:   4033
+  CStrings:  1824
 
Symbols:
+ +[LALocalizedString _localizedStringWithKey:tableSuffix:]
+ +[LALocalizedString ok]
+ +[LALocalizedString passcodeChangeNotAvailable]
+ -[LAPSPasscodeChangeUIAdapter presentAlertWithTitle:message:button:completion:]
+ -[LAPSPasscodeChangeUIPresentationController _setupParentVCIfNeededAnimated:]
+ _LA_LOG_LAPSPasscodePersistenceMCAdapter.log
+ _LA_LOG_LAPSPasscodePersistenceMCAdapter.once
+ ___77-[LAPSPasscodeChangeUIAdapter fetchOldPasscodeViewController:verifyPasscode:]_block_invoke.21
+ ___77-[LAPSPasscodeChangeUIPresentationController _setupParentVCIfNeededAnimated:]_block_invoke
+ ___79-[LAPSPasscodeChangeUIAdapter presentAlertWithTitle:message:button:completion:]_block_invoke
+ ___LA_LOG_LAPSPasscodePersistenceMCAdapter_block_invoke
+ ___block_literal_global.9
+ _objc_msgSend$_setupParentVCIfNeededAnimated:
- -[LAContainerViewController viewDidLoad]
- ___65-[LAPSPasscodeChangeUIPresentationController presentVC:animated:]_block_invoke_2
- ___77-[LAPSPasscodeChangeUIAdapter fetchOldPasscodeViewController:verifyPasscode:]_block_invoke.18
- _objc_msgSend$setPasscodeRecoveryAllowed:
CStrings:
+ "%@-%@"
+ "Ignoring request to set passcodeRecoveryEnabled = %s"
+ "OK"
+ "PASSCODE_CHANGE_NOT_AVAILABLE"
+ "_setupParentVCIfNeededAnimated:"
+ "ok"
+ "passcodeChangeNotAvailable"
+ "presentAlertWithTitle:message:button:completion:"
+ "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?>40"
+ "v48@0:8@16@24@32@?40"
- "setPasscodeRecoveryAllowed:"

```
