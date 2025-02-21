## PowerUI

> `/System/Library/PrivateFrameworks/PowerUI.framework/PowerUI`

```diff

-640.0.0.0.0
-  __TEXT.__text: 0xb62c8
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x1a04c
+651.0.0.0.0
+  __TEXT.__text: 0xbbcc4
+  __TEXT.__auth_stubs: 0xaf0
+  __TEXT.__objc_methlist: 0x1b0dc
   __TEXT.__const: 0x4d8
-  __TEXT.__cstring: 0xd60a
-  __TEXT.__oslogstring: 0x98b2
-  __TEXT.__gcc_except_tab: 0x1230
-  __TEXT.__unwind_info: 0x1ac8
-  __TEXT.__objc_classname: 0xac1
-  __TEXT.__objc_methname: 0x3d395
-  __TEXT.__objc_methtype: 0x4016
-  __TEXT.__objc_stubs: 0xc080
-  __DATA_CONST.__got: 0x4c0
-  __DATA_CONST.__const: 0x1400
-  __DATA_CONST.__objc_classlist: 0x2c8
+  __TEXT.__cstring: 0xd8e3
+  __TEXT.__oslogstring: 0xa9d8
+  __TEXT.__gcc_except_tab: 0x1234
+  __TEXT.__unwind_info: 0x1bf8
+  __TEXT.__objc_classname: 0xb0f
+  __TEXT.__objc_methname: 0x3dac0
+  __TEXT.__objc_methtype: 0x4090
+  __TEXT.__objc_stubs: 0xc520
+  __DATA_CONST.__got: 0x4e8
+  __DATA_CONST.__const: 0x13e0
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4f08
+  __DATA_CONST.__objc_selrefs: 0x5250
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x2b8
   __DATA_CONST.__objc_arraydata: 0x6e70
-  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__auth_got: 0x588
   __AUTH_CONST.__const: 0x640
-  __AUTH_CONST.__cfstring: 0xb280
-  __AUTH_CONST.__objc_const: 0x36b98
-  __AUTH_CONST.__objc_intobj: 0x888
+  __AUTH_CONST.__cfstring: 0xb620
+  __AUTH_CONST.__objc_const: 0x35b30
+  __AUTH_CONST.__objc_intobj: 0x8e8
   __AUTH_CONST.__objc_arrayobj: 0x378
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_dictobj: 0x280
-  __AUTH.__objc_data: 0x1270
-  __DATA.__objc_ivar: 0x3b40
+  __AUTH.__objc_data: 0x1310
+  __DATA.__objc_ivar: 0x3b9c
   __DATA.__data: 0x6c0
-  __DATA.__bss: 0xc0
-  __DATA_DIRTY.__objc_data: 0x960
+  __DATA.__bss: 0xd8
+  __DATA_DIRTY.__objc_data: 0x9b0
   __DATA_DIRTY.__data: 0x20
-  __DATA_DIRTY.__bss: 0x170
+  __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/GridDataServices.framework/GridDataServices
   - /System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode
   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
+  - /System/Library/PrivateFrameworks/MobileStoreDemoKit.framework/MobileStoreDemoKit
   - /System/Library/PrivateFrameworks/MobileTimer.framework/MobileTimer
   - /System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence
   - /System/Library/PrivateFrameworks/PassKitCore.framework/PassKitCore

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 9478
-  Symbols:   9984
-  CStrings:  7012
+  Functions: 9632
+  Symbols:   10162
+  CStrings:  7191
 
Symbols:
+ _OBJC_CLASS_$_MSDKDemoState
+ _OBJC_CLASS_$_MSDKManagedDevice
+ _OBJC_CLASS_$_PowerUICECGridDataForecastEntry
+ _OBJC_CLASS_$_PowerUICECUtilities
+ _OBJC_CLASS_$_PowerUIDemoCECManager
+ _OBJC_METACLASS_$_PowerUICECGridDataForecastEntry
+ _OBJC_METACLASS_$_PowerUICECUtilities
+ _OBJC_METACLASS_$_PowerUIDemoCECManager
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "\x13$"
+ "%@: (%@)"
+ "(\x12\x12"
+ "(SELF.%@.value.externalConnected = %@)"
+ "<%@:%p %@>"
+ "@\"PowerUICECGridDataManager\""
+ "@40@0:8@16Q24Q32"
+ "Already evaluated shouldChargeNow in last %lu mins. Skipping"
+ "B32@0:8@16d24"
+ "Bad date formatting: unable to parse string date into date. Not including in analytics."
+ "Charged to acceptable limit (= batteryLevel %ld >= kEmergencyChargeSocEndThreshold = %ld). Ending emergency charge."
+ "Charging history timeline %@"
+ "Charging state changed: %@"
+ "Cleanest %ld intervals:"
+ "Current time (%@) within clean window starting at %@"
+ "Current time NOT in clean window intervals (current time: %@, clean intervals: %@)"
+ "DEoC override in place, but is supressed due to system conditions"
+ "Demo CEC Engaged: Changed states. Previously was charging = %@, now is charging = %@."
+ "Demo CEC Engaged: in a clean energy window. Charging."
+ "Demo CEC Engaged: in a dirty window. Charging paused."
+ "Demo CEC Phase update from %lu to %lu (%@ --> %@); BatteryLevel %ld, PluggedIntoEligibleSource %d"
+ "Demo CEC State set to: %@"
+ "Demo CEC State: %@"
+ "Demo CEC changed charging states. Previously was charging = %@, now is charging = %@."
+ "Demo CEC is either not supported or disabled. Skipping"
+ "Demo CEC is no longer enabled. Disengaging and resetting state."
+ "DemoCECManager Loaded state from defaults. isDemoCECEnabled %@, lastPluggedInDate %@, pluggedInBatteryLevel %ld, _lastEngagementCheckDate %@,"
+ "DemoCECManager initializing. Was the device restarted: %@"
+ "Determined clean forecast threshold of %lu"
+ "Device no longer plugged into an eligible power source. Disengaging and resetting state."
+ "Device no longer plugged into eligible source."
+ "Downsampling grid data from startResolution = %lu mins to endResolution = %lu mins."
+ "Emergency Charge"
+ "Emergency charging"
+ "Empty forecast. Not engaging."
+ "Enabling emergency charge."
+ "Engaged..."
+ "Engaging for the current session."
+ "Error returned in isDeviceEnrolledWithDeKOTA check: %@"
+ "Error returned in isSecureDemoModeEnabled check: %@"
+ "Evaluated and decided not to engage"
+ "Evaluated and decided not to engage: no forecast available or not enough variation in grid."
+ "Evaluated and decided to engage"
+ "Evaluated and should engage after ending emergency charge"
+ "Evaluating engagement for current plug-in."
+ "Evaluating phase. Trigger: %@ (CurrentPhase %lu batteryLevel %ld, isPluggedIntoEligibleSource %d)"
+ "Exiting from a session previously engaged/deemed eligible"
+ "Figuring out cleanest %.2ld hours from %.02lf hours"
+ "Forecast had insufficient number of entries. Requires at least two distinct entries, but got %lu."
+ "Last engagement check date missing. Unable to determine session length."
+ "Last evaluated engagement %.0lf hours ago (at: %@). Re-evaluating whether or not to engage for the next %.0lf hours."
+ "Missing average emissions for session starting %@"
+ "Missing emissions for charge time %@"
+ "No forecast currently stored in currentForecast. Checking forecasts stored in defaults."
+ "No forecasts stored in defaults."
+ "No forecasts stored in defaults. Returning nil."
+ "No previous evaluation check date set. Re-evaluating whether to engage for the next %.0lf hours."
+ "Not enough variation in forecast values (%lf - %lf). Required variation = %lf."
+ "Pausing charging while SOC is above %ld."
+ "PowerUICECGridDataForecastEntry"
+ "PowerUICECUtilities"
+ "PowerUIDemoCECManager"
+ "Registering timer"
+ "Relevant forecast is  %@"
+ "Reported Demo CEC metrics to CoreAnalytics %@"
+ "Resampled from startResolution = %lu mins to endResolution = %lu mins. Starting array: %@, ending array: %@ "
+ "Resetting state"
+ "SOC fell below acceptable limit (batteryLevel = %ld <= kEmergencyChargeSocStartThreshold = %ld). Deciding to emergency charge regardless of grid."
+ "SOC is above upper charge limit (batteryLevel = %ld >= kUpperChargeLimit = %ld). Pausing charging regardless of grid."
+ "SOC is below acceptable limit (batteryLevel = %ld <= kEmergencyChargeSocStartThreshold = %ld). Deciding to emergency charge regardless of grid."
+ "Same resolution specified, returning original data."
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
+ "Unable to get stored forecasts in order to calculate average emissions."
+ "Unable to get stored forecasts. Unknown emissions for time %@"
+ "Unregistering timer"
+ "User state setting"
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
+ "battLevel"
+ "chargeHistoryAnalytics"
+ "chargingEmissions"
+ "chargingStateIsCharging"
+ "cleanIntervalsStringFromDates:withIntervalDuration:"
+ "cleanestIntervals"
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
+ "downsampleGridData:fromRes:toRes:"
+ "emergencyChargeTime"
+ "emissionsForTime:overForecastHorizon:"
+ "endResolution must be coarser than startResolution, but got startResolution = %lu and endResolution = %lu"
+ "endResolution must be multiple of startResolution, but got startResolution = %lu and endResolution = %lu"
+ "enoughVariationForForecast:withMinDifference:"
+ "evaluateEngagement"
+ "evaluateShouldChargeNow"
+ "forecastDate"
+ "forecastFetchDate"
+ "forecastFromDefaults"
+ "forecastValue"
+ "forecastValues array is empty - nothing to resample. Returning."
+ "gridDataManager"
+ "handleEmergencyCharge"
+ "handleEngagement"
+ "handlePauseChargingAboveMaxSOC"
+ "indexOfObject:"
+ "initWithContextStore:"
+ "initWithDate:forecastValue:"
+ "intervalDuration"
+ "isCleanEnergyChargingEnabled"
+ "isDemoCECEnabled"
+ "isDemoCECSupported"
+ "isDemoCecFlagEnabledForStore"
+ "isDemoDevice"
+ "isDemoMode"
+ "isDeviceEnrolledWithDeKOTA:"
+ "isPluggedIntoEligiblePowerSourceWithContext:"
+ "isSecureDemoModeEnabled:"
+ "lastEngagementCheckDate"
+ "lastForecastFetchDate"
+ "lastPauseChargingCheckDate"
+ "latestBalancingAuthority"
+ "loadStateFromDefaults"
+ "monitorBatteryStateOfChargeChange"
+ "monitorPluggedInChange"
+ "q32@0:8@16d24"
+ "recordChargingStateChange:atBatteryLevel:duringCleanInterval:"
+ "recordEngagementEvaluation:"
+ "recordForecastInDefaults:"
+ "registerTimer:afterTime:withInterval:"
+ "sessionLength"
+ "setDesktopMode:withHandler:"
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
+ "totalChargeTime"
+ "unregisterTimer:"
+ "v32@0:8B16q20B28"
+ "v32@0:8d16q24"
+ "v40@0:8@16d24d32"
+ "wasCleanInterval"
- "\x13\x13"
- "Current time NOT in clean window intervals %@"
- "Current time within clean window startin at %@"
- "Empty forecast. Not engaging"
- "Not enough variation in forecast values (%lf - %lf)"
- "Relavant forecast is  %@"
- "Unsupported CEC State: %@"
- "cleanIntervalsStringFromDates:"
- "enoughVariationForForecast:"
- "forecastMapFrom:ofInterval:"
- "isPluggedIntoEligiblePowerSource"
- "prefs:root=BATTERY_USAGE&path=CHARGING_TITLE"
- "q24@?0@\"NSNumber\"8@\"NSNumber\"16"

```
