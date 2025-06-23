## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

-6074.1.2.4.0
-  __TEXT.__text: 0x7a1bc
+6087.1.2.1.0
+  __TEXT.__text: 0x7a3f4
   __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x89ec
+  __TEXT.__objc_methlist: 0x8a3c
   __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x2afb
+  __TEXT.__cstring: 0x2afe
   __TEXT.__oslogstring: 0xb8ba
-  __TEXT.__gcc_except_tab: 0x123c
-  __TEXT.__unwind_info: 0x2188
-  __TEXT.__objc_classname: 0x1f5f
-  __TEXT.__objc_methname: 0x11a10
-  __TEXT.__objc_methtype: 0x3698
-  __TEXT.__objc_stubs: 0xd520
+  __TEXT.__gcc_except_tab: 0x1254
+  __TEXT.__unwind_info: 0x2198
+  __TEXT.__objc_classname: 0x1fad
+  __TEXT.__objc_methname: 0x11a50
+  __TEXT.__objc_methtype: 0x36cb
+  __TEXT.__objc_stubs: 0xd560
   __DATA_CONST.__got: 0xa80
-  __DATA_CONST.__const: 0x2450
+  __DATA_CONST.__const: 0x2478
   __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x318
+  __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d38
+  __DATA_CONST.__objc_selrefs: 0x3d48
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x360
   __AUTH_CONST.__auth_got: 0x620
   __AUTH_CONST.__const: 0xce0
   __AUTH_CONST.__cfstring: 0x1ec0
-  __AUTH_CONST.__objc_const: 0x100c8
+  __AUTH_CONST.__objc_const: 0x101f0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0xc80
   __DATA.__objc_ivar: 0x5a4
-  __DATA.__data: 0x2530
+  __DATA.__data: 0x25f0
   __DATA_DIRTY.__objc_ivar: 0xd0
   __DATA_DIRTY.__objc_data: 0x2800
   __DATA_DIRTY.__bss: 0xb0

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CC53183F-C4B3-3F10-96D1-3CEF78163307
-  Functions: 2965
-  Symbols:   10656
-  CStrings:  4819
+  UUID: 3EBD3776-5726-357C-B0CD-099BCE1685A9
+  Functions: 2968
+  Symbols:   10679
+  CStrings:  4824
 
