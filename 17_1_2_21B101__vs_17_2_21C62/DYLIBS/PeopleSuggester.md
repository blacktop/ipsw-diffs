## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1852.4.2.0.3
-  __TEXT.__text: 0xe70ec
+1852.4.7.0.3
+  __TEXT.__text: 0xe6ddc
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x8ac0
-  __TEXT.__const: 0x5e0
-  __TEXT.__gcc_except_tab: 0x1bac
-  __TEXT.__cstring: 0x8e69
-  __TEXT.__oslogstring: 0xb6a1
+  __TEXT.__objc_methlist: 0x8b18
+  __TEXT.__const: 0x610
+  __TEXT.__gcc_except_tab: 0x1c7c
+  __TEXT.__cstring: 0x8eb1
+  __TEXT.__oslogstring: 0xb7df
   __TEXT.__dlopen_cstrs: 0x18da
-  __TEXT.__unwind_info: 0x2648
+  __TEXT.__unwind_info: 0x2638
   __TEXT.__objc_classname: 0x10f0
-  __TEXT.__objc_methname: 0x1f11f
+  __TEXT.__objc_methname: 0x1f0f5
   __TEXT.__objc_methtype: 0x2687
-  __TEXT.__objc_stubs: 0x12e20
+  __TEXT.__objc_stubs: 0x12ea0
   __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x25b8
+  __DATA_CONST.__const: 0x2560
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf778
-  __DATA_CONST.__objc_selrefs: 0x5b58
-  __DATA_CONST.__objc_arraydata: 0xd50
-  __AUTH_CONST.__cfstring: 0x8880
+  __DATA_CONST.__objc_const: 0xf758
+  __DATA_CONST.__objc_selrefs: 0x5b78
+  __DATA_CONST.__objc_arraydata: 0xd60
+  __AUTH_CONST.__cfstring: 0x8940
   __AUTH_CONST.__objc_intobj: 0xfd8
   __AUTH_CONST.__objc_arrayobj: 0x888
   __AUTH_CONST.__objc_const: 0x350
-  __AUTH_CONST.__const: 0x6e0
+  __AUTH_CONST.__const: 0x7a0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_doubleobj: 0xe0
-  __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x6f0
+  __DATA.__objc_classrefs: 0x6e8
   __DATA.__objc_superrefs: 0x378
-  __DATA.__objc_ivar: 0xd3c
+  __DATA.__objc_ivar: 0xd38
   __DATA.__data: 0x440
   __DATA.__bss: 0x448
-  __DATA_DIRTY.__const: 0x1000
+  __DATA_DIRTY.__const: 0xf60
   __DATA_DIRTY.__objc_const: 0x3760
   __DATA_DIRTY.__objc_data: 0x2f80
   __DATA_DIRTY.__bss: 0x8e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4434
-  Symbols:   15063
-  CStrings:  7062
+  Functions: 4442
+  Symbols:   15082
+  CStrings:  7078
 
