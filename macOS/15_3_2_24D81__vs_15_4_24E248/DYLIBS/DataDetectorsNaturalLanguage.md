## DataDetectorsNaturalLanguage

> `/System/Library/PrivateFrameworks/DataDetectorsNaturalLanguage.framework/Versions/A/DataDetectorsNaturalLanguage`

```diff

 174.0.0.0.0
-  __TEXT.__text: 0x2e04c
+  __TEXT.__text: 0x2ddec
   __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x19f8
+  __TEXT.__objc_methlist: 0x1a0c
   __TEXT.__const: 0x3a8
   __TEXT.__cstring: 0x18207
-  __TEXT.__gcc_except_tab: 0xaac
+  __TEXT.__gcc_except_tab: 0xab8
   __TEXT.__oslogstring: 0x1752
   __TEXT.__ustring: 0x2669a
-  __TEXT.__unwind_info: 0x7b8
+  __TEXT.__unwind_info: 0x7e8
   __TEXT.__objc_classname: 0x21a
   __TEXT.__objc_methname: 0x5f16
   __TEXT.__objc_methtype: 0x691

   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0xae0
   __AUTH_CONST.__cfstring: 0x363e0
-  __AUTH_CONST.__objc_const: 0x26a0
+  __AUTH_CONST.__objc_const: 0x2680
   __AUTH_CONST.__objc_doubleobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x7140

   - /System/Library/PrivateFrameworks/ResponseKit.framework/Versions/A/ResponseKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 895DEF23-AD95-3E56-8F1E-06573A6B7B95
-  Functions: 669
-  Symbols:   2020
+  UUID: A57434AE-67AD-3909-AB7F-8D7617649D44
+  Functions: 694
+  Symbols:   2098
   CStrings:  11636
 
Symbols:
+ +[IPEventClassificationType taxonomyForLanguageID:clusterIdentifier:].cold.1
+ +[IPFeatureScanner dataDetectorsFeatureExtractor].cold.1
+ +[IPFeatureScanner eventStore].cold.1
+ +[IPFeatureScanner keywordFeatureExtractor].cold.1
+ +[IPFeatureScanner sentenceFeatureExtractor].cold.1
+ +[IPFeatureSentence bestLanguageIDFromText:linesElided:].cold.1
+ +[IPFeatureSentence eventVocabularyRegexForType:languageID:].cold.1
+ +[IPMessageXMLParser dateFormatter].cold.1
+ +[IPRegexToolbox isRangeInsideQuotationMarks:text:limitToSurroundingText:].cold.1
+ +[IPTenseDetector tenseOfString:languageID:].cold.1
+ -[IPDataDetectorsFeatureExtractor featureDataComplementingFeatureData:hour:minute:duration:].cold.1
+ -[IPDataDetectorsFeatureExtractor featuresForTextString:inMessageUnit:context:].cold.1
+ -[IPDataDetectorsFeatureExtractor init].cold.1
+ -[IPDataDetectorsFeatureExtractor newYearsEveDayDateFromReferenceDate:].cold.1
+ -[IPDataDetectorsFeatureExtractor queue].cold.1
+ -[IPDataDetectorsFeatureExtractor thisSaturdayDateFromReferenceDate:].cold.1
+ -[IPDataDetectorsFeatureExtractor valentineDayDateFromReferenceDate:].cold.1
+ -[IPEventClassificationType _mealClassificationTypeUsingStartDate:].cold.1
+ -[IPEventClassificationType _mealClassificationTypeUsingStartDate:].cold.2
+ -[IPEventClassificationType adjustedEventTitleForMessageUnits:subject:dateInSubject:eventStartDate:useTitleGenerationModel:isGeneratedFromSubject:isGeneratedFromTitleGenerationModel:].cold.1
+ -[IPEventClassificationType adjustedEventTitleForMessageUnits:subject:dateInSubject:eventStartDate:useTitleGenerationModel:isGeneratedFromSubject:isGeneratedFromTitleGenerationModel:].cold.2
+ -[IPFeatureMailScanner doSynchronousScanWithCompletionHandler:].cold.1
+ -[IPFeatureMailScanner doSynchronousScanWithCompletionHandler:].cold.2
+ -[IPFeatureMailScanner doSynchronousScanWithCompletionHandler:].cold.3
+ -[IPFeatureMailScanner doSynchronousScanWithCompletionHandler:].cold.4
+ -[IPFeatureMailScanner doSynchronousScanWithCompletionHandler:].cold.5
+ -[IPFeatureMailScanner doSynchronousScanWithCompletionHandler:].cold.6
+ -[IPFeatureMailScanner processScanOfMessageUnit:].cold.1
+ -[IPFeatureMailScanner processScanOfMessageUnit:].cold.2
+ -[IPFeatureMailScanner scanEventsInMessageUnits:synchronously:completionHandler:].cold.1
+ -[IPFeatureScanner _regroupEventsWithSpreadTimeAsAllDayEvents:].cold.1
+ -[IPFeatureScanner adjustTimeForEvent:].cold.1
+ -[IPFeatureScanner adjustTimeForEvent:].cold.2
+ -[IPFeatureScanner adjustTimeForEvent:].cold.3
+ -[IPFeatureScanner cleanedStringForFeatureData:].cold.1
+ -[IPFeatureScanner decoratedTitle:withSubtitles:].cold.1
+ -[IPFeatureScanner decoratedTitle:withSubtitles:].cold.2
+ -[IPFeatureScanner featuresForTextString:inMessageUnit:extractors:context:].cold.1
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.1
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.10
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.2
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.3
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.4
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.5
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.6
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.7
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.8
+ -[IPFeatureScanner filteredEventsForDetectedEvents:referenceDate:].cold.9
+ -[IPFeatureScanner isDateAroundNoon:].cold.1
+ -[IPFeatureScanner isDateRoundedTo5Minutes:].cold.1
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.1
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.10
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.2
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.3
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.4
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.5
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.6
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.7
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.8
+ -[IPFeatureScanner isEventProposalOrConfirmationFromFeatures:fromFeatureAtIndex:messageUnit:eventIsTenseDependent:extractedFromSubject:extractedPolarity:polarityInfluencedByIpsosPlistRef:].cold.9
+ -[IPFeatureScanner normalizedAllDayDateFromDate:].cold.1
+ -[IPFeatureSentence isQuoteAttributionLine].cold.1
+ -[IPFeatureSentence isQuoteAttributionLine].cold.2
+ -[IPFeatureSentence isQuoteAttributionLine].cold.3
+ -[IPFeatureSentence polarityForRange:confidence:].cold.1
+ -[IPFeatureTextMessageScanner doSynchronousScanWithCompletionHandler:].cold.1
+ -[IPFeatureTextMessageScanner doSynchronousScanWithCompletionHandler:].cold.2
+ -[IPFeatureTextMessageScanner doSynchronousScanWithCompletionHandler:].cold.3
+ -[IPFeatureTextMessageScanner doSynchronousScanWithCompletionHandler:].cold.4
+ -[IPFeatureTextMessageScanner scanEventsInMessageUnits:contextMessageUnits:synchronously:completionHandler:].cold.1
+ -[IPFeatureTextMessageScanner scanEventsInMessageUnits:contextMessageUnits:synchronously:completionHandler:].cold.2
+ -[IPKeywordFeatureExtractor _matchingKeywordsForRegex:inText:message:eventType:keywordType:].cold.1
+ -[IPKeywordFeatureExtractor queue].cold.1
+ -[IPSentenceFeatureExtractor queue].cold.1
+ -[IPTextMessageConversation _scanEventsInLastMessageOnly:synchronously:completionHandler:].cold.1
+ IPInitLogging.cold.1
+ __183-[IPEventClassificationType adjustedEventTitleForMessageUnits:subject:dateInSubject:eventStartDate:useTitleGenerationModel:isGeneratedFromSubject:isGeneratedFromTitleGenerationModel:]_block_invoke.161
+ __183-[IPEventClassificationType adjustedEventTitleForMessageUnits:subject:dateInSubject:eventStartDate:useTitleGenerationModel:isGeneratedFromSubject:isGeneratedFromTitleGenerationModel:]_block_invoke.174
+ __59-[IPSentenceFeatureExtractor eventIdentifierForLanguageID:]_block_invoke.38
+ __59-[IPSentenceFeatureExtractor eventIdentifierForLanguageID:]_block_invoke.66
+ __60+[IPFeatureSentence eventVocabularyRegexForType:languageID:]_block_invoke.139
+ __60+[IPFeatureSentence eventVocabularyRegexForType:languageID:]_block_invoke_2.140
+ __69+[IPEventClassificationType taxonomyForLanguageID:clusterIdentifier:]_block_invoke.218
+ __71-[IPFeatureScanner analyzeFeatures:messageUnit:checkPolarity:polarity:]_block_invoke_2.cold.1
+ __75-[IPFeatureScanner featuresForTextString:inMessageUnit:extractors:context:]_block_invoke.37
+ __75-[IPFeatureScanner featuresForTextString:inMessageUnit:extractors:context:]_block_invoke.41
+ __block_literal_global.100
+ __block_literal_global.108
+ __block_literal_global.116
+ __block_literal_global.124
+ __block_literal_global.132
+ __block_literal_global.136
+ __block_literal_global.140
+ __block_literal_global.148
+ __block_literal_global.15
+ __block_literal_global.156
+ __block_literal_global.16
+ __block_literal_global.161
+ __block_literal_global.195
+ __block_literal_global.205
+ __block_literal_global.215
+ __block_literal_global.29
+ __block_literal_global.305
+ __block_literal_global.32
+ __block_literal_global.39
+ __block_literal_global.540
+ __block_literal_global.543
+ __block_literal_global.548
+ __block_literal_global.56
+ __block_literal_global.562
+ __block_literal_global.84
+ __block_literal_global.92
+ getCalendar.cold.1
+ isRangeNearbyExclusionKeyword:text:limitToSurroundingText:language:._ipExprOnceResult.82
+ isRangeNearbyExclusionKeyword:text:limitToSurroundingText:language:._onceToken.83
- __183-[IPEventClassificationType adjustedEventTitleForMessageUnits:subject:dateInSubject:eventStartDate:useTitleGenerationModel:isGeneratedFromSubject:isGeneratedFromTitleGenerationModel:]_block_invoke.155
- __183-[IPEventClassificationType adjustedEventTitleForMessageUnits:subject:dateInSubject:eventStartDate:useTitleGenerationModel:isGeneratedFromSubject:isGeneratedFromTitleGenerationModel:]_block_invoke.168
- __59-[IPSentenceFeatureExtractor eventIdentifierForLanguageID:]_block_invoke.32
- __59-[IPSentenceFeatureExtractor eventIdentifierForLanguageID:]_block_invoke.60
- __60+[IPFeatureSentence eventVocabularyRegexForType:languageID:]_block_invoke.133
- __60+[IPFeatureSentence eventVocabularyRegexForType:languageID:]_block_invoke_2.134
- __69+[IPEventClassificationType taxonomyForLanguageID:clusterIdentifier:]_block_invoke.212
- __75-[IPFeatureScanner featuresForTextString:inMessageUnit:extractors:context:]_block_invoke.31
- __75-[IPFeatureScanner featuresForTextString:inMessageUnit:extractors:context:]_block_invoke.35
- __block_literal_global.10
- __block_literal_global.102
- __block_literal_global.110
- __block_literal_global.118
- __block_literal_global.126
- __block_literal_global.130
- __block_literal_global.134
- __block_literal_global.142
- __block_literal_global.150
- __block_literal_global.155
- __block_literal_global.189
- __block_literal_global.199
- __block_literal_global.20
- __block_literal_global.209
- __block_literal_global.23
- __block_literal_global.293
- __block_literal_global.30
- __block_literal_global.33
- __block_literal_global.50
- __block_literal_global.534
- __block_literal_global.537
- __block_literal_global.542
- __block_literal_global.550
- __block_literal_global.78
- __block_literal_global.86
- __block_literal_global.9
- __block_literal_global.94
- isRangeNearbyExclusionKeyword:text:limitToSurroundingText:language:._ipExprOnceResult.76
- isRangeNearbyExclusionKeyword:text:limitToSurroundingText:language:._onceToken.77

```
