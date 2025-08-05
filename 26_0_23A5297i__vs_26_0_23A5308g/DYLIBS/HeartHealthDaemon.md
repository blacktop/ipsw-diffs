## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

-6100.0.0.0.0
-  __TEXT.__text: 0x4ba30
+6105.0.0.0.0
+  __TEXT.__text: 0x4bc04
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x3be4
+  __TEXT.__objc_methlist: 0x3c24
   __TEXT.__const: 0x1e0
   __TEXT.__gcc_except_tab: 0xa68
-  __TEXT.__cstring: 0x3aae
+  __TEXT.__cstring: 0x3b01
   __TEXT.__oslogstring: 0x877c
   __TEXT.__ustring: 0x86
-  __TEXT.__unwind_info: 0x1120
-  __TEXT.__objc_classname: 0x1628
-  __TEXT.__objc_methname: 0xdac5
+  __TEXT.__unwind_info: 0x1138
+  __TEXT.__objc_classname: 0x1650
+  __TEXT.__objc_methname: 0xdaea
   __TEXT.__objc_methtype: 0x2fab
-  __TEXT.__objc_stubs: 0x8560
-  __DATA_CONST.__got: 0xbb8
-  __DATA_CONST.__const: 0x11f8
-  __DATA_CONST.__objc_classlist: 0x240
+  __TEXT.__objc_stubs: 0x8580
+  __DATA_CONST.__got: 0xbc0
+  __DATA_CONST.__const: 0x1278
+  __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2868
+  __DATA_CONST.__objc_selrefs: 0x2878
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x4b0
   __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x31a0
-  __AUTH_CONST.__objc_const: 0x7380
+  __AUTH_CONST.__cfstring: 0x3240
+  __AUTH_CONST.__objc_const: 0x7410
   __AUTH_CONST.__objc_intobj: 0xc90
   __AUTH_CONST.__objc_doubleobj: 0x3d0
   __AUTH_CONST.__objc_arrayobj: 0xf0

   __DATA.__objc_ivar: 0x48c
   __DATA.__data: 0x18d0
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0xff0
+  __DATA_DIRTY.__objc_data: 0x1040
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 582496A2-587F-305B-BA55-4555AC8222EB
-  Functions: 1497
-  Symbols:   6074
-  CStrings:  3430
+  UUID: 8D0AA916-C903-3B51-BCA5-9B8538B5DE4B
+  Functions: 1502
+  Symbols:   6095
+  CStrings:  3443
 
