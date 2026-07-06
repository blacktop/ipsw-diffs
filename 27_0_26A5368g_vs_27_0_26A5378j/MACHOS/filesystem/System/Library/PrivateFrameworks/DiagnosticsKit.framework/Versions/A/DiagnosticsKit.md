## DiagnosticsKit

> `/System/Library/PrivateFrameworks/DiagnosticsKit.framework/Versions/A/DiagnosticsKit`

```diff

-  __TEXT.__text: 0x20230
+  __TEXT.__text: 0x2038c
   __TEXT.__objc_methlist: 0x2b0c
   __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x1b6b
+  __TEXT.__cstring: 0x1ba4
   __TEXT.__gcc_except_tab: 0x970
-  __TEXT.__oslogstring: 0x1aef
+  __TEXT.__oslogstring: 0x1b2b
   __TEXT.__unwind_info: 0x990
   __TEXT.__objc_stubs: 0x3c40
-  __TEXT.__auth_stubs: 0x500
+  __TEXT.__auth_stubs: 0x520
   __TEXT.__objc_classname: 0x605
-  __TEXT.__objc_methname: 0x51f7
-  __TEXT.__objc_methtype: 0xf76
-  __DATA_CONST.__const: 0x228
+  __TEXT.__objc_methname: 0x520d
+  __TEXT.__objc_methtype: 0xf84
+  __DATA_CONST.__const: 0x230
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x108

   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__got: 0x268
   __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0xde0
+  __AUTH_CONST.__cfstring: 0xe00
   __AUTH_CONST.__objc_const: 0x4a18
   __AUTH_CONST.__objc_intobj: 0xd8
-  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH.__objc_data: 0xd20
   __DATA.__objc_ivar: 0x274
   __DATA.__data: 0xc70
   __DATA.__bss: 0x108
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 920
-  Symbols:   2413
-  CStrings:  1567
+  Symbols:   2415
+  CStrings:  1571
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[DKExtensionRequest _entitlementCheckResultForExtensionContext:entitlement:]
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateWithAuditToken
+ _objc_msgSend$_entitlementCheckResultForExtensionContext:entitlement:
- -[DKExtensionRequest _extensionContext:hasEntitlement:]
- _objc_msgSend$_extensionContext:hasEntitlement:
Functions:
~ -[DKExtensionRequest beginWithPayload:] : 1112 -> 1140
~ -[DKExtensionRequest _extensionContext:hasEntitlement:] -> -[DKExtensionRequest _entitlementCheckResultForExtensionContext:entitlement:] : 124 -> 420
~ -[DKExtensionRequest beginWithPayload:].cold.1 : 112 -> 136
CStrings:
+ "Unable to verify the diagnostic extension's entitlement."
+ "[RID: %@] Cannot start extension (error %ld)."
+ "[RID: %@] Unable to read extension entitlement '%{public}@': %{public}@"
+ "_entitlementCheckResultForExtensionContext:entitlement:"
+ "q32@0:8@16@24"
- "[RID: %@] Cannot start extension. Entitlement is missing."
- "_extensionContext:hasEntitlement:"

```
