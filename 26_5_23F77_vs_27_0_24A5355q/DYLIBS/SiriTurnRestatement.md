## SiriTurnRestatement

> `/System/Library/PrivateFrameworks/SiriTurnRestatement.framework/SiriTurnRestatement`

```diff

-3525.4.4.0.0
-  __TEXT.__text: 0xdb10
-  __TEXT.__auth_stubs: 0xb50
+3600.43.6.1.1
+  __TEXT.__text: 0xd85c
   __TEXT.__const: 0xb40
   __TEXT.__constg_swiftt: 0x3e8
-  __TEXT.__swift5_typeref: 0x31d
+  __TEXT.__swift5_typeref: 0x30d
   __TEXT.__swift5_reflstr: 0x40b
   __TEXT.__swift5_fieldmd: 0x318
   __TEXT.__cstring: 0x7f1

   __TEXT.__swift5_assocty: 0x98
   __TEXT.__swift_as_entry: 0x34
   __TEXT.__swift_as_ret: 0x34
+  __TEXT.__swift_as_cont: 0x5c
   __TEXT.__unwind_info: 0x3c8
   __TEXT.__eh_frame: 0x6f8
-  __TEXT.__objc_classname: 0x24d
-  __TEXT.__objc_methname: 0x3a3
-  __TEXT.__objc_methtype: 0x42
-  __TEXT.__objc_stubs: 0x2a0
-  __DATA_CONST.__got: 0x108
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc50
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH_CONST.__const: 0x4b8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x550
   __AUTH_CONST.__cfstring: 0x1740
   __AUTH_CONST.__objc_const: 0x748
-  __AUTH.__objc_data: 0x190
-  __AUTH.__data: 0x6d8
-  __DATA.__data: 0x240
+  __AUTH_CONST.__auth_got: 0x648
+  __AUTH.__objc_data: 0x140
+  __AUTH.__data: 0x618
+  __DATA.__data: 0x220
   __DATA.__bss: 0x980
-  __DATA_DIRTY.__data: 0xb8
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__data: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 906414F0-5667-3F6F-9448-E008637FEEA8
-  Functions: 277
-  Symbols:   330
-  CStrings:  463
+  UUID: E4DEEB92-52E4-3B2B-BF94-6FCDC4D6E4AA
+  Functions: 276
+  Symbols:   353
+  CStrings:  412
 
Symbols:
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftCompression_$_SiriTurnRestatement
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
+ _swift_unknownObjectRelease
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_SiriTurnRestatement
- _objc_release_x27
- _swift_retain
- _swift_unknownObjectRelease_n
- _symbolic _____y_____GSg 17_StringProcessing5RegexV AA03AnyC6OutputV
CStrings:
- "@\"NSDictionary\"8@?0"
- "_TtC19SiriTurnRestatement17TurnTextExtractor"
- "_TtC19SiriTurnRestatement17TurnTextSanitizer"
- "_TtC19SiriTurnRestatement17TurnTextValidator"
- "_TtC19SiriTurnRestatement22SanitizedTextExtractor"
- "_TtC19SiriTurnRestatement22TurnLanguageCodeReader"
- "_TtC19SiriTurnRestatement25SiriTurnRestatementPlugin"
- "_TtC19SiriTurnRestatement29SiriTurnRestatementCalculator"
- "_TtC19SiriTurnRestatement30CalculatorErrorMetricSubmitter"
- "_TtC19SiriTurnRestatement31SiriTurnRestatementDataProvider"
- "_TtC19SiriTurnRestatement31SiriTurnRestatementSELFReporter"
- "addTurnRestatementScores:"
- "anyEventType"
- "bookmarkService"
- "calculator"
- "calendar"
- "dataProvider"
- "dimFeatureExtractor"
- "errorMetricSubmitter"
- "feedbackLogger"
- "init"
- "initWithNSUUID:"
- "initWithSuiteName:"
- "languageCode"
- "logger"
- "maxConsecutiveTurns"
- "maxSeconds"
- "reportSiriInstrumentationEvent:forBundleID:completion:"
- "reporter"
- "sanitizedTextExtractor"
- "setAggregationInterval:"
- "setCurrentTurnId:"
- "setEventMetadata:"
- "setEventTimestampInMsSince1970:"
- "setNextTurnId:"
- "setNumberOfSeconds:"
- "setOdbatchId:"
- "setSemanticSimilarityScore:"
- "setStartTimestampInSecondsSince1970:"
- "setTurnRestatementScoresReported:"
- "setUtteranceRestatementScore:"
- "sharedLoggerWithPersistenceConfiguration:"
- "similarityScorer"
- "turnLanguageCodeReader"
- "turnRestatementScoresReported"
- "turnTextExtractor"
- "turnTextSanitizer"
- "turnTextValidator"
- "ueiFeatureExtractor"
- "v16@?0@\"NSError\"8"
- "wrapAsAnyEvent"

```
