## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-3486.42.1.0.0
-  __TEXT.__text: 0x1e3c5c
-  __TEXT.__objc_methlist: 0x11300
-  __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x26c67
-  __TEXT.__oslogstring: 0x15fdd
+3486.60.36.0.0
+  __TEXT.__text: 0x1e6df4
+  __TEXT.__objc_methlist: 0x11568
+  __TEXT.__const: 0x720
+  __TEXT.__cstring: 0x26f68
+  __TEXT.__oslogstring: 0x16688
   __TEXT.__gcc_except_tab: 0x25a4
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x6098
+  __TEXT.__unwind_info: 0x6120
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x45b8
-  __DATA_CONST.__objc_classlist: 0x3a8
+  __DATA_CONST.__const: 0x45c8
+  __DATA_CONST.__objc_classlist: 0x3b8
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb2d8
+  __DATA_CONST.__objc_selrefs: 0xb3e0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x2e0
-  __DATA_CONST.__objc_arraydata: 0x16478
-  __DATA_CONST.__got: 0xf88
-  __AUTH_CONST.__const: 0x1a80
-  __AUTH_CONST.__cfstring: 0x34380
-  __AUTH_CONST.__objc_const: 0x16b00
+  __DATA_CONST.__objc_arraydata: 0x165c0
+  __DATA_CONST.__got: 0xf98
+  __AUTH_CONST.__const: 0x1ae0
+  __AUTH_CONST.__cfstring: 0x346c0
+  __AUTH_CONST.__objc_const: 0x16f90
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__objc_intobj: 0x28e0
-  __AUTH_CONST.__objc_dictobj: 0x3b38
-  __AUTH_CONST.__objc_doubleobj: 0xba0
-  __AUTH_CONST.__objc_arrayobj: 0x3060
-  __AUTH_CONST.__auth_got: 0xe08
-  __AUTH.__objc_data: 0xc08
-  __DATA.__objc_ivar: 0x16ec
+  __AUTH_CONST.__objc_intobj: 0x29d0
+  __AUTH_CONST.__objc_dictobj: 0x3bd8
+  __AUTH_CONST.__objc_doubleobj: 0xc10
+  __AUTH_CONST.__objc_arrayobj: 0x30c0
+  __AUTH_CONST.__auth_got: 0xe10
+  __AUTH.__objc_data: 0xca8
+  __DATA.__objc_ivar: 0x1724
   __DATA.__data: 0x580
   __DATA.__common: 0x74
   __DATA_DIRTY.__objc_data: 0x1888

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 8864
-  Symbols:   11993
-  CStrings:  9134
+  Functions: 8925
+  Symbols:   12081
+  CStrings:  9187
 
