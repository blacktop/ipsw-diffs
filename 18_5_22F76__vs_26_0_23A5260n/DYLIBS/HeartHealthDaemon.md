## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x4aef8
-  __TEXT.__auth_stubs: 0xbe0
-  __TEXT.__objc_methlist: 0x3ab4
+6074.1.2.4.0
+  __TEXT.__text: 0x4ba30
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x3bdc
   __TEXT.__const: 0x1e0
-  __TEXT.__gcc_except_tab: 0xa6c
-  __TEXT.__cstring: 0x37d7
-  __TEXT.__oslogstring: 0x84bd
-  __TEXT.__unwind_info: 0x10c0
-  __TEXT.__objc_classname: 0x1686
-  __TEXT.__objc_methname: 0xd56a
-  __TEXT.__objc_methtype: 0x2fc4
-  __TEXT.__objc_stubs: 0x84c0
-  __DATA_CONST.__got: 0xb98
-  __DATA_CONST.__const: 0x1170
+  __TEXT.__gcc_except_tab: 0xa68
+  __TEXT.__cstring: 0x3aae
+  __TEXT.__oslogstring: 0x877c
+  __TEXT.__ustring: 0x86
+  __TEXT.__unwind_info: 0x1118
+  __TEXT.__objc_classname: 0x1628
+  __TEXT.__objc_methname: 0xdaca
+  __TEXT.__objc_methtype: 0x2fe6
+  __TEXT.__objc_stubs: 0x8560
+  __DATA_CONST.__got: 0xbb8
+  __DATA_CONST.__const: 0x11f8
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x218
+  __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27c8
+  __DATA_CONST.__objc_selrefs: 0x2868
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x490
-  __AUTH_CONST.__auth_got: 0x600
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x2fa0
-  __AUTH_CONST.__objc_const: 0x7218
+  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_arraydata: 0x4b0
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x31a0
+  __AUTH_CONST.__objc_const: 0x7380
   __AUTH_CONST.__objc_intobj: 0xc90
   __AUTH_CONST.__objc_doubleobj: 0x3d0
-  __AUTH_CONST.__objc_arrayobj: 0xd8
-  __AUTH.__objc_data: 0x730
-  __DATA.__objc_ivar: 0x46c
-  __DATA.__data: 0x1930
+  __AUTH_CONST.__objc_arrayobj: 0xf0
+  __AUTH.__objc_data: 0x690
+  __DATA.__objc_ivar: 0x48c
+  __DATA.__data: 0x18d0
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0xf50
+  __DATA_DIRTY.__objc_data: 0xff0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AfibBurden.framework/AfibBurden
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
+  - /System/Library/PrivateFrameworks/BiomePubSub.framework/BiomePubSub
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 326085F8-B10B-38C3-ACA2-AD4EF42131BF
-  Functions: 1468
-  Symbols:   6045
-  CStrings:  3355
+  UUID: CE7A6B8B-FCF0-3B68-944F-F063C6E32869
+  Functions: 1497
+  Symbols:   6073
+  CStrings:  3430
 
