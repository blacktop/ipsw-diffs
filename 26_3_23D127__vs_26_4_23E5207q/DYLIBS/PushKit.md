## PushKit

> `/System/Library/Frameworks/PushKit.framework/PushKit`

```diff

-109.100.1.0.0
-  __TEXT.__text: 0x4714
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0x778
+109.500.11.0.0
+  __TEXT.__text: 0x4d44
+  __TEXT.__auth_stubs: 0x420
+  __TEXT.__objc_methlist: 0x798
   __TEXT.__const: 0x48
   __TEXT.__gcc_except_tab: 0x84
   __TEXT.__cstring: 0x646
-  __TEXT.__unwind_info: 0x1f8
-  __TEXT.__objc_classname: 0x196
-  __TEXT.__objc_methname: 0x136c
-  __TEXT.__objc_methtype: 0x308
-  __TEXT.__objc_stubs: 0xa80
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__const: 0x318
-  __DATA_CONST.__objc_classlist: 0x28
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__objc_classname: 0x1a9
+  __TEXT.__objc_methname: 0x13f5
+  __TEXT.__objc_methtype: 0x315
+  __TEXT.__objc_stubs: 0xac0
+  __DATA_CONST.__got: 0x98
+  __DATA_CONST.__const: 0x340
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f8
+  __DATA_CONST.__objc_selrefs: 0x510
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__auth_got: 0x220
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x3a0
-  __AUTH_CONST.__objc_const: 0xd58
-  __DATA.__objc_ivar: 0x64
+  __AUTH_CONST.__objc_const: 0xe28
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x3c0
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/Frameworks/Security.framework/Security
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F057E10-0CAC-372C-A0E5-2589DA8284F0
-  Functions: 154
-  Symbols:   643
-  CStrings:  345
+  UUID: 5A97A058-7F32-393C-B0E9-CA22559EE88E
+  Functions: 162
+  Symbols:   665
+  CStrings:  353
 
Symbols:
+ -[PKVoIPPushMetadata mustReport]
+ -[PKVoIPPushMetadata setMustReport:]
+ _OBJC_CLASS_$_PKVoIPPushMetadata
+ _OBJC_IVAR_$_PKVoIPPushMetadata._mustReport
+ _OBJC_METACLASS_$_PKVoIPPushMetadata
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ __OBJC_$_INSTANCE_METHODS_PKVoIPPushMetadata
+ __OBJC_$_INSTANCE_VARIABLES_PKVoIPPushMetadata
+ __OBJC_$_PROP_LIST_PKVoIPPushMetadata
+ __OBJC_CLASS_RO_$_PKVoIPPushMetadata
+ __OBJC_METACLASS_RO_$_PKVoIPPushMetadata
+ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_4
+ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_5
+ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_6
+ ___73-[PKPushRegistry voipPayloadReceived:mustPostCall:withCompletionHandler:]_block_invoke_7
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_literal_global.47
+ _dispatch_after
+ _dispatch_time
+ _objc_msgSend$pushRegistry:didReceiveIncomingVoIPPushWithPayload:metadata:withCompletionHandler:
+ _objc_msgSend$setMustReport:
+ _objc_retainBlock
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.44
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x23
- _objc_retain_x25
- _objc_retain_x26
- _objc_retain_x8
CStrings:
+ "B"
+ "PKVoIPPushMetadata"
+ "TB,V_mustReport"
+ "_mustReport"
+ "mustReport"
+ "pushRegistry:didReceiveIncomingVoIPPushWithPayload:metadata:withCompletionHandler:"
+ "setMustReport:"
+ "v20@0:8B16"

```
