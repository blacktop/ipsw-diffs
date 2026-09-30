## PeopleSuggester

> `/System/Library/PrivateFrameworks/PeopleSuggester.framework/PeopleSuggester`

```diff

-1922.0.2.0.0
-  __TEXT.__text: 0xec30c
+1924.0.0.0.0
+  __TEXT.__text: 0xec484
   __TEXT.__auth_stubs: 0xf90
-  __TEXT.__objc_methlist: 0x9804
+  __TEXT.__objc_methlist: 0x9814
   __TEXT.__const: 0x8b8
-  __TEXT.__gcc_except_tab: 0x2d80
-  __TEXT.__cstring: 0xa8cb
-  __TEXT.__oslogstring: 0xb715
+  __TEXT.__gcc_except_tab: 0x2d98
+  __TEXT.__cstring: 0xa8bf
+  __TEXT.__oslogstring: 0xb73f
   __TEXT.__dlopen_cstrs: 0x17a6
   __TEXT.__ustring: 0x33e
-  __TEXT.__unwind_info: 0x2a40
+  __TEXT.__unwind_info: 0x2a50
   __TEXT.__eh_frame: 0x50
-  __TEXT.__objc_classname: 0x1126
-  __TEXT.__objc_methname: 0x210a9
+  __TEXT.__objc_classname: 0x1127
+  __TEXT.__objc_methname: 0x210dd
   __TEXT.__objc_methtype: 0x26b6
-  __TEXT.__objc_stubs: 0x128a0
+  __TEXT.__objc_stubs: 0x128c0
   __DATA_CONST.__got: 0x8d8
   __DATA_CONST.__const: 0x35f0
   __DATA_CONST.__objc_classlist: 0x4b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62b0
+  __DATA_CONST.__objc_selrefs: 0x62b8
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0xcb0
   __AUTH_CONST.__auth_got: 0x7d8
   __AUTH_CONST.__const: 0x1920
   __AUTH_CONST.__cfstring: 0xb5e0
-  __AUTH_CONST.__objc_const: 0x12b40
+  __AUTH_CONST.__objc_const: 0x12b60
   __AUTH_CONST.__objc_intobj: 0x1128
   __AUTH_CONST.__objc_arrayobj: 0x810
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0xd30
+  __DATA.__objc_ivar: 0xd34
   __DATA.__data: 0x3c8
-  __DATA.__bss: 0x5d8
+  __DATA.__bss: 0x5d0
   __DATA_DIRTY.__objc_data: 0x2760
   __DATA_DIRTY.__bss: 0x8b0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AFB07272-B741-32D2-AFCB-417708311F56
-  Functions: 4512
-  Symbols:   15779
-  CStrings:  9036
+  UUID: 14A30B04-38A1-34A9-91B1-6475D2A29916
+  Functions: 4514
+  Symbols:   15784
+  CStrings:  9039
 
Symbols:
+ +[_PSContactSuggester contactPriorSuggestionsForText:].cold.3
+ +[_PSEnsembleModel _feedbackDictionary]
+ +[_PSEnsembleModel _feedbackDictionary].cold.1
+ GCC_except_table131
+ GCC_except_table153
+ GCC_except_table158
+ GCC_except_table163
+ GCC_except_table67
+ GCC_except_table81
+ GCC_except_table95
+ _OBJC_IVAR_$__PSInteractionAndContactMonitor._contactsChangedFlag
+ ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.423
+ ___39+[_PSEnsembleModel _feedbackDictionary]_block_invoke
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.374
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.382
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.397
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.403
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.410
+ ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.407
+ ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.597
+ ___93-[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]_block_invoke.461
+ ___block_descriptor_48_e8_32s_e23_v24?0"CNContact"8^B16ls32l8
+ ___block_literal_global.377
+ ___block_literal_global.384
+ ___block_literal_global.400
+ ___block_literal_global.412
+ ___block_literal_global.438
+ ___block_literal_global.457
+ ___block_literal_global.463
+ ___block_literal_global.538
+ ___block_literal_global.580
+ ___block_literal_global.611
+ ___block_literal_global.644
+ ___getSEMTokenizerClass_block_invoke
+ __feedbackDictionary._pasExprOnceResult
+ __feedbackDictionary._pasOnceToken7
+ _getSEMTokenizerClass.softClass
+ _objc_msgSend$_feedbackDictionary
+ _objc_msgSend$initWithTokenizerLocale:error:
+ _objc_msgSend$queryFromText:
- -[_PSEnsembleModel init].cold.2
- GCC_except_table128
- GCC_except_table152
- GCC_except_table157
- GCC_except_table162
- GCC_except_table35
- GCC_except_table80
- GCC_except_table92
- ___103-[_PSEnsembleModel getPhotoBasedFeaturesAsync:shouldProcessPicturesLive:shouldUseVIPModel:withTimeout:]_block_invoke.421
- ___24-[_PSEnsembleModel init]_block_invoke_4
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.371
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.376
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.394
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.400
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke.407
- ___75-[_PSFamilyRecommender familyRecipientsForShareSheetWithPredictionContext:]_block_invoke_2.404
- ___82-[_PSEnsembleModel addExtraInformationWithSuggestions:modelSuggestionProxiesDict:]_block_invoke.596
- ___93-[_PSEnsembleModel _defaultPredictionsWithPredictionContext:trialClient:config:parentSpanId:]_block_invoke.460
- ___block_descriptor_40_e8_32s_e23_v24?0"CNContact"8^B16ls32l8
- ___block_literal_global.374
- ___block_literal_global.378
- ___block_literal_global.397
- ___block_literal_global.403
- ___block_literal_global.437
- ___block_literal_global.456
- ___block_literal_global.462
- ___block_literal_global.579
- ___block_literal_global.610
- ___block_literal_global.643
- ___getSEMSpanMatchQueryBuilderClass_block_invoke
- __feedbackDictionary
- _getSEMSpanMatchQueryBuilderClass.softClass
- _init._pasExprOnceResult
- _init._pasOnceToken7
- _objc_msgSend$build
- _objc_msgSend$initWithLocale:originalText:
Functions:
~ -[_PSEnsembleModel init] : 368 -> 324
~ +[_PSContactSuggester contactPriorSuggestionsForText:] : 1380 -> 1472
+ +[_PSEnsembleModel _feedbackDictionary]
~ +[_PSEnsembleModel saveFeedback:forSessionId:feedbackActionType:transportBundleId:isFallbackFetch:] : 408 -> 424
~ +[_PSEnsembleModel popFeedbackForSession:] : 296 -> 324
~ -[_PSInteractionAndContactMonitor fetchAllContactIdsFromContactStore] : 464 -> 588
~ ___69-[_PSInteractionAndContactMonitor fetchAllContactIdsFromContactStore]_block_invoke : 180 -> 172
~ -[_PSInteractionAndContactMonitor fetchChangedContactIdsFromContactStore] : 1928 -> 1936
+ +[_PSContactSuggester contactPriorSuggestionsForText:].cold.3
+ +[_PSEnsembleModel _feedbackDictionary].cold.1
- -[_PSEnsembleModel init].cold.2
CStrings:
+ "Failed to create SEMTokenizer (error: %@)"
+ "SEMTokenizer"
+ "_contactsChangedFlag"
+ "_feedbackDictionary"
+ "initWithTokenizerLocale:error:"
+ "queryFromText:"
- "SEMSpanMatchQueryBuilder"
- "build"
- "initWithLocale:originalText:"

```
