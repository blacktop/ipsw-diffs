## GenerativeFunctionsInstrumentation

> `/System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation`

```diff

-138.105.0.0.0
-  __TEXT.__text: 0x614b0
+145.505.100.0.0
+  __TEXT.__text: 0x61af4
   __TEXT.__auth_stubs: 0x2580
   __TEXT.__objc_methlist: 0x64
-  __TEXT.__const: 0x2408
-  __TEXT.__cstring: 0x3518
-  __TEXT.__swift5_typeref: 0xf32
-  __TEXT.__oslogstring: 0x1fc8
-  __TEXT.__constg_swiftt: 0xf30
-  __TEXT.__swift5_reflstr: 0x1422
-  __TEXT.__swift5_fieldmd: 0xf6c
+  __TEXT.__const: 0x2418
+  __TEXT.__cstring: 0x3558
+  __TEXT.__swift5_typeref: 0xf74
+  __TEXT.__oslogstring: 0x22c8
+  __TEXT.__constg_swiftt: 0xf40
+  __TEXT.__swift5_reflstr: 0x1452
+  __TEXT.__swift5_fieldmd: 0xf78
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x1b8
   __TEXT.__swift5_types: 0xd4
   __TEXT.__swift5_capture: 0x100
   __TEXT.__swift5_protos: 0x20
   __TEXT.__swift5_assocty: 0x1a8
-  __TEXT.__unwind_info: 0x1570
-  __TEXT.__eh_frame: 0x25e8
+  __TEXT.__unwind_info: 0x15b8
+  __TEXT.__eh_frame: 0x2608
   __TEXT.__objc_classname: 0x1f
   __TEXT.__objc_methname: 0x30a
   __TEXT.__objc_methtype: 0x2e
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0x868
-  __DATA_CONST.__const: 0x78
+  __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x110
   __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__auth_got: 0x12c8
-  __AUTH_CONST.__auth_ptr: 0x618
+  __AUTH_CONST.__auth_ptr: 0x628
   __AUTH_CONST.__const: 0xe90
-  __AUTH_CONST.__objc_const: 0x1c98
-  __AUTH.__objc_data: 0x1e0
-  __AUTH.__data: 0x1920
+  __AUTH_CONST.__objc_const: 0x1cb8
   __DATA.__objc_ivar: 0x10
-  __DATA.__data: 0xdb8
-  __DATA.__bss: 0x2f10
+  __DATA.__data: 0xb30
+  __DATA.__bss: 0x2c10
   __DATA.__common: 0x388
-  __DATA_DIRTY.__data: 0xd8
+  __DATA_DIRTY.__objc_data: 0x1e0
+  __DATA_DIRTY.__data: 0x1c90
+  __DATA_DIRTY.__bss: 0x300
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2158
-  Symbols:   157
-  CStrings:  517
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 2191
+  Symbols:   165
+  CStrings:  528
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "CompletePromptRequestInstrumenter initialized with mismatched EventReporter and userIdentifier"
+ "EventReporter creating stream source"
+ "EventReporter creating system stream source"
+ "EventReporter failedToCreateStreamSource"
+ "EventReporter initialized with user '%!s(MISSING)'"
+ "EventReporter lazily created source"
+ "EventReporter lazily created system source"
+ "EventReporter warmed up"
+ "ExtendInferenceInstrumenter initialized with mismatched EventReporter and userIdentifier"
+ "FirstTokenInferenceInstrumenter initialized with mismatched EventReporter and userIdentifier"
+ "PromptProcessingInstrumenter initialized with mismatched EventReporter and userIdentifier"
+ "outputTokensCount=%!{(MISSING)public, signpost.description=attribute,public}ld requestIdentifier=%!{(MISSING)public, signpost.description=attribute,public}s requestType=%!{(MISSING)public, signpost.description=attribute,public}s error=%!{(MISSING)public, signpost.description=attribute,public}ld tinyModelInferenceCallCount=%!{(MISSING)public, signpost.description=attribute,public}ld draftModelInferenceCallCount=%!{(MISSING)public, signpost.description=attribute,public}ld targetModelInferenceCallCount=%!{(MISSING)public, signpost.description=attribute,public}ld draftSteps=%!{(MISSING)public, signpost.description=attribute,public}ld draftTokenAcceptanceRateInPercent=%!{(MISSING)public, signpost.description=attribute,public}f tinyTokenAcceptanceRateInPercent=%!{(MISSING)public, signpost.description=attribute,public}f speculationSuccessRateInPercent=%!{(MISSING)public, signpost.description=attribute,public}f numberOfDraftOutputTokens=%!{(MISSING)public, signpost.description=attribute,public}ld totalNumberOutputTokens=%!{(MISSING)public, signpost.description=attribute,public}ld tinyModelTotalLatency=%!{(MISSING)public, signpost.description=attribute,public}f draftModelTotalLatency=%!{(MISSING)public, signpost.description=attribute,public}f targetModelTotalLatency=%!{(MISSING)public, signpost.description=attribute,public}f prefixKVCacheTokensMatchCount=%!{(MISSING)public, signpost.description=attribute,public}s promptModulesKVCacheTokensMatchCount=%!{(MISSING)public, signpost.description=attribute,public}s draftEmptyResponse=%!{(MISSING)public, signpost.description=attribute,public}s draftEarlyReturn=%!{(MISSING)public, signpost.description=attribute,public}s"
+ "routeAllEventsToSystemStream"
+ "sourceLock"
+ "systemSourceLock"
- "EventReporter initialized with source '%!s(MISSING)' and user '%!s(MISSING)'"
- "outputTokensCount=%!{(MISSING)public, signpost.description=attribute,public}ld requestIdentifier=%!{(MISSING)public, signpost.description=attribute,public}s requestType=%!{(MISSING)public, signpost.description=attribute,public}s error=%!{(MISSING)public, signpost.description=attribute,public}ld tinyModelInferenceCallCount=%!{(MISSING)public, signpost.description=attribute,public}ld draftModelInferenceCallCount=%!{(MISSING)public, signpost.description=attribute,public}ld targetModelInferenceCallCount=%!{(MISSING)public, signpost.description=attribute,public}ld draftSteps=%!{(MISSING)public, signpost.description=attribute,public}ld draftTokenAcceptanceRateInPercent=%!{(MISSING)public, signpost.description=attribute,public}f tinyTokenAcceptanceRateInPercent=%!{(MISSING)public, signpost.description=attribute,public}f speculationSuccessRateInPercent=%!{(MISSING)public, signpost.description=attribute,public}f numberOfDraftOutputTokens=%!{(MISSING)public, signpost.description=attribute,public}ld totalNumberOutputTokens=%!{(MISSING)public, signpost.description=attribute,public}ld tinyModelTotalLatency=%!{(MISSING)public, signpost.description=attribute,public}f draftModelTotalLatency=%!{(MISSING)public, signpost.description=attribute,public}f targetModelTotalLatency=%!{(MISSING)public, signpost.description=attribute,public}f prefixKVCacheTokensMatchCount=%!{(MISSING)public, signpost.description=attribute,public}s promptModulesKVCacheTokensMatchCount=%!{(MISSING)public, signpost.description=attribute,public}s"
- "source"
- "systemSource"

```
