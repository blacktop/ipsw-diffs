## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-185.0.0.0.0
-  __TEXT.__text: 0x64e5c
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_stubs: 0xa800
-  __TEXT.__objc_methlist: 0x68b4
+191.0.0.0.0
+  __TEXT.__text: 0x65ca0
+  __TEXT.__auth_stubs: 0x890
+  __TEXT.__objc_stubs: 0xa960
+  __TEXT.__objc_methlist: 0x693c
   __TEXT.__objc_classname: 0x827
-  __TEXT.__objc_methtype: 0xf43
-  __TEXT.__cstring: 0xb07b
-  __TEXT.__objc_methname: 0x112b2
+  __TEXT.__objc_methtype: 0xf8b
+  __TEXT.__cstring: 0xb260
+  __TEXT.__objc_methname: 0x114a4
   __TEXT.__const: 0x470
-  __TEXT.__gcc_except_tab: 0x9e8
-  __TEXT.__oslogstring: 0x680d
+  __TEXT.__gcc_except_tab: 0xb7c
+  __TEXT.__oslogstring: 0x6920
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x10a8
-  __DATA_CONST.__auth_got: 0x448
-  __DATA_CONST.__got: 0x510
+  __TEXT.__unwind_info: 0x1108
+  __DATA_CONST.__auth_got: 0x460
+  __DATA_CONST.__got: 0x518
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2c50
-  __DATA_CONST.__cfstring: 0xe1c0
+  __DATA_CONST.__const: 0x2d30
+  __DATA_CONST.__cfstring: 0xe400
   __DATA_CONST.__objc_classlist: 0x2d8
-  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x228
-  __DATA_CONST.__objc_intobj: 0xa98
-  __DATA_CONST.__objc_arraydata: 0x7f8
+  __DATA_CONST.__objc_superrefs: 0x220
+  __DATA_CONST.__objc_intobj: 0xa68
+  __DATA_CONST.__objc_arraydata: 0x828
   __DATA_CONST.__objc_arrayobj: 0x8a0
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__objc_floatobj: 0x1a0
+  __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xbaf0
-  __DATA.__objc_selrefs: 0x35a8
-  __DATA.__objc_ivar: 0x8ec
+  __DATA.__objc_const: 0xbb60
+  __DATA.__objc_selrefs: 0x3618
+  __DATA.__objc_ivar: 0x8fc
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x4c0
   __DATA.__bss: 0x40
-  __DATA.__common: 0x70
+  __DATA.__common: 0x78
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 2403
-  Symbols:   18307
-  CStrings:  5367
+  Functions: 2427
+  Symbols:   18452
+  CStrings:  5417
 
