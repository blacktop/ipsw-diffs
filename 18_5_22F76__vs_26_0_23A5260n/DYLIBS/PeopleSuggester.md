## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1892.22.0.0.0
-  __TEXT.__text: 0x1107c0
+1917.0.1.0.0
+  __TEXT.__text: 0xdf9bc
   __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0xb234
-  __TEXT.__const: 0x738
-  __TEXT.__gcc_except_tab: 0x3768
-  __TEXT.__cstring: 0xb84f
-  __TEXT.__oslogstring: 0xd31d
-  __TEXT.__dlopen_cstrs: 0x1c05
+  __TEXT.__objc_methlist: 0x91fc
+  __TEXT.__const: 0x708
+  __TEXT.__gcc_except_tab: 0x2d4c
+  __TEXT.__cstring: 0x9f4b
+  __TEXT.__oslogstring: 0xab77
+  __TEXT.__dlopen_cstrs: 0x17a6
   __TEXT.__ustring: 0x33e
-  __TEXT.__unwind_info: 0x2ee0
+  __TEXT.__unwind_info: 0x2888
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x1375
-  __TEXT.__objc_methname: 0x25d21
-  __TEXT.__objc_methtype: 0x2c0e
-  __TEXT.__objc_stubs: 0x163e0
-  __DATA_CONST.__got: 0x980
-  __DATA_CONST.__const: 0x3310
-  __DATA_CONST.__objc_classlist: 0x570
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x58
+  __TEXT.__objc_classname: 0x10a4
+  __TEXT.__objc_methname: 0x1f676
+  __TEXT.__objc_methtype: 0x2655
+  __TEXT.__objc_stubs: 0x11c60
+  __DATA_CONST.__got: 0x8a0
+  __DATA_CONST.__const: 0x30d8
+  __DATA_CONST.__objc_classlist: 0x4a8
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x71c0
-  __DATA_CONST.__objc_superrefs: 0x410
-  __DATA_CONST.__objc_arraydata: 0xe20
+  __DATA_CONST.__objc_selrefs: 0x5f98
+  __DATA_CONST.__objc_superrefs: 0x378
+  __DATA_CONST.__objc_arraydata: 0xb60
   __AUTH_CONST.__auth_got: 0x7a0
-  __AUTH_CONST.__const: 0x1ae0
-  __AUTH_CONST.__cfstring: 0xba60
-  __AUTH_CONST.__objc_const: 0x15f48
-  __AUTH_CONST.__objc_intobj: 0x1290
-  __AUTH_CONST.__objc_arrayobj: 0x978
-  __AUTH_CONST.__objc_doubleobj: 0x120
-  __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0xfd4
-  __DATA.__data: 0x428
-  __DATA.__bss: 0x620
-  __DATA_DIRTY.__objc_data: 0x3200
-  __DATA_DIRTY.__bss: 0x9d8
+  __AUTH_CONST.__const: 0x1740
+  __AUTH_CONST.__cfstring: 0x9dc0
+  __AUTH_CONST.__objc_const: 0x124b8
+  __AUTH_CONST.__objc_intobj: 0xf60
+  __AUTH_CONST.__objc_arrayobj: 0x780
+  __AUTH_CONST.__objc_doubleobj: 0xa0
+  __AUTH_CONST.__objc_dictobj: 0xc8
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0xcc0
+  __DATA.__data: 0x3c8
+  __DATA.__bss: 0x528
+  __DATA_DIRTY.__objc_data: 0x2760
+  __DATA_DIRTY.__bss: 0x8b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B0C37499-DB1F-3713-BC88-BACA101DC45D
-  Functions: 5176
-  Symbols:   18070
-  CStrings:  10091
+  UUID: ECB9C7AC-FF55-315A-805A-B1256E798BDA
+  Functions: 4313
+  Symbols:   15087
+  CStrings:  8440
 
