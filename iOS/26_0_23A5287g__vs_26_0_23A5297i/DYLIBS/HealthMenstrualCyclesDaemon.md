## HealthMenstrualCyclesDaemon

> `/System/Library/PrivateFrameworks/HealthMenstrualCyclesDaemon.framework/HealthMenstrualCyclesDaemon`

```diff

-6093.0.0.0.0
-  __TEXT.__text: 0x7b924
-  __TEXT.__auth_stubs: 0x2020
+6100.0.0.0.0
+  __TEXT.__text: 0x7ba2c
+  __TEXT.__auth_stubs: 0x1ff0
   __TEXT.__objc_methlist: 0x33bc
   __TEXT.__const: 0x1890
-  __TEXT.__cstring: 0x4005
+  __TEXT.__cstring: 0x4025
   __TEXT.__oslogstring: 0x62f2
   __TEXT.__gcc_except_tab: 0xe4c
   __TEXT.__constg_swiftt: 0x630

   __TEXT.__swift5_types: 0x68
   __TEXT.__swift5_capture: 0x204
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x1670
+  __TEXT.__unwind_info: 0x1678
   __TEXT.__eh_frame: 0xec8
   __TEXT.__objc_classname: 0xbd5
-  __TEXT.__objc_methname: 0x11169
+  __TEXT.__objc_methname: 0x111ad
   __TEXT.__objc_methtype: 0x209f
   __TEXT.__objc_stubs: 0x95a0
-  __DATA_CONST.__got: 0xc18
-  __DATA_CONST.__const: 0xf60
+  __DATA_CONST.__got: 0xc20
+  __DATA_CONST.__const: 0xf30
   __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c60
+  __DATA_CONST.__objc_selrefs: 0x2c70
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x118
   __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x1028
-  __AUTH_CONST.__const: 0xdb8
+  __AUTH_CONST.__auth_got: 0x1010
+  __AUTH_CONST.__const: 0xde0
   __AUTH_CONST.__cfstring: 0x2280
   __AUTH_CONST.__objc_const: 0x62a8
   __AUTH_CONST.__objc_intobj: 0x2d0

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
-  - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
-  - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
   - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/Coherence.framework/Coherence
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
-  - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
-  - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C29BEDDC-F2F2-34EF-B2B9-F9377DC59C92
-  Functions: 2124
-  Symbols:   5494
-  CStrings:  3298
+  UUID: 9C010FA8-2F56-35A3-822E-F10AD42F1F86
+  Functions: 2127
+  Symbols:   5488
+  CStrings:  3301
 
Symbols:
+ _OBJC_CLASS_$_CHSWidgetService
+ ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.299
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.353
+ ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.360
+ ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.317
+ ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.321
+ ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.309
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.380
+ ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.380.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.321
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.321.cold.1
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.322
+ ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.325.cold.1
+ ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.319
+ ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.356
+ ___block_literal_global.295
+ ___block_literal_global.303
+ ___block_literal_global.305
+ ___block_literal_global.307
+ ___block_literal_global.309
+ ___block_literal_global.311
+ ___block_literal_global.313
+ ___block_literal_global.315
+ ___block_literal_global.344
+ ___block_literal_global.349
+ ___block_literal_global.351
+ ___block_literal_global.388
+ ___block_literal_global.394
+ ___block_literal_global.478
+ ___block_literal_global.510
- ___130-[HDMCAnalysisManager(CycleFactorsAutomaticUpgrade) initiateCycleFactorsAutomaticUpgradeWithDatabaseAccessibilityAssertion:error:]_block_invoke.302
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.359
- ___133-[HDMCAnalysisManager _queue_computeAnalysisWithDatabaseAccessibilityAssertion:forceIncludeCycles:forceAnalyzeCompleteHistory:error:]_block_invoke.363
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke.320
- ___162-[HDMCPluginServer remote_confirmAndSaveDeviationWithMenstrualFlowByDayIndex:intermenstrualBleedingByDayIndex:addedCycleFactors:initialAnalysisWindow:completion:]_block_invoke_2.324
- ___191-[HDMCDailyAnalytics _collectDiagnosticFieldsForMetric:settingsManager:heartRateInputFeatureStatus:deviationDetectionFeatureStatus:wristTemperatureInputFeatureStatus:gregorianCalendar:error:]_block_invoke.312
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.383
- ___41-[HDMCPluginServer _triggerImmediateSync]_block_invoke.383.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.327
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.327.cold.1
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.328
- ___60-[HDMCHeartStatisticsEnumerator enumerateWithError:handler:]_block_invoke.328.cold.1
- ___60-[HDMCNotificationManager _queue_alarm:didReceiveDueEvents:]_block_invoke.322
- ___88-[HDMCPluginServer _queue_saveLastMenstrualPeriodWithDayIndexRange:calendarCache:error:]_block_invoke.359
- ___block_literal_global.301
- ___block_literal_global.306
- ___block_literal_global.308
- ___block_literal_global.310
- ___block_literal_global.312
- ___block_literal_global.314
- ___block_literal_global.316
- ___block_literal_global.321
- ___block_literal_global.350
- ___block_literal_global.352
- ___block_literal_global.354
- ___block_literal_global.391
- ___block_literal_global.397
- ___block_literal_global.484
- ___block_literal_global.513
- __swift_FORCE_LOAD_$_swiftAVFoundation
- __swift_FORCE_LOAD_$_swiftAVFoundation_$_HealthMenstrualCyclesDaemon
- __swift_FORCE_LOAD_$_swiftCoreAudio
- __swift_FORCE_LOAD_$_swiftCoreAudio_$_HealthMenstrualCyclesDaemon
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCoreMIDI_$_HealthMenstrualCyclesDaemon
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftCoreMedia_$_HealthMenstrualCyclesDaemon
- __swift_FORCE_LOAD_$_swiftSpatial
- __swift_FORCE_LOAD_$_swiftSpatial_$_HealthMenstrualCyclesDaemon
- __swift_FORCE_LOAD_$_swiftUIKit
- __swift_FORCE_LOAD_$_swiftUIKit_$_HealthMenstrualCyclesDaemon
CStrings:
+ "invalidateRelevancesOfKind:inBundle:completion:"
+ "sharedWidgetService"
+ "v16@?0@\"NSError\"8"

```
