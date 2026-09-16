## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3600.68.61.11.11
-  __TEXT.__text: 0x19362c
-  __TEXT.__objc_methlist: 0x1f094
+3605.23.1.1.1
+  __TEXT.__text: 0x19597c
+  __TEXT.__objc_methlist: 0x1f31c
   __TEXT.__const: 0x3d0
   __TEXT.__dlopen_cstrs: 0x538
-  __TEXT.__gcc_except_tab: 0x21b8
-  __TEXT.__cstring: 0x3d3fa
-  __TEXT.__oslogstring: 0xf5ac
+  __TEXT.__gcc_except_tab: 0x21d8
+  __TEXT.__cstring: 0x3d9a3
+  __TEXT.__oslogstring: 0xf845
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x9e58
+  __TEXT.__unwind_info: 0x9f28
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x85f0
-  __DATA_CONST.__objc_classlist: 0xef8
+  __DATA_CONST.__const: 0x8730
+  __DATA_CONST.__objc_classlist: 0xf00
   __DATA_CONST.__objc_catlist: 0x2a8
-  __DATA_CONST.__objc_protolist: 0x5e8
+  __DATA_CONST.__objc_protolist: 0x5f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc0f0
-  __DATA_CONST.__objc_protorefs: 0x170
-  __DATA_CONST.__objc_superrefs: 0xf10
-  __DATA_CONST.__objc_arraydata: 0x23a0
-  __DATA_CONST.__got: 0x16d0
+  __DATA_CONST.__objc_selrefs: 0xc210
+  __DATA_CONST.__objc_protorefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0xf18
+  __DATA_CONST.__objc_arraydata: 0x2440
+  __DATA_CONST.__got: 0x16f0
   __AUTH_CONST.__const: 0x3ca0
-  __AUTH_CONST.__cfstring: 0x28480
-  __AUTH_CONST.__objc_const: 0x36340
-  __AUTH_CONST.__objc_intobj: 0x2628
-  __AUTH_CONST.__objc_dictobj: 0xcf8
+  __AUTH_CONST.__cfstring: 0x287c0
+  __AUTH_CONST.__objc_const: 0x365f8
+  __AUTH_CONST.__objc_intobj: 0x2700
+  __AUTH_CONST.__objc_dictobj: 0xd20
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0xae8
-  __AUTH.__objc_data: 0x8610
+  __AUTH_CONST.__auth_got: 0xad8
+  __AUTH.__objc_data: 0x8660
   __AUTH.__data: 0x248
-  __DATA.__objc_ivar: 0x257c
-  __DATA.__data: 0x4800
+  __DATA.__objc_ivar: 0x259c
+  __DATA.__data: 0x4860
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x18
-  __DATA_DIRTY.__bss: 0x200
+  __DATA_DIRTY.__bss: 0x1f0
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12116
-  Symbols:   26771
-  CStrings:  8603
+  Functions: 12182
+  Symbols:   26901
+  CStrings:  8654
 
