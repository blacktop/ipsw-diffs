## FinHealthInsights

> `/System/Library/PrivateFrameworks/FinHealthInsights.framework/FinHealthInsights`

```diff

-1.6.29.1.0
-  __TEXT.__text: 0x3198
-  __TEXT.__auth_stubs: 0x390
-  __TEXT.__objc_methlist: 0x2e8
-  __TEXT.__const: 0x58
-  __TEXT.__gcc_except_tab: 0x100
-  __TEXT.__cstring: 0x305
-  __TEXT.__oslogstring: 0x3f
-  __TEXT.__unwind_info: 0x104
-  __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0xc88
-  __TEXT.__objc_methtype: 0x231
-  __TEXT.__objc_stubs: 0xaa0
-  __DATA_CONST.__got: 0x68
-  __DATA_CONST.__const: 0x200
-  __DATA_CONST.__objc_classlist: 0x28
+1.6.31.3.0
+  __TEXT.__text: 0x3ba4
+  __TEXT.__auth_stubs: 0x3a0
+  __TEXT.__objc_methlist: 0x3b0
+  __TEXT.__const: 0x5c
+  __TEXT.__gcc_except_tab: 0xf0
+  __TEXT.__cstring: 0x391
+  __TEXT.__oslogstring: 0x82
+  __TEXT.__unwind_info: 0x124
+  __TEXT.__objc_classname: 0xbd
+  __TEXT.__objc_methname: 0xea4
+  __TEXT.__objc_methtype: 0x239
+  __TEXT.__objc_stubs: 0xb80
+  __DATA_CONST.__got: 0x70
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x918
-  __DATA_CONST.__objc_selrefs: 0x318
-  __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x520
-  __AUTH_CONST.__const: 0x60
+  __DATA_CONST.__objc_const: 0x9e8
+  __DATA_CONST.__objc_selrefs: 0x3a0
+  __DATA_CONST.__objc_classrefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_arraydata: 0x28
+  __AUTH_CONST.__cfstring: 0x5c0
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_const: 0x2d0
-  __AUTH_CONST.__auth_got: 0x1d8
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x70
-  __DATA.__objc_superrefs: 0x28
-  __DATA.__objc_ivar: 0x38
-  __DATA.__data: 0x180
-  __DATA.__bss: 0x20
+  __AUTH_CONST.__objc_const: 0x360
+  __AUTH_CONST.__auth_got: 0x1e0
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x48
+  __DATA.__data: 0x190
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0xf0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/FinHealthCore.framework/FinHealthCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 68
-  Symbols:   423
-  CStrings:  243
+  Functions: 86
+  Symbols:   487
+  CStrings:  283
 
Symbols:
+ +[FHInsightsSpendingTrends overrideMonthlyFillFactor]
+ +[FHInsightsSpendingTrends overrideWeeklyFillFactor]
+ +[FHInsightsSpendingTrends setThresholdsWithWeeklyThreshold:monthlyThreshold:]
+ +[FHMerchantSpendInsight supportsSecureCoding]
+ -[FHInsightsSpendingTrends _computeAndStoreTrend:indexedAmountSums:insightFeatureName:insightType:trendWindow:]
+ -[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]
+ -[FHInsightsSpendingTrends _fillFactorWithStartOfPeriodForMostRecentEntryDate:mostRecentEntryDate:endOfPeriodForMostRecentEntryDate:numberOfDaysSinceFirstTransaction:transactionCount:transactionCountForMostRecentPeriod:transactionAmountSums:transactionAmountSumsForMostRecentPeriod:]
+ -[FHInsightsSpendingTrends _kendallCoefficientWithIndexedAmountSums:]
+ -[FHInsightsSpendingTrends _spearmanCoefficientWithIndexedAmountSums:]
+ -[FHInsightsSpendingTrends initWithMerchantCounts:]
+ -[FHInsightsSpendingTrends initWithWeeklyThreshold:monthlyThreshold:merchantCounts:]
+ -[FHInsightsSpendingTrends merchantCounts]
+ -[FHInsightsSpendingTrends monthlyThreshold]
+ -[FHInsightsSpendingTrends setMerchantCounts:]
+ -[FHInsightsSpendingTrends trendsWithCompletion:]
+ -[FHInsightsSpendingTrends weeklyThreshold]
+ -[FHMerchantSpendInsight .cxx_destruct]
+ -[FHMerchantSpendInsight description]
+ -[FHMerchantSpendInsight encodeWithCoder:]
+ -[FHMerchantSpendInsight initWithCoder:]
+ -[FHMerchantSpendInsight merchantName]
+ -[FHMerchantSpendInsight setMerchantName:]
+ _FHInsightOverallSpendFeatureName
+ _FHInsightTypeMerchantSpend
+ _FHInsightsMerchantCountThreshold
+ _FHMerchantCategoryFromString
+ _FHMerchantCategoryToString
+ _FHMerchantSpendInsightMerchantNameKey
+ _OBJC_CLASS_$_FHMerchantSpendInsight
+ _OBJC_IVAR_$_FHInsightsSpendingTrends._merchantCounts
+ _OBJC_IVAR_$_FHInsightsSpendingTrends._monthlyThreshold
+ _OBJC_IVAR_$_FHInsightsSpendingTrends._weeklyThreshold
+ _OBJC_IVAR_$_FHMerchantSpendInsight.merchantName
+ _OBJC_METACLASS_$_FHMerchantSpendInsight
+ __OBJC_$_CLASS_METHODS_FHMerchantSpendInsight
+ __OBJC_$_INSTANCE_METHODS_FHMerchantSpendInsight
+ __OBJC_$_INSTANCE_VARIABLES_FHMerchantSpendInsight
+ __OBJC_$_PROP_LIST_FHMerchantSpendInsight
+ __OBJC_CLASS_RO_$_FHMerchantSpendInsight
+ __OBJC_METACLASS_RO_$_FHMerchantSpendInsight
+ ___111-[FHInsightsSpendingTrends _computeAndStoreTrend:indexedAmountSums:insightFeatureName:insightType:trendWindow:]_block_invoke
+ ___49-[FHInsightsSpendingTrends trendsWithCompletion:]_block_invoke
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.42
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke.46
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke_2
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke_3
+ ___61-[FHInsightsSpendingTrends _computeCategoryAndMerchantTrends]_block_invoke_4
+ ___block_descriptor_168_e8_32r40r48r56r64r72r80r88r96r104r112r120r128r136r144r152r160w_e32_v28?0"NSArray"8"NSError"16B24lw160l8r32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8r128l8r136l8r144l8r152l8
+ ___block_descriptor_32_e33_v16?0"FHDatabaseClauseBuilder"8l
+ ___block_descriptor_40_e8_32s_e46_v32?0"NSString"8"NSMutableDictionary"16^B24ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_88_e8_32s40s48s56s_e41_v16?0"FHDatabaseInsertOrUpdateBuilder"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.51
+ ___block_literal_global.97
+ _defaultMonthlyFillFactorStatus
+ _defaultMonthlyThreshold
+ _defaultWeeklyFillFactorStatus
+ _defaultWeeklyThreshold
+ _objc_msgSend$_computeAndStoreTrend:indexedAmountSums:insightFeatureName:insightType:trendWindow:
+ _objc_msgSend$_computeCategoryAndMerchantTrends
+ _objc_msgSend$_fillFactorWithStartOfPeriodForMostRecentEntryDate:mostRecentEntryDate:endOfPeriodForMostRecentEntryDate:numberOfDaysSinceFirstTransaction:transactionCount:transactionCountForMostRecentPeriod:transactionAmountSums:transactionAmountSumsForMostRecentPeriod:
+ _objc_msgSend$_kendallCoefficientWithIndexedAmountSums:
+ _objc_msgSend$addStringValueForField:fieldValue:
+ _objc_msgSend$decimalNumberByAdding:
+ _objc_msgSend$decimalNumberByDividingBy:
+ _objc_msgSend$decimalNumberByRaisingToPower:
+ _objc_msgSend$decimalNumberBySubtracting:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$initWithInteger:
+ _objc_msgSend$initWithWeeklyThreshold:monthlyThreshold:merchantCounts:
+ _objc_msgSend$integerValue
+ _objc_msgSend$merchantName
+ _objc_msgSend$one
+ _objc_msgSend$setMerchantName:
+ _objc_msgSend$setOrAddToDoubleValue:forKey:
+ _objc_msgSend$stringValue
+ _objc_release_x9
+ _objc_retain_x27
+ _objc_retain_x4
+ _objc_retain_x8
- -[FHInsightsSpendingTrends _computeAndStoreAnomaly:indexedAmountSums:scoresIndexedByMerchantCategory:merchantCategory:trendWindow:leftOfCurve:]
- -[FHInsightsSpendingTrends _computeAndStoreTrend:indexedAmountSums:merchantCategory:intervalLengthFromLastInstance:trendWindow:]
- -[FHInsightsSpendingTrends _computeKendallCoefficient:indexedAmountSums:]
- -[FHInsightsSpendingTrends _computeTrendsForAllMerchantCategories:weeklyNegativeScores:monthlyPositiveScores:monthlyNegativeScores:merchantCategory:useCategoryBoundsForTimeSeries:]
- -[FHInsightsSpendingTrends computeAllAnomaliesAndTrends:weeklyNegativeScores:monthlyPositiveScores:monthlyNegativeScores:useCategoryBoundsForTimeSeries:withCompletion:]
- -[FHInsightsSpendingTrends initWithQueue:]
- -[FHInsightsSpendingTrends init]
- _FHInsightTypeTypeMerchantSpend
- ___128-[FHInsightsSpendingTrends _computeAndStoreTrend:indexedAmountSums:merchantCategory:intervalLengthFromLastInstance:trendWindow:]_block_invoke
- ___143-[FHInsightsSpendingTrends _computeAndStoreAnomaly:indexedAmountSums:scoresIndexedByMerchantCategory:merchantCategory:trendWindow:leftOfCurve:]_block_invoke
- ___168-[FHInsightsSpendingTrends computeAllAnomaliesAndTrends:weeklyNegativeScores:monthlyPositiveScores:monthlyNegativeScores:useCategoryBoundsForTimeSeries:withCompletion:]_block_invoke
- ___180-[FHInsightsSpendingTrends _computeTrendsForAllMerchantCategories:weeklyNegativeScores:monthlyPositiveScores:monthlyNegativeScores:merchantCategory:useCategoryBoundsForTimeSeries:]_block_invoke
- ___180-[FHInsightsSpendingTrends _computeTrendsForAllMerchantCategories:weeklyNegativeScores:monthlyPositiveScores:monthlyNegativeScores:merchantCategory:useCategoryBoundsForTimeSeries:]_block_invoke.38
- ___block_descriptor_136_e8_32r40r48r56r64r72r80r88r96r104r112r120r128w_e32_v28?0"NSArray"8"NSError"16B24lw128l8r32l8r40l8r48l8r56l8r64l8r72l8r80l8r88l8r96l8r104l8r112l8r120l8
- ___block_descriptor_41_e33_v16?0"FHDatabaseClauseBuilder"8l
- ___block_descriptor_88_e8_32s40s48s_e41_v16?0"FHDatabaseInsertOrUpdateBuilder"8ls32l8s40l8s48l8
- ___block_descriptor_88_e8_32s40s_e41_v16?0"FHDatabaseInsertOrUpdateBuilder"8ls32l8s40l8
- ___block_descriptor_89_e8_32s40s48s56s64s72bs80w_e5_v8?0lw80l8s72l8s32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.82
- _objc_msgSend$_computeAndStoreAnomaly:indexedAmountSums:scoresIndexedByMerchantCategory:merchantCategory:trendWindow:leftOfCurve:
- _objc_msgSend$_computeAndStoreTrend:indexedAmountSums:merchantCategory:intervalLengthFromLastInstance:trendWindow:
- _objc_msgSend$_computeKendallCoefficient:indexedAmountSums:
- _objc_msgSend$_computeTrendsForAllMerchantCategories:weeklyNegativeScores:monthlyPositiveScores:monthlyNegativeScores:merchantCategory:useCategoryBoundsForTimeSeries:
- _objc_msgSend$decimalNumberWithDecimal:
- _objc_msgSend$decimalNumberWithString:
- _objc_msgSend$decimalValue
- _objc_msgSend$initWithFloat:
- _objc_msgSend$initWithQueue:
- _objc_msgSend$setWindowReference:
- _objc_msgSend$unsignedIntegerValue
- _objc_retain
- _objc_retain_x24
- _objc_retain_x26
- _objc_retain_x28
- _objc_retain_x3
CStrings:
+ "\x01"
+ "\x04"
+ "%@ %@ trend for feature %@, type %@"
+ "@\"NSDictionary\""
+ "@40@0:8d16d24@32"
+ "Downward"
+ "FHInsightTypeMerchantSpend"
+ "FHMerchantSpendInsight"
+ "No trend detected for %@: %@"
+ "OP"
+ "Overall Spend"
+ "T@\"NSDictionary\",C,N,V_merchantCounts"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,VmerchantName"
+ "Td,R,N,V_monthlyThreshold"
+ "Td,R,N,V_weeklyThreshold"
+ "Upward"
+ "_computeAndStoreTrend:indexedAmountSums:insightFeatureName:insightType:trendWindow:"
+ "_computeCategoryAndMerchantTrends"
+ "_fillFactorWithStartOfPeriodForMostRecentEntryDate:mostRecentEntryDate:endOfPeriodForMostRecentEntryDate:numberOfDaysSinceFirstTransaction:transactionCount:transactionCountForMostRecentPeriod:transactionAmountSums:transactionAmountSumsForMostRecentPeriod:"
+ "_kendallCoefficientWithIndexedAmountSums:"
+ "_merchantCounts"
+ "_monthlyThreshold"
+ "_spearmanCoefficientWithIndexedAmountSums:"
+ "_weeklyThreshold"
+ "addStringValueForField:fieldValue:"
+ "d"
+ "d16@0:8"
+ "d80@0:8@16@24@32Q40Q48Q56d64d72"
+ "decimalNumberByAdding:"
+ "decimalNumberByDividingBy:"
+ "decimalNumberByRaisingToPower:"
+ "decimalNumberBySubtracting:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "fillFactorForPeriod: %f"
+ "initWithInteger:"
+ "initWithMerchantCounts:"
+ "initWithWeeklyThreshold:monthlyThreshold:merchantCounts:"
+ "integerValue"
+ "m_displayname"
+ "merchantCounts"
+ "merchantName"
+ "monthly"
+ "monthlyThreshold"
+ "one"
+ "overrideMonthlyFillFactor"
+ "overrideWeeklyFillFactor"
+ "setMerchantCounts:"
+ "setMerchantName:"
+ "setOrAddToDoubleValue:forKey:"
+ "setThresholdsWithWeeklyThreshold:monthlyThreshold:"
+ "stringValue"
+ "t_identifier"
+ "threshold: %f"
+ "trend_feature_name"
+ "trend_feature_type"
+ "trend_readable_description"
+ "trendsWithCompletion:"
+ "v24@0:8@?16"
+ "v32@0:8d16d24"
+ "v32@?0@\"NSString\"8@\"NSMutableDictionary\"16^B24"
+ "v56@0:8@16@24@32@40q48"
+ "weekly"
+ "weeklyThreshold"
- "\x03"
- "%@*%@ + %@"
- "-0.8"
- "0.8"
- "@32@0:8Q16@24"
- "FHInsightTypeTypeMerchantSpend"
- "_computeAndStoreAnomaly:indexedAmountSums:scoresIndexedByMerchantCategory:merchantCategory:trendWindow:leftOfCurve:"
- "_computeAndStoreTrend:indexedAmountSums:merchantCategory:intervalLengthFromLastInstance:trendWindow:"
- "_computeKendallCoefficient:indexedAmountSums:"
- "_computeTrendsForAllMerchantCategories:weeklyNegativeScores:monthlyPositiveScores:monthlyNegativeScores:merchantCategory:useCategoryBoundsForTimeSeries:"
- "computeAllAnomaliesAndTrends:weeklyNegativeScores:monthlyPositiveScores:monthlyNegativeScores:useCategoryBoundsForTimeSeries:withCompletion:"
- "decimalNumberWithDecimal:"
- "decimalNumberWithString:"
- "decimalValue"
- "initWithFloat:"
- "initWithQueue:"
- "stddev(%@)"
- "trend_merchant_category"
- "trend_type"
- "trend_window_reference"
- "unsignedIntegerValue"
- "v56@0:8@16@24q32Q40q48"
- "v60@0:8@16@24@32@40B48@?52"
- "v60@0:8@16@24@32@40q48B56"
- "v60@0:8@16@24@32q40q48B56"

```
