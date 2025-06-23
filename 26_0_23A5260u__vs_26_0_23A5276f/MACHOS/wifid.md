## wifid

> `/usr/sbin/wifid`

```diff

-1975.87.0.0.0
-  __TEXT.__text: 0x1a8b88
-  __TEXT.__auth_stubs: 0x2910
-  __TEXT.__objc_stubs: 0x12a60
-  __TEXT.__objc_methlist: 0x5ac0
-  __TEXT.__gcc_except_tab: 0x1bc4
-  __TEXT.__const: 0x92b
-  __TEXT.__cstring: 0x6a386
-  __TEXT.__objc_methname: 0x175c8
+1975.96.0.0.0
+  __TEXT.__text: 0x1ac89c
+  __TEXT.__auth_stubs: 0x2950
+  __TEXT.__objc_stubs: 0x12c60
+  __TEXT.__objc_methlist: 0x5b48
+  __TEXT.__gcc_except_tab: 0x1c28
+  __TEXT.__const: 0x9eb
+  __TEXT.__cstring: 0x6a736
+  __TEXT.__objc_methname: 0x17856
   __TEXT.__objc_classname: 0x7c2
-  __TEXT.__objc_methtype: 0x2f9a
-  __TEXT.__oslogstring: 0x1992
+  __TEXT.__objc_methtype: 0x2fa5
+  __TEXT.__oslogstring: 0x1fe0
   __TEXT.__ustring: 0x4c2
   __TEXT.__dlopen_cstrs: 0x1a5
-  __TEXT.__unwind_info: 0x3b78
-  __DATA_CONST.__auth_got: 0x1498
-  __DATA_CONST.__got: 0x12e0
-  __DATA_CONST.__auth_ptr: 0x150
-  __DATA_CONST.__const: 0x7260
-  __DATA_CONST.__cfstring: 0x1aa40
+  __TEXT.__unwind_info: 0x3bd0
+  __DATA_CONST.__auth_got: 0x14b8
+  __DATA_CONST.__got: 0x12e8
+  __DATA_CONST.__auth_ptr: 0x158
+  __DATA_CONST.__const: 0x72c8
+  __DATA_CONST.__cfstring: 0x1ac20
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xc0

   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_intobj: 0x1098
-  __DATA_CONST.__objc_arraydata: 0x510
-  __DATA_CONST.__objc_arrayobj: 0x150
-  __DATA_CONST.__objc_dictobj: 0x1e0
-  __DATA.__objc_const: 0xbf58
-  __DATA.__objc_selrefs: 0x5818
-  __DATA.__objc_ivar: 0x8a8
+  __DATA_CONST.__objc_arraydata: 0x550
+  __DATA_CONST.__objc_arrayobj: 0x168
+  __DATA_CONST.__objc_dictobj: 0x208
+  __DATA.__objc_const: 0xbfe8
+  __DATA.__objc_selrefs: 0x5890
+  __DATA.__objc_ivar: 0x8b4
   __DATA.__objc_data: 0x11d0
-  __DATA.__data: 0x10b0
+  __DATA.__data: 0x10b8
   __DATA.__bss: 0x7f8
   __DATA.__common: 0x54
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 400C480C-463F-3919-846C-D525FB6BF9BE
-  Functions: 7459
-  Symbols:   1276
-  CStrings:  19088
+  UUID: 7EF7F0E2-8E15-3AC0-A51C-F291F3CCA247
+  Functions: 7526
+  Symbols:   1281
+  CStrings:  19194
 
Symbols:
+ _CWFGetLinkQualityOSLog
+ _SCDynamicStoreCopyMultiple
+ _dispatch_walltime
+ _kWAMessageMetricNameCarPlayJoinFailureMetrics
+ _os_eligibility_get_domain_answer
CStrings:
+ "%s didRoamFail: %d, lastRoamAge: %2.2f"
+ "%s waitForRoam: %d, plausibleRoamCandidateFound: %d, lastScanAge: %2.2f, largeNetworkEnvironment: %d, isRealTimeApplication: %d, isEdgeBss: %d"
+ "%s: %@:%@ --> %@"
+ "%s: %s low latency Tx mode"
+ "%s: AutoLeave feature is %s"
+ "%s: CarPlay PPID %@"
+ "%s: Device in Lock state over %d minutes but is being used"
+ "%s: Disconnected (%@:code=%d) SSID: %@ BSSID: %@ RSSI: %d Chan: %d ApEnv: %@(%d)"
+ "%s: Error: IOServiceAddMatchingNotification  WiFiHardwareHealthy failed"
+ "%s: Error: monitoring APPLE80211_M_RX_DATA_STALL failed"
+ "%s: Exit"
+ "%s: Failed to get OS eligibility domain %llu (errno=%d, %s)"
+ "%s: Failed to import os_eligibility_get_domain_answer!"
+ "%s: Key:%@ InterfaceName:%@"
+ "%s: No known networks!"
+ "%s: Not triggering tdImminent, we are waiting for roam based off tdImminent\n"
+ "%s: OS eligibility domain %llu=%llu"
+ "%s: Re-evaluating application state for captive websheet"
+ "%s: Rx Stall Received %@"
+ "%s: Sent Rx Stall Notification "
+ "%s: Watchdog reason string %s\n"
+ "%s: WiFiDeviceManagerSetBackgroundScan scheduled"
+ "%s: WiFiHardwareHealthy property not found"
+ "%s: Will temporarily allow captive websheet for join via recommendation UI, will expire state after %d seconds"
+ "%s: completing command with cached GAS response"
+ "%s: hwStatus %u"
+ "%s: ipServices_dict:%@"
+ "%s: isEnableIotBehavior %d"
+ "%s: network='%@' doesn't support Rx Stall recovery"
+ "%s: no known BSS for this network, assuming small environment to start"
+ "%s: reasonStr (%@)"
+ "%s: rxDataStall notification not allowed when Carplay is Active"
+ "%s: setting interface rank %s"
+ "%s: there is already a WiFiDeviceManagerSetBackgroundScan scheduled"
+ "%s: tmp:%@ --> %@"
+ "%s: updated host count: %d at MIS Service, result:%d"
+ "%s: v4:%@ v6:%@"
+ "-[WiFiUserInteractionMonitor _initPrivate]_block_invoke_4"
+ "-[WiFiUserInteractionMonitor updateLastRecommendedNetworkJoinTimestamp]"
+ "-[WiFiWatchdogMonitor setWatchdogCallback:context:]"
+ "-[WiFiXPCManager __getPassword:XPCConnection:]"
+ "1#"
+ "APPLE80211_M_RX_DATA_STALL"
+ "CARPLAY_PPID"
+ "CarPlay join timed out"
+ "CompanionSetup"
+ "IOPropertyExistsMatch"
+ "IPv4"
+ "IPv6"
+ "InterfaceName"
+ "LastRecommendedNetworkTimestamp"
+ "MIS is Restarting. misIsNANPHS %d wasMisHiddenBeforeRestart:%u"
+ "Multi AP Large"
+ "RXSTALL_REASON_CODE"
+ "RXSTALL_REPORT_CODE"
+ "T@\"NSDate\",&,N,V_lastRecommendedNetworkTimestamp"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_lastRecommendedNetworkTimestampExpirationTimer"
+ "T@?,C,N,V_watchdogCallback"
+ "T^v,N,V_watchdogContext"
+ "Tri Band Multi AP Large"
+ "WiFiDeviceIsEnableIotBehavior"
+ "WiFiDeviceUpdateOsEligibility"
+ "WiFiHardwareHealthy"
+ "WiFiManager-1975.96 Jun 18 2025 20:56:01"
+ "WiFiManager-1975.96 Jun 18 2025 20:56:25"
+ "WiFiManagerIsDomainEligible"
+ "WiFiManagerUpdateSystemHealthManager"
+ "WiFiMetricsManagerSubmitCarPlayJoinFailureMetrics"
+ "[corewifi] %s: looking into password backup on behalf of %@ for network %@"
+ "__WiFiDeviceGasCacheCallback"
+ "__WiFiDeviceManagerHandleRxDataStallEvent"
+ "__WiFiDeviceManagerSetTxModeLowLatency"
+ "__WiFiDeviceManagerSubmitCarPlayJoinFailureMetrics"
+ "__WiFiDeviceProcessRxDataStallEvent"
+ "__WiFiLQAMgrIsLargeNetworkEnvironment"
+ "__WiFiLQAMgrRecentRoamFail"
+ "__WiFiManagerWiFiHardwareHealthCallback"
+ "__fetchNetworkSignatures"
+ "__getPassword:XPCConnection:"
+ "_lastRecommendedNetworkTimestamp"
+ "_lastRecommendedNetworkTimestampExpirationTimer"
+ "_watchdogCallback"
+ "_watchdogContext"
+ "associatedNetwork"
+ "com.apple.os-eligibility-domain.change.lanthanum"
+ "dateByAddingTimeInterval:"
+ "didLastRoamFailNoCand"
+ "handleWatchdog:"
+ "lastRecommendedNetworkTimestamp"
+ "lastRecommendedNetworkTimestampExpirationTimer"
+ "networkMtu"
+ "ppid"
+ "rxDataStall: latencySensitiveApps_bitmap:%llu isCriticalAppState:%s"
+ "setLastRecommendedNetworkTimestamp:"
+ "setLastRecommendedNetworkTimestampExpirationTimer:"
+ "setNetworkFlags:"
+ "setNetworkOfInterestHomeStateUpdatedAt:"
+ "setWatchdogCallback:"
+ "setWatchdogCallback:context:"
+ "setWatchdogContext:"
+ "updateLastRecommendedNetworkJoinTimestamp"
+ "v24@0:8*16"
+ "v24@?0*8^v16"
+ "wasRecommendedNetworkRecentlyJoined"
+ "watchdogCallback"
+ "watchdogContext"
+ "wifiutil"
- "%s waitForRoam: %d, plausibleRoamCandidateFound: %d, lastScanAge: %2.2f"
- "%s: calling CB with cached GAS response"
- "%s: incorrect number of arguments (=%d)"
- "%s: nearby device recommendation (captive) joined without foreground networking app, open settings"
- "1\""
- "APPLE80211_M_RENEW_IP_REQ"
- "Join candidate does not match known network passpoint state"
- "MIS in Restarting. misIsNANPHS %d"
- "Td,N,V_lastRoamStatusFailedNoCandidateTs"
- "WiFiManager-1975.87 May 30 2025 21:11:33"
- "WiFiManager-1975.87 May 30 2025 21:11:55"
- "__WiFiDeviceProcessGasDoneEvent"
- "__getPassword:"
- "_lastRoamStatusFailedNoCandidateTs"
- "lastRoamStatusFailedNoCandidateTs"
- "setLastRoamStatusFailedNoCandidateTs:"

```
