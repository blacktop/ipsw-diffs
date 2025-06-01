## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1852.0.1.2.0
-  __TEXT.__text: 0xe5180
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_methlist: 0x8a78
-  __TEXT.__const: 0x5d0
-  __TEXT.__gcc_except_tab: 0x1af8
-  __TEXT.__cstring: 0x8e53
-  __TEXT.__oslogstring: 0xb59f
+1852.4.2.0.3
+  __TEXT.__text: 0xe70ec
+  __TEXT.__auth_stubs: 0xd80
+  __TEXT.__objc_methlist: 0x8ac0
+  __TEXT.__const: 0x5e0
+  __TEXT.__gcc_except_tab: 0x1bac
+  __TEXT.__cstring: 0x8e69
+  __TEXT.__oslogstring: 0xb6a1
   __TEXT.__dlopen_cstrs: 0x18da
-  __TEXT.__unwind_info: 0x25e0
-  __TEXT.__objc_classname: 0x10e6
-  __TEXT.__objc_methname: 0x1ef77
-  __TEXT.__objc_methtype: 0x2647
-  __TEXT.__objc_stubs: 0x12c20
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x24a8
-  __DATA_CONST.__objc_classlist: 0x4c0
+  __TEXT.__unwind_info: 0x2648
+  __TEXT.__objc_classname: 0x10f0
+  __TEXT.__objc_methname: 0x1f11f
+  __TEXT.__objc_methtype: 0x2687
+  __TEXT.__objc_stubs: 0x12e20
+  __DATA_CONST.__got: 0xd0
+  __DATA_CONST.__const: 0x25b8
+  __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf740
-  __DATA_CONST.__objc_selrefs: 0x5ac8
-  __DATA_CONST.__objc_arraydata: 0xd28
-  __AUTH_CONST.__cfstring: 0x8840
-  __AUTH_CONST.__objc_intobj: 0xf60
-  __AUTH_CONST.__objc_arrayobj: 0x870
-  __AUTH_CONST.__objc_const: 0x308
+  __DATA_CONST.__objc_const: 0xf778
+  __DATA_CONST.__objc_selrefs: 0x5b58
+  __DATA_CONST.__objc_arraydata: 0xd50
+  __AUTH_CONST.__cfstring: 0x8880
+  __AUTH_CONST.__objc_intobj: 0xfd8
+  __AUTH_CONST.__objc_arrayobj: 0x888
+  __AUTH_CONST.__objc_const: 0x350
   __AUTH_CONST.__const: 0x6e0
-  __AUTH_CONST.__objc_doubleobj: 0xb0
-  __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x660
-  __DATA.__objc_classrefs: 0x6d0
+  __AUTH_CONST.__objc_doubleobj: 0xe0
+  __AUTH_CONST.__objc_dictobj: 0xa0
+  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_classrefs: 0x6f0
   __DATA.__objc_superrefs: 0x378
   __DATA.__objc_ivar: 0xd3c
   __DATA.__data: 0x440
-  __DATA.__bss: 0x3b8
-  __DATA_DIRTY.__const: 0xf20
+  __DATA.__bss: 0x448
+  __DATA_DIRTY.__const: 0x1000
   __DATA_DIRTY.__objc_const: 0x3760
   __DATA_DIRTY.__objc_data: 0x2f80
-  __DATA_DIRTY.__bss: 0x8e0
+  __DATA_DIRTY.__bss: 0x8e8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0634D3B1-E416-3F1D-A2C5-EEB9288131F0
-  Functions: 4390
-  Symbols:   14900
-  CStrings:  8121
+  UUID: 30C7A65B-0D68-3417-A6F8-665DB474D9EC
+  Functions: 4434
+  Symbols:   15063
+  CStrings:  8154
 
