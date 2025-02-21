## ZeoliteExtension

> `/System/Library/ExtensionKit/Extensions/ZeoliteExtension.appex/ZeoliteExtension`

```diff

-1.3.1.0.0
-  __TEXT.__text: 0x335ac
-  __TEXT.__auth_stubs: 0x1240
-  __TEXT.__cstring: 0x791
-  __TEXT.__swift5_typeref: 0x70e
-  __TEXT.__oslogstring: 0xcfb
-  __TEXT.__swift5_capture: 0x410
-  __TEXT.__const: 0x1e20
-  __TEXT.__swift5_reflstr: 0x4e2
+1.4.5.0.0
+  __TEXT.__text: 0x3ece0
+  __TEXT.__auth_stubs: 0x1420
+  __TEXT.__const: 0x2100
+  __TEXT.__cstring: 0x6a4
+  __TEXT.__swift5_typeref: 0x8c8
+  __TEXT.__oslogstring: 0x10c5
+  __TEXT.__swift5_capture: 0x318
+  __TEXT.__objc_methname: 0x2be
+  __TEXT.__swift_as_entry: 0x40
+  __TEXT.__swift_as_ret: 0x68
+  __TEXT.__swift5_reflstr: 0x6a0
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x428
-  __TEXT.__swift5_fieldmd: 0x878
-  __TEXT.__objc_methname: 0x1ce
-  __TEXT.__swift5_proto: 0x1d8
-  __TEXT.__swift5_types: 0x7c
+  __TEXT.__constg_swiftt: 0x51c
+  __TEXT.__swift5_fieldmd: 0xaf8
+  __TEXT.__swift5_proto: 0x230
+  __TEXT.__swift5_types: 0x98
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xae0
-  __TEXT.__eh_frame: 0x11c0
-  __DATA_CONST.__auth_got: 0x920
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__auth_ptr: 0x2d0
-  __DATA_CONST.__const: 0x1f60
+  __TEXT.__unwind_info: 0xbd0
+  __TEXT.__eh_frame: 0x17d0
+  __DATA_CONST.__auth_got: 0xa10
+  __DATA_CONST.__got: 0x2c8
+  __DATA_CONST.__auth_ptr: 0x2d8
+  __DATA_CONST.__const: 0x2160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0xd8
-  __DATA.__data: 0xa00
+  __DATA.__objc_selrefs: 0x160
+  __DATA.__data: 0xcd0
   __DATA.__common: 0x18
-  __DATA.__bss: 0x3a00
+  __DATA.__bss: 0x4480
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 903
-  Symbols:   125
-  CStrings:  178
+  Functions: 935
+  Symbols:   139
+  CStrings:  217
 
Symbols:
+ _NSKeyedArchiveRootObjectKey
+ _OBJC_CLASS_$_INInteraction
+ _OBJC_CLASS_$_INSendMessageIntent
+ _OBJC_CLASS_$_NSKeyedUnarchiver
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftIntents
+ _log
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x27
+ _swift_allocError
+ _swift_dynamicCastObjCClass
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_getErrorValue
+ _swift_initStructMetadataWithLayoutString
- _objc_retain_x26
- _swift_deletedAsyncMethodErrorTu
- _swift_initStructMetadata
- _swift_projectBox
- _swift_task_isCurrentExecutor
- _swift_task_reportUnexpectedExecutor
CStrings:
+ "App"
+ "B16@?0@8"
+ "Completed tokenization step: %s"
+ "Data reading completed. Found %ld messages."
+ "Dictionary service unavailable"
+ "Failed to complete tokenization step."
+ "Failed to create tokenizer with path: %s."
+ "Failed to encode embeddings to JSON: %s"
+ "Failed to generate embeddings."
+ "Failed to load vocabulary scores file: %@"
+ "Failed to perform inference!"
+ "Failed to query events."
+ "Failed to save embeddings to kvStore: %@"
+ "Failed to unarchive AppIntent, error %s"
+ "Failed to write embeddings events."
+ "Got empty embedding data from KVStore with key %s, exiting early."
+ "Got error reading from KVStore: %@"
+ "INSendMessageIntent"
+ "Input text: %s \n Generated text: %s"
+ "Intent"
+ "Interaction intent read from biome is not of INSendMessageIntent type, message will be discarded."
+ "Invalid kvStoreKey provided"
+ "Loaded %ld vocabulary scores, using top %ld scores as rare tokens."
+ "Message content was nil, discarding message"
+ "MessageIntent read from biome has incorrect contents, message will be discarded."
+ "Missing sms extract parameters."
+ "Queried %ld events."
+ "Query for all available embeddings."
+ "Running tokenization step."
+ "Sent %ld events."
+ "Tokenization completed in %s"
+ "Tokenizer model path is nil."
+ "absoluteTimestamp"
+ "bundleID"
+ "com.apple.MobileSMS"
+ "com.apple.zeolite.ZeoliteExtension"
+ "contactIdentifier"
+ "content"
+ "customIdentifier"
+ "dictionaryService available: %{bool}d"
+ "displayName"
+ "failedToEncode"
+ "failedToReadFromKVStore"
+ "failedToTokenize"
+ "failedToWriteToKVStore"
+ "filterSourceType"
+ "filterWithIsIncluded:"
+ "groupIdentifier"
+ "initForReadingFromData:error:"
+ "intent"
+ "intentClass"
+ "interaction"
+ "interactionDirection"
+ "invalidAppIntent"
+ "invalidScoreInputIOStrategy"
+ "kvStore"
+ "kvStoreUnavailable"
+ "maxTokenFrequency"
+ "minTokenFrequency"
+ "outgoingMessageType"
+ "rareScoresPercentile"
+ "sender"
+ "sms"
+ "tokenCompressionRatio"
+ "tokenization"
+ "tokenizationParameters"
+ "tokenizerModelPath"
+ "vocabularyScoresPath"
- "Data reading completed. %s"
- "Division by zero"
- "Division results in an overflow"
- "Failed to create embedder from embedParameters."
- "Failed to query from Biome"
- "Failed to send events to Biome"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Negative value is not representable"
- "Queried %ld events from Biome."
- "Sent %ld events to Biome."
- "Source type: %s"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/Integers.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unable to extract state for config %ld. Query for all available embeddings with model %s."
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "failed token generation!"
- "input text:%s \n generated text: %s"
- "invalid Collection: less than 'count' elements in collection"

```
