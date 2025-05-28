## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2010.3.1.0.0
-  __TEXT.__text: 0x78e40
+2015.3.1.0.0
+  __TEXT.__text: 0x79ec8
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x657c
-  __TEXT.__const: 0x1cd0
+  __TEXT.__objc_methlist: 0x6684
+  __TEXT.__const: 0x1d60
   __TEXT.__gcc_except_tab: 0x2d0
-  __TEXT.__cstring: 0x9335
+  __TEXT.__cstring: 0x9472
   __TEXT.__oslogstring: 0x8bde
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0xe78
+  __TEXT.__unwind_info: 0xe94
   __TEXT.__objc_classname: 0x385
-  __TEXT.__objc_methname: 0x14296
-  __TEXT.__objc_methtype: 0x1302
-  __TEXT.__objc_stubs: 0xaca0
+  __TEXT.__objc_methname: 0x1464a
+  __TEXT.__objc_methtype: 0x1324
+  __TEXT.__objc_stubs: 0xaec0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0xb88
+  __DATA_CONST.__const: 0xb90
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10978
-  __DATA_CONST.__objc_selrefs: 0x3068
+  __DATA_CONST.__objc_const: 0x10b28
+  __DATA_CONST.__objc_selrefs: 0x30f0
+  __DATA_CONST.__objc_classrefs: 0x1b0
+  __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__cfstring: 0xb180
+  __AUTH_CONST.__cfstring: 0xb2e0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__objc_intobj: 0x318

   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__auth_got: 0x578
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_classrefs: 0x1b0
-  __DATA.__objc_superrefs: 0x100
-  __DATA.__objc_ivar: 0x18c0
-  __DATA.__data: 0x5a8
+  __DATA.__objc_ivar: 0x18ec
+  __DATA.__data: 0x5b0
   __DATA.__bss: 0xe8
   __DATA.__common: 0x21
   __DATA_DIRTY.__const: 0x200

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2774
-  Symbols:   9206
-  CStrings:  5586
+  Functions: 2800
+  Symbols:   9286
+  CStrings:  5631
 
