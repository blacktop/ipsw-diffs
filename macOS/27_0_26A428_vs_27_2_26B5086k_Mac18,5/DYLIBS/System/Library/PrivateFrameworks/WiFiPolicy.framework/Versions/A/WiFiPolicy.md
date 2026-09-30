## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/Versions/A/WiFiPolicy`

```diff

-1075.60.0.0.0
-  __TEXT.__text: 0xdde4c
-  __TEXT.__objc_methlist: 0x13658
-  __TEXT.__const: 0x7a0
-  __TEXT.__cstring: 0x2396b
+1077.3.0.0.0
+  __TEXT.__text: 0xdecac
+  __TEXT.__objc_methlist: 0x137c8
+  __TEXT.__const: 0x7c0
+  __TEXT.__cstring: 0x239fb
   __TEXT.__oslogstring: 0x4026
   __TEXT.__gcc_except_tab: 0x1754
   __TEXT.__dlopen_cstrs: 0x52

   __TEXT.__swift5_fieldmd: 0xa8
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_capture: 0x24
-  __TEXT.__unwind_info: 0x3040
+  __TEXT.__unwind_info: 0x3060
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaad0
+  __DATA_CONST.__objc_selrefs: 0xac30
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x4c0
-  __DATA_CONST.__objc_arraydata: 0x1508
-  __DATA_CONST.__got: 0xb38
+  __DATA_CONST.__objc_arraydata: 0x1528
+  __DATA_CONST.__got: 0xb40
   __AUTH_CONST.__const: 0x2118
-  __AUTH_CONST.__cfstring: 0x1fc20
-  __AUTH_CONST.__objc_const: 0x24fd8
+  __AUTH_CONST.__cfstring: 0x1fc80
+  __AUTH_CONST.__objc_const: 0x25248
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x1a58
   __AUTH_CONST.__objc_arrayobj: 0x438

   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0xc38
   __AUTH.__objc_data: 0x618
-  __DATA.__objc_ivar: 0x24dc
+  __DATA.__objc_ivar: 0x2510
   __DATA.__data: 0x1c38
   __DATA_DIRTY.__objc_data: 0x3488
   __DATA_DIRTY.__data: 0x150

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7036
-  Symbols:   15214
-  CStrings:  5058
+  Functions: 7072
+  Symbols:   15326
+  CStrings:  5062
 
Symbols:
+ +[WiFiUsagePrivacyFilter isInternalOrSeedInstall]
+ -[WiFiUsageMonitor updateCellularWRMScore:forInterface:]
+ -[WiFiUsageNetworkDetails previousJoinDate]
+ -[WiFiUsageNetworkDetails setPreviousJoinDate:]
+ -[WiFiUsageNetworkSession cellularWRMScoreDidChange:]
+ -[WiFiUsageSession bssidAtSessionStart]
+ -[WiFiUsageSession cellDataIndicatorAtSessionStart]
+ -[WiFiUsageSession cellularWRMScoreDidChange:]
+ -[WiFiUsageSession hasCellDataIndicatorAtSessionStart]
+ -[WiFiUsageSession hasCellularStateAtSessionStart]
+ -[WiFiUsageSession iRatScoreAtSessionStart]
+ -[WiFiUsageSession iRatScoreBadCount]
+ -[WiFiUsageSession iRatScoreFairCount]
+ -[WiFiUsageSession iRatScoreGoodCount]
+ -[WiFiUsageSession iRatScoreUnknownCount]
+ -[WiFiUsageSession iRatScoreUnusableCount]
+ -[WiFiUsageSession latestCellularWRMScore]
+ -[WiFiUsageSession latestLqaScore]
+ -[WiFiUsageSession resetJoinSideCaptures]
+ -[WiFiUsageSession setBssidAtSessionStart:]
+ -[WiFiUsageSession setCellDataIndicatorAtSessionStart:]
+ -[WiFiUsageSession setHasCellDataIndicatorAtSessionStart:]
+ -[WiFiUsageSession setHasCellularStateAtSessionStart:]
+ -[WiFiUsageSession setIRatScoreAtSessionStart:]
+ -[WiFiUsageSession setIRatScoreBadCount:]
+ -[WiFiUsageSession setIRatScoreFairCount:]
+ -[WiFiUsageSession setIRatScoreGoodCount:]
+ -[WiFiUsageSession setIRatScoreUnknownCount:]
+ -[WiFiUsageSession setIRatScoreUnusableCount:]
+ -[WiFiUsageSession setLatestCellularWRMScore:]
+ -[WiFiUsageSession setLatestLqaScore:]
+ GCC_except_table302
+ GCC_except_table68
+ GCC_except_table69
+ OBJC_IVAR_$_WiFiUsageNetworkDetails._previousJoinDate
+ OBJC_IVAR_$_WiFiUsageSession._bssidAtSessionStart
+ OBJC_IVAR_$_WiFiUsageSession._cellDataIndicatorAtSessionStart
+ OBJC_IVAR_$_WiFiUsageSession._hasCellDataIndicatorAtSessionStart
+ OBJC_IVAR_$_WiFiUsageSession._hasCellularStateAtSessionStart
+ OBJC_IVAR_$_WiFiUsageSession._iRatScoreAtSessionStart
+ OBJC_IVAR_$_WiFiUsageSession._iRatScoreBadCount
+ OBJC_IVAR_$_WiFiUsageSession._iRatScoreFairCount
+ OBJC_IVAR_$_WiFiUsageSession._iRatScoreGoodCount
+ OBJC_IVAR_$_WiFiUsageSession._iRatScoreUnknownCount
+ OBJC_IVAR_$_WiFiUsageSession._iRatScoreUnusableCount
+ OBJC_IVAR_$_WiFiUsageSession._latestCellularWRMScore
+ OBJC_IVAR_$_WiFiUsageSession._latestLqaScore
+ _WiFiUsageConnectionQualityRecordApnsPartialConnectivityBucket
+ _WiFiUsageConnectionQualityRecordConvertCellDataIndicatorToGEORAT
+ _WiFiUsageConnectionQualityRecordConvertLqaScoreToGEO
+ _WiFiUsageConnectionQualityRecordRssiMedianFromLQM
+ ___56-[WiFiUsageMonitor updateCellularWRMScore:forInterface:]_block_invoke
+ __isSeedInstall
+ _kPerformanceNetAttachPartialConnectivityDetections
+ _objc_msgSend$autoJoinDisabled
+ _objc_msgSend$bssidAtSessionStart
+ _objc_msgSend$cellDataIndicatorAtSessionStart
+ _objc_msgSend$cellularWRMScoreDidChange:
+ _objc_msgSend$count_of_LQMsamples
+ _objc_msgSend$hasCellularStateAtSessionStart
+ _objc_msgSend$iRatScoreAtSessionStart
+ _objc_msgSend$iRatScoreBadCount
+ _objc_msgSend$iRatScoreFairCount
+ _objc_msgSend$iRatScoreGoodCount
+ _objc_msgSend$iRatScoreUnknownCount
+ _objc_msgSend$iRatScoreUnusableCount
+ _objc_msgSend$isAirplane
+ _objc_msgSend$isInternalOrSeedInstall
+ _objc_msgSend$lastJoinDate
+ _objc_msgSend$latestCellularWRMScore
+ _objc_msgSend$latestLqaScore
+ _objc_msgSend$maxRssi
+ _objc_msgSend$minRssi
+ _objc_msgSend$networkDetailsAtEnd
+ _objc_msgSend$previousJoinDate
+ _objc_msgSend$resetJoinSideCaptures
+ _objc_msgSend$rssi40to50
+ _objc_msgSend$rssi50to60
+ _objc_msgSend$rssi60to65
+ _objc_msgSend$rssi65to70
+ _objc_msgSend$rssi70to75
+ _objc_msgSend$rssi75to80
+ _objc_msgSend$rssi80to85
+ _objc_msgSend$rssi85to90
+ _objc_msgSend$rssiAtSessionStart
+ _objc_msgSend$rssiGt40
+ _objc_msgSend$rssiLt90
+ _objc_msgSend$setApnsPartialConnectivityCount:
+ _objc_msgSend$setBssidAtSessionStart:
+ _objc_msgSend$setCellDataIndicatorAtSessionStart:
+ _objc_msgSend$setCellularAvailable:
+ _objc_msgSend$setDisassocAP:
+ _objc_msgSend$setFirstTimeJoin:
+ _objc_msgSend$setHasCellDataIndicatorAtSessionStart:
+ _objc_msgSend$setHasCellularStateAtSessionStart:
+ _objc_msgSend$setIRatScoreAtDisconnect:
+ _objc_msgSend$setIRatScoreAtJoin:
+ _objc_msgSend$setIRatScoreAtSessionStart:
+ _objc_msgSend$setIRatScoreBadCount:
+ _objc_msgSend$setIRatScoreFairCount:
+ _objc_msgSend$setIRatScoreGoodCount:
+ _objc_msgSend$setIRatScoreUnknownCount:
+ _objc_msgSend$setIRatScoreUnusableCount:
+ _objc_msgSend$setJoinedAP:
+ _objc_msgSend$setLatestCellularWRMScore:
+ _objc_msgSend$setLatestLqaScore:
+ _objc_msgSend$setLinkQualityAssessment:
+ _objc_msgSend$setPreviousJoinDate:
+ _objc_msgSend$setRadioAccessTypeAtDisconnect:
+ _objc_msgSend$setRadioAccessTypeAtJoin:
+ _objc_msgSend$setRssiMax:
+ _objc_msgSend$setRssiMedian:
+ _objc_msgSend$setRssiMin:
+ _objc_msgSend$setTransitNetworkType:
- GCC_except_table300
- GCC_except_table66
CStrings:
+ "-[WiFiUsageMonitor updateCellularWRMScore:forInterface:]_block_invoke"
+ "HotSpot_LPEMLSR_LpscTotalIcfCount"
+ "HotSpot_LPEMLSR_MainTotalIcfCount"
+ "delta_HOTSPOT_EMLSR_LPSC_TOTAL_ICF_COUNT"
+ "delta_HOTSPOT_EMLSR_MAIN_TOTAL_ICF_COUNT"
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
```
