## LLMCache

> `/System/Library/PrivateFrameworks/LLMCache.framework/LLMCache`

```diff

-3401.1.1.0.0
-  __TEXT.__text: 0x2d618
-  __TEXT.__auth_stubs: 0x1190
-  __TEXT.__const: 0xd28
-  __TEXT.__cstring: 0x8db
+3404.3.1.0.0
+  __TEXT.__text: 0x297f8
+  __TEXT.__auth_stubs: 0x1120
+  __TEXT.__const: 0xd48
+  __TEXT.__cstring: 0x4eb
   __TEXT.__constg_swiftt: 0x604
   __TEXT.__swift5_typeref: 0x338
   __TEXT.__swift5_reflstr: 0x2c3

   __TEXT.__swift5_proto: 0x98
   __TEXT.__oslogstring: 0x12d9
   __TEXT.__swift5_capture: 0x28
+  __TEXT.__swift_as_entry: 0x7c
+  __TEXT.__swift_as_ret: 0x74
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0xa38
-  __TEXT.__eh_frame: 0x1a28
+  __TEXT.__unwind_info: 0x9a8
+  __TEXT.__eh_frame: 0x1a90
   __TEXT.__objc_methname: 0x167
-  __DATA_CONST.__got: 0x298
-  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0x198
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x90
-  __AUTH_CONST.__auth_got: 0x8c8
+  __AUTH_CONST.__auth_got: 0x890
   __AUTH_CONST.__auth_ptr: 0x240
   __AUTH_CONST.__const: 0x978
   __AUTH_CONST.__objc_const: 0x458
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x6b0
-  __DATA.__data: 0x478
+  __AUTH.__data: 0x5a0
+  __DATA.__data: 0x460
   __DATA.__common: 0x88
-  __DATA.__bss: 0x1180
+  __DATA.__bss: 0x1100
+  __DATA_DIRTY.__data: 0x138
+  __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 726
-  Symbols:   1502
-  CStrings:  173
+  Functions: 673
+  Symbols:   1498
+  CStrings:  151
 
Symbols:
+ _$s8LLMCache0A19ManagerFeatureFlagsO12forceEnabledSbSgvpZMV
+ _$s8LLMCache0A7ManagerC15defaultPageSizeSivpZMV
+ _$s8LLMCache0A7ManagerC19defaultTTLInSecondsSdvpZMV
+ _$s8LLMCache19AnnotatedCacheEntryV13dateFormatterSo013NSISO8601DateF0CvpZMV
+ _$s8LLMCache20VectorDatabaseAccessC11jsonDecoder10Foundation11JSONDecoderCvpZMV
+ _$s8LLMCache20VectorDatabaseAccessC13dimensionFileSSvpZMV
+ _$s8LLMCache20VectorDatabaseAccessC16maxSearchResultsSivpZMV
+ _$s8LLMCache20VectorDatabaseAccessC20defaultClientVersionSSvpZMV
+ _$s8LLMCache26UniversalEmbeddingProviderV16defaultDimensionSivpZMV
+ _$s8LLMCache6LoggerO15instrumentation2osABVvpZMV
+ _$s8LLMCache6LoggerO3logSo06OS_os_C0CvpZMV
+ _$s8LLMCache6LoggerO6logger2osABVvpZMV
+ _$s8LLMCache9DBColumnsO13ttlColumnNameSSvpZMV
+ _$s8LLMCache9DBColumnsO16userIdColumnNameSSvpZMV
+ _$s8LLMCache9DBColumnsO19namespaceColumnNameSSvpZMV
+ _$s8LLMCache9DBColumnsO22rawSearchKeyColumnNameSSvpZMV
+ _$s8LLMCache9DBColumnsO26lastAccessedTimeColumnNameSSvpZMV
+ _$sSaMa
+ _$sSdN
+ __swift_FORCE_LOAD_$_swiftIntents
+ _objc_retain_x21
+ _objc_retain_x25
+ _objc_retain_x27
+ _swift_generic_assignWithCopy
+ _swift_generic_assignWithTake
+ _swift_generic_destroy
+ _swift_generic_initWithCopy
+ _swift_generic_initWithTake
+ _swift_generic_initializeBufferWithCopyOfBuffer
+ _swift_initStructMetadataWithLayoutString
- _$s27IntelligencePlatformLibrary18CacheManagerInsertO6FailedVMa
- _$s27IntelligencePlatformLibrary18CacheManagerSearchO6FailedVMa
- _$sBi64_WV
- _$sSa12_endMutationyyFyXl_Ts5
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _objc_release_x28
- _swift_initStructMetadata
CStrings:
- "Can't construct Array with count < 0"
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/Array.swift"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawBufferPointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutablePointer.moveInitialize with negative count"
- "UnsafeMutableRawBufferPointer.copyMemory source has too many elements"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
