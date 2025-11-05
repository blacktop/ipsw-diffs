## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/Versions/A/WiFiPolicy`

```diff

-885.4.0.0.0
-  __TEXT.__text: 0xbf0c4
-  __TEXT.__auth_stubs: 0x12a0
-  __TEXT.__objc_methlist: 0xffb0
-  __TEXT.__const: 0x638
-  __TEXT.__cstring: 0x1a9aa
-  __TEXT.__oslogstring: 0x3482
-  __TEXT.__gcc_except_tab: 0x1794
-  __TEXT.__unwind_info: 0x2020
-  __TEXT.__objc_classname: 0x1359
-  __TEXT.__objc_methname: 0x3033d
-  __TEXT.__objc_methtype: 0x39c3
-  __TEXT.__objc_stubs: 0x16e40
+925.30.0.0.0
+  __TEXT.__text: 0xc392c
+  __TEXT.__auth_stubs: 0x12d0
+  __TEXT.__objc_methlist: 0x110a8
+  __TEXT.__const: 0x628
+  __TEXT.__cstring: 0x1b514
+  __TEXT.__oslogstring: 0x3559
+  __TEXT.__gcc_except_tab: 0x17a0
+  __TEXT.__unwind_info: 0x20d0
+  __TEXT.__objc_classname: 0x1378
+  __TEXT.__objc_methname: 0x3155f
+  __TEXT.__objc_methtype: 0x39f7
+  __TEXT.__objc_stubs: 0x179e0
   __DATA_CONST.__got: 0x9e0
-  __DATA_CONST.__const: 0xb58
-  __DATA_CONST.__objc_classlist: 0x508
+  __DATA_CONST.__const: 0xb98
+  __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9000
+  __DATA_CONST.__objc_selrefs: 0x95d8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x428
+  __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0xa58
-  __AUTH_CONST.__auth_got: 0x968
+  __AUTH_CONST.__auth_got: 0x980
   __AUTH_CONST.__const: 0x1ba0
-  __AUTH_CONST.__cfstring: 0x17b20
-  __AUTH_CONST.__objc_const: 0x21600
-  __AUTH_CONST.__objc_intobj: 0x16e0
+  __AUTH_CONST.__cfstring: 0x18460
+  __AUTH_CONST.__objc_const: 0x20a88
+  __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x31b0
-  __DATA.__objc_ivar: 0x1fa0
+  __AUTH.__objc_data: 0x3200
+  __DATA.__objc_ivar: 0x208c
   __DATA.__data: 0x1bc0
   __DATA.__bss: 0x263
   __DATA.__common: 0x20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3759F5BB-CA56-3121-B52F-3D19630F3F99
-  Functions: 5823
-  Symbols:   13140
-  CStrings:  15761
+  UUID: 8188FF89-7169-3BC2-B257-E762A11EB95E
+  Functions: 6017
+  Symbols:   13524
+  CStrings:  16117
 
Symbols:
+ +[TBDefaults nearbyTileSearchRadius].cold.1
+ +[TBDefaults tileSearchRadius].cold.1
+ +[TBDefaults zoomLevel].cold.1
+ +[WCAClient sharedClient].cold.1
+ +[WiFiLocationManager sharedWiFiLocationManager].cold.1
+ +[WiFiPersonalHotspotStats sharedInstance].cold.1
+ +[WiFiPolicyNetworkActivityTracing sharedNetworkActivityTracing].cold.1
+ +[WiFiTelephonyClient sharedInstance].cold.1
+ +[WiFiUsageMonitor sharedInstance].cold.1
+ +[WiFiUsagePoorLinkSession timerReason:]
+ +[WiFiUsageSession isDriverUnavailabilityReasonVoluntary:subReason:orReasonString:]
+ -[WFBlackListNode _copyCreateBlacklistedState:reason:reasonData:].cold.1
+ -[WFBlackListNode addBlacklistTrigger:reasonData:bssid:].cold.1
+ -[WFBlackListNode addBlacklistedState:reason:reasonData:].cold.1
+ -[WFBlackListNode addBlacklistedStateHistory:state:reason:reasonData:].cold.1
+ -[WFBlackListNode initWithBlacklistNetwork:].cold.1
+ -[WFBlackListNode initWithBlacklistNetwork:].cold.2
+ -[WFBlackListNode initWithBlacklistNetwork:].cold.3
+ -[WFBlackListNode initWithBlacklistNetwork:].cold.4
+ -[WFBlackListNode initWithBlacklistNetwork:].cold.5
+ -[WFBlackListNode networkPruned].cold.2
+ -[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:].cold.2
+ -[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:].cold.3
+ -[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:].cold.4
+ -[WFBlackListNode processBlacklistedStateMetric:unblacklisting:unblacklistingReason:].cold.5
+ -[WFBlacklistEngine _evaluateTriggersForBlacklisting:reason:reasonData:bssid:ssid:state:].cold.1
+ -[WFBlacklistEngine changeBlacklistingThresholds:value:perSsid:].cold.1
+ -[WFBlacklistEngine clearTriggerForNetworkWithUnblacklistReason:reason:].cold.2
+ -[WFBlacklistEngine clearTriggerForNetworkWithUnblacklistReason:reason:].cold.3
+ -[WFBlacklistEngine clearTriggerForNetworkWithUnblacklistReason:reason:].cold.4
+ -[WFBlacklistEngine initWithBlacklistDelegate:profile:].cold.1
+ -[WFBlacklistEngine initWithBlacklistDelegate:profile:].cold.2
+ -[WFBlacklistEngine initWithBlacklistDelegate:profile:].cold.3
+ -[WFBlacklistEngine initWithBlacklistDelegate:profile:].cold.4
+ -[WFBlacklistEngine networkPruned:].cold.2
+ -[WFBlacklistEngine networkPruned:].cold.3
+ -[WFBlacklistEngine removeBlacklistedStateForNetworkWithReason:state:reason:].cold.1
+ -[WFBlacklistEngine removeBlacklistedStateWithUnblacklistType:].cold.1
+ -[WFBlacklistEngine removeBlacklistedStateWithUnblacklistType:].cold.2
+ -[WFBlacklistEngine removeExpiredBlacklistedState:].cold.1
+ -[WFBlacklistEngine removeExpiredBlacklistedState:].cold.2
+ -[WFBlacklistEngine retrieveBlacklistedNetworkSsids:].cold.1
+ -[WFBlacklistEngine retrieveBlacklistedStateHistoryForNetwork:state:timestamps:reasonData:].cold.1
+ -[WFBlacklistEngine retrieveBlacklistedStateHistoryForNetwork:state:timestamps:reasonData:].cold.2
+ -[WFBlacklistEngine retrieveBlacklistedStateHistoryForNetwork:state:timestamps:reasonData:].cold.3
+ -[WFBlacklistEngine retrieveBlacklistedStateHistoryForNetwork:state:timestamps:reasonData:].cold.4
+ -[WFBlacklistEngine retrieveBlacklistedStateHistoryForNetwork:state:timestamps:reasonData:].cold.5
+ -[WFBlacklistEngine retrieveNetworksInBlacklistedState:].cold.1
+ -[WFBlacklistEngine retrieveNetworksInBlacklistedStateHistory:].cold.1
+ -[WFBlacklistEngine retrieveReasonsForNetworkInBlacklistedState:state:timestamps:reasonData:].cold.1
+ -[WFBlacklistEngine retrieveReasonsForNetworkInBlacklistedState:state:timestamps:reasonData:].cold.2
+ -[WFBlacklistEngine retrieveReasonsForNetworkInBlacklistedState:state:timestamps:reasonData:].cold.3
+ -[WFBlacklistEngine retrieveReasonsForNetworkInBlacklistedState:state:timestamps:reasonData:].cold.4
+ -[WFBlacklistEngine retrieveReasonsForNetworkInBlacklistedState:state:timestamps:reasonData:].cold.5
+ -[WFLoggerFile createDateString].cold.1
+ -[WFLoggerFile createLogFile:fileClassC:].cold.1
+ -[WFLoggerFile generateLogFileName].cold.1
+ -[WFLoggerFile startWatchingLogFile].cold.1
+ -[WFLoggerFile startWatchingLogFile].cold.2
+ -[WFLoggerFile startWatchingLogFile].cold.3
+ -[WFLoggerFile writeToFile:cfStrMsg:].cold.1
+ -[WFTrafficEngManager __sendPeriodicEvent:].cold.1
+ -[WFTrafficEngManager initWithTrafficEngDelegate:].cold.1
+ -[WFTrafficEngManager initWithTrafficEngDelegate:].cold.2
+ -[WiFi3BarsNetwork containsAccessPointMatchingBSSIDs:].cold.1
+ -[WiFi3BarsSource initWithChangeHandler:localStoreType:].cold.1
+ -[WiFiAvailabilityEngine _handleCandidateMatches:].cold.1
+ -[WiFiAvailabilityEngine _handleCandidateMatches:].cold.2
+ -[WiFiLocaleManager getLocaleFromRemoteClient]
+ -[WiFiUsageAccessPointProfile hasColocatedMLOs]
+ -[WiFiUsageAccessPointProfile setHasColocatedMLOs:]
+ -[WiFiUsageBssDetails hasColocatedMLOs]
+ -[WiFiUsageBssDetails setHasColocatedMLOs:]
+ -[WiFiUsageLQMUserSample averageTxPer]
+ -[WiFiUsageLQMUserSample isHighCCAFor2GHz]
+ -[WiFiUsageLQMUserSample populateWithRssi:rssiInUse:rssi0:rssi1:rssiMode:noise:noise0:noise1:snr:selfCca:otherCca:interference:totalReportedCca:beaconPer:rxCrsGlitch:rxBadPLCP:rxStart:rxBphyCrsGlitch:rxBphyBadPLCP:sampleDuration:isHighCCAFor2GHz:]
+ -[WiFiUsageLQMUserSample populateWithTxFrames:RxFrames:TxFails:TxRetries:RxRetries:TxRate:RxRate:txRTS:txRTSFail:txMpdu:txAMPDU:averageTxPer:]
+ -[WiFiUsageLQMUserSample rssiInUse]
+ -[WiFiUsageLQMUserSample setAverageTxPer:]
+ -[WiFiUsageLQMUserSample setIsHighCCAFor2GHz:]
+ -[WiFiUsageLQMUserSample setRssiInUse:]
+ -[WiFiUsageLQMWindowAnalysis fetchKernelLQMRollingWindowForInterface:into:].cold.1
+ -[WiFiUsageLQMWindowAnalysis fetchKernelLQMRollingWindowForInterface:into:].cold.2
+ -[WiFiUsageLQMWindowAnalysis fetchKernelLQMRollingWindowForInterface:into:].cold.3
+ -[WiFiUsageLQMWindowAnalysis fetchKernelLQMRollingWindowForInterface:into:].cold.4
+ -[WiFiUsageMonitor appendSARStatsToDict:]
+ -[WiFiUsageMonitor lastApProfile]
+ -[WiFiUsageMonitor lastWiFiSARState]
+ -[WiFiUsageMonitor setLastApProfile:]
+ -[WiFiUsageMonitor setLastWiFiSARState:]
+ -[WiFiUsageMonitor setSARState:builtInReceiverOn:]
+ -[WiFiUsageMonitor shouldFilterSession:]
+ -[WiFiUsageNetworkDetails carrierPayloadIdentifier]
+ -[WiFiUsageNetworkDetails isCarrierPayloadIdentifierTelemetryApproved]
+ -[WiFiUsageNetworkDetails setCarrierPayloadIdentifier:]
+ -[WiFiUsageNetworkDetails setIsCarrierPayloadIdentifierTelemetryApproved:]
+ -[WiFiUsageParsedBeacon ap6gPowerMode]
+ -[WiFiUsageParsedBeacon parseSSID:length:endOfBuffer:]
+ -[WiFiUsageParsedBeacon setAp6gPowerMode:]
+ -[WiFiUsageParsedBeacon setShortSSID:]
+ -[WiFiUsageParsedBeacon setSsid:]
+ -[WiFiUsageParsedBeacon shortSSID]
+ -[WiFiUsageParsedBeacon ssid]
+ -[WiFiUsagePoorLinkSession dealloc]
+ -[WiFiUsagePoorLinkSession fgAppAtFirstTDConfirmed]
+ -[WiFiUsagePoorLinkSession fgAppAtSessionEnd]
+ -[WiFiUsagePoorLinkSession highImpactTimeAfterFirstTDConfirmed]
+ -[WiFiUsagePoorLinkSession highImpactTime]
+ -[WiFiUsagePoorLinkSession initializeTimer]
+ -[WiFiUsagePoorLinkSession lowModHighImpactTimeAfterFirstTDConfirmed]
+ -[WiFiUsagePoorLinkSession lowModHighImpactTime]
+ -[WiFiUsagePoorLinkSession modHighImpactTimeAfterFirstTDConfirmed]
+ -[WiFiUsagePoorLinkSession modHighImpactTime]
+ -[WiFiUsagePoorLinkSession rtAppAtFirstTDConfirmed]
+ -[WiFiUsagePoorLinkSession rtAppAtSessionEnd]
+ -[WiFiUsagePoorLinkSession sessionRxBytes]
+ -[WiFiUsagePoorLinkSession sessionStartRxBytes]
+ -[WiFiUsagePoorLinkSession sessionStartTxBytes]
+ -[WiFiUsagePoorLinkSession sessionTotalBytes]
+ -[WiFiUsagePoorLinkSession sessionTxBytes]
+ -[WiFiUsagePoorLinkSession setFgAppAtFirstTDConfirmed:]
+ -[WiFiUsagePoorLinkSession setFgAppAtSessionEnd:]
+ -[WiFiUsagePoorLinkSession setHighImpactTime:]
+ -[WiFiUsagePoorLinkSession setHighImpactTimeAfterFirstTDConfirmed:]
+ -[WiFiUsagePoorLinkSession setLowModHighImpactTime:]
+ -[WiFiUsagePoorLinkSession setLowModHighImpactTimeAfterFirstTDConfirmed:]
+ -[WiFiUsagePoorLinkSession setModHighImpactTime:]
+ -[WiFiUsagePoorLinkSession setModHighImpactTimeAfterFirstTDConfirmed:]
+ -[WiFiUsagePoorLinkSession setRtAppAtFirstTDConfirmed:]
+ -[WiFiUsagePoorLinkSession setRtAppAtSessionEnd:]
+ -[WiFiUsagePoorLinkSession setSessionRxBytes:]
+ -[WiFiUsagePoorLinkSession setSessionStartRxBytes:]
+ -[WiFiUsagePoorLinkSession setSessionStartTxBytes:]
+ -[WiFiUsagePoorLinkSession setSessionTotalBytes:]
+ -[WiFiUsagePoorLinkSession setSessionTxBytes:]
+ -[WiFiUsagePoorLinkSession setTotalSessionTime:]
+ -[WiFiUsagePoorLinkSession setTotalSessionTimeAfterFirstTDConfirmed:]
+ -[WiFiUsagePoorLinkSession setTxLatencyImpactTime:]
+ -[WiFiUsagePoorLinkSession setTxPerImpactTime:]
+ -[WiFiUsagePoorLinkSession setTxRxRateImpactTime:]
+ -[WiFiUsagePoorLinkSession setUnifiedImpactTime:]
+ -[WiFiUsagePoorLinkSession startTimerWithTimeout:reason:]
+ -[WiFiUsagePoorLinkSession stopTimer]
+ -[WiFiUsagePoorLinkSession suspendTimer]
+ -[WiFiUsagePoorLinkSession totalSessionTimeAfterFirstTDConfirmed]
+ -[WiFiUsagePoorLinkSession totalSessionTime]
+ -[WiFiUsagePoorLinkSession txLatencyImpactTime]
+ -[WiFiUsagePoorLinkSession txPerImpactTime]
+ -[WiFiUsagePoorLinkSession txRxRateImpactTime]
+ -[WiFiUsagePoorLinkSession unifiedImpactTime]
+ -[WiFiUsagePoorLinkSession updateWithScores:]
+ -[WiFiUsageSession deferCompletion]
+ -[WiFiUsageSession pendingWatchdogs]
+ -[WiFiUsageSession setDeferCompletion:]
+ -[WiFiUsageSession setPendingWatchdogs:]
+ -[WiFiUsageSession updateWithScores:]
+ -[WiFiUsageWatchdogDetails .cxx_destruct]
+ -[WiFiUsageWatchdogDetails availableReasonString]
+ -[WiFiUsageWatchdogDetails availableReason]
+ -[WiFiUsageWatchdogDetails availableSubreason]
+ -[WiFiUsageWatchdogDetails connectedBss]
+ -[WiFiUsageWatchdogDetails createdAt]
+ -[WiFiUsageWatchdogDetails flags]
+ -[WiFiUsageWatchdogDetails initWithInterfaceName:andConnectedBss:]
+ -[WiFiUsageWatchdogDetails interfaceName]
+ -[WiFiUsageWatchdogDetails reportedReasonString]
+ -[WiFiUsageWatchdogDetails reportedReason]
+ -[WiFiUsageWatchdogDetails reportedSubreasonString]
+ -[WiFiUsageWatchdogDetails reportedSubreason]
+ -[WiFiUsageWatchdogDetails setAvailableReason:]
+ -[WiFiUsageWatchdogDetails setAvailableReasonString:]
+ -[WiFiUsageWatchdogDetails setAvailableSubreason:]
+ -[WiFiUsageWatchdogDetails setConnectedBss:]
+ -[WiFiUsageWatchdogDetails setCreatedAt:]
+ -[WiFiUsageWatchdogDetails setFlags:]
+ -[WiFiUsageWatchdogDetails setInterfaceName:]
+ -[WiFiUsageWatchdogDetails setUnavailableReason:]
+ -[WiFiUsageWatchdogDetails setUnavailableReasonString:]
+ -[WiFiUsageWatchdogDetails setUnavailableSubreason:]
+ -[WiFiUsageWatchdogDetails unavailableReasonString]
+ -[WiFiUsageWatchdogDetails unavailableReason]
+ -[WiFiUsageWatchdogDetails unavailableSubreason]
+ -[WiFiWalletSource _passDidBecomeRelevant:].cold.1
+ GCC_except_table104
+ GCC_except_table241
+ GCC_except_table33
+ GCC_except_table41
+ GCC_except_table54
+ OBJC_IVAR_$_WiFiUsageAccessPointProfile._hasColocatedMLOs
+ OBJC_IVAR_$_WiFiUsageBssDetails._hasColocatedMLOs
+ OBJC_IVAR_$_WiFiUsageLQMUserSample._averageTxPer
+ OBJC_IVAR_$_WiFiUsageLQMUserSample._isHighCCAFor2GHz
+ OBJC_IVAR_$_WiFiUsageLQMUserSample._rssiInUse
+ OBJC_IVAR_$_WiFiUsageLinkSession._deferredFailureSessions
+ OBJC_IVAR_$_WiFiUsageLinkSession._joinAttemptedBeforeLinkDown
+ OBJC_IVAR_$_WiFiUsageLinkSession._joinSeqNo
+ OBJC_IVAR_$_WiFiUsageLinkSession._lastSubmittedSessionSeqNo
+ OBJC_IVAR_$_WiFiUsageMonitor._lastApProfile
+ OBJC_IVAR_$_WiFiUsageMonitor._lastWiFiSARState
+ OBJC_IVAR_$_WiFiUsageNetworkDetails._carrierPayloadIdentifier
+ OBJC_IVAR_$_WiFiUsageNetworkDetails._isCarrierPayloadIdentifierTelemetryApproved
+ OBJC_IVAR_$_WiFiUsageParsedBeacon._ap6gPowerMode
+ OBJC_IVAR_$_WiFiUsageParsedBeacon._shortSSID
+ OBJC_IVAR_$_WiFiUsageParsedBeacon._ssid
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._ccaThresholdFor2GHz
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._fgAppAtFirstTDConfirmed
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._fgAppAtSessionEnd
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._firstLQMForSessionReceived
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._highImpactTime
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._highImpactTimeAfterFirstTDConfirmed
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._isFirstTDConfirmed
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._lastIsAnyAppinFG
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._lastIsTimeSensitiveAppRunning
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._lowModHighImpactTime
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._lowModHighImpactTimeAfterFirstTDConfirmed
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._modHighImpactTime
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._modHighImpactTimeAfterFirstTDConfirmed
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._rssiThresholdFor2GHz
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._rtAppAtFirstTDConfirmed
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._rtAppAtSessionEnd
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._sessionRxBytes
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._sessionStartRxBytes
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._sessionStartTxBytes
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._sessionTotalBytes
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._sessionTxBytes
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._timerActive
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._timerReason
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._totalSessionTime
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._totalSessionTimeAfterFirstTDConfirmed
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._txLatencyImpactTime
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._txLatencyThreshold
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._txPerImpactTime
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._txPerThresholdHigh
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._txPerThresholdLow
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._txPerThresholdModerate
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._txRxRateImpactTime
+ OBJC_IVAR_$_WiFiUsagePoorLinkSession._unifiedImpactTime
+ OBJC_IVAR_$_WiFiUsageSession._deferCompletion
+ OBJC_IVAR_$_WiFiUsageSession._pendingWatchdogs
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._availableReason
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._availableReasonString
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._availableSubreason
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._connectedBss
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._createdAt
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._flags
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._interfaceName
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._unavailableReason
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._unavailableReasonString
+ OBJC_IVAR_$_WiFiUsageWatchdogDetails._unavailableSubreason
+ WFLoggerTimerTmoCallBack.cold.1
+ WFLoggerTimerTmoCallBack.cold.2
+ WiFiFaultHandlingLimitsStringMap.cold.1
+ WiFiUsageFaultReasonStringMap.cold.4
+ _Apple80211ReturnToString
+ _CNCRC
+ _OBJC_CLASS_$_WADeviceAnalyticsClient
+ _OBJC_CLASS_$_WiFiUsageWatchdogDetails
+ _OBJC_METACLASS_$_WiFiUsageWatchdogDetails
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_9
+ __24-[WiFiUsageMonitor init]_block_invoke.251
+ __24-[WiFiUsageMonitor init]_block_invoke.254
+ __36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.728
+ __69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.275
+ __85-[WiFiUsageMonitor submitScanResultWithNeighborBSS:withOtherBSS:withChannelInfoList:]_block_invoke.652
+ __85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.802
+ __85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.813
+ __OBJC_$_INSTANCE_METHODS_WiFiUsageWatchdogDetails
+ __OBJC_$_INSTANCE_VARIABLES_WiFiUsageWatchdogDetails
+ __OBJC_$_PROP_LIST_WiFiUsageWatchdogDetails
+ __OBJC_CLASS_RO_$_WiFiUsageWatchdogDetails
+ __OBJC_METACLASS_RO_$_WiFiUsageWatchdogDetails
+ __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne190102Ev
+ __ZNKSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB8ne190102Ev
+ __ZNSt12length_errorC1B8ne190102EPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne190102Emc
+ __ZNSt3__116__pad_and_outputB8ne190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__119__allocate_at_leastB8ne190102INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne190102Ev
+ __ZNSt3__120__throw_length_errorB8ne190102EPKc
+ __ZNSt3__124__put_character_sequenceB8ne190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__127__tree_balance_after_insertB8ne190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS2_RS4_EE
+ __ZSt28__throw_bad_array_new_lengthB8ne190102v
+ ___109-[WiFiUsageLinkSession joinStateDidChange:withReason:lastDisconnectReason:lastJoinFailure:andNetworkDetails:]_block_invoke
+ ___120-[WiFiUsageSession processDriverAvailability:available:version:flags:eventID:reason:subReason:minorReason:reasonString:]_block_invoke
+ ___43-[WiFiUsagePoorLinkSession initializeTimer]_block_invoke
+ ___50-[WiFiUsageMonitor setSARState:builtInReceiverOn:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s_e5_v8?0l
+ __block_literal_global.192
+ __block_literal_global.238
+ __block_literal_global.256
+ __block_literal_global.805
+ __block_literal_global.816
+ __block_literal_global.818
+ __block_literal_global.820
+ _convertLinkChangeReasonToString
+ _objc_msgSend$appendSARStatsToDict:
+ _objc_msgSend$availableReason
+ _objc_msgSend$availableReasonString
+ _objc_msgSend$availableSubreason
+ _objc_msgSend$averageTxPer
+ _objc_msgSend$chanQualScore
+ _objc_msgSend$createdAt
+ _objc_msgSend$fgAppAtFirstTDConfirmed
+ _objc_msgSend$fgAppAtSessionEnd
+ _objc_msgSend$getLocaleFromRemoteClient
+ _objc_msgSend$getRemoteClientCountryCode
+ _objc_msgSend$hasColocatedMLOs
+ _objc_msgSend$highImpactTime
+ _objc_msgSend$highImpactTimeAfterFirstTDConfirmed
+ _objc_msgSend$initWithCString:
+ _objc_msgSend$initWithInterfaceName:andConnectedBss:
+ _objc_msgSend$initializeTimer
+ _objc_msgSend$isDriverUnavailabilityReasonVoluntary:subReason:orReasonString:
+ _objc_msgSend$isHighCCAFor2GHz
+ _objc_msgSend$lastApProfile
+ _objc_msgSend$lastDriverAvailableTime
+ _objc_msgSend$lowModHighImpactTime
+ _objc_msgSend$lowModHighImpactTimeAfterFirstTDConfirmed
+ _objc_msgSend$manufacturerName
+ _objc_msgSend$modHighImpactTime
+ _objc_msgSend$modHighImpactTimeAfterFirstTDConfirmed
+ _objc_msgSend$modelName
+ _objc_msgSend$modelNumber
+ _objc_msgSend$parseSSID:length:endOfBuffer:
+ _objc_msgSend$pendingWatchdogs
+ _objc_msgSend$releaseBackgroundProcessingMOC
+ _objc_msgSend$reportedReason
+ _objc_msgSend$reportedReasonString
+ _objc_msgSend$reportedSubreason
+ _objc_msgSend$reportedSubreasonString
+ _objc_msgSend$rssiInUse
+ _objc_msgSend$rtAppAtFirstTDConfirmed
+ _objc_msgSend$rtAppAtSessionEnd
+ _objc_msgSend$sessionRxBytes
+ _objc_msgSend$sessionTotalBytes
+ _objc_msgSend$sessionTxBytes
+ _objc_msgSend$setAp6gPowerMode:
+ _objc_msgSend$setAvailableReason:
+ _objc_msgSend$setAvailableReasonString:
+ _objc_msgSend$setAvailableSubreason:
+ _objc_msgSend$setCarrierPayloadIdentifier:
+ _objc_msgSend$setCreatedAt:
+ _objc_msgSend$setDeferCompletion:
+ _objc_msgSend$setFgAppAtFirstTDConfirmed:
+ _objc_msgSend$setFgAppAtSessionEnd:
+ _objc_msgSend$setHasColocatedMLOs:
+ _objc_msgSend$setHighImpactTime:
+ _objc_msgSend$setHighImpactTimeAfterFirstTDConfirmed:
+ _objc_msgSend$setIsCarrierPayloadIdentifierTelemetryApproved:
+ _objc_msgSend$setLastApProfile:
+ _objc_msgSend$setLowModHighImpactTime:
+ _objc_msgSend$setLowModHighImpactTimeAfterFirstTDConfirmed:
+ _objc_msgSend$setModHighImpactTime:
+ _objc_msgSend$setModHighImpactTimeAfterFirstTDConfirmed:
+ _objc_msgSend$setPendingWatchdogs:
+ _objc_msgSend$setRtAppAtFirstTDConfirmed:
+ _objc_msgSend$setRtAppAtSessionEnd:
+ _objc_msgSend$setSessionRxBytes:
+ _objc_msgSend$setSessionTotalBytes:
+ _objc_msgSend$setSessionTxBytes:
+ _objc_msgSend$setShortSSID:
+ _objc_msgSend$setTotalSessionTime:
+ _objc_msgSend$setTotalSessionTimeAfterFirstTDConfirmed:
+ _objc_msgSend$setTxLatencyImpactTime:
+ _objc_msgSend$setTxPerImpactTime:
+ _objc_msgSend$setTxRxRateImpactTime:
+ _objc_msgSend$setUnavailableReason:
+ _objc_msgSend$setUnavailableReasonString:
+ _objc_msgSend$setUnavailableSubreason:
+ _objc_msgSend$setUnifiedImpactTime:
+ _objc_msgSend$sharedDeviceAnalyticsClient
+ _objc_msgSend$shortSSID
+ _objc_msgSend$shouldFilterSession:
+ _objc_msgSend$startTimerWithTimeout:reason:
+ _objc_msgSend$stopTimer
+ _objc_msgSend$stringWithCString:
+ _objc_msgSend$suspendTimer
+ _objc_msgSend$timerReason:
+ _objc_msgSend$totalSessionTime
+ _objc_msgSend$totalSessionTimeAfterFirstTDConfirmed
+ _objc_msgSend$txLatencyImpactTime
+ _objc_msgSend$txLatencyP95
+ _objc_msgSend$txLossScore
+ _objc_msgSend$txPerImpactTime
+ _objc_msgSend$txRxRateImpactTime
+ _objc_msgSend$unavailableReason
+ _objc_msgSend$unavailableReasonString
+ _objc_msgSend$unavailableSubreason
+ _objc_msgSend$unifiedImpactTime
+ _objc_msgSend$updateWithScores:
- -[WiFiUsageLQMUserSample populateWithRssi:rssi0:rssi1:rssiMode:noise:noise0:noise1:snr:selfCca:otherCca:interference:totalReportedCca:beaconPer:rxCrsGlitch:rxBadPLCP:rxStart:rxBphyCrsGlitch:rxBphyBadPLCP:sampleDuration:]
- -[WiFiUsageLQMUserSample populateWithTxFrames:RxFrames:TxFails:TxRetries:RxRetries:TxRate:RxRate:txRTS:txRTSFail:txMpdu:txAMPDU:]
- -[WiFiUsageMonitor analyticsProcessor]
- -[WiFiUsageMonitor setAnalyticsProcessor:]
- -[WiFiUsagePoorLinkSession linkStateDidChange:isInvoluntary:linkChangeReason:linkChangeSubreason:withNetworkDetails:].cold.1
- -[WiFiUsageSession setCurrentBand:]
- -[WiFiUsageSession summarizeBandUsage]
- GCC_except_table103
- GCC_except_table237
- GCC_except_table52
- OBJC_IVAR_$_WiFiUsageMonitor._analyticsProcessor
- OBJC_IVAR_$_WiFiUsagePoorLinkSession._waitingOnLinkUp
- _OBJC_CLASS_$_AnalyticsProcessor
- __24-[WiFiUsageMonitor init]_block_invoke.246
- __24-[WiFiUsageMonitor init]_block_invoke.249
- __36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.720
- __69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.270
- __85-[WiFiUsageMonitor submitScanResultWithNeighborBSS:withOtherBSS:withChannelInfoList:]_block_invoke.642
- __85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.794
- __85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.805
- __ZNKSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8ne180100Ev
- __ZNKSt3__16vectorIN6gloria6TileIdENS_9allocatorIS2_EEE20__throw_length_errorB8ne180100Ev
- __ZNSt12length_errorC1B8ne180100EPKc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8ne180100Emc
- __ZNSt3__116__pad_and_outputB8ne180100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__119__allocate_at_leastB8ne180100INS_9allocatorIN6gloria6TileIdEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119basic_ostringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8ne180100Ev
- __ZNSt3__120__throw_length_errorB8ne180100EPKc
- __ZNSt3__124__put_character_sequenceB8ne180100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__127__tree_balance_after_insertB8ne180100IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZSt28__throw_bad_array_new_lengthB8ne180100v
- ___74-[WiFiUsagePoorLinkSession initWithInterfaceName:andCapabilities:onQueue:]_block_invoke
- ___block_descriptor_112_e8_32s40s48s_e5_v8?0l
- __block_literal_global.187
- __block_literal_global.233
- __block_literal_global.251
- __block_literal_global.797
- __block_literal_global.808
- __block_literal_global.810
- __block_literal_global.812
- _objc_msgSend$sharedAnalyticsProcessor
- _objc_msgSend$summarizeBandUsage
CStrings:
+ "\ncolocatedMLD_2G:%@ colocatedMLD_5G:%@ colocatedMLD_6G:%@"
+ "%lu(%@/%lu)"
+ "%s HighImpactTime %lu (afterFirstTDConfirmed: %lu)"
+ "%s LowModHighImpactTime %lu (afterFirstTDConfirmed: %lu)"
+ "%s ModHighImpactTime %lu (afterFirstTDConfirmed: %lu)"
+ "%s RTAppAtSessionEnd %d (atFirstTDConfirmed: %d) , FGAppAtSessionEnd %d (atFirstTDConfirmed: %d)"
+ "%s Session (started: %@, ended: %@)"
+ "%s SessionTotalBytes %lu (SessionTxBytes %lu SessionRxBytes %lu)"
+ "%s TDAlerted due to BadRssi"
+ "%s TotalSessionTime %lu (afterFirstTDConfirmed: %lu)"
+ "%s UnifiedImpactTime %lu (TxPerImpactTime %lu TxRxRateImpactTime %lu TxLatencyImpactTime %lu)"
+ "%s on %@ deferCompletion=%s"
+ "%s: %s joining %@, seqNo %d, reason %@, failure %d"
+ "%s: (GoodRssiTimer expired) calling sessionDidEnd:%@"
+ "%s: (LinkDownNotTDTimer expired) calling sessionDidEnd:%@"
+ "%s: (TDTimer expired) calling sessionDidEnd:%@"
+ "%s: (Timer expired) w/ no reason"
+ "%s: BadLink session detected due to TDAlert; cancel the goodRssi timer/continue the bad session"
+ "%s: BadLink session detected due to driver TD Recommendation; cancel the goodRssi timer/continue the bad session (%@)"
+ "%s: BadLink session detected due to highCCA for 2.4G; cancel the goodRssi timer/continue the bad session"
+ "%s: BadLink session started due to TdAlert"
+ "%s: BadLink session started due to highCCA for 2.4G"
+ "%s: BadLink session will end due to rssi (%lddBm) crossing GoodLink Threshold (%@dBm) or tdRecommended(%@) %d sec GoodRssiTimer up"
+ "%s: Element %u_%u is invalid:%@"
+ "%s: Link changed while in GoodRssi Timer active session ended"
+ "%s: Sending linkTest to DeviceStore: %@"
+ "%s: Session will end due to goodRssi %d sec timer is up"
+ "%s: _toBeClosedAfterLQM: YES, should not happen %@"
+ "%s: link session completion deferred for %{private}@, deferred count %d"
+ "%s: link session ended for %{private}@, deferred count %d"
+ "%s: null interface name"
+ "%s: rssi (%lddBm) crossing BadLink Threshold (%@dBm); cancel the goodRssi timer/continue the bad session"
+ "%s: start timer (%@) wait up to %lu secs"
+ "%s:%d available:%d interface:%@ flags:0x%x reason:%@(0x%x) subreason:0x%x"
+ "-[WiFiUsageLinkSession joinStateDidChange:withReason:lastDisconnectReason:lastJoinFailure:andNetworkDetails:]"
+ "-[WiFiUsageParsedBeacon parseSSID:length:endOfBuffer:]"
+ "-[WiFiUsagePoorLinkSession initializeTimer]_block_invoke"
+ "-[WiFiUsagePoorLinkSession startTimerWithTimeout:reason:]"
+ "-[WiFiUsageSession processDriverAvailability:available:version:flags:eventID:reason:subReason:minorReason:reasonString:]"
+ "-[WiFiUsageSession sessionDidEnd]"
+ "-[WiFiUsageWatchdogDetails initWithInterfaceName:andConnectedBss:]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
+ "@\"WiFiUsageAccessPointProfile\""
+ "B40@0:8q16q24@32"
+ "Driver Booted"
+ "FGAppAtFirstTDConfirmed"
+ "FGAppAtSessionEnd"
+ "FaultReasonMTBFEventCount"
+ "GoodRSSITimer"
+ "GoodRssiThenBadSession"
+ "GoodRssiThenLinkChange"
+ "HND"
+ "HighCca2Ghz"
+ "HighImpactTime"
+ "HighImpactTimeAfterFirstTDConfirmed"
+ "HotspotConnectionInactive"
+ "LinkDownNotTDThenLinkUp"
+ "LinkDownNotTDTimer"
+ "LinkDownTDTimer"
+ "Locale from authorized client: <%@>"
+ "LowModHighImpactTime"
+ "LowModHighImpactTimeAfterFirstTDConfirmed"
+ "ModHighImpactTime"
+ "ModHighImpactTimeAfterFirstTDConfirmed"
+ "NetworkCarrierPayloadIdentifier"
+ "NetworkCarrierPayloadIdentifierIsAllowed"
+ "NoTimer"
+ "RTAppAtFirstTDConfirmed"
+ "RTAppAtSessionEnd"
+ "SessionRxBytes"
+ "SessionTotalBytes"
+ "SessionTxBytes"
+ "T@\"NSDate\",&,N,V_createdAt"
+ "T@\"NSDate\",C,N,V_settledDate"
+ "T@\"NSMutableArray\",&,N,V_pendingWatchdogs"
+ "T@\"NSString\",&,N,V_availableReasonString"
+ "T@\"NSString\",&,N,V_unavailableReasonString"
+ "T@\"NSString\",N,V_carrierPayloadIdentifier"
+ "T@\"WiFiUsageAccessPointProfile\",&,V_lastApProfile"
+ "T@\"WiFiUsageBssDetails\",&,N,V_connectedBss"
+ "TB,N,V_deferCompletion"
+ "TB,N,V_fgAppAtFirstTDConfirmed"
+ "TB,N,V_fgAppAtSessionEnd"
+ "TB,N,V_hasColocatedMLOs"
+ "TB,N,V_isCarrierPayloadIdentifierTelemetryApproved"
+ "TB,N,V_isHighCCAFor2GHz"
+ "TB,N,V_rtAppAtFirstTDConfirmed"
+ "TB,N,V_rtAppAtSessionEnd"
+ "TC,N,V_ap6gPowerMode"
+ "TI,N,V_shortSSID"
+ "TQ,N,V_averageTxPer"
+ "TQ,N,V_highImpactTime"
+ "TQ,N,V_highImpactTimeAfterFirstTDConfirmed"
+ "TQ,N,V_lastWiFiSARState"
+ "TQ,N,V_lowModHighImpactTime"
+ "TQ,N,V_lowModHighImpactTimeAfterFirstTDConfirmed"
+ "TQ,N,V_modHighImpactTime"
+ "TQ,N,V_modHighImpactTimeAfterFirstTDConfirmed"
+ "TQ,N,V_sessionRxBytes"
+ "TQ,N,V_sessionStartRxBytes"
+ "TQ,N,V_sessionStartTxBytes"
+ "TQ,N,V_sessionTotalBytes"
+ "TQ,N,V_sessionTxBytes"
+ "TQ,N,V_totalSessionTime"
+ "TQ,N,V_totalSessionTimeAfterFirstTDConfirmed"
+ "TQ,N,V_txLatencyImpactTime"
+ "TQ,N,V_txPerImpactTime"
+ "TQ,N,V_txRxRateImpactTime"
+ "TQ,N,V_unifiedImpactTime"
+ "Ti,N,V_availableReason"
+ "Ti,N,V_availableSubreason"
+ "Ti,N,V_unavailableReason"
+ "Ti,N,V_unavailableSubreason"
+ "Ti,R,N,V_currentBand"
+ "TotalSessionTime"
+ "TotalSessionTimeAfterFirstTDConfirmed"
+ "Tq,N,V_rssiInUse"
+ "TxLatencyImpactTime"
+ "TxPerImpactTime"
+ "TxRxRateImpactTime"
+ "UnifiedImpactTime"
+ "Unknown=0x%x:0x%x"
+ "WiFiUsageWatchdogDetails"
+ "WiFiUsageWatchdogDetailsSubmitToCA"
+ "[1035Q]"
+ "[35Q]"
+ "_ap6gPowerMode"
+ "_availableReason"
+ "_availableReasonString"
+ "_availableSubreason"
+ "_averageTxPer"
+ "_carrierPayloadIdentifier"
+ "_ccaThresholdFor2GHz"
+ "_createdAt"
+ "_deferCompletion"
+ "_deferredFailureSessions"
+ "_fgAppAtFirstTDConfirmed"
+ "_fgAppAtSessionEnd"
+ "_firstLQMForSessionReceived"
+ "_hasColocatedMLOs"
+ "_highImpactTime"
+ "_highImpactTimeAfterFirstTDConfirmed"
+ "_isCarrierPayloadIdentifierTelemetryApproved"
+ "_isFirstTDConfirmed"
+ "_isHighCCAFor2GHz"
+ "_joinAttemptedBeforeLinkDown"
+ "_joinSeqNo"
+ "_lastApProfile"
+ "_lastIsAnyAppinFG"
+ "_lastIsTimeSensitiveAppRunning"
+ "_lastSubmittedSessionSeqNo"
+ "_lastWiFiSARState"
+ "_lowModHighImpactTime"
+ "_lowModHighImpactTimeAfterFirstTDConfirmed"
+ "_modHighImpactTime"
+ "_modHighImpactTimeAfterFirstTDConfirmed"
+ "_pendingWatchdogs"
+ "_rssiInUse"
+ "_rssiThresholdFor2GHz"
+ "_rtAppAtFirstTDConfirmed"
+ "_rtAppAtSessionEnd"
+ "_sessionRxBytes"
+ "_sessionStartRxBytes"
+ "_sessionStartTxBytes"
+ "_sessionTotalBytes"
+ "_sessionTxBytes"
+ "_shortSSID"
+ "_timerActive"
+ "_timerReason"
+ "_totalSessionTime"
+ "_totalSessionTimeAfterFirstTDConfirmed"
+ "_txLatencyImpactTime"
+ "_txLatencyThreshold"
+ "_txPerImpactTime"
+ "_txPerThresholdHigh"
+ "_txPerThresholdLow"
+ "_txPerThresholdModerate"
+ "_txRxRateImpactTime"
+ "_unavailableReason"
+ "_unavailableReasonString"
+ "_unavailableSubreason"
+ "_unifiedImpactTime"
+ "ap6gPowerMode"
+ "appendSARStatsToDict:"
+ "associated"
+ "associationState"
+ "availableReason"
+ "availableReasonString"
+ "availableSubreason"
+ "averageTxPer"
+ "carrierPayloadIdentifier"
+ "com.apple.wifi.WatchdogEvent"
+ "createdAt"
+ "deferCompletion"
+ "disassociated"
+ "fgAppAtFirstTDConfirmed"
+ "fgAppAtSessionEnd"
+ "foregroundActivity"
+ "getLocaleFromRemoteClient"
+ "getRemoteClientCountryCode"
+ "highImpactTime"
+ "highImpactTimeAfterFirstTDConfirmed"
+ "initWithCString:"
+ "initWithInterfaceName:andConnectedBss:"
+ "initializeTimer"
+ "isCarrierPayloadIdentifierTelemetryApproved"
+ "isDriverAvailabilityNonFatal"
+ "isDriverUnavailabilityReasonVoluntary:subReason:orReasonString:"
+ "isHighCCAFor2GHz"
+ "kWiFiUsageFaultReasonMTBFEvent"
+ "lastApProfile"
+ "lastWiFiSARState"
+ "lowModHighImpactTime"
+ "lowModHighImpactTimeAfterFirstTDConfirmed"
+ "modHighImpactTime"
+ "modHighImpactTimeAfterFirstTDConfirmed"
+ "parseSSID:length:endOfBuffer:"
+ "pendingWatchdogs"
+ "populateWithRssi:rssiInUse:rssi0:rssi1:rssiMode:noise:noise0:noise1:snr:selfCca:otherCca:interference:totalReportedCca:beaconPer:rxCrsGlitch:rxBadPLCP:rxStart:rxBphyCrsGlitch:rxBphyBadPLCP:sampleDuration:isHighCCAFor2GHz:"
+ "populateWithTxFrames:RxFrames:TxFails:TxRetries:RxRetries:TxRate:RxRate:txRTS:txRTSFail:txMpdu:txAMPDU:averageTxPer:"
+ "reasonString"
+ "recoveryLatency"
+ "releaseBackgroundProcessingMOC"
+ "reportedReason"
+ "reportedReasonString"
+ "reportedSubreason"
+ "reportedSubreasonString"
+ "rssiInUse"
+ "rtAppAtFirstTDConfirmed"
+ "rtAppAtSessionEnd"
+ "sessionRxBytes"
+ "sessionStartRxBytes"
+ "sessionStartTxBytes"
+ "sessionTotalBytes"
+ "sessionTxBytes"
+ "setAp6gPowerMode:"
+ "setAvailableReason:"
+ "setAvailableReasonString:"
+ "setAvailableSubreason:"
+ "setAverageTxPer:"
+ "setCarrierPayloadIdentifier:"
+ "setCreatedAt:"
+ "setDeferCompletion:"
+ "setFgAppAtFirstTDConfirmed:"
+ "setFgAppAtSessionEnd:"
+ "setHasColocatedMLOs:"
+ "setHighImpactTime:"
+ "setHighImpactTimeAfterFirstTDConfirmed:"
+ "setIsCarrierPayloadIdentifierTelemetryApproved:"
+ "setIsHighCCAFor2GHz:"
+ "setLastApProfile:"
+ "setLastWiFiSARState:"
+ "setLowModHighImpactTime:"
+ "setLowModHighImpactTimeAfterFirstTDConfirmed:"
+ "setModHighImpactTime:"
+ "setModHighImpactTimeAfterFirstTDConfirmed:"
+ "setPendingWatchdogs:"
+ "setRssiInUse:"
+ "setRtAppAtFirstTDConfirmed:"
+ "setRtAppAtSessionEnd:"
+ "setSARState:builtInReceiverOn:"
+ "setSessionRxBytes:"
+ "setSessionStartRxBytes:"
+ "setSessionStartTxBytes:"
+ "setSessionTotalBytes:"
+ "setSessionTxBytes:"
+ "setShortSSID:"
+ "setTotalSessionTime:"
+ "setTotalSessionTimeAfterFirstTDConfirmed:"
+ "setTxLatencyImpactTime:"
+ "setTxPerImpactTime:"
+ "setTxRxRateImpactTime:"
+ "setUnavailableReason:"
+ "setUnavailableReasonString:"
+ "setUnavailableSubreason:"
+ "setUnifiedImpactTime:"
+ "sharedDeviceAnalyticsClient"
+ "shortSSID"
+ "shouldFilterSession:"
+ "startTimerWithTimeout:reason:"
+ "stopTimer"
+ "stringWithCString:"
+ "subreason"
+ "subreasonString"
+ "suspendTimer"
+ "timeBetweenFailure"
+ "timerReason:"
+ "totalSessionTime"
+ "totalSessionTimeAfterFirstTDConfirmed"
+ "txLatencyImpactTime"
+ "txPerImpactTime"
+ "txRxRateImpactTime"
+ "unavailableReason"
+ "unavailableReasonString"
+ "unavailableSubreason"
+ "unifiedImpactTime"
+ "updateWithScores:"
+ "v112@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80Q88Q96Q104"
+ "v180@0:8q16q24q32q40Q48q56q64q72q80Q88Q96Q104Q112Q120Q128Q136Q144Q152Q160Q168B176"
+ "v28@0:8Q16i24"
+ "v84@0:8@16B24Q28Q36Q44q52q60q68@76"
+ "wifiSARState"
+ "wpsManufacturerElement"
+ "wpsModelName"
+ "wpsModelNumber"
- "%s (%@): %@"
- "%s on %@ - Unexpected ifDown due to %@ while session is inactive"
- "%s: BadLink session ended due to linkUp"
- "%s: BadLink session ended due to rssi (%lddBm) crossing GoodLink Threshold (%@dBm) or tdRecommended(%@)"
- "%s: BadLink session will end due to linkUp (waiting on LQM update)"
- "%s: Link went down due to %@, ending session"
- "%s: Link went down, waiting on linkUp for up to %ds"
- "%s: link session ended for %{private}@"
- "-[WiFiUsageParsedBeacon parseNormalIE:from:length:endOfBuffer:]"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/WiFiPolicy/frameworks/Sources/TrafficEngineering/WFTrafficEngManager.m"
- "@\"AnalyticsProcessor\""
- "HND_AnalyticsProcessor"
- "T@\"AnalyticsProcessor\",&,V_analyticsProcessor"
- "T@\"NSDate\",N,V_settledDate"
- "[1034Q]"
- "[34Q]"
- "_analyticsProcessor"
- "_waitingOnLinkUp"
- "analyticsProcessor"
- "populateWithRssi:rssi0:rssi1:rssiMode:noise:noise0:noise1:snr:selfCca:otherCca:interference:totalReportedCca:beaconPer:rxCrsGlitch:rxBadPLCP:rxStart:rxBphyCrsGlitch:rxBphyBadPLCP:sampleDuration:"
- "populateWithTxFrames:RxFrames:TxFails:TxRetries:RxRetries:TxRate:RxRate:txRTS:txRTSFail:txMpdu:txAMPDU:"
- "setAnalyticsProcessor:"
- "sharedAnalyticsProcessor"
- "summarizeBandUsage"
- "v104@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80Q88Q96"
- "v168@0:8q16q24q32Q40q48q56q64q72Q80Q88Q96Q104Q112Q120Q128Q136Q144Q152Q160"
- "v88@0:8@16Q24Q32Q40Q48Q56Q64Q72@80"

```
