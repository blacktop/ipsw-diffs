## HomeKit

> `/System/Library/PrivateFrameworks/HomeKit.framework/Versions/A/HomeKit`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-1484.2.0.0.0
-  __TEXT.__text: 0x3ea798
-  __TEXT.__objc_methlist: 0x27cfc
-  __TEXT.__const: 0x65e8
-  __TEXT.__dlopen_cstrs: 0x359
-  __TEXT.__swift5_typeref: 0x1ee4
-  __TEXT.__cstring: 0x2ec7e
-  __TEXT.__constg_swiftt: 0x1bc8
-  __TEXT.__swift5_reflstr: 0x1145
-  __TEXT.__swift5_fieldmd: 0x13ec
-  __TEXT.__swift5_builtin: 0x8c
-  __TEXT.__swift5_assocty: 0x320
-  __TEXT.__swift5_capture: 0x8fc
+1490.2.0.0.0
+  __TEXT.__text: 0x3f3d58
+  __TEXT.__objc_methlist: 0x2801c
+  __TEXT.__const: 0x66f8
+  __TEXT.__dlopen_cstrs: 0x3bb
+  __TEXT.__swift5_typeref: 0x1fd4
+  __TEXT.__cstring: 0x2ea1b
+  __TEXT.__constg_swiftt: 0x1c60
+  __TEXT.__swift5_reflstr: 0x1154
+  __TEXT.__swift5_fieldmd: 0x143c
+  __TEXT.__swift5_builtin: 0xa0
+  __TEXT.__swift5_assocty: 0x350
+  __TEXT.__swift5_capture: 0x9a4
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_proto: 0x4b8
-  __TEXT.__swift5_types: 0x1b0
+  __TEXT.__swift5_proto: 0x4c0
+  __TEXT.__swift5_types: 0x1bc
   __TEXT.__swift_as_entry: 0x1e8
-  __TEXT.__swift_as_ret: 0x23c
-  __TEXT.__swift_as_cont: 0x44c
-  __TEXT.__oslogstring: 0x547ae
+  __TEXT.__swift_as_ret: 0x22c
+  __TEXT.__swift_as_cont: 0x434
+  __TEXT.__oslogstring: 0x55476
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__gcc_except_tab: 0x66c8
+  __TEXT.__gcc_except_tab: 0x67a0
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0xc3e0
-  __TEXT.__eh_frame: 0x7b40
+  __TEXT.__unwind_info: 0xc4f0
+  __TEXT.__eh_frame: 0x7a10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5868
-  __DATA_CONST.__objc_classlist: 0x1318
+  __DATA_CONST.__const: 0x5900
+  __DATA_CONST.__objc_classlist: 0x1338
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdda8
+  __DATA_CONST.__objc_selrefs: 0xdf08
   __DATA_CONST.__objc_protorefs: 0x110
-  __DATA_CONST.__objc_superrefs: 0xf80
+  __DATA_CONST.__objc_superrefs: 0xf90
   __DATA_CONST.__objc_arraydata: 0x13f0
-  __DATA_CONST.__got: 0x1dc0
-  __AUTH_CONST.__const: 0x9980
-  __AUTH_CONST.__cfstring: 0x2ac60
-  __AUTH_CONST.__objc_const: 0x47928
+  __DATA_CONST.__got: 0x1dd0
+  __AUTH_CONST.__const: 0x9cf8
+  __AUTH_CONST.__cfstring: 0x2af00
+  __AUTH_CONST.__objc_const: 0x47f48
   __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x1808
-  __AUTH.__objc_data: 0x8ca0
-  __AUTH.__data: 0x1708
-  __DATA.__objc_ivar: 0x2720
-  __DATA.__data: 0x5180
-  __DATA.__bss: 0x9300
+  __AUTH_CONST.__auth_got: 0x1818
+  __AUTH.__objc_data: 0x8e00
+  __AUTH.__data: 0x17b8
+  __DATA.__objc_ivar: 0x2768
+  __DATA.__data: 0x51d0
+  __DATA.__bss: 0x9460
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x36f0
   __DATA_DIRTY.__data: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17236
-  Symbols:   32065
-  CStrings:  12047
+  Functions: 17383
+  Symbols:   32273
+  CStrings:  12138
 
