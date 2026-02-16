## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x6a380
-  __TEXT.__auth_stubs: 0xd50
-  __TEXT.__objc_methlist: 0x500c
+6200.5.77.2.6
+  __TEXT.__text: 0x6bb64
+  __TEXT.__auth_stubs: 0xcf0
+  __TEXT.__objc_methlist: 0x50b4
   __TEXT.__const: 0x230
-  __TEXT.__gcc_except_tab: 0xd90
-  __TEXT.__cstring: 0x5378
-  __TEXT.__oslogstring: 0xc310
+  __TEXT.__gcc_except_tab: 0xd84
+  __TEXT.__cstring: 0x5432
+  __TEXT.__oslogstring: 0xc440
   __TEXT.__ustring: 0x86
-  __TEXT.__unwind_info: 0x1700
-  __TEXT.__objc_classname: 0x1b8f
-  __TEXT.__objc_methname: 0x12989
-  __TEXT.__objc_methtype: 0x397d
-  __TEXT.__objc_stubs: 0xb2e0
-  __DATA_CONST.__got: 0xe98
-  __DATA_CONST.__const: 0x1938
+  __TEXT.__unwind_info: 0x1750
+  __TEXT.__objc_classname: 0x1bb7
+  __TEXT.__objc_methname: 0x12a17
+  __TEXT.__objc_methtype: 0x3a1c
+  __TEXT.__objc_stubs: 0xb2c0
+  __DATA_CONST.__got: 0xe88
+  __DATA_CONST.__const: 0x1988
   __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x250
+  __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3588
-  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_selrefs: 0x35a0
+  __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x298
   __DATA_CONST.__objc_arraydata: 0x510
-  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__auth_got: 0x688
   __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x4620
-  __AUTH_CONST.__objc_const: 0x9cb0
+  __AUTH_CONST.__cfstring: 0x4660
+  __AUTH_CONST.__objc_const: 0x9ce8
   __AUTH_CONST.__objc_intobj: 0xde0
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x3d0
   __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x664
-  __DATA.__data: 0x1cc0
-  __DATA.__bss: 0x50
+  __DATA.__objc_ivar: 0x658
+  __DATA.__data: 0x1d80
+  __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x1590
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
+  - /System/Library/PrivateFrameworks/HealthFeatures.framework/HealthFeatures
   - /System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles
   - /System/Library/PrivateFrameworks/HeartHealth.framework/HeartHealth
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 898F8383-4095-3BD6-A5F6-148E698402A0
-  Functions: 2043
-  Symbols:   8083
-  CStrings:  4594
+  UUID: E2597A47-5F44-3B3D-A286-956D5CCAC7F0
+  Functions: 2064
+  Symbols:   8290
+  CStrings:  4609
 
