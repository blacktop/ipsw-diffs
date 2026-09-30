## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices`

```diff

-3403.5.1.0.0
-  __TEXT.__text: 0x1b4c88
+3404.80.4.0.0
+  __TEXT.__text: 0x1b9d80
   __TEXT.__auth_stubs: 0x1280
-  __TEXT.__objc_methlist: 0x19a4c
+  __TEXT.__objc_methlist: 0x1d83c
   __TEXT.__const: 0x440
-  __TEXT.__gcc_except_tab: 0x2454
-  __TEXT.__cstring: 0x39aef
-  __TEXT.__oslogstring: 0xf8b9
   __TEXT.__dlopen_cstrs: 0x324
-  __TEXT.__unwind_info: 0x75a0
-  __TEXT.__objc_classname: 0x4e00
-  __TEXT.__objc_methname: 0x399af
-  __TEXT.__objc_methtype: 0xa789
-  __TEXT.__objc_stubs: 0x22f40
-  __DATA_CONST.__got: 0x15c8
-  __DATA_CONST.__const: 0x3e68
-  __DATA_CONST.__objc_classlist: 0xdb0
+  __TEXT.__gcc_except_tab: 0x284c
+  __TEXT.__cstring: 0x3a6fc
+  __TEXT.__oslogstring: 0xff26
+  __TEXT.__ustring: 0x2ac
+  __TEXT.__unwind_info: 0x7788
+  __TEXT.__objc_classname: 0x4e8b
+  __TEXT.__objc_methname: 0x39f6b
+  __TEXT.__objc_methtype: 0xa8b9
+  __TEXT.__objc_stubs: 0x23380
+  __DATA_CONST.__got: 0x15e8
+  __DATA_CONST.__const: 0x3ed8
+  __DATA_CONST.__objc_classlist: 0xdc8
   __DATA_CONST.__objc_catlist: 0x290
-  __DATA_CONST.__objc_protolist: 0x540
+  __DATA_CONST.__objc_protolist: 0x548
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xbb98
-  __DATA_CONST.__objc_protorefs: 0x148
-  __DATA_CONST.__objc_superrefs: 0xdc0
-  __DATA_CONST.__objc_arraydata: 0x1fa8
+  __DATA_CONST.__objc_selrefs: 0xbe40
+  __DATA_CONST.__objc_protorefs: 0x150
+  __DATA_CONST.__objc_superrefs: 0xde0
+  __DATA_CONST.__objc_arraydata: 0x2080
   __AUTH_CONST.__auth_got: 0x950
-  __AUTH_CONST.__const: 0x7f40
-  __AUTH_CONST.__cfstring: 0x261a0
-  __AUTH_CONST.__objc_const: 0x39b30
+  __AUTH_CONST.__const: 0x8140
+  __AUTH_CONST.__cfstring: 0x265a0
+  __AUTH_CONST.__objc_const: 0x33188
   __AUTH_CONST.__objc_intobj: 0x2328
   __AUTH_CONST.__objc_dictobj: 0xb90
-  __AUTH_CONST.__objc_arrayobj: 0x588
+  __AUTH_CONST.__objc_arrayobj: 0x5b8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x2f30
-  __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x251c
-  __DATA.__data: 0x4040
-  __DATA.__bss: 0xef0
-  __DATA.__common: 0x38
+  __AUTH.__objc_data: 0x3020
+  __AUTH.__data: 0x80
+  __DATA.__objc_ivar: 0x2518
+  __DATA.__data: 0x40b0
+  __DATA.__bss: 0xf50
+  __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x59b0
-  __DATA_DIRTY.__data: 0xa8
-  __DATA_DIRTY.__bss: 0x80
+  __DATA_DIRTY.__data: 0xa0
   __DATA_DIRTY.__common: 0xd0
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8D9ECBB2-FA8E-346B-9A40-CF796E5D7F81
-  Functions: 11482
-  Symbols:   25811
-  CStrings:  23324
+  UUID: C9BCC917-3BF4-3749-BF7B-E7EFBB0A0B39
+  Functions: 11535
+  Symbols:   26049
+  CStrings:  23490
 
Symbols:
+ +[AFApplicationGroupContainer sharedInstance]
+ +[AFFeatureFlags(SWEFeatureFlags) isASRSpeechProfileAppEntitiesEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isASRSpeechProfileOnscreenEntitiesEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isHomePodNoTTSPerfTestEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isOfflineDictationLanguageMappingEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isPersistentSiriEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isRemoteSessionDisabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isSAEi18nEnabled]
+ +[AFSamplingUtilities fileExistsAndNotEmpty:samplingComponent:]
+ +[AFSpeechMessagesContext supportsSecureCoding]
+ +[AFSpeechVisualContextAndCorrectionsInfo supportsSecureCoding]
+ +[AFSystemAssistantExperienceStatusManager deviceSupportsSAE]
+ +[AFSystemAssistantExperienceStatusManager isVisualIntelligenceEnabled]
+ +[AFSystemAssistantExperienceStatusManager saeAvailable]
+ +[AFSystemAssistantExperienceStatusManager swaiEnabled]
+ +[AFSystemAssistantExperienceStatusManager(UST) ust_deviceSupportsSAE]
+ +[AFSystemAssistantExperienceStatusManager(UST) ust_saeEnabled]
+ +[AFSystemAssistantExperienceStatusManager(UST) ust_swaiEnabled]
+ -[AFApplicationGroupContainer sharedApplicationGroupURL:]
+ -[AFApplicationGroupContainer sharedApplicationGroupURLOnQueue:WithCompletion:]
+ -[AFConnectionClientServiceDelegate requestReplayAllRecordedViews:with:]
+ -[AFConnectionClientServiceDelegate requestReplayRecordedViewAt:with:]
+ -[AFConnectionClientServiceDelegate requestSetReplayEnabled:]
+ -[AFConnectionClientServiceDelegate requestSetReplayOverridePath:]
+ -[AFDictationConnection sendVisualContextAndCorrectionsInfo:interactionIdentifier:]
+ -[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:]
+ -[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:]
+ -[AFHomeAnnouncementObserver _updateForReason:]
+ -[AFMultiUserConnection getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]
+ -[AFMultiUserConnection getPrimaryUserSharedUserInfoWithCompletion:]
+ -[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:completion:]
+ -[AFPreferences allowHeadGestureInjection]
+ -[AFPreferences setAllowHeadGestureInjection:]
+ -[AFPreferences setVisualIntelligenceCameraControlEnabled:]
+ -[AFPreferences visualIntelligenceCameraControlEnabled]
+ -[AFSettingsConnection mockHeadGesture:schedule:withCompletion:]
+ -[AFSettingsConnection replayAllRecordedViews:with:]
+ -[AFSettingsConnection replayRecordedViewAt:with:]
+ -[AFSettingsConnection setReplayEnabled:]
+ -[AFSettingsConnection setReplayOverridePath:]
+ -[AFSharedUserInfo initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:]
+ -[AFSharedUserInfo isDeviceOwner]
+ -[AFSiriCapabilitiesServiceClient .cxx_destruct]
+ -[AFSiriCapabilitiesServiceClient connection]
+ -[AFSiriCapabilitiesServiceClient dealloc]
+ -[AFSiriCapabilitiesServiceClient serviceWithErrorHandler:]
+ -[AFSiriCapabilitiesServiceClient service]
+ -[AFSiriCapabilitiesServiceClient setConnection:]
+ -[AFSiriCapabilitiesServiceClient shouldDownloadAssetsForSiriSystemAssistantExperience:]
+ -[AFSiriCapabilitiesServiceClient shouldDownloadAssetsForSiriSystemAssistantExperienceSync]
+ -[AFSiriCapabilitiesServiceClient siriSystemAssistantExperienceEnabled:]
+ -[AFSiriCapabilitiesServiceClient siriSystemAssistantExperienceEnabledSync]
+ -[AFSiriCapabilitiesServiceClient siriWithAppIntentsEnabled:]
+ -[AFSiriCapabilitiesServiceClient siriWithAppIntentsEnabledSync]
+ -[AFSiriCapabilitiesServiceClient syncServiceWithErrorHandler:]
+ -[AFSiriHeadphonesMonitor mockHeadGesture:schedule:withCompletion:]
+ -[AFSiriHeadphonesMonitor registerInternalGestureTestingHandler:]
+ -[AFSiriRingtone setShouldAppendAutoAnswerTip:]
+ -[AFSiriRingtone shouldAppendAutoAnswerTip]
+ -[AFSpeechMessagesContext .cxx_destruct]
+ -[AFSpeechMessagesContext copyWithZone:]
+ -[AFSpeechMessagesContext description]
+ -[AFSpeechMessagesContext encodeWithCoder:]
+ -[AFSpeechMessagesContext initWithCoder:]
+ -[AFSpeechMessagesContext isEqual:]
+ -[AFSpeechMessagesContext messages]
+ -[AFSpeechMessagesContext sender]
+ -[AFSpeechMessagesContext setMessages:]
+ -[AFSpeechMessagesContext setSender:]
+ -[AFSpeechVisualContextAndCorrectionsInfo .cxx_destruct]
+ -[AFSpeechVisualContextAndCorrectionsInfo copyWithZone:]
+ -[AFSpeechVisualContextAndCorrectionsInfo correctedText]
+ -[AFSpeechVisualContextAndCorrectionsInfo description]
+ -[AFSpeechVisualContextAndCorrectionsInfo encodeWithCoder:]
+ -[AFSpeechVisualContextAndCorrectionsInfo initWithCoder:]
+ -[AFSpeechVisualContextAndCorrectionsInfo isEqual:]
+ -[AFSpeechVisualContextAndCorrectionsInfo messagesContext]
+ -[AFSpeechVisualContextAndCorrectionsInfo recognizedText]
+ -[AFSpeechVisualContextAndCorrectionsInfo setCorrectedText:]
+ -[AFSpeechVisualContextAndCorrectionsInfo setMessagesContext:]
+ -[AFSpeechVisualContextAndCorrectionsInfo setRecognizedText:]
+ -[AFSystemAssistantExperienceStatusManager deviceSupportsSAE]
+ -[AFSystemAssistantExperienceStatusManager init]
+ -[AFSystemAssistantExperienceStatusManager saeAvailable]
+ -[AFSystemAssistantExperienceStatusManager setDeviceSupportsSAE:]
+ -[AFSystemAssistantExperienceStatusManager setSaeAvailable:]
+ -[AFSystemAssistantExperienceStatusManager setSwaiEnabled:]
+ -[AFSystemAssistantExperienceStatusManager setVisualIntelligenceEnabled:]
+ -[AFSystemAssistantExperienceStatusManager swaiEnabled]
+ -[AFSystemAssistantExperienceStatusManager visualIntelligenceEnabled]
+ -[_AFSharedUserInfoMutation getIsDeviceOwner]
+ -[_AFSharedUserInfoMutation setIsDeviceOwner:]
+ AFIsDeviceGreymatterEligible.isDeviceGreymatterEligible
+ AFIsDeviceGreymatterEligible.onceToken
+ AFLocaleIdentifierSupportsSAE.once
+ AFLocaleIdentifierSupportsSAE.supportedEnglishLocales
+ AFLocaleIdentifierSupportsSAE.supportedGlobalLocales
+ BiomeLibraryLibraryCore.45357
+ BiomeLibraryLibraryCore.frameworkLibrary.26957
+ BiomeLibraryLibraryCore.frameworkLibrary.45360
+ BluetoothManagerLibrary.45456
+ CloudSubscriptionFeaturesLibrary.sLib
+ CloudSubscriptionFeaturesLibrary.sOnce
+ GCC_except_table10182
+ GCC_except_table10243
+ GCC_except_table10247
+ GCC_except_table10249
+ GCC_except_table10252
+ GCC_except_table10258
+ GCC_except_table10265
+ GCC_except_table1035
+ GCC_except_table10502
+ GCC_except_table10668
+ GCC_except_table10681
+ GCC_except_table10860
+ GCC_except_table10978
+ GCC_except_table10991
+ GCC_except_table11026
+ GCC_except_table1112
+ GCC_except_table11281
+ GCC_except_table11432
+ GCC_except_table11451
+ GCC_except_table11454
+ GCC_except_table11456
+ GCC_except_table1253
+ GCC_except_table1255
+ GCC_except_table1444
+ GCC_except_table1481
+ GCC_except_table1493
+ GCC_except_table1510
+ GCC_except_table1513
+ GCC_except_table1595
+ GCC_except_table1601
+ GCC_except_table1604
+ GCC_except_table1669
+ GCC_except_table1736
+ GCC_except_table1758
+ GCC_except_table1764
+ GCC_except_table2006
+ GCC_except_table2050
+ GCC_except_table2218
+ GCC_except_table2283
+ GCC_except_table2341
+ GCC_except_table2710
+ GCC_except_table2717
+ GCC_except_table2721
+ GCC_except_table2723
+ GCC_except_table2755
+ GCC_except_table2763
+ GCC_except_table2769
+ GCC_except_table2777
+ GCC_except_table2780
+ GCC_except_table2782
+ GCC_except_table2789
+ GCC_except_table2795
+ GCC_except_table2807
+ GCC_except_table2810
+ GCC_except_table2832
+ GCC_except_table2834
+ GCC_except_table2836
+ GCC_except_table2838
+ GCC_except_table2840
+ GCC_except_table2842
+ GCC_except_table2885
+ GCC_except_table2910
+ GCC_except_table2965
+ GCC_except_table2995
+ GCC_except_table3268
+ GCC_except_table3324
+ GCC_except_table3446
+ GCC_except_table3460
+ GCC_except_table3472
+ GCC_except_table3479
+ GCC_except_table3480
+ GCC_except_table3483
+ GCC_except_table3489
+ GCC_except_table3577
+ GCC_except_table3579
+ GCC_except_table3596
+ GCC_except_table3602
+ GCC_except_table3644
+ GCC_except_table3656
+ GCC_except_table3726
+ GCC_except_table3829
+ GCC_except_table3836
+ GCC_except_table3851
+ GCC_except_table3890
+ GCC_except_table3978
+ GCC_except_table4032
+ GCC_except_table4437
+ GCC_except_table4438
+ GCC_except_table461
+ GCC_except_table4725
+ GCC_except_table4793
+ GCC_except_table4858
+ GCC_except_table4868
+ GCC_except_table4879
+ GCC_except_table4893
+ GCC_except_table5014
+ GCC_except_table512
+ GCC_except_table531
+ GCC_except_table5371
+ GCC_except_table5374
+ GCC_except_table5464
+ GCC_except_table5572
+ GCC_except_table5576
+ GCC_except_table5692
+ GCC_except_table5791
+ GCC_except_table5812
+ GCC_except_table5814
+ GCC_except_table5878
+ GCC_except_table5880
+ GCC_except_table5882
+ GCC_except_table5884
+ GCC_except_table5898
+ GCC_except_table5904
+ GCC_except_table6025
+ GCC_except_table6032
+ GCC_except_table6387
+ GCC_except_table6402
+ GCC_except_table6427
+ GCC_except_table6533
+ GCC_except_table6571
+ GCC_except_table6603
+ GCC_except_table6670
+ GCC_except_table7179
+ GCC_except_table7184
+ GCC_except_table7187
+ GCC_except_table719
+ GCC_except_table7190
+ GCC_except_table7193
+ GCC_except_table7196
+ GCC_except_table726
+ GCC_except_table7403
+ GCC_except_table7406
+ GCC_except_table7408
+ GCC_except_table7420
+ GCC_except_table7644
+ GCC_except_table7749
+ GCC_except_table7781
+ GCC_except_table7967
+ GCC_except_table7972
+ GCC_except_table8036
+ GCC_except_table8142
+ GCC_except_table845
+ GCC_except_table8559
+ GCC_except_table8610
+ GCC_except_table8654
+ GCC_except_table8751
+ GCC_except_table8756
+ GCC_except_table8757
+ GCC_except_table8761
+ GCC_except_table9004
+ GCC_except_table9076
+ GCC_except_table9082
+ GCC_except_table9119
+ GCC_except_table9122
+ GCC_except_table9200
+ GCC_except_table9228
+ GCC_except_table9300
+ GCC_except_table9303
+ GCC_except_table9307
+ GCC_except_table9415
+ GCC_except_table9423
+ GCC_except_table9456
+ GCC_except_table9503
+ GCC_except_table9936
+ GCC_except_table9938
+ GCC_except_table9941
+ GCC_except_table9950
+ GCC_except_table9976
+ GCC_except_table9991
+ IntentsLibraryCore.frameworkLibrary.30881
+ LSApplicationProxyFunction.34261
+ LSApplicationProxyFunction.45959
+ LaunchServicesLibrary.frameworkLibrary.45954
+ OBJC_IVAR_$_AFSharedUserInfo._isDeviceOwner
+ OBJC_IVAR_$_AFSiriCapabilitiesServiceClient._connection
+ OBJC_IVAR_$_AFSiriHeadphonesMonitor._internalGestureTestingHandler
+ OBJC_IVAR_$_AFSiriHeadphonesMonitor._scheduledHeadGesture
+ OBJC_IVAR_$_AFSiriRingtone._shouldAppendAutoAnswerTip
+ OBJC_IVAR_$_AFSpeechMessagesContext._messages
+ OBJC_IVAR_$_AFSpeechMessagesContext._sender
+ OBJC_IVAR_$_AFSpeechVisualContextAndCorrectionsInfo._correctedText
+ OBJC_IVAR_$_AFSpeechVisualContextAndCorrectionsInfo._messagesContext
+ OBJC_IVAR_$_AFSpeechVisualContextAndCorrectionsInfo._recognizedText
+ OBJC_IVAR_$_AFSystemAssistantExperienceStatusManager._deviceSupportsSAE
+ OBJC_IVAR_$_AFSystemAssistantExperienceStatusManager._saeAvailable
+ OBJC_IVAR_$_AFSystemAssistantExperienceStatusManager._swaiEnabled
+ OBJC_IVAR_$_AFSystemAssistantExperienceStatusManager._visualIntelligenceEnabled
+ OBJC_IVAR_$__AFSharedUserInfoMutation._isDeviceOwner
+ SoftBiomeLibrary.45343
+ _AFDeviceSupportsSAEDeprecated
+ _AFDeviceSupportsSystemAssistantExperienceDeprecated
+ _AFDeviceSupportsVisualIntelligence
+ _AFIsAppleIntelligenceEnabled
+ _AFIsDeviceGreymatterEligible
+ _AFIsPersistentSiriAvailable
+ _AFIsRemoteMontaraAllowed
+ _AFLocaleIdentifierSupportsSAE
+ _AFRaiseToSpeakSupportedForLanguage
+ _AFRaiseToSpeakUnsupportedLocales.once
+ _AFRaiseToSpeakUnsupportedLocales.rtsUnsupportedLocales
+ _AFRestrictionsChangedNotificationName
+ _AFShouldEmitAceCommandContextSELFLog
+ _AFSiriLogContextFilesystem
+ _AFVisualIntelligenceEnabled
+ _AllowedNowPlayingKeysAndTypes.makeSchemaOnlyOnceGuard
+ _AllowedNowPlayingKeysAndTypes.schema
+ _CSFGMOptInFunction
+ _HandleSiriCapabilitiesDidChange
+ _NSFileSize
+ _OBJC_CLASS_$_AFApplicationGroupContainer
+ _OBJC_CLASS_$_AFSiriCapabilitiesServiceClient
+ _OBJC_CLASS_$_AFSpeechMessagesContext
+ _OBJC_CLASS_$_AFSpeechVisualContextAndCorrectionsInfo
+ _OBJC_METACLASS_$_AFApplicationGroupContainer
+ _OBJC_METACLASS_$_AFSiriCapabilitiesServiceClient
+ _OBJC_METACLASS_$_AFSpeechMessagesContext
+ _OBJC_METACLASS_$_AFSpeechVisualContextAndCorrectionsInfo
+ _SAVoiceVoiceTypeNaturalValue
+ __105-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesWithCompletion:]_block_invoke.31
+ __105-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesWithCompletion:]_block_invoke.39
+ __105-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesWithCompletion:]_block_invoke_2.32
+ __105-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesWithCompletion:]_block_invoke_3.33
+ __106-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchAvailableAnnouncementRequestTypesWithCompletion:]_block_invoke.40
+ __106-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchAvailableAnnouncementRequestTypesWithCompletion:]_block_invoke.45
+ __30-[AFMyriadCoordinator endTask]_block_invoke.325
+ __40-[AFMyriadCoordinator _advertiseTrigger]_block_invoke.498
+ __40-[AFMyriadCoordinator _advertiseTrigger]_block_invoke.502
+ __40-[AFMyriadCoordinator _advertiseTrigger]_block_invoke.503
+ __43-[AFSettingsConnection dumpAssistantState:]_block_invoke.273
+ __44-[AFSettingsConnection currectNWActivityId:]_block_invoke.151
+ __46-[AFMyriadCoordinator _waitWiProx:andExecute:]_block_invoke.553
+ __47-[AFSettingsConnection startUIRequestWithInfo:]_block_invoke.184
+ __47-[AFSettingsConnection startUIRequestWithText:]_block_invoke.179
+ __48-[AFSettingsConnection siriDesignModeIsEnabled:]_block_invoke.266
+ __50-[AFSettingsConnection areSiriSAEAssetsAvailable:]_block_invoke.272
+ __55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke.284
+ __55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke.307
+ __55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke.318
+ __56-[AFMyriadCoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.552
+ __56-[AFSettingsConnection isSearchDataSharingStatusForced:]_block_invoke.269
+ __57-[AFSettingsConnection setIsHomePodInHH2Mode:completion:]_block_invoke.260
+ __58-[AFSettingsConnection getSearchQueriesDataSharingStatus:]_block_invoke.268
+ __60-[AFSettingsConnection multiUserCompanionDeviceIdentifiers:]_block_invoke.246
+ __60-[AFSettingsConnection setSiriDesignModeEnabled:completion:]_block_invoke.265
+ __60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.600
+ __62-[AFSettingsConnection getCurrentAccessoryInfoWithCompletion:]_block_invoke.165
+ __62-[AFSettingsConnection getPersonalMultiUserDeviceIdentifiers:]_block_invoke.245
+ __64-[AFConnectionClientServiceDelegate requestHandleCommand:reply:]_block_invoke.822
+ __64-[AFSettingsConnection shouldSuppressSiriDataSharingOptInAlert:]_block_invoke.263
+ __65-[AFSettingsConnection setSiriDataSharingOptInStatus:completion:]_block_invoke.253
+ __66-[AFDictationConnectionServiceDelegate speechDidRecognizePackage:]_block_invoke.571
+ __68-[AFSettingsConnection deleteSiriHistoryWithContext:withCompletion:]_block_invoke.264
+ __68-[AFSettingsConnection getSiriDataSharingOptInStatusWithCompletion:]_block_invoke.254
+ __69-[AFSettingsConnection setSearchQueriesDataSharingStatus:completion:]_block_invoke.267
+ __73-[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke.514
+ __73-[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke.534
+ __73-[AFSettingsConnection setSiriDataSharingOptInAlertPresented:completion:]_block_invoke.258
+ __76-[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:completion:]_block_invoke.13
+ __76-[AFMyriadCoordinator _updateArbitrationParticipationContextWithCompletion:]_block_invoke.484
+ __77-[AFSettingsConnection _createRadarWithReason:room:process:crash:completion:]_block_invoke.286
+ __79-[AFSettingsConnection setSiriDataSharingHomePodSetupDeviceIsValid:completion:]_block_invoke.259
+ __83+[AFDictationConnection getForcedOfflineDictationSupportedLanguagesWithCompletion:]_block_invoke.260
+ __88-[AFSiriCapabilitiesServiceClient shouldDownloadAssetsForSiriSystemAssistantExperience:]_block_invoke.56
+ __89-[AFPreferences getAnnounceNotificationsTemporarilyDisabledStatusForPlatform:completion:]_block_invoke.1225
+ __89-[AFPreferences getAnnounceNotificationsTemporarilyDisabledStatusForPlatform:completion:]_block_invoke.1228
+ __90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.117
+ __90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.122
+ __91-[AFSiriCapabilitiesServiceClient shouldDownloadAssetsForSiriSystemAssistantExperienceSync]_block_invoke.52
+ __92-[AFDictationConnectionServiceDelegate speechDidRecognizeTokens:nluResult:usingSpeechModel:]_block_invoke.574
+ __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.320
+ __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.325
+ __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.328
+ __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.334
+ __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.338
+ __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke_2.339
+ __99-[AFSettingsConnection(Internal) _updateMultiUserInfoForUser:score:companionInfo:reset:completion:]_block_invoke.599
+ __AFPreferencesAllowHeadGestureInjection
+ __AFPreferencesAnnounceOnHeadphonesCachedEligibility
+ __AFPreferencesSetAllowHeadGestureInjection
+ __AFPreferencesSetAnnounceOnHeadphonesCachedEligibility
+ __BiomeLibraryLibraryCore_block_invoke.26958
+ __BiomeLibraryLibraryCore_block_invoke.45361
+ __Block_byref_object_copy_.10182
+ __Block_byref_object_copy_.10670
+ __Block_byref_object_copy_.10854
+ __Block_byref_object_copy_.11495
+ __Block_byref_object_copy_.12069
+ __Block_byref_object_copy_.13340
+ __Block_byref_object_copy_.13590
+ __Block_byref_object_copy_.17087
+ __Block_byref_object_copy_.17568
+ __Block_byref_object_copy_.19723
+ __Block_byref_object_copy_.20215
+ __Block_byref_object_copy_.21214
+ __Block_byref_object_copy_.22136
+ __Block_byref_object_copy_.22813
+ __Block_byref_object_copy_.23204
+ __Block_byref_object_copy_.23809
+ __Block_byref_object_copy_.26090
+ __Block_byref_object_copy_.28794
+ __Block_byref_object_copy_.30458
+ __Block_byref_object_copy_.316
+ __Block_byref_object_copy_.34672
+ __Block_byref_object_copy_.35121
+ __Block_byref_object_copy_.37334
+ __Block_byref_object_copy_.38512
+ __Block_byref_object_copy_.41649
+ __Block_byref_object_copy_.46073
+ __Block_byref_object_copy_.47293
+ __Block_byref_object_copy_.48023
+ __Block_byref_object_copy_.48303
+ __Block_byref_object_copy_.5435
+ __Block_byref_object_copy_.5841
+ __Block_byref_object_copy_.7990
+ __Block_byref_object_copy_.8888
+ __Block_byref_object_dispose_.10183
+ __Block_byref_object_dispose_.10671
+ __Block_byref_object_dispose_.10855
+ __Block_byref_object_dispose_.11496
+ __Block_byref_object_dispose_.12070
+ __Block_byref_object_dispose_.13341
+ __Block_byref_object_dispose_.13591
+ __Block_byref_object_dispose_.17088
+ __Block_byref_object_dispose_.17569
+ __Block_byref_object_dispose_.19724
+ __Block_byref_object_dispose_.20216
+ __Block_byref_object_dispose_.21215
+ __Block_byref_object_dispose_.22137
+ __Block_byref_object_dispose_.22814
+ __Block_byref_object_dispose_.23205
+ __Block_byref_object_dispose_.23810
+ __Block_byref_object_dispose_.26091
+ __Block_byref_object_dispose_.28795
+ __Block_byref_object_dispose_.30459
+ __Block_byref_object_dispose_.317
+ __Block_byref_object_dispose_.34673
+ __Block_byref_object_dispose_.35122
+ __Block_byref_object_dispose_.37335
+ __Block_byref_object_dispose_.38513
+ __Block_byref_object_dispose_.41650
+ __Block_byref_object_dispose_.46074
+ __Block_byref_object_dispose_.47294
+ __Block_byref_object_dispose_.48024
+ __Block_byref_object_dispose_.48304
+ __Block_byref_object_dispose_.5436
+ __Block_byref_object_dispose_.5842
+ __Block_byref_object_dispose_.7991
+ __Block_byref_object_dispose_.8889
+ __IntentsLibraryCore_block_invoke.30882
+ __OBJC_$_CLASS_METHODS_AFApplicationGroupContainer
+ __OBJC_$_CLASS_METHODS_AFSpeechMessagesContext
+ __OBJC_$_CLASS_METHODS_AFSpeechVisualContextAndCorrectionsInfo
+ __OBJC_$_CLASS_METHODS_AFSystemAssistantExperienceStatusManager(UST)
+ __OBJC_$_CLASS_PROP_LIST_AFSpeechMessagesContext
+ __OBJC_$_CLASS_PROP_LIST_AFSpeechVisualContextAndCorrectionsInfo
+ __OBJC_$_INSTANCE_METHODS_AFApplicationGroupContainer
+ __OBJC_$_INSTANCE_METHODS_AFSiriCapabilitiesServiceClient
+ __OBJC_$_INSTANCE_METHODS_AFSpeechMessagesContext
+ __OBJC_$_INSTANCE_METHODS_AFSpeechVisualContextAndCorrectionsInfo
+ __OBJC_$_INSTANCE_VARIABLES_AFSiriCapabilitiesServiceClient
+ __OBJC_$_INSTANCE_VARIABLES_AFSpeechMessagesContext
+ __OBJC_$_INSTANCE_VARIABLES_AFSpeechVisualContextAndCorrectionsInfo
+ __OBJC_$_PROP_LIST_AFSiriCapabilitiesServiceClient
+ __OBJC_$_PROP_LIST_AFSpeechMessagesContext
+ __OBJC_$_PROP_LIST_AFSpeechVisualContextAndCorrectionsInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFSiriCapabilitiesServiceClientInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AFSiriCapabilitiesServiceClientInterface
+ __OBJC_$_PROTOCOL_REFS_AFSiriCapabilitiesServiceClientInterface
+ __OBJC_CLASS_PROTOCOLS_$_AFSpeechMessagesContext
+ __OBJC_CLASS_PROTOCOLS_$_AFSpeechVisualContextAndCorrectionsInfo
+ __OBJC_CLASS_RO_$_AFApplicationGroupContainer
+ __OBJC_CLASS_RO_$_AFSiriCapabilitiesServiceClient
+ __OBJC_CLASS_RO_$_AFSpeechMessagesContext
+ __OBJC_CLASS_RO_$_AFSpeechVisualContextAndCorrectionsInfo
+ __OBJC_LABEL_PROTOCOL_$_AFSiriCapabilitiesServiceClientInterface
+ __OBJC_METACLASS_RO_$_AFApplicationGroupContainer
+ __OBJC_METACLASS_RO_$_AFSiriCapabilitiesServiceClient
+ __OBJC_METACLASS_RO_$_AFSpeechMessagesContext
+ __OBJC_METACLASS_RO_$_AFSpeechVisualContextAndCorrectionsInfo
+ __OBJC_PROTOCOL_$_AFSiriCapabilitiesServiceClientInterface
+ __OBJC_PROTOCOL_REFERENCE_$_AFSiriCapabilitiesServiceClientInterface
+ ___104-[AFMultiUserConnection getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]_block_invoke
+ ___104-[AFMultiUserConnection getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]_block_invoke_2
+ ___146-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:]_block_invoke
+ ___147-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:]_block_invoke
+ ___147-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:]_block_invoke_2
+ ___164-[AFSharedUserInfo initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:]_block_invoke
+ ___41-[AFSettingsConnection setReplayEnabled:]_block_invoke
+ ___45+[AFApplicationGroupContainer sharedInstance]_block_invoke
+ ___46-[AFSettingsConnection setReplayOverridePath:]_block_invoke
+ ___47-[AFHomeAnnouncementObserver _updateForReason:]_block_invoke
+ ___47-[AFHomeAnnouncementObserver _updateForReason:]_block_invoke_2
+ ___50-[AFSettingsConnection replayRecordedViewAt:with:]_block_invoke
+ ___52-[AFSettingsConnection replayAllRecordedViews:with:]_block_invoke
+ ___61-[AFConnectionClientServiceDelegate requestSetReplayEnabled:]_block_invoke
+ ___61-[AFSiriCapabilitiesServiceClient siriWithAppIntentsEnabled:]_block_invoke
+ ___61-[AFSiriCapabilitiesServiceClient siriWithAppIntentsEnabled:]_block_invoke_2
+ ___64+[AFFeatureFlags(SWEFeatureFlags) isHomePodNoTTSPerfTestEnabled]_block_invoke
+ ___64-[AFSettingsConnection mockHeadGesture:schedule:withCompletion:]_block_invoke
+ ___64-[AFSiriCapabilitiesServiceClient siriWithAppIntentsEnabledSync]_block_invoke
+ ___64-[AFSiriCapabilitiesServiceClient siriWithAppIntentsEnabledSync]_block_invoke_2
+ ___65-[AFSiriHeadphonesMonitor registerInternalGestureTestingHandler:]_block_invoke
+ ___66-[AFConnectionClientServiceDelegate requestSetReplayOverridePath:]_block_invoke
+ ___67-[AFSiriHeadphonesMonitor mockHeadGesture:schedule:withCompletion:]_block_invoke
+ ___68-[AFMultiUserConnection getPrimaryUserSharedUserInfoWithCompletion:]_block_invoke
+ ___68-[AFMultiUserConnection getPrimaryUserSharedUserInfoWithCompletion:]_block_invoke_2
+ ___70-[AFConnectionClientServiceDelegate requestReplayRecordedViewAt:with:]_block_invoke
+ ___72-[AFConnectionClientServiceDelegate requestReplayAllRecordedViews:with:]_block_invoke
+ ___72-[AFSiriCapabilitiesServiceClient siriSystemAssistantExperienceEnabled:]_block_invoke
+ ___72-[AFSiriCapabilitiesServiceClient siriSystemAssistantExperienceEnabled:]_block_invoke_2
+ ___75-[AFSiriCapabilitiesServiceClient siriSystemAssistantExperienceEnabledSync]_block_invoke
+ ___75-[AFSiriCapabilitiesServiceClient siriSystemAssistantExperienceEnabledSync]_block_invoke_2
+ ___76-[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:completion:]_block_invoke
+ ___79-[AFApplicationGroupContainer sharedApplicationGroupURLOnQueue:WithCompletion:]_block_invoke
+ ___83-[AFDictationConnection sendVisualContextAndCorrectionsInfo:interactionIdentifier:]_block_invoke
+ ___88-[AFSiriCapabilitiesServiceClient shouldDownloadAssetsForSiriSystemAssistantExperience:]_block_invoke
+ ___91-[AFSiriCapabilitiesServiceClient shouldDownloadAssetsForSiriSystemAssistantExperienceSync]_block_invoke
+ ___AFIsDeviceGreymatterEligible_block_invoke
+ ___AFLocaleIdentifierSupportsSAE_block_invoke
+ ___CloudSubscriptionFeaturesLibrary_block_invoke
+ ____AFRaiseToSpeakUnsupportedLocales_block_invoke
+ ____AllowedNowPlayingKeysAndTypes_block_invoke
+ ___block_descriptor_40_e8_32r_e17_v16?0"NSError"8l
+ ___block_descriptor_40_e8_32r_e8_v12?0B8l
+ ___block_descriptor_49_e8_32s_e8_v16?0Q8l
+ ___block_descriptor_57_e8_32s40bs_e5_v8?0l
+ ___block_descriptor_57_e8_32s_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48bs56w_e23_v16?0"BPSCompletion"8l
+ ___block_descriptor_75_e8_32s40s48s56s64s_e36_v16?0"<AFSharedUserInfoMutating>"8l
+ ___initCSFGMOptIn_block_invoke
+ ___useDeprecatedSAECheck_block_invoke
+ __block_literal_global.101.38626
+ __block_literal_global.104.38620
+ __block_literal_global.1045
+ __block_literal_global.10464
+ __block_literal_global.10521
+ __block_literal_global.10608
+ __block_literal_global.10675
+ __block_literal_global.107
+ __block_literal_global.108.22270
+ __block_literal_global.11168
+ __block_literal_global.112.22265
+ __block_literal_global.11699
+ __block_literal_global.1171
+ __block_literal_global.1175
+ __block_literal_global.1177
+ __block_literal_global.11778
+ __block_literal_global.1179
+ __block_literal_global.11805
+ __block_literal_global.1181
+ __block_literal_global.1183
+ __block_literal_global.1185
+ __block_literal_global.11880
+ __block_literal_global.120.22256
+ __block_literal_global.1201
+ __block_literal_global.12092
+ __block_literal_global.12362
+ __block_literal_global.12402
+ __block_literal_global.128.22250
+ __block_literal_global.12911
+ __block_literal_global.130.22247
+ __block_literal_global.1359
+ __block_literal_global.136.22239
+ __block_literal_global.13741
+ __block_literal_global.138.45612
+ __block_literal_global.13948
+ __block_literal_global.14105
+ __block_literal_global.144.22231
+ __block_literal_global.14430
+ __block_literal_global.14458
+ __block_literal_global.14568
+ __block_literal_global.15.26945
+ __block_literal_global.15.44146
+ __block_literal_global.150
+ __block_literal_global.150.45681
+ __block_literal_global.155
+ __block_literal_global.1558
+ __block_literal_global.160.22220
+ __block_literal_global.160.45690
+ __block_literal_global.165
+ __block_literal_global.16597
+ __block_literal_global.16734
+ __block_literal_global.16912
+ __block_literal_global.170
+ __block_literal_global.170.45700
+ __block_literal_global.17130
+ __block_literal_global.17164
+ __block_literal_global.17561
+ __block_literal_global.177
+ __block_literal_global.18
+ __block_literal_global.181.45617
+ __block_literal_global.183
+ __block_literal_global.18582
+ __block_literal_global.186.45716
+ __block_literal_global.18601
+ __block_literal_global.18944
+ __block_literal_global.19099
+ __block_literal_global.191
+ __block_literal_global.19139
+ __block_literal_global.19171
+ __block_literal_global.193
+ __block_literal_global.1937
+ __block_literal_global.19591
+ __block_literal_global.1961
+ __block_literal_global.19668
+ __block_literal_global.19725
+ __block_literal_global.198.45718
+ __block_literal_global.1999
+ __block_literal_global.20.19090
+ __block_literal_global.2002
+ __block_literal_global.201
+ __block_literal_global.20253
+ __block_literal_global.2028
+ __block_literal_global.203
+ __block_literal_global.205
+ __block_literal_global.20502
+ __block_literal_global.2058
+ __block_literal_global.20639
+ __block_literal_global.20706
+ __block_literal_global.20810
+ __block_literal_global.20935
+ __block_literal_global.20965
+ __block_literal_global.210.45740
+ __block_literal_global.2110
+ __block_literal_global.21377
+ __block_literal_global.215
+ __block_literal_global.216
+ __block_literal_global.218
+ __block_literal_global.22.46795
+ __block_literal_global.220
+ __block_literal_global.220.22191
+ __block_literal_global.222
+ __block_literal_global.22330
+ __block_literal_global.224
+ __block_literal_global.23257
+ __block_literal_global.23281
+ __block_literal_global.23364
+ __block_literal_global.235
+ __block_literal_global.237
+ __block_literal_global.23756
+ __block_literal_global.23938
+ __block_literal_global.244
+ __block_literal_global.25307
+ __block_literal_global.255
+ __block_literal_global.2569
+ __block_literal_global.26.10683
+ __block_literal_global.26168
+ __block_literal_global.26195
+ __block_literal_global.262
+ __block_literal_global.262.22128
+ __block_literal_global.26461
+ __block_literal_global.26659
+ __block_literal_global.26830
+ __block_literal_global.26965
+ __block_literal_global.271
+ __block_literal_global.27152
+ __block_literal_global.27316
+ __block_literal_global.278
+ __block_literal_global.28151
+ __block_literal_global.28341
+ __block_literal_global.2852
+ __block_literal_global.28750
+ __block_literal_global.28832
+ __block_literal_global.28927
+ __block_literal_global.29.45524
+ __block_literal_global.29235
+ __block_literal_global.29298
+ __block_literal_global.2939
+ __block_literal_global.296
+ __block_literal_global.29942
+ __block_literal_global.300
+ __block_literal_global.30069
+ __block_literal_global.30171
+ __block_literal_global.30214
+ __block_literal_global.307
+ __block_literal_global.31028
+ __block_literal_global.319
+ __block_literal_global.32663
+ __block_literal_global.3267
+ __block_literal_global.327
+ __block_literal_global.33082
+ __block_literal_global.3334
+ __block_literal_global.33585
+ __block_literal_global.3359
+ __block_literal_global.339
+ __block_literal_global.34254
+ __block_literal_global.347
+ __block_literal_global.348
+ __block_literal_global.34834
+ __block_literal_global.34965
+ __block_literal_global.35137
+ __block_literal_global.352
+ __block_literal_global.35215
+ __block_literal_global.36
+ __block_literal_global.36844
+ __block_literal_global.36864
+ __block_literal_global.37355
+ __block_literal_global.38.22324
+ __block_literal_global.38200
+ __block_literal_global.38227
+ __block_literal_global.38327
+ __block_literal_global.38394
+ __block_literal_global.38635
+ __block_literal_global.38828
+ __block_literal_global.39294
+ __block_literal_global.39345
+ __block_literal_global.398
+ __block_literal_global.40292
+ __block_literal_global.40326
+ __block_literal_global.40601
+ __block_literal_global.407
+ __block_literal_global.40824
+ __block_literal_global.41246
+ __block_literal_global.41461
+ __block_literal_global.41678
+ __block_literal_global.41785
+ __block_literal_global.43.22316
+ __block_literal_global.43017
+ __block_literal_global.43075
+ __block_literal_global.43677
+ __block_literal_global.43950
+ __block_literal_global.44042
+ __block_literal_global.44150
+ __block_literal_global.4497
+ __block_literal_global.45376
+ __block_literal_global.45510
+ __block_literal_global.463
+ __block_literal_global.46452
+ __block_literal_global.46478
+ __block_literal_global.46634
+ __block_literal_global.46785
+ __block_literal_global.4681
+ __block_literal_global.47.22309
+ __block_literal_global.47315
+ __block_literal_global.479
+ __block_literal_global.47979
+ __block_literal_global.48324
+ __block_literal_global.49.48315
+ __block_literal_global.5.48309
+ __block_literal_global.51.26837
+ __block_literal_global.538
+ __block_literal_global.54.26838
+ __block_literal_global.543
+ __block_literal_global.551
+ __block_literal_global.5586
+ __block_literal_global.5760
+ __block_literal_global.582
+ __block_literal_global.5829
+ __block_literal_global.590
+ __block_literal_global.590.46047
+ __block_literal_global.592
+ __block_literal_global.596
+ __block_literal_global.60.35139
+ __block_literal_global.606
+ __block_literal_global.61.23749
+ __block_literal_global.611
+ __block_literal_global.626
+ __block_literal_global.641
+ __block_literal_global.649
+ __block_literal_global.654
+ __block_literal_global.67.22297
+ __block_literal_global.68.35144
+ __block_literal_global.68.45543
+ __block_literal_global.6956
+ __block_literal_global.70.35145
+ __block_literal_global.7027
+ __block_literal_global.7054
+ __block_literal_global.72.22291
+ __block_literal_global.726
+ __block_literal_global.737
+ __block_literal_global.74.35146
+ __block_literal_global.742
+ __block_literal_global.75.43134
+ __block_literal_global.769
+ __block_literal_global.78.43131
+ __block_literal_global.783
+ __block_literal_global.814
+ __block_literal_global.815
+ __block_literal_global.8280
+ __block_literal_global.8318
+ __block_literal_global.8343
+ __block_literal_global.835
+ __block_literal_global.84.22286
+ __block_literal_global.8444
+ __block_literal_global.848
+ __block_literal_global.8496
+ __block_literal_global.85.30131
+ __block_literal_global.85.35129
+ __block_literal_global.850
+ __block_literal_global.852
+ __block_literal_global.86.22283
+ __block_literal_global.864
+ __block_literal_global.881
+ __block_literal_global.887
+ __block_literal_global.894
+ __block_literal_global.899
+ __block_literal_global.903
+ __block_literal_global.906
+ __block_literal_global.9099
+ __block_literal_global.92.38622
+ __block_literal_global.924
+ __block_literal_global.929
+ __block_literal_global.932
+ __block_literal_global.935
+ __block_literal_global.95.38632
+ __block_literal_global.98.38629
+ __block_literal_global.982
+ __block_literal_global.9903
+ __block_literal_global.992
+ __block_literal_global.996
+ __getBMSiriServiceClass_block_invoke.26978
+ __getBiomeLibrarySymbolLoc_block_invoke.45349
+ __initLSApplicationProxy_block_invoke.34258
+ __initLSApplicationProxy_block_invoke.45953
+ _checkGMAvailabilityWithUseCaseIdentifiers
+ _classCSFGMOptIn
+ _getBluetoothFirstDeviceUnlockCompleted
+ _getCSFGMOptInClass
+ _initCSFGMOptIn
+ _kAFAnnounceOnHeadphonesCachedEligibility
+ _kAFAssistantFilesystemDomain
+ _kAFBackedUpVisualIntelligenceCameraControlEnabled
+ _kAFLogContextFilesystem
+ _kAFSiriCapabilitiesDidChangeNotification
+ _kAFSiriCapabilitiesServiceClientEntitlement
+ _kAFSiriCapabilitiesServiceClientMachServiceName
+ _kAFSiriCapabilitiesServiceErrorDomain
+ _objc_msgSend$_fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:
+ _objc_msgSend$_updateForReason:
+ _objc_msgSend$allowHeadGestureInjection
+ _objc_msgSend$assistantConnection:replayAll:with:
+ _objc_msgSend$assistantConnection:replayAt:with:
+ _objc_msgSend$assistantConnection:setReplayEnabled:
+ _objc_msgSend$assistantConnection:setReplayOverridePath:
+ _objc_msgSend$containerURLForSecurityApplicationGroupIdentifier:
+ _objc_msgSend$currentWithUseCaseIdentifiers:language:
+ _objc_msgSend$deviceSupportsSAE
+ _objc_msgSend$fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:
+ _objc_msgSend$getIsDeviceOwner
+ _objc_msgSend$getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:
+ _objc_msgSend$getPrimaryUserSharedUserInfoWithCompletion:
+ _objc_msgSend$initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:
+ _objc_msgSend$isDeviceOwner
+ _objc_msgSend$isHomePodNoTTSPerfTestEnabled
+ _objc_msgSend$isOptedIn
+ _objc_msgSend$isPersistentSiriEnabled
+ _objc_msgSend$isSAEEnabled
+ _objc_msgSend$isSAEi18nEnabled
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$mockHeadGesture:schedule:withCompletion:
+ _objc_msgSend$path
+ _objc_msgSend$replayAllRecordedViews:with:
+ _objc_msgSend$replayRecordedViewAt:with:
+ _objc_msgSend$saeAvailable
+ _objc_msgSend$sendVisualContextAndCorrectionsInfo:interactionIdentifier:
+ _objc_msgSend$setDeviceSupportsSAE:
+ _objc_msgSend$setIsDeviceOwner:
+ _objc_msgSend$setReplayEnabled:
+ _objc_msgSend$setReplayOverridePath:
+ _objc_msgSend$setSaeAvailable:
+ _objc_msgSend$setSwaiEnabled:
+ _objc_msgSend$setVisualIntelligenceEnabled:
+ _objc_msgSend$sharedApplicationGroupURL:
+ _objc_msgSend$shouldDownloadAssetsForSiriSystemAssistantExperience:
+ _objc_msgSend$swaiEnabled
+ _objc_msgSend$syncServiceWithErrorHandler:
+ _objc_msgSend$triggerVoiceProfileUploadWithCompletion:completion:
+ _objc_msgSend$visualIntelligenceEnabled
+ audit_stringBiomeLibrary.26960
+ audit_stringBiomeLibrary.45363
+ audit_stringIntents.30896
+ classLSApplicationProxy.34255
+ classLSApplicationProxy.45951
+ getBMSiriServiceClass.softClass.26977
+ getBiomeLibrarySymbolLoc.ptr.45348
+ getBluetoothPairedStatusChangedNotification.45458
+ getLSApplicationProxyClass.34247
+ getLSApplicationProxyClass.45947
+ initCSFGMOptIn.sOnce
+ initLSApplicationProxy.34252
+ initLSApplicationProxy.45949
+ initLSApplicationProxy.sOnce.34253
+ initLSApplicationProxy.sOnce.45950
+ isHomePodNoTTSPerfTestEnabled.isDefaultSet
+ isHomePodNoTTSPerfTestEnabled.once
+ sharedInstance.instance
+ sharedInstance.onceToken.17129
+ sharedInstance.onceToken.22360
+ sharedInstance.onceToken.23256
+ sharedInstance.onceToken.28340
+ sharedInstance.onceToken.36863
+ sharedInstance.onceToken.44168
+ sharedInstance.singleton.44169
+ sharedManager.onceToken.16596
+ sharedManager.onceToken.21859
+ sharedManager.onceToken.32662
+ sharedManager.onceToken.43016
+ sharedManager.result.32664
+ sharedManager.sharedManager.43018
+ sharedMonitor.onceToken.20267
+ sharedObserver.onceToken.31027
+ sharedObserver.onceToken.45461
+ sharedObserver.onceToken.48323
+ sharedObserver.sharedObserver.31029
+ sharedObserver.sharedObserver.48325
+ useDeprecatedSAECheck.onceToken
+ useDeprecatedSAECheck.result
- -[AFAWDSiriLinkRecommendationInfo beaconPER]
- -[AFAWDSiriLinkRecommendationInfo btPreference]
- -[AFAWDSiriLinkRecommendationInfo btRSSI]
- -[AFAWDSiriLinkRecommendationInfo btRetransmissionRateRx]
- -[AFAWDSiriLinkRecommendationInfo btRetransmissionRateTx]
- -[AFAWDSiriLinkRecommendationInfo btTech]
- -[AFAWDSiriLinkRecommendationInfo expectedThroughputVIBE]
- -[AFAWDSiriLinkRecommendationInfo lsmRecommendationBe]
- -[AFAWDSiriLinkRecommendationInfo nwType]
- -[AFAWDSiriLinkRecommendationInfo packetLifetimeVIBE]
- -[AFAWDSiriLinkRecommendationInfo packetLossRateVIBE]
- -[AFAWDSiriLinkRecommendationInfo setBeaconPER:]
- -[AFAWDSiriLinkRecommendationInfo setBtPreference:]
- -[AFAWDSiriLinkRecommendationInfo setBtRSSI:]
- -[AFAWDSiriLinkRecommendationInfo setBtRetransmissionRateRx:]
- -[AFAWDSiriLinkRecommendationInfo setBtRetransmissionRateTx:]
- -[AFAWDSiriLinkRecommendationInfo setBtTech:]
- -[AFAWDSiriLinkRecommendationInfo setExpectedThroughputVIBE:]
- -[AFAWDSiriLinkRecommendationInfo setLsmRecommendationBe:]
- -[AFAWDSiriLinkRecommendationInfo setNwType:]
- -[AFAWDSiriLinkRecommendationInfo setPacketLifetimeVIBE:]
- -[AFAWDSiriLinkRecommendationInfo setPacketLossRateVIBE:]
- -[AFAWDSiriLinkRecommendationInfo setTimeTaken:]
- -[AFAWDSiriLinkRecommendationInfo setWifiCCA:]
- -[AFAWDSiriLinkRecommendationInfo setWifiPreference:]
- -[AFAWDSiriLinkRecommendationInfo setWifiRSSI:]
- -[AFAWDSiriLinkRecommendationInfo setWifiSNR:]
- -[AFAWDSiriLinkRecommendationInfo timeTaken]
- -[AFAWDSiriLinkRecommendationInfo wifiCCA]
- -[AFAWDSiriLinkRecommendationInfo wifiPreference]
- -[AFAWDSiriLinkRecommendationInfo wifiRSSI]
- -[AFAWDSiriLinkRecommendationInfo wifiSNR]
- -[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObservers]
- -[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:]
- -[AFSharedUserInfo initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:]
- AFLocaleSupportsSAE.once
- AFLocaleSupportsSAE.supportedLocales
- BiomeLibraryLibraryCore.45127
- BiomeLibraryLibraryCore.frameworkLibrary.26909
- BiomeLibraryLibraryCore.frameworkLibrary.45130
- BluetoothManagerLibrary.45227
- GCC_except_table10098
- GCC_except_table1025
- GCC_except_table10412
- GCC_except_table10578
- GCC_except_table10591
- GCC_except_table10769
- GCC_except_table10887
- GCC_except_table10900
- GCC_except_table1092
- GCC_except_table10931
- GCC_except_table11171
- GCC_except_table11322
- GCC_except_table11341
- GCC_except_table11344
- GCC_except_table11346
- GCC_except_table1243
- GCC_except_table1245
- GCC_except_table1434
- GCC_except_table1471
- GCC_except_table1483
- GCC_except_table1585
- GCC_except_table1591
- GCC_except_table1594
- GCC_except_table1659
- GCC_except_table1726
- GCC_except_table1748
- GCC_except_table1754
- GCC_except_table1996
- GCC_except_table2040
- GCC_except_table2208
- GCC_except_table2263
- GCC_except_table2331
- GCC_except_table2694
- GCC_except_table2701
- GCC_except_table2705
- GCC_except_table2707
- GCC_except_table2739
- GCC_except_table2741
- GCC_except_table2747
- GCC_except_table2753
- GCC_except_table2761
- GCC_except_table2764
- GCC_except_table2766
- GCC_except_table2775
- GCC_except_table2779
- GCC_except_table2794
- GCC_except_table2816
- GCC_except_table2818
- GCC_except_table2820
- GCC_except_table2822
- GCC_except_table2824
- GCC_except_table2826
- GCC_except_table2869
- GCC_except_table2894
- GCC_except_table2949
- GCC_except_table2979
- GCC_except_table3250
- GCC_except_table3306
- GCC_except_table3428
- GCC_except_table3447
- GCC_except_table3453
- GCC_except_table3458
- GCC_except_table3462
- GCC_except_table3468
- GCC_except_table3556
- GCC_except_table3558
- GCC_except_table3575
- GCC_except_table3581
- GCC_except_table3623
- GCC_except_table3635
- GCC_except_table3705
- GCC_except_table3808
- GCC_except_table3815
- GCC_except_table3830
- GCC_except_table3867
- GCC_except_table3955
- GCC_except_table4009
- GCC_except_table4406
- GCC_except_table4407
- GCC_except_table453
- GCC_except_table4694
- GCC_except_table4707
- GCC_except_table4767
- GCC_except_table4832
- GCC_except_table4842
- GCC_except_table4853
- GCC_except_table4867
- GCC_except_table4988
- GCC_except_table504
- GCC_except_table523
- GCC_except_table5482
- GCC_except_table5571
- GCC_except_table5575
- GCC_except_table5691
- GCC_except_table5790
- GCC_except_table5811
- GCC_except_table5897
- GCC_except_table5903
- GCC_except_table6024
- GCC_except_table6031
- GCC_except_table6376
- GCC_except_table6391
- GCC_except_table6416
- GCC_except_table6521
- GCC_except_table6559
- GCC_except_table6658
- GCC_except_table706
- GCC_except_table709
- GCC_except_table7366
- GCC_except_table7378
- GCC_except_table7602
- GCC_except_table7702
- GCC_except_table7734
- GCC_except_table7920
- GCC_except_table7925
- GCC_except_table7989
- GCC_except_table8095
- GCC_except_table835
- GCC_except_table8475
- GCC_except_table8526
- GCC_except_table8570
- GCC_except_table8667
- GCC_except_table8672
- GCC_except_table8673
- GCC_except_table8677
- GCC_except_table8920
- GCC_except_table8992
- GCC_except_table8998
- GCC_except_table9035
- GCC_except_table9038
- GCC_except_table9116
- GCC_except_table9144
- GCC_except_table9216
- GCC_except_table9223
- GCC_except_table9331
- GCC_except_table9335
- GCC_except_table9339
- GCC_except_table9372
- GCC_except_table9852
- GCC_except_table9854
- GCC_except_table9857
- GCC_except_table9866
- GCC_except_table9892
- GCC_except_table9907
- IntentsLibraryCore.frameworkLibrary.30800
- LSApplicationProxyFunction.34046
- LSApplicationProxyFunction.45706
- LaunchServicesLibrary.frameworkLibrary.45701
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._beaconPER
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btPreference
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btRSSI
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btRetransmissionRateRx
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btRetransmissionRateTx
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._btTech
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._expectedThroughputVIBE
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._lsmRecommendationBe
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._nwType
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._packetLifetimeVIBE
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._packetLossRateVIBE
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._timeTaken
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._wifiCCA
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._wifiPreference
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._wifiRSSI
- OBJC_IVAR_$_AFAWDSiriLinkRecommendationInfo._wifiSNR
- SoftBiomeLibrary.45113
- _ACXPCEventSubscriberFunction
- _AccountsLibrary
- _HandleGenerativeModelsAvailabilityDidChange
- _OBJC_CLASS_$_AFAWDSiriLinkRecommendationInfo
- _OBJC_METACLASS_$_AFAWDSiriLinkRecommendationInfo
- _WhitelistedNowPlayingKeysAndTypes.makeSchemaOnlyOnceGuard
- _WhitelistedNowPlayingKeysAndTypes.schema
- __105-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesWithCompletion:]_block_invoke.28
- __105-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesWithCompletion:]_block_invoke.36
- __105-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesWithCompletion:]_block_invoke_2.29
- __105-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesWithCompletion:]_block_invoke_3.30
- __106-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchAvailableAnnouncementRequestTypesWithCompletion:]_block_invoke.37
- __106-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchAvailableAnnouncementRequestTypesWithCompletion:]_block_invoke.42
- __30-[AFMyriadCoordinator endTask]_block_invoke.322
- __40-[AFMyriadCoordinator _advertiseTrigger]_block_invoke.495
- __40-[AFMyriadCoordinator _advertiseTrigger]_block_invoke.499
- __40-[AFMyriadCoordinator _advertiseTrigger]_block_invoke.500
- __43-[AFSettingsConnection dumpAssistantState:]_block_invoke.263
- __44-[AFSettingsConnection currectNWActivityId:]_block_invoke.149
- __46-[AFMyriadCoordinator _waitWiProx:andExecute:]_block_invoke.550
- __47-[AFSettingsConnection startUIRequestWithInfo:]_block_invoke.182
- __47-[AFSettingsConnection startUIRequestWithText:]_block_invoke.177
- __48-[AFSettingsConnection siriDesignModeIsEnabled:]_block_invoke.256
- __50-[AFSettingsConnection areSiriSAEAssetsAvailable:]_block_invoke.262
- __55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke.281
- __55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke.304
- __55-[AFMyriadCoordinator _endAdvertisingAnalyticsContext:]_block_invoke.315
- __56-[AFMyriadCoordinator _createWaitWiProxTimer:waitBlock:]_block_invoke.549
- __56-[AFSettingsConnection isSearchDataSharingStatusForced:]_block_invoke.259
- __57-[AFSettingsConnection setIsHomePodInHH2Mode:completion:]_block_invoke.250
- __58-[AFSettingsConnection getSearchQueriesDataSharingStatus:]_block_invoke.258
- __60-[AFSettingsConnection multiUserCompanionDeviceIdentifiers:]_block_invoke.236
- __60-[AFSettingsConnection setSiriDesignModeEnabled:completion:]_block_invoke.255
- __60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.583
- __62-[AFSettingsConnection getCurrentAccessoryInfoWithCompletion:]_block_invoke.163
- __62-[AFSettingsConnection getPersonalMultiUserDeviceIdentifiers:]_block_invoke.235
- __64-[AFConnectionClientServiceDelegate requestHandleCommand:reply:]_block_invoke.812
- __64-[AFSettingsConnection shouldSuppressSiriDataSharingOptInAlert:]_block_invoke.253
- __65-[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:]_block_invoke.13
- __65-[AFSettingsConnection setSiriDataSharingOptInStatus:completion:]_block_invoke.243
- __66-[AFDictationConnectionServiceDelegate speechDidRecognizePackage:]_block_invoke.570
- __68-[AFSettingsConnection deleteSiriHistoryWithContext:withCompletion:]_block_invoke.254
- __68-[AFSettingsConnection getSiriDataSharingOptInStatusWithCompletion:]_block_invoke.244
- __69-[AFSettingsConnection setSearchQueriesDataSharingStatus:completion:]_block_invoke.257
- __73-[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke.511
- __73-[AFMyriadCoordinator _advertiseWith:afterDelay:maxInterval:thenExecute:]_block_invoke.531
- __73-[AFSettingsConnection setSiriDataSharingOptInAlertPresented:completion:]_block_invoke.248
- __76-[AFMyriadCoordinator _updateArbitrationParticipationContextWithCompletion:]_block_invoke.481
- __77-[AFSettingsConnection _createRadarWithReason:room:process:crash:completion:]_block_invoke.276
- __79-[AFSettingsConnection setSiriDataSharingHomePodSetupDeviceIsValid:completion:]_block_invoke.249
- __83+[AFDictationConnection getForcedOfflineDictationSupportedLanguagesWithCompletion:]_block_invoke.259
- __89-[AFPreferences getAnnounceNotificationsTemporarilyDisabledStatusForPlatform:completion:]_block_invoke.1192
- __89-[AFPreferences getAnnounceNotificationsTemporarilyDisabledStatusForPlatform:completion:]_block_invoke.1195
- __90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.116
- __90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.121
- __92-[AFDictationConnectionServiceDelegate speechDidRecognizeTokens:nluResult:usingSpeechModel:]_block_invoke.573
- __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.319
- __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.322
- __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.327
- __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.333
- __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.337
- __97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke_2.338
- __99-[AFSettingsConnection(Internal) _updateMultiUserInfoForUser:score:companionInfo:reset:completion:]_block_invoke.582
- __BiomeLibraryLibraryCore_block_invoke.26910
- __BiomeLibraryLibraryCore_block_invoke.45131
- __Block_byref_object_copy_.10168
- __Block_byref_object_copy_.10710
- __Block_byref_object_copy_.10894
- __Block_byref_object_copy_.11532
- __Block_byref_object_copy_.12098
- __Block_byref_object_copy_.13363
- __Block_byref_object_copy_.13612
- __Block_byref_object_copy_.17095
- __Block_byref_object_copy_.17574
- __Block_byref_object_copy_.19826
- __Block_byref_object_copy_.20286
- __Block_byref_object_copy_.21289
- __Block_byref_object_copy_.22211
- __Block_byref_object_copy_.22886
- __Block_byref_object_copy_.23276
- __Block_byref_object_copy_.23880
- __Block_byref_object_copy_.28714
- __Block_byref_object_copy_.30378
- __Block_byref_object_copy_.315
- __Block_byref_object_copy_.34457
- __Block_byref_object_copy_.34906
- __Block_byref_object_copy_.37127
- __Block_byref_object_copy_.38309
- __Block_byref_object_copy_.41436
- __Block_byref_object_copy_.45821
- __Block_byref_object_copy_.46992
- __Block_byref_object_copy_.47722
- __Block_byref_object_copy_.48002
- __Block_byref_object_copy_.5473
- __Block_byref_object_copy_.5879
- __Block_byref_object_copy_.8016
- __Block_byref_object_copy_.8906
- __Block_byref_object_dispose_.10169
- __Block_byref_object_dispose_.10711
- __Block_byref_object_dispose_.10895
- __Block_byref_object_dispose_.11533
- __Block_byref_object_dispose_.12099
- __Block_byref_object_dispose_.13364
- __Block_byref_object_dispose_.13613
- __Block_byref_object_dispose_.17096
- __Block_byref_object_dispose_.17575
- __Block_byref_object_dispose_.19827
- __Block_byref_object_dispose_.20287
- __Block_byref_object_dispose_.21290
- __Block_byref_object_dispose_.22212
- __Block_byref_object_dispose_.22887
- __Block_byref_object_dispose_.23277
- __Block_byref_object_dispose_.23881
- __Block_byref_object_dispose_.28715
- __Block_byref_object_dispose_.30379
- __Block_byref_object_dispose_.316
- __Block_byref_object_dispose_.34458
- __Block_byref_object_dispose_.34907
- __Block_byref_object_dispose_.37128
- __Block_byref_object_dispose_.38310
- __Block_byref_object_dispose_.41437
- __Block_byref_object_dispose_.45822
- __Block_byref_object_dispose_.46993
- __Block_byref_object_dispose_.47723
- __Block_byref_object_dispose_.48003
- __Block_byref_object_dispose_.5474
- __Block_byref_object_dispose_.5880
- __Block_byref_object_dispose_.8017
- __Block_byref_object_dispose_.8907
- __IntentsLibraryCore_block_invoke.30801
- __OBJC_$_CLASS_METHODS_AFSystemAssistantExperienceStatusManager
- __OBJC_$_INSTANCE_METHODS_AFAWDSiriLinkRecommendationInfo
- __OBJC_$_INSTANCE_VARIABLES_AFAWDSiriLinkRecommendationInfo
- __OBJC_$_PROP_LIST_AFAWDSiriLinkRecommendationInfo
- __OBJC_CLASS_RO_$_AFAWDSiriLinkRecommendationInfo
- __OBJC_METACLASS_RO_$_AFAWDSiriLinkRecommendationInfo
- ___109-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObservers]_block_invoke
- ___109-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObservers]_block_invoke_2
- ___109-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesAndNotifyObservers:]_block_invoke
- ___150-[AFSharedUserInfo initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:]_block_invoke
- ___53-[AFFamilyCircleStatusManager _observeAccountChanges]_block_invoke
- ___54-[AFHomeAnnouncementObserver initWithInstanceContext:]_block_invoke_2
- ___56-[AFHomeAnnouncementObserver getSnapshotWithCompletion:]_block_invoke_3
- ___65-[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:]_block_invoke
- ___77-[AFHomeAnnouncementObserver notifyObserver:didReceiveNotificationWithToken:]_block_invoke
- ___AFLocaleSupportsSAE_block_invoke
- ____WhitelistedNowPlayingKeysAndTypes_block_invoke
- ___block_descriptor_40_e8_32w_e22_v20?0"ACAccount"8i16l
- ___block_descriptor_48_e8_32s_e8_v16?0Q8l
- ___block_descriptor_74_e8_32s40s48s56s64s_e36_v16?0"<AFSharedUserInfoMutating>"8l
- ___initACXPCEventSubscriber_block_invoke
- __block_literal_global.101.38423
- __block_literal_global.1039
- __block_literal_global.104.38417
- __block_literal_global.10504
- __block_literal_global.10561
- __block_literal_global.10648
- __block_literal_global.10715
- __block_literal_global.108.22333
- __block_literal_global.109
- __block_literal_global.1119
- __block_literal_global.112.22327
- __block_literal_global.11208
- __block_literal_global.1138
- __block_literal_global.1142
- __block_literal_global.1144
- __block_literal_global.1146
- __block_literal_global.1148
- __block_literal_global.1150
- __block_literal_global.1168
- __block_literal_global.11730
- __block_literal_global.11809
- __block_literal_global.11836
- __block_literal_global.11911
- __block_literal_global.12
- __block_literal_global.120.22319
- __block_literal_global.12121
- __block_literal_global.12390
- __block_literal_global.12430
- __block_literal_global.128.22313
- __block_literal_global.12935
- __block_literal_global.130.22308
- __block_literal_global.132.45373
- __block_literal_global.136.22302
- __block_literal_global.13755
- __block_literal_global.13960
- __block_literal_global.1402
- __block_literal_global.14117
- __block_literal_global.144.22294
- __block_literal_global.144.45440
- __block_literal_global.14436
- __block_literal_global.14464
- __block_literal_global.14574
- __block_literal_global.149
- __block_literal_global.15.26897
- __block_literal_global.15.43925
- __block_literal_global.154
- __block_literal_global.158
- __block_literal_global.159
- __block_literal_global.1607
- __block_literal_global.162
- __block_literal_global.16604
- __block_literal_global.16741
- __block_literal_global.168.22277
- __block_literal_global.16919
- __block_literal_global.17137
- __block_literal_global.17171
- __block_literal_global.175
- __block_literal_global.17567
- __block_literal_global.176.22272
- __block_literal_global.179
- __block_literal_global.180
- __block_literal_global.184
- __block_literal_global.185
- __block_literal_global.18588
- __block_literal_global.18607
- __block_literal_global.187
- __block_literal_global.18949
- __block_literal_global.1900
- __block_literal_global.19104
- __block_literal_global.19144
- __block_literal_global.19176
- __block_literal_global.192.45478
- __block_literal_global.195
- __block_literal_global.19694
- __block_literal_global.197
- __block_literal_global.19771
- __block_literal_global.19828
- __block_literal_global.1983
- __block_literal_global.1986
- __block_literal_global.199
- __block_literal_global.1998
- __block_literal_global.20.19095
- __block_literal_global.20327
- __block_literal_global.204.45500
- __block_literal_global.2042
- __block_literal_global.20577
- __block_literal_global.2064
- __block_literal_global.207
- __block_literal_global.20714
- __block_literal_global.20781
- __block_literal_global.20885
- __block_literal_global.209
- __block_literal_global.21010
- __block_literal_global.21040
- __block_literal_global.21433
- __block_literal_global.2146
- __block_literal_global.217
- __block_literal_global.22.46495
- __block_literal_global.22393
- __block_literal_global.225
- __block_literal_global.23.45294
- __block_literal_global.23328
- __block_literal_global.23352
- __block_literal_global.234
- __block_literal_global.23435
- __block_literal_global.23827
- __block_literal_global.24009
- __block_literal_global.251
- __block_literal_global.25375
- __block_literal_global.254
- __block_literal_global.26.10723
- __block_literal_global.261
- __block_literal_global.2610
- __block_literal_global.26120
- __block_literal_global.26147
- __block_literal_global.26413
- __block_literal_global.26611
- __block_literal_global.26782
- __block_literal_global.26917
- __block_literal_global.27103
- __block_literal_global.272
- __block_literal_global.27267
- __block_literal_global.28101
- __block_literal_global.28670
- __block_literal_global.28752
- __block_literal_global.28847
- __block_literal_global.2892
- __block_literal_global.290
- __block_literal_global.29155
- __block_literal_global.29218
- __block_literal_global.294
- __block_literal_global.2979
- __block_literal_global.29863
- __block_literal_global.29990
- __block_literal_global.30091
- __block_literal_global.301
- __block_literal_global.30134
- __block_literal_global.30947
- __block_literal_global.318.13618
- __block_literal_global.32448
- __block_literal_global.326
- __block_literal_global.32853
- __block_literal_global.3309
- __block_literal_global.33369
- __block_literal_global.336
- __block_literal_global.3376
- __block_literal_global.3401
- __block_literal_global.34039
- __block_literal_global.343
- __block_literal_global.345
- __block_literal_global.34619
- __block_literal_global.34750
- __block_literal_global.34922
- __block_literal_global.34999
- __block_literal_global.351
- __block_literal_global.36629
- __block_literal_global.36649
- __block_literal_global.37.45097
- __block_literal_global.37148
- __block_literal_global.374
- __block_literal_global.37996
- __block_literal_global.38.22387
- __block_literal_global.38023
- __block_literal_global.38123
- __block_literal_global.38191
- __block_literal_global.38432
- __block_literal_global.38625
- __block_literal_global.39088
- __block_literal_global.39139
- __block_literal_global.395
- __block_literal_global.40086
- __block_literal_global.40120
- __block_literal_global.40395
- __block_literal_global.40618
- __block_literal_global.41033
- __block_literal_global.41248
- __block_literal_global.41465
- __block_literal_global.41572
- __block_literal_global.42803
- __block_literal_global.42861
- __block_literal_global.43462
- __block_literal_global.43736
- __block_literal_global.43828
- __block_literal_global.43929
- __block_literal_global.44
- __block_literal_global.451
- __block_literal_global.45146
- __block_literal_global.45280
- __block_literal_global.4539
- __block_literal_global.46152
- __block_literal_global.46178
- __block_literal_global.46334
- __block_literal_global.46485
- __block_literal_global.47014
- __block_literal_global.4723
- __block_literal_global.47678
- __block_literal_global.48
- __block_literal_global.48023
- __block_literal_global.484
- __block_literal_global.49.48014
- __block_literal_global.5.48008
- __block_literal_global.51.26789
- __block_literal_global.53.22371
- __block_literal_global.535
- __block_literal_global.537
- __block_literal_global.54.26790
- __block_literal_global.548
- __block_literal_global.5624
- __block_literal_global.573
- __block_literal_global.573.22484
- __block_literal_global.575
- __block_literal_global.577
- __block_literal_global.578
- __block_literal_global.579
- __block_literal_global.5798
- __block_literal_global.5867
- __block_literal_global.587
- __block_literal_global.60.34924
- __block_literal_global.61.23820
- __block_literal_global.614
- __block_literal_global.617
- __block_literal_global.62
- __block_literal_global.637
- __block_literal_global.642
- __block_literal_global.67.22362
- __block_literal_global.68.34929
- __block_literal_global.6981
- __block_literal_global.70.34930
- __block_literal_global.7052
- __block_literal_global.7079
- __block_literal_global.714
- __block_literal_global.72.22356
- __block_literal_global.725
- __block_literal_global.730
- __block_literal_global.74.34931
- __block_literal_global.75.42920
- __block_literal_global.756
- __block_literal_global.761
- __block_literal_global.78.42917
- __block_literal_global.787
- __block_literal_global.805
- __block_literal_global.817
- __block_literal_global.819
- __block_literal_global.8312
- __block_literal_global.833
- __block_literal_global.8350
- __block_literal_global.8375
- __block_literal_global.839
- __block_literal_global.84.22351
- __block_literal_global.846
- __block_literal_global.8474
- __block_literal_global.85.30052
- __block_literal_global.85.34914
- __block_literal_global.851
- __block_literal_global.8526
- __block_literal_global.855
- __block_literal_global.858
- __block_literal_global.86.22348
- __block_literal_global.866
- __block_literal_global.882
- __block_literal_global.9116
- __block_literal_global.92.38419
- __block_literal_global.94.22342
- __block_literal_global.95.38429
- __block_literal_global.979
- __block_literal_global.98.38426
- __block_literal_global.989
- __block_literal_global.9923
- __block_literal_global.993
- __getBMSiriServiceClass_block_invoke.26929
- __getBiomeLibrarySymbolLoc_block_invoke.45119
- __initLSApplicationProxy_block_invoke.34043
- __initLSApplicationProxy_block_invoke.45700
- _classACXPCEventSubscriber
- _getACXPCEventSubscriberClass
- _initACXPCEventSubscriber
- _objc_msgSend$_fetchEligibleAnnouncementRequestTypesAndNotifyObservers
- _objc_msgSend$fetchEligibleAnnouncementRequestTypesAndNotifyObservers:
- _objc_msgSend$initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:
- _objc_msgSend$recordAWDSuccessMetrics
- _objc_msgSend$registerAccountChangeEventHandler:
- _objc_msgSend$sharedSubscriber
- _objc_msgSend$triggerVoiceProfileUploadWithCompletion:
- audit_stringBiomeLibrary.26912
- audit_stringBiomeLibrary.45133
- audit_stringIntents.30815
- classLSApplicationProxy.34040
- classLSApplicationProxy.45698
- getBMSiriServiceClass.softClass.26928
- getBiomeLibrarySymbolLoc.ptr.45118
- getLSApplicationProxyClass.34032
- getLSApplicationProxyClass.45694
- initACXPCEventSubscriber.sOnce
- initLSApplicationProxy.34037
- initLSApplicationProxy.45696
- initLSApplicationProxy.sOnce.34038
- initLSApplicationProxy.sOnce.45697
- sharedInstance.onceToken.17136
- sharedInstance.onceToken.22424
- sharedInstance.onceToken.23327
- sharedInstance.onceToken.36648
- sharedInstance.onceToken.43947
- sharedInstance.singleton.43948
- sharedManager.onceToken.16603
- sharedManager.onceToken.21931
- sharedManager.onceToken.32447
- sharedManager.onceToken.42802
- sharedManager.result.32449
- sharedManager.sharedManager.42804
- sharedMonitor.onceToken.20342
- sharedObserver.onceToken.30946
- sharedObserver.onceToken.45233
- sharedObserver.onceToken.48022
- sharedObserver.sharedObserver.30948
- sharedObserver.sharedObserver.48024
CStrings:
+ "\x1b\\pause=2000\\"
+ "%@ {sharedUserId = %@, loggableSharedUserId = %@, companionDeviceInfo = %@, personalRequestsEnabled = %@, companionLinkReady = %@, homeUserId = %@, iCloudAltDSID = %@, isDeviceOwner = %@}"
+ "%@, messagesContext=%@, recognizedText=%@ correctedText=%@"
+ "%@, sender=%@, messages=%@"
+ "%s #AppleIntelligence optIn status: %d"
+ "%s #ReplayAll. intervalSeconds: %lu,  recordingDataURL: %@"
+ "%s #ReplayAt. index: %lu,  recordingDataURL: %@"
+ "%s #SAEStatus available from cache:%d"
+ "%s #SAEStatus enabled from cache:%d"
+ "%s #preferences Setting Visual Intelligence Camera Control %@"
+ "%s #visualIntelligenceStatus from cache:%d"
+ "%s #visualIntelligenceStatus:%d"
+ "%s %@ Sampling: Error retrieving file attributes: %@"
+ "%s %@ Sampling: File at path %@ is empty."
+ "%s %@ Sampling: No file exists at path %@"
+ "%s %p Skipping timeouts and interstitials for testing"
+ "%s AFOpportuneSpeakingModelFeedback was deallocated"
+ "%s Application group container path not found"
+ "%s Complete with error: %@ for sharedUserId: %@"
+ "%s Error in getLoggableIdentiferForUserWithiCloudAltDSID:%@"
+ "%s Error in getPrimaryUserSharedUserInfoWithCompletion:%@"
+ "%s Failed to determine GM eligibility with status code: %d"
+ "%s Fetched AFDeviceSupportsSAEDeprecated: %@"
+ "%s Fetching AFDeviceSupportsSAEDeprecated"
+ "%s Got container URL: %@"
+ "%s Loading GMS availability via deprecated SPI"
+ "%s Loading GMS availability via locale based SPI"
+ "%s Locale is nil, returning unavailable"
+ "%s SAE enabled status: %@"
+ "%s SWAI status: %@"
+ "%s Unknown BPSCompletion status"
+ "%s cached announce eligiblity state: %lu"
+ "%s deviceSupportsSAE from cache:%d"
+ "%s languageCode cannot be nil."
+ "%s previous announcement request eligibility: %lu, now updating to %lu shouldRelyOnCachedStateIfIneligbile: %d"
+ "%s sharedUserID: %@"
+ "%s shouldRelyOnCachedStateIfIneligbile: %d"
+ "%s swaiEnabled from cache:%d"
+ "%s updating cached announce notification eligiblity state to: %d"
+ "%s using cached announce notification eligiblity state: %lu"
+ "%s 🧪 Head gesture injection is not allowed, execute as a non-root user: defaults write com.apple.assistant \"Allow Head Gesture Injection\" -bool true && killall -9 assistantd"
+ "%s 🧪 Mocking gesture: %@"
+ "%s 🧪 Registered internal gesture testing handler: %@"
+ "%s 🧪 Scheduling pending gesture with testing handler: %@"
+ "+[AFSamplingUtilities fileExistsAndNotEmpty:samplingComponent:]"
+ "+[AFSystemAssistantExperienceStatusManager deviceSupportsSAE]"
+ "+[AFSystemAssistantExperienceStatusManager isVisualIntelligenceEnabled]"
+ "+[AFSystemAssistantExperienceStatusManager saeAvailable]"
+ "+[AFSystemAssistantExperienceStatusManager swaiEnabled]"
+ "-[AFApplicationGroupContainer sharedApplicationGroupURL:]"
+ "-[AFConnectionClientServiceDelegate requestReplayAllRecordedViews:with:]_block_invoke"
+ "-[AFConnectionClientServiceDelegate requestReplayRecordedViewAt:with:]_block_invoke"
+ "-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:]"
+ "-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:]_block_invoke"
+ "-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:]_block_invoke_2"
+ "-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchInitialState]_block_invoke"
+ "-[AFHeadphonesAnnouncementRequestCapabilityProvider fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:]"
+ "-[AFMultiUserConnection getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]"
+ "-[AFMultiUserConnection getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:]_block_invoke_2"
+ "-[AFMultiUserConnection getPrimaryUserSharedUserInfoWithCompletion:]"
+ "-[AFMultiUserConnection getPrimaryUserSharedUserInfoWithCompletion:]_block_invoke_2"
+ "-[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:completion:]"
+ "-[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:completion:]_block_invoke"
+ "-[AFSettingsConnection mockHeadGesture:schedule:withCompletion:]_block_invoke"
+ "-[AFSettingsConnection replayAllRecordedViews:with:]"
+ "-[AFSettingsConnection replayAllRecordedViews:with:]_block_invoke"
+ "-[AFSettingsConnection replayRecordedViewAt:with:]"
+ "-[AFSettingsConnection replayRecordedViewAt:with:]_block_invoke"
+ "-[AFSettingsConnection setReplayEnabled:]_block_invoke"
+ "-[AFSettingsConnection setReplayOverridePath:]_block_invoke"
+ "-[AFSiriHeadphonesMonitor mockHeadGesture:schedule:withCompletion:]_block_invoke"
+ "-[AFSiriHeadphonesMonitor registerInternalGestureTestingHandler:]_block_invoke"
+ "/System/Library/PrivateFrameworks/CloudSubscriptionFeatures.framework/CloudSubscriptionFeatures"
+ ">\xd8\xea\xdd "
+ "@68@0:8@16@24@32B40B44@48@56B64"
+ "AFApplicationGroupContainer"
+ "AFDeviceSupportsSAEDeprecated"
+ "AFFilesystem"
+ "AFIsAppleIntelligenceEnabled"
+ "AFIsDeviceGreymatterEligible_block_invoke"
+ "AFSharedUserInfo::isDeviceOwner"
+ "AFSiriCapabilitiesServiceClient"
+ "AFSiriCapabilitiesServiceClientInterface"
+ "AFSpeechMessagesContext"
+ "AFSpeechVisualContextAndCorrectionsInfo"
+ "AUTO_ANSWER"
+ "AddResultObjects"
+ "AddViews"
+ "Allow Head Gesture Injection"
+ "Announce On Headphones Cached Eligibility"
+ "AppPunchOut"
+ "CSFGMOptIn"
+ "ExecuteCallbacks"
+ "HomePodNoTTSPerfTestEnabled"
+ "RequestCompleted"
+ "T@\"NSArray\",C,N,V_messages"
+ "T@\"NSArray\",C,N,V_messagesContext"
+ "T@\"NSString\",C,N,V_recognizedText"
+ "T@\"NSString\",C,N,V_sender"
+ "TB,N,V_shouldAppendAutoAnswerTip"
+ "TB,R,N,V_isDeviceOwner"
+ "TB,V_deviceSupportsSAE"
+ "TB,V_saeAvailable"
+ "TB,V_swaiEnabled"
+ "TB,V_visualIntelligenceEnabled"
+ "UST"
+ "Visual Intelligence Camera Control Enabled"
+ "Vv24@0:8@?<v@?@\"AFSharedUserInfo\">16"
+ "Vv32@0:8@\"AFSpeechVisualContextAndCorrectionsInfo\"16@\"NSString\"24"
+ "Vv32@0:8Q16@\"NSURL\"24"
+ "Vv32@0:8Q16@24"
+ "Vv36@0:8q16B24@?28"
+ "Vv36@0:8q16B24@?<v@?B@\"NSString\">28"
+ "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\">40"
+ "_AFPreferencesReplacementLanguageForLocalRecognizerLanguageCode"
+ "_AFPreferencesSetVisualIntelligenceCameraControlEnabled"
+ "_deviceSupportsSAE"
+ "_fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:"
+ "_internalGestureTestingHandler"
+ "_isDeviceOwner"
+ "_messages"
+ "_messagesContext"
+ "_recognizedText"
+ "_saeAvailable"
+ "_scheduledHeadGesture"
+ "_sender"
+ "_shouldAppendAutoAnswerTip"
+ "_swaiEnabled"
+ "_updateForReason:"
+ "_visualIntelligenceEnabled"
+ "allowHeadGestureInjection"
+ "asr_speech_profile_app_entities"
+ "asr_speech_profile_onscreen_entities"
+ "assistantConnection:replayAll:with:"
+ "assistantConnection:replayAt:with:"
+ "assistantConnection:setReplayEnabled:"
+ "assistantConnection:setReplayOverridePath:"
+ "checkGMAvailabilityWithUseCaseIdentifiers"
+ "com.apple.Settings.AppleIntelligence"
+ "com.apple.siri.orchestration.capabilities"
+ "com.apple.siri.orchestration.capabilities.didChange"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "currentWithUseCaseIdentifiers:language:"
+ "deviceSupportsSAE"
+ "dictation_voice_commands"
+ "disable_remote_network_session"
+ "en-JP"
+ "fetchEligibleAnnouncementRequestTypesAndNotifyObserversAndShouldRelyOnCachedStateIfIneligble:"
+ "fileExistsAndNotEmpty:samplingComponent:"
+ "getIsDeviceOwner"
+ "getLoggableIdentiferForUserWithiCloudAltDSID:sharedUserID:sessionID:completion:"
+ "getPrimaryUserSharedUserInfoWithCompletion:"
+ "group.com.apple.assistant.shared"
+ "initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:"
+ "isASRSpeechProfileAppEntitiesEnabled"
+ "isASRSpeechProfileOnscreenEntitiesEnabled"
+ "isDeviceOwner"
+ "isHomePodNoTTSPerfTestEnabled"
+ "isOfflineDictationLanguageMappingEnabled"
+ "isOptedIn"
+ "isPersistentSiriEnabled"
+ "isRemoteSessionDisabled"
+ "isSAEi18nEnabled"
+ "isVisualIntelligenceEnabled"
+ "kAFAssistantFilesystemDomain"
+ "localizedDescription"
+ "messages"
+ "messagesContext"
+ "mockHeadGesture:schedule:withCompletion:"
+ "offline_dictation_language_mapping_enabled"
+ "path"
+ "persistent_siri"
+ "recognizedText"
+ "registerInternalGestureTestingHandler:"
+ "replayAllRecordedViews:with:"
+ "replayRecordedViewAt:with:"
+ "requestReplayAllRecordedViews:with:"
+ "requestReplayRecordedViewAt:with:"
+ "requestSetReplayEnabled:"
+ "requestSetReplayOverridePath:"
+ "saeAvailable"
+ "sae_enabled_i18n"
+ "sendVisualContextAndCorrectionsInfo:interactionIdentifier:"
+ "sender"
+ "setAllowHeadGestureInjection:"
+ "setDeviceSupportsSAE:"
+ "setIsDeviceOwner:"
+ "setMessages:"
+ "setMessagesContext:"
+ "setRecognizedText:"
+ "setReplayEnabled:"
+ "setReplayOverridePath:"
+ "setSaeAvailable:"
+ "setSender:"
+ "setShouldAppendAutoAnswerTip:"
+ "setSwaiEnabled:"
+ "setVisualIntelligenceCameraControlEnabled:"
+ "setVisualIntelligenceEnabled:"
+ "sharedApplicationGroupURL:"
+ "sharedApplicationGroupURLOnQueue:WithCompletion:"
+ "shouldAppendAutoAnswerTip"
+ "shouldDownloadAssetsForSiriSystemAssistantExperience:"
+ "shouldDownloadAssetsForSiriSystemAssistantExperienceSync"
+ "siriSystemAssistantExperienceEnabled:"
+ "siriSystemAssistantExperienceEnabledSync"
+ "siriWithAppIntentsEnabled:"
+ "siriWithAppIntentsEnabledSync"
+ "swaiEnabled"
+ "syncServiceWithErrorHandler:"
+ "triggerVoiceProfileUploadWithCompletion:completion:"
+ "useDeprecatedSAECheck"
+ "ust_deviceSupportsSAE"
+ "ust_saeEnabled"
+ "ust_swaiEnabled"
+ "v36@0:8q16B24@?28"
+ "vi-VI"
+ "vi-VN-u-sd-vnct"
+ "visualIntelligenceCameraControlEnabled"
+ "visualIntelligenceEnabled"
+ "{_mutationFlags=\"isDirty\"b1\"hasSharedUserId\"b1\"hasLoggableSharedUserId\"b1\"hasCompanionDeviceInfo\"b1\"hasPersonalRequestsEnabled\"b1\"hasCompanionLinkReady\"b1\"hasHomeUserId\"b1\"hasICloudAltDSID\"b1\"hasIsDeviceOwner\"b1}"
- "%@ {sharedUserId = %@, loggableSharedUserId = %@, companionDeviceInfo = %@, personalRequestsEnabled = %@, companionLinkReady = %@, homeUserId = %@, iCloudAltDSID = %@}"
- "%s #Montara #FamilyCircle received account change event account=%@ type=%d"
- "%s #Montara #FamilyCircle setup ACXPCEventSubscriber"
- "%s #Montara #FamilyCircle setup ACXPCEventSubscriber completed"
- "%s #SAEStatus from cache:%d"
- "%s #SAEStatus:%d"
- "%s previous announcement request eligibility: %lu, now updating to %lu"
- "-[AFFamilyCircleStatusManager _observeAccountChanges]_block_invoke"
- "-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObservers]"
- "-[AFHeadphonesAnnouncementRequestCapabilityProvider _fetchEligibleAnnouncementRequestTypesAndNotifyObservers]_block_invoke_2"
- "-[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:]"
- "-[AFMultiUserConnection triggerVoiceProfileUploadWithCompletion:]_block_invoke"
- "@64@0:8@16@24@32B40B44@48@56"
- "ACXPCEventSubscriber"
- "AFAWDSiriLinkRecommendationInfo"
- "AFDeviceSupportsSAE"
- "TB,N,V_btPreference"
- "TB,N,V_wifiPreference"
- "TQ,N,V_btRSSI"
- "Td,N,V_timeTaken"
- "Tq,N,V_beaconPER"
- "Tq,N,V_btRetransmissionRateRx"
- "Tq,N,V_btRetransmissionRateTx"
- "Tq,N,V_btTech"
- "Tq,N,V_expectedThroughputVIBE"
- "Tq,N,V_lsmRecommendationBe"
- "Tq,N,V_nwType"
- "Tq,N,V_packetLifetimeVIBE"
- "Tq,N,V_packetLossRateVIBE"
- "Tq,N,V_wifiCCA"
- "Tq,N,V_wifiRSSI"
- "Tq,N,V_wifiSNR"
- "_beaconPER"
- "_btPreference"
- "_btRSSI"
- "_btRetransmissionRateRx"
- "_btRetransmissionRateTx"
- "_btTech"
- "_expectedThroughputVIBE"
- "_fetchEligibleAnnouncementRequestTypesAndNotifyObservers"
- "_lsmRecommendationBe"
- "_nwType"
- "_packetLifetimeVIBE"
- "_packetLossRateVIBE"
- "_timeTaken"
- "_wifiCCA"
- "_wifiPreference"
- "_wifiRSSI"
- "_wifiSNR"
- "beaconPER"
- "btPreference"
- "btRSSI"
- "btRetransmissionRateRx"
- "btRetransmissionRateTx"
- "btTech"
- "classACXPCEventSubscriber"
- "expectedThroughputVIBE"
- "initACXPCEventSubscriber_block_invoke"
- "initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:"
- "lsmRecommendationBe"
- "nwType"
- "packetLifetimeVIBE"
- "packetLossRateVIBE"
- "recordAWDSuccessMetrics"
- "registerAccountChangeEventHandler:"
- "setBeaconPER:"
- "setBtPreference:"
- "setBtRSSI:"
- "setBtRetransmissionRateRx:"
- "setBtRetransmissionRateTx:"
- "setBtTech:"
- "setExpectedThroughputVIBE:"
- "setLsmRecommendationBe:"
- "setNwType:"
- "setPacketLifetimeVIBE:"
- "setPacketLossRateVIBE:"
- "setTimeTaken:"
- "setWifiCCA:"
- "setWifiPreference:"
- "setWifiRSSI:"
- "setWifiSNR:"
- "sharedSubscriber"
- "timeTaken"
- "triggerVoiceProfileUploadWithCompletion:"
- "v20@?0@\"ACAccount\"8i16"
- "wifiCCA"
- "wifiPreference"
- "wifiRSSI"
- "wifiSNR"
- "{_mutationFlags=\"isDirty\"b1\"hasSharedUserId\"b1\"hasLoggableSharedUserId\"b1\"hasCompanionDeviceInfo\"b1\"hasPersonalRequestsEnabled\"b1\"hasCompanionLinkReady\"b1\"hasHomeUserId\"b1\"hasICloudAltDSID\"b1}"

```
