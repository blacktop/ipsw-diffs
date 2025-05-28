## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3303.9.1.0.0
-  __TEXT.__text: 0x193430
+3304.85.3.0.0
+  __TEXT.__text: 0x1965d4
   __TEXT.__auth_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x18c64
+  __TEXT.__objc_methlist: 0x18fbc
   __TEXT.__const: 0x360
-  __TEXT.__gcc_except_tab: 0x18b4
-  __TEXT.__cstring: 0x398ca
-  __TEXT.__oslogstring: 0xf7b8
+  __TEXT.__gcc_except_tab: 0x19a8
+  __TEXT.__cstring: 0x399d1
+  __TEXT.__oslogstring: 0xf86a
   __TEXT.__dlopen_cstrs: 0x324
-  __TEXT.__unwind_info: 0x75a4
-  __TEXT.__objc_classname: 0x4c73
-  __TEXT.__objc_methname: 0x37d02
-  __TEXT.__objc_methtype: 0xa483
-  __TEXT.__objc_stubs: 0x22f60
+  __TEXT.__unwind_info: 0x763c
+  __TEXT.__objc_classname: 0x4ca8
+  __TEXT.__objc_methname: 0x38492
+  __TEXT.__objc_methtype: 0xa4a7
+  __TEXT.__objc_stubs: 0x23160
   __DATA_CONST.__got: 0x5c0
-  __DATA_CONST.__const: 0x7e10
-  __DATA_CONST.__objc_classlist: 0xd50
+  __DATA_CONST.__const: 0x7e70
+  __DATA_CONST.__objc_classlist: 0xd60
   __DATA_CONST.__objc_catlist: 0x290
   __DATA_CONST.__objc_protolist: 0x540
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2b970
-  __DATA_CONST.__objc_selrefs: 0xb6f8
-  __DATA_CONST.__objc_arraydata: 0x1d50
+  __DATA_CONST.__objc_const: 0x2c000
+  __DATA_CONST.__objc_selrefs: 0xb800
+  __DATA_CONST.__objc_protorefs: 0x138
+  __DATA_CONST.__objc_classrefs: 0x1020
+  __DATA_CONST.__objc_superrefs: 0xd88
+  __DATA_CONST.__objc_arraydata: 0x1d58
   __AUTH_CONST.__cfstring: 0x256a0
   __AUTH_CONST.__const: 0x3600
-  __AUTH_CONST.__objc_const: 0xc9e8
+  __AUTH_CONST.__objc_const: 0xca78
   __AUTH_CONST.__objc_intobj: 0x2028
   __AUTH_CONST.__objc_dictobj: 0xaa0
-  __AUTH_CONST.__objc_arrayobj: 0x5a0
+  __AUTH_CONST.__objc_arrayobj: 0x588
   __AUTH_CONST.__objc_doubleobj: 0x30
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0xab0
-  __AUTH.__objc_data: 0x7080
+  __AUTH.__objc_data: 0x7120
   __AUTH.__data: 0x2d8
-  __DATA.__objc_protorefs: 0x138
-  __DATA.__objc_classrefs: 0x1018
-  __DATA.__objc_superrefs: 0xd80
-  __DATA.__objc_ivar: 0x240c
+  __DATA.__objc_ivar: 0x248c
   __DATA.__objc_const_ax: 0x0
-  __DATA.__data: 0x46f0
+  __DATA.__data: 0x46f8
   __DATA.__common: 0x8
-  __DATA.__bss: 0xb48
+  __DATA.__bss: 0xb40
   __DATA_DIRTY.__objc_data: 0x14a0
   __DATA_DIRTY.__data: 0x8
   __DATA_DIRTY.__common: 0xf0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 11172
-  Symbols:   35830
-  CStrings:  18213
+  Functions: 11255
+  Symbols:   36062
+  CStrings:  18293
 
