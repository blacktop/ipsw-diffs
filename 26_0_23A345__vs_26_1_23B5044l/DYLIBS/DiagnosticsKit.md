## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`

```diff

-72.0.2.0.0
-  __TEXT.__text: 0x1f704
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x2eac
-  __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x1a99
+72.40.4.0.0
+  __TEXT.__text: 0x1eba8
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0x2ed4
+  __TEXT.__const: 0xe0
+  __TEXT.__cstring: 0x1a47
   __TEXT.__oslogstring: 0x17c0
-  __TEXT.__gcc_except_tab: 0xbc4
-  __TEXT.__dlopen_cstrs: 0x173
-  __TEXT.__unwind_info: 0x970
-  __TEXT.__objc_classname: 0x6ca
+  __TEXT.__gcc_except_tab: 0xb14
+  __TEXT.__unwind_info: 0x920
+  __TEXT.__objc_classname: 0x6c9
   __TEXT.__objc_methname: 0x5970
   __TEXT.__objc_methtype: 0x1080
   __TEXT.__objc_stubs: 0x4540
-  __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x700
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x658
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x110
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x328
+  __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0xe20
   __AUTH_CONST.__objc_const: 0x5190

   __AUTH.__objc_data: 0xdc0
   __DATA.__objc_ivar: 0x2d0
   __DATA.__data: 0xe00
-  __DATA.__bss: 0x150
+  __DATA.__bss: 0x108
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9EE91131-226A-35F9-94D0-D409F3600C0E
-  Functions: 940
-  Symbols:   3537
-  CStrings:  1670
+  UUID: 362781CC-0767-3470-8B3E-FA6F2527E2B9
+  Functions: 926
+  Symbols:   3491
+  CStrings:  1661
 
Symbols:
+ -[DKDiagnosticContext remoteHostHideStatusBar]
+ -[DKDiagnosticContext remoteHostSetStatusBarStyle:]
+ -[DKDiagnosticContext remoteHostShowStatusBar]
+ _OBJC_CLASS_$_CBSUtilities
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSTarget
+ ___39-[DKExtensionRequest beginWithPayload:]_block_invoke.97
+ ___39-[DKExtensionRequest connectWithError:]_block_invoke.17
+ ___55-[DKDiagnosticViewController displayPressHomeLabelFor:]_block_invoke.61
- GCC_except_table73
- _CheckerBoardServicesLibraryCore
- _CheckerBoardServicesLibraryCore.frameworkLibrary
- _RunningBoardServicesLibrary
- _RunningBoardServicesLibraryCore
- _RunningBoardServicesLibraryCore.frameworkLibrary
- _UIKitLibraryCore.frameworkLibrary
- ___39-[DKExtensionRequest beginWithPayload:]_block_invoke.93
- ___39-[DKExtensionRequest connectWithError:]_block_invoke.16
- ___55-[DKDiagnosticViewController displayPressHomeLabelFor:]_block_invoke.60
- ___CheckerBoardServicesLibraryCore_block_invoke
- ___RunningBoardServicesLibraryCore_block_invoke
- ___UIKitLibraryCore_block_invoke
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___getCBSUtilitiesClass_block_invoke
- ___getCBSUtilitiesClass_block_invoke.cold.1
- ___getRBSAssertionClass_block_invoke
- ___getRBSAssertionClass_block_invoke.cold.1
- ___getRBSDomainAttributeClass_block_invoke
- ___getRBSDomainAttributeClass_block_invoke.cold.1
- ___getRBSTargetClass_block_invoke
- ___getRBSTargetClass_block_invoke.cold.1
- __sl_dlopen
- _abort_report_np
- _audit_stringCheckerBoardServices
- _audit_stringRunningBoardServices
- _audit_stringUIKit
- _free
- _getCBSUtilitiesClass.softClass
- _getRBSAssertionClass.softClass
- _getRBSDomainAttributeClass.softClass
- _getRBSTargetClass.softClass
- _objc_getClass
CStrings:
- "CBSUtilities"
- "RBSAssertion"
- "RBSDomainAttribute"
- "RBSTarget"
- "Unable to find class %s"
- "softlink:o:path:/System/Library/Frameworks/UIKit.framework/UIKit"
- "softlink:o:path:/System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices"
- "softlink:o:path:/System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices"

```
