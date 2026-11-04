## AssistantServices

> `/System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices`

```diff

-3605.31.1.11.2
-  __TEXT.__text: 0x198898
-  __TEXT.__objc_methlist: 0x1f544
+3610.11.2.0.0
+  __TEXT.__text: 0x19dc98
+  __TEXT.__objc_methlist: 0x1f704
   __TEXT.__const: 0x3d0
   __TEXT.__dlopen_cstrs: 0x538
-  __TEXT.__gcc_except_tab: 0x21e0
-  __TEXT.__cstring: 0x3ded9
-  __TEXT.__oslogstring: 0xfd05
+  __TEXT.__gcc_except_tab: 0x22e4
+  __TEXT.__cstring: 0x3e593
+  __TEXT.__oslogstring: 0x10683
   __TEXT.__ustring: 0x2ac
-  __TEXT.__unwind_info: 0xa020
+  __TEXT.__unwind_info: 0xa170
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x87c0
+  __DATA_CONST.__const: 0x8890
   __DATA_CONST.__objc_classlist: 0xf00
   __DATA_CONST.__objc_catlist: 0x2a8
   __DATA_CONST.__objc_protolist: 0x608
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc320
+  __DATA_CONST.__objc_selrefs: 0xc438
   __DATA_CONST.__objc_protorefs: 0x178
   __DATA_CONST.__objc_superrefs: 0xf18
-  __DATA_CONST.__objc_arraydata: 0x2450
-  __DATA_CONST.__got: 0x1700
-  __AUTH_CONST.__const: 0x3e00
-  __AUTH_CONST.__cfstring: 0x28a40
-  __AUTH_CONST.__objc_const: 0x368c8
+  __DATA_CONST.__objc_arraydata: 0x2458
+  __DATA_CONST.__got: 0x1828
+  __AUTH_CONST.__const: 0x3ec0
+  __AUTH_CONST.__cfstring: 0x28cc0
+  __AUTH_CONST.__objc_const: 0x36ad8
   __AUTH_CONST.__objc_intobj: 0x2730
   __AUTH_CONST.__objc_dictobj: 0xd20
-  __AUTH_CONST.__objc_arrayobj: 0x5d0
+  __AUTH_CONST.__objc_arrayobj: 0x5e8
   __AUTH_CONST.__objc_doubleobj: 0x40
-  __AUTH_CONST.__auth_got: 0xae0
+  __AUTH_CONST.__auth_got: 0xb00
   __AUTH.__objc_data: 0x84f8
-  __AUTH.__data: 0x280
-  __DATA.__objc_ivar: 0x25c8
+  __AUTH.__data: 0x278
+  __AUTH.__thread_vars: 0x30
+  __AUTH.__thread_bss: 0x10
+  __DATA.__objc_ivar: 0x25fc
   __DATA.__data: 0x4988
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x1108

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/FaceTimeNameUtility.framework/FaceTimeNameUtility
   - /System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger
+  - /System/Library/PrivateFrameworks/GenerativeModels.framework/GenerativeModels
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 12257
-  Symbols:   22458
-  CStrings:  8715
+  Functions: 12346
+  Symbols:   22626
+  CStrings:  8793
 
Symbols:
+ +[AFFeatureFlags(SWEFeatureFlags) emergencyOrchestrationModeEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isDeviceSelectionShadowModeEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) isHomePodASRStartOnActivationEnabled]
+ +[AFFeatureFlags(SWEFeatureFlags) linwoodEnabledForCandidateHomePods]
+ +[AFFeatureFlags(SWEFeatureFlags) linwoodEnabledForHomePod2ndGen]
+ +[AFFeatureFlags(SWEFeatureFlags) visualStandbyEnabled]
+ -[AFClientConfiguration carOwnsCommunication]
+ -[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:carOwnsMainAudio:isEyesFreeDevice:carOwnsCommunication:]
+ -[AFConnection _exchangeInputAudioPowerUpdater:]
+ -[AFConnection _inputAudioPowerUpdaterForPolling]
+ -[AFConnection _rejectsCallDuringDealloc:]
+ -[AFConnection _removeSharedObserverListeners]
+ -[AFConnection setCarOwnsCommunication:]
+ -[AFDeviceContextConnection _endUpdateLocalDeviceContextForGeneration:]
+ -[AFDictationConnection _exchangeInputAudioPowerUpdater:]
+ -[AFDictationConnection _inputAudioPowerUpdaterForPolling]
+ -[AFPluginManager _factoryInstanceForPlugin:]
+ -[AFPluginManager _loadBundlesIntoDomainKeyDictionary:]
+ -[AFPluginManager _publishDomainKeyDictionary:]
+ -[AFPluginManager _registerBundle:inDomainKeyDictionary:]
+ -[AFPreferences _AFPublicPreferencesSetValue:forKey:]
+ -[AFPreferences _AFPublicPreferencesValueForKey:]
+ -[AFPreferences getMessageWithoutConfirmationHomeEnabled]
+ -[AFPreferences setMessageWithoutConfirmationHomeEnabled:]
+ -[AFPreferences(Accessibility) companionLinwoodCapableIgnoringUserSetting]
+ -[AFPreferences(Accessibility) setCompanionLinwoodCapableIgnoringUserSetting:]
+ -[AFSpeakableUtteranceParser _currentDateForFunctions]
+ -[AFSpeakableUtteranceParser _setCurrentDateForTesting:]
+ -[AFSystemAssistantExperienceStatusManager availabilityProviderForTesting]
+ -[AFSystemAssistantExperienceStatusManager setAvailabilityProviderForTesting:]
+ -[AFUIApplicationSiriTaskDeliverer _invalidateAppStateMonitor]
+ -[AFUIApplicationSiriTaskDeliverer _invalidateProcessAssertion]
+ -[AFWatchdogTimer _cancelLocked]
+ -[AFWatchdogTimer _startLocked]
+ -[AFWatchdogTimer _stopLocked]
+ -[AFWatchdogTimer _timeRemainingLocked]
+ -[_AFClientConfigurationMutation getCarOwnsCommunication]
+ -[_AFClientConfigurationMutation setCarOwnsCommunication:]
+ GCC_except_table10004
+ GCC_except_table10009
+ GCC_except_table10139
+ GCC_except_table10349
+ GCC_except_table10389
+ GCC_except_table10420
+ GCC_except_table10425
+ GCC_except_table10426
+ GCC_except_table10430
+ GCC_except_table10619
+ GCC_except_table10790
+ GCC_except_table10819
+ GCC_except_table10916
+ GCC_except_table10920
+ GCC_except_table10924
+ GCC_except_table10953
+ GCC_except_table11307
+ GCC_except_table11309
+ GCC_except_table1131
+ GCC_except_table11312
+ GCC_except_table11324
+ GCC_except_table11394
+ GCC_except_table11415
+ GCC_except_table11440
+ GCC_except_table11446
+ GCC_except_table11605
+ GCC_except_table11609
+ GCC_except_table11611
+ GCC_except_table11614
+ GCC_except_table11620
+ GCC_except_table11624
+ GCC_except_table11630
+ GCC_except_table11837
+ GCC_except_table1197
+ GCC_except_table1203
+ GCC_except_table12161
+ GCC_except_table12295
+ GCC_except_table12298
+ GCC_except_table12300
+ GCC_except_table1324
+ GCC_except_table1327
+ GCC_except_table1509
+ GCC_except_table1552
+ GCC_except_table1558
+ GCC_except_table1578
+ GCC_except_table1584
+ GCC_except_table1587
+ GCC_except_table1953
+ GCC_except_table2067
+ GCC_except_table2199
+ GCC_except_table2336
+ GCC_except_table2348
+ GCC_except_table2355
+ GCC_except_table2356
+ GCC_except_table2359
+ GCC_except_table2365
+ GCC_except_table2412
+ GCC_except_table2414
+ GCC_except_table2416
+ GCC_except_table2434
+ GCC_except_table2440
+ GCC_except_table2483
+ GCC_except_table2495
+ GCC_except_table2644
+ GCC_except_table265
+ GCC_except_table2732
+ GCC_except_table2786
+ GCC_except_table3023
+ GCC_except_table3026
+ GCC_except_table3027
+ GCC_except_table3224
+ GCC_except_table3283
+ GCC_except_table3498
+ GCC_except_table3513
+ GCC_except_table3514
+ GCC_except_table3527
+ GCC_except_table3528
+ GCC_except_table3529
+ GCC_except_table3535
+ GCC_except_table3573
+ GCC_except_table3579
+ GCC_except_table3585
+ GCC_except_table3653
+ GCC_except_table3655
+ GCC_except_table3690
+ GCC_except_table3693
+ GCC_except_table373
+ GCC_except_table3804
+ GCC_except_table3867
+ GCC_except_table3869
+ GCC_except_table3871
+ GCC_except_table3873
+ GCC_except_table3887
+ GCC_except_table3893
+ GCC_except_table392
+ GCC_except_table397
+ GCC_except_table4018
+ GCC_except_table4022
+ GCC_except_table4027
+ GCC_except_table4404
+ GCC_except_table4419
+ GCC_except_table4426
+ GCC_except_table4442
+ GCC_except_table4511
+ GCC_except_table4520
+ GCC_except_table4550
+ GCC_except_table4588
+ GCC_except_table4589
+ GCC_except_table4590
+ GCC_except_table4615
+ GCC_except_table4639
+ GCC_except_table4999
+ GCC_except_table5004
+ GCC_except_table5007
+ GCC_except_table5010
+ GCC_except_table5013
+ GCC_except_table5016
+ GCC_except_table5019
+ GCC_except_table5022
+ GCC_except_table5025
+ GCC_except_table5028
+ GCC_except_table5058
+ GCC_except_table5204
+ GCC_except_table5207
+ GCC_except_table5268
+ GCC_except_table5276
+ GCC_except_table5281
+ GCC_except_table5294
+ GCC_except_table5638
+ GCC_except_table5651
+ GCC_except_table5655
+ GCC_except_table5667
+ GCC_except_table5671
+ GCC_except_table5784
+ GCC_except_table5786
+ GCC_except_table5864
+ GCC_except_table5908
+ GCC_except_table603
+ GCC_except_table6275
+ GCC_except_table6282
+ GCC_except_table6288
+ GCC_except_table6290
+ GCC_except_table6292
+ GCC_except_table6344
+ GCC_except_table6346
+ GCC_except_table6352
+ GCC_except_table6357
+ GCC_except_table6361
+ GCC_except_table6367
+ GCC_except_table6374
+ GCC_except_table6376
+ GCC_except_table6381
+ GCC_except_table6383
+ GCC_except_table6388
+ GCC_except_table6400
+ GCC_except_table6403
+ GCC_except_table6417
+ GCC_except_table6419
+ GCC_except_table6421
+ GCC_except_table6423
+ GCC_except_table6425
+ GCC_except_table6427
+ GCC_except_table6429
+ GCC_except_table6476
+ GCC_except_table6502
+ GCC_except_table654
+ GCC_except_table6559
+ GCC_except_table6615
+ GCC_except_table7022
+ GCC_except_table7170
+ GCC_except_table7315
+ GCC_except_table7553
+ GCC_except_table7562
+ GCC_except_table7580
+ GCC_except_table7955
+ GCC_except_table7959
+ GCC_except_table8004
+ GCC_except_table8010
+ GCC_except_table8035
+ GCC_except_table8041
+ GCC_except_table8263
+ GCC_except_table8372
+ GCC_except_table8383
+ GCC_except_table8416
+ GCC_except_table8419
+ GCC_except_table8496
+ GCC_except_table8500
+ GCC_except_table8510
+ GCC_except_table8521
+ GCC_except_table8534
+ GCC_except_table858
+ GCC_except_table8619
+ GCC_except_table8621
+ GCC_except_table8645
+ GCC_except_table865
+ GCC_except_table8768
+ GCC_except_table8831
+ GCC_except_table8834
+ GCC_except_table8838
+ GCC_except_table8855
+ GCC_except_table8869
+ GCC_except_table8945
+ GCC_except_table9003
+ GCC_except_table9029
+ GCC_except_table9056
+ GCC_except_table9310
+ GCC_except_table9470
+ GCC_except_table9515
+ GCC_except_table9611
+ GCC_except_table9715
+ GCC_except_table9815
+ GCC_except_table996
+ _AFDeviceSelectionExcludedHomePod
+ _AFDeviceSelectionParticipating
+ _AFDictionarySchemaFailingKeyPath
+ _AFIsAppleDictationClientSigningIdentity
+ _AFIsHomeAccessory
+ _AFIsSupportedHomePodForLinwood
+ _AFMyriadElectionActivationKindForSpeechEvent
+ _AFObjectsAreEqual
+ _AFPluginManagerLoadsOnCurrentThread
+ _AFPluginManagerLoadsOnCurrentThread$tlv$init
+ _AFPreferencesDeviceOwnerTwentyFourHourTimeDisplay
+ _AFPreferencesSetDeviceOwnerTwentyFourHourTimeDisplay
+ _AFPublicPreferencesSynchronize
+ _AFRemotePeerCommandDispositionForAceCommand
+ _AFRemotePeerCommandDispositionForResolvedAceCommand
+ _AFRemotePeerCommandDispositionGetName
+ _AFSetPendingDictationContinuationDrainedHandlerForTesting
+ _AFSetSiriTaskDeliveryTimeoutForTesting
+ _AFSiriTaskmasterQueueKey
+ _AFSpeakableUtteranceParserNestingDepth
+ _AFSpeakableUtteranceParserNestingDepth$tlv$init
+ _AFSpeechRecognitionArrayHash
+ _AFSpeechRecognitionArrayOfClass
+ _AFSpeechTokenArrayOfClass
+ _AFUserUtteranceInterpretationIndices
+ _OBJC_CLASS_$_GMAvailabilityWrapper
+ _OBJC_IVAR_$_AFAudioPowerUpdater._providerLock
+ _OBJC_IVAR_$_AFClientConfiguration._carOwnsCommunication
+ _OBJC_IVAR_$_AFConnection._deallocInProgress
+ _OBJC_IVAR_$_AFConnection._inputAudioPowerUpdaterLock
+ _OBJC_IVAR_$_AFDeviceContextConnection._localDeviceContextUpdateGeneration
+ _OBJC_IVAR_$_AFDictationConnection._didLogUnreadableOfflineDictationStatus
+ _OBJC_IVAR_$_AFDictationConnection._inputAudioPowerUpdaterLock
+ _OBJC_IVAR_$_AFPluginManager._bundlesLock
+ _OBJC_IVAR_$_AFPluginManager._factoryInstanceLock
+ _OBJC_IVAR_$_AFSiriTaskExecution._taskDeliveryWatchdogTimer
+ _OBJC_IVAR_$_AFSpeakableUtteranceParser._currentDateForTesting
+ _OBJC_IVAR_$_AFSystemAssistantExperienceStatusManager._availabilityProviderForTesting
+ _OBJC_IVAR_$__AFClientConfigurationMutation._carOwnsCommunication
+ _SAABMultiPersonSearchClassIdentifier
+ _SAABPersonSearchClassIdentifier
+ _SAAcknowledgeAlertClassIdentifier
+ _SACalendarDefaultSourceGetClassIdentifier
+ _SACalendarEventSearchClassIdentifier
+ _SACalendarGroupIdentifier
+ _SADeviceControlGroupIdentifier
+ _SADomainObjectCancelClassIdentifier
+ _SADomainObjectCommitClassIdentifier
+ _SADomainObjectCreateClassIdentifier
+ _SADomainObjectDeleteClassIdentifier
+ _SADomainObjectPunchOutClassIdentifier
+ _SADomainObjectRetrieveClassIdentifier
+ _SADomainObjectUpdateClassIdentifier
+ _SAEmailGroupIdentifier
+ _SAEmailSearchClassIdentifier
+ _SAGroupIdentifier
+ _SAHAGroupIdentifier
+ _SAPhoneCallClassIdentifier
+ _SAPhoneGroupIdentifier
+ _SAPhoneSearchClassIdentifier
+ _SAReminderGroupIdentifier
+ _SAReminderListSearchClassIdentifier
+ _SAReminderSearchClassIdentifier
+ _SAReminderSnoozeClassIdentifier
+ _SASettingGroupIdentifier
+ _SASmsGroupIdentifier
+ _SASmsGroupSearchClassIdentifier
+ _SASmsRecipientSearchClassIdentifier
+ _SASmsSearchClassIdentifier
+ _SAStockAddClassIdentifier
+ _SAStockGroupIdentifier
+ _SAStockSearchClassIdentifier
+ _SAUILGroupIdentifier
+ _SAUILParseExpressionsClassIdentifier
+ _SecTaskGetCodeSignStatus
+ __AFAVFAudioFrameworkPath
+ __AFAceDictionaryHasGroupAndClass
+ __AFGetAVAudioSessionClass
+ __AFMigratedPreferencesQueue
+ __AFMigratedPreferencesQueue.onceToken
+ __AFMigratedPreferencesQueue.queue
+ __AFPreferencesGetMessageWithoutConfirmationHomeEnabled
+ __AFPreferencesInvalidateLanguageCaches
+ __AFPreferencesLanguageObserverRegistrationAttemptsForTesting
+ __AFPreferencesLongLivedIdentifierUploadingEnabledWithPreferences
+ __AFPreferencesMigrateToPublicDomainIfNeeded
+ __AFPreferencesSetLanguageBackedUpReaderForTesting
+ __AFPreferencesSetLanguageBackedUpSynchronizerForTesting
+ __AFPreferencesSetLanguageIsInternalInstallOverrideForTesting
+ __AFPreferencesSetMessageWithoutConfirmationHomeEnabled
+ __AFPreferencesSyncMigratedDefaultsToPublicDomain
+ __AFPreferencesSyncMigratedDefaultsToPublicDomainOnQueue
+ __AFPublicPreferencesBoolForKeyWithDefault
+ __AFPublicPreferencesBoolValueForKey
+ __AFPublicPreferencesSetValueForKey
+ __AFPublicPreferencesSetValueForKeyWithContext
+ __AFPublicPreferencesValueForKey
+ __AFPublicPreferencesValueForKeyWithContext
+ __AFRemotePeerAllowedCommands.onceToken
+ __AFRemotePeerAllowedCommands.sAllowedCommands
+ __AFRemotePeerCommandDispositionForResolvedGroupAndClass
+ __AFRemotePeerRefusedGroups.onceToken
+ __AFRemotePeerRefusedGroups.sRefusedGroups
+ __AFSiriAvailabilityValue
+ __AFSoftLinkOptionalClass
+ __OBJC_$_CLASS_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFSiriRequest|AFPreferences|AssistantServices|ShortDescription)
+ __OBJC_$_CLASS_METHODS_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
+ __OBJC_$_INSTANCE_METHODS_AFClockAlarmSnapshot(AFClockAlarmSnapshotMutability|Utility|ShortDescription|ContextSnapshot)
+ __OBJC_$_INSTANCE_METHODS_AFClockTimerSnapshot(AFClockTimerSnapshotMutability|Utility|ShortDescription|ContextSnapshot)
+ __OBJC_$_INSTANCE_METHODS_AFLocationSnapshot(AFLocationSnapshotMutability|Ace|ShortDescription|ContextSnapshot)
+ __OBJC_$_INSTANCE_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFSiriRequest|AFPreferences|AssistantServices|ShortDescription)
+ __OBJC_$_INSTANCE_METHODS_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
+ __OBJC_CLASS_PROTOCOLS_$_AFClockAlarmSnapshot(AFClockAlarmSnapshotMutability|Utility|ShortDescription|ContextSnapshot)
+ __OBJC_CLASS_PROTOCOLS_$_AFClockTimerSnapshot(AFClockTimerSnapshotMutability|Utility|ShortDescription|ContextSnapshot)
+ __OBJC_CLASS_PROTOCOLS_$_AFLocationSnapshot(AFLocationSnapshotMutability|Ace|ShortDescription|ContextSnapshot)
+ __OBJC_CLASS_PROTOCOLS_$_NSURL(AFSecurityDigestibleChunksProvider|STSiriMessage|AFBundleResourceSupport|AMOSExtensions)
+ ___118-[AFDeviceContextConnection donateSerializedContextMapByPrivacyClass:withMetadataMap:forType:pushToRemote:completion:]_block_invoke_2
+ ___40-[AFConnection setCarOwnsCommunication:]_block_invoke
+ ___403-[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:carOwnsMainAudio:isEyesFreeDevice:carOwnsCommunication:]_block_invoke
+ ___41-[AFSiriAvailability initWithDictionary:]_block_invoke
+ ___48-[AFDeviceContextMetadata initWithBackingStore:]_block_invoke
+ ___58-[AFSiriTaskmaster handleSiriTaskUsageResult:fromRequest:]_block_invoke
+ ___68-[AFDeviceContextConnection _fetchLocalDeviceContextWithCompletion:]_block_invoke_2
+ ____AFMigratedPreferencesQueue_block_invoke
+ ____AFPreferencesMigrateToPublicDomainIfNeeded_block_invoke
+ ____AFPreferencesSyncMigratedDefaultsToPublicDomain_block_invoke
+ ____AFRemotePeerAllowedCommands_block_invoke
+ ____AFRemotePeerRefusedGroups_block_invoke
+ ____AFSetAudioSessionActiveResultCreateDeallocated_block_invoke
+ ___block_descriptor_32_e18_"NSString"16?08l
+ ___block_descriptor_40_e8_32s_e45_"NSNumber"24?0"NSDictionary"8"NSString"16ls32l8
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
+ ___block_descriptor_48_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_56_e8_32s40r48w_e25_v16?0"AFDeviceContext"8lw48l8r40l8s32l8
+ ___block_descriptor_56_e8_32s40s48r_e25_v32?0"NSNumber"8Q16^B24ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48r_e31_v16?0"NSXPCListenerEndpoint"8ls32l8r48l8s40l8
+ ___block_descriptor_92_e8_32s40s48s56s64s_e41_v16?0"<AFClientConfigurationMutating>"8ls32l8s40l8s48l8s56l8s64l8
+ __tlv_bootstrap
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _kAFAppleIntelligenceFallbackEnabledKey
+ _kAFDictationSLSEnabledKey
+ _kAFDictationSLSLanguagesEnabledKey
+ _kAFDisplayedLowStorageNotificationStatus
+ _kAFMessageWithoutConfirmationHomeKey
+ _kAFOfflineDictationStatusKey
+ _kAFPublicPreferencesMigratedKey
+ _kAFRemotePeerDeliveredCommandKey
+ _kAFRemotePeerDeliveredCommandValue
+ _kAssistantPublicPreferenceDomain
+ _objc_setProperty_atomic_copy
+ _sAFPendingDictationContinuationDrainedHandler
+ _sLanguageBackedUpReaderForTesting
+ _sLanguageBackedUpSynchronizerForTesting
+ _sLanguageIsInternalInstallOverrideForTesting
+ _sLanguageObserverRegistrationAttemptsForTesting
+ _s_deliveryTimeoutOverride
- -[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:carOwnsMainAudio:isEyesFreeDevice:]
- -[AFPluginManager _registerBundle:]
- GCC_except_table10058
- GCC_except_table10266
- GCC_except_table10306
- GCC_except_table10337
- GCC_except_table10342
- GCC_except_table10343
- GCC_except_table10347
- GCC_except_table10536
- GCC_except_table10707
- GCC_except_table10736
- GCC_except_table10833
- GCC_except_table10837
- GCC_except_table10841
- GCC_except_table10870
- GCC_except_table1121
- GCC_except_table11224
- GCC_except_table11226
- GCC_except_table11229
- GCC_except_table11238
- GCC_except_table11304
- GCC_except_table11325
- GCC_except_table11350
- GCC_except_table11356
- GCC_except_table11515
- GCC_except_table11519
- GCC_except_table11521
- GCC_except_table11524
- GCC_except_table11530
- GCC_except_table11534
- GCC_except_table11540
- GCC_except_table11747
- GCC_except_table1187
- GCC_except_table1193
- GCC_except_table12071
- GCC_except_table12205
- GCC_except_table12208
- GCC_except_table12210
- GCC_except_table1314
- GCC_except_table1316
- GCC_except_table1497
- GCC_except_table1534
- GCC_except_table1540
- GCC_except_table1566
- GCC_except_table1572
- GCC_except_table1575
- GCC_except_table1941
- GCC_except_table2055
- GCC_except_table2186
- GCC_except_table2309
- GCC_except_table2323
- GCC_except_table2342
- GCC_except_table2343
- GCC_except_table2346
- GCC_except_table2352
- GCC_except_table2399
- GCC_except_table2401
- GCC_except_table2403
- GCC_except_table2421
- GCC_except_table2427
- GCC_except_table2470
- GCC_except_table2482
- GCC_except_table264
- GCC_except_table2725
- GCC_except_table2738
- GCC_except_table2742
- GCC_except_table2754
- GCC_except_table2758
- GCC_except_table2871
- GCC_except_table2873
- GCC_except_table2951
- GCC_except_table2995
- GCC_except_table3361
- GCC_except_table3368
- GCC_except_table3374
- GCC_except_table3376
- GCC_except_table3378
- GCC_except_table3423
- GCC_except_table3425
- GCC_except_table3431
- GCC_except_table3437
- GCC_except_table3441
- GCC_except_table3447
- GCC_except_table3454
- GCC_except_table3456
- GCC_except_table3461
- GCC_except_table3463
- GCC_except_table3468
- GCC_except_table3480
- GCC_except_table3483
- GCC_except_table3497
- GCC_except_table3499
- GCC_except_table3503
- GCC_except_table3505
- GCC_except_table3507
- GCC_except_table3509
- GCC_except_table3555
- GCC_except_table3581
- GCC_except_table3638
- GCC_except_table366
- GCC_except_table3674
- GCC_except_table385
- GCC_except_table389
- GCC_except_table4079
- GCC_except_table4368
- GCC_except_table4569
- GCC_except_table4577
- GCC_except_table4635
- GCC_except_table5011
- GCC_except_table5015
- GCC_except_table5060
- GCC_except_table5066
- GCC_except_table5091
- GCC_except_table5097
- GCC_except_table5312
- GCC_except_table5421
- GCC_except_table5432
- GCC_except_table5465
- GCC_except_table5468
- GCC_except_table5545
- GCC_except_table5549
- GCC_except_table5559
- GCC_except_table5570
- GCC_except_table5583
- GCC_except_table5668
- GCC_except_table5670
- GCC_except_table5694
- GCC_except_table5810
- GCC_except_table5873
- GCC_except_table5876
- GCC_except_table5880
- GCC_except_table5897
- GCC_except_table5911
- GCC_except_table593
- GCC_except_table5985
- GCC_except_table6043
- GCC_except_table6069
- GCC_except_table6348
- GCC_except_table644
- GCC_except_table6494
- GCC_except_table6507
- GCC_except_table6552
- GCC_except_table6646
- GCC_except_table6831
- GCC_except_table6917
- GCC_except_table6971
- GCC_except_table7207
- GCC_except_table7210
- GCC_except_table7211
- GCC_except_table7408
- GCC_except_table7467
- GCC_except_table7681
- GCC_except_table7684
- GCC_except_table7696
- GCC_except_table7697
- GCC_except_table7710
- GCC_except_table7711
- GCC_except_table7712
- GCC_except_table7718
- GCC_except_table7756
- GCC_except_table7762
- GCC_except_table7768
- GCC_except_table7836
- GCC_except_table7838
- GCC_except_table7873
- GCC_except_table7876
- GCC_except_table7987
- GCC_except_table8050
- GCC_except_table8052
- GCC_except_table8054
- GCC_except_table8056
- GCC_except_table8070
- GCC_except_table8076
- GCC_except_table8201
- GCC_except_table8205
- GCC_except_table8210
- GCC_except_table845
- GCC_except_table848
- GCC_except_table8587
- GCC_except_table8602
- GCC_except_table8609
- GCC_except_table8625
- GCC_except_table8694
- GCC_except_table8703
- GCC_except_table8733
- GCC_except_table8771
- GCC_except_table8772
- GCC_except_table8773
- GCC_except_table8798
- GCC_except_table8822
- GCC_except_table9182
- GCC_except_table9187
- GCC_except_table9190
- GCC_except_table9193
- GCC_except_table9196
- GCC_except_table9199
- GCC_except_table9202
- GCC_except_table9205
- GCC_except_table9208
- GCC_except_table9211
- GCC_except_table9384
- GCC_except_table9387
- GCC_except_table9448
- GCC_except_table9461
- GCC_except_table9474
- GCC_except_table9634
- GCC_except_table9734
- GCC_except_table986
- GCC_except_table9923
- GCC_except_table9928
- _AVAudioSessionFunction
- _AVFAudioLibrary.frameworkLibrary
- __OBJC_$_CLASS_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFPreferences|AssistantServices|AFSiriRequest|ShortDescription)
- __OBJC_$_CLASS_METHODS_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
- __OBJC_$_INSTANCE_METHODS_AFClockAlarmSnapshot(Utility|AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_$_INSTANCE_METHODS_AFClockTimerSnapshot(Utility|AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_$_INSTANCE_METHODS_AFLocationSnapshot(Ace|AFLocationSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_$_INSTANCE_METHODS_NSString(AFSecurityDigestibleChunksProvider|AFPreferences|AssistantServices|AFSiriRequest|ShortDescription)
- __OBJC_$_INSTANCE_METHODS_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
- __OBJC_CLASS_PROTOCOLS_$_AFClockAlarmSnapshot(Utility|AFClockAlarmSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_CLASS_PROTOCOLS_$_AFClockTimerSnapshot(Utility|AFClockTimerSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_CLASS_PROTOCOLS_$_AFLocationSnapshot(Ace|AFLocationSnapshotMutability|ShortDescription|ContextSnapshot)
- __OBJC_CLASS_PROTOCOLS_$_NSURL(AFSecurityDigestibleChunksProvider|AFBundleResourceSupport|AMOSExtensions|STSiriMessage)
- ___28-[AFSiriTaskExecution start]_block_invoke_3
- ___382-[AFClientConfiguration initWithAccessibilityState:deviceRingerSwitchState:isDeviceInCarDNDMode:isDeviceInStarkMode:supportsCarPlayVehicleData:isDeviceWatchAuthenticated:areAnnouncementRequestsPermittedByPresentationWhileActive:outputVolume:tapToSiriAudioPlaybackRequest:twoShotAudioPlaybackRequest:deviceSetupFlowBeginDate:deviceSetupFlowEndDate:carOwnsMainAudio:isEyesFreeDevice:]_block_invoke
- ___82-[AFDictationConnection forcedOfflineDictationIsAvailableForLanguage:synchronous:]_block_invoke_2
- ___83+[SASSpeechPartialResult(AFSpeechTokenAdditions) createUsingPhrases:andUtterances:]_block_invoke
- ___block_descriptor_48_e8_32bs40w_e25_v16?0"AFDeviceContext"8lw40l8s32l8
- ___block_descriptor_48_e8_32bs40w_e5_v8?0ls32l8w40l8
- ___block_descriptor_48_e8_32r40r_e15_v32?08Q16^B24lr32l8r40l8
- ___block_descriptor_48_e8_32s40bs_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e25_v32?0"NSNumber"8Q16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e31_v16?0"NSXPCListenerEndpoint"8lr48l8s32l8s40l8
- ___block_descriptor_91_e8_32s40s48s56s64s_e41_v16?0"<AFClientConfigurationMutating>"8ls32l8s40l8s48l8s56l8s64l8
- ___initAVAudioSession_block_invoke
- _classAVAudioSession
- _getAVAudioSessionClass
- _initAVAudioSession
- _initAVAudioSession.sOnce
CStrings:
+ "$class"
+ "$group"
+ "%@ (%@)"
+ "%@ {accessibilityState = %@, deviceRingerSwitchState = %@, isDeviceInCarDNDMode = %@, isDeviceInStarkMode = %@, supportsCarPlayVehicleData = %@, isDeviceWatchAuthenticated = %@, areAnnouncementRequestsPermittedByPresentationWhileActive = %@, outputVolume = %f, tapToSiriAudioPlaybackRequest = %@, twoShotAudioPlaybackRequest = %@, deviceSetupFlowBeginDate = %@, deviceSetupFlowEndDate = %@, carOwnsMainAudio = %@, isEyesFreeDevice = %@, carOwnsCommunication = %@}"
+ "%s #Montara restrictions in China, mdm: false, AFMontaraRestricted: false."
+ "%s #SiriAvailability ignored %lu wrong-typed value(s): %{public}@"
+ "%s %p Ignored because generation %lu is not the current one (%lu)."
+ "%s %p No offline dictation status; reporting unavailable, will retry"
+ "%s %p generation = %lu"
+ "%s %p ignoring %{public}@ during dealloc"
+ "%s %p not creating a connection during dealloc"
+ "%s %{public}lu of %{public}lu server utterances have interpretation indices that do not fit the %{public}lu phrases; they are left out"
+ "%s %{public}s has no class %{public}s"
+ "%s +provider called on %@ but the shared instance is a %@"
+ "%s Called back while loading bundles from \"%@\"; no bundles are available yet"
+ "%s Could not load %{public}s for %{public}s: %{public}s"
+ "%s Delivery of %@ timed out after %{public}.2f seconds"
+ "%s Dropping punchout outcome: result=%@ has description %@, request=%@ has name %@"
+ "%s Ignoring an utterance that is not an AFSpeechUtterance"
+ "%s Ignoring phrases that are not an array of AFSpeechPhrase"
+ "%s Ignoring utterance interpretationIndices that are not an array"
+ "%s Ignoring utterance interpretationIndices with a non-number index"
+ "%s Ignoring utterance whose interpretation index %{public}lu at phrase %{public}lu is past its %{public}lu interpretations"
+ "%s Ignoring utterance whose interpretation indices are not an array"
+ "%s Ignoring utterance whose phrase %{public}lu has interpretations that are not an array of AFSpeechInterpretation"
+ "%s Ignoring utterance whose selected interpretation at phrase %{public}lu has tokens that are not an array of AFSpeechToken"
+ "%s Ignoring utterance with %{public}lu interpretation indices for %{public}lu phrases"
+ "%s Ignoring utterance with a non-number interpretation index"
+ "%s Ignoring utterances that are not an array of AFSpeechUtterance"
+ "%s No delegate on %@; punchout outcome %@ is being discarded"
+ "%s No plugin bundles at path \"%@\":%@"
+ "%s Not treating %{public}@ as an Apple client: code sign status 0x%x is not a valid platform binary, or the identifier does not start with com.apple."
+ "%s Pending dictation request was refused; there is nothing to continue"
+ "%s Siri plugin %@ has a non-array %@ entry, ignoring it"
+ "%s Siri plugin %@ has a non-string %@ identifier, ignoring it"
+ "%s passed invalid property list (%{public}@ %ld at %{public}@, %{public}@ with %lu keys): %{private}@"
+ "%s returning nil; passed invalid property list (%{public}@ %ld at %{public}@, %{public}@ with %lu keys): %{private}@"
+ "%s returning nil; unable to create associated data store from property list"
+ "%s utterance has %{public}lu interpretationIndices for %{public}lu phrases"
+ "%s utterance interpretationIndex (%{public}lu) is out of range of %{public}lu interpretations"
+ "(dictionary) (%@)"
+ "(elided: not on the taskmaster queue)"
+ "(none)"
+ "+[AFCarPlayAnnouncementRequestCapabilityProvider provider]"
+ "+[AFHeadphonesAnnouncementRequestCapabilityProvider provider]"
+ "+[AFSpeechRecognition tokenListFromUtterance:phrases:]"
+ "-[AFConnection _connection]"
+ "-[AFConnection _rejectsCallDuringDealloc:]"
+ "-[AFConnection acquireAudioSessionWithContext:completion:]_block_invoke_2"
+ "-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke_3"
+ "-[AFDeviceContextConnection _endUpdateLocalDeviceContextForGeneration:]"
+ "-[AFDeviceContextConnection _fetchLocalDeviceContextWithCompletion:]_block_invoke_2"
+ "-[AFDictationConnection forcedOfflineDictationIsAvailableForLanguage:synchronous:]"
+ "-[AFPluginManager _loadBundlesIntoDomainKeyDictionary:]"
+ "-[AFPluginManager _registerBundle:inDomainKeyDictionary:]"
+ "-[AFSiriAvailability initWithDictionary:]"
+ "-[AFSiriTaskExecution start]_block_invoke_2"
+ "-[AFSiriTaskmaster handleSiriTaskUsageResult:fromRequest:]_block_invoke"
+ "-[AFSpeechRecognition nBestTokenListsFromSausage]"
+ "-[AFSpeechRecognition oneBestTokenList]"
+ "-[AFUserUtterance interpretationOfUtteranceAtIndex:]_block_invoke"
+ "-[SASRecognition(AFSpeechTokenAdditions) af_speechUtterances]"
+ "/System/Library/Frameworks/AVFAudio.framework/AVFAudio"
+ "@\"NSNumber\"24@?0@\"NSDictionary\"8@\"NSString\"16"
+ "@\"NSString\"16@?0@8"
+ "AFClientConfiguration::carOwnsCommunication"
+ "AFDictionarySchemaFailingKeyPath"
+ "AFRemotePeerDeliveredCommand"
+ "AFUserUtteranceInterpretationIndices"
+ "CompanionLinwoodCapableIgnoringUserSetting"
+ "Device Owner Twenty Four Hour Time Display"
+ "Emergency"
+ "LinwoodChinaMainland"
+ "Message Without Confirmation Home"
+ "Public Preferences Migrated"
+ "Standby"
+ "_AFPreferencesSetMessageWithoutConfirmationHomeEnabled"
+ "_AFPublicPreferencesBoolValueForKey"
+ "_AFSoftLinkOptionalClass"
+ "allow"
+ "allow (logged)"
+ "carOwnsCommunication"
+ "com.apple."
+ "com.apple.assistant.preferences.public-domain-migration"
+ "com.apple.assistant.public"
+ "device_selection_shadow"
+ "emergency_orchestration_mode"
+ "homepod_asr_start_on_activation"
+ "linwood_enabled_for_candidate_homepods"
+ "linwood_enabled_for_homepod_2ndgen"
+ "refuse"
+ "\xf0\xf0\xf02"
- "%@ {accessibilityState = %@, deviceRingerSwitchState = %@, isDeviceInCarDNDMode = %@, isDeviceInStarkMode = %@, supportsCarPlayVehicleData = %@, isDeviceWatchAuthenticated = %@, areAnnouncementRequestsPermittedByPresentationWhileActive = %@, outputVolume = %f, tapToSiriAudioPlaybackRequest = %@, twoShotAudioPlaybackRequest = %@, deviceSetupFlowBeginDate = %@, deviceSetupFlowEndDate = %@, carOwnsMainAudio = %@, isEyesFreeDevice = %@}"
- "%s passed invalid property list (%@): %{public}@"
- "%s returning nil; passed invalid property list (%@): %{public}@"
- "%s returning nil; passed invalid property list (%{public}@): %@"
- "%s returning nil; unable co create associated data store from property list %@"
- "-[AFConnection acquireAudioSessionWithContext:completion:]_block_invoke"
- "-[AFConnection startRecordingAndGetContinueBlockForPendingSpeechRequestWithOptions:]_block_invoke_2"
- "-[AFPluginManager _registerBundle:]"
- "-[AFSiriTaskExecution start]_block_invoke_3"
- "/System/Library/Frameworks/AVFoundation.framework/Frameworks/AVFAudio.framework/AVFAudio"
- "AVFAudioLibrary"
- "classAVAudioSession"
- "initAVAudioSession_block_invoke"
- "\xf0\xf0\xf0\""
```
