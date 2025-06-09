## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x7a2dc
-  __TEXT.__auth_stubs: 0xc30
-  __TEXT.__objc_methlist: 0x8994
+6074.1.2.4.0
+  __TEXT.__text: 0x7a1bc
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x89ec
   __TEXT.__const: 0x1d8
   __TEXT.__cstring: 0x2afb
-  __TEXT.__oslogstring: 0xb855
-  __TEXT.__gcc_except_tab: 0x127c
-  __TEXT.__unwind_info: 0x21b8
-  __TEXT.__objc_classname: 0x1f1e
-  __TEXT.__objc_methname: 0x11a16
-  __TEXT.__objc_methtype: 0x360b
+  __TEXT.__oslogstring: 0xb8ba
+  __TEXT.__gcc_except_tab: 0x123c
+  __TEXT.__unwind_info: 0x2188
+  __TEXT.__objc_classname: 0x1f5f
+  __TEXT.__objc_methname: 0x11a10
+  __TEXT.__objc_methtype: 0x3698
   __TEXT.__objc_stubs: 0xd520
-  __DATA_CONST.__got: 0xa78
+  __DATA_CONST.__got: 0xa80
   __DATA_CONST.__const: 0x2450
-  __DATA_CONST.__objc_classlist: 0x538
+  __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x310
+  __DATA_CONST.__objc_protolist: 0x318
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3d38
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x358
-  __AUTH_CONST.__auth_got: 0x628
-  __AUTH_CONST.__const: 0xd00
+  __DATA_CONST.__objc_superrefs: 0x360
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__const: 0xce0
   __AUTH_CONST.__cfstring: 0x1ec0
-  __AUTH_CONST.__objc_const: 0xffd8
+  __AUTH_CONST.__objc_const: 0x100c8
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xcd0
-  __DATA.__objc_ivar: 0x5a0
-  __DATA.__data: 0x24d0
+  __AUTH.__objc_data: 0xc80
+  __DATA.__objc_ivar: 0x5a4
+  __DATA.__data: 0x2530
   __DATA_DIRTY.__objc_ivar: 0xd0
-  __DATA_DIRTY.__objc_data: 0x2760
-  __DATA_DIRTY.__bss: 0xc0
+  __DATA_DIRTY.__objc_data: 0x2800
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
-  - /System/Library/Frameworks/Intents.framework/Intents
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
   - /System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
-  - /System/Library/PrivateFrameworks/ChronoServices.framework/ChronoServices
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98083C6A-7430-31AD-8480-3038E437D6A1
-  Functions: 2964
-  Symbols:   10645
-  CStrings:  4810
+  UUID: CC53183F-C4B3-3F10-96D1-3CEF78163307
+  Functions: 2965
+  Symbols:   10656
+  CStrings:  4819
 
