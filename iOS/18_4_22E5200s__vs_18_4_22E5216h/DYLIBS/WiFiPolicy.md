## WiFiPolicy

> `/System/Library/PrivateFrameworks/WiFiPolicy.framework/WiFiPolicy`

```diff

-980.33.0.0.0
-  __TEXT.__text: 0xb8564
+980.34.0.0.0
+  __TEXT.__text: 0xb8b28
   __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0x10fa0
+  __TEXT.__objc_methlist: 0x110b8
   __TEXT.__const: 0x638
-  __TEXT.__cstring: 0x1bc9f
+  __TEXT.__cstring: 0x1bf6f
   __TEXT.__oslogstring: 0x3a15
-  __TEXT.__gcc_except_tab: 0x1904
+  __TEXT.__gcc_except_tab: 0x18f0
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x21a8
+  __TEXT.__unwind_info: 0x2188
   __TEXT.__objc_classname: 0x1379
-  __TEXT.__objc_methname: 0x31518
-  __TEXT.__objc_methtype: 0x3a1a
-  __TEXT.__objc_stubs: 0x17e80
+  __TEXT.__objc_methname: 0x31869
+  __TEXT.__objc_methtype: 0x3a26
+  __TEXT.__objc_stubs: 0x180a0
   __DATA_CONST.__got: 0xa40
-  __DATA_CONST.__const: 0x21d8
+  __DATA_CONST.__const: 0x21b0
   __DATA_CONST.__objc_classlist: 0x510
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9690
+  __DATA_CONST.__objc_selrefs: 0x9740
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x430
   __DATA_CONST.__objc_arraydata: 0xa58
   __AUTH_CONST.__auth_got: 0xb10
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x185c0
-  __AUTH_CONST.__objc_const: 0x20868
+  __AUTH_CONST.__cfstring: 0x18780
+  __AUTH_CONST.__objc_const: 0x20a28
   __AUTH_CONST.__objc_intobj: 0x1740
   __AUTH_CONST.__objc_arrayobj: 0x390
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x2060
+  __DATA.__objc_ivar: 0x2080
   __DATA.__data: 0x1bc0
   __DATA.__bss: 0x22
   __DATA_DIRTY.__objc_data: 0x2a80

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5987
-  Symbols:   6991
-  CStrings:  13149
+  Functions: 6009
+  Symbols:   7013
+  CStrings:  13204
 
CStrings:
+ "\x03\xb1\x11\x12#EQ"
+ "\x13\x12\xf0\xf0\xf0\xe1\x92"
+ "%s SessionTotalBytes %lu (SessionTxBytes %lu SessionRxBytes %lu)"
+ "%s UnifiedImpactTime %lu (TxPerImpactTime %lu TxRxRateImpactTime %lu TxLatencyImpactTime %lu)"
+ "%s: BadLink session detected due to TDAlert; cancel the goodRssi timer/continue the bad session"
+ "%s: BadLink session detected due to driver TD Recommendation; cancel the goodRssi timer/continue the bad session (%@)"
+ "%s: BadLink session detected due to highCCA for 2.4G; cancel the goodRssi timer/continue the bad session"
+ "%s: BadLink session started due to TdAlert"
+ "%s: BadLink session started due to highCCA for 2.4G"
+ "%s: rssi (%lddBm) crossing BadLink Threshold (%@dBm); cancel the goodRssi timer/continue the bad session"
+ "SessionRxBytes"
+ "SessionTotalBytes"
+ "SessionTxBytes"
+ "TB,N,V_isHighCCAFor2GHz"
+ "TQ,N,V_averageTxPer"
+ "TQ,N,V_sessionRxBytes"
+ "TQ,N,V_sessionStartRxBytes"
+ "TQ,N,V_sessionStartTxBytes"
+ "TQ,N,V_sessionTotalBytes"
+ "TQ,N,V_sessionTxBytes"
+ "TQ,N,V_txLatencyImpactTime"
+ "TQ,N,V_txPerImpactTime"
+ "TQ,N,V_txRxRateImpactTime"
+ "TQ,N,V_unifiedImpactTime"
+ "Tq,N,V_rssiInUse"
+ "TxLatencyImpactTime"
+ "TxPerImpactTime"
+ "TxRxRateImpactTime"
+ "UnifiedImpactTime"
+ "_averageTxPer"
+ "_isHighCCAFor2GHz"
+ "_rssiInUse"
+ "_sessionRxBytes"
+ "_sessionStartRxBytes"
+ "_sessionStartTxBytes"
+ "_sessionTotalBytes"
+ "_sessionTxBytes"
+ "_txLatencyImpactTime"
+ "_txLatencyThreshold"
+ "_txPerImpactTime"
+ "_txRxRateImpactTime"
+ "_unifiedImpactTime"
+ "averageTxPer"
+ "isHighCCAFor2GHz"
+ "populateWithRssi:rssiInUse:rssi0:rssi1:rssiMode:noise:noise0:noise1:snr:selfCca:otherCca:interference:totalReportedCca:beaconPer:rxCrsGlitch:rxBadPLCP:rxStart:rxBphyCrsGlitch:rxBphyBadPLCP:sampleDuration:isHighCCAFor2GHz:"
+ "populateWithTxFrames:RxFrames:TxFails:TxRetries:RxRetries:TxRate:RxRate:txRTS:txRTSFail:txMpdu:txAMPDU:averageTxPer:"
+ "rssiInUse"
+ "sessionRxBytes"
+ "sessionStartRxBytes"
+ "sessionStartTxBytes"
+ "sessionTotalBytes"
+ "sessionTxBytes"
+ "setAverageTxPer:"
+ "setIsHighCCAFor2GHz:"
+ "setRssiInUse:"
+ "setSessionRxBytes:"
+ "setSessionStartRxBytes:"
+ "setSessionStartTxBytes:"
+ "setSessionTotalBytes:"
+ "setSessionTxBytes:"
+ "setTxLatencyImpactTime:"
+ "setTxPerImpactTime:"
+ "setTxRxRateImpactTime:"
+ "setUnifiedImpactTime:"
+ "txLatencyImpactTime"
+ "txPerImpactTime"
+ "txRxRateImpactTime"
+ "unifiedImpactTime"
+ "updateWithScores:"
+ "v112@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80Q88Q96Q104"
+ "v180@0:8q16q24q32q40Q48q56q64q72q80Q88Q96Q104Q112Q120Q128Q136Q144Q152Q160Q168B176"
- "\x03\xd1\x13\x12#EQ"
- "\x13\x12\xf0\xf0\xf0\xc1\x92"
- "%s: BadLink session started due to highCCA for 2.4G "
- "_bcnPerThresholdForPerCoreUse"
- "_maxPerCoreRssiHist"
- "_rssiCore0Array"
- "_rssiCore1Array"
- "_rssiThresholdForPerCoreUse"
- "avgValidRssiInArray:"
- "checkGoodRssiThenBadSession"
- "isHighCcaFor2Ghz:"
- "populateWithRssi:rssi0:rssi1:rssiMode:noise:noise0:noise1:snr:selfCca:otherCca:interference:totalReportedCca:beaconPer:rxCrsGlitch:rxBadPLCP:rxStart:rxBphyCrsGlitch:rxBphyBadPLCP:sampleDuration:"
- "populateWithTxFrames:RxFrames:TxFails:TxRetries:RxRetries:TxRate:RxRate:txRTS:txRTSFail:txMpdu:txAMPDU:"
- "v104@0:8Q16Q24Q32Q40Q48Q56Q64Q72Q80Q88Q96"
- "v168@0:8q16q24q32Q40q48q56q64q72Q80Q88Q96Q104Q112Q120Q128Q136Q144Q152Q160"
- "v32@?0@\"NSNumber\"8Q16^B24"

```
