## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3405.29.4.11.2
-  __TEXT.__text: 0x1ac9cc
-  __TEXT.__auth_stubs: 0x1550
-  __TEXT.__objc_methlist: 0x1dca4
-  __TEXT.__const: 0x458
+3500.97.4.1.2
+  __TEXT.__text: 0x1ae45c
+  __TEXT.__auth_stubs: 0x1560
+  __TEXT.__objc_methlist: 0x1dbd4
+  __TEXT.__const: 0x468
   __TEXT.__dlopen_cstrs: 0x484
-  __TEXT.__gcc_except_tab: 0x2adc
-  __TEXT.__cstring: 0x3d4c0
-  __TEXT.__oslogstring: 0x10f3b
+  __TEXT.__gcc_except_tab: 0x2aec
+  __TEXT.__cstring: 0x3d8eb
+  __TEXT.__oslogstring: 0x115dc
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0x7d40
-  __TEXT.__objc_classname: 0x4f0c
-  __TEXT.__objc_methname: 0x3b3e7
-  __TEXT.__objc_methtype: 0xab16
-  __TEXT.__objc_stubs: 0x248c0
-  __DATA_CONST.__got: 0x1648
-  __DATA_CONST.__const: 0x8448
-  __DATA_CONST.__objc_classlist: 0xdd8
+  __TEXT.__unwind_info: 0x7dc0
+  __TEXT.__objc_classname: 0x4f56
+  __TEXT.__objc_methname: 0x3b0f7
+  __TEXT.__objc_methtype: 0xaadf
+  __TEXT.__objc_stubs: 0x245a0
+  __DATA_CONST.__got: 0x1640
+  __DATA_CONST.__const: 0x83b0
+  __DATA_CONST.__objc_classlist: 0xde8
   __DATA_CONST.__objc_catlist: 0x290
-  __DATA_CONST.__objc_protolist: 0x558
+  __DATA_CONST.__objc_protolist: 0x560
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc388
+  __DATA_CONST.__objc_selrefs: 0xc2f8
   __DATA_CONST.__objc_protorefs: 0x148
-  __DATA_CONST.__objc_superrefs: 0xdf0
-  __DATA_CONST.__objc_arraydata: 0x2090
-  __AUTH_CONST.__auth_got: 0xab8
-  __AUTH_CONST.__const: 0x3a80
-  __AUTH_CONST.__cfstring: 0x27180
-  __AUTH_CONST.__objc_const: 0x33750
-  __AUTH_CONST.__objc_intobj: 0x2328
-  __AUTH_CONST.__objc_dictobj: 0xb90
-  __AUTH_CONST.__objc_arrayobj: 0x5d0
+  __DATA_CONST.__objc_superrefs: 0xe00
+  __DATA_CONST.__objc_arraydata: 0x2098
+  __AUTH_CONST.__auth_got: 0xac0
+  __AUTH_CONST.__const: 0x3ac0
+  __AUTH_CONST.__cfstring: 0x27120
+  __AUTH_CONST.__objc_const: 0x336a8
+  __AUTH_CONST.__objc_intobj: 0x2310
+  __AUTH_CONST.__objc_dictobj: 0xbb8
+  __AUTH_CONST.__objc_arrayobj: 0x5b8
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH.__objc_data: 0x7918
-  __AUTH.__data: 0x2b0
-  __DATA.__objc_ivar: 0x2574
-  __DATA.__data: 0x4178
-  __DATA.__bss: 0x1338
+  __AUTH.__objc_data: 0x7b98
+  __AUTH.__data: 0x288
+  __DATA.__objc_ivar: 0x253c
+  __DATA.__data: 0x41c8
+  __DATA.__bss: 0x1300
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x1158
-  __DATA_DIRTY.__common: 0xf8
-  __DATA_DIRTY.__bss: 0x188
+  __DATA_DIRTY.__objc_data: 0xf78
+  __DATA_DIRTY.__data: 0x18
+  __DATA_DIRTY.__common: 0xf0
+  __DATA_DIRTY.__bss: 0x1f0
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/FaceTimeNameUtility.framework/FaceTimeNameUtility
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
   - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 776626C6-4A7D-36EE-B96B-D98E970688BE
-  Functions: 11773
-  Symbols:   37508
-  CStrings:  24186
+  UUID: 4BC0DFFB-EE04-3887-AEF0-9BF0856ECC91
+  Functions: 11777
+  Symbols:   37494
+  CStrings:  24215
 
