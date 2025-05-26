## ViceroyTrace

> `/System/Library/PrivateFrameworks/AVConference.framework/Frameworks/ViceroyTrace.framework/ViceroyTrace`

```diff

-2015.3.1.0.0
-  __TEXT.__text: 0x79ec8
+2025.5.1.0.0
+  __TEXT.__text: 0x7c80c
   __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x6684
-  __TEXT.__const: 0x1d60
-  __TEXT.__gcc_except_tab: 0x2d0
-  __TEXT.__cstring: 0x9472
-  __TEXT.__oslogstring: 0x8bde
+  __TEXT.__objc_methlist: 0x689c
+  __TEXT.__const: 0x1ea8
+  __TEXT.__gcc_except_tab: 0x2e0
+  __TEXT.__cstring: 0x9623
+  __TEXT.__oslogstring: 0x8fbb
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__unwind_info: 0xe94
-  __TEXT.__objc_classname: 0x385
-  __TEXT.__objc_methname: 0x1464a
-  __TEXT.__objc_methtype: 0x1324
-  __TEXT.__objc_stubs: 0xaec0
+  __TEXT.__unwind_info: 0xf28
+  __TEXT.__objc_classname: 0x3ac
+  __TEXT.__objc_methname: 0x14c45
+  __TEXT.__objc_methtype: 0x13f7
+  __TEXT.__objc_stubs: 0xb1a0
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__const: 0xb90
-  __DATA_CONST.__objc_classlist: 0x130
+  __DATA_CONST.__const: 0xba8
+  __DATA_CONST.__objc_classlist: 0x140
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10b28
-  __DATA_CONST.__objc_selrefs: 0x30f0
-  __DATA_CONST.__objc_classrefs: 0x1b0
-  __DATA_CONST.__objc_superrefs: 0x100
-  __DATA_CONST.__objc_arraydata: 0x1d0
-  __AUTH_CONST.__cfstring: 0xb2e0
+  __DATA_CONST.__objc_const: 0x10e80
+  __DATA_CONST.__objc_selrefs: 0x31d0
+  __DATA_CONST.__objc_classrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x110
+  __DATA_CONST.__objc_arraydata: 0x1e0
+  __AUTH_CONST.__cfstring: 0xb480
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH_CONST.__objc_const: 0x120
-  __AUTH_CONST.__objc_intobj: 0x318
+  __AUTH_CONST.__objc_const: 0x168
+  __AUTH_CONST.__objc_intobj: 0x330
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__auth_got: 0x578
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x18ec
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x192c
   __DATA.__data: 0x5b0
   __DATA.__bss: 0xe8
   __DATA.__common: 0x21
-  __DATA_DIRTY.__const: 0x200
-  __DATA_DIRTY.__objc_const: 0xbd0
-  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__const: 0x240
+  __DATA_DIRTY.__objc_const: 0xc18
+  __DATA_DIRTY.__objc_data: 0xaf0
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x18
+  __DATA_DIRTY.__bss: 0x11
   __DATA_DIRTY.__common: 0x1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2800
-  Symbols:   9286
-  CStrings:  5631
+  Functions: 2857
+  Symbols:   9456
+  CStrings:  5725
 
Symbols:
+ +[VCAggregator mediaStreamDirectionForSegmentReportDirection:]
+ +[VCAggregatorUtils sizeForVideoResolution:]
+ +[VCAggregatorUtils sizeForVideoResolution:].cold.1
+ -[MultiwayCall setTotalConnectionTime_Alt:]
+ -[MultiwayCall totalConnectionTime_Alt]
+ -[MultiwaySegment applyKnownDataModeToNewSegment:]
+ -[MultiwaySegment applyKnownDataModeToNewSegmentForLinkProperty:andNewSegmemnt:]
+ -[MultiwaySegment calculateDataModeDurationForLinkProperty:withCurrentState:andTime:]
+ -[MultiwaySegment endDataModeDuration:totalTime:time:hasStartedCalculating:]
+ -[MultiwaySegment finalizeAllDataModeDurationAtTime:]
+ -[MultiwaySegment flushAllDataModeDurationForLinkProperty:AtTime:]
+ -[MultiwaySegment markConnectionDurationHasStarted:withProperty:]
+ -[MultiwaySegment processDataMode:withTime:]
+ -[MultiwaySegment setupConnectionDurationStart:withProperty:setTime:]
+ -[MultiwaySegment startDataModeDuration:totalTime:time:hasStartedCalculating:]
+ -[MultiwayStream videoTxFecData]
+ -[RTCReportingAgent reportSegment:withMessageType:clientType:]
+ -[StreamGroupStats setVideoTierDurationData:]
+ -[StreamGroupStats videoTierDurationData]
+ -[StreamGroupStats videoTxFecData]
+ -[StreamGroupStats videoTxFecLevel]
+ -[UplinkSegment audioStreamTimestampJumpCount]
+ -[UplinkSegment audioStreamTimestampJumpDuration]
+ -[UplinkSegment audioStreamTimestampJumpMax]
+ -[UplinkSegment calculateUplinkAudioTimestampJumps:]
+ -[UplinkSegment setAudioStreamTimestampJumpCount:]
+ -[UplinkSegment setAudioStreamTimestampJumpMax:]
+ -[VCAggregator addAudioStreamTimestampJumpDurationToReport:]
+ -[VCAggregator messageTypeForSegmentReportWithDirection:]
+ -[VCAggregator updateTimestampJumpStats:]
+ -[VCAggregatorAirPlay messageTypeForSegmentReportWithDirection:]
+ -[VCAggregatorFaceTime updateConnectionSubTimes:]
+ -[VCAggregatorFaceTime updateTotalConnectionTime:]
+ -[VCAggregatorMultiway calculateUplinkAudioTimestampJumps:]
+ -[VCAggregatorMultiway updateReceivedVideoTierDurations:]
+ -[VCAggregatorMultiway updateTotalConnectionTime:]
+ -[VCAggregatorMultiway updateTotalConnectionTime:].cold.1
+ -[VCSymptomReporter reportNoPackets:WithOptionalDictionary:]
+ -[VCVideoFECData accumulate:]
+ -[VCVideoFECData dealloc]
+ -[VCVideoFECData init]
+ -[VCVideoFECData init].cold.1
+ -[VCVideoFECData init].cold.2
+ -[VCVideoFECData updateReport:]
+ -[VCVideoFECData updateReport:withStreamGroup:]
+ -[VCVideoFECData updateWithPayload:]
+ -[VCVideoFECData updateWithPayload:blockFecLevels:]
+ -[VCVideoTierDurationData accumulate:]
+ -[VCVideoTierDurationData accumulate:].cold.1
+ -[VCVideoTierDurationData accumulate:].cold.2
+ -[VCVideoTierDurationData dealloc]
+ -[VCVideoTierDurationData finalize]
+ -[VCVideoTierDurationData init]
+ -[VCVideoTierDurationData init].cold.1
+ -[VCVideoTierDurationData init].cold.2
+ -[VCVideoTierDurationData resolutionForVideoWidth:height:]
+ -[VCVideoTierDurationData updateCurrentReceivedVideoResolution:time:]
+ -[VCVideoTierDurationData updateReport:]
+ -[VCVideoTierDurationData updateReport:withStreamGroup:]
+ -[VCVideoTierDurationData updateWithPayload:]
+ -[VCVideoTierDurationData updateWithPayload:time:]
+ GCC_except_table100
+ GCC_except_table446
+ GCC_except_table977
+ GCC_except_table989
+ GCC_except_table99
+ _AudioTimestampJumpDuration
+ _OBJC_CLASS_$_VCVideoFECData
+ _OBJC_CLASS_$_VCVideoTierDurationData
+ _OBJC_IVAR_$_MultiwayCall._totalConnectionTime_Alt
+ _OBJC_IVAR_$_MultiwaySegment._constrainedConnectionDurationStart
+ _OBJC_IVAR_$_MultiwaySegment._expensiveConnectionDurationStart
+ _OBJC_IVAR_$_MultiwaySegment._isConnectionConstrained
+ _OBJC_IVAR_$_MultiwaySegment._isConnectionExpensive
+ _OBJC_IVAR_$_MultiwayStream._videoTxFecData
+ _OBJC_IVAR_$_StreamGroupStats._videoTierDurationData
+ _OBJC_IVAR_$_StreamGroupStats._videoTxFecData
+ _OBJC_IVAR_$_StreamGroupStats._videoTxFecLevel
+ _OBJC_IVAR_$_UplinkSegment._audioStreamTimestampJumpCount
+ _OBJC_IVAR_$_UplinkSegment._audioStreamTimestampJumpDuration
+ _OBJC_IVAR_$_UplinkSegment._audioStreamTimestampJumpMax
+ _OBJC_IVAR_$_VCAggregator._audioStreamTimestampJumpCount
+ _OBJC_IVAR_$_VCAggregator._audioStreamTimestampJumpDuration
+ _OBJC_IVAR_$_VCAggregator._audioStreamTimestampJumpMax
+ _OBJC_IVAR_$_VCAggregatorFaceTime._totalConnectionTime_Alt
+ _OBJC_IVAR_$_VCVideoFECData._videoTxFecLevel
+ _OBJC_IVAR_$_VCVideoTierDurationData._currentReceivedVideoResolution
+ _OBJC_IVAR_$_VCVideoTierDurationData._lastReceivedTierSwitchTime
+ _OBJC_IVAR_$_VCVideoTierDurationData._receivedVideoTierDuration
+ _OBJC_METACLASS_$_VCVideoFECData
+ _OBJC_METACLASS_$_VCVideoTierDurationData
+ _VideoTxFECLevels
+ __OBJC_$_INSTANCE_METHODS_VCVideoFECData
+ __OBJC_$_INSTANCE_METHODS_VCVideoTierDurationData
+ __OBJC_$_INSTANCE_VARIABLES_VCVideoFECData
+ __OBJC_$_INSTANCE_VARIABLES_VCVideoTierDurationData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_VCAggregatorDataCollector
+ __OBJC_CLASS_PROTOCOLS_$_VCVideoFECData
+ __OBJC_CLASS_PROTOCOLS_$_VCVideoTierDurationData
+ __OBJC_CLASS_RO_$_VCVideoFECData
+ __OBJC_CLASS_RO_$_VCVideoTierDurationData
+ __OBJC_METACLASS_RO_$_VCVideoFECData
+ __OBJC_METACLASS_RO_$_VCVideoTierDurationData
+ ___49-[VCAggregatorFaceTime updateConnectionSubTimes:]_block_invoke
+ ___62-[RTCReportingAgent reportSegment:withMessageType:clientType:]_block_invoke
+ __unnamed_array_storage.732
+ _objc_msgSend$addAudioStreamTimestampJumpDurationToReport:
+ _objc_msgSend$applyKnownDataModeToNewSegment:
+ _objc_msgSend$applyKnownDataModeToNewSegmentForLinkProperty:andNewSegmemnt:
+ _objc_msgSend$audioStreamTimestampJumpCount
+ _objc_msgSend$audioStreamTimestampJumpDuration
+ _objc_msgSend$audioStreamTimestampJumpMax
+ _objc_msgSend$calculateDataModeDurationForLinkProperty:withCurrentState:andTime:
+ _objc_msgSend$calculateUplinkAudioTimestampJumps:
+ _objc_msgSend$endDataModeDuration:totalTime:time:hasStartedCalculating:
+ _objc_msgSend$finalize
+ _objc_msgSend$flushAllDataModeDurationForLinkProperty:AtTime:
+ _objc_msgSend$markConnectionDurationHasStarted:withProperty:
+ _objc_msgSend$mediaStreamDirectionForSegmentReportDirection:
+ _objc_msgSend$messageTypeForSegmentReportWithDirection:
+ _objc_msgSend$numberWithUnsignedLong:
+ _objc_msgSend$processDataMode:withTime:
+ _objc_msgSend$reportNoPackets:WithOptionalDictionary:
+ _objc_msgSend$reportSegment:withMessageType:clientType:
+ _objc_msgSend$resolutionForVideoWidth:height:
+ _objc_msgSend$setAudioStreamTimestampJumpCount:
+ _objc_msgSend$setAudioStreamTimestampJumpMax:
+ _objc_msgSend$setTotalConnectionTime_Alt:
+ _objc_msgSend$setupConnectionDurationStart:withProperty:setTime:
+ _objc_msgSend$sizeForVideoResolution:
+ _objc_msgSend$startDataModeDuration:totalTime:time:hasStartedCalculating:
+ _objc_msgSend$totalConnectionTime_Alt
+ _objc_msgSend$updateConnectionSubTimes:
+ _objc_msgSend$updateCurrentReceivedVideoResolution:time:
+ _objc_msgSend$updateReceivedVideoTierDurations:
+ _objc_msgSend$updateTotalConnectionTime:
+ _objc_msgSend$updateWithPayload:blockFecLevels:
+ _objc_msgSend$updateWithPayload:time:
+ _objc_msgSend$videoTierDurationData
+ _objc_msgSend$videoTxFecData
+ _receivedVideoTierDuration
- -[MultiwaySegment constrainedConnectionDuration]
- -[MultiwaySegment expensiveConnectionDuration]
- -[MultiwaySegment setConstrainedConnectionDuration:]
- -[MultiwaySegment setExpensiveConnectionDuration:]
- -[RTCReportingAgent report:segmentDirection:clientType:]
- -[VCAggregatorFaceTime updateConnectionTimes:]
- -[VCAggregatorMultiway processDataMode:]
- -[VCAggregatorMultiway updateDataModeDuration]
- -[VCAggregatorMultiway updateModeDurationOnSegment:countExpensive:OrCountConstrained:]
- -[VCSymptomReporter reportNoPacketsWithOptionalDictionary:]
- GCC_except_table445
- GCC_except_table95
- GCC_except_table958
- GCC_except_table96
- GCC_except_table970
- _OBJC_IVAR_$_VCAggregatorMultiway._constrainedConnectionDuration
- _OBJC_IVAR_$_VCAggregatorMultiway._countConstrainedConnectionDuration
- _OBJC_IVAR_$_VCAggregatorMultiway._countExpensiveConnectionDuration
- _OBJC_IVAR_$_VCAggregatorMultiway._expensiveConnectionDuration
- ___46-[VCAggregatorFaceTime updateConnectionTimes:]_block_invoke
- ___56-[RTCReportingAgent report:segmentDirection:clientType:]_block_invoke
- __unnamed_array_storage.727
- _objc_msgSend$checkSegmentCanBeUpdated:
- _objc_msgSend$constrainedConnectionDuration
- _objc_msgSend$expensiveConnectionDuration
- _objc_msgSend$processDataMode:
- _objc_msgSend$report:segmentDirection:clientType:
- _objc_msgSend$reportNoPacketsWithOptionalDictionary:
- _objc_msgSend$setConstrainedConnectionDuration:
- _objc_msgSend$setExpensiveConnectionDuration:
- _objc_msgSend$updateConnectionTimes:
- _objc_msgSend$updateDataModeDuration
- _objc_msgSend$updateModeDurationOnSegment:countExpensive:OrCountConstrained:
CStrings:
+ " [%s] %s:%d %@(%p) Failed to create histogram"
+ " [%s] %s:%d %@(%p) Received data collector of a different class"
+ " [%s] %s:%d %@(%p) Received invalid data collector"
+ " [%s] %s:%d Connection timing for participantID=%@, TotalConnectionTime=%d"
+ " [%s] %s:%d Connection timing for participantID=%@, media=%@: TotalConnectionTime=%d, TransportConnectionTime=%d, MediaReceivedTime=%d, _mediaReceivedToProcessedTime=%d, _totalMediaStallSaveInterval=%d, original dictionary=%@"
+ " [%s] %s:%d Connection timing for participantID=%@: totalConnectionTime=%d, firstMKIDelta=%d, firstMediaReceivedDelta=%d, firstFrameProcessingDelta=%d, totalMediaStallSaveDelta=%d, original dictionary=%@"
+ " [%s] %s:%d Connection timing selected for participantID=%@: TotalConnectionTime=%d, StartConnectionTime=%d, TransportConnectionTime=%d, MediaReceivedTime=%d, _mediaReceivedToProcessedTime=%d, _totalMediaStallSaveInterval=%d, original dictionary=%@"
+ " [%s] %s:%d Connection timing: incomplete timing for participantID=%@ received=%@"
+ " [%s] %s:%d Failed to create histogram"
+ " [%s] %s:%d Failed to init self"
+ " [%s] %s:%d Failed to initialize"
+ " [%s] %s:%d Failed to initialize tier duration histogram"
+ " [%s] %s:%d Invalid resolution: %d"
+ " [%s] %s:%d Received data collector of a different class"
+ " [%s] %s:%d Received invalid data collector"
+ " [%s] %s:%d Reported invalid video width=%d height=%d"
+ " [%s] %s:%d SymptomReporter: reporting symptom on NoRemotePacketWiFi with remote participant"
+ "+[VCAggregatorUtils sizeForVideoResolution:]"
+ "-[RTCReportingAgent reportSegment:withMessageType:clientType:]_block_invoke"
+ "-[VCAggregatorFaceTime updateConnectionSubTimes:]_block_invoke"
+ "-[VCAggregatorFaceTime updateTotalConnectionTime:]"
+ "-[VCAggregatorMultiway updateTotalConnectionTime:]"
+ "-[VCSymptomReporter reportNoPackets:WithOptionalDictionary:]"
+ "-[VCVideoFECData init]"
+ "-[VCVideoTierDurationData accumulate:]"
+ "-[VCVideoTierDurationData init]"
+ "-[VCVideoTierDurationData updateWithPayload:time:]"
+ "@\"VCVideoFECData\""
+ "@\"VCVideoTierDurationData\""
+ "A"
+ "AFECL"
+ "ATJC"
+ "ATJD"
+ "ATJM"
+ "I20@0:8i16"
+ "NoPacketsWiFi"
+ "RXVTDH"
+ "T@\"VCHistogram\",R,V_audioStreamTimestampJumpDuration"
+ "T@\"VCReportingHistogram\",R,V_videoTxFecLevel"
+ "T@\"VCVideoFECData\",R,V_videoTxFecData"
+ "T@\"VCVideoTierDurationData\",V_videoTierDurationData"
+ "TI,V_audioStreamTimestampJumpCount"
+ "TI,V_totalConnectionTime_Alt"
+ "TQ,V_audioStreamTimestampJumpMax"
+ "VCASTimestampJumpCount"
+ "VCASTimestampJumpDuration"
+ "VCASTimestampJumpMax"
+ "VCSPIDSID"
+ "VCVideoFECData"
+ "VCVideoTierDurationData"
+ "VFEC"
+ "[3B]"
+ "[3I]"
+ "[55B]"
+ "_audioStreamTimestampJumpCount"
+ "_audioStreamTimestampJumpDuration"
+ "_audioStreamTimestampJumpMax"
+ "_constrainedConnectionDurationStart"
+ "_currentReceivedVideoResolution"
+ "_expensiveConnectionDurationStart"
+ "_isConnectionConstrained"
+ "_isConnectionExpensive"
+ "_lastReceivedTierSwitchTime"
+ "_receivedVideoTierDuration"
+ "_totalConnectionTime_Alt"
+ "_videoTierDurationData"
+ "_videoTxFecData"
+ "_videoTxFecLevel"
+ "addAudioStreamTimestampJumpDurationToReport:"
+ "applyKnownDataModeToNewSegment:"
+ "applyKnownDataModeToNewSegmentForLinkProperty:andNewSegmemnt:"
+ "audioStreamTimestampJumpCount"
+ "audioStreamTimestampJumpDuration"
+ "audioStreamTimestampJumpMax"
+ "calculateDataModeDurationForLinkProperty:withCurrentState:andTime:"
+ "calculateUplinkAudioTimestampJumps:"
+ "endDataModeDuration:totalTime:time:hasStartedCalculating:"
+ "finalize"
+ "finalizeAllDataModeDurationAtTime:"
+ "flushAllDataModeDurationForLinkProperty:AtTime:"
+ "markConnectionDurationHasStarted:withProperty:"
+ "mediaStreamDirectionForSegmentReportDirection:"
+ "messageTypeForSegmentReportWithDirection:"
+ "numberWithUnsignedLong:"
+ "processDataMode:withTime:"
+ "q24@0:8I16I20"
+ "reportNoPackets:WithOptionalDictionary:"
+ "reportSegment:withMessageType:clientType:"
+ "resolutionForVideoWidth:height:"
+ "setAudioStreamTimestampJumpCount:"
+ "setAudioStreamTimestampJumpMax:"
+ "setTotalConnectionTime_Alt:"
+ "setVideoTierDurationData:"
+ "setupConnectionDurationStart:withProperty:setTime:"
+ "sizeForVideoResolution:"
+ "startDataModeDuration:totalTime:time:hasStartedCalculating:"
+ "totalConnectionTime_Alt"
+ "updateConnectionSubTimes:"
+ "updateCurrentReceivedVideoResolution:time:"
+ "updateReceivedVideoTierDurations:"
+ "updateTimestampJumpStats:"
+ "updateTotalConnectionTime:"
+ "updateWithPayload:blockFecLevels:"
+ "updateWithPayload:time:"
+ "v24@0:8C16I20"
+ "v28@0:8C16I20I24"
+ "v28@0:8I16d20"
+ "v32@0:8@\"NSDictionary\"16S24i28"
+ "v32@0:8@\"NSDictionary\"16d24"
+ "v32@0:8@16S24i28"
+ "v32@0:8I16C20d24"
+ "v32@0:8q16d24"
+ "v48@0:8^I16^I24d32^B40"
+ "videoTierDurationData"
+ "videoTxFecData"
+ "videoTxFecLevel"
+ "{CGSize=dd}24@0:8q16"
- " [%s] %s:%d Connection timing for media=%@: TotalConnectionTime=%d, TransportConnectionTime=%d, MediaReceivedTime=%d, _mediaReceivedToProcessedTime=%d, _totalMediaStallSaveInterval=%d, original dictionary=%@"
- " [%s] %s:%d Connection timing: incomplete timing received=%@"
- " [%s] %s:%d Connection timing: totalConnectionTime=%d, firstMKIDelta=%d, firstMediaReceivedDelta=%d, firstFrameProcessingDelta=%d, totalMediaStallSaveDelta=%d, original dictionary=%@"
- "-[RTCReportingAgent report:segmentDirection:clientType:]_block_invoke"
- "-[VCAggregatorFaceTime updateConnectionTimes:]_block_invoke"
- "-[VCSymptomReporter reportNoPacketsWithOptionalDictionary:]"
- "TQ,V_constrainedConnectionDuration"
- "TQ,V_expensiveConnectionDuration"
- "[54B]"
- "_countConstrainedConnectionDuration"
- "_countExpensiveConnectionDuration"
- "constrainedConnectionDuration"
- "expensiveConnectionDuration"
- "processDataMode:"
- "report:segmentDirection:clientType:"
- "reportNoPacketsWithOptionalDictionary:"
- "setConstrainedConnectionDuration:"
- "setExpensiveConnectionDuration:"
- "updateConnectionTimes:"
- "updateDataModeDuration"
- "updateModeDurationOnSegment:countExpensive:OrCountConstrained:"
- "v32@0:8@\"NSDictionary\"16i24i28"
- "v32@0:8@16B24B28"
- "v32@0:8@16i24i28"

```
