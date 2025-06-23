## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1026.66.0.0.0
-  __TEXT.__text: 0xbda34
-  __TEXT.__auth_stubs: 0x1600
-  __TEXT.__objc_methlist: 0x115e0
+1026.74.0.0.0
+  __TEXT.__text: 0xbef9c
+  __TEXT.__auth_stubs: 0x1620
+  __TEXT.__objc_methlist: 0x116b8
   __TEXT.__const: 0x648
-  __TEXT.__cstring: 0x1ca32
-  __TEXT.__oslogstring: 0x3d54
-  __TEXT.__gcc_except_tab: 0x197c
+  __TEXT.__cstring: 0x1cda2
+  __TEXT.__oslogstring: 0x3d90
+  __TEXT.__gcc_except_tab: 0x1980
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x2160
-  __TEXT.__objc_classname: 0x1400
-  __TEXT.__objc_methname: 0x32874
-  __TEXT.__objc_methtype: 0x3b53
-  __TEXT.__objc_stubs: 0x18900
+  __TEXT.__unwind_info: 0x2190
+  __TEXT.__objc_classname: 0x1407
+  __TEXT.__objc_methname: 0x32b1d
+  __TEXT.__objc_methtype: 0x3bb9
+  __TEXT.__objc_stubs: 0x18aa0
   __DATA_CONST.__got: 0xa58
-  __DATA_CONST.__const: 0x22d8
+  __DATA_CONST.__const: 0x2350
   __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x99f8
+  __DATA_CONST.__objc_selrefs: 0x9a88
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x438
-  __DATA_CONST.__objc_arraydata: 0xa88
-  __AUTH_CONST.__auth_got: 0xb18
+  __DATA_CONST.__objc_arraydata: 0xaa0
+  __AUTH_CONST.__auth_got: 0xb28
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x18f40
-  __AUTH_CONST.__objc_const: 0x21610
-  __AUTH_CONST.__objc_intobj: 0x17b8
-  __AUTH_CONST.__objc_arrayobj: 0x390
+  __AUTH_CONST.__cfstring: 0x19200
+  __AUTH_CONST.__objc_const: 0x21760
+  __AUTH_CONST.__objc_intobj: 0x1848
+  __AUTH_CONST.__objc_arrayobj: 0x3a8
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x8c0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x2130
+  __DATA.__objc_ivar: 0x2150
   __DATA.__data: 0x1bc0
   __DATA.__bss: 0x52
   __DATA_DIRTY.__objc_data: 0x2b20

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5ED46304-472C-39DE-ACFA-9CFBC2920A83
-  Functions: 6140
-  Symbols:   20047
-  CStrings:  16596
+  UUID: 295476F1-2928-3B2A-8009-60B5D4A49E51
+  Functions: 6162
+  Symbols:   20117
+  CStrings:  16680
 