Symbols:
+ -[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:activity:]
+ -[HDHRDailyHeartRateManager _queue_transaction_deleteHeartRateOfType:sourceID:cacheIndex:replacementUUID:error:]
+ -[HDHRDailyHeartRateManager _queue_transaction_deleteHeartRateOfType:sourceID:cacheIndex:replacementUUID:error:].cold.1
+ -[HDHRDailyHeartRateManager _queue_transaction_deleteHeartRateOfType:sourceID:cacheIndex:replacementUUID:error:].cold.2
+ -[HDHRHealthLiteDataCollector _queue_handleBradycardiaEventWithDateInterval:threshold:heartRateUUIDs:]
+ -[HDHRHealthLiteDataCollector _queue_handleTachycardiaEventWithDateInterval:threshold:heartRateUUIDs:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:activity:]
+ -[HDHeartDaemonExtension daemonDidReceiveRapportEvent:completion:]
+ -[HDRemoteHeartRateStreamClient .cxx_destruct]
+ -[HDRemoteHeartRateStreamClient _connection]
+ -[HDRemoteHeartRateStreamClient _lock_setupConnection]
+ -[HDRemoteHeartRateStreamClient activateConnectionIfNecessary]
+ -[HDRemoteHeartRateStreamClient connectionInterrupted]
+ -[HDRemoteHeartRateStreamClient connectionInvalidated]
+ -[HDRemoteHeartRateStreamClient dealloc]
+ -[HDRemoteHeartRateStreamClient exportedInterface]
+ -[HDRemoteHeartRateStreamClient initWithConnectionProvider:]
+ -[HDRemoteHeartRateStreamClient initWithEndPoint:]
+ -[HDRemoteHeartRateStreamClient init]
+ -[HDRemoteHeartRateStreamClient invalidateConnection]
+ -[HDRemoteHeartRateStreamClient isConnectionActive]
+ -[HDRemoteHeartRateStreamClient prepareToProvideHeartRateWithCompletion:]
+ -[HDRemoteHeartRateStreamClient remoteInterface]
+ _HDDataEntityPredicateForSourceIdentifier
+ _HKHRAFibBurdenNotificationsDisabledNotificationShownDateKey
+ _OBJC_CLASS_$_HDHeartEventSensorDatum
+ _OBJC_CLASS_$_HDRemoteHeartRateStreamClient
+ _OBJC_CLASS_$_HKDaemonTransaction
+ _OBJC_CLASS_$_HKHRBloodPressureJournalNotificationIdentifier
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$__HKXPCConnection
+ _OBJC_IVAR_$_HDHRDailyHeartRateManager._queue_restingHeartRateByActivityCacheIndex
+ _OBJC_IVAR_$_HDHRDailyHeartRateManager._queue_walkingAverageHeartRateByActivityCacheIndex
+ _OBJC_IVAR_$_HDRemoteHeartRateStreamClient._connectionProvider
+ _OBJC_IVAR_$_HDRemoteHeartRateStreamClient._connectionToService
+ _OBJC_IVAR_$_HDRemoteHeartRateStreamClient._lock
+ _OBJC_IVAR_$_HDRemoteHeartRateStreamClient._running
+ _OBJC_METACLASS_$_HDRemoteHeartRateStreamClient
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_INSTANCE_METHODS_HDRemoteHeartRateStreamClient
+ __OBJC_$_INSTANCE_VARIABLES_HDRemoteHeartRateStreamClient
+ __OBJC_$_PROP_LIST_HDRemoteHeartRateStreamClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKRemoteHeartRateStreamServiceInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__HKXPCExportable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__HKXPCExportable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKRemoteHeartRateStreamServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES__HKXPCExportable
+ __OBJC_$_PROTOCOL_REFS_HKRemoteHeartRateStreamServiceInterface
+ __OBJC_$_PROTOCOL_REFS__HKXPCExportable
+ __OBJC_CLASS_PROTOCOLS_$_HDRemoteHeartRateStreamClient
+ __OBJC_CLASS_RO_$_HDRemoteHeartRateStreamClient
+ __OBJC_LABEL_PROTOCOL_$_HKRemoteHeartRateStreamServiceInterface
+ __OBJC_LABEL_PROTOCOL_$__HKXPCExportable
+ __OBJC_METACLASS_RO_$_HDRemoteHeartRateStreamClient
+ __OBJC_PROTOCOL_$_HKRemoteHeartRateStreamServiceInterface
+ __OBJC_PROTOCOL_$__HKXPCExportable
+ __OBJC_PROTOCOL_REFERENCE_$_HKRemoteHeartRateStreamServiceInterface
+ ___103-[HDHRHeartRateNotificationsFeatureAvailabilityManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.406
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.368
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.368.cold.1
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.369
+ ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.369.cold.1
+ ___104-[HKHRAFibBurdenJulianDayMajorityTimeZoneDeterminer determineJulianDayToMajorityTimeZoneForRange:error:]_block_invoke.370
+ ___104-[HRAtrialFibrillationEventDetector _queue_analyzeCurrentConfirmationCycleSamples:withAlgorithmVersion:]_block_invoke.391
+ ___105-[HDHRBloodPressureJournalManager insertBloodPressureJournals:isUserInitiated:error:onCommit:onRollback:]_block_invoke.394
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.373
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.373.cold.1
+ ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.374
+ ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke.420
+ ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke.420.cold.1
+ ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke.420.cold.2
+ ___109-[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:activity:]_block_invoke
+ ___109-[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:activity:]_block_invoke.354
+ ___109-[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:activity:]_block_invoke_2
+ ___109-[HDHRDailyHeartRateManager _queue_replaceHeartRate:ofType:forCacheIndex:dateInterval:heartRateByCacheIndex:]_block_invoke
+ ___109-[HDHRDailyHeartRateManager _queue_replaceHeartRate:ofType:forCacheIndex:dateInterval:heartRateByCacheIndex:]_block_invoke.cold.1
+ ___114-[HDHRHypertensionNotificationsAnalysisScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:activity:]_block_invoke
+ ___114-[HDHRHypertensionNotificationsAnalysisScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:activity:]_block_invoke.367
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke.375
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke_2.376
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke_3.378
+ ___160-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.358
+ ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.410
+ ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.410.cold.1
+ ___35-[HDHRNotificationAnalytics submit]_block_invoke.361
+ ___35-[HDHRNotificationAnalytics submit]_block_invoke.361.cold.1
+ ___35-[HDHRNotificationAnalytics submit]_block_invoke.361.cold.2
+ ___37-[HDRemoteHeartRateStreamClient init]_block_invoke
+ ___50-[HDRemoteHeartRateStreamClient initWithEndPoint:]_block_invoke
+ ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.371
+ ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.371.cold.1
+ ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.378
+ ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.378.cold.1
+ ___73-[HDHRIrregularRhythmNotificationsV2UpgradeManager doWorkWithCompletion:]_block_invoke.375
+ ___73-[HDHRIrregularRhythmNotificationsV2UpgradeManager doWorkWithCompletion:]_block_invoke.375.cold.1
+ ___73-[HDRemoteHeartRateStreamClient prepareToProvideHeartRateWithCompletion:]_block_invoke
+ ___74-[HRAtrialFibrillationEventDetector _queue_seriesSamplesAdded:lastAnchor:]_block_invoke.379
+ ___75-[HDHRHealthKitSyncManager triggerImmediateSyncWithReason:loggingCategory:]_block_invoke.349
+ ___76-[HRAtrialFibrillationEventDetector _queue_analyzeTachogramsSinceLastAnchor]_block_invoke.376
+ ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.359
+ ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.360
+ ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.363
+ ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.451
+ ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.451.cold.1
+ ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.348
+ ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.348.cold.1
+ ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.344
+ ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.344.cold.1
+ ___97-[HDHRHypertensionNotificationsRescindedAlertManager _presentNotificationWithTitle:message:type:]_block_invoke.393
+ ___97-[HDHRHypertensionNotificationsRescindedAlertManager _presentNotificationWithTitle:message:type:]_block_invoke.393.cold.1
+ ___block_descriptor_32_e23_"_HKXPCConnection"8?0l
+ ___block_descriptor_40_e8_32s_e23_"_HKXPCConnection"8?0ls32l8
+ ___block_descriptor_64_e8_32s40s48bs56bs_e20_v24?0q8"NSError"16ls32l8s48l8s56l8s40l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_literal_global.343
+ ___block_literal_global.371
+ ___block_literal_global.375
+ ___block_literal_global.377
+ ___block_literal_global.381
+ ___block_literal_global.385
+ ___block_literal_global.394
+ ___block_literal_global.405
+ ___block_literal_global.407
+ ___block_literal_global.411
+ ___block_literal_global.412
+ ___block_literal_global.413
+ ___block_literal_global.415
+ ___block_literal_global.455
+ _objc_msgSend$_connection
+ _objc_msgSend$_enqueueSchedulingOnMaintenanceOperationWithCompletion:activity:
+ _objc_msgSend$_lock_setupConnection
+ _objc_msgSend$_queue_transaction_deleteHeartRateOfType:sourceID:cacheIndex:replacementUUID:error:
+ _objc_msgSend$activateConnectionIfNecessary
+ _objc_msgSend$dataCollector:didCollectSensorData:device:options:
+ _objc_msgSend$enqueueMaintenanceOperation:withPeriodicActivity:
+ _objc_msgSend$initWithConnectionProvider:
+ _objc_msgSend$initWithIdentifier:dateInterval:heartRateThreshold:associatedSampleUUIDs:resumeContext:
+ _objc_msgSend$initWithListenerEndpoint:
+ _objc_msgSend$initWithServiceName:
+ _objc_msgSend$interfaceWithProtocol:
+ _objc_msgSend$invalidateConnection
+ _objc_msgSend$remote_prepareToProvideHeartRateWithCompletion:
+ _objc_msgSend$resume
+ _objc_msgSend$setExportedObject:
+ _objc_msgSend$sourceID
+ _objc_msgSend$transactionWithOwner:activityName:
+ _objc_release_x2
- +[HDHRBloodPressureJournalNotificationIdentifier identifierFromBPSample:journal:]
- -[HDHRBloodPressureJournalNotificationIdentifier .cxx_destruct]
- -[HDHRBloodPressureJournalNotificationIdentifier identifierString]
- -[HDHRBloodPressureJournalNotificationIdentifier initWithIdentifierString:]
- -[HDHRBloodPressureJournalNotificationIdentifier initWithJournalIdentifier:notificationDayIndex:journalWindowType:]
- -[HDHRBloodPressureJournalNotificationIdentifier journalIdentifier]
- -[HDHRBloodPressureJournalNotificationIdentifier journalWindowType]
- -[HDHRBloodPressureJournalNotificationIdentifier notificationDayIndex]
- -[HDHRDailyHeartRateManager _queue_deleteHeartRateOfType:forCacheIndex:replacementUUID:]
- -[HDHRDailyHeartRateManager _queue_deleteHeartRateOfType:forCacheIndex:replacementUUID:].cold.1
- -[HDHRDailyHeartRateManager _queue_deleteHeartRateOfType:forCacheIndex:replacementUUID:].cold.2
- -[HDHRDailyHeartRateManager _queue_replaceHeartRate:ofType:forCacheIndex:dateInterval:heartRateByCacheIndex:].cold.1
- -[HDHRHealthLiteDataCollector _assertionManagerStateChanged:]
- -[HDHRHealthLiteDataCollector _assertionManagerStateChanged:].cold.1
- -[HDHRHealthLiteDataCollector _queue_hasHeartRateClientsWithoutWorkouts]
- -[HDHRHealthLiteDataCollector _queue_shouldStreamReducedRateHeartRateUpdates]
- -[HDHRHealthLiteDataCollector _queue_updateHeartRateCollectionType]
- -[HDHRHealthLiteDataCollector _startObservingAssertionManagerChanges]
- -[HDHRHealthLiteDataCollector _startObservingCurrentWorkoutChanges]
- -[HDHRHealthLiteDataCollector _workoutManagerStateDidChange]
- -[HDHRHypertensionNotificationsAnalysisScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]
- _HDAssertionManagerAssertionKey
- _HDAssertionManagerAssertionReturnedNotification
- _HDAssertionManagerAssertionTakenNotification
- _HDCurrentWorkoutSessionAssertion
- _HDHRAFibBurdenNotificationsDisabledNotificationShownDateKey
- _HDQueryServerSampleTypeObservationAssertionName
- _HDWorkoutManagerStateDidChange
- _HKLogHeartRhythmCategory
- _HKStringFromBool
- _OBJC_CLASS_$_HDHRBloodPressureJournalNotificationIdentifier
- _OBJC_CLASS_$_HKHRLearnHypertensionJournalEntryProvider
- _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationIdentifier._identifierString
- _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationIdentifier._journalIdentifier
- _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationIdentifier._journalWindowType
- _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationIdentifier._notificationDayIndex
- _OBJC_IVAR_$_HDHRDailyHeartRateManager._restingHeartRateByActivityCacheIndex
- _OBJC_IVAR_$_HDHRDailyHeartRateManager._walkingAverageHeartRateByActivityCacheIndex
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._heartRateAggregator
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._heartRateCollectionConfiguration
- _OBJC_IVAR_$_HDHRHealthLiteDataCollector._heartRateCollectionState
- _OBJC_METACLASS_$_HDHRBloodPressureJournalNotificationIdentifier
- __LocalWatchDeviceSupportsCountryCode
- __OBJC_$_CLASS_METHODS_HDHRBloodPressureJournalNotificationIdentifier
- __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalNotificationIdentifier
- __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalNotificationIdentifier
- __OBJC_$_PROP_LIST_HDHRBloodPressureJournalNotificationIdentifier
- __OBJC_CLASS_RO_$_HDHRBloodPressureJournalNotificationIdentifier
- __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalNotificationIdentifier
- ___100-[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke
- ___100-[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke.315
- ___100-[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke_2
- ___103-[HDHRHeartRateNotificationsFeatureAvailabilityManager observeValueForKeyPath:ofObject:change:context:]_block_invoke.367
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.329
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.329.cold.1
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.330
- ___104-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setFeatureSettingNumber:forKey:completion:]_block_invoke.330.cold.1
- ___104-[HKHRAFibBurdenJulianDayMajorityTimeZoneDeterminer determineJulianDayToMajorityTimeZoneForRange:error:]_block_invoke.331
- ___104-[HRAtrialFibrillationEventDetector _queue_analyzeCurrentConfirmationCycleSamples:withAlgorithmVersion:]_block_invoke.352
- ___105-[HDHRBloodPressureJournalManager insertBloodPressureJournals:isUserInitiated:error:onCommit:onRollback:]_block_invoke.355
- ___105-[HDHRHypertensionNotificationsAnalysisScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke
- ___105-[HDHRHypertensionNotificationsAnalysisScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke.328
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.334
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.334.cold.1
- ___105-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager removeFeatureSettingValueForKey:completion:]_block_invoke.335
- ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke.381
- ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke.381.cold.1
- ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke.381.cold.2
- ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke.336
- ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke_2.337
- ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke_3.339
- ___160-[HDHRIrregularRhythmNotificationsFeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.319
- ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.371
- ___162-[HDHRIrregularRhythmNotificationsV1FeatureAvailabilityManager setCurrentOnboardingVersionCompletedForCountryCode:countryCodeProvenance:date:settings:completion:]_block_invoke.371.cold.1
- ___35-[HDHRNotificationAnalytics submit]_block_invoke.322
- ___35-[HDHRNotificationAnalytics submit]_block_invoke.322.cold.1
- ___35-[HDHRNotificationAnalytics submit]_block_invoke.322.cold.2
- ___60-[HDHRHealthLiteDataCollector _workoutManagerStateDidChange]_block_invoke
- ___61-[HDHRHealthLiteDataCollector _assertionManagerStateChanged:]_block_invoke
- ___61-[HDHRHealthLiteDataCollector _assertionManagerStateChanged:]_block_invoke.359
- ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.335
- ___71-[HDHRAFibBurdenRescindedNotificationManager _sendNotificationRequest:]_block_invoke.335.cold.1
- ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.339
- ___73-[HDHRAFibBurdenNotificationManager _sendNotificationRequest:completion:]_block_invoke.339.cold.1
- ___73-[HDHRIrregularRhythmNotificationsV2UpgradeManager doWorkWithCompletion:]_block_invoke.336
- ___73-[HDHRIrregularRhythmNotificationsV2UpgradeManager doWorkWithCompletion:]_block_invoke.336.cold.1
- ___74-[HRAtrialFibrillationEventDetector _queue_seriesSamplesAdded:lastAnchor:]_block_invoke.340
- ___75-[HDHRHealthKitSyncManager triggerImmediateSyncWithReason:loggingCategory:]_block_invoke.310
- ___76-[HRAtrialFibrillationEventDetector _queue_analyzeTachogramsSinceLastAnchor]_block_invoke.337
- ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.320
- ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.321
- ___83-[HDHRCardioFitnessAnalyticsDailyEventActivity performPeriodicActivity:completion:]_block_invoke.324
- ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.412
- ___87-[HDHRAFibBurdenDailyAnalyticsEvent _extractWatchWearPropertiesIntoPayload:dataSource:]_block_invoke.412.cold.1
- ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.309
- ___93-[HDHRCardioFitnessFeatureStatusManagerServer remote_setNotificationsEnabled:withCompletion:]_block_invoke.309.cold.1
- ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.305
- ___95-[HDHRIrregularRhythmNotificationsSettingMigrator _syncSettingIfPossibleFromManager:toManager:]_block_invoke.305.cold.1
- ___97-[HDHRHypertensionNotificationsRescindedAlertManager _presentNotificationWithTitle:message:type:]_block_invoke.354
- ___97-[HDHRHypertensionNotificationsRescindedAlertManager _presentNotificationWithTitle:message:type:]_block_invoke.354.cold.1
- ___block_descriptor_56_e8_32s40bs48bs_e20_v24?0q8"NSError"16ls32l8s40l8s48l8
- ___block_literal_global.304
- ___block_literal_global.332
- ___block_literal_global.336
- ___block_literal_global.338
- ___block_literal_global.342
- ___block_literal_global.346
- ___block_literal_global.355
- ___block_literal_global.366
- ___block_literal_global.368
- ___block_literal_global.372
- ___block_literal_global.373
- ___block_literal_global.374
- ___block_literal_global.376
- ___block_literal_global.416
- __assertionManagerStateChanged:.onceToken
- __assertionManagerStateChanged:.relevantAssertionIdentifiers
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$HRCoordinator
- _objc_msgSend$_queue_deleteHeartRateOfType:forCacheIndex:replacementUUID:
- _objc_msgSend$_queue_hasHeartRateClientsWithoutWorkouts
- _objc_msgSend$_queue_updateHeartRateCollectionType
- _objc_msgSend$_startObservingAssertionManagerChanges
- _objc_msgSend$_startObservingCurrentWorkoutChanges
- _objc_msgSend$currentActivityRequiresExtendedMode
- _objc_msgSend$dayIndex
- _objc_msgSend$heartRatePush
- _objc_msgSend$initWithJournal:
- _objc_msgSend$isInHeartRateRecovery
- _objc_msgSend$journalEntryForSample:
- _objc_msgSend$minusSet:
- _objc_msgSend$mutableCopy
- _objc_msgSend$negatedPredicate:
- _objc_msgSend$ownerIdentifiersForAssertionIdentifier:
- _objc_msgSend$removeObserver:name:object:
- _objc_msgSend$sessionAssertionManager
- _objc_msgSend$workoutManager
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x6
- _objc_retain_x7
- _objc_retain_x9
CStrings:
+ "\nHeart enabled in privacy: %@\nTachycardia Collection: %@\nBradycardia Collection: %@"
+ "%s"
+ "%{public}@ persisting bradycardia event with date interval %{public}@"
+ "%{public}@ persisting tachycardia event with date interval %{public}@"
+ "-[HKHRDatabaseAnalysisSchedulerImpl performWorkForOperation:profile:databaseAccessibilityAssertion:completion:]"
+ "16625FBA-332F-481C-B7DE-7E80973B07BF"
+ "2B5E630F-332F-481C-B7DE-7E80973B07BF"
+ "38627122-332F-481C-B7DE-7E80973B07BF"
+ "46D9FF45-332F-481C-B7DE-7E80973B07BF"
+ "68AB2987-332F-481C-B7DE-7E80973B07BF"
+ "7640DD53-332F-481C-B7DE-7E80973B07BF"
+ "@\"NSXPCInterface\"16@0:8"
+ "@\"_HKXPCConnection\""
+ "@\"_HKXPCConnection\"8@?0"
+ "A0A8CBBD-332F-481C-B7DE-7E80973B07BF"
+ "B32@0:8@\"NSString\"16@?<v@?>24"
+ "B32@0:8@16@?24"
+ "B56@0:8@16@24q32@40^@48"
+ "BADB0622-332F-481C-B7DE-7E80973B07BF"
+ "E17D2903-332F-481C-B7DE-7E80973B07BF"
+ "HDRemoteHeartRateStreamClient"
+ "HKRemoteHeartRateStreamServiceInterface"
+ "Unable to retrieve local data provenance"
+ "Unable to retrieve local data provenance source"
+ "[%@] Reporting result %@ to %@"
+ "[%{public}@] Connection Interrupted : %{public}@"
+ "[%{public}@] Connection Invalidated : %{public}@"
+ "[%{public}@] No need to activate. Connection already activated %@"
+ "[%{public}@] Successfully posted hypertension notification"
+ "[%{public}@] Transaction to replace HR (%{public}@) failed %{public}@"
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForLearnHypertensionRiskJournal: Creating notification info with wakeupAlarmCount: %lu and bedtimeAlarmCount: %lu"
+ "[%{public}@] daemonDidReceiveRapportEvent."
+ "[Daily HR] ignoring activity cache (%{public}@) with no date interval for %{public}@"
+ "_HKXPCExportable"
+ "_connection"
+ "_connectionProvider"
+ "_connectionToService"
+ "_enqueueSchedulingOnMaintenanceOperationWithCompletion:activity:"
+ "_lock_setupConnection"
+ "_queue_handleBradycardiaEventWithDateInterval:threshold:heartRateUUIDs:"
+ "_queue_handleTachycardiaEventWithDateInterval:threshold:heartRateUUIDs:"
+ "_queue_restingHeartRateByActivityCacheIndex"
+ "_queue_transaction_deleteHeartRateOfType:sourceID:cacheIndex:replacementUUID:error:"
+ "_queue_walkingAverageHeartRateByActivityCacheIndex"
+ "_running"
+ "activateConnectionIfNecessary"
+ "com.apple.health.RemoteHeartRateStreamService"
+ "connectionConfigured"
+ "connectionInterrupted"
+ "daemonDidReceiveRapportEvent:completion:"
+ "dataCollector:didCollectSensorData:device:options:"
+ "enqueueMaintenanceOperation:withPeriodicActivity:"
+ "initWithConnectionProvider:"
+ "initWithEndPoint:"
+ "initWithIdentifier:dateInterval:heartRateThreshold:associatedSampleUUIDs:resumeContext:"
+ "initWithListenerEndpoint:"
+ "initWithServiceName:"
+ "interfaceWithProtocol:"
+ "invalidateConnection"
+ "isConnectionActive"
+ "prepareToProvideHeartRateWithCompletion:"
+ "remote_prepareToProvideHeartRateWithCompletion:"
+ "resume"
+ "samplesMapWereRemoved:anchor:"
+ "setExportedObject:"
+ "sourceID"
+ "transactionWithOwner:activityName:"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v32@0:8@\"<HDActivityCacheManagerInterface>\"16@\"HKActivityCache\"24"
+ "v32@0:8@\"NSDictionary\"16@\"NSNumber\"24"
+ "v32@0:8@?16@24"
+ "v36@0:8@\"<HDActivityCacheManagerInterface>\"16@\"HKHeartRateSummary\"24B32"
- "\nHeart enabled in privacy: %@\nHeart Rate Collection: %@\nTachycardia Collection: %@\nBradycardia Collection: %@"
- "%{public}@: Heart rate collection transitioning from %{public}@ to %{public}@"
- "%{public}@: Updating heart rate collection type because assertion changed: %{public}@"
- "16625FBA-E847-4494-8191-433915DC9F15"
- "2B5E630F-55DE-4122-A36B-5F8F77D1363E"
- "38627122-E97A-4089-861C-81704B480D2E"
- "46D9FF45-6717-4357-9B04-2E06E1095260"
- "68AB2987-CE75-463C-9EAF-9861B292F01E"
- "7640DD53-A02B-4C03-AB93-9FA49BCD0AB6"
- "@\"HDHeartRateDataAggregator\""
- "@\"NSUUID\""
- "@40@0:8@16q24q32"
- "A0A8CBBD-8F56-46ED-A36B-446D452C0515"
- "BADB0622-1CC0-4CE0-BF07-1B79D4FC28BB"
- "E17D2903-B868-4E6C-8E76-6D4939BEED44"
- "HDHRAFibBurdenNotificationsDisabledNotificationShownDateKey"
- "HDHRBloodPressureJournalNotificationIdentifier"
- "HRCoordinator"
- "T@\"NSUUID\",R,N,V_journalIdentifier"
- "Tq,R,N,V_journalWindowType"
- "Tq,R,N,V_notificationDayIndex"
- "Workout power saving mode is active, full-fidelity streaming allowed: %@, heart rate clients: %@, workout clients: %@"
- "[%{public}@] Invalid Journal type. Could not make identifier for Sample [%{public}@] and journal [%{public}@]."
- "[%{public}@] Sucessfully posted hypertension notification"
- "_"
- "_assertionManagerStateChanged:"
- "_heartRateAggregator"
- "_heartRateCollectionConfiguration"
- "_heartRateCollectionState"
- "_identifierString"
- "_journalIdentifier"
- "_journalWindowType"
- "_notificationDayIndex"
- "_queue_deleteHeartRateOfType:forCacheIndex:replacementUUID:"
- "_queue_hasHeartRateClientsWithoutWorkouts"
- "_queue_shouldStreamReducedRateHeartRateUpdates"
- "_queue_updateHeartRateCollectionType"
- "_restingHeartRateByActivityCacheIndex"
- "_startObservingAssertionManagerChanges"
- "_startObservingCurrentWorkoutChanges"
- "_walkingAverageHeartRateByActivityCacheIndex"
- "_workoutManagerStateDidChange"
- "currentActivityRequiresExtendedMode"
- "dayIndex"
- "heartRatePush"
- "initWithJournal:"
- "isInHeartRateRecovery"
- "journalEntryForSample:"
- "journalWindowType"
- "minusSet:"
- "mutableCopy"
- "negatedPredicate:"
- "notificationDayIndex"
- "ownerIdentifiersForAssertionIdentifier:"
- "removeObserver:name:object:"
- "sessionAssertionManager"
- "v32@0:8@\"HDActivityCacheManager\"16@\"HKActivityCache\"24"
- "v36@0:8@\"HDActivityCacheManager\"16@\"HKHeartRateSummary\"24B32"
- "workoutManager"

```
