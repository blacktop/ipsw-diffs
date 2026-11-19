## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation`

```diff

-3600.70.47.0.0
-  __TEXT.__text: 0xc9310
-  __TEXT.__objc_methlist: 0xd7a0
-  __TEXT.__const: 0xb38
+3605.32.1.14.1
+  __TEXT.__text: 0xcd424
+  __TEXT.__objc_methlist: 0xdad8
+  __TEXT.__const: 0xb98
   __TEXT.__dlopen_cstrs: 0x18c
   __TEXT.__constg_swiftt: 0x25c
   __TEXT.__swift5_typeref: 0x19d
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x20
-  __TEXT.__cstring: 0x158af
+  __TEXT.__cstring: 0x15e27
   __TEXT.__swift5_reflstr: 0x174
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_fieldmd: 0x180
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x3c08
-  __TEXT.__oslogstring: 0x1027f
-  __TEXT.__unwind_info: 0x39d8
+  __TEXT.__gcc_except_tab: 0x3d48
+  __TEXT.__oslogstring: 0x10958
+  __TEXT.__unwind_info: 0x3ae8
   __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xf90
-  __DATA_CONST.__objc_classlist: 0x760
+  __DATA_CONST.__const: 0x1030
+  __DATA_CONST.__objc_classlist: 0x770
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x208
+  __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x7258
+  __DATA_CONST.__objc_selrefs: 0x7420
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x558
+  __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x1e0
-  __DATA_CONST.__got: 0xc58
-  __AUTH_CONST.__const: 0x3a50
-  __AUTH_CONST.__cfstring: 0x92e0
-  __AUTH_CONST.__objc_const: 0x14d18
+  __DATA_CONST.__got: 0xc68
+  __AUTH_CONST.__const: 0x3b60
+  __AUTH_CONST.__cfstring: 0x9a00
+  __AUTH_CONST.__objc_const: 0x151b0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_dictobj: 0x1e0
-  __AUTH_CONST.__objc_intobj: 0x498
+  __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_floatobj: 0x1a0
-  __AUTH_CONST.__auth_got: 0xec8
+  __AUTH_CONST.__auth_got: 0xed0
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x268
+  __AUTH.__objc_data: 0x2b8
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0xd8c
-  __DATA.__data: 0x18a8
+  __DATA.__objc_ivar: 0xdd4
+  __DATA.__data: 0x1908
   __DATA.__bss: 0x9c0
-  __DATA_DIRTY.__objc_data: 0x4810
+  __DATA_DIRTY.__objc_data: 0x4860
   __DATA_DIRTY.__data: 0x310
-  __DATA_DIRTY.__bss: 0x600
+  __DATA_DIRTY.__bss: 0x658
   __DATA_DIRTY.__common: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5229
-  Symbols:   12060
-  CStrings:  3575
+  Functions: 5313
+  Symbols:   12247
+  CStrings:  3661
 
Symbols:
+ +[CSAudioConsumingStateMonitor sharedInstance]
+ +[CSAudioStartStreamOption getRecordingStartTime:useMachContinuousTime:]
+ +[CSAudioStartStreamOption getRecordingStartTime:useMachContinuousTime:isVoiceTriggered:voiceTriggerInfo:useVoiceTriggerStartTime:]
+ +[CSAudioStreamHoldRequestOption defaultOptionWithTimeout:requestExclaveAudio:]
+ +[CSConfig inputRecordingDurationInSecsAttentive]
+ +[CSFModelConfigDecoder purgeCachedConfigs]
+ +[CSFModelConfigDecoder(Test) cachedConfigPathsForTesting]
+ +[CSUtils allowAttentiveRingBufferSize]
+ +[CSUtils isATVFarFieldVoiceTriggerSupportedLanguageCode:]
+ +[CSUtils isAudioBufferPoolEnabled]
+ +[CSUtils isBargeInDisabled]
+ +[CSUtils isContinuousConversationDisabledInSiriX]
+ +[CSUtils isPerceptionBasedSpeakerChangeDetectionEnabled]
+ +[CSUtils isWaffleIron]
+ +[CSUtils supportEarlyRecordingStartNotification]
+ +[CSUtils(AudioDevice) isCarPlayRecordRoute:]
+ +[CSUtils(Directory) _clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:]
+ +[CSUtils(Directory) clearLogFilesInDirectory:matchingPatterns:exceedNumber:]
+ +[CSUtils(Directory) clearLogFilesInDirectorySync:matchingPatterns:exceedNumber:outError:]
+ -[CSAudioConsumingStateMonitor _setAudioConsumingActive:]
+ -[CSAudioConsumingStateMonitor _startMonitoringWithQueue:]
+ -[CSAudioConsumingStateMonitor _stopMonitoring]
+ -[CSAudioConsumingStateMonitor backdateSessionStartBySeconds:]
+ -[CSAudioConsumingStateMonitor init]
+ -[CSAudioConsumingStateMonitor isAudioConsumingSessionActive]
+ -[CSAudioConsumingStateMonitor notifyAudioConsumingSessionDidStart]
+ -[CSAudioConsumingStateMonitor notifyAudioConsumingSessionDidStop]
+ -[CSAudioProvider _acquirePowerMeterLockFrom:option:needsBoost12dB:]
+ -[CSAudioProvider _anyPowerMeterLockNeedsBoost12dB]
+ -[CSAudioProvider _clientIdentityQualifiesForPowerMeter:]
+ -[CSAudioProvider _forceReleaseAllPowerMeterLocks]
+ -[CSAudioProvider _forceReleasePowerMeterLockFrom:]
+ -[CSAudioProvider _rewindExclaveCursorForLookbackWithOption:]
+ -[CSAudioProvider _setStreamStateStreamingForTesting]
+ -[CSAudioProvider exfiltratingStreamHolderCountLock]
+ -[CSAudioProvider exfiltratingStreamHolderCount]
+ -[CSAudioProvider hasPowerMeterLock]
+ -[CSAudioProvider isLinwoodEnabledForPowerMeter]
+ -[CSAudioProvider powerMeterLocks]
+ -[CSAudioProvider powerMeterNeedsBoost12dB]
+ -[CSAudioProvider setExfiltratingStreamHolderCount:]
+ -[CSAudioProvider setExfiltratingStreamHolderCountLock:]
+ -[CSAudioProvider setHasPowerMeterLock:]
+ -[CSAudioProvider setIsLinwoodEnabledForPowerMeter:]
+ -[CSAudioProvider setPowerMeterLocks:]
+ -[CSAudioProvider setPowerMeterNeedsBoost12dB:]
+ -[CSAudioProviderPowerMeterLock initWithClientIdentity:needsBoost12dB:]
+ -[CSAudioProviderPowerMeterLock needsBoost12dB]
+ -[CSAudioRecordContext canCreateContinuousConversationProfile]
+ -[CSAudioRecordContext isInitialRequest]
+ -[CSAudioRecordContext isOdeonProxyVoiceTriggered]
+ -[CSAudioRecordContext isPullDownGesture]
+ -[CSAudioSpectralMeter setMovingWindowNormalizationEnabled:]
+ -[CSAudioSpectralMeter setMovingWindowNormalizationTarget:windowSeconds:primeThreshold:]
+ -[CSAudioSpectralMeter setNormalizationEnabled:]
+ -[CSAudioStreamHoldRequestOption initWithTimeout:clientIdentity:requireRecordModeLock:requireListeningMicIndicatorLock:requestExclaveAudio:]
+ -[CSAudioStreamHoldRequestOption requestExclaveAudio]
+ -[CSAudioStreamHolding initWithName:clientIdentity:requestExclaveAudio:]
+ -[CSAudioStreamHolding requestExclaveAudio]
+ -[CSEventMonitor _removeObserverOnQueue:]
+ -[CSExclaveRecordClient skipProcessingRaiseToSpeakAOE:]
+ -[CSFPreferences spectralMeterNormalizationPrimeThresholdOverride]
+ -[CSFPreferences spectralMeterNormalizationTargetOverride]
+ -[CSFPreferences spectralMeterNormalizationWindowSecondsOverride]
+ CSIsJ265.isJ265
+ CSIsJ265.onceToken
+ GCC_except_table1017
+ GCC_except_table1018
+ GCC_except_table1022
+ GCC_except_table1026
+ GCC_except_table1027
+ GCC_except_table1028
+ GCC_except_table1030
+ GCC_except_table1031
+ GCC_except_table1032
+ GCC_except_table1046
+ GCC_except_table1116
+ GCC_except_table1118
+ GCC_except_table1119
+ GCC_except_table1129
+ GCC_except_table1452
+ GCC_except_table1483
+ GCC_except_table1566
+ GCC_except_table1571
+ GCC_except_table1574
+ GCC_except_table1575
+ GCC_except_table1586
+ GCC_except_table1589
+ GCC_except_table1590
+ GCC_except_table1595
+ GCC_except_table1597
+ GCC_except_table1598
+ GCC_except_table1601
+ GCC_except_table1602
+ GCC_except_table1603
+ GCC_except_table1605
+ GCC_except_table1609
+ GCC_except_table1787
+ GCC_except_table2000
+ GCC_except_table2003
+ GCC_except_table2007
+ GCC_except_table2010
+ GCC_except_table2011
+ GCC_except_table2013
+ GCC_except_table2019
+ GCC_except_table2025
+ GCC_except_table2027
+ GCC_except_table2028
+ GCC_except_table2094
+ GCC_except_table2099
+ GCC_except_table2162
+ GCC_except_table2215
+ GCC_except_table2216
+ GCC_except_table2219
+ GCC_except_table2225
+ GCC_except_table2236
+ GCC_except_table2249
+ GCC_except_table2292
+ GCC_except_table2310
+ GCC_except_table2391
+ GCC_except_table2491
+ GCC_except_table2528
+ GCC_except_table2699
+ GCC_except_table2703
+ GCC_except_table274
+ GCC_except_table2779
+ GCC_except_table2790
+ GCC_except_table2792
+ GCC_except_table2797
+ GCC_except_table2799
+ GCC_except_table2814
+ GCC_except_table2821
+ GCC_except_table2823
+ GCC_except_table284
+ GCC_except_table2841
+ GCC_except_table2862
+ GCC_except_table2912
+ GCC_except_table2916
+ GCC_except_table2975
+ GCC_except_table2977
+ GCC_except_table2978
+ GCC_except_table3145
+ GCC_except_table3285
+ GCC_except_table3293
+ GCC_except_table3303
+ GCC_except_table3312
+ GCC_except_table3315
+ GCC_except_table3317
+ GCC_except_table3318
+ GCC_except_table3357
+ GCC_except_table3363
+ GCC_except_table3410
+ GCC_except_table346
+ GCC_except_table3503
+ GCC_except_table3515
+ GCC_except_table3521
+ GCC_except_table3528
+ GCC_except_table3540
+ GCC_except_table3565
+ GCC_except_table3566
+ GCC_except_table3567
+ GCC_except_table3568
+ GCC_except_table3593
+ GCC_except_table3606
+ GCC_except_table3777
+ GCC_except_table3837
+ GCC_except_table3851
+ GCC_except_table388
+ GCC_except_table3893
+ GCC_except_table3894
+ GCC_except_table3927
+ GCC_except_table3928
+ GCC_except_table3930
+ GCC_except_table3933
+ GCC_except_table3934
+ GCC_except_table3935
+ GCC_except_table3955
+ GCC_except_table3957
+ GCC_except_table3962
+ GCC_except_table3963
+ GCC_except_table3964
+ GCC_except_table3972
+ GCC_except_table3996
+ GCC_except_table4022
+ GCC_except_table4043
+ GCC_except_table4064
+ GCC_except_table4065
+ GCC_except_table4066
+ GCC_except_table4067
+ GCC_except_table410
+ GCC_except_table411
+ GCC_except_table415
+ GCC_except_table4154
+ GCC_except_table4155
+ GCC_except_table416
+ GCC_except_table4166
+ GCC_except_table4168
+ GCC_except_table4169
+ GCC_except_table4170
+ GCC_except_table4171
+ GCC_except_table4174
+ GCC_except_table4175
+ GCC_except_table4178
+ GCC_except_table4179
+ GCC_except_table4181
+ GCC_except_table4184
+ GCC_except_table4185
+ GCC_except_table4186
+ GCC_except_table4187
+ GCC_except_table4188
+ GCC_except_table4191
+ GCC_except_table4194
+ GCC_except_table4200
+ GCC_except_table4201
+ GCC_except_table4203
+ GCC_except_table4205
+ GCC_except_table4206
+ GCC_except_table421
+ GCC_except_table4211
+ GCC_except_table4212
+ GCC_except_table4217
+ GCC_except_table4218
+ GCC_except_table4221
+ GCC_except_table4223
+ GCC_except_table4224
+ GCC_except_table4227
+ GCC_except_table4228
+ GCC_except_table4229
+ GCC_except_table4231
+ GCC_except_table4232
+ GCC_except_table4234
+ GCC_except_table4235
+ GCC_except_table4237
+ GCC_except_table424
+ GCC_except_table4265
+ GCC_except_table4315
+ GCC_except_table4321
+ GCC_except_table4385
+ GCC_except_table4387
+ GCC_except_table4391
+ GCC_except_table4417
+ GCC_except_table4419
+ GCC_except_table4423
+ GCC_except_table4424
+ GCC_except_table4425
+ GCC_except_table4426
+ GCC_except_table4438
+ GCC_except_table4447
+ GCC_except_table4449
+ GCC_except_table4450
+ GCC_except_table4451
+ GCC_except_table4452
+ GCC_except_table4453
+ GCC_except_table4454
+ GCC_except_table4455
+ GCC_except_table4457
+ GCC_except_table4459
+ GCC_except_table4460
+ GCC_except_table4461
+ GCC_except_table4462
+ GCC_except_table4463
+ GCC_except_table4464
+ GCC_except_table4468
+ GCC_except_table4469
+ GCC_except_table4471
+ GCC_except_table4473
+ GCC_except_table4475
+ GCC_except_table4477
+ GCC_except_table4484
+ GCC_except_table4497
+ GCC_except_table4498
+ GCC_except_table4500
+ GCC_except_table4501
+ GCC_except_table4503
+ GCC_except_table4505
+ GCC_except_table4506
+ GCC_except_table4507
+ GCC_except_table4514
+ GCC_except_table4516
+ GCC_except_table4520
+ GCC_except_table4521
+ GCC_except_table4551
+ GCC_except_table4662
+ GCC_except_table4669
+ GCC_except_table475
+ GCC_except_table4752
+ GCC_except_table476
+ GCC_except_table477
+ GCC_except_table478
+ GCC_except_table479
+ GCC_except_table4813
+ GCC_except_table4823
+ GCC_except_table4871
+ GCC_except_table4872
+ GCC_except_table4873
+ GCC_except_table4875
+ GCC_except_table4876
+ GCC_except_table4879
+ GCC_except_table4880
+ GCC_except_table4882
+ GCC_except_table4883
+ GCC_except_table4885
+ GCC_except_table4887
+ GCC_except_table4888
+ GCC_except_table4890
+ GCC_except_table4926
+ GCC_except_table4992
+ GCC_except_table4997
+ GCC_except_table5038
+ GCC_except_table5104
+ GCC_except_table584
+ GCC_except_table587
+ GCC_except_table622
+ GCC_except_table744
+ GCC_except_table748
+ GCC_except_table750
+ GCC_except_table753
+ GCC_except_table759
+ GCC_except_table915
+ GCC_except_table924
+ GCC_except_table986
+ GCC_except_table994
+ OBJC_IVAR_$_CSAudioConsumingStateMonitor._audioConsumingActive
+ OBJC_IVAR_$_CSAudioConsumingStateMonitor._audioConsumingStartHostTime
+ OBJC_IVAR_$_CSAudioConsumingStateMonitor._lock
+ OBJC_IVAR_$_CSAudioPowerProvider._cachedSelfTapIOBufferDurationOverride
+ OBJC_IVAR_$_CSAudioPowerProvider._cachedSpectralNormalizationPrimeThresholdOverride
+ OBJC_IVAR_$_CSAudioPowerProvider._cachedSpectralNormalizationTargetOverride
+ OBJC_IVAR_$_CSAudioPowerProvider._cachedSpectralNormalizationWindowSecondsOverride
+ OBJC_IVAR_$_CSAudioPowerProvider._farFieldNormalizationEnabled
+ OBJC_IVAR_$_CSAudioPowerProvider._spectralNormalizationEnabled
+ OBJC_IVAR_$_CSAudioProvider._exfiltratingStreamHolderCount
+ OBJC_IVAR_$_CSAudioProvider._exfiltratingStreamHolderCountLock
+ OBJC_IVAR_$_CSAudioProvider._hasPowerMeterLock
+ OBJC_IVAR_$_CSAudioProvider._isLinwoodEnabledForPowerMeter
+ OBJC_IVAR_$_CSAudioProvider._powerMeterLocks
+ OBJC_IVAR_$_CSAudioProvider._powerMeterNeedsBoost12dB
+ OBJC_IVAR_$_CSAudioProviderPowerMeterLock._needsBoost12dB
+ OBJC_IVAR_$_CSAudioStreamHoldRequestOption._requestExclaveAudio
+ OBJC_IVAR_$_CSAudioStreamHolding._requestExclaveAudio
+ _CSAudioPoolCleanup
+ _CSAudioPoolDataWithBytes
+ _CSIsJ265
+ _CSSupportsCompanionRuntime
+ _OBJC_CLASS_$_CSAudioConsumingStateMonitor
+ _OBJC_CLASS_$_CSAudioProviderPowerMeterLock
+ _OBJC_METACLASS_$_CSAudioConsumingStateMonitor
+ _OBJC_METACLASS_$_CSAudioProviderPowerMeterLock
+ __87+[CSUtils(Directory) _clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:]_block_invoke
+ __CSInternalNumberOverrideForKey
+ __OBJC_$_CLASS_METHODS_CSAudioConsumingStateMonitor
+ __OBJC_$_CLASS_METHODS_CSFModelConfigDecoder(Test)
+ __OBJC_$_INSTANCE_METHODS_CSAudioConsumingStateMonitor
+ __OBJC_$_INSTANCE_METHODS_CSAudioProviderPowerMeterLock
+ __OBJC_$_INSTANCE_VARIABLES_CSAudioConsumingStateMonitor
+ __OBJC_$_INSTANCE_VARIABLES_CSAudioProviderPowerMeterLock
+ __OBJC_$_PROP_LIST_CSAudioConsumingStateMonitor
+ __OBJC_$_PROP_LIST_CSAudioProviderPowerMeterLock
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioConsumingStateMonitorProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioConsumingStateMonitorProviding
+ __OBJC_$_PROTOCOL_REFS_CSAudioConsumingStateMonitorProviding
+ __OBJC_CLASS_PROTOCOLS_$_CSAudioConsumingStateMonitor
+ __OBJC_CLASS_RO_$_CSAudioConsumingStateMonitor
+ __OBJC_CLASS_RO_$_CSAudioProviderPowerMeterLock
+ __OBJC_LABEL_PROTOCOL_$_CSAudioConsumingStateMonitorProviding
+ __OBJC_METACLASS_RO_$_CSAudioConsumingStateMonitor
+ __OBJC_METACLASS_RO_$_CSAudioProviderPowerMeterLock
+ __OBJC_PROTOCOL_$_CSAudioConsumingStateMonitorProviding
+ __ZN24CSAudioSpectralMeterImpl14_processWindowEPf
+ __ZN24CSAudioSpectralMeterImpl18resetNormalizationEv
+ __ZN24CSAudioSpectralMeterImpl22setNormalizationTargetEf
+ __ZN24CSAudioSpectralMeterImpl23setNormalizationEnabledEb
+ __ZN24CSAudioSpectralMeterImpl29setNormalizationWindowSecondsEf
+ __ZN24CSAudioSpectralMeterImpl30setNormalizationPrimeThresholdEf
+ __ZN24CSAudioSpectralMeterImpl35setMovingWindowNormalizationEnabledEb
+ ___46+[CSAudioConsumingStateMonitor sharedInstance]_block_invoke
+ ___50+[CSUtils isContinuousConversationDisabledInSiriX]_block_invoke
+ ___50-[CSAudioProvider _forceReleaseAllPowerMeterLocks]_block_invoke
+ ___51-[CSAudioProvider _forceReleasePowerMeterLockFrom:]_block_invoke
+ ___57-[CSAudioConsumingStateMonitor _setAudioConsumingActive:]_block_invoke
+ ___58+[CSUtils isATVFarFieldVoiceTriggerSupportedLanguageCode:]_block_invoke
+ ___68-[CSAudioProvider _acquirePowerMeterLockFrom:option:needsBoost12dB:]_block_invoke
+ ___77+[CSUtils(Directory) clearLogFilesInDirectory:matchingPatterns:exceedNumber:]_block_invoke
+ ___87+[CSUtils(Directory) _clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:]_block_invoke
+ ___CSIsJ265_block_invoke
+ ____ensurePools_block_invoke
+ ___block_descriptor_40_e8_32s_e25_q24?0"NSURL"8"NSURL"16l
+ ___block_descriptor_42_e8_32s_e5_v8?0l
+ ___block_descriptor_51_e8_32s40s_e5_v8?0l
+ _ensurePools.onceToken
+ _kCSDiagnosticReporterAudioConsumingSessionStale
+ _kCSEventMonitorQueueKey
+ _objc_msgSend$_acquirePowerMeterLockFrom:option:needsBoost12dB:
+ _objc_msgSend$_anyPowerMeterLockNeedsBoost12dB
+ _objc_msgSend$_clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:
+ _objc_msgSend$_clientIdentityQualifiesForPowerMeter:
+ _objc_msgSend$_forceReleaseAllPowerMeterLocks
+ _objc_msgSend$_forceReleasePowerMeterLockFrom:
+ _objc_msgSend$_removeObserverOnQueue:
+ _objc_msgSend$_rewindExclaveCursorForLookbackWithOption:
+ _objc_msgSend$_setAudioConsumingActive:
+ _objc_msgSend$absoluteHostTimeToContinuousHostTime:
+ _objc_msgSend$allowAttentiveRingBufferSize
+ _objc_msgSend$audioConsumingStateMonitor:didChangeActive:
+ _objc_msgSend$cleanup
+ _objc_msgSend$clearLogFilesInDirectory:matchingPatterns:exceedNumber:
+ _objc_msgSend$configureForRecordRoute:preferUseSelfTap:
+ _objc_msgSend$defaultOptionWithTimeout:requestExclaveAudio:
+ _objc_msgSend$distantPast
+ _objc_msgSend$exclaveCircularBufferDurationInSecs
+ _objc_msgSend$exfiltratingStreamHolderCount
+ _objc_msgSend$getRecordingStartTime:useMachContinuousTime:isVoiceTriggered:voiceTriggerInfo:useVoiceTriggerStartTime:
+ _objc_msgSend$hasPowerMeterLock
+ _objc_msgSend$initWithClientIdentity:needsBoost12dB:
+ _objc_msgSend$initWithName:clientIdentity:requestExclaveAudio:
+ _objc_msgSend$initWithTimeout:clientIdentity:requireRecordModeLock:requireListeningMicIndicatorLock:requestExclaveAudio:
+ _objc_msgSend$inputRecordingDurationInSecsAttentive
+ _objc_msgSend$isAudioBufferPoolEnabled
+ _objc_msgSend$isCarPlayRecordRoute:
+ _objc_msgSend$isDictation
+ _objc_msgSend$isOdeonProxyVoiceTriggered
+ _objc_msgSend$isPullDownGesture
+ _objc_msgSend$isRequestFromSpokenNotification
+ _objc_msgSend$isVoiceTriggered
+ _objc_msgSend$isWaffleIron
+ _objc_msgSend$isiOSButtonPress
+ _objc_msgSend$powerMeterLocks
+ _objc_msgSend$powerMeterNeedsBoost12dB
+ _objc_msgSend$processAudioChunkForTV:
+ _objc_msgSend$selfTapIOBufferDurationOverride
+ _objc_msgSend$setExfiltratingStreamHolderCount:
+ _objc_msgSend$setHasPowerMeterLock:
+ _objc_msgSend$setMovingWindowNormalizationEnabled:
+ _objc_msgSend$setMovingWindowNormalizationTarget:windowSeconds:primeThreshold:
+ _objc_msgSend$setNormalizationEnabled:
+ _objc_msgSend$setPowerMeterNeedsBoost12dB:
+ _objc_msgSend$skipProcessingRaiseToSpeakAOE:
+ _objc_msgSend$spectralMeterNormalizationPrimeThresholdOverride
+ _objc_msgSend$spectralMeterNormalizationTargetOverride
+ _objc_msgSend$spectralMeterNormalizationWindowSecondsOverride
+ _sConfigCache
+ _sConfigCacheLock
+ _sConfigStamp
+ _sLargePool
+ _sSmallPool
+ _stat
+ isATVFarFieldVoiceTriggerSupportedLanguageCode:.farFieldSupportedLocales
+ isATVFarFieldVoiceTriggerSupportedLanguageCode:.onceToken
+ isContinuousConversationDisabledInSiriX.onceToken
- +[CSUtils isSiriDSPTurnedOn]
- +[CSUtils(Directory) clearLogFilesInDirectory:matchingPattern:exceedNumber:]
- GCC_except_table1002
- GCC_except_table1003
- GCC_except_table1004
- GCC_except_table1008
- GCC_except_table1012
- GCC_except_table1014
- GCC_except_table1020
- GCC_except_table1024
- GCC_except_table1025
- GCC_except_table1039
- GCC_except_table1109
- GCC_except_table1111
- GCC_except_table1112
- GCC_except_table1122
- GCC_except_table1432
- GCC_except_table1463
- GCC_except_table1542
- GCC_except_table1546
- GCC_except_table1547
- GCC_except_table1548
- GCC_except_table1549
- GCC_except_table1550
- GCC_except_table1551
- GCC_except_table1552
- GCC_except_table1553
- GCC_except_table1554
- GCC_except_table1561
- GCC_except_table1564
- GCC_except_table1565
- GCC_except_table1580
- GCC_except_table1584
- GCC_except_table1761
- GCC_except_table1974
- GCC_except_table1975
- GCC_except_table1976
- GCC_except_table1977
- GCC_except_table1981
- GCC_except_table1984
- GCC_except_table1985
- GCC_except_table1987
- GCC_except_table1993
- GCC_except_table1999
- GCC_except_table2068
- GCC_except_table2073
- GCC_except_table2133
- GCC_except_table2184
- GCC_except_table2185
- GCC_except_table2187
- GCC_except_table2188
- GCC_except_table2194
- GCC_except_table2205
- GCC_except_table2261
- GCC_except_table2279
- GCC_except_table2358
- GCC_except_table2456
- GCC_except_table2493
- GCC_except_table2649
- GCC_except_table2653
- GCC_except_table272
- GCC_except_table2729
- GCC_except_table2740
- GCC_except_table2742
- GCC_except_table2747
- GCC_except_table2749
- GCC_except_table2764
- GCC_except_table2771
- GCC_except_table2773
- GCC_except_table2791
- GCC_except_table2812
- GCC_except_table282
- GCC_except_table2853
- GCC_except_table2915
- GCC_except_table2917
- GCC_except_table2918
- GCC_except_table3082
- GCC_except_table3222
- GCC_except_table3230
- GCC_except_table3240
- GCC_except_table3249
- GCC_except_table3252
- GCC_except_table3254
- GCC_except_table3255
- GCC_except_table3294
- GCC_except_table3300
- GCC_except_table3347
- GCC_except_table344
- GCC_except_table3440
- GCC_except_table3452
- GCC_except_table3458
- GCC_except_table3465
- GCC_except_table3474
- GCC_except_table3498
- GCC_except_table3499
- GCC_except_table3500
- GCC_except_table3501
- GCC_except_table3526
- GCC_except_table3539
- GCC_except_table3699
- GCC_except_table3759
- GCC_except_table3773
- GCC_except_table3815
- GCC_except_table3816
- GCC_except_table384
- GCC_except_table3849
- GCC_except_table3850
- GCC_except_table3852
- GCC_except_table3855
- GCC_except_table3856
- GCC_except_table3857
- GCC_except_table3877
- GCC_except_table3879
- GCC_except_table3883
- GCC_except_table3884
- GCC_except_table3885
- GCC_except_table3888
- GCC_except_table3911
- GCC_except_table3937
- GCC_except_table3958
- GCC_except_table3979
- GCC_except_table3980
- GCC_except_table3981
- GCC_except_table3982
- GCC_except_table404
- GCC_except_table406
- GCC_except_table4069
- GCC_except_table407
- GCC_except_table4070
- GCC_except_table4081
- GCC_except_table4083
- GCC_except_table4084
- GCC_except_table4085
- GCC_except_table4086
- GCC_except_table4089
- GCC_except_table409
- GCC_except_table4090
- GCC_except_table4093
- GCC_except_table4094
- GCC_except_table4095
- GCC_except_table4096
- GCC_except_table4099
- GCC_except_table4100
- GCC_except_table4101
- GCC_except_table4102
- GCC_except_table4103
- GCC_except_table4106
- GCC_except_table4109
- GCC_except_table4115
- GCC_except_table4116
- GCC_except_table4118
- GCC_except_table4120
- GCC_except_table4121
- GCC_except_table4126
- GCC_except_table4127
- GCC_except_table4132
- GCC_except_table4133
- GCC_except_table4136
- GCC_except_table4138
- GCC_except_table4139
- GCC_except_table4142
- GCC_except_table4143
- GCC_except_table4144
- GCC_except_table4146
- GCC_except_table4147
- GCC_except_table4149
- GCC_except_table4150
- GCC_except_table4151
- GCC_except_table4152
- GCC_except_table417
- GCC_except_table4230
- GCC_except_table4292
- GCC_except_table4293
- GCC_except_table4300
- GCC_except_table4301
- GCC_except_table4302
- GCC_except_table4303
- GCC_except_table4305
- GCC_except_table4306
- GCC_except_table4328
- GCC_except_table4330
- GCC_except_table4331
- GCC_except_table4332
- GCC_except_table4334
- GCC_except_table4335
- GCC_except_table4336
- GCC_except_table4337
- GCC_except_table4338
- GCC_except_table4339
- GCC_except_table4340
- GCC_except_table4341
- GCC_except_table4353
- GCC_except_table4362
- GCC_except_table4364
- GCC_except_table4365
- GCC_except_table4366
- GCC_except_table4367
- GCC_except_table4368
- GCC_except_table4369
- GCC_except_table4370
- GCC_except_table4372
- GCC_except_table4374
- GCC_except_table4375
- GCC_except_table4376
- GCC_except_table4379
- GCC_except_table4381
- GCC_except_table4383
- GCC_except_table4384
- GCC_except_table4392
- GCC_except_table4399
- GCC_except_table4412
- GCC_except_table4418
- GCC_except_table4429
- GCC_except_table4431
- GCC_except_table4435
- GCC_except_table4436
- GCC_except_table4578
- GCC_except_table4585
- GCC_except_table464
- GCC_except_table4668
- GCC_except_table468
- GCC_except_table469
- GCC_except_table470
- GCC_except_table472
- GCC_except_table4729
- GCC_except_table4739
- GCC_except_table4787
- GCC_except_table4788
- GCC_except_table4789
- GCC_except_table4791
- GCC_except_table4792
- GCC_except_table4795
- GCC_except_table4796
- GCC_except_table4799
- GCC_except_table4801
- GCC_except_table4803
- GCC_except_table4804
- GCC_except_table4842
- GCC_except_table4908
- GCC_except_table4913
- GCC_except_table4954
- GCC_except_table5020
- GCC_except_table577
- GCC_except_table580
- GCC_except_table615
- GCC_except_table737
- GCC_except_table741
- GCC_except_table743
- GCC_except_table746
- GCC_except_table752
- GCC_except_table908
- GCC_except_table917
- GCC_except_table979
- GCC_except_table980
- __OBJC_$_CLASS_METHODS_CSFModelConfigDecoder
- ___47-[CSFPreferences setVoiceProfileRepairPrompted]_block_invoke
- ___76+[CSUtils(Directory) clearLogFilesInDirectory:matchingPattern:exceedNumber:]_block_invoke
- _objc_msgSend$clearLogFilesInDirectory:matchingPattern:exceedNumber:
- _objc_msgSend$connect:to:format:
- _objc_msgSend$initWithName:clientIdentity:
- _objc_msgSend$initWithTimeout:clientIdentity:requireRecordModeLock:requireListeningMicIndicatorLock:
- isAudioStreamProvidingEnabled.result
- setVoiceProfileRepairPrompted.onceToken
CStrings:
+ "%ld.%09ld:%lld"
+ "%s #output_stream Failed to connect source node to main mixer: %@"
+ "%s Acquiring listening mic indicator lock from : %{public}@ %@"
+ "%s Acquiring power meter lock from : %{public}@ %@"
+ "%s Acquiring recordModeLock from : %{public}@"
+ "%s Audio consuming session active for %.1fs with no stop notification; resetting stale state"
+ "%s CSAudioProvider[%{public}@]:%{public}@ ask for audio hold stream from %{public}@ for %{public}.2f secs, requestExclaveAudio = %{public}s"
+ "%s CSAudioProvider[%{public}@]:Clamping exclave lookback from requestedSampleCount = %{public}llu to oldestRetainedSampleCount = %{public}llu"
+ "%s CSAudioProvider[%{public}@]:Remaining audio stream holder requesting audio exfiltration: %{public}lu stream holders"
+ "%s CSAudioProvider[%{public}@]:Set LastFetchedExclaveAudioSampleCount = %{public}llu for exclave lookback (startRecordingHostTime = %{public}llu, currentExclaveAudioSampleCount = %{public}llu)"
+ "%s CSAudioProvider[%{public}@]:Skipping exclave lookback rewind, requestedSampleCount = %{public}llu is not in the past of currentExclaveAudioSampleCount = %{public}llu"
+ "%s Cached decoded model config %{public}@ (%{public}lu top-level keys, %{public}lu cached)"
+ "%s Clearing listening mic indicator lock property, locks = %tu"
+ "%s Could not read directory %{public}@: %{public}@"
+ "%s ERR: could not decode model config %{public}@: %{public}@"
+ "%s ERR: could not read model config %{public}@"
+ "%s ERR: model config %{public}@ is %{public}@, expected a dictionary"
+ "%s Force releasing all %tu listening mic indicator locks"
+ "%s Force releasing all %tu power meter locks"
+ "%s Purged %{public}lu cached model config(s)"
+ "%s RecordSettings received from AVVC: %@"
+ "%s Releasing listening mic indicator lock from : %{public}@"
+ "%s Releasing listening mic indicator lock from : %{public}@ UUID = %@"
+ "%s Releasing listening mic indicator lock from = %{public}@"
+ "%s Releasing power meter lock from : %{public}@"
+ "%s Releasing recordModeLock from : %{public}@"
+ "%s Releasing recordModeLock from : %{public}@ UUID = %@"
+ "%s Secure sensor not allowed within %{public}.0fms, last status = %{public}d"
+ "%s Setting listening mic indicator lock property, locks = %tu"
+ "%s Spectral meter moving-window normalization enabled (far-field path)"
+ "%s Spectral meter normalization enabled (CarPlay path)"
+ "%s Updating audio device info : recordRoute[%{public}@] deviceId[%{public}@] isRemoteDevice[%d]"
+ "+[CSFModelConfigDecoder purgeCachedConfigs]"
+ "+[CSUtils(Directory) _clearLogFilesInDirectory:matchingPatterns:exceedNumber:outError:]"
+ "-[CSAudioConsumingStateMonitor isAudioConsumingSessionActive]"
+ "-[CSAudioProvider _acquirePowerMeterLockFrom:option:needsBoost12dB:]"
+ "-[CSAudioProvider _forceReleaseAllListeningMicIndicatorLocks]"
+ "-[CSAudioProvider _forceReleaseAllPowerMeterLocks]"
+ "-[CSAudioProvider _forceReleasePowerMeterLockFrom:]"
+ "-[CSAudioProvider _rewindExclaveCursorForLookbackWithOption:]"
+ "-[CSAudioRecorder recordSettingsWithStreamHandleId:]"
+ "-[CSAudioRecorder setListeningMicIndicatorPropertyForStream:]"
+ "AppleTV18,1"
+ "CSAudioRecordTypePullDownGesture"
+ "IntutiveConvAudioCapture"
+ "IntutiveConvAudioCaptureHolding"
+ "LOCALE_ACW_SA"
+ "LOCALE_AFB_AE"
+ "LOCALE_AJP_JO"
+ "LOCALE_AJP_PS"
+ "LOCALE_APC_LB"
+ "LOCALE_APC_SY"
+ "LOCALE_ARS_SA"
+ "LOCALE_ARZ_EG"
+ "LOCALE_AZ_AZ"
+ "LOCALE_BE_BY"
+ "LOCALE_BG_BG"
+ "LOCALE_BN_IN"
+ "LOCALE_ET_EE"
+ "LOCALE_GU_IN"
+ "LOCALE_HI_LATN"
+ "LOCALE_IS_IS"
+ "LOCALE_KN_IN"
+ "LOCALE_ML_IN"
+ "LOCALE_MR_IN"
+ "LOCALE_PA_IN"
+ "LOCALE_SL_SI"
+ "LOCALE_SR_RS"
+ "LOCALE_TA_IN"
+ "LOCALE_TE_IN"
+ "LOCALE_UR_IN"
+ "LOCALE_UZ_UZ"
+ "LocalAttendingInitiator"
+ "LocalAttendingInitiatorHolding"
+ "NotHeld"
+ "OpportuneSpeakListener"
+ "OpportuneSpeakListenerHolding"
+ "SiriHolding"
+ "SiriRecordStartAlert"
+ "VoiceTriggerTraining"
+ "audioConsumingSessionStale"
+ "de-AT"
+ "de-CH"
+ "en-IE"
+ "en-IN"
+ "en-NZ"
+ "en-ZA"
+ "fi-FI"
+ "fr-BE"
+ "fr-CH"
+ "he-IL"
+ "nb-NO"
+ "nl-BE"
+ "nl-NL"
+ "spectral_meter_normalization_prime_threshold"
+ "spectral_meter_normalization_target"
+ "spectral_meter_normalization_window_seconds"
+ "startAlertBehavior=%ld"
+ "sv-SE"
+ "zh-TW"
+ "\xf0\"1"
- "%s Acquiring listening mic indicator lock from : %d %@"
- "%s Acquiring recordModeLock from : %d"
- "%s CSAudioProvider[%{public}@]:%{public}@ ask for audio hold stream for %{public}f"
- "%s Clearing listening mic indicator lock property"
- "%s ERR: metaData is nil, defaulting to NO for %{public}@"
- "%s ERR: read metafile %{public}@ failed with %{public}@ - defaulting to NO"
- "%s Releasing listening mic indicator lock UUID = %@"
- "%s Releasing listening mic indicator lock from : %d"
- "%s Releasing listening mic indicator lock from = %d"
- "%s Releasing recordModeLock from : %d"
- "%s Releasing recordModeLock lock UUID = %@"
- "%s Setting listening mic indicator lock property"
- "Conclaves"
- "com_apple_audiomxd_conclave"
- "support_audio_streaming"
```
