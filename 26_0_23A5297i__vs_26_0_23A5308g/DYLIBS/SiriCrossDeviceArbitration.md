## SiriCrossDeviceArbitration

> `/System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration`

```diff

-3500.59.1.0.0
-  __TEXT.__text: 0x2f9ac
+3500.66.1.0.0
+  __TEXT.__text: 0x2fee0
   __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x3134
+  __TEXT.__objc_methlist: 0x3154
   __TEXT.__dlopen_cstrs: 0x118
-  __TEXT.__const: 0x1e0
-  __TEXT.__gcc_except_tab: 0x4e0
-  __TEXT.__oslogstring: 0x5080
-  __TEXT.__cstring: 0x5952
-  __TEXT.__unwind_info: 0xd08
-  __TEXT.__objc_classname: 0x61d
-  __TEXT.__objc_methname: 0x8011
+  __TEXT.__const: 0x1e8
+  __TEXT.__gcc_except_tab: 0x4f0
+  __TEXT.__oslogstring: 0x50df
+  __TEXT.__cstring: 0x5b1f
+  __TEXT.__unwind_info: 0xd10
+  __TEXT.__objc_classname: 0x62b
+  __TEXT.__objc_methname: 0x8064
   __TEXT.__objc_methtype: 0x1907
-  __TEXT.__objc_stubs: 0x5ec0
+  __TEXT.__objc_stubs: 0x5f20
   __DATA_CONST.__got: 0x300
   __DATA_CONST.__const: 0x1108
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1e68
+  __DATA_CONST.__objc_selrefs: 0x1e80
   __DATA_CONST.__objc_superrefs: 0x138
   __DATA_CONST.__objc_arraydata: 0xa8
   __AUTH_CONST.__auth_got: 0x428
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x2900
-  __AUTH_CONST.__objc_const: 0x5478
+  __AUTH_CONST.__cfstring: 0x2b80
+  __AUTH_CONST.__objc_const: 0x5498
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x190
-  __DATA.__objc_ivar: 0x4f4
+  __AUTH.__objc_data: 0x230
+  __DATA.__objc_ivar: 0x4f8
   __DATA.__data: 0x5d0
   __DATA.__bss: 0x1a0
-  __DATA_DIRTY.__objc_data: 0xbe0
+  __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__bss: 0x8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 71600471-CFED-38D4-8C16-A5D58E39C2A1
-  Functions: 1200
-  Symbols:   4245
-  CStrings:  2958
+  UUID: C3C91A3D-937E-3869-BFE7-D8507F6F23BF
+  Functions: 1203
+  Symbols:   4255
+  CStrings:  3005
 
Symbols:
+ -[SCDACoordinator winningAdvertisement]
+ -[SCDARecord initWithRealityTrigger:device:]
+ -[SCDARecord(InternalDebug) deviceName]
+ -[SCDARecord(InternalDebug) winReason]
+ GCC_except_table1000
+ GCC_except_table1023
+ GCC_except_table1044
+ GCC_except_table1106
+ GCC_except_table480
+ GCC_except_table533
+ GCC_except_table534
+ GCC_except_table540
+ GCC_except_table638
+ GCC_except_table743
+ GCC_except_table746
+ GCC_except_table853
+ GCC_except_table868
+ GCC_except_table925
+ GCC_except_table929
+ GCC_except_table956
+ _OBJC_IVAR_$_SCDACoordinator._isDelayingAdvertisement
+ __OBJC_$_INSTANCE_METHODS_SCDARecord(InternalDebug)
+ ___31-[SCDACoordinator _enterState:]_block_invoke.246
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.337
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.340
+ ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.341
+ ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.370
+ ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.369
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.348
+ ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.357
+ ___Block_byref_object_copy_.1115
+ ___Block_byref_object_copy_.1685
+ ___Block_byref_object_copy_.2347
+ ___Block_byref_object_dispose_.1116
+ ___Block_byref_object_dispose_.1686
+ ___Block_byref_object_dispose_.2348
+ ___block_literal_global.1069
+ ___block_literal_global.1130
+ ___block_literal_global.1163
+ ___block_literal_global.1188
+ ___block_literal_global.1239
+ ___block_literal_global.1555
+ ___block_literal_global.1763
+ ___block_literal_global.235
+ ___block_literal_global.237
+ ___block_literal_global.2710
+ ___block_literal_global.361
+ ___block_literal_global.364
+ ___block_literal_global.368
+ ___block_literal_global.771
+ _objc_msgSend$deviceName
+ _objc_msgSend$generateVisionProConfidence
+ _objc_msgSend$winReason
- -[SCDARecord isCarplayTrump]
- GCC_except_table1021
- GCC_except_table1041
- GCC_except_table1103
- GCC_except_table478
- GCC_except_table531
- GCC_except_table532
- GCC_except_table538
- GCC_except_table636
- GCC_except_table741
- GCC_except_table744
- GCC_except_table851
- GCC_except_table866
- GCC_except_table923
- GCC_except_table927
- GCC_except_table954
- GCC_except_table998
- __OBJC_$_INSTANCE_METHODS_SCDARecord
- ___31-[SCDACoordinator _enterState:]_block_invoke.234
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.325
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.328
- ___36-[SCDACoordinator _advertiseTrigger]_block_invoke.329
- ___42-[SCDACoordinator _waitWiProx:andExecute:]_block_invoke.358
- ___52-[SCDACoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.357
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.336
- ___89-[SCDACoordinator _advertiseWith:afterDelay:maxInterval:voiceTriggerLatency:thenExecute:]_block_invoke.345
- ___Block_byref_object_copy_.1114
- ___Block_byref_object_copy_.1684
- ___Block_byref_object_copy_.2351
- ___Block_byref_object_dispose_.1115
- ___Block_byref_object_dispose_.1685
- ___Block_byref_object_dispose_.2352
- ___block_literal_global.1068
- ___block_literal_global.1129
- ___block_literal_global.1162
- ___block_literal_global.1187
- ___block_literal_global.1238
- ___block_literal_global.1554
- ___block_literal_global.1762
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.2702
- ___block_literal_global.349
- ___block_literal_global.352
- ___block_literal_global.356
- ___block_literal_global.772
CStrings:
+ "#scda_winlose_reason %@ election %@ %@ due to %@."
+ "%s #scda adjustByMultipler deprecated: Multiplier value of %f will be dropped!"
+ "%s #scda adjustedScoreOverride was set: %du"
+ "Attention (probably) (C: %03d)"
+ "Better Device\n(G: %03d, C: %03d, H: %#06x)"
+ "Button Press"
+ "Carplay Override"
+ "Emergency being handled"
+ "In-Ear Override"
+ "InternalDebug"
+ "Loudness (G: %03d)"
+ "Personalized Siri Setup"
+ "Raise to Speak"
+ "Siri Speaking"
+ "Slow Decision"
+ "Timer or Alarm firing"
+ "Trigger Phrase played by other device"
+ "UI Showing (In Task)"
+ "Vision Pro Override"
+ "Watch Loudness Threshold"
+ "_isDelayingAdvertisement"
+ "deviceName"
+ "initWithRealityTrigger:device:"
+ "on"
+ "stay awake signal (for potentially handling emergencies)"
+ "this device arriving late to the election"
+ "to"
+ "winReason"
+ "winningAdvertisement"
- "%s #scda adjustByMultipler deprecated: Multiplier value of %f will be droped!"
- "isCarplayTrump"

```
