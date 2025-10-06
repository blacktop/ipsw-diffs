## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2000.8.1.1.1
-  __TEXT.__text: 0x70f9c
-  __TEXT.__auth_stubs: 0xae0
-  __TEXT.__objc_methlist: 0x5db0
-  __TEXT.__const: 0x1938
-  __TEXT.__gcc_except_tab: 0x2bc
-  __TEXT.__cstring: 0x85e4
-  __TEXT.__oslogstring: 0x8358
+2005.6.1.1.2
+  __TEXT.__text: 0x74448
+  __TEXT.__auth_stubs: 0xad0
+  __TEXT.__objc_methlist: 0x6264
+  __TEXT.__const: 0x1a68
+  __TEXT.__gcc_except_tab: 0x2d0
+  __TEXT.__cstring: 0x8c21
+  __TEXT.__oslogstring: 0x8608
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0xdfc
+  __TEXT.__unwind_info: 0xe18
   __TEXT.__objc_classname: 0x324
-  __TEXT.__objc_methname: 0x11ccd
-  __TEXT.__objc_methtype: 0x1001
-  __TEXT.__objc_stubs: 0x9ee0
+  __TEXT.__objc_methname: 0x135e9
+  __TEXT.__objc_methtype: 0x121e
+  __TEXT.__objc_stubs: 0xa720
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0xaa0
+  __DATA_CONST.__const: 0xae0
   __DATA_CONST.__objc_classlist: 0x118
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0xf518
-  __DATA_CONST.__objc_selrefs: 0x2c20
-  __DATA_CONST.__objc_arraydata: 0x180
-  __AUTH_CONST.__cfstring: 0xa120
+  __DATA_CONST.__objc_const: 0xff28
+  __DATA_CONST.__objc_selrefs: 0x2f18
+  __DATA_CONST.__objc_arraydata: 0x1d0
+  __AUTH_CONST.__cfstring: 0xa980
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__objc_intobj: 0x288
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__auth_got: 0x580
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__auth_got: 0x578
   __AUTH.__objc_data: 0x50
   __DATA.__objc_classrefs: 0x198
   __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x1708
+  __DATA.__objc_ivar: 0x17ec
   __DATA.__data: 0x548
   __DATA.__bss: 0xe8
   __DATA.__common: 0x21
-  __DATA_DIRTY.__const: 0x220
+  __DATA_DIRTY.__const: 0x200
   __DATA_DIRTY.__objc_const: 0xbd0
   __DATA_DIRTY.__objc_data: 0xaa0
   __DATA_DIRTY.__data: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 92AF9921-BE23-3C21-B31A-2BA318F5E9F2
-  Functions: 2578
-  Symbols:   8543
-  CStrings:  6390
+  UUID: 8E77B4AE-54D9-3976-82D2-4E57340BDC28
+  Functions: 2682
+  Symbols:   8877
+  CStrings:  6726
 