Symbols:
+ +[MOResource getDedupeKeyForResourceData:type:error:]
+ +[MOResource getDedupeKeyForResourceData:type:error:]
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.1
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.1
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.2
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.2
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.3
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.3
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.4
+ +[MOResource getDedupeKeyForResourceData:type:error:].cold.4
+ +[MOResource getDictionaryForData:error:]
+ +[MOResource getDictionaryForData:error:]
+ +[MOResource getDictionaryForData:error:].cold.1
+ +[MOResource getDictionaryForData:error:].cold.1
+ -[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]
+ -[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]
+ -[MOBundleContentExtractor _filterExtractedBundles:withHandler:]
+ -[MOBundleContentExtractor _filterExtractedBundles:withHandler:]
+ -[MOBundleContentExtractor configurationManager]
+ -[MOBundleContentExtractor configurationManager]
+ -[MOBundleContentExtractor initWithConfigurationManager:]
+ -[MOBundleContentExtractor initWithConfigurationManager:]
+ -[MOBundleContentExtractor initWithConfigurationManager:].cold.1
+ -[MOBundleContentExtractor initWithConfigurationManager:].cold.1
+ -[MOBundleContentExtractor setConfigurationManager:]
+ -[MOBundleContentExtractor setConfigurationManager:]
+ -[MOEventBundle _allResourcesImpl]
+ -[MOEventBundle _allResourcesImpl]
+ -[MOEventBundle withResourcesUsingBlock:]
+ -[MOEventBundle withResourcesUsingBlock:]
+ -[MOEventBundleRanking isInternalBuild]
+ -[MOEventBundleRanking isInternalBuild]
+ -[MOEventWorkout isIndoors]
+ -[MOEventWorkout isIndoors]
+ -[MOEventWorkout setIsIndoors:]
+ -[MOEventWorkout setIsIndoors:]
+ -[MOResource getDedupeKeyError:]
+ -[MOResource getDedupeKeyError:]
+ -[MOTemplate promptVersion]
+ -[MOTemplate promptVersion]
+ -[MOTemplate setPromptVersion:]
+ -[MOTemplate setPromptVersion:]
+ -[MOTemplateStore configurationManager]
+ -[MOTemplateStore configurationManager]
+ -[MOTemplateStore initWithPersistenceManager:configurationManager:]
+ -[MOTemplateStore initWithPersistenceManager:configurationManager:]
+ -[MOTemplateStore reset]
+ -[MOTemplateStore reset]
+ -[MOTemplateStore setConfigurationManager:]
+ -[MOTemplateStore setConfigurationManager:]
+ GCC_except_table106
+ GCC_except_table15
+ GCC_except_table20
+ GCC_except_table24
+ GCC_except_table3
+ GCC_except_table30
+ GCC_except_table36
+ GCC_except_table51
+ OBJC_IVAR_$_MOBundleContentExtractor._configurationManager
+ OBJC_IVAR_$_MOEventBundleRanking._isInternalBuild
+ OBJC_IVAR_$_MOEventWorkout._isIndoors
+ OBJC_IVAR_$_MOTemplate._promptVersion
+ OBJC_IVAR_$_MOTemplateStore._configurationManager
+ _MOWorkoutMetaDataKeyIsIndoors
+ _MOWorkoutMetaDataKeyIsIndoors
+ _OBJC_CLASS_$_NSBatchDeleteRequest
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.82
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.82
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke_2.cold.1
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke_2.cold.1
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1216
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1216
+ __55-[MOTemplateStore loadNewTemplatesFromFileWithHandler:]_block_invoke.102
+ __55-[MOTemplateStore loadNewTemplatesFromFileWithHandler:]_block_invoke.102
+ __55-[MOTemplateStore loadNewTemplatesFromFileWithHandler:]_block_invoke.102.cold.1
+ __55-[MOTemplateStore loadNewTemplatesFromFileWithHandler:]_block_invoke.102.cold.1
+ __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.937
+ __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.937
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
+ ___105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke_2
+ ___105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke_2
+ ___139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke
+ ___139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke
+ ___24-[MOTemplateStore reset]_block_invoke
+ ___24-[MOTemplateStore reset]_block_invoke
+ ___34-[MOEventBundle _allResourcesImpl]_block_invoke
+ ___34-[MOEventBundle _allResourcesImpl]_block_invoke
+ ___41-[MOEventBundle withResourcesUsingBlock:]_block_invoke
+ ___41-[MOEventBundle withResourcesUsingBlock:]_block_invoke
+ ___62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke_4
+ ___62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke_4
+ ___64-[MOBundleContentExtractor _filterExtractedBundles:withHandler:]_block_invoke
+ ___64-[MOBundleContentExtractor _filterExtractedBundles:withHandler:]_block_invoke
+ ___65-[MOEventBundleRanking _fillDistincnessInfoForRanking:forBundle:]_block_invoke
+ ___65-[MOEventBundleRanking _fillDistincnessInfoForRanking:forBundle:]_block_invoke
+ ___block_descriptor_32_e32_v16?0"NSManagedObjectContext"8l
+ ___block_descriptor_32_e32_v16?0"NSManagedObjectContext"8l
+ ___block_descriptor_40_e8_32r_e24_v24?0"MOResource"8^B16lr32l8
+ ___block_descriptor_40_e8_32r_e24_v24?0"MOResource"8^B16lr32l8
+ ___block_descriptor_40_e8_32s_e24_v24?0"MOResource"8^B16ls32l8
+ ___block_descriptor_40_e8_32s_e24_v24?0"MOResource"8^B16ls32l8
+ ___block_descriptor_48_e8_32bs40r_e27_v32?0"MOResource"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32bs40r_e27_v32?0"MOResource"8Q16^B24ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls48l8s32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e24_v24?0"MOResource"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48s_e24_v24?0"MOResource"8^B16ls32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56bs64w_e29_v24?0"NSArray"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56bs64w_e29_v24?0"NSArray"8"NSError"16lw64l8s56l8s32l8s40l8s48l8
+ ___block_descriptor_81_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_81_e8_32s40s48s56bs64w_e5_v8?0lw64l8s32l8s40l8s48l8s56l8
+ __block_literal_global.1332
+ __block_literal_global.1332
+ _kEventResourcePatternWorkoutIsIndoors
+ _kEventResourcePatternWorkoutIsIndoors
+ _kRejectedByVisitHeuristicsFilter
+ _kRejectedByVisitHeuristicsFilter
+ _kSuggestionAcceptThreshold
+ _kSuggestionAcceptThreshold
+ _kSuggestionRecommendThreshold
+ _kSuggestionRecommendThreshold
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_msgSend$_allResourcesImpl
+ _objc_msgSend$_extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:
+ _objc_msgSend$_filterExtractedBundles:withHandler:
+ _objc_msgSend$defaultsManager
+ _objc_msgSend$executeRequest:error:
+ _objc_msgSend$getDedupeKeyForResourceData:type:error:
+ _objc_msgSend$getDictionaryForData:error:
+ _objc_msgSend$initWithFetchRequest:
+ _objc_msgSend$initWithPersistenceManager:configurationManager:
+ _objc_msgSend$promptVersion
+ _objc_msgSend$result
+ _objc_msgSend$setPersonalizedSensingFilter:
+ _objc_msgSend$setPersonalizedSensingVisitsAllowed:
+ _objc_msgSend$setPromptVersion:
+ _objc_msgSend$setResultType:
+ _objc_msgSend$setSkipLocalization:
+ _objc_msgSend$withResourcesUsingBlock:
+ _thirdPartyMediaSubtypeVariants
+ _thirdPartyMediaSubtypeVariants
- -[MOBundleContentExtractor _extractContentsFromBundlesWithHandler:]
- -[MOBundleContentExtractor _extractContentsFromBundlesWithHandler:]
- -[MOBundleContentExtractor _shouldFilterBundle:]
- -[MOBundleContentExtractor _shouldFilterBundle:]
- -[MOBundleContentExtractor init]
- -[MOBundleContentExtractor init]
- -[MOBundleContentExtractor init].cold.1
- -[MOBundleContentExtractor init].cold.1
- -[MOContextDefaultsManager .cxx_destruct]
- -[MOContextDefaultsManager .cxx_destruct]
- -[MOContextDefaultsManager initWithSuiteName:]
- -[MOContextDefaultsManager initWithSuiteName:]
- -[MOContextDefaultsManager userDefaults]
- -[MOContextDefaultsManager userDefaults]
- -[MOResource getDictionary].cold.1
- -[NSMutableArray(MOExtensions) shuffleArray]
- -[NSMutableArray(MOExtensions) shuffleArray]
- /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/NSMutableArray+MOExtensions.o
- /Library/Caches/com.apple.xbs/Sources/Moments/PersonalizedSensingService/Core/Extensions/
- GCC_except_table102
- GCC_except_table14
- GCC_except_table21
- GCC_except_table33
- GCC_except_table48
- NSMutableArray+MOExtensions.m
- OBJC_IVAR_$_MOContextDefaultsManager._userDefaults
- __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.72
- __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.72
- __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.cold.1
- __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.cold.1
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1159
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1159
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1159.cold.1
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1159.cold.1
- __49-[MOTemplateStore removeAllTemplatesWithHandler:]_block_invoke.cold.1
- __49-[MOTemplateStore removeAllTemplatesWithHandler:]_block_invoke.cold.1
- __55-[MOTemplateStore loadNewTemplatesFromFileWithHandler:]_block_invoke.98
- __55-[MOTemplateStore loadNewTemplatesFromFileWithHandler:]_block_invoke.98
- __55-[MOTemplateStore loadNewTemplatesFromFileWithHandler:]_block_invoke.98.cold.1
- __55-[MOTemplateStore loadNewTemplatesFromFileWithHandler:]_block_invoke.98.cold.1
- __67-[MOBundleContentExtractor _extractContentsFromBundlesWithHandler:]_block_invoke.1205
- __67-[MOBundleContentExtractor _extractContentsFromBundlesWithHandler:]_block_invoke.1205
- __67-[MOBundleContentExtractor _extractContentsFromBundlesWithHandler:]_block_invoke.1205.cold.1
- __67-[MOBundleContentExtractor _extractContentsFromBundlesWithHandler:]_block_invoke.1205.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1103
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1103
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1109
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1109
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1110
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1110
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1145
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1145
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSMutableArray_$_MOExtensions
- __OBJC_$_CATEGORY_NSMutableArray_$_MOExtensions
- __OBJC_$_CATEGORY_NSMutableArray_$_MOExtensions
- __OBJC_$_INSTANCE_VARIABLES_MOContextDefaultsManager
- __OBJC_$_INSTANCE_VARIABLES_MOContextDefaultsManager
- __OBJC_$_PROP_LIST_MOContextDefaultsManager
- __OBJC_$_PROP_LIST_MOContextDefaultsManager
- ___66-[MOBundleContentExtractor extractContentsFromBundlesWithHandler:]_block_invoke_2
- ___66-[MOBundleContentExtractor extractContentsFromBundlesWithHandler:]_block_invoke_2
- ___67-[MOBundleContentExtractor _extractContentsFromBundlesWithHandler:]_block_invoke
- ___67-[MOBundleContentExtractor _extractContentsFromBundlesWithHandler:]_block_invoke
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40r48r_e29_v24?0"NSArray"8"NSError"16lr40l8r48l8s32l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s40l8r56l8s32l8
- ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0lr48l8s40l8r56l8s32l8
- __block_literal_global.1324
- __block_literal_global.1324
- _arc4random_uniform
- _objc_msgSend$_extractContentsFromBundlesWithHandler:
- _objc_msgSend$_shouldFilterBundle:
- _objc_msgSend$allResources
- _objc_msgSend$arrayByAddingObjectsFromArray:
- _objc_msgSend$exchangeObjectAtIndex:withObjectAtIndex:
- _objc_msgSend$isFiltered
CStrings:
+ "\t"
+ "#bundlecuration, bundle selected and content is queued to generate prompts: %!@(MISSING)"
+ "#bundlecuration, filtered bundle. reason: coarse granularity summary.bundleID %!@(MISSING), interfaceType %!l(MISSING)u, subType %!l(MISSING)u, summarizationGranularity %!l(MISSING)u"
+ "#bundlecuration, prune bundle containing only subset of other content metadata %!@(MISSING)"
+ "%!@(MISSING), delete request, %!@(MISSING), template results count, %!@(MISSING), error, %!@(MISSING)"
+ "@24@0:8^@16"
+ "@32@0:8@16^@24"
+ "@40@0:8@16Q24^@32"
+ "Dedupe key not available for this type, %!@(MISSING)."
+ "GEOPOICategoryBowling"
+ "GEOPOICategoryGolf"
+ "GEOPOICategoryMiniGolf"
+ "GEOPOICategoryPlanetarium"
+ "LocalTemplateVersion"
+ "MOTemplateBuilder:generate context hit error"
+ "MOTemplateStore:load new templates hit error"
+ "MOWorkoutMetaDataKeyIsIndoors"
+ "Malformed dictionary, %!@(MISSING), for resource type, %!@(MISSING), the key %!@(MISSING) is missing."
+ "Malformed dictionary, %!@(MISSING), for resource type, %!@(MISSING), the one of the keys %!@(MISSING), %!@(MISSING), %!@(MISSING) is missing."
+ "NumberOfWeeksForFetchBundle"
+ "TB,N,V_isIndoors"
+ "TB,R,N,V_isInternalBuild"
+ "TQ,N,V_promptVersion"
+ "Template_Version"
+ "Unable to deserialize data to dictionary, %!@(MISSING)"
+ "Using for the dedupe key the dictionary, %!@(MISSING)"
+ "Using for the dedupe key the map item handler , %!l(MISSING)u"
+ "Using for the dedupe key, %!@(MISSING)"
+ "XPCCreateBundleContent"
+ "XPCCreateBundleContent"
+ "_allResourcesImpl"
+ "_extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:"
+ "_filterExtractedBundles:withHandler:"
+ "_isIndoors"
+ "_isInternalBuild"
+ "_promptVersion"
+ "executeRequest:error:"
+ "getDedupeKeyError:"
+ "getDedupeKeyForResourceData:type:error:"
+ "getDictionaryForData:error:"
+ "initWithFetchRequest:"
+ "initWithPersistenceManager:configurationManager:"
+ "isIndoors"
+ "isIndoors"
+ "kEventResourcePatternWorkoutIsIndoors"
+ "kRejectedByVisitHeuristicsFilter"
+ "prompt version: %!l(MISSING)u"
+ "promptVersion"
+ "promptVersion"
+ "resource data dictionary , %!@(MISSING)"
+ "result"
+ "setIsIndoors:"
+ "setPersonalizedSensingFilter:"
+ "setPersonalizedSensingVisitsAllowed:"
+ "setPromptVersion:"
+ "setResultType:"
+ "setSkipLocalization:"
+ "skip removing old templates and loading new templates"
+ "suggestionAcceptThreshold"
+ "suggestionRecommendThreshold"
+ "templateVersion"
+ "v24@?0@\"MOResource\"8^B16"
+ "v32@?0@\"MOResource\"8Q16^B24"
+ "v60@0:8@16@24Q32B40@44@?52"
+ "withResourcesUsingBlock:"
- "\b"
- "#bundlecuration, filtered bundle, reason UIrejected, id, %!@(MISSING), suggestion id, %!@(MISSING), label, %!@(MISSING)"
- "#bundlecuration, filtered bundle, reason work place, id, %!@(MISSING), suggestion id, %!@(MISSING), label, %!@(MISSING)"
- "#bundlecuration, filtered cluster bundle, reason clusterMetadata.isFiltered, bundleId %!@(MISSING), suggestionId %!@(MISSING), bundleSubType %!l(MISSING)u, label, %!@(MISSING)"
- "#bundlecuration, filtered cluster bundle, reason unsupported subtype, bundleId %!@(MISSING), suggestionId %!@(MISSING), bundleSubType %!l(MISSING)u, label, %!@(MISSING)"
- "#bundlededuping, subsumed bundle %!@(MISSING)"
- "MOActivityForPersonalizedSensing"
- "_extractContentsFromBundlesWithHandler:"
- "_shouldFilterBundle:"
- "arrayByAddingObjectsFromArray:"
- "exchangeObjectAtIndex:withObjectAtIndex:"
- "fetched eventBundle goodness score, %!f(MISSING)"
- "shuffleArray"
- "templates deletion operation error, %!@(MISSING)"
- "trying to remove templates count %!l(MISSING)u"

```
