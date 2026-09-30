## HealthUI

> `/System/Library/PrivateFrameworks/HealthUI.framework/HealthUI`

```diff

-6106.1.2.11.0
-  __TEXT.__text: 0x3d6af0
-  __TEXT.__auth_stubs: 0x5100
-  __TEXT.__objc_methlist: 0x39edc
-  __TEXT.__const: 0x7554
-  __TEXT.__cstring: 0x24a27
-  __TEXT.__oslogstring: 0x6d16
-  __TEXT.__gcc_except_tab: 0x259c
+6200.2.7.2.1
+  __TEXT.__text: 0x3d64a4
+  __TEXT.__auth_stubs: 0x5120
+  __TEXT.__objc_methlist: 0x39e7c
+  __TEXT.__const: 0x7564
+  __TEXT.__cstring: 0x24bb7
+  __TEXT.__oslogstring: 0x6bd6
+  __TEXT.__gcc_except_tab: 0x24d0
   __TEXT.__ustring: 0x56
   __TEXT.__dlopen_cstrs: 0x367
   __TEXT.__constg_swiftt: 0x3d78

   __TEXT.__swift_as_entry: 0x3c
   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift5_mpenum: 0x34
-  __TEXT.__unwind_info: 0xdff0
+  __TEXT.__unwind_info: 0xdfc0
   __TEXT.__eh_frame: 0x21dc
-  __TEXT.__objc_classname: 0x9103
-  __TEXT.__objc_methname: 0x7e7c2
-  __TEXT.__objc_methtype: 0x109cd
-  __TEXT.__objc_stubs: 0x49780
+  __TEXT.__objc_classname: 0x90a3
+  __TEXT.__objc_methname: 0x7e1d0
+  __TEXT.__objc_methtype: 0x109e2
+  __TEXT.__objc_stubs: 0x49340
   __DATA_CONST.__got: 0x3460
-  __DATA_CONST.__const: 0x79a0
-  __DATA_CONST.__objc_classlist: 0x20c8
-  __DATA_CONST.__objc_catlist: 0x298
-  __DATA_CONST.__objc_protolist: 0x680
+  __DATA_CONST.__const: 0x7848
+  __DATA_CONST.__objc_classlist: 0x20b0
+  __DATA_CONST.__objc_catlist: 0x2a0
+  __DATA_CONST.__objc_protolist: 0x690
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x183c0
-  __DATA_CONST.__objc_protorefs: 0x160
-  __DATA_CONST.__objc_superrefs: 0x1868
+  __DATA_CONST.__objc_selrefs: 0x182d8
+  __DATA_CONST.__objc_protorefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x1858
   __DATA_CONST.__objc_arraydata: 0x2000
-  __AUTH_CONST.__auth_got: 0x2890
-  __AUTH_CONST.__const: 0x5f08
-  __AUTH_CONST.__cfstring: 0x1eb60
-  __AUTH_CONST.__objc_const: 0x63ba0
+  __AUTH_CONST.__auth_got: 0x28a0
+  __AUTH_CONST.__const: 0x5e88
+  __AUTH_CONST.__cfstring: 0x1eb40
+  __AUTH_CONST.__objc_const: 0x63bb8
   __AUTH_CONST.__objc_arrayobj: 0xf30
   __AUTH_CONST.__objc_intobj: 0x2940
   __AUTH_CONST.__objc_doubleobj: 0x320
   __AUTH_CONST.__objc_dictobj: 0xc8
-  __AUTH.__objc_data: 0x16130
+  __AUTH.__objc_data: 0x16040
   __AUTH.__data: 0x2068
-  __DATA.__objc_ivar: 0x405c
-  __DATA.__data: 0x7190
+  __DATA.__objc_ivar: 0x4028
+  __DATA.__data: 0x7200
   __DATA.__bss: 0x5c68
   __DATA.__common: 0x1e0
   __DATA_DIRTY.__objc_data: 0x1e50

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 4D9A24F3-E7AA-3D43-B813-B479C5CF145B
-  Functions: 24406
-  Symbols:   65389
-  CStrings:  30193
+  UUID: 7C49F566-6CD3-3CC1-9F5C-8120396AC0E7
+  Functions: 24398
+  Symbols:   65204
+  CStrings:  30156
 
Symbols:
+ +[HKSleepComparisonDayChartPoint chartPointsForInformationProviders:context:]
+ +[HKSleepDurationChartPoint chartPointsForInformationProviders:context:]
+ +[HKSleepPeriodChartPoint chartPointsForInformationProviders:context:]
+ +[HKSleepStageChartPoint chartPointsForInformationProviders:context:]
+ +[HKSleepStageDayChartPoint chartPointsForInformationProviders:context:]
+ +[HKSleepStageDurationChartPoint chartPointsForInformationProviders:context:]
+ +[HKSleepUtilities noonAlignedXValueForChartPointInfoProvider:]
+ +[HKSleepUtilities standardXValueForChartPointInfoProvider:]
+ -[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]
+ -[HKSleepChartPointUserInfo chartPointInfoProvider]
+ -[HKSleepChartPointUserInfo initWithSeriesType:chartPointInfoProvider:]
+ -[HKSleepDaySummary(HKSleepChartPointInformationProviding) inBedEndOffset]
+ -[HKSleepDaySummary(HKSleepChartPointInformationProviding) inBedStartOffset]
+ -[HKSleepDaySummary(HKSleepChartPointInformationProviding) isAveraged]
+ -[HKSleepDaySummary(HKSleepChartPointInformationProviding) scheduledBedtimeValue]
+ -[HKSleepDaySummary(HKSleepChartPointInformationProviding) scheduledWakeTimeValue]
+ -[HKSleepDaySummary(HKSleepChartPointInformationProviding) sleepDaySummaries]
+ -[HKSleepDaySummary(HKSleepChartPointInformationProviding) sleepDurationGoalSeconds]
+ -[HKSleepDaySummary(HKSleepChartPointInformationProviding) sleepEndOffset]
+ -[HKSleepDaySummary(HKSleepChartPointInformationProviding) sleepStartOffset]
+ -[HKSourceAuthorizationController copyTypesWithBloodPressureTreatment:]
+ -[_HKSleepDurationAmountContext _countsOfSleepDataFromChartPoints:]
+ -[_HKSleepDurationAmountCounts chartPointsWithSleepDataCount]
+ -[_HKSleepDurationAmountCounts setChartPointsWithSleepDataCount:]
+ -[_HKSleepDurationAmountCounts setTotalChartPoints:]
+ -[_HKSleepDurationAmountCounts totalChartPoints]
+ -[_HKSleepDurationAverageContext _averageValueFromDaySummaries:useInBedAverage:]
+ GCC_except_table49
+ _OBJC_CLASS_$_HKSleepDaySummaryCollection
+ _OBJC_IVAR_$_HKSleepChartPointUserInfo._chartPointInfoProvider
+ _OBJC_IVAR_$__HKSleepDurationAmountCounts._chartPointsWithSleepDataCount
+ _OBJC_IVAR_$__HKSleepDurationAmountCounts._totalChartPoints
+ __CATEGORY_HKSleepDaySummaryCollection_$_HKSleepChartPointInformationProviding
+ __CATEGORY_INSTANCE_METHODS_HKSleepDaySummaryCollection_$_HKSleepChartPointInformationProviding
+ __CATEGORY_PROPERTIES_HKSleepDaySummaryCollection_$_HKSleepChartPointInformationProviding
+ __CATEGORY_PROTOCOLS_HKSleepDaySummaryCollection_$_HKSleepChartPointInformationProviding
+ __ChartPointInformationProvidersForMappingData
+ __OBJC_$_CATEGORY_HKSleepDaySummary_$_HealthUI
+ __OBJC_$_INSTANCE_METHODS_HKSleepDaySummary(HealthUI|HealthUI_TestSupport|HKSleepChartPointInformationProviding)
+ __OBJC_$_PROP_LIST_HKSleepChartPointInformationProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKSleepChartPointInformationProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKSleepChartPointInformationProviding
+ __OBJC_$_PROTOCOL_REFS_HKSleepChartPointInformationProviding
+ __OBJC_CLASS_PROTOCOLS_$_HKSleepDaySummary(HealthUI|HealthUI_TestSupport|HKSleepChartPointInformationProviding)
+ __OBJC_LABEL_PROTOCOL_$_HKSleepChartPointInformationProviding
+ __OBJC_PROTOCOL_$_HKSleepChartPointInformationProviding
+ ___66-[HKSourceAuthorizationController _reloadTypeAuthorizationRecords]_block_invoke.354
+ ___92-[HKSleepChartDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.315
+ ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke
+ ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke.300
+ ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke.300.cold.1
+ ___92-[HKSleepChartDataSource queriesForRequest:useCollectionQueryForSixMonth:completionHandler:]_block_invoke.301
+ ___block_descriptor_40_e8_32s_e32_"HKGraphSeriesDataBlock"16?08ls32l8
+ ___block_descriptor_48_e8_32s40bs_e56_v32?0"HKSleepDaySummaryQuery"8"NSArray"16"NSError"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e56_v32?0"HKSleepDaySummaryQuery"8"NSArray"16"NSError"24ls32l8s40l8s48l8
+ ___block_literal_global.554
+ ___block_literal_global.556
+ _objc_msgSend$_averageValueFromDaySummaries:useInBedAverage:
+ _objc_msgSend$_countsOfSleepDataFromChartPoints:
+ _objc_msgSend$chartPointInfoProvider
+ _objc_msgSend$chartPointsForInformationProviders:context:
+ _objc_msgSend$chartPointsWithSleepDataCount
+ _objc_msgSend$copyTypesWithBloodPressureTreatment:
+ _objc_msgSend$iconSize
+ _objc_msgSend$inBedEndOffset
+ _objc_msgSend$inBedStartOffset
+ _objc_msgSend$initWithDouble:
+ _objc_msgSend$initWithSeriesType:chartPointInfoProvider:
+ _objc_msgSend$isAveraged
+ _objc_msgSend$noonAlignedXValueForChartPointInfoProvider:
+ _objc_msgSend$queriesForRequest:useCollectionQueryForSixMonth:completionHandler:
+ _objc_msgSend$scheduledBedtimeValue
+ _objc_msgSend$scheduledWakeTimeValue
+ _objc_msgSend$setChartPointsWithSleepDataCount:
+ _objc_msgSend$setTotalChartPoints:
+ _objc_msgSend$sleepDurationGoalSeconds
+ _objc_msgSend$sleepEndOffset
+ _objc_msgSend$sleepStartOffset
+ _objc_msgSend$standardXValueForChartPointInfoProvider:
+ _objc_msgSend$totalChartPoints
- +[HKSleepComparisonDayChartPoint chartPointsForSummaries:daySummaryCollections:context:]
- +[HKSleepDaySummary(HealthUI) _aggregateWeeklySummaryFromDailySummaries:calendar:strategy:]
- +[HKSleepDaySummary(HealthUI) _computeAveragePeriodsFromSummaries:summaryDateInterval:]
- +[HKSleepDaySummary(HealthUI) _computeProbablePeriodsFromSummaries:summaryDateInterval:]
- +[HKSleepDaySummary(HealthUI) _endOfWeekContainingDate:calendar:]
- +[HKSleepDaySummary(HealthUI) _findMidPointOffsetForSummary:sleepCategory:]
- +[HKSleepDaySummary(HealthUI) _lastNonEmptySchedules:]
- +[HKSleepDaySummary(HealthUI) _lastNonZeroDurationGoal:]
- +[HKSleepDaySummary(HealthUI) aggregateWeeklySummariesFromDailySummaries:firstWeekdayOverride:strategy:]
- +[HKSleepDurationChartPoint chartPointsForSummaries:daySummaryCollections:context:]
- +[HKSleepPeriodChartPoint chartPointsForSummaries:daySummaryCollections:context:]
- +[HKSleepStageChartPoint chartPointsForSummaries:daySummaryCollections:context:]
- +[HKSleepStageDayChartPoint chartPointsForSummaries:daySummaryCollections:context:]
- +[HKSleepStageDurationChartPoint chartPointsForSummaries:daySummaryCollections:context:]
- +[HKSleepStagePeriodsAggregator _averageStartDateFromSleepDaySummaries:summaryDateInterval:]
- +[HKSleepStagePeriodsAggregator _maximumDurationFromSleepDaySummaries:]
- +[HKSleepUtilities sleepDaySummaryNoonAlignedXValue:]
- +[HKSleepUtilities sleepDaySummaryStandardXValue:]
- +[_HKSleepStageBucket bucketsWithSize:startOfSleep:maxSleepDuration:numberOfDays:]
- -[HKSleepChartDataSource _graphSeriesDataBlockWithSleepDurationChartPointFor:context:]
- -[HKSleepChartDataSource _graphSeriesDataBlockWithSleepPeriodChartPointFor:context:]
- -[HKSleepChartDataSource _graphSeriesDataBlockWithSleepStageChartPointFor:context:]
- -[HKSleepChartDataSource _graphSeriesDataBlockWithSleepStageDurationChartPointFor:context:]
- -[HKSleepChartDataSource _shouldCreateDataSourceQueryResultsWrapperWith:context:]
- -[HKSleepChartPointUserInfo initWithSeriesType:sleepDaySummary:sleepDaySummaryCollection:]
- -[HKSleepChartPointUserInfo sleepDaySummaryCollection]
- -[HKSleepChartPointUserInfo sleepDaySummary]
- -[HKSleepDaySummary(AggregationUtilities) hui_durationOfSleep]
- -[HKSleepDaySummary(AggregationUtilities) hui_endOfSleep]
- -[HKSleepDaySummary(AggregationUtilities) hui_startOfSleepOffset]
- -[HKSleepDaySummary(AggregationUtilities) hui_startOfSleep]
- -[HKSleepDaySummary(HealthUI) hk_bedtimeGoalValue]
- -[HKSleepDaySummary(HealthUI) hk_sleepDurationGoalValue]
- -[HKSleepDaySummary(HealthUI) hk_wakeTimeGoalValue]
- -[HKSleepStagePeriodsAggregator .cxx_destruct]
- -[HKSleepStagePeriodsAggregator _aggregateSleepInterval]
- -[HKSleepStagePeriodsAggregator _aggregateSleepPeriodSegments]
- -[HKSleepStagePeriodsAggregator _bucketIndexForDistanceFromStart:]
- -[HKSleepStagePeriodsAggregator aggregateSleepPeriods]
- -[HKSleepStagePeriodsAggregator buckets]
- -[HKSleepStagePeriodsAggregator initWithSleepDaySummaries:bucketSize:summaryDateInterval:]
- -[HKSleepStagePeriodsAggregator maximumDuration]
- -[HKSleepStagePeriodsAggregator sleepDaySummaries]
- -[HKSleepStagePeriodsAggregator startDate]
- -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper .cxx_destruct]
- -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper daySummaries]
- -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper daySummaryCollections]
- -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper setDaySummaries:]
- -[_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper setDaySummaryCollections:]
- -[_HKSleepDurationAmountContext _daysWithSleepDataFromChartPoints:]
- -[_HKSleepDurationAmountCounts daysWithSleepData]
- -[_HKSleepDurationAmountCounts setDaysWithSleepData:]
- -[_HKSleepDurationAmountCounts setTotalDays:]
- -[_HKSleepDurationAmountCounts totalDays]
- -[_HKSleepDurationAverageContext _averageValueFromChartPoints:useInBedAverage:]
- -[_HKSleepStageBucket .cxx_destruct]
- -[_HKSleepStageBucket _probableSleepStage]
- -[_HKSleepStageBucket bucketSize]
- -[_HKSleepStageBucket distanceFromStart]
- -[_HKSleepStageBucket hasSleepStagesData]
- -[_HKSleepStageBucket initWithBucketSize:distanceFromStart:startOfSleep:numberOfDays:]
- -[_HKSleepStageBucket numberOfDays]
- -[_HKSleepStageBucket probableSleepPeriodSegment]
- -[_HKSleepStageBucket setHasSleepStagesData:]
- -[_HKSleepStageBucket setSleepStageCounts:]
- -[_HKSleepStageBucket sleepStageCounts]
- -[_HKSleepStageBucket startOfSleep]
- -[_HKSleepStageBucket updateWithSegment:]
- _OBJC_CLASS_$_HKSleepStagePeriodsAggregator
- _OBJC_CLASS_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
- _OBJC_CLASS_$__HKSleepStageBucket
- _OBJC_IVAR_$_HKSleepChartPointUserInfo._sleepDaySummary
- _OBJC_IVAR_$_HKSleepChartPointUserInfo._sleepDaySummaryCollection
- _OBJC_IVAR_$_HKSleepStagePeriodsAggregator._buckets
- _OBJC_IVAR_$_HKSleepStagePeriodsAggregator._maximumDuration
- _OBJC_IVAR_$_HKSleepStagePeriodsAggregator._sleepDaySummaries
- _OBJC_IVAR_$_HKSleepStagePeriodsAggregator._startDate
- _OBJC_IVAR_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper._daySummaries
- _OBJC_IVAR_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper._daySummaryCollections
- _OBJC_IVAR_$__HKSleepDurationAmountCounts._daysWithSleepData
- _OBJC_IVAR_$__HKSleepDurationAmountCounts._totalDays
- _OBJC_IVAR_$__HKSleepStageBucket._bucketSize
- _OBJC_IVAR_$__HKSleepStageBucket._distanceFromStart
- _OBJC_IVAR_$__HKSleepStageBucket._hasSleepStagesData
- _OBJC_IVAR_$__HKSleepStageBucket._numberOfDays
- _OBJC_IVAR_$__HKSleepStageBucket._sleepStageCounts
- _OBJC_IVAR_$__HKSleepStageBucket._startOfSleep
- _OBJC_METACLASS_$_HKSleepStagePeriodsAggregator
- _OBJC_METACLASS_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
- _OBJC_METACLASS_$__HKSleepStageBucket
- __DaySummariesForMappingData
- __OBJC_$_CATEGORY_HKSleepDaySummary_$_AggregationUtilities
- __OBJC_$_CLASS_METHODS_HKSleepDaySummary(AggregationUtilities|HealthUI|HealthUI_TestSupport)
- __OBJC_$_CLASS_METHODS_HKSleepStagePeriodsAggregator
- __OBJC_$_CLASS_METHODS__HKSleepStageBucket
- __OBJC_$_INSTANCE_METHODS_HKSleepDaySummary(AggregationUtilities|HealthUI|HealthUI_TestSupport)
- __OBJC_$_INSTANCE_METHODS_HKSleepStagePeriodsAggregator
- __OBJC_$_INSTANCE_METHODS__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
- __OBJC_$_INSTANCE_METHODS__HKSleepStageBucket
- __OBJC_$_INSTANCE_VARIABLES_HKSleepStagePeriodsAggregator
- __OBJC_$_INSTANCE_VARIABLES__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
- __OBJC_$_INSTANCE_VARIABLES__HKSleepStageBucket
- __OBJC_$_PROP_LIST_HKSleepDaySummary_$_AggregationUtilities
- __OBJC_$_PROP_LIST_HKSleepStagePeriodsAggregator
- __OBJC_$_PROP_LIST__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
- __OBJC_$_PROP_LIST__HKSleepStageBucket
- __OBJC_CLASS_RO_$_HKSleepStagePeriodsAggregator
- __OBJC_CLASS_RO_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
- __OBJC_CLASS_RO_$__HKSleepStageBucket
- __OBJC_METACLASS_RO_$_HKSleepStagePeriodsAggregator
- __OBJC_METACLASS_RO_$__HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper
- __OBJC_METACLASS_RO_$__HKSleepStageBucket
- ___106-[_HKSleepDurationAverageContext _updateRangeDataWithChartPoints:useInBedAverage:isHighlighted:timeScope:]_block_invoke
- ___42-[_HKSleepStageBucket _probableSleepStage]_block_invoke
- ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke
- ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.319
- ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.319.cold.1
- ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.320
- ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.323
- ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.327
- ___62-[HKSleepChartDataSource queriesForRequest:completionHandler:]_block_invoke.328
- ___66-[HKSourceAuthorizationController _reloadTypeAuthorizationRecords]_block_invoke.355
- ___67-[HKSleepStageDurationContext _computeAverageValueFromChartPoints:]_block_invoke_2
- ___71+[HKSleepStagePeriodsAggregator _maximumDurationFromSleepDaySummaries:]_block_invoke
- ___72-[HKSleepStagePercentageContext _computePercentageValueFromChartPoints:]_block_invoke
- ___80+[HKSleepStageChartPoint chartPointsForSummaries:daySummaryCollections:context:]_block_invoke
- ___81+[HKSleepPeriodChartPoint chartPointsForSummaries:daySummaryCollections:context:]_block_invoke
- ___83+[HKSleepDurationChartPoint chartPointsForSummaries:daySummaryCollections:context:]_block_invoke
- ___88+[HKSleepStageDurationChartPoint chartPointsForSummaries:daySummaryCollections:context:]_block_invoke
- ___92-[HKSleepChartDataSource generateSharableQueryDataForRequest:healthStore:completionHandler:]_block_invoke.340
- ___block_descriptor_32_e35_16?0"HKSleepDurationChartPoint"8l
- ___block_descriptor_32_e50_16?0"<HKSleepSleepChartPointUserInfoProvider>"8l
- ___block_descriptor_40_e8_32r_e34_v32?0"HKSleepDaySummary"8Q16^B24lr32l8
- ___block_descriptor_48_e8_32s40s_e32_"HKGraphSeriesDataBlock"16?08ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48bs_e20_v24?08"NSError"16ls32l8s48l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e34_v32?0"HKSleepDaySummary"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s_e34_v32?0"HKSleepDaySummary"8Q16^B24ls32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40bs48r56r64r_e5_v8?0lr48l8r56l8s32l8s40l8r64l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e56_v32?0"HKSleepDaySummaryQuery"8"NSArray"16"NSError"24ls32l8s40l8r56l8s48l8r64l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8r72l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0lr64l8s32l8s40l8r72l8s48l8s56l8
- ___block_descriptor_89_e8_32s40s48s56s64bs72r80r_e56_v32?0"HKSleepDaySummaryQuery"8"NSArray"16"NSError"24ls32l8s40l8s48l8r72l8r80l8s56l8s64l8
- ___block_literal_global.561
- ___block_literal_global.563
- ___block_literal_global.831
- _objc_msgSend$_aggregateSleepInterval
- _objc_msgSend$_aggregateSleepPeriodSegments
- _objc_msgSend$_aggregateWeeklySummaryFromDailySummaries:calendar:strategy:
- _objc_msgSend$_averageStartDateFromSleepDaySummaries:summaryDateInterval:
- _objc_msgSend$_averageValueFromChartPoints:useInBedAverage:
- _objc_msgSend$_bucketIndexForDistanceFromStart:
- _objc_msgSend$_computeAveragePeriodsFromSummaries:summaryDateInterval:
- _objc_msgSend$_computeProbablePeriodsFromSummaries:summaryDateInterval:
- _objc_msgSend$_daysWithSleepDataFromChartPoints:
- _objc_msgSend$_endOfWeekContainingDate:calendar:
- _objc_msgSend$_findMidPointOffsetForSummary:sleepCategory:
- _objc_msgSend$_graphSeriesDataBlockWithSleepDurationChartPointFor:context:
- _objc_msgSend$_graphSeriesDataBlockWithSleepPeriodChartPointFor:context:
- _objc_msgSend$_graphSeriesDataBlockWithSleepStageChartPointFor:context:
- _objc_msgSend$_graphSeriesDataBlockWithSleepStageDurationChartPointFor:context:
- _objc_msgSend$_lastNonEmptySchedules:
- _objc_msgSend$_lastNonZeroDurationGoal:
- _objc_msgSend$_maximumDurationFromSleepDaySummaries:
- _objc_msgSend$_probableSleepStage
- _objc_msgSend$_shouldCreateDataSourceQueryResultsWrapperWith:context:
- _objc_msgSend$aggregateSleepPeriods
- _objc_msgSend$bucketSize
- _objc_msgSend$buckets
- _objc_msgSend$bucketsWithSize:startOfSleep:maxSleepDuration:numberOfDays:
- _objc_msgSend$chartPointsForSummaries:daySummaryCollections:context:
- _objc_msgSend$creationInterval
- _objc_msgSend$daySummaries
- _objc_msgSend$daySummaryCollections
- _objc_msgSend$daysWithSleepData
- _objc_msgSend$distanceFromStart
- _objc_msgSend$hk_bedtimeGoalValue
- _objc_msgSend$hk_sleepDurationGoalValue
- _objc_msgSend$hk_wakeTimeGoalValue
- _objc_msgSend$hui_durationOfSleep
- _objc_msgSend$hui_endOfSleep
- _objc_msgSend$hui_startOfSleep
- _objc_msgSend$hui_startOfSleepOffset
- _objc_msgSend$initWithBucketSize:distanceFromStart:startOfSleep:numberOfDays:
- _objc_msgSend$initWithSeriesType:sleepDaySummary:sleepDaySummaryCollection:
- _objc_msgSend$initWithSleepDaySummaries:bucketSize:summaryDateInterval:
- _objc_msgSend$maximumDuration
- _objc_msgSend$probableSleepPeriodSegment
- _objc_msgSend$schedules
- _objc_msgSend$setDaySummaries:
- _objc_msgSend$setDaySummaryCollections:
- _objc_msgSend$setDaysWithSleepData:
- _objc_msgSend$setHasSleepStagesData:
- _objc_msgSend$setTotalDays:
- _objc_msgSend$sleepDaySummary
- _objc_msgSend$sleepDaySummaryCollection
- _objc_msgSend$sleepDaySummaryNoonAlignedXValue:
- _objc_msgSend$sleepDaySummaryStandardXValue:
- _objc_msgSend$sleepPeriodSegmentWithDateInterval:category:
- _objc_msgSend$sleepStageCounts
- _objc_msgSend$startOfSleep
- _objc_msgSend$totalDays
- _objc_msgSend$updateWithSegment:
CStrings:
+ "%s: navigation controller was nil"
+ "@\"<HKSleepChartPointInformationProviding>\""
+ "@\"NSArray\"32@0:8@\"NSArray\"16@\"HKSleepAnalysisDataSourceContext\"24"
+ "@\"NSCalendar\"16@0:8"
+ "@\"NSDateInterval\"16@0:8"
+ "@36@0:8@16B24@?28"
+ "HKSleepChartPointInformationProviding"
+ "Ordered read: %@\nOrdered Write: %@"
+ "T@\"<HKSleepChartPointInformationProviding>\",R,N,V_chartPointInfoProvider"
+ "T@\"NSCalendar\",N,R"
+ "T@\"NSCalendar\",R,C,N"
+ "T@\"NSDateInterval\",N,R"
+ "T@\"NSDateInterval\",R,C,N"
+ "T@\"NSNumber\",N,R"
+ "T@\"NSNumber\",R,C,N"
+ "Tq,N,V_chartPointsWithSleepDataCount"
+ "Tq,N,V_totalChartPoints"
+ "[%{public}@.%{public}@] creating query for day indices: %ld-%ld dates: %{public}@-%{public}@"
+ "_VALUE_LEVEL_FORMAT"
+ "_averageValueFromDaySummaries:useInBedAverage:"
+ "_chartPointInfoProvider"
+ "_chartPointsWithSleepDataCount"
+ "_countsOfSleepDataFromChartPoints:"
+ "_totalChartPoints"
+ "averageAwakeDuration"
+ "averageCoreSleepDuration"
+ "averageDeepSleepDuration"
+ "averageInBedDuration"
+ "averageInBedEndOffset"
+ "averageInBedStartOffset"
+ "averageREMSleepDuration"
+ "averageSleepDuration"
+ "averageSleepEndOffset"
+ "averageSleepStartOffset"
+ "chartPointInfoProvider"
+ "chartPointsForInformationProviders:context:"
+ "chartPointsWithSleepDataCount"
+ "copyTypesWithBloodPressureTreatment:"
+ "hk_popToControllerAtIndex:animated:"
+ "inBedEndOffset"
+ "inBedStartOffset"
+ "initWithSeriesType:chartPointInfoProvider:"
+ "isAveraged"
+ "noonAlignedXValueForChartPointInfoProvider:"
+ "queriesForRequest:useCollectionQueryForSixMonth:completionHandler:"
+ "scheduledBedtimeValue"
+ "scheduledWakeTimeValue"
+ "setChartPointsWithSleepDataCount:"
+ "setTotalChartPoints:"
+ "sleepDurationGoalSeconds"
+ "sleepEndOffset"
+ "sleepStartOffset"
+ "standardXValueForChartPointInfoProvider:"
+ "totalChartPoints"
- "@\"HKSleepDaySummary\""
- "@\"HKSleepDaySummaryCollection\""
- "@\"NSArray\"40@0:8@\"NSArray\"16@\"NSArray\"24@\"HKSleepAnalysisDataSourceContext\"32"
- "@16@?0@\"<HKSleepSleepChartPointUserInfoProvider>\"8"
- "@16@?0@\"HKSleepDurationChartPoint\"8"
- "@48@0:8d16@24d32q40"
- "AggregationUtilities"
- "HKSleepStagePeriodsAggregator"
- "SleepChartDataSource"
- "T@\"HKSleepDaySummary\",R,N,V_sleepDaySummary"
- "T@\"HKSleepDaySummaryCollection\",R,N,V_sleepDaySummaryCollection"
- "T@\"NSArray\",C,N,V_daySummaries"
- "T@\"NSArray\",C,N,V_daySummaryCollections"
- "T@\"NSArray\",R,N,V_buckets"
- "T@\"NSArray\",R,N,V_sleepDaySummaries"
- "T@\"NSDate\",R,N,V_startOfSleep"
- "T@\"NSMutableDictionary\",&,N,V_sleepStageCounts"
- "TB,N,V_hasSleepStagesData"
- "Td,R,N,V_distanceFromStart"
- "Td,R,N,V_maximumDuration"
- "Tq,N,V_daysWithSleepData"
- "Tq,N,V_totalDays"
- "Tq,R,N,V_numberOfDays"
- "[%{public}@.%{public}@] creating query for day indeces: %ld-%ld dates: %{public}@-%{public}@"
- "[%{public}@.%{public}@]: Decremented query counter after sleep day summary collection query with %ld collections"
- "[%{public}@.%{public}@]: Decremented query counter after sleep day summary query"
- "[%{public}@.%{public}@]: Sleep day summary query returned while at 6 month time scope with %ld summaries"
- "[%{public}@.%{public}@]: Task completion counter count is 0, returning %ld summaries and %ld collections"
- "_HKSleepChartSixMonthTimeScopeDataSourceQueryResultsWrapper"
- "_HKSleepStageBucket"
- "_aggregateSleepInterval"
- "_aggregateSleepPeriodSegments"
- "_aggregateWeeklySummaryFromDailySummaries:calendar:strategy:"
- "_averageStartDateFromSleepDaySummaries:summaryDateInterval:"
- "_averageValueFromChartPoints:useInBedAverage:"
- "_bucketIndexForDistanceFromStart:"
- "_buckets"
- "_computeAveragePeriodsFromSummaries:summaryDateInterval:"
- "_computeProbablePeriodsFromSummaries:summaryDateInterval:"
- "_daySummaries"
- "_daySummaryCollections"
- "_daysWithSleepData"
- "_daysWithSleepDataFromChartPoints:"
- "_distanceFromStart"
- "_endOfWeekContainingDate:calendar:"
- "_findMidPointOffsetForSummary:sleepCategory:"
- "_graphSeriesDataBlockWithSleepDurationChartPointFor:context:"
- "_graphSeriesDataBlockWithSleepPeriodChartPointFor:context:"
- "_graphSeriesDataBlockWithSleepStageChartPointFor:context:"
- "_graphSeriesDataBlockWithSleepStageDurationChartPointFor:context:"
- "_hasSleepStagesData"
- "_lastNonEmptySchedules:"
- "_lastNonZeroDurationGoal:"
- "_maximumDuration"
- "_maximumDurationFromSleepDaySummaries:"
- "_numberOfDays"
- "_probableSleepStage"
- "_shouldCreateDataSourceQueryResultsWrapperWith:context:"
- "_sleepDaySummaries"
- "_sleepDaySummary"
- "_sleepDaySummaryCollection"
- "_sleepStageCounts"
- "_startOfSleep"
- "_totalDays"
- "aggregateSleepPeriods"
- "aggregateWeeklySummariesFromDailySummaries:firstWeekdayOverride:strategy:"
- "bucketsWithSize:startOfSleep:maxSleepDuration:numberOfDays:"
- "chartPointsForSummaries:daySummaryCollections:context:"
- "creationInterval"
- "daySummaries"
- "daySummaryCollections"
- "daysWithSleepData"
- "distanceFromStart"
- "hasSleepStagesData"
- "hk_bedtimeGoalValue"
- "hk_sleepDurationGoalValue"
- "hk_wakeTimeGoalValue"
- "hui_durationOfSleep"
- "hui_endOfSleep"
- "hui_startOfSleep"
- "hui_startOfSleepOffset"
- "initWithBucketSize:distanceFromStart:startOfSleep:numberOfDays:"
- "initWithSeriesType:sleepDaySummary:sleepDaySummaryCollection:"
- "initWithSleepDaySummaries:bucketSize:summaryDateInterval:"
- "maximumDuration"
- "numberOfDays"
- "probableSleepPeriodSegment"
- "schedules"
- "setAllowsBackForwardNavigationGestures:"
- "setDaySummaries:"
- "setDaySummaryCollections:"
- "setDaysWithSleepData:"
- "setHasSleepStagesData:"
- "setSleepStageCounts:"
- "setTotalDays:"
- "sleepDaySummary"
- "sleepDaySummaryCollection"
- "sleepDaySummaryNoonAlignedXValue:"
- "sleepDaySummaryStandardXValue:"
- "sleepPeriodSegmentWithDateInterval:category:"
- "sleepStageCounts"
- "startOfSleep"
- "totalDays"
- "updateWithSegment:"
- "v32@?0@\"HKSleepDaySummary\"8Q16^B24"

```
