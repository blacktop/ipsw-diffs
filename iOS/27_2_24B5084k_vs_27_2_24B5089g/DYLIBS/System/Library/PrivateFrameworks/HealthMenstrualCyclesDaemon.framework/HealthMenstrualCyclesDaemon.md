## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-7027.1.36.2.7
-  __TEXT.__text: 0x8e884
-  __TEXT.__objc_methlist: 0x37d4
+7027.1.45.2.4
+  __TEXT.__text: 0x8eef0
+  __TEXT.__objc_methlist: 0x37ec
   __TEXT.__const: 0x1e30
-  __TEXT.__gcc_except_tab: 0xdec
+  __TEXT.__gcc_except_tab: 0xe28
   __TEXT.__oslogstring: 0x6b5c
   __TEXT.__cstring: 0x39c1
   __TEXT.__constg_swiftt: 0x81c

   __TEXT.__swift5_proto: 0x134
   __TEXT.__swift5_types: 0x98
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x20a0
+  __TEXT.__unwind_info: 0x20c0
   __TEXT.__eh_frame: 0xed8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1050
+  __DATA_CONST.__const: 0x10a0
   __DATA_CONST.__objc_classlist: 0x1a8
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x280
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e38
+  __DATA_CONST.__objc_selrefs: 0x2e58
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0xc8
   __DATA_CONST.__got: 0xd48
   __AUTH_CONST.__const: 0x12b8
   __AUTH_CONST.__cfstring: 0x2460
-  __AUTH_CONST.__objc_const: 0x6a28
+  __AUTH_CONST.__objc_const: 0x6a48
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_doubleobj: 0x40

   __AUTH_CONST.__auth_got: 0x11f8
   __AUTH.__objc_data: 0x410
   __AUTH.__data: 0x18
-  __DATA.__objc_ivar: 0x4b8
-  __DATA.__data: 0x1968
+  __DATA.__objc_ivar: 0x4bc
+  __DATA.__data: 0x18f8
   __DATA.__objc_stublist: 0x8
   __DATA_DIRTY.__objc_data: 0x11c0
-  __DATA_DIRTY.__data: 0xcc0
-  __DATA_DIRTY.__bss: 0x1200
+  __DATA_DIRTY.__data: 0xd20
+  __DATA_DIRTY.__bss: 0x1380
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2419
-  Symbols:   4305
-  CStrings:  831
+  Functions: 2424
+  Symbols:   4314
+  CStrings:  832
 
Symbols:
+ +[HDMCRecentBasalBodyTemperatureRangeQuery recentRangeForAnalysisWithProfile:latestEndDate:]
+ -[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:]
+ -[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:addedCycleFactors:deletedCycleFactors:mode:error:]
+ -[HDMCAnalysisManager analysisAsOfDayIndex:forceIncludeCycles:error:]
+ -[HDMCRecentBasalBodyTemperatureRangeQuery initWithProfile:sampleLimit:upperQuantileBound:lowerQuantileBound:latestEndDate:]
+ GCC_except_table14
+ GCC_except_table19
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table39
+ GCC_except_table50
+ _OBJC_IVAR_$_HDMCRecentBasalBodyTemperatureRangeQuery._latestEndDate
+ ___176-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:addedCycleFactors:deletedCycleFactors:mode:error:]_block_invoke
+ ___437-[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:]_block_invoke
+ ___437-[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:]_block_invoke_2
+ ___69-[HDMCAnalysisManager analysisAsOfDayIndex:forceIncludeCycles:error:]_block_invoke
+ ___69-[HDMCAnalysisManager analysisAsOfDayIndex:forceIncludeCycles:error:]_block_invoke_2
+ ___block_descriptor_174_e8_32s40s48s56s64s72s80r88r96r104r112r120r128r_e28_v24?0"HKMCDaySummary"8^B16lr80l8s32l8r88l8s40l8s48l8r96l8r104l8r112l8r120l8s56l8s64l8r128l8s72l8
+ ___block_descriptor_65_e8_32s40r48r_e5_v8?0ls32l8r40l8r48l8
+ ___block_descriptor_65_e8_32s40s48r_e9_B16?0^8lr48l8s32l8s40l8
+ _objc_msgSend$_analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:replayingEarlierDay:
+ _objc_msgSend$_queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:addedCycleFactors:deletedCycleFactors:mode:error:
+ _objc_msgSend$analysisAsOfDayIndex:forceIncludeCycles:error:
+ _objc_msgSend$asOfDayIndex
+ _objc_msgSend$recentRangeForAnalysisWithProfile:latestEndDate:
+ _objc_msgSend$sampleForDayIndex:
- -[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:]
- -[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:addedCycleFactors:deletedCycleFactors:forPreview:error:]
- GCC_except_table11
- GCC_except_table18
- GCC_except_table20
- GCC_except_table23
- GCC_except_table27
- GCC_except_table44
- ___182-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:addedCycleFactors:deletedCycleFactors:forPreview:error:]_block_invoke
- ___417-[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:]_block_invoke
- ___417-[HDMCAnalysisManager _analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:]_block_invoke_2
- ___block_descriptor_166_e8_32s40s48s56s64s72s80r88r96r104r112r120r128r_e28_v24?0"HKMCDaySummary"8^B16lr80l8s32l8r88l8s40l8s48l8r96l8r104l8r112l8r120l8s56l8s64l8r128l8s72l8
- _objc_msgSend$_analysisWithAlgorithmsAnalysis:algorithmsCycles:recentSymptoms:mostRecentBasalBodyTemperature:lastLoggedDayIndex:lastMenstrualFlowDayIndex:currentDayIndex:numberOfDailySleepHeartRateStatisticsForPast100Days:numberOfDailyAwakeHeartRateStatisticsForPast100Days:featureSettings:useHeartRateInput:useWristTemperatureInput:deviationsFeatureSettings:addedCycleFactors:deletedCycleFactors:forPreview:
- _objc_msgSend$_queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:addedCycleFactors:deletedCycleFactors:forPreview:error:
- _objc_msgSend$initWithProfile:sampleLimit:upperQuantileBound:lowerQuantileBound:
- _objc_msgSend$ongoingMenopauseSamples
- _objc_msgSend$recentRangeForAnalysisWithProfile:
CStrings:
+ "A"
```
