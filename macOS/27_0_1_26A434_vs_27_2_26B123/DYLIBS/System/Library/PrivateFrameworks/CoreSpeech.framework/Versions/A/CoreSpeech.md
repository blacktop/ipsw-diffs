## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech`

```diff

-3600.70.47.0.0
-  __TEXT.__text: 0x13f47c
+3605.32.1.14.1
+  __TEXT.__text: 0x13f6bc
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x14038
-  __TEXT.__const: 0x40c
+  __TEXT.__objc_methlist: 0x140ac
+  __TEXT.__const: 0x42c
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0x3194
-  __TEXT.__cstring: 0x2559f
-  __TEXT.__oslogstring: 0x1e169
-  __TEXT.__unwind_info: 0x4ad0
+  __TEXT.__gcc_except_tab: 0x321c
+  __TEXT.__cstring: 0x256a7
+  __TEXT.__oslogstring: 0x1e4e7
+  __TEXT.__unwind_info: 0x4ad8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd40
+  __DATA_CONST.__const: 0xd78
   __DATA_CONST.__objc_classlist: 0x838
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x4b0
+  __DATA_CONST.__objc_protolist: 0x4a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xa518
-  __DATA_CONST.__objc_protorefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0xa5c8
+  __DATA_CONST.__objc_protorefs: 0x98
   __DATA_CONST.__objc_superrefs: 0x658
-  __DATA_CONST.__objc_arraydata: 0x3f0
-  __DATA_CONST.__got: 0x1890
-  __AUTH_CONST.__const: 0x5920
-  __AUTH_CONST.__cfstring: 0x9180
-  __AUTH_CONST.__objc_const: 0x1fb60
+  __DATA_CONST.__objc_arraydata: 0x3f8
+  __DATA_CONST.__got: 0x18a0
+  __AUTH_CONST.__const: 0x59f0
+  __AUTH_CONST.__cfstring: 0x9120
+  __AUTH_CONST.__objc_const: 0x1fce8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8
-  __AUTH_CONST.__objc_intobj: 0x900
+  __AUTH_CONST.__objc_intobj: 0x918
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_floatobj: 0x4d0
-  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__auth_got: 0xc18
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x3b60
-  __DATA.__objc_ivar: 0x1828
-  __DATA.__data: 0x37d4
+  __DATA.__objc_ivar: 0x184c
+  __DATA.__data: 0x3774
   __DATA.__bss: 0x5c8
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x16d0
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7797
-  Symbols:   17140
-  CStrings:  5173
+  Functions: 7810
+  Symbols:   17170
+  CStrings:  5181
 
Symbols:
+ -[CSAttSiriAudioSessionStateClient dispatchStateChangedFrom:to:hostTime:]
+ -[CSAttSiriAudioSessionStateClient setTtsEndHostTime:]
+ -[CSAttSiriAudioSessionStateClient ttsEndHostTime]
+ -[CSAttSiriMitigationAssetProvider getMitigationAssetWithCompletion:]
+ -[CSEndpointDelayReporter analytics]
+ -[CSEndpointDelayReporter selfLoggingStream]
+ -[CSEndpointDelayReporter setAnalytics:]
+ -[CSEndpointDelayReporter setSelfLoggingStream:]
+ -[CSSiriAudioActivationInfo myriadElectionIdentity]
+ -[CSSiriSpeechRecorder _playStopAlertWithError:]
+ -[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]
+ -[CSSiriSpeechRecorder electionLedger]
+ -[CSSiriSpeechRecorder setElectionLedger:]
+ -[CSSiriSpeechRecorder suppressUtteranceGradingIfRequiredForElection:]
+ -[CSSpeechController _invalidateRecordSessionActivationState]
+ -[CSSpeechController _noteAudioSessionActivatedForRecord:]
+ -[CSSpeechController _notifyDelegateDidStartRecordingSuccessfully:error:]
+ -[CSSpeechController didActivateAudioSessionForRecord]
+ -[CSSpeechController prefetchedAudioDeviceInfo]
+ -[CSSpeechController setDidActivateAudioSessionForRecord:]
+ -[CSSpeechController setPrefetchedAudioDeviceInfo:]
+ -[CSVoiceIdXPCConnection delegate]
+ -[CSVoiceIdXPCConnection setDelegate:]
+ -[CSVoiceTriggerAPModeSuspendPolicyIOS _isHearstRouted]
+ -[CSVoiceTriggerAPModeSuspendPolicyIOS _isPhoneCallActive]
+ -[CSVoiceTriggerAssetHandlerMac _handleTriggerAssetRefresh]
+ -[CSVoiceTriggerAssetHandlerMac compileAndUpdateDeviceCachesWithAsset:assetType:endpointId:]
+ -[CSVoiceTriggerEnabledPolicyATVExclave _addVoiceTriggerEnabledConditions]
+ -[CSVoiceTriggerEnabledPolicyATVExclave _subscribeEventMonitors]
+ -[CSVoiceTriggerEnabledPolicyATVExclave init]
+ -[CSVoiceTriggerSecondPass requestExclaveAudio]
+ -[CSVoiceTriggerSecondPass setRequestExclaveAudio:]
+ -[CSXPCClient _sendMessageAndReplySync:reply:error:]
+ -[CSXPCClient activateAudioSessionWithReason:dynamicAttribute:bundleID:audioDeviceInfo:error:]
+ GCC_except_table1241
+ GCC_except_table1255
+ GCC_except_table1462
+ GCC_except_table1536
+ GCC_except_table1588
+ GCC_except_table1612
+ GCC_except_table1616
+ GCC_except_table1632
+ GCC_except_table1635
+ GCC_except_table1661
+ GCC_except_table1668
+ GCC_except_table1677
+ GCC_except_table1780
+ GCC_except_table1786
+ GCC_except_table180
+ GCC_except_table1846
+ GCC_except_table1872
+ GCC_except_table1878
+ GCC_except_table1959
+ GCC_except_table1981
+ GCC_except_table2085
+ GCC_except_table210
+ GCC_except_table2222
+ GCC_except_table2225
+ GCC_except_table2228
+ GCC_except_table2233
+ GCC_except_table2245
+ GCC_except_table2250
+ GCC_except_table2253
+ GCC_except_table2256
+ GCC_except_table2259
+ GCC_except_table2352
+ GCC_except_table2397
+ GCC_except_table2402
+ GCC_except_table2409
+ GCC_except_table2427
+ GCC_except_table2457
+ GCC_except_table2570
+ GCC_except_table261
+ GCC_except_table2629
+ GCC_except_table2641
+ GCC_except_table2672
+ GCC_except_table2697
+ GCC_except_table2708
+ GCC_except_table272
+ GCC_except_table2742
+ GCC_except_table2744
+ GCC_except_table2745
+ GCC_except_table2753
+ GCC_except_table2756
+ GCC_except_table2757
+ GCC_except_table2761
+ GCC_except_table2770
+ GCC_except_table2776
+ GCC_except_table2778
+ GCC_except_table2779
+ GCC_except_table2807
+ GCC_except_table286
+ GCC_except_table289
+ GCC_except_table3079
+ GCC_except_table3154
+ GCC_except_table3191
+ GCC_except_table3221
+ GCC_except_table3224
+ GCC_except_table3227
+ GCC_except_table3258
+ GCC_except_table3318
+ GCC_except_table3475
+ GCC_except_table3501
+ GCC_except_table3529
+ GCC_except_table3567
+ GCC_except_table3568
+ GCC_except_table3570
+ GCC_except_table3572
+ GCC_except_table3590
+ GCC_except_table3592
+ GCC_except_table3594
+ GCC_except_table3596
+ GCC_except_table3598
+ GCC_except_table3600
+ GCC_except_table3603
+ GCC_except_table3611
+ GCC_except_table3621
+ GCC_except_table3623
+ GCC_except_table3625
+ GCC_except_table3629
+ GCC_except_table3631
+ GCC_except_table3632
+ GCC_except_table3633
+ GCC_except_table3634
+ GCC_except_table3636
+ GCC_except_table3638
+ GCC_except_table3644
+ GCC_except_table3646
+ GCC_except_table3666
+ GCC_except_table3669
+ GCC_except_table3781
+ GCC_except_table3805
+ GCC_except_table3871
+ GCC_except_table3887
+ GCC_except_table3908
+ GCC_except_table395
+ GCC_except_table4000
+ GCC_except_table4253
+ GCC_except_table4310
+ GCC_except_table4311
+ GCC_except_table4315
+ GCC_except_table4318
+ GCC_except_table4322
+ GCC_except_table4347
+ GCC_except_table4350
+ GCC_except_table4405
+ GCC_except_table4411
+ GCC_except_table4768
+ GCC_except_table4928
+ GCC_except_table4938
+ GCC_except_table4962
+ GCC_except_table4982
+ GCC_except_table5066
+ GCC_except_table5080
+ GCC_except_table5104
+ GCC_except_table5106
+ GCC_except_table5109
+ GCC_except_table5117
+ GCC_except_table5121
+ GCC_except_table5127
+ GCC_except_table5129
+ GCC_except_table5147
+ GCC_except_table5154
+ GCC_except_table5159
+ GCC_except_table5161
+ GCC_except_table5165
+ GCC_except_table5166
+ GCC_except_table5167
+ GCC_except_table5171
+ GCC_except_table5182
+ GCC_except_table5183
+ GCC_except_table5188
+ GCC_except_table5203
+ GCC_except_table5234
+ GCC_except_table5343
+ GCC_except_table5373
+ GCC_except_table5376
+ GCC_except_table5466
+ GCC_except_table5480
+ GCC_except_table5487
+ GCC_except_table5507
+ GCC_except_table5511
+ GCC_except_table5521
+ GCC_except_table5765
+ GCC_except_table5771
+ GCC_except_table5804
+ GCC_except_table5809
+ GCC_except_table5846
+ GCC_except_table5855
+ GCC_except_table5885
+ GCC_except_table597
+ GCC_except_table5971
+ GCC_except_table6195
+ GCC_except_table6203
+ GCC_except_table6223
+ GCC_except_table6228
+ GCC_except_table6337
+ GCC_except_table6407
+ GCC_except_table6429
+ GCC_except_table6430
+ GCC_except_table6440
+ GCC_except_table6441
+ GCC_except_table6453
+ GCC_except_table6484
+ GCC_except_table6495
+ GCC_except_table6500
+ GCC_except_table6505
+ GCC_except_table6537
+ GCC_except_table655
+ GCC_except_table6619
+ GCC_except_table6645
+ GCC_except_table6656
+ GCC_except_table6682
+ GCC_except_table6694
+ GCC_except_table6737
+ GCC_except_table6883
+ GCC_except_table6919
+ GCC_except_table6970
+ GCC_except_table7025
+ GCC_except_table7048
+ GCC_except_table7084
+ GCC_except_table7103
+ GCC_except_table7113
+ GCC_except_table7123
+ GCC_except_table7164
+ GCC_except_table7171
+ GCC_except_table7193
+ GCC_except_table720
+ GCC_except_table724
+ GCC_except_table7242
+ GCC_except_table728
+ GCC_except_table7333
+ GCC_except_table7334
+ GCC_except_table7335
+ GCC_except_table7336
+ GCC_except_table7337
+ GCC_except_table7342
+ GCC_except_table735
+ GCC_except_table7406
+ GCC_except_table7454
+ GCC_except_table7460
+ GCC_except_table7463
+ GCC_except_table7471
+ GCC_except_table7477
+ GCC_except_table7502
+ GCC_except_table7508
+ GCC_except_table7514
+ GCC_except_table7646
+ GCC_except_table903
+ GCC_except_table921
+ GCC_except_table926
+ OBJC_IVAR_$_CSAttSiriAudioSessionStateClient._ttsEndHostTime
+ OBJC_IVAR_$_CSEndpointDelayReporter._analytics
+ OBJC_IVAR_$_CSEndpointDelayReporter._selfLoggingStream
+ OBJC_IVAR_$_CSSiriAudioActivationInfo._myriadElectionIdentity
+ OBJC_IVAR_$_CSSiriSpeechRecorder._electionLedgerOverride
+ OBJC_IVAR_$_CSSiriSpeechRecordingContext._electionIdentity
+ OBJC_IVAR_$_CSSpeechController._didActivateAudioSessionForRecord
+ OBJC_IVAR_$_CSSpeechController._prefetchedAudioDeviceInfo
+ OBJC_IVAR_$_CSVoiceIdXPCConnection._delegate
+ OBJC_IVAR_$_CSVoiceTriggerSecondPass._requestExclaveAudio
+ _AFIsWaffleiron
+ _OBJC_CLASS_$_CSFModelConfigDecoder
+ _OBJC_CLASS_$_CSPickableRouteChangeMonitor
+ _OBJC_CLASS_$_CSVoiceTriggerEnabledPolicyATVExclave
+ _OBJC_CLASS_$_SCDAElectionLedger
+ _OBJC_METACLASS_$_CSVoiceTriggerEnabledPolicyATVExclave
+ __70-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequiredForElection:]_block_invoke
+ __74-[CSVoiceTriggerEnabledPolicyATVExclave _addVoiceTriggerEnabledConditions]_block_invoke
+ __79-[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]_block_invoke
+ __97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2
+ __OBJC_$_INSTANCE_METHODS_CSVoiceTriggerEnabledPolicyATVExclave
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionProviding
+ __OBJC_CLASS_RO_$_CSVoiceTriggerEnabledPolicyATVExclave
+ __OBJC_METACLASS_RO_$_CSVoiceTriggerEnabledPolicyATVExclave
+ ___52-[CSXPCClient _sendMessageAndReplySync:reply:error:]_block_invoke
+ ___58-[CSSpeechController _noteAudioSessionActivatedForRecord:]_block_invoke
+ ___59-[CSVoiceTriggerAssetHandlerMac _handleTriggerAssetRefresh]_block_invoke
+ ___69-[CSAttSiriMitigationAssetProvider getMitigationAssetWithCompletion:]_block_invoke
+ ___70-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequiredForElection:]_block_invoke
+ ___70-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequiredForElection:]_block_invoke_2
+ ___74-[CSVoiceTriggerEnabledPolicyATVExclave _addVoiceTriggerEnabledConditions]_block_invoke
+ ___79-[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]_block_invoke
+ ___79-[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e32_v20?0B8"SCDAElectionOutcome"12l
+ ___block_descriptor_40_e8_32bs_e8_v12?0B8l
+ ___block_descriptor_41_e8_32bs_e5_v8?0l
+ ___block_descriptor_49_e8_32s40w_e8_v12?0B8l
+ ___block_descriptor_59_e8_32s40r_e20_v20?0B8"NSError"12l
+ ___block_descriptor_64_e8_32s40s48r56w_e29_v24?0"CSAsset"8"NSError"16l
+ ___block_descriptor_68_e8_32s40s48r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48r56w
+ ___destroy_helper_block_e8_32s40s48r56w
+ _objc_msgSend$_handleTriggerAssetRefresh
+ _objc_msgSend$_invalidateRecordSessionActivationState
+ _objc_msgSend$_isHearstRouted
+ _objc_msgSend$_isPhoneCallActive
+ _objc_msgSend$_noteAudioSessionActivatedForRecord:
+ _objc_msgSend$_notifyDelegateDidStartRecordingSuccessfully:error:
+ _objc_msgSend$_playStopAlertWithError:
+ _objc_msgSend$_sendMessageAndReplySync:reply:error:
+ _objc_msgSend$_waitForElectionThenPlayStopAlertWithError:recordRoute:
+ _objc_msgSend$activateAudioSessionWithReason:dynamicAttribute:bundleID:audioDeviceInfo:error:
+ _objc_msgSend$analytics
+ _objc_msgSend$candidates
+ _objc_msgSend$clearLogFilesInDirectory:matchingPatterns:exceedNumber:
+ _objc_msgSend$compileAndUpdateDeviceCachesWithAsset:assetType:endpointId:
+ _objc_msgSend$decisionForElection:reason:detail:deliverOn:completion:
+ _objc_msgSend$decodeJsonFromFile:
+ _objc_msgSend$defaultOptionWithTimeout:requestExclaveAudio:
+ _objc_msgSend$dispatchStateChangedFrom:to:hostTime:
+ _objc_msgSend$electionLedger
+ _objc_msgSend$initWithTimeout:clientIdentity:requireRecordModeLock:requireListeningMicIndicatorLock:requestExclaveAudio:
+ _objc_msgSend$isATVFarFieldVoiceTriggerSupportedLanguageCode:
+ _objc_msgSend$isOdeonProxyVoiceTriggered
+ _objc_msgSend$myriadElectionIdentity
+ _objc_msgSend$notifyRequestCompletionAtHostTime:
+ _objc_msgSend$purgeCachedConfigs
+ _objc_msgSend$requestExclaveAudio
+ _objc_msgSend$selfLoggingStream
+ _objc_msgSend$sharedLedger
+ _objc_msgSend$streamRequest
+ _objc_msgSend$supportEarlyRecordingStartNotification
+ _objc_msgSend$suppressUtteranceGradingIfRequiredForElection:
+ _objc_msgSend$voiceIdXPCConnectionDidInvalidate:
- +[SpeechModelTrainingClient initialize]
- -[CSAttSiriAudioSessionStateClient dispatchStateChangedFrom:to:]
- -[CSVoiceTriggerAPModeSuspendPolicyIOS _isHearstRoutedAndWithNoPhoneCall]
- -[SpeechModelTrainingClient .cxx_destruct]
- -[SpeechModelTrainingClient _serviceProxyWithErrorHandler:]
- -[SpeechModelTrainingClient buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:]
- -[SpeechModelTrainingClient dealloc]
- -[SpeechModelTrainingClient generateAudioWithTexts:language:completion:]
- -[SpeechModelTrainingClient generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedNbest:recognizedText:correctedText:selectedAlternatives:completion:]
- -[SpeechModelTrainingClient generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedTokens:recognizedText:correctedText:selectedAlternatives:completion:]
- -[SpeechModelTrainingClient initWithServiceName:]
- -[SpeechModelTrainingClient init]
- -[SpeechModelTrainingClient invalidate]
- -[SpeechModelTrainingClient trainGlobalNNLMwithFidesSessionURL:completion:]
- -[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:asset:directory:completion:]
- -[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:asset:fides:activity:completion:]
- -[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:fides:activity:completion:]
- -[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:directory:completion:]
- -[SpeechModelTrainingClient upperCaseString:completion:]
- -[SpeechModelTrainingClient xpcExitClean]
- GCC_except_table1239
- GCC_except_table1253
- GCC_except_table1460
- GCC_except_table1534
- GCC_except_table1586
- GCC_except_table1610
- GCC_except_table1614
- GCC_except_table1630
- GCC_except_table1633
- GCC_except_table1659
- GCC_except_table1666
- GCC_except_table1675
- GCC_except_table1774
- GCC_except_table178
- GCC_except_table1784
- GCC_except_table1844
- GCC_except_table1870
- GCC_except_table1876
- GCC_except_table1957
- GCC_except_table1979
- GCC_except_table208
- GCC_except_table2083
- GCC_except_table2220
- GCC_except_table2223
- GCC_except_table2226
- GCC_except_table2231
- GCC_except_table2243
- GCC_except_table2248
- GCC_except_table2251
- GCC_except_table2254
- GCC_except_table2257
- GCC_except_table2350
- GCC_except_table2395
- GCC_except_table2400
- GCC_except_table2407
- GCC_except_table2425
- GCC_except_table2455
- GCC_except_table2560
- GCC_except_table259
- GCC_except_table2619
- GCC_except_table2631
- GCC_except_table2662
- GCC_except_table2687
- GCC_except_table2698
- GCC_except_table270
- GCC_except_table2732
- GCC_except_table2733
- GCC_except_table2734
- GCC_except_table2735
- GCC_except_table2736
- GCC_except_table2740
- GCC_except_table2747
- GCC_except_table2751
- GCC_except_table2766
- GCC_except_table2768
- GCC_except_table2769
- GCC_except_table2797
- GCC_except_table284
- GCC_except_table287
- GCC_except_table3065
- GCC_except_table3139
- GCC_except_table3176
- GCC_except_table3203
- GCC_except_table3206
- GCC_except_table3209
- GCC_except_table3240
- GCC_except_table3300
- GCC_except_table3494
- GCC_except_table3520
- GCC_except_table3548
- GCC_except_table3583
- GCC_except_table3584
- GCC_except_table3586
- GCC_except_table3604
- GCC_except_table3606
- GCC_except_table3608
- GCC_except_table3610
- GCC_except_table3612
- GCC_except_table3616
- GCC_except_table3619
- GCC_except_table3630
- GCC_except_table3639
- GCC_except_table3648
- GCC_except_table3654
- GCC_except_table3657
- GCC_except_table3659
- GCC_except_table3660
- GCC_except_table3662
- GCC_except_table3663
- GCC_except_table3664
- GCC_except_table3665
- GCC_except_table3676
- GCC_except_table3681
- GCC_except_table3682
- GCC_except_table3683
- GCC_except_table3684
- GCC_except_table3796
- GCC_except_table3820
- GCC_except_table3886
- GCC_except_table3902
- GCC_except_table3923
- GCC_except_table393
- GCC_except_table4015
- GCC_except_table4268
- GCC_except_table4325
- GCC_except_table4326
- GCC_except_table4330
- GCC_except_table4333
- GCC_except_table4337
- GCC_except_table4362
- GCC_except_table4415
- GCC_except_table4421
- GCC_except_table4777
- GCC_except_table4937
- GCC_except_table4947
- GCC_except_table4971
- GCC_except_table4991
- GCC_except_table5075
- GCC_except_table5107
- GCC_except_table5113
- GCC_except_table5115
- GCC_except_table5118
- GCC_except_table5126
- GCC_except_table5130
- GCC_except_table5136
- GCC_except_table5138
- GCC_except_table5156
- GCC_except_table5170
- GCC_except_table5172
- GCC_except_table5174
- GCC_except_table5185
- GCC_except_table5186
- GCC_except_table5189
- GCC_except_table5191
- GCC_except_table5192
- GCC_except_table5193
- GCC_except_table5197
- GCC_except_table5212
- GCC_except_table5243
- GCC_except_table5352
- GCC_except_table5382
- GCC_except_table5385
- GCC_except_table5475
- GCC_except_table5489
- GCC_except_table5496
- GCC_except_table5518
- GCC_except_table5522
- GCC_except_table5532
- GCC_except_table5776
- GCC_except_table5782
- GCC_except_table5815
- GCC_except_table5820
- GCC_except_table5857
- GCC_except_table5866
- GCC_except_table5896
- GCC_except_table595
- GCC_except_table5976
- GCC_except_table6198
- GCC_except_table6206
- GCC_except_table6226
- GCC_except_table6231
- GCC_except_table6340
- GCC_except_table6410
- GCC_except_table6432
- GCC_except_table6433
- GCC_except_table6443
- GCC_except_table6444
- GCC_except_table6456
- GCC_except_table6487
- GCC_except_table6498
- GCC_except_table6503
- GCC_except_table6508
- GCC_except_table653
- GCC_except_table6540
- GCC_except_table6622
- GCC_except_table6648
- GCC_except_table6662
- GCC_except_table6685
- GCC_except_table6697
- GCC_except_table6740
- GCC_except_table6884
- GCC_except_table6920
- GCC_except_table6971
- GCC_except_table7026
- GCC_except_table7049
- GCC_except_table7090
- GCC_except_table7100
- GCC_except_table7110
- GCC_except_table7151
- GCC_except_table7158
- GCC_except_table718
- GCC_except_table7180
- GCC_except_table722
- GCC_except_table7229
- GCC_except_table726
- GCC_except_table7320
- GCC_except_table7321
- GCC_except_table7322
- GCC_except_table7323
- GCC_except_table7324
- GCC_except_table7329
- GCC_except_table733
- GCC_except_table7393
- GCC_except_table7441
- GCC_except_table7447
- GCC_except_table7450
- GCC_except_table7458
- GCC_except_table7464
- GCC_except_table7489
- GCC_except_table7495
- GCC_except_table7501
- GCC_except_table7633
- GCC_except_table901
- GCC_except_table919
- GCC_except_table924
- OBJC_IVAR_$_SpeechModelTrainingClient._smtConnection
- _NSSearchPathForDirectoriesInDomains
- _OBJC_CLASS_$_SpeechModelTrainingClient
- _OBJC_METACLASS_$_SpeechModelTrainingClient
- _SpeechModelTrainingGetInterface
- __101-[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:fides:activity:completion:]_block_invoke
- __102-[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:asset:directory:completion:]_block_invoke
- __33-[SpeechModelTrainingClient init]_block_invoke
- __52-[CSVoiceTriggerAssetHandlerMac triggerAssetRefresh]_block_invoke
- __56-[SpeechModelTrainingClient upperCaseString:completion:]_block_invoke
- __OBJC_$_CLASS_METHODS_SpeechModelTrainingClient
- __OBJC_$_INSTANCE_METHODS_SpeechModelTrainingClient
- __OBJC_$_INSTANCE_VARIABLES_SpeechModelTrainingClient
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SpeechModelTrainingProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SpeechModelTrainingProtocol
- __OBJC_CLASS_RO_$_SpeechModelTrainingClient
- __OBJC_LABEL_PROTOCOL_$_SpeechModelTrainingProtocol
- __OBJC_METACLASS_RO_$_SpeechModelTrainingClient
- __OBJC_PROTOCOL_$_SpeechModelTrainingProtocol
- __OBJC_PROTOCOL_REFERENCE_$_SpeechModelTrainingProtocol
- ___101-[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:fides:activity:completion:]_block_invoke
- ___101-[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:fides:activity:completion:]_block_invoke_2
- ___102-[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:asset:directory:completion:]_block_invoke
- ___175-[SpeechModelTrainingClient generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedNbest:recognizedText:correctedText:selectedAlternatives:completion:]_block_invoke
- ___176-[SpeechModelTrainingClient generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedTokens:recognizedText:correctedText:selectedAlternatives:completion:]_block_invoke
- ___33-[SpeechModelTrainingClient init]_block_invoke
- ___41-[SpeechModelTrainingClient xpcExitClean]_block_invoke
- ___45-[CSXPCClient sendMessageAndReplySync:error:]_block_invoke
- ___56-[SpeechModelTrainingClient upperCaseString:completion:]_block_invoke
- ___58-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequired]_block_invoke
- ___72-[SpeechModelTrainingClient generateAudioWithTexts:language:completion:]_block_invoke
- ___75-[SpeechModelTrainingClient trainGlobalNNLMwithFidesSessionURL:completion:]_block_invoke
- ___92-[SpeechModelTrainingClient buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:]_block_invoke
- ___92-[SpeechModelTrainingClient buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16l
- ___block_descriptor_58_e8_32s40r_e20_v20?0B8"NSError"12l
- ___block_descriptor_67_e8_32s40s48r_e5_v8?0l
- _objc_msgSend$_isHearstRoutedAndWithNoPhoneCall
- _objc_msgSend$_serviceProxyWithErrorHandler:
- _objc_msgSend$buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:
- _objc_msgSend$clearLogFilesInDirectory:matchingPattern:exceedNumber:
- _objc_msgSend$defaultOptionWithTimeout:
- _objc_msgSend$didWin
- _objc_msgSend$dispatchStateChangedFrom:to:
- _objc_msgSend$generateAudioWithTexts:language:completion:
- _objc_msgSend$generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedNbest:recognizedText:correctedText:selectedAlternatives:completion:
- _objc_msgSend$generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedTokens:recognizedText:correctedText:selectedAlternatives:completion:
- _objc_msgSend$isMonitoring
- _objc_msgSend$isSiriDSPTurnedOn
- _objc_msgSend$notifyRequestCompletion
- _objc_msgSend$stringByStandardizingPath
- _objc_msgSend$trainGlobalNNLMwithFidesSessionURL:completion:
- _objc_msgSend$trainPersonalizedLMWithLanguage:configuration:asset:directory:completion:
- _objc_msgSend$trainPersonalizedLMWithLanguage:configuration:asset:fides:activity:completion:
- _objc_msgSend$trainPersonalizedLMWithLanguage:configuration:fides:activity:completion:
- _objc_msgSend$trainPersonalizedLMWithLanguage:configuration:fides:write:completion:
- _objc_msgSend$upperCaseString:withReply:
- _objc_msgSend$xpcExitClean
- _sLog
CStrings:
+ "%s Audio session activated for record, audioDeviceInfo = %{public}@"
+ "%s Audio session was already activated for record, skipping activation in startRecording"
+ "%s Audio stream failed to start after reporting didStartRecording early, will report didStop : %{public}@"
+ "%s Audio stream started, didStartRecording was already reported early"
+ "%s BTLE Myriad loss; not playing speech stop alert"
+ "%s BTLE recorder is gone; not playing speech stop alert"
+ "%s BTLE request was cancelled; not playing speech stop alert"
+ "%s BTLE speech controller began waiting for Myriad decision (identity %@)"
+ "%s Client %{public}p connection disconnected, notifying xpc listener"
+ "%s Failed to get audio stream handle ID : %{public}@"
+ "%s Invalidating cached record session activation state"
+ "%s Odeon VT with “Sound When Using Siri” disabled, suppressing twoshot alert play"
+ "%s Report unexpectedly long launch latency %{public}.3f"
+ "%s Report unexpectedly long launch latency %{public}.3f AudioTimeConverter: %@"
+ "%s Reporting didStartRecording early, ahead of the audio stream start"
+ "%s Sending client speechControllerDidStartRecording successfully? %{public}@"
+ "%s Sending client speechControllerDidStartRecording successfully? %{public}@, audioDeviceInfo = %{public}@"
+ "%s Speech Controller to use default channel for OdeonProxy VT: %{public}tu"
+ "%s VoiceTrigger cannot be turned on since Hearst is routed and owned with A2DP"
+ "%s VoiceTrigger cannot be turned on since Siri locale is not FarField VT supported"
+ "%s VoiceTrigger cannot be turned on since other non-eligible App is recording and we are not in a connected or outgoing call"
+ "%s VoiceTrigger cannot be turned on since voiceTriggerInCoreSpeech is NO"
+ "%s fromState:%llu, toState:%llu, hostTime:%llu"
+ "%s isSiriMode=%d, speechEvent=%ld, wasRequestCancelled=%d, shouldSuppressAlert=%d, recordRoute=%@"
+ "%s reporting request completion with %s:%llu"
+ "%s stop alert: didWin=%d, withError=%d, recordRoute=%@"
+ "%s tts Finished:%u isRequestCompleted:%u ttsEndHostTime:%llu currentHostTime:%llu"
+ "-[CSAttSiriAudioSessionStateClient dispatchStateChangedFrom:to:hostTime:]"
+ "-[CSSiriSpeechRecorder _playStopAlertWithError:]"
+ "-[CSSiriSpeechRecorder _waitForElectionThenPlayStopAlertWithError:recordRoute:]_block_invoke"
+ "-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequiredForElection:]_block_invoke"
+ "-[CSSpeechController _invalidateRecordSessionActivationState]"
+ "-[CSSpeechController _noteAudioSessionActivatedForRecord:]_block_invoke"
+ "-[CSSpeechController _notifyDelegateDidStartRecordingSuccessfully:error:]"
+ "-[CSVoiceTriggerAssetHandlerMac _handleTriggerAssetRefresh]_block_invoke"
+ "-[CSVoiceTriggerEnabledPolicyATVExclave _addVoiceTriggerEnabledConditions]_block_invoke"
+ "CSVoiceTriggerAssetHandlerMac.m"
+ "Nil asset"
+ "Recording stop alert"
+ "requestAudioDeviceInfo"
+ "ttsEndHostTime"
+ "v20@?0B8@\"SCDAElectionOutcome\"12"
+ "\xa5"
+ "\xf03"
- "%@"
- "%@ Interrupted"
- "%@ Invalidated"
- "%s BTLE Myriad Not explicitly playing speech stop alert"
- "%s BTLE speech controller began waiting for Myriad decision"
- "%s Client %{public}p connection disconnected, noticing xpc listener"
- "%s Disable FF since this is Exclave hardware without Siri DSP"
- "%s Failed to get audio stream handle ID : %{publid}@"
- "%s Report unexpectedly long launch latency %{publlic}.3f"
- "%s Report unexpectedly long launch latency %{publlic}.3f AudioTimeConverter: %@"
- "%s Sending client speechControllerDidStartRecording successfully? %{pubic}@"
- "%s Sending client speechControllerDidStartRecording successfully? %{pubic}@, audioDeviceInfo = %{public}@"
- "%s fromState:%llu, toState:%llu"
- "%s isSiriMode=%d, speechEvent=%ld, wasRequestCancelled=%d, shouldSuppressAlert=%d, isMonitoringMyriadEvents=%d, didMyriadWin=%d, recordRoute=%@"
- "%s tts Finished:%u isRequestCompleted:%u"
- "-[CSAttSiriAudioSessionStateClient dispatchStateChangedFrom:to:]"
- "-[CSEndpointAnalyzerBase getHybridEndpointerConfigForAsset:]"
- "-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequired]"
- "-[CSSiriSpeechRecorder suppressUtteranceGradingIfRequired]_block_invoke"
- "Assistant/SpeechPersonalizedLM"
- "Assistant/SpeechPersonalizedLM_Fides"
- "Client is 24-hour job"
- "Client is DictationPersonalizationFidesPlugin"
- "Client is PersonalizedLmFidesPlugin"
- "Dealloc-ing"
- "Input directory path(%@) does not match expected path"
- "Invalidating"
- "Received Error %@"
- "Received an error while accessing %@ service: %@"
- "SpeechModelTrainingClient"
- "com.apple.corespeech.speechmodeltraining.xpc"
- "com.apple.siri.speechmodeltraining"
- "com.apple.speech.speechmodeltraining"
- "personalizedLMPath=%@ fidesPersonalizedLMPath=%@"
- "\xa3"
- "\xf0#"
```
