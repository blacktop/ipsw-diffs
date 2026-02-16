## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

-6200.4.9.0.0
-  __TEXT.__text: 0x7dcac
-  __TEXT.__auth_stubs: 0x1070
-  __TEXT.__objc_methlist: 0x8b74
-  __TEXT.__const: 0x298
-  __TEXT.__cstring: 0x2c1f
+6200.5.77.2.6
+  __TEXT.__text: 0x82158
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__objc_methlist: 0x8b14
+  __TEXT.__const: 0x2a8
+  __TEXT.__cstring: 0x2acb
   __TEXT.__constg_swiftt: 0x80
   __TEXT.__swift5_typeref: 0x3a
   __TEXT.__swift5_reflstr: 0x5b
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
   __TEXT.__swift5_capture: 0x10
-  __TEXT.__oslogstring: 0xb986
-  __TEXT.__gcc_except_tab: 0x1250
-  __TEXT.__unwind_info: 0x2280
-  __TEXT.__objc_classname: 0x1fc5
-  __TEXT.__objc_methname: 0x11e5f
-  __TEXT.__objc_methtype: 0x37b7
-  __TEXT.__objc_stubs: 0xd780
-  __DATA_CONST.__got: 0xb38
-  __DATA_CONST.__const: 0x24d8
-  __DATA_CONST.__objc_classlist: 0x558
+  __TEXT.__oslogstring: 0xb9ac
+  __TEXT.__gcc_except_tab: 0x119c
+  __TEXT.__unwind_info: 0x2240
+  __TEXT.__objc_classname: 0x200f
+  __TEXT.__objc_methname: 0x11ee7
+  __TEXT.__objc_methtype: 0x37b8
+  __TEXT.__objc_stubs: 0xd800
+  __DATA_CONST.__got: 0xb40
+  __DATA_CONST.__const: 0x2498
+  __DATA_CONST.__objc_classlist: 0x550
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x3e08
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x368
-  __AUTH_CONST.__auth_got: 0x848
+  __DATA_CONST.__objc_superrefs: 0x360
+  __AUTH_CONST.__auth_got: 0x808
   __AUTH_CONST.__const: 0xd30
   __AUTH_CONST.__cfstring: 0x1ec0
-  __AUTH_CONST.__objc_const: 0x10498
+  __AUTH_CONST.__objc_const: 0x10328
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xe08
+  __AUTH.__objc_data: 0xdb8
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x5ac
-  __DATA.__data: 0x2690
+  __DATA.__objc_ivar: 0x5a4
+  __DATA.__data: 0x2698
   __DATA.__common: 0x28
   __DATA_DIRTY.__objc_ivar: 0xd0
   __DATA_DIRTY.__objc_data: 0x2850

   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
   - /System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices
+  - /System/Library/PrivateFrameworks/HealthPlatformFoundation.framework/HealthPlatformFoundation
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
-  - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 00EE3509-1E6A-32AE-9017-E23BFB290D99
-  Functions: 3042
-  Symbols:   10829
-  CStrings:  4870
+  UUID: DA8558BC-D55F-3D70-9C6A-9D9D987FD7A8
+  Functions: 3032
+  Symbols:   10784
+  CStrings:  4863
 
