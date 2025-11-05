## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech`

```diff

-3403.7.3.0.0
-  __TEXT.__text: 0x152c24
-  __TEXT.__auth_stubs: 0x1910
-  __TEXT.__objc_methlist: 0x126c0
+3404.82.3.0.0
+  __TEXT.__text: 0x1533c4
+  __TEXT.__auth_stubs: 0x18f0
+  __TEXT.__objc_methlist: 0x146f0
   __TEXT.__const: 0x5d8
-  __TEXT.__gcc_except_tab: 0x37a0
-  __TEXT.__cstring: 0x23ee8
-  __TEXT.__oslogstring: 0x1dc81
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x4b08
-  __TEXT.__objc_classname: 0x2d8d
-  __TEXT.__objc_methname: 0x3602d
-  __TEXT.__objc_methtype: 0x73f6
-  __TEXT.__objc_stubs: 0x1a7a0
-  __DATA_CONST.__got: 0x1830
-  __DATA_CONST.__const: 0xc60
-  __DATA_CONST.__objc_classlist: 0x838
+  __TEXT.__gcc_except_tab: 0x3f88
+  __TEXT.__cstring: 0x23fc3
+  __TEXT.__oslogstring: 0x1dd3e
+  __TEXT.__unwind_info: 0x4c40
+  __TEXT.__objc_classname: 0x2d84
+  __TEXT.__objc_methname: 0x36103
+  __TEXT.__objc_methtype: 0x73dd
+  __TEXT.__objc_stubs: 0x1a8e0
+  __DATA_CONST.__got: 0x1838
+  __DATA_CONST.__const: 0xc98
+  __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x460
+  __DATA_CONST.__objc_protolist: 0x468
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa088
+  __DATA_CONST.__objc_selrefs: 0xa258
   __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x660
-  __DATA_CONST.__objc_arraydata: 0x458
-  __AUTH_CONST.__auth_got: 0xca0
-  __AUTH_CONST.__const: 0x5960
-  __AUTH_CONST.__cfstring: 0x8b60
-  __AUTH_CONST.__objc_const: 0x24168
+  __DATA_CONST.__objc_superrefs: 0x658
+  __DATA_CONST.__objc_arraydata: 0x468
+  __AUTH_CONST.__auth_got: 0xc90
+  __AUTH_CONST.__const: 0x5920
+  __AUTH_CONST.__cfstring: 0x8bc0
+  __AUTH_CONST.__objc_const: 0x20768
   __AUTH_CONST.__objc_intobj: 0x978
   __AUTH_CONST.__objc_doubleobj: 0x90
+  __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_floatobj: 0x4a0
-  __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x5230
-  __DATA.__objc_ivar: 0x1978
-  __DATA.__data: 0x34d0
-  __DATA.__bss: 0x740
-  __DATA.__common: 0x18
+  __AUTH.__objc_data: 0x51e0
+  __DATA.__objc_ivar: 0x1960
+  __DATA.__data: 0x3530
+  __DATA.__bss: 0x728
+  __DATA.__common: 0x10
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 618A98B4-4286-3AEF-A1A1-91B4DF34EDCB
-  Functions: 7961
-  Symbols:   17797
-  CStrings:  14830
+  UUID: 35E64238-FB3F-3F9E-B4E6-137B367BF461
+  Functions: 7940
+  Symbols:   17838
+  CStrings:  14835
 
Symbols:
+ +[CSVoiceIdXPCClient notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]
+ -[CSAssetManager installedCompactAssetOfType:language:]
+ -[CSAttSiriMitigationAssetHandler _siriLanguageCode]
+ -[CSAudioSessionInfoProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]
+ -[CSAudioSessionInfoProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]
+ -[CSAudioTapProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]
+ -[CSAudioTapProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]
+ -[CSBuiltInVoiceTrigger CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]
+ -[CSBuiltInVoiceTrigger CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]
+ -[CSBuiltInVoiceTrigger _setAsset:]
+ -[CSHybridEndpointer _isTaskStringAccessible:]
+ -[CSHybridEndpointer currentTaskString]
+ -[CSHybridEndpointer setCurrentTaskString:]
+ -[CSSpeechController _shouldUseVoiceIsolationChannel]
+ -[CSSpeechManager CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]
+ -[CSSpeechManager CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]
+ -[CSSpeechManager _mapAssetToExclaveKit:completion:]
+ -[CSSpeechManager _retryMapAssetToExclaveKit:]
+ -[CSSpeechManager _tearDownBuiltInVoiceTrigger]
+ -[CSSpeechManager macUserSessionMonitor:sessionActive:]
+ -[CSVoiceIdXPCClient _notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]
+ -[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]
+ -[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]
+ -[CSVoiceTriggerAssetHandler mapAssetToExclaveKit:completion:]
+ -[CSVoiceTriggerAssetHandler retryMappingAssetToExclaveKit:completion:]
+ -[CSVoiceTriggerAssetHandler setUafAssetManager:]
+ -[CSVoiceTriggerAssetHandler uafAssetManager]
+ -[CSVoiceTriggerFirstPassJarvisAP multiPhraseSelectedStatus]
+ -[CSVoiceTriggerFirstPassJarvisAP setMultiPhraseSelectedStatus:]
+ -[CSVoiceTriggerSecondPass CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]
+ -[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]
+ -[CSVoiceTriggerSecondPass convertSecureVoiceTriggerKeywordDetectionResultTypeToString:]
+ -[CSVoiceTriggerSecondPass convertSecureVoiceTriggerSpeakerDetectionResultTypeToString:]
+ AudioConverterFillComplexBuffer_BlockInvoke.25728
+ GCC_except_table1071
+ GCC_except_table1085
+ GCC_except_table1291
+ GCC_except_table1356
+ GCC_except_table1382
+ GCC_except_table1386
+ GCC_except_table1402
+ GCC_except_table1405
+ GCC_except_table1429
+ GCC_except_table1436
+ GCC_except_table1445
+ GCC_except_table1544
+ GCC_except_table1546
+ GCC_except_table1548
+ GCC_except_table1555
+ GCC_except_table1610
+ GCC_except_table1636
+ GCC_except_table1642
+ GCC_except_table165
+ GCC_except_table1723
+ GCC_except_table1746
+ GCC_except_table1850
+ GCC_except_table193
+ GCC_except_table2092
+ GCC_except_table2095
+ GCC_except_table2098
+ GCC_except_table2103
+ GCC_except_table2120
+ GCC_except_table2126
+ GCC_except_table2129
+ GCC_except_table2252
+ GCC_except_table2257
+ GCC_except_table2263
+ GCC_except_table2281
+ GCC_except_table240
+ GCC_except_table2416
+ GCC_except_table2474
+ GCC_except_table2486
+ GCC_except_table2519
+ GCC_except_table2540
+ GCC_except_table2554
+ GCC_except_table2595
+ GCC_except_table2596
+ GCC_except_table2597
+ GCC_except_table2603
+ GCC_except_table2610
+ GCC_except_table2614
+ GCC_except_table2615
+ GCC_except_table2624
+ GCC_except_table263
+ GCC_except_table2630
+ GCC_except_table2632
+ GCC_except_table2656
+ GCC_except_table266
+ GCC_except_table2923
+ GCC_except_table3006
+ GCC_except_table3043
+ GCC_except_table3069
+ GCC_except_table3072
+ GCC_except_table3075
+ GCC_except_table3106
+ GCC_except_table3166
+ GCC_except_table3336
+ GCC_except_table3362
+ GCC_except_table3424
+ GCC_except_table3425
+ GCC_except_table3427
+ GCC_except_table3429
+ GCC_except_table3445
+ GCC_except_table3447
+ GCC_except_table3449
+ GCC_except_table3457
+ GCC_except_table3460
+ GCC_except_table3468
+ GCC_except_table3471
+ GCC_except_table3478
+ GCC_except_table3480
+ GCC_except_table3482
+ GCC_except_table3488
+ GCC_except_table3489
+ GCC_except_table3490
+ GCC_except_table3491
+ GCC_except_table3493
+ GCC_except_table3494
+ GCC_except_table3495
+ GCC_except_table3498
+ GCC_except_table3500
+ GCC_except_table3501
+ GCC_except_table3502
+ GCC_except_table3503
+ GCC_except_table3504
+ GCC_except_table3505
+ GCC_except_table3506
+ GCC_except_table3508
+ GCC_except_table3509
+ GCC_except_table3517
+ GCC_except_table3522
+ GCC_except_table3524
+ GCC_except_table3525
+ GCC_except_table3631
+ GCC_except_table3655
+ GCC_except_table3715
+ GCC_except_table372
+ GCC_except_table3729
+ GCC_except_table3750
+ GCC_except_table3840
+ GCC_except_table4090
+ GCC_except_table4143
+ GCC_except_table4144
+ GCC_except_table4148
+ GCC_except_table4151
+ GCC_except_table4155
+ GCC_except_table4180
+ GCC_except_table4230
+ GCC_except_table4236
+ GCC_except_table4552
+ GCC_except_table4708
+ GCC_except_table4718
+ GCC_except_table4742
+ GCC_except_table4762
+ GCC_except_table4843
+ GCC_except_table4855
+ GCC_except_table4864
+ GCC_except_table4873
+ GCC_except_table4879
+ GCC_except_table4884
+ GCC_except_table4896
+ GCC_except_table4902
+ GCC_except_table4922
+ GCC_except_table4928
+ GCC_except_table4933
+ GCC_except_table4935
+ GCC_except_table4939
+ GCC_except_table4940
+ GCC_except_table4941
+ GCC_except_table4945
+ GCC_except_table4956
+ GCC_except_table4957
+ GCC_except_table4962
+ GCC_except_table4977
+ GCC_except_table5103
+ GCC_except_table5132
+ GCC_except_table5135
+ GCC_except_table5320
+ GCC_except_table5336
+ GCC_except_table5346
+ GCC_except_table5353
+ GCC_except_table5380
+ GCC_except_table5384
+ GCC_except_table5388
+ GCC_except_table5399
+ GCC_except_table5669
+ GCC_except_table5675
+ GCC_except_table5707
+ GCC_except_table5712
+ GCC_except_table572
+ GCC_except_table5749
+ GCC_except_table5758
+ GCC_except_table5785
+ GCC_except_table5866
+ GCC_except_table6086
+ GCC_except_table6094
+ GCC_except_table6114
+ GCC_except_table6119
+ GCC_except_table6224
+ GCC_except_table627
+ GCC_except_table6305
+ GCC_except_table6306
+ GCC_except_table6316
+ GCC_except_table6317
+ GCC_except_table6329
+ GCC_except_table6462
+ GCC_except_table6480
+ GCC_except_table6489
+ GCC_except_table6494
+ GCC_except_table6501
+ GCC_except_table6503
+ GCC_except_table6533
+ GCC_except_table6624
+ GCC_except_table6650
+ GCC_except_table6661
+ GCC_except_table6664
+ GCC_except_table6687
+ GCC_except_table6699
+ GCC_except_table691
+ GCC_except_table6944
+ GCC_except_table695
+ GCC_except_table6979
+ GCC_except_table699
+ GCC_except_table7033
+ GCC_except_table7043
+ GCC_except_table7046
+ GCC_except_table7048
+ GCC_except_table7055
+ GCC_except_table7058
+ GCC_except_table706
+ GCC_except_table7063
+ GCC_except_table7068
+ GCC_except_table7069
+ GCC_except_table7075
+ GCC_except_table7076
+ GCC_except_table7081
+ GCC_except_table7083
+ GCC_except_table7086
+ GCC_except_table7088
+ GCC_except_table7089
+ GCC_except_table7118
+ GCC_except_table7173
+ GCC_except_table7197
+ GCC_except_table7239
+ GCC_except_table7249
+ GCC_except_table7259
+ GCC_except_table7300
+ GCC_except_table7307
+ GCC_except_table7331
+ GCC_except_table7380
+ GCC_except_table7462
+ GCC_except_table7463
+ GCC_except_table7464
+ GCC_except_table7465
+ GCC_except_table7466
+ GCC_except_table7471
+ GCC_except_table7535
+ GCC_except_table7577
+ GCC_except_table7603
+ GCC_except_table7620
+ GCC_except_table7626
+ GCC_except_table7629
+ GCC_except_table7637
+ GCC_except_table7643
+ GCC_except_table7663
+ GCC_except_table7793
+ OBJC_IVAR_$_CSHybridEndpointer._currentTaskString
+ OBJC_IVAR_$_CSVoiceTriggerAssetHandler._uafAssetManager
+ OBJC_IVAR_$_CSVoiceTriggerFirstPassJarvisAP._multiPhraseSelectedStatus
+ _CSSiriSpeechRecordingRecordedAudioAppContainerName
+ _OBJC_CLASS_$_CSAudioProviderSelectingProxy
+ _OBJC_CLASS_$_CSFHashUtils
+ _OBJC_CLASS_$_CSMacUserSessionMonitor
+ _OBJC_CLASS_$_CSSystemDaemonStateMonitor
+ __109-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:bundleIdentifier:completion:]_block_invoke.14
+ __109-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:bundleIdentifier:completion:]_block_invoke.18
+ __110+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withfadingTimeWindowLength:handlingDaemon:completion:]_block_invoke.19
+ __110-[CSSiriLauncher notifyDarwinVoiceTrigger:deviceId:myriadPHash:myriadLateActivationExpirationTime:completion:]_block_invoke.31
+ __110-[CSSiriLauncher notifyDarwinVoiceTrigger:deviceId:myriadPHash:myriadLateActivationExpirationTime:completion:]_block_invoke.34
+ __110-[CSVoiceTriggerSecondPass _requestStartAudioStreamWitContext:audioProviderUUID:startStreamOption:completion:]_block_invoke.86
+ __112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.180
+ __119+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.12
+ __119+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.14
+ __121+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:completion:]_block_invoke.21
+ __133-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.156
+ __136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.132
+ __136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.135
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke.40
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke.42
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke.52
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke.60
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke.67
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke.77
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke.80
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke_2.61
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke_2.68
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke_2.78
+ __30-[CSBuiltInVoiceTrigger start]_block_invoke_3.69
+ __35-[CSBuiltInVoiceTrigger _setAsset:]_block_invoke.104
+ __39-[CSBuiltInVoiceTrigger _stopListening]_block_invoke.140
+ __40-[CSHybridEndpointer processTaskString:]_block_invoke.406
+ __44-[CSBuiltInVoiceTrigger _stopAPVoiceTrigger]_block_invoke.153
+ __48+[CSAudioInjectionServices pingpong:completion:]_block_invoke.2
+ __48+[CSAudioInjectionServices pingpong:completion:]_block_invoke.4
+ __49-[CSVoiceTriggerFirstPassJarvisAP _stopListening]_block_invoke.26
+ __50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.47
+ __52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.131
+ __52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.133
+ __52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.41
+ __52-[CSVoiceTriggerAssetHandlerMac triggerAssetRefresh]_block_invoke.29
+ __54-[CSAttSiriMitigationAssetHandler triggerAssetRefresh]_block_invoke.32
+ __56-[CSVoiceTriggerSecondPass _initializeMediaPlayingState]_block_invoke.76
+ __56-[CSVoiceTriggerSecondPass _initializeMediaPlayingState]_block_invoke_2.77
+ __57-[CSAudioTapProvider startAudioStream:option:completion:]_block_invoke.29
+ __62-[CSAudioTapProvider audioStreamWithRequest:streamName:error:]_block_invoke.37
+ __62-[CSVoiceTriggerFirstPassJarvisAP _startListenWithCompletion:]_block_invoke.23
+ __64-[CSBuiltInVoiceTrigger _handleSecondPassResult:deviceId:error:]_block_invoke.194
+ __64-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke.272
+ __65-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke.18
+ __67-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke.15
+ __67-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke.9
+ __68-[CSBuiltInVoiceTrigger _startListenPollingWithInterval:completion:]_block_invoke.124
+ __68-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke.139
+ __69-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke.34
+ __69-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke.36
+ __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.422
+ __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.426
+ __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.430
+ __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.435
+ __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.439
+ __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2.428
+ __71-[CSSpeechManager activationEventNotificationHandler:event:completion:]_block_invoke.82
+ __71-[CSSpeechManager activationEventNotificationHandler:event:completion:]_block_invoke_2.83
+ __76+[CSAudioInjectionServices connectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.25
+ __77-[CSBuiltInVoiceTrigger activationEventNotificationHandler:event:completion:]_block_invoke.199
+ __79+[CSAudioInjectionServices disconnectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.28
+ __80-[CSAttSiriMitigationAssetHandler _getMitigationAssetWithEndpointId:completion:]_block_invoke.25
+ __82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.105
+ __82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.112
+ __84+[CSAudioInjectionServices primaryInputDeviceUUIDWithhandlingDaemon:WithCompletion:]_block_invoke.30
+ __88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.489
+ __88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.496
+ __93-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromAOP:audioProviderUUID:completion:]_block_invoke.153
+ __97-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:]_block_invoke.93
+ __Block_byref_object_copy_.10959
+ __Block_byref_object_copy_.12180
+ __Block_byref_object_copy_.12597
+ __Block_byref_object_copy_.13704
+ __Block_byref_object_copy_.1382
+ __Block_byref_object_copy_.14721
+ __Block_byref_object_copy_.16238
+ __Block_byref_object_copy_.16683
+ __Block_byref_object_copy_.18115
+ __Block_byref_object_copy_.19013
+ __Block_byref_object_copy_.19471
+ __Block_byref_object_copy_.20424
+ __Block_byref_object_copy_.2057
+ __Block_byref_object_copy_.20900
+ __Block_byref_object_copy_.21629
+ __Block_byref_object_copy_.22496
+ __Block_byref_object_copy_.23247
+ __Block_byref_object_copy_.24203
+ __Block_byref_object_copy_.2431
+ __Block_byref_object_copy_.25474
+ __Block_byref_object_copy_.25959
+ __Block_byref_object_copy_.26738
+ __Block_byref_object_copy_.3306
+ __Block_byref_object_copy_.3483
+ __Block_byref_object_copy_.3670
+ __Block_byref_object_copy_.4188
+ __Block_byref_object_copy_.6115
+ __Block_byref_object_copy_.7077
+ __Block_byref_object_copy_.7891
+ __Block_byref_object_copy_.8467
+ __Block_byref_object_copy_.9469
+ __Block_byref_object_dispose_.10960
+ __Block_byref_object_dispose_.12181
+ __Block_byref_object_dispose_.12598
+ __Block_byref_object_dispose_.13705
+ __Block_byref_object_dispose_.1383
+ __Block_byref_object_dispose_.14722
+ __Block_byref_object_dispose_.16239
+ __Block_byref_object_dispose_.16684
+ __Block_byref_object_dispose_.18116
+ __Block_byref_object_dispose_.19014
+ __Block_byref_object_dispose_.19472
+ __Block_byref_object_dispose_.20425
+ __Block_byref_object_dispose_.2058
+ __Block_byref_object_dispose_.20901
+ __Block_byref_object_dispose_.21630
+ __Block_byref_object_dispose_.22497
+ __Block_byref_object_dispose_.23248
+ __Block_byref_object_dispose_.24204
+ __Block_byref_object_dispose_.2432
+ __Block_byref_object_dispose_.25475
+ __Block_byref_object_dispose_.25960
+ __Block_byref_object_dispose_.26739
+ __Block_byref_object_dispose_.3307
+ __Block_byref_object_dispose_.3484
+ __Block_byref_object_dispose_.3671
+ __Block_byref_object_dispose_.4189
+ __Block_byref_object_dispose_.6116
+ __Block_byref_object_dispose_.7078
+ __Block_byref_object_dispose_.7892
+ __Block_byref_object_dispose_.8468
+ __Block_byref_object_dispose_.9470
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSMacUserSessionMonitorDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSystemDaemonStateMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSMacUserSessionMonitorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemDaemonStateMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_CSMacUserSessionMonitorDelegate
+ __OBJC_$_PROTOCOL_REFS_CSSystemDaemonStateMonitorDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSMacUserSessionMonitorDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSSystemDaemonStateMonitorDelegate
+ __OBJC_PROTOCOL_$_CSMacUserSessionMonitorDelegate
+ __OBJC_PROTOCOL_$_CSSystemDaemonStateMonitorDelegate
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_6vectorINS4_IfNS_9allocatorIfEEEENS5_IS7_EEEESA_SA_EENS_4pairIT_T1_EESC_T0_SD_
+ __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8ne190102IPNS_6vectorIfNS_9allocatorIfEEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
+ __ZNKSt3__114default_deleteIN10corespeech25CSAudioCircularBufferImplIhEEEclB8ne190102EPS3_
+ __ZNKSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt12out_of_rangeC1B8ne190102EPKc
+ __ZNSt3__110unique_ptrI15SmartSiriVolumeNS_14default_deleteIS1_EEE5resetB8ne190102EPS1_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorINS_4pairIfjEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__120__throw_out_of_rangeB8ne190102EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ne190102Ev
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne190102Ev
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8ne190102INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ne190102IPS5_S9_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne190102Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne190102IPS3_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne190102IPS3_S7_EEvT_T0_l
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE7__clearB8ne190102Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEEC2B8ne190102EmRKS3_
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne190102Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne190102IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne190102IPfS5_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne190102EmRKf
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___138+[CSVoiceIdXPCClient notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]_block_invoke
+ ___139-[CSVoiceIdXPCClient _notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]_block_invoke
+ ___34-[CSBuiltInVoiceTrigger setAsset:]_block_invoke
+ ___35-[CSBuiltInVoiceTrigger _setAsset:]_block_invoke
+ ___46-[CSSpeechManager _retryMapAssetToExclaveKit:]_block_invoke
+ ___46-[CSSpeechManager _retryMapAssetToExclaveKit:]_block_invoke_2
+ ___52-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke
+ ___52-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke_2
+ ___55-[CSSpeechManager macUserSessionMonitor:sessionActive:]_block_invoke
+ ___55-[CSSpeechManager macUserSessionMonitor:sessionActive:]_block_invoke_2
+ ___62-[CSVoiceTriggerAssetHandler mapAssetToExclaveKit:completion:]_block_invoke
+ ___65-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke
+ ___65-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke_2
+ ___68-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke
+ ___68-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke_2
+ ___69-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke
+ ___70-[CSSpeechManager CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]_block_invoke
+ ___71-[CSVoiceTriggerAssetHandler retryMappingAssetToExclaveKit:completion:]_block_invoke
+ ___73-[CSAudioTapProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]_block_invoke
+ ___76-[CSBuiltInVoiceTrigger CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]_block_invoke
+ ___76-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke_2
+ ___76-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke_3
+ ___81-[CSAudioSessionInfoProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]_block_invoke
+ ___81-[CSSpeechManager CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]_block_invoke
+ ___81-[CSSpeechManager CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]_block_invoke_2
+ ___87-[CSBuiltInVoiceTrigger CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]_block_invoke
+ ___90-[CSVoiceTriggerSecondPass CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]_block_invoke
+ ___92-[CSAudioSessionInfoProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]_block_invoke
+ ___ZL25isRunningListenerCallbackPvP16OpaqueAudioQueuej_block_invoke.238
+ ___block_descriptor_40_e8_32bs_e28_v24?0"NSString"8"NSURL"16l
+ ___block_descriptor_40_e8_32s_e26_v60?0Q8d16I24Q28Q36Q44Q52l
+ ___block_descriptor_48_e8_32s40bs_e28_v24?0"NSString"8"NSURL"16l
+ ___block_descriptor_48_e8_32s_e26_v60?0Q8d16I24Q28Q36Q44Q52l
+ ___block_descriptor_56_e8_32s40s48w_e17_v16?0"NSError"8l
+ ___block_descriptor_57_e8_32s40bs48bs_e29_v68?0Q8Q16d24I32Q36Q44Q52Q60l
+ ___block_descriptor_64_e8_32s40bs48bs_e5_v8?0l
+ ___block_descriptor_64_e8_32s40s48bs56w_e20_v20?0"NSError"8B16l
+ ___block_descriptor_64_e8_32s40s48bs_e11_v20?0Q8B16l
+ ___block_descriptor_65_e8_32s40s48bs56w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48b56w
+ __block_literal_global.10.20159
+ __block_literal_global.10.21458
+ __block_literal_global.10.9920
+ __block_literal_global.10156
+ __block_literal_global.1026
+ __block_literal_global.10372
+ __block_literal_global.10824
+ __block_literal_global.10985
+ __block_literal_global.11.3403
+ __block_literal_global.1122
+ __block_literal_global.11256
+ __block_literal_global.11354
+ __block_literal_global.11474
+ __block_literal_global.11767
+ __block_literal_global.11919
+ __block_literal_global.1198
+ __block_literal_global.12.17046
+ __block_literal_global.12385
+ __block_literal_global.12501
+ __block_literal_global.12728
+ __block_literal_global.13.20260
+ __block_literal_global.13.21459
+ __block_literal_global.13.25888
+ __block_literal_global.13116
+ __block_literal_global.13173
+ __block_literal_global.13446
+ __block_literal_global.13464
+ __block_literal_global.13578
+ __block_literal_global.142
+ __block_literal_global.14708
+ __block_literal_global.14755
+ __block_literal_global.1508
+ __block_literal_global.15317
+ __block_literal_global.15790
+ __block_literal_global.15799
+ __block_literal_global.15845
+ __block_literal_global.15860
+ __block_literal_global.16.12386
+ __block_literal_global.16.20160
+ __block_literal_global.16.25889
+ __block_literal_global.16.9705
+ __block_literal_global.16299
+ __block_literal_global.17030
+ __block_literal_global.17045
+ __block_literal_global.17244
+ __block_literal_global.17849
+ __block_literal_global.18.11243
+ __block_literal_global.18.13547
+ __block_literal_global.18.18725
+ __block_literal_global.18.20261
+ __block_literal_global.18147
+ __block_literal_global.18521
+ __block_literal_global.18602
+ __block_literal_global.187
+ __block_literal_global.18742
+ __block_literal_global.18837
+ __block_literal_global.18884
+ __block_literal_global.18929
+ __block_literal_global.19062
+ __block_literal_global.1915
+ __block_literal_global.19355
+ __block_literal_global.19495
+ __block_literal_global.19571
+ __block_literal_global.19723
+ __block_literal_global.20.12368
+ __block_literal_global.20145
+ __block_literal_global.20158
+ __block_literal_global.20284
+ __block_literal_global.20334
+ __block_literal_global.20369
+ __block_literal_global.204
+ __block_literal_global.20506
+ __block_literal_global.2079
+ __block_literal_global.21456
+ __block_literal_global.2186
+ __block_literal_global.21959
+ __block_literal_global.22.20161
+ __block_literal_global.22126
+ __block_literal_global.22527
+ __block_literal_global.22820
+ __block_literal_global.2290
+ __block_literal_global.23038
+ __block_literal_global.2304
+ __block_literal_global.23125
+ __block_literal_global.23388
+ __block_literal_global.24443
+ __block_literal_global.24791
+ __block_literal_global.25.16080
+ __block_literal_global.25.20162
+ __block_literal_global.25121
+ __block_literal_global.2524
+ __block_literal_global.25280
+ __block_literal_global.25332
+ __block_literal_global.25510
+ __block_literal_global.25615
+ __block_literal_global.25747
+ __block_literal_global.25856
+ __block_literal_global.25887
+ __block_literal_global.2619
+ __block_literal_global.26533
+ __block_literal_global.26749
+ __block_literal_global.27
+ __block_literal_global.27036
+ __block_literal_global.27049
+ __block_literal_global.2872
+ __block_literal_global.29.20163
+ __block_literal_global.30.24763
+ __block_literal_global.3056
+ __block_literal_global.31.18711
+ __block_literal_global.3203
+ __block_literal_global.3355
+ __block_literal_global.3402
+ __block_literal_global.341
+ __block_literal_global.3473
+ __block_literal_global.3706
+ __block_literal_global.4.25281
+ __block_literal_global.417
+ __block_literal_global.44.8574
+ __block_literal_global.4623
+ __block_literal_global.5.27050
+ __block_literal_global.50.10365
+ __block_literal_global.5218
+ __block_literal_global.5481
+ __block_literal_global.5766
+ __block_literal_global.5837
+ __block_literal_global.5862
+ __block_literal_global.595
+ __block_literal_global.6.25505
+ __block_literal_global.6174
+ __block_literal_global.63
+ __block_literal_global.6328
+ __block_literal_global.6614
+ __block_literal_global.676
+ __block_literal_global.7.21457
+ __block_literal_global.7134
+ __block_literal_global.717
+ __block_literal_global.8.1178
+ __block_literal_global.8.27051
+ __block_literal_global.8052
+ __block_literal_global.8615
+ __block_literal_global.8667
+ __block_literal_global.8687
+ __block_literal_global.9.20259
+ __block_literal_global.9.25609
+ __block_literal_global.9070
+ __block_literal_global.944
+ __block_literal_global.9579
+ __block_literal_global.9722
+ __block_literal_global.9945
+ _block_invoke.enableHeartbeat.10152
+ _block_invoke.enableHeartbeat.26245
+ _handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.17787
+ _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10137
+ _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.17779
+ _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.26220
+ _objc_msgSend$URLByAppendingPathComponent:isDirectory:
+ _objc_msgSend$_handleImplicitUtteranceMessage:client:
+ _objc_msgSend$_isTaskStringAccessible:
+ _objc_msgSend$_mapAssetToExclaveKit:completion:
+ _objc_msgSend$_notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:
+ _objc_msgSend$_processSecondPassInExclave:rejectBlock:
+ _objc_msgSend$_retryMapAssetToExclaveKit:
+ _objc_msgSend$_runRetrainerWithAssets:languageCode:
+ _objc_msgSend$_shouldUseVoiceIsolationChannel
+ _objc_msgSend$_siriLanguageCode
+ _objc_msgSend$_tearDownBuiltInVoiceTrigger
+ _objc_msgSend$assetHandler
+ _objc_msgSend$channelForVoiceIsolation
+ _objc_msgSend$cleanupVoiceProfileModelFilesForLocale:withAssets:
+ _objc_msgSend$containerURLForSecurityApplicationGroupIdentifier:
+ _objc_msgSend$convertSecureVoiceTriggerKeywordDetectionResultTypeToString:
+ _objc_msgSend$convertSecureVoiceTriggerSpeakerDetectionResultTypeToString:
+ _objc_msgSend$copyItemAtURL:toURL:error:
+ _objc_msgSend$enforceAutomaticEndpointing
+ _objc_msgSend$getBestSupportedSiriLanguageWithFallback:
+ _objc_msgSend$installedCompactAssetOfType:language:
+ _objc_msgSend$isCompactVersion
+ _objc_msgSend$isMagusRestrictedWithSAEForLanguageCode:
+ _objc_msgSend$notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:
+ _objc_msgSend$retryMappingAssetToExclaveKit:completion:
+ _objc_msgSend$setAudioProviderImp:
+ _objc_msgSend$setUafAssetManager:
+ _objc_msgSend$sha1StringFromInputData:
+ _objc_msgSend$sha256DataFromInputData:
+ _objc_msgSend$sharedContollerProxy
+ _objc_msgSend$supportsPersonalizedHeySiri
+ _objc_msgSend$supportsSystemDaemon
+ _objc_msgSend$uafAssetManager
+ _runRetrainerWithAssets:languageCode:.onceCleanupToken
+ kASRTaskStringSearchOrMessaging_block_invoke.heartbeat_CORESPEECH_HYBRID_CLASSIFIER_PROCESS_END
+ kASRTaskStringSearchOrMessaging_block_invoke.heartbeat_CORESPEECH_PROCESS_SIL_SCORE_ESTIMATE_BEGIN
+ sharedController.onceToken.10984
+ sharedController.sharedController.10986
+ sharedHandler.onceToken.1025
+ sharedHandler.onceToken.18520
+ sharedHandler.onceToken.25509
+ sharedHandler.sharedHandler.1027
+ sharedHandler.sharedHandler.18522
+ sharedHandler.sharedHandler.25511
+ sharedHandlerDisabledOnDeviceCompilation.onceToken.25504
+ sharedHandlerDisabledOnDeviceCompilation.sharedHandler.25506
+ sharedInstance._sharedInstance.10825
+ sharedInstance._sharedInstance.11920
+ sharedInstance._sharedInstance.13174
+ sharedInstance._sharedInstance.13579
+ sharedInstance._sharedInstance.15846
+ sharedInstance._sharedInstance.18885
+ sharedInstance._sharedInstance.19356
+ sharedInstance._sharedInstance.19572
+ sharedInstance._sharedInstance.22821
+ sharedInstance._sharedInstance.23389
+ sharedInstance._sharedInstance.2525
+ sharedInstance._sharedInstance.25333
+ sharedInstance._sharedInstance.26750
+ sharedInstance._sharedInstance.27037
+ sharedInstance._sharedInstance.2873
+ sharedInstance._sharedInstance.5482
+ sharedInstance._sharedInstance.5838
+ sharedInstance._sharedInstance.6329
+ sharedInstance._sharedInstance.677
+ sharedInstance._sharedInstance.718
+ sharedInstance._sharedInstance.8668
+ sharedInstance.onceToken.10823
+ sharedInstance.onceToken.11918
+ sharedInstance.onceToken.1197
+ sharedInstance.onceToken.12500
+ sharedInstance.onceToken.13172
+ sharedInstance.onceToken.13577
+ sharedInstance.onceToken.14707
+ sharedInstance.onceToken.15844
+ sharedInstance.onceToken.16298
+ sharedInstance.onceToken.17029
+ sharedInstance.onceToken.17243
+ sharedInstance.onceToken.186
+ sharedInstance.onceToken.18741
+ sharedInstance.onceToken.18836
+ sharedInstance.onceToken.18883
+ sharedInstance.onceToken.19354
+ sharedInstance.onceToken.19570
+ sharedInstance.onceToken.20144
+ sharedInstance.onceToken.20283
+ sharedInstance.onceToken.20368
+ sharedInstance.onceToken.20505
+ sharedInstance.onceToken.21958
+ sharedInstance.onceToken.22125
+ sharedInstance.onceToken.22526
+ sharedInstance.onceToken.22819
+ sharedInstance.onceToken.23124
+ sharedInstance.onceToken.23387
+ sharedInstance.onceToken.25120
+ sharedInstance.onceToken.2523
+ sharedInstance.onceToken.25331
+ sharedInstance.onceToken.2618
+ sharedInstance.onceToken.26532
+ sharedInstance.onceToken.26748
+ sharedInstance.onceToken.27035
+ sharedInstance.onceToken.2871
+ sharedInstance.onceToken.3202
+ sharedInstance.onceToken.416
+ sharedInstance.onceToken.4622
+ sharedInstance.onceToken.5217
+ sharedInstance.onceToken.5480
+ sharedInstance.onceToken.5836
+ sharedInstance.onceToken.594
+ sharedInstance.onceToken.6327
+ sharedInstance.onceToken.675
+ sharedInstance.onceToken.716
+ sharedInstance.onceToken.8666
+ sharedInstance.onceToken.9721
+ sharedInstance.onceToken.9944
+ sharedInstance.sSharedInstance.17245
+ sharedInstance.sharedInstance.12502
+ sharedInstance.sharedInstance.17031
+ sharedInstance.sharedInstance.18743
+ sharedInstance.sharedInstance.18838
+ sharedInstance.sharedInstance.20146
+ sharedInstance.sharedInstance.20370
+ sharedInstance.sharedInstance.22127
+ sharedInstance.sharedInstance.22528
+ sharedInstance.sharedInstance.26534
+ sharedInstance.sharedInstance.3204
+ sharedInstance.sharedInstance.4624
+ sharedInstance.sharedInstance.5219
+ sharedInstance.sharedManager.25122
+ sharedInstance.sharedPolicy.1199
+ sharedInstance.sharedPolicy.20285
+ sharedInstance.sharedPolicy.23126
+ sharedInstance.sharedProvider.21960
+ sharedManager.onceToken.15789
+ sharedManager.onceToken.18146
+ sharedManager.onceToken.5861
+ sharedManager.onceToken.6613
+ sharedManager.sharedManager.15791
+ sharedManager.sharedManager.5863
+ sharedManager.sharedManager.6615
+ sharedMonitor.onceToken.19494
+ sharedMonitor.sharedMonitor.19496
+ sharedService.onceToken.14754
+ sharedService.onceToken.24790
+ sharedService.sharedService.24792
- +[CSAudioInjectionProviderExclave sharedInstance]
- -[CSAsset(RTModel) _sha1:]
- -[CSAsset(RTModel) _sha256:]
- -[CSAudioInjectionProviderExclave .cxx_destruct]
- -[CSAudioInjectionProviderExclave _createAudioQueueIfNeeded]
- -[CSAudioInjectionProviderExclave _defaultBufferRef]
- -[CSAudioInjectionProviderExclave _defaultOutASBD]
- -[CSAudioInjectionProviderExclave _prepareAndStartAudioQueue]
- -[CSAudioInjectionProviderExclave _readAudioBufferAndFeedIntoAudioQueue]
- -[CSAudioInjectionProviderExclave _setAudioSessionActive:]
- -[CSAudioInjectionProviderExclave bufferDuration]
- -[CSAudioInjectionProviderExclave exclaveAudioQueue]
- -[CSAudioInjectionProviderExclave fileOption]
- -[CSAudioInjectionProviderExclave init]
- -[CSAudioInjectionProviderExclave injectionCompletion]
- -[CSAudioInjectionProviderExclave injectionEndTime]
- -[CSAudioInjectionProviderExclave injectionStartTime]
- -[CSAudioInjectionProviderExclave isAudioQueueStarted]
- -[CSAudioInjectionProviderExclave queue]
- -[CSAudioInjectionProviderExclave setBufferDuration:]
- -[CSAudioInjectionProviderExclave setExclaveAudioQueue:]
- -[CSAudioInjectionProviderExclave setFileOption:]
- -[CSAudioInjectionProviderExclave setInjectionCompletion:]
- -[CSAudioInjectionProviderExclave setInjectionEndTime:]
- -[CSAudioInjectionProviderExclave setInjectionStartTime:]
- -[CSAudioInjectionProviderExclave setIsAudioQueueStarted:]
- -[CSAudioInjectionProviderExclave setQueue:]
- -[CSAudioInjectionProviderExclave speakAudioInExclave:withCompletion:]
- -[CSAudioInjectionProviderExclave start]
- -[CSBuiltInVoiceTrigger _setAsset:forceExclaveToUsePreInstalledAsset:]
- -[CSBuiltInVoiceTrigger setAsset:forceExclaveToUsePreInstalledAsset:]
- -[CSTrialAssetManager _getSiriAttAssetsForType:forLocale:completion:]
- -[CSVoiceIdXPCClient _notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]
- -[CSVoiceTriggerAssetHandlerMac mapAssetToExclaveKit:completion:]
- -[CSVoiceTriggerAssetHandlerMac setUafAssetManager:]
- -[CSVoiceTriggerAssetHandlerMac uafAssetManager]
- -[CSVoiceTriggerSecondPass _processSecondPassInExclave:]
- AudioConverterFillComplexBuffer_BlockInvoke.25722
- CSSecureLogInitIfNeeded.once
- GCC_except_table1061
- GCC_except_table1075
- GCC_except_table1281
- GCC_except_table1346
- GCC_except_table1372
- GCC_except_table1376
- GCC_except_table1392
- GCC_except_table1395
- GCC_except_table1419
- GCC_except_table1426
- GCC_except_table1435
- GCC_except_table1534
- GCC_except_table1536
- GCC_except_table1538
- GCC_except_table1545
- GCC_except_table1600
- GCC_except_table163
- GCC_except_table1632
- GCC_except_table1711
- GCC_except_table1734
- GCC_except_table1838
- GCC_except_table189
- GCC_except_table2112
- GCC_except_table2118
- GCC_except_table2135
- GCC_except_table2140
- GCC_except_table2143
- GCC_except_table2146
- GCC_except_table2149
- GCC_except_table2268
- GCC_except_table2286
- GCC_except_table234
- GCC_except_table2420
- GCC_except_table2477
- GCC_except_table2489
- GCC_except_table2522
- GCC_except_table2546
- GCC_except_table2557
- GCC_except_table256
- GCC_except_table259
- GCC_except_table2600
- GCC_except_table2601
- GCC_except_table2602
- GCC_except_table2612
- GCC_except_table2613
- GCC_except_table2617
- GCC_except_table2618
- GCC_except_table2627
- GCC_except_table2635
- GCC_except_table2636
- GCC_except_table2659
- GCC_except_table2925
- GCC_except_table3008
- GCC_except_table3045
- GCC_except_table3071
- GCC_except_table3074
- GCC_except_table3077
- GCC_except_table3108
- GCC_except_table3170
- GCC_except_table3340
- GCC_except_table3368
- GCC_except_table3431
- GCC_except_table3433
- GCC_except_table3435
- GCC_except_table3459
- GCC_except_table3461
- GCC_except_table3463
- GCC_except_table3477
- GCC_except_table3635
- GCC_except_table3659
- GCC_except_table366
- GCC_except_table3719
- GCC_except_table3754
- GCC_except_table3844
- GCC_except_table4094
- GCC_except_table4159
- GCC_except_table4188
- GCC_except_table4238
- GCC_except_table4244
- GCC_except_table4560
- GCC_except_table4716
- GCC_except_table4726
- GCC_except_table4750
- GCC_except_table4770
- GCC_except_table4851
- GCC_except_table4863
- GCC_except_table4872
- GCC_except_table4887
- GCC_except_table4889
- GCC_except_table4900
- GCC_except_table4911
- GCC_except_table4913
- GCC_except_table4931
- GCC_except_table4944
- GCC_except_table4946
- GCC_except_table4948
- GCC_except_table4959
- GCC_except_table4960
- GCC_except_table4963
- GCC_except_table4965
- GCC_except_table4966
- GCC_except_table4967
- GCC_except_table4971
- GCC_except_table4986
- GCC_except_table5112
- GCC_except_table5141
- GCC_except_table5144
- GCC_except_table5326
- GCC_except_table5342
- GCC_except_table5352
- GCC_except_table5359
- GCC_except_table5386
- GCC_except_table5393
- GCC_except_table5395
- GCC_except_table5404
- GCC_except_table560
- GCC_except_table5670
- GCC_except_table5676
- GCC_except_table5709
- GCC_except_table5714
- GCC_except_table5752
- GCC_except_table5761
- GCC_except_table5788
- GCC_except_table5869
- GCC_except_table6089
- GCC_except_table6097
- GCC_except_table6117
- GCC_except_table6122
- GCC_except_table615
- GCC_except_table6228
- GCC_except_table6309
- GCC_except_table6310
- GCC_except_table6320
- GCC_except_table6321
- GCC_except_table6466
- GCC_except_table6488
- GCC_except_table6493
- GCC_except_table6498
- GCC_except_table6505
- GCC_except_table6507
- GCC_except_table6537
- GCC_except_table6628
- GCC_except_table6654
- GCC_except_table6665
- GCC_except_table6668
- GCC_except_table6691
- GCC_except_table6703
- GCC_except_table679
- GCC_except_table683
- GCC_except_table687
- GCC_except_table694
- GCC_except_table6943
- GCC_except_table6978
- GCC_except_table7032
- GCC_except_table7042
- GCC_except_table7044
- GCC_except_table7047
- GCC_except_table7054
- GCC_except_table7059
- GCC_except_table7060
- GCC_except_table7065
- GCC_except_table7071
- GCC_except_table7072
- GCC_except_table7073
- GCC_except_table7074
- GCC_except_table7079
- GCC_except_table7080
- GCC_except_table7085
- GCC_except_table7114
- GCC_except_table7169
- GCC_except_table7193
- GCC_except_table7235
- GCC_except_table7245
- GCC_except_table7255
- GCC_except_table7296
- GCC_except_table7303
- GCC_except_table7327
- GCC_except_table7376
- GCC_except_table7470
- GCC_except_table7533
- GCC_except_table7575
- GCC_except_table7601
- GCC_except_table7618
- GCC_except_table7624
- GCC_except_table7627
- GCC_except_table7635
- GCC_except_table7641
- GCC_except_table7661
- OBJC_IVAR_$_CSAudioInjectionProviderExclave._bufferDuration
- OBJC_IVAR_$_CSAudioInjectionProviderExclave._exclaveAudioQueue
- OBJC_IVAR_$_CSAudioInjectionProviderExclave._fileOption
- OBJC_IVAR_$_CSAudioInjectionProviderExclave._injectionCompletion
- OBJC_IVAR_$_CSAudioInjectionProviderExclave._injectionEndTime
- OBJC_IVAR_$_CSAudioInjectionProviderExclave._injectionStartTime
- OBJC_IVAR_$_CSAudioInjectionProviderExclave._isAudioQueueStarted
- OBJC_IVAR_$_CSAudioInjectionProviderExclave._queue
- OBJC_IVAR_$_CSVoiceTriggerAssetHandlerMac._uafAssetManager
- _AQInjectionOutputCallback
- _AudioQueueNewOutput
- _CC_SHA256
- _CSLogContextFacilityCoreSpeechExclave
- _CSSecureLogInitIfNeeded
- _OBJC_CLASS_$_AFMyriadGoodnessScoreOverrideState
- _OBJC_CLASS_$_CSAudioInjectionProviderExclave
- _OBJC_CLASS_$_SCDAGoodnessScoreOverrideState
- _OBJC_METACLASS_$_CSAudioInjectionProviderExclave
- __109-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:bundleIdentifier:completion:]_block_invoke.15
- __109-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:bundleIdentifier:completion:]_block_invoke.19
- __110+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withfadingTimeWindowLength:handlingDaemon:completion:]_block_invoke.21
- __110-[CSSiriLauncher notifyDarwinVoiceTrigger:deviceId:myriadPHash:myriadLateActivationExpirationTime:completion:]_block_invoke.39
- __110-[CSSiriLauncher notifyDarwinVoiceTrigger:deviceId:myriadPHash:myriadLateActivationExpirationTime:completion:]_block_invoke.42
- __110-[CSVoiceTriggerSecondPass _requestStartAudioStreamWitContext:audioProviderUUID:startStreamOption:completion:]_block_invoke.76
- __112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.175
- __119+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.13
- __119+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:handlingDaemon:completion:]_block_invoke.16
- __121+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:handlingDaemon:completion:]_block_invoke.22
- __133-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.149
- __136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.125
- __30-[CSBuiltInVoiceTrigger start]_block_invoke.34
- __30-[CSBuiltInVoiceTrigger start]_block_invoke.36
- __30-[CSBuiltInVoiceTrigger start]_block_invoke.46
- __30-[CSBuiltInVoiceTrigger start]_block_invoke.54
- __30-[CSBuiltInVoiceTrigger start]_block_invoke.61
- __30-[CSBuiltInVoiceTrigger start]_block_invoke.70
- __30-[CSBuiltInVoiceTrigger start]_block_invoke.73
- __30-[CSBuiltInVoiceTrigger start]_block_invoke_2.55
- __30-[CSBuiltInVoiceTrigger start]_block_invoke_2.62
- __30-[CSBuiltInVoiceTrigger start]_block_invoke_2.71
- __30-[CSBuiltInVoiceTrigger start]_block_invoke_3.63
- __39-[CSBuiltInVoiceTrigger _stopListening]_block_invoke.133
- __40-[CSHybridEndpointer processTaskString:]_block_invoke.403
- __44-[CSBuiltInVoiceTrigger _stopAPVoiceTrigger]_block_invoke.146
- __48+[CSAudioInjectionServices pingpong:completion:]_block_invoke.3
- __48+[CSAudioInjectionServices pingpong:completion:]_block_invoke.5
- __49-[CSVoiceTriggerFirstPassJarvisAP _stopListening]_block_invoke.25
- __50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.44
- __52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.124
- __52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.126
- __52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.38
- __52-[CSVoiceTriggerAssetHandlerMac triggerAssetRefresh]_block_invoke.30
- __54-[CSAttSiriMitigationAssetHandler triggerAssetRefresh]_block_invoke.36
- __54-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke.16
- __56-[CSVoiceTriggerSecondPass _initializeMediaPlayingState]_block_invoke.66
- __56-[CSVoiceTriggerSecondPass _initializeMediaPlayingState]_block_invoke_2.67
- __56-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke.130
- __57-[CSAudioTapProvider startAudioStream:option:completion:]_block_invoke.15
- __62-[CSAudioTapProvider audioStreamWithRequest:streamName:error:]_block_invoke.23
- __62-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke.61
- __62-[CSVoiceTriggerFirstPassJarvisAP _startListenWithCompletion:]_block_invoke.22
- __64-[CSBuiltInVoiceTrigger _handleSecondPassResult:deviceId:error:]_block_invoke.189
- __64-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke.239
- __67-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke.11
- __67-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke.18
- __68-[CSBuiltInVoiceTrigger _startListenPollingWithInterval:completion:]_block_invoke.117
- __69-[CSTrialAssetManager _getSiriAttAssetsForType:forLocale:completion:]_block_invoke.41
- __70-[CSBuiltInVoiceTrigger _setAsset:forceExclaveToUsePreInstalledAsset:]_block_invoke.97
- __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.417
- __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.418
- __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.419
- __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.432
- __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.436
- __70-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2.425
- __71-[CSSpeechManager activationEventNotificationHandler:event:completion:]_block_invoke.69
- __71-[CSSpeechManager activationEventNotificationHandler:event:completion:]_block_invoke_2.70
- __76+[CSAudioInjectionServices connectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.28
- __76-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke.26
- __76-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke.29
- __77-[CSBuiltInVoiceTrigger activationEventNotificationHandler:event:completion:]_block_invoke.194
- __79+[CSAudioInjectionServices disconnectDeviceWithUUID:handlingDaemon:completion:]_block_invoke.30
- __80-[CSAttSiriMitigationAssetHandler _getMitigationAssetWithEndpointId:completion:]_block_invoke.29
- __82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.102
- __82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.95
- __84+[CSAudioInjectionServices primaryInputDeviceUUIDWithhandlingDaemon:WithCompletion:]_block_invoke.32
- __84-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke.33
- __84-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke.35
- __88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.483
- __88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.493
- __93-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromAOP:audioProviderUUID:completion:]_block_invoke.144
- __97-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:]_block_invoke.83
- __Block_byref_object_copy_.10934
- __Block_byref_object_copy_.12186
- __Block_byref_object_copy_.12601
- __Block_byref_object_copy_.1344
- __Block_byref_object_copy_.13706
- __Block_byref_object_copy_.14720
- __Block_byref_object_copy_.16237
- __Block_byref_object_copy_.16681
- __Block_byref_object_copy_.18135
- __Block_byref_object_copy_.19034
- __Block_byref_object_copy_.19494
- __Block_byref_object_copy_.2002
- __Block_byref_object_copy_.20440
- __Block_byref_object_copy_.20916
- __Block_byref_object_copy_.21640
- __Block_byref_object_copy_.22497
- __Block_byref_object_copy_.23235
- __Block_byref_object_copy_.2372
- __Block_byref_object_copy_.24176
- __Block_byref_object_copy_.25468
- __Block_byref_object_copy_.25951
- __Block_byref_object_copy_.26732
- __Block_byref_object_copy_.3263
- __Block_byref_object_copy_.3445
- __Block_byref_object_copy_.3644
- __Block_byref_object_copy_.4160
- __Block_byref_object_copy_.6212
- __Block_byref_object_copy_.7164
- __Block_byref_object_copy_.7946
- __Block_byref_object_copy_.8450
- __Block_byref_object_copy_.9453
- __Block_byref_object_dispose_.10935
- __Block_byref_object_dispose_.12187
- __Block_byref_object_dispose_.12602
- __Block_byref_object_dispose_.1345
- __Block_byref_object_dispose_.13707
- __Block_byref_object_dispose_.14721
- __Block_byref_object_dispose_.16238
- __Block_byref_object_dispose_.16682
- __Block_byref_object_dispose_.18136
- __Block_byref_object_dispose_.19035
- __Block_byref_object_dispose_.19495
- __Block_byref_object_dispose_.2003
- __Block_byref_object_dispose_.20441
- __Block_byref_object_dispose_.20917
- __Block_byref_object_dispose_.21641
- __Block_byref_object_dispose_.22498
- __Block_byref_object_dispose_.23236
- __Block_byref_object_dispose_.2373
- __Block_byref_object_dispose_.24177
- __Block_byref_object_dispose_.25469
- __Block_byref_object_dispose_.25952
- __Block_byref_object_dispose_.26733
- __Block_byref_object_dispose_.3264
- __Block_byref_object_dispose_.3446
- __Block_byref_object_dispose_.3645
- __Block_byref_object_dispose_.4161
- __Block_byref_object_dispose_.6213
- __Block_byref_object_dispose_.7165
- __Block_byref_object_dispose_.7947
- __Block_byref_object_dispose_.8451
- __Block_byref_object_dispose_.9454
- __OBJC_$_CLASS_METHODS_CSAudioInjectionProviderExclave
- __OBJC_$_INSTANCE_METHODS_CSAudioInjectionProviderExclave
- __OBJC_$_INSTANCE_VARIABLES_CSAudioInjectionProviderExclave
- __OBJC_$_PROP_LIST_CSAudioInjectionProviderExclave
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerAssetHandlerExclaveProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerExclaveProtocol
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerExclaveProtocol
- __OBJC_CLASS_RO_$_CSAudioInjectionProviderExclave
- __OBJC_LABEL_PROTOCOL_$_CSVoiceTriggerAssetHandlerExclaveProtocol
- __OBJC_METACLASS_RO_$_CSAudioInjectionProviderExclave
- __OBJC_PROTOCOL_$_CSVoiceTriggerAssetHandlerExclaveProtocol
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPNS_6vectorINS4_IfNS_9allocatorIfEEEENS5_IS7_EEEESA_SA_EENS_4pairIT_T1_EESC_T0_SD_
- __ZNKSt3__111__copy_loopINS_17_ClassicAlgPolicyEEclB8ne180100IPNS_6vectorIfNS_9allocatorIfEEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
- __ZNKSt3__114default_deleteIN10corespeech25CSAudioCircularBufferImplIhEEEclB8ne180100EPS3_
- __ZNKSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIPKhNS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt12out_of_rangeC1B8ne180100EPKc
- __ZNSt3__110unique_ptrI15SmartSiriVolumeNS_14default_deleteIS1_EEE5resetB8ne180100EPS1_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorINS_4pairIfjEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne180100EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ne180100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne180100Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne180100INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ne180100IPS5_S9_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne180100Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne180100IPS3_S7_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne180100IPS3_S7_EEvT_T0_l
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE7__clearB8ne180100Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEEC2EmRKS3_
- __ZNSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE5eraseENS_11__wrap_iterIPKS2_EES9_
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne180100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne180100IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne180100IPfS5_EEvT_T0_l
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2EmRKf
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___122-[CSVoiceIdXPCClient _notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]_block_invoke
- ___40-[CSAudioInjectionProviderExclave start]_block_invoke
- ___49+[CSAudioInjectionProviderExclave sharedInstance]_block_invoke
- ___54-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke
- ___54-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke_2
- ___56-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke
- ___56-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke_2
- ___62-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_2
- ___62-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_3
- ___65-[CSVoiceTriggerAssetHandlerMac mapAssetToExclaveKit:completion:]_block_invoke
- ___69-[CSBuiltInVoiceTrigger setAsset:forceExclaveToUsePreInstalledAsset:]_block_invoke
- ___69-[CSTrialAssetManager _getSiriAttAssetsForType:forLocale:completion:]_block_invoke
- ___70-[CSAudioInjectionProviderExclave speakAudioInExclave:withCompletion:]_block_invoke
- ___70-[CSBuiltInVoiceTrigger _setAsset:forceExclaveToUsePreInstalledAsset:]_block_invoke
- ___72-[CSAudioInjectionProviderExclave _readAudioBufferAndFeedIntoAudioQueue]_block_invoke
- ___84-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke
- ___CSSecureLogInitIfNeeded_block_invoke
- ___ZL25isRunningListenerCallbackPvP16OpaqueAudioQueuej_block_invoke.220
- ___block_descriptor_40_e8_32bs_e15_v16?0"NSURL"8l
- ___block_descriptor_41_e8_32s_e31_v16?0"<SCDAContextMutating>"8l
- ___block_descriptor_41_e8_32s_e35_v16?0"<AFMyriadContextMutating>"8l
- ___block_descriptor_48_e8_32s40bs_e15_v16?0"NSURL"8l
- ___block_descriptor_48_e8_32s_e29_v56?0Q8d16f24f28I32f36Q40Q48l
- ___block_descriptor_49_e8_32s40bs_e32_v64?0Q8Q16d24f32f36I40f44Q48Q56l
- ___block_descriptor_56_e8_32s40bs48bs_e17_v16?0"NSError"8l
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8l
- ___block_descriptor_56_e8_32s40s_e8_v16?0Q8l
- ___block_descriptor_64_e8_32s40s48bs_e21_v20?0i8"NSString"12l
- __block_literal_global.10.20174
- __block_literal_global.10.21473
- __block_literal_global.10.9904
- __block_literal_global.10128
- __block_literal_global.10343
- __block_literal_global.10795
- __block_literal_global.1080
- __block_literal_global.10960
- __block_literal_global.11.3365
- __block_literal_global.11240
- __block_literal_global.11338
- __block_literal_global.11458
- __block_literal_global.1156
- __block_literal_global.11752
- __block_literal_global.11904
- __block_literal_global.12.17056
- __block_literal_global.12389
- __block_literal_global.12505
- __block_literal_global.12727
- __block_literal_global.13.20275
- __block_literal_global.13.21474
- __block_literal_global.13.25881
- __block_literal_global.13121
- __block_literal_global.13178
- __block_literal_global.13449
- __block_literal_global.13467
- __block_literal_global.135
- __block_literal_global.13580
- __block_literal_global.1470
- __block_literal_global.14707
- __block_literal_global.14754
- __block_literal_global.15319
- __block_literal_global.15792
- __block_literal_global.15801
- __block_literal_global.15847
- __block_literal_global.15862
- __block_literal_global.16.12390
- __block_literal_global.16.20175
- __block_literal_global.16.25882
- __block_literal_global.16.9689
- __block_literal_global.16296
- __block_literal_global.17040
- __block_literal_global.17055
- __block_literal_global.17254
- __block_literal_global.17877
- __block_literal_global.18.13550
- __block_literal_global.18.18744
- __block_literal_global.18.20276
- __block_literal_global.18167
- __block_literal_global.18541
- __block_literal_global.1861
- __block_literal_global.18621
- __block_literal_global.18761
- __block_literal_global.18856
- __block_literal_global.18903
- __block_literal_global.18948
- __block_literal_global.19085
- __block_literal_global.19378
- __block_literal_global.194
- __block_literal_global.19518
- __block_literal_global.19594
- __block_literal_global.19745
- __block_literal_global.20.12372
- __block_literal_global.20160
- __block_literal_global.20173
- __block_literal_global.2024
- __block_literal_global.20299
- __block_literal_global.20349
- __block_literal_global.20385
- __block_literal_global.20522
- __block_literal_global.2066
- __block_literal_global.21
- __block_literal_global.2108
- __block_literal_global.211
- __block_literal_global.21471
- __block_literal_global.21965
- __block_literal_global.22.20176
- __block_literal_global.2210
- __block_literal_global.22127
- __block_literal_global.2224
- __block_literal_global.22529
- __block_literal_global.22814
- __block_literal_global.23028
- __block_literal_global.23114
- __block_literal_global.23376
- __block_literal_global.24407
- __block_literal_global.2465
- __block_literal_global.24756
- __block_literal_global.25.20177
- __block_literal_global.25116
- __block_literal_global.25275
- __block_literal_global.25327
- __block_literal_global.25504
- __block_literal_global.2560
- __block_literal_global.25609
- __block_literal_global.25741
- __block_literal_global.25849
- __block_literal_global.25880
- __block_literal_global.26527
- __block_literal_global.26743
- __block_literal_global.27030
- __block_literal_global.27043
- __block_literal_global.2815
- __block_literal_global.29.20178
- __block_literal_global.30.24728
- __block_literal_global.3000
- __block_literal_global.31.18730
- __block_literal_global.3148
- __block_literal_global.33
- __block_literal_global.3317
- __block_literal_global.3364
- __block_literal_global.3435
- __block_literal_global.348
- __block_literal_global.35
- __block_literal_global.3679
- __block_literal_global.4.25276
- __block_literal_global.415
- __block_literal_global.4593
- __block_literal_global.4760
- __block_literal_global.48
- __block_literal_global.5.27044
- __block_literal_global.50.10336
- __block_literal_global.5300
- __block_literal_global.5560
- __block_literal_global.5841
- __block_literal_global.587
- __block_literal_global.5912
- __block_literal_global.5937
- __block_literal_global.6.25499
- __block_literal_global.6269
- __block_literal_global.6419
- __block_literal_global.67
- __block_literal_global.6706
- __block_literal_global.677
- __block_literal_global.7.21472
- __block_literal_global.713
- __block_literal_global.7219
- __block_literal_global.8.1136
- __block_literal_global.8.27045
- __block_literal_global.8022
- __block_literal_global.8598
- __block_literal_global.8651
- __block_literal_global.8671
- __block_literal_global.899
- __block_literal_global.9.20274
- __block_literal_global.9.25603
- __block_literal_global.9052
- __block_literal_global.9562
- __block_literal_global.9706
- __block_literal_global.980
- __block_literal_global.9929
- _block_invoke.enableHeartbeat.10124
- _block_invoke.enableHeartbeat.26239
- _handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.17801
- _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10109
- _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.17790
- _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.26215
- _objc_msgSend$UAFLevelForFactor:withNamespaceName:withLanguage:
- _objc_msgSend$_createAudioQueueIfNeeded
- _objc_msgSend$_defaultBufferRef
- _objc_msgSend$_getSiriAttAssetsForType:forLocale:completion:
- _objc_msgSend$_notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:
- _objc_msgSend$_prepareAndStartAudioQueue
- _objc_msgSend$_processSecondPassInExclave:
- _objc_msgSend$_readAudioBufferAndFeedIntoAudioQueue
- _objc_msgSend$_setAsset:forceExclaveToUsePreInstalledAsset:
- _objc_msgSend$_setAudioSessionActive:
- _objc_msgSend$_sha256:
- _objc_msgSend$bestSupportedLanguageCodeForLanguageCode:
- _objc_msgSend$bypassTrialAssets
- _objc_msgSend$cleanupVoiceProfileModelFilesForLocale:withAsset:
- _objc_msgSend$enableExclaveAudioInjection:
- _objc_msgSend$exclaveAudioInjectionEnabled
- _objc_msgSend$initWithOverrideOption:reason:
- _objc_msgSend$linkItemAtURL:toURL:error:
- _objc_msgSend$metadata
- _objc_msgSend$notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:
- _objc_msgSend$relativePath
- _objc_msgSend$setAsset:forceExclaveToUsePreInstalledAsset:
- _objc_msgSend$setOverrideState:
- _runVoiceProfileRetrainerWithAsset:withLanguageCode:.onceCleanupToken
- kEnhancedEndpointerTaskTypeDefault_block_invoke.heartbeat_CORESPEECH_HYBRID_CLASSIFIER_PROCESS_END
- kEnhancedEndpointerTaskTypeDefault_block_invoke.heartbeat_CORESPEECH_PROCESS_SIL_SCORE_ESTIMATE_BEGIN
- sharedController.onceToken.10959
- sharedController.sharedController.10961
- sharedHandler.onceToken.18540
- sharedHandler.onceToken.25503
- sharedHandler.onceToken.979
- sharedHandler.sharedHandler.18542
- sharedHandler.sharedHandler.25505
- sharedHandler.sharedHandler.981
- sharedHandlerDisabledOnDeviceCompilation.onceToken.25498
- sharedHandlerDisabledOnDeviceCompilation.sharedHandler.25500
- sharedInstance._sharedInstance.10796
- sharedInstance._sharedInstance.11905
- sharedInstance._sharedInstance.13179
- sharedInstance._sharedInstance.13581
- sharedInstance._sharedInstance.15848
- sharedInstance._sharedInstance.18904
- sharedInstance._sharedInstance.19379
- sharedInstance._sharedInstance.19595
- sharedInstance._sharedInstance.22815
- sharedInstance._sharedInstance.23377
- sharedInstance._sharedInstance.2466
- sharedInstance._sharedInstance.25328
- sharedInstance._sharedInstance.26744
- sharedInstance._sharedInstance.27031
- sharedInstance._sharedInstance.2816
- sharedInstance._sharedInstance.5561
- sharedInstance._sharedInstance.5913
- sharedInstance._sharedInstance.6420
- sharedInstance._sharedInstance.678
- sharedInstance._sharedInstance.714
- sharedInstance._sharedInstance.8652
- sharedInstance.onceToken.10794
- sharedInstance.onceToken.1155
- sharedInstance.onceToken.11903
- sharedInstance.onceToken.12504
- sharedInstance.onceToken.13177
- sharedInstance.onceToken.13579
- sharedInstance.onceToken.14706
- sharedInstance.onceToken.15846
- sharedInstance.onceToken.16295
- sharedInstance.onceToken.17039
- sharedInstance.onceToken.17253
- sharedInstance.onceToken.18760
- sharedInstance.onceToken.18855
- sharedInstance.onceToken.18902
- sharedInstance.onceToken.193
- sharedInstance.onceToken.19377
- sharedInstance.onceToken.19593
- sharedInstance.onceToken.20159
- sharedInstance.onceToken.20298
- sharedInstance.onceToken.20384
- sharedInstance.onceToken.20521
- sharedInstance.onceToken.21964
- sharedInstance.onceToken.22126
- sharedInstance.onceToken.22528
- sharedInstance.onceToken.22813
- sharedInstance.onceToken.23113
- sharedInstance.onceToken.23375
- sharedInstance.onceToken.2464
- sharedInstance.onceToken.25115
- sharedInstance.onceToken.25326
- sharedInstance.onceToken.2559
- sharedInstance.onceToken.26526
- sharedInstance.onceToken.26742
- sharedInstance.onceToken.27029
- sharedInstance.onceToken.2814
- sharedInstance.onceToken.3147
- sharedInstance.onceToken.414
- sharedInstance.onceToken.4592
- sharedInstance.onceToken.4759
- sharedInstance.onceToken.5299
- sharedInstance.onceToken.5559
- sharedInstance.onceToken.586
- sharedInstance.onceToken.5911
- sharedInstance.onceToken.6418
- sharedInstance.onceToken.676
- sharedInstance.onceToken.712
- sharedInstance.onceToken.8650
- sharedInstance.onceToken.9705
- sharedInstance.onceToken.9928
- sharedInstance.sSharedInstance.17255
- sharedInstance.sharedInstance.12506
- sharedInstance.sharedInstance.17041
- sharedInstance.sharedInstance.18762
- sharedInstance.sharedInstance.18857
- sharedInstance.sharedInstance.20161
- sharedInstance.sharedInstance.20386
- sharedInstance.sharedInstance.22128
- sharedInstance.sharedInstance.22530
- sharedInstance.sharedInstance.26528
- sharedInstance.sharedInstance.3149
- sharedInstance.sharedInstance.4594
- sharedInstance.sharedInstance.4761
- sharedInstance.sharedInstance.5301
- sharedInstance.sharedManager.25117
- sharedInstance.sharedPolicy.1157
- sharedInstance.sharedPolicy.20300
- sharedInstance.sharedPolicy.23115
- sharedInstance.sharedProvider.21966
- sharedManager.onceToken.15791
- sharedManager.onceToken.18166
- sharedManager.onceToken.5936
- sharedManager.onceToken.6705
- sharedManager.sharedManager.15793
- sharedManager.sharedManager.5938
- sharedManager.sharedManager.6707
- sharedMonitor.onceToken.19517
- sharedMonitor.sharedMonitor.19519
- sharedService.onceToken.14753
- sharedService.onceToken.24755
- sharedService.sharedService.24757
CStrings:
+ "\t"
+ "%s AOP trigger timestamp was 4 seconds the current time. Ignoring AOP trigger due to trigger time CONSTRAINT check"
+ "%s Asset Provider:%ld, Asset Variant: %ld, attemptAssetMapping:%d"
+ "%s CoreSpeech SystemDaemon crashed"
+ "%s CoreSpeech SystemDaemon recovered from crash"
+ "%s Detected 2nd-pass trigger at %{public}llu, KeywordDetectionBucket : %@, SpeakerDetectionBucket : %@"
+ "%s Failed retrying to map asset with error %@"
+ "%s Failed retrying to map asset with version:%@"
+ "%s Fetched installed voicetrigger asset %@"
+ "%s Magus is not supported since locale is coupled with SAE and is ineligible"
+ "%s Mapping asset failed. Falling back to preinstalled asset with version:%@"
+ "%s Mapping is not supported hardware with no exclaves"
+ "%s Mapping is not supported hardware with no exclaves. Aborting retries."
+ "%s New task string: %{public}@, current task string: %{public}@"
+ "%s Rejected 2nd-pass KeywordDetectionBucket : %@, SpeakerDetectionBucket : %@"
+ "%s Should retry mapping asset? %@"
+ "%s SpeechController to receive data from VoiceIsolation Channel: %{public}tu"
+ "%s Successfully mapped asset with version:%@"
+ "%s Unable to access app container group"
+ "%s Unable to find endpointer model for default task %{public}@"
+ "%s corespeechd_system crashed"
+ "%s corespeechd_system recovered from crash"
+ "%s isSupported=%@: Is request during active call? %@, isDeviceSupported: %@, isFFEnabledOnDevice: %@, isSupportedRequestType: %@, isFFUserDisabled: %@, isTypeToSiriEnabled: %@, isLocaleInDenyList:%@, isSAEEnabled:%@, isLocaleUnsupportedWithSAE:%@ isLocaleCoupledWithSAE:%@"
+ "%s languageCode:  %{public}@ -voiceProfileArray: %{public}@, _currentAssets:%@"
+ "-[CSAudioSessionInfoProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]_block_invoke"
+ "-[CSAudioSessionInfoProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]_block_invoke"
+ "-[CSAudioTapProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]"
+ "-[CSAudioTapProvider CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]"
+ "-[CSBuiltInVoiceTrigger CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:]"
+ "-[CSBuiltInVoiceTrigger CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:]"
+ "-[CSBuiltInVoiceTrigger _setAsset:]"
+ "-[CSBuiltInVoiceTrigger _setAsset:]_block_invoke"
+ "-[CSSiriLauncher notifyCarPlayVoiceTrigger:deviceId:myriadPHash:completion:]_block_invoke_3"
+ "-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSSpeechManager _mapAssetToExclaveKit:completion:]_block_invoke_2"
+ "-[CSSpeechManager _retryMapAssetToExclaveKit:]_block_invoke"
+ "-[CSVoiceIdXPCClient _notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke"
+ "-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke_2"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke"
+ "-[CSVoiceTriggerAssetHandler mapAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSVoiceTriggerAssetHandler retryMappingAssetToExclaveKit:completion:]_block_invoke"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]"
+ "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke_2"
+ "CSMacUserSessionMonitorDelegate"
+ "CSSystemDaemonStateMonitorDelegate"
+ "CSSystemDaemonStateMonitorDidReceiveSysDaemonCrash:"
+ "CSSystemDaemonStateMonitorDidReceiveSysDaemonRestartFromCrash:"
+ "Detected"
+ "Failed retrying to map asset with version:%@"
+ "Fallback_Secure_PreinstalledAsset"
+ "Mapping asset failed. Falling back to preinstalled asset with version:%@"
+ "Mapping_Secure_Asset_Succeeded"
+ "NearMiss"
+ "Rejected"
+ "Retry_Mapping_Secure_Asset_Failed"
+ "StrongAccept"
+ "StrongReject"
+ "Successfully mapped asset with version:%@"
+ "T@\"NSString\",&,N,V_currentTaskString"
+ "URLByAppendingPathComponent:isDirectory:"
+ "Vv32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSURL\">24"
+ "WeakAccept"
+ "WeakReject"
+ "_currentTaskString"
+ "_handleImplicitUtteranceMessage:client:"
+ "_isTaskStringAccessible:"
+ "_mapAssetToExclaveKit:completion:"
+ "_notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
+ "_processSecondPassInExclave:rejectBlock:"
+ "_retryMapAssetToExclaveKit:"
+ "_runRetrainerWithAssets:languageCode:"
+ "_shouldUseVoiceIsolationChannel"
+ "_siriLanguageCode"
+ "_tearDownBuiltInVoiceTrigger"
+ "appContainerName"
+ "ay12!Rd"
+ "channelForVoiceIsolation"
+ "cleanupVoiceProfileModelFilesForLocale:withAssets:"
+ "containerURLForSecurityApplicationGroupIdentifier:"
+ "convertSecureVoiceTriggerKeywordDetectionResultTypeToString:"
+ "convertSecureVoiceTriggerSpeakerDetectionResultTypeToString:"
+ "copyItemAtURL:toURL:error:"
+ "currentTaskString"
+ "enforceAutomaticEndpointing"
+ "getBestSupportedSiriLanguageWithFallback:"
+ "group.com.apple.siri.recorded-audio"
+ "installedCompactAssetOfType:language:"
+ "isCompactVersion"
+ "isMagusRestrictedWithSAEForLanguageCode:"
+ "macUserSessionMonitor:sessionActive:"
+ "notifyImplicitUtterance:appContainerName:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
+ "retryMappingAssetToExclaveKit:completion:"
+ "setAudioProviderImp:"
+ "setCurrentTaskString:"
+ "sha1StringFromInputData:"
+ "sha256DataFromInputData:"
+ "sharedContollerProxy"
+ "supportsPersonalizedHeySiri"
+ "supportsSystemDaemon"
+ "v24@0:8@\"CSSystemDaemonStateMonitor\"16"
+ "v24@?0@\"NSString\"8@\"NSURL\"16"
+ "v60@?0Q8d16I24Q28Q36Q44Q52"
+ "v68@?0Q8Q16d24I32Q36Q44Q52Q60"
+ "v72@0:8@16@24@32@40@48@56@?64"
- "\n"
- "%s %@ - %@"
- "%s ::: CoreSpeech Secure logging initialized"
- "%s Asset handler %@ does not support mapping asset to EK. This is a critical error"
- "%s AudioQueue call back is asking for audio, injected file has been found"
- "%s AudioQueue call back is asking for audio, injected file is not available, injecting digital 1s"
- "%s Client request to speak audio into exclave with URL: %@ at time: %llu"
- "%s Detected 2nd-pass trigger at %{public}llu"
- "%s Failed to create Exclave Audio Injection AudioQueue with OSStatus error: %d"
- "%s Failed to feed audio into exclave, AQ or AQBuffer is invalid"
- "%s Failed to feed audio into exclave, unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
- "%s Failed to feed audio into exclave, unable to enqueue AQ buffer with OSStatus: %d"
- "%s Failed to feed audio into exclave, unable to locate available audio queue"
- "%s Failed to feed audio into exclave, unable to start AQ buffer with OSStatus: %d"
- "%s Falling back to preinstalled assets for EK"
- "%s Fetched exclave audio injection enabled : %d"
- "%s Got Trial rollout for assetType: %lu for locale: %@ version: %@"
- "%s Overriding Myriad state as request was made during a ringtone"
- "%s Setting exclave audio injection enabled : %d"
- "%s Successfully start the audio queue"
- "%s Unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
- "%s Unable to find endpointer model for default task type %{public}@"
- "%s injection is ended at time: %llu"
- "%s isSupported=%@: Is request during active call? %@, isDeviceSupported: %@, isFFEnabledOnDevice: %@, isSupportedRequestType: %@, isFFUserDisabled: %@, isTypeToSiriEnabled: %@, isLocaleInDenyList:%@, isSAEEnabled:%@"
- "%s languageCode:  %{public}@ -voiceProfileArray: %{public}@, _currentAsset:%@"
- "-[CSAudioInjectionProviderExclave _createAudioQueueIfNeeded]"
- "-[CSAudioInjectionProviderExclave _defaultBufferRef]"
- "-[CSAudioInjectionProviderExclave _prepareAndStartAudioQueue]"
- "-[CSAudioInjectionProviderExclave _readAudioBufferAndFeedIntoAudioQueue]_block_invoke"
- "-[CSAudioInjectionProviderExclave speakAudioInExclave:withCompletion:]_block_invoke"
- "-[CSBuiltInVoiceTrigger _setAsset:forceExclaveToUsePreInstalledAsset:]"
- "-[CSBuiltInVoiceTrigger _setAsset:forceExclaveToUsePreInstalledAsset:]_block_invoke"
- "-[CSBuiltInVoiceTrigger setAsset:forceExclaveToUsePreInstalledAsset:]"
- "-[CSSpeechManager _setAssetForBuiltInVoiceTrigger:completion:]_block_invoke_3"
- "-[CSTrialAssetManager _getSiriAttAssetsForType:forLocale:completion:]_block_invoke"
- "-[CSVoiceIdXPCClient _notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:]"
- "-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke"
- "-[CSVoiceIdXPCConnection _handleClientMessage:client:]_block_invoke_2"
- "-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]"
- "-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke"
- "-[CSVoiceTriggerAssetHandlerMac mapAssetToExclaveKit:completion:]_block_invoke"
- "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]"
- "-[CSVoiceTriggerSecondPass _processSecondPassInExclave:]_block_invoke_2"
- "CSAudioInjectionProviderExclave"
- "CSSecureLogInitIfNeeded_block_invoke"
- "CSVoiceTriggerAssetHandlerExclaveProtocol"
- "ExclaveKit"
- "Mismatch between Current locale: %@ & Trial rollout locale: %@"
- "RecordedAudio"
- "T@?,C,N,V_injectionCompletion"
- "TB,N,V_isAudioQueueStarted"
- "TQ,N,V_injectionEndTime"
- "TQ,N,V_injectionStartTime"
- "T^{OpaqueAudioQueue=},N,V_exclaveAudioQueue"
- "Trial asset bypass is set"
- "Trigger was during a ringtone"
- "UAFLevelForFactor:withNamespaceName:withLanguage:"
- "Unable to get Trial factor: %@"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSURL\">24"
- "^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16@0:8"
- "_createAudioQueueIfNeeded"
- "_defaultBufferRef"
- "_exclaveAudioQueue"
- "_getSiriAttAssetsForType:forLocale:completion:"
- "_injectionCompletion"
- "_injectionEndTime"
- "_injectionStartTime"
- "_isAudioQueueStarted"
- "_notifyImplicitUtterance:audioDeviceType:audioRecordType:voiceTriggerEventInfo:otherCtxt:completion:"
- "_prepareAndStartAudioQueue"
- "_processSecondPassInExclave:"
- "_readAudioBufferAndFeedIntoAudioQueue"
- "_setAsset:forceExclaveToUsePreInstalledAsset:"
- "_setAudioSessionActive:"
- "_sha256:"
- "ay12!Rc"
- "bestSupportedLanguageCodeForLanguageCode:"
- "bypassTrialAssets"
- "cleanupVoiceProfileModelFilesForLocale:withAsset:"
- "enableExclaveAudioInjection:"
- "exclave-built-in"
- "exclaveAudioInjectionEnabled"
- "exclaveAudioQueue"
- "initWithOverrideOption:reason:"
- "injectionCompletion"
- "injectionEndTime"
- "injectionStartTime"
- "isAudioQueueStarted"
- "linkItemAtURL:toURL:error:"
- "metadata"
- "relativePath"
- "setAsset:forceExclaveToUsePreInstalledAsset:"
- "setExclaveAudioQueue:"
- "setInjectionCompletion:"
- "setInjectionEndTime:"
- "setInjectionStartTime:"
- "setIsAudioQueueStarted:"
- "setOverrideState:"
- "speakAudioInExclave:withCompletion:"
- "v16@?0@\"NSURL\"8"
- "v32@0:8@\"CSAsset\"16@?<v@?@\"NSError\">24"
- "v56@?0Q8d16f24f28I32f36Q40Q48"
- "v64@?0Q8Q16d24f32f36I40f44Q48Q56"

```
