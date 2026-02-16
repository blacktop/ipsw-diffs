## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1924.11.0.0.0
-  __TEXT.__text: 0xef884
-  __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_methlist: 0x9964
-  __TEXT.__const: 0x8b8
-  __TEXT.__gcc_except_tab: 0x2e68
-  __TEXT.__cstring: 0xae29
-  __TEXT.__oslogstring: 0xba7f
-  __TEXT.__dlopen_cstrs: 0x17f0
+1933.8.0.0.0
+  __TEXT.__text: 0x10659c
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0xa1c4
+  __TEXT.__const: 0x8d0
+  __TEXT.__gcc_except_tab: 0x2f84
+  __TEXT.__cstring: 0xc069
+  __TEXT.__oslogstring: 0xc8d1
+  __TEXT.__dlopen_cstrs: 0x189d
   __TEXT.__ustring: 0x33e
-  __TEXT.__unwind_info: 0x2ac0
+  __TEXT.__unwind_info: 0x31a0
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x1146
-  __TEXT.__objc_methname: 0x21633
-  __TEXT.__objc_methtype: 0x26d8
-  __TEXT.__objc_stubs: 0x12ca0
-  __DATA_CONST.__got: 0x8e0
-  __DATA_CONST.__const: 0x3718
-  __DATA_CONST.__objc_classlist: 0x4c0
+  __TEXT.__objc_classname: 0x12b5
+  __TEXT.__objc_methname: 0x22d0f
+  __TEXT.__objc_methtype: 0x27c9
+  __TEXT.__objc_stubs: 0x13a60
+  __DATA_CONST.__got: 0x970
+  __DATA_CONST.__const: 0x38f8
+  __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x50
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x63c0
-  __DATA_CONST.__objc_superrefs: 0x388
-  __DATA_CONST.__objc_arraydata: 0xcb8
-  __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x19c0
-  __AUTH_CONST.__cfstring: 0xbb00
-  __AUTH_CONST.__objc_const: 0x12dc0
-  __AUTH_CONST.__objc_intobj: 0x1128
+  __DATA_CONST.__objc_selrefs: 0x6848
+  __DATA_CONST.__objc_superrefs: 0x3d8
+  __DATA_CONST.__objc_arraydata: 0xd88
+  __AUTH_CONST.__auth_got: 0x7c0
+  __AUTH_CONST.__const: 0x1a80
+  __AUTH_CONST.__cfstring: 0xe5c0
+  __AUTH_CONST.__objc_const: 0x14488
+  __AUTH_CONST.__objc_intobj: 0x1140
   __AUTH_CONST.__objc_arrayobj: 0x828
-  __AUTH_CONST.__objc_doubleobj: 0xb0
+  __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_dictobj: 0xf0
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0xd5c
-  __DATA.__data: 0x3c8
-  __DATA.__bss: 0x600
+  __AUTH.__objc_data: 0xc80
+  __DATA.__objc_ivar: 0xdf0
+  __DATA.__data: 0x4f0
+  __DATA.__bss: 0x678
   __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__bss: 0x8b0
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/NaturalLanguage.framework/NaturalLanguage
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8082968-3D30-3394-B578-16F1854EB8C4
-  Functions: 4561
-  Symbols:   15949
-  CStrings:  9189
+  UUID: 40EEAFC5-C7A2-3E56-B3F6-9D3B177D092F
+  Functions: 4812
+  Symbols:   16973
+  CStrings:  10184
 
