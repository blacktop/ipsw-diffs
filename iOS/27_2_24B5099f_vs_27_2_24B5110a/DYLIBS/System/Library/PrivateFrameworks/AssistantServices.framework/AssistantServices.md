## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3605.30.1.1.1
-  __TEXT.__text: 0x197988
-  __TEXT.__objc_methlist: 0x1f404
+3605.31.1.11.2
+  __TEXT.__text: 0x198898
+  __TEXT.__objc_methlist: 0x1f544
   __TEXT.__const: 0x3d0
   __TEXT.__dlopen_cstrs: 0x538
   __TEXT.__gcc_except_tab: 0x21e0
-  __TEXT.__cstring: 0x3dc51
-  __TEXT.__oslogstring: 0xfbb3
+  __TEXT.__cstring: 0x3ded9
+  __TEXT.__oslogstring: 0xfd05
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x9fd8
+  __TEXT.__unwind_info: 0xa020
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x8788
+  __DATA_CONST.__const: 0x87c0
   __DATA_CONST.__objc_classlist: 0xf00
   __DATA_CONST.__objc_catlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0x608
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc280
+  __DATA_CONST.__objc_selrefs: 0xc320
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0xf18
   __DATA_CONST.__objc_arraydata: 0x2450
   __DATA_CONST.__got: 0x1700
-  __AUTH_CONST.__const: 0x3dc0
-  __AUTH_CONST.__cfstring: 0x28860
-  __AUTH_CONST.__objc_const: 0x36758
+  __AUTH_CONST.__const: 0x3e00
+  __AUTH_CONST.__cfstring: 0x28a40
+  __AUTH_CONST.__objc_const: 0x368c8
   __AUTH_CONST.__objc_intobj: 0x2730
   __AUTH_CONST.__objc_dictobj: 0xd20
   __AUTH_CONST.__objc_arrayobj: 0x5d0

   __AUTH_CONST.__auth_got: 0xae0
   __AUTH.__objc_data: 0x84f8
   __AUTH.__data: 0x280
-  __DATA.__objc_ivar: 0x25ac
+  __DATA.__objc_ivar: 0x25c8
   __DATA.__data: 0x4988
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1108

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12227
-  Symbols:   22414
-  CStrings:  8694
+  Functions: 12257
+  Symbols:   22458
+  CStrings:  8715
 
