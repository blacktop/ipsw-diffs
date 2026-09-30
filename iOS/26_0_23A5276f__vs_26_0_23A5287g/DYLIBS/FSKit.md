## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-737.0.10.0.0
-  __TEXT.__text: 0x401fc
+737.0.14.0.1
+  __TEXT.__text: 0x403f0
   __TEXT.__auth_stubs: 0xd20
   __TEXT.__objc_methlist: 0x49c4
   __TEXT.__const: 0x390
   __TEXT.__gcc_except_tab: 0xdd8
-  __TEXT.__cstring: 0x429f
-  __TEXT.__oslogstring: 0x3007
+  __TEXT.__oslogstring: 0x3092
+  __TEXT.__cstring: 0x42df
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_reflstr: 0x16

   __TEXT.__unwind_info: 0x12f0
   __TEXT.__eh_frame: 0x160
   __TEXT.__objc_classname: 0x8e7
-  __TEXT.__objc_methname: 0x9991
+  __TEXT.__objc_methname: 0x99ba
   __TEXT.__objc_methtype: 0x32db
   __TEXT.__objc_stubs: 0x56c0
   __DATA_CONST.__got: 0x3f0
-  __DATA_CONST.__const: 0x1338
+  __DATA_CONST.__const: 0x1360
   __DATA_CONST.__objc_classlist: 0x250
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2470
+  __DATA_CONST.__objc_selrefs: 0x2478
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4A5FA78B-4DD5-3D1D-979A-00CF18401299
-  Functions: 1992
-  Symbols:   6336
-  CStrings:  3320
+  UUID: 9EC86963-8B12-310F-9619-5FDCC5D0EC4D
+  Functions: 1993
+  Symbols:   6339
+  CStrings:  3324
 
Symbols:
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:]
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:].cold.1
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:].cold.2
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:].cold.3
+ -[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:].cold.4
+ ___39-[FSModuleConnector sendCloseResource:]_block_invoke.240
+ ___39-[FSModuleConnector sendCloseResource:]_block_invoke.240.cold.1
+ ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.235
+ ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.235.cold.1
+ ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.243
+ ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.243.cold.1
+ ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.243.cold.2
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.263
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.268
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.268.cold.1
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.268.cold.2
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.270
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.273
+ ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.271
+ ___57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.277
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke.279
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.282
+ ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.282.cold.1
+ ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.250
+ ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.252
+ ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.259
+ ___70-[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:]_block_invoke
+ ___block_descriptor_56_e8_32s40bs48bs_e20_v20?0i8"NSError"12ls40l8s48l8s32l8
+ ___block_literal_global.237
+ ___block_literal_global.239
+ ___block_literal_global.242
+ ___block_literal_global.255
+ ___block_literal_global.261
+ ___block_literal_global.281
+ ___block_literal_global.78
+ _objc_msgSend$sendConfigureUserClientWithReplyHandler:
- -[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:]
- -[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:].cold.1
- -[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:].cold.2
- -[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:].cold.3
- ___39-[FSModuleConnector sendCloseResource:]_block_invoke.239
- ___39-[FSModuleConnector sendCloseResource:]_block_invoke.239.cold.1
- ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.234
- ___40-[FSModuleConnector sendRevokeResource:]_block_invoke.234.cold.1
- ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.242
- ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.242.cold.1
- ___51-[FSModuleConnector sendWipeResource:replyHandler:]_block_invoke.242.cold.2
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.262
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.267
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.267.cold.1
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.267.cold.2
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.269
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke.272
- ___55-[FSModuleConnector loadResource:options:replyHandler:]_block_invoke_2.270
- ___57-[FSModuleConnector unloadResource:options:replyHandler:]_block_invoke.276
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke.278
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.281
- ___66-[FSModuleConnector activateVolume:resource:options:replyHandler:]_block_invoke_2.281.cold.1
- ___67-[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:]_block_invoke
- ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.249
- ___69-[FSModuleConnector checkWithOptions:connection:taskID:replyHandler:]_block_invoke.251
- ___70-[FSModuleConnector formatWithOptions:connection:taskID:replyHandler:]_block_invoke.257
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.241
- ___block_literal_global.254
- ___block_literal_global.260
- ___block_literal_global.280
- ___block_literal_global.77
- _objc_msgSend$fsMachPort
CStrings:
+ "%s: Created FSMachPort = %d"
+ "%s: Extension (%{public}@) doesn't have a mach port to configure user client"
+ "%s: Failed to create FSMachPort"
+ "%s: Task didn't start yet, replying (%@) to FSMessageConnection"
+ "-[FSMessageReceiverDelegateWrapper completed:replyHandler:]"
+ "-[FSModuleExtension(Project) sendConfigureUserClientWithReplyHandler:]"
+ "sendConfigureUserClientWithReplyHandler:"
- "%s: Failed to create LiveFSMachPort"
- "-[FSModuleExtension(Project) sendConfigureUserClient:replyHandler:]"
- "created fsFSMachPort = %d"

```
