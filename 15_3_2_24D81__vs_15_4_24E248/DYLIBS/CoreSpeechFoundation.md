## CoreSpeechFoundation

> `/System/Library/PrivateFrameworks/CoreSpeechFoundation.framework/Versions/A/CoreSpeechFoundation`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0xaae00
-  __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_methlist: 0xa270
-  __TEXT.__const: 0x7f0
+3404.82.3.0.0
+  __TEXT.__text: 0xb6774
+  __TEXT.__auth_stubs: 0x1ba0
+  __TEXT.__objc_methlist: 0xb860
+  __TEXT.__const: 0x848
+  __TEXT.__dlopen_cstrs: 0xc6
   __TEXT.__constg_swiftt: 0x240
   __TEXT.__swift5_typeref: 0x185
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x1c
-  __TEXT.__cstring: 0x11a17
+  __TEXT.__cstring: 0x12e3e
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_reflstr: 0x84
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x8
-  __TEXT.__gcc_except_tab: 0x2aec
-  __TEXT.__oslogstring: 0xc210
-  __TEXT.__dlopen_cstrs: 0xc6
-  __TEXT.__unwind_info: 0x2d90
+  __TEXT.__gcc_except_tab: 0x317c
+  __TEXT.__oslogstring: 0xcd41
+  __TEXT.__unwind_info: 0x30d0
   __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x1930
-  __TEXT.__objc_methname: 0x1d993
-  __TEXT.__objc_methtype: 0x407b
-  __TEXT.__objc_stubs: 0xebe0
-  __DATA_CONST.__got: 0xb28
-  __DATA_CONST.__const: 0xcf0
-  __DATA_CONST.__objc_classlist: 0x648
+  __TEXT.__objc_classname: 0x1a75
+  __TEXT.__objc_methname: 0x1ef62
+  __TEXT.__objc_methtype: 0x42f2
+  __TEXT.__objc_stubs: 0xf9c0
+  __DATA_CONST.__got: 0xba0
+  __DATA_CONST.__const: 0xe40
+  __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5fe0
+  __DATA_CONST.__objc_selrefs: 0x65a8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x498
-  __DATA_CONST.__objc_arraydata: 0x1a8
-  __AUTH_CONST.__auth_got: 0xdb0
-  __AUTH_CONST.__const: 0x2ee0
-  __AUTH_CONST.__cfstring: 0x8420
-  __AUTH_CONST.__objc_const: 0x12808
-  __AUTH_CONST.__objc_dictobj: 0x208
+  __DATA_CONST.__objc_superrefs: 0x4d0
+  __DATA_CONST.__objc_arraydata: 0x198
+  __AUTH_CONST.__auth_got: 0xde8
+  __AUTH_CONST.__const: 0x3190
+  __AUTH_CONST.__cfstring: 0x8640
+  __AUTH_CONST.__objc_const: 0x12160
+  __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_floatobj: 0x1b0
-  __AUTH.__objc_data: 0x4088
+  __AUTH.__objc_data: 0x4258
   __AUTH.__data: 0x2d0
-  __DATA.__objc_ivar: 0xb74
-  __DATA.__data: 0x1188
+  __DATA.__objc_ivar: 0xbfc
+  __DATA.__data: 0x1300
+  __DATA.__bss: 0xc28
   __DATA.__common: 0x68
-  __DATA.__bss: 0xbd8
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
+  - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/IOBluetooth.framework/Versions/A/IOBluetooth
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
+  - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/AssistantServices.framework/Versions/A/AssistantServices
   - /System/Library/PrivateFrameworks/AudioToolboxCore.framework/Versions/A/AudioToolboxCore
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 7A8875CE-D328-3A9A-B053-759F059892F4
-  Functions: 4275
-  Symbols:   10301
-  CStrings:  9010
+  UUID: 41884A76-B7E1-36A3-B5AB-F1C522FF4BFB
+  Functions: 4510
+  Symbols:   10858
+  CStrings:  9433
 
