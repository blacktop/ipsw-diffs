## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-651.120.3.0.0
-  __TEXT.__text: 0xbc554
+684.0.0.0.0
+  __TEXT.__text: 0xc17f8
   __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__objc_methlist: 0x1b12c
-  __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0xd911
-  __TEXT.__oslogstring: 0xab9f
-  __TEXT.__gcc_except_tab: 0x1234
-  __TEXT.__unwind_info: 0x1c20
-  __TEXT.__objc_classname: 0xb0f
-  __TEXT.__objc_methname: 0x3db32
-  __TEXT.__objc_methtype: 0x4090
-  __TEXT.__objc_stubs: 0xc5c0
-  __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0x13e0
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __TEXT.__objc_methlist: 0x1b664
+  __TEXT.__const: 0x528
+  __TEXT.__cstring: 0xe082
+  __TEXT.__oslogstring: 0xba6d
+  __TEXT.__gcc_except_tab: 0x125c
+  __TEXT.__unwind_info: 0x1cc8
+  __TEXT.__objc_classname: 0xb55
+  __TEXT.__objc_methname: 0x3e11d
+  __TEXT.__objc_methtype: 0x40f1
+  __TEXT.__objc_stubs: 0xc9e0
+  __DATA_CONST.__got: 0x500
+  __DATA_CONST.__const: 0x14c0
+  __DATA_CONST.__objc_classlist: 0x2f8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5280
+  __DATA_CONST.__objc_selrefs: 0x53d8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2b8
-  __DATA_CONST.__objc_arraydata: 0x6e70
+  __DATA_CONST.__objc_superrefs: 0x2d0
+  __DATA_CONST.__objc_arraydata: 0x6f48
   __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0xb660
-  __AUTH_CONST.__objc_const: 0x35b30
-  __AUTH_CONST.__objc_intobj: 0x8e8
-  __AUTH_CONST.__objc_arrayobj: 0x378
+  __AUTH_CONST.__cfstring: 0xbd00
+  __AUTH_CONST.__objc_const: 0x363c0
+  __AUTH_CONST.__objc_intobj: 0x960
+  __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x1310
-  __DATA.__objc_ivar: 0x3b9c
-  __DATA.__data: 0x6c0
-  __DATA.__bss: 0xd8
+  __AUTH.__objc_data: 0x1400
+  __DATA.__objc_ivar: 0x3c1c
+  __DATA.__data: 0x6c8
+  __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x180
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore
+  - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B04C3324-3521-36D7-AF17-0C6FB0092A3F
-  Functions: 9642
-  Symbols:   26483
-  CStrings:  8643
+  UUID: 4CD90FC9-821E-369A-9202-A589CAA49805
+  Functions: 9778
+  Symbols:   26831
+  CStrings:  8860
 
