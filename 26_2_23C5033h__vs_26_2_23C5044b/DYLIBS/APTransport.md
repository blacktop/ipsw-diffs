## APTransport

> `/System/Library/PrivateFrameworks/APTransport.framework/APTransport`

```diff

-925.4.1.0.0
-  __TEXT.__text: 0xa90bc
-  __TEXT.__auth_stubs: 0x3350
+925.5.1.1.0
+  __TEXT.__text: 0xa78ac
+  __TEXT.__auth_stubs: 0x3220
   __TEXT.__objc_methlist: 0x1394
-  __TEXT.__cstring: 0x2bfbf
+  __TEXT.__cstring: 0x2b9b7
   __TEXT.__const: 0x330
-  __TEXT.__gcc_except_tab: 0x714
+  __TEXT.__gcc_except_tab: 0x6d4
   __TEXT.__oslogstring: 0x16e
   __TEXT.__dlopen_cstrs: 0x18b
-  __TEXT.__unwind_info: 0x2808
+  __TEXT.__unwind_info: 0x27b0
   __TEXT.__objc_classname: 0x1f5
   __TEXT.__objc_methname: 0x49d4
   __TEXT.__objc_methtype: 0xf80
   __TEXT.__objc_stubs: 0x4220
   __DATA_CONST.__got: 0x3e8
-  __DATA_CONST.__const: 0x3700
+  __DATA_CONST.__const: 0x3608
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x1460
   __DATA_CONST.__objc_superrefs: 0x50
   __DATA_CONST.__objc_arraydata: 0x28
-  __AUTH_CONST.__auth_got: 0x19b8
+  __AUTH_CONST.__auth_got: 0x1920
   __AUTH_CONST.__const: 0x2b48
-  __AUTH_CONST.__cfstring: 0x5f40
+  __AUTH_CONST.__cfstring: 0x5ca0
   __AUTH_CONST.__objc_const: 0x1cc8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30

   - /usr/lib/libIOReport.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A6E4F172-85EF-353E-A321-C0D57DA5ED90
-  Functions: 4569
-  Symbols:   11888
-  CStrings:  5935
+  UUID: 61786EE4-1CD1-3B40-83A6-EFBEE4DC627E
+  Functions: 4537
+  Symbols:   11795
+  CStrings:  5856
 
Symbols:
+ _objc_retain_x22
- _APTransportWifiManagerClientCopyWifiStatistics
- _APTransportWifiManagerClientGetPeerRSSI
- _Apple80211ErrToStr
- _Apple80211GetIOReportingService
- _CFSetCreate
- _CFStringTrimWhitespace
- _DataBuffer_Append
- _DataBuffer_Commit
- _DataBuffer_Free
- _DataBuffer_Init
- _IOReportChannelGetChannelName
- _IOReportChannelGetGroup
- _IOReportChannelGetSubGroup
- _IOReportChannelGetUnitLabel
- _IOReportCopyChannelsForDriver
- _IOReportCreateSamples
- _IOReportCreateSubscription
- _IOReportGetChannelCount
- _IOReportIterate
- _IOReportPrune
- _IOReportSelectChannelsInGroup
- _IOReportSimpleGetIntegerValue
- ___APTransportWifiManagerClientCopyWifiStatistics_block_invoke
- ___APTransportWifiManagerClientCopyWifiStatistics_block_invoke.cold.1
- ___APTransportWifiManagerClientCopyWifiStatistics_block_invoke.cold.2
- ___APTransportWifiManagerClientCopyWifiStatistics_block_invoke.cold.3
- ___APTransportWifiManagerClientCopyWifiStatistics_block_invoke.cold.4
- ___APTransportWifiManagerClientGetPeerRSSI_block_invoke
- ___APTransportWifiManagerClientGetPeerRSSI_block_invoke.cold.1
- ___APTransportWifiManagerClientGetPeerRSSI_block_invoke.cold.2
- ___APTransportWifiManagerClientGetPeerRSSI_block_invoke.cold.3
- ___APTransportWifiManagerClientGetPeerRSSI_block_invoke.cold.4
- ___APTransportWifiManagerClientGetPeerRSSI_block_invoke.cold.5
- ___APTransportWifiManagerClientGetPeerRSSI_block_invoke.cold.6
- ___block_descriptor_40_e25_i16?0^{__CFDictionary=}8l
- ___block_descriptor_48_e25_i16?0^{__CFDictionary=}8l
- ___block_descriptor_56_e8_32r40r48r_e25_i16?0^{__CFDictionary=}8lr32l8r40l8r48l8
- ___block_descriptor_tmp.108
- ___wifiManagerClient_copyWifiStatistics_block_invoke
- ___wifiManagerClient_getPeerRSSI_block_invoke
- ___wifiManagerClient_printSamples_block_invoke
- ___wifiManagerClient_printSamples_block_invoke.cold.1
- ___wifiManagerClient_printSamples_block_invoke.cold.2
- ___wifiManagerClient_printSamples_block_invoke.cold.3
- ___wifiManagerClient_printSamples_block_invoke.cold.4
- ___wifiManagerClient_printSamples_block_invoke.cold.5
- ___wifiManagerClient_printSamples_block_invoke.cold.6
- ___wifiManagerClient_pruneIOReport_block_invoke
- ___wifiManagerClient_registerInternal_block_invoke
- ___wifiManagerClient_unregisterInternal_block_invoke
- _kAPTransportWifiManagerClientWifiStatistic_InfrastructureCCA
- _kAPTransportWifiManagerClientWifiStatistic_InfrastructureRSSI
- _kAPTransportWifiManagerClientWifiStatistic_InfrastructureSNR
- _kAPTransportWifiManagerClientWifiStatistic_PeerToPeerCCA
- _wifiManagerClient_dumpWifiStatistics
- _wifiManagerClient_dumpWifiStatistics.cold.1
- _wifiManagerClient_dumpWifiStatistics.cold.2
- _wifiManagerClient_dumpWifiStatistics.cold.3
- _wifiManagerClient_ensureSubscribedForStatistics
CStrings:
+ "925.5.1.1"
- "\n%@: "
- "%@ %.6a"
- "%@ = "
- "%@, "
- "%lld "
- "%lld%@"
- "%lld, "
- "%s\n"
- "%s = "
- "925.4.1"
- "AWDL peer %.6a RSSI = %lld"
- "All IOReport channels = %@"
- "Average CCA"
- "Channel lookup failed"
- "Couldn't find matching service"
- "Create samples failed, error=%@"
- "Create subscription failed"
- "Driver name pruning failed"
- "Effective Data Transfer Rate"
- "Error getting IOReportingService: %s\n"
- "Expected Peak Latency"
- "IOReportIterate failed"
- "IOService matching dictionary = %@"
- "InfraCCA"
- "InfraRSSI"
- "InfraSNR"
- "Interface Avgerage CCA"
- "Interface Open Percent"
- "Interface awdl0"
- "Interface awdl0 Peer"
- "Interface awdl0 Peer %&s"
- "Interface awdl0 Peer RSSIs: "
- "LQM RSSI"
- "LQM RSSI value"
- "LQM SNR"
- "LQM SNR value"
- "Link Latency"
- "Link Open"
- "Link Rate"
- "OSStatus httpconnection_printPeerRSSI(uint8_t *)"
- "OSStatus wifiManagerClient_copyWifiStatistics(APTransportWifiManagerClientRef, CFDictionaryRef *)"
- "OSStatus wifiManagerClient_dumpWifiStatistics(APTransportWifiManagerClientRef)"
- "OSStatus wifiManagerClient_ensureSubscribedForStatistics(APTransportWifiManagerClientRef)"
- "OSStatus wifiManagerClient_getPeerRSSI(APTransportWifiManagerClientRef, uint8_t *, int64_t *)"
- "OSStatus wifiManagerClient_printSamples(CFDictionaryRef)"
- "OSStatus wifiManagerClient_pruneIOReport(CFMutableDictionaryRef)"
- "P2PCCA"
- "Pruned IOReport Channels = %@"
- "RSSI value"
- "httpconnection_printPeerRSSI"
- "i16@?0^{__CFDictionary=}8"
- "wifiManagerClient_copyWifiStatistics"
- "wifiManagerClient_dumpWifiStatistics"
- "wifiManagerClient_ensureSubscribedForStatistics"
- "wifiManagerClient_formatPeerRSSISamples"
- "wifiManagerClient_getPeerRSSI"
- "wifiManagerClient_printSamples"
- "wifiManagerClient_pruneIOReport"

```
