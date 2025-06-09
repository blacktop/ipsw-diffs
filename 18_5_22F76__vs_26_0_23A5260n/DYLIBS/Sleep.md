## Sleep

> `/System/Library/PrivateFrameworks/Sleep.framework/Sleep`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0x58e48
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x72f4
-  __TEXT.__const: 0x1b0
+6074.1.2.4.0
+  __TEXT.__text: 0x58c10
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0x733c
+  __TEXT.__const: 0x250
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__cstring: 0x48db
+  __TEXT.__cstring: 0x493f
   __TEXT.__gcc_except_tab: 0x8dc
-  __TEXT.__oslogstring: 0x4459
-  __TEXT.__unwind_info: 0x1ae0
+  __TEXT.__oslogstring: 0x4306
+  __TEXT.__unwind_info: 0x1b70
   __TEXT.__objc_classname: 0xf0e
-  __TEXT.__objc_methname: 0x111e5
-  __TEXT.__objc_methtype: 0x253b
-  __TEXT.__objc_stubs: 0xa4a0
-  __DATA_CONST.__got: 0x518
-  __DATA_CONST.__const: 0x2b10
+  __TEXT.__objc_methname: 0x11347
+  __TEXT.__objc_methtype: 0x2549
+  __TEXT.__objc_stubs: 0xa520
+  __DATA_CONST.__got: 0x520
+  __DATA_CONST.__const: 0x2b20
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3760
+  __DATA_CONST.__objc_selrefs: 0x3798
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x270
   __DATA_CONST.__objc_arraydata: 0x98
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x4f40
-  __AUTH_CONST.__objc_const: 0xbc68
+  __AUTH_CONST.__cfstring: 0x4fa0
+  __AUTH_CONST.__objc_const: 0xbc98
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x5d4
-  __DATA.__data: 0x1508
-  __DATA.__common: 0x10
+  __AUTH.__objc_data: 0x870
+  __DATA.__objc_ivar: 0x5d8
+  __DATA.__data: 0x14a0
   __DATA_DIRTY.__objc_ivar: 0x64
-  __DATA_DIRTY.__objc_data: 0x1d60
+  __DATA_DIRTY.__objc_data: 0x1540
   __DATA_DIRTY.__bss: 0x128
   __DATA_DIRTY.__common: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
-  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoPreferencesSync.framework/NanoPreferencesSync
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AFA79E75-9079-31E2-9563-35E4A33D8642
-  Functions: 2690
-  Symbols:   8902
-  CStrings:  4722
+  UUID: 92555963-8155-3D72-99DE-59D267E31F4C
+  Functions: 2695
+  Symbols:   8925
+  CStrings:  4733
 
