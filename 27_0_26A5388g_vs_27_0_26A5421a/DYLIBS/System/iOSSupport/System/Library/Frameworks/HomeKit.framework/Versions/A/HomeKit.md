## HomeKit

> `/System/iOSSupport/System/Library/Frameworks/HomeKit.framework/Versions/A/HomeKit`

```diff

-1490.2.0.0.0
-  __TEXT.__text: 0x3bed48
-  __TEXT.__objc_methlist: 0x2824c
-  __TEXT.__const: 0x66e8
+1493.1.5.4.1
+  __TEXT.__text: 0x3c1d2c
+  __TEXT.__objc_methlist: 0x28424
+  __TEXT.__const: 0x6818
   __TEXT.__dlopen_cstrs: 0x3b7
-  __TEXT.__swift5_typeref: 0x1fd4
-  __TEXT.__cstring: 0x2e915
-  __TEXT.__constg_swiftt: 0x1c60
-  __TEXT.__swift5_reflstr: 0x1154
-  __TEXT.__swift5_fieldmd: 0x143c
+  __TEXT.__swift5_typeref: 0x1fe8
+  __TEXT.__cstring: 0x2ecd9
+  __TEXT.__constg_swiftt: 0x1c98
+  __TEXT.__swift5_reflstr: 0x1195
+  __TEXT.__swift5_fieldmd: 0x1474
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_assocty: 0x350
+  __TEXT.__swift5_assocty: 0x368
   __TEXT.__swift5_capture: 0x9a4
   __TEXT.__swift5_protos: 0x38
-  __TEXT.__swift5_proto: 0x4c0
-  __TEXT.__swift5_types: 0x1bc
+  __TEXT.__swift5_proto: 0x4d0
+  __TEXT.__swift5_types: 0x1c4
   __TEXT.__swift_as_entry: 0x1e8
   __TEXT.__swift_as_ret: 0x22c
   __TEXT.__swift_as_cont: 0x434
-  __TEXT.__oslogstring: 0x55742
+  __TEXT.__oslogstring: 0x55c20
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__gcc_except_tab: 0x6694
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0xc588
+  __TEXT.__unwind_info: 0xc5d8
   __TEXT.__eh_frame: 0x7a10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8a10
+  __DATA_CONST.__const: 0x8a88
   __DATA_CONST.__objc_classlist: 0x1350
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe0d0
+  __DATA_CONST.__objc_selrefs: 0xe1c8
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0xfa8
   __DATA_CONST.__objc_arraydata: 0x13f8
-  __DATA_CONST.__got: 0x1e20
-  __AUTH_CONST.__const: 0x62c8
-  __AUTH_CONST.__cfstring: 0x2afe0
-  __AUTH_CONST.__objc_const: 0x48330
+  __DATA_CONST.__got: 0x1e28
+  __AUTH_CONST.__const: 0x63e8
+  __AUTH_CONST.__cfstring: 0x2b420
+  __AUTH_CONST.__objc_const: 0x48698
   __AUTH_CONST.__objc_intobj: 0x9c0
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x5e8
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x19d0
+  __AUTH_CONST.__auth_got: 0x1a00
   __AUTH.__objc_data: 0x8ef0
-  __AUTH.__data: 0x17b8
-  __DATA.__objc_ivar: 0x2788
-  __DATA.__data: 0x51d0
-  __DATA.__bss: 0x9470
+  __AUTH.__data: 0x17a8
+  __DATA.__objc_ivar: 0x27c4
+  __DATA.__data: 0x51f0
+  __DATA.__bss: 0x9670
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x36f0
   __DATA_DIRTY.__data: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17367
-  Symbols:   32457
-  CStrings:  12155
+  Functions: 17421
+  Symbols:   32549
+  CStrings:  12209
 
Symbols:
+ -[HMAccessory isCommissionedOverNFCWithoutPower]
+ -[HMAccessory networkCommissioningState]
+ -[HMAccessory productGroup]
+ -[HMAccessory productNumber]
+ -[HMAccessory setIsCommissionedOverNFCWithoutPower:]
+ -[HMAccessory setNetworkCommissioningState:]
+ -[HMAccessory setProductGroup:]
+ -[HMAccessory setProductNumber:]
+ -[HMAccessory userConfigurationReady]
+ -[HMAccessorySetupManager notifyProxControlLaunchRequested]
+ -[HMCHIPAccessorySetupPayload setSupportsNFCPairing:]
+ -[HMCHIPAccessorySetupPayload supportsNFCPairing]
+ -[HMHomeManager _pingDeviceWithUUID:qualityOfService:monitor:secure:restrictToLocalNetwork:completionHandler:]
+ -[HMProtoAccessoryCapabilities hasSupportsc7ab8e645f37]
+ -[HMProtoAccessoryCapabilities setHasSupportsc7ab8e645f37:]
+ -[HMProtoAccessoryCapabilities setSupportsc7ab8e645f37:]
+ -[HMProtoAccessoryCapabilities supportsc7ab8e645f37]
+ -[HMSetupAccessoryDescription setUserPermissionPromptAcceptButton:]
+ -[HMSetupAccessoryDescription setUserPermissionPromptCancelButton:]
+ -[HMSetupAccessoryDescription setUserPermissionPromptMessage:]
+ -[HMSetupAccessoryDescription setUserPermissionPromptTitle:]
+ -[HMSetupAccessoryDescription userPermissionPromptAcceptButton]
+ -[HMSetupAccessoryDescription userPermissionPromptCancelButton]
+ -[HMSetupAccessoryDescription userPermissionPromptMessage]
+ -[HMSetupAccessoryDescription userPermissionPromptTitle]
+ -[HMSetupAccessoryPayload deferredMatterOnboardingURL]
+ -[HMSetupAccessoryPayload deviceIdentifier]
+ -[HMSetupAccessoryPayload initWithVersion1LegacyPayloadData:value:length:payloadBytes:reserved:setupPayloadURL:outError:]
+ -[HMSetupAccessoryPayload initWithVersion1PayloadData:value:length:payloadBytes:setupPayloadURL:outError:]
+ -[HMSetupAccessoryPayload isThreadAccessory]
+ -[HMSetupAccessoryPayload productGroup]
+ -[HMSetupAccessoryPayload setDeferredMatterOnboardingURL:]
+ -[HMSetupAccessoryPayload setDeviceIdentifier:]
+ -[HMSetupAccessoryPayload setProductGroup:]
+ -[HMSetupAccessoryPayload setSupportsNFCPairing:]
+ -[HMSetupAccessoryPayload setThreadAccessory:]
+ -[HMSetupAccessoryPayload supportsNFCPairing]
+ GCC_except_table10128
+ GCC_except_table10129
+ GCC_except_table10130
+ GCC_except_table10134
+ GCC_except_table10189
+ GCC_except_table10210
+ GCC_except_table10290
+ GCC_except_table10292
+ GCC_except_table10294
+ GCC_except_table10296
+ GCC_except_table10304
+ GCC_except_table10351
+ GCC_except_table10363
+ GCC_except_table10365
+ GCC_except_table10555
+ GCC_except_table10556
+ GCC_except_table10591
+ GCC_except_table10624
+ GCC_except_table10627
+ GCC_except_table10630
+ GCC_except_table10632
+ GCC_except_table10711
+ GCC_except_table10731
+ GCC_except_table10732
+ GCC_except_table10733
+ GCC_except_table10772
+ GCC_except_table10774
+ GCC_except_table10776
+ GCC_except_table10841
+ GCC_except_table10875
+ GCC_except_table10879
+ GCC_except_table10896
+ GCC_except_table10898
+ GCC_except_table10904
+ GCC_except_table10908
+ GCC_except_table10911
+ GCC_except_table10918
+ GCC_except_table10922
+ GCC_except_table10928
+ GCC_except_table10940
+ GCC_except_table10943
+ GCC_except_table10951
+ GCC_except_table10952
+ GCC_except_table10954
+ GCC_except_table10956
+ GCC_except_table10958
+ GCC_except_table10978
+ GCC_except_table10988
+ GCC_except_table11191
+ GCC_except_table11204
+ GCC_except_table11237
+ GCC_except_table11240
+ GCC_except_table11242
+ GCC_except_table11255
+ GCC_except_table11256
+ GCC_except_table11324
+ GCC_except_table11327
+ GCC_except_table11328
+ GCC_except_table11675
+ GCC_except_table11713
+ GCC_except_table11726
+ GCC_except_table12082
+ GCC_except_table12084
+ GCC_except_table12086
+ GCC_except_table12087
+ GCC_except_table12097
+ GCC_except_table12121
+ GCC_except_table12122
+ GCC_except_table12125
+ GCC_except_table12128
+ GCC_except_table12137
+ GCC_except_table12138
+ GCC_except_table12139
+ GCC_except_table12236
+ GCC_except_table12262
+ GCC_except_table12264
+ GCC_except_table12268
+ GCC_except_table12269
+ GCC_except_table12317
+ GCC_except_table12343
+ GCC_except_table12356
+ GCC_except_table12382
+ GCC_except_table12386
+ GCC_except_table12437
+ GCC_except_table12439
+ GCC_except_table12468
+ GCC_except_table12469
+ GCC_except_table12470
+ GCC_except_table12471
+ GCC_except_table12472
+ GCC_except_table12473
+ GCC_except_table12474
+ GCC_except_table12475
+ GCC_except_table12476
+ GCC_except_table12477
+ GCC_except_table12478
+ GCC_except_table12480
+ GCC_except_table12481
+ GCC_except_table12482
+ GCC_except_table12483
+ GCC_except_table12533
+ GCC_except_table12643
+ GCC_except_table12644
+ GCC_except_table12647
+ GCC_except_table12713
+ GCC_except_table12723
+ GCC_except_table12734
+ GCC_except_table12736
+ GCC_except_table12741
+ GCC_except_table12742
+ GCC_except_table12743
+ GCC_except_table12965
+ GCC_except_table13166
+ GCC_except_table13174
+ GCC_except_table13178
+ GCC_except_table13184
+ GCC_except_table13189
+ GCC_except_table13191
+ GCC_except_table13196
+ GCC_except_table13197
+ GCC_except_table13199
+ GCC_except_table13281
+ GCC_except_table13302
+ GCC_except_table13304
+ GCC_except_table13305
+ GCC_except_table13310
+ GCC_except_table13324
+ GCC_except_table13330
+ GCC_except_table13333
+ GCC_except_table13335
+ GCC_except_table13413
+ GCC_except_table13421
+ GCC_except_table13422
+ GCC_except_table13427
+ GCC_except_table13433
+ GCC_except_table13435
+ GCC_except_table13437
+ GCC_except_table13439
+ GCC_except_table13441
+ GCC_except_table13443
+ GCC_except_table13445
+ GCC_except_table13578
+ GCC_except_table13634
+ GCC_except_table13635
+ GCC_except_table13636
+ GCC_except_table13637
+ GCC_except_table13647
+ GCC_except_table13648
+ GCC_except_table13672
+ GCC_except_table13673
+ GCC_except_table13747
+ GCC_except_table13769
+ GCC_except_table13772
+ GCC_except_table13917
+ GCC_except_table14117
+ GCC_except_table14122
+ GCC_except_table14125
+ GCC_except_table14211
+ GCC_except_table14216
+ GCC_except_table14217
+ GCC_except_table14218
+ GCC_except_table14219
+ GCC_except_table14221
+ GCC_except_table14230
+ GCC_except_table14232
+ GCC_except_table14234
+ GCC_except_table14238
+ GCC_except_table14239
+ GCC_except_table14240
+ GCC_except_table14241
+ GCC_except_table14242
+ GCC_except_table14243
+ GCC_except_table14245
+ GCC_except_table14247
+ GCC_except_table14249
+ GCC_except_table14251
+ GCC_except_table14387
+ GCC_except_table14390
+ GCC_except_table14410
+ GCC_except_table14412
+ GCC_except_table14413
+ GCC_except_table3025
+ GCC_except_table3030
+ GCC_except_table3056
+ GCC_except_table3059
+ GCC_except_table3072
+ GCC_except_table3104
+ GCC_except_table3107
+ GCC_except_table3133
+ GCC_except_table3135
+ GCC_except_table3137
+ GCC_except_table3139
+ GCC_except_table3286
+ GCC_except_table3289
+ GCC_except_table3297
+ GCC_except_table3298
+ GCC_except_table3319
+ GCC_except_table3346
+ GCC_except_table3347
+ GCC_except_table3416
+ GCC_except_table3418
+ GCC_except_table3421
+ GCC_except_table3422
+ GCC_except_table3446
+ GCC_except_table3448
+ GCC_except_table3456
+ GCC_except_table3458
+ GCC_except_table3465
+ GCC_except_table3466
+ GCC_except_table3467
+ GCC_except_table3469
+ GCC_except_table3470
+ GCC_except_table3471
+ GCC_except_table3472
+ GCC_except_table3473
+ GCC_except_table3556
+ GCC_except_table3579
+ GCC_except_table3582
+ GCC_except_table3585
+ GCC_except_table3588
+ GCC_except_table3594
+ GCC_except_table3597
+ GCC_except_table3662
+ GCC_except_table3663
+ GCC_except_table3709
+ GCC_except_table3716
+ GCC_except_table3717
+ GCC_except_table3718
+ GCC_except_table3721
+ GCC_except_table3723
+ GCC_except_table3733
+ GCC_except_table3755
+ GCC_except_table3762
+ GCC_except_table3766
+ GCC_except_table3769
+ GCC_except_table3772
+ GCC_except_table3813
+ GCC_except_table3817
+ GCC_except_table3821
+ GCC_except_table3826
+ GCC_except_table3834
+ GCC_except_table3838
+ GCC_except_table3847
+ GCC_except_table3849
+ GCC_except_table4088
+ GCC_except_table4092
+ GCC_except_table4096
+ GCC_except_table4099
+ GCC_except_table4103
+ GCC_except_table4104
+ GCC_except_table4107
+ GCC_except_table4113
+ GCC_except_table4117
+ GCC_except_table4121
+ GCC_except_table4144
+ GCC_except_table4146
+ GCC_except_table4148
+ GCC_except_table4151
+ GCC_except_table4152
+ GCC_except_table4154
+ GCC_except_table4157
+ GCC_except_table4232
+ GCC_except_table4249
+ GCC_except_table4251
+ GCC_except_table4254
+ GCC_except_table4261
+ GCC_except_table4400
+ GCC_except_table4407
+ GCC_except_table4412
+ GCC_except_table4605
+ GCC_except_table4653
+ GCC_except_table4853
+ GCC_except_table4855
+ GCC_except_table4862
+ GCC_except_table4870
+ GCC_except_table4891
+ GCC_except_table4902
+ GCC_except_table4910
+ GCC_except_table4924
+ GCC_except_table4929
+ GCC_except_table4935
+ GCC_except_table4940
+ GCC_except_table4945
+ GCC_except_table4950
+ GCC_except_table4955
+ GCC_except_table4959
+ GCC_except_table4964
+ GCC_except_table5015
+ GCC_except_table5019
+ GCC_except_table5027
+ GCC_except_table5032
+ GCC_except_table5046
+ GCC_except_table5051
+ GCC_except_table5058
+ GCC_except_table5074
+ GCC_except_table5075
+ GCC_except_table5077
+ GCC_except_table5079
+ GCC_except_table5082
+ GCC_except_table5087
+ GCC_except_table5094
+ GCC_except_table5099
+ GCC_except_table5103
+ GCC_except_table5137
+ GCC_except_table5180
+ GCC_except_table5189
+ GCC_except_table5243
+ GCC_except_table5308
+ GCC_except_table5323
+ GCC_except_table5326
+ GCC_except_table5418
+ GCC_except_table5419
+ GCC_except_table5421
+ GCC_except_table5426
+ GCC_except_table5430
+ GCC_except_table5433
+ GCC_except_table5435
+ GCC_except_table5443
+ GCC_except_table5689
+ GCC_except_table5692
+ GCC_except_table5704
+ GCC_except_table5824
+ GCC_except_table5917
+ GCC_except_table6181
+ GCC_except_table6184
+ GCC_except_table6276
+ GCC_except_table6295
+ GCC_except_table6305
+ GCC_except_table6441
+ GCC_except_table6450
+ GCC_except_table6463
+ GCC_except_table6470
+ GCC_except_table6509
+ GCC_except_table6511
+ GCC_except_table6539
+ GCC_except_table6541
+ GCC_except_table6543
+ GCC_except_table6545
+ GCC_except_table6552
+ GCC_except_table6558
+ GCC_except_table6564
+ GCC_except_table6574
+ GCC_except_table6580
+ GCC_except_table6657
+ GCC_except_table6666
+ GCC_except_table6668
+ GCC_except_table6678
+ GCC_except_table6680
+ GCC_except_table6682
+ GCC_except_table6684
+ GCC_except_table6686
+ GCC_except_table6692
+ GCC_except_table6696
+ GCC_except_table6709
+ GCC_except_table6711
+ GCC_except_table6713
+ GCC_except_table6715
+ GCC_except_table6734
+ GCC_except_table6764
+ GCC_except_table6813
+ GCC_except_table6825
+ GCC_except_table6827
+ GCC_except_table6851
+ GCC_except_table6852
+ GCC_except_table6853
+ GCC_except_table6854
+ GCC_except_table6909
+ GCC_except_table6919
+ GCC_except_table7179
+ GCC_except_table7181
+ GCC_except_table7196
+ GCC_except_table7232
+ GCC_except_table7234
+ GCC_except_table7252
+ GCC_except_table7298
+ GCC_except_table7393
+ GCC_except_table7413
+ GCC_except_table7414
+ GCC_except_table7415
+ GCC_except_table7417
+ GCC_except_table7420
+ GCC_except_table7421
+ GCC_except_table7423
+ GCC_except_table7749
+ GCC_except_table7757
+ GCC_except_table7767
+ GCC_except_table7768
+ GCC_except_table7843
+ GCC_except_table7853
+ GCC_except_table7947
+ GCC_except_table8126
+ GCC_except_table8130
+ GCC_except_table8228
+ GCC_except_table8232
+ GCC_except_table8234
+ GCC_except_table8235
+ GCC_except_table8374
+ GCC_except_table8381
+ GCC_except_table8497
+ GCC_except_table8552
+ GCC_except_table8554
+ GCC_except_table8556
+ GCC_except_table8578
+ GCC_except_table8606
+ GCC_except_table8618
+ GCC_except_table8636
+ GCC_except_table8642
+ GCC_except_table8653
+ GCC_except_table8655
+ GCC_except_table8657
+ GCC_except_table8659
+ GCC_except_table8661
+ GCC_except_table8663
+ GCC_except_table8665
+ GCC_except_table8667
+ GCC_except_table8669
+ GCC_except_table8671
+ GCC_except_table8675
+ GCC_except_table8677
+ GCC_except_table8682
+ GCC_except_table8696
+ GCC_except_table8697
+ GCC_except_table8720
+ GCC_except_table8747
+ GCC_except_table8760
+ GCC_except_table8957
+ GCC_except_table9296
+ GCC_except_table9339
+ GCC_except_table9432
+ GCC_except_table9441
+ GCC_except_table9616
+ GCC_except_table9618
+ GCC_except_table9620
+ GCC_except_table9622
+ GCC_except_table9624
+ GCC_except_table9625
+ GCC_except_table9626
+ GCC_except_table9661
+ GCC_except_table9665
+ GCC_except_table9668
+ GCC_except_table9671
+ GCC_except_table9672
+ GCC_except_table9715
+ GCC_except_table9716
+ GCC_except_table9717
+ GCC_except_table9724
+ GCC_except_table9725
+ GCC_except_table9727
+ GCC_except_table9746
+ GCC_except_table9815
+ GCC_except_table9816
+ GCC_except_table9817
+ GCC_except_table9855
+ GCC_except_table9869
+ GCC_except_table9937
+ GCC_except_table9965
+ GCC_except_table9966
+ GCC_except_table9967
+ GCC_except_table9969
+ GCC_except_table9972
+ GCC_except_table9973
+ GCC_except_table9979
+ OBJC_IVAR_$_HMAccessory._isCommissionedOverNFCWithoutPower
+ OBJC_IVAR_$_HMAccessory._networkCommissioningState
+ OBJC_IVAR_$_HMAccessory._productGroup
+ OBJC_IVAR_$_HMAccessory._productNumber
+ OBJC_IVAR_$_HMCHIPAccessorySetupPayload._supportsNFCPairing
+ OBJC_IVAR_$_HMProtoAccessoryCapabilities._supportsc7ab8e645f37
+ OBJC_IVAR_$_HMSetupAccessoryDescription._userPermissionPromptAcceptButton
+ OBJC_IVAR_$_HMSetupAccessoryDescription._userPermissionPromptCancelButton
+ OBJC_IVAR_$_HMSetupAccessoryDescription._userPermissionPromptMessage
+ OBJC_IVAR_$_HMSetupAccessoryDescription._userPermissionPromptTitle
+ OBJC_IVAR_$_HMSetupAccessoryPayload._deferredMatterOnboardingURL
+ OBJC_IVAR_$_HMSetupAccessoryPayload._deviceIdentifier
+ OBJC_IVAR_$_HMSetupAccessoryPayload._productGroup
+ OBJC_IVAR_$_HMSetupAccessoryPayload._supportsNFCPairing
+ OBJC_IVAR_$_HMSetupAccessoryPayload._threadAccessory
+ _HMAccessoryIsCommissionedOverNFCWithoutPowerCodingKey
+ _HMAccessoryNetworkCommissioningStateCodingKey
+ _HMAccessoryNetworkCommissioningStateIsReady
+ _HMAccessoryNetworkCommissioningStateToString
+ _HMAccessoryProductGroupCodingKey
+ _HMAccessoryProductNumberCodingKey
+ _HMAccessorySetupManagerProxControlLaunchRequestedMessage
+ _HMFOptionalBooleanToString
+ _HMHomeManagerPingQualityOfServiceKey
+ __OBJC_$_CLASS_METHODS_HMHome(HomeKit|HomeKit1|SwiftExtensions|HomeKit2|AccessCode|WalletInternal|Wallet|Light|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
+ __OBJC_$_INSTANCE_METHODS_HMHome(HomeKit|HomeKit1|SwiftExtensions|HomeKit2|AccessCode|WalletInternal|Wallet|Light|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
+ __OBJC_CLASS_PROTOCOLS_$_HMHome(HomeKit|HomeKit1|SwiftExtensions|HomeKit2|AccessCode|WalletInternal|Wallet|Light|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
+ ___110-[HMHomeManager _pingDeviceWithUUID:qualityOfService:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke
+ ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s64l8s40l8s48l8s56l8
+ _associated conformance 7HomeKit18SummarizationErrorOSHAASQ
+ _kAccessoryUserPermissionPromptAcceptButtonKey
+ _kAccessoryUserPermissionPromptCancelButtonKey
+ _kAccessoryUserPermissionPromptMessageKey
+ _kAccessoryUserPermissionPromptTitleKey
+ _objc_msgSend$_pingDeviceWithUUID:qualityOfService:monitor:secure:restrictToLocalNetwork:completionHandler:
+ _objc_msgSend$accessory:didUpdateUserConfigurationReady:
+ _objc_msgSend$deferredMatterOnboardingURL
+ _objc_msgSend$initWithVersion1LegacyPayloadData:value:length:payloadBytes:reserved:setupPayloadURL:outError:
+ _objc_msgSend$initWithVersion1PayloadData:value:length:payloadBytes:setupPayloadURL:outError:
+ _objc_msgSend$isCommissionedOverNFCWithoutPower
+ _objc_msgSend$isHMFError
+ _objc_msgSend$isThreadAccessory
+ _objc_msgSend$networkCommissioningState
+ _objc_msgSend$productGroup
+ _objc_msgSend$setDeferredMatterOnboardingURL:
+ _objc_msgSend$setDeviceIdentifier:
+ _objc_msgSend$setIsCommissionedOverNFCWithoutPower:
+ _objc_msgSend$setNetworkCommissioningState:
+ _objc_msgSend$setProductGroup:
+ _objc_msgSend$setSupportsNFCPairing:
+ _objc_msgSend$setThreadAccessory:
+ _objc_msgSend$setUserPermissionPromptAcceptButton:
+ _objc_msgSend$setUserPermissionPromptCancelButton:
+ _objc_msgSend$setUserPermissionPromptMessage:
+ _objc_msgSend$setUserPermissionPromptTitle:
+ _objc_msgSend$supportsNFCPairing
+ _objc_msgSend$userConfigurationReady
+ _swift_release_x25
+ _symbolic _____ 7HomeKit18SummarizationErrorO
+ _symbolic _____ 7HomeKit19SummarizationJoinerO
+ logCategory._hmf_once_t562
+ logCategory._hmf_once_v563
- GCC_except_table10110
- GCC_except_table10111
- GCC_except_table10112
- GCC_except_table10116
- GCC_except_table10171
- GCC_except_table10192
- GCC_except_table10272
- GCC_except_table10274
- GCC_except_table10276
- GCC_except_table10278
- GCC_except_table10286
- GCC_except_table10333
- GCC_except_table10345
- GCC_except_table10347
- GCC_except_table10537
- GCC_except_table10538
- GCC_except_table10573
- GCC_except_table10606
- GCC_except_table10609
- GCC_except_table10612
- GCC_except_table10614
- GCC_except_table10680
- GCC_except_table10700
- GCC_except_table10701
- GCC_except_table10702
- GCC_except_table10741
- GCC_except_table10743
- GCC_except_table10745
- GCC_except_table10810
- GCC_except_table10842
- GCC_except_table10844
- GCC_except_table10848
- GCC_except_table10865
- GCC_except_table10867
- GCC_except_table10877
- GCC_except_table10880
- GCC_except_table10887
- GCC_except_table10891
- GCC_except_table10897
- GCC_except_table10909
- GCC_except_table10912
- GCC_except_table10920
- GCC_except_table10921
- GCC_except_table10923
- GCC_except_table10925
- GCC_except_table10927
- GCC_except_table10947
- GCC_except_table10957
- GCC_except_table11160
- GCC_except_table11173
- GCC_except_table11206
- GCC_except_table11209
- GCC_except_table11211
- GCC_except_table11224
- GCC_except_table11225
- GCC_except_table11293
- GCC_except_table11296
- GCC_except_table11297
- GCC_except_table11648
- GCC_except_table11686
- GCC_except_table11699
- GCC_except_table12055
- GCC_except_table12057
- GCC_except_table12059
- GCC_except_table12060
- GCC_except_table12070
- GCC_except_table12094
- GCC_except_table12095
- GCC_except_table12098
- GCC_except_table12101
- GCC_except_table12110
- GCC_except_table12111
- GCC_except_table12112
- GCC_except_table12209
- GCC_except_table12235
- GCC_except_table12237
- GCC_except_table12241
- GCC_except_table12242
- GCC_except_table12290
- GCC_except_table12316
- GCC_except_table12329
- GCC_except_table12355
- GCC_except_table12359
- GCC_except_table12410
- GCC_except_table12412
- GCC_except_table12441
- GCC_except_table12442
- GCC_except_table12443
- GCC_except_table12444
- GCC_except_table12445
- GCC_except_table12446
- GCC_except_table12447
- GCC_except_table12448
- GCC_except_table12449
- GCC_except_table12450
- GCC_except_table12451
- GCC_except_table12452
- GCC_except_table12453
- GCC_except_table12454
- GCC_except_table12455
- GCC_except_table12456
- GCC_except_table12616
- GCC_except_table12617
- GCC_except_table12620
- GCC_except_table12686
- GCC_except_table12688
- GCC_except_table12696
- GCC_except_table12707
- GCC_except_table12709
- GCC_except_table12714
- GCC_except_table12716
- GCC_except_table12938
- GCC_except_table13139
- GCC_except_table13142
- GCC_except_table13147
- GCC_except_table13151
- GCC_except_table13157
- GCC_except_table13162
- GCC_except_table13164
- GCC_except_table13170
- GCC_except_table13172
- GCC_except_table13254
- GCC_except_table13256
- GCC_except_table13275
- GCC_except_table13276
- GCC_except_table13277
- GCC_except_table13278
- GCC_except_table13297
- GCC_except_table13306
- GCC_except_table13308
- GCC_except_table13386
- GCC_except_table13394
- GCC_except_table13395
- GCC_except_table13400
- GCC_except_table13406
- GCC_except_table13408
- GCC_except_table13410
- GCC_except_table13412
- GCC_except_table13414
- GCC_except_table13416
- GCC_except_table13418
- GCC_except_table13551
- GCC_except_table13607
- GCC_except_table13608
- GCC_except_table13609
- GCC_except_table13610
- GCC_except_table13620
- GCC_except_table13621
- GCC_except_table13645
- GCC_except_table13646
- GCC_except_table13720
- GCC_except_table13742
- GCC_except_table13745
- GCC_except_table13878
- GCC_except_table14078
- GCC_except_table14083
- GCC_except_table14086
- GCC_except_table14139
- GCC_except_table14172
- GCC_except_table14177
- GCC_except_table14179
- GCC_except_table14180
- GCC_except_table14182
- GCC_except_table14191
- GCC_except_table14193
- GCC_except_table14195
- GCC_except_table14199
- GCC_except_table14200
- GCC_except_table14201
- GCC_except_table14202
- GCC_except_table14203
- GCC_except_table14204
- GCC_except_table14206
- GCC_except_table14208
- GCC_except_table14210
- GCC_except_table14212
- GCC_except_table14347
- GCC_except_table14350
- GCC_except_table14370
- GCC_except_table14372
- GCC_except_table14373
- GCC_except_table3015
- GCC_except_table3020
- GCC_except_table3046
- GCC_except_table3049
- GCC_except_table3062
- GCC_except_table3094
- GCC_except_table3097
- GCC_except_table3123
- GCC_except_table3125
- GCC_except_table3127
- GCC_except_table3129
- GCC_except_table3276
- GCC_except_table3279
- GCC_except_table3287
- GCC_except_table3288
- GCC_except_table3309
- GCC_except_table3336
- GCC_except_table3337
- GCC_except_table3392
- GCC_except_table3402
- GCC_except_table3496
- GCC_except_table3559
- GCC_except_table3561
- GCC_except_table3564
- GCC_except_table3565
- GCC_except_table3589
- GCC_except_table3599
- GCC_except_table3601
- GCC_except_table3608
- GCC_except_table3609
- GCC_except_table3610
- GCC_except_table3612
- GCC_except_table3613
- GCC_except_table3614
- GCC_except_table3615
- GCC_except_table3616
- GCC_except_table3699
- GCC_except_table3728
- GCC_except_table3731
- GCC_except_table3734
- GCC_except_table3737
- GCC_except_table3740
- GCC_except_table3805
- GCC_except_table3806
- GCC_except_table3852
- GCC_except_table3859
- GCC_except_table3860
- GCC_except_table3861
- GCC_except_table3864
- GCC_except_table3865
- GCC_except_table3866
- GCC_except_table3868
- GCC_except_table3876
- GCC_except_table3898
- GCC_except_table3905
- GCC_except_table3909
- GCC_except_table3912
- GCC_except_table3915
- GCC_except_table3956
- GCC_except_table3960
- GCC_except_table3964
- GCC_except_table3969
- GCC_except_table3977
- GCC_except_table3981
- GCC_except_table3990
- GCC_except_table3992
- GCC_except_table4231
- GCC_except_table4235
- GCC_except_table4239
- GCC_except_table4242
- GCC_except_table4247
- GCC_except_table4250
- GCC_except_table4256
- GCC_except_table4260
- GCC_except_table4264
- GCC_except_table4287
- GCC_except_table4289
- GCC_except_table4291
- GCC_except_table4294
- GCC_except_table4295
- GCC_except_table4297
- GCC_except_table4300
- GCC_except_table4375
- GCC_except_table4389
- GCC_except_table4392
- GCC_except_table4394
- GCC_except_table4397
- GCC_except_table4404
- GCC_except_table4458
- GCC_except_table4523
- GCC_except_table4538
- GCC_except_table4541
- GCC_except_table4633
- GCC_except_table4634
- GCC_except_table4636
- GCC_except_table4641
- GCC_except_table4645
- GCC_except_table4648
- GCC_except_table4650
- GCC_except_table4658
- GCC_except_table4904
- GCC_except_table4919
- GCC_except_table4995
- GCC_except_table5039
- GCC_except_table5132
- GCC_except_table5383
- GCC_except_table5386
- GCC_except_table5477
- GCC_except_table5496
- GCC_except_table5506
- GCC_except_table5641
- GCC_except_table5650
- GCC_except_table5663
- GCC_except_table5670
- GCC_except_table5709
- GCC_except_table5711
- GCC_except_table5739
- GCC_except_table5741
- GCC_except_table5743
- GCC_except_table5745
- GCC_except_table5752
- GCC_except_table5758
- GCC_except_table5764
- GCC_except_table5774
- GCC_except_table5857
- GCC_except_table5866
- GCC_except_table5868
- GCC_except_table5878
- GCC_except_table5880
- GCC_except_table5882
- GCC_except_table5884
- GCC_except_table5886
- GCC_except_table5892
- GCC_except_table5896
- GCC_except_table5909
- GCC_except_table5911
- GCC_except_table5913
- GCC_except_table5915
- GCC_except_table5934
- GCC_except_table5963
- GCC_except_table6012
- GCC_except_table6024
- GCC_except_table6026
- GCC_except_table6050
- GCC_except_table6051
- GCC_except_table6052
- GCC_except_table6053
- GCC_except_table6108
- GCC_except_table6118
- GCC_except_table6378
- GCC_except_table6380
- GCC_except_table6395
- GCC_except_table6431
- GCC_except_table6433
- GCC_except_table6451
- GCC_except_table6497
- GCC_except_table6592
- GCC_except_table6612
- GCC_except_table6613
- GCC_except_table6614
- GCC_except_table6616
- GCC_except_table6619
- GCC_except_table6620
- GCC_except_table6622
- GCC_except_table6948
- GCC_except_table6954
- GCC_except_table6956
- GCC_except_table6966
- GCC_except_table6967
- GCC_except_table7172
- GCC_except_table7176
- GCC_except_table7287
- GCC_except_table7291
- GCC_except_table7293
- GCC_except_table7294
- GCC_except_table7433
- GCC_except_table7440
- GCC_except_table7556
- GCC_except_table7611
- GCC_except_table7613
- GCC_except_table7615
- GCC_except_table7637
- GCC_except_table7665
- GCC_except_table7677
- GCC_except_table7694
- GCC_except_table7700
- GCC_except_table7711
- GCC_except_table7713
- GCC_except_table7715
- GCC_except_table7717
- GCC_except_table7719
- GCC_except_table7721
- GCC_except_table7723
- GCC_except_table7725
- GCC_except_table7727
- GCC_except_table7729
- GCC_except_table7731
- GCC_except_table7733
- GCC_except_table7735
- GCC_except_table7740
- GCC_except_table7754
- GCC_except_table7778
- GCC_except_table7780
- GCC_except_table7805
- GCC_except_table7818
- GCC_except_table7836
- GCC_except_table8015
- GCC_except_table8350
- GCC_except_table8393
- GCC_except_table8486
- GCC_except_table8495
- GCC_except_table8670
- GCC_except_table8672
- GCC_except_table8674
- GCC_except_table8676
- GCC_except_table8678
- GCC_except_table8679
- GCC_except_table8680
- GCC_except_table8715
- GCC_except_table8718
- GCC_except_table8719
- GCC_except_table8725
- GCC_except_table8726
- GCC_except_table8769
- GCC_except_table8770
- GCC_except_table8771
- GCC_except_table8779
- GCC_except_table8781
- GCC_except_table8800
- GCC_except_table8961
- GCC_except_table8968
- GCC_except_table8973
- GCC_except_table9166
- GCC_except_table9214
- GCC_except_table9414
- GCC_except_table9416
- GCC_except_table9423
- GCC_except_table9431
- GCC_except_table9452
- GCC_except_table9463
- GCC_except_table9468
- GCC_except_table9471
- GCC_except_table9485
- GCC_except_table9490
- GCC_except_table9496
- GCC_except_table9501
- GCC_except_table9506
- GCC_except_table9511
- GCC_except_table9516
- GCC_except_table9520
- GCC_except_table9525
- GCC_except_table9576
- GCC_except_table9580
- GCC_except_table9588
- GCC_except_table9593
- GCC_except_table9607
- GCC_except_table9612
- GCC_except_table9635
- GCC_except_table9636
- GCC_except_table9638
- GCC_except_table9640
- GCC_except_table9643
- GCC_except_table9648
- GCC_except_table9655
- GCC_except_table9660
- GCC_except_table9698
- GCC_except_table9741
- GCC_except_table9750
- GCC_except_table9797
- GCC_except_table9798
- GCC_except_table9799
- GCC_except_table9837
- GCC_except_table9851
- GCC_except_table9919
- GCC_except_table9947
- GCC_except_table9948
- GCC_except_table9949
- GCC_except_table9951
- GCC_except_table9954
- GCC_except_table9955
- GCC_except_table9961
- __OBJC_$_CLASS_METHODS_HMHome(HomeKit|HomeKit1|HomeKit2|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- __OBJC_$_INSTANCE_METHODS_HMHome(HomeKit|HomeKit1|HomeKit2|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- __OBJC_CLASS_PROTOCOLS_$_HMHome(HomeKit|HomeKit1|HomeKit2|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke
- ___block_descriptor_72_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56s64bs_e34_v24?0"NSError"8"NSDictionary"16ls32l8s40l8s48l8s64l8s56l8
- logCategory._hmf_once_t560
- logCategory._hmf_once_v561
CStrings:
+ "%012llx"
+ ", Commissioned Over NFC Without Power: %@"
+ ", Device Identifier: %@"
+ ", Is Thread Accessory: %@"
+ ", Matter Onboarding URL: %@"
+ ", Network Commissioning State: %@"
+ ", Product Group: %@"
+ ", product Group: %@"
+ ", product Number: %@"
+ ", productID: %@"
+ ", vendorID: %@"
+ "-[HMHomeManager _pingDeviceWithUUID:qualityOfService:monitor:secure:restrictToLocalNetwork:completionHandler:]"
+ "Completed"
+ "HMA.isCommissionedOverNFCWithoutPower"
+ "HMA.productGroup"
+ "HMA.productNumber"
+ "HMASM.m.proxControlLaunchRequested"
+ "HMAccessoryCommissioningStateCodingKey"
+ "HMCASP.ck.supportsNFCPairing"
+ "HMUserConsentResponseNoForUserPermissionPrompt"
+ "HMUserConsentResponseYesForUserPermissionPrompt"
+ "NFC pairing tap detected"
+ "Notifying client of updated userConfigurationReady: %{BOOL}d"
+ "Pending"
+ "Requires user permission for PPID confirmation"
+ "Requires user permission for uncertified accessory"
+ "SetupPayload: V1 failed to decode suffix with EUI64: %@"
+ "SetupPayload: V1 failed to decode suffix: %@"
+ "SetupPayload: V1 legacy payload (length %tu)"
+ "SetupPayload: V1 parsed - SetupID:%@ PN:%@ PG:%@"
+ "SetupPayload: V1 parsed - paired:%d NFC:%d SetupID:%@ PN:%@ PG:%@ DeviceID:%@"
+ "SetupPayload: V1 parsed with EUI64 - PN:%@ PG:%@ EUI:%@"
+ "SetupPayload: V1 payload (length %tu)"
+ "SetupPayload: V1 payload too short - expected %tu, got %tu"
+ "SetupPayload: V1 payload too short for EUI64 - expected %tu, got %tu"
+ "[%{public}@] Notifying client of updated userConfigurationReady: %{BOOL}d"
+ "[%{public}@] SetupPayload: V1 failed to decode suffix with EUI64: %@"
+ "[%{public}@] SetupPayload: V1 failed to decode suffix: %@"
+ "[%{public}@] SetupPayload: V1 legacy payload (length %tu)"
+ "[%{public}@] SetupPayload: V1 parsed - SetupID:%@ PN:%@ PG:%@"
+ "[%{public}@] SetupPayload: V1 parsed - paired:%d NFC:%d SetupID:%@ PN:%@ PG:%@ DeviceID:%@"
+ "[%{public}@] SetupPayload: V1 parsed with EUI64 - PN:%@ PG:%@ EUI:%@"
+ "[%{public}@] SetupPayload: V1 payload (length %tu)"
+ "[%{public}@] SetupPayload: V1 payload too short - expected %tu, got %tu"
+ "[%{public}@] SetupPayload: V1 payload too short for EUI64 - expected %tu, got %tu"
+ "isThreadAccessory"
+ "kAccessoryUserPermissionPromptAcceptButtonKey"
+ "kAccessoryUserPermissionPromptCancelButtonKey"
+ "kAccessoryUserPermissionPromptMessageKey"
+ "kAccessoryUserPermissionPromptTitleKey"
+ "matterOnboardingURL"
+ "productGroup"
+ "qualityOfService"
+ "supportsNFCPairing"
+ "supportsc7ab8e645f37"
- "-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]"
```
