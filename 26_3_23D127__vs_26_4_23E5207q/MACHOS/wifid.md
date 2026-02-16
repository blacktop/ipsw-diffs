## wifid

> `/usr/sbin/wifid`

```diff

-1988.3.0.0.0
-  __TEXT.__text: 0x1ae7d0
-  __TEXT.__auth_stubs: 0x2990
-  __TEXT.__objc_stubs: 0x12d00
-  __TEXT.__objc_methlist: 0x5bb8
-  __TEXT.__gcc_except_tab: 0x1c20
-  __TEXT.__const: 0x9fb
-  __TEXT.__cstring: 0x6ae24
-  __TEXT.__objc_methname: 0x17973
-  __TEXT.__objc_classname: 0x7c2
-  __TEXT.__objc_methtype: 0x2fe5
-  __TEXT.__oslogstring: 0x2080
+1995.27.1.0.0
+  __TEXT.__text: 0x1a796c
+  __TEXT.__auth_stubs: 0x2940
+  __TEXT.__objc_stubs: 0x132a0
+  __TEXT.__objc_methlist: 0x5d98
+  __TEXT.__gcc_except_tab: 0x1c70
+  __TEXT.__const: 0xd7b
+  __TEXT.__cstring: 0x6bbd8
+  __TEXT.__objc_methname: 0x18223
+  __TEXT.__objc_classname: 0x7c3
+  __TEXT.__objc_methtype: 0x3041
+  __TEXT.__oslogstring: 0x1ff0
   __TEXT.__ustring: 0x4c2
   __TEXT.__dlopen_cstrs: 0x1a5
-  __TEXT.__unwind_info: 0x3d38
-  __DATA_CONST.__auth_got: 0x14d8
-  __DATA_CONST.__got: 0x12e8
+  __TEXT.__unwind_info: 0x3fd0
+  __DATA_CONST.__auth_got: 0x14b0
+  __DATA_CONST.__got: 0x12f8
   __DATA_CONST.__auth_ptr: 0x158
-  __DATA_CONST.__const: 0x7380
-  __DATA_CONST.__cfstring: 0x1b100
+  __DATA_CONST.__const: 0x7490
+  __DATA_CONST.__cfstring: 0x1b6c0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
-  __DATA_CONST.__objc_intobj: 0x10e0
-  __DATA_CONST.__objc_arraydata: 0x570
+  __DATA_CONST.__objc_intobj: 0x1290
+  __DATA_CONST.__objc_arraydata: 0x5f0
   __DATA_CONST.__objc_arrayobj: 0x168
   __DATA_CONST.__objc_dictobj: 0x208
-  __DATA.__objc_const: 0xc040
-  __DATA.__objc_selrefs: 0x58d0
-  __DATA.__objc_ivar: 0x8b8
+  __DATA.__objc_const: 0xc168
+  __DATA.__objc_selrefs: 0x5a80
+  __DATA.__objc_ivar: 0x8d0
   __DATA.__objc_data: 0x11d0
   __DATA.__data: 0x10b8
   __DATA.__bss: 0x7f8
-  __DATA.__common: 0x5c
+  __DATA.__common: 0x58
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: BB45CD0B-C221-33BB-8FFC-138AE6BEAC91
-  Functions: 7631
-  Symbols:   1285
-  CStrings:  19312
+  UUID: 4897C437-DE11-38FF-8D30-4D8C732DCEFA
+  Functions: 8241
+  Symbols:   1282
+  CStrings:  19508
 
Symbols:
+ _CWFXPCFamilyHotspotPreferencesKey
+ _CWFXPCInternetSharingDiscoveryStateKey
+ _CWFXPCInternetSharingPasswordKey
+ _CWFXPCInternetSharingStateKey
+ _CWFXPCShareMyPersonalHotspotModeKey
+ _OBJC_CLASS_$_CWFHotspotClient
+ _OBJC_CLASS_$_CWFHotspotFamilyMember
+ _OBJC_CLASS_$_CWFMACAddressHash
+ _OBJC_CLASS_$_WAEventLQMHistory
+ _OBJC_CLASS_$_WAEventLeave
+ _OBJC_CLASS_$_WiFiScanMonitor
+ _OBJC_CLASS_$_WiFiUsageSoftApStateInfo
+ _kSCCompInterface
+ _kWAMessageKeyPrivateMacHomeNetwork
+ _objc_retain_x26
+ _objc_retain_x28
- _kWAMessageKeyApProfile
- _kWAMessageKeyForegroundActivity
- _kWAMessageKeyIsDriverAvailabilityNonFatal
- _kWAMessageKeyReasonString
- _kWAMessageKeyRecoveryLatency
- _kWAMessageKeySubReason
- _kWAMessageKeySubReasonString
- _kWAMessageKeyTimeBetweenFailure
- _kWAMessageKeyWPSDeviceNameData
- _kWAMessageKeyWPSMfgElement
- _kWAMessageKeyWPSPrimaryDeviceNameElement
- _kWAMessageMetricNameWatchdogEvent
- _objc_claimAutoreleasedReturnValue
- _objc_release_x2
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ " SDBOpModeChange"
+ "%@:%@:%@"
+ "%s operation=%d ssid=%@"
+ "%s(%{public}@:%@): InfraUptime:%.1fsecs Channel: %d Bandwidth: %dMhz Rssi: %d Cca: %d (S:%d O:%d I:%d) Snr: %hd BcnPer: %.1f%% (%d, %.1f%%) TxFrameCnt: %d TxPer: %.1f%% TxReTrans: %d TxRetryRatio: %0.1f%% RxFrameCnt: %d RxRetryFrames: %d RxRetryRatio: %0.1f%% TxRate: %d RxRate: %d FBRate: %d TxFwFrms: %d TxFwFail: %d  time: %.1fsecs fgApp: %@ V: %s Band: %@"
+ "%s(%{public}@:%@): InfraUptime:%.1fsecs Channel: %d Bandwidth: %dMhz Rssi: %d Cca: %d Snr: %hd  BcnPer: %.1f%% (%d, %.1f%%) TxFrameCnt: %d TxPer: %.1f%% TxReTrans: %d TxRetryRatio: %0.1f%% RxFrameCnt : %d RxRetryFrames: %d RxRetryRatio: %0.1f%% TxRate: %d RxRate: %d FBRate: %d TxFwFrms: %d TxFwFail: %d time: %.1fsecs fgApp: %@ V: %s Band: %@"
+ "%s(%{public}@:%@): InfraUptime:%.1fsecs Channel: %d Bandwidth: %dMhz Rssi: %d {%ld %ld} Cca: %d (S:%d O:%d I:%d) Snr: %hd BcnPer: %.1f%% (%d, %.1f%%) TxFrameCnt: %d TxPer: %.1f%% TxReTrans: %d TxRetryRatio: %0.1f%% RxFrameCnt: %d RxRetryFrames: %d RxRetryRatio: %0.1f%% TxRate: %d RxRate: %d FBRate: %d TxFwFrms: %d TxFwFail: %d Noise: %d {%ld %ld %ld} time: %.1fsecs fgApp: %@ V: %s Band: %@"
+ "%s(%{public}@:%@): InfraUptime:%.1fsecs Channel: %d Bandwidth: %dMhz Rssi: %d {%ld %ld} Cca: %d Snr: %hd BcnPer: %.1f%% (%d, %.1f%%) TxFrameCnt: %d TxPer: %.1f%% TxReTrans: %d TxRetryRatio: %0.1f%% RxFrameCnt: %d RxRetryFrames: %d RxRetryRatio: %0.1f%% TxRate: %d RxRate: %d FBRate: %d TxFwFrms: %d TxFwFail: %d Noise: %d {%ld %ld %ld} time: %.1fsecs fgApp: %@ V: %s Band: %@"
+ "%s, WRM notification 0x%llx cell score %lu confidence %lu"
+ "%s: %s BW reduction - BW (%d)"
+ "%s: 2G-only watch detected, checking for BSSID guessing capability"
+ "%s: <%@> has securityType(enum)=%d"
+ "%s: AJPolicyTuning logic bypassed; isSSIDTemporarilyDenylisted %d isBSSIDDenylisted %d isFilteringAJCandidates %d isTDDenylisted %d, isAutoJoinDenylisted %d"
+ "%s: Allow CarPlay & Hotspot concurrent mode on channel %d\n"
+ "%s: Attempting to connect to CarPlay or already in CarPlay connection.  Disregard the channel (%d)"
+ "%s: Attempting to disable AWDL"
+ "%s: Attempting to disconnect and reconnect..."
+ "%s: BW is already 20 MHz"
+ "%s: CarPlay OUI %@"
+ "%s: Error: failed to create carPlayInterferenceMitigation.timer"
+ "%s: Error: failed to create carPlayReconnectWar.timer"
+ "%s: Error: monitoring APPLE80211_M_RESET_INTERFACE failed"
+ "%s: Error: monitoring APPLE80211_M_SCAN_CACHE_UPDATED failed"
+ "%s: Error: monitoring APPLE80211_M_SDB_MODE_CHANGED failed"
+ "%s: Failed to change BW, err %d"
+ "%s: Failed to create WiFiP2PSPITransactionRequestor"
+ "%s: Failed to create a semaphore"
+ "%s: IDSMinVersion: %ld"
+ "%s: MIS channel (%d), CarPlay channel (%d)\n"
+ "%s: MIS concurrent mode is inactive\n"
+ "%s: Network %@ is a WAC network"
+ "%s: Network '%@', isFilteringAJCandidates %d, isSSIDTemporarilyDenylisted %d, isBSSIDDenylisted %d, isTDDenylisted %d isSSIDDenylistedDueToCrash %d, isAutoJoinDenylisted %d"
+ "%s: No concurrency needed\n"
+ "%s: No longer TD-Deny-Listing %@; isSSIDTemporarilyDenylisted %d isBSSIDDenylisted %d isFilteringAJCandidates %d isTDDenylisted %d, isAutoJoinDenylisted %d"
+ "%s: PHSessionMetric: method=%d end=%d teardown=%d, misStart=%f softAPUp=%f sessionEnd=%f, appleDeviceConnectionCount=%d(%x) nonAppleDeviceConnectionCount=%d deviceDisconnectCount=%d, lpmDuration=%llu, dynamicModeDur=%llu, channel=%d, securityTypes 0x%XnanPhPublisherFailureReason %d, nanPhNanStationCount %d, nanPhNanStartSessionTime %f nanPhNanSessionEndTime %f discoveryDisabledTime:%f"
+ "%s: PHSessionMetric: method=%d end=%d teardown=%d, misStart=%f softAPUp=%fsessionEnd=%f, appleDeviceConnectionCount=%d(%x) nonAppleDeviceConnectionCount=%ddeviceDisconnectCount=%d, lpmDuration=%llu, dynamicModeDur=%llu, channel=%d nanPhNanStationCount=%d lastClientDisconnectedTime:%f"
+ "%s: Phy mode is not capable"
+ "%s: Security Mask: 0x%lx, setting supportedSecurityTypes"
+ "%s: Suppressing Tx stall based roam"
+ "%s: Timeout waiting for transaction completion"
+ "%s: Unable to fetch device name from dictionary %@"
+ "%s: Unexpected SCDynamicStore update: %@"
+ "%s: [NearbyJoinAssist] Bypassing location/time-based banner suppression policy for nearby-recommended network (%@)"
+ "%s: btSCOActivePercent %.2lf btA2DPActivePercent %.2lf softAPActivePercent %.2lf percentTxErrorEventsDuringSoftAP %.2lf"
+ "%s: captive determination is not present for %@"
+ "%s: ccaInterferenceTotalRef is null"
+ "%s: ccaStatsDict is null"
+ "%s: failed to allocate bwRef"
+ "%s: failed to allocate methodRef"
+ "%s: failed to allocate miDict"
+ "%s: failed to get WAEventRoamStatus:%@"
+ "%s: failed to init WAEventLeave: %@"
+ "%s: interface %@ does not match device %@"
+ "%s: isPnoFound=<%d> "
+ "%s: isWaitingForIdsMessageDelivery %d, isWaitingForIdsSendResponse %d, pairedDeviceDestinationID prev %@, new %@, pairedDeviceVersionID prev %@, new %@, pairedDeviceSupportsWiFiNetworkSharing %d"
+ "%s: legacy guessing for network with BSSID"
+ "%s: link recovery is currently %s and auto-join is currently %s, hence assocStateMonitor.timer is suppressed"
+ "%s: network is not CarPlay\n"
+ "%s: null syncNetwork"
+ "%s: phyMode %x, bandWidth %d"
+ "%s: reasonStr (%@) reasonCode (%d) currentState (%d) carplayOUI (%@)"
+ "%s: setup is not yet completed."
+ "%s: state (%d), awdlDisabledForCarPlayConnect (%d)"
+ "%s: using %@ SSID: %@"
+ "%s: wake assertion released for network %@ duration: %.2f seconds"
+ "-[WiFiIDSSyncEngine isWiFiNetworkSharingSupportedOnPairedDevice]"
+ "-[WiFiIDSSyncEngine ssidFromNetworkRecord:]"
+ "-[WiFiIDSSyncEngine updatePairedDeviceID:versionID:wifiNetworkSharingSupported:]"
+ "-[WiFiIDSSyncEngine updatePairedDeviceID:versionID:wifiNetworkSharingSupported:]_block_invoke"
+ "-[WiFiUserInteractionMonitor _initPrivate]_block_invoke_5"
+ "-[WiFiXPCManager _familyHotspotMembersFromArray:]"
+ "6GHz"
+ "AJScan: Allowing 2.4Ghz channels due to CarPlay"
+ "APPLE80211_M_RESET_INTERFACE"
+ "APPLE80211_M_SCAN_CACHE_UPDATED"
+ "APPLE80211_M_SDB_MODE_CHANGED"
+ "APPLE_DEVICE_IE_FEATURE_SUPPORTS_SECURE_WAC"
+ "Auto-Join disabled for hotspot"
+ "B40@0:8^{__WiFiNetwork=}16@24@32"
+ "Canceled join due to SystemWillSleep"
+ "CarPlayReconnectWAR"
+ "Device powering %s isPoweredStateSet %d"
+ "Failed to async add Leave on %@[%@] at %@ in the DB %@"
+ "Failed to async add Roam %@ in the DB %@"
+ "Failed to get the state for com.apple.WRM.iRAT_event.linkRecommendation (%u)"
+ "Failed to register for com.apple.WRM.iRAT_event.linkRecommendation (%u)"
+ "GameModeUltraLowLatency"
+ "Hash"
+ "INSTANT_ROAM_SCAN_COUNT_2G"
+ "INSTANT_ROAM_SCAN_COUNT_5G"
+ "INSTANT_ROAM_SCAN_COUNT_6G"
+ "INSTANT_ROAM_SCAN_DURATION_2G"
+ "INSTANT_ROAM_SCAN_DURATION_5G"
+ "INSTANT_ROAM_SCAN_DURATION_6G"
+ "INSTANT_SC_ROAM_SCAN_COUNT_2G"
+ "INSTANT_SC_ROAM_SCAN_COUNT_5G"
+ "INSTANT_SC_ROAM_SCAN_COUNT_6G"
+ "INSTANT_SC_ROAM_SCAN_DURATION_2G"
+ "INSTANT_SC_ROAM_SCAN_DURATION_5G"
+ "INSTANT_SC_ROAM_SCAN_DURATION_6G"
+ "INSTANT_SC_USER_SCAN_COUNT_2G"
+ "INSTANT_SC_USER_SCAN_COUNT_5G"
+ "INSTANT_SC_USER_SCAN_COUNT_6G"
+ "INSTANT_SC_USER_SCAN_DURATION_2G"
+ "INSTANT_SC_USER_SCAN_DURATION_5G"
+ "INSTANT_SC_USER_SCAN_DURATION_6G"
+ "INSTANT_USER_SCAN_COUNT_2G"
+ "INSTANT_USER_SCAN_COUNT_5G"
+ "INSTANT_USER_SCAN_COUNT_6G"
+ "INSTANT_USER_SCAN_DURATION_2G"
+ "INSTANT_USER_SCAN_DURATION_5G"
+ "INSTANT_USER_SCAN_DURATION_6G"
+ "IO80211MitigateInterferenceBW"
+ "IO80211MitigateInterferenceBWChangeMethod"
+ "Inexpensive cellular available, not allowing joining Personal Hotspot"
+ "Invalid entry value for key %@\n"
+ "Invalid exit and entry value %@ - %@\n"
+ "Invalid exit stats\n"
+ "Invalid exit value for key %@\n"
+ "Invalid key\n"
+ "MitigateInterferenceForCarPlay"
+ "NETWORK_SHARING_SSID_STR"
+ "NetworkSharing"
+ "SALTED_BSSID"
+ "SECURITY_TYPE"
+ "SOFTAP_BRINGUP_METHOD"
+ "SOFTAP_FORCE_2_4G_CHANNEL"
+ "SOFTAP_IMMEDIATE_DISABLE"
+ "SOFTAP_LOWPOWER_STATS_DYNAMIC_STATE_DURATION"
+ "SOFTAP_SOFTAP_CAP_MODEL"
+ "SOFTAP_SOFTAP_OS_VER"
+ "Salt"
+ "TB,V_pairedDeviceSupportsWiFiNetworkSharing"
+ "TQ,N,V_cellularWrmScore"
+ "TQ,N,V_cellularWrmScoreConfidence"
+ "Td,N,V_latestWRMStatusTimestamp"
+ "Ti,N,V_nanSubscriberTimerState"
+ "Ti,N,V_wrmNotifyToken"
+ "WiFiDeviceManagerCreate_block_invoke"
+ "WiFiDeviceManagerShouldSuppressTxStallBasedRoam"
+ "WiFiManager-1995.27.1 Feb  9 2026 22:55:44"
+ "WiFiManager-1995.27.1 Feb  9 2026 22:56:15"
+ "WiFiManagerGetEnableInternal"
+ "WiFiNetworkIsWAC"
+ "WiFiNetworkSyncHelperCreateNetworkSharingRecord"
+ "WiFiNetworkSyncHelperCreateSyncableLegacyNetworkRecord"
+ "WiFiWatchCredentialSharing"
+ "[corewifi] %s: failed to create family hotspot member for '%@'"
+ "__WiFiDeviceManagerAddSocialChannels"
+ "__WiFiDeviceManagerCarPlayInterferenceMitigationTimerCallback"
+ "__WiFiDeviceManagerCarPlayReconnectWarTimerCallback"
+ "__WiFiDeviceManagerCheckCarPlayInterference"
+ "__WiFiDeviceManagerMitigateInterferenceForCarPlay"
+ "__WiFiDeviceManagerScanCacheUpdatedCallback"
+ "__WiFiDeviceManagerSetNetworkDenyListBlocks_block_invoke"
+ "__WiFiDeviceManagerValidateConcurrentModeBeforeCarPlayConnect"
+ "__WiFiDeviceManagerValidatePHAndCarPlayConcurrency"
+ "__WiFiDeviceProcessSdbOpModeDidChange"
+ "__WiFiDeviceScanCacheUpdated"
+ "__WiFiMetricsManagerUpdateDBWithJoinOrLeave"
+ "__copyFamilyHotspotPreferences:"
+ "__copyHotspotClientDataUsage:"
+ "__copyInternetSharingPassword:"
+ "__copyInternetSharingStats:"
+ "__getInternetSharingDiscoveryState:"
+ "__getInternetSharingState:"
+ "__getPersonalHotspotModificationDisabled:"
+ "__getShareMyPersonalHotspotMode:"
+ "__hotspotClientDataUsageFromStoredUsage:interfaceName:"
+ "__isTetheringSupported:"
+ "__resetInternetSharingStats:"
+ "__setFamilyHotspotPreferences:"
+ "__setInternetSharingDiscoveryState:"
+ "__setInternetSharingDiscoveryStateExt:"
+ "__setInternetSharingPassword:"
+ "__setInternetSharingState:"
+ "__setShareMyPersonalHotspotMode:"
+ "_cellularWrmScore"
+ "_cellularWrmScoreConfidence"
+ "_familyHotspotMembersFromArray:"
+ "_latestWRMStatusTimestamp"
+ "_nanSubscriberTimerState"
+ "_pairedDeviceSupportsWiFiNetworkSharing"
+ "_wrmNotifyToken"
+ "asyncSubmitEvent:andDeferReclaimMem:andRunPostProcessing:uponCompletionDo:"
+ "asyncSubmitEvent:uponCompletionDo:"
+ "beaconPerHistory"
+ "beaconSchedHistory"
+ "btA2DPActivePercent"
+ "btSCOActivePercent"
+ "ccaHistory"
+ "cellWRMScoreUpdatedTimestamp"
+ "cellularWrmScore"
+ "cellularWrmScoreConfidence"
+ "channelWidthFromChannelFlags:"
+ "checkSaltedBssidMatchFor2GTargetNetwork:withCompanionHashData:andSaltData:"
+ "com.apple.WRM.iRAT_event.linkRecommendation"
+ "concurrentState"
+ "currentCellWRMScore"
+ "currentCellWRMScoreConfidence"
+ "deny bssid due to crash since only %f passed from last join"
+ "fwTxFramesHistory"
+ "fwTxPerHistory"
+ "gatherScanStatisticsForClient:error:is2GScan:is2GScanScanCore:is5GScan:is5GScanScanCore:is6GScan:is6GScanScanCore:scanDuration2G:scanDuration5G:scanDuration6G:scanCore2GScanDuration:scanCore5GScanDuration:scanCore6GScanDuration:"
+ "generateBSSIDVariants:"
+ "hashData"
+ "initWithBssid:ssid:at:data:withLqmHistory:withError:"
+ "initWithDisplayName:MACAddress:productColor:productMarketingName:productType:peerIdentifier:dataUsageLastBytes:dataUsageTotalBytes:dataUsageLastUpdated:"
+ "initWithDisplayName:identifier:sharingMode:"
+ "initWithDriverEvent:andDeviceCapabilities:at:withLqmHistory:withError:"
+ "initWithHashData:andSalt:andHashMethod:"
+ "initWithMACAddress:"
+ "interferenceMitigationCount"
+ "isNetworkDenyListedForAutoJoinDueToCrash:"
+ "isWiFiNetworkSharingSupported"
+ "isWiFiNetworkSharingSupportedOnPairedDevice"
+ "latestWRMStatusTimestamp"
+ "matchesMACAddressData:"
+ "nanSubscriberTimerState"
+ "noiseHistory"
+ "oui"
+ "pairedDeviceSupportsWiFiNetworkSharing"
+ "percentTxErrorEventsDuringSoftAP"
+ "publisher:getKeysBlobForMulticastSession:"
+ "reasonCode"
+ "reset interface state<%d> "
+ "rssiHistory"
+ "salt"
+ "serviceMinCompatibilityVersion"
+ "setCellularWrmScore:"
+ "setCellularWrmScoreConfidence:"
+ "setChangeReason:"
+ "setChannelWidth:"
+ "setCountryCode:"
+ "setDurationForJoinPMAssertion:"
+ "setDynamicPowerModeDurationSec:"
+ "setIdleTimeAfterLastClientDisconnectedSec:"
+ "setIdleTimeBeforeTeardownSec:"
+ "setIsAwdlUp:"
+ "setIsInfraConnected:"
+ "setLatestWRMStatusTimestamp:"
+ "setLowPowerModeDurationSec:"
+ "setNanSubscriberTimerState:"
+ "setPairedDeviceSupportsWiFiNetworkSharing:"
+ "setPrivateMacNetworkTypeHome:"
+ "setRequestToUpLatency:"
+ "setRequester:"
+ "setSoftApState:"
+ "setTdLogic_cellularState:forInterface:"
+ "setWrmNotifyToken:"
+ "sharedScanMonitor"
+ "snrHistory"
+ "softAPActivePercent"
+ "ssidFromNetworkRecord:"
+ "txFrameHistory"
+ "txPerHistory"
+ "updatePairedDeviceID:versionID:wifiNetworkSharingSupported:"
+ "v32@0:8@\"WiFiAwarePublisher\"16@\"NSData\"24"
+ "v36@0:8@16@24B32"
+ "wrmNotifyToken"
- "%s %@"
- "%s QFA Watchdog metric WPS PROBE RESPONSE IE not found in driverAvailableEventDict. Looking in cache..."
- "%s QFA Watchdog metricWPS PROBE RESPONSE IE found in Known networks cache"
- "%s(%{public}@:%@): InfraUptime:%.1fsecs Channel: %d Bandwidth: %dMhz Rssi: %d Cca: %d (S:%d O:%d I:%d) Snr: %hd BcnPer: %.1f%% (%d, %.1f%%) TxFrameCnt: %d TxPer: %.1f%% TxReTrans: %d TxRetryRatio: %0.1f%% RxFrameCnt: %d RxRetryFrames: %d RxRetryRatio: %0.1f%% TxRate: %d RxRate: %d FBRate: %d TxFwFrms: %d TxFwFail: %d  time: %.1fsecs fgApp: %@ V: %s"
- "%s(%{public}@:%@): InfraUptime:%.1fsecs Channel: %d Bandwidth: %dMhz Rssi: %d Cca: %d Snr: %hd  BcnPer: %.1f%% (%d, %.1f%%) TxFrameCnt: %d TxPer: %.1f%% TxReTrans: %d TxRetryRatio: %0.1f%% RxFrameCnt : %d RxRetryFrames: %d RxRetryRatio: %0.1f%% TxRate: %d RxRate: %d FBRate: %d TxFwFrms: %d TxFwFail: %d time: %.1fsecs fgApp: %@ V: %s"
- "%s(%{public}@:%@): InfraUptime:%.1fsecs Channel: %d Bandwidth: %dMhz Rssi: %d {%ld %ld} Cca: %d (S:%d O:%d I:%d) Snr: %hd BcnPer: %.1f%% (%d, %.1f%%) TxFrameCnt: %d TxPer: %.1f%% TxReTrans: %d TxRetryRatio: %0.1f%% RxFrameCnt: %d RxRetryFrames: %d RxRetryRatio: %0.1f%% TxRate: %d RxRate: %d FBRate: %d TxFwFrms: %d TxFwFail: %d Noise: %d {%ld %ld %ld} time: %.1fsecs fgApp: %@ V: %s"
- "%s(%{public}@:%@): InfraUptime:%.1fsecs Channel: %d Bandwidth: %dMhz Rssi: %d {%ld %ld} Cca: %d Snr: %hd BcnPer: %.1f%% (%d, %.1f%%) TxFrameCnt: %d TxPer: %.1f%% TxReTrans: %d TxRetryRatio: %0.1f%% RxFrameCnt: %d RxRetryFrames: %d RxRetryRatio: %0.1f%% TxRate: %d RxRate: %d FBRate: %d TxFwFrms: %d TxFwFail: %d Noise: %d {%ld %ld %ld} time: %.1fsecs fgApp: %@ V: %s"
- "%s: 2.4 Ghz CarPlay network\n"
- "%s: 5Ghz MIS is inactive\n"
- "%s: <%@> security %d"
- "%s: Allow 5Ghz CarPlay & Hotspot concurrent mode\n"
- "%s: Failed to alloc WAMessage for WatchdogEvent"
- "%s: Fatal chip watchdog with missing reason or subreason"
- "%s: Filename :%s"
- "%s: Function name :%s"
- "%s: Network '%@', isFilteringAJCandidates %d, isSSIDTemporarilyDenylisted %d, isBSSIDDenylisted %d, isTDDenylisted %d"
- "%s: PHSessionMetric: method=%d end=%d teardown=%d, misStart=%f softAPUp=%f sessionEnd=%f, appleDeviceConnectionCount=%d(%x) nonAppleDeviceConnectionCount=%d deviceDisconnectCount=%d, lpmDuration=%llu, channel=%d, securityTypes 0x%XnanPhPublisherFailureReason %d, nanPhNanStationCount %d, nanPhNanStartSessionTime %f nanPhNanSessionEndTime %f discoveryDisabledTime:%f"
- "%s: PHSessionMetric: method=%d end=%d teardown=%d, misStart=%f softAPUp=%fsessionEnd=%f, appleDeviceConnectionCount=%d(%x) nonAppleDeviceConnectionCount=%ddeviceDisconnectCount=%d, lpmDuration=%llu, channel=%d nanPhNanStationCount=%d lastClientDisconnectedTime:%f"
- "%s: Switching cached list from %ld to %ld private mac networks"
- "%s: WAClient failed to process roamevent: %@"
- "%s: [NearbyCaptiveAssistTestable] Location/time-based banner suppression policy for recommended networks is DISABLED: %@"
- "%s: addr is NULL"
- "%s: captive determination is not present for %@ , not adding network!!"
- "%s: captive determination is not present for %@ , not syncing the network to gizmo yet!!"
- "%s: companion network %@ is not a 5ghz network"
- "%s: currentNetwork is NULL"
- "%s: flags: 0x%x available: 0x%x minor_reason: 0x%x filename: %s function: %s"
- "%s: hasExtTrapInfo: 0x%x sequenceNum: %d signatureCount: %d stackTraceCount: %d recoveryLatency: %d"
- "%s: interface from dictionary does not match"
- "%s: isMultiAP:%u"
- "%s: isWaitingForIdsMessageDelivery %d, isWaitingForIdsSendResponse %d, pairedDeviceDestinationID prev %@, new %@, pairedDeviceVersionID prev %@, new %@"
- "%s: metrics is NULL"
- "%s: metrics null"
- "%s: modDates have been added to network, changes written to plist: %d"
- "%s: network usage time is %.2f secs."
- "%s: null available boolRef"
- "%s: null callbackBlock"
- "%s: null driverAvailableEventDict"
- "%s: null flags"
- "%s: null reason"
- "%s: null subreason"
- "%s: null version"
- "%s: null watchdogEventMetric"
- "%s: reason: 0x%x reasonString: %s subreason: 0x%x subreasonString: %s"
- "%s: reason:%s(0x%8x or %d), subreason:%s(0x%8x or %u) flag: %u"
- "%s: reasonStr (%@)"
- "%s: reasonString :%s"
- "%s: subReasonString :%s"
- "%s: waMsg is NULL"
- "%s: wake assertion released for network %@ current timestamp:%f"
- "%s:LeechLocation field is NULL!"
- "%{public}s::%d:Failed to fetch lqm histograms"
- "%{public}s::%d:LinkDown: Preparing WADeviceAnalyticsEventLeaveNetwork"
- "-[WiFiIDSSyncEngine updatePairedDeviceID:versionID:]"
- "AJScan: Disallowing 2.4Ghz channels due to CarPlay"
- "CarPlayConcurrentModeFailure24GHzWithBluetooth"
- "CarPlayConcurrentModeFailure24GHzWithPH"
- "CarPlayConcurrentModeFailure5GHzWithAWDLAndPH"
- "CarPlayConcurrentModeFailure5GHzWithPHAndCellularDenylisted"
- "CarPlayConcurrentModeFailure5GHzWithPHAndDfsChannel"
- "DRIVER_AVAILABLE_TRAP_UCODE"
- "Device powering %s"
- "FIXME: Unexpected WiFiAssociationType, unable to map to WAAssociationType"
- "Fatal chip watchdog with missing reason or subreason"
- "IO80211InterfaceRoamProfilePoorLinkQuality"
- "NetworkDenyList"
- "Not a string"
- "Poor LQM"
- "Poor LQM + Motion"
- "WiFiDeviceManagerSetWoWState"
- "WiFiManager-1988.3 Jan 27 2026 21:06:12"
- "WiFiManager-1988.3 Jan 27 2026 21:06:47"
- "WiFiMetricsManagerSubmitWatchdogEvent"
- "WiFiNetworkSyncHelperCreateSyncableNetworkRecord"
- "WiFiUsageWatchdogDetailsSubmitToCA"
- "__WiFiDeviceManagerCreateNetworkDenyList_block_invoke"
- "__WiFiMetricsManagerWAMessageAppendFieldInColonHexdecFormat"
- "__WiFiMetricsManagerWAMessageSubmitWatchdogEvent"
- "iPad12,1"
- "iPad12,2"
- "initWithDriverEvent:andDeviceCapabilities:"
- "is Null or Key-not-present"
- "leaveEventOnBssid:ssid:at:with:"
- "setAssocDuration:"
- "setBeaconPerHistory:"
- "setBeaconSchedHistory:"
- "setCcaHistory:"
- "setFwTxFramesHistory:"
- "setFwTxPerHistory:"
- "setHistoryBcnPer:"
- "setHistoryBcnSched:"
- "setHistoryCca:"
- "setHistoryFwTxFrames:"
- "setHistoryFwTxPer:"
- "setHistoryRssi:"
- "setHistorySnr:"
- "setHistoryTxFrames:"
- "setHistoryTxPer:"
- "setIsInVoluntary:"
- "setNoiseHistory:"
- "setRssiHistory:"
- "setSnrHistory:"
- "setSoftApState:requester:status:changeReason:channelNumber:countryCode:isHidden:isInfraConnected:isAwdlUp:lowPowerModeDuration:compatibilityMode:requestToUpLatency:idleTimeBeforeTeardownSec:idleTimeAfterLastClientDisconnectedSec:"
- "setSuccess:"
- "setTxFrameHistory:"
- "setTxPerHistory:"
- "submitEvent:at:andDeferReclaimMem:andRunPostProcessing:withError:"
- "updatePairedDeviceID:versionID:"
- "v16@?0@\"WADeviceAnalyticsLeaveRecord\"8"
- "zeroLen"

```
