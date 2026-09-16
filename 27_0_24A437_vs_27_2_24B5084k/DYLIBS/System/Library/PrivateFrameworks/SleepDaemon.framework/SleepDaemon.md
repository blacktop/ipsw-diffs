## SleepDaemon

> `/System/Library/PrivateFrameworks/SleepDaemon.framework/SleepDaemon`

```diff

-7027.0.72.2.7
-  __TEXT.__text: 0x76584
-  __TEXT.__objc_methlist: 0x7ed4
-  __TEXT.__const: 0x3c0
-  __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__swift5_capture: 0x158
-  __TEXT.__oslogstring: 0xb075
-  __TEXT.__constg_swiftt: 0x130
-  __TEXT.__swift5_fieldmd: 0x14c
-  __TEXT.__swift5_builtin: 0x14
+7027.1.36.2.7
+  __TEXT.__text: 0x6b9c4
+  __TEXT.__objc_methlist: 0x77a4
+  __TEXT.__const: 0x328
+  __TEXT.__oslogstring: 0x9bfe
+  __TEXT.__cstring: 0x217d
+  __TEXT.__constg_swiftt: 0x104
+  __TEXT.__swift5_typeref: 0x1c1
   __TEXT.__swift5_reflstr: 0x28b
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__cstring: 0x253c
-  __TEXT.__gcc_except_tab: 0xa34
-  __TEXT.__unwind_info: 0x2978
+  __TEXT.__swift5_fieldmd: 0x13c
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_types: 0x10
+  __TEXT.__swift5_capture: 0x148
+  __TEXT.__gcc_except_tab: 0x844
+  __TEXT.__unwind_info: 0x26c0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x20e8
-  __DATA_CONST.__objc_classlist: 0x4f0
-  __DATA_CONST.__objc_catlist: 0x48
+  __DATA_CONST.__const: 0x1c58
+  __DATA_CONST.__objc_classlist: 0x4a8
+  __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x338
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38a0
-  __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x318
-  __DATA_CONST.__got: 0xba8
-  __AUTH_CONST.__const: 0x1048
-  __AUTH_CONST.__cfstring: 0x1aa0
-  __AUTH_CONST.__objc_const: 0xf220
+  __DATA_CONST.__objc_selrefs: 0x3420
+  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x2e8
+  __DATA_CONST.__got: 0xad0
+  __AUTH_CONST.__const: 0xf60
+  __AUTH_CONST.__cfstring: 0x16c0
+  __AUTH_CONST.__objc_const: 0xe4a0
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0xc88
-  __AUTH.__objc_data: 0x8c0
-  __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x514
-  __DATA.__data: 0x2560
-  __DATA.__common: 0x18
+  __AUTH_CONST.__auth_got: 0xbf8
+  __AUTH.__objc_data: 0x770
+  __DATA.__objc_ivar: 0x4b8
+  __DATA.__data: 0x2350
   __DATA_DIRTY.__objc_ivar: 0xb4
-  __DATA_DIRTY.__objc_data: 0x2b00
+  __DATA_DIRTY.__objc_data: 0x2920
   __DATA_DIRTY.__data: 0x2e8
   __DATA_DIRTY.__common: 0x28
   __DATA_DIRTY.__bss: 0xa0

   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreDuetContext.framework/CoreDuetContext
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
-  - /System/Library/PrivateFrameworks/HealthAppServices.framework/HealthAppServices
   - /System/Library/PrivateFrameworks/HealthPlatformFoundation.framework/HealthPlatformFoundation
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /System/Library/PrivateFrameworks/SleepHealth.framework/SleepHealth
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
-  - /usr/lib/swift/libswiftMetal.dylib
-  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2930
-  Symbols:   6991
-  CStrings:  1191
+  Functions: 2734
+  Symbols:   6492
+  CStrings:  1045
 
Symbols:
+ +[HDSPHealthStoreProvider _initializedLocalDeviceHealthStore]
+ -[HDSPEnvironment initWithBehavior:sleepStorageProvider:sleepScheduleModelManagerProvider:sleepSchedulerProvider:sleepServerProvider:sleepCoordinatorProvider:sleepModeManagerProvider:goodMorningAlertManagerProvider:chargingReminderManagerProvider:wakeDetectionManagerProvider:actionManagerProvider:sleepAlarmManagerProvider:healthStoreProvider:contextStoreManagerProvider:biomeManagerProvider:migrationManagerProvider:notificationManagerProvider:notificationListenerProvider:sleepLockScreenManagerProvider:sleepWidgetManagerProvider:idsServiceManagerProvider:diagnosticsProvider:systemMonitorProvider:assertionManager:preferenceChangeListenerProvider:sensitiveUIMonitorProvider:analyticsManagerProvider:userDefaults:fileManager:currentDateProvider:defaultCallbackScheduler:mutexGenerator:]
+ -[HDSPHealthStoreProvider .cxx_destruct]
+ -[HDSPHealthStoreProvider healthStore]
+ -[HDSPHealthStoreProvider initWithHealthStore:]
+ -[HDSPHealthStoreProvider initWithLocalDeviceHealthStore]
+ -[HDSPProcessStateManager monitoredProcessIdentifiers]
+ GCC_except_table33
+ GCC_except_table44
+ _HKSPAnalyticsActivePairedWatchProductType
+ _OBJC_CLASS_$_HDSPHealthStoreProvider
+ _OBJC_CLASS_$_HKHealthStore
+ _OBJC_IVAR_$_HDSPHealthStoreProvider._healthStore
+ _OBJC_METACLASS_$_HDSPHealthStoreProvider
+ __OBJC_$_CLASS_METHODS_HDSPHealthStoreProvider
+ __OBJC_$_CLASS_PROP_LIST_HKSPObject
+ __OBJC_$_INSTANCE_METHODS_HDSPHealthStoreProvider
+ __OBJC_$_INSTANCE_VARIABLES_HDSPHealthStoreProvider
+ __OBJC_$_PROP_LIST_HDSPHealthStoreProvider
+ __OBJC_$_PROP_LIST_HKSPObject
+ __OBJC_$_PROTOCOL_CLASS_METHODS_HKSPObject
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_HKSPObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSPApplicationWorkspaceMonitorProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKSPObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSMutableCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HKSPObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDSPApplicationWorkspaceMonitorProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HKSPObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSMutableCopying
+ __OBJC_$_PROTOCOL_REFS_HDSPApplicationWorkspaceMonitorProviding
+ __OBJC_$_PROTOCOL_REFS_HKSPObject
+ __OBJC_CLASS_RO_$_HDSPHealthStoreProvider
+ __OBJC_LABEL_PROTOCOL_$_HDSPApplicationWorkspaceMonitorProviding
+ __OBJC_LABEL_PROTOCOL_$_HKSPObject
+ __OBJC_LABEL_PROTOCOL_$_NSMutableCopying
+ __OBJC_METACLASS_RO_$_HDSPHealthStoreProvider
+ __OBJC_PROTOCOL_$_HDSPApplicationWorkspaceMonitorProviding
+ __OBJC_PROTOCOL_$_HKSPObject
+ __OBJC_PROTOCOL_$_NSMutableCopying
+ ___block_descriptor_40_e8_32w_e19_v16?0"NAPromise"8lw32l8
+ ___block_descriptor_64_e8_32s40s48bs_e23_v16?0"HKSPXPCClient"8ls32l8s48l8s40l8
+ _objc_msgSend$_initializedLocalDeviceHealthStore
+ _objc_msgSend$alarmManager
+ _objc_msgSend$initWithBehavior:sleepStorageProvider:sleepScheduleModelManagerProvider:sleepSchedulerProvider:sleepServerProvider:sleepCoordinatorProvider:sleepModeManagerProvider:goodMorningAlertManagerProvider:chargingReminderManagerProvider:wakeDetectionManagerProvider:actionManagerProvider:sleepAlarmManagerProvider:healthStoreProvider:contextStoreManagerProvider:biomeManagerProvider:migrationManagerProvider:notificationManagerProvider:notificationListenerProvider:sleepLockScreenManagerProvider:sleepWidgetManagerProvider:idsServiceManagerProvider:diagnosticsProvider:systemMonitorProvider:assertionManager:preferenceChangeListenerProvider:sensitiveUIMonitorProvider:analyticsManagerProvider:userDefaults:fileManager:currentDateProvider:defaultCallbackScheduler:mutexGenerator:
+ _objc_msgSend$initWithHealthStore:
+ _objc_msgSend$setSleepScoreAlgorithmVersion:
+ _objc_msgSend$setSourceBundleIdentifier:
+ _swift_dynamicCastObjCProtocolConditional
- +[BMPublisherOptions(Sleep) hdsp_optionsForDateInterval:]
- +[BMPublisherOptions(Sleep) hdsp_optionsForDateInterval:reversed:]
- +[HDSPBiomeInBedDetector hoursOfSleepForResult:]
- +[HDSPBiomeInBedDetector inBedDetectorWithProvider:]
- +[HDSPBiomeInBedDetector inBedDetector]
- +[HDSPCDInBedDetector hoursOfSleepForResult:]
- +[HDSPCDInBedDetector inBedDetector]
- +[HDSPEnvironment _sleepTrackingManagerProviderForBehavior:]
- +[HDSPSleepSession sleepSessionWithDateInterval:sleepIntervals:endReason:metadata:requiresFirstUnlock:]
- +[HDSPSleepSession supportsSecureCoding]
- +[HDSPSleepSessionInterval sleepSessionIntervalWithInterval:type:]
- +[HDSPSleepSessionInterval supportsSecureCoding]
- +[HDSPSleepTrackingManager platformSpecificTrackerWithEnvironment:]
- +[HKCategorySample(HDSPSleep) hdsp_categorySampleForSleepSessionInterval:metadata:]
- +[UNNotificationSound(HDSPSleep) hdsp_wakeUpResultsSound]
- -[HDSPBiomeInBedDetectionProvider findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]
- -[HDSPBiomeInBedDetectionProvider findLastTimeDeviceWasPluggedInDuringInterval:error:]
- -[HDSPBiomeInBedDetectionProvider findMotionTerminusDuringInterval:latest:error:]
- -[HDSPBiomeInBedDetectionProvider findTimesDeviceWasUnlockedDuringInterval:error:]
- -[HDSPBiomeInBedDetector .cxx_destruct]
- -[HDSPBiomeInBedDetector detectInBedTimesDuringInterval:]
- -[HDSPBiomeInBedDetector detectInBedTimesHelperDuringInterval:]
- -[HDSPBiomeInBedDetector findLastTimeDeviceWasLockedDuringInterval:error:]
- -[HDSPBiomeInBedDetector findLastTimeDeviceWasUnlockedDuringInterval:error:]
- -[HDSPBiomeInBedDetector findLatestEndOfMovementDuringInterval:error:]
- -[HDSPBiomeInBedDetector initWithProvider:]
- -[HDSPBiomeInBedDetector lockedTimesDuringInterval:error:]
- -[HDSPCDInBedDetector detectInBedTimesDuringInterval:]
- -[HDSPEnvironment initWithBehavior:sleepStorageProvider:sleepScheduleModelManagerProvider:sleepSchedulerProvider:sleepServerProvider:sleepCoordinatorProvider:sleepModeManagerProvider:sleepTrackingManagerProvider:goodMorningAlertManagerProvider:chargingReminderManagerProvider:wakeDetectionManagerProvider:actionManagerProvider:sleepAlarmManagerProvider:healthStoreProvider:contextStoreManagerProvider:biomeManagerProvider:migrationManagerProvider:notificationManagerProvider:notificationListenerProvider:sleepLockScreenManagerProvider:sleepWidgetManagerProvider:idsServiceManagerProvider:diagnosticsProvider:systemMonitorProvider:assertionManager:preferenceChangeListenerProvider:sensitiveUIMonitorProvider:analyticsManagerProvider:userDefaults:fileManager:currentDateProvider:defaultCallbackScheduler:mutexGenerator:]
- -[HDSPEnvironment sleepTrackingManager]
- -[HDSPOrchestrationCenter .cxx_destruct]
- -[HDSPOrchestrationCenter environmentDidBecomeReady:]
- -[HDSPOrchestrationCenter environment]
- -[HDSPOrchestrationCenter initWithEnvironment:]
- -[HDSPOrchestrationCenter publishNotificationForEvent:]
- -[HDSPOrchestrationCenter tearDownNotificationForEventIdentifier:]
- -[HDSPOrchestrationCenter tearDownNotifications]
- -[HDSPSleepSession .cxx_destruct]
- -[HDSPSleepSession descriptionBuilderWithMultilinePrefix:]
- -[HDSPSleepSession descriptionWithMultilinePrefix:]
- -[HDSPSleepSession description]
- -[HDSPSleepSession encodeWithCoder:]
- -[HDSPSleepSession endReason]
- -[HDSPSleepSession initWithCoder:]
- -[HDSPSleepSession initWithDateInterval:sleepIntervals:endReason:metadata:requiresFirstUnlock:]
- -[HDSPSleepSession interval]
- -[HDSPSleepSession isEqual:]
- -[HDSPSleepSession metadata]
- -[HDSPSleepSession requiresFirstUnlock]
- -[HDSPSleepSession sleepIntervals]
- -[HDSPSleepSession succinctDescriptionBuilder]
- -[HDSPSleepSession succinctDescription]
- -[HDSPSleepSessionInterval .cxx_destruct]
- -[HDSPSleepSessionInterval descriptionBuilderWithMultilinePrefix:]
- -[HDSPSleepSessionInterval descriptionWithMultilinePrefix:]
- -[HDSPSleepSessionInterval description]
- -[HDSPSleepSessionInterval encodeWithCoder:]
- -[HDSPSleepSessionInterval initWithCoder:]
- -[HDSPSleepSessionInterval initWithInterval:type:]
- -[HDSPSleepSessionInterval interval]
- -[HDSPSleepSessionInterval isEqual:]
- -[HDSPSleepSessionInterval succinctDescriptionBuilder]
- -[HDSPSleepSessionInterval succinctDescription]
- -[HDSPSleepSessionInterval type]
- -[HDSPSleepSessionManager .cxx_destruct]
- -[HDSPSleepSessionManager _hasUnprocessedSessions]
- -[HDSPSleepSessionManager _locked_savePendingSessions]
- -[HDSPSleepSessionManager _unprocessedSessions]
- -[HDSPSleepSessionManager _waitForFirstUnlock]
- -[HDSPSleepSessionManager _withLock:]
- -[HDSPSleepSessionManager archiveSession:]
- -[HDSPSleepSessionManager delegate]
- -[HDSPSleepSessionManager deviceHasBeenUnlocked]
- -[HDSPSleepSessionManager deviceUnlockManager]
- -[HDSPSleepSessionManager fileManager]
- -[HDSPSleepSessionManager initWithEnvironment:]
- -[HDSPSleepSessionManager initWithEnvironment:persistence:]
- -[HDSPSleepSessionManager persistence]
- -[HDSPSleepSessionManager removeSessionDataFile]
- -[HDSPSleepSessionManager savePendingSessions]
- -[HDSPSleepSessionManager saveSession:]
- -[HDSPSleepSessionManager sessionLock]
- -[HDSPSleepSessionManager setDelegate:]
- -[HDSPSleepSessionManager sleepTracker:didEndSession:reason:]
- -[HDSPSleepSessionManager sleepTrackerDidStartSession:]
- -[HDSPSleepSessionManager startSession]
- -[HDSPSleepSessionManager stopSession]
- -[HDSPSleepTrackingManager .cxx_destruct]
- -[HDSPSleepTrackingManager addObserver:]
- -[HDSPSleepTrackingManager environmentDidBecomeReady:]
- -[HDSPSleepTrackingManager environmentWillBecomeReady:]
- -[HDSPSleepTrackingManager environment]
- -[HDSPSleepTrackingManager initWithEnvironment:]
- -[HDSPSleepTrackingManager initWithEnvironment:sleepSessionManager:sleepTracker:]
- -[HDSPSleepTrackingManager removeObserver:]
- -[HDSPSleepTrackingManager sleepSessionManager:didSaveArchivedSessions:]
- -[HDSPSleepTrackingManager sleepSessionManager:didSaveSession:]
- -[HDSPSleepTrackingManager sleepSessionManager:requestsProcessedSessionForSession:]
- -[HDSPSleepTrackingManager sleepSessionManagerDidFinishSession:]
- -[HDSPSleepTrackingManager sleepSessionManager]
- -[HDSPSleepTrackingManager sleepSessionObservers]
- -[HDSPSleepTrackingManager sleepTracker]
- -[HDSPTimeInBedTracker .cxx_destruct]
- -[HDSPTimeInBedTracker _compareWithCoreDuetInBedDetectionForInterval:]
- -[HDSPTimeInBedTracker _computeSessionMetadataForInterval:]
- -[HDSPTimeInBedTracker _computeSleepSessionStartBeforeDate:]
- -[HDSPTimeInBedTracker _createSleepSessionWithEndDate:endReason:]
- -[HDSPTimeInBedTracker _endSleepSessionWithReason:]
- -[HDSPTimeInBedTracker _logDetections:]
- -[HDSPTimeInBedTracker computeSleepIntervalsForInterval:]
- -[HDSPTimeInBedTracker delegate]
- -[HDSPTimeInBedTracker environmentWillBecomeReady:]
- -[HDSPTimeInBedTracker environment]
- -[HDSPTimeInBedTracker inBedDetector]
- -[HDSPTimeInBedTracker initWithEnvironment:]
- -[HDSPTimeInBedTracker isTimeInBedTrackingEnabled]
- -[HDSPTimeInBedTracker processedSessionForSession:]
- -[HDSPTimeInBedTracker setDelegate:]
- -[HDSPTimeInBedTracker sleepIntervalScheduler]
- -[HDSPTimeInBedTracker sleepScheduleModel]
- -[HDSPTimeInBedTracker sleepScheduleStateDidChange:previousState:reason:]
- -[HDSPUserNotificationCenter _recordSentUserNotificationRequest:]
- -[HDSPUserNotificationCenter _sleepScoreResultsContentWithUserInfo:]
- -[HDSPWatchOnWristMonitor isWristDetectEnabled]
- -[HDSPWatchOnWristMonitor wristDetectionSettingManagerDidObserveWristDetectChange:]
- -[HDSPWatchOnWristMonitor wristDetectionSettingsManager]
- -[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]
- -[HKSleepHealthStore(HDSPSleep) hdsp_startSession]
- -[HKSleepHealthStore(HDSPSleep) hdsp_stopSession]
- GCC_except_table46
- GCC_except_table61
- _HDSPSleepSessionEndReasonDescription
- _HDSPSleepSessionIntervalTypeDescription
- _HDSPSleepSessionIntervalTypeIsAsleep
- _HDSPSleepSessionStartReasonDescription
- _HKCategoryTypeIdentifierSleepAnalysis
- _HKMetadataKeyTimeZone
- _HKSHSleepScoreResultsNotificationEventIdentifier
- _HKSPSleepEventIdentifierSleepScoreResultsNotification
- _HKSPSleepScoreIntroductionCategory
- _HKSPSleepScoreResultsCategory
- _HKSPSleepScoreResultsIdentifier
- _OBJC_CLASS_$_BMPublisherOptions
- _OBJC_CLASS_$_BSEqualsBuilder
- _OBJC_CLASS_$_CMMotionActivityManager
- _OBJC_CLASS_$_HDSPBiomeInBedDetectionProvider
- _OBJC_CLASS_$_HDSPBiomeInBedDetector
- _OBJC_CLASS_$_HDSPCDInBedDetector
- _OBJC_CLASS_$_HDSPOrchestrationCenter
- _OBJC_CLASS_$_HDSPOrchestrationClientWrapper
- _OBJC_CLASS_$_HDSPSleepSession
- _OBJC_CLASS_$_HDSPSleepSessionInterval
- _OBJC_CLASS_$_HDSPSleepSessionManager
- _OBJC_CLASS_$_HDSPSleepTrackingManager
- _OBJC_CLASS_$_HDSPTimeInBedTracker
- _OBJC_CLASS_$_HKCategorySample
- _OBJC_CLASS_$_HKDevice
- _OBJC_CLASS_$_HKObjectType
- _OBJC_CLASS_$_HKSHSleepScoreResultsNotification
- _OBJC_CLASS_$_HKSPAnalyticsWindDownEvent
- _OBJC_CLASS_$_HKSPAnalyticsWindDownEventData
- _OBJC_CLASS_$_HKSPHealthStoreProvider
- _OBJC_CLASS_$_HKSleepHealthStore
- _OBJC_CLASS_$_HKWristDetectionSettingManager
- _OBJC_CLASS_$_NSOperationQueue
- _OBJC_CLASS_$__CDInBedDetector
- _OBJC_EHTYPE_$_NSException
- _OBJC_IVAR_$_HDSPBiomeInBedDetector._biomeProvider
- _OBJC_IVAR_$_HDSPEnvironment._sleepTrackingManager
- _OBJC_IVAR_$_HDSPOrchestrationCenter._environment
- _OBJC_IVAR_$_HDSPSleepSession._endReason
- _OBJC_IVAR_$_HDSPSleepSession._interval
- _OBJC_IVAR_$_HDSPSleepSession._metadata
- _OBJC_IVAR_$_HDSPSleepSession._requiresFirstUnlock
- _OBJC_IVAR_$_HDSPSleepSession._sleepIntervals
- _OBJC_IVAR_$_HDSPSleepSessionInterval._interval
- _OBJC_IVAR_$_HDSPSleepSessionInterval._type
- _OBJC_IVAR_$_HDSPSleepSessionManager._delegate
- _OBJC_IVAR_$_HDSPSleepSessionManager._deviceUnlockManager
- _OBJC_IVAR_$_HDSPSleepSessionManager._fileManager
- _OBJC_IVAR_$_HDSPSleepSessionManager._persistence
- _OBJC_IVAR_$_HDSPSleepSessionManager._sessionLock
- _OBJC_IVAR_$_HDSPSleepTrackingManager._environment
- _OBJC_IVAR_$_HDSPSleepTrackingManager._sleepSessionManager
- _OBJC_IVAR_$_HDSPSleepTrackingManager._sleepSessionObservers
- _OBJC_IVAR_$_HDSPSleepTrackingManager._sleepTracker
- _OBJC_IVAR_$_HDSPTimeInBedTracker._delegate
- _OBJC_IVAR_$_HDSPTimeInBedTracker._environment
- _OBJC_IVAR_$_HDSPTimeInBedTracker._inBedDetector
- _OBJC_IVAR_$_HDSPTimeInBedTracker._sleepIntervalScheduler
- _OBJC_IVAR_$_HDSPWatchOnWristMonitor._wristDetectionSettingsManager
- _OBJC_METACLASS_$_HDSPBiomeInBedDetectionProvider
- _OBJC_METACLASS_$_HDSPBiomeInBedDetector
- _OBJC_METACLASS_$_HDSPCDInBedDetector
- _OBJC_METACLASS_$_HDSPOrchestrationCenter
- _OBJC_METACLASS_$_HDSPOrchestrationClientWrapper
- _OBJC_METACLASS_$_HDSPSleepSession
- _OBJC_METACLASS_$_HDSPSleepSessionInterval
- _OBJC_METACLASS_$_HDSPSleepSessionManager
- _OBJC_METACLASS_$_HDSPSleepTrackingManager
- _OBJC_METACLASS_$_HDSPTimeInBedTracker
- __CLASS_METHODS_HDSPOrchestrationClientWrapper
- __DATA_HDSPOrchestrationClientWrapper
- __HKPrivateMetadataKeySleepAlarmUserSetBedtime
- __HKPrivateMetadataKeySleepAlarmUserWakeTime
- __INSTANCE_METHODS_HDSPOrchestrationClientWrapper
- __METACLASS_DATA_HDSPOrchestrationClientWrapper
- __OBJC_$_CATEGORY_BMPublisherOptions_$_Sleep
- __OBJC_$_CATEGORY_CLASS_METHODS_BMPublisherOptions_$_Sleep
- __OBJC_$_CATEGORY_CLASS_METHODS_HKCategorySample_$_HDSPSleep
- __OBJC_$_CATEGORY_HKCategorySample_$_HDSPSleep
- __OBJC_$_CATEGORY_HKSleepHealthStore_$_HDSPSleep
- __OBJC_$_CATEGORY_INSTANCE_METHODS_HKSleepHealthStore_$_HDSPSleep
- __OBJC_$_CLASS_METHODS_HDSPBiomeInBedDetector
- __OBJC_$_CLASS_METHODS_HDSPCDInBedDetector
- __OBJC_$_CLASS_METHODS_HDSPSleepSession
- __OBJC_$_CLASS_METHODS_HDSPSleepSessionInterval
- __OBJC_$_CLASS_METHODS_HDSPSleepTrackingManager
- __OBJC_$_CLASS_PROP_LIST_HDSPSleepSession
- __OBJC_$_CLASS_PROP_LIST_HDSPSleepSessionInterval
- __OBJC_$_INSTANCE_METHODS_HDSPBiomeInBedDetectionProvider
- __OBJC_$_INSTANCE_METHODS_HDSPBiomeInBedDetector
- __OBJC_$_INSTANCE_METHODS_HDSPCDInBedDetector
- __OBJC_$_INSTANCE_METHODS_HDSPOrchestrationCenter
- __OBJC_$_INSTANCE_METHODS_HDSPSleepSession
- __OBJC_$_INSTANCE_METHODS_HDSPSleepSessionInterval
- __OBJC_$_INSTANCE_METHODS_HDSPSleepSessionManager
- __OBJC_$_INSTANCE_METHODS_HDSPSleepTrackingManager
- __OBJC_$_INSTANCE_METHODS_HDSPTimeInBedTracker
- __OBJC_$_INSTANCE_VARIABLES_HDSPBiomeInBedDetector
- __OBJC_$_INSTANCE_VARIABLES_HDSPOrchestrationCenter
- __OBJC_$_INSTANCE_VARIABLES_HDSPSleepSession
- __OBJC_$_INSTANCE_VARIABLES_HDSPSleepSessionInterval
- __OBJC_$_INSTANCE_VARIABLES_HDSPSleepSessionManager
- __OBJC_$_INSTANCE_VARIABLES_HDSPSleepTrackingManager
- __OBJC_$_INSTANCE_VARIABLES_HDSPTimeInBedTracker
- __OBJC_$_PROP_LIST_HDSPOrchestrationCenter
- __OBJC_$_PROP_LIST_HDSPSleepSession
- __OBJC_$_PROP_LIST_HDSPSleepSessionInterval
- __OBJC_$_PROP_LIST_HDSPSleepSessionManager
- __OBJC_$_PROP_LIST_HDSPSleepTracker
- __OBJC_$_PROP_LIST_HDSPSleepTrackingManager
- __OBJC_$_PROP_LIST_HDSPTimeInBedTracker
- __OBJC_$_PROP_LIST_HKSleepHealthStore_$_HDSPSleep
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSPBiomeInBedDetectionProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSPDeviceUnlockObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSPInBedDetector
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSPSleepSessionManagerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSPSleepSessionPersistence
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSPSleepTracker
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDSPSleepTrackerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_HKWristDetectionSettingManagerObserver
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDSPSleepSessionManagerDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDSPSleepTracker
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HDSPWatchOnWristObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDSPBiomeInBedDetectionProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDSPDeviceUnlockObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDSPInBedDetector
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDSPSleepSessionManagerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDSPSleepSessionPersistence
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDSPSleepTracker
- __OBJC_$_PROTOCOL_METHOD_TYPES_HDSPSleepTrackerDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_HKWristDetectionSettingManagerObserver
- __OBJC_$_PROTOCOL_REFS_HDSPDeviceUnlockObserver
- __OBJC_$_PROTOCOL_REFS_HDSPSleepSessionManagerDelegate
- __OBJC_$_PROTOCOL_REFS_HDSPSleepSessionPersistence
- __OBJC_$_PROTOCOL_REFS_HDSPSleepTracker
- __OBJC_$_PROTOCOL_REFS_HDSPSleepTrackerDelegate
- __OBJC_CATEGORY_PROTOCOLS_$_HKSleepHealthStore_$_HDSPSleep
- __OBJC_CLASS_PROTOCOLS_$_HDSPBiomeInBedDetectionProvider
- __OBJC_CLASS_PROTOCOLS_$_HDSPBiomeInBedDetector
- __OBJC_CLASS_PROTOCOLS_$_HDSPCDInBedDetector
- __OBJC_CLASS_PROTOCOLS_$_HDSPOrchestrationCenter
- __OBJC_CLASS_PROTOCOLS_$_HDSPSleepSession
- __OBJC_CLASS_PROTOCOLS_$_HDSPSleepSessionInterval
- __OBJC_CLASS_PROTOCOLS_$_HDSPSleepSessionManager
- __OBJC_CLASS_PROTOCOLS_$_HDSPSleepTrackingManager
- __OBJC_CLASS_PROTOCOLS_$_HDSPTimeInBedTracker
- __OBJC_CLASS_PROTOCOLS_$_HDSPWatchOnWristMonitor
- __OBJC_CLASS_RO_$_HDSPBiomeInBedDetectionProvider
- __OBJC_CLASS_RO_$_HDSPBiomeInBedDetector
- __OBJC_CLASS_RO_$_HDSPCDInBedDetector
- __OBJC_CLASS_RO_$_HDSPOrchestrationCenter
- __OBJC_CLASS_RO_$_HDSPSleepSession
- __OBJC_CLASS_RO_$_HDSPSleepSessionInterval
- __OBJC_CLASS_RO_$_HDSPSleepSessionManager
- __OBJC_CLASS_RO_$_HDSPSleepTrackingManager
- __OBJC_CLASS_RO_$_HDSPTimeInBedTracker
- __OBJC_LABEL_PROTOCOL_$_HDSPBiomeInBedDetectionProviding
- __OBJC_LABEL_PROTOCOL_$_HDSPDeviceUnlockObserver
- __OBJC_LABEL_PROTOCOL_$_HDSPInBedDetector
- __OBJC_LABEL_PROTOCOL_$_HDSPSleepSessionManagerDelegate
- __OBJC_LABEL_PROTOCOL_$_HDSPSleepSessionPersistence
- __OBJC_LABEL_PROTOCOL_$_HDSPSleepTracker
- __OBJC_LABEL_PROTOCOL_$_HDSPSleepTrackerDelegate
- __OBJC_LABEL_PROTOCOL_$_HKWristDetectionSettingManagerObserver
- __OBJC_METACLASS_RO_$_HDSPBiomeInBedDetectionProvider
- __OBJC_METACLASS_RO_$_HDSPBiomeInBedDetector
- __OBJC_METACLASS_RO_$_HDSPCDInBedDetector
- __OBJC_METACLASS_RO_$_HDSPOrchestrationCenter
- __OBJC_METACLASS_RO_$_HDSPSleepSession
- __OBJC_METACLASS_RO_$_HDSPSleepSessionInterval
- __OBJC_METACLASS_RO_$_HDSPSleepSessionManager
- __OBJC_METACLASS_RO_$_HDSPSleepTrackingManager
- __OBJC_METACLASS_RO_$_HDSPTimeInBedTracker
- __OBJC_PROTOCOL_$_HDSPBiomeInBedDetectionProviding
- __OBJC_PROTOCOL_$_HDSPDeviceUnlockObserver
- __OBJC_PROTOCOL_$_HDSPInBedDetector
- __OBJC_PROTOCOL_$_HDSPSleepSessionManagerDelegate
- __OBJC_PROTOCOL_$_HDSPSleepSessionPersistence
- __OBJC_PROTOCOL_$_HDSPSleepTracker
- __OBJC_PROTOCOL_$_HDSPSleepTrackerDelegate
- __OBJC_PROTOCOL_$_HKWristDetectionSettingManagerObserver
- ___28-[HDSPSleepSession isEqual:]_block_invoke
- ___28-[HDSPSleepSession isEqual:]_block_invoke_2
- ___28-[HDSPSleepSession isEqual:]_block_invoke_3
- ___28-[HDSPSleepSession isEqual:]_block_invoke_4
- ___28-[HDSPSleepSession isEqual:]_block_invoke_5
- ___36-[HDSPSleepSessionInterval isEqual:]_block_invoke
- ___36-[HDSPSleepSessionInterval isEqual:]_block_invoke_2
- ___39-[HDSPSleepSessionManager saveSession:]_block_invoke
- ___39-[HDSPTimeInBedTracker _logDetections:]_block_invoke
- ___46-[HDSPSleepSessionManager savePendingSessions]_block_invoke
- ___51-[HDSPTimeInBedTracker processedSessionForSession:]_block_invoke
- ___54-[HDSPCDInBedDetector detectInBedTimesDuringInterval:]_block_invoke
- ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke
- ___54-[HDSPSleepSessionManager _locked_savePendingSessions]_block_invoke_2
- ___54-[HKSleepHealthStore(HDSPSleep) hdsp_persistSessions:]_block_invoke
- ___57-[HDSPBiomeInBedDetector detectInBedTimesDuringInterval:]_block_invoke
- ___57-[HDSPTimeInBedTracker computeSleepIntervalsForInterval:]_block_invoke
- ___57-[HDSPTimeInBedTracker computeSleepIntervalsForInterval:]_block_invoke_2
- ___57-[HDSPTimeInBedTracker computeSleepIntervalsForInterval:]_block_invoke_3
- ___57-[HDSPTimeInBedTracker computeSleepIntervalsForInterval:]_block_invoke_4
- ___60+[HDSPEnvironment _sleepTrackingManagerProviderForBehavior:]_block_invoke
- ___61-[HDSPSleepSessionManager sleepTracker:didEndSession:reason:]_block_invoke
- ___63-[HDSPSleepTrackingManager sleepSessionManager:didSaveSession:]_block_invoke
- ___65-[HDSPUserNotificationCenter _recordSentUserNotificationRequest:]_block_invoke
- ___70-[HDSPTimeInBedTracker _compareWithCoreDuetInBedDetectionForInterval:]_block_invoke
- ___72-[HDSPSleepTrackingManager sleepSessionManager:didSaveArchivedSessions:]_block_invoke
- ___81-[HDSPBiomeInBedDetectionProvider findMotionTerminusDuringInterval:latest:error:]_block_invoke
- ___82-[HDSPBiomeInBedDetectionProvider findTimesDeviceWasUnlockedDuringInterval:error:]_block_invoke
- ___82-[HDSPBiomeInBedDetectionProvider findTimesDeviceWasUnlockedDuringInterval:error:]_block_invoke_2
- ___82-[HDSPBiomeInBedDetectionProvider findTimesDeviceWasUnlockedDuringInterval:error:]_block_invoke_3
- ___83-[HDSPWatchOnWristMonitor wristDetectionSettingManagerDidObserveWristDetectChange:]_block_invoke
- ___86-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceWasPluggedInDuringInterval:error:]_block_invoke
- ___86-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceWasPluggedInDuringInterval:error:]_block_invoke_2
- ___86-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceWasPluggedInDuringInterval:error:]_block_invoke_3
- ___94-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]_block_invoke
- ___94-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]_block_invoke_2
- ___94-[HDSPBiomeInBedDetectionProvider findLastTimeDeviceLockChangedDuringInterval:isLocked:error:]_block_invoke_3
- ___NSDictionary0__struct
- ___block_descriptor_32_e22_B16?0"BMStoreEvent"8l
- ___block_descriptor_32_e36_v16?0"<HDSPWatchOnWristObserver>"8l
- ___block_descriptor_32_e43_"NSDateInterval"16?0"_CDInBedDetection"8l
- ___block_descriptor_32_e50_"HDSPSleepSessionInterval"16?0"NSDateInterval"8l
- ___block_descriptor_32_e50_"NSArray"24?0"NSMutableArray"8"BMStoreEvent"16l
- ___block_descriptor_32_e51_"HDSPSleepTrackingManager"16?0"HDSPEnvironment"8l
- ___block_descriptor_33_e22_B16?0"BMStoreEvent"8l
- ___block_descriptor_40_e8_32r_e17_v16?0"NSArray"8lr32l8
- ___block_descriptor_40_e8_32r_e22_B16?0"BMStoreEvent"8lr32l8
- ___block_descriptor_40_e8_32r_e23_v16?0"BPSCompletion"8lr32l8
- ___block_descriptor_40_e8_32s_e14_"NSArray"8?0ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
- ___block_descriptor_40_e8_32s_e21_"NSDateInterval"8?0ls32l8
- ___block_descriptor_40_e8_32s_e24_v16?0"NSDateInterval"8ls32l8
- ___block_descriptor_40_e8_32s_e26_16?0"HDSPSleepSession"8ls32l8
- ___block_descriptor_40_e8_32s_e36_"NAFuture"16?0"HDSPSleepSession"8ls32l8
- ___block_descriptor_40_e8_32s_e36_v16?0"<HDSPSleepSessionObserver>"8ls32l8
- ___block_descriptor_40_e8_32s_e5_B8?0ls32l8
- ___block_descriptor_40_e8_32s_e5_Q8?0ls32l8
- ___block_descriptor_48_e8_32s40s_e19_v16?0"NAPromise"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e27_"NAFuture"16?0"NSArray"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e29_v24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s40s_e8_v16?08ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e19_v16?0"NAPromise"8lw40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e20_v24?08"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e23_v16?0"HKSPXPCClient"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r56r_e29_v24?0"NSArray"8"NSError"16ls32l8r48l8r56l8s40l8
- __swiftEmptyDictionarySingleton
- __swift_FORCE_LOAD_$_swiftMetal
- __swift_FORCE_LOAD_$_swiftMetal_$_SleepDaemon
- __swift_FORCE_LOAD_$_swiftOSLog
- __swift_FORCE_LOAD_$_swiftOSLog_$_SleepDaemon
- __swift_FORCE_LOAD_$_swiftsimd
- __swift_FORCE_LOAD_$_swiftsimd_$_SleepDaemon
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_begin_catch
- _objc_end_catch
- _objc_exception_rethrow
- _objc_msgSend$Device
- _objc_msgSend$PluggedIn
- _objc_msgSend$Power
- _objc_msgSend$ScreenLocked
- _objc_msgSend$_compareWithCoreDuetInBedDetectionForInterval:
- _objc_msgSend$_computeSessionMetadataForInterval:
- _objc_msgSend$_computeSleepSessionStartBeforeDate:
- _objc_msgSend$_createSleepSessionWithEndDate:endReason:
- _objc_msgSend$_endSleepSessionWithReason:
- _objc_msgSend$_hasUnprocessedSessions
- _objc_msgSend$_locked_savePendingSessions
- _objc_msgSend$_logDetections:
- _objc_msgSend$_recordSentUserNotificationRequest:
- _objc_msgSend$_sleepScoreResultsContentWithUserInfo:
- _objc_msgSend$_sleepTrackingManagerProviderForBehavior:
- _objc_msgSend$_unprocessedSessions
- _objc_msgSend$_waitForFirstUnlock
- _objc_msgSend$activePairedWatchProductType
- _objc_msgSend$analyticsStore
- _objc_msgSend$appendBool:counterpart:
- _objc_msgSend$appendObject:counterpart:
- _objc_msgSend$appendUnsignedInteger:counterpart:
- _objc_msgSend$appendUnsignedInteger:withName:
- _objc_msgSend$archiveSession:
- _objc_msgSend$archivedSleepSessionsSaved:
- _objc_msgSend$array
- _objc_msgSend$authorizationStatusForType:
- _objc_msgSend$body
- _objc_msgSend$builderWithObject:ofExpectedClass:
- _objc_msgSend$cancelAllOperations
- _objc_msgSend$categorySampleWithType:value:startDate:endDate:device:metadata:
- _objc_msgSend$categoryTypeForIdentifier:
- _objc_msgSend$combineAllFutures:
- _objc_msgSend$compare:
- _objc_msgSend$computeSleepIntervalsForInterval:
- _objc_msgSend$confidence
- _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
- _objc_msgSend$decodeIntegerForKey:
- _objc_msgSend$decodeObjectOfClasses:forKey:
- _objc_msgSend$detectInBedBetweenBedtimeDate:wakupDate:error:
- _objc_msgSend$detectInBedTimesDuringInterval:
- _objc_msgSend$detectInBedTimesHelperDuringInterval:
- _objc_msgSend$duration
- _objc_msgSend$encodeInteger:forKey:
- _objc_msgSend$encodedData
- _objc_msgSend$endReason
- _objc_msgSend$fileManager
- _objc_msgSend$filterWithIsIncluded:
- _objc_msgSend$findLastTimeDeviceLockChangedDuringInterval:isLocked:error:
- _objc_msgSend$findLastTimeDeviceWasLockedDuringInterval:error:
- _objc_msgSend$findLastTimeDeviceWasPluggedInDuringInterval:error:
- _objc_msgSend$findLastTimeDeviceWasUnlockedDuringInterval:error:
- _objc_msgSend$findLatestEndOfMovementDuringInterval:error:
- _objc_msgSend$findMotionTerminusDuringInterval:latest:error:
- _objc_msgSend$findTimesDeviceWasUnlockedDuringInterval:error:
- _objc_msgSend$finishDecoding
- _objc_msgSend$finishEncoding
- _objc_msgSend$futureWithBlock:scheduler:
- _objc_msgSend$futureWithError:
- _objc_msgSend$hdsp_categorySampleForSleepSessionInterval:metadata:
- _objc_msgSend$hdsp_optionsForDateInterval:
- _objc_msgSend$hdsp_optionsForDateInterval:reversed:
- _objc_msgSend$hdsp_persistSessions:
- _objc_msgSend$hdsp_startSession
- _objc_msgSend$hdsp_stopSession
- _objc_msgSend$hdsp_wakeUpResultsSound
- _objc_msgSend$hk_map:
- _objc_msgSend$hkspDataForCacheFileWithName:
- _objc_msgSend$hkspFileWithNameExistsInCache:
- _objc_msgSend$hkspRemoveFileWithNameFromCache:error:
- _objc_msgSend$hkspWriteData:toCacheFileWithName:error:
- _objc_msgSend$hksp_analyticsUserDefaults
- _objc_msgSend$hksp_dateNearestMatchingComponents:
- _objc_msgSend$hksp_supportsSleepTracking
- _objc_msgSend$hoursOfSleepForResult:
- _objc_msgSend$inBedDetector
- _objc_msgSend$inBedDetectorWithProvider:
- _objc_msgSend$initForReadingFromData:error:
- _objc_msgSend$initRequiringSecureCoding:
- _objc_msgSend$initWithBehavior:sleepStorageProvider:sleepScheduleModelManagerProvider:sleepSchedulerProvider:sleepServerProvider:sleepCoordinatorProvider:sleepModeManagerProvider:sleepTrackingManagerProvider:goodMorningAlertManagerProvider:chargingReminderManagerProvider:wakeDetectionManagerProvider:actionManagerProvider:sleepAlarmManagerProvider:healthStoreProvider:contextStoreManagerProvider:biomeManagerProvider:migrationManagerProvider:notificationManagerProvider:notificationListenerProvider:sleepLockScreenManagerProvider:sleepWidgetManagerProvider:idsServiceManagerProvider:diagnosticsProvider:systemMonitorProvider:assertionManager:preferenceChangeListenerProvider:sensitiveUIMonitorProvider:analyticsManagerProvider:userDefaults:fileManager:currentDateProvider:defaultCallbackScheduler:mutexGenerator:
- _objc_msgSend$initWithDateInterval:sleepIntervals:endReason:metadata:requiresFirstUnlock:
- _objc_msgSend$initWithEnvironment:persistence:
- _objc_msgSend$initWithEnvironment:sleepSessionManager:sleepTracker:
- _objc_msgSend$initWithInterval:type:
- _objc_msgSend$initWithProvider:
- _objc_msgSend$initWithStartDate:endDate:maxEvents:lastN:reversed:
- _objc_msgSend$initWithUserInfo:
- _objc_msgSend$initWithWindDownEventData:watchProductType:weeksSinceOnboarded:
- _objc_msgSend$interval
- _objc_msgSend$isActivityAvailable
- _objc_msgSend$isEqual
- _objc_msgSend$isIntroduction
- _objc_msgSend$isTimeInBedTrackingEnabled
- _objc_msgSend$isWristDetectEnabled
- _objc_msgSend$kickOffBackgroundGeneration
- _objc_msgSend$localDevice
- _objc_msgSend$lockedTimesDuringInterval:error:
- _objc_msgSend$markAllActionsAsCollected
- _objc_msgSend$maximumAllowedDuration
- _objc_msgSend$metadata
- _objc_msgSend$na_genericError
- _objc_msgSend$notificationUserInfo
- _objc_msgSend$objectEnumerator
- _objc_msgSend$platformSpecificTrackerWithEnvironment:
- _objc_msgSend$previousSessionFinished
- _objc_msgSend$processedSessionForSession:
- _objc_msgSend$pruneExpiredWindDownActionDataBefore:
- _objc_msgSend$publisherWithUseCase:options:
- _objc_msgSend$queryActivityStartingFromDate:toDate:toQueue:withHandler:
- _objc_msgSend$reduceWithInitial:nextPartialResult:
- _objc_msgSend$registerObserver:
- _objc_msgSend$removeAllWindDownActionsBeforeMorningIndex:
- _objc_msgSend$removeSessionDataFile
- _objc_msgSend$requiresFirstUnlock
- _objc_msgSend$reverseObjectEnumerator
- _objc_msgSend$savePendingSessions
- _objc_msgSend$saveSession:
- _objc_msgSend$saveSleepTrackingSamples:completion:
- _objc_msgSend$scheduler
- _objc_msgSend$setInteractedWithWindDownLast24Hrs:
- _objc_msgSend$setLastWakeUpResultsIntroductionNotificationVersionSent:
- _objc_msgSend$setLastWakeUpResultsIntroductionNotificationVersionSentDate:
- _objc_msgSend$setName:
- _objc_msgSend$setWeeksSinceOnboardedWindDownActions:
- _objc_msgSend$sinkWithCompletion:shouldContinue:
- _objc_msgSend$sleepHealthStore
- _objc_msgSend$sleepIntervals
- _objc_msgSend$sleepSessionIntervalWithInterval:type:
- _objc_msgSend$sleepSessionManager:didSaveArchivedSessions:
- _objc_msgSend$sleepSessionManager:didSaveSession:
- _objc_msgSend$sleepSessionManager:requestsProcessedSessionForSession:
- _objc_msgSend$sleepSessionManagerDidFinishSession:
- _objc_msgSend$sleepSessionSaved:
- _objc_msgSend$sleepSessionWithDateInterval:sleepIntervals:endReason:metadata:requiresFirstUnlock:
- _objc_msgSend$sleepTracker:didEndSession:reason:
- _objc_msgSend$startSession
- _objc_msgSend$startSleepTrackingSession
- _objc_msgSend$stationary
- _objc_msgSend$stopSession
- _objc_msgSend$stopSleepTrackingSession
- _objc_msgSend$timeIntervalSinceReferenceDate
- _objc_msgSend$timestamp
- _objc_msgSend$title
- _objc_msgSend$uncollectedWindDownActions
- _objc_msgSend$unregisterObserver:
- _objc_msgSend$wasUsed
- _objc_msgSend$windDownActionsAfterMorningIndex:
- _objc_msgSend$wristDetectEnabledDidChange
- _objc_terminate
- _swift_isUniquelyReferenced_nonNull_bridgeObject
- _symbolic _____ 11SleepDaemon26OrchestrationClientWrapperC
- _symbolic _____XDXMT 11SleepDaemon26OrchestrationClientWrapperC
CStrings:
+ "[%{public}@] refusing to set sleep mode: %ld"
+ "com.apple.private.health.localdevice"
+ "\xf0\xf0Q"
- "@\"HDSPSleepSessionInterval\"16@?0@\"NSDateInterval\"8"
- "@\"HDSPSleepTrackingManager\"16@?0@\"HDSPEnvironment\"8"
- "@\"NAFuture\"16@?0@\"HDSPSleepSession\"8"
- "@\"NAFuture\"16@?0@\"NSArray\"8"
- "@\"NSArray\"24@?0@\"NSMutableArray\"8@\"BMStoreEvent\"16"
- "@\"NSArray\"8@?0"
- "@\"NSDateInterval\"16@?0@\"_CDInBedDetection\"8"
- "@\"NSDateInterval\"8@?0"
- "@\"NSDictionary\"8@?0"
- "@16@?0@\"HDSPSleepSession\"8"
- "ActivityDetectedAfterWakeUp"
- "AppLaunchedAfterWakeUp"
- "Awake"
- "B16@?0@\"BMStoreEvent\"8"
- "B8@?0"
- "Cancel"
- "CoreSleep"
- "DeepSleep"
- "Error"
- "HDSPUnprocessedSessions"
- "InBed"
- "Internal"
- "Manual"
- "OnCharger"
- "Q8@?0"
- "REMSleep"
- "RequiresFirstUnlock"
- "Scheduled"
- "Sleep interval: %f greater than allowed: %f. Will not be used"
- "SleepSessionDateInterval"
- "SleepSessionEndReason"
- "SleepSessionInterval"
- "SleepSessionMetadata"
- "SleepSessionSleepIntervals"
- "SleepSessionType"
- "SleepSessions.data"
- "TimeOut"
- "UnspecifiedSleep"
- "[%s] fireTaggedWork failed with error %@"
- "[%s] fireTaggedWork succeeded"
- "[%s] kicking off healthappd tagged work for sleep results notification..."
- "[%{public}@] %ld processed sessions"
- "[%{public}@] %ld unprocessed sessions"
- "[%{public}@] Bedtime started less than an hour before end date, not performing further movement based changes on end date."
- "[%{public}@] Cannot create content for sleep score results without valid data: %{public}@"
- "[%{public}@] Detecting in-bed intervals between night start (%@) and end (%@)"
- "[%{public}@] Error finding first start of movement: %@"
- "[%{public}@] Error finding last date device was plugged in between %@ and %@: %@"
- "[%{public}@] Error finding last end of movement: %@"
- "[%{public}@] Error finding last lock date between %@ and %@: %@"
- "[%{public}@] Error identifying locked times between %@ and %@: %@"
- "[%{public}@] Establing night end.."
- "[%{public}@] Establishing final bedtime.."
- "[%{public}@] Establishing night start.."
- "[%{public}@] Final bedtime is %@"
- "[%{public}@] Found %@ in-bed intervals between %@ & %@"
- "[%{public}@] Found %ld activities"
- "[%{public}@] Last lock was %@"
- "[%{public}@] Last motion was %@"
- "[%{public}@] Last plugin was %@"
- "[%{public}@] Limited search for locked events to last lock end %@"
- "[%{public}@] Looking for earliest start of movement between %@ and %@"
- "[%{public}@] Looking for in-bed intervals between %@ and %@"
- "[%{public}@] Looking for last time device was locked between %@ and %@"
- "[%{public}@] Looking for last time device was plugged in between %@ and %@"
- "[%{public}@] Looking for last time device was unlocked between %@ and %@"
- "[%{public}@] Looking for latest end of movement between %@ and %@"
- "[%{public}@] Looking for times device was locked in %@"
- "[%{public}@] Looking for times device was unlocked in between %@ and %@"
- "[%{public}@] Motion activity is not available for in bed detection"
- "[%{public}@] Night end is %@"
- "[%{public}@] Night start is %@"
- "[%{public}@] Querying CoreMotion failed with error: %@"
- "[%{public}@] Querying CoreMotion.."
- "[%{public}@] Timeout during queryActivityStartingFromDate."
- "[%{public}@] Unable to find first start of movement. Falling back to provided end time (%@)."
- "[%{public}@] Unable to find last end of movement. Falling back to provided start time (%@)."
- "[%{public}@] _computeSessionMetadataForInterval: %{public}@"
- "[%{public}@] adding last locked event between %@ and %@"
- "[%{public}@] archiveSession: %{public}@"
- "[%{public}@] archiving session for now"
- "[%{public}@] calculated time in bed hours: %f"
- "[%{public}@] can write session data"
- "[%{public}@] can't write sessions until first unlock"
- "[%{public}@] caught exception %{public}@ when trying to read sessions"
- "[%{public}@] checking auth status"
- "[%{public}@] comparing against _CDInBedDetector..."
- "[%{public}@] computing in bed intervals inside %{public}@"
- "[%{public}@] created %{public}@"
- "[%{public}@] creating HealthKit samples"
- "[%{public}@] deviceHasBeenUnlocked"
- "[%{public}@] didSaveArchivedSessions %{public}@"
- "[%{public}@] didSaveSession %{public}@"
- "[%{public}@] doesn't have write access for HKCategoryTypeIdentifierSleepAnalysis"
- "[%{public}@] ending sleep session with reason %{public}@"
- "[%{public}@] ending time in bed tracking"
- "[%{public}@] failed to detect time-in-bed with error: %{public}@"
- "[%{public}@] failed to remove session data file error %{public}@"
- "[%{public}@] failed to write sessions file with error %{public}@"
- "[%{public}@] finished processing session: %{public}@"
- "[%{public}@] finished saving %lu samples"
- "[%{public}@] found %lu in-bed intervals"
- "[%{public}@] found not locked event between %@ and %@"
- "[%{public}@] inBed [%@ - %@]"
- "[%{public}@] inferring locked event between %@ and %@"
- "[%{public}@] no data found in file %{public}@"
- "[%{public}@] no unlocked events, device was locked between %@ and %@"
- "[%{public}@] no unprocessed sessions to save"
- "[%{public}@] previous occurrence: %{public}@"
- "[%{public}@] processed session has intervals: %@"
- "[%{public}@] processing session: %@"
- "[%{public}@] requestsProcessedSessionForSession %{public}@"
- "[%{public}@] saveSession %{public}@"
- "[%{public}@] saving processed session %{public}@"
- "[%{public}@] saving samples to HealthKit failed with error: %{public}@"
- "[%{public}@] saving session %{public}@ from %{public}@"
- "[%{public}@] saving sessions"
- "[%{public}@] session has nothing to write"
- "[%{public}@] session is ready to write"
- "[%{public}@] session needs additional processing"
- "[%{public}@] skipping session due to missing bedtime or wake time: %@"
- "[%{public}@] sleepSessionManagerDidFinishSession"
- "[%{public}@] starting session"
- "[%{public}@] state changed to wake up (%{public}@)"
- "[%{public}@] stopping session"
- "[%{public}@] there are unprocessed sessions to save"
- "[%{public}@] time in bed tracking disabled"
- "[%{public}@] time in bed tracking feature disabled"
- "[%{public}@] unarchiving failed with error %{public}@"
- "[%{public}@] user set wake time: %{public}@ user set bed time: %{public}@"
- "[%{public}@] using 90 minutes before bedtime %{public}@ as session start"
- "[%{public}@] using bedtime date %{public}@ as session start"
- "[%{public}@] waiting for first unlock"
- "[%{public}@] wristDetectionSettingManagerDidObserveWristDetectChange"
- "[%{public}@] wrote sessions to file %{public}@"
- "[%{public}s] Pruning wind down action data prior to %{public}ld"
- "com.apple.coreduet.inbed.coremotion"
- "com.apple.sleepd.inBedDetection"
- "endReason"
- "interval"
- "requiresFirstUnlock"
- "sleepInterval is nil"
- "sleepIntervalScheduler"
- "sleepIntervals"
- "type"
- "v16@?0@\"<HDSPSleepSessionObserver>\"8"
- "v16@?0@\"<HDSPWatchOnWristObserver>\"8"
- "v16@?0@\"NSDateInterval\"8"
- "\xf0\xf0a"
```
