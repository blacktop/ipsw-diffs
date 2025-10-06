## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3301.21.2.1.2
-  __TEXT.__text: 0x18f7b0
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__objc_methlist: 0x1896c
+3302.23.5.1.1
+  __TEXT.__text: 0x193324
+  __TEXT.__auth_stubs: 0x1540
+  __TEXT.__objc_methlist: 0x18c64
   __TEXT.__const: 0x360
-  __TEXT.__gcc_except_tab: 0x1844
-  __TEXT.__cstring: 0x38ee0
-  __TEXT.__oslogstring: 0xf414
+  __TEXT.__gcc_except_tab: 0x18b4
+  __TEXT.__cstring: 0x398ca
+  __TEXT.__oslogstring: 0xf7b8
   __TEXT.__dlopen_cstrs: 0x324
-  __TEXT.__unwind_info: 0x74c4
-  __TEXT.__objc_classname: 0x4bb7
-  __TEXT.__objc_methname: 0x375ce
-  __TEXT.__objc_methtype: 0xa261
-  __TEXT.__objc_stubs: 0x22c40
+  __TEXT.__unwind_info: 0x759c
+  __TEXT.__objc_classname: 0x4c73
+  __TEXT.__objc_methname: 0x37d02
+  __TEXT.__objc_methtype: 0xa483
+  __TEXT.__objc_stubs: 0x22f60
   __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__const: 0x7d38
-  __DATA_CONST.__objc_classlist: 0xd40
+  __DATA_CONST.__const: 0x7e10
+  __DATA_CONST.__objc_classlist: 0xd50
   __DATA_CONST.__objc_catlist: 0x290
-  __DATA_CONST.__objc_protolist: 0x538
+  __DATA_CONST.__objc_protolist: 0x540
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2b3b8
-  __DATA_CONST.__objc_selrefs: 0xb5c8
-  __DATA_CONST.__objc_arraydata: 0x1d10
-  __AUTH_CONST.__cfstring: 0x253c0
-  __AUTH_CONST.__const: 0x3520
-  __AUTH_CONST.__objc_const: 0xc910
-  __AUTH_CONST.__objc_intobj: 0x1f98
-  __AUTH_CONST.__objc_dictobj: 0xa50
+  __DATA_CONST.__objc_const: 0x2b970
+  __DATA_CONST.__objc_selrefs: 0xb6f8
+  __DATA_CONST.__objc_arraydata: 0x1d50
+  __AUTH_CONST.__cfstring: 0x256a0
+  __AUTH_CONST.__const: 0x35e0
+  __AUTH_CONST.__objc_const: 0xc9e8
+  __AUTH_CONST.__objc_intobj: 0x2028
+  __AUTH_CONST.__objc_dictobj: 0xaa0
   __AUTH_CONST.__objc_arrayobj: 0x5a0
   __AUTH_CONST.__objc_doubleobj: 0x30
-  __AUTH_CONST.__auth_got: 0xaa8
-  __AUTH.__objc_data: 0x6fe0
+  __AUTH_CONST.__auth_got: 0xab0
+  __AUTH.__objc_data: 0x7080
   __AUTH.__data: 0x2d8
   __DATA.__objc_protorefs: 0x138
-  __DATA.__objc_classrefs: 0xff8
-  __DATA.__objc_superrefs: 0xd70
-  __DATA.__objc_ivar: 0x23bc
+  __DATA.__objc_classrefs: 0x1018
+  __DATA.__objc_superrefs: 0xd80
+  __DATA.__objc_ivar: 0x240c
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x4690
+  __DATA.__data: 0x46f0
   __DATA.__common: 0x8
-  __DATA.__bss: 0xb18
+  __DATA.__bss: 0xb38
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0xf0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SAObjects.framework/SAObjects
   - /System/Library/PrivateFrameworks/SiriAnalytics.framework/SiriAnalytics
+  - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitration.framework/SiriCrossDeviceArbitration
   - /System/Library/PrivateFrameworks/SiriCrossDeviceArbitrationFeedback.framework/SiriCrossDeviceArbitrationFeedback
   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /System/Library/PrivateFrameworks/SiriTTSService.framework/SiriTTSService

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B26CF556-11C0-3A55-AAA0-44CA5578403A
-  Functions: 11081
-  Symbols:   35561
-  CStrings:  22817
+  UUID: F1EECDD4-32C0-3A47-996C-A3A4F7A70CA9
+  Functions: 11169
+  Symbols:   35822
+  CStrings:  23002
 