Symbols:
+ +[AFFeatureFlags(SWEFeatureFlags) isAceSyncDisabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isCloudKitCacheMirroredChangeTokensEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isSiriCapabilitiesSettleCoalescingDisabled]
+ +[AFFeatureFlags(SWEFeatureFlags) siriAvailabilityOverXPCEnabled]
+ -[AFCompanionDeviceInfo buildVersion]
+ -[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:]
+ -[AFCompanionDeviceInfo linwoodEnabled]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:]
+ -[AFConnection _endUsefulUserFacingResultsIntervalIfNeeded]
+ -[AFConnection _replyMissingDelegateMethodTo:]
+ -[AFConnection notifyAppLaunchWillBePresentedToUser]
+ -[AFConnection siriDidBecomeEffectivelyActive]
+ -[AFConnection siriDidBecomeEffectivelyInactive]
+ -[AFConnectionClientServiceDelegate notifyAppLaunchWillBePresentedToUser]
+ -[AFConnectionEntitlementCache cacheEntitlement:forPID:pidVersion:bundleID:]
+ -[AFConnectionEntitlementCache hasEntitlement:forPID:pidVersion:]
+ -[AFDictationOptions applicationProcessIdentifier]
+ -[AFDictationOptions setApplicationProcessIdentifier:]
+ -[AFDisambiguationOutcomeDescriptor selectsAll]
+ -[AFDisambiguationOutcomeDescriptor setSelectsAll:]
+ -[AFLocalTurnStatusService .cxx_destruct]
+ -[AFLocalTurnStatusService connection]
+ -[AFLocalTurnStatusService currentLocalTurnStatus:]
+ -[AFLocalTurnStatusService dealloc]
+ -[AFLocalTurnStatusService serviceWithErrorHandler:]
+ -[AFLocalTurnStatusService setConnection:]
+ -[AFMultiArgumentSafetyBlock dealloc]
+ -[AFMultiUserConnection isRecognizeMyVoiceEnabledForAnyUser:]
+ -[AFPreferences announceNotificationsInCarPlayTemporarilyDisabled]
+ -[AFRequestInfo myriadElectionIdentity]
+ -[AFSettingsConnection armAnnounceOverrideFollowUpText:reply:]
+ -[AFSettingsConnection forceWeeklyCloudKitSyncWithCompletion:]
+ -[AFSettingsConnection(Internal) _syncDataWithAnchorKeys:forceReset:reason:completionWithError:]
+ -[AFSiriAnnounceWorkoutVoiceFeedbackRequest performRequestWithResultCompletion:]
+ -[AFSiriAvailability initWithDictionary:]
+ -[AFSiriAvailability initWithSiriLanguageCode:]
+ -[AFSiriCapabilitiesServiceClient siriAvailability:]
+ -[AFSiriCapabilitiesServiceClient siriAvailabilitySync]
+ -[AFSpeechRequestOptions myriadElectionIdentity]
+ -[AFSpeechRequestOptions setMyriadElectionIdentity:]
+ -[_AFCompanionDeviceInfoMutation getBuildVersion]
+ -[_AFCompanionDeviceInfoMutation getLinwoodEnabled]
+ -[_AFCompanionDeviceInfoMutation setBuildVersion:]
+ -[_AFCompanionDeviceInfoMutation setLinwoodEnabled:]
+ GCC_except_table10066
+ GCC_except_table10068
+ GCC_except_table10092
+ GCC_except_table10208
+ GCC_except_table10271
+ GCC_except_table10274
+ GCC_except_table10278
+ GCC_except_table10295
+ GCC_except_table10309
+ GCC_except_table10383
+ GCC_except_table10441
+ GCC_except_table10467
+ GCC_except_table10742
+ GCC_except_table10888
+ GCC_except_table10901
+ GCC_except_table10946
+ GCC_except_table11040
+ GCC_except_table1115
+ GCC_except_table11162
+ GCC_except_table11164
+ GCC_except_table11167
+ GCC_except_table11176
+ GCC_except_table11238
+ GCC_except_table11259
+ GCC_except_table11284
+ GCC_except_table11290
+ GCC_except_table11440
+ GCC_except_table11444
+ GCC_except_table11446
+ GCC_except_table11449
+ GCC_except_table11455
+ GCC_except_table11459
+ GCC_except_table11465
+ GCC_except_table11672
+ GCC_except_table1181
+ GCC_except_table1187
+ GCC_except_table11996
+ GCC_except_table12130
+ GCC_except_table12133
+ GCC_except_table12135
+ GCC_except_table1308
+ GCC_except_table1310
+ GCC_except_table1491
+ GCC_except_table1528
+ GCC_except_table1534
+ GCC_except_table1540
+ GCC_except_table1560
+ GCC_except_table1566
+ GCC_except_table1569
+ GCC_except_table1935
+ GCC_except_table2049
+ GCC_except_table2303
+ GCC_except_table2316
+ GCC_except_table2317
+ GCC_except_table2329
+ GCC_except_table2336
+ GCC_except_table2337
+ GCC_except_table2340
+ GCC_except_table2346
+ GCC_except_table238
+ GCC_except_table2393
+ GCC_except_table2395
+ GCC_except_table2397
+ GCC_except_table2415
+ GCC_except_table2421
+ GCC_except_table244
+ GCC_except_table2464
+ GCC_except_table2476
+ GCC_except_table250
+ GCC_except_table2622
+ GCC_except_table264
+ GCC_except_table2708
+ GCC_except_table2762
+ GCC_except_table2998
+ GCC_except_table3001
+ GCC_except_table3002
+ GCC_except_table3199
+ GCC_except_table3258
+ GCC_except_table3472
+ GCC_except_table3475
+ GCC_except_table3487
+ GCC_except_table3488
+ GCC_except_table3501
+ GCC_except_table3502
+ GCC_except_table3503
+ GCC_except_table3509
+ GCC_except_table3547
+ GCC_except_table3553
+ GCC_except_table3559
+ GCC_except_table361
+ GCC_except_table3627
+ GCC_except_table3629
+ GCC_except_table3664
+ GCC_except_table3667
+ GCC_except_table3778
+ GCC_except_table379
+ GCC_except_table383
+ GCC_except_table3841
+ GCC_except_table3843
+ GCC_except_table3845
+ GCC_except_table3847
+ GCC_except_table3861
+ GCC_except_table3867
+ GCC_except_table3992
+ GCC_except_table3996
+ GCC_except_table4001
+ GCC_except_table4375
+ GCC_except_table4390
+ GCC_except_table4397
+ GCC_except_table4413
+ GCC_except_table4482
+ GCC_except_table4491
+ GCC_except_table4521
+ GCC_except_table4559
+ GCC_except_table4560
+ GCC_except_table4561
+ GCC_except_table4586
+ GCC_except_table4610
+ GCC_except_table4970
+ GCC_except_table4975
+ GCC_except_table4978
+ GCC_except_table4981
+ GCC_except_table4984
+ GCC_except_table4987
+ GCC_except_table4990
+ GCC_except_table4993
+ GCC_except_table4996
+ GCC_except_table4999
+ GCC_except_table5170
+ GCC_except_table5234
+ GCC_except_table5242
+ GCC_except_table5247
+ GCC_except_table5260
+ GCC_except_table5420
+ GCC_except_table5520
+ GCC_except_table5709
+ GCC_except_table5714
+ GCC_except_table5844
+ GCC_except_table587
+ GCC_except_table6052
+ GCC_except_table6092
+ GCC_except_table6123
+ GCC_except_table6129
+ GCC_except_table6130
+ GCC_except_table6134
+ GCC_except_table6323
+ GCC_except_table638
+ GCC_except_table6494
+ GCC_except_table6523
+ GCC_except_table6620
+ GCC_except_table6624
+ GCC_except_table6628
+ GCC_except_table6657
+ GCC_except_table7171
+ GCC_except_table7184
+ GCC_except_table7188
+ GCC_except_table7200
+ GCC_except_table7204
+ GCC_except_table7317
+ GCC_except_table7319
+ GCC_except_table7393
+ GCC_except_table7437
+ GCC_except_table7799
+ GCC_except_table7806
+ GCC_except_table7812
+ GCC_except_table7814
+ GCC_except_table7816
+ GCC_except_table7861
+ GCC_except_table7863
+ GCC_except_table7869
+ GCC_except_table7875
+ GCC_except_table7879
+ GCC_except_table7885
+ GCC_except_table7888
+ GCC_except_table7890
+ GCC_except_table7895
+ GCC_except_table7897
+ GCC_except_table7902
+ GCC_except_table7914
+ GCC_except_table7917
+ GCC_except_table7931
+ GCC_except_table7933
+ GCC_except_table7935
+ GCC_except_table7937
+ GCC_except_table7939
+ GCC_except_table7941
+ GCC_except_table7943
+ GCC_except_table7988
+ GCC_except_table8014
+ GCC_except_table8071
+ GCC_except_table8104
+ GCC_except_table839
+ GCC_except_table842
+ GCC_except_table8482
+ GCC_except_table849
+ GCC_except_table8771
+ GCC_except_table8970
+ GCC_except_table8978
+ GCC_except_table9036
+ GCC_except_table9412
+ GCC_except_table9416
+ GCC_except_table9461
+ GCC_except_table9467
+ GCC_except_table9492
+ GCC_except_table9498
+ GCC_except_table9711
+ GCC_except_table980
+ GCC_except_table9820
+ GCC_except_table9831
+ GCC_except_table9864
+ GCC_except_table9867
+ GCC_except_table9943
+ GCC_except_table9947
+ GCC_except_table9957
+ GCC_except_table9968
+ GCC_except_table9981
+ _AFDaemonIsExitingCleanly
+ _AFDaemonWillExitCleanlyNotification
+ _AFIsHomePod
+ _AFIsHomePod.isHomePod
+ _AFIsHomePod.onceToken
+ _AFResetDaemonIsExitingCleanlyForTesting
+ _AFSimulateDaemonWillExitCleanlyForTesting
+ _AFSiriWorkoutVoiceFeedbackResultGetFromName
+ _AFSiriWorkoutVoiceFeedbackResultGetFromName.map
+ _AFSiriWorkoutVoiceFeedbackResultGetFromName.onceToken
+ _AFSiriWorkoutVoiceFeedbackResultGetIsValid
+ _AFSiriWorkoutVoiceFeedbackResultGetIsValidAndSpecified
+ _AFSiriWorkoutVoiceFeedbackResultGetName
+ _OBJC_CLASS_$_AFLocalTurnStatusService
+ _OBJC_CLASS_$_SAUIStreamChunk
+ _OBJC_CLASS_$_SCDAElectionIdentity
+ _OBJC_CLASS_$_SCDAFeatureFlags
+ _OBJC_IVAR_$_AFCompanionDeviceInfo._buildVersion
+ _OBJC_IVAR_$_AFCompanionDeviceInfo._linwoodEnabled
+ _OBJC_IVAR_$_AFConnectionEntitlementCache._bundleIDToKeyMap
+ _OBJC_IVAR_$_AFDictationOptions._applicationProcessIdentifier
+ _OBJC_IVAR_$_AFDisambiguationOutcomeDescriptor._selectsAll
+ _OBJC_IVAR_$_AFLocalTurnStatusService._connection
+ _OBJC_IVAR_$_AFSpeechRequestOptions._myriadElectionIdentity
+ _OBJC_IVAR_$__AFCompanionDeviceInfoMutation._buildVersion
+ _OBJC_IVAR_$__AFCompanionDeviceInfoMutation._linwoodEnabled
+ _OBJC_METACLASS_$_AFLocalTurnStatusService
+ __AFBeginExitingCleanly
+ __AFPreferencesAnnouncementPlatformOverride
+ __AFPreferencesIsAnnouncementPlatformOverrideActive
+ __AFPreferencesSetAnnouncementPlatformOverride
+ __OBJC_$_CATEGORY_AceObject_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSArray_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSDate_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSDictionary_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSNull_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSString_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSURL_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_SAUIAssistantUtteranceView_$_ClientFeedbackPresented
+ __OBJC_$_CLASS_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions|VSAdditions)
+ __OBJC_$_CLASS_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription|AFPreferences|AssistantServices)
+ __OBJC_$_CLASS_METHODS_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
+ __OBJC_$_INSTANCE_METHODS_AFClockAlarmSnapshot(AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
+ __OBJC_$_INSTANCE_METHODS_AFClockTimer(AFClockTimerMutability|ClockItem)
+ __OBJC_$_INSTANCE_METHODS_AFClockTimerSnapshot(AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
+ __OBJC_$_INSTANCE_METHODS_AFCompanionDeviceInfo(BackwardCompatibility|AFCompanionDeviceInfoMutability)
+ __OBJC_$_INSTANCE_METHODS_AFLocalTurnStatusService
+ __OBJC_$_INSTANCE_METHODS_AFLocationSnapshot(AFLocationSnapshotMutability|ShortDescription|ContextSnapshot|Ace)
+ __OBJC_$_INSTANCE_METHODS_AFPeerInfo(ShortDescription|BackwardCompatibility|AFPeerInfoMutability)
+ __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions|VSAdditions)
+ __OBJC_$_INSTANCE_METHODS_AceObject(AFSecurityDigestibleChunksProvider|AnalyticsContextVending|AssistantAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSArray(AFSecurityDigestibleChunksProvider|AFCollectionUtilities)
+ __OBJC_$_INSTANCE_METHODS_NSDate(AFSecurityDigestibleChunksProvider|AssistantAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(AFSecurityDigestibleChunksProvider|AFCollectionUtilities)
+ __OBJC_$_INSTANCE_METHODS_NSNull(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport)
+ __OBJC_$_INSTANCE_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription|AFPreferences|AssistantServices)
+ __OBJC_$_INSTANCE_METHODS_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
+ __OBJC_$_INSTANCE_METHODS_SAUIAssistantUtteranceView(ClientFeedbackPresented|AnalyticsContextVending|AssistantAdditions)
+ __OBJC_$_INSTANCE_VARIABLES_AFLocalTurnStatusService
+ __OBJC_$_PROP_LIST_AFLocalTurnStatusService
+ __OBJC_$_PROP_LIST_AFPreferences
+ __OBJC_$_PROP_LIST_NSArray_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_PROP_LIST_NSDate_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_PROP_LIST_NSDictionary_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_PROP_LIST_NSString_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFLocalTurnStatusServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AFLocalTurnStatusServiceInterface
+ __OBJC_CATEGORY_PROTOCOLS_$_NSArray_$_AFSecurityDigestibleChunksProvider
+ __OBJC_CATEGORY_PROTOCOLS_$_NSDate_$_AFSecurityDigestibleChunksProvider
+ __OBJC_CATEGORY_PROTOCOLS_$_NSDictionary_$_AFSecurityDigestibleChunksProvider
+ __OBJC_CATEGORY_PROTOCOLS_$_NSString_$_AFSecurityDigestibleChunksProvider
+ __OBJC_CLASS_PROTOCOLS_$_AFClockAlarmSnapshot(AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
+ __OBJC_CLASS_PROTOCOLS_$_AFClockTimer(AFClockTimerMutability|ClockItem)
+ __OBJC_CLASS_PROTOCOLS_$_AFClockTimerSnapshot(AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
+ __OBJC_CLASS_PROTOCOLS_$_AFLocationSnapshot(AFLocationSnapshotMutability|ShortDescription|ContextSnapshot|Ace)
+ __OBJC_CLASS_PROTOCOLS_$_AceObject(AFSecurityDigestibleChunksProvider|AnalyticsContextVending|AssistantAdditions)
+ __OBJC_CLASS_PROTOCOLS_$_NSNull(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport)
+ __OBJC_CLASS_PROTOCOLS_$_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
+ __OBJC_CLASS_RO_$_AFLocalTurnStatusService
+ __OBJC_LABEL_PROTOCOL_$_AFLocalTurnStatusServiceInterface
+ __OBJC_METACLASS_RO_$_AFLocalTurnStatusService
+ __OBJC_PROTOCOL_$_AFLocalTurnStatusServiceInterface
+ __OBJC_PROTOCOL_REFERENCE_$_AFLocalTurnStatusServiceInterface
+ ___239-[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:]_block_invoke
+ ___51-[AFLocalTurnStatusService currentLocalTurnStatus:]_block_invoke
+ ___51-[AFLocalTurnStatusService currentLocalTurnStatus:]_block_invoke_2
+ ___52-[AFSiriCapabilitiesServiceClient siriAvailability:]_block_invoke
+ ___52-[AFSiriCapabilitiesServiceClient siriAvailability:]_block_invoke_2
+ ___55-[AFSiriCapabilitiesServiceClient siriAvailabilitySync]_block_invoke
+ ___55-[AFSiriCapabilitiesServiceClient siriAvailabilitySync]_block_invoke_2
+ ___61-[AFMultiUserConnection isRecognizeMyVoiceEnabledForAnyUser:]_block_invoke
+ ___61-[AFMultiUserConnection isRecognizeMyVoiceEnabledForAnyUser:]_block_invoke_2
+ ___62-[AFSettingsConnection armAnnounceOverrideFollowUpText:reply:]_block_invoke
+ ___62-[AFSettingsConnection forceWeeklyCloudKitSyncWithCompletion:]_block_invoke
+ ___73-[AFConnectionClientServiceDelegate notifyAppLaunchWillBePresentedToUser]_block_invoke
+ ___80-[AFSiriAnnounceWorkoutVoiceFeedbackRequest performRequestWithResultCompletion:]_block_invoke
+ ___96-[AFSettingsConnection(Internal) _syncDataWithAnchorKeys:forceReset:reason:completionWithError:]_block_invoke
+ ___AFIsHomePod_block_invoke
+ ___AFSiriWorkoutVoiceFeedbackResultGetFromName_block_invoke
+ ___block_descriptor_109_e8_32s40s48s56s64s72s80s88s96s_e41_v16?0"<AFCompanionDeviceInfoMutating>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_40_e8_32bs_e21_v24?0Q8"NSString"16ls32l8
+ ___block_descriptor_40_e8_32r_e28_v16?0"AFSiriAvailability"8lr32l8
+ ___block_descriptor_48_e8_32bs40r_e28_v16?0"AFSiriAvailability"8ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_90_e8_32s40s48s56s64bs_e33_v16?0"AceObject<SAAceCommand>"8ls32l8s64l8s40l8s48l8s56l8
+ ___block_descriptor_98_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s72l8s40l8s48l8s56l8s64l8
+ _kAFLocalTurnStatusServiceEntitlement
+ _kAFLocalTurnStatusServiceErrorDomain
+ _kAFLocalTurnStatusServiceMachServiceName
+ _objc_msgSend$_endUsefulUserFacingResultsIntervalIfNeeded
+ _objc_msgSend$_replyMissingDelegateMethodTo:
+ _objc_msgSend$_syncDataWithAnchorKeys:forceReset:reason:replyWithError:
+ _objc_msgSend$applicationProcessIdentifier
+ _objc_msgSend$armAnnounceOverrideFollowUpText:reply:
+ _objc_msgSend$cacheEntitlement:forPID:pidVersion:bundleID:
+ _objc_msgSend$currentLocalTurnStatus:
+ _objc_msgSend$forceWeeklyCloudKitSyncWithCompletion:
+ _objc_msgSend$getArgumentTypeAtIndex:
+ _objc_msgSend$getLinwoodEnabled
+ _objc_msgSend$hasEntitlement:forPID:pidVersion:
+ _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:
+ _objc_msgSend$initWithSiriLanguageCode:
+ _objc_msgSend$isElectionLedgerEnabled
+ _objc_msgSend$isMediaEntitySyncDisabled
+ _objc_msgSend$isRecognizeMyVoiceEnabledForAnyUserWithCompletion:
+ _objc_msgSend$linwoodEnabled
+ _objc_msgSend$mintElectionIdentity
+ _objc_msgSend$myriadElectionIdentity
+ _objc_msgSend$notifyAppLaunchWillBePresentedToUser
+ _objc_msgSend$performRequestWithResultCompletion:
+ _objc_msgSend$setApplicationProcessIdentifier:
+ _objc_msgSend$setLinwoodEnabled:
+ _objc_msgSend$setMyriadElectionIdentity:
+ _objc_msgSend$siriAvailability:
+ _objc_msgSend$siriAvailabilityOverXPCEnabled
+ _objc_msgSend$siriAvailabilitySync
+ _objc_msgSend$siriDidBecomeEffectivelyActive
+ _objc_msgSend$siriDidBecomeEffectivelyInactive
+ _objc_msgSend$streamId
+ _objc_msgSend$streamStage
+ _sAFDaemonIsExitingCleanly
- +[AFFeatureFlags(SWEFeatureFlags) isHintsEnabled]
- +[AFSiriAvailability fromDictionary:]
- -[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:]
- -[AFConnectionEntitlementCache cacheEntitlement:forPID:bundleID:]
- -[AFConnectionEntitlementCache hasEntitlement:forPID:]
- GCC_except_table10148
- GCC_except_table10188
- GCC_except_table10219
- GCC_except_table10224
- GCC_except_table10225
- GCC_except_table10229
- GCC_except_table10418
- GCC_except_table10589
- GCC_except_table10618
- GCC_except_table10715
- GCC_except_table10719
- GCC_except_table10723
- GCC_except_table10752
- GCC_except_table1103
- GCC_except_table11106
- GCC_except_table11108
- GCC_except_table11111
- GCC_except_table11120
- GCC_except_table11181
- GCC_except_table11202
- GCC_except_table11227
- GCC_except_table11233
- GCC_except_table11377
- GCC_except_table11381
- GCC_except_table11383
- GCC_except_table11386
- GCC_except_table11392
- GCC_except_table11396
- GCC_except_table11402
- GCC_except_table11606
- GCC_except_table1169
- GCC_except_table1175
- GCC_except_table11930
- GCC_except_table12064
- GCC_except_table12067
- GCC_except_table12069
- GCC_except_table1468
- GCC_except_table1481
- GCC_except_table1485
- GCC_except_table1497
- GCC_except_table1501
- GCC_except_table1606
- GCC_except_table1608
- GCC_except_table1680
- GCC_except_table1724
- GCC_except_table2086
- GCC_except_table2093
- GCC_except_table2099
- GCC_except_table2101
- GCC_except_table2103
- GCC_except_table2148
- GCC_except_table2150
- GCC_except_table2156
- GCC_except_table2162
- GCC_except_table2166
- GCC_except_table2170
- GCC_except_table2173
- GCC_except_table2175
- GCC_except_table2182
- GCC_except_table2187
- GCC_except_table2199
- GCC_except_table2202
- GCC_except_table2216
- GCC_except_table2218
- GCC_except_table2220
- GCC_except_table2222
- GCC_except_table2224
- GCC_except_table2226
- GCC_except_table2228
- GCC_except_table2273
- GCC_except_table2299
- GCC_except_table231
- GCC_except_table2356
- GCC_except_table237
- GCC_except_table2389
- GCC_except_table243
- GCC_except_table257
- GCC_except_table2763
- GCC_except_table3051
- GCC_except_table3248
- GCC_except_table3256
- GCC_except_table3314
- GCC_except_table352
- GCC_except_table3691
- GCC_except_table3695
- GCC_except_table370
- GCC_except_table374
- GCC_except_table3740
- GCC_except_table3746
- GCC_except_table3771
- GCC_except_table3777
- GCC_except_table3987
- GCC_except_table4096
- GCC_except_table4107
- GCC_except_table4140
- GCC_except_table4143
- GCC_except_table4220
- GCC_except_table4224
- GCC_except_table4234
- GCC_except_table4245
- GCC_except_table4258
- GCC_except_table4343
- GCC_except_table4345
- GCC_except_table4369
- GCC_except_table4484
- GCC_except_table4547
- GCC_except_table4550
- GCC_except_table4554
- GCC_except_table4571
- GCC_except_table4585
- GCC_except_table4659
- GCC_except_table4717
- GCC_except_table4743
- GCC_except_table5017
- GCC_except_table5160
- GCC_except_table5217
- GCC_except_table5311
- GCC_except_table5419
- GCC_except_table5421
- GCC_except_table5602
- GCC_except_table5639
- GCC_except_table5645
- GCC_except_table5649
- GCC_except_table5669
- GCC_except_table5675
- GCC_except_table5678
- GCC_except_table576
- GCC_except_table6044
- GCC_except_table6158
- GCC_except_table626
- GCC_except_table6289
- GCC_except_table6412
- GCC_except_table6425
- GCC_except_table6426
- GCC_except_table6438
- GCC_except_table6445
- GCC_except_table6446
- GCC_except_table6449
- GCC_except_table6455
- GCC_except_table6502
- GCC_except_table6504
- GCC_except_table6506
- GCC_except_table6524
- GCC_except_table6530
- GCC_except_table6573
- GCC_except_table6585
- GCC_except_table6731
- GCC_except_table6817
- GCC_except_table6871
- GCC_except_table7107
- GCC_except_table7110
- GCC_except_table7111
- GCC_except_table7308
- GCC_except_table7367
- GCC_except_table7581
- GCC_except_table7584
- GCC_except_table7596
- GCC_except_table7597
- GCC_except_table7610
- GCC_except_table7611
- GCC_except_table7612
- GCC_except_table7618
- GCC_except_table7656
- GCC_except_table7662
- GCC_except_table7668
- GCC_except_table7736
- GCC_except_table7738
- GCC_except_table7773
- GCC_except_table7776
- GCC_except_table7887
- GCC_except_table7950
- GCC_except_table7952
- GCC_except_table7954
- GCC_except_table7956
- GCC_except_table7970
- GCC_except_table7976
- GCC_except_table8099
- GCC_except_table8103
- GCC_except_table8108
- GCC_except_table827
- GCC_except_table830
- GCC_except_table837
- GCC_except_table8479
- GCC_except_table8494
- GCC_except_table8501
- GCC_except_table8517
- GCC_except_table8584
- GCC_except_table8593
- GCC_except_table8623
- GCC_except_table8661
- GCC_except_table8662
- GCC_except_table8663
- GCC_except_table8688
- GCC_except_table8712
- GCC_except_table9072
- GCC_except_table9077
- GCC_except_table9080
- GCC_except_table9083
- GCC_except_table9086
- GCC_except_table9089
- GCC_except_table9092
- GCC_except_table9095
- GCC_except_table9266
- GCC_except_table9269
- GCC_except_table9330
- GCC_except_table9338
- GCC_except_table9343
- GCC_except_table9356
- GCC_except_table9516
- GCC_except_table9616
- GCC_except_table968
- GCC_except_table9805
- GCC_except_table9810
- GCC_except_table9940
- _AFIsHorseman.isHorseman
- _AFIsHorseman.onceToken
- _AFProcessGetInstanceUUID.instanceUUID
- _OBJC_IVAR_$_AFConnectionEntitlementCache._bundleIDToPIDMap
- __OBJC_$_CATEGORY_AceObject_$_AssistantAdditions
- __OBJC_$_CATEGORY_NSArray_$_AFCollectionUtilities
- __OBJC_$_CATEGORY_NSDate_$_AssistantAdditions
- __OBJC_$_CATEGORY_NSDictionary_$_AFCollectionUtilities
- __OBJC_$_CATEGORY_NSNull_$_AFBundleResourceSupport
- __OBJC_$_CATEGORY_NSString_$_AFPreferences
- __OBJC_$_CATEGORY_NSURL_$_AFBundleResourceSupport
- __OBJC_$_CATEGORY_SAUIAssistantUtteranceView_$_AssistantAdditions
- __OBJC_$_CLASS_METHODS_AFVoiceInfo(AFLocalizationAdditions|SiriTTSServiceAdditions|VSAdditions)
- __OBJC_$_CLASS_METHODS_NSString(AFPreferences|AssistantServices|AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription)
- __OBJC_$_CLASS_METHODS_NSURL(AFBundleResourceSupport|AMOSExtensions|AFSecurityDigestibleChunksProvider|STSiriMessage)
- __OBJC_$_INSTANCE_METHODS_AFClockAlarmSnapshot(Utility|AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_$_INSTANCE_METHODS_AFClockTimer(ClockItem|AFClockTimerMutability)
- __OBJC_$_INSTANCE_METHODS_AFClockTimerSnapshot(Utility|AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_$_INSTANCE_METHODS_AFCompanionDeviceInfo(AFCompanionDeviceInfoMutability)
- __OBJC_$_INSTANCE_METHODS_AFLocationSnapshot(Ace|AFLocationSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_$_INSTANCE_METHODS_AFPeerInfo(BackwardCompatibility|ShortDescription|AFPeerInfoMutability)
- __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(AFLocalizationAdditions|SiriTTSServiceAdditions|VSAdditions)
- __OBJC_$_INSTANCE_METHODS_AceObject(AssistantAdditions|AFSecurityDigestibleChunksProvider|AnalyticsContextVending)
- __OBJC_$_INSTANCE_METHODS_NSArray(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
- __OBJC_$_INSTANCE_METHODS_NSDate(AssistantAdditions|AFSecurityDigestibleChunksProvider)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
- __OBJC_$_INSTANCE_METHODS_NSNull(AFBundleResourceSupport|AFSecurityDigestibleChunksProvider)
- __OBJC_$_INSTANCE_METHODS_NSString(AFPreferences|AssistantServices|AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription)
- __OBJC_$_INSTANCE_METHODS_NSURL(AFBundleResourceSupport|AMOSExtensions|AFSecurityDigestibleChunksProvider|STSiriMessage)
- __OBJC_$_INSTANCE_METHODS_SAUIAssistantUtteranceView(AssistantAdditions|ClientFeedbackPresented|AnalyticsContextVending)
- __OBJC_CLASS_PROTOCOLS_$_AFClockAlarmSnapshot(Utility|AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_CLASS_PROTOCOLS_$_AFClockTimer(ClockItem|AFClockTimerMutability)
- __OBJC_CLASS_PROTOCOLS_$_AFClockTimerSnapshot(Utility|AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_CLASS_PROTOCOLS_$_AFLocationSnapshot(Ace|AFLocationSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_CLASS_PROTOCOLS_$_AceObject(AssistantAdditions|AFSecurityDigestibleChunksProvider|AnalyticsContextVending)
- __OBJC_CLASS_PROTOCOLS_$_NSArray(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
- __OBJC_CLASS_PROTOCOLS_$_NSDate(AssistantAdditions|AFSecurityDigestibleChunksProvider)
- __OBJC_CLASS_PROTOCOLS_$_NSDictionary(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
- __OBJC_CLASS_PROTOCOLS_$_NSNull(AFBundleResourceSupport|AFSecurityDigestibleChunksProvider)
- __OBJC_CLASS_PROTOCOLS_$_NSString(AFPreferences|AssistantServices|AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription)
- __OBJC_CLASS_PROTOCOLS_$_NSURL(AFBundleResourceSupport|AMOSExtensions|AFSecurityDigestibleChunksProvider|STSiriMessage)
- ___211-[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:]_block_invoke
- ___AFIsHorseman_block_invoke
- ___block_descriptor_100_e8_32s40s48s56s64s72s80s88s_e41_v16?0"<AFCompanionDeviceInfoMutating>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_48_e8_32bs40w_e5_v8?0ls32l8w40l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_82_e8_32s40s48s56bs_e33_v16?0"AceObject<SAAceCommand>"8ls32l8s56l8s40l8s48l8
- ___block_descriptor_90_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- _objc_msgSend$cacheEntitlement:forPID:bundleID:
- _objc_msgSend$fromDictionary:
- _objc_msgSend$hasEntitlement:forPID:
- _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:
- _uuid_clear
- _xpc_get_instance
CStrings:
+ "%@ {assistantID = %@, speechID = %@, idsIdentifier = %@, productPrefix = %@, aceHost = %@, syncMetadata = %@, syncMetadataCapability = %@, peerToPeerHandoffCapability = %@, muxSupportCapability = %@, meDevice = %@, siriLanguage = %@, companionName = %@, buildVersion = %@, linwoodEnabled = %@}"
+ "%s Error in isRecognizeMyVoiceEnabledForAnyUser:%@"
+ "%s Is Medoc Supported? %d"
+ "%s Overriding SAE as supported as Linwood is supported"
+ "%s The requestId=%@ is malformed, unable to log ServerExecutionValuesReported"
+ "%s [rdar://178756283] AFConnection receive SAUIAddViews aceId=%@ views.count=%lu isInterstitial=%d"
+ "%s [rdar://178756283] AFConnection receive SAUIStreamChunk streamId=%@ streamStage=%@ aceId=%@ commands=%@"
+ "%s _AFPreferencesAnnouncementPlatformOverride: platform=%ld, isValidAndSpecified=%d"
+ "%s isMediaEntitySyncDisabled=true because Siri/disable_media_entity_sync FF is on"
+ "%s isMedocSupported = %d, deviceSupportsGenerativeModelSystems = %d, linwoodSupported = %d, isNLRouterFeatureEnabled = %d, deviceSupportsSAEByDeviceCapabilityAndFeatureFlags = %d"
+ "%s notifyAppLaunchWillBePresentedToUser: {_uufrID: %llu, _uufrIntervalEnded: %d}"
+ "%s visualIntelligenceRestricted = 1 (no persisted AFSiriAvailability)"
+ "+[AFSiriAvailability fromPreferences]"
+ ", myriadElectionIdentity = %@"
+ "-[AFConnection _endUsefulUserFacingResultsIntervalIfNeeded]"
+ "-[AFConnection notifyAppLaunchWillBePresentedToUser]"
+ "-[AFConnection siriDidBecomeEffectivelyActive]"
+ "-[AFConnection siriDidBecomeEffectivelyInactive]"
+ "-[AFMultiUserConnection isRecognizeMyVoiceEnabledForAnyUser:]"
+ "-[AFMultiUserConnection isRecognizeMyVoiceEnabledForAnyUser:]_block_invoke_2"
+ "-[AFSettingsConnection armAnnounceOverrideFollowUpText:reply:]_block_invoke"
+ "-[AFSettingsConnection forceWeeklyCloudKitSyncWithCompletion:]_block_invoke"
+ "-[AFSiriAnnounceWorkoutVoiceFeedbackRequest performRequestWithResultCompletion:]"
+ "<%@ aceId=%@>"
+ "<%@: %p; isAvailable: %@; siriLocale: %@; desiredOrchestrationMode: %@; desiredOrchestrationModeIfEnabled: %@; unavailabilityReasons: %@; linwoodEverAvailable: %@; bootUUID: %@; fromCurrentBoot: %@>"
+ "<SAUIAddViews aceId=%@ views.count=%lu>"
+ "AFCompanionDeviceInfo::buildVersion"
+ "AFCompanionDeviceInfo::linwoodEnabled"
+ "AFDaemonWillExitCleanlyNotification"
+ "AFDeviceSupportsMedoc"
+ "AFLocalTurnStatusServiceErrorDomain"
+ "AFSiriAvailability {\n  isAvailable: %@\n  siriLocale: %@\n  desiredOrchestrationMode: %@\n  desiredOrchestrationModeIfEnabled: %@\n  unavailabilityReasons: %@\n  linwoodEverAvailable: %@\n  bootUUID: %@\n  fromCurrentBoot: %@\n}"
+ "Announcement Platform Override"
+ "Block %@ argument %lu is type '%s'; AFMultiArgumentSafetyBlock dispatches object arguments only."
+ "GMSEnabled"
+ "Odeon Proxy Voice Trigger"
+ "Pull Down Gesture"
+ "TC_CLIENT_EVENT"
+ "[]"
+ "_AFPreferencesAnnouncementPlatformOverride"
+ "_applicationProcessIdentifier"
+ "_myriadElectionIdentity"
+ "audioInterrupted"
+ "ck_cache_mirrored_tokens"
+ "com.apple.siri.local-turn-status"
+ "continuous_conversation_homepod"
+ "daemonUnavailable"
+ "disable_ace_sync"
+ "inopportune"
+ "linwoodEnabled"
+ "muted"
+ "notificationsDisabled"
+ "routeUnavailable"
+ "selectsAll"
+ "serializationFailed"
+ "siriBusy"
+ "siri_availability_over_xpc"
+ "siri_capabilities_settle_coalescing_disabled"
+ "timedOut"
+ "v16@?0@\"AFSiriAvailability\"8"
+ "v24@?0Q8@\"NSString\"16"
- "%@ {assistantID = %@, speechID = %@, idsIdentifier = %@, productPrefix = %@, aceHost = %@, syncMetadata = %@, syncMetadataCapability = %@, peerToPeerHandoffCapability = %@, muxSupportCapability = %@, meDevice = %@, siriLanguage = %@, companionName = %@}"
- "%s Overriding SAE as enabled on device that is otherwise unsupported"
- "%s isMedocSupported = %d, deviceSupportsGenerativeModelSystems = %d, overrideEnabled = %d, isNLRouterFeatureEnabled = %d, deviceSupportsSAEByDeviceCapabilityAndFeatureFlags = %d"
- "+[AFSiriAvailability fromDictionary:]"
- "-[AFSiriAnnounceWorkoutVoiceFeedbackRequest performRequestWithCompletion:]"
- "<%@: %p; isAvailable: %@; siriLocale: %@; desiredOrchestrationMode: %@; desiredOrchestrationModeIfEnabled: %@; unavailabilityReasons: %@; linwoodEverAvailable:%@; bootUUID:%@ fromCurrentBoot:%@>"
- "AFSiriAvailability {\n  isAvailable: %@\n  siriLocale: %@\n  desiredOrchestrationMode: %@\n  desiredOrchestrationModeIfEnabled: %@\n  unavailabilityReasons: %@\n  linwoodEverAvailable:%@  bootUUID: %@\n  fromCurrentBoot: %@\n}"
- "hints"
- "latency_response"
- "siriLatencyResponse"
```
