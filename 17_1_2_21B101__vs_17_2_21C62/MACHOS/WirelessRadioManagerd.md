## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1630.1.5.0.0
-  __TEXT.__text: 0x1276b0
+1630.2.5.0.0
+  __TEXT.__text: 0x12a3fc
   __TEXT.__auth_stubs: 0x1fc0
-  __TEXT.__objc_stubs: 0x19ce0
-  __TEXT.__objc_methlist: 0xd134
-  __TEXT.__objc_methname: 0x28258
-  __TEXT.__cstring: 0x426a0
+  __TEXT.__objc_stubs: 0x1a2e0
+  __TEXT.__objc_methlist: 0xd26c
+  __TEXT.__objc_methname: 0x2860c
+  __TEXT.__cstring: 0x433a8
   __TEXT.__objc_classname: 0xcf6
-  __TEXT.__objc_methtype: 0x6a8e
-  __TEXT.__const: 0x21070
-  __TEXT.__gcc_except_tab: 0x34c8
+  __TEXT.__objc_methtype: 0x6ad9
+  __TEXT.__const: 0x21098
+  __TEXT.__gcc_except_tab: 0x35dc
   __TEXT.__dlopen_cstrs: 0x2b4
   __TEXT.__oslogstring: 0x85
-  __TEXT.__unwind_info: 0x3ecc
+  __TEXT.__unwind_info: 0x3fd4
   __TEXT.__eh_frame: 0x88
   __DATA_CONST.__auth_got: 0xff8
-  __DATA_CONST.__got: 0x470
+  __DATA_CONST.__got: 0x478
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x44d0
-  __DATA_CONST.__cfstring: 0x254a0
+  __DATA_CONST.__const: 0x4548
+  __DATA_CONST.__cfstring: 0x25b20
   __DATA_CONST.__objc_classlist: 0x3d8
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x70

   __DATA_CONST.__objc_intobj: 0x2bf8
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x17048
-  __DATA.__objc_selrefs: 0x7770
-  __DATA.__objc_classrefs: 0x508
+  __DATA.__objc_const: 0x170a8
+  __DATA.__objc_selrefs: 0x78d0
+  __DATA.__objc_classrefs: 0x520
   __DATA.__objc_superrefs: 0x400
-  __DATA.__objc_ivar: 0x1784
+  __DATA.__objc_ivar: 0x1790
   __DATA.__objc_data: 0x2670
-  __DATA.__data: 0x5a0
+  __DATA.__data: 0x5b8
   __DATA.__common: 0x13a
-  __DATA.__bss: 0x3e8
+  __DATA.__bss: 0x3f0
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /System/Library/PrivateFrameworks/AggregateDictionary.framework/AggregateDictionary
   - /System/Library/PrivateFrameworks/AssertionServices.framework/AssertionServices
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreThreadRadio.framework/CoreThreadRadio
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/GeoAnalytics.framework/GeoAnalytics
   - /System/Library/PrivateFrameworks/IDS.framework/IDS

   - /System/Library/PrivateFrameworks/SymptomReporter.framework/SymptomReporter
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomAnalytics.framework/SymptomAnalytics
   - /System/Library/PrivateFrameworks/Symptoms.framework/Frameworks/SymptomPresentationFeed.framework/SymptomPresentationFeed
+  - /System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities
   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer
   - /usr/lib/libARI.dylib

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 91A9B117-B5C5-36F0-9117-C0BC6F8EAD4A
-  Functions: 6544
-  Symbols:   728
-  CStrings:  17750
+  UUID: A25D1843-0608-3837-828C-C100562C78CC
+  Functions: 6587
+  Symbols:   732
+  CStrings:  17928
 