Symbols:
+ +[HMUserActionPredictionCompositeDataSource convertLegacyPredictionToLegacyScoreFormat:]
+ +[HMUserActionPredictionCompositeDataSource convertLegacyPredictionsToLegacyScoreFormat:]
+ +[HMUserActionPredictionCompositeDataSource logCategory]
+ +[HMUserActionPredictionCompositeDataSource mergePrimaryPrediction:withLegacyPrediction:]
+ +[HMUserActionPredictionCompositeDataSource mergePrimaryPredictions:withLegacyPredictions:]
+ +[HMUserActionPredictionCompositeDataSource predictionMatchingKeyForPrediction:]
+ +[HMUserActionPredictionIntelligentRoutingDataSource logCategory]
+ -[HMAccessory _shouldCreateDynamicAccessorySettingsAdapter]
+ -[HMAccessorySettingsAdapter addNumberSettingForKeyPath:value:minimumValue:maximumValue:stepValue:]
+ -[HMAccessorySettingsAdapter hasAccessorySettingForKeyPath:]
+ -[HMAccessorySetupManager notifyProxCardLaunching]
+ -[HMAccessorySetupManager notifyProxControlLaunched]
+ -[HMHome clearStagedDataForMediaGroupsController:]
+ -[HMMediaContentProfileAccessControl hash]
+ -[HMMediaGroupStagingManager _clearStagedData]
+ -[HMMediaGroupsController clearStagedData]
+ -[HMResidentDevice setSupportsHKSV3:]
+ -[HMResidentDevice supportsHKSV3]
+ -[HMUserActionPrediction initWithPredictionTargetUUID:predictionType:predictionScore:predictionReason:]
+ -[HMUserActionPrediction initWithPredictionTargetUUID:predictionType:predictionScore:predictionReason:legacyPredictionScore:modelHasSignificantData:mapIsValid:peripheralAvailable:microLocationModelCategory:]
+ -[HMUserActionPrediction initWithPredictionTargetUUID:targetServiceUUID:predictionType:predictionScore:predictionReason:]
+ -[HMUserActionPrediction initWithPredictionTargetUUID:targetServiceUUID:predictionType:predictionScore:predictionReason:legacyPredictionScore:modelHasSignificantData:mapIsValid:peripheralAvailable:microLocationModelCategory:]
+ -[HMUserActionPrediction initWithPredictionTargetUUID:targetServiceUUID:targetGroupUUID:targetGroupType:predictionType:predictionScore:predictionReason:]
+ -[HMUserActionPrediction initWithPredictionTargetUUID:targetServiceUUID:targetGroupUUID:targetGroupType:predictionType:predictionScore:predictionReason:legacyPredictionScore:modelHasSignificantData:mapIsValid:peripheralAvailable:microLocationModelCategory:]
+ -[HMUserActionPrediction initWithPredictionTargetUUID:targetServiceUUID:targetServiceGroupUUID:predictionType:predictionScore:predictionReason:legacyPredictionScore:modelHasSignificantData:mapIsValid:peripheralAvailable:microLocationModelCategory:]
+ -[HMUserActionPrediction legacyPredictionScore]
+ -[HMUserActionPrediction mapIsValid]
+ -[HMUserActionPrediction microLocationModelCategory]
+ -[HMUserActionPrediction modelHasSignificantData]
+ -[HMUserActionPrediction peripheralAvailable]
+ -[HMUserActionPrediction predictionReason]
+ -[HMUserActionPredictionCompositeDataSource .cxx_destruct]
+ -[HMUserActionPredictionCompositeDataSource fetchPredictionsFromBackendWithCompletion:]
+ -[HMUserActionPredictionCompositeDataSource fetchPredictionsFromCache]
+ -[HMUserActionPredictionCompositeDataSource initWithWorkQueue:cacheManager:]
+ -[HMUserActionPredictionCompositeDataSource lastMergedPredictions]
+ -[HMUserActionPredictionCompositeDataSource legacyDataSource]
+ -[HMUserActionPredictionCompositeDataSource predictions]
+ -[HMUserActionPredictionCompositeDataSource primaryDataSource]
+ -[HMUserActionPredictionCompositeDataSource setLastMergedPredictions:]
+ -[HMUserActionPredictionCompositeDataSource workQueue]
+ -[HMUserActionPredictionDuetPredictionValue hasMicroLocationModelCategory]
+ -[HMUserActionPredictionDuetPredictionValue hasPeripheralAvailable]
+ -[HMUserActionPredictionDuetPredictionValue microLocationModelCategory]
+ -[HMUserActionPredictionDuetPredictionValue peripheralAvailable]
+ -[HMUserActionPredictionDuetPredictionValue setHasMicroLocationModelCategory:]
+ -[HMUserActionPredictionDuetPredictionValue setHasPeripheralAvailable:]
+ -[HMUserActionPredictionDuetPredictionValue setMicroLocationModelCategory:]
+ -[HMUserActionPredictionDuetPredictionValue setPeripheralAvailable:]
+ -[HMUserActionPredictionIntelligentRoutingDataSource .cxx_destruct]
+ -[HMUserActionPredictionIntelligentRoutingDataSource fetchPredictionsFromBackendWithCompletion:]
+ -[HMUserActionPredictionIntelligentRoutingDataSource fetchPredictionsFromCache]
+ -[HMUserActionPredictionIntelligentRoutingDataSource initWithWorkQueue:cacheManager:]
+ -[HMUserActionPredictionIntelligentRoutingDataSource openCacheIfNeeded]
+ -[HMUserActionPredictionIntelligentRoutingDataSource predictions]
+ GCC_except_table10148
+ GCC_except_table10149
+ GCC_except_table10150
+ GCC_except_table10154
+ GCC_except_table10209
+ GCC_except_table10232
+ GCC_except_table10312
+ GCC_except_table10314
+ GCC_except_table10316
+ GCC_except_table10318
+ GCC_except_table10326
+ GCC_except_table10373
+ GCC_except_table10385
+ GCC_except_table10387
+ GCC_except_table10577
+ GCC_except_table10578
+ GCC_except_table10613
+ GCC_except_table10646
+ GCC_except_table10649
+ GCC_except_table10652
+ GCC_except_table10654
+ GCC_except_table10720
+ GCC_except_table10740
+ GCC_except_table10741
+ GCC_except_table10742
+ GCC_except_table10781
+ GCC_except_table10783
+ GCC_except_table10785
+ GCC_except_table10882
+ GCC_except_table10884
+ GCC_except_table10907
+ GCC_except_table10913
+ GCC_except_table10927
+ GCC_except_table10937
+ GCC_except_table10949
+ GCC_except_table10952
+ GCC_except_table10960
+ GCC_except_table10961
+ GCC_except_table10963
+ GCC_except_table10967
+ GCC_except_table10987
+ GCC_except_table10997
+ GCC_except_table11200
+ GCC_except_table11213
+ GCC_except_table11246
+ GCC_except_table11249
+ GCC_except_table11251
+ GCC_except_table11264
+ GCC_except_table11265
+ GCC_except_table11333
+ GCC_except_table11336
+ GCC_except_table11337
+ GCC_except_table11688
+ GCC_except_table11726
+ GCC_except_table11739
+ GCC_except_table12095
+ GCC_except_table12097
+ GCC_except_table12100
+ GCC_except_table12110
+ GCC_except_table12134
+ GCC_except_table12135
+ GCC_except_table12138
+ GCC_except_table12141
+ GCC_except_table12150
+ GCC_except_table12151
+ GCC_except_table12152
+ GCC_except_table12249
+ GCC_except_table12275
+ GCC_except_table12277
+ GCC_except_table12281
+ GCC_except_table12282
+ GCC_except_table12330
+ GCC_except_table12356
+ GCC_except_table12369
+ GCC_except_table12395
+ GCC_except_table12399
+ GCC_except_table12452
+ GCC_except_table12481
+ GCC_except_table12482
+ GCC_except_table12483
+ GCC_except_table12484
+ GCC_except_table12485
+ GCC_except_table12486
+ GCC_except_table12487
+ GCC_except_table12488
+ GCC_except_table12489
+ GCC_except_table12490
+ GCC_except_table12491
+ GCC_except_table12492
+ GCC_except_table12493
+ GCC_except_table12494
+ GCC_except_table12495
+ GCC_except_table12496
+ GCC_except_table12519
+ GCC_except_table12546
+ GCC_except_table12656
+ GCC_except_table12660
+ GCC_except_table12726
+ GCC_except_table12728
+ GCC_except_table12736
+ GCC_except_table12747
+ GCC_except_table12749
+ GCC_except_table12754
+ GCC_except_table12755
+ GCC_except_table12756
+ GCC_except_table12978
+ GCC_except_table13179
+ GCC_except_table13182
+ GCC_except_table13187
+ GCC_except_table13191
+ GCC_except_table13199
+ GCC_except_table13204
+ GCC_except_table13206
+ GCC_except_table13211
+ GCC_except_table13212
+ GCC_except_table13214
+ GCC_except_table13296
+ GCC_except_table13298
+ GCC_except_table1331
+ GCC_except_table13317
+ GCC_except_table13318
+ GCC_except_table13319
+ GCC_except_table13320
+ GCC_except_table13325
+ GCC_except_table1333
+ GCC_except_table13339
+ GCC_except_table13345
+ GCC_except_table13348
+ GCC_except_table13352
+ GCC_except_table1336
+ GCC_except_table1338
+ GCC_except_table1340
+ GCC_except_table13430
+ GCC_except_table13438
+ GCC_except_table13439
+ GCC_except_table13444
+ GCC_except_table13450
+ GCC_except_table13452
+ GCC_except_table13454
+ GCC_except_table13456
+ GCC_except_table13458
+ GCC_except_table13460
+ GCC_except_table13462
+ GCC_except_table13651
+ GCC_except_table13652
+ GCC_except_table13653
+ GCC_except_table13654
+ GCC_except_table13664
+ GCC_except_table13665
+ GCC_except_table13689
+ GCC_except_table13690
+ GCC_except_table13764
+ GCC_except_table13786
+ GCC_except_table13789
+ GCC_except_table13922
+ GCC_except_table14092
+ GCC_except_table14097
+ GCC_except_table14100
+ GCC_except_table14153
+ GCC_except_table14186
+ GCC_except_table14191
+ GCC_except_table14192
+ GCC_except_table14193
+ GCC_except_table14194
+ GCC_except_table14196
+ GCC_except_table14205
+ GCC_except_table14207
+ GCC_except_table14209
+ GCC_except_table14213
+ GCC_except_table14214
+ GCC_except_table14215
+ GCC_except_table14216
+ GCC_except_table14217
+ GCC_except_table14218
+ GCC_except_table14220
+ GCC_except_table14222
+ GCC_except_table14224
+ GCC_except_table14226
+ GCC_except_table14361
+ GCC_except_table14364
+ GCC_except_table14384
+ GCC_except_table14386
+ GCC_except_table14387
+ GCC_except_table1510
+ GCC_except_table1536
+ GCC_except_table1602
+ GCC_except_table1673
+ GCC_except_table1678
+ GCC_except_table1696
+ GCC_except_table1764
+ GCC_except_table1766
+ GCC_except_table1777
+ GCC_except_table1779
+ GCC_except_table1908
+ GCC_except_table1960
+ GCC_except_table1963
+ GCC_except_table2037
+ GCC_except_table2126
+ GCC_except_table2127
+ GCC_except_table2176
+ GCC_except_table2444
+ GCC_except_table2447
+ GCC_except_table2450
+ GCC_except_table2455
+ GCC_except_table2481
+ GCC_except_table2483
+ GCC_except_table2484
+ GCC_except_table2489
+ GCC_except_table2491
+ GCC_except_table3038
+ GCC_except_table3043
+ GCC_except_table3072
+ GCC_except_table3085
+ GCC_except_table3120
+ GCC_except_table3146
+ GCC_except_table3148
+ GCC_except_table3150
+ GCC_except_table3152
+ GCC_except_table3299
+ GCC_except_table3302
+ GCC_except_table3310
+ GCC_except_table3311
+ GCC_except_table3332
+ GCC_except_table3359
+ GCC_except_table3360
+ GCC_except_table3415
+ GCC_except_table3521
+ GCC_except_table3575
+ GCC_except_table3578
+ GCC_except_table3579
+ GCC_except_table3605
+ GCC_except_table3607
+ GCC_except_table3615
+ GCC_except_table3617
+ GCC_except_table3624
+ GCC_except_table3625
+ GCC_except_table3626
+ GCC_except_table3628
+ GCC_except_table3629
+ GCC_except_table3630
+ GCC_except_table3631
+ GCC_except_table3632
+ GCC_except_table3715
+ GCC_except_table3738
+ GCC_except_table3741
+ GCC_except_table3744
+ GCC_except_table3756
+ GCC_except_table3821
+ GCC_except_table3822
+ GCC_except_table3868
+ GCC_except_table3875
+ GCC_except_table3876
+ GCC_except_table3877
+ GCC_except_table3880
+ GCC_except_table3881
+ GCC_except_table3882
+ GCC_except_table3884
+ GCC_except_table3892
+ GCC_except_table3914
+ GCC_except_table3923
+ GCC_except_table3927
+ GCC_except_table3930
+ GCC_except_table3933
+ GCC_except_table3974
+ GCC_except_table3978
+ GCC_except_table3982
+ GCC_except_table3987
+ GCC_except_table3995
+ GCC_except_table3999
+ GCC_except_table4008
+ GCC_except_table4010
+ GCC_except_table4249
+ GCC_except_table4254
+ GCC_except_table4258
+ GCC_except_table4261
+ GCC_except_table4265
+ GCC_except_table4266
+ GCC_except_table4271
+ GCC_except_table4277
+ GCC_except_table4281
+ GCC_except_table4285
+ GCC_except_table4308
+ GCC_except_table4310
+ GCC_except_table4312
+ GCC_except_table4315
+ GCC_except_table4316
+ GCC_except_table4318
+ GCC_except_table4321
+ GCC_except_table4396
+ GCC_except_table4410
+ GCC_except_table4413
+ GCC_except_table4415
+ GCC_except_table4418
+ GCC_except_table4425
+ GCC_except_table4479
+ GCC_except_table4544
+ GCC_except_table4559
+ GCC_except_table4562
+ GCC_except_table4654
+ GCC_except_table4655
+ GCC_except_table4659
+ GCC_except_table4664
+ GCC_except_table4668
+ GCC_except_table4671
+ GCC_except_table4673
+ GCC_except_table4681
+ GCC_except_table4927
+ GCC_except_table4930
+ GCC_except_table4942
+ GCC_except_table5018
+ GCC_except_table5062
+ GCC_except_table5155
+ GCC_except_table5406
+ GCC_except_table5409
+ GCC_except_table5500
+ GCC_except_table5519
+ GCC_except_table5529
+ GCC_except_table5664
+ GCC_except_table5675
+ GCC_except_table5688
+ GCC_except_table5695
+ GCC_except_table5734
+ GCC_except_table5736
+ GCC_except_table5764
+ GCC_except_table5766
+ GCC_except_table5768
+ GCC_except_table5770
+ GCC_except_table5777
+ GCC_except_table5783
+ GCC_except_table5799
+ GCC_except_table5805
+ GCC_except_table5882
+ GCC_except_table5891
+ GCC_except_table5893
+ GCC_except_table5903
+ GCC_except_table5905
+ GCC_except_table5907
+ GCC_except_table5909
+ GCC_except_table5911
+ GCC_except_table5917
+ GCC_except_table5921
+ GCC_except_table5934
+ GCC_except_table5936
+ GCC_except_table5938
+ GCC_except_table5940
+ GCC_except_table5988
+ GCC_except_table6037
+ GCC_except_table6049
+ GCC_except_table6051
+ GCC_except_table6075
+ GCC_except_table6076
+ GCC_except_table6077
+ GCC_except_table6078
+ GCC_except_table6133
+ GCC_except_table6146
+ GCC_except_table6406
+ GCC_except_table6408
+ GCC_except_table6423
+ GCC_except_table6461
+ GCC_except_table6481
+ GCC_except_table6527
+ GCC_except_table6622
+ GCC_except_table6642
+ GCC_except_table6643
+ GCC_except_table6644
+ GCC_except_table6646
+ GCC_except_table6649
+ GCC_except_table6650
+ GCC_except_table6652
+ GCC_except_table6978
+ GCC_except_table6984
+ GCC_except_table6986
+ GCC_except_table6996
+ GCC_except_table6997
+ GCC_except_table7202
+ GCC_except_table7206
+ GCC_except_table7317
+ GCC_except_table7321
+ GCC_except_table7323
+ GCC_except_table7324
+ GCC_except_table7463
+ GCC_except_table7472
+ GCC_except_table7588
+ GCC_except_table7643
+ GCC_except_table7645
+ GCC_except_table7647
+ GCC_except_table7669
+ GCC_except_table7697
+ GCC_except_table7709
+ GCC_except_table7726
+ GCC_except_table7732
+ GCC_except_table7743
+ GCC_except_table7745
+ GCC_except_table7747
+ GCC_except_table7749
+ GCC_except_table7751
+ GCC_except_table7753
+ GCC_except_table7755
+ GCC_except_table7757
+ GCC_except_table7759
+ GCC_except_table7761
+ GCC_except_table7763
+ GCC_except_table7765
+ GCC_except_table7767
+ GCC_except_table7772
+ GCC_except_table7786
+ GCC_except_table7787
+ GCC_except_table7812
+ GCC_except_table7814
+ GCC_except_table7839
+ GCC_except_table7852
+ GCC_except_table7870
+ GCC_except_table8049
+ GCC_except_table8384
+ GCC_except_table8427
+ GCC_except_table8520
+ GCC_except_table8529
+ GCC_except_table8704
+ GCC_except_table8706
+ GCC_except_table8707
+ GCC_except_table8708
+ GCC_except_table8710
+ GCC_except_table8712
+ GCC_except_table8713
+ GCC_except_table8714
+ GCC_except_table8749
+ GCC_except_table8752
+ GCC_except_table8753
+ GCC_except_table8756
+ GCC_except_table8759
+ GCC_except_table8760
+ GCC_except_table8803
+ GCC_except_table8804
+ GCC_except_table8805
+ GCC_except_table8812
+ GCC_except_table8813
+ GCC_except_table8815
+ GCC_except_table8834
+ GCC_except_table8995
+ GCC_except_table9002
+ GCC_except_table9007
+ GCC_except_table9200
+ GCC_except_table9248
+ GCC_except_table9448
+ GCC_except_table9450
+ GCC_except_table9457
+ GCC_except_table9465
+ GCC_except_table9486
+ GCC_except_table9497
+ GCC_except_table9502
+ GCC_except_table9505
+ GCC_except_table9519
+ GCC_except_table9524
+ GCC_except_table9530
+ GCC_except_table9535
+ GCC_except_table9540
+ GCC_except_table9545
+ GCC_except_table9550
+ GCC_except_table9554
+ GCC_except_table9559
+ GCC_except_table9606
+ GCC_except_table9620
+ GCC_except_table9625
+ GCC_except_table9639
+ GCC_except_table9644
+ GCC_except_table9651
+ GCC_except_table9668
+ GCC_except_table9669
+ GCC_except_table9671
+ GCC_except_table9673
+ GCC_except_table9676
+ GCC_except_table9681
+ GCC_except_table9688
+ GCC_except_table9693
+ GCC_except_table9697
+ GCC_except_table9732
+ GCC_except_table9779
+ GCC_except_table9788
+ GCC_except_table9835
+ GCC_except_table9836
+ GCC_except_table9837
+ GCC_except_table9875
+ GCC_except_table9889
+ GCC_except_table9985
+ GCC_except_table9986
+ GCC_except_table9987
+ GCC_except_table9989
+ GCC_except_table9992
+ GCC_except_table9993
+ GCC_except_table9999
+ IntelligentRoutingLibraryCore.frameworkLibrary
+ OBJC_IVAR_$_HMResidentDevice._supportsHKSV3
+ OBJC_IVAR_$_HMUserActionPrediction._legacyPredictionScore
+ OBJC_IVAR_$_HMUserActionPrediction._mapIsValid
+ OBJC_IVAR_$_HMUserActionPrediction._microLocationModelCategory
+ OBJC_IVAR_$_HMUserActionPrediction._modelHasSignificantData
+ OBJC_IVAR_$_HMUserActionPrediction._peripheralAvailable
+ OBJC_IVAR_$_HMUserActionPrediction._predictionReason
+ OBJC_IVAR_$_HMUserActionPredictionCompositeDataSource._lastMergedPredictions
+ OBJC_IVAR_$_HMUserActionPredictionCompositeDataSource._legacyDataSource
+ OBJC_IVAR_$_HMUserActionPredictionCompositeDataSource._primaryDataSource
+ OBJC_IVAR_$_HMUserActionPredictionCompositeDataSource._workQueue
+ OBJC_IVAR_$_HMUserActionPredictionDuetPredictionValue._microLocationModelCategory
+ OBJC_IVAR_$_HMUserActionPredictionDuetPredictionValue._peripheralAvailable
+ OBJC_IVAR_$_HMUserActionPredictionIntelligentRoutingDataSource._cacheManager
+ OBJC_IVAR_$_HMUserActionPredictionIntelligentRoutingDataSource._lastFetchedPredictions
+ OBJC_IVAR_$_HMUserActionPredictionIntelligentRoutingDataSource._predictionCache
+ OBJC_IVAR_$_HMUserActionPredictionIntelligentRoutingDataSource._session
+ OBJC_IVAR_$_HMUserActionPredictionIntelligentRoutingDataSource._workQueue
+ _CLLocationCoordinate2DIsValid
+ _HMAccessorySetupManagerProxCardLaunchingMessage
+ _HMAccessorySetupManagerProxControlLaunchedMessage
+ _HMCameraProfileSessionErrorMessageKey
+ _HMCameraProfileSessionIDMessageKey
+ _HMCameraStreamAudioStreamSettingMessageKey
+ _HMCameraStreamSessionPreferencesMessageKey
+ _HMHomeUpdateLocationDataKey
+ _HMHomeUpdateLocationRequestMessage
+ _HMHomeUpdateLocationSourceKey
+ _HMMediaContentProfileAccessoryUUIDSet
+ _HMResidentDeviceSupportsHKSV3CodingKey
+ _HMUserActionPredictionIntelligentRoutingDataSourceCacheKey
+ _HMUserActionPredictionIntelligentRoutingDataSourceCacheName
+ _IntelligentRoutingLibrary
+ _OBJC_CLASS_$_HMUserActionPredictionCompositeDataSource
+ _OBJC_CLASS_$_HMUserActionPredictionIntelligentRoutingDataSource
+ _OBJC_CLASS_$__TtC7HomeKit33HMDynamicAccessorySettingsAdapter
+ _OBJC_METACLASS_$_HMUserActionPredictionCompositeDataSource
+ _OBJC_METACLASS_$_HMUserActionPredictionIntelligentRoutingDataSource
+ _OBJC_METACLASS_$__TtC7HomeKit33HMDynamicAccessorySettingsAdapter
+ __87-[HMUserActionPredictionCompositeDataSource fetchPredictionsFromBackendWithCompletion:]_block_invoke
+ __96-[HMUserActionPredictionIntelligentRoutingDataSource fetchPredictionsFromBackendWithCompletion:]_block_invoke
+ __DATA__TtC7HomeKit33HMDynamicAccessorySettingsAdapter
+ __DATA__TtCC7HomeKit33HMDynamicAccessorySettingsAdapter7Storage
+ __INSTANCE_METHODS__TtC7HomeKit33HMDynamicAccessorySettingsAdapter
+ __IVARS__TtC7HomeKit33HMDynamicAccessorySettingsAdapter
+ __IVARS__TtCC7HomeKit33HMDynamicAccessorySettingsAdapter7Storage
+ __METACLASS_DATA__TtC7HomeKit33HMDynamicAccessorySettingsAdapter
+ __METACLASS_DATA__TtCC7HomeKit33HMDynamicAccessorySettingsAdapter7Storage
+ __OBJC_$_CLASS_METHODS_HMAccessory(HomeKit|DynamicAccessorySettingsAdapter|SwiftExtensions|SiriEndpoint|Television|LightInternal|HMDoorbellChimeProfile|NetworkRouter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|Shortcuts|Camera|CHIP|NetworkConfiguration|Climate|Light|Media)
+ __OBJC_$_CLASS_METHODS_HMHome(HomeKit|HomeKit1|HomeKit2|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
+ __OBJC_$_CLASS_METHODS_HMUserActionPredictionCompositeDataSource
+ __OBJC_$_CLASS_METHODS_HMUserActionPredictionIntelligentRoutingDataSource
+ __OBJC_$_INSTANCE_METHODS_HMAccessory(HomeKit|DynamicAccessorySettingsAdapter|SwiftExtensions|SiriEndpoint|Television|LightInternal|HMDoorbellChimeProfile|NetworkRouter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|Shortcuts|Camera|CHIP|NetworkConfiguration|Climate|Light|Media)
+ __OBJC_$_INSTANCE_METHODS_HMHome(HomeKit|HomeKit1|HomeKit2|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
+ __OBJC_$_INSTANCE_METHODS_HMUserActionPredictionCompositeDataSource
+ __OBJC_$_INSTANCE_METHODS_HMUserActionPredictionIntelligentRoutingDataSource
+ __OBJC_$_INSTANCE_VARIABLES_HMUserActionPredictionCompositeDataSource
+ __OBJC_$_INSTANCE_VARIABLES_HMUserActionPredictionIntelligentRoutingDataSource
+ __OBJC_$_PROP_LIST_HMUserActionPredictionCompositeDataSource
+ __OBJC_$_PROP_LIST_HMUserActionPredictionIntelligentRoutingDataSource
+ __OBJC_CLASS_PROTOCOLS_$_HMHome(HomeKit|HomeKit1|HomeKit2|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
+ __OBJC_CLASS_PROTOCOLS_$_HMUserActionPredictionCompositeDataSource
+ __OBJC_CLASS_PROTOCOLS_$_HMUserActionPredictionIntelligentRoutingDataSource
+ __OBJC_CLASS_RO_$_HMUserActionPredictionCompositeDataSource
+ __OBJC_CLASS_RO_$_HMUserActionPredictionIntelligentRoutingDataSource
+ __OBJC_METACLASS_RO_$_HMUserActionPredictionCompositeDataSource
+ __OBJC_METACLASS_RO_$_HMUserActionPredictionIntelligentRoutingDataSource
+ ___56+[HMUserActionPredictionCompositeDataSource logCategory]_block_invoke
+ ___65+[HMUserActionPredictionIntelligentRoutingDataSource logCategory]_block_invoke
+ ___87-[HMUserActionPredictionCompositeDataSource fetchPredictionsFromBackendWithCompletion:]_block_invoke
+ ___89+[HMUserActionPredictionCompositeDataSource convertLegacyPredictionsToLegacyScoreFormat:]_block_invoke
+ ___96-[HMUserActionPredictionIntelligentRoutingDataSource fetchPredictionsFromBackendWithCompletion:]_block_invoke
+ ___96-[HMUserActionPredictionIntelligentRoutingDataSource fetchPredictionsFromBackendWithCompletion:]_block_invoke_2
+ ___IntelligentRoutingLibraryCore_block_invoke
+ ___block_descriptor_40_e94_"HMUserActionPredictionDuetPredictionValue"16?0"HMUserActionPredictionDuetPredictionValue"8l
+ ___block_descriptor_48_e8_32s40bs_e31_v24?0"IRContext"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e69_"HMUserActionPredictionDuetPredictionValue"16?0"IRHomeSuggestion"8l
+ ___block_descriptor_56_e8_32s40s48r_e17_v16?0"NSArray"8l
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0l
+ ___copy_helper_block_e8_32s40b48r56r
+ ___getIRConfigurationClass_block_invoke
+ ___getIRContextMetadataIsMicroLocationMapValidKeySymbolLoc_block_invoke
+ ___getIRContextMetadataIsMicroLocationPredictionValidKeySymbolLoc_block_invoke
+ ___getIRContextMetadataIsPeripheralAvailableKeySymbolLoc_block_invoke
+ ___getIRContextMetadataMicroLocationModelCategoryKeySymbolLoc_block_invoke
+ ___getIRServiceTokenClass_block_invoke
+ ___getIRSessionClass_block_invoke
+ _associated conformance So6HMHomeC7HomeKitE14LocationSourceOSHACSQ
+ _audit_stringIntelligentRouting
+ _getIRConfigurationClass
+ _getIRServiceTokenClass
+ _objc_msgSend$_clearStagedData
+ _objc_msgSend$_shouldCreateDynamicAccessorySettingsAdapter
+ _objc_msgSend$addNumberSettingForKeyPath:value:minimumValue:maximumValue:stepValue:
+ _objc_msgSend$clearStagedDataForMediaGroupsController:
+ _objc_msgSend$convertLegacyPredictionToLegacyScoreFormat:
+ _objc_msgSend$convertLegacyPredictionsToLegacyScoreFormat:
+ _objc_msgSend$coordinate
+ _objc_msgSend$createDynamicAccessoryAdapterWithDataSource:controller:
+ _objc_msgSend$fetchAccessorySettingsWithHomeIdentifier:accessoryIdentifier:keyPaths:completionHandler:
+ _objc_msgSend$hasAccessorySettingForKeyPath:
+ _objc_msgSend$hasLegacyScore
+ _objc_msgSend$hasMapIsValid
+ _objc_msgSend$hasMicroLocationModelCategory
+ _objc_msgSend$hasModelHasSignificantData
+ _objc_msgSend$hasPeripheralAvailable
+ _objc_msgSend$hasReason
+ _objc_msgSend$hasTargetAccessoryServiceIdentifier
+ _objc_msgSend$homeSuggestions
+ _objc_msgSend$initWithFloat:
+ _objc_msgSend$initWithPredictionTargetUUID:predictionType:predictionScore:predictionReason:legacyPredictionScore:modelHasSignificantData:mapIsValid:peripheralAvailable:microLocationModelCategory:
+ _objc_msgSend$initWithPredictionTargetUUID:targetServiceUUID:predictionType:predictionScore:predictionReason:legacyPredictionScore:modelHasSignificantData:mapIsValid:peripheralAvailable:microLocationModelCategory:
+ _objc_msgSend$initWithPredictionTargetUUID:targetServiceUUID:targetGroupUUID:targetGroupType:predictionType:predictionScore:predictionReason:
+ _objc_msgSend$initWithPredictionTargetUUID:targetServiceUUID:targetGroupUUID:targetGroupType:predictionType:predictionScore:predictionReason:legacyPredictionScore:modelHasSignificantData:mapIsValid:peripheralAvailable:microLocationModelCategory:
+ _objc_msgSend$initWithServiceToken:
+ _objc_msgSend$initWithWorkQueue:cacheManager:
+ _objc_msgSend$lastMergedPredictions
+ _objc_msgSend$legacyDataSource
+ _objc_msgSend$legacyPredictionScore
+ _objc_msgSend$legacyScore
+ _objc_msgSend$mapIsValid
+ _objc_msgSend$mergePrimaryPrediction:withLegacyPrediction:
+ _objc_msgSend$mergePrimaryPredictions:withLegacyPredictions:
+ _objc_msgSend$microLocationModelCategory
+ _objc_msgSend$modelHasSignificantData
+ _objc_msgSend$peripheralAvailable
+ _objc_msgSend$predictionMatchingKeyForPrediction:
+ _objc_msgSend$predictionReason
+ _objc_msgSend$primaryDataSource
+ _objc_msgSend$requestCurrentContextWithReply:
+ _objc_msgSend$residentDevice:didUpdateSupportsHKSV3:
+ _objc_msgSend$runWithConfiguration:
+ _objc_msgSend$serviceTokenForServiceIdentifier:
+ _objc_msgSend$setLastMergedPredictions:
+ _objc_msgSend$setLegacyScore:
+ _objc_msgSend$setMapIsValid:
+ _objc_msgSend$setMicroLocationModelCategory:
+ _objc_msgSend$setModelHasSignificantData:
+ _objc_msgSend$setPeripheralAvailable:
+ _objc_msgSend$suggestionReason
+ _symbolic SDySSSaySo8NSNumberCGG
+ _symbolic SS_SaySo8NSNumberCGt
+ _symbolic SaySo18HMImmutableSettingCG
+ _symbolic So26HMAccessorySettingsAdapterC
+ _symbolic So7NSErrorCSgIeyBy_
+ _symbolic So8NSNumberCSg
+ _symbolic _____ 7HomeKit33HMDynamicAccessorySettingsAdapterC
+ _symbolic _____ 7HomeKit33HMDynamicAccessorySettingsAdapterC7StorageC
+ _symbolic _____ So26SettingsAdapterSettingTypeV
+ _symbolic _____ So6HMHomeC7HomeKitE14LocationSourceO
+ _symbolic _____XDXMT 7HomeKit33HMDynamicAccessorySettingsAdapterC
+ _symbolic ______pSgIegg_Sg s5ErrorP
+ _symbolic ______pSgIeghg_ s5ErrorP
+ _symbolic _____ySSSaySo8NSNumberCGG s18_DictionaryStorageC
+ _symbolic _____ySS_SaySo8NSNumberCGtG s23_ContiguousArrayStorageC
+ getIRConfigurationClass.softClass
+ getIRContextMetadataIsMicroLocationMapValidKeySymbolLoc.ptr
+ getIRContextMetadataIsMicroLocationPredictionValidKeySymbolLoc.ptr
+ getIRContextMetadataIsPeripheralAvailableKeySymbolLoc.ptr
+ getIRContextMetadataMicroLocationModelCategoryKeySymbolLoc.ptr
+ getIRServiceTokenClass.softClass
+ getIRSessionClass.softClass
+ logCategory._hmf_once_t110
+ logCategory._hmf_once_t69
+ logCategory._hmf_once_v111
+ logCategory._hmf_once_v70
- -[HMUserActionPrediction initWithPredictionTargetUUID:targetServiceUUID:targetGroupUUID:targetGroupType:predictionType:predictionScore:]
- GCC_except_table10116
- GCC_except_table10117
- GCC_except_table10118
- GCC_except_table10122
- GCC_except_table10177
- GCC_except_table10200
- GCC_except_table10280
- GCC_except_table10282
- GCC_except_table10284
- GCC_except_table10286
- GCC_except_table10294
- GCC_except_table10341
- GCC_except_table10353
- GCC_except_table10355
- GCC_except_table10545
- GCC_except_table10546
- GCC_except_table10581
- GCC_except_table10614
- GCC_except_table10617
- GCC_except_table10620
- GCC_except_table10622
- GCC_except_table10688
- GCC_except_table10708
- GCC_except_table10709
- GCC_except_table10710
- GCC_except_table10749
- GCC_except_table10751
- GCC_except_table10753
- GCC_except_table10818
- GCC_except_table10852
- GCC_except_table10856
- GCC_except_table10873
- GCC_except_table10875
- GCC_except_table10881
- GCC_except_table10885
- GCC_except_table10895
- GCC_except_table10899
- GCC_except_table10928
- GCC_except_table10929
- GCC_except_table10933
- GCC_except_table10935
- GCC_except_table10955
- GCC_except_table11168
- GCC_except_table11181
- GCC_except_table11214
- GCC_except_table11217
- GCC_except_table11219
- GCC_except_table11232
- GCC_except_table11233
- GCC_except_table11301
- GCC_except_table11304
- GCC_except_table11305
- GCC_except_table11652
- GCC_except_table11690
- GCC_except_table11703
- GCC_except_table12059
- GCC_except_table12061
- GCC_except_table12063
- GCC_except_table12064
- GCC_except_table12074
- GCC_except_table12098
- GCC_except_table12102
- GCC_except_table12105
- GCC_except_table12114
- GCC_except_table12115
- GCC_except_table12116
- GCC_except_table12213
- GCC_except_table12239
- GCC_except_table12241
- GCC_except_table12245
- GCC_except_table12246
- GCC_except_table12294
- GCC_except_table12320
- GCC_except_table12333
- GCC_except_table12359
- GCC_except_table12363
- GCC_except_table12412
- GCC_except_table12413
- GCC_except_table12414
- GCC_except_table12415
- GCC_except_table12416
- GCC_except_table12417
- GCC_except_table12418
- GCC_except_table12419
- GCC_except_table12420
- GCC_except_table12421
- GCC_except_table12422
- GCC_except_table12423
- GCC_except_table12424
- GCC_except_table12425
- GCC_except_table12426
- GCC_except_table12427
- GCC_except_table12477
- GCC_except_table12587
- GCC_except_table12588
- GCC_except_table12591
- GCC_except_table12659
- GCC_except_table12667
- GCC_except_table12678
- GCC_except_table12680
- GCC_except_table12685
- GCC_except_table12686
- GCC_except_table12687
- GCC_except_table12909
- GCC_except_table13110
- GCC_except_table13113
- GCC_except_table13118
- GCC_except_table13122
- GCC_except_table13130
- GCC_except_table13135
- GCC_except_table13137
- GCC_except_table13142
- GCC_except_table13143
- GCC_except_table13145
- GCC_except_table13227
- GCC_except_table13229
- GCC_except_table13248
- GCC_except_table13249
- GCC_except_table13250
- GCC_except_table13251
- GCC_except_table13256
- GCC_except_table13270
- GCC_except_table13276
- GCC_except_table13279
- GCC_except_table13283
- GCC_except_table13361
- GCC_except_table13369
- GCC_except_table13370
- GCC_except_table13375
- GCC_except_table13381
- GCC_except_table13383
- GCC_except_table13385
- GCC_except_table13387
- GCC_except_table13389
- GCC_except_table13391
- GCC_except_table13393
- GCC_except_table1346
- GCC_except_table1349
- GCC_except_table1351
- GCC_except_table13526
- GCC_except_table1353
- GCC_except_table1357
- GCC_except_table13582
- GCC_except_table13583
- GCC_except_table13584
- GCC_except_table13585
- GCC_except_table13596
- GCC_except_table13620
- GCC_except_table13621
- GCC_except_table13695
- GCC_except_table13717
- GCC_except_table13720
- GCC_except_table13853
- GCC_except_table14023
- GCC_except_table14028
- GCC_except_table14031
- GCC_except_table14084
- GCC_except_table14117
- GCC_except_table14122
- GCC_except_table14123
- GCC_except_table14124
- GCC_except_table14125
- GCC_except_table14127
- GCC_except_table14136
- GCC_except_table14138
- GCC_except_table14140
- GCC_except_table14143
- GCC_except_table14144
- GCC_except_table14145
- GCC_except_table14146
- GCC_except_table14147
- GCC_except_table14148
- GCC_except_table14150
- GCC_except_table14152
- GCC_except_table14154
- GCC_except_table14156
- GCC_except_table14281
- GCC_except_table14284
- GCC_except_table14304
- GCC_except_table14306
- GCC_except_table14307
- GCC_except_table1523
- GCC_except_table1549
- GCC_except_table1615
- GCC_except_table1682
- GCC_except_table1687
- GCC_except_table1705
- GCC_except_table1773
- GCC_except_table1775
- GCC_except_table1786
- GCC_except_table1788
- GCC_except_table1917
- GCC_except_table1969
- GCC_except_table1972
- GCC_except_table2046
- GCC_except_table2135
- GCC_except_table2136
- GCC_except_table2185
- GCC_except_table2453
- GCC_except_table2456
- GCC_except_table2464
- GCC_except_table2477
- GCC_except_table2493
- GCC_except_table2498
- GCC_except_table2499
- GCC_except_table2500
- GCC_except_table2501
- GCC_except_table3035
- GCC_except_table3040
- GCC_except_table3066
- GCC_except_table3082
- GCC_except_table3114
- GCC_except_table3143
- GCC_except_table3145
- GCC_except_table3147
- GCC_except_table3149
- GCC_except_table3307
- GCC_except_table3334
- GCC_except_table3335
- GCC_except_table3393
- GCC_except_table3395
- GCC_except_table3398
- GCC_except_table3399
- GCC_except_table3427
- GCC_except_table3435
- GCC_except_table3437
- GCC_except_table3444
- GCC_except_table3445
- GCC_except_table3446
- GCC_except_table3448
- GCC_except_table3449
- GCC_except_table3450
- GCC_except_table3451
- GCC_except_table3452
- GCC_except_table3535
- GCC_except_table3558
- GCC_except_table3561
- GCC_except_table3564
- GCC_except_table3567
- GCC_except_table3570
- GCC_except_table3576
- GCC_except_table3641
- GCC_except_table3642
- GCC_except_table3688
- GCC_except_table3695
- GCC_except_table3696
- GCC_except_table3697
- GCC_except_table3700
- GCC_except_table3701
- GCC_except_table3702
- GCC_except_table3704
- GCC_except_table3712
- GCC_except_table3734
- GCC_except_table3743
- GCC_except_table3794
- GCC_except_table3798
- GCC_except_table3802
- GCC_except_table3807
- GCC_except_table3815
- GCC_except_table3819
- GCC_except_table3828
- GCC_except_table3830
- GCC_except_table4084
- GCC_except_table4091
- GCC_except_table4096
- GCC_except_table4291
- GCC_except_table4339
- GCC_except_table4539
- GCC_except_table4541
- GCC_except_table4548
- GCC_except_table4556
- GCC_except_table4577
- GCC_except_table4588
- GCC_except_table4593
- GCC_except_table4596
- GCC_except_table4610
- GCC_except_table4615
- GCC_except_table4621
- GCC_except_table4626
- GCC_except_table4631
- GCC_except_table4636
- GCC_except_table4641
- GCC_except_table4645
- GCC_except_table4650
- GCC_except_table4697
- GCC_except_table4701
- GCC_except_table4711
- GCC_except_table4716
- GCC_except_table4730
- GCC_except_table4735
- GCC_except_table4742
- GCC_except_table4759
- GCC_except_table4760
- GCC_except_table4762
- GCC_except_table4764
- GCC_except_table4767
- GCC_except_table4772
- GCC_except_table4779
- GCC_except_table4784
- GCC_except_table4788
- GCC_except_table4824
- GCC_except_table4871
- GCC_except_table4882
- GCC_except_table4919
- GCC_except_table4921
- GCC_except_table5038
- GCC_except_table5043
- GCC_except_table5047
- GCC_except_table5050
- GCC_except_table5054
- GCC_except_table5055
- GCC_except_table5058
- GCC_except_table5064
- GCC_except_table5068
- GCC_except_table5072
- GCC_except_table5095
- GCC_except_table5097
- GCC_except_table5099
- GCC_except_table5102
- GCC_except_table5103
- GCC_except_table5105
- GCC_except_table5108
- GCC_except_table5183
- GCC_except_table5197
- GCC_except_table5200
- GCC_except_table5202
- GCC_except_table5205
- GCC_except_table5212
- GCC_except_table5266
- GCC_except_table5331
- GCC_except_table5346
- GCC_except_table5349
- GCC_except_table5441
- GCC_except_table5442
- GCC_except_table5445
- GCC_except_table5450
- GCC_except_table5454
- GCC_except_table5457
- GCC_except_table5459
- GCC_except_table5467
- GCC_except_table5683
- GCC_except_table5693
- GCC_except_table5868
- GCC_except_table5871
- GCC_except_table5883
- GCC_except_table6003
- GCC_except_table6096
- GCC_except_table6351
- GCC_except_table6354
- GCC_except_table6444
- GCC_except_table6473
- GCC_except_table6608
- GCC_except_table6617
- GCC_except_table6630
- GCC_except_table6637
- GCC_except_table6676
- GCC_except_table6678
- GCC_except_table6706
- GCC_except_table6708
- GCC_except_table6710
- GCC_except_table6712
- GCC_except_table6719
- GCC_except_table6725
- GCC_except_table6731
- GCC_except_table6741
- GCC_except_table6747
- GCC_except_table6824
- GCC_except_table6833
- GCC_except_table6835
- GCC_except_table6845
- GCC_except_table6847
- GCC_except_table6849
- GCC_except_table6851
- GCC_except_table6853
- GCC_except_table6859
- GCC_except_table6863
- GCC_except_table6876
- GCC_except_table6878
- GCC_except_table6880
- GCC_except_table6882
- GCC_except_table6901
- GCC_except_table6930
- GCC_except_table6979
- GCC_except_table6991
- GCC_except_table6993
- GCC_except_table7017
- GCC_except_table7018
- GCC_except_table7019
- GCC_except_table7020
- GCC_except_table7075
- GCC_except_table7088
- GCC_except_table7348
- GCC_except_table7350
- GCC_except_table7378
- GCC_except_table7380
- GCC_except_table7398
- GCC_except_table7444
- GCC_except_table7539
- GCC_except_table7559
- GCC_except_table7560
- GCC_except_table7561
- GCC_except_table7563
- GCC_except_table7566
- GCC_except_table7567
- GCC_except_table7569
- GCC_except_table7895
- GCC_except_table7901
- GCC_except_table7903
- GCC_except_table7913
- GCC_except_table7914
- GCC_except_table8117
- GCC_except_table8121
- GCC_except_table8219
- GCC_except_table8223
- GCC_except_table8225
- GCC_except_table8226
- GCC_except_table8365
- GCC_except_table8374
- GCC_except_table8490
- GCC_except_table8545
- GCC_except_table8547
- GCC_except_table8549
- GCC_except_table8571
- GCC_except_table8600
- GCC_except_table8612
- GCC_except_table8629
- GCC_except_table8635
- GCC_except_table8646
- GCC_except_table8648
- GCC_except_table8650
- GCC_except_table8652
- GCC_except_table8654
- GCC_except_table8656
- GCC_except_table8658
- GCC_except_table8660
- GCC_except_table8662
- GCC_except_table8664
- GCC_except_table8666
- GCC_except_table8668
- GCC_except_table8670
- GCC_except_table8675
- GCC_except_table8689
- GCC_except_table8690
- GCC_except_table8715
- GCC_except_table8717
- GCC_except_table8742
- GCC_except_table8755
- GCC_except_table8773
- GCC_except_table8952
- GCC_except_table9287
- GCC_except_table9330
- GCC_except_table9423
- GCC_except_table9432
- GCC_except_table9607
- GCC_except_table9609
- GCC_except_table9611
- GCC_except_table9613
- GCC_except_table9615
- GCC_except_table9616
- GCC_except_table9617
- GCC_except_table9652
- GCC_except_table9655
- GCC_except_table9656
- GCC_except_table9659
- GCC_except_table9662
- GCC_except_table9663
- GCC_except_table9706
- GCC_except_table9707
- GCC_except_table9708
- GCC_except_table9715
- GCC_except_table9716
- GCC_except_table9718
- GCC_except_table9737
- GCC_except_table9806
- GCC_except_table9807
- GCC_except_table9808
- GCC_except_table9846
- GCC_except_table9860
- GCC_except_table9928
- GCC_except_table9956
- GCC_except_table9958
- GCC_except_table9960
- GCC_except_table9963
- GCC_except_table9964
- GCC_except_table9969
- __OBJC_$_CLASS_METHODS_HMAccessory(HomeKit|SwiftExtensions|SiriEndpoint|Television|LightInternal|HMDoorbellChimeProfile|NetworkRouter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|Shortcuts|Camera|CHIP|NetworkConfiguration|Climate|Light|Media)
- __OBJC_$_CLASS_METHODS_HMHome(HomeKit|HomeKit1|SwiftExtensions|HomeKit2|AccessCode|WalletInternal|Wallet|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- __OBJC_$_INSTANCE_METHODS_HMAccessory(HomeKit|SwiftExtensions|SiriEndpoint|Television|LightInternal|HMDoorbellChimeProfile|NetworkRouter|PendingConfiguration|Private|CUPeerIdentifier|Diagnostics|Shortcuts|Camera|CHIP|NetworkConfiguration|Climate|Light|Media)
- __OBJC_$_INSTANCE_METHODS_HMHome(HomeKit|HomeKit1|SwiftExtensions|HomeKit2|AccessCode|WalletInternal|Wallet|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- __OBJC_CLASS_PROTOCOLS_$_HMHome(HomeKit|HomeKit1|SwiftExtensions|HomeKit2|AccessCode|WalletInternal|Wallet|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- _associated conformance 7HomeKit18SummarizationErrorOSHAASQ
- _objc_msgSend$initWithPredictionTargetUUID:predictionType:predictionScore:
- _objc_msgSend$initWithPredictionTargetUUID:targetServiceUUID:predictionType:predictionScore:
- _objc_msgSend$initWithPredictionTargetUUID:targetServiceUUID:targetGroupUUID:targetGroupType:predictionType:predictionScore:
- _symbolic _____ 7HomeKit18SummarizationErrorO
- _symbolic ______pSg 7HomeKit22LanguageModelExecutingP
- _symbolic _____ySbG 15Synchronization5MutexVAARi_zrlE
- logCategory._hmf_once_t108
- logCategory._hmf_once_t67
- logCategory._hmf_once_t84
- logCategory._hmf_once_v109
- logCategory._hmf_once_v68
- logCategory._hmf_once_v85
CStrings:
+ "%@-%@-%u"
+ ", legacyPredictionScore: %@"
+ ", mapIsValid: %@"
+ ", microLocationModelCategory: %@"
+ ", modelHasSignificantData: %@"
+ ", peripheralAvailable: %@"
+ ", predictionReason: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uYWFOy/Sources/HomeKit/Sources/HomeKit/Accessory/HMAccessory.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uYWFOy/Sources/HomeKit/Sources/HomeKit/Camera/Source/Snapshot/HMCameraSnapshotControl.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uYWFOy/Sources/HomeKit/Sources/HomeKit/ClientConnection/HMClientConnection.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uYWFOy/Sources/HomeKit/Sources/HomeKit/DeviceSetup/HMDeviceSetupSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uYWFOy/Sources/HomeKit/Sources/HomeKit/Home/HMHome.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uYWFOy/Sources/HomeKit/Sources/HomeKit/Vendor/HMHomeManager+Vendor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.uYWFOy/Sources/HomeKit/Sources/HomeKit/Widgets/HMWidgetManager.m"
+ "/System/Library/PrivateFrameworks/IntelligentRouting.framework/Contents/MacOS/IntelligentRouting"
+ "<Merge> Notifying client of updated supportsHKSV3 value: %@"
+ "<Merge> Updating supportsHKSV3 from %@ to %@"
+ "@\"HMUserActionPredictionDuetPredictionValue\"16@?0@\"HMUserActionPredictionDuetPredictionValue\"8"
+ "@\"HMUserActionPredictionDuetPredictionValue\"16@?0@\"IRHomeSuggestion\"8"
+ "Accessory.Settings.DynamicAdapter"
+ "Dynamic settings adapter built settings tree, notifying delegate."
+ "Dynamic settings adapter cannot update unmanaged key path: %{public}s"
+ "Dynamic settings adapter did update for settings %{public}s"
+ "Dynamic settings adapter has no settings; nothing to subscribe to."
+ "Dynamic settings adapter has no usable constraints for key path: %{public}s"
+ "Dynamic settings adapter ignoring updateSettingsReflected: %{bool}d"
+ "Dynamic settings adapter initial fetch failed: %@"
+ "Dynamic settings adapter only supports accessory containers"
+ "Dynamic settings adapter only supports accessory containers, got: %ld"
+ "Dynamic settings adapter received empty settings array."
+ "Dynamic settings adapter received unmanaged key path: %{public}s"
+ "Dynamic settings adapter subscribing to %ld key path(s) for accessory: %{public}s"
+ "Dynamic settings adapter updating key path: %{public}s"
+ "Expected a boolean setting for key path: %{public}s"
+ "Expected a constrained number setting for key path: %{public}s"
+ "Failed to clear staged data due to no data source"
+ "Failed to create setting node for key path: %{public}s"
+ "Failed to subscribe to dynamic settings: %@"
+ "Fetched %@ predictions from IntelligentRouting: %@"
+ "Fetching predictions from backend for both primary and legacy data sources"
+ "Fetching predictions from cache for both primary and legacy data sources"
+ "HM.updateHomeLocation"
+ "HM.updateHomeLocation.data"
+ "HM.updateHomeLocation.source"
+ "HMASM.m.proxCardLaunching"
+ "HMASM.m.proxControlLaunched"
+ "HMResidentDeviceSupportsHKSV3CodingKey"
+ "HMUserActionPredictionIntelligentRoutingDataSourceCacheKey"
+ "HMUserActionPredictionIntelligentRoutingDataSourceCacheName"
+ "HomeKit.HMDynamicAccessorySettingsAdapter"
+ "IRConfiguration"
+ "IRContextMetadataIsMicroLocationMapValidKey"
+ "IRContextMetadataIsMicroLocationPredictionValidKey"
+ "IRContextMetadataIsPeripheralAvailableKey"
+ "IRContextMetadataMicroLocationModelCategoryKey"
+ "IRHomeSuggestions"
+ "IRHomeSuggestionsCompositeDataSource"
+ "IRServiceToken"
+ "IRSession"
+ "IntelligentRouting cannot be soft linked on current OS"
+ "Key path is not managed by this adapter"
+ "Legacy data source returned %@ predictions"
+ "Loaded %@ predictions from cache"
+ "Merged predictions: %@ total"
+ "No prediction data found in cache (%@) for key: %@"
+ "Primary data source returned %@ predictions"
+ "Returning %@ predictions"
+ "Running IRSession with token: %@"
+ "Skipping prediction (%@) of unknown type from IntelligentRouting"
+ "Successfully subscribed to dynamic settings."
+ "Unable to find or create group for key path: %@"
+ "Unable to load cached predictions from prediction store data."
+ "Unsupported setting kind"
+ "UserActionPredictionCompositeDataSource"
+ "UserActionPredictionIntelligentRoutingDataSource"
+ "[%{public}@] <Merge> Notifying client of updated supportsHKSV3 value: %@"
+ "[%{public}@] <Merge> Updating supportsHKSV3 from %@ to %@"
+ "[%{public}@] Failed to clear staged data due to no data source"
+ "[%{public}@] Fetched %@ predictions from IntelligentRouting: %@"
+ "[%{public}@] Fetching predictions from backend for both primary and legacy data sources"
+ "[%{public}@] Fetching predictions from cache for both primary and legacy data sources"
+ "[%{public}@] IntelligentRouting cannot be soft linked on current OS"
+ "[%{public}@] Legacy data source returned %@ predictions"
+ "[%{public}@] Loaded %@ predictions from cache"
+ "[%{public}@] Merged predictions: %@ total"
+ "[%{public}@] No prediction data found in cache (%@) for key: %@"
+ "[%{public}@] Primary data source returned %@ predictions"
+ "[%{public}@] Returning %@ predictions"
+ "[%{public}@] Running IRSession with token: %@"
+ "[%{public}@] Skipping prediction (%@) of unknown type from IntelligentRouting"
+ "[%{public}@] Unable to find or create group for key path: %@"
+ "[%{public}@] Unable to load cached predictions from prediction store data."
+ "[%{public}@] requestCurrentContextWithReply returned with error: %@"
+ "completion != nil"
+ "importCameraRecording(fileURL:zoneName:clipUUIDSuffix:startDate:)"
+ "init(homeIdentifier:dataSource:controller:work:settingsContainer:containerIdentifier:containerType:settingsControl:context:)"
+ "microLocationModelCategory"
+ "nil"
+ "peripheralAvailable"
+ "requestCurrentContextWithReply returned with error: %@"
+ "softlink:o:path:/System/Library/PrivateFrameworks/IntelligentRouting.framework/IntelligentRouting"
+ "updateLocation(_:source:)"
+ "updatePersonalizedActivityEnabled rejected: caller is not the target user"
+ "updateReduceNotificationsEnabled rejected: caller is not the target user"
+ "v24@?0@\"IRContext\"8@\"NSError\"16"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/HomeKit/Accessory/HMAccessory.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/HomeKit/Camera/Source/Snapshot/HMCameraSnapshotControl.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/HomeKit/ClientConnection/HMClientConnection.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/HomeKit/DeviceSetup/HMDeviceSetupSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/HomeKit/Home/HMHome.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/HomeKit/Vendor/HMHomeManager+Vendor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Rtwm5p/Sources/HomeKit/Sources/HomeKit/Widgets/HMWidgetManager.m"
- "1B"
- "FoundationModels.LanguageModelSession.GenerationError"
- "Primary executor failed (instruction prefix unavailable); downgrading to fallback prompt: error=%@"
- "You are a HomeKit notification summarizer. Summarize events accurately without adding any information not present in the input.\n\n## Optimization Rules\n\n### Event Filtering\n- Drop \"Name is leaving...\" events entirely\n- \"Name is arriving...\" → output \"Name arrived.\" (always keep as separate sentence)\n- Drop \"because someone arrived home\" or similar reason clauses\n\n### Activity Descriptions\n- Keep activity descriptions exactly as they appear in the input\n- Do NOT replace \"Someone\" with a person's name\n- Do NOT split or modify compound activity sentences\n\n### Accessory State Changes with Activity Between Them\n- When activity descriptions appear BETWEEN state changes of the same accessory, report EACH state change separately (do not coalesce)\n- Example: \"Garage Door was opened. Someone unloaded items. Garage Door was closed.\" → report all three separately\n\n### Accessory State Changes with NO Activity Between Them\n- When the same accessory has multiple CONSECUTIVE state changes with no activity between them, report only the FINAL state\n- Example: \"Front Door was unlocked by X. Front Door was locked by X.\" (no activity between) → \"Front Door locked by X.\"\n\n### Accessory State Phrasing\n- \"was opened\" / \"is open\" → \"left open\"\n- \"was closed\" / \"is closed\" → \"closed\"\n- \"was unlocked\" / \"is unlocked\" → \"left unlocked\"\n- \"was locked\" → \"locked\"\n- NEVER use \"left\" before \"closed\" or \"locked\"\n- Preserve \"by Name\" attributions\n\n### Special Case: Arriving + Attributed Accessory\n- If \"Name is arriving...\" appears AND there's an accessory event \"by Name\" with activity between the accessory events, keep \"Name arrived.\" AND report all accessory events separately with their phrasing\n- If \"Name is arriving...\" appears AND consecutive accessory events \"by Name\" have no activity between them, keep \"Name arrived.\" and coalesce to final state only\n\n### Output Format\n- Plain sentences separated by periods, each ending with a period\n- Maintain chronological order from input\n- No bullet points, dashes, or markdown\n- Do not add any information not present in the input"
- "importCameraRecording(fileURL:zoneName:clipUUIDSuffix:)"
- "unknown special token"
- "unknownSpecialToken"
```
