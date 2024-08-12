## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-190.0.0.0.0
-  __TEXT.__text: 0x65ca0
+202.0.2.0.0
+  __TEXT.__text: 0x6680c
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_stubs: 0xa960
-  __TEXT.__objc_methlist: 0x693c
+  __TEXT.__objc_stubs: 0xa9a0
+  __TEXT.__objc_methlist: 0x694c
   __TEXT.__objc_classname: 0x827
   __TEXT.__objc_methtype: 0xf8b
-  __TEXT.__cstring: 0xb260
-  __TEXT.__objc_methname: 0x114a4
+  __TEXT.__cstring: 0xb2de
+  __TEXT.__objc_methname: 0x114d9
   __TEXT.__const: 0x470
-  __TEXT.__gcc_except_tab: 0xb7c
-  __TEXT.__oslogstring: 0x6920
+  __TEXT.__gcc_except_tab: 0xbc0
+  __TEXT.__oslogstring: 0x6a6c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1108
+  __TEXT.__unwind_info: 0x1128
   __DATA_CONST.__auth_got: 0x460
   __DATA_CONST.__got: 0x518
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2d30
-  __DATA_CONST.__cfstring: 0xe400
+  __DATA_CONST.__const: 0x2d70
+  __DATA_CONST.__cfstring: 0xe4c0
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xbb60
-  __DATA.__objc_selrefs: 0x3618
+  __DATA.__objc_selrefs: 0x3628
   __DATA.__objc_ivar: 0x8fc
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x4c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 2427
-  Symbols:   18452
-  CStrings:  5417
+  Functions: 2443
+  Symbols:   18550
+  CStrings:  5435
 
