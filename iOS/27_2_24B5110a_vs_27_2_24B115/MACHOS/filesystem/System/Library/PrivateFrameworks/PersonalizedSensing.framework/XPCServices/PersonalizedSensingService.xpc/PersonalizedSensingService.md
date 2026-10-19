## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 502.0.8.0.0
-  __TEXT.__text: 0x1329cc
+  __TEXT.__text: 0x132220
   __TEXT.__auth_stubs: 0x2490
-  __TEXT.__objc_stubs: 0xb240
+  __TEXT.__objc_stubs: 0xb200
   __TEXT.__objc_methlist: 0x6c10
   __TEXT.__objc_classname: 0x1555
   __TEXT.__objc_methtype: 0xf8b
-  __TEXT.__cstring: 0xeff0
-  __TEXT.__objc_methname: 0x135fa
+  __TEXT.__cstring: 0xecf0
+  __TEXT.__objc_methname: 0x1360a
   __TEXT.__const: 0x514e
   __TEXT.__gcc_except_tab: 0xd3c
   __TEXT.__oslogstring: 0xbf85

   __TEXT.__unwind_info: 0x47c8
   __TEXT.__eh_frame: 0x411c
   __DATA_CONST.__const: 0x9dc1
-  __DATA_CONST.__cfstring: 0xecc0
+  __DATA_CONST.__cfstring: 0xeae0
   __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_floatobj: 0x1c0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x1260
-  __DATA_CONST.__got: 0xd00
+  __DATA_CONST.__got: 0xcf8
   __DATA_CONST.__auth_ptr: 0x9b0
   __DATA.__objc_const: 0xe948
-  __DATA.__objc_selrefs: 0x3c50
+  __DATA.__objc_selrefs: 0x3c40
   __DATA.__objc_ivar: 0x904
   __DATA.__objc_data: 0x3850
   __DATA.__data: 0x3380

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 5767
-  Symbols:   15609
-  CStrings:  6083
+  Symbols:   15606
+  CStrings:  6085
 
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
~ -[MODefaultsManager objectForKey:] : 320 -> 236
~ -[MODefaultsManager objectForKeyWithoutLog:] : 248 -> 152
~ -[MODefaultsManager deleteObjectForKey:] : 312 -> 236
~ -[MODefaultsManager setObject:forKey:] : 348 -> 264
~ -[MODefaultsManager setObjectWithoutLog:forKey:] : 204 -> 88
~ -[MOEventBundleLabelFormat initWithFormat:capitalizationType:] : 268 -> 200
~ +[MODictionaryEncoder encodeDictionary:] : 396 -> 308
~ +[MODictionaryEncoder decodeToDictionary:] : 396 -> 308
~ -[MOResource initWithIdentifier:] : 248 -> 172
~ +[MOPlatformInfo isSeedBuild] : 8 -> 112
~ -[MOEventBundleLabelTemplate initWithConditionStrings:labels:context:] : 336 -> 276
~ -[MOEventBundleLabelTemplate initWithConditions:labels:context:] : 520 -> 460
~ -[MOEventBundleLabelTemplate initWithConditions:formats:context:] : 324 -> 264
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringForKey:withTable:] : 656 -> 592
~ +[MOEventBundleLabelLocalizer _Moments_LocalizedStringWithFormat:arguments:] : 940 -> 872
~ -[MOTime initWithIdentifier:] : 288 -> 204
~ -[MOPlace initWithIdentifier:] : 268 -> 192
~ -[MOEventBundleRanking initWithUniverse:] : 232 -> 164
~ -[MOEventBundleRanking initWithConfigurationManager:] : 17140 -> 17080
~ -[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:] : 31352 -> 31256
~ -[MOEventBundleRanking _mergeScoresToBundles:usingScore:] : 1776 -> 1664
~ -[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:] : 8980 -> 8852
~ -[MOEventBundleRanking updateTripMetaDataForRank:] : 1200 -> 1036
~ -[MOStringArrayTransformer transformedValue:] : 368 -> 272
~ -[MOStringArrayTransformer reverseTransformedValue:] : 340 -> 244
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
