## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/Versions/A/PeopleSuggester`

```diff

-1892.6.3.0.0
-  __TEXT.__text: 0x101e50
-  __TEXT.__auth_stubs: 0xc70
-  __TEXT.__objc_methlist: 0xa544
-  __TEXT.__const: 0x718
-  __TEXT.__gcc_except_tab: 0x2d28
-  __TEXT.__cstring: 0xa93f
-  __TEXT.__oslogstring: 0xb9ba
-  __TEXT.__dlopen_cstrs: 0x16c4
-  __TEXT.__unwind_info: 0x29e0
-  __TEXT.__objc_classname: 0x12fe
-  __TEXT.__objc_methname: 0x2296f
-  __TEXT.__objc_methtype: 0x2a3f
-  __TEXT.__objc_stubs: 0x127a0
-  __DATA_CONST.__got: 0x840
-  __DATA_CONST.__const: 0x1148
-  __DATA_CONST.__objc_classlist: 0x550
+1892.20.1.0.0
+  __TEXT.__text: 0x107f70
+  __TEXT.__auth_stubs: 0xcb0
+  __TEXT.__objc_methlist: 0xae0c
+  __TEXT.__const: 0x728
+  __TEXT.__gcc_except_tab: 0x2d44
+  __TEXT.__cstring: 0xaffa
+  __TEXT.__oslogstring: 0xbd3f
+  __TEXT.__dlopen_cstrs: 0x16d2
+  __TEXT.__unwind_info: 0x2b50
+  __TEXT.__eh_frame: 0x50
+  __TEXT.__objc_classname: 0x131e
+  __TEXT.__objc_methname: 0x2422a
+  __TEXT.__objc_methtype: 0x2b4d
+  __TEXT.__objc_stubs: 0x12f00
+  __DATA_CONST.__got: 0x858
+  __DATA_CONST.__const: 0x1228
+  __DATA_CONST.__objc_classlist: 0x558
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6688
-  __DATA_CONST.__objc_superrefs: 0x3f8
-  __DATA_CONST.__objc_arraydata: 0xdb8
-  __AUTH_CONST.__auth_got: 0x648
-  __AUTH_CONST.__const: 0x3470
-  __AUTH_CONST.__cfstring: 0xa360
-  __AUTH_CONST.__objc_const: 0x15918
+  __DATA_CONST.__objc_selrefs: 0x6b30
+  __DATA_CONST.__objc_superrefs: 0x400
+  __DATA_CONST.__objc_arraydata: 0xdd8
+  __AUTH_CONST.__auth_got: 0x668
+  __AUTH_CONST.__const: 0x3570
+  __AUTH_CONST.__cfstring: 0xab60
+  __AUTH_CONST.__objc_const: 0x15a68
   __AUTH_CONST.__objc_intobj: 0x10e0
-  __AUTH_CONST.__objc_arrayobj: 0x8b8
-  __AUTH_CONST.__objc_doubleobj: 0xe0
+  __AUTH_CONST.__objc_arrayobj: 0x918
+  __AUTH_CONST.__objc_doubleobj: 0x110
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x2d50
-  __DATA.__objc_ivar: 0xf24
+  __AUTH.__objc_data: 0x2da0
+  __DATA.__objc_ivar: 0xf90
   __DATA.__data: 0x428
-  __DATA.__bss: 0xd88
+  __DATA.__bss: 0xda0
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94D60E6D-FE83-3F7A-8A2A-7FD5BF1C8EC9
-  Functions: 4748
-  Symbols:   11370
-  CStrings:  9155
+  UUID: 0EE61D34-FBED-3C26-B508-4DA7D24A006E
+  Functions: 4925
+  Symbols:   11667
+  CStrings:  9471
 
Symbols:
+ +[AeroMLTracerSession logChannelWithSubsystem:category:].cold.1
+ +[PeopleSuggesterShareEvent photoFeaturesType]
+ +[_PSBlockedHandlesCache sharedBlockedHandlesCache].cold.1
+ +[_PSCandidate selfCandidate].cold.1
+ +[_PSConstants mailBundleIds].cold.1
+ +[_PSConstants messagesBundleIds].cold.1
+ +[_PSConstants shareplayBundleIds].cold.1
+ +[_PSConstants systemBundleIds].cold.1
+ +[_PSContactCache sharedInstance].cold.1
+ +[_PSContactSuggester contactPriorSuggestionsForText:].cold.1
+ +[_PSContactSuggester contactPriorSuggestionsForText:].cold.2
+ +[_PSEnsembleModel _suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:].cold.2
+ +[_PSFTZKWSuggestionsTransformerFactory getResultsFromTransformers:suggestions:].cold.1
+ +[_PSFeatureDictionary _fromPlistValue:timeBucket:].cold.1
+ +[_PSFeatureDictionary _fromPlistValue:timeBucket:].cold.2
+ +[_PSFeatureDictionary _fromPlistValue:timeBucket:].cold.3
+ +[_PSFeatureDictionary _fromPlistValue:timeBucket:].cold.4
+ +[_PSFeatureDictionary _fromPlistValue:timeBucket:].cold.5
+ +[_PSFeatureDictionary _fromPlistValue:timeBucket:].cold.6
+ +[_PSFeatureDictionary _fromPlistValue:timeBucket:].cold.7
+ +[_PSLogging contactEmbeddingChannel].cold.1
+ +[_PSLogging coreBehaviorChannel].cold.1
+ +[_PSLogging familyRecommenderChannel].cold.1
+ +[_PSLogging featureGenerationChannel].cold.1
+ +[_PSLogging feedbackChannel].cold.1
+ +[_PSLogging generalChannel].cold.1
+ +[_PSLogging heuristicsChannel].cold.1
+ +[_PSLogging knnChannel].cold.1
+ +[_PSLogging mediaAnalysisChannel].cold.1
+ +[_PSLogging messagePinningChannel].cold.1
+ +[_PSLogging rewriteChannel].cold.1
+ +[_PSLogging shareExtensionChannel].cold.1
+ +[_PSLogging suggestionSignpost].cold.1
+ +[_PSPETMessageBuilder contentTypeFromUTI:]
+ +[_PSPhotoSuggestions allOutstandingRequestsLock].cold.1
+ +[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:]
+ +[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]
+ +[_PSPhotoSuggestions phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]
+ +[_PSPhotoSuggestions sharedMADService].cold.1
+ -[NSString(_PSInteractionAndContactMonitor) _ps_pointerSizedHash].cold.1
+ -[PeopleSuggesterCandidate hasHasSharedSensitiveContentWIthConversation]
+ -[PeopleSuggesterCandidate hasIsFirstPartyApp]
+ -[PeopleSuggesterCandidate hasIsInPhoneCallWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfAppsSharedFromWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfDifferentFacesSharedWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfSharesFromAlbumPhotoBelongsToWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfSharesOfDetectedScenesInPhotoWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfSharesOfPeopleInPhotoIoUWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfSharesOfPetsInCurrentPhotoWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfSharesOfPetsWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfSharesOfScenesInPhotoWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfTimesSharedToTargetAppWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfTopicsSharedWithConversation]
+ -[PeopleSuggesterCandidate hasNumberOfTotalSharesToTargetApp]
+ -[PeopleSuggesterCandidate hasSharedSensitiveContentWIthConversation]
+ -[PeopleSuggesterCandidate hasTimeSinceLastPhoneCallWithConversation]
+ -[PeopleSuggesterCandidate hasTimeSinceLastPhotoShareWithConversation]
+ -[PeopleSuggesterCandidate hasTimeSinceLastShareWithConversation]
+ -[PeopleSuggesterCandidate isFirstPartyApp]
+ -[PeopleSuggesterCandidate isInPhoneCallWithConversation]
+ -[PeopleSuggesterCandidate numberOfAppsSharedFromWithConversation]
+ -[PeopleSuggesterCandidate numberOfDifferentFacesSharedWithConversation]
+ -[PeopleSuggesterCandidate numberOfSharesFromAlbumPhotoBelongsToWithConversation]
+ -[PeopleSuggesterCandidate numberOfSharesOfDetectedScenesInPhotoWithConversation]
+ -[PeopleSuggesterCandidate numberOfSharesOfPeopleInPhotoIoUWithConversation]
+ -[PeopleSuggesterCandidate numberOfSharesOfPetsInCurrentPhotoWithConversation]
+ -[PeopleSuggesterCandidate numberOfSharesOfPetsWithConversation]
+ -[PeopleSuggesterCandidate numberOfSharesOfScenesInPhotoWithConversation]
+ -[PeopleSuggesterCandidate numberOfTimesSharedToTargetAppWithConversation]
+ -[PeopleSuggesterCandidate numberOfTopicsSharedWithConversation]
+ -[PeopleSuggesterCandidate numberOfTotalSharesToTargetApp]
+ -[PeopleSuggesterCandidate setHasIsFirstPartyApp:]
+ -[PeopleSuggesterCandidate setHasIsInPhoneCallWithConversation:]
+ -[PeopleSuggesterCandidate setHasSharedSensitiveContentWIthConversation:]
+ -[PeopleSuggesterCandidate setIsFirstPartyApp:]
+ -[PeopleSuggesterCandidate setIsInPhoneCallWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfAppsSharedFromWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfDifferentFacesSharedWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfSharesFromAlbumPhotoBelongsToWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfSharesOfDetectedScenesInPhotoWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfSharesOfPeopleInPhotoIoUWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfSharesOfPetsInCurrentPhotoWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfSharesOfPetsWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfSharesOfScenesInPhotoWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfTimesSharedToTargetAppWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfTopicsSharedWithConversation:]
+ -[PeopleSuggesterCandidate setNumberOfTotalSharesToTargetApp:]
+ -[PeopleSuggesterCandidate setTimeSinceLastPhoneCallWithConversation:]
+ -[PeopleSuggesterCandidate setTimeSinceLastPhotoShareWithConversation:]
+ -[PeopleSuggesterCandidate setTimeSinceLastShareWithConversation:]
+ -[PeopleSuggesterCandidate timeSinceLastPhoneCallWithConversation]
+ -[PeopleSuggesterCandidate timeSinceLastPhotoShareWithConversation]
+ -[PeopleSuggesterCandidate timeSinceLastShareWithConversation]
+ -[PeopleSuggesterPhotoFeatures copyTo:]
+ -[PeopleSuggesterPhotoFeatures copyWithZone:]
+ -[PeopleSuggesterPhotoFeatures description]
+ -[PeopleSuggesterPhotoFeatures dictionaryRepresentation]
+ -[PeopleSuggesterPhotoFeatures hasIsFavorited]
+ -[PeopleSuggesterPhotoFeatures hasIsScreenShot]
+ -[PeopleSuggesterPhotoFeatures hash]
+ -[PeopleSuggesterPhotoFeatures isEqual:]
+ -[PeopleSuggesterPhotoFeatures isFavorited]
+ -[PeopleSuggesterPhotoFeatures isScreenShot]
+ -[PeopleSuggesterPhotoFeatures mergeFrom:]
+ -[PeopleSuggesterPhotoFeatures readFrom:]
+ -[PeopleSuggesterPhotoFeatures setHasIsFavorited:]
+ -[PeopleSuggesterPhotoFeatures setHasIsScreenShot:]
+ -[PeopleSuggesterPhotoFeatures setIsFavorited:]
+ -[PeopleSuggesterPhotoFeatures setIsScreenShot:]
+ -[PeopleSuggesterPhotoFeatures writeTo:]
+ -[PeopleSuggesterShareEvent StringAsTypeOfContents:]
+ -[PeopleSuggesterShareEvent addPhotoFeatures:]
+ -[PeopleSuggesterShareEvent addTypeOfContent:]
+ -[PeopleSuggesterShareEvent clearPhotoFeatures]
+ -[PeopleSuggesterShareEvent clearTypeOfContents]
+ -[PeopleSuggesterShareEvent dealloc]
+ -[PeopleSuggesterShareEvent hasIsInPhoneCall]
+ -[PeopleSuggesterShareEvent hasIsScreenShot]
+ -[PeopleSuggesterShareEvent hasTimeSinceLastShare]
+ -[PeopleSuggesterShareEvent isInPhoneCall]
+ -[PeopleSuggesterShareEvent isScreenShot]
+ -[PeopleSuggesterShareEvent photoFeaturesAtIndex:]
+ -[PeopleSuggesterShareEvent photoFeaturesCount]
+ -[PeopleSuggesterShareEvent photoFeatures]
+ -[PeopleSuggesterShareEvent setHasIsInPhoneCall:]
+ -[PeopleSuggesterShareEvent setHasIsScreenShot:]
+ -[PeopleSuggesterShareEvent setIsInPhoneCall:]
+ -[PeopleSuggesterShareEvent setIsScreenShot:]
+ -[PeopleSuggesterShareEvent setPhotoFeatures:]
+ -[PeopleSuggesterShareEvent setTimeSinceLastShare:]
+ -[PeopleSuggesterShareEvent setTypeOfContents:count:]
+ -[PeopleSuggesterShareEvent timeSinceLastShare]
+ -[PeopleSuggesterShareEvent typeOfContentAtIndex:]
+ -[PeopleSuggesterShareEvent typeOfContentsAsString:]
+ -[PeopleSuggesterShareEvent typeOfContentsCount]
+ -[PeopleSuggesterShareEvent typeOfContents]
+ -[_PSBlockedHandlesCache handlePrivacyManagerChangeNotification:].cold.1
+ -[_PSEnsembleModel enrichConfig:withInformationFromPredictionContext:andAppToAppExtMapping:]
+ -[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:].cold.1
+ -[_PSEnsembleModel getReasonTypesFromObjects:]
+ -[_PSEnsembleModel getReasonTypesFromObjects:limit:]
+ -[_PSEnsembleModel init].cold.1
+ -[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:].cold.6
+ -[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:].cold.7
+ -[_PSEnsembleModel psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:]
+ -[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:].cold.4
+ -[_PSFTZKWOrchestrator _getDirectSuggestionsWithContext:withTimeout:].cold.1
+ -[_PSFTZKWSuggestionsTransformerFactory formatWithSuggestion:bundleIdsForGroupMatching:checkForMessagesGroupIdentifier:].cold.3
+ -[_PSFeatureCache setFeatureValueForFeatureName:featureValue:candidate:bundleID:].cold.3
+ -[_PSFeatureDictionary setObject:forKey:].cold.1
+ -[_PSHeuristics hyperRecentCallHeuristicSuggestionProxiesForInteractionStatistics:]
+ -[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:]
+ -[_PSHeuristics maxNumberOfSuggestionSlotsForHeuristic:]
+ -[_PSHeuristics peopleAwareSuggestionProxiesForDetectedFaces:]
+ -[_PSHeuristics peopleAwareSuggestionProxiesForDetectedFaces:].cold.1
+ -[_PSHeuristics pslRecencyMargin]
+ -[_PSHeuristics recencyMarginInSecondsForHeuristic:]
+ -[_PSHeuristics scenesBasedFeaturesAwareSuggestionProxiesForInteractionStatistics:forFeatureNames:]
+ -[_PSHeuristics setPslRecencyMargin:]
+ -[_PSHeuristics thresholdForHeuristic:]
+ -[_PSHeuristics updateHeuristicParameterOverrides:]
+ -[_PSHeuristics valueForHeuristic:parameter:]
+ -[_PSInteractionPredictor rankedZkwSuggestionsFromPredictionArray:forBundleID:].cold.1
+ -[_PSKNNModel contactKeysToFetch].cold.1
+ -[_PSPredictionContext supportsZKWSuggestions].cold.1
+ -[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:].cold.2
+ -[_PSSuggester autocompleteSearchResultsWithPredictionContext:].cold.1
+ -[_PSSuggester rankedZKWSuggestionsFromContext:].cold.3
+ -[_PSSuggester reportShareSheetTimeoutWithError:]
+ -[_PSSuggester(InteractionInformation) _dateFormatter].cold.1
+ -[_PSTrialClient psHeuristicsOverrides]
+ -[_PSTrialClient scenesBasedFeatures]
+ -[_PSTrialClient scenesMinimumNumberOfTags]
+ -[_PSTrialClient shouldProcessPicturesLive]
+ -[_PS_TPSDiscoverabilitySignal _knowledgeStore].cold.1
+ GCC_except_table101
+ GCC_except_table110
+ GCC_except_table115
+ GCC_except_table128
+ GCC_except_table14
+ GCC_except_table150
+ GCC_except_table175
+ GCC_except_table294
+ GCC_except_table306
+ GCC_except_table35
+ GCC_except_table36
+ GCC_except_table42
+ GCC_except_table50
+ GCC_except_table59
+ GCC_except_table65
+ GCC_except_table70
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table87
+ GCC_except_table88
+ GCC_except_table91
+ GCC_except_table98
+ OBJC_IVAR_$_PeopleSuggesterCandidate._hasSharedSensitiveContentWIthConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._isFirstPartyApp
+ OBJC_IVAR_$_PeopleSuggesterCandidate._isInPhoneCallWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfAppsSharedFromWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfDifferentFacesSharedWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfSharesFromAlbumPhotoBelongsToWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfSharesOfDetectedScenesInPhotoWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfSharesOfPeopleInPhotoIoUWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfSharesOfPetsInCurrentPhotoWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfSharesOfPetsWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfSharesOfScenesInPhotoWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfTimesSharedToTargetAppWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfTopicsSharedWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._numberOfTotalSharesToTargetApp
+ OBJC_IVAR_$_PeopleSuggesterCandidate._timeSinceLastPhoneCallWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._timeSinceLastPhotoShareWithConversation
+ OBJC_IVAR_$_PeopleSuggesterCandidate._timeSinceLastShareWithConversation
+ OBJC_IVAR_$_PeopleSuggesterPhotoFeatures._has
+ OBJC_IVAR_$_PeopleSuggesterPhotoFeatures._isFavorited
+ OBJC_IVAR_$_PeopleSuggesterPhotoFeatures._isScreenShot
+ OBJC_IVAR_$_PeopleSuggesterShareEvent._isInPhoneCall
+ OBJC_IVAR_$_PeopleSuggesterShareEvent._isScreenShot
+ OBJC_IVAR_$_PeopleSuggesterShareEvent._photoFeatures
+ OBJC_IVAR_$_PeopleSuggesterShareEvent._timeSinceLastShare
+ OBJC_IVAR_$_PeopleSuggesterShareEvent._typeOfContents
+ OBJC_IVAR_$__PSHeuristics._config
+ OBJC_IVAR_$__PSHeuristics._configOverrides
+ OBJC_IVAR_$__PSHeuristics._pslRecencyMargin
+ SiriEntityMatcherLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_PeopleSuggesterPhotoFeatures
+ _OBJC_CLASS_$__CDInteractionsStatisticsConfig
+ _OBJC_METACLASS_$_PeopleSuggesterPhotoFeatures
+ _PBRepeatedInt32Add
+ _PBRepeatedInt32Clear
+ _PBRepeatedInt32Copy
+ _PBRepeatedInt32Hash
+ _PBRepeatedInt32IsEqual
+ _PBRepeatedInt32Set
+ _PSShareSheetSuggestionBundleIDMapping.cold.1
+ _PeopleSuggesterPhotoFeaturesReadFrom
+ _SiriEntityMatcherLibraryCore
+ _SuggestionProxyTypeHyperRecencyCallRewrite
+ _SuggestionProxyTypePASSv1
+ _SuggestionProxyTypeSASS
+ __105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.1031
+ __105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.1040
+ __106-[_PSContactSuggesterForPeopleWidget contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.48
+ __106-[_PSContactSuggesterForPeopleWidget contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.51
+ __108-[_PSHeuristics heuristicsFromInteractionsStatistics:forStatsNames:threshold:maxNumberOfSuggestions:reason:]_block_invoke.305
+ __108-[_PSHeuristics heuristicsFromInteractionsStatistics:forStatsNames:threshold:maxNumberOfSuggestions:reason:]_block_invoke.307
+ __108-[_PSHeuristics heuristicsFromInteractionsStatistics:forStatsNames:threshold:maxNumberOfSuggestions:reason:]_block_invoke.310
+ __118-[_PSSuggestionFromTextPredictor suggestionsFromIncompleteRemindersWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.90
+ __120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.937
+ __125-[_PSSuggestionFromTextPredictor suggestionsFromUnstructuredCalendarEventsWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.108
+ __126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.844
+ __126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.844.cold.1
+ __132-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:]_block_invoke.270
+ __132-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:]_block_invoke.274
+ __150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.214
+ __150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.221
+ __163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke.55
+ __23-[_PSContactCache init]_block_invoke.45
+ __23-[_PSContactCache init]_block_invoke.48
+ __27-[_PSProximityBooster init]_block_invoke.13
+ __27-[_PSProximityBooster init]_block_invoke.13.cold.1
+ __27-[_PSProximityBooster init]_block_invoke.16
+ __27-[_PSProximityBooster init]_block_invoke.16.cold.1
+ __27-[_PSProximityBooster init]_block_invoke.21
+ __27-[_PSProximityBooster init]_block_invoke.21.cold.1
+ __27-[_PSProximityBooster init]_block_invoke.25
+ __27-[_PSProximityBooster init]_block_invoke.25.cold.1
+ __37-[_PSFamilyMLPredictionTask execute:]_block_invoke.20
+ __37-[_PSFamilyMLPredictionTask execute:]_block_invoke.8
+ __37-[_PSFeatureCache saveToVirtualStore]_block_invoke.235
+ __37-[_PSFeatureCache saveToVirtualStore]_block_invoke.235.cold.1
+ __39-[_PSSuggester rankedFamilySuggestions]_block_invoke.386
+ __46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.227
+ __46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.227.cold.1
+ __46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.231
+ __47-[_PSSuggester suggestInteractionsFromContext:]_block_invoke.250
+ __48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.365
+ __48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.366
+ __49-[_PSCoreMLScoringModel featureOrderFromMetadata]_block_invoke.cold.1
+ __50-[_PSEnsembleModel candidatesForShareSheetRanking]_block_invoke.963
+ __50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.1014
+ __50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.1024
+ __50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.1024.cold.1
+ __53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.341
+ __54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.295
+ __54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.302
+ __54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.cold.1
+ __54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.201
+ __54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.205
+ __54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.209
+ __54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_2.213
+ __54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.356
+ __56+[AeroMLTracerSession logChannelWithSubsystem:category:]_block_invoke.11
+ __56+[AeroMLTracerSession logChannelWithSubsystem:category:]_block_invoke.11.cold.1
+ __56-[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:]_block_invoke.140
+ __57-[_PSBlockedHandlesCache rebuildCacheWithBlockedHandles:]_block_invoke.33
+ __57-[_PSEnsembleModel populateCachesWithSupportedBundleIDs:]_block_invoke.515
+ __57-[_PSEnsembleModel populateCachesWithSupportedBundleIDs:]_block_invoke.545
+ __58-[_PSContactSuggester contactPriorsForContactIdentifiers:]_block_invoke.284
+ __58-[_PSContactSuggester contactPriorsForContactIdentifiers:]_block_invoke.289
+ __59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.564
+ __59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.565
+ __59-[_PSFeatureDictionary addEntriesFromDictionary:overwrite:]_block_invoke.cold.1
+ __61-[_PSMessagesPinningSuggester submitMessagesPinningFeedback:]_block_invoke.266
+ __62-[_PSProximityBooster suggestionsByBoostingNearbySuggestions:]_block_invoke.38
+ __62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.609
+ __62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.609.cold.1
+ __63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.377
+ __63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.377.cold.1
+ __63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.380
+ __64-[_PSContactSuggesterForPeopleWidget familyMemberContactHandles]_block_invoke.38
+ __64-[_PSContactSuggesterForPeopleWidget familyMemberContactHandles]_block_invoke.38.cold.1
+ __64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.359
+ __67-[_PSMediaAnalysisProcessingTask executeTaskWithCompletionHandler:]_block_invoke.404
+ __67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.392
+ __68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.906
+ __68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.383
+ __69-[_PSFTZKWOrchestrator _getDirectSuggestionsWithContext:withTimeout:]_block_invoke.53
+ __69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.389
+ __72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.566
+ __72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.576
+ __72-[_PSSuggester computeShareSheetEphemeralFeaturesWithPredictionContext:]_block_invoke.235
+ __72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.395
+ __73-[_PSContactSuggesterForPeopleWidget interactionBasedRecommendedContacts]_block_invoke.45
+ __73-[_PSInteractionAndContactMonitor initWithInteractionStore:contactStore:]_block_invoke.13
+ __73-[_PSInteractionAndContactMonitor initWithInteractionStore:contactStore:]_block_invoke.15
+ __73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.621
+ __74-[_PSInteractionPredictor trainAtDate:usingCompiledModelURL:andSaveToURL:]_block_invoke.147
+ __74-[_PSInteractionPredictor trainAtDate:usingCompiledModelURL:andSaveToURL:]_block_invoke.147.cold.1
+ __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.529
+ __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.531
+ __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.536
+ __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.539
+ __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.554
+ __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.560
+ __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.566
+ __75-[_PSInteractionsStatisticsFeatureProvider initWithInteractionsStatistics:]_block_invoke.105
+ __75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.401
+ __77-[_PSFTZKWSuggestionsTransformerFactory mapRecipientsToContactsWithUnmapped:]_block_invoke.42
+ __77-[_PSFTZKWSuggestionsTransformerFactory mapRecipientsToContactsWithUnmapped:]_block_invoke.42.cold.1
+ __77-[_PSMessagesPinningSuggester chatGuidsForMessagesPinningWithMaxSuggestions:]_block_invoke.206
+ __77-[_PSShareSheetEphemeralFeatureManager computeFeaturesWithHistogramFeatures:]_block_invoke.189
+ __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.291
+ __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.295
+ __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.314
+ __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.321
+ __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.321.cold.1
+ __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.328
+ __79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.356
+ __79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.356.cold.1
+ __80+[_PSContactSuggester _cascadeContentForPriorsArchive:cascadeContactEnumerator:]_block_invoke.314
+ __80+[_PSFTZKWSuggestionsTransformerFactory getResultsFromTransformers:suggestions:]_block_invoke.64
+ __81-[_PSPersonalizationEvaluation adaptMLModel:withTrainingData:modelConfiguration:]_block_invoke.306
+ __81-[_PSPersonalizationEvaluation adaptMLModel:withTrainingData:modelConfiguration:]_block_invoke.306.cold.1
+ __82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.783
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.633
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.636
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.648
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.718
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.726
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.731
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.731.cold.1
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.744
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.747
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.759
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.733
+ __84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.348
+ __84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.351
+ __84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.352
+ __84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.353
+ __87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.362
+ __88-[_PSContactCache getFaceTimeableHandleForContact:interactionStore:seedRecipientHandle:]_block_invoke.79
+ __88-[_PSContactCache getFaceTimeableHandleForContact:interactionStore:seedRecipientHandle:]_block_invoke.83
+ __88-[_PSContactCache getFaceTimeableHandleForContact:interactionStore:seedRecipientHandle:]_block_invoke.84
+ __89-[_PSEnsembleModel psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:]_block_invoke.561
+ __90+[_PSContactSuggester _filteredContactDictionaryFromCascadeContent:forContactIdentifiers:]_block_invoke.276
+ __91-[_PSContactSuggester contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.184
+ __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.214
+ __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.217
+ __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.221
+ __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.221.cold.1
+ __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.221.cold.2
+ __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.233
+ __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.233.cold.1
+ __96-[_PSSuggester(InteractionInformation) interactionCountForHandle:fetchLimit:interactionStoreDB:]_block_invoke.300
+ __98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.80
+ __98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.82
+ __99-[_PSKNNModel rankedCoRecipientSuggestionsWithPredictionContext:modelConfiguration:maxSuggestions:]_block_invoke.388
+ __Block_byref_object_copy_.289
+ __Block_byref_object_dispose_.290
+ __OBJC_$_CLASS_METHODS__PSPETMessageBuilder
+ __OBJC_$_INSTANCE_METHODS_PeopleSuggesterPhotoFeatures
+ __OBJC_$_INSTANCE_VARIABLES_PeopleSuggesterPhotoFeatures
+ __OBJC_$_PROP_LIST_PeopleSuggesterPhotoFeatures
+ __OBJC_CLASS_PROTOCOLS_$_PeopleSuggesterPhotoFeatures
+ __OBJC_CLASS_RO_$_PeopleSuggesterPhotoFeatures
+ __OBJC_METACLASS_RO_$_PeopleSuggesterPhotoFeatures
+ ___105+[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:]_block_invoke
+ ___132-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:]_block_invoke
+ ___37-[_PSTrialClient scenesBasedFeatures]_block_invoke
+ ___52-[_PSEnsembleModel getReasonTypesFromObjects:limit:]_block_invoke
+ ___62-[_PSHeuristics peopleAwareSuggestionProxiesForDetectedFaces:]_block_invoke
+ ___89-[_PSEnsembleModel psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:]_block_invoke
+ ___92-[_PSEnsembleModel enrichConfig:withInformationFromPredictionContext:andAppToAppExtMapping:]_block_invoke
+ ___PSShareSheetSuggestionBundleIDMapping_block_invoke.203
+ ___SiriEntityMatcherLibraryCore_block_invoke
+ ___block_descriptor_32_e18_"NSString"16?08l
+ ___block_descriptor_32_e52_"NSMutableArray"24?0"NSMutableArray"8"NSArray"16l
+ ___block_descriptor_40_e8_32s_e18_16?0"NSString"8l
+ ___block_descriptor_40_e8_32s_e37_"NSArray"16?0"SEMSpanMatchResult"8l
+ ___block_descriptor_40_e8_32s_e59_"_PSContactPrior"16?0"CCItemMessage<CCItemMetaContent>"8l
+ ___block_descriptor_56_e8_32s40s_e18_B16?0"NSString"8l
+ ___block_descriptor_60_e8_32s40s48s_e41_"_PSSuggestionProxy"24?0"NSString"8Q16l
+ ___block_descriptor_64_e8_32s40s48s_e41_"_PSSuggestionProxy"24?0"NSString"8Q16l
+ ___block_descriptor_88_e8_32s40s48s56s64bs72bs80r_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56s64b72b80r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r
+ ___getSEMCascadeEntityFieldInfoClass_block_invoke
+ ___getSEMCascadeEntityInfoClass_block_invoke
+ ___getSEMCascadeItemTypeFilterClass_block_invoke
+ ___getSEMSpanMatchQueryBuilderClass_block_invoke
+ ___getSEMSpanMatcherClass_block_invoke
+ __block_literal_global.10
+ __block_literal_global.1017
+ __block_literal_global.1067
+ __block_literal_global.135
+ __block_literal_global.142
+ __block_literal_global.144
+ __block_literal_global.146
+ __block_literal_global.149
+ __block_literal_global.151
+ __block_literal_global.19
+ __block_literal_global.212
+ __block_literal_global.213
+ __block_literal_global.216
+ __block_literal_global.219
+ __block_literal_global.22
+ __block_literal_global.230
+ __block_literal_global.234
+ __block_literal_global.237
+ __block_literal_global.239
+ __block_literal_global.249
+ __block_literal_global.25
+ __block_literal_global.253
+ __block_literal_global.259
+ __block_literal_global.265
+ __block_literal_global.267
+ __block_literal_global.274
+ __block_literal_global.28
+ __block_literal_global.304
+ __block_literal_global.305
+ __block_literal_global.31
+ __block_literal_global.317
+ __block_literal_global.324
+ __block_literal_global.326
+ __block_literal_global.328
+ __block_literal_global.34
+ __block_literal_global.340
+ __block_literal_global.347
+ __block_literal_global.35
+ __block_literal_global.355
+ __block_literal_global.358
+ __block_literal_global.361
+ __block_literal_global.364
+ __block_literal_global.368
+ __block_literal_global.37
+ __block_literal_global.375
+ __block_literal_global.379
+ __block_literal_global.382
+ __block_literal_global.385
+ __block_literal_global.39
+ __block_literal_global.391
+ __block_literal_global.394
+ __block_literal_global.398
+ __block_literal_global.40
+ __block_literal_global.400
+ __block_literal_global.434
+ __block_literal_global.436
+ __block_literal_global.44
+ __block_literal_global.464
+ __block_literal_global.495
+ __block_literal_global.500
+ __block_literal_global.502
+ __block_literal_global.507
+ __block_literal_global.516
+ __block_literal_global.533
+ __block_literal_global.534
+ __block_literal_global.538
+ __block_literal_global.54
+ __block_literal_global.541
+ __block_literal_global.55
+ __block_literal_global.557
+ __block_literal_global.563
+ __block_literal_global.567
+ __block_literal_global.57
+ __block_literal_global.579
+ __block_literal_global.583
+ __block_literal_global.59
+ __block_literal_global.608
+ __block_literal_global.617
+ __block_literal_global.62
+ __block_literal_global.620
+ __block_literal_global.625
+ __block_literal_global.638
+ __block_literal_global.64
+ __block_literal_global.66
+ __block_literal_global.7
+ __block_literal_global.74
+ __block_literal_global.746
+ __block_literal_global.76
+ __block_literal_global.764
+ __block_literal_global.800
+ __block_literal_global.835
+ __block_literal_global.949
+ __block_literal_global.952
+ __block_literal_global.98
+ _audit_stringSiriEntityMatcher
+ _getSEMCascadeEntityFieldInfoClass
+ _getSEMCascadeEntityInfoClass
+ _objc_msgSend$addPhotoFeatures:
+ _objc_msgSend$addTypeOfContent:
+ _objc_msgSend$allMetaContent
+ _objc_msgSend$build
+ _objc_msgSend$caseInsensitiveCompare:
+ _objc_msgSend$clearPhotoFeatures
+ _objc_msgSend$clearTypeOfContents
+ _objc_msgSend$computeCandidateLevelSignals
+ _objc_msgSend$computeSASSFeatureWithScenesDetectedInPhoto:andConfiguredScenes:
+ _objc_msgSend$contactIdentifiers
+ _objc_msgSend$contentTypeFromUTI:
+ _objc_msgSend$currentConnection
+ _objc_msgSend$currentLocale
+ _objc_msgSend$enrichConfig:withInformationFromPredictionContext:andAppToAppExtMapping:
+ _objc_msgSend$entityFieldInfo
+ _objc_msgSend$entityInfo
+ _objc_msgSend$entityType
+ _objc_msgSend$fieldMatches
+ _objc_msgSend$fieldType
+ _objc_msgSend$getReasonTypesFromObjects:
+ _objc_msgSend$getReasonTypesFromObjects:limit:
+ _objc_msgSend$hyperRecentCallHeuristicSuggestionProxiesForInteractionStatistics:
+ _objc_msgSend$hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:
+ _objc_msgSend$indexMatcher
+ _objc_msgSend$initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:
+ _objc_msgSend$initWithBundleID:interactionRecipients:contactID:handle:reason:reasonType:useGroupsWhenFindingRecipient:
+ _objc_msgSend$initWithItemType:error:
+ _objc_msgSend$initWithLocale:originalText:
+ _objc_msgSend$itemType
+ _objc_msgSend$matchSpans:error:
+ _objc_msgSend$maxNumberOfSuggestionSlotsForHeuristic:
+ _objc_msgSend$mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:
+ _objc_msgSend$peopleAwareSuggestionProxiesForDetectedFaces:
+ _objc_msgSend$peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:
+ _objc_msgSend$phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:
+ _objc_msgSend$photoFeaturesAtIndex:
+ _objc_msgSend$photoFeaturesCount
+ _objc_msgSend$processIdentifier
+ _objc_msgSend$psHeuristicsOverrides
+ _objc_msgSend$pslRecencyMargin
+ _objc_msgSend$psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:
+ _objc_msgSend$recencyMarginInSecondsForHeuristic:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$reportShareSheetTimeoutWithReply:
+ _objc_msgSend$scenesBasedFeatures
+ _objc_msgSend$scenesBasedFeaturesAwareSuggestionProxiesForInteractionStatistics:forFeatureNames:
+ _objc_msgSend$scenesBasedFeaturesNames
+ _objc_msgSend$scenesMinimumNumberOfTags
+ _objc_msgSend$setAppToAppExtMapping:
+ _objc_msgSend$setEntityFilters:
+ _objc_msgSend$setHasSharedSensitiveContentWIthConversation:
+ _objc_msgSend$setIsFirstPartyApp:
+ _objc_msgSend$setNumberOfAppsSharedFromWithConversation:
+ _objc_msgSend$setNumberOfDifferentFacesSharedWithConversation:
+ _objc_msgSend$setNumberOfSharesFromAlbumPhotoBelongsToWithConversation:
+ _objc_msgSend$setNumberOfSharesOfDetectedScenesInPhotoWithConversation:
+ _objc_msgSend$setNumberOfSharesOfPeopleInPhotoIoUWithConversation:
+ _objc_msgSend$setNumberOfSharesOfPetsInCurrentPhotoWithConversation:
+ _objc_msgSend$setNumberOfSharesOfPetsWithConversation:
+ _objc_msgSend$setNumberOfSharesOfScenesInPhotoWithConversation:
+ _objc_msgSend$setNumberOfTimesSharedToTargetAppWithConversation:
+ _objc_msgSend$setNumberOfTopicsSharedWithConversation:
+ _objc_msgSend$setNumberOfTotalSharesToTargetApp:
+ _objc_msgSend$setPslRecencyMargin:
+ _objc_msgSend$setTimeSinceLastPhoneCallWithConversation:
+ _objc_msgSend$setTimeSinceLastPhotoShareWithConversation:
+ _objc_msgSend$setTimeSinceLastShare:
+ _objc_msgSend$setTimeSinceLastShareWithConversation:
+ _objc_msgSend$shouldProcessPicturesLive
+ _objc_msgSend$thresholdForHeuristic:
+ _objc_msgSend$topLevelScenesFromSceneNetTags:
+ _objc_msgSend$typeOfContentAtIndex:
+ _objc_msgSend$typeOfContentsCount
+ _objc_msgSend$updateHeuristicParameterOverrides:
+ _objc_msgSend$valueForHeuristic:parameter:
+ _objc_msgSend$visualIdentifierViewWithError:
+ _suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken173
+ asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:._pasOnceToken74
+ autocompleteSearchResultsWithPredictionContext:._pasOnceToken107
+ getSEMCascadeEntityFieldInfoClass.softClass
+ getSEMCascadeEntityInfoClass.softClass
+ getSEMCascadeItemTypeFilterClass.softClass
+ getSEMSpanMatchQueryBuilderClass.softClass
+ getSEMSpanMatcherClass.softClass
+ rankedZKWSuggestionsFromContext:._pasOnceToken105
- +[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:]
- +[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldUseMDID:withCompletion:]
- +[_PSPhotoSuggestions phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:withCompletion:]
- -[_PSEnsembleModel enrichConfig:withInformationFromPredictionContext:]
- -[_PSEnsembleModel psr_getPhotoBasedFeaturesAsync:withTimeout:]
- -[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:]
- -[_PSHeuristics recencyMargin]
- -[_PSHeuristics setRecencyMargin:]
- CoreDuetFrameworkLibraryCore.frameworkLibrary
- CoreKnowledgeLibraryCore.frameworkLibrary
- GCC_except_table102
- GCC_except_table105
- GCC_except_table108
- GCC_except_table126
- GCC_except_table151
- GCC_except_table172
- GCC_except_table288
- GCC_except_table290
- GCC_except_table41
- GCC_except_table68
- GCC_except_table72
- GCC_except_table75
- GCC_except_table78
- GCC_except_table81
- GCC_except_table82
- GCC_except_table85
- GCC_except_table89
- GCC_except_table95
- GCC_except_table96
- GCC_except_table99
- OBJC_IVAR_$__PSHeuristics._recencyMargin
- _CoreKnowledgeLibraryCore
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.969
- __105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.978
- __106-[_PSContactSuggesterForPeopleWidget contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.42
- __106-[_PSContactSuggesterForPeopleWidget contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.45
- __108-[_PSHeuristics heuristicsFromInteractionsStatistics:forStatsNames:threshold:maxNumberOfSuggestions:reason:]_block_invoke.239
- __108-[_PSHeuristics heuristicsFromInteractionsStatistics:forStatsNames:threshold:maxNumberOfSuggestions:reason:]_block_invoke.241
- __108-[_PSHeuristics heuristicsFromInteractionsStatistics:forStatsNames:threshold:maxNumberOfSuggestions:reason:]_block_invoke.244
- __118-[_PSSuggestionFromTextPredictor suggestionsFromIncompleteRemindersWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.84
- __120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.875
- __125-[_PSSuggestionFromTextPredictor suggestionsFromUnstructuredCalendarEventsWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.102
- __126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.785
- __126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.785.cold.1
- __150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.166
- __150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.173
- __163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke.49
- __23-[_PSContactCache init]_block_invoke.39
- __23-[_PSContactCache init]_block_invoke.42
- __27-[_PSProximityBooster init]_block_invoke.10
- __27-[_PSProximityBooster init]_block_invoke.10.cold.1
- __27-[_PSProximityBooster init]_block_invoke.15
- __27-[_PSProximityBooster init]_block_invoke.15.cold.1
- __27-[_PSProximityBooster init]_block_invoke.19
- __27-[_PSProximityBooster init]_block_invoke.19.cold.1
- __27-[_PSProximityBooster init]_block_invoke.7
- __27-[_PSProximityBooster init]_block_invoke.7.cold.1
- __37-[_PSFamilyMLPredictionTask execute:]_block_invoke.14
- __37-[_PSFamilyMLPredictionTask execute:]_block_invoke.4
- __37-[_PSFeatureCache saveToVirtualStore]_block_invoke.187
- __37-[_PSFeatureCache saveToVirtualStore]_block_invoke.187.cold.1
- __39-[_PSSuggester rankedFamilySuggestions]_block_invoke.334
- __46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.178
- __46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.178.cold.1
- __46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.182
- __47-[_PSSuggester suggestInteractionsFromContext:]_block_invoke.202
- __48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.313
- __48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.314
- __50-[_PSEnsembleModel candidatesForShareSheetRanking]_block_invoke.901
- __50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.952
- __50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.962
- __50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.962.cold.1
- __53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.289
- __54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.249
- __54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.153
- __54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.157
- __54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.161
- __54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_2.165
- __54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.304
- __56+[AeroMLTracerSession logChannelWithSubsystem:category:]_block_invoke.5
- __56+[AeroMLTracerSession logChannelWithSubsystem:category:]_block_invoke.5.cold.1
- __56-[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:]_block_invoke.134
- __57-[_PSBlockedHandlesCache rebuildCacheWithBlockedHandles:]_block_invoke.27
- __57-[_PSEnsembleModel populateCachesWithSupportedBundleIDs:]_block_invoke.467
- __57-[_PSEnsembleModel populateCachesWithSupportedBundleIDs:]_block_invoke.497
- __58-[_PSContactSuggester contactPriorsForContactIdentifiers:]_block_invoke.236
- __58-[_PSContactSuggester contactPriorsForContactIdentifiers:]_block_invoke.241
- __59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.516
- __59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.517
- __61-[_PSMessagesPinningSuggester submitMessagesPinningFeedback:]_block_invoke.224
- __62-[_PSProximityBooster suggestionsByBoostingNearbySuggestions:]_block_invoke.32
- __62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.557
- __62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.557.cold.1
- __63-[_PSEnsembleModel psr_getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.513
- __63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.325
- __63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.325.cold.1
- __63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.328
- __64-[_PSContactSuggesterForPeopleWidget familyMemberContactHandles]_block_invoke.32
- __64-[_PSContactSuggesterForPeopleWidget familyMemberContactHandles]_block_invoke.32.cold.1
- __64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.307
- __67-[_PSMediaAnalysisProcessingTask executeTaskWithCompletionHandler:]_block_invoke.356
- __67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.340
- __68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.844
- __68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.331
- __69-[_PSFTZKWOrchestrator _getDirectSuggestionsWithContext:withTimeout:]_block_invoke.47
- __69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.337
- __72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.514
- __72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.524
- __72-[_PSSuggester computeShareSheetEphemeralFeaturesWithPredictionContext:]_block_invoke.186
- __72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.343
- __73-[_PSContactSuggesterForPeopleWidget interactionBasedRecommendedContacts]_block_invoke.39
- __73-[_PSInteractionAndContactMonitor initWithInteractionStore:contactStore:]_block_invoke.7
- __73-[_PSInteractionAndContactMonitor initWithInteractionStore:contactStore:]_block_invoke.9
- __73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.569
- __74-[_PSInteractionPredictor trainAtDate:usingCompiledModelURL:andSaveToURL:]_block_invoke.141
- __74-[_PSInteractionPredictor trainAtDate:usingCompiledModelURL:andSaveToURL:]_block_invoke.141.cold.1
- __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.481
- __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.483
- __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.488
- __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.491
- __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.506
- __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.512
- __75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.518
- __75-[_PSInteractionsStatisticsFeatureProvider initWithInteractionsStatistics:]_block_invoke.102
- __75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.349
- __77-[_PSFTZKWSuggestionsTransformerFactory mapRecipientsToContactsWithUnmapped:]_block_invoke.36
- __77-[_PSFTZKWSuggestionsTransformerFactory mapRecipientsToContactsWithUnmapped:]_block_invoke.36.cold.1
- __77-[_PSMessagesPinningSuggester chatGuidsForMessagesPinningWithMaxSuggestions:]_block_invoke.164
- __77-[_PSShareSheetEphemeralFeatureManager computeFeaturesWithHistogramFeatures:]_block_invoke.141
- __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.243
- __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.247
- __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.266
- __78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.276
- __79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.308
- __79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.308.cold.1
- __80+[_PSContactSuggester _cascadeContentForPriorsArchive:cascadeContactEnumerator:]_block_invoke.263
- __80+[_PSFTZKWSuggestionsTransformerFactory getResultsFromTransformers:suggestions:]_block_invoke.58
- __81-[_PSPersonalizationEvaluation adaptMLModel:withTrainingData:modelConfiguration:]_block_invoke.300
- __81-[_PSPersonalizationEvaluation adaptMLModel:withTrainingData:modelConfiguration:]_block_invoke.300.cold.1
- __82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.724
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.585
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.588
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.600
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.673
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.681
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.686
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.686.cold.1
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.699
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.702
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.714
- __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.688
- __84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.296
- __84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.299
- __84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.300
- __84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.301
- __87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.310
- __88-[_PSContactCache getFaceTimeableHandleForContact:interactionStore:seedRecipientHandle:]_block_invoke.73
- __88-[_PSContactCache getFaceTimeableHandleForContact:interactionStore:seedRecipientHandle:]_block_invoke.77
- __88-[_PSContactCache getFaceTimeableHandleForContact:interactionStore:seedRecipientHandle:]_block_invoke.78
- __90+[_PSContactSuggester _filteredContactDictionaryFromCascadeContent:forContactIdentifiers:]_block_invoke.228
- __91-[_PSContactSuggester contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.136
- __91-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:]_block_invoke.213
- __91-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:]_block_invoke.215
- __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.166
- __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.169
- __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.173
- __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.173.cold.1
- __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.173.cold.2
- __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.185
- __96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.185.cold.1
- __96-[_PSSuggester(InteractionInformation) interactionCountForHandle:fetchLimit:interactionStoreDB:]_block_invoke.252
- __98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.74
- __98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.76
- __99-[_PSKNNModel rankedCoRecipientSuggestionsWithPredictionContext:modelConfiguration:maxSuggestions:]_block_invoke.340
- __Block_byref_object_copy_.241
- __Block_byref_object_dispose_.242
- ___63-[_PSEnsembleModel psr_getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke
- ___70-[_PSEnsembleModel enrichConfig:withInformationFromPredictionContext:]_block_invoke
- ___79+[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:]_block_invoke
- ___91-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:]_block_invoke
- ___CoreDuetFrameworkLibraryCore_block_invoke
- ___CoreKnowledgeLibraryCore_block_invoke
- ___PSShareSheetSuggestionBundleIDMapping_block_invoke.155
- ___block_descriptor_56_e8_32s40s48s_e18_B16?0"NSString"8l
- ___block_descriptor_56_e8_32s40s48s_e38_"_PSSuggestionProxy"16?0"NSString"8l
- ___block_descriptor_80_e8_32s40s48s56bs64bs72r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56b64b72r
- ___getCKVAppIdContactsSymbolLoc_block_invoke
- ___getCKVocabularySearcherClass_block_invoke
- ___get_CDInteractionsStatisticsConfigClass_block_invoke
- __block_literal_global.12
- __block_literal_global.129
- __block_literal_global.136
- __block_literal_global.138
- __block_literal_global.140
- __block_literal_global.143
- __block_literal_global.145
- __block_literal_global.152
- __block_literal_global.164
- __block_literal_global.165
- __block_literal_global.168
- __block_literal_global.171
- __block_literal_global.177
- __block_literal_global.18
- __block_literal_global.181
- __block_literal_global.185
- __block_literal_global.189
- __block_literal_global.191
- __block_literal_global.205
- __block_literal_global.21
- __block_literal_global.211
- __block_literal_global.217
- __block_literal_global.251
- __block_literal_global.256
- __block_literal_global.261
- __block_literal_global.266
- __block_literal_global.275
- __block_literal_global.277
- __block_literal_global.288
- __block_literal_global.29
- __block_literal_global.295
- __block_literal_global.298
- __block_literal_global.3
- __block_literal_global.303
- __block_literal_global.306
- __block_literal_global.309
- __block_literal_global.312
- __block_literal_global.316
- __block_literal_global.323
- __block_literal_global.327
- __block_literal_global.33
- __block_literal_global.330
- __block_literal_global.333
- __block_literal_global.336
- __block_literal_global.339
- __block_literal_global.342
- __block_literal_global.348
- __block_literal_global.36
- __block_literal_global.38
- __block_literal_global.386
- __block_literal_global.41
- __block_literal_global.416
- __block_literal_global.43
- __block_literal_global.447
- __block_literal_global.452
- __block_literal_global.454
- __block_literal_global.459
- __block_literal_global.461
- __block_literal_global.468
- __block_literal_global.48
- __block_literal_global.485
- __block_literal_global.486
- __block_literal_global.490
- __block_literal_global.493
- __block_literal_global.51
- __block_literal_global.511
- __block_literal_global.515
- __block_literal_global.517
- __block_literal_global.519
- __block_literal_global.520
- __block_literal_global.527
- __block_literal_global.529
- __block_literal_global.531
- __block_literal_global.556
- __block_literal_global.56
- __block_literal_global.58
- __block_literal_global.590
- __block_literal_global.6
- __block_literal_global.60
- __block_literal_global.68
- __block_literal_global.70
- __block_literal_global.701
- __block_literal_global.741
- __block_literal_global.776
- __block_literal_global.887
- __block_literal_global.890
- __block_literal_global.9
- __block_literal_global.92
- __block_literal_global.955
- __block_literal_global.996
- _audit_stringCoreDuetFramework
- _audit_stringCoreKnowledge
- _fmod
- _objc_msgSend$enrichConfig:withInformationFromPredictionContext:
- _objc_msgSend$hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:
- _objc_msgSend$initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldSortAscending:shouldUseSuggestionEngaged:statsDefaultValues:
- _objc_msgSend$itemId
- _objc_msgSend$makeSearcher
- _objc_msgSend$matchSpansOfString:
- _objc_msgSend$mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:
- _objc_msgSend$ontologyLabel
- _objc_msgSend$ordinality
- _objc_msgSend$originAppId
- _objc_msgSend$peopleInSharedPhotoAttachments:forBundleID:shouldUseMDID:withCompletion:
- _objc_msgSend$phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:withCompletion:
- _objc_msgSend$priorInfo
- _objc_msgSend$psr_getPhotoBasedFeaturesAsync:withTimeout:
- _objc_msgSend$recencyMargin
- _objc_msgSend$setRecencyMargin:
- _objc_msgSend$setShouldSortAscending:
- _strcmp
- _suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken171
- asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:._pasOnceToken71
- autocompleteSearchResultsWithPredictionContext:._pasOnceToken104
- getCKVAppIdContactsSymbolLoc.ptr
- getCKVocabularySearcherClass.softClass
- get_CDInteractionsStatisticsConfigClass.softClass
- rankedZKWSuggestionsFromContext:._pasOnceToken102
CStrings:
+ "%td"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/PFL/LighthouseShareSheetPFLTraining.m"
+ "/AppleInternal/Library/BuildRoots/1f0f0a2e-ff28-11ef-9d15-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
+ "/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/Contents/MacOS/SiriEntityMatcher"
+ "1269"
+ "15"
+ "16634"
+ "898"
+ "::"
+ "@\"NSArray\"16@?0@\"SEMSpanMatchResult\"8"
+ "@\"NSMutableArray\"24@?0@\"NSMutableArray\"8@\"NSArray\"16"
+ "@\"NSString\"16@?0@8"
+ "@\"_PSContactPrior\"16@?0@\"CCItemMessage<CCItemMetaContent>\"8"
+ "@\"_PSSuggestionProxy\"24@?0@\"NSString\"8Q16"
+ "@48@0:8@16@24q32q40"
+ "@60@0:8@16@24B32@36@44@?52"
+ "@64@0:8@16@24B32@36@44B52@?56"
+ "@?36@0:8@16B24d28"
+ "B24@0:8^@16"
+ "CoreDuet: App Suggestions"
+ "CoreDuet: Candidates for Share Sheet Ranking"
+ "CoreDuet: Share Sheet Suggestions"
+ "CoreDuet: _PSContactSuggester Prior Generation"
+ "Error getting IntelligencePlatform visualIdentifierView: %@"
+ "Error making item type filter: %@"
+ "Failed to report timeout to DiagnosticRequest: %{public}@"
+ "For text %{private}@ found spans %{private}@"
+ "For text %{private}@ got %{public}@ when %{public}@ was expected"
+ "For text %{private}@ got SEMSpanMatcher error %@"
+ "For text %{private}@ outputting contact identifier %{private}@"
+ "Heuristics config: %@"
+ "LIVE_PHOTO"
+ "No config found for heuristic: %@"
+ "No recency margin found for heuristic: %@"
+ "No slot limit found for heuristic: %@"
+ "No threshold found for heuristic: %@"
+ "PASS heuristic v1 - PS Rewrite"
+ "PASS heuristic v2 - PS Rewrite"
+ "PDF"
+ "PUBLIC_FILE_URL"
+ "PUBLIC_HEIC"
+ "PUBLIC_IMAGE"
+ "PUBLIC_JPEG"
+ "PUBLIC_MOVIE"
+ "PUBLIC_MPEG4"
+ "PUBLIC_PLAIN_TEXT"
+ "PUBLIC_PNG"
+ "PUBLIC_URL"
+ "PUBLIC_VCARD"
+ "PeopleSuggesterPhotoFeatures"
+ "Pruning all candidates that the user never sent a message to nor recently engaged with in the sharing UI."
+ "QUICKTIME_MOVIE"
+ "Reported timeout successfully to DiagnosticRequest"
+ "ResolvedContactIDsFromMD_count"
+ "SASS heuristic - PS Rewrite"
+ "SELF != nil"
+ "SEMCascadeEntityFieldInfo"
+ "SEMCascadeEntityInfo"
+ "SEMCascadeItemTypeFilter"
+ "SEMSpanMatchQueryBuilder"
+ "SEMSpanMatcher"
+ "StringAsTypeOfContents:"
+ "SuggestionProxyTypeHyperRecencyCallRewrite"
+ "SuggestionProxyTypePASSv1"
+ "SuggestionProxyTypeSASS"
+ "T@\"NSMutableArray\",&,N,V_photoFeatures"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_hasSharedSensitiveContentWIthConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfAppsSharedFromWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfDifferentFacesSharedWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfSharesFromAlbumPhotoBelongsToWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfSharesOfDetectedScenesInPhotoWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfSharesOfPeopleInPhotoIoUWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfSharesOfPetsInCurrentPhotoWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfSharesOfPetsWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfSharesOfScenesInPhotoWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfTimesSharedToTargetAppWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfTopicsSharedWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_numberOfTotalSharesToTargetApp"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_timeSinceLastPhoneCallWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_timeSinceLastPhotoShareWithConversation"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_timeSinceLastShare"
+ "T@\"PeopleSuggesterFeatureDouble\",&,N,V_timeSinceLastShareWithConversation"
+ "TB,N,V_isFavorited"
+ "TB,N,V_isFirstPartyApp"
+ "TB,N,V_isInPhoneCall"
+ "TB,N,V_isInPhoneCallWithConversation"
+ "TB,N,V_isScreenShot"
+ "T^i,R,N"
+ "Td,N,V_pslRecencyMargin"
+ "TimeSinceLastUIEngagement"
+ "UNKNOWN"
+ "Updating suggestion conversationIdentifier(%{private}@) since groupName(%{private}@) changed: %{BOOL}d or participants changed: %{BOOL}d"
+ "Using override for heuristic %{public}@, parameter %{public}@: %{public}@"
+ "^i16@0:8"
+ "_PSHeuristicsOverrides"
+ "_PSHeuristicsPSLBackfillLimit"
+ "_PSHeuristicsPSLMessagesRecencyLimit"
+ "_PSHeuristicsPSLRecencyMargin"
+ "_PSHeuristicsPSLShareSheetRecencyLimit"
+ "_PSTrialClient: Final configuration is: timeInterval %f, fetchLimit %lu,  maxComputationTimeInSeconds %.2f, featureNamesToSortWith %@, shouldUseSuggestionEngaged %@, statsDefaultValues %@"
+ "_configOverrides"
+ "_hasSharedSensitiveContentWIthConversation"
+ "_isFavorited"
+ "_isFirstPartyApp"
+ "_isInPhoneCall"
+ "_isInPhoneCallWithConversation"
+ "_isScreenShot"
+ "_numberOfAppsSharedFromWithConversation"
+ "_numberOfDifferentFacesSharedWithConversation"
+ "_numberOfSharesFromAlbumPhotoBelongsToWithConversation"
+ "_numberOfSharesOfDetectedScenesInPhotoWithConversation"
+ "_numberOfSharesOfPeopleInPhotoIoUWithConversation"
+ "_numberOfSharesOfPetsInCurrentPhotoWithConversation"
+ "_numberOfSharesOfPetsWithConversation"
+ "_numberOfSharesOfScenesInPhotoWithConversation"
+ "_numberOfTimesSharedToTargetAppWithConversation"
+ "_numberOfTopicsSharedWithConversation"
+ "_numberOfTotalSharesToTargetApp"
+ "_photoFeatures"
+ "_pslRecencyMargin"
+ "_timeSinceLastPhoneCallWithConversation"
+ "_timeSinceLastPhotoShareWithConversation"
+ "_timeSinceLastShare"
+ "_timeSinceLastShareWithConversation"
+ "_typeOfContents"
+ "addPhotoFeatures:"
+ "addTypeOfContent:"
+ "allMetaContent"
+ "build"
+ "clearPhotoFeatures"
+ "clearTypeOfContents"
+ "com.adobe.pdf"
+ "com.apple.live-photo"
+ "com.apple.quicktime-movie"
+ "computeCandidateLevelSignals"
+ "computeSASSFeatureWithScenesDetectedInPhoto:andConfiguredScenes:"
+ "conditioned_featureCountFor_food"
+ "conditioned_featureCountFor_music"
+ "conditioned_featureCountFor_pet"
+ "conditioned_featureCountFor_sport"
+ "contactIdentifiers"
+ "contentTypeFromUTI:"
+ "currentConnection"
+ "currentLocale"
+ "enrichConfig:withInformationFromPredictionContext:andAppToAppExtMapping:"
+ "entityFieldInfo"
+ "entityInfo"
+ "entityType"
+ "featureCountFor_food"
+ "featureCountFor_music"
+ "featureCountFor_pet"
+ "featureCountFor_sport"
+ "fieldMatches"
+ "fieldType"
+ "getReasonTypesFromObjects:"
+ "getReasonTypesFromObjects:limit:"
+ "hasHasSharedSensitiveContentWIthConversation"
+ "hasIsFavorited"
+ "hasIsFirstPartyApp"
+ "hasIsInPhoneCall"
+ "hasIsInPhoneCallWithConversation"
+ "hasIsScreenShot"
+ "hasNumberOfAppsSharedFromWithConversation"
+ "hasNumberOfDifferentFacesSharedWithConversation"
+ "hasNumberOfSharesFromAlbumPhotoBelongsToWithConversation"
+ "hasNumberOfSharesOfDetectedScenesInPhotoWithConversation"
+ "hasNumberOfSharesOfPeopleInPhotoIoUWithConversation"
+ "hasNumberOfSharesOfPetsInCurrentPhotoWithConversation"
+ "hasNumberOfSharesOfPetsWithConversation"
+ "hasNumberOfSharesOfScenesInPhotoWithConversation"
+ "hasNumberOfTimesSharedToTargetAppWithConversation"
+ "hasNumberOfTopicsSharedWithConversation"
+ "hasNumberOfTotalSharesToTargetApp"
+ "hasSharedSensitiveContentWIthConversation"
+ "hasTimeSinceLastPhoneCallWithConversation"
+ "hasTimeSinceLastPhotoShareWithConversation"
+ "hasTimeSinceLastShare"
+ "hasTimeSinceLastShareWithConversation"
+ "hyperRecentCallHeuristicSuggestionProxiesForInteractionStatistics:"
+ "hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:"
+ "i24@0:8Q16"
+ "idx (%lu) is out of range (%lu)"
+ "indexMatcher"
+ "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldUseSuggestionEngaged:statsDefaultValues:scenesBasedFeatures:scenesMinimumNumberOfTags:"
+ "initWithItemType:error:"
+ "initWithLocale:originalText:"
+ "isFavorited"
+ "isFirstPartyApp"
+ "isInPhoneCall"
+ "isInPhoneCallWithConversation"
+ "isScreenShot"
+ "itemType"
+ "logJointProbabilityScore"
+ "matchSpans:error:"
+ "maxNumberOfSuggestionSlots"
+ "maxNumberOfSuggestionSlotsForHeuristic:"
+ "mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:"
+ "not actually reporting share sheet timeout (requested by pid %{public}@) because that's only supported on iOS"
+ "numberOfAppsSharedFromWithConversation"
+ "numberOfDifferentFacesSharedWithConversation"
+ "numberOfEngagedSuggestionsToTargetApp"
+ "numberOfRecentOutgoingInteractionsWithConversation"
+ "numberOfSharesFromAlbumPhotoBelongsToWithConversation"
+ "numberOfSharesOfDetectedScenesInPhotoWithConversation"
+ "numberOfSharesOfDetectedScenesWithConversation"
+ "numberOfSharesOfPeopleInPhotoIoUWithConversation"
+ "numberOfSharesOfPetsInCurrentPhotoWithConversation"
+ "numberOfSharesOfPetsWithConversation"
+ "numberOfSharesOfScenesInPhotoWithConversation"
+ "numberOfTimesSharedToTargetAppWithConversation"
+ "numberOfTopicsSharedWithConversation"
+ "numberOfTotalSharesToTargetApp"
+ "pCk"
+ "pPASS|Ck"
+ "pRecentInteractions|Ck"
+ "pSource|Ck"
+ "pTopLevelDomain|Ck"
+ "peopleAwareSuggestionProxiesForDetectedFaces:"
+ "peopleInPhotoIdentifiers_count"
+ "peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:"
+ "phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:"
+ "photoFeatures"
+ "photoFeaturesAtIndex:"
+ "photoFeaturesCount"
+ "photoFeaturesType"
+ "processIdentifier"
+ "psHeuristicsOverrides"
+ "pslRecencyMargin"
+ "psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:"
+ "public.heic"
+ "public.movie"
+ "public.mpeg-4"
+ "recencyMarginInSeconds"
+ "recencyMarginInSecondsForHeuristic:"
+ "remoteObjectProxyWithErrorHandler:"
+ "reportShareSheetTimeoutWithError:"
+ "reportShareSheetTimeoutWithReply:"
+ "scenesBasedFeatures"
+ "scenesBasedFeaturesAwareSuggestionProxiesForInteractionStatistics:forFeatureNames:"
+ "scenesBasedFeaturesNames"
+ "scenesMinimumNumberOfTags"
+ "setAppToAppExtMapping:"
+ "setEntityFilters:"
+ "setHasIsFavorited:"
+ "setHasIsFirstPartyApp:"
+ "setHasIsInPhoneCall:"
+ "setHasIsInPhoneCallWithConversation:"
+ "setHasIsScreenShot:"
+ "setHasSharedSensitiveContentWIthConversation:"
+ "setIsFavorited:"
+ "setIsFirstPartyApp:"
+ "setIsInPhoneCall:"
+ "setIsInPhoneCallWithConversation:"
+ "setIsScreenShot:"
+ "setNumberOfAppsSharedFromWithConversation:"
+ "setNumberOfDifferentFacesSharedWithConversation:"
+ "setNumberOfSharesFromAlbumPhotoBelongsToWithConversation:"
+ "setNumberOfSharesOfDetectedScenesInPhotoWithConversation:"
+ "setNumberOfSharesOfPeopleInPhotoIoUWithConversation:"
+ "setNumberOfSharesOfPetsInCurrentPhotoWithConversation:"
+ "setNumberOfSharesOfPetsWithConversation:"
+ "setNumberOfSharesOfScenesInPhotoWithConversation:"
+ "setNumberOfTimesSharedToTargetAppWithConversation:"
+ "setNumberOfTopicsSharedWithConversation:"
+ "setNumberOfTotalSharesToTargetApp:"
+ "setPhotoFeatures:"
+ "setPslRecencyMargin:"
+ "setTimeSinceLastPhoneCallWithConversation:"
+ "setTimeSinceLastPhotoShareWithConversation:"
+ "setTimeSinceLastShare:"
+ "setTimeSinceLastShareWithConversation:"
+ "setTypeOfContents:count:"
+ "shouldProcessPicturesLive"
+ "softlink:o:path:/System/Library/PrivateFrameworks/SiriEntityMatcher.framework/SiriEntityMatcher"
+ "suggestionProxiesReasonTypes: %@"
+ "suggestionProxies_count"
+ "suggestionProxyReasonTypes"
+ "suggestionReasonTypes"
+ "suggestionReasonTypes: %@"
+ "suggestionsProxiesPASSv1Span"
+ "threshold"
+ "thresholdForHeuristic:"
+ "timeSinceLastPhoneCallWithConversation"
+ "timeSinceLastPhotoShareWithConversation"
+ "timeSinceLastShare"
+ "timeSinceLastShareWithConversation"
+ "topLevelScenesFromSceneNetTags:"
+ "typeOfContent"
+ "typeOfContentAtIndex:"
+ "typeOfContents"
+ "typeOfContentsAsString:"
+ "typeOfContentsCount"
+ "updateHeuristicParameterOverrides:"
+ "v32@0:8^i16Q24"
+ "valueForHeuristic:parameter:"
+ "visualIdentifierViewWithError:"
+ "{?=\"appSharedFrom\"b1\"madResponseStatus\"b1\"version\"b1\"isFallbackFetch\"b1\"isInPhoneCall\"b1\"isScreenShot\"b1\"isSharePlayAvailable\"b1}"
+ "{?=\"coreMLModelScore\"b1\"deprecatedField1\"b1\"deprecatedField2\"b1\"deprecatedField3\"b1\"feedbackDeprecated\"b1\"foundInChunk\"b1\"suggestedRank\"b1\"updatedInChunk\"b1\"isFirstPartyApp\"b1\"isInPhoneCallWithConversation\"b1}"
+ "{?=\"isFavorited\"b1\"isScreenShot\"b1}"
+ "{?=\"list\"^i\"count\"Q\"size\"Q}"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/PFL/LighthouseShareSheetPFLTraining.m"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
- "/System/Library/PrivateFrameworks/CoreDuetFramework.framework/Contents/MacOS/CoreDuetFramework"
- "/System/Library/PrivateFrameworks/CoreKnowledge.framework/Contents/MacOS/CoreKnowledge"
- "@\"_PSSuggestionProxy\"16@?0@\"NSString\"8"
- "@44@0:8@16@24B32@?36"
- "CKVAppIdContacts"
- "CKVocabularySearcher"
- "CKVocabularySearcher matchSpansOfString:"
- "Duet: App Suggestions"
- "Duet: Candidates for Share Sheet Ranking"
- "Duet: Share Sheet Suggestions"
- "Duet: _PSContactSuggester Prior Generation"
- "For text %@ found spans %@"
- "P1"
- "P2"
- "P3"
- "P4"
- "PASS heuristic - PS Rewrite"
- "Pruning all candidates that the user never sent a message to."
- "Recency margin: %@."
- "Td,N,V_recencyMargin"
- "Updating suggestion since groupName(%{private}@) changed: %{BOOL}d or participants changed: %{BOOL}d"
- "_CDInteractionsStatisticsConfig"
- "_PSHeuristicsBackfillLimit"
- "_PSHeuristicsMessagesRecencyLimit"
- "_PSHeuristicsRecencyMargin"
- "_PSHeuristicsShareSheetRecencyLimit"
- "_PSTrialClient: Final configuration is: timeInterval %f, fetchLimit %lu, featureNamesToSortWith %@, shouldSortAscending %@, shouldUseSuggestionEngaged %@, statsDefaultValues %@"
- "_recencyMargin"
- "copy:to:"
- "count1"
- "count2"
- "count3"
- "count4"
- "enrichConfig:withInformationFromPredictionContext:"
- "hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:"
- "impute:withConstant:"
- "initWithAnchorDate:leftBoundDate:rightBoundDate:fetchLimit:maxComputationTime:featureNamesToSortWith:shouldSortAscending:shouldUseSuggestionEngaged:statsDefaultValues:"
- "itemId"
- "logJointProbability"
- "logPipelineWithSuggestions"
- "logPipeline_interactionsStatisticsCandidates_with_additional_features"
- "logPipeline_interactionsStatisticsCandidates_with_coreml_output"
- "logPipeline_interactionsStatisticsCandidates_with_photo_based_features"
- "log_P1"
- "log_P2"
- "log_P3"
- "log_P4"
- "makeSearcher"
- "matchSpansOfString:"
- "mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:"
- "ontologyLabel"
- "ordinality"
- "originAppId"
- "partialSum1"
- "partialSum2"
- "pass_data_collection_only"
- "peopleInSharedPhotoAttachments:forBundleID:shouldUseMDID:withCompletion:"
- "personFullName"
- "phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:withCompletion:"
- "priorInfo"
- "psr_getPhotoBasedFeaturesAsync:withTimeout:"
- "recencyMargin"
- "setRecencyMargin:"
- "setShouldSortAscending:"
- "shouldSortAscending"
- "softlink:o:path:/System/Library/PrivateFrameworks/CoreDuetFramework.framework/CoreDuetFramework"
- "softlink:o:path:/System/Library/PrivateFrameworks/CoreKnowledge.framework/CoreKnowledge"
- "{?=\"appSharedFrom\"b1\"madResponseStatus\"b1\"version\"b1\"isFallbackFetch\"b1\"isSharePlayAvailable\"b1}"
- "{?=\"coreMLModelScore\"b1\"deprecatedField1\"b1\"deprecatedField2\"b1\"deprecatedField3\"b1\"feedbackDeprecated\"b1\"foundInChunk\"b1\"suggestedRank\"b1\"updatedInChunk\"b1}"

```