Symbols:
+ -[DownlinkSegment JBSpikeSizeDeltaHistogram]
+ -[DownlinkSegment REDOverhead]
+ -[DownlinkSegment REDPlayedCount]
+ -[DownlinkSegment idrReceivedCount]
+ -[DownlinkSegment jitterBufferJumpSpikeCount]
+ -[DownlinkSegment jitterBufferSlopeSpikeCount]
+ -[DownlinkSegment maxJitterBufferSpikeSizeDelta]
+ -[DownlinkSegment setIdrReceivedCount:]
+ -[DownlinkSegment setJitterBufferJumpSpikeCount:]
+ -[DownlinkSegment setJitterBufferSlopeSpikeCount:]
+ -[DownlinkSegment setMaxJitterBufferSpikeSizeDelta:]
+ -[DownlinkSegment setTotalFIRCount:]
+ -[DownlinkSegment setTotalFIRReceivedCount:]
+ -[DownlinkSegment totalFIRCount]
+ -[DownlinkSegment totalFIRReceivedCount]
+ -[MultiwayCall poorConnectionPercentageThresholdFromTelemetry]
+ -[MultiwayCall setPoorConnectionPercentageThresholdFromTelemetry:]
+ -[MultiwayStream idrReceivedCount]
+ -[MultiwayStream streamID]
+ -[RTCReportingAgent abcSymptomsReportingTelemetryThresholdValues]
+ -[RTCReportingAgent setAbcSymptomsReportingTelemetryThresholdValues:]
+ -[StreamGroupStats firReceivedCount]
+ -[StreamGroupStats idrReceivedCount]
+ -[StreamGroupStats setFirReceivedCount:]
+ -[StreamGroupStats setIdrReceivedCount:]
+ -[StreamGroupStats setTotalFIRCount:]
+ -[StreamGroupStats setTotalFIRDemandCount:]
+ -[StreamGroupStats setTotalRTPDownlinkEgressAudioPackets:]
+ -[StreamGroupStats setTotalRTPDownlinkEgressVideoPackets:]
+ -[StreamGroupStats setTotalRTPDownlinkIngressAudioPackets:]
+ -[StreamGroupStats setTotalRTPDownlinkIngressNonDupAudioPackets:]
+ -[StreamGroupStats setTotalRTPDownlinkIngressNonDupVideoPackets:]
+ -[StreamGroupStats setTotalRTPDownlinkIngressVideoPackets:]
+ -[StreamGroupStats setTotalRTPUplinkIngressAudioPackets:]
+ -[StreamGroupStats setTotalRTPUplinkIngressVideoPackets:]
+ -[StreamGroupStats totalFIRCount]
+ -[StreamGroupStats totalFIRDemandCount]
+ -[StreamGroupStats totalRTPDownlinkEgressAudioPackets]
+ -[StreamGroupStats totalRTPDownlinkEgressVideoPackets]
+ -[StreamGroupStats totalRTPDownlinkIngressAudioPackets]
+ -[StreamGroupStats totalRTPDownlinkIngressNonDupAudioPackets]
+ -[StreamGroupStats totalRTPDownlinkIngressNonDupVideoPackets]
+ -[StreamGroupStats totalRTPDownlinkIngressVideoPackets]
+ -[StreamGroupStats totalRTPUplinkIngressAudioPackets]
+ -[StreamGroupStats totalRTPUplinkIngressVideoPackets]
+ -[UplinkSegment lastReportedVCMQEgressAudioPackets]
+ -[UplinkSegment lastReportedVCMQEgressNonDupAudioPackets]
+ -[UplinkSegment lastReportedVCMQEgressNonDupPackets]
+ -[UplinkSegment lastReportedVCMQEgressNonDupVideoPackets]
+ -[UplinkSegment lastReportedVCMQEgressPackets]
+ -[UplinkSegment lastReportedVCMQEgressVideoPackets]
+ -[UplinkSegment lastReportedVCMQFlushedPackets]
+ -[UplinkSegment lastReportedVCMQIngressAudioPackets]
+ -[UplinkSegment lastReportedVCMQIngressPackets]
+ -[UplinkSegment lastReportedVCMQIngressQueuedPackets]
+ -[UplinkSegment lastReportedVCMQIngressVideoPackets]
+ -[UplinkSegment processMediaQueueEgressIngressTelemetry:]
+ -[UplinkSegment setLastReportedVCMQEgressAudioPackets:]
+ -[UplinkSegment setLastReportedVCMQEgressNonDupAudioPackets:]
+ -[UplinkSegment setLastReportedVCMQEgressNonDupPackets:]
+ -[UplinkSegment setLastReportedVCMQEgressNonDupVideoPackets:]
+ -[UplinkSegment setLastReportedVCMQEgressPackets:]
+ -[UplinkSegment setLastReportedVCMQEgressVideoPackets:]
+ -[UplinkSegment setLastReportedVCMQFlushedPackets:]
+ -[UplinkSegment setLastReportedVCMQIngressAudioPackets:]
+ -[UplinkSegment setLastReportedVCMQIngressPackets:]
+ -[UplinkSegment setLastReportedVCMQIngressQueuedPackets:]
+ -[UplinkSegment setLastReportedVCMQIngressVideoPackets:]
+ -[UplinkSegment setTotalVCMQEgressAudioPackets:]
+ -[UplinkSegment setTotalVCMQEgressNonDupAudioPackets:]
+ -[UplinkSegment setTotalVCMQEgressNonDupPackets:]
+ -[UplinkSegment setTotalVCMQEgressNonDupVideoPackets:]
+ -[UplinkSegment setTotalVCMQEgressPackets:]
+ -[UplinkSegment setTotalVCMQEgressVideoPackets:]
+ -[UplinkSegment setTotalVCMQFlushedPackets:]
+ -[UplinkSegment setTotalVCMQIngressAudioPackets:]
+ -[UplinkSegment setTotalVCMQIngressPackets:]
+ -[UplinkSegment setTotalVCMQIngressQueuedPackets:]
+ -[UplinkSegment setTotalVCMQIngressVideoPackets:]
+ -[UplinkSegment totalVCMQEgressAudioPackets]
+ -[UplinkSegment totalVCMQEgressNonDupAudioPackets]
+ -[UplinkSegment totalVCMQEgressNonDupPackets]
+ -[UplinkSegment totalVCMQEgressNonDupVideoPackets]
+ -[UplinkSegment totalVCMQEgressPackets]
+ -[UplinkSegment totalVCMQEgressVideoPackets]
+ -[UplinkSegment totalVCMQFlushedPackets]
+ -[UplinkSegment totalVCMQIngressAudioPackets]
+ -[UplinkSegment totalVCMQIngressPackets]
+ -[UplinkSegment totalVCMQIngressQueuedPackets]
+ -[UplinkSegment totalVCMQIngressVideoPackets]
+ -[UplinkSegment updateLastValuesForMediaQueueEgressIngressTelemetry:]
+ -[VCAggregatorAudioStream processRealtimeStats:]
+ -[VCAggregatorMultiway addStreamGroupTelemetryForCall:callReport:maxMediaQualityKeysForParticipant:]
+ -[VCAggregatorMultiway multiwayStreamWithStreamID:inStreamGroup:]
+ -[VCAggregatorMultiway processDownlinkStreamData:streamGroupID:]
+ -[VCAggregatorMultiway processMediaQueueEgressIngressTelemetry:]
+ -[VCAggregatorMultiway streamGroupIDForParticipant:withStreamID:]
+ -[VCAggregatorMultiway updateFIRReceivedCount:]
+ -[VCAggregatorMultiway updateFIRReceivedCount:].cold.1
+ -[VCSymptomReporter reportAudioConnectionTimeFromTelemetryWithOptionalDictionary:]
+ -[VCSymptomReporter reportAudioErasurePercentageFromTelemetryWithOptionalDictionary:]
+ -[VCSymptomReporter reportPoorConnectionPercentageFromTelemetryWithOptionalDictionary:]
+ -[VCSymptomReporter reportVideoConnectionTimeFromTelemetryWithOptionalDictionary:]
+ -[VCSymptomReporter reportVideoStallPercentageFromTelemetryWithOptionalDictionary:]
+ GCC_except_table58
+ GCC_except_table65
+ GCC_except_table911
+ GCC_except_table923
+ _JBSpikeSizeBucketRanges
+ _OBJC_IVAR_$_DownlinkSegment._JBSpikeSizeDeltaHistogram
+ _OBJC_IVAR_$_DownlinkSegment._REDOverhead
+ _OBJC_IVAR_$_DownlinkSegment._REDPlayedCount
+ _OBJC_IVAR_$_DownlinkSegment._idrReceivedCount
+ _OBJC_IVAR_$_DownlinkSegment._jitterBufferJumpSpikeCount
+ _OBJC_IVAR_$_DownlinkSegment._jitterBufferSlopeSpikeCount
+ _OBJC_IVAR_$_DownlinkSegment._maxJitterBufferSpikeSizeDelta
+ _OBJC_IVAR_$_DownlinkSegment._totalFIRCount
+ _OBJC_IVAR_$_DownlinkSegment._totalFIRReceivedCount
+ _OBJC_IVAR_$_MultiwayCall._poorConnectionPercentageThresholdFromTelemetry
+ _OBJC_IVAR_$_MultiwayStream._idrReceivedCount
+ _OBJC_IVAR_$_RTCReportingAgent._abcSymptomsReportingTelemetryThresholdValues
+ _OBJC_IVAR_$_StreamGroupStats._firReceivedCount
+ _OBJC_IVAR_$_StreamGroupStats._idrReceivedCount
+ _OBJC_IVAR_$_StreamGroupStats._totalFIRCount
+ _OBJC_IVAR_$_StreamGroupStats._totalFIRDemandCount
+ _OBJC_IVAR_$_StreamGroupStats._totalRTPDownlinkEgressAudioPackets
+ _OBJC_IVAR_$_StreamGroupStats._totalRTPDownlinkEgressVideoPackets
+ _OBJC_IVAR_$_StreamGroupStats._totalRTPDownlinkIngressAudioPackets
+ _OBJC_IVAR_$_StreamGroupStats._totalRTPDownlinkIngressNonDupAudioPackets
+ _OBJC_IVAR_$_StreamGroupStats._totalRTPDownlinkIngressNonDupVideoPackets
+ _OBJC_IVAR_$_StreamGroupStats._totalRTPDownlinkIngressVideoPackets
+ _OBJC_IVAR_$_StreamGroupStats._totalRTPUplinkIngressAudioPackets
+ _OBJC_IVAR_$_StreamGroupStats._totalRTPUplinkIngressVideoPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQEgressAudioPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQEgressNonDupAudioPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQEgressNonDupPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQEgressNonDupVideoPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQEgressPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQEgressVideoPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQFlushedPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQIngressAudioPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQIngressPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQIngressQueuedPackets
+ _OBJC_IVAR_$_UplinkSegment._lastReportedVCMQIngressVideoPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQEgressAudioPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQEgressNonDupAudioPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQEgressNonDupPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQEgressNonDupVideoPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQEgressPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQEgressVideoPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQFlushedPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQIngressAudioPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQIngressPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQIngressQueuedPackets
+ _OBJC_IVAR_$_UplinkSegment._totalVCMQIngressVideoPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQEgressAudioPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQEgressNonDupAudioPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQEgressNonDupPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQEgressNonDupVideoPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQEgressPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQEgressVideoPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQFlushedPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQIngressAudioPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQIngressPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQIngressQueuedPackets
+ _OBJC_IVAR_$_VCAggregatorMultiway._totalVCMQIngressVideoPackets
+ _REDOverheadRanges
+ _REDPlayedCountRanges
+ ___block_descriptor_56_e8_32o40o48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_literal_global.377
+ ___block_literal_global.387
+ ___block_literal_global.467
+ ___reportingSetUserInfo_block_invoke.383
+ ___reportingSetUserInfo_block_invoke.384
+ ___reportingSetUserInfo_block_invoke.384.cold.1
+ __unnamed_array_storage.718
+ _checkAndReportAbcSymptomOnRegressedKPI
+ _checkAndReportAbcSymptomsOnRegressedKPIs
+ _objc_msgSend$JBSpikeSizeDeltaHistogram
+ _objc_msgSend$REDOverhead
+ _objc_msgSend$REDPlayedCount
+ _objc_msgSend$addStreamGroupTelemetryForCall:callReport:maxMediaQualityKeysForParticipant:
+ _objc_msgSend$firReceivedCount
+ _objc_msgSend$idrReceivedCount
+ _objc_msgSend$jitterBufferJumpSpikeCount
+ _objc_msgSend$jitterBufferSlopeSpikeCount
+ _objc_msgSend$maxJitterBufferSpikeSizeDelta
+ _objc_msgSend$multiwayStreamWithStreamID:inStreamGroup:
+ _objc_msgSend$processDownlinkStreamData:streamGroupID:
+ _objc_msgSend$processMediaQueueEgressIngressTelemetry:
+ _objc_msgSend$reportAudioConnectionTimeFromTelemetryWithOptionalDictionary:
+ _objc_msgSend$reportAudioErasurePercentageFromTelemetryWithOptionalDictionary:
+ _objc_msgSend$reportPoorConnectionPercentageFromTelemetryWithOptionalDictionary:
+ _objc_msgSend$reportVideoConnectionTimeFromTelemetryWithOptionalDictionary:
+ _objc_msgSend$reportVideoStallPercentageFromTelemetryWithOptionalDictionary:
+ _objc_msgSend$setFirReceivedCount:
+ _objc_msgSend$setIdrReceivedCount:
+ _objc_msgSend$setJitterBufferJumpSpikeCount:
+ _objc_msgSend$setJitterBufferSlopeSpikeCount:
+ _objc_msgSend$setLastReportedVCMQEgressAudioPackets:
+ _objc_msgSend$setLastReportedVCMQEgressNonDupAudioPackets:
+ _objc_msgSend$setLastReportedVCMQEgressNonDupPackets:
+ _objc_msgSend$setLastReportedVCMQEgressNonDupVideoPackets:
+ _objc_msgSend$setLastReportedVCMQEgressPackets:
+ _objc_msgSend$setLastReportedVCMQEgressVideoPackets:
+ _objc_msgSend$setLastReportedVCMQFlushedPackets:
+ _objc_msgSend$setLastReportedVCMQIngressAudioPackets:
+ _objc_msgSend$setLastReportedVCMQIngressPackets:
+ _objc_msgSend$setLastReportedVCMQIngressQueuedPackets:
+ _objc_msgSend$setLastReportedVCMQIngressVideoPackets:
+ _objc_msgSend$setMaxJitterBufferSpikeSizeDelta:
+ _objc_msgSend$setTotalFIRCount:
+ _objc_msgSend$setTotalFIRDemandCount:
+ _objc_msgSend$setTotalRTPDownlinkEgressAudioPackets:
+ _objc_msgSend$setTotalRTPDownlinkEgressVideoPackets:
+ _objc_msgSend$setTotalRTPDownlinkIngressAudioPackets:
+ _objc_msgSend$setTotalRTPDownlinkIngressNonDupAudioPackets:
+ _objc_msgSend$setTotalRTPDownlinkIngressNonDupVideoPackets:
+ _objc_msgSend$setTotalRTPDownlinkIngressVideoPackets:
+ _objc_msgSend$setTotalRTPUplinkIngressAudioPackets:
+ _objc_msgSend$setTotalRTPUplinkIngressVideoPackets:
+ _objc_msgSend$streamGroupIDForParticipant:withStreamID:
+ _objc_msgSend$totalFIRCount
+ _objc_msgSend$totalFIRDemandCount
+ _objc_msgSend$totalRTPDownlinkEgressAudioPackets
+ _objc_msgSend$totalRTPDownlinkEgressVideoPackets
+ _objc_msgSend$totalRTPDownlinkIngressAudioPackets
+ _objc_msgSend$totalRTPDownlinkIngressNonDupAudioPackets
+ _objc_msgSend$totalRTPDownlinkIngressNonDupVideoPackets
+ _objc_msgSend$totalRTPDownlinkIngressVideoPackets
+ _objc_msgSend$totalRTPUplinkIngressAudioPackets
+ _objc_msgSend$totalRTPUplinkIngressVideoPackets
+ _objc_msgSend$totalVCMQEgressAudioPackets
+ _objc_msgSend$totalVCMQEgressNonDupAudioPackets
+ _objc_msgSend$totalVCMQEgressNonDupPackets
+ _objc_msgSend$totalVCMQEgressNonDupVideoPackets
+ _objc_msgSend$totalVCMQEgressPackets
+ _objc_msgSend$totalVCMQEgressVideoPackets
+ _objc_msgSend$totalVCMQFlushedPackets
+ _objc_msgSend$totalVCMQIngressAudioPackets
+ _objc_msgSend$totalVCMQIngressPackets
+ _objc_msgSend$totalVCMQIngressQueuedPackets
+ _objc_msgSend$totalVCMQIngressVideoPackets
+ _objc_msgSend$unsignedIntegerValue
+ _objc_msgSend$updateFIRReceivedCount:
+ _objc_msgSend$updateLastValuesForMediaQueueEgressIngressTelemetry:
- -[VCAggregatorAudioStream remoteMicProcessRealtimeStats:]
- -[VCAggregatorMultiway addStreamGroupTelemetryForCall:callReport:]
- GCC_except_table53
- GCC_except_table60
- GCC_except_table834
- ___block_literal_global.369
- ___block_literal_global.379
- ___block_literal_global.459
- ___reportingSetUserInfo_block_invoke.375
- ___reportingSetUserInfo_block_invoke.376
- ___reportingSetUserInfo_block_invoke.376.cold.1
- __unnamed_array_storage.685
- _objc_msgSend$addStreamGroupTelemetryForCall:callReport:
- _objc_msgSend$remoteMicProcessRealtimeStats:
- _objc_release_x27
CStrings:
+ " [%s] %s:%d SymptomReporter: reporting symptom on AudioConnectionTimeFromTelemetry with remote participant"
+ " [%s] %s:%d SymptomReporter: reporting symptom on AudioErasurePercentageFromTelemetry with remote participant"
+ " [%s] %s:%d SymptomReporter: reporting symptom on PoorConnectionPercentageFromTelemetry with remote participant"
+ " [%s] %s:%d SymptomReporter: reporting symptom on VideoConnectionTimeFromTelemetry with remote participant"
+ " [%s] %s:%d SymptomReporter: reporting symptom on VideoStallPercentageFromTelemetry with remote participant"
+ " [%s] %s:%d Updating FIR received count with nil participant ID"
+ "-[VCAggregatorMultiway updateFIRReceivedCount:]"
+ "-[VCSymptomReporter reportAudioConnectionTimeFromTelemetryWithOptionalDictionary:]"
+ "-[VCSymptomReporter reportAudioErasurePercentageFromTelemetryWithOptionalDictionary:]"
+ "-[VCSymptomReporter reportPoorConnectionPercentageFromTelemetryWithOptionalDictionary:]"
+ "-[VCSymptomReporter reportVideoConnectionTimeFromTelemetryWithOptionalDictionary:]"
+ "-[VCSymptomReporter reportVideoStallPercentageFromTelemetryWithOptionalDictionary:]"
+ "@128@0:8{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFDictionary}@?@B{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}}16"
+ "@28@0:8S16@20"
+ "AudioConnectionTimeFromTelemetry"
+ "AudioConnectionTimeRegressed"
+ "AudioErasurePercentageFromTelemetry"
+ "AudioErasurePercentageRegressed"
+ "B24@0:8^{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFDictionary}@?@B{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}}16"
+ "E"
+ "FIRFC"
+ "FIRRCVDC"
+ "FIRRCVDR"
+ "I28@0:8@16S24"
+ "IDRRCVDC"
+ "IDRRCVDR"
+ "JBJSR"
+ "JBJumpSpikeCount"
+ "JBSS"
+ "JBSSR"
+ "JBSlopeSpikeCount"
+ "JBSpikeSizeDelta"
+ "JBSpikeSizeDeltaHistogram"
+ "MJBSS"
+ "PoorConnectionPercentageFromTelemetry"
+ "PoorConnectionPercentageRegressed"
+ "REDO"
+ "REDOverhead"
+ "REDPC"
+ "REDPlayedCount"
+ "RTPDLEAP"
+ "RTPDLEVP"
+ "RTPDLIAP"
+ "RTPDLINDP"
+ "RTPDLIVP"
+ "RTPDownlinkEgressAudioPkts"
+ "RTPDownlinkEgressVideoPkts"
+ "RTPDownlinkIngressAudioPkts"
+ "RTPDownlinkIngressNonDupMediaPkts"
+ "RTPDownlinkIngressVideoPkts"
+ "RTPULAP"
+ "RTPULVP"
+ "RTPUplinkIngressAudioPkts"
+ "RTPUplinkIngressVideoPkts"
+ "RedOverheadDelay"
+ "RedRxPlayedCount"
+ "ReportingVC [%s] %s:%d Reporting symptom=%u on key=%d >= Telemetry threshold=%d"
+ "T@\"NSString\",R,V_streamID"
+ "T@\"VCHistogram\",R,V_REDOverhead"
+ "T@\"VCHistogram\",R,V_REDPlayedCount"
+ "T@\"VCReportingHistogram\",R,V_JBSpikeSizeDeltaHistogram"
+ "TI,R,V_idrReceivedCount"
+ "TI,V_idrReceivedCount"
+ "TI,V_jitterBufferJumpSpikeCount"
+ "TI,V_jitterBufferSlopeSpikeCount"
+ "TI,V_poorConnectionPercentageThresholdFromTelemetry"
+ "TI,V_totalFIRCount"
+ "TI,V_totalFIRDemandCount"
+ "TQ,V_firReceivedCount"
+ "TQ,V_lastReportedVCMQEgressAudioPackets"
+ "TQ,V_lastReportedVCMQEgressNonDupAudioPackets"
+ "TQ,V_lastReportedVCMQEgressNonDupPackets"
+ "TQ,V_lastReportedVCMQEgressNonDupVideoPackets"
+ "TQ,V_lastReportedVCMQEgressPackets"
+ "TQ,V_lastReportedVCMQEgressVideoPackets"
+ "TQ,V_lastReportedVCMQFlushedPackets"
+ "TQ,V_lastReportedVCMQIngressAudioPackets"
+ "TQ,V_lastReportedVCMQIngressPackets"
+ "TQ,V_lastReportedVCMQIngressQueuedPackets"
+ "TQ,V_lastReportedVCMQIngressVideoPackets"
+ "TQ,V_totalFIRReceivedCount"
+ "TQ,V_totalRTPDownlinkEgressAudioPackets"
+ "TQ,V_totalRTPDownlinkEgressVideoPackets"
+ "TQ,V_totalRTPDownlinkIngressAudioPackets"
+ "TQ,V_totalRTPDownlinkIngressNonDupAudioPackets"
+ "TQ,V_totalRTPDownlinkIngressNonDupVideoPackets"
+ "TQ,V_totalRTPDownlinkIngressVideoPackets"
+ "TQ,V_totalRTPUplinkIngressAudioPackets"
+ "TQ,V_totalRTPUplinkIngressVideoPackets"
+ "TQ,V_totalVCMQEgressAudioPackets"
+ "TQ,V_totalVCMQEgressNonDupAudioPackets"
+ "TQ,V_totalVCMQEgressNonDupPackets"
+ "TQ,V_totalVCMQEgressNonDupVideoPackets"
+ "TQ,V_totalVCMQEgressPackets"
+ "TQ,V_totalVCMQEgressVideoPackets"
+ "TQ,V_totalVCMQFlushedPackets"
+ "TQ,V_totalVCMQIngressAudioPackets"
+ "TQ,V_totalVCMQIngressPackets"
+ "TQ,V_totalVCMQIngressQueuedPackets"
+ "TQ,V_totalVCMQIngressVideoPackets"
+ "Td,V_maxJitterBufferSpikeSizeDelta"
+ "T{tagABCSymptomsReportingTelemetryThresholdValues=iiiii},GabcSymptomsReportingTelemetryThresholdValues,V_abcSymptomsReportingTelemetryThresholdValues"
+ "VCMQEAP"
+ "VCMQENDAP"
+ "VCMQENDP"
+ "VCMQENDVP"
+ "VCMQEP"
+ "VCMQEVP"
+ "VCMQEgressAudioPkts"
+ "VCMQEgressNonDupAudioPkts"
+ "VCMQEgressNonDupPkts"
+ "VCMQEgressNonDupVideoPkts"
+ "VCMQEgressPkts"
+ "VCMQEgressVideoPkts"
+ "VCMQFP"
+ "VCMQFlushedPkts"
+ "VCMQIAP"
+ "VCMQIP"
+ "VCMQIQP"
+ "VCMQIVP"
+ "VCMQIngressAudioPkts"
+ "VCMQIngressPkts"
+ "VCMQIngressQueuedPkts"
+ "VCMQIngressVideoPkts"
+ "VPBNRFC"
+ "VRxIDRC"
+ "VideoConnectionTimeFromTelemetry"
+ "VideoConnectionTimeRegressed"
+ "VideoStallPercentageFromTelemetry"
+ "VideoStallPercentageRegressed"
+ "Wired"
+ "[54B]"
+ "_JBSpikeSizeDeltaHistogram"
+ "_REDOverhead"
+ "_REDPlayedCount"
+ "_abcSymptomsReportingTelemetryThresholdValues"
+ "_firReceivedCount"
+ "_idrReceivedCount"
+ "_jitterBufferJumpSpikeCount"
+ "_jitterBufferSlopeSpikeCount"
+ "_lastReportedVCMQEgressAudioPackets"
+ "_lastReportedVCMQEgressNonDupAudioPackets"
+ "_lastReportedVCMQEgressNonDupPackets"
+ "_lastReportedVCMQEgressNonDupVideoPackets"
+ "_lastReportedVCMQEgressPackets"
+ "_lastReportedVCMQEgressVideoPackets"
+ "_lastReportedVCMQFlushedPackets"
+ "_lastReportedVCMQIngressAudioPackets"
+ "_lastReportedVCMQIngressPackets"
+ "_lastReportedVCMQIngressQueuedPackets"
+ "_lastReportedVCMQIngressVideoPackets"
+ "_maxJitterBufferSpikeSizeDelta"
+ "_poorConnectionPercentageThresholdFromTelemetry"
+ "_totalFIRCount"
+ "_totalFIRDemandCount"
+ "_totalFIRReceivedCount"
+ "_totalRTPDownlinkEgressAudioPackets"
+ "_totalRTPDownlinkEgressVideoPackets"
+ "_totalRTPDownlinkIngressAudioPackets"
+ "_totalRTPDownlinkIngressNonDupAudioPackets"
+ "_totalRTPDownlinkIngressNonDupVideoPackets"
+ "_totalRTPDownlinkIngressVideoPackets"
+ "_totalRTPUplinkIngressAudioPackets"
+ "_totalRTPUplinkIngressVideoPackets"
+ "_totalVCMQEgressAudioPackets"
+ "_totalVCMQEgressNonDupAudioPackets"
+ "_totalVCMQEgressNonDupPackets"
+ "_totalVCMQEgressNonDupVideoPackets"
+ "_totalVCMQEgressPackets"
+ "_totalVCMQEgressVideoPackets"
+ "_totalVCMQFlushedPackets"
+ "_totalVCMQIngressAudioPackets"
+ "_totalVCMQIngressPackets"
+ "_totalVCMQIngressQueuedPackets"
+ "_totalVCMQIngressVideoPackets"
+ "abcSymptomsReportingTelemetryThresholdValues"
+ "addStreamGroupTelemetryForCall:callReport:maxMediaQualityKeysForParticipant:"
+ "checkAndReportAbcSymptomOnRegressedKPI"
+ "firReceivedCount"
+ "idrReceivedCount"
+ "jitterBufferJumpSpikeCount"
+ "jitterBufferSlopeSpikeCount"
+ "lastReportedVCMQEgressAudioPackets"
+ "lastReportedVCMQEgressNonDupAudioPackets"
+ "lastReportedVCMQEgressNonDupPackets"
+ "lastReportedVCMQEgressNonDupVideoPackets"
+ "lastReportedVCMQEgressPackets"
+ "lastReportedVCMQEgressVideoPackets"
+ "lastReportedVCMQFlushedPackets"
+ "lastReportedVCMQIngressAudioPackets"
+ "lastReportedVCMQIngressPackets"
+ "lastReportedVCMQIngressQueuedPackets"
+ "lastReportedVCMQIngressVideoPackets"
+ "maxJitterBufferSpikeSizeDelta"
+ "multiwayStreamWithStreamID:inStreamGroup:"
+ "poorConnectionPercentageThresholdFromTelemetry"
+ "processDownlinkStreamData:streamGroupID:"
+ "processMediaQueueEgressIngressTelemetry:"
+ "reportAudioConnectionTimeFromTelemetryWithOptionalDictionary:"
+ "reportAudioErasurePercentageFromTelemetryWithOptionalDictionary:"
+ "reportPoorConnectionPercentageFromTelemetryWithOptionalDictionary:"
+ "reportVideoConnectionTimeFromTelemetryWithOptionalDictionary:"
+ "reportVideoStallPercentageFromTelemetryWithOptionalDictionary:"
+ "setAbcSymptomsReportingTelemetryThresholdValues:"
+ "setFirReceivedCount:"
+ "setIdrReceivedCount:"
+ "setJitterBufferJumpSpikeCount:"
+ "setJitterBufferSlopeSpikeCount:"
+ "setLastReportedVCMQEgressAudioPackets:"
+ "setLastReportedVCMQEgressNonDupAudioPackets:"
+ "setLastReportedVCMQEgressNonDupPackets:"
+ "setLastReportedVCMQEgressNonDupVideoPackets:"
+ "setLastReportedVCMQEgressPackets:"
+ "setLastReportedVCMQEgressVideoPackets:"
+ "setLastReportedVCMQFlushedPackets:"
+ "setLastReportedVCMQIngressAudioPackets:"
+ "setLastReportedVCMQIngressPackets:"
+ "setLastReportedVCMQIngressQueuedPackets:"
+ "setLastReportedVCMQIngressVideoPackets:"
+ "setMaxJitterBufferSpikeSizeDelta:"
+ "setPoorConnectionPercentageThresholdFromTelemetry:"
+ "setTotalFIRCount:"
+ "setTotalFIRDemandCount:"
+ "setTotalFIRReceivedCount:"
+ "setTotalRTPDownlinkEgressAudioPackets:"
+ "setTotalRTPDownlinkEgressVideoPackets:"
+ "setTotalRTPDownlinkIngressAudioPackets:"
+ "setTotalRTPDownlinkIngressNonDupAudioPackets:"
+ "setTotalRTPDownlinkIngressNonDupVideoPackets:"
+ "setTotalRTPDownlinkIngressVideoPackets:"
+ "setTotalRTPUplinkIngressAudioPackets:"
+ "setTotalRTPUplinkIngressVideoPackets:"
+ "setTotalVCMQEgressAudioPackets:"
+ "setTotalVCMQEgressNonDupAudioPackets:"
+ "setTotalVCMQEgressNonDupPackets:"
+ "setTotalVCMQEgressNonDupVideoPackets:"
+ "setTotalVCMQEgressPackets:"
+ "setTotalVCMQEgressVideoPackets:"
+ "setTotalVCMQFlushedPackets:"
+ "setTotalVCMQIngressAudioPackets:"
+ "setTotalVCMQIngressPackets:"
+ "setTotalVCMQIngressQueuedPackets:"
+ "setTotalVCMQIngressVideoPackets:"
+ "streamGroupIDForParticipant:withStreamID:"
+ "streamID"
+ "totalFIRCount"
+ "totalFIRDemandCount"
+ "totalFIRReceivedCount"
+ "totalRTPDownlinkEgressAudioPackets"
+ "totalRTPDownlinkEgressVideoPackets"
+ "totalRTPDownlinkIngressAudioPackets"
+ "totalRTPDownlinkIngressNonDupAudioPackets"
+ "totalRTPDownlinkIngressNonDupVideoPackets"
+ "totalRTPDownlinkIngressVideoPackets"
+ "totalRTPUplinkIngressAudioPackets"
+ "totalRTPUplinkIngressVideoPackets"
+ "totalVCMQEgressAudioPackets"
+ "totalVCMQEgressNonDupAudioPackets"
+ "totalVCMQEgressNonDupPackets"
+ "totalVCMQEgressNonDupVideoPackets"
+ "totalVCMQEgressPackets"
+ "totalVCMQEgressVideoPackets"
+ "totalVCMQFlushedPackets"
+ "totalVCMQIngressAudioPackets"
+ "totalVCMQIngressPackets"
+ "totalVCMQIngressQueuedPackets"
+ "totalVCMQIngressVideoPackets"
+ "unsignedIntegerValue"
+ "updateFIRReceivedCount:"
+ "updateLastValuesForMediaQueueEgressIngressTelemetry:"
+ "v36@0:8{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}16"
+ "v40@0:8@16@24^{tagMaxMediaQualityKeysForParticipant=iiiii}32"
+ "{tagABCSymptomsReportingTelemetryThresholdValues=\"audioConnectionTimeThreshold\"i\"audioErasurePercentageThreshold\"i\"poorConnectionPercentageThreshold\"i\"videoConnectionTimeThreshold\"i\"videoStallPercentageThreshold\"i}"
+ "{tagABCSymptomsReportingTelemetryThresholdValues=iiiii}16@0:8"
- "@112@0:8{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFDictionary}@?@B}16"
- "B24@0:8^{?=I^{__CFString}^{__CFDate}iB^v@^{__CFString}^{__CFString}^{__CFDictionary}@?@B}16"
- "[49B]"
- "addStreamGroupTelemetryForCall:callReport:"
- "remoteMicProcessRealtimeStats:"

```
