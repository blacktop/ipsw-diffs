## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3500.122.2.0.0
-  __TEXT.__text: 0x151dac
-  __TEXT.__auth_stubs: 0x1b30
-  __TEXT.__objc_methlist: 0x14394
+3505.14.3.0.0
+  __TEXT.__text: 0x152a94
+  __TEXT.__auth_stubs: 0x1b60
+  __TEXT.__objc_methlist: 0x143e4
   __TEXT.__const: 0x58c
   __TEXT.__dlopen_cstrs: 0x197
   __TEXT.__gcc_except_tab: 0x3cac
-  __TEXT.__cstring: 0x274a0
-  __TEXT.__oslogstring: 0x1edb7
-  __TEXT.__unwind_info: 0x4db8
+  __TEXT.__cstring: 0x275bd
+  __TEXT.__oslogstring: 0x1efaa
+  __TEXT.__unwind_info: 0x4dc8
   __TEXT.__objc_classname: 0x2e76
-  __TEXT.__objc_methname: 0x37a7c
-  __TEXT.__objc_methtype: 0x7a59
-  __TEXT.__objc_stubs: 0x1bf20
-  __DATA_CONST.__got: 0x1a98
+  __TEXT.__objc_methname: 0x37c42
+  __TEXT.__objc_methtype: 0x7a71
+  __TEXT.__objc_stubs: 0x1c020
+  __DATA_CONST.__got: 0x1ab0
   __DATA_CONST.__const: 0x40f8
   __DATA_CONST.__objc_classlist: 0x840
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa7f0
+  __DATA_CONST.__objc_selrefs: 0xa840
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x688
   __DATA_CONST.__objc_arraydata: 0x3e8
-  __AUTH_CONST.__auth_got: 0xdb0
+  __AUTH_CONST.__auth_got: 0xdc8
   __AUTH_CONST.__const: 0x1e00
-  __AUTH_CONST.__cfstring: 0x93a0
-  __AUTH_CONST.__objc_const: 0x20368
+  __AUTH_CONST.__cfstring: 0x9400
+  __AUTH_CONST.__objc_const: 0x203a0
   __AUTH_CONST.__objc_intobj: 0x990
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_floatobj: 0x4c0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH.__objc_data: 0x3e80
-  __DATA.__objc_ivar: 0x18f8
+  __DATA.__objc_ivar: 0x18fc
   __DATA.__data: 0x3650
-  __DATA.__bss: 0x668
+  __DATA.__bss: 0x670
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1400
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__bss: 0x150
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B07EBD11-A798-3F0C-BB83-6126D561DF5B
-  Functions: 7915
-  Symbols:   26014
-  CStrings:  15484
+  UUID: 9DDAFC6E-CE2B-39B9-8B02-922387A741CD
+  Functions: 7924
+  Symbols:   26047
+  CStrings:  15513
 
