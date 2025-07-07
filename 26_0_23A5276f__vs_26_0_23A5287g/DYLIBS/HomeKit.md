## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1334.0.0.0.1
-  __TEXT.__text: 0x2c8f60
+1340.3.0.0.0
+  __TEXT.__text: 0x2c99cc
   __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_methlist: 0x25474
+  __TEXT.__objc_methlist: 0x257b4
   __TEXT.__const: 0x1d0c
   __TEXT.__dlopen_cstrs: 0x3a1
-  __TEXT.__cstring: 0x2a516
+  __TEXT.__cstring: 0x2a563
   __TEXT.__swift5_typeref: 0xa4c
   __TEXT.__constg_swiftt: 0x8fc
   __TEXT.__swift5_reflstr: 0x391

   __TEXT.__swift5_types: 0xa4
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__oslogstring: 0x2ab27
+  __TEXT.__oslogstring: 0x2ac80
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__gcc_except_tab: 0x6fc4
+  __TEXT.__gcc_except_tab: 0x706c
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x9a70
+  __TEXT.__unwind_info: 0x9a78
   __TEXT.__eh_frame: 0xd88
-  __TEXT.__objc_classname: 0x4f6c
-  __TEXT.__objc_methname: 0x48025
-  __TEXT.__objc_methtype: 0x873a
-  __TEXT.__objc_stubs: 0x25ae0
-  __DATA_CONST.__got: 0x1808
-  __DATA_CONST.__const: 0x7da8
-  __DATA_CONST.__objc_classlist: 0x1218
+  __TEXT.__objc_classname: 0x4fb3
+  __TEXT.__objc_methname: 0x482a2
+  __TEXT.__objc_methtype: 0x88d8
+  __TEXT.__objc_stubs: 0x25c40
+  __DATA_CONST.__got: 0x1818
+  __DATA_CONST.__const: 0x7de0
+  __DATA_CONST.__objc_classlist: 0x1228
   __DATA_CONST.__objc_catlist: 0x108
-  __DATA_CONST.__objc_protolist: 0x498
+  __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd118
+  __DATA_CONST.__objc_selrefs: 0xd178
   __DATA_CONST.__objc_protorefs: 0xb8
-  __DATA_CONST.__objc_superrefs: 0xf28
+  __DATA_CONST.__objc_superrefs: 0xf30
   __DATA_CONST.__objc_arraydata: 0x1380
   __AUTH_CONST.__auth_got: 0xd88
-  __AUTH_CONST.__const: 0x2a10
-  __AUTH_CONST.__cfstring: 0x27740
-  __AUTH_CONST.__objc_const: 0x430f8
+  __AUTH_CONST.__const: 0x2a30
+  __AUTH_CONST.__cfstring: 0x277e0
+  __AUTH_CONST.__objc_const: 0x43698
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH.__objc_data: 0x83e8
+  __AUTH.__objc_data: 0x8488
   __AUTH.__data: 0x580
-  __DATA.__objc_ivar: 0x251c
-  __DATA.__data: 0x3ce8
-  __DATA.__bss: 0x31a0
+  __DATA.__objc_ivar: 0x2528
+  __DATA.__data: 0x3e08
+  __DATA.__bss: 0x31c0
   __DATA.__common: 0x59
   __DATA_DIRTY.__objc_data: 0x32a0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x270
+  __DATA_DIRTY.__bss: 0x260
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8DFF4B42-3E16-325E-86EC-C7563D1D20E2
-  Functions: 14310
-  Symbols:   43943
-  CStrings:  25609
+  UUID: 71A72193-0B9D-3042-9A91-5821687C498B
+  Functions: 14339
+  Symbols:   44058
+  CStrings:  25664
 
