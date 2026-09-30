## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-1070.62.0.0.0
-  __TEXT.__text: 0xdfd38
-  __TEXT.__objc_methlist: 0x13d18
-  __TEXT.__const: 0x868
-  __TEXT.__cstring: 0x25d4b
+1072.4.0.0.0
+  __TEXT.__text: 0xe0bbc
+  __TEXT.__objc_methlist: 0x13e88
+  __TEXT.__const: 0x888
+  __TEXT.__cstring: 0x25deb
   __TEXT.__oslogstring: 0x550e
   __TEXT.__gcc_except_tab: 0x190c
   __TEXT.__dlopen_cstrs: 0xa8

   __TEXT.__swift5_fieldmd: 0xb4
   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_capture: 0x34
-  __TEXT.__unwind_info: 0x3320
+  __TEXT.__unwind_info: 0x3348
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf20
+  __DATA_CONST.__objc_selrefs: 0xb080
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x4e0
-  __DATA_CONST.__objc_arraydata: 0x1510
-  __DATA_CONST.__got: 0xbb8
+  __DATA_CONST.__objc_arraydata: 0x1530
+  __DATA_CONST.__got: 0xbc0
   __AUTH_CONST.__const: 0x600
-  __AUTH_CONST.__cfstring: 0x20de0
-  __AUTH_CONST.__objc_const: 0x25980
+  __AUTH_CONST.__cfstring: 0x20e40
+  __AUTH_CONST.__objc_const: 0x25bf0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x1aa0
   __AUTH_CONST.__objc_arrayobj: 0x450

   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__auth_got: 0xee0
   __AUTH.__objc_data: 0x6b8
-  __DATA.__objc_ivar: 0x2568
+  __DATA.__objc_ivar: 0x259c
   __DATA.__data: 0x1ca0
   __DATA_DIRTY.__objc_data: 0x3558
   __DATA_DIRTY.__data: 0x160

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7206
-  Symbols:   15647
-  CStrings:  5323
+  Functions: 7242
+  Symbols:   15758
+  CStrings:  5327
 
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
+ GCC_except_table285
+ GCC_except_table64
+ GCC_except_table65
+ _OBJC_IVAR_$_WiFiUsageNetworkDetails._previousJoinDate
+ _OBJC_IVAR_$_WiFiUsageSession._bssidAtSessionStart
+ _OBJC_IVAR_$_WiFiUsageSession._cellDataIndicatorAtSessionStart
+ _OBJC_IVAR_$_WiFiUsageSession._hasCellDataIndicatorAtSessionStart
+ _OBJC_IVAR_$_WiFiUsageSession._hasCellularStateAtSessionStart
+ _OBJC_IVAR_$_WiFiUsageSession._iRatScoreAtSessionStart
+ _OBJC_IVAR_$_WiFiUsageSession._iRatScoreBadCount
+ _OBJC_IVAR_$_WiFiUsageSession._iRatScoreFairCount
+ _OBJC_IVAR_$_WiFiUsageSession._iRatScoreGoodCount
+ _OBJC_IVAR_$_WiFiUsageSession._iRatScoreUnknownCount
+ _OBJC_IVAR_$_WiFiUsageSession._iRatScoreUnusableCount
+ _OBJC_IVAR_$_WiFiUsageSession._latestCellularWRMScore
+ _OBJC_IVAR_$_WiFiUsageSession._latestLqaScore
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
- GCC_except_table283
- GCC_except_table62
CStrings:
+ "-[WiFiUsageMonitor updateCellularWRMScore:forInterface:]_block_invoke"
+ "HotSpot_LPEMLSR_LpscTotalIcfCount"
+ "HotSpot_LPEMLSR_MainTotalIcfCount"
+ "delta_HOTSPOT_EMLSR_LPSC_TOTAL_ICF_COUNT"
+ "delta_HOTSPOT_EMLSR_MAIN_TOTAL_ICF_COUNT"
- "%s Rejected due to [WiFiUsagePrivacyFilter isInternalInstall]\n"
```
