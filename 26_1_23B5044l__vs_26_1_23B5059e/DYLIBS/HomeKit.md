## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1368.1.0.1.2
-  __TEXT.__text: 0x2d0da0
+1371.2.5.0.0
+  __TEXT.__text: 0x2d1c0c
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0x25b74
+  __TEXT.__objc_methlist: 0x25bbc
   __TEXT.__const: 0x236c
   __TEXT.__dlopen_cstrs: 0x3a1
-  __TEXT.__cstring: 0x2a82a
+  __TEXT.__cstring: 0x2a96b
   __TEXT.__swift5_typeref: 0xbc8
   __TEXT.__constg_swiftt: 0xa58
   __TEXT.__swift5_reflstr: 0x3f1

   __TEXT.__swift5_types: 0xcc
   __TEXT.__swift_as_entry: 0x20
   __TEXT.__swift_as_ret: 0x20
-  __TEXT.__oslogstring: 0x2af25
+  __TEXT.__oslogstring: 0x2b092
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__gcc_except_tab: 0x7178
+  __TEXT.__gcc_except_tab: 0x7230
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x9cc8
+  __TEXT.__unwind_info: 0x9ce8
   __TEXT.__eh_frame: 0x10d0
-  __TEXT.__objc_classname: 0x5050
-  __TEXT.__objc_methname: 0x48a62
+  __TEXT.__objc_classname: 0x5055
+  __TEXT.__objc_methname: 0x48b9c
   __TEXT.__objc_methtype: 0x893e
-  __TEXT.__objc_stubs: 0x25da0
+  __TEXT.__objc_stubs: 0x25e80
   __DATA_CONST.__got: 0x1848
-  __DATA_CONST.__const: 0x7e78
+  __DATA_CONST.__const: 0x7ea0
   __DATA_CONST.__objc_classlist: 0x1248
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd290
+  __DATA_CONST.__objc_selrefs: 0xd2c8
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0xf50
   __DATA_CONST.__objc_arraydata: 0x1380
   __AUTH_CONST.__auth_got: 0xdc0
-  __AUTH_CONST.__const: 0x31a8
-  __AUTH_CONST.__cfstring: 0x27ba0
-  __AUTH_CONST.__objc_const: 0x43e80
+  __AUTH_CONST.__const: 0x31c8
+  __AUTH_CONST.__cfstring: 0x27c40
+  __AUTH_CONST.__objc_const: 0x43f00
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x570
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH.__objc_data: 0x8488
   __AUTH.__data: 0x6b0
-  __DATA.__objc_ivar: 0x256c
+  __DATA.__objc_ivar: 0x2578
   __DATA.__data: 0x3f90
-  __DATA.__bss: 0x3fc0
+  __DATA.__bss: 0x3fb0
   __DATA.__common: 0x59
   __DATA_DIRTY.__objc_data: 0x33e0
   __DATA_DIRTY.__data: 0x28
-  __DATA_DIRTY.__bss: 0x270
+  __DATA_DIRTY.__bss: 0x280
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 628C190A-F6F1-3A92-B97B-8BB024775761
-  Functions: 14562
-  Symbols:   44330
-  CStrings:  25803
+  UUID: D0D5FBBC-1C04-33BC-A5D8-26C4348B873B
+  Functions: 14573
+  Symbols:   44367
+  CStrings:  25835
 
