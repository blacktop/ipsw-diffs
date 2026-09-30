## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit`

```diff

-  __TEXT.__text: 0x20c4c
+  __TEXT.__text: 0x20da0
   __TEXT.__objc_methlist: 0x304c
   __TEXT.__const: 0xf8
-  __TEXT.__cstring: 0x1cd9
-  __TEXT.__oslogstring: 0x1bce
+  __TEXT.__cstring: 0x1d12
+  __TEXT.__oslogstring: 0x1c0a
   __TEXT.__gcc_except_tab: 0xa30
   __TEXT.__unwind_info: 0xa60
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x818
+  __DATA_CONST.__const: 0x820
   __DATA_CONST.__objc_classlist: 0x160
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x128

   __DATA_CONST.__objc_arraydata: 0x60
   __DATA_CONST.__got: 0x2f0
   __AUTH_CONST.__const: 0x420
-  __AUTH_CONST.__cfstring: 0xf20
+  __AUTH_CONST.__cfstring: 0xf40
   __AUTH_CONST.__objc_const: 0x5290
   __AUTH_CONST.__objc_intobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x30

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/CheckerBoardServices.framework/CheckerBoardServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 976
-  Symbols:   3655
-  CStrings:  473
+  Symbols:   3658
+  CStrings:  476
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[DKExtensionRequest _entitlementCheckResultForExtensionContext:entitlement:]
+ _CFRelease
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _objc_msgSend$_entitlementCheckResultForExtensionContext:entitlement:
- -[DKExtensionRequest _extensionContext:hasEntitlement:]
- _objc_msgSend$_extensionContext:hasEntitlement:
Functions:
~ -[DKExtensionRequest beginWithPayload:] : 1024 -> 1052
~ -[DKExtensionRequest _extensionContext:hasEntitlement:] -> -[DKExtensionRequest _entitlementCheckResultForExtensionContext:entitlement:] : 108 -> 396
~ -[DKExtensionRequest beginWithPayload:].cold.1 : 108 -> 132
CStrings:
+ "Unable to verify the diagnostic extension's entitlement."
+ "[RID: %@] Cannot start extension (error %ld)."
+ "[RID: %@] Unable to read extension entitlement '%{public}@': %{public}@"
- "[RID: %@] Cannot start extension. Entitlement is missing."

```