Symbols:
+ -[MultiwayCall processKeyFrameReceived:]
+ -[MultiwayCall processKeyFrameRequestSent:]
+ -[MultiwaySegment constrainedConnectionDuration]
+ -[MultiwaySegment expensiveConnectionDuration]
+ -[MultiwaySegment setConstrainedConnectionDuration:]
+ -[MultiwaySegment setExpensiveConnectionDuration:]
+ -[StreamGroupStats firResponseTime]
+ -[StreamGroupStats packetLossRateAccumulator]
+ -[StreamGroupStats processKeyFrameReceived]
+ -[StreamGroupStats processKeyFrameRequestSent]
+ -[StreamGroupStats setPacketLossRateAccumulator:]
+ -[UplinkSegment firResponseTime]
+ -[UplinkSegment processKeyFrameReceived:]
+ -[UplinkSegment processKeyFrameRequestSent:]
+ -[VCAggregatorMultiway checkSegmentCanBeUpdated:]
+ -[VCAggregatorMultiway processDataMode:]
+ -[VCAggregatorMultiway processKeyFrameReceived:]
+ -[VCAggregatorMultiway processKeyFrameRequestSent:]
+ -[VCAggregatorMultiway updateDataModeDuration]
+ -[VCAggregatorMultiway updateModeDurationOnSegment:countExpensive:OrCountConstrained:]
+ -[VCReportingDistribution initWithHistogramType:reportingKeys:histogramIncrementFactor:]
+ -[VCReportingDistribution initWithHistogramType:reportingKeys:histogramIncrementFactor:].cold.1
+ -[VCReportingDistribution initWithSignedHistogramType:reportingKeys:histogramIncrementFactor:]
+ -[VCReportingDistribution initWithSignedHistogramType:reportingKeys:histogramIncrementFactor:].cold.1
+ GCC_except_table958
+ GCC_except_table970
+ _FIRResponseTime
+ _OBJC_IVAR_$_MultiwaySegment._constrainedConnectionDuration
+ _OBJC_IVAR_$_MultiwaySegment._expensiveConnectionDuration
+ _OBJC_IVAR_$_StreamGroupStats._firResponseTime
+ _OBJC_IVAR_$_StreamGroupStats._oldestPendingFirTime
+ _OBJC_IVAR_$_StreamGroupStats._packetLossRateAccumulator
+ _OBJC_IVAR_$_UplinkSegment._firResponseTime
+ _OBJC_IVAR_$_VCAggregatorMultiway._constrainedConnectionDuration
+ _OBJC_IVAR_$_VCAggregatorMultiway._countConstrainedConnectionDuration
+ _OBJC_IVAR_$_VCAggregatorMultiway._countExpensiveConnectionDuration
+ _OBJC_IVAR_$_VCAggregatorMultiway._expensiveConnectionDuration
+ _OBJC_IVAR_$_VCReportingDistribution._histogramIncrementFactor
+ _VCReportingDistributionKeys_FIRResponseTime
+ ___81-[RTCReportingAgent startLogTimerWithInterval:reportingMultiplier:category:type:]_block_invoke.126
+ ___block_literal_global.383
+ ___block_literal_global.393
+ ___block_literal_global.476
+ ___reportingSetUserInfo_block_invoke.389
+ ___reportingSetUserInfo_block_invoke.390
+ ___reportingSetUserInfo_block_invoke.390.cold.1
+ __unnamed_array_storage.727
+ _objc_msgSend$checkSegmentCanBeUpdated:
+ _objc_msgSend$constrainedConnectionDuration
+ _objc_msgSend$expensiveConnectionDuration
+ _objc_msgSend$firResponseTime
+ _objc_msgSend$initWithHistogramType:reportingKeys:histogramIncrementFactor:
+ _objc_msgSend$initWithSignedHistogramType:reportingKeys:histogramIncrementFactor:
+ _objc_msgSend$packetLossRateAccumulator
+ _objc_msgSend$processDataMode:
+ _objc_msgSend$processKeyFrameReceived
+ _objc_msgSend$processKeyFrameReceived:
+ _objc_msgSend$processKeyFrameRequestSent
+ _objc_msgSend$processKeyFrameRequestSent:
+ _objc_msgSend$setConstrainedConnectionDuration:
+ _objc_msgSend$setExpensiveConnectionDuration:
+ _objc_msgSend$setPacketLossRateAccumulator:
+ _objc_msgSend$updateDataModeDuration
+ _objc_msgSend$updateModeDurationOnSegment:countExpensive:OrCountConstrained:
+ _sRTCReportingPeerCamClientName
- GCC_except_table943
- GCC_except_table955
- ___81-[RTCReportingAgent startLogTimerWithInterval:reportingMultiplier:category:type:]_block_invoke.123
- ___block_literal_global.379
- ___block_literal_global.389
- ___block_literal_global.472
- ___reportingSetUserInfo_block_invoke.385
- ___reportingSetUserInfo_block_invoke.386
- ___reportingSetUserInfo_block_invoke.386.cold.1
- __unnamed_array_storage.723
CStrings:
+ "-[VCReportingDistribution initWithHistogramType:reportingKeys:histogramIncrementFactor:]"
+ "-[VCReportingDistribution initWithSignedHistogramType:reportingKeys:histogramIncrementFactor:]"
+ "@32@0:8i16@20I28"
+ "ARxPLR"
+ "DMCDRTN"
+ "DMEDRTN"
+ "FIRRESPT"
+ "FIRRESPTH"
+ "FIRRESPTMAX"
+ "FIRRESPTMIN"
+ "FIRResponseTimeCount"
+ "FIRResponseTimeSum"
+ "PeerCam"
+ "T@\"NSString\",?,R,C"
+ "T@\"VCReportingDistribution\",R,V_firResponseTime"
+ "TI,V_packetLossRateAccumulator"
+ "TQ,V_constrainedConnectionDuration"
+ "TQ,V_expensiveConnectionDuration"
+ "_constrainedConnectionDuration"
+ "_countConstrainedConnectionDuration"
+ "_countExpensiveConnectionDuration"
+ "_expensiveConnectionDuration"
+ "_firResponseTime"
+ "_histogramIncrementFactor"
+ "_oldestPendingFirTime"
+ "_packetLossRateAccumulator"
+ "checkSegmentCanBeUpdated:"
+ "connectionDataMode"
+ "constrainedConnectionDuration"
+ "expensiveConnectionDuration"
+ "firResponseTime"
+ "initWithHistogramType:reportingKeys:histogramIncrementFactor:"
+ "initWithSignedHistogramType:reportingKeys:histogramIncrementFactor:"
+ "packetLossRateAccumulator"
+ "processDataMode:"
+ "processKeyFrameReceived"
+ "processKeyFrameReceived:"
+ "processKeyFrameRequestSent"
+ "processKeyFrameRequestSent:"
+ "setConstrainedConnectionDuration:"
+ "setExpensiveConnectionDuration:"
+ "setPacketLossRateAccumulator:"
+ "updateDataModeDuration"
+ "updateModeDurationOnSegment:countExpensive:OrCountConstrained:"
+ "v32@0:8@16B24B28"

```