Symbols:
+ +[HDSPBiomeInBedDetector inBedDetectorWithProvider:]
+ -[HDSPBiomeInBedDetectionProvider findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]
+ -[HDSPBiomeInBedDetectionProvider findLastTimeDeviceWasPluggedInDuringInterval:error:]
+ -[HDSPBiomeInBedDetectionProvider findMotionTerminusDuringInterval:latest:error:]
+ -[HDSPBiomeInBedDetectionProvider findTimesDeviceWasUnlockedDuringInterval:error:]
+ -[HDSPBiomeInBedDetector .cxx_destruct]
+ -[HDSPBiomeInBedDetector initWithProvider:]
+ GCC_except_table99
+ _OBJC_CLASS_$_HDSPBiomeInBedDetectionProvider
+ _OBJC_IVAR_$_HDSPBiomeInBedDetector._biomeProvider
+ _OBJC_METACLASS_$_HDSPBiomeInBedDetectionProvider
+ __OBJC_$_INSTANCE_METHODS_HDSPBiomeInBedDetectionProvider
+ __OBJC_$_INSTANCE_VARIABLES_HDSPBiomeInBedDetector
+ __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.408
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSPBiomeInBedDetectionProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDSPBiomeInBedDetectionProviding
+ __OBJC_CLASS_PROTOCOLS_$_HDSPBiomeInBedDetectionProvider
+ __OBJC_CLASS_RO_$_HDSPBiomeInBedDetectionProvider
+ __OBJC_LABEL_PROTOCOL_$_HDSPBiomeInBedDetectionProviding
+ __OBJC_METACLASS_RO_$_HDSPBiomeInBedDetectionProvider
+ __OBJC_PROTOCOL_$_HDSPBiomeInBedDetectionProviding
+ ___39-[HDSPSleepSessionManager saveSession:]_block_invoke.312
+ ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.403
+ ___42-[HDSPMobileTimerBridge _checkAlarmServer]_block_invoke.293
+ ___42-[HDSPSleepWidgetManager eventIdentifiers]_block_invoke.293
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.315
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.317
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.319
+ ___44-[HDSPEnvironment environmentDidBecomeReady]_block_invoke.423
+ ___46-[HDSPSleepLockScreenManager eventIdentifiers]_block_invoke.293
+ ___47-[HDSPEnvironment environmentShouldMigrateData]_block_invoke.419
+ ___47-[HDSPNotificationListener _registerForStream:]_block_invoke.303
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.306
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.311
+ ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.368
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.314
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.315
+ ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke.376
+ ___51-[HDSPSleepModeStateMachineState updateStateCommon]_block_invoke.291
+ ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.295
+ ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.296
+ ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke.301
+ ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.293
+ ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.300
+ ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.381
+ ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.299
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.322
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.324
+ ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.380
+ ___60-[HDSPSleepScheduleModelMigrationManager _migrateToCloudKit]_block_invoke.291
+ ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.306
+ ___64-[HDSPSleepScheduleModelMigrationManager _migrateHomeScreenPage]_block_invoke.300
+ ___64-[HDSPSleepScheduleStateCoordinatorBedtimeState wakeTimeReached]_block_invoke.293
+ ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.304
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.307
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.309
+ ___74-[HDSPSleepLockScreenAssertionManager listener:shouldAcceptNewConnection:]_block_invoke.307
+ ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.328
+ ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.310
+ ___77-[HDSPCFUserNotificationCenter _publishWakeDetectionNotificationForUserInfo:]_block_invoke.292
+ ___78-[HDSPSleepScheduleModelMigrationManager _migrateSleepScheduleFromMobileTimer]_block_invoke.295
+ ___81-[HDSPBiomeInBedDetectionProvider findMotionTerminusDuringInterval:latest:error:]_block_invoke
+ ___82-[HDSPBiomeInBedDetectionProvider findTimesDeviceWasUnlockedDuringInterval:error:]_block_invoke
+ ___82-[HDSPBiomeInBedDetectionProvider findTimesDeviceWasUnlockedDuringInterval:error:]_block_invoke_2
+ ___82-[HDSPBiomeInBedDetectionProvider findTimesDeviceWasUnlockedDuringInterval:error:]_block_invoke_3
+ ___86-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceWasPluggedInDuringInterval:error:]_block_invoke
+ ___86-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceWasPluggedInDuringInterval:error:]_block_invoke_2
+ ___86-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceWasPluggedInDuringInterval:error:]_block_invoke_3
+ ___86-[HDSPSleepModeManager initWithEnvironment:sleepFocusModeBridge:sleepProactiveBridge:]_block_invoke.300
+ ___94-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]_block_invoke
+ ___94-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]_block_invoke_2
+ ___94-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]_block_invoke_3
+ ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.336
+ ___block_literal_global.299
+ ___block_literal_global.303
+ ___block_literal_global.310
+ ___block_literal_global.311
+ ___block_literal_global.315
+ ___block_literal_global.319
+ ___block_literal_global.323
+ ___block_literal_global.324
+ ___block_literal_global.328
+ ___block_literal_global.332
+ ___block_literal_global.336
+ ___block_literal_global.340
+ ___block_literal_global.344
+ ___block_literal_global.348
+ ___block_literal_global.352
+ ___block_literal_global.356
+ ___block_literal_global.357
+ ___block_literal_global.361
+ ___block_literal_global.365
+ ___block_literal_global.369
+ ___block_literal_global.371
+ ___block_literal_global.373
+ ___block_literal_global.377
+ ___block_literal_global.381
+ ___block_literal_global.386
+ ___block_literal_global.390
+ ___block_literal_global.394
+ ___block_literal_global.400
+ _objc_msgSend$findLastTimeDeviceLockChangedDuringInterval:isLocked:error:
+ _objc_msgSend$inBedDetectorWithProvider:
+ _objc_msgSend$initWithProvider:
+ _objc_msgSend$initWithStoreIdentifier:type:
- -[HDSPBiomeInBedDetector _findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]
- -[HDSPBiomeInBedDetector findLastTimeDeviceWasPluggedInDuringInterval:error:]
- -[HDSPBiomeInBedDetector findMotionTerminusDuringInterval:latest:error:]
- -[HDSPBiomeInBedDetector findTimesDeviceWasUnlockedDuringInterval:error:]
- -[HDSPSleepScheduleModelManager _locked_canApplyChangesFrom:to:error:]
- GCC_except_table100
- _HKSPCanResolveChangesToObject
- __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.405
- ___39-[HDSPSleepSessionManager saveSession:]_block_invoke.309
- ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.400
- ___42-[HDSPMobileTimerBridge _checkAlarmServer]_block_invoke.290
- ___42-[HDSPSleepWidgetManager eventIdentifiers]_block_invoke.290
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.312
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.314
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.316
- ___44-[HDSPEnvironment environmentDidBecomeReady]_block_invoke.420
- ___46-[HDSPSleepLockScreenManager eventIdentifiers]_block_invoke.290
- ___47-[HDSPEnvironment environmentShouldMigrateData]_block_invoke.416
- ___47-[HDSPNotificationListener _registerForStream:]_block_invoke.300
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.303
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.305
- ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.365
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.311
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.312
- ___50+[HDSPUserNotificationCenter _stringForEventDate:]_block_invoke
- ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke.373
- ___51-[HDSPSleepModeStateMachineState updateStateCommon]_block_invoke.288
- ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.292
- ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.293
- ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke.298
- ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.290
- ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.297
- ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.378
- ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.296
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.318
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.319
- ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.377
- ___60-[HDSPSleepScheduleModelMigrationManager _migrateToCloudKit]_block_invoke.288
- ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.303
- ___64-[HDSPSleepScheduleModelMigrationManager _migrateHomeScreenPage]_block_invoke.297
- ___64-[HDSPSleepScheduleStateCoordinatorBedtimeState wakeTimeReached]_block_invoke.290
- ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.301
- ___72-[HDSPBiomeInBedDetector findMotionTerminusDuringInterval:latest:error:]_block_invoke
- ___73-[HDSPBiomeInBedDetector findTimesDeviceWasUnlockedDuringInterval:error:]_block_invoke
- ___73-[HDSPBiomeInBedDetector findTimesDeviceWasUnlockedDuringInterval:error:]_block_invoke_2
- ___73-[HDSPBiomeInBedDetector findTimesDeviceWasUnlockedDuringInterval:error:]_block_invoke_3
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.304
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.306
- ___74-[HDSPSleepLockScreenAssertionManager listener:shouldAcceptNewConnection:]_block_invoke.304
- ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.322
- ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.307
- ___77-[HDSPBiomeInBedDetector findLastTimeDeviceWasPluggedInDuringInterval:error:]_block_invoke
- ___77-[HDSPBiomeInBedDetector findLastTimeDeviceWasPluggedInDuringInterval:error:]_block_invoke_2
- ___77-[HDSPBiomeInBedDetector findLastTimeDeviceWasPluggedInDuringInterval:error:]_block_invoke_3
- ___77-[HDSPCFUserNotificationCenter _publishWakeDetectionNotificationForUserInfo:]_block_invoke.289
- ___78-[HDSPSleepScheduleModelMigrationManager _migrateSleepScheduleFromMobileTimer]_block_invoke.292
- ___86-[HDSPBiomeInBedDetector _findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]_block_invoke
- ___86-[HDSPBiomeInBedDetector _findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]_block_invoke_2
- ___86-[HDSPBiomeInBedDetector _findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]_block_invoke_3
- ___86-[HDSPSleepModeManager initWithEnvironment:sleepFocusModeBridge:sleepProactiveBridge:]_block_invoke.297
- ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.330
- ___block_literal_global.289
- ___block_literal_global.290
- ___block_literal_global.291
- ___block_literal_global.302
- ___block_literal_global.306
- ___block_literal_global.309
- ___block_literal_global.313
- ___block_literal_global.317
- ___block_literal_global.321
- ___block_literal_global.325
- ___block_literal_global.329
- ___block_literal_global.333
- ___block_literal_global.337
- ___block_literal_global.341
- ___block_literal_global.342
- ___block_literal_global.346
- ___block_literal_global.350
- ___block_literal_global.354
- ___block_literal_global.358
- ___block_literal_global.362
- ___block_literal_global.366
- ___block_literal_global.368
- ___block_literal_global.370
- ___block_literal_global.374
- ___block_literal_global.378
- ___block_literal_global.383
- ___block_literal_global.387
- ___block_literal_global.391
- ___block_literal_global.397
- _objc_msgSend$_findLastTimeDeviceLockChangedDuringInterval:isLocked:error:
- _objc_msgSend$_initWithStoreIdentifier:usingEndToEndEncryption:
- _objc_msgSend$_locked_canApplyChangesFrom:to:error:
- _objc_msgSend$nebula
CStrings:
+ "@\"<HDSPBiomeInBedDetectionProviding>\""
+ "@\"NSArray\"32@0:8@\"NSDateInterval\"16^@24"
+ "@\"NSDate\"32@0:8@\"NSDateInterval\"16^@24"
+ "@\"NSDate\"36@0:8@\"NSDateInterval\"16B24^@28"
+ "HDSPBiomeInBedDetectionProvider"
+ "HDSPBiomeInBedDetectionProviding"
+ "[%{public}@] Detecting in-bed intervals between night start (%@) and end (%@)"
+ "[%{public}@] Establing night end.."
+ "[%{public}@] Limited search for locked events to last lock end %@"
+ "[%{public}@] Looking for earliest start of movement between %@ and %@"
+ "[%{public}@] Looking for times device was locked in %@"
+ "_biomeProvider"
+ "findLastTimeDeviceLockChangedDuringInterval:isLocked:error:"
+ "inBedDetectorWithProvider:"
+ "initWithProvider:"
+ "initWithStoreIdentifier:type:"
- "B40@0:8@16@24^@32"
- "[%{public}@] Detecting in-bed intervals between %@ and %@"
- "[%{public}@] trying to update %{public}@ (last modified: %{public}@) to %{public}@ (last modified: %{public}@), seeing if we can resolve changes"
- "_findLastTimeDeviceLockChangedDuringInterval:isLocked:error:"
- "_initWithStoreIdentifier:usingEndToEndEncryption:"
- "_locked_canApplyChangesFrom:to:error:"
- "nebula"

```
