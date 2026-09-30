## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2235.63.1.2.0
-  __TEXT.__text: 0xb7798
-  __TEXT.__objc_methlist: 0x9338
+2260.9.1.0.0
+  __TEXT.__text: 0xb8360
+  __TEXT.__objc_methlist: 0x93e0
   __TEXT.__const: 0x27f0
-  __TEXT.__cstring: 0xf46e
-  __TEXT.__oslogstring: 0xf32a
+  __TEXT.__cstring: 0xf612
+  __TEXT.__oslogstring: 0xf4ee
   __TEXT.__gcc_except_tab: 0x38c
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0x23e0
+  __TEXT.__unwind_info: 0x2418
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4700
+  __DATA_CONST.__objc_selrefs: 0x4740
   __DATA_CONST.__objc_superrefs: 0x1a8
   __DATA_CONST.__objc_arraydata: 0x220
   __DATA_CONST.__got: 0x298
   __AUTH_CONST.__const: 0x2a0
-  __AUTH_CONST.__cfstring: 0xee00
-  __AUTH_CONST.__objc_const: 0x17918
+  __AUTH_CONST.__cfstring: 0xefa0
+  __AUTH_CONST.__objc_const: 0x179b0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x498
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x6d8
   __AUTH.__data: 0x30
-  __DATA.__objc_ivar: 0x21fc
+  __DATA.__objc_ivar: 0x220c
   __DATA.__data: 0x750
   __DATA.__common: 0x1
   __DATA_DIRTY.__objc_data: 0x1270

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 4249
-  Symbols:   8766
-  CStrings:  3352
+  Functions: 4262
+  Symbols:   8791
+  CStrings:  3373
 
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
+ GCC_except_table1350
+ GCC_except_table144
+ GCC_except_table146
+ GCC_except_table462
+ _OBJC_IVAR_$_CallSegment._localLinkTransport
+ _OBJC_IVAR_$_MultiwayCall._hasJBInitialRampStats
+ _OBJC_IVAR_$_MultiwayCall._jbInitialRampStats
+ _OBJC_IVAR_$_VCAggregatorFaceTime._localLinkTransport
+ ___44-[VCAggregatorMultiway updateJBRampMetrics:]_block_invoke
+ _objc_msgSend$addJBInitialRampTelemetryForCall:callReport:
+ _objc_msgSend$addJBInitialRampTelemetryToSessionReport:
+ _objc_msgSend$jbInitialRampStats
+ _objc_msgSend$jbInitialRampStatsForSession
+ _objc_msgSend$reportingCurrentTime
+ _objc_msgSend$setJBInitialRampStats:
+ _objc_msgSend$updateJBRampMetrics:
+ _objc_msgSend$writeJBInitialRampStats:toReport:
- GCC_except_table1344
- GCC_except_table143
- GCC_except_table145
- GCC_except_table460
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
