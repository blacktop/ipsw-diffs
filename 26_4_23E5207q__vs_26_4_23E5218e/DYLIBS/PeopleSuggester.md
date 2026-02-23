## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1933.8.0.0.0
-  __TEXT.__text: 0x10659c
+1933.10.0.0.0
+  __TEXT.__text: 0x1081c8
   __TEXT.__auth_stubs: 0xf60
-  __TEXT.__objc_methlist: 0xa1c4
+  __TEXT.__objc_methlist: 0xa224
   __TEXT.__const: 0x8d0
   __TEXT.__gcc_except_tab: 0x2f84
-  __TEXT.__cstring: 0xc069
-  __TEXT.__oslogstring: 0xc8d1
+  __TEXT.__cstring: 0xc245
+  __TEXT.__oslogstring: 0xcafe
   __TEXT.__dlopen_cstrs: 0x189d
   __TEXT.__ustring: 0x33e
-  __TEXT.__unwind_info: 0x31a0
+  __TEXT.__unwind_info: 0x31c0
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x12b5
-  __TEXT.__objc_methname: 0x22d0f
-  __TEXT.__objc_methtype: 0x27c9
-  __TEXT.__objc_stubs: 0x13a60
-  __DATA_CONST.__got: 0x970
-  __DATA_CONST.__const: 0x38f8
+  __TEXT.__objc_methname: 0x23018
+  __TEXT.__objc_methtype: 0x283b
+  __TEXT.__objc_stubs: 0x13bc0
+  __DATA_CONST.__got: 0x9a8
+  __DATA_CONST.__const: 0x3970
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6848
+  __DATA_CONST.__objc_selrefs: 0x68b0
   __DATA_CONST.__objc_superrefs: 0x3d8
   __DATA_CONST.__objc_arraydata: 0xd88
   __AUTH_CONST.__auth_got: 0x7c0
   __AUTH_CONST.__const: 0x1a80
-  __AUTH_CONST.__cfstring: 0xe5c0
-  __AUTH_CONST.__objc_const: 0x14488
+  __AUTH_CONST.__cfstring: 0xe7c0
+  __AUTH_CONST.__objc_const: 0x144e8
   __AUTH_CONST.__objc_intobj: 0x1140
   __AUTH_CONST.__objc_arrayobj: 0x828
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0xc80
-  __DATA.__objc_ivar: 0xdf0
+  __DATA.__objc_ivar: 0xdf8
   __DATA.__data: 0x4f0
-  __DATA.__bss: 0x678
+  __DATA.__bss: 0x680
   __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__bss: 0x8b0
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 40EEAFC5-C7A2-3E56-B3F6-9D3B177D092F
-  Functions: 4812
-  Symbols:   16973
-  CStrings:  10184
+  UUID: 987D0D3E-3350-36D5-9064-FB34B04EDF7E
+  Functions: 4825
+  Symbols:   17026
+  CStrings:  10247
 