Symbols:
+ +[_PSBackgroundProcessingTask attachmentsInObject:hasField:]
+ +[_PSBackgroundProcessingTask interactionStore]
+ +[_PSBackgroundProcessingTask savedBookmark]
+ +[_PSBackgroundProcessingTask savedBookmark].cold.1
+ +[_PSBackgroundProcessingTask updateInteractionWithPhotoFeatures:]
+ +[_PSConstants realityChromeBundleId]
+ +[_PSConstants togetherdBundleId]
+ +[_PSContactHandleFeatureProvider featureNames]
+ +[_PSContactHandleFeatureProvider numberOfIncomingInteractions]
+ +[_PSContactHandleFeatureProvider numberOfOutgoingInteractions]
+ +[_PSContactHandleFeatureProvider timeSinceLastIncomingInteraction]
+ +[_PSContactHandleFeatureProvider timeSinceLastOutgoingInteraction]
+ +[_PSLogging psBackgroundProcessingChannel]
+ +[_PSLogging psBackgroundProcessingChannel].cold.1
+ +[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:]
+ +[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]
+ +[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:].cold.1
+ +[_PSPhotoSuggestions phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:withCompletion:]
+ +[_PSPhotoUtils attachmentsEligibleForPhotoProcessingFromAttachments:]
+ +[_PSPhotoUtils personIdentifiersForPeopleInPicturesWithIdentifiers:]
+ +[_PSPhotoUtils sceneTagsForPhotosWithIdentifiers:]
+ +[_PSPhotoUtils sharedMADService]
+ +[_PSPhotoUtils sharedMADService].cold.1
+ +[_PSPriorityContact supportsSecureCoding]
+ +[_PSSuggester suggesterWithDaemonUsingMaxSuggestionCount:]
+ -[_PSBackgroundProcessingTask .cxx_destruct]
+ -[_PSBackgroundProcessingTask handleRepeatingTask:]
+ -[_PSBackgroundProcessingTask handleRepeatingTask:].cold.1
+ -[_PSBackgroundProcessingTask handleRepeatingTask:].cold.2
+ -[_PSBackgroundProcessingTask handleRepeatingTask:].cold.3
+ -[_PSBackgroundProcessingTask handleRepeatingTask:].cold.4
+ -[_PSBackgroundProcessingTask handleRepeatingTask:].cold.5
+ -[_PSBackgroundProcessingTask init]
+ -[_PSBackgroundProcessingTask saveBookmark]
+ -[_PSBackgroundProcessingTask saveBookmark].cold.1
+ -[_PSBackgroundProcessingTask updatePlistWithDict:]
+ -[_PSBackgroundProcessingTask updatePlistWithDict:].cold.1
+ -[_PSContactHandleFeatureProvider .cxx_destruct]
+ -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:]
+ -[_PSContactHandleFeatureProvider _interactionFeaturesForHandle:].cold.1
+ -[_PSContactHandleFeatureProvider dealloc]
+ -[_PSContactHandleFeatureProvider init]
+ -[_PSContactHandleFeatureProvider interactionFeaturesForHandle:]
+ -[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]
+ -[_PSEnsembleModel psr_suggestionsFromSuggestionProxies:interactionsStatistics:maxSuggestions:predictionContext:]
+ -[_PSEnsembleModel psr_suggestionsFromSuggestionProxies:interactionsStatistics:maxSuggestions:predictionContext:].cold.1
+ -[_PSEnsembleModel shouldUseLegacyUI]
+ -[_PSFTZKWSuggestionsTransformerFactory boostPriorityContacts:]
+ -[_PSFTZKWSuggestionsTransformerFactory filterBlockedContacts]
+ -[_PSFTZKWSuggestionsTransformerFactory filterIDSReachable:]
+ -[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]
+ -[_PSHeuristics psr_inPhoneCallHeuristicSuggestionProxiesWithBundleIds:predictionContext:interactionsStatistics:]
+ -[_PSHyperRecentActivity .cxx_destruct]
+ -[_PSHyperRecentActivity activityType]
+ -[_PSHyperRecentActivity conversationId]
+ -[_PSHyperRecentActivity date]
+ -[_PSHyperRecentActivity initWithDate:activityType:conversationId:]
+ -[_PSHyperRecentActivity setActivityType:]
+ -[_PSHyperRecentActivity setConversationId:]
+ -[_PSHyperRecentActivity setDate:]
+ -[_PSKNNModel _featureVectorFromSuggestionDate:bundleID:peopleInPhotoIdentifiers:sceneTagsInPhotoIdentifiers:]
+ -[_PSPredictionContext bypassIDSFilter]
+ -[_PSPredictionContext priorityContacts]
+ -[_PSPredictionContext sceneTagsInPhotoIdentifiers]
+ -[_PSPredictionContext setBypassIDSFilter:]
+ -[_PSPredictionContext setPriorityContacts:]
+ -[_PSPredictionContext setSceneTagsInPhotoIdentifiers:]
+ -[_PSPriorityContact .cxx_destruct]
+ -[_PSPriorityContact contact]
+ -[_PSPriorityContact description]
+ -[_PSPriorityContact encodeWithCoder:]
+ -[_PSPriorityContact identifier]
+ -[_PSPriorityContact initWithCoder:]
+ -[_PSPriorityContact initWithContact:]
+ -[_PSPriorityContact initWithIdentifier:]
+ -[_PSPriorityContact initWithIdentifier:contact:]
+ -[_PSPriorityContact setContact:]
+ -[_PSPriorityContact setIdentifier:]
+ -[_PSSuggester deleteUIInteractionsMatchingSuggestLessFeedback:]
+ -[_PSSuggester getCachedSuggestionsFetchingIfNeeded:]
+ -[_PSTrialClient scenesBasedFeatures].cold.1
+ -[_PSTrialClient shouldUseVIPModel]
+ GCC_except_table102
+ GCC_except_table127
+ GCC_except_table128
+ GCC_except_table129
+ GCC_except_table146
+ GCC_except_table153
+ GCC_except_table156
+ GCC_except_table54
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table68
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table82
+ GCC_except_table90
+ GCC_except_table91
+ _IMCoreLibrary
+ _IMCoreLibraryCore
+ _LocalIMSPIGetAllChatsContainingParticipantWithHandle
+ _LocalIMSPIGetAllChatsContainingParticipantWithHandle.cold.1
+ _LocalIMSPIGetContactsByChatGUID
+ _LocalIMSPIGetContactsByChatGUID.cold.1
+ _LocalIMSPIGetGroupPhotosForChatsWithGroupIDs
+ _LocalIMSPIGetGroupPhotosForChatsWithGroupIDs.cold.1
+ _NSFileProtectionCompleteUntilFirstUserAuthentication
+ _OBJC_CLASS_$_BMSQLDatabase
+ _OBJC_CLASS_$__DKCoreDataStorage
+ _OBJC_CLASS_$__PSBackgroundProcessingTask
+ _OBJC_CLASS_$__PSContactHandleFeatureProvider
+ _OBJC_CLASS_$__PSHyperRecentActivity
+ _OBJC_CLASS_$__PSPriorityContact
+ _OBJC_IVAR_$__PSBackgroundProcessingTask._bookmark
+ _OBJC_IVAR_$__PSBackgroundProcessingTask._interactionStore
+ _OBJC_IVAR_$__PSContactHandleFeatureProvider._connection
+ _OBJC_IVAR_$__PSHyperRecentActivity._activityType
+ _OBJC_IVAR_$__PSHyperRecentActivity._conversationId
+ _OBJC_IVAR_$__PSHyperRecentActivity._date
+ _OBJC_IVAR_$__PSPredictionContext._bypassIDSFilter
+ _OBJC_IVAR_$__PSPredictionContext._priorityContacts
+ _OBJC_IVAR_$__PSPredictionContext._sceneTagsInPhotoIdentifiers
+ _OBJC_IVAR_$__PSPriorityContact._contact
+ _OBJC_IVAR_$__PSPriorityContact._identifier
+ _OBJC_METACLASS_$__PSBackgroundProcessingTask
+ _OBJC_METACLASS_$__PSContactHandleFeatureProvider
+ _OBJC_METACLASS_$__PSHyperRecentActivity
+ _OBJC_METACLASS_$__PSPriorityContact
+ _SuggestionProxyTypeHyperRecencyViewedThreadRewrite
+ __OBJC_$_CLASS_METHODS__PSBackgroundProcessingTask
+ __OBJC_$_CLASS_METHODS__PSContactHandleFeatureProvider
+ __OBJC_$_CLASS_METHODS__PSPriorityContact
+ __OBJC_$_CLASS_PROP_LIST__PSContactHandleFeatureProvider
+ __OBJC_$_CLASS_PROP_LIST__PSPriorityContact
+ __OBJC_$_INSTANCE_METHODS__PSBackgroundProcessingTask
+ __OBJC_$_INSTANCE_METHODS__PSContactHandleFeatureProvider
+ __OBJC_$_INSTANCE_METHODS__PSHyperRecentActivity
+ __OBJC_$_INSTANCE_METHODS__PSPriorityContact
+ __OBJC_$_INSTANCE_VARIABLES__PSBackgroundProcessingTask
+ __OBJC_$_INSTANCE_VARIABLES__PSContactHandleFeatureProvider
+ __OBJC_$_INSTANCE_VARIABLES__PSHyperRecentActivity
+ __OBJC_$_INSTANCE_VARIABLES__PSPriorityContact
+ __OBJC_$_PROP_LIST__PSHyperRecentActivity
+ __OBJC_$_PROP_LIST__PSPriorityContact
+ __OBJC_CLASS_PROTOCOLS_$__PSPriorityContact
+ __OBJC_CLASS_RO_$__PSBackgroundProcessingTask
+ __OBJC_CLASS_RO_$__PSContactHandleFeatureProvider
+ __OBJC_CLASS_RO_$__PSHyperRecentActivity
+ __OBJC_CLASS_RO_$__PSPriorityContact
+ __OBJC_METACLASS_RO_$__PSBackgroundProcessingTask
+ __OBJC_METACLASS_RO_$__PSContactHandleFeatureProvider
+ __OBJC_METACLASS_RO_$__PSHyperRecentActivity
+ __OBJC_METACLASS_RO_$__PSPriorityContact
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.546
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.547
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.970
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.977
+ ___111-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:]_block_invoke.1009
+ ___118-[_PSSuggestionFromTextPredictor suggestionsFromIncompleteRemindersWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.93
+ ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.866
+ ___123+[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:]_block_invoke
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.782
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.782.cold.1
+ ___150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.220
+ ___150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.225
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.422
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.422.cold.1
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.438
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.464
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.466
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.468
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.470
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke_2
+ ___33+[_PSPhotoUtils sharedMADService]_block_invoke
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.240
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.240.cold.1
+ ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.458
+ ___43+[_PSLogging psBackgroundProcessingChannel]_block_invoke
+ ___43+[_PSLogging psBackgroundProcessingChannel]_block_invoke.cold.1
+ ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.238
+ ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.238.cold.1
+ ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.242
+ ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke.601
+ ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke.639
+ ___47-[_PSSuggester suggestInteractionsFromContext:]_block_invoke.255
+ ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.437
+ ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.438
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.965
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.965.cold.1
+ ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke
+ ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke.208
+ ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.416
+ ___54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.289
+ ___54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.292
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.207
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.211
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_2.213
+ ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.428
+ ___58-[_PSContactSuggester contactPriorsForContactIdentifiers:]_block_invoke.283
+ ___60-[_PSFTZKWSuggestionsTransformerFactory filterIDSReachable:]_block_invoke
+ ___60-[_PSKNNModel rankedMapsShareEtaSuggestions:maxSuggestions:]_block_invoke.525
+ ___61-[_PSMessagesPinningSuggester submitMessagesPinningFeedback:]_block_invoke.272
+ ___62-[_PSFTZKWSuggestionsTransformerFactory filterBlockedContacts]_block_invoke
+ ___62-[_PSFTZKWSuggestionsTransformerFactory filterBlockedContacts]_block_invoke_2
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.682
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.682.cold.1
+ ___63-[_PSFTZKWSuggestionsTransformerFactory boostPriorityContacts:]_block_invoke
+ ___63-[_PSFTZKWSuggestionsTransformerFactory boostPriorityContacts:]_block_invoke_2
+ ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.449
+ ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.449.cold.1
+ ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.452
+ ___64-[_PSContactHandleFeatureProvider interactionFeaturesForHandle:]_block_invoke
+ ___64-[_PSContactHandleFeatureProvider interactionFeaturesForHandle:]_block_invoke.16
+ ___64-[_PSContactHandleFeatureProvider interactionFeaturesForHandle:]_block_invoke.cold.1
+ ___64-[_PSSuggester deleteUIInteractionsMatchingSuggestLessFeedback:]_block_invoke
+ ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.431
+ ___67-[_PSEnsembleModel autocompleteSearchResultsWithPredictionContext:]_block_invoke
+ ___67-[_PSMediaAnalysisProcessingTask executeTaskWithCompletionHandler:]_block_invoke.407
+ ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.464
+ ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.837
+ ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.455
+ ___68-[_PSSuggester showNotificationToFileARadarForUserStudyParticipants]_block_invoke.321
+ ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.461
+ ___70+[_PSPhotoUtils attachmentsEligibleForPhotoProcessingFromAttachments:]_block_invoke
+ ___72-[_PSEnsembleModel rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke
+ ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.643
+ ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.467
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.539
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.544
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.547
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.562
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.568
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.575
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.572
+ ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.473
+ ___77-[_PSMessagesPinningSuggester chatGuidsForMessagesPinningWithMaxSuggestions:]_block_invoke.212
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.372
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.389
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.396
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.396.cold.1
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.403
+ ___79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.362
+ ___79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.362.cold.1
+ ___80+[_PSFTZKWSuggestionsTransformerFactory getResultsFromTransformers:suggestions:]_block_invoke.71
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.726
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.615
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.631
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.704
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.420
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.423
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.424
+ ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.434
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.302
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.307
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_2
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_2.311
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_3
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_4
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_5
+ ___91-[_PSContactSuggester contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.190
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.220
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.223
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.227
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.227.cold.1
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.227.cold.2
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.239
+ ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.239.cold.1
+ ___96-[_PSSuggester(InteractionInformation) interactionCountForHandle:fetchLimit:interactionStoreDB:]_block_invoke.306
+ ___98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.83
+ ___98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.85
+ ___99-[_PSKNNModel rankedCoRecipientSuggestionsWithPredictionContext:modelConfiguration:maxSuggestions:]_block_invoke.392
+ ___Block_byref_object_copy_.370
+ ___Block_byref_object_copy_.471
+ ___Block_byref_object_dispose_.371
+ ___Block_byref_object_dispose_.472
+ ____PSShareSheetSuggestionBundleIDMapping_block_invoke.209
+ ___block_descriptor_32_e25_B16?0"NSManagedObject"8l
+ ___block_descriptor_32_e26_"NSArray"16?0"NSArray"8l
+ ___block_descriptor_32_e35_B16?0"_PSAutocompleteSuggestion"8l
+ ___block_descriptor_32_e38_"NSString"16?0"_PSPriorityContact"8l
+ ___block_descriptor_32_e59_q24?0"_PSHyperRecentActivity"8"_PSHyperRecentActivity"16l
+ ___block_descriptor_40_e8_32s_e26_B24?0"BMStoreEvent"8^B16ls32l8
+ ___block_descriptor_48_e8_32s40r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s_e18_B16?0"NSString"8ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e33_"NSMutableArray"16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_56_e8_32s_e22_B16?0"BMStoreEvent"8ls32l8
+ ___block_descriptor_64_e8_32s40s48s_e15_v16?0"NSSet"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.1000
+ ___block_literal_global.1002
+ ___block_literal_global.101
+ ___block_literal_global.163
+ ___block_literal_global.165
+ ___block_literal_global.167
+ ___block_literal_global.204
+ ___block_literal_global.206
+ ___block_literal_global.208
+ ___block_literal_global.212
+ ___block_literal_global.215
+ ___block_literal_global.222
+ ___block_literal_global.225
+ ___block_literal_global.241
+ ___block_literal_global.245
+ ___block_literal_global.254
+ ___block_literal_global.257
+ ___block_literal_global.269
+ ___block_literal_global.271
+ ___block_literal_global.274
+ ___block_literal_global.295
+ ___block_literal_global.301
+ ___block_literal_global.306
+ ___block_literal_global.310
+ ___block_literal_global.314
+ ___block_literal_global.315
+ ___block_literal_global.317
+ ___block_literal_global.399
+ ___block_literal_global.407
+ ___block_literal_global.412
+ ___block_literal_global.415
+ ___block_literal_global.419
+ ___block_literal_global.422
+ ___block_literal_global.43
+ ___block_literal_global.436
+ ___block_literal_global.447
+ ___block_literal_global.451
+ ___block_literal_global.454
+ ___block_literal_global.457
+ ___block_literal_global.463
+ ___block_literal_global.472
+ ___block_literal_global.504
+ ___block_literal_global.509
+ ___block_literal_global.511
+ ___block_literal_global.524
+ ___block_literal_global.542
+ ___block_literal_global.546
+ ___block_literal_global.549
+ ___block_literal_global.551
+ ___block_literal_global.57
+ ___block_literal_global.571
+ ___block_literal_global.574
+ ___block_literal_global.577
+ ___block_literal_global.600
+ ___block_literal_global.612
+ ___block_literal_global.62
+ ___block_literal_global.624
+ ___block_literal_global.641
+ ___block_literal_global.653
+ ___block_literal_global.656
+ ___block_literal_global.681
+ ___block_literal_global.69
+ ___block_literal_global.690
+ ___block_literal_global.709
+ ___block_literal_global.740
+ ___block_literal_global.773
+ ___block_literal_global.876
+ ___block_literal_global.879
+ ___block_literal_global.882
+ ___block_literal_global.885
+ ___block_literal_global.958
+ ___getIMSPIGetAllChatsContainingParticipantWithHandleSymbolLoc_block_invoke
+ ___getIMSPIGetContactsByChatGUIDSymbolLoc_block_invoke
+ ___getIMSPIGetGroupPhotosForChatsWithGroupIDsSymbolLoc_block_invoke
+ ___getIMSPISuggestionsObjectClass_block_invoke
+ __getDirectSuggestionsWithContext:withTimeout:._pasOnceToken10
+ __suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken140
+ _asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:._pasOnceToken73
+ _autocompleteSearchResultsWithPredictionContext:._pasOnceToken106
+ _chatGUIDFromHandlesBlock_block_invoke
+ _defaultServiceWithMaxSuggestionCount:._pasOnceToken9
+ _dispatch_group_async
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _feedbackDictionary._pasOnceToken8
+ _getIMSPIGetAllChatsContainingParticipantWithHandleSymbolLoc
+ _getIMSPIGetAllChatsContainingParticipantWithHandleSymbolLoc.ptr
+ _getIMSPIGetContactsByChatGUIDSymbolLoc
+ _getIMSPIGetContactsByChatGUIDSymbolLoc.ptr
+ _getIMSPIGetGroupPhotosForChatsWithGroupIDsSymbolLoc
+ _getIMSPIGetGroupPhotosForChatsWithGroupIDsSymbolLoc.ptr
+ _getIMSPISuggestionsObjectClass
+ _getIMSPISuggestionsObjectClass.softClass
+ _getPHPhotoLibraryClass
+ _getResultsFromTransformers:suggestions:._pasOnceToken20
+ _init._pasOnceToken7
+ _objc_msgSend$App
+ _objc_msgSend$ConversationUserInteraction
+ _objc_msgSend$InFocus
+ _objc_msgSend$_featureVectorFromSuggestionDate:bundleID:peopleInPhotoIdentifiers:sceneTagsInPhotoIdentifiers:
+ _objc_msgSend$_setError
+ _objc_msgSend$absoluteTimestamp
+ _objc_msgSend$activityType
+ _objc_msgSend$attachmentsEligibleForPhotoProcessingFromAttachments:
+ _objc_msgSend$attachmentsInObject:hasField:
+ _objc_msgSend$boostPriorityContacts:
+ _objc_msgSend$bypassIDSFilter
+ _objc_msgSend$characterSetWithCharactersInString:
+ _objc_msgSend$chatGUID
+ _objc_msgSend$computeSASSFeatureWithSceneCategoriesDetectedInPhoto:andConfiguredSceneCategoryTags:
+ _objc_msgSend$configuredSceneCategoryTagNames
+ _objc_msgSend$data
+ _objc_msgSend$deleteUIInteractionsMatchingSuggestLessFeedback:
+ _objc_msgSend$detectedSceneCategoryNamesFromSceneNetTags:
+ _objc_msgSend$eventType
+ _objc_msgSend$executeQuery:
+ _objc_msgSend$featureNames
+ _objc_msgSend$filterBlockedContacts
+ _objc_msgSend$filterIDSReachable:
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$getCachedSuggestionsFetchingIfNeeded:
+ _objc_msgSend$getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:
+ _objc_msgSend$hasError
+ _objc_msgSend$hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$initWithDate:activityType:conversationId:
+ _objc_msgSend$initWithIdentifier:contact:
+ _objc_msgSend$interactionFeaturesForHandle:reply:
+ _objc_msgSend$managedObjectContextFor:
+ _objc_msgSend$next
+ _objc_msgSend$numberOfIncomingInteractions
+ _objc_msgSend$numberOfOutgoingInteractions
+ _objc_msgSend$peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:
+ _objc_msgSend$personIdentifiersForPeopleInPicturesWithIdentifiers:
+ _objc_msgSend$phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:withCompletion:
+ _objc_msgSend$position
+ _objc_msgSend$priorityContacts
+ _objc_msgSend$propertyListWithData:options:format:error:
+ _objc_msgSend$psBackgroundProcessingChannel
+ _objc_msgSend$psr_suggestionsFromSuggestionProxies:interactionsStatistics:maxSuggestions:predictionContext:
+ _objc_msgSend$queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:
+ _objc_msgSend$realityChromeBundleId
+ _objc_msgSend$reversed
+ _objc_msgSend$row
+ _objc_msgSend$savedBookmark
+ _objc_msgSend$sceneTagsForPhotosWithIdentifiers:
+ _objc_msgSend$sceneTagsInPhotoIdentifiers
+ _objc_msgSend$setExpirationHandler:
+ _objc_msgSend$setIncludePets:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setPriorityContacts:
+ _objc_msgSend$setSceneTagsInPhotoIdentifiers:
+ _objc_msgSend$setTaskCompleted
+ _objc_msgSend$setTaskExpiredWithRetryAfter:error:
+ _objc_msgSend$setUseVIPModel:
+ _objc_msgSend$shouldUseLegacyUI
+ _objc_msgSend$shouldUseVIPModel
+ _objc_msgSend$starting
+ _objc_msgSend$storage
+ _objc_msgSend$timeSinceLastIncomingInteraction
+ _objc_msgSend$timeSinceLastOutgoingInteraction
+ _objc_msgSend$togetherdBundleId
+ _objc_msgSend$tupleWithFirst:second:
+ _objc_msgSend$updateInteractionWithPhotoFeatures:
+ _objc_msgSend$updateObjectsInContext:entityName:predicate:sortDescriptors:batchFetchLimit:totalFetchLimit:includeSubentities:updateBlock:
+ _objc_msgSend$waitForGroup:
+ _objc_msgSend$waitForGroup:timeoutSeconds:
+ _predictWithPredictionContext:maxSuggestions:contactKeysToFetch:._pasOnceToken102
+ _psBackgroundProcessingChannel.onceToken
+ _psBackgroundProcessingChannel.psBackgroundProcessingChannel
+ _psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:._pasOnceToken226
+ _rankedZKWSuggestionsFromContext:._pasOnceToken104
+ _rankedZkwSuggestionsFromPredictionArray:forBundleID:._pasOnceToken46
+ _sharedInstance._pasOnceToken7
+ _sharedMADService._pasOnceToken15
- +[FidesPHSEvaluatorDataSource defaultRecipeParams]
- +[FidesPHSEvaluatorDataSource initialize]
- +[GBDTEvaluator initialize]
- +[LighthouseShareSheetPFLTraining initialize]
- +[LighthouseShareSheetPFLTraining processDataForStore:recipeInfo:]
- +[LighthouseShareSheetPFLTraining processDataForStore:taskParameters:]
- +[LighthouseShareSheetPFLTraining taskResultFromDict:]
- +[PSDESPlugin initialize]
- +[_PSBehaviorRuleRankingUtilities batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featureDictArray:]
- +[_PSBehaviorRuleRankingUtilities batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featureDictArray:].cold.1
- +[_PSBehaviorRuleRankingUtilities batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featureDictArray:].cold.2
- +[_PSBehaviorRuleRankingUtilities batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featureDictArray:].cold.3
- +[_PSBehaviorRuleRankingUtilities batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featurizedRules:]
- +[_PSBehaviorRuleRankingUtilities batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featurizedRules:].cold.1
- +[_PSBehaviorRuleRankingUtilities batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featurizedRules:].cold.2
- +[_PSBehaviorRuleRankingUtilities batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featurizedRules:].cold.3
- +[_PSBehaviorRuleRankingUtilities batchPredictWithMLModel:featureArrayDict:]
- +[_PSBehaviorRuleRankingUtilities batchPredictWithMLModel:featureArrayDict:].cold.1
- +[_PSBehaviorRuleRankingUtilities batchPredictWithMLModel:featureArrayDict:].cold.2
- +[_PSBehaviorRuleRankingUtilities compileMLModelAtPath:]
- +[_PSBehaviorRuleRankingUtilities compileMLModelAtPath:].cold.1
- +[_PSBehaviorRuleRankingUtilities copyFileFromURL:toURL:]
- +[_PSBehaviorRuleRankingUtilities copyZippedAdaptableModel:]
- +[_PSBehaviorRuleRankingUtilities copyZippedAdaptableModel:].cold.1
- +[_PSBehaviorRuleRankingUtilities copyZippedAdaptableModel:].cold.2
- +[_PSBehaviorRuleRankingUtilities getAdaptedCompiledMLModelPath]
- +[_PSBehaviorRuleRankingUtilities getAdaptedModelRecipeVersionFilePath]
- +[_PSBehaviorRuleRankingUtilities getArchivedDefaultAdaptableModelPath]
- +[_PSBehaviorRuleRankingUtilities getDeployedAdaptableCompiledMLModelPath]
- +[_PSBehaviorRuleRankingUtilities getDeployedCompiledMLModelPathForContactRanker]
- +[_PSBehaviorRuleRankingUtilities getDeployedCompiledMLModelPath]
- +[_PSBehaviorRuleRankingUtilities getIntermediateAdaptableCompiledMLModel]
- +[_PSBehaviorRuleRankingUtilities getTrialCompiledAdaptableMLModelPath]
- +[_PSBehaviorRuleRankingUtilities getTrialCompiledMLModelPathForContactRanker]
- +[_PSBehaviorRuleRankingUtilities getTrialCompiledMLModelPath]
- +[_PSBehaviorRuleRankingUtilities getZippedDefaultAdaptableModelPath]
- +[_PSBehaviorRuleRankingUtilities loadAdaptableModelConfig:]
- +[_PSBehaviorRuleRankingUtilities loadAdaptableModelConfig:].cold.1
- +[_PSBehaviorRuleRankingUtilities loadDeployedAdaptableModelUnderDirectory:]
- +[_PSBehaviorRuleRankingUtilities loadDeployedAdaptableModelUnderDirectory:].cold.1
- +[_PSBehaviorRuleRankingUtilities loadDeployedAdaptableModelUnderDirectory:].cold.2
- +[_PSBehaviorRuleRankingUtilities loadDeployedAdaptableModelUnderDirectory:].cold.3
- +[_PSBehaviorRuleRankingUtilities loadMLModel:modelConfig:]
- +[_PSBehaviorRuleRankingUtilities loadMLModel:modelConfig:].cold.1
- +[_PSBehaviorRuleRankingUtilities loadMLModelConfigurationWithConfigDict:]
- +[_PSBehaviorRuleRankingUtilities predictWithMLModel:featureDictArray:]
- +[_PSBehaviorRuleRankingUtilities predictWithMLModel:featureDictArray:].cold.1
- +[_PSBehaviorRuleRankingUtilities predictWithMLModel:featureDictArray:].cold.2
- +[_PSBehaviorRuleRankingUtilities reformatFeaturesInFeatureDictArray:]
- +[_PSBehaviorRuleRankingUtilities reformatFeaturesInFeaturizedBehaviorRuleArray:]
- +[_PSBehaviorRuleRankingUtilities removeFolderAtPath:]
- +[_PSBehaviorRuleRankingUtilities removeFolderAtPath:].cold.1
- +[_PSBehaviorRuleRankingUtilities unzipFileWithPath:toFileName:toFolderPath:]
- +[_PSBehaviorRuleRankingUtilities unzipFileWithPath:toFileName:toFolderPath:].cold.1
- +[_PSConfidenceModel supportsSecureCoding]
- +[_PSConfidenceModelArchive supportsSecureCoding]
- +[_PSConfidenceModelDriver defaultArchivePath]
- +[_PSConfidenceModelDriver deleteArchiveFile]
- +[_PSConfidenceModelDriver deleteArchiveFile].cold.1
- +[_PSConfidenceModelDriver deleteArchiveFile].cold.2
- +[_PSContactFillerDataCollectionUtilities calculateNormContantsGivenInteractionStore:normConstants:]
- +[_PSContactFillerDataCollectionUtilities calculateNormContantsGivenInteractionStore:normConstants:].cold.1
- +[_PSContactFillerDataCollectionUtilities calculateNormContantsGivenInteractionStore:normConstants:].cold.2
- +[_PSContactFillerDataCollectionUtilities calculateNormContantsGivenInteractionStore:normConstants:].cold.3
- +[_PSContactFillerDataCollectionUtilities calculateNormContantsGivenInteractionStore:normConstants:].cold.4
- +[_PSContactFillerDataCollectionUtilities calculateNormContantsGivenInteractionStore:normConstants:].cold.5
- +[_PSContactFillerDataCollectionUtilities calculateNormalizedCallingFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:direction:]
- +[_PSContactFillerDataCollectionUtilities calculateNormalizedCallingFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:direction:].cold.1
- +[_PSContactFillerDataCollectionUtilities calculateNormalizedShareFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:]
- +[_PSContactFillerDataCollectionUtilities calculateNormalizedShareFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:].cold.1
- +[_PSContactFillerDataCollectionUtilities calculateNormalizedTextingFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:direction:]
- +[_PSContactFillerDataCollectionUtilities calculateNormalizedTextingFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:direction:].cold.1
- +[_PSContactFillerDataCollectionUtilities calculateTimeBucketGivenInteraction:timeOfShareInteraction:]
- +[_PSContactFillerDataCollectionUtilities calculateTimeSinceLastCallForContactGivenContactIdPredicate:direction:timeOfShareInteraction:interactionCache:]
- +[_PSContactFillerDataCollectionUtilities calculateTimeSinceLastShareForContactGivenContactIdPredicate:timeOfShareInteraction:interactionCache:]
- +[_PSContactFillerDataCollectionUtilities calculateTimeSinceLastTextForContactGivenContactIdPredicate:direction:timeOfShareInteraction:interactionCache:]
- +[_PSContactFillerDataCollectionUtilities contactFillerBucketedValue:]
- +[_PSContactFillerDataCollectionUtilities doesSuggestionProxyMatch:withInteraction:]
- +[_PSContactFillerDataCollectionUtilities doesTheRecipientsMatchInInteraction1:interaction2:]
- +[_PSContactFillerDataCollectionUtilities enforceOneSignificantFigureForDouble:]
- +[_PSContactFillerDataCollectionUtilities enforceOneSignificantFigureForSmallDouble:]
- +[_PSContactFillerDataCollectionUtilities extractFeaturesFromBehaviorRulesIntoPETMessage:behaviorRules:MLModelScores:]
- +[_PSContactFillerDataCollectionUtilities extractFeaturesFromBehaviorRulesIntoPETMessage:behaviorRules:contextItems:ruleRankingModel:]
- +[_PSContactFillerDataCollectionUtilities extractFrequencyRecencyFeaturesIntoPETMessage:recipientID:interaction:normConstants:numberOfDaysToLookBack:interactionStore:timeOfShareInteraction:contactPropertyCache:interactionCache:]
- +[_PSContactFillerDataCollectionUtilities extractUserFeaturesIntoPETMessage:normConstants:behaviorRetriever:]
- +[_PSContactFillerDataCollectionUtilities filterRulesBasedOnInteractionGivenRuleList:interaction:]
- +[_PSContactFillerDataCollectionUtilities getBehaviorRulesGivenContext:behaviorRetriever:]
- +[_PSContactFillerDataCollectionUtilities getInteractionModelScoreForEvent:forInteractionRecipients:]
- +[_PSContactFillerDataCollectionUtilities getInteractionModelScoreForSuggestions:forInteractionRecipients:]
- +[_PSContactFillerDataCollectionUtilities getInteractionRecipientFromInteraction:]
- +[_PSContactFillerDataCollectionUtilities getListOfContactsFromCashedMessagesInteraction:cashedShareInteractions:]
- +[_PSContactFillerDataCollectionUtilities getListOfContactsInteractedInTheLastNumberOfDays:interactionStore:limit:]
- +[_PSContactFillerDataCollectionUtilities getListOfContactsInteractedInTheLastNumberOfDays:interactionStore:limit:].cold.1
- +[_PSContactFillerDataCollectionUtilities initContactPropertyCache:timeOfShareInteraction:interactionStore:]
- +[_PSContactFillerDataCollectionUtilities recipientPredictedCorrectlyByRule:interaction:bundleId:]
- +[_PSContactFillerDataCollectionUtilities resolveUniqueContactIdGivenInteraction:]
- +[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:]
- +[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]
- +[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:].cold.1
- +[_PSPhotoSuggestions phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]
- +[_PSSuggester hasInitializedCache]
- +[_PSSuggester setHasInitializedCache:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent .cxx_destruct]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent confidence]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent contentUrlInContext]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent contentUrlInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent contentUrlOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent copyTo:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent copyWithZone:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent description]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent dictionaryRepresentation]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent hasPersonAndAppMatched]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent hasPersonMatched]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent hasSessionId]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent hasTopicContainingRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent hasTopicInContext]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent hasTopicInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent hasTopicOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent hasTopicRulesCardinality]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent hash]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent highConfidenceRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent isEqual:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent isWeekendInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent isWeekendOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent lOIInContext]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent lOIInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent lOIOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent locationOfInterestContainingRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent locationOfInterestRulesCardinality]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent lowConfidenceRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent mediumConfidenceRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent mergeFrom:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent personAndAppMatched]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent personMatched]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoContactContainingRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoContactInContext]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoContactInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoContactOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoContactRulesCardinality]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoSceneContainingRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoSceneInContext]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoSceneInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoSceneOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent photoSceneRulesCardinality]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent readFrom:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent sessionId]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setConfidence:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setContentUrlInContext:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setContentUrlInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setContentUrlOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setHasPersonAndAppMatched:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setHasPersonMatched:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setHasTopicContainingRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setHasTopicInContext:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setHasTopicInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setHasTopicOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setHasTopicRulesCardinality:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setHighConfidenceRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setIsWeekendInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setIsWeekendOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setLOIInContext:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setLOIInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setLOIOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setLocationOfInterestContainingRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setLocationOfInterestRulesCardinality:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setLowConfidenceRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setMediumConfidenceRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPersonAndAppMatched:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPersonMatched:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoContactContainingRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoContactInContext:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoContactInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoContactOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoContactRulesCardinality:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoSceneContainingRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoSceneInContext:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoSceneInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoSceneOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setPhotoSceneRulesCardinality:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setSessionId:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setSourceBundleIdContainingRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setSourceBundleIdInContext:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setSourceBundleIdInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setSourceBundleIdOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setSourceBundleIdRulesCardinality:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setSupport:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTargetBundleIDInConsequent:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTargetBundleIdContainingRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTargetBundleIdInContext:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTargetBundleIdInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTargetBundleIdOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTargetBundleIdRulesCardinality:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTimeOfDaySlotInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTimeOfDaySlotOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTopicContainingRuleCount:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTopicInContext:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTopicInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTopicOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTopicRulesCardinality:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTotalMessagesRecieved:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTotalMessagesSent:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setTotalShares:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setUniqueShareEventIdentifier:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setUtiTypeInContext:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setUtiTypeInRule:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent setUtiTypeOverlap:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent sourceBundleIdContainingRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent sourceBundleIdInContext]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent sourceBundleIdInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent sourceBundleIdOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent sourceBundleIdRulesCardinality]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent support]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent targetBundleIDInConsequent]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent targetBundleIdContainingRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent targetBundleIdInContext]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent targetBundleIdInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent targetBundleIdOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent targetBundleIdRulesCardinality]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent timeOfDaySlotInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent timeOfDaySlotOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent topicContainingRuleCount]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent topicInContext]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent topicInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent topicOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent topicRulesCardinality]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent totalMessagesRecieved]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent totalMessagesSent]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent totalShares]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent uniqueShareEventIdentifier]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent utiTypeInContext]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent utiTypeInRule]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent utiTypeOverlap]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent writeTo:]
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent writeTo:].cold.1
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent writeTo:].cold.2
- -[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent writeTo:].cold.3
- -[FidesPHSEvaluatorDataSource .cxx_destruct]
- -[FidesPHSEvaluatorDataSource GBDTQuestions]
- -[FidesPHSEvaluatorDataSource batchSize]
- -[FidesPHSEvaluatorDataSource classLearningRates]
- -[FidesPHSEvaluatorDataSource classThreshold]
- -[FidesPHSEvaluatorDataSource computeFirstOrderGradients]
- -[FidesPHSEvaluatorDataSource computeSecondOrderGradients]
- -[FidesPHSEvaluatorDataSource freezeComponents]
- -[FidesPHSEvaluatorDataSource gradNormFactor]
- -[FidesPHSEvaluatorDataSource gradNormType]
- -[FidesPHSEvaluatorDataSource initWithRecipe:inputVectors:targetVector:error:]
- -[FidesPHSEvaluatorDataSource inputSplice]
- -[FidesPHSEvaluatorDataSource inputVectors]
- -[FidesPHSEvaluatorDataSource l2NormBound]
- -[FidesPHSEvaluatorDataSource labelMap]
- -[FidesPHSEvaluatorDataSource layersToTrain]
- -[FidesPHSEvaluatorDataSource learningRateDecay]
- -[FidesPHSEvaluatorDataSource learningRate]
- -[FidesPHSEvaluatorDataSource numLocalIterations]
- -[FidesPHSEvaluatorDataSource objectiveFunction]
- -[FidesPHSEvaluatorDataSource recipe]
- -[FidesPHSEvaluatorDataSource recordDatas]
- -[FidesPHSEvaluatorDataSource recordInfos]
- -[FidesPHSEvaluatorDataSource records]
- -[FidesPHSEvaluatorDataSource reportGradientsBothSidesOfSplit]
- -[FidesPHSEvaluatorDataSource reportNodeSumGradients]
- -[FidesPHSEvaluatorDataSource reportPerFeatureResultDifference]
- -[FidesPHSEvaluatorDataSource reportPerNodeResultDifference]
- -[FidesPHSEvaluatorDataSource setRecipe:]
- -[FidesPHSEvaluatorDataSource setRecordDatas:]
- -[FidesPHSEvaluatorDataSource setRecordInfos:]
- -[FidesPHSEvaluatorDataSource setRecords:]
- -[FidesPHSEvaluatorDataSource targetVector]
- -[FidesPHSEvaluatorDataSource translateVector]
- -[FidesPHSEvaluatorDataSource weightVector]
- -[GBDTEvaluator _computeFirstOrderGradientsWithTargets:predictions:positiveSampleWeight:]
- -[GBDTEvaluator _computePredictionsFromModelWithInputVectors:currentModel:error:]
- -[GBDTEvaluator _computeSecondOrderGradientsWithTargets:predictions:positiveSampleWeight:]
- -[GBDTEvaluator _computeSumOfGradientsLeftAndRightOfSplitWithFeature:threshold:inputVectors:gradients:]
- -[GBDTEvaluator _differenceArrayWithArray:]
- -[GBDTEvaluator _evaluateResultWithGradients:questions:inputVectors:reportGradientsBothSidesOfSplit:reportNodeSumGradients:reportPerFeatureResultDifference:reportPerNodeResultDifference:]
- -[GBDTEvaluator _findNodeSamplesWithDecisionPath:inputVectors:gradients:]
- -[GBDTEvaluator _firstOrderGradientWithPrediction:label:]
- -[GBDTEvaluator _l1NormWithArray:]
- -[GBDTEvaluator _l2NormWithArray:]
- -[GBDTEvaluator _makeKeysWithInputVectors:]
- -[GBDTEvaluator _secondOrderGradientWithPrediction:]
- -[GBDTEvaluator _sigmoidWithValue:]
- -[GBDTEvaluator _sumAbsoluteErrorWithPredictions:targets:]
- -[GBDTEvaluator _sumAccuratePredictionsWithPredictions:targets:]
- -[GBDTEvaluator _translateResultWithTranslateVector:result:]
- -[GBDTEvaluator _weightResultWithWeightVector:result:]
- -[GBDTEvaluator evaluateWithModelURL:dataSource:processDataReturnDict:error:]
- -[GBDTEvaluator evaluateWithModelURL:dataSource:processDataReturnDict:error:].cold.1
- -[GBDTEvaluator evaluateWithModelURL:dataSource:processDataReturnDict:error:].cold.2
- -[GBDTEvaluator evaluateWithModelURL:dataSource:processDataReturnDict:error:].cold.3
- -[GBDTEvaluator evaluateWithModelURL:dataSource:processDataReturnDict:error:].cold.4
- -[GBDTEvaluator evaluateWithModelURL:dataSource:processDataReturnDict:error:].cold.5
- -[LighthouseShareSheetPFLTraining .cxx_destruct]
- -[LighthouseShareSheetPFLTraining configBoltTaskIDSpecification]
- -[LighthouseShareSheetPFLTraining configDepthSpecification]
- -[LighthouseShareSheetPFLTraining configTreeSpecification]
- -[LighthouseShareSheetPFLTraining createDataSourceForDodMLRecipe:error:]
- -[LighthouseShareSheetPFLTraining createDataSourceForRecipe:error:]
- -[LighthouseShareSheetPFLTraining createMLFeatureProviderArrayFromSingleShareEventData:]
- -[LighthouseShareSheetPFLTraining dataSource]
- -[LighthouseShareSheetPFLTraining evaluateMetricsWithModelURL:]
- -[LighthouseShareSheetPFLTraining evaluateMetricsWithModelURL:].cold.1
- -[LighthouseShareSheetPFLTraining evaluateMetricsWithModelURL:].cold.2
- -[LighthouseShareSheetPFLTraining featureMatricesForAllShareEvents]
- -[LighthouseShareSheetPFLTraining featureNameDict]
- -[LighthouseShareSheetPFLTraining generateResultsDictionayWithModelURL:error:]
- -[LighthouseShareSheetPFLTraining generateResultsDictionayWithModelURL:error:].cold.1
- -[LighthouseShareSheetPFLTraining generateResultsDictionayWithModelURL:error:].cold.2
- -[LighthouseShareSheetPFLTraining knowledgeStore]
- -[LighthouseShareSheetPFLTraining processDataForMetricEvaluationForStore:]
- -[LighthouseShareSheetPFLTraining processDataReturnDict]
- -[LighthouseShareSheetPFLTraining runTask:knowledgeStore:error:]
- -[LighthouseShareSheetPFLTraining runTask:knowledgeStore:error:].cold.1
- -[LighthouseShareSheetPFLTraining runTask:knowledgeStore:error:].cold.2
- -[LighthouseShareSheetPFLTraining runTask:knowledgeStore:error:].cold.3
- -[LighthouseShareSheetPFLTraining runTask:knowledgeStore:error:].cold.4
- -[LighthouseShareSheetPFLTraining runWithRecipeInfo:knowledgeStore:error:]
- -[LighthouseShareSheetPFLTraining runWithRecipeInfo:knowledgeStore:error:].cold.1
- -[LighthouseShareSheetPFLTraining runWithRecipeInfo:knowledgeStore:error:].cold.2
- -[LighthouseShareSheetPFLTraining runWithRecipeInfo:knowledgeStore:error:].cold.3
- -[LighthouseShareSheetPFLTraining runWithRecipeInfo:knowledgeStore:error:].cold.4
- -[LighthouseShareSheetPFLTraining runWithRecipeInfo:knowledgeStore:error:].cold.5
- -[LighthouseShareSheetPFLTraining selectedFeaturesConfig]
- -[LighthouseShareSheetPFLTraining setConfigBoltTaskIDSpecification:]
- -[LighthouseShareSheetPFLTraining setConfigDepthSpecification:]
- -[LighthouseShareSheetPFLTraining setConfigTreeSpecification:]
- -[LighthouseShareSheetPFLTraining setDataSource:]
- -[LighthouseShareSheetPFLTraining setFeatureMatricesForAllShareEvents:]
- -[LighthouseShareSheetPFLTraining setFeatureNameDict:]
- -[LighthouseShareSheetPFLTraining setKnowledgeStore:]
- -[LighthouseShareSheetPFLTraining setProcessDataReturnDict:]
- -[LighthouseShareSheetPFLTraining setSelectedFeaturesConfig:]
- -[LighthouseShareSheetPFLTraining sigmoid:]
- -[ModelHyperparameters .cxx_destruct]
- -[ModelHyperparameters adaptationStrategy]
- -[ModelHyperparameters initWithNumTrees:learningRate:minChildWeight:adaptationStrategy:]
- -[ModelHyperparameters learningRate]
- -[ModelHyperparameters minChildWeight]
- -[ModelHyperparameters numTrees]
- -[ModelHyperparameters setAdaptationStrategy:]
- -[ModelHyperparameters setLearningRate:]
- -[ModelHyperparameters setMinChildWeight:]
- -[ModelHyperparameters setNumTrees:]
- -[NSMutableArray(Shuffling) shuffle]
- -[PSDESPlugin .cxx_destruct]
- -[PSDESPlugin knowledgeStore]
- -[PSDESPlugin performEvaluation:]
- -[PSDESPlugin setKnowledgeStore:]
- -[PSDESPlugin shouldDownloadAttachmentWithURL:recipe:recordInfo:]
- -[_PSBehaviorRuleFeatureExtraction .cxx_destruct]
- -[_PSBehaviorRuleFeatureExtraction behaviorRetriever]
- -[_PSBehaviorRuleFeatureExtraction bucketedValue:]
- -[_PSBehaviorRuleFeatureExtraction constantFeaturesReady]
- -[_PSBehaviorRuleFeatureExtraction constantFeatures]
- -[_PSBehaviorRuleFeatureExtraction contextFeaturesReady]
- -[_PSBehaviorRuleFeatureExtraction contextFeatures]
- -[_PSBehaviorRuleFeatureExtraction extractConstantFeaturesForMLModelIntoFeatures:]
- -[_PSBehaviorRuleFeatureExtraction extractConstantFeaturesForMLModelIntoFeatures:].cold.1
- -[_PSBehaviorRuleFeatureExtraction extractConstantFeaturesForMLModelIntoFeatures:].cold.2
- -[_PSBehaviorRuleFeatureExtraction extractConstantFeaturesForMLModelIntoFeatures:].cold.3
- -[_PSBehaviorRuleFeatureExtraction extractContextMatchFeatures:features:]
- -[_PSBehaviorRuleFeatureExtraction extractFeaturesGivenRule:contextItems:features:]
- -[_PSBehaviorRuleFeatureExtraction initWithMetadata:]
- -[_PSBehaviorRuleFeatureExtraction interactionStore]
- -[_PSBehaviorRuleFeatureExtraction metadata]
- -[_PSBehaviorRuleFeatureExtraction precalculateConstantFeatures]
- -[_PSBehaviorRuleFeatureExtraction setConstantFeatures:]
- -[_PSBehaviorRuleFeatureExtraction setConstantFeaturesReady:]
- -[_PSBehaviorRuleFeatureExtraction setContextFeatures:]
- -[_PSBehaviorRuleFeatureExtraction setContextFeaturesReady:]
- -[_PSBehaviorRuleFeatureExtraction transferFeaturesFrom:toFeatures:]
- -[_PSConfidenceModel .cxx_destruct]
- -[_PSConfidenceModel addEvent:]
- -[_PSConfidenceModel bufferHead]
- -[_PSConfidenceModel bufferSize]
- -[_PSConfidenceModel circularBuffer]
- -[_PSConfidenceModel copyWithZone:]
- -[_PSConfidenceModel encodeWithCoder:]
- -[_PSConfidenceModel getConfidence]
- -[_PSConfidenceModel initWithBufferSize:minimumInstanceCount:]
- -[_PSConfidenceModel initWithBufferSize:sum:circularBuffer:bufferHead:]
- -[_PSConfidenceModel initWithCoder:]
- -[_PSConfidenceModel minimumInstanceCount]
- -[_PSConfidenceModel resetBuffer]
- -[_PSConfidenceModel setBufferHead:]
- -[_PSConfidenceModel setBufferSize:]
- -[_PSConfidenceModel setCircularBuffer:]
- -[_PSConfidenceModel setMinimumInstanceCount:]
- -[_PSConfidenceModel setSum:]
- -[_PSConfidenceModel sum]
- -[_PSConfidenceModelArchive .cxx_destruct]
- -[_PSConfidenceModelArchive confidenceModelDictionary]
- -[_PSConfidenceModelArchive copyWithZone:]
- -[_PSConfidenceModelArchive encodeWithCoder:]
- -[_PSConfidenceModelArchive initWithCoder:]
- -[_PSConfidenceModelArchive initWithConfidenceModelDictionary:]
- -[_PSConfidenceModelDriver .cxx_destruct]
- -[_PSConfidenceModelDriver addEventForModel:forUseCaseKey:event:]
- -[_PSConfidenceModelDriver confidenceModelDictionary]
- -[_PSConfidenceModelDriver getConfidenceForModel:forUseCaseKey:]
- -[_PSConfidenceModelDriver getDictionaryFromArchiveAtPath:]
- -[_PSConfidenceModelDriver getDictionaryFromArchiveAtPath:].cold.1
- -[_PSConfidenceModelDriver getDictionaryFromArchiveAtPath:].cold.2
- -[_PSConfidenceModelDriver getOrMakeConfidenceModelDictionary]
- -[_PSConfidenceModelDriver init]
- -[_PSConfidenceModelDriver registerModelKey:forUseCaseKey:confidenceWindowSize:minimumInstanceCount:]
- -[_PSConfidenceModelDriver setConfidenceModelDictionary:]
- -[_PSConfidenceModelDriver writeArchive:toFilePath:]
- -[_PSConfidenceModelDriver writeArchive:toFilePath:].cold.1
- -[_PSConfidenceModelDriver writeArchive:toFilePath:].cold.2
- -[_PSConfidenceModelDriver writeArchive:toFilePath:].cold.3
- -[_PSConfidenceModelDriver writeArchiveFromDict:]
- -[_PSConfidenceModelForSharing .cxx_destruct]
- -[_PSConfidenceModelForSharing _PSConfidenceModelInUse]
- -[_PSConfidenceModelForSharing addEventForModel:event:]
- -[_PSConfidenceModelForSharing confidenceModelDriver]
- -[_PSConfidenceModelForSharing findObjectWithID:inArray:]
- -[_PSConfidenceModelForSharing getConfidenceForModel:]
- -[_PSConfidenceModelForSharing getConfidenceRankedModelKeysGivenKeysToSort:]
- -[_PSConfidenceModelForSharing getConfidenceRankedModelKeysGivenKeysToSort:].cold.1
- -[_PSConfidenceModelForSharing initWithConfig:]
- -[_PSConfidenceModelForSharing init]
- -[_PSConfidenceModelForSharing setConfidenceModelDriver:]
- -[_PSConfidenceModelForSharing set_PSConfidenceModelInUse:]
- -[_PSContactFillerDataCollectionStatistics .cxx_destruct]
- -[_PSContactFillerDataCollectionStatistics addValue:]
- -[_PSContactFillerDataCollectionStatistics avg]
- -[_PSContactFillerDataCollectionStatistics calculateStats]
- -[_PSContactFillerDataCollectionStatistics initWithList:]
- -[_PSContactFillerDataCollectionStatistics list]
- -[_PSContactFillerDataCollectionStatistics max]
- -[_PSContactFillerDataCollectionStatistics min]
- -[_PSContactFillerDataCollectionStatistics setAvg:]
- -[_PSContactFillerDataCollectionStatistics setList:]
- -[_PSContactFillerDataCollectionStatistics setMax:]
- -[_PSContactFillerDataCollectionStatistics setMin:]
- -[_PSContactFillerDataCollectionStatistics setStdev:]
- -[_PSContactFillerDataCollectionStatistics stdev]
- -[_PSContactFillerNormalizationConstants .cxx_destruct]
- -[_PSContactFillerNormalizationConstants incomingCallTotal]
- -[_PSContactFillerNormalizationConstants incomingTextTotal]
- -[_PSContactFillerNormalizationConstants init]
- -[_PSContactFillerNormalizationConstants outgoingCallTotal]
- -[_PSContactFillerNormalizationConstants outgoingTextTotal]
- -[_PSContactFillerNormalizationConstants setIncomingCallTotal:]
- -[_PSContactFillerNormalizationConstants setIncomingTextTotal:]
- -[_PSContactFillerNormalizationConstants setOutgoingCallTotal:]
- -[_PSContactFillerNormalizationConstants setOutgoingTextTotal:]
- -[_PSContactFillerNormalizationConstants setShareTotal:]
- -[_PSContactFillerNormalizationConstants shareTotal]
- -[_PSContactFillerRecipient .cxx_destruct]
- -[_PSContactFillerRecipient ID]
- -[_PSContactFillerRecipient init]
- -[_PSContactFillerRecipient interaction]
- -[_PSContactFillerRecipient setID:]
- -[_PSContactFillerRecipient setInteraction:]
- -[_PSEnsembleModel addAdaptedModelUsageInfoToSuggestions:]
- -[_PSEnsembleModel computeEphemeralFeaturesWithPredictionContext:]
- -[_PSEnsembleModel confidenceModelForSharing]
- -[_PSEnsembleModel copyRemoteRuleMinerMLModel:]
- -[_PSEnsembleModel copyRemoteRuleMinerMLModel:].cold.1
- -[_PSEnsembleModel discardAdaptedModel]
- -[_PSEnsembleModel discardAdaptedModel].cold.1
- -[_PSEnsembleModel discardTrialModels]
- -[_PSEnsembleModel discardTrialModels].cold.1
- -[_PSEnsembleModel discardTrialModels].cold.2
- -[_PSEnsembleModel getLatestTrialMLModelVersion]
- -[_PSEnsembleModel getLatestTrialMLModelVersion].cold.1
- -[_PSEnsembleModel getOtherSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:].cold.4
- -[_PSEnsembleModel getPhotoBasedFeatures:]
- -[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]
- -[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:].cold.1
- -[_PSEnsembleModel getRuleMiningSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:]
- -[_PSEnsembleModel getRuleMiningSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:].cold.1
- -[_PSEnsembleModel loadDefaultAdaptableModelConfig]
- -[_PSEnsembleModel portraitContactStore]
- -[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:].cold.7
- -[_PSEnsembleModel psConfigForAdaptableModel]
- -[_PSEnsembleModel psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:]
- -[_PSEnsembleModel ruleMiningModel]
- -[_PSEnsembleModel setConfidenceModelForSharing:]
- -[_PSEnsembleModel setPeopleAnalysisFromAssetsWithPredictionContext:identifiersOfPeopleInPhotos:]
- -[_PSEnsembleModel setPhotoAnalysisFromAssetsWithPredictionContext:]
- -[_PSEnsembleModel setPortraitContactStore:]
- -[_PSEnsembleModel setPsConfigForAdaptableModel:]
- -[_PSEnsembleModel setRuleMiningModel:]
- -[_PSEnsembleModel setSharingContactRankerModel:]
- -[_PSEnsembleModel setTopicStore:]
- -[_PSEnsembleModel sharingContactRankerModel]
- -[_PSEnsembleModel topicStore]
- -[_PSEnsembleModel updateFactorLevels].cold.2
- -[_PSEnsembleModel validateCoreMLModelWithRawInput:predictionContext:]
- -[_PSFTZKWSuggestionsTransformerFactory filterIDSReachable]
- -[_PSFeatureStatistics .cxx_destruct]
- -[_PSFeatureStatistics addValue:]
- -[_PSFeatureStatistics avg]
- -[_PSFeatureStatistics calculateStats]
- -[_PSFeatureStatistics initWithList:]
- -[_PSFeatureStatistics list]
- -[_PSFeatureStatistics max]
- -[_PSFeatureStatistics min]
- -[_PSFeatureStatistics mode]
- -[_PSFeatureStatistics percentiles]
- -[_PSFeatureStatistics setAvg:]
- -[_PSFeatureStatistics setList:]
- -[_PSFeatureStatistics setMax:]
- -[_PSFeatureStatistics setMin:]
- -[_PSFeatureStatistics setMode:]
- -[_PSFeatureStatistics setPercentiles:]
- -[_PSFeatureStatistics setStdev:]
- -[_PSFeatureStatistics stdev]
- -[_PSFeaturizedBehaviorRule .cxx_destruct]
- -[_PSFeaturizedBehaviorRule features]
- -[_PSFeaturizedBehaviorRule initWithRule:score:features:]
- -[_PSFeaturizedBehaviorRule rule]
- -[_PSFeaturizedBehaviorRule score]
- -[_PSFeaturizedBehaviorRule setFeatures:]
- -[_PSFeaturizedBehaviorRule setRule:]
- -[_PSFeaturizedBehaviorRule setScore:]
- -[_PSHeuristics seedSuggestionsForChatGuidsAndTransports:]
- -[_PSHeuristics seedSuggestionsForChatGuidsAndTransports:].cold.1
- -[_PSKNNModel _featureVectorFromSuggestionDate:bundleID:peopleInPhotoIdentifiers:scenesInPhotoIdentifiers:]
- -[_PSPersonalizationEvaluation .cxx_destruct]
- -[_PSPersonalizationEvaluation _getDataStatistics:forData:]
- -[_PSPersonalizationEvaluation accuracyGainThresholdForSwap]
- -[_PSPersonalizationEvaluation adaptMLModel:withMLModelType:withDataArray:modelConfiguration:]
- -[_PSPersonalizationEvaluation adaptMLModel:withTrainingData:modelConfiguration:]
- -[_PSPersonalizationEvaluation adaptableModelConfiguration]
- -[_PSPersonalizationEvaluation adaptableModelDeployPath]
- -[_PSPersonalizationEvaluation adaptationStrategy]
- -[_PSPersonalizationEvaluation batchSize]
- -[_PSPersonalizationEvaluation cloneAdaptableModel:toFilePath:originalXgboostModelName:clonedXgboostModelName:]
- -[_PSPersonalizationEvaluation cloneAdaptableModel:toFilePath:originalXgboostModelName:clonedXgboostModelName:].cold.1
- -[_PSPersonalizationEvaluation createMLArrayBatchProviderWithMLModelType:withDataArray:]
- -[_PSPersonalizationEvaluation createMLFeatureProviderArrayFromSingleShareEventData:forMLModel:]
- -[_PSPersonalizationEvaluation curareEvaluationAndReporting]
- -[_PSPersonalizationEvaluation engagementRateGainThresholdForSwap]
- -[_PSPersonalizationEvaluation epoc]
- -[_PSPersonalizationEvaluation evaluateIsInvokedOnce]
- -[_PSPersonalizationEvaluation evaluateWithModel:]
- -[_PSPersonalizationEvaluation evaluateWithModel:].cold.1
- -[_PSPersonalizationEvaluation evaluationIterationCount]
- -[_PSPersonalizationEvaluation featureNameDict]
- -[_PSPersonalizationEvaluation generateCandidateModels]
- -[_PSPersonalizationEvaluation hyperparametersForCandidateModel:]
- -[_PSPersonalizationEvaluation initWithRecipe:knowledgeStore:shouldContinueBlock:]
- -[_PSPersonalizationEvaluation intermediateCompiledModelURL]
- -[_PSPersonalizationEvaluation knowledgeStore]
- -[_PSPersonalizationEvaluation learningRate]
- -[_PSPersonalizationEvaluation loadAdaptableModelUnderDirectory:]
- -[_PSPersonalizationEvaluation loadAdaptableModelUnderDirectory:].cold.1
- -[_PSPersonalizationEvaluation loadAdaptableModelUnderDirectory:].cold.2
- -[_PSPersonalizationEvaluation loadAdaptableModelUnderDirectory:].cold.3
- -[_PSPersonalizationEvaluation loadDefaultModel]
- -[_PSPersonalizationEvaluation loadDefaultModel].cold.1
- -[_PSPersonalizationEvaluation maxDepth]
- -[_PSPersonalizationEvaluation minChildWeight]
- -[_PSPersonalizationEvaluation minSampleCountForAdaptation]
- -[_PSPersonalizationEvaluation minimumTestDataSizeForSwap]
- -[_PSPersonalizationEvaluation modelTagToCandidateModel]
- -[_PSPersonalizationEvaluation modelTagToHyperparameters]
- -[_PSPersonalizationEvaluation numClasses]
- -[_PSPersonalizationEvaluation numTrees]
- -[_PSPersonalizationEvaluation performPrerequisitesBeforeAdaptationWithFeaturesConfigDeployPath:]
- -[_PSPersonalizationEvaluation personalizeModel:]
- -[_PSPersonalizationEvaluation personalizeModel:].cold.1
- -[_PSPersonalizationEvaluation processDataWithQuery:balanceNeed:]
- -[_PSPersonalizationEvaluation processDataWithQuery:balanceNeed:].cold.1
- -[_PSPersonalizationEvaluation psAdaptationDefaults]
- -[_PSPersonalizationEvaluation recipeID]
- -[_PSPersonalizationEvaluation recipe]
- -[_PSPersonalizationEvaluation results]
- -[_PSPersonalizationEvaluation runAdaptationAndEvaluationWithFeaturesConfigDeployPath:adaptableModelDeployPath:]
- -[_PSPersonalizationEvaluation runAdaptationAndEvaluationWithFeaturesConfigDeployPath:adaptableModelDeployPath:].cold.1
- -[_PSPersonalizationEvaluation runAdaptationAndEvaluationWithFeaturesConfigDeployPath:adaptableModelDeployPath:].cold.2
- -[_PSPersonalizationEvaluation runAdaptationAndEvaluation]
- -[_PSPersonalizationEvaluation selectedFeaturesConfig]
- -[_PSPersonalizationEvaluation setAccuracyGainThresholdForSwap:]
- -[_PSPersonalizationEvaluation setAdaptableModelConfiguration:]
- -[_PSPersonalizationEvaluation setAdaptableModelDeployPath:]
- -[_PSPersonalizationEvaluation setAdaptationStrategy:]
- -[_PSPersonalizationEvaluation setBatchSize:]
- -[_PSPersonalizationEvaluation setCurareEvaluationAndReporting:]
- -[_PSPersonalizationEvaluation setEngagementRateGainThresholdForSwap:]
- -[_PSPersonalizationEvaluation setEpoc:]
- -[_PSPersonalizationEvaluation setEvaluateIsInvokedOnce:]
- -[_PSPersonalizationEvaluation setEvaluationIterationCount:]
- -[_PSPersonalizationEvaluation setFeatureNameDict:]
- -[_PSPersonalizationEvaluation setIntermediateCompiledModelURL:]
- -[_PSPersonalizationEvaluation setKnowledgeStore:]
- -[_PSPersonalizationEvaluation setLastDayOfAdaptation:]
- -[_PSPersonalizationEvaluation setLearningRate:]
- -[_PSPersonalizationEvaluation setMaxDepth:]
- -[_PSPersonalizationEvaluation setMinChildWeight:]
- -[_PSPersonalizationEvaluation setMinSampleCountForAdaptation:]
- -[_PSPersonalizationEvaluation setMinimumTestDataSizeForSwap:]
- -[_PSPersonalizationEvaluation setModelTagToCandidateModel:]
- -[_PSPersonalizationEvaluation setModelTagToHyperparameters:]
- -[_PSPersonalizationEvaluation setNumClasses:]
- -[_PSPersonalizationEvaluation setNumTrees:]
- -[_PSPersonalizationEvaluation setParametersForHyperparmeters:]
- -[_PSPersonalizationEvaluation setParametersFromRecipeForCandidateModel:]
- -[_PSPersonalizationEvaluation setParametersFromRecipe]
- -[_PSPersonalizationEvaluation setPsAdaptationDefaults:]
- -[_PSPersonalizationEvaluation setRecipeID:]
- -[_PSPersonalizationEvaluation setResults:]
- -[_PSPersonalizationEvaluation setSelectedFeaturesConfig:]
- -[_PSPersonalizationEvaluation setShouldContinue:]
- -[_PSPersonalizationEvaluation setSwapOK:]
- -[_PSPersonalizationEvaluation setTestSplitPercent:]
- -[_PSPersonalizationEvaluation setTopN:]
- -[_PSPersonalizationEvaluation shouldContinue]
- -[_PSPersonalizationEvaluation swapOK]
- -[_PSPersonalizationEvaluation testSplitPercent]
- -[_PSPersonalizationEvaluation topN]
- -[_PSPersonalizationEvaluation updateAdaptableModelConfigWithUpdateType:numTrees:]
- -[_PSPersonalizationEvaluation updateMLModelWithURL:withMLModelType:withDataArray:modelConfiguration:]
- -[_PSPredictionContext scenesInPhotoIdentifiers]
- -[_PSPredictionContext setScenesInPhotoIdentifiers:]
- -[_PSRuleMiningModel .cxx_destruct]
- -[_PSRuleMiningModel _PSRuleMiningIsAdaptedMLModelOK]
- -[_PSRuleMiningModel _PSRuleMiningIsMLModelInUse]
- -[_PSRuleMiningModel _PSRuleMiningMLModelScoreThreshold]
- -[_PSRuleMiningModel _PSRuleMiningModelDaysToPromoteRecentlyInstalledAppExtensions]
- -[_PSRuleMiningModel _PSRuleMiningModelMinRuleConfidenceForSuggestion]
- -[_PSRuleMiningModel _PSRuleMiningModelMinSupportForSuggestion]
- -[_PSRuleMiningModel _PSRuleMiningModelRegularizingContextOverlapConstraint]
- -[_PSRuleMiningModel behaviorRetriever]
- -[_PSRuleMiningModel behaviorRulesConsideringInTheContext]
- -[_PSRuleMiningModel contactResolver]
- -[_PSRuleMiningModel extractAdaptedModelRecipeID]
- -[_PSRuleMiningModel filterByRegularizingRules:invalidatedByAnyConflictingItems:containingItemTypes:]
- -[_PSRuleMiningModel filterByRegularizingRulesByContextOverlap:regulularizeItems:queryItems:regularizationConstraint:]
- -[_PSRuleMiningModel initWithKnowledgeStore:contactresolver:withConfig:]
- -[_PSRuleMiningModel isAdaptedModelCreated]
- -[_PSRuleMiningModel isAdaptedModelUsed]
- -[_PSRuleMiningModel knowledgeStore]
- -[_PSRuleMiningModel loadMLModel]
- -[_PSRuleMiningModel psConfigForAdaptableModel]
- -[_PSRuleMiningModel ruleRankingModel]
- -[_PSRuleMiningModel scores]
- -[_PSRuleMiningModel setBehaviorRulesConsideringInTheContext:]
- -[_PSRuleMiningModel setPsConfigForAdaptableModel:]
- -[_PSRuleMiningModel setRuleRankingModel:]
- -[_PSRuleMiningModel setScores:]
- -[_PSRuleMiningModel set_PSRuleMiningIsAdaptedMLModelOK:]
- -[_PSRuleMiningModel set_PSRuleMiningIsMLModelInUse:]
- -[_PSRuleMiningModel set_PSRuleMiningMLModelScoreThreshold:]
- -[_PSRuleMiningModel set_PSRuleMiningModelDaysToPromoteRecentlyInstalledAppExtensions:]
- -[_PSRuleMiningModel set_PSRuleMiningModelMinRuleConfidenceForSuggestion:]
- -[_PSRuleMiningModel set_PSRuleMiningModelMinSupportForSuggestion:]
- -[_PSRuleMiningModel set_PSRuleMiningModelRegularizingContextOverlapConstraint:]
- -[_PSRuleMiningModel shareExtensionSuggestionsFromContext:]
- -[_PSRuleMiningModel suggestionArrayWithArray:appendingUniqueElementsByBundleIdFromArray:]
- -[_PSRuleMiningModel suggestionProxiesWithPredictionContext:photoSuggestedPeople:supportedBundleIDs:]
- -[_PSRuleMiningModel suggestionProxiesWithPredictionContext:photoSuggestedPeople:supportedBundleIDs:].cold.1
- -[_PSRuleMiningModel updateAdaptableModelProperties:]
- -[_PSRuleMiningModel updateModelProperties:]
- -[_PSRuleOverlapFeedback .cxx_destruct]
- -[_PSRuleOverlapFeedback behaviorRetriever]
- -[_PSRuleOverlapFeedback bucketedValue:]
- -[_PSRuleOverlapFeedback confidenceModelForSharing]
- -[_PSRuleOverlapFeedback constantFeaturesFromContextItems:]
- -[_PSRuleOverlapFeedback constantPETFeaturesFromContextItems:]
- -[_PSRuleOverlapFeedback contactStore]
- -[_PSRuleOverlapFeedback contextItemsFromEvent:]
- -[_PSRuleOverlapFeedback contextItemsFromEvent:].cold.1
- -[_PSRuleOverlapFeedback contextItemsFromEvent:].cold.2
- -[_PSRuleOverlapFeedback feedbackPETPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]
- -[_PSRuleOverlapFeedback feedbackPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]
- -[_PSRuleOverlapFeedback getSessionID]
- -[_PSRuleOverlapFeedback init]
- -[_PSRuleOverlapFeedback interactionStoreEventsSinceDate:]
- -[_PSRuleOverlapFeedback interactionStoreEventsSinceDate:].cold.1
- -[_PSRuleOverlapFeedback interactionStore]
- -[_PSRuleOverlapFeedback knowledgeStore]
- -[_PSRuleOverlapFeedback loggingForKnowledgeStoreEvent:WithMatchingInteraction:]
- -[_PSRuleOverlapFeedback loggingForKnowledgeStoreEvent:WithMatchingInteraction:].cold.1
- -[_PSRuleOverlapFeedback loggingTrainDataForContactFillerModel:withMatchingInteraction:interactionRecipients:ruleRankingModel:contactPropertyCache:interactionCache:]
- -[_PSRuleOverlapFeedback loggingTrainDataForContactFillerModel:withMatchingInteraction:interactionRecipients:ruleRankingModel:contactPropertyCache:interactionCache:].cold.1
- -[_PSRuleOverlapFeedback loggingTrainDataForContactFillerModel:withMatchingInteraction:interactionRecipients:ruleRankingModel:contactPropertyCache:interactionCache:].cold.2
- -[_PSRuleOverlapFeedback matchFeedbackEvent:WithInteractions:]
- -[_PSRuleOverlapFeedback modelAccuracyLogging:WithMatchingInteraction:]
- -[_PSRuleOverlapFeedback modelAccuracyLogging:WithMatchingInteraction:].cold.1
- -[_PSRuleOverlapFeedback reviewLastDayOfShares]
- -[_PSRuleOverlapFeedback reviewLastDayOfShares].cold.1
- -[_PSRuleOverlapFeedback reviewLastDayOfShares].cold.2
- -[_PSRuleOverlapFeedback reviewLastDayOfShares].cold.3
- -[_PSRuleOverlapFeedback reviewLastDayOfShares].cold.4
- -[_PSRuleOverlapFeedback ruleOverlapFeedbackDefaults]
- -[_PSRuleOverlapFeedback ruleRankingModel]
- -[_PSRuleOverlapFeedback scoreRanking:forModelKey:]
- -[_PSRuleOverlapFeedback setConfidenceModelForSharing:]
- -[_PSRuleOverlapFeedback setContactStore:]
- -[_PSRuleOverlapFeedback setInteractionStore:]
- -[_PSRuleOverlapFeedback setKnowledgeStore:]
- -[_PSRuleOverlapFeedback setRuleOverlapFeedbackDefaults:]
- -[_PSRuleOverlapFeedback setRuleRankingModel:]
- -[_PSRuleOverlapFeedback sharesheetFeedbackEventsSinceDate:]
- -[_PSRuleOverlapFeedback targetAppPredictedCorrectlyByRule:bundleId:]
- -[_PSRuleOverlapFeedback wasInteractionAmongSuggestLess:]
- -[_PSRuleOverlapFeedback writeRecordObjcWithData:]
- -[_PSRuleRankingMLModel .cxx_destruct]
- -[_PSRuleRankingMLModel adaptableModelConfiguration]
- -[_PSRuleRankingMLModel adaptedModelRecipeVersion]
- -[_PSRuleRankingMLModel extractAdaptedModelRecipeID]
- -[_PSRuleRankingMLModel feaExtHandle]
- -[_PSRuleRankingMLModel getAdaptedModelVersion]
- -[_PSRuleRankingMLModel giveModelDescription]
- -[_PSRuleRankingMLModel initWithAdaptableModelConfig:isAdaptedMLModelOK:scoreThreshold:]
- -[_PSRuleRankingMLModel initWithMLModel:scoreThreshold:isAdaptedModel:psConfigForAdaptableModel:isAdaptedMLModelOK:]
- -[_PSRuleRankingMLModel isAdaptedMLModelOK]
- -[_PSRuleRankingMLModel isAdaptedModelCreated]
- -[_PSRuleRankingMLModel isAdaptedModelUsed]
- -[_PSRuleRankingMLModel isAdaptedModel]
- -[_PSRuleRankingMLModel loadDefaultRuleMinerMLModel]
- -[_PSRuleRankingMLModel metadata]
- -[_PSRuleRankingMLModel mlModel]
- -[_PSRuleRankingMLModel psConfigForAdaptableModel]
- -[_PSRuleRankingMLModel rankRules:contextItems:]
- -[_PSRuleRankingMLModel scoreThreshold]
- -[_PSRuleRankingMLModel scoresOnRules:contextItems:]
- -[_PSRuleRankingMLModel scores]
- -[_PSRuleRankingMLModel setAdaptableModelConfiguration:]
- -[_PSRuleRankingMLModel setAdaptedModelRecipeVersion:]
- -[_PSRuleRankingMLModel setFeaExtHandle:]
- -[_PSRuleRankingMLModel setIsAdaptedMLModelOK:]
- -[_PSRuleRankingMLModel setIsAdaptedModel:]
- -[_PSRuleRankingMLModel setMetadata:]
- -[_PSRuleRankingMLModel setMlModel:]
- -[_PSRuleRankingMLModel setPsConfigForAdaptableModel:]
- -[_PSRuleRankingMLModel setScoreThreshold:]
- -[_PSRuleRankingMLModel setScores:]
- -[_PSSharingContactFeatureExtraction .cxx_destruct]
- -[_PSSharingContactFeatureExtraction behaviorRetriever]
- -[_PSSharingContactFeatureExtraction constantFeaturesReady]
- -[_PSSharingContactFeatureExtraction constantFeatures]
- -[_PSSharingContactFeatureExtraction extractConstantFeaturesInto:]
- -[_PSSharingContactFeatureExtraction extractConstantFeaturesInto:].cold.1
- -[_PSSharingContactFeatureExtraction extractConstantFeaturesInto:].cold.2
- -[_PSSharingContactFeatureExtraction extractConstantFeaturesInto:].cold.3
- -[_PSSharingContactFeatureExtraction extractConstantFeaturesInto:].cold.4
- -[_PSSharingContactFeatureExtraction extractConstantFeaturesInto:].cold.5
- -[_PSSharingContactFeatureExtraction extractConstantFeaturesInto:].cold.6
- -[_PSSharingContactFeatureExtraction extractFeaturesInto:withPredictionContext:forContactId:forInteraction:behaviorRulesConsideringInTheContext:ruleRankingMLModelScores:interactionModelScores:]
- -[_PSSharingContactFeatureExtraction initWithMetadata:interactionStore:]
- -[_PSSharingContactFeatureExtraction interactionStore]
- -[_PSSharingContactFeatureExtraction metadata]
- -[_PSSharingContactFeatureExtraction normConstants]
- -[_PSSharingContactFeatureExtraction setConstantFeatures:]
- -[_PSSharingContactFeatureExtraction setConstantFeaturesReady:]
- -[_PSSharingContactFeatureExtraction setMetadata:]
- -[_PSSharingContactFeatureExtraction setNormConstants:]
- -[_PSSharingContactFeatureExtraction setUserEvent:]
- -[_PSSharingContactFeatureExtraction transferConstantFeatures:to:]
- -[_PSSharingContactFeatureExtraction userEvent]
- -[_PSSharingContactRankerMLModel .cxx_destruct]
- -[_PSSharingContactRankerMLModel giveModelDescription]
- -[_PSSharingContactRankerMLModel initWithMLModel:scoreThreshold:]
- -[_PSSharingContactRankerMLModel initWithScoreThreshold:]
- -[_PSSharingContactRankerMLModel loadDefaultModel]
- -[_PSSharingContactRankerMLModel loadDefaultModel].cold.1
- -[_PSSharingContactRankerMLModel metadata]
- -[_PSSharingContactRankerMLModel mlModel]
- -[_PSSharingContactRankerMLModel scoreThreshold]
- -[_PSSharingContactRankerMLModel scoresOnFeatures:]
- -[_PSSharingContactRankerMLModel setMetadata:]
- -[_PSSharingContactRankerMLModel setMlModel:]
- -[_PSSharingContactRankerMLModel setScoreThreshold:]
- -[_PSSharingContactRankerModel .cxx_destruct]
- -[_PSSharingContactRankerModel _PSSharingContactRankerMLModelInUse]
- -[_PSSharingContactRankerModel _PSSharingContactRankerMLModelScoreThreshold]
- -[_PSSharingContactRankerModel feaExtractionHandle]
- -[_PSSharingContactRankerModel initWithInteractionStore:messageInteractionCache:shareInteractionCache:]
- -[_PSSharingContactRankerModel interactionStore]
- -[_PSSharingContactRankerModel loadMLModel]
- -[_PSSharingContactRankerModel loadMLModel].cold.1
- -[_PSSharingContactRankerModel messageInteractionCache]
- -[_PSSharingContactRankerModel setFeaExtractionHandle:]
- -[_PSSharingContactRankerModel setMessageInteractionCache:]
- -[_PSSharingContactRankerModel setShareInteractionCache:]
- -[_PSSharingContactRankerModel setSharingContactRankerMLModel:]
- -[_PSSharingContactRankerModel set_PSSharingContactRankerMLModelInUse:]
- -[_PSSharingContactRankerModel set_PSSharingContactRankerMLModelScoreThreshold:]
- -[_PSSharingContactRankerModel shareInteractionCache]
- -[_PSSharingContactRankerModel sharingContactRankerMLModel]
- -[_PSSharingContactRankerModel suggestionProxiesWithPredictionContext:supportedBundleIDs:behaviorRulesConsideringInTheContext:interactionModelSuggestions:ruleRankingMLModelScores:]
- -[_PSSharingContactRankerModel suggestionProxiesWithPredictionContext:supportedBundleIDs:behaviorRulesConsideringInTheContext:interactionModelSuggestions:ruleRankingMLModelScores:].cold.1
- -[_PSSharingContactRankerModel suggestionProxiesWithPredictionContext:supportedBundleIDs:behaviorRulesConsideringInTheContext:interactionModelSuggestions:ruleRankingMLModelScores:].cold.2
- -[_PSSharingContactRankerModel updateModelProperties:]
- -[_PSSharingContactRankerModel updateModelProperties:].cold.1
- -[_PSSharingContactRankerScoredContact .cxx_destruct]
- -[_PSSharingContactRankerScoredContact initWithScore:interaction:]
- -[_PSSharingContactRankerScoredContact interaction]
- -[_PSSharingContactRankerScoredContact score]
- -[_PSSharingContactRankerScoredContact setInteraction:]
- -[_PSSharingContactRankerScoredContact setScore:]
- -[_PSSuggester computeShareSheetEphemeralFeaturesWithPredictionContext:]
- -[_PSSuggester computeShareSheetEphemeralFeaturesWithPredictionContext:].cold.1
- -[_PSSuggester getCacheSuggestions]
- -[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]
- -[evaluatedRule .cxx_destruct]
- -[evaluatedRule compare:]
- -[evaluatedRule initWithLabel:score:recipientUniqueID:]
- -[evaluatedRule recipientUniqueID]
- -[evaluatedRule ruleLabel]
- -[evaluatedRule ruleScore]
- -[evaluatedRule setRecipientUniqueID:]
- -[evaluatedRule setRuleLabel:]
- -[evaluatedRule setRuleScore:]
- -[scoredModel .cxx_destruct]
- -[scoredModel compare:]
- -[scoredModel initWithModelKey:score:]
- -[scoredModel modelKey]
- -[scoredModel score]
- -[scoredModel setModelKey:]
- -[scoredModel setScore:]
- -[scoredRule .cxx_destruct]
- -[scoredRule compare:]
- -[scoredRule initWithLabel:score:recipientUniqueID:]
- -[scoredRule recipientUniqueID]
- -[scoredRule ruleLabel]
- -[scoredRule ruleScore]
- -[scoredRule setRecipientUniqueID:]
- -[scoredRule setRuleLabel:]
- -[scoredRule setRuleScore:]
- GCC_except_table107
- GCC_except_table108
- GCC_except_table111
- GCC_except_table147
- GCC_except_table148
- GCC_except_table149
- GCC_except_table154
- GCC_except_table173
- GCC_except_table322
- GCC_except_table324
- GCC_except_table33
- GCC_except_table333
- GCC_except_table37
- GCC_except_table41
- GCC_except_table43
- GCC_except_table44
- GCC_except_table50
- GCC_except_table58
- GCC_except_table59
- GCC_except_table81
- GCC_except_table84
- GCC_except_table86
- GCC_except_table99
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._confidence
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._contentUrlInContext
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._contentUrlInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._contentUrlOverlap
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._has
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._highConfidenceRuleCount
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._isWeekendInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._isWeekendOverlap
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._lOIInContext
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._lOIInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._lOIOverlap
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._locationOfInterestContainingRuleCount
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._locationOfInterestRulesCardinality
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._lowConfidenceRuleCount
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._mediumConfidenceRuleCount
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._personAndAppMatched
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._personMatched
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoContactContainingRuleCount
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoContactInContext
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoContactInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoContactOverlap
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoContactRulesCardinality
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoSceneContainingRuleCount
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoSceneInContext
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoSceneInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoSceneOverlap
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._photoSceneRulesCardinality
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._sessionId
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._sourceBundleIdContainingRuleCount
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._sourceBundleIdInContext
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._sourceBundleIdInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._sourceBundleIdOverlap
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._sourceBundleIdRulesCardinality
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._support
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._targetBundleIDInConsequent
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._targetBundleIdContainingRuleCount
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._targetBundleIdInContext
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._targetBundleIdInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._targetBundleIdOverlap
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._targetBundleIdRulesCardinality
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._timeOfDaySlotInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._timeOfDaySlotOverlap
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._topicContainingRuleCount
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._topicInContext
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._topicInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._topicOverlap
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._topicRulesCardinality
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._totalMessagesRecieved
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._totalMessagesSent
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._totalShares
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._uniqueShareEventIdentifier
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._utiTypeInContext
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._utiTypeInRule
- OBJC_IVAR_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent._utiTypeOverlap
- OBJC_IVAR_$_PBDataReader._bytes
- OBJC_IVAR_$_PBDataReader._error
- OBJC_IVAR_$_PBDataReader._length
- OBJC_IVAR_$_PBDataReader._pos
- _Adaptable
- _All
- _BehaviorMinerLibraryCore
- _BehaviorMinerLibraryCore.frameworkLibrary
- _Classic
- _CoreBehaviorAnalysisPETCoreBehaviorAnalysisEventReadFrom
- _CoreDuetLibraryCore
- _CoreDuetLibraryCore.frameworkLibrary
- _DistributedEvaluationLibraryCore.frameworkLibrary
- _MLRuntimeLibraryCore.frameworkLibrary
- _NSLog
- _NSTemporaryDirectory
- _OBJC_CLASS_$_BMPeopleSuggesterSuggestLessFeedback
- _OBJC_CLASS_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent
- _OBJC_CLASS_$_FidesPHSEvaluatorDataSource
- _OBJC_CLASS_$_GBDTEvaluator
- _OBJC_CLASS_$_LighthouseShareSheetPFLTraining
- _OBJC_CLASS_$_ModelHyperparameters
- _OBJC_CLASS_$_NSNumberFormatter
- _OBJC_CLASS_$_PSDESPlugin
- _OBJC_CLASS_$__DKBehavioralRuleFeaturesMetadataKey
- _OBJC_CLASS_$__PSBehaviorRuleFeatureExtraction
- _OBJC_CLASS_$__PSBehaviorRuleRankingUtilities
- _OBJC_CLASS_$__PSConfidenceModel
- _OBJC_CLASS_$__PSConfidenceModelArchive
- _OBJC_CLASS_$__PSConfidenceModelDriver
- _OBJC_CLASS_$__PSConfidenceModelForSharing
- _OBJC_CLASS_$__PSContactFillerDataCollectionStatistics
- _OBJC_CLASS_$__PSContactFillerDataCollectionUtilities
- _OBJC_CLASS_$__PSContactFillerNormalizationConstants
- _OBJC_CLASS_$__PSContactFillerRecipient
- _OBJC_CLASS_$__PSFeatureStatistics
- _OBJC_CLASS_$__PSFeaturizedBehaviorRule
- _OBJC_CLASS_$__PSPersonalizationEvaluation
- _OBJC_CLASS_$__PSRuleMiningModel
- _OBJC_CLASS_$__PSRuleOverlapFeedback
- _OBJC_CLASS_$__PSRuleRankingMLModel
- _OBJC_CLASS_$__PSSharingContactFeatureExtraction
- _OBJC_CLASS_$__PSSharingContactRankerMLModel
- _OBJC_CLASS_$__PSSharingContactRankerModel
- _OBJC_CLASS_$__PSSharingContactRankerScoredContact
- _OBJC_CLASS_$_evaluatedRule
- _OBJC_CLASS_$_scoredModel
- _OBJC_CLASS_$_scoredRule
- _OBJC_IVAR_$_FidesPHSEvaluatorDataSource._inputVectors
- _OBJC_IVAR_$_FidesPHSEvaluatorDataSource._recipe
- _OBJC_IVAR_$_FidesPHSEvaluatorDataSource._recordDatas
- _OBJC_IVAR_$_FidesPHSEvaluatorDataSource._recordInfos
- _OBJC_IVAR_$_FidesPHSEvaluatorDataSource._records
- _OBJC_IVAR_$_FidesPHSEvaluatorDataSource._targetVector
- _OBJC_IVAR_$_LighthouseShareSheetPFLTraining._configBoltTaskIDSpecification
- _OBJC_IVAR_$_LighthouseShareSheetPFLTraining._configDepthSpecification
- _OBJC_IVAR_$_LighthouseShareSheetPFLTraining._configTreeSpecification
- _OBJC_IVAR_$_LighthouseShareSheetPFLTraining._dataSource
- _OBJC_IVAR_$_LighthouseShareSheetPFLTraining._featureMatricesForAllShareEvents
- _OBJC_IVAR_$_LighthouseShareSheetPFLTraining._featureNameDict
- _OBJC_IVAR_$_LighthouseShareSheetPFLTraining._knowledgeStore
- _OBJC_IVAR_$_LighthouseShareSheetPFLTraining._processDataReturnDict
- _OBJC_IVAR_$_LighthouseShareSheetPFLTraining._selectedFeaturesConfig
- _OBJC_IVAR_$_ModelHyperparameters._adaptationStrategy
- _OBJC_IVAR_$_ModelHyperparameters._learningRate
- _OBJC_IVAR_$_ModelHyperparameters._minChildWeight
- _OBJC_IVAR_$_ModelHyperparameters._numTrees
- _OBJC_IVAR_$_PSDESPlugin._knowledgeStore
- _OBJC_IVAR_$__PSBehaviorRuleFeatureExtraction._behaviorRetriever
- _OBJC_IVAR_$__PSBehaviorRuleFeatureExtraction._constantFeatures
- _OBJC_IVAR_$__PSBehaviorRuleFeatureExtraction._constantFeaturesReady
- _OBJC_IVAR_$__PSBehaviorRuleFeatureExtraction._contextFeatures
- _OBJC_IVAR_$__PSBehaviorRuleFeatureExtraction._contextFeaturesReady
- _OBJC_IVAR_$__PSBehaviorRuleFeatureExtraction._interactionStore
- _OBJC_IVAR_$__PSBehaviorRuleFeatureExtraction._metadata
- _OBJC_IVAR_$__PSConfidenceModel._bufferHead
- _OBJC_IVAR_$__PSConfidenceModel._bufferSize
- _OBJC_IVAR_$__PSConfidenceModel._circularBuffer
- _OBJC_IVAR_$__PSConfidenceModel._minimumInstanceCount
- _OBJC_IVAR_$__PSConfidenceModel._sum
- _OBJC_IVAR_$__PSConfidenceModelArchive._confidenceModelDictionary
- _OBJC_IVAR_$__PSConfidenceModelDriver._confidenceModelDictionary
- _OBJC_IVAR_$__PSConfidenceModelForSharing.__PSConfidenceModelInUse
- _OBJC_IVAR_$__PSConfidenceModelForSharing._confidenceModelDriver
- _OBJC_IVAR_$__PSContactFillerDataCollectionStatistics._avg
- _OBJC_IVAR_$__PSContactFillerDataCollectionStatistics._list
- _OBJC_IVAR_$__PSContactFillerDataCollectionStatistics._max
- _OBJC_IVAR_$__PSContactFillerDataCollectionStatistics._min
- _OBJC_IVAR_$__PSContactFillerDataCollectionStatistics._stdev
- _OBJC_IVAR_$__PSContactFillerNormalizationConstants._incomingCallTotal
- _OBJC_IVAR_$__PSContactFillerNormalizationConstants._incomingTextTotal
- _OBJC_IVAR_$__PSContactFillerNormalizationConstants._outgoingCallTotal
- _OBJC_IVAR_$__PSContactFillerNormalizationConstants._outgoingTextTotal
- _OBJC_IVAR_$__PSContactFillerNormalizationConstants._shareTotal
- _OBJC_IVAR_$__PSContactFillerRecipient._ID
- _OBJC_IVAR_$__PSContactFillerRecipient._interaction
- _OBJC_IVAR_$__PSEnsembleModel._confidenceModelForSharing
- _OBJC_IVAR_$__PSEnsembleModel._portraitContactStore
- _OBJC_IVAR_$__PSEnsembleModel._psConfigForAdaptableModel
- _OBJC_IVAR_$__PSEnsembleModel._ruleMiningModel
- _OBJC_IVAR_$__PSEnsembleModel._sharingContactRankerModel
- _OBJC_IVAR_$__PSEnsembleModel._topicStore
- _OBJC_IVAR_$__PSFeatureStatistics._avg
- _OBJC_IVAR_$__PSFeatureStatistics._list
- _OBJC_IVAR_$__PSFeatureStatistics._max
- _OBJC_IVAR_$__PSFeatureStatistics._min
- _OBJC_IVAR_$__PSFeatureStatistics._mode
- _OBJC_IVAR_$__PSFeatureStatistics._percentiles
- _OBJC_IVAR_$__PSFeatureStatistics._stdev
- _OBJC_IVAR_$__PSFeaturizedBehaviorRule._features
- _OBJC_IVAR_$__PSFeaturizedBehaviorRule._rule
- _OBJC_IVAR_$__PSFeaturizedBehaviorRule._score
- _OBJC_IVAR_$__PSPersonalizationEvaluation._accuracyGainThresholdForSwap
- _OBJC_IVAR_$__PSPersonalizationEvaluation._adaptableModelConfiguration
- _OBJC_IVAR_$__PSPersonalizationEvaluation._adaptableModelDeployPath
- _OBJC_IVAR_$__PSPersonalizationEvaluation._adaptationStrategy
- _OBJC_IVAR_$__PSPersonalizationEvaluation._batchSize
- _OBJC_IVAR_$__PSPersonalizationEvaluation._curareEvaluationAndReporting
- _OBJC_IVAR_$__PSPersonalizationEvaluation._engagementRateGainThresholdForSwap
- _OBJC_IVAR_$__PSPersonalizationEvaluation._epoc
- _OBJC_IVAR_$__PSPersonalizationEvaluation._evaluateIsInvokedOnce
- _OBJC_IVAR_$__PSPersonalizationEvaluation._evaluationIterationCount
- _OBJC_IVAR_$__PSPersonalizationEvaluation._featureNameDict
- _OBJC_IVAR_$__PSPersonalizationEvaluation._intermediateCompiledModelURL
- _OBJC_IVAR_$__PSPersonalizationEvaluation._knowledgeStore
- _OBJC_IVAR_$__PSPersonalizationEvaluation._learningRate
- _OBJC_IVAR_$__PSPersonalizationEvaluation._maxDepth
- _OBJC_IVAR_$__PSPersonalizationEvaluation._minChildWeight
- _OBJC_IVAR_$__PSPersonalizationEvaluation._minSampleCountForAdaptation
- _OBJC_IVAR_$__PSPersonalizationEvaluation._minimumTestDataSizeForSwap
- _OBJC_IVAR_$__PSPersonalizationEvaluation._modelTagToCandidateModel
- _OBJC_IVAR_$__PSPersonalizationEvaluation._modelTagToHyperparameters
- _OBJC_IVAR_$__PSPersonalizationEvaluation._numClasses
- _OBJC_IVAR_$__PSPersonalizationEvaluation._numTrees
- _OBJC_IVAR_$__PSPersonalizationEvaluation._psAdaptationDefaults
- _OBJC_IVAR_$__PSPersonalizationEvaluation._recipe
- _OBJC_IVAR_$__PSPersonalizationEvaluation._recipeID
- _OBJC_IVAR_$__PSPersonalizationEvaluation._results
- _OBJC_IVAR_$__PSPersonalizationEvaluation._selectedFeaturesConfig
- _OBJC_IVAR_$__PSPersonalizationEvaluation._shouldContinue
- _OBJC_IVAR_$__PSPersonalizationEvaluation._swapOK
- _OBJC_IVAR_$__PSPersonalizationEvaluation._testSplitPercent
- _OBJC_IVAR_$__PSPersonalizationEvaluation._topN
- _OBJC_IVAR_$__PSPredictionContext._scenesInPhotoIdentifiers
- _OBJC_IVAR_$__PSRuleMiningModel.__PSRuleMiningIsAdaptedMLModelOK
- _OBJC_IVAR_$__PSRuleMiningModel.__PSRuleMiningIsMLModelInUse
- _OBJC_IVAR_$__PSRuleMiningModel.__PSRuleMiningMLModelScoreThreshold
- _OBJC_IVAR_$__PSRuleMiningModel.__PSRuleMiningModelDaysToPromoteRecentlyInstalledAppExtensions
- _OBJC_IVAR_$__PSRuleMiningModel.__PSRuleMiningModelMinRuleConfidenceForSuggestion
- _OBJC_IVAR_$__PSRuleMiningModel.__PSRuleMiningModelMinSupportForSuggestion
- _OBJC_IVAR_$__PSRuleMiningModel.__PSRuleMiningModelRegularizingContextOverlapConstraint
- _OBJC_IVAR_$__PSRuleMiningModel._behaviorRetriever
- _OBJC_IVAR_$__PSRuleMiningModel._behaviorRulesConsideringInTheContext
- _OBJC_IVAR_$__PSRuleMiningModel._contactResolver
- _OBJC_IVAR_$__PSRuleMiningModel._knowledgeStore
- _OBJC_IVAR_$__PSRuleMiningModel._psConfigForAdaptableModel
- _OBJC_IVAR_$__PSRuleMiningModel._ruleRankingModel
- _OBJC_IVAR_$__PSRuleMiningModel._scores
- _OBJC_IVAR_$__PSRuleOverlapFeedback._behaviorRetriever
- _OBJC_IVAR_$__PSRuleOverlapFeedback._confidenceModelForSharing
- _OBJC_IVAR_$__PSRuleOverlapFeedback._contactStore
- _OBJC_IVAR_$__PSRuleOverlapFeedback._interactionStore
- _OBJC_IVAR_$__PSRuleOverlapFeedback._knowledgeStore
- _OBJC_IVAR_$__PSRuleOverlapFeedback._ruleOverlapFeedbackDefaults
- _OBJC_IVAR_$__PSRuleOverlapFeedback._ruleRankingModel
- _OBJC_IVAR_$__PSRuleRankingMLModel._adaptableModelConfiguration
- _OBJC_IVAR_$__PSRuleRankingMLModel._adaptedModelRecipeVersion
- _OBJC_IVAR_$__PSRuleRankingMLModel._feaExtHandle
- _OBJC_IVAR_$__PSRuleRankingMLModel._isAdaptedMLModelOK
- _OBJC_IVAR_$__PSRuleRankingMLModel._isAdaptedModel
- _OBJC_IVAR_$__PSRuleRankingMLModel._metadata
- _OBJC_IVAR_$__PSRuleRankingMLModel._mlModel
- _OBJC_IVAR_$__PSRuleRankingMLModel._psConfigForAdaptableModel
- _OBJC_IVAR_$__PSRuleRankingMLModel._scoreThreshold
- _OBJC_IVAR_$__PSRuleRankingMLModel._scores
- _OBJC_IVAR_$__PSSharingContactFeatureExtraction._behaviorRetriever
- _OBJC_IVAR_$__PSSharingContactFeatureExtraction._constantFeatures
- _OBJC_IVAR_$__PSSharingContactFeatureExtraction._constantFeaturesReady
- _OBJC_IVAR_$__PSSharingContactFeatureExtraction._interactionStore
- _OBJC_IVAR_$__PSSharingContactFeatureExtraction._metadata
- _OBJC_IVAR_$__PSSharingContactFeatureExtraction._normConstants
- _OBJC_IVAR_$__PSSharingContactFeatureExtraction._userEvent
- _OBJC_IVAR_$__PSSharingContactRankerMLModel._metadata
- _OBJC_IVAR_$__PSSharingContactRankerMLModel._mlModel
- _OBJC_IVAR_$__PSSharingContactRankerMLModel._scoreThreshold
- _OBJC_IVAR_$__PSSharingContactRankerModel.__PSSharingContactRankerMLModelInUse
- _OBJC_IVAR_$__PSSharingContactRankerModel.__PSSharingContactRankerMLModelScoreThreshold
- _OBJC_IVAR_$__PSSharingContactRankerModel._feaExtractionHandle
- _OBJC_IVAR_$__PSSharingContactRankerModel._interactionStore
- _OBJC_IVAR_$__PSSharingContactRankerModel._messageInteractionCache
- _OBJC_IVAR_$__PSSharingContactRankerModel._shareInteractionCache
- _OBJC_IVAR_$__PSSharingContactRankerModel._sharingContactRankerMLModel
- _OBJC_IVAR_$__PSSharingContactRankerScoredContact._interaction
- _OBJC_IVAR_$__PSSharingContactRankerScoredContact._score
- _OBJC_IVAR_$_evaluatedRule._recipientUniqueID
- _OBJC_IVAR_$_evaluatedRule._ruleLabel
- _OBJC_IVAR_$_evaluatedRule._ruleScore
- _OBJC_IVAR_$_scoredModel._modelKey
- _OBJC_IVAR_$_scoredModel._score
- _OBJC_IVAR_$_scoredRule._recipientUniqueID
- _OBJC_IVAR_$_scoredRule._ruleLabel
- _OBJC_IVAR_$_scoredRule._ruleScore
- _OBJC_METACLASS_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent
- _OBJC_METACLASS_$_FidesPHSEvaluatorDataSource
- _OBJC_METACLASS_$_GBDTEvaluator
- _OBJC_METACLASS_$_LighthouseShareSheetPFLTraining
- _OBJC_METACLASS_$_ModelHyperparameters
- _OBJC_METACLASS_$_PSDESPlugin
- _OBJC_METACLASS_$__PSBehaviorRuleFeatureExtraction
- _OBJC_METACLASS_$__PSBehaviorRuleRankingUtilities
- _OBJC_METACLASS_$__PSConfidenceModel
- _OBJC_METACLASS_$__PSConfidenceModelArchive
- _OBJC_METACLASS_$__PSConfidenceModelDriver
- _OBJC_METACLASS_$__PSConfidenceModelForSharing
- _OBJC_METACLASS_$__PSContactFillerDataCollectionStatistics
- _OBJC_METACLASS_$__PSContactFillerDataCollectionUtilities
- _OBJC_METACLASS_$__PSContactFillerNormalizationConstants
- _OBJC_METACLASS_$__PSContactFillerRecipient
- _OBJC_METACLASS_$__PSFeatureStatistics
- _OBJC_METACLASS_$__PSFeaturizedBehaviorRule
- _OBJC_METACLASS_$__PSPersonalizationEvaluation
- _OBJC_METACLASS_$__PSRuleMiningModel
- _OBJC_METACLASS_$__PSRuleOverlapFeedback
- _OBJC_METACLASS_$__PSRuleRankingMLModel
- _OBJC_METACLASS_$__PSSharingContactFeatureExtraction
- _OBJC_METACLASS_$__PSSharingContactRankerMLModel
- _OBJC_METACLASS_$__PSSharingContactRankerModel
- _OBJC_METACLASS_$__PSSharingContactRankerScoredContact
- _OBJC_METACLASS_$_evaluatedRule
- _OBJC_METACLASS_$_scoredModel
- _OBJC_METACLASS_$_scoredRule
- _ODCurareEvaluationAndReportingLibraryCore
- _ODCurareEvaluationAndReportingLibraryCore.frameworkLibrary
- _OUTLINED_FUNCTION_8
- _ProactiveEventTrackerLibraryCore.frameworkLibrary
- _Test
- _Train
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableArray_$_Shuffling
- __OBJC_$_CATEGORY_NSMutableArray_$_Shuffling
- __OBJC_$_CLASS_METHODS_FidesPHSEvaluatorDataSource
- __OBJC_$_CLASS_METHODS_GBDTEvaluator
- __OBJC_$_CLASS_METHODS_LighthouseShareSheetPFLTraining
- __OBJC_$_CLASS_METHODS_PSDESPlugin
- __OBJC_$_CLASS_METHODS__PSBehaviorRuleRankingUtilities
- __OBJC_$_CLASS_METHODS__PSConfidenceModel
- __OBJC_$_CLASS_METHODS__PSConfidenceModelArchive
- __OBJC_$_CLASS_METHODS__PSConfidenceModelDriver
- __OBJC_$_CLASS_METHODS__PSContactFillerDataCollectionUtilities
- __OBJC_$_CLASS_PROP_LIST__PSConfidenceModel
- __OBJC_$_CLASS_PROP_LIST__PSConfidenceModelArchive
- __OBJC_$_CLASS_PROP_LIST__PSSuggester
- __OBJC_$_INSTANCE_METHODS_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent
- __OBJC_$_INSTANCE_METHODS_FidesPHSEvaluatorDataSource
- __OBJC_$_INSTANCE_METHODS_GBDTEvaluator
- __OBJC_$_INSTANCE_METHODS_LighthouseShareSheetPFLTraining
- __OBJC_$_INSTANCE_METHODS_ModelHyperparameters
- __OBJC_$_INSTANCE_METHODS_PSDESPlugin
- __OBJC_$_INSTANCE_METHODS__PSBehaviorRuleFeatureExtraction
- __OBJC_$_INSTANCE_METHODS__PSConfidenceModel
- __OBJC_$_INSTANCE_METHODS__PSConfidenceModelArchive
- __OBJC_$_INSTANCE_METHODS__PSConfidenceModelDriver
- __OBJC_$_INSTANCE_METHODS__PSConfidenceModelForSharing
- __OBJC_$_INSTANCE_METHODS__PSContactFillerDataCollectionStatistics
- __OBJC_$_INSTANCE_METHODS__PSContactFillerNormalizationConstants
- __OBJC_$_INSTANCE_METHODS__PSContactFillerRecipient
- __OBJC_$_INSTANCE_METHODS__PSFeatureStatistics
- __OBJC_$_INSTANCE_METHODS__PSFeaturizedBehaviorRule
- __OBJC_$_INSTANCE_METHODS__PSPersonalizationEvaluation
- __OBJC_$_INSTANCE_METHODS__PSRuleMiningModel
- __OBJC_$_INSTANCE_METHODS__PSRuleOverlapFeedback
- __OBJC_$_INSTANCE_METHODS__PSRuleRankingMLModel
- __OBJC_$_INSTANCE_METHODS__PSSharingContactFeatureExtraction
- __OBJC_$_INSTANCE_METHODS__PSSharingContactRankerMLModel
- __OBJC_$_INSTANCE_METHODS__PSSharingContactRankerModel
- __OBJC_$_INSTANCE_METHODS__PSSharingContactRankerScoredContact
- __OBJC_$_INSTANCE_METHODS_evaluatedRule
- __OBJC_$_INSTANCE_METHODS_scoredModel
- __OBJC_$_INSTANCE_METHODS_scoredRule
- __OBJC_$_INSTANCE_VARIABLES_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent
- __OBJC_$_INSTANCE_VARIABLES_FidesPHSEvaluatorDataSource
- __OBJC_$_INSTANCE_VARIABLES_LighthouseShareSheetPFLTraining
- __OBJC_$_INSTANCE_VARIABLES_ModelHyperparameters
- __OBJC_$_INSTANCE_VARIABLES_PSDESPlugin
- __OBJC_$_INSTANCE_VARIABLES__PSBehaviorRuleFeatureExtraction
- __OBJC_$_INSTANCE_VARIABLES__PSConfidenceModel
- __OBJC_$_INSTANCE_VARIABLES__PSConfidenceModelArchive
- __OBJC_$_INSTANCE_VARIABLES__PSConfidenceModelDriver
- __OBJC_$_INSTANCE_VARIABLES__PSConfidenceModelForSharing
- __OBJC_$_INSTANCE_VARIABLES__PSContactFillerDataCollectionStatistics
- __OBJC_$_INSTANCE_VARIABLES__PSContactFillerNormalizationConstants
- __OBJC_$_INSTANCE_VARIABLES__PSContactFillerRecipient
- __OBJC_$_INSTANCE_VARIABLES__PSFeatureStatistics
- __OBJC_$_INSTANCE_VARIABLES__PSFeaturizedBehaviorRule
- __OBJC_$_INSTANCE_VARIABLES__PSPersonalizationEvaluation
- __OBJC_$_INSTANCE_VARIABLES__PSRuleMiningModel
- __OBJC_$_INSTANCE_VARIABLES__PSRuleOverlapFeedback
- __OBJC_$_INSTANCE_VARIABLES__PSRuleRankingMLModel
- __OBJC_$_INSTANCE_VARIABLES__PSSharingContactFeatureExtraction
- __OBJC_$_INSTANCE_VARIABLES__PSSharingContactRankerMLModel
- __OBJC_$_INSTANCE_VARIABLES__PSSharingContactRankerModel
- __OBJC_$_INSTANCE_VARIABLES__PSSharingContactRankerScoredContact
- __OBJC_$_INSTANCE_VARIABLES_evaluatedRule
- __OBJC_$_INSTANCE_VARIABLES_scoredModel
- __OBJC_$_INSTANCE_VARIABLES_scoredRule
- __OBJC_$_PROP_LIST_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent
- __OBJC_$_PROP_LIST_FidesPHSEvaluatorDataSource
- __OBJC_$_PROP_LIST_LighthouseShareSheetPFLTraining
- __OBJC_$_PROP_LIST_ModelHyperparameters
- __OBJC_$_PROP_LIST_PSDESPlugin
- __OBJC_$_PROP_LIST__PSBehaviorRuleFeatureExtraction
- __OBJC_$_PROP_LIST__PSConfidenceModel
- __OBJC_$_PROP_LIST__PSConfidenceModelArchive
- __OBJC_$_PROP_LIST__PSConfidenceModelDriver
- __OBJC_$_PROP_LIST__PSConfidenceModelForSharing
- __OBJC_$_PROP_LIST__PSContactFillerDataCollectionStatistics
- __OBJC_$_PROP_LIST__PSContactFillerNormalizationConstants
- __OBJC_$_PROP_LIST__PSContactFillerRecipient
- __OBJC_$_PROP_LIST__PSFeatureStatistics
- __OBJC_$_PROP_LIST__PSFeaturizedBehaviorRule
- __OBJC_$_PROP_LIST__PSPersonalizationEvaluation
- __OBJC_$_PROP_LIST__PSRuleMiningModel
- __OBJC_$_PROP_LIST__PSRuleOverlapFeedback
- __OBJC_$_PROP_LIST__PSRuleRankingMLModel
- __OBJC_$_PROP_LIST__PSSharingContactFeatureExtraction
- __OBJC_$_PROP_LIST__PSSharingContactRankerMLModel
- __OBJC_$_PROP_LIST__PSSharingContactRankerModel
- __OBJC_$_PROP_LIST__PSSharingContactRankerScoredContact
- __OBJC_$_PROP_LIST_evaluatedRule
- __OBJC_$_PROP_LIST_scoredModel
- __OBJC_$_PROP_LIST_scoredRule
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_DESRecipeEvaluation
- __OBJC_$_PROTOCOL_METHOD_TYPES_DESRecipeEvaluation
- __OBJC_$_PROTOCOL_REFS_DESRecipeEvaluation
- __OBJC_CLASS_PROTOCOLS_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent
- __OBJC_CLASS_PROTOCOLS_$_PSDESPlugin
- __OBJC_CLASS_PROTOCOLS_$__PSConfidenceModel
- __OBJC_CLASS_PROTOCOLS_$__PSConfidenceModelArchive
- __OBJC_CLASS_RO_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent
- __OBJC_CLASS_RO_$_FidesPHSEvaluatorDataSource
- __OBJC_CLASS_RO_$_GBDTEvaluator
- __OBJC_CLASS_RO_$_LighthouseShareSheetPFLTraining
- __OBJC_CLASS_RO_$_ModelHyperparameters
- __OBJC_CLASS_RO_$_PSDESPlugin
- __OBJC_CLASS_RO_$__PSBehaviorRuleFeatureExtraction
- __OBJC_CLASS_RO_$__PSBehaviorRuleRankingUtilities
- __OBJC_CLASS_RO_$__PSConfidenceModel
- __OBJC_CLASS_RO_$__PSConfidenceModelArchive
- __OBJC_CLASS_RO_$__PSConfidenceModelDriver
- __OBJC_CLASS_RO_$__PSConfidenceModelForSharing
- __OBJC_CLASS_RO_$__PSContactFillerDataCollectionStatistics
- __OBJC_CLASS_RO_$__PSContactFillerDataCollectionUtilities
- __OBJC_CLASS_RO_$__PSContactFillerNormalizationConstants
- __OBJC_CLASS_RO_$__PSContactFillerRecipient
- __OBJC_CLASS_RO_$__PSFeatureStatistics
- __OBJC_CLASS_RO_$__PSFeaturizedBehaviorRule
- __OBJC_CLASS_RO_$__PSPersonalizationEvaluation
- __OBJC_CLASS_RO_$__PSRuleMiningModel
- __OBJC_CLASS_RO_$__PSRuleOverlapFeedback
- __OBJC_CLASS_RO_$__PSRuleRankingMLModel
- __OBJC_CLASS_RO_$__PSSharingContactFeatureExtraction
- __OBJC_CLASS_RO_$__PSSharingContactRankerMLModel
- __OBJC_CLASS_RO_$__PSSharingContactRankerModel
- __OBJC_CLASS_RO_$__PSSharingContactRankerScoredContact
- __OBJC_CLASS_RO_$_evaluatedRule
- __OBJC_CLASS_RO_$_scoredModel
- __OBJC_CLASS_RO_$_scoredRule
- __OBJC_LABEL_PROTOCOL_$_DESRecipeEvaluation
- __OBJC_METACLASS_RO_$_CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent
- __OBJC_METACLASS_RO_$_FidesPHSEvaluatorDataSource
- __OBJC_METACLASS_RO_$_GBDTEvaluator
- __OBJC_METACLASS_RO_$_LighthouseShareSheetPFLTraining
- __OBJC_METACLASS_RO_$_ModelHyperparameters
- __OBJC_METACLASS_RO_$_PSDESPlugin
- __OBJC_METACLASS_RO_$__PSBehaviorRuleFeatureExtraction
- __OBJC_METACLASS_RO_$__PSBehaviorRuleRankingUtilities
- __OBJC_METACLASS_RO_$__PSConfidenceModel
- __OBJC_METACLASS_RO_$__PSConfidenceModelArchive
- __OBJC_METACLASS_RO_$__PSConfidenceModelDriver
- __OBJC_METACLASS_RO_$__PSConfidenceModelForSharing
- __OBJC_METACLASS_RO_$__PSContactFillerDataCollectionStatistics
- __OBJC_METACLASS_RO_$__PSContactFillerDataCollectionUtilities
- __OBJC_METACLASS_RO_$__PSContactFillerNormalizationConstants
- __OBJC_METACLASS_RO_$__PSContactFillerRecipient
- __OBJC_METACLASS_RO_$__PSFeatureStatistics
- __OBJC_METACLASS_RO_$__PSFeaturizedBehaviorRule
- __OBJC_METACLASS_RO_$__PSPersonalizationEvaluation
- __OBJC_METACLASS_RO_$__PSRuleMiningModel
- __OBJC_METACLASS_RO_$__PSRuleOverlapFeedback
- __OBJC_METACLASS_RO_$__PSRuleRankingMLModel
- __OBJC_METACLASS_RO_$__PSSharingContactFeatureExtraction
- __OBJC_METACLASS_RO_$__PSSharingContactRankerMLModel
- __OBJC_METACLASS_RO_$__PSSharingContactRankerModel
- __OBJC_METACLASS_RO_$__PSSharingContactRankerScoredContact
- __OBJC_METACLASS_RO_$_evaluatedRule
- __OBJC_METACLASS_RO_$_scoredModel
- __OBJC_METACLASS_RO_$_scoredRule
- __OBJC_PROTOCOL_$_DESRecipeEvaluation
- __PSModelAccuracyAnalyticsEventName
- __PSRuleOverlapAnalyticsEventName
- __PSRuleOverlapFeedbackEventMatchingTimeWindow
- __PSRuleOverlapFeedbackMinRuleConfidenceForSuggestion
- __PSRuleOverlapFeedbackRegularizingContextOverlapConstraint
- ___101-[_PSRuleMiningModel suggestionProxiesWithPredictionContext:photoSuggestedPeople:supportedBundleIDs:]_block_invoke
- ___101-[_PSRuleOverlapFeedback feedbackPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke
- ___101-[_PSRuleOverlapFeedback feedbackPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke_2
- ___101-[_PSRuleOverlapFeedback feedbackPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke_3
- ___101-[_PSRuleOverlapFeedback feedbackPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke_4
- ___104-[_PSRuleOverlapFeedback feedbackPETPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke
- ___104-[_PSRuleOverlapFeedback feedbackPETPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke_2
- ___104-[_PSRuleOverlapFeedback feedbackPETPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke_3
- ___104-[_PSRuleOverlapFeedback feedbackPETPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke_4
- ___104-[_PSRuleOverlapFeedback feedbackPETPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke_5
- ___104-[_PSRuleOverlapFeedback feedbackPETPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:]_block_invoke_6
- ___105+[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:]_block_invoke
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.1050
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.1057
- ___108+[_PSContactFillerDataCollectionUtilities initContactPropertyCache:timeOfShareInteraction:interactionStore:]_block_invoke
- ___111-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:]_block_invoke.1089
- ___118-[_PSSuggestionFromTextPredictor suggestionsFromIncompleteRemindersWithContext:startDate:endDate:priorScoreThreshold:]_block_invoke.90
- ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.952
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.868
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.868.cold.1
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.425
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.425.cold.1
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.442
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.468
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.470
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.472
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.473
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke_2
- ___144+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke_2.426
- ___150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.214
- ___150-[_PSContactSuggester gameCenterSuggestionsWithMaxSuggestions:interactionDomains:appleUsersOnly:includeGroupSuggestions:excludeContactsByIdentifiers:]_block_invoke.219
- ___180-[_PSSharingContactRankerModel suggestionProxiesWithPredictionContext:supportedBundleIDs:behaviorRulesConsideringInTheContext:interactionModelSuggestions:ruleRankingMLModelScores:]_block_invoke
- ___187-[GBDTEvaluator _evaluateResultWithGradients:questions:inputVectors:reportGradientsBothSidesOfSplit:reportNodeSumGradients:reportPerFeatureResultDifference:reportPerNodeResultDifference:]_block_invoke
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.234
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.234.cold.1
- ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.460
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.236
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.236.cold.1
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.240
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke_2
- ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke.602
- ___46-[_PSSuggester provideFeedbackForSuggestions:]_block_invoke.640
- ___47-[_PSSuggester suggestInteractionsFromContext:]_block_invoke.257
- ___48-[_PSRuleRankingMLModel rankRules:contextItems:]_block_invoke
- ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.439
- ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.440
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.1045
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.1045.cold.1
- ___50-[_PSRuleOverlapFeedback writeRecordObjcWithData:]_block_invoke
- ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.418
- ___54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.283
- ___54+[_PSContactSuggester contactPriorSuggestionsForText:]_block_invoke.286
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.201
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.205
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_2.207
- ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.430
- ___57-[_PSRuleOverlapFeedback wasInteractionAmongSuggestLess:]_block_invoke
- ___57-[_PSRuleOverlapFeedback wasInteractionAmongSuggestLess:]_block_invoke.390
- ___57-[_PSRuleOverlapFeedback wasInteractionAmongSuggestLess:]_block_invoke.cold.1
- ___58-[_PSContactSuggester contactPriorsForContactIdentifiers:]_block_invoke.277
- ___58-[_PSHeuristics seedSuggestionsForChatGuidsAndTransports:]_block_invoke
- ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke
- ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.617
- ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.618
- ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke_2
- ___59-[_PSFTZKWSuggestionsTransformerFactory filterIDSReachable]_block_invoke
- ___59-[_PSRuleOverlapFeedback constantFeaturesFromContextItems:]_block_invoke
- ___59-[_PSRuleOverlapFeedback constantFeaturesFromContextItems:]_block_invoke_2
- ___60-[_PSKNNModel rankedMapsShareEtaSuggestions:maxSuggestions:]_block_invoke.519
- ___60-[_PSRuleOverlapFeedback sharesheetFeedbackEventsSinceDate:]_block_invoke
- ___60-[_PSRuleOverlapFeedback sharesheetFeedbackEventsSinceDate:]_block_invoke.618
- ___60-[_PSRuleOverlapFeedback sharesheetFeedbackEventsSinceDate:]_block_invoke.cold.1
- ___61-[_PSMessagesPinningSuggester submitMessagesPinningFeedback:]_block_invoke.266
- ___62-[_PSRuleOverlapFeedback constantPETFeaturesFromContextItems:]_block_invoke
- ___62-[_PSRuleOverlapFeedback constantPETFeaturesFromContextItems:]_block_invoke_2
- ___62-[_PSRuleOverlapFeedback constantPETFeaturesFromContextItems:]_block_invoke_3
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.683
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.683.cold.1
- ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.451
- ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.451.cold.1
- ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.454
- ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.433
- ___67-[LighthouseShareSheetPFLTraining createDataSourceForRecipe:error:]_block_invoke
- ___67-[_PSMediaAnalysisProcessingTask executeTaskWithCompletionHandler:]_block_invoke.404
- ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.466
- ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.923
- ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.457
- ___68-[_PSSuggester showNotificationToFileARadarForUserStudyParticipants]_block_invoke.323
- ___69-[_PSRuleOverlapFeedback targetAppPredictedCorrectlyByRule:bundleId:]_block_invoke
- ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.463
- ___70-[_PSEnsembleModel validateCoreMLModelWithRawInput:predictionContext:]_block_invoke
- ___71-[_PSRuleOverlapFeedback modelAccuracyLogging:WithMatchingInteraction:]_block_invoke
- ___72-[LighthouseShareSheetPFLTraining createDataSourceForDodMLRecipe:error:]_block_invoke
- ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.644
- ___72-[_PSSuggester computeShareSheetEphemeralFeaturesWithPredictionContext:]_block_invoke
- ___72-[_PSSuggester computeShareSheetEphemeralFeaturesWithPredictionContext:]_block_invoke.244
- ___72-[_PSSuggester computeShareSheetEphemeralFeaturesWithPredictionContext:]_block_invoke.cold.1
- ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.469
- ___73-[_PSBehaviorRuleFeatureExtraction extractContextMatchFeatures:features:]_block_invoke
- ___73-[_PSBehaviorRuleFeatureExtraction extractContextMatchFeatures:features:]_block_invoke.190
- ___73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke
- ___73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.690
- ___73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.cold.1
- ___74-[LighthouseShareSheetPFLTraining processDataForMetricEvaluationForStore:]_block_invoke
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.530
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.535
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.538
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.553
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.559
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.566
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.563
- ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.475
- ___77-[_PSMessagesPinningSuggester chatGuidsForMessagesPinningWithMaxSuggestions:]_block_invoke.206
- ___78-[LighthouseShareSheetPFLTraining generateResultsDictionayWithModelURL:error:]_block_invoke
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.374
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.391
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.398
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.398.cold.1
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.405
- ___79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.356
- ___79-[_PSKNNModel suggestionsByUpdatingGroupNamesFromSuggestions:imCoreTimeBudget:]_block_invoke.356.cold.1
- ___80+[_PSFTZKWSuggestionsTransformerFactory getResultsFromTransformers:suggestions:]_block_invoke.58
- ___80-[_PSRuleOverlapFeedback loggingForKnowledgeStoreEvent:WithMatchingInteraction:]_block_invoke
- ___80-[_PSRuleOverlapFeedback loggingForKnowledgeStoreEvent:WithMatchingInteraction:]_block_invoke_2
- ___80-[_PSRuleOverlapFeedback loggingForKnowledgeStoreEvent:WithMatchingInteraction:]_block_invoke_3
- ___80-[_PSRuleOverlapFeedback loggingForKnowledgeStoreEvent:WithMatchingInteraction:]_block_invoke_4
- ___80-[_PSRuleOverlapFeedback loggingForKnowledgeStoreEvent:WithMatchingInteraction:]_block_invoke_5
- ___80-[_PSRuleOverlapFeedback loggingForKnowledgeStoreEvent:WithMatchingInteraction:]_block_invoke_5.cold.1
- ___81-[_PSPersonalizationEvaluation adaptMLModel:withTrainingData:modelConfiguration:]_block_invoke
- ___81-[_PSPersonalizationEvaluation adaptMLModel:withTrainingData:modelConfiguration:]_block_invoke.356
- ___81-[_PSPersonalizationEvaluation adaptMLModel:withTrainingData:modelConfiguration:]_block_invoke.356.cold.1
- ___81-[_PSPersonalizationEvaluation adaptMLModel:withTrainingData:modelConfiguration:]_block_invoke.cold.1
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.813
- ___83-[_PSBehaviorRuleFeatureExtraction extractFeaturesGivenRule:contextItems:features:]_block_invoke
- ___83-[_PSBehaviorRuleFeatureExtraction extractFeaturesGivenRule:contextItems:features:]_block_invoke_2
- ___83-[_PSBehaviorRuleFeatureExtraction extractFeaturesGivenRule:contextItems:features:]_block_invoke_3
- ___83-[_PSBehaviorRuleFeatureExtraction extractFeaturesGivenRule:contextItems:features:]_block_invoke_4
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.690
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.760
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.766
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.771
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.771.cold.1
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.779
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.782
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.792
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.793
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.773
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_4
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.422
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.426
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.427
- ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.436
- ___89-[_PSEnsembleModel psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:]_block_invoke
- ___89-[_PSEnsembleModel psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:]_block_invoke_2
- ___91-[_PSContactSuggester contactSuggestionsWithMaxSuggestions:excludeContactsWithIdentifiers:]_block_invoke.184
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.214
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.217
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.221
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.221.cold.1
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.221.cold.2
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.233
- ___96+[_PSCNAutocompleteFeedbackProcessingTask runWithInferredEnterAndExit:overImplicit:eventFilter:]_block_invoke.233.cold.1
- ___96-[_PSSuggester(InteractionInformation) interactionCountForHandle:fetchLimit:interactionStoreDB:]_block_invoke.300
- ___98+[_PSContactFillerDataCollectionUtilities recipientPredictedCorrectlyByRule:interaction:bundleId:]_block_invoke
- ___98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.80
- ___98-[_PSSuggestionFromTextPredictor suggestionFromContactPriors:priorScoreThreshold:bundleID:reason:]_block_invoke.82
- ___99-[_PSKNNModel rankedCoRecipientSuggestionsWithPredictionContext:modelConfiguration:maxSuggestions:]_block_invoke.386
- ___BehaviorMinerLibraryCore_block_invoke
- ___Block_byref_object_copy_.372
- ___Block_byref_object_copy_.474
- ___Block_byref_object_dispose_.373
- ___Block_byref_object_dispose_.475
- ___CoreDuetLibraryCore_block_invoke
- ___DistributedEvaluationLibraryCore_block_invoke
- ___MLRuntimeLibraryCore_block_invoke
- ___ODCurareEvaluationAndReportingLibraryCore_block_invoke
- ___ProactiveEventTrackerLibraryCore_block_invoke
- ____PSShareSheetSuggestionBundleIDMapping_block_invoke.203
- ___block_descriptor_32_e12_B24?08^B16l
- ___block_descriptor_32_e28_v24?0"NSUUID"8"NSError"16l
- ___block_descriptor_32_e65_q24?0"_PSFeaturizedBehaviorRule"8"_PSFeaturizedBehaviorRule"16l
- ___block_descriptor_32_e87_q24?0"_PSSharingContactRankerScoredContact"8"_PSSharingContactRankerScoredContact"16l
- ___block_descriptor_40_e8_32s_e26_"NSMutableDictionary"8?0ls32l8
- ___block_descriptor_40_e8_32s_e30_v16?0"_PSPredictionContext"8ls32l8
- ___block_descriptor_48_e8_32s40r_e25_v16?0"MLUpdateContext"8ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e36_"NSDictionary"16?0"_PSCandidate"8ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e27_q24?0"BMRule"8"BMRule"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e33_"NSMutableArray"16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e35_v32?0"NSString"8"NSObject"16^B24ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e25_v16?0"MLUpdateContext"8ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e22_B16?0"BMStoreEvent"8ls32l8r48l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e17_"_PASTuple2"8?0ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
- ___block_descriptor_88_e8_32s40s48s56bs64r_e5_v8?0ls32l8s56l8r64l8s40l8s48l8
- ___block_descriptor_96_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8s48l8s56l8r72l8s64l8
- ___block_literal_global.1038
- ___block_literal_global.1080
- ___block_literal_global.1082
- ___block_literal_global.160
- ___block_literal_global.162
- ___block_literal_global.164
- ___block_literal_global.192
- ___block_literal_global.200
- ___block_literal_global.203
- ___block_literal_global.207
- ___block_literal_global.210
- ___block_literal_global.213
- ___block_literal_global.232
- ___block_literal_global.235
- ___block_literal_global.239
- ___block_literal_global.251
- ___block_literal_global.253
- ___block_literal_global.256
- ___block_literal_global.263
- ___block_literal_global.268
- ___block_literal_global.289
- ___block_literal_global.294
- ___block_literal_global.300
- ___block_literal_global.304
- ___block_literal_global.309
- ___block_literal_global.311
- ___block_literal_global.320
- ___block_literal_global.325
- ___block_literal_global.389
- ___block_literal_global.401
- ___block_literal_global.405
- ___block_literal_global.413
- ___block_literal_global.417
- ___block_literal_global.418
- ___block_literal_global.421
- ___block_literal_global.424
- ___block_literal_global.429
- ___block_literal_global.432
- ___block_literal_global.435
- ___block_literal_global.437
- ___block_literal_global.438
- ___block_literal_global.439
- ___block_literal_global.441
- ___block_literal_global.442
- ___block_literal_global.443
- ___block_literal_global.445
- ___block_literal_global.449
- ___block_literal_global.453
- ___block_literal_global.456
- ___block_literal_global.459
- ___block_literal_global.462
- ___block_literal_global.465
- ___block_literal_global.468
- ___block_literal_global.471
- ___block_literal_global.474
- ___block_literal_global.491
- ___block_literal_global.496
- ___block_literal_global.498
- ___block_literal_global.503
- ___block_literal_global.505
- ___block_literal_global.512
- ___block_literal_global.513
- ___block_literal_global.533
- ___block_literal_global.537
- ___block_literal_global.540
- ___block_literal_global.545
- ___block_literal_global.556
- ___block_literal_global.568
- ___block_literal_global.594
- ___block_literal_global.599
- ___block_literal_global.601
- ___block_literal_global.605
- ___block_literal_global.606
- ___block_literal_global.608
- ___block_literal_global.616
- ___block_literal_global.617
- ___block_literal_global.620
- ___block_literal_global.628
- ___block_literal_global.642
- ___block_literal_global.654
- ___block_literal_global.657
- ___block_literal_global.672
- ___block_literal_global.680
- ___block_literal_global.682
- ___block_literal_global.687
- ___block_literal_global.689
- ___block_literal_global.781
- ___block_literal_global.796
- ___block_literal_global.826
- ___block_literal_global.859
- ___block_literal_global.962
- ___block_literal_global.965
- ___block_literal_global.98
- ___getBMBehaviorRetrieverClass_block_invoke
- ___getBMHourSlotForHourOfDaySymbolLoc_block_invoke
- ___getBMItemClass_block_invoke
- ___getBMItemTypeClass_block_invoke
- ___getBMRetrievalFilterClass_block_invoke
- ___getDESRecordStoreClass_block_invoke
- ___getMLRTaskResultClass_block_invoke
- ___getODCurareCandidateModelClass_block_invoke
- ___getODCurareDataCachePruningPolicyObjectClass_block_invoke
- ___getODCurareEvaluationAndReportingModuleClass_block_invoke
- ___getODCurareModelInformationClass_block_invoke
- ___getODCurareModelSelectionParameterClass_block_invoke
- ___getODCurareModelSelectionPolicyClass_block_invoke
- ___getODCurarePersonalizationPolicyClass_block_invoke
- ___getODCurareReportFillerDataSetClass_block_invoke
- ___getODCurareReportFillerDataSetSizeClass_block_invoke
- ___getODCurareReportFillerDataSetStatsClass_block_invoke
- ___getODCurareReportFillerModelEvaluationClass_block_invoke
- ___getODCurareReportFillerModelEvaluationSummaryClass_block_invoke
- ___getODCurareReportFillerModelHyperparametersClass_block_invoke
- ___getODCurareReportFillerModelInformationClass_block_invoke
- ___getPETEventTracker2Class_block_invoke
- ___getPPTopicStoreClass_block_invoke
- ___get_DKEventQueryClass_block_invoke
- ___get_DKEventStreamClass_block_invoke
- __getDirectSuggestionsWithContext:withTimeout:._pasOnceToken9
- __hasInitializedCache
- __suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken198
- _asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:._pasOnceToken75
- _audit_stringBehaviorMiner
- _audit_stringCoreDuet
- _audit_stringDistributedEvaluation
- _audit_stringMLRuntime
- _audit_stringODCurareEvaluationAndReporting
- _audit_stringProactiveEventTracker
- _autocompleteSearchResultsWithPredictionContext:._pasOnceToken108
- _comparisonResult
- _defaultServiceWithMaxSuggestionCount:._pasOnceToken8
- _feedbackDictionary._pasOnceToken7
- _getBMBehaviorRetrieverClass.softClass
- _getBMHourSlotForHourOfDaySymbolLoc.ptr
- _getBMItemClass
- _getBMItemClass.softClass
- _getBMItemTypeClass
- _getBMItemTypeClass.softClass
- _getBMRetrievalFilterClass
- _getBMRetrievalFilterClass.softClass
- _getDESRecordStoreClass.softClass
- _getMLArrayBatchProviderClass
- _getMLModelClass
- _getMLParameterKeyClass
- _getMLRTaskResultClass.softClass
- _getODCurareCandidateModelClass
- _getODCurareCandidateModelClass.softClass
- _getODCurareDataCachePruningPolicyObjectClass.softClass
- _getODCurareEvaluationAndReportingModuleClass.softClass
- _getODCurareModelInformationClass.softClass
- _getODCurareModelSelectionParameterClass.softClass
- _getODCurareModelSelectionPolicyClass.softClass
- _getODCurarePersonalizationPolicyClass.softClass
- _getODCurareReportFillerDataSetClass.softClass
- _getODCurareReportFillerDataSetSizeClass.softClass
- _getODCurareReportFillerDataSetStatsClass.softClass
- _getODCurareReportFillerModelEvaluationClass
- _getODCurareReportFillerModelEvaluationClass.softClass
- _getODCurareReportFillerModelEvaluationSummaryClass.softClass
- _getODCurareReportFillerModelHyperparametersClass.softClass
- _getODCurareReportFillerModelInformationClass.softClass
- _getPETEventTracker2Class
- _getPETEventTracker2Class.softClass
- _getPPTopicStoreClass.softClass
- _getPhotoBasedFeaturesAsync:withTimeout:._pasExprOnceResult
- _getPhotoBasedFeaturesAsync:withTimeout:._pasOnceToken64
- _getResultsFromTransformers:suggestions:._pasOnceToken19
- _get_DKEventQueryClass
- _get_DKEventQueryClass.softClass
- _get_DKEventStreamClass
- _get_DKEventStreamClass.softClass
- _init._pasOnceToken6
- _malloc_type_malloc
- _objc_msgSend$CDModelDataStreamIdentifier
- _objc_msgSend$CDQuery
- _objc_msgSend$GBDTQuestions
- _objc_msgSend$URLHostAllowedCharacterSet
- _objc_msgSend$_PSRuleMiningIsAdaptedMLModelOK
- _objc_msgSend$_PSRuleMiningIsMLModelInUse
- _objc_msgSend$_PSRuleMiningMLModelScoreThreshold
- _objc_msgSend$_PSRuleMiningModelMinRuleConfidenceForSuggestion
- _objc_msgSend$_PSRuleMiningModelMinSupportForSuggestion
- _objc_msgSend$_PSRuleMiningModelRegularizingContextOverlapConstraint
- _objc_msgSend$_PSSharingContactRankerMLModelInUse
- _objc_msgSend$_PSSharingContactRankerMLModelScoreThreshold
- _objc_msgSend$_computeFirstOrderGradientsWithTargets:predictions:positiveSampleWeight:
- _objc_msgSend$_computePredictionsFromModelWithInputVectors:currentModel:error:
- _objc_msgSend$_computeSecondOrderGradientsWithTargets:predictions:positiveSampleWeight:
- _objc_msgSend$_computeSumOfGradientsLeftAndRightOfSplitWithFeature:threshold:inputVectors:gradients:
- _objc_msgSend$_differenceArrayWithArray:
- _objc_msgSend$_evaluateResultWithGradients:questions:inputVectors:reportGradientsBothSidesOfSplit:reportNodeSumGradients:reportPerFeatureResultDifference:reportPerNodeResultDifference:
- _objc_msgSend$_featureVectorFromSuggestionDate:bundleID:peopleInPhotoIdentifiers:scenesInPhotoIdentifiers:
- _objc_msgSend$_findNodeSamplesWithDecisionPath:inputVectors:gradients:
- _objc_msgSend$_firstOrderGradientWithPrediction:label:
- _objc_msgSend$_getDataStatistics:forData:
- _objc_msgSend$_l1NormWithArray:
- _objc_msgSend$_l2NormWithArray:
- _objc_msgSend$_makeKeysWithInputVectors:
- _objc_msgSend$_secondOrderGradientWithPrediction:
- _objc_msgSend$_sigmoidWithValue:
- _objc_msgSend$_sumAbsoluteErrorWithPredictions:targets:
- _objc_msgSend$_sumAccuratePredictionsWithPredictions:targets:
- _objc_msgSend$_translateResultWithTranslateVector:result:
- _objc_msgSend$_weightResultWithWeightVector:result:
- _objc_msgSend$adaptMLModel:withMLModelType:withDataArray:modelConfiguration:
- _objc_msgSend$adaptMLModel:withTrainingData:modelConfiguration:
- _objc_msgSend$adaptableModelConfiguration
- _objc_msgSend$adaptableModelDeployPath
- _objc_msgSend$adaptationStrategy
- _objc_msgSend$adaptedModelRecipeVersion
- _objc_msgSend$addAdaptedModelUsageInfoToSuggestions:
- _objc_msgSend$addEvent:
- _objc_msgSend$addEventForModel:event:
- _objc_msgSend$addEventForModel:forUseCaseKey:event:
- _objc_msgSend$addExtraInformationWithSuggestions:modelSuggestionProxiesDict:
- _objc_msgSend$addHyperparameterIndices:
- _objc_msgSend$addHyperparameterValues:
- _objc_msgSend$addModelEvaluationResults:
- _objc_msgSend$addStats:
- _objc_msgSend$antecedent
- _objc_msgSend$anyObject
- _objc_msgSend$attachmentURLsForBasename:
- _objc_msgSend$averageBehavioralRuleConfidence
- _objc_msgSend$averageBehavioralRuleConviction
- _objc_msgSend$averageBehavioralRuleLift
- _objc_msgSend$averageBehavioralRuleMLScore
- _objc_msgSend$averageBehavioralRulePowerFactor
- _objc_msgSend$averageBehavioralRuleSupport
- _objc_msgSend$avg
- _objc_msgSend$batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featurizedRules:
- _objc_msgSend$batchPredictWithMLModel:featureArrayDict:
- _objc_msgSend$behaviorRetriever
- _objc_msgSend$behaviorRulesConsideringInTheContext
- _objc_msgSend$behavioralRuleFeaturesStream
- _objc_msgSend$boolValueForKey:defaultValue:
- _objc_msgSend$bucketedValue:
- _objc_msgSend$bufferHead
- _objc_msgSend$bufferSize
- _objc_msgSend$bundleIdOfHostOpenedShareExtension
- _objc_msgSend$bundleIdOfShareExtensionOpened
- _objc_msgSend$calculateNormContantsGivenInteractionStore:normConstants:
- _objc_msgSend$calculateNormalizedCallingFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:direction:
- _objc_msgSend$calculateNormalizedShareFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:
- _objc_msgSend$calculateNormalizedTextingFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:direction:
- _objc_msgSend$calculateStats
- _objc_msgSend$calculateTimeBucketGivenInteraction:timeOfShareInteraction:
- _objc_msgSend$calculateTimeSinceLastCallForContactGivenContactIdPredicate:direction:timeOfShareInteraction:interactionCache:
- _objc_msgSend$calculateTimeSinceLastShareForContactGivenContactIdPredicate:timeOfShareInteraction:interactionCache:
- _objc_msgSend$calculateTimeSinceLastTextForContactGivenContactIdPredicate:direction:timeOfShareInteraction:interactionCache:
- _objc_msgSend$cancel
- _objc_msgSend$candidateLocalIdentifiersFromPhotoSuggestedPeople:
- _objc_msgSend$circularBuffer
- _objc_msgSend$cloneAdaptableModel:toFilePath:originalXgboostModelName:clonedXgboostModelName:
- _objc_msgSend$compileMLModelAtPath:
- _objc_msgSend$compileModelAtURL:error:
- _objc_msgSend$computeEphemeralFeaturesWithCandidates:context:
- _objc_msgSend$computeFirstOrderGradients
- _objc_msgSend$computeSASSFeatureWithScenesDetectedInPhoto:andConfiguredScenes:
- _objc_msgSend$computeSecondOrderGradients
- _objc_msgSend$computeShareSheetEphemeralFeaturesWithPredictionContext:reply:
- _objc_msgSend$confidenceModelDictionary
- _objc_msgSend$confidenceModelDriver
- _objc_msgSend$confidenceModelForSharing
- _objc_msgSend$configBoltTaskIDSpecification
- _objc_msgSend$configDepthSpecification
- _objc_msgSend$configTreeSpecification
- _objc_msgSend$consequent
- _objc_msgSend$constantFeatures
- _objc_msgSend$constantFeaturesFromContextItems:
- _objc_msgSend$constantFeaturesReady
- _objc_msgSend$constantPETFeaturesFromContextItems:
- _objc_msgSend$contactFillerBucketedValue:
- _objc_msgSend$contextFeatures
- _objc_msgSend$contextFeaturesReady
- _objc_msgSend$contextItemsFromEvent:
- _objc_msgSend$conviction
- _objc_msgSend$copyFileFromURL:toURL:
- _objc_msgSend$copyItemAtPath:toPath:error:
- _objc_msgSend$copyRemoteRuleMinerMLModel:
- _objc_msgSend$copyTo:
- _objc_msgSend$copyZippedAdaptableModel:
- _objc_msgSend$coreMLInputFeatureTensor
- _objc_msgSend$coreMLModelFeatureOrder
- _objc_msgSend$coreMLModelNeedsDurableFeatures
- _objc_msgSend$coreMLNumberOfCandidates
- _objc_msgSend$coreMLTensorIndexToCandidate
- _objc_msgSend$countInteractionsUsingPredicate:error:
- _objc_msgSend$createDataSourceForDodMLRecipe:error:
- _objc_msgSend$createDataSourceForRecipe:error:
- _objc_msgSend$createMLArrayBatchProviderWithMLModelType:withDataArray:
- _objc_msgSend$createMLFeatureProviderArrayFromSingleShareEventData:
- _objc_msgSend$createMLFeatureProviderArrayFromSingleShareEventData:forMLModel:
- _objc_msgSend$curareEvaluationAndReporting
- _objc_msgSend$dataSource
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$defaultArchivePath
- _objc_msgSend$defaultRecipeParams
- _objc_msgSend$defaultStore
- _objc_msgSend$derivedIdentifier
- _objc_msgSend$dictionaryWithContentsOfFile:
- _objc_msgSend$discardAdaptedModel
- _objc_msgSend$discardTrialModels
- _objc_msgSend$doesSuggestionProxyMatch:withInteraction:
- _objc_msgSend$doesTheRecipientsMatchInInteraction1:interaction2:
- _objc_msgSend$enforceOneSignificantFigureForDouble:
- _objc_msgSend$enforceOneSignificantFigureForSmallDouble:
- _objc_msgSend$evaluateIsInvokedOnce
- _objc_msgSend$evaluateMetricsWithModelURL:
- _objc_msgSend$evaluateWithModelURL:dataSource:processDataReturnDict:error:
- _objc_msgSend$eventWithStream:startDate:endDate:identifierStringValue:metadata:
- _objc_msgSend$extractAdaptedModelRecipeID
- _objc_msgSend$extractConstantFeaturesForMLModelIntoFeatures:
- _objc_msgSend$extractConstantFeaturesInto:
- _objc_msgSend$extractContextMatchFeatures:features:
- _objc_msgSend$extractFeaturesFromBehaviorRulesIntoPETMessage:behaviorRules:MLModelScores:
- _objc_msgSend$extractFeaturesFromBehaviorRulesIntoPETMessage:behaviorRules:contextItems:ruleRankingModel:
- _objc_msgSend$extractFeaturesGivenRule:contextItems:features:
- _objc_msgSend$extractFeaturesInto:withPredictionContext:forContactId:forInteraction:behaviorRulesConsideringInTheContext:ruleRankingMLModelScores:interactionModelScores:
- _objc_msgSend$extractFrequencyRecencyFeaturesIntoPETMessage:recipientID:interaction:normConstants:numberOfDaysToLookBack:interactionStore:timeOfShareInteraction:contactPropertyCache:interactionCache:
- _objc_msgSend$extractUserFeaturesIntoPETMessage:normConstants:behaviorRetriever:
- _objc_msgSend$feaExtHandle
- _objc_msgSend$feaExtractionHandle
- _objc_msgSend$featureDict
- _objc_msgSend$featureMatricesForAllShareEvents
- _objc_msgSend$featureNameDict
- _objc_msgSend$feedbackPETPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:
- _objc_msgSend$feedbackPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:
- _objc_msgSend$fetchFeaturesWithCandidates:context:
- _objc_msgSend$filterByRegularizingRules:invalidatedByAnyConflictingItems:containingItemTypes:
- _objc_msgSend$filterByRegularizingRulesByContextOverlap:regulularizeItems:queryItems:regularizationConstraint:
- _objc_msgSend$filterIDSReachable
- _objc_msgSend$filterRulesBasedOnInteractionGivenRuleList:interaction:
- _objc_msgSend$filterWithOperand:inclusionOperator:items:
- _objc_msgSend$filterWithOperand:inclusionOperator:types:
- _objc_msgSend$findObjectWithID:inArray:
- _objc_msgSend$floatValueForKey:defaultValue:
- _objc_msgSend$freeCachesIfNotCoreDuetDaemon
- _objc_msgSend$generateCandidateModels
- _objc_msgSend$generateResultsDictionayWithModelURL:error:
- _objc_msgSend$getAdaptedCompiledMLModelPath
- _objc_msgSend$getAdaptedModelRecipeVersionFilePath
- _objc_msgSend$getAdaptedModelVersion
- _objc_msgSend$getBehaviorRulesGivenContext:behaviorRetriever:
- _objc_msgSend$getCacheSuggestions
- _objc_msgSend$getConfidence
- _objc_msgSend$getConfidenceForModel:forUseCaseKey:
- _objc_msgSend$getCoreMLSuggestionProxiesWithPredictionContext:modelSuggestionProxiesDict:candidateToFeatureVectorDictGetter:
- _objc_msgSend$getDeployedAdaptableCompiledMLModelPath
- _objc_msgSend$getDeployedCompiledMLModelPath
- _objc_msgSend$getDeployedCompiledMLModelPathForContactRanker
- _objc_msgSend$getDictionaryFromArchiveAtPath:
- _objc_msgSend$getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:
- _objc_msgSend$getInteractionModelScoreForEvent:forInteractionRecipients:
- _objc_msgSend$getInteractionModelScoreForSuggestions:forInteractionRecipients:
- _objc_msgSend$getInteractionRecipientFromInteraction:
- _objc_msgSend$getIntermediateAdaptableCompiledMLModel
- _objc_msgSend$getKnnSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:
- _objc_msgSend$getLatestTrialMLModelVersion
- _objc_msgSend$getListOfContactsFromCashedMessagesInteraction:cashedShareInteractions:
- _objc_msgSend$getListOfContactsInteractedInTheLastNumberOfDays:interactionStore:limit:
- _objc_msgSend$getModelProxiesArrayWithPredictionContext:
- _objc_msgSend$getModelSuggestionsProxyDictWithModelProxiesArray:
- _objc_msgSend$getOrMakeConfidenceModelDictionary
- _objc_msgSend$getOtherSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:
- _objc_msgSend$getPhotoBasedFeatures:
- _objc_msgSend$getPhotoBasedFeaturesAsync:withTimeout:
- _objc_msgSend$getRuleMiningSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:
- _objc_msgSend$getSelectedModel:
- _objc_msgSend$getSessionID
- _objc_msgSend$getTrialCompiledAdaptableMLModelPath
- _objc_msgSend$getTrialCompiledMLModelPath
- _objc_msgSend$getTrialCompiledMLModelPathForContactRanker
- _objc_msgSend$getZippedDefaultAdaptableModelPath
- _objc_msgSend$giveModelDescription
- _objc_msgSend$highConfidenceRuleCount
- _objc_msgSend$hourOfDaySlot
- _objc_msgSend$hyperparametersForCandidateModel:
- _objc_msgSend$incomingCallTotal
- _objc_msgSend$incomingTextTotal
- _objc_msgSend$initContactPropertyCache:timeOfShareInteraction:interactionStore:
- _objc_msgSend$initWithAdaptableModelConfig:isAdaptedMLModelOK:scoreThreshold:
- _objc_msgSend$initWithBufferSize:minimumInstanceCount:
- _objc_msgSend$initWithBufferSize:sum:circularBuffer:bufferHead:
- _objc_msgSend$initWithBundleIdentifier:
- _objc_msgSend$initWithBundleIdentifier:dataProviderInstance:evaluationInstance:personalizationInstance:pruningPolicy:error:
- _objc_msgSend$initWithConfidenceModelDictionary:
- _objc_msgSend$initWithInteractionStore:messageInteractionCache:shareInteractionCache:
- _objc_msgSend$initWithJSONResult:unprivatizedVector:
- _objc_msgSend$initWithKnowledgeStore:contactresolver:withConfig:
- _objc_msgSend$initWithLabel:score:recipientUniqueID:
- _objc_msgSend$initWithList:
- _objc_msgSend$initWithMaximumNumberOfDays:maximumNumberOfEvents:
- _objc_msgSend$initWithMetadata:
- _objc_msgSend$initWithMetadata:interactionStore:
- _objc_msgSend$initWithMetricName:percentageIncrease:
- _objc_msgSend$initWithModelInformation:modelURL:
- _objc_msgSend$initWithModelKey:score:
- _objc_msgSend$initWithModelSelectionParameters:minimumNumberOfEvaluations:minimumNumberOfSamples:
- _objc_msgSend$initWithModelSelectionParameters:minimumNumberOfSamplesForPersonalization:minimumNumberOfSamplesForPersonalizationSelection:
- _objc_msgSend$initWithModelURL:withCoreDuetStreamIdentifier:andMetadata:
- _objc_msgSend$initWithNumTrees:learningRate:minChildWeight:adaptationStrategy:
- _objc_msgSend$initWithRecipe:inputVectors:targetVector:error:
- _objc_msgSend$initWithRule:score:features:
- _objc_msgSend$initWithScore:interaction:
- _objc_msgSend$initWithScoreThreshold:
- _objc_msgSend$inputVectors
- _objc_msgSend$integerValueForKey:defaultValue:
- _objc_msgSend$interactionContentURL
- _objc_msgSend$interactionExtractedTopicFromAttachment
- _objc_msgSend$interactionModelScore
- _objc_msgSend$interactionPhotoContact
- _objc_msgSend$interactionPhotoScene
- _objc_msgSend$interactionSharingSourceBundleID
- _objc_msgSend$interactionStoreEventsSinceDate:
- _objc_msgSend$interactionTargetBundleID
- _objc_msgSend$interactionUTIType
- _objc_msgSend$intermediateCompiledModelURL
- _objc_msgSend$isAdaptedMLModelOK
- _objc_msgSend$isAdaptedModel
- _objc_msgSend$isDefaultModel
- _objc_msgSend$isDurableFeaturesSetAdmissible
- _objc_msgSend$isPersonalizableModel
- _objc_msgSend$isWeekend
- _objc_msgSend$itemWithType:numberValue:
- _objc_msgSend$itemWithType:stringValue:
- _objc_msgSend$lastPathComponent
- _objc_msgSend$laterDate:
- _objc_msgSend$learningRate
- _objc_msgSend$lift
- _objc_msgSend$list
- _objc_msgSend$loadAdaptableModelConfig:
- _objc_msgSend$loadAdaptableModelUnderDirectory:
- _objc_msgSend$loadDefaultAdaptableModelConfig
- _objc_msgSend$loadDefaultModel
- _objc_msgSend$loadDefaultRuleMinerMLModel
- _objc_msgSend$loadDeployedAdaptableModelUnderDirectory:
- _objc_msgSend$loadMLModel
- _objc_msgSend$loadMLModel:modelConfig:
- _objc_msgSend$loadMLModelConfigurationWithConfigDict:
- _objc_msgSend$locationIdentifier
- _objc_msgSend$loggingForKnowledgeStoreEvent:WithMatchingInteraction:
- _objc_msgSend$loggingTrainDataForContactFillerModel:withMatchingInteraction:interactionRecipients:ruleRankingModel:contactPropertyCache:interactionCache:
- _objc_msgSend$lowConfidenceRuleCount
- _objc_msgSend$matchFeedbackEvent:WithInteractions:
- _objc_msgSend$max
- _objc_msgSend$maxDepth
- _objc_msgSend$maximumBehavioralRuleConfidence
- _objc_msgSend$maximumBehavioralRuleConviction
- _objc_msgSend$maximumBehavioralRuleLift
- _objc_msgSend$maximumBehavioralRuleMLScore
- _objc_msgSend$maximumBehavioralRulePowerFactor
- _objc_msgSend$maximumBehavioralRuleSupport
- _objc_msgSend$mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:
- _objc_msgSend$mediumConfidenceRuleCount
- _objc_msgSend$metadataFromFeedbackEvent:
- _objc_msgSend$min
- _objc_msgSend$minChildWeight
- _objc_msgSend$minimumBehavioralRuleConfidence
- _objc_msgSend$minimumBehavioralRuleConviction
- _objc_msgSend$minimumBehavioralRuleLift
- _objc_msgSend$minimumBehavioralRuleMLScore
- _objc_msgSend$minimumBehavioralRulePowerFactor
- _objc_msgSend$minimumBehavioralRuleSupport
- _objc_msgSend$minimumInstanceCount
- _objc_msgSend$modelAccuracyLogging:WithMatchingInteraction:
- _objc_msgSend$modelKey
- _objc_msgSend$modelTag
- _objc_msgSend$modelTagToCandidateModel
- _objc_msgSend$modelTagToHyperparameters
- _objc_msgSend$moveItemAtPath:toPath:error:
- _objc_msgSend$normConstants
- _objc_msgSend$normalizedIncomingCallFrequency
- _objc_msgSend$normalizedIncomingTextFrequency
- _objc_msgSend$normalizedOutgoingCallFrequency
- _objc_msgSend$normalizedOutgoingTextFrequency
- _objc_msgSend$normalizedShareFrequency
- _objc_msgSend$numClasses
- _objc_msgSend$numTrees
- _objc_msgSend$numberFromString:
- _objc_msgSend$numberOfBehavioralRulesAdvocating
- _objc_msgSend$numberOfUserSamples
- _objc_msgSend$objective
- _objc_msgSend$objectsPassingTest:
- _objc_msgSend$outgoingCallTotal
- _objc_msgSend$outgoingTextTotal
- _objc_msgSend$parameters
- _objc_msgSend$peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:
- _objc_msgSend$percentiles
- _objc_msgSend$performPrerequisitesBeforeAdaptationWithFeaturesConfigDeployPath:
- _objc_msgSend$phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:
- _objc_msgSend$portraitContactStore
- _objc_msgSend$precalculateConstantFeatures
- _objc_msgSend$predicate
- _objc_msgSend$predicateFormat
- _objc_msgSend$processDataForMetricEvaluationForStore:
- _objc_msgSend$processDataForStore:recipeInfo:
- _objc_msgSend$processDataForStore:taskParameters:
- _objc_msgSend$processDataReturnDict
- _objc_msgSend$processDataWithQuery:balanceNeed:
- _objc_msgSend$psAdaptationDefaults
- _objc_msgSend$psConfigForAdaptableModel
- _objc_msgSend$psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:
- _objc_msgSend$publisherWithUseCase:options:
- _objc_msgSend$rankRules:contextItems:
- _objc_msgSend$rawDataToCandidateFeatureDict:
- _objc_msgSend$recentNonSystemSuggestionsForBundleIDs:numberOfSuggestion:
- _objc_msgSend$recipientPredictedCorrectlyByRule:interaction:bundleId:
- _objc_msgSend$recipientUniqueID
- _objc_msgSend$reformatFeaturesInFeatureDictArray:
- _objc_msgSend$reformatFeaturesInFeaturizedBehaviorRuleArray:
- _objc_msgSend$registerModelKey:forUseCaseKey:confidenceWindowSize:minimumInstanceCount:
- _objc_msgSend$removeFolderAtPath:
- _objc_msgSend$replaceObjectAtIndex:withObject:
- _objc_msgSend$reportGradientsBothSidesOfSplit
- _objc_msgSend$reportNodeSumGradients
- _objc_msgSend$reportPerFeatureResultDifference
- _objc_msgSend$reportPerNodeResultDifference
- _objc_msgSend$resetBuffer
- _objc_msgSend$resolveUniqueContactIdGivenInteraction:
- _objc_msgSend$retrieveRulesWithFilters:
- _objc_msgSend$retrieveRulesWithSupport:confidence:filters:
- _objc_msgSend$rule
- _objc_msgSend$ruleLabel
- _objc_msgSend$ruleMiningModel
- _objc_msgSend$rulePowerFactor
- _objc_msgSend$ruleRankingModel
- _objc_msgSend$ruleScore
- _objc_msgSend$runAdaptationAndEvaluationWithFeaturesConfigDeployPath:adaptableModelDeployPath:
- _objc_msgSend$saveRecordWithData:recordInfo:completion:
- _objc_msgSend$saveToVirtualStore
- _objc_msgSend$scenesBasedFeaturesNames
- _objc_msgSend$scenesInPhotoIdentifiers
- _objc_msgSend$scoreRanking:forModelKey:
- _objc_msgSend$scoreThreshold
- _objc_msgSend$scoredCoreMLCandidates
- _objc_msgSend$scores
- _objc_msgSend$scoresOnFeatures:
- _objc_msgSend$scoresOnRules:contextItems:
- _objc_msgSend$seedSuggestionsForChatGuidsAndTransports:
- _objc_msgSend$selectedFeaturesConfig
- _objc_msgSend$setAccuracyGainThresholdForSwap:
- _objc_msgSend$setAdaptableModelConfiguration:
- _objc_msgSend$setAdaptableModelDeployPath:
- _objc_msgSend$setAdaptationStrategy:
- _objc_msgSend$setAdaptedModelRecipeID:
- _objc_msgSend$setAdaptedModelRecipeVersion:
- _objc_msgSend$setAverageBehavioralRuleConfidence:
- _objc_msgSend$setAverageBehavioralRuleConviction:
- _objc_msgSend$setAverageBehavioralRuleLift:
- _objc_msgSend$setAverageBehavioralRuleMLScore:
- _objc_msgSend$setAverageBehavioralRulePowerFactor:
- _objc_msgSend$setAverageBehavioralRuleSupport:
- _objc_msgSend$setAvg:
- _objc_msgSend$setBatchSize:
- _objc_msgSend$setBehaviorRulesConsideringInTheContext:
- _objc_msgSend$setBufferHead:
- _objc_msgSend$setBufferSize:
- _objc_msgSend$setByAddingObject:
- _objc_msgSend$setCircularBuffer:
- _objc_msgSend$setConfidence:
- _objc_msgSend$setConfidenceModelDictionary:
- _objc_msgSend$setConfidenceModelDriver:
- _objc_msgSend$setConfigBoltTaskIDSpecification:
- _objc_msgSend$setConfigDepthSpecification:
- _objc_msgSend$setConfigTreeSpecification:
- _objc_msgSend$setConstantFeatures:
- _objc_msgSend$setConstantFeaturesReady:
- _objc_msgSend$setContentUrlInContext:
- _objc_msgSend$setContentUrlInRule:
- _objc_msgSend$setContentUrlOverlap:
- _objc_msgSend$setContextFeatures:
- _objc_msgSend$setContextFeaturesReady:
- _objc_msgSend$setCoreMLInputFeatureTensor:
- _objc_msgSend$setCoreMLModelFeatureOrder:
- _objc_msgSend$setCoreMLNumberOfCandidates:
- _objc_msgSend$setCoreMLTensorIndexToCandidate:
- _objc_msgSend$setCurareEvaluationAndReporting:
- _objc_msgSend$setDataSource:
- _objc_msgSend$setDataUsedToEvaluateModel:
- _objc_msgSend$setDataUsedToPersonalizeModel:
- _objc_msgSend$setEngagementRateGainThresholdForSwap:
- _objc_msgSend$setEpoc:
- _objc_msgSend$setEvaluateIsInvokedOnce:
- _objc_msgSend$setEvaluationIterationCount:
- _objc_msgSend$setEventStreams:
- _objc_msgSend$setFeaExtHandle:
- _objc_msgSend$setFeaExtractionHandle:
- _objc_msgSend$setFeatureMatricesForAllShareEvents:
- _objc_msgSend$setFeatureName:
- _objc_msgSend$setFeatureNameDict:
- _objc_msgSend$setFeatureValueMax:
- _objc_msgSend$setFeatureValueMean:
- _objc_msgSend$setFeatureValueMin:
- _objc_msgSend$setFeatureValuePercentile10:
- _objc_msgSend$setFeatureValuePercentile25:
- _objc_msgSend$setFeatureValuePercentile50:
- _objc_msgSend$setFeatureValuePercentile75:
- _objc_msgSend$setFeatureValuePercentile90:
- _objc_msgSend$setFeatureValueStd:
- _objc_msgSend$setFeatures:
- _objc_msgSend$setHasInitializedCache:
- _objc_msgSend$setHighConfidenceRuleCount:
- _objc_msgSend$setIncomingCallTotal:
- _objc_msgSend$setIncomingTextTotal:
- _objc_msgSend$setInteraction:
- _objc_msgSend$setInteractionModelScore:
- _objc_msgSend$setIntermediateCompiledModelURL:
- _objc_msgSend$setIsAdaptedMLModelOK:
- _objc_msgSend$setIsAdaptedModel:
- _objc_msgSend$setIsAdaptedModelCreated:
- _objc_msgSend$setIsAdaptedModelUsed:
- _objc_msgSend$setIsCoreMLValidationFetch:
- _objc_msgSend$setIsDefaultModel:
- _objc_msgSend$setIsPersonalizableModel:
- _objc_msgSend$setIsWeekendInRule:
- _objc_msgSend$setIsWeekendOverlap:
- _objc_msgSend$setKnowledgeStore:
- _objc_msgSend$setLOIInContext:
- _objc_msgSend$setLOIInRule:
- _objc_msgSend$setLOIOverlap:
- _objc_msgSend$setLearningRate:
- _objc_msgSend$setLimit:
- _objc_msgSend$setList:
- _objc_msgSend$setLocationOfInterestContainingRuleCount:
- _objc_msgSend$setLocationOfInterestRulesCardinality:
- _objc_msgSend$setLowConfidenceRuleCount:
- _objc_msgSend$setMax:
- _objc_msgSend$setMaxDepth:
- _objc_msgSend$setMaximumBehavioralRuleConfidence:
- _objc_msgSend$setMaximumBehavioralRuleConviction:
- _objc_msgSend$setMaximumBehavioralRuleLift:
- _objc_msgSend$setMaximumBehavioralRuleMLScore:
- _objc_msgSend$setMaximumBehavioralRulePowerFactor:
- _objc_msgSend$setMaximumBehavioralRuleSupport:
- _objc_msgSend$setMediumConfidenceRuleCount:
- _objc_msgSend$setMetricName:
- _objc_msgSend$setMetricValue:
- _objc_msgSend$setMin:
- _objc_msgSend$setMinChildWeight:
- _objc_msgSend$setMinSampleCountForAdaptation:
- _objc_msgSend$setMinimumBehavioralRuleConfidence:
- _objc_msgSend$setMinimumBehavioralRuleConviction:
- _objc_msgSend$setMinimumBehavioralRuleLift:
- _objc_msgSend$setMinimumBehavioralRuleMLScore:
- _objc_msgSend$setMinimumBehavioralRulePowerFactor:
- _objc_msgSend$setMinimumBehavioralRuleSupport:
- _objc_msgSend$setMinimumInstanceCount:
- _objc_msgSend$setMinimumTestDataSizeForSwap:
- _objc_msgSend$setMode:
- _objc_msgSend$setModelHyperparameters:
- _objc_msgSend$setModelKey:
- _objc_msgSend$setModelSuggestionProxies:
- _objc_msgSend$setModelTag:
- _objc_msgSend$setModelTagToCandidateModel:
- _objc_msgSend$setModelTagToHyperparameters:
- _objc_msgSend$setNormConstants:
- _objc_msgSend$setNormalizedIncomingCallFrequency:
- _objc_msgSend$setNormalizedIncomingTextFrequency:
- _objc_msgSend$setNormalizedOutgoingCallFrequency:
- _objc_msgSend$setNormalizedOutgoingTextFrequency:
- _objc_msgSend$setNormalizedShareFrequency:
- _objc_msgSend$setNumClasses:
- _objc_msgSend$setNumTrees:
- _objc_msgSend$setNumberOfBehavioralRulesAdvocating:
- _objc_msgSend$setNumberOfPositiveSamples:
- _objc_msgSend$setNumberOfSamples:
- _objc_msgSend$setNumberOfUserSamples:
- _objc_msgSend$setNumberOfUserSessions:
- _objc_msgSend$setNumberStyle:
- _objc_msgSend$setOffset:
- _objc_msgSend$setOutgoingCallTotal:
- _objc_msgSend$setOutgoingTextTotal:
- _objc_msgSend$setParameters:
- _objc_msgSend$setParametersForHyperparmeters:
- _objc_msgSend$setParametersFromRecipe
- _objc_msgSend$setParametersFromRecipeForCandidateModel:
- _objc_msgSend$setPeopleAnalysisFromAssetsWithPredictionContext:identifiersOfPeopleInPhotos:
- _objc_msgSend$setPercentiles:
- _objc_msgSend$setPersonAndAppMatched:
- _objc_msgSend$setPersonMatched:
- _objc_msgSend$setPhotoAnalysisFromAssetsWithPredictionContext:
- _objc_msgSend$setPhotoContactContainingRuleCount:
- _objc_msgSend$setPhotoContactInContext:
- _objc_msgSend$setPhotoContactInRule:
- _objc_msgSend$setPhotoContactOverlap:
- _objc_msgSend$setPhotoContactRulesCardinality:
- _objc_msgSend$setPhotoSceneContainingRuleCount:
- _objc_msgSend$setPhotoSceneInContext:
- _objc_msgSend$setPhotoSceneInRule:
- _objc_msgSend$setPhotoSceneOverlap:
- _objc_msgSend$setPhotoSceneRulesCardinality:
- _objc_msgSend$setPortraitContactStore:
- _objc_msgSend$setPredictionContextWithContext:
- _objc_msgSend$setProcessDataReturnDict:
- _objc_msgSend$setPsConfigForAdaptableModel:
- _objc_msgSend$setRecipeID:
- _objc_msgSend$setResults:
- _objc_msgSend$setRule:
- _objc_msgSend$setRuleMiningModel:
- _objc_msgSend$setRuleRankingModel:
- _objc_msgSend$setScenesInPhotoIdentifiers:
- _objc_msgSend$setScore:
- _objc_msgSend$setScoreThreshold:
- _objc_msgSend$setScoredCoreMLCandidates:
- _objc_msgSend$setScores:
- _objc_msgSend$setSelectedFeaturesConfig:
- _objc_msgSend$setShareInteractionsSent:
- _objc_msgSend$setShareTotal:
- _objc_msgSend$setSharingContactRankerMLModel:
- _objc_msgSend$setSharingContactRankerModel:
- _objc_msgSend$setSize:
- _objc_msgSend$setSourceBundleIdContainingRuleCount:
- _objc_msgSend$setSourceBundleIdInContext:
- _objc_msgSend$setSourceBundleIdInRule:
- _objc_msgSend$setSourceBundleIdOverlap:
- _objc_msgSend$setSourceBundleIdRulesCardinality:
- _objc_msgSend$setStdev:
- _objc_msgSend$setStdevBehavioralRuleConfidence:
- _objc_msgSend$setStdevBehavioralRuleConviction:
- _objc_msgSend$setStdevBehavioralRuleLift:
- _objc_msgSend$setStdevBehavioralRuleMLScore:
- _objc_msgSend$setStdevBehavioralRulePowerFactor:
- _objc_msgSend$setStdevBehavioralRuleSupport:
- _objc_msgSend$setSum:
- _objc_msgSend$setSupport:
- _objc_msgSend$setSwapOK:
- _objc_msgSend$setTargetBundleIDInConsequent:
- _objc_msgSend$setTargetBundleIdContainingRuleCount:
- _objc_msgSend$setTargetBundleIdInContext:
- _objc_msgSend$setTargetBundleIdInRule:
- _objc_msgSend$setTargetBundleIdOverlap:
- _objc_msgSend$setTargetBundleIdRulesCardinality:
- _objc_msgSend$setTestSplitPercent:
- _objc_msgSend$setTextInteractionsReceived:
- _objc_msgSend$setTextInteractionsSent:
- _objc_msgSend$setTimeOfDaySlotInRule:
- _objc_msgSend$setTimeOfDaySlotOverlap:
- _objc_msgSend$setTimeSinceLastContactViaIncomingCall:
- _objc_msgSend$setTimeSinceLastContactViaIncomingText:
- _objc_msgSend$setTimeSinceLastContactViaOutgoingCall:
- _objc_msgSend$setTimeSinceLastContactViaOutgoingText:
- _objc_msgSend$setTimeSinceLastContactViaShare:
- _objc_msgSend$setTopN:
- _objc_msgSend$setTopicContainingRuleCount:
- _objc_msgSend$setTopicInContext:
- _objc_msgSend$setTopicInRule:
- _objc_msgSend$setTopicOverlap:
- _objc_msgSend$setTopicRulesCardinality:
- _objc_msgSend$setTopicStore:
- _objc_msgSend$setTotalMessagesRecieved:
- _objc_msgSend$setTotalMessagesSent:
- _objc_msgSend$setTotalShares:
- _objc_msgSend$setUniqueShareEventIdentifier:
- _objc_msgSend$setUtiTypeInContext:
- _objc_msgSend$setUtiTypeInRule:
- _objc_msgSend$setUtiTypeOverlap:
- _objc_msgSend$setVersionNumber:
- _objc_msgSend$setWasShareRecipient:
- _objc_msgSend$set_PSRuleMiningIsAdaptedMLModelOK:
- _objc_msgSend$set_PSRuleMiningIsMLModelInUse:
- _objc_msgSend$set_PSRuleMiningMLModelScoreThreshold:
- _objc_msgSend$set_PSRuleMiningModelDaysToPromoteRecentlyInstalledAppExtensions:
- _objc_msgSend$set_PSRuleMiningModelMinRuleConfidenceForSuggestion:
- _objc_msgSend$set_PSRuleMiningModelMinSupportForSuggestion:
- _objc_msgSend$set_PSRuleMiningModelRegularizingContextOverlapConstraint:
- _objc_msgSend$set_PSSharingContactRankerMLModelInUse:
- _objc_msgSend$set_PSSharingContactRankerMLModelScoreThreshold:
- _objc_msgSend$shareInteractionsSent
- _objc_msgSend$shareTotal
- _objc_msgSend$sharesheetFeedbackEventsSinceDate:
- _objc_msgSend$sharingContactRankerMLModel
- _objc_msgSend$sharingContactRankerModel
- _objc_msgSend$shuffle
- _objc_msgSend$sortDescriptorWithKey:ascending:selector:
- _objc_msgSend$stdev
- _objc_msgSend$stdevBehavioralRuleConfidence
- _objc_msgSend$stdevBehavioralRuleConviction
- _objc_msgSend$stdevBehavioralRuleLift
- _objc_msgSend$stdevBehavioralRuleMLScore
- _objc_msgSend$stdevBehavioralRulePowerFactor
- _objc_msgSend$stdevBehavioralRuleSupport
- _objc_msgSend$stringValueForKey:defaultValue:
- _objc_msgSend$stringWithContentsOfFile:encoding:error:
- _objc_msgSend$suggestionProxiesWithPredictionContext:photoSuggestedPeople:supportedBundleIDs:
- _objc_msgSend$suggestionProxiesWithPredictionContext:supportedBundleIDs:behaviorRulesConsideringInTheContext:interactionModelSuggestions:ruleRankingMLModelScores:
- _objc_msgSend$sum
- _objc_msgSend$support
- _objc_msgSend$targetAppPredictedCorrectlyByRule:bundleId:
- _objc_msgSend$targetVector
- _objc_msgSend$textInteractionsReceived
- _objc_msgSend$textInteractionsSent
- _objc_msgSend$timeSinceLastContactViaIncomingCall
- _objc_msgSend$timeSinceLastContactViaIncomingText
- _objc_msgSend$timeSinceLastContactViaOutgoingCall
- _objc_msgSend$timeSinceLastContactViaOutgoingText
- _objc_msgSend$timeSinceLastContactViaShare
- _objc_msgSend$topLevelScenesFromSceneNetTags:
- _objc_msgSend$topN
- _objc_msgSend$topicStore
- _objc_msgSend$trainAndEvaluateModelsWithCandidateModels:personalizationPolicy:selectionPolicy:error:
- _objc_msgSend$transferConstantFeatures:to:
- _objc_msgSend$transferFeaturesFrom:toFeatures:
- _objc_msgSend$translateVector
- _objc_msgSend$unarchivedObjectOfClasses:fromData:error:
- _objc_msgSend$unzipFileWithPath:toFileName:toFolderPath:
- _objc_msgSend$updateAdaptableModelConfigWithUpdateType:numTrees:
- _objc_msgSend$updateAdaptableModelProperties:
- _objc_msgSend$updateMLModelWithURL:withMLModelType:withDataArray:modelConfiguration:
- _objc_msgSend$updateTaskForModelAtURL:trainingData:configuration:progressHandlers:error:
- _objc_msgSend$updateType
- _objc_msgSend$userEvent
- _objc_msgSend$validateCoreMLScoringModelWithRawInput:predictionContext:reply:
- _objc_msgSend$wasInteractionAmongSuggestLess:
- _objc_msgSend$weightVector
- _objc_msgSend$writeArchiveFromDict:
- _objc_msgSend$writeRecordObjcWithData:
- _objc_setProperty_atomic_copy
- _personalizationLog
- _predictWithPredictionContext:maxSuggestions:contactKeysToFetch:._pasOnceToken142
- _psrDataCollectionForContext:timeToWaitInSeconds:maxComputationTime:withConfigAndStatsBlock:._pasOnceToken288
- _rankedZKWSuggestionsFromContext:._pasOnceToken106
- _rankedZkwSuggestionsFromPredictionArray:forBundleID:._pasOnceToken45
- _sharedInstance._pasOnceToken6
CStrings:
+ " ()-"
+ "<%@ %p> identifier: %@, contact: %@"
+ "@\"NSString\"16@?0@\"_PSPriorityContact\"8"
+ "@40@0:8@16@24B32B36"
+ "@64@0:8@16@24B32B36@40@48@?56"
+ "@68@0:8@16@24B32B36@40@48B56@?60"
+ "@?40@0:8@16B24B28d32"
+ "App"
+ "B16@?0@\"NSManagedObject\"8"
+ "B16@?0@\"_PSAutocompleteSuggestion\"8"
+ "Bypassing the IDS reachability filter"
+ "Completed background task: %@"
+ "ConversationGroupName"
+ "ConversationINImageURL"
+ "ConversationUserInteraction"
+ "Couldn't create os_log_t psBackgroundProcessingChannel"
+ "Error encountered while reading bookmark: %@"
+ "Error encountered while updating bookmark: %@"
+ "Error getting features for handle %@"
+ "Failed to expire task with error: %@"
+ "Failed to update interaction with uuid: %@"
+ "Feature flag is turned off, no hyperrecent-viewed-thread heuristics candidate boosted"
+ "Getting cached suggestions"
+ "Hyper-recent opened thread - PS Rewrite"
+ "IMSPIGetAllChatsContainingParticipantWithHandle"
+ "IMSPIGetContactsByChatGUID"
+ "IMSPIGetGroupPhotosForChatsWithGroupIDs"
+ "IMSPISuggestionsObject"
+ "In call heuristic"
+ "InFocus"
+ "Interactions"
+ "No photo attachments in the prediction context for media analysis and scene processing"
+ "No scene tag mapping specified in recipe–using default values."
+ "PSBackgroundTaskData"
+ "PhotoId: %@, person identification error: %@"
+ "RCS"
+ "Retrieved %tu cached suggestions (fetchIfNeeded=%d): %{private}@"
+ "Retrieved NULL cached suggestions (fetchIfNeeded=%d)"
+ "Running background task: %@"
+ "SELECT\n    intentClass,\n    bundleId,\n    groupIdentifier,\n    COALESCE(%d - MAX(CASE WHEN interactionDirection = 2 THEN absoluteTimestamp END), -1) AS %@,    COALESCE(%d - MAX(CASE WHEN interactionDirection = 3 THEN absoluteTimestamp END), -1) AS %@,    COUNT(CASE WHEN interactionDirection = 2 THEN 1 END) AS %@,\n    COUNT(CASE WHEN interactionDirection = 3 THEN 1 END) AS %@\nFROM\n    \"App.Intent\"\nWHERE\n    intentClass = 'INSendMessageIntent'\n    AND groupIdentifier = 'protocol;-;%@'\nGROUP BY\n    groupIdentifier;"
+ "SMS"
+ "Scene tag mapping: %@"
+ "Successfully read App.InFocus Biome stream"
+ "Successfully read MLSE.ShareSheet.ConversationUserInteraction Biome stream"
+ "SuggestionProxyTypeHyperRecencyViewedThreadRewrite"
+ "T@\"NSArray\",C,N,V_priorityContacts"
+ "T@\"NSArray\",C,N,V_sceneTagsInPhotoIdentifiers"
+ "T@\"NSDate\",&,N,V_date"
+ "T@\"NSString\",R,N"
+ "TB,N,V_bypassIDSFilter"
+ "Task expired!"
+ "Tq,N,V_activityType"
+ "UIResolutionTime: UI resolution has taken %fs, isUsingLegacyUI %@"
+ "_PSBackgroundProcessingTask"
+ "_PSContactHandleFeatureProvider"
+ "_PSEnsemble: Getting suggestions for ShareSheet session %@ (trial experimentId: %@ deploymentId: %d treatmentId: %@)"
+ "_PSEnsembleModel_getPhotoBasedFeatures_setPhotoAnalysis"
+ "_PSHyperRecentActivity"
+ "_PSInteractionsUpdate"
+ "_PSPriorityContact"
+ "_activityType"
+ "_bypassIDSFilter"
+ "_date"
+ "_featureVectorFromSuggestionDate:bundleID:peopleInPhotoIdentifiers:sceneTagsInPhotoIdentifiers:"
+ "_interactionFeaturesForHandle:"
+ "_priorityContacts"
+ "_sceneTagsInPhotoIdentifiers"
+ "_setError"
+ "absoluteTimestamp"
+ "activityType"
+ "attachmentsEligibleForPhotoProcessingFromAttachments:"
+ "attachmentsInObject:hasField:"
+ "boostPriorityContacts:"
+ "bypassIDSFilter"
+ "characterSetWithCharactersInString:"
+ "chatGUID"
+ "com.apple.RealityChrome"
+ "com.apple.proactive.psbackgroundprocessingtask"
+ "com.apple.togetherd"
+ "computeSASSFeatureWithSceneCategoriesDetectedInPhoto:andConfiguredSceneCategoryTags:"
+ "configuredSceneCategoryTagNames"
+ "data"
+ "deleteUIInteractionsMatchingSuggestLessFeedback:"
+ "detectedSceneCategoryNamesFromSceneNetTags:"
+ "eventType"
+ "executeQuery:"
+ "filterBlockedContacts"
+ "filterIDSReachable:"
+ "getBytes:range:"
+ "getCachedSuggestionsFetchingIfNeeded:"
+ "getPhotoBasedFeaturesAsync"
+ "getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:"
+ "handleRepeatingTask:"
+ "hasError"
+ "hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics"
+ "initWithContentsOfFile:"
+ "initWithDate:activityType:conversationId:"
+ "initWithIdentifier:contact:"
+ "interactionFeaturesForHandle:"
+ "interactionFeaturesForHandle:reply:"
+ "managedObjectContextFor:"
+ "mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:"
+ "next"
+ "numberOfIncomingInteractions"
+ "numberOfOutgoingInteractions"
+ "peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:"
+ "peoplesuggester_hyperrecent_viewed_thread"
+ "peoplesuggester_uiresolution_rewrite"
+ "personIdentifiersForPeopleInPicturesWithIdentifiers:"
+ "phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:withCompletion:"
+ "photoSceneDescriptor"
+ "position"
+ "predictionContext_sceneTagsInPhotoIdentifiers"
+ "priorityContacts"
+ "propertyListWithData:options:format:error:"
+ "protocol"
+ "psBackgroundProcessing"
+ "psBackgroundProcessingChannel"
+ "psr_inPhoneCallHeuristicSuggestionProxiesWithBundleIds:predictionContext:interactionsStatistics:"
+ "psr_suggestionsFromSuggestionProxies:interactionsStatistics:maxSuggestions:predictionContext:"
+ "q24@?0@\"_PSHyperRecentActivity\"8@\"_PSHyperRecentActivity\"16"
+ "queryInteractionsUsingPredicate:sortDescriptors:limit:offset:objectIDs:error:"
+ "realityChromeBundleId"
+ "reversed"
+ "row"
+ "savedBookmark"
+ "sceneTagsForPhotosWithIdentifiers:"
+ "sceneTagsInPhotoIdentifiers"
+ "self in %@"
+ "setActivityType:"
+ "setBypassIDSFilter:"
+ "setDate:"
+ "setExpirationHandler:"
+ "setIncludePets:"
+ "setPosition:"
+ "setPriorityContacts:"
+ "setSceneTagsInPhotoIdentifiers:"
+ "setTaskCompleted"
+ "setTaskExpiredWithRetryAfter:error:"
+ "setUseVIPModel:"
+ "shouldUseLegacyUI"
+ "shouldUseVIPModel"
+ "starting"
+ "storage"
+ "suggest-less-feedback"
+ "suggesterWithDaemonUsingMaxSuggestionCount:"
+ "togetherdBundleId"
+ "tupleWithFirst:second:"
+ "updateInteractionWithPhotoFeatures:"
+ "updateObjectsInContext:entityName:predicate:sortDescriptors:batchFetchLimit:totalFetchLimit:includeSubentities:updateBlock:"
+ "waitForGroup:"
+ "waitForGroup:timeoutSeconds:"
- "%.01f"
- "%@:%tu"
- "'"
- "(startDate < %@)"
- "-[CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent writeTo:]"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/PFL/LighthouseShareSheetPFLTraining.m"
- "/System/Library/DistributedEvaluation/Plugins/PeopleSuggesterDESPlugin.desPlugin/"
- "/System/Library/PrivateFrameworks/PeopleSuggester.framework/"
- "/dummyStream/tempStream"
- "/sharesheet/behavioralRuleFeatures"
- "/var/tmp/com.apple.siri-distributed-evaluation/"
- "10%"
- "25%"
- "50%"
- "75%"
- "90%"
- "@\"BMBehaviorRetriever\""
- "@\"BMRule\""
- "@\"FidesPHSEvaluatorDataSource\""
- "@\"MLModelConfiguration\""
- "@\"NSDictionary\"16@?0@\"_PSCandidate\"8"
- "@\"NSDictionary\"24@0:8@\"DESRecordSet\"16"
- "@\"NSDictionary\"24@0:8@\"NSDictionary\"16"
- "@\"NSDictionary\"40@0:8@\"DESRecipe\"16@\"DESRecordSet\"24^@32"
- "@\"NSDictionary\"48@0:8@\"DESRecipe\"16@\"DESRecordSet\"24^@32^@40"
- "@\"NSDictionary\"56@0:8@\"NSDictionary\"16@\"NSDictionary\"24@\"NSData\"32@\"NSArray\"40^@48"
- "@\"NSMutableDictionary\"8@?0"
- "@\"ODCurareEvaluationAndReportingModule\""
- "@\"PPContactStore\""
- "@\"PPTopicStore\""
- "@\"_DKKnowledgeStore\""
- "@\"_PSBehaviorRuleFeatureExtraction\""
- "@\"_PSConfidenceModelDriver\""
- "@\"_PSConfidenceModelForSharing\""
- "@\"_PSContactFillerNormalizationConstants\""
- "@\"_PSRuleMiningModel\""
- "@\"_PSRuleRankingMLModel\""
- "@\"_PSSharingContactFeatureExtraction\""
- "@\"_PSSharingContactRankerMLModel\""
- "@\"_PSSharingContactRankerModel\""
- "@24@0:8i16i20"
- "@32@0:8@16^@24"
- "@32@0:8i16@20i28"
- "@36@0:8@16B24d28"
- "@36@0:8q16f24@28"
- "@40@0:8@16d24@32"
- "@40@0:8i16d20@28i36"
- "@40@0:8i16f20@24@32"
- "@48@0:8@16@24@32^@40"
- "@48@0:8@16@24^@32^@40"
- "@48@0:8@16d24B32@36B44"
- "@56@0:8@16@24@32@40^@48"
- "@56@0:8@16@24@32B40B44B48B52"
- "@56@0:8@16@24q32@40@48"
- "@60@0:8@16@24B32@36@44@?52"
- "@64@0:8@16@24B32@36@44B52@?56"
- "@64@0:8@16@24q32@40@48@56"
- "@?32@0:8@16d24"
- "@?36@0:8@16B24d28"
- "ADAPTABLE Loading adapted model from %@"
- "ANY recipients.identifier CONTAINS %@"
- "About to log accuracy CA feedback dictionary: %@"
- "AdaptMLModel config: %@, amount of data: %ld"
- "Adaptable ML file extension change failed with error：%@"
- "Adaptable ML model at path %@ load failed with error：%@"
- "Adaptable ML model cloning to intermediate ML model is unsuccessful"
- "AdaptableRuleImportancePredictor.mlmodelc"
- "AdaptableRuleImportancePredictor.mlmodelc.archivedMLModel"
- "AdaptableRuleImportancePredictor.mlmodelc.zip"
- "AdaptableRuleImportancePredictor.xgboost"
- "Adapted ML model Recipe ID: %@"
- "AdaptedRuleImportancePredictor.mlmodelc"
- "Amount of data for evaluation: %ld"
- "Amount of predictions, %ld"
- "Amount of sharing sessions used for personalization: %ld"
- "Arrived in NEW _getDataStatistics method"
- "Arrived in NEW evaluateWithModel method"
- "Arrived in NEW personalize method"
- "Asked to stop"
- "Attempting to discard persisted models deployed via Trial, if a treatment is rolled back from this client."
- "B24@?0@8^B16"
- "B40@0:8@\"NSURL\"16@\"NSDictionary\"24@\"NSDictionary\"32"
- "B40@0:8@16@24i32i36"
- "B48@0:8@16@24@32@40"
- "BMBehaviorRetriever"
- "BMHourSlotForHourOfDay"
- "BMItem"
- "BMItemType"
- "BMRetrievalFilter"
- "BalanceSamplesByClass"
- "BatchSize"
- "BoltTaskID"
- "CDModelDataStreamIdentifier"
- "CDQuery"
- "Cache is available, fetching cached suggestions"
- "CalculatedPositiveSampleWeight"
- "Candidate model config: %@ model tag: %@"
- "Candidate model in evaluateWithModel had a nil coreDuet query!! Not ok!"
- "Candidate model in personalize had a nil coreDuet query!! Not ok!"
- "Candidate model query predicate: %@"
- "Candidate model stream id: %@"
- "Candidate model was default, not ok!!"
- "ClassLearningRates"
- "ClassThreshold"
- "Cloning adaptable ML model to intermediate model and loading it was successful"
- "Compilation of coreML model complete"
- "Computation and reporting of 1st order gradients: %@"
- "Computation and reporting of 2nd order gradients: %@"
- "Computation of 1st order gradients complete"
- "Computation of 2nd order gradients complete"
- "ComputeFirstOrderGradients"
- "ComputeSecondOrderGradients"
- "Computed ephemeral features %{private}@"
- "Computing ephemeral features"
- "Config: %@"
- "Contact ranker ML Model: Deployed default model is loaded to be used in suggestions from path: %@"
- "Contact ranker ML Model: Trial model is loaded to be used in suggestions from path: %@"
- "ContactRankerModel.mlmodelc"
- "CoreBehavior - Extension Suggester Number of Rules: %@"
- "CoreBehavior - People Suggester ML model threshold: %@"
- "CoreBehavior - People Suggester ML model version: %@"
- "CoreBehavior - People Suggester Number of Rules: %@"
- "CoreBehavior - People Suggester Suggestion proxy: %@ %@ %@"
- "CoreBehavior - _PSRuleMiningIsMLModelInUse: %s"
- "CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent"
- "CoreBehaviorAnalysisPETCoreBehaviorAnalysisEvent.m"
- "Could not find any interaction matching seed suggestion %@"
- "Curare evaluation and dignostics framework will be used"
- "DEFAULT Loading adapted model from %@"
- "DESRecipeEvaluation"
- "DESRecordStore"
- "Default ML Model loaded successfully"
- "Demo mode"
- "Deployed adaptable ML model already exist, no need to unzip"
- "Deployed adaptable ML model cannot be found, therefore adaptation is halted"
- "Deployed archieved adaptable ML model cannot be found under path %@"
- "Deployed default model is loaded for adaptation from path: %@"
- "Depth"
- "Discarding adapted model failed at path:%@"
- "Discarding trial adaptable model failed at path:%@"
- "Discarding trial model failed at path:%@"
- "DodML record writing UUID: %@"
- "Done with persisting featureDict in Knowledge store."
- "EVALUATE Candidate model config: %@ model tag: %@"
- "Element-wise multiplication of result vector with weight vector complete"
- "Element-wise translation of result vector with translate vector complete"
- "Empty archive or filePath when trying to persist _PSConfidenceModelArchive"
- "Error counting interactions for totalMessagesRecieved: %@"
- "Error counting interactions for totalMessagesSent: %@"
- "Error counting interactions for totalShares: %@"
- "Error getting sample point into MLDictionaryFeatureProvider format with error:%@"
- "Error in dodML record creation: %@"
- "Error with reading from Archive for confidenceModel."
- "Error with unarchiving confidenceModel data."
- "Evaluation of results aggregating 1st order gradients left and right of splits for GBDT questions from recipe complete"
- "Evaluation of results aggregating 2nd order gradients left and right of splits for GBDT questions from recipe complete"
- "EvaluationDataSource"
- "Extracting constant features for the rule ranking ML model"
- "Extraction of input vectors and targets from records into arrays complete"
- "Failed to compile ml model with path:%@, with error：%@"
- "Failed to compile model with error：%@"
- "Failed to compile model."
- "Failed to copy file with path:%@ to path:%@, with error：%@"
- "Failed to copy model file to temporary directory."
- "Failed to create ODCurareEvaluationAndReporting instance with error %@"
- "Failed to get data source with error: %@"
- "Failed to get selected model with error: %@"
- "Failed to load adaptable model config with path:%@, with error：%@"
- "Failed to load model"
- "Failed to load model."
- "Failed to load trial model with compiled model path: %@ with error: %@"
- "Failed to remove old model file."
- "Failed to run evaluateMetricsWithModelURL"
- "Failed to run evaluateWithModelURL with error: %@"
- "Failed to run task with error: %@"
- "Fallback Suggestion"
- "Fetched %@ number of events from CoreDuet store"
- "Fetched %tu cached suggestions: %{private}@"
- "Fetching scene descriptors and save person IDs"
- "FidesPHSEvaluatorDataSource"
- "Finished fetching scene descriptors and saving person IDs"
- "Finished saving people IDs to prediction context"
- "For each feature, report difference between gradients, rather than absolute values: %@"
- "For each node, report difference between gradients, rather than absolute values: %@"
- "Found %d candidates with an empty feature dictionary"
- "FrozenComponentIds"
- "GBDTEvaluator"
- "GBDTQuestions"
- "Got nil return from processDataForStore:recipeInfo:"
- "Got nil return from processDataForStore:taskParameters:"
- "GradientNormFactor"
- "GradientNormType"
- "I24@0:8Q16"
- "I24@0:8d16"
- "ID"
- "In processData"
- "In processDataWithQuery"
- "Init successfully"
- "Initiating rule overlap logging."
- "InputSplice"
- "Interaction being used to generate suggestion %@"
- "Interaction store retrieval error. Recieved messages query: %@"
- "Interaction store retrieval error. Sent call query: %@"
- "Interaction store retrieval error. Sent messages query: %@"
- "Interaction store retrieval error. Sent messages query: %@, Recieved messages query: %@, Shares query: %@"
- "Interaction store retrieval error. Shares query: %@"
- "Interaction store retrieval error. Texting query: %@"
- "IntermediateAdaptableModel.mlmodelc"
- "IntermediateAdaptableModel.xgboost"
- "Knowledge event creation failed."
- "L1Norm"
- "L2Norm"
- "L2NormBound"
- "LOIInContext"
- "LOIInRule"
- "LOIOverlap"
- "LabelMap"
- "LastAdaptationDate"
- "LastRuleOverlapFeedbackDate"
- "LearningRate"
- "LearningRateDecay"
- "Length of targets arrays does not equal length of predictions array"
- "LighthouseShareSheetPFLTraining"
- "Loaded adaptable model config from:%@"
- "Loaded model from %@"
- "Logging feedback for shares since: %@"
- "ML Model: Adapted model is loaded to be used in suggestions from path: %@"
- "ML Model: Deployed default model is loaded to be used in suggestions from path: %@"
- "ML Model: Trial model is loaded to be used in suggestions from path: %@"
- "ML model load to predict with error：%@"
- "ML model load: failed to load ml model with path:%@, with error：%@"
- "MLModelCreatorDefinedKey"
- "MLRTaskResult"
- "MaxSamples"
- "MaxSessions"
- "Messages interaction count: %tu, Sharing interaction count: %tu"
- "Model: %@"
- "ModelDeltas"
- "ModelFileName"
- "ModelHyperparameters"
- "New data is logged token"
- "No"
- "No attachments for event."
- "No model file specified for key 'ModelFileName' in Trial attachment"
- "No model is loaded for adaptation"
- "No valid records for GBDT evaluation"
- "NoGradNorm"
- "Not computing or reporting 1st and 2nd order gradients. This is because ComputeFirstOrderGradients and ComputeSecondOrderGradients in recipe were both set to 0. Set these parameters to 1 if gradients are to be computed and reported. Exiting without computing result."
- "NumLocalIterations"
- "Number of behavior rules to consider for this share event: %@"
- "Number of recipients considering: %@"
- "Number of rows in event: %@"
- "Number of rows used for GBDT training = %lu"
- "Number of share sheet events to be logged: %@"
- "NumberTrainingRecords"
- "NumberTrainingRecordsClass0"
- "NumberTrainingRecordsClass1"
- "NumberTrainingSessions"
- "ODCurareCandidateModel"
- "ODCurareDataCachePruningPolicyObject"
- "ODCurareEvaluationAndReportingModule"
- "ODCurareModelInformation"
- "ODCurareModelSelectionParameter"
- "ODCurareModelSelectionPolicy"
- "ODCurarePersonalizationPolicy"
- "ODCurareReportFillerDataSet"
- "ODCurareReportFillerDataSetSize"
- "ODCurareReportFillerDataSetStats"
- "ODCurareReportFillerModelEvaluation"
- "ODCurareReportFillerModelEvaluationSummary"
- "ODCurareReportFillerModelHyperparameters"
- "ODCurareReportFillerModelInformation"
- "ObjectiveFunction"
- "PERSONALIZE Candidate model config: %@ model tag: %@"
- "PETEventTracker2"
- "PPTopicStore"
- "PSConfidenceModel/confidenceModels.archive"
- "PSDESPlugin"
- "PS_Legacy"
- "PeopleSuggesterSuggestLessFeedback"
- "Personalizing with numTrees: %@, maxDepth: %@"
- "Photos-based features fetching is disabled"
- "Plugin"
- "PositiveSampleWeight"
- "Prediction - ContactRankerModel"
- "Prediction - Corebehavior"
- "Prediction Context - Start to re-order"
- "Predictions of all input vectors from coreML model complete"
- "Prereqs are not satisfied"
- "Received a nil event..."
- "Received an event with a nil or empty feature dictionary..."
- "Remote ML model load attempted with null path"
- "ReportGradientsBothSidesOfSplit"
- "ReportNodeSumGradients"
- "ReportPerFeatureResultDifference"
- "ReportPerNodeResultDifference"
- "Reporting gradients on both sides of split: %@"
- "Reporting right and left gradients for last split evaluated in each node"
- "Reporting sum of gradients in each node"
- "Returned suggestions for demo mode %@"
- "Returning %@ recent non-system suggestions"
- "Returning %tu suggestions"
- "Returning nil from processDataForStore because no positive or negative samples were found, and we need to balance classes, compute weights, or randomly select one of two classes, which will fail."
- "RuleImportancePredictor.mlmodelc"
- "Saving people IDs to prediction context"
- "SessionId"
- "SessionIdDate"
- "Setting adaptationStrategy to: %@"
- "Setting learningRate to: %@"
- "Setting minChildWeight to: %@"
- "Setting numTrees to: %@"
- "ShareSheetFeedback"
- "Shuffling"
- "Size of result vector: %lu"
- "Size of translate vector: %lu"
- "Size of weight vector: %lu"
- "Start of GBDT gradient computation"
- "Suggesting interactions from seeded handles: %@"
- "SumAbsolutePredictionError"
- "SumAccuratePredictions"
- "T@\"<_DKKnowledgeQuerying>\",&,N,V_knowledgeStore"
- "T@\"BMBehaviorRetriever\",R,N,V_behaviorRetriever"
- "T@\"BMRule\",&,N,V_rule"
- "T@\"FidesPHSEvaluatorDataSource\",&,N,V_dataSource"
- "T@\"MLModel\",&,V_mlModel"
- "T@\"MLModelConfiguration\",&,N,V_adaptableModelConfiguration"
- "T@\"NSArray\",&,N,V_behaviorRulesConsideringInTheContext"
- "T@\"NSArray\",&,N,V_recordDatas"
- "T@\"NSArray\",&,N,V_recordInfos"
- "T@\"NSArray\",&,N,V_records"
- "T@\"NSArray\",&,N,V_scores"
- "T@\"NSArray\",C,N,V_scenesInPhotoIdentifiers"
- "T@\"NSArray\",R,N,V_inputVectors"
- "T@\"NSArray\",R,N,V_targetVector"
- "T@\"NSDictionary\",&,N,V_percentiles"
- "T@\"NSDictionary\",&,N,V_processDataReturnDict"
- "T@\"NSDictionary\",&,N,V_selectedFeaturesConfig"
- "T@\"NSDictionary\",&,V_metadata"
- "T@\"NSDictionary\",&,V_psConfigForAdaptableModel"
- "T@\"NSDictionary\",C,N,V_recipe"
- "T@\"NSDictionary\",R,N,V_confidenceModelDictionary"
- "T@\"NSDictionary\",R,N,V_recipe"
- "T@\"NSDictionary\",R,V_metadata"
- "T@\"NSMutableArray\",&,N,V_circularBuffer"
- "T@\"NSMutableArray\",&,N,V_featureMatricesForAllShareEvents"
- "T@\"NSMutableArray\",&,N,V_list"
- "T@\"NSMutableArray\",&,N,V_results"
- "T@\"NSMutableDictionary\",&,N,V_confidenceModelDictionary"
- "T@\"NSMutableDictionary\",&,N,V_constantFeatures"
- "T@\"NSMutableDictionary\",&,N,V_contextFeatures"
- "T@\"NSMutableDictionary\",&,N,V_featureNameDict"
- "T@\"NSMutableDictionary\",&,N,V_features"
- "T@\"NSMutableDictionary\",&,N,V_modelTagToCandidateModel"
- "T@\"NSMutableDictionary\",&,N,V_modelTagToHyperparameters"
- "T@\"NSNumber\",&,N,V_accuracyGainThresholdForSwap"
- "T@\"NSNumber\",&,N,V_batchSize"
- "T@\"NSNumber\",&,N,V_engagementRateGainThresholdForSwap"
- "T@\"NSNumber\",&,N,V_epoc"
- "T@\"NSNumber\",&,N,V_evaluationIterationCount"
- "T@\"NSNumber\",&,N,V_learningRate"
- "T@\"NSNumber\",&,N,V_maxDepth"
- "T@\"NSNumber\",&,N,V_minChildWeight"
- "T@\"NSNumber\",&,N,V_minSampleCountForAdaptation"
- "T@\"NSNumber\",&,N,V_minimumTestDataSizeForSwap"
- "T@\"NSNumber\",&,N,V_numClasses"
- "T@\"NSNumber\",&,N,V_numTrees"
- "T@\"NSNumber\",&,N,V_recipeID"
- "T@\"NSNumber\",&,N,V_recipientUniqueID"
- "T@\"NSNumber\",&,N,V_swapOK"
- "T@\"NSNumber\",&,N,V_testSplitPercent"
- "T@\"NSNumber\",&,N,V_topN"
- "T@\"NSNumber\",C,V_incomingCallTotal"
- "T@\"NSNumber\",C,V_incomingTextTotal"
- "T@\"NSNumber\",C,V_outgoingCallTotal"
- "T@\"NSNumber\",C,V_outgoingTextTotal"
- "T@\"NSNumber\",C,V_shareTotal"
- "T@\"NSString\",&,N,V_adaptableModelDeployPath"
- "T@\"NSString\",&,N,V_confidence"
- "T@\"NSString\",&,N,V_configBoltTaskIDSpecification"
- "T@\"NSString\",&,N,V_configDepthSpecification"
- "T@\"NSString\",&,N,V_configTreeSpecification"
- "T@\"NSString\",&,N,V_modelKey"
- "T@\"NSString\",&,N,V_support"
- "T@\"NSString\",&,N,V_uniqueShareEventIdentifier"
- "T@\"NSString\",&,V_adaptedModelRecipeVersion"
- "T@\"NSString\",C,V_ID"
- "T@\"NSURL\",&,N,V_intermediateCompiledModelURL"
- "T@\"NSUserDefaults\",&,N,V_psAdaptationDefaults"
- "T@\"NSUserDefaults\",&,N,V_ruleOverlapFeedbackDefaults"
- "T@\"ODCurareEvaluationAndReportingModule\",&,N,V_curareEvaluationAndReporting"
- "T@\"PPContactStore\",&,N,V_portraitContactStore"
- "T@\"PPTopicStore\",&,N,V_topicStore"
- "T@\"_CDInteraction\",&,N,V_interaction"
- "T@\"_CDInteraction\",C,V_interaction"
- "T@\"_DKKnowledgeStore\",&,N,V_knowledgeStore"
- "T@\"_PSBehaviorRuleFeatureExtraction\",&,V_feaExtHandle"
- "T@\"_PSConfidenceModelDriver\",&,N,V_confidenceModelDriver"
- "T@\"_PSConfidenceModelForSharing\",&,N,V_confidenceModelForSharing"
- "T@\"_PSConfidenceModelForSharing\",&,V_confidenceModelForSharing"
- "T@\"_PSContactFillerNormalizationConstants\",&,N,V_normConstants"
- "T@\"_PSRuleMiningModel\",&,V_ruleMiningModel"
- "T@\"_PSRuleRankingMLModel\",&,V_ruleRankingModel"
- "T@\"_PSSharingContactFeatureExtraction\",&,V_feaExtractionHandle"
- "T@\"_PSSharingContactRankerMLModel\",&,V_sharingContactRankerMLModel"
- "T@\"_PSSharingContactRankerModel\",&,V_sharingContactRankerModel"
- "T@?,C,N,V_shouldContinue"
- "TB"
- "TB,N,V__PSRuleMiningIsAdaptedMLModelOK"
- "TB,N,V__PSRuleMiningIsMLModelInUse"
- "TB,N,V__PSSharingContactRankerMLModelInUse"
- "TB,N,V_constantFeaturesReady"
- "TB,N,V_contentUrlInContext"
- "TB,N,V_contentUrlInRule"
- "TB,N,V_contentUrlOverlap"
- "TB,N,V_contextFeaturesReady"
- "TB,N,V_evaluateIsInvokedOnce"
- "TB,N,V_isAdaptedMLModelOK"
- "TB,N,V_isWeekendInRule"
- "TB,N,V_isWeekendOverlap"
- "TB,N,V_lOIInContext"
- "TB,N,V_lOIInRule"
- "TB,N,V_lOIOverlap"
- "TB,N,V_personAndAppMatched"
- "TB,N,V_personMatched"
- "TB,N,V_sourceBundleIdInContext"
- "TB,N,V_sourceBundleIdInRule"
- "TB,N,V_sourceBundleIdOverlap"
- "TB,N,V_targetBundleIDInConsequent"
- "TB,N,V_targetBundleIdInContext"
- "TB,N,V_targetBundleIdInRule"
- "TB,N,V_targetBundleIdOverlap"
- "TB,N,V_timeOfDaySlotInRule"
- "TB,N,V_timeOfDaySlotOverlap"
- "TB,N,V_topicInContext"
- "TB,N,V_topicInRule"
- "TB,N,V_topicOverlap"
- "TB,N,V_utiTypeInContext"
- "TB,N,V_utiTypeInRule"
- "TB,N,V_utiTypeOverlap"
- "TB,V__PSConfidenceModelInUse"
- "TB,V_isAdaptedModel"
- "TI,N,V_locationOfInterestContainingRuleCount"
- "TI,N,V_locationOfInterestRulesCardinality"
- "TI,N,V_photoContactContainingRuleCount"
- "TI,N,V_photoContactInContext"
- "TI,N,V_photoContactInRule"
- "TI,N,V_photoContactOverlap"
- "TI,N,V_photoContactRulesCardinality"
- "TI,N,V_photoSceneContainingRuleCount"
- "TI,N,V_photoSceneInContext"
- "TI,N,V_photoSceneInRule"
- "TI,N,V_photoSceneOverlap"
- "TI,N,V_photoSceneRulesCardinality"
- "TI,N,V_sourceBundleIdContainingRuleCount"
- "TI,N,V_sourceBundleIdRulesCardinality"
- "TI,N,V_targetBundleIdContainingRuleCount"
- "TI,N,V_targetBundleIdRulesCardinality"
- "TI,N,V_topicContainingRuleCount"
- "TI,N,V_topicRulesCardinality"
- "TI,N,V_totalMessagesRecieved"
- "TI,N,V_totalMessagesSent"
- "TI,N,V_totalShares"
- "Td,N,V__PSRuleMiningMLModelScoreThreshold"
- "Td,N,V__PSRuleMiningModelMinRuleConfidenceForSuggestion"
- "Td,N,V__PSRuleMiningModelMinSupportForSuggestion"
- "Td,N,V__PSSharingContactRankerMLModelScoreThreshold"
- "Td,N,V_score"
- "Td,V_avg"
- "Td,V_max"
- "Td,V_min"
- "Td,V_mode"
- "Td,V_score"
- "Td,V_scoreThreshold"
- "Td,V_stdev"
- "Td,V_sum"
- "Tf,N,V_ruleScore"
- "Ti,V_bufferHead"
- "Ti,V_bufferSize"
- "Ti,V_minimumInstanceCount"
- "Tq,N,V__PSRuleMiningModelDaysToPromoteRecentlyInstalledAppExtensions"
- "Tq,N,V__PSRuleMiningModelRegularizingContextOverlapConstraint"
- "Tq,N,V_adaptationStrategy"
- "Tq,N,V_ruleLabel"
- "TrainLayers"
- "Training"
- "Training data prepped for model adaptation"
- "Translate vector is not the same size as result vector. No translating of results applied."
- "TranslateVector"
- "Tree"
- "Trial model is loaded for adaptation from path: %@"
- "Trial: failed to load trial adaptable model config"
- "Trial: received adaptableModelConfigFilePath path:%@"
- "Trial: received adaptableRuleMinerMLModelFile path:%@"
- "Trial: received ruleMinerMLModelFile path:%@"
- "TrialAdaptableRuleImportancePredictor.mlmodelc"
- "TrialAdaptableRuleImportancePredictor.xgboost"
- "TrialContactRankerModel.mlmodelc"
- "TrialRuleImportancePredictor.mlmodelc"
- "Trying to load model with compiled model path: %@"
- "URLHostAllowedCharacterSet"
- "Unable to decompress adaptable compiled model with error: %@"
- "Unable to query interaction store: %@"
- "Unzipping the adaptable ML model at path: %@ failed"
- "Update task will be initiated with %@ number of samples"
- "Using prediction label name: %@"
- "Validating CoreML model"
- "Weight vector is not the same size as result vector. No weighting of results is being applied."
- "WeightVector"
- "While cloning adaptable model, renaming file with path:%@ to path:%@ failed with error：%@"
- "Yes"
- "Zipped Adaptable ML model copy attempted with null path"
- "Zipped Adaptable ML model copy failed"
- "_DKBehavioralRuleFeaturesMetadataKey-featureDict"
- "_DKEventQuery"
- "_DKEventStream"
- "_ID"
- "_PSBehaviorRuleFeatureExtraction"
- "_PSBehaviorRuleRankingUtilities"
- "_PSConfidenceModel"
- "_PSConfidenceModelArchive"
- "_PSConfidenceModelDriver"
- "_PSConfidenceModelForSharing"
- "_PSContactFillerDataCollectionStatistics"
- "_PSContactFillerDataCollectionUtilities"
- "_PSContactFillerNormalizationConstants"
- "_PSContactFillerRecipient"
- "_PSEnsemble: Getting suggestions for ShareSheet session %@"
- "_PSEnsembleModel_getPhotoBasedFeatures_mdPersonIDsOfPeopleInSharedPhotoAssets"
- "_PSEnsembleModel_getPhotoBasedFeatures_setPhotoAnalysisFromAssetsWithPredictionContext"
- "_PSFeatureStatistics"
- "_PSFeaturizedBehaviorRule"
- "_PSPersonalizationEvaluation"
- "_PSReturnRecentNonSystemSuggestions"
- "_PSRuleMiningIsAdaptedMLModelOK"
- "_PSRuleMiningIsMLModelInUse"
- "_PSRuleMiningMLModelScoreThreshold"
- "_PSRuleMiningModel"
- "_PSRuleMiningModelDaysToPromoteRecentlyInstalledAppExtensions"
- "_PSRuleMiningModelFeatureSet"
- "_PSRuleMiningModelMinRuleConfidenceForSuggestion"
- "_PSRuleMiningModelMinSupportForSuggestion"
- "_PSRuleMiningModelRegularizingContextOverlapConstraint"
- "_PSRuleOverlapFeedback"
- "_PSRuleRankingMLModel"
- "_PSRuleRankingMLModel - People Suggester Extracted featuresList count: %@"
- "_PSRuleRankingMLModel - People Suggester ML model, predictionsFromBatch failure"
- "_PSRuleRankingMLModel - People Suggester ML rule score: %@"
- "_PSRuleRankingMLModel - People Suggester feature extraction MLDictionaryFeatureProvider:initWithDictionary failure"
- "_PSShareSheetFetchSupportedBundleIDs"
- "_PSShareSheetPeopleContactRankerModelSuggestions"
- "_PSShareSheetPeopleMiningSuggestions"
- "_PSShareSheetPeopleSuggestionsMiningFeatureExtraction"
- "_PSShareSheetPeopleSuggestionsMiningMLModelPrediction"
- "_PSSharingContactFeatureExtraction"
- "_PSSharingContactRankerMLModel"
- "_PSSharingContactRankerMLModel - loadDefaultModel"
- "_PSSharingContactRankerMLModelInUse"
- "_PSSharingContactRankerMLModelScoreThreshold"
- "_PSSharingContactRankerModel"
- "_PSSharingContactRankerScoredContact"
- "_PSSuggester: Validate CoreML reply was called"
- "_PSUnarchiverZip returned %@"
- "_PSharingContactRankerMLModelInUse"
- "__PSConfidenceModelInUse"
- "__PSRuleMiningIsAdaptedMLModelOK"
- "__PSRuleMiningIsMLModelInUse"
- "__PSRuleMiningMLModelScoreThreshold"
- "__PSRuleMiningModelDaysToPromoteRecentlyInstalledAppExtensions"
- "__PSRuleMiningModelMinRuleConfidenceForSuggestion"
- "__PSRuleMiningModelMinSupportForSuggestion"
- "__PSRuleMiningModelRegularizingContextOverlapConstraint"
- "__PSSharingContactRankerMLModelInUse"
- "__PSSharingContactRankerMLModelScoreThreshold"
- "_accuracyGainThresholdForSwap"
- "_adaptableModelConfiguration"
- "_adaptableModelDeployPath"
- "_adaptationStrategy"
- "_adaptedModelRecipeVersion"
- "_avg"
- "_behaviorRetriever"
- "_behaviorRulesConsideringInTheContext"
- "_bufferHead"
- "_bufferSize"
- "_circularBuffer"
- "_computeFirstOrderGradientsWithTargets:predictions:positiveSampleWeight:"
- "_computePredictionsFromModelWithInputVectors:currentModel:error:"
- "_computeSecondOrderGradientsWithTargets:predictions:positiveSampleWeight:"
- "_computeSumOfGradientsLeftAndRightOfSplitWithFeature:threshold:inputVectors:gradients:"
- "_confidence"
- "_confidenceModelDictionary"
- "_confidenceModelDriver"
- "_confidenceModelForSharing"
- "_configBoltTaskIDSpecification"
- "_configDepthSpecification"
- "_configTreeSpecification"
- "_constantFeatures"
- "_constantFeaturesReady"
- "_contentUrlInContext"
- "_contentUrlInRule"
- "_contentUrlOverlap"
- "_contextFeatures"
- "_contextFeaturesReady"
- "_curareEvaluationAndReporting"
- "_dataSource"
- "_differenceArrayWithArray:"
- "_engagementRateGainThresholdForSwap"
- "_epoc"
- "_evaluateIsInvokedOnce"
- "_evaluateResultWithGradients:questions:inputVectors:reportGradientsBothSidesOfSplit:reportNodeSumGradients:reportPerFeatureResultDifference:reportPerNodeResultDifference:"
- "_evaluationIterationCount"
- "_feaExtHandle"
- "_feaExtractionHandle"
- "_featureMatricesForAllShareEvents"
- "_featureNameDict"
- "_featureVectorFromSuggestionDate:bundleID:peopleInPhotoIdentifiers:scenesInPhotoIdentifiers:"
- "_findNodeSamplesWithDecisionPath:inputVectors:gradients:"
- "_firstOrderGradientWithPrediction:label:"
- "_getDataStatistics:forData:"
- "_incomingCallTotal"
- "_incomingTextTotal"
- "_inputVectors"
- "_intermediateCompiledModelURL"
- "_isAdaptedMLModelOK"
- "_isAdaptedModel"
- "_isWeekendInRule"
- "_isWeekendOverlap"
- "_l1NormWithArray:"
- "_l2NormWithArray:"
- "_lOIInContext"
- "_lOIInRule"
- "_lOIOverlap"
- "_learningRate"
- "_list"
- "_locationOfInterestContainingRuleCount"
- "_locationOfInterestRulesCardinality"
- "_makeKeysWithInputVectors:"
- "_max"
- "_maxDepth"
- "_min"
- "_minChildWeight"
- "_minSampleCountForAdaptation"
- "_minimumInstanceCount"
- "_minimumTestDataSizeForSwap"
- "_mode"
- "_modelKey"
- "_modelTagToCandidateModel"
- "_modelTagToHyperparameters"
- "_normConstants"
- "_numClasses"
- "_numTrees"
- "_outgoingCallTotal"
- "_outgoingTextTotal"
- "_percentiles"
- "_personAndAppMatched"
- "_personMatched"
- "_photoContactContainingRuleCount"
- "_photoContactInContext"
- "_photoContactInRule"
- "_photoContactOverlap"
- "_photoContactRulesCardinality"
- "_photoSceneContainingRuleCount"
- "_photoSceneInContext"
- "_photoSceneInRule"
- "_photoSceneOverlap"
- "_photoSceneRulesCardinality"
- "_portraitContactStore"
- "_processDataReturnDict"
- "_psAdaptationDefaults"
- "_psConfigForAdaptableModel"
- "_recipeID"
- "_recipientUniqueID"
- "_recordDatas"
- "_recordInfos"
- "_records"
- "_rule"
- "_ruleLabel"
- "_ruleMiningModel"
- "_ruleOverlapFeedbackDefaults"
- "_ruleRankingModel"
- "_ruleScore"
- "_scenesInPhotoIdentifiers"
- "_scoreThreshold"
- "_scores"
- "_secondOrderGradientWithPrediction:"
- "_selectedFeaturesConfig"
- "_shareTotal"
- "_sharingContactRankerMLModel"
- "_sharingContactRankerModel"
- "_shouldContinue"
- "_sigmoidWithValue:"
- "_sourceBundleIdContainingRuleCount"
- "_sourceBundleIdInContext"
- "_sourceBundleIdInRule"
- "_sourceBundleIdOverlap"
- "_sourceBundleIdRulesCardinality"
- "_stdev"
- "_sum"
- "_sumAbsoluteErrorWithPredictions:targets:"
- "_sumAccuratePredictionsWithPredictions:targets:"
- "_support"
- "_swapOK"
- "_targetBundleIDInConsequent"
- "_targetBundleIdContainingRuleCount"
- "_targetBundleIdInContext"
- "_targetBundleIdInRule"
- "_targetBundleIdOverlap"
- "_targetBundleIdRulesCardinality"
- "_targetVector"
- "_testSplitPercent"
- "_timeOfDaySlotInRule"
- "_timeOfDaySlotOverlap"
- "_topN"
- "_topicContainingRuleCount"
- "_topicInContext"
- "_topicInRule"
- "_topicOverlap"
- "_topicRulesCardinality"
- "_topicStore"
- "_totalMessagesRecieved"
- "_totalMessagesSent"
- "_totalShares"
- "_translateResultWithTranslateVector:result:"
- "_uniqueShareEventIdentifier"
- "_utiTypeInContext"
- "_utiTypeInRule"
- "_utiTypeOverlap"
- "_weightResultWithWeightVector:result:"
- "accuracyGainThresholdForSwap"
- "adaptMLModel:withMLModelType:withDataArray:modelConfiguration:"
- "adaptMLModel:withTrainingData:modelConfiguration:"
- "adaptableMLModel"
- "adaptableModelConfiguration"
- "adaptableModelDeployPath"
- "adaptationParameters"
- "adaptationStrategy"
- "adaptedModelRecipeVersion"
- "adaptedModelRecipeVersion.txt"
- "addAdaptedModelUsageInfoToSuggestions:"
- "addEvent:"
- "addEventForModel:event:"
- "addEventForModel:forUseCaseKey:event:"
- "addHyperparameterIndices:"
- "addHyperparameterValues:"
- "addModelEvaluationResults:"
- "addStats:"
- "addValue:"
- "allData"
- "antecedent"
- "anyObject"
- "attachmentURLsForBasename:"
- "avg"
- "batchPredictWithAdaptedMLModel - MLMultiArray creation failure"
- "batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featureDictArray:"
- "batchPredictWithAdaptedMLModel:psConfigForAdaptableModel:featurizedRules:"
- "batchPredictWithMLModel - feature extraction MLArrayBatchProvider:initWithDictionary failure"
- "batchPredictWithMLModel - predictionsFromBatch failure"
- "batchPredictWithMLModel:featureArrayDict:"
- "batchSize"
- "behaviorRetriever"
- "behaviorRulesConsideringInTheContext"
- "behavioralRuleFeaturesStream"
- "binary accuracy"
- "binary accuracy class 0"
- "binary accuracy class 1"
- "binary:logistic"
- "binaryAccuracy"
- "binaryAccuracyClass0"
- "binaryAccuracyClass0_NumPositiveSamples"
- "binaryAccuracyClass0_NumSamples"
- "binaryAccuracyClass1"
- "binaryAccuracyClass1_NumPositiveSamples"
- "binaryAccuracyClass1_NumSamples"
- "binaryAccuracy_NumPositiveSamples"
- "binaryAccuracy_NumSamples"
- "boolValueForKey:defaultValue:"
- "bothMatched"
- "bucketedValue:"
- "bufferHead"
- "bufferSize"
- "bundleIdOfHostOpenedShareExtension"
- "bundleIdOfShareExtensionOpened"
- "calculateNormContantsGivenInteractionStore:normConstants:"
- "calculateNormalizedCallingFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:direction:"
- "calculateNormalizedShareFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:"
- "calculateNormalizedTextingFrequencyForContactGivenContactIdPredicate:totalFrequency:numberOfDaysToLookBack:timeOfShareInteraction:interactionStore:direction:"
- "calculateStats"
- "calculateTimeBucketGivenInteraction:timeOfShareInteraction:"
- "calculateTimeSinceLastCallForContactGivenContactIdPredicate:direction:timeOfShareInteraction:interactionCache:"
- "calculateTimeSinceLastShareForContactGivenContactIdPredicate:timeOfShareInteraction:interactionCache:"
- "calculateTimeSinceLastTextForContactGivenContactIdPredicate:direction:timeOfShareInteraction:interactionCache:"
- "candidateToScore: %{private}@"
- "chatGuidsAndTransports is not of type NSArray as expected"
- "circularBuffer"
- "classLearningRates"
- "classThreshold"
- "classicMLModel"
- "cloneAdaptableModel:toFilePath:originalXgboostModelName:clonedXgboostModelName:"
- "com.apple.CoreBehaviorRuleFeedback"
- "com.apple.LighthouseShareSheetPFLPlugin"
- "com.apple.PeopleSuggester.Config.Default.AdaptableModel"
- "com.apple.PeopleSuggester.Config.SelectedFeatures.plist"
- "com.apple.PeopleSuggester.DeducedSharingIntentFeedback"
- "com.apple.PeopleSuggester.ProactiveShareSheetLighthousePFLPlugin"
- "com.apple.PeopleSuggester.RulesOverlap"
- "com.apple.PeopleSuggester.SeedSuggestions"
- "com.apple.PeopleSuggester.dodML"
- "com.apple.PeopleSuggester.personalization"
- "compileMLModelAtPath:"
- "compileModelAtURL:error:"
- "computeEphemeralFeaturesWithPredictionContext:"
- "computeFirstOrderGradients"
- "computeSASSFeatureWithScenesDetectedInPhoto:andConfiguredScenes:"
- "computeSecondOrderGradients"
- "computeShareSheetEphemeralFeaturesWithPredictionContext:"
- "computeShareSheetEphemeralFeaturesWithPredictionContext:reply:"
- "confidenceModelDictionary"
- "confidenceModelDriver"
- "confidenceModelForSharing"
- "configBoltTaskIDSpecification"
- "configDepthSpecification"
- "configTreeSpecification"
- "consequent"
- "constantFeatures"
- "constantFeaturesFromContextItems:"
- "constantFeaturesReady"
- "constantPETFeaturesFromContextItems:"
- "contact ranker model"
- "contactFillerBucketedValue:"
- "contactFillerFeedbackEvent ready to be logged"
- "contentUrlInContext"
- "contentUrlInRule"
- "contentUrlOverlap"
- "contextFeatures"
- "contextFeaturesReady"
- "contextItemsFromEvent:"
- "conviction"
- "copyFileFromURL:toURL:"
- "copyItemAtPath:toPath:error:"
- "copyRemoteRuleMinerMLModel:"
- "copyZippedAdaptableModel:"
- "countEvents: %@"
- "countInteractionsUsingPredicate:error:"
- "createDataSourceForDodMLRecipe:error:"
- "createDataSourceForRecipe:error:"
- "createMLArrayBatchProviderWithMLModelType:withDataArray:"
- "createMLFeatureProviderArrayFromSingleShareEventData:"
- "createMLFeatureProviderArrayFromSingleShareEventData:forMLModel:"
- "curareEvaluationAndReporting"
- "d24@0:8d16"
- "data point dimension: %@"
- "dataSource"
- "dataWithBytes:length:"
- "decisionPath"
- "defaultArchivePath"
- "defaultRecipeParams"
- "defaultStore"
- "default_model"
- "deleteArchiveFile"
- "derivedIdentifier"
- "dictionaryWithContentsOfFile:"
- "direction IN %@ && mechanism == %@"
- "direction IN %@ && mechanism IN %@"
- "discardAdaptedModel"
- "discardTrialModels"
- "dodML is loading defaultSelectedFeaturesConfigPath from path: %@"
- "dodML is trying to load deployedCompiledMLModel from path: %@"
- "dodML is trying to load trialCompiledMLModel from path: %@"
- "doesSuggestionProxyMatch:withInteraction:"
- "doesTheRecipientsMatchInInteraction1:interaction2:"
- "enablePhotoBasedFeatures"
- "enforceOneSignificantFigureForDouble:"
- "enforceOneSignificantFigureForSmallDouble:"
- "engagement rate new"
- "engagementRate"
- "engagementRateGainThresholdForSwap"
- "engagementRate_NumPositiveSamples"
- "engagementRate_NumSamples"
- "epoc"
- "evaluateIsInvokedOnce"
- "evaluateMetricsWithModelURL:"
- "evaluateRecipe:matchingRecordSet:binaryResult:error:"
- "evaluateRecipe:matchingRecordSet:error:"
- "evaluateRecipe:recordInfo:recordData:attachments:error:"
- "evaluateWithModel:"
- "evaluateWithModelURL:dataSource:processDataReturnDict:error:"
- "evaluatedRule"
- "evaluationIterationCount"
- "eventWithStream:startDate:endDate:identifierStringValue:metadata:"
- "extractAdaptedModelRecipeID"
- "extractConstantFeaturesForMLModelIntoFeatures:"
- "extractConstantFeaturesInto:"
- "extractContextMatchFeatures:features:"
- "extractFeaturesFromBehaviorRulesIntoPETMessage:behaviorRules:MLModelScores:"
- "extractFeaturesFromBehaviorRulesIntoPETMessage:behaviorRules:contextItems:ruleRankingModel:"
- "extractFeaturesGivenRule:contextItems:features:"
- "extractFeaturesInto:withPredictionContext:forContactId:forInteraction:behaviorRulesConsideringInTheContext:ruleRankingMLModelScores:interactionModelScores:"
- "extractFrequencyRecencyFeaturesIntoPETMessage:recipientID:interaction:normConstants:numberOfDaysToLookBack:interactionStore:timeOfShareInteraction:contactPropertyCache:interactionCache:"
- "extractUserFeaturesIntoPETMessage:normConstants:behaviorRetriever:"
- "f24@0:8f16f20"
- "feaExtHandle"
- "feaExtractionHandle"
- "featureDict"
- "featureMatricesForAllShareEvents"
- "featureNameDict"
- "featureNameDict: %@"
- "feedbackPETPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:"
- "feedbackPayloadForRule:ForInteraction:ForContextItems:WithConstantFeatures:"
- "filterByRegularizingRules:invalidatedByAnyConflictingItems:containingItemTypes:"
- "filterByRegularizingRulesByContextOverlap:regulularizeItems:queryItems:regularizationConstraint:"
- "filterIDSReachable"
- "filterRulesBasedOnInteractionGivenRuleList:interaction:"
- "filterWithOperand:inclusionOperator:items:"
- "filterWithOperand:inclusionOperator:types:"
- "findObjectWithID:inArray:"
- "floatValueForKey:defaultValue:"
- "freezeComponents"
- "generateCandidateModels"
- "generateResultsDictionayWithModelURL:error:"
- "getAdaptedCompiledMLModelPath"
- "getAdaptedModelRecipeVersionFilePath"
- "getAdaptedModelVersion"
- "getArchivedDefaultAdaptableModelPath"
- "getBehaviorRulesGivenContext:behaviorRetriever:"
- "getCacheSuggestions"
- "getConfidence"
- "getConfidenceForModel:"
- "getConfidenceForModel:forUseCaseKey:"
- "getConfidenceRankedModelKeysGivenKeysToSort:"
- "getDeployedAdaptableCompiledMLModelPath"
- "getDeployedCompiledMLModelPath"
- "getDeployedCompiledMLModelPathForContactRanker"
- "getDictionaryFromArchiveAtPath:"
- "getInteractionModelScoreForEvent:forInteractionRecipients:"
- "getInteractionModelScoreForSuggestions:forInteractionRecipients:"
- "getInteractionRecipientFromInteraction:"
- "getIntermediateAdaptableCompiledMLModel"
- "getLatestTrialMLModelVersion"
- "getListOfContactsFromCashedMessagesInteraction:cashedShareInteractions:"
- "getListOfContactsInteractedInTheLastNumberOfDays - Number of interactions : %@"
- "getListOfContactsInteractedInTheLastNumberOfDays:interactionStore:limit:"
- "getOrMakeConfidenceModelDictionary"
- "getPhotoBasedFeatures"
- "getPhotoBasedFeatures:"
- "getPhotoBasedFeaturesAsync:withTimeout:"
- "getRuleMiningSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:"
- "getSelectedModel:"
- "getSessionID"
- "getTrialCompiledAdaptableMLModelPath"
- "getTrialCompiledMLModelPath"
- "getTrialCompiledMLModelPathForContactRanker"
- "getZippedDefaultAdaptableModelPath"
- "giveModelDescription"
- "gradNormFactor"
- "gradNormType"
- "hasInitializedCache"
- "hasPersonAndAppMatched"
- "hasPersonMatched"
- "hasTopicContainingRuleCount"
- "hasTopicInContext"
- "hasTopicInRule"
- "hasTopicOverlap"
- "hasTopicRulesCardinality"
- "hourOfDaySlot"
- "hyperRecencyHeuristicPredictedInteractionRank"
- "hyperparametersForCandidateModel:"
- "i48@0:8@16@24@32@40"
- "inPhoneCallHeuristicPredictedInteractionRank"
- "incomingCallTotal"
- "incomingTextTotal"
- "initContactPropertyCache:timeOfShareInteraction:interactionStore:"
- "initWithAdaptableModelConfig:isAdaptedMLModelOK:scoreThreshold:"
- "initWithBufferSize:minimumInstanceCount:"
- "initWithBufferSize:sum:circularBuffer:bufferHead:"
- "initWithBundleIdentifier:"
- "initWithBundleIdentifier:dataProviderInstance:evaluationInstance:personalizationInstance:pruningPolicy:error:"
- "initWithConfidenceModelDictionary:"
- "initWithConfig:"
- "initWithInteractionStore:messageInteractionCache:shareInteractionCache:"
- "initWithJSONResult:unprivatizedVector:"
- "initWithKnowledgeStore:contactresolver:withConfig:"
- "initWithLabel:score:recipientUniqueID:"
- "initWithList:"
- "initWithMLModel:scoreThreshold:"
- "initWithMLModel:scoreThreshold:isAdaptedModel:psConfigForAdaptableModel:isAdaptedMLModelOK:"
- "initWithMaximumNumberOfDays:maximumNumberOfEvents:"
- "initWithMetadata:"
- "initWithMetadata:interactionStore:"
- "initWithMetricName:percentageIncrease:"
- "initWithModelInformation:modelURL:"
- "initWithModelKey:score:"
- "initWithModelSelectionParameters:minimumNumberOfEvaluations:minimumNumberOfSamples:"
- "initWithModelSelectionParameters:minimumNumberOfSamplesForPersonalization:minimumNumberOfSamplesForPersonalizationSelection:"
- "initWithModelURL:withCoreDuetStreamIdentifier:andMetadata:"
- "initWithNumTrees:learningRate:minChildWeight:adaptationStrategy:"
- "initWithRecipe:inputVectors:targetVector:error:"
- "initWithRecipe:knowledgeStore:shouldContinueBlock:"
- "initWithRule:score:features:"
- "initWithScore:interaction:"
- "initWithScoreThreshold:"
- "initialize"
- "input"
- "inputSplice"
- "inputVectors"
- "integerValueForKey:defaultValue:"
- "interactionContentURL"
- "interactionExtractedTopicFromAttachment"
- "interactionPhotoContact"
- "interactionPhotoScene"
- "interactionSharingSourceBundleID"
- "interactionStoreEventsSinceDate:"
- "interactionTargetBundleID"
- "interactionUTIType"
- "intermediateCompiledModelURL"
- "isAdaptedMLModelOK"
- "isAdaptedModel"
- "isDefaultModel"
- "isPersonalizableModel"
- "isWeekend"
- "isWeekendInRule"
- "isWeekendOverlap"
- "itemWithType:numberValue:"
- "itemWithType:stringValue:"
- "knnExpanseSessionsAllAndAppFilterOnPredictedInteractionRank"
- "knnExpanseSessionsAllPredictedInteractionRank"
- "knnExpanseSessionsTopAndAppFilterOnPredictedInteractionRank"
- "knnExpanseSessionsTopPredictedInteractionRank"
- "knnNonShareInteractionsInteractionRank"
- "knnPredictedInteractionRank"
- "knnSharesAllAndAppFilterOnPredictedInteractionRank"
- "knnSharesAllPredictedInteractionRank"
- "knnSharesTopAndAppFilterOnPredictedInteractionRank"
- "knnSharesTopPredictedInteractionRank"
- "knnSuggestionBasedOnExpanseSessionsAllAndAppFilterOnProxiesKey"
- "knnSuggestionBasedOnExpanseSessionsAllProxiesKey"
- "knnSuggestionBasedOnExpanseSessionsTopAndAppFilterOnProxies"
- "knnSuggestionBasedOnExpanseSessionsTopProxies"
- "knowledge store events with data: %@"
- "knowledgeEvents parsing, number of events: %@"
- "knowledgeStore executeQuery failed with error: %@"
- "l2NormBound"
- "lOIInContext"
- "lOIInRule"
- "lOIOverlap"
- "labelMap"
- "lastPathComponent"
- "laterDate:"
- "layersToTrain"
- "learningRate"
- "learningRateDecay"
- "lift"
- "list"
- "loadAdaptableModelConfig is invoked with config file path: %@"
- "loadAdaptableModelConfig:"
- "loadAdaptableModelUnderDirectory:"
- "loadDefaultAdaptableModelConfig"
- "loadDefaultModel"
- "loadDefaultRuleMinerMLModel"
- "loadDeployedAdaptableModelUnderDirectory:"
- "loadMLModel"
- "loadMLModel is invoked with model path: %@"
- "loadMLModel:modelConfig:"
- "loadMLModelConfigurationWithConfigDict:"
- "locationIdentifier"
- "locationOfInterestContainingRuleCount"
- "locationOfInterestRulesCardinality"
- "loggingForKnowledgeStoreEvent:WithMatchingInteraction:"
- "loggingTrainDataForContactFillerModel:withMatchingInteraction:interactionRecipients:ruleRankingModel:contactPropertyCache:interactionCache:"
- "matchFeedbackEvent:WithInteractions:"
- "max"
- "maxDepth"
- "mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:"
- "mechanism == %@"
- "min"
- "minChildWeight"
- "minSampleCountForAdaptation"
- "minimumInstanceCount"
- "minimumTestDataSizeForSwap"
- "miningPredictedInteractionRank"
- "miningSuggestionProxies"
- "mlModelVersion"
- "mode"
- "modelAccuracyLogging:WithMatchingInteraction:"
- "modelKey"
- "modelSuggestionProxiesDict - counts: %@"
- "modelSuggestionProxiesDict: %{private}@"
- "modelTag"
- "modelTagToCandidateModel"
- "modelTagToHyperparameters"
- "modelURLs had a length not equal to 1: %lu"
- "model_%d"
- "moveItemAtPath:toPath:error:"
- "nil"
- "nil != self->_confidence"
- "nil != self->_support"
- "nil != self->_uniqueShareEventIdentifier"
- "normConstants"
- "numClasses"
- "numLocalIterations"
- "numTrees"
- "number of data points: %@"
- "numberFromString:"
- "numberOfUserSamples"
- "objc"
- "objective"
- "objectiveFunction"
- "objectsPassingTest:"
- "outgoingCallTotal"
- "outgoingTextTotal"
- "parameters"
- "peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:shouldUseMDID:withCompletion:"
- "percentiles"
- "performEvaluation:"
- "performPrerequisitesBeforeAdaptationWithFeaturesConfigDeployPath:"
- "personAndAppMatched"
- "personMatched"
- "personalizeModel return: ODCurareModelInformation: %@"
- "personalizeModel:"
- "phPersonIdentifiersOfPeopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:"
- "photoAssetHeuristicPredictedInteractionRank"
- "photoAssetOrMomentHeuristicPredictedInteractionRank"
- "photoContactContainingRuleCount"
- "photoContactInContext"
- "photoContactInRule"
- "photoContactOverlap"
- "photoContactRulesCardinality"
- "photoGroupHeuristicPredictedInteractionRank"
- "photoSceneContainingRuleCount"
- "photoSceneInContext"
- "photoSceneInRule"
- "photoSceneOverlap"
- "photoSceneRulesCardinality"
- "portraitContactStore"
- "portraitContactSuggestionProxies"
- "posCount: %@"
- "precalculateConstantFeatures"
- "predicate"
- "predicateFormat"
- "predictWithMLModel - feature extraction MLDictionaryFeatureProvider:initWithDictionary failure"
- "predictWithMLModel - predictionFromFeatures failure"
- "predictWithMLModel:featureDictArray:"
- "predictedClass"
- "predictedValue"
- "predictionContext_scenesInPhotoIdentifiers"
- "processDataForMetricEvaluationForStore:"
- "processDataForStore:recipeInfo:"
- "processDataForStore:taskParameters:"
- "processDataReturnDict"
- "processDataWithQuery:balanceNeed:"
- "psAdaptableModelConfigFactor"
- "psAdaptableRuleMinerMLModelFactor"
- "psAdaptationDefaults"
- "psConfigForAdaptableModel"
- "psRuleMinerMLModelFactor"
- "psRuleMinerMLModelVersionFactor"
- "psr_getPhotoBasedFeaturesAsync"
- "psr_getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:withTimeout:"
- "publisherWithUseCase:options:"
- "q24@?0@\"BMRule\"8@\"BMRule\"16"
- "q24@?0@\"_PSFeaturizedBehaviorRule\"8@\"_PSFeaturizedBehaviorRule\"16"
- "q24@?0@\"_PSSharingContactRankerScoredContact\"8@\"_PSSharingContactRankerScoredContact\"16"
- "rankRules:contextItems:"
- "recipeID"
- "recipientAndBundleIDAsInteger"
- "recipientPredictedCorrectlyByRule:interaction:bundleId:"
- "recipientUniqueID"
- "recordDatas"
- "recordInfos"
- "records"
- "reformatFeaturesInFeatureDictArray:"
- "reformatFeaturesInFeaturizedBehaviorRuleArray:"
- "registerModelKey:forUseCaseKey:confidenceWindowSize:minimumInstanceCount:"
- "removeFolderAtPath:"
- "replaceObjectAtIndex:withObject:"
- "reportGradientsBothSidesOfSplit"
- "reportNodeSumGradients"
- "reportPerFeatureResultDifference"
- "reportPerNodeResultDifference"
- "resetBuffer"
- "resolveUniqueContactIdGivenInteraction:"
- "retrieveRulesWithFilters:"
- "retrieveRulesWithSupport:confidence:filters:"
- "reviewLastDayOfShares"
- "rule"
- "ruleLabel"
- "ruleMiningModel"
- "ruleOverlapFeedbackDefaults"
- "rulePowerFactor"
- "ruleRankingModel"
- "ruleScore"
- "runAdaptationAndEvaluation"
- "runAdaptationAndEvaluationWithFeaturesConfigDeployPath:adaptableModelDeployPath:"
- "runTask:knowledgeStore:error:"
- "runWithRecipeInfo:knowledgeStore:error:"
- "saveRecordWithData:recordInfo:completion:"
- "scenesBasedFeaturesNames"
- "scenesInPhotoIdentifiers"
- "scoreRanking:forModelKey:"
- "scoreThreshold"
- "scoredModel"
- "scoredRule"
- "scores"
- "scoresOnFeatures:"
- "scoresOnRules:contextItems:"
- "seedSuggestionsForChatGuidsAndTransports:"
- "selectedFeaturesConfig"
- "sender.identifier CONTAINS %@"
- "serverSafeRecordInfoWithRecordInfo:"
- "session_id"
- "setAccuracyGainThresholdForSwap:"
- "setAdaptableModelConfiguration:"
- "setAdaptableModelDeployPath:"
- "setAdaptationStrategy:"
- "setAdaptedModelRecipeVersion:"
- "setAvg:"
- "setBatchSize:"
- "setBehaviorRulesConsideringInTheContext:"
- "setBufferHead:"
- "setBufferSize:"
- "setByAddingObject:"
- "setCircularBuffer:"
- "setConfidence:"
- "setConfidenceModelDictionary:"
- "setConfidenceModelDriver:"
- "setConfidenceModelForSharing:"
- "setConfigBoltTaskIDSpecification:"
- "setConfigDepthSpecification:"
- "setConfigTreeSpecification:"
- "setConstantFeatures:"
- "setConstantFeaturesReady:"
- "setContentUrlInContext:"
- "setContentUrlInRule:"
- "setContentUrlOverlap:"
- "setContextFeatures:"
- "setContextFeaturesReady:"
- "setCurareEvaluationAndReporting:"
- "setDataSource:"
- "setDataUsedToEvaluateModel:"
- "setDataUsedToPersonalizeModel:"
- "setEngagementRateGainThresholdForSwap:"
- "setEpoc:"
- "setEvaluateIsInvokedOnce:"
- "setEvaluationIterationCount:"
- "setEventStreams:"
- "setFeaExtHandle:"
- "setFeaExtractionHandle:"
- "setFeatureMatricesForAllShareEvents:"
- "setFeatureName:"
- "setFeatureNameDict:"
- "setFeatureValueMax:"
- "setFeatureValueMean:"
- "setFeatureValueMin:"
- "setFeatureValuePercentile10:"
- "setFeatureValuePercentile25:"
- "setFeatureValuePercentile50:"
- "setFeatureValuePercentile75:"
- "setFeatureValuePercentile90:"
- "setFeatureValueStd:"
- "setFeatures:"
- "setHasInitializedCache:"
- "setHasPersonAndAppMatched:"
- "setHasPersonMatched:"
- "setHasTopicContainingRuleCount:"
- "setHasTopicInContext:"
- "setHasTopicInRule:"
- "setHasTopicOverlap:"
- "setHasTopicRulesCardinality:"
- "setID:"
- "setIncomingCallTotal:"
- "setIncomingTextTotal:"
- "setInteraction:"
- "setIntermediateCompiledModelURL:"
- "setIsAdaptedMLModelOK:"
- "setIsAdaptedModel:"
- "setIsDefaultModel:"
- "setIsPersonalizableModel:"
- "setIsWeekendInRule:"
- "setIsWeekendOverlap:"
- "setLOIInContext:"
- "setLOIInRule:"
- "setLOIOverlap:"
- "setLastDayOfAdaptation:"
- "setLearningRate:"
- "setLimit:"
- "setList:"
- "setLocationOfInterestContainingRuleCount:"
- "setLocationOfInterestRulesCardinality:"
- "setMax:"
- "setMaxDepth:"
- "setMetricName:"
- "setMetricValue:"
- "setMin:"
- "setMinChildWeight:"
- "setMinSampleCountForAdaptation:"
- "setMinimumInstanceCount:"
- "setMinimumTestDataSizeForSwap:"
- "setMode:"
- "setModelHyperparameters:"
- "setModelKey:"
- "setModelTag:"
- "setModelTagToCandidateModel:"
- "setModelTagToHyperparameters:"
- "setNormConstants:"
- "setNumClasses:"
- "setNumTrees:"
- "setNumberOfPositiveSamples:"
- "setNumberOfSamples:"
- "setNumberOfUserSamples:"
- "setNumberOfUserSessions:"
- "setNumberStyle:"
- "setOffset:"
- "setOutgoingCallTotal:"
- "setOutgoingTextTotal:"
- "setParameters:"
- "setParametersForHyperparmeters:"
- "setParametersFromRecipe"
- "setParametersFromRecipeForCandidateModel:"
- "setPeopleAnalysisFromAssetsWithPredictionContext:identifiersOfPeopleInPhotos:"
- "setPercentiles:"
- "setPersonAndAppMatched:"
- "setPersonMatched:"
- "setPhotoAnalysisFromAssetsWithPredictionContext:"
- "setPhotoContactContainingRuleCount:"
- "setPhotoContactInContext:"
- "setPhotoContactInRule:"
- "setPhotoContactOverlap:"
- "setPhotoContactRulesCardinality:"
- "setPhotoSceneContainingRuleCount:"
- "setPhotoSceneInContext:"
- "setPhotoSceneInRule:"
- "setPhotoSceneOverlap:"
- "setPhotoSceneRulesCardinality:"
- "setPortraitContactStore:"
- "setProcessDataReturnDict:"
- "setPsAdaptationDefaults:"
- "setPsConfigForAdaptableModel:"
- "setRecipe:"
- "setRecipeID:"
- "setRecipientUniqueID:"
- "setRecordDatas:"
- "setRecordInfos:"
- "setRecords:"
- "setResults:"
- "setRule:"
- "setRuleLabel:"
- "setRuleMiningModel:"
- "setRuleOverlapFeedbackDefaults:"
- "setRuleRankingModel:"
- "setRuleScore:"
- "setScenesInPhotoIdentifiers:"
- "setScore:"
- "setScoreThreshold:"
- "setScores:"
- "setSelectedFeaturesConfig:"
- "setShareTotal:"
- "setSharingContactRankerMLModel:"
- "setSharingContactRankerModel:"
- "setShouldContinue:"
- "setSize:"
- "setSourceBundleIdContainingRuleCount:"
- "setSourceBundleIdInContext:"
- "setSourceBundleIdInRule:"
- "setSourceBundleIdOverlap:"
- "setSourceBundleIdRulesCardinality:"
- "setStdev:"
- "setSum:"
- "setSupport:"
- "setSwapOK:"
- "setTargetBundleIDInConsequent:"
- "setTargetBundleIdContainingRuleCount:"
- "setTargetBundleIdInContext:"
- "setTargetBundleIdInRule:"
- "setTargetBundleIdOverlap:"
- "setTargetBundleIdRulesCardinality:"
- "setTestSplitPercent:"
- "setTimeOfDaySlotInRule:"
- "setTimeOfDaySlotOverlap:"
- "setTopN:"
- "setTopicContainingRuleCount:"
- "setTopicInContext:"
- "setTopicInRule:"
- "setTopicOverlap:"
- "setTopicRulesCardinality:"
- "setTopicStore:"
- "setTotalMessagesRecieved:"
- "setTotalMessagesSent:"
- "setTotalShares:"
- "setUniqueShareEventIdentifier:"
- "setUtiTypeInContext:"
- "setUtiTypeInRule:"
- "setUtiTypeOverlap:"
- "setVersionNumber:"
- "set_PSConfidenceModelInUse:"
- "set_PSRuleMiningIsAdaptedMLModelOK:"
- "set_PSRuleMiningIsMLModelInUse:"
- "set_PSRuleMiningMLModelScoreThreshold:"
- "set_PSRuleMiningModelDaysToPromoteRecentlyInstalledAppExtensions:"
- "set_PSRuleMiningModelMinRuleConfidenceForSuggestion:"
- "set_PSRuleMiningModelMinSupportForSuggestion:"
- "set_PSRuleMiningModelRegularizingContextOverlapConstraint:"
- "set_PSSharingContactRankerMLModelInUse:"
- "set_PSSharingContactRankerMLModelScoreThreshold:"
- "shadowEvaluationModels"
- "shareTotal"
- "sharesheet"
- "sharesheetFeedbackEventsSinceDate:"
- "sharingContactRankerInteractionRank"
- "sharingContactRankerMLModel"
- "sharingContactRankerModel"
- "sharingContactRankerModel - loadMLModel"
- "sharingContactRankerModel - updateModelProperties"
- "sharingContactRankerModelSuggestionProxies"
- "shouldContinue"
- "shouldDownloadAttachmentWithURL:recipe:recordInfo:"
- "shuffle"
- "softlink:o:path:/System/Library/PrivateFrameworks/BehaviorMiner.framework/BehaviorMiner"
- "softlink:o:path:/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet"
- "softlink:o:path:/System/Library/PrivateFrameworks/DistributedEvaluation.framework/DistributedEvaluation"
- "softlink:o:path:/System/Library/PrivateFrameworks/MLRuntime.framework/MLRuntime"
- "softlink:o:path:/System/Library/PrivateFrameworks/ODCurareEvaluationAndReporting.framework/ODCurareEvaluationAndReporting"
- "softlink:o:path:/System/Library/PrivateFrameworks/ProactiveEventTracker.framework/ProactiveEventTracker"
- "sortDescriptorWithKey:ascending:selector:"
- "sortedScoredModelArray: %@"
- "sourceBundleIdContainingRuleCount"
- "sourceBundleIdInContext"
- "sourceBundleIdInRule"
- "sourceBundleIdOverlap"
- "sourceBundleIdRulesCardinality"
- "splits"
- "stdev"
- "stringValueForKey:defaultValue:"
- "stringWithContentsOfFile:encoding:error:"
- "suggestionPathDemoMode"
- "suggestionProxiesWithPredictionContext:photoSuggestedPeople:supportedBundleIDs:"
- "suggestionProxiesWithPredictionContext:supportedBundleIDs:behaviorRulesConsideringInTheContext:interactionModelSuggestions:ruleRankingMLModelScores:"
- "sum"
- "support"
- "swapOK"
- "targetAppPredictedCorrectlyByRule:bundleId:"
- "targetBundleIDInConsequent"
- "targetBundleIdContainingRuleCount"
- "targetBundleIdInContext"
- "targetBundleIdInRule"
- "targetBundleIdOverlap"
- "targetBundleIdRulesCardinality"
- "targetVector"
- "taskResultFromDict:"
- "telemetryWithRecordSet:"
- "testData"
- "testSplitPercent"
- "timeOfDaySlotInRule"
- "timeOfDaySlotOverlap"
- "topLevelScenesFromSceneNetTags:"
- "topN"
- "topicContainingRuleCount"
- "topicHeuristicPredictedInteractionRank"
- "topicInContext"
- "topicInRule"
- "topicOverlap"
- "topicRulesCardinality"
- "topicStore"
- "totalMessagesRecieved"
- "totalMessagesSent"
- "totalShares"
- "trainAndEvaluateModelsWithCandidateModels:personalizationPolicy:selectionPolicy:error:"
- "trainData"
- "transferConstantFeatures:to:"
- "transferFeaturesFrom:toFeatures:"
- "translateVector"
- "treeRefresh"
- "unarchivedObjectOfClasses:fromData:error:"
- "uniqueShareEventIdentifier"
- "unzipFileWithPath:toFileName:toFolderPath:"
- "updateAdaptableModelConfigWithUpdateType:numTrees:"
- "updateAdaptableModelProperties:"
- "updateMLModelWithURL:withMLModelType:withDataArray:modelConfiguration:"
- "updateTaskForModelAtURL caused error: %@"
- "updateTaskForModelAtURL initiated"
- "updateTaskForModelAtURL is not initiated due to lack of training data"
- "updateTaskForModelAtURL:trainingData:configuration:progressHandlers:error:"
- "updateType"
- "userEvent-normConstants: %@"
- "userEvent: %@"
- "utiTypeInContext"
- "utiTypeInRule"
- "utiTypeOverlap"
- "v16@?0@\"_PSPredictionContext\"8"
- "v24@0:8@\"DESRecipeEvaluationSession\"16"
- "v24@?0@\"NSUUID\"8@\"NSError\"16"
- "v32@0:8q16@24"
- "v32@?0@\"NSString\"8@\"NSObject\"16^B24"
- "v72@0:8@16@24@32@40@48@56@64"
- "v88@0:8@16@24@32@40q48@56@64@72@80"
- "validateCoreMLModelWithRawInput:predictionContext:"
- "validateCoreMLScoringModelWithRawInput:predictionContext:"
- "validateCoreMLScoringModelWithRawInput:predictionContext:reply:"
- "wasInteractionAmongSuggestLess:"
- "wasInteractionRecipientAmongSuggestLess"
- "weightVector"
- "writeArchiveFromDict:"
- "writeRecordObjcWithData:"
- "xent"
- "{?=\"topicContainingRuleCount\"b1\"topicRulesCardinality\"b1\"personAndAppMatched\"b1\"personMatched\"b1\"topicInContext\"b1\"topicInRule\"b1\"topicOverlap\"b1}"
- "||"

```
