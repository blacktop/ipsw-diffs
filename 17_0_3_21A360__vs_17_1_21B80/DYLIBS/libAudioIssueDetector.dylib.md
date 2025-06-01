## libAudioIssueDetector.dylib

> `/usr/lib/libAudioIssueDetector.dylib`

```diff

-691.1.19.0.0
-  __TEXT.__text: 0x404a0
-  __TEXT.__auth_stubs: 0xfa0
-  __TEXT.__objc_methlist: 0x530
+691.2.8.0.0
+  __TEXT.__text: 0x41294
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__objc_methlist: 0x548
   __TEXT.__const: 0x269
-  __TEXT.__gcc_except_tab: 0x2edc
-  __TEXT.__cstring: 0x19c4
-  __TEXT.__oslogstring: 0x36e4
-  __TEXT.__unwind_info: 0x1148
+  __TEXT.__gcc_except_tab: 0x300c
+  __TEXT.__cstring: 0x19c6
+  __TEXT.__oslogstring: 0x394b
+  __TEXT.__unwind_info: 0x1150
   __TEXT.__eh_frame: 0x38
-  __TEXT.__objc_classname: 0x18f
-  __TEXT.__objc_methname: 0x1c4c
-  __TEXT.__objc_methtype: 0xc59
-  __TEXT.__objc_stubs: 0x1860
+  __TEXT.__objc_classname: 0x193
+  __TEXT.__objc_methname: 0x1e26
+  __TEXT.__objc_methtype: 0xc89
+  __TEXT.__objc_stubs: 0x1a00
   __DATA_CONST.__got: 0x1f0
   __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1248
-  __DATA_CONST.__objc_selrefs: 0x730
+  __DATA_CONST.__objc_const: 0x12e8
+  __DATA_CONST.__objc_selrefs: 0x798
   __AUTH_CONST.__const: 0x1210
   __AUTH_CONST.__objc_const: 0x480
-  __AUTH_CONST.__cfstring: 0x8a0
+  __AUTH_CONST.__cfstring: 0x8e0
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x7e8
+  __AUTH_CONST.__auth_got: 0x7f0
   __AUTH.__objc_data: 0x140
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x1c0
+  __DATA.__objc_classrefs: 0x1f0
   __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0xf0
+  __DATA.__objc_ivar: 0x104
   __DATA.__data: 0x2a0
-  __DATA.__bss: 0x114
+  __DATA.__bss: 0x11c
   __DATA_DIRTY.__objc_data: 0x280
   __DATA_DIRTY.__data: 0x260
   __DATA_DIRTY.__bss: 0x3c8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FD467C5B-EA89-32C8-B7EE-BE9566B7DF56
-  Functions: 782
-  Symbols:   2732
-  CStrings:  1009
+  UUID: E32D809C-5FD9-3533-94DC-DBFE1A28A153
+  Functions: 783
+  Symbols:   2761
+  CStrings:  1036
 
Symbols:
+ -[ADAMSRSensorWriter provideSample:error:]
+ -[ADAMSoundAnalysisWriter _isMonitoringSpeechMetrics]
+ -[ADAMSoundAnalysisWriter initWithWriterName:sessionID:audioFormat:speechMetricsSRWriter:soundDetectionSRWriter:speechEmotionSRWriter:completionHandler:]
+ -[ADAMSpeechAnalysisWriter initWithWriterName:sessionID:audioFormat:speechMetricsSRWriter:completionHandler:]
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table659
+ GCC_except_table663
+ GCC_except_table670
+ GCC_except_table674
+ GCC_except_table679
+ GCC_except_table682
+ GCC_except_table689
+ GCC_except_table691
+ GCC_except_table700
+ GCC_except_table707
+ GCC_except_table711
+ GCC_except_table714
+ GCC_except_table716
+ GCC_except_table734
+ GCC_except_table739
+ GCC_except_table745
+ GCC_except_table756
+ GCC_except_table763
+ GCC_except_table774
+ _OBJC_CLASS_$_SNClassificationResult
+ _OBJC_CLASS_$_SNLKFSResult
+ _OBJC_CLASS_$_SNMeasureLKFSRequest
+ _OBJC_CLASS_$_SRAudioLevel
+ _OBJC_CLASS_$_SRSpeechExpression
+ _OBJC_CLASS_$_SRSpeechMetrics
+ _OBJC_IVAR_$_ADAMSoundAnalysisWriter._audioLevelRequest
+ _OBJC_IVAR_$_ADAMSoundAnalysisWriter._audioLevelTimestamp
+ _OBJC_IVAR_$_ADAMSoundAnalysisWriter._sessionID
+ _OBJC_IVAR_$_ADAMSoundAnalysisWriter._speechMetricsSRWriter
+ _OBJC_IVAR_$_ADAMSpeechAnalysisWriter._sessionID
+ _SRAbsoluteTimeToCFAbsoluteTime
+ __ZN4ADAM15SensorKitWriter17sSessionIDCounterE
+ __ZN5boost9typeindex6detailL23ctti_skip_until_runtimeE.785
+ __ZN5boost9typeindex6detailL23ctti_skip_until_runtimeE.818
+ ____Z28AudioStatisticsLibraryLoaderv_block_invoke.1169
+ ____Z28AudioStatisticsLibraryLoaderv_block_invoke.537
+ ___block_descriptor_tmp.1042
+ ___block_descriptor_tmp.535
+ ___block_literal_global.1016
+ ___block_literal_global.1040
+ ___block_literal_global.1160
+ ___block_literal_global.398
+ ___block_literal_global.532
+ ___block_literal_global.913
+ _objc_msgSend$_isMonitoringSpeechMetrics
+ _objc_msgSend$arousal
+ _objc_msgSend$decibelLevel
+ _objc_msgSend$dominance
+ _objc_msgSend$initWithClassificationDictionary:
+ _objc_msgSend$initWithSessionIdentifier:sessionFlags:timestamp:audioLevel:speechRecognition:soundClassification:speechExpression:
+ _objc_msgSend$initWithTimeRange:loudness:
+ _objc_msgSend$initWithVersion:timeRange:confidence:mood:valence:activation:dominance:
+ _objc_msgSend$initWithWriterName:sessionID:audioFormat:speechMetricsSRWriter:completionHandler:
+ _objc_msgSend$initWithWriterName:sessionID:audioFormat:speechMetricsSRWriter:soundDetectionSRWriter:speechEmotionSRWriter:completionHandler:
+ _objc_msgSend$mood
+ _objc_msgSend$provideSample:error:
+ _objc_msgSend$setTimeRange:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$valence
- -[ADAMSoundAnalysisWriter initWithWriterName:audioFormat:soundDetectionSRWriter:speechEmotionSRWriter:completionHandler:]
- -[ADAMSpeechAnalysisWriter initWithWriterName:audioFormat:speechMetricsSRWriter:completionHandler:]
- GCC_except_table252
- GCC_except_table254
- GCC_except_table661
- GCC_except_table667
- GCC_except_table673
- GCC_except_table677
- GCC_except_table680
- GCC_except_table688
- GCC_except_table690
- GCC_except_table699
- GCC_except_table704
- GCC_except_table710
- GCC_except_table713
- GCC_except_table715
- GCC_except_table733
- GCC_except_table738
- GCC_except_table744
- GCC_except_table755
- GCC_except_table762
- GCC_except_table772
- __ZN4ADAM7get_logEv
- __ZN5boost9typeindex6detailL23ctti_skip_until_runtimeE.782
- __ZN5boost9typeindex6detailL23ctti_skip_until_runtimeE.814
- ____Z28AudioStatisticsLibraryLoaderv_block_invoke.1161
- ____Z28AudioStatisticsLibraryLoaderv_block_invoke.533
- ___block_descriptor_tmp.1035
- ___block_descriptor_tmp.531
- ___block_literal_global.1009
- ___block_literal_global.1033
- ___block_literal_global.1152
- ___block_literal_global.394
- ___block_literal_global.528
- ___block_literal_global.908
- _objc_msgSend$initWithWriterName:audioFormat:soundDetectionSRWriter:speechEmotionSRWriter:completionHandler:
- _objc_msgSend$initWithWriterName:audioFormat:speechMetricsSRWriter:completionHandler:
CStrings:
+ "\x02\x12\"2A"
+ "\x021!\x11\x15\xf01"
+ "%25s:%-5d Created ADAM SN Writer: %@ monitoring emotion? %@, monitoring detecion? %@, monitoring speech metrics? %@, num requests: %lu"
+ "%25s:%-5d failed to write SRSpeechMetrics result to SensorKit: %@, continuous timestamp: continuous %llu, absolute %f, err: %@"
+ "1"
+ "@\"SNMeasureLKFSRequest\""
+ "@52@0:8@16I24@28@36@?44"
+ "@68@0:8@16I24@28@36@44@52@?60"
+ "B32@0:8@16^@24"
+ "[%s:%-5d %.*s:%p] Write SNLKFSResult result: %@, timestamp: continuous %llu, absolute %f"
+ "[%s:%-5d %.*s:%p] Write SRSpeechMetrics result: %@, timestamp: continuous %llu, absolute %f"
+ "[%s:%-5d %.*s:%p] Write SpeechExpression result: %@, timestamp: continuous %llu, absolute %f"
+ "[%s:%-5d %.*s:%p] added SNMeasureAudioLevelRequest"
+ "[%s:%-5d %.*s:%p] failed to add SNMeasureAudioLevelRequest"
+ "[%s:%-5d %.*s:%p] failed to write SNLKFSResult result to SensorKit: %@, continuous timestamp: continuous %llu, absolute %f, err: %@"
+ "[%s:%-5d %.*s:%p] failed to write SRSpeechMetrics result to SensorKit: %@, timestamp: continuous %llu, absolute %f, err: %@"
+ "_audioLevelRequest"
+ "_audioLevelTimestamp"
+ "_isMonitoringSpeechMetrics"
+ "_sessionID"
+ "arousal"
+ "decibelLevel"
+ "dominance"
+ "initWithClassificationDictionary:"
+ "initWithSessionIdentifier:sessionFlags:timestamp:audioLevel:speechRecognition:soundClassification:speechExpression:"
+ "initWithTimeRange:loudness:"
+ "initWithVersion:timeRange:confidence:mood:valence:activation:dominance:"
+ "initWithWriterName:sessionID:audioFormat:speechMetricsSRWriter:completionHandler:"
+ "initWithWriterName:sessionID:audioFormat:speechMetricsSRWriter:soundDetectionSRWriter:speechEmotionSRWriter:completionHandler:"
+ "mood"
+ "provideSample:error:"
+ "setTimeRange:"
+ "stringWithFormat:"
+ "valence"
- "\x02\x12\"2"
- "\x021!$"
- "%25s:%-5d Created ADAM SN Writer: %@ monitoring emotion? %@, monitoring detecion? %@ num requests: %lu"
- "@48@0:8@16@24@32@?40"
- "@56@0:8@16@24@32@40@?48"
- "[%s:%-5d %.*s:%p] Write SNDetectionResult result: %@, timestamp: continuous %llu, absolute %f"
- "[%s:%-5d %.*s:%p] Write SpeechEmotion result: %@, timestamp: continuous %llu, absolute %f"
- "initWithWriterName:audioFormat:soundDetectionSRWriter:speechEmotionSRWriter:completionHandler:"
- "initWithWriterName:audioFormat:speechMetricsSRWriter:completionHandler:"

```
