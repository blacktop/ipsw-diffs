## SpeechRecognitionCore

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/Versions/A/SpeechRecognitionCore`

```diff

-  __TEXT.__text: 0x1cc04
-  __TEXT.__objc_methlist: 0xe14
-  __TEXT.__cstring: 0x1a99
+  __TEXT.__text: 0x1d23c
+  __TEXT.__objc_methlist: 0xe3c
+  __TEXT.__cstring: 0x1b66
   __TEXT.__gcc_except_tab: 0x1000
-  __TEXT.__const: 0x13a
+  __TEXT.__const: 0x152
   __TEXT.__ustring: 0x41a
-  __TEXT.__oslogstring: 0x1054
+  __TEXT.__oslogstring: 0x10a2
   __TEXT.__swift5_typeref: 0x28
   __TEXT.__swift5_fieldmd: 0x10
-  __TEXT.__unwind_info: 0xb58
+  __TEXT.__unwind_info: 0xb78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xa48
+  __DATA_CONST.__objc_selrefs: 0xa60
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_arraydata: 0xf40
   __DATA_CONST.__got: 0x218
-  __AUTH_CONST.__const: 0x950
-  __AUTH_CONST.__cfstring: 0x37c0
-  __AUTH_CONST.__objc_const: 0x1f58
+  __AUTH_CONST.__const: 0x970
+  __AUTH_CONST.__cfstring: 0x3880
+  __AUTH_CONST.__objc_const: 0x1f88
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_dictobj: 0x1e0

   __AUTH_CONST.__auth_got: 0x720
   __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x180
-  __DATA.__objc_ivar: 0x188
+  __DATA.__objc_ivar: 0x18c
   __DATA.__data: 0x4a8
-  __DATA.__bss: 0x160
+  __DATA.__bss: 0x170
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreAudio.framework/Versions/A/CoreAudio
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 662
-  Symbols:   1807
-  CStrings:  979
+  Functions: 672
+  Symbols:   1824
+  CStrings:  991
 
