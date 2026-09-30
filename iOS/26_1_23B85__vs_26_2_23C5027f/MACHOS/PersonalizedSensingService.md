## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-302.0.13.0.0
-  __TEXT.__text: 0x727ac
+304.0.2.0.0
+  __TEXT.__text: 0x733b4
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0xb600
+  __TEXT.__objc_stubs: 0xb640
   __TEXT.__objc_methlist: 0x72ac
   __TEXT.__objc_classname: 0x849
   __TEXT.__objc_methtype: 0x1116
-  __TEXT.__cstring: 0xbaad
-  __TEXT.__objc_methname: 0x12f3f
+  __TEXT.__cstring: 0xbff2
+  __TEXT.__objc_methname: 0x12f4c
   __TEXT.__const: 0x510
   __TEXT.__gcc_except_tab: 0xe80
   __TEXT.__oslogstring: 0x76be
   __TEXT.__ustring: 0x10c
-  __TEXT.__unwind_info: 0x12c0
+  __TEXT.__unwind_info: 0x12d0
   __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__got: 0x538
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x32f0
-  __DATA_CONST.__cfstring: 0xf860
+  __DATA_CONST.__cfstring: 0xfb80
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_floatobj: 0x1c0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xc1f8
-  __DATA.__objc_selrefs: 0x3b40
+  __DATA.__objc_selrefs: 0x3b50
   __DATA.__objc_ivar: 0x9a8
   __DATA.__objc_data: 0x1d60
   __DATA.__data: 0x4e0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 4700F140-D681-3E27-91BA-CE3C51091330
+  UUID: B991D8B0-D7A0-3D7F-84F5-41BB3F0B6D5C
   Functions: 2651
-  Symbols:   20041
-  CStrings:  7837
+  Symbols:   20044
+  CStrings:  7889
 
Symbols:
+ -[MOEventBundleRankingInput pCountMaxNormalized]
+ -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput pCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
+ _OBJC_CLASS_$_NSAssertionHandler
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.772
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.711
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.714
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.715
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.729
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.730
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.758
+ _objc_msgSend$currentHandler
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$pCountMaxNormalized
+ _objc_msgSend$pCountWeightedAverageNormalized
+ _objc_msgSend$pCountWeightedSumNormalized
+ _objc_msgSend$setPCountMaxNormalized:
+ _objc_msgSend$setPCountWeightedAverageNormalized:
+ _objc_msgSend$setPCountWeightedSumNormalized:
- -[MOEventBundleRankingInput peopleCountMaxNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.756
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.758
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.758.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.693
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.693.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.697
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.697.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.701
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.704
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.705
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.709
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.720
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.742
- _objc_msgSend$peopleCountMaxNormalized
- _objc_msgSend$peopleCountWeightedAverageNormalized
- _objc_msgSend$peopleCountWeightedSumNormalized
- _objc_msgSend$setPeopleCountMaxNormalized:
- _objc_msgSend$setPeopleCountWeightedAverageNormalized:
- _objc_msgSend$setPeopleCountWeightedSumNormalized:
Functions:
~ -[MODefaultsManager objectForKey:] : 248 -> 332
~ -[MODefaultsManager objectForKeyWithoutLog:] : 164 -> 260
~ -[MODefaultsManager deleteObjectForKey:] : 280 -> 356
~ -[MODefaultsManager setObject:forKey:] : 308 -> 392
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 100 -> 216
~ -[MOEventBundleLabelFormat initWithFormat:capitalizationType:] : 200 -> 268
~ +[MODictionaryEncoder encodeDictionary:] : 320 -> 408
~ +[MODictionaryEncoder decodeToDictionary:] : 320 -> 408
~ -[MOResource initWithIdentifier:] : 172 -> 248
~ +[MOPlatformInfo isSeedBuild] : 112 -> 8
~ -[MOEvent initWithEventIdentifier:startDate:endDate:creationDate:provider:category:] : 480 -> 716
~ -[MOEvent formatAddressWithFormatOption:] : 116 -> 212
~ -[MOEvent formatLocalityWithFormatOption:] : 116 -> 212
~ -[MOEvent formatAdministrativeAreaWithFormatOption:] : 116 -> 212
~ -[MOEvent formatCountryWithFormatOption:] : 116 -> 212
~ -[MOAction initWithIdentifier:] : 156 -> 240
~ -[MOEventBundleLabelTemplate initWithConditionStrings:labels:context:] : 276 -> 336
~ -[MOEventBundleLabelTemplate initWithConditions:labels:context:] : 460 -> 520
~ -[MOEventBundleLabelTemplate initWithConditions:formats:context:] : 264 -> 324
~ -[MOEventBundle initWithBundleIdentifier:suggestionID:startDate:endDate:creationDate:] : 524 -> 816
~ -[MOEventBundle dateInterval] : 452 -> 548
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:withTable:] : 648 -> 712
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringWithFormat:arguments:] : 884 -> 952
~ -[MOTime initWithIdentifier:] : 172 -> 256
~ -[MOPlace initWithIdentifier:] : 192 -> 268
~ -[MOEventBundleRanking initWithUniverse:] : 164 -> 232
~ -[MOEventBundleRanking initWithConfigurationManager:] : 16500 -> 16560
~ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:] : 30788 -> 30916
~ -[MOEventBundleRanking _mergeScoresToBundles:usingScore:] : 1648 -> 1752
~ -[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:] : 8872 -> 9000
~ -[MOEventBundleRanking updateTripMetaDataForRank:] : 1036 -> 1200
~ -[MOStringArrayTransformer transformedValue:] : 284 -> 380
~ -[MOStringArrayTransformer reverseTransformedValue:] : 256 -> 352
CStrings:
+ "Tf,N,V_pCountMaxNormalized"
+ "Tf,N,V_pCountWeightedAverageNormalized"
+ "Tf,N,V_pCountWeightedSumNormalized"
+ "_pCountMaxNormalized"
+ "_pCountWeightedAverageNormalized"
+ "_pCountWeightedSumNormalized"
+ "currentHandler"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "setPCountMaxNormalized:"
+ "setPCountWeightedAverageNormalized:"
+ "setPCountWeightedSumNormalized:"
- "PlatformInfoOverrideIsSeedBuild"
- "Tf,N,V_peopleCountMaxNormalized"
- "Tf,N,V_peopleCountWeightedAverageNormalized"
- "Tf,N,V_peopleCountWeightedSumNormalized"
- "_peopleCountMaxNormalized"
- "_peopleCountWeightedAverageNormalized"
- "_peopleCountWeightedSumNormalized"
- "peopleCountMaxNormalized"
- "peopleCountWeightedAverageNormalized"
- "peopleCountWeightedSumNormalized"
- "setPeopleCountMaxNormalized:"
- "setPeopleCountWeightedAverageNormalized:"
- "setPeopleCountWeightedSumNormalized:"

```