Symbols:
+ -[HMAccessory HAPInstanceID]
+ -[HMAccessory isVendorAccessory]
+ -[HMAccessory setHAPInstanceID:]
+ -[HMAccessory setVendorAccessory:]
+ -[HMCharacteristic hasFixedValue]
+ -[HMCharacteristic setHasFixedValue:]
+ -[HMHome initWithName:uuid:accessories:mediaSystems:]
+ -[HMHomeManager(Vendor) findVendorAccessoryWithHAPPublicKey:completionHandler:]
+ -[HMUserActionPredictionProvider _fetchPredictionsFromBackendAndUpdateHomesWithCompletion:]
+ GCC_except_table10011
+ GCC_except_table10031
+ GCC_except_table10032
+ GCC_except_table10033
+ GCC_except_table10072
+ GCC_except_table10074
+ GCC_except_table10076
+ GCC_except_table10139
+ GCC_except_table10171
+ GCC_except_table10173
+ GCC_except_table10177
+ GCC_except_table10194
+ GCC_except_table10196
+ GCC_except_table10202
+ GCC_except_table10206
+ GCC_except_table10209
+ GCC_except_table10216
+ GCC_except_table10220
+ GCC_except_table10226
+ GCC_except_table10238
+ GCC_except_table10241
+ GCC_except_table10250
+ GCC_except_table10252
+ GCC_except_table10254
+ GCC_except_table10256
+ GCC_except_table10268
+ GCC_except_table10278
+ GCC_except_table10481
+ GCC_except_table10494
+ GCC_except_table10548
+ GCC_except_table10552
+ GCC_except_table10560
+ GCC_except_table10608
+ GCC_except_table10611
+ GCC_except_table10612
+ GCC_except_table10959
+ GCC_except_table11007
+ GCC_except_table11020
+ GCC_except_table1122
+ GCC_except_table1126
+ GCC_except_table1133
+ GCC_except_table11391
+ GCC_except_table11393
+ GCC_except_table11394
+ GCC_except_table11403
+ GCC_except_table11426
+ GCC_except_table11429
+ GCC_except_table11441
+ GCC_except_table11442
+ GCC_except_table11443
+ GCC_except_table11551
+ GCC_except_table11552
+ GCC_except_table11578
+ GCC_except_table11580
+ GCC_except_table11584
+ GCC_except_table11585
+ GCC_except_table11633
+ GCC_except_table11659
+ GCC_except_table11672
+ GCC_except_table11698
+ GCC_except_table11702
+ GCC_except_table11762
+ GCC_except_table11763
+ GCC_except_table11764
+ GCC_except_table11765
+ GCC_except_table11766
+ GCC_except_table11767
+ GCC_except_table11768
+ GCC_except_table11769
+ GCC_except_table11770
+ GCC_except_table11771
+ GCC_except_table11794
+ GCC_except_table11821
+ GCC_except_table11931
+ GCC_except_table11932
+ GCC_except_table11935
+ GCC_except_table12002
+ GCC_except_table12010
+ GCC_except_table12021
+ GCC_except_table12023
+ GCC_except_table12028
+ GCC_except_table12029
+ GCC_except_table12030
+ GCC_except_table12235
+ GCC_except_table1225
+ GCC_except_table1234
+ GCC_except_table12435
+ GCC_except_table12438
+ GCC_except_table12447
+ GCC_except_table12453
+ GCC_except_table12460
+ GCC_except_table12465
+ GCC_except_table12466
+ GCC_except_table12468
+ GCC_except_table12550
+ GCC_except_table12552
+ GCC_except_table12571
+ GCC_except_table12572
+ GCC_except_table12573
+ GCC_except_table12574
+ GCC_except_table12579
+ GCC_except_table12593
+ GCC_except_table12599
+ GCC_except_table12602
+ GCC_except_table12604
+ GCC_except_table12682
+ GCC_except_table12690
+ GCC_except_table12691
+ GCC_except_table12706
+ GCC_except_table12708
+ GCC_except_table12710
+ GCC_except_table12712
+ GCC_except_table12714
+ GCC_except_table12847
+ GCC_except_table12903
+ GCC_except_table12904
+ GCC_except_table12905
+ GCC_except_table12916
+ GCC_except_table12917
+ GCC_except_table12941
+ GCC_except_table12942
+ GCC_except_table12998
+ GCC_except_table13020
+ GCC_except_table13023
+ GCC_except_table1304
+ GCC_except_table1311
+ GCC_except_table13120
+ GCC_except_table1315
+ GCC_except_table13163
+ GCC_except_table13358
+ GCC_except_table13363
+ GCC_except_table13366
+ GCC_except_table13426
+ GCC_except_table13536
+ GCC_except_table13597
+ GCC_except_table13600
+ GCC_except_table13620
+ GCC_except_table13622
+ GCC_except_table13623
+ GCC_except_table1364
+ GCC_except_table1513
+ GCC_except_table1536
+ GCC_except_table1604
+ GCC_except_table1659
+ GCC_except_table1662
+ GCC_except_table1680
+ GCC_except_table1749
+ GCC_except_table1762
+ GCC_except_table1874
+ GCC_except_table1944
+ GCC_except_table1947
+ GCC_except_table2019
+ GCC_except_table2105
+ GCC_except_table2106
+ GCC_except_table2155
+ GCC_except_table2358
+ GCC_except_table2361
+ GCC_except_table2364
+ GCC_except_table2369
+ GCC_except_table2373
+ GCC_except_table2382
+ GCC_except_table2397
+ GCC_except_table2398
+ GCC_except_table2405
+ GCC_except_table2406
+ GCC_except_table2819
+ GCC_except_table2824
+ GCC_except_table2850
+ GCC_except_table2853
+ GCC_except_table2866
+ GCC_except_table2903
+ GCC_except_table2919
+ GCC_except_table2922
+ GCC_except_table2953
+ GCC_except_table3114
+ GCC_except_table3132
+ GCC_except_table3133
+ GCC_except_table3181
+ GCC_except_table3207
+ GCC_except_table3210
+ GCC_except_table3211
+ GCC_except_table3237
+ GCC_except_table3247
+ GCC_except_table3255
+ GCC_except_table3261
+ GCC_except_table3262
+ GCC_except_table3321
+ GCC_except_table3344
+ GCC_except_table3347
+ GCC_except_table3350
+ GCC_except_table3353
+ GCC_except_table3356
+ GCC_except_table3359
+ GCC_except_table3362
+ GCC_except_table3427
+ GCC_except_table3428
+ GCC_except_table3474
+ GCC_except_table3482
+ GCC_except_table3483
+ GCC_except_table3487
+ GCC_except_table3490
+ GCC_except_table3498
+ GCC_except_table3520
+ GCC_except_table3527
+ GCC_except_table3531
+ GCC_except_table3534
+ GCC_except_table3537
+ GCC_except_table3578
+ GCC_except_table3582
+ GCC_except_table3586
+ GCC_except_table3591
+ GCC_except_table3599
+ GCC_except_table3603
+ GCC_except_table3614
+ GCC_except_table3853
+ GCC_except_table3857
+ GCC_except_table3861
+ GCC_except_table3864
+ GCC_except_table3868
+ GCC_except_table3869
+ GCC_except_table3872
+ GCC_except_table3878
+ GCC_except_table3882
+ GCC_except_table3886
+ GCC_except_table3913
+ GCC_except_table3916
+ GCC_except_table3919
+ GCC_except_table3922
+ GCC_except_table4002
+ GCC_except_table4016
+ GCC_except_table4021
+ GCC_except_table4024
+ GCC_except_table4031
+ GCC_except_table4084
+ GCC_except_table4149
+ GCC_except_table4164
+ GCC_except_table4167
+ GCC_except_table4260
+ GCC_except_table4263
+ GCC_except_table4268
+ GCC_except_table4272
+ GCC_except_table4277
+ GCC_except_table4285
+ GCC_except_table4532
+ GCC_except_table4535
+ GCC_except_table4547
+ GCC_except_table4621
+ GCC_except_table4665
+ GCC_except_table4757
+ GCC_except_table4919
+ GCC_except_table4933
+ GCC_except_table4959
+ GCC_except_table4960
+ GCC_except_table5015
+ GCC_except_table5025
+ GCC_except_table5154
+ GCC_except_table5155
+ GCC_except_table5231
+ GCC_except_table5335
+ GCC_except_table5365
+ GCC_except_table5383
+ GCC_except_table540
+ GCC_except_table5429
+ GCC_except_table545
+ GCC_except_table5524
+ GCC_except_table553
+ GCC_except_table554
+ GCC_except_table5545
+ GCC_except_table5548
+ GCC_except_table5551
+ GCC_except_table5554
+ GCC_except_table5812
+ GCC_except_table5820
+ GCC_except_table5830
+ GCC_except_table5831
+ GCC_except_table6034
+ GCC_except_table6038
+ GCC_except_table6111
+ GCC_except_table6242
+ GCC_except_table6249
+ GCC_except_table6254
+ GCC_except_table6439
+ GCC_except_table6492
+ GCC_except_table6683
+ GCC_except_table6690
+ GCC_except_table6698
+ GCC_except_table6718
+ GCC_except_table6727
+ GCC_except_table6732
+ GCC_except_table6735
+ GCC_except_table6749
+ GCC_except_table6754
+ GCC_except_table6760
+ GCC_except_table6765
+ GCC_except_table6770
+ GCC_except_table6775
+ GCC_except_table6780
+ GCC_except_table6784
+ GCC_except_table6789
+ GCC_except_table6841
+ GCC_except_table6845
+ GCC_except_table6853
+ GCC_except_table6858
+ GCC_except_table6872
+ GCC_except_table6877
+ GCC_except_table6884
+ GCC_except_table6899
+ GCC_except_table6904
+ GCC_except_table6907
+ GCC_except_table6912
+ GCC_except_table6919
+ GCC_except_table6924
+ GCC_except_table6928
+ GCC_except_table6962
+ GCC_except_table7019
+ GCC_except_table7025
+ GCC_except_table7026
+ GCC_except_table712
+ GCC_except_table715
+ GCC_except_table7165
+ GCC_except_table7172
+ GCC_except_table720
+ GCC_except_table723
+ GCC_except_table724
+ GCC_except_table7257
+ GCC_except_table7290
+ GCC_except_table7349
+ GCC_except_table7373
+ GCC_except_table7401
+ GCC_except_table7415
+ GCC_except_table7431
+ GCC_except_table7437
+ GCC_except_table746
+ GCC_except_table7476
+ GCC_except_table7481
+ GCC_except_table7494
+ GCC_except_table7495
+ GCC_except_table7500
+ GCC_except_table7521
+ GCC_except_table7546
+ GCC_except_table7559
+ GCC_except_table7577
+ GCC_except_table763
+ GCC_except_table7757
+ GCC_except_table782
+ GCC_except_table8020
+ GCC_except_table8063
+ GCC_except_table8123
+ GCC_except_table8239
+ GCC_except_table8242
+ GCC_except_table832
+ GCC_except_table8332
+ GCC_except_table835
+ GCC_except_table8351
+ GCC_except_table836
+ GCC_except_table8361
+ GCC_except_table8497
+ GCC_except_table8506
+ GCC_except_table8519
+ GCC_except_table8526
+ GCC_except_table8569
+ GCC_except_table8571
+ GCC_except_table8599
+ GCC_except_table8601
+ GCC_except_table8603
+ GCC_except_table8605
+ GCC_except_table8612
+ GCC_except_table8618
+ GCC_except_table8622
+ GCC_except_table8632
+ GCC_except_table8638
+ GCC_except_table8724
+ GCC_except_table8726
+ GCC_except_table8736
+ GCC_except_table8738
+ GCC_except_table8740
+ GCC_except_table8742
+ GCC_except_table8744
+ GCC_except_table8750
+ GCC_except_table8754
+ GCC_except_table8767
+ GCC_except_table8769
+ GCC_except_table8771
+ GCC_except_table8773
+ GCC_except_table8792
+ GCC_except_table8949
+ GCC_except_table8951
+ GCC_except_table8955
+ GCC_except_table8957
+ GCC_except_table8958
+ GCC_except_table8959
+ GCC_except_table8994
+ GCC_except_table8997
+ GCC_except_table8998
+ GCC_except_table9001
+ GCC_except_table9004
+ GCC_except_table9005
+ GCC_except_table902
+ GCC_except_table9048
+ GCC_except_table9049
+ GCC_except_table9050
+ GCC_except_table9057
+ GCC_except_table9058
+ GCC_except_table9060
+ GCC_except_table9079
+ GCC_except_table910
+ GCC_except_table915
+ GCC_except_table9151
+ GCC_except_table9152
+ GCC_except_table9153
+ GCC_except_table9190
+ GCC_except_table922
+ GCC_except_table923
+ GCC_except_table9374
+ GCC_except_table9376
+ GCC_except_table9380
+ GCC_except_table9435
+ GCC_except_table9456
+ GCC_except_table9532
+ GCC_except_table9534
+ GCC_except_table9536
+ GCC_except_table9538
+ GCC_except_table9546
+ GCC_except_table9593
+ GCC_except_table9605
+ GCC_except_table9607
+ GCC_except_table9623
+ GCC_except_table9651
+ GCC_except_table9825
+ GCC_except_table9827
+ GCC_except_table9829
+ GCC_except_table9873
+ GCC_except_table9874
+ GCC_except_table9909
+ GCC_except_table9942
+ GCC_except_table9948
+ GCC_except_table9950
+ _CoreAnalyticsLibraryCore.frameworkLibrary.40997
+ _CoreHAPLibraryCore.frameworkLibrary.33288
+ _HMAccessoryHAPInstanceIDCodingKey
+ _HMAccessoryIsVendorAccessoryCodingKey
+ _HMAccessoryPublicKeyKey
+ _HMHomeManagerFindVendorAccessoryMessage
+ _IDSFoundationLibraryCore.45308
+ _IDSFoundationLibraryCore.frameworkLibrary.45310
+ _OBJC_IVAR_$_HMAccessory._HAPInstanceID
+ _OBJC_IVAR_$_HMAccessory._vendorAccessory
+ _OBJC_IVAR_$_HMCharacteristic._hasFixedValue
+ _UIKitLibrary.45535
+ _UIKitLibraryCore.45531
+ _UIKitLibraryCore.frameworkLibrary.45544
+ __OBJC_$_CLASS_METHODS_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|OSEligibility|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|Vendor|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
+ __OBJC_$_INSTANCE_METHODS_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|OSEligibility|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|Vendor|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
+ __OBJC_$_PROP_LIST_HMEventTriggerBuilder.215
+ __OBJC_$_PROP_LIST_HMMediaDestination.20097
+ __OBJC_CLASS_PROTOCOLS_$_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|OSEligibility|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|Vendor|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
+ ___102-[HMHome(HMModernMessaging) unregisterModernMessagingRequestHandlerWithMessageName:completionHandler:]_block_invoke.2286
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.800
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.804
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.808
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.810
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.809
+ ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.807
+ ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2243
+ ___123-[HMHome(HMModernMessaging) registerModernMessagingRequestHandlerWithMessageName:options:requestHandler:completionHandler:]_block_invoke.2285
+ ___140-[HMHome(HMModernMessaging) sendModernMessagingRequestWithMessageName:destination:requestPayload:options:responseHandler:completionHandler:]_block_invoke.2288
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1333
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1334
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1336
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1338
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1339
+ ___30-[HMAccessory _mergeServices:]_block_invoke.1126
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1128
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1129
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1148
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1151
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1153
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1156
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1160
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1165
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1298
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1300
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1303
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1312
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1314
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1317
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1319
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1321
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1322
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1130
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1149
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1152
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1154
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1157
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1161
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1166
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1299
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1301
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1306
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1309
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1320
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1324
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1168
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1325
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1169
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1327
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1170
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1328
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1292
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1330
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_7.1331
+ ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.539
+ ___39-[HMCharacteristic mergeFromNewObject:]_block_invoke.258
+ ___39-[HMCharacteristic mergeFromNewObject:]_block_invoke_2.259
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.812
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.814
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1366
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1368
+ ___46-[HMHomeManager removeHome:completionHandler:]_block_invoke.653
+ ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.722
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1354
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1355
+ ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.779
+ ___51-[HMHomeManager addHomeWithName:completionHandler:]_block_invoke.649
+ ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.2059
+ ___54-[HMHome(PowerAssertionInfo) fetchPowerAssertionInfo:]_block_invoke.2223
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.634
+ ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.635
+ ___57-[HMAccessory _mergeBulletinBoardNotificationByEndpoint:]_block_invoke.1123
+ ___59-[HMHome(HMModernMessagingInternal) reRegisterHMMMHandlers]_block_invoke.2297
+ ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2250
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.1052
+ ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.1054
+ ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.2137
+ ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke.2228
+ ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke_2.2229
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.740
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.744
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.746
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.748
+ ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.749
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.871
+ ___71-[HMHome(HomeActivityState) changeHomeActivityState:completionHandler:]_block_invoke.2247
+ ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke.2226
+ ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke_2.2227
+ ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke.2230
+ ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke_2.2231
+ ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke.2302
+ ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke_2.2303
+ ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.719
+ ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1920
+ ___78-[HMHome(HomeActivityState) cancelHomeActivityStateHoldWithCompletionHandler:]_block_invoke.2252
+ ___79-[HMHomeManager(Vendor) findVendorAccessoryWithHAPPublicKey:completionHandler:]_block_invoke
+ ___83-[HMUserActionPredictionProvider fetchPredictionsForHomeWithIdentifier:completion:]_block_invoke.52
+ ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1931
+ ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1922
+ ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.2238
+ ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.2192
+ ___91-[HMUserActionPredictionProvider _fetchPredictionsFromBackendAndUpdateHomesWithCompletion:]_block_invoke
+ ___Block_byref_object_copy_.16737
+ ___Block_byref_object_copy_.17070
+ ___Block_byref_object_copy_.24684
+ ___Block_byref_object_copy_.27018
+ ___Block_byref_object_copy_.33380
+ ___Block_byref_object_copy_.35562
+ ___Block_byref_object_copy_.40884
+ ___Block_byref_object_copy_.44336
+ ___Block_byref_object_copy_.64155
+ ___Block_byref_object_copy_.66568
+ ___Block_byref_object_dispose_.16738
+ ___Block_byref_object_dispose_.17071
+ ___Block_byref_object_dispose_.24685
+ ___Block_byref_object_dispose_.27019
+ ___Block_byref_object_dispose_.33381
+ ___Block_byref_object_dispose_.35563
+ ___Block_byref_object_dispose_.40885
+ ___Block_byref_object_dispose_.44337
+ ___Block_byref_object_dispose_.64156
+ ___Block_byref_object_dispose_.66569
+ ___CoreAnalyticsLibraryCore_block_invoke.40998
+ ___CoreHAPLibraryCore_block_invoke.33289
+ ___IDSFoundationLibraryCore_block_invoke.45311
+ ___UIKitLibraryCore_block_invoke.45545
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSArray"8lw40l8s32l8
+ ___block_literal_global.101.41005
+ ___block_literal_global.101.43187
+ ___block_literal_global.11102
+ ___block_literal_global.1166
+ ___block_literal_global.11682
+ ___block_literal_global.12.51719
+ ___block_literal_global.12397
+ ___block_literal_global.1350
+ ___block_literal_global.14537
+ ___block_literal_global.14678
+ ___block_literal_global.14753
+ ___block_literal_global.15000
+ ___block_literal_global.15373
+ ___block_literal_global.1558
+ ___block_literal_global.15602
+ ___block_literal_global.16184
+ ___block_literal_global.16534
+ ___block_literal_global.16825
+ ___block_literal_global.17.20317
+ ___block_literal_global.17452
+ ___block_literal_global.18662
+ ___block_literal_global.19.16519
+ ___block_literal_global.19193
+ ___block_literal_global.19374
+ ___block_literal_global.1939
+ ___block_literal_global.19507
+ ___block_literal_global.19667
+ ___block_literal_global.20324
+ ___block_literal_global.2056
+ ___block_literal_global.2058
+ ___block_literal_global.2072
+ ___block_literal_global.20982
+ ___block_literal_global.2134
+ ___block_literal_global.21447
+ ___block_literal_global.22086
+ ___block_literal_global.22453
+ ___block_literal_global.23424
+ ___block_literal_global.23728
+ ___block_literal_global.24061
+ ___block_literal_global.24722
+ ___block_literal_global.24911
+ ___block_literal_global.25106
+ ___block_literal_global.2575
+ ___block_literal_global.25877
+ ___block_literal_global.26247
+ ___block_literal_global.26384
+ ___block_literal_global.26630
+ ___block_literal_global.26875
+ ___block_literal_global.27042
+ ___block_literal_global.27135
+ ___block_literal_global.27866
+ ___block_literal_global.29899
+ ___block_literal_global.30.20306
+ ___block_literal_global.30057
+ ___block_literal_global.30336
+ ___block_literal_global.31615
+ ___block_literal_global.32218
+ ___block_literal_global.32480
+ ___block_literal_global.32767
+ ___block_literal_global.32846
+ ___block_literal_global.33.65864
+ ___block_literal_global.33524
+ ___block_literal_global.34
+ ___block_literal_global.34022
+ ___block_literal_global.34295
+ ___block_literal_global.35348
+ ___block_literal_global.35585
+ ___block_literal_global.35886
+ ___block_literal_global.37215
+ ___block_literal_global.38
+ ___block_literal_global.38191
+ ___block_literal_global.38425
+ ___block_literal_global.38652
+ ___block_literal_global.39045
+ ___block_literal_global.39795
+ ___block_literal_global.4068
+ ___block_literal_global.40992
+ ___block_literal_global.41242
+ ___block_literal_global.41579
+ ___block_literal_global.42241
+ ___block_literal_global.43197
+ ___block_literal_global.43460
+ ___block_literal_global.43726
+ ___block_literal_global.44008
+ ___block_literal_global.4406
+ ___block_literal_global.44228
+ ___block_literal_global.4492
+ ___block_literal_global.45371
+ ___block_literal_global.45463
+ ___block_literal_global.4585
+ ___block_literal_global.46170
+ ___block_literal_global.46362
+ ___block_literal_global.47542
+ ___block_literal_global.47987
+ ___block_literal_global.48315
+ ___block_literal_global.49079
+ ___block_literal_global.49736
+ ___block_literal_global.50094
+ ___block_literal_global.51367
+ ___block_literal_global.51731
+ ___block_literal_global.52015
+ ___block_literal_global.52211
+ ___block_literal_global.52491
+ ___block_literal_global.529
+ ___block_literal_global.53190
+ ___block_literal_global.53310
+ ___block_literal_global.54.52531
+ ___block_literal_global.54065
+ ___block_literal_global.54299
+ ___block_literal_global.5445
+ ___block_literal_global.54754
+ ___block_literal_global.55017
+ ___block_literal_global.56094
+ ___block_literal_global.58.38420
+ ___block_literal_global.58386
+ ___block_literal_global.59251
+ ___block_literal_global.6031
+ ___block_literal_global.60538
+ ___block_literal_global.61270
+ ___block_literal_global.61821
+ ___block_literal_global.62131
+ ___block_literal_global.62648
+ ___block_literal_global.62825
+ ___block_literal_global.63214
+ ___block_literal_global.63459
+ ___block_literal_global.6429
+ ___block_literal_global.65268
+ ___block_literal_global.65603
+ ___block_literal_global.6565
+ ___block_literal_global.65870
+ ___block_literal_global.66225
+ ___block_literal_global.66507
+ ___block_literal_global.66863
+ ___block_literal_global.6792
+ ___block_literal_global.7.24922
+ ___block_literal_global.713
+ ___block_literal_global.7279
+ ___block_literal_global.73.25080
+ ___block_literal_global.761
+ ___block_literal_global.763
+ ___block_literal_global.7643
+ ___block_literal_global.7790
+ ___block_literal_global.8294
+ ___block_literal_global.84.41185
+ ___block_literal_global.8551
+ ___block_literal_global.875
+ ___block_literal_global.9137
+ ___block_literal_global.9380
+ ___block_literal_global.9780
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.40995
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.45540
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.45534
+ _audit_stringCoreAnalytics.41001
+ _audit_stringCoreHAP.33291
+ _audit_stringIDSFoundation.45313
+ _audit_stringUIKit.45547
+ _getAnalyticsSendEventLazySymbolLoc.ptr.40994
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.45539
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.45533
+ _kCharacteristicHasFixedValueKey
+ _logCategory._hmf_once_t0.14752
+ _logCategory._hmf_once_t0.23727
+ _logCategory._hmf_once_t0.25105
+ _logCategory._hmf_once_t0.32479
+ _logCategory._hmf_once_t0.32845
+ _logCategory._hmf_once_t0.44007
+ _logCategory._hmf_once_t0.46169
+ _logCategory._hmf_once_t0.46361
+ _logCategory._hmf_once_t0.6030
+ _logCategory._hmf_once_t0.63458
+ _logCategory._hmf_once_t1.19506
+ _logCategory._hmf_once_t1.21446
+ _logCategory._hmf_once_t1.41218
+ _logCategory._hmf_once_t1.47541
+ _logCategory._hmf_once_t1.51718
+ _logCategory._hmf_once_t1.53309
+ _logCategory._hmf_once_t1.58385
+ _logCategory._hmf_once_t10.23423
+ _logCategory._hmf_once_t11.7642
+ _logCategory._hmf_once_t13.43186
+ _logCategory._hmf_once_t16.38424
+ _logCategory._hmf_once_t16.65267
+ _logCategory._hmf_once_t2.24921
+ _logCategory._hmf_once_t2.27041
+ _logCategory._hmf_once_t2.30335
+ _logCategory._hmf_once_t2.34021
+ _logCategory._hmf_once_t20.26629
+ _logCategory._hmf_once_t21.62824
+ _logCategory._hmf_once_t22.4067
+ _logCategory._hmf_once_t24.41578
+ _logCategory._hmf_once_t24.42240
+ _logCategory._hmf_once_t25.26874
+ _logCategory._hmf_once_t25.66224
+ _logCategory._hmf_once_t27.62130
+ _logCategory._hmf_once_t3.54288
+ _logCategory._hmf_once_t3.65863
+ _logCategory._hmf_once_t31.24721
+ _logCategory._hmf_once_t31.54753
+ _logCategory._hmf_once_t31.66862
+ _logCategory._hmf_once_t32.54064
+ _logCategory._hmf_once_t34.20981
+ _logCategory._hmf_once_t37.55043
+ _logCategory._hmf_once_t383
+ _logCategory._hmf_once_t4.14999
+ _logCategory._hmf_once_t4.1569
+ _logCategory._hmf_once_t4.6428
+ _logCategory._hmf_once_t44.26899
+ _logCategory._hmf_once_t5.19192
+ _logCategory._hmf_once_t51.43725
+ _logCategory._hmf_once_t6.35347
+ _logCategory._hmf_once_t6.38190
+ _logCategory._hmf_once_t6.44227
+ _logCategory._hmf_once_t6.49735
+ _logCategory._hmf_once_t6.59250
+ _logCategory._hmf_once_t7.53189
+ _logCategory._hmf_once_t8.38651
+ _logCategory._hmf_once_t8.49078
+ _logCategory._hmf_once_t8.52229
+ _logCategory._hmf_once_t9.30056
+ _logCategory._hmf_once_v1.14754
+ _logCategory._hmf_once_v1.23729
+ _logCategory._hmf_once_v1.25107
+ _logCategory._hmf_once_v1.32481
+ _logCategory._hmf_once_v1.32847
+ _logCategory._hmf_once_v1.44009
+ _logCategory._hmf_once_v1.46171
+ _logCategory._hmf_once_v1.46363
+ _logCategory._hmf_once_v1.6032
+ _logCategory._hmf_once_v1.63460
+ _logCategory._hmf_once_v10.30058
+ _logCategory._hmf_once_v11.23425
+ _logCategory._hmf_once_v12.7644
+ _logCategory._hmf_once_v14.43188
+ _logCategory._hmf_once_v17.38426
+ _logCategory._hmf_once_v17.65269
+ _logCategory._hmf_once_v2.19508
+ _logCategory._hmf_once_v2.21448
+ _logCategory._hmf_once_v2.41219
+ _logCategory._hmf_once_v2.47543
+ _logCategory._hmf_once_v2.51720
+ _logCategory._hmf_once_v2.53311
+ _logCategory._hmf_once_v2.58387
+ _logCategory._hmf_once_v21.26631
+ _logCategory._hmf_once_v22.62826
+ _logCategory._hmf_once_v23.4069
+ _logCategory._hmf_once_v25.41580
+ _logCategory._hmf_once_v25.42242
+ _logCategory._hmf_once_v26.26876
+ _logCategory._hmf_once_v26.66226
+ _logCategory._hmf_once_v28.62132
+ _logCategory._hmf_once_v3.24923
+ _logCategory._hmf_once_v3.27043
+ _logCategory._hmf_once_v3.30337
+ _logCategory._hmf_once_v3.34023
+ _logCategory._hmf_once_v32.24723
+ _logCategory._hmf_once_v32.54755
+ _logCategory._hmf_once_v32.66864
+ _logCategory._hmf_once_v33.54066
+ _logCategory._hmf_once_v35.20983
+ _logCategory._hmf_once_v38.55044
+ _logCategory._hmf_once_v384
+ _logCategory._hmf_once_v4.54289
+ _logCategory._hmf_once_v4.65865
+ _logCategory._hmf_once_v45.26900
+ _logCategory._hmf_once_v5.15001
+ _logCategory._hmf_once_v5.1570
+ _logCategory._hmf_once_v5.6430
+ _logCategory._hmf_once_v52.43727
+ _logCategory._hmf_once_v6.19194
+ _logCategory._hmf_once_v7.35349
+ _logCategory._hmf_once_v7.38192
+ _logCategory._hmf_once_v7.44229
+ _logCategory._hmf_once_v7.49737
+ _logCategory._hmf_once_v7.59252
+ _logCategory._hmf_once_v8.53191
+ _logCategory._hmf_once_v9.38653
+ _logCategory._hmf_once_v9.49080
+ _logCategory._hmf_once_v9.52230
+ _objc_msgSend$HAPInstanceID
+ _objc_msgSend$hasFixedValue
+ _objc_msgSend$initWithName:uuid:accessories:mediaSystems:
+ _objc_msgSend$isVendorAccessory
+ _objc_msgSend$setHAPInstanceID:
+ _objc_msgSend$setHasFixedValue:
+ _objc_msgSend$setVendorAccessory:
+ _objc_msgSend$uuidFromStringForKey:
+ _sharedInstance.onceToken.43196
+ _sharedManager.onceToken.62276
+ _supportedValueClasses.onceToken.52014
+ _supportedValueClasses.onceToken.60501
+ _supportedValueClasses.supportedValueClasses.52016
+ _supportedValueClasses.supportedValueClasses.60502
- -[HMHome initWithName:uuid:mediaSystems:]
- -[HMHomeManager setInitialMergeComplete:]
- GCC_except_table10006
- GCC_except_table10026
- GCC_except_table10027
- GCC_except_table10028
- GCC_except_table10067
- GCC_except_table10069
- GCC_except_table10071
- GCC_except_table10134
- GCC_except_table10166
- GCC_except_table10168
- GCC_except_table10172
- GCC_except_table10189
- GCC_except_table10191
- GCC_except_table10197
- GCC_except_table10201
- GCC_except_table10204
- GCC_except_table10211
- GCC_except_table10215
- GCC_except_table10221
- GCC_except_table10233
- GCC_except_table10236
- GCC_except_table10244
- GCC_except_table10245
- GCC_except_table10247
- GCC_except_table10251
- GCC_except_table10263
- GCC_except_table10273
- GCC_except_table10476
- GCC_except_table10489
- GCC_except_table10538
- GCC_except_table10547
- GCC_except_table10555
- GCC_except_table10603
- GCC_except_table10606
- GCC_except_table10607
- GCC_except_table10954
- GCC_except_table11002
- GCC_except_table11015
- GCC_except_table1120
- GCC_except_table1124
- GCC_except_table1131
- GCC_except_table11384
- GCC_except_table11386
- GCC_except_table11388
- GCC_except_table11419
- GCC_except_table11421
- GCC_except_table11424
- GCC_except_table11431
- GCC_except_table11433
- GCC_except_table11541
- GCC_except_table11542
- GCC_except_table11568
- GCC_except_table11570
- GCC_except_table11574
- GCC_except_table11575
- GCC_except_table11623
- GCC_except_table11649
- GCC_except_table11662
- GCC_except_table11688
- GCC_except_table11692
- GCC_except_table11746
- GCC_except_table11747
- GCC_except_table11748
- GCC_except_table11749
- GCC_except_table11750
- GCC_except_table11751
- GCC_except_table11752
- GCC_except_table11753
- GCC_except_table11754
- GCC_except_table11755
- GCC_except_table11784
- GCC_except_table11811
- GCC_except_table11921
- GCC_except_table11922
- GCC_except_table11925
- GCC_except_table11990
- GCC_except_table11992
- GCC_except_table12011
- GCC_except_table12013
- GCC_except_table12018
- GCC_except_table12019
- GCC_except_table12020
- GCC_except_table12225
- GCC_except_table1223
- GCC_except_table1232
- GCC_except_table12425
- GCC_except_table12428
- GCC_except_table12433
- GCC_except_table12437
- GCC_except_table12448
- GCC_except_table12450
- GCC_except_table12455
- GCC_except_table12456
- GCC_except_table12540
- GCC_except_table12542
- GCC_except_table12561
- GCC_except_table12562
- GCC_except_table12563
- GCC_except_table12564
- GCC_except_table12569
- GCC_except_table12583
- GCC_except_table12589
- GCC_except_table12592
- GCC_except_table12594
- GCC_except_table12672
- GCC_except_table12680
- GCC_except_table12681
- GCC_except_table12686
- GCC_except_table12692
- GCC_except_table12694
- GCC_except_table12698
- GCC_except_table12700
- GCC_except_table12837
- GCC_except_table12893
- GCC_except_table12894
- GCC_except_table12895
- GCC_except_table12896
- GCC_except_table12907
- GCC_except_table12931
- GCC_except_table12932
- GCC_except_table12988
- GCC_except_table1300
- GCC_except_table13010
- GCC_except_table13013
- GCC_except_table1305
- GCC_except_table13110
- GCC_except_table1313
- GCC_except_table13153
- GCC_except_table13348
- GCC_except_table13353
- GCC_except_table13356
- GCC_except_table13416
- GCC_except_table13516
- GCC_except_table13587
- GCC_except_table13590
- GCC_except_table13610
- GCC_except_table13612
- GCC_except_table13613
- GCC_except_table1362
- GCC_except_table1511
- GCC_except_table1534
- GCC_except_table1602
- GCC_except_table1657
- GCC_except_table1660
- GCC_except_table1678
- GCC_except_table1745
- GCC_except_table1758
- GCC_except_table1872
- GCC_except_table1942
- GCC_except_table1945
- GCC_except_table2017
- GCC_except_table2103
- GCC_except_table2104
- GCC_except_table2153
- GCC_except_table2356
- GCC_except_table2359
- GCC_except_table2362
- GCC_except_table2367
- GCC_except_table2371
- GCC_except_table2380
- GCC_except_table2393
- GCC_except_table2396
- GCC_except_table2401
- GCC_except_table2402
- GCC_except_table2817
- GCC_except_table2822
- GCC_except_table2848
- GCC_except_table2851
- GCC_except_table2864
- GCC_except_table2901
- GCC_except_table2917
- GCC_except_table2920
- GCC_except_table2945
- GCC_except_table3112
- GCC_except_table3130
- GCC_except_table3131
- GCC_except_table3177
- GCC_except_table3203
- GCC_except_table3208
- GCC_except_table3209
- GCC_except_table3233
- GCC_except_table3243
- GCC_except_table3252
- GCC_except_table3253
- GCC_except_table3257
- GCC_except_table3319
- GCC_except_table3342
- GCC_except_table3345
- GCC_except_table3348
- GCC_except_table3351
- GCC_except_table3354
- GCC_except_table3357
- GCC_except_table3360
- GCC_except_table3425
- GCC_except_table3426
- GCC_except_table3472
- GCC_except_table3479
- GCC_except_table3480
- GCC_except_table3484
- GCC_except_table3485
- GCC_except_table3496
- GCC_except_table3518
- GCC_except_table3525
- GCC_except_table3529
- GCC_except_table3532
- GCC_except_table3535
- GCC_except_table3576
- GCC_except_table3580
- GCC_except_table3584
- GCC_except_table3589
- GCC_except_table3597
- GCC_except_table3601
- GCC_except_table3610
- GCC_except_table3851
- GCC_except_table3855
- GCC_except_table3859
- GCC_except_table3862
- GCC_except_table3866
- GCC_except_table3867
- GCC_except_table3870
- GCC_except_table3876
- GCC_except_table3880
- GCC_except_table3884
- GCC_except_table3907
- GCC_except_table3914
- GCC_except_table3915
- GCC_except_table3920
- GCC_except_table4000
- GCC_except_table4014
- GCC_except_table4017
- GCC_except_table4022
- GCC_except_table4029
- GCC_except_table4082
- GCC_except_table4147
- GCC_except_table4162
- GCC_except_table4165
- GCC_except_table4258
- GCC_except_table4259
- GCC_except_table4266
- GCC_except_table4270
- GCC_except_table4273
- GCC_except_table4283
- GCC_except_table4530
- GCC_except_table4533
- GCC_except_table4545
- GCC_except_table4619
- GCC_except_table4663
- GCC_except_table4755
- GCC_except_table4917
- GCC_except_table4929
- GCC_except_table4955
- GCC_except_table4956
- GCC_except_table5013
- GCC_except_table5023
- GCC_except_table5152
- GCC_except_table5153
- GCC_except_table5229
- GCC_except_table5331
- GCC_except_table5361
- GCC_except_table538
- GCC_except_table5381
- GCC_except_table541
- GCC_except_table5427
- GCC_except_table549
- GCC_except_table552
- GCC_except_table5522
- GCC_except_table5542
- GCC_except_table5543
- GCC_except_table5549
- GCC_except_table5550
- GCC_except_table5810
- GCC_except_table5816
- GCC_except_table5828
- GCC_except_table5829
- GCC_except_table6032
- GCC_except_table6036
- GCC_except_table6109
- GCC_except_table6240
- GCC_except_table6247
- GCC_except_table6252
- GCC_except_table6437
- GCC_except_table6490
- GCC_except_table6679
- GCC_except_table6688
- GCC_except_table6696
- GCC_except_table6716
- GCC_except_table6725
- GCC_except_table6730
- GCC_except_table6733
- GCC_except_table6747
- GCC_except_table6752
- GCC_except_table6758
- GCC_except_table6763
- GCC_except_table6768
- GCC_except_table6773
- GCC_except_table6778
- GCC_except_table6782
- GCC_except_table6787
- GCC_except_table6839
- GCC_except_table6843
- GCC_except_table6851
- GCC_except_table6856
- GCC_except_table6870
- GCC_except_table6875
- GCC_except_table6882
- GCC_except_table6897
- GCC_except_table6898
- GCC_except_table6905
- GCC_except_table6910
- GCC_except_table6917
- GCC_except_table6922
- GCC_except_table6926
- GCC_except_table6960
- GCC_except_table7017
- GCC_except_table7021
- GCC_except_table7024
- GCC_except_table710
- GCC_except_table713
- GCC_except_table7163
- GCC_except_table7170
- GCC_except_table718
- GCC_except_table721
- GCC_except_table722
- GCC_except_table7255
- GCC_except_table7288
- GCC_except_table7343
- GCC_except_table7371
- GCC_except_table7399
- GCC_except_table7413
- GCC_except_table7429
- GCC_except_table7435
- GCC_except_table744
- GCC_except_table7446
- GCC_except_table7479
- GCC_except_table7492
- GCC_except_table7493
- GCC_except_table7498
- GCC_except_table7517
- GCC_except_table7544
- GCC_except_table7558
- GCC_except_table7576
- GCC_except_table761
- GCC_except_table7756
- GCC_except_table780
- GCC_except_table8019
- GCC_except_table8062
- GCC_except_table8122
- GCC_except_table8238
- GCC_except_table8241
- GCC_except_table830
- GCC_except_table833
- GCC_except_table8331
- GCC_except_table834
- GCC_except_table8350
- GCC_except_table8360
- GCC_except_table8496
- GCC_except_table8505
- GCC_except_table8518
- GCC_except_table8525
- GCC_except_table8564
- GCC_except_table8566
- GCC_except_table8594
- GCC_except_table8596
- GCC_except_table8598
- GCC_except_table8600
- GCC_except_table8607
- GCC_except_table8613
- GCC_except_table8617
- GCC_except_table8627
- GCC_except_table8633
- GCC_except_table8719
- GCC_except_table8721
- GCC_except_table8731
- GCC_except_table8733
- GCC_except_table8735
- GCC_except_table8737
- GCC_except_table8739
- GCC_except_table8745
- GCC_except_table8749
- GCC_except_table8762
- GCC_except_table8764
- GCC_except_table8766
- GCC_except_table8768
- GCC_except_table8787
- GCC_except_table8944
- GCC_except_table8946
- GCC_except_table8947
- GCC_except_table8948
- GCC_except_table8950
- GCC_except_table8954
- GCC_except_table8989
- GCC_except_table8992
- GCC_except_table8993
- GCC_except_table8996
- GCC_except_table8999
- GCC_except_table900
- GCC_except_table9000
- GCC_except_table904
- GCC_except_table9043
- GCC_except_table9044
- GCC_except_table9045
- GCC_except_table905
- GCC_except_table9052
- GCC_except_table9053
- GCC_except_table9055
- GCC_except_table9074
- GCC_except_table9146
- GCC_except_table9147
- GCC_except_table9148
- GCC_except_table9185
- GCC_except_table920
- GCC_except_table921
- GCC_except_table9369
- GCC_except_table9370
- GCC_except_table9371
- GCC_except_table9430
- GCC_except_table9451
- GCC_except_table9527
- GCC_except_table9529
- GCC_except_table9531
- GCC_except_table9533
- GCC_except_table9541
- GCC_except_table9588
- GCC_except_table9600
- GCC_except_table9602
- GCC_except_table9618
- GCC_except_table9646
- GCC_except_table9820
- GCC_except_table9822
- GCC_except_table9824
- GCC_except_table9868
- GCC_except_table9869
- GCC_except_table9904
- GCC_except_table9937
- GCC_except_table9940
- GCC_except_table9943
- _CoreAnalyticsLibraryCore.frameworkLibrary.41013
- _CoreHAPLibraryCore.frameworkLibrary.33293
- _IDSFoundationLibraryCore.45323
- _IDSFoundationLibraryCore.frameworkLibrary.45326
- _UIKitLibrary.45550
- _UIKitLibraryCore.45546
- _UIKitLibraryCore.frameworkLibrary.45559
- __OBJC_$_CLASS_METHODS_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|OSEligibility|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
- __OBJC_$_INSTANCE_METHODS_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|OSEligibility|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
- __OBJC_$_PROP_LIST_HMEventTriggerBuilder.217
- __OBJC_$_PROP_LIST_HMMediaDestination.20098
- __OBJC_CLASS_PROTOCOLS_$_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|OSEligibility|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
- ___102-[HMHome(HMModernMessaging) unregisterModernMessagingRequestHandlerWithMessageName:completionHandler:]_block_invoke.2285
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.795
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.797
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.805
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke.807
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.800
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_3.804
- ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2240
- ___123-[HMHome(HMModernMessaging) registerModernMessagingRequestHandlerWithMessageName:options:requestHandler:completionHandler:]_block_invoke.2284
- ___140-[HMHome(HMModernMessaging) sendModernMessagingRequestWithMessageName:destination:requestPayload:options:responseHandler:completionHandler:]_block_invoke.2287
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1327
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1328
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1330
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1332
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1333
- ___30-[HMAccessory _mergeServices:]_block_invoke.1120
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1122
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1123
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1127
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1130
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1147
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1150
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1154
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1159
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1292
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1294
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1296
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1297
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1299
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1304
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1306
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1307
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1309
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1124
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1128
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1131
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1148
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1151
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1155
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1160
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1293
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1295
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1300
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1303
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1314
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1318
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1156
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1319
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1157
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1321
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1164
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1322
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1286
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1324
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_7.1325
- ___38-[HMHomeManager _updateDataSyncState:]_block_invoke.537
- ___39-[HMCharacteristic mergeFromNewObject:]_block_invoke.255
- ___39-[HMCharacteristic mergeFromNewObject:]_block_invoke_2.256
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.809
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.811
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1360
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1362
- ___46-[HMHomeManager removeHome:completionHandler:]_block_invoke.650
- ___47-[HMHomeManager _recomputeAssistantIdentifiers]_block_invoke.719
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1348
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1349
- ___51-[HMHomeManager _updatePrimaryHome:notifyDelegate:]_block_invoke.776
- ___51-[HMHomeManager addHomeWithName:completionHandler:]_block_invoke.646
- ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.2058
- ___54-[HMHome(PowerAssertionInfo) fetchPowerAssertionInfo:]_block_invoke.2222
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.632
- ___54-[HMHomeManager _refreshBeforeDate:completionHandler:]_block_invoke.633
- ___57-[HMAccessory _mergeBulletinBoardNotificationByEndpoint:]_block_invoke.1117
- ___59-[HMHome(HMModernMessagingInternal) reRegisterHMMMHandlers]_block_invoke.2296
- ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2247
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.1046
- ___63-[HMAccessory pairingIdentityWithPrivateKey:completionHandler:]_block_invoke.1048
- ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.2136
- ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke.2227
- ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke_2.2228
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.737
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.741
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.743
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke.745
- ___68-[HMHomeManager _processHomeConfigurationResponse:refreshRequested:]_block_invoke_2.746
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.868
- ___71-[HMHome(HomeActivityState) changeHomeActivityState:completionHandler:]_block_invoke.2246
- ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke.2225
- ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke_2.2226
- ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke.2229
- ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke_2.2230
- ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke.2301
- ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke_2.2302
- ___74-[HMHomeManager __processSyncResponse:refreshRequested:completionHandler:]_block_invoke.716
- ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1919
- ___78-[HMHome(HomeActivityState) cancelHomeActivityStateHoldWithCompletionHandler:]_block_invoke.2250
- ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1930
- ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1921
- ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.2237
- ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.2191
- ___Block_byref_object_copy_.16739
- ___Block_byref_object_copy_.17073
- ___Block_byref_object_copy_.24685
- ___Block_byref_object_copy_.27020
- ___Block_byref_object_copy_.33390
- ___Block_byref_object_copy_.35577
- ___Block_byref_object_copy_.40900
- ___Block_byref_object_copy_.44353
- ___Block_byref_object_copy_.64117
- ___Block_byref_object_copy_.66530
- ___Block_byref_object_dispose_.16740
- ___Block_byref_object_dispose_.17074
- ___Block_byref_object_dispose_.24686
- ___Block_byref_object_dispose_.27021
- ___Block_byref_object_dispose_.33391
- ___Block_byref_object_dispose_.35578
- ___Block_byref_object_dispose_.40901
- ___Block_byref_object_dispose_.44354
- ___Block_byref_object_dispose_.64118
- ___Block_byref_object_dispose_.66531
- ___CoreAnalyticsLibraryCore_block_invoke.41014
- ___CoreHAPLibraryCore_block_invoke.33294
- ___IDSFoundationLibraryCore_block_invoke.45327
- ___UIKitLibraryCore_block_invoke.45560
- ___block_descriptor_40_e8_32w_e17_v16?0"NSArray"8lw32l8
- ___block_literal_global.101.41021
- ___block_literal_global.101.43204
- ___block_literal_global.11099
- ___block_literal_global.1167
- ___block_literal_global.11681
- ___block_literal_global.12.51727
- ___block_literal_global.12396
- ___block_literal_global.1344
- ___block_literal_global.14539
- ___block_literal_global.14680
- ___block_literal_global.14755
- ___block_literal_global.15002
- ___block_literal_global.15375
- ___block_literal_global.1560
- ___block_literal_global.15604
- ___block_literal_global.16186
- ___block_literal_global.16536
- ___block_literal_global.16827
- ___block_literal_global.17.20318
- ___block_literal_global.17455
- ___block_literal_global.18663
- ___block_literal_global.19.16521
- ___block_literal_global.19194
- ___block_literal_global.19375
- ___block_literal_global.1938
- ___block_literal_global.19508
- ___block_literal_global.19668
- ___block_literal_global.20325
- ___block_literal_global.2055
- ___block_literal_global.2057
- ___block_literal_global.2078
- ___block_literal_global.20983
- ___block_literal_global.2133
- ___block_literal_global.21448
- ___block_literal_global.22087
- ___block_literal_global.22454
- ___block_literal_global.23425
- ___block_literal_global.23729
- ___block_literal_global.24062
- ___block_literal_global.24723
- ___block_literal_global.24912
- ___block_literal_global.25107
- ___block_literal_global.2574
- ___block_literal_global.25879
- ___block_literal_global.26249
- ___block_literal_global.26386
- ___block_literal_global.26632
- ___block_literal_global.26877
- ___block_literal_global.27044
- ___block_literal_global.27137
- ___block_literal_global.27868
- ___block_literal_global.29898
- ___block_literal_global.30.20307
- ___block_literal_global.30056
- ___block_literal_global.30335
- ___block_literal_global.31614
- ___block_literal_global.32219
- ___block_literal_global.32481
- ___block_literal_global.32768
- ___block_literal_global.32847
- ___block_literal_global.33.65826
- ___block_literal_global.33537
- ___block_literal_global.34037
- ___block_literal_global.34310
- ___block_literal_global.35363
- ___block_literal_global.35600
- ___block_literal_global.35901
- ___block_literal_global.36
- ___block_literal_global.37226
- ___block_literal_global.38205
- ___block_literal_global.38439
- ___block_literal_global.38666
- ___block_literal_global.39061
- ___block_literal_global.39811
- ___block_literal_global.4065
- ___block_literal_global.41008
- ___block_literal_global.41259
- ___block_literal_global.41596
- ___block_literal_global.42258
- ___block_literal_global.43214
- ___block_literal_global.43477
- ___block_literal_global.43743
- ___block_literal_global.4402
- ___block_literal_global.44025
- ___block_literal_global.44245
- ___block_literal_global.4488
- ___block_literal_global.45387
- ___block_literal_global.45478
- ___block_literal_global.4581
- ___block_literal_global.46185
- ___block_literal_global.46377
- ___block_literal_global.47557
- ___block_literal_global.47998
- ___block_literal_global.48323
- ___block_literal_global.49087
- ___block_literal_global.49744
- ___block_literal_global.50102
- ___block_literal_global.51
- ___block_literal_global.51375
- ___block_literal_global.51739
- ___block_literal_global.52023
- ___block_literal_global.52219
- ___block_literal_global.523
- ___block_literal_global.52448
- ___block_literal_global.53166
- ___block_literal_global.53286
- ___block_literal_global.54041
- ___block_literal_global.54275
- ___block_literal_global.5441
- ___block_literal_global.54730
- ___block_literal_global.54992
- ___block_literal_global.56070
- ___block_literal_global.58.38434
- ___block_literal_global.58351
- ___block_literal_global.59216
- ___block_literal_global.6027
- ___block_literal_global.60503
- ___block_literal_global.61232
- ___block_literal_global.61783
- ___block_literal_global.62093
- ___block_literal_global.62610
- ___block_literal_global.62787
- ___block_literal_global.63176
- ___block_literal_global.63421
- ___block_literal_global.6426
- ___block_literal_global.65230
- ___block_literal_global.65565
- ___block_literal_global.6562
- ___block_literal_global.65832
- ___block_literal_global.66187
- ___block_literal_global.66469
- ___block_literal_global.66825
- ___block_literal_global.6789
- ___block_literal_global.7.24923
- ___block_literal_global.710
- ___block_literal_global.7281
- ___block_literal_global.73.25081
- ___block_literal_global.758
- ___block_literal_global.760
- ___block_literal_global.7645
- ___block_literal_global.7792
- ___block_literal_global.8295
- ___block_literal_global.84.41202
- ___block_literal_global.8549
- ___block_literal_global.872
- ___block_literal_global.9135
- ___block_literal_global.9378
- ___block_literal_global.9776
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.41011
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.45555
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.45549
- _audit_stringCoreAnalytics.41017
- _audit_stringCoreHAP.33296
- _audit_stringIDSFoundation.45329
- _audit_stringUIKit.45562
- _getAnalyticsSendEventLazySymbolLoc.ptr.41010
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.45554
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.45548
- _logCategory._hmf_once_t0.14754
- _logCategory._hmf_once_t0.23728
- _logCategory._hmf_once_t0.25106
- _logCategory._hmf_once_t0.32480
- _logCategory._hmf_once_t0.32846
- _logCategory._hmf_once_t0.44024
- _logCategory._hmf_once_t0.46184
- _logCategory._hmf_once_t0.46376
- _logCategory._hmf_once_t0.6026
- _logCategory._hmf_once_t0.63420
- _logCategory._hmf_once_t1.19507
- _logCategory._hmf_once_t1.21447
- _logCategory._hmf_once_t1.41235
- _logCategory._hmf_once_t1.47556
- _logCategory._hmf_once_t1.51726
- _logCategory._hmf_once_t1.53285
- _logCategory._hmf_once_t1.58350
- _logCategory._hmf_once_t10.23424
- _logCategory._hmf_once_t11.7644
- _logCategory._hmf_once_t13.43203
- _logCategory._hmf_once_t16.38438
- _logCategory._hmf_once_t16.65229
- _logCategory._hmf_once_t2.24922
- _logCategory._hmf_once_t2.27043
- _logCategory._hmf_once_t2.30334
- _logCategory._hmf_once_t2.34036
- _logCategory._hmf_once_t20.25646
- _logCategory._hmf_once_t20.26631
- _logCategory._hmf_once_t21.62786
- _logCategory._hmf_once_t24.41595
- _logCategory._hmf_once_t24.42257
- _logCategory._hmf_once_t25.26876
- _logCategory._hmf_once_t25.66186
- _logCategory._hmf_once_t27.62092
- _logCategory._hmf_once_t3.54264
- _logCategory._hmf_once_t3.65825
- _logCategory._hmf_once_t31.24722
- _logCategory._hmf_once_t31.54729
- _logCategory._hmf_once_t31.66824
- _logCategory._hmf_once_t32.54040
- _logCategory._hmf_once_t34.20982
- _logCategory._hmf_once_t37.55018
- _logCategory._hmf_once_t379
- _logCategory._hmf_once_t4.15001
- _logCategory._hmf_once_t4.1571
- _logCategory._hmf_once_t4.6425
- _logCategory._hmf_once_t44.26901
- _logCategory._hmf_once_t5.19193
- _logCategory._hmf_once_t51.43742
- _logCategory._hmf_once_t6.35362
- _logCategory._hmf_once_t6.38204
- _logCategory._hmf_once_t6.44244
- _logCategory._hmf_once_t6.49743
- _logCategory._hmf_once_t6.59215
- _logCategory._hmf_once_t7.53165
- _logCategory._hmf_once_t8.38665
- _logCategory._hmf_once_t8.49086
- _logCategory._hmf_once_t8.52237
- _logCategory._hmf_once_t9.30055
- _logCategory._hmf_once_v1.14756
- _logCategory._hmf_once_v1.23730
- _logCategory._hmf_once_v1.25108
- _logCategory._hmf_once_v1.32482
- _logCategory._hmf_once_v1.32848
- _logCategory._hmf_once_v1.44026
- _logCategory._hmf_once_v1.46186
- _logCategory._hmf_once_v1.46378
- _logCategory._hmf_once_v1.6028
- _logCategory._hmf_once_v1.63422
- _logCategory._hmf_once_v10.30057
- _logCategory._hmf_once_v11.23426
- _logCategory._hmf_once_v12.7646
- _logCategory._hmf_once_v14.43205
- _logCategory._hmf_once_v17.38440
- _logCategory._hmf_once_v17.65231
- _logCategory._hmf_once_v2.19509
- _logCategory._hmf_once_v2.21449
- _logCategory._hmf_once_v2.41236
- _logCategory._hmf_once_v2.47558
- _logCategory._hmf_once_v2.51728
- _logCategory._hmf_once_v2.53287
- _logCategory._hmf_once_v2.58352
- _logCategory._hmf_once_v21.25647
- _logCategory._hmf_once_v21.26633
- _logCategory._hmf_once_v22.62788
- _logCategory._hmf_once_v25.41597
- _logCategory._hmf_once_v25.42259
- _logCategory._hmf_once_v26.26878
- _logCategory._hmf_once_v26.66188
- _logCategory._hmf_once_v28.62094
- _logCategory._hmf_once_v3.24924
- _logCategory._hmf_once_v3.27045
- _logCategory._hmf_once_v3.30336
- _logCategory._hmf_once_v3.34038
- _logCategory._hmf_once_v32.24724
- _logCategory._hmf_once_v32.54731
- _logCategory._hmf_once_v32.66826
- _logCategory._hmf_once_v33.54042
- _logCategory._hmf_once_v35.20984
- _logCategory._hmf_once_v38.55019
- _logCategory._hmf_once_v380
- _logCategory._hmf_once_v4.54265
- _logCategory._hmf_once_v4.65827
- _logCategory._hmf_once_v45.26902
- _logCategory._hmf_once_v5.15003
- _logCategory._hmf_once_v5.1572
- _logCategory._hmf_once_v5.6427
- _logCategory._hmf_once_v52.43744
- _logCategory._hmf_once_v6.19195
- _logCategory._hmf_once_v7.35364
- _logCategory._hmf_once_v7.38206
- _logCategory._hmf_once_v7.44246
- _logCategory._hmf_once_v7.49745
- _logCategory._hmf_once_v7.59217
- _logCategory._hmf_once_v8.53167
- _logCategory._hmf_once_v9.38667
- _logCategory._hmf_once_v9.49088
- _logCategory._hmf_once_v9.52238
- _objc_msgSend$initWithName:uuid:mediaSystems:
- _sharedInstance.onceToken.43213
- _sharedManager.onceToken.62238
- _supportedValueClasses.onceToken.52022
- _supportedValueClasses.onceToken.60466
- _supportedValueClasses.supportedValueClasses.52024
- _supportedValueClasses.supportedValueClasses.60467
CStrings:
+ "%#"
+ "%{public}@Characteristics of type %@ has fixed value. So skipping reads to the accessory"
+ "%{public}@[%{public}@] Find vendor accessory failed: %@"
+ "%{public}@[%{public}@] Find vendor accessory with HAP LTPK %@"
+ "%{public}@[%{public}@] Found accessory %@"
+ "%{public}@[%{public}@] No accessory found"
+ "%{public}@findVendorAccessory... called before homeManagerDidUpdateHomes:"
+ "-[HMHomeManager(Vendor) findVendorAccessoryWithHAPPublicKey:completionHandler:]"
+ "/Library/Caches/com.apple.xbs/Sources/HomeKit/Sources/HomeKit/Vendor/HMHomeManager+Vendor.m"
+ "HAPInstanceID"
+ "HMAccessoryHAPInstanceIDCodingKey"
+ "HMAccessoryIsVendorAccessoryCodingKey"
+ "HMHM.findVendorAccessory"
+ "T@\"NSNumber\",R,C,N,V_HAPInstanceID"
+ "TB,N,V_hasFixedValue"
+ "TB,R,N,GisInitialMergeComplete,V_initialMergeComplete"
+ "TB,R,N,GisVendorAccessory,V_vendorAccessory"
+ "_HAPInstanceID"
+ "_hasFixedValue"
+ "_vendorAccessory"
+ "findVendorAccessoryWithHAPPublicKey:completionHandler:"
+ "hasFixedValue"
+ "initWithName:uuid:accessories:mediaSystems:"
+ "isVendorAccessory"
+ "kAccessoryPublicKey"
+ "kCharacteristicHasFixedValueKey"
+ "setHAPInstanceID:"
+ "setHasFixedValue:"
+ "setVendorAccessory:"
+ "uuidFromStringForKey:"
+ "vendorAccessory"
- "T@\"HMHome\",R,W,N"
- "TB,N,GisInitialMergeComplete,V_initialMergeComplete"
- "initWithName:uuid:mediaSystems:"
- "setInitialMergeComplete:"

```