Symbols:
+ +[HDHRHeartCLogEntity columnDefinitionsWithCount:]
+ +[HDHRHeartCLogEntity databaseTable]
+ +[HDHRHeartCLogEntity protectionClass]
+ -[HDHRCardioFitnessAnalyticsDailyEventDataSource initWithProfile:privacyDefaults:heartRateDefaults:]
+ -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager _requestCacheUpdateWorkWithError:]
+ -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager featureAvailabilityExtensionDidUpdatePairedDeviceCapability:]
+ -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager featureAvailabilityExtensionDidUpdatePairedDeviceCapability:].cold.1
+ -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager featureAvailabilityExtensionDidUpdateRegionAvailability:].cold.1
+ -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager featureAvailabilityExtensionOnboardingCompletionDataDidBecomeAvailable:].cold.1
+ -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager featureAvailabilityProvidingDidUpdateOnboardingCompletion:].cold.1
+ -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager initWithV1FeatureAvailabilityManager:v2FeatureAvailabilityManager:cacheDefaults:protectedDataOperationForCaching:]
+ -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager initWithV1FeatureAvailabilityManager:v2FeatureAvailabilityManager:cacheDefaults:protectedDataOperationForCaching:].cold.1
+ -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager performWorkForOperation:profile:databaseAccessibilityAssertion:completion:]
+ -[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager featureAvailabilityExtensionDidUpdatePairedDeviceCapability:]
+ -[HDHRNotificationManager setUnitTest_notificationForExpiredEventSkipped:]
+ -[HDHRNotificationManager setUnitTest_notificationForNonLocalDeviceSourceSkipped:]
+ -[HDHRNotificationManager setUnitTest_notificationForUnsupportedEventSkipped:]
+ -[HDHRNotificationManager setUnitTest_userNotificationCenter:]
+ -[HDHRNotificationManager unitTest_notificationForExpiredEventSkipped]
+ -[HDHRNotificationManager unitTest_notificationForNonLocalDeviceSourceSkipped]
+ -[HDHRNotificationManager unitTest_notificationForUnsupportedEventSkipped]
+ -[HDHRNotificationManager unitTest_userNotificationCenter]
+ -[HDHeartPluginProtectedDatabaseSchema luck_addMigrationStepsForSchemaName:migrator:]
+ -[HDHeartRateWidgetDataManager _latestWorkoutSample]
+ -[HDHeartRateWidgetDataManager _latestWorkoutSample].cold.1
+ -[HDHeartRateWidgetDataManager _reloadWorkoutRelevanceAndWidgetWithReason:for:]
+ -[HDHeartRateWidgetDataManager _watchSamplesFrom:]
+ -[HDHeartRateWidgetDataManager didRequestHRWidgetReloadHandler]
+ -[HDHeartRateWidgetDataManager didRequestWorkoutWidgetReloadHandler]
+ -[HDHeartRateWidgetDataManager initWithProfile:latestWorkoutFetchOperation:]
+ -[HDHeartRateWidgetDataManager latestWorkoutFrom:]
+ -[HDHeartRateWidgetDataManager performWorkForOperation:profile:databaseAccessibilityAssertion:completion:]
+ -[HDHeartRateWidgetDataManager setDidRequestHRWidgetReloadHandler:]
+ -[HDHeartRateWidgetDataManager setDidRequestWorkoutWidgetReloadHandler:]
+ -[HKHRDatabaseAnalysisSchedulerImpl _activityCompletion]
+ -[HKHRDatabaseAnalysisSchedulerImpl _runActivity:withCompletion:].cold.2
+ -[HKHRDatabaseAnalysisSchedulerImpl _setActivityCompletion:]
+ -[HKHRDatabaseAnalysisSchedulerImpl initWithProfile:identifier:loggingCategory:maximumDelay:retryDelay:breadcrumbManager:gatedActivityFactory:persistentStateDefaults:operation:]
+ -[HKHRDatabaseAnalysisSchedulerImpl performWorkForOperation:profile:databaseAccessibilityAssertion:completion:]
+ -[HKHRDatabaseAnalysisSchedulerImpl performWorkForOperation:profile:databaseAccessibilityAssertion:completion:].cold.1
+ GCC_except_table1
+ GCC_except_table24
+ _BiomeLibrary
+ _HDDataEntityPredicateForObjectsFromAppleWatchSources
+ _HDHRHeartCLogEntityPropertyEndDate
+ _HDHRHeartCLogEntityPropertyModifiedDate
+ _HDHRHeartCLogEntityPropertyScheduleType
+ _HDHRHeartCLogEntityPropertyStartDate
+ _HDHRHeartCLogEntityPropertyState
+ _HDHRHeartCLogEntityPropertyType
+ _HDHRHeartCLogEntityPropertyUUID
+ _HDHRHeartCLogEntityTableName
+ _HKLogHeartRateCategory
+ _HKLogHeartRhythmCategory
+ _OBJC_CLASS_$_HDHRHeartCLogEntity
+ _OBJC_IVAR_$_HDHRCardioFitnessAnalyticsDailyEventDataSource._heartRateDefaults
+ _OBJC_IVAR_$_HDHRCardioFitnessAnalyticsDailyEventDataSource._privacyDefaults
+ _OBJC_IVAR_$_HDHRElectrocardiogramRecordingFeatureAvailabilityManager._protectedDataOperationForCaching
+ _OBJC_IVAR_$_HDHRNotificationManager._unitTest_notificationForExpiredEventSkipped
+ _OBJC_IVAR_$_HDHRNotificationManager._unitTest_notificationForNonLocalDeviceSourceSkipped
+ _OBJC_IVAR_$_HDHRNotificationManager._unitTest_notificationForUnsupportedEventSkipped
+ _OBJC_IVAR_$_HDHRNotificationManager._unitTest_userNotificationCenter
+ _OBJC_IVAR_$_HDHeartRateWidgetDataManager._didRequestHRWidgetReloadHandler
+ _OBJC_IVAR_$_HDHeartRateWidgetDataManager._didRequestWorkoutWidgetReloadHandler
+ _OBJC_IVAR_$_HDHeartRateWidgetDataManager._latestWorkoutFetchOperation
+ _OBJC_IVAR_$_HKHRDatabaseAnalysisSchedulerImpl._lock_activityCompletion
+ _OBJC_IVAR_$_HKHRDatabaseAnalysisSchedulerImpl._operation
+ _OBJC_METACLASS_$_HDHRHeartCLogEntity
+ __HDAddHeartCLogTables
+ __OBJC_$_CLASS_METHODS_HDHRHeartCLogEntity
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDFeatureAvailabilityExtensionObserver
+ __OBJC_CLASS_RO_$_HDHRHeartCLogEntity
+ __OBJC_METACLASS_RO_$_HDHRHeartCLogEntity
+ ___103-[HDHRHeartRateNotificationsFeatureAvailabilityManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.355
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.317
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.317.cold.1
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.318
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.318.cold.1
+ ___104-[HKHRAFibBurdenJulianDayMajorityTimeZoneDeterminer determineJulianDayToMajorityTimeZoneForRange:error:]_block_invoke.319
+ ___104-[HRAtrialFibrillationEventDetector _queue_analyzeCurrentConfirmationCycleSamples:withAlgorithmVersion:]_block_invoke.340
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.322
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.322.cold.1
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.323
+ ___111-[HKHRDatabaseAnalysisSchedulerImpl performWorkForOperation:profile:databaseAccessibilityAssertion:completion:]_block_invoke
+ ___120-[HDHRElectrocardiogramRecordingFeatureAvailabilityManager featureAvailabilityExtensionDidUpdatePairedDeviceCapability:]_block_invoke
+ ___122-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager featureAvailabilityExtensionDidUpdatePairedDeviceCapability:]_block_invoke
+ ___160-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.307
+ ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.359
+ ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.359.cold.1
+ ___35-[HDHRNotificationAnalytics submit]_block_invoke.310
+ ___35-[HDHRNotificationAnalytics submit]_block_invoke.310.cold.1
+ ___35-[HDHRNotificationAnalytics submit]_block_invoke.310.cold.2
+ ___44-[HDHeartRateWidgetDataManager daemonReady:]_block_invoke.cold.1
+ ___50-[HDHeartRateWidgetDataManager latestWorkoutFrom:]_block_invoke
+ ___61-[HDHRHealthLiteDataCollector _assertionManagerStateChanged:]_block_invoke.347
+ ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.327
+ ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.327.cold.1
+ ___74-[HRAtrialFibrillationEventDetector _queue_seriesSamplesAdded:lastAnchor:]_block_invoke.328
+ ___75-[HDHRHealthKitSyncManager triggerImmediateSyncWithReason:loggingCategory:]_block_invoke.298
+ ___76-[HDHeartRateWidgetDataManager initWithProfile:latestWorkoutFetchOperation:]_block_invoke
+ ___76-[HRAtrialFibrillationEventDetector _queue_analyzeTachogramsSinceLastAnchor]_block_invoke.325
+ ___79-[HDHeartRateWidgetDataManager _reloadWorkoutRelevanceAndWidgetWithReason:for:]_block_invoke
+ ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.308
+ ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.312
+ ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.400
+ ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.400.cold.1
+ ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.297
+ ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.297.cold.1
+ ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.293
+ ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.293.cold.1
+ ___block_descriptor_56_e8_32s40bs48bs_e20_v24?0q8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.292
+ ___block_literal_global.320
+ ___block_literal_global.324
+ ___block_literal_global.326
+ ___block_literal_global.330
+ ___block_literal_global.334
+ ___block_literal_global.343
+ ___block_literal_global.354
+ ___block_literal_global.356
+ ___block_literal_global.360
+ ___block_literal_global.362
+ ___block_literal_global.364
+ ___block_literal_global.404
+ _kHKHRAFibBurdenRescindedNotificationCategoryIdentifier
+ _objc_msgSend$ComputedMode
+ _objc_msgSend$HRCoordinator
+ _objc_msgSend$UserFocus
+ _objc_msgSend$_activityCompletion
+ _objc_msgSend$_latestWorkoutSample
+ _objc_msgSend$_reloadWorkoutRelevanceAndWidgetWithReason:for:
+ _objc_msgSend$_requestCacheUpdateWorkWithError:
+ _objc_msgSend$_setActivityCompletion:
+ _objc_msgSend$_watchSamplesFrom:
+ _objc_msgSend$autoupdatingCurrentCalendar
+ _objc_msgSend$compoundPredicateWithPredicate:otherPredicate:
+ _objc_msgSend$deprecateIRN1
+ _objc_msgSend$featureAvailabilityExtensionDidUpdatePairedDeviceCapability:
+ _objc_msgSend$initWithAlarmFiredDate:xpcActivityFiredDate:protectedDataOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:
+ _objc_msgSend$initWithProfile:identifier:loggingCategory:maximumDelay:retryDelay:breadcrumbManager:gatedActivityFactory:persistentStateDefaults:operation:
+ _objc_msgSend$initWithProfile:latestWorkoutFetchOperation:
+ _objc_msgSend$initWithProfile:privacyDefaults:heartRateDefaults:
+ _objc_msgSend$initWithV1FeatureAvailabilityManager:v2FeatureAvailabilityManager:cacheDefaults:protectedDataOperationForCaching:
+ _objc_msgSend$latestWorkoutFrom:
+ _objc_msgSend$luck_addMigrationStepsForSchemaName:migrator:
+ _objc_msgSend$publisher
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$starting
- -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager _observerQueue_updateCachedOnboardingVersionIfNeeded]
- -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager featureAvailabilityProvidingDidUpdatePairedDeviceCapability:]
- -[HDHRElectrocardiogramRecordingFeatureAvailabilityManager initWithV1FeatureAvailabilityManager:v2FeatureAvailabilityManager:cacheDefaults:]
- -[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager featureAvailabilityProvidingDidUpdatePairedDeviceCapability:]
- -[HDHeartPluginProtectedDatabaseSchema future_addMigrationStepsForSchemaName:migrator:]
- -[HDHeartRateWidgetDataManager _reloadWorkoutRelevanceAndWidgetWithReason:]
- -[HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl .cxx_destruct]
- -[HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl initWithProfile:identifier:]
- -[HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl takeAssertionWithError:]
- -[HKHRDatabaseAnalysisSchedulerImpl _runMaintenanceOperationForActivity:assertion:withCompletion:]
- -[HKHRDatabaseAnalysisSchedulerImpl _runMaintenanceOperationForActivity:assertion:withCompletion:].cold.1
- -[HKHRDatabaseAnalysisSchedulerImpl initWithProfile:identifier:loggingCategory:maximumDelay:retryDelay:breadcrumbManager:gatedActivityFactory:assertionProvider:persistentStateDefaults:]
- GCC_except_table12
- GCC_except_table30
- _OBJC_CLASS_$_BMStreams
- _OBJC_CLASS_$_HDMutableDatabaseTransactionContext
- _OBJC_CLASS_$_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl
- _OBJC_IVAR_$_HDHeartRateWidgetDataManager._relevanceReloadOperation
- _OBJC_IVAR_$_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl._identifier
- _OBJC_IVAR_$_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl._profile
- _OBJC_IVAR_$_HKHRDatabaseAnalysisSchedulerImpl._assertionProvider
- _OBJC_METACLASS_$_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl
- __OBJC_$_INSTANCE_METHODS_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl
- __OBJC_$_INSTANCE_VARIABLES_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProvider
- __OBJC_$_PROTOCOL_METHOD_TYPES_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProvider
- __OBJC_CLASS_PROTOCOLS_$_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl
- __OBJC_CLASS_RO_$_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl
- __OBJC_LABEL_PROTOCOL_$_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProvider
- __OBJC_METACLASS_RO_$_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl
- __OBJC_PROTOCOL_$_HKHRDatabaseAnalysisSchedulerDatabaseAssertionProvider
- ___103-[HDHRHeartRateNotificationsFeatureAvailabilityManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.352
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.314
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.314.cold.1
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.315
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.315.cold.1
- ___104-[HKHRAFibBurdenJulianDayMajorityTimeZoneDeterminer determineJulianDayToMajorityTimeZoneForRange:error:]_block_invoke.316
- ___104-[HRAtrialFibrillationEventDetector _queue_analyzeCurrentConfirmationCycleSamples:withAlgorithmVersion:]_block_invoke.337
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.319
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.319.cold.1
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.320
- ___120-[HDHRElectrocardiogramRecordingFeatureAvailabilityManager featureAvailabilityProvidingDidUpdatePairedDeviceCapability:]_block_invoke
- ___122-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager featureAvailabilityProvidingDidUpdatePairedDeviceCapability:]_block_invoke
- ___160-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.304
- ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.355
- ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.355.cold.1
- ___35-[HDHRNotificationAnalytics submit]_block_invoke.308
- ___35-[HDHRNotificationAnalytics submit]_block_invoke.308.cold.1
- ___35-[HDHRNotificationAnalytics submit]_block_invoke.308.cold.2
- ___48-[HDHeartRateWidgetDataManager initWithProfile:]_block_invoke
- ___48-[HDHeartRateWidgetDataManager initWithProfile:]_block_invoke_2
- ___61-[HDHRHealthLiteDataCollector _assertionManagerStateChanged:]_block_invoke.343
- ___65-[HKHRDatabaseAnalysisSchedulerImpl _runActivity:withCompletion:]_block_invoke
- ___65-[HKHRDatabaseAnalysisSchedulerImpl _runActivity:withCompletion:]_block_invoke_2
- ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.324
- ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.324.cold.1
- ___74-[HRAtrialFibrillationEventDetector _queue_seriesSamplesAdded:lastAnchor:]_block_invoke.325
- ___75-[HDHRHealthKitSyncManager triggerImmediateSyncWithReason:loggingCategory:]_block_invoke.295
- ___75-[HDHeartRateWidgetDataManager _reloadWorkoutRelevanceAndWidgetWithReason:]_block_invoke
- ___76-[HRAtrialFibrillationEventDetector _queue_analyzeTachogramsSinceLastAnchor]_block_invoke.322
- ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.305
- ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.306
- ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.397
- ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.397.cold.1
- ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.294
- ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.294.cold.1
- ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.290
- ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.290.cold.1
- ___98-[HKHRDatabaseAnalysisSchedulerImpl _runMaintenanceOperationForActivity:assertion:withCompletion:]_block_invoke
- ___98-[HKHRDatabaseAnalysisSchedulerImpl _runMaintenanceOperationForActivity:assertion:withCompletion:]_block_invoke_2
- ___block_descriptor_48_e8_32s40bs_e20_v24?0q8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40bs_e9_B16?0^8ls32l8s40l8
- ___block_descriptor_64_e8_32s40s48bs56bs_e20_v24?0q8"NSError"16ls48l8s32l8s40l8s56l8
- ___block_descriptor_64_e8_32s40s48s56bs_e14_v16?0?<v?>8ls32l8s40l8s48l8s56l8
- ___block_literal_global.289
- ___block_literal_global.317
- ___block_literal_global.321
- ___block_literal_global.323
- ___block_literal_global.327
- ___block_literal_global.331
- ___block_literal_global.340
- ___block_literal_global.351
- ___block_literal_global.353
- ___block_literal_global.357
- ___block_literal_global.358
- ___block_literal_global.359
- ___block_literal_global.401
- _objc_msgSend$_isFirstSampleWorkout:
- _objc_msgSend$_observerQueue_updateCachedOnboardingVersionIfNeeded
- _objc_msgSend$_reloadWorkoutRelevanceAndWidgetWithReason:
- _objc_msgSend$_runMaintenanceOperationForActivity:assertion:withCompletion:
- _objc_msgSend$addAccessibilityAssertion:
- _objc_msgSend$featureAvailabilityProvidingDidUpdatePairedDeviceCapability:
- _objc_msgSend$future_addMigrationStepsForSchemaName:migrator:
- _objc_msgSend$initWithAlarmFiredDate:xpcActivityFiredDate:maintenanceOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:
- _objc_msgSend$initWithProfile:identifier:
- _objc_msgSend$initWithProfile:identifier:loggingCategory:maximumDelay:retryDelay:breadcrumbManager:gatedActivityFactory:assertionProvider:persistentStateDefaults:
- _objc_msgSend$initWithV1FeatureAvailabilityManager:v2FeatureAvailabilityManager:cacheDefaults:
- _objc_msgSend$isStarting
- _objc_msgSend$performWithTransactionContext:error:block:
- _objc_msgSend$publisherFromStartTime:
- _objc_msgSend$removeObserver:
- _objc_msgSend$setCacheScope:
- _objc_msgSend$takeAssertionWithError:
- _objc_msgSend$userFocusComputedMode
CStrings:
+ "38627122-E97A-4089-861C-81704B480D2E"
+ "Activity closure found nil. Fail to return activity result state"
+ "BLOB UNIQUE NOT NULL"
+ "CREATE TABLE heart_c_log (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, uuid BLOB UNIQUE NOT NULL, start_date REAL NOT NULL, end_date REAL, modified_date REAL NOT NULL, c_log_type INTEGER NOT NULL, schedule_type INTEGER NOT NULL, c_log_state INTEGER NOT NULL)"
+ "CREATE TABLE heart_c_log_schedule_interval (ROWID INTEGER PRIMARY KEY AUTOINCREMENT, c_log_id INTEGER NOT NULL REFERENCES heart_c_log (ROWID) ON DELETE CASCADE, schedule_time BLOB NOT NULL, day_window_type INTEGER NOT NULL)"
+ "ComputedMode"
+ "Error retreiving most recent workout : %@"
+ "H"
+ "HDHRHeartCLogEntity"
+ "HKHRDatabaseAnalysisSchedulerOperation"
+ "HRCoordinator"
+ "No samples found"
+ "REAL"
+ "SevenDayAnalysisBreadcrumbProtectedDataOperationRun"
+ "T@\"UNUserNotificationCenter\",&,N,V_unitTest_userNotificationCenter"
+ "T@?,C,N,V_unitTest_notificationForExpiredEventSkipped"
+ "T@?,C,N,V_unitTest_notificationForNonLocalDeviceSourceSkipped"
+ "T@?,C,N,V_unitTest_notificationForUnsupportedEventSkipped"
+ "T@?,C,V__unitTest_processTachograms"
+ "T@?,C,V_didRequestHRWidgetReloadHandler"
+ "T@?,C,V_didRequestWorkoutWidgetReloadHandler"
+ "Unable to take assertion after maintenance"
+ "UserFocus"
+ "WaitingForProtectedDataOperation"
+ "[%{public}@:%{public}@] Activity closure missing, attempting retry later"
+ "[%{public}@:%{public}@] Activity run but assertion returned nil, attempting retry later"
+ "[%{public}@:%{public}@] Unable to request work with error: %{public}@."
+ "[%{public}@] Error re-requesting work due to database inaccessibility: %{public}@"
+ "[%{public}@] Error requesting work for database available: %{public}@"
+ "[%{public}@] Error requesting work for init: %{public}@"
+ "[%{public}@] Error requesting work for onboarding completion update: %{public}@"
+ "[%{public}@] Error requesting work for paired device capability update: %{public}@"
+ "[%{public}@] Error requesting work for region availability update: %{public}@"
+ "[%{public}@] _reloadWorkoutRelevanceAndWidgetWithReason"
+ "[%{public}@] _reloadWorkoutRelevanceAndWidgetWithReason reason %@ delayInSeconds %lf"
+ "[%{public}@] _reloadWorkoutRelevanceAndWidgetWithReason reason %@ for %@"
+ "[%{public}@] error requesting maintenance work for fetching latest workout on healthd ready: %@"
+ "[%{public}@] latestWorkoutFrom in samples %@"
+ "[%{public}@] latestWorkoutFrom sortedSamples %@"
+ "_activityCompletion"
+ "_didRequestHRWidgetReloadHandler"
+ "_didRequestWorkoutWidgetReloadHandler"
+ "_heartRateDefaults"
+ "_latestWorkoutFetchOperation"
+ "_latestWorkoutSample"
+ "_lock_activityCompletion"
+ "_operation"
+ "_privacyDefaults"
+ "_protectedDataOperationForCaching"
+ "_reloadWorkoutRelevanceAndWidgetWithReason:for:"
+ "_requestCacheUpdateWorkWithError:"
+ "_setActivityCompletion:"
+ "_unitTest_notificationForExpiredEventSkipped"
+ "_unitTest_notificationForNonLocalDeviceSourceSkipped"
+ "_unitTest_notificationForUnsupportedEventSkipped"
+ "_unitTest_userNotificationCenter"
+ "_watchSamplesFrom:"
+ "associationsUpdatedForObject:subObject:type:behavior:objects:anchor:"
+ "autoupdatingCurrentCalendar"
+ "c_log_state"
+ "c_log_type"
+ "compoundPredicateWithPredicate:otherPredicate:"
+ "deprecateIRN1"
+ "didRequestHRWidgetReloadHandler"
+ "didRequestWorkoutWidgetReloadHandler"
+ "end_date"
+ "featureAvailabilityExtensionDidUpdatePairedDeviceCapability:"
+ "heart_c_log"
+ "initWithAlarmFiredDate:xpcActivityFiredDate:protectedDataOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:"
+ "initWithProfile:identifier:loggingCategory:maximumDelay:retryDelay:breadcrumbManager:gatedActivityFactory:persistentStateDefaults:operation:"
+ "initWithProfile:latestWorkoutFetchOperation:"
+ "initWithProfile:privacyDefaults:heartRateDefaults:"
+ "initWithV1FeatureAvailabilityManager:v2FeatureAvailabilityManager:cacheDefaults:protectedDataOperationForCaching:"
+ "invalidateAndWait"
+ "latestWorkoutFrom:"
+ "luck_addMigrationStepsForSchemaName:migrator:"
+ "modified_date"
+ "publisher"
+ "removeObserver:name:object:"
+ "schedule_type"
+ "setDidRequestHRWidgetReloadHandler:"
+ "setDidRequestWorkoutWidgetReloadHandler:"
+ "setUnitTest_notificationForExpiredEventSkipped:"
+ "setUnitTest_notificationForNonLocalDeviceSourceSkipped:"
+ "setUnitTest_notificationForUnsupportedEventSkipped:"
+ "setUnitTest_userNotificationCenter:"
+ "start_date"
+ "starting"
+ "unitTest_notificationForExpiredEventSkipped"
+ "unitTest_notificationForNonLocalDeviceSourceSkipped"
+ "unitTest_notificationForUnsupportedEventSkipped"
+ "unitTest_userNotificationCenter"
+ "uuid"
+ "v64@0:8@\"<HKAssociatableObject>\"16@\"<HKAssociatableObject>\"24Q32Q40@\"NSArray\"48@\"NSNumber\"56"
+ "v64@0:8@16@24Q32Q40@48@56"
- "@\"<HKHRDatabaseAnalysisSchedulerDatabaseAssertionProvider>\""
- "@\"HDAssertion\"24@0:8^@16"
- "B16@?0^@8"
- "HKHRDatabaseAnalysisSchedulerDatabaseAssertionProvider"
- "HKHRDatabaseAnalysisSchedulerDatabaseAssertionProviderImpl"
- "HeartAppPlugin.AFibBurden.Rescinded"
- "SevenDayAnalysisBreadcrumbMaintenanceOperationRun"
- "T@?,C,N,V__unitTest_processTachograms"
- "Unable to take assertion"
- "WaitingForMaintenanceOperation"
- "[%{public}@:%{public}@] Unable to get accessibilityAssertion before enqueueing maintenance operation, attempting retry later: %{public}@"
- "[%{public}@:%{public}@] maintenance operation finished"
- "[%{public}@] Error retrieving setting for %{public}@: %{public}@"
- "[%{public}@] Error retrieving setting for key %{public}@: %{public}@"
- "[%{public}@] No samples found."
- "[%{public}@] _reloadWorkoutRelevanceAndWidgetWithReason reason %@"
- "_assertionProvider"
- "_observerQueue_updateCachedOnboardingVersionIfNeeded"
- "_relevanceReloadOperation"
- "_reloadWorkoutRelevanceAndWidgetWithReason:"
- "_runMaintenanceOperationForActivity:assertion:withCompletion:"
- "addAccessibilityAssertion:"
- "featureAvailabilityProvidingDidUpdatePairedDeviceCapability:"
- "future_addMigrationStepsForSchemaName:migrator:"
- "initWithAlarmFiredDate:xpcActivityFiredDate:maintenanceOperationRunDate:analysisStartedDate:tachogramsClassifiedDate:analysisEndedDate:analysisRetryLaterRequestedDate:lastAnalysisResultDate:lastAnalysisResultContext:"
- "initWithProfile:identifier:"
- "initWithProfile:identifier:loggingCategory:maximumDelay:retryDelay:breadcrumbManager:gatedActivityFactory:assertionProvider:persistentStateDefaults:"
- "initWithV1FeatureAvailabilityManager:v2FeatureAvailabilityManager:cacheDefaults:"
- "isStarting"
- "performWithTransactionContext:error:block:"
- "publisherFromStartTime:"
- "removeObserver:"
- "setCacheScope:"
- "takeAssertionWithError:"
- "userFocusComputedMode"

```
