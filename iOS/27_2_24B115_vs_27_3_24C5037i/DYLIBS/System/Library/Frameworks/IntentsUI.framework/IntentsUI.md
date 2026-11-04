## IntentsUI

> `/System/Library/Frameworks/IntentsUI.framework/IntentsUI`

```diff

-4016.1.16.0.0
-  __TEXT.__text: 0xf38c
-  __TEXT.__objc_methlist: 0x16ac
+4016.2.7.0.0
+  __TEXT.__text: 0xfd24
+  __TEXT.__objc_methlist: 0x16bc
   __TEXT.__const: 0x120
   __TEXT.__dlopen_cstrs: 0xc2
-  __TEXT.__gcc_except_tab: 0x1ec
-  __TEXT.__cstring: 0x16cc
-  __TEXT.__oslogstring: 0xa33
+  __TEXT.__gcc_except_tab: 0x268
+  __TEXT.__cstring: 0x17bf
+  __TEXT.__oslogstring: 0xb29
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0x600
+  __TEXT.__unwind_info: 0x630
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6e0
+  __DATA_CONST.__const: 0x730
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1268
+  __DATA_CONST.__objc_selrefs: 0x12b0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x88
-  __DATA_CONST.__got: 0x3c8
+  __DATA_CONST.__got: 0x3f0
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xc20
+  __AUTH_CONST.__cfstring: 0xc60
   __AUTH_CONST.__objc_const: 0x26d0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x0

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
+  - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 409
-  Symbols:   1109
-  CStrings:  201
+  Functions: 416
+  Symbols:   1126
+  CStrings:  208
 
Symbols:
+ -[INUIAppIntentForwardingActionExecutor _executeForwardingAction:verifiedPeerAuditToken:completionHandler:]
+ GCC_except_table244
+ GCC_except_table255
+ GCC_except_table275
+ GCC_except_table288
+ GCC_except_table385
+ GCC_except_table52
+ GCC_except_table58
+ _INIntentDeliveryEntitlement
+ _INIntentDeliveryGetMode
+ _INIntentDeliveryProcessDescription
+ _INIntentDeliveryRequestInActionInfo
+ _OBJC_CLASS_$_BSMutableSettings
+ _OBJC_CLASS_$_INIntentDeliveryListener
+ _OBJC_CLASS_$_INIntentForwardingActionResponse
+ ___107-[INUIAppIntentForwardingActionExecutor _executeForwardingAction:verifiedPeerAuditToken:completionHandler:]_block_invoke
+ ___107-[INUIAppIntentForwardingActionExecutor _executeForwardingAction:verifiedPeerAuditToken:completionHandler:]_block_invoke_2
+ ___107-[INUIAppIntentForwardingActionExecutor _executeForwardingAction:verifiedPeerAuditToken:completionHandler:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e88_v56?0"INIntentForwardingAction"8{?=[8I]}16?<v?"INIntentForwardingActionResponse">48ls32l8
+ ___block_descriptor_88_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ _getWFOnScreenContentExtractorClass
+ _objc_retain_x9
- GCC_except_table237
- GCC_except_table248
- GCC_except_table268
- GCC_except_table281
- GCC_except_table378
CStrings:
+ "%s Refusing intent delivery handshake: verified delivery is off"
+ "%s Refusing intent forwarding action delivered without the handshake"
+ "%s Would refuse intent delivery without the handshake from %{public}@ (claimed): missing %{public}@ (audit mode)"
+ "-[INUIAppIntentForwardingActionExecutor executeAction:completionHandler:]"
+ "Intent delivery requires the verified handshake"
+ "Verified intent delivery is off"
+ "v56@?0@\"INIntentForwardingAction\"8{?=[8I]}16@?<v@?@\"INIntentForwardingActionResponse\">48"
```
