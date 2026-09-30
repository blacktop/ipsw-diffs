## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-6100.0.0.0.0
-  __TEXT.__text: 0x7ba2c
+6105.0.0.0.0
+  __TEXT.__text: 0x7b94c
   __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__objc_methlist: 0x33bc
   __TEXT.__const: 0x1890

   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0x1010
-  __AUTH_CONST.__const: 0xde0
+  __AUTH_CONST.__const: 0xe50
   __AUTH_CONST.__cfstring: 0x2280
   __AUTH_CONST.__objc_const: 0x62a8
   __AUTH_CONST.__objc_intobj: 0x2d0

   __AUTH.__objc_data: 0x3c8
   __AUTH.__data: 0x40
   __DATA.__objc_ivar: 0x47c
-  __DATA.__data: 0x1620
+  __DATA.__data: 0x1610
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x11e0
+  __DATA.__bss: 0x1160
   __DATA.__common: 0xb8
   __DATA_DIRTY.__objc_data: 0x1080
   __DATA_DIRTY.__data: 0x890
-  __DATA_DIRTY.__bss: 0xc80
+  __DATA_DIRTY.__bss: 0xd00
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9C010FA8-2F56-35A3-822E-F10AD42F1F86
+  UUID: 77971A6F-46AC-3F64-A813-2E411C4F1217
   Functions: 2127
   Symbols:   5488
   CStrings:  3301
Symbols:
+ ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.302
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.359
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.363
+ ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.320
+ ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.324
+ ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.312
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.383
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.383.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.327
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.327.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.328
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.328.cold.1
+ ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.322
+ ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.359
+ ___block_literal_global.301
+ ___block_literal_global.306
+ ___block_literal_global.308
+ ___block_literal_global.310
+ ___block_literal_global.312
+ ___block_literal_global.314
+ ___block_literal_global.316
+ ___block_literal_global.321
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.354
+ ___block_literal_global.391
+ ___block_literal_global.397
+ ___block_literal_global.484
+ ___block_literal_global.513
- ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.299
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.353
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.360
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.317
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.321
- ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.309
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.380
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.380.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.321
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.321.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.322
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.325.cold.1
- ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.319
- ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.356
- ___block_literal_global.295
- ___block_literal_global.303
- ___block_literal_global.305
- ___block_literal_global.307
- ___block_literal_global.309
- ___block_literal_global.311
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.344
- ___block_literal_global.349
- ___block_literal_global.351
- ___block_literal_global.388
- ___block_literal_global.394
- ___block_literal_global.478
- ___block_literal_global.510
Functions:
~ sub_22d8ba1c4 -> sub_2275271c4 : 5884 -> 5660

```
