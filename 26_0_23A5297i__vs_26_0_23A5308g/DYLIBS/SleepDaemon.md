## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

-6100.0.0.0.0
-  __TEXT.__text: 0x7a364
-  __TEXT.__auth_stubs: 0xc20
-  __TEXT.__objc_methlist: 0x8a5c
-  __TEXT.__const: 0x1d8
-  __TEXT.__cstring: 0x2b01
-  __TEXT.__oslogstring: 0xb8ba
+6105.0.0.0.0
+  __TEXT.__text: 0x7b244
+  __TEXT.__auth_stubs: 0xe40
+  __TEXT.__objc_methlist: 0x8a8c
+  __TEXT.__const: 0x238
+  __TEXT.__swift5_typeref: 0x20
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__oslogstring: 0xb92c
+  __TEXT.__cstring: 0x2b30
+  __TEXT.__constg_swiftt: 0x38
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_types: 0x4
   __TEXT.__gcc_except_tab: 0x1244
-  __TEXT.__unwind_info: 0x21a0
+  __TEXT.__unwind_info: 0x21f8
   __TEXT.__objc_classname: 0x1fad
-  __TEXT.__objc_methname: 0x11ab7
+  __TEXT.__objc_methname: 0x11ad3
   __TEXT.__objc_methtype: 0x36d5
   __TEXT.__objc_stubs: 0xd580
-  __DATA_CONST.__got: 0xa78
-  __DATA_CONST.__const: 0x2478
-  __DATA_CONST.__objc_classlist: 0x540
+  __DATA_CONST.__got: 0xa98
+  __DATA_CONST.__const: 0x24c0
+  __DATA_CONST.__objc_classlist: 0x548
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x328
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3d50
+  __DATA_CONST.__objc_selrefs: 0x3d58
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x360
-  __AUTH_CONST.__auth_got: 0x620
-  __AUTH_CONST.__const: 0xce0
+  __AUTH_CONST.__auth_got: 0x730
+  __AUTH_CONST.__const: 0xd30
   __AUTH_CONST.__cfstring: 0x1ec0
-  __AUTH_CONST.__objc_const: 0x10228
+  __AUTH_CONST.__objc_const: 0x10270
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xc80
+  __AUTH.__objc_data: 0xd30
+  __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x5a4
-  __DATA.__data: 0x25f0
+  __DATA.__data: 0x2610
+  __DATA.__common: 0x18
   __DATA_DIRTY.__objc_ivar: 0xd0
   __DATA_DIRTY.__objc_data: 0x2800
   __DATA_DIRTY.__bss: 0xb0

   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
+  - /System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer

   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58FDB44E-4B83-3472-9688-2E3B769EC046
-  Functions: 2969
-  Symbols:   10680
-  CStrings:  4825
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  UUID: 444D09CE-2B0A-3A5A-8B2D-C9F6D38ED13F
+  Functions: 2996
+  Symbols:   10738
+  CStrings:  4832
 
Symbols:
+ _OBJC_CLASS_$_HDSPOrchestrationClientWrapper
+ _OBJC_METACLASS_$_HDSPOrchestrationClientWrapper
+ __CLASS_METHODS_HDSPOrchestrationClientWrapper
+ __DATA_HDSPOrchestrationClientWrapper
+ __INSTANCE_METHODS_HDSPOrchestrationClientWrapper
+ __METACLASS_DATA_HDSPOrchestrationClientWrapper
+ __OBJC_$_PROP_LIST_HDSPSleepLockScreenAssertionManager.411
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
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_SleepDaemon
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_SleepDaemon
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_SleepDaemon
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_SleepDaemon
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_SleepDaemon
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_SleepDaemon
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_SleepDaemon
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_SleepDaemon
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_SleepDaemon
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_opt_self
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _symbolic So8NSObjectC
+ _symbolic _____ 11SleepDaemon26OrchestrationClientWrapperC
+ _symbolic _____XDXMT 11SleepDaemon26OrchestrationClientWrapperC
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
+ "HDSPOrchestrationClientWrapper"
+ "[%s] fireOnce failed with error %@"
+ "[%s] fireOnce succeeded"
+ "[%s] kicking off background generation..."
+ "kickOffBackgroundGeneration"

```
