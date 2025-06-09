## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-990.3.0.0.0
-  __TEXT.__text: 0xb92c8
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0x110e8
-  __TEXT.__const: 0x638
-  __TEXT.__cstring: 0x1c060
-  __TEXT.__oslogstring: 0x3ac3
-  __TEXT.__gcc_except_tab: 0x18f0
+1026.66.0.0.0
+  __TEXT.__text: 0xbda34
+  __TEXT.__auth_stubs: 0x1600
+  __TEXT.__objc_methlist: 0x115e0
+  __TEXT.__const: 0x648
+  __TEXT.__cstring: 0x1ca32
+  __TEXT.__oslogstring: 0x3d54
+  __TEXT.__gcc_except_tab: 0x197c
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x20d0
-  __TEXT.__objc_classname: 0x137b
-  __TEXT.__objc_methname: 0x31984
-  __TEXT.__objc_methtype: 0x3a26
-  __TEXT.__objc_stubs: 0x180e0
-  __DATA_CONST.__got: 0xa40
-  __DATA_CONST.__const: 0x21d8
-  __DATA_CONST.__objc_classlist: 0x510
+  __TEXT.__unwind_info: 0x2160
+  __TEXT.__objc_classname: 0x1400
+  __TEXT.__objc_methname: 0x32874
+  __TEXT.__objc_methtype: 0x3b53
+  __TEXT.__objc_stubs: 0x18900
+  __DATA_CONST.__got: 0xa58
+  __DATA_CONST.__const: 0x22d8
+  __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9760
+  __DATA_CONST.__objc_selrefs: 0x99f8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x430
-  __DATA_CONST.__objc_arraydata: 0xa58
-  __AUTH_CONST.__auth_got: 0xb10
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x187c0
-  __AUTH_CONST.__objc_const: 0x20b10
-  __AUTH_CONST.__objc_intobj: 0x1740
+  __DATA_CONST.__objc_superrefs: 0x438
+  __DATA_CONST.__objc_arraydata: 0xa88
+  __AUTH_CONST.__auth_got: 0xb18
+  __AUTH_CONST.__const: 0x440
+  __AUTH_CONST.__cfstring: 0x18f40
+  __AUTH_CONST.__objc_const: 0x21610
+  __AUTH_CONST.__objc_intobj: 0x17b8
   __AUTH_CONST.__objc_arrayobj: 0x390
-  __AUTH_CONST.__objc_dictobj: 0x78
+  __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x2098
+  __AUTH.__objc_data: 0x8c0
+  __AUTH.__data: 0x8
+  __DATA.__objc_ivar: 0x2130
   __DATA.__data: 0x1bc0
-  __DATA.__bss: 0x22
-  __DATA_DIRTY.__objc_data: 0x2a80
+  __DATA.__bss: 0x52
+  __DATA_DIRTY.__objc_data: 0x2b20
   __DATA_DIRTY.__bss: 0x298
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/Bom.framework/Bom
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
+  - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6FB50022-2DBD-3ADE-9896-3641E3F61FBC
-  Functions: 6014
-  Symbols:   19652
-  CStrings:  16306
+  UUID: 5ED46304-472C-39DE-ACFA-9CFBC2920A83
+  Functions: 6140
+  Symbols:   20047
+  CStrings:  16596
 
