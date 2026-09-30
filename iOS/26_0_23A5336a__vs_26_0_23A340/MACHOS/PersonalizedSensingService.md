## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 297.0.0.0.0
-  __TEXT.__text: 0x72f04
+  __TEXT.__text: 0x722f8
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0xb5c0
+  __TEXT.__objc_stubs: 0xb580
   __TEXT.__objc_methlist: 0x7264
   __TEXT.__objc_classname: 0x83e
   __TEXT.__objc_methtype: 0x1116
-  __TEXT.__cstring: 0xbfe8
-  __TEXT.__objc_methname: 0x12ebe
+  __TEXT.__cstring: 0xbaa3
+  __TEXT.__objc_methname: 0x12eb1
   __TEXT.__const: 0x500
   __TEXT.__gcc_except_tab: 0xe80
   __TEXT.__oslogstring: 0x76be
   __TEXT.__ustring: 0x10c
-  __TEXT.__unwind_info: 0x12c0
+  __TEXT.__unwind_info: 0x12b0
   __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__got: 0x530
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x3280
-  __DATA_CONST.__cfstring: 0xfb40
+  __DATA_CONST.__cfstring: 0xf820
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_floatobj: 0x1c0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xc1f8
-  __DATA.__objc_selrefs: 0x3b20
+  __DATA.__objc_selrefs: 0x3b10
   __DATA.__objc_ivar: 0x9a8
   __DATA.__objc_data: 0x1d60
   __DATA.__data: 0x4d8

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: E37E47EE-F66B-388A-9DB2-9BEAE2E36E5C
+  UUID: C51F4F14-0EC9-3ED9-925E-0B430AFB8390
   Functions: 2641
-  Symbols:   19960
-  CStrings:  7878
+  Symbols:   19957
+  CStrings:  7826
 
Symbols:
+ -[MOEventBundleRankingInput peopleCountMaxNormalized]
+ -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.756
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.758
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.758.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.693
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.693.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.697
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.697.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.701
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.704
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.705
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.709
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.720
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.742
+ _objc_msgSend$peopleCountMaxNormalized
+ _objc_msgSend$peopleCountWeightedAverageNormalized
+ _objc_msgSend$peopleCountWeightedSumNormalized
+ _objc_msgSend$setPeopleCountMaxNormalized:
+ _objc_msgSend$setPeopleCountWeightedAverageNormalized:
+ _objc_msgSend$setPeopleCountWeightedSumNormalized:
- -[MOEventBundleRankingInput pCountMaxNormalized]
- -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput pCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setPCountMaxNormalized:]
- -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
- -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
- _OBJC_CLASS_$_NSAssertionHandler
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.772
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.711
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.714
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.715
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.729
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.730
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.758
- _objc_msgSend$currentHandler
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
- _objc_msgSend$pCountMaxNormalized
- _objc_msgSend$pCountWeightedAverageNormalized
- _objc_msgSend$pCountWeightedSumNormalized
- _objc_msgSend$setPCountMaxNormalized:
- _objc_msgSend$setPCountWeightedAverageNormalized:
- _objc_msgSend$setPCountWeightedSumNormalized:
Functions:
~ -[MODefaultsManager objectForKey:] : 332 -> 248
~ -[MODefaultsManager objectForKeyWithoutLog:] : 260 -> 164
~ -[MODefaultsManager deleteObjectForKey:] : 356 -> 280
~ -[MODefaultsManager setObject:forKey:] : 392 -> 308
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 216 -> 100
~ -[MOEventBundleLabelFormat initWithFormat:capitalizationType:] : 268 -> 200
~ +[MODictionaryEncoder encodeDictionary:] : 408 -> 320
~ +[MODictionaryEncoder decodeToDictionary:] : 408 -> 320
~ -[MOResource initWithIdentifier:] : 248 -> 172
~ +[MOPlatformInfo isSeedBuild] : 8 -> 108
~ -[MOEvent initWithEventIdentifier:startDate:endDate:creationDate:provider:category:] : 716 -> 480
~ -[MOEvent formatAddressWithFormatOption:] : 212 -> 116
~ -[MOEvent formatLocalityWithFormatOption:] : 212 -> 116
~ -[MOEvent formatAdministrativeAreaWithFormatOption:] : 212 -> 116
~ -[MOEvent formatCountryWithFormatOption:] : 212 -> 116
~ -[MOAction initWithIdentifier:] : 240 -> 156
~ -[MOEventBundleLabelTemplate initWithConditionStrings:labels:context:] : 336 -> 276
~ -[MOEventBundleLabelTemplate initWithConditions:labels:context:] : 520 -> 460
~ -[MOEventBundleLabelTemplate initWithConditions:formats:context:] : 324 -> 264
~ -[MOEventBundle initWithBundleIdentifier:suggestionID:startDate:endDate:creationDate:] : 816 -> 524
~ -[MOEventBundle dateInterval] : 548 -> 452
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:withTable:] : 712 -> 648
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringWithFormat:arguments:] : 952 -> 884
~ -[MOTime initWithIdentifier:] : 256 -> 172
~ -[MOPlace initWithIdentifier:] : 268 -> 192
~ -[MOEventBundleRanking initWithUniverse:] : 232 -> 164
~ -[MOEventBundleRanking initWithConfigurationManager:] : 16560 -> 16500
~ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:] : 30916 -> 30788
~ -[MOEventBundleRanking _mergeScoresToBundles:usingScore:] : 1752 -> 1648
~ -[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:] : 9000 -> 8872
~ -[MOEventBundleRanking updateTripMetaDataForRank:] : 1200 -> 1036
~ -[MOStringArrayTransformer transformedValue:] : 380 -> 284
~ -[MOStringArrayTransformer reverseTransformedValue:] : 352 -> 256
CStrings:
+ "PlatformInfoOverrideIsSeedBuild"
+ "Tf,N,V_peopleCountMaxNormalized"
+ "Tf,N,V_peopleCountWeightedAverageNormalized"
+ "Tf,N,V_peopleCountWeightedSumNormalized"
+ "_peopleCountMaxNormalized"
+ "_peopleCountWeightedAverageNormalized"
+ "_peopleCountWeightedSumNormalized"
+ "peopleCountMaxNormalized"
+ "peopleCountWeightedAverageNormalized"
+ "peopleCountWeightedSumNormalized"
+ "setPeopleCountMaxNormalized:"
+ "setPeopleCountWeightedAverageNormalized:"
+ "setPeopleCountWeightedSumNormalized:"
- "Tf,N,V_pCountMaxNormalized"
- "Tf,N,V_pCountWeightedAverageNormalized"
- "Tf,N,V_pCountWeightedSumNormalized"
- "_pCountMaxNormalized"
- "_pCountWeightedAverageNormalized"
- "_pCountWeightedSumNormalized"
- "currentHandler"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "setPCountMaxNormalized:"
- "setPCountWeightedAverageNormalized:"
- "setPCountWeightedSumNormalized:"

```