Symbols:
+ +[PowerUISmartChargeUtilities numberForKey:fromDict:withDefault:]
+ +[PowerUISmartChargeUtilities numberForKey:fromDict:withDefault:].cold.1
+ +[PowerUISmartChargeUtilities numberForKey:fromDict:withDefault:].cold.2
+ +[dynamic_scheduling URLOfModelInThisBundle]
+ +[dynamic_scheduling URLOfModelInThisBundle].cold.1
+ +[dynamic_scheduling loadContentsOfURL:configuration:completionHandler:]
+ +[dynamic_scheduling loadWithConfiguration:completionHandler:]
+ -[PowerUICECGridDataManager engagementDecisionReason]
+ -[PowerUICECGridDataManager intervalStartTimesOverForecastHorizon:]
+ -[PowerUICECGridDataManager lastIntervalStartTimeOverForecastHorizon:]
+ -[PowerUICECGridDataManager lastIntervalStartTimeOverForecastHorizon:].cold.1
+ -[PowerUICECGridDataManager setEngagementDecisionReason:]
+ -[PowerUICECGridDataManager startTimeCurrentIntervalWithinForecastHorizon:]
+ -[PowerUICECGridDataManager time:isWithinIntervalWithStart:]
+ -[PowerUICECGridDataManager time:isWithinIntervalWithStart:].cold.1
+ -[PowerUICECManager readLifetimeCECEngagementValues]
+ -[PowerUICECManager recordLifetimeValues:]
+ -[PowerUIChargingController clearChargeLimitForLimitType:].cold.2
+ -[PowerUIChargingController loadChargeLimitTokenForPreferenceKey:forReason:verbose:]
+ -[PowerUIChargingController setChargeLimitTo:forLimitType:setNoChargeToFull:]
+ -[PowerUIChargingController setChargeLimitTo:forLimitType:setNoChargeToFull:].cold.1
+ -[PowerUIChargingController setChargeLimitTo:forLimitType:setNoChargeToFull:].cold.2
+ -[PowerUIDemoCECManager analyticsTimer]
+ -[PowerUIDemoCECManager chargeHistoryAnalytics:]
+ -[PowerUIDemoCECManager chargeHistoryAnalytics:].cold.1
+ -[PowerUIDemoCECManager dateDictionaryFromDefaults:]
+ -[PowerUIDemoCECManager handleCallback:].cold.6
+ -[PowerUIDemoCECManager handleIsEnabledChange]
+ -[PowerUIDemoCECManager handlePauseChargingAboveMaxSOC:]
+ -[PowerUIDemoCECManager isWithinEngagedSession]
+ -[PowerUIDemoCECManager lastUnpluggedDate]
+ -[PowerUIDemoCECManager monitorDemoCecIsEnabledChange]
+ -[PowerUIDemoCECManager recordStartWallEnergyAccum]
+ -[PowerUIDemoCECManager recordStartWallEnergyAccum].cold.1
+ -[PowerUIDemoCECManager recordSystemLoadAccum]
+ -[PowerUIDemoCECManager recordSystemLoadAccum].cold.1
+ -[PowerUIDemoCECManager recordSystemLoadAccum].cold.2
+ -[PowerUIDemoCECManager recordSystemLoadAccum].cold.3
+ -[PowerUIDemoCECManager registerAnalyticsTimer:afterTime:withInterval:]
+ -[PowerUIDemoCECManager registerAnalyticsTimer:afterTime:withInterval:].cold.1
+ -[PowerUIDemoCECManager registerEngagementTimer:afterTime:withInterval:]
+ -[PowerUIDemoCECManager registerEngagementTimer:afterTime:withInterval:].cold.1
+ -[PowerUIDemoCECManager registerEngagementTimer]
+ -[PowerUIDemoCECManager setAnalyticsTimer:]
+ -[PowerUIDemoCECManager setLastUnpluggedDate:]
+ -[PowerUIDemoCECManager startSessionTimers]
+ -[PowerUIDemoCECManager startSystemLoadAccumTimer]
+ -[PowerUIDemoCECManager startSystemLoadAccumTimer].cold.1
+ -[PowerUIDemoCECManager systemLoadEmissionSavings:]
+ -[PowerUIDemoCECManager systemLoadEmissionSavings:].cold.1
+ -[PowerUIDemoCECManager systemLoadEmissionSavings:].cold.2
+ -[PowerUIDemoCECManager totalWallEnergyOverSession]
+ -[PowerUIDemoCECManager totalWallEnergyOverSession].cold.1
+ -[PowerUIDemoCECManager totalWallEnergyOverSession].cold.2
+ -[PowerUIIntelligenceManager postAnalyticsEventForDynamicRuntimeAllocationWithPredictedDurationMinutes:andActualDurationMinutes:andEngagementDecision:andWasWireless:andSPIError:]
+ -[PowerUISmartChargeManager getCECLifetimeValues]
+ -[PowerUISmartChargeManager mostRecentOBCModeOfoperationFromTimeline]
+ -[PowerUISmartChargeManager resourceHint]
+ -[PowerUISmartChargeManager setMCLLimit:].cold.1
+ -[PowerUISmartChargeManager setResourceHint:]
+ -[PowerUISmartChargeManager setVerboseLog:]
+ -[PowerUISmartChargeManager updateResourceHint]
+ -[PowerUISmartChargeManager verboseLog]
+ -[dynamic_scheduling .cxx_destruct]
+ -[dynamic_scheduling initWithConfiguration:error:]
+ -[dynamic_scheduling initWithContentsOfURL:configuration:error:]
+ -[dynamic_scheduling initWithContentsOfURL:error:]
+ -[dynamic_scheduling initWithMLModel:]
+ -[dynamic_scheduling init]
+ -[dynamic_scheduling model]
+ -[dynamic_scheduling predictionFromFeatures:completionHandler:]
+ -[dynamic_scheduling predictionFromFeatures:error:]
+ -[dynamic_scheduling predictionFromFeatures:options:completionHandler:]
+ -[dynamic_scheduling predictionFromFeatures:options:error:]
+ -[dynamic_scheduling predictionFromPlugin_battery_level:time_from_plugin:med_dur_1:med_dur_2:med_dur_4:med_dur_8:med_dur_16:med_dur_24:cnt_dur_1:cnt_dur_2:cnt_dur_4:cnt_dur_8:cnt_dur_16:cnt_dur_24:std_dur_1:std_dur_2:std_dur_4:std_dur_8:std_dur_16:std_dur_24:weekday_med_dur_1:weekday_med_dur_2:weekday_med_dur_4:weekday_med_dur_8:weekday_med_dur_24:weekday_std_dur_4:error:]
+ -[dynamic_scheduling predictionsFromInputs:options:error:]
+ -[dynamic_schedulingInput cnt_dur_16]
+ -[dynamic_schedulingInput cnt_dur_1]
+ -[dynamic_schedulingInput cnt_dur_24]
+ -[dynamic_schedulingInput cnt_dur_2]
+ -[dynamic_schedulingInput cnt_dur_4]
+ -[dynamic_schedulingInput cnt_dur_8]
+ -[dynamic_schedulingInput featureNames]
+ -[dynamic_schedulingInput featureValueForName:]
+ -[dynamic_schedulingInput initWithPlugin_battery_level:time_from_plugin:med_dur_1:med_dur_2:med_dur_4:med_dur_8:med_dur_16:med_dur_24:cnt_dur_1:cnt_dur_2:cnt_dur_4:cnt_dur_8:cnt_dur_16:cnt_dur_24:std_dur_1:std_dur_2:std_dur_4:std_dur_8:std_dur_16:std_dur_24:weekday_med_dur_1:weekday_med_dur_2:weekday_med_dur_4:weekday_med_dur_8:weekday_med_dur_24:weekday_std_dur_4:]
+ -[dynamic_schedulingInput med_dur_16]
+ -[dynamic_schedulingInput med_dur_1]
+ -[dynamic_schedulingInput med_dur_24]
+ -[dynamic_schedulingInput med_dur_2]
+ -[dynamic_schedulingInput med_dur_4]
+ -[dynamic_schedulingInput med_dur_8]
+ -[dynamic_schedulingInput plugin_battery_level]
+ -[dynamic_schedulingInput setCnt_dur_16:]
+ -[dynamic_schedulingInput setCnt_dur_1:]
+ -[dynamic_schedulingInput setCnt_dur_24:]
+ -[dynamic_schedulingInput setCnt_dur_2:]
+ -[dynamic_schedulingInput setCnt_dur_4:]
+ -[dynamic_schedulingInput setCnt_dur_8:]
+ -[dynamic_schedulingInput setMed_dur_16:]
+ -[dynamic_schedulingInput setMed_dur_1:]
+ -[dynamic_schedulingInput setMed_dur_24:]
+ -[dynamic_schedulingInput setMed_dur_2:]
+ -[dynamic_schedulingInput setMed_dur_4:]
+ -[dynamic_schedulingInput setMed_dur_8:]
+ -[dynamic_schedulingInput setPlugin_battery_level:]
+ -[dynamic_schedulingInput setStd_dur_16:]
+ -[dynamic_schedulingInput setStd_dur_1:]
+ -[dynamic_schedulingInput setStd_dur_24:]
+ -[dynamic_schedulingInput setStd_dur_2:]
+ -[dynamic_schedulingInput setStd_dur_4:]
+ -[dynamic_schedulingInput setStd_dur_8:]
+ -[dynamic_schedulingInput setTime_from_plugin:]
+ -[dynamic_schedulingInput setWeekday_med_dur_1:]
+ -[dynamic_schedulingInput setWeekday_med_dur_24:]
+ -[dynamic_schedulingInput setWeekday_med_dur_2:]
+ -[dynamic_schedulingInput setWeekday_med_dur_4:]
+ -[dynamic_schedulingInput setWeekday_med_dur_8:]
+ -[dynamic_schedulingInput setWeekday_std_dur_4:]
+ -[dynamic_schedulingInput std_dur_16]
+ -[dynamic_schedulingInput std_dur_1]
+ -[dynamic_schedulingInput std_dur_24]
+ -[dynamic_schedulingInput std_dur_2]
+ -[dynamic_schedulingInput std_dur_4]
+ -[dynamic_schedulingInput std_dur_8]
+ -[dynamic_schedulingInput time_from_plugin]
+ -[dynamic_schedulingInput weekday_med_dur_1]
+ -[dynamic_schedulingInput weekday_med_dur_24]
+ -[dynamic_schedulingInput weekday_med_dur_2]
+ -[dynamic_schedulingInput weekday_med_dur_4]
+ -[dynamic_schedulingInput weekday_med_dur_8]
+ -[dynamic_schedulingInput weekday_std_dur_4]
+ -[dynamic_schedulingOutput charge_duration]
+ -[dynamic_schedulingOutput featureNames]
+ -[dynamic_schedulingOutput featureValueForName:]
+ -[dynamic_schedulingOutput initWithCharge_duration:]
+ -[dynamic_schedulingOutput setCharge_duration:]
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table487
+ GCC_except_table74
+ GCC_except_table80
+ _OBJC_CLASS_$_NSOperationQueue
+ _OBJC_CLASS_$_ResourceHint
+ _OBJC_CLASS_$_dynamic_scheduling
+ _OBJC_CLASS_$_dynamic_schedulingInput
+ _OBJC_CLASS_$_dynamic_schedulingOutput
+ _OBJC_IVAR_$_PowerUICECGridDataManager._engagementDecisionReason
+ _OBJC_IVAR_$_PowerUIDemoCECManager._analyticsTimer
+ _OBJC_IVAR_$_PowerUIDemoCECManager._lastUnpluggedDate
+ _OBJC_IVAR_$_PowerUISmartChargeManager._resourceHint
+ _OBJC_IVAR_$_PowerUISmartChargeManager._verboseLog
+ _OBJC_IVAR_$_dynamic_scheduling._model
+ _OBJC_IVAR_$_dynamic_schedulingInput._cnt_dur_1
+ _OBJC_IVAR_$_dynamic_schedulingInput._cnt_dur_16
+ _OBJC_IVAR_$_dynamic_schedulingInput._cnt_dur_2
+ _OBJC_IVAR_$_dynamic_schedulingInput._cnt_dur_24
+ _OBJC_IVAR_$_dynamic_schedulingInput._cnt_dur_4
+ _OBJC_IVAR_$_dynamic_schedulingInput._cnt_dur_8
+ _OBJC_IVAR_$_dynamic_schedulingInput._med_dur_1
+ _OBJC_IVAR_$_dynamic_schedulingInput._med_dur_16
+ _OBJC_IVAR_$_dynamic_schedulingInput._med_dur_2
+ _OBJC_IVAR_$_dynamic_schedulingInput._med_dur_24
+ _OBJC_IVAR_$_dynamic_schedulingInput._med_dur_4
+ _OBJC_IVAR_$_dynamic_schedulingInput._med_dur_8
+ _OBJC_IVAR_$_dynamic_schedulingInput._plugin_battery_level
+ _OBJC_IVAR_$_dynamic_schedulingInput._std_dur_1
+ _OBJC_IVAR_$_dynamic_schedulingInput._std_dur_16
+ _OBJC_IVAR_$_dynamic_schedulingInput._std_dur_2
+ _OBJC_IVAR_$_dynamic_schedulingInput._std_dur_24
+ _OBJC_IVAR_$_dynamic_schedulingInput._std_dur_4
+ _OBJC_IVAR_$_dynamic_schedulingInput._std_dur_8
+ _OBJC_IVAR_$_dynamic_schedulingInput._time_from_plugin
+ _OBJC_IVAR_$_dynamic_schedulingInput._weekday_med_dur_1
+ _OBJC_IVAR_$_dynamic_schedulingInput._weekday_med_dur_2
+ _OBJC_IVAR_$_dynamic_schedulingInput._weekday_med_dur_24
+ _OBJC_IVAR_$_dynamic_schedulingInput._weekday_med_dur_4
+ _OBJC_IVAR_$_dynamic_schedulingInput._weekday_med_dur_8
+ _OBJC_IVAR_$_dynamic_schedulingInput._weekday_std_dur_4
+ _OBJC_IVAR_$_dynamic_schedulingOutput._charge_duration
+ _OBJC_METACLASS_$_dynamic_scheduling
+ _OBJC_METACLASS_$_dynamic_schedulingInput
+ _OBJC_METACLASS_$_dynamic_schedulingOutput
+ __OBJC_$_CLASS_METHODS_dynamic_scheduling
+ __OBJC_$_INSTANCE_METHODS_dynamic_scheduling
+ __OBJC_$_INSTANCE_METHODS_dynamic_schedulingInput
+ __OBJC_$_INSTANCE_METHODS_dynamic_schedulingOutput
+ __OBJC_$_INSTANCE_VARIABLES_dynamic_scheduling
+ __OBJC_$_INSTANCE_VARIABLES_dynamic_schedulingInput
+ __OBJC_$_INSTANCE_VARIABLES_dynamic_schedulingOutput
+ __OBJC_$_PROP_LIST_dynamic_scheduling
+ __OBJC_$_PROP_LIST_dynamic_schedulingInput
+ __OBJC_$_PROP_LIST_dynamic_schedulingOutput
+ __OBJC_CLASS_PROTOCOLS_$_dynamic_schedulingInput
+ __OBJC_CLASS_PROTOCOLS_$_dynamic_schedulingOutput
+ __OBJC_CLASS_RO_$_dynamic_scheduling
+ __OBJC_CLASS_RO_$_dynamic_schedulingInput
+ __OBJC_CLASS_RO_$_dynamic_schedulingOutput
+ __OBJC_METACLASS_RO_$_dynamic_scheduling
+ __OBJC_METACLASS_RO_$_dynamic_schedulingInput
+ __OBJC_METACLASS_RO_$_dynamic_schedulingOutput
+ ___101+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:ignoringDisconnectsShorterThan:]_block_invoke.38
+ ___101+[PowerUISmartChargeUtilities timestampOfFirstEventReachingBatteryLevel:betweenStartTime:andEndTime:]_block_invoke.81
+ ___106-[PowerUIAudioAccessorySmartChargeManager addTimeSeriesDataToStream:withSide:withFirmwareVersion:withLog:]_block_invoke.329
+ ___132+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:withMinimumPlugoutBatteryLevel:ignoringDisconnectsShorterThan:]_block_invoke.45
+ ___132+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:withMinimumPlugoutBatteryLevel:ignoringDisconnectsShorterThan:]_block_invoke.45.cold.1
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1017
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1022
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1028
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1030
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1039
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1046
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1050
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1052
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1054
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1062
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1062.cold.1
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1063
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1066
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1066.cold.1
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.1067
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.996
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1018
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1024
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1032
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1041
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1048
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1056
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1065
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.1065.cold.1
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1020
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1026
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1026.cold.1
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1037
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.1058
+ ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_4.1060
+ ___178-[PowerUIIntelligenceManager postAnalyticsEventForDynamicRuntimeAllocationWithPredictedDurationMinutes:andActualDurationMinutes:andEngagementDecision:andWasWireless:andSPIError:]_block_invoke
+ ___34-[PowerUISmartChargeClient status]_block_invoke.137
+ ___38-[PowerUIChargeAwarenessNotifier init]_block_invoke.47
+ ___39-[PowerUISmartChargeManager enableDEoC]_block_invoke
+ ___39-[PowerUISmartChargeManager enableDEoC]_block_invoke.cold.1
+ ___40-[PowerUISmartChargeManager disableDEoC]_block_invoke.1962
+ ___42-[PowerUISmartChargeClient powerLogStatus]_block_invoke.139
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1359
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1378
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1382
+ ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1383
+ ___46-[PowerUIDemoCECManager initWithContextStore:]_block_invoke_3
+ ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.291
+ ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.295
+ ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.299
+ ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.303
+ ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.307
+ ___47-[PowerUIDemoCECManager monitorPluggedInChange]_block_invoke.127
+ ___47-[PowerUISmartChargeClient fullChargeDeadline:]_block_invoke.140
+ ___48-[PowerUICECManager monitorBatteryNotifications]_block_invoke.207
+ ___50-[PowerUISmartChargeClient cecFullChargeDeadline:]_block_invoke.159
+ ___50-[PowerUISmartChargeManager forceDEoCReevaluation]_block_invoke
+ ___51-[PowerUISmartChargeClient resetEngagementOverride]_block_invoke.162
+ ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.164
+ ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.164.cold.1
+ ___54-[PowerUIDemoCECManager monitorDemoCecIsEnabledChange]_block_invoke
+ ___54-[PowerUIDemoCECManager monitorDemoCecIsEnabledChange]_block_invoke_2
+ ___57-[PowerUISmartChargeManager client:setState:withHandler:]_block_invoke.1949
+ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2040
+ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2040.cold.1
+ ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.2040.cold.2
+ ___63-[PowerUISmartChargeClientAudioAccessories getAvailableDevices]_block_invoke.108
+ ___63-[PowerUISmartChargeClientAudioAccessories getStatusForDevice:]_block_invoke.110
+ ___63-[dynamic_scheduling predictionFromFeatures:completionHandler:]_block_invoke
+ ___64-[PowerUISmartChargeClientAudioAccessories lastActionForDevice:]_block_invoke.112
+ ___66-[PowerUISmartChargeClient legacy_client_isOBCEngagedWithHandler:]_block_invoke.146
+ ___68-[PowerUISmartChargeClientAudioAccessories lastUsedLeewayWithError:]_block_invoke.114
+ ___68-[PowerUISmartChargeClientAudioAccessories lastUsedLeewayWithError:]_block_invoke.114.cold.1
+ ___71-[PowerUIDemoCECManager registerAnalyticsTimer:afterTime:withInterval:]_block_invoke
+ ___71-[dynamic_scheduling predictionFromFeatures:options:completionHandler:]_block_invoke
+ ___72+[dynamic_scheduling loadContentsOfURL:configuration:completionHandler:]_block_invoke
+ ___72-[PowerUIChargeAwarenessNotifier displayNotificationForMCL:forWireless:]_block_invoke.119
+ ___72-[PowerUIChargeAwarenessNotifier displayNotificationForMCL:forWireless:]_block_invoke.119.cold.1
+ ___72-[PowerUIChargeAwarenessNotifier displayNotificationForMCL:forWireless:]_block_invoke.139
+ ___72-[PowerUIDemoCECManager registerEngagementTimer:afterTime:withInterval:]_block_invoke
+ ___75-[PowerUICECGridDataManager startTimeCurrentIntervalWithinForecastHorizon:]_block_invoke
+ ___75-[PowerUICECGridDataManager startTimeCurrentIntervalWithinForecastHorizon:]_block_invoke.cold.1
+ ___75-[PowerUICECGridDataManager startTimeCurrentIntervalWithinForecastHorizon:]_block_invoke.cold.2
+ ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.160
+ ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.160.cold.1
+ ___85-[PowerUISmartChargeClientAudioAccessories engageUntil:forDevice:overrideAllSignals:]_block_invoke.107
+ ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.155
+ ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.155.cold.1
+ ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.163
+ ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.163.cold.1
+ ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.144
+ ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.144.cold.1
+ ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.142
+ ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.142.cold.1
+ ___96+[PowerUISmartChargeUtilities historicalFullChargeDurationStartingAt:withMinimumPluginDuration:]_block_invoke.84
+ ___97+[PowerUISmartChargeUtilities drainSessionsInfoBetweenRelevantChargesBefore:withMinimumDuration:]_block_invoke.53
+ ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8ls32l8
+ ___block_descriptor_56_e8_32s40bs48bs_e35_v24?0"NSString"8"NSDictionary"16ls32l8s40l8s48l8
+ ___block_descriptor_58_e8_32s_e19_"NSDictionary"8?0ls32l8
+ ___block_literal_global.117
+ ___block_literal_global.1343
+ ___block_literal_global.149
+ ___block_literal_global.151
+ ___block_literal_global.1528
+ ___block_literal_global.153
+ ___block_literal_global.1568
+ ___block_literal_global.1570
+ ___block_literal_global.158
+ ___block_literal_global.1601
+ ___block_literal_global.1606
+ ___block_literal_global.1762
+ ___block_literal_global.212
+ ___block_literal_global.268
+ ___block_literal_global.2718
+ ___block_literal_global.2720
+ ___block_literal_global.37
+ ___block_literal_global.44
+ ___block_literal_global.52
+ ___block_literal_global.83
+ ___block_literal_global.86
+ ___btConnectionUpdateCallback_block_invoke.319
+ _kMSDCleanEnergyChargingNotificationName
+ _kRecentDeviceConnectedToChargerThresholdSeconds
+ _objc_msgSend$addObserverForName:object:queue:usingBlock:
+ _objc_msgSend$chargeHistoryAnalytics:
+ _objc_msgSend$charge_duration
+ _objc_msgSend$code
+ _objc_msgSend$dateDictionaryFromDefaults:
+ _objc_msgSend$engagementDecisionReason
+ _objc_msgSend$getCECLifetimeValues
+ _objc_msgSend$handleIsEnabledChange
+ _objc_msgSend$handlePauseChargingAboveMaxSOC:
+ _objc_msgSend$initWithCharge_duration:
+ _objc_msgSend$initWithResourceType:andState:
+ _objc_msgSend$intervalStartTimesOverForecastHorizon:
+ _objc_msgSend$isWithinEngagedSession
+ _objc_msgSend$lastIntervalStartTimeOverForecastHorizon:
+ _objc_msgSend$loadChargeLimitTokenForPreferenceKey:forReason:verbose:
+ _objc_msgSend$mainQueue
+ _objc_msgSend$monitorDemoCecIsEnabledChange
+ _objc_msgSend$mostRecentOBCModeOfoperationFromTimeline
+ _objc_msgSend$numberForKey:fromDict:withDefault:
+ _objc_msgSend$orPredicateWithSubpredicates:
+ _objc_msgSend$postAnalyticsEventForDynamicRuntimeAllocationWithPredictedDurationMinutes:andActualDurationMinutes:andEngagementDecision:andWasWireless:andSPIError:
+ _objc_msgSend$readLifetimeCECEngagementValues
+ _objc_msgSend$recordLifetimeValues:
+ _objc_msgSend$recordStartWallEnergyAccum
+ _objc_msgSend$recordSystemLoadAccum
+ _objc_msgSend$registerAnalyticsTimer:afterTime:withInterval:
+ _objc_msgSend$registerEngagementTimer
+ _objc_msgSend$registerEngagementTimer:afterTime:withInterval:
+ _objc_msgSend$setChargeLimitTo:forLimitType:setNoChargeToFull:
+ _objc_msgSend$setSound:
+ _objc_msgSend$startSessionTimers
+ _objc_msgSend$startSystemLoadAccumTimer
+ _objc_msgSend$startTimeCurrentIntervalWithinForecastHorizon:
+ _objc_msgSend$systemLoadEmissionSavings:
+ _objc_msgSend$time:isWithinIntervalWithStart:
+ _objc_msgSend$totalWallEnergyOverSession
+ _objc_msgSend$updateResourceHint
+ _objc_msgSend$updateState:
+ _registerAnalyticsTimer:afterTime:withInterval:.timerToken
+ _registerEngagementTimer:afterTime:withInterval:.timerToken
- +[PowerUISmartChargeUtilities historicalFullChargeDurationStartingAt:withMinimumPluginDuration:].cold.2
- -[PowerUIChargingController loadChargeLimitTokenForPreferenceKey:forReason:]
- -[PowerUIChargingController setChargeLimitTo:forLimitType:].cold.1
- -[PowerUIChargingController setChargeLimitTo:forLimitType:].cold.2
- -[PowerUIDemoCECManager chargeHistoryAnalytics]
- -[PowerUIDemoCECManager chargeHistoryAnalytics].cold.1
- -[PowerUIDemoCECManager debugStatus]
- -[PowerUIDemoCECManager handlePauseChargingAboveMaxSOC]
- -[PowerUIDemoCECManager registerTimer:afterTime:withInterval:]
- -[PowerUIDemoCECManager registerTimer:afterTime:withInterval:].cold.1
- -[PowerUIDemoCECManager registerTimer]
- -[PowerUIDemoCECManager shouldReevaluateEngagement].cold.1
- -[PowerUIDemoCECManager shouldReevaluateEngagement].cold.2
- -[PowerUISmartChargeManager enableDEoC].cold.1
- -[PowerUISmartChargeManager handleNewBatteryLevel:whileExternalConnected:fullyCharged:].cold.1
- GCC_except_table36
- GCC_except_table43
- GCC_except_table478
- GCC_except_table48
- GCC_except_table52
- GCC_except_table79
- GCC_except_table83
- GCC_except_table97
- _OBJC_IVAR_$_PowerUIDemoCECManager._debugStatus
- ___101+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:ignoringDisconnectsShorterThan:]_block_invoke.37
- ___101+[PowerUISmartChargeUtilities timestampOfFirstEventReachingBatteryLevel:betweenStartTime:andEndTime:]_block_invoke.80
- ___106-[PowerUIAudioAccessorySmartChargeManager addTimeSeriesDataToStream:withSide:withFirmwareVersion:withLog:]_block_invoke.326
- ___132+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:withMinimumPlugoutBatteryLevel:ignoringDisconnectsShorterThan:]_block_invoke.44
- ___132+[PowerUISmartChargeUtilities pluginEventsBefore:withMinimumDuration:withMinimumPlugoutBatteryLevel:ignoringDisconnectsShorterThan:]_block_invoke.44.cold.1
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.598
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.619
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.624
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.630
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.632
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.641
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.648
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.652
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.654
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.656
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.664
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.664.cold.1
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.665
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.668
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.668.cold.1
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke.669
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.620
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.626
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.634
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.643
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.650
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.658
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.667
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_2.667.cold.1
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.622
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.628
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.628.cold.1
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.639
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_3.660
- ___136-[PowerUISmartChargeManager initWithDefaultsDomain:contextStore:beforeHandlingBatteryChangeCallback:afterHandlingBatteryChangeCallback:]_block_invoke_4.662
- ___34-[PowerUISmartChargeClient status]_block_invoke.134
- ___38-[PowerUIChargeAwarenessNotifier init]_block_invoke.44
- ___40-[PowerUISmartChargeManager disableDEoC]_block_invoke_2
- ___42-[PowerUISmartChargeClient powerLogStatus]_block_invoke.136
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1000
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1004
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.1005
- ___44-[PowerUISmartChargeManager recordAnalytics]_block_invoke.981
- ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.288
- ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.292
- ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.296
- ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.298
- ___47-[PowerUIAudioAccessorySmartChargeManager init]_block_invoke.300
- ___47-[PowerUIDemoCECManager monitorPluggedInChange]_block_invoke.124
- ___47-[PowerUISmartChargeClient fullChargeDeadline:]_block_invoke.137
- ___48-[PowerUICECManager monitorBatteryNotifications]_block_invoke.192
- ___50-[PowerUISmartChargeClient cecFullChargeDeadline:]_block_invoke.156
- ___51-[PowerUISmartChargeClient resetEngagementOverride]_block_invoke.159
- ___52-[PowerUICECGridDataManager timeToNextCleanInterval]_block_invoke.cold.2
- ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.161
- ___52-[PowerUISmartChargeClient lastUsedLeewayWithError:]_block_invoke.161.cold.1
- ___57-[PowerUISmartChargeManager client:setState:withHandler:]_block_invoke.1535
- ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.1625
- ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.1625.cold.1
- ___60-[PowerUISmartChargeManager accessoryNFCConnectionCallback:]_block_invoke.1625.cold.2
- ___62-[PowerUIDemoCECManager registerTimer:afterTime:withInterval:]_block_invoke
- ___63-[PowerUISmartChargeClientAudioAccessories getAvailableDevices]_block_invoke.105
- ___63-[PowerUISmartChargeClientAudioAccessories getStatusForDevice:]_block_invoke.107
- ___64-[PowerUISmartChargeClientAudioAccessories lastActionForDevice:]_block_invoke.109
- ___66-[PowerUISmartChargeClient legacy_client_isOBCEngagedWithHandler:]_block_invoke.143
- ___68-[PowerUISmartChargeClientAudioAccessories lastUsedLeewayWithError:]_block_invoke.111
- ___68-[PowerUISmartChargeClientAudioAccessories lastUsedLeewayWithError:]_block_invoke.111.cold.1
- ___72-[PowerUIChargeAwarenessNotifier displayNotificationForMCL:forWireless:]_block_invoke.116
- ___72-[PowerUIChargeAwarenessNotifier displayNotificationForMCL:forWireless:]_block_invoke.116.cold.1
- ___72-[PowerUIChargeAwarenessNotifier displayNotificationForMCL:forWireless:]_block_invoke.136
- ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.157
- ___76-[PowerUISmartChargeClient engageFrom:until:repeatUntil:overrideAllSignals:]_block_invoke.157.cold.1
- ___85-[PowerUISmartChargeClientAudioAccessories engageUntil:forDevice:overrideAllSignals:]_block_invoke.104
- ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.152
- ___87-[PowerUISmartChargeClient isOBCEngaged:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.152.cold.1
- ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.160
- ___87-[PowerUISmartChargeClient simulateCurrentOutputAsOfDate:overrideAllSignals:withError:]_block_invoke.160.cold.1
- ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.141
- ___94-[PowerUISmartChargeClient isOBCEngaged:isMaxChargeLimited:chargingOverrideAllowed:withError:]_block_invoke.141.cold.1
- ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.139
- ___95-[PowerUISmartChargeClient smartChargingUIState:chargeLimit:chargingOverrideAllowed:withError:]_block_invoke.139.cold.1
- ___96+[PowerUISmartChargeUtilities historicalFullChargeDurationStartingAt:withMinimumPluginDuration:]_block_invoke.83
- ___97+[PowerUISmartChargeUtilities drainSessionsInfoBetweenRelevantChargesBefore:withMinimumDuration:]_block_invoke.52
- ___block_descriptor_56_e8_32s40bs48bs_e18_B16?0"NSString"8ls32l8s40l8s48l8
- ___block_literal_global.102
- ___block_literal_global.1114
- ___block_literal_global.1154
- ___block_literal_global.1156
- ___block_literal_global.1187
- ___block_literal_global.1192
- ___block_literal_global.1348
- ___block_literal_global.146
- ___block_literal_global.150
- ___block_literal_global.155
- ___block_literal_global.197
- ___block_literal_global.2289
- ___block_literal_global.2291
- ___block_literal_global.253
- ___block_literal_global.36
- ___block_literal_global.43
- ___block_literal_global.51
- ___block_literal_global.82
- ___block_literal_global.85
- ___block_literal_global.938
- ___btConnectionUpdateCallback_block_invoke.316
- _objc_msgSend$chargeHistoryAnalytics
- _objc_msgSend$handlePauseChargingAboveMaxSOC
- _objc_msgSend$loadChargeLimitTokenForPreferenceKey:forReason:
- _objc_msgSend$localWakingRegistrationWithIdentifier:contextualPredicate:callback:
- _objc_msgSend$registerTimer:afterTime:withInterval:
- _registerTimer:afterTime:withInterval:.timerToken
CStrings:
+ "@\"ResourceHint\""
+ "AccumulatedSystemLoad"
+ "AccumulatedWallEnergyEstimate"
+ "Acknowledged record system load timer at time %@"
+ "B36@0:8q16Q24B32"
+ "Bad date formatting: unable to parse string date: %@ into date."
+ "Battery SOC change"
+ "Called for battery level=%d, externalConnected=%u - current checkpoint: %lu"
+ "Charge limit %hhu requested, but is unchanged"
+ "Continue limiting to %lu%% for reason '%@'"
+ "Could not load dynamic_scheduling.mlmodelc in the bundle resource"
+ "Demo CEC now enabled. Triggering callback to evaluate engagement."
+ "Either key or dictionary is null. Returning default value: %ld."
+ "Encountered missing value for %@. Filling with default value: %ld."
+ "Engagement result missing. Assuming device was not in an active engaged session."
+ "Evaluated and decided not to engage: no forecast available or not enough variation in grid (balancingAuthority: %@)"
+ "Feature enabled"
+ "Forcing noChargeToFullFlag for charge limit '%@' "
+ "Found start time of interval: %@ (for check time: %@)"
+ "Idled minutes in last session: %@"
+ "Last system load value following the end of the session not yet recorded, evaluating whether to record.."
+ "Legitimate Usage = %d"
+ "Limited charging to %lu%% for reason '%@'"
+ "Loaded Settings: Enabled=%u, CurrentState=%lu, Signals Ignored=%u, Desktop device=%u, Manual Charge Limit=%lu, Predictor = %@, Full Charge Deadline=%@, EngagementTimeOverride=%@, FullChargeDeadlineOverride=%@, repeatEngagementOverrideEndDate=%@ OverrideAllSignals=%@ minutesToFullCharge=%f"
+ "Logged new accumulated load value of %@ for interval start date %@. Updated list of all logged values: %@."
+ "Missing average emissions for session starting %@. Defaulting to -1."
+ "Missing system load values for either the start or end of the interval (%@ - %@). Unable to compute the load over the interval. Not using this hour's (load x emissions) in the savings computation."
+ "Missing value for the starting accumulated wall energy. Unable to compute total energy used over session."
+ "Most recent SmartCharging mode of operation: %@"
+ "No future clean intervals: not registering clean-segment timer."
+ "No previous evaluation check date set. Re-evaluating whether or not to engage for the next %.0lf hours."
+ "No upcoming clean intervals. All clean intervals already occurred!"
+ "Overriding debounce time to %@ seconds"
+ "Overriding recently connected duration to %@ seconds"
+ "Plugin Notification error: Not enough history, do not post"
+ "Posting metrics from DRA predictions"
+ "PowerTelemetryData"
+ "Previous values %@"
+ "Previously determined engagement opportunity before emergency charging. Checking if we're still within the %.0lf hour session."
+ "Reached emergency charge state outside of an engaged session, which should not be possible. Evaluating as a new session."
+ "Registering analytics timer for waitTime: %.0f minutes and interval: %.0f minutes"
+ "Registering engagement timer for waitTime: %.0f minutes"
+ "Remaining in evaluated and not-engaged phase."
+ "Running DEoC disablement request"
+ "Running DEoC enablement request"
+ "SELF.%@.value.externalConnected = %@ AND SELF.%@.value <= %@"
+ "SELF.%@.value.externalConnected = %@ AND SELF.%@.value = %@"
+ "SELF.%@.value.externalConnected = %@ AND SELF.%@.value >= %@"
+ "Sent engagementEvent: EventType: %d - Mode: %d - SoC: %d - TargetSoC: %d - PredictedEoC: %f"
+ "Setting lastUnplugged date to %@"
+ "Starting accumulated system load logging timer for every %ld mins starting %ld mins from now"
+ "System load computed over the interval from %@ - %@ was negative. Previous accumulated load value: %@, current accumulated load value: %@, delta: %f. The device may have been restarted, or the accumulator may have exceeded the 64-bit max. Not using this hour's (load x emissions) in the savings computation."
+ "T@\"NSDate\",&,N,V_lastUnpluggedDate"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_analyticsTimer"
+ "T@\"NSObject<OS_os_log>\",&,N,V_verboseLog"
+ "T@\"ResourceHint\",&,N,V_resourceHint"
+ "TQ,N,V_engagementDecisionReason"
+ "Td,N,V_charge_duration"
+ "Total wall energy computed over the session was negative (start value: %@. end value: %@. The device may have been restarted (deviceWasRestarted: %d), or the accumulator may have exceeded the 64-bit max. Returning -1."
+ "Unable to compute emissions savings from wall energy over session. Defaulting to -1."
+ "Unable to compute total wall energy used over session. Defaulting to -1."
+ "Unable to get interval start times"
+ "Unable to get stored forecasts in order to calculate average emissions based on system load"
+ "Unable to get the current interval start time. Checking whether we're logging the final load value and within one hour of the session end."
+ "Unable to get the current interval start time. Setting a default timer starting %ld mins from now"
+ "Unable to get the current interval start time: forecast is unavailable or the current time is outside the forecast horizon by more than one hour."
+ "Unable to get the current value for accumulated system load to store in defaults."
+ "Unable to get the current value for accumulated wall energy to store in defaults."
+ "Unable to get the current value for accumulated wall energy. Unable to compute total energy used over session."
+ "Unable to match current time to any intervals (current time: %@, all intervals: %@)"
+ "Updated values %@"
+ "Wall energy estimate over session %.2f Wh"
+ "^{__CFString=}36@0:8@16@24B32"
+ "_analyticsTimer"
+ "_charge_duration"
+ "_engagementDecisionReason"
+ "_lastUnpluggedDate"
+ "_resourceHint"
+ "_verboseLog"
+ "addObserverForName:object:queue:usingBlock:"
+ "analyticsTimer"
+ "bolt.and.smog.fill"
+ "bolt.badge.clock.fill"
+ "chargeHistoryAnalytics:"
+ "chargeSocLimitOwner"
+ "code"
+ "com.apple.das.smartcharging.analytics.countCECSessions"
+ "com.apple.das.smartcharging.analytics.countCECSessionsEnabled"
+ "com.apple.das.smartcharging.analytics.countCECSessionsEnabledSessionsTempDisabled"
+ "com.apple.das.smartcharging.analytics.countDEoCSessions"
+ "com.apple.das.smartcharging.analytics.countDEoCSessionsEnabled"
+ "com.apple.das.smartcharging.analytics.countDEoCSessionsTempDisabled"
+ "com.apple.das.smartcharging.analytics.countOBCSessions"
+ "com.apple.das.smartcharging.analytics.countOBCSessionsEnabled"
+ "com.apple.das.smartcharging.analytics.countOBCSessionsTempDisabled"
+ "com.apple.das.smartcharging.analytics.countTotalMinutesIdledInCEC"
+ "com.apple.das.smartcharging.analytics.countTotalMinutesIdledInDEoC"
+ "com.apple.das.smartcharging.analytics.countTotalMinutesIdledInMCL"
+ "com.apple.das.smartcharging.analytics.countTotalMinutesIdledInOBC"
+ "com.apple.das.smartcharging.analytics.countTotalMinutesIdledInOptimizedLimitCharge"
+ "com.apple.powerui.chargeAwarenessNotifier"
+ "com.apple.powerui.democec.batterySocLevel"
+ "com.apple.powerui.mclstatuschanged"
+ "com.apple.smartcharging.plugoutpredictions.dra"
+ "com.apple.system.powersources.chargingtofulloverride"
+ "d24@0:8q16"
+ "dateDictionaryFromDefaults:"
+ "demoCecAccumWallEnergyStart"
+ "demoCecSysLoadTimeline"
+ "deviceWasRestarted"
+ "draError: %@"
+ "draPredictionInfo"
+ "dynamic_scheduling"
+ "dynamic_schedulingInput"
+ "dynamic_schedulingOutput"
+ "emissionsSavingsFromSysLoad"
+ "emissionsSavingsFromWallEnergy"
+ "engagementDecision"
+ "engagementDecisionReason"
+ "getCECLifetimeValues"
+ "handleIsEnabledChange"
+ "handlePauseChargingAboveMaxSOC:"
+ "initWithCharge_duration:"
+ "initWithResourceType:andState:"
+ "intervalStartTimesOverForecastHorizon:"
+ "isEnabled check returned same state (%@) as before. Doing nothing."
+ "isWithinEngagedSession"
+ "lastIntervalStartTimeOverForecastHorizon:"
+ "lastUnpluggedDate"
+ "lifeTimeIdleHoursCEC"
+ "lifeTimeIdleHoursMCL"
+ "lifeTimeIdleHoursOBC"
+ "lifeTimeSessionCECEnabled"
+ "lifeTimeSessionCECEngaged"
+ "lifeTimeSessionMCLEnabled"
+ "lifeTimeSessionMCLEngaged"
+ "lifeTimeSessionOBCEnabled"
+ "lifeTimeSessionOBCEngaged"
+ "lifetimeIdleDurationMinsForMode"
+ "lifetimeSessions"
+ "lifetimeSessionsEnabled"
+ "lifetimeSessionsTempDisabled"
+ "loadChargeLimitTokenForPreferenceKey:forReason:verbose:"
+ "mainQueue"
+ "monitorDemoCecIsEnabledChange"
+ "mostRecentOBCModeOfoperationFromTimeline"
+ "notEngagedReason"
+ "numberForKey:fromDict:withDefault:"
+ "obcModeOfOperation"
+ "orPredicateWithSubpredicates:"
+ "overpredicted"
+ "overrideRecentDeviceConnectedToChargerThresholdSeconds"
+ "postAnalyticsEventForDynamicRuntimeAllocationWithPredictedDurationMinutes:andActualDurationMinutes:andEngagementDecision:andWasWireless:andSPIError:"
+ "queryReturnedError"
+ "readLifetimeCECEngagementValues"
+ "recordLifetimeValues:"
+ "recordStartWallEnergyAccum"
+ "recordSystemLoadAccum"
+ "registerAnalyticsTimer:afterTime:withInterval:"
+ "registerEngagementTimer"
+ "registerEngagementTimer:afterTime:withInterval:"
+ "resourceHint"
+ "returnedError"
+ "setAnalyticsTimer:"
+ "setChargeLimitTo:forLimitType:setNoChargeToFull:"
+ "setCharge_duration:"
+ "setEngagementDecisionReason:"
+ "setLastUnpluggedDate:"
+ "setResourceHint:"
+ "setSound:"
+ "setVerboseLog:"
+ "smartChargeManager"
+ "smartChargeManager init complete!"
+ "smartChargeManagerVerbose"
+ "startSessionTimers"
+ "startSystemLoadAccumTimer"
+ "startTimeCurrentIntervalWithinForecastHorizon:"
+ "systemLoadEmissionSavings:"
+ "time:isWithinIntervalWithStart:"
+ "totalWallEnergy"
+ "totalWallEnergyOverSession"
+ "unpluggedDateInterval"
+ "updateResourceHint"
+ "updateState:"
+ "utilization"
+ "v16@?0@\"NSNotification\"8"
+ "v44@0:8q16q24B32B36B40"
+ "verboseLog"
+ "withinFiftyPercent"
- "(SELF.%@.value.externalConnected = %@)"
- "Called for battery level=%d, externalConnected=%u"
- "Checkpoint: %@"
- "Demo CEC is no longer enabled. Disengaging and resetting state."
- "Evaluated and decided not to engage: no forecast available or not enough variation in grid."
- "Evaluated and should engage after ending emergency charge"
- "Legitimate Usage = 0"
- "Limited charging to %lu for reason '%@'"
- "Loaded Settings: Enabled=%u, CurrentState=%lu, Signals Ignored=%u, Desktop device=%u, Manual Charge Limit=%lu, Predictor = %@, Full Charge Deadline=%@, EngagementTimeOverride=%@, FullChargeDeadlineOverride=%@, repeatEngagementOverrideEndDate=%@ OverrideAllSignals=%@"
- "Missing average emissions for session starting %@"
- "No previous evaluation check date set. Re-evaluating whether to engage for the next %.0lf hours."
- "No upcoming clean intervals. All clean intervals already occured!"
- "Owner"
- "Queuing engagementEvent"
- "Registering timer"
- "Sent engagementEvent Event: SoC: %d - TargetSoC: %d - PredictedEoC: %f - Mode: %d - event: %d"
- "Should re-evaluate engagement %d"
- "Unkown"
- "chargeHistoryAnalytics"
- "com.apple.das.smartcharging.analytics.countChargeSessionsEnabled"
- "com.apple.das.smartcharging.analytics.countMCLChargeSessionsTempDisabled"
- "com.apple.das.smartcharging.analytics.countOptimizedLimitChargeSessionsEnabled"
- "com.apple.powerui.democec.batteryState"
- "com.apple.system.powersources.gaugingmitigation"
- "handlePauseChargingAboveMaxSOC"
- "loadChargeLimitTokenForPreferenceKey:forReason:"
- "localWakingRegistrationWithIdentifier:contextualPredicate:callback:"
- "registerTimer:afterTime:withInterval:"

```