Symbols:
+ -[AFCompanionDeviceInfo ifpCapableDevice]
+ -[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:ifpCapableDevice:siriAvailability:]
+ -[AFCompanionDeviceInfo linwoodCapableDevice]
+ -[AFCompanionDeviceInfo siriAvailability]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:ifpCapableDevice:]
+ -[AFCompanionDeviceInfo(SiriAvailability) createSiriAvailability]
+ -[AFPreferences _setLinwoodEnabledMeDevice:]
+ -[AFPreferences linwoodEnabledMeDevice]
+ -[AFSettingsConnection isLinwoodEnabledOnAnyHomeDevice:]
+ -[AFSiriAvailability createDictionaryExcludingBootSession]
+ -[AFSiriAvailability isLinwoodAccessRestricted]
+ -[AFSiriAvailability isLinwoodGMSAvailable]
+ -[AFSiriAvailability isLinwoodGMSEnabled]
+ -[AFSpeechRequestOptions isReplyToSiriPrompt]
+ -[AFSpeechRequestOptions setIsReplyToSiriPrompt:]
+ -[_AFCompanionDeviceInfoMutation getIfpCapableDevice]
+ -[_AFCompanionDeviceInfoMutation getLinwoodCapableDevice]
+ -[_AFCompanionDeviceInfoMutation getSiriAvailability]
+ -[_AFCompanionDeviceInfoMutation setIfpCapableDevice:]
+ -[_AFCompanionDeviceInfoMutation setLinwoodCapableDevice:]
+ -[_AFCompanionDeviceInfoMutation setSiriAvailability:]
+ GCC_except_table10058
+ GCC_except_table10266
+ GCC_except_table10306
+ GCC_except_table10337
+ GCC_except_table10342
+ GCC_except_table10343
+ GCC_except_table10347
+ GCC_except_table10536
+ GCC_except_table10707
+ GCC_except_table10736
+ GCC_except_table10833
+ GCC_except_table10837
+ GCC_except_table10841
+ GCC_except_table10870
+ GCC_except_table11224
+ GCC_except_table11226
+ GCC_except_table11229
+ GCC_except_table11238
+ GCC_except_table11304
+ GCC_except_table11325
+ GCC_except_table11350
+ GCC_except_table11356
+ GCC_except_table11515
+ GCC_except_table11519
+ GCC_except_table11521
+ GCC_except_table11524
+ GCC_except_table11530
+ GCC_except_table11534
+ GCC_except_table11540
+ GCC_except_table11747
+ GCC_except_table12071
+ GCC_except_table12205
+ GCC_except_table12208
+ GCC_except_table12210
+ GCC_except_table2725
+ GCC_except_table2738
+ GCC_except_table2742
+ GCC_except_table2754
+ GCC_except_table2758
+ GCC_except_table2871
+ GCC_except_table2873
+ GCC_except_table2951
+ GCC_except_table2995
+ GCC_except_table3361
+ GCC_except_table3368
+ GCC_except_table3374
+ GCC_except_table3376
+ GCC_except_table3378
+ GCC_except_table3423
+ GCC_except_table3425
+ GCC_except_table3431
+ GCC_except_table3437
+ GCC_except_table3441
+ GCC_except_table3447
+ GCC_except_table3454
+ GCC_except_table3456
+ GCC_except_table3461
+ GCC_except_table3463
+ GCC_except_table3468
+ GCC_except_table3480
+ GCC_except_table3483
+ GCC_except_table3497
+ GCC_except_table3499
+ GCC_except_table3501
+ GCC_except_table3503
+ GCC_except_table3505
+ GCC_except_table3555
+ GCC_except_table3581
+ GCC_except_table3638
+ GCC_except_table3674
+ GCC_except_table4079
+ GCC_except_table4368
+ GCC_except_table4569
+ GCC_except_table4577
+ GCC_except_table4635
+ GCC_except_table5011
+ GCC_except_table5015
+ GCC_except_table5060
+ GCC_except_table5066
+ GCC_except_table5091
+ GCC_except_table5097
+ GCC_except_table5312
+ GCC_except_table5421
+ GCC_except_table5432
+ GCC_except_table5465
+ GCC_except_table5468
+ GCC_except_table5545
+ GCC_except_table5549
+ GCC_except_table5559
+ GCC_except_table5570
+ GCC_except_table5583
+ GCC_except_table5668
+ GCC_except_table5670
+ GCC_except_table5694
+ GCC_except_table5810
+ GCC_except_table5873
+ GCC_except_table5876
+ GCC_except_table5880
+ GCC_except_table5897
+ GCC_except_table5911
+ GCC_except_table5985
+ GCC_except_table6043
+ GCC_except_table6069
+ GCC_except_table6348
+ GCC_except_table6494
+ GCC_except_table6507
+ GCC_except_table6552
+ GCC_except_table6646
+ GCC_except_table6831
+ GCC_except_table6917
+ GCC_except_table6971
+ GCC_except_table7207
+ GCC_except_table7210
+ GCC_except_table7211
+ GCC_except_table7408
+ GCC_except_table7467
+ GCC_except_table7681
+ GCC_except_table7684
+ GCC_except_table7696
+ GCC_except_table7697
+ GCC_except_table7710
+ GCC_except_table7711
+ GCC_except_table7712
+ GCC_except_table7756
+ GCC_except_table7762
+ GCC_except_table7768
+ GCC_except_table7836
+ GCC_except_table7873
+ GCC_except_table7876
+ GCC_except_table7987
+ GCC_except_table8050
+ GCC_except_table8052
+ GCC_except_table8054
+ GCC_except_table8056
+ GCC_except_table8070
+ GCC_except_table8076
+ GCC_except_table8201
+ GCC_except_table8205
+ GCC_except_table8210
+ GCC_except_table8587
+ GCC_except_table8602
+ GCC_except_table8609
+ GCC_except_table8625
+ GCC_except_table8694
+ GCC_except_table8703
+ GCC_except_table8733
+ GCC_except_table8771
+ GCC_except_table8772
+ GCC_except_table8773
+ GCC_except_table8798
+ GCC_except_table8822
+ GCC_except_table9182
+ GCC_except_table9187
+ GCC_except_table9190
+ GCC_except_table9193
+ GCC_except_table9196
+ GCC_except_table9199
+ GCC_except_table9202
+ GCC_except_table9205
+ GCC_except_table9208
+ GCC_except_table9211
+ GCC_except_table9384
+ GCC_except_table9387
+ GCC_except_table9448
+ GCC_except_table9456
+ GCC_except_table9461
+ GCC_except_table9474
+ GCC_except_table9634
+ GCC_except_table9734
+ GCC_except_table9923
+ _AFIsJ265
+ _AFIsJ265.isJ265
+ _AFIsJ265.onceToken
+ _AFIsWaffleiron
+ _AFMeDeviceLinwoodEnablementDidChangeNotification
+ _AFVisualIntelligenceCameraRestricted.once
+ _OBJC_IVAR_$_AFCompanionDeviceInfo._ifpCapableDevice
+ _OBJC_IVAR_$_AFCompanionDeviceInfo._linwoodCapableDevice
+ _OBJC_IVAR_$_AFCompanionDeviceInfo._siriAvailability
+ _OBJC_IVAR_$_AFSpeechRequestOptions._isReplyToSiriPrompt
+ _OBJC_IVAR_$__AFCompanionDeviceInfoMutation._ifpCapableDevice
+ _OBJC_IVAR_$__AFCompanionDeviceInfoMutation._linwoodCapableDevice
+ _OBJC_IVAR_$__AFCompanionDeviceInfoMutation._siriAvailability
+ __AFPreferencesSetSiriPersonalContentSetting
+ __AFPreferencesSiriPersonalContentSetting
+ __OBJC_$_CATEGORY_SAUIAssistantUtteranceView_$_AssistantAdditions
+ __OBJC_$_CLASS_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions|VSAdditions)
+ __OBJC_$_CLASS_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFPreferences|AssistantServices|AFSiriRequest|ShortDescription)
+ __OBJC_$_CLASS_METHODS_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
+ __OBJC_$_INSTANCE_METHODS_AFClockAlarmSnapshot(Utility|AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot)
+ __OBJC_$_INSTANCE_METHODS_AFClockTimerSnapshot(Utility|AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot)
+ __OBJC_$_INSTANCE_METHODS_AFCompanionDeviceInfo(BackwardCompatibility|SiriAvailability|AFCompanionDeviceInfoMutability)
+ __OBJC_$_INSTANCE_METHODS_AFLocationSnapshot(Ace|AFLocationSnapshotMutability|ShortDescription|ContextSnapshot)
+ __OBJC_$_INSTANCE_METHODS_AFPeerInfo(BackwardCompatibility|ShortDescription|AFPeerInfoMutability)
+ __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions|VSAdditions)
+ __OBJC_$_INSTANCE_METHODS_AceObject(AFSecurityDigestibleChunksProvider|AssistantAdditions|AnalyticsContextVending)
+ __OBJC_$_INSTANCE_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFPreferences|AssistantServices|AFSiriRequest|ShortDescription)
+ __OBJC_$_INSTANCE_METHODS_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
+ __OBJC_$_INSTANCE_METHODS_SAUIAssistantUtteranceView(AssistantAdditions|ClientFeedbackPresented|AnalyticsContextVending)
+ __OBJC_CLASS_PROTOCOLS_$_AFClockAlarmSnapshot(Utility|AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot)
+ __OBJC_CLASS_PROTOCOLS_$_AFClockTimerSnapshot(Utility|AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot)
+ __OBJC_CLASS_PROTOCOLS_$_AFLocationSnapshot(Ace|AFLocationSnapshotMutability|ShortDescription|ContextSnapshot)
+ __OBJC_CLASS_PROTOCOLS_$_AceObject(AFSecurityDigestibleChunksProvider|AssistantAdditions|AnalyticsContextVending)
+ __OBJC_CLASS_PROTOCOLS_$_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
+ ___294-[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:ifpCapableDevice:siriAvailability:]_block_invoke
+ ___56-[AFSettingsConnection isLinwoodEnabledOnAnyHomeDevice:]_block_invoke
+ ___56-[AFSettingsConnection isLinwoodEnabledOnAnyHomeDevice:]_block_invoke_2
+ ___AFIsJ265_block_invoke
+ ___AFVisualIntelligenceCameraRestricted_block_invoke
+ ___block_descriptor_119_e8_32s40s48s56s64s72s80s88s96s104s_e41_v16?0"<AFCompanionDeviceInfoMutating>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ _kAFLinwoodEnabledMeDeviceKey
+ _kAFPersonalContentSettingChangedDarwinNotification
+ _kAFSiriTVPersonalContentSettingKey
- -[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:]
- GCC_except_table10149
- GCC_except_table10258
- GCC_except_table10269
- GCC_except_table10302
- GCC_except_table10305
- GCC_except_table10381
- GCC_except_table10385
- GCC_except_table10395
- GCC_except_table10406
- GCC_except_table10419
- GCC_except_table10504
- GCC_except_table10506
- GCC_except_table10530
- GCC_except_table10646
- GCC_except_table10709
- GCC_except_table10712
- GCC_except_table10716
- GCC_except_table10733
- GCC_except_table10747
- GCC_except_table10821
- GCC_except_table10879
- GCC_except_table10905
- GCC_except_table11180
- GCC_except_table11326
- GCC_except_table11339
- GCC_except_table11384
- GCC_except_table11478
- GCC_except_table11717
- GCC_except_table12041
- GCC_except_table12175
- GCC_except_table12178
- GCC_except_table12180
- GCC_except_table2628
- GCC_except_table2714
- GCC_except_table2768
- GCC_except_table3004
- GCC_except_table3007
- GCC_except_table3008
- GCC_except_table3205
- GCC_except_table3264
- GCC_except_table3478
- GCC_except_table3481
- GCC_except_table3493
- GCC_except_table3494
- GCC_except_table3508
- GCC_except_table3515
- GCC_except_table3553
- GCC_except_table3559
- GCC_except_table3565
- GCC_except_table3633
- GCC_except_table3635
- GCC_except_table3670
- GCC_except_table3673
- GCC_except_table3784
- GCC_except_table3847
- GCC_except_table3849
- GCC_except_table3851
- GCC_except_table3853
- GCC_except_table3867
- GCC_except_table3873
- GCC_except_table3998
- GCC_except_table4002
- GCC_except_table4007
- GCC_except_table4381
- GCC_except_table4396
- GCC_except_table4403
- GCC_except_table4419
- GCC_except_table4488
- GCC_except_table4497
- GCC_except_table4527
- GCC_except_table4565
- GCC_except_table4566
- GCC_except_table4567
- GCC_except_table4592
- GCC_except_table4616
- GCC_except_table4976
- GCC_except_table4981
- GCC_except_table4984
- GCC_except_table4987
- GCC_except_table4990
- GCC_except_table4993
- GCC_except_table4996
- GCC_except_table4999
- GCC_except_table5002
- GCC_except_table5005
- GCC_except_table5178
- GCC_except_table5181
- GCC_except_table5242
- GCC_except_table5250
- GCC_except_table5255
- GCC_except_table5268
- GCC_except_table5428
- GCC_except_table5528
- GCC_except_table5717
- GCC_except_table5722
- GCC_except_table5852
- GCC_except_table6060
- GCC_except_table6100
- GCC_except_table6131
- GCC_except_table6137
- GCC_except_table6138
- GCC_except_table6142
- GCC_except_table6331
- GCC_except_table6502
- GCC_except_table6531
- GCC_except_table6628
- GCC_except_table6632
- GCC_except_table6636
- GCC_except_table6665
- GCC_except_table7019
- GCC_except_table7021
- GCC_except_table7024
- GCC_except_table7033
- GCC_except_table7095
- GCC_except_table7116
- GCC_except_table7141
- GCC_except_table7147
- GCC_except_table7297
- GCC_except_table7301
- GCC_except_table7303
- GCC_except_table7306
- GCC_except_table7312
- GCC_except_table7316
- GCC_except_table7322
- GCC_except_table7572
- GCC_except_table7585
- GCC_except_table7589
- GCC_except_table7601
- GCC_except_table7605
- GCC_except_table7720
- GCC_except_table7794
- GCC_except_table8202
- GCC_except_table8209
- GCC_except_table8215
- GCC_except_table8217
- GCC_except_table8219
- GCC_except_table8264
- GCC_except_table8266
- GCC_except_table8272
- GCC_except_table8278
- GCC_except_table8282
- GCC_except_table8288
- GCC_except_table8295
- GCC_except_table8297
- GCC_except_table8302
- GCC_except_table8304
- GCC_except_table8309
- GCC_except_table8321
- GCC_except_table8324
- GCC_except_table8338
- GCC_except_table8340
- GCC_except_table8342
- GCC_except_table8344
- GCC_except_table8346
- GCC_except_table8348
- GCC_except_table8350
- GCC_except_table8396
- GCC_except_table8422
- GCC_except_table8479
- GCC_except_table8515
- GCC_except_table8918
- GCC_except_table9207
- GCC_except_table9406
- GCC_except_table9414
- GCC_except_table9472
- GCC_except_table9848
- GCC_except_table9852
- GCC_except_table9897
- GCC_except_table9903
- GCC_except_table9934
- __OBJC_$_CATEGORY_SAUIAssistantUtteranceView_$_ClientFeedbackPresented
- __OBJC_$_CLASS_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|VSAdditions|AFLocalizationAdditions)
- __OBJC_$_CLASS_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription|AFPreferences|AssistantServices)
- __OBJC_$_CLASS_METHODS_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
- __OBJC_$_INSTANCE_METHODS_AFClockAlarmSnapshot(AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
- __OBJC_$_INSTANCE_METHODS_AFClockTimerSnapshot(AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
- __OBJC_$_INSTANCE_METHODS_AFCompanionDeviceInfo(AFCompanionDeviceInfoMutability|BackwardCompatibility)
- __OBJC_$_INSTANCE_METHODS_AFLocationSnapshot(AFLocationSnapshotMutability|ShortDescription|ContextSnapshot|Ace)
- __OBJC_$_INSTANCE_METHODS_AFPeerInfo(ShortDescription|BackwardCompatibility|AFPeerInfoMutability)
- __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|VSAdditions|AFLocalizationAdditions)
- __OBJC_$_INSTANCE_METHODS_AceObject(AFSecurityDigestibleChunksProvider|AnalyticsContextVending|AssistantAdditions)
- __OBJC_$_INSTANCE_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription|AFPreferences|AssistantServices)
- __OBJC_$_INSTANCE_METHODS_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
- __OBJC_$_INSTANCE_METHODS_SAUIAssistantUtteranceView(ClientFeedbackPresented|AnalyticsContextVending|AssistantAdditions)
- __OBJC_CLASS_PROTOCOLS_$_AFClockAlarmSnapshot(AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
- __OBJC_CLASS_PROTOCOLS_$_AFClockTimerSnapshot(AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
- __OBJC_CLASS_PROTOCOLS_$_AFLocationSnapshot(AFLocationSnapshotMutability|ShortDescription|ContextSnapshot|Ace)
- __OBJC_CLASS_PROTOCOLS_$_AceObject(AFSecurityDigestibleChunksProvider|AnalyticsContextVending|AssistantAdditions)
- __OBJC_CLASS_PROTOCOLS_$_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
- ___239-[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:]_block_invoke
- ___block_descriptor_109_e8_32s40s48s56s64s72s80s88s96s_e41_v16?0"<AFCompanionDeviceInfoMutating>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
- ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
CStrings:
+ "%@ {assistantID = %@, speechID = %@, idsIdentifier = %@, productPrefix = %@, aceHost = %@, syncMetadata = %@, syncMetadataCapability = %@, peerToPeerHandoffCapability = %@, muxSupportCapability = %@, meDevice = %@, siriLanguage = %@, companionName = %@, buildVersion = %@, linwoodEnabled = %@, linwoodCapableDevice = %@, ifpCapableDevice = %@, siriAvailability = %@}"
+ "%s Asked to set nil iCloudAltDSID for personal content setting"
+ "%s No readable AFSiriAvailability in this process; the Device Configuration Visual Intelligence restriction is not applied here. Enforcing it requires read access to com.apple.assistant.backedup."
+ "%s Requested nil iCloudAltDSID for personal content setting"
+ "%s visualIntelligenceRestricted = %d (no readable AFSiriAvailability, local policy only)"
+ ", isReplyToSiriPrompt = %d"
+ "AFCompanionDeviceInfo::ifpCapableDevice"
+ "AFCompanionDeviceInfo::linwoodCapableDevice"
+ "AFCompanionDeviceInfo::siriAvailability"
+ "AFMeDeviceLinwoodEnablementDidChangeNotification"
+ "AFVisualIntelligenceCameraRestricted_block_invoke"
+ "AppleTV18,1"
+ "Linwood Enabled Me Device"
+ "RISESSION_CLIENT_EVENT"
+ "RI_CLIENT_EVENT"
+ "Siri Apple TV Personal content setting"
+ "_AFPreferencesSetSiriPersonalContentSetting"
+ "_AFPreferencesSiriPersonalContentSetting"
+ "_isReplyToSiriPrompt"
+ "com.apple.siri.personalcontent.setting.changed"
+ "ifpCapableDevice"
+ "linwoodCapableDevice"
+ "siriAvailability"
- "%@ {assistantID = %@, speechID = %@, idsIdentifier = %@, productPrefix = %@, aceHost = %@, syncMetadata = %@, syncMetadataCapability = %@, peerToPeerHandoffCapability = %@, muxSupportCapability = %@, meDevice = %@, siriLanguage = %@, companionName = %@, buildVersion = %@, linwoodEnabled = %@}"
- "%s visualIntelligenceRestricted = 1 (no persisted AFSiriAvailability)"
```
