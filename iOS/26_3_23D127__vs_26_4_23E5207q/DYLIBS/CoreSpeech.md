## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3515.11.1.0.0
-  __TEXT.__text: 0x152a90
-  __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0x1440c
-  __TEXT.__const: 0x58c
+3520.87.3.1.5
+  __TEXT.__text: 0x163778
+  __TEXT.__auth_stubs: 0x1ad0
+  __TEXT.__objc_methlist: 0x1432c
+  __TEXT.__const: 0x40c
   __TEXT.__dlopen_cstrs: 0x197
-  __TEXT.__gcc_except_tab: 0x3cac
-  __TEXT.__cstring: 0x275e9
-  __TEXT.__oslogstring: 0x1efaa
-  __TEXT.__unwind_info: 0x4dc8
-  __TEXT.__objc_classname: 0x2e76
-  __TEXT.__objc_methname: 0x37c57
-  __TEXT.__objc_methtype: 0x7a83
-  __TEXT.__objc_stubs: 0x1c040
+  __TEXT.__gcc_except_tab: 0x3b44
+  __TEXT.__cstring: 0x27a06
+  __TEXT.__oslogstring: 0x1ee59
+  __TEXT.__unwind_info: 0x5df8
+  __TEXT.__objc_classname: 0x2dc9
+  __TEXT.__objc_methname: 0x37f76
+  __TEXT.__objc_methtype: 0x7aaf
+  __TEXT.__objc_stubs: 0x1c120
   __DATA_CONST.__got: 0x1ab0
-  __DATA_CONST.__const: 0x40f8
-  __DATA_CONST.__objc_classlist: 0x840
+  __DATA_CONST.__const: 0x4110
+  __DATA_CONST.__objc_classlist: 0x818
   __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x490
+  __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa848
-  __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_superrefs: 0x688
+  __DATA_CONST.__objc_selrefs: 0xa8c0
+  __DATA_CONST.__objc_protorefs: 0xa0
+  __DATA_CONST.__objc_superrefs: 0x668
   __DATA_CONST.__objc_arraydata: 0x3e8
-  __AUTH_CONST.__auth_got: 0xdc8
+  __AUTH_CONST.__auth_got: 0xd80
   __AUTH_CONST.__const: 0x1e00
-  __AUTH_CONST.__cfstring: 0x9420
-  __AUTH_CONST.__objc_const: 0x203d0
-  __AUTH_CONST.__objc_intobj: 0x990
+  __AUTH_CONST.__cfstring: 0x94c0
+  __AUTH_CONST.__objc_const: 0x1fe60
+  __AUTH_CONST.__objc_intobj: 0x9a8
   __AUTH_CONST.__objc_doubleobj: 0xb0
   __AUTH_CONST.__objc_dictobj: 0x3c0
-  __AUTH_CONST.__objc_floatobj: 0x4c0
+  __AUTH_CONST.__objc_floatobj: 0x4f0
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0x3e80
-  __DATA.__objc_ivar: 0x1900
-  __DATA.__data: 0x3650
-  __DATA.__bss: 0x668
+  __AUTH.__objc_data: 0x3de0
+  __DATA.__objc_ivar: 0x18c0
+  __DATA.__data: 0x35f0
+  __DATA.__bss: 0x670
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1400
+  __DATA_DIRTY.__objc_data: 0x1310
   __DATA_DIRTY.__data: 0xc0
-  __DATA_DIRTY.__bss: 0x158
+  __DATA_DIRTY.__bss: 0x150
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AFC7D832-8EA6-377E-8171-3C95FBCF638D
-  Functions: 7926
-  Symbols:   26053
-  CStrings:  15516
+  UUID: F82B96AD-29C0-3003-A7A0-C7F19D05EA87
+  Functions: 7905
+  Symbols:   25955
+  CStrings:  15509
 
