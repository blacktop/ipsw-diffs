## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1852.4.7.0.3
-  __TEXT.__text: 0xe6ddc
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_methlist: 0x8b18
+1852.6.1.0.0
+  __TEXT.__text: 0xe7018
+  __TEXT.__auth_stubs: 0xd90
+  __TEXT.__objc_methlist: 0x8b80
   __TEXT.__const: 0x610
-  __TEXT.__gcc_except_tab: 0x1c7c
-  __TEXT.__cstring: 0x8eb1
-  __TEXT.__oslogstring: 0xb7df
+  __TEXT.__gcc_except_tab: 0x1c84
+  __TEXT.__cstring: 0x8ea1
+  __TEXT.__oslogstring: 0xb875
   __TEXT.__dlopen_cstrs: 0x18da
-  __TEXT.__unwind_info: 0x2638
+  __TEXT.__unwind_info: 0x264c
   __TEXT.__objc_classname: 0x10f0
-  __TEXT.__objc_methname: 0x1f0f5
-  __TEXT.__objc_methtype: 0x2687
-  __TEXT.__objc_stubs: 0x12ea0
+  __TEXT.__objc_methname: 0x1f1a3
+  __TEXT.__objc_methtype: 0x26a1
+  __TEXT.__objc_stubs: 0x12f60
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x2560
   __DATA_CONST.__objc_classlist: 0x4c8

   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0xf758
-  __DATA_CONST.__objc_selrefs: 0x5b78
-  __DATA_CONST.__objc_arraydata: 0xd60
-  __AUTH_CONST.__cfstring: 0x8940
+  __DATA_CONST.__objc_selrefs: 0x5bb8
+  __DATA_CONST.__objc_arraydata: 0xd50
+  __AUTH_CONST.__cfstring: 0x8960
   __AUTH_CONST.__objc_intobj: 0xfd8
-  __AUTH_CONST.__objc_arrayobj: 0x888
+  __AUTH_CONST.__objc_arrayobj: 0x870
   __AUTH_CONST.__objc_const: 0x350
-  __AUTH_CONST.__const: 0x7a0
+  __AUTH_CONST.__const: 0x780
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x6d0
+  __AUTH_CONST.__auth_got: 0x6d8
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x6e8
+  __DATA.__objc_classrefs: 0x6e0
   __DATA.__objc_superrefs: 0x378
   __DATA.__objc_ivar: 0xd38
   __DATA.__data: 0x440
   __DATA.__bss: 0x448
-  __DATA_DIRTY.__const: 0xf60
+  __DATA_DIRTY.__const: 0xf80
   __DATA_DIRTY.__objc_const: 0x3760
   __DATA_DIRTY.__objc_data: 0x2f80
   __DATA_DIRTY.__bss: 0x8e8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4442
-  Symbols:   15082
-  CStrings:  7078
+  Functions: 4449
+  Symbols:   15101
+  CStrings:  7089
 