Symbols:
+ +[HDHRHeartCLogEntity privateSubEntities]
+ +[HDHRHeartCLogScheduleTimeIntervalEntity columnDefinitionsWithCount:]
+ +[HDHRHeartCLogScheduleTimeIntervalEntity databaseTable]
+ +[HDHRHeartCLogScheduleTimeIntervalEntity foreignKeys]
+ +[HDHRHeartCLogScheduleTimeIntervalEntity protectionClass]
+ _HDHRHeartCLogScheduleTimeIntervalEntityDayWindowType
+ _HDHRHeartCLogScheduleTimeIntervalEntityOwnerID
+ _HDHRHeartCLogScheduleTimeIntervalEntityScheduleTime
+ _HDHRHeartCLogScheduleTimeIntervalEntityTableName
+ _OBJC_CLASS_$_HDHRHeartCLogScheduleTimeIntervalEntity
+ _OBJC_METACLASS_$_HDHRHeartCLogScheduleTimeIntervalEntity
+ __OBJC_$_CLASS_METHODS_HDHRHeartCLogScheduleTimeIntervalEntity
+ __OBJC_CLASS_RO_$_HDHRHeartCLogScheduleTimeIntervalEntity
+ __OBJC_METACLASS_RO_$_HDHRHeartCLogScheduleTimeIntervalEntity
+ ___103-[HDHRHeartRateNotificationsFeatureAvailabilityManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.358
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.320
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.320.cold.1
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.321
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.321.cold.1
+ ___104-[HKHRAFibBurdenJulianDayMajorityTimeZoneDeterminer determineJulianDayToMajorityTimeZoneForRange:error:]_block_invoke.322
+ ___104-[HRAtrialFibrillationEventDetector _queue_analyzeCurrentConfirmationCycleSamples:withAlgorithmVersion:]_block_invoke.343
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.325
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.325.cold.1
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.326
+ ___160-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.310
+ ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.362
+ ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.362.cold.1
+ ___35-[HDHRNotificationAnalytics submit]_block_invoke.313
+ ___35-[HDHRNotificationAnalytics submit]_block_invoke.313.cold.1
+ ___35-[HDHRNotificationAnalytics submit]_block_invoke.313.cold.2
+ ___61-[HDHRHealthLiteDataCollector _assertionManagerStateChanged:]_block_invoke.350
+ ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.326
+ ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.326.cold.1
+ ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.330
+ ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.330.cold.1
+ ___74-[HRAtrialFibrillationEventDetector _queue_seriesSamplesAdded:lastAnchor:]_block_invoke.331
+ ___75-[HDHRHealthKitSyncManager triggerImmediateSyncWithReason:loggingCategory:]_block_invoke.301
+ ___76-[HRAtrialFibrillationEventDetector _queue_analyzeTachogramsSinceLastAnchor]_block_invoke.328
+ ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.311
+ ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.315
+ ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.403
+ ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.403.cold.1
+ ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.300
+ ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.300.cold.1
+ ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.296
+ ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.296.cold.1
+ ___block_literal_global.295
+ ___block_literal_global.323
+ ___block_literal_global.327
+ ___block_literal_global.329
+ ___block_literal_global.333
+ ___block_literal_global.337
+ ___block_literal_global.346
+ ___block_literal_global.357
+ ___block_literal_global.359
+ ___block_literal_global.363
+ ___block_literal_global.365
+ ___block_literal_global.367
+ ___block_literal_global.407
+ _objc_msgSend$defaultForeignKey
- ___103-[HDHRHeartRateNotificationsFeatureAvailabilityManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.355
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.317
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.317.cold.1
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.318
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.318.cold.1
- ___104-[HKHRAFibBurdenJulianDayMajorityTimeZoneDeterminer determineJulianDayToMajorityTimeZoneForRange:error:]_block_invoke.319
- ___104-[HRAtrialFibrillationEventDetector _queue_analyzeCurrentConfirmationCycleSamples:withAlgorithmVersion:]_block_invoke.340
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.322
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.322.cold.1
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.323
- ___160-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.307
- ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.359
- ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.359.cold.1
- ___35-[HDHRNotificationAnalytics submit]_block_invoke.310
- ___35-[HDHRNotificationAnalytics submit]_block_invoke.310.cold.1
- ___35-[HDHRNotificationAnalytics submit]_block_invoke.310.cold.2
- ___61-[HDHRHealthLiteDataCollector _assertionManagerStateChanged:]_block_invoke.347
- ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.323
- ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.323.cold.1
- ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.327
- ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.327.cold.1
- ___74-[HRAtrialFibrillationEventDetector _queue_seriesSamplesAdded:lastAnchor:]_block_invoke.328
- ___75-[HDHRHealthKitSyncManager triggerImmediateSyncWithReason:loggingCategory:]_block_invoke.298
- ___76-[HRAtrialFibrillationEventDetector _queue_analyzeTachogramsSinceLastAnchor]_block_invoke.325
- ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.308
- ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.309
- ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.400
- ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.400.cold.1
- ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.297
- ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.297.cold.1
- ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.293
- ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.293.cold.1
- ___block_literal_global.292
- ___block_literal_global.320
- ___block_literal_global.324
- ___block_literal_global.326
- ___block_literal_global.330
- ___block_literal_global.334
- ___block_literal_global.343
- ___block_literal_global.354
- ___block_literal_global.356
- ___block_literal_global.360
- ___block_literal_global.361
- ___block_literal_global.362
- ___block_literal_global.404
CStrings:
+ "BLOB NOT NULL"
+ "HDHRHeartCLogScheduleTimeIntervalEntity"
+ "c_log_id"
+ "day_window_type"
+ "defaultForeignKey"
+ "heart_c_log_schedule_interval"
+ "privateSubEntities"
+ "schedule_time"

```
