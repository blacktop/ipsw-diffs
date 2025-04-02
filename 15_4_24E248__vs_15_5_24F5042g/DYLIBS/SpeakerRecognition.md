## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/Versions/A/SpeakerRecognition`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x84804
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x5cc8
-  __TEXT.__const: 0x408
-  __TEXT.__cstring: 0xdfb2
-  __TEXT.__swift5_typeref: 0xe8
-  __TEXT.__swift5_fieldmd: 0xc0
-  __TEXT.__constg_swiftt: 0x204
-  __TEXT.__swift5_reflstr: 0xf4
-  __TEXT.__swift5_types: 0x8
+3405.20.3.0.0
+  __TEXT.__text: 0x88628
+  __TEXT.__auth_stubs: 0x10f0
+  __TEXT.__objc_methlist: 0x5d58
+  __TEXT.__const: 0x478
+  __TEXT.__cstring: 0xed7f
+  __TEXT.__swift5_typeref: 0xe4
+  __TEXT.__constg_swiftt: 0x2f4
+  __TEXT.__swift5_fieldmd: 0x118
+  __TEXT.__swift5_reflstr: 0x18a
+  __TEXT.__swift5_types: 0xc
   __TEXT.__gcc_except_tab: 0x2504
-  __TEXT.__oslogstring: 0xbabc
-  __TEXT.__unwind_info: 0x16d8
+  __TEXT.__oslogstring: 0xbbb9
+  __TEXT.__unwind_info: 0x1730
   __TEXT.__objc_classname: 0xd73
-  __TEXT.__objc_methname: 0x10839
-  __TEXT.__objc_methtype: 0x2357
+  __TEXT.__objc_methname: 0x108ae
+  __TEXT.__objc_methtype: 0x2389
   __TEXT.__objc_stubs: 0x9880
-  __DATA_CONST.__got: 0x8f8
+  __DATA_CONST.__got: 0x980
   __DATA_CONST.__const: 0x788
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3778
+  __DATA_CONST.__objc_selrefs: 0x3790
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x370
-  __AUTH_CONST.__auth_got: 0x6c8
-  __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x1b60
+  __AUTH_CONST.__auth_got: 0x890
+  __AUTH_CONST.__auth_ptr: 0x50
+  __AUTH_CONST.__const: 0x1b80
   __AUTH_CONST.__cfstring: 0x5220
-  __AUTH_CONST.__objc_const: 0x9cc8
+  __AUTH_CONST.__objc_const: 0x9dc8
   __AUTH_CONST.__objc_dictobj: 0x898
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1d90
+  __AUTH.__objc_data: 0x1e90
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x738
-  __DATA.__data: 0xf48
+  __DATA.__objc_ivar: 0x73c
+  __DATA.__data: 0xfa0
   __DATA.__bss: 0x130
-  __DATA.__common: 0x60
+  __DATA.__common: 0x88
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2193
-  Symbols:   5552
-  CStrings:  5122
+  Functions: 2225
+  Symbols:   5567
+  CStrings:  5174
 
