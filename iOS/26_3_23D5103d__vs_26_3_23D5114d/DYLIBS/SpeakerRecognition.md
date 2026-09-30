## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3515.8.1.0.0
-  __TEXT.__text: 0x8e074
+3515.11.1.0.0
+  __TEXT.__text: 0x8e64c
   __TEXT.__auth_stubs: 0x1250
-  __TEXT.__objc_methlist: 0x6658
+  __TEXT.__objc_methlist: 0x6680
   __TEXT.__const: 0x518
   __TEXT.__dlopen_cstrs: 0x56
   __TEXT.__cstring: 0x1005e

   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x18a
   __TEXT.__swift5_types: 0x10
-  __TEXT.__gcc_except_tab: 0x2d38
+  __TEXT.__gcc_except_tab: 0x2d4c
   __TEXT.__oslogstring: 0xc814
-  __TEXT.__unwind_info: 0x18e8
+  __TEXT.__unwind_info: 0x1910
   __TEXT.__objc_classname: 0xe2e
-  __TEXT.__objc_methname: 0x11c16
-  __TEXT.__objc_methtype: 0x253e
-  __TEXT.__objc_stubs: 0xa660
+  __TEXT.__objc_methname: 0x11c71
+  __TEXT.__objc_methtype: 0x2568
+  __TEXT.__objc_stubs: 0xa6c0
   __DATA_CONST.__got: 0x948
-  __DATA_CONST.__const: 0x1d40
+  __DATA_CONST.__const: 0x1d68
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3b78
+  __DATA_CONST.__objc_selrefs: 0x3b88
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x218
   __DATA_CONST.__objc_arraydata: 0x3e0
   __AUTH_CONST.__auth_got: 0x940
   __AUTH_CONST.__const: 0x4f0
   __AUTH_CONST.__cfstring: 0x5260
-  __AUTH_CONST.__objc_const: 0xae10
+  __AUTH_CONST.__objc_const: 0xae18
   __AUTH_CONST.__objc_dictobj: 0x9b0
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_floatobj: 0x20

   __AUTH.__data: 0x78
   __DATA.__objc_ivar: 0x834
   __DATA.__data: 0x1060
-  __DATA.__bss: 0xf8
+  __DATA.__bss: 0x100
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0x730
-  __DATA_DIRTY.__bss: 0x50
+  __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/CoreAudio

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 142C550E-E9FC-38AE-B776-05B402CC32EC
-  Functions: 2414
-  Symbols:   8286
-  CStrings:  6096
+  UUID: 96A0F761-8ED1-3ADF-8084-6C6D6EBD5D48
+  Functions: 2420
+  Symbols:   8303
+  CStrings:  6099
 