Symbols:
+ +[CSAssetTelemetryReporter sharedReporter]
+ +[CSAudioProviderSelectingProxy sharedContollerProxy]
+ +[CSConfig channelForVoiceIsolation]
+ +[CSFHashUtils sha1StringFromInputData:]
+ +[CSFHashUtils sha256DataFromInputData:]
+ +[CSFHashUtils sha256HashStringFromInputString:]
+ +[CSLaunchAgentXPCClient sharedClient]
+ +[CSMacUserSessionMonitor sharedInstance]
+ +[CSSystemDaemonStateMonitor sharedInstance]
+ +[CSSystemDaemonStateMonitor systemDaemonNotifyDidLaunch]
+ +[CSUtils isMagusRestrictedWithSAEForLanguageCode:]
+ +[CSUtils supportsPersonalizedHeySiri]
+ +[CSUtils supportsSecureAssetForSpeakerRecognition]
+ +[CSUtils supportsSecureSensor]
+ +[CSUtils supportsSystemDaemon]
+ +[CSUtils supportsVoiceProfileIDInUserProfile]
+ +[CSUtils(LanguageCode) getBestSupportedSiriLanguageWithFallback:]
+ +[CSUtils(machXPC) isFromActiveUserMachXPCConnection:]
+ -[CSAsset getStringForKey:]
+ -[CSAsset isCompactVersion]
+ -[CSAssetTelemetryReporter reportAssetMapFailTelemetryForError:assetSpecifier:assetConfigVersion:]
+ -[CSAssetTelemetryReporter reportAssetMapLatencyTelemetry:assetSpecifier:assetConfigVersion:]
+ -[CSAssetTelemetryReporter submitSecureAssetMapFailDiagnosticReportForError:]
+ -[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]
+ -[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]
+ -[CSAudioProvider _isAudioStreamTypeBuiltIn]
+ -[CSAudioProviderSelectingProxy .cxx_destruct]
+ -[CSAudioProviderSelectingProxy audioProviderImplementor]
+ -[CSAudioProviderSelectingProxy audioProviderWithContext:error:]
+ -[CSAudioProviderSelectingProxy audioProviderWithStreamID:]
+ -[CSAudioProviderSelectingProxy audioProviderWithUUID:]
+ -[CSAudioProviderSelectingProxy init]
+ -[CSAudioProviderSelectingProxy queue]
+ -[CSAudioProviderSelectingProxy setAudioProviderImp:]
+ -[CSAudioProviderSelectingProxy setAudioProviderImplementor:]
+ -[CSAudioProviderSelectingProxy setQueue:]
+ -[CSAudioRecordDeviceIndicator initWithRecordContext:deviceId:shouldUseRemoteRecorder:streamHandleId:shouldUseSystemDaemonRecorder:]
+ -[CSAudioRecordDeviceIndicator shouldUseSystemDaemonRecorder]
+ -[CSAudioRecorder CSSiriEnabledMonitor:didReceiveEnabled:]
+ -[CSAudioRecorder CSSystemDaemonAudioCallbackForStream:butterTimestamp:]
+ -[CSAudioRecorder CSSystemDaemonDidFinishAlertPlaybackOfType:]
+ -[CSAudioRecorder CSSystemDaemonDidStartRecordingForStream:successfully:]
+ -[CSAudioRecorder CSSystemDaemonDidStopRecordingForStream:forReason:]
+ -[CSAudioRecorder activateSecureSession:]
+ -[CSAudioRecorder currentSensorStatus]
+ -[CSAudioRecorder sensorStartForStream:]
+ -[CSAudioRecorder setListeningMicIndicatorPropertyForStream:]
+ -[CSAudioStartStreamOption enforceAutomaticEndpointing]
+ -[CSAudioStartStreamOption setEnforceAutomaticEndpointing:]
+ -[CSDiagnosticReporter submitSecureAssetIssueReport:withContext:]
+ -[CSExclaveIndicatorController _getCSFSensorStatusWithExclaveSensorStatus:]
+ -[CSExclaveIndicatorController fetchCurrentSensorStatus]
+ -[CSExclaveRecordClient audioCallbackLogHeartbeat]
+ -[CSExclaveRecordClient currentSensorStatus]
+ -[CSExclaveRecordClient reset]
+ -[CSExclaveRecordClient setAudioCallbackLogHeartbeat:]
+ -[CSFAudioChunkQueue .cxx_destruct]
+ -[CSFAudioChunkQueue addChunk:]
+ -[CSFAudioChunkQueue bufferCapacity]
+ -[CSFAudioChunkQueue circularQueue]
+ -[CSFAudioChunkQueue copyChunkFromStartSampleCount:toEndSampleCount:]
+ -[CSFAudioChunkQueue initWithBufferCapacity:]
+ -[CSFAudioChunkQueue lastSampleCount]
+ -[CSFAudioChunkQueue reset]
+ -[CSFAudioChunkQueue setBufferCapacity:]
+ -[CSFAudioChunkQueue setCircularQueue:]
+ -[CSFAudioChunkQueue setLastSampleCount:]
+ -[CSFAudioChunkQueue setTotalSampleCount:]
+ -[CSFAudioChunkQueue totalSampleCount]
+ -[CSFPreferences forceFailExclaveAssetMapping]
+ -[CSFPreferences setForceFailExclaveAssetMapping:]
+ -[CSFTimer .cxx_destruct]
+ -[CSFTimer _armTimer]
+ -[CSFTimer _disarmTimer]
+ -[CSFTimer cancel]
+ -[CSFTimer context]
+ -[CSFTimer eventHandler]
+ -[CSFTimer initWithContext:queue:eventHandler:]
+ -[CSFTimer isCancelled]
+ -[CSFTimer queue]
+ -[CSFTimer resume:]
+ -[CSFTimer setEventHandler:]
+ -[CSFTimer setTimer:]
+ -[CSFTimer timer]
+ -[CSFTimerContext .cxx_destruct]
+ -[CSFTimerContext identifier]
+ -[CSFTimerContext initTimerinterval:identifier:]
+ -[CSFTimerContext timerInterval]
+ -[CSLaunchAgentXPCClient .cxx_destruct]
+ -[CSLaunchAgentXPCClient _connectIfNeeded]
+ -[CSLaunchAgentXPCClient _decodeError:]
+ -[CSLaunchAgentXPCClient _handleAudioCallbackDelegate:]
+ -[CSLaunchAgentXPCClient _handleAudioProvidingDelegateAudioBuffer:]
+ -[CSLaunchAgentXPCClient _handleAudioProvidingDelegateMessageBody:]
+ -[CSLaunchAgentXPCClient _handleDidFinishAlertPlaybackDelegate:]
+ -[CSLaunchAgentXPCClient _handleDidStartRecordingDelegate:]
+ -[CSLaunchAgentXPCClient _handleDidStopRecordingDelegate:]
+ -[CSLaunchAgentXPCClient _handleListenerDisconnectedError:]
+ -[CSLaunchAgentXPCClient _handleListenerError:]
+ -[CSLaunchAgentXPCClient _handleListenerEvent:]
+ -[CSLaunchAgentXPCClient _handleListenerMessage:]
+ -[CSLaunchAgentXPCClient activateSecureSession:]
+ -[CSLaunchAgentXPCClient adBlockerMatchingInProgress:]
+ -[CSLaunchAgentXPCClient configAOPVoiceTrigger]
+ -[CSLaunchAgentXPCClient crashMonitorDelegate]
+ -[CSLaunchAgentXPCClient currentSensorStatus]
+ -[CSLaunchAgentXPCClient delegate]
+ -[CSLaunchAgentXPCClient fetchAOPVoiceTriggerResult:]
+ -[CSLaunchAgentXPCClient fetchAndStoreAudioBuffer]
+ -[CSLaunchAgentXPCClient initAudioRecorderWithError:]
+ -[CSLaunchAgentXPCClient init]
+ -[CSLaunchAgentXPCClient initializeSecondPass]
+ -[CSLaunchAgentXPCClient pingpong:]
+ -[CSLaunchAgentXPCClient prepareAudioRecordWithStreamHandleId:settings:error:]
+ -[CSLaunchAgentXPCClient prepare]
+ -[CSLaunchAgentXPCClient processBargeInVoiceTriggerWithResult:]
+ -[CSLaunchAgentXPCClient processSecondPassVoiceTriggerWithShouldFlushAudio:result:]
+ -[CSLaunchAgentXPCClient requestHistoricalAudioBufferFor:startSample:numSamples:hostTime:]
+ -[CSLaunchAgentXPCClient resetFirstPassVoiceTrigger]
+ -[CSLaunchAgentXPCClient sendAssetsControlMessage:errorCodeIfFailed:completion:]
+ -[CSLaunchAgentXPCClient sendMessageAndReplySync:error:]
+ -[CSLaunchAgentXPCClient sendMessageAsync:completion:]
+ -[CSLaunchAgentXPCClient sendMessageSync:]
+ -[CSLaunchAgentXPCClient setAdBlockerAsset:]
+ -[CSLaunchAgentXPCClient setAssetForLocale:isOTA:completion:]
+ -[CSLaunchAgentXPCClient setContext:]
+ -[CSLaunchAgentXPCClient setCrashMonitorDelegate:]
+ -[CSLaunchAgentXPCClient setDelegate:]
+ -[CSLaunchAgentXPCClient setRecordModeForStreamId:avvcRecordMode:error:]
+ -[CSLaunchAgentXPCClient setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:]
+ -[CSLaunchAgentXPCClient setXpcConnection:]
+ -[CSLaunchAgentXPCClient setXpcReplyQueue:]
+ -[CSLaunchAgentXPCClient setXpcRequestQueue:]
+ -[CSLaunchAgentXPCClient startAdBlockerMatching]
+ -[CSLaunchAgentXPCClient startAudioStreamWithOption:error:]
+ -[CSLaunchAgentXPCClient startBargeInVoiceTrigger]
+ -[CSLaunchAgentXPCClient startSecondPassVoiceTriggerWithFirstPassSource:enablePHS:supportMultiPhrase:activeChannel:]
+ -[CSLaunchAgentXPCClient startSecureAdBlockerMobileAssetLoaderService:]
+ -[CSLaunchAgentXPCClient startSecureMobileAssetLoaderService:completion:]
+ -[CSLaunchAgentXPCClient startSensor]
+ -[CSLaunchAgentXPCClient stopAdBlockerMatching]
+ -[CSLaunchAgentXPCClient stopAudioStreamWithError:]
+ -[CSLaunchAgentXPCClient stopBargeInVoiceTrigger]
+ -[CSLaunchAgentXPCClient stopSecondPassVoiceTrigger]
+ -[CSLaunchAgentXPCClient stopSecureAdBlockerMobileAssetLoaderService:]
+ -[CSLaunchAgentXPCClient stopSecureMobileAssetLoaderService:]
+ -[CSLaunchAgentXPCClient stopSensor]
+ -[CSLaunchAgentXPCClient xpcConnection]
+ -[CSLaunchAgentXPCClient xpcReplyQueue]
+ -[CSLaunchAgentXPCClient xpcRequestQueue]
+ -[CSMacUserSessionMonitor _handleSessionActive:]
+ -[CSMacUserSessionMonitor _handleSessionResign:]
+ -[CSMacUserSessionMonitor _notifySessionActive:]
+ -[CSMacUserSessionMonitor _registerUserSessionNotification]
+ -[CSMacUserSessionMonitor _startMonitoringWithQueue:]
+ -[CSMacUserSessionMonitor _stopMonitoring]
+ -[CSMacUserSessionMonitor _unregisterUserSessionNotification]
+ -[CSMacUserSessionMonitor init]
+ -[CSSystemDaemonStateMonitor .cxx_destruct]
+ -[CSSystemDaemonStateMonitor CSLaunchAgentXPCClientConnectionDisconnected:]
+ -[CSSystemDaemonStateMonitor _handleAgentDaemonXPCClientDisconnection]
+ -[CSSystemDaemonStateMonitor _handleSystemDaemonDidLaunchNotification]
+ -[CSSystemDaemonStateMonitor _notifyObserversSystemDaemonCrashed]
+ -[CSSystemDaemonStateMonitor _notifyObserversSystemDaemonRestartedFromCrash]
+ -[CSSystemDaemonStateMonitor _startMonitoringWithQueue:]
+ -[CSSystemDaemonStateMonitor _stopMonitoring]
+ -[CSSystemDaemonStateMonitor daemonState]
+ -[CSSystemDaemonStateMonitor init]
+ -[CSSystemDaemonStateMonitor notifyToken]
+ -[CSSystemDaemonStateMonitor queue]
+ -[CSSystemDaemonStateMonitor setDaemonState:]
+ -[CSSystemDaemonStateMonitor setNotifyToken:]
+ -[CSSystemDaemonStateMonitor setQueue:]
+ -[CSUAFAssetManager retryMappingAssetToExclaveKit:completion:]
+ -[CSUAFAssetManagerBase .cxx_destruct]
+ -[CSUAFAssetManagerBase _cancelRetryTimerForAsset:]
+ -[CSUAFAssetManagerBase _logMapFailTelemetryAndSubmitDiagnosticReportForError:assetSpecifier:assetConfigVersion:]
+ -[CSUAFAssetManagerBase _logMapOperationLatencyTelemetry:assetSpecifier:assetConfigVersion:]
+ -[CSUAFAssetManagerBase _mapAssetToExclaveKit:assetName:assetSet:completion:]
+ -[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]
+ -[CSUAFAssetManagerBase _resetRetryTimerForAsset:]
+ -[CSUAFAssetManagerBase _retryMappingAssetToExclaveKit:assetName:assetSet:completion:]
+ -[CSUAFAssetManagerBase _setAssetMapRetryTimeInterval:]
+ -[CSUAFAssetManagerBase _setMaxAssetMapRetryCount:]
+ -[CSUAFAssetManagerBase _timerForUUID:eventHandler:]
+ -[CSUAFAssetManagerBase assetMapRetryTimeInterval]
+ -[CSUAFAssetManagerBase exclaveManagerProxy]
+ -[CSUAFAssetManagerBase initWithForceSetIsExclave:exclaveManagerProxy:]
+ -[CSUAFAssetManagerBase init]
+ -[CSUAFAssetManagerBase isExclaveHardware]
+ -[CSUAFAssetManagerBase mapAssetToExclaveKit:assetName:assetSet:completion:]
+ -[CSUAFAssetManagerBase mapAssetToExclaveKit:completion:]
+ -[CSUAFAssetManagerBase maxAssetMapRetryCount]
+ -[CSUAFAssetManagerBase queue]
+ -[CSUAFAssetManagerBase retryAttemptCount]
+ -[CSUAFAssetManagerBase retryMappingAssetToExclaveKit:assetName:assetSet:completion:]
+ -[CSUAFAssetManagerBase retryMappingAssetToExclaveKit:completion:]
+ -[CSUAFAssetManagerBase retryTimers]
+ -[CSVTUITrainingSelfLogger logSiriSetupEnrollmentSessionSummaryWithSiriSetupID:lastOpenedPage:completedPage:pageAttemptsMap:]
+ -[CSVTUITrainingSelfLogger logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:didDetectSpeechStart:didUseTwoPassDetector:didFirstPassTrigger:]
+ AudioConverterFillComplexBuffer_BlockInvoke.6995
+ GCC_except_table1016
+ GCC_except_table1023
+ GCC_except_table1300
+ GCC_except_table1329
+ GCC_except_table1416
+ GCC_except_table1418
+ GCC_except_table1419
+ GCC_except_table1421
+ GCC_except_table1422
+ GCC_except_table1423
+ GCC_except_table1426
+ GCC_except_table1592
+ GCC_except_table1808
+ GCC_except_table1809
+ GCC_except_table1810
+ GCC_except_table1811
+ GCC_except_table1815
+ GCC_except_table1818
+ GCC_except_table1819
+ GCC_except_table1822
+ GCC_except_table1828
+ GCC_except_table1834
+ GCC_except_table1836
+ GCC_except_table1837
+ GCC_except_table1901
+ GCC_except_table1906
+ GCC_except_table1978
+ GCC_except_table2018
+ GCC_except_table2019
+ GCC_except_table2021
+ GCC_except_table2022
+ GCC_except_table2029
+ GCC_except_table2030
+ GCC_except_table2039
+ GCC_except_table2052
+ GCC_except_table2095
+ GCC_except_table2164
+ GCC_except_table2261
+ GCC_except_table2298
+ GCC_except_table2434
+ GCC_except_table2438
+ GCC_except_table2510
+ GCC_except_table2521
+ GCC_except_table2523
+ GCC_except_table2528
+ GCC_except_table2530
+ GCC_except_table2545
+ GCC_except_table2552
+ GCC_except_table2554
+ GCC_except_table2572
+ GCC_except_table2593
+ GCC_except_table2633
+ GCC_except_table2693
+ GCC_except_table2695
+ GCC_except_table2696
+ GCC_except_table281
+ GCC_except_table2838
+ GCC_except_table291
+ GCC_except_table2966
+ GCC_except_table2974
+ GCC_except_table2984
+ GCC_except_table2993
+ GCC_except_table2996
+ GCC_except_table2998
+ GCC_except_table2999
+ GCC_except_table3022
+ GCC_except_table3064
+ GCC_except_table3154
+ GCC_except_table3179
+ GCC_except_table3212
+ GCC_except_table3213
+ GCC_except_table3214
+ GCC_except_table3215
+ GCC_except_table3238
+ GCC_except_table3251
+ GCC_except_table3444
+ GCC_except_table350
+ GCC_except_table3500
+ GCC_except_table3501
+ GCC_except_table3534
+ GCC_except_table3535
+ GCC_except_table3537
+ GCC_except_table3540
+ GCC_except_table3541
+ GCC_except_table3542
+ GCC_except_table3562
+ GCC_except_table3565
+ GCC_except_table3567
+ GCC_except_table3568
+ GCC_except_table3569
+ GCC_except_table3571
+ GCC_except_table3604
+ GCC_except_table3606
+ GCC_except_table3607
+ GCC_except_table3608
+ GCC_except_table3609
+ GCC_except_table3666
+ GCC_except_table3714
+ GCC_except_table3720
+ GCC_except_table374
+ GCC_except_table3775
+ GCC_except_table3776
+ GCC_except_table3783
+ GCC_except_table3784
+ GCC_except_table3785
+ GCC_except_table3786
+ GCC_except_table3788
+ GCC_except_table3789
+ GCC_except_table3810
+ GCC_except_table3811
+ GCC_except_table3812
+ GCC_except_table3813
+ GCC_except_table3814
+ GCC_except_table3815
+ GCC_except_table3816
+ GCC_except_table3827
+ GCC_except_table3838
+ GCC_except_table3839
+ GCC_except_table3841
+ GCC_except_table3842
+ GCC_except_table3843
+ GCC_except_table3844
+ GCC_except_table3847
+ GCC_except_table3848
+ GCC_except_table3849
+ GCC_except_table3850
+ GCC_except_table3851
+ GCC_except_table3854
+ GCC_except_table3857
+ GCC_except_table3861
+ GCC_except_table3862
+ GCC_except_table3866
+ GCC_except_table3879
+ GCC_except_table3880
+ GCC_except_table3882
+ GCC_except_table3883
+ GCC_except_table3885
+ GCC_except_table3887
+ GCC_except_table3888
+ GCC_except_table3889
+ GCC_except_table3896
+ GCC_except_table3902
+ GCC_except_table3903
+ GCC_except_table393
+ GCC_except_table3933
+ GCC_except_table3937
+ GCC_except_table395
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table402
+ GCC_except_table4037
+ GCC_except_table4044
+ GCC_except_table405
+ GCC_except_table4144
+ GCC_except_table4214
+ GCC_except_table4226
+ GCC_except_table4231
+ GCC_except_table4266
+ GCC_except_table4332
+ GCC_except_table450
+ GCC_except_table454
+ GCC_except_table455
+ GCC_except_table456
+ GCC_except_table457
+ GCC_except_table458
+ GCC_except_table542
+ GCC_except_table652
+ GCC_except_table655
+ GCC_except_table656
+ GCC_except_table658
+ GCC_except_table662
+ GCC_except_table813
+ GCC_except_table823
+ GCC_except_table893
+ GCC_except_table916
+ GCC_except_table917
+ GCC_except_table918
+ GCC_except_table922
+ GCC_except_table923
+ GCC_except_table924
+ GCC_except_table925
+ GCC_except_table926
+ GCC_except_table928
+ GCC_except_table929
+ GCC_except_table930
+ GCC_except_table933
+ GCC_except_table934
+ GCC_except_table935
+ GCC_except_table937
+ GCC_except_table938
+ GCC_except_table939
+ GCC_except_table948
+ OBJC_IVAR_$_CSAudioProviderSelectingProxy._audioProviderImplementor
+ OBJC_IVAR_$_CSAudioProviderSelectingProxy._queue
+ OBJC_IVAR_$_CSAudioRecordDeviceIndicator._shouldUseSystemDaemonRecorder
+ OBJC_IVAR_$_CSAudioRecorder._launchAgentAudioClient
+ OBJC_IVAR_$_CSAudioStartStreamOption._enforceAutomaticEndpointing
+ OBJC_IVAR_$_CSExclaveIndicatorController._buffer_port
+ OBJC_IVAR_$_CSExclaveIndicatorController._hasStarted
+ OBJC_IVAR_$_CSExclaveIndicatorController._mem
+ OBJC_IVAR_$_CSExclaveIndicatorController._sensor_port
+ OBJC_IVAR_$_CSExclaveRecordClient._audioCallbackLogHeartbeat
+ OBJC_IVAR_$_CSExclaveRecordClient._audioProvidingProxy
+ OBJC_IVAR_$_CSFAudioChunkQueue._bufferCapacity
+ OBJC_IVAR_$_CSFAudioChunkQueue._circularQueue
+ OBJC_IVAR_$_CSFAudioChunkQueue._lastSampleCount
+ OBJC_IVAR_$_CSFAudioChunkQueue._totalSampleCount
+ OBJC_IVAR_$_CSFTimer._context
+ OBJC_IVAR_$_CSFTimer._eventHandler
+ OBJC_IVAR_$_CSFTimer._isCancelled
+ OBJC_IVAR_$_CSFTimer._queue
+ OBJC_IVAR_$_CSFTimer._timer
+ OBJC_IVAR_$_CSFTimerContext._identifier
+ OBJC_IVAR_$_CSFTimerContext._timerInterval
+ OBJC_IVAR_$_CSLaunchAgentXPCClient._crashMonitorDelegate
+ OBJC_IVAR_$_CSLaunchAgentXPCClient._delegate
+ OBJC_IVAR_$_CSLaunchAgentXPCClient._xpcConnection
+ OBJC_IVAR_$_CSLaunchAgentXPCClient._xpcReplyQueue
+ OBJC_IVAR_$_CSLaunchAgentXPCClient._xpcRequestQueue
+ OBJC_IVAR_$_CSSystemDaemonStateMonitor._daemonState
+ OBJC_IVAR_$_CSSystemDaemonStateMonitor._notifyToken
+ OBJC_IVAR_$_CSSystemDaemonStateMonitor._queue
+ OBJC_IVAR_$_CSUAFAssetManagerBase._assetMapRetryTimeInterval
+ OBJC_IVAR_$_CSUAFAssetManagerBase._exclaveManagerProxy
+ OBJC_IVAR_$_CSUAFAssetManagerBase._isExclaveHardware
+ OBJC_IVAR_$_CSUAFAssetManagerBase._maxAssetMapRetryCount
+ OBJC_IVAR_$_CSUAFAssetManagerBase._queue
+ OBJC_IVAR_$_CSUAFAssetManagerBase._retryAttemptCount
+ OBJC_IVAR_$_CSUAFAssetManagerBase._retryTimers
+ _KCSDiagnosticReporterSecureAssetKeyType
+ _NSWorkspaceSessionDidBecomeActiveNotification
+ _NSWorkspaceSessionDidResignActiveNotification
+ _OBJC_CLASS_$_CSAssetTelemetryReporter
+ _OBJC_CLASS_$_CSAudioProviderSelectingProxy
+ _OBJC_CLASS_$_CSFAudioChunkQueue
+ _OBJC_CLASS_$_CSFHashUtils
+ _OBJC_CLASS_$_CSFTimer
+ _OBJC_CLASS_$_CSFTimerContext
+ _OBJC_CLASS_$_CSLaunchAgentXPCClient
+ _OBJC_CLASS_$_CSMacUserSessionMonitor
+ _OBJC_CLASS_$_CSSecureSiriAudioProvidingProxy
+ _OBJC_CLASS_$_CSSystemDaemonStateMonitor
+ _OBJC_CLASS_$_CSUAFAssetManagerBase
+ _OBJC_CLASS_$_NSWorkspace
+ _OBJC_CLASS_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentPageAttempts
+ _OBJC_CLASS_$_SIRISETUPSchemaSIRISETUPPHSEnrollmentSessionSummary
+ _OBJC_METACLASS_$_CSAssetTelemetryReporter
+ _OBJC_METACLASS_$_CSAudioProviderSelectingProxy
+ _OBJC_METACLASS_$_CSFAudioChunkQueue
+ _OBJC_METACLASS_$_CSFHashUtils
+ _OBJC_METACLASS_$_CSFTimer
+ _OBJC_METACLASS_$_CSFTimerContext
+ _OBJC_METACLASS_$_CSLaunchAgentXPCClient
+ _OBJC_METACLASS_$_CSMacUserSessionMonitor
+ _OBJC_METACLASS_$_CSSystemDaemonStateMonitor
+ _OBJC_METACLASS_$_CSUAFAssetManagerBase
+ _SCDynamicStoreCopyConsoleUser
+ __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke.183
+ __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_2.184
+ __24-[CSAudioProvider start]_block_invoke.58
+ __24-[CSAudioProvider start]_block_invoke.60
+ __51-[CSAudioRecorder _createVoiceControllerWithError:]_block_invoke.61
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.139
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.144
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.149
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.153
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.145
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.150
+ __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.151
+ __54-[CSAudioProvider startAudioStream:option:completion:]_block_invoke.103
+ __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.132
+ __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.133
+ __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.136
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.110
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.116
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.117
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.118
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.119
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.121
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.122
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.125
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.113
+ __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.123
+ __57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.189
+ __61-[CSAlwaysOnProcessorStateMonitor _startMonitoringWithQueue:]_block_invoke.12
+ __62-[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]_block_invoke.131
+ __64-[CSAudioProvider audioStreamWithRequest:streamName:completion:]_block_invoke.88
+ __64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke.314
+ __64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke.315
+ __64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke_2.316
+ __78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.171
+ __86-[CSUAFAssetManagerBase _retryMappingAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke.309
+ __Block_byref_object_copy_.11444
+ __Block_byref_object_copy_.11825
+ __Block_byref_object_copy_.12107
+ __Block_byref_object_copy_.12359
+ __Block_byref_object_copy_.12848
+ __Block_byref_object_copy_.13348
+ __Block_byref_object_copy_.13430
+ __Block_byref_object_copy_.14136
+ __Block_byref_object_copy_.2186
+ __Block_byref_object_copy_.2581
+ __Block_byref_object_copy_.3315
+ __Block_byref_object_copy_.4508
+ __Block_byref_object_copy_.4701
+ __Block_byref_object_copy_.5460
+ __Block_byref_object_copy_.5524
+ __Block_byref_object_copy_.5968
+ __Block_byref_object_copy_.7448
+ __Block_byref_object_copy_.7707
+ __Block_byref_object_copy_.8081
+ __Block_byref_object_copy_.8858
+ __Block_byref_object_dispose_.11445
+ __Block_byref_object_dispose_.11826
+ __Block_byref_object_dispose_.12108
+ __Block_byref_object_dispose_.12360
+ __Block_byref_object_dispose_.12849
+ __Block_byref_object_dispose_.13349
+ __Block_byref_object_dispose_.13431
+ __Block_byref_object_dispose_.14137
+ __Block_byref_object_dispose_.2187
+ __Block_byref_object_dispose_.2582
+ __Block_byref_object_dispose_.3316
+ __Block_byref_object_dispose_.4509
+ __Block_byref_object_dispose_.4702
+ __Block_byref_object_dispose_.5461
+ __Block_byref_object_dispose_.5525
+ __Block_byref_object_dispose_.5969
+ __Block_byref_object_dispose_.7449
+ __Block_byref_object_dispose_.7708
+ __Block_byref_object_dispose_.8082
+ __Block_byref_object_dispose_.8859
+ __OBJC_$_CLASS_METHODS_CSAssetTelemetryReporter
+ __OBJC_$_CLASS_METHODS_CSAudioProviderSelectingProxy
+ __OBJC_$_CLASS_METHODS_CSFHashUtils
+ __OBJC_$_CLASS_METHODS_CSLaunchAgentXPCClient
+ __OBJC_$_CLASS_METHODS_CSMacUserSessionMonitor
+ __OBJC_$_CLASS_METHODS_CSSystemDaemonStateMonitor
+ __OBJC_$_INSTANCE_METHODS_CSAssetTelemetryReporter
+ __OBJC_$_INSTANCE_METHODS_CSAudioProviderSelectingProxy
+ __OBJC_$_INSTANCE_METHODS_CSFAudioChunkQueue
+ __OBJC_$_INSTANCE_METHODS_CSFTimer
+ __OBJC_$_INSTANCE_METHODS_CSFTimerContext
+ __OBJC_$_INSTANCE_METHODS_CSLaunchAgentXPCClient
+ __OBJC_$_INSTANCE_METHODS_CSMacUserSessionMonitor
+ __OBJC_$_INSTANCE_METHODS_CSSystemDaemonStateMonitor
+ __OBJC_$_INSTANCE_METHODS_CSUAFAssetManagerBase
+ __OBJC_$_INSTANCE_VARIABLES_CSAudioProviderSelectingProxy
+ __OBJC_$_INSTANCE_VARIABLES_CSExclaveIndicatorController
+ __OBJC_$_INSTANCE_VARIABLES_CSFAudioChunkQueue
+ __OBJC_$_INSTANCE_VARIABLES_CSFTimer
+ __OBJC_$_INSTANCE_VARIABLES_CSFTimerContext
+ __OBJC_$_INSTANCE_VARIABLES_CSLaunchAgentXPCClient
+ __OBJC_$_INSTANCE_VARIABLES_CSSystemDaemonStateMonitor
+ __OBJC_$_INSTANCE_VARIABLES_CSUAFAssetManagerBase
+ __OBJC_$_PROP_LIST_CSAudioProviderSelectingProxy
+ __OBJC_$_PROP_LIST_CSFAudioChunkQueue
+ __OBJC_$_PROP_LIST_CSFTimer
+ __OBJC_$_PROP_LIST_CSFTimerContext
+ __OBJC_$_PROP_LIST_CSLaunchAgentXPCClient
+ __OBJC_$_PROP_LIST_CSSystemDaemonStateMonitor
+ __OBJC_$_PROP_LIST_CSUAFAssetManagerBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioProviderSelecting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLaunchAgentXPCClientConnectionStatusDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLaunchAgentXPCClientDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriEnabledMonitorDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSystemDaemonStateMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioProviderSelecting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLaunchAgentXPCClientConnectionStatusDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLaunchAgentXPCClientDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriEnabledMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemDaemonStateMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_CSAudioProviderSelecting
+ __OBJC_$_PROTOCOL_REFS_CSLaunchAgentXPCClientConnectionStatusDelegate
+ __OBJC_$_PROTOCOL_REFS_CSLaunchAgentXPCClientDelegate
+ __OBJC_$_PROTOCOL_REFS_CSSiriEnabledMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_CSSystemDaemonStateMonitorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CSAudioProviderSelectingProxy
+ __OBJC_CLASS_PROTOCOLS_$_CSLaunchAgentXPCClient
+ __OBJC_CLASS_PROTOCOLS_$_CSSystemDaemonStateMonitor
+ __OBJC_CLASS_RO_$_CSAssetTelemetryReporter
+ __OBJC_CLASS_RO_$_CSAudioProviderSelectingProxy
+ __OBJC_CLASS_RO_$_CSFAudioChunkQueue
+ __OBJC_CLASS_RO_$_CSFHashUtils
+ __OBJC_CLASS_RO_$_CSFTimer
+ __OBJC_CLASS_RO_$_CSFTimerContext
+ __OBJC_CLASS_RO_$_CSLaunchAgentXPCClient
+ __OBJC_CLASS_RO_$_CSMacUserSessionMonitor
+ __OBJC_CLASS_RO_$_CSSystemDaemonStateMonitor
+ __OBJC_CLASS_RO_$_CSUAFAssetManagerBase
+ __OBJC_LABEL_PROTOCOL_$_CSAudioProviderSelecting
+ __OBJC_LABEL_PROTOCOL_$_CSLaunchAgentXPCClientConnectionStatusDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSLaunchAgentXPCClientDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSSiriEnabledMonitorDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSSystemDaemonStateMonitorDelegate
+ __OBJC_METACLASS_RO_$_CSAssetTelemetryReporter
+ __OBJC_METACLASS_RO_$_CSAudioProviderSelectingProxy
+ __OBJC_METACLASS_RO_$_CSFAudioChunkQueue
+ __OBJC_METACLASS_RO_$_CSFHashUtils
+ __OBJC_METACLASS_RO_$_CSFTimer
+ __OBJC_METACLASS_RO_$_CSFTimerContext
+ __OBJC_METACLASS_RO_$_CSLaunchAgentXPCClient
+ __OBJC_METACLASS_RO_$_CSMacUserSessionMonitor
+ __OBJC_METACLASS_RO_$_CSSystemDaemonStateMonitor
+ __OBJC_METACLASS_RO_$_CSUAFAssetManagerBase
+ __OBJC_PROTOCOL_$_CSAudioProviderSelecting
+ __OBJC_PROTOCOL_$_CSLaunchAgentXPCClientConnectionStatusDelegate
+ __OBJC_PROTOCOL_$_CSLaunchAgentXPCClientDelegate
+ __OBJC_PROTOCOL_$_CSSiriEnabledMonitorDelegate
+ __OBJC_PROTOCOL_$_CSSystemDaemonStateMonitorDelegate
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_6vectorINS4_IfNS_9allocatorIfEEEENS5_IS7_EEEESA_SA_EENS_4pairIT_T1_EESC_T0_SD_
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_6vectorIfNS_9allocatorIfEEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
+ __ZNKSt3__114default_deleteI21CSAudioZeroFilterImplIfEEclB8ne190102EPS2_
+ __ZNKSt3__114default_deleteIN10corespeech25CSAudioCircularBufferImplIfEEEclB8ne190102EPS3_
+ __ZNKSt3__16vectorI21bnns_graph_argument_tNS_9allocatorIS1_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN21CSAudioZeroFilterImplIfE7ZeroRunENS_9allocatorIS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIPKfNS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt16invalid_argumentC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrI18BatchBeepCancellerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI22NonlinearBeepCancellerNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__110unique_ptrI24CSAudioSpectralMeterImplNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorI21bnns_graph_argument_tEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN21CSAudioZeroFilterImplIfE7ZeroRunEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ne190102Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne190102Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ne190102IPS5_S9_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne190102IPS3_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne190102IPS3_S7_EEvT_T0_l
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEEC2B8ne190102EmRKS3_
+ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS0_IjNS_9allocatorIjEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEEC2B8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne190102IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne190102IPKfS6_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne190102IPfS5_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne190102IPhS5_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___125-[CSVTUITrainingSelfLogger logSiriSetupEnrollmentSessionSummaryWithSiriSetupID:lastOpenedPage:completedPage:pageAttemptsMap:]_block_invoke
+ ___18-[CSFTimer cancel]_block_invoke
+ ___19-[CSFTimer resume:]_block_invoke
+ ___21-[CSFTimer _armTimer]_block_invoke
+ ___35-[CSLaunchAgentXPCClient pingpong:]_block_invoke
+ ___38+[CSLaunchAgentXPCClient sharedClient]_block_invoke
+ ___38-[CSLaunchAgentXPCClient setDelegate:]_block_invoke
+ ___39-[CSAudioRecorder initWithQueue:error:]_block_invoke
+ ___41+[CSMacUserSessionMonitor sharedInstance]_block_invoke
+ ___42+[CSAssetTelemetryReporter sharedReporter]_block_invoke
+ ___42-[CSLaunchAgentXPCClient _connectIfNeeded]_block_invoke
+ ___42-[CSLaunchAgentXPCClient sendMessageSync:]_block_invoke
+ ___44+[CSSystemDaemonStateMonitor sharedInstance]_block_invoke
+ ___48-[CSMacUserSessionMonitor _notifySessionActive:]_block_invoke
+ ___51+[CSUtils isMagusRestrictedWithSAEForLanguageCode:]_block_invoke
+ ___53+[CSAudioProviderSelectingProxy sharedContollerProxy]_block_invoke
+ ___53-[CSAudioProviderSelectingProxy setAudioProviderImp:]_block_invoke
+ ___53-[CSLaunchAgentXPCClient fetchAOPVoiceTriggerResult:]_block_invoke
+ ___53-[CSLaunchAgentXPCClient fetchAOPVoiceTriggerResult:]_block_invoke_2
+ ___54-[CSLaunchAgentXPCClient sendMessageAsync:completion:]_block_invoke
+ ___54-[CSLaunchAgentXPCClient sendMessageAsync:completion:]_block_invoke_2
+ ___55-[CSAudioProviderSelectingProxy audioProviderWithUUID:]_block_invoke
+ ___56-[CSLaunchAgentXPCClient sendMessageAndReplySync:error:]_block_invoke
+ ___56-[CSSystemDaemonStateMonitor _startMonitoringWithQueue:]_block_invoke
+ ___58-[CSAudioRecorder CSSiriEnabledMonitor:didReceiveEnabled:]_block_invoke
+ ___59-[CSAudioProviderSelectingProxy audioProviderWithStreamID:]_block_invoke
+ ___62-[CSAudioRecorder CSSystemDaemonDidFinishAlertPlaybackOfType:]_block_invoke
+ ___63-[CSLaunchAgentXPCClient processBargeInVoiceTriggerWithResult:]_block_invoke
+ ___63-[CSLaunchAgentXPCClient processBargeInVoiceTriggerWithResult:]_block_invoke_2
+ ___64-[CSAudioProviderSelectingProxy audioProviderWithContext:error:]_block_invoke
+ ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke
+ ___64-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke_2
+ ___65-[CSSystemDaemonStateMonitor _notifyObserversSystemDaemonCrashed]_block_invoke
+ ___69-[CSAudioRecorder CSSystemDaemonDidStopRecordingForStream:forReason:]_block_invoke
+ ___70-[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]_block_invoke
+ ___73-[CSAudioRecorder CSSystemDaemonDidStartRecordingForStream:successfully:]_block_invoke
+ ___75-[CSSystemDaemonStateMonitor CSLaunchAgentXPCClientConnectionDisconnected:]_block_invoke
+ ___76-[CSSystemDaemonStateMonitor _notifyObserversSystemDaemonRestartedFromCrash]_block_invoke
+ ___76-[CSUAFAssetManagerBase mapAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke
+ ___76-[CSUAFAssetManagerBase mapAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke_2
+ ___77-[CSUAFAssetManagerBase _mapAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke
+ ___80-[CSLaunchAgentXPCClient sendAssetsControlMessage:errorCodeIfFailed:completion:]_block_invoke
+ ___80-[CSLaunchAgentXPCClient sendAssetsControlMessage:errorCodeIfFailed:completion:]_block_invoke_2
+ ___81-[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]_block_invoke
+ ___83-[CSLaunchAgentXPCClient processSecondPassVoiceTriggerWithShouldFlushAudio:result:]_block_invoke
+ ___83-[CSLaunchAgentXPCClient processSecondPassVoiceTriggerWithShouldFlushAudio:result:]_block_invoke_2
+ ___85-[CSUAFAssetManagerBase retryMappingAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke
+ ___86-[CSUAFAssetManagerBase _retryMappingAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke
+ ___86-[CSUAFAssetManagerBase _retryMappingAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke_2
+ ___86-[CSUAFAssetManagerBase _retryMappingAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke_3
+ ___89-[CSExclaveRecordClient requestHistoricalAudioBufferFor:startSample:numSamples:hostTime:]_block_invoke
+ ___93-[CSAssetTelemetryReporter reportAssetMapLatencyTelemetry:assetSpecifier:assetConfigVersion:]_block_invoke
+ ___98-[CSAssetTelemetryReporter reportAssetMapFailTelemetryForError:assetSpecifier:assetConfigVersion:]_block_invoke
+ ___NSDictionary0__struct
+ ___block_descriptor_40_e8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8l
+ ___block_descriptor_40_e8_32s_e20_v20?0B8"NSError"12l
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSNumber"8"NSNumber"16^B24l
+ ___block_descriptor_40_e8_32s_e8_v12?0B8l
+ ___block_descriptor_48_e8_32bs_e5_v8?0l
+ ___block_descriptor_56_e8_32s40bs_e17_v16?0"NSError"8l
+ ___block_descriptor_56_e8_32s40s48s_e19_"NSDictionary"8?0l
+ ___block_descriptor_56_e8_32s40s_e19_"NSDictionary"8?0l
+ ___block_descriptor_64_e8_32s40s48s56bs_e20_v24?0d8"NSError"16l
+ ___block_descriptor_64_ea8_32s_e11_v16?0I8I12l
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e17_v16?0"NSError"8l
+ ___block_descriptor_80_e8_32s40s48s56s64bs72w_e5_v8?0l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64b72w
+ ___copy_helper_block_e8_32s40s48s56s64s72s80b
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s
+ ___destroy_helper_block_e8_32s40s48s56s64s72w
+ __block_literal_global.10551
+ __block_literal_global.10665
+ __block_literal_global.10792
+ __block_literal_global.10906
+ __block_literal_global.10943
+ __block_literal_global.1119
+ __block_literal_global.11489
+ __block_literal_global.11926
+ __block_literal_global.12210
+ __block_literal_global.12451
+ __block_literal_global.1251
+ __block_literal_global.12757
+ __block_literal_global.13102
+ __block_literal_global.13233
+ __block_literal_global.13372
+ __block_literal_global.13628
+ __block_literal_global.13701
+ __block_literal_global.13968
+ __block_literal_global.14162
+ __block_literal_global.1501
+ __block_literal_global.1533
+ __block_literal_global.156.7842
+ __block_literal_global.1561
+ __block_literal_global.1607
+ __block_literal_global.161
+ __block_literal_global.1675
+ __block_literal_global.178
+ __block_literal_global.182
+ __block_literal_global.185
+ __block_literal_global.200
+ __block_literal_global.2172
+ __block_literal_global.2283
+ __block_literal_global.2329
+ __block_literal_global.2368
+ __block_literal_global.240
+ __block_literal_global.248
+ __block_literal_global.2599
+ __block_literal_global.2707
+ __block_literal_global.2751
+ __block_literal_global.2788
+ __block_literal_global.3073
+ __block_literal_global.3227
+ __block_literal_global.33.7932
+ __block_literal_global.3337
+ __block_literal_global.349.7756
+ __block_literal_global.3619
+ __block_literal_global.3701
+ __block_literal_global.3920
+ __block_literal_global.401
+ __block_literal_global.449
+ __block_literal_global.4536
+ __block_literal_global.454
+ __block_literal_global.459
+ __block_literal_global.4669
+ __block_literal_global.470
+ __block_literal_global.4719
+ __block_literal_global.475
+ __block_literal_global.480
+ __block_literal_global.495
+ __block_literal_global.496
+ __block_literal_global.500
+ __block_literal_global.511
+ __block_literal_global.516
+ __block_literal_global.5228
+ __block_literal_global.527
+ __block_literal_global.5311
+ __block_literal_global.535
+ __block_literal_global.5536
+ __block_literal_global.6175
+ __block_literal_global.629
+ __block_literal_global.6320
+ __block_literal_global.6387
+ __block_literal_global.6577
+ __block_literal_global.6594
+ __block_literal_global.67.7187
+ __block_literal_global.6756
+ __block_literal_global.6821
+ __block_literal_global.6924
+ __block_literal_global.6960
+ __block_literal_global.7244
+ __block_literal_global.7949
+ __block_literal_global.7965
+ __block_literal_global.8283
+ __block_literal_global.8395
+ __block_literal_global.8421
+ __block_literal_global.8574
+ __block_literal_global.8643
+ __block_literal_global.8891
+ __block_literal_global.896
+ __block_literal_global.9194
+ __block_literal_global.9324
+ __block_literal_global.9435
+ __block_literal_global.9713
+ _audit_token_to_au32
+ _dispatch_source_testcancel
+ _exclaves_audio_buffer_copyout
+ _exclaves_audio_buffer_create
+ _kCSSecureAssetMappingFailed
+ _kSiriAttAssetAdBlockerAssetName
+ _kSiriAttAssetInvocationAssetName
+ _kSiriAttAssetMetaConfigVersionKey
+ _kSiriAttAssetMetaLocaleKey
+ _kSiriAttAssetMitigationAssetName
+ _kUAFAssetMetadataAssetSpecifierKey
+ _kUAFAttentionLanguageUsageKey
+ _kUAFSiriAttentionAssetSetName
+ _objc_msgSend$CSLaunchAgentXPCClientConnectionDisconnected:
+ _objc_msgSend$CSSystemDaemonAudioCallbackForStream:butterTimestamp:
+ _objc_msgSend$CSSystemDaemonDidFinishAlertPlaybackOfType:
+ _objc_msgSend$CSSystemDaemonDidStartRecordingForStream:successfully:
+ _objc_msgSend$CSSystemDaemonDidStopRecordingForStream:forReason:
+ _objc_msgSend$CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:
+ _objc_msgSend$CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:
+ _objc_msgSend$_armTimer
+ _objc_msgSend$_cancelRetryTimerForAsset:
+ _objc_msgSend$_connectIfNeeded
+ _objc_msgSend$_disarmTimer
+ _objc_msgSend$_handleAgentDaemonXPCClientDisconnection
+ _objc_msgSend$_handleAudioCallbackDelegate:
+ _objc_msgSend$_handleAudioProvidingDelegateAudioBuffer:
+ _objc_msgSend$_handleAudioProvidingDelegateMessageBody:
+ _objc_msgSend$_handleDidFinishAlertPlaybackDelegate:
+ _objc_msgSend$_handleDidStartRecordingDelegate:
+ _objc_msgSend$_handleDidStopRecordingDelegate:
+ _objc_msgSend$_handleListenerDisconnectedError:
+ _objc_msgSend$_handleListenerMessage:
+ _objc_msgSend$_handleSystemDaemonDidLaunchNotification
+ _objc_msgSend$_isAudioStreamTypeBuiltIn
+ _objc_msgSend$_logMapFailTelemetryAndSubmitDiagnosticReportForError:assetSpecifier:assetConfigVersion:
+ _objc_msgSend$_logMapOperationLatencyTelemetry:assetSpecifier:assetConfigVersion:
+ _objc_msgSend$_mapAssetToExclaveKit:assetName:assetSet:completion:
+ _objc_msgSend$_mapVoiceTriggerAsset:asset:completion:
+ _objc_msgSend$_notifyObserversSystemDaemonCrashed
+ _objc_msgSend$_notifyObserversSystemDaemonRestartedFromCrash
+ _objc_msgSend$_notifySessionActive:
+ _objc_msgSend$_registerUserSessionNotification
+ _objc_msgSend$_resetRetryTimerForAsset:
+ _objc_msgSend$_retryMappingAssetToExclaveKit:assetName:assetSet:completion:
+ _objc_msgSend$_timerForUUID:eventHandler:
+ _objc_msgSend$_unregisterUserSessionNotification
+ _objc_msgSend$activateSecureSession:
+ _objc_msgSend$adBlockerMatchingInProgress:
+ _objc_msgSend$audioProviderWithContext:error:
+ _objc_msgSend$audioProviderWithStreamID:
+ _objc_msgSend$audioProviderWithUUID:
+ _objc_msgSend$bufferCapacity
+ _objc_msgSend$cancel
+ _objc_msgSend$circularQueue
+ _objc_msgSend$configAOPVoiceTrigger
+ _objc_msgSend$context
+ _objc_msgSend$copyBufferWithSize:
+ _objc_msgSend$currentSensorStatus
+ _objc_msgSend$exclaveHALInputNumChannelsWithDSP
+ _objc_msgSend$exclaveHALInputNumChannelsWithoutDSP
+ _objc_msgSend$exclaveIndicatorController
+ _objc_msgSend$exclaveRecordClientAudioBuffer:audioStreamHandleId:audioBuffer:hostTime:
+ _objc_msgSend$fetchAOPVoiceTriggerResult:
+ _objc_msgSend$fetchCurrentSensorStatus
+ _objc_msgSend$forceFailExclaveAssetMapping
+ _objc_msgSend$identifier
+ _objc_msgSend$init
+ _objc_msgSend$initAudioRecorderWithError:
+ _objc_msgSend$initTimerinterval:identifier:
+ _objc_msgSend$initWithContext:queue:eventHandler:
+ _objc_msgSend$initWithForceSetIsExclave:exclaveManagerProxy:
+ _objc_msgSend$initWithRecordContext:deviceId:shouldUseRemoteRecorder:streamHandleId:shouldUseSystemDaemonRecorder:
+ _objc_msgSend$initializeSecondPass
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isSiriDSPTurnedOn
+ _objc_msgSend$lastSampleCount
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$macUserSessionMonitor:sessionActive:
+ _objc_msgSend$mapAssetToExclaveKit:assetName:assetSet:completion:
+ _objc_msgSend$prepare:
+ _objc_msgSend$prepareAudioRecordWithStreamHandleId:settings:error:
+ _objc_msgSend$processBargeInVoiceTriggerWithResult:
+ _objc_msgSend$processSecondPassVoiceTriggerWithShouldFlushAudio:result:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$reportAssetMapFailTelemetryForError:assetSpecifier:assetConfigVersion:
+ _objc_msgSend$reportAssetMapLatencyTelemetry:assetSpecifier:assetConfigVersion:
+ _objc_msgSend$requestHistoricalAudioBufferWithStartSample:completion:
+ _objc_msgSend$resetFirstPassVoiceTrigger
+ _objc_msgSend$resume:
+ _objc_msgSend$retryAttemptCount
+ _objc_msgSend$retryMappingAssetToExclaveKit:assetName:assetSet:completion:
+ _objc_msgSend$retryTimers
+ _objc_msgSend$sendAssetsControlMessage:errorCodeIfFailed:completion:
+ _objc_msgSend$sendMessageAndReplySync:error:
+ _objc_msgSend$sendMessageAsync:completion:
+ _objc_msgSend$sendMessageSync:
+ _objc_msgSend$sensorStartForStream:
+ _objc_msgSend$setAdBlockerAsset:
+ _objc_msgSend$setAssetForLocale:isOTA:completion:
+ _objc_msgSend$setContext:
+ _objc_msgSend$setDidTriggerFirstPass:
+ _objc_msgSend$setEnforceAutomaticEndpointing:
+ _objc_msgSend$setLastCompletedPage:
+ _objc_msgSend$setLastOpenedPageNumber:
+ _objc_msgSend$setLastSampleCount:
+ _objc_msgSend$setListeningMicIndicatorPropertyForStream:
+ _objc_msgSend$setNumAttempts:
+ _objc_msgSend$setPageAttempts:
+ _objc_msgSend$setRecordModeForStreamId:avvcRecordMode:error:
+ _objc_msgSend$setSessionSummary:
+ _objc_msgSend$setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:
+ _objc_msgSend$setSpeechStartPointDetected:
+ _objc_msgSend$setTwoPassRecognizerUsed:
+ _objc_msgSend$sha256HashStringFromInputString:
+ _objc_msgSend$sharedReporter
+ _objc_msgSend$shouldUseSystemDaemonRecorder
+ _objc_msgSend$startAdBlockerMatching
+ _objc_msgSend$startAudioStreamWithOption:error:
+ _objc_msgSend$startBargeInVoiceTrigger
+ _objc_msgSend$startSecondPassVoiceTriggerWithStartOption:
+ _objc_msgSend$startSecureAdBlockerMobileAssetLoaderService:
+ _objc_msgSend$stopAdBlockerMatching
+ _objc_msgSend$stopAudioStreamWithError:
+ _objc_msgSend$stopBargeInVoiceTrigger
+ _objc_msgSend$stopSecondPassVoiceTrigger
+ _objc_msgSend$stopSecureAdBlockerMobileAssetLoaderService:
+ _objc_msgSend$submitSecureAssetIssueReport:withContext:
+ _objc_msgSend$submitSecureAssetMapFailDiagnosticReportForError:
+ _objc_msgSend$supportsSecureSensor
+ _objc_msgSend$supportsSystemDaemon
+ _objc_msgSend$timerInterval
+ _objc_msgSend$totalSampleCount
+ _usleep
+ _xpc_connection_get_audit_token
+ _xpc_connection_send_message_with_reply_sync
+ isMagusRestrictedWithSAEForLanguageCode:.magusRestrictedSupportedLocales
+ isMagusRestrictedWithSAEForLanguageCode:.onceToken
+ sharedClient.onceToken
+ sharedClient.sharedClient
+ sharedContollerProxy.onceToken
+ sharedContollerProxy.sharedInstance
+ sharedInstance._sharedInstance.10552
+ sharedInstance._sharedInstance.10944
+ sharedInstance._sharedInstance.1120
+ sharedInstance._sharedInstance.13234
+ sharedInstance._sharedInstance.13629
+ sharedInstance._sharedInstance.13702
+ sharedInstance._sharedInstance.3921
+ sharedInstance._sharedInstance.4670
+ sharedInstance._sharedInstance.5229
+ sharedInstance._sharedInstance.6176
+ sharedInstance._sharedInstance.6925
+ sharedInstance._sharedInstance.7245
+ sharedInstance._sharedInstance.9714
+ sharedInstance.onceToken.10550
+ sharedInstance.onceToken.10664
+ sharedInstance.onceToken.10942
+ sharedInstance.onceToken.1118
+ sharedInstance.onceToken.12209
+ sharedInstance.onceToken.13232
+ sharedInstance.onceToken.13627
+ sharedInstance.onceToken.13700
+ sharedInstance.onceToken.13967
+ sharedInstance.onceToken.14161
+ sharedInstance.onceToken.1532
+ sharedInstance.onceToken.1606
+ sharedInstance.onceToken.1674
+ sharedInstance.onceToken.2282
+ sharedInstance.onceToken.2328
+ sharedInstance.onceToken.2367
+ sharedInstance.onceToken.2598
+ sharedInstance.onceToken.3336
+ sharedInstance.onceToken.3700
+ sharedInstance.onceToken.3919
+ sharedInstance.onceToken.4535
+ sharedInstance.onceToken.4668
+ sharedInstance.onceToken.4718
+ sharedInstance.onceToken.495
+ sharedInstance.onceToken.5227
+ sharedInstance.onceToken.6174
+ sharedInstance.onceToken.628
+ sharedInstance.onceToken.6319
+ sharedInstance.onceToken.6576
+ sharedInstance.onceToken.6923
+ sharedInstance.onceToken.7243
+ sharedInstance.onceToken.7964
+ sharedInstance.onceToken.8282
+ sharedInstance.onceToken.8420
+ sharedInstance.onceToken.8642
+ sharedInstance.onceToken.9193
+ sharedInstance.onceToken.9323
+ sharedInstance.onceToken.9434
+ sharedInstance.onceToken.9712
+ sharedInstance.sharedInstance.10666
+ sharedInstance.sharedInstance.12211
+ sharedInstance.sharedInstance.13969
+ sharedInstance.sharedInstance.14163
+ sharedInstance.sharedInstance.2284
+ sharedInstance.sharedInstance.2369
+ sharedInstance.sharedInstance.2600
+ sharedInstance.sharedInstance.3338
+ sharedInstance.sharedInstance.3702
+ sharedInstance.sharedInstance.4720
+ sharedInstance.sharedInstance.497
+ sharedInstance.sharedInstance.630
+ sharedInstance.sharedInstance.6321
+ sharedInstance.sharedInstance.8284
+ sharedInstance.sharedInstance.8422
+ sharedInstance.sharedInstance.8644
+ sharedInstance.sharedInstance.9325
+ sharedInstance.sharedInstance.9436
+ sharedInstance.sharedManager.6578
+ sharedInstance.sharedManager.7966
+ sharedLogger.onceToken.12756
+ sharedLogger.onceToken.2706
+ sharedLogger.onceToken.6386
+ sharedLogger.onceToken.6593
+ sharedLogger.shared.12758
+ sharedManager.onceToken.13371
+ sharedMonitor.onceToken.5310
+ sharedMonitor.sharedMonitor.5312
+ sharedPreferences.onceToken.8394
+ sharedReporter.onceToken
+ sharedReporter.sender
+ useVoiceIsolationDictation.useVoiceIsolationForDictation
- +[CSExclaveMessageHandlingFactory exclaveEntityKitProvider]
- +[CSFSensorControlSelfLogger sharedLogger]
- -[CSAssetAvailabilityNotifierAssistant _getSettingsConnection]
- -[CSAudioRecordDeviceIndicator initWithRecordContext:deviceId:shouldUseRemoteRecorder:streamHandleId:]
- -[CSAudioRecorder sensorStart]
- -[CSAudioRecorder setListeningMicIndicatorProperty]
- -[CSExclaveRecordClient updateEntityStatistics:]
- -[CSFSensorControlSelfLogger _getMHSensorControlStatusWithCSFSensorStatus:]
- -[CSFSensorControlSelfLogger logSensorControlStartWithStatus:withMHUUID:]
- -[CSUAFAssetManager _initWithForceSetIsExclave:exclaveManagerProxy:]
- -[CSUAFAssetManager _mapAssetToExclaveKitForAssetName:asset:completion:]
- -[CSUAFAssetManager init]
- -[CSVTUITrainingSelfLogger logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:]
- AudioConverterFillComplexBuffer_BlockInvoke.6548
- GCC_except_table1262
- GCC_except_table1358
- GCC_except_table1361
- GCC_except_table1362
- GCC_except_table1363
- GCC_except_table1364
- GCC_except_table1365
- GCC_except_table1366
- GCC_except_table1384
- GCC_except_table1550
- GCC_except_table1766
- GCC_except_table1767
- GCC_except_table1768
- GCC_except_table1769
- GCC_except_table1773
- GCC_except_table1776
- GCC_except_table1777
- GCC_except_table1780
- GCC_except_table1786
- GCC_except_table1792
- GCC_except_table1794
- GCC_except_table1795
- GCC_except_table1859
- GCC_except_table1956
- GCC_except_table1957
- GCC_except_table1959
- GCC_except_table1960
- GCC_except_table1967
- GCC_except_table1968
- GCC_except_table1977
- GCC_except_table1990
- GCC_except_table2033
- GCC_except_table2160
- GCC_except_table2197
- GCC_except_table2333
- GCC_except_table2337
- GCC_except_table2405
- GCC_except_table2416
- GCC_except_table2418
- GCC_except_table2423
- GCC_except_table2425
- GCC_except_table2440
- GCC_except_table2447
- GCC_except_table2449
- GCC_except_table2467
- GCC_except_table2488
- GCC_except_table2526
- GCC_except_table2585
- GCC_except_table2587
- GCC_except_table2588
- GCC_except_table270
- GCC_except_table2728
- GCC_except_table280
- GCC_except_table2856
- GCC_except_table2864
- GCC_except_table2874
- GCC_except_table2883
- GCC_except_table2886
- GCC_except_table2888
- GCC_except_table2889
- GCC_except_table2912
- GCC_except_table2953
- GCC_except_table3068
- GCC_except_table3100
- GCC_except_table3101
- GCC_except_table3102
- GCC_except_table3103
- GCC_except_table3125
- GCC_except_table3271
- GCC_except_table3335
- GCC_except_table3349
- GCC_except_table3383
- GCC_except_table3386
- GCC_except_table3389
- GCC_except_table3390
- GCC_except_table3391
- GCC_except_table3411
- GCC_except_table3414
- GCC_except_table3416
- GCC_except_table3417
- GCC_except_table3418
- GCC_except_table3420
- GCC_except_table3453
- GCC_except_table3455
- GCC_except_table3456
- GCC_except_table3457
- GCC_except_table3549
- GCC_except_table3555
- GCC_except_table3610
- GCC_except_table3611
- GCC_except_table3618
- GCC_except_table3619
- GCC_except_table3620
- GCC_except_table3621
- GCC_except_table3623
- GCC_except_table3624
- GCC_except_table363
- GCC_except_table3633
- GCC_except_table3634
- GCC_except_table3636
- GCC_except_table3637
- GCC_except_table3639
- GCC_except_table3641
- GCC_except_table3642
- GCC_except_table3643
- GCC_except_table3650
- GCC_except_table3652
- GCC_except_table3656
- GCC_except_table3657
- GCC_except_table3687
- GCC_except_table3691
- GCC_except_table3791
- GCC_except_table3798
- GCC_except_table382
- GCC_except_table383
- GCC_except_table384
- GCC_except_table385
- GCC_except_table386
- GCC_except_table391
- GCC_except_table3968
- GCC_except_table3985
- GCC_except_table443
- GCC_except_table444
- GCC_except_table445
- GCC_except_table446
- GCC_except_table447
- GCC_except_table529
- GCC_except_table635
- GCC_except_table638
- GCC_except_table639
- GCC_except_table641
- GCC_except_table645
- GCC_except_table786
- GCC_except_table795
- GCC_except_table865
- GCC_except_table866
- GCC_except_table873
- GCC_except_table888
- GCC_except_table889
- GCC_except_table890
- GCC_except_table895
- GCC_except_table896
- GCC_except_table897
- GCC_except_table898
- GCC_except_table900
- GCC_except_table902
- GCC_except_table905
- GCC_except_table906
- GCC_except_table907
- GCC_except_table909
- GCC_except_table910
- GCC_except_table911
- GCC_except_table920
- GCC_except_table985
- GCC_except_table992
- OBJC_IVAR_$_CSUAFAssetManager._exclaveManagerProxy
- OBJC_IVAR_$_CSUAFAssetManager._isExclaveHardware
- OBJC_IVAR_$_CSUAFAssetManager._queue
- _OBJC_CLASS_$_CSFSensorControlSelfLogger
- _OBJC_CLASS_$_MHSchemaMHSensorControlStatusReported
- _OBJC_METACLASS_$_CSFSensorControlSelfLogger
- __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke.170
- __141-[CSAudioProvider audioRecorderBufferAvailable:audioStreamHandleId:buffer:remoteVAD:atTime:arrivalTimestampToAudioRecorder:numberOfChannels:]_block_invoke_2.171
- __24-[CSAudioProvider start]_block_invoke.51
- __24-[CSAudioProvider start]_block_invoke.53
- __51-[CSAudioRecorder _createVoiceControllerWithError:]_block_invoke.60
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.126
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.131
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.136
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke.140
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.132
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_2.137
- __54-[CSAudioProvider _stopAudioStream:option:completion:]_block_invoke_3.138
- __54-[CSAudioProvider startAudioStream:option:completion:]_block_invoke.90
- __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.119
- __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.120
- __55-[CSAudioProvider _handleDidStopAudioStreamWithReason:]_block_invoke.123
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.103
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.104
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.105
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.108
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.93
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.96
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.97
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke.99
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.100
- __55-[CSAudioProvider _startAudioStream:option:completion:]_block_invoke_2.110
- __57-[CSAudioProvider _didReceiveFinishStartAlertPlaybackAt:]_block_invoke.176
- __61-[CSAlwaysOnProcessorStateMonitor _startMonitoringWithQueue:]_block_invoke.7
- __62-[CSAudioProvider _handleDidStartAudioStreamWithResult:error:]_block_invoke.118
- __64-[CSAudioProvider audioStreamWithRequest:streamName:completion:]_block_invoke.75
- __72-[CSUAFAssetManager _mapAssetToExclaveKitForAssetName:asset:completion:]_block_invoke.378
- __72-[CSUAFAssetManager _mapAssetToExclaveKitForAssetName:asset:completion:]_block_invoke.379
- __72-[CSUAFAssetManager _mapAssetToExclaveKitForAssetName:asset:completion:]_block_invoke_2.380
- __78-[CSAudioProvider playRecordStartingAlertAndResetEndpointerWithAlertOverride:]_block_invoke.158
- __Block_byref_object_copy_.10875
- __Block_byref_object_copy_.11263
- __Block_byref_object_copy_.11512
- __Block_byref_object_copy_.12002
- __Block_byref_object_copy_.12504
- __Block_byref_object_copy_.12586
- __Block_byref_object_copy_.13293
- __Block_byref_object_copy_.2139
- __Block_byref_object_copy_.2534
- __Block_byref_object_copy_.3241
- __Block_byref_object_copy_.4386
- __Block_byref_object_copy_.4582
- __Block_byref_object_copy_.5327
- __Block_byref_object_copy_.5734
- __Block_byref_object_copy_.7008
- __Block_byref_object_copy_.7254
- __Block_byref_object_copy_.7636
- __Block_byref_object_copy_.8407
- __Block_byref_object_dispose_.10876
- __Block_byref_object_dispose_.11264
- __Block_byref_object_dispose_.11513
- __Block_byref_object_dispose_.12003
- __Block_byref_object_dispose_.12505
- __Block_byref_object_dispose_.12587
- __Block_byref_object_dispose_.13294
- __Block_byref_object_dispose_.2140
- __Block_byref_object_dispose_.2535
- __Block_byref_object_dispose_.3242
- __Block_byref_object_dispose_.4387
- __Block_byref_object_dispose_.4583
- __Block_byref_object_dispose_.5328
- __Block_byref_object_dispose_.5735
- __Block_byref_object_dispose_.7009
- __Block_byref_object_dispose_.7255
- __Block_byref_object_dispose_.7637
- __Block_byref_object_dispose_.8408
- __OBJC_$_CLASS_METHODS_CSFSensorControlSelfLogger
- __OBJC_$_INSTANCE_METHODS_CSFSensorControlSelfLogger
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSExclaveEntityKitProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSExclaveEntityKitProviding
- __OBJC_$_PROTOCOL_REFS_CSExclaveEntityKitProviding
- __OBJC_CLASS_RO_$_CSFSensorControlSelfLogger
- __OBJC_LABEL_PROTOCOL_$_CSExclaveEntityKitProviding
- __OBJC_METACLASS_RO_$_CSFSensorControlSelfLogger
- __OBJC_PROTOCOL_$_CSExclaveEntityKitProviding
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPNS_6vectorINS4_IfNS_9allocatorIfEEEENS5_IS7_EEEESA_SA_EENS_4pairIT_T1_EESC_T0_SD_
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPNS_6vectorIfNS_9allocatorIfEEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
- __ZNKSt3__114default_deleteI21CSAudioZeroFilterImplIfEEclB8ne180100EPS2_
- __ZNKSt3__114default_deleteIN10corespeech25CSAudioCircularBufferImplIfEEEclB8ne180100EPS3_
- __ZNKSt3__16vectorI21bnns_graph_argument_tNS_9allocatorIS1_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN21CSAudioZeroFilterImplIfE7ZeroRunENS_9allocatorIS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPKfNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIhNS_9allocatorIhEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt16invalid_argumentC1B8ne180100EPKc
- __ZNSt3__110unique_ptrI18BatchBeepCancellerNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI22NonlinearBeepCancellerNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_
- __ZNSt3__110unique_ptrI24CSAudioSpectralMeterImplNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorI21bnns_graph_argument_tEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN21CSAudioZeroFilterImplIfE7ZeroRunEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne180100Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ne180100IPS5_S9_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne180100IPS3_S7_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne180100IPS3_S7_EEvT_T0_l
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEEC2EmRKS3_
- __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS0_IhNS_9allocatorIhEEEENS1_IS3_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS0_IjNS_9allocatorIjEEEENS1_IS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEEC2Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne180100IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne180100IPKfS6_EEvT_T0_l
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne180100IPfS5_EEvT_T0_l
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2EmRKf
- __ZNSt3__16vectorIhNS_9allocatorIhEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIhNS_9allocatorIhEEE16__init_with_sizeB8ne180100IPhS5_EEvT_T0_m
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___42+[CSFSensorControlSelfLogger sharedLogger]_block_invoke
- ___72-[CSUAFAssetManager _mapAssetToExclaveKitForAssetName:asset:completion:]_block_invoke
- ___72-[CSUAFAssetManager _mapAssetToExclaveKitForAssetName:asset:completion:]_block_invoke_2
- ___block_descriptor_48_e8_32s40s_e8_v12?0i8l
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8l
- __block_literal_global.10035
- __block_literal_global.10149
- __block_literal_global.10276
- __block_literal_global.10389
- __block_literal_global.10426
- __block_literal_global.1087
- __block_literal_global.10920
- __block_literal_global.11363
- __block_literal_global.11602
- __block_literal_global.11908
- __block_literal_global.1221
- __block_literal_global.12258
- __block_literal_global.12389
- __block_literal_global.12528
- __block_literal_global.12783
- __block_literal_global.12856
- __block_literal_global.13125
- __block_literal_global.13319
- __block_literal_global.1470
- __block_literal_global.1502
- __block_literal_global.1522
- __block_literal_global.156.7397
- __block_literal_global.1568
- __block_literal_global.1636
- __block_literal_global.165
- __block_literal_global.173
- __block_literal_global.177
- __block_literal_global.195
- __block_literal_global.2126
- __block_literal_global.2239
- __block_literal_global.2285
- __block_literal_global.2324
- __block_literal_global.238
- __block_literal_global.244
- __block_literal_global.2552
- __block_literal_global.2658
- __block_literal_global.2684
- __block_literal_global.2721
- __block_literal_global.2999
- __block_literal_global.3153
- __block_literal_global.3263
- __block_literal_global.33.7486
- __block_literal_global.349.7303
- __block_literal_global.3536
- __block_literal_global.3618
- __block_literal_global.3833
- __block_literal_global.393
- __block_literal_global.4414
- __block_literal_global.446
- __block_literal_global.451
- __block_literal_global.4550
- __block_literal_global.456
- __block_literal_global.4600
- __block_literal_global.467
- __block_literal_global.472
- __block_literal_global.477
- __block_literal_global.492
- __block_literal_global.497
- __block_literal_global.508
- __block_literal_global.5095
- __block_literal_global.513
- __block_literal_global.5178
- __block_literal_global.524
- __block_literal_global.532
- __block_literal_global.5941
- __block_literal_global.598
- __block_literal_global.6052
- __block_literal_global.6266
- __block_literal_global.6283
- __block_literal_global.6371
- __block_literal_global.6478
- __block_literal_global.6514
- __block_literal_global.67.6737
- __block_literal_global.6794
- __block_literal_global.7504
- __block_literal_global.7520
- __block_literal_global.7835
- __block_literal_global.7947
- __block_literal_global.7973
- __block_literal_global.8121
- __block_literal_global.8191
- __block_literal_global.8440
- __block_literal_global.863
- __block_literal_global.8741
- __block_literal_global.8871
- __block_literal_global.8982
- __block_literal_global.9254
- __block_literal_global.9603
- _kUAFAttentionAssetSetName
- _keypath_getTm
- _keypath_setTm
- _objc_msgSend$_getMHSensorControlStatusWithCSFSensorStatus:
- _objc_msgSend$_initWithForceSetIsExclave:exclaveManagerProxy:
- _objc_msgSend$_mapAssetToExclaveKitForAssetName:asset:completion:
- _objc_msgSend$assetVariant
- _objc_msgSend$initWithRecordContext:deviceId:shouldUseRemoteRecorder:streamHandleId:
- _objc_msgSend$logSensorControlStartWithStatus:withMHUUID:
- _objc_msgSend$setListeningMicIndicatorProperty
- _objc_msgSend$setSensorControlStatus:
- _objc_msgSend$setSensorControlStatusReported:
- isMagusDisabledForLanguageCode:.magusNotSupportedLocales
- keypath_get.3Tm
- keypath_get.5Tm
- keypath_set.4Tm
- keypath_set.6Tm
- sharedInstance._sharedInstance.10036
- sharedInstance._sharedInstance.10427
- sharedInstance._sharedInstance.1088
- sharedInstance._sharedInstance.12390
- sharedInstance._sharedInstance.12784
- sharedInstance._sharedInstance.12857
- sharedInstance._sharedInstance.3834
- sharedInstance._sharedInstance.4551
- sharedInstance._sharedInstance.5096
- sharedInstance._sharedInstance.5942
- sharedInstance._sharedInstance.6479
- sharedInstance._sharedInstance.6795
- sharedInstance._sharedInstance.9255
- sharedInstance.onceToken.10034
- sharedInstance.onceToken.10148
- sharedInstance.onceToken.10425
- sharedInstance.onceToken.1086
- sharedInstance.onceToken.11362
- sharedInstance.onceToken.12388
- sharedInstance.onceToken.12782
- sharedInstance.onceToken.12855
- sharedInstance.onceToken.13124
- sharedInstance.onceToken.13318
- sharedInstance.onceToken.1501
- sharedInstance.onceToken.1567
- sharedInstance.onceToken.1635
- sharedInstance.onceToken.2238
- sharedInstance.onceToken.2284
- sharedInstance.onceToken.2323
- sharedInstance.onceToken.2551
- sharedInstance.onceToken.3262
- sharedInstance.onceToken.3617
- sharedInstance.onceToken.3832
- sharedInstance.onceToken.4413
- sharedInstance.onceToken.4549
- sharedInstance.onceToken.4599
- sharedInstance.onceToken.5094
- sharedInstance.onceToken.5940
- sharedInstance.onceToken.597
- sharedInstance.onceToken.6265
- sharedInstance.onceToken.6477
- sharedInstance.onceToken.6793
- sharedInstance.onceToken.7519
- sharedInstance.onceToken.7834
- sharedInstance.onceToken.7972
- sharedInstance.onceToken.8190
- sharedInstance.onceToken.8740
- sharedInstance.onceToken.8870
- sharedInstance.onceToken.8981
- sharedInstance.onceToken.9253
- sharedInstance.sharedInstance.10150
- sharedInstance.sharedInstance.11364
- sharedInstance.sharedInstance.13126
- sharedInstance.sharedInstance.13320
- sharedInstance.sharedInstance.2240
- sharedInstance.sharedInstance.2325
- sharedInstance.sharedInstance.2553
- sharedInstance.sharedInstance.3264
- sharedInstance.sharedInstance.3619
- sharedInstance.sharedInstance.4601
- sharedInstance.sharedInstance.599
- sharedInstance.sharedInstance.7836
- sharedInstance.sharedInstance.7974
- sharedInstance.sharedInstance.8192
- sharedInstance.sharedInstance.8872
- sharedInstance.sharedInstance.8983
- sharedInstance.sharedManager.6267
- sharedInstance.sharedManager.7521
- sharedLogger.onceToken.11907
- sharedLogger.onceToken.2657
- sharedLogger.onceToken.6051
- sharedLogger.onceToken.6282
- sharedLogger.onceToken.9602
- sharedLogger.shared.11909
- sharedLogger.sharedLogger
- sharedManager.onceToken.12527
- sharedMonitor.onceToken.5177
- sharedMonitor.sharedMonitor.5179
- sharedPreferences.onceToken.7946
- useVoiceIsolationDictation.useVoiceIsolateionDictation
CStrings:
+ "%s AOP listening property on notification : %{public}d"
+ "%s Assets are nil!"
+ "%s CSAudioProvider[%{public}@]:Entering dispatch group for recordingWillStartGroup when CSAudioProviderStreamStateStarting"
+ "%s CSAudioProvider[%{public}@]:Entering dispatch group for recordingWillStartGroup when CSAudioProviderStreamStateStreaming"
+ "%s CSAudioProvider[%{public}@]:Entering dispatch group for recordingWillStartGroup, stream is started"
+ "%s CSAudioProvider[%{public}@]:corespeechd_system crashed"
+ "%s CSAudioProvider[%{public}@]:corespeechd_system recovered from crash"
+ "%s Calling AVVC in system daemon stopRecordForStream"
+ "%s Calling AVVC setRecordMode to mode : %{public}@, streamId: %{public}lu"
+ "%s Calling AVVC startRecordForStream in system daemon : %{public}@"
+ "%s Cannot access to %{public}@"
+ "%s Cannot handle nil message"
+ "%s Exclave Mapping Not supported assetName: %@"
+ "%s Failed EIC audio buffer creation"
+ "%s Failed EIC buffer copy : %d"
+ "%s Failed to config AOP VoiceTrigger"
+ "%s Failed to create audio recorder in system daemon : %{public}@"
+ "%s Failed with error %{public}@"
+ "%s Failed!!!"
+ "%s Generated core analytics payload for assetName: %@, assetConfigVersion: %@, asset map latency:%f"
+ "%s Generated core analytics payload for assetName: %@, assetConfigVersion: %@, errorDomain:%@ errorCode: %ld"
+ "%s Initializing new xpcConnection"
+ "%s Internal Build: Setting to force fail asset mapping is enabled"
+ "%s Invalid context!!"
+ "%s Invalid raw audio buffer"
+ "%s Invalid streamId or settings!!"
+ "%s Invalid streamId!!"
+ "%s LaunchAgentXPCAudioProvidingDelegate messageType : %{public}lld"
+ "%s Mapping asset %@ to ExclaveKit completed in %f second(s) with error %@"
+ "%s Notifying SystemDaemon launched"
+ "%s Prepare CSExclaveRecordClient"
+ "%s Preparing Audio record in System Daemon"
+ "%s Query value for listening property in AOP : %{public}d"
+ "%s Retrying to mapping asset %@ to ExclaveKit"
+ "%s Session summary - lastOpenedPage: %d, lastCompletedPage: %d attemptMap: %@"
+ "%s Siri enabled : %{public}d"
+ "%s Skipping retry to map asset as the operation is not supported."
+ "%s Start monitoring : AOP Listening state"
+ "%s Start monitoring : corespeechd_system crash / recover event"
+ "%s Start sensor with status: %lu"
+ "%s This call is unexpected in macOS"
+ "%s Unexpected audio callback received!!"
+ "%s Unexpected message type : %{public}lld"
+ "%s Unexpected type : %{public}lld"
+ "%s XPC connection not existing, return result as failed"
+ "%s XPC connection not existing, return trigger-length as 0"
+ "%s [%@] Canceling timer"
+ "%s [%@] Mapping asset type: %ld into exclave"
+ "%s [%@] Not resuming timer in cancelled state"
+ "%s [%@] Resuming timer"
+ "%s [%@] Timer resumed:%d"
+ "%s audioRecorderDidStopRecord! audioStreamHandleId: %lu, self->_audioStreamHandleId: %lu, stopReason: %lu"
+ "%s fetch current status: %lu"
+ "%s heartbeat = %llu. startSampleCount: %llu. hostTime: %llu"
+ "%s invalid call for systemDaemon not supported platforms"
+ "%s logSiriSetupPHSEnrollmentDigitalZero, setupID: %@, pageNumber: %d, phID: %@, maxZeros: %d, maxAllowed: %d, isOverThreshold: %d locale: %@, assetConfigVersion: %@, sessionStatus: %u, didDetectSpeechStart: %d, didUseTwoPassDetector: %d, didFirstPassTrigger: %d"
+ "%s shouldUseSystemDaemon? %@"
+ "%s startAudioStream failed due to invalid MicIndicator status"
+ "%s stop monitoring : corespeechd_system crash / recover event"
+ "%s stop sensor with status: %lu"
+ "%s this call is not supported on MacOS"
+ "+[CSSystemDaemonStateMonitor systemDaemonNotifyDidLaunch]"
+ "+[CSUtils(LanguageCode) getBestSupportedSiriLanguageWithFallback:]"
+ "-[CSAlwaysOnProcessorStateMonitor _startMonitoringWithQueue:]"
+ "-[CSAsset getStringForKey:]"
+ "-[CSAssetTelemetryReporter reportAssetMapFailTelemetryForError:assetSpecifier:assetConfigVersion:]_block_invoke"
+ "-[CSAssetTelemetryReporter reportAssetMapLatencyTelemetry:assetSpecifier:assetConfigVersion:]_block_invoke"
+ "-[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]"
+ "-[CSAudioProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]"
+ "-[CSAudioProvider _setLatestRecordContext:]"
+ "-[CSAudioProvider audioRecorderDidStopRecord:audioStreamHandleId:reason:]_block_invoke"
+ "-[CSAudioRecorder CSSiriEnabledMonitor:didReceiveEnabled:]"
+ "-[CSAudioRecorder CSSystemDaemonAudioCallbackForStream:butterTimestamp:]"
+ "-[CSAudioRecorder activateSecureSession:]"
+ "-[CSExclaveIndicatorController copyBufferWithSize:]"
+ "-[CSExclaveIndicatorController init]"
+ "-[CSExclaveRecordClient configAOPVoiceTrigger]"
+ "-[CSExclaveRecordClient currentSensorStatus]"
+ "-[CSExclaveRecordClient fetchAOPVoiceTriggerResult:]"
+ "-[CSExclaveRecordClient prepare]"
+ "-[CSExclaveRecordClient requestHistoricalAudioBufferFor:startSample:numSamples:hostTime:]"
+ "-[CSExclaveRecordClient requestHistoricalAudioBufferFor:startSample:numSamples:hostTime:]_block_invoke"
+ "-[CSExclaveRecordClient startSensor]"
+ "-[CSExclaveRecordClient stopSensor]"
+ "-[CSFTimer _armTimer]"
+ "-[CSFTimer _disarmTimer]"
+ "-[CSFTimer initWithContext:queue:eventHandler:]"
+ "-[CSFTimerContext initTimerinterval:identifier:]"
+ "-[CSLaunchAgentXPCClient _connectIfNeeded]"
+ "-[CSLaunchAgentXPCClient _handleAudioProvidingDelegateAudioBuffer:]"
+ "-[CSLaunchAgentXPCClient _handleAudioProvidingDelegateMessageBody:]"
+ "-[CSLaunchAgentXPCClient _handleListenerError:]"
+ "-[CSLaunchAgentXPCClient _handleListenerEvent:]"
+ "-[CSLaunchAgentXPCClient _handleListenerMessage:]"
+ "-[CSLaunchAgentXPCClient activateSecureSession:]"
+ "-[CSLaunchAgentXPCClient adBlockerMatchingInProgress:]"
+ "-[CSLaunchAgentXPCClient currentSensorStatus]"
+ "-[CSLaunchAgentXPCClient fetchAOPVoiceTriggerResult:]_block_invoke"
+ "-[CSLaunchAgentXPCClient fetchAndStoreAudioBuffer]"
+ "-[CSLaunchAgentXPCClient initAudioRecorderWithError:]"
+ "-[CSLaunchAgentXPCClient initializeSecondPass]"
+ "-[CSLaunchAgentXPCClient prepareAudioRecordWithStreamHandleId:settings:error:]"
+ "-[CSLaunchAgentXPCClient prepare]"
+ "-[CSLaunchAgentXPCClient processBargeInVoiceTriggerWithResult:]_block_invoke"
+ "-[CSLaunchAgentXPCClient processSecondPassVoiceTriggerWithShouldFlushAudio:result:]_block_invoke"
+ "-[CSLaunchAgentXPCClient sendAssetsControlMessage:errorCodeIfFailed:completion:]_block_invoke"
+ "-[CSLaunchAgentXPCClient setAdBlockerAsset:]"
+ "-[CSLaunchAgentXPCClient setContext:]"
+ "-[CSLaunchAgentXPCClient setDelegate:]"
+ "-[CSLaunchAgentXPCClient setRecordModeForStreamId:avvcRecordMode:error:]"
+ "-[CSLaunchAgentXPCClient setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:]"
+ "-[CSLaunchAgentXPCClient startAdBlockerMatching]"
+ "-[CSLaunchAgentXPCClient startAudioStreamWithOption:error:]"
+ "-[CSLaunchAgentXPCClient startSecureAdBlockerMobileAssetLoaderService:]"
+ "-[CSLaunchAgentXPCClient startSensor]"
+ "-[CSLaunchAgentXPCClient stopAdBlockerMatching]"
+ "-[CSLaunchAgentXPCClient stopAudioStreamWithError:]"
+ "-[CSLaunchAgentXPCClient stopSecureAdBlockerMobileAssetLoaderService:]"
+ "-[CSLaunchAgentXPCClient stopSensor]"
+ "-[CSSystemDaemonStateMonitor _startMonitoringWithQueue:]"
+ "-[CSSystemDaemonStateMonitor _stopMonitoring]"
+ "-[CSUAFAssetManager retryMappingAssetToExclaveKit:completion:]"
+ "-[CSUAFAssetManagerBase _mapAssetToExclaveKit:assetName:assetSet:completion:]"
+ "-[CSUAFAssetManagerBase _mapVoiceTriggerAsset:asset:completion:]_block_invoke_2"
+ "-[CSUAFAssetManagerBase _retryMappingAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke"
+ "-[CSUAFAssetManagerBase mapAssetToExclaveKit:assetName:assetSet:completion:]_block_invoke_2"
+ "-[CSVTUITrainingSelfLogger logSiriSetupEnrollmentSessionSummaryWithSiriSetupID:lastOpenedPage:completedPage:pageAttemptsMap:]"
+ "-[CSVTUITrainingSelfLogger logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:didDetectSpeechStart:didUseTwoPassDetector:didFirstPassTrigger:]"
+ "@\"<CSAudioProviderSelecting>\""
+ "@\"<CSExclaveAudioProvidingDelegate><CSLaunchAgentXPCClientDelegate>\""
+ "@\"<CSLaunchAgentXPCClientConnectionStatusDelegate>\""
+ "@\"CSAudioProvider\"24@0:8@\"NSString\"16"
+ "@\"CSAudioProvider\"24@0:8Q16"
+ "@\"CSAudioProvider\"32@0:8@\"CSAudioRecordContext\"16^@24"
+ "@\"CSFTimerContext\""
+ "@\"CSLaunchAgentXPCClient\""
+ "@\"CSSecureSiriAudioProvidingProxy\""
+ "@32@0:8d16@24"
+ "@40@0:8@16@24@?32"
+ "@48@0:8@16@24B32Q36B44"
+ "AOPLateTrigger"
+ "AOPTriggerLength"
+ "APResultTriggerBestChannel"
+ "APResultTriggerTimestamp"
+ "APResultType"
+ "B40@0:8Q16@24^@32"
+ "CSAssetTelemetryReporter"
+ "CSAudioProviderSelecting"
+ "CSAudioProviderSelectingProxy"
+ "CSExclaveLaunchAgentXPCClient Reply Queue"
+ "CSExclaveLaunchAgentXPCClient Request Queue"
+ "CSFAudioChunkQueue"
+ "CSFAudioProviderController"
+ "CSFHashUtils"
+ "CSFTimer"
+ "CSFTimer.m"
+ "CSFTimerContext"
+ "CSLaunchAgentXPCClient"
+ "CSLaunchAgentXPCClientConnectionDisconnected:"
+ "CSLaunchAgentXPCClientConnectionStatusDelegate"
+ "CSLaunchAgentXPCClientDelegate"
+ "CSMacUserSessionMonitor"
+ "CSSiriEnabledMonitorDelegate"
+ "CSSystemDaemonAudioCallbackForStream:butterTimestamp:"
+ "CSSystemDaemonDidFinishAlertPlaybackOfType:"
+ "CSSystemDaemonDidStartRecordingForStream:successfully:"
+ "CSSystemDaemonDidStopRecordingForStream:forReason:"
+ "CSSystemDaemonStateMonitor"
+ "CSSystemDaemonStateMonitor queue"
+ "CSSystemDaemonStateMonitorDelegate"
+ "CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:"
+ "CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:"
+ "CSUAFAssetManagerBase"
+ "ErrorCode"
+ "ErrorDomain"
+ "Exclave asset mapping is not supported on this asset"
+ "Failed to map asset of type %ld after %ld retries"
+ "Force Fail Exclave Asset Mapping"
+ "Internal Build: Setting to force fail asset mapping is enabled"
+ "Mapping_Secure_Asset"
+ "No"
+ "SecureAsset"
+ "T@\"<CSAudioProviderSelecting>\",&,N,V_audioProviderImplementor"
+ "T@\"<CSExclaveAudioProvidingDelegate><CSLaunchAgentXPCClientDelegate>\",W,N,V_delegate"
+ "T@\"<CSLaunchAgentXPCClientConnectionStatusDelegate>\",W,N,V_crashMonitorDelegate"
+ "T@\"CSExclaveAssetManagerProxy\",R,N,V_exclaveManagerProxy"
+ "T@\"CSFTimerContext\",R,N,V_context"
+ "T@\"NSMutableArray\",&,N,V_circularQueue"
+ "T@\"NSMutableDictionary\",R,N,V_retryAttemptCount"
+ "T@\"NSMutableDictionary\",R,N,V_retryTimers"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_xpcReplyQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_xpcRequestQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,N,V_queue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_timer"
+ "T@\"NSUUID\",R,N,V_identifier"
+ "T@?,C,N,V_eventHandler"
+ "TB,N,V_enforceAutomaticEndpointing"
+ "TB,R,N,V_isExclaveHardware"
+ "TB,R,N,V_shouldUseSystemDaemonRecorder"
+ "TB,R,V_isCancelled"
+ "TQ,N,V_audioCallbackLogHeartbeat"
+ "TQ,N,V_bufferCapacity"
+ "TQ,N,V_daemonState"
+ "TQ,N,V_lastSampleCount"
+ "TQ,N,V_totalSampleCount"
+ "TQ,R,N,V_maxAssetMapRetryCount"
+ "Td,R,N,V_assetMapRetryTimeInterval"
+ "Td,R,N,V_timerInterval"
+ "Ti,N,V_notifyToken"
+ "UserInfo"
+ "Yes"
+ "[%@] Mapping asset type: %ld into exclave"
+ "[enforceAutomaticEndpointing = %@]"
+ "_armTimer"
+ "_assetMapRetryTimeInterval"
+ "_audioCallbackLogHeartbeat"
+ "_audioProviderImplementor"
+ "_audioProvidingProxy"
+ "_bufferCapacity"
+ "_buffer_port"
+ "_cancelRetryTimerForAsset:"
+ "_circularQueue"
+ "_connectIfNeeded"
+ "_context"
+ "_crashMonitorDelegate"
+ "_daemonState"
+ "_disarmTimer"
+ "_enforceAutomaticEndpointing"
+ "_eventHandler"
+ "_getCSFSensorStatusWithExclaveSensorStatus:"
+ "_handleAgentDaemonXPCClientDisconnection"
+ "_handleAudioCallbackDelegate:"
+ "_handleAudioProvidingDelegateAudioBuffer:"
+ "_handleAudioProvidingDelegateMessageBody:"
+ "_handleDidFinishAlertPlaybackDelegate:"
+ "_handleDidStartRecordingDelegate:"
+ "_handleDidStopRecordingDelegate:"
+ "_handleListenerDisconnectedError:"
+ "_handleListenerMessage:"
+ "_handleSessionActive:"
+ "_handleSessionResign:"
+ "_handleSystemDaemonDidLaunchNotification"
+ "_hasStarted"
+ "_identifier"
+ "_isAudioStreamTypeBuiltIn"
+ "_lastSampleCount"
+ "_launchAgentAudioClient"
+ "_logMapFailTelemetryAndSubmitDiagnosticReportForError:assetSpecifier:assetConfigVersion:"
+ "_logMapOperationLatencyTelemetry:assetSpecifier:assetConfigVersion:"
+ "_mapAssetToExclaveKit:assetName:assetSet:completion:"
+ "_mapVoiceTriggerAsset:asset:completion:"
+ "_maxAssetMapRetryCount"
+ "_mem"
+ "_notifyObserversSystemDaemonCrashed"
+ "_notifyObserversSystemDaemonRestartedFromCrash"
+ "_notifySessionActive:"
+ "_registerUserSessionNotification"
+ "_resetRetryTimerForAsset:"
+ "_retryAttemptCount"
+ "_retryMappingAssetToExclaveKit:assetName:assetSet:completion:"
+ "_retryTimers"
+ "_sensor_port"
+ "_setAssetMapRetryTimeInterval:"
+ "_setMaxAssetMapRetryCount:"
+ "_shouldUseSystemDaemonRecorder"
+ "_timerForUUID:eventHandler:"
+ "_timerInterval"
+ "_totalSampleCount"
+ "_unregisterUserSessionNotification"
+ "_xpcReplyQueue"
+ "_xpcRequestQueue"
+ "activateSecureSession"
+ "activateSecureSession:"
+ "addChunk:"
+ "alertType"
+ "assetConfigVersion"
+ "assetMapRetryTimeInterval"
+ "assetSpecifier"
+ "audioBuffer"
+ "audioCallbackLogHeartbeat"
+ "audioContext"
+ "audioProviderImplementor"
+ "audioProviderWithContext:error:"
+ "audioProviderWithStreamID:"
+ "audioProviderWithUUID:"
+ "avvcRecordMode"
+ "body"
+ "bufferCapacity"
+ "cancel"
+ "channelForVoiceIsolation"
+ "circularQueue"
+ "com.apple.audio.siri_history"
+ "com.apple.corespeech.corespeechd_system.launch"
+ "com.apple.corespeech.secureasset.assetmapfailed"
+ "com.apple.corespeech.secureasset.exclavemaplatency"
+ "com.apple.corespeech_launchagent.xpc"
+ "compact"
+ "configErrorCode"
+ "copyChunkFromStartSampleCount:toEndSampleCount:"
+ "crashMonitorDelegate"
+ "currentSensorStatus"
+ "daemonState"
+ "didStartResult"
+ "didStopReason"
+ "dimension"
+ "enablePHS"
+ "enforceAutomaticEndpointing"
+ "errorCode"
+ "errorDomain"
+ "eventHandler"
+ "exclaveManagerProxy"
+ "fetchCurrentSensorStatus"
+ "forceFailExclaveAssetMapping"
+ "getBestSupportedSiriLanguageWithFallback:"
+ "getStringForKey:"
+ "identifier"
+ "initAudioRecorderWithError:"
+ "initTimerinterval:identifier:"
+ "initWithBufferCapacity:"
+ "initWithContext:queue:eventHandler:"
+ "initWithForceSetIsExclave:exclaveManagerProxy:"
+ "initWithRecordContext:deviceId:shouldUseRemoteRecorder:streamHandleId:shouldUseSystemDaemonRecorder:"
+ "isAssistant"
+ "isCompactVersion"
+ "isFromActiveUserMachXPCConnection:"
+ "isMagusRestrictedWithSAEForLanguageCode:"
+ "isOTA"
+ "kCSSecureAssetMappingFailed"
+ "keywordDetectResult"
+ "lastSampleCount"
+ "logSiriSetupEnrollmentSessionSummaryWithSiriSetupID:lastOpenedPage:completedPage:pageAttemptsMap:"
+ "logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:didDetectSpeechStart:didUseTwoPassDetector:didFirstPassTrigger:"
+ "lowercaseString"
+ "macUserSessionMonitor:sessionActive:"
+ "mapAssetToExclaveKit:assetName:assetSet:completion:"
+ "maxAssetMapRetryCount"
+ "notifyToken"
+ "numEmbeddings"
+ "numSamplesCount"
+ "pingpong:"
+ "prepare:"
+ "prepareAudioRecordWithStreamHandleId:settings:error:"
+ "prepareSettings"
+ "profileEmbedding"
+ "removeObjectAtIndex:"
+ "reportAssetMapFailTelemetryForError:assetSpecifier:assetConfigVersion:"
+ "reportAssetMapLatencyTelemetry:assetSpecifier:assetConfigVersion:"
+ "requestHistoricalAudioBufferWithStartSample:completion:"
+ "resume:"
+ "retryAttemptCount"
+ "retryMappingAssetToExclaveKit:assetName:assetSet:completion:"
+ "retryMappingAssetToExclaveKit:completion:"
+ "retryTimers"
+ "secondPassPhId"
+ "secondPassResultType"
+ "secondPassSignalIntensity"
+ "secondPassTriggerEndSampleCount"
+ "secondPassTriggerStartSampleCount"
+ "secondPassTriggerTimestamp"
+ "sendAssetsControlMessage:errorCodeIfFailed:completion:"
+ "sendMessageAndReplySync:error:"
+ "sendMessageAsync:completion:"
+ "sendMessageSync:"
+ "sensorStartForStream:"
+ "setAudioCallbackLogHeartbeat:"
+ "setAudioProviderImp:"
+ "setAudioProviderImplementor:"
+ "setBufferCapacity:"
+ "setCircularQueue:"
+ "setContext:"
+ "setCrashMonitorDelegate:"
+ "setDaemonState:"
+ "setDidTriggerFirstPass:"
+ "setEnforceAutomaticEndpointing:"
+ "setEventHandler:"
+ "setForceFailExclaveAssetMapping:"
+ "setLastCompletedPage:"
+ "setLastOpenedPageNumber:"
+ "setLastSampleCount:"
+ "setListeningMicIndicatorPropertyForStream:"
+ "setNotifyToken:"
+ "setNumAttempts:"
+ "setPageAttempts:"
+ "setRecordModeForStreamId:avvcRecordMode:error:"
+ "setSessionSummary:"
+ "setSpeechStartPointDetected:"
+ "setTimer:"
+ "setTwoPassRecognizerUsed:"
+ "setXpcReplyQueue:"
+ "setXpcRequestQueue:"
+ "sha1StringFromInputData:"
+ "sha256DataFromInputData:"
+ "sha256HashStringFromInputString:"
+ "sharedContollerProxy"
+ "sharedReporter"
+ "shouldFlushAudio"
+ "shouldUseSystemDaemonRecorder"
+ "speakerDetectResult"
+ "speakerRecognizerType"
+ "startAudioStreamWithOption:error:"
+ "startSecondPassVoiceTriggerWithStartOption:"
+ "stopAudioStreamWithError:"
+ "submitSecureAssetIssueReport:withContext:"
+ "submitSecureAssetMapFailDiagnosticReportForError:"
+ "supportMultiphrase"
+ "supportsPersonalizedHeySiri"
+ "supportsSecureAssetForSpeakerRecognition"
+ "supportsSecureSensor"
+ "supportsSystemDaemon"
+ "supportsVoiceProfileIDInUserProfile"
+ "systemDaemonNotifyDidLaunch"
+ "timer"
+ "timerInterval"
+ "v16@?0I8I12"
+ "v24@0:8@\"CSLaunchAgentXPCClient\"16"
+ "v24@0:8@\"CSSystemDaemonStateMonitor\"16"
+ "v24@0:8@?<v@?QB>16"
+ "v24@?0d8@\"NSError\"16"
+ "v28@0:8@\"CSSiriEnabledMonitor\"16B24"
+ "v28@0:8B16@?<v@?QQdIQQQQ>20"
+ "v32@0:8Q16q24"
+ "v32@?0@\"NSNumber\"8@\"NSNumber\"16^B24"
+ "v40@0:8@16Q24@?32"
+ "v40@0:8@16i24i28@32"
+ "v40@0:8d16@24@32"
+ "v48@0:8@16@24@32@?40"
+ "v80@0:8@16i24@28i36i40B44@48@56i64B68B72B76"
+ "xpcReplyQueue"
+ "xpcRequestQueue"
+ "\xf01"
- "%s AssetName is nil. Not starting Secure Mobile Asset Loader Service"
- "%s CSAudioProvider[%{public}@]:Entering dispatch group for recordingWillStartGroup"
- "%s Calling AVVC setRecordMode to mode : %{public}@"
- "%s Creating new mhUUID: %@"
- "%s Mapping asset %@ to ExclaveKit completed with error %@"
- "%s listening property in AOP : %{public}d"
- "%s logSiriSetupPHSEnrollmentDigitalZero, setupID: %@, pageNumber: %d, phID: %@, maxZeros: %d, maxAllowed: %d, isOverThreshold: %d locale: %@, assetConfigVersion: %@, sessionStatus: %u"
- "-[CSFSensorControlSelfLogger logSensorControlStartWithStatus:withMHUUID:]"
- "-[CSUAFAssetManager _mapAssetToExclaveKitForAssetName:asset:completion:]"
- "-[CSUAFAssetManager _mapAssetToExclaveKitForAssetName:asset:completion:]_block_invoke_2"
- "-[CSVTUITrainingSelfLogger logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:]"
- "@44@0:8@16@24B32Q36"
- "AssetName is nil. Not starting Secure Mobile Asset Loader Service"
- "CSExclaveEntityKitProviding"
- "CSFSensorControlSelfLogger"
- "Non Exclave OTA variant asset cannot map"
- "UAF asset set doesn't have invocation asset"
- "_getMHSensorControlStatusWithCSFSensorStatus:"
- "_getSettingsConnection"
- "_initWithForceSetIsExclave:exclaveManagerProxy:"
- "_mapAssetToExclaveKitForAssetName:asset:completion:"
- "exclaveEntityKitProvider"
- "initWithRecordContext:deviceId:shouldUseRemoteRecorder:streamHandleId:"
- "logSensorControlStartWithStatus:withMHUUID:"
- "logSiriSetupPHSEnrollmentDigitalZeroDetectionCompletedWithSiriSetupID:withPageNumber:withPhId:withMaxNumContinuousZeros:withMaxNumAllowedContinuousZeros:withIsMaxNumContinuousZerosOverThreshold:withLocale:withVTAssetConfigVersion:withStageStatus:"
- "setListeningMicIndicatorProperty"
- "setSensorControlStatus:"
- "setSensorControlStatusReported:"
- "updateEntityStatistics:"
- "v28@0:8B16@?<v@?QQdffIfQQ>20"
- "v68@0:8@16i24@28i36i40B44@48@56i64"
- "\xf0!"

```