Symbols:
+ -[CSVTUIKeywordDetector analyzeWithBuffer:]
+ -[CSVTUIKeywordDetector triggeredUtteranceWithVoiceTriggerEventInfo:]
+ -[CSVTUITwoPassKeywordDetector analyzeWithBuffer:]
+ -[CSVTUITwoPassKeywordDetector triggeredUtteranceWithVoiceTriggerEventInfo:]
+ -[SSRVTUITrainingManager _fetchPreInstalledSecureAsset]
+ -[SSRVTUITrainingManager _otaAssetsAvailable]
+ -[SSRVTUITrainingManager _secureAssetWithAssetResourcePathURL:assetFileName:]
+ GCC_except_table1013
+ GCC_except_table1069
+ GCC_except_table1073
+ GCC_except_table1091
+ GCC_except_table1177
+ GCC_except_table1179
+ GCC_except_table1197
+ GCC_except_table1201
+ GCC_except_table1210
+ GCC_except_table1220
+ GCC_except_table1226
+ GCC_except_table1277
+ GCC_except_table1283
+ GCC_except_table1290
+ GCC_except_table1319
+ GCC_except_table1332
+ GCC_except_table1362
+ GCC_except_table1368
+ GCC_except_table1437
+ GCC_except_table1546
+ GCC_except_table1561
+ GCC_except_table1573
+ GCC_except_table1583
+ GCC_except_table1588
+ GCC_except_table1605
+ GCC_except_table1609
+ GCC_except_table1618
+ GCC_except_table1633
+ GCC_except_table1708
+ GCC_except_table1712
+ GCC_except_table1751
+ GCC_except_table1786
+ GCC_except_table1851
+ GCC_except_table1862
+ GCC_except_table1871
+ GCC_except_table1882
+ GCC_except_table1892
+ GCC_except_table1909
+ GCC_except_table734
+ GCC_except_table774
+ GCC_except_table781
+ GCC_except_table814
+ GCC_except_table888
+ GCC_except_table901
+ GCC_except_table906
+ GCC_except_table911
+ GCC_except_table988
+ OBJC_IVAR_$_SSRVTUITrainingManager._currentSecureAsset
+ __37-[SSRVTUITrainingManager audioSource]_block_invoke.101
+ __46-[SSRVTUITrainingManager cancelTrainingForID:]_block_invoke.94
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.41
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.50
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.51
+ __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_2.42
+ __55-[SSRVTUITrainingManager playSoundEffectWithAudioTone:]_block_invoke.91
+ __82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke.57
+ __82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_2.58
+ __Block_byref_object_copy_.1666
+ __Block_byref_object_copy_.1877
+ __Block_byref_object_copy_.2038
+ __Block_byref_object_copy_.2692
+ __Block_byref_object_copy_.3236
+ __Block_byref_object_copy_.3391
+ __Block_byref_object_copy_.3560
+ __Block_byref_object_copy_.4320
+ __Block_byref_object_copy_.4640
+ __Block_byref_object_copy_.4831
+ __Block_byref_object_copy_.4918
+ __Block_byref_object_copy_.5152
+ __Block_byref_object_copy_.6012
+ __Block_byref_object_copy_.6415
+ __Block_byref_object_copy_.6529
+ __Block_byref_object_copy_.6755
+ __Block_byref_object_copy_.7116
+ __Block_byref_object_dispose_.1667
+ __Block_byref_object_dispose_.1878
+ __Block_byref_object_dispose_.2039
+ __Block_byref_object_dispose_.2693
+ __Block_byref_object_dispose_.3237
+ __Block_byref_object_dispose_.3392
+ __Block_byref_object_dispose_.3561
+ __Block_byref_object_dispose_.4321
+ __Block_byref_object_dispose_.4641
+ __Block_byref_object_dispose_.4832
+ __Block_byref_object_dispose_.4919
+ __Block_byref_object_dispose_.5153
+ __Block_byref_object_dispose_.6013
+ __Block_byref_object_dispose_.6416
+ __Block_byref_object_dispose_.6530
+ __Block_byref_object_dispose_.6756
+ __Block_byref_object_dispose_.7117
+ __PROTOCOL_INSTANCE_METHODS__TtP18SpeakerRecognition29CSVTUIKeywordDetectorProtocol_
+ __PROTOCOL_METHOD_TYPES__TtP18SpeakerRecognition29CSVTUIKeywordDetectorProtocol_
+ __PROTOCOL__TtP18SpeakerRecognition29CSVTUIKeywordDetectorProtocol_
+ __block_literal_global.1674
+ __block_literal_global.2606
+ __block_literal_global.3414
+ __block_literal_global.3476
+ __block_literal_global.49
+ __block_literal_global.5238
+ __block_literal_global.5449
+ __block_literal_global.6197
+ __block_literal_global.6538
+ __block_literal_global.6790
+ __block_literal_global.7005
+ __block_literal_global.7305
+ __block_literal_global.8147
+ _bzero
+ _objc_msgSend$analyzeWithBuffer:
+ _objc_msgSend$triggeredUtteranceWithVoiceTriggerEventInfo:
+ _swift_beginAccess
+ _swift_endAccess
+ _swift_getSingletonMetadata
+ _swift_isaMask
+ _swift_retain
+ _swift_updateClassMetadata2
+ _symbolic $s18SpeakerRecognition29CSVTUIKeywordDetectorProtocolP
+ _symbolic So22CSPlainAudioFileWriterCSg
+ _symbolic _____ 18SpeakerRecognition7VTEIKeyO
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg 15CoreSpeechUtils20SecurePhraseDetectorC
+ _symbolic _____Sg 15CoreSpeechUtils20SecureVTPhraseConfigV
+ _symbolic _____Sg 15CoreSpeechUtils24SecureSinglePhraseResultV
+ _symbolic _____Sg 15CoreSpeechUtils26SecureKeywordAnalyzerNDAPIC
+ _symbolic _____Sg 15CoreSpeechUtils32SecureKeywordAnalyzerNDAPIResultV
+ sharedInstance.onceToken.3475
+ sharedInstance.onceToken.7304
+ sharedManager.onceToken.6789
- -[CSVTUIKeywordDetector analyze:]
- -[CSVTUIKeywordDetector triggeredUtterance:]
- -[CSVTUITwoPassKeywordDetector analyze:]
- -[CSVTUITwoPassKeywordDetector triggeredUtterance:]
- GCC_except_table1010
- GCC_except_table1066
- GCC_except_table1070
- GCC_except_table1088
- GCC_except_table1173
- GCC_except_table1174
- GCC_except_table1194
- GCC_except_table1198
- GCC_except_table1207
- GCC_except_table1217
- GCC_except_table1223
- GCC_except_table1274
- GCC_except_table1280
- GCC_except_table1287
- GCC_except_table1316
- GCC_except_table1329
- GCC_except_table1359
- GCC_except_table1365
- GCC_except_table1434
- GCC_except_table1543
- GCC_except_table1558
- GCC_except_table1570
- GCC_except_table1580
- GCC_except_table1585
- GCC_except_table1602
- GCC_except_table1606
- GCC_except_table1615
- GCC_except_table1630
- GCC_except_table1705
- GCC_except_table1709
- GCC_except_table1748
- GCC_except_table1783
- GCC_except_table1848
- GCC_except_table1859
- GCC_except_table1868
- GCC_except_table1879
- GCC_except_table1889
- GCC_except_table1906
- GCC_except_table731
- GCC_except_table771
- GCC_except_table778
- GCC_except_table808
- GCC_except_table885
- GCC_except_table886
- GCC_except_table893
- GCC_except_table894
- GCC_except_table985
- _OBJC_CLASS_$_CSKeywordAnalyzerNDAPIResult
- __37-[SSRVTUITrainingManager audioSource]_block_invoke.97
- __46-[SSRVTUITrainingManager cancelTrainingForID:]_block_invoke.90
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.37
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.39
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke.42
- __48-[SSRVTUITrainingManager cleanupWithCompletion:]_block_invoke_2.38
- __55-[SSRVTUITrainingManager playSoundEffectWithAudioTone:]_block_invoke.87
- __82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke.53
- __82-[SSRVTUITrainingManager trainUtterance:shouldUseASR:mhUUID:completionWithResult:]_block_invoke_2.54
- __Block_byref_object_copy_.1669
- __Block_byref_object_copy_.1880
- __Block_byref_object_copy_.2041
- __Block_byref_object_copy_.2694
- __Block_byref_object_copy_.3243
- __Block_byref_object_copy_.3397
- __Block_byref_object_copy_.3565
- __Block_byref_object_copy_.4322
- __Block_byref_object_copy_.4638
- __Block_byref_object_copy_.4828
- __Block_byref_object_copy_.4914
- __Block_byref_object_copy_.5148
- __Block_byref_object_copy_.6006
- __Block_byref_object_copy_.6410
- __Block_byref_object_copy_.6524
- __Block_byref_object_copy_.6750
- __Block_byref_object_copy_.7115
- __Block_byref_object_dispose_.1670
- __Block_byref_object_dispose_.1881
- __Block_byref_object_dispose_.2042
- __Block_byref_object_dispose_.2695
- __Block_byref_object_dispose_.3244
- __Block_byref_object_dispose_.3398
- __Block_byref_object_dispose_.3566
- __Block_byref_object_dispose_.4323
- __Block_byref_object_dispose_.4639
- __Block_byref_object_dispose_.4829
- __Block_byref_object_dispose_.4915
- __Block_byref_object_dispose_.5149
- __Block_byref_object_dispose_.6007
- __Block_byref_object_dispose_.6411
- __Block_byref_object_dispose_.6525
- __Block_byref_object_dispose_.6751
- __Block_byref_object_dispose_.7116
- __PROTOCOL_INSTANCE_METHODS__TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_
- __PROTOCOL_METHOD_TYPES__TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_
- __PROTOCOL__TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_
- __block_literal_global.1676
- __block_literal_global.2610
- __block_literal_global.3420
- __block_literal_global.3482
- __block_literal_global.45
- __block_literal_global.5234
- __block_literal_global.5442
- __block_literal_global.6190
- __block_literal_global.6533
- __block_literal_global.6785
- __block_literal_global.7000
- __block_literal_global.7304
- __block_literal_global.8144
- _objc_msgSend$analyze:
- _objc_msgSend$triggeredUtterance:
- _symbolic $s18SpeakerRecognition26CSVTUIKeywordDetectorSwiftP
- _symbolic So16CSPhraseDetectorCSg
- _symbolic So22CSKeywordAnalyzerNDAPICSg
- _symbolic So29SSRTriggerPhraseDetectorNDAPICSg
- sharedInstance.onceToken.3481
- sharedInstance.onceToken.7303
- sharedManager.onceToken.6784
CStrings:
+ "\x17)\x131"
+ " CSVTUIKeywordDetectorHelper - audioChunkForFirstPass numSamples:%lu numChannel:%lu sampleDepthInBytes:%lu sampleCount:%lu"
+ " CSVTUIKeywordDetectorHelper - buffer.count:%lu, dataArr.count:%lu, sampleCount:%lu isFloat:%u"
+ " CSVTUIKeywordDetectorHelper - failed since keywordAnalyzer is nil!"
+ " CSVTUIKeywordDetectorHelper - failed to get BestAnalyzedResultFromAudioChunk"
+ " CSVTUITwoPassKeywordDetectorHelper - Init Done!"
+ " CSVTUITwoPassKeywordDetectorHelper - Init phraseDetector. :%f"
+ " CSVTUITwoPassKeywordDetectorHelper - Init phraseDetector. extraSamplesAtStart:%lu, analyzerTrailingSamples:%lu"
+ " CSVTUITwoPassKeywordDetectorHelper - Waiting for the entire audio, samplesInBuffer %lu triggerStartSampleCount:%lu triggerSampleFedCount %lu samplesFed:%lu"
+ " CSVTUITwoPassKeywordDetectorHelper - audioChunkForFirstPass numSamples:%lu numChannel:%lu sampleDepthInBytes:%lu sampleCount:%lu"
+ " CSVTUITwoPassKeywordDetectorHelper - buffer.count:%lu, dataArr.count:%lu, sampleCount:%lu isFloat:%u"
+ " CSVTUITwoPassKeywordDetectorHelper - failed since keywordAnalyzer is nil!"
+ " CSVTUITwoPassKeywordDetectorHelper - failed to get BestAnalyzedResultFromAudioChunk"
+ " CSVTUITwoPassKeywordDetectorHelper - firstPassResult received, self.isFirstPassTriggered:%u"
+ " CSVTUITwoPassKeywordDetectorHelper - getBestStart:%lu getBestEnd:%lu getSamplesFed: %lu, getSamplesAtFire:%lu totalSamples:%lu"
+ " CSVTUITwoPassKeywordDetectorHelper - internalReset Done!"
+ " CSVTUITwoPassKeywordDetectorHelper - internalReset Started!"
+ " CSVTUITwoPassKeywordDetectorHelper - isFirstPassTriggered:%u, keywordScore:%f self.keywordThreshold:%f"
+ " CSVTUITwoPassKeywordDetectorHelper - keywordAnalyzer- internalReset Done!"
+ " CSVTUITwoPassKeywordDetectorHelper - phraseDetector- internalReset Done!"
+ " CSVTUITwoPassKeywordDetectorHelper - resetting audioBuffer!"
+ " CSVTUITwoPassKeywordDetectorHelper - supportsMph:%u"
+ " CSVTUITwoPassKeywordDetectorHelper -FirstPass Failed! keywordScore:%f, keywordThreshold:%f"
+ "%s Fetching VoiceTrigger secure asset with config file name:%@ at path: %{private}@"
+ "%s Skipping operation to fetch VoiceTrigger secure asset with config file name:%@ at path: %{private}@"
+ "%s preInstalledBundle:%@ config file name:%@ at path: %{private}@"
+ "-[CSVTUITwoPassKeywordDetector analyzeWithBuffer:]"
+ "-[SSRVTUITrainingManager _fetchPreInstalledSecureAsset]"
+ "@\"<CSVTUIKeywordDetectorProtocol>\""
+ "@\"SecureAsset\""
+ "@24@0:8@\"CSAsset\"16"
+ "@28@0:8@\"CSAsset\"16B24"
+ "@28@0:8@\"SecureAsset\"16B24"
+ "CSVTUIKeywordDetectorHelper - Cannot create CSVTUIKeywordDetectorHelper since we cannot access secureConfigDataNdapiString"
+ "CSVTUIKeywordDetectorHelper - Cannot create CSVTUIKeywordDetectorHelper since we cannot initialize NDAPI"
+ "CSVTUIKeywordDetectorHelper - Cannot get VT First pass config"
+ "CSVTUIKeywordDetectorHelper: firstPassConfigPath:%@"
+ "CSVTUITwoPassKeywordDetectorHelper - Cannot create CSVTUITwoPassKeywordDetectorHelper since we cannot access secureConfigDataNdapiString"
+ "CSVTUITwoPassKeywordDetectorHelper - Cannot create CSVTUITwoPassKeywordDetectorHelper since we cannot initialize NDAPI"
+ "CSVTUITwoPassKeywordDetectorHelper - Cannot get VT First pass config"
+ "CSVTUITwoPassKeywordDetectorHelper - Failure in getting the detector info for the phrase"
+ "CSVTUITwoPassKeywordDetectorHelper - First Pass did not trigger.."
+ "CSVTUITwoPassKeywordDetectorHelper - Phrase detector result: %@"
+ "CSVTUITwoPassKeywordDetectorHelper - Second pass has required audio samples:%lu, stop feeding"
+ "CSVTUITwoPassKeywordDetectorHelper - calling getAnalyzedResultFromAudioChunk, with numSamples:%lu, numChannel:%lu, sampleByteDepth:%lu, sampleCount:%lu, bufferArrivalTime:%lu"
+ "CSVTUITwoPassKeywordDetectorHelper - failed to get keywordDetectorResult"
+ "CSVTUITwoPassKeywordDetectorHelper - failed to get ndapiResult"
+ "CSVTUITwoPassKeywordDetectorHelper - isSecondPassTriggered: %u PhId:%u supportsMph:%u"
+ "CSVTUITwoPassKeywordDetectorHelper - numSamples: %lu"
+ "CSVTUITwoPassKeywordDetectorHelper - triggeredUtterance: %@"
+ "CSVTUITwoPassKeywordDetectorHelper secondPassConfig.memoryIndexesNdapi:%@"
+ "CSVTUITwoPassKeywordDetectorHelper- Report as rejection since the detected phId is not the default"
+ "CSVTUITwoPassKeywordDetectorHelper: firstPassConfigPath:%@"
+ "Cannot create CSVTUIKeywordDetectorHelper since we failed to NDAP mempry Index"
+ "Cannot create CSVTUITwoPassKeywordDetectorHelper since we failed to NDAP mempry Index"
+ "Secure-Enroll-Second-"
+ "_TtP18SpeakerRecognition29CSVTUIKeywordDetectorProtocol_"
+ "_currentSecureAsset"
+ "_fetchPreInstalledSecureAsset"
+ "_otaAssetsAvailable"
+ "arrivalHostTimeToAudioRecorder"
+ "assistantAudioFileLogDirectory"
+ "audioFileWriterSecondPass"
+ "config_1st_secure.txt"
+ "firstPassResult"
+ "initFileURLWithPath:"
+ "isFirstPassTriggered"
+ "numChannels"
+ "totalSamples"
+ "yyyy_MM_dd-HHmmss.SSS"
+ "\xf0\xa1"
- "\x17(\x131"
- " CSVTUITwoPassKeywordDetectorHelper - Init phraseDetector"
- "-[CSVTUITwoPassKeywordDetector analyze:]"
- "CSVTUIKeywordDetectorHelper: analyze result is nil!"
- "CSVTUIKeywordDetectorHelper: keywordAnalyzer:%@ "
- "CSVTUIKeywordDetectorHelper: resourcePath, configPath: is non nil"
- "Cannot create CSVTUIKeywordDetectorHelper since we cannot initialize NDAPI"
- "Cannot create CSVTUIKeywordDetectorHelper since we failed to fetch NDAPI memory Index"
- "Cannot create CSVTUITwoPassKeywordDetectorHelper since we cannot initialize NDAPI"
- "Cannot create CSVTUITwoPassKeywordDetectorHelper since we failed to NDAP memory Index"
- "Cannot get VT First pass config"
- "Cannot initialize phraseDetector"
- "Faiure in getting the detector info for the phrase"
- "Phrase detector result: %@"
- "Report as rejection since the detected phId is not the default"
- "Second pass has required audio, stop feeding"
- "Waiting for the entire audio.."
- "_TtP18SpeakerRecognition26CSVTUIKeywordDetectorSwift_"
- "analyze:"
- "getAnalyzedResults"
- "triggeredUtterance:"
- "\xf0\x91"

```
