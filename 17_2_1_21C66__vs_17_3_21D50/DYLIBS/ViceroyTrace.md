## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2005.6.1.1.2
-  __TEXT.__text: 0x74448
+2010.3.1.0.0
+  __TEXT.__text: 0x78e40
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x6264
-  __TEXT.__const: 0x1a68
+  __TEXT.__objc_methlist: 0x657c
+  __TEXT.__const: 0x1cd0
   __TEXT.__gcc_except_tab: 0x2d0
-  __TEXT.__cstring: 0x8c21
-  __TEXT.__oslogstring: 0x8608
+  __TEXT.__cstring: 0x9335
+  __TEXT.__oslogstring: 0x8bde
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0xe18
-  __TEXT.__objc_classname: 0x324
-  __TEXT.__objc_methname: 0x135e9
-  __TEXT.__objc_methtype: 0x121e
-  __TEXT.__objc_stubs: 0xa720
+  __TEXT.__unwind_info: 0xe78
+  __TEXT.__objc_classname: 0x385
+  __TEXT.__objc_methname: 0x14296
+  __TEXT.__objc_methtype: 0x1302
+  __TEXT.__objc_stubs: 0xaca0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0xae0
-  __DATA_CONST.__objc_classlist: 0x118
-  __DATA_CONST.__objc_protolist: 0x28
+  __DATA_CONST.__const: 0xb88
+  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xff28
-  __DATA_CONST.__objc_selrefs: 0x2f18
+  __DATA_CONST.__objc_const: 0x10978
+  __DATA_CONST.__objc_selrefs: 0x3068
   __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__cfstring: 0xa980
+  __AUTH_CONST.__cfstring: 0xb180
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_const: 0x48
+  __AUTH_CONST.__objc_const: 0x120
   __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__auth_got: 0x578
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_classrefs: 0x198
-  __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x17ec
-  __DATA.__data: 0x548
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_classrefs: 0x1b0
+  __DATA.__objc_superrefs: 0x100
+  __DATA.__objc_ivar: 0x18c0
+  __DATA.__data: 0x5a8
   __DATA.__bss: 0xe8
   __DATA.__common: 0x21
   __DATA_DIRTY.__const: 0x200

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2682
-  Symbols:   8877
-  CStrings:  5370
+  Functions: 2774
+  Symbols:   9206
+  CStrings:  5586
 
