## CascadeEngine

> `/System/Library/PrivateFrameworks/CascadeEngine.framework/CascadeEngine`

```diff

-200.0.0.0.0
-  __TEXT.__text: 0x20330
+200.1.0.0.0
+  __TEXT.__text: 0x20778
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x1864
-  __TEXT.__const: 0x118
-  __TEXT.__gcc_except_tab: 0x79c
-  __TEXT.__cstring: 0x127a
-  __TEXT.__oslogstring: 0x372b
+  __TEXT.__objc_methlist: 0x186c
+  __TEXT.__const: 0x120
+  __TEXT.__gcc_except_tab: 0x7ac
+  __TEXT.__cstring: 0x12d5
+  __TEXT.__oslogstring: 0x37bc
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__unwind_info: 0x880
+  __TEXT.__unwind_info: 0x890
   __TEXT.__objc_classname: 0x46f
-  __TEXT.__objc_methname: 0x551e
+  __TEXT.__objc_methname: 0x5526
   __TEXT.__objc_methtype: 0x1066
-  __TEXT.__objc_stubs: 0x4680
+  __TEXT.__objc_stubs: 0x46a0
   __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0xb10
+  __DATA_CONST.__const: 0xb38
   __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13e8
+  __DATA_CONST.__objc_selrefs: 0x13f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__auth_got: 0x3b8
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x12c0
+  __AUTH_CONST.__cfstring: 0x12e0
   __AUTH_CONST.__objc_const: 0x3330
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E347FCA0-A743-30AC-BB11-1DBD8BEF0DD0
-  Functions: 708
-  Symbols:   2809
-  CStrings:  1681
+  UUID: 5648FD0E-4662-30CA-BFBE-A09628361F40
+  Functions: 712
+  Symbols:   2820
+  CStrings:  1686
 
Symbols:
+ -[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:].cold.1
+ -[CCRapportSyncSession cancel:]
+ GCC_except_table14
+ GCC_except_table26
+ GCC_except_table39
+ GCC_except_table68
+ ___116-[CCRapportSyncEngine _activateSyncSessionWithReason:forInteractionType:activationHandler:sessionCompletionHandler:]_block_invoke_3
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.80
+ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.cold.5
+ ___83-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:]_block_invoke.47
+ ___block_descriptor_56_e8_32bs40w48w_e17_v16?0"NSError"8lw40l8w48l8s32l8
+ ___block_literal_global.85
+ ___block_literal_global.87
+ ___block_literal_global.89
+ _objc_msgSend$cancel:
- GCC_except_table13
- GCC_except_table15
- GCC_except_table18
- GCC_except_table20
- GCC_except_table25
- ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke.77
- ___83-[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:]_block_invoke.46
- ___block_literal_global.82
- ___block_literal_global.84
- ___block_literal_global.86
Functions:
+ -[CCRapportSyncSession cancel:]
~ -[CCRapportSyncEngine _activateSyncSessionWithReason:forInteractionType:activationHandler:sessionCompletionHandler:] : 1076 -> 1240
+ ___116-[CCRapportSyncEngine _activateSyncSessionWithReason:forInteractionType:activationHandler:sessionCompletionHandler:]_block_invoke_3
~ -[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:] : 948 -> 1020
~ ___57-[CCRapportSyncEngine fetchMergeableDeltasRequestHandler]_block_invoke : 2780 -> 3024
+ _OUTLINED_FUNCTION_3
~ -[CCRapportSyncEngine initWithQueue:error:].cold.1 : 144 -> 152
+ -[CCRapportSyncEngine sendFetchMergeableDeltasRequest:forInteraction:continueSync:].cold.1
~ -[CCRapportSyncEngine handleIncomingMergeableDeltaFileTransfer:fromDevice:].cold.1 : 160 -> 168
~ -[CCRapportSyncEngine handleIncomingMergeableDeltaFileTransfer:fromDevice:].cold.2 : 180 -> 188
CStrings:
+ " and submitting reciprocal interaction"
+ " missing inOptions[RPOptionSenderFileTransferTargetID] in fetchMergeableDeltas for set %@"
+ "%@ ignoring device not listing service from serviceTypes com.apple.biomesyncd.cascade.rapport"
+ "%@: cancelling sync session (%@) after activation error: %@"
+ "%@: cannot build file transfer session without localDevice fileTransferTargetID: %@"
+ "cancel:"
- " and ubmitting reciprocal interaction"
- "%@ ignoring device not listing service from serviceTypescom.apple.biomesyncd.cascade.rapport"

```