Symbols:
+ +[PSInteractionAnalyzer categorizeTime:]
+ +[PSInteractionAnalyzer convertTimeToChunks:]
+ +[_PSContactCatalog kPSContactSummaryHandleKey]
+ +[_PSContactCatalog kPSContactSummaryLastInteractionTimeKey]
+ +[_PSContactCatalog kPSContactSummaryNameKey]
+ +[_PSContactCatalog kPSContactSummarySharingContentPatternKey]
+ +[_PSContactCatalog kPSContactSummarySharingContentTagsKey]
+ +[_PSContactCatalog kPSContactSummarySharingTimePatternKey]
+ +[_PSContactCatalogBackgroundTask interactionStore]
+ +[_PSContactCatalogBackgroundTask savedLastRunDate]
+ +[_PSContactCatalogBackgroundTask savedLastRunDate].cold.1
+ +[_PSContactCatalogTaskMetrics sendAnalyticsEvent:]
+ +[_PSInteractionsStatistics featuresKey]
+ +[_PSInteractionsStatistics numberOfEngagedSuggestionsFromSourceAppWithConversation]
+ +[_PSInteractionsStatistics numberOfSharesFromSourceAppWithConversation]
+ +[_PSInteractionsStatistics personIdsInPastShareInteractionsKey]
+ +[_PSInteractionsStatistics personIdsInPastSyntheticShareInteractionsKey]
+ +[_PSInteractionsStatistics propertiesKey]
+ +[_PSLogging contactCatalogChannel]
+ +[_PSLogging contactCatalogChannel].cold.1
+ +[_PSLogging contentAwareShareSheetChannel]
+ +[_PSLogging contentAwareShareSheetChannel].cold.1
+ +[_PSMegadomeFamilyUtility taggingOptions]
+ +[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]
+ +[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:].cold.1
+ +[_PSPhotoUtils photoLibraryAssertion]
+ +[_PSSceneTagsUtils humanReadableLabelForIdentifier:]
+ +[_PSSceneTagsUtils humanReadableSynonymsForIdentifier:]
+ +[_PSSceneTagsUtils identifierToLabelLookup]
+ +[_PSSceneTagsUtils identifierToSynonymsLookup]
+ +[_PSSceneTagsUtils loadJSONResourceAsDict:]
+ +[_PSSceneTagsUtils loadJSONResourceAsDict:].cold.1
+ +[_PSSceneTagsUtils loadJSONResourceAsDict:].cold.2
+ +[_PSSceneTagsUtils loadJSONResourceAsDict:].cold.3
+ +[_PSSceneTagsUtils loadSceneTags]
+ +[_PSSceneTagsUtils loadSceneTags].cold.1
+ +[_PSSceneTagsUtils loadSceneTags].cold.2
+ +[_PSSceneTagsUtils loadSceneTags].cold.3
+ +[_PSSceneTagsUtils loadTagsToClusterNamesDict]
+ +[_PSSceneTagsUtils sceneClusterDict]
+ +[_PSSceneTagsUtils sceneTagsToClusterNames:]
+ -[PSInteractionAnalyzer .cxx_destruct]
+ -[PSInteractionAnalyzer analyzeInteractionPatterns:]
+ -[PSInteractionAnalyzer conversationIDForInteraction:]
+ -[PSInteractionAnalyzer extractContactInfoFromInteraction:]
+ -[PSInteractionAnalyzer generateContactSummariesWithMaxInteractions:]
+ -[PSInteractionAnalyzer generateContactSummariesWithMaxInteractions:].cold.1
+ -[PSInteractionAnalyzer generateSummaryForContactWithConversationId:interactions:]
+ -[PSInteractionAnalyzer initWithStore:]
+ -[PSInteractionAnalyzer setStore:]
+ -[PSInteractionAnalyzer store]
+ -[PSInteractionPattern .cxx_destruct]
+ -[PSInteractionPattern contentPatterns]
+ -[PSInteractionPattern contentTags]
+ -[PSInteractionPattern frequency]
+ -[PSInteractionPattern initWithTimePatterns:contentPatterns:contentTags:frequency:]
+ -[PSInteractionPattern setContentPatterns:]
+ -[PSInteractionPattern setContentTags:]
+ -[PSInteractionPattern setFrequency:]
+ -[PSInteractionPattern setTimePatterns:]
+ -[PSInteractionPattern timePatterns]
+ -[PSSceneTag .cxx_destruct]
+ -[PSSceneTag childrenClasses]
+ -[PSSceneTag detectorClasses]
+ -[PSSceneTag humanReadableLabel]
+ -[PSSceneTag humanReadableSynonyms]
+ -[PSSceneTag identifier]
+ -[PSSceneTag initWithDictionary:]
+ -[PSSceneTag isSearchable]
+ -[PSSceneTag label]
+ -[PSSceneTag network]
+ -[PSSceneTag parentClasses]
+ -[PSSceneTag searchThreshold]
+ -[PSSceneTag setChildrenClasses:]
+ -[PSSceneTag setDetectorClasses:]
+ -[PSSceneTag setHumanReadableLabel:]
+ -[PSSceneTag setHumanReadableSynonyms:]
+ -[PSSceneTag setIdentifier:]
+ -[PSSceneTag setIsSearchable:]
+ -[PSSceneTag setLabel:]
+ -[PSSceneTag setNetwork:]
+ -[PSSceneTag setParentClasses:]
+ -[PSSceneTag setSearchThreshold:]
+ -[_PSBoWEmbedding .cxx_destruct]
+ -[_PSBoWEmbedding averageEmbeddings:]
+ -[_PSBoWEmbedding computeEmbeddingForText:]
+ -[_PSBoWEmbedding computeEmbeddingForWords:]
+ -[_PSBoWEmbedding computeEmbeddingsForTexts:]
+ -[_PSBoWEmbedding computeEmbeddingsForWordArrays:]
+ -[_PSBoWEmbedding cosineSimilarityBetweenEmbedding:andEmbedding:]
+ -[_PSBoWEmbedding cosineSimilarityBetweenEmbedding:andEmbedding:].cold.1
+ -[_PSBoWEmbedding embeddingDimension]
+ -[_PSBoWEmbedding embedding]
+ -[_PSBoWEmbedding findMostSimilarToQuery:fromCandidates:similarity:]
+ -[_PSBoWEmbedding initWithEmbedding:]
+ -[_PSBoWEmbedding initWithLanguage:]
+ -[_PSBoWEmbedding init]
+ -[_PSBoWEmbedding setEmbedding:]
+ -[_PSBoWEmbedding tokenizeText:]
+ -[_PSContactCatalog convertSetsToArraysInObject:]
+ -[_PSContactCatalog generateContactCatalog:maxInteractions:updateCatalog:]
+ -[_PSContactCatalog generateContactCatalog:maxInteractions:updateCatalog:].cold.1
+ -[_PSContactCatalog saveJSONToFile:]
+ -[_PSContactCatalog saveJSONToFile:].cold.1
+ -[_PSContactCatalogBackgroundTask .cxx_destruct]
+ -[_PSContactCatalogBackgroundTask handleRepeatingTask:]
+ -[_PSContactCatalogBackgroundTask handleRepeatingTask:].cold.1
+ -[_PSContactCatalogBackgroundTask handleRepeatingTask:].cold.2
+ -[_PSContactCatalogBackgroundTask init]
+ -[_PSContactCatalogBackgroundTask saveLastRunDate]
+ -[_PSContactCatalogBackgroundTask saveLastRunDate].cold.1
+ -[_PSContactCatalogBackgroundTask updatePlistWithDict:]
+ -[_PSContactCatalogBackgroundTask updatePlistWithDict:].cold.1
+ -[_PSContactCatalogTaskMetrics analyticsPayload]
+ -[_PSContactCatalogTaskMetrics init]
+ -[_PSContactCatalogTaskMetrics processingTime]
+ -[_PSContactCatalogTaskMetrics setProcessingTime:]
+ -[_PSContactCatalogTaskMetrics setStatus:]
+ -[_PSContactCatalogTaskMetrics setTimeSinceLastRun:]
+ -[_PSContactCatalogTaskMetrics status]
+ -[_PSContactCatalogTaskMetrics timeSinceLastRun]
+ -[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:].cold.5
+ -[_PSEnsembleModel addSharePlaySuggestionsToProxies:interactionStatistics:predictionContext:]
+ -[_PSEnsembleModel computeOrLoadFeaturesForInteractionStatistics:trialClient:]
+ -[_PSEnsembleModel getMeContactIdentifierAsync]
+ -[_PSFamilyRecommender familyRecipientsFromMegadomeWithPredictionContext:]
+ -[_PSFamilyRecommender familyRecipientsFromMegadomeWithPredictionContext:].cold.1
+ -[_PSFamilyRecommender familyRecommendationSuggestionsFromMegadomeWithPredictionContext:]
+ -[_PSFamilyRecommender familyRecommendationSuggestionsFromMegadomeWithPredictionContext:].cold.1
+ -[_PSFamilyRecommender megadomeUtility]
+ -[_PSFamilyRecommender setMegadomeUtility:]
+ -[_PSHeuristics embeddingBasedURLSuggestionProxiesForInteractionStatistics:withPredictionContext:]
+ -[_PSHeuristics hyperRecentInteractionSuggestionProxiesForInteractionStatistics:maxCandidates:]
+ -[_PSHeuristics sceneBasedSuggestionsUsingEmbedding:withPredictionContext:]
+ -[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:]
+ -[_PSInteractionsStatistics allInteractionsStats]
+ -[_PSInteractionsStatistics computeRecencyFeaturesWithInteractionStore:]
+ -[_PSInteractionsStatistics computeRecencyFeaturesWithInteractionStore:].cold.1
+ -[_PSInteractionsStatistics deriveAppSpecificFeaturesFromCatalog]
+ -[_PSInteractionsStatistics deriveAppSpecificFeaturesFromCatalog].cold.1
+ -[_PSInteractionsStatistics incrementNumberOfEngagedSuggestionsFromSourceAppWithConversation:forConversationId:]
+ -[_PSInteractionsStatistics incrementNumberOfSharesFromSourceAppWithConversation:forConversationId:]
+ -[_PSInteractionsStatistics loadFeaturesAndPropertiesFromContactCatalog]
+ -[_PSInteractionsStatistics loadFeaturesAndPropertiesFromContactCatalog].cold.1
+ -[_PSInteractionsStatistics loadFeaturesAndPropertiesFromContactCatalog].cold.2
+ -[_PSInteractionsStatistics numberOfEngagedSuggestionsFromSourceAppWithConversation]
+ -[_PSInteractionsStatistics numberOfSharesFromSourceAppWithConversation]
+ -[_PSInteractionsStatistics setNumberOfEngagedSuggestionsFromSourceAppWithConversation:]
+ -[_PSInteractionsStatistics setNumberOfSharesFromSourceAppWithConversation:]
+ -[_PSInteractionsStatistics setSharingContentPatternByConversationId:]
+ -[_PSInteractionsStatistics setSharingTimePatternByConversationId:]
+ -[_PSInteractionsStatistics sharingContentPatternByConversationId]
+ -[_PSInteractionsStatistics sharingTimePatternByConversationId]
+ -[_PSMegadomeFamilyUtility .cxx_destruct]
+ -[_PSMegadomeFamilyUtility contactResolver]
+ -[_PSMegadomeFamilyUtility contactStore]
+ -[_PSMegadomeFamilyUtility familyRecipientsFromMegadomeWithError:]
+ -[_PSMegadomeFamilyUtility familyRecipientsFromMegadomeWithError:].cold.1
+ -[_PSMegadomeFamilyUtility familyRecipientsFromMegadomeWithError:].cold.2
+ -[_PSMegadomeFamilyUtility init]
+ -[_PSMegadomeFamilyUtility megadomeResultsForFamilyTagWithError:]
+ -[_PSMegadomeFamilyUtility megadomeResultsForFamilyTagWithError:].cold.1
+ -[_PSMegadomeFamilyUtility megadomeResultsForFamilyTagWithError:].cold.2
+ -[_PSMegadomeFamilyUtility peopleViewWithError:]
+ -[_PSMegadomeFamilyUtility peopleViewWithError:].cold.1
+ -[_PSMegadomeFamilyUtility recipientFromMegadomePerson:]
+ -[_PSMegadomeFamilyUtility recipientFromMegadomePerson:].cold.1
+ -[_PSMegadomeFamilyUtility recipientFromMegadomePerson:].cold.2
+ -[_PSMegadomeFamilyUtility recipientsFromScoredEntities:inVisualIdentifierView:]
+ -[_PSMegadomeFamilyUtility setContactResolver:]
+ -[_PSMegadomeFamilyUtility setContactStore:]
+ -[_PSPhotoLibraryAssertion .cxx_destruct]
+ -[_PSPhotoLibraryAssertion _init]
+ -[_PSPhotoLibraryAssertion dealloc]
+ -[_PSPhotoLibraryAssertion library]
+ -[_PSPhotoSuggestionsCancellationToken .cxx_destruct]
+ -[_PSRankAggregationContext .cxx_destruct]
+ -[_PSRankAggregationContext initWithPriorityOrder:]
+ -[_PSRankAggregationContext priorityOrder]
+ -[_PSRankAggregationPriorityBased aggregateRankings:withContext:]
+ -[_PSRankAggregationRRF .cxx_destruct]
+ -[_PSRankAggregationRRF aggregateRankings:withContext:]
+ -[_PSRankAggregationRRF heuristicsToFuse]
+ -[_PSRankAggregationRRF initWithK:heuristicsToFuse:]
+ -[_PSRankAggregationRRF k]
+ -[_PSRankAggregationRRF setHeuristicsToFuse:]
+ -[_PSRankAggregationRRF setK:]
+ -[_PSSuggestionProxy recencyTimestamp]
+ -[_PSSuggestionProxy setRecencyTimestamp:]
+ -[_PSTrialClient rankAggregationStrategyType]
+ -[_PSTrialClient rrfConstantK]
+ -[_PSTrialClient shouldUseCatalogInference]
+ GCC_except_table102
+ GCC_except_table103
+ GCC_except_table104
+ GCC_except_table138
+ GCC_except_table139
+ GCC_except_table140
+ GCC_except_table162
+ GCC_except_table167
+ GCC_except_table172
+ GCC_except_table33
+ GCC_except_table43
+ GCC_except_table56
+ GCC_except_table85
+ OBJC_IVAR_$__PSPhotoSuggestionsCancellationToken._personCancellationArray
+ OBJC_IVAR_$__PSPhotoSuggestionsCancellationToken._sceneCancellationBlock
+ _OBJC_CLASS_$_NLEmbedding
+ _OBJC_CLASS_$_NLTokenizer
+ _OBJC_CLASS_$_NSNumberFormatter
+ _OBJC_CLASS_$_PSInteractionAnalyzer
+ _OBJC_CLASS_$_PSInteractionPattern
+ _OBJC_CLASS_$_PSSceneTag
+ _OBJC_CLASS_$__PASCachedResult
+ _OBJC_CLASS_$__PSBoWEmbedding
+ _OBJC_CLASS_$__PSContactCatalog
+ _OBJC_CLASS_$__PSContactCatalogBackgroundTask
+ _OBJC_CLASS_$__PSContactCatalogTaskMetrics
+ _OBJC_CLASS_$__PSMegadomeFamilyUtility
+ _OBJC_CLASS_$__PSPhotoLibraryAssertion
+ _OBJC_CLASS_$__PSPhotoSuggestionsCancellationToken
+ _OBJC_CLASS_$__PSRankAggregationContext
+ _OBJC_CLASS_$__PSRankAggregationPriorityBased
+ _OBJC_CLASS_$__PSRankAggregationRRF
+ _OBJC_CLASS_$__PSSceneTagsUtils
+ _OBJC_IVAR_$_PSInteractionAnalyzer._store
+ _OBJC_IVAR_$_PSInteractionPattern._contentPatterns
+ _OBJC_IVAR_$_PSInteractionPattern._contentTags
+ _OBJC_IVAR_$_PSInteractionPattern._frequency
+ _OBJC_IVAR_$_PSInteractionPattern._timePatterns
+ _OBJC_IVAR_$_PSSceneTag._childrenClasses
+ _OBJC_IVAR_$_PSSceneTag._detectorClasses
+ _OBJC_IVAR_$_PSSceneTag._humanReadableLabel
+ _OBJC_IVAR_$_PSSceneTag._humanReadableSynonyms
+ _OBJC_IVAR_$_PSSceneTag._identifier
+ _OBJC_IVAR_$_PSSceneTag._isSearchable
+ _OBJC_IVAR_$_PSSceneTag._label
+ _OBJC_IVAR_$_PSSceneTag._network
+ _OBJC_IVAR_$_PSSceneTag._parentClasses
+ _OBJC_IVAR_$_PSSceneTag._searchThreshold
+ _OBJC_IVAR_$__PSBoWEmbedding._embedding
+ _OBJC_IVAR_$__PSBoWEmbedding._embeddingDimension
+ _OBJC_IVAR_$__PSContactCatalogBackgroundTask._interactionStore
+ _OBJC_IVAR_$__PSContactCatalogBackgroundTask._lastRunDate
+ _OBJC_IVAR_$__PSContactCatalogBackgroundTask._metrics
+ _OBJC_IVAR_$__PSContactCatalogTaskMetrics._processingTime
+ _OBJC_IVAR_$__PSContactCatalogTaskMetrics._status
+ _OBJC_IVAR_$__PSContactCatalogTaskMetrics._timeSinceLastRun
+ _OBJC_IVAR_$__PSFamilyRecommender._megadomeUtility
+ _OBJC_IVAR_$__PSInteractionsStatistics._numberOfEngagedSuggestionsFromSourceAppWithConversation
+ _OBJC_IVAR_$__PSInteractionsStatistics._numberOfSharesFromSourceAppWithConversation
+ _OBJC_IVAR_$__PSInteractionsStatistics._sharingContentPatternByConversationId
+ _OBJC_IVAR_$__PSInteractionsStatistics._sharingTimePatternByConversationId
+ _OBJC_IVAR_$__PSMegadomeFamilyUtility._contactResolver
+ _OBJC_IVAR_$__PSMegadomeFamilyUtility._contactStore
+ _OBJC_IVAR_$__PSPhotoLibraryAssertion._lazyLibrary
+ _OBJC_IVAR_$__PSRankAggregationContext._priorityOrder
+ _OBJC_IVAR_$__PSRankAggregationRRF._heuristicsToFuse
+ _OBJC_IVAR_$__PSRankAggregationRRF._k
+ _OBJC_IVAR_$__PSSuggestionProxy._recencyTimestamp
+ _OBJC_METACLASS_$_PSInteractionAnalyzer
+ _OBJC_METACLASS_$_PSInteractionPattern
+ _OBJC_METACLASS_$_PSSceneTag
+ _OBJC_METACLASS_$__PSBoWEmbedding
+ _OBJC_METACLASS_$__PSContactCatalog
+ _OBJC_METACLASS_$__PSContactCatalogBackgroundTask
+ _OBJC_METACLASS_$__PSContactCatalogTaskMetrics
+ _OBJC_METACLASS_$__PSMegadomeFamilyUtility
+ _OBJC_METACLASS_$__PSPhotoLibraryAssertion
+ _OBJC_METACLASS_$__PSPhotoSuggestionsCancellationToken
+ _OBJC_METACLASS_$__PSRankAggregationContext
+ _OBJC_METACLASS_$__PSRankAggregationPriorityBased
+ _OBJC_METACLASS_$__PSRankAggregationRRF
+ _OBJC_METACLASS_$__PSSceneTagsUtils
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_9
+ _SuggestionProxyTypeHyperRecentInteraction
+ _SuggestionProxyTypeURLASS
+ __OBJC_$_CLASS_METHODS_PSInteractionAnalyzer
+ __OBJC_$_CLASS_METHODS__PSContactCatalog
+ __OBJC_$_CLASS_METHODS__PSContactCatalogBackgroundTask
+ __OBJC_$_CLASS_METHODS__PSContactCatalogTaskMetrics
+ __OBJC_$_CLASS_METHODS__PSInteractionsStatistics
+ __OBJC_$_CLASS_METHODS__PSMegadomeFamilyUtility
+ __OBJC_$_CLASS_METHODS__PSSceneTagsUtils
+ __OBJC_$_CLASS_PROP_LIST__PSContactCatalog
+ __OBJC_$_CLASS_PROP_LIST__PSInteractionsStatistics
+ __OBJC_$_INSTANCE_METHODS_PSInteractionAnalyzer
+ __OBJC_$_INSTANCE_METHODS_PSInteractionPattern
+ __OBJC_$_INSTANCE_METHODS_PSSceneTag
+ __OBJC_$_INSTANCE_METHODS__PSBoWEmbedding
+ __OBJC_$_INSTANCE_METHODS__PSContactCatalog
+ __OBJC_$_INSTANCE_METHODS__PSContactCatalogBackgroundTask
+ __OBJC_$_INSTANCE_METHODS__PSContactCatalogTaskMetrics
+ __OBJC_$_INSTANCE_METHODS__PSMegadomeFamilyUtility
+ __OBJC_$_INSTANCE_METHODS__PSPhotoLibraryAssertion
+ __OBJC_$_INSTANCE_METHODS__PSPhotoSuggestionsCancellationToken
+ __OBJC_$_INSTANCE_METHODS__PSRankAggregationContext
+ __OBJC_$_INSTANCE_METHODS__PSRankAggregationPriorityBased
+ __OBJC_$_INSTANCE_METHODS__PSRankAggregationRRF
+ __OBJC_$_INSTANCE_VARIABLES_PSInteractionAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_PSInteractionPattern
+ __OBJC_$_INSTANCE_VARIABLES_PSSceneTag
+ __OBJC_$_INSTANCE_VARIABLES__PSBoWEmbedding
+ __OBJC_$_INSTANCE_VARIABLES__PSContactCatalogBackgroundTask
+ __OBJC_$_INSTANCE_VARIABLES__PSContactCatalogTaskMetrics
+ __OBJC_$_INSTANCE_VARIABLES__PSMegadomeFamilyUtility
+ __OBJC_$_INSTANCE_VARIABLES__PSPhotoLibraryAssertion
+ __OBJC_$_INSTANCE_VARIABLES__PSPhotoSuggestionsCancellationToken
+ __OBJC_$_INSTANCE_VARIABLES__PSRankAggregationContext
+ __OBJC_$_INSTANCE_VARIABLES__PSRankAggregationRRF
+ __OBJC_$_PROP_LIST_PSInteractionAnalyzer
+ __OBJC_$_PROP_LIST_PSInteractionPattern
+ __OBJC_$_PROP_LIST_PSSceneTag
+ __OBJC_$_PROP_LIST__PSBoWEmbedding
+ __OBJC_$_PROP_LIST__PSContactCatalogTaskMetrics
+ __OBJC_$_PROP_LIST__PSMegadomeFamilyUtility
+ __OBJC_$_PROP_LIST__PSPhotoLibraryAssertion
+ __OBJC_$_PROP_LIST__PSRankAggregationContext
+ __OBJC_$_PROP_LIST__PSRankAggregationPriorityBased
+ __OBJC_$_PROP_LIST__PSRankAggregationRRF
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__PSRankAggregationStrategy
+ __OBJC_$_PROTOCOL_METHOD_TYPES__PSRankAggregationStrategy
+ __OBJC_$_PROTOCOL_REFS__PSRankAggregationStrategy
+ __OBJC_CLASS_PROTOCOLS_$__PSRankAggregationPriorityBased
+ __OBJC_CLASS_PROTOCOLS_$__PSRankAggregationRRF
+ __OBJC_CLASS_RO_$_PSInteractionAnalyzer
+ __OBJC_CLASS_RO_$_PSInteractionPattern
+ __OBJC_CLASS_RO_$_PSSceneTag
+ __OBJC_CLASS_RO_$__PSBoWEmbedding
+ __OBJC_CLASS_RO_$__PSContactCatalog
+ __OBJC_CLASS_RO_$__PSContactCatalogBackgroundTask
+ __OBJC_CLASS_RO_$__PSContactCatalogTaskMetrics
+ __OBJC_CLASS_RO_$__PSMegadomeFamilyUtility
+ __OBJC_CLASS_RO_$__PSPhotoLibraryAssertion
+ __OBJC_CLASS_RO_$__PSPhotoSuggestionsCancellationToken
+ __OBJC_CLASS_RO_$__PSRankAggregationContext
+ __OBJC_CLASS_RO_$__PSRankAggregationPriorityBased
+ __OBJC_CLASS_RO_$__PSRankAggregationRRF
+ __OBJC_CLASS_RO_$__PSSceneTagsUtils
+ __OBJC_LABEL_PROTOCOL_$__PSRankAggregationStrategy
+ __OBJC_METACLASS_RO_$_PSInteractionAnalyzer
+ __OBJC_METACLASS_RO_$_PSInteractionPattern
+ __OBJC_METACLASS_RO_$_PSSceneTag
+ __OBJC_METACLASS_RO_$__PSBoWEmbedding
+ __OBJC_METACLASS_RO_$__PSContactCatalog
+ __OBJC_METACLASS_RO_$__PSContactCatalogBackgroundTask
+ __OBJC_METACLASS_RO_$__PSContactCatalogTaskMetrics
+ __OBJC_METACLASS_RO_$__PSMegadomeFamilyUtility
+ __OBJC_METACLASS_RO_$__PSPhotoLibraryAssertion
+ __OBJC_METACLASS_RO_$__PSPhotoSuggestionsCancellationToken
+ __OBJC_METACLASS_RO_$__PSRankAggregationContext
+ __OBJC_METACLASS_RO_$__PSRankAggregationPriorityBased
+ __OBJC_METACLASS_RO_$__PSRankAggregationRRF
+ __OBJC_METACLASS_RO_$__PSSceneTagsUtils
+ __OBJC_PROTOCOL_$__PSRankAggregationStrategy
+ __PSPhotoLibraryAssertionInitLock
+ __PSPhotoLibraryAssertionLock
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.426
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.428
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.899
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.900
+ ___118-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:]_block_invoke.984
+ ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.792
+ ___120-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:]_block_invoke
+ ___120-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:]_block_invoke.234
+ ___120-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:]_block_invoke_2
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.710
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.710.cold.1
+ ___132-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:]_block_invoke.190
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke.350
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke.356
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke_2
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke_2.351
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke_3
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke_3.cold.1
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.264
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.264.cold.1
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.280
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.306
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.308
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.310
+ ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.312
+ ___32-[_PSBoWEmbedding tokenizeText:]_block_invoke
+ ___35+[_PSLogging contactCatalogChannel]_block_invoke
+ ___35+[_PSLogging contactCatalogChannel]_block_invoke.cold.1
+ ___35-[_PSPhotoLibraryAssertion library]_block_invoke
+ ___43+[_PSLogging contentAwareShareSheetChannel]_block_invoke
+ ___43+[_PSLogging contentAwareShareSheetChannel]_block_invoke.cold.1
+ ___47-[_PSEnsembleModel getMeContactIdentifierAsync]_block_invoke
+ ___47-[_PSEnsembleModel getMeContactIdentifierAsync]_block_invoke_2
+ ___47-[_PSEnsembleModel getMeContactIdentifierAsync]_block_invoke_3
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.888
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.888.cold.1
+ ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke.103
+ ___55-[_PSContactCatalogBackgroundTask handleRepeatingTask:]_block_invoke
+ ___55-[_PSRankAggregationRRF aggregateRankings:withContext:]_block_invoke
+ ___67-[_PSInteractionsStatistics computeStatisticsWithInteractionStore:]_block_invoke.100
+ ___67-[_PSInteractionsStatistics computeStatisticsWithInteractionStore:]_block_invoke_2.104
+ ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.763
+ ___72-[_PSInteractionsStatistics computeRecencyFeaturesWithInteractionStore:]_block_invoke
+ ___72-[_PSInteractionsStatistics computeRecencyFeaturesWithInteractionStore:]_block_invoke.138
+ ___72-[_PSInteractionsStatistics computeRecencyFeaturesWithInteractionStore:]_block_invoke.139
+ ___72-[_PSInteractionsStatistics computeRecencyFeaturesWithInteractionStore:]_block_invoke_2
+ ___72-[_PSInteractionsStatistics computeRecencyFeaturesWithInteractionStore:]_block_invoke_2.140
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.386
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.392
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.395
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.416
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.423
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.420
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.625
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.154
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.159
+ ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_2.163
+ ___91-[_PSEnsembleModel _conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:]_block_invoke.957
+ ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke.162
+ ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke_2.1409
+ ___93-[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]_block_invoke.471
+ ___95-[_PSHeuristics hyperRecentInteractionSuggestionProxiesForInteractionStatistics:maxCandidates:]_block_invoke
+ ___Block_byref_object_copy_.357
+ ___Block_byref_object_dispose_.358
+ ___block_descriptor_32_e33_"NSString"16?0"_PSAttachment"8l
+ ___block_descriptor_32_e35_B24?0"NSString"8"NSDictionary"16l
+ ___block_descriptor_32_e51_q24?0"_PSSuggestionProxy"8"_PSSuggestionProxy"16l
+ ___block_descriptor_32_e5_8?0l
+ ___block_descriptor_32_e8_v16?0d8l
+ ___block_descriptor_44_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40r_e15_"NSString"8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e27_v40?0{_NSRange=QQ}8Q24^B32ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e20_v20?0"NSArray"8B16ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e8_v12?0B8lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.1411
+ ___block_literal_global.150
+ ___block_literal_global.153
+ ___block_literal_global.158
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.189
+ ___block_literal_global.217
+ ___block_literal_global.221
+ ___block_literal_global.249
+ ___block_literal_global.277
+ ___block_literal_global.293
+ ___block_literal_global.296
+ ___block_literal_global.321
+ ___block_literal_global.354
+ ___block_literal_global.389
+ ___block_literal_global.394
+ ___block_literal_global.397
+ ___block_literal_global.413
+ ___block_literal_global.419
+ ___block_literal_global.422
+ ___block_literal_global.425
+ ___block_literal_global.444
+ ___block_literal_global.447
+ ___block_literal_global.46
+ ___block_literal_global.467
+ ___block_literal_global.473
+ ___block_literal_global.563
+ ___block_literal_global.608
+ ___block_literal_global.639
+ ___block_literal_global.701
+ ___block_literal_global.802
+ ___block_literal_global.805
+ ___block_literal_global.808
+ ___block_literal_global.811
+ ___block_literal_global.881
+ ___block_literal_global.986
+ ___getGDConfigurationClass_block_invoke
+ ___getGDConfigurationClass_block_invoke.cold.1
+ ___getGDEntityTaggingServiceClass_block_invoke
+ ___getGDEntityTaggingServiceClass_block_invoke.cold.1
+ ___getGDPersonTaggingOptionsClass_block_invoke
+ ___getGDPersonTaggingOptionsClass_block_invoke.cold.1
+ ___getVCPMediaAnalysisServiceClass_block_invoke
+ __identifierToLabelLookup
+ __identifierToSynonymsLookup
+ __sceneClusterDict
+ __suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken162
+ _contactCatalogChannel.contactCatalogChannel
+ _contactCatalogChannel.onceToken
+ _contentAwareShareSheetChannel.contentAwareShareSheetChannel
+ _contentAwareShareSheetChannel.onceToken
+ _getGDConfigurationClass.softClass
+ _getGDEntityTaggingServiceClass.softClass
+ _getGDPersonTaggingOptionsClass.softClass
+ _getVCPMediaAnalysisServiceClass
+ _getVCPMediaAnalysisServiceClass.softClass
+ _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.1408
+ _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.148
+ _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.161
+ _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken48
+ _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken49
+ _objc_msgSend$_init
+ _objc_msgSend$addSharePlaySuggestionsToProxies:interactionStatistics:predictionContext:
+ _objc_msgSend$aggregateRankings:withContext:
+ _objc_msgSend$allInteractionsStats
+ _objc_msgSend$analyzeInteractionPatterns:
+ _objc_msgSend$averageEmbeddings:
+ _objc_msgSend$cancelRequest:
+ _objc_msgSend$categorizeTime:
+ _objc_msgSend$computeEmbeddingForText:
+ _objc_msgSend$computeEmbeddingForWords:
+ _objc_msgSend$computeOrLoadFeaturesForInteractionStatistics:trialClient:
+ _objc_msgSend$computeRecencyFeaturesWithInteractionStore:
+ _objc_msgSend$contactCatalogChannel
+ _objc_msgSend$contentAwareShareSheetChannel
+ _objc_msgSend$contentPatterns
+ _objc_msgSend$contentTags
+ _objc_msgSend$conversationIDForInteraction:
+ _objc_msgSend$convertSetsToArraysInObject:
+ _objc_msgSend$convertTimeToChunks:
+ _objc_msgSend$cosineSimilarityBetweenEmbedding:andEmbedding:
+ _objc_msgSend$dataWithJSONObject:options:error:
+ _objc_msgSend$deriveAppSpecificFeaturesFromCatalog
+ _objc_msgSend$dimension
+ _objc_msgSend$embedding
+ _objc_msgSend$embeddingBasedURLSuggestionProxiesForInteractionStatistics:withPredictionContext:
+ _objc_msgSend$entitiesForTag:options:error:
+ _objc_msgSend$enumerateTokensInRange:usingBlock:
+ _objc_msgSend$extractContactInfoFromInteraction:
+ _objc_msgSend$familyRecipientsFromMegadomeWithError:
+ _objc_msgSend$familyRecipientsFromMegadomeWithPredictionContext:
+ _objc_msgSend$familyRecommendationSuggestionsFromMegadomeWithPredictionContext:
+ _objc_msgSend$featuresKey
+ _objc_msgSend$fetchOptionsWithInclusiveDefaultsForPhotoLibrary:
+ _objc_msgSend$generateContactCatalog:maxInteractions:updateCatalog:
+ _objc_msgSend$generateContactSummariesWithMaxInteractions:
+ _objc_msgSend$generateSummaryForContactWithConversationId:interactions:
+ _objc_msgSend$getMeContactIdentifierAsync
+ _objc_msgSend$heuristicsToFuse
+ _objc_msgSend$humanReadableLabel
+ _objc_msgSend$humanReadableLabelForIdentifier:
+ _objc_msgSend$humanReadableSynonyms
+ _objc_msgSend$hyperRecentInteractionSuggestionProxiesForInteractionStatistics:maxCandidates:
+ _objc_msgSend$idValue
+ _objc_msgSend$identifierToLabelLookup
+ _objc_msgSend$identifierToSynonymsLookup
+ _objc_msgSend$incrementNumberOfEngagedSuggestionsFromSourceAppWithConversation:forConversationId:
+ _objc_msgSend$incrementNumberOfSharesFromSourceAppWithConversation:forConversationId:
+ _objc_msgSend$initWithConfig:error:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithEmbedding:
+ _objc_msgSend$initWithK:heuristicsToFuse:
+ _objc_msgSend$initWithLanguage:
+ _objc_msgSend$initWithPhotoLibraryURL:
+ _objc_msgSend$initWithPriorityOrder:
+ _objc_msgSend$initWithStore:
+ _objc_msgSend$initWithTagThresholds:
+ _objc_msgSend$initWithTimePatterns:contentPatterns:contentTags:frequency:
+ _objc_msgSend$initWithUnit:
+ _objc_msgSend$kPSContactSummaryHandleKey
+ _objc_msgSend$kPSContactSummaryLastInteractionTimeKey
+ _objc_msgSend$kPSContactSummaryNameKey
+ _objc_msgSend$kPSContactSummarySharingContentPatternKey
+ _objc_msgSend$kPSContactSummarySharingContentTagsKey
+ _objc_msgSend$kPSContactSummarySharingTimePatternKey
+ _objc_msgSend$languageCode
+ _objc_msgSend$letterCharacterSet
+ _objc_msgSend$library
+ _objc_msgSend$loadFeaturesAndPropertiesFromContactCatalog
+ _objc_msgSend$loadJSONResourceAsDict:
+ _objc_msgSend$loadSceneTags
+ _objc_msgSend$loadTagsToClusterNamesDict
+ _objc_msgSend$megadomeResultsForFamilyTagWithError:
+ _objc_msgSend$megadomeUtility
+ _objc_msgSend$numberFromString:
+ _objc_msgSend$numberOfEngagedSuggestionsFromSourceAppWithConversation
+ _objc_msgSend$numberOfSharesFromSourceAppWithConversation
+ _objc_msgSend$peopleViewWithError:
+ _objc_msgSend$personIdsInPastShareInteractionsKey
+ _objc_msgSend$personIdsInPastSyntheticShareInteractionsKey
+ _objc_msgSend$photoLibraryAssertion
+ _objc_msgSend$priorityOrder
+ _objc_msgSend$propertiesKey
+ _objc_msgSend$rankAggregationStrategyType
+ _objc_msgSend$recencyTimestamp
+ _objc_msgSend$recipientFromMegadomePerson:
+ _objc_msgSend$recipientsFromScoredEntities:inVisualIdentifierView:
+ _objc_msgSend$requestProcessingTypes:forAssetsWithLocalIdentifiers:fromPhotoLibraryWithURL:progressHandler:completionHandler:
+ _objc_msgSend$resultNonnullWithBlock:
+ _objc_msgSend$rrfConstantK
+ _objc_msgSend$saveJSONToFile:
+ _objc_msgSend$saveLastRunDate
+ _objc_msgSend$savedLastRunDate
+ _objc_msgSend$sceneBasedSuggestionsUsingEmbedding:withPredictionContext:
+ _objc_msgSend$sceneClusterDict
+ _objc_msgSend$sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:
+ _objc_msgSend$sceneTagsToClusterNames:
+ _objc_msgSend$scoredEntities
+ _objc_msgSend$setRecencyTimestamp:
+ _objc_msgSend$setString:
+ _objc_msgSend$setTimeSinceLastRun:
+ _objc_msgSend$sharedAnalysisService
+ _objc_msgSend$sharingContentPatternByConversationId
+ _objc_msgSend$shouldUseCatalogInference
+ _objc_msgSend$sortUsingDescriptors:
+ _objc_msgSend$store
+ _objc_msgSend$stringWithContentsOfFile:encoding:error:
+ _objc_msgSend$suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:
+ _objc_msgSend$taggingOptions
+ _objc_msgSend$timePatterns
+ _objc_msgSend$timeSinceLastRun
+ _objc_msgSend$tokenizeText:
+ _objc_msgSend$unsafeShutdownLibraryWithPhotoLibraryURL:
+ _objc_msgSend$vectorForString:
+ _objc_msgSend$wordEmbeddingForLanguage:
+ _objc_msgSend$writeToFile:atomically:encoding:error:
+ _objc_storeWeak
+ _photoLibraryAssertion.assertion
+ _psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:._pasOnceToken272
+ _pthread_rwlock_rdlock
+ _pthread_rwlock_trywrlock
+ _pthread_rwlock_unlock
+ _sharedMADService._pasOnceToken18
- +[_PSFeatureDictionary _fromPlistValue:timeBucket:].cold.7
- +[_PSPhotoSuggestions cancelRequestWithToken:].cold.1
- +[_PSPhotoSuggestions cancelRequestWithToken:].cold.2
- +[_PSPhotoUtils prewarmPhotosFrameworks]
- +[_PSPhotoUtils prewarmPhotosFrameworks].cold.1
- GCC_except_table100
- GCC_except_table134
- GCC_except_table135
- GCC_except_table136
- GCC_except_table14
- GCC_except_table158
- GCC_except_table163
- GCC_except_table168
- GCC_except_table74
- GCC_except_table81
- GCC_except_table98
- GCC_except_table99
- ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.422
- ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.423
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.884
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.885
- ___118-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:]_block_invoke.957
- ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.776
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.694
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.694.cold.1
- ___132-[_PSHeuristics hyperRecentHeuristicSuggestionProxiesForInteractionStatistics:forStatName:withRecencyMargin:maxNumberOfSuggestions:]_block_invoke.177
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.254
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.254.cold.1
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.270
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.296
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.298
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.300
- ___162+[_PSPhotoSuggestions peopleInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:shouldUseVIPModel:withTraceID:withSpanID:shouldUseMDID:withCompletion:]_block_invoke.302
- ___40+[_PSPhotoUtils prewarmPhotosFrameworks]_block_invoke
- ___40+[_PSPhotoUtils prewarmPhotosFrameworks]_block_invoke_2
- ___40+[_PSPhotoUtils prewarmPhotosFrameworks]_block_invoke_3
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.873
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.873.cold.1
- ___51-[_PSBackgroundProcessingTask handleRepeatingTask:]_block_invoke.102
- ___67-[_PSInteractionsStatistics computeStatisticsWithInteractionStore:]_block_invoke.81
- ___67-[_PSInteractionsStatistics computeStatisticsWithInteractionStore:]_block_invoke_2.85
- ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.747
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.374
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.379
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.382
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.397
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.403
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.407
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.609
- ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.147
- ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke.152
- ___90-[_PSHeuristics hyperRecentViewedThreadHeuristicSuggestionProxiesForInteractionStatistics]_block_invoke_2.156
- ___91-[_PSEnsembleModel _conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:]_block_invoke.930
- ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke.84
- ___91-[_PSInteractionsStatisticsConfig(DefaultConfig) initDefaultConfigWithBundleId:anchorDate:]_block_invoke_2.581
- ___93-[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]_block_invoke.461
- ___94-[_PSEnsembleModel finalSuggestionProxiesForInteractionStatistics:config:trialClient:context:]_block_invoke
- ___Block_byref_object_copy_.303
- ___Block_byref_object_dispose_.304
- ___block_descriptor_40_e8_32r_e25_v32?0"NSString"8Q16^B24lr32l8
- ___block_descriptor_56_e8_32s40s48s_e33_"NSMutableArray"16?0"NSArray"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.151
- ___block_literal_global.159
- ___block_literal_global.204
- ___block_literal_global.208
- ___block_literal_global.212
- ___block_literal_global.215
- ___block_literal_global.230
- ___block_literal_global.269
- ___block_literal_global.287
- ___block_literal_global.290
- ___block_literal_global.377
- ___block_literal_global.381
- ___block_literal_global.384
- ___block_literal_global.400
- ___block_literal_global.406
- ___block_literal_global.409
- ___block_literal_global.412
- ___block_literal_global.438
- ___block_literal_global.457
- ___block_literal_global.463
- ___block_literal_global.547
- ___block_literal_global.583
- ___block_literal_global.592
- ___block_literal_global.623
- ___block_literal_global.685
- ___block_literal_global.72
- ___block_literal_global.786
- ___block_literal_global.789
- ___block_literal_global.792
- ___block_literal_global.795
- ___block_literal_global.866
- ___block_literal_global.959
- __suggestionInteractionPredicatesForFirstPartyMessages:bundleID:interactionRecipients:._pasOnceToken161
- _dispatch_group_async
- _getPFSceneTaxonomyClass
- _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.580
- _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.70
- _initDefaultConfigWithBundleId:anchorDate:._pasExprOnceResult.83
- _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken22
- _initDefaultConfigWithBundleId:anchorDate:._pasOnceToken23
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$digest
- _objc_msgSend$fetchOptionsWithInclusiveDefaults
- _objc_msgSend$initWithLatestTaxonomy
- _objc_msgSend$isCloudPhotoLibraryEnabled
- _objc_msgSend$orderedSuggestionProxiesWithProxyOrder:suggestionProxies:suggestionsWithSharePlayAddedBlock:
- _objc_msgSend$sharedPhotoLibrary
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
- _prewarmPhotosFrameworks.prewarmOnce
- _psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:._pasOnceToken269
- _sharedMADService._pasOnceToken15
CStrings:
+ "%@.%@"
+ "%@: %f"
+ "%lld"
+ "%tu"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
+ "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
+ "1010"
+ "10246"
+ "10248"
+ "10249"
+ "10262"
+ "10272"
+ "10356"
+ "10373"
+ "10399"
+ "10557"
+ "1065"
+ "10666"
+ "10773"
+ "1086"
+ "1093"
+ "10949"
+ "11060"
+ "1107"
+ "11129"
+ "1113"
+ "1128"
+ "1139"
+ "11490"
+ "117"
+ "11715"
+ "11771"
+ "11838"
+ "11914"
+ "11915"
+ "12133"
+ "1216"
+ "12162"
+ "12409"
+ "12454"
+ "12516"
+ "12541"
+ "12614"
+ "1262"
+ "12651"
+ "12692"
+ "1285"
+ "13141"
+ "1327"
+ "1328"
+ "1331"
+ "13310"
+ "13354"
+ "134"
+ "13762"
+ "13824"
+ "13955"
+ "13961"
+ "13963"
+ "13974"
+ "13991"
+ "14069"
+ "14081"
+ "14124"
+ "14137"
+ "14188"
+ "14339"
+ "14340"
+ "14341"
+ "14389"
+ "1439"
+ "144"
+ "14419"
+ "1446"
+ "1447"
+ "14539"
+ "147"
+ "14978"
+ "15117"
+ "15126"
+ "1515"
+ "15168"
+ "15169"
+ "15201"
+ "153"
+ "1533"
+ "15359"
+ "15412"
+ "15444"
+ "15459"
+ "15494"
+ "15541"
+ "15640"
+ "15699"
+ "15702"
+ "15853"
+ "15902"
+ "15999"
+ "16131"
+ "16275"
+ "1630"
+ "16301"
+ "1634"
+ "1635"
+ "16370"
+ "16461"
+ "1660"
+ "1662"
+ "16634"
+ "1664"
+ "16693"
+ "16694"
+ "16733"
+ "1676"
+ "1682"
+ "1708"
+ "1717"
+ "17206"
+ "1724"
+ "1736"
+ "17370"
+ "1739"
+ "17471"
+ "17488"
+ "17531"
+ "176"
+ "17639"
+ "17700"
+ "17784"
+ "17847"
+ "17867"
+ "18"
+ "18154"
+ "182"
+ "18381"
+ "18402"
+ "18512"
+ "213"
+ "2147483653"
+ "2147483655"
+ "23"
+ "24"
+ "251"
+ "30"
+ "341"
+ "37"
+ "423"
+ "436"
+ "461"
+ "47"
+ "471"
+ "480"
+ "492"
+ "5"
+ "575"
+ "6"
+ "691"
+ "720"
+ "834"
+ "858"
+ "910"
+ "920"
+ "943"
+ "@\"NLEmbedding\""
+ "@\"NSArray\"32@0:8@\"NSDictionary\"16@\"_PSRankAggregationContext\"24"
+ "@\"NSString\"16@?0@\"_PSAttachment\"8"
+ "@\"_PASCachedResult\""
+ "@\"_PSContactCatalogTaskMetrics\""
+ "@\"_PSMegadomeFamilyUtility\""
+ "@36@0:8@16q24B32"
+ "@40@0:8@16@24^d32"
+ "@48@0:8@16@24@32q40"
+ "@60@0:8@16@24B32@36@44@?52"
+ "Amusement Park"
+ "Animal"
+ "Animal Migration"
+ "Animal Shelter"
+ "Animal Sports"
+ "Antelope"
+ "Antique Car"
+ "Art"
+ "Art Gallery"
+ "AssetsFromIdentifiers_count"
+ "Athlete"
+ "Attempting to get family suggestions from Megadome"
+ "Automobile"
+ "B24@?0@\"NSString\"8@\"NSDictionary\"16"
+ "Baby"
+ "Badminton"
+ "Banknote"
+ "Baseball"
+ "Bathroom"
+ "Bathroom Room"
+ "Beach"
+ "Beach Volleyball"
+ "Bedroom"
+ "Bird"
+ "Bodybuilder"
+ "Boxing"
+ "Boy"
+ "British Cuisine"
+ "Car"
+ "Cattle"
+ "Checkbook"
+ "Child"
+ "Choreography"
+ "City Car"
+ "Coast"
+ "Combat Sport"
+ "Completed computing recency features"
+ "Completed contact catalog background task: %@"
+ "Computing %lu recency features from communication interactions"
+ "Computing %lu recency features from sharing interactions"
+ "Contact catalog loading disabled. We are using full online computation"
+ "Contact catalog not available, falling back to full online computation"
+ "Contact catalog not found at %@"
+ "Contact catalog task metrics: %@"
+ "Contact catalog task was expired during processing: %@"
+ "Could not fetch contact for Megadome person with contactId %@: %@"
+ "Could not find Megadome person with identifier %@, skipping"
+ "Could not find scene_tags.json in bundle"
+ "Could not update plist file for last run date: %@"
+ "Couldn't create os_log_t contactCatalogChannel"
+ "Couldn't create os_log_t contentAwareShareSheetChannel"
+ "Cow"
+ "Cricket"
+ "Cricketer"
+ "Cycle Sport"
+ "Dam"
+ "Deer"
+ "Derived %lu app-specific features for sourceBundleId: %@"
+ "Detected %@ clusters from scene tags: %@"
+ "Diagram"
+ "Dining Room"
+ "Disabled Sport"
+ "Document"
+ "Dog Sport"
+ "Drawing"
+ "Driving"
+ "Eating"
+ "Electric Car"
+ "Emergency Service"
+ "Engine Vehicle"
+ "Envelope"
+ "Error converting to JSON: %@"
+ "Error deserializing scene_tags.json: %@"
+ "Error encountered while reading last run date: %@"
+ "Error encountered while updating last run date: %@"
+ "Error fetching Megadome family recommendations: %@"
+ "Error getting Megadome family tag results: %@"
+ "Error initializing Megadome visual identifier view: %@"
+ "Error loading scene_tags.json: %@"
+ "Error querying interactions: %@"
+ "Failed to create Megadome entity tagging service: %@"
+ "Failed to create Megadome visual identifier view: %@"
+ "Failed to get family entities from Megadome: %@"
+ "Failed to parse contact catalog JSON: %@"
+ "Failed to read contact catalog: %@"
+ "Failed to save contact catalog: %@"
+ "Final Megadome suggestions: %tu"
+ "Foliage"
+ "Food Preservation"
+ "Football"
+ "Found %lu records"
+ "Fractal Art"
+ "Friday"
+ "GDConfiguration"
+ "GDEntityTaggingService"
+ "GDPersonTaggingOptions"
+ "Garden"
+ "Geology"
+ "Girl"
+ "Handwriting"
+ "Horse"
+ "Horse Racing"
+ "HyperRecentInteraction: %lu candidates from hyper recent calls: %@"
+ "HyperRecentInteraction: %lu candidates from hyper recent outgoing: %@"
+ "HyperRecentInteraction: %lu candidates from hyper recent viewed threads: %@"
+ "HyperRecentInteraction: Returning %lu candidates from %lu total recency candidates: %@"
+ "Ice Hockey"
+ "Indian Cuisine"
+ "Individual Sport"
+ "Indoor Sport"
+ "Infrastructure"
+ "Init _PSPhotoLibraryAssertion"
+ "Insect"
+ "Interior Design"
+ "Interior Room"
+ "Japanese Cuisine"
+ "Jazz"
+ "Judo"
+ "Junk Food"
+ "Keyboardist"
+ "Kitchen Room"
+ "Lake"
+ "Landscape"
+ "Landscape Lighting"
+ "Landscaping"
+ "Last interaction time"
+ "LastRunDate"
+ "Lawn"
+ "Leisure"
+ "Living Room"
+ "Loaded contact catalog: %lu conversations, %lu features, %lu properties, %lu personId sets, %lu bundleId counts (skipped %lu timeSince* features)"
+ "Loch"
+ "Mammal"
+ "Mapping scenetags %@"
+ "Media"
+ "Megadome person has no contact identifiers"
+ "Megadome returned %tu family recommendations"
+ "Megadome returned no family recommendations"
+ "Modern Art"
+ "Music Artist"
+ "Musician"
+ "Natural Disaster"
+ "Natural Environment"
+ "Net Sport"
+ "Newspaper"
+ "No records found"
+ "Ocean"
+ "One of the two vectors had magnitude 0, returning 0.0 for similarity"
+ "Open-Wheel Car"
+ "Outdoor"
+ "Outdoor Recreation"
+ "PSContactCatalogTaskData"
+ "PSInteractionAnalyzer"
+ "PSInteractionPattern"
+ "PSSceneTag"
+ "Pack Animal"
+ "Paint"
+ "Painting"
+ "Paper"
+ "Park"
+ "Passenger Car"
+ "Performance Art"
+ "Pet"
+ "PhotoLocalIdentifiers_count"
+ "Physical Fitness"
+ "Pianist"
+ "Playground"
+ "Police Car"
+ "Pond"
+ "Pool"
+ "Primate"
+ "Printed Page"
+ "Rabbit"
+ "Racing Automobile"
+ "Reason: URLASS Heuristic\n\nDescription: Scene tags similar to this URL has been shared to this contact(s) in the past"
+ "Receipt"
+ "Reflecting Pool"
+ "Reptile"
+ "Reranked Megadome suggestions using seed contacts"
+ "Reservoir"
+ "River"
+ "Road Racing"
+ "Rodent"
+ "Rowing"
+ "Rugby"
+ "Running contact catalog background task: %@"
+ "Sand"
+ "Saved contact catalog to: %@"
+ "Scene tag '%@' is not numeric; assuming it's cluster name"
+ "Scene tag '%@' is numeric; mapping it to %@"
+ "Scene tag '%@' is numeric; no mapping found ignoring"
+ "SceneTags_count"
+ "Sculpture"
+ "Sea"
+ "Sedan"
+ "Sharing Content Pattern"
+ "Sharing Content Tags"
+ "Sharing Time Pattern"
+ "Shooting Sport"
+ "Shore"
+ "Skate Park"
+ "Skipping %@ cannot cast tags to NSArray"
+ "Skipping Megadome recipient with no handle"
+ "Speakers Music"
+ "Sport Other"
+ "Sports Competition"
+ "Sports Prototype"
+ "Stadium"
+ "Steak"
+ "Street Art"
+ "SuggestionProxyTypeHyperRecentInteraction"
+ "SuggestionProxyTypeURLASS"
+ "Sunday"
+ "Supercar"
+ "Surfboard"
+ "Surfer"
+ "Surfing"
+ "Suv"
+ "Swimmer"
+ "T@\"NLEmbedding\",&,N,V_embedding"
+ "T@\"NSArray\",&,N,V_childrenClasses"
+ "T@\"NSArray\",&,N,V_contentPatterns"
+ "T@\"NSArray\",&,N,V_contentTags"
+ "T@\"NSArray\",&,N,V_detectorClasses"
+ "T@\"NSArray\",&,N,V_humanReadableSynonyms"
+ "T@\"NSArray\",&,N,V_parentClasses"
+ "T@\"NSArray\",&,N,V_timePatterns"
+ "T@\"NSArray\",R,N,V_priorityOrder"
+ "T@\"NSMutableDictionary\",&,N,V_numberOfEngagedSuggestionsFromSourceAppWithConversation"
+ "T@\"NSMutableDictionary\",&,N,V_numberOfSharesFromSourceAppWithConversation"
+ "T@\"NSMutableDictionary\",&,N,V_sharingContentPatternByConversationId"
+ "T@\"NSMutableDictionary\",&,N,V_sharingTimePatternByConversationId"
+ "T@\"NSSet\",&,N,V_heuristicsToFuse"
+ "T@\"NSString\",&,N,V_humanReadableLabel"
+ "T@\"NSString\",&,N,V_label"
+ "T@\"NSString\",&,N,V_network"
+ "T@\"PHPhotoLibrary\",R,N"
+ "T@\"_CDInteractionStore\",&,N,V_store"
+ "T@\"_PSMegadomeFamilyUtility\",&,N,V_megadomeUtility"
+ "TB,N,V_isSearchable"
+ "Td,N,V_k"
+ "Td,N,V_recencyTimestamp"
+ "Td,N,V_searchThreshold"
+ "Td,N,V_timeSinceLastRun"
+ "Teardown _PSPhotoLibraryAssertion (no action taken due to trylock not successful)"
+ "Teardown _PSPhotoLibraryAssertion (will tell PhotoLibrary to shutdown)"
+ "Technician"
+ "Text"
+ "TimedOut"
+ "Toddler"
+ "Tq,N,V_frequency"
+ "Tq,N,V_identifier"
+ "Tq,R,N,V_embeddingDimension"
+ "Track And Field"
+ "URLASS"
+ "Unable to deserialize JSON from data: %@"
+ "Unable to find embedding for %@"
+ "Unable to get data from %@: %@"
+ "Unable to get url from %@.json"
+ "Ungulates"
+ "Unknown Contact"
+ "Using Megadome for family recommendations"
+ "Using Megadome for getting family recipients"
+ "Using RRF aggregation strategy with k=%f"
+ "Using contact catalog but deriving app-specific and recency features online"
+ "Using priority-based aggregation strategy"
+ "Using programmatic override for heuristic %{public}@, parameter %{public}@: %{public}@"
+ "VCPMediaAnalysisService"
+ "Value overriden by user defaults for heuristic %{public}@, parameter %{public}@: %{public}@"
+ "Vegetation"
+ "Vehicle"
+ "Vintage Car"
+ "Volcanic Crater Lake"
+ "Whole Foods"
+ "Wildlife"
+ "Work Of Art"
+ "Wrestling"
+ "Writing"
+ "Zoo"
+ "_PSBoWEmbedding"
+ "_PSContactCatalog"
+ "_PSContactCatalogBackgroundTask"
+ "_PSContactCatalogTask"
+ "_PSContactCatalogTaskMetrics"
+ "_PSMegadomeFamilyUtility"
+ "_PSPhotoLibraryAssertion"
+ "_PSPhotoSuggestions people cancellation no-op because request was for 0 items"
+ "_PSPhotoSuggestions person request cancelled (%tu of %tu attachments were still in-flight)"
+ "_PSPhotoSuggestionsCancellationToken"
+ "_PSRankAggregationContext"
+ "_PSRankAggregationPriorityBased"
+ "_PSRankAggregationPriorityBased: found duplicate proxy key, skipping '%{public}@' in list %{public}@"
+ "_PSRankAggregationRRF"
+ "_PSRankAggregationRRF: Fused %lu candidates from %lu heuristics with k=%.2f"
+ "_PSRankAggregationStrategy"
+ "_PSSceneTagsUtils"
+ "_childrenClasses"
+ "_contentPatterns"
+ "_contentTags"
+ "_detectorClasses"
+ "_embedding"
+ "_embeddingDimension"
+ "_frequency"
+ "_heuristicsToFuse"
+ "_humanReadableLabel"
+ "_humanReadableSynonyms"
+ "_init"
+ "_isSearchable"
+ "_label"
+ "_lastRunDate"
+ "_lazyLibrary"
+ "_megadomeUtility"
+ "_network"
+ "_numberOfEngagedSuggestionsFromSourceAppWithConversation"
+ "_numberOfSharesFromSourceAppWithConversation"
+ "_parentClasses"
+ "_personCancellationArray"
+ "_priorityOrder"
+ "_recencyTimestamp"
+ "_sceneCancellationBlock"
+ "_searchThreshold"
+ "_sharingContentPatternByConversationId"
+ "_sharingTimePatternByConversationId"
+ "_timePatterns"
+ "_timeSinceLastRun"
+ "addSharePlaySuggestionsToProxies:interactionStatistics:predictionContext:"
+ "afternoon"
+ "aggregateRankings:withContext:"
+ "allInteractionsStats"
+ "analyzeInteractionPatterns:"
+ "any;-;%@"
+ "averageEmbeddings:"
+ "cancelRequest:"
+ "categorizeTime:"
+ "childrenClasses"
+ "com.apple.CoreDuet"
+ "com.apple.PeopleSuggester.ContactCatalogTask"
+ "com.apple.proactive.pscontactcatalogtask"
+ "computeEmbeddingForText:"
+ "computeEmbeddingForWords:"
+ "computeEmbeddingsForTexts:"
+ "computeEmbeddingsForWordArrays:"
+ "computeOrLoadFeaturesForInteractionStatistics:trialClient:"
+ "computeRecencyFeaturesWithInteractionStore:"
+ "conditioned_featureCountFor_animal"
+ "conditioned_featureCountFor_art"
+ "conditioned_featureCountFor_beach"
+ "conditioned_featureCountFor_car"
+ "conditioned_featureCountFor_child"
+ "conditioned_featureCountFor_document"
+ "conditioned_featureCountFor_interior_room"
+ "conditioned_featureCountFor_lake"
+ "conditioned_featureCountFor_landscape"
+ "conditioned_featureCountFor_maintainance_services"
+ "conditioned_featureCountFor_natural_environment"
+ "conditioned_featureCountFor_park"
+ "conditioned_featureCountFor_pool"
+ "conditioned_featureCountFor_writing"
+ "contactCatalog"
+ "contactCatalogChannel"
+ "contact_catalog.json"
+ "contentAwareShareSheet"
+ "contentAwareShareSheetChannel"
+ "contentPatterns"
+ "contentTags"
+ "conversationIDForInteraction:"
+ "convertSetsToArraysInObject:"
+ "convertTimeToChunks:"
+ "cosineSimilarityBetweenEmbedding:andEmbedding:"
+ "dataWithJSONObject:options:error:"
+ "deriveAppSpecificFeaturesFromCatalog"
+ "detectorClasses"
+ "dimension"
+ "early morning"
+ "embedding"
+ "embeddingBasedURLSuggestionProxiesForInteractionStatistics:withPredictionContext:"
+ "embeddingDimension"
+ "entitiesForTag:options:error:"
+ "enumerateTokensInRange:usingBlock:"
+ "error getting scene tags for photo identifiers %{public}@: %@"
+ "extractContactInfoFromInteraction:"
+ "familyRecipientsFromMegadomeWithError:"
+ "familyRecipientsFromMegadomeWithPredictionContext:"
+ "familyRecommendationSuggestionsFromMegadomeWithPredictionContext:"
+ "family_recommender_use_megadome"
+ "featureCountFor_animal"
+ "featureCountFor_art"
+ "featureCountFor_beach"
+ "featureCountFor_car"
+ "featureCountFor_child"
+ "featureCountFor_document"
+ "featureCountFor_interior_room"
+ "featureCountFor_lake"
+ "featureCountFor_landscape"
+ "featureCountFor_maintainance_services"
+ "featureCountFor_natural_environment"
+ "featureCountFor_park"
+ "featureCountFor_pool"
+ "featureCountFor_writing"
+ "featuresKey"
+ "fetchOptionsWithInclusiveDefaultsForPhotoLibrary:"
+ "fetchingSceneTagsRequestSpan"
+ "findMostSimilarToQuery:fromCandidates:similarity:"
+ "frequency"
+ "generateContactCatalog:maxInteractions:updateCatalog:"
+ "generateContactSummariesWithMaxInteractions:"
+ "generateSummaryForContactWithConversationId:interactions:"
+ "getMeContactIdentifierAsync"
+ "heuristicsToFuse"
+ "humanReadableLabel"
+ "humanReadableLabelForIdentifier:"
+ "humanReadableSynonyms"
+ "humanReadableSynonymsForIdentifier:"
+ "hyperRecentInteractionSuggestionProxiesForInteractionStatistics:maxCandidates:"
+ "iCloudFamily - Megadome"
+ "idValue"
+ "identifierToLabelLookup"
+ "identifierToSynonymsLookup"
+ "incrementNumberOfEngagedSuggestionsFromSourceAppWithConversation:forConversationId:"
+ "incrementNumberOfSharesFromSourceAppWithConversation:forConversationId:"
+ "index"
+ "initWithConfig:error:"
+ "initWithData:encoding:"
+ "initWithDouble:"
+ "initWithEmbedding:"
+ "initWithK:heuristicsToFuse:"
+ "initWithLanguage:"
+ "initWithPhotoLibraryURL:"
+ "initWithPriorityOrder:"
+ "initWithStore:"
+ "initWithTagThresholds:"
+ "initWithTimePatterns:contentPatterns:contentTags:frequency:"
+ "initWithUnit:"
+ "invalid request ID when getting scene tags (photoLocalIdentifiers count %tu: %@)"
+ "isSearchable"
+ "kPSContactSummaryHandleKey"
+ "kPSContactSummaryLastInteractionTimeKey"
+ "kPSContactSummaryNameKey"
+ "kPSContactSummarySharingContentPatternKey"
+ "kPSContactSummarySharingContentTagsKey"
+ "kPSContactSummarySharingTimePatternKey"
+ "languageCode"
+ "letterCharacterSet"
+ "library"
+ "loadFeaturesAndPropertiesFromContactCatalog"
+ "loadJSONResourceAsDict:"
+ "loadSceneTags"
+ "loadTagsToClusterNamesDict"
+ "matchedSceneCategoriesCount"
+ "megadomeResultsForFamilyTagWithError:"
+ "megadomeUtility"
+ "midday"
+ "network"
+ "night"
+ "noon"
+ "numberFromString:"
+ "numberOfEngagedSuggestionsFromSourceApp"
+ "numberOfEngagedSuggestionsFromSourceAppWithConversation"
+ "numberOfSharesFromSourceApp"
+ "numberOfSharesFromSourceAppWithConversation"
+ "parentClasses"
+ "peopleViewWithError:"
+ "peoplesuggester_catalog_inference"
+ "personIdsInPastShareInteractions"
+ "personIdsInPastShareInteractionsKey"
+ "personIdsInPastSyntheticShareInteractions"
+ "personIdsInPastSyntheticShareInteractionsKey"
+ "photoLibraryAssertion"
+ "priorityOrder"
+ "propertiesKey"
+ "q24@?0@\"_PSSuggestionProxy\"8@\"_PSSuggestionProxy\"16"
+ "rankAggregationStrategyType"
+ "recencyFeaturesCount"
+ "recencyOnlyComputation"
+ "recencyTimestamp"
+ "recipientFromMegadomePerson:"
+ "recipientsFromScoredEntities:inVisualIdentifierView:"
+ "requestProcessingTypes:forAssetsWithLocalIdentifiers:fromPhotoLibraryWithURL:progressHandler:completionHandler:"
+ "resultNonnullWithBlock:"
+ "retrieveSceneTagsFromLibrarySpan"
+ "rrfConstantK"
+ "saveJSONToFile:"
+ "saveLastRunDate"
+ "savedLastRunDate"
+ "scene request ended (timedOut: %d, photoLocalIdentifiers count %tu: %@)"
+ "scene tags photo library prewarm"
+ "sceneBasedSuggestionsUsingEmbedding:withPredictionContext:"
+ "sceneClusterDict"
+ "sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:"
+ "sceneTagsSpan"
+ "sceneTagsToClusterNames:"
+ "scene_clusters"
+ "scene_tags"
+ "scoredEntities"
+ "searchThreshold"
+ "setChildrenClasses:"
+ "setContentPatterns:"
+ "setContentTags:"
+ "setDetectorClasses:"
+ "setEmbedding:"
+ "setFrequency:"
+ "setHeuristicsToFuse:"
+ "setHumanReadableLabel:"
+ "setHumanReadableSynonyms:"
+ "setIsSearchable:"
+ "setK:"
+ "setLabel:"
+ "setMegadomeUtility:"
+ "setNetwork:"
+ "setNumberOfEngagedSuggestionsFromSourceAppWithConversation:"
+ "setNumberOfSharesFromSourceAppWithConversation:"
+ "setParentClasses:"
+ "setRecencyTimestamp:"
+ "setSearchThreshold:"
+ "setSharingContentPatternByConversationId:"
+ "setSharingTimePatternByConversationId:"
+ "setStore:"
+ "setString:"
+ "setTimePatterns:"
+ "setTimeSinceLastRun:"
+ "sharedAnalysisService"
+ "sharingContentPatternByConversationId"
+ "sharingTimePatternByConversationId"
+ "shouldUseCatalogInference"
+ "similarity"
+ "sortUsingDescriptors:"
+ "sourceBundleId is null"
+ "store"
+ "stringWithContentsOfFile:encoding:error:"
+ "suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:"
+ "taggingOptions"
+ "timePatterns"
+ "timeSinceLastRun"
+ "tokenizeText:"
+ "unsafeShutdownLibraryWithPhotoLibraryURL:"
+ "v16@?0d8"
+ "v20@?0@\"NSArray\"8B16"
+ "v40@?0{_NSRange=QQ}8Q24^B32"
+ "vectorForString:"
+ "weekend"
+ "wordEmbeddingForLanguage:"
+ "work hours"
+ "writeToFile:atomically:encoding:error:"
+ "{}"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
- "10433"
- "1067"
- "12291"
- "12384"
- "12456"
- "1252"
- "1256"
- "12669"
- "12906"
- "12944"
- "1307"
- "13179"
- "13568"
- "1436"
- "14599"
- "1501"
- "1510"
- "15119"
- "15123"
- "15635"
- "159"
- "16406"
- "18195"
- "18303"
- "186"
- "343"
- "462"
- "545"
- "571"
- "588"
- "648"
- "698"
- "906"
- "@\"NSMutableArray\"16@?0@\"NSArray\"8"
- "Auto Racing"
- "Ball"
- "Beagle"
- "Cheerleading"
- "Dancesport"
- "Dancing"
- "Digital Piano"
- "Dog Walking"
- "Electrophone"
- "Feline"
- "Figure Skating"
- "Fish as Food"
- "Flute"
- "Fried Food"
- "Frisbee"
- "Guitar"
- "Gym"
- "Hound"
- "Lunch"
- "Music Venue"
- "Musical Keyboard"
- "Nascar"
- "Percussion Instrument"
- "Racquet"
- "Roller Sport"
- "Soup"
- "Spaniel"
- "String Instrument"
- "Ukulele"
- "Using override for heuristic %{public}@, parameter %{public}@: %{public}@"
- "Volleyball"
- "Weight Training"
- "Wine"
- "Woodwind"
- "_PSPhotoSuggestions request cancelled (%tu of %tu attachments were still in-flight)"
- "_PSPhotoSuggestions request cancelled (no-op because request was for 0 items)"
- "_PSPhotoUtils prewarm"
- "conditioned_featureCountFor_pet"
- "digest"
- "featureCountFor_pet"
- "fetchOptionsWithInclusiveDefaults"
- "initWithLatestTaxonomy"
- "isCloudPhotoLibraryEnabled"
- "prewarmPhotosFrameworks"
- "sharedPhotoLibrary"
- "unexpected cancel token (not array): %{public}@"
- "unexpected cancel token (some items are not NSNumber): %{public}@"

```
