## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3610.11.1.0.0
-  __TEXT.__text: 0xb79fc
-  __TEXT.__objc_methlist: 0x6e08
+3610.19.5.0.0
+  __TEXT.__text: 0xb9348
+  __TEXT.__objc_methlist: 0x6f10
   __TEXT.__const: 0xfa8
   __TEXT.__dlopen_cstrs: 0xa6
-  __TEXT.__cstring: 0x110b3
+  __TEXT.__cstring: 0x11535
   __TEXT.__swift5_typeref: 0x6a0
-  __TEXT.__oslogstring: 0xf0c2
+  __TEXT.__oslogstring: 0xf2a5
   __TEXT.__swift5_capture: 0x230
   __TEXT.__constg_swiftt: 0x910
   __TEXT.__swift5_reflstr: 0x57f

   __TEXT.__swift_as_cont: 0xcc
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x30
-  __TEXT.__gcc_except_tab: 0x29d0
-  __TEXT.__unwind_info: 0x29d8
+  __TEXT.__gcc_except_tab: 0x29e4
+  __TEXT.__unwind_info: 0x2a30
   __TEXT.__eh_frame: 0x1394
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f58
-  __DATA_CONST.__objc_classlist: 0x338
+  __DATA_CONST.__const: 0x2000
+  __DATA_CONST.__objc_classlist: 0x340
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x170
+  __DATA_CONST.__objc_protolist: 0x178
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3f70
-  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_selrefs: 0x4010
+  __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x230
-  __DATA_CONST.__objc_arraydata: 0x3e0
-  __DATA_CONST.__got: 0xb40
+  __DATA_CONST.__objc_arraydata: 0x400
+  __DATA_CONST.__got: 0xb48
   __AUTH_CONST.__const: 0xee0
-  __AUTH_CONST.__cfstring: 0x5740
-  __AUTH_CONST.__objc_const: 0xbc88
-  __AUTH_CONST.__objc_dictobj: 0x9b0
+  __AUTH_CONST.__cfstring: 0x5860
+  __AUTH_CONST.__objc_const: 0xbd88
+  __AUTH_CONST.__objc_dictobj: 0xa00
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH_CONST.__auth_got: 0x1058
-  __AUTH.__objc_data: 0x1b8
+  __AUTH_CONST.__auth_got: 0x1050
+  __AUTH.__objc_data: 0x208
   __AUTH.__data: 0x90
-  __DATA.__objc_ivar: 0x878
-  __DATA.__data: 0x1450
+  __DATA.__objc_ivar: 0x880
+  __DATA.__data: 0x14b0
   __DATA.__common: 0x60
   __DATA_DIRTY.__objc_data: 0x2680
   __DATA_DIRTY.__data: 0x580
-  __DATA_DIRTY.__bss: 0x78
+  __DATA_DIRTY.__bss: 0x68
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3108
-  Symbols:   5015
-  CStrings:  2668
+  Functions: 3130
+  Symbols:   5054
+  CStrings:  2696
 
