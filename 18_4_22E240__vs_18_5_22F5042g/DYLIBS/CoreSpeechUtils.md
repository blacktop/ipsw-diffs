## CoreSpeechUtils

> `/System/Library/PrivateFrameworks/CoreSpeechUtils.framework/CoreSpeechUtils`

```diff

-3404.82.3.0.0
-  __TEXT.__text: 0x17234
-  __TEXT.__auth_stubs: 0x9d0
-  __TEXT.__objc_methlist: 0x3a4
-  __TEXT.__const: 0xb90
-  __TEXT.__cstring: 0x20cc
-  __TEXT.__swift5_typeref: 0x240
-  __TEXT.__oslogstring: 0x86e
-  __TEXT.__constg_swiftt: 0x3f4
-  __TEXT.__swift5_reflstr: 0x891
-  __TEXT.__swift5_fieldmd: 0x718
+3405.20.3.0.0
+  __TEXT.__text: 0x22278
+  __TEXT.__auth_stubs: 0xbc0
+  __TEXT.__objc_methlist: 0x3cc
+  __TEXT.__const: 0x10b0
+  __TEXT.__cstring: 0x276c
+  __TEXT.__swift5_typeref: 0x37c
+  __TEXT.__swift5_reflstr: 0xd49
+  __TEXT.__swift5_assocty: 0x78
+  __TEXT.__constg_swiftt: 0x9e4
+  __TEXT.__swift5_fieldmd: 0xa8c
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0x3c
-  __TEXT.__swift5_types: 0x58
-  __TEXT.__swift5_assocty: 0x60
-  __TEXT.__unwind_info: 0x4c8
-  __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_methname: 0x806
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0xc8
-  __DATA_CONST.__objc_classlist: 0x68
+  __TEXT.__swift5_proto: 0x54
+  __TEXT.__swift5_types: 0x80
+  __TEXT.__oslogstring: 0xf6e
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_capture: 0x50
+  __TEXT.__unwind_info: 0x660
+  __TEXT.__eh_frame: 0xf8
+  __TEXT.__objc_methname: 0x8b4
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x138
+  __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x230
-  __AUTH_CONST.__auth_got: 0x4e8
-  __AUTH_CONST.__auth_ptr: 0x148
-  __AUTH_CONST.__const: 0x670
-  __AUTH_CONST.__objc_const: 0x1660
+  __DATA_CONST.__objc_selrefs: 0x248
+  __AUTH_CONST.__auth_got: 0x5e0
+  __AUTH_CONST.__auth_ptr: 0x1b8
+  __AUTH_CONST.__const: 0xa08
+  __AUTH_CONST.__objc_const: 0x1e10
   __AUTH.__objc_data: 0x310
-  __AUTH.__data: 0x690
-  __DATA.__data: 0x418
-  __DATA.__bss: 0x780
+  __AUTH.__data: 0xdf8
+  __DATA.__data: 0x4b8
+  __DATA.__bss: 0xa00
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/VoiceTrigger.framework/VoiceTrigger
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 582
-  Symbols:   148
-  CStrings:  360
+  Functions: 853
+  Symbols:   156
+  CStrings:  437
 
Symbols:
+ _swift_deallocObject
+ _swift_dynamicCastClass
+ _swift_unknownObjectRetain_n
CStrings:
+ "               [%s] [%ld] [(%u)] : Waiting for logging near miss until timeout %llu samples"
+ "    [%s] [%ld] [(%u)] : Detected near miss candidate at %llulet's wait %llu samples to log"
+ "    [%s] [%ld] [(%u)] : Notify second pass rejected at: %llu with best score up to: %f threshold:%f"
+ "    [%s] [%ld] [(%u)] Detected near miss at %lluwith best score up to : %f"
+ "@136@0:8q16f24f28f32f36f40f44f48f52q56B64B68@72@80@88@96@104q112q120q128"
+ "CoreSpeechUtils/SecureKeywordAnalyzerQuasar.swift"
+ "CoreSpeechUtils/SecurePhraseDetector.swift"
+ "Tq,N,R,VaudioDurationProcessIntervalInMillis"
+ "Tq,N,R,VmaxAudioDurationInMillis"
+ "Tq,N,R,VminAudioDurationInMillis"
+ "[%s] [%ld] Combined token score count:%ld does not match phrase count %ld"
+ "[%s] [%ld] Discriminative config is not defined. This is a single phrase locale"
+ "[%s] [%ld] Failed to create NovDetector for Conformer"
+ "[%s] [%ld] No label scores are available. This is a error."
+ "[%s] [%ld] No token scores are available. What just happened?"
+ "[%s] [%ld] Not processing tokens. Returning the label scores as it is."
+ "[%s] [%ld] Quasar model reset??"
+ "[%s] [%ld] SecurePhraseDetector: phraseDetectorInfos count not valid!"
+ "[%s] [%ld] The discriminative head index collection is empty, break and continue with the existing results"
+ "[%s] [%ld] Token scores=%s"
+ "[%s] [%ld] Unable to create keyword analyzer ndapi since memoryindex or configData nil"
+ "[%s] [%ld] Unable to create keyword analyzer quasar since memoryindex or configData nil"
+ "[%s] [%ld] [(%u)] : Trigger detected with %llu analyzed samples in NDAPI, %f, effectiveThreshold = %f, bestStart = %llu"
+ "[%s] [%ld] discIndexList=%s"
+ "[%s] [%ld] label scores collection size=%ld does not match the token collection size=%ld"
+ "[%s] [%ld] ndapi checker results is not available"
+ "[%s] [%ld] tokenId: %ld, phoneticScore: %f, phoneticWeight: %f, discScore: %f, discScoreWeight: %f, finalScore: %f"
+ "[%s] [%ld] tokens=%s, discScores=%s, phoneScores=%s, labelScores=%s"
+ "_TtC15CoreSpeechUtils16SecureAudioChunk"
+ "_TtC15CoreSpeechUtils20SecurePhraseDetector"
+ "_TtC15CoreSpeechUtils26SecureKeywordAnalyzerNDAPI"
+ "_TtC15CoreSpeechUtils27SecureKeywordAnalyzerQuasar"
+ "activeChannel"
+ "activePhId"
+ "audioDurationProcessIntervalInMillis"
+ "bargeInFirstPass"
+ "bufferArrivalTime"
+ "defaultAudioDurationProcessIntervalInMillis"
+ "defaultMaxAudioDurationInMillis"
+ "defaultMinAudioDurationInMillis"
+ "defaultQuasarCheckerCutOffSamplesCount"
+ "discriminativeConfig"
+ "heartbeat"
+ "initWithNumPruningRetentionUtt:pruningExplicitSATThreshold:pruningExplicitPSRThreshold:pruningSATThreshold:pruningPSRThreshold:combinationWeight:implicitProfileThreshold:implicitProfileDeltaThreshold:implicitVTThreshold:maxEnrollmentUtterances:implicitTrainingEnabled:useTDTIEnrollment:phraseConfig:satMemoryIndex:psrMemoryIndex:satConfig:psrConfig:audioDurationProcessIntervalInMillis:minAudioDurationInMillis:maxAudioDurationInMillis:"
+ "isSecondChance"
+ "isStartSampleCountMarked"
+ "kAudioDurationProcessIntervalInMillis"
+ "kMaxAudioDurationInMillis"
+ "kMinAudioDurationInMillis"
+ "keywordAnalyzerNDAPI"
+ "keywordAnalyzerQuasar"
+ "lastSampleFed"
+ "maxAudioDurationInMillis"
+ "memoryLock"
+ "minAudioDurationInMillis"
+ "nearMissCandidateDetectedSamples"
+ "nearMissDelayTimeout"
+ "novDetect"
+ "novDetector"
+ "numChannel"
+ "numSamples"
+ "phraseDetectorInfos"
+ "phraseResults"
+ "preventDuplicatedReset"
+ "process_label_scores"
+ "processedSampleCount"
+ "quasarCheckerCutOffSamplesCount"
+ "quasarCheckerResultAtCutOff"
+ "sampleCount"
+ "sampleDepthInBytes"
+ "sampleFedWrapAroundOffset"
+ "samples"
+ "secondPassDetector"
+ "startAnalyzeSampleCount"
+ "triggerTokensArray"
+ "voiceTriggerSecondPassNearMissTimeout"
- "@112@0:8q16f24f28f32f36f40f44f48f52q56B64B68@72@80@88@96@104"
- "initWithNumPruningRetentionUtt:pruningExplicitSATThreshold:pruningExplicitPSRThreshold:pruningSATThreshold:pruningPSRThreshold:combinationWeight:implicitProfileThreshold:implicitProfileDeltaThreshold:implicitVTThreshold:maxEnrollmentUtterances:implicitTrainingEnabled:useTDTIEnrollment:phraseConfig:satMemoryIndex:psrMemoryIndex:satConfig:psrConfig:"

```
