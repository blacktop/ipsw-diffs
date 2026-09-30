## HomeKit

> `/System/Library/PrivateFrameworks/HomeKit.framework/Versions/A/HomeKit`

```diff

-1490.2.0.0.0
-  __TEXT.__text: 0x3f3d58
-  __TEXT.__objc_methlist: 0x2801c
-  __TEXT.__const: 0x66f8
+1493.1.5.4.1
+  __TEXT.__text: 0x3f6cb0
+  __TEXT.__objc_methlist: 0x281ec
+  __TEXT.__const: 0x6818
   __TEXT.__dlopen_cstrs: 0x3bb
-  __TEXT.__swift5_typeref: 0x1fd4
-  __TEXT.__cstring: 0x2ea1b
-  __TEXT.__constg_swiftt: 0x1c60
-  __TEXT.__swift5_reflstr: 0x1154
-  __TEXT.__swift5_fieldmd: 0x143c
+  __TEXT.__swift5_typeref: 0x1fe8
+  __TEXT.__cstring: 0x2eddf
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
-  __TEXT.__oslogstring: 0x55476
+  __TEXT.__oslogstring: 0x55954
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__gcc_except_tab: 0x67a0
   __TEXT.__ustring: 0x50
-  __TEXT.__unwind_info: 0xc4f0
+  __TEXT.__unwind_info: 0xc540
   __TEXT.__eh_frame: 0x7a10
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5900
+  __DATA_CONST.__const: 0x5978
   __DATA_CONST.__objc_classlist: 0x1338
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x558
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf08
+  __DATA_CONST.__objc_selrefs: 0xe000
   __DATA_CONST.__objc_protorefs: 0x110
   __DATA_CONST.__objc_superrefs: 0xf90
   __DATA_CONST.__objc_arraydata: 0x13f0
-  __DATA_CONST.__got: 0x1dd0
-  __AUTH_CONST.__const: 0x9cf8
-  __AUTH_CONST.__cfstring: 0x2af00
-  __AUTH_CONST.__objc_const: 0x47f48
+  __DATA_CONST.__got: 0x1dd8
+  __AUTH_CONST.__const: 0x9e18
+  __AUTH_CONST.__cfstring: 0x2b340
+  __AUTH_CONST.__objc_const: 0x482b0
   __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_dictobj: 0x848
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_doubleobj: 0x70
-  __AUTH_CONST.__auth_got: 0x1818
+  __AUTH_CONST.__auth_got: 0x1830
   __AUTH.__objc_data: 0x8e00
-  __AUTH.__data: 0x17b8
-  __DATA.__objc_ivar: 0x2768
-  __DATA.__data: 0x51d0
-  __DATA.__bss: 0x9460
+  __AUTH.__data: 0x17a8
+  __DATA.__objc_ivar: 0x27a4
+  __DATA.__data: 0x51f0
+  __DATA.__bss: 0x9660
   __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x36f0
   __DATA_DIRTY.__data: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17383
-  Symbols:   32273
-  CStrings:  12138
+  Functions: 17435
+  Symbols:   32364
+  CStrings:  12192
 
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
+ GCC_except_table10003
+ GCC_except_table10004
+ GCC_except_table10005
+ GCC_except_table10007
+ GCC_except_table10010
+ GCC_except_table10011
+ GCC_except_table10017
+ GCC_except_table10166
+ GCC_except_table10167
+ GCC_except_table10168
+ GCC_except_table10172
+ GCC_except_table10227
+ GCC_except_table10250
+ GCC_except_table10330
+ GCC_except_table10332
+ GCC_except_table10334
+ GCC_except_table10336
+ GCC_except_table10344
+ GCC_except_table10391
+ GCC_except_table10403
+ GCC_except_table10405
+ GCC_except_table10595
+ GCC_except_table10596
+ GCC_except_table10631
+ GCC_except_table10664
+ GCC_except_table10667
+ GCC_except_table10670
+ GCC_except_table10672
+ GCC_except_table10751
+ GCC_except_table10771
+ GCC_except_table10772
+ GCC_except_table10773
+ GCC_except_table10812
+ GCC_except_table10814
+ GCC_except_table10816
+ GCC_except_table10881
+ GCC_except_table10915
+ GCC_except_table10919
+ GCC_except_table10936
+ GCC_except_table10938
+ GCC_except_table10944
+ GCC_except_table10948
+ GCC_except_table10951
+ GCC_except_table10958
+ GCC_except_table10962
+ GCC_except_table10968
+ GCC_except_table10980
+ GCC_except_table10983
+ GCC_except_table10991
+ GCC_except_table10992
+ GCC_except_table10994
+ GCC_except_table10996
+ GCC_except_table10998
+ GCC_except_table11018
+ GCC_except_table11028
+ GCC_except_table11231
+ GCC_except_table11244
+ GCC_except_table11277
+ GCC_except_table11280
+ GCC_except_table11282
+ GCC_except_table11295
+ GCC_except_table11296
+ GCC_except_table11364
+ GCC_except_table11367
+ GCC_except_table11368
+ GCC_except_table11715
+ GCC_except_table11753
+ GCC_except_table11766
+ GCC_except_table12122
+ GCC_except_table12124
+ GCC_except_table12126
+ GCC_except_table12127
+ GCC_except_table12137
+ GCC_except_table12161
+ GCC_except_table12162
+ GCC_except_table12165
+ GCC_except_table12168
+ GCC_except_table12177
+ GCC_except_table12178
+ GCC_except_table12179
+ GCC_except_table12276
+ GCC_except_table12302
+ GCC_except_table12304
+ GCC_except_table12308
+ GCC_except_table12309
+ GCC_except_table12357
+ GCC_except_table12383
+ GCC_except_table12396
+ GCC_except_table12422
+ GCC_except_table12426
+ GCC_except_table12477
+ GCC_except_table12479
+ GCC_except_table12508
+ GCC_except_table12509
+ GCC_except_table12510
+ GCC_except_table12511
+ GCC_except_table12512
+ GCC_except_table12513
+ GCC_except_table12514
+ GCC_except_table12515
+ GCC_except_table12516
+ GCC_except_table12517
+ GCC_except_table12518
+ GCC_except_table12520
+ GCC_except_table12521
+ GCC_except_table12522
+ GCC_except_table12523
+ GCC_except_table12573
+ GCC_except_table12683
+ GCC_except_table12684
+ GCC_except_table12687
+ GCC_except_table12753
+ GCC_except_table12763
+ GCC_except_table12774
+ GCC_except_table12776
+ GCC_except_table12781
+ GCC_except_table12782
+ GCC_except_table12783
+ GCC_except_table13005
+ GCC_except_table13209
+ GCC_except_table13218
+ GCC_except_table13226
+ GCC_except_table13231
+ GCC_except_table13233
+ GCC_except_table13238
+ GCC_except_table13239
+ GCC_except_table13241
+ GCC_except_table13323
+ GCC_except_table13344
+ GCC_except_table13346
+ GCC_except_table13347
+ GCC_except_table13366
+ GCC_except_table13372
+ GCC_except_table13375
+ GCC_except_table13379
+ GCC_except_table13457
+ GCC_except_table13465
+ GCC_except_table13466
+ GCC_except_table13471
+ GCC_except_table13477
+ GCC_except_table13479
+ GCC_except_table13481
+ GCC_except_table13483
+ GCC_except_table13485
+ GCC_except_table13487
+ GCC_except_table13489
+ GCC_except_table13622
+ GCC_except_table13678
+ GCC_except_table13679
+ GCC_except_table13680
+ GCC_except_table13681
+ GCC_except_table13691
+ GCC_except_table13692
+ GCC_except_table13716
+ GCC_except_table13717
+ GCC_except_table13791
+ GCC_except_table13813
+ GCC_except_table13816
+ GCC_except_table13961
+ GCC_except_table14131
+ GCC_except_table14136
+ GCC_except_table14139
+ GCC_except_table14225
+ GCC_except_table14230
+ GCC_except_table14231
+ GCC_except_table14232
+ GCC_except_table14233
+ GCC_except_table14235
+ GCC_except_table14244
+ GCC_except_table14246
+ GCC_except_table14248
+ GCC_except_table14252
+ GCC_except_table14253
+ GCC_except_table14254
+ GCC_except_table14255
+ GCC_except_table14256
+ GCC_except_table14257
+ GCC_except_table14259
+ GCC_except_table14261
+ GCC_except_table14263
+ GCC_except_table14265
+ GCC_except_table14401
+ GCC_except_table14404
+ GCC_except_table14424
+ GCC_except_table14426
+ GCC_except_table14427
+ GCC_except_table3048
+ GCC_except_table3053
+ GCC_except_table3079
+ GCC_except_table3082
+ GCC_except_table3095
+ GCC_except_table3127
+ GCC_except_table3130
+ GCC_except_table3156
+ GCC_except_table3158
+ GCC_except_table3160
+ GCC_except_table3162
+ GCC_except_table3309
+ GCC_except_table3312
+ GCC_except_table3320
+ GCC_except_table3321
+ GCC_except_table3342
+ GCC_except_table3369
+ GCC_except_table3370
+ GCC_except_table3428
+ GCC_except_table3430
+ GCC_except_table3433
+ GCC_except_table3434
+ GCC_except_table3460
+ GCC_except_table3462
+ GCC_except_table3470
+ GCC_except_table3472
+ GCC_except_table3479
+ GCC_except_table3480
+ GCC_except_table3481
+ GCC_except_table3483
+ GCC_except_table3484
+ GCC_except_table3485
+ GCC_except_table3486
+ GCC_except_table3487
+ GCC_except_table3570
+ GCC_except_table3593
+ GCC_except_table3596
+ GCC_except_table3599
+ GCC_except_table3602
+ GCC_except_table3608
+ GCC_except_table3611
+ GCC_except_table3676
+ GCC_except_table3677
+ GCC_except_table3723
+ GCC_except_table3730
+ GCC_except_table3731
+ GCC_except_table3732
+ GCC_except_table3735
+ GCC_except_table3736
+ GCC_except_table3737
+ GCC_except_table3739
+ GCC_except_table3769
+ GCC_except_table3778
+ GCC_except_table3782
+ GCC_except_table3785
+ GCC_except_table3788
+ GCC_except_table3829
+ GCC_except_table3833
+ GCC_except_table3837
+ GCC_except_table3842
+ GCC_except_table3850
+ GCC_except_table3854
+ GCC_except_table3863
+ GCC_except_table3865
+ GCC_except_table4104
+ GCC_except_table4109
+ GCC_except_table4113
+ GCC_except_table4116
+ GCC_except_table4120
+ GCC_except_table4121
+ GCC_except_table4126
+ GCC_except_table4132
+ GCC_except_table4136
+ GCC_except_table4140
+ GCC_except_table4163
+ GCC_except_table4165
+ GCC_except_table4167
+ GCC_except_table4170
+ GCC_except_table4171
+ GCC_except_table4173
+ GCC_except_table4176
+ GCC_except_table4251
+ GCC_except_table4268
+ GCC_except_table4270
+ GCC_except_table4273
+ GCC_except_table4280
+ GCC_except_table4419
+ GCC_except_table4426
+ GCC_except_table4431
+ GCC_except_table4624
+ GCC_except_table4672
+ GCC_except_table4872
+ GCC_except_table4874
+ GCC_except_table4881
+ GCC_except_table4889
+ GCC_except_table4910
+ GCC_except_table4921
+ GCC_except_table4926
+ GCC_except_table4929
+ GCC_except_table4943
+ GCC_except_table4948
+ GCC_except_table4954
+ GCC_except_table4959
+ GCC_except_table4964
+ GCC_except_table4969
+ GCC_except_table4974
+ GCC_except_table4978
+ GCC_except_table4983
+ GCC_except_table5030
+ GCC_except_table5034
+ GCC_except_table5044
+ GCC_except_table5049
+ GCC_except_table5063
+ GCC_except_table5068
+ GCC_except_table5075
+ GCC_except_table5092
+ GCC_except_table5093
+ GCC_except_table5095
+ GCC_except_table5097
+ GCC_except_table5100
+ GCC_except_table5105
+ GCC_except_table5112
+ GCC_except_table5117
+ GCC_except_table5121
+ GCC_except_table5157
+ GCC_except_table5204
+ GCC_except_table5215
+ GCC_except_table5269
+ GCC_except_table5334
+ GCC_except_table5349
+ GCC_except_table5352
+ GCC_except_table5444
+ GCC_except_table5445
+ GCC_except_table5448
+ GCC_except_table5453
+ GCC_except_table5457
+ GCC_except_table5460
+ GCC_except_table5462
+ GCC_except_table5470
+ GCC_except_table5716
+ GCC_except_table5719
+ GCC_except_table5731
+ GCC_except_table5807
+ GCC_except_table5851
+ GCC_except_table5944
+ GCC_except_table6208
+ GCC_except_table6211
+ GCC_except_table6303
+ GCC_except_table6322
+ GCC_except_table6332
+ GCC_except_table6468
+ GCC_except_table6477
+ GCC_except_table6490
+ GCC_except_table6497
+ GCC_except_table6536
+ GCC_except_table6538
+ GCC_except_table6566
+ GCC_except_table6568
+ GCC_except_table6570
+ GCC_except_table6572
+ GCC_except_table6579
+ GCC_except_table6585
+ GCC_except_table6591
+ GCC_except_table6601
+ GCC_except_table6607
+ GCC_except_table6684
+ GCC_except_table6693
+ GCC_except_table6695
+ GCC_except_table6705
+ GCC_except_table6707
+ GCC_except_table6709
+ GCC_except_table6711
+ GCC_except_table6713
+ GCC_except_table6719
+ GCC_except_table6723
+ GCC_except_table6736
+ GCC_except_table6738
+ GCC_except_table6740
+ GCC_except_table6742
+ GCC_except_table6761
+ GCC_except_table6791
+ GCC_except_table6840
+ GCC_except_table6852
+ GCC_except_table6854
+ GCC_except_table6878
+ GCC_except_table6879
+ GCC_except_table6880
+ GCC_except_table6881
+ GCC_except_table6936
+ GCC_except_table6949
+ GCC_except_table7209
+ GCC_except_table7211
+ GCC_except_table7226
+ GCC_except_table7264
+ GCC_except_table7266
+ GCC_except_table7284
+ GCC_except_table7330
+ GCC_except_table7425
+ GCC_except_table7445
+ GCC_except_table7446
+ GCC_except_table7447
+ GCC_except_table7449
+ GCC_except_table7452
+ GCC_except_table7453
+ GCC_except_table7455
+ GCC_except_table7781
+ GCC_except_table7789
+ GCC_except_table7799
+ GCC_except_table7800
+ GCC_except_table7875
+ GCC_except_table7885
+ GCC_except_table7981
+ GCC_except_table8160
+ GCC_except_table8164
+ GCC_except_table8262
+ GCC_except_table8266
+ GCC_except_table8268
+ GCC_except_table8269
+ GCC_except_table8408
+ GCC_except_table8417
+ GCC_except_table8533
+ GCC_except_table8588
+ GCC_except_table8590
+ GCC_except_table8592
+ GCC_except_table8614
+ GCC_except_table8642
+ GCC_except_table8654
+ GCC_except_table8672
+ GCC_except_table8678
+ GCC_except_table8689
+ GCC_except_table8691
+ GCC_except_table8693
+ GCC_except_table8695
+ GCC_except_table8697
+ GCC_except_table8699
+ GCC_except_table8701
+ GCC_except_table8703
+ GCC_except_table8705
+ GCC_except_table8709
+ GCC_except_table8711
+ GCC_except_table8718
+ GCC_except_table8732
+ GCC_except_table8733
+ GCC_except_table8758
+ GCC_except_table8785
+ GCC_except_table8798
+ GCC_except_table8816
+ GCC_except_table9334
+ GCC_except_table9377
+ GCC_except_table9470
+ GCC_except_table9479
+ GCC_except_table9654
+ GCC_except_table9656
+ GCC_except_table9657
+ GCC_except_table9658
+ GCC_except_table9660
+ GCC_except_table9662
+ GCC_except_table9663
+ GCC_except_table9664
+ GCC_except_table9699
+ GCC_except_table9702
+ GCC_except_table9703
+ GCC_except_table9706
+ GCC_except_table9709
+ GCC_except_table9710
+ GCC_except_table9753
+ GCC_except_table9754
+ GCC_except_table9755
+ GCC_except_table9762
+ GCC_except_table9763
+ GCC_except_table9765
+ GCC_except_table9784
+ GCC_except_table9853
+ GCC_except_table9854
+ GCC_except_table9855
+ GCC_except_table9893
+ GCC_except_table9907
+ GCC_except_table9975
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
+ ___35-[HMAccessory updateAccessoryInfo:]_block_invoke_4
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
+ _symbolic _____ 7HomeKit18SummarizationErrorO
+ _symbolic _____ 7HomeKit19SummarizationJoinerO
+ logCategory._hmf_once_t562
+ logCategory._hmf_once_v563
- GCC_except_table10148
- GCC_except_table10149
- GCC_except_table10150
- GCC_except_table10154
- GCC_except_table10209
- GCC_except_table10232
- GCC_except_table10312
- GCC_except_table10314
- GCC_except_table10316
- GCC_except_table10318
- GCC_except_table10326
- GCC_except_table10373
- GCC_except_table10385
- GCC_except_table10387
- GCC_except_table10577
- GCC_except_table10578
- GCC_except_table10613
- GCC_except_table10646
- GCC_except_table10649
- GCC_except_table10652
- GCC_except_table10654
- GCC_except_table10720
- GCC_except_table10740
- GCC_except_table10741
- GCC_except_table10742
- GCC_except_table10781
- GCC_except_table10783
- GCC_except_table10785
- GCC_except_table10850
- GCC_except_table10882
- GCC_except_table10884
- GCC_except_table10888
- GCC_except_table10905
- GCC_except_table10907
- GCC_except_table10917
- GCC_except_table10920
- GCC_except_table10927
- GCC_except_table10931
- GCC_except_table10937
- GCC_except_table10949
- GCC_except_table10952
- GCC_except_table10960
- GCC_except_table10961
- GCC_except_table10963
- GCC_except_table10965
- GCC_except_table10967
- GCC_except_table10987
- GCC_except_table10997
- GCC_except_table11200
- GCC_except_table11213
- GCC_except_table11246
- GCC_except_table11249
- GCC_except_table11251
- GCC_except_table11264
- GCC_except_table11265
- GCC_except_table11333
- GCC_except_table11336
- GCC_except_table11337
- GCC_except_table11688
- GCC_except_table11726
- GCC_except_table11739
- GCC_except_table12095
- GCC_except_table12097
- GCC_except_table12099
- GCC_except_table12100
- GCC_except_table12110
- GCC_except_table12134
- GCC_except_table12135
- GCC_except_table12138
- GCC_except_table12141
- GCC_except_table12150
- GCC_except_table12151
- GCC_except_table12152
- GCC_except_table12249
- GCC_except_table12275
- GCC_except_table12277
- GCC_except_table12281
- GCC_except_table12282
- GCC_except_table12330
- GCC_except_table12356
- GCC_except_table12369
- GCC_except_table12395
- GCC_except_table12399
- GCC_except_table12450
- GCC_except_table12452
- GCC_except_table12481
- GCC_except_table12482
- GCC_except_table12483
- GCC_except_table12484
- GCC_except_table12485
- GCC_except_table12486
- GCC_except_table12487
- GCC_except_table12488
- GCC_except_table12489
- GCC_except_table12490
- GCC_except_table12491
- GCC_except_table12492
- GCC_except_table12493
- GCC_except_table12494
- GCC_except_table12495
- GCC_except_table12496
- GCC_except_table12656
- GCC_except_table12657
- GCC_except_table12660
- GCC_except_table12726
- GCC_except_table12728
- GCC_except_table12736
- GCC_except_table12747
- GCC_except_table12749
- GCC_except_table12754
- GCC_except_table12756
- GCC_except_table12978
- GCC_except_table13179
- GCC_except_table13182
- GCC_except_table13187
- GCC_except_table13191
- GCC_except_table13199
- GCC_except_table13204
- GCC_except_table13211
- GCC_except_table13212
- GCC_except_table13296
- GCC_except_table13298
- GCC_except_table13317
- GCC_except_table13318
- GCC_except_table13319
- GCC_except_table13320
- GCC_except_table13339
- GCC_except_table13348
- GCC_except_table13430
- GCC_except_table13438
- GCC_except_table13439
- GCC_except_table13444
- GCC_except_table13450
- GCC_except_table13452
- GCC_except_table13454
- GCC_except_table13456
- GCC_except_table13458
- GCC_except_table13460
- GCC_except_table13462
- GCC_except_table13595
- GCC_except_table13651
- GCC_except_table13652
- GCC_except_table13653
- GCC_except_table13654
- GCC_except_table13664
- GCC_except_table13665
- GCC_except_table13689
- GCC_except_table13690
- GCC_except_table13764
- GCC_except_table13786
- GCC_except_table13789
- GCC_except_table13922
- GCC_except_table14092
- GCC_except_table14097
- GCC_except_table14100
- GCC_except_table14153
- GCC_except_table14186
- GCC_except_table14191
- GCC_except_table14193
- GCC_except_table14194
- GCC_except_table14196
- GCC_except_table14205
- GCC_except_table14207
- GCC_except_table14209
- GCC_except_table14213
- GCC_except_table14214
- GCC_except_table14215
- GCC_except_table14216
- GCC_except_table14217
- GCC_except_table14218
- GCC_except_table14220
- GCC_except_table14222
- GCC_except_table14224
- GCC_except_table14226
- GCC_except_table14361
- GCC_except_table14364
- GCC_except_table14384
- GCC_except_table14386
- GCC_except_table14387
- GCC_except_table3038
- GCC_except_table3043
- GCC_except_table3069
- GCC_except_table3072
- GCC_except_table3085
- GCC_except_table3117
- GCC_except_table3120
- GCC_except_table3146
- GCC_except_table3148
- GCC_except_table3150
- GCC_except_table3152
- GCC_except_table3299
- GCC_except_table3302
- GCC_except_table3310
- GCC_except_table3311
- GCC_except_table3332
- GCC_except_table3359
- GCC_except_table3360
- GCC_except_table3415
- GCC_except_table3425
- GCC_except_table3521
- GCC_except_table3573
- GCC_except_table3575
- GCC_except_table3578
- GCC_except_table3579
- GCC_except_table3607
- GCC_except_table3615
- GCC_except_table3617
- GCC_except_table3624
- GCC_except_table3625
- GCC_except_table3626
- GCC_except_table3628
- GCC_except_table3629
- GCC_except_table3630
- GCC_except_table3631
- GCC_except_table3632
- GCC_except_table3715
- GCC_except_table3738
- GCC_except_table3741
- GCC_except_table3744
- GCC_except_table3750
- GCC_except_table3753
- GCC_except_table3756
- GCC_except_table3821
- GCC_except_table3822
- GCC_except_table3868
- GCC_except_table3875
- GCC_except_table3876
- GCC_except_table3877
- GCC_except_table3880
- GCC_except_table3881
- GCC_except_table3882
- GCC_except_table3884
- GCC_except_table3892
- GCC_except_table3914
- GCC_except_table3923
- GCC_except_table3927
- GCC_except_table3930
- GCC_except_table3933
- GCC_except_table3974
- GCC_except_table3978
- GCC_except_table3982
- GCC_except_table3987
- GCC_except_table3995
- GCC_except_table3999
- GCC_except_table4008
- GCC_except_table4010
- GCC_except_table4249
- GCC_except_table4254
- GCC_except_table4258
- GCC_except_table4261
- GCC_except_table4266
- GCC_except_table4271
- GCC_except_table4277
- GCC_except_table4281
- GCC_except_table4285
- GCC_except_table4308
- GCC_except_table4310
- GCC_except_table4312
- GCC_except_table4315
- GCC_except_table4316
- GCC_except_table4318
- GCC_except_table4321
- GCC_except_table4396
- GCC_except_table4410
- GCC_except_table4413
- GCC_except_table4415
- GCC_except_table4418
- GCC_except_table4425
- GCC_except_table4479
- GCC_except_table4544
- GCC_except_table4559
- GCC_except_table4562
- GCC_except_table4654
- GCC_except_table4655
- GCC_except_table4659
- GCC_except_table4664
- GCC_except_table4668
- GCC_except_table4671
- GCC_except_table4673
- GCC_except_table4681
- GCC_except_table4927
- GCC_except_table4930
- GCC_except_table4942
- GCC_except_table5018
- GCC_except_table5062
- GCC_except_table5155
- GCC_except_table5406
- GCC_except_table5409
- GCC_except_table5500
- GCC_except_table5519
- GCC_except_table5529
- GCC_except_table5664
- GCC_except_table5675
- GCC_except_table5688
- GCC_except_table5695
- GCC_except_table5734
- GCC_except_table5736
- GCC_except_table5764
- GCC_except_table5766
- GCC_except_table5768
- GCC_except_table5770
- GCC_except_table5777
- GCC_except_table5783
- GCC_except_table5789
- GCC_except_table5799
- GCC_except_table5805
- GCC_except_table5882
- GCC_except_table5891
- GCC_except_table5893
- GCC_except_table5903
- GCC_except_table5905
- GCC_except_table5907
- GCC_except_table5909
- GCC_except_table5911
- GCC_except_table5917
- GCC_except_table5921
- GCC_except_table5934
- GCC_except_table5936
- GCC_except_table5938
- GCC_except_table5940
- GCC_except_table5959
- GCC_except_table5988
- GCC_except_table6037
- GCC_except_table6049
- GCC_except_table6051
- GCC_except_table6075
- GCC_except_table6076
- GCC_except_table6077
- GCC_except_table6078
- GCC_except_table6133
- GCC_except_table6146
- GCC_except_table6406
- GCC_except_table6408
- GCC_except_table6423
- GCC_except_table6461
- GCC_except_table6463
- GCC_except_table6481
- GCC_except_table6527
- GCC_except_table6622
- GCC_except_table6642
- GCC_except_table6643
- GCC_except_table6644
- GCC_except_table6646
- GCC_except_table6649
- GCC_except_table6650
- GCC_except_table6652
- GCC_except_table6978
- GCC_except_table6984
- GCC_except_table6986
- GCC_except_table6996
- GCC_except_table6997
- GCC_except_table7202
- GCC_except_table7206
- GCC_except_table7317
- GCC_except_table7321
- GCC_except_table7323
- GCC_except_table7324
- GCC_except_table7463
- GCC_except_table7472
- GCC_except_table7588
- GCC_except_table7643
- GCC_except_table7645
- GCC_except_table7647
- GCC_except_table7669
- GCC_except_table7697
- GCC_except_table7709
- GCC_except_table7726
- GCC_except_table7732
- GCC_except_table7743
- GCC_except_table7745
- GCC_except_table7747
- GCC_except_table7749
- GCC_except_table7751
- GCC_except_table7753
- GCC_except_table7755
- GCC_except_table7757
- GCC_except_table7759
- GCC_except_table7761
- GCC_except_table7763
- GCC_except_table7765
- GCC_except_table7767
- GCC_except_table7772
- GCC_except_table7786
- GCC_except_table7812
- GCC_except_table7814
- GCC_except_table7839
- GCC_except_table7852
- GCC_except_table7870
- GCC_except_table8049
- GCC_except_table8384
- GCC_except_table8427
- GCC_except_table8520
- GCC_except_table8529
- GCC_except_table8704
- GCC_except_table8706
- GCC_except_table8708
- GCC_except_table8710
- GCC_except_table8712
- GCC_except_table8714
- GCC_except_table8749
- GCC_except_table8752
- GCC_except_table8753
- GCC_except_table8756
- GCC_except_table8759
- GCC_except_table8803
- GCC_except_table8804
- GCC_except_table8805
- GCC_except_table8812
- GCC_except_table8813
- GCC_except_table8815
- GCC_except_table8834
- GCC_except_table9002
- GCC_except_table9007
- GCC_except_table9200
- GCC_except_table9248
- GCC_except_table9448
- GCC_except_table9450
- GCC_except_table9457
- GCC_except_table9465
- GCC_except_table9486
- GCC_except_table9497
- GCC_except_table9502
- GCC_except_table9505
- GCC_except_table9519
- GCC_except_table9524
- GCC_except_table9530
- GCC_except_table9535
- GCC_except_table9540
- GCC_except_table9545
- GCC_except_table9550
- GCC_except_table9554
- GCC_except_table9559
- GCC_except_table9606
- GCC_except_table9610
- GCC_except_table9620
- GCC_except_table9625
- GCC_except_table9639
- GCC_except_table9644
- GCC_except_table9651
- GCC_except_table9668
- GCC_except_table9669
- GCC_except_table9671
- GCC_except_table9673
- GCC_except_table9676
- GCC_except_table9681
- GCC_except_table9688
- GCC_except_table9693
- GCC_except_table9697
- GCC_except_table9732
- GCC_except_table9779
- GCC_except_table9788
- GCC_except_table9835
- GCC_except_table9836
- GCC_except_table9837
- GCC_except_table9875
- GCC_except_table9889
- GCC_except_table9957
- GCC_except_table9985
- GCC_except_table9986
- GCC_except_table9987
- GCC_except_table9989
- GCC_except_table9992
- GCC_except_table9993
- GCC_except_table9999
- __35-[HMAccessory updateAccessoryInfo:]_block_invoke
- __OBJC_$_CLASS_METHODS_HMHome(HomeKit|HomeKit1|HomeKit2|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- __OBJC_$_INSTANCE_METHODS_HMHome(HomeKit|HomeKit1|HomeKit2|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- __OBJC_CLASS_PROTOCOLS_$_HMHome(HomeKit|HomeKit1|HomeKit2|SwiftExtensions|AccessCode|WalletInternal|Wallet|Light|MediaGroupSettingsControllerFactory|ThreadResidentCommissioning|HMAccessory|HMRoom|HMZone|HMServiceGroup|HMUser|HMActionSet|HMTrigger|RemoteAccess|HMSoftwareUpdate|HMMediaProfile|NetworkRouter|HMUserActionPredictions|ThreadManagement|HMHomeHub|PowerAssertionInfo|HomeNetworkInfo|HomeLocationFeedback|MediaGroupReadinessCheck|HomeActivityState|ResidentSelection|HMModernMessaging|HMModernMessagingInternal|Trigger|Biome|Climate|SiriEndpointProfilesMessengerFactory|HMActionExecution|Person|Person_Internal|Matter|CHIP|AutomationBuilders)
- ___93-[HMHomeManager _pingDeviceWithUUID:monitor:secure:restrictToLocalNetwork:completionHandler:]_block_invoke
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