Symbols:
+ +[SSRVoiceProfileEmbeddingTrainer _addSpeakerEmbedding:toProfile:withContext:]
+ +[SSRVoiceProfileEmbeddingTrainer _copyModelFile:toExclaveModelFile:ofProfile:]
+ +[SSRVoiceProfileEmbeddingTrainer _errorWithCode:reason:]
+ +[SSRVoiceProfileEmbeddingTrainer _seedScorer:withModelFile:embedding:dimensions:]
+ +[SSRVoiceProfileEmbeddingTrainer addSpeakerEmbedding:toProfile:withContext:error:]
+ -[CSVTUIAudioSessionRecorder setAudioRecordingSampleCount:]
+ -[SSRSpeakerAnalyzerPSR latestSpeakerVector]
+ -[SSRSpeakerRecognitionController fetchFinalEmbeddingWithCompletion:]
+ -[SSRSpeakerRecognitionOrchestrator fetchFinalEmbeddingWithCompletion:]
+ -[SSRSpeakerRecognizerPSR latestSpeakerVector]
+ -[SSRVTUITrainingManager _builtInVoiceTrigger]
+ -[SSRVTUITrainingManager _cancelEnrollmentVoiceTriggerWait]
+ -[SSRVTUITrainingManager _startAudioSessionAfterVoiceTrigger:forSession:]
+ -[SSRVoiceProfileManager extractEmbeddingFromSession:toProfile:withContext:withCompletion:]
+ -[SSRVoiceProfileStore addUserVoiceProfile:withSpeakerEmbedding:withContext:withCompletion:]
+ GCC_except_table1020
+ GCC_except_table1023
+ GCC_except_table1025
+ GCC_except_table1026
+ GCC_except_table1027
+ GCC_except_table1028
+ GCC_except_table1029
+ GCC_except_table1030
+ GCC_except_table1031
+ GCC_except_table1032
+ GCC_except_table1034
+ GCC_except_table1035
+ GCC_except_table1037
+ GCC_except_table1040
+ GCC_except_table1117
+ GCC_except_table1143
+ GCC_except_table1197
+ GCC_except_table1201
+ GCC_except_table1219
+ GCC_except_table1319
+ GCC_except_table1320
+ GCC_except_table1322
+ GCC_except_table1343
+ GCC_except_table1347
+ GCC_except_table1356
+ GCC_except_table1361
+ GCC_except_table1365
+ GCC_except_table1426
+ GCC_except_table1432
+ GCC_except_table1436
+ GCC_except_table1440
+ GCC_except_table1443
+ GCC_except_table1449
+ GCC_except_table1450
+ GCC_except_table1458
+ GCC_except_table1487
+ GCC_except_table1536
+ GCC_except_table1567
+ GCC_except_table1574
+ GCC_except_table1621
+ GCC_except_table1628
+ GCC_except_table1650
+ GCC_except_table1677
+ GCC_except_table1777
+ GCC_except_table1783
+ GCC_except_table1798
+ GCC_except_table1808
+ GCC_except_table1818
+ GCC_except_table1839
+ GCC_except_table1843
+ GCC_except_table1847
+ GCC_except_table1853
+ GCC_except_table1861
+ GCC_except_table188
+ GCC_except_table191
+ GCC_except_table1928
+ GCC_except_table193
+ GCC_except_table1932
+ GCC_except_table1993
+ GCC_except_table2028
+ GCC_except_table2095
+ GCC_except_table2127
+ GCC_except_table2136
+ GCC_except_table2155
+ GCC_except_table2217
+ GCC_except_table260
+ GCC_except_table277
+ GCC_except_table283
+ GCC_except_table340
+ GCC_except_table361
+ GCC_except_table390
+ GCC_except_table398
+ GCC_except_table408
+ GCC_except_table411
+ GCC_except_table451
+ GCC_except_table512
+ GCC_except_table568
+ GCC_except_table583
+ GCC_except_table596
+ GCC_except_table672
+ GCC_except_table681
+ GCC_except_table687
+ GCC_except_table755
+ GCC_except_table788
+ GCC_except_table871
+ GCC_except_table913
+ GCC_except_table934
+ GCC_except_table937
+ _OBJC_CLASS_$_SSRVoiceProfileEmbeddingTrainer
+ _OBJC_IVAR_$_CSVTUIAudioSessionRecorder._shouldUseRecordingStartSampleCount
+ _OBJC_IVAR_$_CSVTUIAudioSessionRecorder._startRecordingSampleCount
+ _OBJC_METACLASS_$_SSRVoiceProfileEmbeddingTrainer
+ _SSRVTUITrainingServiceEntitlement
+ __OBJC_$_CLASS_METHODS_SSRVoiceProfileEmbeddingTrainer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSVoiceTriggerManagerProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SSRSpeakerRecognizer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CSVoiceTriggerManagerProviding
+ __OBJC_$_PROTOCOL_REFS_CSVoiceTriggerManagerProviding
+ __OBJC_CLASS_RO_$_SSRVoiceProfileEmbeddingTrainer
+ __OBJC_LABEL_PROTOCOL_$_CSVoiceTriggerManagerProviding
+ __OBJC_METACLASS_RO_$_SSRVoiceProfileEmbeddingTrainer
+ __OBJC_PROTOCOL_$_CSVoiceTriggerManagerProviding
+ __OBJC_PROTOCOL_REFERENCE_$_CSVoiceTriggerManagerProviding
+ ___71-[SSRSpeakerRecognitionOrchestrator fetchFinalEmbeddingWithCompletion:]_block_invoke
+ ___73-[SSRVTUITrainingManager _startAudioSessionAfterVoiceTrigger:forSession:]_block_invoke
+ ___73-[SSRVTUITrainingManager _startAudioSessionAfterVoiceTrigger:forSession:]_block_invoke_2
+ ___91-[SSRVoiceProfileManager extractEmbeddingFromSession:toProfile:withContext:withCompletion:]_block_invoke
+ ___92-[SSRVoiceProfileStore addUserVoiceProfile:withSpeakerEmbedding:withContext:withCompletion:]_block_invoke
+ ___block_descriptor_48_e8_32s40bs_e37_v28?0"CSVTUITrainingResult"8B16^20ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e23_v28?0B8Q12"NSError"20lw40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e16_v16?0"NSData"8ls32l8s48l8s40l8
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- GCC_except_table1003
- GCC_except_table1004
- GCC_except_table1007
- GCC_except_table1008
- GCC_except_table1009
- GCC_except_table1010
- GCC_except_table1011
- GCC_except_table1012
- GCC_except_table1013
- GCC_except_table1014
- GCC_except_table1015
- GCC_except_table1016
- GCC_except_table1018
- GCC_except_table1021
- GCC_except_table1101
- GCC_except_table1111
- GCC_except_table1181
- GCC_except_table1185
- GCC_except_table1203
- GCC_except_table1303
- GCC_except_table1304
- GCC_except_table1306
- GCC_except_table1327
- GCC_except_table1331
- GCC_except_table1340
- GCC_except_table1345
- GCC_except_table1349
- GCC_except_table1410
- GCC_except_table1416
- GCC_except_table1420
- GCC_except_table1424
- GCC_except_table1427
- GCC_except_table1433
- GCC_except_table1434
- GCC_except_table1442
- GCC_except_table1471
- GCC_except_table1520
- GCC_except_table1535
- GCC_except_table1558
- GCC_except_table1605
- GCC_except_table1612
- GCC_except_table1634
- GCC_except_table1661
- GCC_except_table1761
- GCC_except_table1767
- GCC_except_table1782
- GCC_except_table1792
- GCC_except_table1802
- GCC_except_table1807
- GCC_except_table1827
- GCC_except_table1831
- GCC_except_table1837
- GCC_except_table1845
- GCC_except_table187
- GCC_except_table190
- GCC_except_table1909
- GCC_except_table1913
- GCC_except_table192
- GCC_except_table1974
- GCC_except_table2009
- GCC_except_table2075
- GCC_except_table2085
- GCC_except_table2094
- GCC_except_table2133
- GCC_except_table2195
- GCC_except_table258
- GCC_except_table275
- GCC_except_table281
- GCC_except_table338
- GCC_except_table357
- GCC_except_table386
- GCC_except_table394
- GCC_except_table404
- GCC_except_table407
- GCC_except_table447
- GCC_except_table508
- GCC_except_table560
- GCC_except_table579
- GCC_except_table592
- GCC_except_table668
- GCC_except_table677
- GCC_except_table679
- GCC_except_table778
- GCC_except_table856
- GCC_except_table897
- GCC_except_table902
- GCC_except_table921
- ___block_descriptor_72_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s64l8s56l8
- _swift_retain_x28
CStrings:
+ "%s Audio provider selector does not provide a voice trigger, enrollment will not wait for a voice trigger"
+ "%s ERR: Failed to add speaker embedding to %{public}@ with error %{public}@"
+ "%s Exclave voice trigger detected, recording from sample count %llu"
+ "%s Exclave voice trigger was not detected : %{public}@"
+ "%s Live transcriber has text; finalizing at endpoint without EOS window"
+ "%s Setting start recording sample count to %llu"
+ "%s Waiting for the exclave voice trigger before recording"
+ "+[SSRVoiceProfileEmbeddingTrainer _errorWithCode:reason:]"
+ "-[CSVTUIAudioSessionRecorder setAudioRecordingSampleCount:]"
+ "-[SSRVTUITrainingManager _builtInVoiceTrigger]"
+ "-[SSRVTUITrainingManager _startAudioSessionAfterVoiceTrigger:forSession:]"
+ "-[SSRVTUITrainingManager _startAudioSessionAfterVoiceTrigger:forSession:]_block_invoke"
+ "-[SSRVTUITrainingManager _startAudioSessionAfterVoiceTrigger:forSession:]_block_invoke_2"
+ "-[SSRVoiceProfileManager extractEmbeddingFromSession:toProfile:withContext:withCompletion:]"
+ "-[SSRVoiceProfileManager extractEmbeddingFromSession:toProfile:withContext:withCompletion:]_block_invoke"
+ "-[SSRVoiceProfileStore addUserVoiceProfile:withSpeakerEmbedding:withContext:withCompletion:]_block_invoke"
+ "Cannot copy the model to %@: %@"
+ "Cannot create the scorer for the speaker embedding"
+ "Cannot reset the model for the speaker embedding"
+ "No PSR model context to add the speaker embedding to"
+ "No speaker recognition session to extract the embedding from"
+ "Speaker embedding is empty"
+ "Speaker embedding was not added to the model"
+ "The speaker recognition pass has no embedding"
+ "corespeech.uitrainingservice"
+ "v16@?0@\"NSData\"8"
+ "v28@?0B8Q12@\"NSError\"20"
+ "\x81"
```
