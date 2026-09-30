## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-2423.120.12.0.0
-  __TEXT.__text: 0x1d1350
-  __TEXT.__auth_stubs: 0x1d50
-  __TEXT.__objc_methlist: 0xe698
-  __TEXT.__const: 0x5f0
-  __TEXT.__cstring: 0x23440
-  __TEXT.__oslogstring: 0x137de
-  __TEXT.__gcc_except_tab: 0x2678
+2954.0.0.502.3
+  __TEXT.__text: 0x1c0360
+  __TEXT.__auth_stubs: 0x1b60
+  __TEXT.__objc_methlist: 0xe5e0
+  __TEXT.__const: 0x6a8
+  __TEXT.__cstring: 0x22eb6
+  __TEXT.__oslogstring: 0x11e7b
+  __TEXT.__gcc_except_tab: 0x25fc
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x3850
-  __TEXT.__objc_classname: 0xb96
-  __TEXT.__objc_methname: 0x308e5
-  __TEXT.__objc_methtype: 0x2707
-  __TEXT.__objc_stubs: 0x1e000
-  __DATA_CONST.__got: 0xe78
-  __DATA_CONST.__const: 0x44a8
+  __TEXT.__unwind_info: 0x3658
+  __TEXT.__objc_classname: 0xb7d
+  __TEXT.__objc_methname: 0x30a8c
+  __TEXT.__objc_methtype: 0x274d
+  __TEXT.__objc_stubs: 0x1e6a0
+  __DATA_CONST.__got: 0xe68
+  __DATA_CONST.__const: 0x4378
   __DATA_CONST.__objc_classlist: 0x308
-  __DATA_CONST.__objc_nlclslist: 0x110
+  __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x95b0
+  __DATA_CONST.__objc_selrefs: 0x96d8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x290
-  __DATA_CONST.__objc_arraydata: 0x159c8
-  __AUTH_CONST.__auth_got: 0xec0
-  __AUTH_CONST.__const: 0x1860
-  __AUTH_CONST.__cfstring: 0x31620
-  __AUTH_CONST.__objc_const: 0x11ea8
-  __AUTH_CONST.__objc_intobj: 0x2838
-  __AUTH_CONST.__objc_dictobj: 0x33e0
-  __AUTH_CONST.__objc_doubleobj: 0xb30
-  __AUTH_CONST.__objc_arrayobj: 0x2af0
-  __AUTH.__objc_data: 0x820
-  __AUTH.__data: 0x5a0
-  __DATA.__objc_ivar: 0x11dc
-  __DATA.__data: 0x650
-  __DATA.__bss: 0x27b0
-  __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x1630
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x3a8
+  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_arraydata: 0x14758
+  __AUTH_CONST.__auth_got: 0xdc8
+  __AUTH_CONST.__const: 0x1840
+  __AUTH_CONST.__cfstring: 0x31200
+  __AUTH_CONST.__objc_const: 0x11fe0
+  __AUTH_CONST.__objc_intobj: 0x25c8
+  __AUTH_CONST.__objc_dictobj: 0x3318
+  __AUTH_CONST.__objc_doubleobj: 0xb40
+  __AUTH_CONST.__objc_arrayobj: 0x29e8
+  __AUTH.__objc_data: 0x8c0
+  __DATA.__objc_ivar: 0x11fc
+  __DATA.__data: 0x400
+  __DATA.__bss: 0x2330
+  __DATA.__common: 0x74
+  __DATA_DIRTY.__objc_data: 0x1590
+  __DATA_DIRTY.__data: 0x10
+  __DATA_DIRTY.__bss: 0x3c0
   __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/UserNotifications.framework/UserNotifications
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AFKUser.framework/AFKUser
   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/ApplePhotonDetectorServices.framework/ApplePhotonDetectorServices

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 29A3F80D-E1CF-335D-AF67-6954BB03487D
-  Functions: 7910
-  Symbols:   26730
-  CStrings:  22320
+  UUID: A96A9130-52A1-3FBF-A48C-E97178950BAD
+  Functions: 7672
+  Symbols:   26062
+  CStrings:  22139
 
