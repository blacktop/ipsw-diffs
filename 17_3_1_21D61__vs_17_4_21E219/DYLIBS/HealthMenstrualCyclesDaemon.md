## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-4146.3.2.0.0
-  __TEXT.__text: 0x3ddc4
-  __TEXT.__auth_stubs: 0xad0
+4146.4.18.0.0
+  __TEXT.__text: 0x3ddcc
+  __TEXT.__auth_stubs: 0xae0
   __TEXT.__objc_methlist: 0x272c
   __TEXT.__const: 0xd8
   __TEXT.__cstring: 0x29ba

   __TEXT.__oslogstring: 0x4ccf
   __TEXT.__unwind_info: 0xbd4
   __TEXT.__objc_classname: 0x9e1
-  __TEXT.__objc_methname: 0xf976
+  __TEXT.__objc_methname: 0xf98a
   __TEXT.__objc_methtype: 0x1354
   __TEXT.__objc_stubs: 0x9220
   __DATA_CONST.__got: 0x3c0

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4a60
   __DATA_CONST.__objc_selrefs: 0x2758
+  __DATA_CONST.__objc_classrefs: 0x4e8
+  __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__objc_intobj: 0x318
+  __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__cfstring: 0x20c0
   __AUTH_CONST.__objc_const: 0x14b0
   __AUTH_CONST.__const: 0x280
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_classrefs: 0x4e8
-  __DATA.__objc_superrefs: 0x140
   __DATA.__objc_ivar: 0x484
   __DATA.__data: 0x9c0
   __DATA_DIRTY.__objc_data: 0xc30

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B63233D7-A6DB-3B6F-9E5D-770EBF0E2350
+  UUID: E0D07DB8-255D-3B46-90A3-345F4DE850F5
   Functions: 1155
-  Symbols:   4836
-  CStrings:  2829
+  Symbols:   4837
+  CStrings:  2830
 
Symbols:
+ __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8ue170006Ev
+ __ZNSt12length_errorC1B8ue170006EPKc
+ __ZNSt3__119__allocate_at_leastB8ue170006INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ue170006EPKc
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8ue170006Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE16__init_with_sizeB8ue170006IPdS5_EEvT_T0_m
+ __ZSt28__throw_bad_array_new_lengthB8ue170006v
+ ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.248
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.281
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.284
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.288
+ ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.257
+ ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.261
+ ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.265
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.311
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.311.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.270
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.270.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.271
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.273
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.273.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.274
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.274.cold.1
+ ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.268
+ ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.287
+ ___block_literal_global.247
+ ___block_literal_global.252
+ ___block_literal_global.254
+ ___block_literal_global.256
+ ___block_literal_global.258
+ ___block_literal_global.260
+ ___block_literal_global.263
+ ___block_literal_global.337
+ ___block_literal_global.343
+ ___block_literal_global.427
+ ___block_literal_global.430
+ ___block_literal_global.459
+ __unnamed_array_storage.246
+ __unnamed_array_storage.248
+ _memmove
- __ZNKSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB7v160006Ev
- __ZNSt12length_errorC1B7v160006EPKc
- __ZNSt3__119__allocate_at_leastB7v160006INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB7v160006EPKc
- __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB7v160006Em
- __ZNSt3__16vectorIdNS_9allocatorIdEEEC2ERKS3_
- __ZSt28__throw_bad_array_new_lengthB7v160006v
- ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.224
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.257
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.260
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.264
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.233
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.237
- ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.241
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.287
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.287.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.246
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.246.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.247
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.249
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.249.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.250
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.250.cold.1
- ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.244
- ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.263
- ___block_literal_global.223
- ___block_literal_global.228
- ___block_literal_global.230
- ___block_literal_global.232
- ___block_literal_global.234
- ___block_literal_global.236
- ___block_literal_global.239
- ___block_literal_global.312
- ___block_literal_global.318
- ___block_literal_global.403
- ___block_literal_global.406
- ___block_literal_global.435
- __unnamed_array_storage.224
- __unnamed_array_storage.226
CStrings:
+ "T@\"NSString\",?,R,C"

```
