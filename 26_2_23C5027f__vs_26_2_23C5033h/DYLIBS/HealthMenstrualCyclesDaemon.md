## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-6200.3.4.0.0
-  __TEXT.__text: 0x7c340
+6200.3.8.0.0
+  __TEXT.__text: 0x7c348
   __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__objc_methlist: 0x33ec
   __TEXT.__const: 0x1890

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 3E1A9C57-FDAD-3462-88FD-BAB261CC0256
+  UUID: E2E5362D-1EE4-3835-9D32-B52AF6C12441
   Functions: 2134
   Symbols:   5497
   CStrings:  3318
Symbols:
+ ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.311
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.365
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.368
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.372
+ ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.329
+ ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.333
+ ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.321
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.392
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.392.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.333
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.333.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.334
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.336
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.336.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.337
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.337.cold.1
+ ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.331
+ ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.368
+ ___block_literal_global.307
+ ___block_literal_global.315
+ ___block_literal_global.317
+ ___block_literal_global.319
+ ___block_literal_global.323
+ ___block_literal_global.325
+ ___block_literal_global.327
+ ___block_literal_global.330
+ ___block_literal_global.356
+ ___block_literal_global.359
+ ___block_literal_global.361
+ ___block_literal_global.363
+ ___block_literal_global.400
+ ___block_literal_global.406
+ ___block_literal_global.490
+ ___block_literal_global.493
+ ___block_literal_global.522
- ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.302
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.356
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.359
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.363
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.320
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.324
- ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.312
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.383
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.383.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.324
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.324.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.325
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.327
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.327.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.328
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.328.cold.1
- ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.322
- ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.359
- ___block_literal_global.298
- ___block_literal_global.301
- ___block_literal_global.306
- ___block_literal_global.308
- ___block_literal_global.312
- ___block_literal_global.314
- ___block_literal_global.316
- ___block_literal_global.318
- ___block_literal_global.347
- ___block_literal_global.350
- ___block_literal_global.352
- ___block_literal_global.354
- ___block_literal_global.391
- ___block_literal_global.397
- ___block_literal_global.481
- ___block_literal_global.484
- ___block_literal_global.513
Functions:
~ ___76-[HDMCRecentBasalBodyTemperatureRangeQuery accumulateSortedValuesWithError:]_block_invoke : 232 -> 236
~ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ne200100Em : 60 -> 64

```
