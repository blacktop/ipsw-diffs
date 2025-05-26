## CloudPhotoLibrary

> `/System/Library/PrivateFrameworks/CloudPhotoLibrary.framework/CloudPhotoLibrary`

```diff

-612.0.160.0.0
-  __TEXT.__text: 0x1630bc
+622.0.130.0.0
+  __TEXT.__text: 0x1644ac
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x105c0
+  __TEXT.__objc_methlist: 0x10658
   __TEXT.__const: 0x260
-  __TEXT.__gcc_except_tab: 0x2818
-  __TEXT.__oslogstring: 0x1243a
-  __TEXT.__cstring: 0x11581
-  __TEXT.__unwind_info: 0x5034
+  __TEXT.__gcc_except_tab: 0x2834
+  __TEXT.__oslogstring: 0x125b0
+  __TEXT.__cstring: 0x117d0
+  __TEXT.__unwind_info: 0x5064
   __TEXT.__objc_classname: 0x1ab4
-  __TEXT.__objc_methname: 0x26160
+  __TEXT.__objc_methname: 0x26376
   __TEXT.__objc_methtype: 0x4088
-  __TEXT.__objc_stubs: 0x177c0
+  __TEXT.__objc_stubs: 0x178e0
   __DATA_CONST.__got: 0x1c8
-  __DATA_CONST.__const: 0x51b0
+  __DATA_CONST.__const: 0x5208
   __DATA_CONST.__objc_classlist: 0x790
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x16028
-  __DATA_CONST.__objc_selrefs: 0x7910
+  __DATA_CONST.__objc_const: 0x16088
+  __DATA_CONST.__objc_selrefs: 0x7960
   __DATA_CONST.__objc_arraydata: 0x1208
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__cfstring: 0x12d40
-  __AUTH_CONST.__const: 0xf60
+  __AUTH_CONST.__objc_const: 0xd8
+  __AUTH_CONST.__cfstring: 0x12fe0
+  __AUTH_CONST.__const: 0x1060
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xc8

   __DATA.__objc_protorefs: 0x38
   __DATA.__objc_classrefs: 0x800
   __DATA.__objc_superrefs: 0x748
-  __DATA.__objc_ivar: 0x1524
+  __DATA.__objc_ivar: 0x1530
   __DATA.__data: 0xdd8
   __DATA.__common: 0x21
   __DATA.__bss: 0x8a0
-  __DATA_DIRTY.__const: 0x1240
+  __DATA_DIRTY.__const: 0x11a0
   __DATA_DIRTY.__objc_const: 0x6470
   __DATA_DIRTY.__objc_data: 0x4ab0
   __DATA_DIRTY.__data: 0x1

   - /usr/lib/libcupolicy.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7392
-  Symbols:   22909
-  CStrings:  10950
+  Functions: 7412
+  Symbols:   22968
+  CStrings:  10993
 
Symbols:
+ +[CPLEngineStoreTransaction currentTransaction]
+ -[CPLBeforeUploadCheckItem _dropChangeWithReason:]
+ -[CPLBeforeUploadCheckItems setShouldCheckOverQuotaChangesWithServer:]
+ -[CPLBeforeUploadCheckItems shouldCheckOverQuotaChangesWithServer]
+ -[CPLEngineScheduler hasAScheduledSyncSession]
+ -[CPLEngineScopeStorage noteDidCheckAssetWithServerWhenOverQuotaForScope:error:]
+ -[CPLEngineScopeStorage resetDidCheckAssetWithServerWhenOverQuotaForScope:error:]
+ -[CPLEngineScopeStorage shouldCheckAssetsWithServerWhenOverQuotaForScope:]
+ -[CPLEngineStoreTransaction isLibraryClosed]
+ -[CPLRecordChange _recordKnownByCloudCache]
+ -[CPLRecordChange _setRecordKnownByCloudCache:]
+ GCC_except_table1066
+ GCC_except_table1145
+ GCC_except_table1642
+ GCC_except_table1732
+ GCC_except_table1738
+ GCC_except_table1778
+ GCC_except_table1860
+ GCC_except_table1870
+ GCC_except_table2001
+ GCC_except_table2021
+ GCC_except_table2085
+ GCC_except_table2288
+ GCC_except_table2290
+ GCC_except_table2373
+ GCC_except_table2434
+ GCC_except_table2436
+ GCC_except_table2570
+ GCC_except_table2573
+ GCC_except_table2587
+ GCC_except_table2756
+ GCC_except_table2797
+ GCC_except_table3004
+ GCC_except_table3066
+ GCC_except_table3070
+ GCC_except_table3072
+ GCC_except_table3097
+ GCC_except_table3314
+ GCC_except_table3344
+ GCC_except_table3371
+ GCC_except_table3388
+ GCC_except_table3395
+ GCC_except_table3403
+ GCC_except_table3405
+ GCC_except_table3419
+ GCC_except_table3421
+ GCC_except_table3423
+ GCC_except_table354
+ GCC_except_table363
+ GCC_except_table3718
+ GCC_except_table3751
+ GCC_except_table3833
+ GCC_except_table3843
+ GCC_except_table3900
+ GCC_except_table3903
+ GCC_except_table4067
+ GCC_except_table4075
+ GCC_except_table4152
+ GCC_except_table4156
+ GCC_except_table4160
+ GCC_except_table4167
+ GCC_except_table4182
+ GCC_except_table4183
+ GCC_except_table4224
+ GCC_except_table423
+ GCC_except_table4232
+ GCC_except_table427
+ GCC_except_table4287
+ GCC_except_table4289
+ GCC_except_table4303
+ GCC_except_table4438
+ GCC_except_table4475
+ GCC_except_table4484
+ GCC_except_table4485
+ GCC_except_table4542
+ GCC_except_table4545
+ GCC_except_table456
+ GCC_except_table473
+ GCC_except_table474
+ GCC_except_table4829
+ GCC_except_table483
+ GCC_except_table4857
+ GCC_except_table4887
+ GCC_except_table4920
+ GCC_except_table4924
+ GCC_except_table4973
+ GCC_except_table500
+ GCC_except_table5015
+ GCC_except_table506
+ GCC_except_table5062
+ GCC_except_table5086
+ GCC_except_table5099
+ GCC_except_table5108
+ GCC_except_table5174
+ GCC_except_table5291
+ GCC_except_table5304
+ GCC_except_table5307
+ GCC_except_table5733
+ GCC_except_table5769
+ GCC_except_table5773
+ GCC_except_table5775
+ GCC_except_table5797
+ GCC_except_table5804
+ GCC_except_table5827
+ GCC_except_table5865
+ GCC_except_table5889
+ GCC_except_table5898
+ GCC_except_table5916
+ GCC_except_table5919
+ GCC_except_table5921
+ GCC_except_table5923
+ GCC_except_table5955
+ GCC_except_table6024
+ GCC_except_table605
+ GCC_except_table611
+ GCC_except_table6165
+ GCC_except_table6187
+ GCC_except_table6216
+ GCC_except_table632
+ GCC_except_table637
+ GCC_except_table639
+ GCC_except_table6398
+ GCC_except_table6407
+ GCC_except_table641
+ GCC_except_table6412
+ GCC_except_table6426
+ GCC_except_table643
+ GCC_except_table6440
+ GCC_except_table6450
+ GCC_except_table6455
+ GCC_except_table652
+ GCC_except_table6535
+ GCC_except_table654
+ GCC_except_table656
+ GCC_except_table658
+ GCC_except_table6615
+ GCC_except_table665
+ GCC_except_table667
+ GCC_except_table6679
+ GCC_except_table669
+ GCC_except_table671
+ GCC_except_table6723
+ GCC_except_table6724
+ GCC_except_table673
+ GCC_except_table6737
+ GCC_except_table675
+ GCC_except_table684
+ GCC_except_table686
+ GCC_except_table782
+ GCC_except_table800
+ GCC_except_table802
+ GCC_except_table971
+ _CPLConfigurationMinimumIntervalBetweenOverQuotaRechecksKey
+ _OBJC_IVAR_$_CPLBeforeUploadCheckItems._shouldCheckOverQuotaChangesWithServer
+ _OBJC_IVAR_$_CPLRecordChange._recordKnownByCloudCache
+ _OBJC_IVAR_$_CPLUploadPushedChangesTask._shouldCheckAssetsWithServerWhenOverQuota
+ __CPLBaseRecordViewFailure
+ __OBJC_$_CLASS_METHODS_CPLEngineStoreTransaction
+ __OBJC_$_CLASS_PROP_LIST_CPLEngineStoreTransaction
+ ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.108
+ ___41-[CPLEngineScheduler noteQuotaHasChanged]_block_invoke_3
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.239
+ ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.266
+ ___46-[CPLEngineScheduler hasAScheduledSyncSession]_block_invoke
+ ___46-[CPLEngineScheduler hasAScheduledSyncSession]_block_invoke_2
+ ___46-[CPLEngineScheduler hasAScheduledSyncSession]_block_invoke_3
+ ___46-[CPLEngineScheduler hasAScheduledSyncSession]_block_invoke_4
+ ___51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.321
+ ___54-[CPLUploadPushedChangesTask _checkForRecordExistence]_block_invoke_3
+ ___54-[CPLUploadPushedChangesTask _checkForRecordExistence]_block_invoke_4
+ ___54-[CPLUploadPushedChangesTask _checkForRecordExistence]_block_invoke_5
+ ___55-[CPLEngineStore closeAndDeactivate:completionHandler:]_block_invoke.311
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.133
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.135
+ ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.136
+ ___84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.284
+ ___Block_byref_object_copy_.10264
+ ___Block_byref_object_copy_.1108
+ ___Block_byref_object_copy_.11110
+ ___Block_byref_object_copy_.11663
+ ___Block_byref_object_copy_.11965
+ ___Block_byref_object_copy_.12085
+ ___Block_byref_object_copy_.12872
+ ___Block_byref_object_copy_.13460
+ ___Block_byref_object_copy_.14214
+ ___Block_byref_object_copy_.14466
+ ___Block_byref_object_copy_.14903
+ ___Block_byref_object_copy_.15528
+ ___Block_byref_object_copy_.1563
+ ___Block_byref_object_copy_.16317
+ ___Block_byref_object_copy_.17558
+ ___Block_byref_object_copy_.18001
+ ___Block_byref_object_copy_.18563
+ ___Block_byref_object_copy_.19051
+ ___Block_byref_object_copy_.19382
+ ___Block_byref_object_copy_.2019
+ ___Block_byref_object_copy_.20399
+ ___Block_byref_object_copy_.20698
+ ___Block_byref_object_copy_.2095
+ ___Block_byref_object_copy_.21442
+ ___Block_byref_object_copy_.2459
+ ___Block_byref_object_copy_.4628
+ ___Block_byref_object_copy_.5187
+ ___Block_byref_object_copy_.5344
+ ___Block_byref_object_copy_.5821
+ ___Block_byref_object_copy_.6180
+ ___Block_byref_object_copy_.6436
+ ___Block_byref_object_copy_.654
+ ___Block_byref_object_copy_.8082
+ ___Block_byref_object_copy_.8344
+ ___Block_byref_object_copy_.853
+ ___Block_byref_object_copy_.9325
+ ___Block_byref_object_copy_.9609
+ ___Block_byref_object_copy_.965
+ ___Block_byref_object_dispose_.10265
+ ___Block_byref_object_dispose_.1109
+ ___Block_byref_object_dispose_.11111
+ ___Block_byref_object_dispose_.11664
+ ___Block_byref_object_dispose_.11966
+ ___Block_byref_object_dispose_.12086
+ ___Block_byref_object_dispose_.12873
+ ___Block_byref_object_dispose_.13461
+ ___Block_byref_object_dispose_.14215
+ ___Block_byref_object_dispose_.14467
+ ___Block_byref_object_dispose_.14904
+ ___Block_byref_object_dispose_.15529
+ ___Block_byref_object_dispose_.1564
+ ___Block_byref_object_dispose_.16318
+ ___Block_byref_object_dispose_.17559
+ ___Block_byref_object_dispose_.18002
+ ___Block_byref_object_dispose_.18564
+ ___Block_byref_object_dispose_.19052
+ ___Block_byref_object_dispose_.19383
+ ___Block_byref_object_dispose_.2020
+ ___Block_byref_object_dispose_.20400
+ ___Block_byref_object_dispose_.20699
+ ___Block_byref_object_dispose_.2096
+ ___Block_byref_object_dispose_.21443
+ ___Block_byref_object_dispose_.2460
+ ___Block_byref_object_dispose_.4629
+ ___Block_byref_object_dispose_.5188
+ ___Block_byref_object_dispose_.5345
+ ___Block_byref_object_dispose_.5822
+ ___Block_byref_object_dispose_.6181
+ ___Block_byref_object_dispose_.6437
+ ___Block_byref_object_dispose_.655
+ ___Block_byref_object_dispose_.8083
+ ___Block_byref_object_dispose_.8345
+ ___Block_byref_object_dispose_.854
+ ___Block_byref_object_dispose_.9326
+ ___Block_byref_object_dispose_.9610
+ ___Block_byref_object_dispose_.966
+ ___CPLForceSyncOSLogDomain.18104
+ ___CPLForceSyncOSLogDomain.onceToken.18113
+ ___CPLForceSyncOSLogDomain.result.18114
+ ___CPLSchedulerOSLogDomain.6130
+ ___CPLSchedulerOSLogDomain.onceToken.6131
+ ___CPLSchedulerOSLogDomain.result.6132
+ ___CPLSessionOSLogDomain.14084
+ ___CPLSessionOSLogDomain.15898
+ ___CPLSessionOSLogDomain.19983
+ ___CPLSessionOSLogDomain.onceToken.14135
+ ___CPLSessionOSLogDomain.onceToken.15903
+ ___CPLSessionOSLogDomain.onceToken.19985
+ ___CPLSessionOSLogDomain.result.14137
+ ___CPLSessionOSLogDomain.result.15904
+ ___CPLSessionOSLogDomain.result.19987
+ ___CPLStorageOSLogDomain.1544
+ ___CPLStorageOSLogDomain.15496
+ ___CPLStorageOSLogDomain.18702
+ ___CPLStorageOSLogDomain.19369
+ ___CPLStorageOSLogDomain.19616
+ ___CPLStorageOSLogDomain.4967
+ ___CPLStorageOSLogDomain.6396
+ ___CPLStorageOSLogDomain.7032
+ ___CPLStorageOSLogDomain.7440
+ ___CPLStorageOSLogDomain.7562
+ ___CPLStorageOSLogDomain.7743
+ ___CPLStorageOSLogDomain.864
+ ___CPLStorageOSLogDomain.9293
+ ___CPLStorageOSLogDomain.9376
+ ___CPLStorageOSLogDomain.onceToken.12418
+ ___CPLStorageOSLogDomain.onceToken.1546
+ ___CPLStorageOSLogDomain.onceToken.15498
+ ___CPLStorageOSLogDomain.onceToken.17750
+ ___CPLStorageOSLogDomain.onceToken.18706
+ ___CPLStorageOSLogDomain.onceToken.19374
+ ___CPLStorageOSLogDomain.onceToken.19624
+ ___CPLStorageOSLogDomain.onceToken.4969
+ ___CPLStorageOSLogDomain.onceToken.6398
+ ___CPLStorageOSLogDomain.onceToken.7037
+ ___CPLStorageOSLogDomain.onceToken.7446
+ ___CPLStorageOSLogDomain.onceToken.7564
+ ___CPLStorageOSLogDomain.onceToken.7745
+ ___CPLStorageOSLogDomain.onceToken.873
+ ___CPLStorageOSLogDomain.onceToken.9304
+ ___CPLStorageOSLogDomain.onceToken.9379
+ ___CPLStorageOSLogDomain.result.12420
+ ___CPLStorageOSLogDomain.result.1548
+ ___CPLStorageOSLogDomain.result.15500
+ ___CPLStorageOSLogDomain.result.17752
+ ___CPLStorageOSLogDomain.result.18708
+ ___CPLStorageOSLogDomain.result.19376
+ ___CPLStorageOSLogDomain.result.19626
+ ___CPLStorageOSLogDomain.result.4971
+ ___CPLStorageOSLogDomain.result.6399
+ ___CPLStorageOSLogDomain.result.7038
+ ___CPLStorageOSLogDomain.result.7448
+ ___CPLStorageOSLogDomain.result.7566
+ ___CPLStorageOSLogDomain.result.7747
+ ___CPLStorageOSLogDomain.result.875
+ ___CPLStorageOSLogDomain.result.9306
+ ___CPLStorageOSLogDomain.result.9381
+ ___CPLStoreOSLogDomain.2250
+ ___CPLStoreOSLogDomain.onceToken.2251
+ ___CPLStoreOSLogDomain.result.2252
+ ___CPLTaskOSLogDomain.11949
+ ___CPLTaskOSLogDomain.12329
+ ___CPLTaskOSLogDomain.13357
+ ___CPLTaskOSLogDomain.14875
+ ___CPLTaskOSLogDomain.18508
+ ___CPLTaskOSLogDomain.20322
+ ___CPLTaskOSLogDomain.2080
+ ___CPLTaskOSLogDomain.21394
+ ___CPLTaskOSLogDomain.4403
+ ___CPLTaskOSLogDomain.5744
+ ___CPLTaskOSLogDomain.9555
+ ___CPLTaskOSLogDomain.onceToken.11956
+ ___CPLTaskOSLogDomain.onceToken.12331
+ ___CPLTaskOSLogDomain.onceToken.13366
+ ___CPLTaskOSLogDomain.onceToken.14878
+ ___CPLTaskOSLogDomain.onceToken.18550
+ ___CPLTaskOSLogDomain.onceToken.20331
+ ___CPLTaskOSLogDomain.onceToken.2082
+ ___CPLTaskOSLogDomain.onceToken.21402
+ ___CPLTaskOSLogDomain.onceToken.4406
+ ___CPLTaskOSLogDomain.onceToken.5756
+ ___CPLTaskOSLogDomain.onceToken.9591
+ ___CPLTaskOSLogDomain.result.11958
+ ___CPLTaskOSLogDomain.result.12333
+ ___CPLTaskOSLogDomain.result.13368
+ ___CPLTaskOSLogDomain.result.14879
+ ___CPLTaskOSLogDomain.result.18552
+ ___CPLTaskOSLogDomain.result.20332
+ ___CPLTaskOSLogDomain.result.2084
+ ___CPLTaskOSLogDomain.result.21403
+ ___CPLTaskOSLogDomain.result.4408
+ ___CPLTaskOSLogDomain.result.5758
+ ___CPLTaskOSLogDomain.result.9593
+ _____CPLForceSyncOSLogDomain_block_invoke.18116
+ _____CPLSchedulerOSLogDomain_block_invoke.6134
+ _____CPLSessionOSLogDomain_block_invoke.14140
+ _____CPLSessionOSLogDomain_block_invoke.15906
+ _____CPLSessionOSLogDomain_block_invoke.19990
+ _____CPLStorageOSLogDomain_block_invoke.12425
+ _____CPLStorageOSLogDomain_block_invoke.15503
+ _____CPLStorageOSLogDomain_block_invoke.1551
+ _____CPLStorageOSLogDomain_block_invoke.17759
+ _____CPLStorageOSLogDomain_block_invoke.18711
+ _____CPLStorageOSLogDomain_block_invoke.19379
+ _____CPLStorageOSLogDomain_block_invoke.19629
+ _____CPLStorageOSLogDomain_block_invoke.4974
+ _____CPLStorageOSLogDomain_block_invoke.6401
+ _____CPLStorageOSLogDomain_block_invoke.7040
+ _____CPLStorageOSLogDomain_block_invoke.7451
+ _____CPLStorageOSLogDomain_block_invoke.7569
+ _____CPLStorageOSLogDomain_block_invoke.7750
+ _____CPLStorageOSLogDomain_block_invoke.878
+ _____CPLStorageOSLogDomain_block_invoke.9309
+ _____CPLStorageOSLogDomain_block_invoke.9384
+ _____CPLStoreOSLogDomain_block_invoke.2254
+ _____CPLTaskOSLogDomain_block_invoke.11961
+ _____CPLTaskOSLogDomain_block_invoke.12336
+ _____CPLTaskOSLogDomain_block_invoke.13371
+ _____CPLTaskOSLogDomain_block_invoke.14881
+ _____CPLTaskOSLogDomain_block_invoke.18555
+ _____CPLTaskOSLogDomain_block_invoke.20334
+ _____CPLTaskOSLogDomain_block_invoke.2087
+ _____CPLTaskOSLogDomain_block_invoke.21405
+ _____CPLTaskOSLogDomain_block_invoke.4411
+ _____CPLTaskOSLogDomain_block_invoke.5761
+ _____CPLTaskOSLogDomain_block_invoke.9596
+ ___block_descriptor_56_e8_32s40r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8r40l8
+ ___block_descriptor_72_e8_32s40r48r56r64r_e5_B8?0ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_88_e8_32s40s48r56r64r72r80r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8r48l8r56l8r64l8r72l8r80l8s40l8
+ ___block_literal_global.1005
+ ___block_literal_global.10394
+ ___block_literal_global.10642
+ ___block_literal_global.1113
+ ___block_literal_global.11133
+ ___block_literal_global.11957
+ ___block_literal_global.12.6517
+ ___block_literal_global.12131
+ ___block_literal_global.12366
+ ___block_literal_global.12419
+ ___block_literal_global.12591
+ ___block_literal_global.130.18263
+ ___block_literal_global.130.18551
+ ___block_literal_global.13089
+ ___block_literal_global.13107
+ ___block_literal_global.13167
+ ___block_literal_global.13367
+ ___block_literal_global.138.16660
+ ___block_literal_global.1386
+ ___block_literal_global.13947
+ ___block_literal_global.14.12367
+ ___block_literal_global.14.4348
+ ___block_literal_global.14157
+ ___block_literal_global.142.11112
+ ___block_literal_global.142.17751
+ ___block_literal_global.1421
+ ___block_literal_global.14620
+ ___block_literal_global.14929
+ ___block_literal_global.15295
+ ___block_literal_global.1547
+ ___block_literal_global.15499
+ ___block_literal_global.155.7746
+ ___block_literal_global.15915
+ ___block_literal_global.16088
+ ___block_literal_global.16208
+ ___block_literal_global.16771
+ ___block_literal_global.17330
+ ___block_literal_global.17637
+ ___block_literal_global.17754
+ ___block_literal_global.1798
+ ___block_literal_global.18258
+ ___block_literal_global.18570
+ ___block_literal_global.18707
+ ___block_literal_global.18879
+ ___block_literal_global.19375
+ ___block_literal_global.19625
+ ___block_literal_global.1969
+ ___block_literal_global.19785
+ ___block_literal_global.19986
+ ___block_literal_global.2.16770
+ ___block_literal_global.2.21658
+ ___block_literal_global.20138
+ ___block_literal_global.2018
+ ___block_literal_global.20395
+ ___block_literal_global.2083
+ ___block_literal_global.20950
+ ___block_literal_global.210.14136
+ ___block_literal_global.21084
+ ___block_literal_global.21152
+ ___block_literal_global.21542
+ ___block_literal_global.21652
+ ___block_literal_global.21748
+ ___block_literal_global.21934
+ ___block_literal_global.22.6520
+ ___block_literal_global.2229
+ ___block_literal_global.2477
+ ___block_literal_global.27.14177
+ ___block_literal_global.2701
+ ___block_literal_global.275
+ ___block_literal_global.277
+ ___block_literal_global.2909
+ ___block_literal_global.295
+ ___block_literal_global.3113
+ ___block_literal_global.32.19753
+ ___block_literal_global.323
+ ___block_literal_global.33.5871
+ ___block_literal_global.3536
+ ___block_literal_global.3663
+ ___block_literal_global.37.16696
+ ___block_literal_global.37.6524
+ ___block_literal_global.376
+ ___block_literal_global.3817
+ ___block_literal_global.4227
+ ___block_literal_global.4313
+ ___block_literal_global.4407
+ ___block_literal_global.4549
+ ___block_literal_global.4625
+ ___block_literal_global.47.6527
+ ___block_literal_global.479
+ ___block_literal_global.482
+ ___block_literal_global.4970
+ ___block_literal_global.5163
+ ___block_literal_global.533
+ ___block_literal_global.536
+ ___block_literal_global.5757
+ ___block_literal_global.5870
+ ___block_literal_global.6246
+ ___block_literal_global.6514
+ ___block_literal_global.7129
+ ___block_literal_global.717
+ ___block_literal_global.7343
+ ___block_literal_global.7447
+ ___block_literal_global.7565
+ ___block_literal_global.7793
+ ___block_literal_global.7972
+ ___block_literal_global.8214
+ ___block_literal_global.8602
+ ___block_literal_global.874
+ ___block_literal_global.8889
+ ___block_literal_global.89.12332
+ ___block_literal_global.9151
+ ___block_literal_global.9305
+ ___block_literal_global.9380
+ ___block_literal_global.94.8355
+ ___block_literal_global.9592
+ ___block_literal_global.987
+ ___block_literal_global.993
+ ___block_literal_global.996
+ ___cpl_dispatch_async_block_invoke.10068
+ ___cpl_dispatch_async_block_invoke.11944
+ ___cpl_dispatch_async_block_invoke.12252
+ ___cpl_dispatch_async_block_invoke.12325
+ ___cpl_dispatch_async_block_invoke.13449
+ ___cpl_dispatch_async_block_invoke.1352
+ ___cpl_dispatch_async_block_invoke.14451
+ ___cpl_dispatch_async_block_invoke.14871
+ ___cpl_dispatch_async_block_invoke.15248
+ ___cpl_dispatch_async_block_invoke.15723
+ ___cpl_dispatch_async_block_invoke.16204
+ ___cpl_dispatch_async_block_invoke.17988
+ ___cpl_dispatch_async_block_invoke.18506
+ ___cpl_dispatch_async_block_invoke.18887
+ ___cpl_dispatch_async_block_invoke.20140
+ ___cpl_dispatch_async_block_invoke.20338
+ ___cpl_dispatch_async_block_invoke.21451
+ ___cpl_dispatch_async_block_invoke.5384
+ ___cpl_dispatch_async_block_invoke.5742
+ ___cpl_dispatch_async_block_invoke.6004
+ ___cpl_dispatch_async_block_invoke.6409
+ ___cpl_dispatch_async_block_invoke.659
+ ___cpl_dispatch_async_block_invoke.8079
+ ___cpl_dispatch_async_block_invoke.8347
+ ___cpl_dispatch_async_block_invoke.9551
+ __doProtected:.onceToken.13106
+ __doProtected:.onceToken.20137
+ __doProtected:.queue.20139
+ __statusDidChange.10284
+ __unnamed_array_storage.10348
+ __unnamed_array_storage.11506
+ __unnamed_array_storage.1377
+ __unnamed_array_storage.19015
+ __unnamed_array_storage.4548
+ __unnamed_array_storage.4636
+ _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.16681
+ _initWithCoder:.logOnceToken.17639
+ _initWithCoder:.onceToken.12130
+ _initWithCoder:.onceToken.15914
+ _initWithCoder:.onceToken.17636
+ _initWithCoder:.onceToken.19784
+ _initWithCoder:.onceToken.21933
+ _initWithCoder:.onceToken.4206
+ _initWithCoder:.onceToken.4312
+ _initWithCoder:.onceToken.5158
+ _initWithCoder:.onceToken.8888
+ _initWithCoder:.pushContextsClasses.19786
+ _initWithCoder:.stringClass.8890
+ _objc_msgSend$_dropChangeWithReason:
+ _objc_msgSend$_recordKnownByCloudCache
+ _objc_msgSend$_setRecordKnownByCloudCache:
+ _objc_msgSend$currentTransaction
+ _objc_msgSend$isLibraryClosed
+ _objc_msgSend$noteDidCheckAssetWithServerWhenOverQuotaForScope:error:
+ _objc_msgSend$resetDidCheckAssetWithServerWhenOverQuotaForScope:error:
+ _objc_msgSend$setShouldCheckOverQuotaChangesWithServer:
+ _objc_msgSend$shouldCheckAssetsWithServerWhenOverQuotaForScope:
+ _objc_msgSend$shouldCheckOverQuotaChangesWithServer
+ _propertiesForChangeType:.onceToken.12948
+ _propertiesForChangeType:.onceToken.16695
+ _propertiesForChangeType:.onceToken.21083
+ _propertiesForChangeType:.properties.21085
- GCC_except_table1063
- GCC_except_table1142
- GCC_except_table1639
- GCC_except_table1729
- GCC_except_table1735
- GCC_except_table1775
- GCC_except_table1857
- GCC_except_table1867
- GCC_except_table1998
- GCC_except_table2018
- GCC_except_table2082
- GCC_except_table2285
- GCC_except_table2287
- GCC_except_table2365
- GCC_except_table2425
- GCC_except_table2427
- GCC_except_table2561
- GCC_except_table2564
- GCC_except_table2578
- GCC_except_table2744
- GCC_except_table2785
- GCC_except_table2992
- GCC_except_table3054
- GCC_except_table3058
- GCC_except_table3060
- GCC_except_table3085
- GCC_except_table330
- GCC_except_table3302
- GCC_except_table3332
- GCC_except_table3359
- GCC_except_table3376
- GCC_except_table3383
- GCC_except_table339
- GCC_except_table3391
- GCC_except_table3393
- GCC_except_table3407
- GCC_except_table3409
- GCC_except_table3411
- GCC_except_table3706
- GCC_except_table3739
- GCC_except_table3821
- GCC_except_table3831
- GCC_except_table3888
- GCC_except_table3891
- GCC_except_table401
- GCC_except_table405
- GCC_except_table4055
- GCC_except_table4063
- GCC_except_table4140
- GCC_except_table4144
- GCC_except_table4148
- GCC_except_table4155
- GCC_except_table4170
- GCC_except_table4171
- GCC_except_table4212
- GCC_except_table4220
- GCC_except_table4275
- GCC_except_table4277
- GCC_except_table4279
- GCC_except_table4424
- GCC_except_table4461
- GCC_except_table4470
- GCC_except_table4471
- GCC_except_table4528
- GCC_except_table4531
- GCC_except_table454
- GCC_except_table471
- GCC_except_table472
- GCC_except_table481
- GCC_except_table4815
- GCC_except_table4843
- GCC_except_table4873
- GCC_except_table4892
- GCC_except_table4910
- GCC_except_table4959
- GCC_except_table498
- GCC_except_table5001
- GCC_except_table504
- GCC_except_table5048
- GCC_except_table5072
- GCC_except_table5085
- GCC_except_table5094
- GCC_except_table5146
- GCC_except_table5277
- GCC_except_table5290
- GCC_except_table5293
- GCC_except_table5717
- GCC_except_table5752
- GCC_except_table5756
- GCC_except_table5758
- GCC_except_table5780
- GCC_except_table5787
- GCC_except_table5810
- GCC_except_table5848
- GCC_except_table5872
- GCC_except_table5881
- GCC_except_table5899
- GCC_except_table5902
- GCC_except_table5904
- GCC_except_table5906
- GCC_except_table5938
- GCC_except_table6007
- GCC_except_table602
- GCC_except_table608
- GCC_except_table6148
- GCC_except_table6170
- GCC_except_table6199
- GCC_except_table629
- GCC_except_table634
- GCC_except_table636
- GCC_except_table638
- GCC_except_table6381
- GCC_except_table6390
- GCC_except_table6395
- GCC_except_table640
- GCC_except_table6409
- GCC_except_table6423
- GCC_except_table6433
- GCC_except_table6438
- GCC_except_table649
- GCC_except_table651
- GCC_except_table6518
- GCC_except_table653
- GCC_except_table655
- GCC_except_table6598
- GCC_except_table662
- GCC_except_table664
- GCC_except_table666
- GCC_except_table6662
- GCC_except_table668
- GCC_except_table670
- GCC_except_table6706
- GCC_except_table6707
- GCC_except_table6717
- GCC_except_table672
- GCC_except_table681
- GCC_except_table683
- GCC_except_table779
- GCC_except_table797
- GCC_except_table799
- GCC_except_table968
- ___38-[CPLPushToTransportScopeTask _launch]_block_invoke_2.107
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.190
- ___44-[CPLEngineStore openWithCompletionHandler:]_block_invoke.218
- ___51-[CPLEngineStore _reallySchedulePendingUpdateApply]_block_invoke.270
- ___55-[CPLEngineStore closeAndDeactivate:completionHandler:]_block_invoke.260
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.127
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke.129
- ___62-[CPLPushToTransportScopeTask _uploadTask:didFinishWithError:]_block_invoke_2.130
- ___84-[CPLEngineStore _performWriteTransactionByPassBlocker:WithBlock:completionHandler:]_block_invoke.233
- ___Block_byref_object_copy_.1022
- ___Block_byref_object_copy_.10330
- ___Block_byref_object_copy_.11174
- ___Block_byref_object_copy_.1164
- ___Block_byref_object_copy_.11732
- ___Block_byref_object_copy_.12033
- ___Block_byref_object_copy_.12153
- ___Block_byref_object_copy_.12935
- ___Block_byref_object_copy_.13520
- ___Block_byref_object_copy_.14275
- ___Block_byref_object_copy_.14532
- ___Block_byref_object_copy_.14948
- ___Block_byref_object_copy_.15574
- ___Block_byref_object_copy_.1633
- ___Block_byref_object_copy_.16365
- ___Block_byref_object_copy_.17592
- ___Block_byref_object_copy_.18026
- ___Block_byref_object_copy_.18571
- ___Block_byref_object_copy_.19055
- ___Block_byref_object_copy_.19387
- ___Block_byref_object_copy_.20406
- ___Block_byref_object_copy_.20705
- ___Block_byref_object_copy_.2088
- ___Block_byref_object_copy_.21451
- ___Block_byref_object_copy_.2164
- ___Block_byref_object_copy_.2528
- ___Block_byref_object_copy_.4678
- ___Block_byref_object_copy_.5241
- ___Block_byref_object_copy_.5398
- ___Block_byref_object_copy_.5871
- ___Block_byref_object_copy_.6253
- ___Block_byref_object_copy_.650
- ___Block_byref_object_copy_.6512
- ___Block_byref_object_copy_.8149
- ___Block_byref_object_copy_.8405
- ___Block_byref_object_copy_.911
- ___Block_byref_object_copy_.9388
- ___Block_byref_object_copy_.9667
- ___Block_byref_object_dispose_.1023
- ___Block_byref_object_dispose_.10331
- ___Block_byref_object_dispose_.11175
- ___Block_byref_object_dispose_.1165
- ___Block_byref_object_dispose_.11733
- ___Block_byref_object_dispose_.12034
- ___Block_byref_object_dispose_.12154
- ___Block_byref_object_dispose_.12936
- ___Block_byref_object_dispose_.13521
- ___Block_byref_object_dispose_.14276
- ___Block_byref_object_dispose_.14533
- ___Block_byref_object_dispose_.14949
- ___Block_byref_object_dispose_.15575
- ___Block_byref_object_dispose_.1634
- ___Block_byref_object_dispose_.16366
- ___Block_byref_object_dispose_.17593
- ___Block_byref_object_dispose_.18027
- ___Block_byref_object_dispose_.18572
- ___Block_byref_object_dispose_.19056
- ___Block_byref_object_dispose_.19388
- ___Block_byref_object_dispose_.20407
- ___Block_byref_object_dispose_.20706
- ___Block_byref_object_dispose_.2089
- ___Block_byref_object_dispose_.21452
- ___Block_byref_object_dispose_.2165
- ___Block_byref_object_dispose_.2529
- ___Block_byref_object_dispose_.4679
- ___Block_byref_object_dispose_.5242
- ___Block_byref_object_dispose_.5399
- ___Block_byref_object_dispose_.5872
- ___Block_byref_object_dispose_.6254
- ___Block_byref_object_dispose_.651
- ___Block_byref_object_dispose_.6513
- ___Block_byref_object_dispose_.8150
- ___Block_byref_object_dispose_.8406
- ___Block_byref_object_dispose_.912
- ___Block_byref_object_dispose_.9389
- ___Block_byref_object_dispose_.9668
- ___CPLForceSyncOSLogDomain.18110
- ___CPLForceSyncOSLogDomain.onceToken.18119
- ___CPLForceSyncOSLogDomain.result.18120
- ___CPLSchedulerOSLogDomain.6207
- ___CPLSchedulerOSLogDomain.onceToken.6208
- ___CPLSchedulerOSLogDomain.result.6209
- ___CPLSessionOSLogDomain.14145
- ___CPLSessionOSLogDomain.15946
- ___CPLSessionOSLogDomain.19988
- ___CPLSessionOSLogDomain.onceToken.14196
- ___CPLSessionOSLogDomain.onceToken.15951
- ___CPLSessionOSLogDomain.onceToken.19990
- ___CPLSessionOSLogDomain.result.14198
- ___CPLSessionOSLogDomain.result.15952
- ___CPLSessionOSLogDomain.result.19992
- ___CPLStorageOSLogDomain.15542
- ___CPLStorageOSLogDomain.1613
- ___CPLStorageOSLogDomain.18710
- ___CPLStorageOSLogDomain.19374
- ___CPLStorageOSLogDomain.19621
- ___CPLStorageOSLogDomain.5020
- ___CPLStorageOSLogDomain.6475
- ___CPLStorageOSLogDomain.7092
- ___CPLStorageOSLogDomain.7508
- ___CPLStorageOSLogDomain.7630
- ___CPLStorageOSLogDomain.7811
- ___CPLStorageOSLogDomain.922
- ___CPLStorageOSLogDomain.9356
- ___CPLStorageOSLogDomain.9439
- ___CPLStorageOSLogDomain.onceToken.12486
- ___CPLStorageOSLogDomain.onceToken.15544
- ___CPLStorageOSLogDomain.onceToken.1615
- ___CPLStorageOSLogDomain.onceToken.17784
- ___CPLStorageOSLogDomain.onceToken.18714
- ___CPLStorageOSLogDomain.onceToken.19379
- ___CPLStorageOSLogDomain.onceToken.19629
- ___CPLStorageOSLogDomain.onceToken.5022
- ___CPLStorageOSLogDomain.onceToken.6477
- ___CPLStorageOSLogDomain.onceToken.7100
- ___CPLStorageOSLogDomain.onceToken.7514
- ___CPLStorageOSLogDomain.onceToken.7632
- ___CPLStorageOSLogDomain.onceToken.7813
- ___CPLStorageOSLogDomain.onceToken.931
- ___CPLStorageOSLogDomain.onceToken.9367
- ___CPLStorageOSLogDomain.onceToken.9442
- ___CPLStorageOSLogDomain.result.12488
- ___CPLStorageOSLogDomain.result.15546
- ___CPLStorageOSLogDomain.result.1617
- ___CPLStorageOSLogDomain.result.17786
- ___CPLStorageOSLogDomain.result.18716
- ___CPLStorageOSLogDomain.result.19381
- ___CPLStorageOSLogDomain.result.19631
- ___CPLStorageOSLogDomain.result.5024
- ___CPLStorageOSLogDomain.result.6478
- ___CPLStorageOSLogDomain.result.7101
- ___CPLStorageOSLogDomain.result.7516
- ___CPLStorageOSLogDomain.result.7634
- ___CPLStorageOSLogDomain.result.7815
- ___CPLStorageOSLogDomain.result.933
- ___CPLStorageOSLogDomain.result.9369
- ___CPLStorageOSLogDomain.result.9444
- ___CPLStoreOSLogDomain.2319
- ___CPLStoreOSLogDomain.onceToken.2320
- ___CPLStoreOSLogDomain.result.2321
- ___CPLTaskOSLogDomain.12018
- ___CPLTaskOSLogDomain.12397
- ___CPLTaskOSLogDomain.13416
- ___CPLTaskOSLogDomain.14920
- ___CPLTaskOSLogDomain.18516
- ___CPLTaskOSLogDomain.20329
- ___CPLTaskOSLogDomain.21401
- ___CPLTaskOSLogDomain.2149
- ___CPLTaskOSLogDomain.4443
- ___CPLTaskOSLogDomain.5794
- ___CPLTaskOSLogDomain.9620
- ___CPLTaskOSLogDomain.onceToken.12025
- ___CPLTaskOSLogDomain.onceToken.12399
- ___CPLTaskOSLogDomain.onceToken.13425
- ___CPLTaskOSLogDomain.onceToken.14923
- ___CPLTaskOSLogDomain.onceToken.18558
- ___CPLTaskOSLogDomain.onceToken.20338
- ___CPLTaskOSLogDomain.onceToken.21409
- ___CPLTaskOSLogDomain.onceToken.2151
- ___CPLTaskOSLogDomain.onceToken.4446
- ___CPLTaskOSLogDomain.onceToken.5806
- ___CPLTaskOSLogDomain.onceToken.9656
- ___CPLTaskOSLogDomain.result.12027
- ___CPLTaskOSLogDomain.result.12401
- ___CPLTaskOSLogDomain.result.13427
- ___CPLTaskOSLogDomain.result.14924
- ___CPLTaskOSLogDomain.result.18560
- ___CPLTaskOSLogDomain.result.20339
- ___CPLTaskOSLogDomain.result.21411
- ___CPLTaskOSLogDomain.result.2153
- ___CPLTaskOSLogDomain.result.4448
- ___CPLTaskOSLogDomain.result.5808
- ___CPLTaskOSLogDomain.result.9658
- _____CPLForceSyncOSLogDomain_block_invoke.18122
- _____CPLSchedulerOSLogDomain_block_invoke.6211
- _____CPLSessionOSLogDomain_block_invoke.14201
- _____CPLSessionOSLogDomain_block_invoke.15954
- _____CPLSessionOSLogDomain_block_invoke.19995
- _____CPLStorageOSLogDomain_block_invoke.12493
- _____CPLStorageOSLogDomain_block_invoke.15549
- _____CPLStorageOSLogDomain_block_invoke.1620
- _____CPLStorageOSLogDomain_block_invoke.17793
- _____CPLStorageOSLogDomain_block_invoke.18719
- _____CPLStorageOSLogDomain_block_invoke.19384
- _____CPLStorageOSLogDomain_block_invoke.19634
- _____CPLStorageOSLogDomain_block_invoke.5027
- _____CPLStorageOSLogDomain_block_invoke.6480
- _____CPLStorageOSLogDomain_block_invoke.7103
- _____CPLStorageOSLogDomain_block_invoke.7519
- _____CPLStorageOSLogDomain_block_invoke.7637
- _____CPLStorageOSLogDomain_block_invoke.7818
- _____CPLStorageOSLogDomain_block_invoke.936
- _____CPLStorageOSLogDomain_block_invoke.9372
- _____CPLStorageOSLogDomain_block_invoke.9447
- _____CPLStoreOSLogDomain_block_invoke.2323
- _____CPLTaskOSLogDomain_block_invoke.12030
- _____CPLTaskOSLogDomain_block_invoke.12404
- _____CPLTaskOSLogDomain_block_invoke.13430
- _____CPLTaskOSLogDomain_block_invoke.14926
- _____CPLTaskOSLogDomain_block_invoke.18563
- _____CPLTaskOSLogDomain_block_invoke.20341
- _____CPLTaskOSLogDomain_block_invoke.21414
- _____CPLTaskOSLogDomain_block_invoke.2156
- _____CPLTaskOSLogDomain_block_invoke.4451
- _____CPLTaskOSLogDomain_block_invoke.5811
- _____CPLTaskOSLogDomain_block_invoke.9661
- ___block_descriptor_80_e8_32s40s48r56r64r72r_e35_v16?0"CPLEngineStoreTransaction"8ls32l8r48l8r56l8r64l8r72l8s40l8
- ___block_literal_global.10461
- ___block_literal_global.1061
- ___block_literal_global.10703
- ___block_literal_global.11197
- ___block_literal_global.1169
- ___block_literal_global.12.6590
- ___block_literal_global.12026
- ___block_literal_global.12199
- ___block_literal_global.12434
- ___block_literal_global.12487
- ___block_literal_global.12659
- ___block_literal_global.130.18270
- ___block_literal_global.130.18559
- ___block_literal_global.13148
- ___block_literal_global.13166
- ___block_literal_global.13226
- ___block_literal_global.13426
- ___block_literal_global.138.16705
- ___block_literal_global.14.12435
- ___block_literal_global.14.4388
- ___block_literal_global.14007
- ___block_literal_global.142.11176
- ___block_literal_global.142.17785
- ___block_literal_global.14218
- ___block_literal_global.1455
- ___block_literal_global.14689
- ___block_literal_global.1490
- ___block_literal_global.14974
- ___block_literal_global.15341
- ___block_literal_global.155.7814
- ___block_literal_global.15545
- ___block_literal_global.15963
- ___block_literal_global.16136
- ___block_literal_global.1616.4666
- ___block_literal_global.16256
- ___block_literal_global.16818
- ___block_literal_global.17371
- ___block_literal_global.17671
- ___block_literal_global.17788
- ___block_literal_global.18266
- ___block_literal_global.18578
- ___block_literal_global.1865
- ___block_literal_global.18715
- ___block_literal_global.18886
- ___block_literal_global.19380
- ___block_literal_global.19630
- ___block_literal_global.19790
- ___block_literal_global.19991
- ___block_literal_global.2.16817
- ___block_literal_global.2.21661
- ___block_literal_global.20143
- ___block_literal_global.2038
- ___block_literal_global.20402
- ___block_literal_global.2087
- ___block_literal_global.20957
- ___block_literal_global.210.14197
- ___block_literal_global.21091
- ___block_literal_global.21159
- ___block_literal_global.21410
- ___block_literal_global.2152
- ___block_literal_global.21655
- ___block_literal_global.21751
- ___block_literal_global.21937
- ___block_literal_global.22.6593
- ___block_literal_global.2298
- ___block_literal_global.244
- ___block_literal_global.2547
- ___block_literal_global.27.14238
- ___block_literal_global.272
- ___block_literal_global.2773
- ___block_literal_global.2970
- ___block_literal_global.3161
- ___block_literal_global.32.19758
- ___block_literal_global.33.5921
- ___block_literal_global.3581
- ___block_literal_global.37.16743
- ___block_literal_global.37.6597
- ___block_literal_global.3708
- ___block_literal_global.3862
- ___block_literal_global.4270
- ___block_literal_global.4353
- ___block_literal_global.4447
- ___block_literal_global.4585
- ___block_literal_global.4674
- ___block_literal_global.47.6600
- ___block_literal_global.470
- ___block_literal_global.473
- ___block_literal_global.5023
- ___block_literal_global.5217
- ___block_literal_global.526
- ___block_literal_global.529
- ___block_literal_global.5807
- ___block_literal_global.5920
- ___block_literal_global.6321
- ___block_literal_global.6587
- ___block_literal_global.7201
- ___block_literal_global.7411
- ___block_literal_global.7515
- ___block_literal_global.7633
- ___block_literal_global.778
- ___block_literal_global.7861
- ___block_literal_global.8039
- ___block_literal_global.8280
- ___block_literal_global.8662
- ___block_literal_global.89.12400
- ___block_literal_global.8952
- ___block_literal_global.91
- ___block_literal_global.9214
- ___block_literal_global.931
- ___block_literal_global.932
- ___block_literal_global.9368
- ___block_literal_global.937
- ___block_literal_global.940
- ___block_literal_global.9443
- ___block_literal_global.9657
- ___cpl_dispatch_async_block_invoke.10145
- ___cpl_dispatch_async_block_invoke.12013
- ___cpl_dispatch_async_block_invoke.12320
- ___cpl_dispatch_async_block_invoke.12393
- ___cpl_dispatch_async_block_invoke.13508
- ___cpl_dispatch_async_block_invoke.1407
- ___cpl_dispatch_async_block_invoke.14515
- ___cpl_dispatch_async_block_invoke.14916
- ___cpl_dispatch_async_block_invoke.15295
- ___cpl_dispatch_async_block_invoke.15770
- ___cpl_dispatch_async_block_invoke.16252
- ___cpl_dispatch_async_block_invoke.18019
- ___cpl_dispatch_async_block_invoke.18514
- ___cpl_dispatch_async_block_invoke.18894
- ___cpl_dispatch_async_block_invoke.20145
- ___cpl_dispatch_async_block_invoke.20345
- ___cpl_dispatch_async_block_invoke.21460
- ___cpl_dispatch_async_block_invoke.5434
- ___cpl_dispatch_async_block_invoke.5792
- ___cpl_dispatch_async_block_invoke.6086
- ___cpl_dispatch_async_block_invoke.6488
- ___cpl_dispatch_async_block_invoke.653
- ___cpl_dispatch_async_block_invoke.8146
- ___cpl_dispatch_async_block_invoke.8408
- ___cpl_dispatch_async_block_invoke.9616
- __doProtected:.onceToken.13165
- __doProtected:.onceToken.20142
- __doProtected:.queue.20144
- __statusDidChange.10349
- __unnamed_array_storage.10418
- __unnamed_array_storage.11575
- __unnamed_array_storage.1434
- __unnamed_array_storage.19019
- __unnamed_array_storage.4584
- __unnamed_array_storage.4686
- _copyDerivativesFromRecordIfPossible:.originalDerivativesImageAndVideo.16727
- _initWithCoder:.logOnceToken.17673
- _initWithCoder:.onceToken.12198
- _initWithCoder:.onceToken.15962
- _initWithCoder:.onceToken.17670
- _initWithCoder:.onceToken.19789
- _initWithCoder:.onceToken.21936
- _initWithCoder:.onceToken.4249
- _initWithCoder:.onceToken.4352
- _initWithCoder:.onceToken.5212
- _initWithCoder:.onceToken.8951
- _initWithCoder:.pushContextsClasses.19791
- _initWithCoder:.stringClass.8953
- _objc_msgSend$raise
- _propertiesForChangeType:.onceToken.13011
- _propertiesForChangeType:.onceToken.16742
- _propertiesForChangeType:.onceToken.21090
- _propertiesForChangeType:.properties.21092
CStrings:
+ "\x03\x114\x17"
+ " after resetting priority"
+ "CPLMinimumIntervalBetweenOverQuotaRechecks"
+ "Changes have been pushed by client for %{public}@ - restarting uploads%@"
+ "CloudPhotoLibrary-622.0.130"
+ "Context: %@"
+ "Failed to note that engine checked assets on server"
+ "Last reset events:\n\t%@"
+ "Moving priority from %lu to %lu for %@ - reason: %@"
+ "No base record in %@ to apply %@ on - missing scope"
+ "No base record in %@ to apply %@ on - scope: %@"
+ "T@\"CPLEngineStoreTransaction\",R,N"
+ "TB,N,V_shouldCheckOverQuotaChangesWithServer"
+ "Trying to drop an already dropped %@"
+ "Trying to get the current transaction outside of any transaction"
+ "Will check assets of %@ only against cloud cache when over-quota"
+ "Will check assets of %@ with server when over-quota"
+ "_CPLLastAssetCheckOverQuotaDateForPrimarySync"
+ "_dropChangeWithReason:"
+ "_recordKnownByCloudCache"
+ "_setRecordKnownByCloudCache:"
+ "_shouldCheckAssetsWithServerWhenOverQuota"
+ "_shouldCheckOverQuotaChangesWithServer"
+ "acknowledged by client"
+ "conflicting ID mapping"
+ "currentTransaction"
+ "delete staged in cloud cache"
+ "flags: %@"
+ "hasAScheduledSyncSession"
+ "in ID mapping"
+ "in cloud cache"
+ "invalid index"
+ "invalid index from reset sync"
+ "isLibraryClosed"
+ "master has resources to upload"
+ "missing base %@ in %@ (%@)"
+ "missing scope"
+ "no ID mapping"
+ "no context"
+ "not in cloud cache"
+ "noteDidCheckAssetWithServerWhenOverQuotaForScope:error:"
+ "over_quota.minimum_interval_between_rechecks.seconds"
+ "removing asset from recently deleted in scope"
+ "removing asset from recently deleted in sharing scope"
+ "resetDidCheckAssetWithServerWhenOverQuotaForScope:error:"
+ "setShouldCheckOverQuotaChangesWithServer:"
+ "shouldCheckAssetsWithServerWhenOverQuotaForScope:"
+ "shouldCheckOverQuotaChangesWithServer"
+ "staged in cloud cache"
- "\x02\x114\x17"
- "%@ push priority will be moved from %lu to %lu - reason: %@"
- "Changes have been pushed for %{public}@ - restarting uploads"
- "CloudPhotoLibrary-612.0.160"
- "No base record in %@ to apply %@ on"
- "masters has resources to upload"
- "missing base record in changed record view"
- "raise"

```
