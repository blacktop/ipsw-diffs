## wifianalyticsd

> `/usr/libexec/wifianalyticsd`

```diff

-805.6.0.0.0
-  __TEXT.__text: 0xa07ec
-  __TEXT.__auth_stubs: 0x15b0
-  __TEXT.__objc_stubs: 0x8b60
-  __TEXT.__objc_methlist: 0x34fc
-  __TEXT.__const: 0x4a0
+825.52.0.0.0
+  __TEXT.__text: 0x97e2c
+  __TEXT.__auth_stubs: 0x1740
+  __TEXT.__objc_stubs: 0x8e00
+  __TEXT.__objc_methlist: 0x35bc
+  __TEXT.__const: 0x4b0
   __TEXT.__dlopen_cstrs: 0x1e2
-  __TEXT.__objc_classname: 0x45d
-  __TEXT.__constg_swiftt: 0x494
-  __TEXT.__swift5_typeref: 0x276
+  __TEXT.__objc_classname: 0x430
+  __TEXT.__constg_swiftt: 0x464
+  __TEXT.__swift5_typeref: 0x294
   __TEXT.__swift5_fieldmd: 0x1ec
-  __TEXT.__oslogstring: 0x14457
-  __TEXT.__swift5_types: 0x30
-  __TEXT.__cstring: 0x14032
-  __TEXT.__objc_methname: 0xdd0f
+  __TEXT.__oslogstring: 0x14ac5
+  __TEXT.__swift5_types: 0x2c
+  __TEXT.__cstring: 0x14182
+  __TEXT.__objc_methname: 0xe0cf
   __TEXT.__swift5_reflstr: 0x12b
   __TEXT.__swift5_capture: 0xdc
-  __TEXT.__objc_methtype: 0x1127
-  __TEXT.__gcc_except_tab: 0x50b4
-  __TEXT.__unwind_info: 0x1318
+  __TEXT.__objc_methtype: 0x116c
+  __TEXT.__gcc_except_tab: 0x4b10
+  __TEXT.__unwind_info: 0x1030
   __TEXT.__eh_frame: 0x90
-  __DATA_CONST.__auth_got: 0xaf0
-  __DATA_CONST.__got: 0x440
-  __DATA_CONST.__auth_ptr: 0x80
-  __DATA_CONST.__const: 0x1a60
-  __DATA_CONST.__cfstring: 0x10780
+  __DATA_CONST.__const: 0x1a48
+  __DATA_CONST.__cfstring: 0x10900
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb8
-  __DATA_CONST.__objc_arraydata: 0x1f90
-  __DATA_CONST.__objc_dictobj: 0x1978
+  __DATA_CONST.__objc_arraydata: 0x1fd8
+  __DATA_CONST.__objc_dictobj: 0x19a0
   __DATA_CONST.__objc_intobj: 0x438
   __DATA_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_const: 0x5620
-  __DATA.__objc_selrefs: 0x2e30
-  __DATA.__objc_ivar: 0x50c
+  __DATA_CONST.__auth_got: 0xbb8
+  __DATA_CONST.__got: 0x458
+  __DATA_CONST.__auth_ptr: 0x80
+  __DATA.__objc_const: 0x5740
+  __DATA.__objc_selrefs: 0x2ee0
+  __DATA.__objc_ivar: 0x524
   __DATA.__objc_data: 0x9f8
   __DATA.__data: 0x998
   __DATA.__bss: 0x208

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FBFFB19D-6D07-3D45-A591-7AA32DF048C8
-  Functions: 1496
-  Symbols:   525
-  CStrings:  8395
+  UUID: B8BEC824-5D8B-33E7-A27E-8ED58758DEEB
+  Functions: 1510
+  Symbols:   553
+  CStrings:  8480
 
Symbols:
+ _OBJC_CLASS_$_WAClient
+ _OBJC_CLASS_$_WAEventDiagnosticState
+ _OBJC_CLASS_$_WAEventRecovery
+ _kCFBooleanTrue
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x9
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
- _$sSo10CFErrorRefas5Error10FoundationMc
- __swift_stdlib_bridgeErrorToNSError
- _swift_allocError
CStrings:
+ "\"WiFiAnalytics_executables-825.52\""
+ "%{public}s::%d:BE: durationSinceLastFailure[@6s] %u"
+ "%{public}s::%d:BK: durationSinceLastFailure[@6s] %u"
+ "%{public}s::%d:Channels array exists but count is 0"
+ "%{public}s::%d:Channels dict exists but kIOReportChannelsKey array is NULL"
+ "%{public}s::%d:Channels doesn't exist (NULL)"
+ "%{public}s::%d:Current cache already contains CoreCapture channels, skipping redundant CCLogPipe query"
+ "%{public}s::%d:Current cache does not contain CoreCapture, querying CCLogPipe directly"
+ "%{public}s::%d:DPS: NAN Status:%s RTG:%s"
+ "%{public}s::%d:Found CoreCapture channel in current cache: group=%@"
+ "%{public}s::%d:Invalid AC %d encountered\n"
+ "%{public}s::%d:No CoreCapture channels found in current cache"
+ "%{public}s::%d:No tx status on AC:%@ in the last 6.5 seconds\n"
+ "%{public}s::%d:QDPS: Recommendation - kQuickDPSReassoc, triggering Reassoc with reason kQuickDPSRecoveryReassocCCReason"
+ "%{public}s::%d:QDPS: Unhandled case: doReset=%d timeDifference=%d threshold=%d\n"
+ "%{public}s::%d:RSSI-bin:%d raw-RSSI:%d band:%d rssiThreshold:%d\n"
+ "%{public}s::%d:SDPS: Aborting sDPS recovery since WiFi got disassociated atleast once since initial trigger"
+ "%{public}s::%d:Triggering Reassoc for Quick DPS in chip:%@ interface:%@ apple80211InstanceValid:%@"
+ "%{public}s::%d:VI: durationSinceLastFailure[@6s] %u"
+ "%{public}s::%d:VO: durationSinceLastFailure[@6s] %u"
+ "%{public}s::%d:WiFiInterface:: NetworkService Not Enabled!\n"
+ "%{public}s::%d:WiFiInterface:: Reachable:%s ConnectionRequired:%s interventionRequired:%s\n"
+ "%{public}s::%d:WiFiInterface::IPV4: Routable:%s Primary:%s (Addresses:%@)\n"
+ "%{public}s::%d:WiFiInterface::IPV6: Routable:%s Primary:%s (Addresses:%@)\n"
+ "%{public}s::%d:channel: %u channelBandwidth: %u band: %d"
+ "%{public}s::%d:downgradeToReassocRecovery: returning %s\n"
+ "%{public}s::%d:downgradeToReassocRecovery: returning NO\n"
+ "%{public}s::%d:force_dns_failures_symptoms_dps Preference is %s"
+ "%{public}s::%d:force_ping_failures_symptoms_dps Preference is %s"
+ "%{public}s::%d:quick_dps_rssi_threshold_6g Preference is %ld"
+ "-[DPSQuickRecoveryRecommendationEngine recommendReset:currentSample:acList:qDpsStat:chipNumber:dpsSnapshot:originalCCA:aggregateFailureSnaphot:driverType:nanEnabled:downgrade:activeRTG:]"
+ "-[WAApple80211 triggerReassociation:metaData:]"
+ "-[WAEngine downgradeToReassocRecovery:]"
+ "-[WAEngine isWiFiRoutableAndPrimary]"
+ "-[WAIOReporterMessagePopulator doesCurrentCacheContainCoreCaptureChannels:]"
+ "Active"
+ "B28@0:8B16@20"
+ "Band"
+ "Band State"
+ "C24@0:8^{__CFDictionary=}16"
+ "DPSN_activeRTGTraffic"
+ "IPv4RouterAddress"
+ "IPv6RouterAddress"
+ "IS_DPS"
+ "Interface Average CCA"
+ "May 29 2026 20:10:30"
+ "NWAIS_bands"
+ "Q96@0:8@16@24@32@40@48@56I64@68q76B84B88B92"
+ "QuickDPSRecovery-Reassoc"
+ "RTGGating:qDpsStat:"
+ "SlowDpsAbortedDueToLinkStateChange"
+ "TB,N,V_activeRTGTraffic"
+ "TB,N,V_force_dns_failures_symptoms_dps"
+ "TB,N,V_force_ping_failures_symptoms_dps"
+ "TQ,N,V_quick_dps_rssi_threshold_6g"
+ "Ts,N,V_currentInfraBand"
+ "WiFiAnalytics_executables-825.52"
+ "WiFiAnalytics_executables-825.52 May 29 2026 20:10:29"
+ "_activeRTGTraffic"
+ "_currentInfraBand"
+ "_force_dns_failures_symptoms_dps"
+ "_force_ping_failures_symptoms_dps"
+ "_quick_dps_rssi_threshold_6g"
+ "activeRTGTraffic"
+ "asyncSubmitEvent:"
+ "currentInfraBand"
+ "doesCurrentCacheContainCoreCaptureChannels:"
+ "downgradeToReassocRecovery:"
+ "force_dns_failures_symptoms_dps"
+ "force_ping_failures_symptoms_dps"
+ "globalIPv4Addresses"
+ "globalIPv4RouterAddress"
+ "globalIPv6Addresses"
+ "globalIPv6InterfaceName"
+ "globalIPv6RouterAddress"
+ "initWithBssid:reason:type:apple80211Return:at:data:withLqmHistory:withError:"
+ "initWithName:description:uuid:at:data:withLqmHistory:withError:"
+ "interfaceName"
+ "isNetworkServiceEnabled"
+ "isWiFiRoutableAndPrimary"
+ "kActiveRTGTraffic"
+ "kHighNANActivitySuspected"
+ "quick_dps_rssi_threshold_6g"
+ "reachabilityFlags"
+ "recommendReset:currentSample:acList:qDpsStat:chipNumber:dpsSnapshot:originalCCA:aggregateFailureSnaphot:driverType:nanEnabled:downgrade:activeRTG:"
+ "s16@0:8"
+ "setActiveRTGTraffic:"
+ "setCurrentInfraBand:"
+ "setForce_dns_failures_symptoms_dps:"
+ "setForce_ping_failures_symptoms_dps:"
+ "setQuick_dps_rssi_threshold_6g:"
+ "sharedClient"
+ "stringByTrimmingCharactersInSet:"
+ "submitEvent:withError:"
+ "triggerReassociation:metaData:"
+ "v20@0:8s16"
- "\"WiFiAnalytics_executables-805.6\""
- "%{public}s::%d:Aborting Quick DPS recovery action due to notification/study delay"
- "%{public}s::%d:DPS: NAN Status:%s"
- "%{public}s::%d:QDPS: Unhandled case"
- "%{public}s::%d:RSSI-bin:%d raw-RSSI:%d\n"
- "%{public}s::%d:Reseting (fast reset recovery)... to recover from DPS at 6s stall checkpoint."
- "%{public}s::%d:channel: %u channelBandwidth: %u"
- "-[DPSQuickRecoveryRecommendationEngine recommendReset:currentSample:acList:qDpsStat:chipNumber:dpsSnapshot:originalCCA:aggregateFailureSnaphot:driverType:nanEnabled:]"
- "-[ManagedConfiguration profileChangedCallback:]_block_invoke_2"
- "-[WAApple80211 triggerReassociation:]"
- "Apr 18 2026 18:25:11"
- "Interface Avgerage CCA"
- "Q88@0:8@16@24@32@40@48@56I64@68q76B84"
- "WiFiAnalytics_executables-805.6"
- "WiFiAnalytics_executables-805.6 Apr 18 2026 18:25:07"
- "diagnosticEventAt:with:"
- "recommendReset:currentSample:acList:qDpsStat:chipNumber:dpsSnapshot:originalCCA:aggregateFailureSnaphot:driverType:nanEnabled:"
- "recoveryEventOnBssid:at:with:"
- "setApple80211Return:"
- "setDesc:"
- "setEnabled:"
- "setName:"
- "setRecoveryReason:"
- "setRecoveryType:"
- "triggerReassociation:"
- "v16@?0@\"WADeviceAnalyticsDiagnosticStateRecord\"8"
- "v16@?0@\"WADeviceAnalyticsRecoveryRecord\"8"

```
