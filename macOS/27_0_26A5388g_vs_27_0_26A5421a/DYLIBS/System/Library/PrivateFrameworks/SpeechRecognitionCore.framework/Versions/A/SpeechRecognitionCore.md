## SpeechRecognitionCore

> `/System/Library/PrivateFrameworks/SpeechRecognitionCore.framework/Versions/A/SpeechRecognitionCore`

```diff

-39.0.0.0.0
-  __TEXT.__text: 0x1d0d0
+40.1.0.0.0
+  __TEXT.__text: 0x1d148
   __TEXT.__objc_methlist: 0xe3c
   __TEXT.__cstring: 0x1a84
   __TEXT.__gcc_except_tab: 0x1000
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
~ -[SRDCommandMatcher matchWithTranscriptionResult:] : 5548 -> 5552
~ -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:] -> -[SRDCommandMatcher _matchLiteralSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:] : 1024 -> 1008
~ -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:] -> -[SRDCommandMatcher _matchDictationSegment:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:] : 1260 -> 1272
~ -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:] -> -[SRDCommandMatcher _matchCacheSegment:segments:remainingSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:] : 3612 -> 3668
~ -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:] -> -[SRDCommandMatcher _matchSegments:transcription:cache:matchedObjects:consumedCacheKeys:shouldLog:isSpellingMode:checkLinguisticPrefix:] : 780 -> 824
~ -[SRDCommandMatcher _segmentMatchForTranscription:withTemplate:isSpellingMode:] -> -[SRDCommandMatcher _segmentMatchForTranscription:withTemplate:isSpellingMode:checkLinguisticPrefix:] : 252 -> 268
~ -[SRDCommandMatcher prefixMatchStatusForTranscription:isSpellingMode:] : 984 -> 988
```
