## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3500.66.1.0.0
-  __TEXT.__text: 0x2fee0
+3505.2.1.0.0
+  __TEXT.__text: 0x2fea8
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_methlist: 0x3154
   __TEXT.__dlopen_cstrs: 0x118
   __TEXT.__const: 0x1e8
   __TEXT.__gcc_except_tab: 0x4f0
-  __TEXT.__oslogstring: 0x50df
+  __TEXT.__oslogstring: 0x50ae
   __TEXT.__cstring: 0x5b1f
   __TEXT.__unwind_info: 0xd10
   __TEXT.__objc_classname: 0x62b

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 48397F05-0074-38C0-83E2-E1CBC2A74C4C
+  UUID: 64436F72-9CAE-342C-B0C4-41354B0B73C4
   Functions: 1203
   Symbols:   4255
-  CStrings:  3005
+  CStrings:  3004
 
Symbols:
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.338
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.342
+ ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.371
+ ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.370
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.349
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.358
+ ___Block_byref_object_copy_.1114
+ ___Block_byref_object_copy_.1684
+ ___Block_byref_object_dispose_.1115
+ ___Block_byref_object_dispose_.1685
+ ___block_literal_global.1068
+ ___block_literal_global.1129
+ ___block_literal_global.1162
+ ___block_literal_global.1187
+ ___block_literal_global.1238
+ ___block_literal_global.1554
+ ___block_literal_global.1762
+ ___block_literal_global.362
+ ___block_literal_global.365
+ ___block_literal_global.369
+ ___block_literal_global.442
+ ___block_literal_global.498
+ ___block_literal_global.770
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.337
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.340
- ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.370
- ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.369
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.348
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.357
- ___Block_byref_object_copy_.1115
- ___Block_byref_object_copy_.1685
- ___Block_byref_object_dispose_.1116
- ___Block_byref_object_dispose_.1686
- ___block_literal_global.1069
- ___block_literal_global.1130
- ___block_literal_global.1163
- ___block_literal_global.1188
- ___block_literal_global.1239
- ___block_literal_global.1555
- ___block_literal_global.1763
- ___block_literal_global.361
- ___block_literal_global.364
- ___block_literal_global.368
- ___block_literal_global.443
- ___block_literal_global.499
- ___block_literal_global.771
Functions:
~ -[SCDACoordinator _advertiseTrigger] : 1508 -> 1544
~ -[SCDAPerceptualAudioHash initWithData:] : 1096 -> 968
~ -[SCDACoordinator _advertiseSuppressTriggerInOutput] : 728 -> 764
CStrings:
- "%s #scda voice trigger is invalid, resetting: %f"

```
