## HomeKit

> `/System/Library/Frameworks/HomeKit.framework/HomeKit`

```diff

-1340.3.0.0.0
-  __TEXT.__text: 0x2c99cc
-  __TEXT.__auth_stubs: 0x1af0
-  __TEXT.__objc_methlist: 0x257b4
+1345.1.0.1.1
+  __TEXT.__text: 0x2c8578
+  __TEXT.__auth_stubs: 0x1b00
+  __TEXT.__objc_methlist: 0x257bc
   __TEXT.__const: 0x1d0c
   __TEXT.__dlopen_cstrs: 0x3a1
-  __TEXT.__cstring: 0x2a563
+  __TEXT.__cstring: 0x2a4ce
   __TEXT.__swift5_typeref: 0xa4c
   __TEXT.__constg_swiftt: 0x8fc
   __TEXT.__swift5_reflstr: 0x391

   __TEXT.__swift5_types: 0xa4
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__oslogstring: 0x2ac80
+  __TEXT.__oslogstring: 0x2ab40
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__gcc_except_tab: 0x706c
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0x9a78
+  __TEXT.__unwind_info: 0x9a50
   __TEXT.__eh_frame: 0xd88
-  __TEXT.__objc_classname: 0x4fb3
-  __TEXT.__objc_methname: 0x482a2
+  __TEXT.__objc_classname: 0x4fc1
+  __TEXT.__objc_methname: 0x48353
   __TEXT.__objc_methtype: 0x88d8
   __TEXT.__objc_stubs: 0x25c40
   __DATA_CONST.__got: 0x1818
-  __DATA_CONST.__const: 0x7de0
+  __DATA_CONST.__const: 0x7e08
   __DATA_CONST.__objc_classlist: 0x1228
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x4b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd178
+  __DATA_CONST.__objc_selrefs: 0xd180
   __DATA_CONST.__objc_protorefs: 0xb8
   __DATA_CONST.__objc_superrefs: 0xf30
   __DATA_CONST.__objc_arraydata: 0x1380
-  __AUTH_CONST.__auth_got: 0xd88
+  __AUTH_CONST.__auth_got: 0xd90
   __AUTH_CONST.__const: 0x2a30
-  __AUTH_CONST.__cfstring: 0x277e0
-  __AUTH_CONST.__objc_const: 0x43698
+  __AUTH_CONST.__cfstring: 0x277a0
+  __AUTH_CONST.__objc_const: 0x436b0
   __AUTH_CONST.__objc_intobj: 0x7c8
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x570

   __AUTH.__data: 0x580
   __DATA.__objc_ivar: 0x2528
   __DATA.__data: 0x3e08
-  __DATA.__bss: 0x31c0
+  __DATA.__bss: 0x31d0
   __DATA.__common: 0x59
   __DATA_DIRTY.__objc_data: 0x32a0
   __DATA_DIRTY.__data: 0x10
-  __DATA_DIRTY.__bss: 0x260
+  __DATA_DIRTY.__bss: 0x250
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 71A72193-0B9D-3042-9A91-5821687C498B
-  Functions: 14339
-  Symbols:   44058
-  CStrings:  25664
+  UUID: 506F74F8-B5BF-3192-A080-44FAD67B3BB5
+  Functions: 14331
+  Symbols:   44044
+  CStrings:  25657
 
Symbols:
+ +[HMHomeManager(OSEligibility) shouldDisableWiFiPickerBasedOnOSEligibility]
+ -[HMHome _setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:]
+ -[HMHome _setNotificationsEnabled:forCharacteristics:completionHandler:]
+ -[HMHome addUser:withCompletionHandler:]
+ -[HMHome addUserWithoutConfirmation:privilege:completionHandler:]
+ -[HMHome inviteUsers:completionHandler:]
+ -[HMHome reenableNotifications]
+ -[HMHome removeUserWithoutConfirmation:completionHandler:]
+ -[HMHome setAllNotificationsEnabled:completionHandler:]
+ -[HMHome setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:]
+ -[HMHome setNotificationsEnabled:forCharacteristics:completionHandler:]
+ -[HMSetupAccessoryDescription matterSystemCommissionerPairingIsNew]
+ -[HMSetupAccessoryDescription matterSystemCommissionerPairingUUID]
+ -[HMSetupAccessoryDescription setMatterSystemCommissionerPairingIsNew:]
+ -[HMSetupAccessoryDescription setMatterSystemCommissionerPairingUUID:]
+ GCC_except_table10000
+ GCC_except_table10002
+ GCC_except_table10004
+ GCC_except_table10067
+ GCC_except_table10099
+ GCC_except_table10101
+ GCC_except_table10105
+ GCC_except_table10122
+ GCC_except_table10124
+ GCC_except_table10130
+ GCC_except_table10134
+ GCC_except_table10137
+ GCC_except_table10144
+ GCC_except_table10148
+ GCC_except_table10154
+ GCC_except_table10166
+ GCC_except_table10169
+ GCC_except_table10178
+ GCC_except_table10180
+ GCC_except_table10182
+ GCC_except_table10184
+ GCC_except_table10196
+ GCC_except_table10206
+ GCC_except_table10409
+ GCC_except_table10422
+ GCC_except_table10471
+ GCC_except_table10476
+ GCC_except_table10480
+ GCC_except_table10488
+ GCC_except_table10536
+ GCC_except_table10539
+ GCC_except_table10540
+ GCC_except_table10887
+ GCC_except_table10935
+ GCC_except_table10948
+ GCC_except_table11317
+ GCC_except_table11319
+ GCC_except_table11321
+ GCC_except_table11322
+ GCC_except_table11352
+ GCC_except_table11354
+ GCC_except_table11357
+ GCC_except_table11364
+ GCC_except_table11366
+ GCC_except_table11474
+ GCC_except_table11475
+ GCC_except_table11501
+ GCC_except_table11503
+ GCC_except_table11507
+ GCC_except_table11508
+ GCC_except_table11556
+ GCC_except_table11582
+ GCC_except_table11595
+ GCC_except_table11621
+ GCC_except_table11625
+ GCC_except_table11679
+ GCC_except_table11680
+ GCC_except_table11681
+ GCC_except_table11682
+ GCC_except_table11683
+ GCC_except_table11684
+ GCC_except_table11685
+ GCC_except_table11686
+ GCC_except_table11717
+ GCC_except_table11744
+ GCC_except_table11854
+ GCC_except_table11855
+ GCC_except_table11858
+ GCC_except_table11923
+ GCC_except_table11925
+ GCC_except_table11944
+ GCC_except_table11946
+ GCC_except_table11951
+ GCC_except_table11953
+ GCC_except_table12158
+ GCC_except_table12358
+ GCC_except_table12361
+ GCC_except_table12370
+ GCC_except_table12376
+ GCC_except_table12381
+ GCC_except_table12383
+ GCC_except_table12388
+ GCC_except_table12473
+ GCC_except_table12475
+ GCC_except_table12494
+ GCC_except_table12495
+ GCC_except_table12496
+ GCC_except_table12497
+ GCC_except_table12516
+ GCC_except_table12522
+ GCC_except_table12525
+ GCC_except_table12527
+ GCC_except_table12605
+ GCC_except_table12614
+ GCC_except_table12619
+ GCC_except_table12625
+ GCC_except_table12629
+ GCC_except_table12631
+ GCC_except_table12770
+ GCC_except_table12826
+ GCC_except_table12827
+ GCC_except_table12828
+ GCC_except_table12829
+ GCC_except_table12839
+ GCC_except_table12840
+ GCC_except_table12864
+ GCC_except_table12865
+ GCC_except_table12921
+ GCC_except_table12943
+ GCC_except_table12946
+ GCC_except_table13043
+ GCC_except_table13086
+ GCC_except_table13281
+ GCC_except_table13286
+ GCC_except_table13349
+ GCC_except_table13434
+ GCC_except_table13444
+ GCC_except_table13505
+ GCC_except_table13508
+ GCC_except_table13528
+ GCC_except_table13530
+ GCC_except_table13531
+ GCC_except_table2761
+ GCC_except_table2766
+ GCC_except_table2792
+ GCC_except_table2795
+ GCC_except_table2808
+ GCC_except_table2845
+ GCC_except_table2861
+ GCC_except_table2864
+ GCC_except_table2893
+ GCC_except_table2895
+ GCC_except_table3056
+ GCC_except_table3074
+ GCC_except_table3075
+ GCC_except_table3121
+ GCC_except_table3123
+ GCC_except_table3147
+ GCC_except_table3152
+ GCC_except_table3153
+ GCC_except_table3177
+ GCC_except_table3179
+ GCC_except_table3187
+ GCC_except_table3189
+ GCC_except_table3201
+ GCC_except_table3202
+ GCC_except_table3203
+ GCC_except_table3204
+ GCC_except_table3263
+ GCC_except_table3286
+ GCC_except_table3289
+ GCC_except_table3292
+ GCC_except_table3295
+ GCC_except_table3298
+ GCC_except_table3301
+ GCC_except_table3304
+ GCC_except_table3369
+ GCC_except_table3370
+ GCC_except_table3416
+ GCC_except_table3423
+ GCC_except_table3429
+ GCC_except_table3430
+ GCC_except_table3432
+ GCC_except_table3440
+ GCC_except_table3462
+ GCC_except_table3473
+ GCC_except_table3476
+ GCC_except_table3479
+ GCC_except_table3528
+ GCC_except_table3533
+ GCC_except_table3545
+ GCC_except_table3554
+ GCC_except_table3556
+ GCC_except_table3803
+ GCC_except_table3811
+ GCC_except_table3814
+ GCC_except_table3828
+ GCC_except_table3853
+ GCC_except_table3858
+ GCC_except_table3859
+ GCC_except_table3861
+ GCC_except_table3864
+ GCC_except_table3944
+ GCC_except_table3958
+ GCC_except_table3961
+ GCC_except_table3963
+ GCC_except_table3966
+ GCC_except_table3973
+ GCC_except_table4026
+ GCC_except_table4091
+ GCC_except_table4106
+ GCC_except_table4109
+ GCC_except_table4202
+ GCC_except_table4203
+ GCC_except_table4205
+ GCC_except_table4214
+ GCC_except_table4217
+ GCC_except_table4219
+ GCC_except_table4227
+ GCC_except_table4474
+ GCC_except_table4477
+ GCC_except_table4489
+ GCC_except_table4563
+ GCC_except_table4607
+ GCC_except_table4699
+ GCC_except_table4861
+ GCC_except_table4873
+ GCC_except_table4875
+ GCC_except_table4899
+ GCC_except_table4900
+ GCC_except_table4901
+ GCC_except_table4902
+ GCC_except_table4957
+ GCC_except_table4967
+ GCC_except_table5096
+ GCC_except_table5097
+ GCC_except_table5173
+ GCC_except_table5275
+ GCC_except_table5277
+ GCC_except_table5305
+ GCC_except_table5307
+ GCC_except_table5325
+ GCC_except_table5371
+ GCC_except_table5466
+ GCC_except_table5487
+ GCC_except_table5488
+ GCC_except_table5493
+ GCC_except_table5494
+ GCC_except_table5496
+ GCC_except_table5754
+ GCC_except_table5760
+ GCC_except_table5762
+ GCC_except_table5772
+ GCC_except_table5773
+ GCC_except_table5971
+ GCC_except_table6044
+ GCC_except_table6175
+ GCC_except_table6182
+ GCC_except_table6187
+ GCC_except_table6372
+ GCC_except_table6425
+ GCC_except_table6617
+ GCC_except_table6626
+ GCC_except_table6634
+ GCC_except_table6654
+ GCC_except_table6664
+ GCC_except_table6667
+ GCC_except_table6681
+ GCC_except_table6686
+ GCC_except_table6692
+ GCC_except_table6697
+ GCC_except_table6702
+ GCC_except_table6707
+ GCC_except_table6712
+ GCC_except_table6716
+ GCC_except_table6721
+ GCC_except_table6773
+ GCC_except_table6777
+ GCC_except_table6785
+ GCC_except_table6790
+ GCC_except_table6804
+ GCC_except_table6809
+ GCC_except_table6816
+ GCC_except_table6832
+ GCC_except_table6834
+ GCC_except_table6836
+ GCC_except_table6839
+ GCC_except_table6844
+ GCC_except_table6851
+ GCC_except_table6856
+ GCC_except_table6860
+ GCC_except_table6894
+ GCC_except_table6951
+ GCC_except_table6955
+ GCC_except_table6958
+ GCC_except_table7096
+ GCC_except_table7103
+ GCC_except_table7188
+ GCC_except_table7219
+ GCC_except_table7689
+ GCC_except_table7952
+ GCC_except_table7995
+ GCC_except_table8055
+ GCC_except_table8171
+ GCC_except_table8174
+ GCC_except_table8264
+ GCC_except_table8283
+ GCC_except_table8293
+ GCC_except_table8429
+ GCC_except_table8438
+ GCC_except_table8451
+ GCC_except_table8458
+ GCC_except_table8497
+ GCC_except_table8499
+ GCC_except_table8527
+ GCC_except_table8529
+ GCC_except_table8531
+ GCC_except_table8533
+ GCC_except_table8540
+ GCC_except_table8546
+ GCC_except_table8550
+ GCC_except_table8560
+ GCC_except_table8566
+ GCC_except_table8652
+ GCC_except_table8654
+ GCC_except_table8664
+ GCC_except_table8666
+ GCC_except_table8668
+ GCC_except_table8670
+ GCC_except_table8672
+ GCC_except_table8678
+ GCC_except_table8682
+ GCC_except_table8695
+ GCC_except_table8697
+ GCC_except_table8699
+ GCC_except_table8701
+ GCC_except_table8720
+ GCC_except_table8877
+ GCC_except_table8881
+ GCC_except_table8883
+ GCC_except_table8887
+ GCC_except_table8922
+ GCC_except_table8926
+ GCC_except_table8929
+ GCC_except_table8933
+ GCC_except_table8978
+ GCC_except_table8986
+ GCC_except_table8988
+ GCC_except_table9007
+ GCC_except_table9081
+ GCC_except_table9118
+ GCC_except_table9304
+ GCC_except_table9308
+ GCC_except_table9363
+ GCC_except_table9384
+ GCC_except_table9460
+ GCC_except_table9462
+ GCC_except_table9464
+ GCC_except_table9466
+ GCC_except_table9474
+ GCC_except_table9521
+ GCC_except_table9533
+ GCC_except_table9535
+ GCC_except_table9551
+ GCC_except_table9579
+ GCC_except_table9753
+ GCC_except_table9755
+ GCC_except_table9757
+ GCC_except_table9802
+ GCC_except_table9837
+ GCC_except_table9870
+ GCC_except_table9873
+ GCC_except_table9876
+ GCC_except_table9878
+ GCC_except_table9939
+ GCC_except_table9961
+ _CoreAnalyticsLibraryCore.frameworkLibrary.40536
+ _CoreHAPLibraryCore.frameworkLibrary.32825
+ _HMHomeAccessorySystemCommissionerUUIDKey
+ _HMHomeEnableHomeNotificationsMessage
+ _IDSFoundationLibraryCore.44867
+ _IDSFoundationLibraryCore.frameworkLibrary.44870
+ _OBJC_IVAR_$_HMSetupAccessoryDescription._matterSystemCommissionerPairingIsNew
+ _OBJC_IVAR_$_HMSetupAccessoryDescription._matterSystemCommissionerPairingUUID
+ _UIKitLibrary.45098
+ _UIKitLibraryCore.45094
+ _UIKitLibraryCore.frameworkLibrary.45107
+ __OBJC_$_CLASS_METHODS_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|OSEligibility|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
+ __OBJC_$_INSTANCE_METHODS_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|OSEligibility|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
+ __OBJC_$_PROP_LIST_HMApplicationData.13109
+ __OBJC_CLASS_PROTOCOLS_$_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|OSEligibility|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
+ ___102-[HMHome(HMModernMessaging) unregisterModernMessagingRequestHandlerWithMessageName:completionHandler:]_block_invoke.2284
+ ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2239
+ ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2240
+ ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2241
+ ___123-[HMHome(HMModernMessaging) registerModernMessagingRequestHandlerWithMessageName:options:requestHandler:completionHandler:]_block_invoke.2283
+ ___140-[HMHome(HMModernMessaging) sendModernMessagingRequestWithMessageName:destination:requestPayload:options:responseHandler:completionHandler:]_block_invoke.2286
+ ___22-[HMHome _mergeRooms:]_block_invoke.984
+ ___22-[HMHome _mergeRooms:]_block_invoke.985
+ ___22-[HMHome _mergeRooms:]_block_invoke_2.989
+ ___22-[HMHome _mergeRooms:]_block_invoke_3.990
+ ___22-[HMHome _mergeUsers:]_block_invoke.1030
+ ___22-[HMHome _mergeUsers:]_block_invoke.1031
+ ___22-[HMHome _mergeUsers:]_block_invoke_2.1035
+ ___22-[HMHome _mergeUsers:]_block_invoke_3.1036
+ ___22-[HMHome _mergeZones:]_block_invoke.992
+ ___22-[HMHome _mergeZones:]_block_invoke.993
+ ___22-[HMHome _mergeZones:]_block_invoke_2.997
+ ___22-[HMHome _mergeZones:]_block_invoke_3.998
+ ___25-[HMHome _mergeTriggers:]_block_invoke.1026
+ ___27-[HMHome _mergeActionSets:]_block_invoke.1017
+ ___27-[HMHome _mergeActionSets:]_block_invoke.1018
+ ___27-[HMHome _mergeActionSets:]_block_invoke_2.1022
+ ___27-[HMHome _mergeActionSets:]_block_invoke_3.1023
+ ___28-[HMHome _mergeAccessories:]_block_invoke.1000
+ ___28-[HMHome _mergeAccessories:]_block_invoke.1001
+ ___28-[HMHome _mergeAccessories:]_block_invoke.1004
+ ___28-[HMHome _mergeAccessories:]_block_invoke_2.1007
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.732
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.736
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.740
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.744
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.746
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.750
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.754
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.766
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.770
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.774
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.778
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.782
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.938
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.947
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.950
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.958
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.961
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.964
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.967
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.972
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.975
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.978
+ ___29-[HMHome mergeFromNewObject:]_block_invoke.981
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.733
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.737
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.741
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.745
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.747
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.751
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.755
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.767
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.771
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.775
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.779
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.783
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.939
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.948
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.951
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.959
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.962
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.965
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.968
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.971
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.974
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_2.977
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_3.953
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_4.954
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_5.955
+ ___29-[HMHome mergeFromNewObject:]_block_invoke_6.956
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1327
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke.1330
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1332
+ ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1333
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.1009
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke.1010
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.1014
+ ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.1015
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.1038
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke.1039
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.1043
+ ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.1044
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1292
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1294
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1296
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1299
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1302
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1304
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1313
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1315
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1293
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1295
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1300
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1303
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1314
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1318
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1319
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1321
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1322
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1286
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1324
+ ___34-[HMAccessory mergeFromNewObject:]_block_invoke_7.1325
+ ___34-[HMActionSet mergeFromNewObject:]_block_invoke.280
+ ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.1046
+ ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.1024
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.797
+ ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.799
+ ___40-[HMHome addUser:withCompletionHandler:]_block_invoke
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1360
+ ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1362
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.1050
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.1051
+ ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.1054
+ ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.1064
+ ___44-[HMHome _handleAccessoryAddedNotification:]_block_invoke.1141
+ ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1348
+ ___51-[HMActionSet mergeFromNewObjectForBuilderUpdates:]_block_invoke.282
+ ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.2060
+ ___54-[HMHome _notifyDelegateOfAccessControlUpdateForUser:]_block_invoke.1178
+ ___59-[HMHome(HMModernMessagingInternal) reRegisterHMMMHandlers]_block_invoke.2295
+ ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2246
+ ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2247
+ ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2248
+ ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.2138
+ ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke.2226
+ ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke_2.2227
+ ___65-[HMHome addUserWithoutConfirmation:privilege:completionHandler:]_block_invoke
+ ___66-[HMCameraClipManager fetchSignificantEventsWithUUIDs:completion:]_block_invoke.195
+ ___67-[HMHome _addEventTriggerFromResponse:withEventTrigger:completion:]_block_invoke.1134
+ ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.856
+ ___71-[HMHome setNotificationsEnabled:forCharacteristics:completionHandler:]_block_invoke
+ ___71-[HMHome(HomeActivityState) changeHomeActivityState:completionHandler:]_block_invoke.2245
+ ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke.2224
+ ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke_2.2225
+ ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.222
+ ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.223
+ ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.226
+ ___72-[HMHome _setNotificationsEnabled:forCharacteristics:completionHandler:]_block_invoke
+ ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke.2228
+ ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke_2.2229
+ ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke.2300
+ ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke_2.2301
+ ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1921
+ ___78-[HMHome(HomeActivityState) cancelHomeActivityStateHoldWithCompletionHandler:]_block_invoke.2249
+ ___78-[HMHome(HomeActivityState) cancelHomeActivityStateHoldWithCompletionHandler:]_block_invoke.2250
+ ___84-[HMHome setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:]_block_invoke
+ ___85-[HMHome _setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:]_block_invoke
+ ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1932
+ ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1923
+ ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.2236
+ ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.2193
+ ___93-[HMCameraClipManager fetchFaceCropDataRepresentationForSignificantEventWithUUID:completion:]_block_invoke.189
+ ___93-[HMCameraClipManager fetchFaceCropDataRepresentationForSignificantEventWithUUID:completion:]_block_invoke.190
+ ___Block_byref_object_copy_.16350
+ ___Block_byref_object_copy_.16684
+ ___Block_byref_object_copy_.24314
+ ___Block_byref_object_copy_.26660
+ ___Block_byref_object_copy_.31289
+ ___Block_byref_object_copy_.32926
+ ___Block_byref_object_copy_.35103
+ ___Block_byref_object_copy_.40423
+ ___Block_byref_object_copy_.43894
+ ___Block_byref_object_copy_.63712
+ ___Block_byref_object_copy_.66074
+ ___Block_byref_object_dispose_.16351
+ ___Block_byref_object_dispose_.16685
+ ___Block_byref_object_dispose_.24315
+ ___Block_byref_object_dispose_.26661
+ ___Block_byref_object_dispose_.31290
+ ___Block_byref_object_dispose_.32927
+ ___Block_byref_object_dispose_.35104
+ ___Block_byref_object_dispose_.40424
+ ___Block_byref_object_dispose_.43895
+ ___Block_byref_object_dispose_.63713
+ ___Block_byref_object_dispose_.66075
+ ___CoreAnalyticsLibraryCore_block_invoke.40537
+ ___CoreHAPLibraryCore_block_invoke.32826
+ ___IDSFoundationLibraryCore_block_invoke.44871
+ ___UIKitLibraryCore_block_invoke.45108
+ ___block_descriptor_58_e8_32s40s48bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8
+ ___block_literal_global.101.40544
+ ___block_literal_global.101.42738
+ ___block_literal_global.11289
+ ___block_literal_global.1139
+ ___block_literal_global.12.51282
+ ___block_literal_global.12003
+ ___block_literal_global.1223
+ ___block_literal_global.1225
+ ___block_literal_global.1228
+ ___block_literal_global.13041
+ ___block_literal_global.13162
+ ___block_literal_global.1344
+ ___block_literal_global.14143
+ ___block_literal_global.14284
+ ___block_literal_global.14359
+ ___block_literal_global.14606
+ ___block_literal_global.14980
+ ___block_literal_global.15208
+ ___block_literal_global.15796
+ ___block_literal_global.16147
+ ___block_literal_global.16436
+ ___block_literal_global.17.19927
+ ___block_literal_global.17066
+ ___block_literal_global.18274
+ ___block_literal_global.18810
+ ___block_literal_global.18991
+ ___block_literal_global.19.16132
+ ___block_literal_global.191
+ ___block_literal_global.19124
+ ___block_literal_global.19283
+ ___block_literal_global.1940
+ ___block_literal_global.19934
+ ___block_literal_global.2057
+ ___block_literal_global.2059
+ ___block_literal_global.20603
+ ___block_literal_global.21068
+ ___block_literal_global.2135
+ ___block_literal_global.21707
+ ___block_literal_global.22074
+ ___block_literal_global.23046
+ ___block_literal_global.23352
+ ___block_literal_global.23686
+ ___block_literal_global.24352
+ ___block_literal_global.24541
+ ___block_literal_global.246
+ ___block_literal_global.24739
+ ___block_literal_global.25267
+ ___block_literal_global.25511
+ ___block_literal_global.25886
+ ___block_literal_global.26024
+ ___block_literal_global.26271
+ ___block_literal_global.26518
+ ___block_literal_global.26685
+ ___block_literal_global.26778
+ ___block_literal_global.27508
+ ___block_literal_global.29425
+ ___block_literal_global.29584
+ ___block_literal_global.29862
+ ___block_literal_global.30.19916
+ ___block_literal_global.31137
+ ___block_literal_global.31407
+ ___block_literal_global.31746
+ ___block_literal_global.32005
+ ___block_literal_global.32291
+ ___block_literal_global.32371
+ ___block_literal_global.33.65411
+ ___block_literal_global.33069
+ ___block_literal_global.33565
+ ___block_literal_global.33837
+ ___block_literal_global.34889
+ ___block_literal_global.35126
+ ___block_literal_global.35428
+ ___block_literal_global.36752
+ ___block_literal_global.37725
+ ___block_literal_global.37959
+ ___block_literal_global.38188
+ ___block_literal_global.38584
+ ___block_literal_global.39334
+ ___block_literal_global.40531
+ ___block_literal_global.40781
+ ___block_literal_global.41120
+ ___block_literal_global.41786
+ ___block_literal_global.42748
+ ___block_literal_global.43012
+ ___block_literal_global.43281
+ ___block_literal_global.43566
+ ___block_literal_global.43786
+ ___block_literal_global.44932
+ ___block_literal_global.45026
+ ___block_literal_global.45733
+ ___block_literal_global.45925
+ ___block_literal_global.47108
+ ___block_literal_global.47550
+ ___block_literal_global.47876
+ ___block_literal_global.48642
+ ___block_literal_global.49299
+ ___block_literal_global.49657
+ ___block_literal_global.50931
+ ___block_literal_global.51294
+ ___block_literal_global.51578
+ ___block_literal_global.51774
+ ___block_literal_global.52004
+ ___block_literal_global.52721
+ ___block_literal_global.52841
+ ___block_literal_global.53596
+ ___block_literal_global.53830
+ ___block_literal_global.54285
+ ___block_literal_global.54546
+ ___block_literal_global.55628
+ ___block_literal_global.57929
+ ___block_literal_global.58.37954
+ ___block_literal_global.58793
+ ___block_literal_global.60083
+ ___block_literal_global.60815
+ ___block_literal_global.61370
+ ___block_literal_global.61681
+ ___block_literal_global.62198
+ ___block_literal_global.62375
+ ___block_literal_global.62765
+ ___block_literal_global.63013
+ ___block_literal_global.64814
+ ___block_literal_global.65150
+ ___block_literal_global.65417
+ ___block_literal_global.65775
+ ___block_literal_global.66013
+ ___block_literal_global.66369
+ ___block_literal_global.7.24552
+ ___block_literal_global.73.24712
+ ___block_literal_global.84.40725
+ ___block_literal_global.860
+ ___getAnalyticsSendEventLazySymbolLoc_block_invoke.40534
+ ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.45103
+ ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.45097
+ _audit_stringCoreAnalytics.40540
+ _audit_stringCoreHAP.32828
+ _audit_stringIDSFoundation.44873
+ _audit_stringUIKit.45110
+ _getAnalyticsSendEventLazySymbolLoc.ptr.40533
+ _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.45102
+ _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.45096
+ _logCategory._hmf_once_t0.14358
+ _logCategory._hmf_once_t0.23351
+ _logCategory._hmf_once_t0.24738
+ _logCategory._hmf_once_t0.32004
+ _logCategory._hmf_once_t0.32370
+ _logCategory._hmf_once_t0.43565
+ _logCategory._hmf_once_t0.45732
+ _logCategory._hmf_once_t0.45924
+ _logCategory._hmf_once_t0.63012
+ _logCategory._hmf_once_t1.19123
+ _logCategory._hmf_once_t1.21067
+ _logCategory._hmf_once_t1.40757
+ _logCategory._hmf_once_t1.47107
+ _logCategory._hmf_once_t1.51281
+ _logCategory._hmf_once_t1.52840
+ _logCategory._hmf_once_t1.57928
+ _logCategory._hmf_once_t11.13040
+ _logCategory._hmf_once_t13.42737
+ _logCategory._hmf_once_t14.62764
+ _logCategory._hmf_once_t16.31406
+ _logCategory._hmf_once_t16.37958
+ _logCategory._hmf_once_t16.64813
+ _logCategory._hmf_once_t2.24551
+ _logCategory._hmf_once_t2.26684
+ _logCategory._hmf_once_t2.29861
+ _logCategory._hmf_once_t2.33564
+ _logCategory._hmf_once_t20.25279
+ _logCategory._hmf_once_t20.26270
+ _logCategory._hmf_once_t21.62374
+ _logCategory._hmf_once_t24.41119
+ _logCategory._hmf_once_t24.41785
+ _logCategory._hmf_once_t25.26517
+ _logCategory._hmf_once_t25.65774
+ _logCategory._hmf_once_t27.61680
+ _logCategory._hmf_once_t3.43011
+ _logCategory._hmf_once_t3.53819
+ _logCategory._hmf_once_t3.65410
+ _logCategory._hmf_once_t31.24351
+ _logCategory._hmf_once_t31.54284
+ _logCategory._hmf_once_t31.66368
+ _logCategory._hmf_once_t32.53595
+ _logCategory._hmf_once_t34.20602
+ _logCategory._hmf_once_t365
+ _logCategory._hmf_once_t37.54572
+ _logCategory._hmf_once_t4.14605
+ _logCategory._hmf_once_t44.26540
+ _logCategory._hmf_once_t44.32290
+ _logCategory._hmf_once_t5.18809
+ _logCategory._hmf_once_t51.43280
+ _logCategory._hmf_once_t6.34888
+ _logCategory._hmf_once_t6.37724
+ _logCategory._hmf_once_t6.43785
+ _logCategory._hmf_once_t6.49298
+ _logCategory._hmf_once_t6.58792
+ _logCategory._hmf_once_t67
+ _logCategory._hmf_once_t7.52720
+ _logCategory._hmf_once_t8.38187
+ _logCategory._hmf_once_t8.48641
+ _logCategory._hmf_once_t8.51792
+ _logCategory._hmf_once_t9.29583
+ _logCategory._hmf_once_v1.14360
+ _logCategory._hmf_once_v1.23353
+ _logCategory._hmf_once_v1.24740
+ _logCategory._hmf_once_v1.32006
+ _logCategory._hmf_once_v1.32372
+ _logCategory._hmf_once_v1.43567
+ _logCategory._hmf_once_v1.45734
+ _logCategory._hmf_once_v1.45926
+ _logCategory._hmf_once_v1.63014
+ _logCategory._hmf_once_v10.29585
+ _logCategory._hmf_once_v12.13042
+ _logCategory._hmf_once_v14.42739
+ _logCategory._hmf_once_v15.62766
+ _logCategory._hmf_once_v17.31408
+ _logCategory._hmf_once_v17.37960
+ _logCategory._hmf_once_v17.64815
+ _logCategory._hmf_once_v2.19125
+ _logCategory._hmf_once_v2.21069
+ _logCategory._hmf_once_v2.40758
+ _logCategory._hmf_once_v2.47109
+ _logCategory._hmf_once_v2.51283
+ _logCategory._hmf_once_v2.52842
+ _logCategory._hmf_once_v2.57930
+ _logCategory._hmf_once_v21.25280
+ _logCategory._hmf_once_v21.26272
+ _logCategory._hmf_once_v22.62376
+ _logCategory._hmf_once_v25.41121
+ _logCategory._hmf_once_v25.41787
+ _logCategory._hmf_once_v26.26519
+ _logCategory._hmf_once_v26.65776
+ _logCategory._hmf_once_v28.61682
+ _logCategory._hmf_once_v3.24553
+ _logCategory._hmf_once_v3.26686
+ _logCategory._hmf_once_v3.29863
+ _logCategory._hmf_once_v3.33566
+ _logCategory._hmf_once_v32.24353
+ _logCategory._hmf_once_v32.54286
+ _logCategory._hmf_once_v32.66370
+ _logCategory._hmf_once_v33.53597
+ _logCategory._hmf_once_v35.20604
+ _logCategory._hmf_once_v366
+ _logCategory._hmf_once_v38.54573
+ _logCategory._hmf_once_v4.43013
+ _logCategory._hmf_once_v4.53820
+ _logCategory._hmf_once_v4.65412
+ _logCategory._hmf_once_v45.26541
+ _logCategory._hmf_once_v45.32292
+ _logCategory._hmf_once_v5.14607
+ _logCategory._hmf_once_v52.43282
+ _logCategory._hmf_once_v6.18811
+ _logCategory._hmf_once_v68
+ _logCategory._hmf_once_v7.34890
+ _logCategory._hmf_once_v7.37726
+ _logCategory._hmf_once_v7.43787
+ _logCategory._hmf_once_v7.49300
+ _logCategory._hmf_once_v7.58794
+ _logCategory._hmf_once_v8.52722
+ _logCategory._hmf_once_v9.38189
+ _logCategory._hmf_once_v9.48643
+ _logCategory._hmf_once_v9.51793
+ _objc_msgSend$_setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:
+ _objc_msgSend$_setNotificationsEnabled:forCharacteristics:completionHandler:
+ _objc_msgSend$matterSystemCommissionerPairingUUID
+ _objc_msgSend$reenableNotifications
+ _objc_msgSend$setAllNotificationsEnabled:completionHandler:
+ _objc_msgSend$setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:
+ _objc_msgSend$setMatterSystemCommissionerPairingIsNew:
+ _objc_msgSend$setMatterSystemCommissionerPairingUUID:
+ _objc_msgSend$setNotificationsEnabled:forCharacteristics:completionHandler:
+ _os_eligibility_get_domain_answer
+ _sharedInstance.onceToken.42747
+ _sharedManager.onceToken.61827
+ _supportedValueClasses.onceToken.51577
+ _supportedValueClasses.onceToken.60045
+ _supportedValueClasses.supportedValueClasses.51579
+ _supportedValueClasses.supportedValueClasses.60046
- -[HMCameraClipManager fetchFaceCropURLForSignificantEventWithUUID:completion:]
- -[HMCameraClipManager fetchHeroFrameDataRepresentationForClip:completion:]
- -[HMCameraClipManager fetchHeroFrameURLOfClipWithUUID:completion:]
- -[HMHome _enableNotification:forCharacteristics:completionHandler:]
- -[HMHome _enableNotifications:includeAppleMediaAccessoryNotifications:completionHandler:]
- -[HMHome _handleNotificationsEnabled:]
- -[HMHome reEnableNotifications]
- -[HMHome setNotificationsEnabled:]
- -[HMHome setNotificationsUpdatedTime:]
- -[HMHome(HMUser) addUser:withCompletionHandler:]
- -[HMHome(HMUser) addUserWithoutConfirmation:privilege:completionHandler:]
- -[HMHome(HMUser) inviteUsers:completionHandler:]
- -[HMHome(HMUser) removeUserWithoutConfirmation:completionHandler:]
- GCC_except_table10001
- GCC_except_table10003
- GCC_except_table10066
- GCC_except_table10098
- GCC_except_table10100
- GCC_except_table10104
- GCC_except_table10121
- GCC_except_table10123
- GCC_except_table10129
- GCC_except_table10133
- GCC_except_table10136
- GCC_except_table10143
- GCC_except_table10147
- GCC_except_table10153
- GCC_except_table10165
- GCC_except_table10168
- GCC_except_table10176
- GCC_except_table10179
- GCC_except_table10181
- GCC_except_table10183
- GCC_except_table10195
- GCC_except_table10205
- GCC_except_table10408
- GCC_except_table10421
- GCC_except_table10470
- GCC_except_table10475
- GCC_except_table10479
- GCC_except_table10487
- GCC_except_table10544
- GCC_except_table10547
- GCC_except_table10548
- GCC_except_table10895
- GCC_except_table10943
- GCC_except_table10956
- GCC_except_table11325
- GCC_except_table11327
- GCC_except_table11329
- GCC_except_table11330
- GCC_except_table11360
- GCC_except_table11362
- GCC_except_table11372
- GCC_except_table11373
- GCC_except_table11374
- GCC_except_table11482
- GCC_except_table11483
- GCC_except_table11509
- GCC_except_table11511
- GCC_except_table11515
- GCC_except_table11516
- GCC_except_table11564
- GCC_except_table11590
- GCC_except_table11603
- GCC_except_table11629
- GCC_except_table11633
- GCC_except_table11695
- GCC_except_table11696
- GCC_except_table11697
- GCC_except_table11698
- GCC_except_table11699
- GCC_except_table11700
- GCC_except_table11701
- GCC_except_table11702
- GCC_except_table11725
- GCC_except_table11752
- GCC_except_table11862
- GCC_except_table11863
- GCC_except_table11866
- GCC_except_table11931
- GCC_except_table11941
- GCC_except_table11954
- GCC_except_table11959
- GCC_except_table11960
- GCC_except_table11961
- GCC_except_table12166
- GCC_except_table12369
- GCC_except_table12374
- GCC_except_table12378
- GCC_except_table12384
- GCC_except_table12396
- GCC_except_table12397
- GCC_except_table12399
- GCC_except_table12481
- GCC_except_table12483
- GCC_except_table12503
- GCC_except_table12504
- GCC_except_table12505
- GCC_except_table12510
- GCC_except_table12524
- GCC_except_table12530
- GCC_except_table12533
- GCC_except_table12535
- GCC_except_table12621
- GCC_except_table12622
- GCC_except_table12639
- GCC_except_table12641
- GCC_except_table12643
- GCC_except_table12645
- GCC_except_table12778
- GCC_except_table12834
- GCC_except_table12835
- GCC_except_table12836
- GCC_except_table12837
- GCC_except_table12847
- GCC_except_table12848
- GCC_except_table12872
- GCC_except_table12873
- GCC_except_table12929
- GCC_except_table12951
- GCC_except_table12954
- GCC_except_table13051
- GCC_except_table13094
- GCC_except_table13294
- GCC_except_table13297
- GCC_except_table13357
- GCC_except_table13442
- GCC_except_table13452
- GCC_except_table13513
- GCC_except_table13516
- GCC_except_table13536
- GCC_except_table13538
- GCC_except_table13539
- GCC_except_table2757
- GCC_except_table2762
- GCC_except_table2788
- GCC_except_table2791
- GCC_except_table2804
- GCC_except_table2841
- GCC_except_table2857
- GCC_except_table2860
- GCC_except_table2885
- GCC_except_table2887
- GCC_except_table3052
- GCC_except_table3070
- GCC_except_table3071
- GCC_except_table3117
- GCC_except_table3119
- GCC_except_table3143
- GCC_except_table3145
- GCC_except_table3148
- GCC_except_table3173
- GCC_except_table3175
- GCC_except_table3183
- GCC_except_table3185
- GCC_except_table3192
- GCC_except_table3193
- GCC_except_table3194
- GCC_except_table3199
- GCC_except_table3259
- GCC_except_table3282
- GCC_except_table3285
- GCC_except_table3288
- GCC_except_table3291
- GCC_except_table3294
- GCC_except_table3297
- GCC_except_table3300
- GCC_except_table3365
- GCC_except_table3366
- GCC_except_table3412
- GCC_except_table3419
- GCC_except_table3420
- GCC_except_table3421
- GCC_except_table3426
- GCC_except_table3436
- GCC_except_table3458
- GCC_except_table3465
- GCC_except_table3472
- GCC_except_table3475
- GCC_except_table3516
- GCC_except_table3529
- GCC_except_table3537
- GCC_except_table3550
- GCC_except_table3552
- GCC_except_table3791
- GCC_except_table3802
- GCC_except_table3807
- GCC_except_table3816
- GCC_except_table3847
- GCC_except_table3849
- GCC_except_table3854
- GCC_except_table3857
- GCC_except_table3860
- GCC_except_table3940
- GCC_except_table3954
- GCC_except_table3957
- GCC_except_table3959
- GCC_except_table3962
- GCC_except_table3969
- GCC_except_table4022
- GCC_except_table4087
- GCC_except_table4102
- GCC_except_table4105
- GCC_except_table4198
- GCC_except_table4199
- GCC_except_table4201
- GCC_except_table4206
- GCC_except_table4213
- GCC_except_table4215
- GCC_except_table4223
- GCC_except_table4470
- GCC_except_table4473
- GCC_except_table4485
- GCC_except_table4559
- GCC_except_table4603
- GCC_except_table4695
- GCC_except_table4857
- GCC_except_table4869
- GCC_except_table4871
- GCC_except_table4895
- GCC_except_table4896
- GCC_except_table4897
- GCC_except_table4898
- GCC_except_table4953
- GCC_except_table4963
- GCC_except_table5092
- GCC_except_table5093
- GCC_except_table5169
- GCC_except_table5271
- GCC_except_table5273
- GCC_except_table5301
- GCC_except_table5303
- GCC_except_table5321
- GCC_except_table5367
- GCC_except_table5462
- GCC_except_table5482
- GCC_except_table5483
- GCC_except_table5484
- GCC_except_table5489
- GCC_except_table5492
- GCC_except_table5750
- GCC_except_table5756
- GCC_except_table5758
- GCC_except_table5768
- GCC_except_table5769
- GCC_except_table5963
- GCC_except_table6040
- GCC_except_table6160
- GCC_except_table6167
- GCC_except_table6172
- GCC_except_table6361
- GCC_except_table6414
- GCC_except_table6610
- GCC_except_table6612
- GCC_except_table6627
- GCC_except_table6647
- GCC_except_table6657
- GCC_except_table6660
- GCC_except_table6674
- GCC_except_table6679
- GCC_except_table6685
- GCC_except_table6690
- GCC_except_table6695
- GCC_except_table6700
- GCC_except_table6705
- GCC_except_table6709
- GCC_except_table6714
- GCC_except_table6772
- GCC_except_table6776
- GCC_except_table6784
- GCC_except_table6789
- GCC_except_table6803
- GCC_except_table6808
- GCC_except_table6815
- GCC_except_table6830
- GCC_except_table6833
- GCC_except_table6835
- GCC_except_table6838
- GCC_except_table6843
- GCC_except_table6850
- GCC_except_table6855
- GCC_except_table6859
- GCC_except_table6893
- GCC_except_table6950
- GCC_except_table6954
- GCC_except_table6956
- GCC_except_table7095
- GCC_except_table7102
- GCC_except_table7187
- GCC_except_table7218
- GCC_except_table7688
- GCC_except_table7951
- GCC_except_table7994
- GCC_except_table8054
- GCC_except_table8170
- GCC_except_table8173
- GCC_except_table8263
- GCC_except_table8282
- GCC_except_table8292
- GCC_except_table8428
- GCC_except_table8437
- GCC_except_table8450
- GCC_except_table8457
- GCC_except_table8496
- GCC_except_table8498
- GCC_except_table8526
- GCC_except_table8528
- GCC_except_table8530
- GCC_except_table8532
- GCC_except_table8539
- GCC_except_table8545
- GCC_except_table8549
- GCC_except_table8559
- GCC_except_table8565
- GCC_except_table8651
- GCC_except_table8653
- GCC_except_table8663
- GCC_except_table8665
- GCC_except_table8667
- GCC_except_table8669
- GCC_except_table8671
- GCC_except_table8677
- GCC_except_table8681
- GCC_except_table8694
- GCC_except_table8696
- GCC_except_table8698
- GCC_except_table8700
- GCC_except_table8719
- GCC_except_table8876
- GCC_except_table8878
- GCC_except_table8882
- GCC_except_table8884
- GCC_except_table8921
- GCC_except_table8924
- GCC_except_table8928
- GCC_except_table8931
- GCC_except_table8975
- GCC_except_table8984
- GCC_except_table8987
- GCC_except_table9006
- GCC_except_table9078
- GCC_except_table9117
- GCC_except_table9301
- GCC_except_table9307
- GCC_except_table9362
- GCC_except_table9383
- GCC_except_table9459
- GCC_except_table9461
- GCC_except_table9463
- GCC_except_table9465
- GCC_except_table9473
- GCC_except_table9520
- GCC_except_table9532
- GCC_except_table9534
- GCC_except_table9550
- GCC_except_table9578
- GCC_except_table9752
- GCC_except_table9754
- GCC_except_table9756
- GCC_except_table9800
- GCC_except_table9836
- GCC_except_table9869
- GCC_except_table9872
- GCC_except_table9875
- GCC_except_table9877
- GCC_except_table9938
- GCC_except_table9958
- GCC_except_table9999
- _CoreAnalyticsLibraryCore.frameworkLibrary.40542
- _CoreHAPLibraryCore.frameworkLibrary.32847
- _IDSFoundationLibraryCore.44862
- _IDSFoundationLibraryCore.frameworkLibrary.44865
- _OBJC_IVAR_$_HMHome._notificationsEnabled
- _OBJC_IVAR_$_HMHome._notificationsUpdatedTime
- _UIKitLibrary.45092
- _UIKitLibraryCore.45088
- _UIKitLibraryCore.frameworkLibrary.45101
- __OBJC_$_CLASS_METHODS_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
- __OBJC_$_INSTANCE_METHODS_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
- __OBJC_$_PROP_LIST_HMApplicationData.13115
- __OBJC_CLASS_PROTOCOLS_$_HMHomeManager(AccessorySettingsControllerFactory|AccessorySettingsControllerDataSource|HMMultiuserSettingsMessengerFactory|HMAccessoryInfoDataProvider|PairingIdentity|HMHomeManagerAdaptive|DiagnosticExtension|HMAccessorySettingsDataSourceDataSource|AccessorySettingsMessengerFactory|AccessorySettingsMetricsDispatcherFactory|Wallet|AccessorySettingsDataSourceFactory|CoreAnalyticsMetricEventDispatcherFactory|InstanceTracking)
- ___102-[HMHome(HMModernMessaging) unregisterModernMessagingRequestHandlerWithMessageName:completionHandler:]_block_invoke.2290
- ___121-[HMHomeManager _mergeCurrentHomesWithNewHomes:newPrimaryHome:newCurrentHome:newInvitations:newAppData:refreshRequested:]_block_invoke_2.796
- ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2245
- ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2246
- ___122-[HMHome(MediaGroupReadinessCheck) performMediaGroupReadinessCheckForAccessory:timeout:setupSessionIdentifier:completion:]_block_invoke.2247
- ___123-[HMHome(HMModernMessaging) registerModernMessagingRequestHandlerWithMessageName:options:requestHandler:completionHandler:]_block_invoke.2289
- ___140-[HMHome(HMModernMessaging) sendModernMessagingRequestWithMessageName:destination:requestPayload:options:responseHandler:completionHandler:]_block_invoke.2292
- ___22-[HMHome _mergeRooms:]_block_invoke.986
- ___22-[HMHome _mergeRooms:]_block_invoke.989
- ___22-[HMHome _mergeRooms:]_block_invoke_2.991
- ___22-[HMHome _mergeRooms:]_block_invoke_3.992
- ___22-[HMHome _mergeUsers:]_block_invoke.1032
- ___22-[HMHome _mergeUsers:]_block_invoke.1035
- ___22-[HMHome _mergeUsers:]_block_invoke_2.1037
- ___22-[HMHome _mergeUsers:]_block_invoke_3.1038
- ___22-[HMHome _mergeZones:]_block_invoke.994
- ___22-[HMHome _mergeZones:]_block_invoke.997
- ___22-[HMHome _mergeZones:]_block_invoke_2.999
- ___22-[HMHome _mergeZones:]_block_invoke_3.1000
- ___25-[HMHome _mergeTriggers:]_block_invoke.1030
- ___27-[HMHome _mergeActionSets:]_block_invoke.1019
- ___27-[HMHome _mergeActionSets:]_block_invoke.1022
- ___27-[HMHome _mergeActionSets:]_block_invoke_2.1024
- ___27-[HMHome _mergeActionSets:]_block_invoke_3.1025
- ___28-[HMHome _mergeAccessories:]_block_invoke.1002
- ___28-[HMHome _mergeAccessories:]_block_invoke.1005
- ___28-[HMHome _mergeAccessories:]_block_invoke.1008
- ___28-[HMHome _mergeAccessories:]_block_invoke_2.1009
- ___29-[HMHome mergeFromNewObject:]_block_invoke.733
- ___29-[HMHome mergeFromNewObject:]_block_invoke.737
- ___29-[HMHome mergeFromNewObject:]_block_invoke.741
- ___29-[HMHome mergeFromNewObject:]_block_invoke.745
- ___29-[HMHome mergeFromNewObject:]_block_invoke.747
- ___29-[HMHome mergeFromNewObject:]_block_invoke.751
- ___29-[HMHome mergeFromNewObject:]_block_invoke.755
- ___29-[HMHome mergeFromNewObject:]_block_invoke.767
- ___29-[HMHome mergeFromNewObject:]_block_invoke.771
- ___29-[HMHome mergeFromNewObject:]_block_invoke.775
- ___29-[HMHome mergeFromNewObject:]_block_invoke.779
- ___29-[HMHome mergeFromNewObject:]_block_invoke.783
- ___29-[HMHome mergeFromNewObject:]_block_invoke.940
- ___29-[HMHome mergeFromNewObject:]_block_invoke.949
- ___29-[HMHome mergeFromNewObject:]_block_invoke.952
- ___29-[HMHome mergeFromNewObject:]_block_invoke.960
- ___29-[HMHome mergeFromNewObject:]_block_invoke.963
- ___29-[HMHome mergeFromNewObject:]_block_invoke.966
- ___29-[HMHome mergeFromNewObject:]_block_invoke.971
- ___29-[HMHome mergeFromNewObject:]_block_invoke.974
- ___29-[HMHome mergeFromNewObject:]_block_invoke.977
- ___29-[HMHome mergeFromNewObject:]_block_invoke.982
- ___29-[HMHome mergeFromNewObject:]_block_invoke.983
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.734
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.738
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.742
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.746
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.748
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.752
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.756
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.768
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.772
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.776
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.780
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.784
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.941
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.950
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.953
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.961
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.964
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.967
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.970
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.973
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.976
- ___29-[HMHome mergeFromNewObject:]_block_invoke_2.979
- ___29-[HMHome mergeFromNewObject:]_block_invoke_3.955
- ___29-[HMHome mergeFromNewObject:]_block_invoke_4.956
- ___29-[HMHome mergeFromNewObject:]_block_invoke_5.957
- ___29-[HMHome mergeFromNewObject:]_block_invoke_6.958
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1329
- ___30-[HMAccessory _mergeProfiles:]_block_invoke.1331
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_2.1333
- ___30-[HMAccessory _mergeProfiles:]_block_invoke_3.1334
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.1011
- ___30-[HMHome _mergeServiceGroups:]_block_invoke.1014
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_2.1016
- ___30-[HMHome _mergeServiceGroups:]_block_invoke_3.1017
- ___31-[HMHome reEnableNotifications]_block_invoke
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.1040
- ___32-[HMHome _mergeResidentDevices:]_block_invoke.1043
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_2.1045
- ___32-[HMHome _mergeResidentDevices:]_block_invoke_3.1046
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1293
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1295
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1298
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1300
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1303
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1312
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1314
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke.1317
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1294
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1296
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1301
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1304
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1315
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_2.1319
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_3.1320
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_4.1322
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_5.1323
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1287
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_6.1325
- ___34-[HMAccessory mergeFromNewObject:]_block_invoke_7.1326
- ___34-[HMActionSet mergeFromNewObject:]_block_invoke.282
- ___36-[HMHome _mergeOutgoingInvitations:]_block_invoke.1050
- ___38-[HMHome _handleNotificationsEnabled:]_block_invoke
- ___39-[HMHome _mergeTriggerOwnedActionSets:]_block_invoke.1026
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.798
- ___39-[HMHomeManager _mergeHomeInvitations:]_block_invoke.800
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1361
- ___41-[HMAccessory _updateHasSymptomsHandler:]_block_invoke.1363
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.1054
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke.1057
- ___42-[HMHome _mergeAccessoryProtectionGroups:]_block_invoke_2.1056
- ___43-[HMHome fetchPresenceForUsers:completion:]_block_invoke.1068
- ___44-[HMHome _handleAccessoryAddedNotification:]_block_invoke.1145
- ___48-[HMAccessory _deleteSiriHistoryWithCompletion:]_block_invoke.1350
- ___48-[HMHome enableNotifications:completionHandler:]_block_invoke
- ___48-[HMHome(HMUser) addUser:withCompletionHandler:]_block_invoke
- ___51-[HMActionSet mergeFromNewObjectForBuilderUpdates:]_block_invoke.283
- ___52-[HMHome(HMUser) _manageUsersWithCompletionHandler:]_block_invoke.2061
- ___54-[HMHome _notifyDelegateOfAccessControlUpdateForUser:]_block_invoke.1182
- ___59-[HMHome(HMModernMessagingInternal) reRegisterHMMMHandlers]_block_invoke.2301
- ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2252
- ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2253
- ___59-[HMHome(HomeActivityState) fetchCurrentHomeActivityState:]_block_invoke.2254
- ___64-[HMHome(HMMediaProfile) updateMediaPassword:completionHandler:]_block_invoke.2144
- ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke.2232
- ___64-[HMHome(HomeNetworkInfo) fetchWiFiInfosWithTimeout:completion:]_block_invoke_2.2233
- ___66-[HMCameraClipManager fetchHeroFrameURLOfClipWithUUID:completion:]_block_invoke
- ___66-[HMCameraClipManager fetchHeroFrameURLOfClipWithUUID:completion:]_block_invoke.189
- ___66-[HMCameraClipManager fetchHeroFrameURLOfClipWithUUID:completion:]_block_invoke.191
- ___66-[HMCameraClipManager fetchSignificantEventsWithUUIDs:completion:]_block_invoke.206
- ___66-[HMHome enableNotification:forCharacteristics:completionHandler:]_block_invoke
- ___67-[HMHome _addEventTriggerFromResponse:withEventTrigger:completion:]_block_invoke.1138
- ___67-[HMHome _enableNotification:forCharacteristics:completionHandler:]_block_invoke
- ___69-[HMHomeManager addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.857
- ___71-[HMHome(HomeActivityState) changeHomeActivityState:completionHandler:]_block_invoke.2251
- ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke.2230
- ___71-[HMHome(HomeNetworkInfo) getPrimaryResidentNetworkInfoWithCompletion:]_block_invoke_2.2231
- ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.233
- ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.234
- ___72-[HMCameraClipManager fetchVideoSegmentsAssetContextForClip:completion:]_block_invoke.237
- ___73-[HMHome(HMUser) addUserWithoutConfirmation:privilege:completionHandler:]_block_invoke
- ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke.2234
- ___74-[HMHome(HomeNetworkInfo) fetchNetworkInfosFromTarget:timeout:completion:]_block_invoke_2.2235
- ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke.2306
- ___74-[HMHome(Trigger) fetchTriggerNameForTriggerIdentifier:completionHandler:]_block_invoke_2.2307
- ___75-[HMHome(HMAccessory) addAndSetupAccessoriesWithPayload:completionHandler:]_block_invoke.1922
- ___78-[HMCameraClipManager fetchFaceCropURLForSignificantEventWithUUID:completion:]_block_invoke
- ___78-[HMCameraClipManager fetchFaceCropURLForSignificantEventWithUUID:completion:]_block_invoke.200
- ___78-[HMCameraClipManager fetchFaceCropURLForSignificantEventWithUUID:completion:]_block_invoke.201
- ___78-[HMHome(HomeActivityState) cancelHomeActivityStateHoldWithCompletionHandler:]_block_invoke.2255
- ___78-[HMHome(HomeActivityState) cancelHomeActivityStateHoldWithCompletionHandler:]_block_invoke.2256
- ___88-[HMHome enableNotifications:includeAppleMediaAccessoryNotifications:completionHandler:]_block_invoke
- ___88-[HMHome(HMAccessory) addAccessoryWithAccessorySetupPayload:progress:completionHandler:]_block_invoke.1933
- ___88-[HMHome(HMAccessory) addAndSetUpNewAccessoriesWithSuggestedRoomName:completionHandler:]_block_invoke.1924
- ___88-[HMHome(HomeLocationFeedback) retrieveHomeKitLocationForFeedbackWithCompletionHandler:]_block_invoke.2242
- ___89-[HMHome _enableNotifications:includeAppleMediaAccessoryNotifications:completionHandler:]_block_invoke
- ___89-[HMHome(NetworkRouter) updateAccessoryNetworkProtectionGroup:protectionMode:completion:]_block_invoke.2199
- ___93-[HMCameraClipManager fetchFaceCropDataRepresentationForSignificantEventWithUUID:completion:]_block_invoke.195
- ___93-[HMCameraClipManager fetchFaceCropDataRepresentationForSignificantEventWithUUID:completion:]_block_invoke.196
- ___Block_byref_object_copy_.16364
- ___Block_byref_object_copy_.16698
- ___Block_byref_object_copy_.24325
- ___Block_byref_object_copy_.26671
- ___Block_byref_object_copy_.31305
- ___Block_byref_object_copy_.32939
- ___Block_byref_object_copy_.35117
- ___Block_byref_object_copy_.40429
- ___Block_byref_object_copy_.43899
- ___Block_byref_object_copy_.63721
- ___Block_byref_object_copy_.66089
- ___Block_byref_object_dispose_.16365
- ___Block_byref_object_dispose_.16699
- ___Block_byref_object_dispose_.24326
- ___Block_byref_object_dispose_.26672
- ___Block_byref_object_dispose_.31306
- ___Block_byref_object_dispose_.32940
- ___Block_byref_object_dispose_.35118
- ___Block_byref_object_dispose_.40430
- ___Block_byref_object_dispose_.43900
- ___Block_byref_object_dispose_.63722
- ___Block_byref_object_dispose_.66090
- ___CoreAnalyticsLibraryCore_block_invoke.40543
- ___CoreHAPLibraryCore_block_invoke.32848
- ___IDSFoundationLibraryCore_block_invoke.44866
- ___UIKitLibraryCore_block_invoke.45102
- ___block_literal_global.101.40550
- ___block_literal_global.101.42744
- ___block_literal_global.11295
- ___block_literal_global.1143
- ___block_literal_global.12.51283
- ___block_literal_global.12009
- ___block_literal_global.1227
- ___block_literal_global.1229
- ___block_literal_global.1232
- ___block_literal_global.13047
- ___block_literal_global.13168
- ___block_literal_global.1345
- ___block_literal_global.14149
- ___block_literal_global.14290
- ___block_literal_global.14365
- ___block_literal_global.14612
- ___block_literal_global.14986
- ___block_literal_global.15214
- ___block_literal_global.15802
- ___block_literal_global.16155
- ___block_literal_global.16450
- ___block_literal_global.17.19938
- ___block_literal_global.17079
- ___block_literal_global.18284
- ___block_literal_global.18820
- ___block_literal_global.19.16140
- ___block_literal_global.19001
- ___block_literal_global.19134
- ___block_literal_global.192
- ___block_literal_global.19293
- ___block_literal_global.1941
- ___block_literal_global.19945
- ___block_literal_global.2058
- ___block_literal_global.2060
- ___block_literal_global.20615
- ___block_literal_global.21079
- ___block_literal_global.2141
- ___block_literal_global.21718
- ___block_literal_global.22085
- ___block_literal_global.23057
- ___block_literal_global.23363
- ___block_literal_global.23697
- ___block_literal_global.24363
- ___block_literal_global.24552
- ___block_literal_global.24750
- ___block_literal_global.25278
- ___block_literal_global.25522
- ___block_literal_global.257
- ___block_literal_global.25897
- ___block_literal_global.26035
- ___block_literal_global.26282
- ___block_literal_global.26529
- ___block_literal_global.26696
- ___block_literal_global.26789
- ___block_literal_global.27519
- ___block_literal_global.29436
- ___block_literal_global.29596
- ___block_literal_global.29877
- ___block_literal_global.30.19927
- ___block_literal_global.31157
- ___block_literal_global.31425
- ___block_literal_global.31764
- ___block_literal_global.32023
- ___block_literal_global.32308
- ___block_literal_global.32388
- ___block_literal_global.33.65426
- ___block_literal_global.33083
- ___block_literal_global.33581
- ___block_literal_global.33851
- ___block_literal_global.34903
- ___block_literal_global.35140
- ___block_literal_global.35442
- ___block_literal_global.36756
- ___block_literal_global.37732
- ___block_literal_global.37966
- ___block_literal_global.38194
- ___block_literal_global.38590
- ___block_literal_global.39340
- ___block_literal_global.40537
- ___block_literal_global.40787
- ___block_literal_global.41126
- ___block_literal_global.41792
- ___block_literal_global.42754
- ___block_literal_global.43018
- ___block_literal_global.43287
- ___block_literal_global.43571
- ___block_literal_global.43791
- ___block_literal_global.44927
- ___block_literal_global.45020
- ___block_literal_global.45727
- ___block_literal_global.45919
- ___block_literal_global.47102
- ___block_literal_global.47553
- ___block_literal_global.47877
- ___block_literal_global.48643
- ___block_literal_global.49300
- ___block_literal_global.49658
- ___block_literal_global.50932
- ___block_literal_global.51295
- ___block_literal_global.51579
- ___block_literal_global.51775
- ___block_literal_global.52005
- ___block_literal_global.52722
- ___block_literal_global.52842
- ___block_literal_global.53597
- ___block_literal_global.53831
- ___block_literal_global.54286
- ___block_literal_global.54547
- ___block_literal_global.55630
- ___block_literal_global.57943
- ___block_literal_global.58.37961
- ___block_literal_global.58807
- ___block_literal_global.60096
- ___block_literal_global.60824
- ___block_literal_global.61377
- ___block_literal_global.61688
- ___block_literal_global.62205
- ___block_literal_global.62382
- ___block_literal_global.62774
- ___block_literal_global.63022
- ___block_literal_global.64829
- ___block_literal_global.65165
- ___block_literal_global.65432
- ___block_literal_global.65790
- ___block_literal_global.66028
- ___block_literal_global.66384
- ___block_literal_global.7.24563
- ___block_literal_global.73.24723
- ___block_literal_global.84.40731
- ___block_literal_global.861
- ___getAnalyticsSendEventLazySymbolLoc_block_invoke.40540
- ___getNSCharacterEncodingDocumentAttributeSymbolLoc_block_invoke.45097
- ___getNSDocumentTypeDocumentAttributeSymbolLoc_block_invoke.45091
- _audit_stringCoreAnalytics.40546
- _audit_stringCoreHAP.32850
- _audit_stringIDSFoundation.44868
- _audit_stringUIKit.45104
- _getAnalyticsSendEventLazySymbolLoc.ptr.40539
- _getNSCharacterEncodingDocumentAttributeSymbolLoc.ptr.45096
- _getNSDocumentTypeDocumentAttributeSymbolLoc.ptr.45090
- _kEnableHomeNotificationsNotificationKey
- _kEnableHomeNotificationsRequestKey
- _logCategory._hmf_once_t0.14364
- _logCategory._hmf_once_t0.23362
- _logCategory._hmf_once_t0.24749
- _logCategory._hmf_once_t0.32022
- _logCategory._hmf_once_t0.32387
- _logCategory._hmf_once_t0.43570
- _logCategory._hmf_once_t0.45726
- _logCategory._hmf_once_t0.45918
- _logCategory._hmf_once_t0.63021
- _logCategory._hmf_once_t1.19133
- _logCategory._hmf_once_t1.21078
- _logCategory._hmf_once_t1.40763
- _logCategory._hmf_once_t1.47101
- _logCategory._hmf_once_t1.51282
- _logCategory._hmf_once_t1.52841
- _logCategory._hmf_once_t1.57942
- _logCategory._hmf_once_t11.13046
- _logCategory._hmf_once_t13.42743
- _logCategory._hmf_once_t14.62773
- _logCategory._hmf_once_t16.31424
- _logCategory._hmf_once_t16.37965
- _logCategory._hmf_once_t16.64828
- _logCategory._hmf_once_t2.24562
- _logCategory._hmf_once_t2.26695
- _logCategory._hmf_once_t2.29876
- _logCategory._hmf_once_t2.33580
- _logCategory._hmf_once_t20.25290
- _logCategory._hmf_once_t20.26281
- _logCategory._hmf_once_t21.62381
- _logCategory._hmf_once_t24.41125
- _logCategory._hmf_once_t24.41791
- _logCategory._hmf_once_t25.26528
- _logCategory._hmf_once_t25.65789
- _logCategory._hmf_once_t27.61687
- _logCategory._hmf_once_t3.43017
- _logCategory._hmf_once_t3.53820
- _logCategory._hmf_once_t3.65425
- _logCategory._hmf_once_t31.24362
- _logCategory._hmf_once_t31.54285
- _logCategory._hmf_once_t31.66383
- _logCategory._hmf_once_t32.53596
- _logCategory._hmf_once_t34.20614
- _logCategory._hmf_once_t37.54573
- _logCategory._hmf_once_t371
- _logCategory._hmf_once_t4.14611
- _logCategory._hmf_once_t44.26551
- _logCategory._hmf_once_t44.32307
- _logCategory._hmf_once_t5.18819
- _logCategory._hmf_once_t51.43286
- _logCategory._hmf_once_t6.34902
- _logCategory._hmf_once_t6.37731
- _logCategory._hmf_once_t6.43790
- _logCategory._hmf_once_t6.49299
- _logCategory._hmf_once_t6.58806
- _logCategory._hmf_once_t7.52721
- _logCategory._hmf_once_t73
- _logCategory._hmf_once_t8.38193
- _logCategory._hmf_once_t8.48642
- _logCategory._hmf_once_t8.51793
- _logCategory._hmf_once_t9.29595
- _logCategory._hmf_once_v1.14366
- _logCategory._hmf_once_v1.23364
- _logCategory._hmf_once_v1.24751
- _logCategory._hmf_once_v1.32024
- _logCategory._hmf_once_v1.32389
- _logCategory._hmf_once_v1.43572
- _logCategory._hmf_once_v1.45728
- _logCategory._hmf_once_v1.45920
- _logCategory._hmf_once_v1.63023
- _logCategory._hmf_once_v10.29597
- _logCategory._hmf_once_v12.13048
- _logCategory._hmf_once_v14.42745
- _logCategory._hmf_once_v15.62775
- _logCategory._hmf_once_v17.31426
- _logCategory._hmf_once_v17.37967
- _logCategory._hmf_once_v17.64830
- _logCategory._hmf_once_v2.19135
- _logCategory._hmf_once_v2.21080
- _logCategory._hmf_once_v2.40764
- _logCategory._hmf_once_v2.47103
- _logCategory._hmf_once_v2.51284
- _logCategory._hmf_once_v2.52843
- _logCategory._hmf_once_v2.57944
- _logCategory._hmf_once_v21.25291
- _logCategory._hmf_once_v21.26283
- _logCategory._hmf_once_v22.62383
- _logCategory._hmf_once_v25.41127
- _logCategory._hmf_once_v25.41793
- _logCategory._hmf_once_v26.26530
- _logCategory._hmf_once_v26.65791
- _logCategory._hmf_once_v28.61689
- _logCategory._hmf_once_v3.24564
- _logCategory._hmf_once_v3.26697
- _logCategory._hmf_once_v3.29878
- _logCategory._hmf_once_v3.33582
- _logCategory._hmf_once_v32.24364
- _logCategory._hmf_once_v32.54287
- _logCategory._hmf_once_v32.66385
- _logCategory._hmf_once_v33.53598
- _logCategory._hmf_once_v35.20616
- _logCategory._hmf_once_v372
- _logCategory._hmf_once_v38.54574
- _logCategory._hmf_once_v4.43019
- _logCategory._hmf_once_v4.53821
- _logCategory._hmf_once_v4.65427
- _logCategory._hmf_once_v45.26552
- _logCategory._hmf_once_v45.32309
- _logCategory._hmf_once_v5.14613
- _logCategory._hmf_once_v52.43288
- _logCategory._hmf_once_v6.18821
- _logCategory._hmf_once_v7.34904
- _logCategory._hmf_once_v7.37733
- _logCategory._hmf_once_v7.43792
- _logCategory._hmf_once_v7.49301
- _logCategory._hmf_once_v7.58808
- _logCategory._hmf_once_v74
- _logCategory._hmf_once_v8.52723
- _logCategory._hmf_once_v9.38195
- _logCategory._hmf_once_v9.48644
- _logCategory._hmf_once_v9.51794
- _objc_msgSend$_enableNotification:forCharacteristics:completionHandler:
- _objc_msgSend$_enableNotifications:includeAppleMediaAccessoryNotifications:completionHandler:
- _objc_msgSend$areNotificationsEnabled
- _objc_msgSend$fetchHeroFrameDataRepresentationForClipWithUUID:completion:
- _objc_msgSend$home:didEnableNotifications:
- _objc_msgSend$notificationsUpdatedTime
- _objc_msgSend$reEnableNotifications
- _objc_msgSend$setNotificationsEnabled:
- _objc_msgSend$setNotificationsUpdatedTime:
- _sharedInstance.onceToken.42753
- _sharedManager.onceToken.61834
- _supportedValueClasses.onceToken.51578
- _supportedValueClasses.onceToken.60058
- _supportedValueClasses.supportedValueClasses.51580
- _supportedValueClasses.supportedValueClasses.60059
CStrings:
+ "%{public}@Failed to set notifications enabled to %{bool}d, includeAppleMediaAccessories: %{bool}d"
+ "%{public}@Setting notifications enabled to %{bool}d, includeAppleMediaAccessories: %{bool}d"
+ "%{public}@Successfully set notifications enabled to %{bool}d, includeAppleMediaAccessories: %{bool}d"
+ "-[HMHome _setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:]"
+ "-[HMHome _setNotificationsEnabled:forCharacteristics:completionHandler:]"
+ "-[HMHome addUser:withCompletionHandler:]"
+ "-[HMHome addUserWithoutConfirmation:privilege:completionHandler:]"
+ "-[HMHome setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:]"
+ "-[HMHome setNotificationsEnabled:forCharacteristics:completionHandler:]"
+ "HMHomeAccessorySystemCommissionerUUIDKey"
+ "OSEligibility"
+ "T@\"NSUUID\",C,N,V_matterSystemCommissionerPairingUUID"
+ "TB,N,V_matterSystemCommissionerPairingIsNew"
+ "TB,R,GareNotificationsEnabled"
+ "_matterSystemCommissionerPairingIsNew"
+ "_matterSystemCommissionerPairingUUID"
+ "_setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:"
+ "_setNotificationsEnabled:forCharacteristics:completionHandler:"
+ "matterSystemCommissionerPairingIsNew"
+ "matterSystemCommissionerPairingUUID"
+ "reenableNotifications"
+ "setAllNotificationsEnabled:completionHandler:"
+ "setAllNotificationsEnabled:includeAppleMediaAccessories:completionHandler:"
+ "setMatterSystemCommissionerPairingIsNew:"
+ "setMatterSystemCommissionerPairingUUID:"
+ "setNotificationsEnabled:forCharacteristics:completionHandler:"
+ "shouldDisableWiFiPickerBasedOnOSEligibility"
+ "\xa1\xf0\xf0q"
+ "\xf0A"
- "%{public}@Setting notifications enabled to %{bool}d, includeAppleMediaAccessoryNotifications: %{bool}d"
- "%{public}@[%{public}@] Failed to fetch face crop URL for significant event with UUID %@: %@"
- "%{public}@[%{public}@] Failed to fetch the hero frame of clip %@ due to error - %@"
- "%{public}@[%{public}@] Fetching face crop url for significant event with UUID %@"
- "%{public}@[%{public}@] Fetching hero frame url of clip with UUID %@"
- "%{public}@[%{public}@] Successfully fetched face crop URL for significant event with UUID %@: %@"
- "%{public}@[%{public}@] Successfully fetched hero frame URL for clip with UUID %@ : %@]"
- "-[HMHome _enableNotification:forCharacteristics:completionHandler:]"
- "-[HMHome _enableNotifications:includeAppleMediaAccessoryNotifications:completionHandler:]"
- "-[HMHome enableNotification:forCharacteristics:completionHandler:]"
- "-[HMHome enableNotifications:completionHandler:]"
- "-[HMHome enableNotifications:includeAppleMediaAccessoryNotifications:completionHandler:]"
- "-[HMHome reEnableNotifications]"
- "-[HMHome(HMUser) addUser:withCompletionHandler:]"
- "-[HMHome(HMUser) addUserWithoutConfirmation:privilege:completionHandler:]"
- "Fetch face crop URL for significant event"
- "Fetch hero frame URL of clip"
- "HM.enabledNotifications"
- "T@\"NSDate\",C,N,V_notificationsUpdatedTime"
- "TB,N,GareNotificationsEnabled,V_notificationsEnabled"
- "_enableNotification:forCharacteristics:completionHandler:"
- "_enableNotifications:includeAppleMediaAccessoryNotifications:completionHandler:"
- "_handleNotificationsEnabled:"
- "_notificationsEnabled"
- "_notificationsUpdatedTime"
- "fetchFaceCropURLForSignificantEventWithUUID:completion:"
- "fetchHeroFrameDataRepresentationForClip:completion:"
- "fetchHeroFrameURLOfClipWithUUID:completion:"
- "home:didEnableNotifications:"
- "reEnableNotifications"
- "setNotificationsEnabled:"
- "setNotificationsUpdatedTime:"
- "\xa1\xf0\xf0\x81"
- "\xf01"

```
