## CoreSpeech

> `/System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech`

```diff

-3304.82.8.1.2
-  __TEXT.__text: 0x16dd44
-  __TEXT.__auth_stubs: 0x1d40
-  __TEXT.__objc_methlist: 0x147a8
+3305.27.1.0.0
+  __TEXT.__text: 0x171b48
+  __TEXT.__auth_stubs: 0x1d50
+  __TEXT.__objc_methlist: 0x14bb0
   __TEXT.__const: 0x480
-  __TEXT.__gcc_except_tab: 0x29f8
-  __TEXT.__cstring: 0x2a5f5
-  __TEXT.__oslogstring: 0x2096b
+  __TEXT.__gcc_except_tab: 0x2a8c
+  __TEXT.__cstring: 0x2acb9
+  __TEXT.__oslogstring: 0x20f99
   __TEXT.__dlopen_cstrs: 0x245
-  __TEXT.__unwind_info: 0x5560
+  __TEXT.__unwind_info: 0x5614
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x3437
-  __TEXT.__objc_methname: 0x3a68a
-  __TEXT.__objc_methtype: 0x80ec
-  __TEXT.__objc_stubs: 0x1dae0
-  __DATA_CONST.__got: 0x800
-  __DATA_CONST.__const: 0x4988
-  __DATA_CONST.__objc_classlist: 0x990
+  __TEXT.__objc_classname: 0x34b7
+  __TEXT.__objc_methname: 0x3b4e6
+  __TEXT.__objc_methtype: 0x815d
+  __TEXT.__objc_stubs: 0x1e0c0
+  __DATA_CONST.__got: 0x818
+  __DATA_CONST.__const: 0x4ac8
+  __DATA_CONST.__objc_classlist: 0x9a8
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x37340
-  __DATA_CONST.__objc_selrefs: 0xae38
+  __DATA_CONST.__objc_const: 0x375a8
+  __DATA_CONST.__objc_selrefs: 0xb0b0
   __DATA_CONST.__objc_protorefs: 0xa8
-  __DATA_CONST.__objc_classrefs: 0xfe8
-  __DATA_CONST.__objc_superrefs: 0x7c0
+  __DATA_CONST.__objc_classrefs: 0x1000
+  __DATA_CONST.__objc_superrefs: 0x7d8
   __DATA_CONST.__objc_arraydata: 0x498
-  __AUTH_CONST.__cfstring: 0xab20
-  __AUTH_CONST.__objc_const: 0x7ed0
+  __AUTH_CONST.__cfstring: 0xae20
+  __AUTH_CONST.__objc_const: 0x7ff0
   __AUTH_CONST.__objc_intobj: 0xc48
-  __AUTH_CONST.__const: 0x2180
+  __AUTH_CONST.__const: 0x21a0
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_dictobj: 0x3c0
   __AUTH_CONST.__objc_floatobj: 0x500
   __AUTH_CONST.__objc_arrayobj: 0x198
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0xeb8
+  __AUTH_CONST.__auth_got: 0xec0
   __AUTH.__objc_data: 0x4880
-  __DATA.__objc_ivar: 0x1bfc
+  __DATA.__objc_ivar: 0x1c64
   __DATA.__data: 0x39d8
-  __DATA.__common: 0x30
-  __DATA.__bss: 0x820
-  __DATA_DIRTY.__objc_data: 0x1720
+  __DATA.__common: 0x38
+  __DATA.__bss: 0x838
+  __DATA_DIRTY.__objc_data: 0x1810
   __DATA_DIRTY.__data: 0xc0
   __DATA_DIRTY.__bss: 0x190
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8849
-  Symbols:   29501
-  CStrings:  15462
+  Functions: 8946
+  Symbols:   29801
+  CStrings:  15662
 
Symbols:
+ +[CSAudioInjectionProviderExclave sharedInstance]
+ +[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:recordingInfo:speechEvent:activationMode:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usesDeviceSpeakerForTTS:attemptsToUsePastDataBufferFrames:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isDeviceInCarDNDMode:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]
+ -[CSAggressiveECModeHandler echoCancellationReason]
+ -[CSAggressiveECModeHandler readThisOrVoiceOverSessionActive]
+ -[CSAggressiveECModeHandler setEchoCancellationReason:]
+ -[CSAggressiveECModeHandler setReadThisOrVoiceOverSessionActive:]
+ -[CSAudioInjectionProviderExclave .cxx_destruct]
+ -[CSAudioInjectionProviderExclave _createAudioQueueIfNeeded]
+ -[CSAudioInjectionProviderExclave _defaultBufferRef]
+ -[CSAudioInjectionProviderExclave _defaultOutASBD]
+ -[CSAudioInjectionProviderExclave _prepareAndStartAudioQueue]
+ -[CSAudioInjectionProviderExclave _readAudioBufferAndFeedIntoAudioQueue]
+ -[CSAudioInjectionProviderExclave _setAudioSessionActive:]
+ -[CSAudioInjectionProviderExclave bufferDuration]
+ -[CSAudioInjectionProviderExclave exclaveAudioQueue]
+ -[CSAudioInjectionProviderExclave fileOption]
+ -[CSAudioInjectionProviderExclave init]
+ -[CSAudioInjectionProviderExclave injectionCompletion]
+ -[CSAudioInjectionProviderExclave injectionEndTime]
+ -[CSAudioInjectionProviderExclave injectionStartTime]
+ -[CSAudioInjectionProviderExclave isAudioQueueStarted]
+ -[CSAudioInjectionProviderExclave queue]
+ -[CSAudioInjectionProviderExclave setBufferDuration:]
+ -[CSAudioInjectionProviderExclave setExclaveAudioQueue:]
+ -[CSAudioInjectionProviderExclave setFileOption:]
+ -[CSAudioInjectionProviderExclave setInjectionCompletion:]
+ -[CSAudioInjectionProviderExclave setInjectionEndTime:]
+ -[CSAudioInjectionProviderExclave setInjectionStartTime:]
+ -[CSAudioInjectionProviderExclave setIsAudioQueueStarted:]
+ -[CSAudioInjectionProviderExclave setQueue:]
+ -[CSAudioInjectionProviderExclave speakAudioInExclave:withCompletion:]
+ -[CSAudioInjectionProviderExclave start]
+ -[CSBuiltInVoiceTrigger _updateExclaveKitSiriLocale:]
+ -[CSBuiltInVoiceTrigger updateExclaveKitSiriLocale:]
+ -[CSEnhancedEndpointerResult didForceEndpoint]
+ -[CSEnhancedEndpointerResult setDidForceEndpoint:]
+ -[CSHybridEndpointer _updateCurrentAsset:]
+ -[CSMyriadPHash generatePHashFromExclaveVoiceTriggerInfo:writeFile:]
+ -[CSVoiceTriggerFirstPassHearst CSPhoneCallStateMonitor:didRecievePhoneCallStateChange:]
+ -[CSVoiceTriggerFirstPassHearst initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:]
+ -[CSVoiceTriggerFirstPassHearst otherAppRecordingStateMonitor]
+ -[CSVoiceTriggerFirstPassHearst phoneCallStateMonitor]
+ -[CSVoiceTriggerFirstPassHearst phoneCallState]
+ -[CSVoiceTriggerFirstPassHearst setOtherAppRecordingStateMonitor:]
+ -[CSVoiceTriggerFirstPassHearst setPhoneCallState:]
+ -[CSVoiceTriggerFirstPassHearst setPhoneCallStateMonitor:]
+ -[CSVoiceTriggerFirstPassHearst setVoiceTriggerEnabledMonitor:]
+ -[CSVoiceTriggerFirstPassHearst voiceTriggerEnabledMonitor]
+ -[CSVoiceTriggerSecondPass _calculateRecordingTimeForAOPTriggerFromFirstPassInfo:completion:]
+ -[CSVoiceTriggerSecondPass _getExclaveAudioTimeConverter]
+ -[CSVoiceTriggerSecondPass exclaveAudioTimeConverter]
+ -[CSVoiceTriggerSecondPass setExclaveAudioTimeConverter:]
+ -[SecureSpeakerRecognitionConfigBridge .cxx_destruct]
+ -[SecureSpeakerRecognitionConfigBridge combinationWeight]
+ -[SecureSpeakerRecognitionConfigBridge description]
+ -[SecureSpeakerRecognitionConfigBridge implicitProfileDeltaThreshold]
+ -[SecureSpeakerRecognitionConfigBridge implicitProfileThreshold]
+ -[SecureSpeakerRecognitionConfigBridge implicitTrainingEnabled]
+ -[SecureSpeakerRecognitionConfigBridge implicitVTThreshold]
+ -[SecureSpeakerRecognitionConfigBridge initWithPhraseConfigs:numPruningRetentionUtt:pruningExplicitSATThreshold:pruningExplicitPSRThreshold:pruningSATThreshold:pruningPSRThreshold:combinationWeight:implicitProfileThreshold:implicitProfileDeltaThreshold:implicitVTThreshold:maxEnrollmentUtterances:implicit_training_enabled:multiUserHighScoreThreshold:multiUserLowScoreThreshold:multiUserConfidentScoreThreshold:multiUserDeltaScoreThreshold:useTDTIEnrollment:]
+ -[SecureSpeakerRecognitionConfigBridge iteratePhraseConfigs:]
+ -[SecureSpeakerRecognitionConfigBridge maxEnrollmentUtterances]
+ -[SecureSpeakerRecognitionConfigBridge multiUserConfidentScoreThreshold]
+ -[SecureSpeakerRecognitionConfigBridge multiUserDeltaScoreThreshold]
+ -[SecureSpeakerRecognitionConfigBridge multiUserHighScoreThreshold]
+ -[SecureSpeakerRecognitionConfigBridge multiUserLowScoreThreshold]
+ -[SecureSpeakerRecognitionConfigBridge numPruningRetentionUtt]
+ -[SecureSpeakerRecognitionConfigBridge phraseConfigs]
+ -[SecureSpeakerRecognitionConfigBridge pruningExplicitPSRThreshold]
+ -[SecureSpeakerRecognitionConfigBridge pruningExplicitSATThreshold]
+ -[SecureSpeakerRecognitionConfigBridge pruningPSRThreshold]
+ -[SecureSpeakerRecognitionConfigBridge pruningSATThreshold]
+ -[SecureSpeakerRecognitionConfigBridge setCombinationWeight:]
+ -[SecureSpeakerRecognitionConfigBridge setImplicitProfileDeltaThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setImplicitProfileThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setImplicitTrainingEnabled:]
+ -[SecureSpeakerRecognitionConfigBridge setImplicitVTThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setMaxEnrollmentUtterances:]
+ -[SecureSpeakerRecognitionConfigBridge setMultiUserConfidentScoreThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setMultiUserDeltaScoreThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setMultiUserHighScoreThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setMultiUserLowScoreThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setNumPruningRetentionUtt:]
+ -[SecureSpeakerRecognitionConfigBridge setPhraseConfigs:]
+ -[SecureSpeakerRecognitionConfigBridge setPruningExplicitPSRThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setPruningExplicitSATThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setPruningPSRThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setPruningSATThreshold:]
+ -[SecureSpeakerRecognitionConfigBridge setUseTDTIEnrollment:]
+ -[SecureSpeakerRecognitionConfigBridge useTDTIEnrollment]
+ -[SecureSpeakerRecognitionPhraseConfigBridge .cxx_destruct]
+ -[SecureSpeakerRecognitionPhraseConfigBridge initWithName:satThreshold:]
+ -[SecureSpeakerRecognitionPhraseConfigBridge name]
+ -[SecureSpeakerRecognitionPhraseConfigBridge satThreshold]
+ -[SecureSpeakerRecognitionPhraseConfigBridge setName:]
+ -[SecureSpeakerRecognitionPhraseConfigBridge setSatThreshold:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder _decodePhraseConfig:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder _getBooleanValue:forKey:withDefaultValue:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder _getFloatValue:forKey:withDefaultValue:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder _getIntValue:forKey:withDefaultValue:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder decodeSecureVoiceTriggerSpeakerRecognitionConfigForAsset:]
+ -[SecureVoiceTriggerSpeakerRecognitionDecoder init]
+ GCC_except_table1234
+ GCC_except_table1246
+ GCC_except_table1275
+ GCC_except_table1472
+ GCC_except_table149
+ GCC_except_table1538
+ GCC_except_table1562
+ GCC_except_table1566
+ GCC_except_table1582
+ GCC_except_table1585
+ GCC_except_table1613
+ GCC_except_table1709
+ GCC_except_table1711
+ GCC_except_table1713
+ GCC_except_table1719
+ GCC_except_table173
+ GCC_except_table1774
+ GCC_except_table1806
+ GCC_except_table1885
+ GCC_except_table1905
+ GCC_except_table2128
+ GCC_except_table2264
+ GCC_except_table229
+ GCC_except_table2310
+ GCC_except_table2313
+ GCC_except_table2316
+ GCC_except_table232
+ GCC_except_table2321
+ GCC_except_table2333
+ GCC_except_table2338
+ GCC_except_table2341
+ GCC_except_table2367
+ GCC_except_table2371
+ GCC_except_table2469
+ GCC_except_table2487
+ GCC_except_table2619
+ GCC_except_table2684
+ GCC_except_table2687
+ GCC_except_table2698
+ GCC_except_table2739
+ GCC_except_table2740
+ GCC_except_table2741
+ GCC_except_table2742
+ GCC_except_table2743
+ GCC_except_table2748
+ GCC_except_table2751
+ GCC_except_table2754
+ GCC_except_table2755
+ GCC_except_table2758
+ GCC_except_table2759
+ GCC_except_table2768
+ GCC_except_table2774
+ GCC_except_table2776
+ GCC_except_table2777
+ GCC_except_table2843
+ GCC_except_table3112
+ GCC_except_table3198
+ GCC_except_table3219
+ GCC_except_table3237
+ GCC_except_table3250
+ GCC_except_table3271
+ GCC_except_table3274
+ GCC_except_table3277
+ GCC_except_table3307
+ GCC_except_table335
+ GCC_except_table3369
+ GCC_except_table3487
+ GCC_except_table3591
+ GCC_except_table3617
+ GCC_except_table3679
+ GCC_except_table3681
+ GCC_except_table3683
+ GCC_except_table3699
+ GCC_except_table3701
+ GCC_except_table3703
+ GCC_except_table3707
+ GCC_except_table3709
+ GCC_except_table3711
+ GCC_except_table3725
+ GCC_except_table3731
+ GCC_except_table3733
+ GCC_except_table3768
+ GCC_except_table388
+ GCC_except_table391
+ GCC_except_table3924
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table3948
+ GCC_except_table395
+ GCC_except_table397
+ GCC_except_table4006
+ GCC_except_table4041
+ GCC_except_table4130
+ GCC_except_table418
+ GCC_except_table4377
+ GCC_except_table4499
+ GCC_except_table4522
+ GCC_except_table4577
+ GCC_except_table4792
+ GCC_except_table4796
+ GCC_except_table4864
+ GCC_except_table4870
+ GCC_except_table4877
+ GCC_except_table4883
+ GCC_except_table4952
+ GCC_except_table5108
+ GCC_except_table5118
+ GCC_except_table5142
+ GCC_except_table5165
+ GCC_except_table5215
+ GCC_except_table5227
+ GCC_except_table5250
+ GCC_except_table5344
+ GCC_except_table536
+ GCC_except_table5372
+ GCC_except_table5378
+ GCC_except_table5380
+ GCC_except_table5383
+ GCC_except_table5391
+ GCC_except_table5393
+ GCC_except_table5398
+ GCC_except_table5400
+ GCC_except_table5411
+ GCC_except_table5412
+ GCC_except_table5417
+ GCC_except_table5423
+ GCC_except_table5428
+ GCC_except_table5430
+ GCC_except_table5432
+ GCC_except_table5434
+ GCC_except_table5435
+ GCC_except_table5436
+ GCC_except_table5437
+ GCC_except_table5439
+ GCC_except_table5440
+ GCC_except_table5441
+ GCC_except_table5442
+ GCC_except_table5443
+ GCC_except_table5445
+ GCC_except_table5446
+ GCC_except_table5447
+ GCC_except_table5449
+ GCC_except_table5464
+ GCC_except_table5552
+ GCC_except_table5556
+ GCC_except_table5610
+ GCC_except_table5639
+ GCC_except_table5642
+ GCC_except_table5837
+ GCC_except_table585
+ GCC_except_table5853
+ GCC_except_table5861
+ GCC_except_table5866
+ GCC_except_table5883
+ GCC_except_table5886
+ GCC_except_table5890
+ GCC_except_table5893
+ GCC_except_table590
+ GCC_except_table5903
+ GCC_except_table591
+ GCC_except_table592
+ GCC_except_table596
+ GCC_except_table6168
+ GCC_except_table617
+ GCC_except_table618
+ GCC_except_table6198
+ GCC_except_table6203
+ GCC_except_table624
+ GCC_except_table6242
+ GCC_except_table6251
+ GCC_except_table6356
+ GCC_except_table6362
+ GCC_except_table652
+ GCC_except_table6599
+ GCC_except_table6603
+ GCC_except_table6636
+ GCC_except_table6679
+ GCC_except_table6687
+ GCC_except_table6710
+ GCC_except_table6717
+ GCC_except_table6718
+ GCC_except_table6860
+ GCC_except_table6915
+ GCC_except_table7037
+ GCC_except_table7038
+ GCC_except_table704
+ GCC_except_table7048
+ GCC_except_table7049
+ GCC_except_table7194
+ GCC_except_table7212
+ GCC_except_table7216
+ GCC_except_table7221
+ GCC_except_table7226
+ GCC_except_table7233
+ GCC_except_table724
+ GCC_except_table7263
+ GCC_except_table7331
+ GCC_except_table7343
+ GCC_except_table7366
+ GCC_except_table7377
+ GCC_except_table7380
+ GCC_except_table7403
+ GCC_except_table7415
+ GCC_except_table7783
+ GCC_except_table779
+ GCC_except_table7793
+ GCC_except_table781
+ GCC_except_table7844
+ GCC_except_table785
+ GCC_except_table790
+ GCC_except_table7920
+ GCC_except_table7930
+ GCC_except_table7932
+ GCC_except_table7933
+ GCC_except_table7935
+ GCC_except_table7942
+ GCC_except_table7947
+ GCC_except_table7948
+ GCC_except_table7952
+ GCC_except_table7953
+ GCC_except_table7957
+ GCC_except_table7958
+ GCC_except_table7959
+ GCC_except_table7960
+ GCC_except_table7962
+ GCC_except_table7963
+ GCC_except_table7964
+ GCC_except_table7965
+ GCC_except_table7967
+ GCC_except_table7969
+ GCC_except_table7970
+ GCC_except_table7999
+ GCC_except_table8053
+ GCC_except_table8077
+ GCC_except_table8119
+ GCC_except_table8130
+ GCC_except_table8276
+ GCC_except_table8284
+ GCC_except_table8416
+ GCC_except_table8508
+ GCC_except_table8550
+ GCC_except_table8581
+ GCC_except_table8595
+ GCC_except_table8602
+ GCC_except_table8607
+ GCC_except_table8622
+ _AQInjectionOutputCallback
+ _AVAudioSessionCategoryPlayback
+ _AVAudioSessionModeDefault
+ _AudioConverterFillComplexBuffer_BlockInvoke.29697
+ _AudioQueueNewOutput
+ _CSLogContextFacilityCoreSpeechExclave
+ _CSSecureLogInitIfNeeded
+ _CSSecureLogInitIfNeeded.once
+ _MobileTimerLibrary.930
+ _MobileTimerLibraryCore.frameworkLibrary.936
+ _OBJC_CLASS_$_CSAudioInjectionProviderExclave
+ _OBJC_CLASS_$_SSRSpeakerProfileEmbeddingExtractor
+ _OBJC_CLASS_$_SecureSpeakerRecognitionConfigBridge
+ _OBJC_CLASS_$_SecureSpeakerRecognitionPhraseConfigBridge
+ _OBJC_CLASS_$_SecureVoiceTriggerSpeakerRecognitionDecoder
+ _OBJC_IVAR_$_CSAggressiveECModeHandler._echoCancellationReason
+ _OBJC_IVAR_$_CSAggressiveECModeHandler._readThisOrVoiceOverSessionActive
+ _OBJC_IVAR_$_CSAudioInjectionProviderExclave._bufferDuration
+ _OBJC_IVAR_$_CSAudioInjectionProviderExclave._exclaveAudioQueue
+ _OBJC_IVAR_$_CSAudioInjectionProviderExclave._fileOption
+ _OBJC_IVAR_$_CSAudioInjectionProviderExclave._injectionCompletion
+ _OBJC_IVAR_$_CSAudioInjectionProviderExclave._injectionEndTime
+ _OBJC_IVAR_$_CSAudioInjectionProviderExclave._injectionStartTime
+ _OBJC_IVAR_$_CSAudioInjectionProviderExclave._isAudioQueueStarted
+ _OBJC_IVAR_$_CSAudioInjectionProviderExclave._queue
+ _OBJC_IVAR_$_CSEnhancedEndpointerResult._didForceEndpoint
+ _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._otherAppRecordingStateMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._phoneCallState
+ _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._phoneCallStateMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._voiceTriggerEnabledMonitor
+ _OBJC_IVAR_$_CSVoiceTriggerSecondPass._exclaveAudioTimeConverter
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._combinationWeight
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._implicitProfileDeltaThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._implicitProfileThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._implicitTrainingEnabled
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._implicitVTThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._maxEnrollmentUtterances
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._multiUserConfidentScoreThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._multiUserDeltaScoreThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._multiUserHighScoreThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._multiUserLowScoreThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._numPruningRetentionUtt
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._phraseConfigs
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._pruningExplicitPSRThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._pruningExplicitSATThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._pruningPSRThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._pruningSATThreshold
+ _OBJC_IVAR_$_SecureSpeakerRecognitionConfigBridge._useTDTIEnrollment
+ _OBJC_IVAR_$_SecureSpeakerRecognitionPhraseConfigBridge._name
+ _OBJC_IVAR_$_SecureSpeakerRecognitionPhraseConfigBridge._satThreshold
+ _OBJC_METACLASS_$_CSAudioInjectionProviderExclave
+ _OBJC_METACLASS_$_SecureSpeakerRecognitionConfigBridge
+ _OBJC_METACLASS_$_SecureSpeakerRecognitionPhraseConfigBridge
+ _OBJC_METACLASS_$_SecureVoiceTriggerSpeakerRecognitionDecoder
+ __OBJC_$_CLASS_METHODS_CSAudioInjectionProviderExclave
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.12786
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.13105
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.16877
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.17579
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.24483
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.26471
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.28656
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.29141
+ __OBJC_$_INSTANCE_METHODS_CSAudioInjectionProviderExclave
+ __OBJC_$_INSTANCE_METHODS_SecureSpeakerRecognitionConfigBridge
+ __OBJC_$_INSTANCE_METHODS_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_$_INSTANCE_METHODS_SecureVoiceTriggerSpeakerRecognitionDecoder
+ __OBJC_$_INSTANCE_VARIABLES_CSAudioInjectionProviderExclave
+ __OBJC_$_INSTANCE_VARIABLES_SecureSpeakerRecognitionConfigBridge
+ __OBJC_$_INSTANCE_VARIABLES_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_$_PROP_LIST_CSAudioInjectionProviderExclave
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzer.18939
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzer.24304
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzer.25541
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzerImpl.18940
+ __OBJC_$_PROP_LIST_CSEndpointAnalyzerImpl.24305
+ __OBJC_$_PROP_LIST_CSSiriAudioPlaybackSession.14707
+ __OBJC_$_PROP_LIST_NSObject.10103
+ __OBJC_$_PROP_LIST_NSObject.10423
+ __OBJC_$_PROP_LIST_NSObject.10614
+ __OBJC_$_PROP_LIST_NSObject.10887
+ __OBJC_$_PROP_LIST_NSObject.11257
+ __OBJC_$_PROP_LIST_NSObject.11457
+ __OBJC_$_PROP_LIST_NSObject.1148
+ __OBJC_$_PROP_LIST_NSObject.11981
+ __OBJC_$_PROP_LIST_NSObject.12142
+ __OBJC_$_PROP_LIST_NSObject.12503
+ __OBJC_$_PROP_LIST_NSObject.1294
+ __OBJC_$_PROP_LIST_NSObject.13382
+ __OBJC_$_PROP_LIST_NSObject.13559
+ __OBJC_$_PROP_LIST_NSObject.1437
+ __OBJC_$_PROP_LIST_NSObject.14414
+ __OBJC_$_PROP_LIST_NSObject.14708
+ __OBJC_$_PROP_LIST_NSObject.14903
+ __OBJC_$_PROP_LIST_NSObject.15251
+ __OBJC_$_PROP_LIST_NSObject.1535
+ __OBJC_$_PROP_LIST_NSObject.15397
+ __OBJC_$_PROP_LIST_NSObject.156
+ __OBJC_$_PROP_LIST_NSObject.15636
+ __OBJC_$_PROP_LIST_NSObject.1601
+ __OBJC_$_PROP_LIST_NSObject.16420
+ __OBJC_$_PROP_LIST_NSObject.16577
+ __OBJC_$_PROP_LIST_NSObject.17244
+ __OBJC_$_PROP_LIST_NSObject.17399
+ __OBJC_$_PROP_LIST_NSObject.1740
+ __OBJC_$_PROP_LIST_NSObject.18072
+ __OBJC_$_PROP_LIST_NSObject.18244
+ __OBJC_$_PROP_LIST_NSObject.18941
+ __OBJC_$_PROP_LIST_NSObject.19218
+ __OBJC_$_PROP_LIST_NSObject.20072
+ __OBJC_$_PROP_LIST_NSObject.20222
+ __OBJC_$_PROP_LIST_NSObject.21120
+ __OBJC_$_PROP_LIST_NSObject.21403
+ __OBJC_$_PROP_LIST_NSObject.21480
+ __OBJC_$_PROP_LIST_NSObject.21797
+ __OBJC_$_PROP_LIST_NSObject.2237
+ __OBJC_$_PROP_LIST_NSObject.22715
+ __OBJC_$_PROP_LIST_NSObject.22950
+ __OBJC_$_PROP_LIST_NSObject.23249
+ __OBJC_$_PROP_LIST_NSObject.2347
+ __OBJC_$_PROP_LIST_NSObject.24306
+ __OBJC_$_PROP_LIST_NSObject.24981
+ __OBJC_$_PROP_LIST_NSObject.25109
+ __OBJC_$_PROP_LIST_NSObject.25173
+ __OBJC_$_PROP_LIST_NSObject.25277
+ __OBJC_$_PROP_LIST_NSObject.25542
+ __OBJC_$_PROP_LIST_NSObject.25782
+ __OBJC_$_PROP_LIST_NSObject.26043
+ __OBJC_$_PROP_LIST_NSObject.26235
+ __OBJC_$_PROP_LIST_NSObject.26733
+ __OBJC_$_PROP_LIST_NSObject.26998
+ __OBJC_$_PROP_LIST_NSObject.27149
+ __OBJC_$_PROP_LIST_NSObject.27418
+ __OBJC_$_PROP_LIST_NSObject.27554
+ __OBJC_$_PROP_LIST_NSObject.28244
+ __OBJC_$_PROP_LIST_NSObject.28439
+ __OBJC_$_PROP_LIST_NSObject.28903
+ __OBJC_$_PROP_LIST_NSObject.2934
+ __OBJC_$_PROP_LIST_NSObject.29527
+ __OBJC_$_PROP_LIST_NSObject.29632
+ __OBJC_$_PROP_LIST_NSObject.30308
+ __OBJC_$_PROP_LIST_NSObject.30810
+ __OBJC_$_PROP_LIST_NSObject.30904
+ __OBJC_$_PROP_LIST_NSObject.31054
+ __OBJC_$_PROP_LIST_NSObject.3109
+ __OBJC_$_PROP_LIST_NSObject.313
+ __OBJC_$_PROP_LIST_NSObject.3253
+ __OBJC_$_PROP_LIST_NSObject.3474
+ __OBJC_$_PROP_LIST_NSObject.3745
+ __OBJC_$_PROP_LIST_NSObject.390
+ __OBJC_$_PROP_LIST_NSObject.4256
+ __OBJC_$_PROP_LIST_NSObject.4458
+ __OBJC_$_PROP_LIST_NSObject.4856
+ __OBJC_$_PROP_LIST_NSObject.5564
+ __OBJC_$_PROP_LIST_NSObject.568
+ __OBJC_$_PROP_LIST_NSObject.5947
+ __OBJC_$_PROP_LIST_NSObject.6172
+ __OBJC_$_PROP_LIST_NSObject.6284
+ __OBJC_$_PROP_LIST_NSObject.6385
+ __OBJC_$_PROP_LIST_NSObject.7114
+ __OBJC_$_PROP_LIST_NSObject.7350
+ __OBJC_$_PROP_LIST_NSObject.7530
+ __OBJC_$_PROP_LIST_NSObject.7594
+ __OBJC_$_PROP_LIST_NSObject.8142
+ __OBJC_$_PROP_LIST_NSObject.8272
+ __OBJC_$_PROP_LIST_NSObject.8724
+ __OBJC_$_PROP_LIST_NSObject.9192
+ __OBJC_$_PROP_LIST_NSObject.9285
+ __OBJC_$_PROP_LIST_NSObject.9547
+ __OBJC_$_PROP_LIST_SecureSpeakerRecognitionConfigBridge
+ __OBJC_$_PROP_LIST_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.12787
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.13106
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.16878
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.17580
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.24484
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.26472
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.28657
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.29142
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.20073
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.3746
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.4857
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.7115
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAssetManagerDelegate.24307
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAttSiriMitigationAssetHandlerDelegate.26734
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioConverterDelegate.12143
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.12144
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.12504
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.1741
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.22951
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.4257
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioRecorderDelegate.26999
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioRouteChangeMonitorDelegate.21121
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioSessionInfoProviding.25110
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProviding.27419
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.10104
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.11258
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.16421
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.17245
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.19219
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.20074
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.30309
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.4459
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.4858
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.7351
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.8725
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBenchmarkXPCProtocol.22952
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBluetoothWirelessSplitterMonitorDelegate.21122
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBluetoothWirelessSplitterMonitorDelegate.26735
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.18942
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.24308
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.25543
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerDelegate.28245
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImpl.18943
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImpl.24309
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImplDelegate.25544
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFallbackAudioSessionReleaseProviding.27000
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.13383
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.7531
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.8726
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.9548
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSMediaPlayingMonitorDelegate.17246
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.20075
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.26736
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.30310
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSecondPassProgressProviding.20076
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.11458
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.20077
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.5948
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriAudioPlaybackSession.14709
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.10105
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.10888
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.11259
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.13560
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.17247
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.20078
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.26236
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.30311
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.3747
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.4859
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.7929
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSpeakerRecognitionAssetDownloadMonitorDelegate.18245
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSystemShellStartProviding.14904
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSystemShellStartProviding.23250
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSTrialAssetDownloadMonitorDelegate.3475
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSUAFDownloadMonitorDelegate.29528
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.29529
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.7116
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.8727
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.10615
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.11459
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.14415
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.21123
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.25783
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.10889
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.18246
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.20079
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSXPCClientDelegate.7352
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSXPCClientDelegate.8728
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreSpeechXPCProtocol.22617
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_EARCaesuraSilencePosteriorGeneratorDelegate.28904
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.12788
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.13107
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.16879
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.17581
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.24485
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.26473
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.28658
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.29143
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.31113
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.17582
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.24486
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.26474
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.28659
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.29144
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10106
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10424
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10616
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10890
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11260
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11460
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1149
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11982
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12145
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12505
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1295
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.13384
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.13561
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1438
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14416
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14710
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14905
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15252
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1536
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15398
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15637
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.157
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1602
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16422
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16578
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17248
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17400
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1742
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.18073
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.18247
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.18944
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.19220
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.20080
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.20223
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21124
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21404
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21481
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21798
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2238
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22716
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22953
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.23251
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2348
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24310
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24982
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25111
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25174
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25278
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25545
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25784
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26044
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26237
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26737
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27001
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27150
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27420
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27555
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28246
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28440
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28905
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2935
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29530
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29633
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30312
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30811
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30905
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.31055
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3110
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.314
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3254
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3476
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3748
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.391
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4258
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4460
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4860
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5565
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.569
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5949
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6173
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6285
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6386
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7117
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7353
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7532
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7595
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7930
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8143
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8273
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8729
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9193
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9286
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9549
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioRecorderDelegate.27002
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.16423
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.16579
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.17249
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.18074
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.20081
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.27421
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.30313
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.6286
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.6387
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.7118
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionControllerDelegate.28247
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionControllerDelegate.28441
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.10107
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.11261
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.16424
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.17250
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.19221
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.20082
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.30314
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.4461
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.4861
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.7354
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.8730
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.18945
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.24311
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.25546
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerDelegate.28248
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImpl.18946
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImpl.24312
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImplDelegate.25547
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSKeywordAnalyzerNDEAPIScoreDelegate.15399
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSOpportuneSpeakEventMonitorDelegate.10108
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSPGEndpointAnalyzerDelegate.4862
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.10109
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.10891
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.11262
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.13562
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.17251
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.20083
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.26238
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.30315
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.3749
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.4863
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.7931
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.10617
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.11461
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.14417
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.21125
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.25785
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVolumeMonitorDelegate.10618
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EARCaesuraSilencePosteriorGeneratorDelegate.28906
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10110
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10425
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10619
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10892
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11263
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11462
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1150
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11983
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12146
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12506
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1296
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.13385
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.13563
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1439
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14418
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14711
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14906
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15253
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1537
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15400
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15638
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.158
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1603
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.16425
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.16580
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17252
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17401
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1743
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.18075
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.18248
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.18947
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.19222
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.20084
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.20224
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21126
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21405
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21482
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21799
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2239
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22717
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22954
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.23252
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2349
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24313
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24983
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25112
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25175
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25279
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25548
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25786
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26045
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26239
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26738
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27003
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27151
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27422
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27556
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28249
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28442
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28907
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2936
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29531
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29634
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30316
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30812
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30906
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.31056
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3111
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.315
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3255
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3477
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3750
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.392
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4259
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4462
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4864
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5566
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.570
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5950
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6174
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6287
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6388
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7119
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7355
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7533
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7596
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7932
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8144
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8274
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8731
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9194
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9287
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9550
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SNResultsObserving.8145
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRSpeakerRecognitionControllerDelegate.8732
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNResultsObserving.8146
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.20085
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.3751
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.4865
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.7120
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAssetManagerDelegate.24314
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAttSiriMitigationAssetHandlerDelegate.26739
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioConverterDelegate.12147
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.12148
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.12507
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.1744
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.22955
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.4260
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioRecorderDelegate.27004
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioRouteChangeMonitorDelegate.21127
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.16426
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.16581
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.17253
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.18076
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.20086
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.27423
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.30317
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.6288
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.6389
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.7121
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionControllerDelegate.28250
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionControllerDelegate.28443
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionInfoProviding.25113
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProviding.27424
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.10111
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.11264
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.16427
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.17254
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.19223
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.20087
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.30318
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.4463
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.4866
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.7356
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.8733
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBenchmarkXPCProtocol.22956
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBluetoothWirelessSplitterMonitorDelegate.21128
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSBluetoothWirelessSplitterMonitorDelegate.26740
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.18948
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.24315
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.25549
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerDelegate.28251
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImpl.18949
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImpl.24316
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImplDelegate.25550
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSFallbackAudioSessionReleaseProviding.27005
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSKeywordAnalyzerNDEAPIScoreDelegate.15401
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.13386
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.7534
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.8734
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.9551
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSMediaPlayingMonitorDelegate.17255
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSOpportuneSpeakEventMonitorDelegate.10112
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.20088
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.26741
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.30319
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSPGEndpointAnalyzerDelegate.4867
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSecondPassProgressProviding.20089
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.11463
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.20090
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.5951
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriAudioPlaybackSession.14712
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.10113
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.10893
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.11265
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.13564
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.17256
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.20091
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.26240
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.30320
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.3752
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.4868
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.7933
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSpeakerRecognitionAssetDownloadMonitorDelegate.18249
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemShellStartProviding.14907
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemShellStartProviding.23253
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSTrialAssetDownloadMonitorDelegate.3478
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSUAFDownloadMonitorDelegate.29532
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.29533
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.7122
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.8735
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.10620
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.11464
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.14419
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.21129
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.25787
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.10894
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.18250
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.20092
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVolumeMonitorDelegate.10621
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSXPCClientDelegate.7357
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSXPCClientDelegate.8736
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CoreSpeechXPCProtocol.22618
+ __OBJC_$_PROTOCOL_METHOD_TYPES_EARCaesuraSilencePosteriorGeneratorDelegate.28908
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.12789
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.13108
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.16880
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.17583
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.24487
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.26475
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.28660
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.29145
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.31114
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.17584
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.24488
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.26476
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.28661
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.29146
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10114
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10426
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10622
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10895
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11266
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11465
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1151
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11984
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.12149
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.12508
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1297
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.13387
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.13565
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1440
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14420
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14713
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14908
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15254
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1538
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15402
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15639
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.159
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1604
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.16428
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.16582
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17257
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17402
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1745
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18077
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18251
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18950
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.19224
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.20093
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.20225
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21130
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21406
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21483
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21800
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2240
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22718
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22957
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.23254
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2350
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24317
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24984
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25114
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25176
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25280
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25551
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25788
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26046
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26241
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26742
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27006
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27152
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27425
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27557
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.28252
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.28444
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.28909
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2937
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29534
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29635
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30321
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30813
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30907
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.31057
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3112
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.316
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3256
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3479
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3753
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.393
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4261
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4464
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4869
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5567
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.571
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5952
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6175
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6289
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6390
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7123
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7358
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7535
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7597
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7934
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8147
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8275
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8737
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9195
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9288
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9552
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.12790
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.13109
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.16881
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.17585
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.24489
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.26477
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.28662
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.29147
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SNResultsObserving.8148
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SSRSpeakerRecognitionControllerDelegate.8738
+ __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.20094
+ __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.3754
+ __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.4870
+ __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.7124
+ __OBJC_$_PROTOCOL_REFS_CSAssetManagerDelegate.24318
+ __OBJC_$_PROTOCOL_REFS_CSAttSiriMitigationAssetHandlerDelegate.26743
+ __OBJC_$_PROTOCOL_REFS_CSAudioConverterDelegate.12150
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.12151
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.12509
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.1746
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.22958
+ __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.4262
+ __OBJC_$_PROTOCOL_REFS_CSAudioRecorderDelegate.27007
+ __OBJC_$_PROTOCOL_REFS_CSAudioRouteChangeMonitorDelegate.21131
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.16429
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.16583
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.17258
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.18078
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.20095
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.27426
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.30322
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.6290
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.6391
+ __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.7125
+ __OBJC_$_PROTOCOL_REFS_CSAudioSessionControllerDelegate.28253
+ __OBJC_$_PROTOCOL_REFS_CSAudioSessionControllerDelegate.28445
+ __OBJC_$_PROTOCOL_REFS_CSAudioSessionInfoProviding.25115
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProviding.27427
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.10115
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.11267
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.16430
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.17259
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.19225
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.20096
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.30323
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.4465
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.4871
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.7359
+ __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.8739
+ __OBJC_$_PROTOCOL_REFS_CSBluetoothWirelessSplitterMonitorDelegate.21132
+ __OBJC_$_PROTOCOL_REFS_CSBluetoothWirelessSplitterMonitorDelegate.26744
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.18951
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.24319
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.25552
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerDelegate.28254
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImpl.18952
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImpl.24320
+ __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImplDelegate.25553
+ __OBJC_$_PROTOCOL_REFS_CSFallbackAudioSessionReleaseProviding.27008
+ __OBJC_$_PROTOCOL_REFS_CSKeywordAnalyzerNDEAPIScoreDelegate.15403
+ __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.13388
+ __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.7536
+ __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.8740
+ __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.9553
+ __OBJC_$_PROTOCOL_REFS_CSMediaPlayingMonitorDelegate.17260
+ __OBJC_$_PROTOCOL_REFS_CSOpportuneSpeakEventMonitorDelegate.10116
+ __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.20097
+ __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.26745
+ __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.30324
+ __OBJC_$_PROTOCOL_REFS_CSSPGEndpointAnalyzerDelegate.4872
+ __OBJC_$_PROTOCOL_REFS_CSSecondPassProgressProviding.20098
+ __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.11466
+ __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.20099
+ __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.5953
+ __OBJC_$_PROTOCOL_REFS_CSSiriAudioPlaybackSession.14714
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.10117
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.10896
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.11268
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.13566
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.17261
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.20100
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.26242
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.30325
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.3755
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.4873
+ __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.7935
+ __OBJC_$_PROTOCOL_REFS_CSSpeakerRecognitionAssetDownloadMonitorDelegate.18252
+ __OBJC_$_PROTOCOL_REFS_CSSpeechManagerDelegate.31058
+ __OBJC_$_PROTOCOL_REFS_CSSystemShellStartProviding.14909
+ __OBJC_$_PROTOCOL_REFS_CSSystemShellStartProviding.23255
+ __OBJC_$_PROTOCOL_REFS_CSTrialAssetDownloadMonitorDelegate.3480
+ __OBJC_$_PROTOCOL_REFS_CSUAFDownloadMonitorDelegate.29535
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.29536
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.7126
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.8741
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.10623
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.11467
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.14421
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.21133
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.25789
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.10897
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.18253
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.20101
+ __OBJC_$_PROTOCOL_REFS_CSVolumeMonitorDelegate.10624
+ __OBJC_$_PROTOCOL_REFS_CSXPCClientDelegate.7360
+ __OBJC_$_PROTOCOL_REFS_CSXPCClientDelegate.8742
+ __OBJC_$_PROTOCOL_REFS_EARCaesuraSilencePosteriorGeneratorDelegate.28910
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.12791
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.13110
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.16882
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.17586
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.24490
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.26478
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.28663
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding.29148
+ __OBJC_$_PROTOCOL_REFS_SNResultsObserving.8149
+ __OBJC_$_PROTOCOL_REFS_SSRSpeakerRecognitionControllerDelegate.8743
+ __OBJC_CLASS_RO_$_CSAudioInjectionProviderExclave
+ __OBJC_CLASS_RO_$_SecureSpeakerRecognitionConfigBridge
+ __OBJC_CLASS_RO_$_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_CLASS_RO_$_SecureVoiceTriggerSpeakerRecognitionDecoder
+ __OBJC_METACLASS_RO_$_CSAudioInjectionProviderExclave
+ __OBJC_METACLASS_RO_$_SecureSpeakerRecognitionConfigBridge
+ __OBJC_METACLASS_RO_$_SecureSpeakerRecognitionPhraseConfigBridge
+ __OBJC_METACLASS_RO_$_SecureVoiceTriggerSpeakerRecognitionDecoder
+ ___104+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:completion:]_block_invoke.13
+ ___106+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:completion:]_block_invoke.16
+ ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.588
+ ___110-[CSVoiceTriggerSecondPass _requestStartAudioStreamWitContext:audioProviderUUID:startStreamOption:completion:]_block_invoke.502
+ ___112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.545
+ ___113-[CSVoiceTriggerFirstPassJarvis _handleJarvisVoiceTriggerFromDeviceId:activationInfo:triggerHostTime:completion:]_block_invoke.452
+ ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.526
+ ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.535
+ ___133-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.524
+ ___136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.540
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.592
+ ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.593
+ ___160-[CSVoiceTriggerFirstPassHearst initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:]_block_invoke
+ ___30-[CSBuiltInVoiceTrigger start]_block_invoke.460
+ ___30-[CSBuiltInVoiceTrigger start]_block_invoke.468
+ ___30-[CSBuiltInVoiceTrigger start]_block_invoke_2.471
+ ___39-[CSBuiltInVoiceTrigger _stopListening]_block_invoke.519
+ ___40-[CSAudioInjectionProviderExclave start]_block_invoke
+ ___40-[CSHybridEndpointer processTaskString:]_block_invoke.530
+ ___40-[CSVoiceTriggerEventsCoordinator start]_block_invoke.428
+ ___41-[CSSmartSiriVolume startSmartSiriVolume]_block_invoke.473
+ ___42-[CSSpeechController _startPhaticDecision]_block_invoke.735
+ ___42-[CSSpeechController _startPhaticDecision]_block_invoke.738
+ ___42-[CSSpeechController _startPhaticDecision]_block_invoke.739
+ ___44-[CSBuiltInVoiceTrigger _stopAPVoiceTrigger]_block_invoke.523
+ ___46-[CSBuiltInVoiceTrigger _startAOPVoiceTrigger]_block_invoke
+ ___46-[CSBuiltInVoiceTrigger _startAOPVoiceTrigger]_block_invoke_2
+ ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.562
+ ___48+[CSAudioInjectionServices pingpong:completion:]_block_invoke.4
+ ___48+[CSAudioInjectionServices pingpong:completion:]_block_invoke.8
+ ___48-[CSSpeechController CSXPCClient:didDisconnect:]_block_invoke.804
+ ___49+[CSAudioInjectionProviderExclave sharedInstance]_block_invoke
+ ___49-[CSVoiceTriggerFirstPassHearstAP _stopListening]_block_invoke.453
+ ___49-[CSVoiceTriggerFirstPassJarvisAP _stopListening]_block_invoke.446
+ ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.652
+ ___50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.485
+ ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.514
+ ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke_2.515
+ ___52-[CSBuiltInVoiceTrigger updateExclaveKitSiriLocale:]_block_invoke
+ ___52-[CSSelfTriggerDetector _startListenWithCompletion:]_block_invoke.442
+ ___52-[CSSpeechController setCurrentRecordContext:error:]_block_invoke.673
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.460
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.466
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.467
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.471
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.478
+ ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.479
+ ___54-[CSSelfTriggerDetector _stopListeningWithCompletion:]_block_invoke.443
+ ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.642
+ ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.651
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.702
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.710
+ ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke_2.711
+ ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.662
+ ___56-[CSVoiceTriggerFidesClient voiceTriggerGotSuperVector:]_block_invoke.469
+ ___60-[CSSpeechController handleStopRecordingRequestWithOptions:]_block_invoke.741
+ ___61+[CSAudioInjectionServices connectDeviceWithUUID:completion:]_block_invoke.19
+ ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.496
+ ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.497
+ ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.498
+ ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.499
+ ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.503
+ ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.508
+ ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2.504
+ ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.541
+ ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.544
+ ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.545
+ ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.548
+ ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.553
+ ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.557
+ ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke_2.546
+ ___61-[CSNNVADEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke.430
+ ___61-[SecureSpeakerRecognitionConfigBridge iteratePhraseConfigs:]_block_invoke
+ ___62-[CSHybridEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke.489
+ ___62-[CSSpeechController _scheduleAudibleFeedbackAtStartRecording]_block_invoke.723
+ ___62-[CSSpeechController _scheduleAudibleFeedbackAtStartRecording]_block_invoke.726
+ ___62-[CSVoiceTriggerFirstPassJarvisAP _startListenWithCompletion:]_block_invoke.444
+ ___64+[CSAudioInjectionServices disconnectDeviceWithUUID:completion:]_block_invoke.21
+ ___64-[CSSmartSiriVolume _startListenPollingWithInterval:completion:]_block_invoke.478
+ ___64-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke
+ ___64-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke.644
+ ___65+[CSAudioInjectionServices primaryInputDeviceUUIDWithCompletion:]_block_invoke.23
+ ___66-[CSSiriSpeechRecorder _prepareSpeechControllerWithOptions:error:]_block_invoke.483
+ ___67-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke.433
+ ___67-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke.438
+ ___67-[SecureVoiceTriggerSpeakerRecognitionDecoder _decodePhraseConfig:]_block_invoke
+ ___68-[CSBuiltInVoiceTrigger _startListenPollingWithInterval:completion:]_block_invoke.509
+ ___68-[CSSelfTriggerDetector _startListenPollingWithInterval:completion:]_block_invoke.434
+ ___70-[CSAudioInjectionProviderExclave speakAudioInExclave:withCompletion:]_block_invoke
+ ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.663
+ ___72-[CSAudioInjectionProviderExclave _readAudioBufferAndFeedIntoAudioQueue]_block_invoke
+ ___72-[CSVoiceTriggerFirstPassJarvis _handleSecondPassResult:deviceId:error:]_block_invoke.469
+ ___72-[CSVoiceTriggerFirstPassJarvis _handleSecondPassResult:deviceId:error:]_block_invoke.470
+ ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.651
+ ___75-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:]_block_invoke.634
+ ___76-[CSEnhancedEndpointer didEndpointWithFeatures:audioTimestampMs:completion:]_block_invoke.164
+ ___77-[CSBuiltInVoiceTrigger activationEventNotificationHandler:event:completion:]_block_invoke.562
+ ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.534
+ ___77-[CSSpeechManager CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke.497
+ ___79-[CSVoiceProfileRetrainManager CSVoiceTriggerEnabledMonitor:didReceiveEnabled:]_block_invoke.438
+ ___80-[CSVoiceTriggerFirstPassHearstAP _startListenWithAudioProviderUUID:completion:]_block_invoke.449
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.653
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.654
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.656
+ ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.664
+ ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.517
+ ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.518
+ ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.525
+ ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.608
+ ___84-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke.449
+ ___84-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke.451
+ ___85-[CSVoiceTriggerFirstPassRemora activationEventNotificationHandler:event:completion:]_block_invoke.541
+ ___85-[CSVoiceTriggerFirstPassRemora activationEventNotificationHandler:event:completion:]_block_invoke.543
+ ___87-[CSVoiceTriggerFirstPassHearstAP _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:]_block_invoke.467
+ ___88-[CSHybridEndpointAnalyzer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke.492
+ ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.601
+ ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.604
+ ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.607
+ ___88-[CSVoiceTriggerAlwaysOnProcessor disableVoiceTriggerOnAlwaysOnProcessorWithCompletion:]_block_invoke.16
+ ___88-[CSVoiceTriggerFirstPassHearst CSPhoneCallStateMonitor:didRecievePhoneCallStateChange:]_block_invoke
+ ___88-[CSVoiceTriggerFirstPassRemora _handleRemoraTriggerEvent:secondPassRequest:completion:]_block_invoke.552
+ ___93-[CSVoiceTriggerAlwaysOnProcessor enableVoiceTriggerOnAlwaysOnProcessorWithAsset:completion:]_block_invoke.14
+ ___93-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromAOP:audioProviderUUID:completion:]_block_invoke.552
+ ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.551
+ ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.553
+ ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.554
+ ___95+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withfadingTimeWindowLength:completion:]_block_invoke.15
+ ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.513
+ ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.521
+ ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke_2.523
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.620
+ ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.621
+ ___97-[CSVoiceTriggerSecondPass _handleVoiceTriggerFirstPassFromExclave:audioProviderUUID:completion:]_block_invoke.508
+ ___Block_byref_object_copy_.10263
+ ___Block_byref_object_copy_.10792
+ ___Block_byref_object_copy_.11912
+ ___Block_byref_object_copy_.13302
+ ___Block_byref_object_copy_.13693
+ ___Block_byref_object_copy_.14313
+ ___Block_byref_object_copy_.15206
+ ___Block_byref_object_copy_.1576
+ ___Block_byref_object_copy_.16060
+ ___Block_byref_object_copy_.16185
+ ___Block_byref_object_copy_.18152
+ ___Block_byref_object_copy_.18748
+ ___Block_byref_object_copy_.20188
+ ___Block_byref_object_copy_.20445
+ ___Block_byref_object_copy_.21679
+ ___Block_byref_object_copy_.22141
+ ___Block_byref_object_copy_.22864
+ ___Block_byref_object_copy_.2288
+ ___Block_byref_object_copy_.23635
+ ___Block_byref_object_copy_.24091
+ ___Block_byref_object_copy_.24729
+ ___Block_byref_object_copy_.25627
+ ___Block_byref_object_copy_.25957
+ ___Block_byref_object_copy_.26594
+ ___Block_byref_object_copy_.26916
+ ___Block_byref_object_copy_.27954
+ ___Block_byref_object_copy_.28370
+ ___Block_byref_object_copy_.2907
+ ___Block_byref_object_copy_.29452
+ ___Block_byref_object_copy_.29882
+ ___Block_byref_object_copy_.30759
+ ___Block_byref_object_copy_.3926
+ ___Block_byref_object_copy_.4064
+ ___Block_byref_object_copy_.4174
+ ___Block_byref_object_copy_.453
+ ___Block_byref_object_copy_.4747
+ ___Block_byref_object_copy_.6688
+ ___Block_byref_object_copy_.7023
+ ___Block_byref_object_copy_.7735
+ ___Block_byref_object_copy_.8526
+ ___Block_byref_object_copy_.9124
+ ___Block_byref_object_dispose_.10264
+ ___Block_byref_object_dispose_.10793
+ ___Block_byref_object_dispose_.11913
+ ___Block_byref_object_dispose_.13303
+ ___Block_byref_object_dispose_.13694
+ ___Block_byref_object_dispose_.14314
+ ___Block_byref_object_dispose_.15207
+ ___Block_byref_object_dispose_.1577
+ ___Block_byref_object_dispose_.16061
+ ___Block_byref_object_dispose_.16186
+ ___Block_byref_object_dispose_.18153
+ ___Block_byref_object_dispose_.18749
+ ___Block_byref_object_dispose_.20189
+ ___Block_byref_object_dispose_.20446
+ ___Block_byref_object_dispose_.21680
+ ___Block_byref_object_dispose_.22142
+ ___Block_byref_object_dispose_.22865
+ ___Block_byref_object_dispose_.2289
+ ___Block_byref_object_dispose_.23636
+ ___Block_byref_object_dispose_.24092
+ ___Block_byref_object_dispose_.24730
+ ___Block_byref_object_dispose_.25628
+ ___Block_byref_object_dispose_.25958
+ ___Block_byref_object_dispose_.26595
+ ___Block_byref_object_dispose_.26917
+ ___Block_byref_object_dispose_.27955
+ ___Block_byref_object_dispose_.28371
+ ___Block_byref_object_dispose_.2908
+ ___Block_byref_object_dispose_.29453
+ ___Block_byref_object_dispose_.29883
+ ___Block_byref_object_dispose_.30760
+ ___Block_byref_object_dispose_.3927
+ ___Block_byref_object_dispose_.4065
+ ___Block_byref_object_dispose_.4175
+ ___Block_byref_object_dispose_.454
+ ___Block_byref_object_dispose_.4748
+ ___Block_byref_object_dispose_.6689
+ ___Block_byref_object_dispose_.7024
+ ___Block_byref_object_dispose_.7736
+ ___Block_byref_object_dispose_.8527
+ ___Block_byref_object_dispose_.9125
+ ___CSSecureLogInitIfNeeded_block_invoke
+ ___MobileTimerLibraryCore_block_invoke.937
+ ___block_descriptor_40_e8_32bs_e59_v32?0"SecureSpeakerRecognitionPhraseConfigBridge"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e29_v32?0"NSDictionary"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e37_v36?0"NSData"8I16I20I24"NSError"28ls32l8
+ ___block_descriptor_40_e8_32w_e17_v16?0"NSError"8lw32l8
+ ___block_descriptor_48_e8_32r40r_e11_v24?0Q8Q16lr32l8r40l8
+ ___block_descriptor_48_e8_32s_e29_v56?0Q8d16f24f28I32f36Q40Q48ls32l8
+ ___block_descriptor_49_e8_32s40bs_e32_v60?0I8Q12d20f28f32I36f40Q44Q52ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48r_e17_v16?0"NSError"8lr48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e8_v16?0Q8ls32l8s40l8
+ ___block_descriptor_80_e8_32r40r48r56r64r72r_e36_v16?0"CSEnhancedEndpointerResult"8lr32l8r40l8r48l8r56l8r64l8r72l8
+ ___block_literal_global.10.10953
+ ___block_literal_global.10.23264
+ ___block_literal_global.10.24606
+ ___block_literal_global.10367
+ ___block_literal_global.10565
+ ___block_literal_global.10825
+ ___block_literal_global.1092
+ ___block_literal_global.10979
+ ___block_literal_global.1106
+ ___block_literal_global.11164
+ ___block_literal_global.11372
+ ___block_literal_global.11771
+ ___block_literal_global.11938
+ ___block_literal_global.12217
+ ___block_literal_global.12317
+ ___block_literal_global.12437
+ ___block_literal_global.1256
+ ___block_literal_global.12730
+ ___block_literal_global.12835
+ ___block_literal_global.12889
+ ___block_literal_global.13.23436
+ ___block_literal_global.13.24607
+ ___block_literal_global.13017
+ ___block_literal_global.13053
+ ___block_literal_global.13495
+ ___block_literal_global.13607
+ ___block_literal_global.13852
+ ___block_literal_global.1398
+ ___block_literal_global.14225
+ ___block_literal_global.14334
+ ___block_literal_global.14746
+ ___block_literal_global.14793
+ ___block_literal_global.14862
+ ___block_literal_global.14916
+ ___block_literal_global.14934
+ ___block_literal_global.1497
+ ___block_literal_global.15.14794
+ ___block_literal_global.15045
+ ___block_literal_global.15596
+ ___block_literal_global.15681
+ ___block_literal_global.16.14747
+ ___block_literal_global.16.23265
+ ___block_literal_global.16158
+ ___block_literal_global.16169
+ ___block_literal_global.16214
+ ___block_literal_global.16536
+ ___block_literal_global.1680
+ ___block_literal_global.17.23367
+ ___block_literal_global.17142
+ ___block_literal_global.17470
+ ___block_literal_global.17648
+ ___block_literal_global.17657
+ ___block_literal_global.17740
+ ___block_literal_global.17774
+ ___block_literal_global.18.15015
+ ___block_literal_global.18.23437
+ ___block_literal_global.18029
+ ___block_literal_global.18105
+ ___block_literal_global.18203
+ ___block_literal_global.18302
+ ___block_literal_global.19034
+ ___block_literal_global.19081
+ ___block_literal_global.191
+ ___block_literal_global.19286
+ ___block_literal_global.19316
+ ___block_literal_global.19929
+ ___block_literal_global.20.28353
+ ___block_literal_global.20197
+ ___block_literal_global.20732
+ ___block_literal_global.20799
+ ___block_literal_global.21.12836
+ ___block_literal_global.21072
+ ___block_literal_global.21153
+ ___block_literal_global.21202
+ ___block_literal_global.21247
+ ___block_literal_global.21263
+ ___block_literal_global.2140
+ ___block_literal_global.21554
+ ___block_literal_global.21843
+ ___block_literal_global.22.23266
+ ___block_literal_global.22057
+ ___block_literal_global.22163
+ ___block_literal_global.22175
+ ___block_literal_global.22253
+ ___block_literal_global.22429
+ ___block_literal_global.22476
+ ___block_literal_global.22675
+ ___block_literal_global.22847
+ ___block_literal_global.2307
+ ___block_literal_global.23152
+ ___block_literal_global.23208
+ ___block_literal_global.23263
+ ___block_literal_global.23337
+ ___block_literal_global.23366
+ ___block_literal_global.23456
+ ___block_literal_global.23541
+ ___block_literal_global.23581
+ ___block_literal_global.23708
+ ___block_literal_global.24.29480
+ ___block_literal_global.24604
+ ___block_literal_global.25.23267
+ ___block_literal_global.2502
+ ___block_literal_global.25065
+ ___block_literal_global.25237
+ ___block_literal_global.2548
+ ___block_literal_global.25730
+ ___block_literal_global.26.28342
+ ___block_literal_global.2610
+ ___block_literal_global.26286
+ ___block_literal_global.26340
+ ___block_literal_global.2657
+ ___block_literal_global.26617
+ ___block_literal_global.26689
+ ___block_literal_global.26844
+ ___block_literal_global.27.12837
+ ___block_literal_global.27170
+ ___block_literal_global.2758
+ ___block_literal_global.2772
+ ___block_literal_global.28.17998
+ ___block_literal_global.28059
+ ___block_literal_global.28394
+ ___block_literal_global.28750
+ ___block_literal_global.29.23268
+ ___block_literal_global.29.23368
+ ___block_literal_global.29155
+ ___block_literal_global.29204
+ ___block_literal_global.29241
+ ___block_literal_global.29280
+ ___block_literal_global.29485
+ ___block_literal_global.29584
+ ___block_literal_global.29735
+ ___block_literal_global.29844
+ ___block_literal_global.2987
+ ___block_literal_global.29943
+ ___block_literal_global.30.12838
+ ___block_literal_global.3008
+ ___block_literal_global.30499
+ ___block_literal_global.30684
+ ___block_literal_global.3069
+ ___block_literal_global.30770
+ ___block_literal_global.31139
+ ___block_literal_global.3161
+ ___block_literal_global.3212
+ ___block_literal_global.3433
+ ___block_literal_global.36.12839
+ ___block_literal_global.3640
+ ___block_literal_global.38.9368
+ ___block_literal_global.3809
+ ___block_literal_global.39.12840
+ ___block_literal_global.3976
+ ___block_literal_global.4054
+ ___block_literal_global.42.12841
+ ___block_literal_global.4211
+ ___block_literal_global.433
+ ___block_literal_global.438
+ ___block_literal_global.439
+ ___block_literal_global.44.16488
+ ___block_literal_global.441
+ ___block_literal_global.441.12205
+ ___block_literal_global.443
+ ___block_literal_global.444
+ ___block_literal_global.445
+ ___block_literal_global.446
+ ___block_literal_global.446.20953
+ ___block_literal_global.447
+ ___block_literal_global.46.9360
+ ___block_literal_global.469
+ ___block_literal_global.470
+ ___block_literal_global.471
+ ___block_literal_global.472
+ ___block_literal_global.474
+ ___block_literal_global.496
+ ___block_literal_global.499
+ ___block_literal_global.5.31140
+ ___block_literal_global.5161
+ ___block_literal_global.5181
+ ___block_literal_global.53.22825
+ ___block_literal_global.530
+ ___block_literal_global.561
+ ___block_literal_global.6132
+ ___block_literal_global.6242
+ ___block_literal_global.6342
+ ___block_literal_global.6525
+ ___block_literal_global.658
+ ___block_literal_global.6629
+ ___block_literal_global.6652
+ ___block_literal_global.67.2645
+ ___block_literal_global.67.8950
+ ___block_literal_global.6726
+ ___block_literal_global.683
+ ___block_literal_global.7.24605
+ ___block_literal_global.7.948
+ ___block_literal_global.7077
+ ___block_literal_global.7219
+ ___block_literal_global.729
+ ___block_literal_global.7486
+ ___block_literal_global.7786
+ ___block_literal_global.792
+ ___block_literal_global.8.29578
+ ___block_literal_global.8.29944
+ ___block_literal_global.8.31141
+ ___block_literal_global.856
+ ___block_literal_global.8697
+ ___block_literal_global.9245
+ ___block_literal_global.9399
+ ___block_literal_global.9451
+ ___block_literal_global.9568
+ ___block_literal_global.960
+ ___block_literal_global.9999
+ __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.19891
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.11139
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.19883
+ __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.30141
+ __unnamed_array_storage.1244
+ __unnamed_array_storage.165.24852
+ __unnamed_array_storage.176.24828
+ __unnamed_array_storage.177.24829
+ __unnamed_array_storage.21.28980
+ __unnamed_array_storage.22491
+ __unnamed_array_storage.22889
+ __unnamed_array_storage.23545
+ __unnamed_array_storage.24860
+ __unnamed_array_storage.27969
+ __unnamed_array_storage.28989
+ __unnamed_array_storage.38.23546
+ __unnamed_array_storage.641
+ __unnamed_array_storage.648
+ __unnamed_array_storage.649
+ __unnamed_array_storage.6571
+ __unnamed_array_storage.6713
+ __unnamed_array_storage.7790
+ _audit_stringMobileTimer.940
+ _kCFRunLoopCommonModes
+ _kVTEISecondPassRejectionMHUUID_block_invoke.enableHeartbeat.11160
+ _kVTEISecondPassRejectionMHUUID_block_invoke.enableHeartbeat.30202
+ _objc_msgSend$_alertBehaviorForRecordRoute:playbackRoute:recordingInfo:speechEvent:activationMode:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usesDeviceSpeakerForTTS:attemptsToUsePastDataBufferFrames:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isDeviceInCarDNDMode:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:
+ _objc_msgSend$_calculateRecordingTimeForAOPTriggerFromFirstPassInfo:completion:
+ _objc_msgSend$_createAudioQueueIfNeeded
+ _objc_msgSend$_decodePhraseConfig:
+ _objc_msgSend$_defaultBufferRef
+ _objc_msgSend$_getBooleanValue:forKey:withDefaultValue:
+ _objc_msgSend$_getExclaveAudioTimeConverter
+ _objc_msgSend$_getFloatValue:forKey:withDefaultValue:
+ _objc_msgSend$_getIntValue:forKey:withDefaultValue:
+ _objc_msgSend$_prepareAndStartAudioQueue
+ _objc_msgSend$_readAudioBufferAndFeedIntoAudioQueue
+ _objc_msgSend$_setAudioSessionActive:
+ _objc_msgSend$_updateCurrentAsset:
+ _objc_msgSend$_updateExclaveKitSiriLocale:
+ _objc_msgSend$alwaysOnProcessorController
+ _objc_msgSend$cString
+ _objc_msgSend$category
+ _objc_msgSend$configAOPVoiceTrigger
+ _objc_msgSend$defaultExclaveConverter
+ _objc_msgSend$didForceEndpoint
+ _objc_msgSend$enableExclaveAudioInjection:
+ _objc_msgSend$exclaveAudioInjectionEnabled
+ _objc_msgSend$extractPSRVoiceProfileWithContext:completion:
+ _objc_msgSend$extractSATVoiceProfileWithContext:completion:
+ _objc_msgSend$fetchAOPVoiceTriggerResult:
+ _objc_msgSend$generatePHashFromExclaveVoiceTriggerInfo:writeFile:
+ _objc_msgSend$getBool:category:defaultValue:
+ _objc_msgSend$getDictionaryArray:category:
+ _objc_msgSend$getFloat:category:defaultValue:
+ _objc_msgSend$getString:category:defaultValue:
+ _objc_msgSend$getUnsignedLongLongValue:category:defaultValue:
+ _objc_msgSend$initWithName:satThreshold:
+ _objc_msgSend$initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:
+ _objc_msgSend$isFirstPassSourceTypeRingtoneWithVTEI:
+ _objc_msgSend$isSiriDSPTurnedOn
+ _objc_msgSend$isVoiceTriggerFromExclaveWithVTEI:
+ _objc_msgSend$setCategory:mode:options:error:
+ _objc_msgSend$setCombinationWeight:
+ _objc_msgSend$setDidForceEndpoint:
+ _objc_msgSend$setImplicitProfileDeltaThreshold:
+ _objc_msgSend$setImplicitProfileThreshold:
+ _objc_msgSend$setImplicitTrainingEnabled:
+ _objc_msgSend$setImplicitVTThreshold:
+ _objc_msgSend$setMaxEnrollmentUtterances:
+ _objc_msgSend$setMultiUserConfidentScoreThreshold:
+ _objc_msgSend$setMultiUserDeltaScoreThreshold:
+ _objc_msgSend$setMultiUserHighScoreThreshold:
+ _objc_msgSend$setMultiUserLowScoreThreshold:
+ _objc_msgSend$setNumPruningRetentionUtt:
+ _objc_msgSend$setPhraseConfigs:
+ _objc_msgSend$setPruningExplicitPSRThreshold:
+ _objc_msgSend$setPruningExplicitSATThreshold:
+ _objc_msgSend$setPruningPSRThreshold:
+ _objc_msgSend$setPruningSATThreshold:
+ _objc_msgSend$setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:
+ _objc_msgSend$setUseTDTIEnrollment:
+ _objc_msgSend$startSecondPassVoiceTriggerWithFirstPassSource:phsEnabled:supportMultiPhrase:
+ _objc_msgSend$updateExclaveKitSiriLocale:
+ _sharedController.onceToken.11937
+ _sharedController.sharedController.11939
+ _sharedHandler.onceToken.1255
+ _sharedHandler.onceToken.20731
+ _sharedHandler.onceToken.29484
+ _sharedHandler.onceToken.6725
+ _sharedHandler.sharedHandler.1257
+ _sharedHandler.sharedHandler.20733
+ _sharedHandler.sharedHandler.29486
+ _sharedHandler.sharedHandler.6727
+ _sharedHandlerDisabledOnDeviceCompilation.onceToken.29479
+ _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.29481
+ _sharedInstance._sharedInstance.11772
+ _sharedInstance._sharedInstance.13054
+ _sharedInstance._sharedInstance.14863
+ _sharedInstance._sharedInstance.15046
+ _sharedInstance._sharedInstance.16537
+ _sharedInstance._sharedInstance.17471
+ _sharedInstance._sharedInstance.17741
+ _sharedInstance._sharedInstance.18030
+ _sharedInstance._sharedInstance.18106
+ _sharedInstance._sharedInstance.18303
+ _sharedInstance._sharedInstance.19035
+ _sharedInstance._sharedInstance.19287
+ _sharedInstance._sharedInstance.21203
+ _sharedInstance._sharedInstance.21844
+ _sharedInstance._sharedInstance.22058
+ _sharedInstance._sharedInstance.22254
+ _sharedInstance._sharedInstance.22676
+ _sharedInstance._sharedInstance.23209
+ _sharedInstance._sharedInstance.2549
+ _sharedInstance._sharedInstance.26287
+ _sharedInstance._sharedInstance.26341
+ _sharedInstance._sharedInstance.27171
+ _sharedInstance._sharedInstance.29205
+ _sharedInstance._sharedInstance.29242
+ _sharedInstance._sharedInstance.29736
+ _sharedInstance._sharedInstance.2988
+ _sharedInstance._sharedInstance.30685
+ _sharedInstance._sharedInstance.3070
+ _sharedInstance._sharedInstance.30771
+ _sharedInstance._sharedInstance.3213
+ _sharedInstance._sharedInstance.3434
+ _sharedInstance._sharedInstance.6133
+ _sharedInstance._sharedInstance.6243
+ _sharedInstance._sharedInstance.6343
+ _sharedInstance._sharedInstance.6630
+ _sharedInstance._sharedInstance.684
+ _sharedInstance._sharedInstance.7220
+ _sharedInstance._sharedInstance.793
+ _sharedInstance._sharedInstance.857
+ _sharedInstance._sharedInstance.9246
+ _sharedInstance._sharedInstance.9452
+ _sharedInstance._sharedInstance.961
+ _sharedInstance.onceToken.10564
+ _sharedInstance.onceToken.10824
+ _sharedInstance.onceToken.10978
+ _sharedInstance.onceToken.11770
+ _sharedInstance.onceToken.12888
+ _sharedInstance.onceToken.13016
+ _sharedInstance.onceToken.13052
+ _sharedInstance.onceToken.13606
+ _sharedInstance.onceToken.1397
+ _sharedInstance.onceToken.14861
+ _sharedInstance.onceToken.1496
+ _sharedInstance.onceToken.15044
+ _sharedInstance.onceToken.15595
+ _sharedInstance.onceToken.15680
+ _sharedInstance.onceToken.16157
+ _sharedInstance.onceToken.16535
+ _sharedInstance.onceToken.17469
+ _sharedInstance.onceToken.17739
+ _sharedInstance.onceToken.18028
+ _sharedInstance.onceToken.18104
+ _sharedInstance.onceToken.18202
+ _sharedInstance.onceToken.18301
+ _sharedInstance.onceToken.190
+ _sharedInstance.onceToken.19033
+ _sharedInstance.onceToken.19080
+ _sharedInstance.onceToken.19285
+ _sharedInstance.onceToken.19315
+ _sharedInstance.onceToken.21071
+ _sharedInstance.onceToken.21152
+ _sharedInstance.onceToken.21201
+ _sharedInstance.onceToken.21553
+ _sharedInstance.onceToken.21842
+ _sharedInstance.onceToken.22056
+ _sharedInstance.onceToken.22252
+ _sharedInstance.onceToken.22428
+ _sharedInstance.onceToken.22674
+ _sharedInstance.onceToken.23151
+ _sharedInstance.onceToken.23207
+ _sharedInstance.onceToken.23336
+ _sharedInstance.onceToken.23455
+ _sharedInstance.onceToken.23580
+ _sharedInstance.onceToken.23707
+ _sharedInstance.onceToken.25064
+ _sharedInstance.onceToken.25236
+ _sharedInstance.onceToken.2547
+ _sharedInstance.onceToken.25729
+ _sharedInstance.onceToken.2609
+ _sharedInstance.onceToken.26285
+ _sharedInstance.onceToken.26339
+ _sharedInstance.onceToken.26688
+ _sharedInstance.onceToken.26843
+ _sharedInstance.onceToken.27169
+ _sharedInstance.onceToken.28749
+ _sharedInstance.onceToken.29203
+ _sharedInstance.onceToken.29240
+ _sharedInstance.onceToken.29279
+ _sharedInstance.onceToken.29734
+ _sharedInstance.onceToken.2986
+ _sharedInstance.onceToken.3007
+ _sharedInstance.onceToken.30498
+ _sharedInstance.onceToken.3068
+ _sharedInstance.onceToken.30683
+ _sharedInstance.onceToken.30769
+ _sharedInstance.onceToken.3160
+ _sharedInstance.onceToken.3211
+ _sharedInstance.onceToken.3432
+ _sharedInstance.onceToken.3808
+ _sharedInstance.onceToken.5160
+ _sharedInstance.onceToken.529
+ _sharedInstance.onceToken.6131
+ _sharedInstance.onceToken.6241
+ _sharedInstance.onceToken.6341
+ _sharedInstance.onceToken.6628
+ _sharedInstance.onceToken.682
+ _sharedInstance.onceToken.7218
+ _sharedInstance.onceToken.791
+ _sharedInstance.onceToken.855
+ _sharedInstance.onceToken.9244
+ _sharedInstance.onceToken.9450
+ _sharedInstance.onceToken.959
+ _sharedInstance.sSharedInstance.19317
+ _sharedInstance.sharedInstance.12890
+ _sharedInstance.sharedInstance.13018
+ _sharedInstance.sharedInstance.13608
+ _sharedInstance.sharedInstance.15682
+ _sharedInstance.sharedInstance.19082
+ _sharedInstance.sharedInstance.21073
+ _sharedInstance.sharedInstance.21154
+ _sharedInstance.sharedInstance.22430
+ _sharedInstance.sharedInstance.23153
+ _sharedInstance.sharedInstance.23338
+ _sharedInstance.sharedInstance.23582
+ _sharedInstance.sharedInstance.25238
+ _sharedInstance.sharedInstance.25731
+ _sharedInstance.sharedInstance.2611
+ _sharedInstance.sharedInstance.26845
+ _sharedInstance.sharedInstance.29281
+ _sharedInstance.sharedInstance.30500
+ _sharedInstance.sharedInstance.3810
+ _sharedInstance.sharedInstance.5162
+ _sharedInstance.sharedManager.21555
+ _sharedInstance.sharedManager.23709
+ _sharedInstance.sharedManager.28751
+ _sharedInstance.sharedPolicy.1399
+ _sharedInstance.sharedPolicy.23457
+ _sharedInstance.sharedPolicy.26690
+ _sharedInstance.sharedProvider.25066
+ _sharedManager.onceToken.17647
+ _sharedManager.onceToken.20196
+ _sharedManager.onceToken.7485
+ _sharedManager.sharedManager.17649
+ _sharedManager.sharedManager.7487
+ _sharedMonitor.onceToken.22162
+ _sharedMonitor.sharedMonitor.22164
+ _sharedService.onceToken.16213
+ _sharedService.onceToken.28393
+ _sharedService.sharedService.28395
- +[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]
- -[CSAggressiveECModeHandler audioSessionStateActive]
- -[CSAggressiveECModeHandler echoCancellationDeferred]
- -[CSAggressiveECModeHandler setAudioSessionStateActive:]
- -[CSAggressiveECModeHandler setEchoCancellationDeferred:]
- -[CSVoiceTriggerFirstPassHearst initWithSpeechManager:voiceTriggerEnabledPolicyHearst:]
- -[CSVoiceTriggerFirstPassHearst setVoicetriggerHearstEnabledPolicy:]
- -[CSVoiceTriggerFirstPassHearst voicetriggerHearstEnabledPolicy]
- -[CSVoiceTriggerHearstEnabledPolicy .cxx_destruct]
- -[CSVoiceTriggerHearstEnabledPolicy CSEventMonitorDidReceiveEvent:]
- -[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]
- -[CSVoiceTriggerHearstEnabledPolicy _subscribeEventMonitors]
- -[CSVoiceTriggerHearstEnabledPolicy initWithSiriRestrictionOnLockScreenMonitor:screenLockMonitor:voiceTriggerEnabledMonitor:CSPhoneCallStateMonitor:otherAppRecordingStateMonitor:siriClientBehaviorMonitor:srfUserSettingsMonitor:]
- -[CSVoiceTriggerHearstEnabledPolicy init]
- -[CSVoiceTriggerHearstEnabledPolicy otherAppRecordingStateMonitor]
- -[CSVoiceTriggerHearstEnabledPolicy phonecallStateMonitor]
- -[CSVoiceTriggerHearstEnabledPolicy screenLockMonitor]
- -[CSVoiceTriggerHearstEnabledPolicy siriClientBehaviorMonitor]
- -[CSVoiceTriggerHearstEnabledPolicy siriRestrictionOnLockScreenMonitor]
- -[CSVoiceTriggerHearstEnabledPolicy voiceTriggerEnabledMonitor]
- GCC_except_table1179
- GCC_except_table1191
- GCC_except_table1220
- GCC_except_table1411
- GCC_except_table145
- GCC_except_table1474
- GCC_except_table1498
- GCC_except_table1502
- GCC_except_table1518
- GCC_except_table1521
- GCC_except_table1549
- GCC_except_table1645
- GCC_except_table1647
- GCC_except_table1649
- GCC_except_table1655
- GCC_except_table1710
- GCC_except_table1742
- GCC_except_table1821
- GCC_except_table1841
- GCC_except_table2032
- GCC_except_table2168
- GCC_except_table2214
- GCC_except_table2217
- GCC_except_table2220
- GCC_except_table2225
- GCC_except_table2237
- GCC_except_table2242
- GCC_except_table2245
- GCC_except_table225
- GCC_except_table2271
- GCC_except_table2275
- GCC_except_table2373
- GCC_except_table2391
- GCC_except_table2523
- GCC_except_table2567
- GCC_except_table2588
- GCC_except_table2591
- GCC_except_table2602
- GCC_except_table2643
- GCC_except_table2644
- GCC_except_table2645
- GCC_except_table2646
- GCC_except_table2647
- GCC_except_table2651
- GCC_except_table2652
- GCC_except_table2655
- GCC_except_table2658
- GCC_except_table2659
- GCC_except_table2662
- GCC_except_table2672
- GCC_except_table2678
- GCC_except_table2680
- GCC_except_table2681
- GCC_except_table3016
- GCC_except_table3102
- GCC_except_table3123
- GCC_except_table3141
- GCC_except_table3154
- GCC_except_table3175
- GCC_except_table3178
- GCC_except_table3181
- GCC_except_table3211
- GCC_except_table327
- GCC_except_table3273
- GCC_except_table3391
- GCC_except_table3495
- GCC_except_table3521
- GCC_except_table3583
- GCC_except_table3585
- GCC_except_table3587
- GCC_except_table3603
- GCC_except_table3605
- GCC_except_table3607
- GCC_except_table3611
- GCC_except_table3613
- GCC_except_table3615
- GCC_except_table3629
- GCC_except_table3635
- GCC_except_table3637
- GCC_except_table3672
- GCC_except_table380
- GCC_except_table381
- GCC_except_table3828
- GCC_except_table383
- GCC_except_table385
- GCC_except_table3852
- GCC_except_table386
- GCC_except_table387
- GCC_except_table3910
- GCC_except_table3945
- GCC_except_table4034
- GCC_except_table410
- GCC_except_table4281
- GCC_except_table4403
- GCC_except_table4426
- GCC_except_table4475
- GCC_except_table4481
- GCC_except_table4712
- GCC_except_table4716
- GCC_except_table4784
- GCC_except_table4790
- GCC_except_table4797
- GCC_except_table4803
- GCC_except_table4872
- GCC_except_table5028
- GCC_except_table5038
- GCC_except_table5062
- GCC_except_table5085
- GCC_except_table5135
- GCC_except_table5147
- GCC_except_table5170
- GCC_except_table5264
- GCC_except_table5276
- GCC_except_table528
- GCC_except_table5285
- GCC_except_table5292
- GCC_except_table5298
- GCC_except_table5300
- GCC_except_table5303
- GCC_except_table5311
- GCC_except_table5313
- GCC_except_table5318
- GCC_except_table5320
- GCC_except_table5331
- GCC_except_table5332
- GCC_except_table5337
- GCC_except_table5343
- GCC_except_table5348
- GCC_except_table5350
- GCC_except_table5352
- GCC_except_table5354
- GCC_except_table5355
- GCC_except_table5357
- GCC_except_table5359
- GCC_except_table5360
- GCC_except_table5361
- GCC_except_table5362
- GCC_except_table5363
- GCC_except_table5366
- GCC_except_table5367
- GCC_except_table5369
- GCC_except_table5384
- GCC_except_table5472
- GCC_except_table5476
- GCC_except_table5530
- GCC_except_table5559
- GCC_except_table5562
- GCC_except_table5757
- GCC_except_table577
- GCC_except_table5773
- GCC_except_table5781
- GCC_except_table5786
- GCC_except_table5803
- GCC_except_table5806
- GCC_except_table5810
- GCC_except_table5813
- GCC_except_table582
- GCC_except_table5823
- GCC_except_table583
- GCC_except_table584
- GCC_except_table588
- GCC_except_table608
- GCC_except_table6086
- GCC_except_table609
- GCC_except_table610
- GCC_except_table6119
- GCC_except_table6155
- GCC_except_table6164
- GCC_except_table6267
- GCC_except_table6273
- GCC_except_table644
- GCC_except_table6510
- GCC_except_table6514
- GCC_except_table6525
- GCC_except_table6547
- GCC_except_table6583
- GCC_except_table6591
- GCC_except_table6621
- GCC_except_table6622
- GCC_except_table6764
- GCC_except_table6819
- GCC_except_table6941
- GCC_except_table6942
- GCC_except_table6952
- GCC_except_table6953
- GCC_except_table696
- GCC_except_table7098
- GCC_except_table7116
- GCC_except_table7120
- GCC_except_table7125
- GCC_except_table7130
- GCC_except_table7137
- GCC_except_table7139
- GCC_except_table716
- GCC_except_table7167
- GCC_except_table7247
- GCC_except_table7270
- GCC_except_table7281
- GCC_except_table7284
- GCC_except_table7307
- GCC_except_table7319
- GCC_except_table7687
- GCC_except_table7697
- GCC_except_table771
- GCC_except_table773
- GCC_except_table7747
- GCC_except_table777
- GCC_except_table782
- GCC_except_table7823
- GCC_except_table7833
- GCC_except_table7835
- GCC_except_table7836
- GCC_except_table7838
- GCC_except_table7845
- GCC_except_table7850
- GCC_except_table7851
- GCC_except_table7855
- GCC_except_table7856
- GCC_except_table7860
- GCC_except_table7861
- GCC_except_table7862
- GCC_except_table7863
- GCC_except_table7865
- GCC_except_table7866
- GCC_except_table7867
- GCC_except_table7868
- GCC_except_table7870
- GCC_except_table7872
- GCC_except_table7873
- GCC_except_table7902
- GCC_except_table7956
- GCC_except_table7980
- GCC_except_table8022
- GCC_except_table8033
- GCC_except_table8179
- GCC_except_table8187
- GCC_except_table8319
- GCC_except_table8411
- GCC_except_table8453
- GCC_except_table8484
- GCC_except_table8498
- GCC_except_table8505
- GCC_except_table8510
- GCC_except_table8525
- _AudioConverterFillComplexBuffer_BlockInvoke.29377
- _MobileTimerLibrary.920
- _MobileTimerLibraryCore.frameworkLibrary.926
- _OBJC_CLASS_$_CSVoiceTriggerHearstEnabledPolicy
- _OBJC_IVAR_$_CSAggressiveECModeHandler._audioSessionStateActive
- _OBJC_IVAR_$_CSAggressiveECModeHandler._echoCancellationDeferred
- _OBJC_IVAR_$_CSVoiceTriggerFirstPassHearst._voicetriggerHearstEnabledPolicy
- _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._otherAppRecordingStateMonitor
- _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._phonecallStateMonitor
- _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._screenLockMonitor
- _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._siriClientBehaviorMonitor
- _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._siriRestrictionOnLockScreenMonitor
- _OBJC_IVAR_$_CSVoiceTriggerHearstEnabledPolicy._voiceTriggerEnabledMonitor
- _OBJC_METACLASS_$_CSVoiceTriggerHearstEnabledPolicy
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.12399
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.12718
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.16625
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.17329
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.24157
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.26146
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.28336
- __OBJC_$_CLASS_PROP_LIST_NSSecureCoding.28821
- __OBJC_$_INSTANCE_METHODS_CSVoiceTriggerHearstEnabledPolicy
- __OBJC_$_INSTANCE_VARIABLES_CSVoiceTriggerHearstEnabledPolicy
- __OBJC_$_PROP_LIST_CSEndpointAnalyzer.18706
- __OBJC_$_PROP_LIST_CSEndpointAnalyzer.23978
- __OBJC_$_PROP_LIST_CSEndpointAnalyzer.25221
- __OBJC_$_PROP_LIST_CSEndpointAnalyzerImpl.18707
- __OBJC_$_PROP_LIST_CSEndpointAnalyzerImpl.23979
- __OBJC_$_PROP_LIST_CSSiriAudioPlaybackSession.14437
- __OBJC_$_PROP_LIST_CSVoiceTriggerHearstEnabledPolicy
- __OBJC_$_PROP_LIST_NSObject.10016
- __OBJC_$_PROP_LIST_NSObject.10207
- __OBJC_$_PROP_LIST_NSObject.10482
- __OBJC_$_PROP_LIST_NSObject.10863
- __OBJC_$_PROP_LIST_NSObject.11063
- __OBJC_$_PROP_LIST_NSObject.1116
- __OBJC_$_PROP_LIST_NSObject.11590
- __OBJC_$_PROP_LIST_NSObject.11749
- __OBJC_$_PROP_LIST_NSObject.12116
- __OBJC_$_PROP_LIST_NSObject.1259
- __OBJC_$_PROP_LIST_NSObject.12995
- __OBJC_$_PROP_LIST_NSObject.13172
- __OBJC_$_PROP_LIST_NSObject.13554
- __OBJC_$_PROP_LIST_NSObject.1402
- __OBJC_$_PROP_LIST_NSObject.14145
- __OBJC_$_PROP_LIST_NSObject.14438
- __OBJC_$_PROP_LIST_NSObject.14633
- __OBJC_$_PROP_LIST_NSObject.14981
- __OBJC_$_PROP_LIST_NSObject.1500
- __OBJC_$_PROP_LIST_NSObject.15127
- __OBJC_$_PROP_LIST_NSObject.153
- __OBJC_$_PROP_LIST_NSObject.15366
- __OBJC_$_PROP_LIST_NSObject.1566
- __OBJC_$_PROP_LIST_NSObject.16168
- __OBJC_$_PROP_LIST_NSObject.16325
- __OBJC_$_PROP_LIST_NSObject.16994
- __OBJC_$_PROP_LIST_NSObject.1705
- __OBJC_$_PROP_LIST_NSObject.17149
- __OBJC_$_PROP_LIST_NSObject.17822
- __OBJC_$_PROP_LIST_NSObject.17995
- __OBJC_$_PROP_LIST_NSObject.18708
- __OBJC_$_PROP_LIST_NSObject.18985
- __OBJC_$_PROP_LIST_NSObject.19837
- __OBJC_$_PROP_LIST_NSObject.19983
- __OBJC_$_PROP_LIST_NSObject.20850
- __OBJC_$_PROP_LIST_NSObject.21133
- __OBJC_$_PROP_LIST_NSObject.21210
- __OBJC_$_PROP_LIST_NSObject.21526
- __OBJC_$_PROP_LIST_NSObject.2202
- __OBJC_$_PROP_LIST_NSObject.22378
- __OBJC_$_PROP_LIST_NSObject.22618
- __OBJC_$_PROP_LIST_NSObject.22917
- __OBJC_$_PROP_LIST_NSObject.2312
- __OBJC_$_PROP_LIST_NSObject.23980
- __OBJC_$_PROP_LIST_NSObject.24662
- __OBJC_$_PROP_LIST_NSObject.24790
- __OBJC_$_PROP_LIST_NSObject.24854
- __OBJC_$_PROP_LIST_NSObject.24958
- __OBJC_$_PROP_LIST_NSObject.25222
- __OBJC_$_PROP_LIST_NSObject.25459
- __OBJC_$_PROP_LIST_NSObject.25718
- __OBJC_$_PROP_LIST_NSObject.25910
- __OBJC_$_PROP_LIST_NSObject.26405
- __OBJC_$_PROP_LIST_NSObject.26670
- __OBJC_$_PROP_LIST_NSObject.26821
- __OBJC_$_PROP_LIST_NSObject.27090
- __OBJC_$_PROP_LIST_NSObject.27226
- __OBJC_$_PROP_LIST_NSObject.2741
- __OBJC_$_PROP_LIST_NSObject.27923
- __OBJC_$_PROP_LIST_NSObject.28119
- __OBJC_$_PROP_LIST_NSObject.28583
- __OBJC_$_PROP_LIST_NSObject.2916
- __OBJC_$_PROP_LIST_NSObject.29207
- __OBJC_$_PROP_LIST_NSObject.29312
- __OBJC_$_PROP_LIST_NSObject.29987
- __OBJC_$_PROP_LIST_NSObject.30489
- __OBJC_$_PROP_LIST_NSObject.30583
- __OBJC_$_PROP_LIST_NSObject.3060
- __OBJC_$_PROP_LIST_NSObject.30735
- __OBJC_$_PROP_LIST_NSObject.311
- __OBJC_$_PROP_LIST_NSObject.3281
- __OBJC_$_PROP_LIST_NSObject.3522
- __OBJC_$_PROP_LIST_NSObject.387
- __OBJC_$_PROP_LIST_NSObject.4028
- __OBJC_$_PROP_LIST_NSObject.4228
- __OBJC_$_PROP_LIST_NSObject.4634
- __OBJC_$_PROP_LIST_NSObject.5223
- __OBJC_$_PROP_LIST_NSObject.5497
- __OBJC_$_PROP_LIST_NSObject.5611
- __OBJC_$_PROP_LIST_NSObject.564
- __OBJC_$_PROP_LIST_NSObject.5946
- __OBJC_$_PROP_LIST_NSObject.6047
- __OBJC_$_PROP_LIST_NSObject.6775
- __OBJC_$_PROP_LIST_NSObject.7011
- __OBJC_$_PROP_LIST_NSObject.7189
- __OBJC_$_PROP_LIST_NSObject.7253
- __OBJC_$_PROP_LIST_NSObject.7588
- __OBJC_$_PROP_LIST_NSObject.7798
- __OBJC_$_PROP_LIST_NSObject.8370
- __OBJC_$_PROP_LIST_NSObject.8831
- __OBJC_$_PROP_LIST_NSObject.8924
- __OBJC_$_PROP_LIST_NSObject.9186
- __OBJC_$_PROP_LIST_NSObject.9704
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.12400
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.12719
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.16626
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.17330
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.24158
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.26147
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.28337
- __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding.28822
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.19838
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.3523
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.4635
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSActivationEventNotificationHandlerDelegate.6776
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAssetManagerDelegate.23981
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAttSiriMitigationAssetHandlerDelegate.26406
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioConverterDelegate.11750
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.11751
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.12117
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.1706
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.22619
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioInjectionEngineDelegate.4029
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioRecorderDelegate.26671
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioRouteChangeMonitorDelegate.20851
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioSessionInfoProviding.24791
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProviding.27091
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.10864
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.16169
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.16995
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.18986
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.19839
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.29988
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.4229
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.4636
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.7012
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.8371
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSAudioStreamProvidingDelegate.9705
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBenchmarkXPCProtocol.22620
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBluetoothWirelessSplitterMonitorDelegate.20852
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSBluetoothWirelessSplitterMonitorDelegate.26407
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.18709
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.23982
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzer.25223
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerDelegate.27924
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImpl.18710
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImpl.23983
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEndpointAnalyzerImplDelegate.25224
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSEventMonitorDelegate.13555
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSFallbackAudioSessionReleaseProviding.26672
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.12996
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.7190
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.8372
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSLanguageCodeUpdateMonitorDelegate.9187
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSMediaPlayingMonitorDelegate.16996
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.26408
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPhoneCallStateMonitorDelegate.29989
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSecondPassProgressProviding.19840
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.11064
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.19841
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSelfTriggerDetectorDelegate.5612
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriAudioPlaybackSession.14439
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.10483
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.10865
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.13173
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.16997
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.19842
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.25911
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.29990
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.3524
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.4637
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.7589
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSiriClientBehaviorMonitorDelegate.9706
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSpeakerRecognitionAssetDownloadMonitorDelegate.17996
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSystemShellStartProviding.14634
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSSystemShellStartProviding.22918
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSTrialAssetDownloadMonitorDelegate.3282
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSUAFDownloadMonitorDelegate.29208
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.29209
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.6777
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerAssetHandlerDelegate.8373
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.10208
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.11065
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.14146
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.20853
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerDelegate.25460
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.10484
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.17997
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerEnabledMonitorDelegate.19843
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSXPCClientDelegate.7013
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSXPCClientDelegate.8374
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CoreSpeechXPCProtocol.22280
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_EARCaesuraSilencePosteriorGeneratorDelegate.28584
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.12401
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.12720
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.16627
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.17331
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.24159
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.26148
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.28338
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.28823
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding.30794
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.17332
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.24160
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.26149
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.28339
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying.28824
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10017
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10209
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10485
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.10866
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11066
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1117
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11591
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.11752
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12118
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1260
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.12997
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.13174
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.13556
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1403
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14147
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14440
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14635
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.14982
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1501
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15128
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.15367
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.154
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1567
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16170
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16326
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.16998
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.1707
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17150
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17823
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.17998
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.18711
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.18987
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.19844
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.19984
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.20854
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21134
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21211
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.21527
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2203
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22379
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22621
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.22919
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2313
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.23984
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24663
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24792
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24855
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.24959
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25225
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25461
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25719
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.25912
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26409
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26673
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.26822
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27092
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27227
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2742
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.27925
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28120
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.28585
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.2917
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29210
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29313
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.29991
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30490
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30584
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3061
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.30736
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.312
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3283
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.3525
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.388
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4030
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4230
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.4638
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5224
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5498
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5613
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.565
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.5947
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6048
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.6778
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7014
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7191
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7254
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7590
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7799
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.7929
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8375
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8832
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.8925
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9188
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.9707
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioRecorderDelegate.26674
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.16171
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.16327
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.16999
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.17824
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.19845
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.27093
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.29992
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.5948
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.6049
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioServerCrashMonitorDelegate.6779
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionControllerDelegate.27926
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioSessionControllerDelegate.28121
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.10867
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.16172
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.17000
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.18988
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.19846
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.29993
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.4231
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.4639
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.7015
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.8376
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSAudioStreamProvidingDelegate.9708
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.18712
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.23985
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzer.25226
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerDelegate.27927
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImpl.18713
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImpl.23986
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSEndpointAnalyzerImplDelegate.25227
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSKeywordAnalyzerNDEAPIScoreDelegate.15129
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSOpportuneSpeakEventMonitorDelegate.9709
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSPGEndpointAnalyzerDelegate.4640
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.10486
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.10868
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.13175
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.17001
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.19847
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.25913
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.29994
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.3526
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.4641
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.7591
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSSiriClientBehaviorMonitorDelegate.9710
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.10210
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.11067
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.14148
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.20855
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVoiceTriggerDelegate.25462
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSVolumeMonitorDelegate.10211
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_EARCaesuraSilencePosteriorGeneratorDelegate.28586
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10018
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10212
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10487
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.10869
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11068
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1118
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11592
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.11753
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12119
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1261
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.12998
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.13176
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.13557
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1404
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14149
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14441
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14636
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.14983
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1502
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15130
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.15368
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.155
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1568
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.16173
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.16328
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17002
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.1708
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17151
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17825
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.17999
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.18714
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.18989
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.19848
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.19985
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.20856
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21135
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21212
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.21528
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2204
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22380
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22622
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.22920
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2314
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.23987
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24664
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24793
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24856
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.24960
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25228
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25463
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25720
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.25914
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26410
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26675
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.26823
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27094
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27228
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2743
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.27928
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28122
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.28587
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.2918
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29211
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29314
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.29995
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30491
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30585
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3062
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.30737
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.313
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3284
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.3527
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.389
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4031
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4232
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.4642
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5225
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5499
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5614
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.566
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.5949
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6050
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.6780
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7016
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7192
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7255
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7592
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7800
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.7930
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8377
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8833
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.8926
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9189
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.9711
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SNResultsObserving.7801
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRSpeakerRecognitionControllerDelegate.8378
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SNResultsObserving.7802
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.19849
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.3528
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.4643
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSActivationEventNotificationHandlerDelegate.6781
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAssetManagerDelegate.23988
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAttSiriMitigationAssetHandlerDelegate.26411
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioConverterDelegate.11754
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.11755
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.12120
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.1709
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.22623
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioInjectionEngineDelegate.4032
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioRecorderDelegate.26676
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioRouteChangeMonitorDelegate.20857
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.16174
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.16329
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.17003
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.17826
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.19850
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.27095
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.29996
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.5950
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.6051
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioServerCrashMonitorDelegate.6782
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionControllerDelegate.27929
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionControllerDelegate.28123
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioSessionInfoProviding.24794
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProviding.27096
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.10870
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.16175
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.17004
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.18990
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.19851
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.29997
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.4233
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.4644
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.7017
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.8379
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSAudioStreamProvidingDelegate.9712
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSBenchmarkXPCProtocol.22624
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSBluetoothWirelessSplitterMonitorDelegate.20858
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSBluetoothWirelessSplitterMonitorDelegate.26412
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.18715
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.23989
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzer.25229
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerDelegate.27930
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImpl.18716
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImpl.23990
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEndpointAnalyzerImplDelegate.25230
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSEventMonitorDelegate.13558
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSFallbackAudioSessionReleaseProviding.26677
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSKeywordAnalyzerNDEAPIScoreDelegate.15131
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.12999
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.7193
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.8380
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSLanguageCodeUpdateMonitorDelegate.9190
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSMediaPlayingMonitorDelegate.17005
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSOpportuneSpeakEventMonitorDelegate.9713
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.26413
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSPhoneCallStateMonitorDelegate.29998
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSPGEndpointAnalyzerDelegate.4645
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSecondPassProgressProviding.19852
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.11069
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.19853
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSelfTriggerDetectorDelegate.5615
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriAudioPlaybackSession.14442
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.10488
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.10871
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.13177
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.17006
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.19854
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.25915
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.29999
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.3529
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.4646
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.7593
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSiriClientBehaviorMonitorDelegate.9714
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSpeakerRecognitionAssetDownloadMonitorDelegate.18000
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemShellStartProviding.14637
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSSystemShellStartProviding.22921
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSTrialAssetDownloadMonitorDelegate.3285
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSUAFDownloadMonitorDelegate.29212
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.29213
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.6783
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerAssetHandlerDelegate.8381
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.10213
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.11070
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.14150
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.20859
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerDelegate.25464
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.10489
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.18001
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerEnabledMonitorDelegate.19855
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSVolumeMonitorDelegate.10214
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSXPCClientDelegate.7018
- __OBJC_$_PROTOCOL_METHOD_TYPES_CSXPCClientDelegate.8382
- __OBJC_$_PROTOCOL_METHOD_TYPES_CoreSpeechXPCProtocol.22281
- __OBJC_$_PROTOCOL_METHOD_TYPES_EARCaesuraSilencePosteriorGeneratorDelegate.28588
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.12402
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.12721
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.16628
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.17333
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.24161
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.26150
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.28340
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.28825
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding.30795
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.17334
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.24162
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.26151
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.28341
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying.28826
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10019
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10215
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10490
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.10872
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11071
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1119
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11593
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.11756
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.12121
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1262
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.13000
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.13178
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.13559
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1405
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14151
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14443
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14638
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.14984
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1503
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15132
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.15369
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.156
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1569
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.16176
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.16330
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17007
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.1710
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17152
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.17827
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18002
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18717
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.18991
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.19856
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.19986
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.20860
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21136
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21213
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.21529
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2205
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22381
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22625
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.22922
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2315
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.23991
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24665
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24795
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24857
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.24961
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25231
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25465
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25721
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.25916
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26414
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26678
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.26824
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27097
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27229
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2744
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.27931
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.28124
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.28589
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.2919
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29214
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.29315
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30000
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30492
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30586
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3063
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.30738
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.314
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3286
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.3530
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.390
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4033
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4234
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.4647
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5226
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5500
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5616
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.567
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.5951
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6052
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.6784
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7019
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7194
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7256
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7594
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7803
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.7931
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8383
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8834
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.8927
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9191
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.9715
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.12403
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.12722
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.16629
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.17335
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.24163
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.26152
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.28342
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding.28827
- __OBJC_$_PROTOCOL_METHOD_TYPES_SNResultsObserving.7804
- __OBJC_$_PROTOCOL_METHOD_TYPES_SSRSpeakerRecognitionControllerDelegate.8384
- __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.19857
- __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.3531
- __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.4648
- __OBJC_$_PROTOCOL_REFS_CSActivationEventNotificationHandlerDelegate.6785
- __OBJC_$_PROTOCOL_REFS_CSAssetManagerDelegate.23992
- __OBJC_$_PROTOCOL_REFS_CSAttSiriMitigationAssetHandlerDelegate.26415
- __OBJC_$_PROTOCOL_REFS_CSAudioConverterDelegate.11757
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.11758
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.12122
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.1711
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.22626
- __OBJC_$_PROTOCOL_REFS_CSAudioInjectionEngineDelegate.4034
- __OBJC_$_PROTOCOL_REFS_CSAudioRecorderDelegate.26679
- __OBJC_$_PROTOCOL_REFS_CSAudioRouteChangeMonitorDelegate.20861
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.16177
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.16331
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.17008
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.17828
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.19858
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.27098
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.30001
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.5952
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.6053
- __OBJC_$_PROTOCOL_REFS_CSAudioServerCrashMonitorDelegate.6786
- __OBJC_$_PROTOCOL_REFS_CSAudioSessionControllerDelegate.27932
- __OBJC_$_PROTOCOL_REFS_CSAudioSessionControllerDelegate.28125
- __OBJC_$_PROTOCOL_REFS_CSAudioSessionInfoProviding.24796
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProviding.27099
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.10873
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.16178
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.17009
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.18992
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.19859
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.30002
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.4235
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.4649
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.7020
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.8385
- __OBJC_$_PROTOCOL_REFS_CSAudioStreamProvidingDelegate.9716
- __OBJC_$_PROTOCOL_REFS_CSBluetoothWirelessSplitterMonitorDelegate.20862
- __OBJC_$_PROTOCOL_REFS_CSBluetoothWirelessSplitterMonitorDelegate.26416
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.18718
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.23993
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzer.25232
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerDelegate.27933
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImpl.18719
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImpl.23994
- __OBJC_$_PROTOCOL_REFS_CSEndpointAnalyzerImplDelegate.25233
- __OBJC_$_PROTOCOL_REFS_CSEventMonitorDelegate.13560
- __OBJC_$_PROTOCOL_REFS_CSFallbackAudioSessionReleaseProviding.26680
- __OBJC_$_PROTOCOL_REFS_CSKeywordAnalyzerNDEAPIScoreDelegate.15133
- __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.13001
- __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.7195
- __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.8386
- __OBJC_$_PROTOCOL_REFS_CSLanguageCodeUpdateMonitorDelegate.9192
- __OBJC_$_PROTOCOL_REFS_CSMediaPlayingMonitorDelegate.17010
- __OBJC_$_PROTOCOL_REFS_CSOpportuneSpeakEventMonitorDelegate.9717
- __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.26417
- __OBJC_$_PROTOCOL_REFS_CSPhoneCallStateMonitorDelegate.30003
- __OBJC_$_PROTOCOL_REFS_CSSPGEndpointAnalyzerDelegate.4650
- __OBJC_$_PROTOCOL_REFS_CSSecondPassProgressProviding.19860
- __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.11072
- __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.19861
- __OBJC_$_PROTOCOL_REFS_CSSelfTriggerDetectorDelegate.5617
- __OBJC_$_PROTOCOL_REFS_CSSiriAudioPlaybackSession.14444
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.10491
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.10874
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.13179
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.17011
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.19862
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.25917
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.30004
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.3532
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.4651
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.7595
- __OBJC_$_PROTOCOL_REFS_CSSiriClientBehaviorMonitorDelegate.9718
- __OBJC_$_PROTOCOL_REFS_CSSpeakerRecognitionAssetDownloadMonitorDelegate.18003
- __OBJC_$_PROTOCOL_REFS_CSSpeechManagerDelegate.30739
- __OBJC_$_PROTOCOL_REFS_CSSystemShellStartProviding.14639
- __OBJC_$_PROTOCOL_REFS_CSSystemShellStartProviding.22923
- __OBJC_$_PROTOCOL_REFS_CSTrialAssetDownloadMonitorDelegate.3287
- __OBJC_$_PROTOCOL_REFS_CSUAFDownloadMonitorDelegate.29215
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.29216
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.6787
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerAssetHandlerDelegate.8387
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.10216
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.11073
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.14152
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.20863
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerDelegate.25466
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.10492
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.18004
- __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerEnabledMonitorDelegate.19863
- __OBJC_$_PROTOCOL_REFS_CSVolumeMonitorDelegate.10217
- __OBJC_$_PROTOCOL_REFS_CSXPCClientDelegate.7021
- __OBJC_$_PROTOCOL_REFS_CSXPCClientDelegate.8388
- __OBJC_$_PROTOCOL_REFS_EARCaesuraSilencePosteriorGeneratorDelegate.28590
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.12404
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.12723
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.16630
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.17336
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.24164
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.26153
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.28343
- __OBJC_$_PROTOCOL_REFS_NSSecureCoding.28828
- __OBJC_$_PROTOCOL_REFS_SNResultsObserving.7805
- __OBJC_$_PROTOCOL_REFS_SSRSpeakerRecognitionControllerDelegate.8389
- __OBJC_CLASS_PROTOCOLS_$_CSVoiceTriggerHearstEnabledPolicy
- __OBJC_CLASS_RO_$_CSVoiceTriggerHearstEnabledPolicy
- __OBJC_METACLASS_RO_$_CSVoiceTriggerHearstEnabledPolicy
- ___104+[CSAudioInjectionServices createAudioInjectionDeviceWithType:deviceName:deviceID:productID:completion:]_block_invoke.11
- ___106+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withNumChannels:withUserIntentOptions:completion:]_block_invoke.15
- ___110-[CSSiriSpeechRecorder speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:]_block_invoke.573
- ___110-[CSVoiceTriggerSecondPass _requestStartAudioStreamWitContext:audioProviderUUID:startStreamOption:completion:]_block_invoke.487
- ___112-[CSBuiltInVoiceTrigger _handleVoiceTriggerSecondPassWithSource:deviceId:event:audioProviderUUID:firstPassInfo:]_block_invoke.529
- ___113-[CSVoiceTriggerFirstPassJarvis _handleJarvisVoiceTriggerFromDeviceId:activationInfo:triggerHostTime:completion:]_block_invoke.437
- ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.507
- ___115-[CSVoiceTriggerFirstPassHearst _handleSecondPassResult:secondPassRequest:deviceId:requestOption:error:completion:]_block_invoke.516
- ___133-[CSBuiltInVoiceTrigger audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.508
- ___136-[CSVoiceTriggerSecondPass audioStreamProvider:numSamplesAvailableInExclave:hostTime:arrivalHostTimeToAudioRecorder:exclaveSampleCount:]_block_invoke.516
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke.577
- ___145-[CSSiriSpeechRecorder _speechControllerDidStopRecording:audioDeviceInfo:forReason:estimatedSpeechEndHostTime:errorCodeOverride:underlyingError:]_block_invoke_2.578
- ___30-[CSBuiltInVoiceTrigger start]_block_invoke.442
- ___30-[CSBuiltInVoiceTrigger start]_block_invoke.450
- ___30-[CSBuiltInVoiceTrigger start]_block_invoke_2.453
- ___39-[CSBuiltInVoiceTrigger _stopListening]_block_invoke.504
- ___40-[CSHybridEndpointer processTaskString:]_block_invoke.515
- ___40-[CSVoiceTriggerEventsCoordinator start]_block_invoke.413
- ___41-[CSSmartSiriVolume startSmartSiriVolume]_block_invoke.458
- ___42-[CSSpeechController _startPhaticDecision]_block_invoke.720
- ___42-[CSSpeechController _startPhaticDecision]_block_invoke.723
- ___42-[CSSpeechController _startPhaticDecision]_block_invoke.724
- ___44-[CSBuiltInVoiceTrigger _stopAPVoiceTrigger]_block_invoke.507
- ___47-[CSSiriSpeechRecorder playRecordingStartAlert]_block_invoke.547
- ___48+[CSAudioInjectionServices pingpong:completion:]_block_invoke.3
- ___48+[CSAudioInjectionServices pingpong:completion:]_block_invoke.7
- ___48-[CSSpeechController CSXPCClient:didDisconnect:]_block_invoke.789
- ___49-[CSVoiceTriggerFirstPassHearstAP _stopListening]_block_invoke.438
- ___49-[CSVoiceTriggerFirstPassJarvisAP _stopListening]_block_invoke.431
- ___50-[CSSiriSpeechRecorder _playPhaticWithCompletion:]_block_invoke.637
- ___50-[CSSpeechManager audioProviderWithContext:error:]_block_invoke.470
- ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke.499
- ___52-[CSBuiltInVoiceTrigger _startListenWithCompletion:]_block_invoke_2.500
- ___52-[CSSelfTriggerDetector _startListenWithCompletion:]_block_invoke.427
- ___52-[CSSpeechController setCurrentRecordContext:error:]_block_invoke.658
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.445
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.451
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.452
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.456
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke.463
- ___52-[CSSpeechManager _setupVoiceTriggerWithCompletion:]_block_invoke_2.464
- ___54-[CSSelfTriggerDetector _stopListeningWithCompletion:]_block_invoke.428
- ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.627
- ___54-[CSSpeechController prepareRecordWithSettings:error:]_block_invoke.636
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.687
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke.695
- ___55-[CSSpeechController startRecordingWithSettings:error:]_block_invoke_2.696
- ___56-[CSSiriSpeechRecorder performBlockAfterAlerts:timeout:]_block_invoke.647
- ___56-[CSVoiceTriggerFidesClient voiceTriggerGotSuperVector:]_block_invoke.454
- ___60-[CSSpeechController handleStopRecordingRequestWithOptions:]_block_invoke.726
- ___61+[CSAudioInjectionServices connectDeviceWithUUID:completion:]_block_invoke.17
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.481
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.482
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.483
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.484
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.488
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke.493
- ___61-[CSHybridEndpointAnalyzer osdAnalyzer:didUpdateOSDFeatures:]_block_invoke_2.489
- ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.526
- ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.527
- ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.529
- ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.530
- ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.533
- ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke.538
- ___61-[CSHybridEndpointer processOSDFeatures:withFrameDurationMs:]_block_invoke_2.531
- ___61-[CSNNVADEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke.415
- ___62-[CSHybridEndpointAnalyzer processAudioSamplesAsynchronously:]_block_invoke.474
- ___62-[CSSpeechController _scheduleAudibleFeedbackAtStartRecording]_block_invoke.708
- ___62-[CSSpeechController _scheduleAudibleFeedbackAtStartRecording]_block_invoke.711
- ___62-[CSVoiceTriggerFirstPassJarvisAP _startListenWithCompletion:]_block_invoke.429
- ___64+[CSAudioInjectionServices disconnectDeviceWithUUID:completion:]_block_invoke.19
- ___64-[CSSmartSiriVolume _startListenPollingWithInterval:completion:]_block_invoke.463
- ___65+[CSAudioInjectionServices primaryInputDeviceUUIDWithCompletion:]_block_invoke.21
- ___66-[CSSiriSpeechRecorder _prepareSpeechControllerWithOptions:error:]_block_invoke.468
- ___67-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke.418
- ___67-[CSSiriLauncher notifyBuiltInVoiceTrigger:myriadPHash:completion:]_block_invoke.423
- ___68-[CSBuiltInVoiceTrigger _startListenPollingWithInterval:completion:]_block_invoke.494
- ___68-[CSSelfTriggerDetector _startListenPollingWithInterval:completion:]_block_invoke.419
- ___70-[CSSiriSpeechRecorder _startAudioPlaybackRequest:options:completion:]_block_invoke.648
- ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke
- ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke.11
- ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke.6
- ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke.8
- ___70-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke.9
- ___72-[CSVoiceTriggerFirstPassJarvis _handleSecondPassResult:deviceId:error:]_block_invoke.454
- ___72-[CSVoiceTriggerFirstPassJarvis _handleSecondPassResult:deviceId:error:]_block_invoke.455
- ___73-[CSSiriSpeechRecorder _performTwoShotPromptForType:withOverride:atTime:]_block_invoke.636
- ___75-[CSSiriSpeechRecorder endpointer:didDetectHardEndpointAtTime:withMetrics:]_block_invoke.619
- ___76-[CSEnhancedEndpointer didEndpointWithFeatures:audioTimestampMs:completion:]_block_invoke.159
- ___77-[CSSiriSpeechRecorder startSpeechCaptureWithContext:willStartHandler:error:]_block_invoke.519
- ___77-[CSSpeechManager CSAudioRouteChangeMonitor:didReceiveAudioRouteChangeEvent:]_block_invoke.482
- ___79-[CSVoiceProfileRetrainManager CSVoiceTriggerEnabledMonitor:didReceiveEnabled:]_block_invoke.423
- ___80-[CSVoiceTriggerFirstPassHearstAP _startListenWithAudioProviderUUID:completion:]_block_invoke.434
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.638
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.639
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.641
- ___81-[CSSpeechController _activateAudioSessionWithReason:delay:delayRequested:error:]_block_invoke.649
- ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.500
- ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.501
- ___82-[CSVoiceTriggerSecondPass _voiceTriggerFirstPassDidDetectKeywordFrom:completion:]_block_invoke.508
- ___84-[CSSiriSpeechRecorder speechControllerLPCMRecordBufferAvailable:buffer:recordedAt:]_block_invoke.593
- ___84-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke.434
- ___84-[CSVoiceProfileRetrainManager _runVoiceProfileRetrainerWithAsset:withLanguageCode:]_block_invoke.436
- ___85-[CSVoiceTriggerFirstPassRemora activationEventNotificationHandler:event:completion:]_block_invoke.526
- ___85-[CSVoiceTriggerFirstPassRemora activationEventNotificationHandler:event:completion:]_block_invoke.528
- ___87-[CSVoiceTriggerFirstPassHearstAP _keywordAnalyzerNDAPI:hasResultAvailable:forChannel:]_block_invoke.452
- ___88-[CSHybridEndpointAnalyzer shouldAcceptEagerResultForDuration:resultsCompletionHandler:]_block_invoke.477
- ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.586
- ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.589
- ___88-[CSHybridEndpointer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.592
- ___88-[CSVoiceTriggerAlwaysOnProcessor disableVoiceTriggerOnAlwaysOnProcessorWithCompletion:]_block_invoke.15
- ___88-[CSVoiceTriggerFirstPassRemora _handleRemoraTriggerEvent:secondPassRequest:completion:]_block_invoke.537
- ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.536
- ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.538
- ___94-[CSHybridEndpointAnalyzer resetForNewRequestWithSampleRate:recordContext:disableRCSelection:]_block_invoke.539
- ___95+[CSAudioInjectionServices injectAudio:toDeviceWithUUID:withfadingTimeWindowLength:completion:]_block_invoke.14
- ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.494
- ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke.502
- ___96-[CSVoiceTriggerFirstPassHearst _handleRemoteMicVoiceTriggerEvent:secondPassRequest:completion:]_block_invoke_2.504
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke.605
- ___97-[CSSiriSpeechRecorder speechControllerDidDetectVoiceTriggerTwoShot:atTime:wantsAudibleFeedback:]_block_invoke_2.606
- ___Block_byref_object_copy_.10385
- ___Block_byref_object_copy_.11518
- ___Block_byref_object_copy_.12915
- ___Block_byref_object_copy_.13306
- ___Block_byref_object_copy_.14042
- ___Block_byref_object_copy_.14936
- ___Block_byref_object_copy_.1540
- ___Block_byref_object_copy_.15805
- ___Block_byref_object_copy_.15933
- ___Block_byref_object_copy_.17902
- ___Block_byref_object_copy_.18512
- ___Block_byref_object_copy_.19949
- ___Block_byref_object_copy_.20175
- ___Block_byref_object_copy_.21408
- ___Block_byref_object_copy_.21787
- ___Block_byref_object_copy_.2253
- ___Block_byref_object_copy_.22532
- ___Block_byref_object_copy_.23303
- ___Block_byref_object_copy_.23763
- ___Block_byref_object_copy_.24412
- ___Block_byref_object_copy_.25306
- ___Block_byref_object_copy_.25633
- ___Block_byref_object_copy_.26269
- ___Block_byref_object_copy_.26588
- ___Block_byref_object_copy_.2718
- ___Block_byref_object_copy_.27633
- ___Block_byref_object_copy_.28049
- ___Block_byref_object_copy_.29132
- ___Block_byref_object_copy_.29562
- ___Block_byref_object_copy_.30438
- ___Block_byref_object_copy_.3702
- ___Block_byref_object_copy_.3839
- ___Block_byref_object_copy_.3946
- ___Block_byref_object_copy_.438
- ___Block_byref_object_copy_.4524
- ___Block_byref_object_copy_.6350
- ___Block_byref_object_copy_.6682
- ___Block_byref_object_copy_.7394
- ___Block_byref_object_copy_.8176
- ___Block_byref_object_copy_.8763
- ___Block_byref_object_copy_.9858
- ___Block_byref_object_dispose_.10386
- ___Block_byref_object_dispose_.11519
- ___Block_byref_object_dispose_.12916
- ___Block_byref_object_dispose_.13307
- ___Block_byref_object_dispose_.14043
- ___Block_byref_object_dispose_.14937
- ___Block_byref_object_dispose_.1541
- ___Block_byref_object_dispose_.15806
- ___Block_byref_object_dispose_.15934
- ___Block_byref_object_dispose_.17903
- ___Block_byref_object_dispose_.18513
- ___Block_byref_object_dispose_.19950
- ___Block_byref_object_dispose_.20176
- ___Block_byref_object_dispose_.21409
- ___Block_byref_object_dispose_.21788
- ___Block_byref_object_dispose_.22533
- ___Block_byref_object_dispose_.2254
- ___Block_byref_object_dispose_.23304
- ___Block_byref_object_dispose_.23764
- ___Block_byref_object_dispose_.24413
- ___Block_byref_object_dispose_.25307
- ___Block_byref_object_dispose_.25634
- ___Block_byref_object_dispose_.26270
- ___Block_byref_object_dispose_.26589
- ___Block_byref_object_dispose_.2719
- ___Block_byref_object_dispose_.27634
- ___Block_byref_object_dispose_.28050
- ___Block_byref_object_dispose_.29133
- ___Block_byref_object_dispose_.29563
- ___Block_byref_object_dispose_.30439
- ___Block_byref_object_dispose_.3703
- ___Block_byref_object_dispose_.3840
- ___Block_byref_object_dispose_.3947
- ___Block_byref_object_dispose_.439
- ___Block_byref_object_dispose_.4525
- ___Block_byref_object_dispose_.6351
- ___Block_byref_object_dispose_.6683
- ___Block_byref_object_dispose_.7395
- ___Block_byref_object_dispose_.8177
- ___Block_byref_object_dispose_.8764
- ___Block_byref_object_dispose_.9859
- ___MobileTimerLibraryCore_block_invoke.927
- ___block_descriptor_48_e8_32s_e8_v16?0Q8ls32l8
- ___block_descriptor_49_e8_32s40bs_e11_v20?0I8Q12ls40l8s32l8
- ___block_descriptor_72_e8_32r40r48r56r64r_e36_v16?0"CSEnhancedEndpointerResult"8lr32l8r40l8r48l8r56l8r64l8
- ___block_literal_global.10.10548
- ___block_literal_global.10.22932
- ___block_literal_global.10.24280
- ___block_literal_global.10157
- ___block_literal_global.10418
- ___block_literal_global.10574
- ___block_literal_global.1074
- ___block_literal_global.1077
- ___block_literal_global.10770
- ___block_literal_global.10978
- ___block_literal_global.11377
- ___block_literal_global.11545
- ___block_literal_global.11830
- ___block_literal_global.11930
- ___block_literal_global.12050
- ___block_literal_global.1221
- ___block_literal_global.12343
- ___block_literal_global.12448
- ___block_literal_global.12502
- ___block_literal_global.12630
- ___block_literal_global.12666
- ___block_literal_global.13.23104
- ___block_literal_global.13.24281
- ___block_literal_global.13108
- ___block_literal_global.13220
- ___block_literal_global.13494
- ___block_literal_global.13587
- ___block_literal_global.1363
- ___block_literal_global.13953
- ___block_literal_global.14064
- ___block_literal_global.14476
- ___block_literal_global.14523
- ___block_literal_global.14592
- ___block_literal_global.1462
- ___block_literal_global.14646
- ___block_literal_global.14664
- ___block_literal_global.14775
- ___block_literal_global.15.14524
- ___block_literal_global.15326
- ___block_literal_global.15411
- ___block_literal_global.15906
- ___block_literal_global.15917
- ___block_literal_global.15962
- ___block_literal_global.16.14477
- ___block_literal_global.16.22933
- ___block_literal_global.16284
- ___block_literal_global.1645
- ___block_literal_global.16891
- ___block_literal_global.17.23035
- ___block_literal_global.17220
- ___block_literal_global.17398
- ___block_literal_global.17407
- ___block_literal_global.17490
- ___block_literal_global.17524
- ___block_literal_global.17779
- ___block_literal_global.17855
- ___block_literal_global.17953
- ___block_literal_global.18.14745
- ___block_literal_global.18.23105
- ___block_literal_global.18053
- ___block_literal_global.18801
- ___block_literal_global.18848
- ___block_literal_global.190
- ___block_literal_global.19053
- ___block_literal_global.19083
- ___block_literal_global.19693
- ___block_literal_global.19958
- ___block_literal_global.20.28032
- ___block_literal_global.20464
- ___block_literal_global.20531
- ___block_literal_global.20802
- ___block_literal_global.20883
- ___block_literal_global.20932
- ___block_literal_global.20977
- ___block_literal_global.20993
- ___block_literal_global.21.12449
- ___block_literal_global.2105
- ___block_literal_global.21284
- ___block_literal_global.21572
- ___block_literal_global.21703
- ___block_literal_global.21809
- ___block_literal_global.21821
- ___block_literal_global.21899
- ___block_literal_global.22.22934
- ___block_literal_global.22075
- ___block_literal_global.22122
- ___block_literal_global.22338
- ___block_literal_global.22515
- ___block_literal_global.2272
- ___block_literal_global.22820
- ___block_literal_global.22876
- ___block_literal_global.22931
- ___block_literal_global.23005
- ___block_literal_global.23034
- ___block_literal_global.23124
- ___block_literal_global.23209
- ___block_literal_global.23249
- ___block_literal_global.23376
- ___block_literal_global.2357
- ___block_literal_global.24.29160
- ___block_literal_global.2420
- ___block_literal_global.24278
- ___block_literal_global.2467
- ___block_literal_global.24746
- ___block_literal_global.24918
- ___block_literal_global.25.22935
- ___block_literal_global.25409
- ___block_literal_global.2568
- ___block_literal_global.2582
- ___block_literal_global.25961
- ___block_literal_global.26.28021
- ___block_literal_global.26015
- ___block_literal_global.26290
- ___block_literal_global.26361
- ___block_literal_global.26516
- ___block_literal_global.26842
- ___block_literal_global.27.12450
- ___block_literal_global.27738
- ___block_literal_global.2794
- ___block_literal_global.28.17748
- ___block_literal_global.28074
- ___block_literal_global.2815
- ___block_literal_global.28430
- ___block_literal_global.2876
- ___block_literal_global.28835
- ___block_literal_global.28884
- ___block_literal_global.28921
- ___block_literal_global.28960
- ___block_literal_global.29.22936
- ___block_literal_global.29.23036
- ___block_literal_global.29165
- ___block_literal_global.29264
- ___block_literal_global.29415
- ___block_literal_global.29524
- ___block_literal_global.29620
- ___block_literal_global.2968
- ___block_literal_global.30.12451
- ___block_literal_global.30178
- ___block_literal_global.3019
- ___block_literal_global.30363
- ___block_literal_global.30449
- ___block_literal_global.30820
- ___block_literal_global.3240
- ___block_literal_global.3430
- ___block_literal_global.3586
- ___block_literal_global.36.12452
- ___block_literal_global.3751
- ___block_literal_global.38.9007
- ___block_literal_global.3829
- ___block_literal_global.39.12453
- ___block_literal_global.3983
- ___block_literal_global.418
- ___block_literal_global.42.12454
- ___block_literal_global.420
- ___block_literal_global.424
- ___block_literal_global.426
- ___block_literal_global.426.11812
- ___block_literal_global.428
- ___block_literal_global.429
- ___block_literal_global.430
- ___block_literal_global.431
- ___block_literal_global.431.20683
- ___block_literal_global.432
- ___block_literal_global.44.16236
- ___block_literal_global.454
- ___block_literal_global.455
- ___block_literal_global.456
- ___block_literal_global.457
- ___block_literal_global.459
- ___block_literal_global.46.8999
- ___block_literal_global.466
- ___block_literal_global.484
- ___block_literal_global.4842
- ___block_literal_global.5.30821
- ___block_literal_global.527
- ___block_literal_global.53.22493
- ___block_literal_global.546
- ___block_literal_global.5794
- ___block_literal_global.5904
- ___block_literal_global.6004
- ___block_literal_global.6187
- ___block_literal_global.6291
- ___block_literal_global.6314
- ___block_literal_global.6387
- ___block_literal_global.643
- ___block_literal_global.67.2455
- ___block_literal_global.67.8596
- ___block_literal_global.6736
- ___block_literal_global.679
- ___block_literal_global.6880
- ___block_literal_global.7.24279
- ___block_literal_global.7.938
- ___block_literal_global.714
- ___block_literal_global.7145
- ___block_literal_global.7446
- ___block_literal_global.797
- ___block_literal_global.8.29258
- ___block_literal_global.8.29621
- ___block_literal_global.8.30822
- ___block_literal_global.8341
- ___block_literal_global.872
- ___block_literal_global.8884
- ___block_literal_global.9038
- ___block_literal_global.9090
- ___block_literal_global.9207
- ___block_literal_global.950
- ___block_literal_global.9603
- ___block_literal_global.9960
- __handleAudioChunk:.heartbeat_CORESPEECH_VOICETRIGGER_FIRSTPASS_LPCM_RECORD_BUFFER_AVAILABLE.19658
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.10745
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.19648
- __keywordAnalyzerNDAPI:hasResultAvailable:forChannel:.heartbeat.29820
- __unnamed_array_storage.1209
- __unnamed_array_storage.165.24533
- __unnamed_array_storage.176.24510
- __unnamed_array_storage.177.24511
- __unnamed_array_storage.21.28660
- __unnamed_array_storage.22138
- __unnamed_array_storage.22557
- __unnamed_array_storage.23213
- __unnamed_array_storage.24541
- __unnamed_array_storage.27647
- __unnamed_array_storage.28669
- __unnamed_array_storage.38.23214
- __unnamed_array_storage.6233
- __unnamed_array_storage.626
- __unnamed_array_storage.633
- __unnamed_array_storage.634
- __unnamed_array_storage.6375
- __unnamed_array_storage.7450
- _audit_stringMobileTimer.930
- _kVTEISecondPassRejectionMHUUID_block_invoke.enableHeartbeat.10766
- _kVTEISecondPassRejectionMHUUID_block_invoke.enableHeartbeat.29881
- _objc_msgSend$_alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:
- _objc_msgSend$initWithSiriRestrictionOnLockScreenMonitor:screenLockMonitor:voiceTriggerEnabledMonitor:CSPhoneCallStateMonitor:otherAppRecordingStateMonitor:siriClientBehaviorMonitor:srfUserSettingsMonitor:
- _objc_msgSend$initWithSpeechManager:voiceTriggerEnabledPolicyHearst:
- _objc_msgSend$otherAppRecordingStateMonitor
- _objc_msgSend$phonecallStateMonitor
- _objc_msgSend$screenLockMonitor
- _objc_msgSend$setCurrentAsset:
- _objc_msgSend$siriClientBehaviorMonitor
- _objc_msgSend$siriRestrictionOnLockScreenMonitor
- _objc_msgSend$startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:
- _objc_msgSend$voiceTriggerEnabledMonitor
- _sharedController.onceToken.11544
- _sharedController.sharedController.11546
- _sharedHandler.onceToken.1220
- _sharedHandler.onceToken.20463
- _sharedHandler.onceToken.29164
- _sharedHandler.onceToken.6386
- _sharedHandler.sharedHandler.1222
- _sharedHandler.sharedHandler.20465
- _sharedHandler.sharedHandler.29166
- _sharedHandler.sharedHandler.6388
- _sharedHandlerDisabledOnDeviceCompilation.onceToken.29159
- _sharedHandlerDisabledOnDeviceCompilation.sharedHandler.29161
- _sharedInstance._sharedInstance.11378
- _sharedInstance._sharedInstance.12667
- _sharedInstance._sharedInstance.14593
- _sharedInstance._sharedInstance.14776
- _sharedInstance._sharedInstance.16285
- _sharedInstance._sharedInstance.17221
- _sharedInstance._sharedInstance.17491
- _sharedInstance._sharedInstance.17780
- _sharedInstance._sharedInstance.17856
- _sharedInstance._sharedInstance.18054
- _sharedInstance._sharedInstance.18802
- _sharedInstance._sharedInstance.19054
- _sharedInstance._sharedInstance.20933
- _sharedInstance._sharedInstance.21573
- _sharedInstance._sharedInstance.21704
- _sharedInstance._sharedInstance.21900
- _sharedInstance._sharedInstance.22339
- _sharedInstance._sharedInstance.22877
- _sharedInstance._sharedInstance.2358
- _sharedInstance._sharedInstance.25962
- _sharedInstance._sharedInstance.26016
- _sharedInstance._sharedInstance.26843
- _sharedInstance._sharedInstance.2795
- _sharedInstance._sharedInstance.2877
- _sharedInstance._sharedInstance.28885
- _sharedInstance._sharedInstance.28922
- _sharedInstance._sharedInstance.29416
- _sharedInstance._sharedInstance.3020
- _sharedInstance._sharedInstance.30364
- _sharedInstance._sharedInstance.30450
- _sharedInstance._sharedInstance.3241
- _sharedInstance._sharedInstance.5795
- _sharedInstance._sharedInstance.5905
- _sharedInstance._sharedInstance.6005
- _sharedInstance._sharedInstance.6292
- _sharedInstance._sharedInstance.680
- _sharedInstance._sharedInstance.6881
- _sharedInstance._sharedInstance.798
- _sharedInstance._sharedInstance.873
- _sharedInstance._sharedInstance.8885
- _sharedInstance._sharedInstance.9091
- _sharedInstance._sharedInstance.951
- _sharedInstance.onceToken.10156
- _sharedInstance.onceToken.10417
- _sharedInstance.onceToken.10573
- _sharedInstance.onceToken.11376
- _sharedInstance.onceToken.12501
- _sharedInstance.onceToken.12629
- _sharedInstance.onceToken.12665
- _sharedInstance.onceToken.13219
- _sharedInstance.onceToken.1362
- _sharedInstance.onceToken.14591
- _sharedInstance.onceToken.1461
- _sharedInstance.onceToken.14774
- _sharedInstance.onceToken.15325
- _sharedInstance.onceToken.15410
- _sharedInstance.onceToken.15905
- _sharedInstance.onceToken.16283
- _sharedInstance.onceToken.17219
- _sharedInstance.onceToken.17489
- _sharedInstance.onceToken.17778
- _sharedInstance.onceToken.17854
- _sharedInstance.onceToken.17952
- _sharedInstance.onceToken.18052
- _sharedInstance.onceToken.18800
- _sharedInstance.onceToken.18847
- _sharedInstance.onceToken.189
- _sharedInstance.onceToken.19052
- _sharedInstance.onceToken.19082
- _sharedInstance.onceToken.20801
- _sharedInstance.onceToken.20882
- _sharedInstance.onceToken.20931
- _sharedInstance.onceToken.21283
- _sharedInstance.onceToken.21571
- _sharedInstance.onceToken.21702
- _sharedInstance.onceToken.21898
- _sharedInstance.onceToken.22074
- _sharedInstance.onceToken.22337
- _sharedInstance.onceToken.22819
- _sharedInstance.onceToken.22875
- _sharedInstance.onceToken.23004
- _sharedInstance.onceToken.23123
- _sharedInstance.onceToken.23248
- _sharedInstance.onceToken.23375
- _sharedInstance.onceToken.2356
- _sharedInstance.onceToken.2419
- _sharedInstance.onceToken.24745
- _sharedInstance.onceToken.24917
- _sharedInstance.onceToken.25408
- _sharedInstance.onceToken.25960
- _sharedInstance.onceToken.26014
- _sharedInstance.onceToken.26360
- _sharedInstance.onceToken.26515
- _sharedInstance.onceToken.26841
- _sharedInstance.onceToken.2793
- _sharedInstance.onceToken.2814
- _sharedInstance.onceToken.28429
- _sharedInstance.onceToken.2875
- _sharedInstance.onceToken.28883
- _sharedInstance.onceToken.28920
- _sharedInstance.onceToken.28959
- _sharedInstance.onceToken.29414
- _sharedInstance.onceToken.2967
- _sharedInstance.onceToken.30177
- _sharedInstance.onceToken.3018
- _sharedInstance.onceToken.30362
- _sharedInstance.onceToken.30448
- _sharedInstance.onceToken.3239
- _sharedInstance.onceToken.3585
- _sharedInstance.onceToken.526
- _sharedInstance.onceToken.5793
- _sharedInstance.onceToken.5903
- _sharedInstance.onceToken.6003
- _sharedInstance.onceToken.6290
- _sharedInstance.onceToken.678
- _sharedInstance.onceToken.6879
- _sharedInstance.onceToken.796
- _sharedInstance.onceToken.871
- _sharedInstance.onceToken.8883
- _sharedInstance.onceToken.9089
- _sharedInstance.onceToken.949
- _sharedInstance.sSharedInstance.19084
- _sharedInstance.sharedInstance.12503
- _sharedInstance.sharedInstance.12631
- _sharedInstance.sharedInstance.13221
- _sharedInstance.sharedInstance.15412
- _sharedInstance.sharedInstance.18849
- _sharedInstance.sharedInstance.20803
- _sharedInstance.sharedInstance.20884
- _sharedInstance.sharedInstance.22076
- _sharedInstance.sharedInstance.22821
- _sharedInstance.sharedInstance.23006
- _sharedInstance.sharedInstance.23250
- _sharedInstance.sharedInstance.2421
- _sharedInstance.sharedInstance.24919
- _sharedInstance.sharedInstance.25410
- _sharedInstance.sharedInstance.26517
- _sharedInstance.sharedInstance.28961
- _sharedInstance.sharedInstance.30179
- _sharedInstance.sharedInstance.3587
- _sharedInstance.sharedManager.21285
- _sharedInstance.sharedManager.23377
- _sharedInstance.sharedManager.28431
- _sharedInstance.sharedPolicy.1364
- _sharedInstance.sharedPolicy.23125
- _sharedInstance.sharedPolicy.26362
- _sharedInstance.sharedProvider.24747
- _sharedManager.onceToken.17397
- _sharedManager.onceToken.19957
- _sharedManager.onceToken.7144
- _sharedManager.sharedManager.17399
- _sharedManager.sharedManager.7146
- _sharedMonitor.onceToken.21808
- _sharedMonitor.sharedMonitor.21810
- _sharedService.onceToken.15961
- _sharedService.onceToken.28073
- _sharedService.sharedService.28075
CStrings:
+ "\x11\""
+ "%s ::: CoreSpeech Secure logging initialized"
+ "%s AudioQueue call back is asking for audio, injected file has been found"
+ "%s AudioQueue call back is asking for audio, injected file is not available, injecting digital 1s"
+ "%s CSHybridEndpointer can NOT ProcessCurrentRequest, fallback to NNVAD"
+ "%s CSVoiceTriggerSecondPass[%{public}@]:Not valid firstPass source for Exclave : %{public}lu"
+ "%s Client request to speak audio into exclave with URL: %@ at time: %llu"
+ "%s Directly enable AOP without configuring model"
+ "%s Disable FF since this is Exclave hardware without Siri DSP"
+ "%s Failed to activate audioSession with error: %@"
+ "%s Failed to create Exclave Audio Injection AudioQueue with OSStatus error: %d"
+ "%s Failed to deactivate audioSession with error: %@"
+ "%s Failed to feed audio into exclave, AQ or AQBuffer is invalid"
+ "%s Failed to feed audio into exclave, unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
+ "%s Failed to feed audio into exclave, unable to enqueue AQ buffer with OSStatus: %d"
+ "%s Failed to feed audio into exclave, unable to locate available audio queue"
+ "%s Failed to feed audio into exclave, unable to start AQ buffer with OSStatus: %d"
+ "%s Failed to set audioSession properties with error: %@"
+ "%s Fetched exclave audio injection enabled : %d"
+ "%s File doesn't exist: %{public}@"
+ "%s Ignore %{public}@ since Siri client is current listening"
+ "%s Ignore %{public}@ since Siri client is currently in a connected call"
+ "%s Ignore %{public}@ since Siri client is currently in a ringtone and does not support A2DP"
+ "%s Ignore %{public}@ since Siri client is currently in an outgoing call"
+ "%s Ignore %{public}@ since VoiceTrigger was turned off"
+ "%s New asset is the same as current asset - no update needed."
+ "%s Not a ReadThis or voiceOver audioSession - bail out!"
+ "%s PSR Profile Embedding extract : %d * %d with error %@"
+ "%s PSR Profile embedding is nil, not sending embedding to Exclave"
+ "%s Request timeout with features %{public}@"
+ "%s SAT Profile Embedding extract : %d * %d  with error %@"
+ "%s SAT Profile embedding is nil, not sending embedding to Exclave"
+ "%s SecureSpeakerRecognitionConfig string %s"
+ "%s Setting exclave audio injection enabled : %d"
+ "%s Successfully activate audioSession"
+ "%s Successfully deactivate audioSession"
+ "%s Successfully start the audio queue"
+ "%s Unable to alloc AudioQueue AudioBuffer with OSStatus: %d"
+ "%s Updating current asset."
+ "%s attendingStateStart:(%u) readThisOrVoiceOverSessionActive:(%u) aggressiveECParamsApplied:(%u) inAttendingWindow:(%u)"
+ "%s audio session info is nil - bail out!"
+ "%s goodness = %d, confidence = %d absTime = %llu, frac = %d"
+ "%s injection is ended at time: %llu"
+ "%s isReadThisAudioSession:(%u), isVoiceOver:(%u)"
+ "%s locale=%@"
+ "%s readThisOrVoiceOverSessionActive:(%u) aggressiveEchoCancellationApplied:(%u) inAttendingWindow:(%u)"
+ "%s recordRoute = %@, playbackRoute = %@, speechEvent = %lu, activationMode = %ld, speechRecordingMode = %lu, AFDeviceRingerSwitchState = %@, AFSoundID = %@, AFPresentationMode = %lu, usesDeviceSpeakerForTTS = %lu, attemptsToUsePastDataBufferFrames = %d, usePrelistening = %d, isOnPhoneCall = %d, hasPlayedStartAlert = %d, supportsEchoCancellation = %d, isVoiceOverTouchEnabled = %d, isDeviceInCarDNDMode = %d, isVibrationEnabled = %d, isVibrationSupported = %d, suppressStartAlert = %d, activationHostTime = %llu"
+ "%s trigger-length : %{public}llu"
+ "+[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:recordingInfo:speechEvent:activationMode:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usesDeviceSpeakerForTTS:attemptsToUsePastDataBufferFrames:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isDeviceInCarDNDMode:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]"
+ "-[CSAudioInjectionProviderExclave _createAudioQueueIfNeeded]"
+ "-[CSAudioInjectionProviderExclave _defaultBufferRef]"
+ "-[CSAudioInjectionProviderExclave _prepareAndStartAudioQueue]"
+ "-[CSAudioInjectionProviderExclave _readAudioBufferAndFeedIntoAudioQueue]_block_invoke"
+ "-[CSAudioInjectionProviderExclave _setAudioSessionActive:]"
+ "-[CSAudioInjectionProviderExclave speakAudioInExclave:withCompletion:]_block_invoke"
+ "-[CSBuiltInVoiceTrigger activationEventNotificationHandler:event:completion:]_block_invoke"
+ "-[CSBuiltInVoiceTrigger updateExclaveKitSiriLocale:]_block_invoke"
+ "-[CSHybridEndpointer _updateCurrentAsset:]"
+ "-[CSVoiceTriggerSecondPass _calculateRecordingTimeForAOPTriggerFromFirstPassInfo:completion:]"
+ "-[CSVoiceTriggerSecondPass _syncVoiceProfileEmbeddingsToExclave]_block_invoke"
+ "-[SecureVoiceTriggerSpeakerRecognitionDecoder decodeSecureVoiceTriggerSpeakerRecognitionConfigForAsset:]"
+ "9\x14"
+ "@144@0:8@16@24@32q40q48q56q64q72q80q88B96B100B104B108B112B116B120B124B128B132Q136"
+ "@28@0:8@16f24"
+ "@88@0:8@16I24f28f32f36f40f44f48f52f56I60B64I68I72I76I80B84"
+ "ApplicationProcessorExclave"
+ "ApplicationProcessorExclaveWithConnectedCall"
+ "ApplicationProcessorExclaveWithRingtone"
+ "B36@0:8@16@24B32"
+ "BuiltInAlwaysOnProcessorExclave"
+ "CSAudioInjectionProviderExclave"
+ "CSSecureLogInitIfNeeded_block_invoke"
+ "HACBuiltIn"
+ "I40@0:8@16@24Q32"
+ "Q\x1b\xc1\x81\x12\x19A"
+ "SecureSpeakerRecognitionConfigBridge"
+ "SecureSpeakerRecognitionPhraseConfigBridge"
+ "SecureVoiceTriggerSpeakerRecognitionDecoder"
+ "T@\"CSAudioTimeConverter\",&,N,V_exclaveAudioTimeConverter"
+ "T@\"CSPhoneCallStateMonitor\",&,N,V_phoneCallStateMonitor"
+ "T@\"CSVoiceTriggerEnabledMonitor\",&,N,V_voiceTriggerEnabledMonitor"
+ "T@\"NSArray\",C,N,V_phraseConfigs"
+ "T@\"NSString\",C,N,V_name"
+ "T@?,C,N,V_injectionCompletion"
+ "TB,N,V_didForceEndpoint"
+ "TB,N,V_implicitTrainingEnabled"
+ "TB,N,V_isAudioQueueStarted"
+ "TB,N,V_readThisOrVoiceOverSessionActive"
+ "TB,N,V_useTDTIEnrollment"
+ "TI,N,V_maxEnrollmentUtterances"
+ "TI,N,V_multiUserConfidentScoreThreshold"
+ "TI,N,V_multiUserDeltaScoreThreshold"
+ "TI,N,V_multiUserHighScoreThreshold"
+ "TI,N,V_multiUserLowScoreThreshold"
+ "TI,N,V_numPruningRetentionUtt"
+ "TQ,N,V_injectionEndTime"
+ "TQ,N,V_injectionStartTime"
+ "T^{OpaqueAudioQueue=},N,V_exclaveAudioQueue"
+ "Tf,N,V_combinationWeight"
+ "Tf,N,V_implicitProfileDeltaThreshold"
+ "Tf,N,V_implicitProfileThreshold"
+ "Tf,N,V_implicitVTThreshold"
+ "Tf,N,V_pruningExplicitPSRThreshold"
+ "Tf,N,V_pruningExplicitSATThreshold"
+ "Tf,N,V_pruningPSRThreshold"
+ "Tf,N,V_pruningSATThreshold"
+ "Tf,N,V_satThreshold"
+ "Tq,N,V_echoCancellationReason"
+ "^{AudioQueueBuffer=I^vI^vI^{AudioStreamPacketDescription}I}16@0:8"
+ "_alertBehaviorForRecordRoute:playbackRoute:recordingInfo:speechEvent:activationMode:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usesDeviceSpeakerForTTS:attemptsToUsePastDataBufferFrames:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isDeviceInCarDNDMode:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:"
+ "_calculateRecordingTimeForAOPTriggerFromFirstPassInfo:completion:"
+ "_combinationWeight"
+ "_combinationWeight: %f\n"
+ "_createAudioQueueIfNeeded"
+ "_decodePhraseConfig:"
+ "_defaultBufferRef"
+ "_didForceEndpoint"
+ "_echoCancellationReason"
+ "_exclaveAudioQueue"
+ "_exclaveAudioTimeConverter"
+ "_getBooleanValue:forKey:withDefaultValue:"
+ "_getExclaveAudioTimeConverter"
+ "_getFloatValue:forKey:withDefaultValue:"
+ "_getIntValue:forKey:withDefaultValue:"
+ "_implicitProfileDeltaThreshold"
+ "_implicitProfileThreshold"
+ "_implicitProfileThreshold: %f\n"
+ "_implicitTrainingEnabled"
+ "_implicitVTThreshold"
+ "_implicitVTThreshold: %f\n"
+ "_implicit_training_enabled: %d\n"
+ "_injectionCompletion"
+ "_injectionEndTime"
+ "_injectionStartTime"
+ "_isAudioQueueStarted"
+ "_maxEnrollmentUtterances"
+ "_maxEnrollmentUtterances: %u\n"
+ "_multiUserConfidentScoreThreshold"
+ "_multiUserConfidentScoreThreshold: %u\n"
+ "_multiUserDeltaScoreThreshold"
+ "_multiUserDeltaScoreThreshold: %u\n"
+ "_multiUserHighScoreThreshold"
+ "_multiUserHighScoreThreshold: %u\n"
+ "_multiUserLowScoreThreshold"
+ "_multiUserLowScoreThreshold: %u\n"
+ "_numPruningRetentionUtt"
+ "_numPruningRetentionUtt: %u\n"
+ "_phoneCallStateMonitor"
+ "_phraseConfigs"
+ "_prepareAndStartAudioQueue"
+ "_pruningExplicitPSRThreshold"
+ "_pruningExplicitPSRThreshold: %f\n"
+ "_pruningExplicitSATThreshold"
+ "_pruningExplicitSATThreshold: %f\n"
+ "_pruningPSRThreshold"
+ "_pruningPSRThreshold: %f\n"
+ "_pruningSATThreshold"
+ "_pruningSATThreshold: %f\n"
+ "_readAudioBufferAndFeedIntoAudioQueue"
+ "_readThisOrVoiceOverSessionActive"
+ "_satThreshold"
+ "_setAudioSessionActive:"
+ "_updateCurrentAsset:"
+ "_updateExclaveKitSiriLocale:"
+ "_useTDTIEnrollment"
+ "_useTDTIEnrollment: %d\n"
+ "cString"
+ "category"
+ "com.apple.corespeech"
+ "configAOPVoiceTrigger"
+ "decodeSecureVoiceTriggerSpeakerRecognitionConfigForAsset:"
+ "defaultExclaveConverter"
+ "didForceEndpoint"
+ "echoCancellationReason"
+ "enableExclaveAudioInjection:"
+ "exclave-built-in"
+ "exclaveAudioInjectionEnabled"
+ "exclaveAudioQueue"
+ "exclaveAudioTimeConverter"
+ "exclaveSignalIntensity"
+ "extractPSRVoiceProfileWithContext:completion:"
+ "extractSATVoiceProfileWithContext:completion:"
+ "f36@0:8@16@24f32"
+ "fetchAOPVoiceTriggerResult:"
+ "generatePHashFromExclaveVoiceTriggerInfo:writeFile:"
+ "getBool:category:defaultValue:"
+ "getDictionaryArray:category:"
+ "getFloat:category:defaultValue:"
+ "getString:category:defaultValue:"
+ "getUnsignedLongLongValue:category:defaultValue:"
+ "implicitTrainingEnabled"
+ "initWithName:satThreshold:"
+ "initWithPhraseConfigs:numPruningRetentionUtt:pruningExplicitSATThreshold:pruningExplicitPSRThreshold:pruningSATThreshold:pruningPSRThreshold:combinationWeight:implicitProfileThreshold:implicitProfileDeltaThreshold:implicitVTThreshold:maxEnrollmentUtterances:implicit_training_enabled:multiUserHighScoreThreshold:multiUserLowScoreThreshold:multiUserConfidentScoreThreshold:multiUserDeltaScoreThreshold:useTDTIEnrollment:"
+ "initWithSpeechManager:voiceTriggerEnabledMonitor:siriClientBehaviorMonitor:phoneCallStateMonitor:otherAppRecordingStateMonitor:"
+ "injectionCompletion"
+ "injectionEndTime"
+ "injectionStartTime"
+ "isAudioQueueStarted"
+ "isFirstPassSourceTypeRingtoneWithVTEI:"
+ "isSiriDSPTurnedOn"
+ "isVoiceTriggerFromExclaveWithVTEI:"
+ "iteratePhraseConfigs:"
+ "phraseConfigs-count: %ld\n"
+ "readThisOrVoiceOverSessionActive"
+ "setCategory:mode:options:error:"
+ "setCombinationWeight:"
+ "setDidForceEndpoint:"
+ "setEchoCancellationReason:"
+ "setExclaveAudioQueue:"
+ "setExclaveAudioTimeConverter:"
+ "setImplicitProfileDeltaThreshold:"
+ "setImplicitProfileThreshold:"
+ "setImplicitTrainingEnabled:"
+ "setImplicitVTThreshold:"
+ "setInjectionCompletion:"
+ "setInjectionEndTime:"
+ "setInjectionStartTime:"
+ "setIsAudioQueueStarted:"
+ "setMaxEnrollmentUtterances:"
+ "setMultiUserConfidentScoreThreshold:"
+ "setMultiUserDeltaScoreThreshold:"
+ "setMultiUserHighScoreThreshold:"
+ "setMultiUserLowScoreThreshold:"
+ "setNumPruningRetentionUtt:"
+ "setPhoneCallStateMonitor:"
+ "setPhraseConfigs:"
+ "setPruningExplicitPSRThreshold:"
+ "setPruningExplicitSATThreshold:"
+ "setPruningPSRThreshold:"
+ "setPruningSATThreshold:"
+ "setReadThisOrVoiceOverSessionActive:"
+ "setSatThreshold:"
+ "setSpeakerProfile:numEmbeddings:dimension:speakerRecognizerType:"
+ "setUseTDTIEnrollment:"
+ "setVoiceTriggerEnabledMonitor:"
+ "speakAudioInExclave:withCompletion:"
+ "startSecondPassVoiceTriggerWithFirstPassSource:phsEnabled:supportMultiPhrase:"
+ "updateExclaveKitSiriLocale:"
+ "v24@?0Q8Q16"
+ "v32@?0@\"NSDictionary\"8Q16^B24"
+ "v32@?0@\"SecureSpeakerRecognitionPhraseConfigBridge\"8Q16^B24"
+ "v36@?0@\"NSData\"8I16I20I24@\"NSError\"28"
+ "v56@?0Q8d16f24f28I32f36Q40Q48"
+ "v60@?0I8Q12d20f28f32I36f40Q44Q52"
+ "\x81"
- "%s CSHybridEndpointer can-NOT-ProcessCurrentRequest, fallback  to NNVAD"
- "%s File not exist: %{public}@"
- "%s IVoiceTrigger on hearst cannot be turned on since Siri client is currently in an outgoing call"
- "%s Ignore %{public}@ since voice trigger enabled policy returned NO"
- "%s VoiceTrigger on hearst cannot be turned on Siri client is current listening"
- "%s VoiceTrigger on hearst cannot be turned on since Siri client is currently in a connected call"
- "%s VoiceTrigger on hearst cannot be turned on since Siri client is currently in a ringtone and does not support A2DP"
- "%s VoiceTrigger on hearst cannot be turned on since Siri is restricted on lock screen"
- "%s VoiceTrigger on hearst cannot be turned on since VoiceTrigger is disabled"
- "%s VoiceTrigger on hearst cannot be turned on since phrases spotter is disabled"
- "%s VoiceTrigger on hearst cannot be turned on since there is an other non eligible app recording"
- "%s activationMode = %ld, usesDeviceSpeakerForTTS = %lu, attemptsToUsePastDataBufferFrames = %d, isDeviceInCarDNDMode = %d"
- "%s attendingStateStart:(%u) audioSessionStateActive:(%u) aggressiveECParamsApplied:(%u) inAttendingWindow:(%u)"
- "%s audioSessionRequiresECParams:(%u) aggressiveEchoCancellationApplied:(%u) inAttendingWindow:(%u)"
- "%s isReadThis:(%u), isVoiceOver:(%u)"
- "%s progCheckerReocgnizerConfigFiles: %@"
- "%s recordRoute = %@, playbackRoute = %@, speechEvent = %lu, speechRecordingMode = %lu, AFDeviceRingerSwitchState = %@, AFSoundID = %@, AFPresentationMode = %lu, usePrelistening = %d, isOnPhoneCall = %d, hasPlayedStartAlert = %d, supportsEchoCancellation = %d, isVoiceOverTouchEnabled = %d, isVibrationEnabled = %d, isVibrationSupported = %d, suppressStartAlert = %d, activationHostTime = %llu"
- "%s update assets to: %@"
- "+[CSOnDeviceCompilationUtils getModelConfigsWithAsset:modelType:]"
- "+[CSSiriAudioActivationInfo _alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:]"
- "-[CSHybridEndpointer endpointerAssetManagerDidUpdateAsset:]_block_invoke"
- "-[CSVoiceTriggerHearstEnabledPolicy _addVoiceTriggerEnabledConditions]_block_invoke"
- ";"
- "@\"CSScreenLockMonitor\""
- "@\"CSSiriRestrictionOnLockScreenMonitor\""
- "@\"CSVoiceTriggerHearstEnabledPolicy\""
- "@112@0:8@16@24q32q40q48q56q64B72B76B80B84B88B92B96B100Q104"
- "CSVoiceTriggerHearstEnabledPolicy"
- "Q\x1b\xc1\x81\x12\x18A"
- "T@\"CSOtherAppRecordingStateMonitor\",R,N,V_otherAppRecordingStateMonitor"
- "T@\"CSPhoneCallStateMonitor\",R,N,V_phonecallStateMonitor"
- "T@\"CSScreenLockMonitor\",R,N,V_screenLockMonitor"
- "T@\"CSSiriClientBehaviorMonitor\",R,N,V_siriClientBehaviorMonitor"
- "T@\"CSSiriRestrictionOnLockScreenMonitor\",R,N,V_siriRestrictionOnLockScreenMonitor"
- "T@\"CSVoiceTriggerEnabledMonitor\",R,N,V_voiceTriggerEnabledMonitor"
- "T@\"CSVoiceTriggerHearstEnabledPolicy\",&,N,V_voicetriggerHearstEnabledPolicy"
- "TB,N,V_audioSessionStateActive"
- "TB,N,V_echoCancellationDeferred"
- "_alertBehaviorForRecordRoute:playbackRoute:speechEvent:speechRecordingMode:ringerState:startingAlertBeepOverideID:presentationMode:usePrelistening:isOnPhoneCall:hasPlayedStartAlert:supportsEchoCancellation:isVoiceOverTouchEnabled:isVibrationEnabled:isVibrationSupported:suppressStartAlert:activationHostTime:"
- "_audioSessionStateActive"
- "_echoCancellationDeferred"
- "_phonecallStateMonitor"
- "_screenLockMonitor"
- "_siriRestrictionOnLockScreenMonitor"
- "_voicetriggerHearstEnabledPolicy"
- "audioSessionStateActive"
- "echoCancellationDeferred"
- "initWithSiriRestrictionOnLockScreenMonitor:screenLockMonitor:voiceTriggerEnabledMonitor:CSPhoneCallStateMonitor:otherAppRecordingStateMonitor:siriClientBehaviorMonitor:srfUserSettingsMonitor:"
- "initWithSpeechManager:voiceTriggerEnabledPolicyHearst:"
- "phonecallStateMonitor"
- "screenLockMonitor"
- "setAudioSessionStateActive:"
- "setEchoCancellationDeferred:"
- "setVoicetriggerHearstEnabledPolicy:"
- "siriRestrictionOnLockScreenMonitor"
- "startSecondPassVoiceTriggerWithPHSEnabled:supportMultiPhrase:"
- "v20@?0I8Q12"
- "voicetriggerHearstEnabledPolicy"

```
