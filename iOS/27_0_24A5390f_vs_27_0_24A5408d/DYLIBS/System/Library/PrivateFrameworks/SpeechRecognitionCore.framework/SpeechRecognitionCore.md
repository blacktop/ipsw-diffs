## SpeechRecognitionCore

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/SpeechRecognitionCore`

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