Symbols:
+ __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.459
+ ___39-[HDSPSleepSessionManager saveSession:]_block_invoke.363
+ ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.454
+ ___42-[HDSPMobileTimerBridge _checkAlarmServer]_block_invoke.344
+ ___42-[HDSPSleepWidgetManager eventIdentifiers]_block_invoke.344
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.366
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.368
+ ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.370
+ ___44-[HDSPEnvironment environmentDidBecomeReady]_block_invoke.474
+ ___46-[HDSPSleepLockScreenManager eventIdentifiers]_block_invoke.344
+ ___47-[HDSPEnvironment environmentShouldMigrateData]_block_invoke.470
+ ___47-[HDSPNotificationListener _registerForStream:]_block_invoke.354
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.357
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.359
+ ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.362
+ ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.419
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.365
+ ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.366
+ ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke.427
+ ___51-[HDSPSleepModeStateMachineState updateStateCommon]_block_invoke.342
+ ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.346
+ ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.347
+ ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke.352
+ ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.344
+ ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.351
+ ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.432
+ ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.350
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.374
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.375
+ ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.377
+ ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.431
+ ___60-[HDSPSleepScheduleModelMigrationManager _migrateToCloudKit]_block_invoke.342
+ ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.357
+ ___64-[HDSPSleepScheduleModelMigrationManager _migrateHomeScreenPage]_block_invoke.351
+ ___64-[HDSPSleepScheduleStateCoordinatorBedtimeState wakeTimeReached]_block_invoke.344
+ ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.355
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.358
+ ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.360
+ ___74-[HDSPSleepLockScreenAssertionManager listener:shouldAcceptNewConnection:]_block_invoke.358
+ ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.378
+ ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.381
+ ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.361
+ ___77-[HDSPCFUserNotificationCenter _publishWakeDetectionNotificationForUserInfo:]_block_invoke.343
+ ___78-[HDSPSleepScheduleModelMigrationManager _migrateSleepScheduleFromMobileTimer]_block_invoke.346
+ ___86-[HDSPSleepModeManager initWithEnvironment:sleepFocusModeBridge:sleepProactiveBridge:]_block_invoke.351
+ ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.386
+ ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.389
+ ___block_descriptor_48_e8_32s40s_e22_v16?0"<HKSPClient>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e23_v16?0"<BMStoreData>"8ls32l8w40l8
+ ___block_descriptor_56_e8_32s40s48s_e22_v16?0"<HKSPClient>"8ls32l8s40l8s48l8
+ ___block_descriptor_56_e8_32s_e22_v16?0"<HKSPClient>"8ls32l8
+ ___block_literal_global.343
+ ___block_literal_global.345
+ ___block_literal_global.346
+ ___block_literal_global.347
+ ___block_literal_global.349
+ ___block_literal_global.350
+ ___block_literal_global.351
+ ___block_literal_global.354
+ ___block_literal_global.355
+ ___block_literal_global.358
+ ___block_literal_global.359
+ ___block_literal_global.362
+ ___block_literal_global.363
+ ___block_literal_global.366
+ ___block_literal_global.367
+ ___block_literal_global.370
+ ___block_literal_global.371
+ ___block_literal_global.374
+ ___block_literal_global.375
+ ___block_literal_global.379
+ ___block_literal_global.387
+ ___block_literal_global.391
+ ___block_literal_global.395
+ ___block_literal_global.396
+ ___block_literal_global.399
+ ___block_literal_global.400
+ ___block_literal_global.403
+ ___block_literal_global.404
+ ___block_literal_global.407
+ ___block_literal_global.408
+ ___block_literal_global.416
+ ___block_literal_global.420
+ ___block_literal_global.422
+ ___block_literal_global.424
+ ___block_literal_global.428
+ ___block_literal_global.432
+ ___block_literal_global.437
+ ___block_literal_global.441
+ ___block_literal_global.445
+ ___block_literal_global.451
+ _objc_msgSend$init
+ _objc_msgSend$setIsSleepScoreNotificationEnabled:
+ _objc_msgSend$setSleepScoreLastNight:
+ _objc_msgSend$setSleepScoreNotificationThreshold:
+ _swift_retain
+ _swift_unknownObjectRelease
- -[HDSPMacReadyProvider .cxx_destruct]
- -[HDSPMacReadyProvider delegate]
- -[HDSPMacReadyProvider environment]
- -[HDSPMacReadyProvider initWithEnvironment:]
- -[HDSPMacReadyProvider isInDemoMode]
- -[HDSPMacReadyProvider isSystemReady]
- -[HDSPMacReadyProvider setDelegate:]
- _OBJC_CLASS_$_HDSPMacReadyProvider
- _OBJC_IVAR_$_HDSPMacReadyProvider._delegate
- _OBJC_IVAR_$_HDSPMacReadyProvider._environment
- _OBJC_METACLASS_$_HDSPMacReadyProvider
- __OBJC_$_INSTANCE_METHODS_HDSPMacReadyProvider
- __OBJC_$_INSTANCE_VARIABLES_HDSPMacReadyProvider
- __OBJC_$_PROP_LIST_HDSPMacReadyProvider
- __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.420
- __OBJC_CLASS_PROTOCOLS_$_HDSPMacReadyProvider
- __OBJC_CLASS_RO_$_HDSPMacReadyProvider
- __OBJC_METACLASS_RO_$_HDSPMacReadyProvider
- ___39-[HDSPSleepSessionManager saveSession:]_block_invoke.324
- ___39-[_HDSPBiomeBridge subscribe:callback:]_block_invoke.415
- ___42-[HDSPMobileTimerBridge _checkAlarmServer]_block_invoke.305
- ___42-[HDSPSleepWidgetManager eventIdentifiers]_block_invoke.305
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.327
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.329
- ___43-[HDSPAnalyticsManager _lock_executeQuery:]_block_invoke.331
- ___44-[HDSPEnvironment environmentDidBecomeReady]_block_invoke.435
- ___46-[HDSPSleepLockScreenManager eventIdentifiers]_block_invoke.305
- ___47-[HDSPEnvironment environmentShouldMigrateData]_block_invoke.431
- ___47-[HDSPNotificationListener _registerForStream:]_block_invoke.315
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.318
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.320
- ___47-[HDSPSleepActionManager sleepAlarmWasModified]_block_invoke.323
- ___49-[HDSPSleepEventScheduler _schedulePendingEvents]_block_invoke.380
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke.326
- ___49-[HDSPSleepStoreServer processNoLongerSuspended:]_block_invoke_2.327
- ___50-[HDSPSleepEventScheduler notifyForOverdueEvents:]_block_invoke.388
- ___51-[HDSPSleepModeStateMachineState updateStateCommon]_block_invoke.303
- ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.307
- ___53-[HDSPSleepScheduleStateCoordinator sleepEventIsDue:]_block_invoke.308
- ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke.313
- ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke.305
- ___55-[HDSPAnalyticsManager scheduleDailyCollectionActivity]_block_invoke.312
- ___56-[HDSPSleepEventScheduler eventProviderCancelledEvents:]_block_invoke.393
- ___56-[HDSPSleepStoreServer _performWhenClientIsReady:block:]_block_invoke.311
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.335
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.336
- ___56-[HDSPWakeUpResultsNotificationManager _lock_startQuery]_block_invoke.338
- ___58-[HDSPSleepEventScheduler eventProviderHasUpcomingEvents:]_block_invoke.392
- ___60-[HDSPSleepScheduleModelMigrationManager _migrateToCloudKit]_block_invoke.303
- ___60-[HDSPWakeUpResultsNotificationManager scheduleRetryAttempt]_block_invoke.318
- ___64-[HDSPSleepScheduleModelMigrationManager _migrateHomeScreenPage]_block_invoke.312
- ___64-[HDSPSleepScheduleStateCoordinatorBedtimeState wakeTimeReached]_block_invoke.305
- ___71-[HDSPSleepStoreServer publishWakeUpResultsNotificationWithCompletion:]_block_invoke.316
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSchedule:]_block_invoke.319
- ___73-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepSettings:]_block_invoke.321
- ___74-[HDSPSleepLockScreenAssertionManager listener:shouldAcceptNewConnection:]_block_invoke.319
- ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.339
- ___75-[HDSPWakeUpResultsNotificationManager _fetchUserFirstNameWithHealthStore:]_block_invoke.342
- ___76-[HDSPSleepStoreServer sleepScheduleModelManager:didUpdateSleepEventRecord:]_block_invoke.322
- ___77-[HDSPCFUserNotificationCenter _publishWakeDetectionNotificationForUserInfo:]_block_invoke.304
- ___78-[HDSPSleepScheduleModelMigrationManager _migrateSleepScheduleFromMobileTimer]_block_invoke.307
- ___86-[HDSPSleepModeManager initWithEnvironment:sleepFocusModeBridge:sleepProactiveBridge:]_block_invoke.312
- ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.347
- ___96-[HDSPWakeUpResultsNotificationManager _fetchSleepDaySummariesForMorningIndexRange:healthStore:]_block_invoke.350
- ___block_descriptor_40_e8_32s_e64_v16?0"<HDSPSleepNotificationPublisher><HDSPEnvironmentAware>"8ls32l8
- ___block_descriptor_48_e8_32s40s_e27_v16?0"<HKSPSleepClient>"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e33_v16?0"BMUserFocusModeComputed"8ls32l8w40l8
- ___block_descriptor_56_e8_32s40s48s_e27_v16?0"<HKSPSleepClient>"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s_e27_v16?0"<HKSPSleepClient>"8ls32l8
- ___block_literal_global.304
- ___block_literal_global.305
- ___block_literal_global.306
- ___block_literal_global.307
- ___block_literal_global.308
- ___block_literal_global.309
- ___block_literal_global.310
- ___block_literal_global.311
- ___block_literal_global.312
- ___block_literal_global.313
- ___block_literal_global.314
- ___block_literal_global.315
- ___block_literal_global.316
- ___block_literal_global.317
- ___block_literal_global.319
- ___block_literal_global.320
- ___block_literal_global.322
- ___block_literal_global.323
- ___block_literal_global.324
- ___block_literal_global.327
- ___block_literal_global.328
- ___block_literal_global.331
- ___block_literal_global.332
- ___block_literal_global.335
- ___block_literal_global.336
- ___block_literal_global.340
- ___block_literal_global.357
- ___block_literal_global.360
- ___block_literal_global.364
- ___block_literal_global.365
- ___block_literal_global.368
- ___block_literal_global.369
- ___block_literal_global.373
- ___block_literal_global.377
- ___block_literal_global.381
- ___block_literal_global.385
- ___block_literal_global.389
- ___block_literal_global.393
- ___block_literal_global.398
- ___block_literal_global.402
- ___block_literal_global.406
- ___swift_allocate_boxed_opaque_existential_1
- ___swift_destroy_boxed_opaque_existential_1
- ___swift_mutable_project_boxed_opaque_existential_1
- ___swift_project_boxed_opaque_existential_1
- __swift_FORCE_LOAD_$_swiftMetal
- __swift_FORCE_LOAD_$_swiftMetal_$_SleepDaemon
- __swift_FORCE_LOAD_$_swiftQuartzCore
- __swift_FORCE_LOAD_$_swiftQuartzCore_$_SleepDaemon
- __swift_FORCE_LOAD_$_swiftsimd
- __swift_FORCE_LOAD_$_swiftsimd_$_SleepDaemon
- __swift_stdlib_bridgeErrorToNSError
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x10
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _swift_allocBox
- _swift_errorRelease
- _swift_errorRetain
- _swift_makeBoxUnique
CStrings:
+ "[%s] fireTaggedWork failed with error %@"
+ "[%s] fireTaggedWork succeeded"
+ "[%s] kicking off healthappd tagged work for sleep results notification..."
+ "[%{public}@] handling biome event for scheduled"
+ "v16@?0@\"<HKSPClient>\"8"
- "HDSPMacReadyProvider"
- "[%s] fireOnce failed with error %@"
- "[%s] fireOnce succeeded"
- "[%s] kicking off background generation..."
- "[%{public}@] ignoring biome event for scheduled"
- "v16@?0@\"<HDSPSleepNotificationPublisher><HDSPEnvironmentAware>\"8"
- "v16@?0@\"<HKSPSleepClient>\"8"
- "v16@?0@\"BMUserFocusModeComputed\"8"

```
