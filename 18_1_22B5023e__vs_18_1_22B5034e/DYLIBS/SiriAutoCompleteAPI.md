## SiriAutoCompleteAPI

> `/System/Library/PrivateFrameworks/SiriAutoCompleteAPI.framework/SiriAutoCompleteAPI`

```diff

-3401.8.1.0.0
-  __TEXT.__text: 0x1b22c
-  __TEXT.__auth_stubs: 0xe40
-  __TEXT.__const: 0xc9c
-  __TEXT.__cstring: 0xdbc
-  __TEXT.__swift5_typeref: 0x44c
-  __TEXT.__swift5_reflstr: 0x358
+3401.14.1.0.0
+  __TEXT.__text: 0x22720
+  __TEXT.__auth_stubs: 0xfb0
+  __TEXT.__const: 0xd9c
+  __TEXT.__cstring: 0xf0c
+  __TEXT.__swift5_typeref: 0x4d8
+  __TEXT.__swift5_reflstr: 0x3f8
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__constg_swiftt: 0x594
-  __TEXT.__swift5_fieldmd: 0x490
-  __TEXT.__oslogstring: 0xa4e
-  __TEXT.__swift5_proto: 0x84
-  __TEXT.__swift5_types: 0x54
+  __TEXT.__constg_swiftt: 0x6c4
+  __TEXT.__swift5_fieldmd: 0x4f8
+  __TEXT.__oslogstring: 0xcce
+  __TEXT.__swift5_proto: 0x8c
+  __TEXT.__swift5_types: 0x5c
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0x780
-  __TEXT.__eh_frame: 0xba0
-  __TEXT.__objc_methname: 0x14f
-  __DATA_CONST.__got: 0x1c0
+  __TEXT.__unwind_info: 0x930
+  __TEXT.__eh_frame: 0x10f8
+  __TEXT.__objc_methname: 0x15c
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0x1a0
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x720
-  __AUTH_CONST.__auth_ptr: 0x220
-  __AUTH_CONST.__const: 0x750
-  __AUTH_CONST.__objc_const: 0x728
-  __AUTH.__data: 0x168
-  __DATA.__data: 0x208
-  __DATA.__bss: 0xb00
+  __DATA_CONST.__objc_selrefs: 0x70
+  __AUTH_CONST.__auth_got: 0x7d8
+  __AUTH_CONST.__auth_ptr: 0x240
+  __AUTH_CONST.__const: 0x790
+  __AUTH_CONST.__objc_const: 0x910
+  __AUTH.__data: 0x368
+  __DATA.__data: 0x2a0
+  __DATA.__bss: 0xc00
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__data: 0x6b8
+  __DATA_DIRTY.__data: 0x6d0
   __DATA_DIRTY.__common: 0x40
   __DATA_DIRTY.__bss: 0x380
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftRegexBuilder.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswift_errno.dylib
   - /usr/lib/swift/libswift_math.dylib
   - /usr/lib/swift/libswift_signal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 719
-  Symbols:   298
-  CStrings:  146
+  Functions: 877
+  Symbols:   364
+  CStrings:  167
 
Symbols:
+ _OBJC_CLASS_$_AFSystemAssistantExperienceStatusManager
+ _swift_dynamicCast
- _AFDeviceSupportsSystemAssistantExperience
CStrings:
+ "_TtC19SiriAutoCompleteAPI19TypoRecoveryManager"
+ "Function: %!s(MISSING) > INPUT Count: '%!l(MISSING)d'"
+ "addToDBQueryCache(query:results:)"
+ "previousQueryResponse"
+ "Function: %!s(MISSING) > Using phrase from Cache"
+ "Cache hit: %!s(MISSING) > Using cached response for: '%!s(MISSING)'"
+ "dbQueryCache"
+ "getFromDBQueryCache(query:)"
+ "Function: %!s(MISSING) > Count stopWordFilteredPhrases: '%!l(MISSING)d'"
+ "Found phrase within fuzzyDistance threshold. Phrase: %!s(MISSING) => EditDistance: %!l(MISSING)d"
+ "previousQueryNearMatches"
+ "_TtC19SiriAutoCompleteAPI18TypingSessionCache"
+ "Cache read: %!s(MISSING) %!s(MISSING)"
+ "Cache write: %!s(MISSING) %!s(MISSING)"
+ "Typo recovery using previous query \"%!s(MISSING)\" close matches"
+ "isSAEEnabled"
+ "Function: %!s(MISSING) > Count rankedBasedOnSourceAndNormalizedScore: '%!l(MISSING)d'"
+ "filterAndRankPrefixMatches(candidatePhrases:normalizedQuery:isTypoRecovery:)"
+ "typingSessionCache"
+ "assetIdToPhraseMap"
+ "Typo recovery using all matched results leading up to current query"
+ "Phrase: %!s(MISSING), editDistance: %!f(MISSING), source: %!s(MISSING), bundleId: %!s(MISSING), actionIdentifier: %!s(MISSING)"
+ "Function: %!s(MISSING) > Count result: '%!l(MISSING)d'"
- "Phrase: %!s(MISSING), source: %!s(MISSING), bundleId: %!s(MISSING), actionIdentifier: %!s(MISSING)"
- "filterAndRankPrefixMatches(candidatePhrases:normalizedQuery:)"

```