Symbols:
+ +[HMCameraView logCategory]
+ -[HMAccessory _handleSupportsAdaptiveTemperatureAutomationMessage:]
+ -[HMAccessory _handleSupportsCleanEnergyAutomationMessage:]
+ -[HMAccessory handleRuntimeStateUpdate:]
+ -[HMCameraView logIdentifier]
+ -[HMMigrationBoost _handleDaemonInterruptedNotification:]
+ -[HMUserActionPredictionDuetDataSource fetchPredictionsFromBackendWithCompletion:]
+ -[HMUserActionPredictionProvider _fetchPredictionsFromBackendAndUpdateHomes]
+ -[HMUserActionPredictionProvider initWithWorkQueue:messageDispatcher:UUID:dataSource:predictionDataSource:predictionTransformer:darwinNotificationProvider:]
+ -[HMUserActionPredictionProvider predictionDataSource]
+ -[HMXPCClient dataSource]
+ -[HMXPCClient initWithConfiguration:userInfo:dataSource:]
+ -[HMXPCClientDataSource createXPCClientConnectionProxyWithUserInfo:refreshHandler:]
+ -[HMXPCClientDataSource createXPCConnectionWithMachServiceName:]
+ -[HMXPCClientDataSource darwinNotificationProvider]
+ -[HMXPCClientDataSource notificationCenter]
+ -[HMXPCConnection .cxx_destruct]
+ -[HMXPCConnection activate]
+ -[HMXPCConnection attributeDescriptions]
+ -[HMXPCConnection auditToken]
+ -[HMXPCConnection exportedInterface]
+ -[HMXPCConnection exportedObject]
+ -[HMXPCConnection initWithXPCConnection:]
+ -[HMXPCConnection interruptionHandler]
+ -[HMXPCConnection invalidate]
+ -[HMXPCConnection invalidationHandler]
+ -[HMXPCConnection processIdentifier]
+ -[HMXPCConnection processInfo]
+ -[HMXPCConnection queue]
+ -[HMXPCConnection remoteObjectInterface]
+ -[HMXPCConnection remoteObjectProxyWithErrorHandler:]
+ -[HMXPCConnection remoteObjectProxy]
+ -[HMXPCConnection resume]
+ -[HMXPCConnection setExportedInterface:]
+ -[HMXPCConnection setExportedObject:]
+ -[HMXPCConnection setInterruptionHandler:]
+ -[HMXPCConnection setInvalidationHandler:]
+ -[HMXPCConnection setQueue:]
+ -[HMXPCConnection setRemoteObjectInterface:]
+ -[HMXPCConnection synchronousRemoteObjectProxyWithErrorHandler:]
+ -[HMXPCConnection valueForEntitlement:]
+ -[HMXPCConnection xpcConnection]
+ GCC_except_table10001
+ GCC_except_table10003
+ GCC_except_table10066
+ GCC_except_table10098
+ GCC_except_table10100
+ GCC_except_table10104
+ GCC_except_table10121
+ GCC_except_table10123
+ GCC_except_table10129
+ GCC_except_table10133
+ GCC_except_table10136
+ GCC_except_table10143
+ GCC_except_table10147
+ GCC_except_table10165
+ GCC_except_table10168
+ GCC_except_table10176
+ GCC_except_table10179
+ GCC_except_table10181
+ GCC_except_table10183
+ GCC_except_table10195
+ GCC_except_table10205
+ GCC_except_table10408
+ GCC_except_table10421
+ GCC_except_table10470
+ GCC_except_table10475
+ GCC_except_table10479
+ GCC_except_table10487
+ GCC_except_table10544
+ GCC_except_table10547
+ GCC_except_table10548
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table10895
+ GCC_except_table1093
+ GCC_except_table10943
+ GCC_except_table10956
+ GCC_except_table1097
+ GCC_except_table1104
+ GCC_except_table11325
+ GCC_except_table11327
+ GCC_except_table11329
+ GCC_except_table11330
+ GCC_except_table11360
+ GCC_except_table11362
+ GCC_except_table11365
+ GCC_except_table11372
+ GCC_except_table11373
+ GCC_except_table11374
+ GCC_except_table11483
+ GCC_except_table11509
+ GCC_except_table11511
+ GCC_except_table11515
+ GCC_except_table11516
+ GCC_except_table11564
+ GCC_except_table11590
+ GCC_except_table11603
+ GCC_except_table11629
+ GCC_except_table11633
+ GCC_except_table11687
+ GCC_except_table11688
+ GCC_except_table11689
+ GCC_except_table11690
+ GCC_except_table11691
+ GCC_except_table11692
+ GCC_except_table11693
+ GCC_except_table11694
+ GCC_except_table11695
+ GCC_except_table11697
+ GCC_except_table11698
+ GCC_except_table11699
+ GCC_except_table11700
+ GCC_except_table11701
+ GCC_except_table11702
+ GCC_except_table11725
+ GCC_except_table11752
+ GCC_except_table11862
+ GCC_except_table11863
+ GCC_except_table11866
+ GCC_except_table11933
+ GCC_except_table11941
+ GCC_except_table11952
+ GCC_except_table11954
+ GCC_except_table11959
+ GCC_except_table1196
+ GCC_except_table11960
+ GCC_except_table11961
+ GCC_except_table1205
+ GCC_except_table12166
+ GCC_except_table12366
+ GCC_except_table12369
+ GCC_except_table12374
+ GCC_except_table12378
+ GCC_except_table12384
+ GCC_except_table12389
+ GCC_except_table12391
+ GCC_except_table12396
+ GCC_except_table12397
+ GCC_except_table12399
+ GCC_except_table12483
+ GCC_except_table12502
+ GCC_except_table12503
+ GCC_except_table12505
+ GCC_except_table12510
+ GCC_except_table12524
+ GCC_except_table12530
+ GCC_except_table12533
+ GCC_except_table12535
+ GCC_except_table12613
+ GCC_except_table12621
+ GCC_except_table12622
+ GCC_except_table12627
+ GCC_except_table12633
+ GCC_except_table12635
+ GCC_except_table12637
+ GCC_except_table12639
+ GCC_except_table12641
+ GCC_except_table12643
+ GCC_except_table12645
+ GCC_except_table1273
+ GCC_except_table1275
+ GCC_except_table12778
+ GCC_except_table1278
+ GCC_except_table1280
+ GCC_except_table1282
+ GCC_except_table12834
+ GCC_except_table12835
+ GCC_except_table12836
+ GCC_except_table12837
+ GCC_except_table12847
+ GCC_except_table12848
+ GCC_except_table1286
+ GCC_except_table12872
+ GCC_except_table12873
+ GCC_except_table12929
+ GCC_except_table12951
+ GCC_except_table12954
+ GCC_except_table13051
+ GCC_except_table13094
+ GCC_except_table13289
+ GCC_except_table13294
+ GCC_except_table13297
+ GCC_except_table1335
+ GCC_except_table13357
+ GCC_except_table13442
+ GCC_except_table13452
+ GCC_except_table13513
+ GCC_except_table13516
+ GCC_except_table13536
+ GCC_except_table13538
+ GCC_except_table13539
+ GCC_except_table1486
+ GCC_except_table1509
+ GCC_except_table1577
+ GCC_except_table1632
+ GCC_except_table1635
+ GCC_except_table1653
+ GCC_except_table1720
+ GCC_except_table1722
+ GCC_except_table1815
+ GCC_except_table1884
+ GCC_except_table1887
+ GCC_except_table1959
+ GCC_except_table2045
+ GCC_except_table2095
+ GCC_except_table2298
+ GCC_except_table2301
+ GCC_except_table2304
+ GCC_except_table2309
+ GCC_except_table2313
+ GCC_except_table2322
+ GCC_except_table2335
+ GCC_except_table2337
+ GCC_except_table2343
+ GCC_except_table2757
+ GCC_except_table2762
+ GCC_except_table2788
+ GCC_except_table2791
+ GCC_except_table2804
+ GCC_except_table2841
+ GCC_except_table2857
+ GCC_except_table2860
+ GCC_except_table2885
+ GCC_except_table2887
+ GCC_except_table2889
+ GCC_except_table2891
+ GCC_except_table3052
+ GCC_except_table3070
+ GCC_except_table3117
+ GCC_except_table3119
+ GCC_except_table3145
+ GCC_except_table3148
+ GCC_except_table3149
+ GCC_except_table3175
+ GCC_except_table3185
+ GCC_except_table3193
+ GCC_except_table3199
+ GCC_except_table3200
+ GCC_except_table3259
+ GCC_except_table3282
+ GCC_except_table3285
+ GCC_except_table3288
+ GCC_except_table3291
+ GCC_except_table3294
+ GCC_except_table3297
+ GCC_except_table3300
+ GCC_except_table3365
+ GCC_except_table3366
+ GCC_except_table3412
+ GCC_except_table3420
+ GCC_except_table3421
+ GCC_except_table3425
+ GCC_except_table3428
+ GCC_except_table3436
+ GCC_except_table3458
+ GCC_except_table3465
+ GCC_except_table3469
+ GCC_except_table3472
+ GCC_except_table3475
+ GCC_except_table3516
+ GCC_except_table3520
+ GCC_except_table3524
+ GCC_except_table3529
+ GCC_except_table3537
+ GCC_except_table3541
+ GCC_except_table3552
+ GCC_except_table3791
+ GCC_except_table3795
+ GCC_except_table3799
+ GCC_except_table3802
+ GCC_except_table3806
+ GCC_except_table3807
+ GCC_except_table3816
+ GCC_except_table3820
+ GCC_except_table3824
+ GCC_except_table3847
+ GCC_except_table3855
+ GCC_except_table3857
+ GCC_except_table3860
+ GCC_except_table3940
+ GCC_except_table3954
+ GCC_except_table3957
+ GCC_except_table3959
+ GCC_except_table3962
+ GCC_except_table3969
+ GCC_except_table4022
+ GCC_except_table4087
+ GCC_except_table4102
+ GCC_except_table4105
+ GCC_except_table4198
+ GCC_except_table4199
+ GCC_except_table4201
+ GCC_except_table4206
+ GCC_except_table4210
+ GCC_except_table4213
+ GCC_except_table4215
+ GCC_except_table4223
+ GCC_except_table4470
+ GCC_except_table4473
+ GCC_except_table4485
+ GCC_except_table4559
+ GCC_except_table4603
+ GCC_except_table4695
+ GCC_except_table4857
+ GCC_except_table4869
+ GCC_except_table4871
+ GCC_except_table4895
+ GCC_except_table4896
+ GCC_except_table4897
+ GCC_except_table4898
+ GCC_except_table4953
+ GCC_except_table4963
+ GCC_except_table5092
+ GCC_except_table5093
+ GCC_except_table514
+ GCC_except_table5169
+ GCC_except_table519
+ GCC_except_table525
+ GCC_except_table527
+ GCC_except_table5271
+ GCC_except_table5273
+ GCC_except_table5301
+ GCC_except_table5303
+ GCC_except_table5321
+ GCC_except_table5367
+ GCC_except_table5462
+ GCC_except_table5482
+ GCC_except_table5489
+ GCC_except_table5490
+ GCC_except_table5492
+ GCC_except_table5756
+ GCC_except_table5758
+ GCC_except_table5768
+ GCC_except_table5769
+ GCC_except_table5963
+ GCC_except_table5967
+ GCC_except_table6040
+ GCC_except_table6160
+ GCC_except_table6167
+ GCC_except_table6172
+ GCC_except_table6361
+ GCC_except_table6414
+ GCC_except_table6610
+ GCC_except_table6612
+ GCC_except_table6619
+ GCC_except_table6627
+ GCC_except_table6647
+ GCC_except_table6657
+ GCC_except_table6660
+ GCC_except_table6674
+ GCC_except_table6679
+ GCC_except_table6685
+ GCC_except_table6690
+ GCC_except_table6695
+ GCC_except_table6700
+ GCC_except_table6709
+ GCC_except_table6714
+ GCC_except_table6776
+ GCC_except_table6784
+ GCC_except_table6789
+ GCC_except_table6803
+ GCC_except_table6808
+ GCC_except_table6815
+ GCC_except_table6830
+ GCC_except_table6833
+ GCC_except_table6835
+ GCC_except_table6838
+ GCC_except_table6843
+ GCC_except_table685
+ GCC_except_table6850
+ GCC_except_table6859
+ GCC_except_table6893
+ GCC_except_table693
+ GCC_except_table6954
+ GCC_except_table6956
+ GCC_except_table6957
+ GCC_except_table697
+ GCC_except_table7095
+ GCC_except_table7102
+ GCC_except_table7187
+ GCC_except_table719
+ GCC_except_table7218
+ GCC_except_table7276
+ GCC_except_table7278
+ GCC_except_table7302
+ GCC_except_table7330
+ GCC_except_table7344
+ GCC_except_table736
+ GCC_except_table7360
+ GCC_except_table7366
+ GCC_except_table7405
+ GCC_except_table7407
+ GCC_except_table7412
+ GCC_except_table7425
+ GCC_except_table7426
+ GCC_except_table7431
+ GCC_except_table7450
+ GCC_except_table7452
+ GCC_except_table7477
+ GCC_except_table7491
+ GCC_except_table7509
+ GCC_except_table755
+ GCC_except_table7688
+ GCC_except_table7951
+ GCC_except_table7994
+ GCC_except_table805
+ GCC_except_table8054
+ GCC_except_table809
+ GCC_except_table8170
+ GCC_except_table8173
+ GCC_except_table8263
+ GCC_except_table8282
+ GCC_except_table8292
+ GCC_except_table8428
+ GCC_except_table8437
+ GCC_except_table8450
+ GCC_except_table8457
+ GCC_except_table8496
+ GCC_except_table8498
+ GCC_except_table8526
+ GCC_except_table8528
+ GCC_except_table8530
+ GCC_except_table8532
+ GCC_except_table8539
+ GCC_except_table8545
+ GCC_except_table8549
+ GCC_except_table8559
+ GCC_except_table8565
+ GCC_except_table8651
+ GCC_except_table8653
+ GCC_except_table8663
+ GCC_except_table8665
+ GCC_except_table8667
+ GCC_except_table8669
+ GCC_except_table8671
+ GCC_except_table8677
+ GCC_except_table8681
+ GCC_except_table8694
+ GCC_except_table8696
+ GCC_except_table8698
+ GCC_except_table8700
+ GCC_except_table8719
+ GCC_except_table875
+ GCC_except_table879
+ GCC_except_table880
+ GCC_except_table886
+ GCC_except_table8879
+ GCC_except_table8885
+ GCC_except_table8886
+ GCC_except_table8921
+ GCC_except_table8924
+ GCC_except_table8925
+ GCC_except_table8928
+ GCC_except_table893
+ GCC_except_table8931
+ GCC_except_table8932
+ GCC_except_table8976
+ GCC_except_table8977
+ GCC_except_table8984
+ GCC_except_table8987
+ GCC_except_table9006
+ GCC_except_table9079
+ GCC_except_table9080
+ GCC_except_table9117
+ GCC_except_table9302
+ GCC_except_table9303
+ GCC_except_table9307
+ GCC_except_table9362
+ GCC_except_table9383
+ GCC_except_table9465
+ GCC_except_table9473
+ GCC_except_table9520
+ GCC_except_table9534
+ GCC_except_table9550
+ GCC_except_table9578
+ GCC_except_table9756
+ GCC_except_table9800
+ GCC_except_table9801
+ GCC_except_table9836
+ GCC_except_table9869
+ GCC_except_table9872
+ GCC_except_table9875
+ GCC_except_table9877
+ GCC_except_table9938
+ GCC_except_table9958
+ GCC_except_table9959
+ GCC_except_table9960
+ GCC_except_table9999
+ _CoreAnalyticsLibraryCore.frameworkLibrary.40542
+ _CoreHAPLibraryCore.frameworkLibrary.32847
+ _HMAccessorySupportsAdaptiveTemperatureAutomationsMessage
+ _HMAccessorySupportsCleanEnergyAutomationsMessage
+ _HMDaemonDisconnectedNotification
+ _IDSFoundationLibraryCore.44862
+ _IDSFoundationLibraryCore.frameworkLibrary.44865
+ _OBJC_CLASS_$_HMXPCClientDataSource
+ _OBJC_CLASS_$_HMXPCConnection
+ _OBJC_IVAR_$_HMUserActionPredictionProvider._predictionDataSource
+ _OBJC_IVAR_$_HMUserActionPredictionProvider._shouldRefetchFromBackend
+ _OBJC_IVAR_$_HMXPCClient._dataSource
+ _OBJC_IVAR_$_HMXPCConnection._lock
+ _OBJC_IVAR_$_HMXPCConnection._xpcConnection
+ _OBJC_METACLASS_$_HMXPCClientDataSource
+ _OBJC_METACLASS_$_HMXPCConnection
+ _UIKitLibrary.45092
+ _UIKitLibraryCore.45088
+ _UIKitLibraryCore.frameworkLibrary.45101
+ __OBJC_$_CLASS_METHODS_HMCameraView
+ __OBJC_$_INSTANCE_METHODS_HMXPCClientDataSource
+ __OBJC_$_INSTANCE_METHODS_HMXPCConnection
+ __OBJC_$_INSTANCE_VARIABLES_HMXPCConnection
+ __OBJC_$_PROP_LIST_HMApplicationData.13115
+ __OBJC_$_PROP_LIST_HMUserActionPredictionDataSource
+ __OBJC_$_PROP_LIST_HMXPCClientDataSource
+ __OBJC_$_PROP_LIST_HMXPCClientDataSource.59
+ __OBJC_$_PROP_LIST_HMXPCConnection
+ __OBJC_$_PROP_LIST_HMXPCConnection.119
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMUserActionPredictionDataSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMXPCClientDataSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMXPCConnection
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMUserActionPredictionDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMXPCClientDataSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMXPCConnection
+ __OBJC_$_PROTOCOL_REFS_HMUserActionPredictionDataSource
+ __OBJC_$_PROTOCOL_REFS_HMXPCClientDataSource
+ __OBJC_$_PROTOCOL_REFS_HMXPCConnection
+ __OBJC_CLASS_PROTOCOLS_$_HMCameraView
+ __OBJC_CLASS_PROTOCOLS_$_HMXPCClientDataSource
+ __OBJC_CLASS_PROTOCOLS_$_HMXPCConnection
+ __OBJC_CLASS_RO_$_HMXPCClientDataSource
+ __OBJC_CLASS_RO_$_HMXPCConnection
+ __OBJC_LABEL_PROTOCOL_$_HMUserActionPredictionDataSource
+ __OBJC_LABEL_PROTOCOL_$_HMXPCClientDataSource
+ __OBJC_LABEL_PROTOCOL_$_HMXPCConnection
+ __OBJC_METACLASS_RO_$_HMXPCClientDataSource
+ __OBJC_METACLASS_RO_$_HMXPCConnection
+ __OBJC_PROTOCOL_$_HMUserActionPredictionDataSource
+ __OBJC_PROTOCOL_$_HMXPCClientDataSource
+ __OBJC_PROTOCOL_$_HMXPCConnection
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.783
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.785
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.793
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.795
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.788
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.796
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.792
+ ___25-[HMXPCClient connection]_block_invoke.78
+ ___25-[HMXPCClient connection]_block_invoke.79
+ ___25-[HMXPCClient connection]_block_invoke.80
+ ___25-[HMXPCClient connection]_block_invoke.81
+ ___27+[HMCameraView logCategory]_block_invoke
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1328
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1329
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1331
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1333
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1334
+ ___30-[HMAccessory _mergeServices:]_block_invoke.1120
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1122
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1123
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1142
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1145
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1147
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1150
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1154
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1159
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1293
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1295
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1298
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1307
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1309
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1312
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1314
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1316
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1317
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1124
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1143
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1146
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1148
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1151
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1155
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1160
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1294
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1296
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1301
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1304
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1315
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1319
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1162
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1320
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1163
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1322
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1164
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1323
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1287
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1325
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_7.1326
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.798
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.800
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1361
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1363
+ ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.87
+ ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.88
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1349
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1350
+ ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.764
+ ___57-[HMAccessory _mergeBulletinBoardNotificationByEndpoint:]_block_invoke.1117
+ ___57-[HMMigrationBoost _handleDaemonInterruptedNotification:]_block_invoke
+ ___57-[HMMigrationBoost _handleDaemonInterruptedNotification:]_block_invoke.4
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.1046
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.1048
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.857
+ ___75-[HMUserActionPredictionProvider fetchPredictionsFromBackendAndUpdateHomes]_block_invoke
+ ___76-[HMUserActionPredictionProvider _fetchPredictionsFromBackendAndUpdateHomes]_block_invoke
+ ___Block_byref_object_copy_.16364
+ ___Block_byref_object_copy_.16698
+ ___Block_byref_object_copy_.24325
+ ___Block_byref_object_copy_.26671
+ ___Block_byref_object_copy_.31305
+ ___Block_byref_object_copy_.32939
+ ___Block_byref_object_copy_.35117
+ ___Block_byref_object_copy_.40429
+ ___Block_byref_object_copy_.43899
+ ___Block_byref_object_copy_.63721
+ ___Block_byref_object_copy_.66089
+ ___Block_byref_object_dispose_.16365
+ ___Block_byref_object_dispose_.16699
+ ___Block_byref_object_dispose_.24326
+ ___Block_byref_object_dispose_.26672
+ ___Block_byref_object_dispose_.31306
+ ___Block_byref_object_dispose_.32940
+ ___Block_byref_object_dispose_.35118
+ ___Block_byref_object_dispose_.40430
+ ___Block_byref_object_dispose_.43900
+ ___Block_byref_object_dispose_.63722
+ ___Block_byref_object_dispose_.66090
+ ___CoreAnalyticsLibraryCore_block_invoke.40543
+ ___CoreHAPLibraryCore_block_invoke.32848
+ ___IDSFoundationLibraryCore_block_invoke.44866
+ ___UIKitLibraryCore_block_invoke.45102
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_52_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_literal_global.101.40550
+ ___block_literal_global.101.42744
+ ___block_literal_global.10427
+ ___block_literal_global.10701
+ ___block_literal_global.11295
+ ___block_literal_global.12.51283
+ ___block_literal_global.12009
+ ___block_literal_global.13047
+ ___block_literal_global.13168
+ ___block_literal_global.1345
+ ___block_literal_global.14149
+ ___block_literal_global.14290
+ ___block_literal_global.14365
+ ___block_literal_global.1453
+ ___block_literal_global.14612
+ ___block_literal_global.14986
+ ___block_literal_global.15214
+ ___block_literal_global.15802
+ ___block_literal_global.16155
+ ___block_literal_global.16450
+ ___block_literal_global.17.19938
+ ___block_literal_global.17079
+ ___block_literal_global.18284
+ ___block_literal_global.18820
+ ___block_literal_global.19.16140
+ ___block_literal_global.19001
+ ___block_literal_global.19134
+ ___block_literal_global.19293
+ ___block_literal_global.1971
+ ___block_literal_global.19945
+ ___block_literal_global.20615
+ ___block_literal_global.21079
+ ___block_literal_global.21718
+ ___block_literal_global.22085
+ ___block_literal_global.23057
+ ___block_literal_global.23363
+ ___block_literal_global.23697
+ ___block_literal_global.24363
+ ___block_literal_global.24552
+ ___block_literal_global.24750
+ ___block_literal_global.2492
+ ___block_literal_global.25278
+ ___block_literal_global.25522
+ ___block_literal_global.25897
+ ___block_literal_global.26035
+ ___block_literal_global.26282
+ ___block_literal_global.26529
+ ___block_literal_global.26696
+ ___block_literal_global.26789
+ ___block_literal_global.27519
+ ___block_literal_global.29436
+ ___block_literal_global.29596
+ ___block_literal_global.29877
+ ___block_literal_global.30.19927
+ ___block_literal_global.31157
+ ___block_literal_global.31425
+ ___block_literal_global.31764
+ ___block_literal_global.32023
+ ___block_literal_global.32308
+ ___block_literal_global.32388
+ ___block_literal_global.33.65426
+ ___block_literal_global.33083
+ ___block_literal_global.33581
+ ___block_literal_global.33851
+ ___block_literal_global.34903
+ ___block_literal_global.35140
+ ___block_literal_global.35442
+ ___block_literal_global.36
+ ___block_literal_global.36756
+ ___block_literal_global.37732
+ ___block_literal_global.37966
+ ___block_literal_global.38194
+ ___block_literal_global.38590
+ ___block_literal_global.39340
+ ___block_literal_global.3955
+ ___block_literal_global.40537
+ ___block_literal_global.40787
+ ___block_literal_global.41126
+ ___block_literal_global.41792
+ ___block_literal_global.42754
+ ___block_literal_global.4293
+ ___block_literal_global.43018
+ ___block_literal_global.43287
+ ___block_literal_global.43571
+ ___block_literal_global.43791
+ ___block_literal_global.4380
+ ___block_literal_global.4472
+ ___block_literal_global.44927
+ ___block_literal_global.45020
+ ___block_literal_global.45727
+ ___block_literal_global.45919
+ ___block_literal_global.47102
+ ___block_literal_global.475
+ ___block_literal_global.47553
+ ___block_literal_global.47877
+ ___block_literal_global.48643
+ ___block_literal_global.49300
+ ___block_literal_global.49658
+ ___block_literal_global.50932
+ ___block_literal_global.51
+ ___block_literal_global.51295
+ ___block_literal_global.51579
+ ___block_literal_global.51775
+ ___block_literal_global.52005
+ ___block_literal_global.52722
+ ___block_literal_global.52842
+ ___block_literal_global.5333
+ ___block_literal_global.53597
+ ___block_literal_global.53831
+ ___block_literal_global.54286
+ ___block_literal_global.54547
+ ___block_literal_global.55630
+ ___block_literal_global.57943
+ ___block_literal_global.58.37961
+ ___block_literal_global.58807
+ ___block_literal_global.5924
+ ___block_literal_global.60096
+ ___block_literal_global.60824
+ ___block_literal_global.61377
+ ___block_literal_global.61688
+ ___block_literal_global.62205
+ ___block_literal_global.62382
+ ___block_literal_global.62774
+ ___block_literal_global.63022
+ ___block_literal_global.6337
+ ___block_literal_global.6474
+ ___block_literal_global.64829
+ ___block_literal_global.65165
+ ___block_literal_global.65432
+ ___block_literal_global.65790
+ ___block_literal_global.66028
+ ___block_literal_global.66384
+ ___block_literal_global.6704
+ ___block_literal_global.7.24563
+ ___block_literal_global.7192
+ ___block_literal_global.73.24723
+ ___block_literal_global.7559
+ ___block_literal_global.7891
+ ___block_literal_global.8149
+ ___block_literal_global.84.40731
+ ___block_literal_global.861
+ ___block_literal_global.8733
+ ___block_literal_global.8973
+ ___block_literal_global.9375
+ ___block_literal_global.9991
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.40540
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.45097
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.45091
+ _audit_stringCoreAnalytics.40546
+ _audit_stringCoreHAP.32850
+ _audit_stringIDSFoundation.44868
+ _audit_stringUIKit.45104
+ _getAnalyticsSendEventLazySymbolLoc.ptr.40539
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.45096
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.45090
+ _logCategory._hmf_once_t0.14364
+ _logCategory._hmf_once_t0.23362
+ _logCategory._hmf_once_t0.24749
+ _logCategory._hmf_once_t0.32022
+ _logCategory._hmf_once_t0.32387
+ _logCategory._hmf_once_t0.43570
+ _logCategory._hmf_once_t0.45726
+ _logCategory._hmf_once_t0.45918
+ _logCategory._hmf_once_t0.63021
+ _logCategory._hmf_once_t1.19133
+ _logCategory._hmf_once_t1.21078
+ _logCategory._hmf_once_t1.40763
+ _logCategory._hmf_once_t1.47101
+ _logCategory._hmf_once_t1.51282
+ _logCategory._hmf_once_t1.52841
+ _logCategory._hmf_once_t1.57942
+ _logCategory._hmf_once_t11.13046
+ _logCategory._hmf_once_t13.42743
+ _logCategory._hmf_once_t14.62773
+ _logCategory._hmf_once_t16.31424
+ _logCategory._hmf_once_t16.37965
+ _logCategory._hmf_once_t16.64828
+ _logCategory._hmf_once_t2.24562
+ _logCategory._hmf_once_t2.26695
+ _logCategory._hmf_once_t2.29876
+ _logCategory._hmf_once_t2.33580
+ _logCategory._hmf_once_t20.25290
+ _logCategory._hmf_once_t20.26281
+ _logCategory._hmf_once_t21.62381
+ _logCategory._hmf_once_t24.41125
+ _logCategory._hmf_once_t24.41791
+ _logCategory._hmf_once_t25.26528
+ _logCategory._hmf_once_t25.65789
+ _logCategory._hmf_once_t27.61687
+ _logCategory._hmf_once_t3.43017
+ _logCategory._hmf_once_t3.53820
+ _logCategory._hmf_once_t3.65425
+ _logCategory._hmf_once_t31.24362
+ _logCategory._hmf_once_t31.54285
+ _logCategory._hmf_once_t31.66383
+ _logCategory._hmf_once_t32.53596
+ _logCategory._hmf_once_t34.20614
+ _logCategory._hmf_once_t37.54573
+ _logCategory._hmf_once_t379
+ _logCategory._hmf_once_t4.14611
+ _logCategory._hmf_once_t4.1464
+ _logCategory._hmf_once_t4.6336
+ _logCategory._hmf_once_t44.26551
+ _logCategory._hmf_once_t44.32307
+ _logCategory._hmf_once_t5.18819
+ _logCategory._hmf_once_t51.43286
+ _logCategory._hmf_once_t6.34902
+ _logCategory._hmf_once_t6.37731
+ _logCategory._hmf_once_t6.43790
+ _logCategory._hmf_once_t6.49299
+ _logCategory._hmf_once_t6.58806
+ _logCategory._hmf_once_t7.52721
+ _logCategory._hmf_once_t8.38193
+ _logCategory._hmf_once_t8.48642
+ _logCategory._hmf_once_t8.51793
+ _logCategory._hmf_once_t9.29595
+ _logCategory._hmf_once_v1.14366
+ _logCategory._hmf_once_v1.23364
+ _logCategory._hmf_once_v1.24751
+ _logCategory._hmf_once_v1.32024
+ _logCategory._hmf_once_v1.32389
+ _logCategory._hmf_once_v1.43572
+ _logCategory._hmf_once_v1.45728
+ _logCategory._hmf_once_v1.45920
+ _logCategory._hmf_once_v1.63023
+ _logCategory._hmf_once_v10.29597
+ _logCategory._hmf_once_v12.13048
+ _logCategory._hmf_once_v14.42745
+ _logCategory._hmf_once_v15.62775
+ _logCategory._hmf_once_v17.31426
+ _logCategory._hmf_once_v17.37967
+ _logCategory._hmf_once_v17.64830
+ _logCategory._hmf_once_v2.19135
+ _logCategory._hmf_once_v2.21080
+ _logCategory._hmf_once_v2.40764
+ _logCategory._hmf_once_v2.47103
+ _logCategory._hmf_once_v2.51284
+ _logCategory._hmf_once_v2.52843
+ _logCategory._hmf_once_v2.57944
+ _logCategory._hmf_once_v21.25291
+ _logCategory._hmf_once_v21.26283
+ _logCategory._hmf_once_v22.62383
+ _logCategory._hmf_once_v25.41127
+ _logCategory._hmf_once_v25.41793
+ _logCategory._hmf_once_v26.26530
+ _logCategory._hmf_once_v26.65791
+ _logCategory._hmf_once_v28.61689
+ _logCategory._hmf_once_v3.24564
+ _logCategory._hmf_once_v3.26697
+ _logCategory._hmf_once_v3.29878
+ _logCategory._hmf_once_v3.33582
+ _logCategory._hmf_once_v32.24364
+ _logCategory._hmf_once_v32.54287
+ _logCategory._hmf_once_v32.66385
+ _logCategory._hmf_once_v33.53598
+ _logCategory._hmf_once_v35.20616
+ _logCategory._hmf_once_v38.54574
+ _logCategory._hmf_once_v380
+ _logCategory._hmf_once_v4.43019
+ _logCategory._hmf_once_v4.53821
+ _logCategory._hmf_once_v4.65427
+ _logCategory._hmf_once_v45.26552
+ _logCategory._hmf_once_v45.32309
+ _logCategory._hmf_once_v5.14613
+ _logCategory._hmf_once_v5.1465
+ _logCategory._hmf_once_v5.6338
+ _logCategory._hmf_once_v52.43288
+ _logCategory._hmf_once_v6.18821
+ _logCategory._hmf_once_v7.34904
+ _logCategory._hmf_once_v7.37733
+ _logCategory._hmf_once_v7.43792
+ _logCategory._hmf_once_v7.49301
+ _logCategory._hmf_once_v7.58808
+ _logCategory._hmf_once_v8.52723
+ _logCategory._hmf_once_v9.38195
+ _logCategory._hmf_once_v9.48644
+ _logCategory._hmf_once_v9.51794
+ _objc_msgSend$_queue
+ _objc_msgSend$auditToken
+ _objc_msgSend$createXPCClientConnectionProxyWithUserInfo:refreshHandler:
+ _objc_msgSend$createXPCConnectionWithMachServiceName:
+ _objc_msgSend$exportedObject
+ _objc_msgSend$fetchPredictionsFromBackendWithCompletion:
+ _objc_msgSend$initWithConfiguration:userInfo:dataSource:
+ _objc_msgSend$initWithWorkQueue:messageDispatcher:UUID:dataSource:predictionDataSource:predictionTransformer:darwinNotificationProvider:
+ _objc_msgSend$initWithXPCConnection:
+ _objc_msgSend$interruptionHandler
+ _objc_msgSend$invalidationHandler
+ _objc_msgSend$predictionDataSource
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$remoteObjectProxy
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$xpcConnection
+ _sharedInstance.onceToken.42753
+ _sharedManager.onceToken.61834
+ _supportedValueClasses.onceToken.51578
+ _supportedValueClasses.onceToken.60058
+ _supportedValueClasses.supportedValueClasses.51580
+ _supportedValueClasses.supportedValueClasses.60059
- -[HMAccessory handleRuntimeStateUpdate:completionHandler:]
- -[HMHomeManager(HMHomeManagerAdaptive) sendHomecommsdLunchboxWithCompletionHandler:]
- -[HMMigrationBoost _handleDaemonDisconnect:]
- -[HMUserActionPredictionDuetDataSource fetchPredictionsFromDuet]
- -[HMUserActionPredictionProvider _fetchPredictionsFromDuetAndUpdateHomes]
- -[HMUserActionPredictionProvider duetDataSource]
- -[HMUserActionPredictionProvider initWithWorkQueue:messageDispatcher:UUID:dataSource:duetDataSource:predictionTransformer:darwinNotificationProvider:]
- GCC_except_table10038
- GCC_except_table10070
- GCC_except_table10072
- GCC_except_table10076
- GCC_except_table10093
- GCC_except_table10095
- GCC_except_table10101
- GCC_except_table10105
- GCC_except_table10108
- GCC_except_table10115
- GCC_except_table10119
- GCC_except_table10125
- GCC_except_table10137
- GCC_except_table10140
- GCC_except_table10148
- GCC_except_table10149
- GCC_except_table10151
- GCC_except_table10155
- GCC_except_table10167
- GCC_except_table10380
- GCC_except_table10393
- GCC_except_table10442
- GCC_except_table10447
- GCC_except_table10451
- GCC_except_table10459
- GCC_except_table10516
- GCC_except_table10519
- GCC_except_table10520
- GCC_except_table10867
- GCC_except_table10915
- GCC_except_table10928
- GCC_except_table1094
- GCC_except_table1098
- GCC_except_table110
- GCC_except_table1105
- GCC_except_table111
- GCC_except_table11297
- GCC_except_table11299
- GCC_except_table11301
- GCC_except_table11302
- GCC_except_table11332
- GCC_except_table11334
- GCC_except_table11336
- GCC_except_table11343
- GCC_except_table11344
- GCC_except_table11345
- GCC_except_table11453
- GCC_except_table11454
- GCC_except_table11480
- GCC_except_table11486
- GCC_except_table11487
- GCC_except_table11535
- GCC_except_table11561
- GCC_except_table11574
- GCC_except_table11600
- GCC_except_table11604
- GCC_except_table11658
- GCC_except_table11659
- GCC_except_table11660
- GCC_except_table11661
- GCC_except_table11662
- GCC_except_table11663
- GCC_except_table11664
- GCC_except_table11665
- GCC_except_table11666
- GCC_except_table11667
- GCC_except_table11668
- GCC_except_table11669
- GCC_except_table11670
- GCC_except_table11671
- GCC_except_table11672
- GCC_except_table11673
- GCC_except_table11723
- GCC_except_table11833
- GCC_except_table11834
- GCC_except_table11837
- GCC_except_table11902
- GCC_except_table11904
- GCC_except_table11912
- GCC_except_table11923
- GCC_except_table11925
- GCC_except_table11930
- GCC_except_table11932
- GCC_except_table1197
- GCC_except_table1206
- GCC_except_table12137
- GCC_except_table12337
- GCC_except_table12340
- GCC_except_table12345
- GCC_except_table12349
- GCC_except_table12355
- GCC_except_table12360
- GCC_except_table12362
- GCC_except_table12367
- GCC_except_table12368
- GCC_except_table12370
- GCC_except_table12452
- GCC_except_table12454
- GCC_except_table12473
- GCC_except_table12474
- GCC_except_table12475
- GCC_except_table12476
- GCC_except_table12495
- GCC_except_table12501
- GCC_except_table12506
- GCC_except_table12584
- GCC_except_table12592
- GCC_except_table12593
- GCC_except_table12598
- GCC_except_table12604
- GCC_except_table12606
- GCC_except_table12608
- GCC_except_table12610
- GCC_except_table12612
- GCC_except_table12614
- GCC_except_table12616
- GCC_except_table1274
- GCC_except_table12749
- GCC_except_table1276
- GCC_except_table1279
- GCC_except_table12805
- GCC_except_table12806
- GCC_except_table12807
- GCC_except_table12808
- GCC_except_table1281
- GCC_except_table12818
- GCC_except_table12819
- GCC_except_table1283
- GCC_except_table12843
- GCC_except_table12844
- GCC_except_table1287
- GCC_except_table12900
- GCC_except_table12922
- GCC_except_table12925
- GCC_except_table13022
- GCC_except_table13065
- GCC_except_table13260
- GCC_except_table13265
- GCC_except_table13268
- GCC_except_table13328
- GCC_except_table1336
- GCC_except_table13413
- GCC_except_table13423
- GCC_except_table13484
- GCC_except_table13487
- GCC_except_table13507
- GCC_except_table13509
- GCC_except_table13510
- GCC_except_table1487
- GCC_except_table1510
- GCC_except_table1578
- GCC_except_table1633
- GCC_except_table1636
- GCC_except_table1654
- GCC_except_table1721
- GCC_except_table1723
- GCC_except_table1816
- GCC_except_table1885
- GCC_except_table1888
- GCC_except_table1960
- GCC_except_table2047
- GCC_except_table2096
- GCC_except_table2299
- GCC_except_table2302
- GCC_except_table2305
- GCC_except_table2310
- GCC_except_table2314
- GCC_except_table2323
- GCC_except_table2336
- GCC_except_table2339
- GCC_except_table2347
- GCC_except_table2758
- GCC_except_table2763
- GCC_except_table2789
- GCC_except_table2792
- GCC_except_table2805
- GCC_except_table2842
- GCC_except_table2858
- GCC_except_table2861
- GCC_except_table2886
- GCC_except_table2888
- GCC_except_table2890
- GCC_except_table2892
- GCC_except_table3053
- GCC_except_table3072
- GCC_except_table3118
- GCC_except_table3120
- GCC_except_table3141
- GCC_except_table3146
- GCC_except_table3147
- GCC_except_table3171
- GCC_except_table3181
- GCC_except_table3190
- GCC_except_table3191
- GCC_except_table3195
- GCC_except_table3257
- GCC_except_table3280
- GCC_except_table3283
- GCC_except_table3286
- GCC_except_table3289
- GCC_except_table3292
- GCC_except_table3295
- GCC_except_table3298
- GCC_except_table3363
- GCC_except_table3364
- GCC_except_table3410
- GCC_except_table3417
- GCC_except_table3418
- GCC_except_table3422
- GCC_except_table3423
- GCC_except_table3434
- GCC_except_table3456
- GCC_except_table3463
- GCC_except_table3467
- GCC_except_table3470
- GCC_except_table3473
- GCC_except_table3514
- GCC_except_table3518
- GCC_except_table3522
- GCC_except_table3527
- GCC_except_table3535
- GCC_except_table3539
- GCC_except_table3548
- GCC_except_table3785
- GCC_except_table3789
- GCC_except_table3793
- GCC_except_table3796
- GCC_except_table3800
- GCC_except_table3801
- GCC_except_table3804
- GCC_except_table3814
- GCC_except_table3818
- GCC_except_table3841
- GCC_except_table3843
- GCC_except_table3845
- GCC_except_table3848
- GCC_except_table3934
- GCC_except_table3948
- GCC_except_table3951
- GCC_except_table3953
- GCC_except_table3956
- GCC_except_table3963
- GCC_except_table4016
- GCC_except_table4081
- GCC_except_table4096
- GCC_except_table4099
- GCC_except_table4192
- GCC_except_table4193
- GCC_except_table4195
- GCC_except_table4200
- GCC_except_table4204
- GCC_except_table4207
- GCC_except_table4209
- GCC_except_table4217
- GCC_except_table4464
- GCC_except_table4467
- GCC_except_table4479
- GCC_except_table4553
- GCC_except_table4597
- GCC_except_table4689
- GCC_except_table4851
- GCC_except_table4863
- GCC_except_table4865
- GCC_except_table4889
- GCC_except_table4890
- GCC_except_table4891
- GCC_except_table4892
- GCC_except_table4947
- GCC_except_table4957
- GCC_except_table5086
- GCC_except_table5087
- GCC_except_table5163
- GCC_except_table520
- GCC_except_table522
- GCC_except_table5265
- GCC_except_table5267
- GCC_except_table5295
- GCC_except_table5297
- GCC_except_table530
- GCC_except_table531
- GCC_except_table5315
- GCC_except_table5361
- GCC_except_table5456
- GCC_except_table5476
- GCC_except_table5477
- GCC_except_table5478
- GCC_except_table5480
- GCC_except_table5744
- GCC_except_table5752
- GCC_except_table5762
- GCC_except_table5763
- GCC_except_table5957
- GCC_except_table5961
- GCC_except_table6034
- GCC_except_table6154
- GCC_except_table6161
- GCC_except_table6166
- GCC_except_table6357
- GCC_except_table6410
- GCC_except_table6606
- GCC_except_table6608
- GCC_except_table6615
- GCC_except_table6623
- GCC_except_table6643
- GCC_except_table6653
- GCC_except_table6656
- GCC_except_table6670
- GCC_except_table6675
- GCC_except_table6681
- GCC_except_table6686
- GCC_except_table6691
- GCC_except_table6696
- GCC_except_table6701
- GCC_except_table6710
- GCC_except_table6768
- GCC_except_table6780
- GCC_except_table6785
- GCC_except_table6799
- GCC_except_table6804
- GCC_except_table6811
- GCC_except_table6826
- GCC_except_table6827
- GCC_except_table6829
- GCC_except_table6834
- GCC_except_table6839
- GCC_except_table6846
- GCC_except_table6851
- GCC_except_table6889
- GCC_except_table691
- GCC_except_table6946
- GCC_except_table6952
- GCC_except_table6953
- GCC_except_table699
- GCC_except_table700
- GCC_except_table7091
- GCC_except_table7098
- GCC_except_table7183
- GCC_except_table7214
- GCC_except_table722
- GCC_except_table7270
- GCC_except_table7272
- GCC_except_table7298
- GCC_except_table7326
- GCC_except_table7340
- GCC_except_table7356
- GCC_except_table7362
- GCC_except_table7373
- GCC_except_table7375
- GCC_except_table739
- GCC_except_table7408
- GCC_except_table7421
- GCC_except_table7422
- GCC_except_table7427
- GCC_except_table7446
- GCC_except_table7448
- GCC_except_table7473
- GCC_except_table7487
- GCC_except_table7505
- GCC_except_table758
- GCC_except_table7686
- GCC_except_table7949
- GCC_except_table7992
- GCC_except_table8052
- GCC_except_table811
- GCC_except_table812
- GCC_except_table8168
- GCC_except_table8171
- GCC_except_table8261
- GCC_except_table8280
- GCC_except_table8290
- GCC_except_table8427
- GCC_except_table8436
- GCC_except_table8449
- GCC_except_table8456
- GCC_except_table8495
- GCC_except_table8497
- GCC_except_table8525
- GCC_except_table8527
- GCC_except_table8529
- GCC_except_table8531
- GCC_except_table8538
- GCC_except_table8544
- GCC_except_table8548
- GCC_except_table8558
- GCC_except_table8564
- GCC_except_table8648
- GCC_except_table8650
- GCC_except_table8660
- GCC_except_table8662
- GCC_except_table8664
- GCC_except_table8666
- GCC_except_table8668
- GCC_except_table8674
- GCC_except_table8678
- GCC_except_table8691
- GCC_except_table8693
- GCC_except_table8695
- GCC_except_table8697
- GCC_except_table8716
- GCC_except_table877
- GCC_except_table885
- GCC_except_table887
- GCC_except_table8874
- GCC_except_table8877
- GCC_except_table888
- GCC_except_table8883
- GCC_except_table8919
- GCC_except_table8922
- GCC_except_table8923
- GCC_except_table8926
- GCC_except_table8929
- GCC_except_table8930
- GCC_except_table895
- GCC_except_table8973
- GCC_except_table8974
- GCC_except_table8982
- GCC_except_table8983
- GCC_except_table9004
- GCC_except_table9076
- GCC_except_table9077
- GCC_except_table9115
- GCC_except_table9299
- GCC_except_table9300
- GCC_except_table9305
- GCC_except_table9360
- GCC_except_table9381
- GCC_except_table9457
- GCC_except_table9471
- GCC_except_table9518
- GCC_except_table9530
- GCC_except_table9548
- GCC_except_table9576
- GCC_except_table9750
- GCC_except_table9808
- GCC_except_table9841
- GCC_except_table9844
- GCC_except_table9847
- GCC_except_table9849
- GCC_except_table9910
- GCC_except_table9930
- GCC_except_table9931
- GCC_except_table9932
- GCC_except_table9971
- GCC_except_table9973
- GCC_except_table9975
- _CoreAnalyticsLibraryCore.frameworkLibrary.40385
- _CoreHAPLibraryCore.frameworkLibrary.32690
- _HMHomeManagerSendHomecommsdLunchboxRequestMessage
- _IDSFoundationLibraryCore.44566
- _IDSFoundationLibraryCore.frameworkLibrary.44569
- _OBJC_IVAR_$_HMUserActionPredictionProvider._duetDataSource
- _OBJC_IVAR_$_HMUserActionPredictionProvider._shouldRefetchFromDuet
- _UIKitLibrary.44797
- _UIKitLibraryCore.44793
- _UIKitLibraryCore.frameworkLibrary.44806
- __OBJC_$_PROP_LIST_HMApplicationData.13102
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.788
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.792
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.796
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.798
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.797
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.799
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.795
- ___25-[HMXPCClient connection]_block_invoke.73
- ___25-[HMXPCClient connection]_block_invoke.75
- ___25-[HMXPCClient connection]_block_invoke.76
- ___25-[HMXPCClient connection]_block_invoke.77
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1322
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1323
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1325
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1327
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1328
- ___30-[HMAccessory _mergeServices:]_block_invoke.1114
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1116
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1117
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1121
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1124
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1141
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1144
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1148
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1153
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1287
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1289
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1291
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1292
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1294
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1299
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1301
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1302
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1304
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1118
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1122
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1125
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1142
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1145
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1149
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1154
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1288
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1290
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1295
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1298
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1309
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1313
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1150
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1314
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1151
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1316
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1158
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1317
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1281
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1319
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_7.1320
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.801
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.803
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1355
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1357
- ___44-[HMMigrationBoost _handleDaemonDisconnect:]_block_invoke
- ___44-[HMMigrationBoost _handleDaemonDisconnect:]_block_invoke.4
- ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.83
- ___45-[HMXPCClient sendMessage:completionHandler:]_block_invoke.84
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1343
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1344
- ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.767
- ___57-[HMAccessory _mergeBulletinBoardNotificationByEndpoint:]_block_invoke.1111
- ___58-[HMAccessory handleRuntimeStateUpdate:completionHandler:]_block_invoke
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.1040
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.1042
- ___67-[HMPersonManager fetchFaceprintsForFaceCropsWithUUIDs:completion:]_block_invoke.154
- ___67-[HMPersonManager fetchFaceprintsForFaceCropsWithUUIDs:completion:]_block_invoke.156
- ___67-[HMPersonManager fetchFaceprintsForFaceCropsWithUUIDs:completion:]_block_invoke.157
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.860
- ___72-[HMUserActionPredictionProvider fetchPredictionsFromDuetAndUpdateHomes]_block_invoke
- ___78-[HMCameraObjectFetchServer sendCurrentlyBatchedFetchedObjectsWithCompletion:]_block_invoke_2
- ___84-[HMHomeManager(HMHomeManagerAdaptive) sendHomecommsdLunchboxWithCompletionHandler:]_block_invoke
- ___Block_byref_object_copy_.16292
- ___Block_byref_object_copy_.16629
- ___Block_byref_object_copy_.24185
- ___Block_byref_object_copy_.26524
- ___Block_byref_object_copy_.31151
- ___Block_byref_object_copy_.32788
- ___Block_byref_object_copy_.34962
- ___Block_byref_object_copy_.40272
- ___Block_byref_object_copy_.43602
- ___Block_byref_object_copy_.63425
- ___Block_byref_object_copy_.65790
- ___Block_byref_object_dispose_.16293
- ___Block_byref_object_dispose_.16630
- ___Block_byref_object_dispose_.24186
- ___Block_byref_object_dispose_.26525
- ___Block_byref_object_dispose_.31152
- ___Block_byref_object_dispose_.32789
- ___Block_byref_object_dispose_.34963
- ___Block_byref_object_dispose_.40273
- ___Block_byref_object_dispose_.43603
- ___Block_byref_object_dispose_.63426
- ___Block_byref_object_dispose_.65791
- ___CoreAnalyticsLibraryCore_block_invoke.40386
- ___CoreHAPLibraryCore_block_invoke.32691
- ___IDSFoundationLibraryCore_block_invoke.44570
- ___UIKitLibraryCore_block_invoke.44807
- _____handleAccessoryRuntimeStateUpdate_block_invoke
- _____handleAccessoryRuntimeStateUpdate_block_invoke_2
- ___block_descriptor_44_e8_32s_e17_v16?0"NSError"8ls32l8
- ___block_descriptor_44_e8_32s_e5_v8?0ls32l8
- ___block_literal_global.101.40393
- ___block_literal_global.101.42587
- ___block_literal_global.10419
- ___block_literal_global.10692
- ___block_literal_global.11282
- ___block_literal_global.11996
- ___block_literal_global.12.50982
- ___block_literal_global.13034
- ___block_literal_global.13155
- ___block_literal_global.1339
- ___block_literal_global.14138
- ___block_literal_global.14279
- ___block_literal_global.14354
- ___block_literal_global.1454
- ___block_literal_global.14911
- ___block_literal_global.15140
- ___block_literal_global.15729
- ___block_literal_global.16081
- ___block_literal_global.16378
- ___block_literal_global.17.19795
- ___block_literal_global.17011
- ___block_literal_global.18141
- ___block_literal_global.18678
- ___block_literal_global.18859
- ___block_literal_global.18992
- ___block_literal_global.19.16066
- ___block_literal_global.19151
- ___block_literal_global.1972
- ___block_literal_global.19802
- ___block_literal_global.20472
- ___block_literal_global.20937
- ___block_literal_global.21576
- ___block_literal_global.21943
- ___block_literal_global.22917
- ___block_literal_global.23223
- ___block_literal_global.23557
- ___block_literal_global.24223
- ___block_literal_global.24412
- ___block_literal_global.24609
- ___block_literal_global.2478
- ___block_literal_global.25135
- ___block_literal_global.25381
- ___block_literal_global.25751
- ___block_literal_global.25889
- ___block_literal_global.26137
- ___block_literal_global.26383
- ___block_literal_global.26549
- ___block_literal_global.26642
- ___block_literal_global.27370
- ___block_literal_global.29286
- ___block_literal_global.29445
- ___block_literal_global.29726
- ___block_literal_global.30.19784
- ___block_literal_global.31003
- ___block_literal_global.31269
- ___block_literal_global.31606
- ___block_literal_global.31865
- ___block_literal_global.32150
- ___block_literal_global.32230
- ___block_literal_global.32932
- ___block_literal_global.33.65127
- ___block_literal_global.33429
- ___block_literal_global.33699
- ___block_literal_global.34748
- ___block_literal_global.34985
- ___block_literal_global.35
- ___block_literal_global.35287
- ___block_literal_global.36593
- ___block_literal_global.37575
- ___block_literal_global.37809
- ___block_literal_global.38037
- ___block_literal_global.38433
- ___block_literal_global.39183
- ___block_literal_global.3938
- ___block_literal_global.40380
- ___block_literal_global.40631
- ___block_literal_global.40970
- ___block_literal_global.41635
- ___block_literal_global.42597
- ___block_literal_global.42721
- ___block_literal_global.4277
- ___block_literal_global.42990
- ___block_literal_global.43274
- ___block_literal_global.43494
- ___block_literal_global.4364
- ___block_literal_global.4456
- ___block_literal_global.44631
- ___block_literal_global.44725
- ___block_literal_global.45432
- ___block_literal_global.45624
- ___block_literal_global.46807
- ___block_literal_global.47254
- ___block_literal_global.474
- ___block_literal_global.47576
- ___block_literal_global.48342
- ___block_literal_global.48999
- ___block_literal_global.49357
- ___block_literal_global.50
- ___block_literal_global.50631
- ___block_literal_global.50994
- ___block_literal_global.51278
- ___block_literal_global.51474
- ___block_literal_global.51703
- ___block_literal_global.52420
- ___block_literal_global.52540
- ___block_literal_global.5318
- ___block_literal_global.53295
- ___block_literal_global.53529
- ___block_literal_global.53984
- ___block_literal_global.54246
- ___block_literal_global.55330
- ___block_literal_global.57646
- ___block_literal_global.58.37804
- ___block_literal_global.58510
- ___block_literal_global.5902
- ___block_literal_global.59801
- ___block_literal_global.60528
- ___block_literal_global.61081
- ___block_literal_global.61392
- ___block_literal_global.61909
- ___block_literal_global.62086
- ___block_literal_global.62478
- ___block_literal_global.62726
- ___block_literal_global.6321
- ___block_literal_global.64530
- ___block_literal_global.6458
- ___block_literal_global.64866
- ___block_literal_global.65133
- ___block_literal_global.65491
- ___block_literal_global.65729
- ___block_literal_global.66085
- ___block_literal_global.6688
- ___block_literal_global.7.24423
- ___block_literal_global.7183
- ___block_literal_global.73.24583
- ___block_literal_global.7554
- ___block_literal_global.7887
- ___block_literal_global.8141
- ___block_literal_global.84.40574
- ___block_literal_global.864
- ___block_literal_global.8721
- ___block_literal_global.8962
- ___block_literal_global.9364
- ___block_literal_global.9987
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.40383
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.44802
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.44796
- _audit_stringCoreAnalytics.40389
- _audit_stringCoreHAP.32693
- _audit_stringIDSFoundation.44572
- _audit_stringUIKit.44809
- _getAnalyticsSendEventLazySymbolLoc.ptr.40382
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.44801
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.44795
- _logCategory._hmf_once_t0.14353
- _logCategory._hmf_once_t0.23222
- _logCategory._hmf_once_t0.24608
- _logCategory._hmf_once_t0.31864
- _logCategory._hmf_once_t0.32229
- _logCategory._hmf_once_t0.43273
- _logCategory._hmf_once_t0.45431
- _logCategory._hmf_once_t0.45623
- _logCategory._hmf_once_t0.62725
- _logCategory._hmf_once_t1.18991
- _logCategory._hmf_once_t1.20936
- _logCategory._hmf_once_t1.40607
- _logCategory._hmf_once_t1.46806
- _logCategory._hmf_once_t1.50981
- _logCategory._hmf_once_t1.52539
- _logCategory._hmf_once_t1.57645
- _logCategory._hmf_once_t11.13033
- _logCategory._hmf_once_t13.42586
- _logCategory._hmf_once_t14.62477
- _logCategory._hmf_once_t16.31268
- _logCategory._hmf_once_t16.37808
- _logCategory._hmf_once_t16.64529
- _logCategory._hmf_once_t2.24422
- _logCategory._hmf_once_t2.26548
- _logCategory._hmf_once_t2.29725
- _logCategory._hmf_once_t2.33428
- _logCategory._hmf_once_t20.25147
- _logCategory._hmf_once_t20.26136
- _logCategory._hmf_once_t21.62085
- _logCategory._hmf_once_t23
- _logCategory._hmf_once_t24.40969
- _logCategory._hmf_once_t24.41634
- _logCategory._hmf_once_t25.65490
- _logCategory._hmf_once_t27.61391
- _logCategory._hmf_once_t3.42720
- _logCategory._hmf_once_t3.53518
- _logCategory._hmf_once_t3.65126
- _logCategory._hmf_once_t31.24222
- _logCategory._hmf_once_t31.53983
- _logCategory._hmf_once_t31.66084
- _logCategory._hmf_once_t32.53294
- _logCategory._hmf_once_t34.20471
- _logCategory._hmf_once_t37.54272
- _logCategory._hmf_once_t377
- _logCategory._hmf_once_t4.1465
- _logCategory._hmf_once_t4.6320
- _logCategory._hmf_once_t44.26404
- _logCategory._hmf_once_t44.32149
- _logCategory._hmf_once_t5.18677
- _logCategory._hmf_once_t51.42989
- _logCategory._hmf_once_t6.34747
- _logCategory._hmf_once_t6.37574
- _logCategory._hmf_once_t6.43493
- _logCategory._hmf_once_t6.48998
- _logCategory._hmf_once_t6.58509
- _logCategory._hmf_once_t7.52419
- _logCategory._hmf_once_t8.38036
- _logCategory._hmf_once_t8.48341
- _logCategory._hmf_once_t8.51492
- _logCategory._hmf_once_t9.29444
- _logCategory._hmf_once_v1.14355
- _logCategory._hmf_once_v1.23224
- _logCategory._hmf_once_v1.24610
- _logCategory._hmf_once_v1.31866
- _logCategory._hmf_once_v1.32231
- _logCategory._hmf_once_v1.43275
- _logCategory._hmf_once_v1.45433
- _logCategory._hmf_once_v1.45625
- _logCategory._hmf_once_v1.62727
- _logCategory._hmf_once_v10.29446
- _logCategory._hmf_once_v12.13035
- _logCategory._hmf_once_v14.42588
- _logCategory._hmf_once_v15.62479
- _logCategory._hmf_once_v17.31270
- _logCategory._hmf_once_v17.37810
- _logCategory._hmf_once_v17.64531
- _logCategory._hmf_once_v2.18993
- _logCategory._hmf_once_v2.20938
- _logCategory._hmf_once_v2.40608
- _logCategory._hmf_once_v2.46808
- _logCategory._hmf_once_v2.50983
- _logCategory._hmf_once_v2.52541
- _logCategory._hmf_once_v2.57647
- _logCategory._hmf_once_v21.25148
- _logCategory._hmf_once_v21.26138
- _logCategory._hmf_once_v22.62087
- _logCategory._hmf_once_v24
- _logCategory._hmf_once_v25.40971
- _logCategory._hmf_once_v25.41636
- _logCategory._hmf_once_v26.65492
- _logCategory._hmf_once_v28.61393
- _logCategory._hmf_once_v3.24424
- _logCategory._hmf_once_v3.26550
- _logCategory._hmf_once_v3.29727
- _logCategory._hmf_once_v3.33430
- _logCategory._hmf_once_v32.24224
- _logCategory._hmf_once_v32.53985
- _logCategory._hmf_once_v32.66086
- _logCategory._hmf_once_v33.53296
- _logCategory._hmf_once_v35.20473
- _logCategory._hmf_once_v378
- _logCategory._hmf_once_v38.54273
- _logCategory._hmf_once_v4.42722
- _logCategory._hmf_once_v4.53519
- _logCategory._hmf_once_v4.65128
- _logCategory._hmf_once_v45.26405
- _logCategory._hmf_once_v45.32151
- _logCategory._hmf_once_v5.1466
- _logCategory._hmf_once_v5.6322
- _logCategory._hmf_once_v52.42991
- _logCategory._hmf_once_v6.18679
- _logCategory._hmf_once_v7.34749
- _logCategory._hmf_once_v7.37576
- _logCategory._hmf_once_v7.43495
- _logCategory._hmf_once_v7.49000
- _logCategory._hmf_once_v7.58511
- _logCategory._hmf_once_v8.52421
- _logCategory._hmf_once_v9.38038
- _logCategory._hmf_once_v9.48343
- _logCategory._hmf_once_v9.51493
- _objc_msgSend$duetDataSource
- _objc_msgSend$fetchPredictionsFromDuet
- _objc_msgSend$handleRuntimeStateUpdate:completionHandler:
- _objc_msgSend$initWithWorkQueue:messageDispatcher:UUID:dataSource:duetDataSource:predictionTransformer:darwinNotificationProvider:
- _objc_msgSend$scheduleSendBarrierBlock:
- _sharedInstance.onceToken.42596
- _sharedManager.onceToken.61538
- _supportedValueClasses.onceToken.51277
- _supportedValueClasses.onceToken.59761
- _supportedValueClasses.supportedValueClasses.51279
- _supportedValueClasses.supportedValueClasses.59762
CStrings:
+ "%{public}@Failed to get synchronous remote object proxy for re-connecting to the daemon: %@"
+ "%{public}@Home was nil while configuring _HMCameraProfile. Call stack: %@"
+ "%{public}@Ignoring fill slot completion because camera source has changed"
+ "%{public}@Invalidating connection due to dealloc: %p"
+ "%{public}@Marking the connection as requiring check-in due to interruption: %p"
+ "%{public}@No active prediction subscribers, will fetch from backend later."
+ "%{public}@Notified that device has been unlocked for the first time, fetching predictions from backend"
+ "%{public}@Running deferred fetch from backend before returning predictions"
+ "%{public}@Running fetch from backend on subscriber addition"
+ "%{public}@Set camera source to %@"
+ "%{public}@Updating supportsAdaptiveTemperatureAutomations from %@ to %@"
+ "%{public}@Updating supportsCleanEnergyAutomations from %@ to %@"
+ "'"
+ "/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/HomeKit/ClientConnection/HMClientConnection.m"
+ "@\"<HMDarwinNotificationProvider>\"16@0:8"
+ "@\"<HMUserActionPredictionDataSource>\""
+ "@\"<HMXPCClientDataSource>\""
+ "@\"<HMXPCConnection>\""
+ "@\"<HMXPCConnection>\"24@0:8@\"NSString\"16"
+ "@\"HMFProcessInfo\"16@0:8"
+ "@\"HMXPCClientConnectionProxy\"32@0:8@\"NSDictionary\"16@?<v@?>24"
+ "@\"NSNotificationCenter\"16@0:8"
+ "@\"NSXPCInterface\"16@0:8"
+ "@24@0:8@\"NSString\"16"
+ "@24@0:8@?<v@?@\"NSError\">16"
+ "@?<v@?>16@0:8"
+ "HMAccessorySupportsAdaptiveTemperatureAutomationsMessage"
+ "HMAccessorySupportsCleanEnergyAutomationsMessage"
+ "HMDaemonDisconnectedNotification"
+ "HMUserActionPredictionDataSource"
+ "HMXPCClientDataSource"
+ "HMXPCConnection"
+ "Home-%@-%@"
+ "HomeManager-%@-%@"
+ "Merge-Home-%@-%@"
+ "Merge-HomeManager-"
+ "Process ID"
+ "Process Name"
+ "T@\"<HMDarwinNotificationProvider>\",R"
+ "T@\"<HMUserActionPredictionDataSource>\",R,V_predictionDataSource"
+ "T@\"<HMXPCClientDataSource>\",R,V_dataSource"
+ "T@\"<HMXPCConnection>\",&,N,V_connection"
+ "T@\"HMFProcessInfo\",R"
+ "T@\"NSNotificationCenter\",R"
+ "T@\"NSObject<OS_dispatch_queue>\",&"
+ "T@\"NSXPCConnection\",R,V_xpcConnection"
+ "T@\"NSXPCInterface\",&"
+ "T@,&"
+ "T@,R"
+ "T@?,C"
+ "Ti,R"
+ "T{?=[8I]},R"
+ "_handleDaemonInterruptedNotification:"
+ "_handleSupportsAdaptiveTemperatureAutomationMessage:"
+ "_handleSupportsCleanEnergyAutomationMessage:"
+ "_predictionDataSource"
+ "_shouldRefetchFromBackend"
+ "_xpcConnection"
+ "auditToken"
+ "backendPredictions != nil"
+ "camera.view"
+ "createXPCClientConnectionProxyWithUserInfo:refreshHandler:"
+ "createXPCConnectionWithMachServiceName:"
+ "exportedObject"
+ "fetchPredictionsFromBackendWithCompletion:"
+ "initWithConfiguration:userInfo:dataSource:"
+ "initWithWorkQueue:messageDispatcher:UUID:dataSource:predictionDataSource:predictionTransformer:darwinNotificationProvider:"
+ "initWithXPCConnection:"
+ "interruptionHandler"
+ "invalidationHandler"
+ "predictionDataSource"
+ "predictionDataSource != nil"
+ "processIdentifier"
+ "remoteObjectProxy"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "v24@0:8@\"NSXPCInterface\"16"
+ "v24@0:8@?<v@?>16"
+ "v24@0:8@?<v@?@\"NSArray\">16"
+ "xpcConnection"
+ "{?=[8I]}16@0:8"
- "%{public}@Could not find serialized faceprints in response payload: %@"
- "%{public}@Creating accessory info provider with last event store: %@"
- "%{public}@Going to invalidate the XPC connection with HomeKitDaemon."
- "%{public}@No active prediction subscribers, will fetch from duet later."
- "%{public}@Notified that device has been unlocked for the first time, fetching predictions from duet"
- "%{public}@Running deferred fetch from duet before returning predictions"
- "%{public}@Running fetch from duet on subscriber addition"
- "&"
- "-[HMAccessory handleRuntimeStateUpdate:completionHandler:]"
- "-[HMHomeManager(HMHomeManagerAdaptive) sendHomecommsdLunchboxWithCompletionHandler:]"
- "/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/HomeKit/HMClientConnection.m"
- "@\"HMUserActionPredictionDuetDataSource\""
- "HCD"
- "HMHM.lrm"
- "Home-%@%@"
- "HomeManager-"
- "HomeManager-%@%@"
- "Merge-"
- "Merge-HM-%@-%@"
- "T@\"HMUserActionPredictionDuetDataSource\",R,V_duetDataSource"
- "T@\"NSXPCConnection\",&,N,V_connection"
- "_duetDataSource"
- "_handleDaemonDisconnect:"
- "_shouldRefetchFromDuet"
- "duetDataSource"
- "duetDataSource != nil"
- "fetchPredictionsFromDuet"
- "handleRuntimeStateUpdate:completionHandler:"
- "initWithWorkQueue:messageDispatcher:UUID:dataSource:duetDataSource:predictionTransformer:darwinNotificationProvider:"
- "kHomeKitDaemonInterruptedNotification"
- "scheduleSendBarrierBlock:"
- "sendHomecommsdLunchboxWithCompletionHandler:"

```