Symbols:
+ -[MOBundleContentExtractor _addContentRatingForSongTitleAndArtistSuggestions:].cold.2
+ -[MOBundleContentExtractor _addContentRatingForSongTitleAndArtistSuggestions:].cold.2
+ -[MOBundleContentExtractor _extractDictionaryFromBundle:].cold.1
+ -[MOBundleContentExtractor _extractDictionaryFromBundle:].cold.1
+ -[MOBundleContentExtractor _extractPersonsFromBundle:].cold.1
+ -[MOBundleContentExtractor _extractPersonsFromBundle:].cold.1
+ -[MOBundleContentExtractor _fetchEventBundlesWithStartDate:EndDate:SignificantLocationEnabled:Handler:].cold.1
+ -[MOContextManager _addMetaDataToContext:bundleContent:].cold.1
+ -[MOContextManager _addMetaDataToContext:bundleContent:].cold.1
+ -[MOContextManager _addMetaDataToContext:bundleContent:].cold.2
+ -[MOContextManager _addMetaDataToContext:bundleContent:].cold.2
+ -[MOContextManager _addMetaDataToContext:bundleContent:].cold.3
+ -[MOContextManager _addMetaDataToContext:bundleContent:].cold.3
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.7
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.7
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.8
+ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:].cold.8
+ -[MOTemplateBasedContextBuilder _computeTemplateScore:withBundleContent:].cold.1
+ -[MOTemplateBasedContextBuilder _computeTemplateScore:withBundleContent:].cold.1
+ -[MOTemplateBasedContextBuilder _readTemplatesToRemovePlistFile:].cold.3
+ -[MOTemplateBasedContextBuilder _readTemplatesToRemovePlistFile:].cold.3
+ -[MOTemplateBasedContextBuilder _readTemplatesToRemovePlistFile:].cold.4
+ -[MOTemplateBasedContextBuilder _readTemplatesToRemovePlistFile:].cold.4
+ -[MOTemplateStore checkTemplateStoreIsEmptyWithHandler:]
+ -[MOTemplateStore checkTemplateStoreIsEmptyWithHandler:]
+ GCC_except_table22
+ _MOTemplateBasedMusicMoodsChillVariant1
+ _MOTemplateBasedMusicMoodsChillVariant1
+ _MOTemplateBasedMusicMoodsChillVariant2
+ _MOTemplateBasedMusicMoodsChillVariant2
+ _MOTemplateBasedMusicMoodsDreamyVariant1
+ _MOTemplateBasedMusicMoodsDreamyVariant1
+ _MOTemplateBasedMusicMoodsDreamyVariant2
+ _MOTemplateBasedMusicMoodsDreamyVariant2
+ _MOTemplateBasedMusicMoodsEpicVariant1
+ _MOTemplateBasedMusicMoodsEpicVariant1
+ _MOTemplateBasedMusicMoodsEpicVariant2
+ _MOTemplateBasedMusicMoodsEpicVariant2
+ _MOTemplateBasedMusicMoodsHappyVariant1
+ _MOTemplateBasedMusicMoodsHappyVariant1
+ _MOTemplateBasedMusicMoodsHappyVariant2
+ _MOTemplateBasedMusicMoodsHappyVariant2
+ _MOTemplateBasedMusicMoodsSentimentalVariant1
+ _MOTemplateBasedMusicMoodsSentimentalVariant1
+ _MOTemplateBasedMusicMoodsSentimentalVariant2
+ _MOTemplateBasedMusicMoodsSentimentalVariant2
+ _MOTemplateBasedMusicMoodsUpliftingVariant1
+ _MOTemplateBasedMusicMoodsUpliftingVariant1
+ _MOTemplateBasedMusicMoodsUpliftingVariant2
+ _MOTemplateBasedMusicMoodsUpliftingVariant2
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.101
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.101
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.96
+ __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.96
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1234
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1234
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.cold.1
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.cold.1
+ __56-[MOTemplateStore checkTemplateStoreIsEmptyWithHandler:]_block_invoke.cold.1
+ __56-[MOTemplateStore checkTemplateStoreIsEmptyWithHandler:]_block_invoke.cold.1
+ __98-[MOTemplateBasedContextBuilder _generateContextStringsFromTemplateWithBundleContent:withHandler:]_block_invoke.76
+ __98-[MOTemplateBasedContextBuilder _generateContextStringsFromTemplateWithBundleContent:withHandler:]_block_invoke.76
+ ___56-[MOTemplateStore checkTemplateStoreIsEmptyWithHandler:]_block_invoke
+ ___56-[MOTemplateStore checkTemplateStoreIsEmptyWithHandler:]_block_invoke
+ ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8ls32l8r40l8r48l8
+ ___block_descriptor_56_e8_32s40r48r_e17_v16?0"NSError"8ls32l8r40l8r48l8
+ ___block_descriptor_72_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e61_v40?0"NSArray"8"NSError"16"MOClientRequest"24"NSArray"32ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e61_v40?0"NSArray"8"NSError"16"MOClientRequest"24"NSArray"32ls32l8s40l8s48l8s56l8s64l8
+ __block_literal_global.1350
+ __block_literal_global.1350
+ _objc_msgSend$checkTemplateStoreIsEmptyWithHandler:
+ _objc_msgSend$setFetchLimit:
- _MOTemplateBasedMusicMoodsChill
- _MOTemplateBasedMusicMoodsChill
- _MOTemplateBasedMusicMoodsDreamy
- _MOTemplateBasedMusicMoodsDreamy
- _MOTemplateBasedMusicMoodsEpic
- _MOTemplateBasedMusicMoodsEpic
- _MOTemplateBasedMusicMoodsGentle
- _MOTemplateBasedMusicMoodsGentle
- _MOTemplateBasedMusicMoodsHappy
- _MOTemplateBasedMusicMoodsHappy
- _MOTemplateBasedMusicMoodsUplifting
- _MOTemplateBasedMusicMoodsUplifting
- __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.82
- __105-[MOTemplateBasedContextBuilder _generateContextStringsBasedOnNewTemplateFromBundleContents:WithHandler:]_block_invoke.82
- __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1219
- __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1219
- __98-[MOTemplateBasedContextBuilder _generateContextStringsFromTemplateWithBundleContent:withHandler:]_block_invoke.58
- __98-[MOTemplateBasedContextBuilder _generateContextStringsFromTemplateWithBundleContent:withHandler:]_block_invoke.58
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8ls32l8r40l8
- ___block_descriptor_64_e8_32s40s48s56bs_e61_v40?0"NSArray"8"NSError"16"MOClientRequest"24"NSArray"32ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s56bs_e61_v40?0"NSArray"8"NSError"16"MOClientRequest"24"NSArray"32ls32l8s40l8s48l8s56l8
- __block_literal_global.1335
- __block_literal_global.1335
- _kMOContextAnalyticsHasMusicMood
- _kMOContextAnalyticsHasMusicMood
- _kMOContextAnalyticsPromptID
- _kMOContextAnalyticsPromptID
- _kMOContextAnalyticsPromptTemplateIndex
- _kMOContextAnalyticsPromptTemplateIndex
CStrings:
+ " enableTelemetry=YES "
+ "%!@(MISSING), request, %!@(MISSING), checkTemplateStoreIsEmptyWithHandler, template results count, %!l(MISSING)u, error, %!@(MISSING)"
+ ", with a chill song"
+ ", with a dreamy song"
+ ", with a happy song"
+ ", with a sentimental song"
+ ", with an epic song"
+ ", with an uplifting song"
+ ", with chill music"
+ ", with dreamy music"
+ ", with epic music"
+ ", with happy music"
+ ", with sentimental music"
+ ", with the song %!@(MISSING)"
+ ", with the song %!@(MISSING) by %!@(MISSING)"
+ ", with uplifting music"
+ "XPCFetchContexts"
+ "XPCFetchContexts"
+ "XPCNotifyFeedback"
+ "XPCNotifyFeedback"
+ "XPCRequestDBAccess"
+ "XPCRequestDBAccess"
+ "bundle Content Identifier, %!@(MISSING), associated bundleID, %!@(MISSING), associated suggestionID, %!@(MISSING), bundleType %!l(MISSING)d, placeType %!l(MISSING)d, activityType %!l(MISSING)d, photoTrait %!l(MISSING)d, peopleClassification %!l(MISSING)d, hasPersonName %!d(MISSING), hasPlaceName %!d(MISSING), hasCityName %!d(MISSING), hasTimeReference %!d(MISSING), patternType %!l(MISSING)d"
+ "checkTemplateStoreIsEmpty,  %!d(MISSING)"
+ "checkTemplateStoreIsEmptyWithHandler:"
+ "diversityCoefficientDict:%!@(MISSING)"
+ "fetch template hit error when trying to identify if DB is empty, %!@(MISSING)"
+ "local template version: %!f(MISSING)"
+ "no template found for this bundle content with bundle ID %!@(MISSING)"
+ "setFetchLimit:"
+ "v12@?0B8"
+ "visibleInterfaceTypeAndCountDict:%!@(MISSING)"
- ", playing \"%!@(MISSING)\""
- ", playing \"%!@(MISSING)\" by %!@(MISSING)"
- ", playing chill music"
- ", playing dreamy music"
- ", playing epic music"
- ", playing gentle music"
- ", playing happy music"
- ", playing uplifting music"
- "bundle Content Identifier, %!@(MISSING), associated bundleID, %!@(MISSING), associated suggestionID, %!@(MISSING), suggestion label, %!@(MISSING), bundleType %!l(MISSING)d, placeType %!l(MISSING)d, activityType %!l(MISSING)d, photoTrait %!l(MISSING)d, peopleClassification %!l(MISSING)d, hasPersonName %!d(MISSING), hasPlaceName %!d(MISSING), hasCityName %!d(MISSING), hasTimeReference %!d(MISSING), patternType %!l(MISSING)d"
- "hasMusicMood"
- "json file, %!@(MISSING)"
- "no template found for this bundle content with bundle ID %!@(MISSING) with label %!@(MISSING)"
- "promptID"
- "promptTemplateIndex"

```
