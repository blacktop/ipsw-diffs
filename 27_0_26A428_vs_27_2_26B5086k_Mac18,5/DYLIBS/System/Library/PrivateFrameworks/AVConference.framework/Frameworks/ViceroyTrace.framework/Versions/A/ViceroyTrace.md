## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/Versions/A/ViceroyTrace`

```diff

-2235.63.5.2.0
-  __TEXT.__text: 0xb69a0
-  __TEXT.__objc_methlist: 0x9308
+2260.9.1.0.0
+  __TEXT.__text: 0xb7570
+  __TEXT.__objc_methlist: 0x93a0
   __TEXT.__const: 0x2720
-  __TEXT.__cstring: 0xf27b
-  __TEXT.__oslogstring: 0xf7e8
+  __TEXT.__cstring: 0xf41f
+  __TEXT.__oslogstring: 0xf9ac
   __TEXT.__gcc_except_tab: 0x370
   __TEXT.__dlopen_cstrs: 0x4e
-  __TEXT.__unwind_info: 0x23d8
+  __TEXT.__unwind_info: 0x2408
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x46e0
+  __DATA_CONST.__objc_selrefs: 0x4720
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x220
   __DATA_CONST.__got: 0x280
   __AUTH_CONST.__const: 0xbd0
-  __AUTH_CONST.__cfstring: 0xec40
-  __AUTH_CONST.__objc_const: 0x178a8
+  __AUTH_CONST.__cfstring: 0xede0
+  __AUTH_CONST.__objc_const: 0x17940
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x658
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x21f0
+  __DATA.__objc_ivar: 0x2200
   __DATA.__data: 0x748
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1270

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4236
-  Symbols:   8822
-  CStrings:  3324
+  Functions: 4249
+  Symbols:   8847
+  CStrings:  3345
 
Symbols:
+ -[CallSegment localLinkTransport]
+ -[CallSegment setLocalLinkTransport:]
+ -[MultiwayCall jbInitialRampStats]
+ -[MultiwayCall setJBInitialRampStats:]
+ -[MultiwaySegment reportingCurrentTime]
+ -[VCAggregator reportingCurrentTime]
+ -[VCAggregatorMultiway addJBInitialRampTelemetryForCall:callReport:]
+ -[VCAggregatorMultiway addJBInitialRampTelemetryToSessionReport:]
+ -[VCAggregatorMultiway jbInitialRampStatsForSession]
+ -[VCAggregatorMultiway updateJBRampMetrics:]
+ -[VCAggregatorMultiway writeJBInitialRampStats:toReport:]
+ -[VCReportingCommon reportingCurrentTime]
+ GCC_except_table1356
+ GCC_except_table149
+ GCC_except_table464
+ OBJC_IVAR_$_CallSegment._localLinkTransport
+ OBJC_IVAR_$_MultiwayCall._hasJBInitialRampStats
+ OBJC_IVAR_$_MultiwayCall._jbInitialRampStats
+ OBJC_IVAR_$_VCAggregatorFaceTime._localLinkTransport
+ ___44-[VCAggregatorMultiway updateJBRampMetrics:]_block_invoke
+ _objc_msgSend$addJBInitialRampTelemetryForCall:callReport:
+ _objc_msgSend$addJBInitialRampTelemetryToSessionReport:
+ _objc_msgSend$jbInitialRampStats
+ _objc_msgSend$jbInitialRampStatsForSession
+ _objc_msgSend$reportingCurrentTime
+ _objc_msgSend$setJBInitialRampStats:
+ _objc_msgSend$updateJBRampMetrics:
+ _objc_msgSend$writeJBInitialRampStats:toReport:
- GCC_except_table1350
- GCC_except_table148
- GCC_except_table462
CStrings:
+ " [%s] %s:%d %@(%p) JB ramp metrics payload missing participant UUID. Ignoring ..."
+ " [%s] %s:%d JB ramp metrics for unknown participant=%@. Ignoring ..."
+ " [%s] %s:%d JB ramp metrics payload missing participant UUID. Ignoring ..."
+ " [%s] %s:%d VCAggregatorMultiway: skipping uplink segment flush. currentUplinkSegmentKey=%@, currentUplinkSegmentStreamGroups=%u"
+ "-[RTCReportingAgent reportSegment:withMessageType:clientType:]"
+ "-[VCAggregatorMultiway updateJBRampMetrics:]"
+ "-[VCAggregatorMultiway updateJBRampMetrics:]_block_invoke"
+ "JBIRAVGOOO"
+ "JBIRHSA"
+ "JBIRMAXOOO"
+ "JBIRNAP"
+ "JBIRNOOO"
+ "JBIRNP"
+ "JBInitialRampAvgOOOTimeDisplacementMs"
+ "JBInitialRampHasSufficientAudioPackets"
+ "JBInitialRampMaxOOOTimeDisplacementMs"
+ "JBInitialRampNumAudioPackets"
+ "JBInitialRampNumOOOPackets"
+ "JBInitialRampNumPackets"
+ "ReportingVC [%s] %s:%d reportSegment: dropping report with no metrics. method=%u, messageType=%u"
+ "cse_"
```
