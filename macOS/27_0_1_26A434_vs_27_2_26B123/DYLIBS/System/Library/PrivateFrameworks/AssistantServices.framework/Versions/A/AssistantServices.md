## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices`

```diff

-3600.68.61.14.6
-  __TEXT.__text: 0x1a5cf8
-  __TEXT.__objc_methlist: 0x1ec7c
+3605.31.1.14.2
+  __TEXT.__text: 0x1aa05c
+  __TEXT.__objc_methlist: 0x1f104
   __TEXT.__const: 0x3f0
   __TEXT.__dlopen_cstrs: 0x421
-  __TEXT.__gcc_except_tab: 0x1f98
-  __TEXT.__cstring: 0x3b0b5
-  __TEXT.__oslogstring: 0xeb73
+  __TEXT.__gcc_except_tab: 0x1fc0
+  __TEXT.__cstring: 0x3ba11
+  __TEXT.__oslogstring: 0xef74
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x7940
+  __TEXT.__unwind_info: 0x7a40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x41c0
-  __DATA_CONST.__objc_classlist: 0xef0
+  __DATA_CONST.__const: 0x42e0
+  __DATA_CONST.__objc_classlist: 0xef8
   __DATA_CONST.__objc_catlist: 0x2a0
-  __DATA_CONST.__objc_protolist: 0x5d8
+  __DATA_CONST.__objc_protolist: 0x5f8
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
+  __DATA_CONST.__objc_selrefs: 0xbe20
+  __DATA_CONST.__objc_protorefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0xf10
+  __DATA_CONST.__objc_arraydata: 0x2450
+  __DATA_CONST.__got: 0x1660
+  __AUTH_CONST.__const: 0x8370
+  __AUTH_CONST.__cfstring: 0x27fe0
+  __AUTH_CONST.__objc_const: 0x36530
+  __AUTH_CONST.__objc_intobj: 0x2730
+  __AUTH_CONST.__objc_dictobj: 0xd20
   __AUTH_CONST.__objc_arrayobj: 0x5d0
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH_CONST.__auth_got: 0x990
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x85c0
+  __AUTH.__objc_data: 0x84a8
   __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0x2550
-  __DATA.__data: 0x4738
-  __DATA.__bss: 0xed8
+  __DATA.__objc_ivar: 0x259c
+  __DATA.__data: 0x48c0
+  __DATA.__bss: 0xf30
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0xfa0
+  __DATA_DIRTY.__objc_data: 0x1108
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x1e9
+  __DATA_DIRTY.__bss: 0x1b8
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 11913
-  Symbols:   26247
-  CStrings:  8301
+  Functions: 12026
+  Symbols:   26475
+  CStrings:  8386
 
Symbols:
+ +[AFFeatureFlags(SWEFeatureFlags) isAceSyncDisabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isAppExclusionsEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isCloudKitCacheMirroredChangeTokensEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isLinwoodModalityConnectionSkipEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isSiriCapabilitiesSettleCoalescingDisabled]
+ +[AFFeatureFlags(SWEFeatureFlags) siriAvailabilityOverXPCEnabled]
+ -[AFCompanionDeviceInfo buildVersion]
+ -[AFCompanionDeviceInfo ifpCapableDevice]
+ -[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:ifpCapableDevice:siriAvailability:]
+ -[AFCompanionDeviceInfo linwoodCapableDevice]
+ -[AFCompanionDeviceInfo linwoodEnabled]
+ -[AFCompanionDeviceInfo siriAvailability]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:]
+ -[AFCompanionDeviceInfo(BackwardCompatibility) initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:ifpCapableDevice:]
+ -[AFCompanionDeviceInfo(SiriAvailability) createSiriAvailability]
+ -[AFConnection _cleanupRoutingStandby]
+ -[AFConnection _endUsefulUserFacingResultsIntervalIfNeeded]
+ -[AFConnection _replyMissingDelegateMethodTo:]
+ -[AFConnection _resetSpeechTimingForSpeechRequest:options:systemUptime:]
+ -[AFConnection notifyAppLaunchWillBePresentedToUser]
+ -[AFConnection scdaStandbyDidBegin]
+ -[AFConnection scdaStandbyDidEndAsWon:]
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
+ -[AFPreferences assistantEnabledBeforeRestrictionIsCurrentVersion]
+ -[AFPreferences fetchUseWithSiriEnabledForApp:completion:]
+ -[AFPreferences fetchUseWithSiriStateForApp:completion:]
+ -[AFPreferences updateUseWithSiriEnabled:forApp:]
+ -[AFRequestInfo myriadElectionIdentity]
+ -[AFSettingsConnection armAnnounceOverrideFollowUpText:reply:]
+ -[AFSettingsConnection forceWeeklyCloudKitSyncWithCompletion:]
+ -[AFSettingsConnection(Internal) _syncDataWithAnchorKeys:forceReset:reason:completionWithError:]
+ -[AFSiriAnnounceWorkoutVoiceFeedbackRequest performRequestWithResultCompletion:]
+ -[AFSiriAvailability createDictionaryExcludingBootSession]
+ -[AFSiriAvailability initWithDictionary:]
+ -[AFSiriAvailability initWithSiriLanguageCode:]
+ -[AFSiriAvailability isLinwoodAccessRestricted]
+ -[AFSiriAvailability isLinwoodGMSAvailable]
+ -[AFSiriAvailability isLinwoodGMSEnabled]
+ -[AFSiriCapabilitiesServiceClient siriAvailability:]
+ -[AFSiriCapabilitiesServiceClient siriAvailabilitySync]
+ -[AFSpeechRequestOptions isReplyToSiriPrompt]
+ -[AFSpeechRequestOptions myriadElectionIdentity]
+ -[AFSpeechRequestOptions setIsReplyToSiriPrompt:]
+ -[AFSpeechRequestOptions setMyriadElectionIdentity:]
+ -[_AFCompanionDeviceInfoMutation getBuildVersion]
+ -[_AFCompanionDeviceInfoMutation getIfpCapableDevice]
+ -[_AFCompanionDeviceInfoMutation getLinwoodCapableDevice]
+ -[_AFCompanionDeviceInfoMutation getLinwoodEnabled]
+ -[_AFCompanionDeviceInfoMutation getSiriAvailability]
+ -[_AFCompanionDeviceInfoMutation setBuildVersion:]
+ -[_AFCompanionDeviceInfoMutation setIfpCapableDevice:]
+ -[_AFCompanionDeviceInfoMutation setLinwoodCapableDevice:]
+ -[_AFCompanionDeviceInfoMutation setLinwoodEnabled:]
+ -[_AFCompanionDeviceInfoMutation setSiriAvailability:]
+ AFIsHomePod.isHomePod
+ AFIsHomePod.onceToken
+ AFIsJ265.isJ265
+ AFIsJ265.onceToken
+ AFSiriWorkoutVoiceFeedbackResultGetFromName.map
+ AFSiriWorkoutVoiceFeedbackResultGetFromName.onceToken
+ GCC_except_table1006
+ GCC_except_table10112
+ GCC_except_table10117
+ GCC_except_table10118
+ GCC_except_table10122
+ GCC_except_table10312
+ GCC_except_table10485
+ GCC_except_table10513
+ GCC_except_table10610
+ GCC_except_table10614
+ GCC_except_table10618
+ GCC_except_table10647
+ GCC_except_table10997
+ GCC_except_table11000
+ GCC_except_table11009
+ GCC_except_table11075
+ GCC_except_table11090
+ GCC_except_table11115
+ GCC_except_table11121
+ GCC_except_table11280
+ GCC_except_table11284
+ GCC_except_table11286
+ GCC_except_table11289
+ GCC_except_table11295
+ GCC_except_table11302
+ GCC_except_table1142
+ GCC_except_table11509
+ GCC_except_table11833
+ GCC_except_table11974
+ GCC_except_table11977
+ GCC_except_table11979
+ GCC_except_table1209
+ GCC_except_table1219
+ GCC_except_table1340
+ GCC_except_table1342
+ GCC_except_table1562
+ GCC_except_table1570
+ GCC_except_table1576
+ GCC_except_table1596
+ GCC_except_table1602
+ GCC_except_table1605
+ GCC_except_table1972
+ GCC_except_table2086
+ GCC_except_table2219
+ GCC_except_table2341
+ GCC_except_table2354
+ GCC_except_table2355
+ GCC_except_table2369
+ GCC_except_table2377
+ GCC_except_table2378
+ GCC_except_table2381
+ GCC_except_table2387
+ GCC_except_table2434
+ GCC_except_table2436
+ GCC_except_table2438
+ GCC_except_table245
+ GCC_except_table2456
+ GCC_except_table2462
+ GCC_except_table2505
+ GCC_except_table2517
+ GCC_except_table253
+ GCC_except_table259
+ GCC_except_table273
+ GCC_except_table2756
+ GCC_except_table2769
+ GCC_except_table2773
+ GCC_except_table2785
+ GCC_except_table2789
+ GCC_except_table2902
+ GCC_except_table2904
+ GCC_except_table2961
+ GCC_except_table3005
+ GCC_except_table3352
+ GCC_except_table3359
+ GCC_except_table3365
+ GCC_except_table3367
+ GCC_except_table3369
+ GCC_except_table3404
+ GCC_except_table3406
+ GCC_except_table3412
+ GCC_except_table3418
+ GCC_except_table3422
+ GCC_except_table3428
+ GCC_except_table3435
+ GCC_except_table3437
+ GCC_except_table3444
+ GCC_except_table3446
+ GCC_except_table3451
+ GCC_except_table3463
+ GCC_except_table3466
+ GCC_except_table3480
+ GCC_except_table3482
+ GCC_except_table3484
+ GCC_except_table3486
+ GCC_except_table3488
+ GCC_except_table3490
+ GCC_except_table3536
+ GCC_except_table3562
+ GCC_except_table3619
+ GCC_except_table3655
+ GCC_except_table377
+ GCC_except_table396
+ GCC_except_table402
+ GCC_except_table4038
+ GCC_except_table4326
+ GCC_except_table4529
+ GCC_except_table4537
+ GCC_except_table4595
+ GCC_except_table4963
+ GCC_except_table4967
+ GCC_except_table5012
+ GCC_except_table5018
+ GCC_except_table5045
+ GCC_except_table5052
+ GCC_except_table5264
+ GCC_except_table5338
+ GCC_except_table5349
+ GCC_except_table5382
+ GCC_except_table5385
+ GCC_except_table5462
+ GCC_except_table5466
+ GCC_except_table5476
+ GCC_except_table5487
+ GCC_except_table5502
+ GCC_except_table5587
+ GCC_except_table5589
+ GCC_except_table5613
+ GCC_except_table5729
+ GCC_except_table5792
+ GCC_except_table5795
+ GCC_except_table5799
+ GCC_except_table5818
+ GCC_except_table5833
+ GCC_except_table5907
+ GCC_except_table5965
+ GCC_except_table5991
+ GCC_except_table608
+ GCC_except_table6259
+ GCC_except_table6388
+ GCC_except_table6438
+ GCC_except_table6532
+ GCC_except_table662
+ GCC_except_table6717
+ GCC_except_table6805
+ GCC_except_table6859
+ GCC_except_table7085
+ GCC_except_table7086
+ GCC_except_table7283
+ GCC_except_table7343
+ GCC_except_table7557
+ GCC_except_table7560
+ GCC_except_table7565
+ GCC_except_table7569
+ GCC_except_table7583
+ GCC_except_table7630
+ GCC_except_table7636
+ GCC_except_table7642
+ GCC_except_table7735
+ GCC_except_table7739
+ GCC_except_table7849
+ GCC_except_table7912
+ GCC_except_table7914
+ GCC_except_table7916
+ GCC_except_table7918
+ GCC_except_table7932
+ GCC_except_table7938
+ GCC_except_table8063
+ GCC_except_table8067
+ GCC_except_table8072
+ GCC_except_table8444
+ GCC_except_table8459
+ GCC_except_table8466
+ GCC_except_table8482
+ GCC_except_table8553
+ GCC_except_table8582
+ GCC_except_table8620
+ GCC_except_table8621
+ GCC_except_table8622
+ GCC_except_table8647
+ GCC_except_table865
+ GCC_except_table8671
+ GCC_except_table868
+ GCC_except_table875
+ GCC_except_table9031
+ GCC_except_table9036
+ GCC_except_table9039
+ GCC_except_table9042
+ GCC_except_table9045
+ GCC_except_table9048
+ GCC_except_table9051
+ GCC_except_table9054
+ GCC_except_table9057
+ GCC_except_table9060
+ GCC_except_table9233
+ GCC_except_table9236
+ GCC_except_table9309
+ GCC_except_table9469
+ GCC_except_table9571
+ GCC_except_table9762
+ GCC_except_table9767
+ GCC_except_table9895
+ OBJC_IVAR_$_AFCompanionDeviceInfo._buildVersion
+ OBJC_IVAR_$_AFCompanionDeviceInfo._ifpCapableDevice
+ OBJC_IVAR_$_AFCompanionDeviceInfo._linwoodCapableDevice
+ OBJC_IVAR_$_AFCompanionDeviceInfo._linwoodEnabled
+ OBJC_IVAR_$_AFCompanionDeviceInfo._siriAvailability
+ OBJC_IVAR_$_AFConnection._isInRoutingStandby
+ OBJC_IVAR_$_AFConnectionEntitlementCache._bundleIDToKeyMap
+ OBJC_IVAR_$_AFDictationOptions._applicationProcessIdentifier
+ OBJC_IVAR_$_AFDisambiguationOutcomeDescriptor._selectsAll
+ OBJC_IVAR_$_AFLocalTurnStatusService._connection
+ OBJC_IVAR_$_AFLocalization._cachedVoiceMaps
+ OBJC_IVAR_$_AFLocalization._cachedVoiceMapsSource
+ OBJC_IVAR_$_AFLocalization._voiceMapsLock
+ OBJC_IVAR_$_AFSpeechRequestOptions._isReplyToSiriPrompt
+ OBJC_IVAR_$_AFSpeechRequestOptions._myriadElectionIdentity
+ OBJC_IVAR_$__AFCompanionDeviceInfoMutation._buildVersion
+ OBJC_IVAR_$__AFCompanionDeviceInfoMutation._ifpCapableDevice
+ OBJC_IVAR_$__AFCompanionDeviceInfoMutation._linwoodCapableDevice
+ OBJC_IVAR_$__AFCompanionDeviceInfoMutation._linwoodEnabled
+ OBJC_IVAR_$__AFCompanionDeviceInfoMutation._siriAvailability
+ _AFDaemonIsExitingCleanly
+ _AFDaemonWillExitCleanlyNotification
+ _AFIsHomePod
+ _AFIsJ265
+ _AFIsWaffleiron
+ _AFMeDeviceLinwoodEnablementDidChangeNotification
+ _AFPreferencesObserveLanguageChanges.observerOnceToken
+ _AFResetDaemonIsExitingCleanlyForTesting
+ _AFSimulateDaemonWillExitCleanlyForTesting
+ _AFSiriActivationOdeonProxyVoiceTrigger
+ _AFSiriWorkoutVoiceFeedbackResultGetFromName
+ _AFSiriWorkoutVoiceFeedbackResultGetIsValid
+ _AFSiriWorkoutVoiceFeedbackResultGetIsValidAndSpecified
+ _AFSiriWorkoutVoiceFeedbackResultGetName
+ _AFUseWithSiriAvailableForApp
+ _AFUseWithSiriEnabledForApp
+ _AFUseWithSiriSetEnabled
+ _OBJC_CLASS_$_AFLocalTurnStatusService
+ _OBJC_CLASS_$_SAUIStreamChunk
+ _OBJC_CLASS_$_SCDAElectionIdentity
+ _OBJC_CLASS_$_SCDAFeatureFlags
+ _OBJC_CLASS_$_SCDAStandbyObserver
+ _OBJC_METACLASS_$_AFLocalTurnStatusService
+ __51-[AFLocalTurnStatusService currentLocalTurnStatus:]_block_invoke
+ __62-[AFSettingsConnection forceWeeklyCloudKitSyncWithCompletion:]_block_invoke
+ __AFBeginExitingCleanly
+ __AFPreferencesAnnouncementPlatformOverride
+ __AFPreferencesCachedLanguageValue
+ __AFPreferencesIsAnnouncementPlatformOverrideActive
+ __AFPreferencesLanguageCacheGenerationForTesting
+ __AFPreferencesSetAnnouncementPlatformOverride
+ __AFPreferencesSetLanguageCacheDidComputeHookForTesting
+ __AFPreferencesSetSiriPersonalContentSetting
+ __AFPreferencesSiriPersonalContentSetting
+ __OBJC_$_CATEGORY_AceObject_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSArray_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSDate_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSDictionary_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSNull_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSString_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CATEGORY_NSURL_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_CLASS_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions)
+ __OBJC_$_CLASS_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFPreferences|AssistantServices|AFSiriRequest|ShortDescription)
+ __OBJC_$_CLASS_METHODS_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
+ __OBJC_$_INSTANCE_METHODS_AFClockTimer(AFClockTimerMutability|ClockItem)
+ __OBJC_$_INSTANCE_METHODS_AFCompanionDeviceInfo(BackwardCompatibility|SiriAvailability|AFCompanionDeviceInfoMutability)
+ __OBJC_$_INSTANCE_METHODS_AFLocalTurnStatusService
+ __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(SiriTTSServiceAdditions|AFLocalizationAdditions)
+ __OBJC_$_INSTANCE_METHODS_AceObject(AFSecurityDigestibleChunksProvider|AssistantAdditions|AnalyticsContextVending)
+ __OBJC_$_INSTANCE_METHODS_NSArray(AFSecurityDigestibleChunksProvider|AFCollectionUtilities)
+ __OBJC_$_INSTANCE_METHODS_NSDate(AFSecurityDigestibleChunksProvider|AssistantAdditions)
+ __OBJC_$_INSTANCE_METHODS_NSDictionary(AFSecurityDigestibleChunksProvider|AFCollectionUtilities)
+ __OBJC_$_INSTANCE_METHODS_NSNull(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport)
+ __OBJC_$_INSTANCE_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFPreferences|AssistantServices|AFSiriRequest|ShortDescription)
+ __OBJC_$_INSTANCE_METHODS_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
+ __OBJC_$_INSTANCE_VARIABLES_AFLocalTurnStatusService
+ __OBJC_$_PROP_LIST_AFLocalTurnStatusService
+ __OBJC_$_PROP_LIST_AFPreferences
+ __OBJC_$_PROP_LIST_NSArray_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_PROP_LIST_NSDate_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_PROP_LIST_NSDictionary_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_PROP_LIST_NSString_$_AFSecurityDigestibleChunksProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFLocalTurnStatusServiceInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFPreferencesInternalProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFPreferencesProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SCDAStandbyListening
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AFLocalTurnStatusServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AFPreferencesInternalProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AFPreferencesProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SCDAStandbyListening
+ __OBJC_$_PROTOCOL_REFS_AFPreferencesInternalProviding
+ __OBJC_$_PROTOCOL_REFS_AFPreferencesProviding
+ __OBJC_$_PROTOCOL_REFS_SCDAStandbyListening
+ __OBJC_CATEGORY_PROTOCOLS_$_NSArray_$_AFSecurityDigestibleChunksProvider
+ __OBJC_CATEGORY_PROTOCOLS_$_NSDate_$_AFSecurityDigestibleChunksProvider
+ __OBJC_CATEGORY_PROTOCOLS_$_NSDictionary_$_AFSecurityDigestibleChunksProvider
+ __OBJC_CATEGORY_PROTOCOLS_$_NSString_$_AFSecurityDigestibleChunksProvider
+ __OBJC_CLASS_PROTOCOLS_$_AFClockTimer(AFClockTimerMutability|ClockItem)
+ __OBJC_CLASS_PROTOCOLS_$_AFPreferences
+ __OBJC_CLASS_PROTOCOLS_$_AceObject(AFSecurityDigestibleChunksProvider|AssistantAdditions|AnalyticsContextVending)
+ __OBJC_CLASS_PROTOCOLS_$_NSNull(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport)
+ __OBJC_CLASS_PROTOCOLS_$_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
+ __OBJC_CLASS_RO_$_AFLocalTurnStatusService
+ __OBJC_LABEL_PROTOCOL_$_AFLocalTurnStatusServiceInterface
+ __OBJC_LABEL_PROTOCOL_$_AFPreferencesInternalProviding
+ __OBJC_LABEL_PROTOCOL_$_AFPreferencesProviding
+ __OBJC_LABEL_PROTOCOL_$_SCDAStandbyListening
+ __OBJC_METACLASS_RO_$_AFLocalTurnStatusService
+ __OBJC_PROTOCOL_$_AFLocalTurnStatusServiceInterface
+ __OBJC_PROTOCOL_$_AFPreferencesInternalProviding
+ __OBJC_PROTOCOL_$_AFPreferencesProviding
+ __OBJC_PROTOCOL_$_SCDAStandbyListening
+ __OBJC_PROTOCOL_REFERENCE_$_AFLocalTurnStatusServiceInterface
+ ___294-[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:ifpCapableDevice:siriAvailability:]_block_invoke
+ ___35-[AFConnection scdaStandbyDidBegin]_block_invoke
+ ___39-[AFConnection scdaStandbyDidEndAsWon:]_block_invoke
+ ___51-[AFLocalTurnStatusService currentLocalTurnStatus:]_block_invoke
+ ___52-[AFSiriCapabilitiesServiceClient siriAvailability:]_block_invoke
+ ___52-[AFSiriCapabilitiesServiceClient siriAvailability:]_block_invoke_2
+ ___55-[AFSiriCapabilitiesServiceClient siriAvailabilitySync]_block_invoke
+ ___55-[AFSiriCapabilitiesServiceClient siriAvailabilitySync]_block_invoke_2
+ ___56-[AFPreferences fetchUseWithSiriStateForApp:completion:]_block_invoke
+ ___61-[AFMultiUserConnection isRecognizeMyVoiceEnabledForAnyUser:]_block_invoke
+ ___61-[AFMultiUserConnection isRecognizeMyVoiceEnabledForAnyUser:]_block_invoke_2
+ ___62-[AFSettingsConnection armAnnounceOverrideFollowUpText:reply:]_block_invoke
+ ___62-[AFSettingsConnection forceWeeklyCloudKitSyncWithCompletion:]_block_invoke
+ ___66-[AFConnectionClientServiceDelegate requestSetReplayOverridePath:]_block_invoke_2
+ ___73-[AFConnectionClientServiceDelegate notifyAppLaunchWillBePresentedToUser]_block_invoke
+ ___80-[AFSiriAnnounceWorkoutVoiceFeedbackRequest performRequestWithResultCompletion:]_block_invoke
+ ___96-[AFSettingsConnection(Internal) _syncDataWithAnchorKeys:forceReset:reason:completionWithError:]_block_invoke
+ ___AFIsHomePod_block_invoke
+ ___AFIsJ265_block_invoke
+ ___AFSiriActivationOdeonProxyVoiceTrigger_block_invoke
+ ___AFSiriWorkoutVoiceFeedbackResultGetFromName_block_invoke
+ ____AFPreferencesObserveLanguageChanges_block_invoke
+ ____AFPreferencesObserveLanguageChanges_block_invoke_2
+ ___block_descriptor_119_e8_32s40s48s56s64s72s80s88s96s104s_e41_v16?0"<AFCompanionDeviceInfoMutating>"8l
+ ___block_descriptor_32_e8_16?0Q8l
+ ___block_descriptor_32_e8_v12?0i8l
+ ___block_descriptor_40_e8_32bs_e21_v24?0Q8"NSString"16l
+ ___block_descriptor_40_e8_32r_e28_v16?0"AFSiriAvailability"8l
+ ___block_descriptor_40_e8_32s_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_48_e8_32bs40r_e28_v16?0"AFSiriAvailability"8l
+ ___block_descriptor_90_e8_32s40s48s56s64bs_e33_v16?0"AceObject<SAAceCommand>"8l
+ ___block_descriptor_98_e8_32s40s48s56s64s72bs_e5_v8?0l
+ _kAFLocalTurnStatusServiceEntitlement
+ _kAFLocalTurnStatusServiceErrorDomain
+ _kAFLocalTurnStatusServiceMachServiceName
+ _kAFPersonalContentSettingChangedDarwinNotification
+ _kAFSiriTVPersonalContentSettingKey
+ _objc_msgSend$_cleanupRoutingStandby
+ _objc_msgSend$_endUsefulUserFacingResultsIntervalIfNeeded
+ _objc_msgSend$_replyMissingDelegateMethodTo:
+ _objc_msgSend$_resetSpeechTimingForSpeechRequest:options:systemUptime:
+ _objc_msgSend$_syncDataWithAnchorKeys:forceReset:reason:replyWithError:
+ _objc_msgSend$applicationProcessIdentifier
+ _objc_msgSend$armAnnounceOverrideFollowUpText:reply:
+ _objc_msgSend$cacheEntitlement:forPID:pidVersion:bundleID:
+ _objc_msgSend$currentLocalTurnStatus:
+ _objc_msgSend$forceWeeklyCloudKitSyncWithCompletion:
+ _objc_msgSend$getArgumentTypeAtIndex:
+ _objc_msgSend$getIfpCapableDevice
+ _objc_msgSend$getLinwoodCapableDevice
+ _objc_msgSend$getLinwoodEnabled
+ _objc_msgSend$getSiriAvailability
+ _objc_msgSend$hasEntitlement:forPID:pidVersion:
+ _objc_msgSend$ifpCapableDevice
+ _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:
+ _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:
+ _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:
+ _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:ifpCapableDevice:
+ _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:buildVersion:linwoodEnabled:linwoodCapableDevice:ifpCapableDevice:siriAvailability:
+ _objc_msgSend$initWithSiriLanguageCode:
+ _objc_msgSend$isElectionLedgerEnabled
+ _objc_msgSend$isMediaEntitySyncDisabled
+ _objc_msgSend$isRecognizeMyVoiceEnabledForAnyUserWithCompletion:
+ _objc_msgSend$linwoodCapableDevice
+ _objc_msgSend$linwoodEnabled
+ _objc_msgSend$mintElectionIdentity
+ _objc_msgSend$myriadElectionIdentity
+ _objc_msgSend$notifyAppLaunchWillBePresentedToUser
+ _objc_msgSend$performRequestWithResultCompletion:
+ _objc_msgSend$setApplicationProcessIdentifier:
+ _objc_msgSend$setIfpCapableDevice:
+ _objc_msgSend$setIsReplyToSiriPrompt:
+ _objc_msgSend$setLinwoodCapableDevice:
+ _objc_msgSend$setLinwoodEnabled:
+ _objc_msgSend$setListener:
+ _objc_msgSend$setMyriadElectionIdentity:
+ _objc_msgSend$siriAvailability:
+ _objc_msgSend$siriAvailabilityOverXPCEnabled
+ _objc_msgSend$siriAvailabilitySync
+ _objc_msgSend$siriDidBecomeEffectivelyActive
+ _objc_msgSend$siriDidBecomeEffectivelyInactive
+ _objc_msgSend$streamId
+ _objc_msgSend$streamStage
+ _objc_msgSend$toDictionary
+ _sAFDaemonIsExitingCleanly
+ _sLanguageCacheDidComputeHookForTesting
+ _sLanguageCachePublished
+ _sLanguageCaches
+ _sSupportedLanguagesGeneration
+ _sSupportedLanguagesLock
+ sSupportedLanguagesGeneration_block_invoke.token
- +[AFFeatureFlags(SWEFeatureFlags) isHintsEnabled]
- +[AFSiriAvailability fromDictionary:]
- -[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:]
- -[AFConnectionEntitlementCache cacheEntitlement:forPID:bundleID:]
- -[AFConnectionEntitlementCache hasEntitlement:forPID:]
- AFIsHorseman.isHorseman
- AFIsHorseman.onceToken
- AFPreferencesSupportedDictationLanguages.onceToken
- AFPreferencesSupportedDictationLanguages.sSupportedDictationLanguages
- AFPreferencesSupportedDictationLanguagesSet.onceToken
- AFPreferencesSupportedDictationLanguagesSet.stAllLanguagesSet
- AFPreferencesSupportedLanguages.onceToken
- AFPreferencesSupportedLanguages.stAllLanguageCodes
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
- GCC_except_table2371
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
- GCC_except_table4495
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
- _AFPreferencesDictationLanguagePrefixes.onceToken
- _AFPreferencesDictationLanguagePrefixes.sLanguagePrefixes
- __66-[AFConnectionClientServiceDelegate requestSetReplayOverridePath:]_block_invoke
- __OBJC_$_CATEGORY_AceObject_$_AssistantAdditions
- __OBJC_$_CATEGORY_NSArray_$_AFCollectionUtilities
- __OBJC_$_CATEGORY_NSDate_$_AssistantAdditions
- __OBJC_$_CATEGORY_NSDictionary_$_AFCollectionUtilities
- __OBJC_$_CATEGORY_NSNull_$_AFBundleResourceSupport
- __OBJC_$_CATEGORY_NSString_$_AFPreferences
- __OBJC_$_CATEGORY_NSURL_$_AFBundleResourceSupport
- __OBJC_$_CLASS_METHODS_AFVoiceInfo(AFLocalizationAdditions|SiriTTSServiceAdditions)
- __OBJC_$_CLASS_METHODS_NSString(AFPreferences|AssistantServices|AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription)
- __OBJC_$_CLASS_METHODS_NSURL(AFBundleResourceSupport|AMOSExtensions|AFSecurityDigestibleChunksProvider|STSiriMessage)
- __OBJC_$_INSTANCE_METHODS_AFClockTimer(ClockItem|AFClockTimerMutability)
- __OBJC_$_INSTANCE_METHODS_AFCompanionDeviceInfo(AFCompanionDeviceInfoMutability)
- __OBJC_$_INSTANCE_METHODS_AFVoiceInfo(AFLocalizationAdditions|SiriTTSServiceAdditions)
- __OBJC_$_INSTANCE_METHODS_AceObject(AssistantAdditions|AFSecurityDigestibleChunksProvider|AnalyticsContextVending)
- __OBJC_$_INSTANCE_METHODS_NSArray(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
- __OBJC_$_INSTANCE_METHODS_NSDate(AssistantAdditions|AFSecurityDigestibleChunksProvider)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(AFCollectionUtilities|AFSecurityDigestibleChunksProvider)
- __OBJC_$_INSTANCE_METHODS_NSNull(AFBundleResourceSupport|AFSecurityDigestibleChunksProvider)
- __OBJC_$_INSTANCE_METHODS_NSString(AFPreferences|AssistantServices|AFSecurityDigestibleChunksProvider|AFSiriRequest|ShortDescription)
- __OBJC_$_INSTANCE_METHODS_NSURL(AFBundleResourceSupport|AMOSExtensions|AFSecurityDigestibleChunksProvider|STSiriMessage)
- __OBJC_CLASS_PROTOCOLS_$_AFClockTimer(ClockItem|AFClockTimerMutability)
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
- ___block_descriptor_32_e25_v32?0"NSString"8Q16^B24l
- ___block_descriptor_82_e8_32s40s48s56bs_e33_v16?0"AceObject<SAAceCommand>"8l
- ___block_descriptor_90_e8_32s40s48s56s64bs_e5_v8?0l
- _objc_msgSend$cacheEntitlement:forPID:bundleID:
- _objc_msgSend$fromDictionary:
- _objc_msgSend$hasEntitlement:forPID:
- _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:
- _uuid_clear
- _xpc_get_instance
CStrings:
+ "%@ {assistantID = %@, speechID = %@, idsIdentifier = %@, productPrefix = %@, aceHost = %@, syncMetadata = %@, syncMetadataCapability = %@, peerToPeerHandoffCapability = %@, muxSupportCapability = %@, meDevice = %@, siriLanguage = %@, companionName = %@, buildVersion = %@, linwoodEnabled = %@, linwoodCapableDevice = %@, ifpCapableDevice = %@, siriAvailability = %@}"
+ "%s %p entering routing standby - suppressing interstitials"
+ "%s %p leaving routing standby (didWin = %d)"
+ "%s %p skipping interstitials while in routing standby (reason = %{public}@)"
+ "%s Asked to set nil iCloudAltDSID for personal content setting"
+ "%s Error in isRecognizeMyVoiceEnabledForAnyUser:%@"
+ "%s Is Medoc Supported? %d"
+ "%s Overriding SAE as supported as Linwood is supported"
+ "%s Requested nil iCloudAltDSID for personal content setting"
+ "%s The requestId=%@ is malformed, unable to log ServerExecutionValuesReported"
+ "%s Use with Siri unavailable for %@: unsupported platform"
+ "%s [rdar://178756283] AFConnection receive SAUIAddViews aceId=%@ views.count=%lu isInterstitial=%d"
+ "%s [rdar://178756283] AFConnection receive SAUIStreamChunk streamId=%@ streamStage=%@ aceId=%@ commands=%@"
+ "%s _AFPreferencesAnnouncementPlatformOverride: platform=%ld, isValidAndSpecified=%d"
+ "%s isMediaEntitySyncDisabled=true because Siri/disable_media_entity_sync FF is on"
+ "%s isMedocSupported = %d, deviceSupportsGenerativeModelSystems = %d, linwoodSupported = %d, isNLRouterFeatureEnabled = %d, deviceSupportsSAEByDeviceCapabilityAndFeatureFlags = %d"
+ "%s notifyAppLaunchWillBePresentedToUser: {_uufrID: %llu, _uufrIntervalEnded: %d}"
+ "%s visualIntelligenceRestricted = 1 (no persisted AFSiriAvailability)"
+ "+[AFSiriAvailability fromPreferences]"
+ ", isReplyToSiriPrompt = %d"
+ ", myriadElectionIdentity = %@"
+ "-[AFConnection _endUsefulUserFacingResultsIntervalIfNeeded]"
+ "-[AFConnection notifyAppLaunchWillBePresentedToUser]"
+ "-[AFConnection scdaStandbyDidBegin]_block_invoke"
+ "-[AFConnection scdaStandbyDidEndAsWon:]_block_invoke"
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
+ "@16@?0Q8"
+ "AFCompanionDeviceInfo::buildVersion"
+ "AFCompanionDeviceInfo::ifpCapableDevice"
+ "AFCompanionDeviceInfo::linwoodCapableDevice"
+ "AFCompanionDeviceInfo::linwoodEnabled"
+ "AFCompanionDeviceInfo::siriAvailability"
+ "AFDaemonWillExitCleanlyNotification"
+ "AFDeviceSupportsMedoc"
+ "AFLocalTurnStatusServiceErrorDomain"
+ "AFMeDeviceLinwoodEnablementDidChangeNotification"
+ "AFSiriActivationOdeonProxyVoiceTrigger"
+ "AFSiriAvailability {\n  isAvailable: %@\n  siriLocale: %@\n  desiredOrchestrationMode: %@\n  desiredOrchestrationModeIfEnabled: %@\n  unavailabilityReasons: %@\n  linwoodEverAvailable: %@\n  bootUUID: %@\n  fromCurrentBoot: %@\n}"
+ "AFUseWithSiriAvailableForApp"
+ "AFVisualIntelligenceCameraRestricted"
+ "Announcement Platform Override"
+ "AppExclusions"
+ "AppleTV18,1"
+ "Assistant Enabled Before Restriction Version"
+ "Block %@ argument %lu is type '%s'; AFMultiArgumentSafetyBlock dispatches object arguments only."
+ "GMSEnabled"
+ "Odeon Proxy Voice Trigger"
+ "RISESSION_CLIENT_EVENT"
+ "RI_CLIENT_EVENT"
+ "Siri Apple TV Personal content setting"
+ "TC_CLIENT_EVENT"
+ "[]"
+ "_AFPreferencesAnnouncementPlatformOverride"
+ "_AFPreferencesSetSiriPersonalContentSetting"
+ "_AFPreferencesSiriPersonalContentSetting"
+ "_applicationProcessIdentifier"
+ "_isReplyToSiriPrompt"
+ "_myriadElectionIdentity"
+ "audioInterrupted"
+ "ck_cache_mirrored_tokens"
+ "com.apple.siri.local-turn-status"
+ "com.apple.siri.personalcontent.setting.changed"
+ "continuous_conversation_homepod"
+ "daemonUnavailable"
+ "disable_ace_sync"
+ "ifpCapableDevice"
+ "inopportune"
+ "linwoodCapableDevice"
+ "linwoodEnabled"
+ "linwood_modality_connection_skip"
+ "muted"
+ "notificationsDisabled"
+ "odeonProxyVoiceTrigger"
+ "routeUnavailable"
+ "routing target standby began"
+ "routing target standby ended"
+ "selectsAll"
+ "serializationFailed"
+ "siriAvailability"
+ "siriBusy"
+ "siri_availability_over_xpc"
+ "siri_capabilities_settle_coalescing_disabled"
+ "timedOut"
+ "v16@?0@\"AFSiriAvailability\"8"
+ "v24@?0Q8@\"NSString\"16"
+ "\xf0\xf0\xf0\""
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