Symbols:
+ _OBJC_CLASS_$_CtrClient
+ _OBJC_CLASS_$_TUCallCenter
+ _OBJC_CLASS_$_WiFiP2PAWDLStateMonitor
+ _TUCallCenterCallStatusChangedNotification
CStrings:
+ " RCU2: In getRCU2Status - Reading value"
+ " RCU2: In getRCU2Status - Reading value %s"
+ " RCU2: In getRCU2Status - Reading value FAILED"
+ " RCU2: In getRCU2Status - for RCU2 state info %@"
+ " RCU2: In getRCU2Status - previousRCU2State not found"
+ " RCU2: In storeRCU2Status.."
+ " RCU2: In storeRCU2Status.. - Actual write:- failed"
+ " RCU2: In storeRCU2Status.. - Actual write:- passed"
+ " RCU2: In storeRCU2Status.. - Writing value FALSE"
+ " RCU2: In storeRCU2Status.. - Writing value TRUE"
+ "%s: sim slot %s Data indicator: %s"
+ "%s: sim slot %s ECIO %f"
+ "%s: sim slot %s NrRSRP %f"
+ "%s: sim slot %s RSCP %f"
+ "%s: sim slot %s RSRP %f"
+ "%s: sim slot %s RSRQ %f"
+ "%s: sim slot %s SNR %f"
+ "%s: sim slot %s bars %@"
+ "%s: sim slot %s data LQM %d"
+ "%s: sim slot %s data LQM is valid? %s"
+ "%s: sim slot %s isDataAttached %@"
+ "%s: sim slot %s rat property %@ rat %s"
+ "%s: sim slot %s vLQM %d"
+ "%s: sim slot %s vLQM is valid? %s"
+ "%s: slot %s RSRQ %f"
+ "%s: slot %s RSSI %f"
+ "%s: slot %s SNR %f"
+ "%s:metric is not ready"
+ "-[WRM_AWDService submitMetricsTelephonyOrFtCallEnd:]"
+ "-[WRM_EnhancedCTService dataAttachedWithCellularNetwork:]"
+ "-[WRM_EnhancedCTService getCTDataIndictor:]"
+ "-[WRM_EnhancedCTService getCellularDataLQM:]"
+ "-[WRM_EnhancedCTService getCurrentSignalBars:]"
+ "-[WRM_EnhancedCTService getLteVoiceLQM:]"
+ "-[WRM_EnhancedCTService getNrRSRP:]_block_invoke"
+ "-[WRM_EnhancedCTService getNrRSRQ:]_block_invoke"
+ "-[WRM_EnhancedCTService getNrSNR:]_block_invoke"
+ "-[WRM_EnhancedCTService getServingCellECIO:]_block_invoke"
+ "-[WRM_EnhancedCTService getServingCellRSCP:]_block_invoke"
+ "-[WRM_EnhancedCTService getServingCellRSRP:]_block_invoke"
+ "-[WRM_EnhancedCTService getServingCellRSRQ:]_block_invoke"
+ "-[WRM_EnhancedCTService getServingCellSNR:]_block_invoke"
+ "-[WRM_EnhancedCTService getServingCellType:]"
+ "-[WRM_EnhancedCTService isDataLQMValid:]"
+ "-[WRM_EnhancedCTService isVoiceLQMValid:]"
+ "@\"CtrClient\""
+ "@\"WiFiP2PAWDLStateMonitor\""
+ "CtrClientPtr"
+ "NCP:State"
+ "RCU2 Controller - HandleThreadStart - RCU2_SUPPORT_IOS - Feature not enabled"
+ "RCU2 Controller - State change event received Setting Wireless Load"
+ "RCU2 Controller - Thread radio not enabled"
+ "RCU2 Controller - Threadradio Stopped - Disabling sending messages- Current value = %d"
+ "RCU2 Controller - Threadradio started - enabling sending messages - Current value = %d"
+ "RCU2 Controller - sendFullWirelessLoad with BT load %d WiFiBand %d AWDLRealTime:%d FullValue: %llu"
+ "RCU2 Controller - setWirelessLoad Failure - Load set to %llu "
+ "RCU2 Controller - setWirelessLoad Success - Load set to %llu"
+ "Real Time AWDL State changed (%d -> %d)"
+ "TUCallCenterCallStatusChangedNotification register"
+ "^{WRMMetricsiRATFaceTimeHandover=QIqqIIIIIIBII@@III@IIIIiiiBBBBIIBi}"
+ "^{WRMMetricsiRATFaceTimeHandover=QIqqIIIIIIBII@@III@IIIIiiiBBBBIIBi}16@0:8"
+ "awdlStateMonitor"
+ "beginMonitoring"
+ "client.xpc.WirelessRadioManager"
+ "client.xpc.WirelessRadioManager.queue"
+ "d24@0:8q16"
+ "dataAttachedWithCellularNetwork:"
+ "deviceICheapFR2Coverage:%d"
+ "disconnectedReason"
+ "endMonitoring"
+ "evaluateWiFiVersusCell: m5GAvailable: %d"
+ "feedAWDMetricsCellularStatsWithUUID:"
+ "feedCellularMetricsWithUUID found matching slot=%s"
+ "feedCellularMetricsWithUUID:"
+ "fetchWrmSdmLocationDbInfoWithMcc from BB: mcc=%u, mnc=%u, cellId=%llu, simSlot=%d, lastKnown latitude=%f, longitude=%f location obtained from %fsec before"
+ "getCTDataIndictor:"
+ "getCellularDataLQM:"
+ "getCurrentSignalBars:"
+ "getLastKnownLocationTimestamp"
+ "getLteVoiceLQM:"
+ "getNrRSRP:"
+ "getNrRSRQ:"
+ "getNrSNR:"
+ "getServingCellECIO:"
+ "getServingCellRSCP:"
+ "getServingCellRSRP:"
+ "getServingCellRSRQ:"
+ "getServingCellSNR:"
+ "getServingCellType:"
+ "handleAWDLRealTimeMode:"
+ "handleBTBandwidthLoad:"
+ "handleCallNotification callType=%d,callDisconnected %@"
+ "handleCallNotification:"
+ "init:"
+ "initCallNotifications"
+ "initWithTimeIntervalSince1970:"
+ "isDataLQMValid:"
+ "isFaceTimeProvider"
+ "isTelephonyProvider"
+ "isVoiceLQMValid:"
+ "kCallSubType"
+ "kCallSubTypeTelephony"
+ "kCallSubTypeVoLTE"
+ "kCallSubTypeVoNR"
+ "kCallSubTypeWifi"
+ "kWCMBTWirelessLoadValue"
+ "localSenderIdentityUUID"
+ "mLastKnownLocationTimestamp"
+ "object"
+ "previousRCU2State"
+ "provider"
+ "providerContext"
+ "q24@0:8q16"
+ "queryLocationdDBForHarvestingData: prefix GCI:%@ total FR2: %d, total FR1: %d"
+ "queryLocationdDBForHarvestingData: updating FR2 count:%d"
+ "setClientEventsOn"
+ "setEventHandler:EventBlock:dqueue:"
+ "setIsCallFailed:"
+ "setMessageTrigger:"
+ "setMessageType:"
+ "setProperty:prperty_val:"
+ "setRealtimeModeUpdatedHandler:"
+ "state"
+ "stringValue"
+ "submitMetricsTelephonyOrFtCallEnd callFailed=%d, lat=%f, lng=%f location obtained from %fseconds before"
+ "submitMetricsTelephonyOrFtCallEnd rat= LTE, rsrp=%d, snr=%d, rsrq=%d"
+ "submitMetricsTelephonyOrFtCallEnd rat= NR, rsrp=%d, snr=%d, rsrq=%d"
+ "submitMetricsTelephonyOrFtCallEnd rat= UMTS, rsrp=%d, snr=%d"
+ "submitMetricsTelephonyOrFtCallEnd:"
+ "uuid"
+ "v24@?0{shared_ptr<CtrXPC::Event>=^{Event}^{__shared_weak_count}}8"
+ "vendor:coex:radioload"
+ "wrmSdmLocationController: invalidate location since speed %f> 30m/s"
+ "{WRMMetricsiRATFaceTimeHandover=\"timestamp\"Q\"counter\"I\"wifiRssi\"q\"wifiSNR\"q\"cca\"I\"qbssLoad\"I\"wifiRxPhyRate\"I\"wifiRxRetry\"I\"wifiTxPER\"I\"wifiTxPhyRate\"I\"captiveNetworks\"B\"stationCount\"I\"wifiEstimatedBandwitdh\"I\"iRATRecommendation\"@\"NSString\"\"iRATRecommendationReason\"@\"NSString\"\"faceTimeAction\"I\"facetimePacketLoss\"I\"facetimeDelay\"I\"ratType\"@\"NSString\"\"signalBar\"I\"bssLoad\"I\"dataLQM\"I\"voiceLQM\"I\"cellRsrp\"i\"cellRsrq\"i\"cellSnr\"i\"alertedMode\"B\"isNSAMode\"B\"isPCDetected\"B\"isStallDetected\"B\"audioErasure\"I\"videoErasure\"I\"metricsUpdate\"B\"callType\"i}"
- "%s: slot %d RSRQ %f"
- "%s: slot %d RSSI %f"
- "%s: slot %d SNR %f"
- "^{WRMMetricsiRATFaceTimeHandover=QIqqIIIIIIBII@@III@IIIIiiiBBBBIIB}"
- "^{WRMMetricsiRATFaceTimeHandover=QIqqIIIIIIBII@@III@IIIIiiiBBBBIIB}16@0:8"
- "fetchWrmSdmLocationDbInfoWithMcc from BB: mcc=%u, mnc=%u, cellId=%llu, simSlot=%d, lastKnown latitude=%f, longitude=%f"
- "wrmSdmLocationController: ClientLocationHandler callback, latitude=%f, longitude=%f, speed = %f"
- "{WRMMetricsiRATFaceTimeHandover=\"timestamp\"Q\"counter\"I\"wifiRssi\"q\"wifiSNR\"q\"cca\"I\"qbssLoad\"I\"wifiRxPhyRate\"I\"wifiRxRetry\"I\"wifiTxPER\"I\"wifiTxPhyRate\"I\"captiveNetworks\"B\"stationCount\"I\"wifiEstimatedBandwitdh\"I\"iRATRecommendation\"@\"NSString\"\"iRATRecommendationReason\"@\"NSString\"\"faceTimeAction\"I\"facetimePacketLoss\"I\"facetimeDelay\"I\"ratType\"@\"NSString\"\"signalBar\"I\"bssLoad\"I\"dataLQM\"I\"voiceLQM\"I\"cellRsrp\"i\"cellRsrq\"i\"cellSnr\"i\"alertedMode\"B\"isNSAMode\"B\"isPCDetected\"B\"isStallDetected\"B\"audioErasure\"I\"videoErasure\"I\"metricsUpdate\"B}"

```