Sections:
~ __TEXT.__swift5_fieldmd : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Symbols:
+ -[SRDCommandMatcher _coverageForRecognizedText:matchedObjects:]
+ -[SRDCommandMatcher _tokenCountInString:]
+ -[SRDConnection dealloc]
+ -[SRDMatchResult coverage]
+ -[SRDMatchResult initWithCommand:transcriptionResult:matched:score:numberOfAdlibs:numberOfCachePlaceholders:asrRank:coverage:parameters:matchedObjects:displayString:closeMatchType:]
+ OBJC_IVAR_$_SRDMatchResult._coverage
+ SRDShouldRelaxForKoreanNumberSlot
+ SRDShouldRelaxForKoreanNumberSlot.sNumberSlotIdentifiers
+ SRDShouldRelaxForKoreanNumberSlot.sNumberSlotIdentifiersOnce
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _SRDAppendLiteralToRegexPatternWithOptionalSpace
+ _SRDShouldRelaxForKoreanNumberSlot
+ ___SRDShouldRelaxForKoreanNumberSlot_block_invoke
+ _objc_msgSend$_coverageForRecognizedText:matchedObjects:
+ _objc_msgSend$_tokenCountInString:
+ _objc_msgSend$coverage
+ _objc_msgSend$initWithCommand:transcriptionResult:matched:score:numberOfAdlibs:numberOfCachePlaceholders:asrRank:coverage:parameters:matchedObjects:displayString:closeMatchType:
- -[SRDMatchResult initWithCommand:transcriptionResult:matched:score:numberOfAdlibs:numberOfCachePlaceholders:asrRank:parameters:matchedObjects:displayString:closeMatchType:]
- _objc_msgSend$initWithCommand:transcriptionResult:matched:score:numberOfAdlibs:numberOfCachePlaceholders:asrRank:parameters:matchedObjects:displayString:closeMatchType:
CStrings:
+ "  [%lu] Compiled exact match regex: '%{sensitive}@' -> '%{sensitive}@'"
+ "  [%lu] Compiled placeholder regex: '%{sensitive}@' -> '%{sensitive}@', metadata: %{public}@"
+ "  [%lu] Failed to compile placeholder regex for '%{sensitive}@': %{public}@"
+ "  [%lu] Failed to compile regex for '%{sensitive}@': %{public}@"
+ "  [%lu] Skipping invalid command string: '%{sensitive}@'"
+ "  [%lu] Using segment matching for '%{sensitive}@' (%lu cache placeholders), regex fallback: '%{sensitive}@'"
+ " ?"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jam3Tu/Sources/SpeechRecognitionCore/Sources/RXLanguageObject.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jam3Tu/Sources/SpeechRecognitionCore/Sources/RXObject.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jam3Tu/Sources/SpeechRecognitionCore/Sources/RXRecognitionSystem.mm"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.jam3Tu/Sources/SpeechRecognitionCore/Sources/RXXPC.mm"
+ "<%@: %p matched=%@ score=%.3f asrRank=%lu coverage=%lu closeMatchType=%lu \ncommand=%@ \ntranscription=%@ \nmatchedObjects=%@>"
+ "BuiltInLM.NumberTwoThroughNinetyNine"
+ "BuiltInLM.NumberTwoThroughNinetyNine.2"
+ "BuiltInLM.NumberZeroThroughOneHundred"
+ "BuiltInLM.ScreenDistanceCardinalNumber"
+ "BuiltInLM.TextSegmentCardinalNumber"
+ "[%{public}@] Cache hit for '%{public}@'='%{sensitive}@': %lu items"
+ "[%{public}@] Cache miss for '%{public}@'='%{sensitive}@' (key not found)"
+ "[%{public}@] Capture group %lu for '%{public}@': '%{sensitive}@'"
+ "[%{public}@] Close match check: '%{sensitive}@' (normalized)"
+ "[%{public}@] Close match found for '%{sensitive}@' (word distance=1)"
+ "[%{public}@] Dictation placeholder '%{public}@' captured: '%{sensitive}@'"
+ "[%{public}@] Segment: ambiguous cache match '%{sensitive}@' for '%{public}@'"
+ "[%{public}@] Segment: dictation found literal '%{sensitive}@' at position %lu"
+ "[%{public}@] Segment: extra text after all segments: '%{sensitive}@'"
+ "[%{public}@] Segment: literal '%{sensitive}@' matched"
+ "[%{public}@] Segment: literal '%{sensitive}@' mismatch"
+ "[%{public}@] Segment: multi-match branch for '%{public}@'='%{sensitive}@' result=%lu"
+ "[%{public}@] Segment: skipping consumed cache key '%{sensitive}@' for '%{public}@'"
+ "[%{public}@] Segment: transcription is prefix of literal '%{sensitive}@'"
+ "[%{public}@] Segment: trying '%{public}@'='%{sensitive}@'"
+ "[%{public}@] Segment: trying multi-match branch for '%{public}@'='%{sensitive}@'"
+ "[%{public}@] Trying regex for string %lu: '%{sensitive}@'"
- "  [%lu] Compiled exact match regex: '%{public}@' -> '%{public}@'"
- "  [%lu] Compiled placeholder regex: '%{public}@' -> '%{public}@', metadata: %{public}@"
- "  [%lu] Failed to compile placeholder regex for '%{public}@': %{public}@"
- "  [%lu] Failed to compile regex for '%{public}@': %{public}@"
- "  [%lu] Skipping invalid command string: '%{public}@'"
- "  [%lu] Using segment matching for '%{public}@' (%lu cache placeholders), regex fallback: '%{public}@'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1BBb6A/Sources/SpeechRecognitionCore/Sources/RXLanguageObject.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1BBb6A/Sources/SpeechRecognitionCore/Sources/RXObject.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1BBb6A/Sources/SpeechRecognitionCore/Sources/RXRecognitionSystem.mm"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.1BBb6A/Sources/SpeechRecognitionCore/Sources/RXXPC.mm"
- "<%@: %p matched=%@ score=%.3f asrRank=%lu closeMatchType=%lu \ncommand=%@ \ntranscription=%@ \nmatchedObjects=%@>"
- "[%{public}@] Cache hit for '%{public}@'='%{public}@': %lu items"
- "[%{public}@] Cache miss for '%{public}@'='%{public}@' (key not found)"
- "[%{public}@] Capture group %lu for '%{public}@': '%{public}@'"
- "[%{public}@] Close match check: '%{public}@' (normalized)"
- "[%{public}@] Close match found for '%{public}@' (word distance=1)"
- "[%{public}@] Dictation placeholder '%{public}@' captured: '%{public}@'"
- "[%{public}@] Segment: ambiguous cache match '%{public}@' for '%{public}@'"
- "[%{public}@] Segment: dictation found literal '%{public}@' at position %lu"
- "[%{public}@] Segment: extra text after all segments: '%{public}@'"
- "[%{public}@] Segment: literal '%{public}@' matched"
- "[%{public}@] Segment: literal '%{public}@' mismatch"
- "[%{public}@] Segment: multi-match branch for '%{public}@'='%{public}@' result=%lu"
- "[%{public}@] Segment: skipping consumed cache key '%{public}@' for '%{public}@'"
- "[%{public}@] Segment: transcription is prefix of literal '%{public}@'"
- "[%{public}@] Segment: trying '%{public}@'='%{public}@'"
- "[%{public}@] Segment: trying multi-match branch for '%{public}@'='%{public}@'"
- "[%{public}@] Trying regex for string %lu: '%{public}@'"

```