Symbols:
+ +[_PSAppUsageUtilities boostAppsForSourceBundleId:]
+ +[_PSConstants appleNewsBundleId]
+ +[_PSConstants booksBundleId]
+ +[_PSConstants freeformBundleId]
+ +[_PSConstants journalBundleId]
+ +[_PSConstants notesBundleId]
+ +[_PSConstants remindersBundleId]
+ +[_PSFeaturePreprocessor encodeFeatureVectors:]
+ +[_PSFeaturePreprocessor oneHotEncodedFeatureNameForFeatureName:featureValue:]
+ +[_PSFeaturePreprocessor oneHotEncodedFeatureNameForFeatureName:featureValue:].cold.1
+ -[_PSClusterPoint description]
+ -[_PSCoreMLScoringModel predictWithFeatureProvider:]
+ -[_PSCoreMLScoringModel predictWithFeatureProvider:].cold.1
+ -[_PSCoreMLScoringModel predictWithFeatureProvider:].cold.2
+ -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:candidateList:error:]
+ -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:candidateList:error:].cold.1
+ -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:candidateList:error:].cold.2
+ -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:candidateList:error:].cold.3
+ -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:candidateList:error:].cold.4
+ -[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:]
+ -[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:].cold.1
+ -[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:].cold.2
+ -[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:].cold.3
+ -[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:].cold.4
+ -[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:].cold.5
+ -[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:].cold.6
+ -[_PSCoreMLScoringModel scoreCandidatesWithGBDTModel:]
+ -[_PSEnsembleModel freeCachesIfNotCoreDuetDaemon]
+ -[_PSEnsembleModel freeCaches]
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table55
+ GCC_except_table56
+ GCC_except_table58
+ GCC_except_table63
+ GCC_except_table67
+ GCC_except_table76
+ GCC_except_table79
+ GCC_except_table82
+ GCC_except_table87
+ GCC_except_table91
+ _OUTLINED_FUNCTION_11
+ ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.509
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.465
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.465.cold.1
+ ___163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke.45
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.58
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.58.cold.1
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.cold.1
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.cold.2
+ ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.148
+ ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.72
+ ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.72.cold.1
+ ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.79
+ ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.82
+ ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.82.cold.1
+ ___47+[_PSFeaturePreprocessor encodeFeatureVectors:]_block_invoke
+ ___47+[_PSFeaturePreprocessor encodeFeatureVectors:]_block_invoke_2
+ ___47+[_PSFeaturePreprocessor encodeFeatureVectors:]_block_invoke_2.cold.1
+ ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.131
+ ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.108
+ ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.120
+ ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.527
+ ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.527.cold.1
+ ___56-[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:]_block_invoke
+ ___56-[_PSCoreMLScoringModel scoreCandidatesWithCoreMLModel:]_block_invoke.148
+ ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.382
+ ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.384
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.260
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.260.cold.1
+ ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.142
+ ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.123
+ ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.154
+ ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.490
+ ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.145
+ ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.151
+ ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.228
+ ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.157
+ ___73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.267
+ ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.162
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.431
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.400
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.400.cold.1
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.406
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.417
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.424
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.424.cold.1
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.424.cold.2
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.112
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.115
+ ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.126
+ ___90-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:candidateList:error:]_block_invoke
+ ___90-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:candidateList:error:]_block_invoke_2
+ ___block_descriptor_104_e8_32s40s48s56s64s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_32_e22_16?0"_PSCandidate"8l
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e36_"NSDictionary"16?0"_PSCandidate"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e19_"NSDictionary"8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e29_v32?0"_PSCandidate"8Q16^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e43_v32?0"_PSCandidate"8"NSDictionary"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs56bs64r_e5_v8?0ls48l8s32l8s40l8r64l8s56l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e24_v32?0^v8q16"NSArray"24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.107
+ ___block_literal_global.111
+ ___block_literal_global.114
+ ___block_literal_global.119
+ ___block_literal_global.122
+ ___block_literal_global.125
+ ___block_literal_global.141
+ ___block_literal_global.143
+ ___block_literal_global.144
+ ___block_literal_global.147
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.153
+ ___block_literal_global.156
+ ___block_literal_global.211
+ ___block_literal_global.214
+ ___block_literal_global.219
+ ___block_literal_global.231
+ ___block_literal_global.235
+ ___block_literal_global.237
+ ___block_literal_global.239
+ ___block_literal_global.259
+ ___block_literal_global.264
+ ___block_literal_global.266
+ ___block_literal_global.386
+ ___block_literal_global.395
+ ___block_literal_global.44
+ ___block_literal_global.519
+ ___block_literal_global.522
+ ___block_literal_global.71
+ ___block_literal_global.81
+ ___cd_dispatch_async_capture_tx_block_invoke
+ __unnamed_array_storage.27
+ __unnamed_array_storage.28
+ __unnamed_array_storage.51
+ __unnamed_array_storage.64
+ _objc_msgSend$appleNewsBundleId
+ _objc_msgSend$booksBundleId
+ _objc_msgSend$boostAppsForSourceBundleId:
+ _objc_msgSend$encodeFeatureVectors:
+ _objc_msgSend$freeCaches
+ _objc_msgSend$freeCachesIfNotCoreDuetDaemon
+ _objc_msgSend$freeformBundleId
+ _objc_msgSend$journalBundleId
+ _objc_msgSend$notesBundleId
+ _objc_msgSend$oneHotEncodedFeatureNameForFeatureName:featureValue:
+ _objc_msgSend$predictWithFeatureProvider:
+ _objc_msgSend$reformatCandidateDictionaryIntoFeatureTensor:candidateList:error:
+ _objc_msgSend$remindersBundleId
+ _objc_msgSend$scoreCandidatesWithCoreMLModel:
+ _objc_msgSend$scoreCandidatesWithGBDTModel:
+ _objc_msgSend$setAllOtherInteractionCache:
- +[_PSFeaturePreprocessor extractFeatureValuesFromFeatureObjects:]
- +[_PSFeaturePreprocessor extractFeatureValuesFromFeatureObjects:].cold.1
- +[_PSFeaturePreprocessor extractFeatureValuesFromFeatureObjects:].cold.2
- +[_PSFeaturePreprocessor featureNameToOneHotEncodedFeatureNameGivenFeatureName:featureValue:]
- +[_PSFeaturePreprocessor getEnumBasedSuffix:featureValue:]
- +[_PSFeaturePreprocessor getStringBasedSuffix:featureValue:]
- +[_PSFeaturePreprocessor oneHotEncodedDictionaryWithCandidateToFeatureVectorDict:]
- -[_PSCoreMLScoringModel predictWithFeatureTensor:numCandidates:]
- -[_PSCoreMLScoringModel predictWithFeatureTensor:numCandidates:].cold.1
- -[_PSCoreMLScoringModel predictWithFeatureTensor:numCandidates:].cold.2
- -[_PSCoreMLScoringModel predictWithFeatureTensor:numCandidates:].cold.3
- -[_PSCoreMLScoringModel predictWithFeatureTensor:numCandidates:].cold.4
- -[_PSCoreMLScoringModel preprocessAndFetchFeatureTensor:error:]
- -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]
- -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:].cold.1
- -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:].cold.2
- -[_PSCoreMLScoringModel reformatFeatureVectorsIntoFeatureDictArray:]
- -[_PSCoreMLScoringModel scoreCandidates:predictionContext:].cold.4
- -[_PSCoreMLScoringModel scoreCandidates:predictionContext:].cold.5
- -[_PSCoreMLScoringModel scoreCandidates:predictionContext:].cold.6
- GCC_except_table52
- GCC_except_table54
- GCC_except_table57
- GCC_except_table60
- GCC_except_table71
- GCC_except_table80
- GCC_except_table83
- GCC_except_table88
- GCC_except_table92
- GCC_except_table96
- GCC_except_table98
- _OBJC_CLASS_$__PASTuple2
- _OBJC_IVAR_$__PSShareSheetEphemeralFeatureManager._histogramFeatureData
- ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.511
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.467
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.467.cold.1
- ___163+[_PSAppUsageUtilities mostUsedAppShareExtensionsWithAppBundleIdsToShareExtensionBundleIdsMapping:sourceBundleId:sharesFromSourceToTargetBundle:appUsageDurations:]_block_invoke.43
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.59
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.59.cold.1
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.61
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.61.cold.1
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.61.cold.2
- ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.149
- ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.70
- ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.70.cold.1
- ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.77
- ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.80
- ___45+[_PSAppUsageUtilities cacheSharesForEachApp]_block_invoke.80.cold.1
- ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.133
- ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.109
- ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.121
- ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.529
- ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.529.cold.1
- ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.385
- ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.387
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.261
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.261.cold.1
- ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.143
- ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.124
- ___65+[_PSFeaturePreprocessor extractFeatureValuesFromFeatureObjects:]_block_invoke
- ___65+[_PSFeaturePreprocessor extractFeatureValuesFromFeatureObjects:]_block_invoke_2
- ___66-[_PSEnsembleModel computeEphemeralFeaturesWithPredictionContext:]_block_invoke
- ___66-[_PSEnsembleModel computeEphemeralFeaturesWithPredictionContext:]_block_invoke_2
- ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.155
- ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.492
- ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.146
- ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.152
- ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.229
- ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.158
- ___73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.268
- ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.163
- ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke
- ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke.140
- ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_2
- ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_2.cold.1
- ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_3
- ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_4
- ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_4.cold.1
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.106
- ___82+[_PSFeaturePreprocessor oneHotEncodedDictionaryWithCandidateToFeatureVectorDict:]_block_invoke
- ___82+[_PSFeaturePreprocessor oneHotEncodedDictionaryWithCandidateToFeatureVectorDict:]_block_invoke_2
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.433
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.408
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.419
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.426
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.426.cold.1
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.426.cold.2
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.113
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.118
- ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.127
- ___block_descriptor_104_e8_32s40s48s56s64s72s_e24_v32?0^v8q16"NSArray"24ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_112_e8_32s40s48s56s64s72s_e43_v32?0"_PSCandidate"8"NSDictionary"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_descriptor_40_e8_32r_e42_v24?0"NSArray"8"_PSPredictionContext"16lr32l8
- ___block_descriptor_48_e8_32bs40r_e19_"NSDictionary"8?0ls32l8r40l8
- ___block_descriptor_48_e8_32s40s_e25_v32?0"NSString"816^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e43_v32?0"_PSCandidate"8"NSDictionary"16^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s_e25_v32?0"NSString"816^B24ls32l8
- ___block_descriptor_56_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
- ___block_descriptor_56_e8_32s40s_e43_v32?0"_PSCandidate"8"NSDictionary"16^B24ls32l8s40l8
- ___block_descriptor_80_e8_32s40s48s56bs64bs72r_e5_v8?0ls56l8s32l8s40l8s48l8r72l8s64l8
- ___block_literal_global.108
- ___block_literal_global.112
- ___block_literal_global.115
- ___block_literal_global.120
- ___block_literal_global.123
- ___block_literal_global.126
- ___block_literal_global.131
- ___block_literal_global.135
- ___block_literal_global.142
- ___block_literal_global.145
- ___block_literal_global.151
- ___block_literal_global.154
- ___block_literal_global.162
- ___block_literal_global.212
- ___block_literal_global.215
- ___block_literal_global.220
- ___block_literal_global.232
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.260
- ___block_literal_global.389
- ___block_literal_global.398
- ___block_literal_global.446
- ___block_literal_global.521
- ___block_literal_global.524
- ___block_literal_global.69
- __unnamed_array_storage.49
- _objc_msgSend$extractFeatureValuesFromFeatureObjects:
- _objc_msgSend$featureNameToOneHotEncodedFeatureNameGivenFeatureName:featureValue:
- _objc_msgSend$first
- _objc_msgSend$getEnumBasedSuffix:featureValue:
- _objc_msgSend$getStringBasedSuffix:featureValue:
- _objc_msgSend$hasInitializedCache
- _objc_msgSend$initWithFirst:second:
- _objc_msgSend$oneHotEncodedDictionaryWithCandidateToFeatureVectorDict:
- _objc_msgSend$predictWithFeatureTensor:numCandidates:
- _objc_msgSend$preprocessAndFetchFeatureTensor:error:
- _objc_msgSend$reformatCandidateDictionaryIntoFeatureTensor:error:
- _objc_msgSend$reformatFeatureVectorsIntoFeatureDictArray:
CStrings:
+ "\x05\x12"
+ "<_PSClusterPoint %p> timestampExists=%d timestamp=%@ (%@:%@:%@ weekday=%ld) x=%f y=%f"
+ "@\"NSDictionary\"16@?0@\"_PSCandidate\"8"
+ "Copying feature vectors into feature tensor"
+ "Encoding feature dictionary"
+ "Feature %@ unexpectedly produced a nil value"
+ "Feature name %@ produced one-hot feature name %@"
+ "Feature value %@ produced encoded value %@ for candidate %{private}@"
+ "Fetched %tu cached suggestions: %{private}@"
+ "Finished encoding feature dictionary"
+ "Found %d candidates with an empty feature dictionary"
+ "Freeing caches now to save memory"
+ "Missing candidates per feature %{private}@"
+ "Missing features per candidate %{private}@"
+ "Not freeing caches because we're coreduetd"
+ "Pointer %p out of range %p - %p (featureName=%{public}@, featureIdx=%tu, colStride=%tu)"
+ "Rank default (Journal > Reminders) apps for source bundleId: %@"
+ "Rank default (Reminders > Journal) apps for source bundleId: %@"
+ "Requesting candidates over XPC"
+ "Top candidates are: %{private}@, remaining candidates are: %{private}@"
+ "_PSCandidateScoringCoreMLModel - People Suggester run inference with the GBDT model"
+ "_PSCandidateScoringCoreMLModel - candidateToFeatureVectorDict was missing or empty"
+ "_PSCandidateScoringCoreMLModel - model was missing"
+ "_PSCandidateScoringGBDTModel-Inference"
+ "appleNewsBundleId"
+ "booksBundleId"
+ "boostAppsForSourceBundleId:"
+ "cd_dispatch_async_tx"
+ "com.apple.freeform"
+ "com.apple.iBooks"
+ "com.apple.journal"
+ "com.apple.mobilenotes"
+ "com.apple.news"
+ "com.apple.reminders"
+ "encodeFeatureVectors:"
+ "freeCaches"
+ "freeCachesIfNotCoreDuetDaemon"
+ "freeformBundleId"
+ "journalBundleId"
+ "notesBundleId"
+ "oneHotEncodedFeatureNameForFeatureName:featureValue:"
+ "predictWithFeatureProvider:"
+ "reformatCandidateDictionaryIntoFeatureTensor:candidateList:error:"
+ "remindersBundleId"
+ "scoreCandidatesWithCoreMLModel:"
+ "scoreCandidatesWithGBDTModel:"
+ "v32@?0@\"_PSCandidate\"8Q16^B24"
- "\x06\x12"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/FeatureManager/_PSFeatureCache.m:582"
- "Extracting feature values from feature object"
- "Fetched fallback suggestion in coreduetd: %{private}@"
- "Fetching cached people suggestions: %{private}@"
- "Finished extracting feature values from feature object"
- "Finished one hot encoding features"
- "No cache available, fetching fallbacks in coreduetd"
- "One hot encoding features"
- "PASSv2 feature flag is on"
- "Top candidates are: %{sensitive}@, remaining candidates are: %{sensitive}@"
- "_PSCandidateScoringCoreMLModel - People Suggester run inference with the model"
- "_PSCandidateScoringCoreMLModel - candidateToFeatureVectorDict (%{public}@) was missing or empty"
- "_PSCandidateScoringCoreMLModel - mode was missing"
- "candidateToFeatureVectorDictFetchBlock"
- "com.apple.pstestframework"
- "extractFeatureValuesFromFeatureObjects:"
- "featureName not recognized (or featureValue is nil): excluding case-insensitive matches=%{public}@, all=%{public}@"
- "featureNameToOneHotEncodedFeatureNameGivenFeatureName:featureValue:"
- "first"
- "getEnumBasedSuffix:featureValue:"
- "getStringBasedSuffix:featureValue:"
- "initWithFirst:second:"
- "missingFeaturesLogQueue"
- "no feature %@ for candidate %lu"
- "oneHotEncodedDictionaryWithCandidateToFeatureVectorDict:"
- "pass_v2"
- "predictWithFeatureTensor:numCandidates:"
- "preprocessAndFetchFeatureTensor:error:"
- "reformatCandidateDictionaryIntoFeatureTensor:error:"
- "reformatFeatureVectorsIntoFeatureDictArray:"

```