Symbols:
+ +[PLAggregateSummarizationService _chunkNormalizationPropertyMappings]
+ +[PLBatteryAgent meetsTLCNotificationConditionsWithChargingState:uisoc:]
+ -[PLBatteryAgent lastFedDetails]
+ -[PLBatteryAgent logFedDetailsToCA:forPort:]
+ -[PLBatteryAgent setLastFedDetails:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation .cxx_destruct]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation addUsageTimesWithScreenOnTime:screenOffTime:toDaySummary:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation appsForDay:withDrainSummary:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation coalesce]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation configure:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation dailyDrainInformationWithFullDayBreakdown:dynamicDayBreakdown:drainSummaries:screenOnTimes:screenOffTimes:screenTimesEndDate:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation days]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation dependencies]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation drainSummaries]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation dynamicDayBreakdown]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation fullDayBreakdown]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation responderService]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation result]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation run]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation screenOffTimes]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation screenOnTimes]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation screenTimesEndDate]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation screenTimesIndexForDay:bucketCount:endDate:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation setDays:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation setDrainSummaries:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation setDynamicDayBreakdown:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation setFullDayBreakdown:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation setResponderService:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation setScreenOffTimes:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation setScreenOnTimes:]
+ -[PLBatteryUIResponseTypeMergedDailyDrainInformation setScreenTimesEndDate:]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation .cxx_destruct]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation batteryLevels]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation chargingStateIntervals]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation coalesce]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation configure:]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation days]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation dependencies]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation endTime]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation hourlyChargingInformationWithBatteryLevels:chargingStateIntervals:endTime:]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation hoursWithBatteryLevels:firstIndex:windowStart:hasLevelData:]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation intervalsForDay:windowStart:]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation responderService]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation result]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation run]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation setBatteryLevels:]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation setChargingStateIntervals:]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation setDays:]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation setEndTime:]
+ -[PLBatteryUIResponseTypeMergedHourlyChargingInformation setResponderService:]
+ -[PLEnergyIssuesService teardownOperatorDependancies]
+ GCC_except_table139
+ GCC_except_table143
+ GCC_except_table196
+ GCC_except_table266
+ GCC_except_table268
+ GCC_except_table277
+ GCC_except_table284
+ GCC_except_table288
+ GCC_except_table331
+ GCC_except_table334
+ GCC_except_table338
+ _CFDataGetTypeID
+ _OBJC_CLASS_$_PLBatteryUIResponseTypeMergedDailyDrainInformation
+ _OBJC_CLASS_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation
+ _OBJC_IVAR_$_PLBatteryAgent._lastFedDetails
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedDailyDrainInformation._days
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedDailyDrainInformation._drainSummaries
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedDailyDrainInformation._dynamicDayBreakdown
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedDailyDrainInformation._fullDayBreakdown
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedDailyDrainInformation._responderService
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedDailyDrainInformation._screenOffTimes
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedDailyDrainInformation._screenOnTimes
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedDailyDrainInformation._screenTimesEndDate
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation._batteryLevels
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation._chargingStateIntervals
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation._days
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation._endTime
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation._responderService
+ _OBJC_METACLASS_$_PLBatteryUIResponseTypeMergedDailyDrainInformation
+ _OBJC_METACLASS_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation
+ __OBJC_$_INSTANCE_METHODS_PLBatteryUIResponseTypeMergedDailyDrainInformation
+ __OBJC_$_INSTANCE_METHODS_PLBatteryUIResponseTypeMergedHourlyChargingInformation
+ __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIResponseTypeMergedDailyDrainInformation
+ __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIResponseTypeMergedHourlyChargingInformation
+ __OBJC_$_PROP_LIST_PLBatteryUIResponseTypeMergedDailyDrainInformation
+ __OBJC_$_PROP_LIST_PLBatteryUIResponseTypeMergedHourlyChargingInformation
+ __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIResponseTypeMergedDailyDrainInformation
+ __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation
+ __OBJC_CLASS_RO_$_PLBatteryUIResponseTypeMergedDailyDrainInformation
+ __OBJC_CLASS_RO_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation
+ __OBJC_METACLASS_RO_$_PLBatteryUIResponseTypeMergedDailyDrainInformation
+ __OBJC_METACLASS_RO_$_PLBatteryUIResponseTypeMergedHourlyChargingInformation
+ ___44-[PLBatteryAgent logFedDetailsToCA:forPort:]_block_invoke
+ ___73-[PLBatteryUIResponseTypeBatteryBreakdown applyStaticNameTransformation:]_block_invoke
+ ___86-[PLBatteryUIResponseTypeMergedHourlyChargingInformation intervalsForDay:windowStart:]_block_invoke
+ _applyStaticNameTransformation:.recapBundleIDs
+ _applyStaticNameTransformation:.recapOnce
+ _applyStaticNameTransformationsWithEnergyEntries:.recapBundleIDs
+ _applyStaticNameTransformationsWithEnergyEntries:.recapOnce
- GCC_except_table138
- GCC_except_table195
- GCC_except_table265
- GCC_except_table267
- GCC_except_table275
- GCC_except_table281
- GCC_except_table287
- GCC_except_table330
- GCC_except_table333
- GCC_except_table337
- GCC_except_table82
- ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
CStrings:
+ "%@ recapsEnergy: %.3f, batteryPercent %.3f"
+ "CACHED"
+ "Checking %@ with flags %u"
+ "Could not get eachFlags"
+ "Could not get flags"
+ "ExclavesInferenceProvider"
+ "FedCapabilityData"
+ "FedExtSrcCapProductID"
+ "FedExtSrcCapVendorID"
+ "FedMaxCurrent"
+ "FedMaxPower"
+ "FedMaxVoltage"
+ "FedWPDebugData"
+ "FedWPPolicyData"
+ "INSTANT"
+ "Merged Daily Drain Information: \"bui_25\" feature flag is disabled, skipping"
+ "Merged Daily Drain Information: %lu days"
+ "Merged Daily Drain Information: not enough breakdown information"
+ "Merged Hourly Charging Information: \"bui_25\" feature flag is disabled, skipping"
+ "Merged Hourly Charging Information: %lu days"
+ "Merged Hourly Charging Information: not enough battery level information"
+ "PLBatteryUIAnomalousQualifierKey"
+ "PLBatteryUIAppRecapEnergyUsedKey"
+ "PLBatteryUIDailyDrainInformationKey"
+ "PLBatteryUIDrainToday"
+ "PLBatteryUIGraphChargingIntervalTypeKey"
+ "PLBatteryUIHourlyChargingInformationKey"
+ "PLBatteryUIHourlyChargingIntervalsKey"
+ "PLBatteryUIHourlyHasDataKey"
+ "PLBatteryUIHourlyIsChargingKey"
+ "PLBatteryUIHourlyIsCriticalKey"
+ "PLBatteryUIHourlyIsInterpolatedKey"
+ "PLBatteryUIHourlyIsLowPowerModeKey"
+ "PLBatteryUIHourlyLevelKey"
+ "PLBatteryUIHourlyLevelsKey"
+ "Pushing FedDetails metrics for port %d to CA: %@"
+ "SiriRecap"
+ "Skip %@ with flags %u - not a full AP wake reason"
+ "UNUSABLE"
+ "WiFi cumulative UNUSABLE: hasLastEntry=%{public}d wifiPowered=%{public}d"
+ "WiFi cumulative dataset=%{public}s (valid=%{public}d hasLastEntry=%{public}d instantTs=%{public}lu cachedTs=%{public}lu lastLoggedTs=%{public}lu)"
+ "WiFi cumulative entry stashed in lastEntryForMetricd, not persisted"
+ "WiFi cumulative entry ts=%{public}@ hasLastEntry=%{public}d metricd=%{public}d"
+ "WiFi power properties not logged from %{public}@: available=NO"
+ "WiFi power properties not logged: no wifi manager/device (manager=%{public}d device=%{public}d)"
+ "WiFi power-off cumulative entry stashed in lastEntryForMetricd, not persisted"
+ "WiFiDeviceClientCopyProperty(POWER_DEBUG_INFO) returned a non-dictionary value: class=%{public}@"
+ "WiFiDeviceClientCopyProperty(POWER_DEBUG_INFO) returned an empty dictionary"
+ "WiFiDeviceClientCopyProperty(POWER_DEBUG_INFO) returned nil, power properties not logged (associated=%{public}d)"
+ "campo"
+ "com.apple.ExclavesInferenceProvider"
+ "com.apple.conversationd"
+ "com.apple.power.battery.FedDetails"
+ "com.apple.power.camera.property9.activeDuration"
+ "conversationd"
+ "logEventBackwardWifiProperties: needModelPower=%{public}d metricd=%{public}d device=%{public}d"
+ "wifi properties: count=%{public}lu hasInstantTs=%{public}d hasCachedTs=%{public}d hasInstantPM=%{public}d hasInstantMPC=%{public}d"
- "1946944"
- "BatteryLife"
- "No wifi properties"
- "V68 SW"
```
