## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_floatobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 308.0.3.0.0
-  __TEXT.__text: 0x7a718
+  __TEXT.__text: 0x79a94
   __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0xb640
+  __TEXT.__objc_stubs: 0xb600
   __TEXT.__objc_methlist: 0x72ac
   __TEXT.__objc_classname: 0x849
   __TEXT.__objc_methtype: 0x1116
-  __TEXT.__cstring: 0xbff2
-  __TEXT.__objc_methname: 0x12f4c
+  __TEXT.__cstring: 0xbaad
+  __TEXT.__objc_methname: 0x12f3f
   __TEXT.__const: 0x510
   __TEXT.__gcc_except_tab: 0xe4c
   __TEXT.__oslogstring: 0x76be
   __TEXT.__ustring: 0x10c
-  __TEXT.__unwind_info: 0x1a70
+  __TEXT.__unwind_info: 0x1a60
   __DATA_CONST.__auth_got: 0x440
-  __DATA_CONST.__got: 0x538
+  __DATA_CONST.__got: 0x530
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x32f0
-  __DATA_CONST.__cfstring: 0xfb80
+  __DATA_CONST.__cfstring: 0xf860
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_floatobj: 0x1c0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xc1f8
-  __DATA.__objc_selrefs: 0x3b50
+  __DATA.__objc_selrefs: 0x3b40
   __DATA.__objc_ivar: 0x9a8
   __DATA.__objc_data: 0x1d60
   __DATA.__data: 0x4e0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   Functions: 2665
-  Symbols:   7107
-  CStrings:  5423
+  Symbols:   7104
+  CStrings:  5425
 
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
- _objc_msgSend$currentHandler
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
- _objc_msgSend$pCountMaxNormalized
- _objc_msgSend$pCountWeightedAverageNormalized
- _objc_msgSend$pCountWeightedSumNormalized
- _objc_msgSend$setPCountMaxNormalized:
- _objc_msgSend$setPCountWeightedAverageNormalized:
- _objc_msgSend$setPCountWeightedSumNormalized:
Functions:
~ -[MODefaultsManager objectForKey:] : 352 -> 264
~ -[MODefaultsManager objectForKeyWithoutLog:] : 276 -> 176
~ -[MODefaultsManager deleteObjectForKey:] : 368 -> 288
~ -[MODefaultsManager setObject:forKey:] : 400 -> 312
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 224 -> 104
~ -[MOEventBundleLabelFormat initWithFormat:capitalizationType:] : 264 -> 200
~ +[MODictionaryEncoder encodeDictionary:] : 420 -> 328
~ +[MODictionaryEncoder decodeToDictionary:] : 420 -> 328
~ -[MOResource initWithIdentifier:] : 256 -> 176
~ +[MOPlatformInfo isSeedBuild] : 8 -> 120
~ -[MOEvent initWithEventIdentifier:startDate:endDate:creationDate:provider:category:] : 724 -> 480
~ -[MOEvent formatAddressWithFormatOption:] : 224 -> 124
~ -[MOEvent formatLocalityWithFormatOption:] : 224 -> 124
~ -[MOEvent formatAdministrativeAreaWithFormatOption:] : 224 -> 124
~ -[MOEvent formatCountryWithFormatOption:] : 224 -> 124
~ -[MOAction initWithIdentifier:] : 248 -> 160
~ -[MOEventBundleLabelTemplate initWithConditionStrings:labels:context:] : 344 -> 280
~ -[MOEventBundleLabelTemplate initWithConditions:labels:context:] : 508 -> 444
~ -[MOEventBundleLabelTemplate initWithConditions:formats:context:] : 320 -> 256
~ -[MOEventBundle initWithBundleIdentifier:suggestionID:startDate:endDate:creationDate:] : 832 -> 528
~ -[MOEventBundle dateInterval] : 600 -> 500
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:withTable:] : 736 -> 668
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringWithFormat:arguments:] : 976 -> 904
~ -[MOTime initWithIdentifier:] : 268 -> 180
~ -[MOPlace initWithIdentifier:] : 276 -> 196
~ -[MOEventBundleRanking initWithUniverse:] : 240 -> 168
~ -[MOEventBundleRanking initWithConfigurationManager:] : 17488 -> 17424
~ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:] : 32696 -> 32560
~ -[MOEventBundleRanking _mergeScoresToBundles:usingScore:] : 1792 -> 1684
~ -[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:] : 9656 -> 9532
~ -[MOEventBundleRanking updateTripMetaDataForRank:] : 1260 -> 1088
~ -[MOStringArrayTransformer transformedValue:] : 400 -> 300
~ -[MOStringArrayTransformer reverseTransformedValue:] : 364 -> 264
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
