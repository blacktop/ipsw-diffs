## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3600.70.47.11.1
-  __TEXT.__text: 0x148c54
+3605.23.1.0.0
+  __TEXT.__text: 0x146630
   __TEXT.__lazy_helpers: 0x54
-  __TEXT.__objc_methlist: 0x1508c
+  __TEXT.__objc_methlist: 0x14eb4
   __TEXT.__const: 0x42c
   __TEXT.__dlopen_cstrs: 0x1e0
-  __TEXT.__gcc_except_tab: 0x3230
-  __TEXT.__cstring: 0x28ec2
-  __TEXT.__oslogstring: 0x20308
-  __TEXT.__unwind_info: 0x6320
+  __TEXT.__gcc_except_tab: 0x3270
+  __TEXT.__cstring: 0x28db4
+  __TEXT.__oslogstring: 0x2022c
+  __TEXT.__unwind_info: 0x6260
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4258
-  __DATA_CONST.__objc_classlist: 0x868
+  __DATA_CONST.__const: 0x4230
+  __DATA_CONST.__objc_classlist: 0x860
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x4e8
+  __DATA_CONST.__objc_protolist: 0x4e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xaea8
-  __DATA_CONST.__objc_protorefs: 0xa0
-  __DATA_CONST.__objc_superrefs: 0x6a0
-  __DATA_CONST.__objc_arraydata: 0x3e8
-  __DATA_CONST.__got: 0x1b40
-  __AUTH_CONST.__const: 0x1f60
-  __AUTH_CONST.__cfstring: 0x96c0
-  __AUTH_CONST.__objc_const: 0x21458
+  __DATA_CONST.__objc_selrefs: 0xae18
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_superrefs: 0x698
+  __DATA_CONST.__objc_arraydata: 0x3f0
+  __DATA_CONST.__got: 0x1b38
+  __AUTH_CONST.__const: 0x1e20
+  __AUTH_CONST.__cfstring: 0x9620
+  __AUTH_CONST.__objc_const: 0x21380
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__lazy_load_got: 0x8
   __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_floatobj: 0x4f0
-  __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH_CONST.__auth_got: 0xda8
+  __AUTH_CONST.__objc_arrayobj: 0x120
+  __AUTH_CONST.__auth_got: 0xda0
   __AUTH.__objc_data: 0x3ca0