Symbols:
+ -[PSInteractionAnalyzer generateContactSummariesWithMaxInteractions:lookbackPeriodInMonths:]
+ -[PSInteractionAnalyzer generateContactSummariesWithMaxInteractions:lookbackPeriodInMonths:].cold.1
+ -[_PSAttachment contentKeywords]
+ -[_PSAttachment contentTitle]
+ -[_PSAttachment initWithCreationDate:UTI:photoLocalIdentifier:identifier:cloudIdentifier:contentURL:contentText:imageData:photoLocalIdentifiers:suggestedContactIdentifiers:photoSceneDescriptors:peopleInPhoto:contentTitle:contentKeywords:]
+ -[_PSAttachment setContentKeywords:]
+ -[_PSAttachment setContentTitle:]
+ -[_PSContactCatalog generateContactCatalog:maxInteractions:lookbackPeriodInMonths:updateCatalog:]
+ -[_PSContactCatalog generateContactCatalog:maxInteractions:lookbackPeriodInMonths:updateCatalog:].cold.1
+ -[_PSHeuristics buildEnhancedReasonWithBaseReason:contextDetails:useCatalog:conversationId:interactionStatistics:]
+ -[_PSHeuristics embeddingBasedTitleSuggestionProxiesForInteractionStatistics:withPredictionContext:useCatalog:]
+ -[_PSHeuristics embeddingBasedURLSuggestionProxiesForInteractionStatistics:withPredictionContext:useCatalog:]
+ -[_PSHeuristics extractMeaningfulWordsFromText:]
+ -[_PSHeuristics mapTitleToSceneClusters:interactionStatistics:threshold:topK:]
+ -[_PSHeuristics mapTitleToSceneClusters:interactionStatistics:threshold:topK:].cold.1
+ -[_PSHeuristics peopleAwareSuggestionProxiesForInteractionStatistics:withPersonIdentifiers:useCatalog:]
+ -[_PSHeuristics sceneBasedSuggestionsUsingEmbedding:withPredictionContext:config:useCatalog:]
+ -[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:]
+ GCC_except_table35
+ GCC_except_table75
+ GCC_except_table83
+ GCC_except_table88
+ _NLTagNoun
+ _NLTagOrganizationName
+ _NLTagPersonalName
+ _NLTagPlaceName
+ _NLTagSchemeLexicalClass
+ _NLTagSchemeNameType
+ _OBJC_CLASS_$_NLTagger
+ _OBJC_IVAR_$__PSAttachment._contentKeywords
+ _OBJC_IVAR_$__PSAttachment._contentTitle
+ _SuggestionProxyTypeTitleASS
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.429
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.431
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.902
+ ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.903
+ ___118-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:]_block_invoke.987
+ ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.795
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.713
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.713.cold.1
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke_2.357
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke_4
+ ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke_4.cold.1
+ ___146-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:]_block_invoke
+ ___146-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:]_block_invoke.256
+ ___146-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:]_block_invoke_2
+ ___48-[_PSHeuristics extractMeaningfulWordsFromText:]_block_invoke
+ ___48-[_PSHeuristics extractMeaningfulWordsFromText:]_block_invoke_2
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.891
+ ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.891.cold.1
+ ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.766
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.425
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.431
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.434
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.449
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.455
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.462
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.459
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.628
+ ___91-[_PSEnsembleModel _conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:]_block_invoke.960
+ ___93-[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]_block_invoke.474
+ ___Block_byref_object_copy_.359
+ ___Block_byref_object_dispose_.360
+ ___block_descriptor_36_e5_v8?0l
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_56_e8_32s40s48s_e37_v40?0"NSString"8{_NSRange=QQ}16^B32ls32l8s40l8s48l8
+ ___block_descriptor_77_e8_32s40s48s56s64s_e41_"_PSSuggestionProxy"24?0"NSString"8Q16ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e17_v20?0B8?<v?>12lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.299
+ ___block_literal_global.301
+ ___block_literal_global.428
+ ___block_literal_global.433
+ ___block_literal_global.450
+ ___block_literal_global.452
+ ___block_literal_global.458
+ ___block_literal_global.461
+ ___block_literal_global.464
+ ___block_literal_global.470
+ ___block_literal_global.476
+ ___block_literal_global.566
+ ___block_literal_global.611
+ ___block_literal_global.642
+ ___block_literal_global.704
+ ___block_literal_global.814
+ ___block_literal_global.884
+ ___block_literal_global.989
+ __recordFeedbackToInteractionStoreWithFeedback:mechanism:.feedbackXPCInProgress
+ _objc_msgSend$buildEnhancedReasonWithBaseReason:contextDetails:useCatalog:conversationId:interactionStatistics:
+ _objc_msgSend$contentKeywords
+ _objc_msgSend$contentTitle
+ _objc_msgSend$embeddingBasedTitleSuggestionProxiesForInteractionStatistics:withPredictionContext:useCatalog:
+ _objc_msgSend$embeddingBasedURLSuggestionProxiesForInteractionStatistics:withPredictionContext:useCatalog:
+ _objc_msgSend$enumerateTagsInRange:unit:scheme:options:usingBlock:
+ _objc_msgSend$extractMeaningfulWordsFromText:
+ _objc_msgSend$generateContactCatalog:maxInteractions:lookbackPeriodInMonths:updateCatalog:
+ _objc_msgSend$generateContactSummariesWithMaxInteractions:lookbackPeriodInMonths:
+ _objc_msgSend$initWithCreationDate:UTI:photoLocalIdentifier:identifier:cloudIdentifier:contentURL:contentText:imageData:photoLocalIdentifiers:suggestedContactIdentifiers:photoSceneDescriptors:peopleInPhoto:contentTitle:contentKeywords:
+ _objc_msgSend$initWithIdentifier:cloudIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:
+ _objc_msgSend$initWithTagSchemes:
+ _objc_msgSend$iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:
+ _objc_msgSend$mapTitleToSceneClusters:interactionStatistics:threshold:topK:
+ _objc_msgSend$originalURL
+ _objc_msgSend$peopleAwareSuggestionProxiesForInteractionStatistics:withPersonIdentifiers:useCatalog:
+ _objc_msgSend$sceneBasedSuggestionsUsingEmbedding:withPredictionContext:config:useCatalog:
+ _objc_msgSend$setContentKeywords:
+ _objc_msgSend$setContentTitle:
+ _objc_msgSend$setPhotoSceneDescriptor:
+ _objc_msgSend$suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:
- -[PSInteractionAnalyzer generateContactSummariesWithMaxInteractions:]
- -[PSInteractionAnalyzer generateContactSummariesWithMaxInteractions:].cold.1
- -[_PSAttachment initWithCreationDate:UTI:photoLocalIdentifier:identifier:cloudIdentifier:contentURL:contentText:imageData:photoLocalIdentifiers:suggestedContactIdentifiers:photoSceneDescriptors:peopleInPhoto:]
- -[_PSContactCatalog generateContactCatalog:maxInteractions:updateCatalog:]
- -[_PSContactCatalog generateContactCatalog:maxInteractions:updateCatalog:].cold.1
- -[_PSHeuristics embeddingBasedURLSuggestionProxiesForInteractionStatistics:withPredictionContext:]
- -[_PSHeuristics peopleAwareSuggestionProxiesForInteractionStatistics:]
- -[_PSHeuristics sceneBasedSuggestionsUsingEmbedding:withPredictionContext:]
- -[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:]
- GCC_except_table33
- GCC_except_table69
- ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.426
- ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.428
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.899
- ___105-[_PSEnsembleModel getSuggestionsFromInteractionsStatistics:withConfig:trialClient:andPredictionContext:]_block_invoke.900
- ___118-[_PSEnsembleModel psrDataCollectionForContext:timeToWaitInSeconds:interactionStatisticsConfig:interactionStatistics:]_block_invoke.984
- ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.792
- ___120-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:]_block_invoke
- ___120-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:]_block_invoke.234
- ___120-[_PSHeuristics suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:]_block_invoke_2
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.710
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.710.cold.1
- ___133+[_PSPhotoSuggestions sceneTagsInSharedPhotoAttachments:forBundleID:shouldProcessPicturesLive:withTraceID:withSpanID:withCompletion:]_block_invoke_3.cold.1
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.888
- ___50-[_PSEnsembleModel evaluateCandidates:psrMLModel:]_block_invoke.888.cold.1
- ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.763
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.386
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.392
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.395
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.410
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.416
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.423
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.420
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.625
- ___91-[_PSEnsembleModel _conversationIdForFirstInteractionAfterSharingStartDate:targetBundleId:]_block_invoke.957
- ___93-[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]_block_invoke.471
- ___Block_byref_object_copy_.357
- ___Block_byref_object_dispose_.358
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_88_e8_32s40s48s56s64s72bs80r_e8_v12?0B8lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.293
- ___block_literal_global.389
- ___block_literal_global.394
- ___block_literal_global.397
- ___block_literal_global.413
- ___block_literal_global.419
- ___block_literal_global.422
- ___block_literal_global.425
- ___block_literal_global.444
- ___block_literal_global.467
- ___block_literal_global.473
- ___block_literal_global.563
- ___block_literal_global.608
- ___block_literal_global.639
- ___block_literal_global.701
- ___block_literal_global.802
- ___block_literal_global.881
- ___block_literal_global.986
- _objc_msgSend$embeddingBasedURLSuggestionProxiesForInteractionStatistics:withPredictionContext:
- _objc_msgSend$generateContactCatalog:maxInteractions:updateCatalog:
- _objc_msgSend$generateContactSummariesWithMaxInteractions:
- _objc_msgSend$initWithCreationDate:UTI:photoLocalIdentifier:identifier:cloudIdentifier:contentURL:contentText:imageData:
- _objc_msgSend$initWithCreationDate:UTI:photoLocalIdentifier:identifier:cloudIdentifier:contentURL:contentText:imageData:photoLocalIdentifiers:suggestedContactIdentifiers:
- _objc_msgSend$initWithCreationDate:UTI:photoLocalIdentifier:identifier:cloudIdentifier:contentURL:contentText:imageData:photoLocalIdentifiers:suggestedContactIdentifiers:photoSceneDescriptors:peopleInPhoto:
- _objc_msgSend$initWithIdentifier:cloudIdentifier:photoLocalIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:photoSceneDescriptor:personInPhoto:
- _objc_msgSend$peopleAwareSuggestionProxiesForInteractionStatistics:
- _objc_msgSend$sceneBasedSuggestionsUsingEmbedding:withPredictionContext:
- _objc_msgSend$suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:
CStrings:
+ "\n\nCandidate: Sharing Content Pattern: [%@]"
+ "\n\nContext: %@"
+ "\n\nUseCatalog: %@"
+ "\nClustered tags:%@"
+ "\nRaw tags:%@"
+ "\nTitle:%@\nMapped clusters:[%@]"
+ "\nTitle:%@\nMeaningful words:[%@]\nMapped clusters:[%@]"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
+ "/Library/Caches/com.apple.xbs/CC3AE46D-3239-4BA4-99A7-585F4CA34FFC/TemporaryDirectory.Ckcfzg/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
+ "@128@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120"
+ "@32@0:8q16q24"
+ "@44@0:8@16q24q32B40"
+ "@48@0:8@16@24d32Q40"
+ "@52@0:8@16@24B32@36@44"
+ "Not reporting feedback due to backlog"
+ "Reason: TitleAware Heuristic\n\nDescription: Similar title has been shared to this contact(s) in the past"
+ "SuggestionProxyTypeTitleASS"
+ "T@\"NSArray\",C,N,V_contentKeywords"
+ "T@\"NSString\",C,N,V_contentTitle"
+ "TitleAware"
+ "TitleAware: Enriched attachment with title: %{private}@ and %lu keywords"
+ "TitleAware: Failed to compute embedding for title: %{private}@"
+ "TitleAware: Mapped cluster '%@' with similarity %.3f"
+ "TitleAware: Mapping title to %lu scene clusters with threshold %.2f"
+ "TitleAware: No scene clusters available (neither from dict nor history)"
+ "TitleAware: No scene clusters matched for title: %{private}@ (threshold: %.2f, topK: %lu)"
+ "TitleAware: Scene cluster dict unavailable, falling back to conversation history"
+ "Using predicate %@"
+ "_contentKeywords"
+ "_contentTitle"
+ "buildEnhancedReasonWithBaseReason:contextDetails:useCatalog:conversationId:interactionStatistics:"
+ "cluster"
+ "clusterMappingThreshold"
+ "clusterMappingTopK"
+ "contentKeywords"
+ "contentTitle"
+ "embeddingBasedTitleSuggestionProxiesForInteractionStatistics:withPredictionContext:useCatalog:"
+ "embeddingBasedURLSuggestionProxiesForInteractionStatistics:withPredictionContext:useCatalog:"
+ "enumerateTagsInRange:unit:scheme:options:usingBlock:"
+ "extractMeaningfulWordsFromText:"
+ "generateContactCatalog:maxInteractions:lookbackPeriodInMonths:updateCatalog:"
+ "generateContactSummariesWithMaxInteractions:lookbackPeriodInMonths:"
+ "initWithCreationDate:UTI:photoLocalIdentifier:identifier:cloudIdentifier:contentURL:contentText:imageData:photoLocalIdentifiers:suggestedContactIdentifiers:photoSceneDescriptors:peopleInPhoto:contentTitle:contentKeywords:"
+ "initWithIdentifier:cloudIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:"
+ "initWithTagSchemes:"
+ "iterInteractionRecordsWithPredicate:fetchLimit:sortAscending:preemptBackgroundWork:updateTelemetry:withBlock:"
+ "mapTitleToSceneClusters:interactionStatistics:threshold:topK:"
+ "originalURL"
+ "peopleAwareSuggestionProxiesForInteractionStatistics:withPersonIdentifiers:useCatalog:"
+ "sceneBasedSuggestionsUsingEmbedding:withPredictionContext:config:useCatalog:"
+ "setContentKeywords:"
+ "setContentTitle:"
+ "setPhotoSceneDescriptor:"
+ "suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:contextDetails:useCatalog:"
+ "url:%@"
+ "v20@?0B8@?<v@?>12"
+ "v40@?0@\"NSString\"8{_NSRange=QQ}16^B32"
- "\f"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/AppExtensionPredictions/_PSAppUsageUtilities.m"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/Modeling/CloudFamily/_PSFamilyRecommender.m"
- "/Library/Caches/com.apple.xbs/91C81079-7029-4095-A170-4FDA4D8C53C6/TemporaryDirectory.dbGEUd/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/_PSSuggestion.m"
- "@36@0:8@16q24B32"
- "embeddingBasedURLSuggestionProxiesForInteractionStatistics:withPredictionContext:"
- "generateContactCatalog:maxInteractions:updateCatalog:"
- "generateContactSummariesWithMaxInteractions:"
- "initWithCreationDate:UTI:photoLocalIdentifier:identifier:cloudIdentifier:contentURL:contentText:imageData:photoLocalIdentifiers:suggestedContactIdentifiers:photoSceneDescriptors:peopleInPhoto:"
- "initWithIdentifier:cloudIdentifier:photoLocalIdentifier:type:sizeInBytes:creationDate:contentURL:contentText:photoSceneDescriptor:personInPhoto:"
- "peopleAwareSuggestionProxiesForInteractionStatistics:"
- "sceneBasedSuggestionsUsingEmbedding:withPredictionContext:"
- "suggestionProxiesFromAttachmentTags:interactionStatistics:suggestionProxyType:reasonMessage:reasonType:"

```