Symbols:
+ +[CSAttendingOptions optionForFlexibleFollowupWithAudioRecordType:deviceId:startAttendingSampleCount:]
+ +[CSEndpointerAssetManager _getOEPAssetWithLanguage:withOEPEntitledAssetManager:]
+ +[CSVoiceTriggerFileLogger deleteAllOnDeviceSMRAudioLogs]
+ +[CSVoiceTriggerFileLogger pruneOnDeviceSMRAudioLogs]
+ -[CSAsset(SpeakerRecognition) inRequestReferenceAudioLengthInSecs]
+ -[CSAsset(SpeakerRecognition) inRequestSegmentLengthInSecs]
+ -[CSAsset(SpeakerRecognition) inRequestSegmentSpkrIdScoreThreshold]
+ -[CSAsset(SpeakerRecognition) invocationUserMinAudioDurationRequired]
+ -[CSAsset(SpeakerRecognition) invocationUserThreshold]
+ -[CSAttendingOptions initWithAttendingType:startAttendingHostTime:startAttendingSampleCount:useVAD:useOwnVoiceVAD:useBoron:startOfSpeechThresholdInMs:prependAudioDuration:timeoutThresholdInSec:triggerType:audioStreamHoldingDurationInSec:audioRecordType:deviceId:attendingListeningType:pauseDurationThreshold:maxPauseDelay:]
+ -[CSAttendingOptions startAttendingSampleCount]
+ -[CSBuiltInVoiceTrigger _hasHearstRoutedAndNotInSplitterOrJarvisRouted]
+ -[CSConnectionListener _notifyDelegateOfNewConnection:]
+ -[CSConnectionListener _notifyDelegateOfRemovedConnection:]
+ -[CSConnectionListener delegate]
+ -[CSConnectionListener initWithMachService:withServiceInterface:withServiceObject:withDelegateInterface:queue:delegate:]
+ -[CSConnectionListener initWithXpcListener:withMachService:withServiceInterface:withServiceObject:withDelegateInterface:queue:delegate:]
+ -[CSConnectionListener notifyRemoteParameter:WithBlock:]
+ -[CSEndpointerAssetManager _resetAndGetOEPAssetsWithLanguage:]
+ -[CSEndpointerAssetManager oepEntitledAssetManager]
+ -[CSEndpointerAssetManager setOepEntitledAssetManager:]
+ -[CSEndpointerXPCClient setIsStoppingWithHTTMode:]
+ -[CSSiriAudioPlaybackService _injectSessionsByRequest:]
+ -[CSSiriAudioPlaybackService _updateRequest:volume:fadeDuration:completion:]
+ -[CSSiriAudioPlaybackService updateRequest:volume:fadeDuration:completion:]
+ -[CSSiriAudioPlaybackSessionImplAVAudioPlayerBased updateVolume:fadeDuration:completion:]
+ -[CSSiriAudioPlaybackSessionImplAVPlayerBased updateVolume:fadeDuration:completion:]
+ -[CSSiriSpeechRecordingContext shouldUseLocalFileWriter]
+ -[CSSpeechController setIsStoppingWithHTTMode:]
+ -[CSVoiceTriggerFileLogger _geckoLoggingMode]
+ -[CSVoiceTriggerFileLogger _shouldLogGeckoEvent:]
+ -[CSVoiceTriggerFileLogger _shouldSyncToCompanion]
+ -[CSVoiceTriggerFileLogger initWithSpeechManager:fileLoggingEnabled:]
+ GCC_except_table1534
+ GCC_except_table1558
+ GCC_except_table1562
+ GCC_except_table1578
+ GCC_except_table1581
+ GCC_except_table1610
+ GCC_except_table1708
+ GCC_except_table1710
+ GCC_except_table1712
+ GCC_except_table1718
+ GCC_except_table1778
+ GCC_except_table1804
+ GCC_except_table1810
+ GCC_except_table1891
+ GCC_except_table1911
+ GCC_except_table2027
+ GCC_except_table2175
+ GCC_except_table2205
+ GCC_except_table2208
+ GCC_except_table2211
+ GCC_except_table2216
+ GCC_except_table2228
+ GCC_except_table2233
+ GCC_except_table2236
+ GCC_except_table2353
+ GCC_except_table2356
+ GCC_except_table2360
+ GCC_except_table2378
+ GCC_except_table2509
+ GCC_except_table2566
+ GCC_except_table2578
+ GCC_except_table2609
+ GCC_except_table2634
+ GCC_except_table2645
+ GCC_except_table2683
+ GCC_except_table2687
+ GCC_except_table2690
+ GCC_except_table2694
+ GCC_except_table2786
+ GCC_except_table3052
+ GCC_except_table3130
+ GCC_except_table3167
+ GCC_except_table3178
+ GCC_except_table3200
+ GCC_except_table3203
+ GCC_except_table3206
+ GCC_except_table3237
+ GCC_except_table3297
+ GCC_except_table3503
+ GCC_except_table3529
+ GCC_except_table3590
+ GCC_except_table3591
+ GCC_except_table3593
+ GCC_except_table3595
+ GCC_except_table3611
+ GCC_except_table3613
+ GCC_except_table3615
+ GCC_except_table3619
+ GCC_except_table3621
+ GCC_except_table3623
+ GCC_except_table3626
+ GCC_except_table3637
+ GCC_except_table3643
+ GCC_except_table3653
+ GCC_except_table3664
+ GCC_except_table3665
+ GCC_except_table3666
+ GCC_except_table3667
+ GCC_except_table3668
+ GCC_except_table3669
+ GCC_except_table3672
+ GCC_except_table3680
+ GCC_except_table3685
+ GCC_except_table3686
+ GCC_except_table3687
+ GCC_except_table3688
+ GCC_except_table3823
+ GCC_except_table3847
+ GCC_except_table3913
+ GCC_except_table3929
+ GCC_except_table3950
+ GCC_except_table4042
+ GCC_except_table4290
+ GCC_except_table4357
+ GCC_except_table4358
+ GCC_except_table4362
+ GCC_except_table4365
+ GCC_except_table4369
+ GCC_except_table4394
+ GCC_except_table4444
+ GCC_except_table4450
+ GCC_except_table4718
+ GCC_except_table4725
+ GCC_except_table4732
+ GCC_except_table4738
+ GCC_except_table4818
+ GCC_except_table4979
+ GCC_except_table4989
+ GCC_except_table5013
+ GCC_except_table5033
+ GCC_except_table5116
+ GCC_except_table5130
+ GCC_except_table5146
+ GCC_except_table5154
+ GCC_except_table5157
+ GCC_except_table5165
+ GCC_except_table5167
+ GCC_except_table5172
+ GCC_except_table5174
+ GCC_except_table5185
+ GCC_except_table5191
+ GCC_except_table5202
+ GCC_except_table5206
+ GCC_except_table5208
+ GCC_except_table5209
+ GCC_except_table5210
+ GCC_except_table5211
+ GCC_except_table5213
+ GCC_except_table5214
+ GCC_except_table5215
+ GCC_except_table5216
+ GCC_except_table5217
+ GCC_except_table5219
+ GCC_except_table5220
+ GCC_except_table5221
+ GCC_except_table5223
+ GCC_except_table5238
+ GCC_except_table5312
+ GCC_except_table5316
+ GCC_except_table5370
+ GCC_except_table5400
+ GCC_except_table5403
+ GCC_except_table5483
+ GCC_except_table5497
+ GCC_except_table5504
+ GCC_except_table5516
+ GCC_except_table5520
+ GCC_except_table5530
+ GCC_except_table5759
+ GCC_except_table5790
+ GCC_except_table5795
+ GCC_except_table5832
+ GCC_except_table5841
+ GCC_except_table5871
+ GCC_except_table5939
+ GCC_except_table6129
+ GCC_except_table6157
+ GCC_except_table6162
+ GCC_except_table6268
+ GCC_except_table6323
+ GCC_except_table6414
+ GCC_except_table6415
+ GCC_except_table6425
+ GCC_except_table6426
+ GCC_except_table6438
+ GCC_except_table6469
+ GCC_except_table6480
+ GCC_except_table6485
+ GCC_except_table6490
+ GCC_except_table6518
+ GCC_except_table6590
+ GCC_except_table6602
+ GCC_except_table6625
+ GCC_except_table6636
+ GCC_except_table6639
+ GCC_except_table6662
+ GCC_except_table6674
+ GCC_except_table6953
+ GCC_except_table6988
+ GCC_except_table7061
+ GCC_except_table7115
+ GCC_except_table7138
+ GCC_except_table7179
+ GCC_except_table7190
+ GCC_except_table7330
+ GCC_except_table7338
+ GCC_except_table7452
+ GCC_except_table7453
+ GCC_except_table7454
+ GCC_except_table7455
+ GCC_except_table7456
+ GCC_except_table7461
+ GCC_except_table7524
+ GCC_except_table7570
+ GCC_except_table7578
+ GCC_except_table7584
+ GCC_except_table7609
+ GCC_except_table7615
+ GCC_except_table7621
+ GCC_except_table7761
+ _MACancelDownloadErrorDomain_block_invoke.enableHeartbeat
+ _MACancelDownloadErrorDomain_block_invoke.enableHeartbeat.10045
+ _MACancelDownloadErrorDomain_block_invoke.heartbeat
+ _MobileTimerLibrary.656
+ _MobileTimerLibraryCore.frameworkLibrary.660
+ _NSCocoaErrorDomain
+ _OBJC_CLASS_$_CSFAudioConverter
+ _OBJC_CLASS_$_CSFTTRAudioLogger
+ _OBJC_CLASS_$_CSOEPEntitledAssetManager
+ _OBJC_CLASS_$_SSREnrollmentHealthStore
+ _OBJC_IVAR_$_CSAttendingOptions._startAttendingSampleCount
+ _OBJC_IVAR_$_CSConnectionListener._delegate
+ _OBJC_IVAR_$_CSEndpointerAssetManager._oepEntitledAssetManager
+ __OBJC_$_CLASS_METHODS_CSVoiceTriggerFileLogger
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFAudioConverterDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AFAudioPlaybackService
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriAudioPlaybackSession
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSFAudioConverterDelegate
+ __OBJC_$_PROTOCOL_REFS_CSFAudioConverterDelegate
+ __OBJC_LABEL_PROTOCOL_$_CSFAudioConverterDelegate
+ __OBJC_PROTOCOL_$_CSFAudioConverterDelegate
+ __ZNKSt3__111__copy_implclB9foe210106IPNS_6vectorINS2_IfNS_9allocatorIfEEEENS3_IS5_EEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
+ __ZNKSt3__111__copy_implclB9foe210106IPNS_6vectorIfNS_9allocatorIfEEEES6_S6_EENS_4pairIT_T1_EES8_T0_S9_
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt12out_of_rangeC1B9foe210106EPKc
+ __ZNSt3__110unique_ptrI15SmartSiriVolumeNS_14default_deleteIS1_EEE5resetB9foe210106EPS1_
+ __ZNSt3__110unique_ptrIN10corespeech25CSAudioCircularBufferImplIhEENS_14default_deleteIS3_EEE5resetB9foe210106EPS3_
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorINS_4pairIfjEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__120__throw_out_of_rangeB9foe210106EPKc
+ __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B9foe210106Ev
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__135__uninitialized_allocator_copy_implB9foe210106INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__135__uninitialized_allocator_copy_implB9foe210106INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB9foe210106Ev
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB9foe210106IPS5_S9_EEvT_T0_m
+ __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB9foe210106Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB9foe210106IPS3_S7_EEvT_T0_m
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB9foe210106IPS3_S7_EEvT_T0_l
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE5clearB9foe210106Ev
+ __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEEC2B9foe210106EmRKS3_
+ __ZNSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE5eraseENS_11__wrap_iterIPKS2_EES9_
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB9foe210106Em
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB9foe210106IPfS5_EEvT_T0_m
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB9foe210106IPfS5_EEvT_T0_l
+ __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B9foe210106EmRKf
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB9foe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___100-[CSRemoteControlClient _fetchDataFromAudioFileUrl:aesKey:encryptedAudioSampleBypeDepth:completion:]_block_invoke.654
+ ___102-[CSEndpointerXPCClient resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.25
+ ___102-[CoreSpeechXPC voiceTriggerRTModelWithRequestOptions:downloadedModels:preinstalledModels:completion:]_block_invoke.350
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.485
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.489
+ ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.492
+ ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.417
+ ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.419
+ ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.421
+ ___108-[CSSiriAudioPlaybackService _startRequest:options:preparationHandler:executionHandler:finalizationHandler:]_block_invoke.16
+ ___108-[CSSiriAudioPlaybackService _startRequest:options:preparationHandler:executionHandler:finalizationHandler:]_block_invoke_2.17
+ ___108-[CSSiriAudioPlaybackService _startRequest:options:preparationHandler:executionHandler:finalizationHandler:]_block_invoke_3.18
+ ___109-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:bundleIdentifier:completion:]_block_invoke.342
+ ___109-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:bundleIdentifier:completion:]_block_invoke.344
+ ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.188
+ ___110-[CSVoiceTriggerSecondPass _requestStartAudioStreamWitContext:audioProviderUUID:startStreamOption:completion:]_block_invoke.394
+ ___112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.461
+ ___113-[CSVoiceTriggerFirstPassJarvis _handleJarvisVoiceTriggerFromDeviceId:activationInfo:triggerHostTime:completion:]_block_invoke.359
+ ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.436
+ ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.447
+ ___118-[CSSiriAudioPlaybackService _startHapticOnlyRequest:options:preparationHandler:executionHandler:finalizationHandler:]_block_invoke.15
+ ___125-[CSRemoteControlClient createRemoteVoiceProfileWithAudioFiles:aesKey:encryptedAudioSampleBypeDepth:languageCode:completion:]_block_invoke.628
+ ___125-[CSRemoteControlClient createRemoteVoiceProfileWithAudioFiles:aesKey:encryptedAudioSampleBypeDepth:languageCode:completion:]_block_invoke.632
+ ___133-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.439
+ ___136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.428
+ ___136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.429
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.192
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.193
+ ___22-[CSXPCClient connect]_block_invoke.12
+ ___30-[CSBuiltInVoiceTrigger start]_block_invoke.364
+ ___30-[CSBuiltInVoiceTrigger start]_block_invoke.375
+ ___30-[CSBuiltInVoiceTrigger start]_block_invoke_2.378
+ ___35-[CSBuiltInVoiceTrigger _setAsset:]_block_invoke.404
+ ___39-[CSBuiltInVoiceTrigger _stopListening]_block_invoke.430
+ ___41-[CSAssetManager initWithDownloadOption:]_block_invoke.349
+ ___41-[CSAssetManager initWithDownloadOption:]_block_invoke.351
+ ___42-[CSFileAudioInjectionBuiltInEngine start]_block_invoke.350
+ ___42-[CSRemoteControlClient didDeviceConnect:]_block_invoke.403
+ ___44-[CSBuiltInVoiceTrigger _stopAPVoiceTrigger]_block_invoke.438
+ ___46-[CSHybridEndpointAnalyzer processTaskString:]_block_invoke.445
+ ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.162
+ ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.143
+ ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.144
+ ___48-[CSSpeechController CSXPCClient:didDisconnect:]_block_invoke.706
+ ___48-[CSXPCClient triggerInfoForContext:completion:]_block_invoke.54
+ ___49-[CSAssetController _downloadAsset:withComplete:]_block_invoke.378
+ ___49-[CSVoiceTriggerFirstPassHearstAP _stopListening]_block_invoke.360
+ ___49-[CSVoiceTriggerFirstPassJarvisAP _stopListening]_block_invoke.354
+ ___50-[CSEndpointerXPCClient setIsStoppingWithHTTMode:]_block_invoke
+ ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.254
+ ___50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.396
+ ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.425
+ ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke_2.426
+ ___52-[CSSelfTriggerDetector _startListenWithCompletion:]_block_invoke.351
+ ___52-[CSSiriAudioPlaybackService _playHapticForRequest:]_block_invoke.11
+ ___52-[CSSpeechController setCurrentRecordContext:error:]_block_invoke.582
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.373
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.377
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.378
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.382
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.389
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.390
+ ___52-[CSVoiceTriggerAssetHandlerMac triggerAssetRefresh]_block_invoke.350
+ ___53-[CSRemoteControlClient _transferFile:at:completion:]_block_invoke.488
+ ___53-[CSRemoteControlClient _transferFile:at:completion:]_block_invoke.489
+ ___53-[CSXPCClient acousticSLResultForContext:completion:]_block_invoke.50
+ ___54-[CSAssetController fetchRemoteMetaOfType:allowRetry:]_block_invoke.366
+ ___54-[CSAttSiriMitigationAssetHandler triggerAssetRefresh]_block_invoke.359
+ ___54-[CSSelfTriggerDetector _stopListeningWithCompletion:]_block_invoke.352
+ ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.557
+ ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.566
+ ___55-[CSSiriAudioPlaybackService _injectSessionsByRequest:]_block_invoke
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.612
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.620
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke_2.621
+ ___56-[CSConnectionListener notifyRemoteParameter:WithBlock:]_block_invoke
+ ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.264
+ ___58-[CSRemoteControlClient exchangeRemoteDeviceProtocolInfo:]_block_invoke.613
+ ___59-[CSConnectionListener listener:shouldAcceptNewConnection:]_block_invoke.10
+ ___59-[CSConnectionListener listener:shouldAcceptNewConnection:]_block_invoke.12
+ ___60-[CSSpeechController handleStopRecordingRequestWithOptions:]_block_invoke.634
+ ___60-[CSXPCClient audioStreamWithRequest:streamName:completion:]_block_invoke.46
+ ___61-[CSModelBenchmarker _setupAudioInjectionEngineWithAudioURL:]_block_invoke.371
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.389
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.390
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.392
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.393
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.398
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.401
+ ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2.399
+ ___62-[CSRemoraEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke.384
+ ___62-[CSVoiceTriggerFirstPassJarvisAP _startListenWithCompletion:]_block_invoke.352
+ ___64-[CSEndpointerAssetManager _registerForAssetUpdateNotifications]_block_invoke.358
+ ___64-[CSSmartSiriVolume _startListenPollingWithInterval:completion:]_block_invoke.388
+ ___64-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke.559
+ ___65-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke.346
+ ___67-[CSSmartSiriVolume startSmartSiriVolumeWithAudioProviderSelector:]_block_invoke.383
+ ___68-[CSBuiltInVoiceTrigger _startListenPollingWithInterval:completion:]_block_invoke.420
+ ___68-[CSSelfTriggerDetector _startListenPollingWithInterval:completion:]_block_invoke.341
+ ___68-[CSTrialAssetDownloadMonitor _validateDownloadedAssetForAssetType:]_block_invoke.379
+ ___68-[CSTrialAssetDownloadMonitor _validateDownloadedAssetForAssetType:]_block_invoke.380
+ ___68-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke.430
+ ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.265
+ ___72-[CSVoiceTriggerFirstPassJarvis _handleSecondPassResult:deviceId:error:]_block_invoke.378
+ ___72-[CSVoiceTriggerFirstPassJarvis _handleSecondPassResult:deviceId:error:]_block_invoke.379
+ ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.253
+ ___75-[CSSiriAudioPlaybackService updateRequest:volume:fadeDuration:completion:]_block_invoke
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.450
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.451
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.452
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.454
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.455
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.458
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.463
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.467
+ ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2.456
+ ___77-[CSBuiltInVoiceTrigger activationEventNotificationHandler:event:completion:]_block_invoke.478
+ ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.117
+ ___77-[CSSpeechManager CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke.415
+ ___78-[CSRemoteControlClient transferVoiceTriggerAsset:forLanguageCode:completion:]_block_invoke.524
+ ___79-[CSVoiceProfileRetrainManager CSVoiceTriggerEnabledMonitor:didReceiveEnabled:]_block_invoke.346
+ ___80-[CSVoiceTriggerFirstPassHearstAP _startListenWithAudioProviderUUID:completion:]_block_invoke.356
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.568
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.569
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.570
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.578
+ ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.409
+ ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.416
+ ___82-[CoreSpeechXPC voiceTriggerJarvisLanguageList:jarvisSelectedLanguage:completion:]_block_invoke.354
+ ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.208
+ ___85-[CSRemoteControlClient transferInterstitialAudioFiles:interstitialLevel:completion:]_block_invoke.576
+ ___85-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:]_block_invoke.234
+ ___85-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]_block_invoke.358
+ ___85-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]_block_invoke.360
+ ___85-[CSVoiceTriggerFirstPassRemora activationEventNotificationHandler:event:completion:]_block_invoke.448
+ ___85-[CSVoiceTriggerFirstPassRemora activationEventNotificationHandler:event:completion:]_block_invoke.450
+ ___87-[CSVoiceProfileRetrainManager _retrainingVoiceProfile:voiceProfile:asset:secureAsset:]_block_invoke.364
+ ___87-[CSVoiceTriggerFirstPassHearstAP _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:]_block_invoke.374
+ ___88-[CSVoiceTriggerFirstPassRemora _handleRemoraTriggerEvent:secondPassRequest:completion:]_block_invoke.459
+ ___93-[CSFileAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]_block_invoke.350
+ ___93-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromAOP:audioProviderUUID:completion:]_block_invoke.443
+ ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.423
+ ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.431
+ ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke_2.433
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.220
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.221
+ ___97-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:]_block_invoke.400
+ ___Block_byref_object_copy_.10833
+ ___Block_byref_object_copy_.12127
+ ___Block_byref_object_copy_.12531
+ ___Block_byref_object_copy_.1339
+ ___Block_byref_object_copy_.13557
+ ___Block_byref_object_copy_.13886
+ ___Block_byref_object_copy_.14702
+ ___Block_byref_object_copy_.14820
+ ___Block_byref_object_copy_.1580
+ ___Block_byref_object_copy_.16394
+ ___Block_byref_object_copy_.16727
+ ___Block_byref_object_copy_.17885
+ ___Block_byref_object_copy_.19021
+ ___Block_byref_object_copy_.19661
+ ___Block_byref_object_copy_.2024
+ ___Block_byref_object_copy_.20275
+ ___Block_byref_object_copy_.20507
+ ___Block_byref_object_copy_.21066
+ ___Block_byref_object_copy_.21638
+ ___Block_byref_object_copy_.21904
+ ___Block_byref_object_copy_.22655
+ ___Block_byref_object_copy_.23453
+ ___Block_byref_object_copy_.23973
+ ___Block_byref_object_copy_.2417
+ ___Block_byref_object_copy_.24788
+ ___Block_byref_object_copy_.25077
+ ___Block_byref_object_copy_.25891
+ ___Block_byref_object_copy_.3288
+ ___Block_byref_object_copy_.3415
+ ___Block_byref_object_copy_.3502
+ ___Block_byref_object_copy_.4067
+ ___Block_byref_object_copy_.5775
+ ___Block_byref_object_copy_.6652
+ ___Block_byref_object_copy_.68
+ ___Block_byref_object_copy_.7671
+ ___Block_byref_object_copy_.8195
+ ___Block_byref_object_copy_.9244
+ ___Block_byref_object_copy_.9684
+ ___Block_byref_object_dispose_.10834
+ ___Block_byref_object_dispose_.12128
+ ___Block_byref_object_dispose_.12532
+ ___Block_byref_object_dispose_.1340
+ ___Block_byref_object_dispose_.13558
+ ___Block_byref_object_dispose_.13887
+ ___Block_byref_object_dispose_.14703
+ ___Block_byref_object_dispose_.14821
+ ___Block_byref_object_dispose_.1581
+ ___Block_byref_object_dispose_.16395
+ ___Block_byref_object_dispose_.16728
+ ___Block_byref_object_dispose_.17886
+ ___Block_byref_object_dispose_.19022
+ ___Block_byref_object_dispose_.19662
+ ___Block_byref_object_dispose_.2025
+ ___Block_byref_object_dispose_.20276
+ ___Block_byref_object_dispose_.20508
+ ___Block_byref_object_dispose_.21067
+ ___Block_byref_object_dispose_.21639
+ ___Block_byref_object_dispose_.21905
+ ___Block_byref_object_dispose_.22656
+ ___Block_byref_object_dispose_.23454
+ ___Block_byref_object_dispose_.23974
+ ___Block_byref_object_dispose_.2418
+ ___Block_byref_object_dispose_.24789
+ ___Block_byref_object_dispose_.25078
+ ___Block_byref_object_dispose_.25892
+ ___Block_byref_object_dispose_.3289
+ ___Block_byref_object_dispose_.3416
+ ___Block_byref_object_dispose_.3503
+ ___Block_byref_object_dispose_.4068
+ ___Block_byref_object_dispose_.5776
+ ___Block_byref_object_dispose_.6653
+ ___Block_byref_object_dispose_.69
+ ___Block_byref_object_dispose_.7672
+ ___Block_byref_object_dispose_.8196
+ ___Block_byref_object_dispose_.9245
+ ___Block_byref_object_dispose_.9685
+ ___MobileTimerLibraryCore_block_invoke.661
+ ___block_descriptor_32_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
+ ___block_descriptor_66_e8_32s40s48s56s_e24_v24?0"NSURL"8?<v?>16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_68_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.10.18415
+ ___block_literal_global.10.19958
+ ___block_literal_global.10.20942
+ ___block_literal_global.10.9829
+ ___block_literal_global.10049
+ ___block_literal_global.1005
+ ___block_literal_global.10251
+ ___block_literal_global.10659
+ ___block_literal_global.10871
+ ___block_literal_global.11.11127
+ ___block_literal_global.11137
+ ___block_literal_global.11237
+ ___block_literal_global.11359
+ ___block_literal_global.115
+ ___block_literal_global.11660
+ ___block_literal_global.11766
+ ___block_literal_global.11819
+ ___block_literal_global.11874
+ ___block_literal_global.120
+ ___block_literal_global.1220
+ ___block_literal_global.12320
+ ___block_literal_global.12436
+ ___block_literal_global.12652
+ ___block_literal_global.13.19959
+ ___block_literal_global.13.20105
+ ___block_literal_global.13.20943
+ ___block_literal_global.13038
+ ___block_literal_global.13393
+ ___block_literal_global.13450
+ ___block_literal_global.13634
+ ___block_literal_global.13652
+ ___block_literal_global.13760
+ ___block_literal_global.14.20030
+ ___block_literal_global.1425
+ ___block_literal_global.14312
+ ___block_literal_global.14397
+ ___block_literal_global.14807
+ ___block_literal_global.14849
+ ___block_literal_global.151
+ ___block_literal_global.15456
+ ___block_literal_global.15924
+ ___block_literal_global.15933
+ ___block_literal_global.15979
+ ___block_literal_global.16.11117
+ ___block_literal_global.16.12321
+ ___block_literal_global.16.13451
+ ___block_literal_global.16.19960
+ ___block_literal_global.16013
+ ___block_literal_global.161
+ ___block_literal_global.16264
+ ___block_literal_global.16340
+ ___block_literal_global.16448
+ ___block_literal_global.16982
+ ___block_literal_global.17.13394
+ ___block_literal_global.17.20031
+ ___block_literal_global.17051
+ ___block_literal_global.17081
+ ___block_literal_global.17618
+ ___block_literal_global.17910
+ ___block_literal_global.18.20106
+ ___block_literal_global.18217
+ ___block_literal_global.18298
+ ___block_literal_global.18432
+ ___block_literal_global.18546
+ ___block_literal_global.18591
+ ___block_literal_global.18607
+ ___block_literal_global.1879
+ ___block_literal_global.18885
+ ___block_literal_global.18937
+ ___block_literal_global.19043
+ ___block_literal_global.19121
+ ___block_literal_global.19319
+ ___block_literal_global.19645
+ ___block_literal_global.19944
+ ___block_literal_global.19957
+ ___block_literal_global.20.12298
+ ___block_literal_global.20.13395
+ ___block_literal_global.20.20032
+ ___block_literal_global.20029
+ ___block_literal_global.20125
+ ___block_literal_global.20175
+ ___block_literal_global.20218
+ ___block_literal_global.20337
+ ___block_literal_global.2044
+ ___block_literal_global.20940
+ ___block_literal_global.21.11767
+ ___block_literal_global.21410
+ ___block_literal_global.21520
+ ___block_literal_global.2155
+ ___block_literal_global.21669
+ ___block_literal_global.22.19961
+ ___block_literal_global.22.23956
+ ___block_literal_global.22239
+ ___block_literal_global.22453
+ ___block_literal_global.22535
+ ___block_literal_global.2256
+ ___block_literal_global.2270
+ ___block_literal_global.22908
+ ___block_literal_global.23.20033
+ ___block_literal_global.23683
+ ___block_literal_global.24002
+ ___block_literal_global.243
+ ___block_literal_global.24309
+ ___block_literal_global.24596
+ ___block_literal_global.24645
+ ___block_literal_global.24823
+ ___block_literal_global.24926
+ ___block_literal_global.2499
+ ___block_literal_global.25.19962
+ ___block_literal_global.25013
+ ___block_literal_global.25146
+ ___block_literal_global.2559
+ ___block_literal_global.25688
+ ___block_literal_global.25902
+ ___block_literal_global.26176
+ ___block_literal_global.2650
+ ___block_literal_global.27.11768
+ ___block_literal_global.28.23945
+ ___block_literal_global.2823
+ ___block_literal_global.29.19963
+ ___block_literal_global.29.20034
+ ___block_literal_global.30.11769
+ ___block_literal_global.30.12283
+ ___block_literal_global.3026
+ ___block_literal_global.317
+ ___block_literal_global.3181
+ ___block_literal_global.330
+ ___block_literal_global.3333
+ ___block_literal_global.336
+ ___block_literal_global.336.24818
+ ___block_literal_global.340
+ ___block_literal_global.3406
+ ___block_literal_global.346
+ ___block_literal_global.348
+ ___block_literal_global.350
+ ___block_literal_global.351
+ ___block_literal_global.352
+ ___block_literal_global.3537
+ ___block_literal_global.354
+ ___block_literal_global.354.10845
+ ___block_literal_global.36.11770
+ ___block_literal_global.367
+ ___block_literal_global.370
+ ___block_literal_global.377
+ ___block_literal_global.38.8347
+ ___block_literal_global.380
+ ___block_literal_global.392
+ ___block_literal_global.392.5791
+ ___block_literal_global.393
+ ___block_literal_global.41
+ ___block_literal_global.414
+ ___block_literal_global.417
+ ___block_literal_global.42.11771
+ ___block_literal_global.432
+ ___block_literal_global.4488
+ ___block_literal_global.46.8339
+ ___block_literal_global.5.26177
+ ___block_literal_global.5060
+ ___block_literal_global.5170
+ ___block_literal_global.529
+ ___block_literal_global.5353
+ ___block_literal_global.544
+ ___block_literal_global.5455
+ ___block_literal_global.5478
+ ___block_literal_global.572
+ ___block_literal_global.5825
+ ___block_literal_global.5958
+ ___block_literal_global.60
+ ___block_literal_global.619
+ ___block_literal_global.6225
+ ___block_literal_global.677
+ ___block_literal_global.682
+ ___block_literal_global.7.20941
+ ___block_literal_global.7.670
+ ___block_literal_global.7788
+ ___block_literal_global.784
+ ___block_literal_global.8.24920
+ ___block_literal_global.8.25147
+ ___block_literal_global.8.26178
+ ___block_literal_global.8376
+ ___block_literal_global.8428
+ ___block_literal_global.8540
+ ___block_literal_global.858
+ ___block_literal_global.8931
+ ___block_literal_global.9339
+ ___block_literal_global.9484
+ ___block_literal_global.9698
+ ___block_literal_global.9855
+ __compensateChannelDataIfNeeded:receivedNumChannels:.heartbeat.13546
+ __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.17552
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10032
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.17543
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.25379
+ _audit_stringMobileTimer.664
+ _objc_msgSend$_geckoLoggingMode
+ _objc_msgSend$_getOEPAssetWithLanguage:withOEPEntitledAssetManager:
+ _objc_msgSend$_hasHearstRoutedAndNotInSplitterOrJarvisRouted
+ _objc_msgSend$_notifyDelegateOfNewConnection:
+ _objc_msgSend$_notifyDelegateOfRemovedConnection:
+ _objc_msgSend$_resetAndGetOEPAssetsWithLanguage:
+ _objc_msgSend$_shouldLogGeckoEvent:
+ _objc_msgSend$_shouldSyncToCompanion
+ _objc_msgSend$_updateRequest:volume:fadeDuration:completion:
+ _objc_msgSend$assetForAssetType:resourcePath:configVersion:assetProvider:assetVariant:identity:assistantLanguageCode:uafAssetVersion:oepEntitledAssetManager:
+ _objc_msgSend$assetVersion
+ _objc_msgSend$cleanupOrphanedFilesInDirectory:matchingPattern:
+ _objc_msgSend$clearLogFilesInDirectory:matchingPattern:exceedNumber:
+ _objc_msgSend$connectionListener:didAddConnection:
+ _objc_msgSend$connectionListener:didRemoveConnection:
+ _objc_msgSend$initWithAttendingType:startAttendingHostTime:startAttendingSampleCount:useVAD:useOwnVoiceVAD:useBoron:startOfSpeechThresholdInMs:prependAudioDuration:timeoutThresholdInSec:triggerType:audioStreamHoldingDurationInSec:audioRecordType:deviceId:attendingListeningType:pauseDurationThreshold:maxPauseDelay:
+ _objc_msgSend$initWithConfigFile:sampleRate:context:queue:delegate:osdAnalyzerAssetLocker:
+ _objc_msgSend$initWithLocaleIdentifier:
+ _objc_msgSend$initWithSpeechManager:fileLoggingEnabled:
+ _objc_msgSend$initWithXpcListener:withMachService:withServiceInterface:withServiceObject:withDelegateInterface:queue:delegate:
+ _objc_msgSend$installedAssetPath
+ _objc_msgSend$oepEntitledAssetManager
+ _objc_msgSend$onDeviceSMREnabled
+ _objc_msgSend$onDeviceSMRLogRetentionPeriodInDays
+ _objc_msgSend$onDeviceSMRMaxNumLogFiles
+ _objc_msgSend$optionForFlexibleFollowupWithAudioRecordType:deviceId:startAttendingSampleCount:
+ _objc_msgSend$pruneOnDeviceSMRAudioLogs
+ _objc_msgSend$recordedAudioAvailableAt:requestId:filenamePostfix:
+ _objc_msgSend$rootQueueWithFixedPriority:label:
+ _objc_msgSend$setIsStoppingWithHTTMode:
+ _objc_msgSend$shouldUseLocalFileWriter
+ _objc_msgSend$startAttendingSampleCount
+ _objc_msgSend$ttrAudioLoggingEnabled
+ _objc_msgSend$updateEnrollmentHealthForVoiceProfile:asset:completionHandler:
+ _objc_msgSend$updateVolume:fadeDuration:completion:
+ _sharedController.onceToken.10870
+ _sharedController.sharedController.10872
+ _sharedHandler.onceToken.18216
+ _sharedHandler.onceToken.24822
+ _sharedHandler.onceToken.857
+ _sharedHandler.sharedHandler.18218
+ _sharedHandler.sharedHandler.24824
+ _sharedHandler.sharedHandler.859
+ _sharedHandlerDisabledOnDeviceCompilation.onceToken.24817
+ _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.24819
+ _sharedInstance._sharedInstance.10660
+ _sharedInstance._sharedInstance.11875
+ _sharedInstance._sharedInstance.13761
+ _sharedInstance._sharedInstance.15980
+ _sharedInstance._sharedInstance.16265
+ _sharedInstance._sharedInstance.16341
+ _sharedInstance._sharedInstance.17052
+ _sharedInstance._sharedInstance.18547
+ _sharedInstance._sharedInstance.18886
+ _sharedInstance._sharedInstance.18938
+ _sharedInstance._sharedInstance.19122
+ _sharedInstance._sharedInstance.22240
+ _sharedInstance._sharedInstance.22909
+ _sharedInstance._sharedInstance.24646
+ _sharedInstance._sharedInstance.2500
+ _sharedInstance._sharedInstance.2560
+ _sharedInstance._sharedInstance.25903
+ _sharedInstance._sharedInstance.2824
+ _sharedInstance._sharedInstance.5061
+ _sharedInstance._sharedInstance.5171
+ _sharedInstance._sharedInstance.530
+ _sharedInstance._sharedInstance.5456
+ _sharedInstance._sharedInstance.5959
+ _sharedInstance._sharedInstance.620
+ _sharedInstance._sharedInstance.683
+ _sharedInstance._sharedInstance.8429
+ _sharedInstance.onceToken.1004
+ _sharedInstance.onceToken.10658
+ _sharedInstance.onceToken.11818
+ _sharedInstance.onceToken.11873
+ _sharedInstance.onceToken.1219
+ _sharedInstance.onceToken.12435
+ _sharedInstance.onceToken.13759
+ _sharedInstance.onceToken.14311
+ _sharedInstance.onceToken.14396
+ _sharedInstance.onceToken.14806
+ _sharedInstance.onceToken.150
+ _sharedInstance.onceToken.15978
+ _sharedInstance.onceToken.16263
+ _sharedInstance.onceToken.16339
+ _sharedInstance.onceToken.16447
+ _sharedInstance.onceToken.16981
+ _sharedInstance.onceToken.17050
+ _sharedInstance.onceToken.17080
+ _sharedInstance.onceToken.18431
+ _sharedInstance.onceToken.18545
+ _sharedInstance.onceToken.18884
+ _sharedInstance.onceToken.18936
+ _sharedInstance.onceToken.19120
+ _sharedInstance.onceToken.19943
+ _sharedInstance.onceToken.20124
+ _sharedInstance.onceToken.20217
+ _sharedInstance.onceToken.20336
+ _sharedInstance.onceToken.21409
+ _sharedInstance.onceToken.21519
+ _sharedInstance.onceToken.21668
+ _sharedInstance.onceToken.22238
+ _sharedInstance.onceToken.22534
+ _sharedInstance.onceToken.22907
+ _sharedInstance.onceToken.24308
+ _sharedInstance.onceToken.24644
+ _sharedInstance.onceToken.2498
+ _sharedInstance.onceToken.2558
+ _sharedInstance.onceToken.25687
+ _sharedInstance.onceToken.25901
+ _sharedInstance.onceToken.2649
+ _sharedInstance.onceToken.2822
+ _sharedInstance.onceToken.3180
+ _sharedInstance.onceToken.391
+ _sharedInstance.onceToken.40
+ _sharedInstance.onceToken.4487
+ _sharedInstance.onceToken.5059
+ _sharedInstance.onceToken.5169
+ _sharedInstance.onceToken.528
+ _sharedInstance.onceToken.5454
+ _sharedInstance.onceToken.5957
+ _sharedInstance.onceToken.618
+ _sharedInstance.onceToken.681
+ _sharedInstance.onceToken.8427
+ _sharedInstance.onceToken.9483
+ _sharedInstance.onceToken.9697
+ _sharedInstance.onceToken.9854
+ _sharedInstance.sSharedInstance.17082
+ _sharedInstance.sharedInstance.11820
+ _sharedInstance.sharedInstance.12437
+ _sharedInstance.sharedInstance.14398
+ _sharedInstance.sharedInstance.16983
+ _sharedInstance.sharedInstance.18433
+ _sharedInstance.sharedInstance.19945
+ _sharedInstance.sharedInstance.20219
+ _sharedInstance.sharedInstance.21521
+ _sharedInstance.sharedInstance.21670
+ _sharedInstance.sharedInstance.25689
+ _sharedInstance.sharedInstance.3182
+ _sharedInstance.sharedInstance.4489
+ _sharedInstance.sharedManager.24310
+ _sharedInstance.sharedPolicy.1006
+ _sharedInstance.sharedPolicy.20126
+ _sharedInstance.sharedPolicy.22536
+ _sharedInstance.sharedProvider.21411
+ _sharedManager.onceToken.15923
+ _sharedManager.onceToken.17909
+ _sharedManager.onceToken.5824
+ _sharedManager.onceToken.6224
+ _sharedManager.sharedManager.15925
+ _sharedManager.sharedManager.5826
+ _sharedManager.sharedManager.6226
+ _sharedMonitor.onceToken.19042
+ _sharedMonitor.sharedMonitor.19044
+ _sharedService.onceToken.14848
+ _sharedService.onceToken.24001
+ _sharedService.sharedService.24003
- +[CSAudioConverter narrowBandOpusConverter]
- +[CSAudioConverter opusConverter]
- +[CSAudioConverter speexConverter]
- +[CSEndpointerAssetManager _getOEPAssetWithLanguage:]
- +[CSRecordTypeSpeechEventConverter getRecordTypeForSpeechEvent:]
- +[CSRecordTypeSpeechEventConverter getSpeechEventForRecordType:]
- -[CSAudioConverter .cxx_destruct]
- -[CSAudioConverter _configureAudioConverter:]
- -[CSAudioConverter _convertBufferedLPCM:allowPartial:timestamp:arrivalTimestampToAudioRecorder:]
- -[CSAudioConverter addSamples:timestamp:arrivalTimestampToAudioRecorder:]
- -[CSAudioConverter dealloc]
- -[CSAudioConverter delegate]
- -[CSAudioConverter flush]
- -[CSAudioConverter initWithInASBD:outASBD:]
- -[CSAudioConverter reset]
- -[CSAudioConverter setDelegate:]
- -[CSBuiltInVoiceTrigger _hasHearstRoutedAndNotInSplitter]
- -[CSSiriAudioMessageRequestClient .cxx_destruct]
- -[CSSiriAudioMessageRequestClient _connection]
- -[CSSiriAudioMessageRequestClient _newConnection]
- -[CSSiriAudioMessageRequestClient _service]
- -[CSSiriAudioMessageRequestClient dealloc]
- -[CSSiriAudioMessageRequestClient forceReleaseAllAudioMessageRetainLock]
- -[CSSiriAudioMessageRequestClient getAudioFileWithRequestId:completion:]
- -[CSSiriAudioMessageRequestClient init]
- -[CSSiriAudioMessageRequestClient queue]
- -[CSSiriAudioMessageRequestClient releaseAudioMessageRetainLockFromRequestId:]
- -[CSSiriAudioMessageRequestClient setQueue:]
- -[CSSiriAudioMessageRequestClient setXpcConnection:]
- -[CSSiriAudioMessageRequestClient setXpcConnectionUUIDString:]
- -[CSSiriAudioMessageRequestClient xpcConnectionUUIDString]
- -[CSSiriAudioMessageRequestClient xpcConnection]
- -[CSVoiceTriggerFileLogger _clearOldGeckoLoggingFiles]
- -[CSVoiceTriggerFileLogger geckoLoggingEnabled]
- -[CSVoiceTriggerFileLogger initWithSpeechManager:fileLoggingEnabled:geckoLoggingEnabled:]
- -[CSVoiceTriggerFileLogger setGeckoLoggingEnabled:]
- -[SSRDonationUtteranceData .cxx_destruct]
- -[SSRDonationUtteranceData donationId]
- -[SSRDonationUtteranceData initWithDonationInfoString:locale:]
- -[SSRDonationUtteranceData locale]
- -[SSRDonationUtteranceData triggerPhrase]
- -[SSREnrollmentSamplingMetaData .cxx_destruct]
- -[SSREnrollmentSamplingMetaData description]
- -[SSREnrollmentSamplingMetaData dictionaryRepresentation]
- -[SSREnrollmentSamplingMetaData initWithDictionary:]
- -[SSREnrollmentSamplingMetaData initWithSelectionStatus:voiceProfileId:]
- -[SSREnrollmentSamplingMetaData init]
- -[SSREnrollmentSamplingMetaData selectionStatus]
- -[SSREnrollmentSamplingMetaData voiceProfileId]
- GCC_except_table1533
- GCC_except_table1557
- GCC_except_table1561
- GCC_except_table1577
- GCC_except_table1580
- GCC_except_table1609
- GCC_except_table1707
- GCC_except_table1709
- GCC_except_table1711
- GCC_except_table1717
- GCC_except_table1777
- GCC_except_table1803
- GCC_except_table1809
- GCC_except_table1890
- GCC_except_table1910
- GCC_except_table2026
- GCC_except_table2174
- GCC_except_table2204
- GCC_except_table2207
- GCC_except_table2210
- GCC_except_table2215
- GCC_except_table2227
- GCC_except_table2232
- GCC_except_table2235
- GCC_except_table2352
- GCC_except_table2355
- GCC_except_table2359
- GCC_except_table2377
- GCC_except_table2510
- GCC_except_table2567
- GCC_except_table2579
- GCC_except_table2610
- GCC_except_table2633
- GCC_except_table2644
- GCC_except_table2678
- GCC_except_table2686
- GCC_except_table2689
- GCC_except_table2692
- GCC_except_table2783
- GCC_except_table3044
- GCC_except_table3122
- GCC_except_table3159
- GCC_except_table3170
- GCC_except_table3192
- GCC_except_table3195
- GCC_except_table3198
- GCC_except_table3229
- GCC_except_table3289
- GCC_except_table3494
- GCC_except_table3520
- GCC_except_table3581
- GCC_except_table3582
- GCC_except_table3584
- GCC_except_table3586
- GCC_except_table3602
- GCC_except_table3604
- GCC_except_table3606
- GCC_except_table3608
- GCC_except_table3610
- GCC_except_table3612
- GCC_except_table3614
- GCC_except_table3625
- GCC_except_table3628
- GCC_except_table3636
- GCC_except_table3638
- GCC_except_table3640
- GCC_except_table3642
- GCC_except_table3644
- GCC_except_table3646
- GCC_except_table3650
- GCC_except_table3657
- GCC_except_table3662
- GCC_except_table3676
- GCC_except_table3677
- GCC_except_table3678
- GCC_except_table3679
- GCC_except_table3814
- GCC_except_table3838
- GCC_except_table3904
- GCC_except_table3920
- GCC_except_table3941
- GCC_except_table4033
- GCC_except_table4281
- GCC_except_table4348
- GCC_except_table4349
- GCC_except_table4353
- GCC_except_table4356
- GCC_except_table4360
- GCC_except_table4385
- GCC_except_table4435
- GCC_except_table4441
- GCC_except_table4708
- GCC_except_table4715
- GCC_except_table4722
- GCC_except_table4728
- GCC_except_table4808
- GCC_except_table4964
- GCC_except_table4974
- GCC_except_table4998
- GCC_except_table5018
- GCC_except_table5101
- GCC_except_table5115
- GCC_except_table5124
- GCC_except_table5131
- GCC_except_table5137
- GCC_except_table5142
- GCC_except_table5150
- GCC_except_table5156
- GCC_except_table5158
- GCC_except_table5169
- GCC_except_table5170
- GCC_except_table5175
- GCC_except_table5181
- GCC_except_table5188
- GCC_except_table5190
- GCC_except_table5192
- GCC_except_table5193
- GCC_except_table5194
- GCC_except_table5195
- GCC_except_table5198
- GCC_except_table5199
- GCC_except_table5200
- GCC_except_table5201
- GCC_except_table5203
- GCC_except_table5205
- GCC_except_table5207
- GCC_except_table5222
- GCC_except_table5296
- GCC_except_table5300
- GCC_except_table5354
- GCC_except_table5383
- GCC_except_table5386
- GCC_except_table5466
- GCC_except_table5480
- GCC_except_table5487
- GCC_except_table5499
- GCC_except_table5503
- GCC_except_table5513
- GCC_except_table5742
- GCC_except_table5773
- GCC_except_table5778
- GCC_except_table5815
- GCC_except_table5824
- GCC_except_table5851
- GCC_except_table5919
- GCC_except_table6109
- GCC_except_table6117
- GCC_except_table6142
- GCC_except_table6248
- GCC_except_table6303
- GCC_except_table6394
- GCC_except_table6395
- GCC_except_table6405
- GCC_except_table6406
- GCC_except_table6418
- GCC_except_table6449
- GCC_except_table6460
- GCC_except_table6465
- GCC_except_table6470
- GCC_except_table6498
- GCC_except_table6583
- GCC_except_table6595
- GCC_except_table6618
- GCC_except_table6629
- GCC_except_table6632
- GCC_except_table6655
- GCC_except_table6667
- GCC_except_table6947
- GCC_except_table6982
- GCC_except_table7055
- GCC_except_table7109
- GCC_except_table7132
- GCC_except_table7173
- GCC_except_table7184
- GCC_except_table7324
- GCC_except_table7332
- GCC_except_table7438
- GCC_except_table7439
- GCC_except_table7440
- GCC_except_table7441
- GCC_except_table7442
- GCC_except_table7447
- GCC_except_table7510
- GCC_except_table7552
- GCC_except_table7577
- GCC_except_table7592
- GCC_except_table7600
- GCC_except_table7606
- GCC_except_table7631
- GCC_except_table7637
- GCC_except_table7643
- GCC_except_table7783
- _AudioConverterFillComplexBuffer_BlockInvoke.26298
- _AudioConverterGetProperty
- _AudioConverterReset
- _AudioConverterSetProperty
- _CSSiriAudioMessageRequestServiceName
- _CSSiriAudioMessageServiceGetXPCInterface
- _MobileTimerLibrary.803
- _MobileTimerLibraryCore.frameworkLibrary.808
- _NSFileProtectionCompleteUnlessOpen
- _OBJC_CLASS_$_CSAudioConverter
- _OBJC_CLASS_$_SFEntitledAssetConfig
- _OBJC_CLASS_$_SFEntitledAssetManager
- _OBJC_CLASS_$_SSRDonationUtteranceData
- _OBJC_CLASS_$_SSREnrollmentSamplingMetaData
- _OBJC_IVAR_$_CSAudioConverter._bufferedLPCM
- _OBJC_IVAR_$_CSAudioConverter._convertAudioCapacity
- _OBJC_IVAR_$_CSAudioConverter._convertPacketCount
- _OBJC_IVAR_$_CSAudioConverter._delegate
- _OBJC_IVAR_$_CSAudioConverter._lastArrivalTimestampToAudioRecorder
- _OBJC_IVAR_$_CSAudioConverter._lastTimestamp
- _OBJC_IVAR_$_CSAudioConverter._opusConverter
- _OBJC_IVAR_$_CSAudioConverter._opusOutASBD
- _OBJC_IVAR_$_CSAudioConverter._outPacketSizeInSec
- _OBJC_IVAR_$_CSAudioConverter._recordBasePacketsPerSecond
- _OBJC_IVAR_$_CSSiriAudioMessageRequestClient._queue
- _OBJC_IVAR_$_CSSiriAudioMessageRequestClient._xpcConnection
- _OBJC_IVAR_$_CSSiriAudioMessageRequestClient._xpcConnectionUUIDString
- _OBJC_IVAR_$_CSVoiceTriggerFileLogger._geckoLoggingEnabled
- _OBJC_IVAR_$_SSRDonationUtteranceData._donationId
- _OBJC_IVAR_$_SSRDonationUtteranceData._locale
- _OBJC_IVAR_$_SSRDonationUtteranceData._triggerPhrase
- _OBJC_IVAR_$_SSREnrollmentSamplingMetaData._selectionStatus
- _OBJC_IVAR_$_SSREnrollmentSamplingMetaData._voiceProfileId
- _OBJC_METACLASS_$_CSAudioConverter
- _OBJC_METACLASS_$_CSRecordTypeSpeechEventConverter
- _OBJC_METACLASS_$_CSSiriAudioMessageRequestClient
- _OBJC_METACLASS_$_SSRDonationUtteranceData
- _OBJC_METACLASS_$_SSREnrollmentSamplingMetaData
- _SSRLogContextFacilityCoreSpeech
- __OBJC_$_CLASS_METHODS_CSAudioConverter
- __OBJC_$_CLASS_METHODS_CSRecordTypeSpeechEventConverter
- __OBJC_$_INSTANCE_METHODS_CSAudioConverter
- __OBJC_$_INSTANCE_METHODS_CSSiriAudioMessageRequestClient
- __OBJC_$_INSTANCE_METHODS_SSRDonationUtteranceData
- __OBJC_$_INSTANCE_METHODS_SSREnrollmentSamplingMetaData
- __OBJC_$_INSTANCE_VARIABLES_CSAudioConverter
- __OBJC_$_INSTANCE_VARIABLES_CSSiriAudioMessageRequestClient
- __OBJC_$_INSTANCE_VARIABLES_SSRDonationUtteranceData
- __OBJC_$_INSTANCE_VARIABLES_SSREnrollmentSamplingMetaData
- __OBJC_$_PROP_LIST_CSAudioConverter
- __OBJC_$_PROP_LIST_CSSiriAudioMessageRequestClient
- __OBJC_$_PROP_LIST_SSRDonationUtteranceData
- __OBJC_$_PROP_LIST_SSREnrollmentSamplingMetaData
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioConverterDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriAudioMessageRequestService
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioConverterDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriAudioMessageRequestService
- __OBJC_$_PROTOCOL_REFS_CSAudioConverterDelegate
- __OBJC_$_PROTOCOL_REFS_CSSiriAudioMessageRequestService
- __OBJC_CLASS_PROTOCOLS_$_CSVoiceTriggerFileLogger
- __OBJC_CLASS_RO_$_CSAudioConverter
- __OBJC_CLASS_RO_$_CSRecordTypeSpeechEventConverter
- __OBJC_CLASS_RO_$_CSSiriAudioMessageRequestClient
- __OBJC_CLASS_RO_$_SSRDonationUtteranceData
- __OBJC_CLASS_RO_$_SSREnrollmentSamplingMetaData
- __OBJC_LABEL_PROTOCOL_$_CSAudioConverterDelegate
- __OBJC_LABEL_PROTOCOL_$_CSSiriAudioMessageRequestService
- __OBJC_METACLASS_RO_$_CSAudioConverter
- __OBJC_METACLASS_RO_$_CSRecordTypeSpeechEventConverter
- __OBJC_METACLASS_RO_$_CSSiriAudioMessageRequestClient
- __OBJC_METACLASS_RO_$_SSRDonationUtteranceData
- __OBJC_METACLASS_RO_$_SSREnrollmentSamplingMetaData
- __OBJC_PROTOCOL_$_CSAudioConverterDelegate
- __OBJC_PROTOCOL_$_CSSiriAudioMessageRequestService
- __OBJC_PROTOCOL_REFERENCE_$_CSSiriAudioMessageRequestService
- __ZNKSt3__111__copy_implclB8ne200100IPNS_6vectorINS2_IfNS_9allocatorIfEEEENS3_IS5_EEEES8_S8_EENS_4pairIT_T1_EESA_T0_SB_
- __ZNKSt3__111__copy_implclB8ne200100IPNS_6vectorIfNS_9allocatorIfEEEES6_S6_EENS_4pairIT_T1_EES8_T0_S9_
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt12out_of_rangeC1B8ne200100EPKc
- __ZNSt3__110unique_ptrI15SmartSiriVolumeNS_14default_deleteIS1_EEE5resetB8ne200100EPS1_
- __ZNSt3__110unique_ptrIN10corespeech25CSAudioCircularBufferImplIhEENS_14default_deleteIS3_EEE5resetB8ne200100EPS3_
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorINS_4pairIfjEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIPjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIfEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__120__throw_out_of_rangeB8ne200100EPKc
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorINS3_IfNS2_IfEEEENS2_IS5_EEEEEEPS7_EEED2B8ne200100Ev
- __ZNSt3__128__exception_guard_exceptionsINS_29_AllocatorDestroyRangeReverseINS_9allocatorINS_6vectorIfNS2_IfEEEEEEPS5_EEED2B8ne200100Ev
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_6vectorINS2_IfNS1_IfEEEENS1_IS4_EEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__135__uninitialized_allocator_copy_implB8ne200100INS_9allocatorINS_6vectorIfNS1_IfEEEEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
- __ZNSt3__16vectorINS0_INS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEEENS1_IS7_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__destroy_vectorclB8ne200100Ev
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE16__init_with_sizeB8ne200100IPS5_S9_EEvT_T0_m
- __ZNSt3__16vectorINS0_INS0_IfNS_9allocatorIfEEEENS1_IS3_EEEENS1_IS5_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__destroy_vectorclB8ne200100Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE16__init_with_sizeB8ne200100IPS3_S7_EEvT_T0_m
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE18__assign_with_sizeB8ne200100IPS3_S7_EEvT_T0_l
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEE5clearB8ne200100Ev
- __ZNSt3__16vectorINS0_IfNS_9allocatorIfEEEENS1_IS3_EEEC2B8ne200100EmRKS3_
- __ZNSt3__16vectorINS_4pairIfjEENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEE11__vallocateB8ne200100Em
- __ZNSt3__16vectorIfNS_9allocatorIfEEE16__init_with_sizeB8ne200100IPfS5_EEvT_T0_m
- __ZNSt3__16vectorIfNS_9allocatorIfEEE18__assign_with_sizeB8ne200100IPfS5_EEvT_T0_l
- __ZNSt3__16vectorIfNS_9allocatorIfEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__16vectorIfNS_9allocatorIfEEEC2B8ne200100EmRKf
- __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8ne200100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___100-[CSRemoteControlClient _fetchDataFromAudioFileUrl:aesKey:encryptedAudioSampleBypeDepth:completion:]_block_invoke.324
- ___102-[CSEndpointerXPCClient resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.22
- ___102-[CoreSpeechXPC voiceTriggerRTModelWithRequestOptions:downloadedModels:preinstalledModels:completion:]_block_invoke.20
- ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.437
- ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.441
- ___105-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.444
- ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.87
- ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.89
- ___105-[CSRemoraEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:recordOption:voiceTriggerInfo:]_block_invoke.91
- ___108-[CSSiriAudioPlaybackService _startRequest:options:preparationHandler:executionHandler:finalizationHandler:]_block_invoke.14
- ___108-[CSSiriAudioPlaybackService _startRequest:options:preparationHandler:executionHandler:finalizationHandler:]_block_invoke_2.15
- ___108-[CSSiriAudioPlaybackService _startRequest:options:preparationHandler:executionHandler:finalizationHandler:]_block_invoke_3.16
- ___109-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:bundleIdentifier:completion:]_block_invoke.12
- ___109-[CSVoiceTriggerAssetHandlerMac _getVoiceTriggerAssetFromAssetManagerWithLocale:bundleIdentifier:completion:]_block_invoke.14
- ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.185
- ___110-[CSVoiceTriggerSecondPass _requestStartAudioStreamWitContext:audioProviderUUID:startStreamOption:completion:]_block_invoke.64
- ___112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.131
- ___113-[CSVoiceTriggerFirstPassJarvis _handleJarvisVoiceTriggerFromDeviceId:activationInfo:triggerHostTime:completion:]_block_invoke.29
- ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.106
- ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.117
- ___118-[CSSiriAudioPlaybackService _startHapticOnlyRequest:options:preparationHandler:executionHandler:finalizationHandler:]_block_invoke.13
- ___125-[CSRemoteControlClient createRemoteVoiceProfileWithAudioFiles:aesKey:encryptedAudioSampleBypeDepth:languageCode:completion:]_block_invoke.298
- ___125-[CSRemoteControlClient createRemoteVoiceProfileWithAudioFiles:aesKey:encryptedAudioSampleBypeDepth:languageCode:completion:]_block_invoke.302
- ___133-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.109
- ___136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.98
- ___136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.99
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.189
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.190
- ___22-[CSXPCClient connect]_block_invoke.9
- ___30-[CSBuiltInVoiceTrigger start]_block_invoke.34
- ___30-[CSBuiltInVoiceTrigger start]_block_invoke.45
- ___30-[CSBuiltInVoiceTrigger start]_block_invoke_2.48
- ___35-[CSBuiltInVoiceTrigger _setAsset:]_block_invoke.74
- ___39-[CSBuiltInVoiceTrigger _stopListening]_block_invoke.100
- ___41-[CSAssetManager initWithDownloadOption:]_block_invoke.19
- ___41-[CSAssetManager initWithDownloadOption:]_block_invoke.21
- ___42-[CSFileAudioInjectionBuiltInEngine start]_block_invoke.20
- ___42-[CSRemoteControlClient didDeviceConnect:]_block_invoke.73
- ___44-[CSBuiltInVoiceTrigger _stopAPVoiceTrigger]_block_invoke.108
- ___46-[CSHybridEndpointAnalyzer processTaskString:]_block_invoke.397
- ___46-[CSSiriAudioMessageRequestClient _connection]_block_invoke
- ___46-[CSSiriAudioMessageRequestClient _connection]_block_invoke.5
- ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.159
- ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.138
- ___48-[CSEndpointerXPCClient _createClientConnection]_block_invoke.139
- ___48-[CSSpeechController CSXPCClient:didDisconnect:]_block_invoke.373
- ___48-[CSXPCClient triggerInfoForContext:completion:]_block_invoke.51
- ___49-[CSAssetController _downloadAsset:withComplete:]_block_invoke.330
- ___49-[CSVoiceTriggerFirstPassHearstAP _stopListening]_block_invoke.30
- ___49-[CSVoiceTriggerFirstPassJarvisAP _stopListening]_block_invoke.24
- ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.251
- ___50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.63
- ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.95
- ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke_2.96
- ___52-[CSSelfTriggerDetector _startListenWithCompletion:]_block_invoke.21
- ___52-[CSSiriAudioPlaybackService _playHapticForRequest:]_block_invoke.9
- ___52-[CSSpeechController setCurrentRecordContext:error:]_block_invoke.249
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.40
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.44
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.45
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.49
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.56
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.57
- ___52-[CSVoiceTriggerAssetHandlerMac triggerAssetRefresh]_block_invoke.20
- ___53-[CSRemoteControlClient _transferFile:at:completion:]_block_invoke.158
- ___53-[CSRemoteControlClient _transferFile:at:completion:]_block_invoke.159
- ___53-[CSXPCClient acousticSLResultForContext:completion:]_block_invoke.47
- ___54-[CSAssetController fetchRemoteMetaOfType:allowRetry:]_block_invoke.318
- ___54-[CSAttSiriMitigationAssetHandler triggerAssetRefresh]_block_invoke.29
- ___54-[CSSelfTriggerDetector _stopListeningWithCompletion:]_block_invoke.22
- ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.224
- ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.233
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.279
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.287
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke_2.288
- ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.261
- ___58-[CSRemoteControlClient exchangeRemoteDeviceProtocolInfo:]_block_invoke.283
- ___59-[CSConnectionListener listener:shouldAcceptNewConnection:]_block_invoke.6
- ___59-[CSConnectionListener listener:shouldAcceptNewConnection:]_block_invoke.8
- ___60-[CSSpeechController handleStopRecordingRequestWithOptions:]_block_invoke.301
- ___60-[CSXPCClient audioStreamWithRequest:streamName:completion:]_block_invoke.43
- ___61-[CSModelBenchmarker _setupAudioInjectionEngineWithAudioURL:]_block_invoke.41
- ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.59
- ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.60
- ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.62
- ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.63
- ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.68
- ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.71
- ___61-[CSRemoraEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2.69
- ___62-[CSRemoraEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke.54
- ___62-[CSVoiceTriggerFirstPassJarvisAP _startListenWithCompletion:]_block_invoke.22
- ___64-[CSEndpointerAssetManager _registerForAssetUpdateNotifications]_block_invoke.311
- ___64-[CSSmartSiriVolume _startListenPollingWithInterval:completion:]_block_invoke.58
- ___64-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke.229
- ___65-[CSVoiceIdXPCConnection _handleImplicitUtteranceMessage:client:]_block_invoke.18
- ___67-[CSSmartSiriVolume startSmartSiriVolumeWithAudioProviderSelector:]_block_invoke.53
- ___68-[CSBuiltInVoiceTrigger _startListenPollingWithInterval:completion:]_block_invoke.90
- ___68-[CSSelfTriggerDetector _startListenPollingWithInterval:completion:]_block_invoke.11
- ___68-[CSTrialAssetDownloadMonitor _validateDownloadedAssetForAssetType:]_block_invoke.49
- ___68-[CSTrialAssetDownloadMonitor _validateDownloadedAssetForAssetType:]_block_invoke.50
- ___68-[CSVoiceTriggerSecondPass _processSecondPassInExclave:rejectBlock:]_block_invoke.100
- ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.262
- ___72-[CSSiriAudioMessageRequestClient forceReleaseAllAudioMessageRetainLock]_block_invoke
- ___72-[CSSiriAudioMessageRequestClient getAudioFileWithRequestId:completion:]_block_invoke
- ___72-[CSSiriAudioMessageRequestClient getAudioFileWithRequestId:completion:]_block_invoke_2
- ___72-[CSVoiceTriggerFirstPassJarvis _handleSecondPassResult:deviceId:error:]_block_invoke.48
- ___72-[CSVoiceTriggerFirstPassJarvis _handleSecondPassResult:deviceId:error:]_block_invoke.49
- ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.250
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.402
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.403
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.404
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.406
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.407
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.410
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.415
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke.419
- ___76-[CSHybridEndpointAnalyzer processOSDFeatures:withFrameDurationMs:withMHID:]_block_invoke_2.408
- ___77-[CSBuiltInVoiceTrigger activationEventNotificationHandler:event:completion:]_block_invoke.148
- ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.114
- ___77-[CSSpeechManager CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke.82
- ___78-[CSRemoteControlClient transferVoiceTriggerAsset:forLanguageCode:completion:]_block_invoke.194
- ___78-[CSSiriAudioMessageRequestClient releaseAudioMessageRetainLockFromRequestId:]_block_invoke
- ___79-[CSVoiceProfileRetrainManager CSVoiceTriggerEnabledMonitor:didReceiveEnabled:]_block_invoke.18
- ___79-[CSVoiceTriggerFileLogger _logVTResult:metaFilePath:audioFilePath:completion:]_block_invoke_2
- ___79-[CSVoiceTriggerFileLogger _logVTResult:metaFilePath:audioFilePath:completion:]_block_invoke_3
- ___80-[CSVoiceTriggerFirstPassHearstAP _startListenWithAudioProviderUUID:completion:]_block_invoke.26
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.235
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.236
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.237
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.245
- ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.79
- ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.86
- ___82-[CoreSpeechXPC voiceTriggerJarvisLanguageList:jarvisSelectedLanguage:completion:]_block_invoke.24
- ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.205
- ___85-[CSRemoteControlClient transferInterstitialAudioFiles:interstitialLevel:completion:]_block_invoke.246
- ___85-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:eventType:]_block_invoke.231
- ___85-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]_block_invoke.28
- ___85-[CSVoiceProfileRetrainManager _runRetrainerWithAssets:withSecureAsset:languageCode:]_block_invoke.30
- ___85-[CSVoiceTriggerFirstPassRemora activationEventNotificationHandler:event:completion:]_block_invoke.118
- ___85-[CSVoiceTriggerFirstPassRemora activationEventNotificationHandler:event:completion:]_block_invoke.120
- ___87-[CSVoiceTriggerFirstPassHearstAP _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:]_block_invoke.44
- ___88-[CSVoiceTriggerFirstPassRemora _handleRemoraTriggerEvent:secondPassRequest:completion:]_block_invoke.129
- ___93-[CSFileAudioInjectionEngine injectAudio:withScaleFactor:outASBD:playbackStarted:completion:]_block_invoke.20
- ___93-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromAOP:audioProviderUUID:completion:]_block_invoke.113
- ___96-[CSAudioConverter _convertBufferedLPCM:allowPartial:timestamp:arrivalTimestampToAudioRecorder:]_block_invoke
- ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.101
- ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.93
- ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke_2.103
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.217
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.218
- ___97-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:]_block_invoke.70
- ___Block_byref_object_copy_.10158
- ___Block_byref_object_copy_.10627
- ___Block_byref_object_copy_.11859
- ___Block_byref_object_copy_.13150
- ___Block_byref_object_copy_.13569
- ___Block_byref_object_copy_.1450
- ___Block_byref_object_copy_.14629
- ___Block_byref_object_copy_.14964
- ___Block_byref_object_copy_.15840
- ___Block_byref_object_copy_.15953
- ___Block_byref_object_copy_.17580
- ___Block_byref_object_copy_.1774
- ___Block_byref_object_copy_.17868
- ___Block_byref_object_copy_.19029
- ___Block_byref_object_copy_.20165
- ___Block_byref_object_copy_.20817
- ___Block_byref_object_copy_.21429
- ___Block_byref_object_copy_.21671
- ___Block_byref_object_copy_.22307
- ___Block_byref_object_copy_.2268
- ___Block_byref_object_copy_.22961
- ___Block_byref_object_copy_.23232
- ___Block_byref_object_copy_.23966
- ___Block_byref_object_copy_.24773
- ___Block_byref_object_copy_.25207
- ___Block_byref_object_copy_.26044
- ___Block_byref_object_copy_.26479
- ___Block_byref_object_copy_.2661
- ___Block_byref_object_copy_.27297
- ___Block_byref_object_copy_.3645
- ___Block_byref_object_copy_.3780
- ___Block_byref_object_copy_.3986
- ___Block_byref_object_copy_.4587
- ___Block_byref_object_copy_.6435
- ___Block_byref_object_copy_.7388
- ___Block_byref_object_copy_.83
- ___Block_byref_object_copy_.8402
- ___Block_byref_object_copy_.8995
- ___Block_byref_object_dispose_.10159
- ___Block_byref_object_dispose_.10628
- ___Block_byref_object_dispose_.11860
- ___Block_byref_object_dispose_.13151
- ___Block_byref_object_dispose_.13570
- ___Block_byref_object_dispose_.1451
- ___Block_byref_object_dispose_.14630
- ___Block_byref_object_dispose_.14965
- ___Block_byref_object_dispose_.15841
- ___Block_byref_object_dispose_.15954
- ___Block_byref_object_dispose_.17581
- ___Block_byref_object_dispose_.1775
- ___Block_byref_object_dispose_.17869
- ___Block_byref_object_dispose_.19030
- ___Block_byref_object_dispose_.20166
- ___Block_byref_object_dispose_.20818
- ___Block_byref_object_dispose_.21430
- ___Block_byref_object_dispose_.21672
- ___Block_byref_object_dispose_.22308
- ___Block_byref_object_dispose_.2269
- ___Block_byref_object_dispose_.22962
- ___Block_byref_object_dispose_.23233
- ___Block_byref_object_dispose_.23967
- ___Block_byref_object_dispose_.24774
- ___Block_byref_object_dispose_.25208
- ___Block_byref_object_dispose_.26045
- ___Block_byref_object_dispose_.26480
- ___Block_byref_object_dispose_.2662
- ___Block_byref_object_dispose_.27298
- ___Block_byref_object_dispose_.3646
- ___Block_byref_object_dispose_.3781
- ___Block_byref_object_dispose_.3987
- ___Block_byref_object_dispose_.4588
- ___Block_byref_object_dispose_.6436
- ___Block_byref_object_dispose_.7389
- ___Block_byref_object_dispose_.84
- ___Block_byref_object_dispose_.8403
- ___Block_byref_object_dispose_.8996
- ___MobileTimerLibraryCore_block_invoke.809
- ___block_descriptor_40_e8_32bs_e28_v24?0"NSString"8"NSURL"16ls32l8
- ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
- ___block_descriptor_56_e8_32s40s48s_e24_v24?0"NSURL"8?<v?>16ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48r_e86_i32?0^I8^{AudioBufferList=I[1{AudioBuffer=II^v}]}16^^{AudioStreamPacketDescription}24ls32l8r48l8s40l8
- ___block_literal_global.10.10776
- ___block_literal_global.10.19559
- ___block_literal_global.10.21115
- ___block_literal_global.10.22167
- ___block_literal_global.102
- ___block_literal_global.10263
- ___block_literal_global.1029
- ___block_literal_global.10408
- ___block_literal_global.10644
- ___block_literal_global.10802
- ___block_literal_global.11.12139
- ___block_literal_global.11019
- ___block_literal_global.112
- ___block_literal_global.11241
- ___block_literal_global.117
- ___block_literal_global.11713
- ___block_literal_global.1185
- ___block_literal_global.11886
- ___block_literal_global.12.14123
- ___block_literal_global.12149
- ___block_literal_global.12249
- ___block_literal_global.12371
- ___block_literal_global.12679
- ___block_literal_global.12785
- ___block_literal_global.12841
- ___block_literal_global.1287
- ___block_literal_global.12896
- ___block_literal_global.13.21116
- ___block_literal_global.13.21262
- ___block_literal_global.13.22168
- ___block_literal_global.13357
- ___block_literal_global.13473
- ___block_literal_global.13699
- ___block_literal_global.14.21187
- ___block_literal_global.14116
- ___block_literal_global.14462
- ___block_literal_global.14519
- ___block_literal_global.14708
- ___block_literal_global.14726
- ___block_literal_global.14837
- ___block_literal_global.15362
- ___block_literal_global.15447
- ___block_literal_global.158
- ___block_literal_global.1580
- ___block_literal_global.15940
- ___block_literal_global.15982
- ___block_literal_global.16.10390
- ___block_literal_global.16.12129
- ___block_literal_global.16.13358
- ___block_literal_global.16.14520
- ___block_literal_global.16.21117
- ___block_literal_global.16625
- ___block_literal_global.17.14463
- ___block_literal_global.17.21188
- ___block_literal_global.17099
- ___block_literal_global.17108
- ___block_literal_global.17154
- ___block_literal_global.17188
- ___block_literal_global.17452
- ___block_literal_global.17528
- ___block_literal_global.17637
- ___block_literal_global.18.14807
- ___block_literal_global.18.21263
- ___block_literal_global.18098
- ___block_literal_global.18167
- ___block_literal_global.18197
- ___block_literal_global.18769
- ___block_literal_global.19049
- ___block_literal_global.19357
- ___block_literal_global.19438
- ___block_literal_global.195
- ___block_literal_global.19576
- ___block_literal_global.19691
- ___block_literal_global.19736
- ___block_literal_global.19752
- ___block_literal_global.2
- ___block_literal_global.20.13334
- ___block_literal_global.20.14464
- ___block_literal_global.20.21189
- ___block_literal_global.20.25190
- ___block_literal_global.20030
- ___block_literal_global.20082
- ___block_literal_global.20187
- ___block_literal_global.20263
- ___block_literal_global.20464
- ___block_literal_global.20801
- ___block_literal_global.21.12786
- ___block_literal_global.211
- ___block_literal_global.21101
- ___block_literal_global.21114
- ___block_literal_global.21186
- ___block_literal_global.2119
- ___block_literal_global.21282
- ___block_literal_global.21332
- ___block_literal_global.21375
- ___block_literal_global.21498
- ___block_literal_global.22.17426
- ___block_literal_global.22.21118
- ___block_literal_global.22165
- ___block_literal_global.22672
- ___block_literal_global.22843
- ___block_literal_global.2288
- ___block_literal_global.22993
- ___block_literal_global.23.21190
- ___block_literal_global.23543
- ___block_literal_global.2367
- ___block_literal_global.23759
- ___block_literal_global.23843
- ___block_literal_global.239
- ___block_literal_global.24.12787
- ___block_literal_global.240
- ___block_literal_global.24223
- ___block_literal_global.2469
- ___block_literal_global.2483
- ___block_literal_global.24906
- ___block_literal_global.25.21119
- ___block_literal_global.25231
- ___block_literal_global.25562
- ___block_literal_global.25852
- ___block_literal_global.25901
- ___block_literal_global.26.25179
- ___block_literal_global.26080
- ___block_literal_global.26185
- ___block_literal_global.26415
- ___block_literal_global.26548
- ___block_literal_global.27.12788
- ___block_literal_global.27093
- ___block_literal_global.27308
- ___block_literal_global.2751
- ___block_literal_global.27582
- ___block_literal_global.2811
- ___block_literal_global.29.21120
- ___block_literal_global.29.21191
- ___block_literal_global.2902
- ___block_literal_global.30.12789
- ___block_literal_global.30.13319
- ___block_literal_global.303
- ___block_literal_global.306
- ___block_literal_global.31
- ___block_literal_global.3126
- ___block_literal_global.329
- ___block_literal_global.3342
- ___block_literal_global.3512
- ___block_literal_global.36.12790
- ___block_literal_global.3696
- ___block_literal_global.3771
- ___block_literal_global.38.9145
- ___block_literal_global.40.20779
- ___block_literal_global.4024
- ___block_literal_global.410
- ___block_literal_global.42.12791
- ___block_literal_global.46.9137
- ___block_literal_global.47
- ___block_literal_global.5.27583
- ___block_literal_global.5073
- ___block_literal_global.521
- ___block_literal_global.54.2363
- ___block_literal_global.5700
- ___block_literal_global.5811
- ___block_literal_global.59.11235
- ___block_literal_global.59.6466
- ___block_literal_global.5997
- ___block_literal_global.6.26075
- ___block_literal_global.6099
- ___block_literal_global.61
- ___block_literal_global.6122
- ___block_literal_global.63
- ___block_literal_global.6502
- ___block_literal_global.661
- ___block_literal_global.6638
- ___block_literal_global.674
- ___block_literal_global.6921
- ___block_literal_global.7.22166
- ___block_literal_global.7.818
- ___block_literal_global.766
- ___block_literal_global.8.1167
- ___block_literal_global.8.26179
- ___block_literal_global.8.26549
- ___block_literal_global.8.27584
- ___block_literal_global.81
- ___block_literal_global.830
- ___block_literal_global.84
- ___block_literal_global.8574
- ___block_literal_global.9177
- ___block_literal_global.9229
- ___block_literal_global.9346
- ___block_literal_global.944
- ___block_literal_global.9754
- __block_invoke.enableHeartbeat
- __block_invoke.enableHeartbeat.11015
- __compensateChannelDataIfNeeded:receivedNumChannels:.heartbeat.14617
- __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.18695
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.11000
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.18686
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.26779
- _audit_stringMobileTimer.812
- _kBypassSecondPassVoiceTrigger_block_invoke.heartbeat
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$_clearOldGeckoLoggingFiles
- _objc_msgSend$_configureAudioConverter:
- _objc_msgSend$_convertBufferedLPCM:allowPartial:timestamp:arrivalTimestampToAudioRecorder:
- _objc_msgSend$_getOEPAssetWithLanguage:
- _objc_msgSend$_hasHearstRoutedAndNotInSplitter
- _objc_msgSend$_newConnection
- _objc_msgSend$assetForAssetType:resourcePath:configVersion:assetProvider:assetVariant:identity:assistantLanguageCode:uafAssetVersion:
- _objc_msgSend$assetVersionForConfig:
- _objc_msgSend$audioConverterBitrate
- _objc_msgSend$audioConverterDidConvertPackets:packets:durationInSec:timestamp:arrivalTimestampToAudioRecorder:
- _objc_msgSend$convertToEnrollmentTriggerPhraseWithPhId:
- _objc_msgSend$convertToUtteranceDataWithDonationString:
- _objc_msgSend$dictionaryRepresentation
- _objc_msgSend$forceReleaseAllAudioMessageRetainLock
- _objc_msgSend$geckoLoggingEnabled
- _objc_msgSend$initWithAssetType:language:regionId:
- _objc_msgSend$initWithAttendingType:startAttendingHostTime:useVAD:useOwnVoiceVAD:useBoron:startOfSpeechThresholdInMs:prependAudioDuration:timeoutThresholdInSec:triggerType:audioStreamHoldingDurationInSec:audioRecordType:deviceId:attendingListeningType:pauseDurationThreshold:maxPauseDelay:
- _objc_msgSend$initWithConfigFile:sampleRate:context:queue:delegate:
- _objc_msgSend$initWithSelectionStatus:voiceProfileId:
- _objc_msgSend$initWithSpeechManager:fileLoggingEnabled:geckoLoggingEnabled:
- _objc_msgSend$installedAssetWithConfig:
- _objc_msgSend$language
- _objc_msgSend$opusNarrowBandASBD
- _objc_msgSend$replaceBytesInRange:withBytes:length:
- _objc_msgSend$rootQueueWithFixedPriority:
- _objc_msgSend$setGeckoLoggingEnabled:
- _objc_msgSend$switchToNewAssetsForAssetType:
- _objc_msgSend$xpcConnectionUUIDString
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x4
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _sharedController.onceToken.11885
- _sharedController.sharedController.11887
- _sharedHandler.onceToken.1028
- _sharedHandler.onceToken.19356
- _sharedHandler.onceToken.26079
- _sharedHandler.sharedHandler.1030
- _sharedHandler.sharedHandler.19358
- _sharedHandler.sharedHandler.26081
- _sharedHandlerDisabledOnDeviceCompilation.onceToken.26074
- _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.26076
- _sharedInstance._sharedInstance.11714
- _sharedInstance._sharedInstance.12897
- _sharedInstance._sharedInstance.14838
- _sharedInstance._sharedInstance.17155
- _sharedInstance._sharedInstance.17453
- _sharedInstance._sharedInstance.17529
- _sharedInstance._sharedInstance.18168
- _sharedInstance._sharedInstance.19692
- _sharedInstance._sharedInstance.20031
- _sharedInstance._sharedInstance.20083
- _sharedInstance._sharedInstance.20264
- _sharedInstance._sharedInstance.23544
- _sharedInstance._sharedInstance.24224
- _sharedInstance._sharedInstance.25902
- _sharedInstance._sharedInstance.27309
- _sharedInstance._sharedInstance.2752
- _sharedInstance._sharedInstance.2812
- _sharedInstance._sharedInstance.3127
- _sharedInstance._sharedInstance.5701
- _sharedInstance._sharedInstance.5812
- _sharedInstance._sharedInstance.6100
- _sharedInstance._sharedInstance.662
- _sharedInstance._sharedInstance.6639
- _sharedInstance._sharedInstance.767
- _sharedInstance._sharedInstance.831
- _sharedInstance._sharedInstance.9230
- _sharedInstance.onceToken.10407
- _sharedInstance.onceToken.10643
- _sharedInstance.onceToken.10801
- _sharedInstance.onceToken.11712
- _sharedInstance.onceToken.1184
- _sharedInstance.onceToken.12840
- _sharedInstance.onceToken.1286
- _sharedInstance.onceToken.12895
- _sharedInstance.onceToken.13472
- _sharedInstance.onceToken.14836
- _sharedInstance.onceToken.15361
- _sharedInstance.onceToken.15446
- _sharedInstance.onceToken.15939
- _sharedInstance.onceToken.17153
- _sharedInstance.onceToken.17451
- _sharedInstance.onceToken.17527
- _sharedInstance.onceToken.17636
- _sharedInstance.onceToken.18097
- _sharedInstance.onceToken.18166
- _sharedInstance.onceToken.18196
- _sharedInstance.onceToken.194
- _sharedInstance.onceToken.19575
- _sharedInstance.onceToken.19690
- _sharedInstance.onceToken.20029
- _sharedInstance.onceToken.20081
- _sharedInstance.onceToken.20262
- _sharedInstance.onceToken.21100
- _sharedInstance.onceToken.21281
- _sharedInstance.onceToken.21374
- _sharedInstance.onceToken.21497
- _sharedInstance.onceToken.22671
- _sharedInstance.onceToken.22842
- _sharedInstance.onceToken.22992
- _sharedInstance.onceToken.23542
- _sharedInstance.onceToken.23842
- _sharedInstance.onceToken.24222
- _sharedInstance.onceToken.25561
- _sharedInstance.onceToken.25900
- _sharedInstance.onceToken.27092
- _sharedInstance.onceToken.27307
- _sharedInstance.onceToken.2750
- _sharedInstance.onceToken.2810
- _sharedInstance.onceToken.2901
- _sharedInstance.onceToken.3125
- _sharedInstance.onceToken.3511
- _sharedInstance.onceToken.5072
- _sharedInstance.onceToken.520
- _sharedInstance.onceToken.53
- _sharedInstance.onceToken.5699
- _sharedInstance.onceToken.5810
- _sharedInstance.onceToken.6098
- _sharedInstance.onceToken.660
- _sharedInstance.onceToken.6637
- _sharedInstance.onceToken.765
- _sharedInstance.onceToken.829
- _sharedInstance.onceToken.9228
- _sharedInstance.sSharedInstance.18198
- _sharedInstance.sharedInstance.12842
- _sharedInstance.sharedInstance.13474
- _sharedInstance.sharedInstance.15448
- _sharedInstance.sharedInstance.18099
- _sharedInstance.sharedInstance.19577
- _sharedInstance.sharedInstance.21102
- _sharedInstance.sharedInstance.21376
- _sharedInstance.sharedInstance.22844
- _sharedInstance.sharedInstance.22994
- _sharedInstance.sharedInstance.27094
- _sharedInstance.sharedInstance.3513
- _sharedInstance.sharedInstance.5074
- _sharedInstance.sharedManager.25563
- _sharedInstance.sharedPolicy.1186
- _sharedInstance.sharedPolicy.21283
- _sharedInstance.sharedPolicy.23844
- _sharedInstance.sharedProvider.22673
- _sharedManager.onceToken.17098
- _sharedManager.onceToken.19048
- _sharedManager.onceToken.6501
- _sharedManager.onceToken.6920
- _sharedManager.sharedManager.17100
- _sharedManager.sharedManager.6503
- _sharedManager.sharedManager.6922
- _sharedMonitor.onceToken.20186
- _sharedMonitor.sharedMonitor.20188
- _sharedService.onceToken.15981
- _sharedService.onceToken.25230
- _sharedService.sharedService.25232
CStrings:
+ "%s Bypass audio here because ::                   1> VoiceTrigger enabled = %{public}d;                   2> phrase spotter bypassed = %{public}d;                   3> should ignore due to hearst/jarvis routed and not in splitter = %{public}d;                   4> has HFP during call = %{public}d;                   5> AVVC recording client # = %{public}lu                   6> is hearst hijackable = %{public}d;                   heartbeat = %{public}lld"
+ "%s Cannot update volume - player is nil"
+ "%s Cannot update volume - session is not active"
+ "%s Endpointer didDetectHardEndpointAtTime"
+ "%s Failed to delete all on-device SMR audio logs at path: %{public}@, error: %{public}@"
+ "%s Failed to get Gecko log directory URL"
+ "%s Failed to get Gecko log directory for deletion"
+ "%s Finished update with error %@"
+ "%s Forwarding isStoppingWithHTTMode=%d to corespeechd via XPC remoteObjectProxy"
+ "%s Has hearst or jarvis routed and not in splitter ignore AOP trigger notification"
+ "%s No active session found for request (%@)"
+ "%s On-device SMR audio log cleanup completed"
+ "%s Second pass is running, ignore AOP trigger notification"
+ "%s Sending message to remote parameter: %@"
+ "%s Session for request (%@) does not support volume updates"
+ "%s Successfully deleted all on-device SMR audio logs at path: %{public}@"
+ "%s Updated volume from %f to %f (fade duration %f ignored for AVPlayer)"
+ "%s Updated volume from %f to %f immediately"
+ "%s Updated volume from %f to %f with fade duration %f"
+ "%s Updating volume to %f with fade duration %f for request (%@)"
+ "%s VT Asset overriding is enabled but the override path is not existed. CoreSpeech is falling back to use the default asset"
+ "%s Volume already at target %f, skipping update"
+ "%s is recording stopping with HTTMode: %@ with current endpointerOperationMode: %@"
+ "%s siri_signpost_begin `%s`"
+ "%s updateVolume called with volume=%f, fadeDuration=%f, request=%@"
+ "+[CSEndpointerAssetManager _getOEPAssetWithLanguage:withOEPEntitledAssetManager:]"
+ "+[CSVoiceTriggerFileLogger deleteAllOnDeviceSMRAudioLogs]"
+ "+[CSVoiceTriggerFileLogger pruneOnDeviceSMRAudioLogs]"
+ "-[CSConnectionListener initWithXpcListener:withMachService:withServiceInterface:withServiceObject:withDelegateInterface:queue:delegate:]"
+ "-[CSConnectionListener notifyRemoteParameter:WithBlock:]_block_invoke"
+ "-[CSEndpointerXPCClient setIsStoppingWithHTTMode:]_block_invoke"
+ "-[CSSiriAudioPlaybackService _updateRequest:volume:fadeDuration:completion:]"
+ "-[CSSiriAudioPlaybackSessionImplAVAudioPlayerBased updateVolume:fadeDuration:completion:]"
+ "-[CSSiriAudioPlaybackSessionImplAVPlayerBased updateVolume:fadeDuration:completion:]"
+ ".*\\.wav$"
+ "/AppleInternal/Library/BuildRoots/4~CIZYugD20eIkpebSvXZVuYZEcjRFrhTqJ5EdxDI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:1172: libc++ Hardening assertion __first <= __last failed: vector::erase(first, last) called with invalid range\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZYugD20eIkpebSvXZVuYZEcjRFrhTqJ5EdxDI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CIZYugD20eIkpebSvXZVuYZEcjRFrhTqJ5EdxDI/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "@\"<CSConnectionListenerDelegate>\""
+ "@\"CSFAudioConverter\""
+ "@\"CSOEPEntitledAssetManager\""
+ "@132@0:8q16Q24Q32B40B44B48d52d60d68q76d84q92@100Q108d116d124"
+ "@40@0:8q16@24Q32"
+ "A"
+ "CSAttendingOptions:::startAttendingSampleCount"
+ "CSFAudioConverterDelegate"
+ "T@\"<CSConnectionListenerDelegate>\",R,W,N,V_delegate"
+ "T@\"CSFAudioConverter\",&,N,V_encoder"
+ "T@\"CSOEPEntitledAssetManager\",&,N,V_oepEntitledAssetManager"
+ "TB,R,N,V_shouldUseLocalFileWriter"
+ "TQ,R,N,V_startAttendingSampleCount"
+ "_geckoLoggingMode"
+ "_getOEPAssetWithLanguage:withOEPEntitledAssetManager:"
+ "_hasHearstRoutedAndNotInSplitterOrJarvisRouted"
+ "_injectSessionsByRequest:"
+ "_notifyDelegateOfNewConnection:"
+ "_notifyDelegateOfRemovedConnection:"
+ "_oepEntitledAssetManager"
+ "_resetAndGetOEPAssetsWithLanguage:"
+ "_shouldLogGeckoEvent:"
+ "_shouldSyncToCompanion"
+ "_startAttendingSampleCount"
+ "_updateRequest:volume:fadeDuration:completion:"
+ "assetForAssetType:resourcePath:configVersion:assetProvider:assetVariant:identity:assistantLanguageCode:uafAssetVersion:oepEntitledAssetManager:"
+ "cleanupOrphanedFilesInDirectory:matchingPattern:"
+ "clearLogFilesInDirectory:matchingPattern:exceedNumber:"
+ "com.apple.corespeech.csxpcclient"
+ "com.apple.corespeech.endpointanalyzerbase"
+ "com.apple.corespeech.endpointer.xpc"
+ "com.apple.corespeech.speechcontroller"
+ "com.apple.corespeech.speechmanager"
+ "connectionListener:didAddConnection:"
+ "connectionListener:didRemoveConnection:"
+ "deleteAllOnDeviceSMRAudioLogs"
+ "hardEndpointDetectedAtTime:withMetrics:eventType:"
+ "inRequestReferenceAudioLengthInSecs"
+ "inRequestSegmentLengthInSecs"
+ "inRequestSegmentSpkrIdScoreThreshold"
+ "inSpeakerSegmentThreshold"
+ "initWithAttendingType:startAttendingHostTime:startAttendingSampleCount:useVAD:useOwnVoiceVAD:useBoron:startOfSpeechThresholdInMs:prependAudioDuration:timeoutThresholdInSec:triggerType:audioStreamHoldingDurationInSec:audioRecordType:deviceId:attendingListeningType:pauseDurationThreshold:maxPauseDelay:"
+ "initWithConfigFile:sampleRate:context:queue:delegate:osdAnalyzerAssetLocker:"
+ "initWithLocaleIdentifier:"
+ "initWithMachService:withServiceInterface:withServiceObject:withDelegateInterface:queue:delegate:"
+ "initWithSpeechManager:fileLoggingEnabled:"
+ "initWithXpcListener:withMachService:withServiceInterface:withServiceObject:withDelegateInterface:queue:delegate:"
+ "installedAssetPath"
+ "invocationUserMinAudioDurationRequired"
+ "invocationUserThreshold"
+ "minAudioDurationRequired"
+ "notifyRemoteParameter:WithBlock:"
+ "oepEntitledAssetManager"
+ "onDeviceSMREnabled"
+ "onDeviceSMRLogRetentionPeriodInDays"
+ "onDeviceSMRMaxNumLogFiles"
+ "optionForFlexibleFollowupWithAudioRecordType:deviceId:startAttendingSampleCount:"
+ "pruneOnDeviceSMRAudioLogs"
+ "recordedAudioAvailableAt:requestId:filenamePostfix:"
+ "rootQueueWithFixedPriority:label:"
+ "setIsStoppingWithHTTMode:"
+ "setOepEntitledAssetManager:"
+ "shouldUseLocalFileWriter"
+ "snrThreshold"
+ "startAttendingSampleCount"
+ "ttrAudioLoggingEnabled"
+ "twoShotDetectedAtTime:"
+ "updateEnrollmentHealthForVoiceProfile:asset:completionHandler:"
+ "updateRequest:volume:fadeDuration:completion:"
+ "updateVolume:fadeDuration:completion:"
+ "v32@0:8@16@?<v@?@>24"
+ "v36@0:8f16d20@?28"
+ "v36@0:8f16d20@?<v@?@\"NSError\">28"
+ "v44@0:8@\"AFAudioPlaybackRequest\"16f24d28@?<v@?@\"NSError\">36"
+ "v44@0:8@16f24d28@?36"
+ "v52@0:8@\"CSFAudioConverter\"16@\"NSArray\"24f32Q36Q44"
- "%s %{public}d bytesConsumed from opus coverter, remains %{public}d bytes"
- "%s AudioConverter is sad: 0x%{public}xd"
- "%s Bypass audio here because ::                   1> VoiceTrigger enabled = %{public}d;                   2> phrase spotter bypassed = %{public}d;                   3> should ignore due to hearst routed and not in splitter = %{public}d;                   4> has HFP during call = %{public}d;                   5> AVVC recording client # = %{public}lu                   6> is hearst hijackable = %{public}d;                   heartbeat = %{public}lld"
- "%s Cannot create AudioConverter using AudioConverterNew : %{public}u"
- "%s Cannot set encoder bit rate : %{public}u"
- "%s Creating new xpc connection..."
- "%s Failed to get audioConverter property (kAudioConverterCurrentOutputStreamDescription) : %{public}d"
- "%s Got asked for %{public}u packets, have %{public}u"
- "%s Has hearst routed and not in splitter ignore AOP trigger notification"
- "%s Ignore since the UUID of xpc connection not match : %@ vs. %@"
- "%s Override result as 'mpty'"
- "%s Resetting AudioConverter buffer"
- "%s Sending message to remote object: %@"
- "%s There is not audio buffer to convert. Skip this."
- "%s [%{public}02u of %{public}02u %{public}fs] Opus packet with %u bytes"
- "%s _configureAudioConverter: AudioConverterGetProperty(MaximumOutputPacketSize): returned status %{public}d"
- "%s _configureAudioConverter: AudioConverterGetProperty(kAudioConverterPropertyMinimumOutputBufferSize) returned status %{public}d"
- "%s _configureAudioConverter: _convertAudioCapacity %{public}u bytes"
- "%s _configureAudioConverter: _convertPacketCount: %{public}u"
- "%s _configureAudioConverter: encoded audio needs minimum of %{public}u bytes per output buffer"
- "%s _configureAudioConverter: final framesPerBuffer: %{public}u"
- "%s createAudioConverter : initial frames per buffer = dur %{public}.2f * sr %{public}.2f = %{public}u"
- "%s createAudioConverter: outputSizePerPacket: %{public}u"
- "%s deallocated"
- "%s donationInfo contain empty info"
- "%s donationInfo return as nil"
- "%s initializing samplingMetaData with nil inputs: %@, %@"
- "%s invalid input from dictionary"
- "%s invalid selection state"
- "%s invalid voiceProfileIdKey"
- "%s xpc connection %@ Interrupted"
- "%s xpc connection %@ Invalidated"
- "+[CSEndpointerAssetManager _getOEPAssetWithLanguage:]"
- "-[CSAudioConverter _configureAudioConverter:]"
- "-[CSAudioConverter _convertBufferedLPCM:allowPartial:timestamp:arrivalTimestampToAudioRecorder:]"
- "-[CSAudioConverter _convertBufferedLPCM:allowPartial:timestamp:arrivalTimestampToAudioRecorder:]_block_invoke"
- "-[CSAudioConverter reset]"
- "-[CSConnectionListener initWithXpcListener:withMachService:withServiceInterface:withServiceObject:withDelegateInterface:queue:]"
- "-[CSSiriAudioMessageRequestClient _connection]"
- "-[CSSiriAudioMessageRequestClient _connection]_block_invoke"
- "-[CSSiriAudioMessageRequestClient dealloc]"
- "-[SSRDonationUtteranceData initWithDonationInfoString:locale:]"
- "-[SSREnrollmentSamplingMetaData initWithDictionary:]"
- "-[SSREnrollmentSamplingMetaData initWithSelectionStatus:voiceProfileId:]"
- ".*"
- "@\"<CSAudioConverterDelegate>\""
- "@\"CSAudioConverter\""
- "@32@0:8@16B24B28"
- "@96@0:8{AudioStreamBasicDescription=dIIIIIIII}16{AudioStreamBasicDescription=dIIIIIIII}56"
- "CSAudioConverter"
- "CSAudioConverter.m"
- "CSAudioConverterDelegate"
- "CSRecordTypeSpeechEventConverter"
- "CSSiriAudioMessageRequestClient"
- "CSSiriAudioMessageRequestClient Queue"
- "CSSiriAudioMessageRequestService"
- "Cannot produce ASPD for PCM"
- "CreateAudioConverter"
- "SSRDonationUtteranceData"
- "SSREnrollmentSamplingMetaData"
- "SSRSamplingSelectionState"
- "SSRSamplingVoiceProfileId"
- "T@\"<CSAudioConverterDelegate>\",W,V_delegate"
- "T@\"CSAudioConverter\",&,N,V_encoder"
- "T@\"NSNumber\",R,N,V_selectionStatus"
- "T@\"NSString\",&,N,V_xpcConnectionUUIDString"
- "T@\"NSString\",R,N,V_donationId"
- "T@\"NSString\",R,N,V_locale"
- "T@\"NSString\",R,N,V_voiceProfileId"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "TB,N,V_geckoLoggingEnabled"
- "TQ,R,N,V_triggerPhrase"
- "Too many buffers"
- "Vv24@0:8@\"NSString\"16"
- "Vv24@0:8@16"
- "Vv32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSURL\">24"
- "_bufferedLPCM"
- "_clearOldGeckoLoggingFiles"
- "_configureAudioConverter:"
- "_convertAudioCapacity"
- "_convertBufferedLPCM:allowPartial:timestamp:arrivalTimestampToAudioRecorder:"
- "_convertPacketCount"
- "_donationId"
- "_geckoLoggingEnabled"
- "_getOEPAssetWithLanguage:"
- "_hasHearstRoutedAndNotInSplitter"
- "_lastArrivalTimestampToAudioRecorder"
- "_lastTimestamp"
- "_locale"
- "_newConnection"
- "_opusConverter"
- "_opusOutASBD"
- "_outPacketSizeInSec"
- "_recordBasePacketsPerSecond"
- "_selectionStatus"
- "_triggerPhrase"
- "_voiceProfileId"
- "_xpcConnectionUUIDString"
- "assetForAssetType:resourcePath:configVersion:assetProvider:assetVariant:identity:assistantLanguageCode:uafAssetVersion:"
- "assetVersionForConfig:"
- "audioConverterBitrate"
- "com.apple.siri.audio_message_service.xpc"
- "convertToEnrollmentTriggerPhraseWithPhId:"
- "convertToUtteranceDataWithDonationString:"
- "dictionaryRepresentation"
- "donationId"
- "forceReleaseAllAudioMessageRetainLock"
- "geckoLoggingEnabled"
- "getSpeechEventForRecordType:"
- "initWithAssetType:language:regionId:"
- "initWithConfigFile:sampleRate:context:queue:delegate:"
- "initWithDonationInfoString:locale:"
- "initWithSelectionStatus:voiceProfileId:"
- "initWithSpeechManager:fileLoggingEnabled:geckoLoggingEnabled:"
- "installedAssetWithConfig:"
- "language"
- "opusNarrowBandASBD"
- "q24@0:8q16"
- "replaceBytesInRange:withBytes:length:"
- "rootQueueWithFixedPriority:"
- "selectionStatus"
- "setGeckoLoggingEnabled:"
- "setXpcConnectionUUIDString:"
- "switchToNewAssetsForAssetType:"
- "triggerPhrase"
- "v44@0:8@16B24Q28Q36"
- "v52@0:8@\"CSAudioConverter\"16@\"NSArray\"24f32Q36Q44"
- "voiceProfileId"
- "xpcConnectionUUIDString"
- "\xa1"
- "\xc1"

```