-  __DATA.__objc_ivar: 0x1998
-  __DATA.__data: 0x3a74
+  __DATA.__objc_ivar: 0x199c
+  __DATA.__data: 0x3a14
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1770
+  __DATA_DIRTY.__objc_data: 0x1720
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__bss: 0x150
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8197
-  Symbols:   17978
-  CStrings:  5613
+  Functions: 8147
+  Symbols:   17897
+  CStrings:  5597
 
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
+ GCC_except_table3583
+ GCC_except_table3609
+ GCC_except_table3637
+ GCC_except_table3671
+ GCC_except_table3672
+ GCC_except_table3674
+ GCC_except_table3676
+ GCC_except_table3692
+ GCC_except_table3694
+ GCC_except_table3698
+ GCC_except_table3700
+ GCC_except_table3702
+ GCC_except_table3704
+ GCC_except_table3707
+ GCC_except_table3715
+ GCC_except_table3718
+ GCC_except_table3724
+ GCC_except_table3726
+ GCC_except_table3728
+ GCC_except_table3732
+ GCC_except_table3734
+ GCC_except_table3736
+ GCC_except_table3737
+ GCC_except_table3739
+ GCC_except_table3740
+ GCC_except_table3741
+ GCC_except_table3744
+ GCC_except_table3745
+ GCC_except_table3746
+ GCC_except_table3747
+ GCC_except_table3748
+ GCC_except_table3749
+ GCC_except_table3750
+ GCC_except_table3752
+ GCC_except_table3767
+ GCC_except_table3768
+ GCC_except_table3769
+ GCC_except_table3910
+ GCC_except_table3934
+ GCC_except_table4000
+ GCC_except_table4016
+ GCC_except_table4037
+ GCC_except_table4129
+ GCC_except_table4381
+ GCC_except_table4452
+ GCC_except_table4453
+ GCC_except_table4457
+ GCC_except_table4460
+ GCC_except_table4464
+ GCC_except_table4489
+ GCC_except_table4492
+ GCC_except_table4545
+ GCC_except_table4551
+ GCC_except_table4621
+ GCC_except_table4825
+ GCC_except_table4832
+ GCC_except_table4839
+ GCC_except_table4845
+ GCC_except_table4928
+ GCC_except_table5088
+ GCC_except_table5098
+ GCC_except_table5122
+ GCC_except_table5142
+ GCC_except_table5225
+ GCC_except_table5239
+ GCC_except_table5248
+ GCC_except_table5255
+ GCC_except_table5261
+ GCC_except_table5263
+ GCC_except_table5266
+ GCC_except_table5274
+ GCC_except_table5276
+ GCC_except_table5280
+ GCC_except_table5282
+ GCC_except_table5293
+ GCC_except_table5294
+ GCC_except_table5299
+ GCC_except_table5306
+ GCC_except_table5313
+ GCC_except_table5315
+ GCC_except_table5318
+ GCC_except_table5320
+ GCC_except_table5323
+ GCC_except_table5324
+ GCC_except_table5325
+ GCC_except_table5326
+ GCC_except_table5328
+ GCC_except_table5329
+ GCC_except_table5347
+ GCC_except_table5435
+ GCC_except_table5439
+ GCC_except_table5493
+ GCC_except_table5523
+ GCC_except_table5526
+ GCC_except_table5616
+ GCC_except_table5630
+ GCC_except_table5637
+ GCC_except_table5649
+ GCC_except_table5653
+ GCC_except_table5663
+ GCC_except_table5892
+ GCC_except_table5925
+ GCC_except_table5930
+ GCC_except_table5967
+ GCC_except_table5976
+ GCC_except_table6006
+ GCC_except_table6076
+ GCC_except_table6218
+ GCC_except_table6323
+ GCC_except_table6331
+ GCC_except_table6351
+ GCC_except_table6356
+ GCC_except_table6462
+ GCC_except_table6517
+ GCC_except_table6597
+ GCC_except_table6619
+ GCC_except_table6620
+ GCC_except_table6630
+ GCC_except_table6631
+ GCC_except_table6643
+ GCC_except_table6674
+ GCC_except_table6685
+ GCC_except_table6690
+ GCC_except_table6723
+ GCC_except_table6795
+ GCC_except_table6807
+ GCC_except_table6830
+ GCC_except_table6841
+ GCC_except_table6844
+ GCC_except_table6867
+ GCC_except_table6879
+ GCC_except_table6926
+ GCC_except_table7176
+ GCC_except_table7212
+ GCC_except_table7285
+ GCC_except_table7339
+ GCC_except_table7362
+ GCC_except_table7403
+ GCC_except_table7414
+ GCC_except_table7558
+ GCC_except_table7566
+ GCC_except_table7682
+ GCC_except_table7683
+ GCC_except_table7684
+ GCC_except_table7685
+ GCC_except_table7686
+ GCC_except_table7691
+ GCC_except_table7754
+ GCC_except_table7800
+ GCC_except_table7808
+ GCC_except_table7814
+ GCC_except_table7839
+ GCC_except_table7845
+ GCC_except_table7851
+ GCC_except_table7989
+ _OBJC_IVAR_$_CSAttSiriAudioSessionStateClient._ttsEndHostTime
+ _OBJC_IVAR_$_CSVoiceIdXPCConnection._delegate
+ ___59-[CSVoiceTriggerAssetHandlerMac _handleTriggerAssetRefresh]_block_invoke
+ ___69-[CSAttSiriMitigationAssetProvider getMitigationAssetWithCompletion:]_block_invoke
+ ___block_descriptor_64_e8_32s40s48r56w_e29_v24?0"CSAsset"8"NSError"16lw56l8s32l8s40l8r48l8
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
- -[SpeechModelTrainingClient buildSpeechProfileForLanguage:]
- -[SpeechModelTrainingClient dealloc]
- -[SpeechModelTrainingClient extractBundledOovs:appLmDataFileSandboxExtension:appBundleId:completion:]
- -[SpeechModelTrainingClient generateAudioWithTexts:language:completion:]
- -[SpeechModelTrainingClient generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedNbest:recognizedText:correctedText:selectedAlternatives:completion:]
- -[SpeechModelTrainingClient generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedTokens:recognizedText:correctedText:selectedAlternatives:completion:]
- -[SpeechModelTrainingClient initWithServiceName:]
- -[SpeechModelTrainingClient init]
- -[SpeechModelTrainingClient invalidate]
- -[SpeechModelTrainingClient trainAllAppLMWithLanguage:]
- -[SpeechModelTrainingClient trainAllAppLMWithLanguage:completion:]
- -[SpeechModelTrainingClient trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmDataFileSandboxExtension:]
- -[SpeechModelTrainingClient trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmDataFileSandboxExtension:completion:]
- -[SpeechModelTrainingClient trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmModelFile:appLmDataFileSandboxExtension:]
- -[SpeechModelTrainingClient trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmModelFile:appLmDataFileSandboxExtension:completion:]
- -[SpeechModelTrainingClient trainGlobalNNLMwithFidesSessionURL:completion:]
- -[SpeechModelTrainingClient trainPartialAllAppLMWithLanguage:]
- -[SpeechModelTrainingClient trainPartialAllAppLMWithLanguage:completion:]
- -[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:asset:directory:completion:]
- -[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:asset:fides:activity:completion:]
- -[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:fides:activity:completion:]
- -[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:directory:completion:]
- -[SpeechModelTrainingClient upperCaseString:completion:]
- -[SpeechModelTrainingClient wakeUpWithCompletion:]
- -[SpeechModelTrainingClient xpcExitClean]
- GCC_except_table3642
- GCC_except_table3668
- GCC_except_table3731
- GCC_except_table3733
- GCC_except_table3751
- GCC_except_table3755
- GCC_except_table3757
- GCC_except_table3759
- GCC_except_table3763
- GCC_except_table3774
- GCC_except_table3777
- GCC_except_table3783
- GCC_except_table3785
- GCC_except_table3787
- GCC_except_table3789
- GCC_except_table3791
- GCC_except_table3793
- GCC_except_table3794
- GCC_except_table3795
- GCC_except_table3796
- GCC_except_table3798
- GCC_except_table3799
- GCC_except_table3800
- GCC_except_table3803
- GCC_except_table3804
- GCC_except_table3805
- GCC_except_table3806
- GCC_except_table3807
- GCC_except_table3808
- GCC_except_table3809
- GCC_except_table3811
- GCC_except_table3812
- GCC_except_table3820
- GCC_except_table3825
- GCC_except_table3826
- GCC_except_table3827
- GCC_except_table3828
- GCC_except_table3969
- GCC_except_table3993
- GCC_except_table4059
- GCC_except_table4075
- GCC_except_table4096
- GCC_except_table4188
- GCC_except_table4440
- GCC_except_table4511
- GCC_except_table4512
- GCC_except_table4516
- GCC_except_table4519
- GCC_except_table4523
- GCC_except_table4548
- GCC_except_table4601
- GCC_except_table4607
- GCC_except_table4677
- GCC_except_table4881
- GCC_except_table4888
- GCC_except_table4895
- GCC_except_table4901
- GCC_except_table4984
- GCC_except_table5144
- GCC_except_table5154
- GCC_except_table5178
- GCC_except_table5198
- GCC_except_table5281
- GCC_except_table5295
- GCC_except_table5304
- GCC_except_table5336
- GCC_except_table5338
- GCC_except_table5349
- GCC_except_table5350
- GCC_except_table5355
- GCC_except_table5362
- GCC_except_table5367
- GCC_except_table5369
- GCC_except_table5371
- GCC_except_table5373
- GCC_except_table5374
- GCC_except_table5375
- GCC_except_table5376
- GCC_except_table5379
- GCC_except_table5380
- GCC_except_table5381
- GCC_except_table5382
- GCC_except_table5384
- GCC_except_table5385
- GCC_except_table5386
- GCC_except_table5388
- GCC_except_table5403
- GCC_except_table5434
- GCC_except_table5491
- GCC_except_table5495
- GCC_except_table5549
- GCC_except_table5579
- GCC_except_table5582
- GCC_except_table5672
- GCC_except_table5686
- GCC_except_table5693
- GCC_except_table5705
- GCC_except_table5709
- GCC_except_table5719
- GCC_except_table5948
- GCC_except_table5981
- GCC_except_table5986
- GCC_except_table6023
- GCC_except_table6032
- GCC_except_table6062
- GCC_except_table6130
- GCC_except_table6272
- GCC_except_table6375
- GCC_except_table6383
- GCC_except_table6403
- GCC_except_table6408
- GCC_except_table6514
- GCC_except_table6569
- GCC_except_table6649
- GCC_except_table6671
- GCC_except_table6672
- GCC_except_table6682
- GCC_except_table6683
- GCC_except_table6726
- GCC_except_table6737
- GCC_except_table6742
- GCC_except_table6747
- GCC_except_table6775
- GCC_except_table6847
- GCC_except_table6859
- GCC_except_table6882
- GCC_except_table6893
- GCC_except_table6896
- GCC_except_table6919
- GCC_except_table6931
- GCC_except_table6978
- GCC_except_table7226
- GCC_except_table7262
- GCC_except_table7335
- GCC_except_table7389
- GCC_except_table7412
- GCC_except_table7453
- GCC_except_table7464
- GCC_except_table7608
- GCC_except_table7616
- GCC_except_table7732
- GCC_except_table7733
- GCC_except_table7734
- GCC_except_table7735
- GCC_except_table7736
- GCC_except_table7741
- GCC_except_table7804
- GCC_except_table7850
- GCC_except_table7858
- GCC_except_table7864
- GCC_except_table7889
- GCC_except_table7895
- GCC_except_table7901
- GCC_except_table8039
- _NSSearchPathForDirectoriesInDomains
- _OBJC_CLASS_$_SpeechModelTrainingClient
- _OBJC_IVAR_$_SpeechModelTrainingClient._smtConnection
- _OBJC_METACLASS_$_SpeechModelTrainingClient
- _SpeechModelTrainingGetInterface
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
- ___101-[SpeechModelTrainingClient extractBundledOovs:appLmDataFileSandboxExtension:appBundleId:completion:]_block_invoke
- ___101-[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:fides:activity:completion:]_block_invoke
- ___101-[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:fides:activity:completion:]_block_invoke_2
- ___102-[SpeechModelTrainingClient trainPersonalizedLMWithLanguage:configuration:asset:directory:completion:]_block_invoke
- ___122-[SpeechModelTrainingClient trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmDataFileSandboxExtension:]_block_invoke
- ___133-[SpeechModelTrainingClient trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmDataFileSandboxExtension:completion:]_block_invoke
- ___137-[SpeechModelTrainingClient trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmModelFile:appLmDataFileSandboxExtension:]_block_invoke
- ___148-[SpeechModelTrainingClient trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmModelFile:appLmDataFileSandboxExtension:completion:]_block_invoke
- ___175-[SpeechModelTrainingClient generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedNbest:recognizedText:correctedText:selectedAlternatives:completion:]_block_invoke
- ___176-[SpeechModelTrainingClient generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedTokens:recognizedText:correctedText:selectedAlternatives:completion:]_block_invoke
- ___33-[SpeechModelTrainingClient init]_block_invoke
- ___41-[SpeechModelTrainingClient xpcExitClean]_block_invoke
- ___50-[SpeechModelTrainingClient wakeUpWithCompletion:]_block_invoke
- ___55-[SpeechModelTrainingClient trainAllAppLMWithLanguage:]_block_invoke
- ___56-[SpeechModelTrainingClient upperCaseString:completion:]_block_invoke
- ___56-[SpeechModelTrainingClient upperCaseString:completion:]_block_invoke_2
- ___56-[SpeechModelTrainingClient upperCaseString:completion:]_block_invoke_3
- ___59-[SpeechModelTrainingClient buildSpeechProfileForLanguage:]_block_invoke
- ___62-[SpeechModelTrainingClient trainPartialAllAppLMWithLanguage:]_block_invoke
- ___66-[SpeechModelTrainingClient trainAllAppLMWithLanguage:completion:]_block_invoke
- ___72-[SpeechModelTrainingClient generateAudioWithTexts:language:completion:]_block_invoke
- ___73-[SpeechModelTrainingClient trainPartialAllAppLMWithLanguage:completion:]_block_invoke
- ___75-[SpeechModelTrainingClient trainGlobalNNLMwithFidesSessionURL:completion:]_block_invoke
- ___92-[SpeechModelTrainingClient buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:]_block_invoke
- ___92-[SpeechModelTrainingClient buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e30_v24?0"NSString"8"NSError"16ls32l8
- ___block_descriptor_40_e8_32bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8
- _objc_msgSend$_isHearstRoutedAndWithNoPhoneCall
- _objc_msgSend$_serviceProxyWithErrorHandler:
- _objc_msgSend$_tearDownBuiltInVoiceTrigger
- _objc_msgSend$buildPhoneticMatchWithLanguage:saveIntermediateFsts:completion:
- _objc_msgSend$buildSpeechProfileForLanguage:
- _objc_msgSend$clearLogFilesInDirectory:matchingPattern:exceedNumber:
- _objc_msgSend$dispatchStateChangedFrom:to:
- _objc_msgSend$extractBundledOovs:appLmDataFileSandboxExtension:appBundleId:completion:
- _objc_msgSend$generateAudioWithTexts:language:completion:
- _objc_msgSend$generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedNbest:recognizedText:correctedText:selectedAlternatives:completion:
- _objc_msgSend$generateConfusionPairsWithUUID:parameters:language:task:samplingRate:recognizedTokens:recognizedText:correctedText:selectedAlternatives:completion:
- _objc_msgSend$isSiriDSPTurnedOn
- _objc_msgSend$notifyRequestCompletion
- _objc_msgSend$sharedAVSystemController
- _objc_msgSend$stringByStandardizingPath
- _objc_msgSend$trainAllAppLMWithLanguage:
- _objc_msgSend$trainAllAppLMWithLanguage:completion:
- _objc_msgSend$trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmDataFileSandboxExtension:
- _objc_msgSend$trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmDataFileSandboxExtension:completion:
- _objc_msgSend$trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmModelFile:appLmDataFileSandboxExtension:
- _objc_msgSend$trainAppLMWithLanguage:configuration:appBundleId:appLmDataFile:appLmModelFile:appLmDataFileSandboxExtension:completion:
- _objc_msgSend$trainGlobalNNLMwithFidesSessionURL:completion:
- _objc_msgSend$trainPartialAllAppLMWithLanguage:
- _objc_msgSend$trainPartialAllAppLMWithLanguage:completion:
- _objc_msgSend$trainPersonalizedLMWithLanguage:configuration:asset:directory:completion:
- _objc_msgSend$trainPersonalizedLMWithLanguage:configuration:asset:fides:activity:completion:
- _objc_msgSend$trainPersonalizedLMWithLanguage:configuration:fides:activity:completion:
- _objc_msgSend$trainPersonalizedLMWithLanguage:configuration:fides:write:completion:
- _objc_msgSend$upperCaseString:withReply:
- _objc_msgSend$wakeUpWithCompletion:
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
- "buildSpeechProfile is unavailable when siri_vocabulary_speech_profile feature flag is enabled."
- "com.apple.corespeech.speechmodeltraining.xpc"
- "com.apple.siri.speechmodeltraining"
- "com.apple.speech.speechmodeltraining"
- "personalizedLMPath=%@ fidesPersonalizedLMPath=%@"
- "siri_vocabulary_speech_profile"
```
