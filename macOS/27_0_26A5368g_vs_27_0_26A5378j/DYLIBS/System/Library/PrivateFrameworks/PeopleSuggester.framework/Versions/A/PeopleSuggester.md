## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/Versions/A/PeopleSuggester`

```diff

-  __TEXT.__text: 0x11f76c
-  __TEXT.__objc_methlist: 0xa8d4
-  __TEXT.__const: 0x968
-  __TEXT.__gcc_except_tab: 0x3fb4
-  __TEXT.__cstring: 0x30b11
-  __TEXT.__oslogstring: 0xfaf4
+  __TEXT.__text: 0x127c04
+  __TEXT.__objc_methlist: 0xac94
+  __TEXT.__const: 0x978
+  __TEXT.__gcc_except_tab: 0x41fc
+  __TEXT.__cstring: 0x31337
+  __TEXT.__oslogstring: 0xfd50
   __TEXT.__dlopen_cstrs: 0x160f
   __TEXT.__ustring: 0x7e4
-  __TEXT.__unwind_info: 0x3240
+  __TEXT.__unwind_info: 0x3348
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x18d0
-  __DATA_CONST.__objc_classlist: 0x558
+  __DATA_CONST.__const: 0x1948
+  __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b40
-  __DATA_CONST.__objc_superrefs: 0x3f0
-  __DATA_CONST.__objc_arraydata: 0x39ba8
-  __DATA_CONST.__got: 0x910
-  __AUTH_CONST.__const: 0x4240
-  __AUTH_CONST.__cfstring: 0x7e340
-  __AUTH_CONST.__objc_const: 0x150c8
-  __AUTH_CONST.__objc_intobj: 0x1140
+  __DATA_CONST.__objc_selrefs: 0x6d38
+  __DATA_CONST.__objc_superrefs: 0x400
+  __DATA_CONST.__objc_arraydata: 0x39d78
+  __DATA_CONST.__got: 0x928
+  __AUTH_CONST.__const: 0x4340
+  __AUTH_CONST.__cfstring: 0x7eee0
+  __AUTH_CONST.__objc_const: 0x155e8
+  __AUTH_CONST.__objc_intobj: 0x1170
   __AUTH_CONST.__objc_arrayobj: 0x11d18
-  __AUTH_CONST.__objc_doubleobj: 0xd0
-  __AUTH_CONST.__objc_dictobj: 0x22628
-  __AUTH_CONST.__auth_got: 0x6e8
-  __AUTH.__objc_data: 0xeb0
-  __DATA.__objc_ivar: 0xeac
+  __AUTH_CONST.__objc_doubleobj: 0xe0
+  __AUTH_CONST.__objc_dictobj: 0x226c8
+  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH.__objc_data: 0x1bd0
+  __DATA.__objc_ivar: 0xf0c
   __DATA.__data: 0x4f0
-  __DATA.__bss: 0x740
-  __DATA_DIRTY.__objc_data: 0x26c0
+  __DATA.__bss: 0x770
+  __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__bss: 0x780
   - /System/Library/Frameworks/CoreData.framework/Versions/A/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5134
-  Symbols:   12227
-  CStrings:  33700
+  Functions: 5229
+  Symbols:   12447
+  CStrings:  33897
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[_PSDebugUI descriptionForReasonType:]
+ +[_PSEnsembleModel canonicalIdentifierForSuggestion:]
+ +[_PSEnsembleModel(EngagementSpans) engagedCandidateInCatalogStateForConversationId:catalogConversationIds:interactionStatistics:]
+ +[_PSEnsembleModel(EngagementSpans) proxyRankAttributesForConversationId:candidateBundleId:proxyRankLookup:]
+ +[_PSEnsembleModel(ProxyRankLookup) catalogInventoryAttributesForSnapshot:statistics:]
+ +[_PSEnsembleModel(ProxyRankLookup) fullCatalogRanksForSortedConversationIds:cap:bundleIdMap:]
+ +[_PSEnsembleModel(ProxyRankLookup) fullySortedConversationIdsForFeatureNames:interactionsStatistics:]
+ +[_PSEnsembleModel(ProxyRankLookup) isReplayInstrumentationEnabled]
+ +[_PSFeatureCache rotatingDeviceIdentifier]
+ +[_PSPhotoUtils photoAgeSecondsForPhotoLocalIdentifier:]
+ +[_PSSuggestionBuilder(Telemetry) candidAttributesForDedupKeys:multiEngineByDedupKey:]
+ +[_PSSuggestionBuilder(Telemetry) candidStringFromContributions:]
+ +[_PSSuggestionBuilder(Telemetry) captureMultiEngineAndPreRankContributionsFromProxies:dedupKeyResolver:privatizedIdResolver:outMultiEngineByDedupKey:outRawContributions:]
+ +[_PSSuggestionBuilder(Telemetry) firstReasonTypeFromContributions:]
+ +[_PSSuggestionBuilder(Telemetry) modelScoreAttributesForAvailable:]
+ +[_PSSuggestionBuilder(Telemetry) preRankCandidatesAttributesForRawContributions:perEngineCap:]
+ +[_PSSuggestionBuilder(Telemetry) prerank_contribution:worseThan:]
+ +[_PSSuggestionBuilder(Telemetry) prerank_jsonObjectFromContribution:]
+ +[_PSURLClustersUtils cachedEmbeddingsForClusters:]
+ -[AeroMLTracerSpan intervalInMilliSeconds]
+ -[_PSDebugUI .cxx_destruct]
+ -[_PSDebugUI appendCandidateSectionTo:forSuggestion:]
+ -[_PSDebugUI appendCatalogSectionTo:canonicalID:]
+ -[_PSDebugUI appendContentSectionTo:canonicalID:]
+ -[_PSDebugUI appendDevLayoutTo:canonicalID:suggestion:]
+ -[_PSDebugUI appendEnvSectionTo:]
+ -[_PSDebugUI appendIndexSectionTo:]
+ -[_PSDebugUI appendLatencySectionTo:]
+ -[_PSDebugUI appendRankSectionTo:canonicalID:]
+ -[_PSDebugUI appendUserLayoutTo:canonicalID:]
+ -[_PSDebugUI appendWarningsSectionTo:]
+ -[_PSDebugUI applyDebugTextToSuggestions:canonicalIDProvider:]
+ -[_PSDebugUI engineRankSummaryStringForCanonicalID:]
+ -[_PSDebugUI initWithContext:]
+ -[_PSDebugUI initWithContext:showDevLayout:]
+ -[_PSDebugUI isEnabled]
+ -[_PSDebugUI recordCatalogStatsForCanonicalID:sceneClusters:titleClusters:]
+ -[_PSDebugUI recordDurationMillis:forPhase:]
+ -[_PSDebugUI recordEngineRankSummary:forCanonicalID:]
+ -[_PSDebugUI recordIndexStats:]
+ -[_PSDebugUI recordSessionTopMappedCluster:]
+ -[_PSDebugUI recordSpan:forPhase:]
+ -[_PSDebugUI showDevLayout]
+ -[_PSEnsembleModel _shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:predictionContext:]
+ -[_PSEnsembleModel enrichSuggestions:withStatsMap:predictionContext:]
+ -[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:predictionContext:]
+ -[_PSHeuristics _suggestionProxiesFromAttachmentTagsUsingBoW:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:]
+ -[_PSHeuristics _suggestionProxiesFromAttachmentTagsUsingSentenceEmbedding:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:]
+ -[_PSHeuristics sceneBasedSuggestionsUsingEmbedding:withPredictionContext:config:useCatalog:similarityThreshold:sentenceSimilarityThreshold:weightedScoreThreshold:]
+ -[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:sentenceSimilarityThreshold:weightedScoreThreshold:parentSpan:]
+ -[_PSPredictionContext catalogConversationIdsSnapshot]
+ -[_PSPredictionContext debugUI]
+ -[_PSPredictionContext modelScoreAvailable]
+ -[_PSPredictionContext numberOfPeopleInPhoto]
+ -[_PSPredictionContext passV1MappedFaceTagCount]
+ -[_PSPredictionContext photoAgeSeconds]
+ -[_PSPredictionContext setCatalogConversationIdsSnapshot:]
+ -[_PSPredictionContext setModelScoreAvailable:]
+ -[_PSPredictionContext setNumberOfPeopleInPhoto:]
+ -[_PSPredictionContext setPassV1MappedFaceTagCount:]
+ -[_PSPredictionContext setPhotoAgeSeconds:]
+ -[_PSPredictionContext setTitleClusters:]
+ -[_PSPredictionContext setTitleSource:]
+ -[_PSPredictionContext setTopDomainURL:]
+ -[_PSPredictionContext titleClusters]
+ -[_PSPredictionContext titleSource]
+ -[_PSPredictionContext topDomainURL]
+ -[_PSSentenceEmbedding .cxx_destruct]
+ -[_PSSentenceEmbedding computeEmbeddingForText:]
+ -[_PSSentenceEmbedding cosineSimilarityBetweenEmbedding:andEmbedding:]
+ -[_PSSentenceEmbedding embeddingDimension]
+ -[_PSSentenceEmbedding embedding]
+ -[_PSSentenceEmbedding initWithEmbedding:]
+ -[_PSSentenceEmbedding initWithLanguage:]
+ -[_PSSentenceEmbedding init]
+ -[_PSSentenceEmbedding setEmbedding:]
+ -[_PSSuggestionBuilder interactionStatistics]
+ -[_PSSuggestionBuilder predictionContext]
+ -[_PSSuggestionBuilder setInteractionStatistics:]
+ -[_PSSuggestionBuilder setPredictionContext:]
+ -[_PSTrialClient sassSentenceSimilarityThreshold]
+ GCC_except_table113
+ GCC_except_table117
+ GCC_except_table189
+ GCC_except_table199
+ GCC_except_table205
+ GCC_except_table71
+ GCC_except_table88
+ GCC_except_table91
+ OBJC_IVAR_$__PSDebugUI._catalogSceneClustersByID
+ OBJC_IVAR_$__PSDebugUI._catalogTitleClustersByID
+ OBJC_IVAR_$__PSDebugUI._context
+ OBJC_IVAR_$__PSDebugUI._durationsByPhase
+ OBJC_IVAR_$__PSDebugUI._engineRankSummaryByID
+ OBJC_IVAR_$__PSDebugUI._indexStats
+ OBJC_IVAR_$__PSDebugUI._isInternalBuild
+ OBJC_IVAR_$__PSDebugUI._sessionTopMappedCluster
+ OBJC_IVAR_$__PSDebugUI._showDevLayout
+ OBJC_IVAR_$__PSInteractionsStatistics.catalogTotalOutgoingInteractions
+ OBJC_IVAR_$__PSInteractionsStatistics.catalogTotalShares
+ OBJC_IVAR_$__PSPredictionContext._catalogConversationIdsSnapshot
+ OBJC_IVAR_$__PSPredictionContext._debugUI
+ OBJC_IVAR_$__PSPredictionContext._modelScoreAvailable
+ OBJC_IVAR_$__PSPredictionContext._numberOfPeopleInPhoto
+ OBJC_IVAR_$__PSPredictionContext._passV1MappedFaceTagCount
+ OBJC_IVAR_$__PSPredictionContext._photoAgeSeconds
+ OBJC_IVAR_$__PSPredictionContext._titleClusters
+ OBJC_IVAR_$__PSPredictionContext._titleSource
+ OBJC_IVAR_$__PSPredictionContext._topDomainURL
+ OBJC_IVAR_$__PSSentenceEmbedding._embedding
+ OBJC_IVAR_$__PSSentenceEmbedding._embeddingDimension
+ OBJC_IVAR_$__PSSuggestionBuilder._interactionStatistics
+ OBJC_IVAR_$__PSSuggestionBuilder._predictionContext
+ _OBJC_CLASS_$__PSDebugUI
+ _OBJC_CLASS_$__PSSentenceEmbedding
+ _OBJC_METACLASS_$__PSDebugUI
+ _OBJC_METACLASS_$__PSSentenceEmbedding
+ __100-[_PSSuggestionBuilder suggestionsFromProxies:shareInteractions:messageInteractions:maxSuggestions:]_block_invoke
+ __111-[_PSEnsembleModel _shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:predictionContext:]_block_invoke
+ __144-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:predictionContext:]_block_invoke
+ __209-[_PSHeuristics _suggestionProxiesFromAttachmentTagsUsingBoW:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:]_block_invoke
+ __223-[_PSHeuristics _suggestionProxiesFromAttachmentTagsUsingSentenceEmbedding:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:]_block_invoke
+ __83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke
+ __OBJC_$_CLASS_METHODS__PSDebugUI
+ __OBJC_$_CLASS_METHODS__PSEnsembleModel(EngagementSpans|ProxyRankLookup)
+ __OBJC_$_CLASS_METHODS__PSFeatureCache
+ __OBJC_$_CLASS_METHODS__PSSuggestionBuilder(Telemetry)
+ __OBJC_$_INSTANCE_METHODS__PSDebugUI
+ __OBJC_$_INSTANCE_METHODS__PSSentenceEmbedding
+ __OBJC_$_INSTANCE_VARIABLES__PSDebugUI
+ __OBJC_$_INSTANCE_VARIABLES__PSSentenceEmbedding
+ __OBJC_$_PROP_LIST__PSDebugUI
+ __OBJC_$_PROP_LIST__PSSentenceEmbedding
+ __OBJC_CLASS_RO_$__PSDebugUI
+ __OBJC_CLASS_RO_$__PSSentenceEmbedding
+ __OBJC_METACLASS_RO_$__PSDebugUI
+ __OBJC_METACLASS_RO_$__PSSentenceEmbedding
+ ___100-[_PSSuggestionBuilder suggestionsFromProxies:shareInteractions:messageInteractions:maxSuggestions:]_block_invoke
+ ___102+[_PSEnsembleModel(ProxyRankLookup) fullySortedConversationIdsForFeatureNames:interactionsStatistics:]_block_invoke
+ ___103-[_PSHeuristics peopleAwareSuggestionProxiesForInteractionStatistics:withPersonIdentifiers:useCatalog:]_block_invoke
+ ___108+[_PSEnsembleModel(EngagementSpans) proxyRankAttributesForConversationId:candidateBundleId:proxyRankLookup:]_block_invoke
+ ___111-[_PSEnsembleModel _shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:predictionContext:]_block_invoke
+ ___111-[_PSEnsembleModel _shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:predictionContext:]_block_invoke_2
+ ___111-[_PSEnsembleModel _shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:predictionContext:]_block_invoke_3
+ ___144-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:predictionContext:]_block_invoke
+ ___164-[_PSHeuristics sceneBasedSuggestionsUsingEmbedding:withPredictionContext:config:useCatalog:similarityThreshold:sentenceSimilarityThreshold:weightedScoreThreshold:]_block_invoke
+ ___209-[_PSHeuristics _suggestionProxiesFromAttachmentTagsUsingBoW:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:]_block_invoke
+ ___223-[_PSHeuristics _suggestionProxiesFromAttachmentTagsUsingSentenceEmbedding:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:]_block_invoke
+ ___39+[_PSDebugUI descriptionForReasonType:]_block_invoke
+ ___42-[AeroMLTracerSpan intervalInMilliSeconds]_block_invoke
+ ___43+[_PSFeatureCache rotatingDeviceIdentifier]_block_invoke
+ ___95+[_PSSuggestionBuilder(Telemetry) preRankCandidatesAttributesForRawContributions:perEngineCap:]_block_invoke
+ ____formatClusterHistogram_block_invoke
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80r88r96r_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_160_e8_32s40s48s56s64s72s80s88r96r104r112r120r128r136r144r_e25_v32?0"NSString"8Q16^B24l
+ ___block_descriptor_32_e39_q24?0"NSDictionary"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32w_e38_"NSString"16?0"_PSSuggestionProxy"8l
+ ___block_descriptor_48_e8_32s40s_e30_v32?0"_PSSuggestion"8Q16^B24l
+ ___block_descriptor_48_e8_32s40w_e38_"NSString"16?0"_PSSuggestionProxy"8l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80r88r96r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r112r120r128r136r144r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80r88r96r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88r96r104r112r120r128r136r144r
+ __formatClusterHistogram
+ _kPSCatalogInventoryWireCap
+ _kPSInstrumentationVersion
+ _kPSStaticContentFeatureMaxFaceShareIoUWithConversationAsString
+ _kProxyRankLookupCap
+ _log2
+ _objc_msgSend$_shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:predictionContext:
+ _objc_msgSend$_suggestionProxiesFromAttachmentTagsUsingBoW:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:
+ _objc_msgSend$_suggestionProxiesFromAttachmentTagsUsingSentenceEmbedding:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:
+ _objc_msgSend$appendCandidateSectionTo:forSuggestion:
+ _objc_msgSend$appendCatalogSectionTo:canonicalID:
+ _objc_msgSend$appendContentSectionTo:canonicalID:
+ _objc_msgSend$appendDevLayoutTo:canonicalID:suggestion:
+ _objc_msgSend$appendEnvSectionTo:
+ _objc_msgSend$appendIndexSectionTo:
+ _objc_msgSend$appendLatencySectionTo:
+ _objc_msgSend$appendRankSectionTo:canonicalID:
+ _objc_msgSend$appendUserLayoutTo:canonicalID:
+ _objc_msgSend$appendWarningsSectionTo:
+ _objc_msgSend$applyDebugTextToSuggestions:canonicalIDProvider:
+ _objc_msgSend$cachedEmbeddingsForClusters:
+ _objc_msgSend$candidAttributesForDedupKeys:multiEngineByDedupKey:
+ _objc_msgSend$candidStringFromContributions:
+ _objc_msgSend$captureMultiEngineAndPreRankContributionsFromProxies:dedupKeyResolver:privatizedIdResolver:outMultiEngineByDedupKey:outRawContributions:
+ _objc_msgSend$catalogConversationIdsSnapshot
+ _objc_msgSend$catalogInventoryAttributesForSnapshot:statistics:
+ _objc_msgSend$debugUI
+ _objc_msgSend$descriptionForReasonType:
+ _objc_msgSend$engagedCandidateInCatalogStateForConversationId:catalogConversationIds:interactionStatistics:
+ _objc_msgSend$engineRankSummaryStringForCanonicalID:
+ _objc_msgSend$enrichSuggestions:withStatsMap:predictionContext:
+ _objc_msgSend$firstReasonTypeFromContributions:
+ _objc_msgSend$fullCatalogRanksForSortedConversationIds:cap:bundleIdMap:
+ _objc_msgSend$fullySortedConversationIdsForFeatureNames:interactionsStatistics:
+ _objc_msgSend$initWithContext:
+ _objc_msgSend$initWithContext:showDevLayout:
+ _objc_msgSend$initWithData:encoding:
+ _objc_msgSend$interactionStatistics
+ _objc_msgSend$intervalInMilliSeconds
+ _objc_msgSend$isReplayInstrumentationEnabled
+ _objc_msgSend$modelScoreAttributesForAvailable:
+ _objc_msgSend$modelScoreAvailable
+ _objc_msgSend$numberOfPeopleInPhoto
+ _objc_msgSend$passV1MappedFaceTagCount
+ _objc_msgSend$photoAgeSeconds
+ _objc_msgSend$photoAgeSecondsForPhotoLocalIdentifier:
+ _objc_msgSend$preRankCandidatesAttributesForRawContributions:perEngineCap:
+ _objc_msgSend$predictionContext
+ _objc_msgSend$prerank_contribution:worseThan:
+ _objc_msgSend$prerank_jsonObjectFromContribution:
+ _objc_msgSend$proxyRankAttributesForConversationId:candidateBundleId:proxyRankLookup:
+ _objc_msgSend$recordCatalogStatsForCanonicalID:sceneClusters:titleClusters:
+ _objc_msgSend$recordDurationMillis:forPhase:
+ _objc_msgSend$recordEngineRankSummary:forCanonicalID:
+ _objc_msgSend$recordIndexStats:
+ _objc_msgSend$recordSessionTopMappedCluster:
+ _objc_msgSend$recordSpan:forPhase:
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$rotatingDeviceIdentifier
+ _objc_msgSend$sassSentenceSimilarityThreshold
+ _objc_msgSend$sceneBasedSuggestionsUsingEmbedding:withPredictionContext:config:useCatalog:similarityThreshold:sentenceSimilarityThreshold:weightedScoreThreshold:
+ _objc_msgSend$sentenceEmbeddingForLanguage:
+ _objc_msgSend$setCatalogConversationIdsSnapshot:
+ _objc_msgSend$setInteractionStatistics:
+ _objc_msgSend$setModelScoreAvailable:
+ _objc_msgSend$setNumberOfPeopleInPhoto:
+ _objc_msgSend$setPassV1MappedFaceTagCount:
+ _objc_msgSend$setPhotoAgeSeconds:
+ _objc_msgSend$setPredictionContext:
+ _objc_msgSend$setTitleSource:
+ _objc_msgSend$suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:sentenceSimilarityThreshold:weightedScoreThreshold:parentSpan:
+ _objc_msgSend$suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:predictionContext:
+ _objc_msgSend$titleSource
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
+ _sCachedClusterEmbeddings
+ _sCachedClusterNames
+ appendLatencySectionTo:.phases
+ descriptionForReasonType:.once
+ descriptionForReasonType:.table
+ rotatingDeviceIdentifier.defaults
+ rotatingDeviceIdentifier.once
- -[_PSEnsembleModel _shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:]
- -[_PSEnsembleModel canonicalIdentifierForSuggestion:]
- -[_PSEnsembleModel enrichSuggestions:withStatsMap:]
- -[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]
- -[_PSHeuristics sceneBasedSuggestionsUsingEmbedding:withPredictionContext:config:useCatalog:similarityThreshold:weightedScoreThreshold:]
- -[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:]
- GCC_except_table104
- GCC_except_table106
- GCC_except_table107
- GCC_except_table187
- GCC_except_table197
- GCC_except_table49
- GCC_except_table81
- GCC_except_table95
- __126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke
- __200-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:]_block_invoke
- __OBJC_$_CLASS_METHODS__PSEnsembleModel
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke
- ___136-[_PSHeuristics sceneBasedSuggestionsUsingEmbedding:withPredictionContext:config:useCatalog:similarityThreshold:weightedScoreThreshold:]_block_invoke
- ___200-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:]_block_invoke
- ___29-[_PSSuggesterCache _refetch]_block_invoke
- ___93-[_PSEnsembleModel _shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:]_block_invoke
- ___93-[_PSEnsembleModel _shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:]_block_invoke_2
- ___93-[_PSEnsembleModel _shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:]_block_invoke_3
- ___block_descriptor_152_e8_32s40s48s56s64s72s80r88r96r104r112r120r128r136r_e25_v32?0"NSString"8Q16^B24l
- ___block_descriptor_40_e8_32s_e38_"_PSSuggestion"16?0"_PSSuggestion"8l
- ___block_descriptor_56_e8_32s40s48s_e30_v32?0"_PSSuggestion"8Q16^B24l
- ___copy_helper_block_e8_32s40s48s56s64s72s80r88r96r104r112r120r128r136r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80r88r96r104r112r120r128r136r
- _kPSStaticContentFeatureMaxIoUOfSharesOfPeopleInPhotoWithConversationAsString
- _objc_msgSend$_shareTimeBackfillProxiesFromInteractionStatistics:afterHeuristicProxies:
- _objc_msgSend$enrichSuggestions:withStatsMap:
- _objc_msgSend$sceneBasedSuggestionsUsingEmbedding:withPredictionContext:config:useCatalog:similarityThreshold:weightedScoreThreshold:
- _objc_msgSend$suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:similarityThreshold:weightedScoreThreshold:parentSpan:
- _objc_msgSend$suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:
- _objc_msgSend$usedContactCatalogForFallback
CStrings:
+ "\n\n[Contact Info] %@"
+ "\n\n[Content] %@"
+ "\n\n[Index] %@"
+ "\n\n[Latency] %@"
+ "\n\n[Rank] %@"
+ "\n\n[Warning] Fetching photo based feature timeout"
+ "\nFullReasonTypeList: [%@]"
+ "\""
+ "%@(sim=%.3f,count=%@)"
+ "%@=%@ms"
+ "%dd"
+ "%dh"
+ "%dmin"
+ "%ds"
+ "&"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ttHUjs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ttHUjs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ttHUjs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
+ "1.2"
+ "@\"NSString\"16@?0@\"_PSSuggestionProxy\"8"
+ "Cached BoW embeddings for %lu title clusters"
+ "Currently in an active call"
+ "Currently in an active call (collaboration)"
+ "DebugUI user-mode dev dump #%lu: %{private}@"
+ "Eligible for SharePlay"
+ "Face in the photo matches this contact"
+ "Hyper-recent-opened-thread"
+ "One of your most-recently contacted"
+ "One of your most-shared-with contacts"
+ "PASSv2 candidate: %{private}@ weightedIoU=%.4f"
+ "People in the photo were shared with this contact before"
+ "Predicted from your sharing history"
+ "Recently viewed Messages thread"
+ "Similar URL title shared with this contact before"
+ "Similar photo content shared with this contact before"
+ "Suggested by a share-sheet heuristic"
+ "This contact messaged you just now"
+ "This file came from this contact"
+ "Unable to compute sentence embedding for %{private}@"
+ "YES_STATS_ONLY"
+ "You called this contact just now"
+ "You contacted this contact recently"
+ "You just opened this thread"
+ "You messaged this contact just now"
+ "You often share from this app to this contact"
+ "You often share this site with this contact"
+ "You share with this contact frequently"
+ "You've shared with this contact often"
+ "[%@]"
+ "[%@]: %@"
+ "[]"
+ "_PSDebugUIShowDevLayout"
+ "age=%ldm"
+ "catalog.totalOutgoingInteractions"
+ "catalog.totalShares"
+ "catalogConversationIdsSnapshot"
+ "catalogInventorySkippedNoStats"
+ "catalogInventoryTruncated"
+ "catalogPrivatizedIds"
+ "catalogSize"
+ "cluster_embeddings_computed"
+ "cluster_pair_evaluations"
+ "cluster_vocab_size"
+ "clusters_above_similarity_threshold"
+ "com.apple.peopleSuggester"
+ "computeClusterEmbeddings"
+ "computeClusterMaxSimToQuery"
+ "computeSimilarityScores(sentence): conversations=%lu, cluster_pair_evaluations=%lu, clusters_above_threshold=%lu, conversations_matched=%lu"
+ "contacts=%@"
+ "cosine_pairs_computed"
+ "dedupKey"
+ "end2end"
+ "engagedCandidateInCatalog"
+ "faceTagsMapped=%@"
+ "host=%@"
+ "id"
+ "inference"
+ "instrumentationVersion"
+ "interactionStore"
+ "interactionStore.databaseSize=%@MB"
+ "interactionStore.databaseSizeMB"
+ "mappedFaceTagCount"
+ "modelScoreAvailable"
+ "modelScoreUnavailableReason"
+ "peopleInPhoto=%@"
+ "photoAge=%@"
+ "photo_count=%@"
+ "preRankCandidates"
+ "preRankCandidates_truncated"
+ "privatizedId"
+ "q24@?0@\"NSDictionary\"8@\"NSDictionary\"16"
+ "query_clusters_count"
+ "sassSentenceSimilarityThreshold"
+ "scene=%@"
+ "sceneTags(MAD)=[%@]"
+ "sceneTags(Vision)=[%@]"
+ "semanticClusters=[%@]"
+ "simplifiedBackfill"
+ "suggestionProxiesFromAttachmentTags(sentence): candidate=%{private}@ query=%{private}@ score=%.4f threshold=%.3f pairs=%lu matched=[%{private}@]"
+ "suggestionProxiesFromAttachmentTags(sentence): no query embeddings, returning empty"
+ "suggestionProxiesFromAttachmentTags(sentence): query=%{private}@ tagCount=%lu"
+ "suggestionProxiesFromAttachmentTags(sentence): unable to load sentence embedding model"
+ "title=%@"
+ "titleClusters=[%@]"
+ "titleType=%@"
+ "topMappedCluster=%@"
+ "total_outgoingInteractions=%@"
+ "total_shares=%@"
+ "uiResolution"
+ "updateInteractionStatisticsForExplicitEngagement"
+ "url=%@"
+ "useBoWEmbedding"
+ "uti=%@"
+ "verified_faces=%@"
- "%@\n\nFullReasonTypeList: [%@]"
- "%@\n\nPASS heuristics might not be generated because the request for face tags to MediaAnalysisd has exceeded its allocated time budget."
- "%@\n%@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MfZnkT/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MfZnkT/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.MfZnkT/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
- "Cached Suggestion (from Contact Catalog)"
- "Cached Suggestion (from Interaction Store)"
- "Using %lu title clusters from Trial: [%{public}@]"
- "Using %lu title clusters from bundled url_clusters.json: [%{public}@]"

```
