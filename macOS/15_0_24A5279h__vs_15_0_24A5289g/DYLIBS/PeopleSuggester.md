## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/Versions/A/PeopleSuggester`

```diff

-1880.0.1.0.0
-  __TEXT.__text: 0xfefd8
+1882.0.0.0.0
+  __TEXT.__text: 0xfee60
   __TEXT.__auth_stubs: 0xc40
-  __TEXT.__objc_methlist: 0xa47c
+  __TEXT.__objc_methlist: 0xa48c
   __TEXT.__const: 0x708
-  __TEXT.__gcc_except_tab: 0x2abc
-  __TEXT.__cstring: 0xa507
-  __TEXT.__oslogstring: 0xb759
-  __TEXT.__dlopen_cstrs: 0x166e
-  __TEXT.__unwind_info: 0x28e8
+  __TEXT.__gcc_except_tab: 0x2ad4
+  __TEXT.__cstring: 0xa564
+  __TEXT.__oslogstring: 0xb768
+  __TEXT.__dlopen_cstrs: 0x16c4
+  __TEXT.__unwind_info: 0x28f8
   __TEXT.__objc_classname: 0x12fe
-  __TEXT.__objc_methname: 0x22416
+  __TEXT.__objc_methname: 0x223a5
   __TEXT.__objc_methtype: 0x2a2a
-  __TEXT.__objc_stubs: 0x12300
+  __TEXT.__objc_stubs: 0x122c0
   __DATA_CONST.__got: 0x7e8
-  __DATA_CONST.__const: 0x1088
+  __DATA_CONST.__const: 0x10c0
   __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_arraydata: 0xdb8
   __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x3180
-  __AUTH_CONST.__cfstring: 0xa160
-  __AUTH_CONST.__objc_const: 0x15900
+  __AUTH_CONST.__const: 0x3190
+  __AUTH_CONST.__cfstring: 0xa1a0
+  __AUTH_CONST.__objc_const: 0x158f8
   __AUTH_CONST.__objc_intobj: 0x1080
   __AUTH_CONST.__objc_arrayobj: 0x8b8
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x2d50
-  __DATA.__objc_ivar: 0xf1c
+  __DATA.__objc_ivar: 0xf20
   __DATA.__data: 0x428
-  __DATA.__bss: 0xd68
+  __DATA.__bss: 0xd78
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4694
-  Symbols:   11229
-  CStrings:  1614
+  Functions: 4699
+  Symbols:   11236
+  CStrings:  1619
 
Symbols:
+ +[_PSInteractionPredictor deleteArchiveFileAtDate:modelName:].cold.3
+ +[_PSInteractionStoreUtils metadataFromFeedbackEvent:]
+ -[_PSFeedback donateToBiome]
+ -[_PSFeedback donateToBiome].cold.1
+ -[_PSMapsFeedback donateToBiome]
+ -[_PSPredictionContext feedBack]
+ -[_PSPredictionContext setFeedBack:]
+ GCC_except_table122
+ GCC_except_table168
+ OBJC_IVAR_$__PSPredictionContext._feedBack
+ _OBJC_CLASS_$_BMMapsShareETAFeedback
+ _OUTLINED_FUNCTION_9
+ __118-[_PSSuggestionFromTextPredictor suggestionsFromIncompleteRemindersWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.78
+ __125-[_PSSuggestionFromTextPredictor suggestionsFromUnstructuredCalendarEventsWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.96
+ __28-[_PSFeedback donateToBiome]_block_invoke_2.cold.1
+ __62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.544
+ __62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.544.cold.1
+ __72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.501
+ __72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.511
+ __73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.556
+ __98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.68
+ __98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.70
+ ___28-[_PSFeedback donateToBiome]_block_invoke
+ ___28-[_PSFeedback donateToBiome]_block_invoke_2
+ ___block_descriptor_32_e26_"NSString"16?0"NSUUID"8l
+ ___block_descriptor_32_e30_"NSData"16?0"NSDictionary"8l
+ ___block_descriptor_64_e8_32s40s48s56s_e26_B24?0"BMStoreEvent"8^B16l
+ ___getBMMapsShareETAFeedbackClass_block_invoke
+ __block_literal_global.498
+ __block_literal_global.514
+ __block_literal_global.518
+ __block_literal_global.543
+ __block_literal_global.555
+ __block_literal_global.86
+ __getBMMapsShareETAFeedbackClass_block_invoke.cold.1
+ _objc_msgSend$ETAFeedback
+ _objc_msgSend$MapsShare
+ _objc_msgSend$deleteWithPolicy:eventsPassingTest:
+ _objc_msgSend$donateToBiome
+ _objc_msgSend$endLocationId
+ _objc_msgSend$feedBack
+ _objc_msgSend$initWithIdentifier:bundleId:handle:startLocationId:endLocationId:contactId:groupId:
+ _objc_msgSend$pruner
+ _objc_msgSend$startLocationId
+ _suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken171
+ formatWithSuggestion:bundleIdsForGroupMatching:checkForMessagesGroupIdentifier:._pasOnceToken7
+ getBMMapsShareETAFeedbackClass.softClass
+ getPhotoBasedFeaturesAsync:withTimeout:._pasOnceToken40
+ getResultsFromTransformers:suggestions:._pasOnceToken19
+ init._pasOnceToken6
+ predictWithPredictionContext:maxSuggestions:contactKeysToFetch:._pasOnceToken118
- -[_PSFeedback knowledgeEvent]
- -[_PSFeedback knowledgeEvent].cold.1
- -[_PSMapsFeedback knowledgeEvent]
- -[_PSMapsSuggester provideMapsFeedback:].cold.3
- -[_PSSuggester donateToBiome:]
- GCC_except_table125
- GCC_except_table171
- _OBJC_CLASS_$__DKMapsShareEtaFeedbackMetadataKey
- __118-[_PSSuggestionFromTextPredictor suggestionsFromIncompleteRemindersWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.81
- __125-[_PSSuggestionFromTextPredictor suggestionsFromUnstructuredCalendarEventsWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.99
- __46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke_3.cold.1
- __62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.553
- __62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.553.cold.1
- __72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.510
- __72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.520
- __73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.565
- __98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.71
- __98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.73
- __99-[_PSMapsSuggester deleteMapsFeedbackEventsMatchingHandle:contactId:startLocationId:endLocationId:]_block_invoke.cold.1
- ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke_2
- ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke_3
- ___block_descriptor_32_e20_v24?0Q8"NSError"16l
- __block_literal_global.500
- __block_literal_global.503
- __block_literal_global.508
- __block_literal_global.523
- __block_literal_global.527
- __block_literal_global.561
- __block_literal_global.564
- __block_literal_global.89
- _objc_msgSend$deleteAllEventsMatchingPredicate:responseQueue:withCompletion:
- _objc_msgSend$donateToBiome:
- _objc_msgSend$eventWithStream:source:startDate:endDate:categoryIntegerValue:metadata:
- _objc_msgSend$knowledgeEvent
- _objc_msgSend$mapsShareEtaFeedbackStream
- _objc_msgSend$navigationEndLocationIdentifier
- _objc_msgSend$navigationStartLocationIdentifier
- _objc_msgSend$predicateForEventsWithStreamName:
- _objc_msgSend$predicateForObjectsWithMetadataKey:andValue:
- _objc_msgSend$saveObjects:error:
- _objc_msgSend$shareSheetFeedbackStream
- _suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken167
- formatWithSuggestion:bundleIdsForGroupMatching:checkForMessagesGroupIdentifier:._pasOnceToken8
- getPhotoBasedFeaturesAsync:withTimeout:._pasOnceToken36
- getResultsFromTransformers:suggestions:._pasOnceToken20
- init._pasOnceToken2
- predictWithPredictionContext:maxSuggestions:contactKeysToFetch:._pasOnceToken114
CStrings:
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/PFL/LighthouseShareSheetPFLTraining.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
+ "@\"NSData\"16@?0@\"NSDictionary\"8"
+ "@\"NSString\"16@?0@\"NSUUID\"8"
+ "B24@?0@\"BMStoreEvent\"8^B16"
+ "BMMapsShareETAFeedback"
+ "MapsShareETAFeedback"
+ "delete-maps-feedback"
+ "feedBack"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/PFL/LighthouseShareSheetPFLTraining.m"
- "/AppleInternal/Library/BuildRoots/fd9f31ad-2a77-11ef-8189-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
- "com.apple.PeopleSuggester.MapsShareETAFeedbackDelete"
- "mapsShareEta"

```
