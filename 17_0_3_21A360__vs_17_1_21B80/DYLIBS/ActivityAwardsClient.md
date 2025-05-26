## ActivityAwardsClient

> `/System/Library/PrivateFrameworks/ActivityAwardsClient.framework/ActivityAwardsClient`

```diff

-569.1.1.0.0
-  __TEXT.__text: 0x4828
-  __TEXT.__auth_stubs: 0x340
-  __TEXT.__objc_methlist: 0x190
+572.3.0.0.0
+  __TEXT.__text: 0x4b58
+  __TEXT.__auth_stubs: 0x350
+  __TEXT.__objc_methlist: 0x1ac
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x10b
   __TEXT.__gcc_except_tab: 0x104
-  __TEXT.__oslogstring: 0x4a4
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__oslogstring: 0x53e
+  __TEXT.__unwind_info: 0x184
   __TEXT.__objc_classname: 0x60
   __TEXT.__objc_methname: 0x7f5
   __TEXT.__objc_methtype: 0x22c
   __TEXT.__objc_stubs: 0x520
   __DATA_CONST.__got: 0x10
-  __DATA_CONST.__const: 0x2b8
+  __DATA_CONST.__const: 0x2e0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __AUTH_CONST.__cfstring: 0xc0
   __AUTH_CONST.__objc_const: 0x90
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__auth_got: 0x1b8
   __DATA.__objc_protorefs: 0x10
   __DATA.__objc_classrefs: 0x68
   __DATA.__objc_superrefs: 0x10

   - /System/Library/PrivateFrameworks/ActivityAchievements.framework/ActivityAchievements
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 106
-  Symbols:   402
-  CStrings:  161
+  Functions: 114
+  Symbols:   420
+  CStrings:  164
 
Symbols:
+ -[AACAwardsClient dealloc]
+ -[AACXPCClient dealloc].cold.1
+ -[AACXPCClient invalidate]
+ -[AACXPCClient invalidate].cold.1
+ GCC_except_table12
+ GCC_except_table31
+ GCC_except_table38
+ GCC_except_table43
+ GCC_except_table8
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke_4.cold.2
+ ___53-[AACXPCClient _remoteSynchronousProxy:errorHandler:]_block_invoke_4.cold.3
+ ___block_descriptor_56_e8_32bs40r48w_e17_v16?0"NSError"8lw48l8r40l8s32l8
+ ___block_descriptor_64_e8_32s40bs48bs56w_e5_v8?0ls32l8w56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40bs48bs56r64w_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16ls32l8r56l8w64l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56bs64bs72r80w_e5_v8?0ls32l8r72l8s40l8w80l8s56l8s64l8s48l8
+ _objc_retain_x23
- GCC_except_table11
- GCC_except_table30
- GCC_except_table37
- GCC_except_table42
- GCC_except_table7
- ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSError"8ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40bs48bs56r_e43_v24?0"NSXPCListenerEndpoint"8"NSError"16ls32l8r56l8s40l8s48l8
- ___block_descriptor_80_e8_32s40s48s56bs64bs72r_e5_v8?0ls32l8r72l8s40l8s56l8s64l8s48l8
CStrings:
+ "Dealloc called on AACXPCClient"
+ "Invalidate called on AACXPCClient"
+ "Invaliding sync XPC endpoint connection after handler returned"
+ "Sync XPC endpoint setup complete for %{public}@, passing proxy to handler."
- "Sync XPC endpoint setup complete for %{public}@."

```