Symbols:
+ -[HDSPAnalyticsDailyReportBuilder _lastNightsNumberOfAwakeEvents]
+ GCC_except_table26
+ __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.411
+ __OBJC_$_PROP_LIST_HKSHWakeUpResultsNotificationDescribing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKSHWakeUpResultsNotificationBuilding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKSHWakeUpResultsNotificationDescribing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKSHWakeUpResultsNotificationBuilding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKSHWakeUpResultsNotificationDescribing
+ __OBJC_$_PROTOCOL_REFS_HKSHWakeUpResultsNotificationBuilding
+ __OBJC_$_PROTOCOL_REFS_HKSHWakeUpResultsNotificationDescribing
+ __OBJC_CLASS_PROTOCOLS_$_HDSPWakeUpResultsNotification
+ __OBJC_CLASS_PROTOCOLS_$_HDSPWakeUpResultsNotificationBuilder
+ __OBJC_LABEL_PROTOCOL_$_HKSHWakeUpResultsNotificationBuilding
+ __OBJC_LABEL_PROTOCOL_$_HKSHWakeUpResultsNotificationDescribing
+ __OBJC_PROTOCOL_$_HKSHWakeUpResultsNotificationBuilding
+ __OBJC_PROTOCOL_$_HKSHWakeUpResultsNotificationDescribing
+ ___39-[HDSPSleepSessionManager saveSession:]_block_invoke.315
+ ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.406
+ ___42-[HDSPMobileTimerBridge _checkAlarmServer]_block_invoke.296
+ ___42-[HDSPSleepWidgetManager eventIdentifiers]_block_invoke.296
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.318
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.320
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.322
+ ___44-[HDSPEnvironment environmentDidBecomeReady]_block_invoke.426
+ ___46-[HDSPSleepLockScreenManager eventIdentifiers]_block_invoke.296
+ ___47-[HDSPEnvironment environmentShouldMigrateData]_block_invoke.422
+ ___47-[HDSPNotificationListener _registerForStream:]_block_invoke.306
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.309
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.314
+ ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.371
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.317
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.318
+ ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke.379
+ ___51-[HDSPSleepModeStateMachineState updateStateCommon]_block_invoke.294
+ ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.298
+ ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.299
+ ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke.304
+ ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.296
+ ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.303
+ ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.384
+ ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.302
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.325
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.327
+ ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.383
+ ___60-[HDSPSleepScheduleModelMigrationManager _migrateToCloudKit]_block_invoke.294
+ ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.309
+ ___64-[HDSPSleepScheduleModelMigrationManager _migrateHomeScreenPage]_block_invoke.303
+ ___64-[HDSPSleepScheduleStateCoordinatorBedtimeState wakeTimeReached]_block_invoke.296
+ ___65-[HDSPAnalyticsDailyReportBuilder _lastNightsNumberOfAwakeEvents]_block_invoke
+ ___65-[HDSPAnalyticsDailyReportBuilder _lastNightsNumberOfAwakeEvents]_block_invoke_2
+ ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.307
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.310
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.312
+ ___74-[HDSPSleepLockScreenAssertionManager listener:shouldAcceptNewConnection:]_block_invoke.310
+ ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.331
+ ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.313
+ ___77-[HDSPCFUserNotificationCenter _publishWakeDetectionNotificationForUserInfo:]_block_invoke.295
+ ___78-[HDSPSleepScheduleModelMigrationManager _migrateSleepScheduleFromMobileTimer]_block_invoke.298
+ ___86-[HDSPSleepModeManager initWithEnvironment:sleepFocusModeBridge:sleepProactiveBridge:]_block_invoke.303
+ ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.339
+ ___block_descriptor_40_e8_32w_e49_v16?0"<HKSHWakeUpResultsNotificationBuilding>"8lw32l8
+ ___block_descriptor_48_e8_32r40r_e30_v16?0"HKSleepPeriodSegment"8lr32l8r40l8
+ ___block_literal_global.302
+ ___block_literal_global.306
+ ___block_literal_global.313
+ ___block_literal_global.314
+ ___block_literal_global.318
+ ___block_literal_global.322
+ ___block_literal_global.326
+ ___block_literal_global.327
+ ___block_literal_global.331
+ ___block_literal_global.335
+ ___block_literal_global.339
+ ___block_literal_global.343
+ ___block_literal_global.347
+ ___block_literal_global.351
+ ___block_literal_global.355
+ ___block_literal_global.359
+ ___block_literal_global.360
+ ___block_literal_global.364
+ ___block_literal_global.368
+ ___block_literal_global.372
+ ___block_literal_global.374
+ ___block_literal_global.376
+ ___block_literal_global.380
+ ___block_literal_global.384
+ ___block_literal_global.389
+ ___block_literal_global.393
+ ___block_literal_global.397
+ ___block_literal_global.403
+ _objc_msgSend$_lastNightsNumberOfAwakeEvents
+ _objc_msgSend$setNumberOfAwakeEventsLastNight:
- __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.408
- ___39-[HDSPSleepSessionManager saveSession:]_block_invoke.312
- ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.403
- ___42-[HDSPMobileTimerBridge _checkAlarmServer]_block_invoke.293
- ___42-[HDSPSleepWidgetManager eventIdentifiers]_block_invoke.293
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.315
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.317
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.319
- ___44-[HDSPEnvironment environmentDidBecomeReady]_block_invoke.423
- ___46-[HDSPSleepLockScreenManager eventIdentifiers]_block_invoke.293
- ___47-[HDSPEnvironment environmentShouldMigrateData]_block_invoke.419
- ___47-[HDSPNotificationListener _registerForStream:]_block_invoke.303
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.306
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.308
- ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.368
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.314
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.315
- ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke.376
- ___51-[HDSPSleepModeStateMachineState updateStateCommon]_block_invoke.291
- ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.295
- ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.296
- ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke.301
- ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.293
- ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.300
- ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.381
- ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.299
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.321
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.322
- ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.380
- ___60-[HDSPSleepScheduleModelMigrationManager _migrateToCloudKit]_block_invoke.291
- ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.306
- ___64-[HDSPSleepScheduleModelMigrationManager _migrateHomeScreenPage]_block_invoke.300
- ___64-[HDSPSleepScheduleStateCoordinatorBedtimeState wakeTimeReached]_block_invoke.293
- ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.304
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.307
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.309
- ___74-[HDSPSleepLockScreenAssertionManager listener:shouldAcceptNewConnection:]_block_invoke.307
- ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.325
- ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.310
- ___77-[HDSPCFUserNotificationCenter _publishWakeDetectionNotificationForUserInfo:]_block_invoke.292
- ___78-[HDSPSleepScheduleModelMigrationManager _migrateSleepScheduleFromMobileTimer]_block_invoke.295
- ___86-[HDSPSleepModeManager initWithEnvironment:sleepFocusModeBridge:sleepProactiveBridge:]_block_invoke.300
- ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.333
- ___block_descriptor_40_e8_32w_e46_v16?0"HDSPWakeUpResultsNotificationBuilder"8lw32l8
- ___block_literal_global.292
- ___block_literal_global.293
- ___block_literal_global.294
- ___block_literal_global.305
- ___block_literal_global.312
- ___block_literal_global.316
- ___block_literal_global.320
- ___block_literal_global.324
- ___block_literal_global.328
- ___block_literal_global.332
- ___block_literal_global.336
- ___block_literal_global.340
- ___block_literal_global.344
- ___block_literal_global.345
- ___block_literal_global.349
- ___block_literal_global.353
- ___block_literal_global.357
- ___block_literal_global.361
- ___block_literal_global.365
- ___block_literal_global.369
- ___block_literal_global.371
- ___block_literal_global.373
- ___block_literal_global.377
- ___block_literal_global.381
- ___block_literal_global.386
- ___block_literal_global.390
- ___block_literal_global.394
- ___block_literal_global.400
CStrings:
+ "@\"<HKSHWakeUpResultsNotificationDescribing>\"16@0:8"
+ "HKSHWakeUpResultsNotificationBuilding"
+ "HKSHWakeUpResultsNotificationDescribing"
+ "_lastNightsNumberOfAwakeEvents"
+ "setNumberOfAwakeEventsLastNight:"
+ "v16@?0@\"<HKSHWakeUpResultsNotificationBuilding>\"8"
- "v16@?0@\"HDSPWakeUpResultsNotificationBuilder\"8"

```
