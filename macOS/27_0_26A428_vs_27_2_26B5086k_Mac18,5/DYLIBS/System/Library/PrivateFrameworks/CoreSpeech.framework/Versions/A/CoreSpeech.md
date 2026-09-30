## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/Versions/A/CoreSpeech`

```diff

-3600.70.47.0.0
-  __TEXT.__text: 0x13af40
+3605.23.1.0.0
+  __TEXT.__text: 0x139958
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x14038
-  __TEXT.__const: 0x40c
+  __TEXT.__objc_methlist: 0x13f64
+  __TEXT.__const: 0x3fc
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__gcc_except_tab: 0x3194
-  __TEXT.__cstring: 0x2559f
-  __TEXT.__oslogstring: 0x1e169
-  __TEXT.__unwind_info: 0x5d08
+  __TEXT.__gcc_except_tab: 0x31d8
+  __TEXT.__cstring: 0x2550f
+  __TEXT.__oslogstring: 0x1e08d
+  __TEXT.__unwind_info: 0x5ca8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xd40
-  __DATA_CONST.__objc_classlist: 0x838
+  __DATA_CONST.__objc_classlist: 0x830
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x4b0
+  __DATA_CONST.__objc_protolist: 0x4a8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xa518
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x658
-  __DATA_CONST.__objc_arraydata: 0x3f0
-  __DATA_CONST.__got: 0x1890
-  __AUTH_CONST.__const: 0x5920
-  __AUTH_CONST.__cfstring: 0x9180
-  __AUTH_CONST.__objc_const: 0x1fb60
+  __DATA_CONST.__objc_selrefs: 0xa4e8
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x650
+  __DATA_CONST.__objc_arraydata: 0x3f8
+  __DATA_CONST.__got: 0x1888
+  __AUTH_CONST.__const: 0x5890
+  __AUTH_CONST.__cfstring: 0x9100
+  __AUTH_CONST.__objc_const: 0x1fae0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x3e8
   __AUTH_CONST.__objc_floatobj: 0x4d0
-  __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0xc18
+  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__auth_got: 0xc10
   __AUTH.__objc_data: 0x3b60
-  __DATA.__objc_ivar: 0x1828
-  __DATA.__data: 0x37d4
+  __DATA.__objc_ivar: 0x182c
+  __DATA.__data: 0x3774
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x16d0
+  __DATA_DIRTY.__objc_data: 0x1680
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x108
+  __DATA_DIRTY.__bss: 0xf8
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7797
-  Symbols:   17140
-  CStrings:  5173
+  Functions: 7771
+  Symbols:   17093
+  CStrings:  5159
 
Symbols:
+ -[CSAttSiriAudioSessionStateClient dispatchStateChangedFrom:to:hostTime:]
+ -[CSAttSiriAudioSessionStateClient setTtsEndHostTime:]
+ -[CSAttSiriAudioSessionStateClient ttsEndHostTime]
+ -[CSAttSiriMitigationAssetProvider getMitigationAssetWithCompletion:]
+ -[CSVoiceIdXPCConnection delegate]
+ -[CSVoiceIdXPCConnection setDelegate:]
+ -[CSVoiceTriggerAPModeSuspendPolicyIOS _isHearstRouted]
+ -[CSVoiceTriggerAPModeSuspendPolicyIOS _isPhoneCallActive]
+ -[CSVoiceTriggerAssetHandlerMac _handleTriggerAssetRefresh]
+ -[CSVoiceTriggerAssetHandlerMac compileAndUpdateDeviceCachesWithAsset:assetType:endpointId:]
+ GCC_except_table3457
+ GCC_except_table3483
+ GCC_except_table3511
+ GCC_except_table3546
+ GCC_except_table3547
+ GCC_except_table3549
+ GCC_except_table3551
+ GCC_except_table3567
+ GCC_except_table3569
+ GCC_except_table3571
+ GCC_except_table3573
+ GCC_except_table3575
+ GCC_except_table3577
+ GCC_except_table3579
+ GCC_except_table3582
+ GCC_except_table3590
+ GCC_except_table3593
+ GCC_except_table3600
+ GCC_except_table3602
+ GCC_except_table3611
+ GCC_except_table3613
+ GCC_except_table3615
+ GCC_except_table3617
+ GCC_except_table3620
+ GCC_except_table3622
+ GCC_except_table3623
+ GCC_except_table3624
+ GCC_except_table3625
+ GCC_except_table3626
+ GCC_except_table3628
+ GCC_except_table3631
+ GCC_except_table3644
+ GCC_except_table3646
+ GCC_except_table3759
+ GCC_except_table3783
+ GCC_except_table3849
+ GCC_except_table3865
+ GCC_except_table3978
+ GCC_except_table4231
+ GCC_except_table4288
+ GCC_except_table4289
+ GCC_except_table4293
+ GCC_except_table4296
+ GCC_except_table4300
+ GCC_except_table4328
+ GCC_except_table4383
+ GCC_except_table4389
+ GCC_except_table4745
+ GCC_except_table4905
+ GCC_except_table4915
+ GCC_except_table4939
+ GCC_except_table4959
+ GCC_except_table5043
+ GCC_except_table5057
+ GCC_except_table5066
+ GCC_except_table5081
+ GCC_except_table5083
+ GCC_except_table5086
+ GCC_except_table5094
+ GCC_except_table5104
+ GCC_except_table5106
+ GCC_except_table5124
+ GCC_except_table5131
+ GCC_except_table5140
+ GCC_except_table5142
+ GCC_except_table5143
+ GCC_except_table5144
+ GCC_except_table5145
+ GCC_except_table5148
+ GCC_except_table5152
+ GCC_except_table5153
+ GCC_except_table5154
+ GCC_except_table5157
+ GCC_except_table5159
+ GCC_except_table5160
+ GCC_except_table5161
+ GCC_except_table5165
+ GCC_except_table5211
+ GCC_except_table5320
+ GCC_except_table5350
+ GCC_except_table5353
+ GCC_except_table5443
+ GCC_except_table5457
+ GCC_except_table5464
+ GCC_except_table5486
+ GCC_except_table5490
+ GCC_except_table5500
+ GCC_except_table5744
+ GCC_except_table5750
+ GCC_except_table5783
+ GCC_except_table5788
+ GCC_except_table5825
+ GCC_except_table5834
+ GCC_except_table5864
+ GCC_except_table5946
+ GCC_except_table6170
+ GCC_except_table6178
+ GCC_except_table6203
+ GCC_except_table6312
+ GCC_except_table6382
+ GCC_except_table6404
+ GCC_except_table6405
+ GCC_except_table6415
+ GCC_except_table6416
+ GCC_except_table6428
+ GCC_except_table6459
+ GCC_except_table6470
+ GCC_except_table6475
+ GCC_except_table6480
+ GCC_except_table6512
+ GCC_except_table6594
+ GCC_except_table6620
+ GCC_except_table6631
+ GCC_except_table6634
+ GCC_except_table6657
+ GCC_except_table6669
+ GCC_except_table6712
+ GCC_except_table6858
+ GCC_except_table6894
+ GCC_except_table6945
+ GCC_except_table7000
+ GCC_except_table7023
+ GCC_except_table7064
+ GCC_except_table7074
+ GCC_except_table7084
+ GCC_except_table7125
+ GCC_except_table7132
+ GCC_except_table7154
+ GCC_except_table7203
+ GCC_except_table7294
+ GCC_except_table7295
+ GCC_except_table7296
+ GCC_except_table7297
+ GCC_except_table7298
+ GCC_except_table7303
+ GCC_except_table7367
+ GCC_except_table7415
+ GCC_except_table7421
+ GCC_except_table7424
+ GCC_except_table7432
+ GCC_except_table7438
+ GCC_except_table7463
+ GCC_except_table7469
+ GCC_except_table7475
+ GCC_except_table7607
+ OBJC_IVAR_$_CSAttSiriAudioSessionStateClient._ttsEndHostTime
+ OBJC_IVAR_$_CSVoiceIdXPCConnection._delegate
+ ___59-[CSVoiceTriggerAssetHandlerMac _handleTriggerAssetRefresh]_block_invoke
+ ___69-[CSAttSiriMitigationAssetProvider getMitigationAssetWithCompletion:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48r56w_e29_v24?0"CSAsset"8"NSError"16l
+ ___copy_helper_block_e8_32s40s48r56w
+ ___destroy_helper_block_e8_32s40s48r56w
+ _objc_msgSend$_handleTriggerAssetRefresh
+ _objc_msgSend$_isHearstRouted
+ _objc_msgSend$_isPhoneCallActive
+ _objc_msgSend$clearLogFilesInDirectory:matchingPatterns:exceedNumber:
+ _objc_msgSend$compileAndUpdateDeviceCachesWithAsset:assetType:endpointId:
+ _objc_msgSend$dispatchStateChangedFrom:to:hostTime:
+ _objc_msgSend$notifyRequestCompletionAtHostTime:
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
- GCC_except_table3494
- GCC_except_table3520
- GCC_except_table3548
- GCC_except_table3583
- GCC_except_table3584
- GCC_except_table3586
- GCC_except_table3588
- GCC_except_table3614
- GCC_except_table3619
- GCC_except_table3637
- GCC_except_table3641
- GCC_except_table3643
- GCC_except_table3648
- GCC_except_table3649
- GCC_except_table3650
- GCC_except_table3652
- GCC_except_table3653
- GCC_except_table3654
- GCC_except_table3657
- GCC_except_table3659
- GCC_except_table3660
- GCC_except_table3661
- GCC_except_table3662
- GCC_except_table3663
- GCC_except_table3664
- GCC_except_table3665
- GCC_except_table3667
- GCC_except_table3668
- GCC_except_table3676
- GCC_except_table3681
- GCC_except_table3682
- GCC_except_table3683
- GCC_except_table3684
- GCC_except_table3796
- GCC_except_table3820
- GCC_except_table3902
- GCC_except_table3923
- GCC_except_table4015
- GCC_except_table4268
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
- GCC_except_table5089
- GCC_except_table5107
- GCC_except_table5113
- GCC_except_table5115
- GCC_except_table5118
- GCC_except_table5126
- GCC_except_table5130
- GCC_except_table5156
- GCC_except_table5163
- GCC_except_table5168
- GCC_except_table5170
- GCC_except_table5172
- GCC_except_table5174
- GCC_except_table5175
- GCC_except_table5176
- GCC_except_table5177
- GCC_except_table5184
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
- GCC_except_table5976
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
- GCC_except_table6540
- GCC_except_table6622
- GCC_except_table6648
- GCC_except_table6659
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
- GCC_except_table7180
- GCC_except_table7229
- GCC_except_table7320
- GCC_except_table7321
- GCC_except_table7322
- GCC_except_table7323
- GCC_except_table7324
- GCC_except_table7329
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
- ___56-[SpeechModelTrainingClient upperCaseString:completion:]_block_invoke
- ___72-[SpeechModelTrainingClient generateAudioWithTexts:language:completion:]_block_invoke
- ___75-[SpeechModelTrainingClient trainGlobalNNLMwithFidesSessionURL:completion:]_block_invoke
- ___92-[SpeechModelTrainingClient buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:]_block_invoke
- ___92-[SpeechModelTrainingClient buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16l
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16l
- _objc_msgSend$_isHearstRoutedAndWithNoPhoneCall
- _objc_msgSend$_serviceProxyWithErrorHandler:
- _objc_msgSend$buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:
- _objc_msgSend$clearLogFilesInDirectory:matchingPattern:exceedNumber:
- _objc_msgSend$dispatchStateChangedFrom:to:
- _objc_msgSend$generateAudioWithTexts:language:completion:
- _objc_msgSend$generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedNbest:recognizedText:correctedText:selectedAlternatives:completion:
- _objc_msgSend$generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedTokens:recognizedText:correctedText:selectedAlternatives:completion:
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
+ "%s Client %{public}p connection disconnected, notifying xpc listener"
+ "%s Failed to get audio stream handle ID : %{public}@"
+ "%s Report unexpectedly long launch latency %{public}.3f"
+ "%s Report unexpectedly long launch latency %{public}.3f AudioTimeConverter: %@"
+ "%s Sending client speechControllerDidStartRecording successfully? %{public}@"
+ "%s Sending client speechControllerDidStartRecording successfully? %{public}@, audioDeviceInfo = %{public}@"
+ "%s fromState:%llu, toState:%llu, hostTime:%llu"
+ "%s reporting request completion with %s:%llu"
+ "%s tts Finished:%u isRequestCompleted:%u ttsEndHostTime:%llu currentHostTime:%llu"
+ "-[CSAttSiriAudioSessionStateClient dispatchStateChangedFrom:to:hostTime:]"
+ "-[CSVoiceTriggerAssetHandlerMac _handleTriggerAssetRefresh]_block_invoke"
+ "CSVoiceTriggerAssetHandlerMac.m"
+ "Nil asset"
+ "ttsEndHostTime"
- "%@"
- "%@ Interrupted"
- "%@ Invalidated"
- "%s Client %{public}p connection disconnected, noticing xpc listener"
- "%s Disable FF since this is Exclave hardware without Siri DSP"
- "%s Failed to get audio stream handle ID : %{publid}@"
- "%s Report unexpectedly long launch latency %{publlic}.3f"
- "%s Report unexpectedly long launch latency %{publlic}.3f AudioTimeConverter: %@"
- "%s Sending client speechControllerDidStartRecording successfully? %{pubic}@"
- "%s Sending client speechControllerDidStartRecording successfully? %{pubic}@, audioDeviceInfo = %{public}@"
- "%s fromState:%llu, toState:%llu"
- "%s tts Finished:%u isRequestCompleted:%u"
- "-[CSAttSiriAudioSessionStateClient dispatchStateChangedFrom:to:]"
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
```