Symbols:
+ +[AFBluetoothDeviceBooleanSettingResponse newWithBuilder:]
+ +[AFBluetoothDeviceBooleanSettingResponse supportsSecureCoding]
+ +[AFFeatureFlags(SWEFeatureFlags) isSCDATrialEnabled]
+ +[AFSiriHeadphonesMonitor _getCurrentAudioRoute:]
+ +[AFSiriHeadphonesMonitor getCurrentAudioRoute]
+ +[AFUtilitiesWrapper uodStatusSupportedFull:languageCode:]
+ -[AFBluetoothDeviceBooleanSettingResponse _descriptionWithIndent:]
+ -[AFBluetoothDeviceBooleanSettingResponse copyWithZone:]
+ -[AFBluetoothDeviceBooleanSettingResponse description]
+ -[AFBluetoothDeviceBooleanSettingResponse encodeWithCoder:]
+ -[AFBluetoothDeviceBooleanSettingResponse hash]
+ -[AFBluetoothDeviceBooleanSettingResponse initWithBuilder:]
+ -[AFBluetoothDeviceBooleanSettingResponse initWithCoder:]
+ -[AFBluetoothDeviceBooleanSettingResponse initWithValue:status:]
+ -[AFBluetoothDeviceBooleanSettingResponse init]
+ -[AFBluetoothDeviceBooleanSettingResponse isEqual:]
+ -[AFBluetoothDeviceBooleanSettingResponse status]
+ -[AFBluetoothDeviceBooleanSettingResponse value]
+ -[AFBluetoothDeviceBooleanSettingResponse(AFBluetoothDeviceBooleanSettingResponseMutability) mutatedCopyWithMutator:]
+ -[AFBluetoothDeviceInfo initWithAddress:name:deviceUID:vendorID:productID:isAdvancedAppleAudioDevice:supportsInEarDetection:supportsVoiceTrigger:supportsJustSiri:supportsSpokenNotification:supportsListeningModeANC:supportsListeningModeTransparency:supportsListeningModeAutomatic:supportsConversationAwareness:supportsPersonalVolume:supportsAnnounceCall:]
+ -[AFBluetoothDeviceInfo supportsConversationAwareness]
+ -[AFBluetoothDeviceInfo supportsPersonalVolume]
+ -[AFMyriadGoodnessScoreEvaluator _findSidekickBoost:isSpeaker:model:]
+ -[AFMyriadGoodnessScoreEvaluator _readSidekickBoostsFile:]
+ -[AFMyriadGoodnessScoreEvaluator _reloadTrialConfiguredBoostValues]
+ -[AFMyriadGoodnessScoreEvaluator _setSidekickPlatformBiasForSpeaker:model:]
+ -[AFMyriadGoodnessScoreEvaluator _updateMediaPlaybackBoost:]
+ -[AFMyriadGoodnessScoreEvaluator _updateRecentSiriBoostTrialEnabled:]
+ -[AFMyriadGoodnessScoreEvaluator _updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:]
+ -[AFMyriadGoodnessScoreEvaluator _updateSidekickBoosts:]
+ -[AFMyriadGoodnessScoreEvaluator dealloc]
+ -[AFMyriadGoodnessScoreEvaluator myriadTrialBoostsUpdated:]
+ -[AFPreferences getConversationAwarenessForCurrentlyRoutedDeviceWithCompletion:]
+ -[AFPreferences getPersonalVolumeForCurrentlyRoutedDeviceWithCompletion:]
+ -[AFPreferences isSyncDisabledForFullUoDDevices]
+ -[AFPreferences setConversationAwarenessForCurrentlyRoutedDevice:withCompletion:]
+ -[AFPreferences setPersonalVolumeForCurrentlyRoutedDevice:withCompletion:]
+ -[AFPreferences setServerOverride:]
+ -[AFRequestInfo isATVHandoff]
+ -[AFRequestInfo setIsATVHandoff:]
+ -[AFSettingsConnection getAccessoryInfoForAccessoryWithUUID:completionHandler:]
+ -[AFSettingsConnection getConversationAwarenessForCurrentlyRoutedDevice:]
+ -[AFSettingsConnection getPersonalVolumeForCurrentlyRoutedDevice:]
+ -[AFSettingsConnection getSidekickBoostsFileWithCompletion:]
+ -[AFSettingsConnection getTrialEnables:doubleFactors:withCompletion:]
+ -[AFSettingsConnection pushSCDAAdvertisementContext:completionHandler:]
+ -[AFSettingsConnection setConversationAwarenessForCurrentlyRoutedDevice:withCompletion:]
+ -[AFSettingsConnection setPersonalVolumeForCurrentlyRoutedDevice:withCompletion:]
+ -[AFSettingsConnection(Internal) _isInactiveDeviceSyncDisabled:]
+ -[AFSettingsConnection(Internal) _isInactiveDeviceSyncDisabledByTrial:]
+ -[AFSiriDataSharingSensitivityManager _hasActiveServerSideDictationLanguage:]
+ -[AFSiriDataSharingSensitivityManager _isOptedOutOfMTEWithOptInStatus:locale:activeDictationLanguages:supportsUOD:]
+ -[AFSpeechRequestOptions scdaContext]
+ -[AFSpeechRequestOptions setScdaContext:]
+ -[_AFBluetoothDeviceBooleanSettingResponseMutation .cxx_destruct]
+ -[_AFBluetoothDeviceBooleanSettingResponseMutation getStatus]
+ -[_AFBluetoothDeviceBooleanSettingResponseMutation getValue]
+ -[_AFBluetoothDeviceBooleanSettingResponseMutation initWithBase:]
+ -[_AFBluetoothDeviceBooleanSettingResponseMutation isDirty]
+ -[_AFBluetoothDeviceBooleanSettingResponseMutation setStatus:]
+ -[_AFBluetoothDeviceBooleanSettingResponseMutation setValue:]
+ -[_AFBluetoothDeviceInfoMutation getSupportsConversationAwareness]
+ -[_AFBluetoothDeviceInfoMutation getSupportsPersonalVolume]
+ -[_AFBluetoothDeviceInfoMutation setSupportsConversationAwareness:]
+ -[_AFBluetoothDeviceInfoMutation setSupportsPersonalVolume:]
+ GCC_except_table10159
+ GCC_except_table10600
+ GCC_except_table10613
+ GCC_except_table10863
+ GCC_except_table11005
+ GCC_except_table11022
+ GCC_except_table11024
+ GCC_except_table11027
+ GCC_except_table11029
+ GCC_except_table1526
+ GCC_except_table1532
+ GCC_except_table1535
+ GCC_except_table1600
+ GCC_except_table1669
+ GCC_except_table1922
+ GCC_except_table2124
+ GCC_except_table2589
+ GCC_except_table2596
+ GCC_except_table2600
+ GCC_except_table2602
+ GCC_except_table2639
+ GCC_except_table2653
+ GCC_except_table2657
+ GCC_except_table2661
+ GCC_except_table2664
+ GCC_except_table2666
+ GCC_except_table2671
+ GCC_except_table2673
+ GCC_except_table2677
+ GCC_except_table2689
+ GCC_except_table2692
+ GCC_except_table2706
+ GCC_except_table2708
+ GCC_except_table2710
+ GCC_except_table2712
+ GCC_except_table2774
+ GCC_except_table2828
+ GCC_except_table2858
+ GCC_except_table3202
+ GCC_except_table3325
+ GCC_except_table3344
+ GCC_except_table3350
+ GCC_except_table3355
+ GCC_except_table3356
+ GCC_except_table3359
+ GCC_except_table3365
+ GCC_except_table3453
+ GCC_except_table3455
+ GCC_except_table3472
+ GCC_except_table3478
+ GCC_except_table3520
+ GCC_except_table3532
+ GCC_except_table3602
+ GCC_except_table3703
+ GCC_except_table3710
+ GCC_except_table3724
+ GCC_except_table3751
+ GCC_except_table3837
+ GCC_except_table3891
+ GCC_except_table4255
+ GCC_except_table4258
+ GCC_except_table4259
+ GCC_except_table4580
+ GCC_except_table4642
+ GCC_except_table4647
+ GCC_except_table4658
+ GCC_except_table4670
+ GCC_except_table4785
+ GCC_except_table5231
+ GCC_except_table5237
+ GCC_except_table5243
+ GCC_except_table5279
+ GCC_except_table5281
+ GCC_except_table5294
+ GCC_except_table5314
+ GCC_except_table5317
+ GCC_except_table5330
+ GCC_except_table5331
+ GCC_except_table5332
+ GCC_except_table5333
+ GCC_except_table5355
+ GCC_except_table5358
+ GCC_except_table5451
+ GCC_except_table5567
+ GCC_except_table5659
+ GCC_except_table5665
+ GCC_except_table5771
+ GCC_except_table5778
+ GCC_except_table6111
+ GCC_except_table6126
+ GCC_except_table6157
+ GCC_except_table6259
+ GCC_except_table6268
+ GCC_except_table6307
+ GCC_except_table7123
+ GCC_except_table7129
+ GCC_except_table7299
+ GCC_except_table7397
+ GCC_except_table7427
+ GCC_except_table7628
+ GCC_except_table7633
+ GCC_except_table7697
+ GCC_except_table7803
+ GCC_except_table8181
+ GCC_except_table8235
+ GCC_except_table8279
+ GCC_except_table8367
+ GCC_except_table8407
+ GCC_except_table8438
+ GCC_except_table8443
+ GCC_except_table8444
+ GCC_except_table8448
+ GCC_except_table8688
+ GCC_except_table8753
+ GCC_except_table8759
+ GCC_except_table8794
+ GCC_except_table8797
+ GCC_except_table8869
+ GCC_except_table8898
+ GCC_except_table8970
+ GCC_except_table8977
+ GCC_except_table9087
+ GCC_except_table9091
+ GCC_except_table9095
+ GCC_except_table9128
+ GCC_except_table9173
+ GCC_except_table9609
+ GCC_except_table9611
+ GCC_except_table9614
+ GCC_except_table9623
+ GCC_except_table9649
+ GCC_except_table9670
+ GCC_except_table9822
+ _AFBluetoothDeviceBooleanSettingResponseKey
+ _AFBluetoothDeviceSettingBooleanValueGetFromName
+ _AFBluetoothDeviceSettingBooleanValueGetFromName.map
+ _AFBluetoothDeviceSettingBooleanValueGetFromName.onceToken
+ _AFBluetoothDeviceSettingBooleanValueGetIsValid
+ _AFBluetoothDeviceSettingBooleanValueGetIsValidAndSpecified
+ _AFBluetoothDeviceSettingBooleanValueGetName
+ _AFBluetoothDeviceSettingResponseStatusGetFromName
+ _AFBluetoothDeviceSettingResponseStatusGetFromName.map
+ _AFBluetoothDeviceSettingResponseStatusGetFromName.onceToken
+ _AFBluetoothDeviceSettingResponseStatusGetIsValid
+ _AFBluetoothDeviceSettingResponseStatusGetIsValidAndSpecified
+ _AFBluetoothDeviceSettingResponseStatusGetName
+ _AFMyriadGoodnessComputeExponentialBoost
+ _AFMyriadTrialBoostsUpdatedNotification
+ _AnnounceLibrary.sLib.41519
+ _AnnounceLibrary.sOnce.41517
+ _BluetoothManagerLibrary.43515
+ _BluetoothManagerLibraryCore.frameworkLibrary.19392
+ _CoreServicesLibrary.frameworkLibrary.44112
+ _CoreSpeechLibrary.frameworkLibrary.37466
+ _DataCollectionServicesLibrary.sLib.44126
+ _DataCollectionServicesLibrary.sOnce.44125
+ _IntentsLibrary.14732
+ _IntentsLibraryCore.frameworkLibrary.14736
+ _IntentsLibraryCore.frameworkLibrary.29726
+ _LSApplicationProxyFunction.32895
+ _LSApplicationProxyFunction.44118
+ _MediaExperienceLibrary.26125
+ _MediaExperienceLibraryCore.frameworkLibrary.26152
+ _OBJC_CLASS_$_AFBluetoothDeviceBooleanSettingResponse
+ _OBJC_CLASS_$_SCDAContext
+ _OBJC_CLASS_$_SCDACoordinator
+ _OBJC_CLASS_$__AFBluetoothDeviceBooleanSettingResponseMutation
+ _OBJC_IVAR_$_AFBluetoothDeviceBooleanSettingResponse._status
+ _OBJC_IVAR_$_AFBluetoothDeviceBooleanSettingResponse._value
+ _OBJC_IVAR_$_AFBluetoothDeviceInfo._supportsConversationAwareness
+ _OBJC_IVAR_$_AFBluetoothDeviceInfo._supportsPersonalVolume
+ _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._endpointModelName
+ _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._isExponentialBoostDefined
+ _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._isRecentSiriBoostTrialEnabled
+ _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._isSpeakerEndpoint
+ _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._mediaPlaybackBoost
+ _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._recentSiriFirstDegreeCoefficient
+ _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._recentSiriIntercept
+ _OBJC_IVAR_$_AFMyriadGoodnessScoreEvaluator._recentSiriSecondDegreeCoefficient
+ _OBJC_IVAR_$_AFRequestInfo._isATVHandoff
+ _OBJC_IVAR_$_AFSpeechRequestOptions._scdaContext
+ _OBJC_IVAR_$__AFBluetoothDeviceBooleanSettingResponseMutation._base
+ _OBJC_IVAR_$__AFBluetoothDeviceBooleanSettingResponseMutation._mutationFlags
+ _OBJC_IVAR_$__AFBluetoothDeviceBooleanSettingResponseMutation._status
+ _OBJC_IVAR_$__AFBluetoothDeviceBooleanSettingResponseMutation._value
+ _OBJC_IVAR_$__AFBluetoothDeviceInfoMutation._supportsConversationAwareness
+ _OBJC_IVAR_$__AFBluetoothDeviceInfoMutation._supportsPersonalVolume
+ _OBJC_METACLASS_$_AFBluetoothDeviceBooleanSettingResponse
+ _OBJC_METACLASS_$__AFBluetoothDeviceBooleanSettingResponseMutation
+ _VTPreferencesFunction.44296
+ _VoiceTriggerLibrary.frameworkLibrary.44290
+ __DKEventQueryFunction.20560
+ __DKKnowledgeStoreFunction.20598
+ __DKQueryFunction.20572
+ __DKSystemEventStreamsFunction.20582
+ __OBJC_$_CLASS_METHODS_AFBluetoothDeviceBooleanSettingResponse(AFBluetoothDeviceBooleanSettingResponseMutability)
+ __OBJC_$_CLASS_PROP_LIST_AFBluetoothDeviceBooleanSettingResponse
+ __OBJC_$_INSTANCE_METHODS_AFBluetoothDeviceBooleanSettingResponse(AFBluetoothDeviceBooleanSettingResponseMutability)
+ __OBJC_$_INSTANCE_METHODS__AFBluetoothDeviceBooleanSettingResponseMutation
+ __OBJC_$_INSTANCE_VARIABLES_AFBluetoothDeviceBooleanSettingResponse
+ __OBJC_$_INSTANCE_VARIABLES__AFBluetoothDeviceBooleanSettingResponseMutation
+ __OBJC_$_PROP_LIST_AFBluetoothDeviceBooleanSettingResponse
+ __OBJC_$_PROP_LIST__AFBluetoothDeviceBooleanSettingResponseMutation
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AFBluetoothDeviceBooleanSettingResponseMutating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AFBluetoothDeviceBooleanSettingResponseMutating
+ __OBJC_$_PROTOCOL_REFS_AFBluetoothDeviceBooleanSettingResponseMutating
+ __OBJC_CLASS_PROTOCOLS_$_AFBluetoothDeviceBooleanSettingResponse
+ __OBJC_CLASS_PROTOCOLS_$__AFBluetoothDeviceBooleanSettingResponseMutation
+ __OBJC_CLASS_RO_$_AFBluetoothDeviceBooleanSettingResponse
+ __OBJC_CLASS_RO_$__AFBluetoothDeviceBooleanSettingResponseMutation
+ __OBJC_LABEL_PROTOCOL_$_AFBluetoothDeviceBooleanSettingResponseMutating
+ __OBJC_METACLASS_RO_$_AFBluetoothDeviceBooleanSettingResponse
+ __OBJC_METACLASS_RO_$__AFBluetoothDeviceBooleanSettingResponseMutation
+ __OBJC_PROTOCOL_$_AFBluetoothDeviceBooleanSettingResponseMutating
+ ___354-[AFBluetoothDeviceInfo initWithAddress:name:deviceUID:vendorID:productID:isAdvancedAppleAudioDevice:supportsInEarDetection:supportsVoiceTrigger:supportsJustSiri:supportsSpokenNotification:supportsListeningModeANC:supportsListeningModeTransparency:supportsListeningModeAutomatic:supportsConversationAwareness:supportsPersonalVolume:supportsAnnounceCall:]_block_invoke
+ ___38-[AFConnection _startRequestWithInfo:]_block_invoke.313
+ ___38-[AFConnection _startRequestWithInfo:]_block_invoke.318
+ ___38-[AFConnection _startRequestWithInfo:]_block_invoke_2.314
+ ___43-[AFSettingsConnection dumpAssistantState:]_block_invoke.220
+ ___44-[AFSettingsConnection currectNWActivityId:]_block_invoke.134
+ ___47-[AFSettingsConnection startUIRequestWithInfo:]_block_invoke.155
+ ___47-[AFSettingsConnection startUIRequestWithText:]_block_invoke.150
+ ___48-[AFSettingsConnection siriDesignModeIsEnabled:]_block_invoke.217
+ ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke.336
+ ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke_2.337
+ ___57-[AFSettingsConnection setIsHomePodInHH2Mode:completion:]_block_invoke.211
+ ___58-[AFConnection acquireAudioSessionWithContext:completion:]_block_invoke.299
+ ___59-[AFMyriadGoodnessScoreEvaluator myriadTrialBoostsUpdated:]_block_invoke
+ ___60-[AFSettingsConnection getSidekickBoostsFileWithCompletion:]_block_invoke
+ ___60-[AFSettingsConnection multiUserCompanionDeviceIdentifiers:]_block_invoke.201
+ ___60-[AFSettingsConnection setSiriDesignModeEnabled:completion:]_block_invoke.216
+ ___60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.518
+ ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.286
+ ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.293
+ ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke_2.297
+ ___62-[AFSettingsConnection getCurrentAccessoryInfoWithCompletion:]_block_invoke.141
+ ___62-[AFSettingsConnection getPersonalMultiUserDeviceIdentifiers:]_block_invoke.200
+ ___64-[AFBluetoothDeviceBooleanSettingResponse initWithValue:status:]_block_invoke
+ ___64-[AFConnectionClientServiceDelegate requestHandleCommand:reply:]_block_invoke.720
+ ___64-[AFSettingsConnection shouldSuppressSiriDataSharingOptInAlert:]_block_invoke.214
+ ___64-[AFSettingsConnection(Internal) _isInactiveDeviceSyncDisabled:]_block_invoke
+ ___65-[AFSettingsConnection setSiriDataSharingOptInStatus:completion:]_block_invoke.206
+ ___66-[AFSettingsConnection getPersonalVolumeForCurrentlyRoutedDevice:]_block_invoke
+ ___67-[AFMyriadGoodnessScoreEvaluator _reloadTrialConfiguredBoostValues]_block_invoke
+ ___68-[AFSettingsConnection deleteSiriHistoryWithContext:withCompletion:]_block_invoke.215
+ ___68-[AFSettingsConnection getSiriDataSharingOptInStatusWithCompletion:]_block_invoke.207
+ ___69-[AFSettingsConnection getTrialEnables:doubleFactors:withCompletion:]_block_invoke
+ ___70-[AFSettingsConnection(Internal) _setSyncToken:forAceHost:completion:]_block_invoke.520
+ ___71-[AFSettingsConnection pushSCDAAdvertisementContext:completionHandler:]_block_invoke
+ ___71-[AFSettingsConnection(Internal) _isInactiveDeviceSyncDisabledByTrial:]_block_invoke
+ ___73-[AFPreferences getPersonalVolumeForCurrentlyRoutedDeviceWithCompletion:]_block_invoke
+ ___73-[AFSettingsConnection getConversationAwarenessForCurrentlyRoutedDevice:]_block_invoke
+ ___73-[AFSettingsConnection setSiriDataSharingOptInAlertPresented:completion:]_block_invoke.209
+ ___74-[AFPreferences setPersonalVolumeForCurrentlyRoutedDevice:withCompletion:]_block_invoke
+ ___77-[AFSettingsConnection _createRadarWithReason:room:process:crash:completion:]_block_invoke.228
+ ___79-[AFSettingsConnection getAccessoryInfoForAccessoryWithUUID:completionHandler:]_block_invoke
+ ___79-[AFSettingsConnection setSiriDataSharingHomePodSetupDeviceIsValid:completion:]_block_invoke.210
+ ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke.334
+ ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke_2.335
+ ___80-[AFPreferences getConversationAwarenessForCurrentlyRoutedDeviceWithCompletion:]_block_invoke
+ ___81-[AFPreferences setConversationAwarenessForCurrentlyRoutedDevice:withCompletion:]_block_invoke
+ ___81-[AFSettingsConnection setPersonalVolumeForCurrentlyRoutedDevice:withCompletion:]_block_invoke
+ ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.331
+ ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.333
+ ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke_2.332
+ ___88-[AFSettingsConnection setConversationAwarenessForCurrentlyRoutedDevice:withCompletion:]_block_invoke
+ ___99-[AFSettingsConnection(Internal) _sendSyncTokenToPersonalRequestsEnabledAccessoriesWithCompletion:]_block_invoke.521
+ ___AFBluetoothDeviceSettingBooleanValueGetFromName_block_invoke
+ ___AFBluetoothDeviceSettingResponseStatusGetFromName_block_invoke
+ ___AFSiriActivationPerform_block_invoke.46
+ ___AnnounceLibrary_block_invoke.41523
+ ___Block_byref_object_copy_.10547
+ ___Block_byref_object_copy_.11175
+ ___Block_byref_object_copy_.11730
+ ___Block_byref_object_copy_.12972
+ ___Block_byref_object_copy_.13241
+ ___Block_byref_object_copy_.16500
+ ___Block_byref_object_copy_.16956
+ ___Block_byref_object_copy_.19084
+ ___Block_byref_object_copy_.19407
+ ___Block_byref_object_copy_.21357
+ ___Block_byref_object_copy_.21996
+ ___Block_byref_object_copy_.22405
+ ___Block_byref_object_copy_.27600
+ ___Block_byref_object_copy_.29309
+ ___Block_byref_object_copy_.33320
+ ___Block_byref_object_copy_.33734
+ ___Block_byref_object_copy_.35871
+ ___Block_byref_object_copy_.37079
+ ___Block_byref_object_copy_.40164
+ ___Block_byref_object_copy_.44232
+ ___Block_byref_object_copy_.45404
+ ___Block_byref_object_copy_.46114
+ ___Block_byref_object_copy_.46399
+ ___Block_byref_object_copy_.5297
+ ___Block_byref_object_copy_.7700
+ ___Block_byref_object_copy_.9657
+ ___Block_byref_object_dispose_.10548
+ ___Block_byref_object_dispose_.11176
+ ___Block_byref_object_dispose_.11731
+ ___Block_byref_object_dispose_.12973
+ ___Block_byref_object_dispose_.13242
+ ___Block_byref_object_dispose_.16501
+ ___Block_byref_object_dispose_.16957
+ ___Block_byref_object_dispose_.19085
+ ___Block_byref_object_dispose_.19408
+ ___Block_byref_object_dispose_.21358
+ ___Block_byref_object_dispose_.21997
+ ___Block_byref_object_dispose_.22406
+ ___Block_byref_object_dispose_.27601
+ ___Block_byref_object_dispose_.29310
+ ___Block_byref_object_dispose_.33321
+ ___Block_byref_object_dispose_.33735
+ ___Block_byref_object_dispose_.35872
+ ___Block_byref_object_dispose_.37080
+ ___Block_byref_object_dispose_.40165
+ ___Block_byref_object_dispose_.44233
+ ___Block_byref_object_dispose_.45405
+ ___Block_byref_object_dispose_.46115
+ ___Block_byref_object_dispose_.46400
+ ___Block_byref_object_dispose_.5298
+ ___Block_byref_object_dispose_.7701
+ ___Block_byref_object_dispose_.9658
+ ___BluetoothManagerLibraryCore_block_invoke.19393
+ ___DataCollectionServicesLibrary_block_invoke.44129
+ ___IntentsLibraryCore_block_invoke.14737
+ ___IntentsLibraryCore_block_invoke.29727
+ ___MediaExperienceLibraryCore_block_invoke.26153
+ ___block_descriptor_48_e59_v16?0"<AFBluetoothDeviceBooleanSettingResponseMutating>"8l
+ ___block_descriptor_48_e8_32bs40r_e49_v16?0"AFBluetoothDeviceBooleanSettingResponse"8ls32l8r40l8
+ ___block_descriptor_48_e8_32r40w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw40l8r32l8
+ ___block_descriptor_75_e8_32s40s48s_e41_v16?0"<AFBluetoothDeviceInfoMutating>"8ls32l8s40l8s48l8
+ ___block_literal_global.100.1987
+ ___block_literal_global.10090
+ ___block_literal_global.101.37191
+ ___block_literal_global.10148
+ ___block_literal_global.10298
+ ___block_literal_global.10354
+ ___block_literal_global.104.37185
+ ___block_literal_global.10851
+ ___block_literal_global.109.21464
+ ___block_literal_global.1100
+ ___block_literal_global.111.21461
+ ___block_literal_global.112.20552
+ ___block_literal_global.1129
+ ___block_literal_global.1131
+ ___block_literal_global.1133
+ ___block_literal_global.11384
+ ___block_literal_global.11463
+ ___block_literal_global.1149
+ ___block_literal_global.11490
+ ___block_literal_global.115.21455
+ ___block_literal_global.11552
+ ___block_literal_global.117.32025
+ ___block_literal_global.11750
+ ___block_literal_global.118.43606
+ ___block_literal_global.119.21450
+ ___block_literal_global.120.32080
+ ___block_literal_global.12005
+ ___block_literal_global.12045
+ ___block_literal_global.123.21445
+ ___block_literal_global.12534
+ ___block_literal_global.12677
+ ___block_literal_global.127.21440
+ ___block_literal_global.129.21437
+ ___block_literal_global.1301
+ ___block_literal_global.131.32077
+ ___block_literal_global.133
+ ___block_literal_global.13388
+ ___block_literal_global.135.41518
+ ___block_literal_global.13578
+ ___block_literal_global.13735
+ ___block_literal_global.1376
+ ___block_literal_global.138.41532
+ ___block_literal_global.140.32060
+ ___block_literal_global.14054
+ ___block_literal_global.14162
+ ___block_literal_global.143.32030
+ ___block_literal_global.144.41528
+ ___block_literal_global.149.32042
+ ___block_literal_global.149.37459
+ ___block_literal_global.15.22006
+ ___block_literal_global.15.44907
+ ___block_literal_global.150.43657
+ ___block_literal_global.152.32054
+ ___block_literal_global.153.43719
+ ___block_literal_global.154
+ ___block_literal_global.15571
+ ___block_literal_global.1577
+ ___block_literal_global.161.32049
+ ___block_literal_global.16165
+ ___block_literal_global.16333
+ ___block_literal_global.16544
+ ___block_literal_global.167.32040
+ ___block_literal_global.16949
+ ___block_literal_global.177.39774
+ ___block_literal_global.179.43746
+ ___block_literal_global.17963
+ ___block_literal_global.17982
+ ___block_literal_global.1801
+ ___block_literal_global.181
+ ___block_literal_global.183
+ ___block_literal_global.18327
+ ___block_literal_global.18469
+ ___block_literal_global.185
+ ___block_literal_global.18509
+ ___block_literal_global.18541
+ ___block_literal_global.187
+ ___block_literal_global.1884
+ ___block_literal_global.1887
+ ___block_literal_global.18953
+ ___block_literal_global.190
+ ___block_literal_global.19028
+ ___block_literal_global.19086
+ ___block_literal_global.1934
+ ___block_literal_global.194
+ ___block_literal_global.1944
+ ___block_literal_global.19458
+ ___block_literal_global.1953
+ ___block_literal_global.196
+ ___block_literal_global.19822
+ ___block_literal_global.19889
+ ___block_literal_global.199
+ ___block_literal_global.1992
+ ___block_literal_global.1997
+ ___block_literal_global.19991
+ ___block_literal_global.20.43574
+ ___block_literal_global.2009
+ ___block_literal_global.20116
+ ___block_literal_global.20146
+ ___block_literal_global.20590
+ ___block_literal_global.2092
+ ___block_literal_global.213
+ ___block_literal_global.21530
+ ___block_literal_global.219
+ ___block_literal_global.22014
+ ___block_literal_global.22456
+ ___block_literal_global.22480
+ ___block_literal_global.22560
+ ___block_literal_global.22937
+ ___block_literal_global.23114
+ ___block_literal_global.24432
+ ___block_literal_global.250
+ ___block_literal_global.25180
+ ___block_literal_global.25207
+ ___block_literal_global.253
+ ___block_literal_global.25345
+ ___block_literal_global.2546
+ ___block_literal_global.25541
+ ___block_literal_global.25711
+ ___block_literal_global.25970
+ ___block_literal_global.26.10364
+ ___block_literal_global.26182
+ ___block_literal_global.27008
+ ___block_literal_global.274
+ ___block_literal_global.27557
+ ___block_literal_global.27636
+ ___block_literal_global.27730
+ ___block_literal_global.280
+ ___block_literal_global.28048
+ ___block_literal_global.2808
+ ___block_literal_global.28098
+ ___block_literal_global.28152
+ ___block_literal_global.28794
+ ___block_literal_global.289.13243
+ ___block_literal_global.28920
+ ___block_literal_global.29.10355
+ ___block_literal_global.2901
+ ___block_literal_global.29019
+ ___block_literal_global.29062
+ ___block_literal_global.29869
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.31624
+ ___block_literal_global.3205
+ ___block_literal_global.32083
+ ___block_literal_global.32218
+ ___block_literal_global.3271
+ ___block_literal_global.32888
+ ___block_literal_global.3296
+ ___block_literal_global.33479
+ ___block_literal_global.33747
+ ___block_literal_global.33819
+ ___block_literal_global.35810
+ ___block_literal_global.35887
+ ___block_literal_global.36764
+ ___block_literal_global.36791
+ ___block_literal_global.36899
+ ___block_literal_global.36964
+ ___block_literal_global.37198
+ ___block_literal_global.37392
+ ___block_literal_global.37846
+ ___block_literal_global.37897
+ ___block_literal_global.38.21518
+ ___block_literal_global.38829
+ ___block_literal_global.38863
+ ___block_literal_global.39135
+ ___block_literal_global.39356
+ ___block_literal_global.39770
+ ___block_literal_global.39981
+ ___block_literal_global.40.21512
+ ___block_literal_global.40191
+ ___block_literal_global.40311
+ ___block_literal_global.41294
+ ___block_literal_global.41346
+ ___block_literal_global.414
+ ___block_literal_global.41539
+ ___block_literal_global.417
+ ___block_literal_global.41988
+ ___block_literal_global.42.21509
+ ___block_literal_global.420
+ ___block_literal_global.42260
+ ___block_literal_global.42346
+ ___block_literal_global.43558
+ ___block_literal_global.4404
+ ___block_literal_global.44573
+ ___block_literal_global.44599
+ ___block_literal_global.44753
+ ___block_literal_global.44901
+ ___block_literal_global.45.25719
+ ___block_literal_global.45423
+ ___block_literal_global.4581
+ ___block_literal_global.46070
+ ___block_literal_global.46419
+ ___block_literal_global.48.25720
+ ___block_literal_global.489
+ ___block_literal_global.492
+ ___block_literal_global.5.46405
+ ___block_literal_global.504
+ ___block_literal_global.509
+ ___block_literal_global.511
+ ___block_literal_global.513
+ ___block_literal_global.517
+ ___block_literal_global.518
+ ___block_literal_global.537
+ ___block_literal_global.5452
+ ___block_literal_global.5623
+ ___block_literal_global.5682
+ ___block_literal_global.586
+ ___block_literal_global.59.43589
+ ___block_literal_global.60.22930
+ ___block_literal_global.60.33749
+ ___block_literal_global.64.43594
+ ___block_literal_global.65.21495
+ ___block_literal_global.6689
+ ___block_literal_global.67.19078
+ ___block_literal_global.6760
+ ___block_literal_global.689
+ ___block_literal_global.698
+ ___block_literal_global.70.33754
+ ___block_literal_global.705
+ ___block_literal_global.71.28982
+ ___block_literal_global.713
+ ___block_literal_global.725
+ ___block_literal_global.728
+ ___block_literal_global.73.21490
+ ___block_literal_global.73.33755
+ ___block_literal_global.739
+ ___block_literal_global.75.21487
+ ___block_literal_global.769
+ ___block_literal_global.781
+ ___block_literal_global.790
+ ___block_literal_global.792
+ ___block_literal_global.7993
+ ___block_literal_global.8055
+ ___block_literal_global.812
+ ___block_literal_global.8149
+ ___block_literal_global.8198
+ ___block_literal_global.820
+ ___block_literal_global.83.41411
+ ___block_literal_global.85.25714
+ ___block_literal_global.856
+ ___block_literal_global.859
+ ___block_literal_global.863
+ ___block_literal_global.867
+ ___block_literal_global.8704
+ ___block_literal_global.874
+ ___block_literal_global.890
+ ___block_literal_global.9.43563
+ ___block_literal_global.915
+ ___block_literal_global.92.37187
+ ___block_literal_global.922
+ ___block_literal_global.926
+ ___block_literal_global.929
+ ___block_literal_global.936
+ ___block_literal_global.941
+ ___block_literal_global.944
+ ___block_literal_global.9442
+ ___block_literal_global.95.37195
+ ___getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.14741
+ ___getINSendMessageIntentIdentifierSymbolLoc_block_invoke.14731
+ ___initLSApplicationProxy_block_invoke.32892
+ ___initLSApplicationProxy_block_invoke.44111
+ ___initVTPreferences_block_invoke.44289
+ ___init_DKEventQuery_block_invoke.20556
+ ___init_DKKnowledgeStore_block_invoke.20594
+ ___init_DKQuery_block_invoke.20568
+ ___init_DKSystemEventStreams_block_invoke.20578
+ __unnamed_array_storage.10094
+ __unnamed_array_storage.10152
+ __unnamed_array_storage.10855
+ __unnamed_array_storage.11467
+ __unnamed_array_storage.11556
+ __unnamed_array_storage.12009
+ __unnamed_array_storage.12049
+ __unnamed_array_storage.12538
+ __unnamed_array_storage.13739
+ __unnamed_array_storage.1380
+ __unnamed_array_storage.14.13740
+ __unnamed_array_storage.14.18546
+ __unnamed_array_storage.14.25212
+ __unnamed_array_storage.14.28799
+ __unnamed_array_storage.14.36796
+ __unnamed_array_storage.14.36969
+ __unnamed_array_storage.14.39361
+ __unnamed_array_storage.14.4586
+ __unnamed_array_storage.14.46075
+ __unnamed_array_storage.14.7998
+ __unnamed_array_storage.14.8060
+ __unnamed_array_storage.14450
+ __unnamed_array_storage.1581
+ __unnamed_array_storage.17986
+ __unnamed_array_storage.1803
+ __unnamed_array_storage.1806
+ __unnamed_array_storage.1809
+ __unnamed_array_storage.1812
+ __unnamed_array_storage.18545
+ __unnamed_array_storage.1872
+ __unnamed_array_storage.18957
+ __unnamed_array_storage.19.12050
+ __unnamed_array_storage.19.22485
+ __unnamed_array_storage.19.25185
+ __unnamed_array_storage.19.27013
+ __unnamed_array_storage.19.2813
+ __unnamed_array_storage.19.3301
+ __unnamed_array_storage.19.36769
+ __unnamed_array_storage.19.38834
+ __unnamed_array_storage.19.42265
+ __unnamed_array_storage.19033
+ __unnamed_array_storage.1982
+ __unnamed_array_storage.20150
+ __unnamed_array_storage.22484
+ __unnamed_array_storage.22564
+ __unnamed_array_storage.23.44578
+ __unnamed_array_storage.23102
+ __unnamed_array_storage.24.10095
+ __unnamed_array_storage.24.23118
+ __unnamed_array_storage.24.24437
+ __unnamed_array_storage.24.26187
+ __unnamed_array_storage.24.28053
+ __unnamed_array_storage.24.32223
+ __unnamed_array_storage.24.37851
+ __unnamed_array_storage.24436
+ __unnamed_array_storage.25184
+ __unnamed_array_storage.25211
+ __unnamed_array_storage.25545
+ __unnamed_array_storage.25974
+ __unnamed_array_storage.26186
+ __unnamed_array_storage.27012
+ __unnamed_array_storage.27561
+ __unnamed_array_storage.27640
+ __unnamed_array_storage.28052
+ __unnamed_array_storage.2812
+ __unnamed_array_storage.28156
+ __unnamed_array_storage.28798
+ __unnamed_array_storage.29.25975
+ __unnamed_array_storage.29.38868
+ __unnamed_array_storage.29066
+ __unnamed_array_storage.29706
+ __unnamed_array_storage.3.17987
+ __unnamed_array_storage.3.27562
+ __unnamed_array_storage.3.33484
+ __unnamed_array_storage.3.44604
+ __unnamed_array_storage.32222
+ __unnamed_array_storage.3275
+ __unnamed_array_storage.3300
+ __unnamed_array_storage.33483
+ __unnamed_array_storage.33823
+ __unnamed_array_storage.34.20151
+ __unnamed_array_storage.36768
+ __unnamed_array_storage.36795
+ __unnamed_array_storage.36968
+ __unnamed_array_storage.37850
+ __unnamed_array_storage.37901
+ __unnamed_array_storage.38833
+ __unnamed_array_storage.38867
+ __unnamed_array_storage.39139
+ __unnamed_array_storage.39360
+ __unnamed_array_storage.40195
+ __unnamed_array_storage.41992
+ __unnamed_array_storage.42264
+ __unnamed_array_storage.42350
+ __unnamed_array_storage.425
+ __unnamed_array_storage.44.12010
+ __unnamed_array_storage.44.12539
+ __unnamed_array_storage.44.39140
+ __unnamed_array_storage.44008
+ __unnamed_array_storage.44577
+ __unnamed_array_storage.44603
+ __unnamed_array_storage.4585
+ __unnamed_array_storage.46074
+ __unnamed_array_storage.469
+ __unnamed_array_storage.474
+ __unnamed_array_storage.475
+ __unnamed_array_storage.49.11557
+ __unnamed_array_storage.49.29067
+ __unnamed_array_storage.54.37902
+ __unnamed_array_storage.621
+ __unnamed_array_storage.650.44146
+ __unnamed_array_storage.659
+ __unnamed_array_storage.674.44193
+ __unnamed_array_storage.6764
+ __unnamed_array_storage.728
+ __unnamed_array_storage.730
+ __unnamed_array_storage.731
+ __unnamed_array_storage.762
+ __unnamed_array_storage.765
+ __unnamed_array_storage.766
+ __unnamed_array_storage.777
+ __unnamed_array_storage.778
+ __unnamed_array_storage.7997
+ __unnamed_array_storage.8.18958
+ __unnamed_array_storage.8059
+ __unnamed_array_storage.809
+ __unnamed_array_storage.817
+ __unnamed_array_storage.8708
+ __unnamed_array_storage.894
+ __unnamed_array_storage.911
+ __unnamed_array_storage.912
+ __unnamed_array_storage.9782
+ _audit_stringBluetoothManager.19396
+ _audit_stringIntents.14739
+ _audit_stringIntents.29741
+ _audit_stringMediaExperience.26156
+ _classLSApplicationProxy.32889
+ _classLSApplicationProxy.44109
+ _classVTPreferences.44287
+ _class_DKEventQuery.20553
+ _class_DKKnowledgeStore.20591
+ _class_DKQuery.20566
+ _class_DKSystemEventStreams.20576
+ _exp
+ _getINSearchForMessagesIntentIdentifier.14729
+ _getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.14740
+ _getINSendMessageIntentIdentifierSymbolLoc.ptr.14730
+ _getLSApplicationProxyClass.32881
+ _getLSApplicationProxyClass.44105
+ _getVTPreferencesClass.44283
+ _get_DKEventQueryClass.20527
+ _get_DKKnowledgeStoreClass.20585
+ _get_DKQueryClass.20524
+ _get_DKSystemEventStreamsClass.20522
+ _initLSApplicationProxy.32886
+ _initLSApplicationProxy.44107
+ _initLSApplicationProxy.sOnce.32887
+ _initLSApplicationProxy.sOnce.44108
+ _initVTPreferences.44285
+ _initVTPreferences.sOnce.44286
+ _init_DKEventQuery.20550
+ _init_DKEventQuery.sOnce.20551
+ _init_DKKnowledgeStore.20588
+ _init_DKKnowledgeStore.sOnce.20589
+ _init_DKQuery.20564
+ _init_DKQuery.sOnce.20565
+ _init_DKSystemEventStreams.20574
+ _init_DKSystemEventStreams.sOnce.20575
+ _kAFServerOverride
+ _objc_msgSend$_getCurrentAudioRoute:
+ _objc_msgSend$_hasActiveServerSideDictationLanguage:
+ _objc_msgSend$_isInactiveDeviceSyncDisabled:
+ _objc_msgSend$_isInactiveDeviceSyncDisabledByTrial:
+ _objc_msgSend$_isOptedOutOfMTEWithOptInStatus:locale:activeDictationLanguages:supportsUOD:
+ _objc_msgSend$_reloadTrialConfiguredBoostValues
+ _objc_msgSend$_updateMediaPlaybackBoost:
+ _objc_msgSend$_updateRecentSiriBoostTrialEnabled:
+ _objc_msgSend$_updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:
+ _objc_msgSend$activeDictationLanguages
+ _objc_msgSend$getAccessoryInfoForAccessoryWithUUID:completionHandler:
+ _objc_msgSend$getConversationAwarenessForCurrentlyRoutedDevice:
+ _objc_msgSend$getPersonalVolumeForCurrentlyRoutedDevice:
+ _objc_msgSend$getSidekickBoostsFileWithCompletion:
+ _objc_msgSend$getStatus
+ _objc_msgSend$getSupportsConversationAwareness
+ _objc_msgSend$getSupportsPersonalVolume
+ _objc_msgSend$getTrialEnables:doubleFactors:withCompletion:
+ _objc_msgSend$getValue
+ _objc_msgSend$initWithAddress:name:deviceUID:vendorID:productID:isAdvancedAppleAudioDevice:supportsInEarDetection:supportsVoiceTrigger:supportsJustSiri:supportsSpokenNotification:supportsListeningModeANC:supportsListeningModeTransparency:supportsListeningModeAutomatic:supportsConversationAwareness:supportsPersonalVolume:supportsAnnounceCall:
+ _objc_msgSend$initWithValue:status:
+ _objc_msgSend$isSCDATrialEnabled
+ _objc_msgSend$pushSCDAAdvertisementContext:completionHandler:
+ _objc_msgSend$setConversationAwarenessForCurrentlyRoutedDevice:withCompletion:
+ _objc_msgSend$setPersonalVolumeForCurrentlyRoutedDevice:withCompletion:
+ _objc_msgSend$setScdaContext:
+ _objc_msgSend$setSupportsConversationAwareness:
+ _objc_msgSend$setSupportsPersonalVolume:
+ _objc_msgSend$setValue:
+ _objc_msgSend$supportsConversationAwareness
+ _objc_msgSend$supportsPersonalVolume
+ _provider.onceToken.14744
+ _provider.provider.14745
+ _sharedInstance.onceToken.16543
+ _sharedInstance.onceToken.22455
+ _sharedManager.onceToken.21060
+ _sharedManager.onceToken.41293
+ _sharedManager.sharedManager.41295
+ _sharedMonitor.onceToken.19482
+ _sharedObserver.onceToken.29868
+ _sharedObserver.onceToken.43519
+ _sharedObserver.onceToken.46418
+ _sharedObserver.sharedObserver.29870
+ _sharedObserver.sharedObserver.46420
- -[AFBluetoothDeviceInfo initWithAddress:name:deviceUID:vendorID:productID:isAdvancedAppleAudioDevice:supportsInEarDetection:supportsVoiceTrigger:supportsJustSiri:supportsSpokenNotification:supportsListeningModeANC:supportsListeningModeTransparency:supportsListeningModeAutomatic:supportsAnnounceCall:]
- -[AFMyriadGoodnessScoreEvaluator _supportsConfigurableBoost]
- -[AFMyriadGoodnessScoreEvaluator _updateBiasValueWithDefault:]
- -[AFSiriDataSharingSensitivityManager _isOptedOutOfMTEWithOptInStatus:locale:supportsUOD:]
- -[AFSiriHeadphonesMonitor _getCurrentAudioRoute]
- GCC_except_table10071
- GCC_except_table10512
- GCC_except_table10525
- GCC_except_table10775
- GCC_except_table10917
- GCC_except_table10934
- GCC_except_table10936
- GCC_except_table10939
- GCC_except_table10941
- GCC_except_table1521
- GCC_except_table1527
- GCC_except_table1530
- GCC_except_table1595
- GCC_except_table1664
- GCC_except_table1917
- GCC_except_table2119
- GCC_except_table2560
- GCC_except_table2567
- GCC_except_table2571
- GCC_except_table2573
- GCC_except_table2609
- GCC_except_table2611
- GCC_except_table2617
- GCC_except_table2623
- GCC_except_table2627
- GCC_except_table2631
- GCC_except_table2634
- GCC_except_table2636
- GCC_except_table2643
- GCC_except_table2659
- GCC_except_table2662
- GCC_except_table2736
- GCC_except_table2790
- GCC_except_table2820
- GCC_except_table3159
- GCC_except_table3282
- GCC_except_table3301
- GCC_except_table3307
- GCC_except_table3312
- GCC_except_table3313
- GCC_except_table3316
- GCC_except_table3322
- GCC_except_table3410
- GCC_except_table3412
- GCC_except_table3429
- GCC_except_table3435
- GCC_except_table3477
- GCC_except_table3489
- GCC_except_table3559
- GCC_except_table3660
- GCC_except_table3667
- GCC_except_table3681
- GCC_except_table3708
- GCC_except_table3794
- GCC_except_table3848
- GCC_except_table4205
- GCC_except_table4208
- GCC_except_table4209
- GCC_except_table4528
- GCC_except_table4590
- GCC_except_table4595
- GCC_except_table4606
- GCC_except_table4618
- GCC_except_table4733
- GCC_except_table5179
- GCC_except_table5185
- GCC_except_table5191
- GCC_except_table5227
- GCC_except_table5229
- GCC_except_table5242
- GCC_except_table5262
- GCC_except_table5265
- GCC_except_table5272
- GCC_except_table5282
- GCC_except_table5283
- GCC_except_table5284
- GCC_except_table5285
- GCC_except_table5305
- GCC_except_table5398
- GCC_except_table5514
- GCC_except_table5606
- GCC_except_table5612
- GCC_except_table5710
- GCC_except_table5717
- GCC_except_table6042
- GCC_except_table6057
- GCC_except_table6088
- GCC_except_table6185
- GCC_except_table6194
- GCC_except_table6233
- GCC_except_table7047
- GCC_except_table7053
- GCC_except_table7223
- GCC_except_table7321
- GCC_except_table7351
- GCC_except_table7552
- GCC_except_table7557
- GCC_except_table7621
- GCC_except_table7716
- GCC_except_table8094
- GCC_except_table8148
- GCC_except_table8192
- GCC_except_table8280
- GCC_except_table8320
- GCC_except_table8351
- GCC_except_table8356
- GCC_except_table8357
- GCC_except_table8361
- GCC_except_table8601
- GCC_except_table8666
- GCC_except_table8672
- GCC_except_table8707
- GCC_except_table8710
- GCC_except_table8782
- GCC_except_table8811
- GCC_except_table8883
- GCC_except_table8890
- GCC_except_table8999
- GCC_except_table9003
- GCC_except_table9007
- GCC_except_table9040
- GCC_except_table9085
- GCC_except_table9521
- GCC_except_table9523
- GCC_except_table9526
- GCC_except_table9535
- GCC_except_table9561
- GCC_except_table9582
- GCC_except_table9734
- _AnnounceLibrary.sLib.41228
- _AnnounceLibrary.sOnce.41226
- _BluetoothManagerLibrary.43212
- _BluetoothManagerLibraryCore.frameworkLibrary.19195
- _CoreServicesLibrary.frameworkLibrary.43820
- _CoreSpeechLibrary.frameworkLibrary.37177
- _DataCollectionServicesLibrary.sLib.43834
- _DataCollectionServicesLibrary.sOnce.43833
- _IntentsLibrary.14532
- _IntentsLibraryCore.frameworkLibrary.14536
- _IntentsLibraryCore.frameworkLibrary.29445
- _LSApplicationProxyFunction.32607
- _LSApplicationProxyFunction.43826
- _MediaExperienceLibrary.25905
- _MediaExperienceLibraryCore.frameworkLibrary.25932
- _VTPreferencesFunction.44003
- _VoiceTriggerLibrary.frameworkLibrary.43997
- __DKEventQueryFunction.20359
- __DKKnowledgeStoreFunction.20397
- __DKQueryFunction.20371
- __DKSystemEventStreamsFunction.20381
- ___301-[AFBluetoothDeviceInfo initWithAddress:name:deviceUID:vendorID:productID:isAdvancedAppleAudioDevice:supportsInEarDetection:supportsVoiceTrigger:supportsJustSiri:supportsSpokenNotification:supportsListeningModeANC:supportsListeningModeTransparency:supportsListeningModeAutomatic:supportsAnnounceCall:]_block_invoke
- ___38-[AFConnection _startRequestWithInfo:]_block_invoke.312
- ___38-[AFConnection _startRequestWithInfo:]_block_invoke.317
- ___38-[AFConnection _startRequestWithInfo:]_block_invoke_2.313
- ___43-[AFSettingsConnection dumpAssistantState:]_block_invoke.212
- ___44-[AFSettingsConnection currectNWActivityId:]_block_invoke.126
- ___47-[AFSettingsConnection startUIRequestWithInfo:]_block_invoke.147
- ___47-[AFSettingsConnection startUIRequestWithText:]_block_invoke.142
- ___48-[AFSettingsConnection siriDesignModeIsEnabled:]_block_invoke.209
- ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke.335
- ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke_2.336
- ___57-[AFSettingsConnection setIsHomePodInHH2Mode:completion:]_block_invoke.203
- ___58-[AFConnection acquireAudioSessionWithContext:completion:]_block_invoke.298
- ___60-[AFSettingsConnection multiUserCompanionDeviceIdentifiers:]_block_invoke.193
- ___60-[AFSettingsConnection setSiriDesignModeEnabled:completion:]_block_invoke.208
- ___60-[AFSettingsConnection(Internal) _handleCommand:completion:]_block_invoke.502
- ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.285
- ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.292
- ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke_2.296
- ___62-[AFMyriadGoodnessScoreEvaluator _updateBiasValueWithDefault:]_block_invoke
- ___62-[AFMyriadGoodnessScoreEvaluator _updateBiasValueWithDefault:]_block_invoke.62
- ___62-[AFSettingsConnection getCurrentAccessoryInfoWithCompletion:]_block_invoke.133
- ___62-[AFSettingsConnection getPersonalMultiUserDeviceIdentifiers:]_block_invoke.192
- ___64-[AFConnectionClientServiceDelegate requestHandleCommand:reply:]_block_invoke.719
- ___64-[AFSettingsConnection shouldSuppressSiriDataSharingOptInAlert:]_block_invoke.206
- ___65-[AFSettingsConnection setSiriDataSharingOptInStatus:completion:]_block_invoke.198
- ___68-[AFSettingsConnection deleteSiriHistoryWithContext:withCompletion:]_block_invoke.207
- ___68-[AFSettingsConnection getSiriDataSharingOptInStatusWithCompletion:]_block_invoke.199
- ___70-[AFSettingsConnection(Internal) _setSyncToken:forAceHost:completion:]_block_invoke.504
- ___73-[AFSettingsConnection setSiriDataSharingOptInAlertPresented:completion:]_block_invoke.201
- ___77-[AFSettingsConnection _createRadarWithReason:room:process:crash:completion:]_block_invoke.220
- ___79-[AFSettingsConnection setSiriDataSharingHomePodSetupDeviceIsValid:completion:]_block_invoke.202
- ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke.333
- ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke_2.334
- ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.330
- ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.332
- ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke_2.331
- ___99-[AFSettingsConnection(Internal) _sendSyncTokenToPersonalRequestsEnabledAccessoriesWithCompletion:]_block_invoke.505
- ___AFSiriActivationPerform_block_invoke.40
- ___AnnounceLibrary_block_invoke.41232
- ___Block_byref_object_copy_.10402
- ___Block_byref_object_copy_.11030
- ___Block_byref_object_copy_.11585
- ___Block_byref_object_copy_.12827
- ___Block_byref_object_copy_.13101
- ___Block_byref_object_copy_.16296
- ___Block_byref_object_copy_.16757
- ___Block_byref_object_copy_.18888
- ___Block_byref_object_copy_.19210
- ___Block_byref_object_copy_.21154
- ___Block_byref_object_copy_.21787
- ___Block_byref_object_copy_.22195
- ___Block_byref_object_copy_.27382
- ___Block_byref_object_copy_.33032
- ___Block_byref_object_copy_.33446
- ___Block_byref_object_copy_.35582
- ___Block_byref_object_copy_.36790
- ___Block_byref_object_copy_.39873
- ___Block_byref_object_copy_.43940
- ___Block_byref_object_copy_.45105
- ___Block_byref_object_copy_.45815
- ___Block_byref_object_copy_.46100
- ___Block_byref_object_copy_.5273
- ___Block_byref_object_copy_.7676
- ___Block_byref_object_copy_.9545
- ___Block_byref_object_dispose_.10403
- ___Block_byref_object_dispose_.11031
- ___Block_byref_object_dispose_.11586
- ___Block_byref_object_dispose_.12828
- ___Block_byref_object_dispose_.13102
- ___Block_byref_object_dispose_.16297
- ___Block_byref_object_dispose_.16758
- ___Block_byref_object_dispose_.18889
- ___Block_byref_object_dispose_.19211
- ___Block_byref_object_dispose_.21155
- ___Block_byref_object_dispose_.21788
- ___Block_byref_object_dispose_.22196
- ___Block_byref_object_dispose_.27383
- ___Block_byref_object_dispose_.33033
- ___Block_byref_object_dispose_.33447
- ___Block_byref_object_dispose_.35583
- ___Block_byref_object_dispose_.36791
- ___Block_byref_object_dispose_.39874
- ___Block_byref_object_dispose_.43941
- ___Block_byref_object_dispose_.45106
- ___Block_byref_object_dispose_.45816
- ___Block_byref_object_dispose_.46101
- ___Block_byref_object_dispose_.5274
- ___Block_byref_object_dispose_.7677
- ___Block_byref_object_dispose_.9546
- ___BluetoothManagerLibraryCore_block_invoke.19196
- ___DataCollectionServicesLibrary_block_invoke.43837
- ___IntentsLibraryCore_block_invoke.14537
- ___IntentsLibraryCore_block_invoke.29446
- ___MediaExperienceLibraryCore_block_invoke.25933
- ___block_descriptor_48_e8_32w_e30_v24?0"NSNumber"8"NSError"16lw32l8
- ___block_descriptor_73_e8_32s40s48s_e41_v16?0"<AFBluetoothDeviceInfoMutating>"8ls32l8s40l8s48l8
- ___block_literal_global.100.1986
- ___block_literal_global.10003
- ___block_literal_global.101.36902
- ___block_literal_global.10153
- ___block_literal_global.10209
- ___block_literal_global.104.36896
- ___block_literal_global.10706
- ___block_literal_global.109.21254
- ___block_literal_global.1094
- ___block_literal_global.111.21250
- ___block_literal_global.1113
- ___block_literal_global.1117
- ___block_literal_global.112.20351
- ___block_literal_global.1121
- ___block_literal_global.11239
- ___block_literal_global.11318
- ___block_literal_global.11345
- ___block_literal_global.11407
- ___block_literal_global.1143
- ___block_literal_global.115.21245
- ___block_literal_global.11605
- ___block_literal_global.117.31739
- ___block_literal_global.118.43305
- ___block_literal_global.11860
- ___block_literal_global.119.21240
- ___block_literal_global.11900
- ___block_literal_global.120.31792
- ___block_literal_global.123.21236
- ___block_literal_global.12389
- ___block_literal_global.12532
- ___block_literal_global.1291
- ___block_literal_global.130
- ___block_literal_global.132
- ___block_literal_global.13249
- ___block_literal_global.13439
- ___block_literal_global.135.41227
- ___block_literal_global.13596
- ___block_literal_global.136
- ___block_literal_global.1375
- ___block_literal_global.13903
- ___block_literal_global.14011
- ___block_literal_global.141.41242
- ___block_literal_global.143.31744
- ___block_literal_global.144.41239
- ___block_literal_global.146.31771
- ___block_literal_global.149.31756
- ___block_literal_global.149.37170
- ___block_literal_global.15.21797
- ___block_literal_global.15.44608
- ___block_literal_global.150.43356
- ___block_literal_global.151
- ___block_literal_global.153.41234
- ___block_literal_global.153.43422
- ___block_literal_global.15368
- ___block_literal_global.155.31767
- ___block_literal_global.1576
- ___block_literal_global.15961
- ___block_literal_global.161.31763
- ___block_literal_global.16129
- ___block_literal_global.16340
- ___block_literal_global.167.31754
- ___block_literal_global.16750
- ___block_literal_global.177.39484
- ___block_literal_global.17765
- ___block_literal_global.17784
- ___block_literal_global.1785
- ___block_literal_global.179.43451
- ___block_literal_global.18129
- ___block_literal_global.182
- ___block_literal_global.18271
- ___block_literal_global.18311
- ___block_literal_global.18343
- ___block_literal_global.186
- ___block_literal_global.1868
- ___block_literal_global.1871
- ___block_literal_global.18757
- ___block_literal_global.188
- ___block_literal_global.18832
- ___block_literal_global.18890
- ___block_literal_global.191
- ___block_literal_global.1918
- ___block_literal_global.19262
- ___block_literal_global.1928
- ___block_literal_global.1952
- ___block_literal_global.19621
- ___block_literal_global.19688
- ___block_literal_global.1976
- ___block_literal_global.19790
- ___block_literal_global.1981
- ___block_literal_global.19915
- ___block_literal_global.19945
- ___block_literal_global.20.43273
- ___block_literal_global.2008
- ___block_literal_global.20389
- ___block_literal_global.205.43475
- ___block_literal_global.2091
- ___block_literal_global.211
- ___block_literal_global.21322
- ___block_literal_global.21805
- ___block_literal_global.22246
- ___block_literal_global.22270
- ___block_literal_global.22350
- ___block_literal_global.22727
- ___block_literal_global.22904
- ___block_literal_global.24220
- ___block_literal_global.249
- ___block_literal_global.24964
- ___block_literal_global.24991
- ___block_literal_global.25129
- ___block_literal_global.252
- ___block_literal_global.25325
- ___block_literal_global.2545
- ___block_literal_global.25491
- ___block_literal_global.25750
- ___block_literal_global.25962
- ___block_literal_global.26.10219
- ___block_literal_global.26790
- ___block_literal_global.273
- ___block_literal_global.27339
- ___block_literal_global.27418
- ___block_literal_global.27512
- ___block_literal_global.27830
- ___block_literal_global.27880
- ___block_literal_global.279
- ___block_literal_global.27934
- ___block_literal_global.2807
- ___block_literal_global.28575
- ___block_literal_global.28701
- ___block_literal_global.288
- ___block_literal_global.28800
- ___block_literal_global.28843
- ___block_literal_global.29.10210
- ___block_literal_global.2900
- ___block_literal_global.29588
- ___block_literal_global.301
- ___block_literal_global.303
- ___block_literal_global.31345
- ___block_literal_global.31795
- ___block_literal_global.31930
- ___block_literal_global.3204
- ___block_literal_global.32600
- ___block_literal_global.3270
- ___block_literal_global.3295
- ___block_literal_global.33191
- ___block_literal_global.33459
- ___block_literal_global.33531
- ___block_literal_global.35517
- ___block_literal_global.35598
- ___block_literal_global.36477
- ___block_literal_global.36504
- ___block_literal_global.36610
- ___block_literal_global.36675
- ___block_literal_global.36909
- ___block_literal_global.37103
- ___block_literal_global.37557
- ___block_literal_global.376
- ___block_literal_global.37608
- ___block_literal_global.379
- ___block_literal_global.38.21310
- ___block_literal_global.382
- ___block_literal_global.38539
- ___block_literal_global.38573
- ___block_literal_global.38845
- ___block_literal_global.39066
- ___block_literal_global.39480
- ___block_literal_global.39691
- ___block_literal_global.39900
- ___block_literal_global.40.21304
- ___block_literal_global.40020
- ___block_literal_global.41003
- ___block_literal_global.41055
- ___block_literal_global.41250
- ___block_literal_global.41699
- ___block_literal_global.41971
- ___block_literal_global.42.21301
- ___block_literal_global.42.25499
- ___block_literal_global.42057
- ___block_literal_global.43257
- ___block_literal_global.4403
- ___block_literal_global.44274
- ___block_literal_global.44300
- ___block_literal_global.44454
- ___block_literal_global.44602
- ___block_literal_global.45.25500
- ___block_literal_global.45124
- ___block_literal_global.45771
- ___block_literal_global.46120
- ___block_literal_global.488
- ___block_literal_global.495
- ___block_literal_global.497
- ___block_literal_global.498
- ___block_literal_global.499
- ___block_literal_global.5.46106
- ___block_literal_global.501
- ___block_literal_global.510
- ___block_literal_global.524
- ___block_literal_global.531
- ___block_literal_global.5428
- ___block_literal_global.5599
- ___block_literal_global.5658
- ___block_literal_global.59.43288
- ___block_literal_global.592
- ___block_literal_global.60.22720
- ___block_literal_global.60.33461
- ___block_literal_global.64.43293
- ___block_literal_global.65.21287
- ___block_literal_global.6665
- ___block_literal_global.67.18882
- ___block_literal_global.6736
- ___block_literal_global.695
- ___block_literal_global.70.33466
- ___block_literal_global.704
- ___block_literal_global.71.28763
- ___block_literal_global.711
- ___block_literal_global.719
- ___block_literal_global.73.21282
- ___block_literal_global.73.33467
- ___block_literal_global.731
- ___block_literal_global.734
- ___block_literal_global.745
- ___block_literal_global.75.21279
- ___block_literal_global.763
- ___block_literal_global.775
- ___block_literal_global.784
- ___block_literal_global.786
- ___block_literal_global.7968
- ___block_literal_global.8005
- ___block_literal_global.81.25494
- ___block_literal_global.8124
- ___block_literal_global.8173
- ___block_literal_global.818
- ___block_literal_global.826
- ___block_literal_global.83.41120
- ___block_literal_global.862
- ___block_literal_global.865
- ___block_literal_global.8678
- ___block_literal_global.869
- ___block_literal_global.873
- ___block_literal_global.873.43677
- ___block_literal_global.889
- ___block_literal_global.9.43262
- ___block_literal_global.92.36898
- ___block_literal_global.921.43789
- ___block_literal_global.927
- ___block_literal_global.9305
- ___block_literal_global.935
- ___block_literal_global.938
- ___block_literal_global.942
- ___block_literal_global.95.36906
- ___block_literal_global.953
- ___block_literal_global.956
- ___getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.14541
- ___getINSendMessageIntentIdentifierSymbolLoc_block_invoke.14531
- ___initLSApplicationProxy_block_invoke.32604
- ___initLSApplicationProxy_block_invoke.43819
- ___initVTPreferences_block_invoke.43996
- ___init_DKEventQuery_block_invoke.20355
- ___init_DKKnowledgeStore_block_invoke.20393
- ___init_DKQuery_block_invoke.20367
- ___init_DKSystemEventStreams_block_invoke.20377
- __unnamed_array_storage.10007
- __unnamed_array_storage.10710
- __unnamed_array_storage.11322
- __unnamed_array_storage.11411
- __unnamed_array_storage.11864
- __unnamed_array_storage.11904
- __unnamed_array_storage.12393
- __unnamed_array_storage.13600
- __unnamed_array_storage.1379
- __unnamed_array_storage.14.13601
- __unnamed_array_storage.14.18348
- __unnamed_array_storage.14.24996
- __unnamed_array_storage.14.28580
- __unnamed_array_storage.14.36509
- __unnamed_array_storage.14.36680
- __unnamed_array_storage.14.39071
- __unnamed_array_storage.14.45776
- __unnamed_array_storage.14.7973
- __unnamed_array_storage.14.8035
- __unnamed_array_storage.14248
- __unnamed_array_storage.1580
- __unnamed_array_storage.17788
- __unnamed_array_storage.1787
- __unnamed_array_storage.1790
- __unnamed_array_storage.1793
- __unnamed_array_storage.1796
- __unnamed_array_storage.18347
- __unnamed_array_storage.1856
- __unnamed_array_storage.18761
- __unnamed_array_storage.18837
- __unnamed_array_storage.19.11905
- __unnamed_array_storage.19.22275
- __unnamed_array_storage.19.24969
- __unnamed_array_storage.19.26795
- __unnamed_array_storage.19.2812
- __unnamed_array_storage.19.3300
- __unnamed_array_storage.19.36482
- __unnamed_array_storage.19.38544
- __unnamed_array_storage.19.41976
- __unnamed_array_storage.1966
- __unnamed_array_storage.19949
- __unnamed_array_storage.22274
- __unnamed_array_storage.22354
- __unnamed_array_storage.22892
- __unnamed_array_storage.23.44279
- __unnamed_array_storage.24.22908
- __unnamed_array_storage.24.24225
- __unnamed_array_storage.24.25967
- __unnamed_array_storage.24.27835
- __unnamed_array_storage.24.31935
- __unnamed_array_storage.24.37562
- __unnamed_array_storage.24224
- __unnamed_array_storage.24968
- __unnamed_array_storage.24995
- __unnamed_array_storage.25329
- __unnamed_array_storage.25754
- __unnamed_array_storage.25966
- __unnamed_array_storage.26794
- __unnamed_array_storage.27343
- __unnamed_array_storage.27422
- __unnamed_array_storage.27834
- __unnamed_array_storage.27938
- __unnamed_array_storage.2811
- __unnamed_array_storage.28579
- __unnamed_array_storage.28847
- __unnamed_array_storage.29.25755
- __unnamed_array_storage.29.38578
- __unnamed_array_storage.29425
- __unnamed_array_storage.3.17789
- __unnamed_array_storage.3.27344
- __unnamed_array_storage.3.33196
- __unnamed_array_storage.3.44305
- __unnamed_array_storage.31934
- __unnamed_array_storage.3274
- __unnamed_array_storage.3299
- __unnamed_array_storage.33195
- __unnamed_array_storage.33535
- __unnamed_array_storage.34.19950
- __unnamed_array_storage.36481
- __unnamed_array_storage.36508
- __unnamed_array_storage.36679
- __unnamed_array_storage.37561
- __unnamed_array_storage.37612
- __unnamed_array_storage.38543
- __unnamed_array_storage.38577
- __unnamed_array_storage.387
- __unnamed_array_storage.38849
- __unnamed_array_storage.39070
- __unnamed_array_storage.39904
- __unnamed_array_storage.41703
- __unnamed_array_storage.41975
- __unnamed_array_storage.42061
- __unnamed_array_storage.43704
- __unnamed_array_storage.44.11865
- __unnamed_array_storage.44.12394
- __unnamed_array_storage.44.38850
- __unnamed_array_storage.44278
- __unnamed_array_storage.44304
- __unnamed_array_storage.45775
- __unnamed_array_storage.472
- __unnamed_array_storage.480
- __unnamed_array_storage.481
- __unnamed_array_storage.49.11412
- __unnamed_array_storage.49.28848
- __unnamed_array_storage.54.37613
- __unnamed_array_storage.542
- __unnamed_array_storage.627
- __unnamed_array_storage.656.43854
- __unnamed_array_storage.6740
- __unnamed_array_storage.680.43901
- __unnamed_array_storage.683
- __unnamed_array_storage.724
- __unnamed_array_storage.725
- __unnamed_array_storage.732
- __unnamed_array_storage.759
- __unnamed_array_storage.760
- __unnamed_array_storage.771
- __unnamed_array_storage.772
- __unnamed_array_storage.7972
- __unnamed_array_storage.8.18762
- __unnamed_array_storage.8034
- __unnamed_array_storage.815
- __unnamed_array_storage.823
- __unnamed_array_storage.8682
- __unnamed_array_storage.893
- __unnamed_array_storage.917
- __unnamed_array_storage.918
- __unnamed_array_storage.9628
- _audit_stringBluetoothManager.19199
- _audit_stringIntents.14539
- _audit_stringIntents.29460
- _audit_stringMediaExperience.25936
- _classLSApplicationProxy.32601
- _classLSApplicationProxy.43817
- _classVTPreferences.43994
- _class_DKEventQuery.20352
- _class_DKKnowledgeStore.20390
- _class_DKQuery.20365
- _class_DKSystemEventStreams.20375
- _getINSearchForMessagesIntentIdentifier.14529
- _getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.14540
- _getINSendMessageIntentIdentifierSymbolLoc.ptr.14530
- _getLSApplicationProxyClass.32593
- _getLSApplicationProxyClass.43813
- _getVTPreferencesClass.43990
- _get_DKEventQueryClass.20326
- _get_DKKnowledgeStoreClass.20384
- _get_DKQueryClass.20323
- _get_DKSystemEventStreamsClass.20321
- _initLSApplicationProxy.32598
- _initLSApplicationProxy.43815
- _initLSApplicationProxy.sOnce.32599
- _initLSApplicationProxy.sOnce.43816
- _initVTPreferences.43992
- _initVTPreferences.sOnce.43993
- _init_DKEventQuery.20349
- _init_DKEventQuery.sOnce.20350
- _init_DKKnowledgeStore.20387
- _init_DKKnowledgeStore.sOnce.20388
- _init_DKQuery.20363
- _init_DKQuery.sOnce.20364
- _init_DKSystemEventStreams.20373
- _init_DKSystemEventStreams.sOnce.20374
- _objc_msgSend$_createSettingsConnectionIfRequired
- _objc_msgSend$_getCurrentAudioRoute
- _objc_msgSend$_isOptedOutOfMTEWithOptInStatus:locale:supportsUOD:
- _objc_msgSend$_supportsConfigurableBoost
- _objc_msgSend$_updateBiasValueWithDefault:
- _objc_msgSend$initWithAddress:name:deviceUID:vendorID:productID:isAdvancedAppleAudioDevice:supportsInEarDetection:supportsVoiceTrigger:supportsJustSiri:supportsSpokenNotification:supportsListeningModeANC:supportsListeningModeTransparency:supportsListeningModeAutomatic:supportsAnnounceCall:
- _provider.onceToken.14544
- _provider.provider.14545
- _sharedInstance.onceToken.16339
- _sharedInstance.onceToken.22245
- _sharedManager.onceToken.20859
- _sharedManager.onceToken.41002
- _sharedManager.sharedManager.41004
- _sharedMonitor.onceToken.19280
- _sharedObserver.onceToken.29587
- _sharedObserver.onceToken.43219
- _sharedObserver.onceToken.46119
- _sharedObserver.sharedObserver.29589
- _sharedObserver.sharedObserver.46121
CStrings:
+ "\x01A\x13\x11"
+ "%@ {address = %@, name = %@, deviceUID = %@, vendorID = %u, productID = %u, isAdvancedAppleAudioDevice = %@, supportsInEarDetection = %@, supportsVoiceTrigger = %@, supportsJustSiri = %@, supportsSpokenNotification = %@, supportsListeningModeANC = %@, supportsListeningModeTransparency = %@, supportsListeningModeAutomatic = %@, supportsConversationAwareness = %@, supportsPersonalVolume = %@, supportsAnnounceCall = %@}"
+ "%@ {value = %@, status = %@}"
+ "%s #MTEOptOut Should drop MTE: %@ with optInStatus: %@, locale: %@, supportsUOD: %@, activeDictationLanguages: %@"
+ "%s #MTEOptOut active server-side dictation language detected: %@. Can't drop MTE."
+ "%s #myriad Error loading Trial factors: %@"
+ "%s #myriad Error updating sidekick boosts: unsupported platform"
+ "%s #myriad Recent Siri Boost Trial Enable Not Loaded"
+ "%s #myriad Recent Siri exponential factors not loaded: %@ %@ %@"
+ "%s #myriad Trial HomePod Boost not loaded: %@"
+ "%s #myriad Trial Playback Boost not loaded: %@"
+ "%s #myriad exponential bump %f"
+ "%s #myriad trial exponential boost configured, replacing %f with %du"
+ "%s #myriad updated Trial recent Siri exponential boost to %du %.12f %.12f %.12f"
+ "%s #myriad updated _isRecentSiriBoostTrialEnabled to %@"
+ "%s #myriad updated _mediaPlaybackBoost to %d"
+ "%s #myriad updated platform bias to %d"
+ "%s Activation context is textRequest. Don't set speechRequestOptions."
+ "%s Trial Boosts Updated Notification"
+ "%s Unable to find sidekick boosts plist at path %@."
+ "%s Unable to initialize sidekick boosts from plist file at path %@ due to error %@"
+ "%s Unable to read sidekick boosts plist file at path %@."
+ "%s Unexpected type of initialized sidekick boosts plist %@."
+ "%s _readSidekickBoostsFile: called with empty filepath"
+ "%s isSyncDisabledForFullUoDDevices configured to '%d' with Trial"
+ "-[AFMyriadGoodnessScoreEvaluator _readSidekickBoostsFile:]"
+ "-[AFMyriadGoodnessScoreEvaluator _reloadTrialConfiguredBoostValues]_block_invoke"
+ "-[AFMyriadGoodnessScoreEvaluator _updateMediaPlaybackBoost:]"
+ "-[AFMyriadGoodnessScoreEvaluator _updateRecentSiriBoostTrialEnabled:]"
+ "-[AFMyriadGoodnessScoreEvaluator _updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:]"
+ "-[AFMyriadGoodnessScoreEvaluator _updateSidekickBoosts:]"
+ "-[AFMyriadGoodnessScoreEvaluator myriadTrialBoostsUpdated:]_block_invoke"
+ "-[AFPreferences isSyncDisabledForFullUoDDevices]"
+ "-[AFSettingsConnection getAccessoryInfoForAccessoryWithUUID:completionHandler:]_block_invoke"
+ "-[AFSettingsConnection getConversationAwarenessForCurrentlyRoutedDevice:]_block_invoke"
+ "-[AFSettingsConnection getPersonalVolumeForCurrentlyRoutedDevice:]_block_invoke"
+ "-[AFSettingsConnection getSidekickBoostsFileWithCompletion:]_block_invoke"
+ "-[AFSettingsConnection getTrialEnables:doubleFactors:withCompletion:]_block_invoke"
+ "-[AFSettingsConnection pushSCDAAdvertisementContext:completionHandler:]_block_invoke"
+ "-[AFSettingsConnection setConversationAwarenessForCurrentlyRoutedDevice:withCompletion:]_block_invoke"
+ "-[AFSettingsConnection setPersonalVolumeForCurrentlyRoutedDevice:withCompletion:]_block_invoke"
+ "-[AFSettingsConnection(Internal) _isInactiveDeviceSyncDisabled:]_block_invoke"
+ "-[AFSettingsConnection(Internal) _isInactiveDeviceSyncDisabledByTrial:]_block_invoke"
+ "-[AFSiriDataSharingSensitivityManager _hasActiveServerSideDictationLanguage:]"
+ "@\"AFBluetoothDeviceBooleanSettingResponse\""
+ "@\"SCDAContext\""
+ "@92@0:8@16@24@32I40I44B48B52B56B60B64B68B72B76B80B84B88"
+ "AFBluetoothDeviceBooleanSettingResponse"
+ "AFBluetoothDeviceBooleanSettingResponse::status"
+ "AFBluetoothDeviceBooleanSettingResponse::value"
+ "AFBluetoothDeviceBooleanSettingResponseMutability"
+ "AFBluetoothDeviceBooleanSettingResponseMutating"
+ "AFBluetoothDeviceInfo::supportsConversationAwareness"
+ "AFBluetoothDeviceInfo::supportsPersonalVolume"
+ "AFMyriadGoodnessComputeExponentialBoost"
+ "AFMyriadTrialBoostsUpdatedNotification"
+ "B44@0:8q16@24@32B40"
+ "HOMEPOD_BOOST"
+ "Is Trial config set to disable sync for FullUoD en_US devices"
+ "ODD_SIRI_CLIENT_EVENT"
+ "Q36@0:8@16B24@28"
+ "R\x11a\x19\x17\x11\x12\x14!"
+ "RECENT_PLAYBACK_BOOST"
+ "RECENT_SIRI_BOOST_FIRST_DEGREE_COEFF"
+ "RECENT_SIRI_BOOST_INTERCEPT"
+ "RECENT_SIRI_BOOST_SECOND_DEGREE_COEFF"
+ "RECENT_SIRI_BOOST_TRIAL_ENABLE"
+ "SESSION_BYTE_EVENT"
+ "SESSION_EVENT"
+ "Server Override"
+ "T@\"SCDAContext\",C,N,V_scdaContext"
+ "TB,N,V_isATVHandoff"
+ "TB,R,N,V_supportsConversationAwareness"
+ "TB,R,N,V_supportsPersonalVolume"
+ "Tq,R,N,V_status"
+ "Tq,R,N,V_value"
+ "Vv24@0:8@?<v@?@\"AFBluetoothDeviceBooleanSettingResponse\">16"
+ "Vv28@0:8B16@?<v@?@\"AFBluetoothDeviceBooleanSettingResponse\">20"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?B@\"NSString\"@\"NSError\">24"
+ "Vv32@0:8@\"SCDAAdvertisementContext\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "Vv40@0:8@\"NSArray\"16@\"NSArray\"24@?<v@?@\"NSDictionary\"@\"NSDictionary\"@\"NSError\">32"
+ "_AFBluetoothDeviceBooleanSettingResponseMutation"
+ "_endpointModelName"
+ "_findSidekickBoost:isSpeaker:model:"
+ "_getCurrentAudioRoute:"
+ "_hasActiveServerSideDictationLanguage:"
+ "_isATVHandoff"
+ "_isExponentialBoostDefined"
+ "_isInactiveDeviceSyncDisabled:"
+ "_isInactiveDeviceSyncDisabledByTrial:"
+ "_isOptedOutOfMTEWithOptInStatus:locale:activeDictationLanguages:supportsUOD:"
+ "_isRecentSiriBoostTrialEnabled"
+ "_isSpeakerEndpoint"
+ "_mediaPlaybackBoost"
+ "_readSidekickBoostsFile:"
+ "_recentSiriFirstDegreeCoefficient"
+ "_recentSiriIntercept"
+ "_recentSiriSecondDegreeCoefficient"
+ "_reloadTrialConfiguredBoostValues"
+ "_scdaContext"
+ "_setSidekickPlatformBiasForSpeaker:model:"
+ "_status"
+ "_supportsConversationAwareness"
+ "_supportsPersonalVolume"
+ "_updateMediaPlaybackBoost:"
+ "_updateRecentSiriBoostTrialEnabled:"
+ "_updateRecentSiriExponentialBoostDefined:withSecondDegree:andFirstDegree:andIntercept:"
+ "_updateSidekickBoosts:"
+ "ar_SA"
+ "da_DK"
+ "de_AT"
+ "de_CH"
+ "en_IE"
+ "en_NZ"
+ "en_SG"
+ "en_ZA"
+ "es_CL"
+ "fi_FI"
+ "fr_BE"
+ "fr_CA"
+ "fr_CH"
+ "getAccessoryInfoForAccessoryWithUUID:completionHandler:"
+ "getConversationAwarenessForCurrentlyRoutedDevice:"
+ "getConversationAwarenessForCurrentlyRoutedDeviceWithCompletion:"
+ "getCurrentAudioRoute"
+ "getPersonalVolumeForCurrentlyRoutedDevice:"
+ "getPersonalVolumeForCurrentlyRoutedDeviceWithCompletion:"
+ "getSidekickBoostsFileWithCompletion:"
+ "getStatus"
+ "getSupportsConversationAwareness"
+ "getSupportsPersonalVolume"
+ "getTrialEnables:doubleFactors:withCompletion:"
+ "getValue"
+ "he_IL"
+ "id_ID"
+ "initWithAddress:name:deviceUID:vendorID:productID:isAdvancedAppleAudioDevice:supportsInEarDetection:supportsVoiceTrigger:supportsJustSiri:supportsSpokenNotification:supportsListeningModeANC:supportsListeningModeTransparency:supportsListeningModeAutomatic:supportsConversationAwareness:supportsPersonalVolume:supportsAnnounceCall:"
+ "initWithValue:status:"
+ "isATVHandoff"
+ "isSCDATrialEnabled"
+ "isSyncDisabledForFullUoDDevices"
+ "it_CH"
+ "it_IT"
+ "ko_KR"
+ "ms_MY"
+ "myriadTrialBoostsUpdated:"
+ "nb_NO"
+ "nl_BE"
+ "nl_NL"
+ "noDevice"
+ "pt_BR"
+ "pushSCDAAdvertisementContext:completionHandler:"
+ "ru_RU"
+ "scdaContext"
+ "scda_trial_boosts"
+ "setConversationAwarenessForCurrentlyRoutedDevice:withCompletion:"
+ "setIsATVHandoff:"
+ "setPersonalVolumeForCurrentlyRoutedDevice:withCompletion:"
+ "setScdaContext:"
+ "setServerOverride:"
+ "setSupportsConversationAwareness:"
+ "setSupportsPersonalVolume:"
+ "supportsConversationAwareness"
+ "supportsPersonalVolume"
+ "sv_SE"
+ "th_TH"
+ "tr_TR"
+ "unsupported"
+ "uodStatusSupportedFull:languageCode:"
+ "v16@?0@\"<AFBluetoothDeviceBooleanSettingResponseMutating>\"8"
+ "v16@?0@\"AFBluetoothDeviceBooleanSettingResponse\"8"
+ "v32@?0@\"NSDictionary\"8@\"NSDictionary\"16@\"NSError\"24"
+ "v44@0:8B16d20d28d36"
+ "vi_VN"
+ "yue_CN"
+ "zh_TW"
+ "{_mutationFlags=\"isDirty\"b1\"hasAddress\"b1\"hasName\"b1\"hasDeviceUID\"b1\"hasVendorID\"b1\"hasProductID\"b1\"hasIsAdvancedAppleAudioDevice\"b1\"hasSupportsInEarDetection\"b1\"hasSupportsVoiceTrigger\"b1\"hasSupportsJustSiri\"b1\"hasSupportsSpokenNotification\"b1\"hasSupportsListeningModeANC\"b1\"hasSupportsListeningModeTransparency\"b1\"hasSupportsListeningModeAutomatic\"b1\"hasSupportsConversationAwareness\"b1\"hasSupportsPersonalVolume\"b1\"hasSupportsAnnounceCall\"b1}"
+ "{_mutationFlags=\"isDirty\"b1\"hasValue\"b1\"hasStatus\"b1}"
- "\x01\x11\x13"
- "%@ {address = %@, name = %@, deviceUID = %@, vendorID = %u, productID = %u, isAdvancedAppleAudioDevice = %@, supportsInEarDetection = %@, supportsVoiceTrigger = %@, supportsJustSiri = %@, supportsSpokenNotification = %@, supportsListeningModeANC = %@, supportsListeningModeTransparency = %@, supportsListeningModeAutomatic = %@, supportsAnnounceCall = %@}"
- "%s #MTEOptOut Should drop MTE: %@ with optInStatus: %@, locale: %@, supportsUOD: %@"
- "%s #myriad Failed to fetch platform bias from Trial: %@ using %lu as platform boost."
- "%s #myriad platform bias value fetched from Trial: %lu"
- "%s #myriad platform bias value:%@, error: %@"
- "%s #myriad updating platform bias to %d"
- "%s Acitivation context is textRequest. Don't set speechRequestOptions."
- "-[AFMyriadGoodnessScoreEvaluator _updateBiasValueWithDefault:]_block_invoke"
- "@84@0:8@16@24@32I40I44B48B52B56B60B64B68B72B76B80"
- "B36@0:8q16@24B32"
- "R\x11a\x18\x17\x11\x12\x14!"
- "_getCurrentAudioRoute"
- "_isOptedOutOfMTEWithOptInStatus:locale:supportsUOD:"
- "_supportsConfigurableBoost"
- "_updateBiasValueWithDefault:"
- "initWithAddress:name:deviceUID:vendorID:productID:isAdvancedAppleAudioDevice:supportsInEarDetection:supportsVoiceTrigger:supportsJustSiri:supportsSpokenNotification:supportsListeningModeANC:supportsListeningModeTransparency:supportsListeningModeAutomatic:supportsAnnounceCall:"
- "ms"
- "v24@?0@\"NSNumber\"8@\"NSError\"16"
- "{_mutationFlags=\"isDirty\"b1\"hasAddress\"b1\"hasName\"b1\"hasDeviceUID\"b1\"hasVendorID\"b1\"hasProductID\"b1\"hasIsAdvancedAppleAudioDevice\"b1\"hasSupportsInEarDetection\"b1\"hasSupportsVoiceTrigger\"b1\"hasSupportsJustSiri\"b1\"hasSupportsSpokenNotification\"b1\"hasSupportsListeningModeANC\"b1\"hasSupportsListeningModeTransparency\"b1\"hasSupportsListeningModeAutomatic\"b1\"hasSupportsAnnounceCall\"b1}"

```
