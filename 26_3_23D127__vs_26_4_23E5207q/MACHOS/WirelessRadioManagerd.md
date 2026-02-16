## WirelessRadioManagerd

> `/usr/sbin/WirelessRadioManagerd`

```diff

-1860.5.1.0.0
-  __TEXT.__text: 0x15fc2c
-  __TEXT.__auth_stubs: 0x24a0
-  __TEXT.__objc_stubs: 0x1e3c0
+1870.4.0.0.0
+  __TEXT.__text: 0x165a50
+  __TEXT.__auth_stubs: 0x2460
+  __TEXT.__objc_stubs: 0x1efe0
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0x102a4
-  __TEXT.__gcc_except_tab: 0x5230
-  __TEXT.__const: 0x18c60
-  __TEXT.__cstring: 0x4e443
-  __TEXT.__objc_classname: 0x10aa
-  __TEXT.__objc_methname: 0x2fabb
-  __TEXT.__objc_methtype: 0x79e7
+  __TEXT.__objc_methlist: 0x10894
+  __TEXT.__gcc_except_tab: 0x5454
+  __TEXT.__const: 0x18cf0
+  __TEXT.__cstring: 0x502c4
+  __TEXT.__objc_classname: 0x10da
+  __TEXT.__objc_methname: 0x30728
+  __TEXT.__objc_methtype: 0x7a90
   __TEXT.__dlopen_cstrs: 0x3ca
   __TEXT.__oslogstring: 0x90
-  __TEXT.__unwind_info: 0x46f0
-  __DATA_CONST.__auth_got: 0x1268
+  __TEXT.__unwind_info: 0x4b10
+  __DATA_CONST.__auth_got: 0x1248
   __DATA_CONST.__got: 0x710
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x4db0
-  __DATA_CONST.__cfstring: 0x2d380
-  __DATA_CONST.__objc_classlist: 0x4e0
+  __DATA_CONST.__const: 0x4e68
+  __DATA_CONST.__cfstring: 0x2dd00
+  __DATA_CONST.__objc_classlist: 0x4f0
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x508
+  __DATA_CONST.__objc_superrefs: 0x518
   __DATA_CONST.__objc_intobj: 0x3558
-  __DATA_CONST.__objc_arraydata: 0x12810
+  __DATA_CONST.__objc_arraydata: 0x12870
   __DATA_CONST.__objc_arrayobj: 0x80d0
   __DATA_CONST.__objc_dictobj: 0x7a8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1a3e0
-  __DATA.__objc_selrefs: 0x9158
-  __DATA.__objc_ivar: 0x1b3c
-  __DATA.__objc_data: 0x30c0
+  __DATA.__objc_const: 0x1ae58
+  __DATA.__objc_selrefs: 0x9440
+  __DATA.__objc_ivar: 0x1c08
+  __DATA.__objc_data: 0x3160
   __DATA.__data: 0x760
-  __DATA.__common: 0x1e1
-  __DATA.__bss: 0x5c0
+  __DATA.__bss: 0x5d8
+  __DATA.__common: 0x1e9
   - /System/Library/Frameworks/CallKit.framework/CallKit
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B847F6F-D038-3D53-9659-F4E7FEDD2641
-  Functions: 7047
-  Symbols:   816
-  CStrings:  21158
+  UUID: DFE95133-EC92-3CAC-950E-9612AEF0D5B7
+  Functions: 7209
+  Symbols:   812
+  CStrings:  21509
 
Symbols:
+ _WiFiDeviceClientRegisterSDBOpModeChangeCallback
+ __ZNSt3__132__internal_log_hardening_failureEPKc
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x28
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:293: libc++ Hardening assertion __k != __leftmost failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:603: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:615: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:633: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:638: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:669: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:682: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:692: libc++ Hardening assertion __first != __end failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__algorithm/sort.h:697: libc++ Hardening assertion __last != __begin failed: Would read out of bounds, does your comparator satisfy the strict-weak ordering requirement?\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:410: libc++ Hardening assertion __n < size() failed: vector[] index out of bounds\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:425: libc++ Hardening assertion !empty() failed: front() called on an empty vector\n"
+ "/AppleInternal/Library/BuildRoots/4~CHwYugBHUAGXWSkzrqzpwrh16Ix38lcYg_L83Dw/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__vector/vector.h:433: libc++ Hardening assertion !empty() failed: back() called on an empty vector\n"
+ "@\"WRM_CoexRFMetrics\""
+ "COEX_OUTLIER_DETECTION"
+ "MCS: %lu, PMode: %lu, GI: %lu, NSS: %lu, CCH: %@, COEX mode: %lu"
+ "NotifyiRATClients - Sending to CoexWI Radio Stats Evaluator"
+ "QMI.NAS.%d: Send Gaming Status message state."
+ "QMI.NAS.%d: failed to send Gaming Status message. Error %d %s"
+ "QMI.NAS.%d: notifyGamingStatus status: %d"
+ "RCU2 Controller No Change in WiFi Band/Channel - Not Updating"
+ "RCU2 Controller WiFi band changed from %d to %d and channel from %ld to %ld"
+ "Receivd WiFi controller event controller %p"
+ "T@\"NSDate\",&,N,V_creationTimestamp"
+ "T@\"NSDictionary\",&,N,V_wcmWiFiBTCoexProfileSDB"
+ "TB,N,V_isFR1"
+ "TB,N,V_nsaEnabled"
+ "TB,V_clientStarted"
+ "TI,N,V_cellARFCN"
+ "TI,N,V_cellLqmScore"
+ "TI,N,V_devicePointOfInterest"
+ "TI,N,V_lqmScoreWifi"
+ "TI,N,V_phyRate"
+ "TI,N,V_rrcState"
+ "TI,N,V_rxRate"
+ "TI,N,V_rxRetransmissionRate"
+ "TI,N,V_rxRetry"
+ "TI,N,V_txPER"
+ "TI,N,V_txRate"
+ "TI,N,V_txRetransmissionRate"
+ "TI,N,V_wifiCapability"
+ "TI,N,V_wifiChannelBW"
+ "TI,N,V_wifiChannelType"
+ "TQ,N,V_btWiFiCoexState"
+ "TQ,N,V_wifichannel"
+ "TQ,N,V_wifiguardinterval"
+ "TQ,N,V_wifimcsindex"
+ "TQ,N,V_wifinumberOfSpatialStreams"
+ "Td,N,V_cellAchievedBandwidth"
+ "Td,N,V_cellChannelBandwidth"
+ "Td,N,V_cellEstimatedBandwidth"
+ "Td,N,V_cellMaxAchievedBandwidth"
+ "Td,N,V_cellPreviousBandwidth"
+ "Td,N,V_lteRSRP"
+ "Td,N,V_lteRSRQ"
+ "Td,N,V_lteSINR"
+ "Td,N,V_nrRSRP"
+ "Td,N,V_nrRSRQ"
+ "Td,N,V_nrSNR"
+ "Ti,N,V_bandInfo"
+ "Ti,N,V_cca"
+ "Ti,N,V_nrType"
+ "Ti,N,V_ratType"
+ "Ti,N,V_rssi"
+ "Ti,N,V_snr"
+ "Ti,N,V_weightedAverageRssi"
+ "Ti,N,V_weightedAverageSnr"
+ "WCM_WiFiService getSDBStatus default implementation"
+ "WRM_CoexRFMetrics"
+ "WRM_CoexRadioStatsEvalManager"
+ "WRM_CoexRadioStatsEvalManagerSingleton"
+ "WRM_CoexWI initialized"
+ "WRM_CoexWI: Added metrics to buffer, count: %lu"
+ "WRM_CoexWI: CT or SC service is nil, cannot update cellular metrics"
+ "WRM_CoexWI: Cannot submit metrics to CA, RF metrics are nil"
+ "WRM_CoexWI: Cannot submit metrics to CA, metrics buffer is empty"
+ "WRM_CoexWI: Cannot submit metrics to CA, streaming metrics are nil"
+ "WRM_CoexWI: Exception while copying metrics: %@"
+ "WRM_CoexWI: Exception while updating cellular metrics: %@"
+ "WRM_CoexWI: Exception while updating metrics: %@"
+ "WRM_CoexWI: Failed to copy basic WiFi metrics: %@"
+ "WRM_CoexWI: Failed to copy cellular bandwidth metrics: %@"
+ "WRM_CoexWI: Failed to copy cellular radio technology metrics: %@"
+ "WRM_CoexWI: Failed to copy cellular signal metrics: %@"
+ "WRM_CoexWI: Failed to copy channel metrics: %@"
+ "WRM_CoexWI: Failed to copy rate metrics: %@"
+ "WRM_CoexWI: Failed to create CWFInterface"
+ "WRM_CoexWI: Failed to determine FR type for NR: %@"
+ "WRM_CoexWI: Failed to determine FR type: %@"
+ "WRM_CoexWI: Failed to get LTE metrics: %@"
+ "WRM_CoexWI: Failed to get NR metrics in NSA mode: %@"
+ "WRM_CoexWI: Failed to get NR metrics: %@"
+ "WRM_CoexWI: Failed to get RRC state or ARFCN: %@"
+ "WRM_CoexWI: Failed to get UMTS metrics: %@"
+ "WRM_CoexWI: Failed to get bandwidth metrics: %@"
+ "WRM_CoexWI: Failed to get cellular LQM score: %@"
+ "WRM_CoexWI: Failed to get channel metrics: %@"
+ "WRM_CoexWI: Failed to get data indicator: %@"
+ "WRM_CoexWI: Failed to get rate metrics: %@"
+ "WRM_CoexWI: Failed to get serving cell type: %@"
+ "WRM_CoexWI: Failed to update basic metrics: %@"
+ "WRM_CoexWI: No session found for processId %d"
+ "WRM_CoexWI: Reported %lu metrics to CA"
+ "WRM_CoexWI: Source metrics is nil, cannot copy"
+ "WRM_CoexWI: Successfully copied all metrics"
+ "WRM_CoexWI: Successfully submitted %lu complete metrics to CA"
+ "WRM_CoexWI: Successfully submitted all metrics to CA"
+ "WRM_CoexWI: Successfully submitted streaming metrics to CA"
+ "WRM_CoexWI: Successfully updated metrics from WiFi service"
+ "WRM_CoexWI: Updated WiFi metrics - RSSI: %d, SNR: %d, TxRate: %u, RxRate: %u"
+ "WRM_CoexWI: Updated cellular metrics - RAT: %d, LTE RSRP: %.2f, LTE SINR: %.2f, NR RSRP: %.2f, NR SNR: %.2f, LQM: %u, RRC State: %u, ARFCN: %u"
+ "WRM_CoexWI: Updated cellular metrics and added to buffer, count: %lu"
+ "WRM_CoexWI: WiFi controller not available"
+ "WRM_CoexWI: WiFi service is nil, cannot update metrics"
+ "WRM_CoexWI: WiFi service not available"
+ "WRM_CoexWI: deallocated"
+ "WRM_CoexWI: received WiFi LQM update"
+ "WRM_CoexWI: updateControllerState - no args"
+ "WiFiBtSDBProfile"
+ "WiFiS: callbackWiFiDeviceClientSDBOpModeChangeCallback sdBOn: %d"
+ "_bandInfo"
+ "_btWiFiCoexState"
+ "_cellAchievedBandwidth"
+ "_cellChannelBandwidth"
+ "_cellEstimatedBandwidth"
+ "_cellLqmScore"
+ "_cellMaxAchievedBandwidth"
+ "_cellPreviousBandwidth"
+ "_clientStarted"
+ "_creationTimestamp"
+ "_devicePointOfInterest"
+ "_isFR1"
+ "_lqmScoreWifi"
+ "_lteRSRP"
+ "_lteRSRQ"
+ "_lteSINR"
+ "_nrRSRP"
+ "_nrRSRQ"
+ "_nrSNR"
+ "_nrType"
+ "_nsaEnabled"
+ "_phyRate"
+ "_rssi"
+ "_rxRate"
+ "_rxRetransmissionRate"
+ "_rxRetry"
+ "_snr"
+ "_txPER"
+ "_txRate"
+ "_txRetransmissionRate"
+ "_wcmWiFiBTCoexProfileSDB"
+ "_weightedAverageRssi"
+ "_weightedAverageSnr"
+ "_wifiCapability"
+ "_wifiChannelBW"
+ "_wifiChannelType"
+ "_wifichannel"
+ "_wifimcsindex"
+ "bandInfo"
+ "cellAchievedBandwidth"
+ "cellChannelBandwidth"
+ "cellEstimatedBandwidth"
+ "cellLqmScore"
+ "cellMaxAchievedBandwidth"
+ "cellPreviousBandwidth"
+ "clientStart"
+ "clientStop"
+ "com.apple.CoexManager.MipcDriver.CellularController"
+ "com.apple.Telephony.Test.wrmCoexReport"
+ "com.apple.WRM_CoexRadioStatsEvalManager"
+ "com.apple.games"
+ "copyMetricsFrom:"
+ "createMetricsDictionaryFrom:"
+ "creationTimestamp"
+ "feedCoreWiFiMetrics"
+ "getCellularMetricsForMLPrediction"
+ "getSDBStatus"
+ "getWiFiMetricsForMLPrediction"
+ "handleGamingStateChange skip, some apps are still active %@"
+ "handleGamingStateChange state= %d, appId=%@"
+ "handleGamingStateChange:appId:"
+ "handleWiFiBTCoexChange Setting SDB profile"
+ "handleWiFiBTCoexChange Setting default profile"
+ "isMav25PlusDevice"
+ "lteRSRP"
+ "lteRSRQ"
+ "lteSINR"
+ "mCellularControllerQueue"
+ "mMetricsBuffer"
+ "mMetricsCount"
+ "mRFMetrics"
+ "mSDBOn"
+ "notifyGamingStatus:"
+ "nrType"
+ "nsaEnabled"
+ "postBBNotification NOT calling notifyGamingStatus : mIBIClient: %x"
+ "postBBNotification calling notifyGamingStatus : mQMINasClientPrimary: %x"
+ "reportCollectedMetrics"
+ "resetMetrics"
+ "rssi"
+ "rxRate"
+ "setBandInfo:"
+ "setBtWiFiCoexState:"
+ "setCellAchievedBandwidth:"
+ "setCellChannelBandwidth:"
+ "setCellEstimatedBandwidth:"
+ "setCellLqmScore:"
+ "setCellMaxAchievedBandwidth:"
+ "setCellPreviousBandwidth:"
+ "setClientStarted:"
+ "setCreationTimestamp:"
+ "setDevicePointOfInterest:"
+ "setIsFR1:"
+ "setLqmScoreWifi:"
+ "setLteRSRP:"
+ "setLteRSRQ:"
+ "setLteSINR:"
+ "setNrType:"
+ "setNsaEnabled:"
+ "setPhyRate:"
+ "setRssi:"
+ "setRxRate:"
+ "setRxRetransmissionRate:"
+ "setRxRetry:"
+ "setSnr:"
+ "setTxPER:"
+ "setTxRate:"
+ "setTxRetransmissionRate:"
+ "setWcmWiFiBTCoexProfileSDB:"
+ "setWeightedAverageRssi:"
+ "setWeightedAverageSnr:"
+ "setWifiCapability:"
+ "setWifiChannelBW:"
+ "setWifiChannelType:"
+ "setWifichannel:"
+ "setWifimcsindex:"
+ "snr"
+ "submitCollectedMetricsToCA"
+ "submitMetricsToCA"
+ "submitMetricsToCA:"
+ "txPER"
+ "txRate"
+ "updateBasicMetricsFromWiFiService:"
+ "updateCellularMetrics"
+ "updateCellularMetricsFromCTService:scService:"
+ "updateMetricsFromWiFiService:"
+ "updateRateAndChannelMetricsFromWiFiService:"
+ "updateWiFiBand:andChannel:"
+ "updateWiFiMetrics"
+ "v16@?0^{GamingStatus=B}8"
+ "v24@0:8^{WRMMetricsiRATStreaming=QIIIIIIIiIIIIIIqIIIIIIIIIIIIIIIIIIIIIIIIIIII@IIIIIIIICIIIiiiiiiiIIIIIBBiiiiIIIII@IIIIIIIIIIBBBBBB}16"
+ "v28@0:8C16q20"
+ "wcmWiFiBTCoexProfileSDB"
+ "wifiChannelBW"
+ "wifiChannelType"
- "RCU2 Controller No Change in WiFi Band - Not Updataing"
- "RCU2 Controller No Change in WiFi Channel - Not Updating"
- "RCU2 Controller WiFi band changed from %d to %d"
- "RCU2 Controller WiFi channel changed from %ld to %ld"
- "mClientStarted"
- "updateWiFiBand:"
- "updateWiFiChannel:"
- "wifiService:"

```
