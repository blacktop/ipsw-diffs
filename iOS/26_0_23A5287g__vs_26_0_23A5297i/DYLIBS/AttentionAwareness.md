## AttentionAwareness

> `/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness`

```diff

-237.0.0.0.0
-  __TEXT.__text: 0x37c30
+237.0.0.0.1
+  __TEXT.__text: 0x37c50
   __TEXT.__auth_stubs: 0x9c0
-  __TEXT.__objc_methlist: 0x274c
-  __TEXT.__const: 0x178
+  __TEXT.__objc_methlist: 0x276c
+  __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0x820
-  __TEXT.__oslogstring: 0x55c5
+  __TEXT.__oslogstring: 0x55d5
   __TEXT.__cstring: 0x39af
-  __TEXT.__unwind_info: 0xc78
+  __TEXT.__unwind_info: 0xc80
   __TEXT.__objc_classname: 0x5da
-  __TEXT.__objc_methname: 0x52ee
+  __TEXT.__objc_methname: 0x530e
   __TEXT.__objc_methtype: 0x1908
-  __TEXT.__objc_stubs: 0x43a0
+  __TEXT.__objc_stubs: 0x43c0
   __DATA_CONST.__got: 0x210
   __DATA_CONST.__const: 0xe20
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1448
+  __DATA_CONST.__objc_selrefs: 0x1450
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x108
   __DATA_CONST.__objc_arraydata: 0x40

   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x54c
   __DATA.__data: 0xae0
-  __DATA.__bss: 0x48
+  __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0x820
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__bss: 0x148
+  __DATA_DIRTY.__bss: 0x138
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E465CCA7-652C-31F1-8024-0B74BB109E8B
-  Functions: 954
-  Symbols:   3646
-  CStrings:  2345
+  UUID: 5765D866-A1B3-3BF7-9355-D44F375CECAC
+  Functions: 957
+  Symbols:   3653
+  CStrings:  2346
 
Symbols:
+ -[AWAttentionSampler isMatchOrEnrollOperationRunning]
+ -[AWPearlAttentionSampler isMatchOrEnrollOperationRunning]
+ -[AWScheduler isMatchOrEnrollOperationRunning]
+ GCC_except_table115
+ GCC_except_table162
+ GCC_except_table166
+ GCC_except_table181
+ GCC_except_table200
+ GCC_except_table202
+ GCC_except_table226
+ GCC_except_table230
+ GCC_except_table262
+ GCC_except_table286
+ GCC_except_table343
+ GCC_except_table355
+ GCC_except_table374
+ GCC_except_table434
+ GCC_except_table508
+ GCC_except_table514
+ GCC_except_table519
+ GCC_except_table523
+ GCC_except_table527
+ GCC_except_table532
+ GCC_except_table536
+ GCC_except_table540
+ GCC_except_table607
+ GCC_except_table631
+ GCC_except_table708
+ GCC_except_table79
+ GCC_except_table841
+ GCC_except_table867
+ GCC_except_table871
+ GCC_except_table878
+ GCC_except_table882
+ GCC_except_table883
+ GCC_except_table893
+ GCC_except_table895
+ GCC_except_table900
+ GCC_except_table906
+ GCC_except_table908
+ ___Block_byref_object_copy_.1031
+ ___Block_byref_object_copy_.1130
+ ___Block_byref_object_copy_.1635
+ ___Block_byref_object_copy_.2050
+ ___Block_byref_object_copy_.2318
+ ___Block_byref_object_copy_.585
+ ___Block_byref_object_copy_.716
+ ___Block_byref_object_dispose_.1032
+ ___Block_byref_object_dispose_.1131
+ ___Block_byref_object_dispose_.1636
+ ___Block_byref_object_dispose_.2051
+ ___Block_byref_object_dispose_.2319
+ ___Block_byref_object_dispose_.586
+ ___Block_byref_object_dispose_.717
+ ___block_literal_global.1069
+ ___block_literal_global.1153
+ ___block_literal_global.1573
+ ___block_literal_global.1651
+ ___block_literal_global.2070
+ ___block_literal_global.221
+ ___block_literal_global.2350
+ ___block_literal_global.2720
+ ___block_literal_global.454
+ ___block_literal_global.714
+ ___block_literal_global.869
+ _objc_msgSend$isMatchOrEnrollOperationRunning
+ _sharedManager.manager.1154
+ _sharedManager.onceToken.1152
- GCC_except_table113
- GCC_except_table160
- GCC_except_table165
- GCC_except_table180
- GCC_except_table199
- GCC_except_table201
- GCC_except_table225
- GCC_except_table229
- GCC_except_table261
- GCC_except_table285
- GCC_except_table342
- GCC_except_table354
- GCC_except_table373
- GCC_except_table432
- GCC_except_table506
- GCC_except_table512
- GCC_except_table517
- GCC_except_table521
- GCC_except_table525
- GCC_except_table530
- GCC_except_table534
- GCC_except_table538
- GCC_except_table605
- GCC_except_table629
- GCC_except_table705
- GCC_except_table78
- GCC_except_table838
- GCC_except_table864
- GCC_except_table868
- GCC_except_table872
- GCC_except_table877
- GCC_except_table879
- GCC_except_table890
- GCC_except_table892
- GCC_except_table897
- GCC_except_table903
- GCC_except_table905
- ___Block_byref_object_copy_.1022
- ___Block_byref_object_copy_.1121
- ___Block_byref_object_copy_.1629
- ___Block_byref_object_copy_.2046
- ___Block_byref_object_copy_.2314
- ___Block_byref_object_copy_.577
- ___Block_byref_object_copy_.706
- ___Block_byref_object_dispose_.1023
- ___Block_byref_object_dispose_.1122
- ___Block_byref_object_dispose_.1630
- ___Block_byref_object_dispose_.2047
- ___Block_byref_object_dispose_.2315
- ___Block_byref_object_dispose_.578
- ___Block_byref_object_dispose_.707
- ___block_literal_global.1060
- ___block_literal_global.1144
- ___block_literal_global.1567
- ___block_literal_global.1645
- ___block_literal_global.2067
- ___block_literal_global.216
- ___block_literal_global.2346
- ___block_literal_global.2716
- ___block_literal_global.451
- ___block_literal_global.704
- ___block_literal_global.858
- _sharedManager.manager.1145
- _sharedManager.onceToken.1143
CStrings:
+ "%13.5f: Match or enroll operation underway, send init to polling clients immediately"
+ "%30s:%-4d: %13.5f: Match or enroll operation underway, send init to polling clients immediately"
+ "isMatchOrEnrollOperationRunning"
- "%13.5f: Match or enroll operation underway, initialize the state immediately"
- "%30s:%-4d: %13.5f: Match or enroll operation underway, initialize the state immediately"

```
