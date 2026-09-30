## AppStoreUI

> `/System/Library/PrivateFrameworks/AppStoreUI.framework/Versions/A/AppStoreUI`

```diff

-715.0.13.0.0
-  __TEXT.__text: 0xba18
-  __TEXT.__auth_stubs: 0x2d0
+715.0.14.0.0
+  __TEXT.__text: 0xbbd4
+  __TEXT.__auth_stubs: 0x2f0
   __TEXT.__objc_methlist: 0xb50
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x4e1
-  __TEXT.__gcc_except_tab: 0x1ec
+  __TEXT.__cstring: 0x52a
+  __TEXT.__gcc_except_tab: 0x1f8
   __TEXT.__oslogstring: 0x274
   __TEXT.__unwind_info: 0x3b8
   __TEXT.__objc_classname: 0x1cb
-  __TEXT.__objc_methname: 0x2871
+  __TEXT.__objc_methname: 0x2926
   __TEXT.__objc_methtype: 0x6dc
-  __TEXT.__objc_stubs: 0x2600
-  __DATA_CONST.__got: 0x1c8
+  __TEXT.__objc_stubs: 0x2680
+  __DATA_CONST.__got: 0x1e0
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb20
+  __DATA_CONST.__objc_selrefs: 0xb40
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x30
-  __AUTH_CONST.__auth_got: 0x178
-  __AUTH_CONST.__const: 0x370
-  __AUTH_CONST.__cfstring: 0x7e0
+  __AUTH_CONST.__auth_got: 0x188
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0x2078
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/Versions/A/QuartzCore
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/Versions/A/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices
+  - /System/Library/PrivateFrameworks/AppleMediaServicesUI.framework/Versions/A/AppleMediaServicesUI
   - /System/Library/PrivateFrameworks/CommerceKit.framework/Versions/A/CommerceKit
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/Versions/A/OnBoardingKit
   - /System/Library/PrivateFrameworks/StoreFoundation.framework/Versions/A/StoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 287
-  Symbols:   966
-  CStrings:  75
+  Symbols:   977
+  CStrings:  78
 
Symbols:
+ -[ASWriteReviewWindowController showReviewComposerInWindow:]
+ GCC_except_table12
+ _NSLog
+ _OBJC_CLASS_$_AMSBag
+ _OBJC_CLASS_$_AMSProcessInfo
+ _OBJC_CLASS_$_AMSUIReviewContext
+ _OBJC_CLASS_$_AMSUIReviewCoordinator
+ ___60-[ASWriteReviewWindowController showReviewComposerInWindow:]_block_invoke
+ ___block_descriptor_48_e8_32s40w_e20_v24?0Q8"NSError"16l
+ _objc_msgSend$activateIgnoringOtherApps:
+ _objc_msgSend$bagForProfile:profileVersion:
+ _objc_msgSend$currentProcess
+ _objc_msgSend$initWithAccentColor:mediaTaskType:clientInfo:itemIdentifier:
+ _objc_msgSend$presentReviewComposerWithWindow:context:bag:completion:
+ _objc_msgSend$showReviewComposerInWindow:
+ _objc_opt_new
- -[ASWriteReviewWindowController createReviewViewController]
- GCC_except_table10
- ___59-[ASWriteReviewWindowController createReviewViewController]_block_invoke
- _objc_msgSend$activate
- _objc_msgSend$createReviewViewController
CStrings:
+ "1"
+ "StoreKit"
+ "[%!@(MISSING)] Review of app '%!@(MISSING)' completed with result: %!l(MISSING)u. Error: %!@(MISSING)"

```
