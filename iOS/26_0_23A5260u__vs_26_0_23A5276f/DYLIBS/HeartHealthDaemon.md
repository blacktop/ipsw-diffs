## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

-6074.1.2.4.0
+6087.1.2.1.0
   __TEXT.__text: 0x4ba30
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x3bdc
+  __TEXT.__objc_methlist: 0x3bcc
   __TEXT.__const: 0x1e0
   __TEXT.__gcc_except_tab: 0xa68
   __TEXT.__cstring: 0x3aae

   __TEXT.__ustring: 0x86
   __TEXT.__unwind_info: 0x1118
   __TEXT.__objc_classname: 0x1628
-  __TEXT.__objc_methname: 0xdaca
-  __TEXT.__objc_methtype: 0x2fe6
+  __TEXT.__objc_methname: 0xda8e
+  __TEXT.__objc_methtype: 0x2f75
   __TEXT.__objc_stubs: 0x8560
   __DATA_CONST.__got: 0xbb8
   __DATA_CONST.__const: 0x11f8

   __DATA_CONST.__objc_catlist: 0x60
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2868
+  __DATA_CONST.__objc_selrefs: 0x2860
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0x4b0
   __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0x400
   __AUTH_CONST.__cfstring: 0x31a0
-  __AUTH_CONST.__objc_const: 0x7380
+  __AUTH_CONST.__objc_const: 0x7378
   __AUTH_CONST.__objc_intobj: 0xc90
   __AUTH_CONST.__objc_doubleobj: 0x3d0
   __AUTH_CONST.__objc_arrayobj: 0xf0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CE7A6B8B-FCF0-3B68-944F-F063C6E32869
+  UUID: CE599281-C0B3-3F0A-9441-7D662146B975
   Functions: 1497
   Symbols:   6073
-  CStrings:  3430
+  CStrings:  3427
 
Symbols:
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
+ "Error retrieving most recent workout : %@"
- "Error retreiving most recent workout : %@"
- "associationsUpdatedForObject:subObject:type:objects:anchor:"
- "v56@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32@\"NSArray\"40@\"NSNumber\"48"
- "v56@0:8@16@24Q32@40@48"

```
