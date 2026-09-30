## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-6074.1.2.4.0
-  __TEXT.__text: 0x7b1f4
-  __TEXT.__auth_stubs: 0x1ff0
-  __TEXT.__objc_methlist: 0x33b4
-  __TEXT.__const: 0x1880
+6087.1.2.1.0
+  __TEXT.__text: 0x7b924
+  __TEXT.__auth_stubs: 0x2020
+  __TEXT.__objc_methlist: 0x33a4
+  __TEXT.__const: 0x1890
   __TEXT.__cstring: 0x4005
-  __TEXT.__oslogstring: 0x6222
+  __TEXT.__oslogstring: 0x62f2
   __TEXT.__gcc_except_tab: 0xe4c
   __TEXT.__constg_swiftt: 0x630
   __TEXT.__swift5_typeref: 0xb68
-  __TEXT.__swift5_reflstr: 0x72d
-  __TEXT.__swift5_fieldmd: 0x540
+  __TEXT.__swift5_reflstr: 0x74d
+  __TEXT.__swift5_fieldmd: 0x54c
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x1d8
   __TEXT.__swift5_proto: 0xf8
   __TEXT.__swift5_types: 0x68
-  __TEXT.__swift5_capture: 0x1f0
+  __TEXT.__swift5_capture: 0x204
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x15f0
+  __TEXT.__unwind_info: 0x15f8
   __TEXT.__eh_frame: 0xec8
   __TEXT.__objc_classname: 0xbd5
-  __TEXT.__objc_methname: 0x11177
-  __TEXT.__objc_methtype: 0x20da
+  __TEXT.__objc_methname: 0x11132
+  __TEXT.__objc_methtype: 0x2069
   __TEXT.__objc_stubs: 0x95a0
-  __DATA_CONST.__got: 0xc08
-  __DATA_CONST.__const: 0xf68
+  __DATA_CONST.__got: 0xc18
+  __DATA_CONST.__const: 0xf60
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x218

   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x1010
-  __AUTH_CONST.__const: 0xd38
+  __AUTH_CONST.__auth_got: 0x1028
+  __AUTH_CONST.__const: 0xdb8
   __AUTH_CONST.__cfstring: 0x2280
-  __AUTH_CONST.__objc_const: 0x62c8
+  __AUTH_CONST.__objc_const: 0x62a0
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x3c8
   __AUTH.__data: 0x40
-  __DATA.__objc_ivar: 0x480
+  __DATA.__objc_ivar: 0x47c
   __DATA.__data: 0x1620
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x11e0

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
+  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/Coherence.framework/Coherence
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2708F427-73DE-3B60-AA48-214DD8EC3C5D
-  Functions: 2118
-  Symbols:   5492
+  UUID: 5A4A64E9-E560-34BE-BAEF-72793C34620A
+  Functions: 2124
+  Symbols:   5493
   CStrings:  3295
 
Symbols:
+ -[HDMCAnalysisScheduler initWithDaemon:analysisManager:settingsManager:]
+ _HKMCMenstrualCyclesWidgetContainerBundleID
+ _HKMCNanoMenstrualCyclesWidgetContainerBundleID
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
+ ___swift_memcpy24_8
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_HealthMenstrualCyclesDaemon
+ __swift_FORCE_LOAD_$_swiftSpatial
+ __swift_FORCE_LOAD_$_swiftSpatial_$_HealthMenstrualCyclesDaemon
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_HealthMenstrualCyclesDaemon
+ _objc_msgSend$initWithDaemon:analysisManager:settingsManager:
- -[HDMCAnalysisScheduler initWithDaemon:analysisManager:settingsManager:calendarCache:]
- _OBJC_IVAR_$_HDMCAnalysisScheduler._calendarCache
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
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_HealthMenstrualCyclesDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HealthMenstrualCyclesDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HealthMenstrualCyclesDaemon
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HealthMenstrualCyclesDaemon
- _objc_msgSend$initWithDaemon:analysisManager:settingsManager:calendarCache:
CStrings:
+ "[%{public}s] error invalidating relevance %{public}s for widget of kind %{public}s in bundleIdentifier: %{public}s"
+ "[%{public}s] invalidating widget relevances for kind %s"
+ "[%{public}s] reloading widget kind %s with reason: %s"
+ "initWithDaemon:analysisManager:settingsManager:"
+ "kind"
- "[%{public}s] reloading widgets with reason: %s"
- "associationsUpdatedForObject:subObject:type:objects:anchor:"
- "initWithDaemon:analysisManager:settingsManager:calendarCache:"
- "v56@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32@\"NSArray\"40@\"NSNumber\"48"
- "v56@0:8@16@24Q32@40@48"

```
