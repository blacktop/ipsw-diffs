## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1035.6.0.0.0
-  __TEXT.__text: 0xbf518
-  __TEXT.__auth_stubs: 0x1630
-  __TEXT.__objc_methlist: 0x11700
-  __TEXT.__const: 0x648
-  __TEXT.__cstring: 0x1ceb7
-  __TEXT.__oslogstring: 0x3e14
-  __TEXT.__gcc_except_tab: 0x1980
-  __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x2200
-  __TEXT.__objc_classname: 0x1407
-  __TEXT.__objc_methname: 0x32bc8
-  __TEXT.__objc_methtype: 0x3bb9
-  __TEXT.__objc_stubs: 0x18b00
-  __DATA_CONST.__got: 0xa60
-  __DATA_CONST.__const: 0x2300
-  __DATA_CONST.__objc_classlist: 0x530
+1041.19.2.0.0
+  __TEXT.__text: 0xd5698
+  __TEXT.__auth_stubs: 0x1730
+  __TEXT.__objc_methlist: 0x12188
+  __TEXT.__const: 0x6e8
+  __TEXT.__cstring: 0x1fe26
+  __TEXT.__oslogstring: 0x480a
+  __TEXT.__gcc_except_tab: 0x1990
+  __TEXT.__dlopen_cstrs: 0xf3
+  __TEXT.__ustring: 0x82
+  __TEXT.__unwind_info: 0x2f40
+  __TEXT.__objc_classname: 0x149e
+  __TEXT.__objc_methname: 0x34689
+  __TEXT.__objc_methtype: 0x3f90
+  __TEXT.__objc_stubs: 0x19e40
+  __DATA_CONST.__got: 0xaa8
+  __DATA_CONST.__const: 0x2378
+  __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9aa8
+  __DATA_CONST.__objc_selrefs: 0xa020
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x438
-  __DATA_CONST.__objc_arraydata: 0xae0
-  __AUTH_CONST.__auth_got: 0xb30
-  __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x19300
-  __AUTH_CONST.__objc_const: 0x217f0
-  __AUTH_CONST.__objc_intobj: 0x1848
-  __AUTH_CONST.__objc_arrayobj: 0x3a8
-  __AUTH_CONST.__objc_dictobj: 0x140
+  __DATA_CONST.__objc_superrefs: 0x480
+  __DATA_CONST.__objc_arraydata: 0xb50
+  __AUTH_CONST.__auth_got: 0xbb0
+  __AUTH_CONST.__const: 0x4e0
+  __AUTH_CONST.__cfstring: 0x1ad00
+  __AUTH_CONST.__objc_const: 0x229f0
+  __AUTH_CONST.__objc_intobj: 0x19e0
+  __AUTH_CONST.__objc_arrayobj: 0x3f0
+  __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x7a8
-  __DATA.__objc_ivar: 0x215c
-  __DATA.__data: 0x1bc0
-  __DATA.__bss: 0x2a
-  __DATA_DIRTY.__objc_data: 0x2c38
+  __DATA.__objc_ivar: 0x2268
+  __DATA.__data: 0x1c20
+  __DATA.__bss: 0x78
+  __DATA_DIRTY.__objc_data: 0x2e68
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x2c0
+  __DATA_DIRTY.__bss: 0x300
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4DE04112-419F-3FBC-A101-DC582BB51ADB
-  Functions: 6170
-  Symbols:   20139
-  CStrings:  16708
+  UUID: C7FD2622-55E4-349B-9AAE-3F6DA27FA00C
+  Functions: 6497
+  Symbols:   21220
+  CStrings:  17526
 