Symbols:
+ +[AFFeatureFlags(SWEFeatureFlags) isASRSpeechProfileMigrationEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isAWDLFallbackForPersonalRequestsEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isDictationAutoPunctuationSpring2024LocaleExpansionEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isHighSpeedSiriTTSEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isSiriEntityMatcherMigrationEnabled]
+ -[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:]
+ -[AFClientConfiguration supportsCarPlayVehicleData]
+ -[AFConnection _markNetworkDidBecomeActive]
+ -[AFConnection setSupportsCarPlayVehicleData:]
+ -[AFConnectionClientServiceDelegate networkDidBecomeActive]
+ -[AFLocalization getValidOutputVoiceWithDialects:]
+ -[AFPreferences multilingualResponseEnabledForLanguage:]
+ -[AFPreferences setMultilingualResponseEnabled:forLanguage:]
+ -[AFRequestContextData .cxx_destruct]
+ -[AFRequestContextData approximatePreviousTTSInterval]
+ -[AFRequestContextData audioDestination]
+ -[AFRequestContextData audioSource]
+ -[AFRequestContextData bargeInModes]
+ -[AFRequestContextData deviceRestrictions]
+ -[AFRequestContextData initWithBuilder:]
+ -[AFRequestContextData init]
+ -[AFRequestContextData isEyesFree]
+ -[AFRequestContextData isInAmbient]
+ -[AFRequestContextData isSystemApertureEnabled]
+ -[AFRequestContextData isTextToSpeechEnabled]
+ -[AFRequestContextData isTriggerlessFollowup]
+ -[AFRequestContextData isVoiceTriggerEnabled]
+ -[AFRequestContextData responseMode]
+ -[AFRequestContextData voiceAudioSessionId]
+ -[AFRequestContextData voiceTriggerEventInfo]
+ -[AFRequestContextDataMutating .cxx_destruct]
+ -[AFRequestContextDataMutating approximatePreviousTTSInterval]
+ -[AFRequestContextDataMutating audioDestination]
+ -[AFRequestContextDataMutating audioSource]
+ -[AFRequestContextDataMutating bargeInModes]
+ -[AFRequestContextDataMutating deviceRestrictions]
+ -[AFRequestContextDataMutating isEyesFree]
+ -[AFRequestContextDataMutating isInAmbient]
+ -[AFRequestContextDataMutating isSystemApertureEnabled]
+ -[AFRequestContextDataMutating isTextToSpeechEnabled]
+ -[AFRequestContextDataMutating isTriggerlessFollowup]
+ -[AFRequestContextDataMutating isVoiceTriggerEnabled]
+ -[AFRequestContextDataMutating responseMode]
+ -[AFRequestContextDataMutating setApproximatePreviousTTSInterval:]
+ -[AFRequestContextDataMutating setAudioDestination:]
+ -[AFRequestContextDataMutating setAudioSource:]
+ -[AFRequestContextDataMutating setBargeInModes:]
+ -[AFRequestContextDataMutating setDeviceRestrictions:]
+ -[AFRequestContextDataMutating setIsEyesFree:]
+ -[AFRequestContextDataMutating setIsInAmbient:]
+ -[AFRequestContextDataMutating setIsSystemApertureEnabled:]
+ -[AFRequestContextDataMutating setIsTextToSpeechEnabled:]
+ -[AFRequestContextDataMutating setIsTriggerlessFollowup:]
+ -[AFRequestContextDataMutating setIsVoiceTriggerEnabled:]
+ -[AFRequestContextDataMutating setResponseMode:]
+ -[AFRequestContextDataMutating setVoiceAudioSessionId:]
+ -[AFRequestContextDataMutating setVoiceTriggerEventInfo:]
+ -[AFRequestContextDataMutating voiceAudioSessionId]
+ -[AFRequestContextDataMutating voiceTriggerEventInfo]
+ -[AFSiriAudioRoute connectedBTProductID]
+ -[AFSiriAudioRoute setConnectedBTProductID:]
+ -[AFSpeechInterpretation initWithDictionary:]
+ -[AFSpeechPackage hash]
+ -[AFSpeechPackage initWithDictionary:]
+ -[AFSpeechPackage isEqual:]
+ -[AFSpeechPhrase initWithDictionary:]
+ -[AFSpeechRecognition hash]
+ -[AFSpeechRecognition initWithDictionary:]
+ -[AFSpeechRecognition isEqual:]
+ -[AFSpeechToken initWithDictionary:]
+ -[AFSpeechUtterance initWithDictionary:]
+ -[_AFClientConfigurationMutation getSupportsCarPlayVehicleData]
+ -[_AFClientConfigurationMutation setSupportsCarPlayVehicleData:]
+ GCC_except_table10242
+ GCC_except_table1052
+ GCC_except_table1058
+ GCC_except_table10686
+ GCC_except_table10699
+ GCC_except_table10949
+ GCC_except_table11091
+ GCC_except_table11108
+ GCC_except_table11110
+ GCC_except_table11113
+ GCC_except_table11115
+ GCC_except_table1198
+ GCC_except_table1200
+ GCC_except_table1386
+ GCC_except_table1423
+ GCC_except_table1433
+ GCC_except_table1531
+ GCC_except_table1537
+ GCC_except_table1540
+ GCC_except_table1605
+ GCC_except_table1674
+ GCC_except_table1927
+ GCC_except_table2179
+ GCC_except_table2231
+ GCC_except_table2239
+ GCC_except_table2297
+ GCC_except_table231
+ GCC_except_table250
+ GCC_except_table2668
+ GCC_except_table2670
+ GCC_except_table2707
+ GCC_except_table2709
+ GCC_except_table2715
+ GCC_except_table2721
+ GCC_except_table2725
+ GCC_except_table2729
+ GCC_except_table2732
+ GCC_except_table2734
+ GCC_except_table2739
+ GCC_except_table2741
+ GCC_except_table2745
+ GCC_except_table2757
+ GCC_except_table2760
+ GCC_except_table2776
+ GCC_except_table2778
+ GCC_except_table2780
+ GCC_except_table2842
+ GCC_except_table2896
+ GCC_except_table2926
+ GCC_except_table3220
+ GCC_except_table3277
+ GCC_except_table3400
+ GCC_except_table3419
+ GCC_except_table3425
+ GCC_except_table3430
+ GCC_except_table3431
+ GCC_except_table3434
+ GCC_except_table3440
+ GCC_except_table3528
+ GCC_except_table3530
+ GCC_except_table3547
+ GCC_except_table3553
+ GCC_except_table3595
+ GCC_except_table3607
+ GCC_except_table3677
+ GCC_except_table3781
+ GCC_except_table3788
+ GCC_except_table3802
+ GCC_except_table3829
+ GCC_except_table3915
+ GCC_except_table3969
+ GCC_except_table433
+ GCC_except_table4338
+ GCC_except_table4341
+ GCC_except_table4342
+ GCC_except_table4663
+ GCC_except_table4726
+ GCC_except_table4731
+ GCC_except_table4742
+ GCC_except_table4754
+ GCC_except_table4869
+ GCC_except_table496
+ GCC_except_table5315
+ GCC_except_table5321
+ GCC_except_table5327
+ GCC_except_table5363
+ GCC_except_table5365
+ GCC_except_table5378
+ GCC_except_table5398
+ GCC_except_table5401
+ GCC_except_table5414
+ GCC_except_table5415
+ GCC_except_table5416
+ GCC_except_table5417
+ GCC_except_table5439
+ GCC_except_table5442
+ GCC_except_table5535
+ GCC_except_table5651
+ GCC_except_table5743
+ GCC_except_table5749
+ GCC_except_table5855
+ GCC_except_table5862
+ GCC_except_table6195
+ GCC_except_table6210
+ GCC_except_table6241
+ GCC_except_table6339
+ GCC_except_table6348
+ GCC_except_table6387
+ GCC_except_table674
+ GCC_except_table677
+ GCC_except_table684
+ GCC_except_table7205
+ GCC_except_table7211
+ GCC_except_table7381
+ GCC_except_table7479
+ GCC_except_table7509
+ GCC_except_table7710
+ GCC_except_table7715
+ GCC_except_table7779
+ GCC_except_table7885
+ GCC_except_table803
+ GCC_except_table8263
+ GCC_except_table8317
+ GCC_except_table8361
+ GCC_except_table8449
+ GCC_except_table8489
+ GCC_except_table8520
+ GCC_except_table8525
+ GCC_except_table8526
+ GCC_except_table8530
+ GCC_except_table8770
+ GCC_except_table8835
+ GCC_except_table8841
+ GCC_except_table8876
+ GCC_except_table8879
+ GCC_except_table8951
+ GCC_except_table8980
+ GCC_except_table9052
+ GCC_except_table9059
+ GCC_except_table9170
+ GCC_except_table9174
+ GCC_except_table9178
+ GCC_except_table9211
+ GCC_except_table9256
+ GCC_except_table9692
+ GCC_except_table9694
+ GCC_except_table9697
+ GCC_except_table9706
+ GCC_except_table9732
+ GCC_except_table9753
+ GCC_except_table986
+ GCC_except_table9905
+ _AFEffectiveSiriBundlePathForLocation
+ _AnnounceLibrary.sLib.41844
+ _AnnounceLibrary.sOnce.41842
+ _BluetoothManagerLibrary.43844
+ _BluetoothManagerLibraryCore.frameworkLibrary.19552
+ _CoreServicesLibrary.frameworkLibrary.44404
+ _CoreSpeechLibrary.frameworkLibrary.37760
+ _DataCollectionServicesLibrary.sLib.44418
+ _DataCollectionServicesLibrary.sOnce.44417
+ _IntentsLibrary.14874
+ _IntentsLibraryCore.frameworkLibrary.14878
+ _IntentsLibraryCore.frameworkLibrary.29931
+ _LSApplicationProxyFunction.33143
+ _LSApplicationProxyFunction.44410
+ _MediaExperienceLibrary.26314
+ _MediaExperienceLibraryCore.frameworkLibrary.26341
+ _OBJC_CLASS_$_AFRequestContextData
+ _OBJC_CLASS_$_AFRequestContextDataMutating
+ _OBJC_IVAR_$_AFClientConfiguration._supportsCarPlayVehicleData
+ _OBJC_IVAR_$_AFConnection._connectionHadActiveNetwork
+ _OBJC_IVAR_$_AFRequestContextData._approximatePreviousTTSInterval
+ _OBJC_IVAR_$_AFRequestContextData._audioDestination
+ _OBJC_IVAR_$_AFRequestContextData._audioSource
+ _OBJC_IVAR_$_AFRequestContextData._bargeInModes
+ _OBJC_IVAR_$_AFRequestContextData._deviceRestrictions
+ _OBJC_IVAR_$_AFRequestContextData._isEyesFree
+ _OBJC_IVAR_$_AFRequestContextData._isInAmbient
+ _OBJC_IVAR_$_AFRequestContextData._isSystemApertureEnabled
+ _OBJC_IVAR_$_AFRequestContextData._isTextToSpeechEnabled
+ _OBJC_IVAR_$_AFRequestContextData._isTriggerlessFollowup
+ _OBJC_IVAR_$_AFRequestContextData._isVoiceTriggerEnabled
+ _OBJC_IVAR_$_AFRequestContextData._responseMode
+ _OBJC_IVAR_$_AFRequestContextData._voiceAudioSessionId
+ _OBJC_IVAR_$_AFRequestContextData._voiceTriggerEventInfo
+ _OBJC_IVAR_$_AFRequestContextDataMutating._approximatePreviousTTSInterval
+ _OBJC_IVAR_$_AFRequestContextDataMutating._audioDestination
+ _OBJC_IVAR_$_AFRequestContextDataMutating._audioSource
+ _OBJC_IVAR_$_AFRequestContextDataMutating._bargeInModes
+ _OBJC_IVAR_$_AFRequestContextDataMutating._deviceRestrictions
+ _OBJC_IVAR_$_AFRequestContextDataMutating._isEyesFree
+ _OBJC_IVAR_$_AFRequestContextDataMutating._isInAmbient
+ _OBJC_IVAR_$_AFRequestContextDataMutating._isSystemApertureEnabled
+ _OBJC_IVAR_$_AFRequestContextDataMutating._isTextToSpeechEnabled
+ _OBJC_IVAR_$_AFRequestContextDataMutating._isTriggerlessFollowup
+ _OBJC_IVAR_$_AFRequestContextDataMutating._isVoiceTriggerEnabled
+ _OBJC_IVAR_$_AFRequestContextDataMutating._responseMode
+ _OBJC_IVAR_$_AFRequestContextDataMutating._voiceAudioSessionId
+ _OBJC_IVAR_$_AFRequestContextDataMutating._voiceTriggerEventInfo
+ _OBJC_IVAR_$_AFSiriAudioRoute._connectedBTProductID
+ _OBJC_IVAR_$__AFClientConfigurationMutation._supportsCarPlayVehicleData
+ _OBJC_METACLASS_$_AFRequestContextData
+ _OBJC_METACLASS_$_AFRequestContextDataMutating
+ _VTPreferencesFunction.44592
+ _VoiceTriggerLibrary.frameworkLibrary.44586
+ __AFPreferencesBuiltInVisionLanguages
+ __DKEventQueryFunction.20720
+ __DKKnowledgeStoreFunction.20759
+ __DKQueryFunction.20732
+ __DKSystemEventStreamsFunction.20743
+ __OBJC_$_INSTANCE_METHODS_AFRequestContextData
+ __OBJC_$_INSTANCE_METHODS_AFRequestContextDataMutating
+ __OBJC_$_INSTANCE_VARIABLES_AFRequestContextData
+ __OBJC_$_INSTANCE_VARIABLES_AFRequestContextDataMutating
+ __OBJC_$_PROP_LIST_AFRequestContextData
+ __OBJC_$_PROP_LIST_AFRequestContextDataMutating
+ __OBJC_CLASS_RO_$_AFRequestContextData
+ __OBJC_CLASS_RO_$_AFRequestContextDataMutating
+ __OBJC_METACLASS_RO_$_AFRequestContextData
+ __OBJC_METACLASS_RO_$_AFRequestContextDataMutating
+ ___27-[AFConnection _connection]_block_invoke.219
+ ___27-[AFConnection _connection]_block_invoke_2.220
+ ___31-[AFUIBridgeClient _connection]_block_invoke.67
+ ___31-[AFUIBridgeClient _connection]_block_invoke.69
+ ___348-[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:]_block_invoke
+ ___37-[AFSpeechPhrase initWithDictionary:]_block_invoke
+ ___38-[AFConnection _startRequestWithInfo:]_block_invoke.314
+ ___38-[AFConnection _startRequestWithInfo:]_block_invoke.319
+ ___38-[AFConnection _startRequestWithInfo:]_block_invoke_2.315
+ ___40-[AFAssertionCoordinator _addAssertion:]_block_invoke.111
+ ___40-[AFSpeechUtterance initWithDictionary:]_block_invoke
+ ___42-[AFSpeechRecognition initWithDictionary:]_block_invoke
+ ___42-[AFSpeechRecognition initWithDictionary:]_block_invoke_2
+ ___45-[AFSpeechInterpretation initWithDictionary:]_block_invoke
+ ___46-[AFConnection setSupportsCarPlayVehicleData:]_block_invoke
+ ___49-[AFManagedStorageConnection domainObjectForKey:]_block_invoke.58
+ ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke.337
+ ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke_2.338
+ ___53-[AFAssertionCoordinator _activateAssertionWithUUID:]_block_invoke.113
+ ___58-[AFConnection acquireAudioSessionWithContext:completion:]_block_invoke.300
+ ___58-[AFManagedStorageConnection resetKnowledgeStoreWithName:]_block_invoke.69
+ ___59-[AFConnectionClientServiceDelegate networkDidBecomeActive]_block_invoke
+ ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.287
+ ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.294
+ ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke_2.298
+ ___64-[AFConnectionClientServiceDelegate requestHandleCommand:reply:]_block_invoke.724
+ ___66-[AFManagedStorageConnection dataForKey:inKnowledgeStoreWithName:]_block_invoke.60
+ ___70-[AFManagedStorageConnection setData:forKey:inKnowledgeStoreWithName:]_block_invoke.64
+ ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke.335
+ ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke_2.336
+ ___83+[AFDictationConnection getForcedOfflineDictationSupportedLanguagesWithCompletion:]_block_invoke.235
+ ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.332
+ ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.334
+ ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke_2.333
+ ___90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.107
+ ___90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.110
+ ___97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.294
+ ___97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.297
+ ___97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke_2.301
+ ___AnnounceLibrary_block_invoke.41848
+ ___Block_byref_object_copy_.10476
+ ___Block_byref_object_copy_.10672
+ ___Block_byref_object_copy_.11305
+ ___Block_byref_object_copy_.11862
+ ___Block_byref_object_copy_.13117
+ ___Block_byref_object_copy_.13388
+ ___Block_byref_object_copy_.16656
+ ___Block_byref_object_copy_.17109
+ ___Block_byref_object_copy_.19244
+ ___Block_byref_object_copy_.19567
+ ___Block_byref_object_copy_.21510
+ ___Block_byref_object_copy_.22159
+ ___Block_byref_object_copy_.22576
+ ___Block_byref_object_copy_.27796
+ ___Block_byref_object_copy_.287
+ ___Block_byref_object_copy_.29515
+ ___Block_byref_object_copy_.33570
+ ___Block_byref_object_copy_.33984
+ ___Block_byref_object_copy_.36190
+ ___Block_byref_object_copy_.37374
+ ___Block_byref_object_copy_.40481
+ ___Block_byref_object_copy_.44528
+ ___Block_byref_object_copy_.45708
+ ___Block_byref_object_copy_.46421
+ ___Block_byref_object_copy_.46708
+ ___Block_byref_object_copy_.5336
+ ___Block_byref_object_copy_.7828
+ ___Block_byref_object_copy_.8631
+ ___Block_byref_object_copy_.9775
+ ___Block_byref_object_dispose_.10477
+ ___Block_byref_object_dispose_.10673
+ ___Block_byref_object_dispose_.11306
+ ___Block_byref_object_dispose_.11863
+ ___Block_byref_object_dispose_.13118
+ ___Block_byref_object_dispose_.13389
+ ___Block_byref_object_dispose_.16657
+ ___Block_byref_object_dispose_.17110
+ ___Block_byref_object_dispose_.19245
+ ___Block_byref_object_dispose_.19568
+ ___Block_byref_object_dispose_.21511
+ ___Block_byref_object_dispose_.22160
+ ___Block_byref_object_dispose_.22577
+ ___Block_byref_object_dispose_.27797
+ ___Block_byref_object_dispose_.288
+ ___Block_byref_object_dispose_.29516
+ ___Block_byref_object_dispose_.33571
+ ___Block_byref_object_dispose_.33985
+ ___Block_byref_object_dispose_.36191
+ ___Block_byref_object_dispose_.37375
+ ___Block_byref_object_dispose_.40482
+ ___Block_byref_object_dispose_.44529
+ ___Block_byref_object_dispose_.45709
+ ___Block_byref_object_dispose_.46422
+ ___Block_byref_object_dispose_.46709
+ ___Block_byref_object_dispose_.5337
+ ___Block_byref_object_dispose_.7829
+ ___Block_byref_object_dispose_.8632
+ ___Block_byref_object_dispose_.9776
+ ___BluetoothManagerLibraryCore_block_invoke.19553
+ ___DataCollectionServicesLibrary_block_invoke.44421
+ ___IntentsLibraryCore_block_invoke.14879
+ ___IntentsLibraryCore_block_invoke.29932
+ ___MediaExperienceLibraryCore_block_invoke.26342
+ ____AFBundleResourceGetSoundMap_block_invoke.110
+ ____AFBundleResourceGetSoundMap_block_invoke.118
+ ____AFBundleResourceGetSoundMap_block_invoke.126
+ ____AFBundleResourceGetSoundMap_block_invoke.134
+ ____AFBundleResourceGetSoundMap_block_invoke.142
+ ____AFBundleResourceGetSoundMap_block_invoke.71
+ ____AFBundleResourceGetSoundMap_block_invoke.83
+ ____AFBundleResourceGetSoundMap_block_invoke.91
+ ____AFBundleResourceGetSoundMap_block_invoke.99
+ ___block_descriptor_48_e8_32r40r_e15_v32?08Q16^B24lr32l8r40l8
+ ___block_descriptor_89_e8_32s40s48s56s64s_e41_v16?0"<AFClientConfigurationMutating>"8ls32l8s40l8s48l8s56l8s64l8
+ ___block_literal_global.101.21622
+ ___block_literal_global.101.37484
+ ___block_literal_global.10205
+ ___block_literal_global.10263
+ ___block_literal_global.103.21618
+ ___block_literal_global.104.20736
+ ___block_literal_global.104.37480
+ ___block_literal_global.10415
+ ___block_literal_global.10481
+ ___block_literal_global.109.21613
+ ___block_literal_global.10978
+ ___block_literal_global.1103
+ ___block_literal_global.112.10411
+ ___block_literal_global.112.20712
+ ___block_literal_global.1122
+ ___block_literal_global.1126
+ ___block_literal_global.1128
+ ___block_literal_global.1130
+ ___block_literal_global.1132
+ ___block_literal_global.1134
+ ___block_literal_global.1136
+ ___block_literal_global.115.21606
+ ___block_literal_global.11516
+ ___block_literal_global.1152
+ ___block_literal_global.11595
+ ___block_literal_global.11622
+ ___block_literal_global.11685
+ ___block_literal_global.118.32276
+ ___block_literal_global.118.43936
+ ___block_literal_global.11882
+ ___block_literal_global.120.10347
+ ___block_literal_global.121.32327
+ ___block_literal_global.12139
+ ___block_literal_global.12179
+ ___block_literal_global.123.21598
+ ___block_literal_global.12678
+ ___block_literal_global.12822
+ ___block_literal_global.129.21592
+ ___block_literal_global.129.32323
+ ___block_literal_global.1304
+ ___block_literal_global.132
+ ___block_literal_global.13529
+ ___block_literal_global.136
+ ___block_literal_global.136.41843
+ ___block_literal_global.13721
+ ___block_literal_global.138.32317
+ ___block_literal_global.13878
+ ___block_literal_global.1388
+ ___block_literal_global.139
+ ___block_literal_global.14199
+ ___block_literal_global.142.41856
+ ___block_literal_global.14307
+ ___block_literal_global.144.21575
+ ___block_literal_global.144.32281
+ ___block_literal_global.145
+ ___block_literal_global.148
+ ___block_literal_global.149.37753
+ ___block_literal_global.15.22169
+ ___block_literal_global.15.45209
+ ___block_literal_global.150.43987
+ ___block_literal_global.151
+ ___block_literal_global.153.44051
+ ___block_literal_global.154.41850
+ ___block_literal_global.157.41840
+ ___block_literal_global.15719
+ ___block_literal_global.159.32299
+ ___block_literal_global.1593
+ ___block_literal_global.162
+ ___block_literal_global.16316
+ ___block_literal_global.16485
+ ___block_literal_global.165.32295
+ ___block_literal_global.16700
+ ___block_literal_global.168.44069
+ ___block_literal_global.171.32274
+ ___block_literal_global.17102
+ ___block_literal_global.178
+ ___block_literal_global.179.44081
+ ___block_literal_global.1806
+ ___block_literal_global.18118
+ ___block_literal_global.18137
+ ___block_literal_global.18483
+ ___block_literal_global.18625
+ ___block_literal_global.18665
+ ___block_literal_global.18697
+ ___block_literal_global.1889
+ ___block_literal_global.1892
+ ___block_literal_global.19110
+ ___block_literal_global.19185
+ ___block_literal_global.19246
+ ___block_literal_global.1939
+ ___block_literal_global.1949
+ ___block_literal_global.19616
+ ___block_literal_global.1974
+ ___block_literal_global.19982
+ ___block_literal_global.20.43906
+ ___block_literal_global.2000
+ ___block_literal_global.20049
+ ___block_literal_global.2005
+ ___block_literal_global.20152
+ ___block_literal_global.20276
+ ___block_literal_global.2030
+ ___block_literal_global.20306
+ ___block_literal_global.20751
+ ___block_literal_global.2114
+ ___block_literal_global.21687
+ ___block_literal_global.22177
+ ___block_literal_global.22626
+ ___block_literal_global.22650
+ ___block_literal_global.22730
+ ___block_literal_global.23112
+ ___block_literal_global.232.44132
+ ___block_literal_global.23289
+ ___block_literal_global.24608
+ ___block_literal_global.252
+ ___block_literal_global.25362
+ ___block_literal_global.25389
+ ___block_literal_global.255
+ ___block_literal_global.25528
+ ___block_literal_global.25726
+ ___block_literal_global.2574
+ ___block_literal_global.25896
+ ___block_literal_global.26.10491
+ ___block_literal_global.26154
+ ___block_literal_global.26371
+ ___block_literal_global.27203
+ ___block_literal_global.275
+ ___block_literal_global.27754
+ ___block_literal_global.27832
+ ___block_literal_global.27927
+ ___block_literal_global.281
+ ___block_literal_global.28246
+ ___block_literal_global.28296
+ ___block_literal_global.28350
+ ___block_literal_global.2837
+ ___block_literal_global.28998
+ ___block_literal_global.29.10482
+ ___block_literal_global.290
+ ___block_literal_global.290.13390
+ ___block_literal_global.29125
+ ___block_literal_global.29224
+ ___block_literal_global.29267
+ ___block_literal_global.2931
+ ___block_literal_global.296
+ ___block_literal_global.30076
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.310.44239
+ ___block_literal_global.313
+ ___block_literal_global.31854
+ ___block_literal_global.32330
+ ___block_literal_global.3241
+ ___block_literal_global.32465
+ ___block_literal_global.3306
+ ___block_literal_global.33136
+ ___block_literal_global.3331
+ ___block_literal_global.33730
+ ___block_literal_global.33997
+ ___block_literal_global.34071
+ ___block_literal_global.36127
+ ___block_literal_global.36209
+ ___block_literal_global.37058
+ ___block_literal_global.37085
+ ___block_literal_global.37193
+ ___block_literal_global.37258
+ ___block_literal_global.37491
+ ___block_literal_global.37686
+ ___block_literal_global.38.21675
+ ___block_literal_global.38141
+ ___block_literal_global.38192
+ ___block_literal_global.39169
+ ___block_literal_global.39443
+ ___block_literal_global.39667
+ ___block_literal_global.40.21669
+ ___block_literal_global.40086
+ ___block_literal_global.40297
+ ___block_literal_global.40508
+ ___block_literal_global.40630
+ ___block_literal_global.41616
+ ___block_literal_global.41668
+ ___block_literal_global.41864
+ ___block_literal_global.42.21666
+ ___block_literal_global.42315
+ ___block_literal_global.425
+ ___block_literal_global.42586
+ ___block_literal_global.42672
+ ___block_literal_global.428
+ ___block_literal_global.431
+ ___block_literal_global.43890
+ ___block_literal_global.4448
+ ___block_literal_global.44875
+ ___block_literal_global.44901
+ ___block_literal_global.45.25904
+ ___block_literal_global.45055
+ ___block_literal_global.45203
+ ___block_literal_global.45728
+ ___block_literal_global.4625
+ ___block_literal_global.46377
+ ___block_literal_global.46728
+ ___block_literal_global.48.25905
+ ___block_literal_global.496
+ ___block_literal_global.5.46714
+ ___block_literal_global.540
+ ___block_literal_global.5492
+ ___block_literal_global.5664
+ ___block_literal_global.5723
+ ___block_literal_global.60.21656
+ ___block_literal_global.60.33999
+ ___block_literal_global.61
+ ___block_literal_global.63.34001
+ ___block_literal_global.64.43924
+ ___block_literal_global.66.19240
+ ___block_literal_global.662
+ ___block_literal_global.671
+ ___block_literal_global.6721
+ ___block_literal_global.678
+ ___block_literal_global.68.19236
+ ___block_literal_global.68.34005
+ ___block_literal_global.686
+ ___block_literal_global.6906
+ ___block_literal_global.701
+ ___block_literal_global.71.21648
+ ___block_literal_global.71.29187
+ ___block_literal_global.712
+ ___block_literal_global.73.34006
+ ___block_literal_global.74
+ ___block_literal_global.75.21644
+ ___block_literal_global.772
+ ___block_literal_global.784
+ ___block_literal_global.785
+ ___block_literal_global.787
+ ___block_literal_global.793
+ ___block_literal_global.795
+ ___block_literal_global.8121
+ ___block_literal_global.8158
+ ___block_literal_global.8183
+ ___block_literal_global.823
+ ___block_literal_global.8278
+ ___block_literal_global.83.41733
+ ___block_literal_global.8327
+ ___block_literal_global.85.21637
+ ___block_literal_global.85.25899
+ ___block_literal_global.855
+ ___block_literal_global.862
+ ___block_literal_global.866
+ ___block_literal_global.881
+ ___block_literal_global.8842
+ ___block_literal_global.897
+ ___block_literal_global.9.43895
+ ___block_literal_global.914
+ ___block_literal_global.920
+ ___block_literal_global.925
+ ___block_literal_global.927
+ ___block_literal_global.93.21631
+ ___block_literal_global.935
+ ___block_literal_global.940
+ ___block_literal_global.95.37488
+ ___block_literal_global.9596
+ ___block_literal_global.977
+ ___block_literal_global.989
+ ___block_literal_global.993
+ ___block_literal_global.998
+ ___getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.14883
+ ___getINSendMessageIntentIdentifierSymbolLoc_block_invoke.14873
+ ___initLSApplicationProxy_block_invoke.33140
+ ___initLSApplicationProxy_block_invoke.44403
+ ___initVTPreferences_block_invoke.44585
+ ___init_DKEventQuery_block_invoke.20716
+ ___init_DKKnowledgeStore_block_invoke.20755
+ ___init_DKQuery_block_invoke.20728
+ ___init_DKSystemEventStreams_block_invoke.20739
+ __unnamed_array_storage.10209
+ __unnamed_array_storage.10267
+ __unnamed_array_storage.108
+ __unnamed_array_storage.10982
+ __unnamed_array_storage.11599
+ __unnamed_array_storage.11689
+ __unnamed_array_storage.12143
+ __unnamed_array_storage.12183
+ __unnamed_array_storage.12682
+ __unnamed_array_storage.13882
+ __unnamed_array_storage.1392
+ __unnamed_array_storage.14.13883
+ __unnamed_array_storage.14.18702
+ __unnamed_array_storage.14.25394
+ __unnamed_array_storage.14.29003
+ __unnamed_array_storage.14.37090
+ __unnamed_array_storage.14.37263
+ __unnamed_array_storage.14.39672
+ __unnamed_array_storage.14.4630
+ __unnamed_array_storage.14.46382
+ __unnamed_array_storage.14.8126
+ __unnamed_array_storage.14.8188
+ __unnamed_array_storage.14590
+ __unnamed_array_storage.1597
+ __unnamed_array_storage.1808
+ __unnamed_array_storage.1811
+ __unnamed_array_storage.1814
+ __unnamed_array_storage.18141
+ __unnamed_array_storage.1817
+ __unnamed_array_storage.18701
+ __unnamed_array_storage.1877
+ __unnamed_array_storage.19.12184
+ __unnamed_array_storage.19.22655
+ __unnamed_array_storage.19.25367
+ __unnamed_array_storage.19.27208
+ __unnamed_array_storage.19.2842
+ __unnamed_array_storage.19.3336
+ __unnamed_array_storage.19.37063
+ __unnamed_array_storage.19.39140
+ __unnamed_array_storage.19.42591
+ __unnamed_array_storage.19114
+ __unnamed_array_storage.19190
+ __unnamed_array_storage.1990
+ __unnamed_array_storage.20310
+ __unnamed_array_storage.22654
+ __unnamed_array_storage.22734
+ __unnamed_array_storage.23.44880
+ __unnamed_array_storage.23277
+ __unnamed_array_storage.24.10210
+ __unnamed_array_storage.24.23293
+ __unnamed_array_storage.24.24613
+ __unnamed_array_storage.24.26376
+ __unnamed_array_storage.24.28251
+ __unnamed_array_storage.24.32470
+ __unnamed_array_storage.24.38146
+ __unnamed_array_storage.24612
+ __unnamed_array_storage.25366
+ __unnamed_array_storage.25393
+ __unnamed_array_storage.25730
+ __unnamed_array_storage.26158
+ __unnamed_array_storage.26375
+ __unnamed_array_storage.27207
+ __unnamed_array_storage.27758
+ __unnamed_array_storage.27836
+ __unnamed_array_storage.28250
+ __unnamed_array_storage.28354
+ __unnamed_array_storage.2841
+ __unnamed_array_storage.29.26159
+ __unnamed_array_storage.29.39174
+ __unnamed_array_storage.29002
+ __unnamed_array_storage.29271
+ __unnamed_array_storage.29911
+ __unnamed_array_storage.3.18142
+ __unnamed_array_storage.3.27759
+ __unnamed_array_storage.3.33735
+ __unnamed_array_storage.3.44906
+ __unnamed_array_storage.32469
+ __unnamed_array_storage.3310
+ __unnamed_array_storage.3335
+ __unnamed_array_storage.33734
+ __unnamed_array_storage.34.20311
+ __unnamed_array_storage.34075
+ __unnamed_array_storage.37062
+ __unnamed_array_storage.37089
+ __unnamed_array_storage.37262
+ __unnamed_array_storage.38145
+ __unnamed_array_storage.38196
+ __unnamed_array_storage.39173
+ __unnamed_array_storage.39447
+ __unnamed_array_storage.39671
+ __unnamed_array_storage.40512
+ __unnamed_array_storage.42319
+ __unnamed_array_storage.42590
+ __unnamed_array_storage.42676
+ __unnamed_array_storage.436.44317
+ __unnamed_array_storage.44.12144
+ __unnamed_array_storage.44.12683
+ __unnamed_array_storage.44.39448
+ __unnamed_array_storage.44316
+ __unnamed_array_storage.44879
+ __unnamed_array_storage.44905
+ __unnamed_array_storage.4629
+ __unnamed_array_storage.46381
+ __unnamed_array_storage.49.11690
+ __unnamed_array_storage.49.29272
+ __unnamed_array_storage.54.38197
+ __unnamed_array_storage.551
+ __unnamed_array_storage.557
+ __unnamed_array_storage.563
+ __unnamed_array_storage.569
+ __unnamed_array_storage.575
+ __unnamed_array_storage.581
+ __unnamed_array_storage.587
+ __unnamed_array_storage.593
+ __unnamed_array_storage.599
+ __unnamed_array_storage.605
+ __unnamed_array_storage.611
+ __unnamed_array_storage.617
+ __unnamed_array_storage.623
+ __unnamed_array_storage.629.44465
+ __unnamed_array_storage.647.44489
+ __unnamed_array_storage.653
+ __unnamed_array_storage.659
+ __unnamed_array_storage.665
+ __unnamed_array_storage.671
+ __unnamed_array_storage.677
+ __unnamed_array_storage.683
+ __unnamed_array_storage.689
+ __unnamed_array_storage.6910
+ __unnamed_array_storage.695
+ __unnamed_array_storage.701
+ __unnamed_array_storage.707
+ __unnamed_array_storage.713
+ __unnamed_array_storage.719
+ __unnamed_array_storage.725
+ __unnamed_array_storage.733
+ __unnamed_array_storage.734
+ __unnamed_array_storage.741
+ __unnamed_array_storage.747
+ __unnamed_array_storage.753
+ __unnamed_array_storage.759
+ __unnamed_array_storage.768
+ __unnamed_array_storage.769
+ __unnamed_array_storage.780
+ __unnamed_array_storage.781
+ __unnamed_array_storage.782
+ __unnamed_array_storage.8.19115
+ __unnamed_array_storage.8125
+ __unnamed_array_storage.8187
+ __unnamed_array_storage.8846
+ __unnamed_array_storage.901
+ __unnamed_array_storage.910
+ __unnamed_array_storage.911
+ __unnamed_array_storage.9858
+ _audit_stringBluetoothManager.19556
+ _audit_stringIntents.14881
+ _audit_stringIntents.29946
+ _audit_stringMediaExperience.26345
+ _classLSApplicationProxy.33137
+ _classLSApplicationProxy.44401
+ _classVTPreferences.44583
+ _class_DKEventQuery.20713
+ _class_DKKnowledgeStore.20752
+ _class_DKQuery.20726
+ _class_DKSystemEventStreams.20737
+ _getINSearchForMessagesIntentIdentifier.14871
+ _getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.14882
+ _getINSendMessageIntentIdentifierSymbolLoc.ptr.14872
+ _getLSApplicationProxyClass.33129
+ _getLSApplicationProxyClass.44397
+ _getVTPreferencesClass.44579
+ _get_DKEventQueryClass.20687
+ _get_DKKnowledgeStoreClass.20746
+ _get_DKQueryClass.20684
+ _get_DKSystemEventStreamsClass.20682
+ _initLSApplicationProxy.33134
+ _initLSApplicationProxy.44399
+ _initLSApplicationProxy.sOnce.33135
+ _initLSApplicationProxy.sOnce.44400
+ _initVTPreferences.44581
+ _initVTPreferences.sOnce.44582
+ _init_DKEventQuery.20710
+ _init_DKEventQuery.sOnce.20711
+ _init_DKKnowledgeStore.20749
+ _init_DKKnowledgeStore.sOnce.20750
+ _init_DKQuery.20724
+ _init_DKQuery.sOnce.20725
+ _init_DKSystemEventStreams.20734
+ _init_DKSystemEventStreams.sOnce.20735
+ _kAFMultilingualResponseEnablementPerLanguage
+ _kUAFNLXAssetNamespaceUpdate
+ _kUAFSiriAssistantAssetNamespaceUpdate
+ _objc_msgSend$_markNetworkDidBecomeActive
+ _objc_msgSend$approximatePreviousTTSInterval
+ _objc_msgSend$audioDestination
+ _objc_msgSend$audioSource
+ _objc_msgSend$bargeInModes
+ _objc_msgSend$bundlePath
+ _objc_msgSend$getSupportsCarPlayVehicleData
+ _objc_msgSend$initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:
+ _objc_msgSend$initWithLanguageCode:gender:name:footprint:isCustom:
+ _objc_msgSend$isDictationAutoPunctuationSpring2024LocaleExpansionEnabled
+ _objc_msgSend$isMultilingualResponseVariantSelectorEnabled
+ _objc_msgSend$isSystemApertureEnabled
+ _objc_msgSend$isTextToSpeechEnabled
+ _objc_msgSend$isTriggerlessFollowup
+ _objc_msgSend$isVoiceTriggerEnabled
+ _objc_msgSend$responseMode
+ _objc_msgSend$setByAddingObjectsFromSet:
+ _objc_msgSend$setSupportsCarPlayVehicleData:
+ _objc_msgSend$supportsCarPlayVehicleData
+ _objc_msgSend$voiceAudioSessionId
+ _provider.onceToken.14886
+ _provider.provider.14887
+ _sharedInstance.onceToken.16699
+ _sharedInstance.onceToken.22625
+ _sharedManager.onceToken.21220
+ _sharedManager.onceToken.41615
+ _sharedManager.sharedManager.41617
+ _sharedMonitor.onceToken.19640
+ _sharedObserver.onceToken.30075
+ _sharedObserver.onceToken.43850
+ _sharedObserver.onceToken.46727
+ _sharedObserver.sharedObserver.30077
+ _sharedObserver.sharedObserver.46729
+ _strictValidationOfObjectWithClassType
+ _validationOfObjectWithClassType
- -[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:]
- -[AFSettingsConnection(Internal) _isDisablingDictationOnlySyncSupported:]
- -[AFSettingsConnection(Internal) _isSiriVocabularyNotificationForAddressBookSyncSupported:]
- GCC_except_table10159
- GCC_except_table1047
- GCC_except_table1053
- GCC_except_table10603
- GCC_except_table10616
- GCC_except_table10866
- GCC_except_table11008
- GCC_except_table11025
- GCC_except_table11027
- GCC_except_table11030
- GCC_except_table11032
- GCC_except_table1193
- GCC_except_table1195
- GCC_except_table1381
- GCC_except_table1418
- GCC_except_table1428
- GCC_except_table1526
- GCC_except_table1532
- GCC_except_table1535
- GCC_except_table1600
- GCC_except_table1669
- GCC_except_table1922
- GCC_except_table2124
- GCC_except_table229
- GCC_except_table246
- GCC_except_table2589
- GCC_except_table2596
- GCC_except_table2600
- GCC_except_table2602
- GCC_except_table2639
- GCC_except_table2641
- GCC_except_table2647
- GCC_except_table2653
- GCC_except_table2661
- GCC_except_table2666
- GCC_except_table2671
- GCC_except_table2673
- GCC_except_table2677
- GCC_except_table2689
- GCC_except_table2692
- GCC_except_table2706
- GCC_except_table2708
- GCC_except_table2710
- GCC_except_table2712
- GCC_except_table2828
- GCC_except_table2858
- GCC_except_table3202
- GCC_except_table3325
- GCC_except_table3344
- GCC_except_table3350
- GCC_except_table3355
- GCC_except_table3356
- GCC_except_table3359
- GCC_except_table3365
- GCC_except_table3453
- GCC_except_table3455
- GCC_except_table3472
- GCC_except_table3478
- GCC_except_table3520
- GCC_except_table3532
- GCC_except_table3602
- GCC_except_table3703
- GCC_except_table3710
- GCC_except_table3724
- GCC_except_table3751
- GCC_except_table3837
- GCC_except_table3891
- GCC_except_table4255
- GCC_except_table4258
- GCC_except_table4259
- GCC_except_table428
- GCC_except_table4580
- GCC_except_table4642
- GCC_except_table4647
- GCC_except_table4658
- GCC_except_table4670
- GCC_except_table4785
- GCC_except_table491
- GCC_except_table5231
- GCC_except_table5237
- GCC_except_table5243
- GCC_except_table5279
- GCC_except_table5281
- GCC_except_table5294
- GCC_except_table5314
- GCC_except_table5317
- GCC_except_table5330
- GCC_except_table5331
- GCC_except_table5332
- GCC_except_table5333
- GCC_except_table5355
- GCC_except_table5358
- GCC_except_table5451
- GCC_except_table5567
- GCC_except_table5659
- GCC_except_table5665
- GCC_except_table5771
- GCC_except_table5778
- GCC_except_table6111
- GCC_except_table6126
- GCC_except_table6157
- GCC_except_table6259
- GCC_except_table6268
- GCC_except_table6307
- GCC_except_table669
- GCC_except_table672
- GCC_except_table679
- GCC_except_table7123
- GCC_except_table7129
- GCC_except_table7299
- GCC_except_table7397
- GCC_except_table7427
- GCC_except_table7628
- GCC_except_table7633
- GCC_except_table7697
- GCC_except_table7803
- GCC_except_table785
- GCC_except_table798
- GCC_except_table8181
- GCC_except_table8235
- GCC_except_table8279
- GCC_except_table8367
- GCC_except_table8407
- GCC_except_table8438
- GCC_except_table8443
- GCC_except_table8444
- GCC_except_table8448
- GCC_except_table8688
- GCC_except_table8753
- GCC_except_table8759
- GCC_except_table8794
- GCC_except_table8797
- GCC_except_table8869
- GCC_except_table8898
- GCC_except_table8970
- GCC_except_table8977
- GCC_except_table9087
- GCC_except_table9091
- GCC_except_table9095
- GCC_except_table9128
- GCC_except_table9173
- GCC_except_table9609
- GCC_except_table9611
- GCC_except_table9614
- GCC_except_table9623
- GCC_except_table9649
- GCC_except_table9670
- GCC_except_table981
- GCC_except_table9822
- _AnnounceLibrary.sLib.41519
- _AnnounceLibrary.sOnce.41517
- _BluetoothManagerLibrary.43525
- _BluetoothManagerLibraryCore.frameworkLibrary.19392
- _CoreServicesLibrary.frameworkLibrary.44073
- _CoreSpeechLibrary.frameworkLibrary.37466
- _DataCollectionServicesLibrary.sLib.44089
- _DataCollectionServicesLibrary.sOnce.44088
- _IntentsLibrary.14732
- _IntentsLibraryCore.frameworkLibrary.14736
- _IntentsLibraryCore.frameworkLibrary.29726
- _LSApplicationProxyFunction.32895
- _LSApplicationProxyFunction.44080
- _MediaExperienceLibrary.26125
- _MediaExperienceLibraryCore.frameworkLibrary.26152
- _VTPreferencesFunction.44257
- _VoiceTriggerLibrary.frameworkLibrary.44251
- __DKEventQueryFunction.20560
- __DKKnowledgeStoreFunction.20598
- __DKQueryFunction.20572
- __DKSystemEventStreamsFunction.20582
- ___27-[AFConnection _connection]_block_invoke.218
- ___27-[AFConnection _connection]_block_invoke_2.219
- ___31-[AFUIBridgeClient _connection]_block_invoke.66
- ___31-[AFUIBridgeClient _connection]_block_invoke.68
- ___321-[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:]_block_invoke
- ___38-[AFConnection _startRequestWithInfo:]_block_invoke.313
- ___38-[AFConnection _startRequestWithInfo:]_block_invoke.318
- ___38-[AFConnection _startRequestWithInfo:]_block_invoke_2.314
- ___40-[AFAssertionCoordinator _addAssertion:]_block_invoke.110
- ___49-[AFManagedStorageConnection domainObjectForKey:]_block_invoke.57
- ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke.336
- ___50-[AFConnection startAcousticIDRequestWithOptions:]_block_invoke_2.337
- ___53-[AFAssertionCoordinator _activateAssertionWithUUID:]_block_invoke.112
- ___58-[AFConnection acquireAudioSessionWithContext:completion:]_block_invoke.299
- ___58-[AFManagedStorageConnection resetKnowledgeStoreWithName:]_block_invoke.68
- ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.286
- ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke.293
- ___62-[AFConnection forceAudioSessionActiveWithContext:completion:]_block_invoke_2.297
- ___64-[AFConnectionClientServiceDelegate requestHandleCommand:reply:]_block_invoke.720
- ___66-[AFManagedStorageConnection dataForKey:inKnowledgeStoreWithName:]_block_invoke.59
- ___70-[AFManagedStorageConnection setData:forKey:inKnowledgeStoreWithName:]_block_invoke.63
- ___73-[AFSettingsConnection(Internal) _isDisablingDictationOnlySyncSupported:]_block_invoke
- ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke.334
- ___80-[AFConnection startSpeechPronunciationRequestWithOptions:pronunciationContext:]_block_invoke_2.335
- ___83+[AFDictationConnection getForcedOfflineDictationSupportedLanguagesWithCompletion:]_block_invoke.234
- ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.331
- ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke.333
- ___84-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke_2.332
- ___90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.106
- ___90-[AFConnection _dispatchCommand:isInterstitial:interstitialPhase:interstitialDelay:reply:]_block_invoke.109
- ___91-[AFSettingsConnection(Internal) _isSiriVocabularyNotificationForAddressBookSyncSupported:]_block_invoke
- ___97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.290
- ___97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke.296
- ___97-[AFDictationConnection startRecordingForPendingDictationWithLanguageCode:options:speechOptions:]_block_invoke_2.300
- ___AnnounceLibrary_block_invoke.41523
- ___Block_byref_object_copy_.10547
- ___Block_byref_object_copy_.11175
- ___Block_byref_object_copy_.11730
- ___Block_byref_object_copy_.12972
- ___Block_byref_object_copy_.13241
- ___Block_byref_object_copy_.16500
- ___Block_byref_object_copy_.16956
- ___Block_byref_object_copy_.19084
- ___Block_byref_object_copy_.19407
- ___Block_byref_object_copy_.21357
- ___Block_byref_object_copy_.21996
- ___Block_byref_object_copy_.22405
- ___Block_byref_object_copy_.27600
- ___Block_byref_object_copy_.286
- ___Block_byref_object_copy_.29309
- ___Block_byref_object_copy_.33320
- ___Block_byref_object_copy_.33734
- ___Block_byref_object_copy_.35871
- ___Block_byref_object_copy_.37079
- ___Block_byref_object_copy_.40164
- ___Block_byref_object_copy_.44196
- ___Block_byref_object_copy_.45376
- ___Block_byref_object_copy_.46086
- ___Block_byref_object_copy_.46371
- ___Block_byref_object_copy_.5297
- ___Block_byref_object_copy_.7700
- ___Block_byref_object_copy_.9657
- ___Block_byref_object_dispose_.10548
- ___Block_byref_object_dispose_.11176
- ___Block_byref_object_dispose_.11731
- ___Block_byref_object_dispose_.12973
- ___Block_byref_object_dispose_.13242
- ___Block_byref_object_dispose_.16501
- ___Block_byref_object_dispose_.16957
- ___Block_byref_object_dispose_.19085
- ___Block_byref_object_dispose_.19408
- ___Block_byref_object_dispose_.21358
- ___Block_byref_object_dispose_.21997
- ___Block_byref_object_dispose_.22406
- ___Block_byref_object_dispose_.27601
- ___Block_byref_object_dispose_.287
- ___Block_byref_object_dispose_.29310
- ___Block_byref_object_dispose_.33321
- ___Block_byref_object_dispose_.33735
- ___Block_byref_object_dispose_.35872
- ___Block_byref_object_dispose_.37080
- ___Block_byref_object_dispose_.40165
- ___Block_byref_object_dispose_.44197
- ___Block_byref_object_dispose_.45377
- ___Block_byref_object_dispose_.46087
- ___Block_byref_object_dispose_.46372
- ___Block_byref_object_dispose_.5298
- ___Block_byref_object_dispose_.7701
- ___Block_byref_object_dispose_.9658
- ___BluetoothManagerLibraryCore_block_invoke.19393
- ___DataCollectionServicesLibrary_block_invoke.44092
- ___IntentsLibraryCore_block_invoke.14737
- ___IntentsLibraryCore_block_invoke.29727
- ___MediaExperienceLibraryCore_block_invoke.26153
- ____AFBundleResourceGetSoundMap_block_invoke.109
- ____AFBundleResourceGetSoundMap_block_invoke.117
- ____AFBundleResourceGetSoundMap_block_invoke.125
- ____AFBundleResourceGetSoundMap_block_invoke.133
- ____AFBundleResourceGetSoundMap_block_invoke.141
- ____AFBundleResourceGetSoundMap_block_invoke.70
- ____AFBundleResourceGetSoundMap_block_invoke.82
- ____AFBundleResourceGetSoundMap_block_invoke.90
- ____AFBundleResourceGetSoundMap_block_invoke.98
- ___block_descriptor_88_e8_32s40s48s56s64s_e41_v16?0"<AFClientConfigurationMutating>"8ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.100
- ___block_literal_global.100.1987
- ___block_literal_global.10090
- ___block_literal_global.101.37191
- ___block_literal_global.10148
- ___block_literal_global.102
- ___block_literal_global.10298
- ___block_literal_global.10354
- ___block_literal_global.104.37185
- ___block_literal_global.10851
- ___block_literal_global.109.21464
- ___block_literal_global.1100
- ___block_literal_global.111.21461
- ___block_literal_global.1119
- ___block_literal_global.112.20552
- ___block_literal_global.1123
- ___block_literal_global.1125
- ___block_literal_global.1127
- ___block_literal_global.1129
- ___block_literal_global.1131
- ___block_literal_global.1133
- ___block_literal_global.11384
- ___block_literal_global.11463
- ___block_literal_global.1149
- ___block_literal_global.11490
- ___block_literal_global.115.21455
- ___block_literal_global.11552
- ___block_literal_global.117.32025
- ___block_literal_global.11750
- ___block_literal_global.118.43616
- ___block_literal_global.119.21450
- ___block_literal_global.120.32080
- ___block_literal_global.12005
- ___block_literal_global.12045
- ___block_literal_global.123.21445
- ___block_literal_global.12534
- ___block_literal_global.12677
- ___block_literal_global.127.21440
- ___block_literal_global.129.21437
- ___block_literal_global.1301
- ___block_literal_global.131.32077
- ___block_literal_global.13388
- ___block_literal_global.134
- ___block_literal_global.135.41518
- ___block_literal_global.13578
- ___block_literal_global.137
- ___block_literal_global.13735
- ___block_literal_global.1376
- ___block_literal_global.138.41532
- ___block_literal_global.140.32060
- ___block_literal_global.14054
- ___block_literal_global.14162
- ___block_literal_global.143
- ___block_literal_global.143.32030
- ___block_literal_global.144.41528
- ___block_literal_global.146
- ___block_literal_global.149.32042
- ___block_literal_global.149.37459
- ___block_literal_global.15.22006
- ___block_literal_global.15.44879
- ___block_literal_global.150.43667
- ___block_literal_global.152.32054
- ___block_literal_global.153.43730
- ___block_literal_global.155
- ___block_literal_global.15571
- ___block_literal_global.1577
- ___block_literal_global.158
- ___block_literal_global.161.32049
- ___block_literal_global.16165
- ___block_literal_global.16333
- ___block_literal_global.164
- ___block_literal_global.16544
- ___block_literal_global.167.32040
- ___block_literal_global.16949
- ___block_literal_global.170
- ___block_literal_global.177.39774
- ___block_literal_global.179.43758
- ___block_literal_global.17963
- ___block_literal_global.17982
- ___block_literal_global.1801
- ___block_literal_global.18327
- ___block_literal_global.18469
- ___block_literal_global.18509
- ___block_literal_global.18541
- ___block_literal_global.1884
- ___block_literal_global.1887
- ___block_literal_global.18953
- ___block_literal_global.19028
- ___block_literal_global.19086
- ___block_literal_global.1934
- ___block_literal_global.1944
- ___block_literal_global.19458
- ___block_literal_global.1953
- ___block_literal_global.19822
- ___block_literal_global.19889
- ___block_literal_global.1992
- ___block_literal_global.1997
- ___block_literal_global.19991
- ___block_literal_global.20.43584
- ___block_literal_global.2009
- ___block_literal_global.20116
- ___block_literal_global.20146
- ___block_literal_global.20590
- ___block_literal_global.2092
- ___block_literal_global.21530
- ___block_literal_global.22014
- ___block_literal_global.22456
- ___block_literal_global.22480
- ___block_literal_global.22560
- ___block_literal_global.22937
- ___block_literal_global.231
- ___block_literal_global.23114
- ___block_literal_global.24432
- ___block_literal_global.250
- ___block_literal_global.25180
- ___block_literal_global.25207
- ___block_literal_global.253
- ___block_literal_global.25345
- ___block_literal_global.2546
- ___block_literal_global.25541
- ___block_literal_global.25711
- ___block_literal_global.25970
- ___block_literal_global.26.10364
- ___block_literal_global.26182
- ___block_literal_global.27008
- ___block_literal_global.274
- ___block_literal_global.27557
- ___block_literal_global.27636
- ___block_literal_global.27730
- ___block_literal_global.280
- ___block_literal_global.28048
- ___block_literal_global.2808
- ___block_literal_global.28098
- ___block_literal_global.28152
- ___block_literal_global.28794
- ___block_literal_global.289
- ___block_literal_global.289.13243
- ___block_literal_global.28920
- ___block_literal_global.29.10355
- ___block_literal_global.2901
- ___block_literal_global.29019
- ___block_literal_global.29062
- ___block_literal_global.295
- ___block_literal_global.29869
- ___block_literal_global.302
- ___block_literal_global.304
- ___block_literal_global.309
- ___block_literal_global.312
- ___block_literal_global.31624
- ___block_literal_global.3205
- ___block_literal_global.32083
- ___block_literal_global.32218
- ___block_literal_global.3271
- ___block_literal_global.32888
- ___block_literal_global.3296
- ___block_literal_global.33479
- ___block_literal_global.33747
- ___block_literal_global.33819
- ___block_literal_global.35810
- ___block_literal_global.35887
- ___block_literal_global.36764
- ___block_literal_global.36791
- ___block_literal_global.36899
- ___block_literal_global.36964
- ___block_literal_global.37198
- ___block_literal_global.37392
- ___block_literal_global.37846
- ___block_literal_global.37897
- ___block_literal_global.38.21518
- ___block_literal_global.38829
- ___block_literal_global.38863
- ___block_literal_global.39356
- ___block_literal_global.39770
- ___block_literal_global.39981
- ___block_literal_global.40.21512
- ___block_literal_global.40191
- ___block_literal_global.40311
- ___block_literal_global.41294
- ___block_literal_global.41346
- ___block_literal_global.414
- ___block_literal_global.41539
- ___block_literal_global.417
- ___block_literal_global.41988
- ___block_literal_global.42.21509
- ___block_literal_global.420
- ___block_literal_global.42260
- ___block_literal_global.42346
- ___block_literal_global.43568
- ___block_literal_global.4404
- ___block_literal_global.44545
- ___block_literal_global.44571
- ___block_literal_global.44725
- ___block_literal_global.44873
- ___block_literal_global.45.25719
- ___block_literal_global.45395
- ___block_literal_global.4581
- ___block_literal_global.46042
- ___block_literal_global.46391
- ___block_literal_global.48.25720
- ___block_literal_global.489
- ___block_literal_global.5.46377
- ___block_literal_global.537
- ___block_literal_global.5452
- ___block_literal_global.5623
- ___block_literal_global.5682
- ___block_literal_global.59.43599
- ___block_literal_global.60.22930
- ___block_literal_global.60.33749
- ___block_literal_global.62
- ___block_literal_global.64.43604
- ___block_literal_global.65.21495
- ___block_literal_global.659
- ___block_literal_global.668
- ___block_literal_global.6689
- ___block_literal_global.67
- ___block_literal_global.67.19078
- ___block_literal_global.675
- ___block_literal_global.6760
- ___block_literal_global.683
- ___block_literal_global.695
- ___block_literal_global.70.33754
- ___block_literal_global.709
- ___block_literal_global.71.28982
- ___block_literal_global.73.21490
- ___block_literal_global.73.33755
- ___block_literal_global.75.21487
- ___block_literal_global.769
- ___block_literal_global.781
- ___block_literal_global.782
- ___block_literal_global.790
- ___block_literal_global.790.44258
- ___block_literal_global.792
- ___block_literal_global.7993
- ___block_literal_global.8030
- ___block_literal_global.8055
- ___block_literal_global.8149
- ___block_literal_global.8198
- ___block_literal_global.826
- ___block_literal_global.83.41411
- ___block_literal_global.84
- ___block_literal_global.85.25714
- ___block_literal_global.861
- ___block_literal_global.865
- ___block_literal_global.869
- ___block_literal_global.8704
- ___block_literal_global.874
- ___block_literal_global.890
- ___block_literal_global.9.43573
- ___block_literal_global.917
- ___block_literal_global.92.37187
- ___block_literal_global.922
- ___block_literal_global.923
- ___block_literal_global.934
- ___block_literal_global.938
- ___block_literal_global.9442
- ___block_literal_global.95.37195
- ___block_literal_global.952
- ___block_literal_global.976
- ___block_literal_global.988
- ___block_literal_global.992
- ___block_literal_global.997
- ___getINSearchForMessagesIntentIdentifierSymbolLoc_block_invoke.14741
- ___getINSendMessageIntentIdentifierSymbolLoc_block_invoke.14731
- ___initLSApplicationProxy_block_invoke.32892
- ___initLSApplicationProxy_block_invoke.44072
- ___initVTPreferences_block_invoke.44250
- ___init_DKEventQuery_block_invoke.20556
- ___init_DKKnowledgeStore_block_invoke.20594
- ___init_DKQuery_block_invoke.20568
- ___init_DKSystemEventStreams_block_invoke.20578
- __unnamed_array_storage.10094
- __unnamed_array_storage.10152
- __unnamed_array_storage.104
- __unnamed_array_storage.10855
- __unnamed_array_storage.11467
- __unnamed_array_storage.11556
- __unnamed_array_storage.12009
- __unnamed_array_storage.12049
- __unnamed_array_storage.12538
- __unnamed_array_storage.13739
- __unnamed_array_storage.1380
- __unnamed_array_storage.14.13740
- __unnamed_array_storage.14.18546
- __unnamed_array_storage.14.25212
- __unnamed_array_storage.14.28799
- __unnamed_array_storage.14.36796
- __unnamed_array_storage.14.36969
- __unnamed_array_storage.14.39361
- __unnamed_array_storage.14.4586
- __unnamed_array_storage.14.46047
- __unnamed_array_storage.14.7998
- __unnamed_array_storage.14.8060
- __unnamed_array_storage.14450
- __unnamed_array_storage.1581
- __unnamed_array_storage.17986
- __unnamed_array_storage.1803
- __unnamed_array_storage.1806
- __unnamed_array_storage.1809
- __unnamed_array_storage.1812
- __unnamed_array_storage.18545
- __unnamed_array_storage.1872
- __unnamed_array_storage.18957
- __unnamed_array_storage.19.12050
- __unnamed_array_storage.19.22485
- __unnamed_array_storage.19.25185
- __unnamed_array_storage.19.27013
- __unnamed_array_storage.19.2813
- __unnamed_array_storage.19.3301
- __unnamed_array_storage.19.36769
- __unnamed_array_storage.19.38834
- __unnamed_array_storage.19.42265
- __unnamed_array_storage.19033
- __unnamed_array_storage.1982
- __unnamed_array_storage.20150
- __unnamed_array_storage.22484
- __unnamed_array_storage.22564
- __unnamed_array_storage.23.44550
- __unnamed_array_storage.23102
- __unnamed_array_storage.24.10095
- __unnamed_array_storage.24.23118
- __unnamed_array_storage.24.24437
- __unnamed_array_storage.24.26187
- __unnamed_array_storage.24.28053
- __unnamed_array_storage.24.32223
- __unnamed_array_storage.24.37851
- __unnamed_array_storage.24436
- __unnamed_array_storage.25184
- __unnamed_array_storage.25211
- __unnamed_array_storage.25545
- __unnamed_array_storage.25974
- __unnamed_array_storage.26186
- __unnamed_array_storage.27012
- __unnamed_array_storage.27561
- __unnamed_array_storage.27640
- __unnamed_array_storage.28052
- __unnamed_array_storage.2812
- __unnamed_array_storage.28156
- __unnamed_array_storage.28798
- __unnamed_array_storage.29.25975
- __unnamed_array_storage.29.38868
- __unnamed_array_storage.29066
- __unnamed_array_storage.29706
- __unnamed_array_storage.3.17987
- __unnamed_array_storage.3.27562
- __unnamed_array_storage.3.33484
- __unnamed_array_storage.3.44576
- __unnamed_array_storage.32222
- __unnamed_array_storage.3275
- __unnamed_array_storage.3300
- __unnamed_array_storage.33483
- __unnamed_array_storage.33823
- __unnamed_array_storage.34.20151
- __unnamed_array_storage.36768
- __unnamed_array_storage.36795
- __unnamed_array_storage.36968
- __unnamed_array_storage.37850
- __unnamed_array_storage.37901
- __unnamed_array_storage.38833
- __unnamed_array_storage.38867
- __unnamed_array_storage.39360
- __unnamed_array_storage.40195
- __unnamed_array_storage.41992
- __unnamed_array_storage.42264
- __unnamed_array_storage.42350
- __unnamed_array_storage.425
- __unnamed_array_storage.43999
- __unnamed_array_storage.44.12010
- __unnamed_array_storage.44.12539
- __unnamed_array_storage.44.39140
- __unnamed_array_storage.44549
- __unnamed_array_storage.44575
- __unnamed_array_storage.4585
- __unnamed_array_storage.46046
- __unnamed_array_storage.49.11557
- __unnamed_array_storage.49.29067
- __unnamed_array_storage.54.37902
- __unnamed_array_storage.548
- __unnamed_array_storage.554
- __unnamed_array_storage.560
- __unnamed_array_storage.566
- __unnamed_array_storage.572
- __unnamed_array_storage.578
- __unnamed_array_storage.584
- __unnamed_array_storage.590
- __unnamed_array_storage.596
- __unnamed_array_storage.602
- __unnamed_array_storage.608
- __unnamed_array_storage.614
- __unnamed_array_storage.620.44110
- __unnamed_array_storage.626
- __unnamed_array_storage.632
- __unnamed_array_storage.644.44157
- __unnamed_array_storage.656
- __unnamed_array_storage.662
- __unnamed_array_storage.668
- __unnamed_array_storage.674
- __unnamed_array_storage.6764
- __unnamed_array_storage.680
- __unnamed_array_storage.686
- __unnamed_array_storage.692
- __unnamed_array_storage.698
- __unnamed_array_storage.704
- __unnamed_array_storage.710
- __unnamed_array_storage.716
- __unnamed_array_storage.722
- __unnamed_array_storage.728
- __unnamed_array_storage.730
- __unnamed_array_storage.738
- __unnamed_array_storage.744
- __unnamed_array_storage.750
- __unnamed_array_storage.756
- __unnamed_array_storage.762
- __unnamed_array_storage.766
- __unnamed_array_storage.777
- __unnamed_array_storage.778
- __unnamed_array_storage.779
- __unnamed_array_storage.787
- __unnamed_array_storage.7997
- __unnamed_array_storage.8.18958
- __unnamed_array_storage.8059
- __unnamed_array_storage.8708
- __unnamed_array_storage.894
- __unnamed_array_storage.913
- __unnamed_array_storage.914
- __unnamed_array_storage.9782
- _audit_stringBluetoothManager.19396
- _audit_stringIntents.14739
- _audit_stringIntents.29741
- _audit_stringMediaExperience.26156
- _classLSApplicationProxy.32889
- _classLSApplicationProxy.44070
- _classVTPreferences.44248
- _class_DKEventQuery.20553
- _class_DKKnowledgeStore.20591
- _class_DKQuery.20566
- _class_DKSystemEventStreams.20576
- _getINSearchForMessagesIntentIdentifier.14729
- _getINSearchForMessagesIntentIdentifierSymbolLoc.ptr.14740
- _getINSendMessageIntentIdentifierSymbolLoc.ptr.14730
- _getLSApplicationProxyClass.32881
- _getLSApplicationProxyClass.44066
- _getVTPreferencesClass.44244
- _get_DKEventQueryClass.20527
- _get_DKKnowledgeStoreClass.20585
- _get_DKQueryClass.20524
- _get_DKSystemEventStreamsClass.20522
- _initLSApplicationProxy.32886
- _initLSApplicationProxy.44068
- _initLSApplicationProxy.sOnce.32887
- _initLSApplicationProxy.sOnce.44069
- _initVTPreferences.44246
- _initVTPreferences.sOnce.44247
- _init_DKEventQuery.20550
- _init_DKEventQuery.sOnce.20551
- _init_DKKnowledgeStore.20588
- _init_DKKnowledgeStore.sOnce.20589
- _init_DKQuery.20564
- _init_DKQuery.sOnce.20565
- _init_DKSystemEventStreams.20574
- _init_DKSystemEventStreams.sOnce.20575
- _objc_msgSend$_isDisablingDictationOnlySyncSupported:
- _objc_msgSend$_isSiriVocabularyNotificationForAddressBookSyncSupported:
- _objc_msgSend$initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:
- _objc_msgSend$requestWillPresentUsefulUserResult
- _provider.onceToken.14744
- _provider.provider.14745
- _sharedInstance.onceToken.16543
- _sharedInstance.onceToken.22455
- _sharedManager.onceToken.21060
- _sharedManager.onceToken.41293
- _sharedManager.sharedManager.41295
- _sharedMonitor.onceToken.19482
- _sharedObserver.onceToken.29868
- _sharedObserver.onceToken.43531
- _sharedObserver.onceToken.46390
- _sharedObserver.sharedObserver.29870
- _sharedObserver.sharedObserver.46392
CStrings:
+ "\x02\x11\x112"
+ "\x024"
+ "!\x14"
+ "%@ {accessibilityState = %@, deviceRingerSwitchState = %@, isDeviceInCarDNDMode = %@, isDeviceInStarkMode = %@, supportsCarPlayVehicleData = %@, isDeviceWatchAuthenticated = %@, areAnnouncementRequestsPermittedByPresentationWhileActive = %@, outputVolume = %f, tapToSiriAudioPlaybackRequest = %@, twoShotAudioPlaybackRequest = %@, deviceSetupFlowBeginDate = %@, deviceSetupFlowEndDate = %@}"
+ "%s %d %@"
+ "%s Invalid output voice '%@:%@' found. Updated to '%@:%@'"
+ "%s Not ending the ongoing request because the active request ID is different than the completed request ID: (_activeRequestUUID = %@, requestUUID = %@, turnId = %@)"
+ "%s isMediaEntitySyncDisabled=%d: pommesEnabled=%d pommesEnabledForLanguage=%d hasATVOrHomePodInHome=%d optedOutOfDataSharing=%d "
+ "'"
+ "-[AFLocalization getValidOutputVoiceWithDialects:]"
+ "-[AFPreferences multilingualResponseEnabledForLanguage:]"
+ "-[AFPreferences setMultilingualResponseEnabled:forLanguage:]"
+ "76,8229"
+ "@88@0:8@16q24B32B36B40B44B48f52@56@64@72@80"
+ "AFClientConfiguration::supportsCarPlayVehicleData"
+ "AFRequestContextData"
+ "AFRequestContextDataMutating"
+ "Accessibility"
+ "HighSpeedSiriTTS"
+ "Multilingual Response Enablement Per Language"
+ "ODBATCH_CLIENT_EVENT"
+ "PFA_CLIENT_EVENT"
+ "T@\"NSArray\",C,N,V_bargeInModes"
+ "T@\"NSArray\",C,N,V_deviceRestrictions"
+ "T@\"NSArray\",R,C,N,V_bargeInModes"
+ "T@\"NSDateInterval\",C,N,V_approximatePreviousTTSInterval"
+ "T@\"NSDateInterval\",R,C,N,V_approximatePreviousTTSInterval"
+ "T@\"NSDictionary\",R,C,N,V_voiceTriggerEventInfo"
+ "T@\"NSString\",&,N,V_connectedBTProductID"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_audioDestination"
+ "T@\"NSString\",C,N,V_audioSource"
+ "T@\"NSString\",C,N,V_responseMode"
+ "T@\"NSString\",R,C,N,V_audioDestination"
+ "T@\"NSString\",R,C,N,V_audioSource"
+ "T@\"NSString\",R,C,N,V_responseMode"
+ "TB,N,V_isTextToSpeechEnabled"
+ "TB,N,V_isTriggerlessFollowup"
+ "TB,N,V_isVoiceTriggerEnabled"
+ "TB,R,N,V_isSystemApertureEnabled"
+ "TB,R,N,V_isTextToSpeechEnabled"
+ "TB,R,N,V_isTriggerlessFollowup"
+ "TB,R,N,V_isVoiceTriggerEnabled"
+ "TB,R,N,V_supportsCarPlayVehicleData"
+ "TI,N,V_voiceAudioSessionId"
+ "TI,R,N,V_voiceAudioSessionId"
+ "_approximatePreviousTTSInterval"
+ "_audioDestination"
+ "_audioSource"
+ "_bargeInModes"
+ "_connectedBTProductID"
+ "_connectionHadActiveNetwork"
+ "_isTextToSpeechEnabled"
+ "_isTriggerlessFollowup"
+ "_isVoiceTriggerEnabled"
+ "_markNetworkDidBecomeActive"
+ "_responseMode"
+ "_supportsCarPlayVehicleData"
+ "_voiceAudioSessionId"
+ "approximatePreviousTTSInterval"
+ "asr_speech_profile_migration"
+ "audioDestination"
+ "audioSource"
+ "awdl_fallback_for_personal_requests"
+ "bargeInModes"
+ "bundlePath"
+ "com.apple.siri.uaf.com.apple.siri.understanding"
+ "com.apple.siri.uaf.com.apple.siri.understanding.nl.overrides"
+ "connectedBTProductID"
+ "dictation_auto_punctuation_spring2024_locale_expansion"
+ "getSupportsCarPlayVehicleData"
+ "getValidOutputVoiceWithDialects:"
+ "initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:"
+ "isASRSpeechProfileMigrationEnabled"
+ "isAWDLFallbackForPersonalRequestsEnabled"
+ "isDictationAutoPunctuationSpring2024LocaleExpansionEnabled"
+ "isHighSpeedSiriTTSEnabled"
+ "isSiriEntityMatcherMigrationEnabled"
+ "isTextToSpeechEnabled"
+ "isTriggerlessFollowup"
+ "isVoiceTriggerEnabled"
+ "latMitRes"
+ "multilingualResponseEnabledForLanguage:"
+ "networkDidBecomeActive"
+ "responseMode"
+ "setApproximatePreviousTTSInterval:"
+ "setAudioDestination:"
+ "setAudioSource:"
+ "setBargeInModes:"
+ "setByAddingObjectsFromSet:"
+ "setConnectedBTProductID:"
+ "setIsTextToSpeechEnabled:"
+ "setIsTriggerlessFollowup:"
+ "setIsVoiceTriggerEnabled:"
+ "setMultilingualResponseEnabled:forLanguage:"
+ "setResponseMode:"
+ "setSupportsCarPlayVehicleData:"
+ "setVoiceAudioSessionId:"
+ "siri_entity_matcher_migration"
+ "supportsCarPlayVehicleData"
+ "voiceAudioSessionId"
+ "zh-Hans-US"
+ "{NSDecimalNumber=#b8b4b1b1b1b1b16^S}"
+ "{_mutationFlags=\"isDirty\"b1\"hasAccessibilityState\"b1\"hasDeviceRingerSwitchState\"b1\"hasIsDeviceInCarDNDMode\"b1\"hasIsDeviceInStarkMode\"b1\"hasSupportsCarPlayVehicleData\"b1\"hasIsDeviceWatchAuthenticated\"b1\"hasAreAnnouncementRequestsPermittedByPresentationWhileActive\"b1\"hasOutputVolume\"b1\"hasTapToSiriAudioPlaybackRequest\"b1\"hasTwoShotAudioPlaybackRequest\"b1\"hasDeviceSetupFlowBeginDate\"b1\"hasDeviceSetupFlowEndDate\"b1}"
- "\x02\x11B"
- "\x02$"
- "\x11\x14"
- "%@ {accessibilityState = %@, deviceRingerSwitchState = %@, isDeviceInCarDNDMode = %@, isDeviceInStarkMode = %@, isDeviceWatchAuthenticated = %@, areAnnouncementRequestsPermittedByPresentationWhileActive = %@, outputVolume = %f, tapToSiriAudioPlaybackRequest = %@, twoShotAudioPlaybackRequest = %@, deviceSetupFlowBeginDate = %@, deviceSetupFlowEndDate = %@}"
- "%s Assistant Enablement State: %d"
- "%s isMediaEntitySyncDisabled=%d: pommesEnabled=%d pommesEnabledForLanguage=%d hasPairedWatches=%d hasATVOrHomePodInHome=%d optedOutOfDataSharing=%d "
- "-[AFPreferences assistantIsEnabled]"
- "-[AFSettingsConnection(Internal) _isDisablingDictationOnlySyncSupported:]_block_invoke"
- "-[AFSettingsConnection(Internal) _isSiriVocabularyNotificationForAddressBookSyncSupported:]_block_invoke"
- "@84@0:8@16q24B32B36B40B44f48@52@60@68@76"
- "_isDisablingDictationOnlySyncSupported:"
- "_isSiriVocabularyNotificationForAddressBookSyncSupported:"
- "_latMitRes"
- "initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:"
- "{NSDecimalNumber=#b8b4b1b1b1b1b16[0S]}"
- "{_mutationFlags=\"isDirty\"b1\"hasAccessibilityState\"b1\"hasDeviceRingerSwitchState\"b1\"hasIsDeviceInCarDNDMode\"b1\"hasIsDeviceInStarkMode\"b1\"hasIsDeviceWatchAuthenticated\"b1\"hasAreAnnouncementRequestsPermittedByPresentationWhileActive\"b1\"hasOutputVolume\"b1\"hasTapToSiriAudioPlaybackRequest\"b1\"hasTwoShotAudioPlaybackRequest\"b1\"hasDeviceSetupFlowBeginDate\"b1\"hasDeviceSetupFlowEndDate\"b1}"

```