Symbols:
+ -[_PSFeatureDictionary addEntriesFromDictionary:overwrite:]
+ -[_PSRecipient descriptionRedacted:]
+ -[_PSRecipient redactedDescription]
+ -[_PSSuggester getCacheSuggestions]
+ -[_PSSuggester getCacheSuggestions].cold.1
+ -[_PSSuggesterCache _refetch]
+ -[_PSSuggesterCache getCachedSuggestionsAndSessionID:]
+ -[_PSSuggesterCache performInitialFetchIfNeeded]
+ -[_PSSuggestionProxy descriptionRedacted:]
+ -[_PSSuggestionProxy redactedDescription]
+ ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.510
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.466
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.466.cold.1
+ ___29-[_PSSuggesterCache _refetch]_block_invoke
+ ___35-[_PSSuggester getCacheSuggestions]_block_invoke
+ ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.150
+ ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.52
+ ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.52.cold.1
+ ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.56
+ ___47-[_PSSuggester suggestInteractionsFromContext:]_block_invoke.68
+ ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.133
+ ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.134
+ ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.110
+ ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.122
+ ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.528
+ ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.528.cold.1
+ ___59-[_PSFeatureDictionary addEntriesFromDictionary:overwrite:]_block_invoke
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.262
+ ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.262.cold.1
+ ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.144
+ ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.125
+ ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.156
+ ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.491
+ ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.147
+ ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.153
+ ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.230
+ ___72-[_PSSuggester computeShareSheetEphemeralFeaturesWithPredictionContext:]_block_invoke.60
+ ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.159
+ ___73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.269
+ ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.164
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.100
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.101
+ ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.95
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.432
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.407
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.418
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.425
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.425.cold.1
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.425.cold.2
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.114
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.118
+ ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.119
+ ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.128
+ ___Block_byref_object_copy_.93
+ ___Block_byref_object_dispose_.94
+ ___block_descriptor_41_e8_32s_e46_v32?0"NSNumber"8"NSMutableDictionary"16^B24ls32l8
+ ___block_descriptor_72_e8_32s40s48bs56bs64r_e5_v8?0ls48l8s32l8r64l8s40l8s56l8
+ ___block_descriptor_72_e8_32s40s48r56r64r_e42_v24?0"NSArray"8"_PSPredictionContext"16lr48l8s32l8r56l8s40l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56bs64bs_e5_v8?0ls56l8s32l8s40l8s48l8s64l8
+ ___block_literal_global.109
+ ___block_literal_global.113
+ ___block_literal_global.116
+ ___block_literal_global.121
+ ___block_literal_global.124
+ ___block_literal_global.136
+ ___block_literal_global.146
+ ___block_literal_global.149
+ ___block_literal_global.155
+ ___block_literal_global.213
+ ___block_literal_global.216
+ ___block_literal_global.221
+ ___block_literal_global.233
+ ___block_literal_global.241
+ ___block_literal_global.268
+ ___block_literal_global.277
+ ___block_literal_global.282
+ ___block_literal_global.284
+ ___block_literal_global.289
+ ___block_literal_global.291
+ ___block_literal_global.298
+ ___block_literal_global.311
+ ___block_literal_global.327
+ ___block_literal_global.445
+ ___block_literal_global.48
+ ___block_literal_global.520
+ ___block_literal_global.523
+ ___block_literal_global.66
+ __unnamed_array_storage.204
+ __unnamed_array_storage.316
+ _objc_msgSend$_refetch
+ _objc_msgSend$addEntriesFromDictionary:overwrite:
+ _objc_msgSend$descriptionOfArray:redacted:
+ _objc_msgSend$descriptionOfObject:redacted:
+ _objc_msgSend$descriptionRedacted:
+ _objc_msgSend$getCacheSuggestions
+ _objc_msgSend$getCachedSuggestionsAndSessionID:
+ _objc_msgSend$performInitialFetchIfNeeded
+ _objc_msgSend$setByAddingObject:
+ _os_unfair_lock_assert_owner
- -[_PSSuggester getCacheSuggestionsWithPredictionContext:]
- -[_PSSuggester getCacheSuggestionsWithPredictionContext:].cold.1
- _OBJC_CLASS_$__CDCacheCandidate
- ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.509
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.465
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.465.cold.1
- ___28-[_PSSuggesterCache refetch]_block_invoke
- ___39-[_PSSuggester rankedFamilySuggestions]_block_invoke.148
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.53
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.53.cold.1
- ___46-[_PSSuggester candidatesForShareSheetRanking]_block_invoke.57
- ___47-[_PSSuggester suggestInteractionsFromContext:]_block_invoke.69
- ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.131
- ___48-[_PSSuggester rankedZKWSuggestionsFromContext:]_block_invoke.132
- ___49-[_PSFeatureDictionary addEntriesFromDictionary:]_block_invoke
- ___53-[_PSSuggester shareExtensionSuggestionsFromContext:]_block_invoke.108
- ___54-[_PSSuggester rankedNameSuggestionsFromContext:name:]_block_invoke.120
- ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.527
- ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.527.cold.1
- ___57-[_PSSuggester getCacheSuggestionsWithPredictionContext:]_block_invoke
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.260
- ___62-[_PSSuggester deleteInteractionsMatchingSuggestLessFeedback:]_block_invoke.260.cold.1
- ___63-[_PSSuggester autocompleteSearchResultsWithPredictionContext:]_block_invoke.142
- ___64-[_PSSuggester rankedGlobalSuggestionsFromContext:contactsOnly:]_block_invoke.123
- ___67-[_PSSuggester photosRelationshipSuggestionsWithPredictionContext:]_block_invoke.154
- ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.490
- ___68-[_PSSuggester rankedAutocompleteSuggestionsFromContext:candidates:]_block_invoke.145
- ___69-[_PSSuggester familyRecommendationSuggestionsWithPredictionContext:]_block_invoke.151
- ___72-[_PSSuggester _recordFeedbackToInteractionStoreWithFeedback:mechanism:]_block_invoke.228
- ___72-[_PSSuggester computeShareSheetEphemeralFeaturesWithPredictionContext:]_block_invoke.61
- ___72-[_PSSuggester photosContactInferencesSuggestionsWithPredictionContext:]_block_invoke.157
- ___73-[_PSSuggester validateCoreMLScoringModelWithRawInput:predictionContext:]_block_invoke.267
- ___75-[_PSSuggester relativeAppUsageProbabilitiesForCandidateBundleIds:daysAgo:]_block_invoke.162
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.104
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.105
- ___78-[_PSSuggester asyncSuggestInteractionsFromContext:timeout:completionHandler:]_block_invoke.96
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.431
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.406
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.417
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.424
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.424.cold.1
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.424.cold.2
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.112
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.115
- ___84-[_PSSuggester asyncShareExtensionSuggestionsFromContext:timeout:completionHandler:]_block_invoke.116
- ___87-[_PSSuggester rankedSiriNLContactSuggestionsFromContext:maxSuggestions:interactionId:]_block_invoke.126
- ___88+[_PSLastCommunicatedFeatures lastInteractionFromCandidate:caches:direction:mechanisms:]_block_invoke
- ___Block_byref_object_copy_.94
- ___Block_byref_object_dispose_.95
- ___block_descriptor_48_e8_32s40s_e29_B16?0"_CDInteractionCache"8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48bs56bs64r_e5_v8?0ls48l8s32l8s40l8r64l8s56l8
- ___block_descriptor_80_e8_32s40s48r56r64r72r_e42_v24?0"NSArray"8"_PSPredictionContext"16lr48l8s32l8r56l8s40l8r64l8r72l8
- ___block_literal_global.107
- ___block_literal_global.111
- ___block_literal_global.114
- ___block_literal_global.119
- ___block_literal_global.122
- ___block_literal_global.125
- ___block_literal_global.134
- ___block_literal_global.141
- ___block_literal_global.144
- ___block_literal_global.147
- ___block_literal_global.153
- ___block_literal_global.156
- ___block_literal_global.211
- ___block_literal_global.214
- ___block_literal_global.219
- ___block_literal_global.231
- ___block_literal_global.235
- ___block_literal_global.240
- ___block_literal_global.259
- ___block_literal_global.264
- ___block_literal_global.280
- ___block_literal_global.285
- ___block_literal_global.287
- ___block_literal_global.292
- ___block_literal_global.301
- ___block_literal_global.314
- ___block_literal_global.519
- ___block_literal_global.52
- ___block_literal_global.522
- ___block_literal_global.56
- ___block_literal_global.67
- __unnamed_array_storage.198
- __unnamed_array_storage.210
- __unnamed_array_storage.319
- _objc_msgSend$containsUniqueCacheCandidate:
- _objc_msgSend$getCacheSuggestionsWithPredictionContext:
- _objc_msgSend$getCachedSuggestions
CStrings:
+ "@24@0:8^@16"
+ "Blocking on cache population consumed the entire timeout interval. Bailing prior to firing main daemon request."
+ "Ensuring cache is populated"
+ "Not freeing caches because we're coreduetd or knowledge-agent"
+ "Simulating a timeout for testing"
+ "Timeout. Falling back to cached suggestions."
+ "ZKW fallback interaction suggestions: %{sensitive}@"
+ "ZKW primary interaction suggestions: %{sensitive}@"
+ "_PSContactCache: ZKW FaceTime suggestions attempted to lookup contact for handle %@, found contacts %{sensitive}@, error %@"
+ "_PSContactCache: ZKW FaceTime suggestions attempted to lookup contact for uuid %@, found contact %{sensitive}@, error %@"
+ "_refetch"
+ "addEntriesFromDictionary:overwrite:"
+ "com.apple.coreduet.logging"
+ "descriptionOfArray:redacted:"
+ "descriptionOfObject:redacted:"
+ "descriptionRedacted:"
+ "forceSuggesterTimeoutForTesting"
+ "getCacheSuggestions"
+ "getCachedSuggestionsAndSessionID:"
+ "performInitialFetchIfNeeded"
+ "redactedDescription"
+ "setByAddingObject:"
+ "trainArray %{sensitive}@"
+ "v28@0:8@16B24"
- "B16@?0@\"_CDInteractionCache\"8"
- "Fetched in process suggestions: %{private}@"
- "No cache available, fetching suggestions in process"
- "Not freeing caches because we're coreduetd"
- "Too many concurrent requests, had to fallback"
- "Too many requests in flight, timed out query"
- "ZKW fallback interaction suggestions: %@"
- "ZKW primary interaction suggestions: %@"
- "_PSContactCache: ZKW FaceTime suggestions attempted to lookup contact for handle %@, found contacts %@, error %@"
- "_PSContactCache: ZKW FaceTime suggestions attempted to lookup contact for uuid %@, found contact %@, error %@"
- "containsUniqueCacheCandidate:"
- "getCacheSuggestionsWithPredictionContext:"
- "trainArray %@"

```
