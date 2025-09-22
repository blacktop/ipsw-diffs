## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-297.0.0.0.0
-  __TEXT.__text: 0x722f8
+302.0.2.0.0
+  __TEXT.__text: 0x733b4
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0xb580
-  __TEXT.__objc_methlist: 0x7264
-  __TEXT.__objc_classname: 0x83e
+  __TEXT.__objc_stubs: 0xb640
+  __TEXT.__objc_methlist: 0x72ac
+  __TEXT.__objc_classname: 0x849
   __TEXT.__objc_methtype: 0x1116
-  __TEXT.__cstring: 0xbaa3
-  __TEXT.__objc_methname: 0x12eb1
-  __TEXT.__const: 0x500
+  __TEXT.__cstring: 0xbff2
+  __TEXT.__objc_methname: 0x12f4c
+  __TEXT.__const: 0x510
   __TEXT.__gcc_except_tab: 0xe80
   __TEXT.__oslogstring: 0x76be
   __TEXT.__ustring: 0x10c
-  __TEXT.__unwind_info: 0x12b0
+  __TEXT.__unwind_info: 0x12d0
   __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__got: 0x538
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3280
-  __DATA_CONST.__cfstring: 0xf820
+  __DATA_CONST.__const: 0x32f0
+  __DATA_CONST.__cfstring: 0xfb80
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_floatobj: 0x1c0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xc1f8
-  __DATA.__objc_selrefs: 0x3b10
+  __DATA.__objc_selrefs: 0x3b50
   __DATA.__objc_ivar: 0x9a8
   __DATA.__objc_data: 0x1d60
-  __DATA.__data: 0x4d8
-  __DATA.__bss: 0x50
+  __DATA.__data: 0x4e0
+  __DATA.__bss: 0x68
   __DATA.__common: 0x78
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: C51F4F14-0EC9-3ED9-925E-0B430AFB8390
-  Functions: 2641
-  Symbols:   19957
-  CStrings:  7826
+  UUID: 1F6886C4-7FD3-3A93-AAA2-070C31CEF8C1
+  Functions: 2651
+  Symbols:   20044
+  CStrings:  7889
 
Symbols:
+ +[MOPlatformInfo _createDefaultsManagerDaemon]
+ +[MOPlatformInfo _createDefaultsManagerDaemon].cold.1
+ +[MOPlatformInfo _getMainBundleIdentifier]
+ +[MOPlatformInfo _getMainBundleIdentifier].cold.1
+ -[MOEventBundleRankingInput pCountMaxNormalized]
+ -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput pCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
+ -[MOPlace(Comparison) _isString:equalToString:]
+ -[MOPlace(Comparison) isSimilarToPlace:]
+ -[MOPlace(Comparison) isSimilarToPlace:locationThreshold:]
+ -[MOPlace(Comparison) placeKey]
+ /Library/Caches/com.apple.xbs/Binaries/Moments/install/TempContent/Objects/Moments.build/PersonalizedSensingService.build/Objects-normal/arm64e/MOPlace+Comparison.o
+ GCC_except_table18
+ MOPlace+Comparison.m
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
+ __OBJC_$_INSTANCE_METHODS_MOPlace(Comparison)
+ ___42+[MOPlatformInfo _getMainBundleIdentifier]_block_invoke
+ ___46+[MOPlatformInfo _createDefaultsManagerDaemon]_block_invoke
+ __block_literal_global.41
+ __block_literal_global.76
+ _createDefaultsManagerDaemon.isMomentsDaemon
+ _createDefaultsManagerDaemon.onceToken
+ _getMainBundleIdentifier.bundleIdentifier
+ _getMainBundleIdentifier.onceToken
+ _kDefaultSameLocationThreshold
+ _kMOBundleActionMetadata
+ _kMOBundleDateReferenceTag
+ _kMOBundleTimeIdentifier
+ _kMOPhotoTraitAssociatedPersonLocalIdentifiers
+ _kMOPhotoTraitHolidayIdentifier
+ _kMOPhotoTraitLabelType
+ _kMOPhotoTraitMeaningIdentifier
+ _objc_msgSend$_createDefaultsManagerDaemon
+ _objc_msgSend$_getMainBundleIdentifier
+ _objc_msgSend$_isString:equalToString:
+ _objc_msgSend$currentHandler
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$isSimilarToPlace:locationThreshold:
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
- GCC_except_table14
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
- __OBJC_$_INSTANCE_METHODS_MOPlace
- _kMOBundleConcurrentMediaActionName
- _objc_msgSend$peopleCountMaxNormalized
- _objc_msgSend$peopleCountWeightedAverageNormalized
- _objc_msgSend$peopleCountWeightedSumNormalized
- _objc_msgSend$setPeopleCountMaxNormalized:
- _objc_msgSend$setPeopleCountWeightedAverageNormalized:
- _objc_msgSend$setPeopleCountWeightedSumNormalized:
CStrings:
+ "%@|%@"
+ "Comparison"
+ "Tf,N,V_pCountMaxNormalized"
+ "Tf,N,V_pCountWeightedAverageNormalized"
+ "Tf,N,V_pCountWeightedSumNormalized"
+ "_createDefaultsManagerDaemon"
+ "_getMainBundleIdentifier"
+ "_isString:equalToString:"
+ "_pCountMaxNormalized"
+ "_pCountWeightedAverageNormalized"
+ "_pCountWeightedSumNormalized"
+ "bundleActionMetadata"
+ "currentHandler"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "isSimilarToPlace:"
+ "isSimilarToPlace:locationThreshold:"
+ "placeKey"
+ "setPCountMaxNormalized:"
+ "setPCountWeightedAverageNormalized:"
+ "setPCountWeightedSumNormalized:"
+ "timeIdentifier"
- "PlatformInfoOverrideIsSeedBuild"
- "Tf,N,V_peopleCountMaxNormalized"
- "Tf,N,V_peopleCountWeightedAverageNormalized"
- "Tf,N,V_peopleCountWeightedSumNormalized"
- "_peopleCountMaxNormalized"
- "_peopleCountWeightedAverageNormalized"
- "_peopleCountWeightedSumNormalized"
- "bundleConcurrentMediaActionName"
- "peopleCountMaxNormalized"
- "peopleCountWeightedAverageNormalized"
- "peopleCountWeightedSumNormalized"
- "setPeopleCountMaxNormalized:"
- "setPeopleCountWeightedAverageNormalized:"
- "setPeopleCountWeightedSumNormalized:"

```
