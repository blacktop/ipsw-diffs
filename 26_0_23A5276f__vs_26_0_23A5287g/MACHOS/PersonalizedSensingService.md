## PersonalizedSensingService

> `/System/Library/PrivateFrameworks/PersonalizedSensing.framework/XPCServices/PersonalizedSensingService.xpc/PersonalizedSensingService`

```diff

-265.0.0.0.0
-  __TEXT.__text: 0x7278c
+269.0.0.0.0
+  __TEXT.__text: 0x72e74
   __TEXT.__auth_stubs: 0x8c0
-  __TEXT.__objc_stubs: 0xb520
-  __TEXT.__objc_methlist: 0x7234
+  __TEXT.__objc_stubs: 0xb5a0
+  __TEXT.__objc_methlist: 0x7264
   __TEXT.__objc_classname: 0x83e
   __TEXT.__objc_methtype: 0x1116
-  __TEXT.__cstring: 0xbf65
-  __TEXT.__objc_methname: 0x12dfc
+  __TEXT.__cstring: 0xbfbb
+  __TEXT.__objc_methname: 0x12ebe
   __TEXT.__const: 0x500
-  __TEXT.__gcc_except_tab: 0xe84
-  __TEXT.__oslogstring: 0x753b
+  __TEXT.__gcc_except_tab: 0xe80
+  __TEXT.__oslogstring: 0x76be
   __TEXT.__ustring: 0x10c
-  __TEXT.__unwind_info: 0x12b8
+  __TEXT.__unwind_info: 0x12c0
   __DATA_CONST.__auth_got: 0x478
   __DATA_CONST.__got: 0x538
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0x3280
-  __DATA_CONST.__cfstring: 0xfaa0
+  __DATA_CONST.__cfstring: 0xfae0
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_floatobj: 0x1c0
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xc1c8
-  __DATA.__objc_selrefs: 0x3b00
-  __DATA.__objc_ivar: 0x9a4
+  __DATA.__objc_const: 0xc1f8
+  __DATA.__objc_selrefs: 0x3b20
+  __DATA.__objc_ivar: 0x9a8
   __DATA.__objc_data: 0x1d60
   __DATA.__data: 0x4d8
   __DATA.__bss: 0x50

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libperfcheck.dylib
-  UUID: 2D1BE678-939A-3FA7-B46E-0A2E469F4E22
-  Functions: 2635
-  Symbols:   19924
-  CStrings:  7858
+  UUID: CBC33217-85F8-34A2-8B68-7F5A0C4EF8CD
+  Functions: 2641
+  Symbols:   19959
+  CStrings:  7872
 
Symbols:
+ -[MOEventBundleRanking holidayTuningParameters]
+ -[MOEventBundleRanking loadHolidayTuningParameterJSONFromFilePath]
+ -[MOEventBundleRanking loadHolidayTuningParameterJSONFromFilePath].cold.1
+ -[MOEventBundleRanking loadHolidayTuningParameterJSONFromFilePath].cold.2
+ -[MOEventBundleRanking setHolidayTuningParameters:]
+ -[MOEventBundleRanking setHolidayTuningParameters]
+ GCC_except_table113
+ OBJC_IVAR_$_MOEventBundleRanking._holidayTuningParameters
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.772
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774
+ __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.774.cold.1
+ __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.526
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.703.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.707.cold.1
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.711
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.714
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.715
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.719
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.729
+ __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.730
+ __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.758
+ _objc_msgSend$holidayTuningParameters
+ _objc_msgSend$loadHolidayTuningParameterJSONFromFilePath
+ _objc_msgSend$setHolidayTuningParameters
+ _objc_msgSend$setHolidayTuningParameters:
- GCC_except_table109
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.763
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.765
- __114-[MOEventBundleRanking identifyRepetitiveSignificantContactBundlesFromBundles:precedingSignificantContactBundles:]_block_invoke.765.cold.1
- __62-[MOEventBundleRanking _fillRichnessInfoForRanking:forBundle:]_block_invoke.517
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.694
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.694.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.698
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.698.cold.1
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.702
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.705
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.706
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.710
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.720
- __88-[MOEventBundleRanking _calculateRankingScore:withMinRecommendedBundleCountRequirement:]_block_invoke.721
- __94-[MOEventBundleRanking _submitEventBundleRankingAnalytics:withRankingInput:andSubmissionDate:]_block_invoke.749
CStrings:
+ "/System/Library/Trial/NamespaceDescriptors/HolidayTuningParameters.json"
+ "?"
+ "Could not read the holiday tuning parameter json file, error: %@"
+ "Couldn't parse the holiday tuning parameter json to dictionary. %@, error, %@"
+ "T@\"NSDictionary\",&,N,V_holidayTuningParameters"
+ "The holiday tuning parameter json file was successfully read from path, %@"
+ "Thematic summary bundle got suppressed from Recommended tab since it shared the same place(s) with more highly ranked bundle. SuggestionID:%@, bundleID:%@, startDate:%@"
+ "_holidayTuningParameters"
+ "holidayTuningParameters"
+ "loadHolidayTuningParameterJSONFromFilePath"
+ "minPhotoCount"
+ "setHolidayTuningParameters"
+ "setHolidayTuningParameters:"

```
