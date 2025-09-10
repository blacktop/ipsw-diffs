## HeartHealthDaemon

> `/System/Library/PrivateFrameworks/HeartHealthDaemon.framework/HeartHealthDaemon`

```diff

 6106.1.2.11.0
-  __TEXT.__text: 0x4bcac
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x3c54
-  __TEXT.__const: 0x1e0
-  __TEXT.__gcc_except_tab: 0xa68
-  __TEXT.__cstring: 0x3b01
-  __TEXT.__oslogstring: 0x877c
+  __TEXT.__text: 0x6a380
+  __TEXT.__auth_stubs: 0xd50
+  __TEXT.__objc_methlist: 0x500c
+  __TEXT.__const: 0x230
+  __TEXT.__gcc_except_tab: 0xd90
+  __TEXT.__cstring: 0x5378
+  __TEXT.__oslogstring: 0xc310
   __TEXT.__ustring: 0x86
-  __TEXT.__unwind_info: 0x1140
-  __TEXT.__objc_classname: 0x166e
-  __TEXT.__objc_methname: 0xdaea
-  __TEXT.__objc_methtype: 0x2fab
-  __TEXT.__objc_stubs: 0x8580
-  __DATA_CONST.__got: 0xbc0
-  __DATA_CONST.__const: 0x1278
-  __DATA_CONST.__objc_classlist: 0x250
-  __DATA_CONST.__objc_catlist: 0x60
-  __DATA_CONST.__objc_protolist: 0x210
+  __TEXT.__unwind_info: 0x1700
+  __TEXT.__objc_classname: 0x1b8f
+  __TEXT.__objc_methname: 0x12989
+  __TEXT.__objc_methtype: 0x397d
+  __TEXT.__objc_stubs: 0xb2e0
+  __DATA_CONST.__got: 0xe98
+  __DATA_CONST.__const: 0x1938
+  __DATA_CONST.__objc_classlist: 0x308
+  __DATA_CONST.__objc_catlist: 0x80
+  __DATA_CONST.__objc_protolist: 0x250
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2878
-  __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1f0
-  __DATA_CONST.__objc_arraydata: 0x4b0
-  __AUTH_CONST.__auth_got: 0x620
-  __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0x3240
-  __AUTH_CONST.__objc_const: 0x74c8
-  __AUTH_CONST.__objc_intobj: 0xc90
+  __DATA_CONST.__objc_selrefs: 0x3588
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x298
+  __DATA_CONST.__objc_arraydata: 0x510
+  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x4620
+  __AUTH_CONST.__objc_const: 0x9cb0
+  __AUTH_CONST.__objc_intobj: 0xd68
+  __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__objc_doubleobj: 0x3d0
-  __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x490
-  __DATA.__data: 0x18d0
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x664
+  __DATA.__data: 0x1cc0
   __DATA.__bss: 0x50
-  __DATA_DIRTY.__objc_data: 0x1040
+  __DATA_DIRTY.__objc_data: 0x1590
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
+  - /System/Library/PrivateFrameworks/HealthAlgorithms.framework/HealthAlgorithms
   - /System/Library/PrivateFrameworks/HealthDaemon.framework/HealthDaemon
   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/HealthMenstrualCycles.framework/HealthMenstrualCycles

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: CD5B9B22-505D-361B-999F-1B02523DF476
-  Functions: 1505
-  Symbols:   6108
-  CStrings:  3444
+  UUID: 7E76D803-8BCC-3654-BD95-C992AF10C6C2
+  Functions: 2043
+  Symbols:   8083
+  CStrings:  4594
 
Symbols:
+ +[HDFeatureAvailabilityManager(BPJ) bloodPressureJournalFeatureAvailabilityManagerWithProfile:]
+ +[HDHRBloodPressureJournalControlServer configurationClass]
+ +[HDHRBloodPressureJournalControlServer createTaskServerWithUUID:configuration:client:delegate:error:]
+ +[HDHRBloodPressureJournalControlServer taskIdentifier]
+ +[HDHRBloodPressureJournalControlServer validateConfiguration:client:error:]
+ +[HDHRBloodPressureJournalNotificationIdentifier identifierFromBPSample:journal:]
+ +[HDHRBloodPressureJournalNotificationManager _stringFromNotificationReason:]
+ +[HDHRHeartCLogEntity _enumerateJournalsWithPredicate:limit:orderingTerms:transaction:error:enumerationHandler:]
+ +[HDHRHeartCLogEntity _insertJournal:transaction:error:]
+ +[HDHRHeartCLogEntity _insertTimeIntervals:journalPrimaryKey:transaction:error:]
+ +[HDHRHeartCLogEntity _journalEntityProperties]
+ +[HDHRHeartCLogEntity _journalFromRow:persistentID:transaction:error:]
+ +[HDHRHeartCLogEntity enumerateJournalsWithPredicate:limit:orderingTerms:transaction:error:enumerationHandler:]
+ +[HDHRHeartCLogEntity insertBloodPressureJournal:profile:transaction:error:]
+ +[HDHRHeartCLogScheduleTimeIntervalEntity _journalScheduleIntervalFromRow:]
+ +[HDHRHeartCLogScheduleTimeIntervalEntity _journalScheduleTimeIntervalEntityProperties]
+ +[HDHRHeartCLogScheduleTimeIntervalEntity enumerateJournalScheduleIntervalWithOwnerID:transaction:error:enumerationHandler:]
+ +[HDHRHeartCLogScheduleTimeIntervalEntity insertJournalScheduleInterval:ownerID:database:error:]
+ +[HDKeyValueDomain(HypertensionNotifications) hdhr_hypertensionNotificationsDeviceLocalDomainForProfile:]
+ +[HDKeyValueDomain(HypertensionNotifications) hdhr_hypertensionNotificationsSyncedDomainForProfile:]
+ +[HKCountrySet(BloodPressureJournal) localAvailabilityForBloodPressureJournal]
+ +[HKCountrySet(BloodPressureJournal) localAvailabilityForBloodPressureJournal].cold.1
+ +[HKCountrySet(HypertensionNotifications) localAvailabilityForHypertensionNotifications]
+ +[HKCountrySet(HypertensionNotifications) localAvailabilityForHypertensionNotifications].cold.1
+ +[HKFeatureAvailabilityRequirementSet(BPJ) bloodPressureJournalFeatureAvailabilityRequirementSet]
+ +[HKHRBloodPressureJournalStateSyncEntity _sevenDaysTimeWindow]
+ +[HKHRBloodPressureJournalStateSyncEntity _stringFromSyncResult:]
+ +[HKHRBloodPressureJournalStateSyncEntity _windowUpdaterConfigurationForBloodPressureSamplesWithKey:sampleOriginKey:sampleType:syncEntityClass:sampleUUIDSFunction:]
+ +[HKHRBloodPressureJournalStateSyncEntity bloodPressureJournalFromCodableJournal:]
+ +[HKHRBloodPressureJournalStateSyncEntity codableJournalFromBloodPressureJournal:]
+ +[HKHRBloodPressureJournalStateSyncEntity stateEntitySchema]
+ +[HKHRBloodPressureJournalStateSyncEntity syncDidFinishWithResult:stateStore:profile:]
+ +[HKHRBloodPressureJournalStateSyncEntity updateDataWithStateStorage:profile:transaction:error:]
+ +[HKHRStateSyncBloodPressureJournalDelegate _fetchCloudState:codableSyncState:profile:error:]
+ +[HKHRStateSyncBloodPressureJournalDelegate _fetchLocalJournals:profile:transaction:error:]
+ +[HKHRStateSyncBloodPressureJournalDelegate _persistCloudState:profile:error:]
+ +[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]
+ +[HKHRStateSyncBloodPressureJournalDelegate _updateCodableSyncState:withMergeState:profile:error:]
+ +[HKHRStateSyncBloodPressureJournalDelegate supportedSyncVersionRange]
+ +[HKNotificationInstruction(BloodPressureJournal) categoryIdentifierFromAlarmEventIdentifier:]
+ +[HKNotificationInstruction(BloodPressureJournal) categoryIdentifierFromJournalIdentifier:]
+ +[HKNotificationInstruction(BloodPressureJournal) notificationIdentifierFromCategoryIdentifier:]
+ +[HKNotificationInstruction(BloodPressureJournal) notificationIdentifiersFromCategoryIdentifiers:]
+ -[HDAlarmEvent(BloodPressureJournal) boolValueFromKeyValuePair:]
+ -[HDAlarmEvent(BloodPressureJournal) integerValueFromKeyValuePair:]
+ -[HDAlarmEvent(BloodPressureJournal) isFollowUp]
+ -[HDAlarmEvent(BloodPressureJournal) isFollowUp].cold.1
+ -[HDAlarmEvent(BloodPressureJournal) journalIdentifierString]
+ -[HDAlarmEvent(BloodPressureJournal) journalIdentifierString].cold.1
+ -[HDAlarmEvent(BloodPressureJournal) journalType]
+ -[HDAlarmEvent(BloodPressureJournal) journalType].cold.1
+ -[HDAlarmEvent(BloodPressureJournal) measurementInfo]
+ -[HDAlarmEvent(BloodPressureJournal) notificationIdentifierString]
+ -[HDAlarmEvent(BloodPressureJournal) notificationIdentifierString].cold.1
+ -[HDAlarmEvent(BloodPressureJournal) valueFromKeyValuePair:]
+ -[HDAlarmEvent(BloodPressureJournal) valueFromKeyValuePair:].cold.1
+ -[HDHRBloodPressureDailyAnalyticsEvent .cxx_destruct]
+ -[HDHRBloodPressureDailyAnalyticsEvent _IHAGatedDemographicsFieldsWithDataSource:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _bucketedWeeksSinceDate:dataSource:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _calculateJournalEntryAnalytics:dataSource:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _calculateJournalStateAnalytics:dataSource:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _calculateMostRecentBPJCycleAnalytics:dataSource:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _featureStatusForFeatureIdentifier:dataSource:error:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _fetchBloodPressureJournals]
+ -[HDHRBloodPressureDailyAnalyticsEvent _fetchBloodPressureJournals].cold.1
+ -[HDHRBloodPressureDailyAnalyticsEvent _fetchBloodPressureSamplesWithPredicate:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _fetchBloodPressureSamplesWithPredicate:].cold.1
+ -[HDHRBloodPressureDailyAnalyticsEvent _fetchMostRecentBPJCycleWithBloodPressureJournals:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _fetchMostRecentBPJCycleWithBloodPressureJournals:].cold.1
+ -[HDHRBloodPressureDailyAnalyticsEvent _hasUserEverSetUpBPJ:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _isFeatureEnabledForFeatureIdentifier:dataSource:featureAvailabilityContext:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _isPregnancyModeEnabled]
+ -[HDHRBloodPressureDailyAnalyticsEvent _numDaysSinceLastLoggedinBPJWithDataSource:]
+ -[HDHRBloodPressureDailyAnalyticsEvent _observePregnancy]
+ -[HDHRBloodPressureDailyAnalyticsEvent _weeksSinceOnboardingWithDataSource:]
+ -[HDHRBloodPressureDailyAnalyticsEvent eventName]
+ -[HDHRBloodPressureDailyAnalyticsEvent initWithProfile:]
+ -[HDHRBloodPressureDailyAnalyticsEvent isEventSubmissionIHAGated]
+ -[HDHRBloodPressureDailyAnalyticsEvent makeIHAGatedEventPayloadWithDataSource:error:]
+ -[HDHRBloodPressureDailyAnalyticsEvent makeUnrestrictedEventPayloadWithDataSource:error:]
+ -[HDHRBloodPressureDailyAnalyticsEvent numberOfDaysBetweenStartDate:endDate:withCalendar:]
+ -[HDHRBloodPressureDailyAnalyticsEvent pregnancyModelDidUpdate:]
+ -[HDHRBloodPressureJournalBPSampleObserver .cxx_destruct]
+ -[HDHRBloodPressureJournalBPSampleObserver _currentActiveJournal]
+ -[HDHRBloodPressureJournalBPSampleObserver _currentActiveJournal].cold.1
+ -[HDHRBloodPressureJournalBPSampleObserver _regenerateNotificationsIfNecessaryWithJournalSamples:]
+ -[HDHRBloodPressureJournalBPSampleObserver _regenerateNotificationsIfNecessaryWithJournalSamples:].cold.1
+ -[HDHRBloodPressureJournalBPSampleObserver _removeDeliveredNotificationsFromNotificationCenterForSamples:journal:]
+ -[HDHRBloodPressureJournalBPSampleObserver _samplesFromCurrentDeviceIn:]
+ -[HDHRBloodPressureJournalBPSampleObserver _samplesInCurrentActiveJournalPeriodFor:from:]
+ -[HDHRBloodPressureJournalBPSampleObserver _samplesInCurrentActiveJournalPeriodFor:from:].cold.1
+ -[HDHRBloodPressureJournalBPSampleObserver didRegenerateNotificationsHandler]
+ -[HDHRBloodPressureJournalBPSampleObserver didRequestNotificationsRemovalHandler]
+ -[HDHRBloodPressureJournalBPSampleObserver didTriggerSyncHandler]
+ -[HDHRBloodPressureJournalBPSampleObserver initWithProfile:]
+ -[HDHRBloodPressureJournalBPSampleObserver samplesAdded:anchor:]
+ -[HDHRBloodPressureJournalBPSampleObserver samplesOfTypesWereRemoved:anchor:]
+ -[HDHRBloodPressureJournalBPSampleObserver setDidRegenerateNotificationsHandler:]
+ -[HDHRBloodPressureJournalBPSampleObserver setDidRequestNotificationsRemovalHandler:]
+ -[HDHRBloodPressureJournalBPSampleObserver setDidTriggerSyncHandler:]
+ -[HDHRBloodPressureJournalControlServer exportedInterface]
+ -[HDHRBloodPressureJournalControlServer initWithUUID:configuration:client:delegate:]
+ -[HDHRBloodPressureJournalControlServer journalManager:didAddOrModifyJournals:]
+ -[HDHRBloodPressureJournalControlServer remoteInterface]
+ -[HDHRBloodPressureJournalControlServer remote_closeJournal:completion:]
+ -[HDHRBloodPressureJournalControlServer remote_closeJournalWithIdentifier:completion:]
+ -[HDHRBloodPressureJournalControlServer remote_fetchActiveJournalWithCompletion:]
+ -[HDHRBloodPressureJournalControlServer remote_fetchAllJournalsWithCompletion:]
+ -[HDHRBloodPressureJournalControlServer remote_observeJournalChanges:completion:]
+ -[HDHRBloodPressureJournalControlServer remote_saveJournal:completion:]
+ -[HDHRBloodPressureJournalControlServer remote_snoozeJournalNotificationWithIdentifier:journalType:userInfo:onDate:completion:]
+ -[HDHRBloodPressureJournalManager .cxx_destruct]
+ -[HDHRBloodPressureJournalManager _enumerateJournalsWithPredicate:limit:orderingTerms:transaction:error:enumerationHandler:]
+ -[HDHRBloodPressureJournalManager _rescheduleNotificationandIsUserInitated:]
+ -[HDHRBloodPressureJournalManager _rescheduleNotificationandIsUserInitated:].cold.1
+ -[HDHRBloodPressureJournalManager bloodPressureJournalWithIdentifier:error:]
+ -[HDHRBloodPressureJournalManager bloodPressureJournalsWithError:]
+ -[HDHRBloodPressureJournalManager bloodPressureJournalsWithLimit:ascending:error:]
+ -[HDHRBloodPressureJournalManager bloodPressureJournalsWithPredicate:error:]
+ -[HDHRBloodPressureJournalManager closeAllExpiredJournalsBy:error:]
+ -[HDHRBloodPressureJournalManager enumerateJournalsWithPredicate:limit:orderingTerms:error:enumerationHandler:]
+ -[HDHRBloodPressureJournalManager initWithProfile:]
+ -[HDHRBloodPressureJournalManager insertBloodPressureJournal:isUserInitiated:error:onCommit:onRollback:]
+ -[HDHRBloodPressureJournalManager insertBloodPressureJournals:error:onCommit:onRollback:]
+ -[HDHRBloodPressureJournalManager insertBloodPressureJournals:isUserInitiated:error:onCommit:onRollback:]
+ -[HDHRBloodPressureJournalManager latestActiveBloodPressureJournalWithError:]
+ -[HDHRBloodPressureJournalManager notifyObserversOfAddOrModifyJournals:]
+ -[HDHRBloodPressureJournalManager registerObserver:queue:]
+ -[HDHRBloodPressureJournalManager unregisterObserver:]
+ -[HDHRBloodPressureJournalManager updateNotificationSyncManagerWithClosedJournals:]
+ -[HDHRBloodPressureJournalNotificationIdentifier .cxx_destruct]
+ -[HDHRBloodPressureJournalNotificationIdentifier identifierString]
+ -[HDHRBloodPressureJournalNotificationIdentifier initWithIdentifierString:]
+ -[HDHRBloodPressureJournalNotificationIdentifier initWithJournalIdentifier:notificationDayIndex:journalWindowType:]
+ -[HDHRBloodPressureJournalNotificationIdentifier journalIdentifier]
+ -[HDHRBloodPressureJournalNotificationIdentifier journalWindowType]
+ -[HDHRBloodPressureJournalNotificationIdentifier notificationDayIndex]
+ -[HDHRBloodPressureJournalNotificationInfo .cxx_destruct]
+ -[HDHRBloodPressureJournalNotificationInfo bedtimeAlarmCount]
+ -[HDHRBloodPressureJournalNotificationInfo bedtimeAlarmStartDate]
+ -[HDHRBloodPressureJournalNotificationInfo description]
+ -[HDHRBloodPressureJournalNotificationInfo initWithWakeupAlarmStartDate:wakeupAlarmCount:bedtimeAlarmStartDate:bedtimeAlarmCount:]
+ -[HDHRBloodPressureJournalNotificationInfo setBedtimeAlarmCount:]
+ -[HDHRBloodPressureJournalNotificationInfo setBedtimeAlarmStartDate:]
+ -[HDHRBloodPressureJournalNotificationInfo setWakeupAlarmCount:]
+ -[HDHRBloodPressureJournalNotificationInfo setWakeupAlarmStartDate:]
+ -[HDHRBloodPressureJournalNotificationInfo wakeupAlarmCount]
+ -[HDHRBloodPressureJournalNotificationInfo wakeupAlarmStartDate]
+ -[HDHRBloodPressureJournalNotificationManager .cxx_destruct]
+ -[HDHRBloodPressureJournalNotificationManager _alarm:confirmDeliveryByRemovingEvent:]
+ -[HDHRBloodPressureJournalNotificationManager _alarm:confirmDeliveryByRemovingEvents:]
+ -[HDHRBloodPressureJournalNotificationManager _alarm:dueEventsToHandleFrom:date:]
+ -[HDHRBloodPressureJournalNotificationManager _alarmTimeForDate:withScheduleTimeInterval:calendar:]
+ -[HDHRBloodPressureJournalNotificationManager _bloodPressureSampleFrom:error:]
+ -[HDHRBloodPressureJournalNotificationManager _isDueEventExpired:fromDate:]
+ -[HDHRBloodPressureJournalNotificationManager _isEventOnHold:]
+ -[HDHRBloodPressureJournalNotificationManager _isEventOnHold:].cold.1
+ -[HDHRBloodPressureJournalNotificationManager _isJournal:inNoticationPeriodFor:calendar:]
+ -[HDHRBloodPressureJournalNotificationManager _isJournal:inNoticationPeriodFor:calendar:].cold.1
+ -[HDHRBloodPressureJournalNotificationManager _nextDayFor:calendar:]
+ -[HDHRBloodPressureJournalNotificationManager _notificationInfoFor:startDate:calendar:schedulingUUID:error:]
+ -[HDHRBloodPressureJournalNotificationManager _notificationInfoForLearnHypertensionRiskJournal:startDate:calendar:schedulingUUID:error:]
+ -[HDHRBloodPressureJournalNotificationManager _notificationInfoForMonitorHypertensionJournal:startDate:calendar:schedulingUUID:error:]
+ -[HDHRBloodPressureJournalNotificationManager _notificationInfoForMonitorHypertensionJournal:startDate:calendar:schedulingUUID:error:].cold.1
+ -[HDHRBloodPressureJournalNotificationManager _notificationSchedulingIsEnabled]
+ -[HDHRBloodPressureJournalNotificationManager _notificationsEnabled]
+ -[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:]
+ -[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]
+ -[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:].cold.1
+ -[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveExpiredEvents:]
+ -[HDHRBloodPressureJournalNotificationManager _removeAllExpiredEvents]
+ -[HDHRBloodPressureJournalNotificationManager _removeAllExpiredEvents].cold.1
+ -[HDHRBloodPressureJournalNotificationManager _scheduleNotificationsWithError:]
+ -[HDHRBloodPressureJournalNotificationManager _scheduleNotificationsWithStartDate:error:]
+ -[HDHRBloodPressureJournalNotificationManager _scheduleNotificationsWithStartDate:schedulingUUID:error:]
+ -[HDHRBloodPressureJournalNotificationManager _scheduleRestorableAlarmEventsWith:forJournal:calendar:schedulingUUID:error:]
+ -[HDHRBloodPressureJournalNotificationManager initWithProfile:]
+ -[HDHRBloodPressureJournalNotificationManager initWithProfile:operation:]
+ -[HDHRBloodPressureJournalNotificationManager performWorkForOperation:profile:databaseAccessibilityAssertion:completion:]
+ -[HDHRBloodPressureJournalNotificationManager removeDeliveredNotificationsForSamples:journal:]
+ -[HDHRBloodPressureJournalNotificationManager scheduleNotificationsWithReason:error:]
+ -[HDHRBloodPressureJournalNotificationManager setUnitTesting_configuredDate:]
+ -[HDHRBloodPressureJournalNotificationManager setUnitTesting_expirationRestorableAlarm:]
+ -[HDHRBloodPressureJournalNotificationManager setUnitTesting_forceEnableNotifications:]
+ -[HDHRBloodPressureJournalNotificationManager setUnitTesting_restorableAlarm:]
+ -[HDHRBloodPressureJournalNotificationManager setUnitTesting_restorableAlarmQueue:]
+ -[HDHRBloodPressureJournalNotificationManager setUnitTesting_shouldIgnoreDeliveredAlarmEvents:]
+ -[HDHRBloodPressureJournalNotificationManager setUnitTesting_snoozeRestorableAlarm:]
+ -[HDHRBloodPressureJournalNotificationManager snoozeBloodPressureJournalNotificationWithIdentifier:journalType:userInfo:onDate:error:]
+ -[HDHRBloodPressureJournalNotificationManager unitTesting_configuredDate]
+ -[HDHRBloodPressureJournalNotificationManager unitTesting_expirationRestorableAlarm]
+ -[HDHRBloodPressureJournalNotificationManager unitTesting_forceEnableNotifications]
+ -[HDHRBloodPressureJournalNotificationManager unitTesting_restorableAlarmQueue]
+ -[HDHRBloodPressureJournalNotificationManager unitTesting_restorableAlarm]
+ -[HDHRBloodPressureJournalNotificationManager unitTesting_shouldIgnoreDeliveredAlarmEvents]
+ -[HDHRBloodPressureJournalNotificationManager unitTesting_snoozeRestorableAlarm]
+ -[HDHRBloodPressureJournalNotificationMeasurementInfo initWithMeasurementIndex:measurementCount:measurementWindowType:]
+ -[HDHRBloodPressureJournalNotificationMeasurementInfo isEqual:]
+ -[HDHRBloodPressureJournalNotificationMeasurementInfo measurementCount]
+ -[HDHRBloodPressureJournalNotificationMeasurementInfo measurementIndex]
+ -[HDHRBloodPressureJournalNotificationMeasurementInfo measurementWindowType]
+ -[HDHRBloodPressureJournalNotificationSyncManager .cxx_destruct]
+ -[HDHRBloodPressureJournalNotificationSyncManager _identifiersForHoldInstructionsFrom:journal:]
+ -[HDHRBloodPressureJournalNotificationSyncManager bloodPressureJournalsClosed:]
+ -[HDHRBloodPressureJournalNotificationSyncManager bloodPressureSamplesAdded:forJournal:]
+ -[HDHRBloodPressureJournalNotificationSyncManager initWithProfile:]
+ -[HDHRBloodPressureJournalNotificationSyncManager isAlarmEventWithIdentifiersOnHold:journalIdentifier:error:]
+ -[HDHRBloodPressureJournalNotificationSyncManager isAlarmEventWithJournalIdentifierOnHold:error:]
+ -[HDHRBloodPressureJournalNotificationSyncManager isAlarmEventWithNotificationIdentifierOnHold:error:]
+ -[HDHRBloodPressureJournalNotificationSyncManager notificationSyncClient:didReceiveInstructionWithAction:]
+ -[HDHRBloodPressureJournalNotificationSyncManager notificationSyncClient:didReceiveInstructionWithAction:].cold.1
+ -[HDHRBloodPressureJournalNotificationSyncManager notificationSyncClient]
+ -[HDHRBloodPressureJournalPeriodicScheduler .cxx_destruct]
+ -[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]
+ -[HDHRBloodPressureJournalPeriodicScheduler _resetActivityInterval]
+ -[HDHRBloodPressureJournalPeriodicScheduler activity]
+ -[HDHRBloodPressureJournalPeriodicScheduler database:protectedDataDidBecomeAvailable:]
+ -[HDHRBloodPressureJournalPeriodicScheduler initWithDaemon:]
+ -[HDHRBloodPressureJournalPeriodicScheduler performPeriodicActivity:completion:]
+ -[HDHRBloodPressureJournalPeriodicScheduler performPeriodicActivity:completion:].cold.1
+ -[HDHRBloodPressureJournalPeriodicScheduler periodicActivity:configureXPCActivityCriteria:]
+ -[HDHRBloodPressureJournalPeriodicScheduler periodicActivity:configureXPCActivityCriteria:].cold.1
+ -[HDHRBloodPressureJournalPeriodicScheduler periodicActivityRequiresProtectedData:]
+ -[HDHRBloodPressureJournalPeriodicScheduler profileDidBecomeReady:]
+ -[HDHRBloodPressureJournalSyncRequester .cxx_destruct]
+ -[HDHRBloodPressureJournalSyncRequester initWithProfile:]
+ -[HDHRBloodPressureJournalSyncRequester requestStateSyncWithReason:]
+ -[HDHRBloodPressureJournalTimeZoneObserver .cxx_destruct]
+ -[HDHRBloodPressureJournalTimeZoneObserver didRegenerateNotificationsHandler]
+ -[HDHRBloodPressureJournalTimeZoneObserver hasTimeZoneChange]
+ -[HDHRBloodPressureJournalTimeZoneObserver initWithProfile:]
+ -[HDHRBloodPressureJournalTimeZoneObserver initWithProfile:userDefaults:]
+ -[HDHRBloodPressureJournalTimeZoneObserver localTimeZone]
+ -[HDHRBloodPressureJournalTimeZoneObserver setDidRegenerateNotificationsHandler:]
+ -[HDHRBloodPressureJournalTimeZoneObserver setUnitTesting_localTimeZone:]
+ -[HDHRBloodPressureJournalTimeZoneObserver timeZoneDidChange:]
+ -[HDHRBloodPressureJournalTimeZoneObserver timeZoneDidChange:].cold.1
+ -[HDHRBloodPressureJournalTimeZoneObserver timeZoneFromDefaults]
+ -[HDHRBloodPressureJournalTimeZoneObserver unitTesting_localTimeZone]
+ -[HDHRBloodPressureJournalTimeZoneObserver updateDefaultsTimeZone:]
+ -[HDHRBloodPressureJournalTimeZoneObserver updateTimeZoneIfRequired]
+ -[HDHRCarouselUITriggerObserver _postHypertensionNotificationWithCompletion:]
+ -[HDHRHypertensionMeasurementAnalyzer .cxx_destruct]
+ -[HDHRHypertensionMeasurementAnalyzer _analyzeMeasurementsWithDateInterval:error:]
+ -[HDHRHypertensionMeasurementAnalyzer _measurementsWithDateInterval:error:]
+ -[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:databaseTransactionContext:error:]
+ -[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleWithDateInterval:error:]
+ -[HDHRHypertensionMeasurementAnalyzer initWithProfile:]
+ -[HDHRHypertensionMeasurementAnalyzer initWithProfile:analysisWindowInterval:keyValueDomain:analyticsEventSubmissionManager:]
+ -[HDHRHypertensionMeasurementAnalyzer init]
+ -[HDHRHypertensionMeasurementAnalyzer performAnalysisWithStartDate:endDate:databaseTransactionContext:error:]
+ -[HDHRHypertensionMeasurementAnalyzer performAnalysisWithStartDate:endDate:databaseTransactionContext:error:].cold.1
+ -[HDHRHypertensionMeasurementAnalyzer performAnalysisWithStartDate:endDate:databaseTransactionContext:error:].cold.2
+ -[HDHRHypertensionNotificationAnalysisEvent .cxx_destruct]
+ -[HDHRHypertensionNotificationAnalysisEvent _daysSinceHTNLastEnabled:]
+ -[HDHRHypertensionNotificationAnalysisEvent _dnuAdditionalPayload]
+ -[HDHRHypertensionNotificationAnalysisEvent _dnuNumDaysWatchWornAnalyticsWithCalendar:]
+ -[HDHRHypertensionNotificationAnalysisEvent _dnuNumDaysWatchWornAnalyticsWithCalendar:].cold.1
+ -[HDHRHypertensionNotificationAnalysisEvent _featureStatusForFeatureIdentifier:dataSource:error:]
+ -[HDHRHypertensionNotificationAnalysisEvent _ihaAdditionalPayload]
+ -[HDHRHypertensionNotificationAnalysisEvent _ihaDemographicsPayloadWithDataSource:]
+ -[HDHRHypertensionNotificationAnalysisEvent _isAFibHistoryEnabledWithDataSource:]
+ -[HDHRHypertensionNotificationAnalysisEvent eventName]
+ -[HDHRHypertensionNotificationAnalysisEvent initWithProfile:dateInterval:additionalPayload:]
+ -[HDHRHypertensionNotificationAnalysisEvent init]
+ -[HDHRHypertensionNotificationAnalysisEvent isEventSubmissionIHAGated]
+ -[HDHRHypertensionNotificationAnalysisEvent makeIHAGatedEventPayloadWithDataSource:error:]
+ -[HDHRHypertensionNotificationAnalysisEvent makeIHAGatedEventPayloadWithDataSource:error:].cold.1
+ -[HDHRHypertensionNotificationAnalysisEvent makeIHAGatedEventPayloadWithDataSource:error:].cold.2
+ -[HDHRHypertensionNotificationAnalysisEvent makeIHAGatedEventPayloadWithDataSource:error:].cold.3
+ -[HDHRHypertensionNotificationAnalysisEvent makeIHAGatedEventPayloadWithDataSource:error:].cold.4
+ -[HDHRHypertensionNotificationAnalysisEvent makeIHAGatedEventPayloadWithDataSource:error:].cold.5
+ -[HDHRHypertensionNotificationAnalysisEvent makeUnrestrictedEventPayloadWithDataSource:error:]
+ -[HDHRHypertensionNotificationDeliveryEvent .cxx_destruct]
+ -[HDHRHypertensionNotificationDeliveryEvent _payloadForEventType:]
+ -[HDHRHypertensionNotificationDeliveryEvent eventName]
+ -[HDHRHypertensionNotificationDeliveryEvent initWithProfile:type:]
+ -[HDHRHypertensionNotificationDeliveryEvent isEventSubmissionIHAGated]
+ -[HDHRHypertensionNotificationDeliveryEvent makeIHAGatedEventPayloadWithDataSource:error:]
+ -[HDHRHypertensionNotificationDeliveryEvent makeUnrestrictedEventPayloadWithDataSource:error:]
+ -[HDHRHypertensionNotificationManager .cxx_destruct]
+ -[HDHRHypertensionNotificationManager _queue_addNotificationRequestForHypertensionEvent:]
+ -[HDHRHypertensionNotificationManager _queue_addNotificationRequestForHypertensionEvent:].cold.1
+ -[HDHRHypertensionNotificationManager daemonReady:]
+ -[HDHRHypertensionNotificationManager dealloc]
+ -[HDHRHypertensionNotificationManager initWithProfile:]
+ -[HDHRHypertensionNotificationManager samplesAdded:anchor:]
+ -[HDHRHypertensionNotificationManager setUnitTesting_notificationNotPostedHandler:]
+ -[HDHRHypertensionNotificationManager setUnitTesting_postNotificationWithRequestHandler:]
+ -[HDHRHypertensionNotificationManager unitTesting_notificationNotPostedHandler]
+ -[HDHRHypertensionNotificationManager unitTesting_postNotificationWithRequestHandler]
+ -[HDHRHypertensionNotificationsAnalysisScheduler .cxx_destruct]
+ -[HDHRHypertensionNotificationsAnalysisScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler _lastAnalysisWindowEndDateOrOnboardingDateWithFeatureStatus:error:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler _queue_performAnalysisIfNeededWithDatabaseTransactionContext:completion:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler _queue_resetActivityInterval]
+ -[HDHRHypertensionNotificationsAnalysisScheduler _takeAccessibilityAssertion]
+ -[HDHRHypertensionNotificationsAnalysisScheduler database:protectedDataDidBecomeAvailable:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler database:protectedDataDidBecomeAvailable:].cold.1
+ -[HDHRHypertensionNotificationsAnalysisScheduler featureStatusProviding:didUpdateFeatureStatus:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler featureStatusProviding:didUpdateFeatureStatus:].cold.1
+ -[HDHRHypertensionNotificationsAnalysisScheduler initWithProfile:featureStatusProvider:keyValueDomain:analysisWindowInterval:analysisWindowGraceInterval:analysisCadenceInterval:analysisRetryInterval:pregnancyStateProvider:measurementAnalyzer:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler initWithProfile:featureStatusProvider:pregnancyStateProvider:measurementAnalyzer:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler init]
+ -[HDHRHypertensionNotificationsAnalysisScheduler performPeriodicActivity:completion:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler periodicActivity:configureXPCActivityCriteria:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler periodicActivityRequiresProtectedData:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler periodicActivity]
+ -[HDHRHypertensionNotificationsAnalysisScheduler profileDidBecomeReady:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler setUnitTest_analysisOperationEnqueued:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler setUnitTest_featureStatusUpdateBlock:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler setUnitTest_latestAnalysisStartDate:]
+ -[HDHRHypertensionNotificationsAnalysisScheduler unitTest_analysisOperationEnqueued]
+ -[HDHRHypertensionNotificationsAnalysisScheduler unitTest_featureStatusUpdateBlock]
+ -[HDHRHypertensionNotificationsAnalysisScheduler unitTest_latestAnalysisStartDate]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent .cxx_destruct]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _countOfLast30DaysWithHypertensiveMeasurementSamplesWithCurrentDate:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _countOfLast30DaysWithHypertensiveMeasurementSamplesWithCurrentDate:calendar:].cold.1
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _countOfSamplesWithType:dateInterval:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _countOfSamplesWithType:dateInterval:additionalPredicate:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _countOfSamplesWithType:dateInterval:additionalPredicate:].cold.1
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _dateIntervalForCalendarDays:fromDate:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _daysSinceLastHypertensionNotificationToDate:withinDateInterval:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _daysSinceLastHypertensionNotificationToDate:withinDateInterval:calendar:].cold.1
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _daysSinceMostRecentSampleWithType:toDate:calendar:additionalPredicate:error:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _daysSinceOldestHypertensionNotificationToDate:withinDateInterval:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _daysSinceOldestHypertensionNotificationToDate:withinDateInterval:calendar:].cold.1
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _daysSinceOldestSampleWithType:toDate:calendar:additionalPredicate:error:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _dnuNumDaysAnalyticsWithCurrentDate:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _dnuOnboardingAnalyticsWithDataSource:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _dnuSampleCountsInPreviousCalendarDayWithCurrentDate:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _ihaBPJCountAnalyticsWithCurrentDate:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _ihaBPJCountAnalyticsWithCurrentDate:calendar:].cold.1
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _ihaNumDaysAnalyticsWithCurrentDate:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _ihaOnboardingAnalyticsWithDataSource:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _ihaSampleCountsAnalyticsWithCurrentDate:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _numDaysSinceLastAnalysisWithCurrentDate:calendar:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent _numDaysSinceLastAnalysisWithCurrentDate:calendar:].cold.1
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent eventName]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent initWithProfile:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent isEventSubmissionIHAGated]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent makeIHAGatedEventPayloadWithDataSource:error:]
+ -[HDHRHypertensionNotificationsDailyAnalyticsEvent makeUnrestrictedEventPayloadWithDataSource:error:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager .cxx_destruct]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _isFeatureRescindedWithUsageEvaluation:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _isFeatureUnavailableForNonRescindedReasonsWithUsageEvaluation:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _presentHypertensionNotificationsReEnabledAlert]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _presentHypertensionNotificationsRescindedAlertForUsageEvaluation:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _presentHypertensionNotificationsRescindedAlertForUsageEvaluation:].cold.1
+ -[HDHRHypertensionNotificationsRescindedAlertManager _presentNotificationWithTitle:message:type:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _queue_presentRescindedOrReEnabledAlertIfNeededWithFeatureStatus:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _queue_presentRescindedOrReEnabledAlertIfNeededWithFeatureStatus:].cold.1
+ -[HDHRHypertensionNotificationsRescindedAlertManager _queue_presentRescindedOrReEnabledAlertIfNeededWithFeatureStatus:].cold.2
+ -[HDHRHypertensionNotificationsRescindedAlertManager _queue_presentRescindedOrReEnabledAlertIfNeededWithFeatureStatus:].cold.3
+ -[HDHRHypertensionNotificationsRescindedAlertManager _queue_pullFeatureStatusAndPresentAlertIfNeeded]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _queue_pullFeatureStatusAndPresentAlertIfNeeded].cold.1
+ -[HDHRHypertensionNotificationsRescindedAlertManager _rescindedAlertBodyForUsageEvaluation:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _rescindedAlertTitleForUsageEvaluation:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _rescindedAlertTypeForUsageEvaluation:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager _unitTesting_callNotificationNotPostedHandlerIfSet]
+ -[HDHRHypertensionNotificationsRescindedAlertManager daemonReady:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager database:protectedDataDidBecomeAvailable:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager dealloc]
+ -[HDHRHypertensionNotificationsRescindedAlertManager featureStatusProviding:didUpdateFeatureStatus:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager initWithProfile:featureStatusProvider:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager initWithProfile:featureStatusProvider:pairedSyncStateProvider:keyValueDomain:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager setUnitTesting_notificationNotPostedHandler:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager setUnitTesting_postNotificationHandler:]
+ -[HDHRHypertensionNotificationsRescindedAlertManager unitTesting_notificationNotPostedHandler]
+ -[HDHRHypertensionNotificationsRescindedAlertManager unitTesting_postNotificationHandler]
+ -[HDHRHypertensionNotificationsSettingsResetter .cxx_destruct]
+ -[HDHRHypertensionNotificationsSettingsResetter featureAvailabilityProvidingDidUpdateOnboardingCompletion:]
+ -[HDHRHypertensionNotificationsSettingsResetter featureAvailabilityProvidingDidUpdateOnboardingCompletion:].cold.1
+ -[HDHRHypertensionNotificationsSettingsResetter featureAvailabilityProvidingDidUpdateOnboardingCompletion:].cold.2
+ -[HDHRHypertensionNotificationsSettingsResetter featureAvailabilityProvidingDidUpdateOnboardingCompletion:].cold.3
+ -[HDHRHypertensionNotificationsSettingsResetter initWithKeyValueDomain:featureAvailabilityProvider:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager .cxx_destruct]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager _reportAnalyticsEventForCountryCode:eventType:errorCategory:errorDetail:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager _reportAnalyticsEventForCountryCode:eventType:errorCategory:errorDetail:].cold.1
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager _reportDeliveryAnalyticsEventForCountryCode:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager _reportErrorAnalyticsEventForCountryCode:errorCategory:errorDetail:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager _startObservingOnboardingChanges]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager _stopObservingOnboardingChanges]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager doWorkWithCompletion:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager featureAvailabilityExtensionDidUpdateRegionAvailability:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager featureAvailabilityExtensionOnboardingCompletionDataDidBecomeAvailable:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager featureAvailabilityProvidingDidUpdateOnboardingCompletion:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager hypertensionNotificationsAvailabilityManager]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager initWithProfile:v1FeatureAvailabilityManager:v2FeatureAvailabilityManager:hypertensionNotificationsFeatureAvailabilityManager:analyticsSubmissionManager:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager initWithProfile:v1FeatureAvailabilityManager:v2FeatureAvailabilityManager:hypertensionNotificationsFeatureAvailabilityManager:analyticsSubmissionManager:protectedDataOperation:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager pairedDeviceCapabilitiesDidUpdate:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager performWorkForOperation:profile:databaseAccessibilityAssertion:completion:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager setUnitTesting_didRequestRetryOnFeatureStatusChangeHandler:]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager unitTesting_didRequestRetryOnFeatureStatusChangeHandler]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager v1FeatureAvailabilityManager]
+ -[HDHRIrregularRhythmNotificationsV2UpgradeManager v2FeatureAvailabilityManager]
+ -[HDHeartDaemonExtension bloodPressureJournalPeriodicScheduler]
+ -[HDHeartProfileExtension _setupBloodPressureDailyAnalyticsManagerWithProfile:]
+ -[HDHeartProfileExtension _setupBloodPressureJournalManagerWithProfile:]
+ -[HDHeartProfileExtension _setupBloodPressureJournalNotificationManagerWithProfile:]
+ -[HDHeartProfileExtension _setupBloodPressureJournalNotificationSyncManagerWithProfile:]
+ -[HDHeartProfileExtension _setupBloodPressureJournalSyncRequesterWithProfile:]
+ -[HDHeartProfileExtension _setupBloodPressureJournalTimeZoneObserverWithProfile:]
+ -[HDHeartProfileExtension _setupBloodPressureSampleObserverWithProfile:]
+ -[HDHeartProfileExtension _setupHypertensionNotificationsWithProfile:]
+ -[HDHeartProfileExtension bloodPressureJournalManager]
+ -[HDHeartProfileExtension bloodPressureJournalNotificationManager]
+ -[HDHeartProfileExtension bloodPressureJournalNotificationSyncManager]
+ -[HDHeartProfileExtension bloodPressureJournalSyncRequester]
+ -[HDHeartProfileExtension bloodPressureJournalTimeZoneObserver]
+ -[HDHeartProfileExtension bloodPressureSampleObserver]
+ -[HDNotificationManager(BloodPressureJournal) getBloodPressureJournalDeliveredNotificationIdentifiersWithCompletionHandler:]
+ -[HDRestorableAlarm(BloodPressureJournal) bloodPressureJournalAlarmEventWithNotificationIdentifier:journalType:dueDate:isFollowUp:measurementInfo:]
+ -[HDRestorableAlarm(BloodPressureJournal) bloodPressureJournalExpirationEventWithIdentifier:dueDate:]
+ -[HKHRBloodPressureJournalStateSyncEntity init]
+ -[HKHRStateSyncBloodPressureJournalDelegate description]
+ -[HKHRStateSyncBloodPressureJournalDelegate domain]
+ -[HKHRStateSyncBloodPressureJournalDelegate fetchCloudState:codableSyncState:profile:error:]
+ -[HKHRStateSyncBloodPressureJournalDelegate fetchLocalState:profile:transaction:error:]
+ -[HKHRStateSyncBloodPressureJournalDelegate key]
+ -[HKHRStateSyncBloodPressureJournalDelegate persistCloudState:profile:error:]
+ -[HKHRStateSyncBloodPressureJournalDelegate persistCloudState:profile:error:].cold.1
+ -[HKHRStateSyncBloodPressureJournalDelegate shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]
+ -[HKHRStateSyncBloodPressureJournalDelegate shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:].cold.1
+ -[HKHRStateSyncBloodPressureJournalDelegate shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:].cold.2
+ -[HKHRStateSyncBloodPressureJournalDelegate supportedSyncVersionRange]
+ -[HKHRStateSyncBloodPressureJournalDelegate updateCodableSyncState:withMergeState:profile:error:]
+ -[HKHRStateSyncBloodPressureJournalDelegate updateCodableSyncState:withMergeState:profile:error:].cold.1
+ -[HKNotificationInstruction(BloodPressureJournal) initWithAction:alarmEventIdentifier:]
+ -[HKNotificationInstruction(BloodPressureJournal) initWithAction:journalIdentifier:]
+ GCC_except_table12
+ GCC_except_table14
+ GCC_except_table17
+ GCC_except_table18
+ GCC_except_table5
+ _HDAnalyticsCountOfIntervalsForQuantityType
+ _HDAnalyticsStatisticsCollectionOfIntervalsForQuantityType
+ _HDDecodeDateForValue
+ _HDEncodeValueForDate
+ _HDHRAnalyticsPropertyNameAfibOnboardedVersion
+ _HDHRAnalyticsPropertyNameAlertStatus
+ _HDHRAnalyticsPropertyNameCountHTNotificationsUntilMostRecentBPJStarted
+ _HDHRAnalyticsPropertyNameCountryCodeHTN
+ _HDHRAnalyticsPropertyNameDaysSinceNotificationsLastEnabled
+ _HDHRAnalyticsPropertyNameDifferenceInDaysBetweenFirstHTNotificationAndBPJStarted
+ _HDHRAnalyticsPropertyNameDifferenceInDaysBetweenMostRecentHTNotificationAndBPJStarted
+ _HDHRAnalyticsPropertyNameIRNOnboardedVersion
+ _HDHRAnalyticsPropertyNameIsAfibHistoryEnabled
+ _HDHRAnalyticsPropertyNameIsOnboardedHTN
+ _HDHRAnalyticsPropertyNameMeanEnteredBpCategory
+ _HDHRAnalyticsPropertyNameMeanScore
+ _HDHRAnalyticsPropertyNameNumBGHRHoursPast30Days
+ _HDHRAnalyticsPropertyNameNumBackgroundHRSamplesInPreviousCalendarDay
+ _HDHRAnalyticsPropertyNameNumDaysSinceLastAnalysis
+ _HDHRAnalyticsPropertyNameNumDaysSinceLastHTNotification
+ _HDHRAnalyticsPropertyNameNumDaysSinceOpenedHTNDataTypeRoom
+ _HDHRAnalyticsPropertyNameNumDaysWatchWornMoreThan12Hours
+ _HDHRAnalyticsPropertyNameNumDaysWatchWornMoreThan8Hours
+ _HDHRAnalyticsPropertyNameNumDaysWithAdequateDataInPast30Days
+ _HDHRAnalyticsPropertyNameNumHRVValuesPast30Days
+ _HDHRAnalyticsPropertyNameNumHTNotificationsInPast180Days
+ _HDHRAnalyticsPropertyNameNumHTNotificationsInPast30Days
+ _HDHRAnalyticsPropertyNameNumScores
+ _HDHRAnalyticsPropertyNameNumStandHoursInPast30Days
+ _HDHRAnalyticsPropertyNameNumStandHoursInPreviousCalendarDay
+ _HDHRAnalyticsPropertyNameNumTachogramsInPreviousCalendarDay
+ _HDHRAnalyticsPropertyNameTotalCountBpValuesEntered
+ _HDHRAnalyticsPropertyNameValidScoreDays
+ _HDHRAnalyticsPropertyNameWeeksSinceOnboardedHTN
+ _HDHRBloodPressureClassificationAnalyticsString
+ _HDHRBloodPressureJournalPredicateForIdentifier
+ _HDHRBloodPressureJournalPredicateForStartDate
+ _HDHRBloodPressureJournalPredicateForState
+ _HDHRHypertensionNotificationRequestForEvent
+ _HDHRHypertensionNotificationsAnalysisCadenceIntervalRespectingOverride
+ _HDHRHypertensionNotificationsAnalysisResultForceHypertensionOverride
+ _HDHRHypertensionNotificationsAnalysisSchedulerRetryIntervalRespectingOverride
+ _HDHRHypertensionNotificationsAnalysisWindowGraceIntervalRespectingOverride
+ _HDHRHypertensionNotificationsAnalysisWindowIntervalRespectingOverride
+ _HDHRHypertensionNotificationsDisabledNotificationShownDateKey
+ _HDSQLiteBindNumberToProperty
+ _HDSQLiteBindSecureCodingObjectToProperty
+ _HDSQLiteColumnWithNameAsInt64
+ _HDSQLiteColumnWithNameAsObject
+ _HDSampleEntityPredicateForEndDate
+ _HKAnalyticsPropertyNameIsImproveHealthAndActivityAllowed
+ _HKAnalyticsSigFigBinnedValue
+ _HKBloodPressureClassificationCategoryAHAElevated
+ _HKBloodPressureClassificationCategoryAHAHypertensionStage1
+ _HKBloodPressureClassificationCategoryAHAHypertensionStage2
+ _HKBloodPressureClassificationCategoryAHAHypertensiveCrisis
+ _HKBloodPressureClassificationCategoryAHANormal
+ _HKCategoryTypeIdentifierHypertensionEvent
+ _HKCorrelationTypeIdentifierBloodPressure
+ _HKFeatureAvailabilityContextAnalysis
+ _HKFeatureAvailabilityContextBloodPressureJournalCanBeStarted
+ _HKFeatureAvailabilityRequirementIdentifierActiveRemoteDeviceIsPresentWhenRequiredForRegionAvailabilityOrDeviceCapability
+ _HKFeatureAvailabilityRequirementIdentifierCapabilityIsSupportedOnActiveRemoteDevice
+ _HKFeatureAvailabilityRequirementIdentifierFeatureFlagIsEnabled
+ _HKFeatureAvailabilityRequirementIdentifierNotInStoreDemoMode
+ _HKFeatureIdentifierBloodPressureJournal
+ _HKFeatureIdentifierHypertensionNotifications
+ _HKFeatureSettingsKeyOnboardingAcknowledged
+ _HKFeatureSettingsKeyOnboardingAcknowledgedDate
+ _HKHRBloodPressureCloudSyncStateEntityDomain
+ _HKHRBloodPressureJournalNotificationMeasurementCountKey
+ _HKHRBloodPressureJournalNotificationMeasurementIndexKey
+ _HKHRBloodPressureJournalNotificationMeasurementWindowTypeKey
+ _HKHRBloodPressureJournalTimeZoneNameKey
+ _HKHRBloodPressureJournalValidTimeInDays
+ _HKHRHypertensionEventSampleDetailsLink
+ _HKHRHypertensionNotificationsDefaultsDomain
+ _HKHRHypertensionNotificationsLastAnalysisWindowEndDateKey
+ _HKHRHypertensionNotificationsLocalFeatureAttributes
+ _HKHRStateSyncBloodPressureJournalDelegateKey
+ _HKLogBloodPressureJournal
+ _HKQuantityTypeIdentifierBloodPressureDiastolic
+ _HKQuantityTypeIdentifierBloodPressureSystolic
+ _HKQuantityTypeIdentifierHypertensivePatternMeasurement
+ _HKSampleSortIdentifierStartDate
+ _NSStringFromHKNotificationInstructionAction
+ _NSStringFromProtocol
+ _NSSystemTimeZoneDidChangeNotification
+ _OBJC_CLASS_$_HAHypertensivePatternAnalyzer
+ _OBJC_CLASS_$_HAHypertensivePatternMeasurement
+ _OBJC_CLASS_$_HDAlarmEvent
+ _OBJC_CLASS_$_HDCloudSyncStateSampleWindowUpdater
+ _OBJC_CLASS_$_HDCloudSyncStateSampleWindowUpdaterConfiguration
+ _OBJC_CLASS_$_HDCloudSyncStateUpdater
+ _OBJC_CLASS_$_HDCodableBloodPressureJournal
+ _OBJC_CLASS_$_HDCodableBloodPressureJournalScheduleTimeInterval
+ _OBJC_CLASS_$_HDCodableBloodPressureJournalState
+ _OBJC_CLASS_$_HDCorrelationSampleEntity
+ _OBJC_CLASS_$_HDDataSyncUtilities
+ _OBJC_CLASS_$_HDHRBloodPressureDailyAnalyticsEvent
+ _OBJC_CLASS_$_HDHRBloodPressureJournalBPSampleObserver
+ _OBJC_CLASS_$_HDHRBloodPressureJournalControlServer
+ _OBJC_CLASS_$_HDHRBloodPressureJournalManager
+ _OBJC_CLASS_$_HDHRBloodPressureJournalNotificationIdentifier
+ _OBJC_CLASS_$_HDHRBloodPressureJournalNotificationInfo
+ _OBJC_CLASS_$_HDHRBloodPressureJournalNotificationManager
+ _OBJC_CLASS_$_HDHRBloodPressureJournalNotificationMeasurementInfo
+ _OBJC_CLASS_$_HDHRBloodPressureJournalNotificationSyncManager
+ _OBJC_CLASS_$_HDHRBloodPressureJournalPeriodicScheduler
+ _OBJC_CLASS_$_HDHRBloodPressureJournalSyncRequester
+ _OBJC_CLASS_$_HDHRBloodPressureJournalTimeZoneObserver
+ _OBJC_CLASS_$_HDHRHypertensionMeasurementAnalyzer
+ _OBJC_CLASS_$_HDHRHypertensionNotificationAnalysisEvent
+ _OBJC_CLASS_$_HDHRHypertensionNotificationDeliveryEvent
+ _OBJC_CLASS_$_HDHRHypertensionNotificationManager
+ _OBJC_CLASS_$_HDHRHypertensionNotificationsAnalysisScheduler
+ _OBJC_CLASS_$_HDHRHypertensionNotificationsDailyAnalyticsEvent
+ _OBJC_CLASS_$_HDHRHypertensionNotificationsRescindedAlertManager
+ _OBJC_CLASS_$_HDHRHypertensionNotificationsSettingsResetter
+ _OBJC_CLASS_$_HDHRIrregularRhythmNotificationsV2UpgradeManager
+ _OBJC_CLASS_$_HDMutableDatabaseTransactionContext
+ _OBJC_CLASS_$_HDNotificationSyncClient
+ _OBJC_CLASS_$_HDStateSyncEntitySchema
+ _OBJC_CLASS_$_HKBloodPressureClassificationEvaluator
+ _OBJC_CLASS_$_HKCorrelationType
+ _OBJC_CLASS_$_HKHRBloodPressureJournal
+ _OBJC_CLASS_$_HKHRBloodPressureJournalControl
+ _OBJC_CLASS_$_HKHRBloodPressureJournalNotification
+ _OBJC_CLASS_$_HKHRBloodPressureJournalNotificationAnalyticsUtilities
+ _OBJC_CLASS_$_HKHRBloodPressureJournalScheduleTimeInterval
+ _OBJC_CLASS_$_HKHRBloodPressureJournalStateSyncEntity
+ _OBJC_CLASS_$_HKHRHypertensionNotificationsFeatureAvailabilityRequirements
+ _OBJC_CLASS_$_HKHRLearnHypertensionJournalEntryProvider
+ _OBJC_CLASS_$_HKHRLearnHypertensionJournalSummaryBuilder
+ _OBJC_CLASS_$_HKHRMonitorHypertensionJournalSummaryBuilder
+ _OBJC_CLASS_$_HKHRStateSyncBloodPressureJournalDelegate
+ _OBJC_CLASS_$_HKNotificationInstruction
+ _OBJC_CLASS_$_HKStateSyncRequest
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_UNNotificationSound
+ _OBJC_IVAR_$_HDHRBloodPressureDailyAnalyticsEvent._bloodPressureJournalManager
+ _OBJC_IVAR_$_HDHRBloodPressureDailyAnalyticsEvent._htnDailyAnalyticsEvent
+ _OBJC_IVAR_$_HDHRBloodPressureDailyAnalyticsEvent._pregnancyState
+ _OBJC_IVAR_$_HDHRBloodPressureDailyAnalyticsEvent._profile
+ _OBJC_IVAR_$_HDHRBloodPressureJournalBPSampleObserver._didRegenerateNotificationsHandler
+ _OBJC_IVAR_$_HDHRBloodPressureJournalBPSampleObserver._didRequestNotificationsRemovalHandler
+ _OBJC_IVAR_$_HDHRBloodPressureJournalBPSampleObserver._didTriggerSyncHandler
+ _OBJC_IVAR_$_HDHRBloodPressureJournalBPSampleObserver._profile
+ _OBJC_IVAR_$_HDHRBloodPressureJournalControlServer._lock
+ _OBJC_IVAR_$_HDHRBloodPressureJournalControlServer._shouldObserveChanges
+ _OBJC_IVAR_$_HDHRBloodPressureJournalManager._observers
+ _OBJC_IVAR_$_HDHRBloodPressureJournalManager._profile
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationIdentifier._identifierString
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationIdentifier._journalIdentifier
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationIdentifier._journalWindowType
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationIdentifier._notificationDayIndex
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationInfo._bedtimeAlarmCount
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationInfo._bedtimeAlarmStartDate
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationInfo._wakeupAlarmCount
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationInfo._wakeupAlarmStartDate
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._expirationRestorableAlarm
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._notificationAnalyticUtilities
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._operation
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._profile
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._queue
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._restorableAlarm
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._schedulingQueue
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._snoozeRestorableAlarm
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._unitTesting_configuredDate
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._unitTesting_expirationRestorableAlarm
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._unitTesting_forceEnableNotifications
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._unitTesting_restorableAlarm
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._unitTesting_restorableAlarmQueue
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._unitTesting_shouldIgnoreDeliveredAlarmEvents
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationManager._unitTesting_snoozeRestorableAlarm
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationMeasurementInfo._measurementCount
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationMeasurementInfo._measurementIndex
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationMeasurementInfo._measurementWindowType
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationSyncManager._notificationSyncClient
+ _OBJC_IVAR_$_HDHRBloodPressureJournalNotificationSyncManager._profile
+ _OBJC_IVAR_$_HDHRBloodPressureJournalPeriodicScheduler._daemon
+ _OBJC_IVAR_$_HDHRBloodPressureJournalPeriodicScheduler._periodicActivity
+ _OBJC_IVAR_$_HDHRBloodPressureJournalPeriodicScheduler._profile
+ _OBJC_IVAR_$_HDHRBloodPressureJournalSyncRequester._profile
+ _OBJC_IVAR_$_HDHRBloodPressureJournalTimeZoneObserver._defaults
+ _OBJC_IVAR_$_HDHRBloodPressureJournalTimeZoneObserver._didRegenerateNotificationsHandler
+ _OBJC_IVAR_$_HDHRBloodPressureJournalTimeZoneObserver._profile
+ _OBJC_IVAR_$_HDHRBloodPressureJournalTimeZoneObserver._unitTesting_localTimeZone
+ _OBJC_IVAR_$_HDHRHypertensionMeasurementAnalyzer._analysisWindowInterval
+ _OBJC_IVAR_$_HDHRHypertensionMeasurementAnalyzer._analyticsEventSubmissionManager
+ _OBJC_IVAR_$_HDHRHypertensionMeasurementAnalyzer._measurementsType
+ _OBJC_IVAR_$_HDHRHypertensionMeasurementAnalyzer._profile
+ _OBJC_IVAR_$_HDHRHypertensionMeasurementAnalyzer._syncedKeyValueDomain
+ _OBJC_IVAR_$_HDHRHypertensionNotificationAnalysisEvent._additionalPayload
+ _OBJC_IVAR_$_HDHRHypertensionNotificationAnalysisEvent._dateInterval
+ _OBJC_IVAR_$_HDHRHypertensionNotificationAnalysisEvent._profile
+ _OBJC_IVAR_$_HDHRHypertensionNotificationDeliveryEvent._areHealthNotificationsAuthorized
+ _OBJC_IVAR_$_HDHRHypertensionNotificationDeliveryEvent._profile
+ _OBJC_IVAR_$_HDHRHypertensionNotificationDeliveryEvent._type
+ _OBJC_IVAR_$_HDHRHypertensionNotificationManager._analyticsEventSubmissionManager
+ _OBJC_IVAR_$_HDHRHypertensionNotificationManager._profile
+ _OBJC_IVAR_$_HDHRHypertensionNotificationManager._queue
+ _OBJC_IVAR_$_HDHRHypertensionNotificationManager._unitTesting_notificationNotPostedHandler
+ _OBJC_IVAR_$_HDHRHypertensionNotificationManager._unitTesting_postNotificationWithRequestHandler
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._analysisCadenceInterval
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._analysisRetryInterval
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._analysisWindowGraceInterval
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._analysisWindowInterval
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._analyzer
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._featureStatusManager
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._periodicActivity
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._pregnancyStateProvider
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._profile
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._queue
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._syncedKeyValueDomain
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._unitTest_analysisOperationEnqueued
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._unitTest_featureStatusUpdateBlock
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsAnalysisScheduler._unitTest_latestAnalysisStartDate
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsDailyAnalyticsEvent._profile
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsRescindedAlertManager._analyticsEventSubmissionManager
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsRescindedAlertManager._featureStatusProvider
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsRescindedAlertManager._localKeyValueDomain
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsRescindedAlertManager._pairedSyncStateProvider
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsRescindedAlertManager._profile
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsRescindedAlertManager._queue
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsRescindedAlertManager._unitTesting_notificationNotPostedHandler
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsRescindedAlertManager._unitTesting_postNotificationHandler
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsSettingsResetter._featureAvailabilityProvider
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsSettingsResetter._keyValueDomain
+ _OBJC_IVAR_$_HDHRHypertensionNotificationsSettingsResetter._queue
+ _OBJC_IVAR_$_HDHRIrregularRhythmNotificationsV2UpgradeManager._analyticsSubmissionManager
+ _OBJC_IVAR_$_HDHRIrregularRhythmNotificationsV2UpgradeManager._hypertensionNotificationsAvailabilityManager
+ _OBJC_IVAR_$_HDHRIrregularRhythmNotificationsV2UpgradeManager._profile
+ _OBJC_IVAR_$_HDHRIrregularRhythmNotificationsV2UpgradeManager._protectedDataOperation
+ _OBJC_IVAR_$_HDHRIrregularRhythmNotificationsV2UpgradeManager._queue
+ _OBJC_IVAR_$_HDHRIrregularRhythmNotificationsV2UpgradeManager._unitTesting_didRequestRetryOnFeatureStatusChangeHandler
+ _OBJC_IVAR_$_HDHRIrregularRhythmNotificationsV2UpgradeManager._v1FeatureAvailabilityManager
+ _OBJC_IVAR_$_HDHRIrregularRhythmNotificationsV2UpgradeManager._v2FeatureAvailabilityManager
+ _OBJC_IVAR_$_HDHeartDaemonExtension._bloodPressureJournalPeriodicScheduler
+ _OBJC_IVAR_$_HDHeartProfileExtension._bloodPressureDailyEventManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._bloodPressureJournalBackgroundFeatureDeliveryManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._bloodPressureJournalFeatureAvailabilityManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._bloodPressureJournalManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._bloodPressureJournalNotificationManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._bloodPressureJournalNotificationSyncManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._bloodPressureJournalSyncRequester
+ _OBJC_IVAR_$_HDHeartProfileExtension._bloodPressureJournalTimeZoneObserver
+ _OBJC_IVAR_$_HDHeartProfileExtension._bloodPressureSampleObserver
+ _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionMeasurementAnalyzer
+ _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionNotificationManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionNotificationsAnalysisScheduler
+ _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionNotificationsAvailabilityManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionNotificationsBackgroundFeatureDeliveryManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionNotificationsRescindedAlertManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._hypertensionNotificationsSettingsResetter
+ _OBJC_IVAR_$_HDHeartProfileExtension._irregularRhythmNotificationsV2UpgradeManager
+ _OBJC_IVAR_$_HDHeartProfileExtension._uiTriggerObserver
+ _OBJC_METACLASS_$_HDHRBloodPressureDailyAnalyticsEvent
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalBPSampleObserver
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalControlServer
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalManager
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalNotificationIdentifier
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalNotificationInfo
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalNotificationManager
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalNotificationMeasurementInfo
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalNotificationSyncManager
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalPeriodicScheduler
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalSyncRequester
+ _OBJC_METACLASS_$_HDHRBloodPressureJournalTimeZoneObserver
+ _OBJC_METACLASS_$_HDHRHypertensionMeasurementAnalyzer
+ _OBJC_METACLASS_$_HDHRHypertensionNotificationAnalysisEvent
+ _OBJC_METACLASS_$_HDHRHypertensionNotificationDeliveryEvent
+ _OBJC_METACLASS_$_HDHRHypertensionNotificationManager
+ _OBJC_METACLASS_$_HDHRHypertensionNotificationsAnalysisScheduler
+ _OBJC_METACLASS_$_HDHRHypertensionNotificationsDailyAnalyticsEvent
+ _OBJC_METACLASS_$_HDHRHypertensionNotificationsRescindedAlertManager
+ _OBJC_METACLASS_$_HDHRHypertensionNotificationsSettingsResetter
+ _OBJC_METACLASS_$_HDHRIrregularRhythmNotificationsV2UpgradeManager
+ _OBJC_METACLASS_$_HKHRBloodPressureJournalStateSyncEntity
+ _OBJC_METACLASS_$_HKHRStateSyncBloodPressureJournalDelegate
+ _XPC_ACTIVITY_INTERVAL
+ _XPC_ACTIVITY_REPEATING
+ __BPJournalScheduleIntervalPredicateForOwnerID
+ __OBJC_$_CATEGORY_CLASS_METHODS_HKFeatureAvailabilityRequirementSet_$_BPJ
+ __OBJC_$_CATEGORY_CLASS_METHODS_HKNotificationInstruction_$_BloodPressureJournal
+ __OBJC_$_CATEGORY_HDAlarmEvent_$_BloodPressureJournal
+ __OBJC_$_CATEGORY_HDRestorableAlarm_$_BloodPressureJournal
+ __OBJC_$_CATEGORY_HKCountrySet_$_HypertensionNotifications
+ __OBJC_$_CATEGORY_HKFeatureAvailabilityRequirementSet_$_BPJ
+ __OBJC_$_CATEGORY_HKNotificationInstruction_$_BloodPressureJournal
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_HDAlarmEvent_$_BloodPressureJournal
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_HDRestorableAlarm_$_BloodPressureJournal
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_HKNotificationInstruction_$_BloodPressureJournal
+ __OBJC_$_CLASS_METHODS_HDFeatureAvailabilityManager(HDHRIrregularRhythmNotificationsV2FeatureAvailabilityManager|CardioFitness|BPJ)
+ __OBJC_$_CLASS_METHODS_HDHRBloodPressureJournalControlServer
+ __OBJC_$_CLASS_METHODS_HDHRBloodPressureJournalNotificationIdentifier
+ __OBJC_$_CLASS_METHODS_HDHRBloodPressureJournalNotificationManager
+ __OBJC_$_CLASS_METHODS_HDKeyValueDomain(HKHeartRhythm|HypertensionNotifications|AFibBurdenNotificationManagerAdherence|ElectrocardiogramRecording)
+ __OBJC_$_CLASS_METHODS_HKCountrySet(HypertensionNotifications|BloodPressureJournal|IrregularRhythmNotificationsV2|ElectrocardiogramV2Recording)
+ __OBJC_$_CLASS_METHODS_HKHRBloodPressureJournalStateSyncEntity
+ __OBJC_$_CLASS_METHODS_HKHRStateSyncBloodPressureJournalDelegate
+ __OBJC_$_CLASS_PROP_LIST_HDCloudSyncStateEntity
+ __OBJC_$_CLASS_PROP_LIST_HKHRBloodPressureJournalStateSyncEntity
+ __OBJC_$_CLASS_PROP_LIST_HKHRStateSyncBloodPressureJournalDelegate
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureDailyAnalyticsEvent
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalBPSampleObserver
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalControlServer
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalManager
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalNotificationIdentifier
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalNotificationInfo
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalNotificationManager
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalNotificationMeasurementInfo
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalNotificationSyncManager
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalPeriodicScheduler
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalSyncRequester
+ __OBJC_$_INSTANCE_METHODS_HDHRBloodPressureJournalTimeZoneObserver
+ __OBJC_$_INSTANCE_METHODS_HDHRHypertensionMeasurementAnalyzer
+ __OBJC_$_INSTANCE_METHODS_HDHRHypertensionNotificationAnalysisEvent
+ __OBJC_$_INSTANCE_METHODS_HDHRHypertensionNotificationDeliveryEvent
+ __OBJC_$_INSTANCE_METHODS_HDHRHypertensionNotificationManager
+ __OBJC_$_INSTANCE_METHODS_HDHRHypertensionNotificationsAnalysisScheduler
+ __OBJC_$_INSTANCE_METHODS_HDHRHypertensionNotificationsDailyAnalyticsEvent
+ __OBJC_$_INSTANCE_METHODS_HDHRHypertensionNotificationsRescindedAlertManager
+ __OBJC_$_INSTANCE_METHODS_HDHRHypertensionNotificationsSettingsResetter
+ __OBJC_$_INSTANCE_METHODS_HDHRIrregularRhythmNotificationsV2UpgradeManager
+ __OBJC_$_INSTANCE_METHODS_HDKeyValueDomain(HKHeartRhythm|HypertensionNotifications|AFibBurdenNotificationManagerAdherence|ElectrocardiogramRecording)
+ __OBJC_$_INSTANCE_METHODS_HDNotificationManager(HDHRAFibBurdenAnalyticsEventHealthAppNotificationsAuthorizedProvider|BloodPressureJournal)
+ __OBJC_$_INSTANCE_METHODS_HKHRBloodPressureJournalStateSyncEntity
+ __OBJC_$_INSTANCE_METHODS_HKHRStateSyncBloodPressureJournalDelegate
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureDailyAnalyticsEvent
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalBPSampleObserver
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalControlServer
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalManager
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalNotificationIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalNotificationInfo
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalNotificationManager
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalNotificationMeasurementInfo
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalNotificationSyncManager
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalPeriodicScheduler
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalSyncRequester
+ __OBJC_$_INSTANCE_VARIABLES_HDHRBloodPressureJournalTimeZoneObserver
+ __OBJC_$_INSTANCE_VARIABLES_HDHRHypertensionMeasurementAnalyzer
+ __OBJC_$_INSTANCE_VARIABLES_HDHRHypertensionNotificationAnalysisEvent
+ __OBJC_$_INSTANCE_VARIABLES_HDHRHypertensionNotificationDeliveryEvent
+ __OBJC_$_INSTANCE_VARIABLES_HDHRHypertensionNotificationManager
+ __OBJC_$_INSTANCE_VARIABLES_HDHRHypertensionNotificationsAnalysisScheduler
+ __OBJC_$_INSTANCE_VARIABLES_HDHRHypertensionNotificationsDailyAnalyticsEvent
+ __OBJC_$_INSTANCE_VARIABLES_HDHRHypertensionNotificationsRescindedAlertManager
+ __OBJC_$_INSTANCE_VARIABLES_HDHRHypertensionNotificationsSettingsResetter
+ __OBJC_$_INSTANCE_VARIABLES_HDHRIrregularRhythmNotificationsV2UpgradeManager
+ __OBJC_$_PROP_LIST_HDCloudSyncStateUpdaterDelegate
+ __OBJC_$_PROP_LIST_HDHRBloodPressureDailyAnalyticsEvent
+ __OBJC_$_PROP_LIST_HDHRBloodPressureJournalBPSampleObserver
+ __OBJC_$_PROP_LIST_HDHRBloodPressureJournalControlServer
+ __OBJC_$_PROP_LIST_HDHRBloodPressureJournalNotificationIdentifier
+ __OBJC_$_PROP_LIST_HDHRBloodPressureJournalNotificationInfo
+ __OBJC_$_PROP_LIST_HDHRBloodPressureJournalNotificationManager
+ __OBJC_$_PROP_LIST_HDHRBloodPressureJournalNotificationMeasurementInfo
+ __OBJC_$_PROP_LIST_HDHRBloodPressureJournalNotificationSyncManager
+ __OBJC_$_PROP_LIST_HDHRBloodPressureJournalPeriodicScheduler
+ __OBJC_$_PROP_LIST_HDHRBloodPressureJournalTimeZoneObserver
+ __OBJC_$_PROP_LIST_HDHRHypertensionNotificationAnalysisEvent
+ __OBJC_$_PROP_LIST_HDHRHypertensionNotificationDeliveryEvent
+ __OBJC_$_PROP_LIST_HDHRHypertensionNotificationManager
+ __OBJC_$_PROP_LIST_HDHRHypertensionNotificationsAnalysisScheduler
+ __OBJC_$_PROP_LIST_HDHRHypertensionNotificationsDailyAnalyticsEvent
+ __OBJC_$_PROP_LIST_HDHRHypertensionNotificationsRescindedAlertManager
+ __OBJC_$_PROP_LIST_HDHRHypertensionNotificationsSettingsResetter
+ __OBJC_$_PROP_LIST_HDHRIrregularRhythmNotificationsV2UpgradeManager
+ __OBJC_$_PROP_LIST_HKHRBloodPressureJournalStateSyncEntity
+ __OBJC_$_PROP_LIST_HKHRStateSyncBloodPressureJournalDelegate
+ __OBJC_$_PROTOCOL_CLASS_METHODS_HDCloudSyncStateEntity
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDCloudSyncStateUpdaterDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDHRBloodPressureJournalObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDNotificationSyncClientDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKHRBloodPressureJournalControlServerInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKMCPregnancyModelObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKMCPregnancyModelProvidingInterface
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKUnitTestingTaskServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDCloudSyncStateEntity
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDCloudSyncStateUpdaterDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDHRBloodPressureJournalObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDNotificationSyncClientDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKHRBloodPressureJournalControlServerInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKMCPregnancyModelObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKMCPregnancyModelProvidingInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKUnitTestingTaskServerInterface
+ __OBJC_$_PROTOCOL_REFS_HDCloudSyncStateEntity
+ __OBJC_$_PROTOCOL_REFS_HDCloudSyncStateUpdaterDelegate
+ __OBJC_$_PROTOCOL_REFS_HDHRBloodPressureJournalObserver
+ __OBJC_$_PROTOCOL_REFS_HDNotificationSyncClientDelegate
+ __OBJC_$_PROTOCOL_REFS_HKHRBloodPressureJournalControlServerInterface
+ __OBJC_$_PROTOCOL_REFS_HKMCPregnancyModelProvidingInterface
+ __OBJC_CLASS_PROTOCOLS_$_HDHRBloodPressureDailyAnalyticsEvent
+ __OBJC_CLASS_PROTOCOLS_$_HDHRBloodPressureJournalBPSampleObserver
+ __OBJC_CLASS_PROTOCOLS_$_HDHRBloodPressureJournalControlServer
+ __OBJC_CLASS_PROTOCOLS_$_HDHRBloodPressureJournalNotificationManager
+ __OBJC_CLASS_PROTOCOLS_$_HDHRBloodPressureJournalNotificationSyncManager
+ __OBJC_CLASS_PROTOCOLS_$_HDHRBloodPressureJournalPeriodicScheduler
+ __OBJC_CLASS_PROTOCOLS_$_HDHRHypertensionNotificationAnalysisEvent
+ __OBJC_CLASS_PROTOCOLS_$_HDHRHypertensionNotificationDeliveryEvent
+ __OBJC_CLASS_PROTOCOLS_$_HDHRHypertensionNotificationManager
+ __OBJC_CLASS_PROTOCOLS_$_HDHRHypertensionNotificationsAnalysisScheduler
+ __OBJC_CLASS_PROTOCOLS_$_HDHRHypertensionNotificationsDailyAnalyticsEvent
+ __OBJC_CLASS_PROTOCOLS_$_HDHRHypertensionNotificationsRescindedAlertManager
+ __OBJC_CLASS_PROTOCOLS_$_HDHRHypertensionNotificationsSettingsResetter
+ __OBJC_CLASS_PROTOCOLS_$_HDHRIrregularRhythmNotificationsV2UpgradeManager
+ __OBJC_CLASS_PROTOCOLS_$_HDKeyValueDomain(HKHeartRhythm|HypertensionNotifications|AFibBurdenNotificationManagerAdherence|ElectrocardiogramRecording)
+ __OBJC_CLASS_PROTOCOLS_$_HKHRBloodPressureJournalStateSyncEntity
+ __OBJC_CLASS_PROTOCOLS_$_HKHRStateSyncBloodPressureJournalDelegate
+ __OBJC_CLASS_RO_$_HDHRBloodPressureDailyAnalyticsEvent
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalBPSampleObserver
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalControlServer
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalManager
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalNotificationIdentifier
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalNotificationInfo
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalNotificationManager
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalNotificationMeasurementInfo
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalNotificationSyncManager
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalPeriodicScheduler
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalSyncRequester
+ __OBJC_CLASS_RO_$_HDHRBloodPressureJournalTimeZoneObserver
+ __OBJC_CLASS_RO_$_HDHRHypertensionMeasurementAnalyzer
+ __OBJC_CLASS_RO_$_HDHRHypertensionNotificationAnalysisEvent
+ __OBJC_CLASS_RO_$_HDHRHypertensionNotificationDeliveryEvent
+ __OBJC_CLASS_RO_$_HDHRHypertensionNotificationManager
+ __OBJC_CLASS_RO_$_HDHRHypertensionNotificationsAnalysisScheduler
+ __OBJC_CLASS_RO_$_HDHRHypertensionNotificationsDailyAnalyticsEvent
+ __OBJC_CLASS_RO_$_HDHRHypertensionNotificationsRescindedAlertManager
+ __OBJC_CLASS_RO_$_HDHRHypertensionNotificationsSettingsResetter
+ __OBJC_CLASS_RO_$_HDHRIrregularRhythmNotificationsV2UpgradeManager
+ __OBJC_CLASS_RO_$_HKHRBloodPressureJournalStateSyncEntity
+ __OBJC_CLASS_RO_$_HKHRStateSyncBloodPressureJournalDelegate
+ __OBJC_LABEL_PROTOCOL_$_HDCloudSyncStateEntity
+ __OBJC_LABEL_PROTOCOL_$_HDCloudSyncStateUpdaterDelegate
+ __OBJC_LABEL_PROTOCOL_$_HDHRBloodPressureJournalObserver
+ __OBJC_LABEL_PROTOCOL_$_HDNotificationSyncClientDelegate
+ __OBJC_LABEL_PROTOCOL_$_HKHRBloodPressureJournalControlServerInterface
+ __OBJC_LABEL_PROTOCOL_$_HKMCPregnancyModelObserver
+ __OBJC_LABEL_PROTOCOL_$_HKMCPregnancyModelProvidingInterface
+ __OBJC_LABEL_PROTOCOL_$_HKUnitTestingTaskServerInterface
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureDailyAnalyticsEvent
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalBPSampleObserver
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalControlServer
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalManager
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalNotificationIdentifier
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalNotificationInfo
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalNotificationManager
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalNotificationMeasurementInfo
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalNotificationSyncManager
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalPeriodicScheduler
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalSyncRequester
+ __OBJC_METACLASS_RO_$_HDHRBloodPressureJournalTimeZoneObserver
+ __OBJC_METACLASS_RO_$_HDHRHypertensionMeasurementAnalyzer
+ __OBJC_METACLASS_RO_$_HDHRHypertensionNotificationAnalysisEvent
+ __OBJC_METACLASS_RO_$_HDHRHypertensionNotificationDeliveryEvent
+ __OBJC_METACLASS_RO_$_HDHRHypertensionNotificationManager
+ __OBJC_METACLASS_RO_$_HDHRHypertensionNotificationsAnalysisScheduler
+ __OBJC_METACLASS_RO_$_HDHRHypertensionNotificationsDailyAnalyticsEvent
+ __OBJC_METACLASS_RO_$_HDHRHypertensionNotificationsRescindedAlertManager
+ __OBJC_METACLASS_RO_$_HDHRHypertensionNotificationsSettingsResetter
+ __OBJC_METACLASS_RO_$_HDHRIrregularRhythmNotificationsV2UpgradeManager
+ __OBJC_METACLASS_RO_$_HKHRBloodPressureJournalStateSyncEntity
+ __OBJC_METACLASS_RO_$_HKHRStateSyncBloodPressureJournalDelegate
+ __OBJC_PROTOCOL_$_HDCloudSyncStateEntity
+ __OBJC_PROTOCOL_$_HDCloudSyncStateUpdaterDelegate
+ __OBJC_PROTOCOL_$_HDHRBloodPressureJournalObserver
+ __OBJC_PROTOCOL_$_HDNotificationSyncClientDelegate
+ __OBJC_PROTOCOL_$_HKHRBloodPressureJournalControlServerInterface
+ __OBJC_PROTOCOL_$_HKMCPregnancyModelObserver
+ __OBJC_PROTOCOL_$_HKMCPregnancyModelProvidingInterface
+ __OBJC_PROTOCOL_$_HKUnitTestingTaskServerInterface
+ __OBJC_PROTOCOL_REFERENCE_$_HDHRBloodPressureJournalObserver
+ __OBJC_PROTOCOL_REFERENCE_$_HKMCPregnancyModelProvidingInterface
+ ___100-[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke
+ ___100-[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke.306
+ ___100-[HDHRBloodPressureJournalPeriodicScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke_2
+ ___100-[HDHRHypertensionNotificationsRescindedAlertManager featureStatusProviding:didUpdateFeatureStatus:]_block_invoke
+ ___105-[HDHRBloodPressureJournalManager insertBloodPressureJournals:isUserInitiated:error:onCommit:onRollback:]_block_invoke
+ ___105-[HDHRBloodPressureJournalManager insertBloodPressureJournals:isUserInitiated:error:onCommit:onRollback:]_block_invoke.346
+ ___105-[HDHRBloodPressureJournalManager insertBloodPressureJournals:isUserInitiated:error:onCommit:onRollback:]_block_invoke_2
+ ___105-[HDHRHypertensionNotificationsAnalysisScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke
+ ___105-[HDHRHypertensionNotificationsAnalysisScheduler _enqueueSchedulingOnMaintenanceOperationWithCompletion:]_block_invoke.319
+ ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke
+ ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke.372
+ ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke.372.cold.1
+ ___106-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveDueEvents:date:handledEventsHandler:]_block_invoke.372.cold.2
+ ___111-[HDHRBloodPressureJournalManager enumerateJournalsWithPredicate:limit:orderingTerms:error:enumerationHandler:]_block_invoke
+ ___112+[HDHRHeartCLogEntity _enumerateJournalsWithPredicate:limit:orderingTerms:transaction:error:enumerationHandler:]_block_invoke
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke.327
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke_2
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke_2.328
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke_3
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke_3.330
+ ___122+[HKHRStateSyncBloodPressureJournalDelegate _shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:]_block_invoke_4
+ ___122-[HDHRHypertensionNotificationsAnalysisScheduler _queue_performAnalysisIfNeededWithDatabaseTransactionContext:completion:]_block_invoke
+ ___124+[HDHRHeartCLogScheduleTimeIntervalEntity enumerateJournalScheduleIntervalWithOwnerID:transaction:error:enumerationHandler:]_block_invoke
+ ___124-[HDNotificationManager(BloodPressureJournal) getBloodPressureJournalDeliveredNotificationIdentifiersWithCompletionHandler:]_block_invoke
+ ___126-[HDHRIrregularRhythmNotificationsV2UpgradeManager performWorkForOperation:profile:databaseAccessibilityAssertion:completion:]_block_invoke
+ ___146-[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:databaseTransactionContext:error:]_block_invoke
+ ___146-[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:databaseTransactionContext:error:]_block_invoke_2
+ ___146-[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:databaseTransactionContext:error:]_block_invoke_2.cold.1
+ ___146-[HDHRHypertensionMeasurementAnalyzer _saveHypertensionEventSampleAndLastAnalysisDateAtomicallyWithDateInterval:databaseTransactionContext:error:]_block_invoke_2.cold.2
+ ___56+[HDHRHeartCLogEntity _insertJournal:transaction:error:]_block_invoke
+ ___59-[HDHRHypertensionNotificationManager samplesAdded:anchor:]_block_invoke
+ ___66-[HDHRBloodPressureJournalManager bloodPressureJournalsWithError:]_block_invoke
+ ___67-[HDHRBloodPressureJournalManager closeAllExpiredJournalsBy:error:]_block_invoke
+ ___68-[HDHRBloodPressureJournalSyncRequester requestStateSyncWithReason:]_block_invoke
+ ___68-[HDHRBloodPressureJournalSyncRequester requestStateSyncWithReason:]_block_invoke.cold.1
+ ___70+[HDHRHeartCLogEntity _journalFromRow:persistentID:transaction:error:]_block_invoke
+ ___71-[HDHRBloodPressureJournalControlServer remote_saveJournal:completion:]_block_invoke
+ ___71-[HDHRBloodPressureJournalControlServer remote_saveJournal:completion:]_block_invoke_2
+ ___72-[HDHRBloodPressureJournalBPSampleObserver _samplesFromCurrentDeviceIn:]_block_invoke
+ ___72-[HDHRBloodPressureJournalControlServer remote_closeJournal:completion:]_block_invoke
+ ___72-[HDHRBloodPressureJournalManager notifyObserversOfAddOrModifyJournals:]_block_invoke
+ ___73-[HDHRBloodPressureJournalNotificationManager initWithProfile:operation:]_block_invoke
+ ___73-[HDHRBloodPressureJournalNotificationManager initWithProfile:operation:]_block_invoke_2
+ ___73-[HDHRBloodPressureJournalNotificationManager initWithProfile:operation:]_block_invoke_3
+ ___73-[HDHRIrregularRhythmNotificationsV2UpgradeManager doWorkWithCompletion:]_block_invoke
+ ___73-[HDHRIrregularRhythmNotificationsV2UpgradeManager doWorkWithCompletion:]_block_invoke.327
+ ___73-[HDHRIrregularRhythmNotificationsV2UpgradeManager doWorkWithCompletion:]_block_invoke.327.cold.1
+ ___73-[HDHRIrregularRhythmNotificationsV2UpgradeManager doWorkWithCompletion:]_block_invoke.cold.1
+ ___75-[HDHRHypertensionMeasurementAnalyzer _measurementsWithDateInterval:error:]_block_invoke
+ ___75-[HDHRHypertensionMeasurementAnalyzer _measurementsWithDateInterval:error:]_block_invoke_2
+ ___76-[HDHRBloodPressureJournalManager bloodPressureJournalWithIdentifier:error:]_block_invoke
+ ___76-[HDHRBloodPressureJournalManager bloodPressureJournalsWithPredicate:error:]_block_invoke
+ ___77-[HDHRBloodPressureJournalManager latestActiveBloodPressureJournalWithError:]_block_invoke
+ ___77-[HDHRCarouselUITriggerObserver _postHypertensionNotificationWithCompletion:]_block_invoke
+ ___77-[HDHRCarouselUITriggerObserver _postHypertensionNotificationWithCompletion:]_block_invoke.cold.1
+ ___78+[HKHRStateSyncBloodPressureJournalDelegate _persistCloudState:profile:error:]_block_invoke
+ ___79-[HDHRBloodPressureJournalControlServer journalManager:didAddOrModifyJournals:]_block_invoke
+ ___79-[HDHRBloodPressureJournalControlServer journalManager:didAddOrModifyJournals:]_block_invoke.cold.1
+ ___79-[HDHeartProfileExtension _setupBloodPressureDailyAnalyticsManagerWithProfile:]_block_invoke
+ ___82+[HKHRBloodPressureJournalStateSyncEntity bloodPressureJournalFromCodableJournal:]_block_invoke
+ ___82+[HKHRBloodPressureJournalStateSyncEntity codableJournalFromBloodPressureJournal:]_block_invoke
+ ___82-[HDHRBloodPressureJournalManager bloodPressureJournalsWithLimit:ascending:error:]_block_invoke
+ ___83-[HDHRBloodPressureDailyAnalyticsEvent _calculateJournalStateAnalytics:dataSource:]_block_invoke
+ ___83-[HDHRBloodPressureDailyAnalyticsEvent _calculateJournalStateAnalytics:dataSource:]_block_invoke_2
+ ___83-[HDHRBloodPressureDailyAnalyticsEvent _calculateJournalStateAnalytics:dataSource:]_block_invoke_3
+ ___83-[HDHRBloodPressureDailyAnalyticsEvent _calculateJournalStateAnalytics:dataSource:]_block_invoke_4
+ ___83-[HDHRBloodPressureDailyAnalyticsEvent _numDaysSinceLastLoggedinBPJWithDataSource:]_block_invoke
+ ___84-[HDHRBloodPressureJournalNotificationManager _queue_alarm:didReceiveExpiredEvents:]_block_invoke
+ ___86-[HDHRBloodPressureJournalPeriodicScheduler database:protectedDataDidBecomeAvailable:]_block_invoke
+ ___89-[HDHRBloodPressureJournalBPSampleObserver _samplesInCurrentActiveJournalPeriodFor:from:]_block_invoke
+ ___89-[HDHRHypertensionNotificationManager _queue_addNotificationRequestForHypertensionEvent:]_block_invoke
+ ___89-[HDHRHypertensionNotificationManager _queue_addNotificationRequestForHypertensionEvent:]_block_invoke.cold.1
+ ___91+[HKHRStateSyncBloodPressureJournalDelegate _fetchLocalJournals:profile:transaction:error:]_block_invoke
+ ___91-[HDHRHypertensionNotificationsAnalysisScheduler database:protectedDataDidBecomeAvailable:]_block_invoke
+ ___96+[HDHRHeartCLogScheduleTimeIntervalEntity insertJournalScheduleInterval:ownerID:database:error:]_block_invoke
+ ___96-[HDHRHypertensionNotificationsAnalysisScheduler featureStatusProviding:didUpdateFeatureStatus:]_block_invoke
+ ___97-[HDHRHypertensionNotificationsRescindedAlertManager _presentNotificationWithTitle:message:type:]_block_invoke
+ ___97-[HDHRHypertensionNotificationsRescindedAlertManager _presentNotificationWithTitle:message:type:]_block_invoke.345
+ ___97-[HDHRHypertensionNotificationsRescindedAlertManager _presentNotificationWithTitle:message:type:]_block_invoke.345.cold.1
+ ___98+[HKNotificationInstruction(BloodPressureJournal) notificationIdentifiersFromCategoryIdentifiers:]_block_invoke
+ ___block_descriptor_32_e22_16?0"HDAlarmEvent"8l
+ ___block_descriptor_32_e26_16?0"HKQuantitySample"8l
+ ___block_descriptor_32_e34_B16?0"HKHRBloodPressureJournal"8l
+ ___block_descriptor_32_e39_16?0"HDCodableBloodPressureJournal"8l
+ ___block_descriptor_40_e18_16?0"NSString"8l
+ ___block_descriptor_40_e35_B24?0"HKSample"8"NSDictionary"16l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32r_e25_B32?0"HKObject"8q16^24lr32l8
+ ___block_descriptor_40_e8_32r_e38_B24?0"HKHRBloodPressureJournal"8^16lr32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e23_v32?0q8d16"NSError"24ls32l8
+ ___block_descriptor_40_e8_32s_e34_B16?0"HKHRBloodPressureJournal"8ls32l8
+ ___block_descriptor_40_e8_32s_e34_v16?0^{HDSQLiteStatementBinder=}8ls32l8
+ ___block_descriptor_40_e8_32s_e41_v32?0"HKHRBloodPressureJournal"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e46_v32?0"HDCodableBloodPressureJournal"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e58_B24?0"HKHRBloodPressureJournalScheduleTimeInterval"8^16ls32l8
+ ___block_descriptor_40_e8_32s_e61_v32?0"HKHRBloodPressureJournalScheduleTimeInterval"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e9_B16?0^8ls32l8
+ ___block_descriptor_48_e8_32bs_e38_B32?0"NSArray"8^{HDSQLiteRow=}16^24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e23_v32?0q8d16"NSError"24ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e41_v32?0"HKHRBloodPressureJournal"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e34_v16?0^{HDSQLiteStatementBinder=}8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e35_B24?0"HKSample"8"NSDictionary"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e44_v16?0"<HDHRBloodPressureJournalObserver>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e9_B16?0^8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e66_v32?0"HDCodableBloodPressureJournalScheduleTimeInterval"8Q16^B24ls32l8
+ ___block_descriptor_56_e8_32s40bs_e41_B40?0q8"NSArray"16^{HDSQLiteRow=}24^32ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e14_v16?0?<v?>8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
+ ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40r48r56r_e41_v32?0"HKHRBloodPressureJournal"8Q16^B24lr40l8s32l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48r56r_e41_v32?0"HKHRBloodPressureJournal"8Q16^B24ls32l8s40l8r48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e9_B16?0^8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48w_e20_v20?0B8"NSError"12lw48l8s32l8s40l8
+ ___block_descriptor_64_e8_32s40s48w_e5_v8?0ls32l8s40l8w48l8
+ ___block_descriptor_65_e8_32s40s48bs56bs_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs_e35_B24?0"HDDatabaseTransaction"8^16ls32l8s40l8s48l8s56l8
+ _bloodPressureSystolicDiastolicSampleUUIDsFromCodableObjectCollection
+ _correlationSampleUUIDsFromCodableObjectCollection
+ _kHDHRHypertensionNotificationsThreadIdentifier
+ _kHKHRHypertensionNotificationsCategoryIdentifier
+ _kHKHRHypertensionNotificationsRescindedCategoryIdentifier
+ _objc_msgSend$_IHAGatedDemographicsFieldsWithDataSource:
+ _objc_msgSend$_alarm:confirmDeliveryByRemovingEvent:
+ _objc_msgSend$_alarm:confirmDeliveryByRemovingEvents:
+ _objc_msgSend$_alarm:dueEventsToHandleFrom:date:
+ _objc_msgSend$_alarmTimeForDate:withScheduleTimeInterval:calendar:
+ _objc_msgSend$_bloodPressureSampleFrom:error:
+ _objc_msgSend$_calculateJournalEntryAnalytics:dataSource:
+ _objc_msgSend$_calculateJournalStateAnalytics:dataSource:
+ _objc_msgSend$_calculateMostRecentBPJCycleAnalytics:dataSource:
+ _objc_msgSend$_countOfLast30DaysWithHypertensiveMeasurementSamplesWithCurrentDate:calendar:
+ _objc_msgSend$_countOfSamplesWithType:dateInterval:
+ _objc_msgSend$_countOfSamplesWithType:dateInterval:additionalPredicate:
+ _objc_msgSend$_currentActiveJournal
+ _objc_msgSend$_dateIntervalForCalendarDays:fromDate:calendar:
+ _objc_msgSend$_daysSinceHTNLastEnabled:
+ _objc_msgSend$_daysSinceLastHypertensionNotificationToDate:withinDateInterval:calendar:
+ _objc_msgSend$_daysSinceMostRecentSampleWithType:toDate:calendar:additionalPredicate:error:
+ _objc_msgSend$_daysSinceOldestHypertensionNotificationToDate:withinDateInterval:calendar:
+ _objc_msgSend$_daysSinceOldestSampleWithType:toDate:calendar:additionalPredicate:error:
+ _objc_msgSend$_dnuAdditionalPayload
+ _objc_msgSend$_dnuNumDaysAnalyticsWithCurrentDate:calendar:
+ _objc_msgSend$_dnuNumDaysWatchWornAnalyticsWithCalendar:
+ _objc_msgSend$_dnuOnboardingAnalyticsWithDataSource:
+ _objc_msgSend$_dnuSampleCountsInPreviousCalendarDayWithCurrentDate:calendar:
+ _objc_msgSend$_enqueueSchedulingOnMaintenanceOperationWithCompletion:
+ _objc_msgSend$_enumerateJournalsWithPredicate:limit:orderingTerms:transaction:error:enumerationHandler:
+ _objc_msgSend$_featureStatusForFeatureIdentifier:dataSource:error:
+ _objc_msgSend$_fetchBloodPressureJournals
+ _objc_msgSend$_fetchBloodPressureSamplesWithPredicate:
+ _objc_msgSend$_fetchMostRecentBPJCycleWithBloodPressureJournals:
+ _objc_msgSend$_hasUserEverSetUpBPJ:
+ _objc_msgSend$_hk_urlForHypertensionEventType
+ _objc_msgSend$_identifiersForHoldInstructionsFrom:journal:
+ _objc_msgSend$_ihaAdditionalPayload
+ _objc_msgSend$_ihaBPJCountAnalyticsWithCurrentDate:calendar:
+ _objc_msgSend$_ihaDemographicsPayloadWithDataSource:
+ _objc_msgSend$_ihaNumDaysAnalyticsWithCurrentDate:calendar:
+ _objc_msgSend$_ihaOnboardingAnalyticsWithDataSource:
+ _objc_msgSend$_ihaSampleCountsAnalyticsWithCurrentDate:calendar:
+ _objc_msgSend$_insertJournal:transaction:error:
+ _objc_msgSend$_insertTimeIntervals:journalPrimaryKey:transaction:error:
+ _objc_msgSend$_isAFibHistoryEnabledWithDataSource:
+ _objc_msgSend$_isDueEventExpired:fromDate:
+ _objc_msgSend$_isEventOnHold:
+ _objc_msgSend$_isFeatureRescindedWithUsageEvaluation:
+ _objc_msgSend$_isFeatureUnavailableForNonRescindedReasonsWithUsageEvaluation:
+ _objc_msgSend$_isJournal:inNoticationPeriodFor:calendar:
+ _objc_msgSend$_isPregnancyModeEnabled
+ _objc_msgSend$_journalEntityProperties
+ _objc_msgSend$_journalFromRow:persistentID:transaction:error:
+ _objc_msgSend$_journalScheduleIntervalFromRow:
+ _objc_msgSend$_journalScheduleTimeIntervalEntityProperties
+ _objc_msgSend$_lastAnalysisWindowEndDateOrOnboardingDateWithFeatureStatus:error:
+ _objc_msgSend$_nextDayFor:calendar:
+ _objc_msgSend$_notificationInfoFor:startDate:calendar:schedulingUUID:error:
+ _objc_msgSend$_notificationInfoForLearnHypertensionRiskJournal:startDate:calendar:schedulingUUID:error:
+ _objc_msgSend$_notificationInfoForMonitorHypertensionJournal:startDate:calendar:schedulingUUID:error:
+ _objc_msgSend$_notificationSchedulingIsEnabled
+ _objc_msgSend$_notificationsEnabled
+ _objc_msgSend$_numDaysSinceLastAnalysisWithCurrentDate:calendar:
+ _objc_msgSend$_numDaysSinceLastLoggedinBPJWithDataSource:
+ _objc_msgSend$_observePregnancy
+ _objc_msgSend$_payloadForEventType:
+ _objc_msgSend$_presentHypertensionNotificationsReEnabledAlert
+ _objc_msgSend$_presentHypertensionNotificationsRescindedAlertForUsageEvaluation:
+ _objc_msgSend$_presentNotificationWithTitle:message:type:
+ _objc_msgSend$_queue_alarm:didReceiveDueEvents:date:handledEventsHandler:
+ _objc_msgSend$_queue_alarm:didReceiveExpiredEvents:
+ _objc_msgSend$_queue_presentRescindedOrReEnabledAlertIfNeededWithFeatureStatus:
+ _objc_msgSend$_queue_pullFeatureStatusAndPresentAlertIfNeeded
+ _objc_msgSend$_regenerateNotificationsIfNecessaryWithJournalSamples:
+ _objc_msgSend$_removeAllExpiredEvents
+ _objc_msgSend$_removeDeliveredNotificationsFromNotificationCenterForSamples:journal:
+ _objc_msgSend$_reportAnalyticsEventForCountryCode:eventType:errorCategory:errorDetail:
+ _objc_msgSend$_reportDeliveryAnalyticsEventForCountryCode:
+ _objc_msgSend$_reportErrorAnalyticsEventForCountryCode:errorCategory:errorDetail:
+ _objc_msgSend$_rescheduleNotificationandIsUserInitated:
+ _objc_msgSend$_rescindedAlertBodyForUsageEvaluation:
+ _objc_msgSend$_rescindedAlertTitleForUsageEvaluation:
+ _objc_msgSend$_rescindedAlertTypeForUsageEvaluation:
+ _objc_msgSend$_resetActivityInterval
+ _objc_msgSend$_samplesFromCurrentDeviceIn:
+ _objc_msgSend$_samplesInCurrentActiveJournalPeriodFor:from:
+ _objc_msgSend$_scheduleNotificationsWithStartDate:schedulingUUID:error:
+ _objc_msgSend$_scheduleRestorableAlarmEventsWith:forJournal:calendar:schedulingUUID:error:
+ _objc_msgSend$_setupBloodPressureDailyAnalyticsManagerWithProfile:
+ _objc_msgSend$_setupBloodPressureJournalManagerWithProfile:
+ _objc_msgSend$_setupBloodPressureJournalNotificationManagerWithProfile:
+ _objc_msgSend$_setupBloodPressureJournalNotificationSyncManagerWithProfile:
+ _objc_msgSend$_setupBloodPressureJournalSyncRequesterWithProfile:
+ _objc_msgSend$_setupBloodPressureJournalTimeZoneObserverWithProfile:
+ _objc_msgSend$_setupBloodPressureSampleObserverWithProfile:
+ _objc_msgSend$_setupHypertensionNotificationsWithProfile:
+ _objc_msgSend$_startObservingOnboardingChanges
+ _objc_msgSend$_stopObservingOnboardingChanges
+ _objc_msgSend$_stringFromNotificationReason:
+ _objc_msgSend$_unitTesting_callNotificationNotPostedHandlerIfSet
+ _objc_msgSend$_weeksSinceOnboardingWithDataSource:
+ _objc_msgSend$addAccessibilityAssertion:
+ _objc_msgSend$addBloodPressureJournal:
+ _objc_msgSend$addProtectedDataObserver:queue:
+ _objc_msgSend$allBloodPressureJournalNotificationCategoryIdentifiers
+ _objc_msgSend$analyzeMeasurements:forDateInterval:
+ _objc_msgSend$arrayWithObjects:
+ _objc_msgSend$bedTimeCount
+ _objc_msgSend$bedtimeAlarmCount
+ _objc_msgSend$bedtimeAlarmStartDate
+ _objc_msgSend$bedtimeTimeInterval
+ _objc_msgSend$bloodPressureJournalAlarmEventWithNotificationIdentifier:journalType:dueDate:isFollowUp:measurementInfo:
+ _objc_msgSend$bloodPressureJournalExpirationEventWithIdentifier:dueDate:
+ _objc_msgSend$bloodPressureJournalFeatureAvailabilityManagerWithProfile:
+ _objc_msgSend$bloodPressureJournalFeatureAvailabilityRequirementSet
+ _objc_msgSend$bloodPressureJournalFromCodableJournal:
+ _objc_msgSend$bloodPressureJournalManager
+ _objc_msgSend$bloodPressureJournalNotificationManager
+ _objc_msgSend$bloodPressureJournalNotificationSyncManager
+ _objc_msgSend$bloodPressureJournalSyncRequester
+ _objc_msgSend$bloodPressureJournalWithIdentifier:error:
+ _objc_msgSend$bloodPressureJournals
+ _objc_msgSend$bloodPressureJournalsClosed:
+ _objc_msgSend$bloodPressureJournalsCount
+ _objc_msgSend$bloodPressureJournalsWithError:
+ _objc_msgSend$bloodPressureJournalsWithLimit:ascending:error:
+ _objc_msgSend$bloodPressureJournalsWithPredicate:error:
+ _objc_msgSend$bloodPressureSamplesAdded:forJournal:
+ _objc_msgSend$bloodPressureType
+ _objc_msgSend$boolValueFromKeyValuePair:
+ _objc_msgSend$categoryForClassificationGuidelines:systolic:diastolic:
+ _objc_msgSend$categoryIdentifierFromAlarmEventIdentifier:
+ _objc_msgSend$categoryIdentifierFromJournalIdentifier:
+ _objc_msgSend$categorySampleWithType:value:startDate:endDate:
+ _objc_msgSend$chutney
+ _objc_msgSend$clientInterface
+ _objc_msgSend$client_notifyDidAddOrModifyBloodPressureJournals:
+ _objc_msgSend$closeAllExpiredJournalsBy:error:
+ _objc_msgSend$closedJournal
+ _objc_msgSend$codableJournalFromBloodPressureJournal:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$content
+ _objc_msgSend$contextForAccessibilityAssertion:
+ _objc_msgSend$copyForWritingProtectedData
+ _objc_msgSend$correlationSampleSyncEntityClass
+ _objc_msgSend$correlationTypeForIdentifier:
+ _objc_msgSend$correlations
+ _objc_msgSend$countryIsSupportedOnLocalDeviceForFeatureWithIdentifier:
+ _objc_msgSend$currentSyncIdentity
+ _objc_msgSend$dataCount
+ _objc_msgSend$dataTypeWithCode:
+ _objc_msgSend$dateByAddingComponents:toDate:options:
+ _objc_msgSend$dateForKey:
+ _objc_msgSend$datesWithSamples
+ _objc_msgSend$dayIndex
+ _objc_msgSend$dayWindowType
+ _objc_msgSend$decodedObjectOfClass:version:decodedObject:error:
+ _objc_msgSend$doWorkWithCompletion:
+ _objc_msgSend$dueDate
+ _objc_msgSend$entity
+ _objc_msgSend$enumerateJournalScheduleIntervalWithOwnerID:transaction:error:enumerationHandler:
+ _objc_msgSend$enumerateJournalsWithPredicate:limit:orderingTerms:error:enumerationHandler:
+ _objc_msgSend$enumerateJournalsWithPredicate:limit:orderingTerms:transaction:error:enumerationHandler:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$enumeratePersistentIDsAndProperties:error:enumerationHandler:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$eventIdentifier
+ _objc_msgSend$eventWithIdentifier:dueDate:eventOptions:
+ _objc_msgSend$featureFlagIsEnabled:
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$getBloodPressureJournalDeliveredNotificationIdentifiersWithCompletionHandler:
+ _objc_msgSend$getDeliveredNotificationsWithCompletionHandler:
+ _objc_msgSend$getPregnancyModelProvider
+ _objc_msgSend$hasBedtimeSamplesForDayIndex:
+ _objc_msgSend$hasEndDate
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasTimeZoneChange
+ _objc_msgSend$hasWakeupSamplesForDayIndex:
+ _objc_msgSend$hd_dataOriginProvenance
+ _objc_msgSend$hdhr_hypertensionNotificationsDeviceLocalDomainForProfile:
+ _objc_msgSend$hdhr_hypertensionNotificationsSyncedDomainForProfile:
+ _objc_msgSend$heartHealthProfileExtension
+ _objc_msgSend$hermit
+ _objc_msgSend$hk_UUIDWithData:
+ _objc_msgSend$hk_addEntriesFromNonNilDictionary:
+ _objc_msgSend$hk_addNonNilObject:
+ _objc_msgSend$hk_codableDateComponents
+ _objc_msgSend$hk_dataForUUIDBytes
+ _objc_msgSend$hk_dateComponentsForCalendarUnit:
+ _objc_msgSend$hk_dateComponentsWithCodableDateComponents:calendarUnits:
+ _objc_msgSend$hk_dateIntervalForDayFromDate:calendar:
+ _objc_msgSend$hk_isAfterOrEqualToDate:
+ _objc_msgSend$hk_isBeforeOrEqualToDate:
+ _objc_msgSend$hk_oneDay
+ _objc_msgSend$hkhrBPJ_requestForNotification:
+ _objc_msgSend$hkhr_bloodPressureJournalDefaults
+ _objc_msgSend$hkhr_hypertensionNotificationsDefaults
+ _objc_msgSend$hypertensionEventType
+ _objc_msgSend$hypertensiveMeasurementType
+ _objc_msgSend$identifierFromBPSample:journal:
+ _objc_msgSend$identifierString
+ _objc_msgSend$initWithAction:alarmEventIdentifier:
+ _objc_msgSend$initWithAction:categoryIdentifier:expirationDate:
+ _objc_msgSend$initWithAction:journalIdentifier:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$initWithChangesSyncRequest:contextSyncRequest:stateSyncRequest:medicalIDSyncRequest:summarySharingSyncRequest:
+ _objc_msgSend$initWithDaemon:
+ _objc_msgSend$initWithDate:value:
+ _objc_msgSend$initWithDayWindowType:scheduledTime:
+ _objc_msgSend$initWithDomain:key:sampleOriginKey:sampleType:syncEntityClass:timeWindow:loggingCategory:sampleUUIDsFunction:
+ _objc_msgSend$initWithEventSubmissionManager:
+ _objc_msgSend$initWithIdentifierString:
+ _objc_msgSend$initWithJournal:
+ _objc_msgSend$initWithJournalIdentifier:notificationDayIndex:journalWindowType:
+ _objc_msgSend$initWithKeyValueDomain:featureAvailabilityProvider:
+ _objc_msgSend$initWithMeasurementIndex:measurementCount:measurementWindowType:
+ _objc_msgSend$initWithName:
+ _objc_msgSend$initWithPregnancySampleProvider:
+ _objc_msgSend$initWithProfile:analysisWindowInterval:keyValueDomain:analyticsEventSubmissionManager:
+ _objc_msgSend$initWithProfile:clientIdentifier:queue:
+ _objc_msgSend$initWithProfile:dateInterval:additionalPayload:
+ _objc_msgSend$initWithProfile:featureAvailabilityExtension:loggingCategory:
+ _objc_msgSend$initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:
+ _objc_msgSend$initWithProfile:featureStatusProvider:keyValueDomain:analysisWindowInterval:analysisWindowGraceInterval:analysisCadenceInterval:analysisRetryInterval:pregnancyStateProvider:measurementAnalyzer:
+ _objc_msgSend$initWithProfile:featureStatusProvider:pairedSyncStateProvider:keyValueDomain:
+ _objc_msgSend$initWithProfile:featureStatusProvider:pregnancyStateProvider:measurementAnalyzer:
+ _objc_msgSend$initWithProfile:operation:
+ _objc_msgSend$initWithProfile:type:
+ _objc_msgSend$initWithProfile:userDefaults:
+ _objc_msgSend$initWithProfile:v1FeatureAvailabilityManager:v2FeatureAvailabilityManager:hypertensionNotificationsFeatureAvailabilityManager:analyticsSubmissionManager:
+ _objc_msgSend$initWithProfile:v1FeatureAvailabilityManager:v2FeatureAvailabilityManager:hypertensionNotificationsFeatureAvailabilityManager:analyticsSubmissionManager:protectedDataOperation:
+ _objc_msgSend$initWithUUID:startDate:endDate:timestamp:journalType:scheduleType:journalState:timeIntervals:
+ _objc_msgSend$initWithWakeupAlarmStartDate:wakeupAlarmCount:bedtimeAlarmStartDate:bedtimeAlarmCount:
+ _objc_msgSend$initWithWithDomain:dataKeys:
+ _objc_msgSend$insertBloodPressureJournal:isUserInitiated:error:onCommit:onRollback:
+ _objc_msgSend$insertBloodPressureJournal:profile:transaction:error:
+ _objc_msgSend$insertBloodPressureJournals:error:onCommit:onRollback:
+ _objc_msgSend$insertBloodPressureJournals:isUserInitiated:error:onCommit:onRollback:
+ _objc_msgSend$insertJournalScheduleInterval:ownerID:database:error:
+ _objc_msgSend$integerValueFromKeyValuePair:
+ _objc_msgSend$isAlarmEventWithIdentifiersOnHold:journalIdentifier:error:
+ _objc_msgSend$isComplete
+ _objc_msgSend$isFollowUp
+ _objc_msgSend$isImproveHealthAndActivityEnabled
+ _objc_msgSend$isPairedSyncCompleted
+ _objc_msgSend$journalEntryForSample:
+ _objc_msgSend$journalIdentifier
+ _objc_msgSend$journalIdentifierString
+ _objc_msgSend$journalManager:didAddOrModifyJournals:
+ _objc_msgSend$journalStartDayFor:
+ _objc_msgSend$journalState
+ _objc_msgSend$journalType
+ _objc_msgSend$key
+ _objc_msgSend$lastInsertRowID
+ _objc_msgSend$latestActiveBloodPressureJournalWithError:
+ _objc_msgSend$latestWashoutEndDateWithError:
+ _objc_msgSend$localAvailabilityForBloodPressureJournal
+ _objc_msgSend$localAvailabilityForHypertensionNotifications
+ _objc_msgSend$longLongValue
+ _objc_msgSend$longValue
+ _objc_msgSend$makeIHAGatedEventPayloadWithDataSource:error:
+ _objc_msgSend$makeUnrestrictedEventPayloadWithDataSource:error:
+ _objc_msgSend$measurementCount
+ _objc_msgSend$measurementIndex
+ _objc_msgSend$measurementInfo
+ _objc_msgSend$measurementWindowType
+ _objc_msgSend$measurementsRequiredToCompleteJournal
+ _objc_msgSend$millimeterOfMercuryUnit
+ _objc_msgSend$minute
+ _objc_msgSend$modificationDateForKey:
+ _objc_msgSend$notificationEndDateForIncompleteJournal:
+ _objc_msgSend$notificationForLearnHypertensionRiskWithIdentifier:dueDate:isFollowUp:measurementIndex:measurementCount:measurementWindowType:
+ _objc_msgSend$notificationHoldInstructionsWithError:
+ _objc_msgSend$notificationIdentifierFromCategoryIdentifier:
+ _objc_msgSend$notificationIdentifierString
+ _objc_msgSend$notificationIdentifiersFromCategoryIdentifiers:
+ _objc_msgSend$notificationToMonitorHypertensionWithIdentifier:dueDate:isFollowUp:
+ _objc_msgSend$notifyObserversOfAddOrModifyJournals:
+ _objc_msgSend$numberOfDaysBetweenStartDate:endDate:withCalendar:
+ _objc_msgSend$object
+ _objc_msgSend$objectsForType:
+ _objc_msgSend$oldestSampleWithType:profile:encodingOptions:predicate:error:
+ _objc_msgSend$onCommit:orRollback:
+ _objc_msgSend$onboardingNotAcknowledgedWithIdentifier:
+ _objc_msgSend$onboardingRecordIsPresentForFeatureWithIdentifier:
+ _objc_msgSend$performAnalysisWithStartDate:endDate:databaseTransactionContext:error:
+ _objc_msgSend$performWithTransactionContext:error:block:
+ _objc_msgSend$persistentID
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$predicateWithProperty:equalToValue:
+ _objc_msgSend$primaryProfile
+ _objc_msgSend$profileExtensionsConformingToProtocol:
+ _objc_msgSend$profileIdentifier
+ _objc_msgSend$quantitySampleSyncEntityClass
+ _objc_msgSend$quantitySamples
+ _objc_msgSend$registerObserver:
+ _objc_msgSend$registerObserver:isUserInitiated:
+ _objc_msgSend$remoteObjectProxyWithErrorHandler:
+ _objc_msgSend$remote_closeJournal:completion:
+ _objc_msgSend$removeAllEventsWithError:
+ _objc_msgSend$removeDeliveredNotificationsForSamples:journal:
+ _objc_msgSend$removeDeliveredNotificationsWithIdentifiers:
+ _objc_msgSend$removeEvents:error:
+ _objc_msgSend$request
+ _objc_msgSend$requestStateSyncWithReason:
+ _objc_msgSend$resetInterval
+ _objc_msgSend$sample
+ _objc_msgSend$scheduleEvents:error:
+ _objc_msgSend$scheduleNotificationsWithReason:error:
+ _objc_msgSend$scheduleType
+ _objc_msgSend$scheduledTime
+ _objc_msgSend$secondsFromGMT
+ _objc_msgSend$seedIsNotExpiredForFeatureWithIdentifier:
+ _objc_msgSend$sendNotificationInstruction:criteria:error:
+ _objc_msgSend$serverInterface
+ _objc_msgSend$setBedtimeAlarmCount:
+ _objc_msgSend$setBedtimeAlarmStartDate:
+ _objc_msgSend$setCacheScope:
+ _objc_msgSend$setCodableObject:version:profile:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setDay:
+ _objc_msgSend$setDayWindowType:
+ _objc_msgSend$setEndDate:
+ _objc_msgSend$setJournalState:
+ _objc_msgSend$setJournalType:
+ _objc_msgSend$setMinute:
+ _objc_msgSend$setScheduleType:
+ _objc_msgSend$setScheduledTime:
+ _objc_msgSend$setSortDescriptors:
+ _objc_msgSend$setStartDate:
+ _objc_msgSend$setTimeIntervals:
+ _objc_msgSend$setTimestamp:
+ _objc_msgSend$setUnitTest_analysisOperationEnqueued:
+ _objc_msgSend$setUnitTest_latestAnalysisStartDate:
+ _objc_msgSend$setWakeupAlarmCount:
+ _objc_msgSend$setWakeupAlarmStartDate:
+ _objc_msgSend$snoozeBloodPressureJournalNotificationWithIdentifier:journalType:userInfo:onDate:error:
+ _objc_msgSend$sortDescriptorWithKey:ascending:
+ _objc_msgSend$statistics
+ _objc_msgSend$submitAnalyticsEvent:forJournal:windowType:
+ _objc_msgSend$substringFromIndex:
+ _objc_msgSend$summaryFromSamples:journal:
+ _objc_msgSend$supportedSyncVersionRange
+ _objc_msgSend$syncIdentity
+ _objc_msgSend$syncIdentityManager
+ _objc_msgSend$systemTimeZone
+ _objc_msgSend$timeIntervals
+ _objc_msgSend$timeIntervalsCount
+ _objc_msgSend$timeZoneFromDefaults
+ _objc_msgSend$timestamp
+ _objc_msgSend$unitTest_featureStatusUpdateBlock
+ _objc_msgSend$unitTesting_notificationNotPostedHandler
+ _objc_msgSend$unitTesting_postNotificationWithRequestHandler
+ _objc_msgSend$unsatisfiedRequirementIdentifiersDescription
+ _objc_msgSend$updateDataWithStateStorage:configuration:profile:transaction:error:
+ _objc_msgSend$updateDataWithStateStore:delegate:profile:transaction:error:
+ _objc_msgSend$updateDefaultsTimeZone:
+ _objc_msgSend$updateNotificationSyncManagerWithClosedJournals:
+ _objc_msgSend$updateTimeZoneIfRequired
+ _objc_msgSend$uuid
+ _objc_msgSend$valueFromKeyValuePair:
+ _objc_msgSend$wakeUpCount
+ _objc_msgSend$wakeupAlarmCount
+ _objc_msgSend$wakeupAlarmStartDate
+ _objc_msgSend$wakeupTimeInterval
+ _objc_msgSend$weekOfYear
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _objc_setProperty_atomic
+ _xpc_dictionary_set_int64
- __OBJC_$_CATEGORY_CLASS_METHODS_HDKeyValueDomain_$_HKHeartRhythm
- __OBJC_$_CATEGORY_HKCountrySet_$_IrregularRhythmNotificationsV2
- __OBJC_$_CLASS_METHODS_HDFeatureAvailabilityManager(HDHRIrregularRhythmNotificationsV2FeatureAvailabilityManager|CardioFitness)
- __OBJC_$_CLASS_METHODS_HKCountrySet(IrregularRhythmNotificationsV2|ElectrocardiogramV2Recording)
- __OBJC_$_INSTANCE_METHODS_HDKeyValueDomain(HKHeartRhythm|AFibBurdenNotificationManagerAdherence|ElectrocardiogramRecording)
- __OBJC_CLASS_PROTOCOLS_$_HDKeyValueDomain(HKHeartRhythm|AFibBurdenNotificationManagerAdherence|ElectrocardiogramRecording)
CStrings:
+ "!!! [HDHRHypertensionMeasurementAnalyzer] Overriding analyzer result, should force hypertension: %@"
+ "!!! [HDHRHypertensionNotificationsAnalysisScheduler] Using overriden scheduler analysis cadence interval: %@"
+ "!!! [HDHRHypertensionNotificationsAnalysisScheduler] Using overriden scheduler analysis window grace interval: %@"
+ "!!! [HDHRHypertensionNotificationsAnalysisScheduler] Using overriden scheduler analysis window interval: %@"
+ "!!! [HDHRHypertensionNotificationsAnalysisScheduler] Using overriden scheduler retry interval: %@"
+ "%@-%@"
+ "%ld"
+ "%{public}@: Began observing changes to journal manager."
+ "%{public}@: Failed to fetch intervals for journal UUID: %{public}@ error: %{public}@"
+ "%{public}@: Notify client for didAddOrModifyJournals journal count %ld"
+ "%{public}@: Stopped observing changes to journal manager."
+ "%{public}@: There are no expired journals to close. "
+ "%{public}@: Unable to notify client for didAddOrModifyJournals: %{public}@"
+ "%{public}@: ignoring changes from didAddOrModifyJournals"
+ "(Unexpected classification)"
+ ","
+ "-[HDAlarmEvent(BloodPressureJournal) isFollowUp]"
+ "-[HDAlarmEvent(BloodPressureJournal) journalIdentifierString]"
+ "-[HDAlarmEvent(BloodPressureJournal) journalType]"
+ "-[HDAlarmEvent(BloodPressureJournal) notificationIdentifierString]"
+ "-[HDAlarmEvent(BloodPressureJournal) valueFromKeyValuePair:]"
+ ":"
+ "<%@: %p> {\n  wakeupAlarmStartDate: %@,\n  wakeupAlarmCount: %lu,\n  bedtimeAlarmStartDate: %@,\n  bedtimeAlarmCount: %lu\n}"
+ "@\"<HDHRPairedSyncStateProviding>\""
+ "@\"<HDHRPregnancyStateProviding>\""
+ "@\"<HKMCPregnancyModelProviding>\"16@0:8"
+ "@\"HDDaemon\""
+ "@\"HDFeatureAvailabilityManager\""
+ "@\"HDHRBloodPressureJournalBPSampleObserver\""
+ "@\"HDHRBloodPressureJournalManager\""
+ "@\"HDHRBloodPressureJournalNotificationManager\""
+ "@\"HDHRBloodPressureJournalNotificationSyncManager\""
+ "@\"HDHRBloodPressureJournalPeriodicScheduler\""
+ "@\"HDHRBloodPressureJournalSyncRequester\""
+ "@\"HDHRBloodPressureJournalTimeZoneObserver\""
+ "@\"HDHRCarouselUITriggerObserver\""
+ "@\"HDHRHypertensionMeasurementAnalyzer\""
+ "@\"HDHRHypertensionNotificationManager\""
+ "@\"HDHRHypertensionNotificationsAnalysisScheduler\""
+ "@\"HDHRHypertensionNotificationsDailyAnalyticsEvent\""
+ "@\"HDHRHypertensionNotificationsRescindedAlertManager\""
+ "@\"HDHRHypertensionNotificationsSettingsResetter\""
+ "@\"HDHRIrregularRhythmNotificationsV2UpgradeManager\""
+ "@\"HDNotificationSyncClient\""
+ "@\"HDStateSyncEntitySchema\"16@0:8"
+ "@\"HKHRBloodPressureJournalNotificationAnalyticsUtilities\""
+ "@\"HKObserverSet<HDHRBloodPressureJournalObserver>\""
+ "@\"HKQuantityType\""
+ "@\"NSDateInterval\""
+ "@\"NSTimeZone\""
+ "@\"NSUUID\""
+ "@16@?0@\"HDAlarmEvent\"8"
+ "@16@?0@\"HDCodableBloodPressureJournal\"8"
+ "@16@?0@\"HKQuantitySample\"8"
+ "@16@?0@\"NSString\"8"
+ "@24@0:8^{HDSQLiteRow=}16"
+ "@32@0:8q16@24"
+ "@36@0:8Q16B24^@28"
+ "@40@0:8@16q24q32"
+ "@40@0:8q16@24@32"
+ "@40@0:8q16q24q32"
+ "@48@0:8@16@24@32^@40"
+ "@48@0:8@16Q24@32Q40"
+ "@48@0:8@16d24@32@40"
+ "@48@0:8^{HDSQLiteRow=}16q24@32^@40"
+ "@52@0:8@16q24@32B40@44"
+ "@88@0:8@16@24@32d40d48d56d64@72@80"
+ "A0A8CBBD-8F56-46ED-A36B-446D452C0515"
+ "AfibOnboardedVersion"
+ "AnalysisCadenceIntervalOverride"
+ "AnalysisResultForceHypertensionOverride"
+ "AnalysisSchedulerRetryIntervalOverride"
+ "AnalysisWindowGraceIntervalOverride"
+ "AnalysisWindowIntervalOverride"
+ "Average blood pressure classification is nil for date interval: %@"
+ "B16@?0@\"HKHRBloodPressureJournal\"8"
+ "B16@?0^@8"
+ "B24@?0@\"HKHRBloodPressureJournal\"8^@16"
+ "B24@?0@\"HKHRBloodPressureJournalScheduleTimeInterval\"8^@16"
+ "B24@?0@\"HKSample\"8@\"NSDictionary\"16"
+ "B32@0:8q16^@24"
+ "B40@0:8@\"<HDSyncCodable>\"16@\"HDProfile\"24^@32"
+ "B40@0:8@16@24@32"
+ "B40@?0q8@\"NSArray\"16^{HDSQLiteRow=}24^@32"
+ "B48@0:8@\"<HDCloudSyncStateStore>\"16@\"HDProfile\"24@\"HDDatabaseTransaction\"32^@40"
+ "B48@0:8@\"HDCodableSyncState\"16@\"<HDSyncCodable>\"24@\"HDProfile\"32^@40"
+ "B48@0:8@16@24@32^@40"
+ "B48@0:8@16^@24@?32@?40"
+ "B48@0:8^@16@\"HDProfile\"24@\"HDDatabaseTransaction\"32^@40"
+ "B48@0:8^@16@24@32^@40"
+ "B48@0:8q16@24^@32@?40"
+ "B52@0:8@16B24^@28@?36@?44"
+ "B56@0:8@16@24@32@40^@48"
+ "B56@0:8@16q24@32@40^@48"
+ "B56@0:8@16q24@32^@40@?48"
+ "B64@0:8@16Q24@32@40^@48@?56"
+ "B64@0:8@16q24@32@40^@48@?56"
+ "BADB0622-1CC0-4CE0-BF07-1B79D4FC28BB"
+ "BPJ"
+ "BPJAlarmEventID-"
+ "BPJID-"
+ "BPJTypeForMostRecentCycle"
+ "Blood Pressure analytics classification: %@"
+ "Blood Pressure average of %@ samples within date interval: %@ is systolic: %@ and diastolic: %@"
+ "Blood Pressure journal is closed"
+ "Blood Pressure journal is expired and closed"
+ "Blood Pressure journal is saved"
+ "Blood Pressure samples added"
+ "Blood Pressure samples removed"
+ "BloodPressureJournal"
+ "BloodPressureJournalNotificationAlarmIdentifier"
+ "BloodPressureJournalNotificationExpirationAlarmIdentifier"
+ "BloodPressureJournalNotificationSnoozeAlarmIdentifier"
+ "Cannot upgrade V1 user to V2 as no associated feature country code exists"
+ "CloudSyncStateEntityDomainBloodPressureJournal"
+ "Could not get BPJs with error: %{public}@"
+ "Could not get average blood pressure for date interval: %@ with error: %{public}@"
+ "Could not get count of Blood Pressure sample types with error: %{public}@"
+ "Could not get count of HRV sample types with error: %{public}@"
+ "Could not get count of hours with bghr with error: %{public}@"
+ "Could not get days since most recent hypertension event with error: %{public}@"
+ "Could not get days since oldest hypertension event with error: %{public}@"
+ "Could not get last analysis window end date with error: %{public}@"
+ "Could not get number of days with adequate data with error: %{public}@"
+ "Could not get number of hours with bg hr samples with error: %{public}@"
+ "Could not insert journal with UUID %@"
+ "DROP TABLE IF EXISTS heart_blood_pressure_journal"
+ "DROP TABLE IF EXISTS heart_blood_pressure_journal_schedule_interval"
+ "Elevated"
+ "Failed to save hypertension event sample and last analyzed window end date"
+ "Failed to save hypertension event to HealthKit"
+ "Failure"
+ "HDCloudSyncStateEntity"
+ "HDCloudSyncStateUpdaterDelegate"
+ "HDHRBloodPressureDailyAnalyticsEvent"
+ "HDHRBloodPressureJournalBPSampleObserver"
+ "HDHRBloodPressureJournalControlServer"
+ "HDHRBloodPressureJournalManager"
+ "HDHRBloodPressureJournalNotificationIdentifier"
+ "HDHRBloodPressureJournalNotificationInfo"
+ "HDHRBloodPressureJournalNotificationManager"
+ "HDHRBloodPressureJournalNotificationMeasurementInfo"
+ "HDHRBloodPressureJournalNotificationSyncManager"
+ "HDHRBloodPressureJournalObserver"
+ "HDHRBloodPressureJournalPeriodicScheduler"
+ "HDHRBloodPressureJournalSyncRequester"
+ "HDHRBloodPressureJournalTimeZoneObserver"
+ "HDHRHypertensionMeasurementAnalyzer"
+ "HDHRHypertensionNotificationAnalysisEvent"
+ "HDHRHypertensionNotificationDeliveryEvent"
+ "HDHRHypertensionNotificationManager"
+ "HDHRHypertensionNotificationsAnalysisScheduler"
+ "HDHRHypertensionNotificationsDailyAnalyticsEvent"
+ "HDHRHypertensionNotificationsRescindedAlertManager"
+ "HDHRHypertensionNotificationsSettingsResetter"
+ "HDHRIrregularRhythmNotificationsV2UpgradeManager"
+ "HDNotificationSyncClientDelegate"
+ "HDRestorableAlarm+BloodPressureJournal.m"
+ "HKCountrySet+BloodPressureJournal.m"
+ "HKCountrySet+HypertensionNotifications.m"
+ "HKHRBloodPressureJournalControlServerInterface"
+ "HKHRBloodPressureJournalStateSyncEntity"
+ "HKHRStateSyncBloodPressureJournalDelegate"
+ "HKHRStateSyncBloodPressureJournalDelegate.m"
+ "HKMCPregnancyModelObserver"
+ "HKMCPregnancyModelProvidingInterface"
+ "HKUnitTestingTaskServerInterface"
+ "HYPERTENSION_NOTIFICATIONS_REENABLED_BODY"
+ "HYPERTENSION_NOTIFICATIONS_REENABLED_TITLE"
+ "HYPERTENSION_NOTIFICATIONS_REMOTELY_DISABLED_ALERT_BODY"
+ "HYPERTENSION_NOTIFICATIONS_REMOTELY_DISABLED_ALERT_TITLE"
+ "HYPERTENSION_NOTIFICATIONS_SEED_EXPIRED_ALERT_BODY"
+ "HYPERTENSION_NOTIFICATIONS_SEED_EXPIRED_ALERT_TITLE"
+ "HYPERTENSION_NOTIFICATIONS_UNSUPPORTED_REGION_ALERT_BODY"
+ "HYPERTENSION_NOTIFICATIONS_UNSUPPORTED_REGION_ALERT_TITLE"
+ "HYPERTENSION_NOTIFICATION_BODY"
+ "HYPERTENSION_NOTIFICATION_TITLE"
+ "High BP Stage 1"
+ "High BP Stage 2"
+ "HypertensionNotifications"
+ "HypertensionNotificationsDisabledNotificationShownDateKey"
+ "Hypertensive Crisis"
+ "IRNOnboardedVersion"
+ "Invalid Event Identifier '%@' called with '%s'"
+ "Invalid Key Value format '%@' called with '%s'"
+ "Invalid notificationIdentifier '%@' called with '%s'"
+ "JournalChangedBackground"
+ "JournalChangedUserInitiated"
+ "Last analysis window end date is nil"
+ "Localizable-Hermit"
+ "ManualRequest"
+ "Month"
+ "No Blood Pressure samples found for date interval: %@"
+ "No hypertension pattern detected"
+ "No journal exists with identifer %@"
+ "Normal"
+ "Not eligible for analysis with unsatisfied requirements: %@"
+ "Onboarding acknowledged date is missing."
+ "PeriodicUpdate"
+ "Q24@0:8@16"
+ "Q32@0:8@16@24"
+ "StateSyncBloodPressureDiastolicSampleOriginKey"
+ "StateSyncBloodPressureDiastolicSampleWindowKey"
+ "StateSyncBloodPressureSampleCorrelationsOriginKey"
+ "StateSyncBloodPressureSampleCorrelationsWindowKey"
+ "StateSyncBloodPressureSystolicSampleOriginKey"
+ "StateSyncBloodPressureSystolicSampleWindowKey"
+ "Success"
+ "T@\"<HDFeatureAvailabilityExtension>\",R,N,V_hypertensionNotificationsAvailabilityManager"
+ "T@\"HDHRBloodPressureJournalBPSampleObserver\",R,N,V_bloodPressureSampleObserver"
+ "T@\"HDHRBloodPressureJournalManager\",R,N,V_bloodPressureJournalManager"
+ "T@\"HDHRBloodPressureJournalNotificationManager\",R,N,V_bloodPressureJournalNotificationManager"
+ "T@\"HDHRBloodPressureJournalNotificationSyncManager\",R,N,V_bloodPressureJournalNotificationSyncManager"
+ "T@\"HDHRBloodPressureJournalPeriodicScheduler\",R,N,V_bloodPressureJournalPeriodicScheduler"
+ "T@\"HDHRBloodPressureJournalSyncRequester\",R,N,V_bloodPressureJournalSyncRequester"
+ "T@\"HDHRBloodPressureJournalTimeZoneObserver\",R,N,V_bloodPressureJournalTimeZoneObserver"
+ "T@\"HDNotificationSyncClient\",R,N,V_notificationSyncClient"
+ "T@\"HDPeriodicActivity\",R,N"
+ "T@\"HDPeriodicActivity\",R,V_periodicActivity"
+ "T@\"HDRestorableAlarm\",&,N,V_unitTesting_expirationRestorableAlarm"
+ "T@\"HDRestorableAlarm\",&,N,V_unitTesting_restorableAlarm"
+ "T@\"HDRestorableAlarm\",&,N,V_unitTesting_snoozeRestorableAlarm"
+ "T@\"HDStateSyncEntitySchema\",R,C,N"
+ "T@\"NSDate\",&,N,V_unitTesting_configuredDate"
+ "T@\"NSDate\",&,V_unitTest_latestAnalysisStartDate"
+ "T@\"NSDate\",C,N,V_bedtimeAlarmStartDate"
+ "T@\"NSDate\",C,N,V_wakeupAlarmStartDate"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_unitTesting_restorableAlarmQueue"
+ "T@\"NSTimeZone\",C,N,V_unitTesting_localTimeZone"
+ "T@\"NSUUID\",R,N,V_journalIdentifier"
+ "T@?,C,N,V_didRegenerateNotificationsHandler"
+ "T@?,C,N,V_didRequestNotificationsRemovalHandler"
+ "T@?,C,N,V_didTriggerSyncHandler"
+ "T@?,C,N,V_unitTest_featureStatusUpdateBlock"
+ "T@?,C,N,V_unitTesting_didRequestRetryOnFeatureStatusChangeHandler"
+ "T@?,C,N,V_unitTesting_notificationNotPostedHandler"
+ "T@?,C,N,V_unitTesting_postNotificationHandler"
+ "T@?,C,N,V_unitTesting_postNotificationWithRequestHandler"
+ "TB,N,V_unitTest_analysisOperationEnqueued"
+ "TB,N,V_unitTesting_forceEnableNotifications"
+ "TB,N,V_unitTesting_shouldIgnoreDeliveredAlarmEvents"
+ "TQ,N,V_bedtimeAlarmCount"
+ "TQ,N,V_wakeupAlarmCount"
+ "TimeZoneChanged"
+ "Tq,R,N,V_journalWindowType"
+ "Tq,R,N,V_measurementCount"
+ "Tq,R,N,V_measurementIndex"
+ "Tq,R,N,V_measurementWindowType"
+ "Tq,R,N,V_notificationDayIndex"
+ "T{?=ii},R,N"
+ "Unknown (%ld)"
+ "UserInfo does not contain measurement related info %@"
+ "UserInfo should be provided for LearnHypertensionRisk journal type"
+ "Week"
+ "Zero correlated Blood Pressure samples found for date interval: %@"
+ "[%@:%p (%@, %@)]"
+ "[%@] Decode %ld blood pressure journals for state sync"
+ "[%@] Persist %ld blood pressure journals for state sync"
+ "[%{public}@ Unable to aquire database assertion]"
+ "[%{public}@:%p] Failed to request sync for blood pressure journal with error: %{public}@"
+ "[%{public}@:%p] Successfully requested sync for blood pressure journal"
+ "[%{public}@] %{public}@"
+ "[%{public}@] %{public}@ error: %{public}@"
+ "[%{public}@] %{public}@ samples of types removed: %{public}@. anchor: %{public}@"
+ "[%{public}@] %{public}@ with error %@"
+ "[%{public}@] (Skipping reset) Failed to retrieve hypertension notifications earliest onboarding date with error %@"
+ "[%{public}@] (Skipping reset) Failed to retrieve hypertension notifications last analysis window end date with error %@"
+ "[%{public}@] (Skipping reset) Hypertension notifications key value settings are not set"
+ "[%{public}@] *** notification: %{public}@ categoryIdentifier  %{public}@"
+ "[%{public}@] About to post Hypertension notifications rescinded/reenabled notification"
+ "[%{public}@] Already onboarded to IRN2"
+ "[%{public}@] Analyzing %ld analysis window(s)"
+ "[%{public}@] Analyzing hypertension measurements with startDate: %@, endDate: %@"
+ "[%{public}@] Beginning IRN2 upgrade using Hypertension Notifications onboarding country: %{public}@"
+ "[%{public}@] Beginning IRN2 upgrade using IRN1 country: %{public}@"
+ "[%{public}@] Blood Pressure samples added. Number of samples added %lu"
+ "[%{public}@] Blood Pressure samples added. Regeneration success state  %{BOOL}d"
+ "[%{public}@] Blood Pressure samples added. Request sent to remove delivered notifications, requested notification identifier count %lu"
+ "[%{public}@] Cannot upgrade to IRN2 as not onboarded to Hypertension Notifications"
+ "[%{public}@] Cannot upgrade to IRN2 as not onboarded to IRN1"
+ "[%{public}@] Checking if feature is unavailable for non-rescinding reasons: featureFlag -> %{public}@, age gated -> %{public}@, disabled in privacy -> %{public}@, wrist detection disabled -> %{public}@, health app hidden -> %{public}@, store demo mode -> %{public}@, active remote device not present -> %{public}@, capability not supported -> %{public}@"
+ "[%{public}@] Checking if feature is unavailable for rescinding reasons: regionNotSupportedOnRemoteDevice -> %{public}@, regionNotSupportedOnLocalDevice -> %{public}@, expired -> %{public}@, disabled -> %{public}@"
+ "[%{public}@] Cleaned up hypertension notifications key value settings"
+ "[%{public}@] Completed schedule notifications with success state: %d"
+ "[%{public}@] Completed schedule notifications: %{BOOL}d"
+ "[%{public}@] Configuring periodic activity with a time interval: %@"
+ "[%{public}@] Could not get feature status with error %@"
+ "[%{public}@] Could not get latest washout end date with error %@"
+ "[%{public}@] Could not load last analysis date with error %@"
+ "[%{public}@] Could not make identifier for sample [%{public}@] and  journal [%{public}@]."
+ "[%{public}@] Daemon ready"
+ "[%{public}@] Daemon ready (not companion)"
+ "[%{public}@] Did not successfully insert journal"
+ "[%{public}@] Did successfully post notification for : %{public}@"
+ "[%{public}@] Error requesting notification: %{public}@"
+ "[%{public}@] Error saving IRN2 Upgrade: %{public}@"
+ "[%{public}@] Executing analysis operation with date range ([%{public}@] - [%{public}@]), with an analysis window timeinterval: [%{public}@], grace time interval: [%{public}@]"
+ "[%{public}@] Executing maintenance operation"
+ "[%{public}@] Failed to analyze hypertension measurements with startDate: %@, endDate: %@, error %@"
+ "[%{public}@] Failed to calculate journal end day. Got nil for journal End day."
+ "[%{public}@] Failed to confirm delivery by removing event for client identifier: %{public}@, error: %{public}@"
+ "[%{public}@] Failed to fetch active blood pressure journal with error: %{public}@"
+ "[%{public}@] Failed to fetch all blood pressure journals with error: %{public}@"
+ "[%{public}@] Failed to fetch latest active journal with error: %{public}@"
+ "[%{public}@] Failed to fetch latest active journal: %{public}@"
+ "[%{public}@] Failed to load feature status with error: %{public}@"
+ "[%{public}@] Failed to load hypertension measurements with error %@"
+ "[%{public}@] Failed to post a rescinded notification (could not load either title or message)"
+ "[%{public}@] Failed to post hypertension notification with error: %@"
+ "[%{public}@] Failed to post notification request for : %{public}@, error:%{public}@"
+ "[%{public}@] Failed to reset hypertension notifications last analysis window end date with error %@"
+ "[%{public}@] Failed to reset last shown date with error: %{public}@"
+ "[%{public}@] Failed to save last analyzed window end date with error %@"
+ "[%{public}@] Failed to save last shown date with error: %{public}@"
+ "[%{public}@] Failed to schedule expiration events with error: %{public}@"
+ "[%{public}@] Failed to schedule notifications error: %{public}@"
+ "[%{public}@] Failed to schedule notifications: %{public}@"
+ "[%{public}@] Failed to send `hold` message for blood pressure sample with event identifier  %{public}@  error: %{public}@"
+ "[%{public}@] Failed to send `hold` message for closed journal with identifier  %{public}@  error: %{public}@"
+ "[%{public}@] Feature status did change to: %{public}@"
+ "[%{public}@] Health App is hidden or deleted, will not post notification"
+ "[%{public}@] Hypertension notification could not load alert's last shown date with error: %{public}@"
+ "[%{public}@] Hypertension notifications are disabled in settings"
+ "[%{public}@] Hypertension notifications are not rescinded (last shown date: %{public}@)"
+ "[%{public}@] Hypertension notifications are rescinded (last shown date: %{public}@)"
+ "[%{public}@] Hypertension notifications are unavailable for non-rescinding reasons"
+ "[%{public}@] Ignoring event from other devices: %@"
+ "[%{public}@] Inserted journal with persistent ID: %{public}lld"
+ "[%{public}@] Invalid Journal type. Could not make identifier for Sample [%{public}@] and journal [%{public}@]."
+ "[%{public}@] Journal notification scheduling is disabled. Health app is hidden or not installed."
+ "[%{public}@] Last analysis window end data is missing, using onboarding acknowledged date %@"
+ "[%{public}@] No difference in secondsFromGMT."
+ "[%{public}@] Notification Sync Client didReceiveInstructionWithAction %{public}@"
+ "[%{public}@] Notification scheduling is not enabled."
+ "[%{public}@] Notifications are disabled. Removing alarmEvents."
+ "[%{public}@] Paired sync not complete"
+ "[%{public}@] Performing periodic activity"
+ "[%{public}@] Posting notification with request: %{public}@"
+ "[%{public}@] Received %{public}@ due events: %{public}@"
+ "[%{public}@] Received ExpiredEvents %{public}@ events: %{public}@"
+ "[%{public}@] Removed event: %{public}@"
+ "[%{public}@] Requested a chance to upgrade due to OnboardingCompletionData becoming available (error: %{public}@)"
+ "[%{public}@] Requested a chance to upgrade due to onboardingCompletion of Feature: %@ (error: %{public}@)"
+ "[%{public}@] Requested a chance to upgrade due to region availability changes of Feature: %@ (error: %{public}@)"
+ "[%{public}@] Rescheduling notifications. Journal changed: %{public}@"
+ "[%{public}@] Resetting periodic activity"
+ "[%{public}@] Samples do not belong to current active journal."
+ "[%{public}@] Scheduling Hypertension notifications re-enabled alert"
+ "[%{public}@] Scheduling Hypertension notifications rescinded alert"
+ "[%{public}@] Scheduling a notification"
+ "[%{public}@] Sending `hold` notification in response to journal closure, with categoryIdentifier=[%{public}@]"
+ "[%{public}@] Sending `hold` notification in response to sample addition, with categoryIdentifier=[%{public}@]"
+ "[%{public}@] Set %ld blood pressure journals in cloud state for state sync"
+ "[%{public}@] Setting next analysis date to %@: %@"
+ "[%{public}@] Stale event. Removing alarmEvent: %{public}@"
+ "[%{public}@] Sucessfully posted hypertension notification"
+ "[%{public}@] There is no current active journal."
+ "[%{public}@] Time interval since last window end date is less than analysis window time interval + grace period"
+ "[%{public}@] TimeZones are equal."
+ "[%{public}@] Unable to insert journals due to error: %{public}@"
+ "[%{public}@] Unable to take an accessibility assertion: %{public}@"
+ "[%{public}@] Unexpected activity received; not setting activity criteria."
+ "[%{public}@] [UUID: %{public}@] _notificationInfoFor: Computing notification info for journal type: %ld, startDate: %{public}@"
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForLearnHypertensionRiskJournal: Computing notification info for LearnHypertensionRisk journal"
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForLearnHypertensionRiskJournal: Failed to fetch blood pressure samples with error: %{public}@"
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForLearnHypertensionRiskJournal: Found %ld blood pressure samples since journal start of day:%@"
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForLearnHypertensionRiskJournal: Journal is complete - no notifications needed"
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForLearnHypertensionRiskJournal: Journal not complete - wakeup count: %ld, bedtime count: %ld, required: %ld"
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForMonitorHypertensionJournal: Failed to calculate notification end date. Got nil for Notification End date."
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForMonitorHypertensionJournal: Failed to fetch blood pressure samples with error: %{public}@"
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForMonitorHypertensionJournal: Found %ld blood pressure samples from:%@"
+ "[%{public}@] [UUID: %{public}@] _notificationInfoForMonitorHypertensionJournal: Notification start date: %{public}@, end date: %{public}@ Calculated %ld remaining notifications"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: Active Journal Notification Period is complete - returning early"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: Active Journal is complete (notification info is nil) - returning early"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: Computed notification info successfully: %{public}@"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: Failed to compute notification info error: %{public}@"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: Failed to fetch latest active journal with error: %{public}@"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: Failed to remove existing alarm events with error: %{public}@"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: Failed to schedule restorable alarms with error: %{public}@"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: Found active journal: UUID=%{public}@, type=%ld, state=%ld, startDate=%{public}@"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: No active journal found to schedule notifications - removing alarms"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: Notification scheduling is not enabled - returning early"
+ "[%{public}@] [UUID: %{public}@] _scheduleNotificationsWithStartDate: started - date: %{public}@"
+ "[%{public}@] [UUID: %{public}@] _scheduleRestorableAlarmEventsWith events count:(%lu) [WAKEUP: alarm count:(%lu) starting from index:(%lu)] [BEDTIME: alarm count:(%lu) starting from index:(%lu)]"
+ "[%{public}@] [UUID: %{public}@] performOperation started - notificationStartDate: %{public}@"
+ "[%{public}@] [scheduleNotificationsWithReason called with reason: %{public}@"
+ "[%{public}@] _isJournal:inNoticationPeriodFor: Checking notification period for journal state: %ld, date: %{public}@"
+ "[%{public}@] _isJournal:inNoticationPeriodFor: Failed to calculate notification end date. Got nil for Notification End date."
+ "[%{public}@] _isJournal:inNoticationPeriodFor: Journal is closed - not in notification period"
+ "[%{public}@] _isJournal:inNoticationPeriodFor: Notification period check - endDate: %{public}@, isInPeriod: %{public}@"
+ "[%{public}@] could not remove expiration events with error: %{public}@"
+ "[%{public}@] notificationIdentifiers being removed: %{public}@"
+ "[%{public}@] samplesAdded: %@"
+ "[%{public}@] state sync result '%{public}@' for %{public}@"
+ "[%{public}@] timeZoneDidChange "
+ "[%{public}@]: Could not fetch notification hold instructions Error: %{public}@ "
+ "[%{public}@]: configuring periodic activity %{public}@"
+ "[%{public}@]: isAlarmEventWithIdentifiersOnHold returned error=[%{public}@],treating as not on hold"
+ "[%{public}@]: performing periodic activity %{public}@"
+ "[%{public}@]: periodic activity %{public}@ - protectedData not available - skipping trigger on healthd launch"
+ "[%{public}@]: periodic activity %{public}@ is not an expected activity, not configuring"
+ "[%{public}@]: periodic activity %{public}@ is not the expected activity, not performing"
+ "[%{public}@]: unable to take accessibility assertion: %{public}@"
+ "[HDHRHypertensionNotificationsAnalysisScheduler] Overriden scheduler analysis cadence interval is %@, which is equal or less than zero, returning default value"
+ "[HDHRHypertensionNotificationsAnalysisScheduler] Overriden scheduler analysis window grace interval is %@, which is equal or less than zero, returning default value"
+ "[HDHRHypertensionNotificationsAnalysisScheduler] Overriden scheduler analysis window interval is %@, which is equal or less than zero, returning default value"
+ "[HDHRHypertensionNotificationsAnalysisScheduler] Using scheduler retry interval: %@"
+ "[cloudState isKindOfClass:HDCodableBloodPressureJournalState.class]"
+ "[codableCloudState isKindOfClass:HDCodableBloodPressureJournalState.class]"
+ "[localState isKindOfClass:HDCodableBloodPressureJournalState.class]"
+ "[mergeState isKindOfClass:HDCodableBloodPressureJournalState.class]"
+ "_"
+ "_IHAGatedDemographicsFieldsWithDataSource:"
+ "_additionalPayload"
+ "_alarm:confirmDeliveryByRemovingEvent:"
+ "_alarm:confirmDeliveryByRemovingEvents:"
+ "_alarm:dueEventsToHandleFrom:date:"
+ "_alarmTimeForDate:withScheduleTimeInterval:calendar:"
+ "_analysisCadenceInterval"
+ "_analysisRetryInterval"
+ "_analysisWindowGraceInterval"
+ "_analysisWindowInterval"
+ "_bedtimeAlarmCount"
+ "_bedtimeAlarmStartDate"
+ "_bloodPressureDailyEventManager"
+ "_bloodPressureJournalBackgroundFeatureDeliveryManager"
+ "_bloodPressureJournalFeatureAvailabilityManager"
+ "_bloodPressureJournalManager"
+ "_bloodPressureJournalNotificationManager"
+ "_bloodPressureJournalNotificationSyncManager"
+ "_bloodPressureJournalPeriodicScheduler"
+ "_bloodPressureJournalSyncRequester"
+ "_bloodPressureJournalTimeZoneObserver"
+ "_bloodPressureSampleFrom:error:"
+ "_bloodPressureSampleObserver"
+ "_calculateJournalEntryAnalytics:dataSource:"
+ "_calculateJournalStateAnalytics:dataSource:"
+ "_calculateMostRecentBPJCycleAnalytics:dataSource:"
+ "_countOfLast30DaysWithHypertensiveMeasurementSamplesWithCurrentDate:calendar:"
+ "_countOfSamplesWithType:dateInterval:"
+ "_countOfSamplesWithType:dateInterval:additionalPredicate:"
+ "_currentActiveJournal"
+ "_daemon"
+ "_dateInterval"
+ "_dateIntervalForCalendarDays:fromDate:calendar:"
+ "_daysSinceHTNLastEnabled:"
+ "_daysSinceLastHypertensionNotificationToDate:withinDateInterval:calendar:"
+ "_daysSinceMostRecentSampleWithType:toDate:calendar:additionalPredicate:error:"
+ "_daysSinceOldestHypertensionNotificationToDate:withinDateInterval:calendar:"
+ "_daysSinceOldestSampleWithType:toDate:calendar:additionalPredicate:error:"
+ "_didRegenerateNotificationsHandler"
+ "_didRequestNotificationsRemovalHandler"
+ "_didTriggerSyncHandler"
+ "_dnuAdditionalPayload"
+ "_dnuNumDaysAnalyticsWithCurrentDate:calendar:"
+ "_dnuNumDaysWatchWornAnalyticsWithCalendar:"
+ "_dnuOnboardingAnalyticsWithDataSource:"
+ "_dnuSampleCountsInPreviousCalendarDayWithCurrentDate:calendar:"
+ "_enqueueSchedulingOnMaintenanceOperationWithCompletion:"
+ "_enumerateJournalsWithPredicate:limit:orderingTerms:transaction:error:enumerationHandler:"
+ "_expirationRestorableAlarm"
+ "_featureStatusForFeatureIdentifier:dataSource:error:"
+ "_fetchBloodPressureJournals"
+ "_fetchBloodPressureSamplesWithPredicate:"
+ "_fetchMostRecentBPJCycleWithBloodPressureJournals:"
+ "_hasUserEverSetUpBPJ:"
+ "_hk_urlForHypertensionEventType"
+ "_htnDailyAnalyticsEvent"
+ "_hypertensionMeasurementAnalyzer"
+ "_hypertensionNotificationManager"
+ "_hypertensionNotificationsAnalysisScheduler"
+ "_hypertensionNotificationsAvailabilityManager"
+ "_hypertensionNotificationsBackgroundFeatureDeliveryManager"
+ "_hypertensionNotificationsRescindedAlertManager"
+ "_hypertensionNotificationsSettingsResetter"
+ "_identifierString"
+ "_identifiersForHoldInstructionsFrom:journal:"
+ "_ihaAdditionalPayload"
+ "_ihaBPJCountAnalyticsWithCurrentDate:calendar:"
+ "_ihaDemographicsPayloadWithDataSource:"
+ "_ihaNumDaysAnalyticsWithCurrentDate:calendar:"
+ "_ihaOnboardingAnalyticsWithDataSource:"
+ "_ihaSampleCountsAnalyticsWithCurrentDate:calendar:"
+ "_insertJournal:transaction:error:"
+ "_insertTimeIntervals:journalPrimaryKey:transaction:error:"
+ "_irregularRhythmNotificationsV2UpgradeManager"
+ "_isAFibHistoryEnabledWithDataSource:"
+ "_isDueEventExpired:fromDate:"
+ "_isEventOnHold:"
+ "_isFeatureEnabledForFeatureIdentifier:dataSource:featureAvailabilityContext:"
+ "_isFeatureRescindedWithUsageEvaluation:"
+ "_isFeatureUnavailableForNonRescindedReasonsWithUsageEvaluation:"
+ "_isJournal:inNoticationPeriodFor:calendar:"
+ "_isPregnancyModeEnabled"
+ "_journalEntityProperties"
+ "_journalFromRow:persistentID:transaction:error:"
+ "_journalIdentifier"
+ "_journalScheduleIntervalFromRow:"
+ "_journalScheduleTimeIntervalEntityProperties"
+ "_journalWindowType"
+ "_lastAnalysisWindowEndDateOrOnboardingDateWithFeatureStatus:error:"
+ "_measurementCount"
+ "_measurementIndex"
+ "_measurementWindowType"
+ "_measurementsType"
+ "_nextDayFor:calendar:"
+ "_notificationAnalyticUtilities"
+ "_notificationDayIndex"
+ "_notificationInfoFor:startDate:calendar:schedulingUUID:error:"
+ "_notificationInfoForLearnHypertensionRiskJournal:startDate:calendar:schedulingUUID:error:"
+ "_notificationInfoForMonitorHypertensionJournal:startDate:calendar:schedulingUUID:error:"
+ "_notificationSchedulingIsEnabled"
+ "_notificationSyncClient"
+ "_notificationsEnabled"
+ "_numDaysSinceLastAnalysisWithCurrentDate:calendar:"
+ "_numDaysSinceLastLoggedinBPJWithDataSource:"
+ "_observePregnancy"
+ "_pairedSyncStateProvider"
+ "_payloadForEventType:"
+ "_postHypertensionNotificationWithCompletion:"
+ "_pregnancyState"
+ "_pregnancyStateProvider"
+ "_presentHypertensionNotificationsReEnabledAlert"
+ "_presentHypertensionNotificationsRescindedAlertForUsageEvaluation:"
+ "_presentNotificationWithTitle:message:type:"
+ "_queue_alarm:didReceiveDueEvents:date:handledEventsHandler:"
+ "_queue_alarm:didReceiveExpiredEvents:"
+ "_queue_presentRescindedOrReEnabledAlertIfNeededWithFeatureStatus:"
+ "_queue_pullFeatureStatusAndPresentAlertIfNeeded"
+ "_regenerateNotificationsIfNecessaryWithJournalSamples:"
+ "_removeAllExpiredEvents"
+ "_removeDeliveredNotificationsFromNotificationCenterForSamples:journal:"
+ "_reportAnalyticsEventForCountryCode:eventType:errorCategory:errorDetail:"
+ "_reportDeliveryAnalyticsEventForCountryCode:"
+ "_reportErrorAnalyticsEventForCountryCode:errorCategory:errorDetail:"
+ "_rescheduleNotificationandIsUserInitated:"
+ "_rescindedAlertBodyForUsageEvaluation:"
+ "_rescindedAlertTitleForUsageEvaluation:"
+ "_rescindedAlertTypeForUsageEvaluation:"
+ "_resetActivityInterval"
+ "_restorableAlarm"
+ "_samplesFromCurrentDeviceIn:"
+ "_samplesInCurrentActiveJournalPeriodFor:from:"
+ "_scheduleNotificationsWithError:"
+ "_scheduleNotificationsWithStartDate:error:"
+ "_scheduleNotificationsWithStartDate:schedulingUUID:error:"
+ "_scheduleRestorableAlarmEventsWith:forJournal:calendar:schedulingUUID:error:"
+ "_schedulingQueue"
+ "_setupBloodPressureDailyAnalyticsManagerWithProfile:"
+ "_setupBloodPressureJournalManagerWithProfile:"
+ "_setupBloodPressureJournalNotificationManagerWithProfile:"
+ "_setupBloodPressureJournalNotificationSyncManagerWithProfile:"
+ "_setupBloodPressureJournalSyncRequesterWithProfile:"
+ "_setupBloodPressureJournalTimeZoneObserverWithProfile:"
+ "_setupBloodPressureSampleObserverWithProfile:"
+ "_setupHypertensionNotificationsWithProfile:"
+ "_shouldObserveChanges"
+ "_snoozeRestorableAlarm"
+ "_startObservingOnboardingChanges"
+ "_stopObservingOnboardingChanges"
+ "_stringFromNotificationReason:"
+ "_type"
+ "_uiTriggerObserver"
+ "_unitTest_analysisOperationEnqueued"
+ "_unitTest_featureStatusUpdateBlock"
+ "_unitTest_latestAnalysisStartDate"
+ "_unitTesting_callNotificationNotPostedHandlerIfSet"
+ "_unitTesting_configuredDate"
+ "_unitTesting_didRequestRetryOnFeatureStatusChangeHandler"
+ "_unitTesting_expirationRestorableAlarm"
+ "_unitTesting_forceEnableNotifications"
+ "_unitTesting_localTimeZone"
+ "_unitTesting_notificationNotPostedHandler"
+ "_unitTesting_postNotificationWithRequestHandler"
+ "_unitTesting_restorableAlarm"
+ "_unitTesting_restorableAlarmQueue"
+ "_unitTesting_shouldIgnoreDeliveredAlarmEvents"
+ "_unitTesting_snoozeRestorableAlarm"
+ "_wakeupAlarmCount"
+ "_wakeupAlarmStartDate"
+ "_weeksSinceOnboardingWithDataSource:"
+ "activity"
+ "addAccessibilityAssertion:"
+ "addBloodPressureJournal:"
+ "addProtectedDataObserver:queue:"
+ "alert_status"
+ "allBloodPressureJournalNotificationCategoryIdentifiers"
+ "analyzeMeasurements:forDateInterval:"
+ "arrayWithObjects:"
+ "bedTimeCount"
+ "bedtimeAlarmCount"
+ "bedtimeAlarmStartDate"
+ "bedtimeTimeInterval"
+ "bloodPressureJournalAlarmEventWithNotificationIdentifier:journalType:dueDate:isFollowUp:measurementInfo:"
+ "bloodPressureJournalExpirationEventWithIdentifier:dueDate:"
+ "bloodPressureJournalFeatureAvailabilityManagerWithProfile:"
+ "bloodPressureJournalFeatureAvailabilityRequirementSet"
+ "bloodPressureJournalFromCodableJournal:"
+ "bloodPressureJournalManager"
+ "bloodPressureJournalNotificationManager"
+ "bloodPressureJournalNotificationSyncManager"
+ "bloodPressureJournalPeriodicScheduler"
+ "bloodPressureJournalSyncRequester"
+ "bloodPressureJournalTimeZoneObserver"
+ "bloodPressureJournalWithIdentifier:error:"
+ "bloodPressureJournals"
+ "bloodPressureJournalsClosed:"
+ "bloodPressureJournalsCount"
+ "bloodPressureJournalsWithError:"
+ "bloodPressureJournalsWithLimit:ascending:error:"
+ "bloodPressureJournalsWithPredicate:error:"
+ "bloodPressureSampleObserver"
+ "bloodPressureSamplesAdded:forJournal:"
+ "bloodPressureType"
+ "boolValueFromKeyValuePair:"
+ "categoryForClassificationGuidelines:systolic:diastolic:"
+ "categoryIdentifierFromAlarmEventIdentifier:"
+ "categoryIdentifierFromJournalIdentifier:"
+ "categorySampleWithType:value:startDate:endDate:"
+ "chutney"
+ "clientInterface"
+ "client_notifyDidAddOrModifyBloodPressureJournals:"
+ "closeAllExpiredJournalsBy:error:"
+ "closedJournal"
+ "codableJournalFromBloodPressureJournal:"
+ "com.apple.health.bp.daily"
+ "com.apple.health.htn.notificationinteractions"
+ "com.apple.healthd.bloodPressureJournal.scheduler"
+ "com.apple.healthd.heart.hypertension-measurement-analysis"
+ "com.apple.hid.htn.notification"
+ "com.apple.private.health.HypertensionMeasurementsAnalyzerErrorDomain"
+ "componentsSeparatedByString:"
+ "content"
+ "contextForAccessibilityAssertion:"
+ "copyForWritingProtectedData"
+ "correlationSampleSyncEntityClass"
+ "correlationTypeForIdentifier:"
+ "correlations"
+ "countHTNotificationsUntilMostRecentBPJStarted"
+ "countryCodeHTN"
+ "countryIsSupportedOnLocalDeviceForFeatureWithIdentifier:"
+ "countryNotSupported"
+ "currentSyncIdentity"
+ "dataCount"
+ "dataTypeWithCode:"
+ "dateByAddingComponents:toDate:options:"
+ "dateForKey:"
+ "datesWithSamples"
+ "dayIndex"
+ "dayWindowType"
+ "daysSinceNotificationsLastEnabled"
+ "decodedObjectOfClass:version:decodedObject:error:"
+ "delivered"
+ "deviceNotSupported"
+ "didCompleteMonthBPJInMostRecentCycle"
+ "didCompleteWeekBPJInMostRecentCycle"
+ "didRegenerateNotificationsHandler"
+ "didRequestNotificationsRemovalHandler"
+ "didTriggerSyncHandler"
+ "differenceInDaysBetweenFirstHTNotificationAndBPJStarted"
+ "differenceInDaysBetweenMostRecentHTNotificationAndBPJStarted"
+ "doWorkWithCompletion:"
+ "dueDate"
+ "entity"
+ "enumerateJournalScheduleIntervalWithOwnerID:transaction:error:enumerationHandler:"
+ "enumerateJournalsWithPredicate:limit:orderingTerms:error:enumerationHandler:"
+ "enumerateJournalsWithPredicate:limit:orderingTerms:transaction:error:enumerationHandler:"
+ "enumerateObjectsUsingBlock:"
+ "enumeratePersistentIDsAndProperties:error:enumerationHandler:"
+ "errorWithDomain:code:userInfo:"
+ "eventIdentifier"
+ "eventWithIdentifier:dueDate:eventOptions:"
+ "featureFlagIsEnabled:"
+ "fetchCloudState:codableSyncState:profile:error:"
+ "fetchLocalState:profile:transaction:error:"
+ "filteredArrayUsingPredicate:"
+ "getBloodPressureJournalDeliveredNotificationIdentifiersWithCompletionHandler:"
+ "getDeliveredNotificationsWithCompletionHandler:"
+ "getPregnancyModelProvider"
+ "hasBedtimeSamplesForDayIndex:"
+ "hasEndDate"
+ "hasPrefix:"
+ "hasSetUpBPJ"
+ "hasTimeZoneChange"
+ "hasWakeupSamplesForDayIndex:"
+ "hd_dataOriginProvenance"
+ "hdhr_hypertensionNotificationsDeviceLocalDomainForProfile:"
+ "hdhr_hypertensionNotificationsSyncedDomainForProfile:"
+ "hermit"
+ "hk_UUIDWithData:"
+ "hk_addEntriesFromNonNilDictionary:"
+ "hk_addNonNilObject:"
+ "hk_codableDateComponents"
+ "hk_dataForUUIDBytes"
+ "hk_dateComponentsForCalendarUnit:"
+ "hk_dateComponentsWithCodableDateComponents:calendarUnits:"
+ "hk_dateIntervalForDayFromDate:calendar:"
+ "hk_isAfterOrEqualToDate:"
+ "hk_isBeforeOrEqualToDate:"
+ "hk_oneDay"
+ "hkhrBPJ_requestForNotification:"
+ "hkhr_bloodPressureJournalDefaults"
+ "hkhr_hypertensionNotificationsDefaults"
+ "hypertensionEventType"
+ "hypertensionNotificationsAvailabilityManager"
+ "hypertensionNotifications_eligibility"
+ "hypertensiveMeasurementType"
+ "identifierFromBPSample:journal:"
+ "identifierString"
+ "initWithAction:alarmEventIdentifier:"
+ "initWithAction:categoryIdentifier:expirationDate:"
+ "initWithAction:journalIdentifier:"
+ "initWithArray:"
+ "initWithChangesSyncRequest:contextSyncRequest:stateSyncRequest:medicalIDSyncRequest:summarySharingSyncRequest:"
+ "initWithDaemon:"
+ "initWithDate:value:"
+ "initWithDayWindowType:scheduledTime:"
+ "initWithDomain:key:sampleOriginKey:sampleType:syncEntityClass:timeWindow:loggingCategory:sampleUUIDsFunction:"
+ "initWithEventSubmissionManager:"
+ "initWithIdentifierString:"
+ "initWithJournal:"
+ "initWithJournalIdentifier:notificationDayIndex:journalWindowType:"
+ "initWithKeyValueDomain:featureAvailabilityProvider:"
+ "initWithMeasurementIndex:measurementCount:measurementWindowType:"
+ "initWithName:"
+ "initWithProfile:analysisWindowInterval:keyValueDomain:analyticsEventSubmissionManager:"
+ "initWithProfile:clientIdentifier:queue:"
+ "initWithProfile:dateInterval:additionalPayload:"
+ "initWithProfile:featureAvailabilityExtension:loggingCategory:"
+ "initWithProfile:featureIdentifier:availabilityRequirements:currentOnboardingVersion:pairedDeviceCapability:regionAvailabilityProvider:disableAndExpiryProvider:loggingCategory:"
+ "initWithProfile:featureStatusProvider:keyValueDomain:analysisWindowInterval:analysisWindowGraceInterval:analysisCadenceInterval:analysisRetryInterval:pregnancyStateProvider:measurementAnalyzer:"
+ "initWithProfile:featureStatusProvider:pairedSyncStateProvider:keyValueDomain:"
+ "initWithProfile:featureStatusProvider:pregnancyStateProvider:measurementAnalyzer:"
+ "initWithProfile:operation:"
+ "initWithProfile:type:"
+ "initWithProfile:userDefaults:"
+ "initWithProfile:v1FeatureAvailabilityManager:v2FeatureAvailabilityManager:hypertensionNotificationsFeatureAvailabilityManager:analyticsSubmissionManager:"
+ "initWithProfile:v1FeatureAvailabilityManager:v2FeatureAvailabilityManager:hypertensionNotificationsFeatureAvailabilityManager:analyticsSubmissionManager:protectedDataOperation:"
+ "initWithUUID:startDate:endDate:timestamp:journalType:scheduleType:journalState:timeIntervals:"
+ "initWithWakeupAlarmStartDate:wakeupAlarmCount:bedtimeAlarmStartDate:bedtimeAlarmCount:"
+ "initWithWithDomain:dataKeys:"
+ "insertBloodPressureJournal:isUserInitiated:error:onCommit:onRollback:"
+ "insertBloodPressureJournal:profile:transaction:error:"
+ "insertBloodPressureJournals:error:onCommit:onRollback:"
+ "insertBloodPressureJournals:isUserInitiated:error:onCommit:onRollback:"
+ "insertJournalScheduleInterval:ownerID:database:error:"
+ "integerValueFromKeyValuePair:"
+ "isAFibHistoryEnabled"
+ "isAlarmEventWithIdentifiersOnHold:journalIdentifier:error:"
+ "isAlarmEventWithJournalIdentifierOnHold:error:"
+ "isAlarmEventWithNotificationIdentifierOnHold:error:"
+ "isComplete"
+ "isFollowUp"
+ "isImproveHealthAndActivityEnabled"
+ "isOnboardedHTN"
+ "isPregnancyModeEnabled"
+ "journalEntryForSample:"
+ "journalIdentifier"
+ "journalIdentifierString"
+ "journalManager:didAddOrModifyJournals:"
+ "journalStartDayFor:"
+ "journalState"
+ "journalType"
+ "journalWindowType"
+ "key"
+ "lastInsertRowID"
+ "latestActiveBloodPressureJournalWithError:"
+ "localAvailabilityForBloodPressureJournal"
+ "localAvailabilityForHypertensionNotifications"
+ "longLongValue"
+ "longValue"
+ "mean_entered_bp_category"
+ "mean_score"
+ "measurementCount"
+ "measurementIndex"
+ "measurementInfo"
+ "measurementWindowType"
+ "measurementsRequiredToCompleteJournal"
+ "mesurementIndex"
+ "millimeterOfMercuryUnit"
+ "minute"
+ "modificationDateForKey:"
+ "notificationDayIndex"
+ "notificationEndDateForIncompleteJournal:"
+ "notificationForLearnHypertensionRiskWithIdentifier:dueDate:isFollowUp:measurementIndex:measurementCount:measurementWindowType:"
+ "notificationHoldInstructionsWithError:"
+ "notificationIdentifier"
+ "notificationIdentifier provided is invalid %@"
+ "notificationIdentifierFromCategoryIdentifier:"
+ "notificationIdentifierString"
+ "notificationIdentifiersFromCategoryIdentifiers:"
+ "notificationSyncClient"
+ "notificationSyncClient:didReceiveInstructionWithAction:"
+ "notificationToMonitorHypertensionWithIdentifier:dueDate:isFollowUp:"
+ "notificationsReenabled"
+ "notifyObserversOfAddOrModifyJournals:"
+ "numBGHRHoursPast30Days"
+ "numBPJRemindersSinceMostRecentBPJCycleStart"
+ "numBackgroundHRSamplesInPreviousCalendarDay"
+ "numCompletedBPJBedTimeEntriesInMostRecentCycle"
+ "numCompletedBPJDailyEntriesInMostRecentCycle"
+ "numCompletedBPJWakeUpEntriesInMostRecentCycle"
+ "numDaysSinceLastAnalysis"
+ "numDaysSinceLastHTNotification"
+ "numDaysSinceLastLoggedinBPJ"
+ "numDaysSinceMostRecentBPJCycleStart"
+ "numDaysSinceOpenedHTNDataTypeRoom"
+ "numDaysWatchWornMoreThan12Hours"
+ "numDaysWatchWornMoreThan8Hours"
+ "numDaysWithAdequateDataInPast30Days"
+ "numHRVValuesInPast30Days"
+ "numHTNotificationsInPast180Days"
+ "numHTNotificationsInPast30Days"
+ "numMonthBPJCyclesClosedPastYear"
+ "numMonthBPJCyclesCompletedPastYear"
+ "numMonthBPJCyclesStartedPastYear"
+ "numStandHoursInPast30Days"
+ "numStandHoursInPreviousCalendarDay"
+ "numTachogramsInPreviousCalendarDay"
+ "numWeekBPJCyclesClosedPastYear"
+ "numWeekBPJCyclesCompletedPastYear"
+ "numWeekBPJCyclesStartedPastYear"
+ "num_scores"
+ "numberOfDaysBetweenStartDate:endDate:withCalendar:"
+ "object"
+ "objectsForType:"
+ "oldestSampleWithType:profile:encodingOptions:predicate:error:"
+ "onCommit:orRollback:"
+ "onboardingNotAcknowledgedWithIdentifier:"
+ "onboardingRecordIsPresentForFeatureWithIdentifier:"
+ "performAnalysisWithStartDate:endDate:databaseTransactionContext:error:"
+ "performWithTransactionContext:error:block:"
+ "persistCloudState:profile:error:"
+ "persistentID"
+ "possible washout end date"
+ "possibleHypertension"
+ "predicateWithBlock:"
+ "predicateWithProperty:equalToValue:"
+ "pregnancyModelDidUpdate:"
+ "primaryProfile"
+ "profileExtensionsConformingToProtocol:"
+ "profileIdentifier"
+ "q48@0:8^@16@\"HDCodableSyncState\"24@\"HDProfile\"32^@40"
+ "q48@0:8^@16@24@32^@40"
+ "q64@0:8^@16@\"<HDSyncCodable>\"24@\"<HDSyncCodable>\"32@\"HDProfile\"40@\"HDDatabaseTransaction\"48^@56"
+ "q64@0:8^@16@24@32@40@48^@56"
+ "quantitySampleSyncEntityClass"
+ "quantitySamples"
+ "registerObserver:"
+ "registerObserver:isUserInitiated:"
+ "remoteDisabled"
+ "remoteObjectProxyWithErrorHandler:"
+ "remote_closeJournal:completion:"
+ "remote_closeJournalWithIdentifier:completion:"
+ "remote_fetchActiveJournalWithCompletion:"
+ "remote_fetchAllJournalsWithCompletion:"
+ "remote_observeJournalChanges:completion:"
+ "remote_saveJournal:completion:"
+ "remote_snoozeJournalNotificationWithIdentifier:journalType:userInfo:onDate:completion:"
+ "remote_unitTesting_createTaskServerNoOpWithCompletion:"
+ "removeAllEventsWithError:"
+ "removeDeliveredNotificationsForSamples:journal:"
+ "removeDeliveredNotificationsWithIdentifiers:"
+ "removeEvents:error:"
+ "request"
+ "requestStateSyncWithReason:"
+ "rescindedUnknown"
+ "resetInterval"
+ "sample"
+ "scheduleEvents:error:"
+ "scheduleNotificationsWithReason:error:"
+ "scheduleType"
+ "scheduledTime"
+ "secondsFromGMT"
+ "seedExpiry"
+ "seedIsNotExpiredForFeatureWithIdentifier:"
+ "sendNotificationInstruction:criteria:error:"
+ "serverInterface"
+ "setBedtimeAlarmCount:"
+ "setBedtimeAlarmStartDate:"
+ "setCacheScope:"
+ "setCodableObject:version:profile:"
+ "setDateFormat:"
+ "setDay:"
+ "setDayWindowType:"
+ "setDidRegenerateNotificationsHandler:"
+ "setDidRequestNotificationsRemovalHandler:"
+ "setDidTriggerSyncHandler:"
+ "setEndDate:"
+ "setJournalState:"
+ "setJournalType:"
+ "setMinute:"
+ "setScheduleType:"
+ "setScheduledTime:"
+ "setSortDescriptors:"
+ "setStartDate:"
+ "setTimeIntervals:"
+ "setTimestamp:"
+ "setUnitTest_analysisOperationEnqueued:"
+ "setUnitTest_featureStatusUpdateBlock:"
+ "setUnitTest_latestAnalysisStartDate:"
+ "setUnitTesting_configuredDate:"
+ "setUnitTesting_didRequestRetryOnFeatureStatusChangeHandler:"
+ "setUnitTesting_expirationRestorableAlarm:"
+ "setUnitTesting_forceEnableNotifications:"
+ "setUnitTesting_localTimeZone:"
+ "setUnitTesting_notificationNotPostedHandler:"
+ "setUnitTesting_postNotificationWithRequestHandler:"
+ "setUnitTesting_restorableAlarm:"
+ "setUnitTesting_restorableAlarmQueue:"
+ "setUnitTesting_shouldIgnoreDeliveredAlarmEvents:"
+ "setUnitTesting_snoozeRestorableAlarm:"
+ "setWakeupAlarmCount:"
+ "setWakeupAlarmStartDate:"
+ "shouldUpdateWithMergedState:cloudState:localState:profile:transaction:error:"
+ "snoozeBloodPressureJournalNotificationWithIdentifier:journalType:userInfo:onDate:error:"
+ "sortDescriptorWithKey:ascending:"
+ "stateEntitySchema"
+ "stateSyncBloodPressureJournalDelegateKey"
+ "statistics"
+ "submitAnalyticsEvent:forJournal:windowType:"
+ "substringFromIndex:"
+ "summaryFromSamples:journal:"
+ "supportedSyncVersionRange"
+ "syncDidFinishWithResult:stateStore:profile:"
+ "syncIdentity"
+ "syncIdentityManager"
+ "systemTimeZone"
+ "timeIntervals"
+ "timeIntervalsCount"
+ "timeZoneDidChange:"
+ "timeZoneFromDefaults"
+ "timestamp"
+ "total_count_bp_values_entered"
+ "unitTest_analysisOperationEnqueued"
+ "unitTest_featureStatusUpdateBlock"
+ "unitTest_latestAnalysisStartDate"
+ "unitTesting_configuredDate"
+ "unitTesting_didRequestRetryOnFeatureStatusChangeHandler"
+ "unitTesting_expirationRestorableAlarm"
+ "unitTesting_forceEnableNotifications"
+ "unitTesting_localTimeZone"
+ "unitTesting_notificationNotPostedHandler"
+ "unitTesting_postNotificationWithRequestHandler"
+ "unitTesting_restorableAlarm"
+ "unitTesting_restorableAlarmQueue"
+ "unitTesting_shouldIgnoreDeliveredAlarmEvents"
+ "unitTesting_snoozeRestorableAlarm"
+ "unsatisfiedRequirementIdentifiersDescription"
+ "updateCodableSyncState:withMergeState:profile:error:"
+ "updateDataWithStateStorage:configuration:profile:transaction:error:"
+ "updateDataWithStateStorage:profile:transaction:error:"
+ "updateDataWithStateStore:delegate:profile:transaction:error:"
+ "updateDefaultsTimeZone:"
+ "updateNotificationSyncManagerWithClosedJournals:"
+ "updateTimeZoneIfRequired"
+ "v16@?0@\"<HDHRBloodPressureJournalObserver>\"8"
+ "v16@?0@\"NSArray\"8"
+ "v24@0:8@\"HKMCPregnancyModel\"16"
+ "v24@0:8@?<v@?@\"HKHRBloodPressureJournal\"@\"NSError\">16"
+ "v24@0:8@?<v@?@\"NSArray\"@\"NSError\">16"
+ "v32@0:8@\"HDHRBloodPressureJournalManager\"16@\"NSArray\"24"
+ "v32@0:8@\"HDNotificationSyncClient\"16q24"
+ "v32@0:8@\"HKHRBloodPressureJournal\"16@?<v@?B@\"NSError\">24"
+ "v32@?0@\"HDCodableBloodPressureJournal\"8Q16^B24"
+ "v32@?0@\"HDCodableBloodPressureJournalScheduleTimeInterval\"8Q16^B24"
+ "v32@?0@\"HKHRBloodPressureJournal\"8Q16^B24"
+ "v32@?0@\"HKHRBloodPressureJournalScheduleTimeInterval\"8Q16^B24"
+ "v40@0:8@16@24q32"
+ "v40@0:8q16@\"<HDCloudSyncStateStore>\"24@\"HDProfile\"32"
+ "v40@0:8q16@24@32"
+ "v56@0:8@\"NSString\"16q24@\"NSDictionary\"32@\"NSDate\"40@?<v@?B@\"NSError\">48"
+ "valid_score_days"
+ "valueFromKeyValuePair:"
+ "wakeUpCount"
+ "wakeupAlarmCount"
+ "wakeupAlarmStartDate"
+ "wakeupTimeInterval"
+ "weekOfYear"
+ "weeksSinceOnboardedBPJ"
+ "weeksSinceOnboardedHTN"
+ "yyyy-MM-dd HH:mm"
+ "yyyy-MM-dd HH:mm:ss"
+ "{?=ii}16@0:8"
+ "\xf0\xe1"
- "\xf0!"

```
