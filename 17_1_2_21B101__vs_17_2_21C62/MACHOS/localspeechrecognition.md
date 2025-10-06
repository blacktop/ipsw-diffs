## localspeechrecognition

> `/System/Library/Frameworks/Speech.framework/XPCServices/localspeechrecognition.xpc/localspeechrecognition`

```diff

-3301.14.1.1.1
-  __TEXT.__text: 0x2995c
+3302.15.1.0.0
+  __TEXT.__text: 0x2b7c4
   __TEXT.__auth_stubs: 0x13b0
   __TEXT.__objc_stubs: 0x2a40
-  __TEXT.__objc_methlist: 0x8bc
-  __TEXT.__const: 0x888
-  __TEXT.__objc_methname: 0x42b2
-  __TEXT.__cstring: 0x27b9
-  __TEXT.__constg_swiftt: 0xa0c
-  __TEXT.__swift5_typeref: 0x719
-  __TEXT.__swift5_reflstr: 0x4f2
-  __TEXT.__swift5_fieldmd: 0x380
+  __TEXT.__objc_methlist: 0x914
+  __TEXT.__const: 0x898
+  __TEXT.__objc_methname: 0x43f0
+  __TEXT.__cstring: 0x2a09
+  __TEXT.__constg_swiftt: 0xa78
+  __TEXT.__swift5_typeref: 0x6f9
+  __TEXT.__swift5_reflstr: 0x582
+  __TEXT.__swift5_fieldmd: 0x3e4
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_proto: 0x48
-  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift5_types: 0x48
   __TEXT.__objc_classname: 0x170
-  __TEXT.__objc_methtype: 0x111b
-  __TEXT.__swift5_capture: 0xc0
+  __TEXT.__objc_methtype: 0x11eb
+  __TEXT.__swift5_capture: 0xf8
   __TEXT.__gcc_except_tab: 0x39c
   __TEXT.__oslogstring: 0x136a
-  __TEXT.__unwind_info: 0x8c0
-  __TEXT.__eh_frame: 0x4f0
+  __TEXT.__unwind_info: 0x94c
+  __TEXT.__eh_frame: 0x658
   __DATA_CONST.__auth_got: 0x9e8
   __DATA_CONST.__got: 0x2d8
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0xdf0
+  __DATA_CONST.__const: 0xe68
   __DATA_CONST.__cfstring: 0x760
-  __DATA_CONST.__objc_classlist: 0x90
-  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_classlist: 0x98
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2420
-  __DATA.__objc_selrefs: 0x10e0
+  __DATA.__objc_const: 0x2580
+  __DATA.__objc_selrefs: 0x1140
   __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x390
+  __DATA.__objc_classrefs: 0x388
   __DATA.__objc_superrefs: 0x18
   __DATA.__objc_ivar: 0x84
-  __DATA.__objc_data: 0x790
-  __DATA.__data: 0x1320
+  __DATA.__objc_data: 0x8b0
+  __DATA.__data: 0x13a0
   __DATA.__common: 0xa0
   __DATA.__bss: 0x978
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/EmbeddedAcousticRecognition.framework/EmbeddedAcousticRecognition
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 752CC604-38BE-3BCE-BCEE-CE096E100132
-  Functions: 763
-  Symbols:   395
-  CStrings:  1224
+  UUID: D3E605A1-E891-3B5E-9179-E33ED720FA7B
+  Functions: 816
+  Symbols:   394
+  CStrings:  1257
 
Symbols:
- _OBJC_CLASS_$__EARSpeechRecognitionAudioBuffer
CStrings:
+ "EARSpeechRecognitionAudioBuffer.%s"
+ "EARSpeechRecognitionAudioBuffer.%s replying %llu"
+ "Vv28@0:8f16@?20"
+ "Vv28@0:8f16@?<v@?Q>20"
+ "Vv48@0:8@\"NSUUID\"16@\"_SFSpeechRecognizerSupportedFeatures\"24@\"_SFAnalysisContextCodingObject\"32@\"_SFAnalysisOptions\"40"
+ "Vv48@0:8@16@24@32@40"
+ "_TtC22localspeechrecognition31EARSpeechRecognitionAudioBuffer"
+ "addAudioSampleData(_:)"
+ "assets"
+ "audioBuffer"
+ "cancelRecognition()"
+ "clientInfo"
+ "detectAfterTime"
+ "detectionOptions"
+ "dictationUIInteractionId"
+ "geoLanguageModelLoaded"
+ "hammerModelVersion"
+ "inputOrigin"
+ "localspeechrecognition.EARSpeechRecognitionAudioBuffer"
+ "packetArrivalTimestamp(fromAudioTimestamp:)"
+ "packetArrivalTimestampFromAudioTime:"
+ "packetArrivalTimestampFromAudioTimestamp:reply:"
+ "prepareForReuseWithNewAsrID:supportedFeatures:analysisContext:analysisOptions:"
+ "setEndpointStart:"
+ "setInputOrigin:"
+ "speechRecognizerDidRecognizePartialResult:"
+ "speechRecognizerDidReportStatus:"
+ "supportedFeatures"
+ "v24@0:8@\"EARSpeechRecognitionResult\"16"
+ "v24@0:8Q16"
+ "v28@0:8f16@?<v@?Q>20"
- "speechRecognizerDidRecognizePartialResultNbest:"
- "v24@0:8@\"NSArray\"16"

```
