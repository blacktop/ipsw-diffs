## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

-6200.3.4.0.0
+6200.3.8.0.0
   __TEXT.__text: 0x7dcac
   __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x8b54
+  __TEXT.__objc_methlist: 0x8b74
   __TEXT.__const: 0x298
   __TEXT.__cstring: 0x2c1f
   __TEXT.__constg_swiftt: 0x80

   __TEXT.__gcc_except_tab: 0x1250
   __TEXT.__unwind_info: 0x2280
   __TEXT.__objc_classname: 0x1fc5
-  __TEXT.__objc_methname: 0x11e00
-  __TEXT.__objc_methtype: 0x375f
+  __TEXT.__objc_methname: 0x11e5f
+  __TEXT.__objc_methtype: 0x37b7
   __TEXT.__objc_stubs: 0xd780
   __DATA_CONST.__got: 0xb38
   __DATA_CONST.__const: 0x24d8

   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3df8
+  __DATA_CONST.__objc_selrefs: 0x3e08
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x368
   __AUTH_CONST.__auth_got: 0x848
   __AUTH_CONST.__const: 0xd30
   __AUTH_CONST.__cfstring: 0x1ec0
-  __AUTH_CONST.__objc_const: 0x10488
+  __AUTH_CONST.__objc_const: 0x10498
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0xe08
   __AUTH.__data: 0x50

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: C135B622-752F-32F7-89A3-1A90529704F3
+  UUID: 38700535-CEA9-3FDD-A77F-64DDEB08B125
   Functions: 3042
   Symbols:   10829
-  CStrings:  4866
+  CStrings:  4870
 
Symbols:
+ __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.420
+ ___39-[HDSPSleepSessionManager saveSession:]_block_invoke.324
+ ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.415
+ ___42-[HDSPMobileTimerBridge _checkAlarmServer]_block_invoke.305
+ ___42-[HDSPSleepWidgetManager eventIdentifiers]_block_invoke.305
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.327
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.329
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.331
+ ___44-[HDSPEnvironment environmentDidBecomeReady]_block_invoke.435
+ ___46-[HDSPSleepLockScreenManager eventIdentifiers]_block_invoke.305
+ ___47-[HDSPEnvironment environmentShouldMigrateData]_block_invoke.431
+ ___47-[HDSPNotificationListener _registerForStream:]_block_invoke.315
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.318
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.320
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.323
+ ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.380
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.326
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.327
+ ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke.388
+ ___51-[HDSPSleepModeStateMachineState updateStateCommon]_block_invoke.303
+ ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.307
+ ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.308
+ ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke.313
+ ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.305
+ ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.312
+ ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.393
+ ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.311
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.335
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.336
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.338
+ ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.392
+ ___60-[HDSPSleepScheduleModelMigrationManager _migrateToCloudKit]_block_invoke.303
+ ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.318
+ ___64-[HDSPSleepScheduleModelMigrationManager _migrateHomeScreenPage]_block_invoke.312
+ ___64-[HDSPSleepScheduleStateCoordinatorBedtimeState wakeTimeReached]_block_invoke.305
+ ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.316
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.319
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.321
+ ___74-[HDSPSleepLockScreenAssertionManager listener:shouldAcceptNewConnection:]_block_invoke.319
+ ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.339
+ ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.342
+ ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.322
+ ___77-[HDSPCFUserNotificationCenter _publishWakeDetectionNotificationForUserInfo:]_block_invoke.304
+ ___78-[HDSPSleepScheduleModelMigrationManager _migrateSleepScheduleFromMobileTimer]_block_invoke.307
+ ___86-[HDSPSleepModeManager initWithEnvironment:sleepFocusModeBridge:sleepProactiveBridge:]_block_invoke.312
+ ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.347
+ ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.350
+ ___block_literal_global.309
+ ___block_literal_global.312
+ ___block_literal_global.316
+ ___block_literal_global.317
+ ___block_literal_global.320
+ ___block_literal_global.324
+ ___block_literal_global.328
+ ___block_literal_global.332
+ ___block_literal_global.336
+ ___block_literal_global.340
+ ___block_literal_global.344
+ ___block_literal_global.357
+ ___block_literal_global.361
+ ___block_literal_global.365
+ ___block_literal_global.369
+ ___block_literal_global.373
+ ___block_literal_global.377
+ ___block_literal_global.381
+ ___block_literal_global.383
+ ___block_literal_global.385
+ ___block_literal_global.398
+ ___block_literal_global.402
+ ___block_literal_global.406
+ ___block_literal_global.412
- __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.411
- ___39-[HDSPSleepSessionManager saveSession:]_block_invoke.315
- ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.406
- ___42-[HDSPMobileTimerBridge _checkAlarmServer]_block_invoke.296
- ___42-[HDSPSleepWidgetManager eventIdentifiers]_block_invoke.296
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.318
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.320
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.322
- ___44-[HDSPEnvironment environmentDidBecomeReady]_block_invoke.426
- ___46-[HDSPSleepLockScreenManager eventIdentifiers]_block_invoke.296
- ___47-[HDSPEnvironment environmentShouldMigrateData]_block_invoke.422
- ___47-[HDSPNotificationListener _registerForStream:]_block_invoke.306
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.309
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.311
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.314
- ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.371
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.317
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.318
- ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke.379
- ___51-[HDSPSleepModeStateMachineState updateStateCommon]_block_invoke.294
- ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.298
- ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.299
- ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke.304
- ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.296
- ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.303
- ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.384
- ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.302
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.326
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.327
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.329
- ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.383
- ___60-[HDSPSleepScheduleModelMigrationManager _migrateToCloudKit]_block_invoke.294
- ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.309
- ___64-[HDSPSleepScheduleModelMigrationManager _migrateHomeScreenPage]_block_invoke.303
- ___64-[HDSPSleepScheduleStateCoordinatorBedtimeState wakeTimeReached]_block_invoke.296
- ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.307
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.310
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.312
- ___74-[HDSPSleepLockScreenAssertionManager listener:shouldAcceptNewConnection:]_block_invoke.310
- ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.330
- ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.333
- ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.313
- ___77-[HDSPCFUserNotificationCenter _publishWakeDetectionNotificationForUserInfo:]_block_invoke.295
- ___78-[HDSPSleepScheduleModelMigrationManager _migrateSleepScheduleFromMobileTimer]_block_invoke.298
- ___86-[HDSPSleepModeManager initWithEnvironment:sleepFocusModeBridge:sleepProactiveBridge:]_block_invoke.303
- ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.338
- ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.341
- ___block_literal_global.295
- ___block_literal_global.296
- ___block_literal_global.297
- ___block_literal_global.298
- ___block_literal_global.299
- ___block_literal_global.300
- ___block_literal_global.301
- ___block_literal_global.302
- ___block_literal_global.303
- ___block_literal_global.318
- ___block_literal_global.326
- ___block_literal_global.339
- ___block_literal_global.343
- ___block_literal_global.347
- ___block_literal_global.351
- ___block_literal_global.355
- ___block_literal_global.359
- ___block_literal_global.372
- ___block_literal_global.374
- ___block_literal_global.376
- ___block_literal_global.380
- ___block_literal_global.384
- ___block_literal_global.397
- ___block_literal_global.403
CStrings:
+ "applicationsDidUpdateMetadata:"
+ "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
+ "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
+ "v52@0:8@16@24B32@36@44"

```