Symbols:
+ +[AFFeatureFlags(SWEFeatureFlags) isDiagnosticsBridgeFeatureEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isSAEi18nWave2Enabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isSiriMUSessionsGuestSessionUpgradeEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isUIUtteranceJSStringCatalogEnabled]
+ +[AFLocalization effectiveGenderKeyForKey:gender:]
+ +[AFSamplingUtilities deleteItemAtFilePath:error:]
+ +[AFSiriAnnounceWorkoutVoiceFeedbackRequest deactivateRequestForFeedbackIdentifier:completion:]
+ +[AFSiriAudioRouteMonitor sharedMonitor]
+ +[AFSiriWorkoutVoiceFeedback supportsSecureCoding]
+ -[AFCheckSRT .cxx_destruct]
+ -[AFCheckSRT dealloc]
+ -[AFCheckSRT didReceivePluginSelected:]
+ -[AFCheckSRT init]
+ -[AFCheckSRT trackEvent:forTurn:]
+ -[AFClientConfiguration carOwnsMainAudio]
+ -[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:carOwnsMainAudio:]
+ -[AFCompanionDeviceInfo companionName]
+ -[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:]
+ -[AFConnection setCarOwnsMainAudio:]
+ -[AFConnectionClientServiceDelegate endWaitingForEmergency]
+ -[AFDictationOptions messagesContext]
+ -[AFDictationOptions setMessagesContext:]
+ -[AFDictationOptions setShouldPerformFullPayloadCorrection:]
+ -[AFDictationOptions shouldPerformFullPayloadCorrection]
+ -[AFLocalization(StringCatalog) localizedStringFromCatalogForKey:gender:table:bundle:languageCode:defaultValue:]
+ -[AFLocalization(StringCatalog) localizedStringOrNilFromCatalogForKey:gender:table:bundle:languageCode:defaultValue:]
+ -[AFModesConfiguration initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isUserEngagedWithDevice:]
+ -[AFPreferences isSyncNeededForAtv]
+ -[AFPreferences isSyncNeededForWatch]
+ -[AFRequestInfo setSuggestionRequestType:]
+ -[AFRequestInfo suggestionRequestType]
+ -[AFSettingsConnection getODDDeviceAggregationId:]
+ -[AFSettingsConnection sendSampledAudioToServerIgnoringMinimumSampleAge:completion:]
+ -[AFSharedUserInfo initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:isMediaFallbackUser:]
+ -[AFSharedUserInfo isMediaFallbackUser]
+ -[AFSiriAnnounceWorkoutVoiceFeedbackRequest initWithWorkoutVoiceFeedback:]
+ -[AFSiriAudioRoute _descriptionWithIndent:]
+ -[AFSiriAudioRoute _isAppleHeadphone]
+ -[AFSiriAudioRoute description]
+ -[AFSiriAudioRoute setUid:]
+ -[AFSiriAudioRoute uid]
+ -[AFSiriAudioRouteMonitor .cxx_destruct]
+ -[AFSiriAudioRouteMonitor _broadcastRouteChangeFrom:to:]
+ -[AFSiriAudioRouteMonitor _fetchInitialState]
+ -[AFSiriAudioRouteMonitor _init]
+ -[AFSiriAudioRouteMonitor _updateAudioRouteAvailabilityAndBroadcast:]
+ -[AFSiriAudioRouteMonitor addDelegate:]
+ -[AFSiriAudioRouteMonitor currentAudioRoute]
+ -[AFSiriAudioRouteMonitor deviceRingerObserver:didChangeState:]
+ -[AFSiriAudioRouteMonitor initializeAVSystemControllerSubscriptions:]
+ -[AFSiriAudioRouteMonitor removeDelegate:]
+ -[AFSiriAudioRouteMonitor setCurrentAudioRoute:]
+ -[AFSiriAudioRouteMonitor updateAudioRouteAvailability:]
+ -[AFSiriHeadphonesMonitor _audioRouteMonitor]
+ -[AFSiriHeadphonesMonitor _updateAudioRouteFromRoute:toRoute:andBroadcast:]
+ -[AFSiriHeadphonesMonitor currentAudioRouteDidChangeFrom:to:]
+ -[AFSiriHeadphonesMonitor discoveryNotificationAssertion]
+ -[AFSiriHeadphonesMonitor invalidateDiscoveryNotificationAssertion:]
+ -[AFSiriWorkoutVoiceFeedback .cxx_destruct]
+ -[AFSiriWorkoutVoiceFeedback copyWithZone:]
+ -[AFSiriWorkoutVoiceFeedback encodeWithCoder:]
+ -[AFSiriWorkoutVoiceFeedback feedbackAudioASBD]
+ -[AFSiriWorkoutVoiceFeedback feedbackAudioData]
+ -[AFSiriWorkoutVoiceFeedback feedbackIdentifier]
+ -[AFSiriWorkoutVoiceFeedback feedbackText]
+ -[AFSiriWorkoutVoiceFeedback initWithCoder:]
+ -[AFSiriWorkoutVoiceFeedback initWithVoiceFeedbackAudioData:asbd:]
+ -[AFSiriWorkoutVoiceFeedback initWithVoiceFeedbackIdentifier:audioData:asbd:]
+ -[AFSiriWorkoutVoiceFeedback initWithVoiceFeedbackIdentifier:text:]
+ -[AFSiriWorkoutVoiceFeedback initWithVoiceFeedbackText:]
+ -[AFSpeechRequestOptions computedActivationEventMachAbsoluteTime]
+ -[_AFClientConfigurationMutation getCarOwnsMainAudio]
+ -[_AFClientConfigurationMutation setCarOwnsMainAudio:]
+ -[_AFCompanionDeviceInfoMutation getCompanionName]
+ -[_AFCompanionDeviceInfoMutation setCompanionName:]
+ -[_AFSharedUserInfoMutation getIsMediaFallbackUser]
+ -[_AFSharedUserInfoMutation setIsMediaFallbackUser:]
+ GCC_except_table10098
+ GCC_except_table10103
+ GCC_except_table10112
+ GCC_except_table10138
+ GCC_except_table10159
+ GCC_except_table1017
+ GCC_except_table1083
+ GCC_except_table10878
+ GCC_except_table1089
+ GCC_except_table10891
+ GCC_except_table11079
+ GCC_except_table11218
+ GCC_except_table11231
+ GCC_except_table11269
+ GCC_except_table11527
+ GCC_except_table11670
+ GCC_except_table11689
+ GCC_except_table11692
+ GCC_except_table11694
+ GCC_except_table1230
+ GCC_except_table1232
+ GCC_except_table1419
+ GCC_except_table1456
+ GCC_except_table1466
+ GCC_except_table1487
+ GCC_except_table1569
+ GCC_except_table1575
+ GCC_except_table1578
+ GCC_except_table1643
+ GCC_except_table1712
+ GCC_except_table1738
+ GCC_except_table1980
+ GCC_except_table2024
+ GCC_except_table2192
+ GCC_except_table2245
+ GCC_except_table2253
+ GCC_except_table2311
+ GCC_except_table233
+ GCC_except_table251
+ GCC_except_table255
+ GCC_except_table2692
+ GCC_except_table2699
+ GCC_except_table2705
+ GCC_except_table2750
+ GCC_except_table2752
+ GCC_except_table2758
+ GCC_except_table2764
+ GCC_except_table2768
+ GCC_except_table2775
+ GCC_except_table2777
+ GCC_except_table2782
+ GCC_except_table2784
+ GCC_except_table2788
+ GCC_except_table2803
+ GCC_except_table2825
+ GCC_except_table2827
+ GCC_except_table2829
+ GCC_except_table2831
+ GCC_except_table2833
+ GCC_except_table2835
+ GCC_except_table2878
+ GCC_except_table2903
+ GCC_except_table2958
+ GCC_except_table2988
+ GCC_except_table3284
+ GCC_except_table3342
+ GCC_except_table3465
+ GCC_except_table3478
+ GCC_except_table3479
+ GCC_except_table3491
+ GCC_except_table3498
+ GCC_except_table3499
+ GCC_except_table3508
+ GCC_except_table3596
+ GCC_except_table3598
+ GCC_except_table3621
+ GCC_except_table3663
+ GCC_except_table3675
+ GCC_except_table3745
+ GCC_except_table3852
+ GCC_except_table3859
+ GCC_except_table3873
+ GCC_except_table3910
+ GCC_except_table3996
+ GCC_except_table4050
+ GCC_except_table4463
+ GCC_except_table4466
+ GCC_except_table4467
+ GCC_except_table449
+ GCC_except_table4756
+ GCC_except_table4822
+ GCC_except_table4885
+ GCC_except_table4895
+ GCC_except_table4906
+ GCC_except_table4919
+ GCC_except_table497
+ GCC_except_table5044
+ GCC_except_table516
+ GCC_except_table5398
+ GCC_except_table5401
+ GCC_except_table5468
+ GCC_except_table5469
+ GCC_except_table5482
+ GCC_except_table5483
+ GCC_except_table5490
+ GCC_except_table5528
+ GCC_except_table5534
+ GCC_except_table5540
+ GCC_except_table5612
+ GCC_except_table5649
+ GCC_except_table5652
+ GCC_except_table5786
+ GCC_except_table5885
+ GCC_except_table5906
+ GCC_except_table5908
+ GCC_except_table5972
+ GCC_except_table5974
+ GCC_except_table5976
+ GCC_except_table5978
+ GCC_except_table5992
+ GCC_except_table5998
+ GCC_except_table6121
+ GCC_except_table6128
+ GCC_except_table6483
+ GCC_except_table6498
+ GCC_except_table6521
+ GCC_except_table6624
+ GCC_except_table6633
+ GCC_except_table6672
+ GCC_except_table6704
+ GCC_except_table6771
+ GCC_except_table702
+ GCC_except_table709
+ GCC_except_table7239
+ GCC_except_table7244
+ GCC_except_table7247
+ GCC_except_table7250
+ GCC_except_table7253
+ GCC_except_table7256
+ GCC_except_table7463
+ GCC_except_table7466
+ GCC_except_table7468
+ GCC_except_table7480
+ GCC_except_table7552
+ GCC_except_table7558
+ GCC_except_table7728
+ GCC_except_table7834
+ GCC_except_table7864
+ GCC_except_table8053
+ GCC_except_table8058
+ GCC_except_table8122
+ GCC_except_table8228
+ GCC_except_table828
+ GCC_except_table8655
+ GCC_except_table8709
+ GCC_except_table8753
+ GCC_except_table8841
+ GCC_except_table8881
+ GCC_except_table8912
+ GCC_except_table8917
+ GCC_except_table8922
+ GCC_except_table9168
+ GCC_except_table9238
+ GCC_except_table9244
+ GCC_except_table9279
+ GCC_except_table9282
+ GCC_except_table9360
+ GCC_except_table9389
+ GCC_except_table9461
+ GCC_except_table9464
+ GCC_except_table9468
+ GCC_except_table9573
+ GCC_except_table9577
+ GCC_except_table9581
+ GCC_except_table9614
+ GCC_except_table9659
+ _AFDeviceSupportsCrossSession
+ _AFDeviceSupportsMUSessionsGuestSessionUpgrade
+ _AFExternalRequestMessageKeyWorkoutVoiceFeedbackIdentifier
+ _AFInternalConfigValueForKey.internalConfig
+ _AFInternalConfigValueForKey.onceToken
+ _AFIsLocaleSupportedForSiriClassic.once
+ _AFIsLocaleSupportedForSiriClassic.supportedSiriClassicLocales
+ _AFLocaleIdentifierSupportsSAE.supportedGlobalLocalesWave2
+ _AFPreferencesOnDeviceLocaleForDictationLocale
+ _AFPreferencesOnDeviceLocaleForDictationLocale.onDeviceLocaleForDictationLocale
+ _AFPreferencesOnDeviceLocaleForDictationLocale.onceToken
+ _AFPreferencesOnDeviceLocaleForSpellingLocale
+ _AFPreferencesOnDeviceLocaleForSpellingLocale.onDeviceLocaleForSpellingLocale
+ _AFPreferencesOnDeviceLocaleForSpellingLocale.onceToken
+ _AFSiriAudioRouteMonitorGetCurrentlySelectedAudioRoute
+ _AFSpeechEventIsSmartRoutingEligible
+ _AFSuggestionRequestTypeGetName
+ _AnnounceLibrary.sLib.43626
+ _AnnounceLibrary.sOnce.43624
+ _BiomeLibraryLibraryCore.45763
+ _BiomeLibraryLibraryCore.frameworkLibrary.27073
+ _BiomeLibraryLibraryCore.frameworkLibrary.45766
+ _BluetoothManagerLibrary.45860
+ _BluetoothManagerLibraryCore.frameworkLibrary.20379
+ _CoreServicesLibrary.frameworkLibrary.46509
+ _CoreSpeechLibrary.frameworkLibrary.39265
+ _DataCollectionServicesLibrary.sLib.46521
+ _DataCollectionServicesLibrary.sOnce.46520
+ _IntentsLibrary.15188
+ _IntentsLibraryCore.frameworkLibrary.15191
+ _IntentsLibraryCore.frameworkLibrary.31145
+ _LSApplicationProxyFunction.34607
+ _LSApplicationProxyFunction.46515
+ _MediaExperienceLibrary.27523
+ _MediaExperienceLibraryCore.frameworkLibrary.27549
+ _OBJC_CLASS_$_AFCheckSRT
+ _OBJC_CLASS_$_AFSiriAudioRouteMonitor
+ _OBJC_CLASS_$_AFSiriWorkoutVoiceFeedback
+ _OBJC_CLASS_$_FTNUServiceNames
+ _OBJC_IVAR_$_AFCheckSRT._currentTurnID
+ _OBJC_IVAR_$_AFCheckSRT._pluginSelected
+ _OBJC_IVAR_$_AFCheckSRT._stateLock
+ _OBJC_IVAR_$_AFClientConfiguration._carOwnsMainAudio
+ _OBJC_IVAR_$_AFCompanionDeviceInfo._companionName
+ _OBJC_IVAR_$_AFConnection._checkSRT
+ _OBJC_IVAR_$_AFDictationOptions._messagesContext
+ _OBJC_IVAR_$_AFDictationOptions._shouldPerformFullPayloadCorrection
+ _OBJC_IVAR_$_AFRequestInfo._suggestionRequestType
+ _OBJC_IVAR_$_AFSharedUserInfo._isMediaFallbackUser
+ _OBJC_IVAR_$_AFSiriAnnounceWorkoutVoiceFeedbackRequest._workoutVoiceFeedback
+ _OBJC_IVAR_$_AFSiriAudioRoute._uid
+ _OBJC_IVAR_$_AFSiriAudioRouteMonitor._btAddress
+ _OBJC_IVAR_$_AFSiriAudioRouteMonitor._currentAudioRoute
+ _OBJC_IVAR_$_AFSiriAudioRouteMonitor._delegates
+ _OBJC_IVAR_$_AFSiriAudioRouteMonitor._queue
+ _OBJC_IVAR_$_AFSiriAudioRouteMonitor._ringerSwitchObserver
+ _OBJC_IVAR_$_AFSiriAudioRouteMonitor._routeName
+ _OBJC_IVAR_$_AFSiriHeadphonesMonitor._notificationPostAssertions
+ _OBJC_IVAR_$_AFSiriWorkoutVoiceFeedback._feedbackAudioASBD
+ _OBJC_IVAR_$_AFSiriWorkoutVoiceFeedback._feedbackAudioData
+ _OBJC_IVAR_$_AFSiriWorkoutVoiceFeedback._feedbackIdentifier
+ _OBJC_IVAR_$_AFSiriWorkoutVoiceFeedback._feedbackText
+ _OBJC_IVAR_$__AFClientConfigurationMutation._carOwnsMainAudio
+ _OBJC_IVAR_$__AFCompanionDeviceInfoMutation._companionName
+ _OBJC_IVAR_$__AFSharedUserInfoMutation._isMediaFallbackUser
+ _OBJC_METACLASS_$_AFCheckSRT
+ _OBJC_METACLASS_$_AFSiriAudioRouteMonitor
+ _OBJC_METACLASS_$_AFSiriWorkoutVoiceFeedback
+ _STCallServiceGetDescription.facetimeServiceNames
+ _STCallServiceGetDescription.onceToken
+ _SoftBiomeLibrary.45749
+ _VTPreferencesFunction.46725
+ _VoiceTriggerLibrary.frameworkLibrary.46719
+ __FlowPluginSelected
+ __OBJC_$_CLASS_METHODS_AFSiriAudioRouteMonitor
+ __OBJC_$_CLASS_METHODS_AFSiriWorkoutVoiceFeedback
+ __OBJC_$_CLASS_PROP_LIST_AFSiriWorkoutVoiceFeedback
+ __OBJC_$_INSTANCE_METHODS_AFCheckSRT
+ __OBJC_$_INSTANCE_METHODS_AFLocalization(StringCatalog)
+ __OBJC_$_INSTANCE_METHODS_AFSiriAudioRouteMonitor
+ __OBJC_$_INSTANCE_METHODS_AFSiriWorkoutVoiceFeedback
+ __OBJC_$_INSTANCE_VARIABLES_AFCheckSRT
+ __OBJC_$_INSTANCE_VARIABLES_AFSiriAudioRouteMonitor
+ __OBJC_$_INSTANCE_VARIABLES_AFSiriWorkoutVoiceFeedback
+ __OBJC_$_PROP_LIST_AFSiriAudioRouteMonitor
+ __OBJC_$_PROP_LIST_AFSiriWorkoutVoiceFeedback
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFSiriAudioRouteMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AFSiriAudioRouteMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_AFSiriAudioRouteMonitorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_AFSiriAudioRouteMonitor
+ __OBJC_CLASS_PROTOCOLS_$_AFSiriWorkoutVoiceFeedback
+ __OBJC_CLASS_RO_$_AFCheckSRT
+ __OBJC_CLASS_RO_$_AFSiriAudioRouteMonitor
+ __OBJC_CLASS_RO_$_AFSiriWorkoutVoiceFeedback
+ __OBJC_LABEL_PROTOCOL_$_AFSiriAudioRouteMonitorDelegate
+ __OBJC_METACLASS_RO_$_AFCheckSRT
+ __OBJC_METACLASS_RO_$_AFSiriAudioRouteMonitor
+ __OBJC_METACLASS_RO_$_AFSiriWorkoutVoiceFeedback
+ __OBJC_PROTOCOL_$_AFSiriAudioRouteMonitorDelegate
+ ___184-[AFSharedUserInfo initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:isMediaFallbackUser:]_block_invoke
+ ___211-[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:]_block_invoke
+ ___27-[AFConnection _connection]_block_invoke.230
+ ___27-[AFConnection _connection]_block_invoke_2.231
+ ___32-[AFSiriAudioRouteMonitor _init]_block_invoke
+ ___346-[AFModesConfiguration initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isUserEngagedWithDevice:]_block_invoke
+ ___36-[AFConnection setCarOwnsMainAudio:]_block_invoke
+ ___365-[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:carOwnsMainAudio:]_block_invoke
+ ___38-[AFConnection _startRequestWithInfo:]_block_invoke.322
+ ___38-[AFConnection _startRequestWithInfo:]_block_invoke.327
+ ___38-[AFConnection _startRequestWithInfo:]_block_invoke_2.323
+ ___39-[AFSiriAudioRouteMonitor addDelegate:]_block_invoke
+ ___40+[AFSiriAudioRouteMonitor sharedMonitor]_block_invoke
+ ___42-[AFSiriAudioRouteMonitor removeDelegate:]_block_invoke
+ ___44-[AFSiriAudioRouteMonitor currentAudioRoute]_block_invoke
+ ___45-[AFSiriAudioRouteMonitor _fetchInitialState]_block_invoke
+ ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke.345
+ ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke_2.346
+ ___50-[AFSettingsConnection getODDDeviceAggregationId:]_block_invoke
+ ___56-[AFSiriAudioRouteMonitor _broadcastRouteChangeFrom:to:]_block_invoke
+ ___56-[AFSiriAudioRouteMonitor updateAudioRouteAvailability:]_block_invoke
+ ___57-[AFSiriHeadphonesMonitor discoveryNotificationAssertion]_block_invoke
+ ___58-[AFConnection acquireAudioSessionWithContext:completion:]_block_invoke.308
+ ___59-[AFSiriHeadphonesMonitor _settingsConnectionDidDisconnect]_block_invoke.23
+ ___60-[AFMyriadEmergencyCallPunchout initiateEmergencyCallMyriad]_block_invoke.24
+ ___60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.562
+ ___61-[AFSiriHeadphonesMonitor currentAudioRouteDidChangeFrom:to:]_block_invoke
+ ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.295
+ ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.302
+ ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke_2.306
+ ___63-[AFSiriAudioRouteMonitor deviceRingerObserver:didChangeState:]_block_invoke
+ ___64-[AFConnectionClientServiceDelegate requestHandleCommand:reply:]_block_invoke.751
+ ___64-[AFSiriHeadphonesMonitor notifyObserver:didChangeStateFrom:to:]_block_invoke.26
+ ___66-[AFSiriHeadphonesMonitor fetchPrivateSessionStateWithCompletion:]_block_invoke.34
+ ___68-[AFSiriHeadphonesMonitor invalidateDiscoveryNotificationAssertion:]_block_invoke
+ ___69-[AFSiriAudioRouteMonitor initializeAVSystemControllerSubscriptions:]_block_invoke
+ ___75-[AFSiriHeadphonesMonitor _updateAudioRouteFromRoute:toRoute:andBroadcast:]_block_invoke
+ ___75-[AFSiriHeadphonesMonitor _updateAudioRouteFromRoute:toRoute:andBroadcast:]_block_invoke.13
+ ___75-[AFSiriHeadphonesMonitor _updateAudioRouteFromRoute:toRoute:andBroadcast:]_block_invoke_2
+ ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke.343
+ ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke_2.344
+ ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.340
+ ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.342
+ ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke_2.341
+ ___84-[AFSettingsConnection sendSampledAudioToServerIgnoringMinimumSampleAge:completion:]_block_invoke
+ ___85-[AFSiriHeadphonesMonitor _postJSDiscoveryNotificationForBTDeviceWithInfo:scheduled:]_block_invoke.45
+ ___90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.118
+ ___90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.121
+ ___95+[AFSiriAnnounceWorkoutVoiceFeedbackRequest deactivateRequestForFeedbackIdentifier:completion:]_block_invoke
+ ___AFInternalConfigValueForKey_block_invoke
+ ___AFIsLocaleSupportedForSiriClassic_block_invoke
+ ___AFPreferencesOnDeviceLocaleForDictationLocale_block_invoke
+ ___AFPreferencesOnDeviceLocaleForSpellingLocale_block_invoke
+ ___AnnounceLibrary_block_invoke.43630
+ ___BiomeLibraryLibraryCore_block_invoke.27074
+ ___BiomeLibraryLibraryCore_block_invoke.45767
+ ___Block_byref_object_copy_.10639
+ ___Block_byref_object_copy_.10832
+ ___Block_byref_object_copy_.11464
+ ___Block_byref_object_copy_.12046
+ ___Block_byref_object_copy_.13296
+ ___Block_byref_object_copy_.13568
+ ___Block_byref_object_copy_.16560
+ ___Block_byref_object_copy_.17089
+ ___Block_byref_object_copy_.17581
+ ___Block_byref_object_copy_.19623
+ ___Block_byref_object_copy_.19864
+ ___Block_byref_object_copy_.20395
+ ___Block_byref_object_copy_.21467
+ ___Block_byref_object_copy_.22412
+ ___Block_byref_object_copy_.23084
+ ___Block_byref_object_copy_.23502
+ ___Block_byref_object_copy_.24100
+ ___Block_byref_object_copy_.26212
+ ___Block_byref_object_copy_.29058
+ ___Block_byref_object_copy_.30730
+ ___Block_byref_object_copy_.35034
+ ___Block_byref_object_copy_.35478
+ ___Block_byref_object_copy_.37703
+ ___Block_byref_object_copy_.38884
+ ___Block_byref_object_copy_.42006
+ ___Block_byref_object_copy_.46657
+ ___Block_byref_object_copy_.47916
+ ___Block_byref_object_copy_.48641
+ ___Block_byref_object_copy_.48923
+ ___Block_byref_object_copy_.5357
+ ___Block_byref_object_copy_.5763
+ ___Block_byref_object_copy_.7899
+ ___Block_byref_object_copy_.8703
+ ___Block_byref_object_copy_.9934
+ ___Block_byref_object_dispose_.10640
+ ___Block_byref_object_dispose_.10833
+ ___Block_byref_object_dispose_.11465
+ ___Block_byref_object_dispose_.12047
+ ___Block_byref_object_dispose_.13297
+ ___Block_byref_object_dispose_.13569
+ ___Block_byref_object_dispose_.16561
+ ___Block_byref_object_dispose_.17090
+ ___Block_byref_object_dispose_.17582
+ ___Block_byref_object_dispose_.19624
+ ___Block_byref_object_dispose_.19865
+ ___Block_byref_object_dispose_.20396
+ ___Block_byref_object_dispose_.21468
+ ___Block_byref_object_dispose_.22413
+ ___Block_byref_object_dispose_.23085
+ ___Block_byref_object_dispose_.23503
+ ___Block_byref_object_dispose_.24101
+ ___Block_byref_object_dispose_.26213
+ ___Block_byref_object_dispose_.29059
+ ___Block_byref_object_dispose_.30731
+ ___Block_byref_object_dispose_.35035
+ ___Block_byref_object_dispose_.35479
+ ___Block_byref_object_dispose_.37704
+ ___Block_byref_object_dispose_.38885
+ ___Block_byref_object_dispose_.42007
+ ___Block_byref_object_dispose_.46658
+ ___Block_byref_object_dispose_.47917
+ ___Block_byref_object_dispose_.48642
+ ___Block_byref_object_dispose_.48924
+ ___Block_byref_object_dispose_.5358
+ ___Block_byref_object_dispose_.5764
+ ___Block_byref_object_dispose_.7900
+ ___Block_byref_object_dispose_.8704
+ ___Block_byref_object_dispose_.9935
+ ___BluetoothManagerLibraryCore_block_invoke.20380
+ ___DataCollectionServicesLibrary_block_invoke.46523
+ ___IntentsLibraryCore_block_invoke.15192
+ ___IntentsLibraryCore_block_invoke.31146
+ ___MediaExperienceLibraryCore_block_invoke.27550
+ ___STCallServiceGetDescription_block_invoke
+ ___block_descriptor_100_e8_32s40s48s56s64s72s80s88s_e41_v16?0"<AFCompanionDeviceInfoMutating>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_62_e8_32s_e40_v16?0"<AFModesConfigurationMutating>"8ls32l8
+ ___block_descriptor_76_e8_32s40s48s56s64s_e36_v16?0"<AFSharedUserInfoMutating>"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_90_e8_32s40s48s56s64s_e41_v16?0"<AFClientConfigurationMutating>"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.101.22542
+ ___block_literal_global.101.38992
+ ___block_literal_global.1024
+ ___block_literal_global.103.22538
+ ___block_literal_global.1035
+ ___block_literal_global.10368
+ ___block_literal_global.1038
+ ___block_literal_global.1041
+ ___block_literal_global.10425
+ ___block_literal_global.1050
+ ___block_literal_global.1053
+ ___block_literal_global.1056
+ ___block_literal_global.10577
+ ___block_literal_global.1059
+ ___block_literal_global.10644
+ ___block_literal_global.1083
+ ___block_literal_global.1086
+ ___block_literal_global.1089
+ ___block_literal_global.109.22531
+ ___block_literal_global.1091
+ ___block_literal_global.111.22528
+ ___block_literal_global.11139
+ ___block_literal_global.112.10572
+ ___block_literal_global.115.22523
+ ___block_literal_global.11680
+ ___block_literal_global.1172
+ ___block_literal_global.11759
+ ___block_literal_global.11786
+ ___block_literal_global.11861
+ ___block_literal_global.1191
+ ___block_literal_global.1195
+ ___block_literal_global.1197
+ ___block_literal_global.1199
+ ___block_literal_global.120.10509
+ ___block_literal_global.1201
+ ___block_literal_global.1203
+ ___block_literal_global.1205
+ ___block_literal_global.12066
+ ___block_literal_global.121.33777
+ ___block_literal_global.1221
+ ___block_literal_global.123.22515
+ ___block_literal_global.12322
+ ___block_literal_global.12362
+ ___block_literal_global.12858
+ ___block_literal_global.129.22509
+ ___block_literal_global.129.33773
+ ___block_literal_global.13002
+ ___block_literal_global.131.45971
+ ___block_literal_global.1339
+ ___block_literal_global.134
+ ___block_literal_global.135.33767
+ ___block_literal_global.13722
+ ___block_literal_global.13916
+ ___block_literal_global.14073
+ ___block_literal_global.141.33755
+ ___block_literal_global.1419
+ ___block_literal_global.142.43625
+ ___block_literal_global.144.33731
+ ___block_literal_global.14400
+ ___block_literal_global.14428
+ ___block_literal_global.14537
+ ___block_literal_global.148.43638
+ ___block_literal_global.15.23094
+ ___block_literal_global.15.27061
+ ___block_literal_global.15.44567
+ ___block_literal_global.15.45917
+ ___block_literal_global.152.22486
+ ___block_literal_global.1542
+ ___block_literal_global.160.43632
+ ___block_literal_global.16033
+ ___block_literal_global.163.43622
+ ___block_literal_global.16393
+ ___block_literal_global.16597
+ ___block_literal_global.16734
+ ___block_literal_global.168.22479
+ ___block_literal_global.168.33741
+ ___block_literal_global.16903
+ ___block_literal_global.17138
+ ___block_literal_global.17172
+ ___block_literal_global.17574
+ ___block_literal_global.176.22473
+ ___block_literal_global.178.41614
+ ___block_literal_global.182.46113
+ ___block_literal_global.18592
+ ___block_literal_global.18611
+ ___block_literal_global.188.46128
+ ___block_literal_global.18959
+ ___block_literal_global.19102
+ ___block_literal_global.19141
+ ___block_literal_global.19173
+ ___block_literal_global.1946
+ ___block_literal_global.1950
+ ___block_literal_global.19730
+ ___block_literal_global.198.46138
+ ___block_literal_global.19805
+ ___block_literal_global.19866
+ ___block_literal_global.2005
+ ___block_literal_global.2012
+ ___block_literal_global.2015
+ ___block_literal_global.20437
+ ___block_literal_global.2062
+ ___block_literal_global.20679
+ ___block_literal_global.2072
+ ___block_literal_global.20816
+ ___block_literal_global.2089
+ ___block_literal_global.20961
+ ___block_literal_global.21065
+ ___block_literal_global.2116
+ ___block_literal_global.21189
+ ___block_literal_global.2119
+ ___block_literal_global.21219
+ ___block_literal_global.2134
+ ___block_literal_global.21620
+ ___block_literal_global.22602
+ ___block_literal_global.23102
+ ___block_literal_global.23553
+ ___block_literal_global.23577
+ ___block_literal_global.23660
+ ___block_literal_global.24047
+ ___block_literal_global.241.46167
+ ___block_literal_global.24223
+ ___block_literal_global.252
+ ___block_literal_global.25386
+ ___block_literal_global.2555
+ ___block_literal_global.26.45928
+ ___block_literal_global.26289
+ ___block_literal_global.26316
+ ___block_literal_global.26582
+ ___block_literal_global.26780
+ ___block_literal_global.26949
+ ___block_literal_global.27081
+ ___block_literal_global.27268
+ ___block_literal_global.27579
+ ___block_literal_global.283
+ ___block_literal_global.2832
+ ___block_literal_global.28409
+ ___block_literal_global.28595
+ ___block_literal_global.289
+ ___block_literal_global.29016
+ ___block_literal_global.29094
+ ___block_literal_global.29189
+ ___block_literal_global.2927
+ ___block_literal_global.29509
+ ___block_literal_global.29572
+ ___block_literal_global.298
+ ___block_literal_global.30214
+ ___block_literal_global.30341
+ ___block_literal_global.30440
+ ___block_literal_global.30483
+ ___block_literal_global.311
+ ___block_literal_global.31290
+ ___block_literal_global.313
+ ___block_literal_global.32006
+ ___block_literal_global.3240
+ ___block_literal_global.32936
+ ___block_literal_global.3306
+ ___block_literal_global.33306
+ ___block_literal_global.3331
+ ___block_literal_global.33780
+ ___block_literal_global.33915
+ ___block_literal_global.34
+ ___block_literal_global.34601
+ ___block_literal_global.35194
+ ___block_literal_global.35323
+ ___block_literal_global.35491
+ ___block_literal_global.35563
+ ___block_literal_global.37
+ ___block_literal_global.37191
+ ___block_literal_global.37211
+ ___block_literal_global.37635
+ ___block_literal_global.37722
+ ___block_literal_global.38.22590
+ ___block_literal_global.38575
+ ___block_literal_global.38604
+ ___block_literal_global.38699
+ ___block_literal_global.38766
+ ___block_literal_global.38999
+ ___block_literal_global.39193
+ ___block_literal_global.39656
+ ___block_literal_global.39707
+ ___block_literal_global.40.47423
+ ___block_literal_global.404
+ ___block_literal_global.40647
+ ___block_literal_global.40681
+ ___block_literal_global.40955
+ ___block_literal_global.411
+ ___block_literal_global.41179
+ ___block_literal_global.41610
+ ___block_literal_global.41822
+ ___block_literal_global.42.14894
+ ___block_literal_global.42.22583
+ ___block_literal_global.42033
+ ___block_literal_global.42155
+ ___block_literal_global.43.47417
+ ___block_literal_global.43387
+ ___block_literal_global.43448
+ ___block_literal_global.43647
+ ___block_literal_global.44100
+ ___block_literal_global.44371
+ ___block_literal_global.44463
+ ___block_literal_global.4448
+ ___block_literal_global.44571
+ ___block_literal_global.45781
+ ___block_literal_global.45912
+ ___block_literal_global.4627
+ ___block_literal_global.47.48938
+ ___block_literal_global.47086
+ ___block_literal_global.47109
+ ___block_literal_global.47263
+ ___block_literal_global.47411
+ ___block_literal_global.479
+ ___block_literal_global.47936
+ ___block_literal_global.48.26957
+ ___block_literal_global.48597
+ ___block_literal_global.489
+ ___block_literal_global.48946
+ ___block_literal_global.5.48929
+ ___block_literal_global.501
+ ___block_literal_global.506
+ ___block_literal_global.515
+ ___block_literal_global.521
+ ___block_literal_global.524
+ ___block_literal_global.54.22573
+ ___block_literal_global.55.48934
+ ___block_literal_global.5512
+ ___block_literal_global.555
+ ___block_literal_global.557
+ ___block_literal_global.559
+ ___block_literal_global.561
+ ___block_literal_global.5684
+ ___block_literal_global.57
+ ___block_literal_global.5751
+ ___block_literal_global.583
+ ___block_literal_global.63.35494
+ ___block_literal_global.66.19860
+ ___block_literal_global.68.19856
+ ___block_literal_global.68.35498
+ ___block_literal_global.6872
+ ___block_literal_global.6943
+ ___block_literal_global.6970
+ ___block_literal_global.70.45946
+ ___block_literal_global.71.30403
+ ___block_literal_global.710
+ ___block_literal_global.719
+ ___block_literal_global.72
+ ___block_literal_global.726
+ ___block_literal_global.73.35499
+ ___block_literal_global.734
+ ___block_literal_global.746
+ ___block_literal_global.749
+ ___block_literal_global.75.22561
+ ___block_literal_global.75.45953
+ ___block_literal_global.760
+ ___block_literal_global.768
+ ___block_literal_global.773
+ ___block_literal_global.8197
+ ___block_literal_global.82.45964
+ ___block_literal_global.8234
+ ___block_literal_global.8259
+ ___block_literal_global.833
+ ___block_literal_global.8361
+ ___block_literal_global.8413
+ ___block_literal_global.843
+ ___block_literal_global.849
+ ___block_literal_global.85.22554
+ ___block_literal_global.85.26952
+ ___block_literal_global.854
+ ___block_literal_global.859
+ ___block_literal_global.859.46761
+ ___block_literal_global.86
+ ___block_literal_global.868
+ ___block_literal_global.870
+ ___block_literal_global.89.43512
+ ___block_literal_global.8908
+ ___block_literal_global.907
+ ___block_literal_global.93.22548
+ ___block_literal_global.949
+ ___block_literal_global.95.38996
+ ___block_literal_global.962
+ ___block_literal_global.965
+ ___block_literal_global.968
+ ___block_literal_global.972
+ ___block_literal_global.9727
+ ___block_literal_global.976
+ ___getBMSiriServiceClass_block_invoke.27092
+ ___getBiomeLibrarySymbolLoc_block_invoke.45755
+ ___getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.15196
+ ___getINSendMessageIntentIdentifierSymbolLoc_block_invoke.15187
+ ___initLSApplicationProxy_block_invoke.34605
+ ___initLSApplicationProxy_block_invoke.46508
+ ___initVTPreferences_block_invoke.46718
+ _audit_stringBiomeLibrary.27076
+ _audit_stringBiomeLibrary.45769
+ _audit_stringBluetoothManager.20384
+ _audit_stringIntents.15194
+ _audit_stringIntents.31160
+ _audit_stringMediaExperience.27553
+ _classLSApplicationProxy.34602
+ _classLSApplicationProxy.46506
+ _classVTPreferences.46716
+ _getBMSiriServiceClass.softClass.27091
+ _getBiomeLibrarySymbolLoc.ptr.45754
+ _getBluetoothPairedStatusChangedNotification.45866
+ _getINSearchForMessagesIntentIdentifier.15185
+ _getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.15195
+ _getINSendMessageIntentIdentifierSymbolLoc.ptr.15186
+ _getLSApplicationProxyClass.34594
+ _getLSApplicationProxyClass.46502
+ _getVTPreferencesClass.46712
+ _initLSApplicationProxy.34599
+ _initLSApplicationProxy.46504
+ _initLSApplicationProxy.sOnce.34600
+ _initLSApplicationProxy.sOnce.46505
+ _initVTPreferences.46714
+ _initVTPreferences.sOnce.46715
+ _objc_msgSend$_audioRouteMonitor
+ _objc_msgSend$_broadcastRouteChangeFrom:to:
+ _objc_msgSend$_isAppleHeadphone
+ _objc_msgSend$_setError
+ _objc_msgSend$_updateAudioRouteFromRoute:toRoute:andBroadcast:
+ _objc_msgSend$carOwnsMainAudio
+ _objc_msgSend$companionName
+ _objc_msgSend$currentAudioRouteDidChangeFrom:to:
+ _objc_msgSend$deleteItemAtFilePath:error:
+ _objc_msgSend$didReceivePluginSelected:
+ _objc_msgSend$effectiveGenderKeyForKey:gender:
+ _objc_msgSend$endWaitingForEmergency
+ _objc_msgSend$faceTimeAudioServiceName
+ _objc_msgSend$faceTimeServiceName
+ _objc_msgSend$getCarOwnsMainAudio
+ _objc_msgSend$getCompanionName
+ _objc_msgSend$getIsMediaFallbackUser
+ _objc_msgSend$getODDDeviceAggregationId:
+ _objc_msgSend$hasError
+ _objc_msgSend$initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:carOwnsMainAudio:
+ _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:
+ _objc_msgSend$initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isUserEngagedWithDevice:
+ _objc_msgSend$initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:isMediaFallbackUser:
+ _objc_msgSend$initWithVoiceFeedbackIdentifier:audioData:asbd:
+ _objc_msgSend$initWithVoiceFeedbackIdentifier:text:
+ _objc_msgSend$isMediaFallbackUser
+ _objc_msgSend$isSAEi18nWave2Enabled
+ _objc_msgSend$isUIUtteranceJSStringCatalogEnabled
+ _objc_msgSend$localizedStringForKey:value:table:localizations:
+ _objc_msgSend$localizedStringFromCatalogForKey:gender:table:bundle:languageCode:defaultValue:
+ _objc_msgSend$localizedStringOrNilFromCatalogForKey:gender:table:bundle:languageCode:defaultValue:
+ _objc_msgSend$messagesContext
+ _objc_msgSend$position
+ _objc_msgSend$sendSampledAudioToServerIgnoringMinimumSampleAge:completion:
+ _objc_msgSend$setCarOwnsMainAudio:
+ _objc_msgSend$setCompanionName:
+ _objc_msgSend$setIsMediaFallbackUser:
+ _objc_msgSend$setMessagesContext:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setShouldPerformFullPayloadCorrection:
+ _objc_msgSend$setSuggestionRequestType:
+ _objc_msgSend$shouldPerformFullPayloadCorrection
+ _objc_msgSend$trackEvent:forTurn:
+ _objc_retain_x15
+ _provider.onceToken.15199
+ _provider.provider.15200
+ _sharedInstance.onceToken.17137
+ _sharedInstance.onceToken.22630
+ _sharedInstance.onceToken.23552
+ _sharedInstance.onceToken.28594
+ _sharedInstance.onceToken.37210
+ _sharedInstance.onceToken.44589
+ _sharedInstance.singleton.44590
+ _sharedManager.onceToken.16596
+ _sharedManager.onceToken.22100
+ _sharedManager.onceToken.32935
+ _sharedManager.onceToken.43386
+ _sharedManager.result.32937
+ _sharedManager.sharedManager.43388
+ _sharedMonitor.monitor.20451
+ _sharedMonitor.onceToken.19662
+ _sharedMonitor.onceToken.20450
+ _sharedObserver.onceToken.31289
+ _sharedObserver.onceToken.48945
+ _sharedObserver.sharedObserver.31291
+ _sharedObserver.sharedObserver.48947
- +[AFFeatureFlags(SWEFeatureFlags) isHintsEnabled]
- +[AFLocalSpeechRecognitionSamplingUtilities calculateFileNameAgeInDays:]
- +[AFSiriAnnounceWorkoutVoiceFeedbackRequest deactivateOngoingRequestWithCompletion:]
- -[AFAttentionAwarenessController .cxx_destruct]
- -[AFAttentionAwarenessController identifier]
- -[AFAttentionAwarenessController initWithIdentifier:]
- -[AFAttentionAwarenessController requestAttentionStateWithCompletion:]
- -[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:]
- -[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:]
- -[AFModesConfiguration buttonPressDetected]
- -[AFModesConfiguration deviceMotion]
- -[AFModesConfiguration deviceOrientation]
- -[AFModesConfiguration deviceRaised]
- -[AFModesConfiguration faceDetected]
- -[AFModesConfiguration flatDevicePosture]
- -[AFModesConfiguration initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:isUserEngagedWithDevice:]
- -[AFModesConfiguration isBacklightOn]
- -[AFModesConfiguration isInPocket]
- -[AFModesConfiguration isInSleepLock]
- -[AFModesConfiguration isInTheaterMode]
- -[AFModesConfiguration isInWaterLock]
- -[AFModesConfiguration isInWorkout]
- -[AFModesConfiguration isMediaPlaying]
- -[AFModesConfiguration isOnWrist]
- -[AFModesConfiguration liftToWakeDetected]
- -[AFModesConfiguration touchScreenDetected]
- -[AFModesConfiguration userInitiatedWakeDetected]
- -[AFPeerInfo initWithIsDeviceOwnedByCurrentUser:assistantIdentifier:sharedUserIdentifier:idsIdentifier:idsDeviceUniqueIdentifier:rapportEffectiveIdentifier:homeKitAccessoryIdentifier:mediaSystemIdentifier:mediaRouteIdentifier:isCommunalDevice:roomName:name:productType:buildVersion:userInterfaceIdiom:aceVersion:isLocationSharingDevice:myriadTrialTreatment:]
- -[AFPreferences databaseSyncEnabled]
- -[AFPreferences deviceHasAtvInHome]
- -[AFPreferences setDatabaseSyncEnabled:]
- -[AFSettingsConnection sendSampledAudioToServerWithCompletion:]
- -[AFSettingsConnection(Internal) _readSyncTokenForAceHost:completion:]
- -[AFSettingsConnection(Internal) _sendSyncTokenToPersonalRequestsEnabledAccessoriesWithCompletion:]
- -[AFSettingsConnection(Internal) _setSyncToken:forAceHost:completion:]
- -[AFSettingsConnection(Internal) _setSyncVerificationNeededAndFullReportNeeded:shouldPostNotification:completion:]
- -[AFSettingsConnectionServiceDelegate syncVerificationPartialResult:]
- -[AFSettingsConnectionServiceDelegate syncVerificationServerReport:]
- -[AFSharedUserInfo initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:]
- -[AFSiriDataSharingSensitivityManager _isOptedOutOfMTEWithSupportsUOD:]
- -[AFSiriHeadphonesMonitor _broadcastRouteAndAuthenticationCapability]
- -[AFSiriHeadphonesMonitor _updateAudioRouteAvailabilityAndBroadcast:]
- -[AFSiriHeadphonesMonitor deviceRingerObserver:didChangeState:]
- -[AFSiriHeadphonesMonitor initializeAVSystemControllerSubscriptions:]
- -[AFSiriHeadphonesMonitor updateAudioRouteAvailability:]
- -[_AFModesConfigurationMutation getButtonPressDetected]
- -[_AFModesConfigurationMutation getDeviceMotion]
- -[_AFModesConfigurationMutation getDeviceOrientation]
- -[_AFModesConfigurationMutation getDeviceRaised]
- -[_AFModesConfigurationMutation getFaceDetected]
- -[_AFModesConfigurationMutation getFlatDevicePosture]
- -[_AFModesConfigurationMutation getIsBacklightOn]
- -[_AFModesConfigurationMutation getIsInPocket]
- -[_AFModesConfigurationMutation getIsInSleepLock]
- -[_AFModesConfigurationMutation getIsInTheaterMode]
- -[_AFModesConfigurationMutation getIsInWaterLock]
- -[_AFModesConfigurationMutation getIsInWorkout]
- -[_AFModesConfigurationMutation getIsMediaPlaying]
- -[_AFModesConfigurationMutation getIsOnWrist]
- -[_AFModesConfigurationMutation getLiftToWakeDetected]
- -[_AFModesConfigurationMutation getTouchScreenDetected]
- -[_AFModesConfigurationMutation getUserInitiatedWakeDetected]
- -[_AFModesConfigurationMutation setButtonPressDetected:]
- -[_AFModesConfigurationMutation setDeviceMotion:]
- -[_AFModesConfigurationMutation setDeviceOrientation:]
- -[_AFModesConfigurationMutation setDeviceRaised:]
- -[_AFModesConfigurationMutation setFaceDetected:]
- -[_AFModesConfigurationMutation setFlatDevicePosture:]
- -[_AFModesConfigurationMutation setIsBacklightOn:]
- -[_AFModesConfigurationMutation setIsInPocket:]
- -[_AFModesConfigurationMutation setIsInSleepLock:]
- -[_AFModesConfigurationMutation setIsInTheaterMode:]
- -[_AFModesConfigurationMutation setIsInWaterLock:]
- -[_AFModesConfigurationMutation setIsInWorkout:]
- -[_AFModesConfigurationMutation setIsMediaPlaying:]
- -[_AFModesConfigurationMutation setIsOnWrist:]
- -[_AFModesConfigurationMutation setLiftToWakeDetected:]
- -[_AFModesConfigurationMutation setTouchScreenDetected:]
- -[_AFModesConfigurationMutation setUserInitiatedWakeDetected:]
- GCC_except_table10102
- GCC_except_table10105
- GCC_except_table10114
- GCC_except_table1014
- GCC_except_table10140
- GCC_except_table10161
- GCC_except_table1080
- GCC_except_table1086
- GCC_except_table10876
- GCC_except_table10889
- GCC_except_table11077
- GCC_except_table11215
- GCC_except_table11228
- GCC_except_table11266
- GCC_except_table11521
- GCC_except_table11666
- GCC_except_table11685
- GCC_except_table11688
- GCC_except_table11690
- GCC_except_table1227
- GCC_except_table1229
- GCC_except_table1416
- GCC_except_table1453
- GCC_except_table1463
- GCC_except_table1480
- GCC_except_table1565
- GCC_except_table1571
- GCC_except_table1574
- GCC_except_table1639
- GCC_except_table1708
- GCC_except_table1730
- GCC_except_table1974
- GCC_except_table2018
- GCC_except_table2186
- GCC_except_table2239
- GCC_except_table2247
- GCC_except_table2305
- GCC_except_table231
- GCC_except_table249
- GCC_except_table253
- GCC_except_table2690
- GCC_except_table2697
- GCC_except_table2701
- GCC_except_table2747
- GCC_except_table2749
- GCC_except_table2755
- GCC_except_table2761
- GCC_except_table2765
- GCC_except_table2769
- GCC_except_table2774
- GCC_except_table2779
- GCC_except_table2781
- GCC_except_table2785
- GCC_except_table2797
- GCC_except_table2822
- GCC_except_table2824
- GCC_except_table2826
- GCC_except_table2828
- GCC_except_table2830
- GCC_except_table2832
- GCC_except_table2875
- GCC_except_table2900
- GCC_except_table2955
- GCC_except_table2985
- GCC_except_table3278
- GCC_except_table3336
- GCC_except_table3459
- GCC_except_table3472
- GCC_except_table3473
- GCC_except_table3485
- GCC_except_table3492
- GCC_except_table3493
- GCC_except_table3496
- GCC_except_table3590
- GCC_except_table3592
- GCC_except_table3609
- GCC_except_table3657
- GCC_except_table3669
- GCC_except_table3739
- GCC_except_table3843
- GCC_except_table3850
- GCC_except_table3864
- GCC_except_table3901
- GCC_except_table3987
- GCC_except_table4041
- GCC_except_table4451
- GCC_except_table4454
- GCC_except_table4455
- GCC_except_table446
- GCC_except_table4742
- GCC_except_table4808
- GCC_except_table4871
- GCC_except_table4881
- GCC_except_table4892
- GCC_except_table4904
- GCC_except_table494
- GCC_except_table5025
- GCC_except_table513
- GCC_except_table5379
- GCC_except_table5382
- GCC_except_table5472
- GCC_except_table5478
- GCC_except_table5556
- GCC_except_table5558
- GCC_except_table5575
- GCC_except_table5576
- GCC_except_table5598
- GCC_except_table5601
- GCC_except_table5613
- GCC_except_table5615
- GCC_except_table5633
- GCC_except_table5731
- GCC_except_table5830
- GCC_except_table5851
- GCC_except_table5853
- GCC_except_table5917
- GCC_except_table5919
- GCC_except_table5921
- GCC_except_table5923
- GCC_except_table5937
- GCC_except_table5943
- GCC_except_table6064
- GCC_except_table6071
- GCC_except_table6426
- GCC_except_table6441
- GCC_except_table6474
- GCC_except_table6578
- GCC_except_table6587
- GCC_except_table6626
- GCC_except_table6658
- GCC_except_table6725
- GCC_except_table696
- GCC_except_table706
- GCC_except_table7240
- GCC_except_table7245
- GCC_except_table7248
- GCC_except_table7251
- GCC_except_table7254
- GCC_except_table7257
- GCC_except_table7464
- GCC_except_table7467
- GCC_except_table7469
- GCC_except_table7481
- GCC_except_table7542
- GCC_except_table7548
- GCC_except_table7718
- GCC_except_table7824
- GCC_except_table7854
- GCC_except_table8055
- GCC_except_table8060
- GCC_except_table8124
- GCC_except_table8230
- GCC_except_table825
- GCC_except_table8656
- GCC_except_table8710
- GCC_except_table8754
- GCC_except_table8842
- GCC_except_table8882
- GCC_except_table8913
- GCC_except_table8919
- GCC_except_table8923
- GCC_except_table9169
- GCC_except_table9239
- GCC_except_table9245
- GCC_except_table9280
- GCC_except_table9283
- GCC_except_table9361
- GCC_except_table9390
- GCC_except_table9462
- GCC_except_table9465
- GCC_except_table9469
- GCC_except_table9575
- GCC_except_table9579
- GCC_except_table9583
- GCC_except_table9616
- GCC_except_table9661
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _AFSiriHeadphonesMonitorGetCurrentlySelectedAudioRoute
- _AFSiriLogContextMUXReverseSync
- _AWAttentionAwarenessClientFunction
- _AWAttentionAwarenessConfigurationFunction
- _AnnounceLibrary.sLib.43637
- _AnnounceLibrary.sOnce.43635
- _AttentionAwarenessLibrary
- _AttentionAwarenessLibrary.frameworkLibrary
- _BiomeLibraryLibraryCore.45737
- _BiomeLibraryLibraryCore.frameworkLibrary.27115
- _BiomeLibraryLibraryCore.frameworkLibrary.45740
- _BluetoothManagerLibrary.45862
- _BluetoothManagerLibraryCore.frameworkLibrary.20304
- _CoreServicesLibrary.frameworkLibrary.46468
- _CoreSpeechLibrary.frameworkLibrary.39287
- _DataCollectionServicesLibrary.sLib.46487
- _DataCollectionServicesLibrary.sOnce.46486
- _IntentsLibrary.15261
- _IntentsLibraryCore.frameworkLibrary.15264
- _IntentsLibraryCore.frameworkLibrary.31136
- _LSApplicationProxyFunction.34600
- _LSApplicationProxyFunction.46474
- _MediaExperienceLibrary.27471
- _MediaExperienceLibraryCore.frameworkLibrary.27498
- _OBJC_CLASS_$_AFAttentionAwarenessController
- _OBJC_IVAR_$_AFAttentionAwarenessController._attentionClient
- _OBJC_IVAR_$_AFAttentionAwarenessController._attentionQueue
- _OBJC_IVAR_$_AFAttentionAwarenessController._identifier
- _OBJC_IVAR_$_AFModesConfiguration._buttonPressDetected
- _OBJC_IVAR_$_AFModesConfiguration._deviceMotion
- _OBJC_IVAR_$_AFModesConfiguration._deviceOrientation
- _OBJC_IVAR_$_AFModesConfiguration._deviceRaised
- _OBJC_IVAR_$_AFModesConfiguration._faceDetected
- _OBJC_IVAR_$_AFModesConfiguration._flatDevicePosture
- _OBJC_IVAR_$_AFModesConfiguration._isBacklightOn
- _OBJC_IVAR_$_AFModesConfiguration._isInPocket
- _OBJC_IVAR_$_AFModesConfiguration._isInSleepLock
- _OBJC_IVAR_$_AFModesConfiguration._isInTheaterMode
- _OBJC_IVAR_$_AFModesConfiguration._isInWaterLock
- _OBJC_IVAR_$_AFModesConfiguration._isInWorkout
- _OBJC_IVAR_$_AFModesConfiguration._isMediaPlaying
- _OBJC_IVAR_$_AFModesConfiguration._isOnWrist
- _OBJC_IVAR_$_AFModesConfiguration._liftToWakeDetected
- _OBJC_IVAR_$_AFModesConfiguration._touchScreenDetected
- _OBJC_IVAR_$_AFModesConfiguration._userInitiatedWakeDetected
- _OBJC_IVAR_$_AFSiriAnnounceWorkoutVoiceFeedbackRequest._data
- _OBJC_IVAR_$_AFSiriAudioRoute._avAudioRouteName
- _OBJC_IVAR_$_AFSiriHeadphonesMonitor._ringerSwitchObserver
- _OBJC_IVAR_$__AFModesConfigurationMutation._buttonPressDetected
- _OBJC_IVAR_$__AFModesConfigurationMutation._deviceMotion
- _OBJC_IVAR_$__AFModesConfigurationMutation._deviceOrientation
- _OBJC_IVAR_$__AFModesConfigurationMutation._deviceRaised
- _OBJC_IVAR_$__AFModesConfigurationMutation._faceDetected
- _OBJC_IVAR_$__AFModesConfigurationMutation._flatDevicePosture
- _OBJC_IVAR_$__AFModesConfigurationMutation._isBacklightOn
- _OBJC_IVAR_$__AFModesConfigurationMutation._isInPocket
- _OBJC_IVAR_$__AFModesConfigurationMutation._isInSleepLock
- _OBJC_IVAR_$__AFModesConfigurationMutation._isInTheaterMode
- _OBJC_IVAR_$__AFModesConfigurationMutation._isInWaterLock
- _OBJC_IVAR_$__AFModesConfigurationMutation._isInWorkout
- _OBJC_IVAR_$__AFModesConfigurationMutation._isMediaPlaying
- _OBJC_IVAR_$__AFModesConfigurationMutation._isOnWrist
- _OBJC_IVAR_$__AFModesConfigurationMutation._liftToWakeDetected
- _OBJC_IVAR_$__AFModesConfigurationMutation._touchScreenDetected
- _OBJC_IVAR_$__AFModesConfigurationMutation._userInitiatedWakeDetected
- _OBJC_METACLASS_$_AFAttentionAwarenessController
- _SoftBiomeLibrary.45723
- _VTPreferencesFunction.46616
- _VoiceTriggerLibrary.frameworkLibrary.46610
- __AFPreferencesDatabaseSyncingEnabled
- __AFPreferencesReplacementLanguageForLocalRecognizerLanguageCode.onDeviceAlternativeForLanguageCode
- __AFPreferencesReplacementLanguageForLocalRecognizerLanguageCode.onceToken
- __AFPreferencesSetDatabaseSyncingEnabled
- __OBJC_$_INSTANCE_METHODS_AFAttentionAwarenessController
- __OBJC_$_INSTANCE_METHODS_AFLocalization
- __OBJC_$_INSTANCE_VARIABLES_AFAttentionAwarenessController
- __OBJC_$_PROP_LIST_AFAttentionAwarenessController
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFSettingsServiceDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_AFSettingsServiceDelegate
- __OBJC_CLASS_RO_$_AFAttentionAwarenessController
- __OBJC_METACLASS_RO_$_AFAttentionAwarenessController
- ___114-[AFSettingsConnection(Internal) _setSyncVerificationNeededAndFullReportNeeded:shouldPostNotification:completion:]_block_invoke
- ___164-[AFSharedUserInfo initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:]_block_invoke
- ___197-[AFCompanionDeviceInfo initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:]_block_invoke
- ___27-[AFConnection _connection]_block_invoke.229
- ___27-[AFConnection _connection]_block_invoke_2.230
- ___32-[AFSiriHeadphonesMonitor _init]_block_invoke_2
- ___348-[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:]_block_invoke
- ___358-[AFPeerInfo initWithIsDeviceOwnedByCurrentUser:assistantIdentifier:sharedUserIdentifier:idsIdentifier:idsDeviceUniqueIdentifier:rapportEffectiveIdentifier:homeKitAccessoryIdentifier:mediaSystemIdentifier:mediaRouteIdentifier:isCommunalDevice:roomName:name:productType:buildVersion:userInterfaceIdiom:aceVersion:isLocationSharingDevice:myriadTrialTreatment:]_block_invoke
- ___38-[AFConnection _startRequestWithInfo:]_block_invoke.321
- ___38-[AFConnection _startRequestWithInfo:]_block_invoke.326
- ___38-[AFConnection _startRequestWithInfo:]_block_invoke_2.322
- ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke.344
- ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke_2.345
- ___56-[AFSiriHeadphonesMonitor updateAudioRouteAvailability:]_block_invoke
- ___58-[AFConnection acquireAudioSessionWithContext:completion:]_block_invoke.307
- ___59-[AFSiriHeadphonesMonitor _settingsConnectionDidDisconnect]_block_invoke.24
- ___60-[AFMyriadEmergencyCallPunchout initiateEmergencyCallMyriad]_block_invoke.6
- ___60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.561
- ___612-[AFModesConfiguration initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:isUserEngagedWithDevice:]_block_invoke
- ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.294
- ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.301
- ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke_2.305
- ___63-[AFSettingsConnection sendSampledAudioToServerWithCompletion:]_block_invoke
- ___63-[AFSiriHeadphonesMonitor deviceRingerObserver:didChangeState:]_block_invoke
- ___64-[AFConnectionClientServiceDelegate requestHandleCommand:reply:]_block_invoke.747
- ___64-[AFSiriHeadphonesMonitor notifyObserver:didChangeStateFrom:to:]_block_invoke.27
- ___66-[AFSiriHeadphonesMonitor fetchPrivateSessionStateWithCompletion:]_block_invoke.39
- ___69-[AFSiriHeadphonesMonitor _broadcastRouteAndAuthenticationCapability]_block_invoke
- ___69-[AFSiriHeadphonesMonitor _updateAudioRouteAvailabilityAndBroadcast:]_block_invoke
- ___69-[AFSiriHeadphonesMonitor _updateAudioRouteAvailabilityAndBroadcast:]_block_invoke.21
- ___69-[AFSiriHeadphonesMonitor _updateAudioRouteAvailabilityAndBroadcast:]_block_invoke_2
- ___69-[AFSiriHeadphonesMonitor initializeAVSystemControllerSubscriptions:]_block_invoke
- ___70-[AFAttentionAwarenessController requestAttentionStateWithCompletion:]_block_invoke
- ___70-[AFSettingsConnection(Internal) _readSyncTokenForAceHost:completion:]_block_invoke
- ___70-[AFSettingsConnection(Internal) _setSyncToken:forAceHost:completion:]_block_invoke
- ___70-[AFSettingsConnection(Internal) _setSyncToken:forAceHost:completion:]_block_invoke.563
- ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke.342
- ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke_2.343
- ___84+[AFSiriAnnounceWorkoutVoiceFeedbackRequest deactivateOngoingRequestWithCompletion:]_block_invoke
- ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.339
- ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.341
- ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke_2.340
- ___85-[AFSiriHeadphonesMonitor _postJSDiscoveryNotificationForBTDeviceWithInfo:scheduled:]_block_invoke.50
- ___90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.117
- ___90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.120
- ___99-[AFSettingsConnection(Internal) _sendSyncTokenToPersonalRequestsEnabledAccessoriesWithCompletion:]_block_invoke
- ___99-[AFSettingsConnection(Internal) _sendSyncTokenToPersonalRequestsEnabledAccessoriesWithCompletion:]_block_invoke.564
- ___AnnounceLibrary_block_invoke.43641
- ___BiomeLibraryLibraryCore_block_invoke.27116
- ___BiomeLibraryLibraryCore_block_invoke.45741
- ___Block_byref_object_copy_.10017
- ___Block_byref_object_copy_.10708
- ___Block_byref_object_copy_.10901
- ___Block_byref_object_copy_.11533
- ___Block_byref_object_copy_.12112
- ___Block_byref_object_copy_.13370
- ___Block_byref_object_copy_.13648
- ___Block_byref_object_copy_.16630
- ___Block_byref_object_copy_.17157
- ___Block_byref_object_copy_.17643
- ___Block_byref_object_copy_.19791
- ___Block_byref_object_copy_.20319
- ___Block_byref_object_copy_.21330
- ___Block_byref_object_copy_.22266
- ___Block_byref_object_copy_.22950
- ___Block_byref_object_copy_.23369
- ___Block_byref_object_copy_.23966
- ___Block_byref_object_copy_.26255
- ___Block_byref_object_copy_.29006
- ___Block_byref_object_copy_.30720
- ___Block_byref_object_copy_.35027
- ___Block_byref_object_copy_.35471
- ___Block_byref_object_copy_.37704
- ___Block_byref_object_copy_.38905
- ___Block_byref_object_copy_.42023
- ___Block_byref_object_copy_.46573
- ___Block_byref_object_copy_.47805
- ___Block_byref_object_copy_.48533
- ___Block_byref_object_copy_.48815
- ___Block_byref_object_copy_.5395
- ___Block_byref_object_copy_.5802
- ___Block_byref_object_copy_.7947
- ___Block_byref_object_copy_.8775
- ___Block_byref_object_dispose_.10018
- ___Block_byref_object_dispose_.10709
- ___Block_byref_object_dispose_.10902
- ___Block_byref_object_dispose_.11534
- ___Block_byref_object_dispose_.12113
- ___Block_byref_object_dispose_.13371
- ___Block_byref_object_dispose_.13649
- ___Block_byref_object_dispose_.16631
- ___Block_byref_object_dispose_.17158
- ___Block_byref_object_dispose_.17644
- ___Block_byref_object_dispose_.19792
- ___Block_byref_object_dispose_.20320
- ___Block_byref_object_dispose_.21331
- ___Block_byref_object_dispose_.22267
- ___Block_byref_object_dispose_.22951
- ___Block_byref_object_dispose_.23370
- ___Block_byref_object_dispose_.23967
- ___Block_byref_object_dispose_.26256
- ___Block_byref_object_dispose_.29007
- ___Block_byref_object_dispose_.30721
- ___Block_byref_object_dispose_.35028
- ___Block_byref_object_dispose_.35472
- ___Block_byref_object_dispose_.37705
- ___Block_byref_object_dispose_.38906
- ___Block_byref_object_dispose_.42024
- ___Block_byref_object_dispose_.46574
- ___Block_byref_object_dispose_.47806
- ___Block_byref_object_dispose_.48534
- ___Block_byref_object_dispose_.48816
- ___Block_byref_object_dispose_.5396
- ___Block_byref_object_dispose_.5803
- ___Block_byref_object_dispose_.7948
- ___Block_byref_object_dispose_.8776
- ___BluetoothManagerLibraryCore_block_invoke.20305
- ___DataCollectionServicesLibrary_block_invoke.46490
- ___IntentsLibraryCore_block_invoke.15265
- ___IntentsLibraryCore_block_invoke.31137
- ___MediaExperienceLibraryCore_block_invoke.27499
- ____AFPreferencesReplacementLanguageForLocalRecognizerLanguageCode_block_invoke
- ___block_descriptor_155_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136s144s_e30_v16?0"<AFPeerInfoMutating>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8s120l8s128l8s136l8s144l8
- ___block_descriptor_170_e8_32s_e40_v16?0"<AFModesConfigurationMutating>"8ls32l8
- ___block_descriptor_75_e8_32s40s48s56s64s_e36_v16?0"<AFSharedUserInfoMutating>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_89_e8_32s40s48s56s64s_e41_v16?0"<AFClientConfigurationMutating>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_92_e8_32s40s48s56s64s72s80s_e41_v16?0"<AFCompanionDeviceInfoMutating>"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.101.22398
- ___block_literal_global.101.39013
- ___block_literal_global.1019
- ___block_literal_global.1025
- ___block_literal_global.103.22394
- ___block_literal_global.1033
- ___block_literal_global.1036
- ___block_literal_global.1040
- ___block_literal_global.10436
- ___block_literal_global.1048
- ___block_literal_global.10493
- ___block_literal_global.1051
- ___block_literal_global.1054
- ___block_literal_global.10646
- ___block_literal_global.107.22390
- ___block_literal_global.10713
- ___block_literal_global.1073
- ___block_literal_global.1081
- ___block_literal_global.1084
- ___block_literal_global.109.22386
- ___block_literal_global.112.10641
- ___block_literal_global.11208
- ___block_literal_global.115.22380
- ___block_literal_global.1169
- ___block_literal_global.11746
- ___block_literal_global.11825
- ___block_literal_global.11852
- ___block_literal_global.1188
- ___block_literal_global.1192
- ___block_literal_global.11927
- ___block_literal_global.1194
- ___block_literal_global.1196
- ___block_literal_global.1198
- ___block_literal_global.120.10577
- ___block_literal_global.1200
- ___block_literal_global.1202
- ___block_literal_global.121.33773
- ___block_literal_global.12132
- ___block_literal_global.1218
- ___block_literal_global.123.22372
- ___block_literal_global.12389
- ___block_literal_global.12429
- ___block_literal_global.129.22366
- ___block_literal_global.129.33769
- ___block_literal_global.12932
- ___block_literal_global.130
- ___block_literal_global.13076
- ___block_literal_global.131.45975
- ___block_literal_global.135.33763
- ___block_literal_global.1377
- ___block_literal_global.13808
- ___block_literal_global.14001
- ___block_literal_global.141.33751
- ___block_literal_global.1413
- ___block_literal_global.14158
- ___block_literal_global.142.43636
- ___block_literal_global.144.33727
- ___block_literal_global.14484
- ___block_literal_global.14512
- ___block_literal_global.14621
- ___block_literal_global.148.43649
- ___block_literal_global.15.22960
- ___block_literal_global.15.27103
- ___block_literal_global.15.44578
- ___block_literal_global.15.45918
- ___block_literal_global.152.22343
- ___block_literal_global.1579
- ___block_literal_global.16
- ___block_literal_global.160.43643
- ___block_literal_global.16103
- ___block_literal_global.163.43633
- ___block_literal_global.16463
- ___block_literal_global.16667
- ___block_literal_global.168.22333
- ___block_literal_global.168.33737
- ___block_literal_global.16804
- ___block_literal_global.16973
- ___block_literal_global.17201
- ___block_literal_global.17235
- ___block_literal_global.176.22327
- ___block_literal_global.17636
- ___block_literal_global.178.41631
- ___block_literal_global.182.46117
- ___block_literal_global.18655
- ___block_literal_global.18674
- ___block_literal_global.188.46131
- ___block_literal_global.19
- ___block_literal_global.19022
- ___block_literal_global.19165
- ___block_literal_global.19205
- ___block_literal_global.19237
- ___block_literal_global.1945
- ___block_literal_global.19657
- ___block_literal_global.19732
- ___block_literal_global.1979
- ___block_literal_global.19793
- ___block_literal_global.198.46141
- ___block_literal_global.2007
- ___block_literal_global.2010
- ___block_literal_global.20373
- ___block_literal_global.2049
- ___block_literal_global.2057
- ___block_literal_global.20621
- ___block_literal_global.2067
- ___block_literal_global.20758
- ___block_literal_global.20825
- ___block_literal_global.20929
- ___block_literal_global.21053
- ___block_literal_global.21083
- ___block_literal_global.2111
- ___block_literal_global.2114
- ___block_literal_global.2124
- ___block_literal_global.2133
- ___block_literal_global.21484
- ___block_literal_global.22.47311
- ___block_literal_global.22458
- ___block_literal_global.22968
- ___block_literal_global.23420
- ___block_literal_global.23444
- ___block_literal_global.23527
- ___block_literal_global.23913
- ___block_literal_global.24095
- ___block_literal_global.241.46170
- ___block_literal_global.25.47305
- ___block_literal_global.253
- ___block_literal_global.25450
- ___block_literal_global.2590
- ___block_literal_global.26.20350
- ___block_literal_global.26.45929
- ___block_literal_global.26332
- ___block_literal_global.26359
- ___block_literal_global.26625
- ___block_literal_global.26822
- ___block_literal_global.26991
- ___block_literal_global.27123
- ___block_literal_global.27310
- ___block_literal_global.27528
- ___block_literal_global.282
- ___block_literal_global.28357
- ___block_literal_global.28543
- ___block_literal_global.2869
- ___block_literal_global.288
- ___block_literal_global.28964
- ___block_literal_global.29042
- ___block_literal_global.29137
- ___block_literal_global.29456
- ___block_literal_global.29506
- ___block_literal_global.2956
- ___block_literal_global.29563
- ___block_literal_global.297
- ___block_literal_global.30205
- ___block_literal_global.30332
- ___block_literal_global.30431
- ___block_literal_global.30474
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.31281
- ___block_literal_global.3269
- ___block_literal_global.32931
- ___block_literal_global.33302
- ___block_literal_global.3335
- ___block_literal_global.3360
- ___block_literal_global.33776
- ___block_literal_global.33911
- ___block_literal_global.34594
- ___block_literal_global.35186
- ___block_literal_global.35315
- ___block_literal_global.35484
- ___block_literal_global.35559
- ___block_literal_global.37187
- ___block_literal_global.37207
- ___block_literal_global.37645
- ___block_literal_global.37724
- ___block_literal_global.38.22446
- ___block_literal_global.38593
- ___block_literal_global.38622
- ___block_literal_global.38719
- ___block_literal_global.38787
- ___block_literal_global.39020
- ___block_literal_global.39215
- ___block_literal_global.39678
- ___block_literal_global.39729
- ___block_literal_global.40672
- ___block_literal_global.40706
- ___block_literal_global.409
- ___block_literal_global.40980
- ___block_literal_global.41204
- ___block_literal_global.41627
- ___block_literal_global.41839
- ___block_literal_global.42.14967
- ___block_literal_global.42.22439
- ___block_literal_global.42050
- ___block_literal_global.42172
- ___block_literal_global.43401
- ___block_literal_global.43459
- ___block_literal_global.43658
- ___block_literal_global.44111
- ___block_literal_global.44382
- ___block_literal_global.44474
- ___block_literal_global.44582
- ___block_literal_global.4483
- ___block_literal_global.45755
- ___block_literal_global.45913
- ___block_literal_global.4659
- ___block_literal_global.46971
- ___block_literal_global.46997
- ___block_literal_global.47.48828
- ___block_literal_global.47151
- ___block_literal_global.47299
- ___block_literal_global.47825
- ___block_literal_global.48.26999
- ___block_literal_global.483
- ___block_literal_global.48489
- ___block_literal_global.487
- ___block_literal_global.48836
- ___block_literal_global.499
- ___block_literal_global.5.48821
- ___block_literal_global.504
- ___block_literal_global.509
- ___block_literal_global.512
- ___block_literal_global.513
- ___block_literal_global.54.22429
- ___block_literal_global.554
- ___block_literal_global.5551
- ___block_literal_global.556
- ___block_literal_global.558
- ___block_literal_global.56.32937
- ___block_literal_global.560
- ___block_literal_global.5723
- ___block_literal_global.5790
- ___block_literal_global.581
- ___block_literal_global.60.35486
- ___block_literal_global.63.35488
- ___block_literal_global.66.19787
- ___block_literal_global.68.19783
- ___block_literal_global.68.35492
- ___block_literal_global.6919
- ___block_literal_global.6990
- ___block_literal_global.70.45947
- ___block_literal_global.7017
- ___block_literal_global.708
- ___block_literal_global.71.30394
- ___block_literal_global.717
- ___block_literal_global.724
- ___block_literal_global.73.22418
- ___block_literal_global.73.35493
- ___block_literal_global.732
- ___block_literal_global.744
- ___block_literal_global.747
- ___block_literal_global.75.45954
- ___block_literal_global.758
- ___block_literal_global.76
- ___block_literal_global.766
- ___block_literal_global.771
- ___block_literal_global.82.45968
- ___block_literal_global.8247
- ___block_literal_global.8284
- ___block_literal_global.8309
- ___block_literal_global.841
- ___block_literal_global.8410
- ___block_literal_global.8462
- ___block_literal_global.85.22410
- ___block_literal_global.85.26994
- ___block_literal_global.85.43524
- ___block_literal_global.852
- ___block_literal_global.857
- ___block_literal_global.862
- ___block_literal_global.864
- ___block_literal_global.873
- ___block_literal_global.88
- ___block_literal_global.889
- ___block_literal_global.896
- ___block_literal_global.8978
- ___block_literal_global.93.22404
- ___block_literal_global.938
- ___block_literal_global.95.39017
- ___block_literal_global.957
- ___block_literal_global.958
- ___block_literal_global.960
- ___block_literal_global.967
- ___block_literal_global.971
- ___block_literal_global.9787
- ___getBMSiriServiceClass_block_invoke.27134
- ___getBiomeLibrarySymbolLoc_block_invoke.45729
- ___getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.15269
- ___getINSendMessageIntentIdentifierSymbolLoc_block_invoke.15260
- ___initAWAttentionAwarenessClient_block_invoke
- ___initAWAttentionAwarenessConfiguration_block_invoke
- ___initLSApplicationProxy_block_invoke.34598
- ___initLSApplicationProxy_block_invoke.46467
- ___initVTPreferences_block_invoke.46609
- __broadcastRouteAndAuthenticationCapability.previousAudioRoute
- _attention_awareness_queue_label
- _audit_stringBiomeLibrary.27118
- _audit_stringBiomeLibrary.45743
- _audit_stringBluetoothManager.20308
- _audit_stringIntents.15267
- _audit_stringIntents.31151
- _audit_stringMediaExperience.27502
- _classAWAttentionAwarenessClient
- _classAWAttentionAwarenessConfiguration
- _classLSApplicationProxy.34595
- _classLSApplicationProxy.46465
- _classVTPreferences.46607
- _getAWAttentionAwarenessClientClass
- _getAWAttentionAwarenessConfigurationClass
- _getBMSiriServiceClass.softClass.27133
- _getBiomeLibrarySymbolLoc.ptr.45728
- _getBluetoothPairedStatusChangedNotification.45865
- _getINSearchForMessagesIntentIdentifier.15258
- _getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.15268
- _getINSendMessageIntentIdentifierSymbolLoc.ptr.15259
- _getLSApplicationProxyClass.34587
- _getLSApplicationProxyClass.46461
- _getVTPreferencesClass.46603
- _initAWAttentionAwarenessClient
- _initAWAttentionAwarenessClient.sOnce
- _initAWAttentionAwarenessConfiguration
- _initAWAttentionAwarenessConfiguration.sOnce
- _initLSApplicationProxy.34592
- _initLSApplicationProxy.46463
- _initLSApplicationProxy.sOnce.34593
- _initLSApplicationProxy.sOnce.46464
- _initVTPreferences.46605
- _initVTPreferences.sOnce.46606
- _kAFSiriLogContextMUXReverseSync
- _objc_msgSend$_broadcastRouteAndAuthenticationCapability
- _objc_msgSend$_isOptedOutOfMTEWithSupportsUOD:
- _objc_msgSend$_setSyncVerificationNeededAndFullReportNeeded:shouldPostNotification:completion:
- _objc_msgSend$_tellDelegatePartialVerificationResult:
- _objc_msgSend$_tellDelegateServerVerificationReport:
- _objc_msgSend$buttonPressDetected
- _objc_msgSend$deleteItemAtFilePath:
- _objc_msgSend$deviceMotion
- _objc_msgSend$deviceOrientation
- _objc_msgSend$deviceRaised
- _objc_msgSend$faceDetected
- _objc_msgSend$flatDevicePosture
- _objc_msgSend$getButtonPressDetected
- _objc_msgSend$getDeviceMotion
- _objc_msgSend$getDeviceOrientation
- _objc_msgSend$getDeviceRaised
- _objc_msgSend$getFaceDetected
- _objc_msgSend$getFlatDevicePosture
- _objc_msgSend$getIsBacklightOn
- _objc_msgSend$getIsInPocket
- _objc_msgSend$getIsInSleepLock
- _objc_msgSend$getIsInTheaterMode
- _objc_msgSend$getIsInWaterLock
- _objc_msgSend$getIsInWorkout
- _objc_msgSend$getIsMediaPlaying
- _objc_msgSend$getIsOnWrist
- _objc_msgSend$getLiftToWakeDetected
- _objc_msgSend$getTouchScreenDetected
- _objc_msgSend$getUserInitiatedWakeDetected
- _objc_msgSend$initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:
- _objc_msgSend$initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:
- _objc_msgSend$initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:isUserEngagedWithDevice:
- _objc_msgSend$initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:
- _objc_msgSend$isBacklightOn
- _objc_msgSend$isInPocket
- _objc_msgSend$isInSleepLock
- _objc_msgSend$isInTheaterMode
- _objc_msgSend$isInWaterLock
- _objc_msgSend$isInWorkout
- _objc_msgSend$isOnWrist
- _objc_msgSend$liftToWakeDetected
- _objc_msgSend$pollForAttentionWithTimeout:event:error:
- _objc_msgSend$readSyncTokenForAceHost:completion:
- _objc_msgSend$resumeWithError:
- _objc_msgSend$routeName
- _objc_msgSend$sendSampledAudioToServerWithCompletion:
- _objc_msgSend$sendSyncTokenToPersonalRequestsEnabledAccessoriesWithCompletion:
- _objc_msgSend$setButtonPressDetected:
- _objc_msgSend$setDeviceMotion:
- _objc_msgSend$setDeviceOrientation:
- _objc_msgSend$setDeviceRaised:
- _objc_msgSend$setEventMask:
- _objc_msgSend$setFaceDetected:
- _objc_msgSend$setFlatDevicePosture:
- _objc_msgSend$setIsBacklightOn:
- _objc_msgSend$setIsInPocket:
- _objc_msgSend$setIsInSleepLock:
- _objc_msgSend$setIsInTheaterMode:
- _objc_msgSend$setIsInWaterLock:
- _objc_msgSend$setIsInWorkout:
- _objc_msgSend$setIsOnWrist:
- _objc_msgSend$setLiftToWakeDetected:
- _objc_msgSend$setSyncToken:forAceHost:completion:
- _objc_msgSend$setTouchScreenDetected:
- _objc_msgSend$setUserInitiatedWakeDetected:
- _objc_msgSend$suspendWithError:
- _objc_msgSend$touchScreenDetected
- _objc_msgSend$userInitiatedWakeDetected
- _provider.onceToken.15272
- _provider.provider.15273
- _sharedInstance.onceToken.17200
- _sharedInstance.onceToken.22492
- _sharedInstance.onceToken.23419
- _sharedInstance.onceToken.28542
- _sharedInstance.onceToken.37206
- _sharedInstance.onceToken.44600
- _sharedInstance.singleton.44601
- _sharedManager.onceToken.16666
- _sharedManager.onceToken.21964
- _sharedManager.onceToken.32930
- _sharedManager.onceToken.43400
- _sharedManager.result.32932
- _sharedManager.sharedManager.43402
- _sharedMonitor.onceToken.20388
- _sharedObserver.onceToken.31280
- _sharedObserver.onceToken.48835
- _sharedObserver.sharedObserver.31282
- _sharedObserver.sharedObserver.48837
CStrings:
+ "%@ {accessibilityState = %@, deviceRingerSwitchState = %@, isDeviceInCarDNDMode = %@, isDeviceInStarkMode = %@, supportsCarPlayVehicleData = %@, isDeviceWatchAuthenticated = %@, areAnnouncementRequestsPermittedByPresentationWhileActive = %@, outputVolume = %f, tapToSiriAudioPlaybackRequest = %@, twoShotAudioPlaybackRequest = %@, deviceSetupFlowBeginDate = %@, deviceSetupFlowEndDate = %@, carOwnsMainAudio = %@}"
+ "%@ {assistantID = %@, speechID = %@, idsIdentifier = %@, productPrefix = %@, aceHost = %@, syncMetadata = %@, syncMetadataCapability = %@, peerToPeerHandoffCapability = %@, muxSupportCapability = %@, meDevice = %@, siriLanguage = %@, companionName = %@}"
+ "%@ {isDeviceOwnedByCurrentUser = %@, assistantIdentifier = %@, sharedUserIdentifier = %@, idsIdentifier = %@, idsDeviceUniqueIdentifier = %@, rapportEffectiveIdentifier = %@, homeKitAccessoryIdentifier = %@, mediaSystemIdentifier = %@, mediaRouteIdentifier = %@, isCommunalDevice = %@, roomName = %@, name = %@, productType = %@, buildVersion = %@, userInterfaceIdiom = %@, aceVersion = %@, isLocationSharingDevice = %@, isSiriCloudSyncEnabled = %@, myriadTrialTreatment = %@}"
+ "%@ {isEyesFree = %@, isUIFree = %@, isForCarDND = %@, isInAmbient = %@, isMapsNavigationActive = %@, isVoiceTriggerRequest = %@, isConnectedToCarPlay = %@, isRequestMadeWithPhysicalDeviceInteraction = %@, isAudioAccessoryButtonActivation = %@, isSiriAutoPrompt = %@, isFlexibleFollowup = %@, userTypedInSiri = %@, modeOverrideValue = %@, isDeviceUnlocked = %@, isDeviceScreenON = %@, isUserEngagedWithDevice = %@}"
+ "%@ {sharedUserId = %@, loggableSharedUserId = %@, companionDeviceInfo = %@, personalRequestsEnabled = %@, companionLinkReady = %@, homeUserId = %@, iCloudAltDSID = %@, isDeviceOwner = %@, isMediaFallbackUser = %@}"
+ "%s #MTEOptOut device is opted out of uploading MTE."
+ "%s #SAEStatus #cacheRead deviceSupportsSAE: %d"
+ "%s #SAEStatus #cacheRead saeAvailable: %d"
+ "%s #SAEStatus #cacheRead saeEnabled: %d"
+ "%s #SAEStatus #cacheRead swaiEnabled: %d"
+ "%s #SAEStatus #cacheRead visualIntelligenceEnabled: %d"
+ "%s #SAEStatus #cacheUpdate Cache already up to date"
+ "%s #SAEStatus #cacheUpdate Fetched deviceSupportsSAE (deprecated): %d"
+ "%s #SAEStatus #cacheUpdate Fetched saeAvailable: %d"
+ "%s #SAEStatus #cacheUpdate Fetched saeEnabled: %d"
+ "%s #SAEStatus #cacheUpdate Fetched swaiEnabled: %d"
+ "%s #SAEStatus #cacheUpdate Fetched visualIntelligenceEnabled: %d"
+ "%s #SAEStatus #cacheUpdate Fetching deviceSupportsSAE (deprecated)"
+ "%s #SAEStatus #cacheUpdate Initializing cache"
+ "%s #SAEStatus #cacheUpdate Posting AFSystemAssistantExperienceAvailabilityDidChangeNotificationName"
+ "%s #SAEStatus #cacheUpdate Received notification %@, updating cache if needed"
+ "%s #SAEStatus #cacheUpdate Updating cache:\ndeviceSupportsSAE: %d->%d\nsaeEnabled: %d->%d\nsaeAvailable: %d->%d\nswaiEnabled: %d->%d\nvisualIntelligenceEnabled: %d->%d"
+ "%s %@ Sampling - Deletion: Deleting all sampling data."
+ "%s %@ Sampling - Deletion: Failed to delete file: %@, error: %@"
+ "%s %@ Sampling - Deletion: Failed to delete sampling cache: %@"
+ "%s %@ Sampling - Deletion: Failed to delete sampling directory: %@"
+ "%s %@ Sampling - Deletion: Successfully deleted file: %@"
+ "%s %@ Sampling - Deletion: Successfully deleted sampling cache: %@"
+ "%s %@ Sampling - Deletion: Successfully deleted sampling directory: %@"
+ "%s %@ Sampling: Failed to create sampling directory (%@), error: %@"
+ "%s %@ Sampling: Failed to resolve attributes for file: %@, error: %@"
+ "%s %@ Sampling: File ineligible for upload as it is only %ld minutes old: %@"
+ "%s %@ Sampling: File is empty: %@"
+ "%s %@ Sampling: No file at path: %@"
+ "%s AFDeviceSupportsDisablingServerFallbackWhenMissingAsset returns true as locale is nil"
+ "%s AFDeviceSupportsDisablingServerFallbackWhenMissingAsset returns true for unsupported server locale: %@"
+ "%s Audio route changed from: %@ to: %@"
+ "%s Creating xpc to deactivate workout voice feedback announcement with feedback identifier: %@"
+ "%s Deferring discovery notification because of active assertions"
+ "%s Failed to serialize workout voice feedback identifier %@: %@"
+ "%s Failed to serialize workoutvoice feedback audio %@: %@"
+ "%s Finished setting CFPreferencesSetAppValue to value: %@ for domain: %@ subdomain: %@ key: %@"
+ "%s Getting localized string for effective key: %@ for locale: %@"
+ "%s Getting localized string for key: %@ for locale: %@"
+ "%s Initializing AVSystemController's subscriptions due to: %@"
+ "%s Listening for '%@' notifications"
+ "%s No language code saved, Returning languageCode: %@"
+ "%s No language code saved, but Assistant is enabled"
+ "%s No longer listening for '%@' notifications"
+ "%s Notify: %d; route changed from %@(%@) to %@(%@)"
+ "%s Posting kAFPreferencesDidChangeDarwinNotification"
+ "%s Posting notification '%@' with SRT stats: %@"
+ "%s Received notification: '%@', with payload: %@"
+ "%s Sending deactivate workout voice feedback xpc message for workout voice feedback identifier: %@"
+ "%s Telling %@ currentAudioRouteDidChangeFrom:%@(%@) to:%@(%@)"
+ "%s Unable to send deactivate request xpc message for workout voice feedback %@"
+ "%s Unexpected nil payload, no-op"
+ "%s Updating route availability due to route change from: %@ to: %@"
+ "%s isMedocSupported = %d, deviceSupportsGenerativeModelSystems = %d, isSAEOverrideEnabled = %d, isNLRouterFeatureEnabled = %d, deviceSupportsSAEByDeviceCapabilityAndFeatureFlags = %d"
+ "%s localeIdentifier cannot be nil."
+ "%s value is nil for  domain: %@ subdomain: %@ key: %@"
+ "%u,"
+ "+[AFSamplingUtilities deleteItemAtFilePath:error:]"
+ "+[AFSiriAnnounceWorkoutVoiceFeedbackRequest deactivateRequestForFeedbackIdentifier:completion:]"
+ "-[AFCheckSRT dealloc]"
+ "-[AFCheckSRT didReceivePluginSelected:]"
+ "-[AFCheckSRT init]"
+ "-[AFCheckSRT trackEvent:forTurn:]"
+ "-[AFLocalization(StringCatalog) localizedStringFromCatalogForKey:gender:table:bundle:languageCode:defaultValue:]"
+ "-[AFSettingsConnection sendSampledAudioToServerIgnoringMinimumSampleAge:completion:]_block_invoke"
+ "-[AFSiriAudioRouteMonitor _broadcastRouteChangeFrom:to:]_block_invoke"
+ "-[AFSiriAudioRouteMonitor _updateAudioRouteAvailabilityAndBroadcast:]"
+ "-[AFSiriAudioRouteMonitor deviceRingerObserver:didChangeState:]_block_invoke"
+ "-[AFSiriAudioRouteMonitor initializeAVSystemControllerSubscriptions:]_block_invoke"
+ "-[AFSiriAudioRouteMonitor updateAudioRouteAvailability:]"
+ "-[AFSiriDataSharingSensitivityManager isOptedOutOfMTE]"
+ "-[AFSiriHeadphonesMonitor _updateAudioRouteFromRoute:toRoute:andBroadcast:]"
+ "-[AFSiriHeadphonesMonitor _updateAudioRouteFromRoute:toRoute:andBroadcast:]_block_invoke"
+ "-[AFSiriHeadphonesMonitor _updateAudioRouteFromRoute:toRoute:andBroadcast:]_block_invoke_2"
+ "-[AFSiriHeadphonesMonitor currentAudioRouteDidChangeFrom:to:]"
+ "-[AFSystemAssistantExperienceStatusManager init]"
+ "@\"AFCheckSRT\""
+ "@\"AFSiriWorkoutVoiceFeedback\""
+ "@64@0:8@16q24@32@40@48@56"
+ "@64@0:8@16{AudioStreamBasicDescription=dIIIIIIII}24"
+ "@72@0:8@16@24@32B40B44@48@56B64B68"
+ "@72@0:8@16@24{AudioStreamBasicDescription=dIIIIIIII}32"
+ "@88@0:8B16B20B24B28B32B36B40B44B48B52B56B60@64B72B76q80"
+ "@92@0:8@16q24B32B36B40B44B48f52@56@64@72@80B88"
+ "@96@0:8@16@24@32@40@48@56B64B68B72B76@80@88"
+ "AFCheckSRT"
+ "AFClientConfiguration::carOwnsMainAudio"
+ "AFCompanionDeviceInfo::companionName"
+ "AFPreferencesOnDeviceLocaleForDictationLocale"
+ "AFPreferencesOnDeviceLocaleForSpellingLocale"
+ "AFSharedUserInfo::isMediaFallbackUser"
+ "AFSiriAudioRouteMonitor"
+ "AFSiriAudioRouteMonitor.m"
+ "AFSiriAudioRouteMonitorDelegate"
+ "AFSiriWorkoutVoiceFeedback"
+ "AppIntent"
+ "B32@0:8d16@24"
+ "FlowPlugin"
+ "HandleSiriCapabilitiesDidChange"
+ "Is user data sync needed for peer ATV"
+ "Is user data sync needed for peer watch"
+ "PluginMeasuringSRT"
+ "REDACTED"
+ "RelatedQuestion"
+ "SRTTime"
+ "SelectedFlowPlugin"
+ "SiriXRequest"
+ "StringCatalog"
+ "T@\"NSData\",R,N,V_feedbackAudioData"
+ "T@\"NSString\",&,N,V_uid"
+ "T@\"NSString\",R,C,N,V_companionName"
+ "T@\"NSString\",R,N,V_feedbackIdentifier"
+ "T@\"NSString\",R,N,V_feedbackText"
+ "TB,N,V_shouldPerformFullPayloadCorrection"
+ "TB,R,N,GisDiagnosticsBridgeFeatureEnabled"
+ "TB,R,N,V_carOwnsMainAudio"
+ "TB,R,N,V_isMediaFallbackUser"
+ "Tq,N,V_suggestionRequestType"
+ "T{AudioStreamBasicDescription=dIIIIIIII},R,N,V_feedbackAudioASBD"
+ "UIUtterances-JS-catalog"
+ "Vv24@0:8@?<v@?@\"SISchemaUUID\"@\"NSError\">16"
+ "_AFPreferencesClearAnnounceNotificationsInCarPlayTemporarilyDisabled"
+ "_AFPreferencesClearAnnounceNotificationsInCarPlayType"
+ "_AFPreferencesClearMessageWithoutConfirmationEnabled"
+ "_AFPreferencesClearMessageWithoutConfirmationHeadphonesEnabled"
+ "_AFPreferencesClearMessageWithoutConfirmationInCarPlayEnabled"
+ "_AFPreferencesClearShowAppsBehindSiriInCarPlayEnabled"
+ "_AFPreferencesClearSiriInCallEnabled"
+ "_AFPreferencesClearSpokenNotificationTemporarilyDisabledStatus"
+ "_AFPreferencesInsertThreadCancellationForApp"
+ "_AFPreferencesRemoveThreadCancellationForApp"
+ "_AFPreferencesRemoveThreadCancellationsOlderThanTimeInterval"
+ "_AFPreferencesSetAnnounceNotificationsInCarPlayTemporarilyDisabled"
+ "_AFPreferencesSetAnnounceNotificationsInCarPlayType"
+ "_AFPreferencesSetAnnounceNotificationsOnBuiltInSpeakerEnabled"
+ "_AFPreferencesSetAnnounceNotificationsOnHearingAidsEnabled"
+ "_AFPreferencesSetAnnounceNotificationsOnHearingAidsSupported"
+ "_AFPreferencesSetAnnounceNotificationsTemporarilyDisabledEndDateForAppOnPlatform"
+ "_AFPreferencesSetAnnounceNotificationsTemporarilyDisabledEndDateForPlatform"
+ "_AFPreferencesSetManagedConfigurationDictationAllowed"
+ "_AFPreferencesSetMessageWithoutConfirmationEnabled"
+ "_AFPreferencesSetMessageWithoutConfirmationHeadphonesEnabled"
+ "_AFPreferencesSetMessageWithoutConfirmationInCarPlayEnabled"
+ "_AFPreferencesSetShowAppsBehindSiriInCarPlayEnabled"
+ "_AFPreferencesSetSiriInCallEnabled"
+ "_AFPreferencesSetSpokenNotificationSkipTriggerlessReplyConfirmation"
+ "_AFPreferencesSetSpokenNotificationsProxCardSeen"
+ "_AFPreferencesSetValueForKeyWithContext"
+ "_FlowPluginSelected"
+ "_audioRouteMonitor"
+ "_broadcastRouteChangeFrom:to:"
+ "_carOwnsMainAudio"
+ "_checkSRT"
+ "_companionName"
+ "_currentTurnID"
+ "_feedbackAudioASBD"
+ "_feedbackAudioData"
+ "_feedbackIdentifier"
+ "_feedbackText"
+ "_isAppleHeadphone"
+ "_isMediaFallbackUser"
+ "_notificationPostAssertions"
+ "_pluginSelected"
+ "_setError"
+ "_shouldPerformFullPayloadCorrection"
+ "_suggestionRequestType"
+ "_uid"
+ "_updateAudioRouteFromRoute:toRoute:andBroadcast:"
+ "_workoutVoiceFeedback"
+ "announcePlatformForRoute = %ld"
+ "availableAnnouncementRequestTypes = %lu"
+ "btAddress = %@"
+ "carOwnsMainAudio"
+ "com.apple.assistant.srt.stats"
+ "companionName"
+ "computedActivationEventMachAbsoluteTime"
+ "connectedBTProductID = %@"
+ "currentAudioRouteDidChangeFrom:to:"
+ "deactivateRequestForFeedbackIdentifier:completion:"
+ "deleteItemAtFilePath:error:"
+ "diagnosticsBridgeFeatureEnabled"
+ "diagnostics_bridge"
+ "didReceivePluginSelected:"
+ "disablePersistentIDLoggingAppleTV"
+ "disablePersistentIDLoggingAppleTVOptOut"
+ "disablePersistentIDLoggingHomePod"
+ "disablePersistentIDLoggingHomePodOptOut"
+ "discoveryNotificationAssertion"
+ "effectiveGenderKeyForKey:gender:"
+ "endWaitingForEmergency"
+ "faceTimeAudioServiceName"
+ "faceTimeServiceName"
+ "feedbackAudioASBD"
+ "feedbackAudioData"
+ "feedbackIdentifier"
+ "feedbackText"
+ "getCarOwnsMainAudio"
+ "getCompanionName"
+ "getIsMediaFallbackUser"
+ "getODDDeviceAggregationId:"
+ "hasAuthenticationCapability = %d"
+ "hasError"
+ "initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:carOwnsMainAudio:"
+ "initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:companionName:"
+ "initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isUserEngagedWithDevice:"
+ "initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:isMediaFallbackUser:"
+ "initWithVoiceFeedbackAudioData:asbd:"
+ "initWithVoiceFeedbackIdentifier:audioData:asbd:"
+ "initWithVoiceFeedbackIdentifier:text:"
+ "initWithVoiceFeedbackText:"
+ "initWithWorkoutVoiceFeedback:"
+ "invalidateDiscoveryNotificationAssertion:"
+ "isDiagnosticsBridgeFeatureEnabled"
+ "isMediaFallbackUser"
+ "isSAEi18nWave2Enabled"
+ "isSiriMUSessionsGuestSessionUpgradeEnabled"
+ "isSyncNeededForAtv"
+ "isSyncNeededForWatch"
+ "isUIUtteranceJSStringCatalogEnabled"
+ "localizedStringForKey:value:table:localizations:"
+ "localizedStringFromCatalogForKey:gender:table:bundle:languageCode:defaultValue:"
+ "localizedStringOrNilFromCatalogForKey:gender:table:bundle:languageCode:defaultValue:"
+ "mu_sessions_guest_session_upgrade"
+ "name = %@"
+ "position"
+ "productID = %@"
+ "sae_enabled_i18n_wave2"
+ "sendSampledAudioToServerIgnoringMinimumSampleAge:completion:"
+ "setCarOwnsMainAudio:"
+ "setCompanionName:"
+ "setIsMediaFallbackUser:"
+ "setPosition:"
+ "setShouldPerformFullPayloadCorrection:"
+ "setSuggestionRequestType:"
+ "setUid:"
+ "settings.changed-quick-type-gesture"
+ "settings.changed-visual-intelligence-camera-control"
+ "shouldPerformFullPayloadCorrection"
+ "suggestionRequestType"
+ "text = REDACTED"
+ "trackEvent:forTurn:"
+ "ui_utterance_string_catalog_enabled"
+ "uid"
+ "uid = %@"
+ "uuid: %@, timestamp: %llu, requestId: %@, turnId: %@, options: %lu, notifyState: %@ text: %@ directAction: %@ handoffOriginDeviceName: %@ handOffData: %@ handoffURL: %@ handoffRequiresUserInteraction ? %d handoffNotification %@ correctedSpeech: %@ startRequest: %@ activationEvent: %@ speechRequestOptions: %@ testRequestOptions: %@ requestCompletionOptions: %@ sharedUserID: %@ confidenceScore: %lu nonspeakerConfidenceScores: %@ SuggestionRequestType: %@"
+ "v32@0:8@\"AFSiriAudioRoute\"16@\"AFSiriAudioRoute\"24"
+ "workout_voice_feedback_identifier"
+ "{AudioStreamBasicDescription=\"mSampleRate\"d\"mFormatID\"I\"mFormatFlags\"I\"mBytesPerPacket\"I\"mFramesPerPacket\"I\"mBytesPerFrame\"I\"mChannelsPerFrame\"I\"mBitsPerChannel\"I\"mReserved\"I}"
+ "{AudioStreamBasicDescription=dIIIIIIII}16@0:8"
+ "{_mutationFlags=\"isDirty\"b1\"hasAccessibilityState\"b1\"hasDeviceRingerSwitchState\"b1\"hasIsDeviceInCarDNDMode\"b1\"hasIsDeviceInStarkMode\"b1\"hasSupportsCarPlayVehicleData\"b1\"hasIsDeviceWatchAuthenticated\"b1\"hasAreAnnouncementRequestsPermittedByPresentationWhileActive\"b1\"hasOutputVolume\"b1\"hasTapToSiriAudioPlaybackRequest\"b1\"hasTwoShotAudioPlaybackRequest\"b1\"hasDeviceSetupFlowBeginDate\"b1\"hasDeviceSetupFlowEndDate\"b1\"hasCarOwnsMainAudio\"b1}"
+ "{_mutationFlags=\"isDirty\"b1\"hasAssistantID\"b1\"hasSpeechID\"b1\"hasIdsIdentifier\"b1\"hasProductPrefix\"b1\"hasAceHost\"b1\"hasSyncMetadata\"b1\"hasSyncMetadataCapability\"b1\"hasPeerToPeerHandoffCapability\"b1\"hasMuxSupportCapability\"b1\"hasMeDevice\"b1\"hasSiriLanguage\"b1\"hasCompanionName\"b1}"
+ "{_mutationFlags=\"isDirty\"b1\"hasIsEyesFree\"b1\"hasIsUIFree\"b1\"hasIsForCarDND\"b1\"hasIsInAmbient\"b1\"hasIsMapsNavigationActive\"b1\"hasIsVoiceTriggerRequest\"b1\"hasIsConnectedToCarPlay\"b1\"hasIsRequestMadeWithPhysicalDeviceInteraction\"b1\"hasIsAudioAccessoryButtonActivation\"b1\"hasIsSiriAutoPrompt\"b1\"hasIsFlexibleFollowup\"b1\"hasUserTypedInSiri\"b1\"hasModeOverrideValue\"b1\"hasIsDeviceUnlocked\"b1\"hasIsDeviceScreenON\"b1\"hasIsUserEngagedWithDevice\"b1}"
+ "{_mutationFlags=\"isDirty\"b1\"hasSharedUserId\"b1\"hasLoggableSharedUserId\"b1\"hasCompanionDeviceInfo\"b1\"hasPersonalRequestsEnabled\"b1\"hasCompanionLinkReady\"b1\"hasHomeUserId\"b1\"hasICloudAltDSID\"b1\"hasIsDeviceOwner\"b1\"hasIsMediaFallbackUser\"b1}"
+ "\xf0\xf0\xe2"
- "%@ {accessibilityState = %@, deviceRingerSwitchState = %@, isDeviceInCarDNDMode = %@, isDeviceInStarkMode = %@, supportsCarPlayVehicleData = %@, isDeviceWatchAuthenticated = %@, areAnnouncementRequestsPermittedByPresentationWhileActive = %@, outputVolume = %f, tapToSiriAudioPlaybackRequest = %@, twoShotAudioPlaybackRequest = %@, deviceSetupFlowBeginDate = %@, deviceSetupFlowEndDate = %@}"
- "%@ {assistantID = %@, speechID = %@, idsIdentifier = %@, productPrefix = %@, aceHost = %@, syncMetadata = %@, syncMetadataCapability = %@, peerToPeerHandoffCapability = %@, muxSupportCapability = %@, meDevice = %@, siriLanguage = %@}"
- "%@ {isDeviceOwnedByCurrentUser = %@, assistantIdentifier = %@, sharedUserIdentifier = %@, idsIdentifier = %@, idsDeviceUniqueIdentifier = %@, rapportEffectiveIdentifier = %@, homeKitAccessoryIdentifier = %@, mediaSystemIdentifier = %@, mediaRouteIdentifier = %@, isCommunalDevice = %@, roomName = %@, name = %@, productType = %@, buildVersion = %@, userInterfaceIdiom = %@, aceVersion = %@, isLocationSharingDevice = %@, isSiriCloudSyncEnabled = %@, trialTreatment = %@}"
- "%@ {isEyesFree = %@, isUIFree = %@, isForCarDND = %@, isInAmbient = %@, isMapsNavigationActive = %@, isVoiceTriggerRequest = %@, isConnectedToCarPlay = %@, isRequestMadeWithPhysicalDeviceInteraction = %@, isAudioAccessoryButtonActivation = %@, isSiriAutoPrompt = %@, isFlexibleFollowup = %@, isMediaPlaying = %@, userTypedInSiri = %@, modeOverrideValue = %@, isDeviceUnlocked = %@, isDeviceScreenON = %@, isInPocket = %@, liftToWakeDetected = %@, userInitiatedWakeDetected = %@, deviceMotion = %@, deviceRaised = %@, faceDetected = %@, touchScreenDetected = %@, buttonPressDetected = %@, flatDevicePosture = %@, deviceOrientation = %@, isInWorkout = %@, isBacklightOn = %@, isInWaterLock = %@, isInSleepLock = %@, isInTheaterMode = %@, isOnWrist = %@, isUserEngagedWithDevice = %@}"
- "%@ {sharedUserId = %@, loggableSharedUserId = %@, companionDeviceInfo = %@, personalRequestsEnabled = %@, companionLinkReady = %@, homeUserId = %@, iCloudAltDSID = %@, isDeviceOwner = %@}"
- "%@, messagesContext=%@, recognizedText=%@ correctedText=%@"
- "%@, sender=%@, messages=%@"
- "%s #MTEOptOut Should drop MTE: %@ with supportsUOD: %@"
- "%s #SAEStatus available from cache:%d"
- "%s #SAEStatus enabled from cache:%d"
- "%s #attention awareness start"
- "%s #attention awareness sync resumeWithError failed: %@"
- "%s #attention sync awareness error: %@"
- "%s #attention sync awareness state event: %@, error: %@"
- "%s #attention sync suspendWithError failed: %@"
- "%s #posting AFSystemAssistantExperienceAvailabilityDidChangeNotificationName"
- "%s #visualIntelligenceStatus from cache:%d"
- "%s #visualIntelligenceStatus:%d"
- "%s %@ Sampling: Deleting all the %@ sampling data"
- "%s %@ Sampling: Done with deleting all the sampling data. Deleted - %@, %@"
- "%s %@ Sampling: Error creating directory %@ - %@"
- "%s %@ Sampling: Error deleting item at %@ - %@"
- "%s %@ Sampling: Error retrieving file attributes: %@"
- "%s %@ Sampling: File at path %@ is empty."
- "%s %@ Sampling: File at path: %@ is ineligible for upload as it is only %ld minutes old."
- "%s %@ Sampling: No attributes for file at path: %@, error: %@"
- "%s %@ Sampling: No file exists at path %@"
- "%s %@ Sampling: Successfully deleted %@"
- "%s Creating xpc to deactivate workout voice feedback announcement"
- "%s Failed to serialize workoutvoice feedback data %@: %@"
- "%s Fetched AFDeviceSupportsSAEDeprecated: %@"
- "%s Fetching AFDeviceSupportsSAEDeprecated"
- "%s No language code saved, but Assistant is enabled - returning: %@"
- "%s SAE available status: %@"
- "%s SAE enabled status: %@"
- "%s SWAI status: %@"
- "%s Sending deactivate workout reminder xpc message for workout voice feedback"
- "%s Unable to send deactivate request xpc message for workout voice feedback"
- "%s deviceSupportsSAE from cache:%d"
- "%s initializing AVSystemController's subscriptions due to: %@"
- "%s isMedocSupported = %d, deviceSupportsGenerativeModelSystems = %d, isSAEOverrideEnabled = %d, isNLRouterEnabled = %d, deviceSupportsSAEByDeviceCapabilityAndFeatureFlags = %d"
- "%s languageCode cannot be nil."
- "%s swaiEnabled from cache:%d"
- "+[AFSamplingUtilities deleteItemAtFilePath:]"
- "+[AFSiriAnnounceWorkoutVoiceFeedbackRequest deactivateOngoingRequestWithCompletion:]"
- "-[AFAttentionAwarenessController requestAttentionStateWithCompletion:]_block_invoke"
- "-[AFSettingsConnection sendSampledAudioToServerWithCompletion:]_block_invoke"
- "-[AFSettingsConnection(Internal) _readSyncTokenForAceHost:completion:]_block_invoke"
- "-[AFSettingsConnection(Internal) _sendSyncTokenToPersonalRequestsEnabledAccessoriesWithCompletion:]_block_invoke"
- "-[AFSettingsConnection(Internal) _setSyncToken:forAceHost:completion:]_block_invoke"
- "-[AFSiriDataSharingSensitivityManager _isOptedOutOfMTEWithSupportsUOD:]"
- "-[AFSiriHeadphonesMonitor _broadcastRouteAndAuthenticationCapability]_block_invoke"
- "-[AFSiriHeadphonesMonitor _updateAudioRouteAvailabilityAndBroadcast:]"
- "-[AFSiriHeadphonesMonitor _updateAudioRouteAvailabilityAndBroadcast:]_block_invoke"
- "-[AFSiriHeadphonesMonitor _updateAudioRouteAvailabilityAndBroadcast:]_block_invoke_2"
- "-[AFSiriHeadphonesMonitor deviceRingerObserver:didChangeState:]_block_invoke"
- "-[AFSiriHeadphonesMonitor initializeAVSystemControllerSubscriptions:]_block_invoke"
- "-[AFSiriHeadphonesMonitor updateAudioRouteAvailability:]"
- "/System/Library/PrivateFrameworks/AttentionAwareness.framework/AttentionAwareness"
- "@\"AWAttentionAwarenessClient\""
- "@148@0:8B16@20@28@36@44@52@60@68@76B84@88@96@104@112@120@128B136@140"
- "@208@0:8B16B20B24B28B32B36B40B44B48B52B56B60B64@68B76B80B84B88B92q96q104q112q120q128q136q144q152q160q168q176q184q192q200"
- "@68@0:8@16@24@32B40B44@48@56B64"
- "@88@0:8@16@24@32@40@48@56B64B68B72B76@80"
- "@88@0:8@16q24B32B36B40B44B48f52@56@64@72@80"
- "AFAttentionAwarenessController"
- "AFAttentionAwarenessController.m"
- "AFModesConfiguration::buttonPressDetected"
- "AFModesConfiguration::deviceMotion"
- "AFModesConfiguration::deviceOrientation"
- "AFModesConfiguration::deviceRaised"
- "AFModesConfiguration::faceDetected"
- "AFModesConfiguration::flatDevicePosture"
- "AFModesConfiguration::isBacklightOn"
- "AFModesConfiguration::isInPocket"
- "AFModesConfiguration::isInSleepLock"
- "AFModesConfiguration::isInTheaterMode"
- "AFModesConfiguration::isInWaterLock"
- "AFModesConfiguration::isInWorkout"
- "AFModesConfiguration::isMediaPlaying"
- "AFModesConfiguration::isOnWrist"
- "AFModesConfiguration::liftToWakeDetected"
- "AFModesConfiguration::touchScreenDetected"
- "AFModesConfiguration::userInitiatedWakeDetected"
- "AWAttentionAwarenessClient"
- "AWAttentionAwarenessConfiguration"
- "AttentionAwarenessLibrary"
- "Enable Database Syncing"
- "FaceTime Audio"
- "Has ATV in the home"
- "MUXReverseSync"
- "TB,R,N,V_isInPocket"
- "TB,R,N,V_isMediaPlaying"
- "TB,R,N,V_liftToWakeDetected"
- "TB,R,N,V_userInitiatedWakeDetected"
- "Tq,R,N,V_buttonPressDetected"
- "Tq,R,N,V_deviceMotion"
- "Tq,R,N,V_deviceOrientation"
- "Tq,R,N,V_deviceRaised"
- "Tq,R,N,V_faceDetected"
- "Tq,R,N,V_flatDevicePosture"
- "Tq,R,N,V_isBacklightOn"
- "Tq,R,N,V_isInSleepLock"
- "Tq,R,N,V_isInTheaterMode"
- "Tq,R,N,V_isInWaterLock"
- "Tq,R,N,V_isInWorkout"
- "Tq,R,N,V_isOnWrist"
- "Tq,R,N,V_touchScreenDetected"
- "Vv48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"AFSyncSnapshot\">40"
- "_AFPreferencesReplacementLanguageForLocalRecognizerLanguageCode"
- "_attentionClient"
- "_attentionQueue"
- "_avAudioRouteName"
- "_broadcastRouteAndAuthenticationCapability"
- "_buttonPressDetected"
- "_deviceMotion"
- "_deviceOrientation"
- "_deviceRaised"
- "_faceDetected"
- "_flatDevicePosture"
- "_isBacklightOn"
- "_isInPocket"
- "_isInSleepLock"
- "_isInTheaterMode"
- "_isInWaterLock"
- "_isInWorkout"
- "_isOnWrist"
- "_isOptedOutOfMTEWithSupportsUOD:"
- "_liftToWakeDetected"
- "_readSyncTokenForAceHost:completion:"
- "_sendSyncTokenToPersonalRequestsEnabledAccessoriesWithCompletion:"
- "_setSyncToken:forAceHost:completion:"
- "_setSyncVerificationNeededAndFullReportNeeded:shouldPostNotification:completion:"
- "_touchScreenDetected"
- "_userInitiatedWakeDetected"
- "buttonPressDetected"
- "classAWAttentionAwarenessClient"
- "classAWAttentionAwarenessConfiguration"
- "com.apple.siri.AFAttentionAwarenessController"
- "com.apple.siri.attention_awareness"
- "databaseSyncEnabled"
- "deactivateOngoingRequestWithCompletion:"
- "deviceHasAtvInHome"
- "deviceMotion"
- "deviceOrientation"
- "deviceRaised"
- "faceDetected"
- "fetchCurrentSyncSnapshotForServicePath:className:key:completion:"
- "flatDevicePosture"
- "getButtonPressDetected"
- "getDeviceMotion"
- "getDeviceOrientation"
- "getDeviceRaised"
- "getFaceDetected"
- "getFlatDevicePosture"
- "getIsBacklightOn"
- "getIsInPocket"
- "getIsInSleepLock"
- "getIsInTheaterMode"
- "getIsInWaterLock"
- "getIsInWorkout"
- "getIsMediaPlaying"
- "getIsOnWrist"
- "getLiftToWakeDetected"
- "getTouchScreenDetected"
- "getUserInitiatedWakeDetected"
- "hints"
- "initAWAttentionAwarenessClient_block_invoke"
- "initAWAttentionAwarenessConfiguration_block_invoke"
- "initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:"
- "initWithAssistantID:speechID:idsIdentifier:productPrefix:aceHost:syncMetadata:syncMetadataCapability:peerToPeerHandoffCapability:muxSupportCapability:meDevice:siriLanguage:"
- "initWithIsDeviceOwnedByCurrentUser:assistantIdentifier:sharedUserIdentifier:idsIdentifier:idsDeviceUniqueIdentifier:rapportEffectiveIdentifier:homeKitAccessoryIdentifier:mediaSystemIdentifier:mediaRouteIdentifier:isCommunalDevice:roomName:name:productType:buildVersion:userInterfaceIdiom:aceVersion:isLocationSharingDevice:myriadTrialTreatment:"
- "initWithIsEyesFree:isUIFree:isForCarDND:isInAmbient:isMapsNavigationActive:isVoiceTriggerRequest:isConnectedToCarPlay:isRequestMadeWithPhysicalDeviceInteraction:isAudioAccessoryButtonActivation:isSiriAutoPrompt:isFlexibleFollowup:isMediaPlaying:userTypedInSiri:modeOverrideValue:isDeviceUnlocked:isDeviceScreenON:isInPocket:liftToWakeDetected:userInitiatedWakeDetected:deviceMotion:deviceRaised:faceDetected:touchScreenDetected:buttonPressDetected:flatDevicePosture:deviceOrientation:isInWorkout:isBacklightOn:isInWaterLock:isInSleepLock:isInTheaterMode:isOnWrist:isUserEngagedWithDevice:"
- "initWithSharedUserId:loggableSharedUserId:companionDeviceInfo:personalRequestsEnabled:companionLinkReady:homeUserId:iCloudAltDSID:isDeviceOwner:"
- "isBacklightOn"
- "isHintsEnabled"
- "isInPocket"
- "isInSleepLock"
- "isInTheaterMode"
- "isInWaterLock"
- "isInWorkout"
- "isOnWrist"
- "liftToWakeDetected"
- "pollForAttentionWithTimeout:event:error:"
- "readSyncTokenForAceHost:completion:"
- "requestAttentionStateWithCompletion:"
- "resumeWithError:"
- "sendSampledAudioToServerWithCompletion:"
- "sendSyncTokenToPersonalRequestsEnabledAccessoriesWithCompletion:"
- "setButtonPressDetected:"
- "setDatabaseSyncEnabled:"
- "setDeviceMotion:"
- "setDeviceOrientation:"
- "setDeviceRaised:"
- "setEventMask:"
- "setFaceDetected:"
- "setFlatDevicePosture:"
- "setIsBacklightOn:"
- "setIsInPocket:"
- "setIsInSleepLock:"
- "setIsInTheaterMode:"
- "setIsInWaterLock:"
- "setIsInWorkout:"
- "setIsOnWrist:"
- "setLiftToWakeDetected:"
- "setSyncToken:forAceHost:completion:"
- "setTouchScreenDetected:"
- "setUserInitiatedWakeDetected:"
- "suspendWithError:"
- "syncVerificationPartialResult:"
- "syncVerificationServerReport:"
- "text = %@"
- "touchScreenDetected"
- "trialTreatment"
- "userInitiatedWakeDetected"
- "uuid: %@, timestamp: %llu, requestId: %@, turnId: %@, options: %lu, notifyState: %@ text: %@ directAction: %@ handoffOriginDeviceName: %@ handOffData: %@ handoffURL: %@ handoffRequiresUserInteraction ? %d handoffNotification %@ correctedSpeech: %@ startRequest: %@ activationEvent: %@ speechRequestOptions: %@ testRequestOptions: %@ requestCompletionOptions: %@ sharedUserID: %@ confidenceScore: %lu nonspeakerConfidenceScores: %@"
- "v32@0:8B16B20@?<v@?@\"NSArray\">24"
- "{_mutationFlags=\"isDirty\"b1\"hasAccessibilityState\"b1\"hasDeviceRingerSwitchState\"b1\"hasIsDeviceInCarDNDMode\"b1\"hasIsDeviceInStarkMode\"b1\"hasSupportsCarPlayVehicleData\"b1\"hasIsDeviceWatchAuthenticated\"b1\"hasAreAnnouncementRequestsPermittedByPresentationWhileActive\"b1\"hasOutputVolume\"b1\"hasTapToSiriAudioPlaybackRequest\"b1\"hasTwoShotAudioPlaybackRequest\"b1\"hasDeviceSetupFlowBeginDate\"b1\"hasDeviceSetupFlowEndDate\"b1}"
- "{_mutationFlags=\"isDirty\"b1\"hasAssistantID\"b1\"hasSpeechID\"b1\"hasIdsIdentifier\"b1\"hasProductPrefix\"b1\"hasAceHost\"b1\"hasSyncMetadata\"b1\"hasSyncMetadataCapability\"b1\"hasPeerToPeerHandoffCapability\"b1\"hasMuxSupportCapability\"b1\"hasMeDevice\"b1\"hasSiriLanguage\"b1}"
- "{_mutationFlags=\"isDirty\"b1\"hasIsEyesFree\"b1\"hasIsUIFree\"b1\"hasIsForCarDND\"b1\"hasIsInAmbient\"b1\"hasIsMapsNavigationActive\"b1\"hasIsVoiceTriggerRequest\"b1\"hasIsConnectedToCarPlay\"b1\"hasIsRequestMadeWithPhysicalDeviceInteraction\"b1\"hasIsAudioAccessoryButtonActivation\"b1\"hasIsSiriAutoPrompt\"b1\"hasIsFlexibleFollowup\"b1\"hasIsMediaPlaying\"b1\"hasUserTypedInSiri\"b1\"hasModeOverrideValue\"b1\"hasIsDeviceUnlocked\"b1\"hasIsDeviceScreenON\"b1\"hasIsInPocket\"b1\"hasLiftToWakeDetected\"b1\"hasUserInitiatedWakeDetected\"b1\"hasDeviceMotion\"b1\"hasDeviceRaised\"b1\"hasFaceDetected\"b1\"hasTouchScreenDetected\"b1\"hasButtonPressDetected\"b1\"hasFlatDevicePosture\"b1\"hasDeviceOrientation\"b1\"hasIsInWorkout\"b1\"hasIsBacklightOn\"b1\"hasIsInWaterLock\"b1\"hasIsInSleepLock\"b1\"hasIsInTheaterMode\"b1\"hasIsOnWrist\"b1\"hasIsUserEngagedWithDevice\"b1}"
- "{_mutationFlags=\"isDirty\"b1\"hasSharedUserId\"b1\"hasLoggableSharedUserId\"b1\"hasCompanionDeviceInfo\"b1\"hasPersonalRequestsEnabled\"b1\"hasCompanionLinkReady\"b1\"hasHomeUserId\"b1\"hasICloudAltDSID\"b1\"hasIsDeviceOwner\"b1}"
- "\xf0\xf0\xd2"

```
