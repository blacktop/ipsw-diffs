## Sleep

> `/System/Library/PrivateFrameworks/Sleep.framework/Sleep`

```diff

-6093.0.0.0.0
+6100.0.0.0.0
   __TEXT.__text: 0x58ca0
   __TEXT.__auth_stubs: 0x710
   __TEXT.__objc_methlist: 0x7354
   __TEXT.__const: 0x250
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__cstring: 0x497c
+  __TEXT.__cstring: 0x498a
   __TEXT.__gcc_except_tab: 0x8dc
   __TEXT.__oslogstring: 0x4306
   __TEXT.__unwind_info: 0x1c10

   __TEXT.__objc_methtype: 0x2549
   __TEXT.__objc_stubs: 0xa560
   __DATA_CONST.__got: 0x520
-  __DATA_CONST.__const: 0x2b28
+  __DATA_CONST.__const: 0x2b30
   __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1b8

   __DATA_CONST.__objc_arraydata: 0xa0
   __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x4fe0
+  __AUTH_CONST.__cfstring: 0x5000
   __AUTH_CONST.__objc_const: 0xbcc8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D052DA9B-4129-3D0D-8F12-A32EF9C4E861
+  UUID: CA9D4AC3-C787-39C3-8842-AC7382493A7D
   Functions: 2697
-  Symbols:   8933
-  CStrings:  4742
+  Symbols:   8934
+  CStrings:  4744
 
Symbols:
+ _.str.289
+ _.str.301
+ _.str.312
+ _.str.313
+ _.str.325
+ _.str.326
+ _.str.390
+ _HKSPOpenAppAction
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
+ ___46-[HKSPSleepWidgetManager invalidateRelevances]_block_invoke.316
+ ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke.319
+ ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke_2.321
+ ___47-[HKSPSleepStore _setSleepModeOnServer:reason:]_block_invoke.483
+ ___48-[HKSPSleepStore _getSleepModeFromServerDoSync:]_block_invoke.355
+ ___49-[HKSPSleepStore _sleepAlarmWasModifiedOnServer:]_block_invoke.490
+ ___50-[HKSPSleepWidgetManager reloadWidgetsWithReason:]_block_invoke.313
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
+ ___block_literal_global.291
+ ___block_literal_global.292
+ ___block_literal_global.298
+ ___block_literal_global.305
+ ___block_literal_global.311
+ ___block_literal_global.312
+ ___block_literal_global.316
+ ___block_literal_global.318
+ ___block_literal_global.324
+ ___block_literal_global.325
+ ___block_literal_global.326
+ ___block_literal_global.335
+ ___block_literal_global.350
+ ___block_literal_global.352
+ ___block_literal_global.358
+ ___block_literal_global.379
+ ___block_literal_global.393
+ ___block_literal_global.421
+ ___block_literal_global.557
+ ___block_literal_global.559
- _.str.292
- _.str.304
- _.str.315
- _.str.316
- _.str.328
- _.str.329
- _.str.393
- ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.293
- ___38-[HKSPLimitingScheduler scheduleTask:]_block_invoke.294
- ___39-[HKSPSleepStore _confirmAwakeOnServer]_block_invoke.488
- ___39-[HKSPXPCConnectionProvider connection]_block_invoke.306
- ___40-[HKSPDiagnostics _registerStateHandler]_block_invoke.294
- ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke.302
- ___40-[HKSPSleepModeButtonModel setSelected:]_block_invoke_2.303
- ___43-[HKSPSleepStore _dismissSleepLockOnServer]_block_invoke.490
- ___45-[HKSPSleepStore _dismissGoodMorningOnServer]_block_invoke.489
- ___46-[HKSPSleepStore _clearWidgetOverrideOnServer]_block_invoke.498
- ___46-[HKSPSleepWidgetManager invalidateRelevances]_block_invoke.319
- ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke.322
- ___47-[HKSPSleepSchedule allowableRangeForWeekdays:]_block_invoke_2.324
- ___47-[HKSPSleepStore _setSleepModeOnServer:reason:]_block_invoke.486
- ___48-[HKSPSleepStore _getSleepModeFromServerDoSync:]_block_invoke.358
- ___49-[HKSPSleepStore _sleepAlarmWasModifiedOnServer:]_block_invoke.493
- ___50-[HKSPSleepWidgetManager reloadWidgetsWithReason:]_block_invoke.316
- ___52-[HKSPSleepStore _getSleepScheduleFromServerDoSync:]_block_invoke.346
- ___52-[HKSPSleepStore _getSleepSettingsFromServerDoSync:]_block_invoke.351
- ___55-[HKSPSleepStore _getSleepEventRecordFromServerDoSync:]_block_invoke.353
- ___55-[HKSPSleepStore _getSleepWidgetStateFromServerDoSync:]_block_invoke.363
- ___57-[HKSPSleepStore _getSleepScheduleModelFromServerDoSync:]_block_invoke.355
- ___57-[HKSPSleepStore _getSleepScheduleStateFromServerDoSync:]_block_invoke.365
- ___59-[HKSPSleepStore _publishWakeUpResultsNotificationOnServer]_block_invoke.500
- ___59-[HKSPSleepStore _setWidgetOverrideStateOnServerWithState:]_block_invoke.497
- ___60-[HKSPSleepStore _saveCurrentSleepScheduleOnServer:options:]_block_invoke.366
- ___60-[HKSPSleepStore _saveCurrentSleepSettingsOnServer:options:]_block_invoke.389
- ___63-[HKSPSleepStore _saveCurrentSleepEventRecordOnServer:options:]_block_invoke.485
- ___63-[HKSPSleepStore _sleepAlarmWasDismissedOnDateOnServer:source:]_block_invoke.491
- ___64-[HKSPSleepStore _sleepAlarmWasSnoozedUntilDateOnServer:source:]_block_invoke.492
- ___64-[HKSPXPCConnectionListener listener:shouldAcceptNewConnection:]_block_invoke.296
- ___70-[HKSPSleepStore _publishNotificationOnServerWithIdentifier:userInfo:]_block_invoke.495
- ___72-[HKSPSleepStore _setLockScreenOverrideStateOnServerWithState:userInfo:]_block_invoke.496
- ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.295
- ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke.300
- ___76-[HKSPSleepStore(Proactive) suggestedSleepScheduleWithProviders:completion:]_block_invoke_2.302
- ___87-[HKSPDNDConfigurationService modeConfigurationService:didReceiveAvailableModesUpdate:]_block_invoke.307
- ___block_literal_global.295
- ___block_literal_global.304
- ___block_literal_global.308
- ___block_literal_global.309
- ___block_literal_global.314
- ___block_literal_global.315
- ___block_literal_global.319
- ___block_literal_global.321
- ___block_literal_global.327
- ___block_literal_global.329
- ___block_literal_global.331
- ___block_literal_global.338
- ___block_literal_global.353
- ___block_literal_global.355
- ___block_literal_global.361
- ___block_literal_global.385
- ___block_literal_global.396
- ___block_literal_global.424
- ___block_literal_global.560
- ___block_literal_global.562
CStrings:
+ "OpenAppAction"

```