Symbols:
+ +[_PSConfig _configs]
+ +[_PSConfig _loadPlistNamed:]
+ +[_PSConfig _loadPlistNamed:].cold.1
+ +[_PSConfig _loadPlistNamed:].cold.2
+ +[_PSConfig _loadPlistNamed:].cold.3
+ +[_PSConfig contactEmbeddingConfig]
+ +[_PSConfig defaultConfig]
+ +[_PSConfig messagesPinningConfig]
+ +[_PSConfig vocab]
+ +[_PSFeaturePreprocessor extractFeatureValuesFromFeatureObjects:].cold.1
+ +[_PSFeaturePreprocessor extractFeatureValuesFromFeatureObjects:].cold.2
+ +[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:]
+ +[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:].cold.1
+ +[_PSPhotoUtils prewarmPhotosFrameworks]
+ -[_PSCandidate candidateForDeduping]
+ -[_PSCandidate populateIsSystemBundleId]
+ -[_PSCoreMLScoringModel batchPredictWithFeatureDictArray:].cold.4
+ -[_PSCoreMLScoringModel featureOrderFromMetadata]
+ -[_PSCoreMLScoringModel featureOrderFromMetadata].cold.1
+ -[_PSCoreMLScoringModel featureOrderFromMetadata].cold.2
+ -[_PSCoreMLScoringModel getSuggestionProxiesForCandidateToFeatureVectorDictGetter:predictionContext:messageInteractionCache:shareInteractionCache:]
+ -[_PSCoreMLScoringModel mlModelInitialized]
+ -[_PSCoreMLScoringModel preprocessAndFetchFeatureTensor:error:]
+ -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]
+ -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:].cold.1
+ -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:].cold.2
+ -[_PSCoreMLScoringModel scoreCandidates:predictionContext:].cold.3
+ -[_PSCoreMLScoringModel scoreCandidates:predictionContext:].cold.4
+ -[_PSCoreMLScoringModel scoreCandidates:predictionContext:].cold.5
+ -[_PSCoreMLScoringModel scoreCandidates:predictionContext:].cold.6
+ -[_PSCoreMLScoringModel setMlModelInitialized:]
+ -[_PSEnsembleModel getCoreMLSuggestionProxiesWithPredictionContext:modelSuggestionProxiesDict:candidateToFeatureVectorDictGetter:]
+ -[_PSEnsembleModel getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:]
+ -[_PSEnsembleModel getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:].cold.1
+ -[_PSEnsembleModel getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:].cold.2
+ -[_PSEnsembleModel getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:].cold.3
+ -[_PSEnsembleModel getModelSuggestionsProxyDictWithModelProxiesArray:].cold.1
+ -[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]
+ -[_PSEnsembleModel loadPSConfigPath:]
+ -[_PSEnsembleModel loadPSConfigPath:].cold.1
+ -[_PSFeatureCache setFeatureValueForFeatureName:featureValue:candidate:bundleID:]
+ -[_PSFeatureCache setFeatureValueForFeatureName:featureValue:candidate:bundleID:].cold.1
+ -[_PSFeatureCache setFeatureValueForFeatureName:featureValue:candidate:bundleID:].cold.2
+ -[_PSFeatureDictionary _removeObjectForKey:]
+ -[_PSFeatureDictionary _setPlistValue:inTimeBucket:forKey:]
+ -[_PSFeatureDictionary _unoptimizedValuesCreateIfNeeded]
+ -[_PSFeatureDictionary addEntriesFromDictionary:]
+ -[_PSFeatureDictionary addFeatureWithIntValue:doubleValue:stringValue:boolValue:timeBucket:forKey:]
+ -[_PSKNNModel suggestionProxiesBasedOnSharingInteractionsWithPredictionContext:withOnlyTopShares:withFilterOutNonMatchingSourceBundleIDs:].cold.1
+ -[_PSKNNModel suggestionProxiesWithPredictionContext:].cold.1
+ -[_PSMessagesPinningSuggester loadPSConfig]
+ -[_PSSuggester getCacheSuggestionsWithPredictionContext:].cold.1
+ -[_PSSuggesterCache backgroundRefetch]
+ GCC_except_table22
+ GCC_except_table24
+ GCC_except_table53
+ GCC_except_table57
+ GCC_except_table59
+ GCC_except_table64
+ GCC_except_table68
+ GCC_except_table70
+ GCC_except_table71
+ GCC_except_table73
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table80
+ GCC_except_table83
+ GCC_except_table92
+ GCC_except_table96
+ GCC_except_table98
+ OBJC_IVAR_$__PSFeatureDictionary._unoptimizedValues
+ _CFNumberGetValue
+ _CFStringLowercase
+ _NSMallocException
+ _OBJC_CLASS_$_LSApplicationExtensionRecord
+ _OBJC_CLASS_$_LSExtensionPointRecord
+ _OBJC_CLASS_$__PASDeviceState
+ _OBJC_CLASS_$__PASLazyPlistWithBPlistSupport
+ _OBJC_CLASS_$__PSConfig
+ _OBJC_IVAR_$__PSCandidate._isSystemBundleId
+ _OBJC_IVAR_$__PSCoreMLScoringModel._mlModelInitialized
+ _OBJC_METACLASS_$__PSConfig
+ __OBJC_$_CLASS_METHODS__PSConfig
+ __OBJC_CLASS_RO_$__PSConfig
+ __OBJC_METACLASS_RO_$__PSConfig
+ __PASEvaluateLogFaultAndProbCrashCriteria
+ __PSMapsContactKeysToFetch.cold.5
+ __PSShareSheetSuggestionBundleIDMapping.lock
+ __PSShareSheetSuggestionBundleIDMapping.onceToken
+ __PSShareSheetSuggestionBundleIDMapping.queue
+ ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.511
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.467
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.467.cold.1
+ ___147-[_PSCoreMLScoringModel getSuggestionProxiesForCandidateToFeatureVectorDictGetter:predictionContext:messageInteractionCache:shareInteractionCache:]_block_invoke
+ ___21+[_PSConfig _configs]_block_invoke
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.59
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.59.cold.1
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.61
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.61.cold.1
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.61.cold.2
+ ___38-[_PSSuggesterCache backgroundRefetch]_block_invoke
+ ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.149
+ ___40+[_PSPhotoUtils prewarmPhotosFrameworks]_block_invoke
+ ___40+[_PSPhotoUtils prewarmPhotosFrameworks]_block_invoke_2
+ ___40+[_PSPhotoUtils prewarmPhotosFrameworks]_block_invoke_3
+ ___44-[_PSFeatureDictionary _removeObjectForKey:]_block_invoke
+ ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.132
+ ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.133
+ ___49-[_PSCoreMLScoringModel featureOrderFromMetadata]_block_invoke
+ ___49-[_PSFeatureDictionary addEntriesFromDictionary:]_block_invoke
+ ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.109
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.25
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.29
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_2.31
+ ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.121
+ ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.529
+ ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.529.cold.1
+ ___57-[_PSSuggester getCacheSuggestionsWithPredictionContext:]_block_invoke
+ ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke
+ ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.385
+ ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke.387
+ ___59-[_PSEnsembleModel getPhotoBasedFeaturesAsync:withTimeout:]_block_invoke_2
+ ___61-[_PSMessagesPinningSuggester submitMessagesPinningFeedback:]_block_invoke.104
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.261
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.261.cold.1
+ ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.143
+ ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.124
+ ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.155
+ ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.492
+ ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.146
+ ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.152
+ ___70-[_PSEnsembleModel validateCoreMLModelWithRawInput:predictionContext:]_block_invoke
+ ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.229
+ ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.158
+ ___73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.268
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.287
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.292
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.310
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.316
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.320
+ ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.163
+ ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke
+ ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke.140
+ ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_2
+ ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_2.cold.1
+ ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_3
+ ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_4
+ ___76-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:error:]_block_invoke_4.cold.1
+ ___77-[_PSMessagesPinningSuggester chatGuidsForMessagesPinningWithMaxSuggestions:]_block_invoke.44
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.104
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.105
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.106
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.96
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.433
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.408
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.419
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.426
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.426.cold.1
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.426.cold.2
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.113
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.116
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.117
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.118
+ ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.127
+ ___99-[_PSKNNModel rankedCoRecipientSuggestionsWithPredictionContext:modelConfiguration:maxSuggestions:]_block_invoke.174
+ ___Block_byref_object_copy_.94
+ ___Block_byref_object_dispose_.95
+ ____PSShareSheetSuggestionBundleIDMapping_block_invoke.29
+ ____PSShareSheetSuggestionBundleIDMapping_block_invoke_2
+ ____PSShareSheetSuggestionBundleIDMapping_block_invoke_3
+ ____uncachedPSShareSheetSuggestionBundleIDMapping_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s_e24_v32?0^v8q16"NSArray"24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s_e25_v32?0"NSString"8Q16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_112_e8_32s40s48s56s64s72s_e43_v32?0"_PSCandidate"8"NSDictionary"16^B24ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_32_e36_"_PSCandidate"16?0"_PSCandidate"8l
+ ___block_descriptor_33_e29_v16?0"NSMutableDictionary"8l
+ ___block_descriptor_33_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e38_B16?0"LSApplicationExtensionRecord"8ls32l8
+ ___block_descriptor_41_e8_32r_e29_v16?0"NSMutableDictionary"8lr32l8
+ ___block_descriptor_48_e8_32bs40r_e19_"NSDictionary"8?0ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e22_B16?0"BMStoreEvent"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e32_"NSString"16?0"_PSCandidate"8ls32l8s40l8
+ ___block_descriptor_56_e8_32s40r48w_e5_v8?0lw48l8r40l8s32l8
+ ___block_descriptor_56_e8_32s40s_e25_v32?0"NSString"816^B24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e43_v32?0"_PSCandidate"8"NSDictionary"16^B24ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56bs64r_e5_v8?0ls32l8s56l8r64l8s40l8s48l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80s88s_e22_v16?0"BMStoreEvent"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.103
+ ___block_literal_global.112
+ ___block_literal_global.115
+ ___block_literal_global.120
+ ___block_literal_global.123
+ ___block_literal_global.126
+ ___block_literal_global.142
+ ___block_literal_global.145
+ ___block_literal_global.148
+ ___block_literal_global.151
+ ___block_literal_global.154
+ ___block_literal_global.157
+ ___block_literal_global.161
+ ___block_literal_global.162
+ ___block_literal_global.165
+ ___block_literal_global.212
+ ___block_literal_global.215
+ ___block_literal_global.220
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.260
+ ___block_literal_global.280
+ ___block_literal_global.285
+ ___block_literal_global.287
+ ___block_literal_global.290
+ ___block_literal_global.297
+ ___block_literal_global.313
+ ___block_literal_global.314
+ ___block_literal_global.319
+ ___block_literal_global.322
+ ___block_literal_global.34
+ ___block_literal_global.389
+ ___block_literal_global.398
+ ___block_literal_global.446
+ ___block_literal_global.521
+ ___block_literal_global.524
+ ___block_literal_global.91
+ ___block_literal_global.97
+ ___getCNContactPostalAddressesKeySymbolLoc_block_invoke
+ ___internedValues_block_invoke
+ __configs.configs
+ __configs.onceToken
+ __uncachedPSShareSheetSuggestionBundleIDMapping
+ __unnamed_array_storage.100
+ __unnamed_array_storage.130
+ __unnamed_array_storage.151
+ __unnamed_array_storage.158
+ __unnamed_array_storage.171
+ __unnamed_array_storage.189
+ __unnamed_array_storage.198
+ __unnamed_array_storage.207
+ __unnamed_array_storage.210
+ __unnamed_array_storage.23
+ __unnamed_array_storage.24
+ __unnamed_array_storage.252
+ __unnamed_array_storage.261
+ __unnamed_array_storage.265
+ __unnamed_array_storage.29
+ __unnamed_array_storage.319
+ __unnamed_array_storage.38
+ __unnamed_array_storage.47
+ __unnamed_array_storage.50
+ __unnamed_array_storage.53
+ __unnamed_array_storage.56
+ __unnamed_array_storage.59
+ __unnamed_array_storage.67
+ __unnamed_array_storage.70
+ __unnamed_array_storage.96
+ __unnamed_array_storage.97
+ _abort
+ _bzero
+ _dyld_get_active_platform
+ _getCNContactPostalAddressesKeySymbolLoc.ptr
+ _getPFSceneTaxonomyClass
+ _getPhotoBasedFeaturesAsync:withTimeout:._onceToken
+ _getPhotoBasedFeaturesAsync:withTimeout:._pasExprOnceResult
+ _internedValues.onceToken
+ _internedValues.values.0
+ _internedValues.values.1
+ _internedValues.values.2
+ _internedValues.values.3
+ _internedValues.values.4
+ _internedValues.values.5
+ _malloc_type_posix_memalign
+ _objc_autorelease
+ _objc_begin_catch
+ _objc_end_catch
+ _objc_exception_rethrow
+ _objc_exception_throw
+ _objc_msgSend$addFeatureWithIntValue:doubleValue:stringValue:boolValue:timeBucket:forKey:
+ _objc_msgSend$autoreleasingSerialQueueWithLabel:qosClass:
+ _objc_msgSend$candidateForDeduping
+ _objc_msgSend$contactEmbeddingConfig
+ _objc_msgSend$containingBundleRecord
+ _objc_msgSend$defaultConfig
+ _objc_msgSend$dictionaryWithPath:error:
+ _objc_msgSend$digest
+ _objc_msgSend$doubleForKey:
+ _objc_msgSend$enumeratorWithExtensionPointRecord:options:
+ _objc_msgSend$featureOrderFromMetadata
+ _objc_msgSend$getCharacters:
+ _objc_msgSend$getCoreMLSuggestionProxiesWithPredictionContext:modelSuggestionProxiesDict:candidateToFeatureVectorDictGetter:
+ _objc_msgSend$getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:
+ _objc_msgSend$getMutableBytesWithHandler:
+ _objc_msgSend$getPhotoBasedFeaturesAsync:withTimeout:
+ _objc_msgSend$getSuggestionProxiesForCandidateToFeatureVectorDictGetter:predictionContext:messageInteractionCache:shareInteractionCache:
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$initWithCharacters:length:
+ _objc_msgSend$initWithContentsOfURL:error:
+ _objc_msgSend$initWithId:type:engagedSuggestionId:airdropOptionPresent:visiblePeopleSuggestionCount:visibleAppSuggestionCount:trialExperimentId:trialTreatmentId:trialDeploymentId:peopleSuggestionTimeoutOccurred:
+ _objc_msgSend$initWithIdentifier:platform:error:
+ _objc_msgSend$initWithIdentifier:responseType:suggestions:
+ _objc_msgSend$initWithIdentifier:suggestions:
+ _objc_msgSend$initWithLatestTaxonomy
+ _objc_msgSend$isCloudPhotoLibraryEnabled
+ _objc_msgSend$loadPSConfigPath:
+ _objc_msgSend$mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:
+ _objc_msgSend$messagesPinningConfig
+ _objc_msgSend$modelDisplayName
+ _objc_msgSend$mostRecentInteractionForCandidateIdentifier:
+ _objc_msgSend$populateIsSystemBundleId
+ _objc_msgSend$postalAddresses
+ _objc_msgSend$preprocessAndFetchFeatureTensor:error:
+ _objc_msgSend$prewarmPhotosFrameworks
+ _objc_msgSend$reformatCandidateDictionaryIntoFeatureTensor:error:
+ _objc_msgSend$runBlockWhenDeviceIsClassCUnlocked:
+ _objc_msgSend$setFeatureValueForFeatureName:featureValue:candidate:bundleID:
+ _objc_msgSend$setFilter:
+ _objc_msgSend$setMlModelInitialized:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$vocab
+ _objc_terminate
+ _prewarmPhotosFrameworks.prewarmOnce
+ _stat
- +[_PSContactEmbeddingUtilities loadFeaturesDictFromPath:]
- +[_PSContactEmbeddingUtilities loadFeaturesDictFromPath:].cold.1
- +[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAssets:]
- +[_PSPhotoSuggestions mdPersonIDsOfPeopleInSharedPhotoAssets:].cold.1
- -[_PSCoreMLScoringModel _getIndexForIndices:multiArray:]
- -[_PSCoreMLScoringModel _getIndexForIndices:multiArray:].cold.1
- -[_PSCoreMLScoringModel _getIndexForIndices:multiArray:].cold.2
- -[_PSCoreMLScoringModel featureOrderLookup]
- -[_PSCoreMLScoringModel featureOrder]
- -[_PSCoreMLScoringModel getNumberAtIndices:forMultiArray:]
- -[_PSCoreMLScoringModel getSuggestionProxiesForCandidateToFeatureVectorDict:predictionContext:messageInteractionCache:shareInteractionCache:]
- -[_PSCoreMLScoringModel loadModelMetadata].cold.2
- -[_PSCoreMLScoringModel loadModelMetadata].cold.3
- -[_PSCoreMLScoringModel predictWithFeatureTensor:numCandidates:].cold.5
- -[_PSCoreMLScoringModel preprocessAndFetchFeatureTensor:]
- -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:]
- -[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:].cold.1
- -[_PSCoreMLScoringModel setFeatureOrder:]
- -[_PSCoreMLScoringModel setFeatureOrderLookup:]
- -[_PSCoreMLScoringModel setNumberAtIndices:forMultiArray:value:]
- -[_PSEnsembleModel getCoreMLSuggestionProxiesWithPredictionContext:modelSuggestionProxiesDict:candidateToFeatureVectorDict:]
- -[_PSEnsembleModel getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:meContactIdentifier:]
- -[_PSEnsembleModel getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:meContactIdentifier:].cold.1
- -[_PSEnsembleModel getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:meContactIdentifier:].cold.2
- -[_PSEnsembleModel getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:meContactIdentifier:].cold.3
- -[_PSEnsembleModel loadPSConfig:].cold.1
- -[_PSFeatureCache setFeatureValueForFeatureName:featureValue:candidate:]
- -[_PSFeatureCache setFeatureValueForFeatureName:featureValue:candidate:].cold.1
- -[_PSFeatureCache setFeatureValueForFeatureName:featureValue:candidate:].cold.2
- -[_PSFeatureDictionary _otherValuesCreateIfNeeded]
- -[_PSFeatureDictionary init]
- -[_PSMessagesPinningSuggester initWithRegularityThreshold:intensityThreshold:regularityWeight:intensityWeight:minimalInteration:minimalUniqueDaysInteracted:interactionStore:lookbackWindow:outgoingOnly:].cold.1
- -[_PSMessagesPinningSuggester loadPSConfig:]
- -[_PSMessagesPinningSuggester loadPSConfig:].cold.1
- -[_PSShareSheetEphemeralFeatureManager loadPSConfig].cold.1
- GCC_except_table55
- GCC_except_table58
- GCC_except_table63
- GCC_except_table69
- GCC_except_table72
- GCC_except_table75
- GCC_except_table78
- GCC_except_table81
- GCC_except_table86
- GCC_except_table90
- OBJC_IVAR_$__PSFeatureDictionary._otherValues
- _OBJC_CLASS_$_LSEnumerator
- _OBJC_IVAR_$__PSCoreMLScoringModel._featureOrder
- _OBJC_IVAR_$__PSCoreMLScoringModel._featureOrderLookup
- _OUTLINED_FUNCTION_11
- ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.492
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.448
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.448.cold.1
- ___141-[_PSCoreMLScoringModel getSuggestionProxiesForCandidateToFeatureVectorDict:predictionContext:messageInteractionCache:shareInteractionCache:]_block_invoke
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.53
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.53.cold.1
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.55
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.55.cold.1
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke_2.55.cold.2
- ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.142
- ___42-[_PSCoreMLScoringModel loadModelMetadata]_block_invoke
- ___43-[_PSFeatureDictionary removeObjectForKey:]_block_invoke
- ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.125
- ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.126
- ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.102
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_4
- ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.114
- ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.510
- ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.510.cold.1
- ___61-[_PSMessagesPinningSuggester submitMessagesPinningFeedback:]_block_invoke.106
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.255
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.255.cold.1
- ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.136
- ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.117
- ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.148
- ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.473
- ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.139
- ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.145
- ___70-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:]_block_invoke
- ___70-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:]_block_invoke.135
- ___70-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:]_block_invoke_2
- ___70-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:]_block_invoke_2.137
- ___70-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:]_block_invoke_2.cold.1
- ___70-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:]_block_invoke_3
- ___70-[_PSCoreMLScoringModel reformatCandidateDictionaryIntoFeatureTensor:]_block_invoke_3.cold.1
- ___70-[_PSFamilyRecommender personRelationshipVocabularyByLocaleDictionary]_block_invoke
- ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.223
- ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.151
- ___73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.262
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.300
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.303
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.318
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.330
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.327
- ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.156
- ___77-[_PSMessagesPinningSuggester chatGuidsForMessagesPinningWithMaxSuggestions:]_block_invoke.46
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.89
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.97
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.98
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.99
- ___82+[_PSFeaturePreprocessor oneHotEncodedDictionaryWithCandidateToFeatureVectorDict:]_block_invoke_3
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.414
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.401
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.cold.1
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.cold.2
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.106
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.109
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.110
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.111
- ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.120
- ___88+[_PSLastCommunicatedFeatures lastInteractionFromCandidate:caches:direction:mechanisms:]_block_invoke_2
- ___99-[_PSKNNModel rankedCoRecipientSuggestionsWithPredictionContext:modelConfiguration:maxSuggestions:]_block_invoke.172
- ___Block_byref_object_copy_.87
- ___Block_byref_object_dispose_.88
- ___block_descriptor_100_e8_32s40s48s56s64s72s80s88r_e29_v32?0"_PSCandidate"8Q16^B24ls32l8s40l8r88l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_32_e39_q24?0"_PSCandidate"8"_PSCandidate"16l
- ___block_descriptor_33_e24_B16?0"LSPropertyList"8l
- ___block_descriptor_40_e8_32bs_e25_v32?0"NSString"816^B24ls32l8
- ___block_descriptor_40_e8_32s_e22_B16?0"_PSCandidate"8ls32l8
- ___block_descriptor_40_e8_32s_e25_v32?0"NSString"8Q16^B24ls32l8
- ___block_descriptor_48_e8_32s40bs_e25_v32?0"NSString"816^B24ls32l8s40l8
- ___block_descriptor_48_e8_32s40r_e22_B16?0"BMStoreEvent"8lr40l8s32l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e21_v24?0"NSString"816ls32l8s40l8s48l8r64l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e22_v16?0"BMStoreEvent"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_literal_global.101
- ___block_literal_global.105
- ___block_literal_global.113
- ___block_literal_global.116
- ___block_literal_global.119
- ___block_literal_global.124
- ___block_literal_global.128
- ___block_literal_global.138
- ___block_literal_global.141
- ___block_literal_global.144
- ___block_literal_global.147
- ___block_literal_global.150
- ___block_literal_global.155
- ___block_literal_global.156
- ___block_literal_global.206
- ___block_literal_global.209
- ___block_literal_global.214
- ___block_literal_global.226
- ___block_literal_global.230
- ___block_literal_global.234
- ___block_literal_global.254
- ___block_literal_global.259
- ___block_literal_global.284
- ___block_literal_global.298
- ___block_literal_global.302
- ___block_literal_global.305
- ___block_literal_global.318
- ___block_literal_global.321
- ___block_literal_global.326
- ___block_literal_global.329
- ___block_literal_global.332
- ___block_literal_global.334
- ___block_literal_global.502
- ___block_literal_global.505
- ___block_literal_global.99
- __unnamed_array_storage.104
- __unnamed_array_storage.107
- __unnamed_array_storage.118
- __unnamed_array_storage.128
- __unnamed_array_storage.132
- __unnamed_array_storage.139
- __unnamed_array_storage.143
- __unnamed_array_storage.154
- __unnamed_array_storage.169
- __unnamed_array_storage.187
- __unnamed_array_storage.196
- __unnamed_array_storage.205
- __unnamed_array_storage.208
- __unnamed_array_storage.273
- __unnamed_array_storage.31
- __unnamed_array_storage.323
- __unnamed_array_storage.36
- __unnamed_array_storage.45
- __unnamed_array_storage.54
- __unnamed_array_storage.57
- __unnamed_array_storage.60
- __unnamed_array_storage.63
- __unnamed_array_storage.66
- __unnamed_array_storage.69
- __unnamed_array_storage.94
- _lastInteractionFromCandidate:caches:direction:mechanisms:._onceToken
- _lastInteractionFromCandidate:caches:direction:mechanisms:._pasExprOnceResult
- _objc_msgSend$_getIndexForIndices:multiArray:
- _objc_msgSend$containingBundle
- _objc_msgSend$dictionaryWithContentsOfURL:
- _objc_msgSend$enumeratorForPlugInKitProxiesWithExtensionPoint:options:filter:
- _objc_msgSend$featureOrder
- _objc_msgSend$featureOrderLookup
- _objc_msgSend$getCoreMLSuggestionProxiesWithPredictionContext:modelSuggestionProxiesDict:candidateToFeatureVectorDict:
- _objc_msgSend$getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:meContactIdentifier:
- _objc_msgSend$getSuggestionProxiesForCandidateToFeatureVectorDict:predictionContext:messageInteractionCache:shareInteractionCache:
- _objc_msgSend$initWithDictionary:copyItems:
- _objc_msgSend$initWithId:sourceBundleId:suggestions:
- _objc_msgSend$initWithId:sourceBundleId:timedOutModels:suggestions:
- _objc_msgSend$initWithId:type:engagedSuggestionId:airdropOptionPresent:visiblePeopleSuggestionCount:visibleAppSuggestionCount:inferenceSource:trialExperimentId:trialTreatmentId:trialDeploymentId:peopleSuggestionTimeoutOccurred:
- _objc_msgSend$isCoreMLValidationFetch
- _objc_msgSend$loadFeaturesDictFromPath:
- _objc_msgSend$mdPersonIDsOfPeopleInSharedPhotoAssets:
- _objc_msgSend$numberWithChar:
- _objc_msgSend$numberWithUnsignedShort:
- _objc_msgSend$pathForResource:ofType:
- _objc_msgSend$preprocessAndFetchFeatureTensor:
- _objc_msgSend$reformatCandidateDictionaryIntoFeatureTensor:
- _objc_msgSend$setFeatureOrder:
- _objc_msgSend$setFeatureOrderLookup:
- _objc_msgSend$setFeatureValueForFeatureName:featureValue:candidate:
- _objc_msgSend$setNumberAtIndices:forMultiArray:value:
- _objc_msgSend$strides
- _personRelationshipVocabularyByLocaleDictionary.onceToken
- _personRelationshipVocabularyByLocaleDictionary.sPersonRelationshipVocabularyByLocaleDictionary
CStrings:
+ "\x17\x11"
+ "%@ not in metadata"
+ "(   (recipientCount > 1)   OR    (recipientCount >= 1 AND sender != nil)) AND (   (SUBQUERY(recipients, $recipient, ANY $recipient.displayName BEGINSWITH[cd] %@).@count > 0)   OR    (direction != %d AND sender != nil AND sender.displayName BEGINSWITH[cd] %@))"
+ "/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/FeatureManager/_PSFeatureCache.m:582"
+ "@\"_PSCandidate\"16@?0@\"_PSCandidate\"8"
+ "@32@0:8@?16@24"
+ "@48@0:8@?16@24@32@40"
+ "@?32@0:8@16d24"
+ "B16@?0@\"LSApplicationExtensionRecord\"8"
+ "CNContactPostalAddressesKey"
+ "Could not decode feature list. %@"
+ "Error creating tensor: %@"
+ "Failed to decode plist named %{public}@: %{public}@"
+ "Failed to stat plist named %{public}@"
+ "Final ZKW suggestions post-transformers: %{sensitive}@"
+ "Finished one hot encoding features"
+ "Loaded psConfig"
+ "One hot encoding features"
+ "Resolved group name or display image, group name: %{sensitive}@, display name: %{sensitive}@"
+ "SuggestLess: Feedback handle is nil. Falling back to NO predicate"
+ "T@\"_PSInteractionAndContactMonitor\",&,N,V_contactMonitor"
+ "TB,N,V_mlModelInitialized"
+ "Unable to generate URL path for plist %{public}@"
+ "Unexpected output shape %@"
+ "_PSCandidateScoringCoreMLModel - candidateToFeatureVectorDict (%{public}@) was missing or empty"
+ "_PSCandidateScoringCoreMLModel - mode was missing"
+ "_PSConfig"
+ "_PSEnsembleModel_populateCachesWithSupportedBundleIDs"
+ "_PSFeatureCacheDurableCachesWithCandidates"
+ "_PSGetPhotoBasedFeaturesTimeout"
+ "_PSPhotoUtils prewarm"
+ "_PSShareSheetCoreMLSuggestions"
+ "_PSShareSheetLoadMLModel"
+ "_PSShareSheetRefreshDurableCachesWithCandidates"
+ "_PSShareSheetReplaceEphemeralFeaturesWithCache"
+ "_PSShareSheetSuggestionBundleIDMapping expiration"
+ "_PSSuggestionAsyncFallbackTotalTime"
+ "_PSSuggestionAsyncTotalTime"
+ "_isSystemBundleId"
+ "_mlModelInitialized"
+ "_unoptimizedValues"
+ "addFeatureWithIntValue:doubleValue:stringValue:boolValue:timeBucket:forKey:"
+ "appSuggestions"
+ "autoreleasingSerialQueueWithLabel:qosClass:"
+ "backgroundRefetch"
+ "cached"
+ "candidateForDeduping"
+ "candidateToFeatureVectorDictFetchBlock"
+ "com.apple.PeopleSuggester.ContactEmbedding.Features"
+ "com.apple.PeopleSuggester.MessagesPinning.Config"
+ "contactEmbeddingConfig"
+ "contacts: %{sensitive}@ templateContactIDs: %@ mergedContactIdentifiers: %@"
+ "containingBundleRecord"
+ "defaultConfig"
+ "dictionaryWithPath:error:"
+ "digest"
+ "doubleForKey:"
+ "enumeratorWithExtensionPointRecord:options:"
+ "feature list length doesn't match shape"
+ "featureName not recognized (or featureValue is nil): excluding case-insensitive matches=%{public}@, all=%{public}@"
+ "featureOrderFromMetadata"
+ "getCharacters:"
+ "getCoreMLSuggestionProxiesWithPredictionContext:modelSuggestionProxiesDict:candidateToFeatureVectorDictGetter:"
+ "getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:"
+ "getMutableBytesWithHandler:"
+ "getPhotoBasedFeatures"
+ "getPhotoBasedFeaturesAsync:withTimeout:"
+ "getSuggestionProxiesForCandidateToFeatureVectorDictGetter:predictionContext:messageInteractionCache:shareInteractionCache:"
+ "infoDictionary"
+ "initWithCharacters:length:"
+ "initWithContentsOfURL:error:"
+ "initWithId:type:engagedSuggestionId:airdropOptionPresent:visiblePeopleSuggestionCount:visibleAppSuggestionCount:trialExperimentId:trialTreatmentId:trialDeploymentId:peopleSuggestionTimeoutOccurred:"
+ "initWithIdentifier:platform:error:"
+ "initWithIdentifier:responseType:suggestions:"
+ "initWithIdentifier:suggestions:"
+ "initWithLatestTaxonomy"
+ "isCloudPhotoLibraryEnabled"
+ "loadPSConfigPath:"
+ "malloc failed"
+ "mdPersonIDsOfPeopleInSharedPhotoAttachments:forBundleID:"
+ "messagesPinningConfig"
+ "missingFeaturesLogQueue"
+ "mlModelInitialized"
+ "modelDisplayName"
+ "mostRecentInteractionForCandidateIdentifier:"
+ "no feature %@ for candidate %lu"
+ "no features"
+ "populateIsSystemBundleId"
+ "postalAddresses"
+ "prediction count (%ld) < candidate count (%@)"
+ "preprocessAndFetchFeatureTensor:error:"
+ "prewarmPhotosFrameworks"
+ "reformatCandidateDictionaryIntoFeatureTensor:error:"
+ "runBlockWhenDeviceIsClassCUnlocked:"
+ "setFeatureValueForFeatureName:featureValue:candidate:bundleID:"
+ "setFilter:"
+ "setMlModelInitialized:"
+ "suggestions array: %{sensitive}@, addedRecipientInfo: %@"
+ "unsignedIntValue"
+ "v32@?0^v8q16@\"NSArray\"24"
+ "v44@0:8i16@20@28@36"
+ "v60@0:8@16@24@32@40i48@52"
- "\t\x11"
- "(recipientCount > 1 OR (recipientCount >= 1 AND sender != nil)) AND (SUBQUERY(recipients, $recipient, ANY $recipient.displayName BEGINSWITH[cd] %@).@count > 0 OR (sender != nil AND sender.displayName BEGINSWITH[cd] %@))"
- "-[_PSCoreMLScoringModel _getIndexForIndices:multiArray:]"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/PeopleSuggester/PeopleSuggester/FeatureManager/_PSFeatureCache.m:558"
- "/System/Library/PrivateFrameworks/PeopleSuggester.framework/com.apple.PeopleSuggester.ContactEmbedding.Features.plist"
- "@\"NSOrderedSet\""
- "B16@?0@\"LSPropertyList\"8"
- "B16@?0@\"_PSCandidate\"8"
- "Candidate count exceeded the input dimensions of the tensor"
- "Counted %tu suggestions for metrics"
- "Failed to load config with path:%@, with error：%@"
- "Failed to resolve path for default config plist %@"
- "Feature value %@ was not processed correctly to be passed into the model, input feature value was %@"
- "Final ZKW suggestions post-transformers: %@"
- "Finished one hot econding features"
- "Input tensor %{private}@"
- "Loaded psConfig from:%@"
- "ML Model: expected no repeated features: %{private}@"
- "ML Model: no feature order encoded in model"
- "MLFeatureInput: %{private}@"
- "One hot econding features"
- "PSShareSheetEphemeralFeatureManager: failed to load trial config with path:%@, with error：%@"
- "Resolved group name or display image, group name: %@, display name: %@"
- "Successfully fetched feature ouput: %{private}@"
- "T@\"NSArray\",&,N,V_featureOrder"
- "T@\"NSOrderedSet\",&,N,V_featureOrderLookup"
- "T@\"_PSInteractionAndContactMonitor\",&,V_contactMonitor"
- "_PSCandidateScoringCoreMLModel - model or candidateToFeatureVectorDict was missing"
- "_PSCoreMLScoringModel.m"
- "_PSCoreMLScoringModel: finished unloading model"
- "_PSCoreMLScoringModel: unloading model"
- "_featureOrder"
- "_featureOrderLookup"
- "_getIndexForIndices:multiArray:"
- "c"
- "com.apple.PeopleSuggester.MessagesPinning.Config.plist"
- "contacts: %@ templateContactIDs: %@ mergedContactIdentifiers: %@"
- "containingBundle"
- "dictionaryWithContentsOfURL:"
- "enumeratorForPlugInKitProxiesWithExtensionPoint:options:filter:"
- "featureOrder"
- "featureOrderLookup"
- "getCoreMLSuggestionProxiesWithPredictionContext:modelSuggestionProxiesDict:candidateToFeatureVectorDict:"
- "getHeuristicSuggestionProxies:supportedBundleIDs:modelSuggestionProxiesDict:meContactIdentifier:"
- "getNumberAtIndices:forMultiArray:"
- "getSuggestionProxiesForCandidateToFeatureVectorDict:predictionContext:messageInteractionCache:shareInteractionCache:"
- "indexInt < shapeInt"
- "indices.count == shape.count"
- "initWithDictionary:copyItems:"
- "initWithId:sourceBundleId:suggestions:"
- "initWithId:sourceBundleId:timedOutModels:suggestions:"
- "initWithId:type:engagedSuggestionId:airdropOptionPresent:visiblePeopleSuggestionCount:visibleAppSuggestionCount:inferenceSource:trialExperimentId:trialTreatmentId:trialDeploymentId:peopleSuggestionTimeoutOccurred:"
- "loadFeaturesDictFromPath:"
- "mdPersonIDsOfPeopleInSharedPhotoAssets:"
- "numberWithChar:"
- "numberWithUnsignedShort:"
- "pathForResource:ofType:"
- "preprocessAndFetchFeatureTensor:"
- "q24@?0@\"_PSCandidate\"8@\"_PSCandidate\"16"
- "reformatCandidateDictionaryIntoFeatureTensor:"
- "rule_mining"
- "setFeatureOrder:"
- "setFeatureOrderLookup:"
- "setFeatureValueForFeatureName:featureValue:candidate:"
- "setNumberAtIndices:forMultiArray:value:"
- "strides"
- "suggestions array: %@, addedRecipientInfo: %@"
- "v24@?0@\"NSString\"8@16"
- "v32@?0@\"_PSCandidate\"8Q16^B24"
- "v36@0:8i16@20@28"

```
