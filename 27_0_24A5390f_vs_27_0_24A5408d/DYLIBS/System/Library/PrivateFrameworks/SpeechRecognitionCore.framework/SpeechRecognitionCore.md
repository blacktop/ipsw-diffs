## SpeechRecognitionCore

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__cstring`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-39.0.0.0.0
-  __TEXT.__text: 0x1ba88
+40.1.0.0.0
+  __TEXT.__text: 0x1baec
   __TEXT.__objc_methlist: 0xe3c
   __TEXT.__cstring: 0x19ec
   __TEXT.__gcc_except_tab: 0xf90
Symbols:
+ -[SRDBuiltInLMMatchingCache hasLinguisticExtensionForItem:forIdentifier:]
+ -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:]
+ -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:]
+ -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:]
+ -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:]
+ -[SRDCommandMatcher _segmentMatchForTranscription:withTemplate:isSpellingMode:checkLinguisticPrefix:]
+ _objc_msgSend$_matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:
+ _objc_msgSend$_matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:
+ _objc_msgSend$_matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:
+ _objc_msgSend$_matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:
+ _objc_msgSend$_segmentMatchForTranscription:withTemplate:isSpellingMode:checkLinguisticPrefix:
+ _objc_msgSend$hasLinguisticExtensionForItem:forIdentifier:
- -[SRDBuiltInLMMatchingCache hasAmbiguousPrefixForItem:forIdentifier:]
- -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:]
- -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:]
- -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:]
- -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:]
- -[SRDCommandMatcher _segmentMatchForTranscription:withTemplate:isSpellingMode:]
- _objc_msgSend$_matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:
- _objc_msgSend$_matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:
- _objc_msgSend$_matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:
- _objc_msgSend$_matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:
- _objc_msgSend$_segmentMatchForTranscription:withTemplate:isSpellingMode:
- _objc_msgSend$hasAmbiguousPrefixForItem:forIdentifier:
Functions:
~ -[SRDCommandMatcher matchWithTranscriptionResult:] : 5348 -> 5352
~ -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:] -> -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:] : 920 -> 908
~ -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:] -> -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:] : 1160 -> 1172
~ -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:] -> -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:] : 3412 -> 3444
~ -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:] -> -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:] : 720 -> 764
~ -[SRDCommandMatcher _segmentMatchForTranscription:withTemplate:isSpellingMode:] -> -[SRDCommandMatcher _segmentMatchForTranscription:withTemplate:isSpellingMode:checkLinguisticPrefix:] : 236 -> 252
~ -[SRDCommandMatcher prefixMatchStatusForTranscription:isSpellingMode:] : 960 -> 964
```