Symbols:
+ +[WFMeasure supportsLinkRecoveryTests]
+ +[WiFiDiagnosticReporter sharedWiFiDiagnosticReporter]
+ +[WiFiDiagnosticReporter sharedWiFiDiagnosticReporter].cold.1
+ +[WiFiSoftError _updateHUDWithHost:messageDict:]
+ +[WiFiSoftError _updateHUDWithHost:messageDict:].cold.1
+ +[WiFiSoftError _updateHUDWithHost:messageDict:].cold.2
+ +[WiFiSoftError _updateHUDWithHost:messageDict:].cold.3
+ +[WiFiUsageAccessPointProfile _isProfileValidForUse:withCachedDict:onlyIfCurrent:withError:]
+ +[WiFiUsageAccessPointProfile _isProfileValidForUse:withCachedDict:withError:]
+ +[WiFiUsageAccessPointProfile _loadFromUserDefaults:withKey:withCachedData:withError:]
+ +[WiFiUsageAccessPointProfile errorStringForTelemetry:]
+ +[WiFiUsageAccessPointProfile longProfileForBSSID:withError:]
+ +[WiFiUsageAccessPointProfile profileForBSSID:onlyIfCurrent:withError:]
+ +[WiFiUsageAccessPointProfile profileForBSSID:withError:]
+ +[WiFiUsageAccessPointProfile shortProfileForBSSID:withError:]
+ +[WiFiUsageAccessPointProfile submitToCAForBSSID:]
+ +[WiFiUsageAccessPointProfile submitToCAForBSSID:].cold.1
+ +[WiFiUsageAccessPointProfile submitToCAForBSSID:].cold.2
+ +[WiFiUsageAccessPointProfile submitToCAForBSSID:].cold.3
+ +[WiFiUsageLQMDistributionConfiguration getConfigForKey:]
+ +[WiFiUsageLQMDistributionConfiguration initialize]
+ +[WiFiUsageLQMDistributionConfiguration setConfig:]
+ +[WiFiUsagePrivacyFilter canPerformActionWithRawSampleRate:]
+ +[WiFiUsagePrivacyFilter scalingFactorForRawSampleRate:]
+ +[WiFiUsagePrivacyFilter waBandFromBand:]
+ -[WCAFetchWiFiBehaviorParameters lqmDistribution]
+ -[WCAFetchWiFiBehaviorParameters setLqmDistribution:]
+ -[WFMeasure dispatchULThroughputTest]
+ -[WFMeasure doThroughputTest].cold.1
+ -[WFMeasure doULThroughputTest]
+ -[WFMeasure doULThroughputTest].cold.1
+ -[WFMeasure initializePerformanceTest]
+ -[WFMeasureResult backhaulULThroughput]
+ -[WFMeasureResult setBackhaulULThroughput:]
+ -[WFMeasureResult setUploadError:]
+ -[WFMeasureResult uploadError]
+ -[WiFi3BarsSource removalHandler]
+ -[WiFi3BarsSource setRemovalHandler:]
+ -[WiFiAvailabilityEngine _handleWalletChange:removed:]
+ -[WiFiAvailabilityEngine _handleWalletRemoval:]
+ -[WiFiAvailabilityNearbyCandidateNetwork .cxx_destruct]
+ -[WiFiAvailabilityNearbyCandidateNetwork SSID]
+ -[WiFiAvailabilityNearbyCandidateNetwork accessPoints]
+ -[WiFiAvailabilityNearbyCandidateNetwork attributes]
+ -[WiFiAvailabilityNearbyCandidateNetwork containsAccessPointMatchingBSSIDs:]
+ -[WiFiAvailabilityNearbyCandidateNetwork matched]
+ -[WiFiAvailabilityNearbyCandidateNetwork password]
+ -[WiFiAvailabilityNearbyCandidateNetwork popularityScore]
+ -[WiFiAvailabilityNearbyCandidateNetwork qualityScore]
+ -[WiFiAvailabilityNearbyCandidateNetwork receivedFromDeviceName]
+ -[WiFiAvailabilityNearbyCandidateNetwork setMatched:]
+ -[WiFiAvailabilityNearbyCandidateNetwork setReceivedFromDeviceName:]
+ -[WiFiAvailabilityNearbyCandidateNetwork setSSID:]
+ -[WiFiAvailabilityNearbyCandidateNetwork source]
+ -[WiFiAvailabilityNearbyCandidateNetwork type]
+ -[WiFiAvailabilityNearbyCandidateNetwork venueGroup]
+ -[WiFiAvailabilityNearbyCandidateNetwork venueType]
+ -[WiFiAvailabilityNearbySource .cxx_destruct]
+ -[WiFiAvailabilityNearbySource changeHandler]
+ -[WiFiAvailabilityNearbySource recommendedNetworks]
+ -[WiFiAvailabilityNearbySource relevancyHandler]
+ -[WiFiAvailabilityNearbySource relevantNetworks]
+ -[WiFiAvailabilityNearbySource removalHandler]
+ -[WiFiAvailabilityNearbySource setChangeHandler:]
+ -[WiFiAvailabilityNearbySource setRecommendedNetworks:]
+ -[WiFiAvailabilityNearbySource setRelevancyHandler:]
+ -[WiFiAvailabilityNearbySource setRemovalHandler:]
+ -[WiFiDiagnosticReporter .cxx_destruct]
+ -[WiFiDiagnosticReporter SubmitDiagnosticSignatureLazy]
+ -[WiFiDiagnosticReporter initABCReporter]
+ -[WiFiDiagnosticReporter initABCReporter].cold.1
+ -[WiFiDiagnosticReporter init]
+ -[WiFiDiagnosticReporter submitWiFiWatchdogReason:subtypeContext:]
+ -[WiFiDiagnosticReporter submitWiFiWatchdogReason:subtypeContext:].cold.1
+ -[WiFiSoftError isRecommendedPriority]
+ -[WiFiSoftError updateHUDWithHost:messageDict:]
+ -[WiFiSoftError updateHUDWithHost:messageDict:].cold.1
+ -[WiFiSoftError updateHUDWithHost:messageDict:].cold.2
+ -[WiFiUsageBssDetails apProfileError]
+ -[WiFiUsageBssDetails setApProfileError:]
+ -[WiFiUsageLinkSession faultEventSoftError]
+ -[WiFiUsageLinkSession setFaultEventSoftError:]
+ -[WiFiUsageMonitor addFaultEvent:forInterface:at:]
+ -[WiFiUsageMonitor lqmDistributionSampling_store]
+ -[WiFiUsageMonitor lqmDistributionSampling_telemetry]
+ -[WiFiUsageMonitor setLqmDistributionSampling_store:]
+ -[WiFiUsageMonitor setLqmDistributionSampling_telemetry:]
+ -[WiFiUsageMonitor setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]
+ -[WiFiUsageMonitor submitBeaconInfoToCAForInterface:]
+ -[WiFiUsageMonitor submitBeaconInfoToCAForInterface:].cold.1
+ -[WiFiUsageParsedBeacon lastParsedOK]
+ -[WiFiUsageParsedBeacon parseBeaconIE:endOfBuffer:]
+ -[WiFiUsageParsedBeacon setLastParsedOK:]
+ -[WiFiUsagePoorLinkSession logUserImpactTimes]
+ -[WiFiUsagePoorLinkSession setTdSoftError:]
+ -[WiFiUsagePoorLinkSession setVote_FastTD_2GDataStall_Duration:]
+ -[WiFiUsagePoorLinkSession setVote_FastTD_2GPoorLink_Duration:]
+ -[WiFiUsagePoorLinkSession setVote_FastTD_HighLatency_Duration:]
+ -[WiFiUsagePoorLinkSession setVote_FastTD_InsufficientRxFrames_Duration:]
+ -[WiFiUsagePoorLinkSession tdSoftError]
+ -[WiFiUsagePoorLinkSession vote_FastTD_2GDataStall_Duration]
+ -[WiFiUsagePoorLinkSession vote_FastTD_2GPoorLink_Duration]
+ -[WiFiUsagePoorLinkSession vote_FastTD_HighLatency_Duration]
+ -[WiFiUsagePoorLinkSession vote_FastTD_InsufficientRxFrames_Duration]
+ -[WiFiUsageSession softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]
+ -[WiFiUsageSoftApSession idleTimeAfterLastClientDisconnectedSec]
+ -[WiFiUsageSoftApSession idleTimeBeforeTeardownSec]
+ -[WiFiUsageSoftApSession setIdleTimeAfterLastClientDisconnectedSec:]
+ -[WiFiUsageSoftApSession setIdleTimeBeforeTeardownSec:]
+ -[WiFiUsageSoftApSession softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]
+ -[WiFiWalletPass captiveTokenAuthURL]
+ -[WiFiWalletPass captiveToken]
+ -[WiFiWalletPass passTypeIdentifier]
+ -[WiFiWalletPass setCaptiveToken:]
+ -[WiFiWalletPass setCaptiveTokenAuthURL:]
+ -[WiFiWalletPass setPassTypeIdentifier:]
+ -[WiFiWalletSource _addPass:].cold.1
+ -[WiFiWalletSource _issueChangeCallbackWithPass:removedNetworks:]
+ -[WiFiWalletSource _issueRemovalCallbackWithPass:]
+ -[WiFiWalletSource _removePass:withSerialNumber:]
+ -[WiFiWalletSource _replacePass:]
+ -[WiFiWalletSource removalHandler]
+ -[WiFiWalletSource setRemovalHandler:]
+ GCC_except_table225
+ GCC_except_table36
+ GCC_except_table39
+ GCC_except_table44
+ GCC_except_table49
+ GCC_except_table55
+ GCC_except_table59
+ GCC_except_table63
+ GCC_except_table90
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_NSDecimalNumber
+ _OBJC_CLASS_$_WALQM
+ _OBJC_CLASS_$_WiFiAvailabilityNearbyCandidateNetwork
+ _OBJC_CLASS_$_WiFiAvailabilityNearbySource
+ _OBJC_CLASS_$_WiFiDiagnosticReporter
+ _OBJC_CLASS_$_WiFiUsageLQMDistributionConfiguration
+ _OBJC_IVAR_$_WCAFetchWiFiBehaviorParameters._lqmDistribution
+ _OBJC_IVAR_$_WFMeasureResult._backhaulULThroughput
+ _OBJC_IVAR_$_WFMeasureResult._uploadError
+ _OBJC_IVAR_$_WiFi3BarsSource.removalHandler
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.SSID
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.accessPoints
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.attributes
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.matched
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.password
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.popularityScore
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.qualityScore
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.receivedFromDeviceName
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.type
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.venueGroup
+ _OBJC_IVAR_$_WiFiAvailabilityNearbyCandidateNetwork.venueType
+ _OBJC_IVAR_$_WiFiAvailabilityNearbySource.changeHandler
+ _OBJC_IVAR_$_WiFiAvailabilityNearbySource.recommendedNetworks
+ _OBJC_IVAR_$_WiFiAvailabilityNearbySource.relevancyHandler
+ _OBJC_IVAR_$_WiFiAvailabilityNearbySource.removalHandler
+ _OBJC_IVAR_$_WiFiDiagnosticReporter._ABCReporter
+ _OBJC_IVAR_$_WiFiSoftError._isRecommendedPriority
+ _OBJC_IVAR_$_WiFiUsageBssDetails._apProfileError
+ _OBJC_IVAR_$_WiFiUsageLinkSession._faultCountOnBss
+ _OBJC_IVAR_$_WiFiUsageLinkSession._faultEventSoftError
+ _OBJC_IVAR_$_WiFiUsageMonitor._lqmDistributionSampling_store
+ _OBJC_IVAR_$_WiFiUsageMonitor._lqmDistributionSampling_telemetry
+ _OBJC_IVAR_$_WiFiUsageParsedBeacon._lastParsedOK
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._tdSoftError
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._vote_FastTD_2GDataStall_Duration
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._vote_FastTD_2GPoorLink_Duration
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._vote_FastTD_HighLatency_Duration
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._vote_FastTD_InsufficientRxFrames_Duration
+ _OBJC_IVAR_$_WiFiUsageSoftApSession._idleTimeAfterLastClientDisconnectedSec
+ _OBJC_IVAR_$_WiFiUsageSoftApSession._idleTimeBeforeTeardownSec
+ _OBJC_IVAR_$_WiFiWalletPass._captiveToken
+ _OBJC_IVAR_$_WiFiWalletPass._captiveTokenAuthURL
+ _OBJC_IVAR_$_WiFiWalletPass._passTypeIdentifier
+ _OBJC_IVAR_$_WiFiWalletSource.removalHandler
+ _OBJC_METACLASS_$_WiFiAvailabilityNearbyCandidateNetwork
+ _OBJC_METACLASS_$_WiFiAvailabilityNearbySource
+ _OBJC_METACLASS_$_WiFiDiagnosticReporter
+ _OBJC_METACLASS_$_WiFiUsageLQMDistributionConfiguration
+ _PKPassLibraryPassTypeIdentifierUserInfoKey
+ _PKPassLibraryRemovedPassInfosUserInfoKey
+ _PKPassLibrarySerialNumberUserInfoKey
+ _PKPassSemanticWifiAccessStringKeyCaptiveToken
+ _PKPassSemanticWifiAccessStringKeyCaptiveTokenAuthURL
+ _SDRDiagnosticReporterFunction
+ _SymptomDiagnosticReporterLibrary.sLib
+ _SymptomDiagnosticReporterLibrary.sOnce
+ _WALogCategoryDeviceStoreHandle
+ __OBJC_$_CLASS_METHODS_WiFiDiagnosticReporter
+ __OBJC_$_CLASS_METHODS_WiFiUsageLQMDistributionConfiguration
+ __OBJC_$_INSTANCE_METHODS_WiFiAvailabilityNearbyCandidateNetwork
+ __OBJC_$_INSTANCE_METHODS_WiFiAvailabilityNearbySource
+ __OBJC_$_INSTANCE_METHODS_WiFiDiagnosticReporter
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAvailabilityNearbyCandidateNetwork
+ __OBJC_$_INSTANCE_VARIABLES_WiFiAvailabilityNearbySource
+ __OBJC_$_INSTANCE_VARIABLES_WiFiDiagnosticReporter
+ __OBJC_$_PROP_LIST_WiFiAvailabilityNearbyCandidateNetwork
+ __OBJC_$_PROP_LIST_WiFiAvailabilityNearbySource
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAvailabilityNearbyCandidateNetwork
+ __OBJC_CLASS_PROTOCOLS_$_WiFiAvailabilityNearbySource
+ __OBJC_CLASS_RO_$_WiFiAvailabilityNearbyCandidateNetwork
+ __OBJC_CLASS_RO_$_WiFiAvailabilityNearbySource
+ __OBJC_CLASS_RO_$_WiFiDiagnosticReporter
+ __OBJC_CLASS_RO_$_WiFiUsageLQMDistributionConfiguration
+ __OBJC_METACLASS_RO_$_WiFiAvailabilityNearbyCandidateNetwork
+ __OBJC_METACLASS_RO_$_WiFiAvailabilityNearbySource
+ __OBJC_METACLASS_RO_$_WiFiDiagnosticReporter
+ __OBJC_METACLASS_RO_$_WiFiUsageLQMDistributionConfiguration
+ __WiFiWalletSourcePassContainsWiFiSemantics
+ __ZNSt12length_errorC1B8ne200100EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8ne200100Ev
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne200100Ej
+ __ZNSt3__116__pad_and_outputB8ne200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocate_at_leastB8ne200100INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne200100Ev
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED2Ev
+ __ZNSt3__120__throw_length_errorB8ne200100EPKc
+ __ZNSt3__124__put_character_sequenceB8ne200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__tree_balance_after_insertB8ne200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB8ne200100Ev
+ __ZSt28__throw_bad_array_new_lengthB8ne200100v
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZnwmSt19__type_descriptor_t
+ ___24-[WiFiUsageMonitor init]_block_invoke.256
+ ___24-[WiFiUsageMonitor init]_block_invoke.260
+ ___249-[WiFiUsageMonitor setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]_block_invoke
+ ___29-[WiFiSoftError submitMetric]_block_invoke.79
+ ___30-[WFMeasure dispatchPingTest:]_block_invoke.411
+ ___31-[WFMeasure doULThroughputTest]_block_invoke
+ ___31-[WFMeasure doULThroughputTest]_block_invoke_2
+ ___31-[WFMeasure doULThroughputTest]_block_invoke_3
+ ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.687
+ ___37-[WFMeasure dispatchULThroughputTest]_block_invoke
+ ___38-[WiFiSoftError submitMetricWithData:]_block_invoke.82
+ ___40-[WiFiSoftError initWithName:andParams:]_block_invoke.48
+ ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke
+ ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.124
+ ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.124.cold.1
+ ___48-[WiFiAvailabilityEngine _setupSourceCallbacks:]_block_invoke_3
+ ___48-[WiFiAvailabilityEngine _setupSourceCallbacks:]_block_invoke_4
+ ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.92
+ ___50+[WiFiUsageAccessPointProfile submitToCAForBSSID:]_block_invoke
+ ___50-[WiFiUsageMonitor addFaultEvent:forInterface:at:]_block_invoke
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.146
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.146.cold.1
+ ___54+[WiFiDiagnosticReporter sharedWiFiDiagnosticReporter]_block_invoke
+ ___62-[WiFiAvailabilityEngine findRecommendationForScannedNetwork:]_block_invoke
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.354
+ ___66-[WiFiDiagnosticReporter submitWiFiWatchdogReason:subtypeContext:]_block_invoke
+ ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.279
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.744
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.755
+ ___SymptomDiagnosticReporterLibrary_block_invoke
+ ___block_descriptor_117_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_32_e57_q24?0"WiFiAvailabilityMatch"8"WiFiAvailabilityMatch"16l
+ ___block_descriptor_40_e8_32w_e15_v16?0"NSSet"8lw32l8
+ ___block_descriptor_49_e8_32s40w_e34_v24?0"NSDictionary"8"NSArray"16lw40l8s32l8
+ ___block_descriptor_49_e8_32s40w_e37_v24?0"NPTMetricResult"8"NSError"16lw40l8s32l8
+ ___block_descriptor_68_e8_32s40s48s56r_e5_v8?0ls32l8r56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_92_e8_32s40s48s56s64s72s80s_e41_v16?0"WADeviceAnalyticsLinkTestRecord"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.101
+ ___block_literal_global.197
+ ___block_literal_global.22
+ ___block_literal_global.243
+ ___block_literal_global.262
+ ___block_literal_global.51
+ ___block_literal_global.747
+ ___block_literal_global.758
+ ___block_literal_global.760
+ ___block_literal_global.762
+ __lqmDistribution
+ _classSDRDiagnosticReporter
+ _dlopen
+ _getSDRDiagnosticReporterClass
+ _initSDRDiagnosticReporter
+ _initSDRDiagnosticReporter.cold.1
+ _kWiFiUsageAccessPointProfileBeaconInfoParsingErrorAfter
+ _kWiFiUsageAccessPointProfileEventName
+ _objc_msgSend$_handleWalletChange:removed:
+ _objc_msgSend$_handleWalletRemoval:
+ _objc_msgSend$_isProfileValidForUse:withCachedDict:onlyIfCurrent:withError:
+ _objc_msgSend$_isProfileValidForUse:withCachedDict:withError:
+ _objc_msgSend$_issueChangeCallbackWithPass:removedNetworks:
+ _objc_msgSend$_issueRemovalCallbackWithPass:
+ _objc_msgSend$_loadFromUserDefaults:withKey:withCachedData:withError:
+ _objc_msgSend$_removePass:withSerialNumber:
+ _objc_msgSend$_replacePass:
+ _objc_msgSend$_updateHUDWithHost:messageDict:
+ _objc_msgSend$addFaultEvent:forInterface:at:
+ _objc_msgSend$canPerformActionWithRawSampleRate:
+ _objc_msgSend$captiveToken
+ _objc_msgSend$decimalNumberWithDecimal:
+ _objc_msgSend$decimalValue
+ _objc_msgSend$dispatchULThroughputTest
+ _objc_msgSend$doULThroughputTest
+ _objc_msgSend$errorStringForTelemetry:
+ _objc_msgSend$faultEventOn:at:type:interface:
+ _objc_msgSend$initABCReporter
+ _objc_msgSend$initializePerformanceTest
+ _objc_msgSend$isCarPlay
+ _objc_msgSend$lastParsedOK
+ _objc_msgSend$linkTestEventOn:at:with:
+ _objc_msgSend$logUserImpactTimes
+ _objc_msgSend$lqmDistribution
+ _objc_msgSend$lqmEvent:on:at:
+ _objc_msgSend$parseBeaconIE:endOfBuffer:
+ _objc_msgSend$passTypeIdentifier
+ _objc_msgSend$profileForBSSID:onlyIfCurrent:withError:
+ _objc_msgSend$profileForBSSID:withError:
+ _objc_msgSend$queryItemWithName:value:
+ _objc_msgSend$receivedFromDeviceName
+ _objc_msgSend$recommendedNetworks
+ _objc_msgSend$removalHandler
+ _objc_msgSend$scalingFactorForRawSampleRate:
+ _objc_msgSend$setApProfileError:
+ _objc_msgSend$setBackhaulULThroughput:
+ _objc_msgSend$setBadDNSServers:
+ _objc_msgSend$setBadGateway:
+ _objc_msgSend$setCaptiveToken:
+ _objc_msgSend$setCaptiveTokenAuthURL:
+ _objc_msgSend$setChangeHandler:
+ _objc_msgSend$setFoundCriticalFailure:
+ _objc_msgSend$setIdleTimeAfterLastClientDisconnectedSec:
+ _objc_msgSend$setIdleTimeBeforeTeardownSec:
+ _objc_msgSend$setInitiatingReason:
+ _objc_msgSend$setIsTriggeredByFault:
+ _objc_msgSend$setLqmDistribution:
+ _objc_msgSend$setPassTypeIdentifier:
+ _objc_msgSend$setReceivedFromDeviceName:
+ _objc_msgSend$setRemovalHandler:
+ _objc_msgSend$setStatusForDNS:
+ _objc_msgSend$setStatusForInternet:
+ _objc_msgSend$setStatusForLocal:
+ _objc_msgSend$setStatusForSiriTCP:
+ _objc_msgSend$setStatusForSiriTLS:
+ _objc_msgSend$setUploadError:
+ _objc_msgSend$setUploadSize:
+ _objc_msgSend$setVote_FastTD_2GDataStall_Duration:
+ _objc_msgSend$setVote_FastTD_2GPoorLink_Duration:
+ _objc_msgSend$setVote_FastTD_HighLatency_Duration:
+ _objc_msgSend$setVote_FastTD_InsufficientRxFrames_Duration:
+ _objc_msgSend$sharedWiFiDiagnosticReporter
+ _objc_msgSend$snapshotWithSignature:delay:events:payload:actions:reply:
+ _objc_msgSend$softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:
+ _objc_msgSend$sortDescriptorWithKey:ascending:comparator:
+ _objc_msgSend$startUploadWithCompletion:
+ _objc_msgSend$submitToCAForBSSID:
+ _objc_msgSend$submitWiFiWatchdogReason:subtypeContext:
+ _objc_msgSend$updateHUDWithHost:messageDict:
+ _objc_msgSend$vote_FastTD_2GDataStall_Duration
+ _objc_msgSend$vote_FastTD_2GPoorLink_Duration
+ _objc_msgSend$vote_FastTD_HighLatency_Duration
+ _objc_msgSend$vote_FastTD_InsufficientRxFrames_Duration
+ _objc_msgSend$waBandFromBand:
+ _objc_msgSend$waLQMonChannel:band:rssi:noise:snr:totalCCA:selfCca:otherCca:interference:beaconPer:rxFrames:rxRetryFrames:txFrames:txRetries:txFail:txRate:rxRate:isAnyAppInFG:isFTactive:isTimeSensitiveAppRunning:duration:
+ _sharedWiFiDiagnosticReporter.onceToken
+ _sharedWiFiDiagnosticReporter.sharedWiFiDiagnosticReporter
- +[WFMeasure isOnSupportedPlatform]
- +[WiFiSoftError _updateHUDWithMessage:].cold.1
- +[WiFiSoftError _updateHUDWithMessage:].cold.2
- +[WiFiSoftError _updateHUDWithMessage:].cold.3
- +[WiFiUsageAccessPointProfile _isProfileValidForUse:withCachedDict:]
- +[WiFiUsageAccessPointProfile _isProfileValidForUse:withCachedDict:onlyIfCurrent:]
- +[WiFiUsageAccessPointProfile longProfileForBSSID:]
- +[WiFiUsageAccessPointProfile profileForBSSID:onlyIfCurrent:]
- +[WiFiUsageAccessPointProfile shortProfileForBSSID:]
- -[TBRemoteDataSource init].cold.1
- -[TBRemoteDataSource init].cold.2
- -[WiFiSoftError updateHUDWithMessage:].cold.1
- -[WiFiUsageMonitor sendFaultToDB:]
- -[WiFiUsageMonitor setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:]
- -[WiFiUsageParsedBeacon parseBeaconIE:length:endOfBuffer:]
- -[WiFiUsageSession softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:]
- -[WiFiUsageSoftApSession softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:]
- GCC_except_table224
- GCC_except_table42
- GCC_except_table43
- GCC_except_table52
- GCC_except_table56
- GCC_except_table89
- _OBJC_CLASS_$_WAMessage
- _WADeviceAnalyticsLinkTestInfo
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
- __ZNKSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
- __ZNSt12length_errorC1B8ne190102EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEED1Ev
- __ZNSt3__120__throw_length_errorB8ne190102EPKc
- __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZSt28__throw_bad_array_new_lengthB8ne190102v
- __Znwm
- ___184-[WiFiUsageMonitor setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:]_block_invoke
- ___24-[WiFiUsageMonitor init]_block_invoke.251
- ___24-[WiFiUsageMonitor init]_block_invoke.255
- ___29-[WiFiSoftError submitMetric]_block_invoke.76
- ___30-[WFMeasure dispatchPingTest:]_block_invoke.392
- ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.674
- ___38-[WiFiSoftError submitMetricWithData:]_block_invoke.79
- ___38-[WiFiSoftError updateHUDWithMessage:]_block_invoke
- ___38-[WiFiSoftError updateHUDWithMessage:]_block_invoke.114
- ___38-[WiFiSoftError updateHUDWithMessage:]_block_invoke.114.cold.1
- ___40-[WiFiSoftError initWithName:andParams:]_block_invoke.45
- ___47-[WiFiUsageMonitor addFaultEvent:forInterface:]_block_invoke
- ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.89
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.130
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.130.cold.1
- ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.274
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.730
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.741
- ___block_descriptor_101_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_60_e8_32s40s48r_e5_v8?0ls32l8r48l8s40l8
- ___block_literal_global.192
- ___block_literal_global.238
- ___block_literal_global.257
- ___block_literal_global.48
- ___block_literal_global.733
- ___block_literal_global.744
- ___block_literal_global.746
- ___block_literal_global.748
- ___block_literal_global.98
- ___stderrp
- _fprintf
- _kWAMessageKeyBSSID
- _kWAMessageKeyFaultDate
- _kWAMessageKeyFaultInterface
- _kWAMessageKeyFaultName
- _kWAMessageKeySSID
- _kWAMessageMetricNameFault
- _objc_msgSend$_isProfileValidForUse:withCachedDict:
- _objc_msgSend$_isProfileValidForUse:withCachedDict:onlyIfCurrent:
- _objc_msgSend$addFaultEvent:forInterface:
- _objc_msgSend$initWithName:value:
- _objc_msgSend$parseBeaconIE:length:endOfBuffer:
- _objc_msgSend$processWAMessageMetric:data:
- _objc_msgSend$profileForBSSID:
- _objc_msgSend$profileForBSSID:onlyIfCurrent:
- _objc_msgSend$pushTDEventToHUD:
- _objc_msgSend$releaseBackgroundProcessingMOC
- _objc_msgSend$sendFaultToDB:
- _objc_msgSend$softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:
CStrings:
+ "\t"
+ " reasonString=%@"
+ " subreason=0x%x"
+ " subreasonString=%@"
+ "%s - Cannot start WiFiUsageLQMWindowAnalysis for %@(%@) (max number of concurrent analysis (%lu) reached: %u)"
+ "%s: %@ (%@) is not a number"
+ "%s: ABC snapshotWithSignature signature: %@"
+ "%s: Element %hhu is invalid"
+ "%s: Element %hhu is invalid:%@"
+ "%s: Element %hhu_%hhu is invalid"
+ "%s: Element %u_%hhu is invalid:%@"
+ "%s: HUD UI preference is set to Recommended, but this softerror is not allowed."
+ "%s: LQM-WiFi: Upload task completed, uploaded %llu bytes in %f seconds, throughput %f Mbps"
+ "%s: Metadata task starting..."
+ "%s: Received LQMDistribution config from Mobile Assets"
+ "%s: Upload task errored out (%@)"
+ "%s: Upload task exited without running"
+ "%s: Upload task starting..."
+ "%s: Upload task will run"
+ "%s: _ABCReporter failing to init, skipping submitting reasonString: %@ \n"
+ "%s: initABCReporter already exists \n"
+ "%s: profile for bssid %@ doesn't exist"
+ "%s: profile for bssid %@ is %s sent to CA"
+ "%s: profile for bssid %@ is not valid"
+ "%s: reached end of IE before parsing extended IE Type"
+ "%s: reached end of buffer while parsing IE %hhu before parsing IE content (ieLength:%hhu IE content:(%p + %hhu = %p) > %p)"
+ "%s: reached end of buffer while parsing IE %hhu before parsing length ((%p + %zu = %p) > %p)"
+ "%s: reasonString: %@ ABC snapshot response: %@"
+ "%s: removed wallet networks: %@, added wallet networks: %@"
+ "%s: submitting CA metric %@ : %@"
+ "%s: top match %@ for network %@"
+ "%s: tried to isssue callback without added and removed networks"
+ "%s: tried to isssue callback without removed networks"
+ "%s: unable to learn currentBSSID (ParsedIE:%@ bssid:%@)"
+ "%s: wallet networks that have been removed: %@"
+ "%{public}s::%d:%s: Saving linkTest in DeviceStore: %@"
+ "+[WiFiUsageAccessPointProfile _isProfileValidForUse:withCachedDict:onlyIfCurrent:withError:]"
+ "+[WiFiUsageAccessPointProfile _loadFromUserDefaults:withKey:withCachedData:withError:]"
+ "+[WiFiUsageAccessPointProfile submitToCAForBSSID:]"
+ "+[WiFiUsageLQMDistributionConfiguration getConfigForKey:]"
+ "+[WiFiUsageLQMDistributionConfiguration setConfig:]"
+ "-[WFMeasure doULThroughputTest]"
+ "-[WFMeasure doULThroughputTest]_block_invoke"
+ "-[WFMeasure doULThroughputTest]_block_invoke_2"
+ "-[WFMeasure initializePerformanceTest]"
+ "-[WiFiAvailabilityEngine _handleWalletChange:removed:]"
+ "-[WiFiAvailabilityEngine _handleWalletRemoval:]"
+ "-[WiFiDiagnosticReporter initABCReporter]"
+ "-[WiFiDiagnosticReporter submitWiFiWatchdogReason:subtypeContext:]"
+ "-[WiFiDiagnosticReporter submitWiFiWatchdogReason:subtypeContext:]_block_invoke"
+ "-[WiFiSoftError updateHUDWithHost:messageDict:]"
+ "-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke"
+ "-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke_2"
+ "-[WiFiUsageMonitor addFaultEvent:forInterface:at:]_block_invoke"
+ "-[WiFiUsageMonitor submitBeaconInfoToCAForInterface:]"
+ "-[WiFiUsageParsedBeacon parseBeaconIE:endOfBuffer:]"
+ "-[WiFiUsagePoorLinkSession logUserImpactTimes]"
+ "-[WiFiUsageSoftApSession softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:]"
+ "-[WiFiWalletSource _issueChangeCallbackWithPass:removedNetworks:]"
+ "-[WiFiWalletSource _issueRemovalCallbackWithPass:]"
+ "-[WiFiWalletSource _replacePass:]"
+ "/System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter"
+ "2GDataStall & "
+ "2GPoorLink & "
+ "@32@0:8@16^@24"
+ "@36@0:8@16B24^@28"
+ "@40@0:8{?=QBBBBBBBBBB}16"
+ "@48@0:8@16@24@32^@40"
+ "@?<v@?@\"NSSet\">16@0:8"
+ "B32@0:8*16*24"
+ "B40@0:8@16@24^@32"
+ "B44@0:8@16@24B32^@36"
+ "Backhaul:DL-Tput:(%d)mbps Error:(%@) "
+ "Backhaul:UL-Tput:(%d)mbps Error:(%@) "
+ "Captive network: %@ "
+ "DebugCommand"
+ "FaultEvent"
+ "HighLatency & "
+ "IE value %d"
+ "IdleTimeAfterLastClientDisconnectedSec"
+ "IdleTimeBeforeTeardownSec"
+ "InsufficientRxFrames & "
+ "LQMDistribution"
+ "Len value of IE %d"
+ "Never"
+ "Parsing Failed. Last Parsed: %@"
+ "Payload value of IE %d_%@"
+ "Payload value of IE %hhu"
+ "Payload value of IE %hhu_%hhu"
+ "Primary Not Set"
+ "Recommended"
+ "RecommendedSoftError"
+ "SDRDiagnosticReporter"
+ "SharingSilentRepair"
+ "SubmitDiagnosticSignatureLazy"
+ "T@\"NSArray\",C,VrecommendedNetworks"
+ "T@\"NSDictionary\",&,N,V_lqmDistribution"
+ "T@\"NSError\",C,N,V_apProfileError"
+ "T@\"NSError\",C,N,V_uploadError"
+ "T@\"NSNumber\",&,V_lqmDistributionSampling_store"
+ "T@\"NSNumber\",&,V_lqmDistributionSampling_telemetry"
+ "T@\"NSString\",&,N,V_lastParsedOK"
+ "T@\"NSString\",C,N,V_captiveToken"
+ "T@\"NSString\",C,N,V_captiveTokenAuthURL"
+ "T@\"NSString\",C,N,V_passTypeIdentifier"
+ "T@\"NSString\",C,N,VreceivedFromDeviceName"
+ "T@\"WiFiSoftError\",&,N,V_faultEventSoftError"
+ "T@?,C,N,VremovalHandler"
+ "TB,R,N,V_isRecommendedPriority"
+ "TD_VoteFastTD_2GDataStall"
+ "TD_VoteFastTD_2GDataStall_PercTDEvalDuration"
+ "TD_VoteFastTD_2GPoorLink"
+ "TD_VoteFastTD_2GPoorLink_PercTDEvalDuration"
+ "TD_VoteFastTD_HighLatency"
+ "TD_VoteFastTD_HighLatency_PercTDEvalDuration"
+ "TD_VoteFastTD_InsufficientRxFrames"
+ "TD_VoteFastTD_InsufficientRxFrames_PercTDEvalDuration"
+ "TQ,N,V_lastRoamScanContainsRoamCandidateCount"
+ "Td,N,V_backhaulULThroughput"
+ "Td,N,V_idleTimeAfterLastClientDisconnectedSec"
+ "Td,N,V_idleTimeBeforeTeardownSec"
+ "Td,N,V_vote_FastTD_2GDataStall_Duration"
+ "Td,N,V_vote_FastTD_2GPoorLink_Duration"
+ "Td,N,V_vote_FastTD_HighLatency_Duration"
+ "Td,N,V_vote_FastTD_InsufficientRxFrames_Duration"
+ "Ti,N,V_siriTrafficClass"
+ "Ti,N,V_tclass"
+ "T{?=QBBBBBBBBBB},N,V_last_FastTdVotes"
+ "WUAPProfile"
+ "WUAPProfileErrorMinAssocTimeNotMet"
+ "WUAPProfileErrorMinOccurrencesNotMet"
+ "WUAPProfileErrorPreInit"
+ "WUAPProfileErrorProfileNotCurrent"
+ "WalletPassCaptivePortal"
+ "WiFi Watchdog"
+ "WiFiAvailabilityNearbyCandidateNetwork"
+ "WiFiAvailabilityNearbySource"
+ "WiFiDiagnosticReporter"
+ "WiFiUsageLQMDistributionConfiguration"
+ "[1036Q]"
+ "[36Q]"
+ "[HUD]: ignoring empty HUD message dict info"
+ "_ABCReporter"
+ "_apProfileError"
+ "_backhaulULThroughput"
+ "_captiveToken"
+ "_captiveTokenAuthURL"
+ "_faultCountOnBss"
+ "_faultEventSoftError"
+ "_handleWalletChange:removed:"
+ "_handleWalletRemoval:"
+ "_idleTimeAfterLastClientDisconnectedSec"
+ "_idleTimeBeforeTeardownSec"
+ "_isProfileValidForUse:withCachedDict:onlyIfCurrent:withError:"
+ "_isProfileValidForUse:withCachedDict:withError:"
+ "_isRecommendedPriority"
+ "_issueChangeCallbackWithPass:removedNetworks:"
+ "_issueRemovalCallbackWithPass:"
+ "_lastParsedOK"
+ "_loadFromUserDefaults:withKey:withCachedData:withError:"
+ "_lqmDistribution"
+ "_lqmDistributionSampling_store"
+ "_lqmDistributionSampling_telemetry"
+ "_passTypeIdentifier"
+ "_removePass:withSerialNumber:"
+ "_replacePass:"
+ "_updateHUDWithHost:messageDict:"
+ "_uploadError"
+ "_vote_FastTD_2GDataStall_Duration"
+ "_vote_FastTD_2GPoorLink_Duration"
+ "_vote_FastTD_HighLatency_Duration"
+ "_vote_FastTD_InsufficientRxFrames_Duration"
+ "addFaultEvent:forInterface:at:"
+ "already sent"
+ "analyticsStoreSampling"
+ "apProfileBeaconInfoParsingErrorAfter"
+ "apProfileError"
+ "backhaulULThroughput"
+ "canPerformActionWithRawSampleRate:"
+ "captiveToken"
+ "captiveTokenAuthURL"
+ "com.apple.wifi.policy.approfile"
+ "decimalNumberWithDecimal:"
+ "decimalValue"
+ "dispatchULThroughputTest"
+ "doULThroughputTest"
+ "errorStringForTelemetry:"
+ "fastTD (RTApp:%@ Cheap5G:%@) votes:%lu %@%@%@%@%@%@%@%@"
+ "faultEventOn:at:type:interface:"
+ "faultEventSoftError"
+ "idleTimeAfterLastClientDisconnectedSec"
+ "idleTimeBeforeTeardownSec"
+ "initABCReporter"
+ "initializePerformanceTest"
+ "isRecommendedPriority"
+ "kWiFiUsageFaultReasonPrimarySetFailure"
+ "lastParsedOK"
+ "linkTestEventOn:at:with:"
+ "logUserImpactTimes"
+ "longProfileForBSSID:withError:"
+ "lqmDistribution"
+ "lqmDistributionSampling_store"
+ "lqmDistributionSampling_telemetry"
+ "lqmEvent:on:at:"
+ "metricPrefix set to '%@' ; cdfMetricName set to '%@' ; sankeyMetricName set to '%@' ; maxConcurrentAnalysis set to %u\nLikelyhood of creating an analysis: %@\nLikelyhood of sending analysis to CA: %@\nKernel window parsing enabled: %@ %@\nInCall LQMAnalysis enabled: %@ %@"
+ "nil"
+ "not nil"
+ "not yet"
+ "parseBeaconIE:endOfBuffer:"
+ "passTypeIdentifier"
+ "profileForBSSID:onlyIfCurrent:withError:"
+ "profileForBSSID:withError:"
+ "q24@?0@\"WiFiAvailabilityMatch\"8@\"WiFiAvailabilityMatch\"16"
+ "queryItemWithName:value:"
+ "reason=0x%x"
+ "receivedFromDeviceName"
+ "recommendedNetworks"
+ "removalHandler"
+ "r\xf0\xa2"
+ "s20@0:8i16"
+ "scalingFactorForRawSampleRate:"
+ "setApProfileError:"
+ "setBackhaulULThroughput:"
+ "setBadDNSServers:"
+ "setBadGateway:"
+ "setCaptiveToken:"
+ "setCaptiveTokenAuthURL:"
+ "setFaultEventSoftError:"
+ "setFoundCriticalFailure:"
+ "setIdleTimeAfterLastClientDisconnectedSec:"
+ "setIdleTimeBeforeTeardownSec:"
+ "setInitiatingReason:"
+ "setIsTriggeredByFault:"
+ "setLastParsedOK:"
+ "setLqmDistribution:"
+ "setLqmDistributionSampling_store:"
+ "setLqmDistributionSampling_telemetry:"
+ "setPassTypeIdentifier:"
+ "setReceivedFromDeviceName:"
+ "setRecommendedNetworks:"
+ "setRemovalHandler:"
+ "setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:"
+ "setStatusForDNS:"
+ "setStatusForInternet:"
+ "setStatusForLocal:"
+ "setStatusForSiriTCP:"
+ "setStatusForSiriTLS:"
+ "setUploadError:"
+ "setUploadSize:"
+ "setVote_FastTD_2GDataStall_Duration:"
+ "setVote_FastTD_2GPoorLink_Duration:"
+ "setVote_FastTD_HighLatency_Duration:"
+ "setVote_FastTD_InsufficientRxFrames_Duration:"
+ "sharedWiFiDiagnosticReporter"
+ "shortProfileForBSSID:withError:"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:"
+ "sortDescriptorWithKey:ascending:comparator:"
+ "startUploadWithCompletion:"
+ "submitBeaconInfoToCAForInterface:"
+ "submitToCAForBSSID:"
+ "submitWiFiWatchdogReason:subtypeContext:"
+ "supportsLinkRecoveryTests"
+ "telemetrySampling"
+ "triggerDisc"
+ "updateHUDWithHost:messageDict:"
+ "uplinkThroughputTest"
+ "uploadError"
+ "v108@0:8B16@20@28@36Q44Q52B60B64B68d72B80d84d92d100"
+ "v16@?0@\"NSSet\"8"
+ "v16@?0@\"WADeviceAnalyticsLinkTestRecord\"8"
+ "v24@0:8@?<v@?@\"NSSet\">16"
+ "v40@0:8Q16@24@32"
+ "v40@0:8{?=QBBBBBBBBBB}16"
+ "v48@0:8{?=QBBBBBBBBBB}16@40"
+ "vote_FastTD_2GDataStall_Duration"
+ "vote_FastTD_2GPoorLink_Duration"
+ "vote_FastTD_HighLatency_Duration"
+ "vote_FastTD_InsufficientRxFrames_Duration"
+ "waBandFromBand:"
+ "waLQMonChannel:band:rssi:noise:snr:totalCCA:selfCca:otherCca:interference:beaconPer:rxFrames:rxRetryFrames:txFrames:txRetries:txFail:txRate:rxRate:isAnyAppInFG:isFTactive:isTimeSensitiveAppRunning:duration:"
+ "{?=\"fastTD_voteCount\"Q\"fastTD_vote_recommendation\"B\"fastTD_vote_TxPER\"B\"fastTD_vote_BeaconPER\"B\"fastTD_vote_FWTxPER\"B\"fastTD_vote_HighLatency\"B\"fastTD_vote_2GPoorLink\"B\"fastTD_vote_2GDataStall\"B\"fastTD_vote_InsufficientRxFrames\"B\"fastTD_RTApp\"B\"fastTD_Cheap5G\"B}"
+ "{?=QBBBBBBBBBB}16@0:8"
+ "\x81:"
- "%s - Cannot start WiFiUsageLQMWindowAnalysis for %@ (max number of concurrent analysis (%lu) reached: %u)"
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
- "%s: Download Metadata task starting..."
- "%s: Element %u is invalid:%@"
- "%s: Element %u_%u is invalid:%@"
- "%s: Sending linkTest to DeviceStore: %@"
- "%s: reached end of buffer before parsing IE type (length:%lu IE content:(%p + %lu = %p) > %p)"
- "%s: reached end of buffer while parsing IE %u before parsing IE content (length:%hhu IE content:(%p + %u = %p) > %p)"
- "%s: reached end of buffer while parsing IE %u before parsing length ((%p + %lu = %p) > %p)"
- "(locationAge <=0)"
- "+[WiFiUsageAccessPointProfile _isProfileValidForUse:withCachedDict:onlyIfCurrent:]"
- "+[WiFiUsageAccessPointProfile _loadFromUserDefaults:withKey:withCachedData:]"
- "-[WiFiSoftError updateHUDWithMessage:]"
- "-[WiFiSoftError updateHUDWithMessage:]_block_invoke"
- "-[WiFiUsageMonitor addFaultEvent:forInterface:]_block_invoke"
- "-[WiFiUsageParsedBeacon parseBeaconIE:length:endOfBuffer:]"
- "-[WiFiUsageParsedBeacon parseSSID:length:endOfBuffer:]"
- "-[WiFiUsageSoftApSession softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:]"
- "/Library/Caches/com.apple.xbs/Sources/WiFiPolicy/frameworks/Sources/ThreeBars/Data Sources/TBRemoteDataSource.m"
- "/Library/Caches/com.apple.xbs/Sources/WiFiPolicy/frameworks/Sources/WiFiLocationServices/WiFiLocationManager.m"
- "@32@0:8{?=QBBBBBB}16"
- "AssertMacros: %s, %s file: %s, line: %d, value: %lld\n"
- "B36@0:8@16@24B32"
- "Backhaul:Tput:(%d)mbps Error:(%@) "
- "Q\xf0\xb2"
- "TB,N,V_lastRoamScanContainsRoamCandidateCount"
- "TD evaluation complete: disconnected the link"
- "TI,N,V_tclass"
- "Tq,N,V_siriTrafficClass"
- "T{?=QBBBBBB},N,V_last_FastTdVotes"
- "[1035Q]"
- "[35Q]"
- "[HUD]: ignoring empty HUD message info"
- "_isProfileValidForUse:withCachedDict:"
- "_isProfileValidForUse:withCachedDict:onlyIfCurrent:"
- "fastTD (RTApp:%@ Cheap5G:%@) votes:%lu %@%@%@%@"
- "initWithName:value:"
- "isOnSupportedPlatform"
- "longProfileForBSSID:"
- "metricPrefix set to '%@' ; cdfMetricName set to '%@' ; sankeyMetricName set to '%@' ; maxConcurrentAnalysis set to %u\nLikelyhood of creating an analsyis: %@\nLikelyhood of sending analsyis to CA: %@\nKernel window parsing enabled: %@ %@\nInCall LQMAnalysis enabled: %@ %@"
- "parseBeaconIE:length:endOfBuffer:"
- "processWAMessageMetric:data:"
- "profileForBSSID:onlyIfCurrent:"
- "q:"
- "releaseBackgroundProcessingMOC"
- "sendFaultToDB:"
- "setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:"
- "shortProfileForBSSID:"
- "softApStateDidChange:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:"
- "v32@0:8{?=QBBBBBB}16"
- "v40@0:8{?=QBBBBBB}16@32"
- "v92@0:8B16@20@28@36Q44Q52B60B64B68d72B80d84"
- "{?=\"fastTD_voteCount\"Q\"fastTD_vote_recommendation\"B\"fastTD_vote_TxPER\"B\"fastTD_vote_BeaconPER\"B\"fastTD_vote_FWTxPER\"B\"fastTD_RTApp\"B\"fastTD_Cheap5G\"B}"
- "{?=QBBBBBB}16@0:8"

```
