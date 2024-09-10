## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 197.0.0.0.0
-  __TEXT.__text: 0x65fbc
+  __TEXT.__text: 0x65340
   __TEXT.__auth_stubs: 0x890
-  __TEXT.__objc_stubs: 0xa960
+  __TEXT.__objc_stubs: 0xa920
   __TEXT.__objc_methlist: 0x693c
   __TEXT.__objc_classname: 0x827
   __TEXT.__objc_methtype: 0xf8b
-  __TEXT.__cstring: 0xb26c
-  __TEXT.__objc_methname: 0x114a4
+  __TEXT.__cstring: 0xac79
+  __TEXT.__objc_methname: 0x11497
   __TEXT.__const: 0x470
   __TEXT.__gcc_except_tab: 0xb7c
   __TEXT.__oslogstring: 0x69ac
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x1108
   __DATA_CONST.__auth_got: 0x460
-  __DATA_CONST.__got: 0x518
+  __DATA_CONST.__got: 0x510
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2d18
-  __DATA_CONST.__cfstring: 0xe400
+  __DATA_CONST.__cfstring: 0xe080
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xbb60
-  __DATA.__objc_selrefs: 0x3618
+  __DATA.__objc_selrefs: 0x3608
   __DATA.__objc_ivar: 0x8fc
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x4c0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   Functions: 2429
-  Symbols:   18456
-  CStrings:  5423
+  Symbols:   18453
+  CStrings:  5393
 
Symbols:
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1118
+ -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1113
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1155
+ _objc_msgSend$setPeopleCountWeightedAverageNormalized:
+ _objc_msgSend$peopleCountWeightedSumNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
+ -[MOEventBundleRankingInput peopleCountMaxNormalized]
+ -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
+ _objc_msgSend$peopleCountWeightedAverageNormalized
+ -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
+ _objc_msgSend$peopleCountMaxNormalized
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1107
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1143
+ _objc_msgSend$setPeopleCountWeightedSumNormalized:
+ -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
+ _objc_msgSend$setPeopleCountMaxNormalized:
- -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
- _objc_msgSend$pCountWeightedAverageNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
- _OBJC_CLASS_$_NSAssertionHandler
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
- _objc_msgSend$setPCountMaxNormalized:
- _objc_msgSend$pCountMaxNormalized
- _objc_msgSend$setPCountWeightedSumNormalized:
- -[MOEventBundleRankingInput pCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
- _objc_msgSend$pCountWeightedSumNormalized
- -[MOEventBundleRankingInput pCountMaxNormalized]
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
- -[MOEventBundleRankingInput setPCountMaxNormalized:]
- _objc_msgSend$setPCountWeightedAverageNormalized:
- _objc_msgSend$currentHandler
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
- -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
CStrings:
+ "_peopleCountWeightedAverageNormalized"
+ "peopleCountWeightedSumNormalized"
+ "setPeopleCountWeightedAverageNormalized:"
+ "peopleCountMaxNormalized"
+ "setPeopleCountMaxNormalized:"
+ "Tf,N,V_peopleCountMaxNormalized"
+ "Tf,N,V_peopleCountWeightedAverageNormalized"
+ "_peopleCountMaxNormalized"
+ "peopleCountWeightedAverageNormalized"
+ "setPeopleCountWeightedSumNormalized:"
+ "_peopleCountWeightedSumNormalized"
+ "PlatformInfoOverrideIsSeedBuild"
+ "Tf,N,V_peopleCountWeightedSumNormalized"
- "currentHandler"
- "Tf,N,V_pCountWeightedAverageNormalized"
- "_pCountWeightedAverageNormalized"
- "_pCountMaxNormalized"
- "_pCountWeightedSumNormalized"
- "setPCountWeightedSumNormalized:"
- "setPCountMaxNormalized:"
- "Tf,N,V_pCountMaxNormalized"
- "setPCountWeightedAverageNormalized:"
- "Tf,N,V_pCountWeightedSumNormalized"
- "handleFailureInMethod:object:file:lineNumber:description:"

```
