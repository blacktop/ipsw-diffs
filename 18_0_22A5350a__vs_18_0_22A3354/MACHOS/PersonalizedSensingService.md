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
+ -[MOEventBundleRankingInput peopleCountMaxNormalized]
+ _objc_msgSend$setPeopleCountMaxNormalized:
+ -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
+ _objc_msgSend$peopleCountMaxNormalized
+ _objc_msgSend$setPeopleCountWeightedAverageNormalized:
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
+ _objc_msgSend$setPeopleCountWeightedSumNormalized:
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1107
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1155
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1113
+ _objc_msgSend$peopleCountWeightedAverageNormalized
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157.cold.1
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1118
+ -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
+ _objc_msgSend$peopleCountWeightedSumNormalized
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1143
+ -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
+ OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
- -[MOEventBundleRankingInput pCountWeightedSumNormalized]
- _objc_msgSend$setPCountMaxNormalized:
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
- _objc_msgSend$setPCountWeightedSumNormalized:
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
- _objc_msgSend$pCountWeightedSumNormalized
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
- -[MOEventBundleRankingInput pCountMaxNormalized]
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
- _objc_msgSend$currentHandler
- _objc_msgSend$pCountMaxNormalized
- -[MOEventBundleRankingInput setPCountMaxNormalized:]
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
- -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
- _objc_msgSend$pCountWeightedAverageNormalized
- _OBJC_CLASS_$_NSAssertionHandler
- OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
- -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
- _objc_msgSend$setPCountWeightedAverageNormalized:
CStrings:
+ "_peopleCountWeightedAverageNormalized"
+ "setPeopleCountWeightedAverageNormalized:"
+ "_peopleCountMaxNormalized"
+ "setPeopleCountMaxNormalized:"
+ "Tf,N,V_peopleCountWeightedSumNormalized"
+ "peopleCountMaxNormalized"
+ "peopleCountWeightedSumNormalized"
+ "_peopleCountWeightedSumNormalized"
+ "Tf,N,V_peopleCountWeightedAverageNormalized"
+ "PlatformInfoOverrideIsSeedBuild"
+ "Tf,N,V_peopleCountMaxNormalized"
+ "setPeopleCountWeightedSumNormalized:"
+ "peopleCountWeightedAverageNormalized"
- "_pCountMaxNormalized"
- "setPCountWeightedSumNormalized:"
- "Tf,N,V_pCountWeightedAverageNormalized"
- "Tf,N,V_pCountWeightedSumNormalized"
- "currentHandler"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "_pCountWeightedSumNormalized"
- "_pCountWeightedAverageNormalized"
- "setPCountMaxNormalized:"
- "setPCountWeightedAverageNormalized:"
- "Tf,N,V_pCountMaxNormalized"

```
