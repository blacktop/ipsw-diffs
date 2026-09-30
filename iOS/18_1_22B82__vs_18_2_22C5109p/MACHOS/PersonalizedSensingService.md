## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-202.0.8.0.0
-  __TEXT.__text: 0x679b8
+204.0.2.0.0
+  __TEXT.__text: 0x68b24
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0xab00
-  __TEXT.__objc_methlist: 0x6a54
+  __TEXT.__objc_stubs: 0xabe0
+  __TEXT.__objc_methlist: 0x6a64
   __TEXT.__objc_classname: 0x825
-  __TEXT.__objc_methtype: 0xfa1
-  __TEXT.__cstring: 0xaf7c
-  __TEXT.__objc_methname: 0x11863
+  __TEXT.__objc_methtype: 0xfbc
+  __TEXT.__cstring: 0xb55b
+  __TEXT.__objc_methname: 0x118ed
   __TEXT.__const: 0x498
-  __TEXT.__gcc_except_tab: 0xbd0
-  __TEXT.__oslogstring: 0x6c4f
+  __TEXT.__gcc_except_tab: 0xbe0
+  __TEXT.__oslogstring: 0x6d60
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1160
+  __TEXT.__unwind_info: 0x1168
   __DATA_CONST.__auth_got: 0x478
-  __DATA_CONST.__got: 0x520
+  __DATA_CONST.__got: 0x528
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x2e58
-  __DATA_CONST.__cfstring: 0xe5e0
+  __DATA_CONST.__const: 0x2ea8
+  __DATA_CONST.__cfstring: 0xe960
   __DATA_CONST.__objc_classlist: 0x2d8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_floatobj: 0x1b0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xbcb0
-  __DATA.__objc_selrefs: 0x36b0
+  __DATA.__objc_const: 0xbcd0
+  __DATA.__objc_selrefs: 0x36e0
   __DATA.__objc_ivar: 0x918
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x4c0

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  Functions: 2472
-  Symbols:   18759
-  CStrings:  5482
+  Functions: 2477
+  Symbols:   18796
+  CStrings:  5523
 
Symbols:
+ -[MOContextManager refreshMomentsContextWithReply:]
+ -[MOEventBundleRankingInput pCountMaxNormalized]
+ -[MOEventBundleRankingInput pCountWeightedAverageNormalized]
+ -[MOEventBundleRankingInput pCountWeightedSumNormalized]
+ -[MOEventBundleRankingInput setPCountMaxNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedAverageNormalized:]
+ -[MOEventBundleRankingInput setPCountWeightedSumNormalized:]
+ -[PersonalizedSensingService refreshMomentsContextWithReply:]
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountMaxNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedAverageNormalized
+ OBJC_IVAR_$_MOEventBundleRankingInput._pCountWeightedSumNormalized
+ _OBJC_CLASS_$_NSAssertionHandler
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1174
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1176.cold.1
+ __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1370
+ __51-[MOContextManager refreshMomentsContextWithReply:]_block_invoke.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1120
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1126
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1127
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1131
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1162
+ ___51-[MOContextManager refreshMomentsContextWithReply:]_block_invoke
+ ___61-[PersonalizedSensingService refreshMomentsContextWithReply:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e5_v8?0ls32l8r56l8s40l8s48l8r64l8
+ __block_literal_global.1490
+ _objc_msgSend$currentHandler
+ _objc_msgSend$domain
+ _objc_msgSend$handleFailureInMethod:object:file:lineNumber:description:
+ _objc_msgSend$pCountMaxNormalized
+ _objc_msgSend$pCountWeightedAverageNormalized
+ _objc_msgSend$pCountWeightedSumNormalized
+ _objc_msgSend$persistentStoreCoordinator
+ _objc_msgSend$persistentStores
+ _objc_msgSend$refreshMomentsContextWithReply:
+ _objc_msgSend$setPCountMaxNormalized:
+ _objc_msgSend$setPCountWeightedAverageNormalized:
+ _objc_msgSend$setPCountWeightedSumNormalized:
+ _objc_msgSend$softRefreshEventsWithRefreshVariant:andIgnoreLastTrigger:andHandler:
- -[MOEventBundleRankingInput peopleCountMaxNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedAverageNormalized]
- -[MOEventBundleRankingInput peopleCountWeightedSumNormalized]
- -[MOEventBundleRankingInput setPeopleCountMaxNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedAverageNormalized:]
- -[MOEventBundleRankingInput setPeopleCountWeightedSumNormalized:]
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountMaxNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedAverageNormalized
- OBJC_IVAR_$_MOEventBundleRankingInput._peopleCountWeightedSumNormalized
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1155
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.1157.cold.1
- __139-[MOBundleContentExtractor _extractContentsFromBundleStartDate:endDate:daysPerFetch:significantLocationEnabled:partialResults:withHandler:]_block_invoke.1369
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1107
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1113
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1114
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.1118
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.1143
- ___block_descriptor_56_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
- __block_literal_global.1489
- _objc_msgSend$peopleCountMaxNormalized
- _objc_msgSend$peopleCountWeightedAverageNormalized
- _objc_msgSend$peopleCountWeightedSumNormalized
- _objc_msgSend$setPeopleCountMaxNormalized:
- _objc_msgSend$setPeopleCountWeightedAverageNormalized:
- _objc_msgSend$setPeopleCountWeightedSumNormalized:
CStrings:
+ "PSService, refreshMomentsContextWithReply"
+ "Tf,N,V_pCountMaxNormalized"
+ "Tf,N,V_pCountWeightedAverageNormalized"
+ "Tf,N,V_pCountWeightedSumNormalized"
+ "XPCRefreshMomentsContext"
+ "_pCountMaxNormalized"
+ "_pCountWeightedAverageNormalized"
+ "_pCountWeightedSumNormalized"
+ "calling soft refresh , error, %!@(MISSING)"
+ "context result count, %!l(MISSING)d, error, %!@(MISSING)"
+ "currentHandler"
+ "domain"
+ "handleFailureInMethod:object:file:lineNumber:description:"
+ "persistentStores"
+ "refreshMomentsContextWithReply:"
+ "setPCountMaxNormalized:"
+ "setPCountWeightedAverageNormalized:"
+ "setPCountWeightedSumNormalized:"
+ "softRefreshEventsWithRefreshVariant:andIgnoreLastTrigger:andHandler:"
+ "store is already loaded"
+ "suppress the template error as the context is not empty so the error is only for part of the bundles, error, %!@(MISSING)"
+ "v24@0:8@?<v@?@\"NSError\">16"
- "MOTemplateBuilder:generate context hit error"
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
