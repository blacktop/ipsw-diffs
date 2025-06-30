## Passbook

> `/private/var/staged_system_apps/Passbook.app/Passbook`

```diff

-0.0.0.0.0
-  __TEXT.__text: 0xc044
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_stubs: 0x2400
+1552.5.17.0.0
+  __TEXT.__text: 0xc4d0
+  __TEXT.__auth_stubs: 0x5b0
+  __TEXT.__objc_stubs: 0x24a0
   __TEXT.__objc_methlist: 0x278
   __TEXT.__const: 0x50
   __TEXT.__gcc_except_tab: 0x34
-  __TEXT.__objc_methname: 0x352a
-  __TEXT.__cstring: 0x59a
-  __TEXT.__oslogstring: 0x46c
+  __TEXT.__objc_methname: 0x367b
+  __TEXT.__cstring: 0x611
+  __TEXT.__oslogstring: 0x4ec
   __TEXT.__objc_classname: 0xf3
-  __TEXT.__objc_methtype: 0xb08
-  __TEXT.__unwind_info: 0x1f4
-  __DATA_CONST.__auth_got: 0x2b8
-  __DATA_CONST.__got: 0x5f8
-  __DATA_CONST.__const: 0x570
+  __TEXT.__objc_methtype: 0xb17
+  __TEXT.__unwind_info: 0x204
+  __DATA_CONST.__auth_got: 0x2e8
+  __DATA_CONST.__got: 0x600
+  __DATA_CONST.__const: 0x5b0
   __DATA_CONST.__cfstring: 0x360
   __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1058
-  __DATA.__objc_selrefs: 0xa00
-  __DATA.__objc_classrefs: 0x1e0
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x50
+  __DATA_CONST.__objc_classrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x10
+  __DATA.__objc_const: 0x1078
+  __DATA.__objc_selrefs: 0xa28
+  __DATA.__objc_ivar: 0x54
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x240
+  __DATA.__data: 0x248
+  __DATA.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
+  - /System/Library/PrivateFrameworks/PassKitCore_SoftLinking.framework/PassKitCore_SoftLinking
   - /System/Library/PrivateFrameworks/PassKitUI.framework/PassKitUI
   - /System/Library/PrivateFrameworks/PassKitUIFoundation.framework/PassKitUIFoundation
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences

   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BD7EB81F-8344-326E-9E69-2025DCF19166
-  Functions: 120
-  Symbols:   345
-  CStrings:  616
+  UUID: F2A4FF56-BE52-30F7-BBC5-4FE0EA4102F3
+  Functions: 125
+  Symbols:   351
+  CStrings:  627
 
Symbols:
+ _PKGetClassNFHardwareManager
+ _PKURLActionRouteSavingsAddBeneficiary
+ _PKURLActionRouteSavingsBankVerification
+ __os_log_debug_impl
+ _dispatch_once
+ _dlopen
+ _objc_getClass
- _OBJC_CLASS_$_PKBankConnectTransactionsProvider
CStrings:
+ "\x02\x16\x11\x13"
+ "/System/Library/Frameworks/FinanceKit.framework/FinanceKit"
+ "@\"NFAssertion\""
+ "FKBankConnectSpotlightTransactionsProvider"
+ "Failed to retrieve a response with transaction for url %@"
+ "PBKAppDelegate (%p): acquired foreground nearfield informative assertion %p."
+ "PBKAppDelegate (%p): failed to acquire foreground nearfield informative assertion - %@."
+ "T@\"NSString\",?,R,C"
+ "T@\"UIWindow\",?,&,N"
+ "_informativeForegroundAssertion"
+ "presentAccountFeature:animated:destination:fundingSourceIdentifier:completion:"
+ "primaryAccountIdentifier"
+ "releaseAssertion:"
+ "requestAssertion:error:"
+ "sharedHardwareManagerWithNoUI"
+ "transaction"
+ "v16@?0@\"FKBankConnectSpotlightTransactionsProviderResponse\"8"
- "\x02\x15\x11\x13"
- "Failed to retrieve pass for transaction with url %@"
- "Failed to retrieve transaction with url %@"
- "T@\"UIWindow\",&,N"
- "presentAccountFeature:animated:destination:completion:"
- "v24@?0@\"PKPaymentTransaction\"8@\"NSString\"16"

```
