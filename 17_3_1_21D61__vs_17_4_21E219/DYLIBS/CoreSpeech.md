## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3303.7.1.0.0
-  __TEXT.__text: 0x1a2198
-  __TEXT.__auth_stubs: 0x1ee0
-  __TEXT.__objc_methlist: 0x17058
-  __TEXT.__const: 0x4c4
-  __TEXT.__gcc_except_tab: 0x3064
-  __TEXT.__cstring: 0x2ef0e
-  __TEXT.__oslogstring: 0x25fcd
-  __TEXT.__dlopen_cstrs: 0x2e9
-  __TEXT.__unwind_info: 0x614c
+3304.82.8.1.2
+  __TEXT.__text: 0x16dd44
+  __TEXT.__auth_stubs: 0x1d40
+  __TEXT.__objc_methlist: 0x147a8
+  __TEXT.__const: 0x480
+  __TEXT.__gcc_except_tab: 0x29f8
+  __TEXT.__cstring: 0x2a5f5
+  __TEXT.__oslogstring: 0x2096b
+  __TEXT.__dlopen_cstrs: 0x245
+  __TEXT.__unwind_info: 0x5560
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x3979
-  __TEXT.__objc_methname: 0x3fa5a
-  __TEXT.__objc_methtype: 0x8960
-  __TEXT.__objc_stubs: 0x20ec0
-  __DATA_CONST.__got: 0x908
-  __DATA_CONST.__const: 0x4e00
-  __DATA_CONST.__objc_classlist: 0xac0
-  __DATA_CONST.__objc_catlist: 0x90
-  __DATA_CONST.__objc_protolist: 0x528
+  __TEXT.__objc_classname: 0x3437
+  __TEXT.__objc_methname: 0x3a68a
+  __TEXT.__objc_methtype: 0x80ec
+  __TEXT.__objc_stubs: 0x1dae0
+  __DATA_CONST.__got: 0x800
+  __DATA_CONST.__const: 0x4988
+  __DATA_CONST.__objc_classlist: 0x990
+  __DATA_CONST.__objc_catlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3bcd8
-  __DATA_CONST.__objc_selrefs: 0xbe38
-  __DATA_CONST.__objc_arraydata: 0x460
-  __AUTH_CONST.__cfstring: 0xb880
-  __AUTH_CONST.__objc_const: 0x9168
-  __AUTH_CONST.__objc_intobj: 0xc78
-  __AUTH_CONST.__const: 0x23a0
+  __DATA_CONST.__objc_const: 0x37340
+  __DATA_CONST.__objc_selrefs: 0xae38
+  __DATA_CONST.__objc_protorefs: 0xa8
+  __DATA_CONST.__objc_classrefs: 0xfe8
+  __DATA_CONST.__objc_superrefs: 0x7c0
+  __DATA_CONST.__objc_arraydata: 0x498
+  __AUTH_CONST.__cfstring: 0xab20
+  __AUTH_CONST.__objc_const: 0x7ed0
+  __AUTH_CONST.__objc_intobj: 0xc48
+  __AUTH_CONST.__const: 0x2180
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_dictobj: 0x410
-  __AUTH_CONST.__objc_floatobj: 0x530
-  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__objc_dictobj: 0x3c0
+  __AUTH_CONST.__objc_floatobj: 0x500
+  __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xf88
-  __AUTH.__objc_data: 0x5140
-  __DATA.__objc_protorefs: 0xa8
-  __DATA.__objc_classrefs: 0x10d0
-  __DATA.__objc_superrefs: 0x8a0
-  __DATA.__objc_ivar: 0x1eb0
-  __DATA.__data: 0x3de0
+  __AUTH_CONST.__auth_got: 0xeb8
+  __AUTH.__objc_data: 0x4880
+  __DATA.__objc_ivar: 0x1bfc
+  __DATA.__data: 0x39d8
   __DATA.__common: 0x30
-  __DATA.__bss: 0x978
-  __DATA_DIRTY.__objc_data: 0x1a40
+  __DATA.__bss: 0x820
+  __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__bss: 0x190
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition
   - /System/Library/PrivateFrameworks/SpeechDetector.framework/SpeechDetector
   - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
+  - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9964
-  Symbols:   32944
-  CStrings:  17082
+  Functions: 8849
+  Symbols:   29501
+  CStrings:  15462
 
Symbols:
+ +[CSAsset(RTModel) supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:]
+ +[CSAttSiriMitigationAssetHandler sharedHandlerDisabledOnDeviceCompilation]
+ +[CSCoreSpeechServices supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]
+ +[CSMil2BnnsUtils _compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:compilationFramework:error:]
+ +[CSMil2BnnsUtils _isBnnsIrReadable:]
+ +[CSMil2BnnsUtils compileModelWithMilFile:bnnsIrCachePath:compilationFramework:]
+ +[CSMil2BnnsUtils mmapModelWithConfig:mappedSizeOut:modelType:]
+ +[CSOnDeviceCompilationUtils _getCachedIrsFromConfigFile:modelType:CSAsset:cachedIrDir:]
+ +[CSOnDeviceCompilationUtils getModelCompiledDirWithModelType:basePath:]
+ +[CSOnDeviceCompilationUtils getModelConfigsWithAsset:modelType:]
+ +[CSOnDeviceCompilationUtils readMilFilePathFromConfig:modelType:]
+ +[CSOnDeviceCompilationUtils shouldCompileForAssetType:]
+ +[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]
+ -[CSAsset(AttSiri) getAllMitigationConfigFiles]
+ -[CSAsset(AttSiri) getAllNldaConfigFiles]
+ -[CSAsset(AttSiri) mitigationModelDefaultNLDAScore]
+ -[CSAsset(Liminal) contConvRecognizerConfigFiles]
+ -[CSAsset(Liminal) getRecognizerConfigsFrom:]
+ -[CSAsset(Liminal) progCheckerRecognizerConfigFiles]
+ -[CSAttSiriMitigationAssetHandler _getPreinstalledMitigationAssetForCurrentLocale:]
+ -[CSAttSiriMitigationAssetHandler initWithAssetManager:withUAFAssetManager:withUAFDownloadMonitor:withLanguageCodeUpdateMonitor:withAssetOverrideFlag:withOverrideAssetPath:disableOnDeviceCompilation:]
+ -[CSAttSiriMitigationAssetHandler initWithDisableOnDeviceCompilation]
+ -[CSAttSiriMitigationAssetHandler onDeviceCompilationHandler]
+ -[CSAttSiriMitigationAssetHandler setCachedAssetWithOverride:]
+ -[CSAttSiriMitigationAssetHandler setOnDeviceCompilationHandler:]
+ -[CSAttSiriMitigationAssetHandler voiceTriggerAssetHandler:endpointId:didChangeCachedAsset:]
+ -[CSBuiltInVoiceTrigger _reportVoiceTriggerFirstPassFireFromAPWithSource:voiceTriggerFirstPassInfo:]
+ -[CSBuiltInVoiceTrigger _resetFirstExclaveAudioBufferMarkerIfNeeded]
+ -[CSBuiltInVoiceTrigger _shouldSkipAudioChunkHandling]
+ -[CSBuiltInVoiceTrigger _voiceTriggerFirstPassInfoFromAP]
+ -[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]
+ -[CSBuiltInVoiceTrigger exclaveClient]
+ -[CSBuiltInVoiceTrigger isFirstExclaveAudioBuffer]
+ -[CSBuiltInVoiceTrigger setExclaveClient:]
+ -[CSBuiltInVoiceTrigger setIsFirstExclaveAudioBuffer:]
+ -[CSContinuousVoiceTrigger _startDetectTwoShot:]
+ -[CSContinuousVoiceTrigger pendingTwoShotDetection]
+ -[CSContinuousVoiceTrigger setPendingTwoShotDetection:]
+ -[CSEndpointerProxy _setActiveEndpointer:]
+ -[CSEndpointerProxy lastUsedAnalyzerType]
+ -[CSEndpointerProxy setLastUsedAnalyzerType:]
+ -[CSFExclaveAudioAvailability arrivalHostTimeToAudioRecorder]
+ -[CSFExclaveAudioAvailability hostTime]
+ -[CSFExclaveAudioAvailability initWithNumChannels:numSamples:sampleByteDepth:startSampleCount:hostTime:arrivalHostTimeToAudioRecorder:]
+ -[CSFExclaveAudioAvailability numChannels]
+ -[CSFExclaveAudioAvailability numSamples]
+ -[CSFExclaveAudioAvailability sampleByteDepth]
+ -[CSFExclaveAudioAvailability startSampleCount]
+ -[CSModelBenchmarker _onDeviceCompilationWithConfigFile:locale:modelType:]
+ -[CSOnDeviceCachedIrPurgingHandler _purgeCachedIrExceptActiveCachedIrs:cachedIrDir:]
+ -[CSOnDeviceCachedIrPurgingHandler _purgeCachedIrFilesWithAsset:]
+ -[CSOnDeviceCachedIrPurgingHandler mitigationAssetHandler:endpointId:didChangeCachedAsset:]
+ -[CSOnDeviceCachedIrPurgingHandler purgeCachedIrForTrialAssetExcludingCurrentAsset:baseCachedIrDir:]
+ -[CSOnDeviceCompilationHandler _compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:modelType:compilationFramework:]
+ -[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:modelType:deviceId:currentLocale:compileDirectory:errOut:]
+ -[CSOnDeviceCompilationHandler compileUsingConfig:locale:compileDirectory:modelType:errOut:]
+ -[CSPreferences dateWhenVoiceTriggerRePrompted]
+ -[CSSpeechController _audioStreamProvider:audioBufferAvailable:]
+ -[CSSpeechManager CSLanguageCodeUpdateMonitor:didReceiveLanguageCodeChanged:]
+ -[CSSpeechManager _notifyLanguageCodeChangeToExclaveKit]
+ -[CSUAFDownloadMonitor _stopMonitoring]
+ -[CSVoiceTriggerFirstPassHearst initWithSpeechManager:voiceTriggerEnabledPolicyHearst:]
+ -[CSVoiceTriggerFirstPassHearst setVoicetriggerHearstEnabledPolicy:]
+ -[CSVoiceTriggerFirstPassHearst voicetriggerHearstEnabledPolicy]
+ -[CSVoiceTriggerHearstEnabledPolicy .cxx_destruct]
+ -[CSVoiceTriggerHearstEnabledPolicy CSEventMonitorDidReceiveEvent:]
+ -[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]
+ -[CSVoiceTriggerHearstEnabledPolicy _subscribeEventMonitors]
+ -[CSVoiceTriggerHearstEnabledPolicy initWithSiriRestrictionOnLockScreenMonitor:screenLockMonitor:voiceTriggerEnabledMonitor:CSPhoneCallStateMonitor:otherAppRecordingStateMonitor:siriClientBehaviorMonitor:srfUserSettingsMonitor:]
+ -[CSVoiceTriggerHearstEnabledPolicy init]
+ -[CSVoiceTriggerHearstEnabledPolicy otherAppRecordingStateMonitor]
+ -[CSVoiceTriggerHearstEnabledPolicy phonecallStateMonitor]
+ -[CSVoiceTriggerHearstEnabledPolicy screenLockMonitor]
+ -[CSVoiceTriggerHearstEnabledPolicy siriClientBehaviorMonitor]
+ -[CSVoiceTriggerHearstEnabledPolicy siriRestrictionOnLockScreenMonitor]
+ -[CSVoiceTriggerHearstEnabledPolicy voiceTriggerEnabledMonitor]
+ -[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:]
+ -[CSVoiceTriggerSecondPass _isFirstPassSourceExclave:]
+ -[CSVoiceTriggerSecondPass _processSecondPassInExclave:]
+ -[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]
+ -[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]
+ -[CSVoiceTriggerSecondPass exclaveClient]
+ -[CSVoiceTriggerSecondPass setExclaveClient:]
+ -[CoreSpeechXPC supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]
+ GCC_except_table1179
+ GCC_except_table1191
+ GCC_except_table1220
+ GCC_except_table1411
+ GCC_except_table145
+ GCC_except_table1474
+ GCC_except_table1498
+ GCC_except_table1502
+ GCC_except_table1518
+ GCC_except_table1521
+ GCC_except_table1549
+ GCC_except_table1645
+ GCC_except_table1647
+ GCC_except_table1649
+ GCC_except_table1655
+ GCC_except_table1710
+ GCC_except_table1742
+ GCC_except_table1821
+ GCC_except_table1841
+ GCC_except_table2032
+ GCC_except_table2168
+ GCC_except_table2214
+ GCC_except_table2217
+ GCC_except_table2220
+ GCC_except_table2225
+ GCC_except_table2237
+ GCC_except_table2242
+ GCC_except_table2245
+ GCC_except_table225
+ GCC_except_table2271
+ GCC_except_table2275
+ GCC_except_table2373
+ GCC_except_table2391
+ GCC_except_table2523
+ GCC_except_table2567
+ GCC_except_table2588
+ GCC_except_table2602
+ GCC_except_table2643
+ GCC_except_table2644
+ GCC_except_table2645
+ GCC_except_table2646
+ GCC_except_table2647
+ GCC_except_table2651
+ GCC_except_table2652
+ GCC_except_table2655
+ GCC_except_table2658
+ GCC_except_table2659
+ GCC_except_table2662
+ GCC_except_table2663
+ GCC_except_table2672
+ GCC_except_table2678
+ GCC_except_table2680
+ GCC_except_table2681
+ GCC_except_table2747
+ GCC_except_table3016
+ GCC_except_table3102
+ GCC_except_table3123
+ GCC_except_table3141
+ GCC_except_table3154
+ GCC_except_table3175
+ GCC_except_table3178
+ GCC_except_table3181
+ GCC_except_table3211
+ GCC_except_table327
+ GCC_except_table3273
+ GCC_except_table3391
+ GCC_except_table3495
+ GCC_except_table3521
+ GCC_except_table3583
+ GCC_except_table3585
+ GCC_except_table3587
+ GCC_except_table3603
+ GCC_except_table3605
+ GCC_except_table3607
+ GCC_except_table3611
+ GCC_except_table3613
+ GCC_except_table3615
+ GCC_except_table3629
+ GCC_except_table3635
+ GCC_except_table3637
+ GCC_except_table3672
+ GCC_except_table380
+ GCC_except_table381
+ GCC_except_table3828
+ GCC_except_table383
+ GCC_except_table385
+ GCC_except_table3852
+ GCC_except_table386
+ GCC_except_table387
+ GCC_except_table389
+ GCC_except_table3910
+ GCC_except_table3945
+ GCC_except_table4034
+ GCC_except_table410
+ GCC_except_table4281
+ GCC_except_table4403
+ GCC_except_table4426
+ GCC_except_table4475
+ GCC_except_table4481
+ GCC_except_table4571
+ GCC_except_table4712
+ GCC_except_table4716
+ GCC_except_table4784
+ GCC_except_table4790
+ GCC_except_table4797
+ GCC_except_table4803
+ GCC_except_table4872
+ GCC_except_table5038
+ GCC_except_table5062
+ GCC_except_table5085
+ GCC_except_table5135
+ GCC_except_table5147
+ GCC_except_table5170
+ GCC_except_table5264
+ GCC_except_table5276
+ GCC_except_table528
+ GCC_except_table5285
+ GCC_except_table5292
+ GCC_except_table5298
+ GCC_except_table5300
+ GCC_except_table5311
+ GCC_except_table5313
+ GCC_except_table5318
+ GCC_except_table5320
+ GCC_except_table5331
+ GCC_except_table5332
+ GCC_except_table5337
+ GCC_except_table5343
+ GCC_except_table5348
+ GCC_except_table5350
+ GCC_except_table5352
+ GCC_except_table5354
+ GCC_except_table5355
+ GCC_except_table5356
+ GCC_except_table5357
+ GCC_except_table5359
+ GCC_except_table5360
+ GCC_except_table5361
+ GCC_except_table5362
+ GCC_except_table5363
+ GCC_except_table5365
+ GCC_except_table5366
+ GCC_except_table5367
+ GCC_except_table5384
+ GCC_except_table5472
+ GCC_except_table5476
+ GCC_except_table5530
+ GCC_except_table5559
+ GCC_except_table5562
+ GCC_except_table5757
+ GCC_except_table577
+ GCC_except_table5773
+ GCC_except_table5781
+ GCC_except_table5786
+ GCC_except_table5803
+ GCC_except_table5806
+ GCC_except_table5810
+ GCC_except_table5813
+ GCC_except_table582
+ GCC_except_table5823
+ GCC_except_table583
+ GCC_except_table584
+ GCC_except_table588
+ GCC_except_table608
+ GCC_except_table6086
+ GCC_except_table609
+ GCC_except_table610
+ GCC_except_table6119
+ GCC_except_table6155
+ GCC_except_table616
+ GCC_except_table6164
+ GCC_except_table6267
+ GCC_except_table6273
+ GCC_except_table644
+ GCC_except_table6510
+ GCC_except_table6514
+ GCC_except_table6525
+ GCC_except_table6547
+ GCC_except_table6583
+ GCC_except_table6591
+ GCC_except_table6614
+ GCC_except_table6621
+ GCC_except_table6622
+ GCC_except_table6764
+ GCC_except_table6819
+ GCC_except_table6941
+ GCC_except_table6942
+ GCC_except_table6952
+ GCC_except_table6953
+ GCC_except_table696
+ GCC_except_table7098
+ GCC_except_table7116
+ GCC_except_table7120
+ GCC_except_table7125
+ GCC_except_table7130
+ GCC_except_table7137
+ GCC_except_table7139
+ GCC_except_table716
+ GCC_except_table7167
+ GCC_except_table7235
+ GCC_except_table7247
+ GCC_except_table7270
+ GCC_except_table7281
+ GCC_except_table7284
+ GCC_except_table7307
+ GCC_except_table7319
+ GCC_except_table7687
+ GCC_except_table7697
+ GCC_except_table771
+ GCC_except_table773
+ GCC_except_table7747
+ GCC_except_table777
+ GCC_except_table782
+ GCC_except_table7823
+ GCC_except_table7833
+ GCC_except_table7835
+ GCC_except_table7836
+ GCC_except_table7838
+ GCC_except_table7845
+ GCC_except_table7850
+ GCC_except_table7851
+ GCC_except_table7855
+ GCC_except_table7856
+ GCC_except_table7860
+ GCC_except_table7861
+ GCC_except_table7862
+ GCC_except_table7863
+ GCC_except_table7865
+ GCC_except_table7866
+ GCC_except_table7867
+ GCC_except_table7868
+ GCC_except_table7870
+ GCC_except_table7872
+ GCC_except_table7873
+ GCC_except_table7902
+ GCC_except_table7956
+ GCC_except_table7980
+ GCC_except_table8022
+ GCC_except_table8033
+ GCC_except_table8179
+ GCC_except_table8187
+ GCC_except_table8319
+ GCC_except_table8411
+ GCC_except_table8453
+ GCC_except_table8484
+ GCC_except_table8498
+ GCC_except_table8505
+ GCC_except_table8510
+ GCC_except_table8525
+ _AFDeviceSupportsFullSiriUOD
+ _AVAudioSessionCategoryPlayAndRecord
+ _AudioConverterFillComplexBuffer_BlockInvoke.29540
+ _CSSystemRootDirectory
+ _MobileTimerLibrary.920
+ _MobileTimerLibraryCore.frameworkLibrary.926
+ _OBJC_CLASS_$_CSExclaveRecordClient
+ _OBJC_CLASS_$_CSFAudioDeviceInfo
+ _OBJC_CLASS_$_CSFAudioRecordDeviceInfo
+ _OBJC_CLASS_$_CSFBnnsIrLookUp
+ _OBJC_CLASS_$_CSFExclaveAudioAvailability
+ _OBJC_CLASS_$_CSFModelComputeBackendUtils
+ _OBJC_CLASS_$_CSFModelConfigDecoder
+ _OBJC_CLASS_$_CSSafetyOneArgumentCompletionBlock
+ _OBJC_CLASS_$_CSVoiceTriggerHearstEnabledPolicy
+ _OBJC_CLASS_$_SFEntitledAssetManager
+ _OBJC_CLASS_$_SLODLDConfigDecoder
+ _OBJC_CLASS_$_SLUresMitigatorConfigDecoder
+ _OBJC_CLASS_$_UAFAssetSetManager
+ _OBJC_IVAR_$_CSAttSiriMitigationAssetHandler._onDeviceCompilationHandler
+ _OBJC_IVAR_$_CSBuiltInVoiceTrigger._exclaveClient
+ _OBJC_IVAR_$_CSBuiltInVoiceTrigger._isFirstExclaveAudioBuffer
+ _OBJC_IVAR_$_CSContinuousVoiceTrigger._pendingTwoShotDetection
+ _OBJC_IVAR_$_CSEndpointerProxy._lastUsedAnalyzerType
+ _OBJC_IVAR_$_CSFExclaveAudioAvailability._arrivalHostTimeToAudioRecorder
+ _OBJC_IVAR_$_CSFExclaveAudioAvailability._hostTime
+ _OBJC_IVAR_$_CSFExclaveAudioAvailability._numChannels
+ _OBJC_IVAR_$_CSFExclaveAudioAvailability._numSamples
+ _OBJC_IVAR_$_CSFExclaveAudioAvailability._sampleByteDepth
+ _OBJC_IVAR_$_CSFExclaveAudioAvailability._startSampleCount
+ _OBJC_IVAR_$_CSUAFDownloadMonitor._observerToken
+ _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._voicetriggerHearstEnabledPolicy
+ _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._otherAppRecordingStateMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._phonecallStateMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._screenLockMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._siriClientBehaviorMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._siriRestrictionOnLockScreenMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._voiceTriggerEnabledMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerSecondPass._exclaveClient
+ _OBJC_METACLASS_$_CSFAudioDeviceInfo
+ _OBJC_METACLASS_$_CSFAudioRecordDeviceInfo
+ _OBJC_METACLASS_$_CSFExclaveAudioAvailability
+ _OBJC_METACLASS_$_CSVoiceTriggerHearstEnabledPolicy
+ __OBJC_$_CATEGORY_CSAudioRecordContext_$_Helper
+ __OBJC_$_CATEGORY_NSString_$_Nvi
+ __OBJC_$_CLASS_METHODS_CSUtils(Statistics|Json|AudioFile|NSXPC|Trial)
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.12399
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.12718
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.16625
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.17329
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.24172
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.26153
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.28499
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.28984
+ __OBJC_$_INSTANCE_METHODS_CSAudioRecordContext(Helper|isPluginContext)
+ __OBJC_$_INSTANCE_METHODS_CSFExclaveAudioAvailability
+ __OBJC_$_INSTANCE_METHODS_CSVoiceTriggerHearstEnabledPolicy
+ __OBJC_$_INSTANCE_METHODS_NSData(Nvi)
+ __OBJC_$_INSTANCE_METHODS_NSString(Nvi)
+ __OBJC_$_INSTANCE_VARIABLES_CSFExclaveAudioAvailability
+ __OBJC_$_INSTANCE_VARIABLES_CSVoiceTriggerHearstEnabledPolicy
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzer.18734
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzer.23993
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzer.25236
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzerImpl.18735
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzerImpl.23994
+ __OBJC_$_PROP_LIST_CSFExclaveAudioAvailability
+ __OBJC_$_PROP_LIST_CSSiriAudioPlaybackSession.14437
+ __OBJC_$_PROP_LIST_CSVoiceTriggerHearstEnabledPolicy
+ __OBJC_$_PROP_LIST_NSObject.10016
+ __OBJC_$_PROP_LIST_NSObject.10207
+ __OBJC_$_PROP_LIST_NSObject.10482
+ __OBJC_$_PROP_LIST_NSObject.10863
+ __OBJC_$_PROP_LIST_NSObject.11063
+ __OBJC_$_PROP_LIST_NSObject.1116
+ __OBJC_$_PROP_LIST_NSObject.11590
+ __OBJC_$_PROP_LIST_NSObject.11749
+ __OBJC_$_PROP_LIST_NSObject.12116
+ __OBJC_$_PROP_LIST_NSObject.1259
+ __OBJC_$_PROP_LIST_NSObject.12995
+ __OBJC_$_PROP_LIST_NSObject.13172
+ __OBJC_$_PROP_LIST_NSObject.13554
+ __OBJC_$_PROP_LIST_NSObject.1402
+ __OBJC_$_PROP_LIST_NSObject.14145
+ __OBJC_$_PROP_LIST_NSObject.14438
+ __OBJC_$_PROP_LIST_NSObject.14633
+ __OBJC_$_PROP_LIST_NSObject.14981
+ __OBJC_$_PROP_LIST_NSObject.1500
+ __OBJC_$_PROP_LIST_NSObject.15127
+ __OBJC_$_PROP_LIST_NSObject.153
+ __OBJC_$_PROP_LIST_NSObject.15366
+ __OBJC_$_PROP_LIST_NSObject.1566
+ __OBJC_$_PROP_LIST_NSObject.16168
+ __OBJC_$_PROP_LIST_NSObject.16325
+ __OBJC_$_PROP_LIST_NSObject.16994
+ __OBJC_$_PROP_LIST_NSObject.1705
+ __OBJC_$_PROP_LIST_NSObject.17149
+ __OBJC_$_PROP_LIST_NSObject.17822
+ __OBJC_$_PROP_LIST_NSObject.17995
+ __OBJC_$_PROP_LIST_NSObject.18736
+ __OBJC_$_PROP_LIST_NSObject.19013
+ __OBJC_$_PROP_LIST_NSObject.19865
+ __OBJC_$_PROP_LIST_NSObject.20011
+ __OBJC_$_PROP_LIST_NSObject.20878
+ __OBJC_$_PROP_LIST_NSObject.21161
+ __OBJC_$_PROP_LIST_NSObject.21238
+ __OBJC_$_PROP_LIST_NSObject.21541
+ __OBJC_$_PROP_LIST_NSObject.2202
+ __OBJC_$_PROP_LIST_NSObject.22393
+ __OBJC_$_PROP_LIST_NSObject.22633
+ __OBJC_$_PROP_LIST_NSObject.22932
+ __OBJC_$_PROP_LIST_NSObject.2312
+ __OBJC_$_PROP_LIST_NSObject.23995
+ __OBJC_$_PROP_LIST_NSObject.24677
+ __OBJC_$_PROP_LIST_NSObject.24805
+ __OBJC_$_PROP_LIST_NSObject.24869
+ __OBJC_$_PROP_LIST_NSObject.24973
+ __OBJC_$_PROP_LIST_NSObject.25237
+ __OBJC_$_PROP_LIST_NSObject.25474
+ __OBJC_$_PROP_LIST_NSObject.25725
+ __OBJC_$_PROP_LIST_NSObject.25917
+ __OBJC_$_PROP_LIST_NSObject.26412
+ __OBJC_$_PROP_LIST_NSObject.26677
+ __OBJC_$_PROP_LIST_NSObject.26828
+ __OBJC_$_PROP_LIST_NSObject.27097
+ __OBJC_$_PROP_LIST_NSObject.27233
+ __OBJC_$_PROP_LIST_NSObject.2741
+ __OBJC_$_PROP_LIST_NSObject.28086
+ __OBJC_$_PROP_LIST_NSObject.28282
+ __OBJC_$_PROP_LIST_NSObject.28746
+ __OBJC_$_PROP_LIST_NSObject.2916
+ __OBJC_$_PROP_LIST_NSObject.29370
+ __OBJC_$_PROP_LIST_NSObject.29475
+ __OBJC_$_PROP_LIST_NSObject.30150
+ __OBJC_$_PROP_LIST_NSObject.3060
+ __OBJC_$_PROP_LIST_NSObject.30652
+ __OBJC_$_PROP_LIST_NSObject.30746
+ __OBJC_$_PROP_LIST_NSObject.30898
+ __OBJC_$_PROP_LIST_NSObject.311
+ __OBJC_$_PROP_LIST_NSObject.3281
+ __OBJC_$_PROP_LIST_NSObject.3522
+ __OBJC_$_PROP_LIST_NSObject.387
+ __OBJC_$_PROP_LIST_NSObject.4028
+ __OBJC_$_PROP_LIST_NSObject.4228
+ __OBJC_$_PROP_LIST_NSObject.4634
+ __OBJC_$_PROP_LIST_NSObject.5223
+ __OBJC_$_PROP_LIST_NSObject.5497
+ __OBJC_$_PROP_LIST_NSObject.5611
+ __OBJC_$_PROP_LIST_NSObject.564
+ __OBJC_$_PROP_LIST_NSObject.5834
+ __OBJC_$_PROP_LIST_NSObject.5946
+ __OBJC_$_PROP_LIST_NSObject.6047
+ __OBJC_$_PROP_LIST_NSObject.6775
+ __OBJC_$_PROP_LIST_NSObject.7011
+ __OBJC_$_PROP_LIST_NSObject.7189
+ __OBJC_$_PROP_LIST_NSObject.7253
+ __OBJC_$_PROP_LIST_NSObject.7588
+ __OBJC_$_PROP_LIST_NSObject.7798
+ __OBJC_$_PROP_LIST_NSObject.7928
+ __OBJC_$_PROP_LIST_NSObject.8370
+ __OBJC_$_PROP_LIST_NSObject.8831
+ __OBJC_$_PROP_LIST_NSObject.8924
+ __OBJC_$_PROP_LIST_NSObject.9186
+ __OBJC_$_PROP_LIST_NSObject.9704
+ __OBJC_$_PROP_LIST_NSObject.99
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.12400
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.12719
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.16626
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.17330
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.24173
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.26154
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.28500
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.28985
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.19866
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.3523
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.4635
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.6776
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAssetManagerDelegate.23996
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAttSiriMitigationAssetHandlerDelegate.26413
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioConverterDelegate.11750
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.11751
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.12117
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.1706
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.22634
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.4029
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioRecorderDelegate.26678
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioRouteChangeMonitorDelegate.20879
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioSessionInfoProviding.24806
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProviding.27098
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.10864
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.16169
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.16995
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.19014
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.19867
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.30151
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.4229
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.4636
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.7012
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.8371
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.9705
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBenchmarkXPCProtocol.22635
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBluetoothWirelessSplitterMonitorDelegate.20880
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBluetoothWirelessSplitterMonitorDelegate.26414
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.18737
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.23997
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.25238
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerDelegate.28087
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImpl.18738
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImpl.23998
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImplDelegate.25239
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEventMonitorDelegate.13555
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFallbackAudioSessionReleaseProviding.26679
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.12996
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.7190
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.8372
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.9187
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSMediaPlayingMonitorDelegate.16996
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.26415
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.30152
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSecondPassProgressProviding.19868
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.11064
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.19869
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.5612
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriAudioPlaybackSession.14439
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.10483
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.10865
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.13173
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.16997
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.19870
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.25918
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.30153
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.3524
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.4637
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.7589
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.9706
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSpeakerRecognitionAssetDownloadMonitorDelegate.17996
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSystemShellStartProviding.14634
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSystemShellStartProviding.22933
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSTrialAssetDownloadMonitorDelegate.3282
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSUAFDownloadMonitorDelegate.29371
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.29372
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.6777
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.8373
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.10208
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.11065
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.14146
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.20881
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.25475
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.10484
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.17997
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.19871
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSXPCClientDelegate.7013
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSXPCClientDelegate.8374
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreSpeechXPCProtocol.22295
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EARCaesuraSilencePosteriorGeneratorDelegate.28747
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.12401
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.12720
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.16627
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.17331
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.24174
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.26155
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.28501
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.28986
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.30957
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.17332
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.24175
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.26156
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.28502
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.28987
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.100
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10017
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10209
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10485
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10866
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11066
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1117
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11591
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11752
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12118
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1260
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12997
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.13174
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.13556
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1403
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14147
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14440
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14635
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14982
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1501
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15128
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15367
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.154
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1567
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16170
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16326
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16998
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1707
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17150
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17823
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17998
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.18739
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.19015
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.19872
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.20012
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.20882
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21162
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21239
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21542
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2203
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22394
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22636
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22934
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2313
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.23999
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24678
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24807
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24870
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24974
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25240
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25476
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25726
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25919
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26416
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26680
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26829
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27099
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27234
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2742
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28088
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28283
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28748
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2917
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29373
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29476
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30154
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3061
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30653
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30747
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30899
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.312
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3283
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3525
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.388
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4030
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4230
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4638
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5224
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5498
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5613
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.565
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5835
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5947
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6048
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6778
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7014
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7191
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7254
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7590
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7799
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7929
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8375
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8832
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8925
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9188
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9707
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioRecorderDelegate.26681
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.16171
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.16327
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.16999
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.17824
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.19873
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.27100
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.30155
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.5948
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.6049
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.6779
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionControllerDelegate.28089
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionControllerDelegate.28284
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.10867
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.16172
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.17000
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.19016
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.19874
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.30156
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.4231
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.4639
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.7015
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.8376
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.9708
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.18740
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.24000
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.25241
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerDelegate.28090
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImpl.18741
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImpl.24001
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImplDelegate.25242
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSKeywordAnalyzerNDEAPIScoreDelegate.15129
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSOpportuneSpeakEventMonitorDelegate.9709
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSPGEndpointAnalyzerDelegate.4640
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.10486
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.10868
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.13175
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.17001
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.19875
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.25920
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.30157
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.3526
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.4641
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.7591
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.9710
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.10210
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.11067
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.14148
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.20883
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.25477
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVolumeMonitorDelegate.10211
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EARCaesuraSilencePosteriorGeneratorDelegate.28749
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10018
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.101
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10212
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10487
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10869
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11068
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1118
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11592
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11753
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12119
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1261
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12998
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.13176
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.13557
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1404
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14149
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14441
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14636
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14983
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1502
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15130
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15368
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.155
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1568
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.16173
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.16328
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17002
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1708
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17151
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17825
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17999
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.18742
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.19017
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.19876
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.20013
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.20884
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21163
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21240
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21543
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2204
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22395
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22637
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22935
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2314
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24002
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24679
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24808
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24871
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24975
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25243
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25478
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25727
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25921
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26417
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26682
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26830
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27101
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27235
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2743
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28091
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28285
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28750
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2918
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29374
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29477
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30158
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3062
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30654
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30748
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30900
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.313
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3284
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3527
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.389
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4031
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4232
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4642
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5225
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5499
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5614
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.566
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5836
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5949
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6050
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6780
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7016
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7192
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7255
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7592
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7800
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7930
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8377
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8833
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8926
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9189
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9711
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SNResultsObserving.7801
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRSpeakerRecognitionControllerDelegate.8378
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFEntitledAssetDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNResultsObserving.7802
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.19877
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.3528
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.4643
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.6781
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAssetManagerDelegate.24003
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAttSiriMitigationAssetHandlerDelegate.26418
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioConverterDelegate.11754
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.11755
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.12120
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.1709
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.22638
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.4032
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioRecorderDelegate.26683
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioRouteChangeMonitorDelegate.20885
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.16174
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.16329
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.17003
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.17826
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.19878
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.27102
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.30159
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.5950
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.6051
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.6782
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionControllerDelegate.28092
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionControllerDelegate.28286
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionInfoProviding.24809
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProviding.27103
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.10870
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.16175
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.17004
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.19018
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.19879
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.30160
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.4233
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.4644
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.7017
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.8379
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.9712
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBenchmarkXPCProtocol.22639
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBluetoothWirelessSplitterMonitorDelegate.20886
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBluetoothWirelessSplitterMonitorDelegate.26419
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.18743
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.24004
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.25244
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerDelegate.28093
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImpl.18744
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImpl.24005
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImplDelegate.25245
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEventMonitorDelegate.13558
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSFallbackAudioSessionReleaseProviding.26684
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSKeywordAnalyzerNDEAPIScoreDelegate.15131
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.12999
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.7193
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.8380
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.9190
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSMediaPlayingMonitorDelegate.17005
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSOpportuneSpeakEventMonitorDelegate.9713
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.26420
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.30161
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSPGEndpointAnalyzerDelegate.4645
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSecondPassProgressProviding.19880
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.11069
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.19881
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.5615
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriAudioPlaybackSession.14442
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.10488
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.10871
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.13177
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.17006
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.19882
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.25922
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.30162
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.3529
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.4646
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.7593
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.9714
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSpeakerRecognitionAssetDownloadMonitorDelegate.18000
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemShellStartProviding.14637
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemShellStartProviding.22936
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSTrialAssetDownloadMonitorDelegate.3285
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSUAFDownloadMonitorDelegate.29375
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.29376
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.6783
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.8381
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.10213
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.11070
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.14150
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.20887
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.25479
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.10489
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.18001
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.19883
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVolumeMonitorDelegate.10214
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSXPCClientDelegate.7018
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSXPCClientDelegate.8382
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreSpeechXPCProtocol.22296
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EARCaesuraSilencePosteriorGeneratorDelegate.28751
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.12402
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.12721
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.16628
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.17333
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.24176
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.26157
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.28503
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.28988
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.30958
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.17334
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.24177
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.26158
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.28504
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.28989
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10019
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.102
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10215
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10490
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10872
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11071
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1119
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11593
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11756
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.12121
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1262
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.13000
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.13178
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.13559
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1405
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14151
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14443
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14638
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14984
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1503
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15132
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15369
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.156
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1569
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.16176
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.16330
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17007
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1710
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17152
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17827
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18002
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18745
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.19019
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.19884
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.20014
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.20888
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21164
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21241
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21544
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2205
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22396
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22640
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22937
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2315
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24006
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24680
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24810
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24872
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24976
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25246
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25480
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25728
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25923
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26421
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26685
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26831
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27104
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27236
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2744
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.28094
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.28752
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2919
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29377
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29478
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30163
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3063
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30655
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30749
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30901
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.314
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3286
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3530
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.390
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4033
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4234
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4647
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5226
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5500
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5616
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.567
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5837
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5951
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6052
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6784
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7019
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7194
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7256
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7594
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7803
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7931
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8383
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8834
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8927
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9191
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9715
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.12403
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.12722
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.16629
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.17335
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.24178
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.26159
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.28505
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.28990
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SFEntitledAssetDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SNResultsObserving.7804
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRSpeakerRecognitionControllerDelegate.8384
+ __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.19885
+ __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.3531
+ __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.4648
+ __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.6785
+ __OBJC_$_PROTOCOL_REFS_CSAssetManagerDelegate.24007
+ __OBJC_$_PROTOCOL_REFS_CSAttSiriMitigationAssetHandlerDelegate.26422
+ __OBJC_$_PROTOCOL_REFS_CSAudioConverterDelegate.11757
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.11758
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.12122
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.1711
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.22641
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.4034
+ __OBJC_$_PROTOCOL_REFS_CSAudioRecorderDelegate.26686
+ __OBJC_$_PROTOCOL_REFS_CSAudioRouteChangeMonitorDelegate.20889
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.16177
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.16331
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.17008
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.17828
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.19886
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.27105
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.30164
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.5952
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.6053
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.6786
+ __OBJC_$_PROTOCOL_REFS_CSAudioSessionControllerDelegate.28095
+ __OBJC_$_PROTOCOL_REFS_CSAudioSessionControllerDelegate.28288
+ __OBJC_$_PROTOCOL_REFS_CSAudioSessionInfoProviding.24811
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProviding.27106
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.10873
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.16178
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.17009
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.19020
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.19887
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.30165
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.4235
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.4649
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.7020
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.8385
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.9716
+ __OBJC_$_PROTOCOL_REFS_CSBluetoothWirelessSplitterMonitorDelegate.20890
+ __OBJC_$_PROTOCOL_REFS_CSBluetoothWirelessSplitterMonitorDelegate.26423
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.18746
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.24008
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.25247
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerDelegate.28096
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImpl.18747
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImpl.24009
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImplDelegate.25248
+ __OBJC_$_PROTOCOL_REFS_CSEventMonitorDelegate.13560
+ __OBJC_$_PROTOCOL_REFS_CSFallbackAudioSessionReleaseProviding.26687
+ __OBJC_$_PROTOCOL_REFS_CSKeywordAnalyzerNDEAPIScoreDelegate.15133
+ __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.13001
+ __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.7195
+ __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.8386
+ __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.9192
+ __OBJC_$_PROTOCOL_REFS_CSMediaPlayingMonitorDelegate.17010
+ __OBJC_$_PROTOCOL_REFS_CSOpportuneSpeakEventMonitorDelegate.9717
+ __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.26424
+ __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.30166
+ __OBJC_$_PROTOCOL_REFS_CSSPGEndpointAnalyzerDelegate.4650
+ __OBJC_$_PROTOCOL_REFS_CSSecondPassProgressProviding.19888
+ __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.11072
+ __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.19889
+ __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.5617
+ __OBJC_$_PROTOCOL_REFS_CSSiriAudioPlaybackSession.14444
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.10491
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.10874
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.13179
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.17011
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.19890
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.25924
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.30167
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.3532
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.4651
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.7595
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.9718
+ __OBJC_$_PROTOCOL_REFS_CSSpeakerRecognitionAssetDownloadMonitorDelegate.18003
+ __OBJC_$_PROTOCOL_REFS_CSSpeechManagerDelegate.30902
+ __OBJC_$_PROTOCOL_REFS_CSSystemShellStartProviding.14639
+ __OBJC_$_PROTOCOL_REFS_CSSystemShellStartProviding.22938
+ __OBJC_$_PROTOCOL_REFS_CSTrialAssetDownloadMonitorDelegate.3287
+ __OBJC_$_PROTOCOL_REFS_CSUAFDownloadMonitorDelegate.29378
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.29379
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.6787
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.8387
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.10216
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.11073
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.14152
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.20891
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.25481
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.10492
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.18004
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.19891
+ __OBJC_$_PROTOCOL_REFS_CSVolumeMonitorDelegate.10217
+ __OBJC_$_PROTOCOL_REFS_CSXPCClientDelegate.7021
+ __OBJC_$_PROTOCOL_REFS_CSXPCClientDelegate.8388
+ __OBJC_$_PROTOCOL_REFS_EARCaesuraSilencePosteriorGeneratorDelegate.28753
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.12404
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.12723
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.16630
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.17336
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.24179
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.26160
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.28506
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.28991
+ __OBJC_$_PROTOCOL_REFS_SFEntitledAssetDelegate
+ __OBJC_$_PROTOCOL_REFS_SNResultsObserving.7805
+ __OBJC_$_PROTOCOL_REFS_SSRSpeakerRecognitionControllerDelegate.8389
+ __OBJC_CLASS_PROTOCOLS_$_CSVoiceTriggerHearstEnabledPolicy
+ __OBJC_CLASS_RO_$_CSFExclaveAudioAvailability
+ __OBJC_CLASS_RO_$_CSVoiceTriggerHearstEnabledPolicy
+ __OBJC_LABEL_PROTOCOL_$_SFEntitledAssetDelegate
+ __OBJC_METACLASS_RO_$_CSFExclaveAudioAvailability
+ __OBJC_METACLASS_RO_$_CSVoiceTriggerHearstEnabledPolicy
+ __OBJC_PROTOCOL_$_SFEntitledAssetDelegate
+ __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ue170006IPNS_6vectorINS4_IfNS_9allocatorIfEEEENS5_IS7_EEEESA_SA_EENS_4pairIT_T1_EESC_T0_SD_
+ __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ue170006IPNS_6vectorIfNS_9allocatorIfEEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
+ __ZNKSt3__114default_deleteIN10corespeech25CSAudioCircularBufferImplIhEEEclB8ue170006EPS3_
+ __ZNKSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIPKhNS_9allocatorIS2_EEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ue170006Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt12out_of_rangeC1B8ue170006EPKc
+ __ZNSt3__110unique_ptrI15SmartSiriVolumeNS_14default_deleteIS1_EEE5resetB8ue170006EPS1_
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorINS_4pairIfjEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ue170006EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ue170006Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ue170006Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ue170006INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ue170006INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ue170006IPS5_S9_EEvT_T0_m
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE18__assign_with_sizeB8ue170006IPS5_S9_EEvT_T0_l
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ue170006Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ue170006IPS3_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ue170006IPS3_S7_EEvT_T0_l
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE7__clearB8ue170006Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ue170006IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ue170006IPfS5_EEvT_T0_l
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___100-[CSOnDeviceCachedIrPurgingHandler purgeCachedIrForTrialAssetExcludingCurrentAsset:baseCachedIrDir:]_block_invoke
+ ___100-[CSRemoteControlClient _fetchDataFromAudioFileUrl:aesKey:encryptedAudioSampleBypeDepth:completion:]_block_invoke.324
+ ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.573
+ ___110-[CSVoiceTriggerSecondPass _requestStartAudioStreamWitContext:audioProviderUUID:startStreamOption:completion:]_block_invoke.487
+ ___112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.529
+ ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.507
+ ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.516
+ ___123+[CSCoreSpeechServices supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]_block_invoke
+ ___123+[CSCoreSpeechServices supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]_block_invoke.25
+ ___123+[CSCoreSpeechServices supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]_block_invoke.26
+ ___123+[CSCoreSpeechServices supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]_block_invoke_2
+ ___125-[CSRemoteControlClient createRemoteVoiceProfileWithAudioFiles:aesKey:encryptedAudioSampleBypeDepth:languageCode:completion:]_block_invoke.298
+ ___125-[CSRemoteControlClient createRemoteVoiceProfileWithAudioFiles:aesKey:encryptedAudioSampleBypeDepth:languageCode:completion:]_block_invoke.302
+ ___133-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke
+ ___133-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.508
+ ___136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke
+ ___136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.516
+ ___137-[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:modelType:deviceId:currentLocale:compileDirectory:errOut:]_block_invoke
+ ___137-[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:modelType:deviceId:currentLocale:compileDirectory:errOut:]_block_invoke.51
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.577
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.578
+ ___161+[CSCoreSpeechServices _voiceTriggerRTModelForVersion:minorVersion:accessoryRTModelType:accessoryInfo:endpointId:downloadedModels:preinstalledModels:completion:]_block_invoke.34
+ ___161+[CSCoreSpeechServices _voiceTriggerRTModelForVersion:minorVersion:accessoryRTModelType:accessoryInfo:endpointId:downloadedModels:preinstalledModels:completion:]_block_invoke.41
+ ___30-[CSBuiltInVoiceTrigger start]_block_invoke.442
+ ___30-[CSBuiltInVoiceTrigger start]_block_invoke.450
+ ___30-[CSBuiltInVoiceTrigger start]_block_invoke_2.453
+ ___36-[CSSiriAcousticFingerprinter flush]_block_invoke.62
+ ___39-[CSBuiltInVoiceTrigger _stopListening]_block_invoke.504
+ ___42-[CSRemoteControlClient didDeviceConnect:]_block_invoke.73
+ ___44-[CSBuiltInVoiceTrigger _stopAPVoiceTrigger]_block_invoke.507
+ ___45-[CSSiriAcousticFingerprinter appendPCMData:]_block_invoke.58
+ ___45-[CSSiriAcousticFingerprinter appendPCMData:]_block_invoke.60
+ ___46+[CSCoreSpeechServices requestUpdatedSATAudio]_block_invoke.53
+ ___46-[CSSiriMobileBluetoothDeviceProxy deviceInfo]_block_invoke.117
+ ___47+[CSCoreSpeechServices getFirstPassRunningMode]_block_invoke.54
+ ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.547
+ ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.58
+ ___49-[CSAssetController _downloadAsset:withComplete:]_block_invoke.294
+ ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.637
+ ___50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.470
+ ___51-[CSAttendingServiceClient _createClientConnection]_block_invoke.79
+ ___51-[CSAttendingServiceClient _createClientConnection]_block_invoke.81
+ ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.499
+ ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke_2.500
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.445
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.452
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.456
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.463
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.464
+ ___52-[CSVoiceTriggerAssetHandlerMac triggerAssetRefresh]_block_invoke.38
+ ___53-[CSRemoteControlClient _transferFile:at:completion:]_block_invoke.159
+ ___54-[CSAssetController fetchRemoteMetaOfType:allowRetry:]_block_invoke.282
+ ___54-[CSAttSiriMitigationAssetHandler triggerAssetRefresh]_block_invoke.50
+ ___55-[CSAttSiriServiceClient _setupAttSiriSvcXpcConnection]_block_invoke.73
+ ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.647
+ ___56-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke
+ ___56-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke_2
+ ___58-[CSRemoteControlClient exchangeRemoteDeviceProtocolInfo:]_block_invoke.283
+ ___61-[CSModelBenchmarker _setupAudioInjectionEngineWithAudioURL:]_block_invoke.54
+ ___65-[CSOnDeviceCachedIrPurgingHandler _purgeCachedIrFilesWithAsset:]_block_invoke
+ ___66+[CSOnDeviceCompilationUtils getCachedIrsFromCSAsset:cachedIrDir:]_block_invoke
+ ___68-[CSBuiltInVoiceTrigger _startListenPollingWithInterval:completion:]_block_invoke.494
+ ___69-[CSSiriMobileBluetoothDeviceProxy initWithAddress:dataSource:queue:]_block_invoke.115
+ ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.648
+ ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke
+ ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke.11
+ ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke.6
+ ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke.8
+ ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke.9
+ ___71-[CSSiriMobileBluetoothDeviceProxy initWithDeviceUID:dataSource:queue:]_block_invoke.116
+ ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.636
+ ___75+[CSAttSiriMitigationAssetHandler sharedHandlerDisabledOnDeviceCompilation]_block_invoke
+ ___75-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:]_block_invoke.619
+ ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.519
+ ___77-[CSSpeechManager CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke.482
+ ___77-[CSSpeechManager CSLanguageCodeUpdateMonitor:didReceiveLanguageCodeChanged:]_block_invoke
+ ___78-[CSRemoteControlClient transferVoiceTriggerAsset:forLanguageCode:completion:]_block_invoke.194
+ ___80-[CSAttSiriMitigationAssetHandler _getMitigationAssetWithEndpointId:completion:]_block_invoke_2
+ ___81-[CSSiriMobileBluetoothDeviceProxy _accessBTDeviceAndAccessoryManagerUsingBlock:]_block_invoke.125
+ ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.501
+ ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.508
+ ___83-[CSAttSiriMitigationAssetHandler _getPreinstalledMitigationAssetForCurrentLocale:]_block_invoke
+ ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.593
+ ___85-[CSRemoteControlClient transferInterstitialAudioFiles:interstitialLevel:completion:]_block_invoke.246
+ ___89+[CSCoreSpeechServices voiceTriggerJarvisLanguageList:jarvisSelectedLanguage:completion:]_block_invoke.51
+ ___92-[CSOnDeviceCompilationHandler compileUsingConfig:locale:compileDirectory:modelType:errOut:]_block_invoke
+ ___92-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:completion:]_block_invoke.30
+ ___92-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:completion:]_block_invoke.32
+ ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.494
+ ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.502
+ ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke_2.504
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.605
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.606
+ ___97-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:]_block_invoke
+ ___Block_byref_object_copy_.10385
+ ___Block_byref_object_copy_.11518
+ ___Block_byref_object_copy_.12915
+ ___Block_byref_object_copy_.13306
+ ___Block_byref_object_copy_.14042
+ ___Block_byref_object_copy_.14936
+ ___Block_byref_object_copy_.1540
+ ___Block_byref_object_copy_.15805
+ ___Block_byref_object_copy_.15933
+ ___Block_byref_object_copy_.17902
+ ___Block_byref_object_copy_.18520
+ ___Block_byref_object_copy_.19977
+ ___Block_byref_object_copy_.20203
+ ___Block_byref_object_copy_.21433
+ ___Block_byref_object_copy_.21802
+ ___Block_byref_object_copy_.2253
+ ___Block_byref_object_copy_.22547
+ ___Block_byref_object_copy_.23318
+ ___Block_byref_object_copy_.23778
+ ___Block_byref_object_copy_.24427
+ ___Block_byref_object_copy_.25321
+ ___Block_byref_object_copy_.25640
+ ___Block_byref_object_copy_.26276
+ ___Block_byref_object_copy_.26595
+ ___Block_byref_object_copy_.2718
+ ___Block_byref_object_copy_.27640
+ ___Block_byref_object_copy_.28212
+ ___Block_byref_object_copy_.29295
+ ___Block_byref_object_copy_.29725
+ ___Block_byref_object_copy_.30601
+ ___Block_byref_object_copy_.3702
+ ___Block_byref_object_copy_.3839
+ ___Block_byref_object_copy_.3946
+ ___Block_byref_object_copy_.4524
+ ___Block_byref_object_copy_.6350
+ ___Block_byref_object_copy_.6682
+ ___Block_byref_object_copy_.7394
+ ___Block_byref_object_copy_.8176
+ ___Block_byref_object_copy_.8763
+ ___Block_byref_object_copy_.9858
+ ___Block_byref_object_dispose_.10386
+ ___Block_byref_object_dispose_.11519
+ ___Block_byref_object_dispose_.12916
+ ___Block_byref_object_dispose_.13307
+ ___Block_byref_object_dispose_.14043
+ ___Block_byref_object_dispose_.14937
+ ___Block_byref_object_dispose_.1541
+ ___Block_byref_object_dispose_.15806
+ ___Block_byref_object_dispose_.15934
+ ___Block_byref_object_dispose_.17903
+ ___Block_byref_object_dispose_.18521
+ ___Block_byref_object_dispose_.19978
+ ___Block_byref_object_dispose_.20204
+ ___Block_byref_object_dispose_.21434
+ ___Block_byref_object_dispose_.21803
+ ___Block_byref_object_dispose_.2254
+ ___Block_byref_object_dispose_.22548
+ ___Block_byref_object_dispose_.23319
+ ___Block_byref_object_dispose_.23779
+ ___Block_byref_object_dispose_.24428
+ ___Block_byref_object_dispose_.25322
+ ___Block_byref_object_dispose_.25641
+ ___Block_byref_object_dispose_.26277
+ ___Block_byref_object_dispose_.26596
+ ___Block_byref_object_dispose_.2719
+ ___Block_byref_object_dispose_.27641
+ ___Block_byref_object_dispose_.28213
+ ___Block_byref_object_dispose_.29296
+ ___Block_byref_object_dispose_.29726
+ ___Block_byref_object_dispose_.30602
+ ___Block_byref_object_dispose_.3703
+ ___Block_byref_object_dispose_.3840
+ ___Block_byref_object_dispose_.3947
+ ___Block_byref_object_dispose_.4525
+ ___Block_byref_object_dispose_.6351
+ ___Block_byref_object_dispose_.6683
+ ___Block_byref_object_dispose_.7395
+ ___Block_byref_object_dispose_.8177
+ ___Block_byref_object_dispose_.8764
+ ___Block_byref_object_dispose_.9859
+ ___MobileTimerLibraryCore_block_invoke.927
+ ___block_descriptor_40_e8_32bs_e18_v16?0"NSNumber"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0B8ls40l8s32l8
+ ___block_descriptor_48_e8_32s_e11_v20?0B8Q12ls32l8
+ ___block_descriptor_48_e8_32s_e8_v16?0Q8ls32l8
+ ___block_descriptor_49_e8_32s40bs_e11_v20?0I8Q12ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e15_v32?0816^B24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0lr48l8s32l8r56l8s40l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.10.10548
+ ___block_literal_global.10.22947
+ ___block_literal_global.10.24295
+ ___block_literal_global.10157
+ ___block_literal_global.10418
+ ___block_literal_global.10574
+ ___block_literal_global.1074
+ ___block_literal_global.1077
+ ___block_literal_global.10770
+ ___block_literal_global.10978
+ ___block_literal_global.11377
+ ___block_literal_global.11545
+ ___block_literal_global.11830
+ ___block_literal_global.11930
+ ___block_literal_global.12050
+ ___block_literal_global.1221
+ ___block_literal_global.12343
+ ___block_literal_global.12448
+ ___block_literal_global.12502
+ ___block_literal_global.12630
+ ___block_literal_global.12666
+ ___block_literal_global.13.23119
+ ___block_literal_global.13.24296
+ ___block_literal_global.13108
+ ___block_literal_global.13220
+ ___block_literal_global.13494
+ ___block_literal_global.13587
+ ___block_literal_global.1363
+ ___block_literal_global.13953
+ ___block_literal_global.14064
+ ___block_literal_global.14476
+ ___block_literal_global.14523
+ ___block_literal_global.14592
+ ___block_literal_global.1462
+ ___block_literal_global.14646
+ ___block_literal_global.14664
+ ___block_literal_global.14775
+ ___block_literal_global.15.14524
+ ___block_literal_global.15326
+ ___block_literal_global.15411
+ ___block_literal_global.15906
+ ___block_literal_global.15917
+ ___block_literal_global.15962
+ ___block_literal_global.16.14477
+ ___block_literal_global.16.22948
+ ___block_literal_global.16284
+ ___block_literal_global.1645
+ ___block_literal_global.16891
+ ___block_literal_global.17.23050
+ ___block_literal_global.17220
+ ___block_literal_global.17398
+ ___block_literal_global.17407
+ ___block_literal_global.17490
+ ___block_literal_global.17524
+ ___block_literal_global.17779
+ ___block_literal_global.17855
+ ___block_literal_global.17953
+ ___block_literal_global.18.14745
+ ___block_literal_global.18.23120
+ ___block_literal_global.18053
+ ___block_literal_global.18829
+ ___block_literal_global.18876
+ ___block_literal_global.190
+ ___block_literal_global.19081
+ ___block_literal_global.19111
+ ___block_literal_global.19721
+ ___block_literal_global.19986
+ ___block_literal_global.20.28195
+ ___block_literal_global.20492
+ ___block_literal_global.20559
+ ___block_literal_global.20830
+ ___block_literal_global.20911
+ ___block_literal_global.20960
+ ___block_literal_global.21.12449
+ ___block_literal_global.21005
+ ___block_literal_global.21021
+ ___block_literal_global.2105
+ ___block_literal_global.21312
+ ___block_literal_global.21587
+ ___block_literal_global.21718
+ ___block_literal_global.21824
+ ___block_literal_global.21836
+ ___block_literal_global.21914
+ ___block_literal_global.22.22949
+ ___block_literal_global.22090
+ ___block_literal_global.22137
+ ___block_literal_global.22353
+ ___block_literal_global.22530
+ ___block_literal_global.2272
+ ___block_literal_global.22835
+ ___block_literal_global.22891
+ ___block_literal_global.22946
+ ___block_literal_global.23020
+ ___block_literal_global.23049
+ ___block_literal_global.23139
+ ___block_literal_global.23224
+ ___block_literal_global.23264
+ ___block_literal_global.23391
+ ___block_literal_global.2357
+ ___block_literal_global.24.29323
+ ___block_literal_global.2420
+ ___block_literal_global.24293
+ ___block_literal_global.2467
+ ___block_literal_global.24761
+ ___block_literal_global.24933
+ ___block_literal_global.25.22950
+ ___block_literal_global.25424
+ ___block_literal_global.2568
+ ___block_literal_global.2582
+ ___block_literal_global.25968
+ ___block_literal_global.26.28184
+ ___block_literal_global.26022
+ ___block_literal_global.26297
+ ___block_literal_global.26368
+ ___block_literal_global.26523
+ ___block_literal_global.26849
+ ___block_literal_global.27.12450
+ ___block_literal_global.270
+ ___block_literal_global.27901
+ ___block_literal_global.2794
+ ___block_literal_global.28.17748
+ ___block_literal_global.2815
+ ___block_literal_global.28237
+ ___block_literal_global.2876
+ ___block_literal_global.28998
+ ___block_literal_global.29.22951
+ ___block_literal_global.29.23051
+ ___block_literal_global.29047
+ ___block_literal_global.29084
+ ___block_literal_global.29123
+ ___block_literal_global.293
+ ___block_literal_global.29328
+ ___block_literal_global.29427
+ ___block_literal_global.29578
+ ___block_literal_global.2968
+ ___block_literal_global.29687
+ ___block_literal_global.29783
+ ___block_literal_global.30.12451
+ ___block_literal_global.3019
+ ___block_literal_global.30341
+ ___block_literal_global.30526
+ ___block_literal_global.30612
+ ___block_literal_global.30983
+ ___block_literal_global.3240
+ ___block_literal_global.3430
+ ___block_literal_global.3586
+ ___block_literal_global.36.12452
+ ___block_literal_global.3751
+ ___block_literal_global.38.9007
+ ___block_literal_global.3829
+ ___block_literal_global.39.12453
+ ___block_literal_global.3983
+ ___block_literal_global.42.12454
+ ___block_literal_global.426.11812
+ ___block_literal_global.431.20711
+ ___block_literal_global.435
+ ___block_literal_global.44.16236
+ ___block_literal_global.454
+ ___block_literal_global.46.8999
+ ___block_literal_global.466
+ ___block_literal_global.481
+ ___block_literal_global.484
+ ___block_literal_global.4842
+ ___block_literal_global.5.30984
+ ___block_literal_global.527
+ ___block_literal_global.53.22508
+ ___block_literal_global.546
+ ___block_literal_global.5794
+ ___block_literal_global.5904
+ ___block_literal_global.6004
+ ___block_literal_global.6187
+ ___block_literal_global.6291
+ ___block_literal_global.6314
+ ___block_literal_global.6387
+ ___block_literal_global.67.2455
+ ___block_literal_global.67.8596
+ ___block_literal_global.6736
+ ___block_literal_global.679
+ ___block_literal_global.6880
+ ___block_literal_global.7.24294
+ ___block_literal_global.7.938
+ ___block_literal_global.7145
+ ___block_literal_global.7446
+ ___block_literal_global.797
+ ___block_literal_global.8.29421
+ ___block_literal_global.8.29784
+ ___block_literal_global.8.30985
+ ___block_literal_global.8341
+ ___block_literal_global.872
+ ___block_literal_global.8884
+ ___block_literal_global.9038
+ ___block_literal_global.9090
+ ___block_literal_global.9207
+ ___block_literal_global.9603
+ ___block_literal_global.9960
+ __audioStreamProvider:audioBufferAvailable:.heartbeat_CORESPEECH_OPUS_ENCODING_BEGIN
+ __audioStreamProvider:audioBufferAvailable:.heartbeat_CORESPEECH_OPUS_ENCODING_END
+ __audioStreamProvider:audioBufferAvailable:.heartbeat_CORESPEECH_SPEECH_MANAGER_LPCM_RECORD_BUFFER_AVAILABLE
+ __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.19686
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10745
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.19676
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.29983
+ __shouldSkipAudioChunkHandling.enableHeartbeat
+ __unnamed_array_storage.1209
+ __unnamed_array_storage.137
+ __unnamed_array_storage.144
+ __unnamed_array_storage.155
+ __unnamed_array_storage.165.24548
+ __unnamed_array_storage.176.24525
+ __unnamed_array_storage.177.24526
+ __unnamed_array_storage.200
+ __unnamed_array_storage.21
+ __unnamed_array_storage.21.28823
+ __unnamed_array_storage.22153
+ __unnamed_array_storage.22572
+ __unnamed_array_storage.226
+ __unnamed_array_storage.23228
+ __unnamed_array_storage.233
+ __unnamed_array_storage.24
+ __unnamed_array_storage.241
+ __unnamed_array_storage.24556
+ __unnamed_array_storage.249
+ __unnamed_array_storage.27666
+ __unnamed_array_storage.28832
+ __unnamed_array_storage.289
+ __unnamed_array_storage.296
+ __unnamed_array_storage.337
+ __unnamed_array_storage.38.23229
+ __unnamed_array_storage.41
+ __unnamed_array_storage.45
+ __unnamed_array_storage.48
+ __unnamed_array_storage.49
+ __unnamed_array_storage.6233
+ __unnamed_array_storage.626
+ __unnamed_array_storage.633
+ __unnamed_array_storage.634
+ __unnamed_array_storage.6375
+ __unnamed_array_storage.7450
+ _audit_stringMobileTimer.930
+ _close
+ _fstat
+ _kCSDiagnosticReporterEndpointDelayComponentsNegative
+ _kCSDiagnosticReporterEndpointDelayValuesNegative
+ _kVTEISecondPassRejectionMHUUID_block_invoke.enableHeartbeat.10766
+ _kVTEISecondPassRejectionMHUUID_block_invoke.enableHeartbeat.30044
+ _objc_msgSend$_alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:
+ _objc_msgSend$_audioStreamProvider:audioBufferAvailable:
+ _objc_msgSend$_compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:modelType:compilationFramework:
+ _objc_msgSend$_compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:compilationFramework:error:
+ _objc_msgSend$_getCachedIrsFromConfigFile:modelType:CSAsset:cachedIrDir:
+ _objc_msgSend$_handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:
+ _objc_msgSend$_isBnnsIrReadable:
+ _objc_msgSend$_isFirstPassSourceExclave:
+ _objc_msgSend$_notifyLanguageCodeChangeToExclaveKit
+ _objc_msgSend$_onDeviceCompilationWithConfigFile:locale:modelType:
+ _objc_msgSend$_processSecondPassInExclave:
+ _objc_msgSend$_purgeCachedIrExceptActiveCachedIrs:cachedIrDir:
+ _objc_msgSend$_purgeCachedIrFilesWithAsset:
+ _objc_msgSend$_reportVoiceTriggerFirstPassFireFromAPWithSource:voiceTriggerFirstPassInfo:
+ _objc_msgSend$_resetFirstExclaveAudioBufferMarkerIfNeeded
+ _objc_msgSend$_setActiveEndpointer:
+ _objc_msgSend$_shouldSkipAudioChunkHandling
+ _objc_msgSend$_startDetectTwoShot:
+ _objc_msgSend$_syncVoiceProfileEmbeddingsToExclave
+ _objc_msgSend$_voiceTriggerFirstPassInfoFromAP
+ _objc_msgSend$allObjects
+ _objc_msgSend$assetNamed:
+ _objc_msgSend$channelSelectionScores
+ _objc_msgSend$compileAndUpdateDeviceCachesWithAsset:assetType:modelType:deviceId:currentLocale:compileDirectory:errOut:
+ _objc_msgSend$compileModelWithMilFile:bnnsIrCachePath:compilationFramework:
+ _objc_msgSend$compileUsingConfig:locale:compileDirectory:modelType:errOut:
+ _objc_msgSend$compileWithMilFile:bnnsIrPath:
+ _objc_msgSend$contConvRecognizerConfigFiles
+ _objc_msgSend$dateWhenVoiceTriggerRePrompted
+ _objc_msgSend$deviceSupportsMagus
+ _objc_msgSend$exclaveClient
+ _objc_msgSend$exclaveRecordingNumSamples
+ _objc_msgSend$getAftmRecognizerConfigFromConfigDict:
+ _objc_msgSend$getAllMitigationConfigFiles
+ _objc_msgSend$getAllNldaConfigFiles
+ _objc_msgSend$getBertModelFile
+ _objc_msgSend$getModelCompiledDirWithModelType:basePath:
+ _objc_msgSend$getModelConfigsWithAsset:modelType:
+ _objc_msgSend$getModelFile
+ _objc_msgSend$getRecognizerConfigsFrom:
+ _objc_msgSend$initWithAssetManager:withUAFAssetManager:withUAFDownloadMonitor:withLanguageCodeUpdateMonitor:withAssetOverrideFlag:withOverrideAssetPath:disableOnDeviceCompilation:
+ _objc_msgSend$initWithConfigFile:errOut:
+ _objc_msgSend$initWithDefaultValue:completionBlock:
+ _objc_msgSend$initWithDisableOnDeviceCompilation
+ _objc_msgSend$initWithSiriRestrictionOnLockScreenMonitor:screenLockMonitor:voiceTriggerEnabledMonitor:CSPhoneCallStateMonitor:otherAppRecordingStateMonitor:siriClientBehaviorMonitor:srfUserSettingsMonitor:
+ _objc_msgSend$initWithSpeechManager:voiceTriggerEnabledPolicyHearst:
+ _objc_msgSend$isBlushingPhantomEnabled
+ _objc_msgSend$isExclaveHardware
+ _objc_msgSend$isMagusDisabledForLanguageCode:
+ _objc_msgSend$mitigatonConfigFile
+ _objc_msgSend$mmapModelWithConfig:mappedSizeOut:modelType:
+ _objc_msgSend$nldaConfigFile
+ _objc_msgSend$nldaConfigFileForCategory:
+ _objc_msgSend$notifyRequestCompletion
+ _objc_msgSend$observeAssetSet:queue:handler:
+ _objc_msgSend$otherAppRecordingStateMonitor
+ _objc_msgSend$pathWithComponents:
+ _objc_msgSend$phonecallStateMonitor
+ _objc_msgSend$processBargeInVoiceTriggerWithResult:
+ _objc_msgSend$processSecondPassVoiceTriggerWithShouldFlushAudio:result:
+ _objc_msgSend$progCheckerRecognizerConfigFiles
+ _objc_msgSend$purgeCachedIrForTrialAssetExcludingCurrentAsset:baseCachedIrDir:
+ _objc_msgSend$readMilFilePathFromConfig:modelType:
+ _objc_msgSend$resetFirstPassVoiceTrigger
+ _objc_msgSend$retrieveAssetSet:usages:
+ _objc_msgSend$screenLockMonitor
+ _objc_msgSend$setCacheMapWithMilFile:bnnsIr:
+ _objc_msgSend$setCachedAssetWithOverride:
+ _objc_msgSend$setCategory:withOptions:error:
+ _objc_msgSend$setIsFirstExclaveAudioBuffer:
+ _objc_msgSend$setRequestExclaveAudio:
+ _objc_msgSend$sharedClient
+ _objc_msgSend$shouldCompileForAssetType:
+ _objc_msgSend$siriClientBehaviorMonitor
+ _objc_msgSend$siriRestrictionOnLockScreenMonitor
+ _objc_msgSend$startBargeInVoiceTrigger
+ _objc_msgSend$startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:
+ _objc_msgSend$stopBargeInVoiceTrigger
+ _objc_msgSend$stopSecondPassVoiceTrigger
+ _objc_msgSend$submitEndpointerIssueReport:withContext:
+ _objc_msgSend$supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:
+ _objc_msgSend$supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:
+ _objc_msgSend$voiceTriggerEnabledMonitor
+ _setCachedAssetWithOverride:.overrideAsset
+ _sharedController.onceToken.11544
+ _sharedController.sharedController.11546
+ _sharedHandler.onceToken.1220
+ _sharedHandler.onceToken.20491
+ _sharedHandler.onceToken.29327
+ _sharedHandler.onceToken.6386
+ _sharedHandler.sharedHandler.1222
+ _sharedHandler.sharedHandler.20493
+ _sharedHandler.sharedHandler.29329
+ _sharedHandler.sharedHandler.6388
+ _sharedHandlerDisabledOnDeviceCompilation.onceToken.29322
+ _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.29324
+ _sharedInstance._sharedInstance.11378
+ _sharedInstance._sharedInstance.12667
+ _sharedInstance._sharedInstance.14593
+ _sharedInstance._sharedInstance.14776
+ _sharedInstance._sharedInstance.16285
+ _sharedInstance._sharedInstance.17221
+ _sharedInstance._sharedInstance.17491
+ _sharedInstance._sharedInstance.17780
+ _sharedInstance._sharedInstance.17856
+ _sharedInstance._sharedInstance.18054
+ _sharedInstance._sharedInstance.18830
+ _sharedInstance._sharedInstance.19082
+ _sharedInstance._sharedInstance.20961
+ _sharedInstance._sharedInstance.21588
+ _sharedInstance._sharedInstance.21719
+ _sharedInstance._sharedInstance.21915
+ _sharedInstance._sharedInstance.22354
+ _sharedInstance._sharedInstance.22892
+ _sharedInstance._sharedInstance.2358
+ _sharedInstance._sharedInstance.25969
+ _sharedInstance._sharedInstance.26023
+ _sharedInstance._sharedInstance.26850
+ _sharedInstance._sharedInstance.2795
+ _sharedInstance._sharedInstance.2877
+ _sharedInstance._sharedInstance.29048
+ _sharedInstance._sharedInstance.29085
+ _sharedInstance._sharedInstance.29579
+ _sharedInstance._sharedInstance.3020
+ _sharedInstance._sharedInstance.30527
+ _sharedInstance._sharedInstance.30613
+ _sharedInstance._sharedInstance.3241
+ _sharedInstance._sharedInstance.5795
+ _sharedInstance._sharedInstance.5905
+ _sharedInstance._sharedInstance.6005
+ _sharedInstance._sharedInstance.6292
+ _sharedInstance._sharedInstance.680
+ _sharedInstance._sharedInstance.6881
+ _sharedInstance._sharedInstance.798
+ _sharedInstance._sharedInstance.873
+ _sharedInstance._sharedInstance.8885
+ _sharedInstance._sharedInstance.9091
+ _sharedInstance.onceToken.10156
+ _sharedInstance.onceToken.10417
+ _sharedInstance.onceToken.10573
+ _sharedInstance.onceToken.11376
+ _sharedInstance.onceToken.12501
+ _sharedInstance.onceToken.12629
+ _sharedInstance.onceToken.12665
+ _sharedInstance.onceToken.13219
+ _sharedInstance.onceToken.1362
+ _sharedInstance.onceToken.14591
+ _sharedInstance.onceToken.1461
+ _sharedInstance.onceToken.14774
+ _sharedInstance.onceToken.15325
+ _sharedInstance.onceToken.15410
+ _sharedInstance.onceToken.15905
+ _sharedInstance.onceToken.16283
+ _sharedInstance.onceToken.17219
+ _sharedInstance.onceToken.17489
+ _sharedInstance.onceToken.17778
+ _sharedInstance.onceToken.17854
+ _sharedInstance.onceToken.17952
+ _sharedInstance.onceToken.18052
+ _sharedInstance.onceToken.18828
+ _sharedInstance.onceToken.18875
+ _sharedInstance.onceToken.189
+ _sharedInstance.onceToken.19080
+ _sharedInstance.onceToken.19110
+ _sharedInstance.onceToken.20829
+ _sharedInstance.onceToken.20910
+ _sharedInstance.onceToken.20959
+ _sharedInstance.onceToken.21311
+ _sharedInstance.onceToken.21586
+ _sharedInstance.onceToken.21717
+ _sharedInstance.onceToken.21913
+ _sharedInstance.onceToken.22089
+ _sharedInstance.onceToken.22352
+ _sharedInstance.onceToken.22834
+ _sharedInstance.onceToken.22890
+ _sharedInstance.onceToken.23019
+ _sharedInstance.onceToken.23138
+ _sharedInstance.onceToken.23263
+ _sharedInstance.onceToken.23390
+ _sharedInstance.onceToken.2356
+ _sharedInstance.onceToken.2419
+ _sharedInstance.onceToken.24760
+ _sharedInstance.onceToken.24932
+ _sharedInstance.onceToken.25423
+ _sharedInstance.onceToken.25967
+ _sharedInstance.onceToken.26021
+ _sharedInstance.onceToken.26367
+ _sharedInstance.onceToken.26522
+ _sharedInstance.onceToken.26848
+ _sharedInstance.onceToken.2793
+ _sharedInstance.onceToken.2814
+ _sharedInstance.onceToken.2875
+ _sharedInstance.onceToken.29046
+ _sharedInstance.onceToken.29083
+ _sharedInstance.onceToken.29122
+ _sharedInstance.onceToken.29577
+ _sharedInstance.onceToken.2967
+ _sharedInstance.onceToken.3018
+ _sharedInstance.onceToken.30340
+ _sharedInstance.onceToken.30525
+ _sharedInstance.onceToken.30611
+ _sharedInstance.onceToken.3239
+ _sharedInstance.onceToken.3585
+ _sharedInstance.onceToken.526
+ _sharedInstance.onceToken.5793
+ _sharedInstance.onceToken.5903
+ _sharedInstance.onceToken.6003
+ _sharedInstance.onceToken.6290
+ _sharedInstance.onceToken.66
+ _sharedInstance.onceToken.678
+ _sharedInstance.onceToken.6879
+ _sharedInstance.onceToken.796
+ _sharedInstance.onceToken.871
+ _sharedInstance.onceToken.8883
+ _sharedInstance.onceToken.9089
+ _sharedInstance.sSharedInstance.19112
+ _sharedInstance.sharedInstance.12503
+ _sharedInstance.sharedInstance.12631
+ _sharedInstance.sharedInstance.13221
+ _sharedInstance.sharedInstance.15412
+ _sharedInstance.sharedInstance.18877
+ _sharedInstance.sharedInstance.20831
+ _sharedInstance.sharedInstance.20912
+ _sharedInstance.sharedInstance.22091
+ _sharedInstance.sharedInstance.22836
+ _sharedInstance.sharedInstance.23021
+ _sharedInstance.sharedInstance.23265
+ _sharedInstance.sharedInstance.2421
+ _sharedInstance.sharedInstance.24934
+ _sharedInstance.sharedInstance.25425
+ _sharedInstance.sharedInstance.26524
+ _sharedInstance.sharedInstance.29124
+ _sharedInstance.sharedInstance.30342
+ _sharedInstance.sharedInstance.3587
+ _sharedInstance.sharedManager.21313
+ _sharedInstance.sharedManager.23392
+ _sharedInstance.sharedManager.28594
+ _sharedInstance.sharedPolicy.1364
+ _sharedInstance.sharedPolicy.23140
+ _sharedInstance.sharedPolicy.26369
+ _sharedInstance.sharedProvider.24762
+ _sharedManager.onceToken.17397
+ _sharedManager.onceToken.19985
+ _sharedManager.onceToken.7144
+ _sharedManager.sharedManager.17399
+ _sharedManager.sharedManager.7146
+ _sharedMonitor.onceToken.21823
+ _sharedMonitor.sharedMonitor.21825
+ _sharedService.onceToken.15961
+ _sharedService.onceToken.28236
+ _sharedService.sharedService.28238
- +[CSAVVoiceTriggerClientManager sharedVoiceTriggerClient]
- +[CSAlertBehaviorPredictor predictStartAlertBehaviorFor:avSystemController:hasAOP:supportVibrator:isiOS:isWatchOS:isHorseman:isBridgeOS:recordRoute:playbackRoute:]
- +[CSAlertBehaviorPredictor predictStartAlertBehaviorFor:recordRoute:playbackRoute:]
- +[CSAudioDeviceInfo supportsSecureCoding]
- +[CSAudioRecordDeviceInfo supportsSecureCoding]
- +[CSAudioRecorder _convertDeactivateOption:]
- +[CSAudioRecorder createSharedAudioSession]
- +[CSAudioRecorder resetDuckSettings]
- +[CSAudioRouteChangeMonitor sharedInstance]
- +[CSAudioSampleRateConverter downsampler]
- +[CSAudioSampleRateConverter upsampler]
- +[CSAudioServerCrashMonitor sharedInstance]
- +[CSAudioStartStreamOption(AVVC) avvcAlertOverrideType:]
- +[CSAudioStreamActivityMonitor sharedInstance]
- +[CSBluetoothManager sharedInstance]
- +[CSCXPhoneCallStateMonitor sharedInstance]
- +[CSCarKitUtils sharedInstance]
- +[CSDefaultAudioRouteChangeMonitorMac sharedInstance]
- +[CSHardwareLatencyHelper sharedInstance]
- +[CSMSNExceptionManager sharedInstance]
- +[CSMil2BnnsUtils _compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:error:]
- +[CSMil2BnnsUtils compileModelWithMilFile:bnnsIrCachePath:]
- +[CSMil2BnnsUtils mmapModelWithConfig:mappedSizeOut:]
- +[CSMil2BnnsUtils removeBnnsIrFromCacheMapWithMilFile:]
- +[CSMil2BnnsUtils setBnnsIrForCacheMap:withMilFile:]
- +[CSOnDeviceCompilationUtils readMilFilePathFromConfig:]
- +[CSPhoneCallStateMonitor sharedInstance]
- +[CSPhoneCallStateMonitorFactory phoneCallStateMonitor]
- +[CSRemoteDarwinDeviceInfo sharedInstance]
- +[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:recordingInfo:speechEvent:activationMode:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usesDeviceSpeakerForTTS:attemptsToUsePastDataBufferFrames:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isDeviceInCarDNDMode:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]
- +[CSSiriAudioSession currentInputDeviceUIDArray]
- +[CSSiriAudioSession sharedSession]
- +[CSSiriPreferences sharedPreferences]
- +[CSTUPhoneCallStateMonitor sharedInstance]
- +[CSUserSessionActiveMonitor sharedInstance]
- +[CSUtils(AudioHardware) hasRemoteBuiltInMic]
- +[CSUtils(AudioHardware) isRemoteDarwinWithDeviceId:]
- +[CSUtils(LanguageCode) getSiriLanguageWithEndpointId:fallbackLanguage:]
- +[CSUtils(LanguageCode) getSiriLanguageWithFallback:]
- +[CSUtils(RecordContext) isRecordContextAutoPrompt:]
- +[CSUtils(RecordContext) isRecordContextBuiltInVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextDarwinVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextHearstDoubleTap:]
- +[CSUtils(RecordContext) isRecordContextHearstVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextHomeButtonPress:]
- +[CSUtils(RecordContext) isRecordContextJarvisButtonPress:]
- +[CSUtils(RecordContext) isRecordContextJarvisVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextRaiseToSpeak:]
- +[CSUtils(RecordContext) isRecordContextRemoraVoiceTrigger:]
- +[CSUtils(RecordContext) isRecordContextSpeakerIdTrainingTrigger:]
- +[CSUtils(RecordContext) isRecordContextVoiceTrigger:]
- +[CSUtils(RecordContext) isValidRecordContext:]
- +[CSUtils(RecordContext) recordContextString:]
- +[CSVoiceTriggerEventInfoProvider isVoiceTriggerInfoAvailableLocally:]
- +[CSVoiceTriggerEventInfoProvider sharedInstance]
- +[CSVoiceTriggerStatAggregator sharedAggregator]
- -[AVVCAudioBuffer(remoteVoiceActivityVADBuffer) remoteVoiceActivityVADBuffer]
- -[AVVCContextSettings(debugDescription) debugDescription]
- -[AVVCStartRecordSettings(debugDescription) debugDescription]
- -[CSAudioDeviceInfo .cxx_destruct]
- -[CSAudioDeviceInfo copyWithZone:]
- -[CSAudioDeviceInfo description]
- -[CSAudioDeviceInfo encodeWithCoder:]
- -[CSAudioDeviceInfo initWithCoder:]
- -[CSAudioDeviceInfo initWithRecordDeviceInfo:playbackRoute:playbackDeviceTypeList:]
- -[CSAudioDeviceInfo initWithXPCObject:]
- -[CSAudioDeviceInfo playbackDeviceTypeList]
- -[CSAudioDeviceInfo playbackRoute]
- -[CSAudioDeviceInfo recordDeviceInfo]
- -[CSAudioDeviceInfo xpcObject]
- -[CSAudioFileReader .cxx_destruct]
- -[CSAudioFileReader _readAudioBufferAndFeed]
- -[CSAudioFileReader close]
- -[CSAudioFileReader dealloc]
- -[CSAudioFileReader delegate]
- -[CSAudioFileReader initWithURL:]
- -[CSAudioFileReader prepareRecording:]
- -[CSAudioFileReader readSamplesFromChannelIdx:]
- -[CSAudioFileReader setDelegate:]
- -[CSAudioFileReader setRecordBufferDuration:]
- -[CSAudioFileReader startRecording]
- -[CSAudioFileReader stopRecording]
- -[CSAudioPreprocessor .cxx_destruct]
- -[CSAudioPreprocessor _fetchCurrentMetrics]
- -[CSAudioPreprocessor _isNarrowBand:]
- -[CSAudioPreprocessor _reportMetrics]
- -[CSAudioPreprocessor beepCancellerDidCancelSamples:buffer:timestamp:]
- -[CSAudioPreprocessor beepCanceller]
- -[CSAudioPreprocessor delegate]
- -[CSAudioPreprocessor flush]
- -[CSAudioPreprocessor initWithSampleRate:withNumberOfChannels:]
- -[CSAudioPreprocessor numChannels]
- -[CSAudioPreprocessor processBuffer:atTime:arrivalTimestampToAudioRecorder:]
- -[CSAudioPreprocessor reportMetricsForSiriRequestWithUUID:]
- -[CSAudioPreprocessor resetWithSampleRate:containsVoiceTrigger:voiceTriggerInfo:]
- -[CSAudioPreprocessor sampleRate]
- -[CSAudioPreprocessor setBeepCanceller:]
- -[CSAudioPreprocessor setDelegate:]
- -[CSAudioPreprocessor setNumChannels:]
- -[CSAudioPreprocessor setSampleRate:]
- -[CSAudioPreprocessor setUpsampler:]
- -[CSAudioPreprocessor setZeroCounter:]
- -[CSAudioPreprocessor setZeroFilter:]
- -[CSAudioPreprocessor upsampler]
- -[CSAudioPreprocessor willBeepWithRecordRoute:playbackRoute:]
- -[CSAudioPreprocessor zeroCounter]
- -[CSAudioPreprocessor zeroFilter:zeroFilteredBufferAvailable:atHostTime:]
- -[CSAudioPreprocessor zeroFilter]
- -[CSAudioProvider .cxx_destruct]
- -[CSAudioProvider CSAudioServerCrashMonitorDidReceiveServerCrash:]
- -[CSAudioProvider CSAudioServerCrashMonitorDidReceiveServerRestart:]
- -[CSAudioProvider CSPhoneCallStateMonitor:didRecievePhoneCallStateChange:]
- -[CSAudioProvider UUID]
- -[CSAudioProvider _acquireListeningMicIndicatorLockFrom:]
- -[CSAudioProvider _acquireRecordModeLockFrom:]
- -[CSAudioProvider _activateAudioSessionWithReason:error:]
- -[CSAudioProvider _audioChunkFrom:to:]
- -[CSAudioProvider _audioChunkFrom:to:channelIdx:]
- -[CSAudioProvider _audioStreamWithRequest:streamName:error:]
- -[CSAudioProvider _canSetContext]
- -[CSAudioProvider _cancelAudioPacketWatchDog]
- -[CSAudioProvider _cancelAudioStreamHold:]
- -[CSAudioProvider _clearDidStartRecordingDelegateWatchDog]
- -[CSAudioProvider _clearDidStopRecordingDelegateWatchDog]
- -[CSAudioProvider _clearListeningMicIndicatorPropertyIfNeeded]
- -[CSAudioProvider _clearListeningMicIndicatorProperty]
- -[CSAudioProvider _createCircularBufferIfNeededWithNumChannel:playbackRoute:]
- -[CSAudioProvider _deactivateAudioSession:error:]
- -[CSAudioProvider _deliverHistoricalAudioToStreamsWithRemoteVAD:]
- -[CSAudioProvider _deliverPostprocessAudioChunk:toStream:lastForwardedSampleCount:]
- -[CSAudioProvider _didFireStreamHolderTimeout:]
- -[CSAudioProvider _didPlayStartAlertSoundForSiri:audioStream:]
- -[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]
- -[CSAudioProvider _fetchHistoricalAudioAndForwardToStream:remoteVAD:]
- -[CSAudioProvider _forceReleaseAllListeningMicIndicatorLocks]
- -[CSAudioProvider _forceReleaseAllRecordModeLocks]
- -[CSAudioProvider _forceReleaseListeningMicIndicatorLockFrom:]
- -[CSAudioProvider _forceReleaseRecordModeLockFrom:]
- -[CSAudioProvider _forwardAudioChunk:toStream:]
- -[CSAudioProvider _forwardAudioChunkForTV:toStream:]
- -[CSAudioProvider _handleAudioRecorderStreamHandleIdInvalidated:]
- -[CSAudioProvider _handleAudioSystemFailure]
- -[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]
- -[CSAudioProvider _handleDidStopAudioStreamWithReason:]
- -[CSAudioProvider _holdAudioStreamWithHolder:option:]
- -[CSAudioProvider _holdRecordingExceptionIfNeeded:]
- -[CSAudioProvider _holdRecordingTransactionIfNeeded]
- -[CSAudioProvider _isDuckingOnSpeakerOutputSupportedWithCurrentRoute]
- -[CSAudioProvider _onAudioPacketWatchdogFire]
- -[CSAudioProvider _postEpilogueAudioStream]
- -[CSAudioProvider _preEpilogueAudioStream]
- -[CSAudioProvider _prepareAudioStream:request:completion:]
- -[CSAudioProvider _prepareAudioStreamSync:request:error:]
- -[CSAudioProvider _processAudioBuffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]
- -[CSAudioProvider _releaseListeningMicIndicatorLock:]
- -[CSAudioProvider _releaseRecordModeLock:]
- -[CSAudioProvider _releaseRecordingTransactionIfNeeded]
- -[CSAudioProvider _resetCircularBufferStartTime]
- -[CSAudioProvider _saveRecordingBufferFrom:to:toURL:]
- -[CSAudioProvider _schduleDidStartRecordingDelegateWatchDogWithToken:]
- -[CSAudioProvider _scheduleAlertFinishTimeout:]
- -[CSAudioProvider _scheduleAudioPacketWatchDog]
- -[CSAudioProvider _scheduleDidStartRecordingDelegateWatchDog]
- -[CSAudioProvider _scheduleDidStopRecordingDelegateWatchDog:]
- -[CSAudioProvider _scheduleDidStopRecordingDelegateWatchDog]
- -[CSAudioProvider _setLatestRecordContext:]
- -[CSAudioProvider _setListeningMicIndicatorPropertyIfNeeded]
- -[CSAudioProvider _setListeningMicIndicatorProperty]
- -[CSAudioProvider _shouldDuckOnBuiltInSpeaker]
- -[CSAudioProvider _shouldHandleStartPendingOnStopping:withStopReason:]
- -[CSAudioProvider _shouldStopRecording]
- -[CSAudioProvider _startAudioStream:option:completion:]
- -[CSAudioProvider _stopAudioStream:option:completion:]
- -[CSAudioProvider _streamStateName:]
- -[CSAudioProvider _switchToListeningMode]
- -[CSAudioProvider _switchToRecordingMode]
- -[CSAudioProvider _updateRemoteDeviceIdFromAVVCIfNeeded]
- -[CSAudioProvider activateAudioSessionWithReason:dynamicAttribute:bundleID:error:]
- -[CSAudioProvider adpAssertion]
- -[CSAudioProvider alertDelegate]
- -[CSAudioProvider alertPlaybackFinishTimeoutToken]
- -[CSAudioProvider alertPlaybackFinishWaitingCompletions]
- -[CSAudioProvider alertPlaybackFinishWaitingStreams]
- -[CSAudioProvider alertStartTime]
- -[CSAudioProvider attachTandemStream:toPrimaryStream:completion:]
- -[CSAudioProvider audioChunkFrom:to:]
- -[CSAudioProvider audioChunkFrom:to:channelIdx:]
- -[CSAudioProvider audioChunkToEndFrom:]
- -[CSAudioProvider audioChunkToEndFrom:channelIdx:]
- -[CSAudioProvider audioDeviceInfo]
- -[CSAudioProvider audioMetric]
- -[CSAudioProvider audioPacketDeliveryCount]
- -[CSAudioProvider audioPacketWatchdog]
- -[CSAudioProvider audioPreprocessor:hasAvailableBuffer:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]
- -[CSAudioProvider audioPreprocessor]
- -[CSAudioProvider audioRecorder:didSetAudioSessionActive:]
- -[CSAudioProvider audioRecorder:willSetAudioSessionActive:]
- -[CSAudioProvider audioRecorderBeginRecordInterruption:]
- -[CSAudioProvider audioRecorderBeginRecordInterruption:withContext:]
- -[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:]
- -[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]
- -[CSAudioProvider audioRecorderBuiltInAudioStreamInvalidated:error:]
- -[CSAudioProvider audioRecorderDidFinishAlertPlayback:ofType:error:]
- -[CSAudioProvider audioRecorderDidStartRecord:audioStreamHandleId:successfully:error:]
- -[CSAudioProvider audioRecorderDidStopRecord:audioStreamHandleId:reason:]
- -[CSAudioProvider audioRecorderDisconnected:]
- -[CSAudioProvider audioRecorderEndRecordInterruption:]
- -[CSAudioProvider audioRecorderRecordHardwareConfigurationDidChange:toConfiguration:]
- -[CSAudioProvider audioRecorderStreamHandleIdInvalidated:]
- -[CSAudioProvider audioRecorderWillBeDestroyed:]
- -[CSAudioProvider audioRecorder]
- -[CSAudioProvider audioStreamHandleId]
- -[CSAudioProvider audioStreamId]
- -[CSAudioProvider audioStreamType]
- -[CSAudioProvider audioStreamWithRequest:streamName:completion:]
- -[CSAudioProvider audioStreamWithRequest:streamName:error:]
- -[CSAudioProvider audioSystemRecovering]
- -[CSAudioProvider audioTimeConverter]
- -[CSAudioProvider averagePowerForChannel:]
- -[CSAudioProvider cancelAudioStreamHold:]
- -[CSAudioProvider circularBufferInputRecordingDuration]
- -[CSAudioProvider circularBufferNumInputChannel]
- -[CSAudioProvider circularBufferStartHostTime]
- -[CSAudioProvider circularBufferStartSampleCount]
- -[CSAudioProvider circularBuffer]
- -[CSAudioProvider configureAlertBehavior:]
- -[CSAudioProvider currentSessionShouldDuckOnBuiltInSpeaker]
- -[CSAudioProvider deactivateAudioSession:error:]
- -[CSAudioProvider dealloc]
- -[CSAudioProvider enableMiniDucking:]
- -[CSAudioProvider enableSmartRoutingConsideration:]
- -[CSAudioProvider estimatedStartHostTime]
- -[CSAudioProvider historicalBufferRequestStreams]
- -[CSAudioProvider holdAudioStreamWithDescription:option:]
- -[CSAudioProvider initWithAudioStreamHandleId:audioStreamType:audioRecordContext:audioRecorder:]
- -[CSAudioProvider initWithAudioStreamHandleId:audioStreamType:audioRecordContext:audioRecorder:phoneCallStateMonitor:]
- -[CSAudioProvider isNarrowBand]
- -[CSAudioProvider isRecording]
- -[CSAudioProvider lastAudioRecorderContext]
- -[CSAudioProvider listeningMicIndicatorLocks]
- -[CSAudioProvider loggingQueue]
- -[CSAudioProvider micUsageReporter]
- -[CSAudioProvider notifyProviderContextChanged]
- -[CSAudioProvider peakPowerForChannel:]
- -[CSAudioProvider pendingStartCompletions]
- -[CSAudioProvider pendingStopCompletions]
- -[CSAudioProvider phoneCallStateMonitor]
- -[CSAudioProvider phoneCallState]
- -[CSAudioProvider playAlertSoundForType:]
- -[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]
- -[CSAudioProvider playbackRoute]
- -[CSAudioProvider prepareAudioStream:request:completion:]
- -[CSAudioProvider prepareAudioStreamSync:request:error:]
- -[CSAudioProvider prewarmAudioSessionWithError:]
- -[CSAudioProvider providerDelegate]
- -[CSAudioProvider recordDeviceIndicator]
- -[CSAudioProvider recordDeviceInfo]
- -[CSAudioProvider recordModeLocks]
- -[CSAudioProvider recordQueue]
- -[CSAudioProvider recordRoute]
- -[CSAudioProvider recordSettings]
- -[CSAudioProvider recordingTransaction]
- -[CSAudioProvider recordingWillStartGroup]
- -[CSAudioProvider saveRecordingBufferFrom:to:toURL:]
- -[CSAudioProvider saveRecordingBufferToEndFrom:toURL:]
- -[CSAudioProvider sessionDelegate]
- -[CSAudioProvider setAdpAssertion:]
- -[CSAudioProvider setAlertDelegate:]
- -[CSAudioProvider setAlertPlaybackFinishTimeoutToken:]
- -[CSAudioProvider setAlertPlaybackFinishWaitingCompletions:]
- -[CSAudioProvider setAlertPlaybackFinishWaitingStreams:]
- -[CSAudioProvider setAlertSoundFromURL:forType:force:]
- -[CSAudioProvider setAnnounceCallsEnabled:withStreamHandleID:]
- -[CSAudioProvider setAudioAlertDelegate:]
- -[CSAudioProvider setAudioPacketDeliveryCount:]
- -[CSAudioProvider setAudioPacketWatchdog:]
- -[CSAudioProvider setAudioPreprocessor:]
- -[CSAudioProvider setAudioProviderDelegate:]
- -[CSAudioProvider setAudioRecorder:]
- -[CSAudioProvider setAudioSessionDelegate:]
- -[CSAudioProvider setAudioStreamHandleId:]
- -[CSAudioProvider setAudioStreamType:]
- -[CSAudioProvider setAudioSystemRecovering:]
- -[CSAudioProvider setAudioTimeConverter:]
- -[CSAudioProvider setCircularBuffer:]
- -[CSAudioProvider setCircularBufferStartHostTime:]
- -[CSAudioProvider setCircularBufferStartSampleCount:]
- -[CSAudioProvider setCurrentContext:error:]
- -[CSAudioProvider setCurrentSessionShouldDuckOnBuiltInSpeaker:]
- -[CSAudioProvider setDuckOthersOption:]
- -[CSAudioProvider setEstimatedStartHostTime:]
- -[CSAudioProvider setHistoricalBufferRequestStreams:]
- -[CSAudioProvider setLastAudioRecorderContext:]
- -[CSAudioProvider setLatestRecordContext:streamType:]
- -[CSAudioProvider setListeningMicIndicatorLocks:]
- -[CSAudioProvider setLoggingQueue:]
- -[CSAudioProvider setMeteringEnabled:]
- -[CSAudioProvider setMicUsageReporter:]
- -[CSAudioProvider setPendingStartCompletions:]
- -[CSAudioProvider setPendingStopCompletions:]
- -[CSAudioProvider setPhoneCallState:]
- -[CSAudioProvider setPhoneCallStateMonitor:]
- -[CSAudioProvider setProviderDelegate:]
- -[CSAudioProvider setRecordDeviceIndicator:]
- -[CSAudioProvider setRecordModeLocks:]
- -[CSAudioProvider setRecordQueue:]
- -[CSAudioProvider setRecordingTransaction:]
- -[CSAudioProvider setRecordingWillStartGroup:]
- -[CSAudioProvider setSessionDelegate:]
- -[CSAudioProvider setStartPendingOnStoppingStreamToCompletionDict:]
- -[CSAudioProvider setStartPendingOnStoppingStreams:]
- -[CSAudioProvider setStartPendingStreams:]
- -[CSAudioProvider setStartRecordingWatchDogToken:]
- -[CSAudioProvider setStateCapture:]
- -[CSAudioProvider setStopPendingStreams:]
- -[CSAudioProvider setStopRecordingWatchDogToken:]
- -[CSAudioProvider setStreamHandleQueue:]
- -[CSAudioProvider setStreamHolders:]
- -[CSAudioProvider setStreamState:]
- -[CSAudioProvider setStreams:]
- -[CSAudioProvider setWaitingForAlertFinish:]
- -[CSAudioProvider startAudioStream:option:completion:]
- -[CSAudioProvider startPendingOnStoppingStreamToCompletionDict]
- -[CSAudioProvider startPendingOnStoppingStreams]
- -[CSAudioProvider startPendingStreams]
- -[CSAudioProvider startRecordingWatchDogToken]
- -[CSAudioProvider start]
- -[CSAudioProvider stateCapture]
- -[CSAudioProvider stopAudioStream:option:completion:]
- -[CSAudioProvider stopPendingStreams]
- -[CSAudioProvider stopRecordingWatchDogToken]
- -[CSAudioProvider streamHandleQueue]
- -[CSAudioProvider streamHolders]
- -[CSAudioProvider streamState]
- -[CSAudioProvider streams]
- -[CSAudioProvider supportsDuckingOnCurrentRouteWithError:]
- -[CSAudioProvider triggerInfoForContext:completion:]
- -[CSAudioProvider updateMeters]
- -[CSAudioProvider waitingForAlertFinish]
- -[CSAudioProviderRequestLock .cxx_destruct]
- -[CSAudioProviderRequestLock UUIDString]
- -[CSAudioProviderRequestLock clientIdentity]
- -[CSAudioProviderRequestLock initWithClientIdentity:]
- -[CSAudioRecordContext(AVVC) avvcContextSettings]
- -[CSAudioRecordDeviceIndicator .cxx_destruct]
- -[CSAudioRecordDeviceIndicator deviceId]
- -[CSAudioRecordDeviceIndicator initWithRecordContext:deviceId:shouldUseRemoteRecorder:streamHandleId:]
- -[CSAudioRecordDeviceIndicator recordContext]
- -[CSAudioRecordDeviceIndicator shouldUseRemoteRecorder]
- -[CSAudioRecordDeviceIndicator streamHandleId]
- -[CSAudioRecordDeviceIndicator updateDeviceId:]
- -[CSAudioRecordDeviceIndicator updateWithLatestRecordContext:]
- -[CSAudioRecordDeviceInfo .cxx_destruct]
- -[CSAudioRecordDeviceInfo copyWithZone:]
- -[CSAudioRecordDeviceInfo description]
- -[CSAudioRecordDeviceInfo encodeWithCoder:]
- -[CSAudioRecordDeviceInfo initWithAVVCRecordDeviceInfo:]
- -[CSAudioRecordDeviceInfo initWithCoder:]
- -[CSAudioRecordDeviceInfo initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:]
- -[CSAudioRecordDeviceInfo initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:]
- -[CSAudioRecordDeviceInfo initWithXPCObject:]
- -[CSAudioRecordDeviceInfo isRemoteDevice]
- -[CSAudioRecordDeviceInfo remoteDeviceProductIdentifier]
- -[CSAudioRecordDeviceInfo remoteDeviceUIDString]
- -[CSAudioRecordDeviceInfo remoteDeviceUID]
- -[CSAudioRecordDeviceInfo route]
- -[CSAudioRecordDeviceInfo xpcObject]
- -[CSAudioRecorder .cxx_destruct]
- -[CSAudioRecorder _audioIsFromRemoteAccessory:]
- -[CSAudioRecorder _audioRecorderDidStartRecordingSuccessfully:streamHandleID:error:]
- -[CSAudioRecorder _audioRecorderDidStopRecordingForReason:streamHandleID:]
- -[CSAudioRecorder _compensateChannelDataIfNeeded:receivedNumChannels:]
- -[CSAudioRecorder _createVoiceControllerWithError:]
- -[CSAudioRecorder _destroyVoiceController]
- -[CSAudioRecorder _fetchRemoteRecordClientWithDeviceId:streamHandleId:]
- -[CSAudioRecorder _getRecordSettingsWithRequest:]
- -[CSAudioRecorder _getVoiceController]
- -[CSAudioRecorder _hasLocalPendingTwoShot]
- -[CSAudioRecorder _isDarwinDeviceId:]
- -[CSAudioRecorder _logResourceNotAvailableErrorIfNeeded:]
- -[CSAudioRecorder _needResetAudioInjectionIndex:]
- -[CSAudioRecorder _processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:]
- -[CSAudioRecorder _processAudioChain:audioStreamHandleId:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]
- -[CSAudioRecorder _recordModeString:]
- -[CSAudioRecorder _shouldInjectAudio]
- -[CSAudioRecorder _shouldLogResourceNotAvailableError]
- -[CSAudioRecorder _shouldUseRemoteBuiltInMic:]
- -[CSAudioRecorder _startAudioStreamForAudioInjectionWithAVVCContext:]
- -[CSAudioRecorder _stopTrackingRemoteAccessoryStreamId:]
- -[CSAudioRecorder _trackRemoteAccessoryStreamIdIfNeeded:]
- -[CSAudioRecorder _updateLanguageCodeForRemoteVTEIResult:]
- -[CSAudioRecorder activateAudioSessionWithReason:streamHandleId:error:]
- -[CSAudioRecorder alertStartTime]
- -[CSAudioRecorder audioDecoderDidDecodePackets:audioStreamHandleId:buffer:remoteVAD:timestamp:arrivalTimestampToAudioRecorder:wasBuffered:receivedNumChannels:]
- -[CSAudioRecorder audioDeviceInfoWithStreamHandleId:recordDeviceIndicator:]
- -[CSAudioRecorder audioFileReaderBufferAvailable:buffer:atTime:]
- -[CSAudioRecorder audioFileReaderDidStartRecording:successfully:error:]
- -[CSAudioRecorder audioFileReaderDidStopRecording:forReason:]
- -[CSAudioRecorder averagePowerForChannel:]
- -[CSAudioRecorder clearListeningMicIndicatorProperty]
- -[CSAudioRecorder configureAlertBehavior:audioStreamHandleId:]
- -[CSAudioRecorder deactivateAudioSession:error:]
- -[CSAudioRecorder deactivateAudioSession:streamHandleId:error:]
- -[CSAudioRecorder dealloc]
- -[CSAudioRecorder enableMiniDucking:]
- -[CSAudioRecorder enableSmartRoutingConsiderationForStream:enable:]
- -[CSAudioRecorder fetchGibraltarVoiceTriggerInfoWithRecordDeviceIndicator:]
- -[CSAudioRecorder getPlaybackRouteForStreamID:]
- -[CSAudioRecorder initWithQueue:error:]
- -[CSAudioRecorder init]
- -[CSAudioRecorder isDuckingSupportedOnCurrentRouteWithStreamHandleID:error:]
- -[CSAudioRecorder isNarrowBandWithStreamHandleId:]
- -[CSAudioRecorder isRecordingWithRecordDeviceIndicator:]
- -[CSAudioRecorder isSessionCurrentlyActivated]
- -[CSAudioRecorder metrics]
- -[CSAudioRecorder observers]
- -[CSAudioRecorder peakPowerForChannel:]
- -[CSAudioRecorder playAlertSoundForType:overrideMode:]
- -[CSAudioRecorder playAlertSoundForType:recordDevideIndicator:]
- -[CSAudioRecorder playRecordStartingAlertAndResetEndpointerFromStream:withAlertOverride:]
- -[CSAudioRecorder prepareAudioStreamRecord:recordDeviceIndicator:error:]
- -[CSAudioRecorder prewarmAudioSessionWithStreamHandleId:error:]
- -[CSAudioRecorder queue]
- -[CSAudioRecorder recordDeviceInfoWithStreamHandleId:recordDeviceIndicator:]
- -[CSAudioRecorder recordRouteWithRecordDeviceIndicator:]
- -[CSAudioRecorder recordSettingsWithStreamHandleId:]
- -[CSAudioRecorder recordingSampleRateWithStreamHandleId:]
- -[CSAudioRecorder registerObserver:]
- -[CSAudioRecorder remoteAccessoryStreamIdSet]
- -[CSAudioRecorder remoteRecordConnectionDisconnected:]
- -[CSAudioRecorder remoteRecordDidStartRecordingWithStreamHandleId:error:]
- -[CSAudioRecorder remoteRecordDidStopRecordingWithWithStreamHandleId:error:]
- -[CSAudioRecorder remoteRecordLPCMBufferAvailable:streamHandleId:]
- -[CSAudioRecorder remoteRecordTwoShotDetectedAtTime:]
- -[CSAudioRecorder sessionEventDelegate]
- -[CSAudioRecorder setAlertSoundFromURL:forType:force:]
- -[CSAudioRecorder setAnnounceCallsEnabled:withStreamHandleID:]
- -[CSAudioRecorder setAudioSessionEventDelegate:]
- -[CSAudioRecorder setContext:completion:]
- -[CSAudioRecorder setCurrentContext:streamHandleId:error:]
- -[CSAudioRecorder setDuckMixWithOthersForStream:duckOthers:duckToLevelInDB:mixWithOthers:]
- -[CSAudioRecorder setListeningMicIndicatorProperty]
- -[CSAudioRecorder setMeteringEnabled:]
- -[CSAudioRecorder setObservers:]
- -[CSAudioRecorder setQueue:]
- -[CSAudioRecorder setRecordMode:streamHandleId:error:]
- -[CSAudioRecorder setRemoteAccessoryStreamIdSet:]
- -[CSAudioRecorder setSessionEventDelegate:]
- -[CSAudioRecorder setVoiceControllerCreationQueue:]
- -[CSAudioRecorder startAudioStreamWithOption:recordDeviceIndicator:error:]
- -[CSAudioRecorder stopAudioStreamWithRecordDeviceIndicator:error:]
- -[CSAudioRecorder unregisterObserver:]
- -[CSAudioRecorder updateMeters]
- -[CSAudioRecorder userSessionActivateMonitor:didReceivedUserSessionActiveHasChanged:]
- -[CSAudioRecorder voiceControllerAudioCallback:forStream:buffer:]
- -[CSAudioRecorder voiceControllerBeginRecordInterruption:]
- -[CSAudioRecorder voiceControllerBeginRecordInterruption:withContext:]
- -[CSAudioRecorder voiceControllerCreationQueue]
- -[CSAudioRecorder voiceControllerDidFinishAlertPlayback:ofType:error:]
- -[CSAudioRecorder voiceControllerDidSetAudioSessionActive:isActivated:]
- -[CSAudioRecorder voiceControllerDidStartRecording:forStream:successfully:error:]
- -[CSAudioRecorder voiceControllerDidStopRecording:forStream:forReason:]
- -[CSAudioRecorder voiceControllerEncoderErrorDidOccur:error:]
- -[CSAudioRecorder voiceControllerEndRecordInterruption:]
- -[CSAudioRecorder voiceControllerRecordHardwareConfigurationDidChange:toConfiguration:]
- -[CSAudioRecorder voiceControllerStreamInvalidated:forStream:]
- -[CSAudioRecorder voiceControllerWillSetAudioSessionActive:willActivate:]
- -[CSAudioRecorder willDestroy]
- -[CSAudioRouteChangeMonitor _startMonitoringWithQueue:]
- -[CSAudioRouteChangeMonitor _stopMonitoring]
- -[CSAudioRouteChangeMonitor carPlayConnected]
- -[CSAudioRouteChangeMonitor getHearstOwnershipStatus:]
- -[CSAudioRouteChangeMonitor getHearstRouteStatus:]
- -[CSAudioRouteChangeMonitor getJarvisConnected:]
- -[CSAudioRouteChangeMonitor hearstOwnership]
- -[CSAudioRouteChangeMonitor hearstRouteStatus]
- -[CSAudioRouteChangeMonitor jarvisConnected]
- -[CSAudioRouteChangeMonitor routeIsDoAPSupportedWithRouteUID:withCompletion:]
- -[CSAudioRouteChangeMonitorImpl .cxx_destruct]
- -[CSAudioRouteChangeMonitorImpl _fetchHearstConnectionState]
- -[CSAudioRouteChangeMonitorImpl _fetchHearstRouteStatusWithCompletion:]
- -[CSAudioRouteChangeMonitorImpl _fetchJarvisConnectionState]
- -[CSAudioRouteChangeMonitorImpl _notifyHearstRouteStatus:]
- -[CSAudioRouteChangeMonitorImpl _notifyJarvisConnectionState:]
- -[CSAudioRouteChangeMonitorImpl _startMonitoringWithQueue:]
- -[CSAudioRouteChangeMonitorImpl _startObservingAudioRouteChange]
- -[CSAudioRouteChangeMonitorImpl _startObservingSystemControllerLifecycle]
- -[CSAudioRouteChangeMonitorImpl _stopMonitoring]
- -[CSAudioRouteChangeMonitorImpl _systemControllerDied:]
- -[CSAudioRouteChangeMonitorImpl carPlayAuxStreamSupportDidChange:]
- -[CSAudioRouteChangeMonitorImpl carPlayConnected]
- -[CSAudioRouteChangeMonitorImpl carPlayIsConnectedDidChange:]
- -[CSAudioRouteChangeMonitorImpl getHearstOwnershipStatus:]
- -[CSAudioRouteChangeMonitorImpl getHearstRouteStatus:]
- -[CSAudioRouteChangeMonitorImpl getJarvisConnected:]
- -[CSAudioRouteChangeMonitorImpl hearstOwnership]
- -[CSAudioRouteChangeMonitorImpl hearstRouteStatus]
- -[CSAudioRouteChangeMonitorImpl init]
- -[CSAudioRouteChangeMonitorImpl jarvisConnected]
- -[CSAudioRouteChangeMonitorImpl pickableRoutesDidChange:]
- -[CSAudioRouteChangeMonitorImpl preferredExternalRouteDidChange:]
- -[CSAudioRouteChangeMonitorImplWatch .cxx_destruct]
- -[CSAudioRouteChangeMonitorImplWatch _fetchHearstRouteStatusWithCompletion:]
- -[CSAudioRouteChangeMonitorImplWatch _notifyHearstRouteStatus:]
- -[CSAudioRouteChangeMonitorImplWatch _startMonitoringWithQueue:]
- -[CSAudioRouteChangeMonitorImplWatch _startObservingAudioRouteChange]
- -[CSAudioRouteChangeMonitorImplWatch _startObservingSystemControllerLifecycle]
- -[CSAudioRouteChangeMonitorImplWatch _stopMonitoring]
- -[CSAudioRouteChangeMonitorImplWatch _systemControllerDied:]
- -[CSAudioRouteChangeMonitorImplWatch activeAudioRouteDidChange:]
- -[CSAudioRouteChangeMonitorImplWatch carPlayConnected]
- -[CSAudioRouteChangeMonitorImplWatch getHearstOwnershipStatus:]
- -[CSAudioRouteChangeMonitorImplWatch getHearstRouteStatus:]
- -[CSAudioRouteChangeMonitorImplWatch getJarvisConnected:]
- -[CSAudioRouteChangeMonitorImplWatch hearstOwnership]
- -[CSAudioRouteChangeMonitorImplWatch hearstRouteStatus]
- -[CSAudioRouteChangeMonitorImplWatch init]
- -[CSAudioRouteChangeMonitorImplWatch jarvisConnected]
- -[CSAudioSampleRateConverter _createSampleRateConverterWithInASBD:outASBD:]
- -[CSAudioSampleRateConverter convertSampleRateOfBuffer:]
- -[CSAudioSampleRateConverter dealloc]
- -[CSAudioSampleRateConverter initWithInASBD:outASBD:]
- -[CSAudioServerCrashMonitor _didReceiveMediaserverNotification:]
- -[CSAudioServerCrashMonitor _mediaserverdDidRestart]
- -[CSAudioServerCrashMonitor _notifyObserver:withMediaserverState:]
- -[CSAudioServerCrashMonitor _startMonitoringWithQueue:]
- -[CSAudioServerCrashMonitor init]
- -[CSAudioServerCrashMonitor serverState]
- -[CSAudioServerCrashMonitor setServerState:]
- -[CSAudioStartStreamOption(AVVC) _alertBehaviorTypeFromAVVCOverrideType:]
- -[CSAudioStartStreamOption(AVVC) adjustStartRecordingHostTime:]
- -[CSAudioStartStreamOption(AVVC) avvcAlertBehavior]
- -[CSAudioStartStreamOption(AVVC) avvcStartRecordSettingsWithAudioStreamHandleId:]
- -[CSAudioStartStreamOption(AVVC) isAlertBehaviorOverridedBeep]
- -[CSAudioStartStreamOption(AVVC) setAVVCAlertBehavior:]
- -[CSAudioStream .cxx_destruct]
- -[CSAudioStream UUID]
- -[CSAudioStream audioStreamProvider:audioBufferAvailable:]
- -[CSAudioStream audioStreamProvider:audioBufferAvailable:lastForwardedSampleCount:]
- -[CSAudioStream audioStreamProvider:audioChunkForTVAvailable:]
- -[CSAudioStream audioStreamProvider:didHardwareConfigurationChange:]
- -[CSAudioStream audioStreamProvider:didStopStreamUnexpectedly:]
- -[CSAudioStream dealloc]
- -[CSAudioStream delegate]
- -[CSAudioStream initWithAudioStreamProvider:streamName:streamRequest:]
- -[CSAudioStream isNarrowBand]
- -[CSAudioStream isStreaming]
- -[CSAudioStream isWeakStream]
- -[CSAudioStream lastForwardedSampleCount]
- -[CSAudioStream name]
- -[CSAudioStream needsBoost12dB]
- -[CSAudioStream prepareAudioStreamSyncWithRequest:error:]
- -[CSAudioStream prepareAudioStreamWithRequest:completion:]
- -[CSAudioStream recordSettings]
- -[CSAudioStream scheduledFutureSample]
- -[CSAudioStream setDelegate:]
- -[CSAudioStream setIsWeakStream:]
- -[CSAudioStream setName:]
- -[CSAudioStream setNeedsBoost12dB:]
- -[CSAudioStream setScheduledFutureSample:]
- -[CSAudioStream setStartStreamOption:]
- -[CSAudioStream setStreamProvider:]
- -[CSAudioStream setStreamRequest:]
- -[CSAudioStream setStreaming:]
- -[CSAudioStream setStreamingUUID:]
- -[CSAudioStream startAudioStreamWithOption:completion:]
- -[CSAudioStream startSampleCount]
- -[CSAudioStream startStreamOption]
- -[CSAudioStream stopAudioStreamWithOption:completion:]
- -[CSAudioStream streamProvider]
- -[CSAudioStream streamRequest]
- -[CSAudioStream streamingUUID]
- -[CSAudioStream streaming]
- -[CSAudioStream tandemStreams]
- -[CSAudioStream updateAudioStreamStartTimeInSampleCount:]
- -[CSAudioStreamActivityMonitor .cxx_destruct]
- -[CSAudioStreamActivityMonitor _startMonitoringWithQueue:]
- -[CSAudioStreamActivityMonitor _stopMonitoring]
- -[CSAudioStreamActivityMonitor hasNonVoiceTriggerStreamsActive]
- -[CSAudioStreamActivityMonitor hasNonVoiceTriggerStreamsOrStreamHoldersActive]
- -[CSAudioStreamActivityMonitor init]
- -[CSAudioStreamActivityMonitor notifyActiveStreamsChanged:streamHolders:streamId:]
- -[CSAudioStreamActivityMonitor queue]
- -[CSAudioStreamActivityMonitor setHasNonVoiceTriggerStreamsActive:]
- -[CSAudioStreamActivityMonitor setQueue:]
- -[CSAudioStreamHolding .cxx_destruct]
- -[CSAudioStreamHolding clientIdentity]
- -[CSAudioStreamHolding dealloc]
- -[CSAudioStreamHolding initWithName:clientIdentity:]
- -[CSAudioStreamHolding listeningMicIndicatorLockUUIDString]
- -[CSAudioStreamHolding name]
- -[CSAudioStreamHolding recordModeLockUUIDString]
- -[CSAudioStreamHolding setListeningMicIndicatorLockUUIDString:]
- -[CSAudioStreamHolding setRecordModeLockUUIDString:]
- -[CSAudioTandemStream .cxx_destruct]
- -[CSAudioTandemStream attachToPrimaryStreamWithCompletion:]
- -[CSAudioTandemStream initWithMasterAudioStream:name:]
- -[CSAudioTandemStream isStreaming]
- -[CSAudioTandemStream prepareAudioStreamSyncWithRequest:error:]
- -[CSAudioTandemStream prepareAudioStreamWithRequest:completion:]
- -[CSAudioTandemStream primaryStream]
- -[CSAudioTandemStream setPrimaryStream:]
- -[CSAudioTandemStream startAudioStreamWithOption:completion:]
- -[CSAudioTandemStream stopAudioStreamWithOption:completion:]
- -[CSBluetoothDeviceInfo .cxx_destruct]
- -[CSBluetoothDeviceInfo address]
- -[CSBluetoothDeviceInfo deviceIdentifier]
- -[CSBluetoothDeviceInfo isTemporaryPairedNotInContacts]
- -[CSBluetoothDeviceInfo setAddress:]
- -[CSBluetoothDeviceInfo setDeviceIdentifier:]
- -[CSBluetoothDeviceInfo setIsTemporaryPairedNotInContacts:]
- -[CSBluetoothDeviceInfo setSupportDoAP:]
- -[CSBluetoothDeviceInfo setSupportMph:]
- -[CSBluetoothDeviceInfo supportDoAP]
- -[CSBluetoothDeviceInfo supportMph]
- -[CSBluetoothManager .cxx_destruct]
- -[CSBluetoothManager _attachBluetoothSession]
- -[CSBluetoothManager _clearBluetoothDeviceInfoForDevice:]
- -[CSBluetoothManager _detachBluetoothSession]
- -[CSBluetoothManager _fetchAllConnectedDevices]
- -[CSBluetoothManager _getAddressWithBTDevice:]
- -[CSBluetoothManager _getBluetoothDeviceInfoForDeviceWithBTAddressString:]
- -[CSBluetoothManager _getConnectedBluetoothDeviceAddressesFromLocalDevice:]
- -[CSBluetoothManager _getWirelessSplitterInfoFromLocalDevice:]
- -[CSBluetoothManager _loadAACPCapabilityForDevice:deviceAddress:]
- -[CSBluetoothManager _sessionAttached:result:]
- -[CSBluetoothManager _sessionDetached:]
- -[CSBluetoothManager _sessionTerminated:]
- -[CSBluetoothManager _setBluetoothDeviceInfoForDevice:]
- -[CSBluetoothManager _setUpAccessoryManager]
- -[CSBluetoothManager _setUpLocalDevice]
- -[CSBluetoothManager _tearDownAccessoryManager]
- -[CSBluetoothManager _tearDownLocalDevice]
- -[CSBluetoothManager accessoryManager:accessoryEvent:device:accessoryState:]
- -[CSBluetoothManager accessoryManager]
- -[CSBluetoothManager bluetoothSessionSetupGroup]
- -[CSBluetoothManager bluetoothSession]
- -[CSBluetoothManager connectedDeviceAddresses]
- -[CSBluetoothManager device:serviceMask:serviceEventType:serviceSpecificEvent:result:]
- -[CSBluetoothManager deviceAddressToDeviceInfoMap]
- -[CSBluetoothManager getBTDeviceInfoWithBTAddressString:withCompletion:]
- -[CSBluetoothManager getBTLocalDeviceWithCompletion:]
- -[CSBluetoothManager getBluetoothDeviceInfoForDeviceWithId:]
- -[CSBluetoothManager getConnectedBluetoothDeviceAddressesWithCompletion:]
- -[CSBluetoothManager getWirelessSplitterInfoWithCompletion:]
- -[CSBluetoothManager init]
- -[CSBluetoothManager isAttachingBluetoothSession]
- -[CSBluetoothManager localDevice:event:result:]
- -[CSBluetoothManager localDevice]
- -[CSBluetoothManager observers]
- -[CSBluetoothManager pairedDeviceAddresses]
- -[CSBluetoothManager queue]
- -[CSBluetoothManager setAccessoryManager:]
- -[CSBluetoothManager setBluetoothSession:]
- -[CSBluetoothManager setBluetoothSessionSetupGroup:]
- -[CSBluetoothManager setConnectedDeviceAddresses:]
- -[CSBluetoothManager setDeviceAddressToDeviceInfoMap:]
- -[CSBluetoothManager setIsAttachingBluetoothSession:]
- -[CSBluetoothManager setLocalDevice:]
- -[CSBluetoothManager setObservers:]
- -[CSBluetoothManager setPairedDeviceAddresses:]
- -[CSBluetoothManager setQueue:]
- -[CSBluetoothWirelessSplitterInfo .cxx_destruct]
- -[CSBluetoothWirelessSplitterInfo _hasDeviceTemporaryPairedNotInContacts]
- -[CSBluetoothWirelessSplitterInfo addDeviceIntoSplitterDeviceList:]
- -[CSBluetoothWirelessSplitterInfo description]
- -[CSBluetoothWirelessSplitterInfo init]
- -[CSBluetoothWirelessSplitterInfo setSplitterEnabled:]
- -[CSBluetoothWirelessSplitterInfo shouldDisableSpeakerVerificationInSplitterMode]
- -[CSBluetoothWirelessSplitterInfo splitterDeviceList]
- -[CSBluetoothWirelessSplitterInfo splitterEnabled]
- -[CSBluetoothWirelessSplitterInfo splitterState]
- -[CSBuiltInVoiceTrigger _reportVoiceTriggerFirstPassFireFromAP]
- -[CSCXPhoneCallStateMonitor .cxx_destruct]
- -[CSCXPhoneCallStateMonitor _startMonitoringWithQueue:]
- -[CSCXPhoneCallStateMonitor _stopMonitoring]
- -[CSCXPhoneCallStateMonitor callObserver:callChanged:]
- -[CSCXPhoneCallStateMonitor callObserver]
- -[CSCXPhoneCallStateMonitor firstPartyCall]
- -[CSCXPhoneCallStateMonitor init]
- -[CSCXPhoneCallStateMonitor phoneCallState]
- -[CSCXPhoneCallStateMonitor setCallObserver:]
- -[CSCXPhoneCallStateMonitor setTuCallProviderManager:]
- -[CSCXPhoneCallStateMonitor tuCallProviderManager]
- -[CSCarKitUtils .cxx_destruct]
- -[CSCarKitUtils _delayBecauseCarKitSendsNotificationBeforeCapabilitiesActuallyReady]
- -[CSCarKitUtils _fetchCarCapabilitiesDict]
- -[CSCarKitUtils _fetchCarCapabilitiesInBackgroundWithCompletion:]
- -[CSCarKitUtils _invalidateCachedCarPlayCapabilities]
- -[CSCarKitUtils _isValidLatencyCorrectionValue:]
- -[CSCarKitUtils _latencyCorrectionSecondsForHeadUnit]
- -[CSCarKitUtils _recacheCarPlayCapabilitiesWithCompletion:]
- -[CSCarKitUtils _startObservingCarCapabilitiesNotfication:]
- -[CSCarKitUtils _updateCarPlayCapabilitiesDict]
- -[CSCarKitUtils _userInfoValueForKey:]
- -[CSCarKitUtils carPlayCapabilitiesDict]
- -[CSCarKitUtils dealloc]
- -[CSCarKitUtils handleCarCapabilitiesUpdatedWithCompletion:]
- -[CSCarKitUtils handleHeadUnitConnectedWithAsyncCompletion:]
- -[CSCarKitUtils init]
- -[CSCarKitUtils isCarPlayConnected]
- -[CSCarKitUtils isFlexibleFollowupDisabledForConnectedVehicle]
- -[CSCarKitUtils potentiallyAddHWLatencyToOption:streamHandle:voiceController:]
- -[CSDefaultAudioRouteChangeMonitorMac defaultOutputAudioDeviceID]
- -[CSDefaultAudioRouteChangeMonitorMac isDefaultInputBuiltInMic]
- -[CSDefaultAudioRouteChangeMonitorMac isDefaultOutputBultInSpeaker]
- -[CSEndpointerProxy _setFirstAudioSampleSensorHostTimeIfNeeded:]
- -[CSEndpointerProxy endpointMode]
- -[CSEndpointerProxy getFirstAudioSampleSensorHostTimeWithReply:]
- -[CSEndpointerProxy setEndpointMode:]
- -[CSEndpointerXPCClient getFirstAudioSampleSensorHostTimeWithReply:]
- -[CSHardwareLatencyHelper _adjustmentSecondsFromLatencyInfo:error:]
- -[CSHardwareLatencyHelper _hardwareLatenciesUsingStreamHandle:andVoiceController:]
- -[CSHardwareLatencyHelper _hardwareLatencyAdjustmentSeconds:hwLatencyType:error:]
- -[CSHardwareLatencyHelper _hardwareLatencyAdjustmentSecondsUsingStreamHandle:andVoiceController:]
- -[CSHardwareLatencyHelper _valuesAreMinimalyValidForInfoDictionary:type:]
- -[CSHardwareLatencyHelper addHWLatencyToOption:withCorrection:streamHandle:voiceController:]
- -[CSHybridEndpointAnalyzer endpointMode]
- -[CSHybridEndpointAnalyzer getFirstAudioSampleSensorHostTimeWithReply:]
- -[CSHybridEndpointAnalyzer setEndpointMode:]
- -[CSHybridEndpointer endpointMode]
- -[CSHybridEndpointer getFirstAudioSampleSensorHostTimeWithReply:]
- -[CSHybridEndpointer setEndpointMode:]
- -[CSMSNExceptionManager .cxx_destruct]
- -[CSMSNExceptionManager announceMessageExceptions]
- -[CSMSNExceptionManager beginAnnounceMessageException:reason:]
- -[CSMSNExceptionManager endAnnounceMessageException:reason:]
- -[CSMSNExceptionManager init]
- -[CSMSNExceptionManager queue]
- -[CSMSNExceptionManager setAnnounceMessageExceptions:]
- -[CSMSNExceptionManager setQueue:]
- -[CSMicUsageReporter .cxx_destruct]
- -[CSMicUsageReporter init]
- -[CSMicUsageReporter queue]
- -[CSMicUsageReporter reportMicUsage:]
- -[CSMicUsageReporter setQueue:]
- -[CSModelBenchmarker _onDeviceCompilationWithConfigFile:locale:]
- -[CSNNVADEndpointAnalyzer endpointMode]
- -[CSNNVADEndpointAnalyzer getFirstAudioSampleSensorHostTimeWithReply:]
- -[CSNNVADEndpointAnalyzer setEndpointMode:]
- -[CSOnDeviceCachedIrPurgingHandler purgeCachedIrForTrialAssetExcludingCurrentAsset:cachedIrDir:]
- -[CSOnDeviceCompilationHandler _compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:]
- -[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:]
- -[CSOnDeviceCompilationHandler compileUsingConfig:locale:compileDirectory:errOut:]
- -[CSPhoneCallStateMonitor firstPartyCall]
- -[CSPhoneCallStateMonitor phoneCallState]
- -[CSRemoteDarwinDeviceInfo .cxx_destruct]
- -[CSRemoteDarwinDeviceInfo _isRemoteDarwinConnectedWithUUID:]
- -[CSRemoteDarwinDeviceInfo addDeviceIDPairToMapTable:withDeviceUID:]
- -[CSRemoteDarwinDeviceInfo allDeviceDisconnected]
- -[CSRemoteDarwinDeviceInfo deviceConnectedWithUUID:]
- -[CSRemoteDarwinDeviceInfo deviceDisconnectedWithUUID:]
- -[CSRemoteDarwinDeviceInfo deviceUIDMapTable]
- -[CSRemoteDarwinDeviceInfo fetchDeviceUUIDStringFromUID:]
- -[CSRemoteDarwinDeviceInfo fetchRichDeviceUIDStringFromUUID:]
- -[CSRemoteDarwinDeviceInfo hasDarwinDeviceConnected]
- -[CSRemoteDarwinDeviceInfo hasDarwinDeviceHandleVoiceTrigger]
- -[CSRemoteDarwinDeviceInfo init]
- -[CSRemoteDarwinDeviceInfo isPrimaryVoiceTriggerDeviceWithUUID:]
- -[CSRemoteDarwinDeviceInfo isRemoteDarwinConnectedWithUUID:]
- -[CSRemoteDarwinDeviceInfo notifyVoiceTriggerDisabledWithDeviceUUID:]
- -[CSRemoteDarwinDeviceInfo notifyVoiceTriggerEnabledWithDeviceUUID:]
- -[CSRemoteDarwinDeviceInfo queue]
- -[CSRemoteDarwinDeviceInfo setDeviceUIDMapTable:]
- -[CSRemoteDarwinDeviceInfo setQueue:]
- -[CSRemoteDarwinDeviceInfo setVoiceTriggerEnabledDevices:]
- -[CSRemoteDarwinDeviceInfo voiceTriggerEnabledDevices]
- -[CSRemoteRecordClient .cxx_destruct]
- -[CSRemoteRecordClient _handleDidStartRecordingMessage:]
- -[CSRemoteRecordClient _handleServerError:]
- -[CSRemoteRecordClient _handleServerEvent:]
- -[CSRemoteRecordClient _handleServerMessage:]
- -[CSRemoteRecordClient _handleTwoShotDetectedMessage:]
- -[CSRemoteRecordClient audioStreamHandleId]
- -[CSRemoteRecordClient dealloc]
- -[CSRemoteRecordClient delegate]
- -[CSRemoteRecordClient deviceId]
- -[CSRemoteRecordClient device]
- -[CSRemoteRecordClient didDeviceConnect:]
- -[CSRemoteRecordClient didDeviceDisconnect:]
- -[CSRemoteRecordClient didPlayEndpointBeep]
- -[CSRemoteRecordClient hasPendingTwoShotBeep]
- -[CSRemoteRecordClient initWithDeviceId:audioStreamHandleId:]
- -[CSRemoteRecordClient initWithQueue:IsRemoteRecording:]
- -[CSRemoteRecordClient init]
- -[CSRemoteRecordClient isConnected]
- -[CSRemoteRecordClient isRecording]
- -[CSRemoteRecordClient isRemoteDeviceDarwin]
- -[CSRemoteRecordClient isRemoteDeviceGibraltar]
- -[CSRemoteRecordClient setDelegate:]
- -[CSRemoteRecordClient setDevice:]
- -[CSRemoteRecordClient startRecordingWithOptions:error:]
- -[CSRemoteRecordClient stopRecording:]
- -[CSRemoteRecordClient voiceTriggerEventInfo]
- -[CSRemoteRecordClient waitingForConnection:error:]
- -[CSSiriAudioRoute .cxx_destruct]
- -[CSSiriAudioRoute destination]
- -[CSSiriAudioRoute deviceName]
- -[CSSiriAudioRoute initWithAudioDeviceID:]
- -[CSSiriAudioRoute isBluetooth]
- -[CSSiriAudioRoute source]
- -[CSSiriAudioRoute uid]
- -[CSSiriAudioSession .cxx_destruct]
- -[CSSiriAudioSession currentInputRoute]
- -[CSSiriAudioSession currentOutputRoute]
- -[CSSiriAudioSession init]
- -[CSSiriPreferences .cxx_destruct]
- -[CSSiriPreferences initWithInstanceContext:]
- -[CSSiriPreferences init]
- -[CSSiriPreferences internalUserClassification]
- -[CSSiriPreferences overrideAudioSessionActiveDelay]
- -[CSSiriPreferences serverAudioSessionActivationDelayAboveMediaPlaybackVolumeThreshold]
- -[CSSiriPreferences serverAudioSessionActivationDelay]
- -[CSSiriPreferences serverMediaPlaybackVolumeThresholdForAudioSessionActivationDelay]
- -[CSSpeechController _audioStreamProvdider:audioBufferAvailable:]
- -[CSTUPhoneCallStateMonitor .cxx_destruct]
- -[CSTUPhoneCallStateMonitor _callStatusDidChangeHandler:]
- -[CSTUPhoneCallStateMonitor _fetchTUPhoneCallState]
- -[CSTUPhoneCallStateMonitor _registerPhoneCallStateChangeNotifier]
- -[CSTUPhoneCallStateMonitor _startMonitoringWithQueue:]
- -[CSTUPhoneCallStateMonitor _stopMonitoring]
- -[CSTUPhoneCallStateMonitor firstPartyCall]
- -[CSTUPhoneCallStateMonitor init]
- -[CSTUPhoneCallStateMonitor phoneCallState]
- -[CSTUPhoneCallStateMonitor queue]
- -[CSTUPhoneCallStateMonitor setQueue:]
- -[CSTUPhoneCallStateMonitor setTuCallCenter:]
- -[CSTUPhoneCallStateMonitor setTuPhoneCallState:]
- -[CSTUPhoneCallStateMonitor tuCallCenter]
- -[CSTUPhoneCallStateMonitor tuPhoneCallState]
- -[CSUserSessionActiveMonitor _startMonitoringWithQueue:]
- -[CSUserSessionActiveMonitor _stopMonitoring]
- -[CSUserSessionActiveMonitor isUserActive]
- -[CSVoiceTriggerAwareZeroFilter .cxx_destruct]
- -[CSVoiceTriggerAwareZeroFilter delegate]
- -[CSVoiceTriggerAwareZeroFilter flush]
- -[CSVoiceTriggerAwareZeroFilter init]
- -[CSVoiceTriggerAwareZeroFilter metrics]
- -[CSVoiceTriggerAwareZeroFilter numSamplesProcessed]
- -[CSVoiceTriggerAwareZeroFilter processBuffer:atTime:]
- -[CSVoiceTriggerAwareZeroFilter resetWithSampleRate:containsVoiceTrigger:voiceTriggerInfo:]
- -[CSVoiceTriggerAwareZeroFilter sampleRate]
- -[CSVoiceTriggerAwareZeroFilter setDelegate:]
- -[CSVoiceTriggerAwareZeroFilter setNumSamplesProcessed:]
- -[CSVoiceTriggerAwareZeroFilter setSampleRate:]
- -[CSVoiceTriggerAwareZeroFilter setVtEndInSampleCount:]
- -[CSVoiceTriggerAwareZeroFilter setZeroFilter:]
- -[CSVoiceTriggerAwareZeroFilter vtEndInSampleCount]
- -[CSVoiceTriggerAwareZeroFilter zeroFilter]
- -[CSVoiceTriggerEventInfoProvider .cxx_destruct]
- -[CSVoiceTriggerEventInfoProvider _isBuiltInDeviceFromDeviceId:]
- -[CSVoiceTriggerEventInfoProvider fetchVoiceTriggerInfoWithAudioContext:resultVoiceTriggerInfo:resultRTSTriggerInfo:]
- -[CSVoiceTriggerEventInfoProvider init]
- -[CSVoiceTriggerEventInfoProvider rtsTriggerInfo]
- -[CSVoiceTriggerEventInfoProvider setRtsTriggerInfo:]
- -[CSVoiceTriggerEventInfoProvider setTriggerNotifiedMachTime:]
- -[CSVoiceTriggerEventInfoProvider setVoiceTriggerInfo:deviceId:]
- -[CSVoiceTriggerEventInfoProvider triggerNotifiedMachTime]
- -[CSVoiceTriggerFirstPassHearst CSPhoneCallStateMonitor:didRecievePhoneCallStateChange:]
- -[CSVoiceTriggerFirstPassHearst initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:]
- -[CSVoiceTriggerFirstPassHearst otherAppRecordingStateMonitor]
- -[CSVoiceTriggerFirstPassHearst phoneCallStateMonitor]
- -[CSVoiceTriggerFirstPassHearst phoneCallState]
- -[CSVoiceTriggerFirstPassHearst setOtherAppRecordingStateMonitor:]
- -[CSVoiceTriggerFirstPassHearst setPhoneCallState:]
- -[CSVoiceTriggerFirstPassHearst setPhoneCallStateMonitor:]
- -[CSVoiceTriggerFirstPassHearst setVoiceTriggerEnabledMonitor:]
- -[CSVoiceTriggerFirstPassHearst voiceTriggerEnabledMonitor]
- -[CSVoiceTriggerStatAggregator .cxx_destruct]
- -[CSVoiceTriggerStatAggregator falseWakePhraseDictionary]
- -[CSVoiceTriggerStatAggregator init]
- -[CSVoiceTriggerStatAggregator lastAggTimeFalseWakeUp]
- -[CSVoiceTriggerStatAggregator logAOPFirstPassTriggerWakeupLatency:]
- -[CSVoiceTriggerStatAggregator logFalseWakeUp:withPhrase:]
- -[CSVoiceTriggerStatAggregator logSecondPassResult:eventInfo:triggerAPWakeUp:]
- -[CSVoiceTriggerStatAggregator logTimeBasedTriggerLengthSampleCountStatistics:withAOPVTTriggerLengthSampleCount:]
- -[CSVoiceTriggerStatAggregator numFalseWakeUp]
- -[CSVoiceTriggerStatAggregator reportDigitalZerosWithAudioZeroRun:]
- -[CSVoiceTriggerStatAggregator setFalseWakePhraseDictionary:]
- -[CSVoiceTriggerStatAggregator setLastAggTimeFalseWakeUp:]
- -[CSVoiceTriggerStatAggregator setNumFalseWakeUp:]
- -[NSArray(XPCObject) _cs_initWithXPCObject:]
- -[NSArray(XPCObject) _cs_xpcObject]
- -[NSData(XPCObject) _cs_initWithXPCObject:]
- -[NSData(XPCObject) _cs_xpcObject]
- -[NSDictionary(XPCObject) _cs_initWithXPCObject:]
- -[NSDictionary(XPCObject) _cs_xpcObject]
- -[NSHashTable(Indexing) _cs_isHashTableEmpty]
- -[NSNumber(XPCObject) _cs_initWithXPCObject:]
- -[NSNumber(XPCObject) _cs_xpcObject]
- -[NSString(XPCObject) _cs_initWithXPCObject:]
- -[NSString(XPCObject) _cs_xpcObject]
- GCC_except_table1260
- GCC_except_table1344
- GCC_except_table1356
- GCC_except_table1384
- GCC_except_table141
- GCC_except_table1593
- GCC_except_table1625
- GCC_except_table1646
- GCC_except_table1693
- GCC_except_table1717
- GCC_except_table1721
- GCC_except_table1737
- GCC_except_table1740
- GCC_except_table1768
- GCC_except_table1864
- GCC_except_table1866
- GCC_except_table1868
- GCC_except_table1874
- GCC_except_table1931
- GCC_except_table1963
- GCC_except_table2042
- GCC_except_table2062
- GCC_except_table213
- GCC_except_table2256
- GCC_except_table2394
- GCC_except_table2440
- GCC_except_table2443
- GCC_except_table2446
- GCC_except_table2451
- GCC_except_table2458
- GCC_except_table2463
- GCC_except_table2466
- GCC_except_table2493
- GCC_except_table2497
- GCC_except_table2609
- GCC_except_table2741
- GCC_except_table2785
- GCC_except_table2808
- GCC_except_table2811
- GCC_except_table2822
- GCC_except_table2863
- GCC_except_table2864
- GCC_except_table2865
- GCC_except_table2866
- GCC_except_table2867
- GCC_except_table2871
- GCC_except_table2872
- GCC_except_table2875
- GCC_except_table2878
- GCC_except_table2879
- GCC_except_table2881
- GCC_except_table2882
- GCC_except_table2891
- GCC_except_table2897
- GCC_except_table2899
- GCC_except_table2900
- GCC_except_table2966
- GCC_except_table3236
- GCC_except_table3322
- GCC_except_table3343
- GCC_except_table3361
- GCC_except_table3374
- GCC_except_table3395
- GCC_except_table3398
- GCC_except_table340
- GCC_except_table3401
- GCC_except_table3431
- GCC_except_table3492
- GCC_except_table3610
- GCC_except_table3721
- GCC_except_table3747
- GCC_except_table3809
- GCC_except_table3811
- GCC_except_table3813
- GCC_except_table3829
- GCC_except_table3831
- GCC_except_table3833
- GCC_except_table3837
- GCC_except_table3839
- GCC_except_table3841
- GCC_except_table3855
- GCC_except_table3861
- GCC_except_table3863
- GCC_except_table3898
- GCC_except_table393
- GCC_except_table394
- GCC_except_table396
- GCC_except_table397
- GCC_except_table398
- GCC_except_table399
- GCC_except_table400
- GCC_except_table401
- GCC_except_table403
- GCC_except_table4073
- GCC_except_table4097
- GCC_except_table411
- GCC_except_table4155
- GCC_except_table4190
- GCC_except_table4279
- GCC_except_table441
- GCC_except_table4542
- GCC_except_table4664
- GCC_except_table4687
- GCC_except_table4736
- GCC_except_table4742
- GCC_except_table4956
- GCC_except_table4960
- GCC_except_table5034
- GCC_except_table5041
- GCC_except_table5047
- GCC_except_table5116
- GCC_except_table5293
- GCC_except_table5327
- GCC_except_table5419
- GCC_except_table5431
- GCC_except_table5454
- GCC_except_table5548
- GCC_except_table5560
- GCC_except_table5569
- GCC_except_table5576
- GCC_except_table5582
- GCC_except_table5584
- GCC_except_table5587
- GCC_except_table5595
- GCC_except_table5597
- GCC_except_table5602
- GCC_except_table5604
- GCC_except_table5615
- GCC_except_table5616
- GCC_except_table5621
- GCC_except_table5627
- GCC_except_table5632
- GCC_except_table5634
- GCC_except_table5636
- GCC_except_table5638
- GCC_except_table5639
- GCC_except_table5640
- GCC_except_table5641
- GCC_except_table5643
- GCC_except_table5644
- GCC_except_table5645
- GCC_except_table5646
- GCC_except_table5647
- GCC_except_table5649
- GCC_except_table5650
- GCC_except_table5651
- GCC_except_table5653
- GCC_except_table5668
- GCC_except_table570
- GCC_except_table5741
- GCC_except_table5788
- GCC_except_table5792
- GCC_except_table5846
- GCC_except_table5875
- GCC_except_table5878
- GCC_except_table591
- GCC_except_table596
- GCC_except_table6076
- GCC_except_table6092
- GCC_except_table6100
- GCC_except_table6105
- GCC_except_table6122
- GCC_except_table6125
- GCC_except_table6129
- GCC_except_table6132
- GCC_except_table6142
- GCC_except_table6189
- GCC_except_table6196
- GCC_except_table635
- GCC_except_table640
- GCC_except_table641
- GCC_except_table642
- GCC_except_table6452
- GCC_except_table646
- GCC_except_table6479
- GCC_except_table6515
- GCC_except_table6524
- GCC_except_table6627
- GCC_except_table6633
- GCC_except_table666
- GCC_except_table667
- GCC_except_table668
- GCC_except_table674
- GCC_except_table6869
- GCC_except_table6873
- GCC_except_table6884
- GCC_except_table6906
- GCC_except_table6947
- GCC_except_table6955
- GCC_except_table6978
- GCC_except_table6985
- GCC_except_table6986
- GCC_except_table7045
- GCC_except_table7047
- GCC_except_table7058
- GCC_except_table7061
- GCC_except_table7064
- GCC_except_table7075
- GCC_except_table711
- GCC_except_table7211
- GCC_except_table7266
- GCC_except_table7423
- GCC_except_table7427
- GCC_except_table7496
- GCC_except_table7507
- GCC_except_table7509
- GCC_except_table7514
- GCC_except_table7516
- GCC_except_table7529
- GCC_except_table7536
- GCC_except_table7538
- GCC_except_table7556
- GCC_except_table7577
- GCC_except_table759
- GCC_except_table7666
- GCC_except_table7668
- GCC_except_table7669
- GCC_except_table7734
- GCC_except_table7738
- GCC_except_table7776
- GCC_except_table7777
- GCC_except_table7787
- GCC_except_table7788
- GCC_except_table779
- GCC_except_table7936
- GCC_except_table7954
- GCC_except_table7958
- GCC_except_table7963
- GCC_except_table7968
- GCC_except_table7975
- GCC_except_table7977
- GCC_except_table8005
- GCC_except_table8077
- GCC_except_table8089
- GCC_except_table8112
- GCC_except_table8123
- GCC_except_table8126
- GCC_except_table8149
- GCC_except_table8161
- GCC_except_table834
- GCC_except_table836
- GCC_except_table840
- GCC_except_table845
- GCC_except_table8532
- GCC_except_table8542
- GCC_except_table8603
- GCC_except_table8679
- GCC_except_table8689
- GCC_except_table8691
- GCC_except_table8692
- GCC_except_table8694
- GCC_except_table8701
- GCC_except_table8706
- GCC_except_table8707
- GCC_except_table8711
- GCC_except_table8712
- GCC_except_table8716
- GCC_except_table8717
- GCC_except_table8718
- GCC_except_table8719
- GCC_except_table8721
- GCC_except_table8722
- GCC_except_table8723
- GCC_except_table8724
- GCC_except_table8726
- GCC_except_table8728
- GCC_except_table8729
- GCC_except_table8758
- GCC_except_table8812
- GCC_except_table8836
- GCC_except_table8878
- GCC_except_table8889
- GCC_except_table9036
- GCC_except_table9044
- GCC_except_table9161
- GCC_except_table9183
- GCC_except_table9269
- GCC_except_table9323
- GCC_except_table9345
- GCC_except_table9370
- GCC_except_table9385
- GCC_except_table9392
- GCC_except_table9397
- GCC_except_table9412
- GCC_except_table9442
- GCC_except_table9596
- GCC_except_table9599
- GCC_except_table9604
- GCC_except_table9743
- GCC_except_table9750
- _AFPreferencesMobileUserSessionLanguage
- _AVLinearPCMIsNonInterleaved
- _AVSystemController_ActiveAudioRouteDidChangeNotification
- _AVSystemController_CarPlayAuxStreamSupportAttribute
- _AVSystemController_CarPlayAuxStreamSupportDidChangeNotification
- _AVSystemController_CarPlayIsConnectedAttribute
- _AVSystemController_CarPlayIsConnectedDidChangeNotification
- _AVSystemController_PickableRoutesAttribute
- _AVSystemController_PickableRoutesDidChangeNotification
- _AVSystemController_PreferredExternalRouteDidChangeNotification
- _AVSystemController_RouteDescriptionKey_BTDetails_IsHFPRoute
- _AVSystemController_RouteDescriptionKey_BTDetails_SupportsDoAP
- _AVSystemController_RouteDescriptionKey_IsPreferredExternalRoute
- _AVSystemController_RouteDescriptionKey_PreferredExternalRouteDetails_InEarDetectSupported
- _AVSystemController_RouteDescriptionKey_PreferredExternalRouteDetails_IsActive
- _AVSystemController_RouteDescriptionKey_RouteCurrentlyPicked
- _AVSystemController_RouteDescriptionKey_RouteUID
- _AVVCCurrentInputDeviceLatencyKey
- _AVVCCurrentOutputDeviceLatencyKey
- _AVVoiceActivationDeviceIDKey
- _AudioConverterFillComplexBuffer_BlockInvoke.29799
- _AudioConverterFillComplexBuffer_BlockInvoke.32235
- _AudioObjectAddPropertyListenerBlock
- _AudioObjectGetPropertyData
- _AudioObjectGetPropertyDataSize
- _AudioObjectRemovePropertyListenerBlock
- _BTAccessoryManagerGetAACPCapabilityInteger
- _BTDeviceAddressToString
- _BTDeviceIsTemporaryPairedNotInContacts
- _BTDeviceSupportsHS
- _BTLocalDeviceGetConnectedDevices
- _BTLocalDeviceGetSharingAddresses
- _BTLocalDeviceIsSharingEnabled
- _CFStringGetTypeID
- _CRSessionStatusCapabilitiesUpdatedNotificationCallback
- _CSSiriAudioSessionPortBluetoothA2DP
- _CSSiriAudioSessionPortBluetoothHFP
- _CSSiriAudioSessionPortBluetoothLE
- _CSSiriAudioSessionPortBuiltInMic
- _CSSiriAudioSessionPortBuiltInSpeaker
- _CSSiriAudioSessionPortHDMI
- _CSSiriAudioSessionPortHeadphones
- _CSSiriAudioSessionPortHeadsetMic
- _CSSiriAudioSessionPortLineIn
- _CSSiriAudioSessionPortOther
- _CSSiriAudioSessionPortUSBAudio
- _CSSiriRefreshDeviceExperimentGroup
- _CSSiriUserSupportBaseURL.once
- _CSSiriUserSupportBaseURL.sUserSupportBaseURL
- _CarKitLibrary
- _CarKitLibraryCore.frameworkLibrary
- _ExtAudioFileSeek
- _MediaSafetyNetLibrary
- _MediaSafetyNetLibraryCore.frameworkLibrary
- _MobileTimerLibrary.1228
- _MobileTimerLibraryCore.frameworkLibrary.1234
- _OBJC_CLASS_$_AVVCAudioBuffer
- _OBJC_CLASS_$_AVVCConfigureAlertBehaviorSettings
- _OBJC_CLASS_$_AVVCContextSettings
- _OBJC_CLASS_$_AVVCDuckOverride
- _OBJC_CLASS_$_AVVCDuckSettings
- _OBJC_CLASS_$_AVVCPrepareRecordSettings
- _OBJC_CLASS_$_AVVCStartRecordSettings
- _OBJC_CLASS_$_AVVoiceController
- _OBJC_CLASS_$_CESRAssetManager
- _OBJC_CLASS_$_CESRTrialAssetManager
- _OBJC_CLASS_$_CSADPPreventStandbyAssertion
- _OBJC_CLASS_$_CSAlertBehaviorPredictor
- _OBJC_CLASS_$_CSAudioFileReader
- _OBJC_CLASS_$_CSAudioPreprocessor
- _OBJC_CLASS_$_CSAudioProviderListeningMicIndicatorLock
- _OBJC_CLASS_$_CSAudioProviderRecordModeLock
- _OBJC_CLASS_$_CSAudioProviderRequestLock
- _OBJC_CLASS_$_CSAudioRecordDeviceIndicator
- _OBJC_CLASS_$_CSAudioRouteChangeMonitorImpl
- _OBJC_CLASS_$_CSAudioRouteChangeMonitorImplWatch
- _OBJC_CLASS_$_CSAudioStreamHolding
- _OBJC_CLASS_$_CSAudioTandemStream
- _OBJC_CLASS_$_CSAudioZeroFilter
- _OBJC_CLASS_$_CSBeepCanceller
- _OBJC_CLASS_$_CSBluetoothDeviceInfo
- _OBJC_CLASS_$_CSBluetoothWirelessSplitterInfo
- _OBJC_CLASS_$_CSCXPhoneCallStateMonitor
- _OBJC_CLASS_$_CSDarwinVoiceTriggerEventInfoProvider
- _OBJC_CLASS_$_CSDefaultAudioRouteChangeMonitorMac
- _OBJC_CLASS_$_CSHardwareLatencyHelper
- _OBJC_CLASS_$_CSMSNExceptionManager
- _OBJC_CLASS_$_CSMicUsageReporter
- _OBJC_CLASS_$_CSPhoneCallStateMonitor
- _OBJC_CLASS_$_CSRemoteRecordClient
- _OBJC_CLASS_$_CSReusableBufferPool
- _OBJC_CLASS_$_CSReusableBufferPoolConfiguration
- _OBJC_CLASS_$_CSSiriAudioRoute
- _OBJC_CLASS_$_CSSiriAudioSession
- _OBJC_CLASS_$_CSTUPhoneCallStateMonitor
- _OBJC_CLASS_$_CXCallObserver
- _OBJC_CLASS_$_NSMutableOrderedSet
- _OBJC_CLASS_$_TUCallCenter
- _OBJC_CLASS_$_TUCallProviderManager
- _OBJC_CLASS_$_UAFAssetSet
- _OBJC_CLASS_$_UAFAssetSetObserver
- _OBJC_IVAR_$_CSAudioDeviceInfo._playbackDeviceTypeList
- _OBJC_IVAR_$_CSAudioDeviceInfo._playbackRoute
- _OBJC_IVAR_$_CSAudioDeviceInfo._recordDeviceInfo
- _OBJC_IVAR_$_CSAudioFileReader._audioFeedTimer
- _OBJC_IVAR_$_CSAudioFileReader._bufferDuration
- _OBJC_IVAR_$_CSAudioFileReader._delegate
- _OBJC_IVAR_$_CSAudioFileReader._fFile
- _OBJC_IVAR_$_CSAudioFileReader._outASBD
- _OBJC_IVAR_$_CSAudioFileReader._queue
- _OBJC_IVAR_$_CSAudioPreprocessor._beepCanceller
- _OBJC_IVAR_$_CSAudioPreprocessor._delegate
- _OBJC_IVAR_$_CSAudioPreprocessor._numChannels
- _OBJC_IVAR_$_CSAudioPreprocessor._sampleRate
- _OBJC_IVAR_$_CSAudioPreprocessor._upsampler
- _OBJC_IVAR_$_CSAudioPreprocessor._zeroCounter
- _OBJC_IVAR_$_CSAudioPreprocessor._zeroFilter
- _OBJC_IVAR_$_CSAudioProvider._UUID
- _OBJC_IVAR_$_CSAudioProvider._adpAssertion
- _OBJC_IVAR_$_CSAudioProvider._alertDelegate
- _OBJC_IVAR_$_CSAudioProvider._alertPlaybackFinishTimeoutToken
- _OBJC_IVAR_$_CSAudioProvider._alertPlaybackFinishWaitingCompletions
- _OBJC_IVAR_$_CSAudioProvider._alertPlaybackFinishWaitingStreams
- _OBJC_IVAR_$_CSAudioProvider._audioPacketDeliveryCount
- _OBJC_IVAR_$_CSAudioProvider._audioPacketWatchdog
- _OBJC_IVAR_$_CSAudioProvider._audioPreprocessor
- _OBJC_IVAR_$_CSAudioProvider._audioRecorder
- _OBJC_IVAR_$_CSAudioProvider._audioStreamHandleId
- _OBJC_IVAR_$_CSAudioProvider._audioStreamType
- _OBJC_IVAR_$_CSAudioProvider._audioSystemRecovering
- _OBJC_IVAR_$_CSAudioProvider._audioTimeConverter
- _OBJC_IVAR_$_CSAudioProvider._circularBuffer
- _OBJC_IVAR_$_CSAudioProvider._circularBufferStartHostTime
- _OBJC_IVAR_$_CSAudioProvider._circularBufferStartSampleCount
- _OBJC_IVAR_$_CSAudioProvider._currentSessionShouldDuckOnBuiltInSpeaker
- _OBJC_IVAR_$_CSAudioProvider._estimatedStartHostTime
- _OBJC_IVAR_$_CSAudioProvider._historicalBufferRequestStreams
- _OBJC_IVAR_$_CSAudioProvider._lastAudioRecorderContext
- _OBJC_IVAR_$_CSAudioProvider._listeningMicIndicatorLocks
- _OBJC_IVAR_$_CSAudioProvider._loggingQueue
- _OBJC_IVAR_$_CSAudioProvider._micUsageReporter
- _OBJC_IVAR_$_CSAudioProvider._pendingStartCompletions
- _OBJC_IVAR_$_CSAudioProvider._pendingStopCompletions
- _OBJC_IVAR_$_CSAudioProvider._phoneCallState
- _OBJC_IVAR_$_CSAudioProvider._phoneCallStateMonitor
- _OBJC_IVAR_$_CSAudioProvider._providerDelegate
- _OBJC_IVAR_$_CSAudioProvider._recordDeviceIndicator
- _OBJC_IVAR_$_CSAudioProvider._recordModeLocks
- _OBJC_IVAR_$_CSAudioProvider._recordQueue
- _OBJC_IVAR_$_CSAudioProvider._recordingTransaction
- _OBJC_IVAR_$_CSAudioProvider._recordingWillStartGroup
- _OBJC_IVAR_$_CSAudioProvider._sessionDelegate
- _OBJC_IVAR_$_CSAudioProvider._startPendingOnStoppingStreamToCompletionDict
- _OBJC_IVAR_$_CSAudioProvider._startPendingOnStoppingStreams
- _OBJC_IVAR_$_CSAudioProvider._startPendingStreams
- _OBJC_IVAR_$_CSAudioProvider._startRecordingWatchDogToken
- _OBJC_IVAR_$_CSAudioProvider._stateCapture
- _OBJC_IVAR_$_CSAudioProvider._stopPendingStreams
- _OBJC_IVAR_$_CSAudioProvider._stopRecordingWatchDogToken
- _OBJC_IVAR_$_CSAudioProvider._streamHandleQueue
- _OBJC_IVAR_$_CSAudioProvider._streamHolders
- _OBJC_IVAR_$_CSAudioProvider._streamState
- _OBJC_IVAR_$_CSAudioProvider._streams
- _OBJC_IVAR_$_CSAudioProvider._waitingForAlertFinish
- _OBJC_IVAR_$_CSAudioProviderRequestLock._UUIDString
- _OBJC_IVAR_$_CSAudioProviderRequestLock._clientIdentity
- _OBJC_IVAR_$_CSAudioRecordDeviceIndicator._deviceId
- _OBJC_IVAR_$_CSAudioRecordDeviceIndicator._recordContext
- _OBJC_IVAR_$_CSAudioRecordDeviceIndicator._shouldUseRemoteRecorder
- _OBJC_IVAR_$_CSAudioRecordDeviceIndicator._streamHandleId
- _OBJC_IVAR_$_CSAudioRecordDeviceInfo._isRemoteDevice
- _OBJC_IVAR_$_CSAudioRecordDeviceInfo._remoteDeviceProductIdentifier
- _OBJC_IVAR_$_CSAudioRecordDeviceInfo._remoteDeviceUID
- _OBJC_IVAR_$_CSAudioRecordDeviceInfo._remoteDeviceUIDString
- _OBJC_IVAR_$_CSAudioRecordDeviceInfo._route
- _OBJC_IVAR_$_CSAudioRecorder._audioBufferPool
- _OBJC_IVAR_$_CSAudioRecorder._audioFilePathIndex
- _OBJC_IVAR_$_CSAudioRecorder._audioFileReader
- _OBJC_IVAR_$_CSAudioRecorder._hasSetAlertDictionary
- _OBJC_IVAR_$_CSAudioRecorder._interleavedABL
- _OBJC_IVAR_$_CSAudioRecorder._observers
- _OBJC_IVAR_$_CSAudioRecorder._opusDecoders
- _OBJC_IVAR_$_CSAudioRecorder._pNonInterleavedABL
- _OBJC_IVAR_$_CSAudioRecorder._pendingTwoShotVTToken
- _OBJC_IVAR_$_CSAudioRecorder._queue
- _OBJC_IVAR_$_CSAudioRecorder._remoteAccessoryStreamIdSet
- _OBJC_IVAR_$_CSAudioRecorder._remoteRecordClient
- _OBJC_IVAR_$_CSAudioRecorder._sessionEventDelegate
- _OBJC_IVAR_$_CSAudioRecorder._voiceController
- _OBJC_IVAR_$_CSAudioRecorder._voiceControllerCreationQueue
- _OBJC_IVAR_$_CSAudioRecorder._waitingForDidStart
- _OBJC_IVAR_$_CSAudioRouteChangeMonitorImpl._hearstRouteStatus
- _OBJC_IVAR_$_CSAudioRouteChangeMonitorImpl._isJarvisConnected
- _OBJC_IVAR_$_CSAudioRouteChangeMonitorImpl._queue
- _OBJC_IVAR_$_CSAudioRouteChangeMonitorImplWatch._hearstRouteStatus
- _OBJC_IVAR_$_CSAudioRouteChangeMonitorImplWatch._queue
- _OBJC_IVAR_$_CSAudioSampleRateConverter._inASBD
- _OBJC_IVAR_$_CSAudioSampleRateConverter._outASBD
- _OBJC_IVAR_$_CSAudioSampleRateConverter._outBufferScaleFactor
- _OBJC_IVAR_$_CSAudioSampleRateConverter._sampleRateConverter
- _OBJC_IVAR_$_CSAudioServerCrashMonitor._serverState
- _OBJC_IVAR_$_CSAudioStream._UUID
- _OBJC_IVAR_$_CSAudioStream._delegate
- _OBJC_IVAR_$_CSAudioStream._isWeakStream
- _OBJC_IVAR_$_CSAudioStream._lastForwardedSampleCount
- _OBJC_IVAR_$_CSAudioStream._name
- _OBJC_IVAR_$_CSAudioStream._needsBoost12dB
- _OBJC_IVAR_$_CSAudioStream._scheduledFutureSample
- _OBJC_IVAR_$_CSAudioStream._startSampleCount
- _OBJC_IVAR_$_CSAudioStream._startStreamOption
- _OBJC_IVAR_$_CSAudioStream._streamProvider
- _OBJC_IVAR_$_CSAudioStream._streamRequest
- _OBJC_IVAR_$_CSAudioStream._streaming
- _OBJC_IVAR_$_CSAudioStream._streamingUUID
- _OBJC_IVAR_$_CSAudioStream._tandemStreams
- _OBJC_IVAR_$_CSAudioStreamActivityMonitor._hasNonVoiceTriggerStreamsActive
- _OBJC_IVAR_$_CSAudioStreamActivityMonitor._queue
- _OBJC_IVAR_$_CSAudioStreamHolding._clientIdentity
- _OBJC_IVAR_$_CSAudioStreamHolding._listeningMicIndicatorLockUUIDString
- _OBJC_IVAR_$_CSAudioStreamHolding._name
- _OBJC_IVAR_$_CSAudioStreamHolding._recordModeLockUUIDString
- _OBJC_IVAR_$_CSAudioTandemStream._primaryStream
- _OBJC_IVAR_$_CSBluetoothDeviceInfo._address
- _OBJC_IVAR_$_CSBluetoothDeviceInfo._deviceIdentifier
- _OBJC_IVAR_$_CSBluetoothDeviceInfo._isTemporaryPairedNotInContacts
- _OBJC_IVAR_$_CSBluetoothDeviceInfo._supportDoAP
- _OBJC_IVAR_$_CSBluetoothDeviceInfo._supportMph
- _OBJC_IVAR_$_CSBluetoothManager._accessoryManager
- _OBJC_IVAR_$_CSBluetoothManager._bluetoothSession
- _OBJC_IVAR_$_CSBluetoothManager._bluetoothSessionSetupGroup
- _OBJC_IVAR_$_CSBluetoothManager._connectedDeviceAddresses
- _OBJC_IVAR_$_CSBluetoothManager._deviceAddressToDeviceInfoMap
- _OBJC_IVAR_$_CSBluetoothManager._isAttachingBluetoothSession
- _OBJC_IVAR_$_CSBluetoothManager._localDevice
- _OBJC_IVAR_$_CSBluetoothManager._observers
- _OBJC_IVAR_$_CSBluetoothManager._pairedDeviceAddresses
- _OBJC_IVAR_$_CSBluetoothManager._queue
- _OBJC_IVAR_$_CSBluetoothWirelessSplitterInfo._splitterDeviceList
- _OBJC_IVAR_$_CSBluetoothWirelessSplitterInfo._splitterEnabled
- _OBJC_IVAR_$_CSCXPhoneCallStateMonitor._callObserver
- _OBJC_IVAR_$_CSCXPhoneCallStateMonitor._tuCallProviderManager
- _OBJC_IVAR_$_CSCarKitUtils._carCapabilitiesLock
- _OBJC_IVAR_$_CSCarKitUtils._carPlayCapabilitiesDict
- _OBJC_IVAR_$_CSCarKitUtils._queue
- _OBJC_IVAR_$_CSHybridEndpointAnalyzer._endpointMode
- _OBJC_IVAR_$_CSHybridEndpointer._endpointMode
- _OBJC_IVAR_$_CSMSNExceptionManager._announceMessageExceptions
- _OBJC_IVAR_$_CSMSNExceptionManager._queue
- _OBJC_IVAR_$_CSMicUsageReporter._queue
- _OBJC_IVAR_$_CSNNVADEndpointAnalyzer._endpointMode
- _OBJC_IVAR_$_CSRemoteDarwinDeviceInfo._deviceUIDMapTable
- _OBJC_IVAR_$_CSRemoteDarwinDeviceInfo._queue
- _OBJC_IVAR_$_CSRemoteDarwinDeviceInfo._voiceTriggerEnabledDevices
- _OBJC_IVAR_$_CSRemoteRecordClient._audioStreamHandleId
- _OBJC_IVAR_$_CSRemoteRecordClient._connection
- _OBJC_IVAR_$_CSRemoteRecordClient._delegate
- _OBJC_IVAR_$_CSRemoteRecordClient._device
- _OBJC_IVAR_$_CSRemoteRecordClient._deviceBrowser
- _OBJC_IVAR_$_CSRemoteRecordClient._deviceId
- _OBJC_IVAR_$_CSRemoteRecordClient._deviceWaitingGroup
- _OBJC_IVAR_$_CSRemoteRecordClient._isRemoteRecording
- _OBJC_IVAR_$_CSRemoteRecordClient._queue
- _OBJC_IVAR_$_CSSiriAudioRoute._destination
- _OBJC_IVAR_$_CSSiriAudioRoute._deviceName
- _OBJC_IVAR_$_CSSiriAudioRoute._isBluetooth
- _OBJC_IVAR_$_CSSiriAudioRoute._source
- _OBJC_IVAR_$_CSSiriAudioRoute._uid
- _OBJC_IVAR_$_CSSiriAudioSession._inputRoute
- _OBJC_IVAR_$_CSSiriAudioSession._outputRoute
- _OBJC_IVAR_$_CSSiriAudioSession._queue
- _OBJC_IVAR_$_CSSiriPreferences._instanceContext
- _OBJC_IVAR_$_CSSiriPreferences._queue
- _OBJC_IVAR_$_CSTUPhoneCallStateMonitor._queue
- _OBJC_IVAR_$_CSTUPhoneCallStateMonitor._tuCallCenter
- _OBJC_IVAR_$_CSTUPhoneCallStateMonitor._tuPhoneCallState
- _OBJC_IVAR_$_CSUAFAssetManager._locale
- _OBJC_IVAR_$_CSUAFDownloadMonitor._observer
- _OBJC_IVAR_$_CSVoiceTriggerAwareZeroFilter._delegate
- _OBJC_IVAR_$_CSVoiceTriggerAwareZeroFilter._numSamplesProcessed
- _OBJC_IVAR_$_CSVoiceTriggerAwareZeroFilter._sampleRate
- _OBJC_IVAR_$_CSVoiceTriggerAwareZeroFilter._vtEndInSampleCount
- _OBJC_IVAR_$_CSVoiceTriggerAwareZeroFilter._zeroFilter
- _OBJC_IVAR_$_CSVoiceTriggerEventInfoProvider._accessoryVoiceTriggerEvents
- _OBJC_IVAR_$_CSVoiceTriggerEventInfoProvider._builtInVoiceTriggerEvent
- _OBJC_IVAR_$_CSVoiceTriggerEventInfoProvider._queue
- _OBJC_IVAR_$_CSVoiceTriggerEventInfoProvider._rtsTriggerInfo
- _OBJC_IVAR_$_CSVoiceTriggerEventInfoProvider._triggerNotifiedMachTime
- _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._otherAppRecordingStateMonitor
- _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._phoneCallState
- _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._phoneCallStateMonitor
- _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._voiceTriggerEnabledMonitor
- _OBJC_IVAR_$_CSVoiceTriggerStatAggregator._falseWakePhraseDictionary
- _OBJC_IVAR_$_CSVoiceTriggerStatAggregator._lastAggTimeFalseWakeUp
- _OBJC_IVAR_$_CSVoiceTriggerStatAggregator._numFalseWakeUp
- _OBJC_METACLASS_$_CSAVVoiceTriggerClientManager
- _OBJC_METACLASS_$_CSAlertBehaviorPredictor
- _OBJC_METACLASS_$_CSAudioFileReader
- _OBJC_METACLASS_$_CSAudioPreprocessor
- _OBJC_METACLASS_$_CSAudioProvider
- _OBJC_METACLASS_$_CSAudioProviderListeningMicIndicatorLock
- _OBJC_METACLASS_$_CSAudioProviderRecordModeLock
- _OBJC_METACLASS_$_CSAudioProviderRequestLock
- _OBJC_METACLASS_$_CSAudioRecordDeviceIndicator
- _OBJC_METACLASS_$_CSAudioRouteChangeMonitor
- _OBJC_METACLASS_$_CSAudioRouteChangeMonitorImpl
- _OBJC_METACLASS_$_CSAudioRouteChangeMonitorImplWatch
- _OBJC_METACLASS_$_CSAudioSampleRateConverter
- _OBJC_METACLASS_$_CSAudioServerCrashMonitor
- _OBJC_METACLASS_$_CSAudioStream
- _OBJC_METACLASS_$_CSAudioStreamActivityMonitor
- _OBJC_METACLASS_$_CSAudioStreamHolding
- _OBJC_METACLASS_$_CSAudioTandemStream
- _OBJC_METACLASS_$_CSBluetoothDeviceInfo
- _OBJC_METACLASS_$_CSBluetoothManager
- _OBJC_METACLASS_$_CSBluetoothWirelessSplitterInfo
- _OBJC_METACLASS_$_CSCXPhoneCallStateMonitor
- _OBJC_METACLASS_$_CSCarKitUtils
- _OBJC_METACLASS_$_CSDefaultAudioRouteChangeMonitorMac
- _OBJC_METACLASS_$_CSHardwareLatencyHelper
- _OBJC_METACLASS_$_CSMSNExceptionManager
- _OBJC_METACLASS_$_CSMicUsageReporter
- _OBJC_METACLASS_$_CSPhoneCallStateMonitor
- _OBJC_METACLASS_$_CSPhoneCallStateMonitorFactory
- _OBJC_METACLASS_$_CSRemoteDarwinDeviceInfo
- _OBJC_METACLASS_$_CSRemoteRecordClient
- _OBJC_METACLASS_$_CSSiriAudioRoute
- _OBJC_METACLASS_$_CSSiriAudioSession
- _OBJC_METACLASS_$_CSSiriPreferences
- _OBJC_METACLASS_$_CSTUPhoneCallStateMonitor
- _OBJC_METACLASS_$_CSUserSessionActiveMonitor
- _OBJC_METACLASS_$_CSVoiceTriggerAwareZeroFilter
- _OBJC_METACLASS_$_CSVoiceTriggerEventInfoProvider
- _OBJC_METACLASS_$_CSVoiceTriggerStatAggregator
- _TUCallCenterCallStatusChangedNotification
- _TUCallCenterVideoCallStatusChangedNotification
- __AFBackedUpPreferencesValueForKey
- __AFPreferencesValueForKeyWithContext
- __AudioDeviceIsInputDevice
- __AudioDeviceIsOutputDevice
- __AudioDeviceRegisterForChangedNotification
- __AudioDeviceUID
- __AudioObjectGetCFTypeRef
- __AudioObjectGetIntValue
- __AudioObjectGetScalarArray
- __BTAccessoryCallbacks.28214
- __BTAccessoryEventCallback.28216
- __BTLocalDeviceCallbacks.28221
- __BTLocalDeviceStatusEventCallback.28223
- __BTServiceEventCallback.28229
- __BTSessionCallbacks.28234
- __BTSessionEventCallback.28238
- __OBJC_$_CATEGORY_AVVCAudioBuffer_$_remoteVoiceActivityVADBuffer
- __OBJC_$_CATEGORY_AVVCContextSettings_$_debugDescription
- __OBJC_$_CATEGORY_AVVCStartRecordSettings_$_debugDescription
- __OBJC_$_CATEGORY_CSAudioRecordContext_$_AVVC
- __OBJC_$_CATEGORY_CSAudioStartStreamOption_$_AVVC
- __OBJC_$_CATEGORY_NSArray_$_XPCObject
- __OBJC_$_CATEGORY_NSDictionary_$_XPCObject
- __OBJC_$_CATEGORY_NSHashTable_$_Indexing
- __OBJC_$_CATEGORY_NSNumber_$_XPCObject
- __OBJC_$_CATEGORY_NSString_$_XPCObject
- __OBJC_$_CLASS_METHODS_CSAVVoiceTriggerClientManager
- __OBJC_$_CLASS_METHODS_CSAlertBehaviorPredictor
- __OBJC_$_CLASS_METHODS_CSAudioDeviceInfo
- __OBJC_$_CLASS_METHODS_CSAudioRecordDeviceInfo
- __OBJC_$_CLASS_METHODS_CSAudioRecorder
- __OBJC_$_CLASS_METHODS_CSAudioRouteChangeMonitor
- __OBJC_$_CLASS_METHODS_CSAudioSampleRateConverter
- __OBJC_$_CLASS_METHODS_CSAudioServerCrashMonitor
- __OBJC_$_CLASS_METHODS_CSAudioStartStreamOption(AVVC)
- __OBJC_$_CLASS_METHODS_CSAudioStreamActivityMonitor
- __OBJC_$_CLASS_METHODS_CSBluetoothManager
- __OBJC_$_CLASS_METHODS_CSCXPhoneCallStateMonitor
- __OBJC_$_CLASS_METHODS_CSCarKitUtils
- __OBJC_$_CLASS_METHODS_CSDefaultAudioRouteChangeMonitorMac
- __OBJC_$_CLASS_METHODS_CSHardwareLatencyHelper
- __OBJC_$_CLASS_METHODS_CSMSNExceptionManager
- __OBJC_$_CLASS_METHODS_CSPhoneCallStateMonitor
- __OBJC_$_CLASS_METHODS_CSPhoneCallStateMonitorFactory
- __OBJC_$_CLASS_METHODS_CSRemoteDarwinDeviceInfo
- __OBJC_$_CLASS_METHODS_CSSiriAudioSession
- __OBJC_$_CLASS_METHODS_CSSiriPreferences
- __OBJC_$_CLASS_METHODS_CSTUPhoneCallStateMonitor
- __OBJC_$_CLASS_METHODS_CSUserSessionActiveMonitor
- __OBJC_$_CLASS_METHODS_CSUtils(Statistics|LanguageCode|Json|AudioHardware|AudioFile|NSXPC|Trial|RecordContext)
- __OBJC_$_CLASS_METHODS_CSVoiceTriggerEventInfoProvider
- __OBJC_$_CLASS_METHODS_CSVoiceTriggerStatAggregator
- __OBJC_$_CLASS_PROP_LIST_CSAudioDeviceInfo
- __OBJC_$_CLASS_PROP_LIST_CSAudioRecordDeviceInfo
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.13487
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.13806
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.17723
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.18394
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.26683
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.28724
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.31132
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.31622
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.32070
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.9382
- __OBJC_$_INSTANCE_METHODS_AVVCAudioBuffer(remoteVoiceActivityVADBuffer)
- __OBJC_$_INSTANCE_METHODS_AVVCContextSettings(debugDescription)
- __OBJC_$_INSTANCE_METHODS_AVVCStartRecordSettings(debugDescription)
- __OBJC_$_INSTANCE_METHODS_CSAudioDeviceInfo
- __OBJC_$_INSTANCE_METHODS_CSAudioFileReader
- __OBJC_$_INSTANCE_METHODS_CSAudioPreprocessor
- __OBJC_$_INSTANCE_METHODS_CSAudioProvider
- __OBJC_$_INSTANCE_METHODS_CSAudioProviderRequestLock
- __OBJC_$_INSTANCE_METHODS_CSAudioRecordContext(AVVC|Helper|isPluginContext)
- __OBJC_$_INSTANCE_METHODS_CSAudioRecordDeviceIndicator
- __OBJC_$_INSTANCE_METHODS_CSAudioRecordDeviceInfo
- __OBJC_$_INSTANCE_METHODS_CSAudioRecorder
- __OBJC_$_INSTANCE_METHODS_CSAudioRouteChangeMonitor
- __OBJC_$_INSTANCE_METHODS_CSAudioRouteChangeMonitorImpl
- __OBJC_$_INSTANCE_METHODS_CSAudioRouteChangeMonitorImplWatch
- __OBJC_$_INSTANCE_METHODS_CSAudioSampleRateConverter
- __OBJC_$_INSTANCE_METHODS_CSAudioServerCrashMonitor
- __OBJC_$_INSTANCE_METHODS_CSAudioStartStreamOption(AVVC)
- __OBJC_$_INSTANCE_METHODS_CSAudioStream
- __OBJC_$_INSTANCE_METHODS_CSAudioStreamActivityMonitor
- __OBJC_$_INSTANCE_METHODS_CSAudioStreamHolding
- __OBJC_$_INSTANCE_METHODS_CSAudioTandemStream
- __OBJC_$_INSTANCE_METHODS_CSBluetoothDeviceInfo
- __OBJC_$_INSTANCE_METHODS_CSBluetoothManager
- __OBJC_$_INSTANCE_METHODS_CSBluetoothWirelessSplitterInfo
- __OBJC_$_INSTANCE_METHODS_CSCXPhoneCallStateMonitor
- __OBJC_$_INSTANCE_METHODS_CSCarKitUtils
- __OBJC_$_INSTANCE_METHODS_CSDefaultAudioRouteChangeMonitorMac
- __OBJC_$_INSTANCE_METHODS_CSHardwareLatencyHelper
- __OBJC_$_INSTANCE_METHODS_CSMSNExceptionManager
- __OBJC_$_INSTANCE_METHODS_CSMicUsageReporter
- __OBJC_$_INSTANCE_METHODS_CSPhoneCallStateMonitor
- __OBJC_$_INSTANCE_METHODS_CSRemoteDarwinDeviceInfo
- __OBJC_$_INSTANCE_METHODS_CSRemoteRecordClient
- __OBJC_$_INSTANCE_METHODS_CSSiriAudioRoute
- __OBJC_$_INSTANCE_METHODS_CSSiriAudioSession
- __OBJC_$_INSTANCE_METHODS_CSSiriPreferences
- __OBJC_$_INSTANCE_METHODS_CSTUPhoneCallStateMonitor
- __OBJC_$_INSTANCE_METHODS_CSUserSessionActiveMonitor
- __OBJC_$_INSTANCE_METHODS_CSVoiceTriggerAwareZeroFilter
- __OBJC_$_INSTANCE_METHODS_CSVoiceTriggerEventInfoProvider
- __OBJC_$_INSTANCE_METHODS_CSVoiceTriggerStatAggregator
- __OBJC_$_INSTANCE_METHODS_NSArray(XPCObject)
- __OBJC_$_INSTANCE_METHODS_NSData(Nvi|XPCObject)
- __OBJC_$_INSTANCE_METHODS_NSDictionary(XPCObject)
- __OBJC_$_INSTANCE_METHODS_NSHashTable(Indexing)
- __OBJC_$_INSTANCE_METHODS_NSNumber(XPCObject)
- __OBJC_$_INSTANCE_METHODS_NSString(XPCObject|Nvi)
- __OBJC_$_INSTANCE_VARIABLES_CSAudioDeviceInfo
- __OBJC_$_INSTANCE_VARIABLES_CSAudioFileReader
- __OBJC_$_INSTANCE_VARIABLES_CSAudioPreprocessor
- __OBJC_$_INSTANCE_VARIABLES_CSAudioProvider
- __OBJC_$_INSTANCE_VARIABLES_CSAudioProviderRequestLock
- __OBJC_$_INSTANCE_VARIABLES_CSAudioRecordDeviceIndicator
- __OBJC_$_INSTANCE_VARIABLES_CSAudioRecordDeviceInfo
- __OBJC_$_INSTANCE_VARIABLES_CSAudioRecorder
- __OBJC_$_INSTANCE_VARIABLES_CSAudioRouteChangeMonitorImpl
- __OBJC_$_INSTANCE_VARIABLES_CSAudioRouteChangeMonitorImplWatch
- __OBJC_$_INSTANCE_VARIABLES_CSAudioSampleRateConverter
- __OBJC_$_INSTANCE_VARIABLES_CSAudioServerCrashMonitor
- __OBJC_$_INSTANCE_VARIABLES_CSAudioStream
- __OBJC_$_INSTANCE_VARIABLES_CSAudioStreamActivityMonitor
- __OBJC_$_INSTANCE_VARIABLES_CSAudioStreamHolding
- __OBJC_$_INSTANCE_VARIABLES_CSAudioTandemStream
- __OBJC_$_INSTANCE_VARIABLES_CSBluetoothDeviceInfo
- __OBJC_$_INSTANCE_VARIABLES_CSBluetoothManager
- __OBJC_$_INSTANCE_VARIABLES_CSBluetoothWirelessSplitterInfo
- __OBJC_$_INSTANCE_VARIABLES_CSCXPhoneCallStateMonitor
- __OBJC_$_INSTANCE_VARIABLES_CSCarKitUtils
- __OBJC_$_INSTANCE_VARIABLES_CSMSNExceptionManager
- __OBJC_$_INSTANCE_VARIABLES_CSMicUsageReporter
- __OBJC_$_INSTANCE_VARIABLES_CSRemoteDarwinDeviceInfo
- __OBJC_$_INSTANCE_VARIABLES_CSRemoteRecordClient
- __OBJC_$_INSTANCE_VARIABLES_CSSiriAudioRoute
- __OBJC_$_INSTANCE_VARIABLES_CSSiriAudioSession
- __OBJC_$_INSTANCE_VARIABLES_CSSiriPreferences
- __OBJC_$_INSTANCE_VARIABLES_CSTUPhoneCallStateMonitor
- __OBJC_$_INSTANCE_VARIABLES_CSVoiceTriggerAwareZeroFilter
- __OBJC_$_INSTANCE_VARIABLES_CSVoiceTriggerEventInfoProvider
- __OBJC_$_INSTANCE_VARIABLES_CSVoiceTriggerStatAggregator
- __OBJC_$_PROP_LIST_CSAudioDeviceInfo
- __OBJC_$_PROP_LIST_CSAudioFileReader
- __OBJC_$_PROP_LIST_CSAudioPreprocessor
- __OBJC_$_PROP_LIST_CSAudioProvider
- __OBJC_$_PROP_LIST_CSAudioProviderRequestLock
- __OBJC_$_PROP_LIST_CSAudioRecordDeviceIndicator
- __OBJC_$_PROP_LIST_CSAudioRecordDeviceInfo
- __OBJC_$_PROP_LIST_CSAudioRecorder
- __OBJC_$_PROP_LIST_CSAudioServerCrashMonitor
- __OBJC_$_PROP_LIST_CSAudioStream
- __OBJC_$_PROP_LIST_CSAudioStreamActivityMonitor
- __OBJC_$_PROP_LIST_CSAudioStreamHolding
- __OBJC_$_PROP_LIST_CSAudioTandemStream
- __OBJC_$_PROP_LIST_CSBluetoothDeviceInfo
- __OBJC_$_PROP_LIST_CSBluetoothManager
- __OBJC_$_PROP_LIST_CSBluetoothWirelessSplitterInfo
- __OBJC_$_PROP_LIST_CSCXPhoneCallStateMonitor
- __OBJC_$_PROP_LIST_CSCarKitUtils
- __OBJC_$_PROP_LIST_CSEndpointAnalyzer.19858
- __OBJC_$_PROP_LIST_CSEndpointAnalyzer.26505
- __OBJC_$_PROP_LIST_CSEndpointAnalyzer.27777
- __OBJC_$_PROP_LIST_CSEndpointAnalyzerImpl.19859
- __OBJC_$_PROP_LIST_CSEndpointAnalyzerImpl.26506
- __OBJC_$_PROP_LIST_CSMSNExceptionManager
- __OBJC_$_PROP_LIST_CSMicUsageReporter
- __OBJC_$_PROP_LIST_CSRemoteDarwinDeviceInfo
- __OBJC_$_PROP_LIST_CSRemoteRecordClient
- __OBJC_$_PROP_LIST_CSSiriAudioPlaybackSession.15338
- __OBJC_$_PROP_LIST_CSSiriAudioRoute
- __OBJC_$_PROP_LIST_CSTUPhoneCallStateMonitor
- __OBJC_$_PROP_LIST_CSVoiceTriggerAwareZeroFilter
- __OBJC_$_PROP_LIST_CSVoiceTriggerEventInfoProvider
- __OBJC_$_PROP_LIST_CSVoiceTriggerStatAggregator
- __OBJC_$_PROP_LIST_NSObject.10025
- __OBJC_$_PROP_LIST_NSObject.10607
- __OBJC_$_PROP_LIST_NSObject.10916
- __OBJC_$_PROP_LIST_NSObject.11105
- __OBJC_$_PROP_LIST_NSObject.11245
- __OBJC_$_PROP_LIST_NSObject.11517
- __OBJC_$_PROP_LIST_NSObject.11887
- __OBJC_$_PROP_LIST_NSObject.12086
- __OBJC_$_PROP_LIST_NSObject.12642
- __OBJC_$_PROP_LIST_NSObject.12789
- __OBJC_$_PROP_LIST_NSObject.13196
- __OBJC_$_PROP_LIST_NSObject.14026
- __OBJC_$_PROP_LIST_NSObject.14202
- __OBJC_$_PROP_LIST_NSObject.1457
- __OBJC_$_PROP_LIST_NSObject.15048
- __OBJC_$_PROP_LIST_NSObject.15339
- __OBJC_$_PROP_LIST_NSObject.1547
- __OBJC_$_PROP_LIST_NSObject.15533
- __OBJC_$_PROP_LIST_NSObject.156
- __OBJC_$_PROP_LIST_NSObject.15880
- __OBJC_$_PROP_LIST_NSObject.16026
- __OBJC_$_PROP_LIST_NSObject.16272
- __OBJC_$_PROP_LIST_NSObject.16396
- __OBJC_$_PROP_LIST_NSObject.1696
- __OBJC_$_PROP_LIST_NSObject.17268
- __OBJC_$_PROP_LIST_NSObject.17425
- __OBJC_$_PROP_LIST_NSObject.1797
- __OBJC_$_PROP_LIST_NSObject.18063
- __OBJC_$_PROP_LIST_NSObject.18214
- __OBJC_$_PROP_LIST_NSObject.1860
- __OBJC_$_PROP_LIST_NSObject.18930
- __OBJC_$_PROP_LIST_NSObject.19101
- __OBJC_$_PROP_LIST_NSObject.19860
- __OBJC_$_PROP_LIST_NSObject.1999
- __OBJC_$_PROP_LIST_NSObject.20312
- __OBJC_$_PROP_LIST_NSObject.209
- __OBJC_$_PROP_LIST_NSObject.21174
- __OBJC_$_PROP_LIST_NSObject.21354
- __OBJC_$_PROP_LIST_NSObject.22219
- __OBJC_$_PROP_LIST_NSObject.22496
- __OBJC_$_PROP_LIST_NSObject.22571
- __OBJC_$_PROP_LIST_NSObject.22905
- __OBJC_$_PROP_LIST_NSObject.23496
- __OBJC_$_PROP_LIST_NSObject.24071
- __OBJC_$_PROP_LIST_NSObject.24301
- __OBJC_$_PROP_LIST_NSObject.24599
- __OBJC_$_PROP_LIST_NSObject.25300
- __OBJC_$_PROP_LIST_NSObject.2566
- __OBJC_$_PROP_LIST_NSObject.26507
- __OBJC_$_PROP_LIST_NSObject.2676
- __OBJC_$_PROP_LIST_NSObject.27221
- __OBJC_$_PROP_LIST_NSObject.27348
- __OBJC_$_PROP_LIST_NSObject.27411
- __OBJC_$_PROP_LIST_NSObject.27514
- __OBJC_$_PROP_LIST_NSObject.27778
- __OBJC_$_PROP_LIST_NSObject.28015
- __OBJC_$_PROP_LIST_NSObject.28284
- __OBJC_$_PROP_LIST_NSObject.28477
- __OBJC_$_PROP_LIST_NSObject.2882
- __OBJC_$_PROP_LIST_NSObject.28994
- __OBJC_$_PROP_LIST_NSObject.29311
- __OBJC_$_PROP_LIST_NSObject.29462
- __OBJC_$_PROP_LIST_NSObject.29730
- __OBJC_$_PROP_LIST_NSObject.29866
- __OBJC_$_PROP_LIST_NSObject.30721
- __OBJC_$_PROP_LIST_NSObject.30916
- __OBJC_$_PROP_LIST_NSObject.31378
- __OBJC_$_PROP_LIST_NSObject.31973
- __OBJC_$_PROP_LIST_NSObject.32170
- __OBJC_$_PROP_LIST_NSObject.32984
- __OBJC_$_PROP_LIST_NSObject.33815
- __OBJC_$_PROP_LIST_NSObject.34218
- __OBJC_$_PROP_LIST_NSObject.34311
- __OBJC_$_PROP_LIST_NSObject.34462
- __OBJC_$_PROP_LIST_NSObject.3447
- __OBJC_$_PROP_LIST_NSObject.3621
- __OBJC_$_PROP_LIST_NSObject.3764
- __OBJC_$_PROP_LIST_NSObject.4056
- __OBJC_$_PROP_LIST_NSObject.4302
- __OBJC_$_PROP_LIST_NSObject.431
- __OBJC_$_PROP_LIST_NSObject.4911
- __OBJC_$_PROP_LIST_NSObject.5115
- __OBJC_$_PROP_LIST_NSObject.523
- __OBJC_$_PROP_LIST_NSObject.5507
- __OBJC_$_PROP_LIST_NSObject.6100
- __OBJC_$_PROP_LIST_NSObject.6375
- __OBJC_$_PROP_LIST_NSObject.6501
- __OBJC_$_PROP_LIST_NSObject.6722
- __OBJC_$_PROP_LIST_NSObject.6834
- __OBJC_$_PROP_LIST_NSObject.6933
- __OBJC_$_PROP_LIST_NSObject.707
- __OBJC_$_PROP_LIST_NSObject.7664
- __OBJC_$_PROP_LIST_NSObject.7898
- __OBJC_$_PROP_LIST_NSObject.8076
- __OBJC_$_PROP_LIST_NSObject.8136
- __OBJC_$_PROP_LIST_NSObject.8469
- __OBJC_$_PROP_LIST_NSObject.8684
- __OBJC_$_PROP_LIST_NSObject.878
- __OBJC_$_PROP_LIST_NSObject.8806
- __OBJC_$_PROP_LIST_NSObject.9215
- __OBJC_$_PROP_LIST_NSObject.9672
- __OBJC_$_PROP_LIST_NSObject.9763
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.13488
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.13807
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.17724
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.18395
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.26684
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.28725
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.31133
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.31623
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.32071
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.9383
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.21175
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.4303
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.5508
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.7665
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAssetManagerDelegate.26508
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioAlertProviding.25301
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioConverterDelegate.12790
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioDecoderDelegate.33816
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioFileReaderDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.12791
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.13197
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.2000
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.24302
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.4912
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioMeterProviding.25302
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioMetricProviding.25303
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioPreprocessorDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioRecorderDelegate.25304
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioRecorderDelegate.29312
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioRouteChangeMonitorDelegate.22220
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioSessionEventProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioSessionInfoProviding.27349
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioSessionProviding.25305
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProviding.25306
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProviding.29731
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.10608
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.11888
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.16273
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.17269
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.18064
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.20313
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.21176
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.23497
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.32985
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.5116
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.5509
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.7899
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.9216
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBeepCancellerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBenchmarkXPCProtocol.24303
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBluetoothWirelessSplitterMonitorDelegate.22221
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBluetoothWirelessSplitterMonitorDelegate.28995
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSDigitalZeroReporting
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.19861
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.26509
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.27779
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerDelegate.30722
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImpl.19862
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImpl.26510
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImplDelegate.27780
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFallbackAudioSessionReleaseProviding.29313
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.10026
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.14027
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.9217
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSMediaPlayingMonitorDelegate.18065
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.21177
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.28996
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.32986
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSRemoteRecordClientDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSecondPassProgressProviding.21178
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.12087
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.21179
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.6502
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriAudioPlaybackSession.15340
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.10609
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.11518
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.11889
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.14203
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.18066
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.21180
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.28478
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.32987
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.4304
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.5510
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.8470
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSpeakerRecognitionAssetDownloadMonitorDelegate.19102
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSystemShellStartProviding.15534
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSystemShellStartProviding.24600
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSTrialAssetDownloadMonitorDelegate.4057
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSTriggerInfoProviding.25307
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSUAFDownloadMonitorDelegate.31974
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.31975
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.7666
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.9218
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAwareZeroFilterDelegate.2883
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.11246
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.12088
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.15049
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.22222
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.28016
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.11519
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.19103
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.21181
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSXPCClientDelegate.7900
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSXPCClientDelegate.9219
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CXCallObserverDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreSpeechXPCProtocol.23974
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_EARCaesuraSilencePosteriorGeneratorDelegate.31379
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.13489
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.13808
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.17725
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.18396
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.26685
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.28726
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.31134
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.31624
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.32072
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.34521
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.9384
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.17726
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.18397
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.26686
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.28727
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.31135
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.31625
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.32073
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10027
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10610
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10917
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11106
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11247
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11520
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11890
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12089
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12643
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12792
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.13198
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14028
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14204
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1458
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15050
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15341
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1548
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15535
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.157
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15881
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16027
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16274
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16397
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1697
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17270
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17426
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1798
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.18067
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.18215
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1861
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.18931
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.19104
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.19863
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2001
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.20314
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.210
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21182
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21355
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22223
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22497
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22572
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22906
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.23498
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24072
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24304
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24601
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25308
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2567
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26511
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2677
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27222
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27350
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27412
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27515
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27781
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28017
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28285
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28479
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2884
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28997
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29314
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29463
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29732
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29867
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30723
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30917
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.31380
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.31976
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.32171
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.32988
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.33817
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.34219
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.34312
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.34463
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3448
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3622
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3765
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4058
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4305
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.432
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4913
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5117
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.524
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5511
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6101
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6376
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6503
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6723
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6835
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6934
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.708
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7667
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7901
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8077
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8137
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8471
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8685
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.879
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8807
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9220
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9673
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9764
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AVVoiceControllerRecordDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioRecorderDelegate.25309
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioRecorderDelegate.29315
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.17271
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.17427
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.18068
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.18932
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.21183
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.25310
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.29733
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.32989
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.6836
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.6935
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.7668
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionControllerDelegate.30724
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionControllerDelegate.30918
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.10611
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.11891
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.16275
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.17272
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.18069
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.20315
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.21184
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.23499
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.32990
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.5118
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.5512
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.7902
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.9221
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.19864
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.26512
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.27782
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerDelegate.30725
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImpl.19865
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImpl.26513
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImplDelegate.27783
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSKeywordAnalyzerNDEAPIScoreDelegate.16028
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSOpportuneSpeakEventMonitorDelegate.10612
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSPGEndpointAnalyzerDelegate.5513
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.10613
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.11521
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.11892
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.14205
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.18070
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.21185
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.28480
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.32991
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.4306
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.5514
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.8472
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSUserSessionActiveMonitorDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.11248
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.12090
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.15051
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.22224
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.28018
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVolumeMonitorDelegate.11249
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EARCaesuraSilencePosteriorGeneratorDelegate.31381
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10028
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10614
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10918
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11107
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11250
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11522
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11893
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12091
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12644
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12793
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.13199
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14029
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14206
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1459
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15052
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15342
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1549
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15536
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.158
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15882
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.16029
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.16276
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.16398
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1698
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17273
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17428
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1799
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.18071
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.18216
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1862
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.18933
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.19105
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.19866
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2002
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.20316
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.211
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21186
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21356
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22225
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22498
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22573
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22907
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.23500
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24073
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24305
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24602
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25311
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2568
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26514
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2678
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27223
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27351
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27413
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27516
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27784
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28019
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28286
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28481
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2885
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28998
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29316
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29464
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29734
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29868
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30726
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30919
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.31382
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.31977
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.32172
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.32992
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.33818
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.34220
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.34313
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.34464
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3449
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3623
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3766
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4059
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4307
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.433
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4914
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5119
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.525
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5515
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6102
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6377
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6504
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6724
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6837
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6936
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.709
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7669
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7903
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8078
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8138
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8473
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8686
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.880
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8808
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9222
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9674
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9765
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SNResultsObserving.8687
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRSpeakerRecognitionControllerDelegate.9223
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SFEntitledTrialAssetDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNResultsObserving.8688
- __OBJC_$_PROTOCOL_METHOD_TYPES_AVVoiceControllerRecordDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.21187
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.4308
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.5516
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.7670
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAssetManagerDelegate.26515
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioAlertProviding.25312
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioConverterDelegate.12794
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioDecoderDelegate.33819
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioFileReaderDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.12795
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.13200
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.2003
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.24306
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.4915
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioMeterProviding.25313
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioMetricProviding.25314
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioPreprocessorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioRecorderDelegate.25315
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioRecorderDelegate.29317
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioRouteChangeMonitorDelegate.22226
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.17274
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.17429
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.18072
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.18934
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.21188
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.25316
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.29735
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.32993
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.6838
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.6937
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.7671
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionControllerDelegate.30727
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionControllerDelegate.30920
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionEventProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionInfoProviding.27352
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionProviding.25317
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProviding.25318
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProviding.29736
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.10615
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.11894
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.16277
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.17275
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.18073
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.20317
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.21189
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.23501
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.32994
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.5120
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.5517
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.7904
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.9224
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSBeepCancellerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSBenchmarkXPCProtocol.24307
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSBluetoothWirelessSplitterMonitorDelegate.22227
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSBluetoothWirelessSplitterMonitorDelegate.28999
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSDigitalZeroReporting
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.19867
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.26516
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.27785
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerDelegate.30728
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImpl.19868
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImpl.26517
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImplDelegate.27786
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSFallbackAudioSessionReleaseProviding.29318
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSKeywordAnalyzerNDEAPIScoreDelegate.16030
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.10029
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.14030
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.9225
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSMediaPlayingMonitorDelegate.18074
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSOpportuneSpeakEventMonitorDelegate.10616
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.21190
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.29000
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.32995
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSRemoteRecordClientDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSPGEndpointAnalyzerDelegate.5518
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSecondPassProgressProviding.21191
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.12092
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.21192
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.6505
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriAudioPlaybackSession.15343
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.10617
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.11523
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.11895
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.14207
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.18075
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.21193
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.28482
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.32996
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.4309
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.5519
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.8474
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSpeakerRecognitionAssetDownloadMonitorDelegate.19106
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemShellStartProviding.15537
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemShellStartProviding.24603
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSTrialAssetDownloadMonitorDelegate.4060
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSTriggerInfoProviding.25319
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSUAFDownloadMonitorDelegate.31978
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSUserSessionActiveMonitorDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.31979
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.7672
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.9226
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAwareZeroFilterDelegate.2886
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.11251
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.12093
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.15053
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.22228
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.28020
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.11524
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.19107
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.21194
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVolumeMonitorDelegate.11252
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSXPCClientDelegate.7905
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSXPCClientDelegate.9227
- __OBJC_$_PROTOCOL_METHOD_TYPES_CXCallObserverDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CoreSpeechXPCProtocol.23975
- __OBJC_$_PROTOCOL_METHOD_TYPES_EARCaesuraSilencePosteriorGeneratorDelegate.31383
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.13490
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.13809
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.17727
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.18398
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.26687
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.28728
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.31136
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.31626
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.32074
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.34522
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.9385
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.17728
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.18399
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.26688
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.28729
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.31137
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.31627
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.32075
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10030
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10618
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10919
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11108
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11253
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11525
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11896
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.12094
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.12645
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.12796
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.13201
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14031
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14208
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1460
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15054
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15344
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1550
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15538
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15883
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.159
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.16031
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.16278
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.16399
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1699
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17276
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17430
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1800
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18076
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18217
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1863
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18935
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.19108
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.19869
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2004
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.20318
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21195
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.212
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21357
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22229
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22499
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22574
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22908
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.23502
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24074
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24308
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24604
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25320
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2569
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26518
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2679
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27224
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27353
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27414
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27517
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27787
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.28021
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.28483
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2887
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29001
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29319
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29465
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29737
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29869
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30729
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30921
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.31384
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.31980
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.32173
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.32997
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.33820
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.34221
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.34314
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.34465
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3450
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3624
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3767
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4061
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4310
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.434
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4916
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5121
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.526
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5520
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6103
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6378
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6506
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6725
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6839
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6938
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.710
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7673
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7906
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8079
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8139
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8475
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8689
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8809
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.881
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9228
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9675
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9766
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.13491
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.13810
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.17729
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.18400
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.26689
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.28730
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.31138
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.31628
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.32076
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.9386
- __OBJC_$_PROTOCOL_METHOD_TYPES_SFEntitledTrialAssetDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNResultsObserving.8690
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRSpeakerRecognitionControllerDelegate.9229
- __OBJC_$_PROTOCOL_REFS_AVVoiceControllerRecordDelegate
- __OBJC_$_PROTOCOL_REFS_CESRTrialAssetDelegate
- __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.21196
- __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.4311
- __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.5521
- __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.7674
- __OBJC_$_PROTOCOL_REFS_CSAssetManagerDelegate.26519
- __OBJC_$_PROTOCOL_REFS_CSAudioAlertProviding.25321
- __OBJC_$_PROTOCOL_REFS_CSAudioConverterDelegate.12797
- __OBJC_$_PROTOCOL_REFS_CSAudioDecoderDelegate.33821
- __OBJC_$_PROTOCOL_REFS_CSAudioFileReaderDelegate
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.12798
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.13202
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.2005
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.24309
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.4917
- __OBJC_$_PROTOCOL_REFS_CSAudioMeterProviding.25322
- __OBJC_$_PROTOCOL_REFS_CSAudioMetricProviding.25323
- __OBJC_$_PROTOCOL_REFS_CSAudioPreprocessorDelegate
- __OBJC_$_PROTOCOL_REFS_CSAudioRecorderDelegate.25324
- __OBJC_$_PROTOCOL_REFS_CSAudioRecorderDelegate.29320
- __OBJC_$_PROTOCOL_REFS_CSAudioRouteChangeMonitorDelegate.22230
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.17277
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.17431
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.18077
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.18936
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.21197
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.25325
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.29738
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.32998
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.6840
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.6939
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.7675
- __OBJC_$_PROTOCOL_REFS_CSAudioSessionControllerDelegate.30730
- __OBJC_$_PROTOCOL_REFS_CSAudioSessionControllerDelegate.30922
- __OBJC_$_PROTOCOL_REFS_CSAudioSessionEventProviding
- __OBJC_$_PROTOCOL_REFS_CSAudioSessionInfoProviding.27354
- __OBJC_$_PROTOCOL_REFS_CSAudioSessionProviding.25326
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProviding.25327
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProviding.29739
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.10619
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.11897
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.16279
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.17278
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.18078
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.20319
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.21198
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.23503
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.32999
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.5122
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.5522
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.7907
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.9230
- __OBJC_$_PROTOCOL_REFS_CSBeepCancellerDelegate
- __OBJC_$_PROTOCOL_REFS_CSBluetoothWirelessSplitterMonitorDelegate.22231
- __OBJC_$_PROTOCOL_REFS_CSBluetoothWirelessSplitterMonitorDelegate.29002
- __OBJC_$_PROTOCOL_REFS_CSDigitalZeroReporting
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.19870
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.26520
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.27788
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerDelegate.30731
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImpl.19871
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImpl.26521
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImplDelegate.27789
- __OBJC_$_PROTOCOL_REFS_CSFallbackAudioSessionReleaseProviding.29321
- __OBJC_$_PROTOCOL_REFS_CSKeywordAnalyzerNDEAPIScoreDelegate.16032
- __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.10031
- __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.14032
- __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.9231
- __OBJC_$_PROTOCOL_REFS_CSMediaPlayingMonitorDelegate.18079
- __OBJC_$_PROTOCOL_REFS_CSOpportuneSpeakEventMonitorDelegate.10620
- __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.21199
- __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.29003
- __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.33000
- __OBJC_$_PROTOCOL_REFS_CSRemoteRecordClientDelegate
- __OBJC_$_PROTOCOL_REFS_CSSPGEndpointAnalyzerDelegate.5523
- __OBJC_$_PROTOCOL_REFS_CSSecondPassProgressProviding.21200
- __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.12095
- __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.21201
- __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.6507
- __OBJC_$_PROTOCOL_REFS_CSSiriAudioPlaybackSession.15345
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.10621
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.11526
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.11898
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.14209
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.18080
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.21202
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.28484
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.33001
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.4312
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.5524
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.8476
- __OBJC_$_PROTOCOL_REFS_CSSpeakerRecognitionAssetDownloadMonitorDelegate.19109
- __OBJC_$_PROTOCOL_REFS_CSSpeechManagerDelegate.34466
- __OBJC_$_PROTOCOL_REFS_CSSystemShellStartProviding.15539
- __OBJC_$_PROTOCOL_REFS_CSSystemShellStartProviding.24605
- __OBJC_$_PROTOCOL_REFS_CSTrialAssetDownloadMonitorDelegate.4062
- __OBJC_$_PROTOCOL_REFS_CSTriggerInfoProviding.25328
- __OBJC_$_PROTOCOL_REFS_CSUAFDownloadMonitorDelegate.31981
- __OBJC_$_PROTOCOL_REFS_CSUserSessionActiveMonitorDelegate
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.31982
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.7676
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.9232
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAwareZeroFilterDelegate.2888
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.11254
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.12096
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.15055
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.22232
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.28022
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.11527
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.19110
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.21203
- __OBJC_$_PROTOCOL_REFS_CSVolumeMonitorDelegate.11255
- __OBJC_$_PROTOCOL_REFS_CSXPCClientDelegate.7908
- __OBJC_$_PROTOCOL_REFS_CSXPCClientDelegate.9233
- __OBJC_$_PROTOCOL_REFS_CXCallObserverDelegate
- __OBJC_$_PROTOCOL_REFS_EARCaesuraSilencePosteriorGeneratorDelegate.31385
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.13492
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.13811
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.17730
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.18401
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.26690
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.28731
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.31139
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.31629
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.32077
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.9387
- __OBJC_$_PROTOCOL_REFS_SFEntitledTrialAssetDelegate
- __OBJC_$_PROTOCOL_REFS_SNResultsObserving.8691
- __OBJC_$_PROTOCOL_REFS_SSRSpeakerRecognitionControllerDelegate.9234
- __OBJC_CLASS_PROTOCOLS_$_CSAudioDeviceInfo
- __OBJC_CLASS_PROTOCOLS_$_CSAudioPreprocessor
- __OBJC_CLASS_PROTOCOLS_$_CSAudioProvider
- __OBJC_CLASS_PROTOCOLS_$_CSAudioRecordDeviceInfo
- __OBJC_CLASS_PROTOCOLS_$_CSAudioRecorder
- __OBJC_CLASS_PROTOCOLS_$_CSAudioStream
- __OBJC_CLASS_PROTOCOLS_$_CSAudioTandemStream
- __OBJC_CLASS_PROTOCOLS_$_CSCXPhoneCallStateMonitor
- __OBJC_CLASS_PROTOCOLS_$_CSVoiceTriggerStatAggregator
- __OBJC_CLASS_RO_$_CSAVVoiceTriggerClientManager
- __OBJC_CLASS_RO_$_CSAlertBehaviorPredictor
- __OBJC_CLASS_RO_$_CSAudioFileReader
- __OBJC_CLASS_RO_$_CSAudioPreprocessor
- __OBJC_CLASS_RO_$_CSAudioProvider
- __OBJC_CLASS_RO_$_CSAudioProviderListeningMicIndicatorLock
- __OBJC_CLASS_RO_$_CSAudioProviderRecordModeLock
- __OBJC_CLASS_RO_$_CSAudioProviderRequestLock
- __OBJC_CLASS_RO_$_CSAudioRecordDeviceIndicator
- __OBJC_CLASS_RO_$_CSAudioRecorder
- __OBJC_CLASS_RO_$_CSAudioRouteChangeMonitor
- __OBJC_CLASS_RO_$_CSAudioRouteChangeMonitorImpl
- __OBJC_CLASS_RO_$_CSAudioRouteChangeMonitorImplWatch
- __OBJC_CLASS_RO_$_CSAudioSampleRateConverter
- __OBJC_CLASS_RO_$_CSAudioServerCrashMonitor
- __OBJC_CLASS_RO_$_CSAudioStream
- __OBJC_CLASS_RO_$_CSAudioStreamActivityMonitor
- __OBJC_CLASS_RO_$_CSAudioStreamHolding
- __OBJC_CLASS_RO_$_CSAudioTandemStream
- __OBJC_CLASS_RO_$_CSBluetoothDeviceInfo
- __OBJC_CLASS_RO_$_CSBluetoothManager
- __OBJC_CLASS_RO_$_CSBluetoothWirelessSplitterInfo
- __OBJC_CLASS_RO_$_CSCXPhoneCallStateMonitor
- __OBJC_CLASS_RO_$_CSCarKitUtils
- __OBJC_CLASS_RO_$_CSDefaultAudioRouteChangeMonitorMac
- __OBJC_CLASS_RO_$_CSHardwareLatencyHelper
- __OBJC_CLASS_RO_$_CSMSNExceptionManager
- __OBJC_CLASS_RO_$_CSMicUsageReporter
- __OBJC_CLASS_RO_$_CSPhoneCallStateMonitor
- __OBJC_CLASS_RO_$_CSPhoneCallStateMonitorFactory
- __OBJC_CLASS_RO_$_CSRemoteDarwinDeviceInfo
- __OBJC_CLASS_RO_$_CSRemoteRecordClient
- __OBJC_CLASS_RO_$_CSSiriAudioRoute
- __OBJC_CLASS_RO_$_CSSiriAudioSession
- __OBJC_CLASS_RO_$_CSSiriPreferences
- __OBJC_CLASS_RO_$_CSTUPhoneCallStateMonitor
- __OBJC_CLASS_RO_$_CSUserSessionActiveMonitor
- __OBJC_CLASS_RO_$_CSVoiceTriggerAwareZeroFilter
- __OBJC_CLASS_RO_$_CSVoiceTriggerEventInfoProvider
- __OBJC_CLASS_RO_$_CSVoiceTriggerStatAggregator
- __OBJC_LABEL_PROTOCOL_$_AVVoiceControllerRecordDelegate
- __OBJC_LABEL_PROTOCOL_$_CESRTrialAssetDelegate
- __OBJC_LABEL_PROTOCOL_$_CSAudioFileReaderDelegate
- __OBJC_LABEL_PROTOCOL_$_CSAudioPreprocessorDelegate
- __OBJC_LABEL_PROTOCOL_$_CSAudioSessionEventProviding
- __OBJC_LABEL_PROTOCOL_$_CSBeepCancellerDelegate
- __OBJC_LABEL_PROTOCOL_$_CSDigitalZeroReporting
- __OBJC_LABEL_PROTOCOL_$_CSRemoteRecordClientDelegate
- __OBJC_LABEL_PROTOCOL_$_CSUserSessionActiveMonitorDelegate
- __OBJC_LABEL_PROTOCOL_$_CXCallObserverDelegate
- __OBJC_LABEL_PROTOCOL_$_SFEntitledTrialAssetDelegate
- __OBJC_METACLASS_RO_$_CSAVVoiceTriggerClientManager
- __OBJC_METACLASS_RO_$_CSAlertBehaviorPredictor
- __OBJC_METACLASS_RO_$_CSAudioFileReader
- __OBJC_METACLASS_RO_$_CSAudioPreprocessor
- __OBJC_METACLASS_RO_$_CSAudioProvider
- __OBJC_METACLASS_RO_$_CSAudioProviderListeningMicIndicatorLock
- __OBJC_METACLASS_RO_$_CSAudioProviderRecordModeLock
- __OBJC_METACLASS_RO_$_CSAudioProviderRequestLock
- __OBJC_METACLASS_RO_$_CSAudioRecordDeviceIndicator
- __OBJC_METACLASS_RO_$_CSAudioRecorder
- __OBJC_METACLASS_RO_$_CSAudioRouteChangeMonitor
- __OBJC_METACLASS_RO_$_CSAudioRouteChangeMonitorImpl
- __OBJC_METACLASS_RO_$_CSAudioRouteChangeMonitorImplWatch
- __OBJC_METACLASS_RO_$_CSAudioSampleRateConverter
- __OBJC_METACLASS_RO_$_CSAudioServerCrashMonitor
- __OBJC_METACLASS_RO_$_CSAudioStream
- __OBJC_METACLASS_RO_$_CSAudioStreamActivityMonitor
- __OBJC_METACLASS_RO_$_CSAudioStreamHolding
- __OBJC_METACLASS_RO_$_CSAudioTandemStream
- __OBJC_METACLASS_RO_$_CSBluetoothDeviceInfo
- __OBJC_METACLASS_RO_$_CSBluetoothManager
- __OBJC_METACLASS_RO_$_CSBluetoothWirelessSplitterInfo
- __OBJC_METACLASS_RO_$_CSCXPhoneCallStateMonitor
- __OBJC_METACLASS_RO_$_CSCarKitUtils
- __OBJC_METACLASS_RO_$_CSDefaultAudioRouteChangeMonitorMac
- __OBJC_METACLASS_RO_$_CSHardwareLatencyHelper
- __OBJC_METACLASS_RO_$_CSMSNExceptionManager
- __OBJC_METACLASS_RO_$_CSMicUsageReporter
- __OBJC_METACLASS_RO_$_CSPhoneCallStateMonitor
- __OBJC_METACLASS_RO_$_CSPhoneCallStateMonitorFactory
- __OBJC_METACLASS_RO_$_CSRemoteDarwinDeviceInfo
- __OBJC_METACLASS_RO_$_CSRemoteRecordClient
- __OBJC_METACLASS_RO_$_CSSiriAudioRoute
- __OBJC_METACLASS_RO_$_CSSiriAudioSession
- __OBJC_METACLASS_RO_$_CSSiriPreferences
- __OBJC_METACLASS_RO_$_CSTUPhoneCallStateMonitor
- __OBJC_METACLASS_RO_$_CSUserSessionActiveMonitor
- __OBJC_METACLASS_RO_$_CSVoiceTriggerAwareZeroFilter
- __OBJC_METACLASS_RO_$_CSVoiceTriggerEventInfoProvider
- __OBJC_METACLASS_RO_$_CSVoiceTriggerStatAggregator
- __OBJC_PROTOCOL_$_AVVoiceControllerRecordDelegate
- __OBJC_PROTOCOL_$_CESRTrialAssetDelegate
- __OBJC_PROTOCOL_$_CSAudioFileReaderDelegate
- __OBJC_PROTOCOL_$_CSAudioPreprocessorDelegate
- __OBJC_PROTOCOL_$_CSAudioSessionEventProviding
- __OBJC_PROTOCOL_$_CSBeepCancellerDelegate
- __OBJC_PROTOCOL_$_CSDigitalZeroReporting
- __OBJC_PROTOCOL_$_CSRemoteRecordClientDelegate
- __OBJC_PROTOCOL_$_CSUserSessionActiveMonitorDelegate
- __OBJC_PROTOCOL_$_CXCallObserverDelegate
- __OBJC_PROTOCOL_$_SFEntitledTrialAssetDelegate
- __ZL21milBnnsIrCacheMapLock
- __ZL22modelMilBnnsIrCacheMap
- __ZNKSt3__114default_deleteIN10corespeech25CSAudioCircularBufferImplIhEEEclB7v160006EPS3_
- __ZNKSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIPKhNS_9allocatorIS2_EEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB7v160006Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt12out_of_rangeC1B7v160006EPKc
- __ZNSt3__110unique_ptrI15SmartSiriVolumeNS_14default_deleteIS1_EEE5resetB7v160006EPS1_
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorINS_4pairIfjEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__120__throw_out_of_rangeB7v160006EPKc
- __ZNSt3__121__unwrap_and_dispatchB7v160006INS_10__overloadINS_11__copy_loopINS_17_ClassicAlgPolicyEEENS_14__copy_trivialEEEPNS_6vectorINS7_IfNS_9allocatorIfEEEENS8_ISA_EEEESD_SD_Li0EEENS_4pairIT0_T2_EESF_T1_SG_
- __ZNSt3__121__unwrap_and_dispatchB7v160006INS_10__overloadINS_11__copy_loopINS_17_ClassicAlgPolicyEEENS_14__copy_trivialEEEPNS_6vectorIfNS_9allocatorIfEEEESB_SB_Li0EEENS_4pairIT0_T2_EESD_T1_SE_
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B7v160006Ev
- __ZNSt3__130__uninitialized_allocator_copyB7v160006INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__130__uninitialized_allocator_copyB7v160006INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE6assignIPS5_Li0EEEvT_SA_
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEC2ERKS7_
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB7v160006Em
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB7v160006Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE6assignIPS3_Li0EEEvT_S8_
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE7__clearB7v160006Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEEC2ERKS5_
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE6assignIPfLi0EEEvT_S6_
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2ERKS3_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___100-[CSRemoteControlClient _fetchDataFromAudioFileUrl:aesKey:encryptedAudioSampleBypeDepth:completion:]_block_invoke.323
- ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.577
- ___110-[CSVoiceTriggerSecondPass _requestStartAudioStreamWitContext:audioProviderUUID:startStreamOption:completion:]_block_invoke.486
- ___112-[CSAudioProvider audioPreprocessor:hasAvailableBuffer:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke
- ___112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.526
- ___113-[CSVoiceTriggerStatAggregator logTimeBasedTriggerLengthSampleCountStatistics:withAOPVTTriggerLengthSampleCount:]_block_invoke
- ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.511
- ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.520
- ___117-[CSVoiceTriggerEventInfoProvider fetchVoiceTriggerInfoWithAudioContext:resultVoiceTriggerInfo:resultRTSTriggerInfo:]_block_invoke
- ___124-[CSAudioRecorder _processAudioChain:audioStreamHandleId:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke
- ___125-[CSRemoteControlClient createRemoteVoiceProfileWithAudioFiles:aesKey:encryptedAudioSampleBypeDepth:languageCode:completion:]_block_invoke.297
- ___125-[CSRemoteControlClient createRemoteVoiceProfileWithAudioFiles:aesKey:encryptedAudioSampleBypeDepth:languageCode:completion:]_block_invoke.301
- ___127-[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:]_block_invoke
- ___141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke
- ___141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_2
- ___141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_3
- ___141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_4
- ___141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_5
- ___141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_6
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.581
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.582
- ___159-[CSAudioRecorder audioDecoderDidDecodePackets:audioStreamHandleId:buffer:remoteVAD:timestamp:arrivalTimestampToAudioRecorder:wasBuffered:receivedNumChannels:]_block_invoke
- ___160-[CSVoiceTriggerFirstPassHearst initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:]_block_invoke
- ___161+[CSCoreSpeechServices _voiceTriggerRTModelForVersion:minorVersion:accessoryRTModelType:accessoryInfo:endpointId:downloadedModels:preinstalledModels:completion:]_block_invoke.28
- ___161+[CSCoreSpeechServices _voiceTriggerRTModelForVersion:minorVersion:accessoryRTModelType:accessoryInfo:endpointId:downloadedModels:preinstalledModels:completion:]_block_invoke.31
- ___21-[CSCarKitUtils init]_block_invoke
- ___24-[CSAudioProvider start]_block_invoke
- ___24-[CSAudioProvider start]_block_invoke.52
- ___24-[CSAudioProvider start]_block_invoke_2
- ___24-[CSAudioProvider start]_block_invoke_3
- ___24-[CSAudioProvider start]_block_invoke_4
- ___26-[CSBluetoothManager init]_block_invoke
- ___30-[CSAudioProvider isRecording]_block_invoke
- ___30-[CSAudioProvider recordRoute]_block_invoke
- ___30-[CSAudioRecorder willDestroy]_block_invoke
- ___30-[CSAudioRecorder willDestroy]_block_invoke_2
- ___30-[CSAudioRecorder willDestroy]_block_invoke_3
- ___30-[CSBuiltInVoiceTrigger start]_block_invoke.440
- ___30-[CSBuiltInVoiceTrigger start]_block_invoke.448
- ___30-[CSBuiltInVoiceTrigger start]_block_invoke_2.451
- ___31+[CSCarKitUtils sharedInstance]_block_invoke
- ___31-[CSAudioProvider isNarrowBand]_block_invoke
- ___32-[CSAudioProvider playbackRoute]_block_invoke
- ___33-[CSAudioProvider alertStartTime]_block_invoke
- ___33-[CSAudioProvider recordSettings]_block_invoke
- ___34-[CSAudioFileReader stopRecording]_block_invoke
- ___34-[CSAudioProvider audioDeviceInfo]_block_invoke
- ___35+[CSSiriAudioSession sharedSession]_block_invoke
- ___35-[CSAudioFileReader startRecording]_block_invoke
- ___35-[CSAudioFileReader startRecording]_block_invoke_2
- ___35-[CSAudioProvider recordDeviceInfo]_block_invoke
- ___35-[CSRemoteRecordClient isConnected]_block_invoke
- ___35-[CSRemoteRecordClient isRecording]_block_invoke
- ___35-[NSArray(XPCObject) _cs_xpcObject]_block_invoke
- ___36+[CSBluetoothManager sharedInstance]_block_invoke
- ___36-[CSAudioProvider setAudioRecorder:]_block_invoke
- ___36-[CSAudioRecorder registerObserver:]_block_invoke
- ___36-[CSSiriAcousticFingerprinter flush]_block_invoke.61
- ___37-[CSAudioProvider audioChunkFrom:to:]_block_invoke
- ___37-[CSAudioProvider enableMiniDucking:]_block_invoke
- ___38+[CSSiriPreferences sharedPreferences]_block_invoke
- ___38-[CSAudioRecorder _getVoiceController]_block_invoke
- ___38-[CSAudioRecorder unregisterObserver:]_block_invoke
- ___38-[CSRemoteRecordClient stopRecording:]_block_invoke
- ___39+[CSMSNExceptionManager sharedInstance]_block_invoke
- ___39-[CSAudioProvider _shouldStopRecording]_block_invoke
- ___39-[CSAudioProvider audioChunkToEndFrom:]_block_invoke
- ___39-[CSAudioProvider setDuckOthersOption:]_block_invoke
- ___39-[CSBuiltInVoiceTrigger _stopListening]_block_invoke.503
- ___39-[CSSiriAudioSession currentInputRoute]_block_invoke
- ___39-[CSSiriAudioSession currentInputRoute]_block_invoke.34
- ___39-[CSSiriAudioSession currentInputRoute]_block_invoke_2
- ___40-[CSSiriAudioSession currentOutputRoute]_block_invoke
- ___40-[CSSiriAudioSession currentOutputRoute]_block_invoke_2
- ___40-[CSSiriAudioSession currentOutputRoute]_block_invoke_3
- ___40-[NSDictionary(XPCObject) _cs_xpcObject]_block_invoke
- ___41+[CSHardwareLatencyHelper sharedInstance]_block_invoke
- ___41-[CSAudioProvider cancelAudioStreamHold:]_block_invoke
- ___41-[CSAudioProvider playAlertSoundForType:]_block_invoke
- ___41-[CSAudioProvider setAudioAlertDelegate:]_block_invoke
- ___41-[CSAudioRecorder setContext:completion:]_block_invoke
- ___41-[CSRemoteRecordClient didDeviceConnect:]_block_invoke
- ___41-[CSRemoteRecordClient didDeviceConnect:]_block_invoke.10
- ___42+[CSRemoteDarwinDeviceInfo sharedInstance]_block_invoke
- ___42-[CSAudioProvider _preEpilogueAudioStream]_block_invoke
- ___42-[CSAudioProvider configureAlertBehavior:]_block_invoke
- ___42-[CSAudioRecorder _hasLocalPendingTwoShot]_block_invoke
- ___42-[CSCarKitUtils _fetchCarCapabilitiesDict]_block_invoke
- ___42-[CSCarKitUtils _fetchCarCapabilitiesDict]_block_invoke_2
- ___42-[CSRemoteControlClient didDeviceConnect:]_block_invoke.72
- ___43+[CSAudioRouteChangeMonitor sharedInstance]_block_invoke
- ___43+[CSAudioServerCrashMonitor sharedInstance]_block_invoke
- ___43+[CSCXPhoneCallStateMonitor sharedInstance]_block_invoke
- ___43+[CSTUPhoneCallStateMonitor sharedInstance]_block_invoke
- ___43-[CSAudioProvider _postEpilogueAudioStream]_block_invoke
- ___43-[CSAudioProvider setAudioSessionDelegate:]_block_invoke
- ___43-[CSAudioProvider setCurrentContext:error:]_block_invoke
- ___43-[CSRemoteRecordClient didPlayEndpointBeep]_block_invoke
- ___43-[CSRemoteRecordClient didPlayEndpointBeep]_block_invoke_2
- ___43-[CSTUPhoneCallStateMonitor firstPartyCall]_block_invoke
- ___43-[CSTUPhoneCallStateMonitor phoneCallState]_block_invoke
- ___44+[CSUserSessionActiveMonitor sharedInstance]_block_invoke
- ___44-[CSAudioProvider _handleAudioSystemFailure]_block_invoke
- ___44-[CSAudioProvider setAudioProviderDelegate:]_block_invoke
- ___44-[CSBuiltInVoiceTrigger _stopAPVoiceTrigger]_block_invoke.506
- ___44-[CSRemoteRecordClient didDeviceDisconnect:]_block_invoke
- ___44-[NSArray(XPCObject) _cs_initWithXPCObject:]_block_invoke
- ___45-[CSAudioProvider audioRecorderDisconnected:]_block_invoke
- ___45-[CSRemoteRecordClient hasPendingTwoShotBeep]_block_invoke
- ___45-[CSRemoteRecordClient hasPendingTwoShotBeep]_block_invoke_2
- ___45-[CSRemoteRecordClient voiceTriggerEventInfo]_block_invoke
- ___45-[CSRemoteRecordClient voiceTriggerEventInfo]_block_invoke_2
- ___45-[CSSiriAcousticFingerprinter appendPCMData:]_block_invoke.57
- ___45-[CSSiriAcousticFingerprinter appendPCMData:]_block_invoke.59
- ___46+[CSAudioStreamActivityMonitor sharedInstance]_block_invoke
- ___46+[CSCoreSpeechServices requestUpdatedSATAudio]_block_invoke.48
- ___46-[CSSiriMobileBluetoothDeviceProxy deviceInfo]_block_invoke.116
- ___47+[CSCoreSpeechServices getFirstPassRunningMode]_block_invoke.50
- ___47-[CSAudioProvider _scheduleAlertFinishTimeout:]_block_invoke
- ___47-[CSAudioProvider _scheduleAudioPacketWatchDog]_block_invoke
- ___47-[CSAudioProvider notifyProviderContextChanged]_block_invoke
- ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.551
- ___48+[CSSiriAudioSession currentInputDeviceUIDArray]_block_invoke
- ___48+[CSVoiceTriggerStatAggregator sharedAggregator]_block_invoke
- ___48-[CSAudioProvider audioChunkFrom:to:channelIdx:]_block_invoke
- ___48-[CSAudioProvider audioRecorderWillBeDestroyed:]_block_invoke
- ___48-[CSAudioProvider circularBufferNumInputChannel]_block_invoke
- ___48-[CSAudioProvider deactivateAudioSession:error:]_block_invoke
- ___48-[CSAudioProvider prewarmAudioSessionWithError:]_block_invoke
- ___48-[CSAudioRecorder setAudioSessionEventDelegate:]_block_invoke
- ___48-[CSAudioRouteChangeMonitorImpl jarvisConnected]_block_invoke
- ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.60
- ___49+[CSVoiceTriggerEventInfoProvider sharedInstance]_block_invoke
- ___49-[CSAssetController _downloadAsset:withComplete:]_block_invoke.270
- ___49-[CSRemoteDarwinDeviceInfo allDeviceDisconnected]_block_invoke
- ___49-[NSDictionary(XPCObject) _cs_initWithXPCObject:]_block_invoke
- ___50-[CSAttSiriMitigationAssetHandler setCachedAsset:]_block_invoke
- ___50-[CSAudioProvider audioChunkToEndFrom:channelIdx:]_block_invoke
- ___50-[CSAudioRouteChangeMonitorImpl hearstRouteStatus]_block_invoke
- ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.641
- ___50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.469
- ___51-[CSAttendingServiceClient _createClientConnection]_block_invoke.78
- ___51-[CSAttendingServiceClient _createClientConnection]_block_invoke.80
- ___51-[CSAudioProvider enableSmartRoutingConsideration:]_block_invoke
- ___51-[CSAudioRecorder _createVoiceControllerWithError:]_block_invoke
- ___51-[CSAudioRecorder _createVoiceControllerWithError:]_block_invoke_2
- ___51-[CSTUPhoneCallStateMonitor _fetchTUPhoneCallState]_block_invoke
- ___52-[CSAudioProvider saveRecordingBufferFrom:to:toURL:]_block_invoke
- ___52-[CSAudioProvider triggerInfoForContext:completion:]_block_invoke
- ___52-[CSAudioRouteChangeMonitorImpl getJarvisConnected:]_block_invoke
- ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.498
- ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke_2.499
- ___52-[CSRemoteDarwinDeviceInfo deviceConnectedWithUUID:]_block_invoke
- ___52-[CSRemoteDarwinDeviceInfo hasDarwinDeviceConnected]_block_invoke
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.444
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.450
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.455
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.462
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.463
- ___52-[CSVoiceTriggerAssetHandlerMac triggerAssetRefresh]_block_invoke.248
- ___53-[CSAudioProvider _holdAudioStreamWithHolder:option:]_block_invoke
- ___53-[CSAudioProvider _saveRecordingBufferFrom:to:toURL:]_block_invoke
- ___53-[CSAudioProvider setLatestRecordContext:streamType:]_block_invoke
- ___53-[CSAudioProvider stopAudioStream:option:completion:]_block_invoke
- ___53-[CSBluetoothManager getBTLocalDeviceWithCompletion:]_block_invoke
- ___53-[CSRemoteControlClient _transferFile:at:completion:]_block_invoke.157
- ___54-[CSAssetController fetchRemoteMetaOfType:allowRetry:]_block_invoke.258
- ___54-[CSAttSiriMitigationAssetHandler triggerAssetRefresh]_block_invoke.26
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.103
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.108
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.111
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.97
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.104
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.109
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3
- ___54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.110
- ___54-[CSAudioProvider saveRecordingBufferToEndFrom:toURL:]_block_invoke
- ___54-[CSAudioProvider setAlertSoundFromURL:forType:force:]_block_invoke
- ___54-[CSAudioProvider startAudioStream:option:completion:]_block_invoke
- ___54-[CSAudioProvider startAudioStream:option:completion:]_block_invoke.79
- ___54-[CSAudioProvider startAudioStream:option:completion:]_block_invoke_2
- ___54-[CSAudioRecorder _shouldLogResourceNotAvailableError]_block_invoke
- ___54-[CSAudioRecorder remoteRecordConnectionDisconnected:]_block_invoke
- ___54-[CSAudioRouteChangeMonitorImpl getHearstRouteStatus:]_block_invoke
- ___54-[CSAudioStream stopAudioStreamWithOption:completion:]_block_invoke
- ___54-[CSCXPhoneCallStateMonitor callObserver:callChanged:]_block_invoke
- ___55-[CSAttSiriServiceClient _setupAttSiriSvcXpcConnection]_block_invoke.72
- ___55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke
- ___55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.95
- ___55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.96
- ___55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke_2
- ___55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke_3
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.80
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.81
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.83
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.86
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.87
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.88
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.89
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.92
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.84
- ___55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.90
- ___55-[CSAudioProvider circularBufferInputRecordingDuration]_block_invoke
- ___55-[CSAudioRouteChangeMonitorImplWatch hearstRouteStatus]_block_invoke
- ___55-[CSAudioServerCrashMonitor _startMonitoringWithQueue:]_block_invoke
- ___55-[CSAudioServerCrashMonitor _startMonitoringWithQueue:]_block_invoke.6
- ___55-[CSAudioStream startAudioStreamWithOption:completion:]_block_invoke
- ___55-[CSRemoteDarwinDeviceInfo deviceDisconnectedWithUUID:]_block_invoke
- ___56-[CSAudioProvider prepareAudioStreamSync:request:error:]_block_invoke
- ___56-[CSAudioRecorder voiceControllerEndRecordInterruption:]_block_invoke
- ___56-[CSAudioSampleRateConverter convertSampleRateOfBuffer:]_block_invoke
- ___56-[CSRemoteRecordClient startRecordingWithOptions:error:]_block_invoke
- ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.651
- ___57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke
- ___57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.133
- ___57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke_2
- ___57-[CSAudioProvider holdAudioStreamWithDescription:option:]_block_invoke
- ___57-[CSAudioProvider prepareAudioStream:request:completion:]_block_invoke
- ___57-[CSAudioProvider prepareAudioStream:request:completion:]_block_invoke_2
- ___57-[CSAudioRouteChangeMonitorImpl pickableRoutesDidChange:]_block_invoke
- ___57-[CSAudioRouteChangeMonitorImpl pickableRoutesDidChange:]_block_invoke.6
- ___57-[CSAudioRouteChangeMonitorImplWatch getJarvisConnected:]_block_invoke
- ___57-[CSRemoteDarwinDeviceInfo fetchDeviceUUIDStringFromUID:]_block_invoke
- ___57-[CSTUPhoneCallStateMonitor _callStatusDidChangeHandler:]_block_invoke
- ___58-[CSAudioProvider _prepareAudioStream:request:completion:]_block_invoke
- ___58-[CSAudioProvider audioRecorderStreamHandleIdInvalidated:]_block_invoke
- ___58-[CSAudioProvider supportsDuckingOnCurrentRouteWithError:]_block_invoke
- ___58-[CSAudioRecorder voiceControllerBeginRecordInterruption:]_block_invoke
- ___58-[CSAudioRouteChangeMonitorImpl _notifyHearstRouteStatus:]_block_invoke
- ___58-[CSAudioRouteChangeMonitorImpl getHearstOwnershipStatus:]_block_invoke
- ___58-[CSRemoteControlClient exchangeRemoteDeviceProtocolInfo:]_block_invoke.282
- ___59-[CSAudioProvider audioStreamWithRequest:streamName:error:]_block_invoke
- ___59-[CSAudioRouteChangeMonitorImpl _startMonitoringWithQueue:]_block_invoke
- ___59-[CSAudioRouteChangeMonitorImpl _startMonitoringWithQueue:]_block_invoke_2
- ___59-[CSAudioRouteChangeMonitorImplWatch getHearstRouteStatus:]_block_invoke
- ___59-[CSConnectionListener listener:shouldAcceptNewConnection:]_block_invoke_2.9
- ___60-[CSAudioProvider _scheduleDidStopRecordingDelegateWatchDog]_block_invoke
- ___60-[CSBluetoothManager getBluetoothDeviceInfoForDeviceWithId:]_block_invoke
- ___60-[CSBluetoothManager getWirelessSplitterInfoWithCompletion:]_block_invoke
- ___60-[CSMSNExceptionManager endAnnounceMessageException:reason:]_block_invoke
- ___60-[CSRemoteDarwinDeviceInfo isRemoteDarwinConnectedWithUUID:]_block_invoke
- ___60-[CSSiriSpeechRecorder _reportServerEndpointMetricsIfNeeded]_block_invoke_2
- ___61-[CSAudioProvider _scheduleDidStartRecordingDelegateWatchDog]_block_invoke
- ___61-[CSAudioRecorder voiceControllerEncoderErrorDidOccur:error:]_block_invoke
- ___61-[CSAudioRouteChangeMonitorImpl carPlayIsConnectedDidChange:]_block_invoke
- ___61-[CSModelBenchmarker _setupAudioInjectionEngineWithAudioURL:]_block_invoke.50
- ___61-[CSRemoteDarwinDeviceInfo fetchRichDeviceUIDStringFromUUID:]_block_invoke
- ___61-[CSRemoteDarwinDeviceInfo hasDarwinDeviceHandleVoiceTrigger]_block_invoke
- ___61-[CSRemoteRecordClient initWithDeviceId:audioStreamHandleId:]_block_invoke
- ___61-[CSRemoteRecordClient initWithDeviceId:audioStreamHandleId:]_block_invoke_2
- ___62-[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]_block_invoke
- ___62-[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]_block_invoke_2
- ___62-[CSAudioProvider setAnnounceCallsEnabled:withStreamHandleID:]_block_invoke
- ___62-[CSAudioRecorder voiceControllerStreamInvalidated:forStream:]_block_invoke
- ___62-[CSAudioRouteChangeMonitorImpl _notifyJarvisConnectionState:]_block_invoke
- ___62-[CSMSNExceptionManager beginAnnounceMessageException:reason:]_block_invoke
- ___63-[CSAudioRouteChangeMonitorImplWatch _notifyHearstRouteStatus:]_block_invoke
- ___63-[CSAudioRouteChangeMonitorImplWatch getHearstOwnershipStatus:]_block_invoke
- ___64-[CSAudioProvider audioStreamWithRequest:streamName:completion:]_block_invoke
- ___64-[CSAudioProvider audioStreamWithRequest:streamName:completion:]_block_invoke_2
- ___64-[CSAudioRouteChangeMonitorImplWatch _startMonitoringWithQueue:]_block_invoke
- ___64-[CSAudioRouteChangeMonitorImplWatch activeAudioRouteDidChange:]_block_invoke
- ___64-[CSAudioRouteChangeMonitorImplWatch activeAudioRouteDidChange:]_block_invoke.2
- ___64-[CSAudioServerCrashMonitor _didReceiveMediaserverNotification:]_block_invoke
- ___64-[CSRemoteDarwinDeviceInfo isPrimaryVoiceTriggerDeviceWithUUID:]_block_invoke
- ___64-[CSVoiceTriggerEventInfoProvider setVoiceTriggerInfo:deviceId:]_block_invoke
- ___65-[CSAudioProvider attachTandemStream:toPrimaryStream:completion:]_block_invoke
- ___65-[CSAudioProvider attachTandemStream:toPrimaryStream:completion:]_block_invoke_2
- ___65-[CSAudioRouteChangeMonitorImpl preferredExternalRouteDidChange:]_block_invoke
- ___65-[CSAudioRouteChangeMonitorImpl preferredExternalRouteDidChange:]_block_invoke.4
- ___65-[CSCarKitUtils _fetchCarCapabilitiesInBackgroundWithCompletion:]_block_invoke
- ___66-[CSAudioProvider CSAudioServerCrashMonitorDidReceiveServerCrash:]_block_invoke
- ___66-[CSAudioRecorder remoteRecordLPCMBufferAvailable:streamHandleId:]_block_invoke
- ___66-[CSAudioRouteChangeMonitorImpl carPlayAuxStreamSupportDidChange:]_block_invoke
- ___67-[CSVoiceTriggerStatAggregator reportDigitalZerosWithAudioZeroRun:]_block_invoke
- ___68-[CSAudioProvider CSAudioServerCrashMonitorDidReceiveServerRestart:]_block_invoke
- ___68-[CSAudioProvider audioRecorderBuiltInAudioStreamInvalidated:error:]_block_invoke
- ___68-[CSAudioProvider audioRecorderDidFinishAlertPlayback:ofType:error:]_block_invoke
- ___68-[CSBuiltInVoiceTrigger _startListenPollingWithInterval:completion:]_block_invoke.493
- ___68-[CSEndpointerXPCClient getFirstAudioSampleSensorHostTimeWithReply:]_block_invoke
- ___68-[CSRemoteDarwinDeviceInfo addDeviceIDPairToMapTable:withDeviceUID:]_block_invoke
- ___68-[CSRemoteDarwinDeviceInfo notifyVoiceTriggerEnabledWithDeviceUUID:]_block_invoke
- ___68-[CSVoiceTriggerStatAggregator logAOPFirstPassTriggerWakeupLatency:]_block_invoke
- ___69-[CSRemoteDarwinDeviceInfo notifyVoiceTriggerDisabledWithDeviceUUID:]_block_invoke
- ___69-[CSSiriMobileBluetoothDeviceProxy initWithAddress:dataSource:queue:]_block_invoke.114
- ___70-[CSAudioRecorder voiceControllerBeginRecordInterruption:withContext:]_block_invoke
- ___70-[CSAudioRecorder voiceControllerDidFinishAlertPlayback:ofType:error:]_block_invoke
- ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.652
- ___71-[CSAudioRecorder audioFileReaderDidStartRecording:successfully:error:]_block_invoke
- ___71-[CSAudioRecorder voiceControllerDidSetAudioSessionActive:isActivated:]_block_invoke
- ___71-[CSAudioRecorder voiceControllerDidStopRecording:forStream:forReason:]_block_invoke
- ___71-[CSAudioRouteChangeMonitorImpl _fetchHearstRouteStatusWithCompletion:]_block_invoke
- ___71-[CSSiriMobileBluetoothDeviceProxy initWithDeviceUID:dataSource:queue:]_block_invoke.115
- ___72-[CSBluetoothManager getBTDeviceInfoWithBTAddressString:withCompletion:]_block_invoke
- ___73-[CSAudioProvider audioRecorderDidStopRecord:audioStreamHandleId:reason:]_block_invoke
- ___73-[CSAudioRecorder remoteRecordDidStartRecordingWithStreamHandleId:error:]_block_invoke
- ___73-[CSAudioRecorder voiceControllerWillSetAudioSessionActive:willActivate:]_block_invoke
- ___73-[CSBluetoothManager getConnectedBluetoothDeviceAddressesWithCompletion:]_block_invoke
- ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.640
- ___74-[CSAudioProvider CSPhoneCallStateMonitor:didRecievePhoneCallStateChange:]_block_invoke
- ___75-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:]_block_invoke
- ___75-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:]_block_invoke_2
- ___75-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:]_block_invoke.623
- ___76-[CSAudioRecorder remoteRecordDidStopRecordingWithWithStreamHandleId:error:]_block_invoke
- ___76-[CSAudioRouteChangeMonitorImplWatch _fetchHearstRouteStatusWithCompletion:]_block_invoke
- ___76-[CSBluetoothManager accessoryManager:accessoryEvent:device:accessoryState:]_block_invoke
- ___77-[CSAudioRouteChangeMonitor routeIsDoAPSupportedWithRouteUID:withCompletion:]_block_invoke
- ___77-[CSAudioRouteChangeMonitor routeIsDoAPSupportedWithRouteUID:withCompletion:]_block_invoke_2
- ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.522
- ___77-[CSSpeechManager CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke.481
- ___78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke
- ___78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.123
- ___78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke_2
- ___78-[CSAudioStreamActivityMonitor hasNonVoiceTriggerStreamsOrStreamHoldersActive]_block_invoke
- ___78-[CSRemoteControlClient transferVoiceTriggerAsset:forLanguageCode:completion:]_block_invoke.193
- ___78-[CSVoiceTriggerStatAggregator logSecondPassResult:eventInfo:triggerAPWakeUp:]_block_invoke
- ___81-[CSAudioRecorder voiceControllerDidStartRecording:forStream:successfully:error:]_block_invoke
- ___81-[CSSiriMobileBluetoothDeviceProxy _accessBTDeviceAndAccessoryManagerUsingBlock:]_block_invoke.123
- ___82-[CSAudioProvider activateAudioSessionWithReason:dynamicAttribute:bundleID:error:]_block_invoke
- ___82-[CSAudioStreamActivityMonitor notifyActiveStreamsChanged:streamHolders:streamId:]_block_invoke
- ___82-[CSAudioStreamActivityMonitor notifyActiveStreamsChanged:streamHolders:streamId:]_block_invoke_2
- ___82-[CSHardwareLatencyHelper _hardwareLatenciesUsingStreamHandle:andVoiceController:]_block_invoke
- ___82-[CSHardwareLatencyHelper _hardwareLatenciesUsingStreamHandle:andVoiceController:]_block_invoke_2
- ___82-[CSOnDeviceCompilationHandler compileUsingConfig:locale:compileDirectory:errOut:]_block_invoke
- ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.499
- ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.507
- ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.597
- ___85-[CSAudioProvider audioRecorderRecordHardwareConfigurationDidChange:toConfiguration:]_block_invoke
- ___85-[CSAudioProvider audioRecorderRecordHardwareConfigurationDidChange:toConfiguration:]_block_invoke_2
- ___85-[CSAudioRecorder userSessionActivateMonitor:didReceivedUserSessionActiveHasChanged:]_block_invoke
- ___85-[CSRemoteControlClient transferInterstitialAudioFiles:interstitialLevel:completion:]_block_invoke.245
- ___86-[CSAudioProvider audioRecorderDidStartRecord:audioStreamHandleId:successfully:error:]_block_invoke
- ___86-[CSBluetoothManager device:serviceMask:serviceEventType:serviceSpecificEvent:result:]_block_invoke
- ___87-[CSAudioRecorder voiceControllerRecordHardwareConfigurationDidChange:toConfiguration:]_block_invoke
- ___88-[CSVoiceTriggerFirstPassHearst CSPhoneCallStateMonitor:didRecievePhoneCallStateChange:]_block_invoke
- ___89+[CSCoreSpeechServices voiceTriggerJarvisLanguageList:jarvisSelectedLanguage:completion:]_block_invoke.46
- ___91-[CSAudioRecorder _processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:]_block_invoke
- ___92-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:completion:]_block_invoke.240
- ___92-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:completion:]_block_invoke.242
- ___93-[CSOnDeviceCachedIrPurgingHandler voiceTriggerAssetHandler:endpointId:didChangeCachedAsset:]_block_invoke
- ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.498
- ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.506
- ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke_2.508
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.609
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.610
- ___Block_byref_object_copy_.10758
- ___Block_byref_object_copy_.11422
- ___Block_byref_object_copy_.12573
- ___Block_byref_object_copy_.13978
- ___Block_byref_object_copy_.14335
- ___Block_byref_object_copy_.14941
- ___Block_byref_object_copy_.15835
- ___Block_byref_object_copy_.16830
- ___Block_byref_object_copy_.17037
- ___Block_byref_object_copy_.1837
- ___Block_byref_object_copy_.19009
- ___Block_byref_object_copy_.19636
- ___Block_byref_object_copy_.19954
- ___Block_byref_object_copy_.21302
- ___Block_byref_object_copy_.21569
- ___Block_byref_object_copy_.22788
- ___Block_byref_object_copy_.23194
- ___Block_byref_object_copy_.23550
- ___Block_byref_object_copy_.24216
- ___Block_byref_object_copy_.25128
- ___Block_byref_object_copy_.25812
- ___Block_byref_object_copy_.2616
- ___Block_byref_object_copy_.26288
- ___Block_byref_object_copy_.26959
- ___Block_byref_object_copy_.27861
- ___Block_byref_object_copy_.28183
- ___Block_byref_object_copy_.28847
- ___Block_byref_object_copy_.29232
- ___Block_byref_object_copy_.30268
- ___Block_byref_object_copy_.30846
- ___Block_byref_object_copy_.31899
- ___Block_byref_object_copy_.32
- ___Block_byref_object_copy_.32332
- ___Block_byref_object_copy_.32485
- ___Block_byref_object_copy_.32606
- ___Block_byref_object_copy_.3267
- ___Block_byref_object_copy_.33180
- ___Block_byref_object_copy_.33737
- ___Block_byref_object_copy_.34167
- ___Block_byref_object_copy_.3426
- ___Block_byref_object_copy_.346
- ___Block_byref_object_copy_.4583
- ___Block_byref_object_copy_.4721
- ___Block_byref_object_copy_.4828
- ___Block_byref_object_copy_.5400
- ___Block_byref_object_copy_.7241
- ___Block_byref_object_copy_.7573
- ___Block_byref_object_copy_.8280
- ___Block_byref_object_copy_.9025
- ___Block_byref_object_copy_.9605
- ___Block_byref_object_dispose_.10759
- ___Block_byref_object_dispose_.11423
- ___Block_byref_object_dispose_.12574
- ___Block_byref_object_dispose_.13979
- ___Block_byref_object_dispose_.14336
- ___Block_byref_object_dispose_.14942
- ___Block_byref_object_dispose_.15836
- ___Block_byref_object_dispose_.16831
- ___Block_byref_object_dispose_.17038
- ___Block_byref_object_dispose_.1838
- ___Block_byref_object_dispose_.19010
- ___Block_byref_object_dispose_.19637
- ___Block_byref_object_dispose_.19955
- ___Block_byref_object_dispose_.21303
- ___Block_byref_object_dispose_.21570
- ___Block_byref_object_dispose_.22789
- ___Block_byref_object_dispose_.23195
- ___Block_byref_object_dispose_.23551
- ___Block_byref_object_dispose_.24217
- ___Block_byref_object_dispose_.25129
- ___Block_byref_object_dispose_.25813
- ___Block_byref_object_dispose_.2617
- ___Block_byref_object_dispose_.26289
- ___Block_byref_object_dispose_.26960
- ___Block_byref_object_dispose_.27862
- ___Block_byref_object_dispose_.28184
- ___Block_byref_object_dispose_.28848
- ___Block_byref_object_dispose_.29233
- ___Block_byref_object_dispose_.30269
- ___Block_byref_object_dispose_.30847
- ___Block_byref_object_dispose_.31900
- ___Block_byref_object_dispose_.32333
- ___Block_byref_object_dispose_.32486
- ___Block_byref_object_dispose_.32607
- ___Block_byref_object_dispose_.3268
- ___Block_byref_object_dispose_.33
- ___Block_byref_object_dispose_.33181
- ___Block_byref_object_dispose_.33738
- ___Block_byref_object_dispose_.34168
- ___Block_byref_object_dispose_.3427
- ___Block_byref_object_dispose_.347
- ___Block_byref_object_dispose_.4584
- ___Block_byref_object_dispose_.4722
- ___Block_byref_object_dispose_.4829
- ___Block_byref_object_dispose_.5401
- ___Block_byref_object_dispose_.7242
- ___Block_byref_object_dispose_.7574
- ___Block_byref_object_dispose_.8281
- ___Block_byref_object_dispose_.9026
- ___Block_byref_object_dispose_.9606
- ___CSSiriUserSupportBaseURL_block_invoke
- ___CarKitLibraryCore_block_invoke
- ___MediaSafetyNetLibraryCore_block_invoke
- ___MobileTimerLibraryCore_block_invoke.1235
- ____AudioDeviceInputSource_block_invoke
- ____AudioDeviceIsInputDevice_block_invoke
- ____AudioDeviceIsOutputDevice_block_invoke
- ____AudioDeviceIsStereoDevice_block_invoke
- ____AudioDeviceName_block_invoke
- ____AudioDeviceOutputSource_block_invoke
- ____AudioDeviceRegisterForChangedNotification_block_invoke
- ____AudioDeviceRegisterForChangedNotification_block_invoke_2
- ____AudioDeviceTransport_block_invoke
- ____AudioDeviceUID_block_invoke
- ___block_descriptor_40_e8_32bs_e31_v16?0"CSBluetoothDeviceInfo"8ls32l8
- ___block_descriptor_40_e8_32bs_e44_v20?0I8r^{AudioObjectPropertyAddress=III}12ls32l8
- ___block_descriptor_40_e8_32bs_e8_v12?0B8ls32l8
- ___block_descriptor_40_e8_32r_e12_v24?0^v8Q16lr32l8
- ___block_descriptor_40_e8_32r_e8_v12?0I8lr32l8
- ___block_descriptor_40_e8_32r_e9_v16?0^v8lr32l8
- ___block_descriptor_40_e8_32s_e12_v24?0^v8Q16ls32l8
- ___block_descriptor_40_e8_32s_e15_v32?0816^B24ls32l8
- ___block_descriptor_40_e8_32s_e15_v32?08Q16^B24ls32l8
- ___block_descriptor_40_e8_32s_e36_B24?0Q8"NSObject<OS_xpc_object>"16ls32l8
- ___block_descriptor_40_e8_32w_e42_v16?0"<CSStateCaptureOptionsMutablity>"8lw32l8
- ___block_descriptor_45_e8_32s_e19_"NSDictionary"8?0ls32l8
- ___block_descriptor_48_e8_32s40bs_e28_v16?0^{BTLocalDeviceImpl=}8ls40l8s32l8
- ___block_descriptor_48_e8_32s40r_e33_v16?0"NSObject<OS_xpc_object>"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e34_v24?0"NSDictionary"8"NSError"16lr40l8s32l8
- ___block_descriptor_52_e8_32s_e12_v24?0^v8Q16ls32l8
- ___block_descriptor_56_e19_"NSDictionary"8?0l
- ___block_descriptor_56_e8_32s40bs48r_e8_v12?0B8ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e28_v16?0^{BTLocalDeviceImpl=}8ls48l8s32l8s40l8
- ___block_descriptor_61_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_64_e8_32s40s48r_e5_v8?0ls32l8s40l8r48l8
- ___block_descriptor_64_e8_32s40s48r_e86_i32?0^I8^{AudioBufferList=I[1{AudioBuffer=II^v}]}16^^{AudioStreamPacketDescription}24ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls56l8s32l8s40l8s48l8
- ___block_descriptor_64_ea8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_68_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_72_e8_32s40r_e5_v8?0ls32l8r40l8
- ___block_descriptor_72_e8_32s40s48r56r64r_e5_v8?0lr48l8s32l8s40l8r56l8r64l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8s48l8r64l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e5_v8?0lr64l8s32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s_e20_v24?0"NSError"8Q16ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_84_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.10.11583
- ___block_literal_global.10.25337
- ___block_literal_global.10.26828
- ___block_literal_global.10046
- ___block_literal_global.10506
- ___block_literal_global.1053
- ___block_literal_global.1080
- ___block_literal_global.10862
- ___block_literal_global.11069
- ___block_literal_global.11192
- ___block_literal_global.1130
- ___block_literal_global.11454
- ___block_literal_global.11609
- ___block_literal_global.11792
- ___block_literal_global.1190
- ___block_literal_global.12001
- ___block_literal_global.12402
- ___block_literal_global.125
- ___block_literal_global.1258
- ___block_literal_global.12596
- ___block_literal_global.12869
- ___block_literal_global.12963
- ___block_literal_global.13.25530
- ___block_literal_global.13.26829
- ___block_literal_global.13011
- ___block_literal_global.13130
- ___block_literal_global.13431
- ___block_literal_global.13536
- ___block_literal_global.13589
- ___block_literal_global.13717
- ___block_literal_global.13753
- ___block_literal_global.14138
- ___block_literal_global.1415
- ___block_literal_global.14250
- ___block_literal_global.14473
- ___block_literal_global.14854
- ___block_literal_global.14963
- ___block_literal_global.15.15425
- ___block_literal_global.1507
- ___block_literal_global.15377
- ___block_literal_global.15424
- ___block_literal_global.15492
- ___block_literal_global.15546
- ___block_literal_global.15564
- ___block_literal_global.15675
- ___block_literal_global.16.15378
- ___block_literal_global.16.25338
- ___block_literal_global.16356
- ___block_literal_global.16441
- ___block_literal_global.1657
- ___block_literal_global.16927
- ___block_literal_global.17.25460
- ___block_literal_global.17021
- ___block_literal_global.17066
- ___block_literal_global.17383
- ___block_literal_global.1759
- ___block_literal_global.17963
- ___block_literal_global.18.15645
- ___block_literal_global.18.25531
- ___block_literal_global.18285
- ___block_literal_global.18463
- ___block_literal_global.18472
- ___block_literal_global.18599
- ___block_literal_global.18633
- ___block_literal_global.18887
- ___block_literal_global.18963
- ___block_literal_global.19060
- ___block_literal_global.19159
- ___block_literal_global.1935
- ___block_literal_global.20.30829
- ___block_literal_global.20130
- ___block_literal_global.20177
- ___block_literal_global.20407
- ___block_literal_global.20437
- ___block_literal_global.21.13537
- ___block_literal_global.21024
- ___block_literal_global.21316
- ___block_literal_global.21834
- ___block_literal_global.21899
- ___block_literal_global.22.25339
- ___block_literal_global.22170
- ___block_literal_global.22252
- ___block_literal_global.22301
- ___block_literal_global.22345
- ___block_literal_global.22361
- ___block_literal_global.22662
- ___block_literal_global.22951
- ___block_literal_global.23068
- ___block_literal_global.23216
- ___block_literal_global.23228
- ___block_literal_global.23306
- ___block_literal_global.23599
- ___block_literal_global.23774
- ___block_literal_global.23818
- ___block_literal_global.24031
- ___block_literal_global.2408
- ___block_literal_global.24202
- ___block_literal_global.24503
- ___block_literal_global.24558
- ___block_literal_global.246
- ___block_literal_global.25.25340
- ___block_literal_global.252
- ___block_literal_global.25336
- ___block_literal_global.25430
- ___block_literal_global.25459
- ___block_literal_global.25550
- ___block_literal_global.25625
- ___block_literal_global.25696
- ___block_literal_global.25737
- ___block_literal_global.25774
- ___block_literal_global.25885
- ___block_literal_global.26.30818
- ___block_literal_global.2636
- ___block_literal_global.26805
- ___block_literal_global.26826
- ___block_literal_global.269
- ___block_literal_global.27.13538
- ___block_literal_global.2722
- ___block_literal_global.27304
- ___block_literal_global.27474
- ___block_literal_global.27964
- ___block_literal_global.28.18856
- ___block_literal_global.28539
- ___block_literal_global.28868
- ___block_literal_global.28952
- ___block_literal_global.29.25341
- ___block_literal_global.29.25461
- ___block_literal_global.29058
- ___block_literal_global.29161
- ___block_literal_global.2927
- ___block_literal_global.29483
- ___block_literal_global.2996
- ___block_literal_global.30.13539
- ___block_literal_global.30533
- ___block_literal_global.30871
- ___block_literal_global.3097
- ___block_literal_global.3111
- ___block_literal_global.31226
- ___block_literal_global.31501
- ___block_literal_global.31636
- ___block_literal_global.31685
- ___block_literal_global.31722
- ___block_literal_global.31761
- ___block_literal_global.31928
- ___block_literal_global.32121
- ___block_literal_global.32273
- ___block_literal_global.32348
- ___block_literal_global.32447
- ___block_literal_global.32543
- ___block_literal_global.32634
- ___block_literal_global.3291
- ___block_literal_global.33240
- ___block_literal_global.33661
- ___block_literal_global.33899
- ___block_literal_global.34093
- ___block_literal_global.34178
- ___block_literal_global.34547
- ___block_literal_global.3502
- ___block_literal_global.3521
- ___block_literal_global.3581
- ___block_literal_global.36.13540
- ___block_literal_global.364
- ___block_literal_global.3673
- ___block_literal_global.3723
- ___block_literal_global.38.9846
- ___block_literal_global.4015
- ___block_literal_global.41.17339
- ___block_literal_global.42.13541
- ___block_literal_global.4201
- ___block_literal_global.426.12851
- ___block_literal_global.431.22051
- ___block_literal_global.44.17335
- ___block_literal_global.4462
- ___block_literal_global.453
- ___block_literal_global.46.9838
- ___block_literal_global.4633
- ___block_literal_global.465
- ___block_literal_global.4711
- ___block_literal_global.480
- ___block_literal_global.483
- ___block_literal_global.4867
- ___block_literal_global.49.24180
- ___block_literal_global.5.34548
- ___block_literal_global.550
- ___block_literal_global.571
- ___block_literal_global.5714
- ___block_literal_global.6682
- ___block_literal_global.669
- ___block_literal_global.67.9443
- ___block_literal_global.6792
- ___block_literal_global.6890
- ___block_literal_global.7.1246
- ___block_literal_global.7.26827
- ___block_literal_global.7071
- ___block_literal_global.7171
- ___block_literal_global.7194
- ___block_literal_global.7279
- ___block_literal_global.7624
- ___block_literal_global.7769
- ___block_literal_global.8.32115
- ___block_literal_global.8.32544
- ___block_literal_global.8.34549
- ___block_literal_global.8034
- ___block_literal_global.8332
- ___block_literal_global.841
- ___block_literal_global.9187
- ___block_literal_global.95
- ___block_literal_global.9723
- ___block_literal_global.9878
- ___block_literal_global.9930
- ___getCRCapabilitiesUserInfoKeySymbolLoc_block_invoke
- ___getCRFetchCarPlayCapabilitiesSymbolLoc_block_invoke
- ___getMSNMonitorBeginExceptionSymbolLoc_block_invoke
- ___getMSNMonitorEndExceptionSymbolLoc_block_invoke
- __audioStreamProvdider:audioBufferAvailable:.heartbeat_CORESPEECH_OPUS_ENCODING_BEGIN
- __audioStreamProvdider:audioBufferAvailable:.heartbeat_CORESPEECH_OPUS_ENCODING_END
- __audioStreamProvdider:audioBufferAvailable:.heartbeat_CORESPEECH_SPEECH_MANAGER_LPCM_RECORD_BUFFER_AVAILABLE
- __compensateChannelDataIfNeeded:receivedNumChannels:.heartbeat.33580
- __fetchHistoricalAudioAndForwardToStream:remoteVAD:.overrunHeartBeat
- __handleAudioChunk:.enableHeartbeat
- __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.20997
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.11767
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.20987
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.32820
- __processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:.heartbeat
- __processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:.heartbeat.536
- __sIsCarryDevice
- __shouldLogResourceNotAvailableError.answer
- __shouldLogResourceNotAvailableError.onceToken
- __unnamed_array_storage.136
- __unnamed_array_storage.142
- __unnamed_array_storage.153.27089
- __unnamed_array_storage.163
- __unnamed_array_storage.175
- __unnamed_array_storage.176.27073
- __unnamed_array_storage.198
- __unnamed_array_storage.20
- __unnamed_array_storage.224
- __unnamed_array_storage.231
- __unnamed_array_storage.23831
- __unnamed_array_storage.239
- __unnamed_array_storage.24239
- __unnamed_array_storage.247
- __unnamed_array_storage.25
- __unnamed_array_storage.25700
- __unnamed_array_storage.26
- __unnamed_array_storage.27097
- __unnamed_array_storage.287
- __unnamed_array_storage.294
- __unnamed_array_storage.30285
- __unnamed_array_storage.32
- __unnamed_array_storage.33.7097
- __unnamed_array_storage.33.8337
- __unnamed_array_storage.335
- __unnamed_array_storage.34
- __unnamed_array_storage.40
- __unnamed_array_storage.43
- __unnamed_array_storage.630
- __unnamed_array_storage.637
- __unnamed_array_storage.638
- __unnamed_array_storage.7112
- __unnamed_array_storage.7262
- __unnamed_array_storage.8336
- __xpc_type_array
- __xpc_type_bool
- __xpc_type_data
- __xpc_type_double
- __xpc_type_int64
- __xpc_type_string
- __xpc_type_uint64
- _audit_stringCarKit
- _audit_stringMediaSafetyNet
- _audit_stringMobileTimer.1238
- _getCRCapabilitiesUserInfoKeySymbolLoc.ptr
- _getCRFetchCarPlayCapabilitiesSymbolLoc.ptr
- _getMSNMonitorBeginExceptionSymbolLoc.ptr
- _getMSNMonitorEndExceptionSymbolLoc.ptr
- _init.onceToken
- _kAFSiriInternalUserClassification
- _kAssistantPreferencesDomain
- _kCSAudioStartStreamOptionStartHostTimeAdjustmentExceededMax
- _kCSDiagnosticReporterAudioDeliveryWatchDogFire
- _kCSDiagnosticReporterAudioDidStartWatchDogFire
- _kCSDiagnosticReporterAudioDidStopWatchDogFire
- _kCSDiagnosticReporterAudioInsufficientPriority
- _kCSDiagnosticReporterAudioResourceNotAvailable
- _kCSDiagnosticReporterEndpointDelayNegative
- _kCSDiagnosticReporterEndpointerProxyMissingFirstAudioSampleHostTime
- _kCSDiagnosticReporterRemoteCoreSpeechSubtypeAudioRecordingFailed
- _kCarPlayCapabilitiesUserInfoFlexibleFollowupDisabledKey
- _kCarPlayCapabilitiesUserInfoLatencyCorrectionSecondsKey
- _kKnownBadLatencyButCorrectionUnavailableValue
- _kMaxHostTimeAdjustmentSeconds
- _kRemoteRecordGibraltarDeviceId
- _kVTEISecondPassRejectionMHUUID_block_invoke.enableHeartbeat.11788
- _kVTEISecondPassRejectionMHUUID_block_invoke.enableHeartbeat.32881
- _kXPCEncodeKeyIsRemoteDevice
- _kXPCEncodeKeyPlaybackDeviceType
- _kXPCEncodeKeyPlaybackRoute
- _kXPCEncodeKeyRecordDeviceInfo
- _kXPCEncodeKeyRemoteDeviceProductIdentifier
- _kXPCEncodeKeyRemoteDeviceUID
- _kXPCEncodeKeyRemoteDeviceUIDString
- _kXPCEncodeKeyRoute
- _msnExceptionAnnounceMessage
- _objc_msgSend$CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:
- _objc_msgSend$CSAudioServerCrashMonitorDidReceiveServerCrash:
- _objc_msgSend$CSAudioServerCrashMonitorDidReceiveServerRestart:
- _objc_msgSend$CSPhoneCallStateMonitor:didRecievePhoneCallStateChange:
- _objc_msgSend$_acquireListeningMicIndicatorLockFrom:
- _objc_msgSend$_acquireRecordModeLockFrom:
- _objc_msgSend$_adjustmentSecondsFromLatencyInfo:error:
- _objc_msgSend$_alertBehaviorForRecordRoute:playbackRoute:recordingInfo:speechEvent:activationMode:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usesDeviceSpeakerForTTS:attemptsToUsePastDataBufferFrames:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isDeviceInCarDNDMode:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:
- _objc_msgSend$_alertBehaviorTypeFromAVVCOverrideType:
- _objc_msgSend$_attachBluetoothSession
- _objc_msgSend$_audioChunkFrom:to:
- _objc_msgSend$_audioChunkFrom:to:channelIdx:
- _objc_msgSend$_audioIsFromRemoteAccessory:
- _objc_msgSend$_audioRecorderDidStartRecordingSuccessfully:streamHandleID:error:
- _objc_msgSend$_audioRecorderDidStopRecordingForReason:streamHandleID:
- _objc_msgSend$_audioStreamProvdider:audioBufferAvailable:
- _objc_msgSend$_audioStreamWithRequest:streamName:error:
- _objc_msgSend$_canSetContext
- _objc_msgSend$_cancelAudioPacketWatchDog
- _objc_msgSend$_cancelAudioStreamHold:
- _objc_msgSend$_changePermissionOfBnnsIr:
- _objc_msgSend$_clearBluetoothDeviceInfoForDevice:
- _objc_msgSend$_clearDidStartRecordingDelegateWatchDog
- _objc_msgSend$_clearDidStopRecordingDelegateWatchDog
- _objc_msgSend$_clearListeningMicIndicatorProperty
- _objc_msgSend$_clearListeningMicIndicatorPropertyIfNeeded
- _objc_msgSend$_compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:
- _objc_msgSend$_compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:error:
- _objc_msgSend$_convertDeactivateOption:
- _objc_msgSend$_createCircularBufferIfNeededWithNumChannel:playbackRoute:
- _objc_msgSend$_createSampleRateConverterWithInASBD:outASBD:
- _objc_msgSend$_createVoiceControllerWithError:
- _objc_msgSend$_cs_isHashTableEmpty
- _objc_msgSend$_deactivateAudioSession:error:
- _objc_msgSend$_delayBecauseCarKitSendsNotificationBeforeCapabilitiesActuallyReady
- _objc_msgSend$_deliverHistoricalAudioToStreamsWithRemoteVAD:
- _objc_msgSend$_deliverPostprocessAudioChunk:toStream:lastForwardedSampleCount:
- _objc_msgSend$_destroyVoiceController
- _objc_msgSend$_detachBluetoothSession
- _objc_msgSend$_didFireStreamHolderTimeout:
- _objc_msgSend$_didPlayStartAlertSoundForSiri:audioStream:
- _objc_msgSend$_didReceiveFinishStartAlertPlaybackAt:
- _objc_msgSend$_didReceiveMediaserverNotification:
- _objc_msgSend$_fetchAllConnectedDevices
- _objc_msgSend$_fetchCarCapabilitiesDict
- _objc_msgSend$_fetchCarCapabilitiesInBackgroundWithCompletion:
- _objc_msgSend$_fetchCurrentMetrics
- _objc_msgSend$_fetchHearstConnectionState
- _objc_msgSend$_fetchHearstRouteStatusWithCompletion:
- _objc_msgSend$_fetchHistoricalAudioAndForwardToStream:remoteVAD:
- _objc_msgSend$_fetchJarvisConnectionState
- _objc_msgSend$_fetchRemoteRecordClientWithDeviceId:streamHandleId:
- _objc_msgSend$_fetchTUPhoneCallState
- _objc_msgSend$_forceReleaseAllListeningMicIndicatorLocks
- _objc_msgSend$_forceReleaseAllRecordModeLocks
- _objc_msgSend$_forceReleaseListeningMicIndicatorLockFrom:
- _objc_msgSend$_forceReleaseRecordModeLockFrom:
- _objc_msgSend$_forwardAudioChunk:toStream:
- _objc_msgSend$_forwardAudioChunkForTV:toStream:
- _objc_msgSend$_getAddressWithBTDevice:
- _objc_msgSend$_getBluetoothDeviceInfoForDeviceWithBTAddressString:
- _objc_msgSend$_getConnectedBluetoothDeviceAddressesFromLocalDevice:
- _objc_msgSend$_getRecordSettingsWithRequest:
- _objc_msgSend$_getVoiceController
- _objc_msgSend$_getWirelessSplitterInfoFromLocalDevice:
- _objc_msgSend$_handleAudioRecorderStreamHandleIdInvalidated:
- _objc_msgSend$_handleAudioSystemFailure
- _objc_msgSend$_handleDidStartAudioStreamWithResult:error:
- _objc_msgSend$_handleDidStartRecordingMessage:
- _objc_msgSend$_handleDidStopAudioStreamWithReason:
- _objc_msgSend$_handleTwoShotDetectedMessage:
- _objc_msgSend$_hardwareLatenciesUsingStreamHandle:andVoiceController:
- _objc_msgSend$_hardwareLatencyAdjustmentSeconds:hwLatencyType:error:
- _objc_msgSend$_hardwareLatencyAdjustmentSecondsUsingStreamHandle:andVoiceController:
- _objc_msgSend$_hasDeviceTemporaryPairedNotInContacts
- _objc_msgSend$_hasLocalPendingTwoShot
- _objc_msgSend$_holdAudioStreamWithHolder:option:
- _objc_msgSend$_holdRecordingExceptionIfNeeded:
- _objc_msgSend$_holdRecordingTransactionIfNeeded
- _objc_msgSend$_invalidateCachedCarPlayCapabilities
- _objc_msgSend$_isBuiltInDeviceFromDeviceId:
- _objc_msgSend$_isDuckingOnSpeakerOutputSupportedWithCurrentRoute
- _objc_msgSend$_isNarrowBand:
- _objc_msgSend$_isRemoteDarwinConnectedWithUUID:
- _objc_msgSend$_isValidLatencyCorrectionValue:
- _objc_msgSend$_latencyCorrectionSecondsForHeadUnit
- _objc_msgSend$_loadAACPCapabilityForDevice:deviceAddress:
- _objc_msgSend$_logResourceNotAvailableErrorIfNeeded:
- _objc_msgSend$_needResetAudioInjectionIndex:
- _objc_msgSend$_notifyHearstRouteStatus:
- _objc_msgSend$_notifyJarvisConnectionState:
- _objc_msgSend$_notifyObserver:withMediaserverState:
- _objc_msgSend$_onAudioPacketWatchdogFire
- _objc_msgSend$_onDeviceCompilationWithConfigFile:locale:
- _objc_msgSend$_postEpilogueAudioStream
- _objc_msgSend$_preEpilogueAudioStream
- _objc_msgSend$_prepareAudioStream:request:completion:
- _objc_msgSend$_prepareAudioStreamSync:request:error:
- _objc_msgSend$_processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:
- _objc_msgSend$_processAudioBuffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:
- _objc_msgSend$_processAudioChain:audioStreamHandleId:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:
- _objc_msgSend$_recacheCarPlayCapabilitiesWithCompletion:
- _objc_msgSend$_recordModeString:
- _objc_msgSend$_registerPhoneCallStateChangeNotifier
- _objc_msgSend$_releaseListeningMicIndicatorLock:
- _objc_msgSend$_releaseRecordModeLock:
- _objc_msgSend$_releaseRecordingTransactionIfNeeded
- _objc_msgSend$_reportMetrics
- _objc_msgSend$_reportVoiceTriggerFirstPassFireFromAP
- _objc_msgSend$_resetCircularBufferStartTime
- _objc_msgSend$_schduleDidStartRecordingDelegateWatchDogWithToken:
- _objc_msgSend$_scheduleAlertFinishTimeout:
- _objc_msgSend$_scheduleAudioPacketWatchDog
- _objc_msgSend$_scheduleDidStartRecordingDelegateWatchDog
- _objc_msgSend$_scheduleDidStopRecordingDelegateWatchDog
- _objc_msgSend$_scheduleDidStopRecordingDelegateWatchDog:
- _objc_msgSend$_setBluetoothDeviceInfoForDevice:
- _objc_msgSend$_setFirstAudioSampleSensorHostTimeIfNeeded:
- _objc_msgSend$_setLatestRecordContext:
- _objc_msgSend$_setListeningMicIndicatorProperty
- _objc_msgSend$_setListeningMicIndicatorPropertyIfNeeded
- _objc_msgSend$_shouldDuckOnBuiltInSpeaker
- _objc_msgSend$_shouldHandleStartPendingOnStopping:withStopReason:
- _objc_msgSend$_shouldInjectAudio
- _objc_msgSend$_shouldLogResourceNotAvailableError
- _objc_msgSend$_shouldStopRecording
- _objc_msgSend$_startAudioStream:option:completion:
- _objc_msgSend$_startAudioStreamForAudioInjectionWithAVVCContext:
- _objc_msgSend$_startObservingAudioRouteChange
- _objc_msgSend$_startObservingCarCapabilitiesNotfication:
- _objc_msgSend$_stopAudioStream:option:completion:
- _objc_msgSend$_stopTrackingRemoteAccessoryStreamId:
- _objc_msgSend$_streamStateName:
- _objc_msgSend$_switchToListeningMode
- _objc_msgSend$_switchToRecordingMode
- _objc_msgSend$_trackRemoteAccessoryStreamIdIfNeeded:
- _objc_msgSend$_updateCarPlayCapabilitiesDict
- _objc_msgSend$_updateLanguageCodeForRemoteVTEIResult:
- _objc_msgSend$_updateRemoteDeviceIdFromAVVCIfNeeded
- _objc_msgSend$_userInfoValueForKey:
- _objc_msgSend$_valuesAreMinimalyValidForInfoDictionary:type:
- _objc_msgSend$accessoryManager:accessoryEvent:device:accessoryState:
- _objc_msgSend$activateAudioSessionForStream:isPrewarm:error:
- _objc_msgSend$activateAudioSessionForStream:isPrewarm:recordMode:error:
- _objc_msgSend$activateAudioSessionWithReason:streamHandleId:error:
- _objc_msgSend$activationDeviceUID
- _objc_msgSend$activationMode
- _objc_msgSend$activeAudioRouteDidChange:
- _objc_msgSend$addDeviceIntoSplitterDeviceList:
- _objc_msgSend$addHWLatencyToOption:withCorrection:streamHandle:voiceController:
- _objc_msgSend$adjustStartRecordingHostTime:
- _objc_msgSend$alertDelegate
- _objc_msgSend$alertPlaybackFinishWaitingCompletions
- _objc_msgSend$alertPlaybackFinishWaitingStreams
- _objc_msgSend$allowExtendedRingBufferSize
- _objc_msgSend$allowRecordWhileBeep
- _objc_msgSend$announceCallsEnabled
- _objc_msgSend$attachTandemStream:toPrimaryStream:completion:
- _objc_msgSend$audioDeviceInfoWithStreamHandleId:recordDeviceIndicator:
- _objc_msgSend$audioFileReaderBufferAvailable:buffer:atTime:
- _objc_msgSend$audioFileReaderDidStartRecording:successfully:error:
- _objc_msgSend$audioFileReaderDidStopRecording:forReason:
- _objc_msgSend$audioInjectionFilePath
- _objc_msgSend$audioPreprocessor
- _objc_msgSend$audioPreprocessor:hasAvailableBuffer:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:
- _objc_msgSend$audioProviderInvalidated:streamHandleId:
- _objc_msgSend$audioRecorder:didSetAudioSessionActive:
- _objc_msgSend$audioRecorder:willSetAudioSessionActive:
- _objc_msgSend$audioRecorderBeginRecordInterruption:
- _objc_msgSend$audioRecorderBeginRecordInterruption:withContext:
- _objc_msgSend$audioRecorderBuiltInAudioStreamInvalidated:error:
- _objc_msgSend$audioRecorderDidFinishAlertPlayback:ofType:error:
- _objc_msgSend$audioRecorderDisconnected:
- _objc_msgSend$audioRecorderEndRecordInterruption:
- _objc_msgSend$audioRecorderRecordHardwareConfigurationDidChange:toConfiguration:
- _objc_msgSend$audioSessionEventProvidingDidSetAudioSessionActive:
- _objc_msgSend$audioSessionEventProvidingWillSetAudioSessionActive:
- _objc_msgSend$audioStreamProvider:audioBufferAvailable:lastForwardedSampleCount:
- _objc_msgSend$audioStreamType
- _objc_msgSend$averagePowerForChannel:
- _objc_msgSend$avvcAlertBehavior
- _objc_msgSend$avvcAlertOverrideType:
- _objc_msgSend$avvcContext
- _objc_msgSend$avvcStartRecordSettingsWithAudioStreamHandleId:
- _objc_msgSend$beepCanceller
- _objc_msgSend$beginAnnounceMessageException:reason:
- _objc_msgSend$bytesDataSize
- _objc_msgSend$callCenterWithQueue:
- _objc_msgSend$calls
- _objc_msgSend$cancelBeepFromSamples:timestamp:
- _objc_msgSend$carPlayAuxStreamSupportDidChange:
- _objc_msgSend$carPlayIsConnectedDidChange:
- _objc_msgSend$channels
- _objc_msgSend$chunkForChannel:
- _objc_msgSend$circularBufferStartHostTime
- _objc_msgSend$circularBufferStartSampleCount
- _objc_msgSend$clearListeningMicIndicatorProperty
- _objc_msgSend$clientIdentity
- _objc_msgSend$compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:
- _objc_msgSend$compileModelWithMilFile:bnnsIrCachePath:
- _objc_msgSend$compileUsingConfig:locale:compileDirectory:errOut:
- _objc_msgSend$configureAlertBehavior:audioStreamHandleId:
- _objc_msgSend$configureAlertBehaviorForStream:error:
- _objc_msgSend$copySamplesFrom:to:channelIdx:
- _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
- _objc_msgSend$currentAudioAndVideoCalls
- _objc_msgSend$currentInputDeviceUIDArray
- _objc_msgSend$deactivateAudioSession:streamHandleId:error:
- _objc_msgSend$deactivateAudioSessionForStream:withOptions:error:
- _objc_msgSend$deactivateAudioSessionWithOptions:
- _objc_msgSend$debugDescription
- _objc_msgSend$defaultContext
- _objc_msgSend$deviceUIDMapTable
- _objc_msgSend$didPlayEndpointBeep
- _objc_msgSend$disableBoostForDoAP
- _objc_msgSend$enableSmartRoutingConsiderationForStream:enable:
- _objc_msgSend$enableSmartRoutingConsiderationForStream:enable:error:
- _objc_msgSend$encoderBitRate
- _objc_msgSend$endAnnounceMessageException:reason:
- _objc_msgSend$endAudioAndFetchAnyTrailingZerosPacket:
- _objc_msgSend$endpointType
- _objc_msgSend$errorAlertBehavior
- _objc_msgSend$estimatedStartHostTime
- _objc_msgSend$fetchDeviceUUIDStringFromUID:
- _objc_msgSend$fetchGibraltarVoiceTriggerInfoWithRecordDeviceIndicator:
- _objc_msgSend$filterZerosInAudioPacket:atBufferHostTime:filteredPacket:
- _objc_msgSend$gainCompensatedChunk
- _objc_msgSend$getAsset:
- _objc_msgSend$getAveragePowerForStream:forChannel:
- _objc_msgSend$getBTDeviceInfoWithBTAddressString:withCompletion:
- _objc_msgSend$getBTLocalDeviceWithCompletion:
- _objc_msgSend$getCurrentSessionState
- _objc_msgSend$getCurrentStreamState:
- _objc_msgSend$getDeviceLatenciesForStream:withCompletion:
- _objc_msgSend$getFirstAudioSampleSensorHostTimeWithReply:
- _objc_msgSend$getHostClockFrequency
- _objc_msgSend$getMachTimeAdjustedVoiceTriggerEventInfoForDeviceUUID:
- _objc_msgSend$getPeakPowerForStream:forChannel:
- _objc_msgSend$getPlaybackRouteForStream:withError:
- _objc_msgSend$getRecordDeviceInfoForStream:
- _objc_msgSend$getRecordSettingsForStream:
- _objc_msgSend$handleCarCapabilitiesUpdatedWithCompletion:
- _objc_msgSend$handleHeadUnitConnectedWithAsyncCompletion:
- _objc_msgSend$hasConnected
- _objc_msgSend$hasEnded
- _objc_msgSend$hasPendingTwoShotBeep
- _objc_msgSend$historicalBufferRequestStreams
- _objc_msgSend$holdRequest
- _objc_msgSend$identifier
- _objc_msgSend$initFileURLWithPath:isDirectory:
- _objc_msgSend$initTandemWithOption:
- _objc_msgSend$initTandemWithRequest:
- _objc_msgSend$initWithAVVCRecordDeviceInfo:
- _objc_msgSend$initWithAssetSet:queue:updateHandler:
- _objc_msgSend$initWithAssetSet:usages:
- _objc_msgSend$initWithAudioDeviceID:
- _objc_msgSend$initWithAudioStreamHandleId:audioStreamType:audioRecordContext:audioRecorder:phoneCallStateMonitor:
- _objc_msgSend$initWithBackingStoreCapacity:minimalNumberOfBackingStores:maximumNumberOfBackingStores:backingStoreIdleTimeout:
- _objc_msgSend$initWithBool:
- _objc_msgSend$initWithClientIdentity:
- _objc_msgSend$initWithConfiguration:
- _objc_msgSend$initWithDeviceId:audioStreamHandleId:
- _objc_msgSend$initWithDouble:
- _objc_msgSend$initWithDuckOthers:duckToLevel:mixWithOthers:
- _objc_msgSend$initWithError:
- _objc_msgSend$initWithLongLong:
- _objc_msgSend$initWithMode:deviceUID:
- _objc_msgSend$initWithName:clientIdentity:
- _objc_msgSend$initWithName:clientQueue:
- _objc_msgSend$initWithRecordContext:deviceId:shouldUseRemoteRecorder:streamHandleId:
- _objc_msgSend$initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:
- _objc_msgSend$initWithSampleRate:withNumberOfChannels:
- _objc_msgSend$initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:
- _objc_msgSend$initWithStreamID:
- _objc_msgSend$initWithStreamID:atStartHostTime:
- _objc_msgSend$initWithStreamID:settings:bufferDuration:
- _objc_msgSend$initWithUnsignedLongLong:
- _objc_msgSend$initWithZeroWindowSize:approxAbsSpeechThreshold:numHostTicksPerAudioSample:
- _objc_msgSend$inputRecordingDuration
- _objc_msgSend$inputRecordingDurationInSecsExtended
- _objc_msgSend$internalUserClassification
- _objc_msgSend$isCarPlayConnected
- _objc_msgSend$isDuckingSupportedOnCurrentRouteWithStreamHandleID:error:
- _objc_msgSend$isDuckingSupportedOnPickedRouteForStream:error:
- _objc_msgSend$isEqualToNumber:
- _objc_msgSend$isHeadphoneDeviceWithRecordRoute:playbackRoute:
- _objc_msgSend$isNarrowBandWithStreamHandleId:
- _objc_msgSend$isOnHold
- _objc_msgSend$isOutgoing
- _objc_msgSend$isRecordContextAutoPrompt:
- _objc_msgSend$isRecordContextBuiltInVoiceTrigger:
- _objc_msgSend$isRecordContextDarwinVoiceTrigger:
- _objc_msgSend$isRecordContextHearstDoubleTap:
- _objc_msgSend$isRecordContextHearstVoiceTrigger:
- _objc_msgSend$isRecordContextJarvisVoiceTrigger:
- _objc_msgSend$isRecordContextRaiseToSpeak:
- _objc_msgSend$isRecordContextRemoraVoiceTrigger:
- _objc_msgSend$isRecordContextVoiceTrigger:
- _objc_msgSend$isRecordingWithRecordDeviceIndicator:
- _objc_msgSend$isRemoteDarwinConnectedWithUUID:
- _objc_msgSend$isRemoteDevice
- _objc_msgSend$isRemoteDeviceDarwin
- _objc_msgSend$isRemoteDeviceGibraltar
- _objc_msgSend$isSessionCurrentlyActivated
- _objc_msgSend$isSystemProvider
- _objc_msgSend$isTemporaryPairedNotInContacts
- _objc_msgSend$isUpsamplingSourceAudio
- _objc_msgSend$isVoiceTriggerInfoAvailableLocally:
- _objc_msgSend$isWeakStream
- _objc_msgSend$languageCodeDarwin
- _objc_msgSend$lastForwardedSampleCount
- _objc_msgSend$listeningMicIndicatorLockUUIDString
- _objc_msgSend$listeningMicIndicatorLocks
- _objc_msgSend$logCoreSpeechPreprocessorCompletedWithMHUUID:withMetricsDictionary:
- _objc_msgSend$lpcmBitDepth
- _objc_msgSend$lpcmIsFloat
- _objc_msgSend$metrics
- _objc_msgSend$mmapModelWithConfig:mappedSizeOut:
- _objc_msgSend$needsBoost12dB
- _objc_msgSend$notifyActiveStreamsChanged:streamHolders:streamId:
- _objc_msgSend$numInputChannels
- _objc_msgSend$numberOfChannels
- _objc_msgSend$objCType
- _objc_msgSend$orderedSet
- _objc_msgSend$outputs
- _objc_msgSend$packetDescriptionCount
- _objc_msgSend$packetDescriptions
- _objc_msgSend$peakPowerForChannel:
- _objc_msgSend$pendingStartCompletions
- _objc_msgSend$pendingStopCompletions
- _objc_msgSend$persistentDomainForName:
- _objc_msgSend$pickableRoutesDidChange:
- _objc_msgSend$playAlertSoundForType:overrideMode:
- _objc_msgSend$playAlertSoundForType:recordDevideIndicator:
- _objc_msgSend$playRecordStartingAlertAndResetEndpointerFromStream:withAlertOverride:
- _objc_msgSend$potentiallyAddHWLatencyToOption:streamHandle:voiceController:
- _objc_msgSend$powerWithNumFalseWakeup:withDuration:withPhraseDict:
- _objc_msgSend$predictStartAlertBehaviorFor:avSystemController:hasAOP:supportVibrator:isiOS:isWatchOS:isHorseman:isBridgeOS:recordRoute:playbackRoute:
- _objc_msgSend$predictStartAlertBehaviorFor:recordRoute:playbackRoute:
- _objc_msgSend$preferredExternalRouteDidChange:
- _objc_msgSend$prepareAudioStream:request:completion:
- _objc_msgSend$prepareAudioStreamRecord:recordDeviceIndicator:error:
- _objc_msgSend$prepareAudioStreamSync:request:error:
- _objc_msgSend$prepareRecordForStream:error:
- _objc_msgSend$prepareRecording:
- _objc_msgSend$prewarmAudioSessionWithStreamHandleId:error:
- _objc_msgSend$primaryStream
- _objc_msgSend$processBuffer:atTime:arrivalTimestampToAudioRecorder:
- _objc_msgSend$provider
- _objc_msgSend$providerDelegate
- _objc_msgSend$providerIdentifier
- _objc_msgSend$providerManager
- _objc_msgSend$providerWithIdentifier:
- _objc_msgSend$purgeCachedIrForTrialAssetExcludingCurrentAsset:cachedIrDir:
- _objc_msgSend$readMilFilePathFromConfig:
- _objc_msgSend$recordDeviceIndicator
- _objc_msgSend$recordModeLockUUIDString
- _objc_msgSend$recordModeLocks
- _objc_msgSend$recordQueue
- _objc_msgSend$recordRouteWithRecordDeviceIndicator:
- _objc_msgSend$recordSettingsWithStreamHandleId:
- _objc_msgSend$recordingSampleRateWithStreamHandleId:
- _objc_msgSend$remoteDeviceProductIdentifier
- _objc_msgSend$remoteProductIdentifier
- _objc_msgSend$remoteRecordConnectionDisconnected:
- _objc_msgSend$remoteRecordDidStartRecordingWithStreamHandleId:error:
- _objc_msgSend$remoteRecordDidStopRecordingWithWithStreamHandleId:error:
- _objc_msgSend$remoteRecordLPCMBufferAvailable:streamHandleId:
- _objc_msgSend$remoteRecordTwoShotDetectedAtTime:
- _objc_msgSend$remoteVoiceActivityAvailable
- _objc_msgSend$remoteVoiceActivityVAD
- _objc_msgSend$remoteVoiceActivityVADBuffer
- _objc_msgSend$reportMetricsForSiriRequestWithUUID:
- _objc_msgSend$requestForLpcmRecordSettingsWithContext:
- _objc_msgSend$requestHistoricalAudioDataSampleCount
- _objc_msgSend$requestListeningMicIndicatorLock
- _objc_msgSend$requestRecordModeLock
- _objc_msgSend$requireListeningMicIndicatorLock
- _objc_msgSend$requireRecordModeLock
- _objc_msgSend$requireSingleChannelLookup
- _objc_msgSend$resetDuckSettings
- _objc_msgSend$resetWithSampleRate:
- _objc_msgSend$routeIsDoAPSupportedWithRouteUID:withCompletion:
- _objc_msgSend$sampleCountFromHostTime:anchorHostTime:anchorSampleCount:sampleRate:
- _objc_msgSend$scheduledFutureSample
- _objc_msgSend$selectedChannel
- _objc_msgSend$sessionDelegate
- _objc_msgSend$setActivationMode:
- _objc_msgSend$setAlertDelegate:
- _objc_msgSend$setAlertSoundFromURL:forType:
- _objc_msgSend$setAllowMixableAudioWhileRecording:error:
- _objc_msgSend$setAnnounceCallsEnabled:
- _objc_msgSend$setAnnounceCallsEnabledForStream:enable:
- _objc_msgSend$setAvgPower:
- _objc_msgSend$setBnnsIrForCacheMap:withMilFile:
- _objc_msgSend$setCircularBufferStartHostTime:
- _objc_msgSend$setCircularBufferStartSampleCount:
- _objc_msgSend$setContext:streamType:error:
- _objc_msgSend$setContextForStream:forStream:error:
- _objc_msgSend$setCurrentContext:streamHandleId:error:
- _objc_msgSend$setDeviceIdentifier:
- _objc_msgSend$setDuckMixWithOthersForStream:duckOthers:duckToLevelInDB:mixWithOthers:
- _objc_msgSend$setDuckOthersForStream:withSettings:error:
- _objc_msgSend$setDuckOverride:
- _objc_msgSend$setDuckToLevelDB:error:
- _objc_msgSend$setEndpointMode:
- _objc_msgSend$setHasNonVoiceTriggerStreamsActive:
- _objc_msgSend$setIAmTheAssistant:error:
- _objc_msgSend$setIsBlur:
- _objc_msgSend$setIsTemporaryPairedNotInContacts:
- _objc_msgSend$setListeningMicIndicatorLockUUIDString:
- _objc_msgSend$setListeningMicIndicatorProperty
- _objc_msgSend$setMXSessionProperty:value:error:
- _objc_msgSend$setNeedsBoost12dB:
- _objc_msgSend$setPeakPower:
- _objc_msgSend$setPrimaryStream:
- _objc_msgSend$setProviderDelegate:
- _objc_msgSend$setQueue:
- _objc_msgSend$setRecordDelegate:
- _objc_msgSend$setRecordMode:streamHandleId:error:
- _objc_msgSend$setRecordModeForStream:recordMode:error:
- _objc_msgSend$setRecordModeLockUUIDString:
- _objc_msgSend$setScheduledFutureSample:
- _objc_msgSend$setServerCrashedBlock:
- _objc_msgSend$setServerResetBlock:
- _objc_msgSend$setSessionDelegate:
- _objc_msgSend$setSkipAlert:
- _objc_msgSend$setSplitterEnabled:
- _objc_msgSend$setStartAlert:
- _objc_msgSend$setStartStreamOption:
- _objc_msgSend$setStopAlert:
- _objc_msgSend$setStopOnErrorAlert:
- _objc_msgSend$setStreamRequest:
- _objc_msgSend$setStreamState:
- _objc_msgSend$setStreaming:
- _objc_msgSend$setStreamingUUID:
- _objc_msgSend$setSupportDoAP:
- _objc_msgSend$setSupportMph:
- _objc_msgSend$setUpsampler:
- _objc_msgSend$shouldUseRemoteRecorder
- _objc_msgSend$skipAlert
- _objc_msgSend$skipAlertBehavior
- _objc_msgSend$standardUserDefaults
- _objc_msgSend$startAlert
- _objc_msgSend$startAlertBehavior
- _objc_msgSend$startAudioStream:option:completion:
- _objc_msgSend$startAudioStreamWithOption:recordDeviceIndicator:error:
- _objc_msgSend$startHostTime
- _objc_msgSend$startPendingOnStoppingStreamToCompletionDict
- _objc_msgSend$startPendingOnStoppingStreams
- _objc_msgSend$startPendingStreams
- _objc_msgSend$startRecordForStream:error:
- _objc_msgSend$startRecording
- _objc_msgSend$startRecordingWithOptions:error:
- _objc_msgSend$startStreamOption
- _objc_msgSend$stopAlert
- _objc_msgSend$stopAlertBehavior
- _objc_msgSend$stopAudioStream:option:completion:
- _objc_msgSend$stopAudioStreamWithRecordDeviceIndicator:error:
- _objc_msgSend$stopOnErrorAlert
- _objc_msgSend$stopPendingStreams
- _objc_msgSend$stopRecordForStream:error:
- _objc_msgSend$stopRecording:
- _objc_msgSend$streamDescription
- _objc_msgSend$streamHandleQueue
- _objc_msgSend$streamHolders
- _objc_msgSend$streamID
- _objc_msgSend$streamRequest
- _objc_msgSend$streamState
- _objc_msgSend$streaming
- _objc_msgSend$streamingUUID
- _objc_msgSend$streams
- _objc_msgSend$submitRemoteCoreSpeechIssueReport:context:
- _objc_msgSend$supportBeepCanceller:
- _objc_msgSend$supportDoAP
- _objc_msgSend$supportRelayCall
- _objc_msgSend$tandemStreams
- _objc_msgSend$teardownWithError:
- _objc_msgSend$timeout
- _objc_msgSend$triggerNotifiedMachTime
- _objc_msgSend$updateAudioStreamStartTimeInSampleCount:
- _objc_msgSend$updateDeviceId:
- _objc_msgSend$updateMeterForStream:
- _objc_msgSend$updateMeters
- _objc_msgSend$updateWithLatestRecordContext:
- _objc_msgSend$upsampler
- _objc_msgSend$useCustomizedRecordSettings
- _objc_msgSend$useOpportunisticZLL
- _objc_msgSend$voiceTriggerEnabledDevices
- _objc_msgSend$waitingForConnection:error:
- _objc_msgSend$willBeep
- _objc_msgSend$willBeepWithRecordRoute:playbackRoute:
- _objc_msgSend$willDestroy
- _objc_msgSend$withElapsedTimeLogging:execute:
- _objc_msgSend$zeroFilter
- _objc_msgSend$zeroFilter:zeroFilteredBufferAvailable:atHostTime:
- _objc_msgSend$zeroFilterApproxAbsSpeechThreshold
- _objc_msgSend$zeroFilterWindowSizeInMs
- _remote_device_copy_device_with_uuid
- _remote_device_copy_property
- _remote_device_copy_unique_of_type
- _setCachedAsset:.onceToken
- _setCachedAsset:.overrideAsset
- _sharedAggregator.onceToken
- _sharedAggregator.sharedAggregator
- _sharedController.onceToken.12595
- _sharedController.sharedController.12597
- _sharedHandler.onceToken.1506
- _sharedHandler.onceToken.21833
- _sharedHandler.onceToken.31927
- _sharedHandler.onceToken.7278
- _sharedHandler.sharedHandler.1508
- _sharedHandler.sharedHandler.21835
- _sharedHandler.sharedHandler.31929
- _sharedHandler.sharedHandler.7280
- _sharedInstance._sharedInstance.1131
- _sharedInstance._sharedInstance.1191
- _sharedInstance._sharedInstance.12403
- _sharedInstance._sharedInstance.1259
- _sharedInstance._sharedInstance.13754
- _sharedInstance._sharedInstance.15493
- _sharedInstance._sharedInstance.15676
- _sharedInstance._sharedInstance.17384
- _sharedInstance._sharedInstance.18286
- _sharedInstance._sharedInstance.18600
- _sharedInstance._sharedInstance.18888
- _sharedInstance._sharedInstance.18964
- _sharedInstance._sharedInstance.19160
- _sharedInstance._sharedInstance.20131
- _sharedInstance._sharedInstance.20408
- _sharedInstance._sharedInstance.22302
- _sharedInstance._sharedInstance.22952
- _sharedInstance._sharedInstance.23069
- _sharedInstance._sharedInstance.23307
- _sharedInstance._sharedInstance.24032
- _sharedInstance._sharedInstance.24559
- _sharedInstance._sharedInstance.2723
- _sharedInstance._sharedInstance.28540
- _sharedInstance._sharedInstance.28594
- _sharedInstance._sharedInstance.29484
- _sharedInstance._sharedInstance.31502
- _sharedInstance._sharedInstance.31686
- _sharedInstance._sharedInstance.31723
- _sharedInstance._sharedInstance.32274
- _sharedInstance._sharedInstance.34094
- _sharedInstance._sharedInstance.34179
- _sharedInstance._sharedInstance.3503
- _sharedInstance._sharedInstance.3582
- _sharedInstance._sharedInstance.3724
- _sharedInstance._sharedInstance.4016
- _sharedInstance._sharedInstance.6683
- _sharedInstance._sharedInstance.6793
- _sharedInstance._sharedInstance.6891
- _sharedInstance._sharedInstance.7172
- _sharedInstance._sharedInstance.7770
- _sharedInstance._sharedInstance.9724
- _sharedInstance._sharedInstance.9931
- _sharedInstance.monitor
- _sharedInstance.onceToken.1052
- _sharedInstance.onceToken.11191
- _sharedInstance.onceToken.1129
- _sharedInstance.onceToken.11453
- _sharedInstance.onceToken.11608
- _sharedInstance.onceToken.1189
- _sharedInstance.onceToken.124
- _sharedInstance.onceToken.12401
- _sharedInstance.onceToken.1257
- _sharedInstance.onceToken.12962
- _sharedInstance.onceToken.13588
- _sharedInstance.onceToken.13716
- _sharedInstance.onceToken.13752
- _sharedInstance.onceToken.14249
- _sharedInstance.onceToken.15491
- _sharedInstance.onceToken.15674
- _sharedInstance.onceToken.16355
- _sharedInstance.onceToken.16440
- _sharedInstance.onceToken.1656
- _sharedInstance.onceToken.16926
- _sharedInstance.onceToken.17382
- _sharedInstance.onceToken.1758
- _sharedInstance.onceToken.18284
- _sharedInstance.onceToken.18598
- _sharedInstance.onceToken.18886
- _sharedInstance.onceToken.18962
- _sharedInstance.onceToken.19059
- _sharedInstance.onceToken.19158
- _sharedInstance.onceToken.20129
- _sharedInstance.onceToken.20176
- _sharedInstance.onceToken.20406
- _sharedInstance.onceToken.20436
- _sharedInstance.onceToken.22169
- _sharedInstance.onceToken.22251
- _sharedInstance.onceToken.22300
- _sharedInstance.onceToken.22661
- _sharedInstance.onceToken.22950
- _sharedInstance.onceToken.23067
- _sharedInstance.onceToken.23305
- _sharedInstance.onceToken.23773
- _sharedInstance.onceToken.24030
- _sharedInstance.onceToken.24502
- _sharedInstance.onceToken.24557
- _sharedInstance.onceToken.251
- _sharedInstance.onceToken.25429
- _sharedInstance.onceToken.25549
- _sharedInstance.onceToken.25624
- _sharedInstance.onceToken.25736
- _sharedInstance.onceToken.25773
- _sharedInstance.onceToken.25884
- _sharedInstance.onceToken.2721
- _sharedInstance.onceToken.27303
- _sharedInstance.onceToken.27473
- _sharedInstance.onceToken.27963
- _sharedInstance.onceToken.28538
- _sharedInstance.onceToken.28951
- _sharedInstance.onceToken.29160
- _sharedInstance.onceToken.2926
- _sharedInstance.onceToken.29482
- _sharedInstance.onceToken.31225
- _sharedInstance.onceToken.31500
- _sharedInstance.onceToken.31684
- _sharedInstance.onceToken.31721
- _sharedInstance.onceToken.31760
- _sharedInstance.onceToken.32272
- _sharedInstance.onceToken.32347
- _sharedInstance.onceToken.32633
- _sharedInstance.onceToken.3290
- _sharedInstance.onceToken.33239
- _sharedInstance.onceToken.33898
- _sharedInstance.onceToken.34092
- _sharedInstance.onceToken.34177
- _sharedInstance.onceToken.3501
- _sharedInstance.onceToken.3520
- _sharedInstance.onceToken.3580
- _sharedInstance.onceToken.363
- _sharedInstance.onceToken.3672
- _sharedInstance.onceToken.3722
- _sharedInstance.onceToken.4014
- _sharedInstance.onceToken.4461
- _sharedInstance.onceToken.668
- _sharedInstance.onceToken.6681
- _sharedInstance.onceToken.6791
- _sharedInstance.onceToken.6889
- _sharedInstance.onceToken.7170
- _sharedInstance.onceToken.7768
- _sharedInstance.onceToken.840
- _sharedInstance.onceToken.94
- _sharedInstance.onceToken.9722
- _sharedInstance.onceToken.9929
- _sharedInstance.sSharedInstance.20438
- _sharedInstance.sharedInfo
- _sharedInstance.sharedInstance.1054
- _sharedInstance.sharedInstance.12964
- _sharedInstance.sharedInstance.13590
- _sharedInstance.sharedInstance.13718
- _sharedInstance.sharedInstance.14251
- _sharedInstance.sharedInstance.16442
- _sharedInstance.sharedInstance.20178
- _sharedInstance.sharedInstance.22171
- _sharedInstance.sharedInstance.22253
- _sharedInstance.sharedInstance.23775
- _sharedInstance.sharedInstance.24504
- _sharedInstance.sharedInstance.25431
- _sharedInstance.sharedInstance.25626
- _sharedInstance.sharedInstance.25738
- _sharedInstance.sharedInstance.25775
- _sharedInstance.sharedInstance.27475
- _sharedInstance.sharedInstance.27965
- _sharedInstance.sharedInstance.29162
- _sharedInstance.sharedInstance.2928
- _sharedInstance.sharedInstance.31762
- _sharedInstance.sharedInstance.32349
- _sharedInstance.sharedInstance.3292
- _sharedInstance.sharedInstance.33900
- _sharedInstance.sharedInstance.4463
- _sharedInstance.sharedInstance.670
- _sharedInstance.sharedInstance.842
- _sharedInstance.sharedManager.22663
- _sharedInstance.sharedManager.25886
- _sharedInstance.sharedManager.31227
- _sharedInstance.sharedPolicy.1658
- _sharedInstance.sharedPolicy.25551
- _sharedInstance.sharedPolicy.28953
- _sharedInstance.sharedProvider.27305
- _sharedInstance.singleton
- _sharedManager.onceToken.18462
- _sharedManager.onceToken.21315
- _sharedManager.onceToken.8033
- _sharedManager.sharedManager.18464
- _sharedManager.sharedManager.8035
- _sharedMonitor.onceToken.23215
- _sharedMonitor.sharedMonitor.23217
- _sharedPreferences.onceToken.29057
- _sharedPreferences.sharedPreferences
- _sharedService.onceToken.17065
- _sharedService.onceToken.30870
- _sharedService.sharedService.30872
- _sharedSession.onceToken
- _sharedSession.sSession
- _uuid_is_null
- _uuid_parse
- _voiceControllerAudioCallback:forStream:buffer:.heartbeat
- _xpc_array_apply
- _xpc_array_create
- _xpc_bool_get_value
- _xpc_copy_clean_description
- _xpc_data_create
- _xpc_data_get_bytes_ptr
- _xpc_data_get_length
- _xpc_double_get_value
- _xpc_int64_get_value
- _xpc_string_get_string_ptr
- _xpc_uint64_get_value
CStrings:
+ "%s CS set AVAudioSession category/options failed with error: %@"
+ "%s Compile override Mitigation asset to onDevice CacheIr with error: %@"
+ "%s Connection invalidated"
+ "%s Could not find AssetMeta for current locale: %@, preinstalledAssetMeta: %@. No mitigation functionality"
+ "%s Could not fstat() BNNSIR: %s"
+ "%s Could not read OPEN() BNNSIR: %s"
+ "%s Detected 2nd-pass trigger at %{public}llu"
+ "%s Does not support model type: %lu"
+ "%s FirstPass detected VoiceTrigger at exclaveSampleCount = %llu"
+ "%s IVoiceTrigger on hearst cannot be turned on since Siri client is currently in an outgoing call"
+ "%s Ignore %{public}@ since voice trigger enabled policy returned NO"
+ "%s Incoming Major version:%@, Incoming Minor version:%@"
+ "%s Invalid bnnsIr removal error: %@"
+ "%s Invalidating Connection %p"
+ "%s Not reporting EPD due to unexpected zero or negative component values: _stopRecordingHostTime: %{public}llu, _userSpeakingEndedHostTime: %{public}llu, _userSpeakingEndedTimeInMs: %{public}f, _endpointTimeInMs: %{public}f"
+ "%s One or more EPD values are negative: EPD: %f, EPD_Model: %f, EPD_Latency: %f"
+ "%s Preinstalled model meta not found: %{public}@. No mitigation functionality."
+ "%s RTS triggered with nil voicetrigger info. Falling back to CVT pending two shot detection"
+ "%s Remote object proxy %p"
+ "%s Remote object proxy is nil"
+ "%s Reset first-pass VoiceTrigger in Exclave"
+ "%s Setting default enhanced endpointer model to %{public}@ for task %{public}@, with defaultThresholdPartial: %{public}f, defaultThresholdRC: %{public}f, relaxedThresholdPartial: %{public}f, relaxedThresholdRC: %{public}f, extraDelayMs: %{public}d"
+ "%s Starting pending two shot detection"
+ "%s The first pass source is not from AP, skip handling!"
+ "%s UAFDownloadMonitor stop monitoring"
+ "%s VoiceTrigger on hearst cannot be turned on Siri client is current listening"
+ "%s VoiceTrigger on hearst cannot be turned on since Siri client is currently in a connected call"
+ "%s VoiceTrigger on hearst cannot be turned on since Siri client is currently in a ringtone and does not support A2DP"
+ "%s VoiceTrigger on hearst cannot be turned on since Siri is restricted on lock screen"
+ "%s VoiceTrigger on hearst cannot be turned on since VoiceTrigger is disabled"
+ "%s VoiceTrigger on hearst cannot be turned on since phrases spotter is disabled"
+ "%s VoiceTrigger on hearst cannot be turned on since there is an other non eligible app recording"
+ "%s _activeEndpointer: %@ should only be set to one of _hybridEndpointer: %@, _nnvadEndpointer: %@, or nil"
+ "%s activationMode = %ld, usesDeviceSpeakerForTTS = %lu, attemptsToUsePastDataBufferFrames = %d, isDeviceInCarDNDMode = %d"
+ "%s can't open bnnsIr: %@, recompiling to a new bnnsir file"
+ "%s failed to instantiate deviceInput - bailing!"
+ "%s isSupported=%@: Is request during active call? %@, isDeviceSupported: %@, isSupportedRequestType: %@, isFFUserDisabled: %@, isTypeToSiriEnabled: %@, isLocaleInDenyList:%@"
+ "%s model compilation finished with error %@: "
+ "%s model init error: %@"
+ "%s progCheckerReocgnizerConfigFiles: %@"
+ "%s received notification to purge mitigation asset with endPoint id: %@"
+ "%s received notification to purge voice trigger asset with endPoint id: %@"
+ "%s recordRoute = %@, playbackRoute = %@, speechEvent = %lu, speechRecordingMode = %lu, AFDeviceRingerSwitchState = %@, AFSoundID = %@, AFPresentationMode = %lu, usePrelistening = %d, isOnPhoneCall = %d, hasPlayedStartAlert = %d, supportsEchoCancellation = %d, isVoiceOverTouchEnabled = %d, isVibrationEnabled = %d, isVibrationSupported = %d, suppressStartAlert = %d, activationHostTime = %llu"
+ "+[CSAsset(RTModel) supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:]"
+ "+[CSCoreSpeechServices supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]"
+ "+[CSCoreSpeechServices supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]_block_invoke"
+ "+[CSCoreSpeechServices supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]_block_invoke_2"
+ "+[CSMil2BnnsUtils _compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:compilationFramework:error:]"
+ "+[CSMil2BnnsUtils _isBnnsIrReadable:]"
+ "+[CSMil2BnnsUtils compileModelWithMilFile:bnnsIrCachePath:compilationFramework:]"
+ "+[CSMil2BnnsUtils mmapModelWithConfig:mappedSizeOut:modelType:]"
+ "+[CSOnDeviceCompilationUtils getModelCompiledDirWithModelType:basePath:]"
+ "+[CSOnDeviceCompilationUtils getModelConfigsWithAsset:modelType:]"
+ "+[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]"
+ "-[CSAttSiriMitigationAssetHandler _getPreinstalledMitigationAssetForCurrentLocale:]"
+ "-[CSAttSiriMitigationAssetHandler setCachedAssetWithOverride:]"
+ "-[CSAudioInjectionProvider activateAudioSessionWithReason:streamHandleId:error:]"
+ "-[CSBuiltInVoiceTrigger _reportVoiceTriggerFirstPassFireFromAPWithSource:voiceTriggerFirstPassInfo:]"
+ "-[CSBuiltInVoiceTrigger _resetFirstExclaveAudioBufferMarkerIfNeeded]"
+ "-[CSBuiltInVoiceTrigger _shouldSkipAudioChunkHandling]"
+ "-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke"
+ "-[CSContinuousVoiceTrigger _startDetectTwoShot:]"
+ "-[CSEndpointerProxy _setActiveEndpointer:]"
+ "-[CSModelBenchmarker _onDeviceCompilationWithConfigFile:locale:modelType:]"
+ "-[CSModelBenchmarker runNCModelWithConfig:completion:]"
+ "-[CSOnDeviceCachedIrPurgingHandler _purgeCachedIrExceptActiveCachedIrs:cachedIrDir:]"
+ "-[CSOnDeviceCachedIrPurgingHandler _purgeCachedIrFilesWithAsset:]"
+ "-[CSOnDeviceCachedIrPurgingHandler mitigationAssetHandler:endpointId:didChangeCachedAsset:]"
+ "-[CSOnDeviceCachedIrPurgingHandler purgeCachedIrForTrialAssetExcludingCurrentAsset:baseCachedIrDir:]"
+ "-[CSOnDeviceCompilationHandler _compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:modelType:compilationFramework:]"
+ "-[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:modelType:deviceId:currentLocale:compileDirectory:errOut:]_block_invoke"
+ "-[CSOnDeviceCompilationHandler compileUsingConfig:locale:compileDirectory:modelType:errOut:]_block_invoke"
+ "-[CSSpeechController _audioStreamProvider:audioBufferAvailable:]"
+ "-[CSUAFDownloadMonitor _stopMonitoring]"
+ "-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke"
+ "-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:]"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]"
+ "-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke"
+ "-[CoreSpeechXPC supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:]"
+ "/PreinstalledAssets/preinstalledMeta.json"
+ ";"
+ "@\"CSExclaveRecordClient\""
+ "@\"CSFAudioDeviceInfo\""
+ "@\"CSFAudioDeviceInfo\"16@0:8"
+ "@\"CSFAudioRecordDeviceInfo\""
+ "@\"CSFAudioRecordDeviceInfo\"16@0:8"
+ "@\"CSScreenLockMonitor\""
+ "@\"CSSiriRestrictionOnLockScreenMonitor\""
+ "@\"CSVoiceTriggerHearstEnabledPolicy\""
+ "@112@0:8@16@24q32q40q48q56q64B72B76B80B84B88B92B96B100Q104"
+ "@40@0:8@16@24q32"
+ "@48@0:8@16q24@32@40"
+ "@64@0:8@16@24@32@40B48@52B60"
+ "@64@0:8Q16Q24Q32Q40Q48Q56"
+ "@72@0:8@16@24@32@40@48q56q64"
+ "CSFExclaveAudioAvailability"
+ "CSTempModel"
+ "CSVoiceTriggerHearstEnabledPolicy"
+ "EPD"
+ "EPD_Latency"
+ "EPD_Model"
+ "F\x12A\x14\x14\x14#!\x12"
+ "Q\x1b\xc1\x81\x12\x18A"
+ "SFEntitledAssetDelegate"
+ "SecondPassChecker"
+ "T@\"<CSAttendingServiceDelegate>\",?,W,N"
+ "T@\"<CSAttendingServiceDelegate>\",?,W,N,V_delegate"
+ "T@\"CSExclaveRecordClient\",&,N,V_exclaveClient"
+ "T@\"CSFAudioDeviceInfo\",&,N,V_audioDeviceInfo"
+ "T@\"CSFAudioRecordDeviceInfo\",R,N,V_deviceInfo"
+ "T@\"CSOtherAppRecordingStateMonitor\",R,N,V_otherAppRecordingStateMonitor"
+ "T@\"CSPhoneCallStateMonitor\",R,N,V_phonecallStateMonitor"
+ "T@\"CSScreenLockMonitor\",R,N,V_screenLockMonitor"
+ "T@\"CSSiriClientBehaviorMonitor\",R,N,V_siriClientBehaviorMonitor"
+ "T@\"CSSiriRestrictionOnLockScreenMonitor\",R,N,V_siriRestrictionOnLockScreenMonitor"
+ "T@\"CSVoiceTriggerEnabledMonitor\",R,N,V_voiceTriggerEnabledMonitor"
+ "T@\"CSVoiceTriggerHearstEnabledPolicy\",&,N,V_voicetriggerHearstEnabledPolicy"
+ "T@\"NSString\",?,&,N"
+ "T@\"NSString\",?,&,N,V_mhId"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,N"
+ "TB,?,N"
+ "TB,?,N,V_saveSamplesSeenInReset"
+ "TB,N,V_isFirstExclaveAudioBuffer"
+ "TB,N,V_pendingTwoShotDetection"
+ "TQ,N,V_lastUsedAnalyzerType"
+ "TQ,R,N,V_arrivalHostTimeToAudioRecorder"
+ "TQ,R,N,V_hostTime"
+ "TQ,R,N,V_numChannels"
+ "TQ,R,N,V_numSamples"
+ "TQ,R,N,V_sampleByteDepth"
+ "Td,?,N"
+ "Td,?,N,V_endWaitTime"
+ "Td,?,N,V_interspeechWaitTime"
+ "Td,?,R,N"
+ "Unrecognizer compilation backend"
+ "^v40@0:8@16^@24q32"
+ "_alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:"
+ "_arrivalHostTimeToAudioRecorder"
+ "_audioStreamProvider:audioBufferAvailable:"
+ "_compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:modelType:compilationFramework:"
+ "_compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:compilationFramework:error:"
+ "_exclaveClient"
+ "_getCachedIrsFromConfigFile:modelType:CSAsset:cachedIrDir:"
+ "_getPreinstalledMitigationAssetForCurrentLocale:"
+ "_handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:"
+ "_hostTime"
+ "_isBnnsIrReadable:"
+ "_isFirstExclaveAudioBuffer"
+ "_isFirstPassSourceExclave:"
+ "_lastUsedAnalyzerType"
+ "_notifyLanguageCodeChangeToExclaveKit"
+ "_numSamples"
+ "_observerToken"
+ "_onDeviceCompilationWithConfigFile:locale:modelType:"
+ "_pendingTwoShotDetection"
+ "_phonecallStateMonitor"
+ "_processSecondPassInExclave:"
+ "_purgeCachedIrExceptActiveCachedIrs:cachedIrDir:"
+ "_purgeCachedIrFilesWithAsset:"
+ "_reportVoiceTriggerFirstPassFireFromAPWithSource:voiceTriggerFirstPassInfo:"
+ "_resetFirstExclaveAudioBufferMarkerIfNeeded"
+ "_sampleByteDepth"
+ "_screenLockMonitor"
+ "_setActiveEndpointer:"
+ "_shouldSkipAudioChunkHandling"
+ "_siriRestrictionOnLockScreenMonitor"
+ "_startDetectTwoShot:"
+ "_syncVoiceProfileEmbeddingsToExclave"
+ "_voiceTriggerFirstPassInfoFromAP"
+ "_voicetriggerHearstEnabledPolicy"
+ "aftm"
+ "allObjects"
+ "ar8!!!R\x11"
+ "assetNamed:"
+ "audioRecorderExclaveBufferAvailable:audioStreamHandleId:hostTime:arrivalTimestampToAudioRecorder:"
+ "audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:"
+ "ay12!RS"
+ "compileAndUpdateDeviceCachesWithAsset:assetType:modelType:deviceId:currentLocale:compileDirectory:errOut:"
+ "compileModelWithMilFile:bnnsIrCachePath:compilationFramework:"
+ "compileUsingConfig:locale:compileDirectory:modelType:errOut:"
+ "compileWithMilFile:bnnsIrPath:"
+ "contConvRecognizerConfigFiles"
+ "dateWhenVoiceTriggerRePrompted"
+ "defaultNLDAValue"
+ "deviceSupportsMagus"
+ "exclaveClient"
+ "exclaveRecordingNumSamples"
+ "getAftmRecognizerConfigFromConfigDict:"
+ "getAllMitigationConfigFiles"
+ "getAllNldaConfigFiles"
+ "getBertModelFile"
+ "getConversationAwareness:"
+ "getModelCompiledDirWithModelType:basePath:"
+ "getModelConfigsWithAsset:modelType:"
+ "getModelFile"
+ "getPersonalVolume:"
+ "getRecognizerConfigsFrom:"
+ "initWithAssetManager:withUAFAssetManager:withUAFDownloadMonitor:withLanguageCodeUpdateMonitor:withAssetOverrideFlag:withOverrideAssetPath:disableOnDeviceCompilation:"
+ "initWithConfigFile:errOut:"
+ "initWithDefaultValue:completionBlock:"
+ "initWithDisableOnDeviceCompilation"
+ "initWithNumChannels:numSamples:sampleByteDepth:startSampleCount:hostTime:arrivalHostTimeToAudioRecorder:"
+ "initWithSiriRestrictionOnLockScreenMonitor:screenLockMonitor:voiceTriggerEnabledMonitor:CSPhoneCallStateMonitor:otherAppRecordingStateMonitor:siriClientBehaviorMonitor:srfUserSettingsMonitor:"
+ "initWithSpeechManager:voiceTriggerEnabledPolicyHearst:"
+ "isBlushingPhantomEnabled"
+ "isExclaveHardware"
+ "isFirstExclaveAudioBuffer"
+ "isMagusDisabledForLanguageCode:"
+ "lastUsedAnalyzerType"
+ "mitigation"
+ "mitigationModelDefaultNLDAScore"
+ "mmapModelWithConfig:mappedSizeOut:modelType:"
+ "neuralCombiner"
+ "notifyRequestCompletion"
+ "observeAssetSet:queue:handler:"
+ "odld"
+ "pathWithComponents:"
+ "pendingTwoShotDetection"
+ "phonecallStateMonitor"
+ "processBargeInVoiceTriggerWithResult:"
+ "processSecondPassVoiceTriggerWithShouldFlushAudio:result:"
+ "progCheckerRecognizerConfigFiles"
+ "purgeCachedIrForTrialAssetExcludingCurrentAsset:baseCachedIrDir:"
+ "qaaB"
+ "readMilFilePathFromConfig:modelType:"
+ "resetFirstPassVoiceTrigger"
+ "retrieveAssetSet:usages:"
+ "screenLockMonitor"
+ "setCacheMapWithMilFile:bnnsIr:"
+ "setCachedAssetWithOverride:"
+ "setCategory:withOptions:error:"
+ "setConversationAwareness:completion:"
+ "setExclaveClient:"
+ "setIsFirstExclaveAudioBuffer:"
+ "setLastUsedAnalyzerType:"
+ "setPendingTwoShotDetection:"
+ "setPersonalVolume:completion:"
+ "setRequestExclaveAudio:"
+ "setVoicetriggerHearstEnabledPolicy:"
+ "sharedClient"
+ "shouldCompileForAssetType:"
+ "siriRestrictionOnLockScreenMonitor"
+ "startBargeInVoiceTrigger"
+ "startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:"
+ "stopBargeInVoiceTrigger"
+ "stopSecondPassVoiceTrigger"
+ "submitEndpointerIssueReport:withContext:"
+ "supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:"
+ "supportsMultiPhraseVoiceTriggerForEngineVersion:engineMinorVersion:accessoryRTModelType:completion:"
+ "v16@?0@\"NSNumber\"8"
+ "v20@?0I8Q12"
+ "v24@0:8@\"CSFAudioDeviceInfo\"16"
+ "v24@0:8@?<v@?@\"AFBluetoothDeviceBooleanSettingResponse\">16"
+ "v28@0:8B16@?<v@?@\"AFBluetoothDeviceBooleanSettingResponse\">20"
+ "v40@0:8@16@24q32"
+ "v44@0:8@\"CSSpeechController\"16@\"CSFAudioDeviceInfo\"24B32@\"NSError\"36"
+ "v48@0:8@\"CSAudioRecorder\"16Q24Q32Q40"
+ "v48@0:8@\"CSSpeechController\"16@\"CSFAudioDeviceInfo\"24q32Q40"
+ "v48@0:8@\"NSNumber\"16@\"NSNumber\"24@\"NSNumber\"32@?<v@?B>40"
+ "v48@0:8@16Q24Q32Q40"
+ "v52@0:8@\"CSSpeechController\"16@\"NSArray\"24f32Q36@\"CSFAudioDeviceInfo\"44"
+ "v56@0:8@\"<CSAudioStreamProviding>\"16Q24Q32Q40Q48"
+ "v56@0:8@16@24@32q40^@48"
+ "v72@0:8@16Q24@32@40@48@56^@64"
+ "voicetriggerHearstEnabledPolicy"
- "\x01\x12"
- "\x01C5\x11"
- "\x042"
- "\x12#\x11"
- "\x15\x19#\x14\x14!\"\x12\x13"
- "%@ {recordDeviceInfo = %@, playbackRoute = %@, playbackDevices = %@"
- "%@ {route = %@, isRemoteDevice = %d, remoteDeviceUID = %@, remoteDeviceProductIdentifier = %@, remoteDeviceUIDString = %@}"
- "%@-%@"
- "%llu"
- "%s %{public}@ miniDucking now"
- "%s (darwinOS) : isNarrowBand = NO for streamHandleId = %{public}lu"
- "%s ::: CSAudioRecord will inject audio file instead of recording"
- "%s ::: Error reading file %@, err: %d"
- "%s ::: accumulated false wakeup count is %{public}llu so far, not reporting yet because it has been only %{public}.2f seconds since last report with current phrases %{public}@"
- "%s ::: incrementing false wakeup to %{public}llu"
- "%s AVVC doesn't return sampleRate, assume it is default sample rate"
- "%s AVVC getDeviceLatenciesForStream:withCompletion timed out"
- "%s AVVC initialization failed"
- "%s AVVC prepareRecordForStream failed : %{public}@"
- "%s AVVC sampling rate = %{public}f"
- "%s AVVC setRecordMode has failed : %{public}@"
- "%s AVVC setSessionActivate has failed : %{public}@"
- "%s AVVC successfully activated audioSession"
- "%s AVVC successfully setRecordMode"
- "%s AVVCAudioBuffer contains %{public}d packet descriptions, size %{public}d, channels %{public}d. Ignoring"
- "%s Accessing BTLocalDevice"
- "%s Accessory manager is not initialized"
- "%s Acquiring listening mic indicator lock from : %d %@"
- "%s Acquiring recordModeLock from : %d"
- "%s Add (%{public}@, %{public}@) pair into mapping table"
- "%s Alert behavior is either not Muted or is not Haptic with State Feedback enabled. Not adjusting latency from CS layer."
- "%s Already Attaching Bluetooth Session"
- "%s Applying adjustment for hardware latency %{public}f secs, %{public}llu ticks (AVF=%f Correction=%f)"
- "%s Asking startRecording to remote device with context : %{public}@ (original context : %{public}@)"
- "%s Attached stream %{public}@ as tandem to master stream %{public}@ %{public}@, error : %{public}@"
- "%s Audio Packet Delivery WatchDog fired, trying to recover"
- "%s Audio Streaming already stopped"
- "%s Audio record route is %{private}@ for stream id %{private}lu"
- "%s Audio resampling done : %lu"
- "%s AudioFilePathIndex is out-of-boundary _audioFilePathIndex:%d injectAudioFilePaths:%d"
- "%s AudioFilePathIndex:%d accessing:%@"
- "%s AudioSessionState = NO"
- "%s AudioSessionState = YES"
- "%s AudioStream<%{public}@> has received didHardwareConfigurationChange"
- "%s AudioStream<%{public}@> has received didStopStreamUnexpectedly"
- "%s AudioStream<%{public}@> is streaming : %{public}d"
- "%s BT AACP capability retrieval latency %f seconds"
- "%s BTLocalDevice %{public}p"
- "%s Bad packet length %{public}d. Skipping rest of record buffer."
- "%s Beep Canceller Metrics : %{public}@"
- "%s Bluetooth Session is NULL"
- "%s CRFetchCarPlayCapabilities returned nil"
- "%s CSAudioFileReader only support LinearPCM to feed"
- "%s CSAudioFileReader requires prepare recording settings to feed audio"
- "%s CSAudioProvider is deallocated"
- "%s CSAudioProvider[%{public}@]:"
- "%s CSAudioProvider[%{public}@]:%{public}@ ask for audio hold stream for %{public}f"
- "%s CSAudioProvider[%{public}@]:%{public}@ ask for cancel hold stream"
- "%s CSAudioProvider[%{public}@]:%{public}@ is requesting earlier audio than asked, we can't deliver earlier audio"
- "%s CSAudioProvider[%{public}@]:%{public}@ stream holder was already removed from stream holders"
- "%s CSAudioProvider[%{public}@]:AVVC is recovering, ignore command..."
- "%s CSAudioProvider[%{public}@]:Activating Audio Session under : %{public}@"
- "%s CSAudioProvider[%{public}@]:Asking AudioRecorder prepareAudioStreamRecord"
- "%s CSAudioProvider[%{public}@]:Audio Recorder Disconnected"
- "%s CSAudioProvider[%{public}@]:AudioRecorder will be destroyed"
- "%s CSAudioProvider[%{public}@]:Buffer overrun!!! lastForwardedSampleTime:%{public}lu,                                    theMostRecentSampleCount:%{public}lu, stream:%{public}@"
- "%s CSAudioProvider[%{public}@]:Buffer underrun!!!!, lastForwardedSampleTime:%{public}lu, oldestSampleTimeInBuffer:%{public}lu, stream:%{public}@"
- "%s CSAudioProvider[%{public}@]:Cannot change context since audio recorder is currently recording"
- "%s CSAudioProvider[%{public}@]:Cannot handle start audio stream on : %{public}@"
- "%s CSAudioProvider[%{public}@]:Cannot handle stop audio stream on : %{public}@"
- "%s CSAudioProvider[%{public}@]:Cannot prepare, audio system is recovering"
- "%s CSAudioProvider[%{public}@]:Cannot startAudioStream, audio system is recovering"
- "%s CSAudioProvider[%{public}@]:Cannot stopRecording as there are %{public}tu streamHolders"
- "%s CSAudioProvider[%{public}@]:Create circular buffer : numChannels(%d), duration(%f)"
- "%s CSAudioProvider[%{public}@]:Deactivating Audio Session under : %{public}@"
- "%s CSAudioProvider[%{public}@]:Entering dispatch group for recordingWillStartGroup"
- "%s CSAudioProvider[%{public}@]:Failed to fetch historical audio since _clientStartSampleCount is newer than audioBuffer sample count(%{public}llu)"
- "%s CSAudioProvider[%{public}@]:Failed to stop audioStream : %{public}@"
- "%s CSAudioProvider[%{public}@]:Ignore forwarding stream %{public}@                                        the audio packets until sampleCount == %{public}lu (theMostRecentSampleCount:%{public}lu)"
- "%s CSAudioProvider[%{public}@]:Leaving dispatch group for recordingWillStartGroup"
- "%s CSAudioProvider[%{public}@]:Prepare audio stream reuqested while state is %{public}@"
- "%s CSAudioProvider[%{public}@]:Received didStartRecording while %{public}@"
- "%s CSAudioProvider[%{public}@]:Received didStopRecording reason : %{public}d, streamState : %{public}@"
- "%s CSAudioProvider[%{public}@]:Received didStopRecording while %{public}@"
- "%s CSAudioProvider[%{public}@]:Release recording transaction at streamState : %{public}@"
- "%s CSAudioProvider[%{public}@]:Removing %{public}@ from stream holders"
- "%s CSAudioProvider[%{public}@]:Requested alertFinishHostTime = %{public}llu, _clientStartSampleCount = %{public}tu, circularBufferSampleCount = %{public}tu"
- "%s CSAudioProvider[%{public}@]:Requested startHostTime = %{public}llu, _clientStartSampleCount = %{public}tu"
- "%s CSAudioProvider[%{public}@]:Scheduled stopAudioStream after waiting for recordingWillStartGroup - stopAudioStream %{public}@ with streamState : %{public}@"
- "%s CSAudioProvider[%{public}@]:Set circularBufferStartHostTime = %{public}llu, circularBufferStartSampleCount = %{public}lu"
- "%s CSAudioProvider[%{public}@]:Setting audioRecorder : %{public}p"
- "%s CSAudioProvider[%{public}@]:Shouldn't stop AVVC recording as there are %{public}tu streams"
- "%s CSAudioProvider[%{public}@]:Skipping start alert to start recording"
- "%s CSAudioProvider[%{public}@]:Stop all recordings, moving stream state to %{public}@"
- "%s CSAudioProvider[%{public}@]:Stream %{public}@ is not streaming on stream state : %{public}@, ignore the stopAudioStream request"
- "%s CSAudioProvider[%{public}@]:StreamState changed from : %{public}@ to : %{public}@"
- "%s CSAudioProvider[%{public}@]:Timeout for %{public}@ has fired"
- "%s CSAudioProvider[%{public}@]:Waiting for recordingWillStartGroup before scheduling stopAudioStream"
- "%s CSAudioProvider[%{public}@]:audioStreamWithRequest for stream <%{public}@>"
- "%s CSAudioProvider[%{public}@]:audiomxd/bridgeaudiod crashed"
- "%s CSAudioProvider[%{public}@]:audiomxd/bridgeaudiod recovered from crash"
- "%s CSAudioProvider[%{public}@]:prepareAudioStream with stream : %{public}@ with stream state : %{public}@"
- "%s CSAudioProvider[%{public}@]:prepareAudioStreamRecord failed : %{public}@"
- "%s CSAudioProvider[%{public}@]:prepareAudioStreamSync with stream : %{public}@ with stream state : %{public}@, request : %{public}@"
- "%s CSAudioProvider[%{public}@]:recordingTransaction already released"
- "%s CSAudioProvider[%{public}@]:requested stop audio stream while stopping, adding audio stream into stop pending"
- "%s CSAudioProvider[%{public}@]:requested stop audio stream while stoppingWithScheduledStart, take out audio stream from schedule"
- "%s CSAudioProvider[%{public}@]:setCurrentContext : %{public}@"
- "%s CSAudioProvider[%{public}@]:shouldDuckOnBuiltInSpeaker: %{public}@ (audioStreamType: %{public}lu, isPlaybackRouteBuiltInSpeaker: %{public}@, isDuckingOnSpeakerOutputSupported: %{public}@)"
- "%s CSAudioProvider[%{public}@]:shouldWaitForAlertFinish:%u"
- "%s CSAudioProvider[%{public}@]:startAudioStream with stream : %{public}@ with stream state : %{public}@, option : %{public}@, streamId : %{public}llu"
- "%s CSAudioProvider[%{public}@]:state was %{public}@, prepareAudioStream first"
- "%s CSAudioRecorder %{public}p deallocated"
- "%s Caching CarPlayCapabilities dictionary: %@"
- "%s Call : [connected:%d] [onhold:%d] [hasEnd:%d] [isOutputgoing:%d]"
- "%s Call : [providerIdentifier: %@]"
- "%s Call identifier is not first party: %@"
- "%s Calling AVVC : Disable Smart Routing Consideration"
- "%s Calling AVVC : Enable Smart Routing Consideration"
- "%s Calling AVVC playAlertSoundForType to play %ld alert with override %ld"
- "%s Calling AVVC playAlertSoundsForType : %{public}ld"
- "%s Calling AVVC prepareRecordForStream(%{public}llu) : %{public}@"
- "%s Calling AVVC setContext : %@"
- "%s Calling AVVC setContextForStream : %{public}@"
- "%s Calling AVVC setDuckOthersForStream(%d) for DuckOthers/MixWithOthers"
- "%s Calling AVVC setRecordMode to mode : %{public}@"
- "%s Calling AVVC setSessionActivate for activation with streamId(%{public}lu)"
- "%s Calling AVVC setSessionActivate for deactivation : %{public}tu"
- "%s Calling AVVC setSessionActivate for deactivation for stream %d: %{public}tu"
- "%s Calling AVVC setSessionActive for Prewarm"
- "%s Calling AVVC startRecordForStream : %{public}@"
- "%s Calling AVVC stopRecordForStream"
- "%s Calling MSN begin announce message exception for %{public}@"
- "%s Calling MSN end announce message exception for %{public}@"
- "%s Calling audio session reset ducking settings"
- "%s Calling unexpected didStop for all weak streams"
- "%s Can't find corresponding deviceUID from UUID, return existing UUID instead"
- "%s Cannot ask VoiceTriggerEventInfo while connection does not exist"
- "%s Cannot ask didPlayEndpointBeep while connection does not exist"
- "%s Cannot ask hasPendingTwoShotBeep while connection does not exist"
- "%s Cannot create NSData with size 0"
- "%s Cannot create NSNumber if xpcObject is NULL"
- "%s Cannot create SampleRateConverter using AudioConverterNew : %{public}d"
- "%s Cannot create xpcObject if objcType is NULL"
- "%s Cannot create xpcObject since there is no matching type"
- "%s Cannot decode non-plist types of XPC object"
- "%s Cannot encode key into xpcobject since the key is not NSString class type"
- "%s Cannot encode non-plist types into XPC object : %{public}@"
- "%s Cannot handle TwoShotDetected message since it failed to decode xpcObject to NSDictionary"
- "%s Cannot handle audio buffer : unexpected format(%{public}u)"
- "%s Cannot report two shot since delegate doesn't have protocol implemented"
- "%s Cannot set Complexity property to audioConverter"
- "%s Cannot set Quality property to audioConverter"
- "%s Cannot start recording while connection does not exist"
- "%s Cannot stop recording while connection does not exist"
- "%s CarCapabilities latencyCorrectionSeconds: %@"
- "%s CarKit CRFetchCarPlayCapabilities timed out"
- "%s CarPlayCapabilities userInfo returned bad value: %@; returning nil for key=%@."
- "%s Clearing didStartRecordingDelegate WatchDogTimer : %{public}@"
- "%s Clearing didStopRecordingDelegate WatchDogTimer : %{public}@"
- "%s Clearing listening mic indicator lock property"
- "%s Context(%{public}d) recordRoute(%{public}@) playbackRoute(%{public}@) isRouteToBuiltInMic(%{public}d) isZLLAvailable(%{public}d)"
- "%s Create new CSAudioRecorder = %{public}p"
- "%s Created shared instance: %@"
- "%s Creating UUID for start audio stream request : %{public}@"
- "%s Creating audio session with allow mixable audio while recording to YES"
- "%s Current Picked route supportDoAP: %d"
- "%s Dealloc audioStreamHolding : %{public}@"
- "%s Delivering didStop to %{public}lu tandem stream(s)"
- "%s Detaching bluetooth session : %{public}p"
- "%s Device connection waiting timed out"
- "%s Device is temporary paired and not in contacts"
- "%s Device with address %{private}@ is temporary paired and not in contacts"
- "%s Did not find deviceUID(%{public}@) in mapping table"
- "%s DidStartRecording error : %{public}@"
- "%s Ducking %{public}@ supported on current route with streamId: %{public}ld"
- "%s Earcon removal feature flag disabled. Not adjusting latency from CS layer."
- "%s Elapsed time: %f seconds"
- "%s Encoder error : %{public}@"
- "%s Error getting adjustment for hardware latency. infoDict=%{public}@; err=%{public}@"
- "%s Error in CRFetchCarPlayCapabilities: %@"
- "%s Existing remoteRecordClient (deviceId = %@) doesn't match required one (deviceId = %@), create new remoteRecordClient"
- "%s Fail - Received didStartRecording : %{public}p, forStream:%{public}llu, successfully:%{public}d, error:%{public}@"
- "%s Fail to setSmartRoutingConsideration : %{public}@"
- "%s Failed converting address from BTDeviceAddress (result = %d)."
- "%s Failed getting audio property %{public}.4s %{public}d"
- "%s Failed getting audio property size %{public}.4s %d{public}"
- "%s Failed getting connected devices from local device %p (result = %d)."
- "%s Failed getting sharing device addresses %d"
- "%s Failed registering for property listener %{public}.4s %{public}d"
- "%s Failed to _prepareAudioStreamSync : %{public}@"
- "%s Failed to activateAudioSession : %{public}@"
- "%s Failed to activateAudioSessionWithReason: %{public}@"
- "%s Failed to add accessory manager callbacks"
- "%s Failed to add local device callback from session %{public}p, (result = %{public}d"
- "%s Failed to clear listening mic indicator lock property : %@"
- "%s Failed to configureAlertBehaviorForStream : %{public}@"
- "%s Failed to create AVVC : %{public}@"
- "%s Failed to deactivate audio session : %{public}@"
- "%s Failed to deactivateAudioSession : %{public}@"
- "%s Failed to fetch deviceUID"
- "%s Failed to fetch duckingSupported result : %{public}@"
- "%s Failed to fetch property of %{public}@ from deviceUUID %{public}@"
- "%s Failed to fetch remote deviceUId from AVVC"
- "%s Failed to fetch valid context"
- "%s Failed to get default accessory manager"
- "%s Failed to get default local device from session %{public}p, (result = %{public}d)"
- "%s Failed to get handle id : %{public}@"
- "%s Failed to get sharing enable flag : %d"
- "%s Failed to prepare remote device : %{public}@"
- "%s Failed to prewarmAudioSessionWithError : %{public}@"
- "%s Failed to query language code with endpointId %@, trying legacy query"
- "%s Failed to set listening mic indicator lock property : %@"
- "%s Failed to setAllowMixableAudioWhileRecording : %{public}@"
- "%s Failed to setDuckOthersForStream : %{public}@"
- "%s Failed to setDuckToLevelDB : %{public}@"
- "%s Failed to setIamTheAssistant : %{public}@"
- "%s Failed to startRecording : %{public}@"
- "%s Failed to stopRecordForStream : %{public}@"
- "%s Failed to stopRecording to remoteRecordClient : %{public}@"
- "%s Failed to teardown AVVC : %{public}@"
- "%s Fetched CSBluetoothDeviceInfo: %{private}@ for BTDevice with address: %{private}@"
- "%s Fetched CSBluetoothDeviceInfo: %{private}@ for BTDevice with address: %{private}@, supportDoAP: %d"
- "%s Fetching voiceTriggerInfo from audioRecorder"
- "%s Flushing audio preprocessor"
- "%s Forward %d samples from historical audio buffer from streamName:%@"
- "%s Found (%{public}@, %{public}@) pair in mapping table"
- "%s Found BTDevice with address %@"
- "%s General CarPlay is connected ? %{public}@"
- "%s GetAACPCapability result: BT_SUCCESS=%d, AACP capability bit: %d,  AACP capability supported: %d (%d)"
- "%s Getting connected devices from local device %p..."
- "%s Getting reply timed out!!"
- "%s Got %tu connected devices from local device %p."
- "%s HeadUnit is not recognized as having problematic latencies, but we failed to add AVF latencies"
- "%s HeadUnit is recognized as having problematic latencies, but didn't have a correction, and also failed to add AVF latencies"
- "%s HeadUnit is recognized as having problematic latencies, but no correction available. Adding earcon."
- "%s HeadUnit is recognized as having problematic latencies, correction is available but failed to add AVF latencies. Adding earcon."
- "%s Ignore %{public}@ since Siri client is current listening"
- "%s Ignore %{public}@ since Siri client is currently in a connected call"
- "%s Ignore %{public}@ since Siri client is currently in a ringtone and does not support A2DP"
- "%s Ignore %{public}@ since Siri client is currently in an outgoing call"
- "%s Ignore %{public}@ since VoiceTrigger was turned off"
- "%s Ignore playing endpoint beep(record stopped beep) since it already played beep in gibraltar"
- "%s Increase AudioFilePathIndex = %d"
- "%s Input route changed"
- "%s Invalid device with deviceId %{public}@"
- "%s Invalid deviceUID"
- "%s Invalid deviceUUID"
- "%s Invalid deviceUUIDString"
- "%s Invalid input streams"
- "%s Loading AACP capabilities for BTDevice with address %{private}@"
- "%s Local device is NULL."
- "%s Lost BTDevice with address %{private}@"
- "%s No adjustment for hardware latency to apply. avfLatencySeconds = %@"
- "%s No tuCallCenter to register"
- "%s Not CarPlay. Not adjusting latency from CS layer."
- "%s Not handled by this function"
- "%s Not reporting EPD due to unexpected zero or negative values: _stopRecordingHostTime: %{public}llu, _userSpeakingEndedHostTime: %{public}llu, _userSpeakingEndedTimeInMs: %{public}f, _endpointTimeInMs: %{public}f"
- "%s Not using remoteRecorder. Deprecated use of voiceTriggerInfo from AVVC"
- "%s Notifying Hearst Route State: %{public}ld"
- "%s Notifying Jarvis Connection State : %{public}d"
- "%s Output route changed"
- "%s Peak : %f, Avg : %f"
- "%s PowerLog : HeySiriFalseTrigger numFalseWakeUp:%{public}d, secondsSinceLastReport:%{public}lf, phrase:%{public}@"
- "%s Prewarm AudioSession has failed : %{public}@"
- "%s Primary device UUID : %{public}@, input device UUID : %{public}@"
- "%s PrimaryStream is already tandem of stream %{public}@, can't add mutual tandem relation here!"
- "%s Providing built-in voiceTriggerEventInfo"
- "%s Providing voiceTriggerEventInfo with deviceId %{public}@"
- "%s Raw VoiceTriggerEventInfo from remote = %{public}@"
- "%s Reach to EOF, chunkSize = %d"
- "%s Received AACP capabilities for BTDevice with address %{private}@ not in the connected list."
- "%s Received Call Observer Input : [connected:%d] [onhold:%d] [hasEnd:%d] [isOutputgoing:%d]"
- "%s Received CarPlay AuxStream support change notification"
- "%s Received CarPlay connection change notification"
- "%s Received Stream Invalidated : %{public}llu"
- "%s Received active route change notification"
- "%s Received audio buffer %{public}d, heartbeat = %{public}llu, streamID (%{public}lu)"
- "%s Received audiomxd or bridgeaudiod crashes event"
- "%s Received audiomxd or bridgeaudiod reset event"
- "%s Received didStartRecording : %{public}p, forStream:%{public}llu, successfully:%{public}d, error:%{public}@"
- "%s Received didStopRecording : %{public}p forStream:%{public}llu forReason:%{public}ld"
- "%s Received external pickable route change notification"
- "%s Received external route change notification"
- "%s Received finishStartAlertPlaybackAt:%{public}llu streamState : %{public}@"
- "%s Releasing listening mic indicator lock %@"
- "%s Releasing listening mic indicator lock UUID = %@"
- "%s Releasing listening mic indicator lock from : %d"
- "%s Releasing recordModeLock from : %d"
- "%s Releasing recordModeLock lock %@"
- "%s Releasing recordModeLock lock UUID = %@"
- "%s Remote device with device id: %{private}@ not found"
- "%s Replace deviceId(%{public}@) to nil for VoiceTrigger from Gibraltar."
- "%s Reporting server metrics to endpoint delay reporter"
- "%s Reset recordDeviceIndicator as we have new audioRecorder"
- "%s Resetting AudioFilePathIndex"
- "%s Resetting audio preprocessor : %{public}f, containsVoiceTrigger:%{public}d"
- "%s Return existing simple UID(%{public}@)"
- "%s Schedule didStart WDT %{public}@ for %{public}lf seconds"
- "%s Schedule didStop WDT %{public}@ for %{public}lf seconds"
- "%s ScheduleAlertFinishTimeout : %{public}@"
- "%s ScheduleAlertFinishTimeout will be ignored : %{public}@, %{public}@"
- "%s Sending event with time based triggerLengthSampleCount %llu, AOPVT triggerLengthSampleCount %llu, and delta of %lld samples"
- "%s Session State = %d"
- "%s Setting ExtAudioFileSetProperty failed : %d"
- "%s Setting announced call flag to: %d with stream handle Id: %lu"
- "%s Setting default enhanced endpointer model to %{public}@ for task %{public}@"
- "%s Setting firstAudioSampleSensorHostTime: %llu"
- "%s Setting listening mic indicator lock property"
- "%s Setting mixable to yes as we are in an active call"
- "%s Siri language is nil, falling back to %@"
- "%s Skip predictStartAlertBehavior for serverInvoke here"
- "%s Skip waiting for alert playing as we are allowing record during beep playing"
- "%s Start Recording Host Time = %{public}llu"
- "%s Start Recording Host Time: adjustment %{public}llu -> %{public}llu"
- "%s Start attaching bluetooth session"
- "%s Start deliver historical audio buffer immediately"
- "%s Start monitoring : AudioRouteChangeMonitor"
- "%s Start monitoring : audio stream activity"
- "%s Start monitoring : audiomxd crash / recover event"
- "%s Starting audio file feed timer, bufferDuration = %f sampleRate = %f, bytesPerFrame = %d, channelsPerFrame = %d"
- "%s Stop monitoring : AudioRouteChangeMonitor"
- "%s Stop monitoring : audio stream activity"
- "%s Stopping audio file feed timer"
- "%s Stream %{public}@ set startTimeInSampleCount : %{public}llu"
- "%s Successfully create AVVC : %{public}p"
- "%s TUPhone Call - [providerIdentifier: %@]"
- "%s TUPhone call - [TUCallStatus: %d]"
- "%s TUPhone call - identifier is not first party: %@"
- "%s Tear down _remoteRecordClient if needed"
- "%s Testing: Add (%{public}@, %{public}@) pair into mapping table"
- "%s The input streamHandleId(%{public}lu) is not expected(%{public}lu)"
- "%s There is no cached exception for %{public}@"
- "%s There is no remote device"
- "%s Tried to setCurrentContext with mode %ld. This method can only be used for auto and post"
- "%s Trying to access BTLocalDevice"
- "%s Unable to disable duckOthers in HomePod"
- "%s Unable to find injectAudioFilePath = %@"
- "%s Unexpected exception request : %{public}@"
- "%s Unsupported audio format!"
- "%s Update remote deviceUId fetched from AVVC : %{public}@ (this must be deviceUID of Darwin device only)"
- "%s Updated announce message exception table : %{public}@, reason : %{public}@"
- "%s Updated languageCode to: %{public}@ in VTEI received from remote"
- "%s Using cached CSBluetoothDeviceInfo: %{private}@ for BTDevice with Address: %{private}@"
- "%s Using cached CSBluetoothDeviceInfo: %{private}@ for BTDevice with identifier: %{private}@"
- "%s Using cached CarPlayCapabilities: %@"
- "%s VoiceTriggerInfo is nil from AVVC"
- "%s Will invalidate current builtIn audio stream : %{public}@"
- "%s XPC object type should be BOOL, DOUBLE, INT64, or UINT64"
- "%s Zero Filter Metrics: %{public}@"
- "%s _vtEndInSampleCount:%{public}ld, _numSamplesProcessed: %{public}ld, voiceTriggerInfo: %{public}@"
- "%s activate : %{public}d"
- "%s aux stream supported ? %{public}@"
- "%s carPlayCapabilitiesDict is nil, background fetching and returning nil immediately for key=%@."
- "%s checking modelMilBnnsIrCacheMap: %@"
- "%s configureAlertBehavior elapsed time = %{public}lf"
- "%s correctableHeadUnit: %d"
- "%s detached session is different from currently attached session, ignore"
- "%s enableMiniDucking elapsed time = %{public}lf"
- "%s enableSmartRoutingConsiderationForStream elapsed time = %{public}lf"
- "%s endpointUUID not provided, fallback to legacy query"
- "%s failed to stopAudioStream : %{public}@"
- "%s fetch CarPlay connection attribute elapsed time = %{public}lf"
- "%s fetch EndpointDeviceType elapsed time = %{public}lf"
- "%s fetch recordDeviceInfo elapsed time = %{public}lf"
- "%s getDeviceLatenciesForStream error: %@"
- "%s getFirstAudioSampleSensorHostTimeWithReply failed: %{public}@"
- "%s hasLocalPendingTwoShot = %{public}d, token : %{public}llu"
- "%s isHandsFree = %{public}d hasHaptic = %{public}d"
- "%s isNarrowBand = %{public}@ for streamHandleId = %{public}lu"
- "%s isNarrowBand = NO for streamHandleId = %{public}lu"
- "%s isSupported=%@: Is request during active call? %@, isDeviceSupported: %@, isSupportedRequestType: %@, isFFUserDisabled: %@, isTypeToSiriEnabled: %@"
- "%s packets count %{public}d"
- "%s prepareRecordForStream elapsed time = %{public}lf"
- "%s primaryStream already torn down"
- "%s received hostTimeAdjustment of %{public}llu, instead using max of %{public}llu."
- "%s received notification to purge asset with endPoint id: %@"
- "%s recordRoute = %@, playbackRoute = %@, speechEvent = %lu, activationMode = %ld, speechRecordingMode = %lu, AFDeviceRingerSwitchState = %@, AFSoundID = %@, AFPresentationMode = %lu, usesDeviceSpeakerForTTS = %lu, attemptsToUsePastDataBufferFrames = %d, usePrelistening = %d, isOnPhoneCall = %d, hasPlayedStartAlert = %d, supportsEchoCancellation = %d, isVoiceOverTouchEnabled = %d, isDeviceInCarDNDMode = %d, isVibrationEnabled = %d, isVibrationSupported = %d, suppressStartAlert = %d, activationHostTime = %llu"
- "%s register tuCallCenter notification call backs"
- "%s resetDuckSettings elapsed time = %{public}lf"
- "%s returning %@ for key=%@."
- "%s session = %{public}p, result = %{public}d"
- "%s setContext elapsed time = %{public}lf, streamHandleId = %{public}lu, streamType = %{public}lu"
- "%s setCurrentContext elapsed time = %{public}lf"
- "%s setDuckOthersForStream elapsed time = %{public}lf"
- "%s setRecordMode elapsed time = %{public}lf"
- "%s setSessionActivate elapsed time = %{public}lf"
- "%s startRecordForStream elapsed time = %{public}lf"
- "%s startRecordForStream failed : %{public}@"
- "%s startRecordingWatchDogDidFire : %{public}@, currentToken : %{public}@"
- "%s startRecordingWatchDogToken doesn't match. Ignore this WDT fire"
- "%s startRecordingWithOptions elapsed time = %{public}lf"
- "%s stopRecordForStream elapsed time = %{public}lf"
- "%s stopRecording elapsed time = %{public}lf"
- "%s stopRecordingWatchDogDidFire : %{public}@, currentToken : %{public}@"
- "%s stopRecordingWatchDogToken doesn't match. Ignore this WDT fire"
- "%s stream %@ is active"
- "%s stream %{public}@ initialized"
- "%s stream %{public}@ is deallocated"
- "%s streamHolder %@ is active"
- "%s success"
- "%s terminated session is different from currently attached session, ignore"
- "%s toConfiguration : %{public}d"
- "%s trackedHeadUnit: %d"
- "%s type : %{public}d, error : %{public}@"
- "%s withContext : %{public}@"
- "%s xpc object should be XPC_TYPE_ARRAY"
- "%s xpc object should be XPC_TYPE_DATA"
- "%s xpc object should be XPC_TYPE_DICTIONARY"
- "%s xpc object should be XPC_TYPE_STRING"
- "%s xpc object string return nil"
- "%s xpcObject value is NULL"
- "%s zeroFilterWinSz: %{public}tu, numHostTicksPerAudioSample: %{public}f"
- "+[CSAlertBehaviorPredictor predictStartAlertBehaviorFor:avSystemController:hasAOP:supportVibrator:isiOS:isWatchOS:isHorseman:isBridgeOS:recordRoute:playbackRoute:]"
- "+[CSAudioRecorder createSharedAudioSession]"
- "+[CSAudioRecorder resetDuckSettings]"
- "+[CSCarKitUtils sharedInstance]_block_invoke"
- "+[CSMil2BnnsUtils _compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:error:]"
- "+[CSMil2BnnsUtils compileModelWithMilFile:bnnsIrCachePath:]"
- "+[CSMil2BnnsUtils mmapModelWithConfig:mappedSizeOut:]"
- "+[CSPhoneCallStateMonitor sharedInstance]"
- "+[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:recordingInfo:speechEvent:activationMode:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usesDeviceSpeakerForTTS:attemptsToUsePastDataBufferFrames:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isDeviceInCarDNDMode:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]"
- "+[CSUtils(AudioHardware) isRemoteDarwinWithDeviceId:]"
- "+[CSUtils(LanguageCode) getSiriLanguageWithEndpointId:fallbackLanguage:]"
- "+[CSUtils(LanguageCode) getSiriLanguageWithFallback:]"
- "-[CSAttSiriMitigationAssetHandler setCachedAsset:]_block_invoke"
- "-[CSAudioFileReader _readAudioBufferAndFeed]"
- "-[CSAudioFileReader initWithURL:]"
- "-[CSAudioFileReader prepareRecording:]"
- "-[CSAudioFileReader startRecording]"
- "-[CSAudioFileReader stopRecording]"
- "-[CSAudioInjectionProvider startAudioStreamWithOption:recordDeviceIndicator:error:]"
- "-[CSAudioPreprocessor _fetchCurrentMetrics]"
- "-[CSAudioPreprocessor flush]"
- "-[CSAudioPreprocessor resetWithSampleRate:containsVoiceTrigger:voiceTriggerInfo:]"
- "-[CSAudioProvider CSAudioServerCrashMonitorDidReceiveServerCrash:]"
- "-[CSAudioProvider CSAudioServerCrashMonitorDidReceiveServerRestart:]"
- "-[CSAudioProvider _acquireListeningMicIndicatorLockFrom:]"
- "-[CSAudioProvider _acquireRecordModeLockFrom:]"
- "-[CSAudioProvider _activateAudioSessionWithReason:error:]"
- "-[CSAudioProvider _audioStreamWithRequest:streamName:error:]"
- "-[CSAudioProvider _cancelAudioStreamHold:]"
- "-[CSAudioProvider _clearDidStartRecordingDelegateWatchDog]"
- "-[CSAudioProvider _clearDidStopRecordingDelegateWatchDog]"
- "-[CSAudioProvider _clearListeningMicIndicatorProperty]"
- "-[CSAudioProvider _createCircularBufferIfNeededWithNumChannel:playbackRoute:]"
- "-[CSAudioProvider _deactivateAudioSession:error:]"
- "-[CSAudioProvider _didFireStreamHolderTimeout:]"
- "-[CSAudioProvider _didPlayStartAlertSoundForSiri:audioStream:]"
- "-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]"
- "-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke"
- "-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke_2"
- "-[CSAudioProvider _fetchHistoricalAudioAndForwardToStream:remoteVAD:]"
- "-[CSAudioProvider _forceReleaseListeningMicIndicatorLockFrom:]"
- "-[CSAudioProvider _forceReleaseRecordModeLockFrom:]"
- "-[CSAudioProvider _handleAudioRecorderStreamHandleIdInvalidated:]"
- "-[CSAudioProvider _handleAudioSystemFailure]"
- "-[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]"
- "-[CSAudioProvider _handleDidStopAudioStreamWithReason:]"
- "-[CSAudioProvider _isDuckingOnSpeakerOutputSupportedWithCurrentRoute]"
- "-[CSAudioProvider _onAudioPacketWatchdogFire]"
- "-[CSAudioProvider _prepareAudioStreamSync:request:error:]"
- "-[CSAudioProvider _releaseListeningMicIndicatorLock:]"
- "-[CSAudioProvider _releaseRecordModeLock:]"
- "-[CSAudioProvider _releaseRecordingTransactionIfNeeded]"
- "-[CSAudioProvider _saveRecordingBufferFrom:to:toURL:]_block_invoke"
- "-[CSAudioProvider _schduleDidStartRecordingDelegateWatchDogWithToken:]"
- "-[CSAudioProvider _scheduleAlertFinishTimeout:]"
- "-[CSAudioProvider _scheduleAlertFinishTimeout:]_block_invoke"
- "-[CSAudioProvider _scheduleDidStartRecordingDelegateWatchDog]"
- "-[CSAudioProvider _scheduleDidStopRecordingDelegateWatchDog:]"
- "-[CSAudioProvider _scheduleDidStopRecordingDelegateWatchDog]"
- "-[CSAudioProvider _setListeningMicIndicatorProperty]"
- "-[CSAudioProvider _shouldDuckOnBuiltInSpeaker]"
- "-[CSAudioProvider _shouldStopRecording]"
- "-[CSAudioProvider _startAudioStream:option:completion:]"
- "-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke"
- "-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2"
- "-[CSAudioProvider _stopAudioStream:option:completion:]"
- "-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke"
- "-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2"
- "-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3"
- "-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_4"
- "-[CSAudioProvider _updateRemoteDeviceIdFromAVVCIfNeeded]"
- "-[CSAudioProvider activateAudioSessionWithReason:dynamicAttribute:bundleID:error:]"
- "-[CSAudioProvider alertStartTime]"
- "-[CSAudioProvider attachTandemStream:toPrimaryStream:completion:]_block_invoke"
- "-[CSAudioProvider attachTandemStream:toPrimaryStream:completion:]_block_invoke_2"
- "-[CSAudioProvider audioRecorderBuiltInAudioStreamInvalidated:error:]_block_invoke"
- "-[CSAudioProvider audioRecorderDisconnected:]"
- "-[CSAudioProvider audioRecorderWillBeDestroyed:]_block_invoke"
- "-[CSAudioProvider cancelAudioStreamHold:]"
- "-[CSAudioProvider deactivateAudioSession:error:]"
- "-[CSAudioProvider dealloc]"
- "-[CSAudioProvider holdAudioStreamWithDescription:option:]"
- "-[CSAudioProvider playAlertSoundForType:]"
- "-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]"
- "-[CSAudioProvider prepareAudioStream:request:completion:]"
- "-[CSAudioProvider prepareAudioStreamSync:request:error:]"
- "-[CSAudioProvider prewarmAudioSessionWithError:]"
- "-[CSAudioProvider setAlertSoundFromURL:forType:force:]"
- "-[CSAudioProvider setAudioRecorder:]_block_invoke"
- "-[CSAudioProvider setCurrentContext:error:]"
- "-[CSAudioProvider setCurrentContext:error:]_block_invoke"
- "-[CSAudioProvider setDuckOthersOption:]"
- "-[CSAudioProvider setStreamState:]"
- "-[CSAudioProvider startAudioStream:option:completion:]"
- "-[CSAudioProvider startAudioStream:option:completion:]_block_invoke"
- "-[CSAudioProvider supportsDuckingOnCurrentRouteWithError:]"
- "-[CSAudioProvider triggerInfoForContext:completion:]_block_invoke"
- "-[CSAudioRecordContext(AVVC) avvcContextSettings]"
- "-[CSAudioRecordDeviceIndicator updateWithLatestRecordContext:]"
- "-[CSAudioRecorder _compensateChannelDataIfNeeded:receivedNumChannels:]"
- "-[CSAudioRecorder _createVoiceControllerWithError:]"
- "-[CSAudioRecorder _createVoiceControllerWithError:]_block_invoke"
- "-[CSAudioRecorder _createVoiceControllerWithError:]_block_invoke_2"
- "-[CSAudioRecorder _destroyVoiceController]"
- "-[CSAudioRecorder _fetchRemoteRecordClientWithDeviceId:streamHandleId:]"
- "-[CSAudioRecorder _getRecordSettingsWithRequest:]"
- "-[CSAudioRecorder _hasLocalPendingTwoShot]_block_invoke"
- "-[CSAudioRecorder _processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:]"
- "-[CSAudioRecorder _startAudioStreamForAudioInjectionWithAVVCContext:]"
- "-[CSAudioRecorder _trackRemoteAccessoryStreamIdIfNeeded:]"
- "-[CSAudioRecorder _updateLanguageCodeForRemoteVTEIResult:]"
- "-[CSAudioRecorder activateAudioSessionWithReason:streamHandleId:error:]"
- "-[CSAudioRecorder audioDeviceInfoWithStreamHandleId:recordDeviceIndicator:]"
- "-[CSAudioRecorder clearListeningMicIndicatorProperty]"
- "-[CSAudioRecorder configureAlertBehavior:audioStreamHandleId:]"
- "-[CSAudioRecorder deactivateAudioSession:error:]"
- "-[CSAudioRecorder deactivateAudioSession:streamHandleId:error:]"
- "-[CSAudioRecorder dealloc]"
- "-[CSAudioRecorder enableMiniDucking:]"
- "-[CSAudioRecorder enableSmartRoutingConsiderationForStream:enable:]"
- "-[CSAudioRecorder fetchGibraltarVoiceTriggerInfoWithRecordDeviceIndicator:]"
- "-[CSAudioRecorder initWithQueue:error:]"
- "-[CSAudioRecorder isDuckingSupportedOnCurrentRouteWithStreamHandleID:error:]"
- "-[CSAudioRecorder isNarrowBandWithStreamHandleId:]"
- "-[CSAudioRecorder isSessionCurrentlyActivated]"
- "-[CSAudioRecorder playAlertSoundForType:overrideMode:]"
- "-[CSAudioRecorder playAlertSoundForType:recordDevideIndicator:]"
- "-[CSAudioRecorder prepareAudioStreamRecord:recordDeviceIndicator:error:]"
- "-[CSAudioRecorder prewarmAudioSessionWithStreamHandleId:error:]"
- "-[CSAudioRecorder recordDeviceInfoWithStreamHandleId:recordDeviceIndicator:]"
- "-[CSAudioRecorder recordingSampleRateWithStreamHandleId:]"
- "-[CSAudioRecorder setAnnounceCallsEnabled:withStreamHandleID:]"
- "-[CSAudioRecorder setContext:completion:]"
- "-[CSAudioRecorder setCurrentContext:streamHandleId:error:]"
- "-[CSAudioRecorder setDuckMixWithOthersForStream:duckOthers:duckToLevelInDB:mixWithOthers:]"
- "-[CSAudioRecorder setListeningMicIndicatorProperty]"
- "-[CSAudioRecorder setRecordMode:streamHandleId:error:]"
- "-[CSAudioRecorder startAudioStreamWithOption:recordDeviceIndicator:error:]"
- "-[CSAudioRecorder stopAudioStreamWithRecordDeviceIndicator:error:]"
- "-[CSAudioRecorder userSessionActivateMonitor:didReceivedUserSessionActiveHasChanged:]_block_invoke"
- "-[CSAudioRecorder voiceControllerAudioCallback:forStream:buffer:]"
- "-[CSAudioRecorder voiceControllerBeginRecordInterruption:]"
- "-[CSAudioRecorder voiceControllerBeginRecordInterruption:withContext:]"
- "-[CSAudioRecorder voiceControllerDidFinishAlertPlayback:ofType:error:]"
- "-[CSAudioRecorder voiceControllerDidSetAudioSessionActive:isActivated:]"
- "-[CSAudioRecorder voiceControllerDidStartRecording:forStream:successfully:error:]"
- "-[CSAudioRecorder voiceControllerDidStopRecording:forStream:forReason:]"
- "-[CSAudioRecorder voiceControllerEncoderErrorDidOccur:error:]"
- "-[CSAudioRecorder voiceControllerEndRecordInterruption:]"
- "-[CSAudioRecorder voiceControllerRecordHardwareConfigurationDidChange:toConfiguration:]"
- "-[CSAudioRecorder voiceControllerStreamInvalidated:forStream:]"
- "-[CSAudioRecorder voiceControllerWillSetAudioSessionActive:willActivate:]"
- "-[CSAudioRecorder willDestroy]"
- "-[CSAudioRouteChangeMonitor _startMonitoringWithQueue:]"
- "-[CSAudioRouteChangeMonitor _stopMonitoring]"
- "-[CSAudioRouteChangeMonitor carPlayConnected]"
- "-[CSAudioRouteChangeMonitor getHearstOwnershipStatus:]"
- "-[CSAudioRouteChangeMonitor getHearstRouteStatus:]"
- "-[CSAudioRouteChangeMonitor getJarvisConnected:]"
- "-[CSAudioRouteChangeMonitor hearstOwnership]"
- "-[CSAudioRouteChangeMonitor hearstRouteStatus]"
- "-[CSAudioRouteChangeMonitor jarvisConnected]"
- "-[CSAudioRouteChangeMonitorImpl _fetchHearstRouteStatusWithCompletion:]_block_invoke"
- "-[CSAudioRouteChangeMonitorImpl _fetchJarvisConnectionState]"
- "-[CSAudioRouteChangeMonitorImpl _notifyHearstRouteStatus:]"
- "-[CSAudioRouteChangeMonitorImpl _notifyJarvisConnectionState:]"
- "-[CSAudioRouteChangeMonitorImpl _startMonitoringWithQueue:]"
- "-[CSAudioRouteChangeMonitorImpl _stopMonitoring]"
- "-[CSAudioRouteChangeMonitorImpl _systemControllerDied:]"
- "-[CSAudioRouteChangeMonitorImpl carPlayAuxStreamSupportDidChange:]_block_invoke"
- "-[CSAudioRouteChangeMonitorImpl carPlayConnected]"
- "-[CSAudioRouteChangeMonitorImpl carPlayIsConnectedDidChange:]"
- "-[CSAudioRouteChangeMonitorImpl pickableRoutesDidChange:]_block_invoke"
- "-[CSAudioRouteChangeMonitorImpl preferredExternalRouteDidChange:]_block_invoke"
- "-[CSAudioRouteChangeMonitorImplWatch _fetchHearstRouteStatusWithCompletion:]_block_invoke"
- "-[CSAudioRouteChangeMonitorImplWatch _notifyHearstRouteStatus:]"
- "-[CSAudioRouteChangeMonitorImplWatch _startMonitoringWithQueue:]"
- "-[CSAudioRouteChangeMonitorImplWatch _stopMonitoring]"
- "-[CSAudioRouteChangeMonitorImplWatch _systemControllerDied:]"
- "-[CSAudioRouteChangeMonitorImplWatch activeAudioRouteDidChange:]_block_invoke"
- "-[CSAudioSampleRateConverter _createSampleRateConverterWithInASBD:outASBD:]"
- "-[CSAudioSampleRateConverter convertSampleRateOfBuffer:]"
- "-[CSAudioServerCrashMonitor _startMonitoringWithQueue:]"
- "-[CSAudioServerCrashMonitor _startMonitoringWithQueue:]_block_invoke"
- "-[CSAudioStartStreamOption(AVVC) adjustStartRecordingHostTime:]"
- "-[CSAudioStartStreamOption(AVVC) avvcStartRecordSettingsWithAudioStreamHandleId:]"
- "-[CSAudioStream audioStreamProvider:didHardwareConfigurationChange:]"
- "-[CSAudioStream audioStreamProvider:didStopStreamUnexpectedly:]"
- "-[CSAudioStream dealloc]"
- "-[CSAudioStream initWithAudioStreamProvider:streamName:streamRequest:]"
- "-[CSAudioStream isStreaming]"
- "-[CSAudioStream startAudioStreamWithOption:completion:]"
- "-[CSAudioStream stopAudioStreamWithOption:completion:]_block_invoke"
- "-[CSAudioStream updateAudioStreamStartTimeInSampleCount:]"
- "-[CSAudioStreamActivityMonitor _startMonitoringWithQueue:]"
- "-[CSAudioStreamActivityMonitor _stopMonitoring]"
- "-[CSAudioStreamActivityMonitor notifyActiveStreamsChanged:streamHolders:streamId:]"
- "-[CSAudioStreamHolding dealloc]"
- "-[CSAudioTandemStream attachToPrimaryStreamWithCompletion:]"
- "-[CSAudioTandemStream prepareAudioStreamSyncWithRequest:error:]"
- "-[CSAudioTandemStream prepareAudioStreamWithRequest:completion:]"
- "-[CSAudioTandemStream startAudioStreamWithOption:completion:]"
- "-[CSAudioTandemStream stopAudioStreamWithOption:completion:]"
- "-[CSBluetoothManager _attachBluetoothSession]"
- "-[CSBluetoothManager _clearBluetoothDeviceInfoForDevice:]"
- "-[CSBluetoothManager _detachBluetoothSession]"
- "-[CSBluetoothManager _fetchAllConnectedDevices]"
- "-[CSBluetoothManager _getAddressWithBTDevice:]"
- "-[CSBluetoothManager _getBluetoothDeviceInfoForDeviceWithBTAddressString:]"
- "-[CSBluetoothManager _getConnectedBluetoothDeviceAddressesFromLocalDevice:]"
- "-[CSBluetoothManager _getWirelessSplitterInfoFromLocalDevice:]"
- "-[CSBluetoothManager _loadAACPCapabilityForDevice:deviceAddress:]"
- "-[CSBluetoothManager _sessionAttached:result:]"
- "-[CSBluetoothManager _sessionDetached:]"
- "-[CSBluetoothManager _sessionTerminated:]"
- "-[CSBluetoothManager _setBluetoothDeviceInfoForDevice:]"
- "-[CSBluetoothManager _setUpAccessoryManager]"
- "-[CSBluetoothManager _setUpLocalDevice]"
- "-[CSBluetoothManager accessoryManager:accessoryEvent:device:accessoryState:]"
- "-[CSBluetoothManager getBTLocalDeviceWithCompletion:]"
- "-[CSBluetoothManager getBTLocalDeviceWithCompletion:]_block_invoke"
- "-[CSBluetoothManager getBluetoothDeviceInfoForDeviceWithId:]"
- "-[CSBluetoothManager getBluetoothDeviceInfoForDeviceWithId:]_block_invoke"
- "-[CSBuiltInVoiceTrigger _handleAudioChunk:]"
- "-[CSCXPhoneCallStateMonitor callObserver:callChanged:]"
- "-[CSCXPhoneCallStateMonitor firstPartyCall]"
- "-[CSCXPhoneCallStateMonitor phoneCallState]"
- "-[CSCarKitUtils _fetchCarCapabilitiesDict]_block_invoke"
- "-[CSCarKitUtils _fetchCarCapabilitiesDict]_block_invoke_2"
- "-[CSCarKitUtils _invalidateCachedCarPlayCapabilities]"
- "-[CSCarKitUtils _updateCarPlayCapabilitiesDict]"
- "-[CSCarKitUtils _userInfoValueForKey:]"
- "-[CSCarKitUtils dealloc]"
- "-[CSCarKitUtils handleCarCapabilitiesUpdatedWithCompletion:]"
- "-[CSCarKitUtils handleHeadUnitConnectedWithAsyncCompletion:]"
- "-[CSCarKitUtils potentiallyAddHWLatencyToOption:streamHandle:voiceController:]"
- "-[CSContinuousVoiceTrigger startDetectTwoShot:]_block_invoke"
- "-[CSEndpointerProxy _setFirstAudioSampleSensorHostTimeIfNeeded:]"
- "-[CSHardwareLatencyHelper _hardwareLatenciesUsingStreamHandle:andVoiceController:]_block_invoke"
- "-[CSHardwareLatencyHelper _hardwareLatenciesUsingStreamHandle:andVoiceController:]_block_invoke_2"
- "-[CSHardwareLatencyHelper _hardwareLatencyAdjustmentSecondsUsingStreamHandle:andVoiceController:]"
- "-[CSHardwareLatencyHelper addHWLatencyToOption:withCorrection:streamHandle:voiceController:]"
- "-[CSMSNExceptionManager beginAnnounceMessageException:reason:]"
- "-[CSMSNExceptionManager beginAnnounceMessageException:reason:]_block_invoke"
- "-[CSMSNExceptionManager endAnnounceMessageException:reason:]"
- "-[CSMSNExceptionManager endAnnounceMessageException:reason:]_block_invoke"
- "-[CSModelBenchmarker _onDeviceCompilationWithConfigFile:locale:]"
- "-[CSOnDeviceCachedIrPurgingHandler purgeCachedIrForTrialAssetExcludingCurrentAsset:cachedIrDir:]"
- "-[CSOnDeviceCompilationHandler _compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:]"
- "-[CSOnDeviceCompilationHandler compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:]_block_invoke"
- "-[CSOnDeviceCompilationHandler compileUsingConfig:locale:compileDirectory:errOut:]_block_invoke"
- "-[CSPhoneCallStateMonitor firstPartyCall]"
- "-[CSPhoneCallStateMonitor phoneCallState]"
- "-[CSRemoteDarwinDeviceInfo addDeviceIDPairToMapTable:withDeviceUID:]_block_invoke"
- "-[CSRemoteDarwinDeviceInfo allDeviceDisconnected]_block_invoke"
- "-[CSRemoteDarwinDeviceInfo deviceConnectedWithUUID:]"
- "-[CSRemoteDarwinDeviceInfo deviceConnectedWithUUID:]_block_invoke"
- "-[CSRemoteDarwinDeviceInfo fetchDeviceUUIDStringFromUID:]"
- "-[CSRemoteDarwinDeviceInfo fetchDeviceUUIDStringFromUID:]_block_invoke"
- "-[CSRemoteDarwinDeviceInfo fetchRichDeviceUIDStringFromUUID:]"
- "-[CSRemoteDarwinDeviceInfo isPrimaryVoiceTriggerDeviceWithUUID:]_block_invoke"
- "-[CSRemoteRecordClient _handleDidStartRecordingMessage:]"
- "-[CSRemoteRecordClient _handleServerError:]"
- "-[CSRemoteRecordClient _handleServerEvent:]"
- "-[CSRemoteRecordClient _handleServerMessage:]"
- "-[CSRemoteRecordClient _handleTwoShotDetectedMessage:]"
- "-[CSRemoteRecordClient dealloc]"
- "-[CSRemoteRecordClient didDeviceConnect:]"
- "-[CSRemoteRecordClient didDeviceConnect:]_block_invoke"
- "-[CSRemoteRecordClient didDeviceDisconnect:]"
- "-[CSRemoteRecordClient didPlayEndpointBeep]"
- "-[CSRemoteRecordClient didPlayEndpointBeep]_block_invoke"
- "-[CSRemoteRecordClient hasPendingTwoShotBeep]"
- "-[CSRemoteRecordClient hasPendingTwoShotBeep]_block_invoke"
- "-[CSRemoteRecordClient initWithDeviceId:audioStreamHandleId:]"
- "-[CSRemoteRecordClient startRecordingWithOptions:error:]_block_invoke"
- "-[CSRemoteRecordClient stopRecording:]_block_invoke"
- "-[CSRemoteRecordClient voiceTriggerEventInfo]"
- "-[CSRemoteRecordClient voiceTriggerEventInfo]_block_invoke"
- "-[CSRemoteRecordClient waitingForConnection:error:]"
- "-[CSSiriAudioSession currentInputRoute]_block_invoke"
- "-[CSSiriAudioSession currentOutputRoute]_block_invoke_3"
- "-[CSSiriSpeechRecorder _reportServerEndpointMetricsIfNeeded]_block_invoke"
- "-[CSSiriSpeechRecorder _reportServerEndpointMetricsIfNeeded]_block_invoke_2"
- "-[CSSpeechController _audioStreamProvdider:audioBufferAvailable:]"
- "-[CSTUPhoneCallStateMonitor _fetchTUPhoneCallState]_block_invoke"
- "-[CSTUPhoneCallStateMonitor _registerPhoneCallStateChangeNotifier]"
- "-[CSTUPhoneCallStateMonitor firstPartyCall]_block_invoke"
- "-[CSVoiceTriggerAwareZeroFilter resetWithSampleRate:containsVoiceTrigger:voiceTriggerInfo:]"
- "-[CSVoiceTriggerEventInfoProvider fetchVoiceTriggerInfoWithAudioContext:resultVoiceTriggerInfo:resultRTSTriggerInfo:]_block_invoke"
- "-[CSVoiceTriggerStatAggregator logFalseWakeUp:withPhrase:]"
- "-[CSVoiceTriggerStatAggregator logTimeBasedTriggerLengthSampleCountStatistics:withAOPVTTriggerLengthSampleCount:]"
- "-[NSArray(XPCObject) _cs_initWithXPCObject:]"
- "-[NSArray(XPCObject) _cs_initWithXPCObject:]_block_invoke"
- "-[NSArray(XPCObject) _cs_xpcObject]_block_invoke"
- "-[NSData(XPCObject) _cs_initWithXPCObject:]"
- "-[NSDictionary(XPCObject) _cs_initWithXPCObject:]"
- "-[NSDictionary(XPCObject) _cs_initWithXPCObject:]_block_invoke"
- "-[NSDictionary(XPCObject) _cs_xpcObject]_block_invoke"
- "-[NSNumber(XPCObject) _cs_initWithXPCObject:]"
- "-[NSNumber(XPCObject) _cs_xpcObject]"
- "-[NSString(XPCObject) _cs_initWithXPCObject:]"
- "9\x14"
- "@\"<CSAudioFileReaderDelegate>\""
- "@\"<CSAudioPreprocessorDelegate>\""
- "@\"<CSAudioProviderDelegate>\""
- "@\"<CSAudioSessionEventProvidingDelegate>\""
- "@\"<CSRemoteRecordClientDelegate>\""
- "@\"<CSVoiceTriggerAwareZeroFilterDelegate>\""
- "@\"AFInstanceContext\""
- "@\"AVVoiceController\""
- "@\"CSADPPreventStandbyAssertion\""
- "@\"CSAudioDeviceInfo\""
- "@\"CSAudioDeviceInfo\"16@0:8"
- "@\"CSAudioFileReader\""
- "@\"CSAudioPreprocessor\""
- "@\"CSAudioRecordDeviceIndicator\""
- "@\"CSAudioRecordDeviceInfo\""
- "@\"CSAudioRecordDeviceInfo\"16@0:8"
- "@\"CSAudioStreamRequest\""
- "@\"CSAudioZeroFilter\""
- "@\"CSBeepCanceller\""
- "@\"CSMicUsageReporter\""
- "@\"CSRemoteRecordClient\""
- "@\"CSReusableBufferPool\""
- "@\"CSSiriAudioRoute\""
- "@\"CXCallObserver\""
- "@\"NSMutableOrderedSet\""
- "@\"OS_remote_device_browser\""
- "@\"TUCallCenter\""
- "@\"TUCallProviderManager\""
- "@\"UAFAssetSetObserver\""
- "@144@0:8@16@24@32q40q48q56q64q72q80q88B96B100B104B108B112B116B120B124B128B132Q136"
- "@24@0:8^{BTDeviceImpl=}16"
- "@24@0:8^{BTLocalDeviceImpl=}16"
- "@24@0:8f16i20"
- "@40@0:8@16Q24^@32"
- "@44@0:8@16@24B32Q36"
- "@44@0:8@16B24@28@36"
- "@48@0:8Q16q24@32@40"
- "@52@0:8@16B24@28@36@44"
- "@56@0:8Q16q24@32@40@48"
- "ADAudioSessionPortOther"
- "AVVC"
- "AVVoiceControllerRecordDelegate"
- "Audio Session Active Delay"
- "AudioHardware"
- "B20@0:8f16"
- "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
- "B32@0:8@16Q24"
- "B32@0:8q16q24"
- "B48@0:8@16d24Q32@40"
- "BeepCancellerMetrics"
- "BluetoothA2DPOutput"
- "BluetoothHFP"
- "BluetoothLE"
- "BuiltInMicrophoneDevice"
- "Builtin Microphone"
- "CARSessionCarCapabilitiesReadyNotification"
- "CARSessionCarCapabilitiesUpdatedNotification"
- "CESRTrialAssetDelegate"
- "CRCapabilitiesUserInfoKey"
- "CRFetchCarPlayCapabilities"
- "CSAVVoiceTriggerClientManager"
- "CSAlertBehaviorPredictor"
- "CSAudioFileReader"
- "CSAudioFileReader Queue"
- "CSAudioFileReaderDelegate"
- "CSAudioPreprocessor"
- "CSAudioPreprocessorDelegate"
- "CSAudioProvider"
- "CSAudioProvider Stream Handle Queue"
- "CSAudioProvider logging"
- "CSAudioProvider.m"
- "CSAudioProviderListeningMicIndicatorLock"
- "CSAudioProviderRecordModeLock"
- "CSAudioProviderRequestLock"
- "CSAudioRecordDeviceIndicator"
- "CSAudioRecorder"
- "CSAudioRouteChangeMonitor"
- "CSAudioRouteChangeMonitor.m"
- "CSAudioRouteChangeMonitorImpl"
- "CSAudioRouteChangeMonitorImpl queue"
- "CSAudioRouteChangeMonitorImplWatch"
- "CSAudioRouteChangeMonitorImplWatch queue"
- "CSAudioSampleRateConverter"
- "CSAudioSampleRateConverter.m"
- "CSAudioServerCrashMonitor"
- "CSAudioSessionEventProviding"
- "CSAudioStream"
- "CSAudioStreamActivityMonitor"
- "CSAudioStreamHolding"
- "CSAudioTandemStream"
- "CSAudioTandemStream.m"
- "CSBeepCancellerDelegate"
- "CSBluetoothDeviceInfo"
- "CSBluetoothManager"
- "CSBluetoothManager Queue"
- "CSBluetoothWirelessSplitterInfo"
- "CSCXPhoneCallStateMonitor"
- "CSCarKitUtils"
- "CSCarKitUtils.m"
- "CSDefaultAudioRouteChangeMonitorMac"
- "CSDigitalZeroReporting"
- "CSHardwareLatencyHelper"
- "CSMSNExceptionManager"
- "CSMSNExceptionManager Queue"
- "CSMSNExceptionManager.m"
- "CSMicUsageReporter"
- "CSPhoneCallStateMonitor"
- "CSPhoneCallStateMonitor.m"
- "CSPhoneCallStateMonitorFactory"
- "CSRemoteDarwinDeviceInfo"
- "CSRemoteDarwinDeviceInfo Queue"
- "CSRemoteRecordClient"
- "CSRemoteRecordClient Queue"
- "CSRemoteRecordClientDelegate"
- "CSSiriAudioRoute"
- "CSSiriAudioSession"
- "CSSiriPreferences"
- "CSTUPhoneCallStateMonitor"
- "CSTUPhoneCallStateMonitor queue"
- "CSUserSessionActiveMonitor"
- "CSUserSessionActiveMonitorDelegate"
- "CSVoiceTriggerAwareZeroFilter"
- "CSVoiceTriggerEventInfoProvider"
- "CSVoiceTriggerEventInfoProvider Queue"
- "CSVoiceTriggerStatAggregator"
- "CXCallObserverDelegate"
- "CoreSpeech-AudioStates[CSAudioProvider-%@]"
- "Device Type"
- "Expected startRecordingHostTime == 0; %@"
- "ExperimentGroup"
- "F\x12A\x14\x14\x14#!\x11"
- "HDMIOutput"
- "Headphones"
- "Internal User Classification"
- "LPCMBufferAvailable"
- "LanguageCode"
- "LineIn"
- "Listening"
- "MSNMonitorBeginException"
- "MSNMonitorEndException"
- "MicrophoneAttribution"
- "MicrophoneBuiltIn"
- "MicrophoneWired"
- "NSString *getCRCapabilitiesUserInfoKey(void)"
- "Q\x1b\xc1\x81\x12\x18"
- "RecordContext"
- "Recording"
- "Recording transaction"
- "Requested at stop"
- "SFEntitledTrialAssetDelegate"
- "Server Audio Session Activation Delay"
- "Server Audio Session Activation Delay Above Media Playback Volume Threshold"
- "Server Media Playback Volume Threshold for Audio Session Activation Delay"
- "StreamInit"
- "StreamPrepared"
- "StreamStarting"
- "StreamState[CSAudioProvider-%@]"
- "StreamStopping"
- "StreamStoppingWithScheduledStart"
- "StreamStreaming"
- "T@\"<CSAttendingServiceDelegate>\",W,N"
- "T@\"<CSAttendingServiceDelegate>\",W,N,V_delegate"
- "T@\"<CSAudioAlertProvidingDelegate>\",W,N,V_alertDelegate"
- "T@\"<CSAudioFileReaderDelegate>\",W,N,V_delegate"
- "T@\"<CSAudioPreprocessorDelegate>\",W,N,V_delegate"
- "T@\"<CSAudioProviderDelegate>\",W,N,V_providerDelegate"
- "T@\"<CSAudioSessionEventProvidingDelegate>\",W,N,V_sessionEventDelegate"
- "T@\"<CSAudioSessionProvidingDelegate>\",W,N,V_sessionDelegate"
- "T@\"<CSAudioStreamProviding>\",W,N,V_streamProvider"
- "T@\"<CSAudioStreamProvidingDelegate>\",W,N,V_delegate"
- "T@\"<CSRemoteRecordClientDelegate>\",W,N,V_delegate"
- "T@\"<CSVoiceTriggerAwareZeroFilterDelegate>\",W,N,V_delegate"
- "T@\"CSADPPreventStandbyAssertion\",&,N,V_adpAssertion"
- "T@\"CSAudioDeviceInfo\",&,N,V_audioDeviceInfo"
- "T@\"CSAudioPreprocessor\",&,N,V_audioPreprocessor"
- "T@\"CSAudioRecordContext\",&,N,V_lastAudioRecorderContext"
- "T@\"CSAudioRecordContext\",R,N,V_recordContext"
- "T@\"CSAudioRecordDeviceIndicator\",&,N,V_recordDeviceIndicator"
- "T@\"CSAudioRecordDeviceInfo\",R,C,N,V_recordDeviceInfo"
- "T@\"CSAudioRecordDeviceInfo\",R,N,V_deviceInfo"
- "T@\"CSAudioSampleRateConverter\",&,N,V_upsampler"
- "T@\"CSAudioStartStreamOption\",&,N,SsetStartStreamOption:,V_startStreamOption"
- "T@\"CSAudioStream\",W,N,V_primaryStream"
- "T@\"CSAudioStreamRequest\",&,N,V_streamRequest"
- "T@\"CSAudioZeroCounter\",&,N,V_zeroCounter"
- "T@\"CSAudioZeroFilter\",&,N,V_zeroFilter"
- "T@\"CSBeepCanceller\",&,N,V_beepCanceller"
- "T@\"CSMicUsageReporter\",&,N,V_micUsageReporter"
- "T@\"CSOSTransaction\",&,N,V_recordingTransaction"
- "T@\"CSPhoneCallStateMonitor\",&,N,V_phoneCallStateMonitor"
- "T@\"CSVoiceTriggerEnabledMonitor\",&,N,V_voiceTriggerEnabledMonitor"
- "T@\"CXCallObserver\",&,N,V_callObserver"
- "T@\"NSArray\",&,N,V_connectedDeviceAddresses"
- "T@\"NSArray\",&,N,V_pairedDeviceAddresses"
- "T@\"NSArray\",R,C,N,V_playbackDeviceTypeList"
- "T@\"NSDictionary\",C,N,V_rtsTriggerInfo"
- "T@\"NSDictionary\",R,N,V_carPlayCapabilitiesDict"
- "T@\"NSHashTable\",&,N,V_alertPlaybackFinishWaitingStreams"
- "T@\"NSHashTable\",&,N,V_historicalBufferRequestStreams"
- "T@\"NSHashTable\",&,N,V_startPendingOnStoppingStreams"
- "T@\"NSHashTable\",&,N,V_startPendingStreams"
- "T@\"NSHashTable\",&,N,V_stopPendingStreams"
- "T@\"NSHashTable\",&,N,V_streams"
- "T@\"NSHashTable\",R,N,V_tandemStreams"
- "T@\"NSMutableArray\",&,N,V_alertPlaybackFinishWaitingCompletions"
- "T@\"NSMutableArray\",&,N,V_pendingStartCompletions"
- "T@\"NSMutableArray\",&,N,V_pendingStopCompletions"
- "T@\"NSMutableArray\",&,N,V_streamHolders"
- "T@\"NSMutableDictionary\",&,N,V_announceMessageExceptions"
- "T@\"NSMutableDictionary\",&,N,V_deviceAddressToDeviceInfoMap"
- "T@\"NSMutableDictionary\",&,N,V_deviceUIDMapTable"
- "T@\"NSMutableDictionary\",&,N,V_falseWakePhraseDictionary"
- "T@\"NSMutableDictionary\",&,N,V_listeningMicIndicatorLocks"
- "T@\"NSMutableDictionary\",&,N,V_recordModeLocks"
- "T@\"NSMutableDictionary\",&,N,V_startPendingOnStoppingStreamToCompletionDict"
- "T@\"NSMutableOrderedSet\",&,N,V_voiceTriggerEnabledDevices"
- "T@\"NSMutableSet\",&,N,V_remoteAccessoryStreamIdSet"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_bluetoothSessionSetupGroup"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_recordQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_streamHandleQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_voiceControllerCreationQueue"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_audioPacketWatchdog"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_listeningMicIndicatorLockUUIDString"
- "T@\"NSString\",&,N,V_recordModeLockUUIDString"
- "T@\"NSString\",C,N,V_address"
- "T@\"NSString\",C,N,V_deviceIdentifier"
- "T@\"NSString\",R,C,N,V_destination"
- "T@\"NSString\",R,C,N,V_deviceName"
- "T@\"NSString\",R,C,N,V_playbackRoute"
- "T@\"NSString\",R,C,N,V_remoteDeviceProductIdentifier"
- "T@\"NSString\",R,C,N,V_remoteDeviceUIDString"
- "T@\"NSString\",R,C,N,V_route"
- "T@\"NSString\",R,C,N,V_source"
- "T@\"NSString\",R,C,N,V_uid"
- "T@\"NSString\",R,N,V_UUIDString"
- "T@\"NSString\",R,N,V_name"
- "T@\"NSUUID\",&,N,V_alertPlaybackFinishTimeoutToken"
- "T@\"NSUUID\",&,N,V_startRecordingWatchDogToken"
- "T@\"NSUUID\",&,N,V_stopRecordingWatchDogToken"
- "T@\"NSUUID\",&,V_streamingUUID"
- "T@\"NSUUID\",R,C,N,V_remoteDeviceUID"
- "T@\"OS_remote_device\",&,N,V_device"
- "T@\"TUCallCenter\",&,N,V_tuCallCenter"
- "T@\"TUCallProviderManager\",&,N,V_tuCallProviderManager"
- "TB,N"
- "TB,N,SsetScheduledFutureSample:,V_scheduledFutureSample"
- "TB,N,V_audioSystemRecovering"
- "TB,N,V_currentSessionShouldDuckOnBuiltInSpeaker"
- "TB,N,V_hasNonVoiceTriggerStreamsActive"
- "TB,N,V_isAttachingBluetoothSession"
- "TB,N,V_isTemporaryPairedNotInContacts"
- "TB,N,V_isWeakStream"
- "TB,N,V_needsBoost12dB"
- "TB,N,V_saveSamplesSeenInReset"
- "TB,N,V_splitterEnabled"
- "TB,N,V_supportDoAP"
- "TB,N,V_supportMph"
- "TB,N,V_waitingForAlertFinish"
- "TB,R,N,V_isBluetooth"
- "TB,R,N,V_isRemoteDevice"
- "TB,R,N,V_shouldUseRemoteRecorder"
- "TB,V_streaming"
- "TQ,N,V_audioPacketDeliveryCount"
- "TQ,N,V_circularBufferStartHostTime"
- "TQ,N,V_circularBufferStartSampleCount"
- "TQ,N,V_estimatedStartHostTime"
- "TQ,N,V_lastAggTimeFalseWakeUp"
- "TQ,N,V_numFalseWakeUp"
- "TQ,N,V_serverState"
- "TQ,N,V_streamState"
- "TQ,N,V_triggerNotifiedMachTime"
- "TQ,N,V_tuPhoneCallState"
- "TQ,R,N,V_audioStreamHandleId"
- "TQ,R,N,V_clientIdentity"
- "TQ,R,N,V_lastForwardedSampleCount"
- "TQ,R,N,V_streamHandleId"
- "T^{BTAccessoryManagerImpl=},N,V_accessoryManager"
- "T^{BTLocalDeviceImpl=},N,V_localDevice"
- "T^{BTSessionImpl=},N,V_bluetoothSession"
- "Td,N,V_endWaitTime"
- "Td,N,V_interspeechWaitTime"
- "Tf,N,V_sampleRate"
- "Ti,N,V_numChannels"
- "Tq,N,V_audioStreamType"
- "Tq,N,V_endpointMode"
- "USBAudio"
- "UniqueDeviceID"
- "V"
- "XPCObject"
- "ZeroFilterMetrics"
- "[Announced = %d]"
- "[Context = %ld]"
- "[Device%d(%@) DoAP(%d)]"
- "[DeviceId = %@]"
- "[SplitterEnabled(%d)]"
- "[SplitterState:%d]"
- "[skipAlert = %@]"
- "[startAlert = %d]"
- "[startHostTime = %llu]"
- "[stopAlert = %d]"
- "[stopOnErrorAlert = %d]"
- "[streamHandleId = %d]"
- "^v32@0:8@16^@24"
- "^{BTAccessoryManagerImpl=}16@0:8"
- "^{BTLocalDeviceImpl=}16@0:8"
- "^{BTSessionImpl=}16@0:8"
- "^{OpaqueAudioConverter=}96@0:8{AudioStreamBasicDescription=dIIIIIIII}16{AudioStreamBasicDescription=dIIIIIIII}56"
- "_AudioDeviceRegisterForChangedNotification"
- "_AudioObjectGetCFTypeRef"
- "_AudioObjectGetIntValue"
- "_AudioObjectGetScalarArray"
- "_accessoryVoiceTriggerEvents"
- "_acquireListeningMicIndicatorLockFrom:"
- "_acquireRecordModeLockFrom:"
- "_adjustmentSecondsFromLatencyInfo:error:"
- "_adpAssertion"
- "_alertBehaviorForRecordRoute:playbackRoute:recordingInfo:speechEvent:activationMode:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usesDeviceSpeakerForTTS:attemptsToUsePastDataBufferFrames:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isDeviceInCarDNDMode:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:"
- "_alertBehaviorTypeFromAVVCOverrideType:"
- "_alertDelegate"
- "_alertPlaybackFinishTimeoutToken"
- "_alertPlaybackFinishWaitingCompletions"
- "_alertPlaybackFinishWaitingStreams"
- "_announceMessageExceptions"
- "_attachBluetoothSession"
- "_audioBufferPool"
- "_audioChunkFrom:to:"
- "_audioChunkFrom:to:channelIdx:"
- "_audioFilePathIndex"
- "_audioFileReader"
- "_audioIsFromRemoteAccessory:"
- "_audioPacketDeliveryCount"
- "_audioPacketWatchdog"
- "_audioPreprocessor"
- "_audioRecorderDidStartRecordingSuccessfully:streamHandleID:error:"
- "_audioRecorderDidStopRecordingForReason:streamHandleID:"
- "_audioStreamProvdider:audioBufferAvailable:"
- "_audioStreamType"
- "_audioStreamWithRequest:streamName:error:"
- "_audioSystemRecovering"
- "_beepCanceller"
- "_bluetoothSession"
- "_bluetoothSessionSetupGroup"
- "_builtInVoiceTriggerEvent"
- "_callObserver"
- "_callStatusDidChangeHandler:"
- "_canSetContext"
- "_cancelAudioPacketWatchDog"
- "_cancelAudioStreamHold:"
- "_carCapabilitiesLock"
- "_carPlayCapabilitiesDict"
- "_circularBufferStartHostTime"
- "_circularBufferStartSampleCount"
- "_clearBluetoothDeviceInfoForDevice:"
- "_clearDidStartRecordingDelegateWatchDog"
- "_clearDidStopRecordingDelegateWatchDog"
- "_clearListeningMicIndicatorProperty"
- "_clearListeningMicIndicatorPropertyIfNeeded"
- "_clientIdentity"
- "_compileModelAndAddToCacheWithConfigFiles:compileDirectoryPath:locale:assetVersion:hashToUse:"
- "_compileWithExceptionHandlingUsingModelFilePath:bnnsIrPath:milConfigPath:error:"
- "_connectedDeviceAddresses"
- "_convertDeactivateOption:"
- "_createCircularBufferIfNeededWithNumChannel:playbackRoute:"
- "_createSampleRateConverterWithInASBD:outASBD:"
- "_createVoiceControllerWithError:"
- "_cs_isHashTableEmpty"
- "_currentSessionShouldDuckOnBuiltInSpeaker"
- "_deactivateAudioSession:error:"
- "_delayBecauseCarKitSendsNotificationBeforeCapabilitiesActuallyReady"
- "_deliverHistoricalAudioToStreamsWithRemoteVAD:"
- "_deliverPostprocessAudioChunk:toStream:lastForwardedSampleCount:"
- "_destroyVoiceController"
- "_detachBluetoothSession"
- "_deviceAddressToDeviceInfoMap"
- "_deviceBrowser"
- "_deviceUIDMapTable"
- "_didFireStreamHolderTimeout:"
- "_didPlayStartAlertSoundForSiri:audioStream:"
- "_didReceiveFinishStartAlertPlaybackAt:"
- "_didReceiveMediaserverNotification:"
- "_endpointMode"
- "_estimatedStartHostTime"
- "_falseWakePhraseDictionary"
- "_fetchAllConnectedDevices"
- "_fetchCarCapabilitiesDict"
- "_fetchCarCapabilitiesInBackgroundWithCompletion:"
- "_fetchCurrentMetrics"
- "_fetchHearstConnectionState"
- "_fetchHearstRouteStatusWithCompletion:"
- "_fetchHistoricalAudioAndForwardToStream:remoteVAD:"
- "_fetchJarvisConnectionState"
- "_fetchRemoteRecordClientWithDeviceId:streamHandleId:"
- "_fetchTUPhoneCallState"
- "_forceReleaseAllListeningMicIndicatorLocks"
- "_forceReleaseAllRecordModeLocks"
- "_forceReleaseListeningMicIndicatorLockFrom:"
- "_forceReleaseRecordModeLockFrom:"
- "_forwardAudioChunk:toStream:"
- "_forwardAudioChunkForTV:toStream:"
- "_getAddressWithBTDevice:"
- "_getBluetoothDeviceInfoForDeviceWithBTAddressString:"
- "_getConnectedBluetoothDeviceAddressesFromLocalDevice:"
- "_getRecordSettingsWithRequest:"
- "_getVoiceController"
- "_getWirelessSplitterInfoFromLocalDevice:"
- "_handleAudioRecorderStreamHandleIdInvalidated:"
- "_handleAudioSystemFailure"
- "_handleDidStartAudioStreamWithResult:error:"
- "_handleDidStartRecordingMessage:"
- "_handleDidStopAudioStreamWithReason:"
- "_handleTwoShotDetectedMessage:"
- "_hardwareLatenciesUsingStreamHandle:andVoiceController:"
- "_hardwareLatencyAdjustmentSeconds:hwLatencyType:error:"
- "_hardwareLatencyAdjustmentSecondsUsingStreamHandle:andVoiceController:"
- "_hasDeviceTemporaryPairedNotInContacts"
- "_hasLocalPendingTwoShot"
- "_hasNonVoiceTriggerStreamsActive"
- "_hasSetAlertDictionary"
- "_historicalBufferRequestStreams"
- "_holdAudioStreamWithHolder:option:"
- "_holdRecordingExceptionIfNeeded:"
- "_holdRecordingTransactionIfNeeded"
- "_inASBD"
- "_inputRoute"
- "_instanceContext"
- "_interleavedABL"
- "_invalidateCachedCarPlayCapabilities"
- "_isAttachingBluetoothSession"
- "_isBluetooth"
- "_isBuiltInDeviceFromDeviceId:"
- "_isDarwinDeviceId:"
- "_isDuckingOnSpeakerOutputSupportedWithCurrentRoute"
- "_isNarrowBand:"
- "_isRemoteDarwinConnectedWithUUID:"
- "_isRemoteDevice"
- "_isRemoteRecording"
- "_isTemporaryPairedNotInContacts"
- "_isValidLatencyCorrectionValue:"
- "_isWeakStream"
- "_lastAggTimeFalseWakeUp"
- "_lastAudioRecorderContext"
- "_latencyCorrectionSecondsForHeadUnit"
- "_listeningMicIndicatorLockUUIDString"
- "_listeningMicIndicatorLocks"
- "_loadAACPCapabilityForDevice:deviceAddress:"
- "_locale"
- "_logResourceNotAvailableErrorIfNeeded:"
- "_mediaserverdDidRestart"
- "_micUsageReporter"
- "_needResetAudioInjectionIndex:"
- "_needsBoost12dB"
- "_notifyHearstRouteStatus:"
- "_notifyJarvisConnectionState:"
- "_notifyObserver:withMediaserverState:"
- "_numFalseWakeUp"
- "_observer"
- "_onAudioPacketWatchdogFire"
- "_onDeviceCompilationWithConfigFile:locale:"
- "_opusDecoders"
- "_outBufferScaleFactor"
- "_outputRoute"
- "_pairedDeviceAddresses"
- "_pendingStartCompletions"
- "_pendingStopCompletions"
- "_pendingTwoShotVTToken"
- "_phoneCallStateMonitor"
- "_playbackDeviceTypeList"
- "_playbackRoute"
- "_postEpilogueAudioStream"
- "_preEpilogueAudioStream"
- "_prepareAudioStream:request:completion:"
- "_prepareAudioStreamSync:request:error:"
- "_primaryStream"
- "_processAudioBuffer:audioStreamHandleId:arrivalTimestampToAudioRecorder:"
- "_processAudioBuffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:"
- "_processAudioChain:audioStreamHandleId:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:"
- "_providerDelegate"
- "_recacheCarPlayCapabilitiesWithCompletion:"
- "_recordDeviceIndicator"
- "_recordDeviceInfo"
- "_recordModeLockUUIDString"
- "_recordModeLocks"
- "_recordModeString:"
- "_recordQueue"
- "_recordingTransaction"
- "_registerPhoneCallStateChangeNotifier"
- "_releaseListeningMicIndicatorLock:"
- "_releaseRecordModeLock:"
- "_releaseRecordingTransactionIfNeeded"
- "_remoteAccessoryStreamIdSet"
- "_remoteDeviceProductIdentifier"
- "_remoteDeviceUID"
- "_remoteDeviceUIDString"
- "_remoteRecordClient"
- "_reportMetrics"
- "_reportVoiceTriggerFirstPassFireFromAP"
- "_resetCircularBufferStartTime"
- "_rtsTriggerInfo"
- "_sampleRate"
- "_sampleRateConverter"
- "_schduleDidStartRecordingDelegateWatchDogWithToken:"
- "_scheduleAlertFinishTimeout:"
- "_scheduleAudioPacketWatchDog"
- "_scheduleDidStartRecordingDelegateWatchDog"
- "_scheduleDidStopRecordingDelegateWatchDog"
- "_scheduleDidStopRecordingDelegateWatchDog:"
- "_scheduledFutureSample"
- "_serverState"
- "_sessionDelegate"
- "_sessionEventDelegate"
- "_setBluetoothDeviceInfoForDevice:"
- "_setFirstAudioSampleSensorHostTimeIfNeeded:"
- "_setLatestRecordContext:"
- "_setListeningMicIndicatorProperty"
- "_setListeningMicIndicatorPropertyIfNeeded"
- "_shouldDuckOnBuiltInSpeaker"
- "_shouldHandleStartPendingOnStopping:withStopReason:"
- "_shouldInjectAudio"
- "_shouldLogResourceNotAvailableError"
- "_shouldStopRecording"
- "_shouldUseRemoteBuiltInMic:"
- "_shouldUseRemoteRecorder"
- "_splitterDeviceList"
- "_splitterEnabled"
- "_startAudioStream:option:completion:"
- "_startAudioStreamForAudioInjectionWithAVVCContext:"
- "_startObservingAudioRouteChange"
- "_startObservingCarCapabilitiesNotfication:"
- "_startPendingOnStoppingStreamToCompletionDict"
- "_startPendingOnStoppingStreams"
- "_startPendingStreams"
- "_startRecordingWatchDogToken"
- "_stopAudioStream:option:completion:"
- "_stopPendingStreams"
- "_stopRecordingWatchDogToken"
- "_stopTrackingRemoteAccessoryStreamId:"
- "_streamHandleId"
- "_streamHandleQueue"
- "_streamHolders"
- "_streamRequest"
- "_streamState"
- "_streamStateName:"
- "_streaming"
- "_streamingUUID"
- "_streams"
- "_supportDoAP"
- "_supportMph"
- "_switchToListeningMode"
- "_switchToRecordingMode"
- "_tandemStreams"
- "_trackRemoteAccessoryStreamIdIfNeeded:"
- "_triggerNotifiedMachTime"
- "_tuCallCenter"
- "_tuCallProviderManager"
- "_tuPhoneCallState"
- "_uid"
- "_updateCarPlayCapabilitiesDict"
- "_updateLanguageCodeForRemoteVTEIResult:"
- "_updateRemoteDeviceIdFromAVVCIfNeeded"
- "_upsampler"
- "_userInfoValueForKey:"
- "_valuesAreMinimalyValidForInfoDictionary:type:"
- "_voiceController"
- "_voiceControllerCreationQueue"
- "_voiceTriggerEnabledDevices"
- "_waitingForAlertFinish"
- "_waitingForDidStart"
- "_zeroCounter"
- "accessoryManager"
- "accessoryManager:accessoryEvent:device:accessoryState:"
- "activateAudioSessionForStream:isPrewarm:error:"
- "activateAudioSessionForStream:isPrewarm:recordMode:error:"
- "activationDeviceUID"
- "activationMode"
- "activeAudioRouteDidChange:"
- "activeStreams[CSAudioProvider-%@]"
- "addDeviceIDPairToMapTable:withDeviceUID:"
- "addDeviceIntoSplitterDeviceList:"
- "addHWLatencyToOption:withCorrection:streamHandle:voiceController:"
- "adjustStartRecordingHostTime:"
- "adpAssertion"
- "alertDelegate"
- "alertPlaybackFinishTimeoutToken"
- "alertPlaybackFinishWaitingCompletions"
- "alertPlaybackFinishWaitingStreams"
- "allDeviceDisconnected"
- "allowExtendedRingBufferSize"
- "allowRecordWhileBeep"
- "announceCallsEnabled"
- "announceMessageExceptions"
- "announcemessage"
- "asr_adopting_uaf"
- "attachToPrimaryStreamWithCompletion:"
- "audioFileReaderBufferAvailable:buffer:atTime:"
- "audioFileReaderDidStartRecording:successfully:error:"
- "audioFileReaderDidStopRecording:forReason:"
- "audioInjectionFilePath"
- "audioPacketDeliveryCount"
- "audioPacketWatchdog"
- "audioPreprocessor"
- "audioPreprocessor:hasAvailableBuffer:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:"
- "audioStreamProvider:audioBufferAvailable:lastForwardedSampleCount:"
- "audioStreamType"
- "audioSystemRecovering"
- "auto"
- "avvcAlertBehavior"
- "avvcAlertOverrideType:"
- "avvcContext"
- "avvcStartRecordSettingsWithAudioStreamHandleId:"
- "a\x828!!!R\x11"
- "a\x8912!RS"
- "beepCanceller"
- "beepCancellerDidCancelSamples:buffer:timestamp:"
- "beginAnnounceMessageException:reason:"
- "bluetoothSession"
- "bluetoothSessionSetupGroup"
- "buffer"
- "bytesDataSize"
- "callCenterWithQueue:"
- "callObserver"
- "callObserver:callChanged:"
- "calls"
- "cancelBeepFromSamples:timestamp:"
- "carPlayAuxStreamSupportDidChange:"
- "carPlayCapabilitiesDict"
- "carPlayIsConnectedDidChange:"
- "carplay"
- "carry"
- "channels"
- "chunkForChannel:"
- "circularBufferInputRecordingDuration"
- "circularBufferNumInputChannel"
- "circularBufferStartHostTime"
- "circularBufferStartSampleCount"
- "clearListeningMicIndicatorProperty"
- "clientIdentity"
- "com.apple.CoreSpeech.CSCarKitUtilsQueue"
- "com.apple.corespeech.AudioZeroRun"
- "com.apple.corespeech.SecondPassWakeUp"
- "com.apple.corespeech.aopFirstPassTriggerWakeupLatency"
- "com.apple.corespeech.recording"
- "com.apple.corespeech.xpc.remote.record"
- "com.apple.corespeech.xpc.remote.record.darwin"
- "com.apple.da"
- "com.apple.exprAOPSecondPass"
- "compileAndUpdateDeviceCachesWithAsset:assetType:deviceId:currentLocale:compileDirectory:errOut:"
- "compileModelWithMilFile:bnnsIrCachePath:"
- "compileUsingConfig:locale:compileDirectory:errOut:"
- "configureAlertBehaviorForStream:error:"
- "connectedDeviceAddresses"
- "copySamplesFrom:to:channelIdx:"
- "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
- "currentAudioAndVideoCalls"
- "currentInputDeviceUIDArray"
- "currentInputRoute"
- "currentOutputRoute"
- "currentSessionShouldDuckOnBuiltInSpeaker"
- "deactivateAudioSessionForStream:withOptions:error:"
- "deactivateAudioSessionWithOptions:"
- "defaultContext"
- "defaultOutputAudioDeviceID"
- "deviceAddressToDeviceInfoMap"
- "deviceConnectedWithUUID:"
- "deviceDisconnectedWithUUID:"
- "deviceUIDMapTable"
- "didPlayEndpointBeep"
- "didStartRecording"
- "didStartRecordingError"
- "didStopRecording"
- "disableBoostForDoAP"
- "disableFlexibleFollowup"
- "duration"
- "enableSmartRoutingConsiderationForStream:enable:error:"
- "encoderBitRate"
- "endAnnounceMessageException:reason:"
- "endAudioAndFetchAnyTrailingZerosPacket:"
- "endpointMode"
- "endpointType"
- "errorAlertBehavior"
- "estimatedStartHostTime"
- "failed"
- "falseWakePhraseDictionary"
- "fetchDeviceUUIDStringFromUID:"
- "fetchRichDeviceUIDStringFromUUID:"
- "fetchVoiceTriggerInfoWithAudioContext:resultVoiceTriggerInfo:resultRTSTriggerInfo:"
- "filterZerosInAudioPacket:atBufferHostTime:filteredPacket:"
- "gainCompensatedChunk"
- "getAsset:"
- "getAveragePowerForStream:forChannel:"
- "getBTDeviceInfoWithBTAddressString:withCompletion:"
- "getBluetoothDeviceInfoForDeviceWithId_latency"
- "getCurrentSessionState"
- "getCurrentStreamState:"
- "getDeviceLatenciesForStream:withCompletion:"
- "getFirstAudioSampleSensorHostTimeWithReply:"
- "getHearstOwnershipStatus:"
- "getHostClockFrequency"
- "getMachTimeAdjustedVoiceTriggerEventInfoForDeviceUUID:"
- "getPeakPowerForStream:forChannel:"
- "getPlaybackRouteForStream:withError:"
- "getRecordDeviceInfoForStream:"
- "getRecordSettingsForStream:"
- "handleCarCapabilitiesUpdatedWithCompletion:"
- "handleHeadUnitConnectedWithAsyncCompletion:"
- "hasConnected"
- "hasEnded"
- "hasNonVoiceTriggerStreamsActive"
- "hasPendingTwoShotBeep"
- "hearst"
- "hearstOwnership"
- "historicalBufferRequestStreams"
- "holdRequest"
- "iPhone9,1"
- "iPhone9,2"
- "iPhone9,3"
- "iPhone9,4"
- "initFileURLWithPath:isDirectory:"
- "initTandemWithOption:"
- "initTandemWithRequest:"
- "initWithAVVCRecordDeviceInfo:"
- "initWithAssetSet:queue:updateHandler:"
- "initWithAssetSet:usages:"
- "initWithAudioDeviceID:"
- "initWithAudioStreamHandleId:audioStreamType:audioRecordContext:audioRecorder:phoneCallStateMonitor:"
- "initWithBackingStoreCapacity:minimalNumberOfBackingStores:maximumNumberOfBackingStores:backingStoreIdleTimeout:"
- "initWithBool:"
- "initWithClientIdentity:"
- "initWithConfiguration:"
- "initWithDeviceId:audioStreamHandleId:"
- "initWithDouble:"
- "initWithDuckOthers:duckToLevel:mixWithOthers:"
- "initWithError:"
- "initWithLongLong:"
- "initWithMasterAudioStream:name:"
- "initWithMode:deviceUID:"
- "initWithName:clientIdentity:"
- "initWithName:clientQueue:"
- "initWithQueue:IsRemoteRecording:"
- "initWithRecordContext:deviceId:shouldUseRemoteRecorder:streamHandleId:"
- "initWithRoute:isRemoteDevice:remoteDeviceUID:remoteDeviceProductIdentifier:remoteDeviceUIDString:"
- "initWithSampleRate:withNumberOfChannels:"
- "initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:"
- "initWithStreamID:"
- "initWithStreamID:atStartHostTime:"
- "initWithStreamID:settings:bufferDuration:"
- "initWithUnsignedLongLong:"
- "initWithZeroWindowSize:approxAbsSpeechThreshold:numHostTicksPerAudioSample:"
- "inputRecordingDuration"
- "inputRecordingDurationInSecsExtended"
- "internalUserClassification"
- "invalid type specified"
- "is"
- "is not"
- "isAttachingBluetoothSession"
- "isCarPlayConnected"
- "isDefaultInputBuiltInMic"
- "isDefaultOutputBultInSpeaker"
- "isDuckingSupportedOnCurrentRouteWithStreamHandleID:error:"
- "isDuckingSupportedOnPickedRouteForStream:error:"
- "isEqualToNumber:"
- "isHeadphoneDeviceWithRecordRoute:playbackRoute:"
- "isOnHold"
- "isOutgoing"
- "isPrimaryVoiceTriggerDeviceWithUUID:"
- "isRecordContextAutoPrompt:"
- "isRecordContextBuiltInVoiceTrigger:"
- "isRecordContextDarwinVoiceTrigger:"
- "isRecordContextHearstDoubleTap:"
- "isRecordContextHearstVoiceTrigger:"
- "isRecordContextHomeButtonPress:"
- "isRecordContextJarvisButtonPress:"
- "isRecordContextJarvisVoiceTrigger:"
- "isRecordContextRaiseToSpeak:"
- "isRecordContextRemoraVoiceTrigger:"
- "isRecordContextSpeakerIdTrainingTrigger:"
- "isRecordContextVoiceTrigger:"
- "isRemoteDarwinConnectedWithUUID:"
- "isRemoteDarwinWithDeviceId:"
- "isRemoteDevice"
- "isRemoteDeviceDarwin"
- "isRemoteDeviceGibraltar"
- "isSystemProvider"
- "isTemporaryPairedNotInContacts"
- "isUpsamplingSourceAudio"
- "isValidRecordContext:"
- "isVoiceTriggerInfoAvailableLocally:"
- "isWeakStream"
- "kAFPreferencesDidChangeDarwinNotification"
- "languageCodeDarwin"
- "lastAggTimeFalseWakeUp"
- "lastAudioRecorderContext"
- "latency"
- "latencyCorrectionSeconds"
- "listeningMicIndicatorLockUUIDString"
- "listeningMicIndicatorLocks"
- "localDevice"
- "logCoreSpeechPreprocessorCompletedWithMHUUID:withMetricsDictionary:"
- "lpcmBitDepth"
- "lpcmIsFloat"
- "micUsageReporter"
- "mil"
- "missing needed values"
- "mmapModelWithConfig:mappedSizeOut:"
- "modelVersion"
- "needsBoost12dB"
- "newTriggerLengthSampleCount"
- "nil input"
- "notifyActiveStreamsChanged:streamHolders:streamId:"
- "notifyVoiceTriggerDisabledWithDeviceUUID:"
- "notifyVoiceTriggerEnabledWithDeviceUUID:"
- "numFalseWakeUp"
- "numInputChannels"
- "numberOfChannels"
- "objCType"
- "oldTriggerLengthSampleCount"
- "orderedSet"
- "outputs"
- "packetDescriptionCount"
- "packetDescriptions"
- "pairedDeviceAddresses"
- "pendingStartCompletions"
- "pendingStopCompletions"
- "persistentDomainForName:"
- "pickableRoutesDidChange:"
- "playAlertSoundForType:overrideMode:"
- "potentiallyAddHWLatencyToOption:streamHandle:voiceController:"
- "powerWithNumFalseWakeup:withDuration:withPhraseDict:"
- "predictStartAlertBehaviorFor:avSystemController:hasAOP:supportVibrator:isiOS:isWatchOS:isHorseman:isBridgeOS:recordRoute:playbackRoute:"
- "predictStartAlertBehaviorFor:recordRoute:playbackRoute:"
- "preferredExternalRouteDidChange:"
- "prepareAudioStreamWithRequest:completion:"
- "prepareRecordForStream:error:"
- "prepareRecording:"
- "primaryStream"
- "processBuffer:atTime:arrivalTimestampToAudioRecorder:"
- "provider"
- "providerDelegate"
- "providerIdentifier"
- "providerManager"
- "providerWithIdentifier:"
- "purgeCachedIrForTrialAssetExcludingCurrentAsset:cachedIrDir:"
- "q24@0:8q16"
- "q40@0:8q16@24@32"
- "q72@0:8q16@24B32B36B40B44B48B52@56@64"
- "qqaB"
- "raisetospeak"
- "readMilFilePathFromConfig:"
- "readSamplesFromChannelIdx:"
- "recordContextString:"
- "recordDeviceIndicator"
- "recordModeLockUUIDString"
- "recordModeLocks"
- "recordQueue"
- "recordingTransaction"
- "remoteAccessoryStreamIdSet"
- "remoteDeviceProductIdentifier"
- "remoteProductIdentifier"
- "remoteRecordConnectionDisconnected:"
- "remoteRecordDidStartRecordingWithStreamHandleId:error:"
- "remoteRecordDidStopRecordingWithWithStreamHandleId:error:"
- "remoteRecordLPCMBufferAvailable:streamHandleId:"
- "remoteRecordTwoShotDetectedAtTime:"
- "remoteVoiceActivityAvailable"
- "remoteVoiceActivityVAD"
- "remoteVoiceActivityVADBuffer"
- "replyDidPlayEndpointBeep"
- "replyHasPendingTwoShotBeep"
- "replyVoiceTriggerEventInfo"
- "reportDigitalZerosWithAudioZeroRun:"
- "reportMetricsForSiriRequestWithUUID:"
- "reportMicUsage:"
- "requestForLpcmRecordSettingsWithContext:"
- "requestHistoricalAudioDataSampleCount"
- "requestListeningMicIndicatorLock"
- "requestRecordModeLock"
- "requireListeningMicIndicatorLock"
- "requireRecordModeLock"
- "requireSingleChannelLookup"
- "resetDuckSettings"
- "resetWithSampleRate:"
- "routeIsDoAPSupportedWithRouteUID:withCompletion:"
- "sampleCountDelta"
- "sampleCountFromHostTime:anchorHostTime:anchorSampleCount:sampleRate:"
- "scheduledFutureSample"
- "selectedChannel"
- "serverState"
- "sessionDelegate"
- "sessionEventDelegate"
- "setAccessoryManager:"
- "setActivationMode:"
- "setAdpAssertion:"
- "setAlertDelegate:"
- "setAlertPlaybackFinishTimeoutToken:"
- "setAlertPlaybackFinishWaitingCompletions:"
- "setAlertPlaybackFinishWaitingStreams:"
- "setAlertSoundFromURL:forType:"
- "setAllowMixableAudioWhileRecording:error:"
- "setAnnounceCallsEnabled:"
- "setAnnounceCallsEnabledForStream:enable:"
- "setAnnounceMessageExceptions:"
- "setAudioPacketDeliveryCount:"
- "setAudioPacketWatchdog:"
- "setAudioPreprocessor:"
- "setAudioStreamType:"
- "setAudioSystemRecovering:"
- "setAvgPower:"
- "setBeepCanceller:"
- "setBluetoothSession:"
- "setBluetoothSessionSetupGroup:"
- "setBnnsIrForCacheMap:withMilFile:"
- "setCallObserver:"
- "setCircularBufferStartHostTime:"
- "setCircularBufferStartSampleCount:"
- "setConnectedDeviceAddresses:"
- "setContext:streamType:error:"
- "setContextForStream:forStream:error:"
- "setCurrentSessionShouldDuckOnBuiltInSpeaker:"
- "setDevice:"
- "setDeviceAddressToDeviceInfoMap:"
- "setDeviceIdentifier:"
- "setDeviceUIDMapTable:"
- "setDuckMixWithOthersForStream:duckOthers:duckToLevelInDB:mixWithOthers:"
- "setDuckOthersForStream:withSettings:error:"
- "setDuckOverride:"
- "setDuckToLevelDB:error:"
- "setEndpointMode:"
- "setFalseWakePhraseDictionary:"
- "setHasNonVoiceTriggerStreamsActive:"
- "setHistoricalBufferRequestStreams:"
- "setIAmTheAssistant:error:"
- "setIsAttachingBluetoothSession:"
- "setIsBlur:"
- "setIsTemporaryPairedNotInContacts:"
- "setLastAggTimeFalseWakeUp:"
- "setLastAudioRecorderContext:"
- "setListeningMicIndicatorLockUUIDString:"
- "setListeningMicIndicatorLocks:"
- "setListeningMicIndicatorProperty"
- "setLocalDevice:"
- "setMXSessionProperty:value:error:"
- "setMicUsageReporter:"
- "setNeedsBoost12dB:"
- "setNumFalseWakeUp:"
- "setPairedDeviceAddresses:"
- "setPeakPower:"
- "setPendingStartCompletions:"
- "setPendingStopCompletions:"
- "setPhoneCallStateMonitor:"
- "setPrimaryStream:"
- "setProviderDelegate:"
- "setRecordDelegate:"
- "setRecordDeviceIndicator:"
- "setRecordModeForStream:recordMode:error:"
- "setRecordModeLockUUIDString:"
- "setRecordModeLocks:"
- "setRecordQueue:"
- "setRecordingTransaction:"
- "setRemoteAccessoryStreamIdSet:"
- "setRtsTriggerInfo:"
- "setScheduledFutureSample:"
- "setServerCrashedBlock:"
- "setServerResetBlock:"
- "setServerState:"
- "setSessionDelegate:"
- "setSessionEventDelegate:"
- "setSkipAlert:"
- "setSplitterEnabled:"
- "setStartAlert:"
- "setStartPendingOnStoppingStreamToCompletionDict:"
- "setStartPendingOnStoppingStreams:"
- "setStartPendingStreams:"
- "setStartRecordingWatchDogToken:"
- "setStopAlert:"
- "setStopOnErrorAlert:"
- "setStopPendingStreams:"
- "setStopRecordingWatchDogToken:"
- "setStreamHandleQueue:"
- "setStreamHolders:"
- "setStreamRequest:"
- "setStreamState:"
- "setStreaming:"
- "setStreamingUUID:"
- "setStreams:"
- "setSupportDoAP:"
- "setSupportMph:"
- "setTriggerNotifiedMachTime:"
- "setTuCallCenter:"
- "setTuCallProviderManager:"
- "setTuPhoneCallState:"
- "setUpsampler:"
- "setVoiceControllerCreationQueue:"
- "setVoiceTriggerEnabledDevices:"
- "setVoiceTriggerEnabledMonitor:"
- "setWaitingForAlertFinish:"
- "setZeroCounter:"
- "sharedSession"
- "shouldUseRemoteRecorder"
- "skipAlert"
- "skipAlertBehavior"
- "softlink:r:path:/System/Library/PrivateFrameworks/CarKit.framework/CarKit"
- "softlink:r:path:/System/Library/PrivateFrameworks/MediaSafetyNet.framework/MediaSafetyNet"
- "splitterDeviceList"
- "splitterEnabled"
- "standardUserDefaults"
- "startAlert"
- "startAlertBehavior"
- "startHostTime"
- "startPendingOnStoppingStreamToCompletionDict"
- "startPendingOnStoppingStreams"
- "startPendingStreams"
- "startRecordForStream:error:"
- "startRecordingOptions"
- "startRecordingWatchDogToken"
- "startRecordingWithOptions:error:"
- "stopAlert"
- "stopAlertBehavior"
- "stopOnErrorAlert"
- "stopPendingStreams"
- "stopRecordForStream:error:"
- "stopRecording:"
- "stopRecordingWatchDogToken"
- "streamDescription"
- "streamHandleQueue"
- "streamHolders"
- "streamID"
- "streamRequest"
- "streamState"
- "streaming"
- "streamingUUID"
- "streams"
- "submitRemoteCoreSpeechIssueReport:context:"
- "successfully"
- "supportBeepCanceller:"
- "supportDoAP"
- "supportRelayCall"
- "tandemStreams"
- "teardownWithError:"
- "timeout"
- "triggerAPWakeup"
- "triggerNotifiedMachTime"
- "tuCallCenter"
- "tuCallProviderManager"
- "tuPhoneCallState"
- "twoShotDetected"
- "uid"
- "updateAudioStreamStartTimeInSampleCount:"
- "updateDeviceId:"
- "updateMeterForStream:"
- "updateWithLatestRecordContext:"
- "upsampler"
- "useCustomizedRecordSettings"
- "useOpportunisticZLL"
- "useRemoteBuiltInMic"
- "userSessionActivateMonitor:didReceivedUserSessionActiveHasChanged:"
- "v16@?0@\"CSBluetoothDeviceInfo\"8"
- "v16@?0^v8"
- "v16@?0^{BTLocalDeviceImpl=}8"
- "v20@?0I8r^{AudioObjectPropertyAddress=III}12"
- "v24@0:8@\"<CSAudioSessionEventProvidingDelegate>\"16"
- "v24@0:8@\"AVVoiceController\"16"
- "v24@0:8@\"CSAudioDeviceInfo\"16"
- "v24@0:8@\"CSRemoteRecordClient\"16"
- "v24@0:8^{BTAccessoryManagerImpl=}16"
- "v24@0:8^{BTLocalDeviceImpl=}16"
- "v24@0:8r^{__CFString=}16"
- "v24@?0^v8Q16"
- "v28@0:8@\"AVVoiceController\"16B24"
- "v28@0:8@\"AVVoiceController\"16i24"
- "v28@0:8@\"CSUserSessionActiveMonitor\"16B24"
- "v28@0:8B16@\"NSArray\"20"
- "v32@0:8@\"AVVoiceController\"16@\"AVVCAudioBuffer\"24"
- "v32@0:8@\"AVVoiceController\"16@\"NSDictionary\"24"
- "v32@0:8@\"AVVoiceController\"16@\"NSError\"24"
- "v32@0:8@\"AVVoiceController\"16Q24"
- "v32@0:8@\"AVVoiceController\"16q24"
- "v32@0:8@\"CSAudioFileReader\"16q24"
- "v32@0:8@\"CXCallObserver\"16@\"CXCall\"24"
- "v32@0:8@\"NSData\"16Q24"
- "v32@0:8Q16@\"NSError\"24"
- "v32@0:8^{BTDeviceImpl=}16@24"
- "v32@0:8f16B20@24"
- "v32@0:8i16@20B28"
- "v32@0:8q16Q24"
- "v32@?0@8Q16^B24"
- "v36@0:8@\"AVVoiceController\"16B24@\"NSError\"28"
- "v36@0:8@\"AVVoiceController\"16i24@\"NSError\"28"
- "v36@0:8@\"AVVoiceController\"16i24d28"
- "v36@0:8@\"CSAudioFileReader\"16B24@\"NSError\"28"
- "v36@0:8@16i24@28"
- "v36@0:8@16i24d28"
- "v36@0:8B16Q20@28"
- "v40@0:8@\"AVVoiceController\"16@\"AVVCAlertInformation\"24@\"NSError\"32"
- "v40@0:8@\"AVVoiceController\"16Q24@\"AVVCAudioBuffer\"32"
- "v40@0:8@\"AVVoiceController\"16Q24@\"NSError\"32"
- "v40@0:8@\"AVVoiceController\"16Q24q32"
- "v40@0:8@\"CSAudioFileReader\"16@\"NSData\"24Q32"
- "v40@0:8@\"CSBeepCanceller\"16@\"NSData\"24Q32"
- "v40@0:8@16^@24^@32"
- "v40@0:8Q16B24@28B36"
- "v44@0:8@\"AVVoiceController\"16Q24B32@\"NSError\"36"
- "v44@0:8@\"CSSpeechController\"16@\"CSAudioDeviceInfo\"24B32@\"NSError\"36"
- "v48@0:8@\"CSSpeechController\"16@\"CSAudioDeviceInfo\"24q32Q40"
- "v48@0:8@16@24@32^@40"
- "v52@0:8@\"CSAudioPreprocessor\"16@\"NSData\"24Q32Q40i48"
- "v52@0:8@\"CSSpeechController\"16@\"NSArray\"24f32Q36@\"CSAudioDeviceInfo\"44"
- "v52@0:8@16@24Q32Q40i48"
- "v60@0:8@16Q24@32Q40Q48i56"
- "v64@0:8@16Q24@32@40@48^@56"
- "voic"
- "voiceControllerAudioCallback:forStream:buffer:"
- "voiceControllerBeginRecordInterruption:"
- "voiceControllerBeginRecordInterruption:withContext:"
- "voiceControllerCreationQueue"
- "voiceControllerDidDetectEndpoint:ofType:"
- "voiceControllerDidDetectEndpoint:ofType:atTime:"
- "voiceControllerDidDetectStartpoint:"
- "voiceControllerDidFinishAlertPlayback:ofType:error:"
- "voiceControllerDidFinishAlertPlayback:withSettings:error:"
- "voiceControllerDidSetAudioSessionActive:isActivated:"
- "voiceControllerDidStartRecording:forStream:successfully:error:"
- "voiceControllerDidStartRecording:successfully:"
- "voiceControllerDidStartRecording:successfully:error:"
- "voiceControllerDidStopRecording:forReason:"
- "voiceControllerDidStopRecording:forStream:forReason:"
- "voiceControllerEncoderErrorDidOccur:error:"
- "voiceControllerEndRecordInterruption:"
- "voiceControllerEventOccurred:forStream:error:"
- "voiceControllerLPCMAudioCallback:forStream:buffer:"
- "voiceControllerLPCMRecordBufferAvailable:buffer:"
- "voiceControllerMediaServicesWereLost:"
- "voiceControllerMediaServicesWereReset:"
- "voiceControllerRecordBufferAvailable:buffer:"
- "voiceControllerRecordHardwareConfigurationDidChange:toConfiguration:"
- "voiceControllerStreamInvalidated:forStream:"
- "voiceControllerWillSetAudioSessionActive:willActivate:"
- "voiceControllerWirelessSplitterRouteAvailable:devices:"
- "voiceTriggerEnabledDevices"
- "void *CarKitLibrary(void)"
- "void *MediaSafetyNetLibrary(void)"
- "void localMSNMonitorBeginException(const char *)"
- "void localMSNMonitorEndException(const char *)"
- "void softlinked_CRFetchCarPlayCapabilities(void (^__strong)(NSDictionary *__strong, NSError *__strong))"
- "waitingForAlertFinish"
- "walkabout"
- "willBeep"
- "willBeepWithRecordRoute:playbackRoute:"
- "withElapsedTimeLogging:execute:"
- "zeroCounter"
- "zeroFilterApproxAbsSpeechThreshold"
- "zeroFilterWindowSizeInMs"
- "{AudioBufferList=\"mNumberBuffers\"I\"mBuffers\"[1{AudioBuffer=\"mNumberChannels\"I\"mDataByteSize\"I\"mData\"^v}]}"
- "\x91"
- "\xf0\x11"
- "\xf0\x121"

```