Symbols:
+ -[DownlinkSegment processVTPEgressIngressTelemetry:]
+ -[DownlinkSegment setTotalVTPDownlinkEgressMediaPackets:]
+ -[DownlinkSegment setTotalVTPDownlinkIngressMediaPackets:]
+ -[DownlinkSegment totalVTPDownlinkEgressMediaPackets]
+ -[DownlinkSegment totalVTPDownlinkIngressMediaPackets]
+ -[MultiwaySegment processRTEventCommon:]
+ -[MultiwayStream averageVideoRxFecBitrate]
+ -[MultiwayStream averageVideoTxFecBitrate]
+ -[MultiwayStream cameraCaptureData]
+ -[MultiwayStream processData:algosScorer:algosScorerAlternate:timestamp:]
+ -[MultiwayStream transmitterAVHostTimeData]
+ -[MultiwayStream videoPlayerDisplayData]
+ -[RTCReportingAgent updateSymptomCount:]
+ -[StreamGroupStats audioTierBundling_Alternate]
+ -[StreamGroupStats audioTierChangeHistogram]
+ -[StreamGroupStats audioTierCodecBitrate_Alternate]
+ -[StreamGroupStats audioTierCodecPayload_Alternate]
+ -[StreamGroupStats audioTierREDMaxDelay_Alternate]
+ -[StreamGroupStats audioTierREDPayload_Alternate]
+ -[StreamGroupStats averageVideoRxFecBitrate]
+ -[StreamGroupStats averageVideoTxFecBitrate]
+ -[StreamGroupStats setAverageVideoRxFecBitrate:]
+ -[StreamGroupStats setAverageVideoTxFecBitrate:]
+ -[StreamGroupStats transmitterAVHostTimeData]
+ -[StreamGroupStats videoPlayerDisplayData]
+ -[UplinkSegment cameraCaptureData]
+ -[UplinkSegment processStreamGroupStats:]
+ -[UplinkSegment processStreamGroupStats:].cold.1
+ -[UplinkSegment processStreamGroupStats:].cold.2
+ -[UplinkSegment processVTPEgressIngressTelemetry:]
+ -[UplinkSegment releaseWRMMetrics]
+ -[UplinkSegment setTotalVTPUplinkEgressMediaPackets:]
+ -[UplinkSegment setTotalVTPUplinkIngressMediaPackets:]
+ -[UplinkSegment totalVTPUplinkEgressMediaPackets]
+ -[UplinkSegment totalVTPUplinkIngressMediaPackets]
+ -[VCAggregator algosScoreAggregatorAlternate]
+ -[VCAggregatorMultiway applyKnownWRMMetricsToNewUplinkSegment:]
+ -[VCAggregatorMultiway calculateAverageReceivingBitrateForStreamGroup:audioStreamsCount:avgAudioRecvBitrate:vedioStreamsCount:avgVedioRecvBitrate:]
+ -[VCAggregatorMultiway processVTPEgressIngressTelemetry:]
+ -[VCAggregatorMultiway releaseWRMMetrics]
+ -[VCReportingDeltaDistribution absoluteMax]
+ -[VCReportingDeltaDistribution absoluteMin]
+ -[VCReportingDeltaDistribution absoluteSum]
+ -[VCReportingDeltaDistribution accumulate:]
+ -[VCReportingDeltaDistribution deltaHistogram]
+ -[VCReportingDeltaDistribution initWithSignedHistogramType:reportingKeys:]
+ -[VCReportingDeltaDistribution initWithSignedHistogramType:reportingKeys:].cold.1
+ -[VCReportingDeltaDistribution initWithSignedHistogramType:reportingKeys:].cold.2
+ -[VCReportingDeltaDistribution updateReport:]
+ -[VCReportingDeltaDistribution updateReport:withStreamGroup:]
+ -[VCReportingDeltaDistribution updateWithPayload:]
+ -[VCReportingDeltaDistribution updateWithPayload:].cold.1
+ -[VCReportingDistribution accumulate:]
+ -[VCReportingDistribution accumulate:].cold.1
+ -[VCReportingDistribution count]
+ -[VCReportingDistribution dealloc]
+ -[VCReportingDistribution histogram]
+ -[VCReportingDistribution initWithHistogramType:reportingKeys:]
+ -[VCReportingDistribution initWithHistogramType:reportingKeys:].cold.1
+ -[VCReportingDistribution initWithHistogramType:reportingKeys:].cold.2
+ -[VCReportingDistribution initWithKeys:]
+ -[VCReportingDistribution initWithKeys:].cold.1
+ -[VCReportingDistribution initWithKeys:].cold.2
+ -[VCReportingDistribution initWithSignedHistogramType:reportingKeys:]
+ -[VCReportingDistribution initWithSignedHistogramType:reportingKeys:].cold.1
+ -[VCReportingDistribution initWithSignedHistogramType:reportingKeys:].cold.2
+ -[VCReportingDistribution keys]
+ -[VCReportingDistribution max]
+ -[VCReportingDistribution min]
+ -[VCReportingDistribution sum]
+ -[VCReportingDistribution updateReport:]
+ -[VCReportingDistribution updateReport:withStreamGroup:]
+ -[VCReportingDistribution updateReport:withStreamGroup:].cold.1
+ -[VCReportingDistribution updateWithPayload:]
+ -[VCReportingDistribution updateWithPayload:].cold.1
+ -[VCSignedHistogram addOnlyExactMatchingValue:increment:]
+ -[VCSignedHistogram addValue:withIncrement:]
+ -[VCSignedHistogram initWithType:bucketValues:]
+ -[VCSignedHistogram initWithType:bucketValues:].cold.1
+ -[VCSignedHistogram initWithType:bucketValues:].cold.2
+ -[VCSignedHistogram initWithType:bucketValues:].cold.3
+ -[VCSignedHistogram merge:]
+ -[VCSignedHistogram signedRanges]
+ GCC_except_table943
+ GCC_except_table955
+ _AudioTierChangeFrequencyRanges
+ _CameraCaptureFrameRate
+ _MaxWlanRadioCoexistence
+ _OBJC_CLASS_$_VCReportingDeltaDistribution
+ _OBJC_CLASS_$_VCReportingDistribution
+ _OBJC_CLASS_$_VCSignedHistogram
+ _OBJC_IVAR_$_DownlinkSegment._totalVTPDownlinkEgressMediaPackets
+ _OBJC_IVAR_$_DownlinkSegment._totalVTPDownlinkIngressMediaPackets
+ _OBJC_IVAR_$_MultiwaySegment._wlanMaxSingleOutagePeriod
+ _OBJC_IVAR_$_MultiwaySegment._wlanOffChannelTime
+ _OBJC_IVAR_$_MultiwaySegment._wlanRadioCoexistence
+ _OBJC_IVAR_$_MultiwayStream._averageVideoRxFecBitrate
+ _OBJC_IVAR_$_MultiwayStream._averageVideoTxFecBitrate
+ _OBJC_IVAR_$_MultiwayStream._cameraCaptureData
+ _OBJC_IVAR_$_MultiwayStream._transmitterAVHostTimeData
+ _OBJC_IVAR_$_MultiwayStream._videoPlayerDisplayData
+ _OBJC_IVAR_$_StreamGroupStats._audioTierBundling_Alternate
+ _OBJC_IVAR_$_StreamGroupStats._audioTierChangeHistogram
+ _OBJC_IVAR_$_StreamGroupStats._audioTierCodecBitrate_Alternate
+ _OBJC_IVAR_$_StreamGroupStats._audioTierCodecPayload_Alternate
+ _OBJC_IVAR_$_StreamGroupStats._audioTierREDMaxDelay_Alternate
+ _OBJC_IVAR_$_StreamGroupStats._audioTierREDPayload_Alternate
+ _OBJC_IVAR_$_StreamGroupStats._averageVideoRxFecBitrate
+ _OBJC_IVAR_$_StreamGroupStats._averageVideoTxFecBitrate
+ _OBJC_IVAR_$_StreamGroupStats._transmitterAVHostTimeData
+ _OBJC_IVAR_$_StreamGroupStats._videoPlayerDisplayData
+ _OBJC_IVAR_$_UplinkSegment._cameraCaptureData
+ _OBJC_IVAR_$_UplinkSegment._totalVTPUplinkEgressMediaPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVTPUplinkIngressMediaPackets
+ _OBJC_IVAR_$_UplinkSegment.transmitterAVHostTimeData
+ _OBJC_IVAR_$_VCAggregator._algosScoreAggregatorAlternate
+ _OBJC_IVAR_$_VCAggregator._algosScorerAlternate
+ _OBJC_IVAR_$_VCAggregator._redOverhead
+ _OBJC_IVAR_$_VCAggregatorMultiway._cameraCaptureData
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVTPDownlinkEgressMediaPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVTPDownlinkIngressMediaPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVTPUplinkEgressMediaPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVTPUplinkIngressMediaPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmLinkTypeCellServingCellType
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmLinkTypeCellSignalBar
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmLinkTypeCellSignalStrength
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmLinkTypeChangeReasonCode
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmLinkTypeSuggestion
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmLinkTypeWifiCCA
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmLinkTypeWifiPacketLoss
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmLinkTypeWifiRSSI
+ _OBJC_IVAR_$_VCAggregatorMultiway._wrmLinkTypeWifiSNR
+ _OBJC_IVAR_$_VCAggregatorMultiway.avgReceivingBitrate
+ _OBJC_IVAR_$_VCAggregatorMultiway.maxTargetBitrate
+ _OBJC_IVAR_$_VCReportingDeltaDistribution._absoluteMax
+ _OBJC_IVAR_$_VCReportingDeltaDistribution._absoluteMin
+ _OBJC_IVAR_$_VCReportingDeltaDistribution._absoluteSum
+ _OBJC_IVAR_$_VCReportingDeltaDistribution._deltaHistogram
+ _OBJC_IVAR_$_VCReportingDistribution._count
+ _OBJC_IVAR_$_VCReportingDistribution._histogram
+ _OBJC_IVAR_$_VCReportingDistribution._keys
+ _OBJC_IVAR_$_VCReportingDistribution._max
+ _OBJC_IVAR_$_VCReportingDistribution._min
+ _OBJC_IVAR_$_VCReportingDistribution._sum
+ _OBJC_IVAR_$_VCSignedHistogram._signedRanges
+ _OBJC_METACLASS_$_VCReportingDeltaDistribution
+ _OBJC_METACLASS_$_VCReportingDistribution
+ _OBJC_METACLASS_$_VCSignedHistogram
+ _TxAVHostTimeDelta
+ _VCReportingDeltaDistributionKey_AggregatedAbsoluteAverage
+ _VCReportingDeltaDistributionKey_AggregatedAbsoluteMax
+ _VCReportingDeltaDistributionKey_AggregatedAbsoluteMin
+ _VCReportingDeltaDistributionKey_ReportingAbsoluteMax
+ _VCReportingDeltaDistributionKey_ReportingAbsoluteMin
+ _VCReportingDeltaDistributionKey_ReportingAbsoluteSum
+ _VCReportingDeltaDistributionKeys_TransmitterHostTimeDelta
+ _VCReportingDistributionKey_AggregatedAverage
+ _VCReportingDistributionKey_AggregatedHistogram
+ _VCReportingDistributionKey_AggregatedMax
+ _VCReportingDistributionKey_AggregatedMin
+ _VCReportingDistributionKey_ReportingCount
+ _VCReportingDistributionKey_ReportingMax
+ _VCReportingDistributionKey_ReportingMin
+ _VCReportingDistributionKey_ReportingSum
+ _VCReportingDistributionKeys_CameraCaptureFrameRate
+ _VCReportingDistributionKeys_VideoPlayerDisplayFrameRate
+ _VideoPlayerDisplayFrameRate
+ _WlanMaxSingleOutagePeriod
+ _WlanOffChannelTime
+ __OBJC_$_INSTANCE_METHODS_VCReportingDeltaDistribution
+ __OBJC_$_INSTANCE_METHODS_VCReportingDistribution
+ __OBJC_$_INSTANCE_METHODS_VCSignedHistogram
+ __OBJC_$_INSTANCE_VARIABLES_VCReportingDeltaDistribution
+ __OBJC_$_INSTANCE_VARIABLES_VCReportingDistribution
+ __OBJC_$_INSTANCE_VARIABLES_VCSignedHistogram
+ __OBJC_$_PROP_LIST_VCReportingDeltaDistribution
+ __OBJC_$_PROP_LIST_VCReportingDistribution
+ __OBJC_$_PROP_LIST_VCSignedHistogram
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VCAggregatorDataCollector
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VCAggregatorDataCollector
+ __OBJC_CLASS_PROTOCOLS_$_VCReportingDeltaDistribution
+ __OBJC_CLASS_PROTOCOLS_$_VCReportingDistribution
+ __OBJC_CLASS_RO_$_VCReportingDeltaDistribution
+ __OBJC_CLASS_RO_$_VCReportingDistribution
+ __OBJC_CLASS_RO_$_VCSignedHistogram
+ __OBJC_LABEL_PROTOCOL_$_VCAggregatorDataCollector
+ __OBJC_METACLASS_RO_$_VCReportingDeltaDistribution
+ __OBJC_METACLASS_RO_$_VCReportingDistribution
+ __OBJC_METACLASS_RO_$_VCSignedHistogram
+ __OBJC_PROTOCOL_$_VCAggregatorDataCollector
+ ___40-[RTCReportingAgent updateSymptomCount:]_block_invoke
+ ___49-[VCAggregatorMultiway updateWRMMetrics:payload:]_block_invoke.cold.1
+ ___block_literal_global.379
+ ___block_literal_global.389
+ ___block_literal_global.472
+ ___reportingSetUserInfo_block_invoke.385
+ ___reportingSetUserInfo_block_invoke.386
+ ___reportingSetUserInfo_block_invoke.386.cold.1
+ __unnamed_array_storage.723
+ _objc_msgSend$absoluteMax
+ _objc_msgSend$absoluteMin
+ _objc_msgSend$absoluteSum
+ _objc_msgSend$accumulate:
+ _objc_msgSend$algosScoreAggregatorAlternate
+ _objc_msgSend$applyKnownWRMMetricsToNewUplinkSegment:
+ _objc_msgSend$audioTierBundling_Alternate
+ _objc_msgSend$audioTierChangeHistogram
+ _objc_msgSend$audioTierCodecBitrate_Alternate
+ _objc_msgSend$audioTierCodecPayload_Alternate
+ _objc_msgSend$audioTierREDMaxDelay_Alternate
+ _objc_msgSend$audioTierREDPayload_Alternate
+ _objc_msgSend$averageVideoRxFecBitrate
+ _objc_msgSend$averageVideoTxFecBitrate
+ _objc_msgSend$avgReceivingBitrate
+ _objc_msgSend$calculateAverageReceivingBitrateForStreamGroup:audioStreamsCount:avgAudioRecvBitrate:vedioStreamsCount:avgVedioRecvBitrate:
+ _objc_msgSend$cameraCaptureData
+ _objc_msgSend$duplicationType
+ _objc_msgSend$histogram
+ _objc_msgSend$initWithHistogramType:reportingKeys:
+ _objc_msgSend$initWithKeys:
+ _objc_msgSend$initWithSignedHistogramType:reportingKeys:
+ _objc_msgSend$keys
+ _objc_msgSend$longValue
+ _objc_msgSend$max
+ _objc_msgSend$min
+ _objc_msgSend$processData:algosScorer:algosScorerAlternate:timestamp:
+ _objc_msgSend$processRTEventCommon:
+ _objc_msgSend$processStreamGroupStats:
+ _objc_msgSend$processVTPEgressIngressTelemetry:
+ _objc_msgSend$releaseWRMMetrics
+ _objc_msgSend$setAverageVideoRxFecBitrate:
+ _objc_msgSend$setAverageVideoTxFecBitrate:
+ _objc_msgSend$signedRanges
+ _objc_msgSend$sum
+ _objc_msgSend$transmitterAVHostTimeData
+ _objc_msgSend$updateReport:
+ _objc_msgSend$updateReport:withStreamGroup:
+ _objc_msgSend$updateWithPayload:
+ _objc_msgSend$videoPlayerDisplayData
+ _objc_msgSend$wrmLinkTypeCellServingCellType
+ _objc_msgSend$wrmLinkTypeCellSignalBar
+ _objc_msgSend$wrmLinkTypeCellSignalStrength
+ _objc_msgSend$wrmLinkTypeChangeReasonCode
+ _objc_msgSend$wrmLinkTypeSuggestion
+ _objc_msgSend$wrmLinkTypeWifiCCA
+ _objc_msgSend$wrmLinkTypeWifiPacketLoss
+ _objc_msgSend$wrmLinkTypeWifiRSSI
+ _objc_msgSend$wrmLinkTypeWifiSNR
+ _objc_retain_x20
- -[MultiwayStream processData:algosScorer:timestamp:]
- -[StreamGroupStats averageVideoFecBitrate]
- -[StreamGroupStats setAverageVideoFecBitrate:]
- -[UplinkSegment processTransmitterStats:]
- -[UplinkSegment processTransmitterStats:].cold.1
- -[UplinkSegment processTransmitterStats:].cold.2
- GCC_except_table911
- GCC_except_table923
- _OBJC_IVAR_$_StreamGroupStats._averageVideoFecBitrate
- ___block_literal_global.377
- ___block_literal_global.387
- ___block_literal_global.467
- ___reportingSetUserInfo_block_invoke.383
- ___reportingSetUserInfo_block_invoke.384
- ___reportingSetUserInfo_block_invoke.384.cold.1
- __unnamed_array_storage.718
- _objc_msgSend$NANData
- _objc_msgSend$averageVideoFecBitrate
- _objc_msgSend$processData:algosScorer:timestamp:
- _objc_msgSend$processTransmitterStats:
- _objc_msgSend$setAverageVideoFecBitrate:
- _objc_release_x25
CStrings:
+ " [%s] %s:%d %@(%p) Failed to find bucket ranges for histogramType=%d"
+ " [%s] %s:%d %@(%p) Failed to initialize VCReportingDistribution"
+ " [%s] %s:%d %@(%p) Failed to initialize VCSignedHistogram"
+ " [%s] %s:%d %@(%p) Failed to initialize histogram for type=%d"
+ " [%s] %s:%d %@(%p) Failed to initialize reporting distribution"
+ " [%s] %s:%d %@(%p) Received in payload"
+ " [%s] %s:%d %@(%p) Received nil keys argument"
+ " [%s] %s:%d %@(%p) Received nil payload"
+ " [%s] %s:%d %@(%p) Received nil reportDict"
+ " [%s] %s:%d Adding WRM metrics to uplink segment report=%@ wrmLinkTypeSuggestion=%@ wrmLinkTypeChangeReasonCode=%@ wrmLinkTypeWifiRSSI=%@  wrmLinkTypeWifiSNR=%@ _currentSegment.wrmLinkTypeWifiCCA=%@ wrmLinkTypeWifiPacketLoss=%@ wrmLinkTypeCellSignalStrength=%@ wrmLinkTypeCellSignalBar=%@ wrmLinkTypeCellServingCellType=%@"
+ " [%s] %s:%d Failed to find bucket ranges for histogramType=%d"
+ " [%s] %s:%d Failed to initialize VCReportingDistribution"
+ " [%s] %s:%d Failed to initialize VCSignedHistogram"
+ " [%s] %s:%d Failed to initialize histogram for type=%d"
+ " [%s] %s:%d Failed to initialize reporting distribution"
+ " [%s] %s:%d Received in payload"
+ " [%s] %s:%d Received nil keys argument"
+ " [%s] %s:%d Received nil payload"
+ " [%s] %s:%d Received nil reportDict"
+ " [%s] %s:%d Updating WRM metrics in uplink segment report=%@ wrmLinkTypeSuggestion=%@ wrmLinkTypeChangeReasonCode=%@ wrmLinkTypeWifiRSSI=%@ wrmLinkTypeWifiSNR=%@ wrmLinkTypeWifiCCA=%@ wrmLinkTypeWifiPacketLoss=%@ wrmLinkTypeCellSignalStrength=%@ wrmLinkTypeCellSignalBar=%@ wrmLinkTypeCellServingCellType=%@"
+ "-[UplinkSegment addSegmentWRMReportStats:]"
+ "-[UplinkSegment processStreamGroupStats:]"
+ "-[VCAggregatorMultiway updateWRMMetrics:payload:]_block_invoke"
+ "-[VCReportingDeltaDistribution initWithSignedHistogramType:reportingKeys:]"
+ "-[VCReportingDeltaDistribution updateWithPayload:]"
+ "-[VCReportingDistribution accumulate:]"
+ "-[VCReportingDistribution initWithHistogramType:reportingKeys:]"
+ "-[VCReportingDistribution initWithKeys:]"
+ "-[VCReportingDistribution initWithSignedHistogramType:reportingKeys:]"
+ "-[VCReportingDistribution updateReport:withStreamGroup:]"
+ "-[VCReportingDistribution updateWithPayload:]"
+ "-[VCSignedHistogram initWithType:bucketValues:]"
+ "@\"VCReportingDeltaDistribution\""
+ "@\"VCReportingDistribution\""
+ "AATBH_A"
+ "AATCC"
+ "ATierChangeCount"
+ "AVHTDAbsSum"
+ "AVHTDCount"
+ "AVHTDMax"
+ "AVHTDMin"
+ "AVHTDSum"
+ "AlternateParticipantID"
+ "BitRateAlt"
+ "BundleAlt"
+ "CAMCFRMAX"
+ "CAMCFRMIN"
+ "CAMDUR"
+ "CAMFC"
+ "CAMFR"
+ "CAMFRH"
+ "MAXSOP"
+ "NWOffChannelTime"
+ "NWOutagePeriodMax"
+ "NWRadioCoexMax"
+ "OFFCHANNEL"
+ "PayloadAlt"
+ "RADIOCOEX"
+ "REDMD_A"
+ "REDNPU_A"
+ "RedMaxDelayAlt"
+ "RedPayloadsAlt"
+ "T@\"NSDictionary\",R,V_keys"
+ "T@\"NSNumber\",C,V_wrmLinkTypeCellServingCellType"
+ "T@\"NSNumber\",C,V_wrmLinkTypeCellSignalBar"
+ "T@\"NSNumber\",C,V_wrmLinkTypeCellSignalStrength"
+ "T@\"NSNumber\",C,V_wrmLinkTypeChangeReasonCode"
+ "T@\"NSNumber\",C,V_wrmLinkTypeSuggestion"
+ "T@\"NSNumber\",C,V_wrmLinkTypeWifiCCA"
+ "T@\"NSNumber\",C,V_wrmLinkTypeWifiPacketLoss"
+ "T@\"NSNumber\",C,V_wrmLinkTypeWifiRSSI"
+ "T@\"NSNumber\",C,V_wrmLinkTypeWifiSNR"
+ "T@\"VCAlgosStreamingScoreAggregator\",R,V_algosScoreAggregatorAlternate"
+ "T@\"VCHistogram\",R,V_deltaHistogram"
+ "T@\"VCHistogram\",R,V_histogram"
+ "T@\"VCReportingDeltaDistribution\",R,V_transmitterAVHostTimeData"
+ "T@\"VCReportingDistribution\",R,V_cameraCaptureData"
+ "T@\"VCReportingDistribution\",R,V_videoPlayerDisplayData"
+ "T@\"VCReportingHistogram\",R,V_audioTierBundling_Alternate"
+ "T@\"VCReportingHistogram\",R,V_audioTierChangeHistogram"
+ "T@\"VCReportingHistogram\",R,V_audioTierCodecBitrate_Alternate"
+ "T@\"VCReportingHistogram\",R,V_audioTierCodecPayload_Alternate"
+ "T@\"VCReportingHistogram\",R,V_audioTierREDMaxDelay_Alternate"
+ "T@\"VCReportingHistogram\",R,V_audioTierREDPayload_Alternate"
+ "TALGOS_A"
+ "TAMBR_A"
+ "TAPAY_A"
+ "TI,R,V_averageVideoRxFecBitrate"
+ "TI,R,V_averageVideoTxFecBitrate"
+ "TI,V_averageVideoRxFecBitrate"
+ "TI,V_averageVideoTxFecBitrate"
+ "TQ,V_totalVTPDownlinkEgressMediaPackets"
+ "TQ,V_totalVTPDownlinkIngressMediaPackets"
+ "TQ,V_totalVTPUplinkEgressMediaPackets"
+ "TQ,V_totalVTPUplinkIngressMediaPackets"
+ "Td,R,V_absoluteMax"
+ "Td,R,V_absoluteMin"
+ "Td,R,V_absoluteSum"
+ "Td,R,V_count"
+ "Td,R,V_max"
+ "Td,R,V_min"
+ "Td,R,V_sum"
+ "Tr^i,R,V_signedRanges"
+ "VCAggregatorDataCollector"
+ "VCReportingDeltaDistribution"
+ "VCReportingDeltaDistributionKey_AggregatedAbsoluteAverage"
+ "VCReportingDeltaDistributionKey_AggregatedAbsoluteMax"
+ "VCReportingDeltaDistributionKey_AggregatedAbsoluteMin"
+ "VCReportingDeltaDistributionKey_ReportingAbsoluteMax"
+ "VCReportingDeltaDistributionKey_ReportingAbsoluteMin"
+ "VCReportingDeltaDistributionKey_ReportingAbsoluteSum"
+ "VCReportingDistribution"
+ "VCReportingDistributionKey_AggregatedAverage"
+ "VCReportingDistributionKey_AggregatedHistogram"
+ "VCReportingDistributionKey_AggregatedMax"
+ "VCReportingDistributionKey_AggregatedMin"
+ "VCReportingDistributionKey_ReportingCount"
+ "VCReportingDistributionKey_ReportingMax"
+ "VCReportingDistributionKey_ReportingMin"
+ "VCReportingDistributionKey_ReportingSum"
+ "VCSignedHistogram"
+ "VPDFR"
+ "VPDFRH"
+ "VPDFRMAX"
+ "VPDFRMIN"
+ "VPFDC"
+ "VPFDCD"
+ "VTABSAVHTD"
+ "VTAVHTD"
+ "VTAVHTDH"
+ "VTAVHTDMAX"
+ "VTAVHTDMIN"
+ "VTPDLEP"
+ "VTPDLIP"
+ "VTPDownlinkEgressMediaPkts"
+ "VTPDownlinkIngressMediaPkts"
+ "VTPULEP"
+ "VTPULIP"
+ "VTPUplinkEgressPkts"
+ "VTPUplinkIngressPkts"
+ "_absoluteMax"
+ "_absoluteMin"
+ "_absoluteSum"
+ "_algosScoreAggregatorAlternate"
+ "_algosScorerAlternate"
+ "_audioTierBundling_Alternate"
+ "_audioTierChangeHistogram"
+ "_audioTierCodecBitrate_Alternate"
+ "_audioTierCodecPayload_Alternate"
+ "_audioTierREDMaxDelay_Alternate"
+ "_audioTierREDPayload_Alternate"
+ "_averageVideoRxFecBitrate"
+ "_averageVideoTxFecBitrate"
+ "_cameraCaptureData"
+ "_count"
+ "_deltaHistogram"
+ "_histogram"
+ "_keys"
+ "_max"
+ "_min"
+ "_redOverhead"
+ "_signedRanges"
+ "_sum"
+ "_totalVTPDownlinkEgressMediaPackets"
+ "_totalVTPDownlinkIngressMediaPackets"
+ "_totalVTPUplinkEgressMediaPackets"
+ "_totalVTPUplinkIngressMediaPackets"
+ "_transmitterAVHostTimeData"
+ "_videoPlayerDisplayData"
+ "_wlanMaxSingleOutagePeriod"
+ "_wlanOffChannelTime"
+ "_wlanRadioCoexistence"
+ "absoluteMax"
+ "absoluteMin"
+ "absoluteSum"
+ "accumulate:"
+ "algosScoreAggregatorAlternate"
+ "applyKnownWRMMetricsToNewUplinkSegment:"
+ "audioTierBundling_Alternate"
+ "audioTierChangeHistogram"
+ "audioTierCodecBitrate_Alternate"
+ "audioTierCodecPayload_Alternate"
+ "audioTierREDMaxDelay_Alternate"
+ "audioTierREDPayload_Alternate"
+ "averageVideoRxFecBitrate"
+ "averageVideoTxFecBitrate"
+ "calculateAverageReceivingBitrateForStreamGroup:audioStreamsCount:avgAudioRecvBitrate:vedioStreamsCount:avgVedioRecvBitrate:"
+ "cameraCaptureData"
+ "deltaHistogram"
+ "histogram"
+ "initWithHistogramType:reportingKeys:"
+ "initWithKeys:"
+ "initWithSignedHistogramType:reportingKeys:"
+ "keys"
+ "longValue"
+ "max"
+ "min"
+ "processData:algosScorer:algosScorerAlternate:timestamp:"
+ "processRTEventCommon:"
+ "processStreamGroupStats:"
+ "processVTPEgressIngressTelemetry:"
+ "r^i"
+ "r^i16@0:8"
+ "releaseWRMMetrics"
+ "setAverageVideoRxFecBitrate:"
+ "setAverageVideoTxFecBitrate:"
+ "setTotalVTPDownlinkEgressMediaPackets:"
+ "setTotalVTPDownlinkIngressMediaPackets:"
+ "setTotalVTPUplinkEgressMediaPackets:"
+ "setTotalVTPUplinkIngressMediaPackets:"
+ "signedRanges"
+ "sum"
+ "totalVTPDownlinkEgressMediaPackets"
+ "totalVTPDownlinkIngressMediaPackets"
+ "totalVTPUplinkEgressMediaPackets"
+ "totalVTPUplinkIngressMediaPackets"
+ "transmitterAVHostTimeData"
+ "updateReport:"
+ "updateReport:withStreamGroup:"
+ "updateWithPayload:"
+ "v24@0:8@\"NSMutableDictionary\"16"
+ "v24@0:8@\"NSObject<VCAggregatorDataCollector>\"16"
+ "v32@0:8@\"NSMutableDictionary\"16@\"NSNumber\"24"
+ "v48@0:8@16@24@32d40"
+ "v56@0:8@16^I24^I32^I40^I48"
+ "videoPlayerDisplayData"
- " [%s] %s:%d PHS: NAN interface profile=%@"
- "-[UplinkSegment processTransmitterStats:]"
- "NANData"
- "TI,V_averageVideoFecBitrate"
- "_averageVideoFecBitrate"
- "averageVideoFecBitrate"
- "processData:algosScorer:timestamp:"
- "processTransmitterStats:"
- "setAverageVideoFecBitrate:"
- "v40@0:8@16@24d32"

```
