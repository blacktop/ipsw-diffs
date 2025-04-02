## SpeakerRecognition

> `/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x88854
-  __TEXT.__auth_stubs: 0x10c0
-  __TEXT.__objc_methlist: 0x6248
-  __TEXT.__const: 0x468
+3405.20.3.0.0
+  __TEXT.__text: 0x8c5a8
+  __TEXT.__auth_stubs: 0x1410
+  __TEXT.__objc_methlist: 0x62e0
+  __TEXT.__const: 0x4c8
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__swift5_typeref: 0x17e
+  __TEXT.__cstring: 0xfbe1
+  __TEXT.__swift5_typeref: 0x17a
+  __TEXT.__constg_swiftt: 0x3c4
+  __TEXT.__swift5_fieldmd: 0x170
+  __TEXT.__swift5_reflstr: 0x1ca
+  __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_capture: 0x54
-  __TEXT.__cstring: 0xee04
-  __TEXT.__constg_swiftt: 0x2d4
-  __TEXT.__swift5_reflstr: 0x144
-  __TEXT.__swift5_fieldmd: 0x118
-  __TEXT.__swift5_types: 0xc
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__gcc_except_tab: 0x2d50
-  __TEXT.__oslogstring: 0xc390
-  __TEXT.__unwind_info: 0x1878
+  __TEXT.__oslogstring: 0xc48d
+  __TEXT.__unwind_info: 0x18d8
   __TEXT.__eh_frame: 0x180
   __TEXT.__objc_classname: 0xd99
-  __TEXT.__objc_methname: 0x11452
-  __TEXT.__objc_methtype: 0x24b7
+  __TEXT.__objc_methname: 0x114c7
+  __TEXT.__objc_methtype: 0x24da
   __TEXT.__objc_stubs: 0xa3a0
-  __DATA_CONST.__got: 0x8e8
+  __DATA_CONST.__got: 0x970
   __DATA_CONST.__const: 0x1d48
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3a28
+  __DATA_CONST.__objc_selrefs: 0x3a40
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x390
-  __AUTH_CONST.__auth_got: 0x878
-  __AUTH_CONST.__auth_ptr: 0x60
-  __AUTH_CONST.__const: 0x4b8
+  __AUTH_CONST.__auth_got: 0xa20
+  __AUTH_CONST.__auth_ptr: 0x90
+  __AUTH_CONST.__const: 0x4d8
   __AUTH_CONST.__cfstring: 0x51c0
-  __AUTH_CONST.__objc_const: 0xa700
+  __AUTH_CONST.__objc_const: 0xa800
   __AUTH_CONST.__objc_dictobj: 0x8e8
   __AUTH_CONST.__objc_intobj: 0x168
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x8d8
+  __AUTH.__objc_data: 0x9d8
   __AUTH.__data: 0x78
-  __DATA.__objc_ivar: 0x7ec
-  __DATA.__data: 0x10a8
+  __DATA.__objc_ivar: 0x7f0
+  __DATA.__data: 0x1100
   __DATA.__bss: 0xf0
-  __DATA.__common: 0x68
+  __DATA.__common: 0x90
   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__bss: 0x48
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 2311
-  Symbols:   3011
-  CStrings:  5328
+  Functions: 2342
+  Symbols:   3016
+  CStrings:  5379
 
Symbols:
+ _bzero
+ _swift_endAccess
+ _swift_isaMask
- _OBJC_CLASS_$_CSKeywordAnalyzerNDAPIResult
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
