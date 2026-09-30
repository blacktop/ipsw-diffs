## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices`

```diff

-3600.68.61.14.6
-  __TEXT.__text: 0x19b2b8
-  __TEXT.__objc_methlist: 0x1ec7c
+3605.23.1.4.1
+  __TEXT.__text: 0x19d828
+  __TEXT.__objc_methlist: 0x1ef0c
   __TEXT.__const: 0x3f0
   __TEXT.__dlopen_cstrs: 0x421
-  __TEXT.__gcc_except_tab: 0x1f98
-  __TEXT.__cstring: 0x3b0b5
-  __TEXT.__oslogstring: 0xeb73
+  __TEXT.__gcc_except_tab: 0x1fb8
+  __TEXT.__cstring: 0x3b683
+  __TEXT.__oslogstring: 0xee0c
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x9790
+  __TEXT.__unwind_info: 0x9870
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x41c0
-  __DATA_CONST.__objc_classlist: 0xef0
+  __DATA_CONST.__const: 0x4288
+  __DATA_CONST.__objc_classlist: 0xef8
   __DATA_CONST.__objc_catlist: 0x2a0
-  __DATA_CONST.__objc_protolist: 0x5d8
+  __DATA_CONST.__objc_protolist: 0x5e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbc20
-  __DATA_CONST.__objc_protorefs: 0x178
-  __DATA_CONST.__objc_superrefs: 0xf08
-  __DATA_CONST.__objc_arraydata: 0x23a0
-  __DATA_CONST.__got: 0x1638
-  __AUTH_CONST.__const: 0x8270
-  __AUTH_CONST.__cfstring: 0x27a80
-  __AUTH_CONST.__objc_const: 0x35fb0
-  __AUTH_CONST.__objc_intobj: 0x2628
-  __AUTH_CONST.__objc_dictobj: 0xcf8
+  __DATA_CONST.__objc_selrefs: 0xbd40
+  __DATA_CONST.__objc_protorefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0xf10
+  __DATA_CONST.__objc_arraydata: 0x2440
+  __DATA_CONST.__got: 0x1658
+  __AUTH_CONST.__const: 0x8300
+  __AUTH_CONST.__cfstring: 0x27dc0
+  __AUTH_CONST.__objc_const: 0x36268
+  __AUTH_CONST.__objc_intobj: 0x2700
+  __AUTH_CONST.__objc_dictobj: 0xd20
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH.__objc_data: 0x85c0
+  __AUTH_CONST.__auth_got: 0x990
+  __AUTH.__objc_data: 0x8610
   __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0x2550
-  __DATA.__data: 0x4738
+  __DATA.__objc_ivar: 0x2570
+  __DATA.__data: 0x4798
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xfa0
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x1e9
+  __DATA_DIRTY.__bss: 0x1e0
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11913
-  Symbols:   26247
-  CStrings:  8301
+  Functions: 11979
+  Symbols:   26378
+  CStrings:  8353
 
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
+ AFIsHomePod.isHomePod
+ AFIsHomePod.onceToken
+ AFSiriWorkoutVoiceFeedbackResultGetFromName.map
+ AFSiriWorkoutVoiceFeedbackResultGetFromName.onceToken
+ GCC_except_table1000
+ GCC_except_table10040
+ GCC_except_table10103
+ GCC_except_table10106
+ GCC_except_table10110
+ GCC_except_table10129
+ GCC_except_table10143
+ GCC_except_table10217
+ GCC_except_table10275
+ GCC_except_table10301
+ GCC_except_table10566
+ GCC_except_table10695
+ GCC_except_table10745
+ GCC_except_table10839
+ GCC_except_table10961
+ GCC_except_table10963
+ GCC_except_table10966
+ GCC_except_table10975
+ GCC_except_table11037
+ GCC_except_table11052
+ GCC_except_table11077
+ GCC_except_table11083
+ GCC_except_table11233
+ GCC_except_table11237
+ GCC_except_table11239
+ GCC_except_table11242
+ GCC_except_table11248
+ GCC_except_table11255
+ GCC_except_table1136
+ GCC_except_table11462
+ GCC_except_table11786
+ GCC_except_table11927
+ GCC_except_table11930
+ GCC_except_table11932
+ GCC_except_table1203
+ GCC_except_table1213
+ GCC_except_table1334
+ GCC_except_table1336
+ GCC_except_table1519
+ GCC_except_table1556
+ GCC_except_table1564
+ GCC_except_table1570
+ GCC_except_table1590
+ GCC_except_table1596
+ GCC_except_table1599
+ GCC_except_table1966
+ GCC_except_table2080
+ GCC_except_table2213
+ GCC_except_table2335
+ GCC_except_table2348
+ GCC_except_table2349
+ GCC_except_table2363
+ GCC_except_table2372
+ GCC_except_table2375
+ GCC_except_table2381
+ GCC_except_table2428
+ GCC_except_table2430
+ GCC_except_table2432
+ GCC_except_table245
+ GCC_except_table2450
+ GCC_except_table2456
+ GCC_except_table2499
+ GCC_except_table2511
+ GCC_except_table253
+ GCC_except_table259
+ GCC_except_table2653
+ GCC_except_table273
+ GCC_except_table2743
+ GCC_except_table2797
+ GCC_except_table3023
+ GCC_except_table3024
+ GCC_except_table3221
+ GCC_except_table3282
+ GCC_except_table3498
+ GCC_except_table3501
+ GCC_except_table3506
+ GCC_except_table3510
+ GCC_except_table3524
+ GCC_except_table3571
+ GCC_except_table3577
+ GCC_except_table3583
+ GCC_except_table3676
+ GCC_except_table3680
+ GCC_except_table372
+ GCC_except_table3790
+ GCC_except_table3853
+ GCC_except_table3855
+ GCC_except_table3857
+ GCC_except_table3859
+ GCC_except_table3873
+ GCC_except_table3879
+ GCC_except_table390
+ GCC_except_table396
+ GCC_except_table4004
+ GCC_except_table4008
+ GCC_except_table4013
+ GCC_except_table4385
+ GCC_except_table4400
+ GCC_except_table4407
+ GCC_except_table4423
+ GCC_except_table4524
+ GCC_except_table4562
+ GCC_except_table4563
+ GCC_except_table4564
+ GCC_except_table4589
+ GCC_except_table4613
+ GCC_except_table4973
+ GCC_except_table4978
+ GCC_except_table4981
+ GCC_except_table4984
+ GCC_except_table4987
+ GCC_except_table4990
+ GCC_except_table4993
+ GCC_except_table4996
+ GCC_except_table4999
+ GCC_except_table5002
+ GCC_except_table5173
+ GCC_except_table5176
+ GCC_except_table5249
+ GCC_except_table5409
+ GCC_except_table5511
+ GCC_except_table5702
+ GCC_except_table5707
+ GCC_except_table5835
+ GCC_except_table602
+ GCC_except_table6052
+ GCC_except_table6058
+ GCC_except_table6059
+ GCC_except_table6063
+ GCC_except_table6253
+ GCC_except_table6426
+ GCC_except_table6454
+ GCC_except_table6551
+ GCC_except_table6555
+ GCC_except_table6559
+ GCC_except_table656
+ GCC_except_table6588
+ GCC_except_table7096
+ GCC_except_table7109
+ GCC_except_table7113
+ GCC_except_table7125
+ GCC_except_table7129
+ GCC_except_table7242
+ GCC_except_table7244
+ GCC_except_table7296
+ GCC_except_table7340
+ GCC_except_table7685
+ GCC_except_table7692
+ GCC_except_table7698
+ GCC_except_table7700
+ GCC_except_table7702
+ GCC_except_table7737
+ GCC_except_table7739
+ GCC_except_table7745
+ GCC_except_table7751
+ GCC_except_table7755
+ GCC_except_table7761
+ GCC_except_table7764
+ GCC_except_table7766
+ GCC_except_table7771
+ GCC_except_table7773
+ GCC_except_table7778
+ GCC_except_table7790
+ GCC_except_table7793
+ GCC_except_table7807
+ GCC_except_table7809
+ GCC_except_table7811
+ GCC_except_table7813
+ GCC_except_table7815
+ GCC_except_table7817
+ GCC_except_table7862
+ GCC_except_table7888
+ GCC_except_table7945
+ GCC_except_table7978
+ GCC_except_table8356
+ GCC_except_table859
+ GCC_except_table862
+ GCC_except_table8644
+ GCC_except_table869
+ GCC_except_table8843
+ GCC_except_table8851
+ GCC_except_table8909
+ GCC_except_table9277
+ GCC_except_table9281
+ GCC_except_table9326
+ GCC_except_table9332
+ GCC_except_table9359
+ GCC_except_table9366
+ GCC_except_table9576
+ GCC_except_table9650
+ GCC_except_table9661
+ GCC_except_table9694
+ GCC_except_table9697
+ GCC_except_table9773
+ GCC_except_table9777
+ GCC_except_table9787
+ GCC_except_table9798
+ GCC_except_table9813
+ GCC_except_table9898
+ GCC_except_table9900
+ GCC_except_table9924
+ OBJC_IVAR_$_AFCompanionDeviceInfo._buildVersion
+ OBJC_IVAR_$_AFCompanionDeviceInfo._linwoodEnabled
+ OBJC_IVAR_$_AFConnectionEntitlementCache._bundleIDToKeyMap
+ OBJC_IVAR_$_AFDictationOptions._applicationProcessIdentifier
+ OBJC_IVAR_$_AFDisambiguationOutcomeDescriptor._selectsAll
+ OBJC_IVAR_$_AFLocalTurnStatusService._connection
+ OBJC_IVAR_$_AFSpeechRequestOptions._myriadElectionIdentity
+ OBJC_IVAR_$__AFCompanionDeviceInfoMutation._buildVersion
+ OBJC_IVAR_$__AFCompanionDeviceInfoMutation._linwoodEnabled
+ _AFDaemonIsExitingCleanly
+ _AFDaemonWillExitCleanlyNotification
+ _AFIsHomePod
+ _AFResetDaemonIsExitingCleanlyForTesting
+ _AFSimulateDaemonWillExitCleanlyForTesting
+ _AFSiriWorkoutVoiceFeedbackResultGetFromName
+ _AFSiriWorkoutVoiceFeedbackResultGetIsValid
+ _AFSiriWorkoutVoiceFeedbackResultGetIsValidAndSpecified
+ _AFSiriWorkoutVoiceFeedbackResultGetName
+ _OBJC_CLASS_$_AFLocalTurnStatusService
+ _OBJC_CLASS_$_SAUIStreamChunk
+ _OBJC_CLASS_$_SCDAElectionIdentity
+ _OBJC_CLASS_$_SCDAFeatureFlags
+ _OBJC_METACLASS_$_AFLocalTurnStatusService
+ __51-[AFLocalTurnStatusService currentLocalTurnStatus:]_block_invoke
+ __62-[AFSettingsConnection forceWeeklyCloudKitSyncWithCompletion:]_block_invoke
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
+ __OBJC_$_CLASS_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions)
+ __OBJC_$_CLASS_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription|AFPreferences|AssistantServices)
+ __OBJC_$_CLASS_METHODS_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
+ __OBJC_$_INSTANCE_METHODS_AFClockAlarmSnapshot(AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
+ __OBJC_$_INSTANCE_METHODS_AFClockTimer(AFClockTimerMutability|ClockItem)
+ __OBJC_$_INSTANCE_METHODS_AFClockTimerSnapshot(AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot|Utility)
+ __OBJC_$_INSTANCE_METHODS_AFCompanionDeviceInfo(BackwardCompatibility|AFCompanionDeviceInfoMutability)
+ __OBJC_$_INSTANCE_METHODS_AFLocalTurnStatusService
+ __OBJC_$_INSTANCE_METHODS_AFLocationSnapshot(AFLocationSnapshotMutability|ShortDescription|ContextSnapshot|Ace)
+ __OBJC_$_INSTANCE_METHODS_AFPeerInfo(ShortDescription|BackwardCompatibility|AFPeerInfoMutability)
+ __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions)
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
+ ___block_descriptor_109_e8_32s40s48s56s64s72s80s88s96s_e41_v16?0"<AFCompanionDeviceInfoMutating>"8l
+ ___block_descriptor_40_e8_32bs_e21_v24?0Q8"NSString"16l
+ ___block_descriptor_40_e8_32r_e28_v16?0"AFSiriAvailability"8l
+ ___block_descriptor_48_e8_32bs40r_e28_v16?0"AFSiriAvailability"8l
+ ___block_descriptor_90_e8_32s40s48s56s64bs_e33_v16?0"AceObject<SAAceCommand>"8l
+ ___block_descriptor_98_e8_32s40s48s56s64s72bs_e5_v8?0l
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
- AFIsHorseman.isHorseman
- AFIsHorseman.onceToken
- AFProcessGetInstanceUUID.instanceUUID
- GCC_except_table10022
- GCC_except_table10027
- GCC_except_table10028
- GCC_except_table10032
- GCC_except_table10222
- GCC_except_table10395
- GCC_except_table10423
- GCC_except_table10520
- GCC_except_table10524
- GCC_except_table10528
- GCC_except_table10557
- GCC_except_table10905
- GCC_except_table10907
- GCC_except_table10910
- GCC_except_table10919
- GCC_except_table10980
- GCC_except_table10995
- GCC_except_table11020
- GCC_except_table11026
- GCC_except_table11170
- GCC_except_table11174
- GCC_except_table11176
- GCC_except_table11179
- GCC_except_table11185
- GCC_except_table11192
- GCC_except_table1124
- GCC_except_table11396
- GCC_except_table11720
- GCC_except_table11861
- GCC_except_table11864
- GCC_except_table11866
- GCC_except_table1191
- GCC_except_table1201
- GCC_except_table1494
- GCC_except_table1509
- GCC_except_table1513
- GCC_except_table1525
- GCC_except_table1529
- GCC_except_table1634
- GCC_except_table1636
- GCC_except_table1688
- GCC_except_table1732
- GCC_except_table2078
- GCC_except_table2085
- GCC_except_table2091
- GCC_except_table2093
- GCC_except_table2095
- GCC_except_table2130
- GCC_except_table2132
- GCC_except_table2138
- GCC_except_table2144
- GCC_except_table2148
- GCC_except_table2152
- GCC_except_table2155
- GCC_except_table2157
- GCC_except_table2164
- GCC_except_table2166
- GCC_except_table2171
- GCC_except_table2183
- GCC_except_table2186
- GCC_except_table2200
- GCC_except_table2202
- GCC_except_table2204
- GCC_except_table2206
- GCC_except_table2208
- GCC_except_table2210
- GCC_except_table2255
- GCC_except_table2281
- GCC_except_table2338
- GCC_except_table238
- GCC_except_table246
- GCC_except_table252
- GCC_except_table266
- GCC_except_table2745
- GCC_except_table3032
- GCC_except_table3231
- GCC_except_table3239
- GCC_except_table3297
- GCC_except_table363
- GCC_except_table3666
- GCC_except_table3670
- GCC_except_table3715
- GCC_except_table3723
- GCC_except_table3750
- GCC_except_table3758
- GCC_except_table381
- GCC_except_table387
- GCC_except_table3965
- GCC_except_table4039
- GCC_except_table4050
- GCC_except_table4083
- GCC_except_table4086
- GCC_except_table4163
- GCC_except_table4167
- GCC_except_table4177
- GCC_except_table4188
- GCC_except_table4203
- GCC_except_table4288
- GCC_except_table4290
- GCC_except_table4314
- GCC_except_table4429
- GCC_except_table4492
- GCC_except_table4499
- GCC_except_table4518
- GCC_except_table4533
- GCC_except_table4607
- GCC_except_table4665
- GCC_except_table4691
- GCC_except_table4955
- GCC_except_table5081
- GCC_except_table5130
- GCC_except_table5224
- GCC_except_table5332
- GCC_except_table5334
- GCC_except_table5516
- GCC_except_table5553
- GCC_except_table5560
- GCC_except_table5564
- GCC_except_table5584
- GCC_except_table5590
- GCC_except_table5593
- GCC_except_table591
- GCC_except_table5960
- GCC_except_table6074
- GCC_except_table6205
- GCC_except_table6327
- GCC_except_table6340
- GCC_except_table6341
- GCC_except_table6353
- GCC_except_table6360
- GCC_except_table6361
- GCC_except_table6364
- GCC_except_table6370
- GCC_except_table6417
- GCC_except_table6419
- GCC_except_table6421
- GCC_except_table6439
- GCC_except_table644
- GCC_except_table6445
- GCC_except_table6488
- GCC_except_table6500
- GCC_except_table6642
- GCC_except_table6730
- GCC_except_table6784
- GCC_except_table7010
- GCC_except_table7011
- GCC_except_table7208
- GCC_except_table7268
- GCC_except_table7482
- GCC_except_table7485
- GCC_except_table7490
- GCC_except_table7494
- GCC_except_table7508
- GCC_except_table7555
- GCC_except_table7561
- GCC_except_table7567
- GCC_except_table7660
- GCC_except_table7664
- GCC_except_table7774
- GCC_except_table7837
- GCC_except_table7839
- GCC_except_table7841
- GCC_except_table7843
- GCC_except_table7857
- GCC_except_table7863
- GCC_except_table7986
- GCC_except_table7990
- GCC_except_table7995
- GCC_except_table8364
- GCC_except_table8379
- GCC_except_table8386
- GCC_except_table8402
- GCC_except_table847
- GCC_except_table8471
- GCC_except_table850
- GCC_except_table8500
- GCC_except_table8538
- GCC_except_table8539
- GCC_except_table8540
- GCC_except_table8565
- GCC_except_table857
- GCC_except_table8589
- GCC_except_table8949
- GCC_except_table8954
- GCC_except_table8957
- GCC_except_table8960
- GCC_except_table8963
- GCC_except_table8966
- GCC_except_table8969
- GCC_except_table8972
- GCC_except_table9143
- GCC_except_table9146
- GCC_except_table9219
- GCC_except_table9379
- GCC_except_table9481
- GCC_except_table9672
- GCC_except_table9677
- GCC_except_table9805
- GCC_except_table988
- OBJC_IVAR_$_AFConnectionEntitlementCache._bundleIDToPIDMap
- __OBJC_$_CATEGORY_AceObject_$_AssistantAdditions
- __OBJC_$_CATEGORY_NSArray_$_AFCollectionUtilities
- __OBJC_$_CATEGORY_NSDate_$_AssistantAdditions
- __OBJC_$_CATEGORY_NSDictionary_$_AFCollectionUtilities
- __OBJC_$_CATEGORY_NSNull_$_AFBundleResourceSupport
- __OBJC_$_CATEGORY_NSString_$_AFPreferences
- __OBJC_$_CATEGORY_NSURL_$_AFBundleResourceSupport
- __OBJC_$_CATEGORY_SAUIAssistantUtteranceView_$_AssistantAdditions
- __OBJC_$_CLASS_METHODS_AFVoiceInfo(AFLocalizationAdditions|SiriTTSServiceAdditions)
- __OBJC_$_CLASS_METHODS_NSString(AFPreferences|AssistantServices|AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription)
- __OBJC_$_CLASS_METHODS_NSURL(AFBundleResourceSupport|AMOSExtensions|AFSecurityDigestibleChunksProvider|STSiriMessage)
- __OBJC_$_INSTANCE_METHODS_AFClockAlarmSnapshot(Utility|AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_$_INSTANCE_METHODS_AFClockTimer(ClockItem|AFClockTimerMutability)
- __OBJC_$_INSTANCE_METHODS_AFClockTimerSnapshot(Utility|AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_$_INSTANCE_METHODS_AFCompanionDeviceInfo(AFCompanionDeviceInfoMutability)
- __OBJC_$_INSTANCE_METHODS_AFLocationSnapshot(Ace|AFLocationSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_$_INSTANCE_METHODS_AFPeerInfo(BackwardCompatibility|ShortDescription|AFPeerInfoMutability)
- __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(AFLocalizationAdditions|SiriTTSServiceAdditions)
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
- ___block_descriptor_100_e8_32s40s48s56s64s72s80s88s_e41_v16?0"<AFCompanionDeviceInfoMutating>"8l
- ___block_descriptor_82_e8_32s40s48s56bs_e33_v16?0"AceObject<SAAceCommand>"8l
- ___block_descriptor_90_e8_32s40s48s56s64bs_e5_v8?0l
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
+ "AFVisualIntelligenceCameraRestricted"
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
