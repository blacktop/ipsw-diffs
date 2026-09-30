## SiriSuggestionsAPI

> `/System/Library/PrivateFrameworks/SiriSuggestionsAPI.framework/SiriSuggestionsAPI`

```diff

-3400.118.1.0.0
-  __TEXT.__text: 0xb6dd4
-  __TEXT.__auth_stubs: 0x2500
+3401.8.1.0.0
+  __TEXT.__text: 0xbaa00
+  __TEXT.__auth_stubs: 0x2540
   __TEXT.__objc_methlist: 0x44
   __TEXT.__const: 0x77ca
-  __TEXT.__cstring: 0x2b25
-  __TEXT.__swift5_typeref: 0x223e
-  __TEXT.__swift5_capture: 0x7f4
-  __TEXT.__oslogstring: 0x37d5
-  __TEXT.__swift5_reflstr: 0x1ac2
+  __TEXT.__cstring: 0x2bd5
+  __TEXT.__swift5_typeref: 0x22bc
+  __TEXT.__swift5_capture: 0x834
+  __TEXT.__oslogstring: 0x39e5
+  __TEXT.__swift5_reflstr: 0x1ad2
   __TEXT.__swift5_assocty: 0x180
-  __TEXT.__swift5_fieldmd: 0x25b4
-  __TEXT.__constg_swiftt: 0x22d0
+  __TEXT.__swift5_fieldmd: 0x25d8
+  __TEXT.__constg_swiftt: 0x22e8
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_protos: 0x94
   __TEXT.__swift5_proto: 0x6f8
   __TEXT.__swift5_types: 0x284
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3ef0
-  __TEXT.__eh_frame: 0x9430
-  __TEXT.__objc_methname: 0x8a3
-  __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x198
+  __TEXT.__unwind_info: 0x4028
+  __TEXT.__eh_frame: 0x98b0
+  __TEXT.__objc_methname: 0x9b9
+  __DATA_CONST.__got: 0xae8
+  __DATA_CONST.__const: 0x1d8
   __DATA_CONST.__objc_classlist: 0x170
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x340
+  __DATA_CONST.__objc_selrefs: 0x3a0
   __DATA_CONST.__objc_protorefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1280
-  __AUTH_CONST.__auth_ptr: 0x878
-  __AUTH_CONST.__const: 0x54d8
+  __AUTH_CONST.__auth_got: 0x12a0
+  __AUTH_CONST.__auth_ptr: 0x898
+  __AUTH_CONST.__const: 0x5568
   __AUTH_CONST.__objc_const: 0x25d8
-  __AUTH.__objc_data: 0x270
-  __AUTH.__data: 0xba8
-  __DATA.__data: 0x1f50
-  __DATA.__bss: 0x7d80
-  __DATA.__common: 0x58
-  __DATA_DIRTY.__objc_data: 0x168
-  __DATA_DIRTY.__data: 0x2510
-  __DATA_DIRTY.__bss: 0x3480
-  __DATA_DIRTY.__common: 0x8
+  __AUTH.__objc_data: 0x220
+  __AUTH.__data: 0xa40
+  __DATA.__data: 0x1ce8
+  __DATA.__bss: 0x7180
+  __DATA.__common: 0x40
+  __DATA_DIRTY.__objc_data: 0x1b8
+  __DATA_DIRTY.__data: 0x2998
+  __DATA_DIRTY.__bss: 0x4080
+  __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
   - /System/Library/PrivateFrameworks/CoreSpeech.framework/CoreSpeech

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5255
-  Symbols:   1581
-  CStrings:  642
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 5339
+  Symbols:   1624
+  CStrings:  665
 
Symbols:
+ _OBJC_CLASS_$_SUGSchemaSUGAutoCompleteQuery
+ _OBJC_CLASS_$_SUGSchemaSUGAutoCompleteSuggestionMetaData
+ _OBJC_CLASS_$_SUGSchemaSUGSuggestionTier1
+ _OBJC_CLASS_$_SUGSchemaSUGSuggestionsGeneratedTier1
+ _OBJC_CLASS_$_SUGSchemaSUGSuggestionsUIActivityTier1
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _swift_continuation_await
- _swift_continuation_init
CStrings:
+ "Default no-op implementation provided for submitEngagement(for inIntent:, with requestId:)"
+ "Failed to initialize SUGSchemaSUGSuggestionsGenerated/SUGSchemaSUGSuggestionsGeneratedTier1/SUGSchemaSUGAutoCompleteQuery object"
+ "Failed to initialize SUGSchemaSUGSuggestionsUIActivity/SUGSchemaSUGSuggestionsUIActivityTier1 object"
+ "Logging INIntent %!s(MISSING) for %!s(MISSING)"
+ "Must take zero or more splits"
+ "Range requires lowerBound <= upperBound"
+ "Smart Suppression Score not found, returning nil"
+ "SmartSuppressionPolicy"
+ "Swift/Collection.swift"
+ "Swift/Range.swift"
+ "error generating the SUGSchemaSUGSuggestion/SUGSchemaSUGSuggestionTier1"
+ "setAutoCompleteQuery:"
+ "setAutoCompleteSuggestionMetaData:"
+ "setAutoCompleteSuggestionSource:"
+ "setLinkId:"
+ "setNumCharactersInQuery:"
+ "setNumCharactersInSuggestion:"
+ "setNumWordsInQuery:"
+ "setNumWordsInSuggestion:"
+ "setSmartSuppressionScore:"
+ "setSugGeneratedTier1:"
+ "setUiActivityTier1:"
+ "typeName"

```