Symbols:
+ -[SSRVTUITrainingMessageHandler updateTrainingManagerViaXPCForDevice:trainingDeviceUUIDList:withCompletion:]
+ -[SSRVTUITrainingServiceClient updateTrainingManagerViaXPCForDevice:trainingDeviceUUIDList:withCompletion:]
+ GCC_except_table1059
+ GCC_except_table1081
+ GCC_except_table1135
+ GCC_except_table1139
+ GCC_except_table1157
+ GCC_except_table1245
+ GCC_except_table1246
+ GCC_except_table1248
+ GCC_except_table1267
+ GCC_except_table1271
+ GCC_except_table1280
+ GCC_except_table1285
+ GCC_except_table1289
+ GCC_except_table1356
+ GCC_except_table1360
+ GCC_except_table1364
+ GCC_except_table1373
+ GCC_except_table1402
+ GCC_except_table1451
+ GCC_except_table1466
+ GCC_except_table1482
+ GCC_except_table1489
+ GCC_except_table1559
+ GCC_except_table1669
+ GCC_except_table1684
+ GCC_except_table1694
+ GCC_except_table1704
+ GCC_except_table1709
+ GCC_except_table1725
+ GCC_except_table1729
+ GCC_except_table1739
+ GCC_except_table1747
+ GCC_except_table1811
+ GCC_except_table1815
+ GCC_except_table1857
+ GCC_except_table1892
+ GCC_except_table1957
+ GCC_except_table1966
+ GCC_except_table1975
+ GCC_except_table1986
+ GCC_except_table1995
+ GCC_except_table2014
+ GCC_except_table2076
+ GCC_except_table390
+ GCC_except_table400
+ GCC_except_table403
+ GCC_except_table440
+ GCC_except_table480
+ GCC_except_table532
+ GCC_except_table536
+ GCC_except_table551
+ GCC_except_table564
+ GCC_except_table637
+ GCC_except_table645
+ GCC_except_table651
+ GCC_except_table736
+ GCC_except_table814
+ GCC_except_table855
+ GCC_except_table860
+ GCC_except_table876
+ GCC_except_table879
+ GCC_except_table969
+ GCC_except_table972
+ GCC_except_table974
+ GCC_except_table977
+ GCC_except_table979
+ GCC_except_table982
+ ___107-[SSRVTUITrainingServiceClient updateTrainingManagerViaXPCForDevice:trainingDeviceUUIDList:withCompletion:]_block_invoke
+ ___107-[SSRVTUITrainingServiceClient updateTrainingManagerViaXPCForDevice:trainingDeviceUUIDList:withCompletion:]_block_invoke_2
+ ___43-[SSRVTUITrainingServiceClient _connection]_block_invoke.11
+ ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.27
+ ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.29
+ ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.33
+ ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_2.28
+ ___80-[SSRVTUITrainingManager updateTrainingManagerForDevice:trainingDeviceUUIDList:]_block_invoke
+ ___80-[SSRVTUITrainingManager updateTrainingManagerForDevice:trainingDeviceUUIDList:]_block_invoke_2
+ ___Block_byref_object_copy_.2045
+ ___Block_byref_object_copy_.2285
+ ___Block_byref_object_copy_.2450
+ ___Block_byref_object_copy_.3132
+ ___Block_byref_object_copy_.3708
+ ___Block_byref_object_copy_.3863
+ ___Block_byref_object_copy_.4024
+ ___Block_byref_object_copy_.4807
+ ___Block_byref_object_copy_.5171
+ ___Block_byref_object_copy_.5303
+ ___Block_byref_object_copy_.5516
+ ___Block_byref_object_copy_.5711
+ ___Block_byref_object_copy_.5914
+ ___Block_byref_object_copy_.6723
+ ___Block_byref_object_copy_.7172
+ ___Block_byref_object_copy_.7287
+ ___Block_byref_object_copy_.7512
+ ___Block_byref_object_copy_.7856
+ ___Block_byref_object_copy_.8667
+ ___Block_byref_object_copy_.990
+ ___Block_byref_object_dispose_.2046
+ ___Block_byref_object_dispose_.2286
+ ___Block_byref_object_dispose_.2451
+ ___Block_byref_object_dispose_.3133
+ ___Block_byref_object_dispose_.3709
+ ___Block_byref_object_dispose_.3864
+ ___Block_byref_object_dispose_.4025
+ ___Block_byref_object_dispose_.4808
+ ___Block_byref_object_dispose_.5172
+ ___Block_byref_object_dispose_.5304
+ ___Block_byref_object_dispose_.5517
+ ___Block_byref_object_dispose_.5712
+ ___Block_byref_object_dispose_.5915
+ ___Block_byref_object_dispose_.6724
+ ___Block_byref_object_dispose_.7173
+ ___Block_byref_object_dispose_.7288
+ ___Block_byref_object_dispose_.7513
+ ___Block_byref_object_dispose_.7857
+ ___Block_byref_object_dispose_.8668
+ ___Block_byref_object_dispose_.991
+ ___block_descriptor_72_e8_32s40s48s56r_e5_v8?0ls32l8s40l8r56l8s48l8
+ ___block_literal_global.1726
+ ___block_literal_global.2063
+ ___block_literal_global.3015
+ ___block_literal_global.31
+ ___block_literal_global.3884
+ ___block_literal_global.3946
+ ___block_literal_global.4475
+ ___block_literal_global.4850
+ ___block_literal_global.5065
+ ___block_literal_global.5999
+ ___block_literal_global.6201
+ ___block_literal_global.6777
+ ___block_literal_global.7297
+ ___block_literal_global.7545
+ ___block_literal_global.7734
+ ___block_literal_global.8007
+ ___block_literal_global.8196
+ ___block_literal_global.8508
+ ___block_literal_global.8970
+ ___block_literal_global.9340
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$updateTrainingManagerForDevice:trainingDeviceUUIDList:
+ _objc_msgSend$updateTrainingManagerViaXPCForDevice:trainingDeviceUUIDList:withCompletion:
+ _sharedInstance.onceToken.1725
+ _sharedInstance.onceToken.3945
+ _sharedInstance.onceToken.8006
+ _sharedInstance.onceToken.8507
+ _sharedManager.onceToken.7544
- GCC_except_table1053
- GCC_except_table1075
- GCC_except_table1129
- GCC_except_table1133
- GCC_except_table1151
- GCC_except_table1239
- GCC_except_table1240
- GCC_except_table1242
- GCC_except_table1261
- GCC_except_table1265
- GCC_except_table1274
- GCC_except_table1279
- GCC_except_table1283
- GCC_except_table1344
- GCC_except_table1354
- GCC_except_table1358
- GCC_except_table1361
- GCC_except_table1396
- GCC_except_table1445
- GCC_except_table1460
- GCC_except_table1476
- GCC_except_table1483
- GCC_except_table1553
- GCC_except_table1657
- GCC_except_table1678
- GCC_except_table1688
- GCC_except_table1698
- GCC_except_table1703
- GCC_except_table1719
- GCC_except_table1723
- GCC_except_table1727
- GCC_except_table1741
- GCC_except_table1805
- GCC_except_table1809
- GCC_except_table1851
- GCC_except_table1886
- GCC_except_table1951
- GCC_except_table1960
- GCC_except_table1969
- GCC_except_table1980
- GCC_except_table1989
- GCC_except_table2008
- GCC_except_table2070
- GCC_except_table395
- GCC_except_table398
- GCC_except_table437
- GCC_except_table477
- GCC_except_table529
- GCC_except_table533
- GCC_except_table548
- GCC_except_table561
- GCC_except_table633
- GCC_except_table641
- GCC_except_table643
- GCC_except_table732
- GCC_except_table808
- GCC_except_table849
- GCC_except_table854
- GCC_except_table870
- GCC_except_table873
- GCC_except_table955
- GCC_except_table956
- GCC_except_table959
- GCC_except_table960
- GCC_except_table963
- GCC_except_table964
- ___43-[SSRVTUITrainingServiceClient _connection]_block_invoke.10
- ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.26
- ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.28
- ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.31
- ___48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_2.27
- ___Block_byref_object_copy_.2041
- ___Block_byref_object_copy_.2270
- ___Block_byref_object_copy_.2435
- ___Block_byref_object_copy_.3115
- ___Block_byref_object_copy_.3699
- ___Block_byref_object_copy_.3854
- ___Block_byref_object_copy_.4014
- ___Block_byref_object_copy_.4803
- ___Block_byref_object_copy_.5164
- ___Block_byref_object_copy_.5297
- ___Block_byref_object_copy_.5510
- ___Block_byref_object_copy_.5702
- ___Block_byref_object_copy_.5906
- ___Block_byref_object_copy_.6714
- ___Block_byref_object_copy_.7161
- ___Block_byref_object_copy_.7275
- ___Block_byref_object_copy_.7501
- ___Block_byref_object_copy_.7847
- ___Block_byref_object_copy_.8659
- ___Block_byref_object_copy_.995
- ___Block_byref_object_dispose_.2042
- ___Block_byref_object_dispose_.2271
- ___Block_byref_object_dispose_.2436
- ___Block_byref_object_dispose_.3116
- ___Block_byref_object_dispose_.3700
- ___Block_byref_object_dispose_.3855
- ___Block_byref_object_dispose_.4015
- ___Block_byref_object_dispose_.4804
- ___Block_byref_object_dispose_.5165
- ___Block_byref_object_dispose_.5298
- ___Block_byref_object_dispose_.5511
- ___Block_byref_object_dispose_.5703
- ___Block_byref_object_dispose_.5907
- ___Block_byref_object_dispose_.6715
- ___Block_byref_object_dispose_.7162
- ___Block_byref_object_dispose_.7276
- ___Block_byref_object_dispose_.7502
- ___Block_byref_object_dispose_.7848
- ___Block_byref_object_dispose_.8660
- ___Block_byref_object_dispose_.996
- ___block_literal_global.1721
- ___block_literal_global.2049
- ___block_literal_global.30
- ___block_literal_global.3003
- ___block_literal_global.3875
- ___block_literal_global.3937
- ___block_literal_global.4466
- ___block_literal_global.4846
- ___block_literal_global.5057
- ___block_literal_global.5991
- ___block_literal_global.6193
- ___block_literal_global.6768
- ___block_literal_global.7285
- ___block_literal_global.7535
- ___block_literal_global.7724
- ___block_literal_global.7999
- ___block_literal_global.8188
- ___block_literal_global.8499
- ___block_literal_global.8961
- ___block_literal_global.9330
- _sharedInstance.onceToken.1720
- _sharedInstance.onceToken.3936
- _sharedInstance.onceToken.7998
- _sharedInstance.onceToken.8498
- _sharedManager.onceToken.7534
CStrings:
+ "setWithObject:"
+ "updateTrainingManagerViaXPCForDevice:trainingDeviceUUIDList:withCompletion:"
+ "v40@0:8Q16@\"NSArray\"24@?<v@?@\"NSError\">32"

```