Symbols:
+ -[HKSPAlarmConfiguration snoozeDuration]
+ -[HKSPMutableAlarmConfiguration setSnoozeDuration:]
+ -[HKSPMutableAlarmConfiguration snoozeDuration]
+ -[HKSPSleepStore _shouldNotifyObserversForClientIdentifier:]
+ -[HKSPSleepStore _updateAndNotifyForChangedSleepEventRecord:clientIdentifier:]
+ -[HKSPSleepStore _updateAndNotifyForChangedSleepMode:]
+ -[HKSPSleepStore _updateAndNotifyForChangedSleepSchedule:clientIdentifier:]
+ -[HKSPSleepStore _updateAndNotifyForChangedSleepScheduleState:]
+ -[HKSPSleepStore _updateAndNotifyForChangedSleepSettings:clientIdentifier:]
+ -[HKSPSleepStore _updateAndNotifyForSleepEvent:]
+ -[HKSPSleepWidgetManager initWithTimelineControllers:relevanceController:timelineScheduler:]
+ GCC_except_table1
+ _.str.289
+ _.str.301
+ _.str.312
+ _.str.313
+ _.str.325
+ _.str.326
+ _.str.390
+ _HKCreateSerialDispatchQueue
+ _HKFeatureAvailabilityContextOnboardingInitiation
+ _HKSPAlarmSnoozeDurationKey
+ _HKSPAlarmSnoozeDurationMinutesDefault
+ _HKSPAlarmSnoozeDurationMinutesMaximum
+ _HKSPAlarmSnoozeDurationMinutesMinimum
+ _HKSPAlarmSnoozeDurationMinutesStep
+ _OBJC_IVAR_$_HKSPAlarmConfiguration._snoozeDuration
+ ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.290
+ ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.291
+ ___39-[HKSPSleepStore _confirmAwakeOnServer]_block_invoke.485
+ ___39-[HKSPXPCConnectionProvider connection]_block_invoke.303
+ ___40-[HKSPDiagnostics _registerStateHandler]_block_invoke.291
+ ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke.299
+ ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke_2.300
+ ___43-[HKSPSleepStore _dismissSleepLockOnServer]_block_invoke.487
+ ___45-[HKSPSleepStore _dismissGoodMorningOnServer]_block_invoke.486
+ ___46-[HKSPSleepStore _clearWidgetOverrideOnServer]_block_invoke.495
+ ___46-[HKSPSleepWidgetManager invalidateRelevances]_block_invoke.315
+ ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke.319
+ ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke_2.321
+ ___47-[HKSPSleepStore _setSleepModeOnServer:reason:]_block_invoke.483
+ ___48-[HKSPSleepStore _getSleepModeFromServerDoSync:]_block_invoke.355
+ ___49-[HKSPSleepStore _sleepAlarmWasModifiedOnServer:]_block_invoke.490
+ ___50-[HKSPSleepWidgetManager reloadWidgetsWithReason:]_block_invoke.312
+ ___52-[HKSPSleepStore _getSleepScheduleFromServerDoSync:]_block_invoke.343
+ ___52-[HKSPSleepStore _getSleepSettingsFromServerDoSync:]_block_invoke.348
+ ___55-[HKSPSleepStore _getSleepEventRecordFromServerDoSync:]_block_invoke.350
+ ___55-[HKSPSleepStore _getSleepWidgetStateFromServerDoSync:]_block_invoke.360
+ ___57-[HKSPSleepStore _getSleepScheduleModelFromServerDoSync:]_block_invoke.352
+ ___57-[HKSPSleepStore _getSleepScheduleStateFromServerDoSync:]_block_invoke.362
+ ___59-[HKSPSleepStore _publishWakeUpResultsNotificationOnServer]_block_invoke.497
+ ___59-[HKSPSleepStore _setWidgetOverrideStateOnServerWithState:]_block_invoke.494
+ ___60-[HKSPSleepStore _saveCurrentSleepScheduleOnServer:options:]_block_invoke.363
+ ___60-[HKSPSleepStore _saveCurrentSleepSettingsOnServer:options:]_block_invoke.386
+ ___63-[HKSPSleepStore _saveCurrentSleepEventRecordOnServer:options:]_block_invoke.482
+ ___63-[HKSPSleepStore _sleepAlarmWasDismissedOnDateOnServer:source:]_block_invoke.488
+ ___64-[HKSPSleepStore _sleepAlarmWasSnoozedUntilDateOnServer:source:]_block_invoke.489
+ ___64-[HKSPXPCConnectionListener listener:shouldAcceptNewConnection:]_block_invoke.293
+ ___70-[HKSPSleepStore _publishNotificationOnServerWithIdentifier:userInfo:]_block_invoke.492
+ ___72-[HKSPSleepStore _setLockScreenOverrideStateOnServerWithState:userInfo:]_block_invoke.493
+ ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.292
+ ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.297
+ ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke_2.299
+ ___87-[HKSPDNDConfigurationService modeConfigurationService:didReceiveAvailableModesUpdate:]_block_invoke.304
+ ___block_literal_global.292
+ ___block_literal_global.294
+ ___block_literal_global.301
+ ___block_literal_global.305
+ ___block_literal_global.306
+ ___block_literal_global.311
+ ___block_literal_global.312
+ ___block_literal_global.316
+ ___block_literal_global.318
+ ___block_literal_global.324
+ ___block_literal_global.326
+ ___block_literal_global.328
+ ___block_literal_global.335
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.358
+ ___block_literal_global.382
+ ___block_literal_global.393
+ ___block_literal_global.421
+ ___block_literal_global.557
+ ___block_literal_global.559
+ _objc_msgSend$_updateAndNotifyForChangedSleepEventRecord:clientIdentifier:
+ _objc_msgSend$_updateAndNotifyForChangedSleepMode:
+ _objc_msgSend$_updateAndNotifyForChangedSleepSchedule:clientIdentifier:
+ _objc_msgSend$_updateAndNotifyForChangedSleepScheduleState:
+ _objc_msgSend$_updateAndNotifyForChangedSleepSettings:clientIdentifier:
+ _objc_msgSend$_updateAndNotifyForSleepEvent:
+ _objc_msgSend$appendTimeInterval:withName:decomposeUnits:
+ _objc_msgSend$canConnectToSystemMachService
+ _objc_msgSend$initWithTimelineControllers:relevanceController:timelineScheduler:
+ _objc_msgSend$removeObserver:name:object:
+ _objc_msgSend$setSnoozeDuration:
+ _objc_msgSend$snoozeDuration
- -[HKSPAlarmConfiguration playOptions]
- -[HKSPSleepStoreExportedObject _mergeExternalSleepEventRecordChange:clientIdentifier:]
- -[HKSPSleepStoreExportedObject _mergeExternalSleepScheduleChange:clientIdentifier:]
- -[HKSPSleepStoreExportedObject _mergeExternalSleepSettingsChange:clientIdentifier:]
- -[HKSPSleepStoreExportedObject _shouldNotifyObserversForClientIdentifier:]
- _.str.27
- _.str.28
- _.str.286
- _.str.298
- _.str.322
- _.str.323
- _.str.387
- _HKSPCanResolveChangesToObject
- ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.287
- ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.288
- ___39-[HKSPSleepStore _confirmAwakeOnServer]_block_invoke.482
- ___39-[HKSPXPCConnectionProvider connection]_block_invoke.300
- ___40-[HKSPDiagnostics _registerStateHandler]_block_invoke.288
- ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke.296
- ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke_2.297
- ___43-[HKSPSleepStore _dismissSleepLockOnServer]_block_invoke.484
- ___45-[HKSPSleepStore _dismissGoodMorningOnServer]_block_invoke.483
- ___46-[HKSPSleepStore _clearWidgetOverrideOnServer]_block_invoke.492
- ___46-[HKSPSleepWidgetManager invalidateRelevances]_block_invoke.312
- ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke.316
- ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke_2.318
- ___47-[HKSPSleepStore _setSleepModeOnServer:reason:]_block_invoke.480
- ___48-[HKSPSleepStore _getSleepModeFromServerDoSync:]_block_invoke.352
- ___49-[HKSPSleepStore _sleepAlarmWasModifiedOnServer:]_block_invoke.487
- ___50-[HKSPSleepWidgetManager reloadWidgetsWithReason:]_block_invoke.309
- ___52-[HKSPSleepStore _getSleepScheduleFromServerDoSync:]_block_invoke.340
- ___52-[HKSPSleepStore _getSleepSettingsFromServerDoSync:]_block_invoke.345
- ___55-[HKSPSleepStore _getSleepEventRecordFromServerDoSync:]_block_invoke.347
- ___55-[HKSPSleepStore _getSleepWidgetStateFromServerDoSync:]_block_invoke.357
- ___57-[HKSPSleepStore _getSleepScheduleModelFromServerDoSync:]_block_invoke.349
- ___57-[HKSPSleepStore _getSleepScheduleStateFromServerDoSync:]_block_invoke.359
- ___59-[HKSPSleepStore _publishWakeUpResultsNotificationOnServer]_block_invoke.494
- ___59-[HKSPSleepStore _setWidgetOverrideStateOnServerWithState:]_block_invoke.491
- ___60-[HKSPSleepStore _saveCurrentSleepScheduleOnServer:options:]_block_invoke.360
- ___60-[HKSPSleepStore _saveCurrentSleepSettingsOnServer:options:]_block_invoke.383
- ___63-[HKSPSleepStore _saveCurrentSleepEventRecordOnServer:options:]_block_invoke.479
- ___63-[HKSPSleepStore _sleepAlarmWasDismissedOnDateOnServer:source:]_block_invoke.485
- ___64-[HKSPSleepStore _sleepAlarmWasSnoozedUntilDateOnServer:source:]_block_invoke.486
- ___64-[HKSPXPCConnectionListener listener:shouldAcceptNewConnection:]_block_invoke.290
- ___70-[HKSPSleepStore _publishNotificationOnServerWithIdentifier:userInfo:]_block_invoke.489
- ___72-[HKSPSleepStore _setLockScreenOverrideStateOnServerWithState:userInfo:]_block_invoke.490
- ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.289
- ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.294
- ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke_2.296
- ___87-[HKSPDNDConfigurationService modeConfigurationService:didReceiveAvailableModesUpdate:]_block_invoke.301
- ___block_literal_global.12
- ___block_literal_global.15
- ___block_literal_global.18
- ___block_literal_global.288
- ___block_literal_global.289
- ___block_literal_global.295
- ___block_literal_global.302
- ___block_literal_global.308
- ___block_literal_global.309
- ___block_literal_global.313
- ___block_literal_global.315
- ___block_literal_global.321
- ___block_literal_global.322
- ___block_literal_global.323
- ___block_literal_global.332
- ___block_literal_global.349
- ___block_literal_global.355
- ___block_literal_global.376
- ___block_literal_global.390
- ___block_literal_global.418
- ___block_literal_global.50
- ___block_literal_global.554
- ___block_literal_global.556
- ___block_literal_global.65
- ___block_literal_global.67
- _objc_msgSend$_mergeExternalSleepEventRecordChange:clientIdentifier:
- _objc_msgSend$_mergeExternalSleepScheduleChange:clientIdentifier:
- _objc_msgSend$_mergeExternalSleepSettingsChange:clientIdentifier:
- _objc_msgSend$cachedSleepEventRecord
- _objc_msgSend$cachedSleepSchedule
- _objc_msgSend$cachedSleepSettings
- _objc_msgSend$lavender
- _objc_msgSend$setLastModifiedDate:
CStrings:
+ "B32@0:8q16@24"
+ "C"
+ "HKSPAlarmSnoozeDuration"
+ "HKSPFeatureAvailabilityStoreObserver"
+ "Migrating snooze duration"
+ "Td,R,N,V_snoozeDuration"
+ "_snoozeDuration"
+ "_updateAndNotifyForChangedSleepEventRecord:clientIdentifier:"
+ "_updateAndNotifyForChangedSleepMode:"
+ "_updateAndNotifyForChangedSleepSchedule:clientIdentifier:"
+ "_updateAndNotifyForChangedSleepScheduleState:"
+ "_updateAndNotifyForChangedSleepSettings:clientIdentifier:"
+ "_updateAndNotifyForSleepEvent:"
+ "appendTimeInterval:withName:decomposeUnits:"
+ "canConnectToSystemMachService"
+ "initWithTimelineControllers:relevanceController:timelineScheduler:"
+ "removeObserver:name:object:"
+ "setSnoozeDuration:"
+ "settings-navigation://com.apple.Settings.ScreenTime/CONTENT_PRIVACY/ALLOWED_APPS"
+ "snoozeDuration"
- "%{public}@ received unexpected nil sleepSchedule"
- "3"
- "[HKSPObject] can't resolve %{public}@"
- "[HKSPObject] changed value == saved value, allowing update"
- "[HKSPObject] checking relationship change..."
- "[HKSPObject] original value == saved value, allowing update"
- "[HKSPObject] property: %{public}@, original value: %{public}@, changed value: %{public}@, saved value: %{public}@"
- "_mergeExternalSleepEventRecordChange:clientIdentifier:"
- "_mergeExternalSleepScheduleChange:clientIdentifier:"
- "_mergeExternalSleepSettingsChange:clientIdentifier:"
- "lavender"
- "playOptions"
- "prefs:root=SCREEN_TIME&path=CONTENT_PRIVACY/ALLOWED_APPS"

```