Symbols:
+ -[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:secureAsset:]
+ -[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]
+ -[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withSecureAsset:withLanguageCode:]
+ -[CSVoiceProfileRetrainManager triggerVoiceProfileRetrainingWithAsset:withSecureAsset:]
+ -[CSVoiceTriggerFileLogger _moveSecureAudioCaptureFrom:withExclaveTimestamp:]
+ -[CSVoiceTriggerFileLogger _syncAvailableSecureCaptures]
+ -[CSVoiceTriggerFileLogger isExclaveHardware]
+ -[CSVoiceTriggerFileLogger setIsExclaveHardware:]
+ -[CSVoiceTriggerSecondPass _getSecondPassRejectReasonFromExclaveKeywordResult:speakerDetectionResult:]
+ -[CSVoiceTriggerSecondPass getSecondPassRejectReasonFromExclaveKeywordResult:speakerDetectionResult:]
+ GCC_except_table1249
+ GCC_except_table1261
+ GCC_except_table1467
+ GCC_except_table1533
+ GCC_except_table1557
+ GCC_except_table1561
+ GCC_except_table1577
+ GCC_except_table1580
+ GCC_except_table1608
+ GCC_except_table169
+ GCC_except_table1710
+ GCC_except_table1716
+ GCC_except_table1774
+ GCC_except_table1800
+ GCC_except_table1806
+ GCC_except_table1887
+ GCC_except_table1907
+ GCC_except_table193
+ GCC_except_table2023
+ GCC_except_table2171
+ GCC_except_table2201
+ GCC_except_table2204
+ GCC_except_table2207
+ GCC_except_table2212
+ GCC_except_table2224
+ GCC_except_table2229
+ GCC_except_table2232
+ GCC_except_table2349
+ GCC_except_table235
+ GCC_except_table2352
+ GCC_except_table2356
+ GCC_except_table2374
+ GCC_except_table2507
+ GCC_except_table254
+ GCC_except_table2564
+ GCC_except_table257
+ GCC_except_table2576
+ GCC_except_table2607
+ GCC_except_table2630
+ GCC_except_table2641
+ GCC_except_table2678
+ GCC_except_table2679
+ GCC_except_table2683
+ GCC_except_table2686
+ GCC_except_table2689
+ GCC_except_table2690
+ GCC_except_table2694
+ GCC_except_table2695
+ GCC_except_table2704
+ GCC_except_table2712
+ GCC_except_table2713
+ GCC_except_table2780
+ GCC_except_table3041
+ GCC_except_table3119
+ GCC_except_table3156
+ GCC_except_table3167
+ GCC_except_table3189
+ GCC_except_table3192
+ GCC_except_table3195
+ GCC_except_table3226
+ GCC_except_table3286
+ GCC_except_table3491
+ GCC_except_table3517
+ GCC_except_table357
+ GCC_except_table3578
+ GCC_except_table3583
+ GCC_except_table3611
+ GCC_except_table3614
+ GCC_except_table3622
+ GCC_except_table3625
+ GCC_except_table3643
+ GCC_except_table3647
+ GCC_except_table3648
+ GCC_except_table3656
+ GCC_except_table3659
+ GCC_except_table3660
+ GCC_except_table3668
+ GCC_except_table3675
+ GCC_except_table3676
+ GCC_except_table3811
+ GCC_except_table3835
+ GCC_except_table3901
+ GCC_except_table3917
+ GCC_except_table3938
+ GCC_except_table4030
+ GCC_except_table4278
+ GCC_except_table430
+ GCC_except_table4346
+ GCC_except_table4350
+ GCC_except_table4353
+ GCC_except_table4357
+ GCC_except_table4382
+ GCC_except_table4432
+ GCC_except_table4438
+ GCC_except_table4705
+ GCC_except_table4712
+ GCC_except_table4719
+ GCC_except_table4725
+ GCC_except_table4805
+ GCC_except_table4961
+ GCC_except_table4971
+ GCC_except_table4995
+ GCC_except_table5015
+ GCC_except_table5098
+ GCC_except_table5112
+ GCC_except_table5121
+ GCC_except_table5134
+ GCC_except_table5136
+ GCC_except_table5149
+ GCC_except_table5153
+ GCC_except_table5155
+ GCC_except_table5166
+ GCC_except_table5167
+ GCC_except_table5172
+ GCC_except_table5178
+ GCC_except_table5185
+ GCC_except_table5191
+ GCC_except_table5195
+ GCC_except_table5197
+ GCC_except_table5198
+ GCC_except_table5200
+ GCC_except_table5201
+ GCC_except_table5202
+ GCC_except_table5204
+ GCC_except_table5219
+ GCC_except_table528
+ GCC_except_table5293
+ GCC_except_table5297
+ GCC_except_table5351
+ GCC_except_table5380
+ GCC_except_table5383
+ GCC_except_table5463
+ GCC_except_table5477
+ GCC_except_table5484
+ GCC_except_table5496
+ GCC_except_table5500
+ GCC_except_table5510
+ GCC_except_table553
+ GCC_except_table559
+ GCC_except_table560
+ GCC_except_table564
+ GCC_except_table5739
+ GCC_except_table5771
+ GCC_except_table5776
+ GCC_except_table5822
+ GCC_except_table5849
+ GCC_except_table585
+ GCC_except_table586
+ GCC_except_table5917
+ GCC_except_table592
+ GCC_except_table6107
+ GCC_except_table6115
+ GCC_except_table6135
+ GCC_except_table6140
+ GCC_except_table618
+ GCC_except_table6246
+ GCC_except_table6301
+ GCC_except_table6392
+ GCC_except_table6393
+ GCC_except_table6403
+ GCC_except_table6404
+ GCC_except_table6416
+ GCC_except_table6447
+ GCC_except_table6458
+ GCC_except_table6463
+ GCC_except_table6468
+ GCC_except_table6496
+ GCC_except_table6581
+ GCC_except_table6593
+ GCC_except_table6616
+ GCC_except_table6627
+ GCC_except_table6630
+ GCC_except_table6653
+ GCC_except_table6665
+ GCC_except_table668
+ GCC_except_table688
+ GCC_except_table6945
+ GCC_except_table6980
+ GCC_except_table7053
+ GCC_except_table7107
+ GCC_except_table7130
+ GCC_except_table7171
+ GCC_except_table7182
+ GCC_except_table7322
+ GCC_except_table7330
+ GCC_except_table7437
+ GCC_except_table7438
+ GCC_except_table7439
+ GCC_except_table7440
+ GCC_except_table7445
+ GCC_except_table745
+ GCC_except_table749
+ GCC_except_table7508
+ GCC_except_table754
+ GCC_except_table7550
+ GCC_except_table7575
+ GCC_except_table7590
+ GCC_except_table7598
+ GCC_except_table7604
+ GCC_except_table7629
+ GCC_except_table7635
+ GCC_except_table7641
+ GCC_except_table7781
+ GCC_except_table919
+ GCC_except_table931
+ GCC_except_table934
+ _AudioConverterFillComplexBuffer_BlockInvoke.26283
+ _MobileTimerLibrary.803
+ _MobileTimerLibraryCore.frameworkLibrary.808
+ _NSURLIsPurgeableKey
+ _OBJC_CLASS_$_CSRemoteAssetManagerFactory
+ _OBJC_CLASS_$_SSRSecureAssetProvider
+ _OBJC_IVAR_$_CSVoiceTriggerFileLogger._isExclaveHardware
+ _SSRVoiceRetrainingSecureAssetKey
+ ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.185
+ ___112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.132
+ ___133-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.111
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.189
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.190
+ ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.159
+ ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.251
+ ___50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.63
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.40
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.45
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.49
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.56
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.57
+ ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.261
+ ___66-[CSSiriSpeechRecorder _prepareSpeechControllerWithOptions:error:]_block_invoke.63
+ ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.262
+ ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.250
+ ___77-[CSBuiltInVoiceTrigger activationEventNotificationHandler:event:completion:]_block_invoke.149
+ ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.114
+ ___77-[CSSpeechManager CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke.82
+ ___79-[CSVoiceProfileRetrainManager CSVoiceTriggerEnabledMonitor:didReceiveEnabled:]_block_invoke.18
+ ___79-[CSVoiceTriggerFileLogger _logVTResult:metaFilePath:audioFilePath:completion:]_block_invoke_2
+ ___79-[CSVoiceTriggerFileLogger _logVTResult:metaFilePath:audioFilePath:completion:]_block_invoke_3
+ ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.205
+ ___85-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:]_block_invoke.231
+ ___85-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]_block_invoke
+ ___85-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]_block_invoke.28
+ ___85-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]_block_invoke.30
+ ___87-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:secureAsset:]_block_invoke
+ ___87-[CSVoiceProfileRetrainManager triggerVoiceProfileRetrainingWithAsset:withSecureAsset:]_block_invoke
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.217
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.218
+ ___Block_byref_object_copy_.10150
+ ___Block_byref_object_copy_.10620
+ ___Block_byref_object_copy_.11852
+ ___Block_byref_object_copy_.13143
+ ___Block_byref_object_copy_.13562
+ ___Block_byref_object_copy_.1450
+ ___Block_byref_object_copy_.14622
+ ___Block_byref_object_copy_.14957
+ ___Block_byref_object_copy_.15833
+ ___Block_byref_object_copy_.15946
+ ___Block_byref_object_copy_.17573
+ ___Block_byref_object_copy_.1774
+ ___Block_byref_object_copy_.17861
+ ___Block_byref_object_copy_.19012
+ ___Block_byref_object_copy_.20146
+ ___Block_byref_object_copy_.20797
+ ___Block_byref_object_copy_.21409
+ ___Block_byref_object_copy_.21651
+ ___Block_byref_object_copy_.22287
+ ___Block_byref_object_copy_.2268
+ ___Block_byref_object_copy_.22948
+ ___Block_byref_object_copy_.23218
+ ___Block_byref_object_copy_.23951
+ ___Block_byref_object_copy_.24755
+ ___Block_byref_object_copy_.25192
+ ___Block_byref_object_copy_.26029
+ ___Block_byref_object_copy_.26464
+ ___Block_byref_object_copy_.2661
+ ___Block_byref_object_copy_.27284
+ ___Block_byref_object_copy_.3644
+ ___Block_byref_object_copy_.3779
+ ___Block_byref_object_copy_.3986
+ ___Block_byref_object_copy_.4579
+ ___Block_byref_object_copy_.6425
+ ___Block_byref_object_copy_.7377
+ ___Block_byref_object_copy_.8394
+ ___Block_byref_object_copy_.8987
+ ___Block_byref_object_dispose_.10151
+ ___Block_byref_object_dispose_.10621
+ ___Block_byref_object_dispose_.11853
+ ___Block_byref_object_dispose_.13144
+ ___Block_byref_object_dispose_.13563
+ ___Block_byref_object_dispose_.1451
+ ___Block_byref_object_dispose_.14623
+ ___Block_byref_object_dispose_.14958
+ ___Block_byref_object_dispose_.15834
+ ___Block_byref_object_dispose_.15947
+ ___Block_byref_object_dispose_.17574
+ ___Block_byref_object_dispose_.1775
+ ___Block_byref_object_dispose_.17862
+ ___Block_byref_object_dispose_.19013
+ ___Block_byref_object_dispose_.20147
+ ___Block_byref_object_dispose_.20798
+ ___Block_byref_object_dispose_.21410
+ ___Block_byref_object_dispose_.21652
+ ___Block_byref_object_dispose_.22288
+ ___Block_byref_object_dispose_.2269
+ ___Block_byref_object_dispose_.22949
+ ___Block_byref_object_dispose_.23219
+ ___Block_byref_object_dispose_.23952
+ ___Block_byref_object_dispose_.24756
+ ___Block_byref_object_dispose_.25193
+ ___Block_byref_object_dispose_.26030
+ ___Block_byref_object_dispose_.26465
+ ___Block_byref_object_dispose_.2662
+ ___Block_byref_object_dispose_.27285
+ ___Block_byref_object_dispose_.3645
+ ___Block_byref_object_dispose_.3780
+ ___Block_byref_object_dispose_.3987
+ ___Block_byref_object_dispose_.4580
+ ___Block_byref_object_dispose_.6426
+ ___Block_byref_object_dispose_.7378
+ ___Block_byref_object_dispose_.8395
+ ___Block_byref_object_dispose_.8988
+ ___MobileTimerLibraryCore_block_invoke.809
+ ___block_literal_global.10.10769
+ ___block_literal_global.10.19540
+ ___block_literal_global.10.21095
+ ___block_literal_global.10.22147
+ ___block_literal_global.10255
+ ___block_literal_global.1029
+ ___block_literal_global.10401
+ ___block_literal_global.10637
+ ___block_literal_global.10795
+ ___block_literal_global.11.12132
+ ___block_literal_global.11012
+ ___block_literal_global.112
+ ___block_literal_global.11234
+ ___block_literal_global.117
+ ___block_literal_global.11706
+ ___block_literal_global.1185
+ ___block_literal_global.11879
+ ___block_literal_global.12.14116
+ ___block_literal_global.12142
+ ___block_literal_global.12242
+ ___block_literal_global.12364
+ ___block_literal_global.12672
+ ___block_literal_global.12778
+ ___block_literal_global.12834
+ ___block_literal_global.1287
+ ___block_literal_global.12889
+ ___block_literal_global.13.21096
+ ___block_literal_global.13.21242
+ ___block_literal_global.13.22148
+ ___block_literal_global.13350
+ ___block_literal_global.13466
+ ___block_literal_global.13692
+ ___block_literal_global.14.21167
+ ___block_literal_global.14109
+ ___block_literal_global.14455
+ ___block_literal_global.14512
+ ___block_literal_global.14701
+ ___block_literal_global.14719
+ ___block_literal_global.14830
+ ___block_literal_global.15355
+ ___block_literal_global.15440
+ ___block_literal_global.158
+ ___block_literal_global.1580
+ ___block_literal_global.15933
+ ___block_literal_global.15975
+ ___block_literal_global.16.10383
+ ___block_literal_global.16.12122
+ ___block_literal_global.16.13351
+ ___block_literal_global.16.14513
+ ___block_literal_global.16.21097
+ ___block_literal_global.16618
+ ___block_literal_global.17.14456
+ ___block_literal_global.17.21168
+ ___block_literal_global.17092
+ ___block_literal_global.17101
+ ___block_literal_global.17147
+ ___block_literal_global.17181
+ ___block_literal_global.17445
+ ___block_literal_global.17521
+ ___block_literal_global.17630
+ ___block_literal_global.18.14800
+ ___block_literal_global.18.21243
+ ___block_literal_global.18091
+ ___block_literal_global.18160
+ ___block_literal_global.18190
+ ___block_literal_global.18747
+ ___block_literal_global.19032
+ ___block_literal_global.19338
+ ___block_literal_global.19419
+ ___block_literal_global.19557
+ ___block_literal_global.19672
+ ___block_literal_global.19717
+ ___block_literal_global.19733
+ ___block_literal_global.20.13327
+ ___block_literal_global.20.14457
+ ___block_literal_global.20.21169
+ ___block_literal_global.20.25175
+ ___block_literal_global.20011
+ ___block_literal_global.20063
+ ___block_literal_global.20168
+ ___block_literal_global.20244
+ ___block_literal_global.20444
+ ___block_literal_global.20781
+ ___block_literal_global.21.12779
+ ___block_literal_global.21081
+ ___block_literal_global.21094
+ ___block_literal_global.21166
+ ___block_literal_global.2119
+ ___block_literal_global.21262
+ ___block_literal_global.21312
+ ___block_literal_global.21355
+ ___block_literal_global.21478
+ ___block_literal_global.22.17419
+ ___block_literal_global.22.21098
+ ___block_literal_global.22145
+ ___block_literal_global.22658
+ ___block_literal_global.22830
+ ___block_literal_global.2288
+ ___block_literal_global.22980
+ ___block_literal_global.23.21170
+ ___block_literal_global.23528
+ ___block_literal_global.2367
+ ___block_literal_global.23744
+ ___block_literal_global.23828
+ ___block_literal_global.24.12780
+ ___block_literal_global.240
+ ___block_literal_global.24207
+ ___block_literal_global.2469
+ ___block_literal_global.2483
+ ___block_literal_global.24892
+ ___block_literal_global.25.21099
+ ___block_literal_global.25216
+ ___block_literal_global.25547
+ ___block_literal_global.25837
+ ___block_literal_global.25886
+ ___block_literal_global.26.25164
+ ___block_literal_global.26065
+ ___block_literal_global.26170
+ ___block_literal_global.26400
+ ___block_literal_global.26533
+ ___block_literal_global.27.12781
+ ___block_literal_global.27079
+ ___block_literal_global.27295
+ ___block_literal_global.2751
+ ___block_literal_global.27569
+ ___block_literal_global.2811
+ ___block_literal_global.29.21100
+ ___block_literal_global.29.21171
+ ___block_literal_global.2902
+ ___block_literal_global.30.12782
+ ___block_literal_global.30.13312
+ ___block_literal_global.3126
+ ___block_literal_global.3342
+ ___block_literal_global.3512
+ ___block_literal_global.36.12783
+ ___block_literal_global.3695
+ ___block_literal_global.3770
+ ___block_literal_global.38.9137
+ ___block_literal_global.40.20759
+ ___block_literal_global.4024
+ ___block_literal_global.42.12784
+ ___block_literal_global.46.9129
+ ___block_literal_global.47
+ ___block_literal_global.5.27570
+ ___block_literal_global.5063
+ ___block_literal_global.521
+ ___block_literal_global.54.2363
+ ___block_literal_global.5690
+ ___block_literal_global.57
+ ___block_literal_global.5801
+ ___block_literal_global.59.11228
+ ___block_literal_global.59.6456
+ ___block_literal_global.5987
+ ___block_literal_global.6.26060
+ ___block_literal_global.6089
+ ___block_literal_global.61
+ ___block_literal_global.6112
+ ___block_literal_global.6492
+ ___block_literal_global.661
+ ___block_literal_global.6628
+ ___block_literal_global.674
+ ___block_literal_global.6911
+ ___block_literal_global.7.22146
+ ___block_literal_global.7.818
+ ___block_literal_global.766
+ ___block_literal_global.8.1167
+ ___block_literal_global.8.26164
+ ___block_literal_global.8.26534
+ ___block_literal_global.8.27571
+ ___block_literal_global.81
+ ___block_literal_global.830
+ ___block_literal_global.84
+ ___block_literal_global.8566
+ ___block_literal_global.9169
+ ___block_literal_global.9221
+ ___block_literal_global.9338
+ ___block_literal_global.944
+ ___block_literal_global.9746
+ __block_invoke.enableHeartbeat.11008
+ __compensateChannelDataIfNeeded:receivedNumChannels:.heartbeat.14610
+ __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.18672
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10993
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.18661
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.26765
+ __runRetrainerWithAssets:withSecureAsset:languageCode:.onceCleanupToken
+ _audit_stringMobileTimer.812
+ _objc_msgSend$_getSecondPassRejectReasonFromExclaveKeywordResult:speakerDetectionResult:
+ _objc_msgSend$_moveSecureAudioCaptureFrom:withExclaveTimestamp:
+ _objc_msgSend$_retrainingVoiceProfile:voiceProfile:asset:secureAsset:
+ _objc_msgSend$_runRetrainerWithAssets:withSecureAsset:languageCode:
+ _objc_msgSend$_runVoiceProfileRetrainerWithAsset:withSecureAsset:withLanguageCode:
+ _objc_msgSend$_syncAvailableSecureCaptures
+ _objc_msgSend$copyItemAtPath:toPath:error:
+ _objc_msgSend$fetchSecureAssetForLocale:withAsset:
+ _objc_msgSend$needRetrainingForExclaveOnly
+ _objc_msgSend$remoteAssetManager
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$triggerVoiceProfileRetrainingWithAsset:withSecureAsset:
+ _remote_device_copy_device_with_uuid
+ _remote_device_copy_product_type
+ _sharedController.onceToken.11878
+ _sharedController.sharedController.11880
+ _sharedHandler.onceToken.1028
+ _sharedHandler.onceToken.19337
+ _sharedHandler.onceToken.26064
+ _sharedHandler.sharedHandler.1030
+ _sharedHandler.sharedHandler.19339
+ _sharedHandler.sharedHandler.26066
+ _sharedHandlerDisabledOnDeviceCompilation.onceToken.26059
+ _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.26061
+ _sharedInstance._sharedInstance.11707
+ _sharedInstance._sharedInstance.12890
+ _sharedInstance._sharedInstance.14831
+ _sharedInstance._sharedInstance.17148
+ _sharedInstance._sharedInstance.17446
+ _sharedInstance._sharedInstance.17522
+ _sharedInstance._sharedInstance.18161
+ _sharedInstance._sharedInstance.19673
+ _sharedInstance._sharedInstance.20012
+ _sharedInstance._sharedInstance.20064
+ _sharedInstance._sharedInstance.20245
+ _sharedInstance._sharedInstance.23529
+ _sharedInstance._sharedInstance.24208
+ _sharedInstance._sharedInstance.25887
+ _sharedInstance._sharedInstance.27296
+ _sharedInstance._sharedInstance.2752
+ _sharedInstance._sharedInstance.2812
+ _sharedInstance._sharedInstance.3127
+ _sharedInstance._sharedInstance.5691
+ _sharedInstance._sharedInstance.5802
+ _sharedInstance._sharedInstance.6090
+ _sharedInstance._sharedInstance.662
+ _sharedInstance._sharedInstance.6629
+ _sharedInstance._sharedInstance.767
+ _sharedInstance._sharedInstance.831
+ _sharedInstance._sharedInstance.9222
+ _sharedInstance.onceToken.10400
+ _sharedInstance.onceToken.10636
+ _sharedInstance.onceToken.10794
+ _sharedInstance.onceToken.11705
+ _sharedInstance.onceToken.1184
+ _sharedInstance.onceToken.12833
+ _sharedInstance.onceToken.1286
+ _sharedInstance.onceToken.12888
+ _sharedInstance.onceToken.13465
+ _sharedInstance.onceToken.14829
+ _sharedInstance.onceToken.15354
+ _sharedInstance.onceToken.15439
+ _sharedInstance.onceToken.15932
+ _sharedInstance.onceToken.17146
+ _sharedInstance.onceToken.17444
+ _sharedInstance.onceToken.17520
+ _sharedInstance.onceToken.17629
+ _sharedInstance.onceToken.18090
+ _sharedInstance.onceToken.18159
+ _sharedInstance.onceToken.18189
+ _sharedInstance.onceToken.19556
+ _sharedInstance.onceToken.19671
+ _sharedInstance.onceToken.20010
+ _sharedInstance.onceToken.20062
+ _sharedInstance.onceToken.20243
+ _sharedInstance.onceToken.21080
+ _sharedInstance.onceToken.21261
+ _sharedInstance.onceToken.21354
+ _sharedInstance.onceToken.21477
+ _sharedInstance.onceToken.22657
+ _sharedInstance.onceToken.22829
+ _sharedInstance.onceToken.22979
+ _sharedInstance.onceToken.23527
+ _sharedInstance.onceToken.23827
+ _sharedInstance.onceToken.24206
+ _sharedInstance.onceToken.25546
+ _sharedInstance.onceToken.25885
+ _sharedInstance.onceToken.27078
+ _sharedInstance.onceToken.27294
+ _sharedInstance.onceToken.2750
+ _sharedInstance.onceToken.2810
+ _sharedInstance.onceToken.2901
+ _sharedInstance.onceToken.3125
+ _sharedInstance.onceToken.3511
+ _sharedInstance.onceToken.5062
+ _sharedInstance.onceToken.520
+ _sharedInstance.onceToken.5689
+ _sharedInstance.onceToken.5800
+ _sharedInstance.onceToken.6088
+ _sharedInstance.onceToken.660
+ _sharedInstance.onceToken.6627
+ _sharedInstance.onceToken.765
+ _sharedInstance.onceToken.829
+ _sharedInstance.onceToken.9220
+ _sharedInstance.sSharedInstance.18191
+ _sharedInstance.sharedInstance.12835
+ _sharedInstance.sharedInstance.13467
+ _sharedInstance.sharedInstance.15441
+ _sharedInstance.sharedInstance.18092
+ _sharedInstance.sharedInstance.19558
+ _sharedInstance.sharedInstance.21082
+ _sharedInstance.sharedInstance.21356
+ _sharedInstance.sharedInstance.22831
+ _sharedInstance.sharedInstance.22981
+ _sharedInstance.sharedInstance.27080
+ _sharedInstance.sharedInstance.3513
+ _sharedInstance.sharedInstance.5064
+ _sharedInstance.sharedManager.25548
+ _sharedInstance.sharedPolicy.1186
+ _sharedInstance.sharedPolicy.21263
+ _sharedInstance.sharedPolicy.23829
+ _sharedInstance.sharedProvider.22659
+ _sharedManager.onceToken.17091
+ _sharedManager.onceToken.19031
+ _sharedManager.onceToken.6491
+ _sharedManager.onceToken.6910
+ _sharedManager.sharedManager.17093
+ _sharedManager.sharedManager.6493
+ _sharedManager.sharedManager.6912
+ _sharedMonitor.onceToken.20167
+ _sharedMonitor.sharedMonitor.20169
+ _sharedService.onceToken.15974
+ _sharedService.onceToken.25215
+ _sharedService.sharedService.25217
+ _uuid_parse
- -[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:]
- -[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]
- -[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]
- -[CSVoiceProfileRetrainManager triggerVoiceProfileRetrainingWithAsset:]
- GCC_except_table1247
- GCC_except_table1259
- GCC_except_table1465
- GCC_except_table1531
- GCC_except_table1555
- GCC_except_table1559
- GCC_except_table1575
- GCC_except_table1578
- GCC_except_table1606
- GCC_except_table168
- GCC_except_table1704
- GCC_except_table1714
- GCC_except_table1772
- GCC_except_table1798
- GCC_except_table1804
- GCC_except_table1885
- GCC_except_table1905
- GCC_except_table192
- GCC_except_table2021
- GCC_except_table2169
- GCC_except_table2199
- GCC_except_table2202
- GCC_except_table2205
- GCC_except_table2210
- GCC_except_table2222
- GCC_except_table2227
- GCC_except_table2230
- GCC_except_table233
- GCC_except_table2347
- GCC_except_table2350
- GCC_except_table2354
- GCC_except_table2372
- GCC_except_table2505
- GCC_except_table252
- GCC_except_table255
- GCC_except_table2562
- GCC_except_table2574
- GCC_except_table2605
- GCC_except_table2628
- GCC_except_table2639
- GCC_except_table2673
- GCC_except_table2674
- GCC_except_table2681
- GCC_except_table2684
- GCC_except_table2687
- GCC_except_table2688
- GCC_except_table2692
- GCC_except_table2693
- GCC_except_table2702
- GCC_except_table2708
- GCC_except_table2711
- GCC_except_table2778
- GCC_except_table3039
- GCC_except_table3117
- GCC_except_table3154
- GCC_except_table3165
- GCC_except_table3187
- GCC_except_table3190
- GCC_except_table3193
- GCC_except_table3224
- GCC_except_table3284
- GCC_except_table3489
- GCC_except_table3515
- GCC_except_table355
- GCC_except_table3576
- GCC_except_table3577
- GCC_except_table3597
- GCC_except_table3612
- GCC_except_table3620
- GCC_except_table3623
- GCC_except_table3629
- GCC_except_table3640
- GCC_except_table3645
- GCC_except_table3649
- GCC_except_table3650
- GCC_except_table3658
- GCC_except_table3666
- GCC_except_table3671
- GCC_except_table3672
- GCC_except_table3809
- GCC_except_table3833
- GCC_except_table3893
- GCC_except_table3909
- GCC_except_table3930
- GCC_except_table4022
- GCC_except_table4270
- GCC_except_table428
- GCC_except_table4337
- GCC_except_table4338
- GCC_except_table4342
- GCC_except_table4349
- GCC_except_table4374
- GCC_except_table4424
- GCC_except_table4430
- GCC_except_table4697
- GCC_except_table4704
- GCC_except_table4711
- GCC_except_table4717
- GCC_except_table4797
- GCC_except_table4953
- GCC_except_table4963
- GCC_except_table4987
- GCC_except_table5007
- GCC_except_table5090
- GCC_except_table5104
- GCC_except_table5113
- GCC_except_table5120
- GCC_except_table5126
- GCC_except_table5131
- GCC_except_table5141
- GCC_except_table5145
- GCC_except_table5158
- GCC_except_table5159
- GCC_except_table5164
- GCC_except_table5170
- GCC_except_table5175
- GCC_except_table5177
- GCC_except_table5179
- GCC_except_table5181
- GCC_except_table5182
- GCC_except_table5184
- GCC_except_table5186
- GCC_except_table5188
- GCC_except_table5193
- GCC_except_table5211
- GCC_except_table526
- GCC_except_table5285
- GCC_except_table5289
- GCC_except_table5343
- GCC_except_table5372
- GCC_except_table5375
- GCC_except_table5455
- GCC_except_table5469
- GCC_except_table5476
- GCC_except_table5488
- GCC_except_table5492
- GCC_except_table5502
- GCC_except_table551
- GCC_except_table556
- GCC_except_table557
- GCC_except_table562
- GCC_except_table5731
- GCC_except_table5762
- GCC_except_table5767
- GCC_except_table5804
- GCC_except_table582
- GCC_except_table583
- GCC_except_table5840
- GCC_except_table590
- GCC_except_table5908
- GCC_except_table6098
- GCC_except_table6106
- GCC_except_table6126
- GCC_except_table6131
- GCC_except_table616
- GCC_except_table6237
- GCC_except_table6292
- GCC_except_table6383
- GCC_except_table6384
- GCC_except_table6394
- GCC_except_table6395
- GCC_except_table6407
- GCC_except_table6438
- GCC_except_table6449
- GCC_except_table6454
- GCC_except_table6459
- GCC_except_table6487
- GCC_except_table6572
- GCC_except_table6584
- GCC_except_table6607
- GCC_except_table6618
- GCC_except_table6621
- GCC_except_table6644
- GCC_except_table6656
- GCC_except_table666
- GCC_except_table686
- GCC_except_table6936
- GCC_except_table6971
- GCC_except_table7044
- GCC_except_table7098
- GCC_except_table7121
- GCC_except_table7162
- GCC_except_table7173
- GCC_except_table7313
- GCC_except_table7321
- GCC_except_table741
- GCC_except_table7427
- GCC_except_table7428
- GCC_except_table7429
- GCC_except_table7430
- GCC_except_table7431
- GCC_except_table747
- GCC_except_table7499
- GCC_except_table752
- GCC_except_table7541
- GCC_except_table7566
- GCC_except_table7581
- GCC_except_table7589
- GCC_except_table7595
- GCC_except_table7620
- GCC_except_table7626
- GCC_except_table7632
- GCC_except_table7772
- GCC_except_table917
- GCC_except_table929
- GCC_except_table932
- _AudioConverterFillComplexBuffer_BlockInvoke.26244
- _MobileTimerLibrary.800
- _MobileTimerLibraryCore.frameworkLibrary.805
- _OBJC_CLASS_$_CSRemoteAssetManager
- ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.182
- ___112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.131
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.186
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.187
- ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.156
- ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.248
- ___50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.62
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.39
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.43
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.48
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.55
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.56
- ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.258
- ___66-[CSSiriSpeechRecorder _prepareSpeechControllerWithOptions:error:]_block_invoke.60
- ___69-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke
- ___69-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke.28
- ___69-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke.30
- ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.259
- ___71-[CSVoiceProfileRetrainManager triggerVoiceProfileRetrainingWithAsset:]_block_invoke
- ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.247
- ___75-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:]_block_invoke
- ___77-[CSBuiltInVoiceTrigger activationEventNotificationHandler:event:completion:]_block_invoke.148
- ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.111
- ___77-[CSSpeechManager CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke.81
- ___79-[CSVoiceProfileRetrainManager CSVoiceTriggerEnabledMonitor:didReceiveEnabled:]_block_invoke.17
- ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.202
- ___85-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:]_block_invoke.228
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.214
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.215
- ___Block_byref_object_copy_.10152
- ___Block_byref_object_copy_.10622
- ___Block_byref_object_copy_.11829
- ___Block_byref_object_copy_.13120
- ___Block_byref_object_copy_.13539
- ___Block_byref_object_copy_.1447
- ___Block_byref_object_copy_.14599
- ___Block_byref_object_copy_.14934
- ___Block_byref_object_copy_.15809
- ___Block_byref_object_copy_.15922
- ___Block_byref_object_copy_.17548
- ___Block_byref_object_copy_.1771
- ___Block_byref_object_copy_.17840
- ___Block_byref_object_copy_.18991
- ___Block_byref_object_copy_.20126
- ___Block_byref_object_copy_.20778
- ___Block_byref_object_copy_.21390
- ___Block_byref_object_copy_.21632
- ___Block_byref_object_copy_.22265
- ___Block_byref_object_copy_.2265
- ___Block_byref_object_copy_.22920
- ___Block_byref_object_copy_.23191
- ___Block_byref_object_copy_.23927
- ___Block_byref_object_copy_.24718
- ___Block_byref_object_copy_.25152
- ___Block_byref_object_copy_.25990
- ___Block_byref_object_copy_.26425
- ___Block_byref_object_copy_.2658
- ___Block_byref_object_copy_.27244
- ___Block_byref_object_copy_.3641
- ___Block_byref_object_copy_.3776
- ___Block_byref_object_copy_.3983
- ___Block_byref_object_copy_.4576
- ___Block_byref_object_copy_.6428
- ___Block_byref_object_copy_.7381
- ___Block_byref_object_copy_.8393
- ___Block_byref_object_copy_.8989
- ___Block_byref_object_dispose_.10153
- ___Block_byref_object_dispose_.10623
- ___Block_byref_object_dispose_.11830
- ___Block_byref_object_dispose_.13121
- ___Block_byref_object_dispose_.13540
- ___Block_byref_object_dispose_.1448
- ___Block_byref_object_dispose_.14600
- ___Block_byref_object_dispose_.14935
- ___Block_byref_object_dispose_.15810
- ___Block_byref_object_dispose_.15923
- ___Block_byref_object_dispose_.17549
- ___Block_byref_object_dispose_.1772
- ___Block_byref_object_dispose_.17841
- ___Block_byref_object_dispose_.18992
- ___Block_byref_object_dispose_.20127
- ___Block_byref_object_dispose_.20779
- ___Block_byref_object_dispose_.21391
- ___Block_byref_object_dispose_.21633
- ___Block_byref_object_dispose_.22266
- ___Block_byref_object_dispose_.2266
- ___Block_byref_object_dispose_.22921
- ___Block_byref_object_dispose_.23192
- ___Block_byref_object_dispose_.23928
- ___Block_byref_object_dispose_.24719
- ___Block_byref_object_dispose_.25153
- ___Block_byref_object_dispose_.25991
- ___Block_byref_object_dispose_.26426
- ___Block_byref_object_dispose_.2659
- ___Block_byref_object_dispose_.27245
- ___Block_byref_object_dispose_.3642
- ___Block_byref_object_dispose_.3777
- ___Block_byref_object_dispose_.3984
- ___Block_byref_object_dispose_.4577
- ___Block_byref_object_dispose_.6429
- ___Block_byref_object_dispose_.7382
- ___Block_byref_object_dispose_.8394
- ___Block_byref_object_dispose_.8990
- ___MobileTimerLibraryCore_block_invoke.806
- ___block_literal_global.10.10771
- ___block_literal_global.10.19520
- ___block_literal_global.10.21076
- ___block_literal_global.10.22128
- ___block_literal_global.10257
- ___block_literal_global.1026
- ___block_literal_global.10403
- ___block_literal_global.10639
- ___block_literal_global.10797
- ___block_literal_global.109
- ___block_literal_global.11.12107
- ___block_literal_global.11013
- ___block_literal_global.11225
- ___block_literal_global.114
- ___block_literal_global.11684
- ___block_literal_global.1182
- ___block_literal_global.11856
- ___block_literal_global.12.14093
- ___block_literal_global.12117
- ___block_literal_global.12217
- ___block_literal_global.12339
- ___block_literal_global.12647
- ___block_literal_global.12753
- ___block_literal_global.12809
- ___block_literal_global.1284
- ___block_literal_global.12864
- ___block_literal_global.13.21077
- ___block_literal_global.13.21223
- ___block_literal_global.13.22129
- ___block_literal_global.13327
- ___block_literal_global.13443
- ___block_literal_global.13669
- ___block_literal_global.14.21148
- ___block_literal_global.14086
- ___block_literal_global.14432
- ___block_literal_global.14489
- ___block_literal_global.14678
- ___block_literal_global.14696
- ___block_literal_global.14807
- ___block_literal_global.15332
- ___block_literal_global.15417
- ___block_literal_global.155
- ___block_literal_global.1577
- ___block_literal_global.15909
- ___block_literal_global.15951
- ___block_literal_global.16.10385
- ___block_literal_global.16.12097
- ___block_literal_global.16.13328
- ___block_literal_global.16.14490
- ___block_literal_global.16.21078
- ___block_literal_global.16595
- ___block_literal_global.17.14433
- ___block_literal_global.17.21149
- ___block_literal_global.17069
- ___block_literal_global.17078
- ___block_literal_global.17124
- ___block_literal_global.17158
- ___block_literal_global.17422
- ___block_literal_global.17498
- ___block_literal_global.17606
- ___block_literal_global.18.14777
- ___block_literal_global.18.21224
- ___block_literal_global.18069
- ___block_literal_global.18138
- ___block_literal_global.18168
- ___block_literal_global.18731
- ___block_literal_global.19011
- ___block_literal_global.19318
- ___block_literal_global.19399
- ___block_literal_global.19537
- ___block_literal_global.19652
- ___block_literal_global.19697
- ___block_literal_global.19713
- ___block_literal_global.19991
- ___block_literal_global.20.13304
- ___block_literal_global.20.14434
- ___block_literal_global.20.21150
- ___block_literal_global.20.25135
- ___block_literal_global.20043
- ___block_literal_global.20148
- ___block_literal_global.20224
- ___block_literal_global.20425
- ___block_literal_global.20762
- ___block_literal_global.21.12754
- ___block_literal_global.21062
- ___block_literal_global.21075
- ___block_literal_global.21147
- ___block_literal_global.2116
- ___block_literal_global.21243
- ___block_literal_global.21293
- ___block_literal_global.21336
- ___block_literal_global.21459
- ___block_literal_global.22.17396
- ___block_literal_global.22.21079
- ___block_literal_global.22126
- ___block_literal_global.22630
- ___block_literal_global.22802
- ___block_literal_global.2285
- ___block_literal_global.22952
- ___block_literal_global.23.21151
- ___block_literal_global.23504
- ___block_literal_global.2364
- ___block_literal_global.237
- ___block_literal_global.23720
- ___block_literal_global.23804
- ___block_literal_global.24.12755
- ___block_literal_global.24181
- ___block_literal_global.2466
- ___block_literal_global.2480
- ___block_literal_global.24854
- ___block_literal_global.25.21080
- ___block_literal_global.25176
- ___block_literal_global.25508
- ___block_literal_global.25798
- ___block_literal_global.25847
- ___block_literal_global.26.25124
- ___block_literal_global.26026
- ___block_literal_global.26131
- ___block_literal_global.26361
- ___block_literal_global.26494
- ___block_literal_global.27.12756
- ___block_literal_global.27039
- ___block_literal_global.27255
- ___block_literal_global.2748
- ___block_literal_global.27529
- ___block_literal_global.2808
- ___block_literal_global.2899
- ___block_literal_global.29.21081
- ___block_literal_global.29.21152
- ___block_literal_global.30.12757
- ___block_literal_global.30.13289
- ___block_literal_global.3123
- ___block_literal_global.3339
- ___block_literal_global.3509
- ___block_literal_global.36.12758
- ___block_literal_global.3692
- ___block_literal_global.3767
- ___block_literal_global.38.9139
- ___block_literal_global.40.20740
- ___block_literal_global.4021
- ___block_literal_global.42.12759
- ___block_literal_global.46.6462
- ___block_literal_global.46.9131
- ___block_literal_global.5.27530
- ___block_literal_global.50
- ___block_literal_global.5060
- ___block_literal_global.518
- ___block_literal_global.52
- ___block_literal_global.54.11215
- ___block_literal_global.54.2360
- ___block_literal_global.5687
- ___block_literal_global.5798
- ___block_literal_global.58
- ___block_literal_global.5984
- ___block_literal_global.6.26021
- ___block_literal_global.6086
- ___block_literal_global.6109
- ___block_literal_global.6495
- ___block_literal_global.658
- ___block_literal_global.6632
- ___block_literal_global.671
- ___block_literal_global.6915
- ___block_literal_global.7.22127
- ___block_literal_global.7.815
- ___block_literal_global.763
- ___block_literal_global.8.1164
- ___block_literal_global.8.26125
- ___block_literal_global.8.26495
- ___block_literal_global.8.27531
- ___block_literal_global.80
- ___block_literal_global.827
- ___block_literal_global.83
- ___block_literal_global.8565
- ___block_literal_global.9171
- ___block_literal_global.9223
- ___block_literal_global.9340
- ___block_literal_global.941
- ___block_literal_global.9748
- __block_invoke.enableHeartbeat.11009
- __compensateChannelDataIfNeeded:receivedNumChannels:.heartbeat.14587
- __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.18657
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10994
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.18648
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.26725
- __runRetrainerWithAssets:languageCode:.onceCleanupToken
- _audit_stringMobileTimer.809
- _objc_msgSend$_retrainingVoiceProfile:voiceProfile:asset:
- _objc_msgSend$_runRetrainerWithAssets:languageCode:
- _objc_msgSend$_runVoiceProfileRetrainerWithAsset:withLanguageCode:
- _objc_msgSend$triggerVoiceProfileRetrainingWithAsset:
- _sharedController.onceToken.11855
- _sharedController.sharedController.11857
- _sharedHandler.onceToken.1025
- _sharedHandler.onceToken.19317
- _sharedHandler.onceToken.26025
- _sharedHandler.sharedHandler.1027
- _sharedHandler.sharedHandler.19319
- _sharedHandler.sharedHandler.26027
- _sharedHandlerDisabledOnDeviceCompilation.onceToken.26020
- _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.26022
- _sharedInstance._sharedInstance.11685
- _sharedInstance._sharedInstance.12865
- _sharedInstance._sharedInstance.14808
- _sharedInstance._sharedInstance.17125
- _sharedInstance._sharedInstance.17423
- _sharedInstance._sharedInstance.17499
- _sharedInstance._sharedInstance.18139
- _sharedInstance._sharedInstance.19653
- _sharedInstance._sharedInstance.19992
- _sharedInstance._sharedInstance.20044
- _sharedInstance._sharedInstance.20225
- _sharedInstance._sharedInstance.23505
- _sharedInstance._sharedInstance.24182
- _sharedInstance._sharedInstance.25848
- _sharedInstance._sharedInstance.27256
- _sharedInstance._sharedInstance.2749
- _sharedInstance._sharedInstance.2809
- _sharedInstance._sharedInstance.3124
- _sharedInstance._sharedInstance.5688
- _sharedInstance._sharedInstance.5799
- _sharedInstance._sharedInstance.6087
- _sharedInstance._sharedInstance.659
- _sharedInstance._sharedInstance.6633
- _sharedInstance._sharedInstance.764
- _sharedInstance._sharedInstance.828
- _sharedInstance._sharedInstance.9224
- _sharedInstance.onceToken.10402
- _sharedInstance.onceToken.10638
- _sharedInstance.onceToken.10796
- _sharedInstance.onceToken.11683
- _sharedInstance.onceToken.1181
- _sharedInstance.onceToken.12808
- _sharedInstance.onceToken.1283
- _sharedInstance.onceToken.12863
- _sharedInstance.onceToken.13442
- _sharedInstance.onceToken.14806
- _sharedInstance.onceToken.15331
- _sharedInstance.onceToken.15416
- _sharedInstance.onceToken.15908
- _sharedInstance.onceToken.17123
- _sharedInstance.onceToken.17421
- _sharedInstance.onceToken.17497
- _sharedInstance.onceToken.17605
- _sharedInstance.onceToken.18068
- _sharedInstance.onceToken.18137
- _sharedInstance.onceToken.18167
- _sharedInstance.onceToken.19536
- _sharedInstance.onceToken.19651
- _sharedInstance.onceToken.19990
- _sharedInstance.onceToken.20042
- _sharedInstance.onceToken.20223
- _sharedInstance.onceToken.21061
- _sharedInstance.onceToken.21242
- _sharedInstance.onceToken.21335
- _sharedInstance.onceToken.21458
- _sharedInstance.onceToken.22629
- _sharedInstance.onceToken.22801
- _sharedInstance.onceToken.22951
- _sharedInstance.onceToken.23503
- _sharedInstance.onceToken.23803
- _sharedInstance.onceToken.24180
- _sharedInstance.onceToken.25507
- _sharedInstance.onceToken.25846
- _sharedInstance.onceToken.27038
- _sharedInstance.onceToken.27254
- _sharedInstance.onceToken.2747
- _sharedInstance.onceToken.2807
- _sharedInstance.onceToken.2898
- _sharedInstance.onceToken.3122
- _sharedInstance.onceToken.3508
- _sharedInstance.onceToken.5059
- _sharedInstance.onceToken.517
- _sharedInstance.onceToken.5686
- _sharedInstance.onceToken.5797
- _sharedInstance.onceToken.6085
- _sharedInstance.onceToken.657
- _sharedInstance.onceToken.6631
- _sharedInstance.onceToken.762
- _sharedInstance.onceToken.826
- _sharedInstance.onceToken.9222
- _sharedInstance.sSharedInstance.18169
- _sharedInstance.sharedInstance.12810
- _sharedInstance.sharedInstance.13444
- _sharedInstance.sharedInstance.15418
- _sharedInstance.sharedInstance.18070
- _sharedInstance.sharedInstance.19538
- _sharedInstance.sharedInstance.21063
- _sharedInstance.sharedInstance.21337
- _sharedInstance.sharedInstance.22803
- _sharedInstance.sharedInstance.22953
- _sharedInstance.sharedInstance.27040
- _sharedInstance.sharedInstance.3510
- _sharedInstance.sharedInstance.5061
- _sharedInstance.sharedManager.25509
- _sharedInstance.sharedPolicy.1183
- _sharedInstance.sharedPolicy.21244
- _sharedInstance.sharedPolicy.23805
- _sharedInstance.sharedProvider.22631
- _sharedManager.onceToken.17068
- _sharedManager.onceToken.19010
- _sharedManager.onceToken.6494
- _sharedManager.onceToken.6914
- _sharedManager.sharedManager.17070
- _sharedManager.sharedManager.6496
- _sharedManager.sharedManager.6916
- _sharedMonitor.onceToken.20147
- _sharedMonitor.sharedMonitor.20149
- _sharedService.onceToken.15950
- _sharedService.onceToken.25175
- _sharedService.sharedService.25177
CStrings:
+ "%@-%@"
+ "%s Audio capture folder name %@ is too short to parse date time"
+ "%s Display productType = %@, isLegacyDisplay = %d"
+ "%s Failed to check purgeable status for file %@"
+ "%s Failed to get secure audio capture"
+ "%s Failed to get secure audio logging directory"
+ "%s Failed to move secure audio capture file %@"
+ "%s Failed to parse display UUID %@"
+ "%s Failed to retrieve remote device with UUID %@"
+ "%s Secure audio capture file %@ copied successfully"
+ "%s Secure audio capture file %@ skipped (likely in progress)"
+ "%s Skip start alert for legacy studio display"
+ "-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:secureAsset:]"
+ "-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:secureAsset:]_block_invoke"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]"
+ "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]_block_invoke"
+ "-[CSVoiceProfileRetrainManager triggerVoiceProfileRetrainingWithAsset:withSecureAsset:]_block_invoke"
+ "-[CSVoiceTriggerFileLogger _moveSecureAudioCaptureFrom:withExclaveTimestamp:]"
+ "-[CSVoiceTriggerFileLogger _syncAvailableSecureCaptures]"
+ "/var/mobile/tmp/com.apple.corespeechd/AudioCapture/siri"
+ "AppleDisplay2,1"
+ "Q32@0:8Q16Q24"
+ "_getSecondPassRejectReasonFromExclaveKeywordResult:speakerDetectionResult:"
+ "_moveSecureAudioCaptureFrom:withExclaveTimestamp:"
+ "_retrainingVoiceProfile:voiceProfile:asset:secureAsset:"
+ "_runRetrainerWithAssets:withSecureAsset:languageCode:"
+ "_runVoiceProfileRetrainerWithAsset:withSecureAsset:withLanguageCode:"
+ "_syncAvailableSecureCaptures"
+ "audioRecorderSensorInvalidated:"
+ "copyItemAtPath:toPath:error:"
+ "fetchSecureAssetForLocale:withAsset:"
+ "getSecondPassRejectReasonFromExclaveKeywordResult:speakerDetectionResult:"
+ "needRetrainingForExclaveOnly"
+ "remoteAssetManager"
+ "substringFromIndex:"
+ "triggerVoiceProfileRetrainingWithAsset:withSecureAsset:"
+ "v24@0:8@\"<CSRemoteAssetManagerProtocol>\"16"
- "%s Skip start alert for studio display"
- "-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:]"
- "-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:]_block_invoke"
- "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]"
- "-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:languageCode:]_block_invoke"
- "-[CSVoiceProfileRetrainManager triggerVoiceProfileRetrainingWithAsset:]_block_invoke"
- "_retrainingVoiceProfile:voiceProfile:asset:"
- "_runRetrainerWithAssets:languageCode:"
- "_runVoiceProfileRetrainerWithAsset:withLanguageCode:"
- "triggerVoiceProfileRetrainingWithAsset:"
- "v24@0:8@\"CSRemoteAssetManager\"16"

```
