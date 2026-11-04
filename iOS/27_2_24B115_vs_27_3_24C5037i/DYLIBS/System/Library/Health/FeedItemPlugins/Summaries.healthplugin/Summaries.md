## Summaries

> `/System/Library/Health/FeedItemPlugins/Summaries.healthplugin/Summaries`

```diff

-7027.1.56.2.9
-  __TEXT.__text: 0x1ee090
+7027.2.13.0.0
+  __TEXT.__text: 0x1ee914
   __TEXT.__objc_methlist: 0x3f0
-  __TEXT.__const: 0xb464
+  __TEXT.__const: 0xb4a4
   __TEXT.__constg_swiftt: 0x4974
-  __TEXT.__swift5_typeref: 0x3de0
-  __TEXT.__swift5_fieldmd: 0x2f78
+  __TEXT.__swift5_typeref: 0x3da2
+  __TEXT.__swift5_fieldmd: 0x2f90
   __TEXT.__swift5_builtin: 0x17c
-  __TEXT.__swift5_reflstr: 0x43cb
+  __TEXT.__swift5_reflstr: 0x43eb
   __TEXT.__swift5_assocty: 0x1160
   __TEXT.__swift5_proto: 0x860
   __TEXT.__swift5_types: 0x444
-  __TEXT.__swift5_capture: 0x11d8
-  __TEXT.__oslogstring: 0x5701
-  __TEXT.__cstring: 0x68b9
-  __TEXT.__swift_as_entry: 0x284
-  __TEXT.__swift_as_ret: 0x2fc
-  __TEXT.__swift_as_cont: 0x1094
+  __TEXT.__swift5_capture: 0x1154
+  __TEXT.__oslogstring: 0x57d1
+  __TEXT.__cstring: 0x6779
+  __TEXT.__swift_as_entry: 0x270
+  __TEXT.__swift_as_ret: 0x2e4
+  __TEXT.__swift_as_cont: 0x13f0
   __TEXT.__swift5_protos: 0x5c
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x6bb0
-  __TEXT.__eh_frame: 0xab20
+  __TEXT.__unwind_info: 0x6ad0
+  __TEXT.__eh_frame: 0xa440
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1348
+  __DATA_CONST.__objc_selrefs: 0x12e0
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x6cb8
-  __AUTH_CONST.__objc_const: 0x3780
-  __AUTH_CONST.__auth_got: 0x4650
+  __AUTH_CONST.__const: 0x6bc8
+  __AUTH_CONST.__objc_const: 0x3740
+  __AUTH_CONST.__auth_got: 0x46f0
   __AUTH.__objc_data: 0x908
-  __AUTH.__data: 0x3368
-  __DATA.__data: 0x29f8
+  __AUTH.__data: 0x3378
+  __DATA.__data: 0x2b40
   __DATA.__objc_stublist: 0x38
   __DATA.__common: 0x250
   __DATA_DIRTY.__objc_data: 0xd90
-  __DATA_DIRTY.__data: 0x62d8
+  __DATA_DIRTY.__data: 0x6208
   __DATA_DIRTY.__bss: 0x5680
-  __DATA_DIRTY.__common: 0x210
+  __DATA_DIRTY.__common: 0x200
   - /System/Library/Frameworks/Charts.framework/Charts
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/HealthPlatformFoundation.framework/HealthPlatformFoundation
   - /System/Library/PrivateFrameworks/HealthToolbox.framework/HealthToolbox
   - /System/Library/PrivateFrameworks/HealthUI.framework/HealthUI
+  - /System/Library/PrivateFrameworks/HealthUtilities.framework/HealthUtilities
   - /System/Library/PrivateFrameworks/HealthVisualization.framework/HealthVisualization
   - /System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth
   - /System/Library/PrivateFrameworks/MentalHealthUI.framework/MentalHealthUI

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6961
-  Symbols:   530
-  CStrings:  917
+  Functions: 7187
+  Symbols:   525
+  CStrings:  914
 
Symbols:
+ _OBJC_CLASS_$_HKPauseRingsSchedule
+ _swift_unknownObjectRetain_n
- _FITypicalDayActivityModelDaysOfActivityHistory
- _OBJC_CLASS_$_FITypicalDayActivityModel
- _OBJC_CLASS_$_HKSleepDaySummaryQuery
- _OBJC_CLASS_$_HKSleepPeriod
- __HKCategoryTypeIdentifierWristEvent
- _objc_release_x9
- _swift_asyncLet_get
CStrings:
+ "ActivityDashboardExecutor:fetchPauseRingsResumeDate"
+ "Unexpected nil date interval on sleep session"
+ "Unexpected no sleep sessions in sleep day summary"
+ "[%s]: Activity move mode state updated. Updating data sources with activityMoveModeState: %s"
+ "[%{public}s] Anchor did not have requested 1 day of sleep scores"
+ "[%{public}s] Can't make a work plan due to unexpected missing characteristic anchor"
+ "[%{public}s] Missing required anchor; skipping"
+ "[%{public}s] No sleep score day summary anchor; skipping"
+ "[%{public}s] Sleep day summary and calendar change input signals are out of sync; skipping"
+ "[%{public}s] Work plan unexpectedly has nil sleepScoreDaySummary"
+ "data-logging-promotion-tile"
- ":sleepDaySummaries"
- "SleepDurationCurrentValueSharableModelStep:makeCurrentValue"
- "TypicalDayActivityProgressFetcher:fetchFirstOnWristDateToday"
- "Unexpected no periods in sleep day summary"
- "[%s]: Profile information updated. Updating data sources with activityMoveModeState: %s"
- "[%{public}s] Missing calendar-change anchor; skipping"
- "[TypicalDayActivityProgressFetcher] Activity summary prefetch failed: %{public}@"
- "[TypicalDayActivityProgressFetcher] Failed to derive history range; skipping."
- "[TypicalDayActivityProgressFetcher] Wrist-on prefetch failed: %{public}@"
- "com.apple.health.summaries.data-logging"
- "com.apple.health.summaries.data-logging-promotion-tile"
- "com.apple.health.summaries.wheelchair-setting"
- "com.apple.health.summaries.wheelchair-setting-summary-sharing"
- "makeCurrentValue()"
```
