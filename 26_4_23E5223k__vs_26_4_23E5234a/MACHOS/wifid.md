## wifid

> `/usr/sbin/wifid`

```diff

-1995.26.5.0.0
-  __TEXT.__text: 0x1a8b34
-  __TEXT.__auth_stubs: 0x2960
-  __TEXT.__objc_stubs: 0x134e0
-  __TEXT.__objc_methlist: 0x5fb0
+1995.26.6.0.0
+  __TEXT.__text: 0x1a82a8
+  __TEXT.__auth_stubs: 0x2940
+  __TEXT.__objc_stubs: 0x132c0
+  __TEXT.__objc_methlist: 0x5da0
   __TEXT.__gcc_except_tab: 0x1f78
   __TEXT.__const: 0xd7b
-  __TEXT.__cstring: 0x6bfa2
-  __TEXT.__objc_methname: 0x1885e
-  __TEXT.__objc_classname: 0x7e3
-  __TEXT.__objc_methtype: 0x33ca
+  __TEXT.__cstring: 0x6bcd8
+  __TEXT.__objc_methname: 0x18243
+  __TEXT.__objc_classname: 0x7c3
+  __TEXT.__objc_methtype: 0x3041
   __TEXT.__oslogstring: 0x1ff0
   __TEXT.__ustring: 0x4c2
   __TEXT.__dlopen_cstrs: 0x1a5
-  __TEXT.__unwind_info: 0x4050
-  __DATA_CONST.__auth_got: 0x14c0
+  __TEXT.__unwind_info: 0x4028
+  __DATA_CONST.__auth_got: 0x14b0
   __DATA_CONST.__got: 0x12f8
   __DATA_CONST.__auth_ptr: 0x158
   __DATA_CONST.__const: 0x74c0
-  __DATA_CONST.__cfstring: 0x1b780
+  __DATA_CONST.__cfstring: 0x1b740
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x1a0

   __DATA_CONST.__objc_arraydata: 0x5f0
   __DATA_CONST.__objc_arrayobj: 0x168
   __DATA_CONST.__objc_dictobj: 0x208
-  __DATA.__objc_const: 0xc368
-  __DATA.__objc_selrefs: 0x5c00
-  __DATA.__objc_ivar: 0x8e8
+  __DATA.__objc_const: 0xc168
+  __DATA.__objc_selrefs: 0x5a88
+  __DATA.__objc_ivar: 0x8d0
   __DATA.__objc_data: 0x11d0
-  __DATA.__data: 0x1118
+  __DATA.__data: 0x10b8
   __DATA.__bss: 0x7f8
   __DATA.__common: 0x58
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: F999C5A1-383D-3A63-8DBE-345BE53F443A
-  Functions: 8261
-  Symbols:   1284
-  CStrings:  19617
+  UUID: 88A3F6DD-94A8-3716-B241-FBA8ABB23126
+  Functions: 8240
+  Symbols:   1282
+  CStrings:  19520
 
Symbols:
- __CTServerConnectionGetSupportedEnhancedLinkQualityMetric
- __CTServerConnectionRegisterSupportedEnhancedLinkQualityMetric
CStrings:
+ "%s waitForRoam: %d, plausibleRoamCandidateFound: %d, lastScanAge: %2.2f, largeNetworkEnvironment: %d, isRealTimeApplication: %d, isEdgeBss: %d"
+ "WiFiManager-1995.26.6 Mar  5 2026 23:59:36"
+ "WiFiManager-1995.26.6 Mar  6 2026 00:00:05"
- "%s Suboptimal Wi-Fi but Cell is unusable; overriding TrgDisc decision"
- "%s waitForRoam: %d, plausibleRoamCandidateFound: %d, lastScanAge: %2.2f, largeNetworkEnvironment: %d, isRealTimeApplication: %d, isEdgeBss: %d, isRecentCellLQMAbort: %d"
- "%s: Fast Disconnect not triggered - Cell LQM is ABORT"
- "%s: created CoreTelephonyClient for eLQM notifications"
- "%s: data slot changed from %ld to %ld"
- "%s: eLQM not supported or query failed, error=(%d,%d)"
- "%s: eLQM updated (payload = %@): (LQM = %d, RRC = %u, INTF = %u)"
- "%s: failed to register for eLQM, error=(%d,%d)"
- "%s: ignoring eLQM for non-active slot %ld (active: %ld)"
- "%s: refreshed data slot from %ld to %ld"
- "%s: registered for eLQM notifications"
- "-[WiFiUserInteractionMonitor dataSubscriptionContextChanged:]"
- "-[WiFiUserInteractionMonitor enhancedDataLinkQualityChanged:metric:]"
- "@\"CoreTelephonyClient\""
- "CellulareLQM"
- "CoreTelephonyClientDataDelegate"
- "LQM:%d RRC:%u Interface:%u"
- "T@\"CoreTelephonyClient\",&,N,V_ctClient"
- "TC,N,V_cellularInterfaceAvailable"
- "TC,N,V_cellularRRCState"
- "Tc,N,V_cellularLQM"
- "Td,N,V_latesteLQMTimestamp"
- "Tq,N,V_currentDataSlotID"
- "WiFiManager-1995.26.5 Feb 26 2026 23:20:19"
- "WiFiManager-1995.26.5 Feb 26 2026 23:20:46"
- "_cellularInterfaceAvailable"
- "_cellularLQM"
- "_cellularRRCState"
- "_ctClient"
- "_currentDataSlotID"
- "_latesteLQMTimestamp"
- "anbrActivationState:enabled:"
- "anbrBitrateRecommendation:bitrate:direction:"
- "cellLQMUpdatedTimestamp"
- "cellularInterfaceAvailable"
- "cellularLQM"
- "cellularRRCState"
- "connectionActivationError:connection:error:"
- "connectionAvailability:availableConnections:"
- "connectionStateChanged:connection:dataConnectionStatusInfo:"
- "ctClient"
- "currentCellularInterfaceAvailable"
- "currentCellularLQM"
- "currentCellularRRCState"
- "currentDataServiceDescriptorChanged:"
- "currentDataSimChanged:"
- "currentDataSlotID"
- "dataRoamingSettingsChanged:status:"
- "dataSettingsChanged:"
- "dataStatus:dataStatusInfo:"
- "dataSubscriptionContextChanged:"
- "enhancedDataLinkQualityChanged:metric:"
- "enhancedLinkQuality"
- "getCurrentDataSubscriptionContextSync:"
- "internetConnectionActivationError:"
- "internetConnectionAvailability:"
- "internetConnectionStateChanged:"
- "internetDataStatus:"
- "internetDataStatusBasic:"
- "isRecentCellLQMAbort"
- "latesteLQMTimestamp"
- "metricType"
- "nrSliceAppStateChanged:status:trafficDescriptors:"
- "nrSlicedRunningAppStateChanged:"
- "preferredDataServiceDescriptorChanged:"
- "preferredDataSimChanged:"
- "regDataModeChanged:dataMode:"
- "serviceDisconnection:status:"
- "servingNetworkChanged:"
- "setCellularInterfaceAvailable:"
- "setCellularLQM:"
- "setCellularRRCState:"
- "setCtClient:"
- "setCurrentDataSlotID:"
- "setLatesteLQMTimestamp:"
- "slotID"
- "tetheringStatus:"
- "tetheringStatus:connectionType:"
- "v24@0:8@\"CTDataConnectionStatus\"16"
- "v24@0:8@\"CTDataSettings\"16"
- "v24@0:8@\"CTDataStatus\"16"
- "v24@0:8@\"CTDataStatusBasic\"16"
- "v24@0:8@\"CTServiceDescriptor\"16"
- "v24@0:8@\"CTSlicedRunningAppInfoContainer\"16"
- "v24@0:8@\"CTTetheringStatus\"16"
- "v24@0:8@\"CTXPCServiceSubscriptionContext\"16"
- "v28@0:8@\"CTServiceDescriptor\"16B24"
- "v28@0:8@\"CTTetheringStatus\"16i24"
- "v28@0:8@\"CTXPCServiceSubscriptionContext\"16B24"
- "v28@0:8@\"CTXPCServiceSubscriptionContext\"16i24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTDataStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"CTServiceDisconnectionStatus\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSArray\"24"
- "v32@0:8@\"CTXPCServiceSubscriptionContext\"16i24i28"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16@\"NSNumber\"24i32"
- "v36@0:8@\"CTXPCServiceSubscriptionContext\"16i24@\"CTDataConnectionStatus\"28"
- "v36@0:8@\"NSString\"16B24@\"CTTrafficDescriptorsContainer\"28"
- "v36@0:8@16B24@28"

```
