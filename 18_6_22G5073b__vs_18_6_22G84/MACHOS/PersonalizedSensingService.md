## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 206.0.7.0.0
-  __TEXT.__text: 0x690ec
+  __TEXT.__text: 0x6842c
   __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__objc_stubs: 0xad00
+  __TEXT.__objc_stubs: 0xacc0
   __TEXT.__objc_methlist: 0x6db0
   __TEXT.__objc_classname: 0x848
   __TEXT.__objc_methtype: 0xfe8
-  __TEXT.__cstring: 0xb745
-  __TEXT.__objc_methname: 0x11b62
+  __TEXT.__cstring: 0xb152
+  __TEXT.__objc_methname: 0x11b55
   __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0xbe0
   __TEXT.__oslogstring: 0x6d58
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1198
+  __TEXT.__unwind_info: 0x1190
   __DATA_CONST.__auth_got: 0x480
-  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__got: 0x530
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2f50
-  __DATA_CONST.__cfstring: 0xecc0
+  __DATA_CONST.__cfstring: 0xe940
   __DATA_CONST.__objc_classlist: 0x2e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xbd00
-  __DATA.__objc_selrefs: 0x37c0
+  __DATA.__objc_selrefs: 0x37b0
   __DATA.__objc_ivar: 0x938
   __DATA.__objc_data: 0x1d10
   __DATA.__data: 0x4c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 2858E157-0B22-3AFE-B4CC-4E51C3552680
+  UUID: A3CB7D6C-CA34-355F-ABF2-6BD23B0C1138
   Functions: 2497
-  Symbols:   19015
-  CStrings:  7450
+  Symbols:   19012
+  CStrings:  7392
 
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
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1161
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1163
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1163.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1113
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1119
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1124
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1149
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
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1180
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1182
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1182.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1132
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1133
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1137
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1168
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
~ -[MOPublicEvent initWithEventDictionary:] : 304 -> 244
~ -[MOEventExtendedAttributes initWithLocalIdentifier:] : 248 -> 172
~ -[MOEventBundleLabelFormat initWithFormat:capitalizationType:] : 268 -> 200
~ +[MODictionaryEncoder encodeDictionary:] : 408 -> 320
~ +[MODictionaryEncoder decodeToDictionary:] : 408 -> 320
~ -[MOResource initWithIdentifier:] : 244 -> 168
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
~ -[MOPlace initWithIdentifier:] : 264 -> 188
~ -[MOEventBundleRanking initWithUniverse:] : 228 -> 160
~ -[MOEventBundleRanking initWithConfigurationManager:] : 15244 -> 15184
~ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:] : 23968 -> 23788
~ -[MOEventBundleRanking _mergeScoresToBundles:usingScore:] : 1536 -> 1424
~ -[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:] : 8772 -> 8660
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