Symbols:
+ +[PLApplicationAgent entryEventForwardDefinitionRBSApplication]
+ +[PLBatteryUIResponseTypeUtilities getNonAppBundleIDs].cold.1
+ +[PLEnergyIssuesService isTestRackDevice:withExpGroup:internalKeyDetected:]
+ +[PLEnergyIssuesService shouldPopUpForPowerExceptionForProcess:]
+ +[PLEnergyIssuesService shouldPopUpForPowerExceptionForProcess:].cold.1
+ +[PLEnergyIssuesService shouldPopUpForPowerExceptionForProcess:].cold.2
+ +[PLEnergyIssuesService shouldPopUpForPowerExceptionWithFatalCount:withNonFatalCount:withMitigationsEnabled:]
+ +[PLProcessNetworkAgent isEnabled]
+ +[PLPushAgent entryAggregateDefinitionSentKeepAlive]
+ +[PLSleepWakeAgent entryEventPointDefinitionCoSocPower]
+ +[PLUtilities dateFromnSecEpoch:]
+ +[PLUtilities experimentGroup]
+ +[PLUtilities experimentGroup].cold.1
+ +[PLUtilities hasInternalKey:]
+ +[PLUtilities hasInternalKey:].cold.1
+ +[PLUtilities hasInternalKey:].cold.2
+ +[PLUtilities hasInternalKey]
+ +[PLUtilities hasInternalKey].cold.1
+ +[PLUtilities isPerfPowerMetricd]
+ +[PLUtilities isPerfPowerMetricd].cold.1
+ +[PLUtilities isPowerexceptionsd]
+ +[PLUtilities isPowerexceptionsd].cold.1
+ +[PLUtilities machTimeFromSeconds:]
+ +[PLUtilities machTimeFromSeconds:].cold.1
+ +[PLUtilities machTimeFromSeconds:].cold.2
+ +[PLUtilities machTimeFromSeconds:].cold.3
+ +[PLUtilities machTimeFromSeconds:].cold.4
+ +[PLUtilities pUUIDForPid:]
+ +[PPSFileUtilities containerPath]
+ +[PPSFileUtilities containerPath].cold.1
+ +[PPSFileUtilities(APFS) _debugStringForPurgeableLabel:]
+ +[PPSFileUtilities(APFS) _purgeableLabelWithUrgency:startDate:]
+ +[PPSFileUtilities(APFS) markAsPurgeable:label:]
+ +[PPSFileUtilities(APFS) markAsPurgeable:urgency:startDate:]
+ +[PPSFileUtilities(APFS) supportsEnhancedAPFS]
+ +[PPSFileUtilities(APFS) supportsEnhancedAPFS].cold.1
+ -[PLApplicationAgent RBSStatetoPLState:state:]
+ -[PLApplicationAgent logEventForwardRBSApplicationForBundleID:withPid:withState:withReasons:withVisibility:]
+ -[PLApplicationAgent logEventForwardRBSApplicationForBundleID:withPid:withState:withReasons:withVisibility:].cold.1
+ -[PLApplicationAgent stateDidChange:state:prevState:]
+ -[PLBatteryUIDrainDateInterval .cxx_destruct]
+ -[PLBatteryUIDrainDateInterval accumulatedDrainLevel]
+ -[PLBatteryUIDrainDateInterval description]
+ -[PLBatteryUIDrainDateInterval endDate]
+ -[PLBatteryUIDrainDateInterval initWithStartDate:endDate:]
+ -[PLBatteryUIDrainDateInterval initWithStartDate:endDate:accumulatedDrain:]
+ -[PLBatteryUIDrainDateInterval setAccumulatedDrainLevel:]
+ -[PLBatteryUIDrainDateInterval setEndDate:]
+ -[PLBatteryUIDrainDateInterval setStartDate:]
+ -[PLBatteryUIDrainDateInterval startDate]
+ -[PLBatteryUIInsightsAndSuggestionsSummary .cxx_destruct]
+ -[PLBatteryUIInsightsAndSuggestionsSummary autoBrightnessSuggestion]
+ -[PLBatteryUIInsightsAndSuggestionsSummary autolockSuggestion]
+ -[PLBatteryUIInsightsAndSuggestionsSummary coalesce]
+ -[PLBatteryUIInsightsAndSuggestionsSummary configure:]
+ -[PLBatteryUIInsightsAndSuggestionsSummary dependencies]
+ -[PLBatteryUIInsightsAndSuggestionsSummary getResultFromCacheForSuggestionResponseType:]
+ -[PLBatteryUIInsightsAndSuggestionsSummary insightSummaryResult]
+ -[PLBatteryUIInsightsAndSuggestionsSummary recentUsageInsight]
+ -[PLBatteryUIInsightsAndSuggestionsSummary reduceBrightnessSuggestion]
+ -[PLBatteryUIInsightsAndSuggestionsSummary responderService]
+ -[PLBatteryUIInsightsAndSuggestionsSummary result]
+ -[PLBatteryUIInsightsAndSuggestionsSummary run]
+ -[PLBatteryUIInsightsAndSuggestionsSummary setInsightSummaryResult:]
+ -[PLBatteryUIInsightsAndSuggestionsSummary setResponderService:]
+ -[PLBatteryUIInsightsAndSuggestionsSummary setSuggestionSummaryResult:]
+ -[PLBatteryUIInsightsAndSuggestionsSummary suggestionSummaryResult]
+ -[PLBatteryUINotificationService handleUrsaNotificationRequest:]
+ -[PLBatteryUINotificationService handleUrsaNotificationRequest:].cold.1
+ -[PLBatteryUINotificationService initializeUrsaNotifications]
+ -[PLBatteryUINotificationService ursaBaseContent]
+ -[PLBatteryUINotificationService ursaBootargContent:]
+ -[PLBatteryUINotificationService ursaBootargContent:].cold.1
+ -[PLBatteryUINotificationService ursaBootargContent:].cold.2
+ -[PLBatteryUINotificationService ursaBootargContent:].cold.3
+ -[PLBatteryUINotificationService ursaBootargContent:].cold.4
+ -[PLBatteryUINotificationService ursaRadarContent:]
+ -[PLBatteryUINotificationService ursaRadarContent:].cold.1
+ -[PLBatteryUINotificationService ursaRadarContent:].cold.2
+ -[PLBatteryUINotificationService ursaTTRContent:]
+ -[PLBatteryUINotificationService ursaTTRContent:].cold.1
+ -[PLBatteryUINotificationService ursaTTRContent:].cold.2
+ -[PLBatteryUINotificationService ursaTTRContent:].cold.3
+ -[PLBatteryUINotificationService ursaTTRContent:].cold.4
+ -[PLBatteryUIResponderService convertResponseToLegacyFormat:].cold.1
+ -[PLBatteryUIResponderService createCoalescedBreakdownWithResponse:]
+ -[PLBatteryUIResponderService getBreakdownForLength:fromCachedLength:forBucketSize:]
+ -[PLBatteryUIResponderService getBreakdownForLength:fromCachedLength:forBucketSize:].cold.1
+ -[PLBatteryUIResponderService getBreakdownForLength:fromCachedLength:forBucketSize:].cold.2
+ -[PLBatteryUIResponderService possibleRequests]
+ -[PLBatteryUIResponderService prepareBreakdown:withDrainSummaries:withFullDayBreakdown:withDynamicBreakdown:]
+ -[PLBatteryUIResponderService rangeKeyForLength:bucketSize:]
+ -[PLBatteryUIResponderService result].cold.6
+ -[PLBatteryUIResponderService setShouldUseMidnightQueryRange:]
+ -[PLBatteryUIResponderService shouldUseMidnightQueryRange]
+ -[PLBatteryUIResponseTypeBatteryBreakdown addTotals:with:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown adjustEnergyValues:].cold.2
+ -[PLBatteryUIResponseTypeBatteryBreakdown createPerAppBreakdown:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown dynamicEndOffset]
+ -[PLBatteryUIResponseTypeBatteryBreakdown excludeTimeOnCharger]
+ -[PLBatteryUIResponseTypeBatteryBreakdown getBatteryMaximumCapacityPercentWithError:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown getDrainPerBucketIn:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown isDynamicEnd]
+ -[PLBatteryUIResponseTypeBatteryBreakdown normalizeBucket:to:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown normalizeForBucket:with:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown percentageOption]
+ -[PLBatteryUIResponseTypeBatteryBreakdown setDynamicEndOffset:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown setExcludeTimeOnCharger:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown setIsDynamicEnd:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown setPercentageOption:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown setUiLevelDrainEntries:]
+ -[PLBatteryUIResponseTypeBatteryBreakdown uiLevelDrainEntries]
+ -[PLBatteryUIResponseTypeChargingStateIntervals bucketSize]
+ -[PLBatteryUIResponseTypeChargingStateIntervals dailyChargingStateIntervalsDict]
+ -[PLBatteryUIResponseTypeChargingStateIntervals dailyLastBattEntry]
+ -[PLBatteryUIResponseTypeChargingStateIntervals getBattUIEntriesWithKey:inRange:]
+ -[PLBatteryUIResponseTypeChargingStateIntervals getChargingStateIntervalsDictWithRange:addToDailyArrays:]
+ -[PLBatteryUIResponseTypeChargingStateIntervals organizeStateIntervalsWithRange:lastBattUIEntry:chargingIntervalsDict:addToDailyArrays:]
+ -[PLBatteryUIResponseTypeChargingStateIntervals resultArray]
+ -[PLBatteryUIResponseTypeChargingStateIntervals setBucketSize:]
+ -[PLBatteryUIResponseTypeChargingStateIntervals setDailyChargingStateIntervalsDict:]
+ -[PLBatteryUIResponseTypeChargingStateIntervals setDailyLastBattEntry:]
+ -[PLBatteryUIResponseTypeChargingStateIntervals setResultArray:]
+ -[PLBatteryUIResponseTypeChargingStateIntervals setShouldSnapInterval:]
+ -[PLBatteryUIResponseTypeChargingStateIntervals shouldSnapInterval]
+ -[PLBatteryUIResponseTypeChargingStateIntervals(Utilities) snapIntervals:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary .cxx_destruct]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary averageDrainRate]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary buckets]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary bundleIDToDisplayNameMap]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary coalesce]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary comparisonDateIntervalsWithTargetStartTime:withEndTime:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary comparisonType]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary configure:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary createAnomalousAppEntriesFrom:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary createAppDataMapForComparisonDateIntervals:currentDateInterval:targetTopApps:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary dependencies]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap].cold.1
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap].cold.2
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap].cold.3
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getEnergyForAppWithBundleID:inDateInterval:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getEnergyForQualificationID:withAppWithBundleID:inDateInterval:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getInstalledPluginToParentIDMap]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getNodeIDToNodeNameMap]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getParentBundleIDForBundleID:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary getUsageTimesForAppWithBundleID:inDateInterval:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary installedPluginToParentIDMap]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary intervalSummaryItems:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.1
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.10
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.11
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.2
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.3
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.4
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.5
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.6
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.7
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.8
+ -[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:].cold.9
+ -[PLBatteryUIResponseTypeDrainComparisonSummary middayFromMidnight:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary nodeIDToNodeNameMap]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary responderService]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary resultArray]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary result]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary run]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setAverageDrainRate:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setBuckets:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setBundleIDToDisplayNameMap:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setComparisonType:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setInstalledPluginToParentIDMap:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setNodeIDToNodeNameMap:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setResponderService:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setResultArray:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary setSuggest:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary sortedAppEnergyArrayFromAppDataMap:]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary suggest]
+ -[PLBatteryUIResponseTypeDrainComparisonSummary targetDateIntervalWithBucketStartTime:withEndTime:]
+ -[PLCoalitionAgent logCoalitionObjectMemory:]
+ -[PLCoalitionSample QOSBackground]
+ -[PLCoalitionSample QOSUserInitiated]
+ -[PLCoalitionSample QOSUserInteractive]
+ -[PLCoalitionSample QOSUtility]
+ -[PLCoalitionSample setQOSBackground:]
+ -[PLCoalitionSample setQOSUserInitiated:]
+ -[PLCoalitionSample setQOSUserInteractive:]
+ -[PLCoalitionSample setQOSUtility:]
+ -[PLDisplayAODStats oneHzBicAccumCount]
+ -[PLDisplayAODStats oneHzFlipbookFrameCount]
+ -[PLDisplayAODStats oneHzFrameMissCount]
+ -[PLDisplayAODStats setOneHzBicAccumCount:]
+ -[PLDisplayAODStats setOneHzFlipbookFrameCount:]
+ -[PLDisplayAODStats setOneHzFrameMissCount:]
+ -[PLEnergyIssuesService coalitionCallback]
+ -[PLEnergyIssuesService entryKeyPLCoalitionAgentEventIntervalCoalition]
+ -[PLEnergyIssuesService initializeSafeguardsSystem].cold.1
+ -[PLEnergyIssuesService safeguardsManagingClient]
+ -[PLEnergyIssuesService setCoalitionCallback:]
+ -[PLEnergyIssuesService setSafeguardsManagingClient:]
+ -[PLLocationAgent geoFenceTriggerListener]
+ -[PLLocationAgent logEventPointGeofenceTrigger:]
+ -[PLLocationAgent logEventPointGeofenceTrigger:].cold.1
+ -[PLLocationAgent logEventPointGeofenceTrigger:].cold.2
+ -[PLLocationAgent setGeoFenceTriggerListener:]
+ -[PLPowerMetricMonitorService _accountingMetrics]
+ -[PLPowerMetricMonitorService _accountingMetrics].cold.1
+ -[PLPowerMetricMonitorService _calculateAccumSystemLoad:]
+ -[PLPowerMetricMonitorService _calculateAccumSystemLoad:].cold.1
+ -[PLPowerMetricMonitorService _calculateAccumSystemLoad:].cold.2
+ -[PLPowerMetricMonitorService _calculateAndStoreSleepDuration]
+ -[PLPowerMetricMonitorService _calculateAndStoreSleepDuration].cold.1
+ -[PLPowerMetricMonitorService _calculateAndStoreSleepDuration].cold.2
+ -[PLPowerMetricMonitorService _calculateAndStoreSleepDuration].cold.3
+ -[PLPowerMetricMonitorService _calculateAndStoreSleepDuration].cold.4
+ -[PLPowerMetricMonitorService _getGPUTotalTime]
+ -[PLPowerMetricMonitorService _getGPUTotalTime].cold.1
+ -[PLPowerMetricMonitorService _handleDisplayLayoutUpdate:]
+ -[PLPowerMetricMonitorService _handlePowerNotification:argument:]
+ -[PLPowerMetricMonitorService _handlePowerNotification:argument:].cold.1
+ -[PLPowerMetricMonitorService _handlePowerNotification:argument:].cold.2
+ -[PLPowerMetricMonitorService _parseDisplayAZLMetricsFromEntry:]
+ -[PLPowerMetricMonitorService _parseProcessNetworkMetricsFromEntry:].cold.2
+ -[PLPowerMetricMonitorService _parseWifiPowerMetricsFromEntry:]
+ -[PLPowerMetricMonitorService _queryCumulativeNetworkBytes]
+ -[PLPowerMetricMonitorService _queryCumulativeNetworkBytes].cold.1
+ -[PLPowerMetricMonitorService _queryCumulativeNetworkBytes].cold.2
+ -[PLPowerMetricMonitorService _queryCumulativeNetworkBytes].cold.3
+ -[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:minRequestInterval:block:]
+ -[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:minRequestInterval:block:].cold.1
+ -[PLPowerMetricMonitorService _sampleGPUTime]
+ -[PLPowerMetricMonitorService _setUpIOReporting].cold.6
+ -[PLPowerMetricMonitorService _setUpSleepWakeMonitoring]
+ -[PLPowerMetricMonitorService _setUpSleepWakeMonitoring].cold.1
+ -[PLPowerMetricMonitorService _setupMetrics]
+ -[PLPowerMetricMonitorService _setupMetrics].cold.1
+ -[PLPowerMetricMonitorService _supportsGPUCoalitions]
+ -[PLPowerMetricMonitorService _supportsGPUCoalitions].cold.1
+ -[PLPowerMetricMonitorService _tearDownSleepWakeMonitoring]
+ -[PLPowerMetricMonitorService accountingEnabled]
+ -[PLPowerMetricMonitorService accumSystemLoadCount]
+ -[PLPowerMetricMonitorService accumSystemLoad]
+ -[PLPowerMetricMonitorService addMonitoredProcessWithPID:error:].cold.1
+ -[PLPowerMetricMonitorService batteryCapacity]
+ -[PLPowerMetricMonitorService batteryCapacity].cold.1
+ -[PLPowerMetricMonitorService brightnessPercent]
+ -[PLPowerMetricMonitorService brightnessPercentage]
+ -[PLPowerMetricMonitorService brightnessSum]
+ -[PLPowerMetricMonitorService cellularInBytes]
+ -[PLPowerMetricMonitorService cellularOutBytes]
+ -[PLPowerMetricMonitorService collectMetricsWithTimeout:]
+ -[PLPowerMetricMonitorService currentPowerState]
+ -[PLPowerMetricMonitorService dcpDisplayStats]
+ -[PLPowerMetricMonitorService disableAccounting]
+ -[PLPowerMetricMonitorService enableAccounting]
+ -[PLPowerMetricMonitorService getMachTimeFromSeconds:]
+ -[PLPowerMetricMonitorService getSecondsFromMachTime:]
+ -[PLPowerMetricMonitorService gpuTotalTime]
+ -[PLPowerMetricMonitorService invalidateScreenStateUpdates]
+ -[PLPowerMetricMonitorService isReadyToMonitor]
+ -[PLPowerMetricMonitorService lastSleepDuration]
+ -[PLPowerMetricMonitorService lastSleepTime]
+ -[PLPowerMetricMonitorService lastWakeTime]
+ -[PLPowerMetricMonitorService mainDisplayMonitor]
+ -[PLPowerMetricMonitorService metricNormalizer]
+ -[PLPowerMetricMonitorService metricNormalizer].cold.1
+ -[PLPowerMetricMonitorService networkCumulativeCount]
+ -[PLPowerMetricMonitorService pmNotifier]
+ -[PLPowerMetricMonitorService prevCumulativeCellularInBytes]
+ -[PLPowerMetricMonitorService prevCumulativeCellularOutBytes]
+ -[PLPowerMetricMonitorService prevCumulativeWiFiInBytes]
+ -[PLPowerMetricMonitorService prevCumulativeWiFiOutBytes]
+ -[PLPowerMetricMonitorService prevGpuTotalTime]
+ -[PLPowerMetricMonitorService queryLastSleepTimeMCT]
+ -[PLPowerMetricMonitorService queryLastWakeTimeMCT]
+ -[PLPowerMetricMonitorService receivedNetworkUpdate]
+ -[PLPowerMetricMonitorService rootDomainConnect]
+ -[PLPowerMetricMonitorService screenState]
+ -[PLPowerMetricMonitorService setAccountingEnabled:]
+ -[PLPowerMetricMonitorService setAccumSystemLoad:]
+ -[PLPowerMetricMonitorService setAccumSystemLoadCount:]
+ -[PLPowerMetricMonitorService setBrightnessPercentage:]
+ -[PLPowerMetricMonitorService setBrightnessSum:]
+ -[PLPowerMetricMonitorService setCellularInBytes:]
+ -[PLPowerMetricMonitorService setCellularOutBytes:]
+ -[PLPowerMetricMonitorService setCurrentPowerState:]
+ -[PLPowerMetricMonitorService setDcpDisplayStats:]
+ -[PLPowerMetricMonitorService setGpuTotalTime:]
+ -[PLPowerMetricMonitorService setIsReadyToMonitor:]
+ -[PLPowerMetricMonitorService setLastSleepDuration:]
+ -[PLPowerMetricMonitorService setLastSleepTime:]
+ -[PLPowerMetricMonitorService setLastWakeTime:]
+ -[PLPowerMetricMonitorService setMainDisplayMonitor:]
+ -[PLPowerMetricMonitorService setNetworkCumulativeCount:]
+ -[PLPowerMetricMonitorService setPmNotifier:]
+ -[PLPowerMetricMonitorService setPrevCumulativeCellularInBytes:]
+ -[PLPowerMetricMonitorService setPrevCumulativeCellularOutBytes:]
+ -[PLPowerMetricMonitorService setPrevCumulativeWiFiInBytes:]
+ -[PLPowerMetricMonitorService setPrevCumulativeWiFiOutBytes:]
+ -[PLPowerMetricMonitorService setPrevGpuTotalTime:]
+ -[PLPowerMetricMonitorService setReceivedNetworkUpdate:]
+ -[PLPowerMetricMonitorService setRootDomainConnect:]
+ -[PLPowerMetricMonitorService setScreenState:]
+ -[PLPowerMetricMonitorService setSystemPowerPortRef:]
+ -[PLPowerMetricMonitorService setTotalCell:]
+ -[PLPowerMetricMonitorService setTotalWiFi:]
+ -[PLPowerMetricMonitorService setUpScreenStateUpdates]
+ -[PLPowerMetricMonitorService setWifiInBytes:]
+ -[PLPowerMetricMonitorService setWifiOutBytes:]
+ -[PLPowerMetricMonitorService startMonitoring]
+ -[PLPowerMetricMonitorService systemPowerPortRef]
+ -[PLPowerMetricMonitorService totalCell]
+ -[PLPowerMetricMonitorService totalWiFi]
+ -[PLPowerMetricMonitorService wifiInBytes]
+ -[PLPowerMetricMonitorService wifiOutBytes]
+ -[PLPushAgent logAggregateSentKeepAlive:]
+ -[PLPushAgent logAggregateSentKeepAlive:].cold.1
+ -[PLSleepWakeAgent CoSocPowerTimer]
+ -[PLSleepWakeAgent iokitCoSocPower]
+ -[PLSleepWakeAgent setCoSocPowerTimer:]
+ -[PLSoCAgent triggerLTSStats]
+ -[PLWifiAgent lastEntryForMetricd]
+ -[PLWifiAgent logEventForwardModuleInfo].cold.3
+ -[PLWifiAgent logEventForwardModuleInfo].cold.4
+ -[PLWifiAgent setLastEntryForMetricd:]
+ -[PLXPCAgent convertPPSSKALogEventName:]
+ -[PLXPCAgent convertPPSSKALogEventName:].cold.1
+ -[PLXPCAgent convertPPSSKALogEventName:].cold.2
+ -[PLXPCAgent logEventIntervalPowerExceptionsDetection:]
+ -[PLXPCAgent logEventIntervalPowerExceptionsDetection:].cold.1
+ -[PLXPCAgent logStatusKitAgentAggregatePushes:]
+ -[PLXPCAgent logStatusKitAgentAggregatePushes:].cold.1
+ -[PLXPCAgent powerExceptionsDetectionXPCListener]
+ -[PLXPCAgent setPowerExceptionsDetectionXPCListener:]
+ -[PLXPCAgent setStatusKitAgentAggregatedPushesListener:]
+ -[PLXPCAgent statusKitAgentAggregatedPushesListener]
+ GCC_except_table114
+ GCC_except_table120
+ GCC_except_table124
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table138
+ GCC_except_table165
+ GCC_except_table171
+ GCC_except_table175
+ GCC_except_table18
+ GCC_except_table190
+ GCC_except_table240
+ GCC_except_table250
+ GCC_except_table253
+ GCC_except_table255
+ GCC_except_table260
+ GCC_except_table261
+ GCC_except_table266
+ GCC_except_table268
+ GCC_except_table272
+ GCC_except_table279
+ GCC_except_table28
+ GCC_except_table314
+ GCC_except_table316
+ GCC_except_table320
+ GCC_except_table425
+ GCC_except_table436
+ GCC_except_table472
+ GCC_except_table55
+ GCC_except_table60
+ GCC_except_table65
+ GCC_except_table81
+ _IODeregisterForSystemPower
+ _IONotificationPortDestroy
+ _KPLBatteryAgentStringSlowChargerReason
+ _OBJC_CLASS_$_FBSDisplayLayoutMonitorConfiguration
+ _OBJC_CLASS_$_OSASystemConfiguration
+ _OBJC_CLASS_$_PLBatteryUIDrainDateInterval
+ _OBJC_CLASS_$_PLBatteryUIInsightsAndSuggestionsSummary
+ _OBJC_CLASS_$_PLBatteryUIResponseTypeDrainComparisonSummary
+ _OBJC_CLASS_$_PLGestaltUtilities
+ _OBJC_CLASS_$_PLMetricdLifecycleManager
+ _OBJC_CLASS_$_PPSFileUtilities
+ _OBJC_CLASS_$_SafeguardsManagingClient
+ _OBJC_IVAR_$_PLBatteryUIDrainDateInterval._accumulatedDrainLevel
+ _OBJC_IVAR_$_PLBatteryUIDrainDateInterval._endDate
+ _OBJC_IVAR_$_PLBatteryUIDrainDateInterval._startDate
+ _OBJC_IVAR_$_PLBatteryUIInsightsAndSuggestionsSummary._insightSummaryResult
+ _OBJC_IVAR_$_PLBatteryUIInsightsAndSuggestionsSummary._responderService
+ _OBJC_IVAR_$_PLBatteryUIInsightsAndSuggestionsSummary._suggestionSummaryResult
+ _OBJC_IVAR_$_PLBatteryUIResponderService._shouldUseMidnightQueryRange
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeBatteryBreakdown._dynamicEndOffset
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeBatteryBreakdown._excludeTimeOnCharger
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeBatteryBreakdown._isDynamicEnd
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeBatteryBreakdown._percentageOption
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeBatteryBreakdown._uiLevelDrainEntries
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeChargingStateIntervals._bucketSize
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeChargingStateIntervals._dailyChargingStateIntervalsDict
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeChargingStateIntervals._dailyLastBattEntry
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeChargingStateIntervals._resultArray
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeChargingStateIntervals._shouldSnapInterval
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._averageDrainRate
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._buckets
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._bundleIDToDisplayNameMap
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._comparisonType
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._installedPluginToParentIDMap
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._nodeIDToNodeNameMap
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._responderService
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._resultArray
+ _OBJC_IVAR_$_PLBatteryUIResponseTypeDrainComparisonSummary._suggest
+ _OBJC_IVAR_$_PLCoalitionSample._QOSBackground
+ _OBJC_IVAR_$_PLCoalitionSample._QOSUserInitiated
+ _OBJC_IVAR_$_PLCoalitionSample._QOSUserInteractive
+ _OBJC_IVAR_$_PLCoalitionSample._QOSUtility
+ _OBJC_IVAR_$_PLDisplayAODStats._oneHzBicAccumCount
+ _OBJC_IVAR_$_PLDisplayAODStats._oneHzFlipbookFrameCount
+ _OBJC_IVAR_$_PLDisplayAODStats._oneHzFrameMissCount
+ _OBJC_IVAR_$_PLEnergyIssuesService._coalitionCallback
+ _OBJC_IVAR_$_PLEnergyIssuesService._entryKeyPLCoalitionAgentEventIntervalCoalition
+ _OBJC_IVAR_$_PLEnergyIssuesService._safeguardsManagingClient
+ _OBJC_IVAR_$_PLLocationAgent._geoFenceTriggerListener
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._accountingEnabled
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._accumSystemLoad
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._accumSystemLoadCount
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._brightnessPercentage
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._brightnessSum
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._cellularInBytes
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._cellularOutBytes
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._currentPowerState
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._dcpDisplayStats
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._gpuTotalTime
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._isReadyToMonitor
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._lastSleepDuration
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._lastSleepTime
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._lastWakeTime
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._mainDisplayMonitor
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._networkCumulativeCount
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._pmNotifier
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._prevCumulativeCellularInBytes
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._prevCumulativeCellularOutBytes
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._prevCumulativeWiFiInBytes
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._prevCumulativeWiFiOutBytes
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._prevGpuTotalTime
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._receivedNetworkUpdate
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._rootDomainConnect
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._screenState
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._systemPowerPortRef
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._totalCell
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._totalWiFi
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._wifiInBytes
+ _OBJC_IVAR_$_PLPowerMetricMonitorService._wifiOutBytes
+ _OBJC_IVAR_$_PLSleepWakeAgent._CoSocPowerTimer
+ _OBJC_IVAR_$_PLSleepWakeAgent._iokitCoSocPower
+ _OBJC_IVAR_$_PLWifiAgent._lastEntryForMetricd
+ _OBJC_IVAR_$_PLXPCAgent._powerExceptionsDetectionXPCListener
+ _OBJC_IVAR_$_PLXPCAgent._statusKitAgentAggregatedPushesListener
+ _OBJC_METACLASS_$_PLBatteryUIDrainDateInterval
+ _OBJC_METACLASS_$_PLBatteryUIInsightsAndSuggestionsSummary
+ _OBJC_METACLASS_$_PLBatteryUIResponseTypeDrainComparisonSummary
+ _OBJC_METACLASS_$_PPSFileUtilities
+ _PLBatteryUIDrainComparisonTypes
+ _PLLogProcessNetwork
+ _PLLogProcessNetwork.__logObj
+ _PLLogProcessNetwork.cold.1
+ _PLLogProcessNetwork.onceToken
+ _PLProcessMetricsAdd
+ _PLProcessMetricsForIdleBand
+ _PLProcessMetricsInitWithRusage
+ _PLProcessMetricsRead
+ _PLProcessPrioritiesDelete
+ _PLProcessPrioritiesInit
+ _PLProcessPrioritiesMetricsForPriority
+ _PLProcessPrioritiesRead
+ _PowerChangedCallback.classDebugEnabled.436
+ _PowerChangedCallback.classDebugEnabled.442
+ _PowerChangedCallback.classDebugEnabled.452
+ _PowerChangedCallback.classDebugEnabled.458
+ _PowerChangedCallback.defaultOnce.435
+ _PowerChangedCallback.defaultOnce.441
+ _PowerChangedCallback.defaultOnce.451
+ _PowerChangedCallback.defaultOnce.457
+ __OBJC_$_CLASS_METHODS_PPSFileUtilities(APFS)
+ __OBJC_$_INSTANCE_METHODS_PLBatteryUIDrainDateInterval
+ __OBJC_$_INSTANCE_METHODS_PLBatteryUIInsightsAndSuggestionsSummary
+ __OBJC_$_INSTANCE_METHODS_PLBatteryUIResponseTypeDrainComparisonSummary
+ __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIDrainDateInterval
+ __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIInsightsAndSuggestionsSummary
+ __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIResponseTypeDrainComparisonSummary
+ __OBJC_$_PROP_LIST_PLBatteryUIDrainDateInterval
+ __OBJC_$_PROP_LIST_PLBatteryUIInsightsAndSuggestionsSummary
+ __OBJC_$_PROP_LIST_PLBatteryUIResponseTypeDrainComparisonSummary
+ __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIInsightsAndSuggestionsSummary
+ __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIResponseTypeDrainComparisonSummary
+ __OBJC_CLASS_RO_$_PLBatteryUIDrainDateInterval
+ __OBJC_CLASS_RO_$_PLBatteryUIInsightsAndSuggestionsSummary
+ __OBJC_CLASS_RO_$_PLBatteryUIResponseTypeDrainComparisonSummary
+ __OBJC_CLASS_RO_$_PPSFileUtilities
+ __OBJC_METACLASS_RO_$_PLBatteryUIDrainDateInterval
+ __OBJC_METACLASS_RO_$_PLBatteryUIInsightsAndSuggestionsSummary
+ __OBJC_METACLASS_RO_$_PLBatteryUIResponseTypeDrainComparisonSummary
+ __OBJC_METACLASS_RO_$_PPSFileUtilities
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN12PLProcessCPU12inode_data_tEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEED1B8ne200100Ev
+ __ZNSt3__112__destroy_atB8ne200100INS_4pairIKyN12PLProcessCPU12inode_data_tEEELi0EEEvPT_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__113__tree_removeB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ ___101-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.862
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.793
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.805
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.809
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.809.cold.1
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.809.cold.2
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.831
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.838
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.845
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.845.cold.1
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.852
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.856
+ ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke_2.846
+ ___109-[PLBatteryUIResponderService prepareBreakdown:withDrainSummaries:withFullDayBreakdown:withDynamicBreakdown:]_block_invoke
+ ___109-[PLBatteryUIResponderService prepareBreakdown:withDrainSummaries:withFullDayBreakdown:withDynamicBreakdown:]_block_invoke_2
+ ___120-[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:minRequestInterval:block:]_block_invoke
+ ___120-[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:minRequestInterval:block:]_block_invoke_2
+ ___120-[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:minRequestInterval:block:]_block_invoke_2.cold.1
+ ___136-[PLBatteryUIResponseTypeChargingStateIntervals organizeStateIntervalsWithRange:lastBattUIEntry:chargingIntervalsDict:addToDailyArrays:]_block_invoke
+ ___20-[PLXPCService init]_block_invoke.537
+ ___20-[PLXPCService init]_block_invoke.537.cold.1
+ ___20-[PLXPCService init]_block_invoke.558
+ ___20-[PLXPCService init]_block_invoke.565
+ ___20-[PLXPCService init]_block_invoke.573
+ ___20-[PLXPCService init]_block_invoke.577
+ ___20-[PLXPCService init]_block_invoke.577.cold.1
+ ___20-[PLXPCService init]_block_invoke.577.cold.2
+ ___20-[PLXPCService init]_block_invoke.584
+ ___20-[PLXPCService init]_block_invoke.588
+ ___20-[PLXPCService init]_block_invoke.588.cold.1
+ ___20-[PLXPCService init]_block_invoke.599
+ ___20-[PLXPCService init]_block_invoke_2.578
+ ___20-[PLXPCService init]_block_invoke_2.589
+ ___22-[PLBatteryAgent init]_block_invoke.3251
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.1
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.10
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.11
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.2
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.3
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.4
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.5
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.6
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.7
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.8
+ ___22-[PLBatteryAgent init]_block_invoke.3251.cold.9
+ ___22-[PLBatteryAgent init]_block_invoke.3263
+ ___22-[PLBatteryAgent init]_block_invoke.3265
+ ___22-[PLBatteryAgent init]_block_invoke.3291
+ ___22-[PLBatteryAgent init]_block_invoke.3294
+ ___22-[PLBatteryAgent init]_block_invoke.3302
+ ___22-[PLBatteryAgent init]_block_invoke.3302.cold.1
+ ___22-[PLBatteryAgent init]_block_invoke.3302.cold.2
+ ___22-[PLBatteryAgent init]_block_invoke.3308
+ ___22-[PLBatteryAgent init]_block_invoke.3312
+ ___22-[PLBatteryAgent init]_block_invoke_2.3334
+ ___22-[PLDisplayAgent init]_block_invoke.1431
+ ___22-[PLDisplayAgent init]_block_invoke.1431.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke.1431.cold.2
+ ___22-[PLDisplayAgent init]_block_invoke.1431.cold.3
+ ___22-[PLDisplayAgent init]_block_invoke.1431.cold.4
+ ___22-[PLDisplayAgent init]_block_invoke.1442
+ ___22-[PLDisplayAgent init]_block_invoke.1446
+ ___22-[PLDisplayAgent init]_block_invoke.1450
+ ___22-[PLDisplayAgent init]_block_invoke.1456
+ ___22-[PLDisplayAgent init]_block_invoke.1456.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke.1456.cold.2
+ ___22-[PLDisplayAgent init]_block_invoke.1474
+ ___22-[PLDisplayAgent init]_block_invoke.1482
+ ___22-[PLDisplayAgent init]_block_invoke_2.1433
+ ___22-[PLDisplayAgent init]_block_invoke_2.1452
+ ___22-[PLDisplayAgent init]_block_invoke_2.1452.cold.1
+ ___22-[PLDisplayAgent init]_block_invoke_2.1452.cold.2
+ ___22-[PLDisplayAgent init]_block_invoke_2.1468
+ ___22-[PLDisplayAgent init]_block_invoke_2.1485
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5025
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5034
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5043
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5052
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5058
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5064
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5070
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5079
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5085
+ ___24-[PLBatteryAgent xFlags]_block_invoke.5091
+ ___29+[PLUtilities deviceBootUUID]_block_invoke.118
+ ___29+[PLUtilities hasInternalKey]_block_invoke
+ ___29-[PLSoCAgent triggerLTSStats]_block_invoke
+ ___29-[PLSoCAgent triggerLTSStats]_block_invoke.cold.1
+ ___29-[PLSoCAgent triggerLTSStats]_block_invoke.cold.2
+ ___30+[PLUtilities experimentGroup]_block_invoke
+ ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2459
+ ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4712
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3432
+ ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3438
+ ___33+[PLPushAgent bundleIdFromTopic:]_block_invoke.343
+ ___33+[PLUtilities isPerfPowerMetricd]_block_invoke
+ ___33+[PLUtilities isPowerexceptionsd]_block_invoke
+ ___33+[PPSFileUtilities containerPath]_block_invoke
+ ___33+[PPSFileUtilities containerPath]_block_invoke.cold.1
+ ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3423
+ ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5104
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.935
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.951
+ ___33-[PLWifiAgent logEventPointWake:]_block_invoke.963
+ ___34+[PLSMCAgent reportPMUEventsToCA:]_block_invoke.920
+ ___36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.2393
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.689
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.695
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.701
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.707
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.716
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.726
+ ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.730
+ ___37+[PLUtilities exitWithReason:action:]_block_invoke.179
+ ___37-[PLXPCAgent logEventForwardGMSOptIn]_block_invoke.3012
+ ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3781
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1889
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1889.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1897
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1897.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1905
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1905.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1913
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1913.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1921
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1921.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1929
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1929.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1937
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1937.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1945
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1945.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1966
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1966.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1977
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1977.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1988
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1988.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1999
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1999.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2010
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2010.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2015
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2029
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2029.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2037
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2037.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2042
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2042.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2049
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2049.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2056
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2064
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2064.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2074
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2074.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2079
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2079.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2086
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2086.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2091
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2091.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2101
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2101.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2109
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2109.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2117
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2117.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2122
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2122.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2130
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2130.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2138
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2138.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2177
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2177.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2182
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2182.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2190
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2190.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2200
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2200.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2208
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2208.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2216
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2216.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2224
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2224.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2232
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2232.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2239
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2239.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2244
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2244.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2265
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2265.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2270
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2270.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2295
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2295.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2305
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2305.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2313
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2313.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2331
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2331.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2346
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2346.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2356
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2356.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2366
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2366.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2374
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2374.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2384
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2384.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2393
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2393.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2402
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2402.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2412
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2412.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2420
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2420.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2438
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2438.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2454
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2454.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2492
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2492.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2502
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2502.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2510
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2510.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2520
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2520.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2528
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2528.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2541
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2541.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2551
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2551.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2556
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2556.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2563
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2563.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2568
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2568.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2573
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2573.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2578
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2578.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2583
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2583.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2597
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2597.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2604
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2604.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2614
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2614.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2630
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2630.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2638
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2638.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2646
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2646.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2651
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2651.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2661
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2661.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2671
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2671.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2679
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2679.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2687
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2687.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2702
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2702.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2710
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2710.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2720
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2720.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2730
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2730.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2740
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2740.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2747
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2747.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2757
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2757.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2765
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2765.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2773
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2773.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2781
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2781.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2788
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2788.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2793
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2793.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2800
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2800.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2805
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2805.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2813
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2813.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2818
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2818.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2835
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2835.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2843
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2843.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2855
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2855.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2856
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2864
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2864.cold.1
+ ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.cold.1
+ ___39-[PLProcessMonitorAgent logProcessExit]_block_invoke.553
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.193
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.193.cold.1
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.202
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.202.cold.1
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.210
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.210.cold.1
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.218
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.218.cold.1
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.226
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.226.cold.1
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.234.cold.1
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.236
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.255
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.255.cold.1
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.263
+ ___39-[PLPushAgent initOperatorDependancies]_block_invoke.263.cold.1
+ ___39-[PLXPCService logMessage:withPayload:]_block_invoke.655
+ ___40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1612
+ ___40-[PLWifiAgent logEventForwardAWDLState:]_block_invoke.1149
+ ___40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1117
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4112
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4119
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4115
+ ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4122
+ ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.721
+ ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.727
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3510
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3516
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3516.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3532
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3565
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625.cold.2
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3625.cold.3
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3642
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3642.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3653
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3657
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3657.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3665
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3665.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3681
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3687
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3694
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3694.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3701
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3701.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3715
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3715.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3720
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3720.cold.1
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3727
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3750
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3517
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3562
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3577
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3649
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3666
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3676
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3695
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3702
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3758
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3762
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3766
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3770
+ ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3772
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5255
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5255.cold.1
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5255.cold.2
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5263
+ ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5257
+ ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.3977
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1503
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1519
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1532
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1532.cold.1
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1532.cold.2
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1539
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1545
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1522
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1533
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1550
+ ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1550.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1762
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1762.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1767
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1767.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1774
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1774.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1779
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1779.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1789
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1789.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1799
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1799.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1804
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1804.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1811
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1811.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1816
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1816.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1833
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1833.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1865
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1865.cold.1
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1872
+ ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1872.cold.1
+ ___42-[PLXPCService resetPermissionsForClients]_block_invoke.670
+ ___42-[PLXPCService resetPermissionsForClients]_block_invoke.680
+ ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.2019
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.518
+ ___43-[PLLocationAgent initOperatorDependancies]_block_invoke.518.cold.1
+ ___43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.711
+ ___43-[PLWifiAgent logEventForwardHotspotState:]_block_invoke.1158
+ ___44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.446
+ ___44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.473
+ ___44-[PLPowerMetricMonitorService _setupMetrics]_block_invoke
+ ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.634
+ ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.640
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5291
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5292
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5293
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5294
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5295
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5295.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5296
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5296.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5297
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5297.cold.1
+ ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5338
+ ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.2067
+ ___46+[PPSFileUtilities(APFS) supportsEnhancedAPFS]_block_invoke
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.397
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.397.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.402
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.418
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.447
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.447.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.453
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.453.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.458
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.458.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.465
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.465.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.475
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.475.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.482
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.482.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.489
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.489.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.494
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.494.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.499
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.499.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.507
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.507.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.515
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.515.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.520
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.520.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.525
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.525.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.526
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.540
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.540.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.548
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.548.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.404
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.421
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.527
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.527.cold.1
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.527.cold.2
+ ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_3.414
+ ___46-[PLPowerMetricMonitorService batteryCapacity]_block_invoke
+ ___46-[PLPowerMetricMonitorService startMonitoring]_block_invoke
+ ___46-[PLPowerMetricMonitorService startMonitoring]_block_invoke.cold.1
+ ___46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.285
+ ___46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.285.cold.1
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1203
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1209
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1217
+ ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1223
+ ___47-[PLBatteryUIResponderService linkDependencies]_block_invoke.67
+ ___47-[PLPowerMetricMonitorService metricNormalizer]_block_invoke
+ ___49-[PLBatteryUINotificationService ursaTTRContent:]_block_invoke
+ ___49-[PLBatteryUINotificationService ursaTTRContent:]_block_invoke.cold.1
+ ___49-[PLCoalitionAgent logCoalitionObjectDifference:]_block_invoke.782
+ ___49-[PLPowerMetricMonitorService _accountingMetrics]_block_invoke
+ ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.428
+ ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.428.cold.1
+ ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.442
+ ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.442.cold.1
+ ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.454
+ ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.454.cold.1
+ ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.469
+ ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.469.cold.1
+ ___49-[PLProcessMonitorAgent updateProcessExitSummary]_block_invoke.477
+ ___49-[PLProcessMonitorAgent updateProcessExitSummary]_block_invoke.477.cold.1
+ ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.214
+ ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.244
+ ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.244.cold.1
+ ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.253
+ ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.253.cold.1
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5280
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5281
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5285
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5285.cold.1
+ ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5285.cold.2
+ ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.2076
+ ___50-[PLProcessMonitorAgent disableProcessExitLogging]_block_invoke.489
+ ___50-[PLProcessMonitorAgent ledgerDataAtIndex:forPid:]_block_invoke.513
+ ___50-[PLProcessMonitorAgent ledgerDataAtIndex:forPid:]_block_invoke.519
+ ___51-[PLPowerMetricMonitorService queryLastWakeTimeMCT]_block_invoke
+ ___52-[PLPowerMetricMonitorService queryLastSleepTimeMCT]_block_invoke
+ ___52-[PLProcessMonitorAgent logEventPointMemoryTracking]_block_invoke.529
+ ___52-[PLProcessMonitorAgent logEventPointMemoryTracking]_block_invoke.535
+ ___52-[PLProcessMonitorAgent logEventPointMemoryTracking]_block_invoke.541
+ ___53-[PLBatteryUINotificationService surfaceNotification]_block_invoke.82
+ ___53-[PLBatteryUINotificationService ursaBootargContent:]_block_invoke
+ ___53-[PLPowerMetricMonitorService _supportsGPUCoalitions]_block_invoke
+ ___53-[PLProcessMonitorAgent logEventPointFreezerDemotion]_block_invoke.642
+ ___54+[PLBatteryUIResponseTypeUtilities getNonAppBundleIDs]_block_invoke
+ ___54-[PLBatteryAgent showOrHideTLCNotification:timeInTLC:]_block_invoke.3375
+ ___54-[PLPowerMetricMonitorService setUpScreenStateUpdates]_block_invoke
+ ___54-[PLPowerMetricMonitorService setUpScreenStateUpdates]_block_invoke_2
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.746
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.752
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.758
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.764
+ ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.770
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4968
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4968.cold.1
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4972
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4972.cold.1
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4977
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.4981
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4973
+ ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.4978
+ ___55-[PLCoalitionAgent processPerAppLogicalWritesWithInfo:]_block_invoke.811
+ ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1069
+ ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1078
+ ___56-[PLApplicationAgent createWidgetStatsAccountingEvents:]_block_invoke.578
+ ___56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.1105
+ ___57-[PLBatteryUIResponseTypeBatteryBreakdown addQualifiers:]_block_invoke.381
+ ___57-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke
+ ___57-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke.258
+ ___57-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke.258.cold.1
+ ___57-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke.cold.1
+ ___57-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke.cold.2
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35.cold.1
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35.cold.2
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35.cold.3
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35.cold.4
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35.cold.5
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35.cold.6
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35.cold.7
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35.cold.8
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.35.cold.9
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.43
+ ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.66
+ ___58-[PLProcessMonitorAgent logEventIntervalKernelTaskMonitor]_block_invoke.707
+ ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3403
+ ___59-[PLPowerMetricMonitorService invalidateScreenStateUpdates]_block_invoke
+ ___61-[PLBatteryBreakdownService mapDeletedAppsWithEnergyEntries:]_block_invoke.1816
+ ___61-[PLBatteryUINotificationService initializeUrsaNotifications]_block_invoke
+ ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.222
+ ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.266
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1060
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.991
+ ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.997
+ ___63-[PLBatteryBreakdownService mapPluginsToAppsWithEnergyEntries:]_block_invoke.1825
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1735
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1753
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1753.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1764
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1764.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1765
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1765.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1766
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1766.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1768
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1768.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1769
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1769.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1769.cold.2
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1776
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1776.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1780
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1780.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1785
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1789
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1789.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1814
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1815
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1815.cold.1
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1748
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1760
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1781
+ ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1808
+ ___64+[PLEnergyIssuesService shouldPopUpForPowerExceptionForProcess:]_block_invoke
+ ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1889
+ ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1893
+ ___64-[PLBatteryUINotificationService handleUrsaNotificationRequest:]_block_invoke
+ ___64-[PLBatteryUINotificationService handleUrsaNotificationRequest:]_block_invoke.cold.1
+ ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4375
+ ___65-[PLBatteryUIResponseTypeBatteryBreakdown collapseEnergyEntries:]_block_invoke.576
+ ___65-[PLBatteryUIResponseTypeBatteryBreakdown createPerAppBreakdown:]_block_invoke
+ ___65-[PLBatteryUIResponseTypeBatteryBreakdown createPerAppBreakdown:]_block_invoke_2
+ ___66-[PLBatteryUIResponseTypeBatteryBreakdown reaccountBackupRestore:]_block_invoke.608
+ ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1910
+ ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1916
+ ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1922
+ ___68-[PLBatteryBreakdownService determineDisplayNamesWithEnergyEntries:]_block_invoke.1904
+ ___69-[PLBatteryBreakdownService reaccountBackupRestoreWithEnergyEntries:]_block_invoke.1878
+ ___71-[PLBatteryUIResponseTypeBatteryBreakdown transformPlugins:withBucket:]_block_invoke.622
+ ___73-[PLBatteryBreakdownService populateRootNodeEnergyKeysWithEnergyEntries:]_block_invoke.1609
+ ___73-[PLBatteryBreakdownService populateRootNodeEnergyKeysWithEnergyEntries:]_block_invoke.1615
+ ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.137
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1742
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1754
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1762
+ ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1768
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83.cold.1
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83.cold.2
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.83.cold.3
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.87
+ ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.87.cold.1
+ ___75-[PLBatteryBreakdownService addNotificationValues:withRange:withQueryType:]_block_invoke.1732
+ ___76-[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap]_block_invoke
+ ___76-[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap]_block_invoke.177
+ ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1783
+ ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1789
+ ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1797
+ ___81-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:shouldMaskTimestamp:]_block_invoke.618
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1945
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1962
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1970
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2020
+ ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2030
+ ___81-[PLProcessMonitorAgent logEventBackwardProcessExitHistogram:withStats:withDate:]_block_invoke.682
+ ___84-[PLBatteryUIResponseTypeDrainComparisonSummary sortedAppEnergyArrayFromAppDataMap:]_block_invoke
+ ___84-[PLBatteryUIResponseTypeDrainComparisonSummary sortedAppEnergyArrayFromAppDataMap:]_block_invoke_2
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2276
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2288
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2297
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2303
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2309
+ ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2315
+ ___87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.509
+ ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1534
+ ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1540
+ ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1546
+ ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1552
+ ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1558
+ ___90-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]_block_invoke.784
+ ___99-[PLProcessMonitorAgent logEventPointProcessExit:excludeProcesses:withStats:withDate:withNowInSec:]_block_invoke.593
+ ___99-[PLProcessMonitorAgent logEventPointProcessExit:excludeProcesses:withStats:withDate:withNowInSec:]_block_invoke_2.615
+ ___PLLogProcessNetwork_block_invoke
+ ___PowerChangedCallback_block_invoke.437
+ ___PowerChangedCallback_block_invoke.443
+ ___PowerChangedCallback_block_invoke.447
+ ___PowerChangedCallback_block_invoke.447.cold.1
+ ___PowerChangedCallback_block_invoke.453
+ ___PowerChangedCallback_block_invoke.459
+ ___block_descriptor_40_e8_32s_e92_v32?0"FBSDisplayLayoutMonitor"8"FBSDisplayLayout"16"FBSDisplayLayoutTransitionContext"24ls32l8
+ ___block_descriptor_48_e8_32s40s_e36_v32?0"NSMutableDictionary"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24ls32l8w40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8s48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e35_v32?0"NSString"8"NSString"16^B24lr56l8s32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48w_e5_v8?0lw48l8s32l8s40l8
+ ___block_descriptor_76_e8_32s40s48s_e25_v32?0"NSNumber"816^B24ls32l8s40l8s48l8
+ ___block_literal_global.105
+ ___block_literal_global.108
+ ___block_literal_global.123
+ ___block_literal_global.142
+ ___block_literal_global.17
+ ___block_literal_global.1747
+ ___block_literal_global.181
+ ___block_literal_global.1844
+ ___block_literal_global.1848
+ ___block_literal_global.1850
+ ___block_literal_global.1854
+ ___block_literal_global.1856
+ ___block_literal_global.1858
+ ___block_literal_global.1864
+ ___block_literal_global.1914
+ ___block_literal_global.1916
+ ___block_literal_global.1957
+ ___block_literal_global.199
+ ___block_literal_global.2100
+ ___block_literal_global.217
+ ___block_literal_global.220
+ ___block_literal_global.2315
+ ___block_literal_global.235
+ ___block_literal_global.253
+ ___block_literal_global.266
+ ___block_literal_global.268
+ ___block_literal_global.2845
+ ___block_literal_global.286
+ ___block_literal_global.287
+ ___block_literal_global.289
+ ___block_literal_global.295
+ ___block_literal_global.303
+ ___block_literal_global.307
+ ___block_literal_global.308
+ ___block_literal_global.316
+ ___block_literal_global.3238
+ ___block_literal_global.325
+ ___block_literal_global.329
+ ___block_literal_global.3349
+ ___block_literal_global.3362
+ ___block_literal_global.3377
+ ___block_literal_global.339
+ ___block_literal_global.3478
+ ___block_literal_global.348
+ ___block_literal_global.3535
+ ___block_literal_global.3579
+ ___block_literal_global.3588
+ ___block_literal_global.3597
+ ___block_literal_global.3609
+ ___block_literal_global.369
+ ___block_literal_global.3722
+ ___block_literal_global.373
+ ___block_literal_global.3774
+ ___block_literal_global.3780
+ ___block_literal_global.3790
+ ___block_literal_global.381
+ ___block_literal_global.405
+ ___block_literal_global.411
+ ___block_literal_global.413
+ ___block_literal_global.418
+ ___block_literal_global.423
+ ___block_literal_global.433
+ ___block_literal_global.435
+ ___block_literal_global.439
+ ___block_literal_global.4424
+ ___block_literal_global.445
+ ___block_literal_global.448
+ ___block_literal_global.453
+ ___block_literal_global.458
+ ___block_literal_global.46
+ ___block_literal_global.4668
+ ___block_literal_global.467
+ ___block_literal_global.4680
+ ___block_literal_global.4730
+ ___block_literal_global.475
+ ___block_literal_global.484
+ ___block_literal_global.5229
+ ___block_literal_global.525
+ ___block_literal_global.5290
+ ___block_literal_global.532
+ ___block_literal_global.535
+ ___block_literal_global.538
+ ___block_literal_global.543
+ ___block_literal_global.558
+ ___block_literal_global.647
+ ___block_literal_global.68
+ ___block_literal_global.712
+ ___block_literal_global.714
+ ___block_literal_global.716
+ ___block_literal_global.717
+ ___block_literal_global.724
+ ___block_literal_global.727
+ ___block_literal_global.730
+ ___block_literal_global.741
+ ___block_literal_global.788
+ ___block_literal_global.790
+ ___block_literal_global.84
+ ___block_literal_global.852
+ ___block_literal_global.854
+ ___block_literal_global.855
+ ___block_literal_global.856
+ ___block_literal_global.858
+ ___block_literal_global.86
+ ___block_literal_global.860
+ ___block_literal_global.862
+ ___block_literal_global.883
+ ___block_literal_global.885
+ ___block_literal_global.887
+ ___block_literal_global.889
+ ___block_literal_global.89
+ ___block_literal_global.891
+ ___block_literal_global.894
+ ___block_literal_global.896
+ ___block_literal_global.916
+ ___block_literal_global.927
+ ___block_literal_global.94
+ ___block_literal_global.99
+ ___fakeSleep_block_invoke.394
+ ___fakeSleep_block_invoke.406
+ ___fakeSleep_block_invoke.410
+ ___fakeSleep_block_invoke.410.cold.1
+ ___fakeSleep_block_invoke.416
+ ___updateDisplayIOReportAODStats_block_invoke.cold.12
+ ___updateDisplayIOReportAODStats_block_invoke.cold.13
+ ___updateDisplayIOReportAODStats_block_invoke.cold.14
+ __idlePhysFootprintBytes
+ __idleWiredBytes
+ __supportsGPUCoalitions.gpu_coliations_supported
+ __supportsGPUCoalitions.onceToken
+ _addQualifiers:.classDebugEnabled.380
+ _addQualifiers:.defaultOnce.379
+ _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1782
+ _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1788
+ _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1796
+ _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1781
+ _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1787
+ _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1795
+ _batteryCapacity.batteryCapacity
+ _batteryCapacity.onceToken
+ _cancelEALogging.classDebugEnabled.3422
+ _cancelEALogging.defaultOnce.3421
+ _combineDuplicatesWithEnergyEntries:.classDebugEnabled.1888
+ _combineDuplicatesWithEnergyEntries:.classDebugEnabled.1895
+ _combineDuplicatesWithEnergyEntries:.defaultOnce.1887
+ _combineDuplicatesWithEnergyEntries:.defaultOnce.1894
+ _dailyTasks.defaultOnce.613
+ _determineDisplayNamesWithEnergyEntries:.classDebugEnabled.1903
+ _determineDisplayNamesWithEnergyEntries:.defaultOnce.1902
+ _deviceBootUUID.classDebugEnabled.117
+ _deviceBootUUID.defaultOnce.116
+ _disableProcessExitLogging.classDebugEnabled.488
+ _disableProcessExitLogging.defaultOnce.487
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1533
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1539
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1545
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1551
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1557
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1532
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1538
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1544
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1550
+ _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1556
+ _experimentGroup.expGroup
+ _experimentGroup.onceToken
+ _fakeSleep.classDebugEnabled.393
+ _fakeSleep.classDebugEnabled.405
+ _fakeSleep.classDebugEnabled.415
+ _fakeSleep.defaultOnce.392
+ _fakeSleep.defaultOnce.404
+ _fakeSleep.defaultOnce.414
+ _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1741
+ _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1753
+ _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1761
+ _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1767
+ _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1740
+ _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1752
+ _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1760
+ _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1766
+ _filterWithEnergyEntries:withQueryType:.classDebugEnabled.1909
+ _filterWithEnergyEntries:withQueryType:.classDebugEnabled.1915
+ _filterWithEnergyEntries:withQueryType:.classDebugEnabled.1921
+ _filterWithEnergyEntries:withQueryType:.defaultOnce.1908
+ _filterWithEnergyEntries:withQueryType:.defaultOnce.1914
+ _filterWithEnergyEntries:withQueryType:.defaultOnce.1920
+ _freeifaddrs
+ _getBundleIDToDisplayNameMap.classDebugEnabled.176
+ _getBundleIDToDisplayNameMap.defaultOnce.175
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.136
+ _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.135
+ _getIOPSDevices.classDebugEnabled.3431
+ _getIOPSDevices.classDebugEnabled.3437
+ _getIOPSDevices.defaultOnce.3430
+ _getIOPSDevices.defaultOnce.3436
+ _getNonAppBundleIDs.nonAppBundleIDs
+ _getNonAppBundleIDs.onceToken
+ _getifaddrs
+ _handleBrightnessClientNotification:withValue:.classDebugEnabled.1813
+ _handleBrightnessClientNotification:withValue:.defaultOnce.1812
+ _handlePeer:forEvent:.classDebugEnabled.688
+ _handlePeer:forEvent:.classDebugEnabled.694
+ _handlePeer:forEvent:.classDebugEnabled.700
+ _handlePeer:forEvent:.classDebugEnabled.706
+ _handlePeer:forEvent:.classDebugEnabled.715
+ _handlePeer:forEvent:.classDebugEnabled.725
+ _handlePeer:forEvent:.defaultOnce.687
+ _handlePeer:forEvent:.defaultOnce.693
+ _handlePeer:forEvent:.defaultOnce.699
+ _handlePeer:forEvent:.defaultOnce.705
+ _handlePeer:forEvent:.defaultOnce.714
+ _handlePeer:forEvent:.defaultOnce.724
+ _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.861
+ _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.860
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.792
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.804
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.851
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.791
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.803
+ _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.850
+ _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:.classDebugEnabled.783
+ _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:.defaultOnce.782
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.745
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.751
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.757
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.763
+ _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.769
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.744
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.750
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.756
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.762
+ _handleSingleMessage:fromPeer:forEvent:.defaultOnce.768
+ _hasInternalKey._hasInternalAccount
+ _hasInternalKey.onceToken
+ _init.classDebugEnabled.1441
+ _init.classDebugEnabled.564
+ _init.classDebugEnabled.572
+ _init.defaultOnce.1440
+ _init.defaultOnce.563
+ _init.defaultOnce.571
+ _initOperatorDependancies.classDebugEnabled.3675
+ _initOperatorDependancies.classDebugEnabled.3683
+ _initOperatorDependancies.classDebugEnabled.3686
+ _initOperatorDependancies.defaultOnce.3674
+ _initOperatorDependancies.defaultOnce.3682
+ _initOperatorDependancies.defaultOnce.3685
+ _isPerfPowerMetricd.isPerfPowerMetricd
+ _isPerfPowerMetricd.onceToken
+ _isPowerexceptionsd.isPowerexceptionsd
+ _isPowerexceptionsd.onceToken
+ _kPLApplicationAgentEventForwardNameRBSApplication
+ _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3293
+ _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3307
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3253
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3289
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3292
+ _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3306
+ _kPLBatteryAgentStringUserType_block_invoke.objectForKey.3290
+ _kPLBatteryAgentStringUserType_block_invoke_12.classDebugEnabled.5262
+ _kPLBatteryAgentStringUserType_block_invoke_12.defaultOnce.5261
+ _kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3509
+ _kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3508
+ _kPLPushAgentAggregateNameSentKeepAlive
+ _kPLSleepWakeAgentEventPointNameCoSocPower
+ _kPLSleepWakeAgentEventPointNameCoSocPowerActiveClients
+ _kPLSleepWakeAgentEventPointNameCoSocPowerState
+ _kPLSleepWakeAgentEventPointNameCoSocPowerTriggerType
+ _kPLSleepWakeAgentEventPointNameCoSocPowerTriggerType_block_invoke.classDebugEnabled
+ _kPLSleepWakeAgentEventPointNameCoSocPowerTriggerType_block_invoke.defaultOnce
+ _kPLSleepWakeAgentEventPointNameCoSocPowerTriggerType_block_invoke_2.classDebugEnabled
+ _kPLSleepWakeAgentEventPointNameCoSocPowerTriggerType_block_invoke_2.defaultOnce
+ _kPLXPCAgentComputeEmbeddingsForQuery
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_2.classDebugEnabled.583
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_2.defaultOnce.582
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.classDebugEnabled.830
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.classDebugEnabled.837
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.defaultOnce.829
+ _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.defaultOnce.836
+ _kPRearNits_block_invoke_2.classDebugEnabled.1473
+ _kPRearNits_block_invoke_2.defaultOnce.1472
+ _kPRearNits_block_invoke_3.classDebugEnabled.1538
+ _kPRearNits_block_invoke_3.defaultOnce.1537
+ _kPRearNits_block_invoke_4.classDebugEnabled.1734
+ _kPRearNits_block_invoke_4.classDebugEnabled.1741
+ _kPRearNits_block_invoke_4.defaultOnce.1733
+ _kPRearNits_block_invoke_4.defaultOnce.1740
+ _kSymptomActivityBitmapWiFiNonInfraInterface
+ _ledgerDataAtIndex:forPid:.classDebugEnabled.512
+ _ledgerDataAtIndex:forPid:.classDebugEnabled.518
+ _ledgerDataAtIndex:forPid:.defaultOnce.511
+ _ledgerDataAtIndex:forPid:.defaultOnce.517
+ _logCoalitionObjectDifference:.classDebugEnabled.781
+ _logCoalitionObjectDifference:.defaultOnce.780
+ _logEventBackwardHeatMap.classDebugEnabled.4114
+ _logEventBackwardHeatMap.classDebugEnabled.4121
+ _logEventBackwardHeatMap.defaultOnce.4113
+ _logEventBackwardHeatMap.defaultOnce.4120
+ _logEventBackwardProcessExitHistogram:withStats:withDate:.classDebugEnabled.681
+ _logEventBackwardProcessExitHistogram:withStats:withDate:.defaultOnce.680
+ _logEventBackwardWifiProperties:.classDebugEnabled.1202
+ _logEventBackwardWifiProperties:.classDebugEnabled.1208
+ _logEventBackwardWifiProperties:.classDebugEnabled.1216
+ _logEventBackwardWifiProperties:.classDebugEnabled.1222
+ _logEventBackwardWifiProperties:.defaultOnce.1201
+ _logEventBackwardWifiProperties:.defaultOnce.1207
+ _logEventBackwardWifiProperties:.defaultOnce.1215
+ _logEventBackwardWifiProperties:.defaultOnce.1221
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2275
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2287
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2296
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2302
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2308
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2314
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2274
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2286
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2295
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2301
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2307
+ _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2313
+ _logEventForwardALSLux:.classDebugEnabled.1611
+ _logEventForwardALSLux:.defaultOnce.1610
+ _logEventForwardAWDLState:.classDebugEnabled.1148
+ _logEventForwardAWDLState:.defaultOnce.1147
+ _logEventForwardHotspotState:.classDebugEnabled.1157
+ _logEventForwardHotspotState:.defaultOnce.1156
+ _logEventForwardModuleInfo.classDebugEnabled.1116
+ _logEventForwardModuleInfo.defaultOnce.1115
+ _logEventIntervalGasGauge.classDebugEnabled.3976
+ _logEventIntervalGasGauge.defaultOnce.3975
+ _logEventIntervalKernelTaskMonitor.classDebugEnabled.706
+ _logEventIntervalKernelTaskMonitor.defaultOnce.705
+ _logEventNoneBatteryConfigWithRawData:.classDebugEnabled.4980
+ _logEventNoneBatteryConfigWithRawData:.defaultOnce.4979
+ _logEventPointMemoryTracking.classDebugEnabled.528
+ _logEventPointMemoryTracking.classDebugEnabled.534
+ _logEventPointMemoryTracking.classDebugEnabled.540
+ _logEventPointMemoryTracking.defaultOnce.527
+ _logEventPointMemoryTracking.defaultOnce.533
+ _logEventPointMemoryTracking.defaultOnce.539
+ _logEventPointWake:.classDebugEnabled.934
+ _logEventPointWake:.classDebugEnabled.950
+ _logEventPointWake:.classDebugEnabled.962
+ _logEventPointWake:.defaultOnce.933
+ _logEventPointWake:.defaultOnce.949
+ _logEventPointWake:.defaultOnce.961
+ _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.1059
+ _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.990
+ _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.996
+ _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.1058
+ _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.989
+ _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.995
+ _logEventPointWakeLink:withParams:toEntry:.classDebugEnabled.1104
+ _logEventPointWakeLink:withParams:toEntry:.defaultOnce.1103
+ _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1068
+ _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1077
+ _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1067
+ _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1076
+ _logMessage:withPayload:.classDebugEnabled.657
+ _logMessage:withPayload:.defaultOnce.654
+ _logMessage:withPayload:.defaultOnce.656
+ _logProcessExit.defaultOnce.551
+ _logProcessExit.defaultOnce.554
+ _logProcessExit.objectForKey.552
+ _logProcessExit.objectForKey.555
+ _mapDeletedAppsWithEnergyEntries:.classDebugEnabled.1815
+ _mapDeletedAppsWithEnergyEntries:.defaultOnce.1814
+ _mapPluginsToAppsWithEnergyEntries:.classDebugEnabled.1824
+ _mapPluginsToAppsWithEnergyEntries:.defaultOnce.1823
+ _metricNormalizer.onceToken
+ _metricNormalizer.val
+ _modelDisplayPowerFromIOMFB:.classDebugEnabled.2066
+ _modelDisplayPowerFromIOMFB:.defaultOnce.2065
+ _modelDynamicDisplayPower:.classDebugEnabled.2018
+ _modelDynamicDisplayPower:.defaultOnce.2017
+ _modelDynamicDisplayPowerFromAPL:.classDebugEnabled.2075
+ _modelDynamicDisplayPowerFromAPL:.defaultOnce.2074
+ _modelWiFiPower:.classDebugEnabled.2458
+ _modelWiFiPower:.defaultOnce.2457
+ _objc_msgSend$QOSBackground
+ _objc_msgSend$QOSUserInitiated
+ _objc_msgSend$QOSUserInteractive
+ _objc_msgSend$QOSUtility
+ _objc_msgSend$RBSStatetoPLState:state:
+ _objc_msgSend$URLQueryAllowedCharacterSet
+ _objc_msgSend$_accountingMetrics
+ _objc_msgSend$_calculateAccumSystemLoad:
+ _objc_msgSend$_calculateAndStoreSleepDuration
+ _objc_msgSend$_debugStringForPurgeableLabel:
+ _objc_msgSend$_getGPUTotalTime
+ _objc_msgSend$_handleDisplayLayoutUpdate:
+ _objc_msgSend$_handlePowerNotification:argument:
+ _objc_msgSend$_parseDisplayAZLMetricsFromEntry:
+ _objc_msgSend$_parseWifiPowerMetricsFromEntry:
+ _objc_msgSend$_purgeableLabelWithUrgency:startDate:
+ _objc_msgSend$_queryCumulativeNetworkBytes
+ _objc_msgSend$_registerNotificationWithAgent:type:tableName:isProcessSpecific:minRequestInterval:block:
+ _objc_msgSend$_sampleGPUTime
+ _objc_msgSend$_setUpSleepWakeMonitoring
+ _objc_msgSend$_setupMetrics
+ _objc_msgSend$_supportsGPUCoalitions
+ _objc_msgSend$_tearDownSleepWakeMonitoring
+ _objc_msgSend$accountingEnabled
+ _objc_msgSend$accumSystemLoad
+ _objc_msgSend$accumSystemLoadCount
+ _objc_msgSend$accumulatedDrainLevel
+ _objc_msgSend$addTotals:with:
+ _objc_msgSend$autoBrightnessSuggestion
+ _objc_msgSend$autolockSuggestion
+ _objc_msgSend$brightnessPercentage
+ _objc_msgSend$brightnessSum
+ _objc_msgSend$bundleIDToDisplayNameMap
+ _objc_msgSend$cellIn
+ _objc_msgSend$cellOut
+ _objc_msgSend$cellularPower
+ _objc_msgSend$comparisonDateIntervalsWithTargetStartTime:withEndTime:
+ _objc_msgSend$configurationForDefaultMainDisplayMonitor
+ _objc_msgSend$convertPPSSKALogEventName:
+ _objc_msgSend$createAnomalousAppEntriesFrom:
+ _objc_msgSend$createAppDataMapForComparisonDateIntervals:currentDateInterval:targetTopApps:
+ _objc_msgSend$createCoalescedBreakdownWithResponse:
+ _objc_msgSend$createPerAppBreakdown:
+ _objc_msgSend$criticalBatteryLevel
+ _objc_msgSend$currentPowerState
+ _objc_msgSend$dailyChargingStateIntervalsDict
+ _objc_msgSend$dcpDisplayStats
+ _objc_msgSend$dynamicEndOffset
+ _objc_msgSend$entryAggregateDefinitionSentKeepAlive
+ _objc_msgSend$entryEventForwardDefinitionRBSApplication
+ _objc_msgSend$entryEventPointDefinitionCoSocPower
+ _objc_msgSend$excludeTimeOnCharger
+ _objc_msgSend$experimentGroup
+ _objc_msgSend$getBattUIEntriesWithKey:inRange:
+ _objc_msgSend$getBatteryMaximumCapacityPercentWithError:
+ _objc_msgSend$getBreakdownForLength:fromCachedLength:forBucketSize:
+ _objc_msgSend$getChargingStateIntervalsDictWithRange:addToDailyArrays:
+ _objc_msgSend$getDrainPerBucketIn:
+ _objc_msgSend$getEnergyForAppWithBundleID:inDateInterval:
+ _objc_msgSend$getEnergyForQualificationID:withAppWithBundleID:inDateInterval:
+ _objc_msgSend$getInstalledPluginToParentIDMap
+ _objc_msgSend$getParentBundleIDForBundleID:
+ _objc_msgSend$getUsageTimesForAppWithBundleID:inDateInterval:
+ _objc_msgSend$gpuPower
+ _objc_msgSend$gpuTotalTime
+ _objc_msgSend$handleUrsaNotificationRequest:
+ _objc_msgSend$hasBatteryModuleAuth
+ _objc_msgSend$hasFixedChargingLimit
+ _objc_msgSend$hasInductiveCharging
+ _objc_msgSend$hasInternalKey:
+ _objc_msgSend$hasRearALS
+ _objc_msgSend$initWithHitchTimeRatio:perceivedHitchTimeRatio:
+ _objc_msgSend$initWithStartDate:endDate:accumulatedDrain:
+ _objc_msgSend$initWithUUIDBytes:
+ _objc_msgSend$initializeUrsaNotifications
+ _objc_msgSend$installedPluginToParentIDMap
+ _objc_msgSend$internalKey
+ _objc_msgSend$intervalSummaryItems:
+ _objc_msgSend$invalidateScreenStateUpdates
+ _objc_msgSend$isDateIntervalAnomalous:comparedTo:
+ _objc_msgSend$isDynamicEnd
+ _objc_msgSend$isPerfPowerMetricd
+ _objc_msgSend$isUsingAnOlderWifiChip
+ _objc_msgSend$isVirtualDevice
+ _objc_msgSend$kPLWiFiClassIsOneOf:
+ _objc_msgSend$lastSleepTime
+ _objc_msgSend$lastWakeTime
+ _objc_msgSend$logAggregateSentKeepAlive:
+ _objc_msgSend$logCoalitionObjectMemory:
+ _objc_msgSend$logEventForwardRBSApplicationForBundleID:withPid:withState:withReasons:withVisibility:
+ _objc_msgSend$logEventIntervalPowerExceptionsDetection:
+ _objc_msgSend$logEventPointGeofenceTrigger:
+ _objc_msgSend$logStatusKitAgentAggregatePushes:
+ _objc_msgSend$machTimeFromSeconds:
+ _objc_msgSend$markAsPurgeable:label:
+ _objc_msgSend$markAsPurgeable:urgency:startDate:
+ _objc_msgSend$middayFromMidnight:
+ _objc_msgSend$networkCumulativeCount
+ _objc_msgSend$normalizeBucket:to:
+ _objc_msgSend$normalizeForBucket:with:
+ _objc_msgSend$oneHzBicAccumCount
+ _objc_msgSend$oneHzFlipbookFrameCount
+ _objc_msgSend$oneHzFrameMissCount
+ _objc_msgSend$organizeStateIntervalsWithRange:lastBattUIEntry:chargingIntervalsDict:addToDailyArrays:
+ _objc_msgSend$pUUIDForPid:
+ _objc_msgSend$percentageOption
+ _objc_msgSend$possibleRequests
+ _objc_msgSend$predicatePowerLogProcesses
+ _objc_msgSend$prepareBreakdown:withDrainSummaries:withFullDayBreakdown:withDynamicBreakdown:
+ _objc_msgSend$prevCumulativeCellularInBytes
+ _objc_msgSend$prevCumulativeCellularOutBytes
+ _objc_msgSend$prevCumulativeWiFiInBytes
+ _objc_msgSend$prevCumulativeWiFiOutBytes
+ _objc_msgSend$prevGpuTotalTime
+ _objc_msgSend$rangeKeyForLength:bucketSize:
+ _objc_msgSend$receivedNetworkUpdate
+ _objc_msgSend$recentUsageInsight
+ _objc_msgSend$reduceBrightnessSuggestion
+ _objc_msgSend$screenState
+ _objc_msgSend$setAccountingEnabled:
+ _objc_msgSend$setAccumSystemLoad:
+ _objc_msgSend$setAccumSystemLoadCount:
+ _objc_msgSend$setAccumulatedDrainLevel:
+ _objc_msgSend$setBrightnessPercentage:
+ _objc_msgSend$setBrightnessSum:
+ _objc_msgSend$setBundleIDToDisplayNameMap:
+ _objc_msgSend$setCurrentPowerState:
+ _objc_msgSend$setDailyChargingStateIntervalsDict:
+ _objc_msgSend$setDailyLastBattEntry:
+ _objc_msgSend$setDcpDisplayStats:
+ _objc_msgSend$setDisplayEnergy:
+ _objc_msgSend$setDynamicEndOffset:
+ _objc_msgSend$setExcludeTimeOnCharger:
+ _objc_msgSend$setGpuTotalTime:
+ _objc_msgSend$setInstalledPluginToParentIDMap:
+ _objc_msgSend$setIsDynamicEnd:
+ _objc_msgSend$setIsReadyToMonitor:
+ _objc_msgSend$setLastEntryForMetricd:
+ _objc_msgSend$setLastSleepDuration:
+ _objc_msgSend$setLastSleepTime:
+ _objc_msgSend$setLastWakeTime:
+ _objc_msgSend$setLocationDesiredAccuracy:
+ _objc_msgSend$setMainDisplayMonitor:
+ _objc_msgSend$setNetworkCumulativeCount:
+ _objc_msgSend$setNetworkingPower:
+ _objc_msgSend$setOneHzBicAccumCount:
+ _objc_msgSend$setOneHzFlipbookFrameCount:
+ _objc_msgSend$setOneHzFrameMissCount:
+ _objc_msgSend$setPackageEnergy:
+ _objc_msgSend$setPercentageOption:
+ _objc_msgSend$setPmNotifier:
+ _objc_msgSend$setPowerExceptionsDetectionXPCListener:
+ _objc_msgSend$setPrevCumulativeCellularInBytes:
+ _objc_msgSend$setPrevCumulativeCellularOutBytes:
+ _objc_msgSend$setPrevCumulativeWiFiInBytes:
+ _objc_msgSend$setPrevCumulativeWiFiOutBytes:
+ _objc_msgSend$setPrevGpuTotalTime:
+ _objc_msgSend$setQOSBackground:
+ _objc_msgSend$setQOSUserInitiated:
+ _objc_msgSend$setQOSUserInteractive:
+ _objc_msgSend$setQOSUtility:
+ _objc_msgSend$setQosBackground:
+ _objc_msgSend$setQosUserInitiated:
+ _objc_msgSend$setQosUserInteractive:
+ _objc_msgSend$setQosUtility:
+ _objc_msgSend$setReceivedNetworkUpdate:
+ _objc_msgSend$setRootDomainConnect:
+ _objc_msgSend$setScreenState:
+ _objc_msgSend$setShouldSnapInterval:
+ _objc_msgSend$setShouldUseMidnightQueryRange:
+ _objc_msgSend$setStatusKitAgentAggregatedPushesListener:
+ _objc_msgSend$setSystemPowerPortRef:
+ _objc_msgSend$setTotalCell:
+ _objc_msgSend$setTotalWiFi:
+ _objc_msgSend$setTransitionHandler:
+ _objc_msgSend$setUpScreenStateUpdates
+ _objc_msgSend$setWeightOnScreen:
+ _objc_msgSend$shouldSnapInterval
+ _objc_msgSend$shouldUseMidnightQueryRange
+ _objc_msgSend$signalActive
+ _objc_msgSend$signalInactive
+ _objc_msgSend$snapIntervals:
+ _objc_msgSend$sortedAppEnergyArrayFromAppDataMap:
+ _objc_msgSend$startOfDayForDate:
+ _objc_msgSend$stateDidChange:state:prevState:
+ _objc_msgSend$stringByAddingPercentEncodingWithAllowedCharacters:
+ _objc_msgSend$supportsEnhancedAPFS
+ _objc_msgSend$systemPowerPortRef
+ _objc_msgSend$targetDateIntervalWithBucketStartTime:withEndTime:
+ _objc_msgSend$totalCell
+ _objc_msgSend$totalWiFi
+ _objc_msgSend$triggerLTSStats
+ _objc_msgSend$ursaBaseContent
+ _objc_msgSend$ursaBootargContent:
+ _objc_msgSend$ursaRadarContent:
+ _objc_msgSend$ursaTTRContent:
+ _objc_msgSend$wifiIn
+ _objc_msgSend$wifiOut
+ _os_variant_is_darwinos
+ _populateRootNodeEnergyKeysWithEnergyEntries:.classDebugEnabled.1608
+ _populateRootNodeEnergyKeysWithEnergyEntries:.classDebugEnabled.1614
+ _populateRootNodeEnergyKeysWithEnergyEntries:.defaultOnce.1607
+ _populateRootNodeEnergyKeysWithEnergyEntries:.defaultOnce.1613
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1944
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1961
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1969
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1943
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1960
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1968
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1977
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2018
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2028
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2031
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2019
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2029
+ _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2032
+ _reaccountBackupRestore:.classDebugEnabled.610
+ _reaccountBackupRestore:.defaultOnce.609
+ _reaccountBackupRestoreWithEnergyEntries:.classDebugEnabled.1880
+ _reaccountBackupRestoreWithEnergyEntries:.defaultOnce.1879
+ _readKeyViaOSAccum:toOutput:.classDebugEnabled.720
+ _readKeyViaOSAccum:toOutput:.classDebugEnabled.726
+ _readKeyViaOSAccum:toOutput:.defaultOnce.719
+ _readKeyViaOSAccum:toOutput:.defaultOnce.725
+ _resetPermissionsForClients.classDebugEnabled.679
+ _resetPermissionsForClients.defaultOnce.678
+ _respondToEvent:withResponse:.classDebugEnabled.633
+ _respondToEvent:withResponse:.classDebugEnabled.639
+ _respondToEvent:withResponse:.defaultOnce.632
+ _respondToEvent:withResponse:.defaultOnce.638
+ _setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3414
+ _setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3413
+ _shouldPopUpForPowerExceptionForProcess:.allowedProcesses
+ _shouldPopUpForPowerExceptionForProcess:.onceToken
+ _supportsEnhancedAPFS.onceToken
+ _supportsEnhancedAPFS.result
+ _transformPlugins:withBucket:.classDebugEnabled.621
+ _transformPlugins:withBucket:.defaultOnce.620
+ _wifiManufacturerQuery.classDebugEnabled.2392
+ _wifiManufacturerQuery.defaultOnce.2391
+ _xFlags.classDebugEnabled.5024
+ _xFlags.classDebugEnabled.5033
+ _xFlags.classDebugEnabled.5042
+ _xFlags.classDebugEnabled.5051
+ _xFlags.classDebugEnabled.5057
+ _xFlags.classDebugEnabled.5063
+ _xFlags.classDebugEnabled.5069
+ _xFlags.classDebugEnabled.5078
+ _xFlags.classDebugEnabled.5084
+ _xFlags.classDebugEnabled.5090
+ _xFlags.defaultOnce.5023
+ _xFlags.defaultOnce.5032
+ _xFlags.defaultOnce.5041
+ _xFlags.defaultOnce.5050
+ _xFlags.defaultOnce.5056
+ _xFlags.defaultOnce.5062
+ _xFlags.defaultOnce.5068
+ _xFlags.defaultOnce.5077
+ _xFlags.defaultOnce.5083
+ _xFlags.defaultOnce.5089
- +[PLBatteryAgent entryEventPointDefinitionPPMClientMetrics]
- +[PLBatteryAgent entryEventPointDefinitionPPMDebug]
- +[PLBatteryAgent hasWirelessCharger]
- +[PLBatteryAgent hasWirelessCharger].cold.1
- +[PLBatteryAgent supportsAccConnectionLogging]
- +[PLBatteryAgent supportsAccConnectionLogging].cold.1
- +[PLBatteryAgent supportsFixedLimitCharging]
- +[PLBatteryAgent supportsFixedLimitCharging].cold.1
- +[PLBatteryAgent supportsxFlags]
- +[PLBatteryAgent supportsxFlags].cold.1
- +[PLBatteryGaugeService load]
- +[PLBatteryGaugeService shouldCalculateDisplayCost]
- +[PLDisplayAgent shouldLogAPL].cold.1
- +[PLDisplayAgent shouldLogLuxStats].cold.1
- +[PLUtilities devBoardDevice]
- +[PLUtilities devBoardDevice].cold.1
- +[PLUtilities getDeviceSoC]
- +[PLUtilities getDeviceSoC].cold.1
- +[PLUtilities hardwareModelSMC:]
- +[PLUtilities hardwareModel]
- +[PLUtilities hardwareModel].cold.1
- +[PLUtilities markFileAsPurgeable:withUrgency:]
- +[PLUtilities markFileAsPurgeable:withUrgency:].cold.1
- +[PLUtilities markFilesAsPurgeable:withUrgency:]
- +[PLUtilities markFilesInDirectoryAsPurgeable:ofType:withUrgency:]
- +[PLUtilities markFilesInDirectoryAsPurgeable:ofType:withUrgency:].cold.1
- +[PLUtilities markFilesInDirectoryAsPurgeable:ofType:withUrgency:].cold.2
- +[PLUtilities productType]
- +[PLUtilities productType].cold.1
- +[PLXPCAgent entryEventBackwardDefinitionVoicemailDuration]
- +[PLXPCAgent entryEventIntervalDefinitionAnimatedStickerScoring]
- +[PLXPCAgent entryEventIntervalDefinitionMomentsDeferredProcessing]
- +[PLXPCAgent entryEventIntervalDefinitionStaticStickerScoring]
- -[PLBatteryAgent gasGagueConnection]
- -[PLBatteryAgent gasGaugeOpenAndStartLogging].cold.1
- -[PLBatteryAgent gasGaugeOpenAndStartLogging].cold.2
- -[PLBatteryAgent gasGaugeRead].cold.1
- -[PLBatteryAgent gasGaugeRead].cold.10
- -[PLBatteryAgent gasGaugeRead].cold.2
- -[PLBatteryAgent gasGaugeRead].cold.3
- -[PLBatteryAgent gasGaugeRead].cold.4
- -[PLBatteryAgent gasGaugeRead].cold.5
- -[PLBatteryAgent gasGaugeRead].cold.6
- -[PLBatteryAgent gasGaugeRead].cold.7
- -[PLBatteryAgent gasGaugeRead].cold.8
- -[PLBatteryAgent gasGaugeRead].cold.9
- -[PLBatteryAgent getPPMDebugData]
- -[PLBatteryAgent handlePPMCallback].cold.1
- -[PLBatteryAgent logPPMDebug]
- -[PLBatteryAgent setGasGagueConnection:]
- -[PLBatteryBreakdownService suggestionsWithEnergyEntries:].cold.5
- -[PLBatteryGaugeService .cxx_destruct]
- -[PLBatteryGaugeService DTQueryResponse:]
- -[PLBatteryGaugeService DTQueryResponse:].cold.1
- -[PLBatteryGaugeService applicationResults]
- -[PLBatteryGaugeService bundleIDandPidMap]
- -[PLBatteryGaugeService clearStateRoutine:]
- -[PLBatteryGaugeService clearStateRoutine:].cold.1
- -[PLBatteryGaugeService compileSnapshotResponse]
- -[PLBatteryGaugeService compileSnapshotResponse].cold.1
- -[PLBatteryGaugeService computeDisplayCostWithAvgRed:withAvgGreen:withAvgBlue:]
- -[PLBatteryGaugeService computeDisplayCostWithAvgRed:withAvgGreen:withAvgBlue:].cold.1
- -[PLBatteryGaugeService computeGPUCostWithGPUSec:]
- -[PLBatteryGaugeService computeGPUCostWithGPUSec:].cold.1
- -[PLBatteryGaugeService computeLocationCostWithWifiCost:withGpsCost:withCellCost:withSkyhookCost:]
- -[PLBatteryGaugeService computeLocationCostWithWifiCost:withGpsCost:withCellCost:withSkyhookCost:].cold.1
- -[PLBatteryGaugeService computeNetworkingCostWithWifiIn:withWifiOut:withCellIn:withCellOut:]
- -[PLBatteryGaugeService computeNetworkingCostWithWifiIn:withWifiOut:withCellIn:withCellOut:].cold.1
- -[PLBatteryGaugeService convertRawUsageToScore:]
- -[PLBatteryGaugeService convertRawUsageToScore:].cold.1
- -[PLBatteryGaugeService costElement]
- -[PLBatteryGaugeService curQueryCount]
- -[PLBatteryGaugeService curQueryTime]
- -[PLBatteryGaugeService dataReceivedFrom:]
- -[PLBatteryGaugeService dataReceivedFrom:].cold.1
- -[PLBatteryGaugeService entrykeyCallBackMapping]
- -[PLBatteryGaugeService entrykeyCallBackOnceMapping]
- -[PLBatteryGaugeService exitTimer]
- -[PLBatteryGaugeService extractAndSetProcessIdentifierWithPayload:]
- -[PLBatteryGaugeService extractAndSetProcessIdentifierWithPayload:].cold.1
- -[PLBatteryGaugeService extractAndSetProcessIdentifierWithPayload:].cold.2
- -[PLBatteryGaugeService extractAndTranslateProcessIdentifier:]
- -[PLBatteryGaugeService extractAndTranslateProcessIdentifier:].cold.1
- -[PLBatteryGaugeService getObjectInMeasurementsWithPid:withCategory:withKey:]
- -[PLBatteryGaugeService initOperatorDependancies]
- -[PLBatteryGaugeService initResponseSemaphore]
- -[PLBatteryGaugeService init]
- -[PLBatteryGaugeService isTestingRunning]
- -[PLBatteryGaugeService lastQueryCount]
- -[PLBatteryGaugeService lastQueryTime]
- -[PLBatteryGaugeService listAllRunningPidsWithBuffer:withSizeOfBuffer:]
- -[PLBatteryGaugeService locationResults]
- -[PLBatteryGaugeService matchingPidWithProcessName:withBundleID:]
- -[PLBatteryGaugeService measurements]
- -[PLBatteryGaugeService networkingCostElement]
- -[PLBatteryGaugeService parseApplicationResults:]
- -[PLBatteryGaugeService parseApplicationResults:].cold.1
- -[PLBatteryGaugeService parseApplicationResults:].cold.2
- -[PLBatteryGaugeService parseCoalitionResults:]
- -[PLBatteryGaugeService parseCoalitionResults:].cold.1
- -[PLBatteryGaugeService parseCoalitionResults:].cold.2
- -[PLBatteryGaugeService parseDisplayResults:]
- -[PLBatteryGaugeService parseDisplayResults:].cold.1
- -[PLBatteryGaugeService parseLocationResults:]
- -[PLBatteryGaugeService parseLocationResults:].cold.1
- -[PLBatteryGaugeService parseLocationResults:].cold.2
- -[PLBatteryGaugeService parseProcessMonitorResults:]
- -[PLBatteryGaugeService parseProcessMonitorResults:].cold.1
- -[PLBatteryGaugeService parseProcessMonitorResults:].cold.2
- -[PLBatteryGaugeService parseProcessNetworkResults:]
- -[PLBatteryGaugeService parseProcessNetworkResults:].cold.1
- -[PLBatteryGaugeService parseThermalStateCallback:]
- -[PLBatteryGaugeService parseThermalStateCallback:].cold.1
- -[PLBatteryGaugeService parseThermalStateCallback:].cold.2
- -[PLBatteryGaugeService pauseRoutineWithPayload:]
- -[PLBatteryGaugeService processMonitorResults]
- -[PLBatteryGaugeService processNetworkResults]
- -[PLBatteryGaugeService registerNotificationWithAgent:withType:withTableName:withCallBackType:withBlock:]
- -[PLBatteryGaugeService reportedApplication]
- -[PLBatteryGaugeService reportedLocation]
- -[PLBatteryGaugeService reportedProcessMonitor]
- -[PLBatteryGaugeService reportedProcessNetwork]
- -[PLBatteryGaugeService reported]
- -[PLBatteryGaugeService requestDataFrom:withType:]
- -[PLBatteryGaugeService requestDataFrom:withType:].cold.1
- -[PLBatteryGaugeService requestTime]
- -[PLBatteryGaugeService resetExitTimer]
- -[PLBatteryGaugeService resetExitTimer].cold.1
- -[PLBatteryGaugeService responseSemaphore]
- -[PLBatteryGaugeService responseTime]
- -[PLBatteryGaugeService results]
- -[PLBatteryGaugeService resumeRoutineWithPayload:]
- -[PLBatteryGaugeService returnTime]
- -[PLBatteryGaugeService scoringEntities]
- -[PLBatteryGaugeService selfExit:]
- -[PLBatteryGaugeService selfExit:].cold.1
- -[PLBatteryGaugeService setApplicationResults:]
- -[PLBatteryGaugeService setBundleIDandPidMap:]
- -[PLBatteryGaugeService setCostElement:]
- -[PLBatteryGaugeService setCurQueryCount:]
- -[PLBatteryGaugeService setCurQueryTime:]
- -[PLBatteryGaugeService setEntrykeyCallBackMapping:]
- -[PLBatteryGaugeService setEntrykeyCallBackOnceMapping:]
- -[PLBatteryGaugeService setExitTimer:]
- -[PLBatteryGaugeService setIsTestingRunning:]
- -[PLBatteryGaugeService setLastActiveStartTimeAndLastSuspendTimeWithPid:withAppState:withCurrentTime:]
- -[PLBatteryGaugeService setLastQueryCount:]
- -[PLBatteryGaugeService setLastQueryTime:]
- -[PLBatteryGaugeService setLocationResults:]
- -[PLBatteryGaugeService setMeasurements:]
- -[PLBatteryGaugeService setNetworkingCostElement:]
- -[PLBatteryGaugeService setObjectInMeasurementsWithObject:withPid:withCategory:withKey:]
- -[PLBatteryGaugeService setProcessMonitorResults:]
- -[PLBatteryGaugeService setProcessNetworkResults:]
- -[PLBatteryGaugeService setReported:]
- -[PLBatteryGaugeService setReportedApplication:]
- -[PLBatteryGaugeService setReportedLocation:]
- -[PLBatteryGaugeService setReportedProcessMonitor:]
- -[PLBatteryGaugeService setReportedProcessNetwork:]
- -[PLBatteryGaugeService setRequestTime:]
- -[PLBatteryGaugeService setResponseSemaphore:]
- -[PLBatteryGaugeService setResponseTime:]
- -[PLBatteryGaugeService setResults:]
- -[PLBatteryGaugeService setReturnTime:]
- -[PLBatteryGaugeService setStartTime:]
- -[PLBatteryGaugeService setStopTime:]
- -[PLBatteryGaugeService setThermalStateTimer:]
- -[PLBatteryGaugeService setTrackedProcesses:]
- -[PLBatteryGaugeService setXpcResponderBatteryGaugeDT:]
- -[PLBatteryGaugeService startRoutineWithPayload:]
- -[PLBatteryGaugeService startRoutineWithPayload:].cold.1
- -[PLBatteryGaugeService startRoutineWithPayload:].cold.2
- -[PLBatteryGaugeService startRoutineWithPayload:].cold.3
- -[PLBatteryGaugeService startRoutineWithPayload:].cold.4
- -[PLBatteryGaugeService startRoutineWithPayload:].cold.5
- -[PLBatteryGaugeService startRoutineWithPayload:].cold.6
- -[PLBatteryGaugeService startRoutineWithPayload:].cold.7
- -[PLBatteryGaugeService startRoutineWithPayload:].cold.8
- -[PLBatteryGaugeService startRoutineWithPayload:].cold.9
- -[PLBatteryGaugeService startTime]
- -[PLBatteryGaugeService stopRoutineWithPayload:]
- -[PLBatteryGaugeService stopRoutineWithPayload:].cold.1
- -[PLBatteryGaugeService stopRoutineWithPayload:].cold.2
- -[PLBatteryGaugeService stopRoutineWithPayload:].cold.3
- -[PLBatteryGaugeService stopRoutineWithPayload:].cold.4
- -[PLBatteryGaugeService stopRoutineWithPayload:].cold.5
- -[PLBatteryGaugeService stopTime]
- -[PLBatteryGaugeService testGaugeServiceSingleInstance:]
- -[PLBatteryGaugeService testGaugeServiceSingleInstance:].cold.1
- -[PLBatteryGaugeService testGaugeService]
- -[PLBatteryGaugeService thermalStateTimer]
- -[PLBatteryGaugeService trackedProcesses]
- -[PLBatteryGaugeService translateProcessIdentifierWithInput:]
- -[PLBatteryGaugeService translateProcessIdentifierWithInput:].cold.1
- -[PLBatteryGaugeService triggerAllData]
- -[PLBatteryGaugeService xpcResponderBatteryGaugeDT]
- -[PLBatteryUINotificationService initOperatorDependancies].cold.3
- -[PLBatteryUINotificationService initOperatorDependancies].cold.4
- -[PLBatteryUINotificationService surfaceNotificationForIssues:]
- -[PLBatteryUINotificationService surfaceNotificationForIssues:].cold.1
- -[PLBatteryUINotificationService ursaBootArgContent:]
- -[PLBatteryUINotificationService ursaBootArgContent:].cold.1
- -[PLBatteryUINotificationService ursaBootArgContent:].cold.2
- -[PLBatteryUINotificationService ursaBootArgContent:].cold.3
- -[PLBatteryUINotificationService ursaBootArgContent:].cold.4
- -[PLBatteryUINotificationService ursaNotificationContentWithIssue:]
- -[PLBatteryUINotificationService ursaNotificationContentWithIssue:].cold.1
- -[PLBatteryUINotificationService ursaNotificationContentWithIssue:].cold.2
- -[PLBatteryUINotificationService ursaNotificationRequestWithIssue:]
- -[PLBatteryUINotificationService ursaNotificationRequestWithIssue:].cold.1
- -[PLBatteryUINotificationService ursaPowerExceptionContent:]
- -[PLBatteryUINotificationService ursaPowerExceptionContent:].cold.1
- -[PLBatteryUINotificationService ursaPowerExceptionContent:].cold.2
- -[PLBatteryUINotificationService ursaPowerExceptionContent:].cold.3
- -[PLBatteryUINotificationService ursaPowerExceptionContent:].cold.4
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight .cxx_destruct]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight applyTransformationsForBuckets:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight appsForBackgroundActivityInsightFromApps:withThresholdAboveAverageBackgroundDrainPercentage:locationEnergyThreshold:inNDays:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight appsForBackgroundActivityInsight]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight averageBackgroundDrainThreshold]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight bucketSize]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight buckets]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight buildBucketWithEnergyEntries:andRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight buildBucketsForRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight buildEnergyEntriesWithRootNodes:andQualificationNodes:andRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight coalesce]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight computeNumberOfBuckets]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight configure:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight configure:].cold.1
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight dailyBackgroundDrainThreshold]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight daysToTrackActivityForBatteryBreakdown:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight dependencies]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight end]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight enumerateBucketsUsingBlock:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight generateRange:withDataRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight generateRangeFromConfiguration:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getAppRuntimesInRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getAppUsageEventsInRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getDataRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getDataRange:].cold.1
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getDataRange:].cold.2
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getDataRange:].cold.3
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getDataRange:].cold.4
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getNodeEntriesForEntryKey:withRange:andTimeInterval:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getNodeIDToNodeNameMap]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getNonAppRuntimesWith:identificationKey:andRange:withNow:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getQualificationNodeEntriesInRange:withTimeInterval:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight getRootNodeEntriesInRange:withTimeInterval:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight initializeBucketsWithRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight locationEnergyDrainThreshold]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight mockAppForBackgroundActivityInsight]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight monotonicNow]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight nodeIDsToNodeNames]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight perAppUsageForBatteryBreakdown:withStart:withEnd:withThresholdAboveDailyBackgroundDrainPercentage:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight prepareBucketsWithRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight prepareBucketsWithRange:].cold.1
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight prepareBucketsWithRange:].cold.2
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight processAppTimeEntries:inRange:withAppArray:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight processAppUsageEventsEntries:inRange:withAppArray:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight processQualificationNodes:inRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight processRootNodes:inRange:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight responderService]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight result]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight run]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight run].cold.1
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight run].cold.2
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight run].cold.3
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight run].cold.4
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight run].cold.5
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight run].cold.6
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight setAppsForBackgroundActivityInsight:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight setBucketSize:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight setBuckets:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight setEnd:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight setMonotonicNow:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight setNodeIDsToNodeNames:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight setResponderService:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight setStart:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight setSuggest:]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight shouldShowInsightThroughOverrides]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight start]
- -[PLBatteryUIResponseTypeBackgroundAppUsageInsight suggest]
- -[PLBatteryUIResponseTypeChargingStateIntervals getBattUIEntriesWithKey:]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight .cxx_destruct]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight batteryBreakdown_Last24hrs]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight coalesce]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight configure:]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight dependencies]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight didRestore]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight didRestore].cold.1
- -[PLBatteryUIResponseTypeOngoingRestoreInsight didUpgradeInLast:]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight didUpgradeInLast:].cold.1
- -[PLBatteryUIResponseTypeOngoingRestoreInsight end]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight lastUpgradeTimestamp]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight responderService]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight result]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight run]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight run].cold.1
- -[PLBatteryUIResponseTypeOngoingRestoreInsight run].cold.2
- -[PLBatteryUIResponseTypeOngoingRestoreInsight setBatteryBreakdown_Last24hrs:]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight setEnd:]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight setLastUpgradeTimestamp:]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight setResponderService:]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight setSuggest:]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight shouldShowSuggestionThroughOverrides]
- -[PLBatteryUIResponseTypeOngoingRestoreInsight suggest]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight .cxx_destruct]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight batteryBreakdown_Last24hrs]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight coalesce]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight configure:]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight dependencies]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight didUpgradeInLast:]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight didUpgradeInLast:].cold.1
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight didUpgrade]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight didUpgrade].cold.1
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight end]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight lastUpgradeTimestamp]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight responderService]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight result]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight run]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight run].cold.1
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight run].cold.2
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight setBatteryBreakdown_Last24hrs:]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight setEnd:]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight setLastUpgradeTimestamp:]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight setResponderService:]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight setSuggest:]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight shouldShowSuggestionThroughOverrides]
- -[PLBatteryUIResponseTypeOngoingUpgradeInsight suggest]
- -[PLBatteryUIResponseTypeUISOCLevel criticalLevel]
- -[PLCoalitionAgent logCoalitionObjectMemory:shouldLogBatteryTableCadence:]
- -[PLEnergyIssuesService handleStateChangeForSafeguards]
- -[PLEnergyIssuesService safeguardsDaemon]
- -[PLEnergyIssuesService setSafeguardsDaemon:]
- -[PLEnergyIssuesService setStateTrackerForSafeguards:]
- -[PLEnergyIssuesService stateTrackerForSafeguards]
- -[PLEnergyIssuesService updateDisplayState]
- -[PLEnergyIssuesService updateDisplayState].cold.1
- -[PLEnergyIssuesService updatePluggedInState]
- -[PLEnergyIssuesService updatePluggedInState].cold.1
- -[PLPowerMetricMonitorService _batteryGaugeServiceDidBecomeActive]
- -[PLPowerMetricMonitorService _batteryGaugeServiceDidBecomeActive].cold.1
- -[PLPowerMetricMonitorService _batteryGaugeServiceDidBecomeInactive]
- -[PLPowerMetricMonitorService _batteryGaugeServiceDidBecomeInactive].cold.1
- -[PLPowerMetricMonitorService _batteryGaugeServiceDidBecomeInactive].cold.2
- -[PLPowerMetricMonitorService _canCacheMetrics]
- -[PLPowerMetricMonitorService _computeEnergyScoreForProcess].cold.2
- -[PLPowerMetricMonitorService _emitPowerSignpostWithMetric:value:]
- -[PLPowerMetricMonitorService _emitPowerSignpostWithMetric:value:pid:]
- -[PLPowerMetricMonitorService _extractCurrentUsageMetrics]
- -[PLPowerMetricMonitorService _parseDisplayAZLMetricsFromEntry:cacheMetrics:]
- -[PLPowerMetricMonitorService _parseLocationMetricsFromEntry:].cold.2
- -[PLPowerMetricMonitorService _parseProcessMonitorMetricsFromEntry:]
- -[PLPowerMetricMonitorService _parseProcessMonitorMetricsFromEntry:].cold.1
- -[PLPowerMetricMonitorService _parseWifiPowerMetricsFromEntry:cacheMetrics:]
- -[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:canRequestWhileBatteryGaugeIsRunning:minRequestInterval:block:]
- -[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:canRequestWhileBatteryGaugeIsRunning:minRequestInterval:block:].cold.1
- -[PLPowerMetricMonitorService _sendMetrics]
- -[PLPowerMetricMonitorService batteryGaugeConflictingProcessSpecificEntryKeys]
- -[PLPowerMetricMonitorService batteryGaugeConflictingSystemMetricEntryKeys]
- -[PLPowerMetricMonitorService changeUpdateInterval:]
- -[PLPowerMetricMonitorService collectMetricsOnDemand]
- -[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]
- -[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:].cold.1
- -[PLPowerMetricMonitorService currentUpdateInterval]
- -[PLPowerMetricMonitorService currentUpdateMode]
- -[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]
- -[PLPowerMetricMonitorService setBatteryGaugeConflictingProcessSpecificEntryKeys:]
- -[PLPowerMetricMonitorService setBatteryGaugeConflictingSystemMetricEntryKeys:]
- -[PLPowerMetricMonitorService setUpdateInterval:]
- -[PLPowerMetricMonitorService setUpdateMode:]
- -[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]
- -[PLPowerMetricMonitorService updateBrightnessMetrics]
- -[PLPowerMetricMonitorService updateInterval]
- -[PLPowerMetricMonitorService updateMode]
- -[PLProcessMonitorAgent logEventIntervalProcessMonitorInterval]
- -[PLWifiAgent lastEntryForHelperd]
- -[PLWifiAgent setLastEntryForHelperd:]
- -[PLXPCAgent animatedStickerScoringListener]
- -[PLXPCAgent groupActivitiesXPCListener]
- -[PLXPCAgent logEventBackwardVoicemailDuration:]
- -[PLXPCAgent logEventIntervalAnimatedStickerScoring:]
- -[PLXPCAgent logEventIntervalGroupActivities:]
- -[PLXPCAgent logEventIntervalGroupActivities:].cold.1
- -[PLXPCAgent logEventIntervalMomentsDeferredProcessing:]
- -[PLXPCAgent logEventIntervalStaticStickerScoring:]
- -[PLXPCAgent momentsDeferredProcessingListener]
- -[PLXPCAgent setAnimatedStickerScoringListener:]
- -[PLXPCAgent setGroupActivitiesXPCListener:]
- -[PLXPCAgent setMomentsDeferredProcessingListener:]
- -[PLXPCAgent setStaticStickerScoringListener:]
- -[PLXPCAgent setVoicemailDurationListener:]
- -[PLXPCAgent staticStickerScoringListener]
- -[PLXPCAgent voicemailDurationListener]
- GCC_except_table111
- GCC_except_table119
- GCC_except_table123
- GCC_except_table126
- GCC_except_table128
- GCC_except_table135
- GCC_except_table144
- GCC_except_table148
- GCC_except_table17
- GCC_except_table202
- GCC_except_table235
- GCC_except_table245
- GCC_except_table269
- GCC_except_table274
- GCC_except_table275
- GCC_except_table280
- GCC_except_table281
- GCC_except_table282
- GCC_except_table286
- GCC_except_table31
- GCC_except_table328
- GCC_except_table330
- GCC_except_table334
- GCC_except_table38
- GCC_except_table445
- GCC_except_table454
- GCC_except_table468
- GCC_except_table47
- GCC_except_table51
- GCC_except_table58
- GCC_except_table59
- GCC_except_table61
- GCC_except_table63
- GCC_except_table74
- _CFAbsoluteTimeGetCurrent
- _CFArrayCreate
- _CFDataCreate
- _CFDataCreateMutable
- _CFDataGetMutableBytePtr
- _CFDataSetLength
- _CFRunLoopRunInMode
- _CFShow
- _CFStringCreateWithBytesNoCopy
- _CFStringCreateWithCString
- _DTQueryResponse:.classDebugEnabled
- _DTQueryResponse:.defaultOnce
- _IOConnectCallMethod
- _IOConnectCallStructMethod
- _IOConnectMapMemory
- _IOConnectUnmapMemory
- _IONotificationPortCreate
- _IONotificationPortGetRunLoopSource
- _IORegistryEntrySetCFProperties
- _IORegistryEntrySetCFProperty
- _NSClassFromString
- _NSStringFromBOOL
- _OBJC_CLASS_$_PLBatteryGaugeService
- _OBJC_CLASS_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight
- _OBJC_CLASS_$_PLBatteryUIResponseTypeOngoingRestoreInsight
- _OBJC_CLASS_$_PLBatteryUIResponseTypeOngoingUpgradeInsight
- _OBJC_CLASS_$_PLHelperdLifecycleManager
- _OBJC_IVAR_$_PLBatteryAgent._gasGagueConnection
- _OBJC_IVAR_$_PLBatteryGaugeService._applicationResults
- _OBJC_IVAR_$_PLBatteryGaugeService._bundleIDandPidMap
- _OBJC_IVAR_$_PLBatteryGaugeService._costElement
- _OBJC_IVAR_$_PLBatteryGaugeService._curQueryCount
- _OBJC_IVAR_$_PLBatteryGaugeService._curQueryTime
- _OBJC_IVAR_$_PLBatteryGaugeService._entrykeyCallBackMapping
- _OBJC_IVAR_$_PLBatteryGaugeService._entrykeyCallBackOnceMapping
- _OBJC_IVAR_$_PLBatteryGaugeService._exitTimer
- _OBJC_IVAR_$_PLBatteryGaugeService._isTestingRunning
- _OBJC_IVAR_$_PLBatteryGaugeService._lastQueryCount
- _OBJC_IVAR_$_PLBatteryGaugeService._lastQueryTime
- _OBJC_IVAR_$_PLBatteryGaugeService._locationResults
- _OBJC_IVAR_$_PLBatteryGaugeService._measurements
- _OBJC_IVAR_$_PLBatteryGaugeService._networkingCostElement
- _OBJC_IVAR_$_PLBatteryGaugeService._processMonitorResults
- _OBJC_IVAR_$_PLBatteryGaugeService._processNetworkResults
- _OBJC_IVAR_$_PLBatteryGaugeService._reported
- _OBJC_IVAR_$_PLBatteryGaugeService._reportedApplication
- _OBJC_IVAR_$_PLBatteryGaugeService._reportedLocation
- _OBJC_IVAR_$_PLBatteryGaugeService._reportedProcessMonitor
- _OBJC_IVAR_$_PLBatteryGaugeService._reportedProcessNetwork
- _OBJC_IVAR_$_PLBatteryGaugeService._requestTime
- _OBJC_IVAR_$_PLBatteryGaugeService._responseSemaphore
- _OBJC_IVAR_$_PLBatteryGaugeService._responseTime
- _OBJC_IVAR_$_PLBatteryGaugeService._results
- _OBJC_IVAR_$_PLBatteryGaugeService._returnTime
- _OBJC_IVAR_$_PLBatteryGaugeService._scoringEntities
- _OBJC_IVAR_$_PLBatteryGaugeService._startTime
- _OBJC_IVAR_$_PLBatteryGaugeService._stopTime
- _OBJC_IVAR_$_PLBatteryGaugeService._thermalStateTimer
- _OBJC_IVAR_$_PLBatteryGaugeService._trackedProcesses
- _OBJC_IVAR_$_PLBatteryGaugeService._xpcResponderBatteryGaugeDT
- _OBJC_IVAR_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight._appsForBackgroundActivityInsight
- _OBJC_IVAR_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight._bucketSize
- _OBJC_IVAR_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight._buckets
- _OBJC_IVAR_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight._end
- _OBJC_IVAR_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight._monotonicNow
- _OBJC_IVAR_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight._nodeIDsToNodeNames
- _OBJC_IVAR_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight._responderService
- _OBJC_IVAR_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight._start
- _OBJC_IVAR_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight._suggest
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingRestoreInsight._batteryBreakdown_Last24hrs
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingRestoreInsight._end
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingRestoreInsight._lastUpgradeTimestamp
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingRestoreInsight._responderService
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingRestoreInsight._suggest
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingUpgradeInsight._batteryBreakdown_Last24hrs
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingUpgradeInsight._end
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingUpgradeInsight._lastUpgradeTimestamp
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingUpgradeInsight._responderService
- _OBJC_IVAR_$_PLBatteryUIResponseTypeOngoingUpgradeInsight._suggest
- _OBJC_IVAR_$_PLEnergyIssuesService._safeguardsDaemon
- _OBJC_IVAR_$_PLEnergyIssuesService._stateTrackerForSafeguards
- _OBJC_IVAR_$_PLPowerMetricMonitorService._batteryGaugeConflictingProcessSpecificEntryKeys
- _OBJC_IVAR_$_PLPowerMetricMonitorService._batteryGaugeConflictingSystemMetricEntryKeys
- _OBJC_IVAR_$_PLPowerMetricMonitorService._updateInterval
- _OBJC_IVAR_$_PLPowerMetricMonitorService._updateMode
- _OBJC_IVAR_$_PLWifiAgent._lastEntryForHelperd
- _OBJC_IVAR_$_PLXPCAgent._animatedStickerScoringListener
- _OBJC_IVAR_$_PLXPCAgent._groupActivitiesXPCListener
- _OBJC_IVAR_$_PLXPCAgent._momentsDeferredProcessingListener
- _OBJC_IVAR_$_PLXPCAgent._staticStickerScoringListener
- _OBJC_IVAR_$_PLXPCAgent._voicemailDurationListener
- _OBJC_METACLASS_$_PLBatteryGaugeService
- _OBJC_METACLASS_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight
- _OBJC_METACLASS_$_PLBatteryUIResponseTypeOngoingRestoreInsight
- _OBJC_METACLASS_$_PLBatteryUIResponseTypeOngoingUpgradeInsight
- _OSThermalNotificationCurrentLevel
- _OUTLINED_FUNCTION_15
- _PLLogBatteryGaugeService
- _PLLogBatteryGaugeService.cold.1
- _PLLogBatteryGaugeService.log
- _PLLogBatteryGaugeService.onceToken
- _PLLogNetwork
- _PLLogNetwork.__logObj
- _PLLogNetwork.cold.1
- _PLLogNetwork.onceToken
- _PowerChangedCallback.classDebugEnabled.415
- _PowerChangedCallback.classDebugEnabled.421
- _PowerChangedCallback.classDebugEnabled.431
- _PowerChangedCallback.classDebugEnabled.437
- _PowerChangedCallback.defaultOnce.414
- _PowerChangedCallback.defaultOnce.420
- _PowerChangedCallback.defaultOnce.430
- _PowerChangedCallback.defaultOnce.436
- _UpSeconds
- _UpSeconds.boottime
- __OBJC_$_CLASS_METHODS_PLBatteryGaugeService
- __OBJC_$_INSTANCE_METHODS_PLBatteryGaugeService
- __OBJC_$_INSTANCE_METHODS_PLBatteryUIResponseTypeBackgroundAppUsageInsight
- __OBJC_$_INSTANCE_METHODS_PLBatteryUIResponseTypeOngoingRestoreInsight
- __OBJC_$_INSTANCE_METHODS_PLBatteryUIResponseTypeOngoingUpgradeInsight
- __OBJC_$_INSTANCE_VARIABLES_PLBatteryGaugeService
- __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIResponseTypeBackgroundAppUsageInsight
- __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIResponseTypeOngoingRestoreInsight
- __OBJC_$_INSTANCE_VARIABLES_PLBatteryUIResponseTypeOngoingUpgradeInsight
- __OBJC_$_PROP_LIST_PLBatteryGaugeService
- __OBJC_$_PROP_LIST_PLBatteryUIResponseTypeBackgroundAppUsageInsight
- __OBJC_$_PROP_LIST_PLBatteryUIResponseTypeOngoingRestoreInsight
- __OBJC_$_PROP_LIST_PLBatteryUIResponseTypeOngoingUpgradeInsight
- __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight
- __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIResponseTypeOngoingRestoreInsight
- __OBJC_CLASS_PROTOCOLS_$_PLBatteryUIResponseTypeOngoingUpgradeInsight
- __OBJC_CLASS_RO_$_PLBatteryGaugeService
- __OBJC_CLASS_RO_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight
- __OBJC_CLASS_RO_$_PLBatteryUIResponseTypeOngoingRestoreInsight
- __OBJC_CLASS_RO_$_PLBatteryUIResponseTypeOngoingUpgradeInsight
- __OBJC_METACLASS_RO_$_PLBatteryGaugeService
- __OBJC_METACLASS_RO_$_PLBatteryUIResponseTypeBackgroundAppUsageInsight
- __OBJC_METACLASS_RO_$_PLBatteryUIResponseTypeOngoingRestoreInsight
- __OBJC_METACLASS_RO_$_PLBatteryUIResponseTypeOngoingUpgradeInsight
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN12PLProcessCPU12inode_data_tEEEPvEENS_22__hash_node_destructorINS_9allocatorIS7_EEEEE5resetB8ne190102EPS7_
- __ZNSt3__112__destroy_atB8ne190102INS_4pairIKyN12PLProcessCPU12inode_data_tEEELi0EEEvPT_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102ILi0EEEPKc
- __ZNSt3__113__tree_removeB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___101-[PLXPCService handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.860
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.791
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.803
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.807
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.807.cold.1
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.807.cold.2
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.829
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.836
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.843
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.843.cold.1
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.850
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke.854
- ___102-[PLXPCService handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:]_block_invoke_2.844
- ___105-[PLBatteryGaugeService registerNotificationWithAgent:withType:withTableName:withCallBackType:withBlock:]_block_invoke
- ___105-[PLBatteryGaugeService registerNotificationWithAgent:withType:withTableName:withCallBackType:withBlock:]_block_invoke.cold.1
- ___105-[PLBatteryGaugeService registerNotificationWithAgent:withType:withTableName:withCallBackType:withBlock:]_block_invoke_2
- ___157-[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:canRequestWhileBatteryGaugeIsRunning:minRequestInterval:block:]_block_invoke
- ___157-[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:canRequestWhileBatteryGaugeIsRunning:minRequestInterval:block:]_block_invoke_2
- ___157-[PLPowerMetricMonitorService _registerNotificationWithAgent:type:tableName:isProcessSpecific:canRequestWhileBatteryGaugeIsRunning:minRequestInterval:block:]_block_invoke_2.cold.1
- ___20-[PLXPCService init]_block_invoke.534
- ___20-[PLXPCService init]_block_invoke.534.cold.1
- ___20-[PLXPCService init]_block_invoke.555
- ___20-[PLXPCService init]_block_invoke.562
- ___20-[PLXPCService init]_block_invoke.570
- ___20-[PLXPCService init]_block_invoke.574
- ___20-[PLXPCService init]_block_invoke.574.cold.1
- ___20-[PLXPCService init]_block_invoke.574.cold.2
- ___20-[PLXPCService init]_block_invoke.581
- ___20-[PLXPCService init]_block_invoke.585
- ___20-[PLXPCService init]_block_invoke.585.cold.1
- ___20-[PLXPCService init]_block_invoke.596
- ___20-[PLXPCService init]_block_invoke_2.575
- ___20-[PLXPCService init]_block_invoke_2.586
- ___22-[PLBatteryAgent init]_block_invoke.3352
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.1
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.10
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.11
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.2
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.3
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.4
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.5
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.6
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.7
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.8
- ___22-[PLBatteryAgent init]_block_invoke.3352.cold.9
- ___22-[PLBatteryAgent init]_block_invoke.3364
- ___22-[PLBatteryAgent init]_block_invoke.3367
- ___22-[PLBatteryAgent init]_block_invoke.3393
- ___22-[PLBatteryAgent init]_block_invoke.3396
- ___22-[PLBatteryAgent init]_block_invoke.3404
- ___22-[PLBatteryAgent init]_block_invoke.3404.cold.1
- ___22-[PLBatteryAgent init]_block_invoke.3404.cold.2
- ___22-[PLBatteryAgent init]_block_invoke.3410
- ___22-[PLBatteryAgent init]_block_invoke.3414
- ___22-[PLBatteryAgent init]_block_invoke_2.3436
- ___22-[PLDisplayAgent init]_block_invoke.1409
- ___22-[PLDisplayAgent init]_block_invoke.1409.cold.1
- ___22-[PLDisplayAgent init]_block_invoke.1409.cold.2
- ___22-[PLDisplayAgent init]_block_invoke.1409.cold.3
- ___22-[PLDisplayAgent init]_block_invoke.1409.cold.4
- ___22-[PLDisplayAgent init]_block_invoke.1420
- ___22-[PLDisplayAgent init]_block_invoke.1424
- ___22-[PLDisplayAgent init]_block_invoke.1428
- ___22-[PLDisplayAgent init]_block_invoke.1434
- ___22-[PLDisplayAgent init]_block_invoke.1434.cold.1
- ___22-[PLDisplayAgent init]_block_invoke.1434.cold.2
- ___22-[PLDisplayAgent init]_block_invoke.1452
- ___22-[PLDisplayAgent init]_block_invoke.1460
- ___22-[PLDisplayAgent init]_block_invoke_2.1411
- ___22-[PLDisplayAgent init]_block_invoke_2.1430
- ___22-[PLDisplayAgent init]_block_invoke_2.1430.cold.1
- ___22-[PLDisplayAgent init]_block_invoke_2.1430.cold.2
- ___22-[PLDisplayAgent init]_block_invoke_2.1446
- ___22-[PLDisplayAgent init]_block_invoke_2.1463
- ___24-[PLBatteryAgent xFlags]_block_invoke.5229
- ___24-[PLBatteryAgent xFlags]_block_invoke.5238
- ___24-[PLBatteryAgent xFlags]_block_invoke.5247
- ___24-[PLBatteryAgent xFlags]_block_invoke.5256
- ___24-[PLBatteryAgent xFlags]_block_invoke.5262
- ___24-[PLBatteryAgent xFlags]_block_invoke.5268
- ___24-[PLBatteryAgent xFlags]_block_invoke.5274
- ___24-[PLBatteryAgent xFlags]_block_invoke.5283
- ___24-[PLBatteryAgent xFlags]_block_invoke.5289
- ___24-[PLBatteryAgent xFlags]_block_invoke.5295
- ___26+[PLUtilities productType]_block_invoke
- ___27+[PLUtilities getDeviceSoC]_block_invoke
- ___28+[PLUtilities hardwareModel]_block_invoke
- ___28+[PLUtilities hardwareModel]_block_invoke.cold.1
- ___28+[PLUtilities hardwareModel]_block_invoke.cold.2
- ___29+[PLUtilities devBoardDevice]_block_invoke
- ___29+[PLUtilities devBoardDevice]_block_invoke.cold.1
- ___29+[PLUtilities deviceBootUUID]_block_invoke.117
- ___30+[PLDisplayAgent shouldLogAPL]_block_invoke
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5138
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5144
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5150
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5156
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5161
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5169
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5175
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5181
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5187
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke.5193
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke_2
- ___30-[PLBatteryAgent gasGaugeRead]_block_invoke_2.5196
- ___30-[PLWifiAgent modelWiFiPower:]_block_invoke.2456
- ___32+[PLBatteryAgent supportsxFlags]_block_invoke
- ___32-[PLBatteryAgent aggdTimerFired]_block_invoke.4836
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3539
- ___32-[PLBatteryAgent getIOPSDevices]_block_invoke.3545
- ___33+[PLPushAgent bundleIdFromTopic:]_block_invoke.341
- ___33-[PLBatteryAgent cancelEALogging]_block_invoke.3525
- ___33-[PLBatteryAgent setupCSMLogging]_block_invoke.5308
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.932
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.948
- ___33-[PLWifiAgent logEventPointWake:]_block_invoke.960
- ___34+[PLSMCAgent reportPMUEventsToCA:]_block_invoke.905
- ___35+[PLDisplayAgent shouldLogLuxStats]_block_invoke
- ___35-[PLBatteryAgent handlePPMCallback]_block_invoke
- ___35-[PLBatteryAgent handlePPMCallback]_block_invoke_2
- ___36+[PLBatteryAgent hasWirelessCharger]_block_invoke
- ___36-[PLWifiAgent wifiManufacturerQuery]_block_invoke.2390
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.686
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.692
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.698
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.704
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.713
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.723
- ___36-[PLXPCService handlePeer:forEvent:]_block_invoke.727
- ___37+[PLUtilities exitWithReason:action:]_block_invoke.178
- ___37-[PLXPCAgent logEventForwardGMSOptIn]_block_invoke.2997
- ___38-[PLBatteryAgent handleBDCAMALogging:]_block_invoke.3895
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1907
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1907.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1915
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1915.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1923
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1923.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1931
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1931.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1939
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1939.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1947.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1963
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1963.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1971
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1971.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1979
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1979.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1990
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.1990.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2001
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2001.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2012
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2012.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2023
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2023.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2034
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2034.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2039
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2053
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2053.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2061
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2061.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2066
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2066.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2073
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2073.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2080
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2088
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2088.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2098
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2098.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2103
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2103.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2110
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2110.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2115
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2115.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2125
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2125.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2133
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2133.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2141
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2141.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2178
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2178.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2186
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2186.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2194
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2194.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2201
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2201.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2206
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2206.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2214
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2214.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2219
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2219.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2229
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2229.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2237
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2237.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2245
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2245.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2268
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2268.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2273
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2273.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2283
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2283.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2296
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2296.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2304
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2304.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2309
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2309.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2314
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2314.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2322
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2322.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2332
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2332.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2349
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2349.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2357
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2357.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2375
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2375.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2383
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2383.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2390
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2390.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2400
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2400.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2410
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2410.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2418
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2418.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2437
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2437.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2456
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2456.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2490
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2490.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2498
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2498.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2508
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2508.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2516
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2516.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2526
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2526.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2554
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2554.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2564
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2564.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2572
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2572.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2580
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2580.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2585
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2585.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2590
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2590.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2595
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2595.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2600
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2600.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2607
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2607.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2612
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2612.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2617
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2617.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2627
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2627.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2641
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2641.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2648
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2648.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2658
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2658.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2666
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2666.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2674
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2674.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2682
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2682.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2690
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2690.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2705
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2705.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2715
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2715.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2723
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2723.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2731
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2731.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2739
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2739.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2746
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2746.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2754
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2754.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2764
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2764.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2774
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2774.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2784
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2784.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2791
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2791.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2801
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2801.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2809
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2809.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2817
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2817.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2832
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2832.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2837
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2837.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2844
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2844.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2849
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2849.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2857
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2857.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2862
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2862.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2869
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2869.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2879
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2879.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2887
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2887.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2899
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2899.cold.1
- ___38-[PLXPCAgent initOperatorDependancies]_block_invoke.2900
- ___39-[PLProcessMonitorAgent logProcessExit]_block_invoke.548
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.191
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.191.cold.1
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.200
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.200.cold.1
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.208
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.208.cold.1
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.216
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.216.cold.1
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.224
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.224.cold.1
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.232
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.232.cold.1
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.253
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.253.cold.1
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.261
- ___39-[PLPushAgent initOperatorDependancies]_block_invoke.261.cold.1
- ___39-[PLXPCService logMessage:withPayload:]_block_invoke.652
- ___40-[PLDisplayAgent logEventForwardALSLux:]_block_invoke.1590
- ___40-[PLWifiAgent logEventForwardAWDLState:]_block_invoke.1146
- ___40-[PLWifiAgent logEventForwardModuleInfo]_block_invoke.1114
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4236
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke.4243
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4239
- ___41-[PLBatteryAgent logEventBackwardHeatMap]_block_invoke_2.4246
- ___41-[PLBatteryGaugeService DTQueryResponse:]_block_invoke
- ___41-[PLBatteryGaugeService DTQueryResponse:]_block_invoke.232
- ___41-[PLBatteryGaugeService DTQueryResponse:]_block_invoke.cold.1
- ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.706
- ___41-[PLSMCAgent readKeyViaOSAccum:toOutput:]_block_invoke.712
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3617
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3623
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3623.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3639
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3732
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3732.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3732.cold.2
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3732.cold.3
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3749
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3749.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3760
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3764
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3764.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3772
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3772.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3779
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3788
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3794
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3801
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3801.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3808
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3808.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3822
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3822.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3827
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3827.cold.1
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3834
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke.3857
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3624
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3669
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3756
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3773
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3783
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3791
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3802
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3809
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_2.3865
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_3.3869
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_4.3873
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_5.3877
- ___42-[PLBatteryAgent initOperatorDependancies]_block_invoke_6.3879
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5459
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5459.cold.1
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5459.cold.2
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke.5467
- ___42-[PLBatteryAgent initSmartChargingLogging]_block_invoke_2.5461
- ___42-[PLBatteryAgent logEventIntervalGasGauge]_block_invoke.4101
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1481
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1497
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1510
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1510.cold.1
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1510.cold.2
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1517
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke.1523
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1500
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1511
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1528
- ___42-[PLDisplayAgent initOperatorDependancies]_block_invoke_2.1528.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1786
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1786.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1791
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1791.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1798
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1798.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1803
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1803.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1813
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1813.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1835
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1835.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1852
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1852.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1864
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1864.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1871
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1871.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1881
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1881.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1889
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1889.cold.1
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1896
- ___42-[PLXPCAgent initTaskOperatorDependancies]_block_invoke.1896.cold.1
- ___42-[PLXPCService resetPermissionsForClients]_block_invoke.667
- ___42-[PLXPCService resetPermissionsForClients]_block_invoke.677
- ___43-[PLDisplayAgent modelDynamicDisplayPower:]_block_invoke.1994
- ___43-[PLSMCAgent logThermalAggregationKeysToCA]_block_invoke.696
- ___43-[PLWifiAgent logEventForwardHotspotState:]_block_invoke.1155
- ___44+[PLBatteryAgent supportsFixedLimitCharging]_block_invoke
- ___44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.447
- ___44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.447.cold.1
- ___44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.449
- ___44-[PLCoalitionAgent initOperatorDependancies]_block_invoke.474
- ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.631
- ___44-[PLXPCService respondToEvent:withResponse:]_block_invoke.637
- ___45-[PLBatteryAgent gasGaugeOpenAndStartLogging]_block_invoke
- ___45-[PLBatteryAgent gasGaugeOpenAndStartLogging]_block_invoke.5129
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5495
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5496
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5497
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5498
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5499
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5499.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5500
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5500.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5501
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5501.cold.1
- ___45-[PLBatteryAgent logCPMSSnapshotWithTrigger:]_block_invoke.5542
- ___45-[PLDisplayAgent modelDisplayPowerFromIOMFB:]_block_invoke.2042
- ___45-[PLSoCAgent taskingEndNotificationReceived:]_block_invoke
- ___45-[PLSoCAgent taskingEndNotificationReceived:]_block_invoke.cold.1
- ___45-[PLSoCAgent taskingEndNotificationReceived:]_block_invoke.cold.2
- ___46+[PLBatteryAgent supportsAccConnectionLogging]_block_invoke
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.382
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.385
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.385.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.408
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.438
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.438.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.444
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.444.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.449
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.449.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.456
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.456.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.466
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.466.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.473
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.473.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.480
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.480.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.485
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.485.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.490
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.490.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.498
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.498.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.506
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.506.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.511
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.511.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.516
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.516.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.517
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.531
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.531.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.539
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke.539.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.396
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.409
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.518
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.518.cold.1
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_2.518.cold.2
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_3.406
- ___46-[PLApplicationAgent initOperatorDependancies]_block_invoke_3.412
- ___46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.283
- ___46-[PLProcessNetworkAgent logEventBackwardUsage]_block_invoke.283.cold.1
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1200
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1206
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1214
- ___46-[PLWifiAgent logEventBackwardWifiProperties:]_block_invoke.1220
- ___47-[PLBatteryUIResponderService linkDependencies]_block_invoke.65
- ___47-[PLSoCAgent taskingStartNotificationReceived:]_block_invoke
- ___47-[PLSoCAgent taskingStartNotificationReceived:]_block_invoke.cold.1
- ___47-[PLSoCAgent taskingStartNotificationReceived:]_block_invoke.cold.2
- ___48-[PLPowerMetricMonitorService currentUpdateMode]_block_invoke
- ___49-[PLBatteryGaugeService initOperatorDependancies]_block_invoke
- ___49-[PLBatteryGaugeService initOperatorDependancies]_block_invoke.68
- ___49-[PLBatteryGaugeService initOperatorDependancies]_block_invoke.cold.1
- ___49-[PLBatteryGaugeService initOperatorDependancies]_block_invoke.cold.2
- ___49-[PLBatteryGaugeService initOperatorDependancies]_block_invoke_2
- ___49-[PLBatteryGaugeService initOperatorDependancies]_block_invoke_3
- ___49-[PLBatteryGaugeService initOperatorDependancies]_block_invoke_4
- ___49-[PLBatteryGaugeService initOperatorDependancies]_block_invoke_5
- ___49-[PLBatteryGaugeService initOperatorDependancies]_block_invoke_6
- ___49-[PLCoalitionAgent logCoalitionObjectDifference:]_block_invoke.783
- ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.423
- ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.423.cold.1
- ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.432
- ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.432.cold.1
- ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.449
- ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.449.cold.1
- ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.464
- ___49-[PLProcessMonitorAgent initOperatorDependancies]_block_invoke.464.cold.1
- ___49-[PLProcessMonitorAgent updateProcessExitSummary]_block_invoke.472
- ___49-[PLProcessMonitorAgent updateProcessExitSummary]_block_invoke.472.cold.1
- ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.212
- ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.242
- ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.242.cold.1
- ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.251
- ___49-[PLProcessNetworkAgent initOperatorDependancies]_block_invoke.251.cold.1
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5484
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5485
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5489
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5489.cold.1
- ___50-[PLBatteryAgent initializeChargingStateIntervals]_block_invoke.5489.cold.2
- ___50-[PLBatteryGaugeService requestDataFrom:withType:]_block_invoke
- ___50-[PLDisplayAgent modelDynamicDisplayPowerFromAPL:]_block_invoke.2051
- ___50-[PLProcessMonitorAgent disableProcessExitLogging]_block_invoke.484
- ___50-[PLProcessMonitorAgent ledgerDataAtIndex:forPid:]_block_invoke.508
- ___50-[PLProcessMonitorAgent ledgerDataAtIndex:forPid:]_block_invoke.514
- ___51-[PLBatteryGaugeService parseThermalStateCallback:]_block_invoke
- ___51-[PLBatteryUIResponseTypeOngoingRestoreInsight run]_block_invoke
- ___51-[PLBatteryUIResponseTypeOngoingRestoreInsight run]_block_invoke.cold.1
- ___51-[PLBatteryUIResponseTypeOngoingUpgradeInsight run]_block_invoke
- ___51-[PLBatteryUIResponseTypeOngoingUpgradeInsight run]_block_invoke.cold.1
- ___51-[PLEnergyIssuesService initializeSafeguardsSystem]_block_invoke
- ___51-[PLEnergyIssuesService initializeSafeguardsSystem]_block_invoke_2
- ___52-[PLBatteryGaugeService parseProcessMonitorResults:]_block_invoke
- ___52-[PLBatteryUIResponseTypeChargingStateIntervals run]_block_invoke
- ___52-[PLPowerMetricMonitorService changeUpdateInterval:]_block_invoke
- ___52-[PLPowerMetricMonitorService changeUpdateInterval:]_block_invoke.cold.1
- ___52-[PLPowerMetricMonitorService currentUpdateInterval]_block_invoke
- ___52-[PLProcessMonitorAgent logEventPointMemoryTracking]_block_invoke.524
- ___52-[PLProcessMonitorAgent logEventPointMemoryTracking]_block_invoke.530
- ___52-[PLProcessMonitorAgent logEventPointMemoryTracking]_block_invoke.536
- ___53-[PLBatteryUINotificationService surfaceNotification]_block_invoke.108
- ___53-[PLBatteryUINotificationService ursaBootArgContent:]_block_invoke
- ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke
- ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.235
- ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.235.cold.1
- ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.cold.1
- ___53-[PLPowerMetricMonitorService collectMetricsOnDemand]_block_invoke.cold.2
- ___53-[PLProcessMonitorAgent logEventPointFreezerDemotion]_block_invoke.625
- ___54-[PLBatteryAgent showOrHideTLCNotification:timeInTLC:]_block_invoke.3477
- ___54-[PLBatteryUIResponseTypeOngoingRestoreInsight result]_block_invoke
- ___54-[PLBatteryUIResponseTypeOngoingRestoreInsight result]_block_invoke_2
- ___54-[PLBatteryUIResponseTypeOngoingUpgradeInsight result]_block_invoke
- ___54-[PLBatteryUIResponseTypeOngoingUpgradeInsight result]_block_invoke_2
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.740
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.749
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.755
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.761
- ___54-[PLXPCService handleSingleMessage:fromPeer:forEvent:]_block_invoke.767
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5092
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5092.cold.1
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5096
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5096.cold.1
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5101
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke.5105
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5097
- ___55-[PLBatteryAgent logEventNoneBatteryConfigWithRawData:]_block_invoke_2.5102
- ___55-[PLCoalitionAgent processPerAppLogicalWritesWithInfo:]_block_invoke.812
- ___55-[PLPowerMetricMonitorService initOperatorDependancies]_block_invoke
- ___55-[PLPowerMetricMonitorService initOperatorDependancies]_block_invoke_2
- ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1066
- ___55-[PLWifiAgent logEventPointWakePNO:withParams:toEntry:]_block_invoke.1075
- ___56-[PLApplicationAgent createWidgetStatsAccountingEvents:]_block_invoke.569
- ___56-[PLWifiAgent logEventPointWakeLink:withParams:toEntry:]_block_invoke.1102
- ___57-[PLBatteryUIResponseTypeBatteryBreakdown addQualifiers:]_block_invoke.360
- ___58-[PLBatteryBreakdownService suggestionsWithEnergyEntries:]_block_invoke.1275
- ___58-[PLBatteryBreakdownService suggestionsWithEnergyEntries:]_block_invoke.1285
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37.cold.1
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37.cold.2
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37.cold.3
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37.cold.4
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37.cold.5
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37.cold.6
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37.cold.7
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37.cold.8
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.37.cold.9
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.45
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.68
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.88
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.88.cold.1
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.88.cold.2
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.88.cold.3
- ___58-[PLBatteryUINotificationService initOperatorDependancies]_block_invoke.88.cold.4
- ___58-[PLBatteryUIResponseTypeBackgroundAppUsageInsight result]_block_invoke
- ___58-[PLProcessMonitorAgent logEventIntervalKernelTaskMonitor]_block_invoke.690
- ___59-[PLBatteryAgent setupEALoggingTriggeredByConnectionEvent:]_block_invoke.3505
- ___60-[PLBatteryUINotificationService ursaPowerExceptionContent:]_block_invoke
- ___61-[PLBatteryBreakdownService mapDeletedAppsWithEnergyEntries:]_block_invoke.1832
- ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.214
- ___61-[PLBatteryUIResponderService convertResponseToLegacyFormat:]_block_invoke.249
- ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke
- ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.234
- ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.cold.1
- ___61-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke.cold.2
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.1057
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.988
- ___61-[PLWifiAgent logEventPointWakeDataFrame:withParams:toEntry:]_block_invoke.994
- ___63-[PLBatteryBreakdownService mapPluginsToAppsWithEnergyEntries:]_block_invoke.1841
- ___63-[PLBatteryUINotificationService surfaceNotificationForIssues:]_block_invoke
- ___63-[PLBatteryUINotificationService surfaceNotificationForIssues:]_block_invoke.cold.1
- ___63-[PLBatteryUINotificationService surfaceNotificationForIssues:]_block_invoke.cold.2
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1713
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1720
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1725
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1725.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1731
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1731.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1742.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1743
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1743.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1744
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1744.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1745
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1745.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1746
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1746.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1747.cold.2
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1754
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1754.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1758
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1758.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1763
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1792
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1793
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke.1793.cold.1
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1726
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1738
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1759
- ___63-[PLDisplayAgent handleBrightnessClientNotification:withValue:]_block_invoke_2.1786
- ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1905
- ___64-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:]_block_invoke.1909
- ___64-[PLPowerMetricMonitorService addMonitoredProcessWithPID:error:]_block_invoke.cold.4
- ___65-[PLBatteryAgent logEventBackwardHeatMapCallback:andHeatMapType:]_block_invoke.4499
- ___65-[PLBatteryUIResponseTypeBatteryBreakdown collapseEnergyEntries:]_block_invoke.559
- ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke
- ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.241
- ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.241.cold.1
- ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.cold.1
- ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.cold.2
- ___65-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke.cold.3
- ___66-[PLBatteryUIResponseTypeBatteryBreakdown reaccountBackupRestore:]_block_invoke.591
- ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1926
- ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1932
- ___67-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:]_block_invoke.1938
- ___68-[PLBatteryBreakdownService determineDisplayNamesWithEnergyEntries:]_block_invoke.1920
- ___69-[PLBatteryBreakdownService reaccountBackupRestoreWithEnergyEntries:]_block_invoke.1894
- ___71-[PLBatteryUIResponseTypeBatteryBreakdown transformPlugins:withBucket:]_block_invoke.605
- ___73-[PLBatteryBreakdownService populateRootNodeEnergyKeysWithEnergyEntries:]_block_invoke.1625
- ___73-[PLBatteryBreakdownService populateRootNodeEnergyKeysWithEnergyEntries:]_block_invoke.1631
- ___74+[PLUtilities getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:]_block_invoke.136
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1758
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1770
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1778
- ___74-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:]_block_invoke.1784
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82.cold.1
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82.cold.2
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.82.cold.3
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.86
- ___75+[PLUtilities remove:oldestFilesFromDirectory:containingFileNameSubstring:]_block_invoke.86.cold.1
- ___75-[PLBatteryBreakdownService addNotificationValues:withRange:withQueryType:]_block_invoke.1748
- ___76-[PLBatteryUIResponseTypeBackgroundAppUsageInsight prepareBucketsWithRange:]_block_invoke
- ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1799
- ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1805
- ___77-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:]_block_invoke.1813
- ___79-[PLBatteryUIResponseTypeBackgroundAppUsageInsight initializeBucketsWithRange:]_block_invoke
- ___79-[PLBatteryUIResponseTypeBackgroundAppUsageInsight initializeBucketsWithRange:]_block_invoke.cold.1
- ___81-[PLApplicationAgent logInstalledAppWithRecord:withBundleID:shouldMaskTimestamp:]_block_invoke.606
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1961
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1986
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.1994
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2036
- ___81-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:]_block_invoke.2046
- ___81-[PLProcessMonitorAgent logEventBackwardProcessExitHistogram:withStats:withDate:]_block_invoke.665
- ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke
- ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.233
- ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.cold.1
- ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke.cold.2
- ___83-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke_2
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2273
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2285
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2294
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2300
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2306
- ___84-[PLWifiAgent logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:]_block_invoke.2312
- ___87-[PLCoalitionAgent logToCAProcessMemory:andAccumulatedMemory:dailyReport:systemUptime:]_block_invoke.511
- ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1550
- ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1556
- ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1562
- ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1568
- ___88-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:]_block_invoke.1574
- ___90-[PLXPCService handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:]_block_invoke.781
- ___99-[PLProcessMonitorAgent logEventPointProcessExit:excludeProcesses:withStats:withDate:withNowInSec:]_block_invoke.576
- ___99-[PLProcessMonitorAgent logEventPointProcessExit:excludeProcesses:withStats:withDate:withNowInSec:]_block_invoke_2.598
- ___PLLogBatteryGaugeService_block_invoke
- ___PLLogNetwork_block_invoke
- ___PowerChangedCallback_block_invoke.416
- ___PowerChangedCallback_block_invoke.422
- ___PowerChangedCallback_block_invoke.426
- ___PowerChangedCallback_block_invoke.426.cold.1
- ___PowerChangedCallback_block_invoke.432
- ___PowerChangedCallback_block_invoke.438
- ___block_descriptor_40_e8_32r_e29_v32?0"NSDictionary"8Q16^B24lr32l8
- ___block_descriptor_40_e8_32s_e24_v16?0"NSNotification"8ls32l8
- ___block_descriptor_40_e8_32s_e25_v32?0"NSNumber"816^B24ls32l8
- ___block_descriptor_40_e8_32w_e74_v32?0"RBSProcessMonitor"8"RBSProcessHandle"16"RBSProcessStateUpdate"24lw32l8
- ___block_descriptor_56_e8_32s40s48bs_e38_v32?0"NSDictionary"8"NSString"1624ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48r_e35_v32?0"NSString"8"NSString"16^B24lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_72_e8_32s40s48s_e57_v44?0i8{_PLTimeIntervalRange=dd}12"NSDate"28"NSDate"36ls32l8s40l8s48l8
- ___block_literal_global.104
- ___block_literal_global.107
- ___block_literal_global.110
- ___block_literal_global.122
- ___block_literal_global.132
- ___block_literal_global.141
- ___block_literal_global.155
- ___block_literal_global.1740
- ___block_literal_global.1745
- ___block_literal_global.180
- ___block_literal_global.1822
- ___block_literal_global.1824
- ___block_literal_global.1826
- ___block_literal_global.1828
- ___block_literal_global.1830
- ___block_literal_global.1832
- ___block_literal_global.1834
- ___block_literal_global.1836
- ___block_literal_global.1838
- ___block_literal_global.1847
- ___block_literal_global.1887
- ___block_literal_global.1889
- ___block_literal_global.1891
- ___block_literal_global.1932
- ___block_literal_global.20
- ___block_literal_global.2116
- ___block_literal_global.216
- ___block_literal_global.225
- ___block_literal_global.234
- ___block_literal_global.2359
- ___block_literal_global.252
- ___block_literal_global.270
- ___block_literal_global.285
- ___block_literal_global.288
- ___block_literal_global.2889
- ___block_literal_global.293
- ___block_literal_global.301
- ___block_literal_global.306
- ___block_literal_global.314
- ___block_literal_global.322
- ___block_literal_global.327
- ___block_literal_global.3339
- ___block_literal_global.335
- ___block_literal_global.3451
- ___block_literal_global.3464
- ___block_literal_global.3479
- ___block_literal_global.3530
- ___block_literal_global.3585
- ___block_literal_global.3642
- ___block_literal_global.368
- ___block_literal_global.3686
- ___block_literal_global.3695
- ___block_literal_global.3704
- ___block_literal_global.371
- ___block_literal_global.3716
- ___block_literal_global.380
- ___block_literal_global.3829
- ___block_literal_global.3881
- ___block_literal_global.3894
- ___block_literal_global.3904
- ___block_literal_global.404
- ___block_literal_global.410
- ___block_literal_global.412
- ___block_literal_global.417
- ___block_literal_global.422
- ___block_literal_global.424
- ___block_literal_global.431
- ___block_literal_global.434
- ___block_literal_global.437
- ___block_literal_global.447
- ___block_literal_global.452
- ___block_literal_global.4548
- ___block_literal_global.456
- ___block_literal_global.464
- ___block_literal_global.473
- ___block_literal_global.4792
- ___block_literal_global.48
- ___block_literal_global.4804
- ___block_literal_global.4854
- ___block_literal_global.513
- ___block_literal_global.5433
- ___block_literal_global.5494
- ___block_literal_global.552
- ___block_literal_global.553
- ___block_literal_global.628
- ___block_literal_global.693
- ___block_literal_global.695
- ___block_literal_global.699
- ___block_literal_global.70
- ___block_literal_global.706
- ___block_literal_global.708
- ___block_literal_global.713
- ___block_literal_global.718
- ___block_literal_global.725
- ___block_literal_global.726
- ___block_literal_global.728
- ___block_literal_global.731
- ___block_literal_global.734
- ___block_literal_global.789
- ___block_literal_global.791
- ___block_literal_global.837
- ___block_literal_global.839
- ___block_literal_global.841
- ___block_literal_global.843
- ___block_literal_global.845
- ___block_literal_global.847
- ___block_literal_global.85
- ___block_literal_global.864
- ___block_literal_global.868
- ___block_literal_global.870
- ___block_literal_global.872
- ___block_literal_global.874
- ___block_literal_global.876
- ___block_literal_global.879
- ___block_literal_global.88
- ___block_literal_global.881
- ___block_literal_global.901
- ___block_literal_global.91
- ___block_literal_global.932
- ___block_literal_global.98
- ___fakeSleep_block_invoke.373
- ___fakeSleep_block_invoke.385
- ___fakeSleep_block_invoke.389
- ___fakeSleep_block_invoke.389.cold.1
- ___fakeSleep_block_invoke.395
- _addQualifiers:.classDebugEnabled.359
- _addQualifiers:.defaultOnce.358
- _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1798
- _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1804
- _applyStaticNameTransformationsWithEnergyEntries:.classDebugEnabled.1812
- _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1797
- _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1803
- _applyStaticNameTransformationsWithEnergyEntries:.defaultOnce.1811
- _batteryThread
- _battery_health_metric_config
- _bq_sealed
- _bq_sealed.cold.1
- _bq_sleep_mode
- _bq_vlow_enable
- _bq_write_dfchecksum
- _calculateBatteryHealthMetric
- _calculateChemicalWeightedRa
- _calculateWra
- _cancelEALogging.classDebugEnabled.3524
- _cancelEALogging.defaultOnce.3523
- _combineDuplicatesWithEnergyEntries:.classDebugEnabled.1904
- _combineDuplicatesWithEnergyEntries:.classDebugEnabled.1911
- _combineDuplicatesWithEnergyEntries:.defaultOnce.1903
- _combineDuplicatesWithEnergyEntries:.defaultOnce.1910
- _controlOp16
- _controlRead16
- _controlReadS16
- _controlReadU16
- _controlWrite16
- _createStringWithBytes
- _dailyTasks.defaultOnce.610
- _debugLog
- _debugLog.cold.1
- _debugLog.cold.2
- _debug_cnt_ut_err
- _debug_cnt_ut_recv
- _debug_cnt_ut_sent
- _debug_polling
- _determineDisplayNamesWithEnergyEntries:.classDebugEnabled.1919
- _determineDisplayNamesWithEnergyEntries:.defaultOnce.1918
- _determinePoSMThreshold
- _determinePoSMThreshold.lastAbove95
- _determinePoSMThreshold.lastBatteryCycleCount
- _determinePoSMThreshold.lastToT
- _determinePoSMThreshold.vac95Threshold
- _determinePoSMThreshold.vac95pThreshold
- _determinePoSMThreshold.vacThreshold
- _determinePoSMThreshold.vacpThreshold
- _determineVACVoltage
- _determineVACVoltage.lastBatteryCycleCount
- _determineVACVoltage.lastTimeAbove95
- _determineVACVoltage.lastToT
- _determineVACVoltage.vac95BasedVoltageMV
- _determineVACVoltage.vacBasedVoltageMV
- _devBoardDevice._devBoard
- _devBoardDevice.onceToken
- _deviceBootUUID.classDebugEnabled.116
- _deviceBootUUID.defaultOnce.115
- _disableProcessExitLogging.classDebugEnabled.483
- _disableProcessExitLogging.defaultOnce.482
- _drainDataLog
- _dumpBuffer
- _dynamicATV
- _dynamicATV.cold.1
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1549
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1555
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1561
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1567
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.classDebugEnabled.1573
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1548
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1554
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1560
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1566
- _energyEntriesWithRange:withEntryTimeInterval:withQueryType:.defaultOnce.1572
- _fakeSleep.classDebugEnabled.372
- _fakeSleep.classDebugEnabled.384
- _fakeSleep.classDebugEnabled.394
- _fakeSleep.defaultOnce.371
- _fakeSleep.defaultOnce.383
- _fakeSleep.defaultOnce.393
- _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1757
- _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1769
- _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1777
- _filterEnergyEntriesBasedOnTime:withQueryType:.classDebugEnabled.1783
- _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1756
- _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1768
- _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1776
- _filterEnergyEntriesBasedOnTime:withQueryType:.defaultOnce.1782
- _filterWithEnergyEntries:withQueryType:.classDebugEnabled.1925
- _filterWithEnergyEntries:withQueryType:.classDebugEnabled.1931
- _filterWithEnergyEntries:withQueryType:.classDebugEnabled.1937
- _filterWithEnergyEntries:withQueryType:.defaultOnce.1924
- _filterWithEnergyEntries:withQueryType:.defaultOnce.1930
- _filterWithEnergyEntries:withQueryType:.defaultOnce.1936
- _findRaWeightMulitplier
- _find_pmu.pmu_service
- _find_pmu.tmp
- _find_pmu.zero_number
- _gRestrictLogCounter
- _gRestrictLogMessagesCounter
- _gasGaugeOpenAndStartLogging.classDebugEnabled
- _gasGaugeOpenAndStartLogging.classDebugEnabled.5128
- _gasGaugeOpenAndStartLogging.defaultOnce
- _gasGaugeOpenAndStartLogging.defaultOnce.5127
- _gasGaugeRead.classDebugEnabled
- _gasGaugeRead.classDebugEnabled.5137
- _gasGaugeRead.classDebugEnabled.5143
- _gasGaugeRead.classDebugEnabled.5149
- _gasGaugeRead.classDebugEnabled.5155
- _gasGaugeRead.classDebugEnabled.5163
- _gasGaugeRead.classDebugEnabled.5168
- _gasGaugeRead.classDebugEnabled.5174
- _gasGaugeRead.classDebugEnabled.5180
- _gasGaugeRead.classDebugEnabled.5186
- _gasGaugeRead.classDebugEnabled.5195
- _gasGaugeRead.defaultOnce
- _gasGaugeRead.defaultOnce.5136
- _gasGaugeRead.defaultOnce.5142
- _gasGaugeRead.defaultOnce.5148
- _gasGaugeRead.defaultOnce.5154
- _gasGaugeRead.defaultOnce.5160
- _gasGaugeRead.defaultOnce.5162
- _gasGaugeRead.defaultOnce.5167
- _gasGaugeRead.defaultOnce.5173
- _gasGaugeRead.defaultOnce.5179
- _gasGaugeRead.defaultOnce.5185
- _gasGaugeRead.defaultOnce.5191
- _gasGaugeRead.defaultOnce.5194
- _gasGaugeRead.maxCurrent
- _gasGaugeRead.maxCurrentTime
- _gasGaugeRead.minCurrent
- _gasGaugeRead.minCurrentTime
- _gasGaugeRead.objectForKey
- _gasGaugeRead.objectForKey.5192
- _gasGaugeRead.savedStartDate
- _gasGaugeRead.totalCurrent
- _gasGaugeRead.totalEnergy
- _gasGaugeRead.totalNumReadings
- _gasgauge_close
- _gasgauge_currentlog_entries
- _gasgauge_currentlog_entries.cold.1
- _gasgauge_currentlog_entries.cold.2
- _gasgauge_currentlog_get_entries
- _gasgauge_currentlog_interval
- _gasgauge_currentlog_sleepinterval
- _gasgauge_currentlog_start
- _gasgauge_currentlog_start__
- _gasgauge_currentlog_start__.cold.1
- _gasgauge_currentlog_start_collection
- _gasgauge_currentlog_stop
- _gasgauge_currentlog_stop.cold.1
- _gasgauge_disconnect
- _gasgauge_info
- _gasgauge_open
- _gasgauge_sn
- _gasgauge_start_update_thread
- _gasgauge_swupdate
- _gasgauge_swupdate_log
- _gasgauge_swupdate_log.cold.1
- _gasgauge_watch
- _gaugeDisableInterrupts
- _gaugeDisconnect
- _gaugeEnableInterrupts
- _gauge_reset_count
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.classDebugEnabled.135
- _getCurrentMonotonicAndMachAbsTime:machAbsTime:machContTime:.defaultOnce.134
- _getDeviceSoC._soc
- _getDeviceSoC.onceToken
- _getFWVersion
- _getFWVersion.gFWVersion
- _getIOPSDevices.classDebugEnabled.3538
- _getIOPSDevices.classDebugEnabled.3544
- _getIOPSDevices.defaultOnce.3537
- _getIOPSDevices.defaultOnce.3543
- _getUPOData
- _gettimeofday
- _ggctl_close_device
- _ggctl_connect
- _ggctl_connect.cold.1
- _ggctl_connect.cold.2
- _ggctl_controlRead16
- _ggctl_controlWrite16
- _ggctl_disconnect
- _ggctl_drainDataLog
- _ggctl_enable_currentlog
- _ggctl_gaugeInterrupts
- _ggctl_get_device_configuration
- _ggctl_get_hdq_state
- _ggctl_hdqBreak
- _ggctl_hdqRead16
- _ggctl_hdqRead8
- _ggctl_hdqWrite8
- _ggctl_logShutdownReason
- _ggctl_logShutdownReason2
- _ggctl_map_currentlog
- _ggctl_open_device
- _ggctl_open_device.cold.1
- _ggctl_open_device.cold.2
- _ggctl_open_device.cold.3
- _ggctl_open_device.cold.4
- _ggctl_readBlock
- _ggctl_reset
- _ggctl_reset.cold.1
- _ggctl_writeBlock
- _handleBrightnessClientNotification:withValue:.classDebugEnabled.1791
- _handleBrightnessClientNotification:withValue:.defaultOnce.1790
- _handlePPMCallback.classDebugEnabled
- _handlePPMCallback.defaultOnce
- _handlePPMCallback.defaultOnce.3885
- _handlePPMCallback.objectForKey
- _handlePeer:forEvent:.classDebugEnabled.685
- _handlePeer:forEvent:.classDebugEnabled.691
- _handlePeer:forEvent:.classDebugEnabled.697
- _handlePeer:forEvent:.classDebugEnabled.703
- _handlePeer:forEvent:.classDebugEnabled.712
- _handlePeer:forEvent:.classDebugEnabled.722
- _handlePeer:forEvent:.defaultOnce.684
- _handlePeer:forEvent:.defaultOnce.690
- _handlePeer:forEvent:.defaultOnce.696
- _handlePeer:forEvent:.defaultOnce.702
- _handlePeer:forEvent:.defaultOnce.711
- _handlePeer:forEvent:.defaultOnce.721
- _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.859
- _handlePeerListenerEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.858
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.790
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.802
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.classDebugEnabled.849
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.789
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.801
- _handlePeerResponderEvent:withMessage:withClientID:withProcessName:withKey:withPayload:.defaultOnce.848
- _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:.classDebugEnabled.780
- _handlePeerShouldLogEvent:withMessage:withClientID:withProcessName:withKey:.defaultOnce.779
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.739
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.748
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.754
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.760
- _handleSingleMessage:fromPeer:forEvent:.classDebugEnabled.766
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.738
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.747
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.753
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.759
- _handleSingleMessage:fromPeer:forEvent:.defaultOnce.765
- _hardwareModel._hardwareModel
- _hardwareModel.onceToken
- _hasWirelessCharger.__hasWirelessCharger
- _hasWirelessCharger.onceToken
- _hdqBreak
- _hdqRead8
- _hdqReadS16
- _hdqReadS8
- _hdqReadU16
- _hdqReadU8
- _hdqWrite8
- _init.classDebugEnabled.1419
- _init.classDebugEnabled.561
- _init.classDebugEnabled.569
- _init.defaultOnce.1418
- _init.defaultOnce.560
- _init.defaultOnce.568
- _initComputeSafeguards
- _initOperatorDependancies.classDebugEnabled.3782
- _initOperatorDependancies.classDebugEnabled.3790
- _initOperatorDependancies.classDebugEnabled.3793
- _initOperatorDependancies.defaultOnce.3781
- _initOperatorDependancies.defaultOnce.3789
- _initOperatorDependancies.defaultOnce.3792
- _iokit_callback
- _kCFAllocatorNull
- _kCFBooleanFalse
- _kCFBooleanTrue
- _kCFTypeArrayCallBacks
- _kPLBatteryAgentEventPointNamePPMClientMetrics
- _kPLBatteryAgentEventPointNamePPMDebug
- _kPLBatteryAgentStringAvgRdcRatio
- _kPLBatteryAgentStringBaselineSysCap
- _kPLBatteryAgentStringBdg
- _kPLBatteryAgentStringCar
- _kPLBatteryAgentStringClient
- _kPLBatteryAgentStringIdx
- _kPLBatteryAgentStringModeledSysCap
- _kPLBatteryAgentStringNetSysCap
- _kPLBatteryAgentStringOutputFlag
- _kPLBatteryAgentStringOverrideSysCap
- _kPLBatteryAgentStringPPMDebugTimestamp
- _kPLBatteryAgentStringPb
- _kPLBatteryAgentStringPp
- _kPLBatteryAgentStringProactiveSysCap
- _kPLBatteryAgentStringPs
- _kPLBatteryAgentStringPwr
- _kPLBatteryAgentStringR0
- _kPLBatteryAgentStringR1
- _kPLBatteryAgentStringR2
- _kPLBatteryAgentStringR3
- _kPLBatteryAgentStringReqBdg
- _kPLBatteryAgentStringTotalDemandAdj
- _kPLBatteryAgentStringTotalDemandRaw
- _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3395
- _kPLBatteryAgentStringUserType_block_invoke.classDebugEnabled.3409
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3354
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3391
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3394
- _kPLBatteryAgentStringUserType_block_invoke.defaultOnce.3408
- _kPLBatteryAgentStringUserType_block_invoke.objectForKey.3392
- _kPLBatteryAgentStringUserType_block_invoke_12.classDebugEnabled.5466
- _kPLBatteryAgentStringUserType_block_invoke_12.defaultOnce.5465
- _kPLBatteryAgentStringUserType_block_invoke_2.classDebugEnabled.3616
- _kPLBatteryAgentStringUserType_block_invoke_2.defaultOnce.3615
- _kPLBatteryAgentStringVgg
- _kPLBatteryAgentStringbaselineR0
- _kPLBatteryAgentStringbaselineR1
- _kPLBatteryAgentStringbaselineR2
- _kPLBatteryAgentStringbaselineR3
- _kPLBatteryAgentStringmPb
- _kPLBatteryAgentStringmPp
- _kPLEntry
- _kPLGPUTime
- _kPLGPUTime_block_invoke.classDebugEnabled
- _kPLGPUTime_block_invoke.defaultOnce
- _kPLHelperdLifecycleManagerServiceIsActiveNotification
- _kPLHelperdLifecycleManagerServiceIsInactiveNotification
- _kPLHelperdLifecycleManagerServiceKey
- _kPLResponseSemaphore
- _kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke.classDebugEnabled
- _kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke.defaultOnce
- _kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_2.classDebugEnabled
- _kPLSleepWakeAgentEventPointNameScheduledWakeProcessName_block_invoke_2.defaultOnce
- _kPLUINUrsaBootArgCategory
- _kPLUINUrsaPowerExceptionCategory
- _kPLXPCAgentEventBackwardNameVoicemailDuration
- _kPLXPCAgentEventIntervalNameAnimatedStickerScoring
- _kPLXPCAgentEventIntervalNameMomentsDeferredProcessing
- _kPLXPCAgentEventIntervalNameStaticStickerScoring
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_2.classDebugEnabled.580
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_2.defaultOnce.579
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.classDebugEnabled.828
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.classDebugEnabled.835
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.defaultOnce.827
- _kPLXPCServiceEventPointNameClientLoggingDrops_block_invoke_6.defaultOnce.834
- _kPRearNits_block_invoke_2.classDebugEnabled.1451
- _kPRearNits_block_invoke_2.defaultOnce.1450
- _kPRearNits_block_invoke_3.classDebugEnabled.1516
- _kPRearNits_block_invoke_3.defaultOnce.1515
- _kPRearNits_block_invoke_4.classDebugEnabled.1712
- _kPRearNits_block_invoke_4.classDebugEnabled.1719
- _kPRearNits_block_invoke_4.defaultOnce.1711
- _kPRearNits_block_invoke_4.defaultOnce.1718
- _ledgerDataAtIndex:forPid:.classDebugEnabled.507
- _ledgerDataAtIndex:forPid:.classDebugEnabled.513
- _ledgerDataAtIndex:forPid:.defaultOnce.506
- _ledgerDataAtIndex:forPid:.defaultOnce.512
- _logCoalitionObjectDifference:.classDebugEnabled.782
- _logCoalitionObjectDifference:.defaultOnce.781
- _logEventBackwardHeatMap.classDebugEnabled.4238
- _logEventBackwardHeatMap.classDebugEnabled.4245
- _logEventBackwardHeatMap.defaultOnce.4237
- _logEventBackwardHeatMap.defaultOnce.4244
- _logEventBackwardProcessExitHistogram:withStats:withDate:.classDebugEnabled.664
- _logEventBackwardProcessExitHistogram:withStats:withDate:.defaultOnce.663
- _logEventBackwardWifiProperties:.classDebugEnabled.1199
- _logEventBackwardWifiProperties:.classDebugEnabled.1205
- _logEventBackwardWifiProperties:.classDebugEnabled.1213
- _logEventBackwardWifiProperties:.classDebugEnabled.1219
- _logEventBackwardWifiProperties:.defaultOnce.1198
- _logEventBackwardWifiProperties:.defaultOnce.1204
- _logEventBackwardWifiProperties:.defaultOnce.1212
- _logEventBackwardWifiProperties:.defaultOnce.1218
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2272
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2284
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2293
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2299
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2305
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.classDebugEnabled.2311
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2271
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2283
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2292
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2298
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2304
- _logEventBackwardWifiProperties:withNetworkProperties:shallModelPower:.defaultOnce.2310
- _logEventForwardALSLux:.classDebugEnabled.1589
- _logEventForwardALSLux:.defaultOnce.1588
- _logEventForwardAWDLState:.classDebugEnabled.1145
- _logEventForwardAWDLState:.defaultOnce.1144
- _logEventForwardHotspotState:.classDebugEnabled.1154
- _logEventForwardHotspotState:.defaultOnce.1153
- _logEventForwardModuleInfo.classDebugEnabled.1113
- _logEventForwardModuleInfo.defaultOnce.1112
- _logEventIntervalGasGauge.classDebugEnabled.4100
- _logEventIntervalGasGauge.defaultOnce.4099
- _logEventIntervalKernelTaskMonitor.classDebugEnabled.689
- _logEventIntervalKernelTaskMonitor.defaultOnce.688
- _logEventNoneBatteryConfigWithRawData:.classDebugEnabled.5104
- _logEventNoneBatteryConfigWithRawData:.defaultOnce.5103
- _logEventPointMemoryTracking.classDebugEnabled.523
- _logEventPointMemoryTracking.classDebugEnabled.529
- _logEventPointMemoryTracking.classDebugEnabled.535
- _logEventPointMemoryTracking.defaultOnce.522
- _logEventPointMemoryTracking.defaultOnce.528
- _logEventPointMemoryTracking.defaultOnce.534
- _logEventPointWake:.classDebugEnabled.931
- _logEventPointWake:.classDebugEnabled.947
- _logEventPointWake:.classDebugEnabled.959
- _logEventPointWake:.defaultOnce.930
- _logEventPointWake:.defaultOnce.946
- _logEventPointWake:.defaultOnce.958
- _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.1056
- _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.987
- _logEventPointWakeDataFrame:withParams:toEntry:.classDebugEnabled.993
- _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.1055
- _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.986
- _logEventPointWakeDataFrame:withParams:toEntry:.defaultOnce.992
- _logEventPointWakeLink:withParams:toEntry:.classDebugEnabled.1101
- _logEventPointWakeLink:withParams:toEntry:.defaultOnce.1100
- _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1065
- _logEventPointWakePNO:withParams:toEntry:.classDebugEnabled.1074
- _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1064
- _logEventPointWakePNO:withParams:toEntry:.defaultOnce.1073
- _logMessage:withPayload:.classDebugEnabled.654
- _logMessage:withPayload:.defaultOnce.651
- _logMessage:withPayload:.defaultOnce.653
- _logProcessExit.defaultOnce.546
- _logProcessExit.defaultOnce.549
- _logProcessExit.objectForKey.547
- _logProcessExit.objectForKey.550
- _log_default
- _logger
- _mach_error_string
- _malloc
- _mapDeletedAppsWithEnergyEntries:.classDebugEnabled.1831
- _mapDeletedAppsWithEnergyEntries:.defaultOnce.1830
- _mapPluginsToAppsWithEnergyEntries:.classDebugEnabled.1840
- _mapPluginsToAppsWithEnergyEntries:.defaultOnce.1839
- _modelDisplayPowerFromIOMFB:.classDebugEnabled.2041
- _modelDisplayPowerFromIOMFB:.defaultOnce.2040
- _modelDynamicDisplayPower:.classDebugEnabled.1993
- _modelDynamicDisplayPower:.defaultOnce.1992
- _modelDynamicDisplayPowerFromAPL:.classDebugEnabled.2050
- _modelDynamicDisplayPowerFromAPL:.defaultOnce.2049
- _modelWiFiPower:.classDebugEnabled.2455
- _modelWiFiPower:.defaultOnce.2454
- _objc_msgSend$DTQueryResponse:
- _objc_msgSend$_batteryGaugeServiceDidBecomeActive
- _objc_msgSend$_batteryGaugeServiceDidBecomeInactive
- _objc_msgSend$_canCacheMetrics
- _objc_msgSend$_emitPowerSignpostWithMetric:value:
- _objc_msgSend$_emitPowerSignpostWithMetric:value:pid:
- _objc_msgSend$_parseDisplayAZLMetricsFromEntry:cacheMetrics:
- _objc_msgSend$_parseWifiPowerMetricsFromEntry:cacheMetrics:
- _objc_msgSend$_registerNotificationWithAgent:type:tableName:isProcessSpecific:canRequestWhileBatteryGaugeIsRunning:minRequestInterval:block:
- _objc_msgSend$_sendMetrics
- _objc_msgSend$_startMetricCollectionTimerWithInterval:block:
- _objc_msgSend$addEntryTypesToEnergyEntriesInBucket:withResponderService:
- _objc_msgSend$addObserverForName:object:queue:usingBlock:
- _objc_msgSend$applyDynamicNameTransformation:withResponderService:
- _objc_msgSend$applyStaticNameTransformation:withResponderService:
- _objc_msgSend$applyTransformationsForBuckets:
- _objc_msgSend$appsForBackgroundActivityInsight
- _objc_msgSend$appsForBackgroundActivityInsightFromApps:withThresholdAboveAverageBackgroundDrainPercentage:locationEnergyThreshold:inNDays:
- _objc_msgSend$averageBackgroundDrainThreshold
- _objc_msgSend$batteryGaugeConflictingProcessSpecificEntryKeys
- _objc_msgSend$batteryGaugeConflictingSystemMetricEntryKeys
- _objc_msgSend$bundleIDandPidMap
- _objc_msgSend$clearStateRoutine:
- _objc_msgSend$collectMetricsOnSnapshotWithError:
- _objc_msgSend$compileSnapshotResponse
- _objc_msgSend$computeDisplayCostWithAvgRed:withAvgGreen:withAvgBlue:
- _objc_msgSend$computeGPUCostWithGPUSec:
- _objc_msgSend$computeLocationCostWithWifiCost:withGpsCost:withCellCost:withSkyhookCost:
- _objc_msgSend$computeNetworkingCostWithWifiIn:withWifiOut:withCellIn:withCellOut:
- _objc_msgSend$constructSlowChargingIntervals:
- _objc_msgSend$convertRawUsageToScore:
- _objc_msgSend$criticalLevel
- _objc_msgSend$curQueryCount
- _objc_msgSend$curQueryTime
- _objc_msgSend$dailyBackgroundDrainThreshold
- _objc_msgSend$dataReceivedFrom:
- _objc_msgSend$daysToTrackActivityForBatteryBreakdown:
- _objc_msgSend$destinations
- _objc_msgSend$didRestore
- _objc_msgSend$didUpgradeInLast:
- _objc_msgSend$endWithError:
- _objc_msgSend$entryEventBackwardDefinitionVoicemailDuration
- _objc_msgSend$entryEventIntervalDefinitionAnimatedStickerScoring
- _objc_msgSend$entryEventIntervalDefinitionMomentsDeferredProcessing
- _objc_msgSend$entryEventIntervalDefinitionStaticStickerScoring
- _objc_msgSend$entryEventPointDefinitionPPMClientMetrics
- _objc_msgSend$entryEventPointDefinitionPPMDebug
- _objc_msgSend$entrykeyCallBackMapping
- _objc_msgSend$entrykeyCallBackOnceMapping
- _objc_msgSend$extractAndSetProcessIdentifierWithPayload:
- _objc_msgSend$extractAndTranslateProcessIdentifier:
- _objc_msgSend$filterEnergyEntriesByAppTypeFromBucket:
- _objc_msgSend$gasGagueConnection
- _objc_msgSend$gasGaugeConsecutiveEmptyEntriesCount
- _objc_msgSend$generateRangeFromConfiguration:
- _objc_msgSend$getAppUsageEventsInRange:
- _objc_msgSend$getBattUIEntriesWithKey:
- _objc_msgSend$getCurrState:
- _objc_msgSend$getPPMDebugData
- _objc_msgSend$handleStateChangeForSafeguards
- _objc_msgSend$hardwareModelSMC:
- _objc_msgSend$initResponseSemaphore
- _objc_msgSend$initWithGlitchTimeRatio:
- _objc_msgSend$initWithTime:
- _objc_msgSend$initWithWorkQueue:forEntryKey:withBlock:
- _objc_msgSend$isScanLoggingEnabled
- _objc_msgSend$isServiceActive:
- _objc_msgSend$listAllRunningPidsWithBuffer:withSizeOfBuffer:
- _objc_msgSend$locationEnergyDrainThreshold
- _objc_msgSend$logCoalitionObjectMemory:shouldLogBatteryTableCadence:
- _objc_msgSend$logEventBackwardVoicemailDuration:
- _objc_msgSend$logEventIntervalAnimatedStickerScoring:
- _objc_msgSend$logEventIntervalGroupActivities:
- _objc_msgSend$logEventIntervalMomentsDeferredProcessing:
- _objc_msgSend$logEventIntervalStaticStickerScoring:
- _objc_msgSend$logPPMDebug
- _objc_msgSend$markFileAsPurgeable:withUrgency:
- _objc_msgSend$matchingPidWithProcessName:withBundleID:
- _objc_msgSend$measurements
- _objc_msgSend$mockAppForBackgroundActivityInsight
- _objc_msgSend$objectsForSubKey:ofSubKeyType:
- _objc_msgSend$parseApplicationResults:
- _objc_msgSend$parseCoalitionResults:
- _objc_msgSend$parseDisplayResults:
- _objc_msgSend$parseLocationResults:
- _objc_msgSend$parseProcessMonitorResults:
- _objc_msgSend$parseProcessNetworkResults:
- _objc_msgSend$pauseRoutineWithPayload:
- _objc_msgSend$perAppUsageForBatteryBreakdown:withStart:withEnd:withThresholdAboveDailyBackgroundDrainPercentage:
- _objc_msgSend$predicateMatchingProcessTypeApplication
- _objc_msgSend$processAppUsageEventsEntries:inRange:withAppArray:
- _objc_msgSend$registerNotificationWithAgent:withType:withTableName:withCallBackType:withBlock:
- _objc_msgSend$replaceBundleIDsWithDisplayNamesForEnergyEntryInBucket:withResponderService:
- _objc_msgSend$reported
- _objc_msgSend$requestDataFrom:withType:
- _objc_msgSend$requestTime
- _objc_msgSend$resetExitTimer
- _objc_msgSend$responseSemaphore
- _objc_msgSend$responseTime
- _objc_msgSend$results
- _objc_msgSend$resumeRoutineWithPayload:
- _objc_msgSend$returnTime
- _objc_msgSend$scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:
- _objc_msgSend$scoringEntities
- _objc_msgSend$setAnimatedStickerScoringListener:
- _objc_msgSend$setAppsForBackgroundActivityInsight:
- _objc_msgSend$setCurQueryCount:
- _objc_msgSend$setCurQueryTime:
- _objc_msgSend$setGasGagueConnection:
- _objc_msgSend$setGasGaugeConsecutiveEmptyEntriesCount:
- _objc_msgSend$setGroupActivitiesXPCListener:
- _objc_msgSend$setLastActiveStartTimeAndLastSuspendTimeWithPid:withAppState:withCurrentTime:
- _objc_msgSend$setLastEntryForHelperd:
- _objc_msgSend$setMetricCollectionTimerUpdateInterval:
- _objc_msgSend$setMomentsDeferredProcessingListener:
- _objc_msgSend$setStaticStickerScoringListener:
- _objc_msgSend$setUpdateInterval:
- _objc_msgSend$setUpdateMode:
- _objc_msgSend$setVoicemailDurationListener:
- _objc_msgSend$setXpcResponderBatteryGaugeDT:
- _objc_msgSend$shouldCalculateDisplayCost
- _objc_msgSend$shouldShowInsightThroughOverrides
- _objc_msgSend$shouldShowOngoingRestoreInsight
- _objc_msgSend$signalServiceActive:
- _objc_msgSend$signalServiceInactive:
- _objc_msgSend$startRoutineWithPayload:
- _objc_msgSend$stopRoutineWithPayload:
- _objc_msgSend$supportsAccConnectionLogging
- _objc_msgSend$supportsFixedLimitCharging
- _objc_msgSend$supportsxFlags
- _objc_msgSend$surfaceNotificationForIssues:
- _objc_msgSend$translateProcessIdentifierWithInput:
- _objc_msgSend$triggerAllData
- _objc_msgSend$updateBrightnessMetrics
- _objc_msgSend$updateContextForIdentifier:withState:
- _objc_msgSend$updateDisplayState
- _objc_msgSend$updateInterval
- _objc_msgSend$updateMetrics:forPid:
- _objc_msgSend$updateMode
- _objc_msgSend$updatePluggedInState
- _objc_msgSend$updateWithMetricCollection:
- _objc_msgSend$ursaBootArgContent:
- _objc_msgSend$ursaNotificationContentWithIssue:
- _objc_msgSend$ursaNotificationRequestWithIssue:
- _objc_msgSend$ursaPowerExceptionContent:
- _objc_retain_x7
- _okToLoad
- _os_release
- _parseBatteryData
- _parseBatteryData.cold.1
- _parseBatteryData.cold.2
- _parseProcessMonitorResults:.classDebugEnabled
- _parseProcessMonitorResults:.defaultOnce
- _parseShutdownReason
- _parseThermalStateCallback:.cltmDefaults
- _parseThermalStateCallback:.onceToken
- _parseThermalStateCallback:.thermalStateToken
- _pmps_service
- _populateRootNodeEnergyKeysWithEnergyEntries:.classDebugEnabled.1624
- _populateRootNodeEnergyKeysWithEnergyEntries:.classDebugEnabled.1630
- _populateRootNodeEnergyKeysWithEnergyEntries:.defaultOnce.1623
- _populateRootNodeEnergyKeysWithEnergyEntries:.defaultOnce.1629
- _printf
- _productType._productType
- _productType.onceToken
- _pthread_attr_destroy
- _pthread_attr_init
- _pthread_attr_setdetachstate
- _pthread_create
- _pthread_setname_np
- _putchar
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1960
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1977
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.classDebugEnabled.1985
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1959
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1976
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1984
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.1993
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2034
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2044
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.defaultOnce.2047
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2035
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2045
- _qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:.objectForKey.2048
- _reaccountBackupRestore:.classDebugEnabled.593
- _reaccountBackupRestore:.defaultOnce.592
- _reaccountBackupRestoreWithEnergyEntries:.classDebugEnabled.1896
- _reaccountBackupRestoreWithEnergyEntries:.defaultOnce.1895
- _readBatteryData
- _readBlock
- _readChargeTable
- _readChargerData
- _readChargerData.chargerAlert
- _readChargerData.chargerRegs
- _readChargerData.chargerStatus
- _readChargerData.chargingCurrent
- _readChargerData.chargingVoltage
- _readChargerData.notChargingReason
- _readFAC__
- _readIMAXAndSOCSmoothData
- _readKeyViaOSAccum:toOutput:.classDebugEnabled.705
- _readKeyViaOSAccum:toOutput:.classDebugEnabled.711
- _readKeyViaOSAccum:toOutput:.defaultOnce.704
- _readKeyViaOSAccum:toOutput:.defaultOnce.710
- _readLifetimeData
- _readRaTableData
- _readRegister
- _readRemainingCapacity__
- _readShutdownReasonData
- _registerName
- _requestDataFrom:withType:.classDebugEnabled
- _requestDataFrom:withType:.defaultOnce
- _resetPermissionsForClients.classDebugEnabled.676
- _resetPermissionsForClients.defaultOnce.675
- _respondToEvent:withResponse:.classDebugEnabled.630
- _respondToEvent:withResponse:.classDebugEnabled.636
- _respondToEvent:withResponse:.defaultOnce.629
- _respondToEvent:withResponse:.defaultOnce.635
- _service
- _setUPOData
- _setUPOData.tmp
- _setupEALoggingTriggeredByConnectionEvent:.classDebugEnabled.3516
- _setupEALoggingTriggeredByConnectionEvent:.defaultOnce.3515
- _shouldLogAPL.onceToken
- _shouldLogAPL.result
- _shouldLogLuxStats.onceToken
- _shouldLogLuxStats.result
- _startUpdateThread
- _statsAndLogs
- _statsAndLogs.cold.1
- _statsAndLogs.cold.2
- _suggestionsWithEnergyEntries:.classDebugEnabled.1274
- _suggestionsWithEnergyEntries:.defaultOnce.1273
- _supportsAccConnectionLogging.onceToken
- _supportsAccConnectionLogging.ret
- _supportsFixedLimitCharging.onceToken
- _supportsFixedLimitCharging.supportsFixedCharge
- _supportsxFlags.__supportsBatteryModuleAuthentication
- _supportsxFlags.onceToken
- _swupdate_checkpoint
- _testGaugeServiceSingleInstance:.iteration
- _time
- _transformPlugins:withBucket:.classDebugEnabled.604
- _transformPlugins:withBucket:.defaultOnce.603
- _triggerAllData.triggered
- _uart_close_device
- _uart_open_device
- _updateThermalCoolDownState
- _updateThermalCoolDownState.cold.1
- _updateThread
- _updateThread.batteryInfo
- _updateThread.cold.1
- _updateThread.cold.10
- _updateThread.cold.2
- _updateThread.cold.3
- _updateThread.cold.4
- _updateThread.cold.5
- _updateThread.cold.6
- _updateThread.cold.7
- _updateThread.cold.8
- _updateThread.cold.9
- _updateThread.debug_break_failures
- _updateThread.oneTime
- _updateThread.updates
- _wifiManufacturerQuery.classDebugEnabled.2389
- _wifiManufacturerQuery.defaultOnce.2388
- _writeBatteryDiagnosticData
- _writeBlock
- _xFlags.classDebugEnabled.5228
- _xFlags.classDebugEnabled.5237
- _xFlags.classDebugEnabled.5246
- _xFlags.classDebugEnabled.5255
- _xFlags.classDebugEnabled.5261
- _xFlags.classDebugEnabled.5267
- _xFlags.classDebugEnabled.5273
- _xFlags.classDebugEnabled.5282
- _xFlags.classDebugEnabled.5288
- _xFlags.classDebugEnabled.5294
- _xFlags.defaultOnce.5227
- _xFlags.defaultOnce.5236
- _xFlags.defaultOnce.5245
- _xFlags.defaultOnce.5254
- _xFlags.defaultOnce.5260
- _xFlags.defaultOnce.5266
- _xFlags.defaultOnce.5272
- _xFlags.defaultOnce.5281
- _xFlags.defaultOnce.5287
- _xFlags.defaultOnce.5293
CStrings:
+ "$percent"
+ "$time"
+ "%s pid %d"
+ "%s: "
+ "%s: Return gpu_total_time=%f"
+ "-[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap]"
+ "-[PLPowerMetricMonitorService _accountingMetrics]"
+ "-[PLPowerMetricMonitorService _getGPUTotalTime]"
+ "-[PLPowerMetricMonitorService _queryCumulativeNetworkBytes]"
+ "-[PLPowerMetricMonitorService _setupMetrics]"
+ "-[PLPowerMetricMonitorService addMonitoredProcessWithPID:error:]"
+ "-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke"
+ "-[PLPowerMetricMonitorService startMonitoring]_block_invoke"
+ "/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/BatteryUIResponseTypes/PLBatteryUIResponseTypeDrainComparisonSummary.m"
+ "1hz_bic_accum_c"
+ "1hz_bic_accum_count"
+ "1hz_flipbook_fr"
+ "1hz_flipbook_frame_count"
+ "1hz_frame_miss_"
+ "1hz_frame_miss_count"
+ ";"
+ "@\"PPSMetricCollection\"24@0:8d16"
+ "@\"SafeguardsManagingClient\""
+ "@24@0:8^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQQ}]}16"
+ "@24@0:8d16"
+ "@28@0:8i16i20i24"
+ "@32@0:8d16d24"
+ "@64@0:8{apfs_label_purgeable_request=QQQQQQ}16"
+ "AOD 1hz_bic_accum_c is equal to %@"
+ "AOD 1hz_flipbook_fr is equal to %@"
+ "AOD 1hz_frame_miss_ is equal to %@"
+ "APFS"
+ "Accumulated should not go backwards"
+ "ActiveClients"
+ "Adjusted wake time (monotonic): %@"
+ "AggregatedPushes"
+ "All clients disconnected"
+ "AppInfo"
+ "AssertedPresence"
+ "Attempted to convert negative seconds (%f) to mach time. Returning 0."
+ "Auto Lock Suggestion: 24h breakdown cache unavailable, retry with 15 days"
+ "Auto-Brightness is currently turned off. You can save battery by turning it on."
+ "Auto-Lock is currently turned off. You can save battery by turning it on."
+ "Awake"
+ "B40@0:8@16Q24@32"
+ "B72@0:8@16{apfs_label_purgeable_request=QQQQQQ}24"
+ "BBPoorEnergy"
+ "BackgrounTime"
+ "Calculated sleep duration: %.3f seconds"
+ "CanSystemSleep received."
+ "ChannelType"
+ "ClientID"
+ "CoSocPower"
+ "CoSocPowerTimer"
+ "Collecting initial cumulative network bytes"
+ "ComparisonDateIntervals"
+ "CoreLocation"
+ "CoreLocation GeofenceTrigger XPC with payload=%@"
+ "CoreLocation::GeofenceTrigger"
+ "CreatedChannel"
+ "Current State Changed: %{public}s"
+ "Current State Final: %{public}s"
+ "Current State Initialized: Awake"
+ "CurrentInterval"
+ "DISPEXT"
+ "Date"
+ "Debug: Call to fetch module parameters returned (null)."
+ "DeepLink"
+ "Drain"
+ "ECPM"
+ "ECPM_SRAM"
+ "ECPU"
+ "E_RX_IP_PACKET"
+ "Enable Auto-Brightness"
+ "Enable Auto-Lock"
+ "EnergyDifference"
+ "Error getting maxCapacityPercent: %@"
+ "Error: Call to fetch module parameters returned (null)."
+ "EventName"
+ "Failed to get %s: %d. Using current time as wake time."
+ "Failed to get kern.sleeptime: %d"
+ "Failed to mark file '%@' as purgeable with label: '%@' (error %d = '%s')"
+ "Failed to mark file at path as purgeable with retention duration of %f seconds: %@"
+ "Failed to open file handle for '%@' to apply purgeable status: '%@' (error %d = '%s')"
+ "Failed to register for system power notifications."
+ "Failed to subscribe to IOReport DCP display stats"
+ "GameController.gamecontrollerd"
+ "GeofenceTrigger"
+ "Have not gotten any new accumulation data, using instantaneous value"
+ "High display brightness consumes large amounts of energy. Consider reducing brightness to improve battery life."
+ "IDSMessage"
+ "IODeviceTree:/filesystems"
+ "Kernel sleep time (monotonic): %@"
+ "LocationMetrics GeofenceTrigger logging absolute time %d as logging timestamp %@"
+ "LocationMetrics GeofenceTrigger timestamp is missing, logging current time as timestamp"
+ "Logging RBS entry=%@"
+ "MM/dd HH:mm"
+ "Mach time calculation overflowed for %f seconds. Clamping to UINT64_MAX."
+ "Mach time calculation resulted in negative value (%f) for %f seconds. Returning 0."
+ "Mach time ratio is zero, cannot convert seconds (%f) to mach time. Returning 0."
+ "Marked file '%@' as purgeable with label: '%@'"
+ "Metric collection timed out after %.2f seconds requested %@ collected %@"
+ "MetricKitD"
+ "N/A"
+ "Negative sleep duration calculated (%.3f s). Sleep: %@, Wake: %@"
+ "No valid last sleep time found, cannot calculate duration."
+ "NodeID"
+ "Not invoking initOperatorDependancies"
+ "NumIncoming"
+ "NumOutgoing"
+ "PCPM"
+ "PCPM_SRAM"
+ "PCPU"
+ "PLAccountingOperator_Aggregate_RootNodeEnergy"
+ "PLBatteryAgent_Aggregate_UILevel"
+ "PLBatteryUIAppBreakdownSortOrderKey"
+ "PLBatteryUIComparisonType"
+ "PLBatteryUIDailyCoalescedBreakdown"
+ "PLBatteryUIDailyDynamicDayBreakdown"
+ "PLBatteryUIDailyFullDayBreakdown"
+ "PLBatteryUIDrainAverage"
+ "PLBatteryUIDrainDateInterval"
+ "PLBatteryUIGraphDays24hrs"
+ "PLBatteryUIInsightsAndSuggestionsSummary"
+ "PLBatteryUIIsAnomalous"
+ "PLBatteryUIPerAppBreakdownKey"
+ "PLBatteryUIPreviousDrain"
+ "PLBatteryUIQualifierDuration"
+ "PLBatteryUIQueryRangeWeekTapDynamicEndKey"
+ "PLBatteryUIResponseTypeDrainComparisonSummary"
+ "PLBatteryUIUsageSummaryKey"
+ "PLPushAgent:: Aggregate SentKeepAlive with aggregatePayload=%@"
+ "PPSFileUtilities"
+ "PR6b"
+ "PUUID"
+ "PolledForPresence"
+ "PosterName"
+ "PowerChangedCallback received with nil refcon!"
+ "PowerExceptionsDetection"
+ "PowerExceptionsDetection payload: %@"
+ "PowerExceptionsDetection updated payload: %@"
+ "ProvisionedPayload"
+ "PublishedStatus"
+ "QOSBackground"
+ "QOSUserInitiated"
+ "QOSUserInteractive"
+ "QOSUtility"
+ "RBSApplication"
+ "RBSStatetoPLState:state:"
+ "Received callback from PowerDataD: %@"
+ "Received power notification: %u"
+ "ReceivedPayload"
+ "Recent Usage"
+ "Recent Usage Insight: 10 day breakdown cache unavailable, retry with 15 days"
+ "Reduce Brightness"
+ "Reduce Brightness Suggestion: 24h breakdown cache unavailable, retry with 15 days"
+ "Responder Service: breakdown cachedLength was shorter than requestLength"
+ "Responder Service: coalescedBreakdown count: %d"
+ "Responder Service: coalescedBreakdown was nil"
+ "Responder Service: createCoalescedBreakdownWithResponse"
+ "Responder Service: no cached breakdown for %@"
+ "SELECT %@,SUM(%@/1000.0) AS %@ FROM %@ QE JOIN %@ N ON QE.NodeID = N.ID WHERE %@ = %d AND %@ LIKE \"%@\" AND QE.timestamp >= %f AND QE.timestamp <= %f AND timeInterval = 3600.0 GROUP BY %@"
+ "SELECT %@,SUM(%@/1000.0) AS %@ FROM %@ RNE JOIN %@ N ON RNE.NodeID = N.ID WHERE %@ LIKE \"%@\" AND RNE.timestamp >= %f AND RNE.timestamp <= %f  AND timeInterval = 3600.0 GROUP BY %@"
+ "SELECT (SUM(%@) - SUM(%@)) as %@, (SUM(%@) - SUM(%@)) as %@, %@ FROM %@ WHERE %@ LIKE \"%@\" AND timestamp >= %f AND timestamp <= %f  AND timeInterval = 3600.0 GROUP BY %@"
+ "SELECT SUM(Energy/1000.0) AS Energy,NodeID,RootNodeID FROM PLAccountingOperator_Aggregate_RootNodeEnergy WHERE timestamp >= %f AND timestamp <= %f AND timeInterval = 3600.0 GROUP BY NodeID ORDER BY Energy DESC LIMIT 30"
+ "SELECT SUM(Level) AS Level FROM PLBatteryAgent_Aggregate_UILevel WHERE timestamp >= %f AND timestamp <= %f"
+ "ScreenTimeAgent"
+ "Setting up sleep/wake monitoring."
+ "Sleep/wake monitoring already set up."
+ "Sleep/wake monitoring teardown complete."
+ "Sleeping"
+ "SlowChargerReason"
+ "Start Date:%@, End Date:%@, Accumulated Drain:%@"
+ "StatusKitAgent"
+ "StatusKitAgent AggregatedPushes callback: %@"
+ "StatusKitAgent AggregatedPushes converting eventName %@ to an enum"
+ "StatusKitAgent AggregatedPushes entryPayload:%@"
+ "StatusKitAgent AggregatedPushes eventName %@ does not fall in any enum"
+ "StatusKitAgent AggregatedPushes payload is empty!"
+ "StatusKitAgent AggregatedPushes pushes Dictionary is empty for event: %@"
+ "StatusKitAgent::AggregatedPushes"
+ "Stopping powerlogHelperd"
+ "Subscribed"
+ "Successfully registered for sleep/wake notifications."
+ "SummaryChart"
+ "SummaryComparisonType"
+ "SummaryDrainAverage"
+ "SummaryDrainToday"
+ "SummaryList"
+ "SystemHasPoweredOn received."
+ "SystemWillNotSleep received."
+ "SystemWillPowerOn received."
+ "SystemWillSleep received."
+ "T@\"NSArray\",&,V_buckets"
+ "T@\"NSArray\",&,V_insightSummaryResult"
+ "T@\"NSArray\",&,V_suggestionSummaryResult"
+ "T@\"NSDictionary\",&,V_bundleIDToDisplayNameMap"
+ "T@\"NSDictionary\",&,V_installedPluginToParentIDMap"
+ "T@\"NSDictionary\",&,V_nodeIDToNodeNameMap"
+ "T@\"NSMutableArray\",&,V_dailyChargingStateIntervalsDict"
+ "T@\"NSMutableArray\",&,V_dailyLastBattEntry"
+ "T@\"NSMutableArray\",&,V_resultArray"
+ "T@\"NSMutableDictionary\",&,N,V_screenState"
+ "T@\"NSNumber\",&,V_accumulatedDrainLevel"
+ "T@\"NSNumber\",&,V_averageDrainRate"
+ "T@\"NSNumber\",&,V_oneHzBicAccumCount"
+ "T@\"NSNumber\",&,V_oneHzFlipbookFrameCount"
+ "T@\"NSNumber\",&,V_oneHzFrameMissCount"
+ "T@\"PLEntry\",&,N,V_lastEntryForMetricd"
+ "T@\"PLIOKitOperatorComposition\",R,V_iokitCoSocPower"
+ "T@\"PLIOReportStats\",&,N,V_dcpDisplayStats"
+ "T@\"PLTimer\",&,V_CoSocPowerTimer"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_geoFenceTriggerListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_powerExceptionsDetectionXPCListener"
+ "T@\"PLXPCListenerOperatorComposition\",&,V_statusKitAgentAggregatedPushesListener"
+ "T@\"SafeguardsManagingClient\",&,V_safeguardsManagingClient"
+ "TB,N,V_receivedNetworkUpdate"
+ "TB,V_accountingEnabled"
+ "TB,V_excludeTimeOnCharger"
+ "TB,V_isDynamicEnd"
+ "TB,V_isReadyToMonitor"
+ "TB,V_shouldSnapInterval"
+ "TB,V_shouldUseMidnightQueryRange"
+ "TI,N,V_pmNotifier"
+ "TI,N,V_rootDomainConnect"
+ "TQ,N,V_cellularInBytes"
+ "TQ,N,V_cellularOutBytes"
+ "TQ,N,V_prevCumulativeCellularInBytes"
+ "TQ,N,V_prevCumulativeCellularOutBytes"
+ "TQ,N,V_prevCumulativeWiFiInBytes"
+ "TQ,N,V_prevCumulativeWiFiOutBytes"
+ "TQ,N,V_wifiInBytes"
+ "TQ,N,V_wifiOutBytes"
+ "TQ,V_QOSBackground"
+ "TQ,V_QOSUserInitiated"
+ "TQ,V_QOSUserInteractive"
+ "TQ,V_QOSUtility"
+ "TQ,V_lastSleepDuration"
+ "TQ,V_lastSleepTime"
+ "TQ,V_lastWakeTime"
+ "TVMx"
+ "T^{IONotificationPort=},N,V_systemPowerPortRef"
+ "Td,V_accumSystemLoad"
+ "Td,V_accumSystemLoadCount"
+ "Td,V_brightnessPercentage"
+ "Td,V_brightnessSum"
+ "Td,V_dynamicEndOffset"
+ "Td,V_gpuTotalTime"
+ "Td,V_prevGpuTotalTime"
+ "Td,V_totalCell"
+ "Td,V_totalWiFi"
+ "Tearing down sleep/wake monitoring."
+ "Text"
+ "Ti,N,V_networkCumulativeCount"
+ "Ti,V_comparisonType"
+ "TimeOfIssue"
+ "Title"
+ "TotalAppEnergy"
+ "TotalAppUsageTime"
+ "TotalPastAppEnergy"
+ "TotalPastAppUsageTime"
+ "Tq,V_currentPowerState"
+ "Ts,V_percentageOption"
+ "URLQueryAllowedCharacterSet"
+ "UTTypeIcon"
+ "UnassertedPresence"
+ "Unhandled power message type: %u."
+ "Unsubscribed"
+ "Updating total network bytes: total wifi %f total cell %f"
+ "Usage Summary: Absolute drain difference = %d%%, relative drain difference:%d%% "
+ "Usage Summary: Interval drain is *above* average, relative drain:%d, absolute drain: %d"
+ "Usage Summary: Interval drain is *below* average, relative drain:%d, absolute drain: %d"
+ "Usage Summary: Interval drain is *similar* to average, relative drain:%d, absolute drain: %d"
+ "Usage Summary: Interval is not anomalous, not enough average past drain to compare"
+ "Usage Summary: Interval is not anomalous, not enough information to compare"
+ "Usage Summary: No past intervals to compare"
+ "Usage Summary: Not enough past intervals to compare"
+ "Usage Summary: current accumulated drain: %f "
+ "Usage Summary: past average accumulated drain: %f "
+ "Visibility"
+ "WidgetStats Accounting: totalScreenOnTime=%f, identifierToWeight=%@"
+ "XPCMetrics::PowerExceptionsDetection"
+ "Your %@ has been used more than usual since upgrading iOS, which may affect battery life."
+ "_CoSocPowerTimer"
+ "_QOSBackground"
+ "_QOSUserInitiated"
+ "_QOSUserInteractive"
+ "_QOSUtility"
+ "_accountingEnabled"
+ "_accountingMetrics"
+ "_accumSystemLoad"
+ "_accumSystemLoadCount"
+ "_accumulatedDrainLevel"
+ "_averageDrainRate"
+ "_brightnessPercentage"
+ "_brightnessSum"
+ "_bundleIDToDisplayNameMap"
+ "_calculateAccumSystemLoad:"
+ "_calculateAndStoreSleepDuration"
+ "_cellularInBytes"
+ "_cellularOutBytes"
+ "_comparisonType"
+ "_currentPowerState"
+ "_dailyChargingStateIntervalsDict"
+ "_dailyLastBattEntry"
+ "_dcpDisplayStats"
+ "_debugStringForPurgeableLabel:"
+ "_dynamicEndOffset"
+ "_excludeTimeOnCharger"
+ "_geoFenceTriggerListener"
+ "_getGPUTotalTime"
+ "_gpuTotalTime"
+ "_handleDisplayLayoutUpdate:"
+ "_handlePowerNotification:argument:"
+ "_insightSummaryResult"
+ "_installedPluginToParentIDMap"
+ "_iokitCoSocPower"
+ "_isDynamicEnd"
+ "_isReadyToMonitor"
+ "_lastEntryForMetricd"
+ "_lastSleepDuration"
+ "_lastSleepTime"
+ "_lastWakeTime"
+ "_networkCumulativeCount"
+ "_nodeIDToNodeNameMap"
+ "_oneHzBicAccumCount"
+ "_oneHzFlipbookFrameCount"
+ "_oneHzFrameMissCount"
+ "_parseDisplayAZLMetricsFromEntry:"
+ "_parseWifiPowerMetricsFromEntry:"
+ "_percentageOption"
+ "_powerExceptionsDetectionXPCListener"
+ "_prevCumulativeCellularInBytes"
+ "_prevCumulativeCellularOutBytes"
+ "_prevCumulativeWiFiInBytes"
+ "_prevCumulativeWiFiOutBytes"
+ "_prevGpuTotalTime"
+ "_purgeableLabelWithUrgency:startDate:"
+ "_queryCumulativeNetworkBytes"
+ "_receivedNetworkUpdate"
+ "_registerNotificationWithAgent:type:tableName:isProcessSpecific:minRequestInterval:block:"
+ "_safeguardsManagingClient"
+ "_sampleGPUTime"
+ "_screenState"
+ "_setUpSleepWakeMonitoring"
+ "_setupMetrics"
+ "_shouldSnapInterval"
+ "_shouldUseMidnightQueryRange"
+ "_statusKitAgentAggregatedPushesListener"
+ "_suggestionSummaryResult"
+ "_supportsGPUCoalitions"
+ "_tearDownSleepWakeMonitoring"
+ "_totalCell"
+ "_totalWiFi"
+ "_wifiInBytes"
+ "_wifiOutBytes"
+ "accountingEnabled"
+ "accumSystemLoad"
+ "accumSystemLoadCount"
+ "accumulatedDrainLevel"
+ "addTotals:with:"
+ "adg set: %d"
+ "appending %@ for key %@"
+ "autoBrightnessSuggestion"
+ "autolockSuggestion"
+ "averageDrainRate"
+ "batteryCapacity"
+ "biomed"
+ "biomesyncd"
+ "brightnessPercent"
+ "brightnessPercentage"
+ "brightnessSum"
+ "bui_25"
+ "bundleIDToDisplayNameMap"
+ "carry"
+ "carry expGroup detected"
+ "cellIn"
+ "cellOut"
+ "cellularInBytes"
+ "cellularOutBytes"
+ "cellularPower"
+ "clear"
+ "collectMetrics called without start monitoring"
+ "collectMetrics dispatch_semaphore_signal"
+ "collectMetricsWithTimeout:"
+ "com.apple.PerfPowerServices"
+ "com.apple.PerfPowerServices.lastChargingValueNotification"
+ "com.apple.graphic-icon.auto-brightness"
+ "com.apple.graphic-icon.auto-lock"
+ "com.apple.graphic-icon.display"
+ "com.apple.graphic-icon.recent-usage"
+ "comparisonDateIntervalsWithTargetStartTime:withEndTime:"
+ "comparisonType"
+ "computeEmbeddingsForQuery"
+ "configurationForDefaultMainDisplayMonitor"
+ "convertPPSSKALogEventName:"
+ "corespeechd"
+ "cpu_hog"
+ "createAnomalousAppEntriesFrom:"
+ "createAppDataMapForComparisonDateIntervals:currentDateInterval:targetTopApps:"
+ "createCoalescedBreakdownWithResponse:"
+ "createPerAppBreakdown:"
+ "creating radar for %@"
+ "criticalBatteryLevel"
+ "currentPowerState"
+ "dailyChargingStateIntervalsDict"
+ "dailyLastBattEntry"
+ "dateFromnSecEpoch:"
+ "dcpDisplayStats"
+ "disableAccounting"
+ "duetexpertd"
+ "dynamicEndOffset"
+ "e-apfs"
+ "en0"
+ "enableAccounting"
+ "entryAggregateDefinitionSentKeepAlive"
+ "entryEventForwardDefinitionRBSApplication"
+ "entryEventPointDefinitionCoSocPower"
+ "error %@ while posting %@"
+ "error checking for internal key, %@"
+ "excludeTimeOnCharger"
+ "experimentGroup"
+ "flags=%llu, startTime=%llu"
+ "geoFenceTriggerListener"
+ "getBattUIEntriesWithKey:inRange:"
+ "getBatteryMaximumCapacityPercentWithError:"
+ "getBreakdownForLength:fromCachedLength:forBucketSize:"
+ "getChargingStateIntervalsDictWithRange:addToDailyArrays:"
+ "getDrainPerBucketIn:"
+ "getEnergyForAppWithBundleID:inDateInterval:"
+ "getEnergyForQualificationID:withAppWithBundleID:inDateInterval:"
+ "getInstalledPluginToParentIDMap"
+ "getMachTimeFromSeconds:"
+ "getParentBundleIDForBundleID:"
+ "getSecondsFromMachTime:"
+ "getUsageTimesForAppWithBundleID:inDateInterval:"
+ "glitchTimeRatio"
+ "gpuPower"
+ "gpuPower = %f, gpuTime = %f, gpuTotalTime = %f, approx_GPU_energy = %f"
+ "gpuTotalTime"
+ "handleUrsaNotificationRequest:"
+ "hasBatteryModuleAuth"
+ "hasFixedChargingLimit"
+ "hasInductiveCharging"
+ "hasInternalKey"
+ "hasInternalKey:"
+ "hasRearALS"
+ "i24@0:8^@16"
+ "iPad"
+ "iPhone"
+ "icloud.searchpartyd"
+ "idle_phys_footprint"
+ "idle_wired"
+ "initWithHitchTimeRatio:perceivedHitchTimeRatio:"
+ "initWithStartDate:endDate:accumulatedDrain:"
+ "initWithUUIDBytes:"
+ "initializeSafeguardsSystem: Failed to alloc/init _safeguardsManagingClient"
+ "initializeUrsaNotifications"
+ "insightSummary"
+ "insightSummaryResult"
+ "insightsAndSuggestionsSummaryKey"
+ "installedPluginToParentIDMap"
+ "internal key detected"
+ "internalKey"
+ "intervalSummaryItems:"
+ "invalid action: %@"
+ "invalid internal key: %{private}@ resulting in %lu components"
+ "invalid payload"
+ "invalid payload %@"
+ "invalidateScreenStateUpdates"
+ "iokitCoSocPower"
+ "isDateIntervalAnomalous:comparedTo:"
+ "isDynamicEnd"
+ "isEnabled"
+ "isPerfPowerMetricd"
+ "isPowerexceptionsd"
+ "isReadyToMonitor"
+ "isTestRackDevice:withExpGroup:internalKeyDetected:"
+ "isUsingAnOlderWifiChip"
+ "isVirtualDevice"
+ "kPLWiFiClassIsOneOf:"
+ "kPPSDebugLogRetentionDuration"
+ "knowledgeconstructiond"
+ "lastChargingSystemTimestamp"
+ "lastEntryForMetricd"
+ "lastSleepDuration"
+ "lastSleepTime"
+ "lastWakeTime"
+ "launch_instigating_process"
+ "launch_reason"
+ "livability"
+ "logAggregateSentKeepAlive:"
+ "logCoalitionObjectMemory:"
+ "logEventForwardRBSApplicationForBundleID:withPid:withState:withReasons:withVisibility:"
+ "logEventIntervalPowerExceptionsDetection:"
+ "logEventPointGeofenceTrigger:"
+ "logStatusKitAgentAggregatePushes:"
+ "machTimeFromSeconds:"
+ "markAsPurgeable:label:"
+ "markAsPurgeable:urgency:startDate:"
+ "messageNoDrain"
+ "messageWithDrain"
+ "metricNormalizer"
+ "middayFromMidnight:"
+ "networkCumulativeCount"
+ "noBatteryData"
+ "nodeIDToNodeNameMap"
+ "normalizeBucket:to:"
+ "normalizeForBucket:with:"
+ "oneHzBicAccumCount"
+ "oneHzFlipbookFrameCount"
+ "oneHzFrameMissCount"
+ "organizeStateIntervalsWithRange:lastBattUIEntry:chargingIntervalsDict:addToDailyArrays:"
+ "pUUIDForPid:"
+ "pdp_ip0"
+ "peEnergy"
+ "percentageOption"
+ "perfpowermetricd"
+ "pid: %d, name: %@, state: %@, prevState: %@ reasons: %@"
+ "possibleRequests"
+ "posted notification %@"
+ "posterName"
+ "powerExceptionsDetectionXPCListener"
+ "powerexceptionsd"
+ "predicatePowerLogProcesses"
+ "prepareBreakdown:withDrainSummaries:withFullDayBreakdown:withDynamicBreakdown:"
+ "prevCumulativeCellularInBytes"
+ "prevCumulativeCellularOutBytes"
+ "prevCumulativeWiFiInBytes"
+ "prevCumulativeWiFiOutBytes"
+ "prevGpuTotalTime"
+ "qualifierDuration"
+ "qualifierType"
+ "queryLastSleepTimeMCT"
+ "queryLastWakeTimeMCT"
+ "rangeKeyForLength:bucketSize:"
+ "receivedNetworkUpdate"
+ "recentUsageInsight"
+ "reduceBrightnessSuggestion"
+ "routined"
+ "safeguardsManagingClient"
+ "searchd"
+ "setAccountingEnabled:"
+ "setAccumSystemLoad:"
+ "setAccumSystemLoadCount:"
+ "setAccumulatedDrainLevel:"
+ "setAverageDrainRate:"
+ "setBrightnessPercentage:"
+ "setBrightnessSum:"
+ "setBundleIDToDisplayNameMap:"
+ "setCellularInBytes:"
+ "setCellularOutBytes:"
+ "setCoSocPowerTimer:"
+ "setComparisonType:"
+ "setCurrentPowerState:"
+ "setDailyChargingStateIntervalsDict:"
+ "setDailyLastBattEntry:"
+ "setDcpDisplayStats:"
+ "setDisplayEnergy:"
+ "setDynamicEndOffset:"
+ "setExcludeTimeOnCharger:"
+ "setGeoFenceTriggerListener:"
+ "setGpuTotalTime:"
+ "setInsightSummaryResult:"
+ "setInstalledPluginToParentIDMap:"
+ "setIsDynamicEnd:"
+ "setIsReadyToMonitor:"
+ "setLastEntryForMetricd:"
+ "setLastSleepDuration:"
+ "setLastSleepTime:"
+ "setLastWakeTime:"
+ "setLocationDesiredAccuracy:"
+ "setNetworkCumulativeCount:"
+ "setNetworkingPower:"
+ "setNodeIDToNodeNameMap:"
+ "setOneHzBicAccumCount:"
+ "setOneHzFlipbookFrameCount:"
+ "setOneHzFrameMissCount:"
+ "setPackageEnergy:"
+ "setPercentageOption:"
+ "setPowerExceptionsDetectionXPCListener:"
+ "setPrevCumulativeCellularInBytes:"
+ "setPrevCumulativeCellularOutBytes:"
+ "setPrevCumulativeWiFiInBytes:"
+ "setPrevCumulativeWiFiOutBytes:"
+ "setPrevGpuTotalTime:"
+ "setQOSBackground:"
+ "setQOSUserInitiated:"
+ "setQOSUserInteractive:"
+ "setQOSUtility:"
+ "setQosBackground:"
+ "setQosUserInitiated:"
+ "setQosUserInteractive:"
+ "setQosUtility:"
+ "setReceivedNetworkUpdate:"
+ "setSafeguardsManagingClient:"
+ "setScreenState:"
+ "setShouldSnapInterval:"
+ "setShouldUseMidnightQueryRange:"
+ "setStatusKitAgentAggregatedPushesListener:"
+ "setSuggestionSummaryResult:"
+ "setTotalCell:"
+ "setTotalWiFi:"
+ "setTransitionHandler:"
+ "setUpScreenStateUpdates"
+ "setWeightOnScreen:"
+ "setWifiInBytes:"
+ "setWifiOutBytes:"
+ "settings-navigation://com.apple.Settings.Accessibility/DISPLAY_AND_TEXT#AUTO_BRIGHTNESS"
+ "settings-navigation://com.apple.Settings.Battery"
+ "settings-navigation://com.apple.Settings.Display/AUTOLOCK"
+ "settings-navigation://com.apple.Settings.Display/BRIGHTNESS"
+ "settings-navigation://com.apple.Settings.General/SOFTWARE_UPDATE_LINK"
+ "shouldPopUpForPowerExceptionForProcess:"
+ "shouldPopUpForPowerExceptionWithFatalCount:withNonFatalCount:withMitigationsEnabled:"
+ "shouldSnapInterval"
+ "shouldUseMidnightQueryRange"
+ "signalActive"
+ "signalInactive"
+ "smc_redesign"
+ "snapIntervals:"
+ "sortedAppEnergyArrayFromAppDataMap:"
+ "spotlightknowledged"
+ "startOfDayForDate:"
+ "stateDidChange:state:prevState:"
+ "statusKitAgentAggregatedPushesListener"
+ "stringByAddingPercentEncodingWithAllowedCharacters:"
+ "suggestionSummary"
+ "suggestionSummaryResult"
+ "supportsEnhancedAPFS"
+ "targetDateIntervalWithBucketStartTime:withEndTime:"
+ "totalCell"
+ "totalWiFi"
+ "triggerLTSStats"
+ "ttr"
+ "update"
+ "ursaBaseContent"
+ "ursaBootargContent:"
+ "ursaRadarContent:"
+ "ursaTTRContent:"
+ "v28@0:8I16^v20"
+ "v32@0:8@\"NSArray\"16^@24"
+ "v32@0:8@16^@24"
+ "v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24"
+ "v36@0:8{_PLTimeIntervalRange=dd}16B32"
+ "v44@0:8@16i24i28@32B40"
+ "v52@0:8{_PLTimeIntervalRange=dd}16@32@40B48"
+ "v60@0:8#16@24@32B40d44@?52"
+ "wifi power %f cellular power %f totalCell %f totalWiFi %f, processCellular %f processWifi %f networkingPower %f"
+ "wifiIn"
+ "wifiInBytes"
+ "wifiOut"
+ "wifiOutBytes"
+ "yyyy.MM.dd_HH-mm-ss"
+ "zSLa"
+ "zSLc"
+ "{apfs_label_purgeable_request=QQQQQQ}32@0:8Q16@24"
- " %02x"
- "!!! %s/%d: Pid=%@, BundleID=%@, ProcessName=%@, response=%@"
- "!!! %s/%d: Pid=%d, BundleID=%@, ProcessName=%@, input=%@"
- "!!! %s/%d: applicationPid=%@, self.measurements=%@, applicationEntry=%@, keys=%@"
- "!!! %s/%d: bundleId=%@, bundleIDandPidMap=%@, userInfo=%@"
- "!!! %s/%d: bundleId=%@, locationDesiredAccuracy=%d, userInfo=%@"
- "!!! %s/%d: bundleId=%@, measurements=%@, userInfo=%@"
- "!!! %s/%d: displayEntry[@\"BundleName\"]=%@, measuerment=%@"
- "!!! %s/%d: empty bundleIDandPidMap! measurements=%@, userInfo=%@"
- "!!! %s/%d: gpuCost=%f"
- "!!! %s/%d: location start signal; bundleId=%@, measuerment=%@"
- "!!! %s/%d: location terminate signal; bundleId=%@, measuerment=%@"
- "!!! %s/%d: locationCost=%f"
- "!!! %s/%d: measurements=%@"
- "!!! %s/%d: no bundleID; userInfo=%@"
- "!!! %s/%d: no more process to track; signaling PLBatteryGaugeService becoming inactive!"
- "!!! %s/%d: no more process to track; signalling PLBatteryGaugeService becoming inactive!"
- "!!! %s/%d: payload=%@, response=%@"
- "!!! %s/%d: pid (%@) is tracked already; usageDict=%@"
- "!!! %s/%d: processMonitorEntry=%@"
- "!!! %s/%d: processNetworkEntry[@\"BundleName\"]=%@, measuerment=%@"
- "!!! %s/%d: rawUsage=%@"
- "!!! %s/%d: request entry:%@, requestTime=%@"
- "!!! %s/%d: requestDataFrom:%@"
- "!!! %s/%d: reset exit timer!"
- "!!! %s/%d: response=%@, payload=%@"
- "!!! %s/%d: return entry:%@, returnTime=%@"
- "!!! %s/%d: signalling PLBatteryGaugeService becoming inactive; usageDict=%@"
- "!!! %s/%d: signalling PLBatteryGaugeService is becoming inactive!"
- "!!! %s/%d: something wrong; cannot find valid process identifier; payload=%@"
- "!!! %s/%d: usageDict=%@"
- "!!! curApplicationState=%d"
- "!!! current ThermalState=%llu, induced ThermalState=%lld"
- "!!! displayEntry=%@, avgRed=%d, avgGreen=%d, avgBlue=%d"
- "!!! pid=%@ is not tracked"
- "!!! processNetworkEntry=%@, wifiIn=%d, wifiOut=%d, cellIn=%d, cellOut=%d, pid=%@"
- "!/\v"
- "%@ Ursa notifications"
- "%@-%i-%@"
- "%d: retry OpenProtector (%d)"
- "%s interval: %f"
- "%s mode: %ld interval: %f"
- "%s/%d: iteration = %d"
- "%s/%d: response timer fired!"
- "%s/%d: trigger response timer!"
- "%s: %s"
- "%s: No matching bundleID found; entry=%@"
- "%s: PLServiceTypeBatteryGaugeService active, returning"
- "%s:%d  Error Reading Shutdown reason"
- "%s:%d  updatesDone=%d POLLING THE BATTERY"
- "%s:%d  updatesDone=%d PUBLISHING BATTERY data"
- "%s:%d  updatesDone=%d READING FLAGS"
- "%s:%d  updatesDone=%d criticalValue=%d external_connected=%d UpSeconds=%llu batteryInfo.voltage=%d"
- "%s:%d  updatesDone=%d criticalValue=%d external_connected=%d UpSeconds=%llu cfd=%d cfd-voltage=%d batteryInfo.voltage=%d"
- "%s:%d  updatesDone=%d dictionary failed"
- "%s:%d  updatesDone=%d, fullUpdate=%d, bootFullUpdate=%d, forceFullUpdate=%d] "
- "%s:%d UpSeconds=%llu (cfd = %u) forcing critical to 0"
- "%s:%d break failed (%d)"
- "%s:%d break failed break_failures=%d (%d)"
- "%s:%d cannot create dictionary"
- "%s:%d cannot disable gauge interrupts (%d)"
- "%s:%d cannot dump stats and logs (%x)"
- "%s:%d cannot read data"
- "%s:%d cannot read upo data"
- "%s:%d cannot update thermal state"
- "%s:%d deadline expired at UpSeconds=%llu (cfd = %u)"
- "%s:%d invalid timestamp"
- "%s:%d updatesDone=%d UpSeconds=%llu voltage=%d (low)"
- "*** %s:%d updatesDone=%d last_update_ignored=%d now=%f deadline=%f *** "
- "*** %s:%d updatesDone=%d last_update_ignored=%d now=%f deadline=%f update_interval=%f *** "
- "*** %s:%d updatesDone=%d message.messageType=%#x  (ign) *** "
- "*** %s:%d updatesDone=%d message.messageType=%#x system_sleep=%d *** "
- "*** %s:%d updatesDone=%d same_adaptor=%d adaptor_type=%d external_connected=%d *** "
- "---------- App Background Usage Insight: Bucket %d -------------------"
- "---------- App Background Usage Insight: Current daily background drain threshold: %f%% -------------------"
- "---------- App Background Usage Insight: Current default battery capacity: %f -------------------"
- "---------- App Background Usage Insight: Current location energy drain threshold: %f%% -------------------"
- "---------- App Background Usage Insight: Current total average background drain threshold: %f%% -------------------"
- "---------- App Background Usage Insight: Tracking %u days of activity -------------------"
- "-[PLBatteryAgent gasGaugeOpenAndStartLogging]"
- "-[PLBatteryAgent gasGaugeRead]"
- "-[PLBatteryAgent handlePPMCallback]"
- "-[PLBatteryGaugeService DTQueryResponse:]"
- "-[PLBatteryGaugeService DTQueryResponse:]_block_invoke"
- "-[PLBatteryGaugeService clearStateRoutine:]"
- "-[PLBatteryGaugeService computeGPUCostWithGPUSec:]"
- "-[PLBatteryGaugeService computeLocationCostWithWifiCost:withGpsCost:withCellCost:withSkyhookCost:]"
- "-[PLBatteryGaugeService convertRawUsageToScore:]"
- "-[PLBatteryGaugeService dataReceivedFrom:]"
- "-[PLBatteryGaugeService extractAndSetProcessIdentifierWithPayload:]"
- "-[PLBatteryGaugeService extractAndTranslateProcessIdentifier:]"
- "-[PLBatteryGaugeService initOperatorDependancies]_block_invoke"
- "-[PLBatteryGaugeService parseApplicationResults:]"
- "-[PLBatteryGaugeService parseCoalitionResults:]"
- "-[PLBatteryGaugeService parseDisplayResults:]"
- "-[PLBatteryGaugeService parseLocationResults:]"
- "-[PLBatteryGaugeService parseProcessMonitorResults:]"
- "-[PLBatteryGaugeService parseProcessNetworkResults:]"
- "-[PLBatteryGaugeService registerNotificationWithAgent:withType:withTableName:withCallBackType:withBlock:]_block_invoke"
- "-[PLBatteryGaugeService requestDataFrom:withType:]"
- "-[PLBatteryGaugeService resetExitTimer]"
- "-[PLBatteryGaugeService selfExit:]"
- "-[PLBatteryGaugeService startRoutineWithPayload:]"
- "-[PLBatteryGaugeService stopRoutineWithPayload:]"
- "-[PLBatteryGaugeService testGaugeServiceSingleInstance:]"
- "-[PLBatteryGaugeService translateProcessIdentifierWithInput:]"
- "-[PLBatteryGaugeService triggerAllData]"
- "-[PLPowerMetricMonitorService _parseProcessMonitorMetricsFromEntry:]"
- "-[PLPowerMetricMonitorService changeUpdateInterval:]_block_invoke"
- "-[PLPowerMetricMonitorService collectMetricsOnSnapshotWithError:]_block_invoke"
- "-[PLPowerMetricMonitorService finishMonitoringAndSendMetrics]_block_invoke"
- "-[PLPowerMetricMonitorService startMonitoringWithConfigurationMode:updateInterval:]_block_invoke"
- "/Library/Caches/com.apple.xbs/Sources/AppleHDQGasGauge/AppleHDQGasGauge.c"
- "/Library/Caches/com.apple.xbs/Sources/PerfPowerServices_Operators/Operators/Services/PLBatteryGaugeService.m"
- "/dev/cu.gas-gauge"
- "======================= Adding energy to accounting, duration: %f"
- "======================= B244: Energy Drained %@"
- "======================= Device Battery - Adding: %f"
- "======================= Local Battery: Energy drained %@"
- "======================= Overall Energy Drained %@, Power %@"
- "@\"CSDaemon\""
- "@\"NSTimer\""
- "@\"PLDTCostElement\""
- "@\"PPSMetricCollection\"16@0:8"
- "@\"PPSMetricCollection\"24@0:8^@16"
- "@\"PPSMetricCollection\"32@0:8@\"NSArray\"16^@24"
- "@24@0:8^@16"
- "@24@0:8^{jetsam_snapshot=QQQ{memorystatus_kernel_stats=IIIIIIIIIIQQQQQQ[80c]}Q[0{jetsam_snapshot_entry=i[33c]iIIi[16C]QQQQQQQQQQQQQQQQQQQ{timeval64=qq}QQQIQ}]}16"
- "@32@0:8@16^@24"
- "@48@0:8@16Q24Q32Q40"
- "@48@0:8@16Q24d32Q40"
- "AP"
- "Added atvAbsMaxVoltageMV=%u to battery dict"
- "Already monitoring process"
- "AnimatedStickerScoring"
- "AnimatedStickerScoring callback %@"
- "App Background Usage Insight gathered %d app runtime entries..."
- "App Background Usage Insight: %@ has %f energy used per bucket(%f%%) and %f mwh location energy, has usage event in bucket: %@"
- "App Background Usage Insight: %@ has %f mwh total average energy used (estimated %u%%) and %f%% location energy used, has usage events: %d"
- "App Background Usage Insight: %@ has met the criteria!"
- "App Background Usage Insight: App usage Events for %@: audio: %d, carplay:%d, widgets:%d, notifications:%d"
- "App Background Usage Insight: Couldn't find 14 day breakdown"
- "App Background Usage Insight: Couldn't prepare buckets"
- "App Background Usage Insight: gathered %d appUsageEvents entries..."
- "App Background Usage: prepared %d buckets"
- "AppleDynamicATV"
- "AppleHDQGasGauge.c"
- "AppleRawBatteryFlags"
- "AppleRawExternalConnected"
- "Application parsing for PID %@: app state = %@"
- "Application_State"
- "Asked: %@"
- "Attempting to monitor multiple times"
- "B24@0:8d16"
- "B40@0:8@16@24Q32"
- "BUI_BACKGROUNDAPPUSAGE_SUGGESTION_SHOW"
- "BUI_BACKGROUND_ACTIVITY_AVERAGE_THRESHOLD"
- "BUI_BACKGROUND_ACTIVITY_DAILY_THRESHOLD"
- "BUI_BACKGROUND_ACTIVITY_DAYS"
- "BUI_BACKGROUND_LOCATION_ENERGY_THRESHOLD"
- "BUI_ONGOINGRESTORE_SUGGESTION_SHOW"
- "BUI_ONGOINGUPGRADE_SUGGESTION_SHOW"
- "BackgroundAppUsageTestApp"
- "BaselineSysCap"
- "Battery Life Issue Detected"
- "Battery_Power_W"
- "Battery_Temp_C"
- "Bdg"
- "CCA: GasGauge still calibrating now=%lu"
- "CCA: cannot disable DLOG (%#x)"
- "CCA: cannot read DLOG status (%#x)"
- "CCA: disabled DLOG updatesDone=%d ccaDeadline=%lu"
- "CCA: re-enable DLOG updatesDone=%d, now=%lu"
- "CCA: re-enable DLOG updatesDone=%u, now=%lu"
- "CCA: usermode cannot disable DLOG (%#x)"
- "CCA: wait for deadline now=%lu"
- "CPU_Cost"
- "CPU_Inst"
- "CPU_PInst"
- "CPU_Power_W"
- "CPU_Seconds"
- "Cannot create the lifetime dictionary"
- "Cannot find specified process:%@"
- "Car"
- "Cell_In"
- "Cell_Out"
- "Cellular_Power_W"
- "ChargeTable"
- "ChargerTimeout"
- "ChargerWatchdogTimeout"
- "Charging_Rate_mA"
- "Clearing state..."
- "Client%d"
- "Coalition parsing for PID %@: GPU cost = %@"
- "Coalition parsing for PID %@: current thermal state = %@, induced thermal state = %@"
- "Compiled snapshot response: %@"
- "Consecutive Empty Entries %d"
- "Constructed raw measurement dictionaries: %@, %@"
- "Cost %f"
- "Created UrsaNotificationRequest: %@"
- "Critical battery shutdown disabled"
- "CriticalBattery"
- "CriticalFlagDelay"
- "D6/BMDrlb8V3WSiqL8gL+w"
- "DC_Input_Power_W"
- "DEV"
- "DRAM_Power_W"
- "DT query payload received: %@"
- "DTQueryResponse:"
- "DebugPolling"
- "Device does not support GenerativeFunctionMetrics assetLoad logging"
- "Device does not support GenerativeFunctionMetrics mmExecuteRequest logging"
- "Device does not support GenerativeFunctionMetrics smartReplySession logging"
- "Device does not support GenerativeFunctionMetrics tgiExecuteRequest logging"
- "DeviceSupports80ChargeLimit"
- "Disk_Read"
- "Disk_Write"
- "Display parsing for PID %@: display cost = %@"
- "Display state has changed to: %@"
- "Display_APL"
- "Display_Power_W"
- "Energy_Cost"
- "Energy_Overhead"
- "Error in pushing notification %@"
- "FCFlag"
- "Failed to create notification request"
- "Failed to mark %@ purgeable - can't open error: %s"
- "Failed to mark %@ purgeable - flags 0x%llx returned %d (%s)"
- "Failed to mark files in directory %@ purgeable -- error when retrieving contents of directory: '%@'"
- "Failed to mark files in directory %@ purgeable -- path is not directory"
- "GPU_Cost"
- "GPU_Power_W"
- "GPU_Time"
- "GasGauge Open: already have a connection"
- "GasGauge Open: result=%@ gg_log_interval=%d gg_sleep_interval=%d gg_currentlog_start=%d"
- "GasGauge-updateThread"
- "Got callback for PLSoCAgent_EventPoint_LifetimeServoStats: %@"
- "GroupActivities"
- "GroupActivities payload: %@"
- "GroupActivities updated payload: %@"
- "HDR.Nits"
- "HWModelStr"
- "HardwarePlatform"
- "IMaxAndSocSmoothTable"
- "IOPMUBootBatteryHealthMetric"
- "IOPMUBootUPOState"
- "IORegistryEntrySetCFProperties(0x%x)"
- "Idx"
- "Induced_Thermal_State"
- "Initializing Battery Gauge Service..."
- "Initializing query responder"
- "IsOnDemand"
- "Issue missing notification message, issue: %@"
- "Issue missing radar, issue: %@"
- "Location parsing for PID %@: location cost = %@"
- "Location_Cost"
- "Logging logCoalitionObjectMemory stats for new EventBackward_Battery entry logged"
- "ManufactureDate"
- "Marked %@ purgeable with urgency: %llu"
- "Metric collection timed out after %.2f seconds"
- "MfgData"
- "ModeledSysCap"
- "MomentsDeferredProcessing"
- "MomentsDeferredProcessing callback %@"
- "NetSysCap"
- "No gas gauge update for this platform."
- "No issues available"
- "No payload available or key missing"
- "Not invoking initOperatorDependancies for powerlogHelperd"
- "OCVTakenFlag"
- "Ongoing Location"
- "OngoingRestoreInsight: Build count:%lu"
- "OngoingRestoreInsight: DeviceSetup entity in the breakdown"
- "OngoingRestoreInsight: Restore occured more than a week ago"
- "OngoingRestoreInsight: Seconds since last upgrade:%f, last upgrade timestamp:%f"
- "OngoingRestoreInsight: Should suggest:%d"
- "OngoingUpgradeInsight: Build count:%lu"
- "OngoingUpgradeInsight: DeviceSetup entity in the breakdown"
- "OngoingUpgradeInsight: Restore occured more than a week ago"
- "OngoingUpgradeInsight: Seconds since last upgrade:%f"
- "OngoingUpgradeInsight: Should suggest:%d"
- "Ongoing_Location"
- "Other_SoC_Power_W"
- "OverrideSysCap"
- "PLBatteryGaugeQuery"
- "PLBatteryGaugeService"
- "PLBatteryGaugeService became active; ending with error"
- "PLBatteryGaugeService became active; stopping querying conflicting agents"
- "PLBatteryGaugeService became inactive; mode is updateOnSnapshot so we should have already ended with error"
- "PLBatteryGaugeService became inactive; mode is updateOnStop so we should have already ended with error"
- "PLBatteryGaugeService became inactive; resuming querying conflicting agents"
- "PLBatteryUIInsightAverageDrainKey"
- "PLBatteryUIInsightBackgroundAppUsageAppKey"
- "PLBatteryUIInsightDailyDrainBoolKey"
- "PLBatteryUIResponseTypeBackgroundAppUsageInsight"
- "PLBatteryUIResponseTypeOngoingRestoreInsight"
- "PLBatteryUIResponseTypeOngoingUpgradeInsight"
- "PLConfigAgent_EventNone_Config"
- "PPMBatteryModel"
- "PPMClientMetrics"
- "PPMDebug"
- "PPMDebug logging at PPMEvent count %ld"
- "PPMVector"
- "PPSMetricMonitorMode is not PPSMetricMonitorModeUpdateOnSnapshot"
- "Pausing routine..."
- "Pb"
- "PluggedIn state has changed to: %d"
- "PoSMEnabled"
- "PoSMLowerThreshold"
- "PoSMUpperThreshold"
- "Pp"
- "PpmzzBVLpZVubmP0tCIymg"
- "ProactiveSysCap"
- "ProcessMonitor parsing for PID %@: CPU cost = %@"
- "ProcessNetwork parsing for PID %@: network cost = %@"
- "ProcessedAssetCount"
- "ProcessingType"
- "ProductType"
- "Ps"
- "Pushed notification"
- "Pwr"
- "R0"
- "R1"
- "R2"
- "R3"
- "RaTable"
- "Raw"
- "RearALSCapability"
- "Removing"
- "RequestedAssetCount"
- "Requesting source data..."
- "ResetEnabled"
- "Resetting the gasgauge connection"
- "RestricLogCounter"
- "Resuming routine..."
- "SELECT * FROM '%@' WHERE (timestamp>%f AND timestamp<%f AND timeInterval=%f AND (%@));"
- "SELECT DISTINCT Build FROM PLConfigAgent_EventNone_Config"
- "SOCBasedShutdown"
- "Service is busy (Xcode Energy Gauges is running)"
- "ShowUrsaNotification"
- "Skin_Temp_C"
- "Skipping %@ for marking as purgeable -- file is of type '%@' & doesn't not match given extension filter."
- "Specified process is not tracked:%@"
- "Starting routine..."
- "StaticStickerScoring"
- "StaticStickerScoring callback %@"
- "StickerScoringAssetCount"
- "Stopping routine..."
- "Surfacing"
- "System_Load_Power_W"
- "T@\"CSDaemon\",&,V_safeguardsDaemon"
- "T@\"NSDate\",&,V_curQueryTime"
- "T@\"NSDate\",&,V_lastQueryTime"
- "T@\"NSMutableArray\",&,V_appsForBackgroundActivityInsight"
- "T@\"NSMutableArray\",&,V_trackedProcesses"
- "T@\"NSMutableDictionary\",&,V_applicationResults"
- "T@\"NSMutableDictionary\",&,V_bundleIDandPidMap"
- "T@\"NSMutableDictionary\",&,V_entrykeyCallBackMapping"
- "T@\"NSMutableDictionary\",&,V_entrykeyCallBackOnceMapping"
- "T@\"NSMutableDictionary\",&,V_locationResults"
- "T@\"NSMutableDictionary\",&,V_measurements"
- "T@\"NSMutableDictionary\",&,V_processMonitorResults"
- "T@\"NSMutableDictionary\",&,V_processNetworkResults"
- "T@\"NSMutableDictionary\",&,V_reported"
- "T@\"NSMutableDictionary\",&,V_reportedApplication"
- "T@\"NSMutableDictionary\",&,V_reportedLocation"
- "T@\"NSMutableDictionary\",&,V_reportedProcessMonitor"
- "T@\"NSMutableDictionary\",&,V_reportedProcessNetwork"
- "T@\"NSMutableDictionary\",&,V_requestTime"
- "T@\"NSMutableDictionary\",&,V_responseTime"
- "T@\"NSMutableDictionary\",&,V_results"
- "T@\"NSMutableDictionary\",&,V_returnTime"
- "T@\"NSMutableSet\",&,N,V_batteryGaugeConflictingProcessSpecificEntryKeys"
- "T@\"NSMutableSet\",&,N,V_batteryGaugeConflictingSystemMetricEntryKeys"
- "T@\"NSSet\",R,V_scoringEntities"
- "T@\"NSTimer\",&,V_exitTimer"
- "T@\"NSTimer\",&,V_thermalStateTimer"
- "T@\"PLDTCostElement\",&,V_networkingCostElement"
- "T@\"PLEntry\",&,N,V_lastEntryForHelperd"
- "T@\"PLSemaphore\",&,V_responseSemaphore"
- "T@\"PLStateTrackingComposition\",&,V_stateTrackerForSafeguards"
- "T@\"PLXPCListenerOperatorComposition\",&,V_animatedStickerScoringListener"
- "T@\"PLXPCListenerOperatorComposition\",&,V_groupActivitiesXPCListener"
- "T@\"PLXPCListenerOperatorComposition\",&,V_momentsDeferredProcessingListener"
- "T@\"PLXPCListenerOperatorComposition\",&,V_staticStickerScoringListener"
- "T@\"PLXPCListenerOperatorComposition\",&,V_voicemailDurationListener"
- "T@\"PLXPCResponderOperatorComposition\",&,V_xpcResponderBatteryGaugeDT"
- "T@,&,V_costElement"
- "TB,V_isTestingRunning"
- "TStamp"
- "T^{ggcontext=},V_gasGagueConnection"
- "Td,N,V_updateInterval"
- "Td,V_startTime"
- "Td,V_stopTime"
- "Test App"
- "ThermalCoolDown"
- "Thermal_State"
- "Ti,V_curQueryCount"
- "Ti,V_lastQueryCount"
- "TimeRemaining"
- "Timed out while trying to collect metrics"
- "TotalDemandAdj"
- "TotalDemandRaw"
- "Tq,N,V_updateMode"
- "Unexpected call of finishMonitoringAndSendMetrics in mode %d"
- "UpdateSampleConfig"
- "Ursa notifications:%@ "
- "UrsaBootArg"
- "UrsaNotificationIssues"
- "UrsaNotifyBuildVersion"
- "UrsaPowerException"
- "UserMode"
- "Vgg"
- "VisualSearchAssetCount"
- "VoicemailDuration"
- "VoicemailDuration callback: %@"
- "WiFi_In"
- "WiFi_Out"
- "WiFi_Power_W"
- "WidgetStats Accounting: totalFramesRendered=%f, identifierToWeight=%@"
- "XPCMetrics::GroupActivities"
- "[Internal] "
- "^{ggcontext=}"
- "^{ggcontext=}16@0:8"
- "_animatedStickerScoringListener"
- "_applicationResults"
- "_appsForBackgroundActivityInsight"
- "_batteryGaugeConflictingProcessSpecificEntryKeys"
- "_batteryGaugeConflictingSystemMetricEntryKeys"
- "_batteryGaugeServiceDidBecomeActive"
- "_batteryGaugeServiceDidBecomeInactive"
- "_bundleIDandPidMap"
- "_canCacheMetrics"
- "_curQueryCount"
- "_curQueryTime"
- "_emitPowerSignpostWithMetric:value:"
- "_emitPowerSignpostWithMetric:value:pid:"
- "_entrykeyCallBackMapping"
- "_entrykeyCallBackOnceMapping"
- "_exitTimer"
- "_extractCurrentUsageMetrics"
- "_gasGagueConnection"
- "_groupActivitiesXPCListener"
- "_isTestingRunning"
- "_lastEntryForHelperd"
- "_locationResults"
- "_measurements"
- "_momentsDeferredProcessingListener"
- "_networkingCostElement"
- "_parseDisplayAZLMetricsFromEntry:cacheMetrics:"
- "_parseProcessMonitorMetricsFromEntry:"
- "_parseWifiPowerMetricsFromEntry:cacheMetrics:"
- "_processMonitorResults"
- "_processNetworkResults"
- "_registerNotificationWithAgent:type:tableName:isProcessSpecific:canRequestWhileBatteryGaugeIsRunning:minRequestInterval:block:"
- "_reported"
- "_reportedApplication"
- "_reportedLocation"
- "_reportedProcessMonitor"
- "_reportedProcessNetwork"
- "_requestTime"
- "_responseSemaphore"
- "_responseTime"
- "_results"
- "_returnTime"
- "_safeguardsDaemon"
- "_scoringEntities"
- "_sendMetrics"
- "_startTime"
- "_stateTrackerForSafeguards"
- "_staticStickerScoringListener"
- "_stopTime"
- "_thermalStateTimer"
- "_updateInterval"
- "_updateMode"
- "_voicemailDurationListener"
- "_xpcResponderBatteryGaugeDT"
- "addObserverForName:object:queue:usingBlock:"
- "animatedStickerScoringListener"
- "applicationResults"
- "applyTransformationsForBuckets:"
- "appsForBackgroundActivityInsight"
- "appsForBackgroundActivityInsightFromApps:withThresholdAboveAverageBackgroundDrainPercentage:locationEnergyThreshold:inNDays:"
- "atvAbsMaxVoltageMV"
- "atvBatteryCapacityMA"
- "averageBackgroundDrainThreshold"
- "avgRdcRatio"
- "baselineR0"
- "baselineR1"
- "baselineR2"
- "baselineR3"
- "battery"
- "batteryDataCount<=kNumBatteryDataUpdateKeys"
- "batteryGaugeConflictingProcessSpecificEntryKeys"
- "batteryGaugeConflictingSystemMetricEntryKeys"
- "batteryGaugeService"
- "bui_absolute"
- "built-in"
- "bundleIDandPidMap"
- "bundle_id"
- "cannot disable DLOG (%#x)"
- "cannot disable currentlog %#x"
- "cannot drain data log (%d)"
- "cannot drain the data log (%d)"
- "cannot enable current log (%d)"
- "cannot enable gauge interrupts (%d)"
- "cannot read average current (%d)"
- "cannot read battery data count=%d (err=%d)"
- "changeUpdateInterval:"
- "changed updateSampleConfig=%#x"
- "checkreset"
- "clearStateRoutine:"
- "coalitionEntry=%@"
- "collectMetricsOnDemand"
- "collectMetricsOnDemand called without start monitoring"
- "collectMetricsOnDemand dispatch_semaphore_signal"
- "collectMetricsOnDemand mode is not PPSMetricMonitorModeUpdateOnDemand"
- "collectMetricsOnSnapshot called without start monitoring"
- "collectMetricsOnSnapshot dispatch_semaphore_signal"
- "collectMetricsOnSnapshotWithError:"
- "com.apple.AppleHDQGasGauge"
- "com.apple.batteryui.deviceSetupInsightDuration"
- "com.apple.batteryui.insights.ongoingrestore"
- "com.apple.batteryui.insights.ongoingupgrade"
- "com.apple.batteryui.iosUpdateInsightDuration"
- "com.apple.gasgauge"
- "compileSnapshotResponse"
- "computeDisplayCostWithAvgRed:withAvgGreen:withAvgBlue:"
- "computeGPUCostWithGPUSec:"
- "computeLocationCostWithWifiCost:withGpsCost:withCellCost:withSkyhookCost:"
- "computeNetworkingCostWithWifiIn:withWifiOut:withCellIn:withCellOut:"
- "convertRawUsageToScore:"
- "cost=%f"
- "could not find %s service"
- "could not find hw.model: %s"
- "could not open service: %#x"
- "could not read gas gauge control status"
- "criticalLevel"
- "curQueryCount"
- "curQueryTime"
- "currentUpdateInterval"
- "currentUpdateMode"
- "dailyBackgroundDrainThreshold"
- "data log clients: %d"
- "data log entries: %u"
- "data log supported: %d"
- "dataReceivedFrom:"
- "daysToTrackActivityForBatteryBreakdown:"
- "debug"
- "debugLog"
- "destinations"
- "determinePoSMThreshold, changed:%d %d %d %d "
- "determinePoSMThreshold, cmp:%d>%u %d>%u %d>%u %d>%u"
- "determinePoSMThreshold, enabled:%d %d %d %d "
- "determinePoSMThreshold,minThreshold=%u threshold:%u %u %u %u"
- "determineVACVoltage, vacLevelCount=%d, vac95LevelCount=%d"
- "determineVACVoltage:: vac95BasedVoltageMV=%d absMaxVoltageMV=%d"
- "determineVACVoltage:: vacBasedVoltageMV=%d"
- "determineVACVoltage:: waiting for vbat(%d) < vac(%d)"
- "devBoardDevice"
- "devBoardDevice: returning %d"
- "didRestore"
- "didUpgradeInLast:"
- "disablePPMEventThreshold"
- "disabled passedCharge PCFF=%d err=%d"
- "disabling DLOG (num_clients=%i)"
- "dynATV: cannot write to charger startus (%d)"
- "endWithError:"
- "entryEventBackwardDefinitionVoicemailDuration"
- "entryEventIntervalDefinitionAnimatedStickerScoring"
- "entryEventIntervalDefinitionMomentsDeferredProcessing"
- "entryEventIntervalDefinitionStaticStickerScoring"
- "entryEventPointDefinitionPPMClientMetrics"
- "entryEventPointDefinitionPPMDebug"
- "entrykeyCallBackMapping"
- "entrykeyCallBackOnceMapping"
- "exitTimer"
- "extractAndSetProcessIdentifierWithPayload:"
- "extractAndTranslateProcessIdentifier:"
- "failure last_update_failed_counter=%d last_success at %g, supressing %d subsequent errors"
- "fasterMemoryPolling"
- "fatal"
- "finishMonitoringAndSendMetrics"
- "flags update only"
- "gas gauge charge table bad checksum: checksum %#x checksum byte %#x expecting %#x"
- "gas gauge charge table inconsistent: %d data entries, %d bytes"
- "gas gauge charge table invalid type: %#x"
- "gas gauge firmware 1.09: disabling critical battery shutdown"
- "gas gauge reset detected (flags %#x capacity %d/%dmAh voltage %dmV current %dmA)"
- "gas gauge: SWI line low, issuing reset"
- "gas gauge: cannot determine the state of SWI line"
- "gas gauge: cannot issue a reset"
- "gas gauge: critical flag delay %d"
- "gas gauge: debug_polling=%d"
- "gas gauge: log counter %d"
- "gas gauge: reset"
- "gas gauge: userModeEnabled=%d"
- "gasGagueConnection"
- "gasGagueConnection=%p"
- "gasgauge success after previous %gs failure"
- "gasgauge success after previous failure"
- "gasgauge: %llu updateThread critical(%d, 0x%x), uscfg=0x%x, dyn=%d cfd=%d cfd-voltage=%d, upos=%x"
- "gasgauge: SWI line low issuing reset"
- "gasgauge: SWI line low reset disabled, ignoring"
- "gasgauge: SWI line, cannot determine the state of line"
- "gasgauge: could not map data log: %s"
- "gasgauge: could not register for battery events err=%x"
- "gasgauge: could not register for power source events"
- "gasgauge: could not register for system power notifications"
- "gasgauge: listening for battery interrupts"
- "gasgauge: updateThread start"
- "gasgauge: updateThread terminated"
- "gathering data log updatesDone=%d num_clients=%d"
- "generateRangeFromConfiguration:"
- "getAppUsageEventsInRange:"
- "getBattUIEntriesWithKey:"
- "getCurrState:"
- "getDeviceSoC"
- "getObjectInMeasurementsWithPid:withCategory:withKey:"
- "getPPMDebugData"
- "ggctl_open_device"
- "groupActivitiesXPCListener"
- "handleStateChangeForSafeguards"
- "hardwareModel"
- "hardwareModel: HWModelStr = %@"
- "hardwareModel: returning %@"
- "hardwareModelSMC:"
- "hw.model"
- "iMaxAndSocSmoothTable"
- "initResponseSemaphore"
- "initWithGlitchTimeRatio:"
- "initWithWorkQueue:forEntryKey:withBlock:"
- "isServiceActive:"
- "isTestingRunning"
- "kHasUsageEvent"
- "kLocationEnergy"
- "kern.boottime"
- "lastEntryForHelperd"
- "listAllRunningPidsWithBuffer:withSizeOfBuffer:"
- "locationEnergyDrainThreshold"
- "locationResults"
- "logCoalitionObjectMemory:shouldLogBatteryTableCadence:"
- "logEventBackwardVoicemailDuration:"
- "logEventIntervalAnimatedStickerScoring:"
- "logEventIntervalGroupActivities:"
- "logEventIntervalMomentsDeferredProcessing:"
- "logEventIntervalProcessMonitorInterval"
- "logEventIntervalStaticStickerScoring:"
- "logPPMDebug"
- "logs=%p"
- "mPb"
- "mPp"
- "markFileAsPurgeable:withUrgency:"
- "markFilesAsPurgeable:withUrgency:"
- "markFilesInDirectoryAsPurgeable:ofType:withUrgency:"
- "mask real UPOState=%x FCC=%d RemCap=%d new FCC=%d new RemCap=%d"
- "matchingPidWithProcessName:withBundleID:"
- "measurements"
- "messageFatal"
- "messageWarn"
- "mockAppForBackgroundActivityInsight"
- "momentsDeferredProcessingListener"
- "networkingCostElement"
- "numReadings=%i"
- "numReadings=%i, logs=%p"
- "num_client<0, client error?"
- "objectsForSubKey:ofSubKeyType:"
- "ongoingUpgrade"
- "outputFlag"
- "parseApplicationResults:"
- "parseBatteryData"
- "parseCoalitionResults:"
- "parseDisplayResults:"
- "parseLocationResults:"
- "parseProcessMonitorResults:"
- "parseProcessNetworkResults:"
- "parseThermalStateCallback:"
- "pauseRoutineWithPayload:"
- "perAppUsageForBatteryBreakdown:withStart:withEnd:withThresholdAboveDailyBackgroundDrainPercentage:"
- "pid: %d, name: %@, state: %d, reasons: %@"
- "predicateMatchingProcessTypeApplication"
- "processAppUsageEventsEntries:inRange:withAppArray:"
- "processMonitorResults"
- "processNetworkResults"
- "productType"
- "pthread_create"
- "q24@0:8q16"
- "rate limited popup, not yet %f"
- "readShutdownReasonData"
- "registerNotificationWithAgent:withType:withTableName:withCallBackType:withBlock:"
- "reported"
- "reportedApplication"
- "reportedApplication=%@"
- "reportedLocation"
- "reportedProcessMonitor"
- "reportedProcessNetwork"
- "reqBdg"
- "requestDataFrom:withType:"
- "requestTime"
- "resetExitTimer"
- "response"
- "responseSemaphore"
- "responseTime"
- "results"
- "resumeRoutineWithPayload:"
- "returnTime"
- "return_value"
- "s7nuHoZIYNoOHCqT9iyZkQ"
- "safeguardsDaemon"
- "scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:"
- "scoringEntities"
- "selfExit:"
- "setAnimatedStickerScoringListener:"
- "setApplicationResults:"
- "setAppsForBackgroundActivityInsight:"
- "setBatteryGaugeConflictingProcessSpecificEntryKeys:"
- "setBatteryGaugeConflictingSystemMetricEntryKeys:"
- "setBundleIDandPidMap:"
- "setCurQueryCount:"
- "setCurQueryTime:"
- "setEntrykeyCallBackMapping:"
- "setEntrykeyCallBackOnceMapping:"
- "setExitTimer:"
- "setGasGagueConnection:"
- "setGroupActivitiesXPCListener:"
- "setIsTestingRunning:"
- "setLastActiveStartTimeAndLastSuspendTimeWithPid:withAppState:withCurrentTime:"
- "setLastEntryForHelperd:"
- "setLocationResults:"
- "setMeasurements:"
- "setMomentsDeferredProcessingListener:"
- "setNetworkingCostElement:"
- "setObjectInMeasurementsWithObject:withPid:withCategory:withKey:"
- "setProcessMonitorResults:"
- "setProcessNetworkResults:"
- "setReported:"
- "setReportedApplication:"
- "setReportedLocation:"
- "setReportedProcessMonitor:"
- "setReportedProcessNetwork:"
- "setRequestTime:"
- "setResponseSemaphore:"
- "setResponseTime:"
- "setResults:"
- "setReturnTime:"
- "setSafeguardsDaemon:"
- "setStartTime:"
- "setStateTrackerForSafeguards:"
- "setStaticStickerScoringListener:"
- "setStopTime:"
- "setThermalStateTimer:"
- "setUpdateInterval:"
- "setUpdateMode:"
- "setVoicemailDurationListener:"
- "setXpcResponderBatteryGaugeDT:"
- "shouldCalculateDisplayCost"
- "shouldShowInsightThroughOverrides"
- "showing restore in progress"
- "signalServiceActive:"
- "signalServiceInactive:"
- "startMonitoringWithConfigurationMode:updateInterval:"
- "startRoutineWithPayload:"
- "start_time"
- "stateTrackerForSafeguards"
- "staticStickerScoringListener"
- "statsAndLogs"
- "stopRoutineWithPayload:"
- "stopTime"
- "stop_time"
- "supportsAccConnectionLogging"
- "supportsFixedLimitCharging"
- "supportsxFlags"
- "surfaceNotificationForIssues:"
- "testGaugeService"
- "testGaugeServiceSingleInstance:"
- "thermalStateTimer"
- "tracked_processes"
- "translateProcessIdentifierWithInput:"
- "triggerAllData"
- "updateBrightnessMetrics"
- "updateContextForIdentifier:withState:"
- "updateDisplayState"
- "updateMetrics:forPid:"
- "updateMode"
- "updatePluggedInState"
- "updateThermalCoolDownState"
- "updateThread"
- "updateWithMetricCollection:"
- "ursaBootArgContent:"
- "ursaNotificationContentWithIssue:"
- "ursaNotificationRequestWithIssue:"
- "ursaPowerExceptionContent:"
- "usage_data"
- "v16@?0@\"NSNotification\"8"
- "v24@0:8^{ggcontext=}16"
- "v28@0:8^i16i24"
- "v32@0:8q16d24"
- "v52@0:8@16@24@32B40@?44"
- "v64@0:8#16@24@32B40B44d48@?56"
- "voicemailDurationListener"
- "xpcResponderBatteryGaugeDT"

```