Symbols:
+ -[WiFiUsageLQMUserSample isAVcallOnWiFi]
+ -[WiFiUsageLQMUserSample isNwAppInFG]
+ -[WiFiUsageLQMUserSample setIsAVcallOnWiFi:]
+ -[WiFiUsageLQMUserSample setIsNwAppInFG:]
+ -[WiFiUsageLQMWindowAnalysis _generateState]
+ -[WiFiUsageLinkSession faultEventDetected:event:]
+ -[WiFiUsageMonitor addFaultEvent:forInterface:at:event:]
+ -[WiFiUsageMonitor addFaultEvent:forInterface:event:]
+ -[WiFiUsagePoorLinkSession cellularFallbackEnabledAtLinkDown]
+ -[WiFiUsagePoorLinkSession cellularFallbackStateDidChange:]
+ -[WiFiUsagePoorLinkSession faultEventDetected:event:]
+ -[WiFiUsagePoorLinkSession resetRxFrameImpact]
+ -[WiFiUsagePoorLinkSession rxFrameImpactTime]
+ -[WiFiUsagePoorLinkSession setCellularFallbackEnabledAtLinkDown:]
+ -[WiFiUsagePoorLinkSession setRxFrameImpactTime:]
+ -[WiFiUsagePoorLinkSession updateRxFrameImpactWith:]
+ -[WiFiUsageSession _generateState]
+ -[WiFiUsageSession dealloc]
+ -[WiFiUsageSession faultEventDetected:event:]
+ -[WiFiUsageSession osStateHandle]
+ -[WiFiUsageSession setOsStateHandle:]
+ GCC_except_table227
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table57
+ GCC_except_table58
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._isAVcallOnWiFi
+ _OBJC_IVAR_$_WiFiUsageLQMUserSample._isNwAppInFG
+ _OBJC_IVAR_$_WiFiUsageLQMWindowAnalysis._osStateHandle
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._cellularFallbackEnabled
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._cellularFallbackEnabledAtLinkDown
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._rxFrameImpactTime
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._rxFrameThresholds
+ _OBJC_IVAR_$_WiFiUsagePoorLinkSession._ssidAtLinkDown
+ _OBJC_IVAR_$_WiFiUsageSession._osStateHandle
+ ___24-[WiFiUsageMonitor init]_block_invoke.266
+ ___24-[WiFiUsageMonitor init]_block_invoke.270
+ ___29-[WiFiSoftError submitMetric]_block_invoke.80
+ ___30-[WFMeasure dispatchPingTest:]_block_invoke.417
+ ___34-[WiFiUsageSession _generateState]_block_invoke
+ ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.697
+ ___38-[WiFiSoftError submitMetricWithData:]_block_invoke.83
+ ___40-[WiFiSoftError initWithName:andParams:]_block_invoke.34
+ ___40-[WiFiSoftError initWithName:andParams:]_block_invoke.49
+ ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.125
+ ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.125.cold.1
+ ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.93
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.147
+ ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.147.cold.1
+ ___56-[WiFiUsageMonitor addFaultEvent:forInterface:at:event:]_block_invoke
+ ___61-[WiFiUsageSession setCompletionHandler:withContext:onQueue:]_block_invoke
+ ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.366
+ ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.289
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.754
+ ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.765
+ ___94-[WiFiUsageLQMWindowAnalysis initWithRollingWindow:andReason:andContext:andTimestamp:onQueue:]_block_invoke_2
+ ___block_descriptor_40_e8_32w_e103_^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16?0^{os_state_hints_s=I*II}8lw32l8
+ ___block_descriptor_48_e8_32s40s_e15_v32?0816^B24ls32l8s40l8
+ ___block_descriptor_72_e8_32s40s48s56s_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_literal_global.102
+ ___block_literal_global.207
+ ___block_literal_global.253
+ ___block_literal_global.272
+ ___block_literal_global.52
+ ___block_literal_global.757
+ ___block_literal_global.768
+ ___block_literal_global.770
+ ___block_literal_global.772
+ _objc_msgSend$_generateState
+ _objc_msgSend$addFaultEvent:forInterface:at:event:
+ _objc_msgSend$cellularFallbackEnabledAtLinkDown
+ _objc_msgSend$faultEventDetected:event:
+ _objc_msgSend$isAVcallOnWiFi
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isNwAppInFG
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$resetRxFrameImpact
+ _objc_msgSend$setCellularFallbackEnabledAtLinkDown:
+ _objc_msgSend$setIsAVcallOnWiFi:
+ _objc_msgSend$setIsNwAppInFG:
+ _objc_msgSend$updateRxFrameImpactWith:
+ _os_state_add_handler
+ _os_state_remove_handler
- -[WiFiUsageLinkSession faultEventDetected:]
- -[WiFiUsagePoorLinkSession faultEventDetected:]
- -[WiFiUsageSession faultEventDetected:]
- GCC_except_table225
- GCC_except_table26
- GCC_except_table41
- GCC_except_table44
- GCC_except_table53
- GCC_except_table54
- _OBJC_IVAR_$_WiFiUsagePoorLinkSession._ssidAtTD
- ___24-[WiFiUsageMonitor init]_block_invoke.256
- ___24-[WiFiUsageMonitor init]_block_invoke.260
- ___29-[WiFiSoftError submitMetric]_block_invoke.79
- ___30-[WFMeasure dispatchPingTest:]_block_invoke.411
- ___36-[WiFiUsageMonitor submitAnalytics:]_block_invoke.687
- ___38-[WiFiSoftError submitMetricWithData:]_block_invoke.82
- ___40-[WiFiSoftError initWithName:andParams:]_block_invoke.48
- ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.124
- ___47-[WiFiSoftError updateHUDWithHost:messageDict:]_block_invoke.124.cold.1
- ___49-[WiFiSoftError submitABCReportWithReason:event:]_block_invoke.92
- ___50-[WiFiUsageMonitor addFaultEvent:forInterface:at:]_block_invoke
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.146
- ___53-[WiFiSoftError tapToRadarWithURL:completionHandler:]_block_invoke.146.cold.1
- ___62-[WiFiUsageLinkSession performLinkTestFor:isTriggeredByFault:]_block_invoke.354
- ___69-[WiFiUsageMonitor startMonitoringWiFiInterface:withLinkSessionOnly:]_block_invoke.279
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.744
- ___85-[WiFiUsageMonitor updateKnownNetworksSupportingSeamless:forBSS:andSSID:beaconCache:]_block_invoke.755
- ___block_literal_global.101
- ___block_literal_global.197
- ___block_literal_global.243
- ___block_literal_global.262
- ___block_literal_global.51
- ___block_literal_global.747
- ___block_literal_global.758
- ___block_literal_global.760
- ___block_literal_global.762
CStrings:
+ "%s %@"
+ "%s RTAppAtSessionEnd %d (atFirstTDConfirmed: %d) , FGAppAtSessionEnd %d (atFirstTDConfirmed: %d), CellularFallbackEnabledAtLinkDown %d"
+ "%s RxFrameImpactTime [Threshold, Duration] "
+ "%s kWiFiUsageFaultReasonRxDataStallEvent Rejected _linkUp %d _didBecomePrimary %d\n"
+ "%s kWiFiUsageFaultReasonRxDataStallEvent Rejected since _lastFaultIndicationTime %f ago\n"
+ "%s: %@ BEGIN"
+ "%s: BEGIN"
+ "%s: END (%s), bytes: %zu (limit: %d)"
+ "-[WiFiUsageLQMWindowAnalysis _generateState]"
+ "-[WiFiUsageLinkSession faultEventDetected:event:]"
+ "-[WiFiUsageMonitor addFaultEvent:forInterface:at:event:]_block_invoke"
+ "-[WiFiUsagePoorLinkSession faultEventDetected:event:]"
+ "-[WiFiUsageSession _generateState]"
+ "Avg"
+ "Context: %@"
+ "Count"
+ "Duration"
+ "FaultReasonRxDataStallEvent"
+ "Features: %@"
+ "LQM window analysis for %@ (%@: %@ - %@ ; %@: %@ - %@)\n"
+ "Max"
+ "Min"
+ "Network at end of analysis: %@"
+ "Network at trigger: %@"
+ "PH Client Info Fetch Failure"
+ "Rx Data Stall"
+ "T@\"NSMutableArray\",&,N,V_rxFrameImpactTime"
+ "TB,N,V_cellularFallbackEnabledAtLinkDown"
+ "TB,N,V_isAVcallOnWiFi"
+ "TB,N,V_isNwAppInFG"
+ "TQ,N,V_osStateHandle"
+ "[%lu, %lu] "
+ "[38Q]"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@0:8"
+ "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}16@?0^{os_state_hints_s=I*II}8"
+ "_cellularFallbackEnabledAtLinkDown"
+ "_generateState"
+ "_isAVcallOnWiFi"
+ "_isNwAppInFG"
+ "_osStateHandle"
+ "_rxFrameImpactTime"
+ "_rxFrameThresholds"
+ "_ssidAtLinkDown"
+ "addFaultEvent:forInterface:at:event:"
+ "addFaultEvent:forInterface:event:"
+ "cellularFallbackEnabledAtLinkDown"
+ "failed"
+ "faultEventDetected:event:"
+ "isAVcallOnWiFi"
+ "isEqualToNumber:"
+ "isNwAppInFG"
+ "kWiFiUsageFaultReasonPHClientInfoFetchFailure"
+ "kWiFiUsageFaultReasonRxDataStallEvent"
+ "osStateHandle"
+ "replaceObjectAtIndex:withObject:"
+ "resetRxFrameImpact"
+ "rxFrameImpactTime"
+ "setCellularFallbackEnabledAtLinkDown:"
+ "setIsAVcallOnWiFi:"
+ "setIsNwAppInFG:"
+ "setOsStateHandle:"
+ "setRxFrameImpactTime:"
+ "success"
+ "updateRxFrameImpactWith:"
+ "v29@0:8@16{?=CCCCC}24"
+ "v32@?0@8@16^B24"
+ "v48@0:8Q16@24@32@40"
- "%s RTAppAtSessionEnd %d (atFirstTDConfirmed: %d) , FGAppAtSessionEnd %d (atFirstTDConfirmed: %d)"
- "-[WiFiUsageLinkSession faultEventDetected:]"
- "-[WiFiUsageMonitor addFaultEvent:forInterface:at:]_block_invoke"
- "-[WiFiUsagePoorLinkSession faultEventDetected:]"
- "[36Q]"
- "_ssidAtTD"
- "v27@0:8@16{?=CCC}24"

```
