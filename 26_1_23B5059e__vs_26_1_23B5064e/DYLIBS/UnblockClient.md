## UnblockClient

> `/System/Library/PrivateFrameworks/UnblockClient.framework/UnblockClient`

```diff

-10.0.0.0.0
-  __TEXT.__text: 0x5dfc
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x508
-  __TEXT.__const: 0x70
-  __TEXT.__gcc_except_tab: 0x140
-  __TEXT.__cstring: 0xb1b
-  __TEXT.__oslogstring: 0x60b
+12.0.0.0.0
+  __TEXT.__text: 0x6000
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x538
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0x150
+  __TEXT.__cstring: 0xb68
+  __TEXT.__oslogstring: 0x615
   __TEXT.__unwind_info: 0x170
   __TEXT.__objc_classname: 0x9c
-  __TEXT.__objc_methname: 0xedc
-  __TEXT.__objc_methtype: 0x1c5
-  __TEXT.__objc_stubs: 0xb80
+  __TEXT.__objc_methname: 0xf81
+  __TEXT.__objc_methtype: 0x1d5
+  __TEXT.__objc_stubs: 0xc00
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b8
+  __DATA_CONST.__objc_selrefs: 0x3e8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x278
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0xea0
-  __AUTH_CONST.__objc_const: 0xae0
+  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__const: 0xc0
+  __AUTH_CONST.__cfstring: 0xf00
+  __AUTH_CONST.__objc_const: 0xb40
   __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x80
+  __DATA.__objc_ivar: 0x88
   __DATA.__data: 0xc0
   __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 35BCD319-8025-399C-904F-AD57F0F33F41
-  Functions: 132
-  Symbols:   574
-  CStrings:  490
+  UUID: 5618E0BA-9585-384A-82FE-DF63199C06B0
+  Functions: 140
+  Symbols:   600
+  CStrings:  508
 
Symbols:
+ -[UBProcessInfo initWithPid:name:is3P:]
+ -[UBProcessInfo is3P]
+ -[UBProcessInfo telemetryName]
+ -[UBStuckServiceRecoveryResult serviceProcessIs3P]
+ -[UBStuckServiceRecoveryResult setServiceProcessIs3P:]
+ GCC_except_table53
+ _OBJC_IVAR_$_UBProcessInfo._is3P
+ _OBJC_IVAR_$_UBStuckServiceRecoveryResult._serviceProcessIs3P
+ _OUTLINED_FUNCTION_5
+ ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke.327
+ ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke_2.338
+ ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke_3
+ ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke_4
+ ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.615
+ ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.616
+ ___block_literal_global.340
+ ___block_literal_global.351
+ ___block_literal_global.359
+ ___block_literal_global.574
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$serviceProcessIs3P
+ _objc_msgSend$telemetryName
+ _objc_retain_x27
- -[UBProcessInfo initWithPid:name:]
- GCC_except_table51
- ___58-[UBStuckServiceRecoveryResult _recoveryHadEffectiveness:]_block_invoke.312
- ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.587
- ___61-[UBUnblockClient recover:stackshotData:replyQueue:callback:]_block_invoke.588
- ___block_literal_global.546
CStrings:
+ "%s for pid:%d tid:%llu timeElapsed:%.1f incidentUUID:%@ recoveryStatus:%@ issueType:%@ recoveryConfidence:%@"
+ "@32@0:8i16@20B28"
+ "B"
+ "Result has invalid pid/thread_id/incident service's data: %@ vs %@"
+ "TB,R,V_is3P"
+ "TB,V_serviceProcessIs3P"
+ "ThirdPartyProcess"
+ "_is3P"
+ "_serviceProcessIs3P"
+ "decodeBoolForKey:"
+ "encodeBool:forKey:"
+ "initWithPid:name:is3P:"
+ "is3P"
+ "serviceProcessIs3P"
+ "setServiceProcessIs3P:"
+ "telemetryName"
+ "v20@0:8B16"
- "%s for pid:%d tid:%llu recoveryStatus:%@ issueType:%@ recoveryConfidence:%@"
- "@28@0:8i16@20"
- "initWithPid:name:"

```
