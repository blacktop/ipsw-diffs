## ZeoliteFramework

> `/System/Library/PrivateFrameworks/ZeoliteFramework.framework/ZeoliteFramework`

```diff

-1.2.3.0.0
-  __TEXT.__text: 0x48560
-  __TEXT.__auth_stubs: 0x1530
-  __TEXT.__const: 0x30a2
-  __TEXT.__cstring: 0x713
-  __TEXT.__constg_swiftt: 0x11c8
-  __TEXT.__swift5_typeref: 0xdae
-  __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x618
-  __TEXT.__swift5_fieldmd: 0xd34
-  __TEXT.__swift5_assocty: 0x448
-  __TEXT.__swift5_proto: 0x324
-  __TEXT.__swift5_types: 0xec
-  __TEXT.__swift5_protos: 0x28
-  __TEXT.__oslogstring: 0x547
-  __TEXT.__swift5_capture: 0x8c
-  __TEXT.__unwind_info: 0x1518
-  __TEXT.__eh_frame: 0x2a10
-  __TEXT.__objc_methname: 0x1b2
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0x240
+1.3.1.0.0
+  __TEXT.__text: 0x42f78
+  __TEXT.__auth_stubs: 0x1320
+  __TEXT.__const: 0x2cf2
+  __TEXT.__cstring: 0x643
+  __TEXT.__swift5_typeref: 0xc16
+  __TEXT.__swift5_fieldmd: 0xc44
+  __TEXT.__constg_swiftt: 0x10d0
+  __TEXT.__swift5_protos: 0x24
+  __TEXT.__oslogstring: 0x2c7
+  __TEXT.__swift5_reflstr: 0x548
+  __TEXT.__swift5_assocty: 0x3e8
+  __TEXT.__swift5_proto: 0x2e8
+  __TEXT.__swift5_types: 0xd4
+  __TEXT.__swift5_capture: 0x78
+  __TEXT.__unwind_info: 0x12f0
+  __TEXT.__eh_frame: 0x24f8
+  __TEXT.__objc_methname: 0x38
+  __DATA_CONST.__got: 0x268
+  __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x98
-  __AUTH_CONST.__auth_got: 0xa98
-  __AUTH_CONST.__auth_ptr: 0x3c8
-  __AUTH_CONST.__const: 0x2540
+  __DATA_CONST.__objc_selrefs: 0x10
+  __AUTH_CONST.__auth_got: 0x990
+  __AUTH_CONST.__auth_ptr: 0x358
+  __AUTH_CONST.__const: 0x2120
   __AUTH_CONST.__objc_const: 0x6a0
   __AUTH.__data: 0x638
-  __DATA.__data: 0xfd0
-  __DATA.__bss: 0x5f80
+  __DATA.__data: 0xe88
+  __DATA.__bss: 0x5980
   __DATA.__common: 0x20
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/Planks.framework/Planks
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1648
-  Symbols:   210
-  CStrings:  111
+  Functions: 1512
+  Symbols:   169
+  CStrings:  74
 
Symbols:
- _NLLanguageEnglish
- _OBJC_CLASS_$_MADService
- _OBJC_CLASS_$_MADTextEmbeddingRequest
- _OBJC_CLASS_$_MADTextEmbeddingResult
- _OBJC_CLASS_$_MADTextRequest
- _OBJC_CLASS_$_NLContextualEmbedding
- _OBJC_CLASS_$_NLEmbedding
- _OBJC_CLASS_$_NLLanguageRecognizer
- _OBJC_CLASS_$_NSNumber
- __Block_copy
- __Block_release
- __NSConcreteStackBlock
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreImage
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftNaturalLanguage
- __swift_FORCE_LOAD_$_swiftQuartzCore
- __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
- _objc_allocWithZone
- _objc_release
- _objc_retain
- _objc_retain_x19
- _objc_retain_x21
- _objc_retain_x22
- _objc_retain_x26
- _swift_allocBox
- _swift_continuation_await
- _swift_continuation_init
- _swift_getDynamicType
- _swift_getForeignTypeMetadata
- _swift_getMetatypeMetadata
CStrings:
- "Embedding type not supported."
- "Embedding type: %lu"
- "Failed at calling MAD service: %@"
- "Failed at creating NLContextualEmbedding."
- "Failed at generating embeddings."
- "Failed to generate embedding."
- "Found embedding with nan values. Return zeros embedding."
- "Found result: %s"
- "MADTextEmbedder"
- "NLContextualEmbedder"
- "NLContextualEmbedder failed at requesting assets."
- "NLContextualEmbedding doesn't have available assets."
- "NLContextualEmbedding has no available assets. Requesting assets."
- "NLContextualEmbedding.AssetsResult: %ld"
- "NLEmbedder"
- "No results returned by MAD service."
- "_createCheckedThrowingContinuation(_:)"
- "contextualEmbeddingWithLanguage:"
- "count"
- "data"
- "dominantLanguageForString:"
- "embedding"
- "embeddingResults"
- "floatValue"
- "hasAvailableAssets"
- "init"
- "performRequests:text:identifier:completionHandler:"
- "requestEmbeddingAssetsWithCompletionHandler:"
- "requestSentenceEmbeddingVectorForString:language:completionHandler:"
- "sentenceEmbeddingForLanguage:"
- "service"
- "setExtendedContextLength:"
- "setVersion:"
- "type"
- "v20@?0i8@\"NSError\"12"
- "v24@?0@\"NSArray\"8@\"NSError\"16"
- "v24@?0q8@\"NSError\"16"

```