Symbols:
+ +[IoRegisterClient sharedInstance]
+ +[IoRegisterClient sharedInstance].cold.1
+ +[WiFiAirplaneLandingDetector clearPersistedState]
+ +[WiFiAirplaneLandingDetector defaultAltimeter]
+ +[WiFiAirplaneLandingDetector defaultAltimeter].cold.1
+ +[WiFiAirplaneLandingDetector defaultAltimeter].cold.2
+ +[WiFiAirplaneLandingDetector defaultAltimeter].cold.3
+ +[WiFiAirplaneLandingDetector defaultConfig]
+ +[WiFiAirplaneLandingDetector describeTime:]
+ +[WiFiAirplaneLandingDetector isDetectorActive]
+ +[WiFiScanMonitor sharedScanMonitor]
+ +[WiFiScanMonitor sharedScanMonitor].cold.1
+ +[WiFiUsageConfiguration getPlatformConfigFor:from:]
+ +[WiFiUsageConfiguration getPlatformConfigFor:from:].cold.1
+ +[WiFiUsagePlatformConfig initialize]
+ +[WiFiUsagePoorLinkSession describeWiFiUsageMonitor_tdCellularState:]
+ +[WiFiUsagePrivacyFilter canPerformActionWithDynamicBaseSampleRate:]
+ +[WiFiUsagePrivacyFilter scalingFactorForSamplingRate:]
+ -[IoRegisterClient .cxx_destruct]
+ -[IoRegisterClient _collectEntryInfo:propertyKeys:planeName:]
+ -[IoRegisterClient _collectEntryInfo:propertyKeys:planeName:].cold.1
+ -[IoRegisterClient _collectEntryInfo:propertyKeys:planeName:].cold.2
+ -[IoRegisterClient _collectEntryInfo:propertyKeys:planeName:].cold.3
+ -[IoRegisterClient _collectEntryInfo:propertyKeys:planeName:].cold.4
+ -[IoRegisterClient _isMatch:onClassNames:]
+ -[IoRegisterClient _isMatch:onKeys:planeName:results:]
+ -[IoRegisterClient _searchEntry:hasMatchedDepth:currentDepth:maxDepth:classNames:keys:planeName:results:]
+ -[IoRegisterClient _searchEntry:hasMatchedDepth:currentDepth:maxDepth:classNames:keys:planeName:results:].cold.1
+ -[IoRegisterClient description]
+ -[IoRegisterClient fetchEntriesForClasses:depth:keys:plane:error:]
+ -[IoRegisterClient init]
+ -[IoRegisterClient internalQueue]
+ -[IoRegisterClient setInternalQueue:]
+ -[WFLoggerFileWithTTL WFLog:privacy:cfStrMsg:]
+ -[WFLoggerFileWithTTL WFLog:privacy:message:valist:]
+ -[WFLoggerFileWithTTL checkForRotation]
+ -[WFLoggerFileWithTTL cleanupOldFiles]
+ -[WFLoggerFileWithTTL cleanupOldFiles].cold.1
+ -[WFLoggerFileWithTTL createLogDirectoryIfNeeded]
+ -[WFLoggerFileWithTTL createNewLogFile]
+ -[WFLoggerFileWithTTL createNewLogFile].cold.1
+ -[WFLoggerFileWithTTL createNewLogFile].cold.2
+ -[WFLoggerFileWithTTL createPurgeableClassCFile:]
+ -[WFLoggerFileWithTTL createPurgeableClassCFile:].cold.1
+ -[WFLoggerFileWithTTL createPurgeableClassCFile:].cold.2
+ -[WFLoggerFileWithTTL dealloc]
+ -[WFLoggerFileWithTTL getLogDirURL]
+ -[WFLoggerFileWithTTL getLogFileNamePrefix]
+ -[WFLoggerFileWithTTL getLogFilePath]
+ -[WFLoggerFileWithTTL getLogLevelEnable]
+ -[WFLoggerFileWithTTL getLogLevelPersist]
+ -[WFLoggerFileWithTTL getLogLifespanInDays]
+ -[WFLoggerFileWithTTL getLogPrivacy]
+ -[WFLoggerFileWithTTL getMaxFileSizeInMB]
+ -[WFLoggerFileWithTTL initWithDirectoryPath:dirPath:fileNamePrefix:runLoopRef:runLoopMode:dateFormatter:maxFileSizeInMB:ttlInHours:rotationIntervalInHours:dispatchQueue:]
+ -[WFLoggerFileWithTTL parseTimestampFromFilename:]
+ -[WFLoggerFileWithTTL rotateToNewFile]
+ -[WFLoggerFileWithTTL setLogLevelEnable:]
+ -[WFLoggerFileWithTTL setLogLevelPersist:]
+ -[WFLoggerFileWithTTL setLogLifespanInDays:]
+ -[WFLoggerFileWithTTL setLogPrivacy:]
+ -[WFLoggerFileWithTTL setMaxFileSizeInMB:]
+ -[WFLoggerFileWithTTL shouldRotateFile]
+ -[WFLoggerFileWithTTL softError]
+ -[WFLoggerFileWithTTL startWatchingLogFile]
+ -[WFLoggerFileWithTTL startWatchingLogFile].cold.1
+ -[WFLoggerFileWithTTL startWatchingLogFile].cold.2
+ -[WFLoggerFileWithTTL startWatchingLogFile].cold.3
+ -[WFLoggerFileWithTTL stopWatchingLogFile]
+ -[WFLoggerFileWithTTL writeToFile:cfStrMsg:]
+ -[WiFi3BarsNetwork setAccessPoints:]
+ -[WiFiAirplaneLandingDetector .cxx_destruct]
+ -[WiFiAirplaneLandingDetector airplaneModeDidChange:]
+ -[WiFiAirplaneLandingDetector altimeter]
+ -[WiFiAirplaneLandingDetector checkDetectionCriteria:]
+ -[WiFiAirplaneLandingDetector config]
+ -[WiFiAirplaneLandingDetector createSamplingTimer]
+ -[WiFiAirplaneLandingDetector currentModeName]
+ -[WiFiAirplaneLandingDetector currentSamplingInterval]
+ -[WiFiAirplaneLandingDetector dealloc]
+ -[WiFiAirplaneLandingDetector description]
+ -[WiFiAirplaneLandingDetector dispatchQueue]
+ -[WiFiAirplaneLandingDetector enterActiveFlightMode]
+ -[WiFiAirplaneLandingDetector enterInactiveMode]
+ -[WiFiAirplaneLandingDetector enterLayoverMode:]
+ -[WiFiAirplaneLandingDetector firstTimeExceededAirportRadius]
+ -[WiFiAirplaneLandingDetector gatherLandingDetectedLogs:]
+ -[WiFiAirplaneLandingDetector getAltitudeSample]
+ -[WiFiAirplaneLandingDetector inInactiveMode]
+ -[WiFiAirplaneLandingDetector inLayoverMode]
+ -[WiFiAirplaneLandingDetector initWithCompletion:]
+ -[WiFiAirplaneLandingDetector initWithCompletion:config:altimeter:]
+ -[WiFiAirplaneLandingDetector initWithCompletion:config:altimeter:].cold.1
+ -[WiFiAirplaneLandingDetector landingCallback]
+ -[WiFiAirplaneLandingDetector lastAltitude]
+ -[WiFiAirplaneLandingDetector lastSampleDate]
+ -[WiFiAirplaneLandingDetector layoverModeStartDate]
+ -[WiFiAirplaneLandingDetector maxAltitude]
+ -[WiFiAirplaneLandingDetector networkDidJoinWithDetails:]
+ -[WiFiAirplaneLandingDetector notifyExceededAirportRadius]
+ -[WiFiAirplaneLandingDetector persistState]
+ -[WiFiAirplaneLandingDetector processSample:]
+ -[WiFiAirplaneLandingDetector queue]
+ -[WiFiAirplaneLandingDetector resetExceededAirportRadius]
+ -[WiFiAirplaneLandingDetector retrieveAndClearState]
+ -[WiFiAirplaneLandingDetector samplingDescription]
+ -[WiFiAirplaneLandingDetector samplingTimer]
+ -[WiFiAirplaneLandingDetector setAltimeter:]
+ -[WiFiAirplaneLandingDetector setConfig:]
+ -[WiFiAirplaneLandingDetector setCurrentSamplingInterval:]
+ -[WiFiAirplaneLandingDetector setDispatchQueue:]
+ -[WiFiAirplaneLandingDetector setFirstTimeExceededAirportRadius:]
+ -[WiFiAirplaneLandingDetector setLandingCallback:]
+ -[WiFiAirplaneLandingDetector setLastAltitude:]
+ -[WiFiAirplaneLandingDetector setLastSampleDate:]
+ -[WiFiAirplaneLandingDetector setLayoverModeStartDate:]
+ -[WiFiAirplaneLandingDetector setMaxAltitude:]
+ -[WiFiAirplaneLandingDetector setQueue:]
+ -[WiFiAirplaneLandingDetector setSamplingTimer:]
+ -[WiFiAirplaneLandingDetector setSoftError:]
+ -[WiFiAirplaneLandingDetector setVerticalSpeedSamples:]
+ -[WiFiAirplaneLandingDetector setWaitingForFirstSampleAfterReboot:]
+ -[WiFiAirplaneLandingDetector softError]
+ -[WiFiAirplaneLandingDetector ttr:]
+ -[WiFiAirplaneLandingDetector updateConfig:]
+ -[WiFiAirplaneLandingDetector updateSpeedSamples:]
+ -[WiFiAirplaneLandingDetector updateTimerInterval:]
+ -[WiFiAirplaneLandingDetector verticalSpeedSamples]
+ -[WiFiAirplaneLandingDetector waitingForFirstSampleAfterReboot]
+ -[WiFiScanMonitor .cxx_destruct]
+ -[WiFiScanMonitor gatherScanStatisticsForClient:error:is2GScan:is2GScanScanCore:is5GScan:is5GScanScanCore:is6GScan:is6GScanScanCore:scanDuration2G:scanDuration5G:scanDuration6G:scanCore2GScanDuration:scanCore5GScanDuration:scanCore6GScanDuration:]
+ -[WiFiScanMonitor init]
+ -[WiFiScanMonitor scanAggregator]
+ -[WiFiScanMonitor setScanAggregator:]
+ -[WiFiScanStatistics add:with:]
+ -[WiFiScanStatistics aggregateValues:]
+ -[WiFiScanStatistics aggregateValues:].cold.1
+ -[WiFiScanStatistics client]
+ -[WiFiScanStatistics err]
+ -[WiFiScanStatistics failureCount]
+ -[WiFiScanStatistics gatherDataToBePosted:]
+ -[WiFiScanStatistics initForClient:]
+ -[WiFiScanStatistics is2GScanScanCore]
+ -[WiFiScanStatistics is2GScan]
+ -[WiFiScanStatistics is5GScanScanCore]
+ -[WiFiScanStatistics is5GScan]
+ -[WiFiScanStatistics is6GScanScanCore]
+ -[WiFiScanStatistics is6GScan]
+ -[WiFiScanStatistics postDailyScanMetricsToCA]
+ -[WiFiScanStatistics postIndividualScanMetricsToCA]
+ -[WiFiScanStatistics scanCore2GScanDuration]
+ -[WiFiScanStatistics scanCore5GScanDuration]
+ -[WiFiScanStatistics scanCore6GScanDuration]
+ -[WiFiScanStatistics scanCoreScanDurationAllBands]
+ -[WiFiScanStatistics scanDuration2G]
+ -[WiFiScanStatistics scanDuration5G]
+ -[WiFiScanStatistics scanDuration6G]
+ -[WiFiScanStatistics scanDurationAllBands]
+ -[WiFiScanStatistics setClient:]
+ -[WiFiScanStatistics setErr:]
+ -[WiFiScanStatistics setFailureCount:]
+ -[WiFiScanStatistics setIs2GScan:]
+ -[WiFiScanStatistics setIs2GScanScanCore:]
+ -[WiFiScanStatistics setIs5GScan:]
+ -[WiFiScanStatistics setIs5GScanScanCore:]
+ -[WiFiScanStatistics setIs6GScan:]
+ -[WiFiScanStatistics setIs6GScanScanCore:]
+ -[WiFiScanStatistics setScanCore2GScanDuration:]
+ -[WiFiScanStatistics setScanCore5GScanDuration:]
+ -[WiFiScanStatistics setScanCore6GScanDuration:]
+ -[WiFiScanStatistics setScanCoreScanDurationAllBands:]
+ -[WiFiScanStatistics setScanDuration2G:]
+ -[WiFiScanStatistics setScanDuration5G:]
+ -[WiFiScanStatistics setScanDuration6G:]
+ -[WiFiScanStatistics setScanDurationAllBands:]
+ -[WiFiScanStatistics setSuccessCount:]
+ -[WiFiScanStatistics successCount]
+ -[WiFiScanStatistics twoSigFig:]
+ -[WiFiScanStatisticsAggregator .cxx_destruct]
+ -[WiFiScanStatisticsAggregator aggregateClientMetrics:]
+ -[WiFiScanStatisticsAggregator aggregator]
+ -[WiFiScanStatisticsAggregator canSubmitToCA:]
+ -[WiFiScanStatisticsAggregator init]
+ -[WiFiScanStatisticsAggregator internalQueue]
+ -[WiFiScanStatisticsAggregator lastSubmissionTime]
+ -[WiFiScanStatisticsAggregator setAggregator:]
+ -[WiFiScanStatisticsAggregator setInternalQueue:]
+ -[WiFiScanStatisticsAggregator setLastSubmissionTime:]
+ -[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:]
+ -[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:].cold.1
+ -[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:].cold.2
+ -[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:].cold.3
+ -[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:keywords:displayReason:completionHandler:]
+ -[WiFiUsageMonitor appendUsbStatsToDict:].cold.1
+ -[WiFiUsageMonitor appendUsbStatsToDict:].cold.2
+ -[WiFiUsageMonitor findHighestNomSignFqMHz:]
+ -[WiFiUsageMonitor mapIORegistryEntryPathToCAFieldPort:]
+ -[WiFiUsageMonitor mapIORegistryEntryPathToCAFieldPort:].cold.1
+ -[WiFiUsageMonitor mapIORegistryEntryPathToCAFieldTransport:]
+ -[WiFiUsageMonitor setLinkEventWithIntegerReason:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:forInterface:]
+ -[WiFiUsageMonitor setSoftApState:]
+ -[WiFiUsageMonitor setTdLogic_cellularState:forInterface:]
+ -[WiFiUsageNetworkDetails isAirplane]
+ -[WiFiUsageNetworkDetails isAppleInternalNetwork]
+ -[WiFiUsageNetworkDetails setIsAirplane:]
+ -[WiFiUsageNetworkSession _isInternalDeviceAndAppleInternalNetwork]
+ -[WiFiUsagePlatformConfig .cxx_destruct]
+ -[WiFiUsagePlatformConfig config]
+ -[WiFiUsagePlatformConfig initWith:platform:key:]
+ -[WiFiUsagePlatformConfig platform]
+ -[WiFiUsagePlatformConfig setConfig:]
+ -[WiFiUsagePlatformConfig setPlatform:]
+ -[WiFiUsagePoorLinkSession captureCellularStateAtLinkDown]
+ -[WiFiUsagePoorLinkSession cellularStateAtLinkDown]
+ -[WiFiUsagePoorLinkSession isCellularStateAtLinkDownValid]
+ -[WiFiUsagePoorLinkSession isLastCellularStateValid]
+ -[WiFiUsagePoorLinkSession lastRoamCacheAt]
+ -[WiFiUsagePoorLinkSession lastRoamCacheMaxRssi2G]
+ -[WiFiUsagePoorLinkSession lastRoamCacheMaxRssi5G]
+ -[WiFiUsagePoorLinkSession lastRoamCacheMaxRssi6G]
+ -[WiFiUsagePoorLinkSession lastSuccessfulRoamAt]
+ -[WiFiUsagePoorLinkSession last_CellularState]
+ -[WiFiUsagePoorLinkSession roamCacheDidUpdate:]
+ -[WiFiUsagePoorLinkSession setCellularStateAtLinkDown:]
+ -[WiFiUsagePoorLinkSession setIsCellularStateAtLinkDownValid:]
+ -[WiFiUsagePoorLinkSession setIsLastCellularStateValid:]
+ -[WiFiUsagePoorLinkSession setLastRoamCacheAt:]
+ -[WiFiUsagePoorLinkSession setLastRoamCacheMaxRssi2G:]
+ -[WiFiUsagePoorLinkSession setLastRoamCacheMaxRssi5G:]
+ -[WiFiUsagePoorLinkSession setLastRoamCacheMaxRssi6G:]
+ -[WiFiUsagePoorLinkSession setLastSuccessfulRoamAt:]
+ -[WiFiUsagePoorLinkSession setLast_CellularState:]
+ -[WiFiUsagePoorLinkSession setTimeFromLastRoamCacheToSessionEnd:]
+ -[WiFiUsagePoorLinkSession setTimeFromLastRoamCacheToTDConfirmed:]
+ -[WiFiUsagePoorLinkSession setTimeFromLastSuccessfulRoamToSessionEnd:]
+ -[WiFiUsagePoorLinkSession setTimeFromLastSuccessfulRoamToTDConfirmed:]
+ -[WiFiUsagePoorLinkSession tdLogic_cellularState:]
+ -[WiFiUsagePoorLinkSession timeFromLastRoamCacheToSessionEnd]
+ -[WiFiUsagePoorLinkSession timeFromLastRoamCacheToTDConfirmed]
+ -[WiFiUsagePoorLinkSession timeFromLastSuccessfulRoamToSessionEnd]
+ -[WiFiUsagePoorLinkSession timeFromLastSuccessfulRoamToTDConfirmed]
+ -[WiFiUsagePrivacyFilterSamplingRate description]
+ -[WiFiUsagePrivacyFilterSamplingRate initWithValue:]
+ -[WiFiUsagePrivacyFilterSamplingRate samplingBase]
+ -[WiFiUsagePrivacyFilterSamplingRate samplingRate]
+ -[WiFiUsageSession softApStateDidChange:]
+ -[WiFiUsageSession tdLogic_cellularState:]
+ -[WiFiUsageSoftApSession dynamicPowerModeDurationSec]
+ -[WiFiUsageSoftApSession lowPowerModeDurationSec]
+ -[WiFiUsageSoftApSession setDynamicPowerModeDurationSec:]
+ -[WiFiUsageSoftApSession setLowPowerModeDurationSec:]
+ -[WiFiUsageSoftApSession softApStateDidChange:]
+ -[WiFiUsageSoftApStateInfo .cxx_destruct]
+ -[WiFiUsageSoftApStateInfo active]
+ -[WiFiUsageSoftApStateInfo changeReason]
+ -[WiFiUsageSoftApStateInfo channelNumber]
+ -[WiFiUsageSoftApStateInfo compatibilityMode]
+ -[WiFiUsageSoftApStateInfo countryCode]
+ -[WiFiUsageSoftApStateInfo description]
+ -[WiFiUsageSoftApStateInfo dynamicPowerModeDurationSec]
+ -[WiFiUsageSoftApStateInfo idleTimeAfterLastClientDisconnectedSec]
+ -[WiFiUsageSoftApStateInfo idleTimeBeforeTeardownSec]
+ -[WiFiUsageSoftApStateInfo init]
+ -[WiFiUsageSoftApStateInfo isAwdlUp]
+ -[WiFiUsageSoftApStateInfo isHidden]
+ -[WiFiUsageSoftApStateInfo isInfraConnected]
+ -[WiFiUsageSoftApStateInfo lowPowerModeDurationSec]
+ -[WiFiUsageSoftApStateInfo requestToUpLatency]
+ -[WiFiUsageSoftApStateInfo requester]
+ -[WiFiUsageSoftApStateInfo setActive:]
+ -[WiFiUsageSoftApStateInfo setChangeReason:]
+ -[WiFiUsageSoftApStateInfo setChannelNumber:]
+ -[WiFiUsageSoftApStateInfo setCompatibilityMode:]
+ -[WiFiUsageSoftApStateInfo setCountryCode:]
+ -[WiFiUsageSoftApStateInfo setDynamicPowerModeDurationSec:]
+ -[WiFiUsageSoftApStateInfo setIdleTimeAfterLastClientDisconnectedSec:]
+ -[WiFiUsageSoftApStateInfo setIdleTimeBeforeTeardownSec:]
+ -[WiFiUsageSoftApStateInfo setIsAwdlUp:]
+ -[WiFiUsageSoftApStateInfo setIsHidden:]
+ -[WiFiUsageSoftApStateInfo setIsInfraConnected:]
+ -[WiFiUsageSoftApStateInfo setLowPowerModeDurationSec:]
+ -[WiFiUsageSoftApStateInfo setRequestToUpLatency:]
+ -[WiFiUsageSoftApStateInfo setRequester:]
+ -[WiFiUsageSoftApStateInfo setStatus:]
+ -[WiFiUsageSoftApStateInfo status]
+ GCC_except_table21
+ GCC_except_table232
+ GCC_except_table26
+ GCC_except_table54
+ GCC_except_table93
+ _CFDateFormatterSetProperty
+ _CFRunLoopGetMain
+ _CFStringGetLength
+ _CFTimeZoneCreateWithName
+ _CoreMotionLibraryCore.frameworkLibrary
+ _IOIteratorNext
+ _IOObjectConformsTo
+ _IOObjectGetClass
+ _IOObjectRelease
+ _IORegistryEntryCreateCFProperty
+ _IORegistryEntryGetChildIterator
+ _IORegistryEntryGetNameInPlane
+ _IORegistryEntryGetPath
+ _IORegistryEntryGetRegistryEntryID
+ _IORegistryGetRootEntry
+ _NSFilePosixPermissions
+ _OBJC_CLASS_$_IoRegisterClient
+ _OBJC_CLASS_$_WFLoggerFileWithTTL
+ _OBJC_CLASS_$_WiFiAirplaneLandingDetector
+ _OBJC_CLASS_$_WiFiScanMonitor
+ _OBJC_CLASS_$_WiFiScanStatistics
+ _OBJC_CLASS_$_WiFiScanStatisticsAggregator
+ _OBJC_CLASS_$_WiFiUsageConfiguration
+ _OBJC_CLASS_$_WiFiUsagePlatformConfig
+ _OBJC_CLASS_$_WiFiUsagePrivacyFilterSamplingRate
+ _OBJC_CLASS_$_WiFiUsageSoftApStateInfo
+ _OBJC_IVAR_$_IoRegisterClient._internalQueue
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._cleanupAgeInSeconds
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._directoryURL
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._enabledLevel
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._eventSource
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._fileCreationDate
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._fileNamePrefix
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._filePtr
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._logFilePath
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._maxFileSizeInBytes
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._rotationIntervalInHours
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._softError
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._timestampFormatter
+ _OBJC_IVAR_$_WFLoggerFileWithTTL._ttlInHours
+ _OBJC_IVAR_$_WiFi3BarsNetwork._accessPoints
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._altimeter
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._config
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._currentSamplingInterval
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._dispatchQueue
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._firstTimeExceededAirportRadius
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._landingCallback
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._lastAltitude
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._lastSampleDate
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._layoverModeStartDate
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._maxAltitude
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._queue
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._samplingTimer
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._softError
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._verticalSpeedSamples
+ _OBJC_IVAR_$_WiFiAirplaneLandingDetector._waitingForFirstSampleAfterReboot
+ _OBJC_IVAR_$_WiFiScanMonitor._scanAggregator
+ _OBJC_IVAR_$_WiFiScanStatistics._client
+ _OBJC_IVAR_$_WiFiScanStatistics._err
+ _OBJC_IVAR_$_WiFiScanStatistics._failureCount
+ _OBJC_IVAR_$_WiFiScanStatistics._is2GScan
+ _OBJC_IVAR_$_WiFiScanStatistics._is2GScanScanCore
+ _OBJC_IVAR_$_WiFiScanStatistics._is5GScan
+ _OBJC_IVAR_$_WiFiScanStatistics._is5GScanScanCore
+ _OBJC_IVAR_$_WiFiScanStatistics._is6GScan
+ _OBJC_IVAR_$_WiFiScanStatistics._is6GScanScanCore
+ _OBJC_IVAR_$_WiFiScanStatistics._scanCore2GScanDuration
+ _OBJC_IVAR_$_WiFiScanStatistics._scanCore5GScanDuration
+ _OBJC_IVAR_$_WiFiScanStatistics._scanCore6GScanDuration
+ _OBJC_IVAR_$_WiFiScanStatistics._scanCoreScanDurationAllBands
+ _OBJC_IVAR_$_WiFiScanStatistics._scanDuration2G
+ _OBJC_IVAR_$_WiFiScanStatistics._scanDuration5G
+ _OBJC_IVAR_$_WiFiScanStatistics._scanDuration6G
+ _OBJC_IVAR_$_WiFiScanStatistics._scanDurationAllBands
+ _OBJC_IVAR_$_WiFiScanStatistics._successCount
+ _OBJC_IVAR_$_WiFiScanStatisticsAggregator._aggregator
+ _OBJC_IVAR_$_WiFiScanStatisticsAggregator._internalQueue
+ _OBJC_IVAR_$_WiFiScanStatisticsAggregator._lastSubmissionTime
+ _OBJC_IVAR_$_WiFiUsageNetworkDetails._isAirplane
+ _OBJC_IVAR_$_WiFiUsagePlatformConfig._config
+ _OBJC_IVAR_$_WiFiUsagePlatformConfig._platform
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._cellularStateAtLinkDown
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._isCellularStateAtLinkDownValid
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._isLastCellularStateValid
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._lastRoamCacheAt
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._lastRoamCacheMaxRssi2G
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._lastRoamCacheMaxRssi5G
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._lastRoamCacheMaxRssi6G
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._lastSuccessfulRoamAt
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._last_CellularState
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._timeFromLastRoamCacheToSessionEnd
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._timeFromLastRoamCacheToTDConfirmed
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._timeFromLastSuccessfulRoamToSessionEnd
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._timeFromLastSuccessfulRoamToTDConfirmed
+ _OBJC_IVAR_$_WiFiUsagePrivacyFilterSamplingRate._samplingBase
+ _OBJC_IVAR_$_WiFiUsagePrivacyFilterSamplingRate._samplingRate
+ _OBJC_IVAR_$_WiFiUsageSoftApSession._dynamicPowerModeDurationSec
+ _OBJC_IVAR_$_WiFiUsageSoftApSession._lowPowerModeDurationSec
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._active
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._changeReason
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._channelNumber
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._compatibilityMode
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._countryCode
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._dynamicPowerModeDurationSec
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._idleTimeAfterLastClientDisconnectedSec
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._idleTimeBeforeTeardownSec
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._isAwdlUp
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._isHidden
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._isInfraConnected
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._lowPowerModeDurationSec
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._requestToUpLatency
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._requester
+ _OBJC_IVAR_$_WiFiUsageSoftApStateInfo._status
+ _OBJC_METACLASS_$_IoRegisterClient
+ _OBJC_METACLASS_$_WFLoggerFileWithTTL
+ _OBJC_METACLASS_$_WiFiAirplaneLandingDetector
+ _OBJC_METACLASS_$_WiFiScanMonitor
+ _OBJC_METACLASS_$_WiFiScanStatistics
+ _OBJC_METACLASS_$_WiFiScanStatisticsAggregator
+ _OBJC_METACLASS_$_WiFiUsageConfiguration
+ _OBJC_METACLASS_$_WiFiUsagePlatformConfig
+ _OBJC_METACLASS_$_WiFiUsagePrivacyFilterSamplingRate
+ _OBJC_METACLASS_$_WiFiUsageSoftApStateInfo
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _TapToRadarKitLibrary
+ _TapToRadarKitLibraryCore
+ _TapToRadarKitLibraryCore.frameworkLibrary
+ _WFLoggerAirplaneWiFiDetectorFileHandle
+ _WFLoggerAirplaneWiFiDetectorFileHandle.cold.1
+ _WFLoggerAirplaneWiFiDetectorFileHandle.cold.2
+ _WFLoggerAirplaneWiFiDetectorFileHandle.log
+ _WFLoggerAirplaneWiFiDetectorFileHandle.onceToken
+ _WiFiPolicyLibraryCore.frameworkLibrary
+ __OBJC_$_CLASS_METHODS_IoRegisterClient
+ __OBJC_$_CLASS_METHODS_WiFiAirplaneLandingDetector
+ __OBJC_$_CLASS_METHODS_WiFiScanMonitor
+ __OBJC_$_CLASS_METHODS_WiFiUsageConfiguration
+ __OBJC_$_CLASS_METHODS_WiFiUsagePlatformConfig
+ __OBJC_$_INSTANCE_METHODS_IoRegisterClient
+ __OBJC_$_INSTANCE_METHODS_WFLoggerFileWithTTL
+ __OBJC_$_INSTANCE_METHODS_WiFiAirplaneLandingDetector
+ __OBJC_$_INSTANCE_METHODS_WiFiScanMonitor
+ __OBJC_$_INSTANCE_METHODS_WiFiScanStatistics
+ __OBJC_$_INSTANCE_METHODS_WiFiScanStatisticsAggregator
+ __OBJC_$_INSTANCE_METHODS_WiFiUsagePlatformConfig
+ __OBJC_$_INSTANCE_METHODS_WiFiUsagePrivacyFilterSamplingRate
+ __OBJC_$_INSTANCE_METHODS_WiFiUsageSoftApStateInfo
+ __OBJC_$_INSTANCE_VARIABLES_IoRegisterClient
+ __OBJC_$_INSTANCE_VARIABLES_WFLoggerFileWithTTL
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAirplaneLandingDetector
+ __OBJC_$_INSTANCE_VARIABLES_WiFiScanMonitor
+ __OBJC_$_INSTANCE_VARIABLES_WiFiScanStatistics
+ __OBJC_$_INSTANCE_VARIABLES_WiFiScanStatisticsAggregator
+ __OBJC_$_INSTANCE_VARIABLES_WiFiUsagePlatformConfig
+ __OBJC_$_INSTANCE_VARIABLES_WiFiUsagePrivacyFilterSamplingRate
+ __OBJC_$_INSTANCE_VARIABLES_WiFiUsageSoftApStateInfo
+ __OBJC_$_PROP_LIST_IoRegisterClient
+ __OBJC_$_PROP_LIST_WFLoggerFileWithTTL
+ __OBJC_$_PROP_LIST_WiFiAirplaneLandingDetector
+ __OBJC_$_PROP_LIST_WiFiScanMonitor
+ __OBJC_$_PROP_LIST_WiFiScanStatistics
+ __OBJC_$_PROP_LIST_WiFiScanStatisticsAggregator
+ __OBJC_$_PROP_LIST_WiFiUsageAccessPointProfileConfiguration
+ __OBJC_$_PROP_LIST_WiFiUsageBeaconParsingConfiguration
+ __OBJC_$_PROP_LIST_WiFiUsageLQMConfiguration
+ __OBJC_$_PROP_LIST_WiFiUsageLQMDistributionConfiguration
+ __OBJC_$_PROP_LIST_WiFiUsagePlatformConfig
+ __OBJC_$_PROP_LIST_WiFiUsagePrivacyFilterSamplingRate
+ __OBJC_$_PROP_LIST_WiFiUsageSoftApStateInfo
+ __OBJC_$_PROTOCOL_CLASS_METHODS_WiFiUsageConfiguration
+ __OBJC_$_PROTOCOL_METHOD_TYPES_WiFiUsageConfiguration
+ __OBJC_$_PROTOCOL_REFS_WiFiUsageConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_WiFiUsageAccessPointProfileConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_WiFiUsageBeaconParsingConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_WiFiUsageLQMConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_WiFiUsageLQMDistributionConfiguration
+ __OBJC_CLASS_RO_$_IoRegisterClient
+ __OBJC_CLASS_RO_$_WFLoggerFileWithTTL
+ __OBJC_CLASS_RO_$_WiFiAirplaneLandingDetector
+ __OBJC_CLASS_RO_$_WiFiScanMonitor
+ __OBJC_CLASS_RO_$_WiFiScanStatistics
+ __OBJC_CLASS_RO_$_WiFiScanStatisticsAggregator
+ __OBJC_CLASS_RO_$_WiFiUsageConfiguration
+ __OBJC_CLASS_RO_$_WiFiUsagePlatformConfig
+ __OBJC_CLASS_RO_$_WiFiUsagePrivacyFilterSamplingRate
+ __OBJC_CLASS_RO_$_WiFiUsageSoftApStateInfo
+ __OBJC_LABEL_PROTOCOL_$_WiFiUsageConfiguration
+ __OBJC_METACLASS_RO_$_IoRegisterClient
+ __OBJC_METACLASS_RO_$_WFLoggerFileWithTTL
+ __OBJC_METACLASS_RO_$_WiFiAirplaneLandingDetector
+ __OBJC_METACLASS_RO_$_WiFiScanMonitor
+ __OBJC_METACLASS_RO_$_WiFiScanStatistics
+ __OBJC_METACLASS_RO_$_WiFiScanStatisticsAggregator
+ __OBJC_METACLASS_RO_$_WiFiUsageConfiguration
+ __OBJC_METACLASS_RO_$_WiFiUsagePlatformConfig
+ __OBJC_METACLASS_RO_$_WiFiUsagePrivacyFilterSamplingRate
+ __OBJC_METACLASS_RO_$_WiFiUsageSoftApStateInfo
+ __OBJC_PROTOCOL_$_WiFiUsageConfiguration
+ __WFLoggerAirplaneWiFiDetectorGetFileLogger
+ __ZNSt12length_errorC1B9foe210106EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB9foe210106Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB9foe210106Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B9foe210106Ej
+ __ZNSt3__116__pad_and_outputB9foe210106IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocate_at_leastB9foe210106INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B9foe210106Ev
+ __ZNSt3__120__throw_length_errorB9foe210106EPKc
+ __ZNSt3__124__put_character_sequenceB9foe210106IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__tree_balance_after_insertB9foe210106IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__132__internal_log_hardening_failureEPKc
+ __ZNSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB9foe210106Ev
+ __ZSt28__throw_bad_array_new_lengthB9foe210106v
+ ___179-[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:]_block_invoke
+ ___179-[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:]_block_invoke_2
+ ___179-[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:]_block_invoke_2.cold.1
+ ___24-[WiFiUsageMonitor init]_block_invoke.296
+ ___24-[WiFiUsageMonitor init]_block_invoke.300
+ ___29-[WiFiSoftError submitMetric]_block_invoke.91
+ ___34+[IoRegisterClient sharedInstance]_block_invoke
+ ___35-[WiFiAirplaneLandingDetector ttr:]_block_invoke
+ ___35-[WiFiUsageMonitor setSoftApState:]_block_invoke
+ ___36+[WiFiScanMonitor sharedScanMonitor]_block_invoke
+ ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.783
+ ___38-[WiFiSoftError submitMetricWithData:]_block_invoke.94
+ ___40-[WiFiSoftError initWithName:andParams:]_block_invoke.45
+ ___40-[WiFiSoftError initWithName:andParams:]_block_invoke.60
+ ___43-[WFLoggerFileWithTTL startWatchingLogFile]_block_invoke
+ ___43-[WFLoggerFileWithTTL startWatchingLogFile]_block_invoke.176
+ ___46-[WiFiScanStatistics postDailyScanMetricsToCA]_block_invoke
+ ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.148
+ ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.148.cold.1
+ ___48-[WiFiAirplaneLandingDetector getAltitudeSample]_block_invoke
+ ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.116
+ ___50-[WiFiAirplaneLandingDetector createSamplingTimer]_block_invoke
+ ___51-[WiFiScanStatistics postIndividualScanMetricsToCA]_block_invoke
+ ___53-[WiFiAirplaneLandingDetector airplaneModeDidChange:]_block_invoke
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.169
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.169.cold.1
+ ___55-[WiFiScanStatisticsAggregator aggregateClientMetrics:]_block_invoke
+ ___55-[WiFiScanStatisticsAggregator aggregateClientMetrics:]_block_invoke.cold.1
+ ___57-[WiFiAirplaneLandingDetector networkDidJoinWithDetails:]_block_invoke
+ ___57-[WiFiAirplaneLandingDetector resetExceededAirportRadius]_block_invoke
+ ___58-[WiFiAirplaneLandingDetector notifyExceededAirportRadius]_block_invoke
+ ___58-[WiFiAirplaneLandingDetector notifyExceededAirportRadius]_block_invoke.cold.1
+ ___58-[WiFiUsageMonitor setTdLogic_cellularState:forInterface:]_block_invoke
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.369
+ ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.319
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.840
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.848
+ ___CoreMotionLibraryCore_block_invoke
+ ___TapToRadarKitLibraryCore_block_invoke
+ ___WFLoggerAirplaneWiFiDetectorFileHandle_block_invoke
+ ___WFLoggerAirplaneWiFiDetectorFileHandle_block_invoke_2
+ ___WiFiPolicyLibraryCore_block_invoke
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8
+ ___block_descriptor_112_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_40_e5_v8?0ls32l8
+ ___block_descriptor_40_e8_32r_e19_"NSDictionary"8?0lr32l8
+ ___block_descriptor_40_e8_32w_e44_v24?0"CMAbsoluteAltitudeData"8"NSError"16lw32l8
+ ___block_descriptor_64_e8_32s40s48s_e15_v32?0816^B24ls32l8s40l8s48l8
+ ___block_descriptor_70_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_literal_global.10
+ ___block_literal_global.125
+ ___block_literal_global.237
+ ___block_literal_global.283
+ ___block_literal_global.302
+ ___block_literal_global.350
+ ___block_literal_global.63
+ ___block_literal_global.843
+ ___block_literal_global.851
+ ___block_literal_global.853
+ ___block_literal_global.855
+ ___getCMAltimeterClass_block_invoke
+ ___getRadarComponentClass_block_invoke
+ ___getRadarDraftClass_block_invoke
+ ___getTapToRadarServiceClass_block_invoke
+ ___getWiFi3BarsNetworkClass_block_invoke
+ ___getWiFi3BarsNetworkClass_block_invoke.cold.1
+ __airplaneFileLogger
+ __airplaneFileOnceToken
+ __platformsKeys
+ _audit_stringCoreMotion
+ _audit_stringWiFiPolicy
+ _fsctl
+ _getCMAltimeterClass
+ _getCMAltimeterClass.softClass
+ _getRadarComponentClass.softClass
+ _getRadarDraftClass.softClass
+ _getTapToRadarServiceClass.softClass
+ _getWiFi3BarsNetworkClass.softClass
+ _getprogname
+ _kCFDateFormatterTimeZone
+ _kCFRunLoopDefaultMode
+ _kIOMainPortDefault
+ _objc_msgSend$_collectEntryInfo:propertyKeys:planeName:
+ _objc_msgSend$_isInternalDeviceAndAppleInternalNetwork
+ _objc_msgSend$_isMatch:onClassNames:
+ _objc_msgSend$_isMatch:onKeys:planeName:results:
+ _objc_msgSend$_searchEntry:hasMatchedDepth:currentDepth:maxDepth:classNames:keys:planeName:results:
+ _objc_msgSend$active
+ _objc_msgSend$add:with:
+ _objc_msgSend$aggregateClientMetrics:
+ _objc_msgSend$aggregateValues:
+ _objc_msgSend$aggregator
+ _objc_msgSend$altimeter
+ _objc_msgSend$authorizationStatus
+ _objc_msgSend$canPerformActionWithDynamicBaseSampleRate:
+ _objc_msgSend$canSubmitToCA:
+ _objc_msgSend$captureCellularStateAtLinkDown
+ _objc_msgSend$cellularStateAtLinkDown
+ _objc_msgSend$changeReason
+ _objc_msgSend$checkDetectionCriteria:
+ _objc_msgSend$checkForRotation
+ _objc_msgSend$cleanupOldFiles
+ _objc_msgSend$client
+ _objc_msgSend$compatibilityMode
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$countryCode
+ _objc_msgSend$createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:
+ _objc_msgSend$createBackgroundTapToRadarDraftWithTitle:description:keywords:displayReason:completionHandler:
+ _objc_msgSend$createDirectoryAtURL:withIntermediateDirectories:attributes:error:
+ _objc_msgSend$createDraft:forProcessNamed:withDisplayReason:completionHandler:
+ _objc_msgSend$createLogDirectoryIfNeeded
+ _objc_msgSend$createNewLogFile
+ _objc_msgSend$createPurgeableClassCFile:
+ _objc_msgSend$createSamplingTimer
+ _objc_msgSend$currentModeName
+ _objc_msgSend$currentSamplingInterval
+ _objc_msgSend$defaultAltimeter
+ _objc_msgSend$defaultConfig
+ _objc_msgSend$describeTime:
+ _objc_msgSend$dispatchQueue
+ _objc_msgSend$dynamicPowerModeDurationSec
+ _objc_msgSend$enterActiveFlightMode
+ _objc_msgSend$enterInactiveMode
+ _objc_msgSend$enterLayoverMode:
+ _objc_msgSend$err
+ _objc_msgSend$failureCount
+ _objc_msgSend$fetchEntriesForClasses:depth:keys:plane:error:
+ _objc_msgSend$findHighestNomSignFqMHz:
+ _objc_msgSend$firstTimeExceededAirportRadius
+ _objc_msgSend$gatherDataToBePosted:
+ _objc_msgSend$getAltitudeSample
+ _objc_msgSend$idleTimeAfterLastClientDisconnectedSec
+ _objc_msgSend$idleTimeBeforeTeardownSec
+ _objc_msgSend$inInactiveMode
+ _objc_msgSend$inLayoverMode
+ _objc_msgSend$initForClient:
+ _objc_msgSend$initWith:platform:key:
+ _objc_msgSend$initWithCompletion:config:altimeter:
+ _objc_msgSend$initWithDirectoryPath:dirPath:fileNamePrefix:runLoopRef:runLoopMode:dateFormatter:maxFileSizeInMB:ttlInHours:rotationIntervalInHours:dispatchQueue:
+ _objc_msgSend$initWithName:version:identifier:
+ _objc_msgSend$intersectsSet:
+ _objc_msgSend$is2GScan
+ _objc_msgSend$is2GScanScanCore
+ _objc_msgSend$is5GScan
+ _objc_msgSend$is5GScanScanCore
+ _objc_msgSend$is6GScan
+ _objc_msgSend$is6GScanScanCore
+ _objc_msgSend$isAbsoluteAltitudeAvailable
+ _objc_msgSend$isAirplane
+ _objc_msgSend$isAppleInternalNetwork
+ _objc_msgSend$isAwdlUp
+ _objc_msgSend$isCellularStateAtLinkDownValid
+ _objc_msgSend$isInfraConnected
+ _objc_msgSend$isWork
+ _objc_msgSend$joinReasonAsString:
+ _objc_msgSend$landingCallback
+ _objc_msgSend$lastAltitude
+ _objc_msgSend$lastSampleDate
+ _objc_msgSend$lastSubmissionTime
+ _objc_msgSend$last_CellularState
+ _objc_msgSend$layoverModeStartDate
+ _objc_msgSend$lowPowerModeDurationSec
+ _objc_msgSend$mapIORegistryEntryPathToCAFieldPort:
+ _objc_msgSend$mapIORegistryEntryPathToCAFieldTransport:
+ _objc_msgSend$maxAltitude
+ _objc_msgSend$parseTimestampFromFilename:
+ _objc_msgSend$persistState
+ _objc_msgSend$platform
+ _objc_msgSend$postDailyScanMetricsToCA
+ _objc_msgSend$postIndividualScanMetricsToCA
+ _objc_msgSend$processSample:
+ _objc_msgSend$rangeOfString:
+ _objc_msgSend$removePersistentDomainForName:
+ _objc_msgSend$requestToUpLatency
+ _objc_msgSend$requester
+ _objc_msgSend$retrieveAndClearState
+ _objc_msgSend$rotateToNewFile
+ _objc_msgSend$samplingDescription
+ _objc_msgSend$samplingTimer
+ _objc_msgSend$scalingFactorForSamplingRate:
+ _objc_msgSend$scanAggregator
+ _objc_msgSend$scanCore2GScanDuration
+ _objc_msgSend$scanCore5GScanDuration
+ _objc_msgSend$scanCore6GScanDuration
+ _objc_msgSend$scanCoreScanDurationAllBands
+ _objc_msgSend$scanDuration2G
+ _objc_msgSend$scanDuration5G
+ _objc_msgSend$scanDuration6G
+ _objc_msgSend$scanDurationAllBands
+ _objc_msgSend$setAggregator:
+ _objc_msgSend$setCellularStateAtLinkDown:
+ _objc_msgSend$setClassification:
+ _objc_msgSend$setClient:
+ _objc_msgSend$setComponent:
+ _objc_msgSend$setCurrentSamplingInterval:
+ _objc_msgSend$setDiagnosticExtensionIDs:
+ _objc_msgSend$setDynamicPowerModeDurationSec:
+ _objc_msgSend$setErr:
+ _objc_msgSend$setFailureCount:
+ _objc_msgSend$setFirstTimeExceededAirportRadius:
+ _objc_msgSend$setIs2GScan:
+ _objc_msgSend$setIs2GScanScanCore:
+ _objc_msgSend$setIs5GScan:
+ _objc_msgSend$setIs5GScanScanCore:
+ _objc_msgSend$setIs6GScan:
+ _objc_msgSend$setIs6GScanScanCore:
+ _objc_msgSend$setIsAirplane:
+ _objc_msgSend$setIsCellularStateAtLinkDownValid:
+ _objc_msgSend$setIsLastCellularStateValid:
+ _objc_msgSend$setIsUserInitiated:
+ _objc_msgSend$setKeywords:
+ _objc_msgSend$setLastAltitude:
+ _objc_msgSend$setLastRoamCacheAt:
+ _objc_msgSend$setLastRoamCacheMaxRssi2G:
+ _objc_msgSend$setLastRoamCacheMaxRssi5G:
+ _objc_msgSend$setLastRoamCacheMaxRssi6G:
+ _objc_msgSend$setLastSampleDate:
+ _objc_msgSend$setLastSubmissionTime:
+ _objc_msgSend$setLastSuccessfulRoamAt:
+ _objc_msgSend$setLast_CellularState:
+ _objc_msgSend$setLayoverModeStartDate:
+ _objc_msgSend$setLinkEvent:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:forInterface:
+ _objc_msgSend$setLowPowerModeDurationSec:
+ _objc_msgSend$setMaxAltitude:
+ _objc_msgSend$setMaxConcurrentOperationCount:
+ _objc_msgSend$setPersistentDomain:forName:
+ _objc_msgSend$setPlatform:
+ _objc_msgSend$setProblemDescription:
+ _objc_msgSend$setReproducibility:
+ _objc_msgSend$setSamplingTimer:
+ _objc_msgSend$setScanAggregator:
+ _objc_msgSend$setScanCore2GScanDuration:
+ _objc_msgSend$setScanCore5GScanDuration:
+ _objc_msgSend$setScanCore6GScanDuration:
+ _objc_msgSend$setScanCoreScanDurationAllBands:
+ _objc_msgSend$setScanDuration2G:
+ _objc_msgSend$setScanDuration5G:
+ _objc_msgSend$setScanDuration6G:
+ _objc_msgSend$setScanDurationAllBands:
+ _objc_msgSend$setSoftError:
+ _objc_msgSend$setSuccessCount:
+ _objc_msgSend$setTimeFromLastRoamCacheToSessionEnd:
+ _objc_msgSend$setTimeFromLastRoamCacheToTDConfirmed:
+ _objc_msgSend$setTimeFromLastSuccessfulRoamToSessionEnd:
+ _objc_msgSend$setTimeFromLastSuccessfulRoamToTDConfirmed:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$setUnderlyingQueue:
+ _objc_msgSend$setWaitingForFirstSampleAfterReboot:
+ _objc_msgSend$shared
+ _objc_msgSend$sharedWFLoggerSingleton
+ _objc_msgSend$shouldRotateFile
+ _objc_msgSend$softApStateDidChange:
+ _objc_msgSend$softError
+ _objc_msgSend$startAbsoluteAltitudeUpdatesToQueue:withHandler:
+ _objc_msgSend$stopAbsoluteAltitudeUpdates
+ _objc_msgSend$successCount
+ _objc_msgSend$tdLogic_cellularState:
+ _objc_msgSend$ttr:
+ _objc_msgSend$updateConfig:
+ _objc_msgSend$updateSpeedSamples:
+ _objc_msgSend$updateTimerInterval:
+ _objc_msgSend$verticalSpeedSamples
+ _objc_msgSend$waitingForFirstSampleAfterReboot
+ _os_parse_boot_arg_int
+ _pthread_threadid_np
+ _sharedScanMonitor.onceToken
+ _sharedScanMonitor.sharedMonitor
- +[WiFiUsageLQMConfiguration getConfigForPlatform]
- +[WiFiUsagePrivacyFilter scalingFactorForRawSampleRate:]
- -[WCAFetchBeaconDBParameters .cxx_destruct]
- -[WCAFetchBeaconDBParameters QBSS_Load]
- -[WCAFetchBeaconDBParameters UAPSD]
- -[WCAFetchBeaconDBParameters antennas11c]
- -[WCAFetchBeaconDBParameters antennas11n]
- -[WCAFetchBeaconDBParameters beaconInterval]
- -[WCAFetchBeaconDBParameters fetchWithCompletion:]
- -[WCAFetchBeaconDBParameters has_11krm]
- -[WCAFetchBeaconDBParameters max_rates]
- -[WCAFetchBeaconDBParameters setAntennas11c:]
- -[WCAFetchBeaconDBParameters setAntennas11n:]
- -[WCAFetchBeaconDBParameters setBeaconInterval:]
- -[WCAFetchBeaconDBParameters setHas_11krm:]
- -[WCAFetchBeaconDBParameters setMax_rates:]
- -[WCAFetchBeaconDBParameters setQBSS_Load:]
- -[WCAFetchBeaconDBParameters setUAPSD:]
- -[WCAFetchBeaconDBParameters setWlanAsel:]
- -[WCAFetchBeaconDBParameters setWlanFixedCapabilities:]
- -[WCAFetchBeaconDBParameters setWlanHTAmpduparam:]
- -[WCAFetchBeaconDBParameters setWlanHTCapabilities:]
- -[WCAFetchBeaconDBParameters setWlanHtexCapabilities:]
- -[WCAFetchBeaconDBParameters setWlanTimDtimPeriod:]
- -[WCAFetchBeaconDBParameters setWlanTxbf:]
- -[WCAFetchBeaconDBParameters setWlanVhtCapabilities:]
- -[WCAFetchBeaconDBParameters setWlanWfaIeWmeQosInfo:]
- -[WCAFetchBeaconDBParameters wlanAsel]
- -[WCAFetchBeaconDBParameters wlanFixedCapabilities]
- -[WCAFetchBeaconDBParameters wlanHTAmpduparam]
- -[WCAFetchBeaconDBParameters wlanHTCapabilities]
- -[WCAFetchBeaconDBParameters wlanHtexCapabilities]
- -[WCAFetchBeaconDBParameters wlanTimDtimPeriod]
- -[WCAFetchBeaconDBParameters wlanTxbf]
- -[WCAFetchBeaconDBParameters wlanVhtCapabilities]
- -[WCAFetchBeaconDBParameters wlanWfaIeWmeQosInfo]
- -[WCAFetchSQLiteBeaconDBRequest init]
- -[WiFi3BarsNetwork containsAccessPointMatchingBSSIDs:].cold.1
- -[WiFi3BarsNetwork network]
- -[WiFi3BarsNetwork setNetwork:]
- -[WiFiUsageLQMAnalysisSamplingRate description]
- -[WiFiUsageLQMAnalysisSamplingRate initWithValue:]
- -[WiFiUsageLQMAnalysisSamplingRate samplingBase]
- -[WiFiUsageLQMAnalysisSamplingRate samplingRate]
- -[WiFiUsageMonitor setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]
- -[WiFiUsageSession softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]
- -[WiFiUsageSoftApSession lowPowerModeDuration]
- -[WiFiUsageSoftApSession setLowPowerModeDuration:]
- -[WiFiUsageSoftApSession softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]
- GCC_except_table227
- GCC_except_table57
- GCC_except_table90
- _OBJC_CLASS_$_WCAFetchBeaconDBParameters
- _OBJC_CLASS_$_WCAFetchSQLiteBeaconDBRequest
- _OBJC_CLASS_$_WiFiUsageLQMAnalysisSamplingRate
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._QBSS_Load
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._UAPSD
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._antennas11c
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._antennas11n
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._beaconInterval
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._has_11krm
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._max_rates
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._wlanAsel
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._wlanFixedCapabilities
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._wlanHTAmpduparam
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._wlanHTCapabilities
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._wlanHtexCapabilities
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._wlanTimDtimPeriod
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._wlanTxbf
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._wlanVhtCapabilities
- _OBJC_IVAR_$_WCAFetchBeaconDBParameters._wlanWfaIeWmeQosInfo
- _OBJC_IVAR_$_WiFi3BarsNetwork._network
- _OBJC_IVAR_$_WiFiUsageLQMAnalysisSamplingRate._samplingBase
- _OBJC_IVAR_$_WiFiUsageLQMAnalysisSamplingRate._samplingRate
- _OBJC_IVAR_$_WiFiUsageSoftApSession._lowPowerModeDuration
- _OBJC_METACLASS_$_WCAFetchBeaconDBParameters
- _OBJC_METACLASS_$_WCAFetchSQLiteBeaconDBRequest
- _OBJC_METACLASS_$_WiFiUsageLQMAnalysisSamplingRate
- __OBJC_$_INSTANCE_METHODS_WCAFetchBeaconDBParameters
- __OBJC_$_INSTANCE_METHODS_WCAFetchSQLiteBeaconDBRequest
- __OBJC_$_INSTANCE_METHODS_WiFiUsageLQMAnalysisSamplingRate
- __OBJC_$_INSTANCE_VARIABLES_WCAFetchBeaconDBParameters
- __OBJC_$_INSTANCE_VARIABLES_WiFiUsageLQMAnalysisSamplingRate
- __OBJC_$_PROP_LIST_WCAFetchBeaconDBParameters
- __OBJC_$_PROP_LIST_WiFiUsageLQMAnalysisSamplingRate
- __OBJC_CLASS_RO_$_WCAFetchBeaconDBParameters
- __OBJC_CLASS_RO_$_WCAFetchSQLiteBeaconDBRequest
- __OBJC_CLASS_RO_$_WiFiUsageLQMAnalysisSamplingRate
- __OBJC_METACLASS_RO_$_WCAFetchBeaconDBParameters
- __OBJC_METACLASS_RO_$_WCAFetchSQLiteBeaconDBRequest
- __OBJC_METACLASS_RO_$_WiFiUsageLQMAnalysisSamplingRate
- __ZNSt12length_errorC1B8ne200100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
- __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100Ej
- __ZNSt3__116__pad_and_outputB8ne200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
- __ZNSt3__120__throw_length_errorB8ne200100EPKc
- __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
- __ZSt28__throw_bad_array_new_lengthB8ne200100v
- ___24-[WiFiUsageMonitor init]_block_invoke.266
- ___24-[WiFiUsageMonitor init]_block_invoke.270
- ___249-[WiFiUsageMonitor setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]_block_invoke
- ___29-[WiFiSoftError submitMetric]_block_invoke.80
- ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.697
- ___38-[WiFiSoftError submitMetricWithData:]_block_invoke.83
- ___40-[WiFiSoftError initWithName:andParams:]_block_invoke.34
- ___40-[WiFiSoftError initWithName:andParams:]_block_invoke.49
- ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.137
- ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.137.cold.1
- ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.105
- ___50-[WCAFetchBeaconDBParameters fetchWithCompletion:]_block_invoke
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.158
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.158.cold.1
- ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.372
- ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.289
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.754
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.765
- ___block_descriptor_104_e8_32s40s_e5_v8?0ls32l8s40l8
- ___block_descriptor_117_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
- ___block_descriptor_74_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_descriptor_81_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- ___block_literal_global.114
- ___block_literal_global.20
- ___block_literal_global.207
- ___block_literal_global.253
- ___block_literal_global.272
- ___block_literal_global.52
- ___block_literal_global.757
- ___block_literal_global.768
- ___block_literal_global.770
- ___block_literal_global.772
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$QBSS_Load
- _objc_msgSend$UAPSD
- _objc_msgSend$accessPointCount
- _objc_msgSend$antennas11c
- _objc_msgSend$antennas11n
- _objc_msgSend$beaconInterval
- _objc_msgSend$beaconsDataAsset
- _objc_msgSend$getConfigForPlatform
- _objc_msgSend$has_11krm
- _objc_msgSend$max_rates
- _objc_msgSend$records
- _objc_msgSend$scalingFactorForRawSampleRate:
- _objc_msgSend$setColumnNames:
- _objc_msgSend$setLimit:
- _objc_msgSend$setLowPowerModeDuration:
- _objc_msgSend$setParameters:
- _objc_msgSend$setTableName:
- _objc_msgSend$softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:
- _objc_msgSend$wlanAsel
- _objc_msgSend$wlanFixedCapabilities
- _objc_msgSend$wlanHTAmpduparam
- _objc_msgSend$wlanHTCapabilities
- _objc_msgSend$wlanHtexCapabilities
- _objc_msgSend$wlanTimDtimPeriod
- _objc_msgSend$wlanTxbf
- _objc_msgSend$wlanVhtCapabilities
- _objc_msgSend$wlanWfaIeWmeQosInfo
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
CStrings:
+ "%.0f"
+ "%.0f %@"
+ "%.0fs ago"
+ "%@-"
+ "%@-%@.log"
+ "%@_%@_highestNomSignFqMHz"
+ "%s - %@"
+ "%s - %lu vertical speed samples"
+ "%s - Absolute altitude is not available"
+ "%s - Airplane landing detected"
+ "%s - Airplane mode enabled while in %@ - triggering immediate altitude sample"
+ "%s - Altitude increased %.2f m, calling resetForNewFlight"
+ "%s - Away from airport and in inactive mode for %@ (less than %@) - waiting"
+ "%s - Away from airport and in inactive mode for over %@ - requesting deallocation"
+ "%s - Cleared persisted state"
+ "%s - CoreMotion framework not available"
+ "%s - Created background TTR draft with notification for airplane WiFi detection"
+ "%s - Detection check - samples above threshold: %lu/%lu >= %lu (%@), max altitude: %.2f m"
+ "%s - Detector deallocating"
+ "%s - Detector initializing"
+ "%s - Detector reset to Active Flight Mode (cleared vertical speed samples, sampling interval: %@)"
+ "%s - Entering inactive mode (sampling interval: %@)"
+ "%s - In layover mode for %@ without flight, entering inactive mode"
+ "%s - Left airport"
+ "%s - Location near airport - Resetting persisted %@"
+ "%s - Network is %@ - requesting deallocation"
+ "%s - New max altitude: %.2f meters"
+ "%s - NominalSignalingFrequenciesHz is not a Set"
+ "%s - Not in inactive mode"
+ "%s - Received altitude sample: %.2f meters (mode: %@ - delta: %.2fm)"
+ "%s - Recovered persisted state: (max altitude: %.2f sampling interval: %@ layover start date: %@)"
+ "%s - Restored into active mode. First sample after reboot: current altitude %.2f m < %.2f m - won't be able to detect landing, requesting deallocation"
+ "%s - Sampling timer fired"
+ "%s - Transitioned to Layover Mode (sampling interval: %@)"
+ "%s - Updating timer interval to %@"
+ "%s - Vertical speed: %.2f m/s (altitude Δ=%.2f m, time Δ=%.2f s)"
+ "%s - fetching filtered entries from IoRegistry failed with %@"
+ "%s CellularStateAtLinkDown - Invalid/Not Available"
+ "%s CellularStateAtLinkDown - WiFiPreferredOverCell: %d, CellularDataUsable: %d, WRMScore: %lu, WRMScoreConfidence: %lu, TimeSinceLastUpdate: %lu"
+ "%s Error: Response is not of type WCAFetchKeyValuesResponse, instead its %@"
+ "%s RoamInfo - LastRoam: %@ LastCache: %@ MaxRSSI[2G:%ld 5G:%ld 6G:%ld]"
+ "%s service %u matched class:%@"
+ "%s service %u matched key:%@"
+ "%s: %@ BEGIN, excludeFlag[%lld]"
+ "%s: CMAltimeter authorization %@"
+ "%s: Cleanup complete, deleted %lu old log files"
+ "%s: Created Class C protected log file: %@"
+ "%s: Created log directory %@"
+ "%s: Current log file deleted, rotating"
+ "%s: Deleted old log file: %@ (age: %.1fh)"
+ "%s: Device not yet unlocked since boot, file logging will be available after first unlock"
+ "%s: Error receiving altitude data: %@"
+ "%s: Failed to create TapToRadarKit draft with error: %@"
+ "%s: Failed to create directory %@: %@"
+ "%s: Failed to create file URL"
+ "%s: Failed to create log file after rotation attempt, file logging unavailable"
+ "%s: Failed to delete %@: %@"
+ "%s: Failed to list directory %@: %@"
+ "%s: Failed to mark %@ as purgeable with flags 0x%llx, supplemental 0x%llx, notBeforeDate:%@: (%d) %s"
+ "%s: Failed to parse timestamp from filename: %@"
+ "%s: File age (%.1fh) >= rotation interval (%luh), rotating"
+ "%s: File size (%llu bytes) > max (%lu bytes), rotating"
+ "%s: IOObjectGetClass failed with error: %d"
+ "%s: IORegistryEntryGetChildIterator failed with error: %d"
+ "%s: IORegistryEntryGetNameInPlane failed with error: %d"
+ "%s: IORegistryEntryGetPath failed with error: %d"
+ "%s: IORegistryEntryGetRegistryEntryID failed with error: %d"
+ "%s: Initialized with _enabledLevel = %lu (WFLogLevelDefault)"
+ "%s: Initializing with TTL=%luh, rotation=%luh, cleanup=%luh (always using Class C protection)"
+ "%s: Log file deletion detected, rotating..."
+ "%s: Marked %@ purgeable with flags 0x%llx (supplemental 0x%llx notBeforeDate:%@)"
+ "%s: Matched privacyExcludedKey: excluding[%u]: key['%{public}@']"
+ "%s: Persisted sampling interval invalid (%.2f), using layover interval as default"
+ "%s: Received LQMDistribution config from Mobile Assets: %@"
+ "%s: SoftError <%@> component Name and Version shall either either both be nil - WiFi (New Bugs) | iOS will be used, or both non nil"
+ "%s: SoftError <%@> created background TTR draft with notification"
+ "%s: SoftError <%@> failed to create background TapToRadarKit draft: %@"
+ "%s: SoftError <%@> is disabled"
+ "%s: SoftError <%@> missing input for TapToRadarKit draft"
+ "%s: Successfully wrote and flushed log entry to file"
+ "%s: Watching log file %@"
+ "%s: Writing to file: level=%lu, message length=%lu"
+ "%s: _filePtr is NULL, attempting to create new log file"
+ "%s: `platformDependent` expected to be an array of dictionaries, found %@ instead : %@"
+ "%s: `platformDependent` expected to be an array, found %@ instead : %@"
+ "%s: each dictionary in the array `platformDependent` is expected to contain key '%@' of type dictionary, found %@ instead : %@"
+ "%s: each dictionary in the array `platformDependent` is expected to contain key 'validOnPlatforms' of type array, found %@ instead : %@"
+ "%s: fdopen failed %@ (%s)"
+ "%s: found %@ config for platform %@"
+ "%s: log file: %@, creation time: %@"
+ "%s: lqmDistributionSampling for store:%@"
+ "%s: lqmDistributionSampling for telemetry:%@"
+ "%s: network (%@) contains %lu access points: %@"
+ "%s: new log file: %@"
+ "%s: open_dprotected_np failed %@ (%s)"
+ "%s: unable to find %@ configuration for current platform (%u)"
+ "+[WCAFetchWiFiBehaviorParameters fetchWiFiBehaviorWithCompletion:]_block_invoke"
+ "+[WiFiAirplaneLandingDetector clearPersistedState]"
+ "+[WiFiAirplaneLandingDetector defaultAltimeter]"
+ "+[WiFiUsageConfiguration getPlatformConfigFor:from:]"
+ "-[IoRegisterClient _collectEntryInfo:propertyKeys:planeName:]"
+ "-[IoRegisterClient _isMatch:onClassNames:]"
+ "-[IoRegisterClient _isMatch:onKeys:planeName:results:]"
+ "-[IoRegisterClient _searchEntry:hasMatchedDepth:currentDepth:maxDepth:classNames:keys:planeName:results:]"
+ "-[WFLoggerFileWithTTL cleanupOldFiles]"
+ "-[WFLoggerFileWithTTL createLogDirectoryIfNeeded]"
+ "-[WFLoggerFileWithTTL createNewLogFile]"
+ "-[WFLoggerFileWithTTL createPurgeableClassCFile:]"
+ "-[WFLoggerFileWithTTL initWithDirectoryPath:dirPath:fileNamePrefix:runLoopRef:runLoopMode:dateFormatter:maxFileSizeInMB:ttlInHours:rotationIntervalInHours:dispatchQueue:]"
+ "-[WFLoggerFileWithTTL setLogLifespanInDays:]"
+ "-[WFLoggerFileWithTTL setMaxFileSizeInMB:]"
+ "-[WFLoggerFileWithTTL shouldRotateFile]"
+ "-[WFLoggerFileWithTTL startWatchingLogFile]"
+ "-[WFLoggerFileWithTTL startWatchingLogFile]_block_invoke"
+ "-[WFLoggerFileWithTTL stopWatchingLogFile]"
+ "-[WFLoggerFileWithTTL writeToFile:cfStrMsg:]"
+ "-[WiFi3BarsNetwork initWithNetwork:]"
+ "-[WiFiAirplaneLandingDetector airplaneModeDidChange:]_block_invoke"
+ "-[WiFiAirplaneLandingDetector checkDetectionCriteria:]"
+ "-[WiFiAirplaneLandingDetector createSamplingTimer]_block_invoke"
+ "-[WiFiAirplaneLandingDetector dealloc]"
+ "-[WiFiAirplaneLandingDetector enterActiveFlightMode]"
+ "-[WiFiAirplaneLandingDetector enterInactiveMode]"
+ "-[WiFiAirplaneLandingDetector enterLayoverMode:]"
+ "-[WiFiAirplaneLandingDetector getAltitudeSample]_block_invoke"
+ "-[WiFiAirplaneLandingDetector initWithCompletion:config:altimeter:]"
+ "-[WiFiAirplaneLandingDetector networkDidJoinWithDetails:]_block_invoke"
+ "-[WiFiAirplaneLandingDetector notifyExceededAirportRadius]_block_invoke"
+ "-[WiFiAirplaneLandingDetector processSample:]"
+ "-[WiFiAirplaneLandingDetector resetExceededAirportRadius]_block_invoke"
+ "-[WiFiAirplaneLandingDetector retrieveAndClearState]"
+ "-[WiFiAirplaneLandingDetector ttr:]"
+ "-[WiFiAirplaneLandingDetector ttr:]_block_invoke"
+ "-[WiFiAirplaneLandingDetector updateSpeedSamples:]"
+ "-[WiFiAirplaneLandingDetector updateTimerInterval:]"
+ "-[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:]"
+ "-[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:]_block_invoke"
+ "-[WiFiSoftError createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:]_block_invoke_2"
+ "-[WiFiUsageMonitor appendUsbStatsToDict:]"
+ "-[WiFiUsageMonitor setTdLogic_cellularState:forInterface:]_block_invoke"
+ "-[WiFiUsageSession _generateState]_block_invoke"
+ "-[WiFiUsageSoftApSession softApStateDidChange:]"
+ "/"
+ "/AppleInternal/Library/BuildRoots/4~CIsLugB0o5r6EMNbd3-qJ3HQjkUA2rYwTNuyDaY/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:406: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "/Library/Caches/com.apple.xbs/C53332FF-2975-4DD8-8EE5-3E472D547CC9/TemporaryDirectory.iTB48e/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
+ "/Library/Logs/com.apple.WiFiPolicy"
+ "/System/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "/System/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "/System/Library/PrivateFrameworks/TapToRadarKit.framework/TapToRadarKit"
+ "<%@:%p>"
+ "<WiFiUsageSoftApStateInfo: active=%d, requester=%@, status=%@, reason=%@, channel=%lu, countryCode=%lu, hidden=%d, infraConnected=%d, awdlUp=%d, lowPowerModeDurationSec=%.2f, dynamicPowerModeDurationSec=%.2f, compat=%d, reqToUpLatency=%.2f, idleBeforeTeardown=%.2f, idleAfterClientDisconnect=%.2f>"
+ "<class error>"
+ "<name error>"
+ "@\"<WiFiAltimeterProtocol>\""
+ "@\"NSObject\"24@0:8@\"NSString\"16"
+ "@\"WiFiScanStatisticsAggregator\""
+ "@\"WiFiUsagePrivacyFilterSamplingRate\""
+ "@36@0:8I16@20r*28"
+ "@40@0:8@?16@24@32"
+ "@48@0:8{?=BBQQd}16"
+ "@56@0:8@16Q24@32@40^@48"
+ "@67@0:8@16B24i28q32Q40{context=BBB}48@51@59"
+ "@96@0:8@16@24@32^{__CFRunLoop=}40^{__CFString=}48^{__CFDateFormatter=}56Q64Q72Q80@88"
+ "Active Flight"
+ "Airplane Landing"
+ "AirplaneLandingDetector"
+ "AirplaneWiFiDetector"
+ "Around %@ was this device on an airplane?"
+ "B28@0:8I16@20"
+ "B44@0:8I16@20r*28@36"
+ "CMAltimeter"
+ "Client mismatch %lu[%lu]\n"
+ "Could not obtain I/O Kit's root service"
+ "DEBUG"
+ "DEFAULT"
+ "DP"
+ "DynamicPowerModeDuration"
+ "ERROR_CODE"
+ "ExceededAssignedRFPowerBudget"
+ "ExceededAssignedRoamPowerBudget"
+ "ExceededRelativeRFPowerBudget"
+ "ExceededRelativeRoamPowerBudget"
+ "FAILURE_COUNT"
+ "FAULT"
+ "FaultReasonAlwaysOnLPASAssignedRFBudgetExceeded"
+ "FaultReasonAlwaysOnLPASAssignedRoamBudgetExceeded"
+ "FaultReasonAlwaysOnLPASRelativeRFBudgetExceeded"
+ "FaultReasonAlwaysOnLPASRelativeRoamBudgetExceeded"
+ "FaultReasonAlwaysOnLPASScanBudgetExceeded"
+ "FaultReasonAlwaysOnLPASTotalBudgetExceeded"
+ "INFO"
+ "IOObjectClass"
+ "IOPortTransportStateCIO"
+ "IOPortTransportStateDisplayPort"
+ "IOPortTransportStateUSB2"
+ "IOPortTransportStateUSB3"
+ "IORegistryEntryID"
+ "IORegistryEntryName"
+ "IORegistryEntryPath"
+ "IOService"
+ "IS_2G_SCAN"
+ "IS_2G_SCAN_COUNT"
+ "IS_2G_SCAN_SCAN_CORE"
+ "IS_2G_SCAN_SCAN_CORE_COUNT"
+ "IS_5G_SCAN"
+ "IS_5G_SCAN_COUNT"
+ "IS_5G_SCAN_SCAN_CORE"
+ "IS_5G_SCAN_SCAN_CORE_COUNT"
+ "IS_6G_SCAN"
+ "IS_6G_SCAN_COUNT"
+ "IS_6G_SCAN_SCAN_CORE"
+ "IS_6G_SCAN_SCAN_CORE_COUNT"
+ "Inactive"
+ "Invalid client %lu\n"
+ "Invalid statistics object\n"
+ "Invalid statistics object provided for aggregation\n"
+ "IoRegisterClient"
+ "Is %@ an Airplane WiFi?"
+ "LastRoamCacheMaxRssi2G"
+ "LastRoamCacheMaxRssi5G"
+ "LastRoamCacheMaxRssi6G"
+ "Last_WiFiPreferredOverCell"
+ "Last_cellularWRMScore"
+ "Last_cellularWRMScoreConfidence"
+ "Last_isCellularDataUsable"
+ "Last_timeSinceCellularWRMScoreUpdate"
+ "Layover"
+ "Missing input parameter"
+ "NominalSignalingFrequenciesHz"
+ "Please help us gathering Airplane WiFi logs by filing a radar (even if you were not using the Airplane WiFi)\n\n%@\n\n%@\n\n"
+ "Port-USB-C@"
+ "RadarComponent"
+ "RadarDraft"
+ "Rate limiting scan metric post\n"
+ "SCAN_CLIENT"
+ "SCAN_CORE_SCAN_DURATION_2G_MS"
+ "SCAN_CORE_SCAN_DURATION_5G_MS"
+ "SCAN_CORE_SCAN_DURATION_6G_MS"
+ "SCAN_CORE_SCAN_DURATION_MS"
+ "SCAN_DURATION_2G_MS"
+ "SCAN_DURATION_5G_MS"
+ "SCAN_DURATION_6G_MS"
+ "SCAN_DURATION_MS"
+ "SUCCESS_COUNT"
+ "T@\"<WiFiAltimeterProtocol>\",&,N,V_altimeter"
+ "T@\"NSDate\",&,N,V_firstTimeExceededAirportRadius"
+ "T@\"NSDate\",&,N,V_lastRoamCacheAt"
+ "T@\"NSDate\",&,N,V_lastSampleDate"
+ "T@\"NSDate\",&,N,V_lastSubmissionTime"
+ "T@\"NSDate\",&,N,V_lastSuccessfulRoamAt"
+ "T@\"NSDate\",&,N,V_layoverModeStartDate"
+ "T@\"NSDictionary\",&,V_config"
+ "T@\"NSMutableArray\",&,N,V_aggregator"
+ "T@\"NSMutableArray\",&,N,V_verticalSpeedSamples"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_samplingTimer"
+ "T@\"NSOperationQueue\",&,N,V_queue"
+ "T@\"NSSet\",&,N,V_accessPoints"
+ "T@\"NSString\",&,N,V_changeReason"
+ "T@\"NSString\",&,V_platform"
+ "T@\"NSString\",R,GgetLogFileNamePrefix"
+ "T@\"NSString\",R,GgetLogFilePath"
+ "T@\"NSURL\",R,GgetLogDirURL"
+ "T@\"WiFiScanStatisticsAggregator\",&,N,V_scanAggregator"
+ "T@\"WiFiSoftError\",&,N,V_softError"
+ "T@\"WiFiSoftError\",R,N,V_softError"
+ "T@\"WiFiUsagePrivacyFilterSamplingRate\",&,N,V_lqmDistributionSampling_store"
+ "T@\"WiFiUsagePrivacyFilterSamplingRate\",&,N,V_lqmDistributionSampling_telemetry"
+ "T@?,C,N,V_landingCallback"
+ "TB,N,V_active"
+ "TB,N,V_compatibilityMode"
+ "TB,N,V_isAirplane"
+ "TB,N,V_isAwdlUp"
+ "TB,N,V_isCellularStateAtLinkDownValid"
+ "TB,N,V_isInfraConnected"
+ "TB,N,V_isLastCellularStateValid"
+ "TB,N,V_waitingForFirstSampleAfterReboot"
+ "TQ,N,V_channelNumber"
+ "TQ,N,V_client"
+ "TQ,N,V_countryCode"
+ "TQ,N,V_failureCount"
+ "TQ,N,V_is2GScan"
+ "TQ,N,V_is2GScanScanCore"
+ "TQ,N,V_is5GScan"
+ "TQ,N,V_is5GScanScanCore"
+ "TQ,N,V_is6GScan"
+ "TQ,N,V_is6GScanScanCore"
+ "TQ,N,V_scanCore2GScanDuration"
+ "TQ,N,V_scanCore5GScanDuration"
+ "TQ,N,V_scanCore6GScanDuration"
+ "TQ,N,V_scanCoreScanDurationAllBands"
+ "TQ,N,V_scanDuration2G"
+ "TQ,N,V_scanDuration5G"
+ "TQ,N,V_scanDuration6G"
+ "TQ,N,V_scanDurationAllBands"
+ "TQ,N,V_successCount"
+ "TapToRadarService"
+ "Td,N,V_currentSamplingInterval"
+ "Td,N,V_dynamicPowerModeDurationSec"
+ "Td,N,V_lastAltitude"
+ "Td,N,V_lowPowerModeDurationSec"
+ "Td,N,V_maxAltitude"
+ "Td,N,V_timeFromLastRoamCacheToSessionEnd"
+ "Td,N,V_timeFromLastRoamCacheToTDConfirmed"
+ "Td,N,V_timeFromLastSuccessfulRoamToSessionEnd"
+ "Td,N,V_timeFromLastSuccessfulRoamToTDConfirmed"
+ "This SoftError is disabled"
+ "Ti,N,V_err"
+ "Ti,N,V_lastDisconnectReason"
+ "Ti,N,V_lastJoinReason"
+ "Ti,N,V_prevJoinReason"
+ "Ti,N,V_previousDisconnectReason"
+ "Ti,N,V_savedLastJoinReason"
+ "Ti,N,V_savedPrevJoinReason"
+ "Ti,N,V_savedPreviousDisconnectReason"
+ "TimeFromLastRoamCacheToSessionEnd"
+ "TimeFromLastRoamCacheToTDConfirmed"
+ "TimeFromLastSuccessfulRoamToSessionEnd"
+ "TimeFromLastSuccessfulRoamToTDConfirmed"
+ "Tq,N,V_lastRoamCacheMaxRssi2G"
+ "Tq,N,V_lastRoamCacheMaxRssi5G"
+ "Tq,N,V_lastRoamCacheMaxRssi6G"
+ "T{?=BBQQd},N,V_cellularStateAtLinkDown"
+ "T{?=BBQQd},N,V_last_CellularState"
+ "T{?=dddQQddddd},N,V_config"
+ "UNEXPECTED ERROR"
+ "UNKNOWN"
+ "UTC"
+ "Unable to aggregate scan result for client %lu\n"
+ "Unable to create dictionary\n"
+ "Unable to gather data to be posted\n"
+ "Unable to init internal queue, exiting....\n"
+ "Unable to init scan Aggregator, exiting....\n"
+ "Unable to init scan aggregator, exiting....\n"
+ "Unable to init scan stats, exiting....\n"
+ "Unable to init stats aggregator, exiting....\n"
+ "Unable to init super, exiting....\n"
+ "WARNING: Integer overflow detected when adding %llu and %llu"
+ "WAUnavailable=%u"
+ "WFLoggerFileWithTTL"
+ "WiFi (New Bugs)"
+ "WiFiAirplaneLandingDetector"
+ "WiFiScanMonitor"
+ "WiFiScanStatistics"
+ "WiFiScanStatisticsAggregator"
+ "WiFiUsageConfiguration"
+ "WiFiUsagePlatformConfig"
+ "WiFiUsagePrivacyFilterSamplingRate"
+ "WiFiUsageSoftApStateInfo"
+ "[%@] [%s:%d:%llu] [%@] %@\n"
+ "[1040Q]"
+ "[16Q]"
+ "[29Q]"
+ "[44Q]"
+ "[AirplaneWiFi] Possible Airplane WiFi Detection"
+ "^{__sFILE=*iiss{__sbuf=*i}i^v^?^?^?^?{__sbuf=*i}^{__sFILEX}i[3C][1C]{__sbuf=*i}iq}24@0:8@16"
+ "_accessPoints"
+ "_active"
+ "_aggregator"
+ "_altimeter"
+ "_cellularStateAtLinkDown"
+ "_changeReason"
+ "_channelNumber"
+ "_cleanupAgeInSeconds"
+ "_client"
+ "_collectEntryInfo:propertyKeys:planeName:"
+ "_compatibilityMode"
+ "_countryCode"
+ "_currentSamplingInterval"
+ "_directoryURL"
+ "_dynamicPowerModeDurationSec"
+ "_enabledLevel"
+ "_err"
+ "_failureCount"
+ "_firstTimeExceededAirportRadius"
+ "_is2GScan"
+ "_is2GScanScanCore"
+ "_is5GScan"
+ "_is5GScanScanCore"
+ "_is6GScan"
+ "_is6GScanScanCore"
+ "_isAirplane"
+ "_isAwdlUp"
+ "_isCellularStateAtLinkDownValid"
+ "_isInfraConnected"
+ "_isInternalDeviceAndAppleInternalNetwork"
+ "_isLastCellularStateValid"
+ "_isMatch:onClassNames:"
+ "_isMatch:onKeys:planeName:results:"
+ "_landingCallback"
+ "_lastAltitude"
+ "_lastRoamCacheAt"
+ "_lastRoamCacheMaxRssi2G"
+ "_lastRoamCacheMaxRssi5G"
+ "_lastRoamCacheMaxRssi6G"
+ "_lastSampleDate"
+ "_lastSubmissionTime"
+ "_lastSuccessfulRoamAt"
+ "_last_CellularState"
+ "_layoverModeStartDate"
+ "_lowPowerModeDurationSec"
+ "_maxAltitude"
+ "_platform"
+ "_rotationIntervalInHours"
+ "_samplingTimer"
+ "_scanAggregator"
+ "_scanCore2GScanDuration"
+ "_scanCore5GScanDuration"
+ "_scanCore6GScanDuration"
+ "_scanCoreScanDurationAllBands"
+ "_scanDuration2G"
+ "_scanDuration5G"
+ "_scanDuration6G"
+ "_scanDurationAllBands"
+ "_searchEntry:hasMatchedDepth:currentDepth:maxDepth:classNames:keys:planeName:results:"
+ "_softError"
+ "_successCount"
+ "_timeFromLastRoamCacheToSessionEnd"
+ "_timeFromLastRoamCacheToTDConfirmed"
+ "_timeFromLastSuccessfulRoamToSessionEnd"
+ "_timeFromLastSuccessfulRoamToTDConfirmed"
+ "_timestampFormatter"
+ "_ttlInHours"
+ "_verticalSpeedSamples"
+ "_waitingForFirstSampleAfterReboot"
+ "active"
+ "activeFlightInterval"
+ "add:with:"
+ "aggregateClientMetrics:"
+ "aggregateValues:"
+ "aggregator"
+ "airplane"
+ "airplane-wifi"
+ "airplaneModeDidChange:"
+ "altimeter"
+ "altimeter: %@\n  layoverModeStartDate: %@\n  maxAltitude: %.2f m\n  lastAltitude: %.2f m\n  lastSampleDate: %@\n  currentSamplingInterval: %@\n  inInactiveMode: %@\n  verticalSpeedSamples: (%lu samples) %@\n  config: {\n    activeFlightInterval: %@ sec\n    layoverInterval: %@ sec\n    inactiveInterval: %@ sec\n    maxSamples: %lu\n    minSamplesAboveThreshold: %lu\n    minVerticalSpeed: %.2f m/s\n    minMaxAltitude: %.2f m\n    takeoffAltitudeIncrease: %.2f m\n    layoverTimeout: %@ sec\n    sustainedInactivityTimeout: %@ sec\n  }"
+ "applewatch"
+ "applewifi"
+ "applewifisecure"
+ "authorizationStatus"
+ "canPerformActionWithDynamicBaseSampleRate:"
+ "canSubmitToCA:"
+ "captureCellularStateAtLinkDown"
+ "cellularStateAtLinkDown"
+ "cellularWRMScoreAtLinkDown"
+ "cellularWRMScoreConfidenceAtLinkDown"
+ "changeReason"
+ "checkDetectionCriteria:"
+ "checkForRotation"
+ "cleanupOldFiles"
+ "clearPersistedState"
+ "client"
+ "com.apple.DiagnosticExtensions.WiFi"
+ "com.apple.wifi.airplane-landing-detector"
+ "com.apple.wifi.dailyScanMetrics"
+ "com.apple.wifi.instantaneousScanMetrics"
+ "com.apple.wifi.ioregister-client"
+ "com.apple.wifi.scanstats.aggregator"
+ "com.apple.wifipolicy.airplane_wifi_detector"
+ "compatibilityMode"
+ "completion and altimeter cannot be nil"
+ "component Name and Version shall either either both be nil or neither"
+ "contentsOfDirectoryAtPath:error:"
+ "countryCode"
+ "createBackgroundTapToRadarDraftWithTitle:description:component:componentVersion:componentIdentifier:keywords:displayReason:diagnosticExtensions:completionHandler:"
+ "createBackgroundTapToRadarDraftWithTitle:description:keywords:displayReason:completionHandler:"
+ "createDirectoryAtURL:withIntermediateDirectories:attributes:error:"
+ "createDraft:forProcessNamed:withDisplayReason:completionHandler:"
+ "createLogDirectoryIfNeeded"
+ "createNewLogFile"
+ "createPurgeableClassCFile:"
+ "createSamplingTimer"
+ "currentModeName"
+ "currentSamplingInterval"
+ "current_altimeter_sampling_interval"
+ "d24@0:8@16"
+ "defaultAltimeter"
+ "defaultConfig"
+ "denied"
+ "describeTime:"
+ "describeWiFiUsageMonitor_tdCellularState:"
+ "didDetectAirplaneLanding"
+ "dispatchQueue"
+ "dynamicPowerModeDurationSec"
+ "enterActiveFlightMode"
+ "enterInactiveMode"
+ "enterLayoverMode:"
+ "err"
+ "failureCount"
+ "fetchEntriesForClasses:depth:keys:plane:error:"
+ "findHighestNomSignFqMHz:"
+ "firstTimeExceededAirportRadius"
+ "gatherDataToBePosted:"
+ "gatherLandingDetectedLogs:"
+ "gatherScanStatisticsForClient:error:is2GScan:is2GScanScanCore:is5GScan:is5GScanScanCore:is6GScan:is6GScanScanCore:scanDuration2G:scanDuration5G:scanDuration6G:scanCore2GScanDuration:scanCore5GScanDuration:scanCore6GScanDuration:"
+ "getAltitudeSample"
+ "getLogDirURL"
+ "getPlatformConfigFor:from:"
+ "home"
+ "hrs"
+ "iOS"
+ "inInactiveMode"
+ "inLayoverMode"
+ "inactiveInterval"
+ "initForClient:"
+ "initWith:platform:key:"
+ "initWithCompletion:"
+ "initWithCompletion:config:altimeter:"
+ "initWithDirectoryPath:dirPath:fileNamePrefix:runLoopRef:runLoopMode:dateFormatter:maxFileSizeInMB:ttlInHours:rotationIntervalInHours:dispatchQueue:"
+ "initWithName:version:identifier:"
+ "intersectsSet:"
+ "is2GScan"
+ "is2GScanScanCore"
+ "is5GScan"
+ "is5GScanScanCore"
+ "is6GScan"
+ "is6GScanScanCore"
+ "isAbsoluteAltitudeAvailable"
+ "isAirplane"
+ "isAppleInternalNetwork"
+ "isAwdlUp"
+ "isCellularDataUsableAtLinkDown"
+ "isCellularStateAtLinkDownValid"
+ "isDetectorActive"
+ "isInfraConnected"
+ "isLastCellularStateValid"
+ "it detected an Airplane WiFi network. Please tap to file a radar"
+ "joinReasonAsString:"
+ "kWiFiUsageFaultReasonAlwaysOnLPASAssignedRFBudgetExceeded"
+ "kWiFiUsageFaultReasonAlwaysOnLPASAssignedRoamBudgetExceeded"
+ "kWiFiUsageFaultReasonAlwaysOnLPASRelativeRFBudgetExceeded"
+ "kWiFiUsageFaultReasonAlwaysOnLPASRelativeRoamBudgetExceeded"
+ "kWiFiUsageFaultReasonAlwaysOnLPASScanBudgetExceeded"
+ "kWiFiUsageFaultReasonAlwaysOnLPASTotalBudgetExceeded"
+ "landingCallback"
+ "lastAltitude"
+ "lastRoamCacheAt"
+ "lastRoamCacheMaxRssi2G"
+ "lastRoamCacheMaxRssi5G"
+ "lastRoamCacheMaxRssi6G"
+ "lastSampleDate"
+ "lastSubmissionTime"
+ "lastSuccessfulRoamAt"
+ "last_CellularState"
+ "layoverInterval"
+ "layoverModeStartDate"
+ "layoverTimeout"
+ "layover_mode_start_date"
+ "leftAirport"
+ "lowPowerModeDurationSec"
+ "mapIORegistryEntryPathToCAFieldPort:"
+ "mapIORegistryEntryPathToCAFieldTransport:"
+ "maxAltitude"
+ "maxSamples"
+ "max_altitude"
+ "min"
+ "minMaxAltitude"
+ "minSamplesAboveThreshold"
+ "minVerticalSpeed"
+ "networkDidJoinWithDetails:"
+ "notifyExceededAirportRadius"
+ "parseTimestampFromFilename:"
+ "persistState"
+ "platform"
+ "portUSBC%@"
+ "postDailyScanMetricsToCA"
+ "postIndividualScanMetricsToCA"
+ "processSample:"
+ "rangeOfString:"
+ "reality"
+ "removePersistentDomainForName:"
+ "resetExceededAirportRadius"
+ "restricted"
+ "retrieveAndClearState"
+ "rotateToNewFile"
+ "samplingDescription"
+ "samplingTimer"
+ "scalingFactorForSamplingRate:"
+ "scanAggregator"
+ "scanCore2GScanDuration"
+ "scanCore5GScanDuration"
+ "scanCore6GScanDuration"
+ "scanCoreScanDurationAllBands"
+ "scanDuration2G"
+ "scanDuration5G"
+ "scanDuration6G"
+ "scanDurationAllBands"
+ "sec"
+ "setAccessPoints:"
+ "setActive:"
+ "setAggregator:"
+ "setAltimeter:"
+ "setCellularStateAtLinkDown:"
+ "setChangeReason:"
+ "setChannelNumber:"
+ "setClassification:"
+ "setClient:"
+ "setCompatibilityMode:"
+ "setComponent:"
+ "setCountryCode:"
+ "setCurrentSamplingInterval:"
+ "setDiagnosticExtensionIDs:"
+ "setDynamicPowerModeDurationSec:"
+ "setErr:"
+ "setFailureCount:"
+ "setFirstTimeExceededAirportRadius:"
+ "setIs2GScan:"
+ "setIs2GScanScanCore:"
+ "setIs5GScan:"
+ "setIs5GScanScanCore:"
+ "setIs6GScan:"
+ "setIs6GScanScanCore:"
+ "setIsAirplane:"
+ "setIsAwdlUp:"
+ "setIsCellularStateAtLinkDownValid:"
+ "setIsInfraConnected:"
+ "setIsLastCellularStateValid:"
+ "setIsUserInitiated:"
+ "setKeywords:"
+ "setLandingCallback:"
+ "setLastAltitude:"
+ "setLastRoamCacheAt:"
+ "setLastRoamCacheMaxRssi2G:"
+ "setLastRoamCacheMaxRssi5G:"
+ "setLastRoamCacheMaxRssi6G:"
+ "setLastSampleDate:"
+ "setLastSubmissionTime:"
+ "setLastSuccessfulRoamAt:"
+ "setLast_CellularState:"
+ "setLayoverModeStartDate:"
+ "setLinkEventWithIntegerReason:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:forInterface:"
+ "setLowPowerModeDurationSec:"
+ "setMaxAltitude:"
+ "setMaxConcurrentOperationCount:"
+ "setPersistentDomain:forName:"
+ "setPlatform:"
+ "setProblemDescription:"
+ "setReproducibility:"
+ "setSamplingTimer:"
+ "setScanAggregator:"
+ "setScanCore2GScanDuration:"
+ "setScanCore5GScanDuration:"
+ "setScanCore6GScanDuration:"
+ "setScanCoreScanDurationAllBands:"
+ "setScanDuration2G:"
+ "setScanDuration5G:"
+ "setScanDuration6G:"
+ "setScanDurationAllBands:"
+ "setSoftApState:"
+ "setSoftError:"
+ "setSuccessCount:"
+ "setTdLogic_cellularState:forInterface:"
+ "setTimeFromLastRoamCacheToSessionEnd:"
+ "setTimeFromLastRoamCacheToTDConfirmed:"
+ "setTimeFromLastSuccessfulRoamToSessionEnd:"
+ "setTimeFromLastSuccessfulRoamToTDConfirmed:"
+ "setTitle:"
+ "setUnderlyingQueue:"
+ "setVerticalSpeedSamples:"
+ "setWaitingForFirstSampleAfterReboot:"
+ "shared"
+ "sharedScanMonitor"
+ "shouldRotateFile"
+ "softApStateDidChange:"
+ "softError"
+ "softlink:r:path:/System/Library/Frameworks/CoreMotion.framework/CoreMotion"
+ "softlink:r:path:/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy"
+ "startAbsoluteAltitudeUpdatesToQueue:withHandler:"
+ "stopAbsoluteAltitudeUpdates"
+ "successCount"
+ "sustainedInactivityOutsideAirportTimeout"
+ "takeoffAltitudeIncrease"
+ "tdLogic_cellularState:"
+ "timeFromLastRoamCacheToSessionEnd"
+ "timeFromLastRoamCacheToTDConfirmed"
+ "timeFromLastSuccessfulRoamToSessionEnd"
+ "timeFromLastSuccessfulRoamToTDConfirmed"
+ "timeSinceCellularWRMScoreUpdateAtLinkDown"
+ "ttr:"
+ "unexpected %@"
+ "updateConfig:"
+ "updateSpeedSamples:"
+ "updateTimerInterval:"
+ "v100@0:8Q16i24B28B32B36B40B44B48Q52Q60Q68Q76Q84Q92"
+ "v24@?0@\"CMAbsoluteAltitudeData\"8@\"NSError\"16"
+ "v36@0:8d16i24@28"
+ "v44@0:8B16B20i24q28@36"
+ "v48@0:8@16i24i28q32@40"
+ "v48@0:8{?=BBQQd}16"
+ "v52@0:8B16B20i24q28@36@44"
+ "v52@0:8B16i20i24q28@36@44"
+ "v56@0:8@16@24@32@40@?48"
+ "v56@0:8{?=BBQQd}16@48"
+ "v76@0:8I16Q20Q28Q36@44@52r*60@68"
+ "v88@0:8@16@24@32@40Q48@56@64@72@?80"
+ "v96@0:8{?=dddQQddddd}16"
+ "verticalSpeedSamples"
+ "waitingForFirstSampleAfterReboot"
+ "wifiPreferredOverCell:%@ isCellularDataUsable:%@ cellularWRMScore:%lu cellularWRMScoreConfidence:%lu cellularWRMStateChangeTimestamp:%f"
+ "wifiPreferredOverCellAtLinkDown"
+ "wifipolicy.state.exclude-flag"
+ "work"
+ "yyyy-MM-dd HH:mm:ss.SSS zzz"
+ "yyyy-MM-dd_HH-mm-ss"
+ "{?=\"activeFlightInterval\"d\"layoverInterval\"d\"inactiveInterval\"d\"maxSamples\"Q\"minSamplesAboveThreshold\"Q\"minVerticalSpeed\"d\"minMaxAltitude\"d\"takeoffAltitudeIncrease\"d\"layoverTimeout\"d\"sustainedInactivityOutsideAirportTimeout\"d}"
+ "{?=\"wifiPreferredOverCell\"B\"isCellularDataUsable\"B\"cellularWRMScore\"Q\"cellularWRMScoreConfidence\"Q\"cellularWRMStateChangeTimestamp\"d}"
+ "{?=BBQQd}16@0:8"
+ "{?=dddQQddddd}16@0:8"
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
- "%s: %@ BEGIN"
- "%s: Cannot parse DataPathTelemetry.platformDependent: %@"
- "%s: Received LQMDistribution config from Mobile Assets"
- "%s: received config for platform %@"
- "%s: unable to find DataPathTelemetry configuration for current platform"
- "+[WiFiUsageLQMConfiguration getConfigForPlatform]"
- "-[WiFiUsageSoftApSession softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]"
- "/Library/Caches/com.apple.xbs/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
- "11c_antennas"
- "11n_antennas"
- "@\"<TBNetwork>\""
- "@71@0:8@16B24q28q36Q44{context=BBB}52@55@63"
- "AutoHotspot"
- "Error: Response is not of type WCAFetchKeyValuesResponse, instead its %@"
- "HomeKit"
- "Legacy Transition"
- "OtherClient"
- "QBSS_Load"
- "Recommendation"
- "Seamless Transition"
- "Setup"
- "Sharing"
- "T@\"<TBNetwork>\",&,N,V_network"
- "T@\"NSNumber\",&,V_lqmDistributionSampling_store"
- "T@\"NSNumber\",&,V_lqmDistributionSampling_telemetry"
- "T@\"NSString\",&,N,V_antennas11n"
- "T@\"NSString\",&,N,V_wlanAsel"
- "T@\"NSString\",&,N,V_wlanFixedCapabilities"
- "T@\"NSString\",&,N,V_wlanHTAmpduparam"
- "T@\"NSString\",&,N,V_wlanHTCapabilities"
- "T@\"NSString\",&,N,V_wlanHtexCapabilities"
- "T@\"NSString\",&,N,V_wlanTxbf"
- "T@\"NSString\",&,N,V_wlanVhtCapabilities"
- "T@\"NSString\",&,N,V_wlanWfaIeWmeQosInfo"
- "TB,N,V_QBSS_Load"
- "TB,N,V_UAPSD"
- "TB,N,V_has_11krm"
- "TQ,N,V_lastJoinReason"
- "TQ,N,V_prevJoinReason"
- "TQ,N,V_savedLastJoinReason"
- "TQ,N,V_savedPrevJoinReason"
- "Td,N,V_lowPowerModeDuration"
- "Tf,N,V_antennas11c"
- "Tf,N,V_max_rates"
- "Tf,N,V_wlanTimDtimPeriod"
- "Tq,N,V_beaconInterval"
- "Tq,N,V_lastDisconnectReason"
- "Tq,N,V_previousDisconnectReason"
- "Tq,N,V_savedPreviousDisconnectReason"
- "U-APSD"
- "UAPSD"
- "UserOverridesAutoJoinDenyList"
- "WCAFetchBeaconDBParameters"
- "WCAFetchSQLiteBeaconDBRequest"
- "WiFiUsageLQMAnalysisSamplingRate"
- "WiFiUsageWatchdogDetailsSubmitToCA"
- "[1036Q]"
- "[15Q]"
- "[27Q]"
- "[38Q]"
- "_QBSS_Load"
- "_UAPSD"
- "_antennas11c"
- "_antennas11n"
- "_has_11krm"
- "_lowPowerModeDuration"
- "_max_rates"
- "_wlanAsel"
- "_wlanFixedCapabilities"
- "_wlanHTAmpduparam"
- "_wlanHTCapabilities"
- "_wlanHtexCapabilities"
- "_wlanTimDtimPeriod"
- "_wlanTxbf"
- "_wlanVhtCapabilities"
- "_wlanWfaIeWmeQosInfo"
- "antennas11c"
- "antennas11n"
- "beacon_interval"
- "f"
- "fetchWithCompletion:"
- "getConfigForPlatform"
- "has_11krm"
- "index"
- "lowPowerModeDuration"
- "max_rates"
- "prof_clean"
- "scalingFactorForRawSampleRate:"
- "setAntennas11c:"
- "setAntennas11n:"
- "setHas_11krm:"
- "setLowPowerModeDuration:"
- "setMax_rates:"
- "setQBSS_Load:"
- "setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:"
- "setUAPSD:"
- "setWlanAsel:"
- "setWlanFixedCapabilities:"
- "setWlanHTAmpduparam:"
- "setWlanHTCapabilities:"
- "setWlanHtexCapabilities:"
- "setWlanTimDtimPeriod:"
- "setWlanTxbf:"
- "setWlanVhtCapabilities:"
- "setWlanWfaIeWmeQosInfo:"
- "softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:"
- "v108@0:8B16@20@28@36Q44Q52B60B64B68d72B80d84d92d100"
- "v20@0:8f16"
- "v40@0:8d16Q24@32"
- "v48@0:8B16B20q24q32@40"
- "v56@0:8@16Q24q32q40@48"
- "v60@0:8B16Q20Q28q36@44@52"
- "wlan-asel"
- "wlan-fixed-capabilities"
- "wlan-ht-ampduparam"
- "wlan-ht-capabilities"
- "wlan-htex-capabilities"
- "wlan-tim-dtim_period"
- "wlan-txbf"
- "wlan-vht-capabilities"
- "wlan-wfa-ie-wme-qos_info"
- "wlanAsel"
- "wlanFixedCapabilities"
- "wlanHTAmpduparam"
- "wlanHTCapabilities"
- "wlanHtexCapabilities"
- "wlanTimDtimPeriod"
- "wlanTxbf"
- "wlanVhtCapabilities"
- "wlanWfaIeWmeQosInfo"

```
