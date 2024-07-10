## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices`

```diff

-3400.143.1.0.0
-  __TEXT.__text: 0x1ac5e0
+3400.149.2.0.0
+  __TEXT.__text: 0x1acd34
   __TEXT.__auth_stubs: 0x1260
-  __TEXT.__objc_methlist: 0x192b4
+  __TEXT.__objc_methlist: 0x1949c
   __TEXT.__const: 0x440
   __TEXT.__gcc_except_tab: 0x22ac
-  __TEXT.__cstring: 0x38428
-  __TEXT.__oslogstring: 0xf1fa
+  __TEXT.__cstring: 0x38513
+  __TEXT.__oslogstring: 0xf246
   __TEXT.__dlopen_cstrs: 0x222
-  __TEXT.__unwind_info: 0x7388
-  __TEXT.__objc_classname: 0x4d0b
-  __TEXT.__objc_methname: 0x38324
-  __TEXT.__objc_methtype: 0xa6a5
-  __TEXT.__objc_stubs: 0x22580
-  __DATA_CONST.__got: 0x15a0
-  __DATA_CONST.__const: 0x3c60
-  __DATA_CONST.__objc_classlist: 0xd68
+  __TEXT.__unwind_info: 0x73a0
+  __TEXT.__objc_classname: 0x4d2b
+  __TEXT.__objc_methname: 0x38a25
+  __TEXT.__objc_methtype: 0xa6df
+  __TEXT.__objc_stubs: 0x22680
+  __DATA_CONST.__got: 0x15a8
+  __DATA_CONST.__const: 0x3c48
+  __DATA_CONST.__objc_classlist: 0xd70
   __DATA_CONST.__objc_catlist: 0x290
   __DATA_CONST.__objc_protolist: 0x540
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb6d8
+  __DATA_CONST.__objc_selrefs: 0xb820
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0xd98
   __DATA_CONST.__objc_arraydata: 0x1ee0
   __AUTH_CONST.__auth_got: 0x940
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x7c30
-  __AUTH_CONST.__cfstring: 0x259c0
-  __AUTH_CONST.__objc_const: 0x38af0
+  __AUTH_CONST.__const: 0x7c50
+  __AUTH_CONST.__cfstring: 0x25a00
+  __AUTH_CONST.__objc_const: 0x38f80
   __AUTH_CONST.__objc_intobj: 0x22c8
   __AUTH_CONST.__objc_dictobj: 0xb68
   __AUTH_CONST.__objc_arrayobj: 0x5a0
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x2c60
+  __AUTH.__objc_data: 0x2cb0
   __AUTH.__data: 0x68
-  __DATA.__objc_ivar: 0x2458
+  __DATA.__objc_ivar: 0x24a8
   __DATA.__data: 0x4030
-  __DATA.__bss: 0xeb8
+  __DATA.__bss: 0xec0
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_data: 0x59b0
   __DATA_DIRTY.__data: 0xf0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11260
-  Symbols:   25338
-  CStrings:  6760
+  Functions: 11305
+  Symbols:   25418
+  CStrings:  6765
 
Symbols:
+ +[AFFeatureFlags(SWEFeatureFlags) isSiriCapellaEnabledForTVOS]
+ -[AFAWDSiriLinkRecommendationInfo beaconPER]
+ -[AFAWDSiriLinkRecommendationInfo btPreference]
+ -[AFAWDSiriLinkRecommendationInfo btRSSI]
+ -[AFAWDSiriLinkRecommendationInfo btRetransmissionRateRx]
+ -[AFAWDSiriLinkRecommendationInfo btRetransmissionRateTx]
+ -[AFAWDSiriLinkRecommendationInfo btTech]
+ -[AFAWDSiriLinkRecommendationInfo expectedThroughputVIBE]
+ -[AFAWDSiriLinkRecommendationInfo lsmRecommendationBe]
+ -[AFAWDSiriLinkRecommendationInfo nwType]
+ -[AFAWDSiriLinkRecommendationInfo packetLifetimeVIBE]
+ -[AFAWDSiriLinkRecommendationInfo packetLossRateVIBE]
+ -[AFAWDSiriLinkRecommendationInfo setBeaconPER:]
+ -[AFAWDSiriLinkRecommendationInfo setBtPreference:]
+ -[AFAWDSiriLinkRecommendationInfo setBtRSSI:]
+ -[AFAWDSiriLinkRecommendationInfo setBtRetransmissionRateRx:]
+ -[AFAWDSiriLinkRecommendationInfo setBtRetransmissionRateTx:]
+ -[AFAWDSiriLinkRecommendationInfo setBtTech:]
+ -[AFAWDSiriLinkRecommendationInfo setExpectedThroughputVIBE:]
+ -[AFAWDSiriLinkRecommendationInfo setLsmRecommendationBe:]
+ -[AFAWDSiriLinkRecommendationInfo setNwType:]
+ -[AFAWDSiriLinkRecommendationInfo setPacketLifetimeVIBE:]
+ -[AFAWDSiriLinkRecommendationInfo setPacketLossRateVIBE:]
+ -[AFAWDSiriLinkRecommendationInfo setTimeTaken:]
+ -[AFAWDSiriLinkRecommendationInfo setWifiCCA:]
+ -[AFAWDSiriLinkRecommendationInfo setWifiPreference:]
+ -[AFAWDSiriLinkRecommendationInfo setWifiRSSI:]
+ -[AFAWDSiriLinkRecommendationInfo setWifiSNR:]
+ -[AFAWDSiriLinkRecommendationInfo timeTaken]
+ -[AFAWDSiriLinkRecommendationInfo wifiCCA]
+ -[AFAWDSiriLinkRecommendationInfo wifiPreference]
+ -[AFAWDSiriLinkRecommendationInfo wifiRSSI]
+ -[AFAWDSiriLinkRecommendationInfo wifiSNR]
+ -[AFConversation _addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:asChildrenOfItemWithIdentifier:isSupplemental:isImmersiveExperience:isPersistentAcrossInvocations:]
+ -[AFConversation _addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:atIndexPaths:isSupplemental:isImmersiveExperience:isPersistentAcrossInvocations:]
+ -[AFConversationInsertion initWithConversationItemType:aceObject:aceCommandIdentifier:transient:supplemental:immersiveExperience:persistentAcrossInvocations:indexPath:]
+ -[AFConversationInsertion isPersistentAcrossInvocations]
+ -[AFConversationItem initWithIdentifier:revisionIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:persistentAcrossInvocations:associatedDataStore:]
+ -[AFConversationItem initWithType:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:persistentAcrossInvocations:associatedDataStore:]
+ -[AFConversationItem isPersistentAcrossInvocations]
+ -[AFModesConfiguration initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:]
+ -[AFModesConfiguration isAudioAccessoryButtonActivation]
+ -[AFMutableConversationItem initWithIdentifier:revisionIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:persistentAcrossInvocations:associatedDataStore:]
+ -[AFMutableConversationItem initWithIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:persistentAcrossInvocations:associatedDataStore:]
+ -[AFMutableConversationItem initWithType:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:persistentAcrossInvocations:associatedDataStore:]
+ -[AFMutableConversationItem isPersistentAcrossInvocations]
+ -[AFMutableConversationItem setPersistentAcrossInvocations:]
+ -[AFSettingsConnection areSiriSAEAssetsAvailable:]
+ -[_AFModesConfigurationMutation getIsAudioAccessoryButtonActivation]
+ -[_AFModesConfigurationMutation setIsAudioAccessoryButtonActivation:]
+ AFHasGMSCapabilityUnembargoed.deviceSupportsGenerativeModelSystems
+ AFHasGMSCapabilityUnembargoed.once
+ BluetoothManagerLibrary.44497
+ GCC_except_table1020
+ GCC_except_table10272
+ GCC_except_table10593
+ GCC_except_table10711
+ GCC_except_table10724
+ GCC_except_table10759
+ GCC_except_table1087
+ GCC_except_table1097
+ GCC_except_table10994
+ GCC_except_table11145
+ GCC_except_table11164
+ GCC_except_table11167
+ GCC_except_table11169
+ GCC_except_table1240
+ GCC_except_table1429
+ GCC_except_table1466
+ GCC_except_table1478
+ GCC_except_table1576
+ GCC_except_table1582
+ GCC_except_table1585
+ GCC_except_table1650
+ GCC_except_table1717
+ GCC_except_table2000
+ GCC_except_table2206
+ GCC_except_table2261
+ GCC_except_table2271
+ GCC_except_table2329
+ GCC_except_table2690
+ GCC_except_table2697
+ GCC_except_table2703
+ GCC_except_table2737
+ GCC_except_table2743
+ GCC_except_table2749
+ GCC_except_table2753
+ GCC_except_table2757
+ GCC_except_table2762
+ GCC_except_table2771
+ GCC_except_table2775
+ GCC_except_table2787
+ GCC_except_table2790
+ GCC_except_table2818
+ GCC_except_table2859
+ GCC_except_table2884
+ GCC_except_table2939
+ GCC_except_table2969
+ GCC_except_table3238
+ GCC_except_table3294
+ GCC_except_table3416
+ GCC_except_table3435
+ GCC_except_table3441
+ GCC_except_table3448
+ GCC_except_table3449
+ GCC_except_table3452
+ GCC_except_table3458
+ GCC_except_table3548
+ GCC_except_table3565
+ GCC_except_table3571
+ GCC_except_table3613
+ GCC_except_table3625
+ GCC_except_table3695
+ GCC_except_table3798
+ GCC_except_table3805
+ GCC_except_table3820
+ GCC_except_table3857
+ GCC_except_table3945
+ GCC_except_table3999
+ GCC_except_table4390
+ GCC_except_table4391
+ GCC_except_table4717
+ GCC_except_table4782
+ GCC_except_table4791
+ GCC_except_table4802
+ GCC_except_table4816
+ GCC_except_table4932
+ GCC_except_table5414
+ GCC_except_table5420
+ GCC_except_table5426
+ GCC_except_table5494
+ GCC_except_table5516
+ GCC_except_table5520
+ GCC_except_table5640
+ GCC_except_table5739
+ GCC_except_table5760
+ GCC_except_table5856
+ GCC_except_table5862
+ GCC_except_table5980
+ GCC_except_table5987
+ GCC_except_table6319
+ GCC_except_table6334
+ GCC_except_table6359
+ GCC_except_table6461
+ GCC_except_table6499
+ GCC_except_table7487
+ GCC_except_table7587
+ GCC_except_table7619
+ GCC_except_table7805
+ GCC_except_table7810
+ GCC_except_table7874
+ GCC_except_table7982
+ GCC_except_table8355
+ GCC_except_table8406
+ GCC_except_table8450
+ GCC_except_table8547
+ GCC_except_table8552
+ GCC_except_table8553
+ GCC_except_table8557
+ GCC_except_table8800
+ GCC_except_table8872
+ GCC_except_table8878
+ GCC_except_table8915
+ GCC_except_table8918
+ GCC_except_table8994
+ GCC_except_table9022
+ GCC_except_table9094
+ GCC_except_table9101
+ GCC_except_table9210
+ GCC_except_table9214
+ GCC_except_table9218
+ GCC_except_table9251
+ GCC_except_table9298
+ GCC_except_table9731
+ GCC_except_table9733
+ GCC_except_table9736
+ GCC_except_table9745
+ GCC_except_table9771
+ GCC_except_table9786
+ GCC_except_table9969
+ IntentsLibrary.14920
+ IntentsLibraryCore.frameworkLibrary.14930
+ IntentsLibraryCore.frameworkLibrary.30284
+ LSApplicationProxyFunction.33473
+ LSApplicationProxyFunction.44994
+ LaunchServicesLibrary.frameworkLibrary.44989
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._beaconPER
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btPreference
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btRSSI
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btRetransmissionRateRx
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btRetransmissionRateTx
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btTech
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._expectedThroughputVIBE
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._lsmRecommendationBe
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._nwType
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._packetLifetimeVIBE
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._packetLossRateVIBE
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._timeTaken
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._wifiCCA
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._wifiPreference
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._wifiRSSI
+ OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._wifiSNR
+ OBJC_IVAR_$_AFConversationInsertion._persistentAcrossInvocations
+ OBJC_IVAR_$_AFModesConfiguration._isAudioAccessoryButtonActivation
+ OBJC_IVAR_$_AFMutableConversationItem._persistentAcrossInvocations
+ OBJC_IVAR_$__AFModesConfigurationMutation._isAudioAccessoryButtonActivation
+ _AFAssetsAvailabilityMatchesRequiredAssets
+ _AFDeviceSupportsSiriCapella
+ _AFHasGMSCapabilityUnembargoed
+ _AFSAERequiredAssets
+ _AFUODStatusSupportedSAE
+ _DKEventQueryFunction.21137
+ _DKKnowledgeStoreFunction.21176
+ _DKQueryFunction.21151
+ _DKSystemEventStreamsFunction.21161
+ _OBJC_CLASS_$_AFAWDSiriLinkRecommendationInfo
+ _OBJC_CLASS_$_FLLogger
+ _OBJC_METACLASS_$_AFAWDSiriLinkRecommendationInfo
+ __43-[AFSettingsConnection dumpAssistantState:]_block_invoke.255
+ __50-[AFSettingsConnection areSiriSAEAssetsAvailable:]_block_invoke.254
+ __60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.567
+ __64-[AFMutableConversationItem initWithPropertyListRepresentation:]_block_invoke.123
+ __77-[AFSettingsConnection _createRadarWithReason:room:process:crash:completion:]_block_invoke.268
+ __99-[AFSettingsConnection(Internal) _updateMultiUserInfoForUser:score:companionInfo:reset:completion:]_block_invoke.566
+ __Block_byref_object_copy_.11883
+ __Block_byref_object_copy_.13149
+ __Block_byref_object_copy_.13394
+ __Block_byref_object_copy_.16772
+ __Block_byref_object_copy_.17218
+ __Block_byref_object_copy_.19473
+ __Block_byref_object_copy_.19936
+ __Block_byref_object_copy_.20955
+ __Block_byref_object_copy_.21950
+ __Block_byref_object_copy_.22605
+ __Block_byref_object_copy_.22993
+ __Block_byref_object_copy_.28200
+ __Block_byref_object_copy_.29866
+ __Block_byref_object_copy_.33884
+ __Block_byref_object_copy_.34335
+ __Block_byref_object_copy_.36541
+ __Block_byref_object_copy_.37722
+ __Block_byref_object_copy_.40850
+ __Block_byref_object_copy_.45043
+ __Block_byref_object_copy_.46207
+ __Block_byref_object_copy_.46937
+ __Block_byref_object_copy_.47217
+ __Block_byref_object_copy_.5441
+ __Block_byref_object_copy_.7890
+ __Block_byref_object_dispose_.11884
+ __Block_byref_object_dispose_.13150
+ __Block_byref_object_dispose_.13395
+ __Block_byref_object_dispose_.16773
+ __Block_byref_object_dispose_.17219
+ __Block_byref_object_dispose_.19474
+ __Block_byref_object_dispose_.19937
+ __Block_byref_object_dispose_.20956
+ __Block_byref_object_dispose_.21951
+ __Block_byref_object_dispose_.22606
+ __Block_byref_object_dispose_.22994
+ __Block_byref_object_dispose_.28201
+ __Block_byref_object_dispose_.29867
+ __Block_byref_object_dispose_.33885
+ __Block_byref_object_dispose_.34336
+ __Block_byref_object_dispose_.36542
+ __Block_byref_object_dispose_.37723
+ __Block_byref_object_dispose_.40851
+ __Block_byref_object_dispose_.45044
+ __Block_byref_object_dispose_.46208
+ __Block_byref_object_dispose_.46938
+ __Block_byref_object_dispose_.47218
+ __Block_byref_object_dispose_.5442
+ __Block_byref_object_dispose_.7891
+ __IntentsLibraryCore_block_invoke.14931
+ __IntentsLibraryCore_block_invoke.30285
+ __OBJC_$_INSTANCE_METHODS_AFAWDSiriLinkRecommendationInfo
+ __OBJC_$_INSTANCE_VARIABLES_AFAWDSiriLinkRecommendationInfo
+ __OBJC_$_PROP_LIST_AFAWDSiriLinkRecommendationInfo
+ __OBJC_CLASS_RO_$_AFAWDSiriLinkRecommendationInfo
+ __OBJC_METACLASS_RO_$_AFAWDSiriLinkRecommendationInfo
+ ___161-[AFConversation _addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:atIndexPaths:isSupplemental:isImmersiveExperience:isPersistentAcrossInvocations:]_block_invoke
+ ___50-[AFSettingsConnection areSiriSAEAssetsAvailable:]_block_invoke
+ ___588-[AFModesConfiguration initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:]_block_invoke
+ ___AFAssetsAvailabilityMatchesRequiredAssets_block_invoke
+ ___AFHasGMSCapabilityUnembargoed_block_invoke
+ ___block_descriptor_162_e8_32s_e40_v16?0"<AFModesConfigurationMutating>"8l
+ ___block_descriptor_59_e8_32s40s48s_e26_v32?0"SAAceView"8Q16^B24l
+ __block_literal_global.101.37836
+ __block_literal_global.104.22070
+ __block_literal_global.104.37830
+ __block_literal_global.108.21143
+ __block_literal_global.108.22064
+ __block_literal_global.112.21129
+ __block_literal_global.112.22059
+ __block_literal_global.116.22054
+ __block_literal_global.11906
+ __block_literal_global.120.22050
+ __block_literal_global.12175
+ __block_literal_global.12215
+ __block_literal_global.12720
+ __block_literal_global.128.22042
+ __block_literal_global.13539
+ __block_literal_global.136.22034
+ __block_literal_global.13745
+ __block_literal_global.13902
+ __block_literal_global.14221
+ __block_literal_global.14249
+ __block_literal_global.14359
+ __block_literal_global.144.22027
+ __block_literal_global.15778
+ __block_literal_global.16137
+ __block_literal_global.16418
+ __block_literal_global.16596
+ __block_literal_global.16815
+ __block_literal_global.172.44627
+ __block_literal_global.17211
+ __block_literal_global.177.44718
+ __block_literal_global.18232
+ __block_literal_global.18251
+ __block_literal_global.18593
+ __block_literal_global.18747
+ __block_literal_global.18787
+ __block_literal_global.18819
+ __block_literal_global.189.44727
+ __block_literal_global.19337
+ __block_literal_global.19414
+ __block_literal_global.19475
+ __block_literal_global.1993
+ __block_literal_global.19987
+ __block_literal_global.20.18738
+ __block_literal_global.201.44746
+ __block_literal_global.20242
+ __block_literal_global.20379
+ __block_literal_global.20446
+ __block_literal_global.20550
+ __block_literal_global.2059
+ __block_literal_global.20675
+ __block_literal_global.20705
+ __block_literal_global.21169
+ __block_literal_global.2141
+ __block_literal_global.22.45709
+ __block_literal_global.22126
+ __block_literal_global.23.44560
+ __block_literal_global.23045
+ __block_literal_global.23069
+ __block_literal_global.23152
+ __block_literal_global.23534
+ __block_literal_global.23711
+ __block_literal_global.245.44793
+ __block_literal_global.25065
+ __block_literal_global.25799
+ __block_literal_global.25826
+ __block_literal_global.25964
+ __block_literal_global.2600
+ __block_literal_global.26162
+ __block_literal_global.26333
+ __block_literal_global.26595
+ __block_literal_global.26760
+ __block_literal_global.27595
+ __block_literal_global.28156
+ __block_literal_global.28238
+ __block_literal_global.28333
+ __block_literal_global.28641
+ __block_literal_global.28704
+ __block_literal_global.2882
+ __block_literal_global.29349
+ __block_literal_global.29476
+ __block_literal_global.29577
+ __block_literal_global.29620
+ __block_literal_global.2977
+ __block_literal_global.30431
+ __block_literal_global.318.13400
+ __block_literal_global.32283
+ __block_literal_global.32799
+ __block_literal_global.3303
+ __block_literal_global.33466
+ __block_literal_global.3370
+ __block_literal_global.3395
+ __block_literal_global.34046
+ __block_literal_global.34177
+ __block_literal_global.34351
+ __block_literal_global.34427
+ __block_literal_global.36057
+ __block_literal_global.36562
+ __block_literal_global.37407
+ __block_literal_global.37434
+ __block_literal_global.37537
+ __block_literal_global.37604
+ __block_literal_global.37845
+ __block_literal_global.38.22120
+ __block_literal_global.38038
+ __block_literal_global.38500
+ __block_literal_global.38551
+ __block_literal_global.39497
+ __block_literal_global.39531
+ __block_literal_global.39806
+ __block_literal_global.40029
+ __block_literal_global.40447
+ __block_literal_global.40662
+ __block_literal_global.40879
+ __block_literal_global.40986
+ __block_literal_global.42.14644
+ __block_literal_global.42170
+ __block_literal_global.42228
+ __block_literal_global.42829
+ __block_literal_global.43.22112
+ __block_literal_global.43102
+ __block_literal_global.43194
+ __block_literal_global.44546
+ __block_literal_global.4528
+ __block_literal_global.45366
+ __block_literal_global.45392
+ __block_literal_global.45548
+ __block_literal_global.45699
+ __block_literal_global.46229
+ __block_literal_global.46893
+ __block_literal_global.4712
+ __block_literal_global.47238
+ __block_literal_global.49.47229
+ __block_literal_global.5.47223
+ __block_literal_global.51.26340
+ __block_literal_global.54.26341
+ __block_literal_global.557
+ __block_literal_global.559.45017
+ __block_literal_global.5592
+ __block_literal_global.561
+ __block_literal_global.563
+ __block_literal_global.5766
+ __block_literal_global.5829
+ __block_literal_global.60.34353
+ __block_literal_global.61.23527
+ __block_literal_global.67.22095
+ __block_literal_global.68.34358
+ __block_literal_global.6894
+ __block_literal_global.6965
+ __block_literal_global.70.34359
+ __block_literal_global.706
+ __block_literal_global.72.19465
+ __block_literal_global.72.22089
+ __block_literal_global.732
+ __block_literal_global.737
+ __block_literal_global.74.34360
+ __block_literal_global.75.19466
+ __block_literal_global.75.42287
+ __block_literal_global.78.42284
+ __block_literal_global.807
+ __block_literal_global.813
+ __block_literal_global.8181
+ __block_literal_global.820
+ __block_literal_global.8219
+ __block_literal_global.8244
+ __block_literal_global.825
+ __block_literal_global.832
+ __block_literal_global.8341
+ __block_literal_global.8393
+ __block_literal_global.84.22084
+ __block_literal_global.85.29538
+ __block_literal_global.85.34343
+ __block_literal_global.86.22081
+ __block_literal_global.92.37832
+ __block_literal_global.95.37842
+ __block_literal_global.98.37839
+ __getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.14937
+ __getINSendMessageIntentIdentifierSymbolLoc_block_invoke.14919
+ __initLSApplicationProxy_block_invoke.33470
+ __initLSApplicationProxy_block_invoke.44988
+ __init_DKEventQuery_block_invoke.21133
+ __init_DKKnowledgeStore_block_invoke.21173
+ __init_DKQuery_block_invoke.21147
+ __init_DKSystemEventStreams_block_invoke.21157
+ _objc_msgSend$_addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:asChildrenOfItemWithIdentifier:isSupplemental:isImmersiveExperience:isPersistentAcrossInvocations:
+ _objc_msgSend$_addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:atIndexPaths:isSupplemental:isImmersiveExperience:isPersistentAcrossInvocations:
+ _objc_msgSend$areSiriSAEAssetsAvailable:
+ _objc_msgSend$getIsAudioAccessoryButtonActivation
+ _objc_msgSend$initWithConversationItemType:aceObject:aceCommandIdentifier:transient:supplemental:immersiveExperience:persistentAcrossInvocations:indexPath:
+ _objc_msgSend$initWithIdentifier:revisionIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:persistentAcrossInvocations:associatedDataStore:
+ _objc_msgSend$initWithIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:persistentAcrossInvocations:associatedDataStore:
+ _objc_msgSend$initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:
+ _objc_msgSend$initWithType:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:persistentAcrossInvocations:associatedDataStore:
+ _objc_msgSend$isAudioAccessoryButtonActivation
+ _objc_msgSend$isPersistentAcrossInvocations
+ _objc_msgSend$persistentAcrossInvocations
+ _objc_msgSend$setIsAudioAccessoryButtonActivation:
+ _objc_msgSend$setPersistentAcrossInvocations:
+ _objc_msgSend$setValue:forUploadHeaderNamed:
+ _objc_msgSend$sharedLogger
+ audit_stringIntents.14934
+ audit_stringIntents.30299
+ classLSApplicationProxy.33467
+ classLSApplicationProxy.44986
+ class_DKEventQuery.21130
+ class_DKKnowledgeStore.21170
+ class_DKQuery.21144
+ class_DKSystemEventStreams.21155
+ getINSearchForMessagesIntentIdentifier.14917
+ getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.14936
+ getINSendMessageIntentIdentifierSymbolLoc.ptr.14918
+ getLSApplicationProxyClass.33459
+ getLSApplicationProxyClass.44982
+ get_DKEventQueryClass.21104
+ get_DKKnowledgeStoreClass.21164
+ get_DKQueryClass.21101
+ get_DKSystemEventStreamsClass.21099
+ initLSApplicationProxy.33464
+ initLSApplicationProxy.44984
+ initLSApplicationProxy.sOnce.33465
+ initLSApplicationProxy.sOnce.44985
+ init_DKEventQuery.21127
+ init_DKEventQuery.sOnce.21128
+ init_DKKnowledgeStore.21167
+ init_DKKnowledgeStore.sOnce.21168
+ init_DKQuery.21141
+ init_DKQuery.sOnce.21142
+ init_DKSystemEventStreams.21153
+ init_DKSystemEventStreams.sOnce.21154
+ provider.onceToken.14939
+ provider.provider.14940
+ sharedInstance.onceToken.16814
+ sharedInstance.onceToken.22161
+ sharedInstance.onceToken.23044
+ sharedInstance.onceToken.43299
+ sharedInstance.singleton.43300
+ sharedManager.onceToken.21654
+ sharedManager.onceToken.42169
+ sharedManager.sharedManager.42171
+ sharedMonitor.onceToken.20007
+ sharedObserver.onceToken.30430
+ sharedObserver.onceToken.44505
+ sharedObserver.onceToken.47237
+ sharedObserver.sharedObserver.30432
+ sharedObserver.sharedObserver.47239
- -[AFConversation _addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:asChildrenOfItemWithIdentifier:isSupplemental:isImmersiveExperience:]
- -[AFConversation _addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:atIndexPaths:isSupplemental:isImmersiveExperience:]
- -[AFConversationInsertion initWithConversationItemType:aceObject:aceCommandIdentifier:transient:supplemental:immersiveExperience:indexPath:]
- -[AFConversationItem initWithIdentifier:revisionIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:associatedDataStore:]
- -[AFConversationItem initWithType:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:associatedDataStore:]
- -[AFModesConfiguration initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:]
- -[AFMutableConversationItem initWithIdentifier:revisionIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:associatedDataStore:]
- -[AFMutableConversationItem initWithIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:associatedDataStore:]
- -[AFMutableConversationItem initWithType:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:associatedDataStore:]
- -[AFSettingsConnection JSCapableHomeDevices:]
- BluetoothManagerLibrary.44368
- GCC_except_table1018
- GCC_except_table10233
- GCC_except_table10554
- GCC_except_table10670
- GCC_except_table10683
- GCC_except_table10716
- GCC_except_table1085
- GCC_except_table10949
- GCC_except_table1095
- GCC_except_table11100
- GCC_except_table11119
- GCC_except_table11122
- GCC_except_table11124
- GCC_except_table1236
- GCC_except_table1427
- GCC_except_table1464
- GCC_except_table1476
- GCC_except_table1574
- GCC_except_table1580
- GCC_except_table1583
- GCC_except_table1648
- GCC_except_table1715
- GCC_except_table1998
- GCC_except_table2204
- GCC_except_table2259
- GCC_except_table2269
- GCC_except_table2327
- GCC_except_table2688
- GCC_except_table2695
- GCC_except_table2699
- GCC_except_table2733
- GCC_except_table2741
- GCC_except_table2747
- GCC_except_table2751
- GCC_except_table2755
- GCC_except_table2758
- GCC_except_table2767
- GCC_except_table2773
- GCC_except_table2785
- GCC_except_table2788
- GCC_except_table2810
- GCC_except_table2857
- GCC_except_table2882
- GCC_except_table2937
- GCC_except_table2967
- GCC_except_table3236
- GCC_except_table3292
- GCC_except_table3414
- GCC_except_table3433
- GCC_except_table3439
- GCC_except_table3446
- GCC_except_table3447
- GCC_except_table3450
- GCC_except_table3456
- GCC_except_table3544
- GCC_except_table3563
- GCC_except_table3569
- GCC_except_table3611
- GCC_except_table3623
- GCC_except_table3693
- GCC_except_table3796
- GCC_except_table3803
- GCC_except_table3818
- GCC_except_table3855
- GCC_except_table3943
- GCC_except_table3997
- GCC_except_table4387
- GCC_except_table4388
- GCC_except_table4714
- GCC_except_table4779
- GCC_except_table4788
- GCC_except_table4799
- GCC_except_table4813
- GCC_except_table4929
- GCC_except_table5379
- GCC_except_table5385
- GCC_except_table5391
- GCC_except_table5459
- GCC_except_table5481
- GCC_except_table5485
- GCC_except_table5605
- GCC_except_table5704
- GCC_except_table5725
- GCC_except_table5821
- GCC_except_table5827
- GCC_except_table5942
- GCC_except_table5949
- GCC_except_table6284
- GCC_except_table6299
- GCC_except_table6324
- GCC_except_table6426
- GCC_except_table6464
- GCC_except_table7449
- GCC_except_table7549
- GCC_except_table7581
- GCC_except_table7767
- GCC_except_table7772
- GCC_except_table7836
- GCC_except_table7944
- GCC_except_table8317
- GCC_except_table8368
- GCC_except_table8412
- GCC_except_table8509
- GCC_except_table8514
- GCC_except_table8515
- GCC_except_table8519
- GCC_except_table8762
- GCC_except_table8834
- GCC_except_table8840
- GCC_except_table8877
- GCC_except_table8880
- GCC_except_table8956
- GCC_except_table8984
- GCC_except_table9056
- GCC_except_table9063
- GCC_except_table9172
- GCC_except_table9176
- GCC_except_table9180
- GCC_except_table9213
- GCC_except_table9260
- GCC_except_table9692
- GCC_except_table9694
- GCC_except_table9697
- GCC_except_table9706
- GCC_except_table9732
- GCC_except_table9747
- GCC_except_table9930
- IntentsLibrary.14914
- IntentsLibraryCore.frameworkLibrary.14924
- IntentsLibraryCore.frameworkLibrary.30152
- LSApplicationProxyFunction.33344
- LSApplicationProxyFunction.44866
- LaunchServicesLibrary.frameworkLibrary.44859
- _AFUODStatusMatchesRequiredAssets
- _DKEventQueryFunction.21024
- _DKKnowledgeStoreFunction.21063
- _DKQueryFunction.21038
- _DKSystemEventStreamsFunction.21048
- __43-[AFSettingsConnection dumpAssistantState:]_block_invoke.254
- __60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.566
- __64-[AFMutableConversationItem initWithPropertyListRepresentation:]_block_invoke.120
- __77-[AFSettingsConnection _createRadarWithReason:room:process:crash:completion:]_block_invoke.267
- __99-[AFSettingsConnection(Internal) _updateMultiUserInfoForUser:score:companionInfo:reset:completion:]_block_invoke.565
- __Block_byref_object_copy_.11882
- __Block_byref_object_copy_.13146
- __Block_byref_object_copy_.13392
- __Block_byref_object_copy_.16766
- __Block_byref_object_copy_.17212
- __Block_byref_object_copy_.19361
- __Block_byref_object_copy_.19823
- __Block_byref_object_copy_.20842
- __Block_byref_object_copy_.21828
- __Block_byref_object_copy_.22484
- __Block_byref_object_copy_.22872
- __Block_byref_object_copy_.28066
- __Block_byref_object_copy_.29733
- __Block_byref_object_copy_.33755
- __Block_byref_object_copy_.34206
- __Block_byref_object_copy_.36414
- __Block_byref_object_copy_.37594
- __Block_byref_object_copy_.40721
- __Block_byref_object_copy_.44911
- __Block_byref_object_copy_.46066
- __Block_byref_object_copy_.46796
- __Block_byref_object_copy_.47076
- __Block_byref_object_copy_.5448
- __Block_byref_object_copy_.7896
- __Block_byref_object_dispose_.11883
- __Block_byref_object_dispose_.13147
- __Block_byref_object_dispose_.13393
- __Block_byref_object_dispose_.16767
- __Block_byref_object_dispose_.17213
- __Block_byref_object_dispose_.19362
- __Block_byref_object_dispose_.19824
- __Block_byref_object_dispose_.20843
- __Block_byref_object_dispose_.21829
- __Block_byref_object_dispose_.22485
- __Block_byref_object_dispose_.22873
- __Block_byref_object_dispose_.28067
- __Block_byref_object_dispose_.29734
- __Block_byref_object_dispose_.33756
- __Block_byref_object_dispose_.34207
- __Block_byref_object_dispose_.36415
- __Block_byref_object_dispose_.37595
- __Block_byref_object_dispose_.40722
- __Block_byref_object_dispose_.44912
- __Block_byref_object_dispose_.46067
- __Block_byref_object_dispose_.46797
- __Block_byref_object_dispose_.47077
- __Block_byref_object_dispose_.5449
- __Block_byref_object_dispose_.7897
- __IntentsLibraryCore_block_invoke.14925
- __IntentsLibraryCore_block_invoke.30153
- ___131-[AFConversation _addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:atIndexPaths:isSupplemental:isImmersiveExperience:]_block_invoke
- ___45-[AFSettingsConnection JSCapableHomeDevices:]_block_invoke
- ___45-[AFSettingsConnection JSCapableHomeDevices:]_block_invoke_2
- ___555-[AFModesConfiguration initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:]_block_invoke
- ___AFUODStatusMatchesRequiredAssets_block_invoke
- ___block_descriptor_161_e8_32s_e40_v16?0"<AFModesConfigurationMutating>"8l
- ___block_descriptor_58_e8_32s40s48s_e26_v32?0"SAAceView"8Q16^B24l
- __block_literal_global.101.37708
- __block_literal_global.104.21949
- __block_literal_global.104.37702
- __block_literal_global.108.21030
- __block_literal_global.108.21943
- __block_literal_global.112.21016
- __block_literal_global.112.21938
- __block_literal_global.116.21933
- __block_literal_global.11905
- __block_literal_global.120.21929
- __block_literal_global.12174
- __block_literal_global.12214
- __block_literal_global.12718
- __block_literal_global.128.21921
- __block_literal_global.13535
- __block_literal_global.136.21913
- __block_literal_global.13741
- __block_literal_global.13898
- __block_literal_global.14218
- __block_literal_global.14246
- __block_literal_global.14356
- __block_literal_global.144.21906
- __block_literal_global.15772
- __block_literal_global.16131
- __block_literal_global.16412
- __block_literal_global.16590
- __block_literal_global.16809
- __block_literal_global.172.44492
- __block_literal_global.17205
- __block_literal_global.177.44583
- __block_literal_global.18226
- __block_literal_global.18245
- __block_literal_global.18587
- __block_literal_global.18741
- __block_literal_global.18781
- __block_literal_global.18813
- __block_literal_global.189.44592
- __block_literal_global.19225
- __block_literal_global.19302
- __block_literal_global.19363
- __block_literal_global.19874
- __block_literal_global.1995
- __block_literal_global.20.18732
- __block_literal_global.201.44611
- __block_literal_global.20129
- __block_literal_global.20266
- __block_literal_global.20333
- __block_literal_global.20437
- __block_literal_global.20562
- __block_literal_global.20592
- __block_literal_global.2061
- __block_literal_global.21056
- __block_literal_global.2143
- __block_literal_global.22.45568
- __block_literal_global.22005
- __block_literal_global.22924
- __block_literal_global.22948
- __block_literal_global.23.44425
- __block_literal_global.23031
- __block_literal_global.23413
- __block_literal_global.23590
- __block_literal_global.245.44658
- __block_literal_global.24931
- __block_literal_global.25666
- __block_literal_global.25693
- __block_literal_global.25831
- __block_literal_global.26029
- __block_literal_global.2604
- __block_literal_global.26200
- __block_literal_global.26462
- __block_literal_global.26627
- __block_literal_global.27461
- __block_literal_global.28022
- __block_literal_global.28104
- __block_literal_global.28199
- __block_literal_global.28507
- __block_literal_global.28570
- __block_literal_global.2886
- __block_literal_global.29215
- __block_literal_global.29342
- __block_literal_global.29443
- __block_literal_global.29486
- __block_literal_global.2981
- __block_literal_global.30299
- __block_literal_global.318.13398
- __block_literal_global.32155
- __block_literal_global.32669
- __block_literal_global.3305
- __block_literal_global.33337
- __block_literal_global.3372
- __block_literal_global.33917
- __block_literal_global.3397
- __block_literal_global.34048
- __block_literal_global.34222
- __block_literal_global.34298
- __block_literal_global.35928
- __block_literal_global.36435
- __block_literal_global.37279
- __block_literal_global.37306
- __block_literal_global.37409
- __block_literal_global.37476
- __block_literal_global.37717
- __block_literal_global.37910
- __block_literal_global.38.21999
- __block_literal_global.38372
- __block_literal_global.38423
- __block_literal_global.39368
- __block_literal_global.39402
- __block_literal_global.39677
- __block_literal_global.39900
- __block_literal_global.40318
- __block_literal_global.40533
- __block_literal_global.40750
- __block_literal_global.40857
- __block_literal_global.42.14638
- __block_literal_global.42041
- __block_literal_global.42099
- __block_literal_global.42700
- __block_literal_global.42973
- __block_literal_global.43.21991
- __block_literal_global.43065
- __block_literal_global.44411
- __block_literal_global.45225
- __block_literal_global.45251
- __block_literal_global.4530
- __block_literal_global.45407
- __block_literal_global.45558
- __block_literal_global.46088
- __block_literal_global.46752
- __block_literal_global.47097
- __block_literal_global.4714
- __block_literal_global.49.47088
- __block_literal_global.5.47082
- __block_literal_global.51.26207
- __block_literal_global.54.26208
- __block_literal_global.556
- __block_literal_global.558
- __block_literal_global.5599
- __block_literal_global.560
- __block_literal_global.562
- __block_literal_global.5773
- __block_literal_global.5836
- __block_literal_global.60.34224
- __block_literal_global.61.23406
- __block_literal_global.67.21974
- __block_literal_global.68.34229
- __block_literal_global.6900
- __block_literal_global.6971
- __block_literal_global.70.34230
- __block_literal_global.72.19353
- __block_literal_global.72.21968
- __block_literal_global.733
- __block_literal_global.74.34231
- __block_literal_global.741
- __block_literal_global.75.19354
- __block_literal_global.75.42158
- __block_literal_global.78.42155
- __block_literal_global.811
- __block_literal_global.817
- __block_literal_global.8185
- __block_literal_global.8223
- __block_literal_global.824
- __block_literal_global.8248
- __block_literal_global.833
- __block_literal_global.8345
- __block_literal_global.836
- __block_literal_global.8397
- __block_literal_global.84.21963
- __block_literal_global.85.29404
- __block_literal_global.85.34214
- __block_literal_global.86.21960
- __block_literal_global.92.37704
- __block_literal_global.95.37714
- __block_literal_global.98.37711
- __getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.14931
- __getINSendMessageIntentIdentifierSymbolLoc_block_invoke.14913
- __initLSApplicationProxy_block_invoke.33341
- __initLSApplicationProxy_block_invoke.44858
- __init_DKEventQuery_block_invoke.21020
- __init_DKKnowledgeStore_block_invoke.21060
- __init_DKQuery_block_invoke.21034
- __init_DKSystemEventStreams_block_invoke.21044
- _kBypassDeviceSupportsAssistantEngineDefaultsDomain
- _kBypassDeviceSupportsAssistantEnginePreferenceKey
- _kBypassDeviceSupportsSAEDefaultsDomain
- _kBypassDeviceSupportsSAEPreferenceKey
- _objc_msgSend$JSCapableHomeDevices:
- _objc_msgSend$_addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:asChildrenOfItemWithIdentifier:isSupplemental:isImmersiveExperience:
- _objc_msgSend$_addItemsForAceViews:withDialogPhase:fromCommandWithIdentifier:atIndexPaths:isSupplemental:isImmersiveExperience:
- _objc_msgSend$initWithConversationItemType:aceObject:aceCommandIdentifier:transient:supplemental:immersiveExperience:indexPath:
- _objc_msgSend$initWithIdentifier:revisionIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:associatedDataStore:
- _objc_msgSend$initWithIdentifier:type:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:associatedDataStore:
- _objc_msgSend$initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:
- _objc_msgSend$initWithType:aceObject:dialogPhase:presentationState:aceCommandIdentifier:virgin:transient:supplemental:immersiveExperience:associatedDataStore:
- audit_stringIntents.14928
- audit_stringIntents.30167
- classLSApplicationProxy.33338
- classLSApplicationProxy.44856
- class_DKEventQuery.21017
- class_DKKnowledgeStore.21057
- class_DKQuery.21031
- class_DKSystemEventStreams.21042
- getINSearchForMessagesIntentIdentifier.14911
- getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.14930
- getINSendMessageIntentIdentifierSymbolLoc.ptr.14912
- getLSApplicationProxyClass.33330
- getLSApplicationProxyClass.44852
- get_DKEventQueryClass.20991
- get_DKKnowledgeStoreClass.21051
- get_DKQueryClass.20988
- get_DKSystemEventStreamsClass.20986
- initLSApplicationProxy.33335
- initLSApplicationProxy.44854
- initLSApplicationProxy.sOnce.33336
- initLSApplicationProxy.sOnce.44855
- init_DKEventQuery.21014
- init_DKEventQuery.sOnce.21015
- init_DKKnowledgeStore.21054
- init_DKKnowledgeStore.sOnce.21055
- init_DKQuery.21028
- init_DKQuery.sOnce.21029
- init_DKSystemEventStreams.21040
- init_DKSystemEventStreams.sOnce.21041
- provider.onceToken.14933
- provider.provider.14934
- sharedInstance.onceToken.16808
- sharedInstance.onceToken.22038
- sharedInstance.onceToken.22923
- sharedInstance.onceToken.43170
- sharedInstance.singleton.43171
- sharedManager.onceToken.21541
- sharedManager.onceToken.42040
- sharedManager.sharedManager.42042
- sharedMonitor.onceToken.19894
- sharedObserver.onceToken.30298
- sharedObserver.onceToken.44373
- sharedObserver.onceToken.47096
- sharedObserver.sharedObserver.30300
- sharedObserver.sharedObserver.47098
CStrings:
+ "%!@(MISSING) {isEyesFree = %!@(MISSING), isUIFree = %!@(MISSING), isForCarDND = %!@(MISSING), isInAmbient = %!@(MISSING), isMapsNavigationActive = %!@(MISSING), isVoiceTriggerRequest = %!@(MISSING), isConnectedToCarPlay = %!@(MISSING), isRequestMadeWithPhysicalDeviceInteraction = %!@(MISSING), isAudioAccessoryButtonActivation = %!@(MISSING), isSiriAutoPrompt = %!@(MISSING), isFlexibleFollowup = %!@(MISSING), isMediaPlaying = %!@(MISSING), userTypedInSiri = %!@(MISSING), modeOverrideValue = %!@(MISSING), isDeviceUnlocked = %!@(MISSING), isDeviceScreenON = %!@(MISSING), isInPocket = %!@(MISSING), liftToWakeDetected = %!@(MISSING), userInitiatedWakeDetected = %!@(MISSING), deviceMotion = %!@(MISSING), deviceRaised = %!@(MISSING), faceDetected = %!@(MISSING), touchScreenDetected = %!@(MISSING), buttonPressDetected = %!@(MISSING), flatDevicePosture = %!@(MISSING), deviceOrientation = %!@(MISSING), isInWorkout = %!@(MISSING), isBacklightOn = %!@(MISSING), isInWaterLock = %!@(MISSING), isInSleepLock = %!@(MISSING), isInTheaterMode = %!@(MISSING), isOnWrist = %!@(MISSING)}"
+ "-[AFSettingsConnection areSiriSAEAssetsAvailable:]_block_invoke"
+ "<ConversationItem %!p(MISSING); %!@(MISSING) (revision %!@(MISSING)): type=%!@(MISSING), aceObject=%!@(MISSING), dialogPhase=%!@(MISSING), presentationState=%!@(MISSING), aceCommandIdentifier=%!@(MISSING)%!@(MISSING)%!@(MISSING), transient=%!@(MISSING), supplemental=%!@(MISSING), immersiveExperience=%!@(MISSING), persistentAcrossInvocations=%!@(MISSING)>"
+ "A2DP"
+ "AFHasGMSCapability"
+ "AFHasGMSCapabilityUnembargoed"
+ "AFModesConfiguration::isAudioAccessoryButtonActivation"
+ "PersistentAcrossInvocations"
+ "isAudioAccessoryButtonActivation"
+ "preferredOutputRoute_v2"
+ "siri_capella_enabled_for_tvos"
+ "userId"
- "%!@(MISSING) {isEyesFree = %!@(MISSING), isUIFree = %!@(MISSING), isForCarDND = %!@(MISSING), isInAmbient = %!@(MISSING), isMapsNavigationActive = %!@(MISSING), isVoiceTriggerRequest = %!@(MISSING), isConnectedToCarPlay = %!@(MISSING), isRequestMadeWithPhysicalDeviceInteraction = %!@(MISSING), isSiriAutoPrompt = %!@(MISSING), isFlexibleFollowup = %!@(MISSING), isMediaPlaying = %!@(MISSING), userTypedInSiri = %!@(MISSING), modeOverrideValue = %!@(MISSING), isDeviceUnlocked = %!@(MISSING), isDeviceScreenON = %!@(MISSING), isInPocket = %!@(MISSING), liftToWakeDetected = %!@(MISSING), userInitiatedWakeDetected = %!@(MISSING), deviceMotion = %!@(MISSING), deviceRaised = %!@(MISSING), faceDetected = %!@(MISSING), touchScreenDetected = %!@(MISSING), buttonPressDetected = %!@(MISSING), flatDevicePosture = %!@(MISSING), deviceOrientation = %!@(MISSING), isInWorkout = %!@(MISSING), isBacklightOn = %!@(MISSING), isInWaterLock = %!@(MISSING), isInSleepLock = %!@(MISSING), isInTheaterMode = %!@(MISSING), isOnWrist = %!@(MISSING)}"
- "-[AFSettingsConnection JSCapableHomeDevices:]"
- "<ConversationItem %!p(MISSING); %!@(MISSING) (revision %!@(MISSING)): type=%!@(MISSING), aceObject=%!@(MISSING), dialogPhase=%!@(MISSING), presentationState=%!@(MISSING), aceCommandIdentifier=%!@(MISSING)%!@(MISSING)%!@(MISSING), transient=%!@(MISSING), supplemental=%!@(MISSING), immersiveExperience=%!@(MISSING)>"
- "HFP"
- "bypassDeviceSupportsAssistantEngine"
- "bypassDeviceSupportsSAE"
- "preferredOutputRoute"

```
