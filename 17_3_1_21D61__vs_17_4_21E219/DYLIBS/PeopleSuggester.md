## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1852.6.1.0.0
-  __TEXT.__text: 0xe7018
-  __TEXT.__auth_stubs: 0xd90
-  __TEXT.__objc_methlist: 0x8b80
+1852.19.0.2.0
+  __TEXT.__text: 0xe7454
+  __TEXT.__auth_stubs: 0xdc0
+  __TEXT.__objc_methlist: 0x8b88
   __TEXT.__const: 0x610
-  __TEXT.__gcc_except_tab: 0x1c84
-  __TEXT.__cstring: 0x8ea1
-  __TEXT.__oslogstring: 0xb875
+  __TEXT.__gcc_except_tab: 0x1ca8
+  __TEXT.__cstring: 0x8ece
+  __TEXT.__oslogstring: 0xb97a
   __TEXT.__dlopen_cstrs: 0x18da
   __TEXT.__unwind_info: 0x264c
   __TEXT.__objc_classname: 0x10f0
-  __TEXT.__objc_methname: 0x1f1a3
+  __TEXT.__objc_methname: 0x1f1e1
   __TEXT.__objc_methtype: 0x26a1
-  __TEXT.__objc_stubs: 0x12f60
+  __TEXT.__objc_stubs: 0x12f80
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x2560
   __DATA_CONST.__objc_classlist: 0x4c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf758
-  __DATA_CONST.__objc_selrefs: 0x5bb8
+  __DATA_CONST.__objc_const: 0xf778
+  __DATA_CONST.__objc_selrefs: 0x5bc0
+  __DATA_CONST.__objc_classrefs: 0x6e0
+  __DATA_CONST.__objc_superrefs: 0x378
   __DATA_CONST.__objc_arraydata: 0xd50
-  __AUTH_CONST.__cfstring: 0x8960
+  __AUTH_CONST.__cfstring: 0x89a0
   __AUTH_CONST.__objc_intobj: 0xfd8
   __AUTH_CONST.__objc_arrayobj: 0x870
   __AUTH_CONST.__objc_const: 0x350
-  __AUTH_CONST.__const: 0x780
+  __AUTH_CONST.__const: 0x7e0
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH_CONST.__auth_got: 0x6d8
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x6e0
-  __DATA.__objc_superrefs: 0x378
-  __DATA.__objc_ivar: 0xd38
-  __DATA.__data: 0x440
-  __DATA.__bss: 0x448
-  __DATA_DIRTY.__const: 0xf80
+  __AUTH_CONST.__auth_got: 0x6f0
+  __DATA.__objc_ivar: 0xd3c
+  __DATA.__data: 0x4b8
+  __DATA.__bss: 0x388
+  __DATA_DIRTY.__const: 0xf40
   __DATA_DIRTY.__objc_const: 0x3760
-  __DATA_DIRTY.__objc_data: 0x2f80
-  __DATA_DIRTY.__bss: 0x8e8
+  __DATA_DIRTY.__objc_data: 0x2fd0
+  __DATA_DIRTY.__bss: 0x930
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C5527424-40FF-3A16-85F8-4065A93A565B
-  Functions: 4449
-  Symbols:   15101
-  CStrings:  8188
+  UUID: 25A14742-2896-30F7-8289-469FED7FA515
+  Functions: 4452
+  Symbols:   15112
+  CStrings:  8200
 
Symbols:
+ -[_PSFamilyMLModel initializeModels].cold.1
+ -[_PSFeatureCache dealloc]
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table65
+ GCC_except_table69
+ GCC_except_table75
+ GCC_except_table78
+ _OBJC_IVAR_$__PSSuggesterCache._fetches
+ _OBJC_IVAR_$__PSSuggesterCache._ticks
+ ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.517
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.473
+ ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.473.cold.1
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.60
+ ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.60.cold.1
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.27
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.31
+ ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_2.33
+ ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.535
+ ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.535.cold.1
+ ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.498
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.311
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.319
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.334
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.340
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.347
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.344
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.439
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.411
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.414
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.425
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.432
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.432.cold.1
+ ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.432.cold.2
+ ___block_literal_global.242
+ ___block_literal_global.26
+ ___block_literal_global.314
+ ___block_literal_global.318
+ ___block_literal_global.321
+ ___block_literal_global.337
+ ___block_literal_global.343
+ ___block_literal_global.346
+ ___block_literal_global.349
+ ___block_literal_global.36
+ ___block_literal_global.413
+ ___block_literal_global.452
+ ___block_literal_global.527
+ ___block_literal_global.530
+ __unnamed_array_storage.289
+ _dispatch_assert_queue$V2
+ _objc_msgSend$setContactBatchCount:
+ _pthread_mutex_destroy
+ _pthread_mutexattr_destroy
- GCC_except_table100
- GCC_except_table102
- GCC_except_table68
- GCC_except_table74
- GCC_except_table77
- _OBJC_IVAR_$__PSSuggesterCache._leeway
- ___120-[_PSEnsembleModel rankedGlobalSuggestionsWithPredictionContext:contactsOnly:maxSuggestions:excludeBackfillSuggestions:]_block_invoke.510
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.466
- ___126-[_PSEnsembleModel suggestionsFromSuggestionProxies:supportedBundleIDs:contactKeysToFetch:meContactIdentifier:maxSuggestions:]_block_invoke.466.cold.1
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.58
- ___37-[_PSFeatureCache saveToVirtualStore]_block_invoke.58.cold.1
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.25
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke.29
- ___54-[_PSFeatureCache refreshDurableCachesWithCandidates:]_block_invoke_2.31
- ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.528
- ___55-[_PSEnsembleModel appExtensionSuggestionsFromContext:]_block_invoke.528.cold.1
- ___68-[_PSEnsembleModel predictWithMapsPredictionContext:maxSuggestions:]_block_invoke.491
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.287
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.292
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.295
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.310
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.323
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.320
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.432
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.407
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke.418
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.425
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.425.cold.1
- ___83-[_PSEnsembleModel predictWithPredictionContext:maxSuggestions:contactKeysToFetch:]_block_invoke_2.425.cold.2
- ___block_literal_global.290
- ___block_literal_global.297
- ___block_literal_global.313
- ___block_literal_global.319
- ___block_literal_global.322
- ___block_literal_global.34
- ___block_literal_global.445
- ___block_literal_global.520
- ___block_literal_global.523
- __unnamed_array_storage.265
- _cacheUpdateTime
CStrings:
+ "\x06\x83#"
+ "Failed to load all %tu models (successfully loaded %tu models: %{public}@)"
+ "Photos-based features fetching is disabled"
+ "T@\"NSString\",?,R,C"
+ "_PSSuggesterCache: Timer tick: Initial fetch (ticks=%tu, fetches=%tu)"
+ "_PSSuggesterCache: Timer tick: Refreshing cache (ticks=%tu, fetches=%tu)"
+ "_fetches"
+ "_ticks"
+ "cacheUpdateInterval"
+ "enablePhotoBasedFeatures"
+ "setContactBatchCount:"
- "\x06\x13#"

```
