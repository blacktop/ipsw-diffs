## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/Versions/A/PowerUI`

```diff

-640.0.0.0.0
-  __TEXT.__text: 0xa8b80
+651.100.4.0.0
+  __TEXT.__text: 0xae280
   __TEXT.__auth_stubs: 0x880
-  __TEXT.__objc_methlist: 0x18e78
+  __TEXT.__objc_methlist: 0x19b34
   __TEXT.__const: 0x4f0
-  __TEXT.__cstring: 0xbbaa
-  __TEXT.__oslogstring: 0x6ca3
+  __TEXT.__cstring: 0xbe92
+  __TEXT.__oslogstring: 0x7a86
   __TEXT.__gcc_except_tab: 0xe6c
-  __TEXT.__unwind_info: 0x15e8
-  __TEXT.__objc_classname: 0x90e
-  __TEXT.__objc_methname: 0x39ee4
-  __TEXT.__objc_methtype: 0x373d
-  __TEXT.__objc_stubs: 0xa580
-  __DATA_CONST.__got: 0x3e0
-  __DATA_CONST.__const: 0x488
-  __DATA_CONST.__objc_classlist: 0x288
+  __TEXT.__unwind_info: 0x1708
+  __TEXT.__objc_classname: 0x95c
+  __TEXT.__objc_methname: 0x3a5fe
+  __TEXT.__objc_methtype: 0x37a6
+  __TEXT.__objc_stubs: 0xaa20
+  __DATA_CONST.__got: 0x400
+  __DATA_CONST.__const: 0x468
+  __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x44b0
+  __DATA_CONST.__objc_selrefs: 0x47a8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x268
+  __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x6e70
   __AUTH_CONST.__auth_got: 0x450
   __AUTH_CONST.__const: 0x1540
-  __AUTH_CONST.__cfstring: 0x9f40
-  __AUTH_CONST.__objc_const: 0x32d08
-  __AUTH_CONST.__objc_intobj: 0x798
+  __AUTH_CONST.__cfstring: 0xa300
+  __AUTH_CONST.__objc_const: 0x32448
+  __AUTH_CONST.__objc_intobj: 0x7f8
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x1680
-  __DATA.__objc_ivar: 0x39e4
+  __AUTH.__objc_data: 0x1770
+  __DATA.__objc_ivar: 0x3a40
   __DATA.__data: 0x520
-  __DATA.__bss: 0x190
+  __DATA.__bss: 0x1b8
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/CoreRoutine.framework/Versions/A/CoreRoutine
   - /System/Library/PrivateFrameworks/CoreSuggestions.framework/Versions/A/CoreSuggestions
   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/Versions/A/MobileBluetooth
+  - /System/Library/PrivateFrameworks/MobileStoreDemoCore.framework/Versions/A/MobileStoreDemoCore
   - /System/Library/PrivateFrameworks/OSIntelligence.framework/Versions/A/OSIntelligence
   - /System/Library/PrivateFrameworks/PowerLog.framework/Versions/A/PowerLog
   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/Versions/A/RegulatoryDomain

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6AF3FA68-DA99-3D19-8134-56554209CB37
-  Functions: 8992
-  Symbols:   15436
-  CStrings:  7254
+  UUID: FA11395D-2EF9-37FD-971D-1E0A90A91F0F
+  Functions: 9141
+  Symbols:   15676
+  CStrings:  7451
 
Symbols:
+ +[PowerUIBDCDataManager sharedInstance].cold.1
+ +[PowerUIBatteryMitigationManager sharedManager].cold.1
+ +[PowerUIBrightnessController sharedInstance].cold.1
+ +[PowerUICECGridDataManager cleanIntervalsStringFromDates:withIntervalDuration:]
+ +[PowerUICECManager manager].cold.1
+ +[PowerUICECUtilities deviceWasRestartedWithDefaults:]
+ +[PowerUICECUtilities fetchEstimatedCountryCode]
+ +[PowerUICECUtilities isDemoCECSupported]
+ +[PowerUICECUtilities isDemoCecFlagEnabledForStore]
+ +[PowerUICECUtilities isDemoDevice]
+ +[PowerUICECUtilities isDemoDevice].cold.1
+ +[PowerUICECUtilities isPluggedIntoEligiblePowerSourceWithContext:]
+ +[PowerUICECUtilities isPluggedIntoEligiblePowerSourceWithContext:].cold.1
+ +[PowerUICECUtilities isPluggedIntoEligiblePowerSourceWithContext:].cold.2
+ +[PowerUICECUtilities isPluggedIntoEligiblePowerSourceWithContext:].cold.3
+ +[PowerUICECUtilities log]
+ +[PowerUIChargingController sharedInstance].cold.1
+ +[PowerUIDemoCECManager log]
+ +[PowerUIDemoCECManager manager]
+ +[PowerUIDemoCECManager manager].cold.1
+ +[PowerUIDrainAnalyzer sharedInstance].cold.1
+ +[PowerUIDrainMonitor sharedInstance].cold.1
+ +[PowerUINotificationManager fullChargeDeadlineStringFromDate:].cold.1
+ +[PowerUINotificationManager sharedInstance].cold.1
+ +[PowerUISmartChargeUtilities cachedHistorical80ToFullDuration].cold.1
+ +[PowerUISmartChargeUtilities dateFormatter]
+ +[PowerUISmartChargeUtilities dateFormatter].cold.1
+ +[PowerUISmartChargeUtilities doesTimeOfDayForDate:fallBetweenDate:andDate:].cold.1
+ +[PowerUISmartChargeUtilities isInternalBuild].cold.1
+ -[PowerUICECGridDataForecastEntry .cxx_destruct]
+ -[PowerUICECGridDataForecastEntry description]
+ -[PowerUICECGridDataForecastEntry forecastDate]
+ -[PowerUICECGridDataForecastEntry forecastValue]
+ -[PowerUICECGridDataForecastEntry hash]
+ -[PowerUICECGridDataForecastEntry initWithDate:forecastValue:]
+ -[PowerUICECGridDataForecastEntry init]
+ -[PowerUICECGridDataForecastEntry isEqual:]
+ -[PowerUICECGridDataForecastEntry setForecastDate:]
+ -[PowerUICECGridDataForecastEntry setForecastValue:]
+ -[PowerUICECGridDataManager averageEmissionsOverForecastHorizon:]
+ -[PowerUICECGridDataManager averageEmissionsOverForecastHorizon:].cold.1
+ -[PowerUICECGridDataManager emissionsForTime:overForecastHorizon:]
+ -[PowerUICECGridDataManager emissionsForTime:overForecastHorizon:].cold.1
+ -[PowerUICECGridDataManager emissionsForTime:overForecastHorizon:].cold.2
+ -[PowerUICECGridDataManager enoughVariationForForecast:withMinDifference:]
+ -[PowerUICECGridDataManager forecastFromDefaults]
+ -[PowerUICECGridDataManager intervalDuration]
+ -[PowerUICECGridDataManager isDemoMode]
+ -[PowerUICECGridDataManager lastForecastFetchDate]
+ -[PowerUICECGridDataManager recordForecastInDefaults:]
+ -[PowerUICECGridDataManager setIntervalDuration:]
+ -[PowerUICECGridDataManager setIsDemoMode:]
+ -[PowerUICECGridDataManager setLastForecastFetchDate:]
+ -[PowerUICECGridDataManager setupDemoChargingTimeOverForecastHorizon:withKChargingSegments:]
+ -[PowerUICECGridDataManager storedForecastForDemoAnalyticsWithForecastHorizon:]
+ -[PowerUICECGridDataManager thresholdFromForecast:forChargeTime:].cold.3
+ -[PowerUICECManager dateFormatter].cold.1
+ -[PowerUICECManager defaultDateToDisableUntilGivenDate:].cold.1
+ -[PowerUIDemoCECManager .cxx_destruct]
+ -[PowerUIDemoCECManager chargeHistoryAnalytics]
+ -[PowerUIDemoCECManager chargeHistoryAnalytics].cold.1
+ -[PowerUIDemoCECManager chargingController]
+ -[PowerUIDemoCECManager clearAnalytics]
+ -[PowerUIDemoCECManager context]
+ -[PowerUIDemoCECManager currentPhase]
+ -[PowerUIDemoCECManager currentState]
+ -[PowerUIDemoCECManager debugStatus]
+ -[PowerUIDemoCECManager defaults]
+ -[PowerUIDemoCECManager evaluateEngagement]
+ -[PowerUIDemoCECManager evaluateShouldChargeNow]
+ -[PowerUIDemoCECManager evaluateShouldChargeNow].cold.1
+ -[PowerUIDemoCECManager gridDataManager]
+ -[PowerUIDemoCECManager handleCallback:]
+ -[PowerUIDemoCECManager handleCallback:].cold.1
+ -[PowerUIDemoCECManager handleCallback:].cold.2
+ -[PowerUIDemoCECManager handleCallback:].cold.3
+ -[PowerUIDemoCECManager handleCallback:].cold.4
+ -[PowerUIDemoCECManager handleCallback:].cold.5
+ -[PowerUIDemoCECManager handleDisengagement]
+ -[PowerUIDemoCECManager handleEmergencyCharge]
+ -[PowerUIDemoCECManager handleEngagement]
+ -[PowerUIDemoCECManager handlePauseChargingAboveMaxSOC]
+ -[PowerUIDemoCECManager handlePowerUICECStateChange:withHandler:]
+ -[PowerUIDemoCECManager initWithContextStore:]
+ -[PowerUIDemoCECManager init]
+ -[PowerUIDemoCECManager isChargingPaused]
+ -[PowerUIDemoCECManager isDemoCECEnabled]
+ -[PowerUIDemoCECManager isEnabled]
+ -[PowerUIDemoCECManager isEngaged]
+ -[PowerUIDemoCECManager isInternal]
+ -[PowerUIDemoCECManager lastEngagementCheckDate]
+ -[PowerUIDemoCECManager lastPluggedInDate]
+ -[PowerUIDemoCECManager loadStateFromDefaults]
+ -[PowerUIDemoCECManager loadState]
+ -[PowerUIDemoCECManager log]
+ -[PowerUIDemoCECManager monitorBatteryNotifications]
+ -[PowerUIDemoCECManager monitorBatteryStateOfChargeChange]
+ -[PowerUIDemoCECManager monitorPluggedInChange]
+ -[PowerUIDemoCECManager pauseChargingCheckDate]
+ -[PowerUIDemoCECManager phaseDescriptions]
+ -[PowerUIDemoCECManager pluggedInBatteryLevel]
+ -[PowerUIDemoCECManager queue]
+ -[PowerUIDemoCECManager recordAnalytics]
+ -[PowerUIDemoCECManager recordChargingStateChange:atBatteryLevel:duringCleanInterval:]
+ -[PowerUIDemoCECManager recordEngagementEvaluation:]
+ -[PowerUIDemoCECManager registerTimer:afterTime:withInterval:]
+ -[PowerUIDemoCECManager registerTimer:afterTime:withInterval:].cold.1
+ -[PowerUIDemoCECManager registerTimer]
+ -[PowerUIDemoCECManager resetState]
+ -[PowerUIDemoCECManager sessionEndCECAnalytics]
+ -[PowerUIDemoCECManager sessionEndCECAnalytics].cold.1
+ -[PowerUIDemoCECManager setChargingController:]
+ -[PowerUIDemoCECManager setContext:]
+ -[PowerUIDemoCECManager setCurrentPhase:]
+ -[PowerUIDemoCECManager setCurrentState:]
+ -[PowerUIDemoCECManager setDefaults:]
+ -[PowerUIDemoCECManager setEnabledState:]
+ -[PowerUIDemoCECManager setEnabledState:].cold.1
+ -[PowerUIDemoCECManager setGridDataManager:]
+ -[PowerUIDemoCECManager setIsChargingPaused:]
+ -[PowerUIDemoCECManager setIsDemoCECEnabled:]
+ -[PowerUIDemoCECManager setIsInternal:]
+ -[PowerUIDemoCECManager setLastEngagementCheckDate:]
+ -[PowerUIDemoCECManager setLastPluggedInDate:]
+ -[PowerUIDemoCECManager setLog:]
+ -[PowerUIDemoCECManager setPauseChargingCheckDate:]
+ -[PowerUIDemoCECManager setPhaseDescriptions:]
+ -[PowerUIDemoCECManager setPluggedInBatteryLevel:]
+ -[PowerUIDemoCECManager setQueue:]
+ -[PowerUIDemoCECManager setTimer:]
+ -[PowerUIDemoCECManager shouldEngageDemoCEC]
+ -[PowerUIDemoCECManager shouldReevaluateEngagement]
+ -[PowerUIDemoCECManager shouldReevaluateEngagement].cold.1
+ -[PowerUIDemoCECManager shouldReevaluateEngagement].cold.2
+ -[PowerUIDemoCECManager timer]
+ -[PowerUIDemoCECManager unregisterTimer:]
+ -[PowerUIDemoCECManager unregisterTimer:].cold.1
+ -[PowerUIDemoCECManager updatePhaseFrom:to:]
+ -[PowerUIDesktopModePredictor timeStringFromDate:].cold.1
+ -[PowerUIDrainMonitor disableMitigations]
+ -[PowerUIDrainMonitor enableMitigations]
+ -[PowerUIMLTwoStageModelPredictor timeStringFromDate:].cold.1
+ -[PowerUISmartChargeManager defaultDateToDisableUntilGivenDate:].cold.1
+ -[PowerUISmartChargeManager stringFromDecisionMaker:decisionDate:].cold.1
+ -[PowerUISmartChargeManager stringFromInterval:].cold.1
+ -[PowerUISmartChargeManager timeStringFromDate:].cold.1
+ -[PowerUISmartChargeManagerUnsupported setDesktopMode:withHandler:]
+ GCC_except_table35
+ GCC_except_table41
+ GCC_except_table50
+ GCC_except_table57
+ GCC_except_table61
+ OBJC_IVAR_$_PowerUICECGridDataForecastEntry._forecastDate
+ OBJC_IVAR_$_PowerUICECGridDataForecastEntry._forecastValue
+ OBJC_IVAR_$_PowerUICECGridDataManager._intervalDuration
+ OBJC_IVAR_$_PowerUICECGridDataManager._isDemoMode
+ OBJC_IVAR_$_PowerUICECGridDataManager._lastForecastFetchDate
+ OBJC_IVAR_$_PowerUIDemoCECManager._chargingController
+ OBJC_IVAR_$_PowerUIDemoCECManager._context
+ OBJC_IVAR_$_PowerUIDemoCECManager._currentPhase
+ OBJC_IVAR_$_PowerUIDemoCECManager._currentState
+ OBJC_IVAR_$_PowerUIDemoCECManager._debugStatus
+ OBJC_IVAR_$_PowerUIDemoCECManager._defaults
+ OBJC_IVAR_$_PowerUIDemoCECManager._gridDataManager
+ OBJC_IVAR_$_PowerUIDemoCECManager._isChargingPaused
+ OBJC_IVAR_$_PowerUIDemoCECManager._isDemoCECEnabled
+ OBJC_IVAR_$_PowerUIDemoCECManager._isInternal
+ OBJC_IVAR_$_PowerUIDemoCECManager._lastEngagementCheckDate
+ OBJC_IVAR_$_PowerUIDemoCECManager._lastPluggedInDate
+ OBJC_IVAR_$_PowerUIDemoCECManager._log
+ OBJC_IVAR_$_PowerUIDemoCECManager._pauseChargingCheckDate
+ OBJC_IVAR_$_PowerUIDemoCECManager._phaseDescriptions
+ OBJC_IVAR_$_PowerUIDemoCECManager._pluggedInBatteryLevel
+ OBJC_IVAR_$_PowerUIDemoCECManager._queue
+ OBJC_IVAR_$_PowerUIDemoCECManager._timer
+ _OBJC_CLASS_$_MSDCDemoState
+ _OBJC_CLASS_$_PowerUICECGridDataForecastEntry
+ _OBJC_CLASS_$_PowerUICECUtilities
+ _OBJC_CLASS_$_PowerUIDemoCECManager
+ _OBJC_METACLASS_$_PowerUICECGridDataForecastEntry
+ _OBJC_METACLASS_$_PowerUICECUtilities
+ _OBJC_METACLASS_$_PowerUIDemoCECManager
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.595
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.606
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.613
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.618
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.622
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.631
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.633
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.640
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.647
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.649
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.651
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.653
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.660
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.660.cold.1
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.665
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.665.cold.1
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.619
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.625
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.638
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.642
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.655
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.627
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.627.cold.1
+ __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.657
+ __25-[PowerUICECManager init]_block_invoke.144
+ __25-[PowerUICECManager init]_block_invoke_2.145
+ __25-[PowerUICECManager init]_block_invoke_3.147
+ __44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1009
+ __44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1014
+ __44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.990
+ __46-[PowerUIDemoCECManager initWithContextStore:]_block_invoke.67
+ __46-[PowerUISmartChargeManager reportMonthlyData]_block_invoke.731
+ __47-[PowerUIDemoCECManager monitorPluggedInChange]_block_invoke.127
+ __48-[PowerUICECManager monitorBatteryNotifications]_block_invoke.196
+ __48-[PowerUICECManager monitorBatteryNotifications]_block_invoke_2.197
+ __57-[PowerUISmartChargeManager client:setState:withHandler:]_block_invoke.1573
+ __OBJC_$_CLASS_METHODS_PowerUICECUtilities
+ __OBJC_$_CLASS_METHODS_PowerUIDemoCECManager
+ __OBJC_$_INSTANCE_METHODS_PowerUICECGridDataForecastEntry
+ __OBJC_$_INSTANCE_METHODS_PowerUIDemoCECManager
+ __OBJC_$_INSTANCE_VARIABLES_PowerUICECGridDataForecastEntry
+ __OBJC_$_INSTANCE_VARIABLES_PowerUIDemoCECManager
+ __OBJC_$_PROP_LIST_PowerUICECGridDataForecastEntry
+ __OBJC_$_PROP_LIST_PowerUIDemoCECManager
+ __OBJC_CLASS_RO_$_PowerUICECGridDataForecastEntry
+ __OBJC_CLASS_RO_$_PowerUICECUtilities
+ __OBJC_CLASS_RO_$_PowerUIDemoCECManager
+ __OBJC_METACLASS_RO_$_PowerUICECGridDataForecastEntry
+ __OBJC_METACLASS_RO_$_PowerUICECUtilities
+ __OBJC_METACLASS_RO_$_PowerUIDemoCECManager
+ ___32+[PowerUIDemoCECManager manager]_block_invoke
+ ___40-[PowerUIDemoCECManager recordAnalytics]_block_invoke
+ ___44+[PowerUISmartChargeUtilities dateFormatter]_block_invoke
+ ___46-[PowerUIDemoCECManager initWithContextStore:]_block_invoke
+ ___47-[PowerUIDemoCECManager monitorPluggedInChange]_block_invoke
+ ___47-[PowerUIDemoCECManager monitorPluggedInChange]_block_invoke_2
+ ___58-[PowerUIDemoCECManager monitorBatteryStateOfChargeChange]_block_invoke
+ ___58-[PowerUIDemoCECManager monitorBatteryStateOfChargeChange]_block_invoke_2
+ ___62-[PowerUIDemoCECManager registerTimer:afterTime:withInterval:]_block_invoke
+ ___65-[PowerUIDemoCECManager handlePowerUICECStateChange:withHandler:]_block_invoke
+ __block_literal_global.1123
+ __block_literal_global.1163
+ __block_literal_global.1165
+ __block_literal_global.1190
+ __block_literal_global.1195
+ __block_literal_global.1382
+ __block_literal_global.203
+ __block_literal_global.2224
+ __block_literal_global.2226
+ __block_literal_global.259
+ __block_literal_global.837
+ __block_literal_global.947
+ __block_literal_global.95
+ _objc_msgSend$averageEmissionsOverForecastHorizon:
+ _objc_msgSend$balancingAuthorityName
+ _objc_msgSend$chargeHistoryAnalytics
+ _objc_msgSend$cleanIntervalsStringFromDates:withIntervalDuration:
+ _objc_msgSend$clearAnalytics
+ _objc_msgSend$deviceWasRestartedWithDefaults:
+ _objc_msgSend$emissionsForTime:overForecastHorizon:
+ _objc_msgSend$enableMitigations
+ _objc_msgSend$evaluateEngagement
+ _objc_msgSend$evaluateShouldChargeNow
+ _objc_msgSend$forecastDate
+ _objc_msgSend$forecastValue
+ _objc_msgSend$handleEmergencyCharge
+ _objc_msgSend$handleEngagement
+ _objc_msgSend$handlePauseChargingAboveMaxSOC
+ _objc_msgSend$hash
+ _objc_msgSend$indexOfObject:
+ _objc_msgSend$initWithContextStore:
+ _objc_msgSend$initWithDate:forecastValue:
+ _objc_msgSend$isDemoCECSupported
+ _objc_msgSend$isDemoDevice
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isPluggedIntoEligiblePowerSourceWithContext:
+ _objc_msgSend$isSecureDemoModeEnabled
+ _objc_msgSend$loadStateFromDefaults
+ _objc_msgSend$monitorBatteryStateOfChargeChange
+ _objc_msgSend$monitorPluggedInChange
+ _objc_msgSend$recordChargingStateChange:atBatteryLevel:duringCleanInterval:
+ _objc_msgSend$recordEngagementEvaluation:
+ _objc_msgSend$registerTimer:afterTime:withInterval:
+ _objc_msgSend$resetMitigation
+ _objc_msgSend$setEnabledState:
+ _objc_msgSend$setupDemoChargingTimeOverForecastHorizon:withKChargingSegments:
+ _objc_msgSend$shouldEngageDemoCEC
+ _objc_msgSend$shouldReevaluateEngagement
+ _objc_msgSend$sortedArrayUsingDescriptors:
+ _objc_msgSend$storedForecastForDemoAnalyticsWithForecastHorizon:
+ _objc_msgSend$timeToNextCleanInterval
+ _objc_msgSend$unregisterTimer:
+ registerTimer:afterTime:withInterval:.timerToken
- +[PowerUICECGridDataManager cleanIntervalsStringFromDates:]
- +[PowerUICECManager fetchEstimatedCountryCode]
- -[PowerUICECGridDataManager enoughVariationForForecast:]
- -[PowerUICECManager isPluggedIntoEligiblePowerSource]
- -[PowerUICECManager isPluggedIntoEligiblePowerSource].cold.1
- -[PowerUICECManager isPluggedIntoEligiblePowerSource].cold.2
- -[PowerUICECManager isPluggedIntoEligiblePowerSource].cold.3
- GCC_except_table34
- GCC_except_table49
- GCC_except_table56
- GCC_except_table60
- GCC_except_table83
- GCC_except_table91
- GCC_except_table95
- _OUTLINED_FUNCTION_10
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.594
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.605
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.612
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.617
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.621
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.630
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.632
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.639
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.646
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.648
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.650
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.652
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.659
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.659.cold.1
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.663
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.663.cold.1
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.618
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.624
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.637
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.641
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.654
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.626
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.626.cold.1
- __136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.656
- __25-[PowerUICECManager init]_block_invoke.147
- __25-[PowerUICECManager init]_block_invoke_2.148
- __25-[PowerUICECManager init]_block_invoke_3.150
- __44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1008
- __44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1012
- __44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.989
- __46-[PowerUISmartChargeManager reportMonthlyData]_block_invoke.730
- __48-[PowerUICECManager monitorBatteryNotifications]_block_invoke.200
- __48-[PowerUICECManager monitorBatteryNotifications]_block_invoke_2.199
- __57-[PowerUISmartChargeManager client:setState:withHandler:]_block_invoke.1572
- ___50+[PowerUISmartChargeUtilities timeStringFromDate:]_block_invoke
- ___56-[PowerUICECGridDataManager enoughVariationForForecast:]_block_invoke
- ___block_descriptor_32_e31_q24?0"NSNumber"8"NSNumber"16l
- __block_literal_global.100
- __block_literal_global.1122
- __block_literal_global.1162
- __block_literal_global.1164
- __block_literal_global.1189
- __block_literal_global.1194
- __block_literal_global.1381
- __block_literal_global.205
- __block_literal_global.2223
- __block_literal_global.2225
- __block_literal_global.268
- __block_literal_global.836
- __block_literal_global.946
- _objc_msgSend$cleanIntervalsStringFromDates:
- _objc_msgSend$isPluggedIntoEligiblePowerSource
CStrings:
+ "(SELF.%@.value.externalConnected = %@)"
+ "<%@:%p %@>"
+ "@\"PowerUICECGridDataManager\""
+ "Already evaluated shouldChargeNow in last %.0f mins. Skipping"
+ "B32@0:8@16d24"
+ "Bad date formatting: unable to parse string date into date. Not including in analytics."
+ "Charged to acceptable limit (= batteryLevel %ld >= kEmergencyChargeSocEndThreshold = %ld). Ending emergency charge."
+ "Charging history timeline %@"
+ "Charging state changed: %@"
+ "Current time (%@) within clean window starting at %@"
+ "Current time NOT in clean window intervals (current time: %@, clean intervals: %@)"
+ "DEoC override in place, but is supressed due to system conditions"
+ "Demo CEC Engaged: Changed states. Previously was charging = %@, now is charging = %@."
+ "Demo CEC Engaged: in a clean energy window. Charging."
+ "Demo CEC Engaged: in a dirty window. Charging paused."
+ "Demo CEC Phase update from %lu to %lu (%@ --> %@); BatteryLevel %ld, PluggedIn %d"
+ "Demo CEC State set to: %@"
+ "Demo CEC State: %@"
+ "Demo CEC changed charging states. Previously was charging = %@, now is charging = %@."
+ "Demo CEC is either not supported or disabled. Skipping"
+ "Demo CEC is no longer enabled. Disengaging and resetting state."
+ "Demo CEC no longer enabled. Resetting state."
+ "DemoCECManager Loaded state from defaults. isDemoCECEnabled %@, lastPluggedInDate %@, pluggedInBatteryLevel %ld, _lastEngagementCheckDate %@,"
+ "DemoCECManager initializing. Was the device restarted: %@"
+ "Determined clean forecast threshold of %lu"
+ "Device no longer plugged into a power source."
+ "Device no longer plugged into a power source. Disengaging and resetting state."
+ "Emergency Charge"
+ "Emergency charging"
+ "Enabled Ambrosia!"
+ "Enabling emergency charge."
+ "Engaged..."
+ "Engaging for the current session."
+ "Evaluated and decided not to engage"
+ "Evaluated and decided not to engage: no forecast available or not enough variation in grid."
+ "Evaluated and decided to engage"
+ "Evaluated and should engage after ending emergency charge"
+ "Evaluating engagement for current plug-in."
+ "Evaluating phase. Trigger: %@ (CurrentPhase %lu batteryLevel %ld, isPluggedIn %d)"
+ "Exiting from a session previously engaged/deemed eligible"
+ "Last engagement check date missing. Unable to determine session length."
+ "Last evaluated engagement %.0lf hours ago (at: %@). Re-evaluating whether or not to engage for the next %.0lf hours."
+ "Missing average emissions for session starting %@"
+ "Missing emissions for charge time %@"
+ "No forecasts stored in defaults. Returning nil."
+ "No previous evaluation check date set. Re-evaluating whether to engage for the next %.0lf hours."
+ "Not enough variation in forecast values (%lf - %lf). Required variation = %lf."
+ "Pausing charging while SOC is above %ld."
+ "PowerUICECGridDataForecastEntry"
+ "PowerUICECUtilities"
+ "PowerUIDemoCECManager"
+ "Registering timer"
+ "Reported Demo CEC metrics to CoreAnalytics %@"
+ "Resetting state"
+ "SOC fell below acceptable limit (batteryLevel = %ld <= kEmergencyChargeSocStartThreshold = %ld). Deciding to emergency charge regardless of grid."
+ "SOC is above upper charge limit (batteryLevel = %ld >= kUpperChargeLimit = %ld). Pausing charging regardless of grid."
+ "SOC is below acceptable limit (batteryLevel = %ld <= kEmergencyChargeSocStartThreshold = %ld). Deciding to emergency charge regardless of grid."
+ "Setting lastPluggedIn battery level to %ld"
+ "Setting lastPluggedIn date to %@"
+ "Should re-evaluate engagement %d"
+ "Specified time not covered by the current forecast's time horizon. Unable to get emissions for time %@"
+ "Still emergency charging. Not yet at acceptable SOC limit (= batteryLevel %ld < kEmergencyChargeSocEndThreshold = %ld)."
+ "T@\"NSDate\",&,N,V_forecastDate"
+ "T@\"NSDate\",&,N,V_lastEngagementCheckDate"
+ "T@\"NSDate\",&,N,V_lastForecastFetchDate"
+ "T@\"NSDate\",&,N,V_lastPluggedInDate"
+ "T@\"NSNumber\",&,N,V_forecastValue"
+ "T@\"PowerUICECGridDataManager\",&,N,V_gridDataManager"
+ "TB,N,V_isDemoCECEnabled"
+ "TB,N,V_isDemoMode"
+ "Td,N,V_intervalDuration"
+ "TestMode: isDemoDevice set to %d"
+ "Time %@ within forecast window starting at %@. Emissions during interval: %ld g/kWh."
+ "Unable to compute average emissions over charging periods. Defaulting to -1."
+ "Unable to compute time until next clean session. Defaulting to registering %.0f minute timer."
+ "Unable to get stored forecasts in order to calculate average emissions."
+ "Unable to get stored forecasts. Unknown emissions for time %@"
+ "Unregistering timer"
+ "User state setting"
+ "[Internal] IBLM"
+ "_forecastDate"
+ "_forecastValue"
+ "_gridDataManager"
+ "_intervalDuration"
+ "_isDemoCECEnabled"
+ "_isDemoMode"
+ "_lastEngagementCheckDate"
+ "_lastForecastFetchDate"
+ "_lastPluggedInDate"
+ "averageEmissionsOverForecastHorizon:"
+ "avgEmissions"
+ "balancingAuthority"
+ "balancingAuthorityName"
+ "battLevel"
+ "chargeHistoryAnalytics"
+ "chargingEmissions"
+ "chargingStateIsCharging"
+ "cleanIntervalsStringFromDates:withIntervalDuration:"
+ "clearAnalytics"
+ "com.apple.das.smartcharging.democec.sessionstats"
+ "com.apple.powerui.cecutilities"
+ "com.apple.powerui.democec"
+ "com.apple.powerui.democec.battery"
+ "com.apple.powerui.democec.batteryState"
+ "com.apple.powerui.democec.pluggedIn"
+ "com.apple.powerui.democec.unplug"
+ "com.apple.powerui.democecmanager.queue"
+ "demoCecChargingStatusTimeline"
+ "demoCecEngagement"
+ "demoForecast"
+ "deviceWasRestartedWithDefaults:"
+ "disableMitigations"
+ "emergencyChargeTime"
+ "emissionsForTime:overForecastHorizon:"
+ "enableMitigations"
+ "enoughVariationForForecast:withMinDifference:"
+ "evaluateEngagement"
+ "evaluateShouldChargeNow"
+ "forecastDate"
+ "forecastFetchDate"
+ "forecastFromDefaults"
+ "forecastValue"
+ "gridDataManager"
+ "handleEmergencyCharge"
+ "handleEngagement"
+ "handlePauseChargingAboveMaxSOC"
+ "indexOfObject:"
+ "initWithContextStore:"
+ "initWithDate:forecastValue:"
+ "intervalDuration"
+ "isDemoCECEnabled"
+ "isDemoCECSupported"
+ "isDemoCecFlagEnabledForStore"
+ "isDemoDevice"
+ "isDemoMode"
+ "isEqualToNumber:"
+ "isPluggedIntoEligiblePowerSourceWithContext:"
+ "isSecureDemoModeEnabled"
+ "lastEngagementCheckDate"
+ "lastForecastFetchDate"
+ "lastPauseChargingCheckDate"
+ "loadStateFromDefaults"
+ "monitorBatteryStateOfChargeChange"
+ "monitorPluggedInChange"
+ "q32@0:8@16d24"
+ "recordChargingStateChange:atBatteryLevel:duringCleanInterval:"
+ "recordEngagementEvaluation:"
+ "recordForecastInDefaults:"
+ "registerTimer:afterTime:withInterval:"
+ "sessionLength"
+ "setEnabledState:"
+ "setForecastDate:"
+ "setForecastValue:"
+ "setGridDataManager:"
+ "setIntervalDuration:"
+ "setIsDemoCECEnabled:"
+ "setIsDemoMode:"
+ "setLastEngagementCheckDate:"
+ "setLastForecastFetchDate:"
+ "setLastPluggedInDate:"
+ "settings-navigation://com.apple.Settings.Battery/CHARGING_OPTIONS_IDENTIFIER"
+ "setupDemoChargingTimeOverForecastHorizon:withKChargingSegments:"
+ "shouldEngageDemoCEC"
+ "shouldReevaluateEngagement"
+ "sortedArrayUsingDescriptors:"
+ "storedForecastForDemoAnalyticsWithForecastHorizon:"
+ "testIsDemoDevice"
+ "timeToNextCleanInterval"
+ "totalChargeTime"
+ "unregisterTimer:"
+ "v32@0:8B16q20B28"
+ "v32@0:8d16q24"
+ "v40@0:8@16d24d32"
+ "wasCleanInterval"
- "Current time NOT in clean window intervals %@"
- "Current time within clean window startin at %@"
- "Enable LPM!"
- "Not enough variation in forecast values (%lf - %lf)"
- "Unsupported CEC State: %@"
- "[Internal] Low Power Mode"
- "cleanIntervalsStringFromDates:"
- "enoughVariationForForecast:"
- "isPluggedIntoEligiblePowerSource"
- "prefs:root=BATTERY_USAGE&path=CHARGING_TITLE"
- "q24@?0@\"NSNumber\"8@\"NSNumber\"16"

```
