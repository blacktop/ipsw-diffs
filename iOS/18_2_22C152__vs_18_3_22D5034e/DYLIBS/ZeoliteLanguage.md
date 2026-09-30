## ZeoliteLanguage

> `/System/Library/PrivateFrameworks/ZeoliteLanguage.framework/ZeoliteLanguage`

```diff

-1.2.3.0.0
-  __TEXT.__text: 0x100d8
-  __TEXT.__auth_stubs: 0xee0
-  __TEXT.__const: 0x862
-  __TEXT.__swift5_typeref: 0x389
-  __TEXT.__cstring: 0x4c2
-  __TEXT.__constg_swiftt: 0x128
-  __TEXT.__swift5_reflstr: 0x10e
-  __TEXT.__swift5_fieldmd: 0x120
-  __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_assocty: 0x138
-  __TEXT.__swift5_proto: 0x64
-  __TEXT.__swift5_types: 0x18
-  __TEXT.__oslogstring: 0x7c
-  __TEXT.__swift5_capture: 0x10
-  __TEXT.__unwind_info: 0x3b8
-  __TEXT.__eh_frame: 0x708
-  __TEXT.__objc_methname: 0x336
-  __DATA_CONST.__got: 0x240
-  __DATA_CONST.__const: 0xd8
+1.3.1.0.0
+  __TEXT.__text: 0x161dc
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__const: 0xbf0
+  __TEXT.__cstring: 0x772
+  __TEXT.__constg_swiftt: 0x214
+  __TEXT.__swift5_typeref: 0x52a
+  __TEXT.__swift5_builtin: 0x78
+  __TEXT.__swift5_reflstr: 0x1a1
+  __TEXT.__swift5_fieldmd: 0x210
+  __TEXT.__swift5_assocty: 0x198
+  __TEXT.__swift5_proto: 0xa0
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__oslogstring: 0x2fc
+  __TEXT.__swift5_capture: 0x24
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__eh_frame: 0xc50
+  __TEXT.__objc_methname: 0x4ab
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0xf8
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x118
-  __AUTH_CONST.__auth_got: 0x770
-  __AUTH_CONST.__auth_ptr: 0x2f8
-  __AUTH_CONST.__const: 0x1e0
+  __DATA_CONST.__objc_selrefs: 0x198
+  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH_CONST.__auth_ptr: 0x348
+  __AUTH_CONST.__const: 0x600
   __AUTH_CONST.__objc_const: 0xd8
   __AUTH.__data: 0x168
-  __DATA.__data: 0x320
-  __DATA.__bss: 0xc90
+  __DATA.__data: 0x480
+  __DATA.__bss: 0x1290
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/PrivateFrameworks/Email.framework/Email
   - /System/Library/PrivateFrameworks/EmailCore.framework/EmailCore
   - /System/Library/PrivateFrameworks/EmojiFoundation.framework/EmojiFoundation
   - /System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation
+  - /System/Library/PrivateFrameworks/MediaAnalysisServices.framework/MediaAnalysisServices
   - /System/Library/PrivateFrameworks/TokenGeneration.framework/TokenGeneration
   - /System/Library/PrivateFrameworks/TokenGenerationCore.framework/TokenGenerationCore
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation

   - /System/Library/PrivateFrameworks/ZeoliteFramework.framework/ZeoliteFramework
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 267
-  Symbols:   161
-  CStrings:  67
+  Functions: 414
+  Symbols:   188
+  CStrings:  113
 
Symbols:
+ _NLLanguageEnglish
+ _OBJC_CLASS_$_MADService
+ _OBJC_CLASS_$_MADTextEmbeddingRequest
+ _OBJC_CLASS_$_MADTextEmbeddingResult
+ _OBJC_CLASS_$_MADTextRequest
+ _OBJC_CLASS_$_NLContextualEmbedding
+ _OBJC_CLASS_$_NLEmbedding
+ _OBJC_CLASS_$_NLLanguageRecognizer
+ _OBJC_CLASS_$_NSNumber
+ __swift_FORCE_LOAD_$_swiftAVFoundation
+ __swift_FORCE_LOAD_$_swiftCoreAudio
+ __swift_FORCE_LOAD_$_swiftCoreMIDI
+ __swift_FORCE_LOAD_$_swiftCoreMedia
+ __swift_stdlib_bridgeErrorToNSError
+ _swift_errorRetain
+ _swift_getDynamicType
+ _swift_getMetatypeMetadata
CStrings:
+ "Embedding type not supported."
+ "Embedding type: %lu"
+ "Failed at calling MAD service: %@"
+ "Failed at creating NLContextualEmbedding."
+ "Failed at generating embeddings."
+ "Failed to generate embedding."
+ "Found embedding with nan values. Return zeros embedding."
+ "Found result: %s"
+ "Insufficient space allocated to copy string contents"
+ "MADTextEmbedder"
+ "NLContextualEmbedder"
+ "NLContextualEmbedder failed at requesting assets."
+ "NLContextualEmbedding doesn't have available assets."
+ "NLContextualEmbedding has no available assets. Requesting assets."
+ "NLContextualEmbedding.AssetsResult: %ld"
+ "NLEmbedder"
+ "Negative value is not representable"
+ "No results returned by MAD service."
+ "Swift/ContiguousArrayBuffer.swift"
+ "Swift/Integers.swift"
+ "Swift/StringTesting.swift"
+ "Swift/StringUTF8View.swift"
+ "Swift/UnsafeBufferPointer.swift"
+ "Swift/UnsafeRawPointer.swift"
+ "Unexpectedly found nil while unwrapping an Optional value"
+ "UnsafeMutableBufferPointer with negative count"
+ "UnsafeMutableRawPointer.initializeMemory overlapping range"
+ "contextualEmbeddingWithLanguage:"
+ "count"
+ "data"
+ "dominantLanguageForString:"
+ "embedding"
+ "embeddingResults"
+ "floatValue"
+ "hasAvailableAssets"
+ "invalid Collection: less than 'count' elements in collection"
+ "performRequests:text:identifier:completionHandler:"
+ "requestEmbeddingAssetsWithCompletionHandler:"
+ "requestSentenceEmbeddingVectorForString:language:completionHandler:"
+ "sentenceEmbeddingForLanguage:"
+ "service"
+ "setExtendedContextLength:"
+ "setVersion:"
+ "type"
+ "v20@?0i8@\"NSError\"12"
+ "v24@?0q8@\"NSError\"16"

```
