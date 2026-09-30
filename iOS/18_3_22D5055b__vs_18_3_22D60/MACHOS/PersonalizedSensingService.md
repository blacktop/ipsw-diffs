## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

 205.0.1.0.0
-  __TEXT.__text: 0x68acc
+  __TEXT.__text: 0x67e50
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0xabe0
+  __TEXT.__objc_stubs: 0xaba0
   __TEXT.__objc_methlist: 0x6a64
   __TEXT.__objc_classname: 0x825
   __TEXT.__objc_methtype: 0xfbc
-  __TEXT.__cstring: 0xb55b
-  __TEXT.__objc_methname: 0x118ed
+  __TEXT.__cstring: 0xaf68
+  __TEXT.__objc_methname: 0x118e0
   __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0xbe0
   __TEXT.__oslogstring: 0x6d60
   __TEXT.__ustring: 0x4
   __TEXT.__unwind_info: 0x1168
   __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x528
+  __DATA_CONST.__got: 0x520
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x2ea8
-  __DATA_CONST.__cfstring: 0xe960
+  __DATA_CONST.__cfstring: 0xe5e0
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_const: 0xbcd0
-  __DATA.__objc_selrefs: 0x36e0
+  __DATA.__objc_selrefs: 0x36d0
   __DATA.__objc_ivar: 0x918
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x4c0

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
   Functions: 2477
-  Symbols:   18796
-  CStrings:  5523
+  Symbols:   18793
+  CStrings:  5493
 
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
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1155
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1107
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1113
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1118
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1143
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
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
- _objc_msgSend$currentHandler
- _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
- _objc_msgSend$pCountMaxNormalized
- _objc_msgSend$pCountWeightedAverageNormalized
- _objc_msgSend$pCountWeightedSumNormalized
- _objc_msgSend$setPCountMaxNormalized:
- _objc_msgSend$setPCountWeightedAverageNormalized:
- _objc_msgSend$setPCountWeightedSumNormalized:
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
