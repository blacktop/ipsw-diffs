## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/Versions/A/AVConference`

```diff

 2215.5.1.0.0
-  __TEXT.__text: 0x72fe38
+  __TEXT.__text: 0x7331e0
   __TEXT.__auth_stubs: 0x54a0
-  __TEXT.__objc_methlist: 0x352b0
+  __TEXT.__objc_methlist: 0x35310
   __TEXT.__const: 0x17e00
-  __TEXT.__cstring: 0x8cc20
-  __TEXT.__oslogstring: 0x118080
-  __TEXT.__gcc_except_tab: 0x2ed4
+  __TEXT.__cstring: 0x8ce30
+  __TEXT.__oslogstring: 0x118dce
+  __TEXT.__gcc_except_tab: 0x2ed8
   __TEXT.__ustring: 0x2d4
-  __TEXT.__unwind_info: 0x10a08
+  __TEXT.__unwind_info: 0x10a78
   __TEXT.__objc_classname: 0x4ebf
-  __TEXT.__objc_methname: 0x7c7f6
-  __TEXT.__objc_methtype: 0x27fed
-  __TEXT.__objc_stubs: 0x4d540
+  __TEXT.__objc_methname: 0x7c947
+  __TEXT.__objc_methtype: 0x28023
+  __TEXT.__objc_stubs: 0x4d600
   __DATA_CONST.__got: 0x1650
-  __DATA_CONST.__const: 0x3690
+  __DATA_CONST.__const: 0x3670
   __DATA_CONST.__objc_classlist: 0x12e0
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x490
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x163c0
+  __DATA_CONST.__objc_selrefs: 0x163f8
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10c8
-  __DATA_CONST.__objc_arraydata: 0x25c8
+  __DATA_CONST.__objc_arraydata: 0x25d8
   __AUTH_CONST.__auth_got: 0x2a68
-  __AUTH_CONST.__const: 0x7bc8
-  __AUTH_CONST.__cfstring: 0x25dc0
-  __AUTH_CONST.__objc_const: 0x633f0
+  __AUTH_CONST.__const: 0x7c68
+  __AUTH_CONST.__cfstring: 0x25e20
+  __AUTH_CONST.__objc_const: 0x63480
   __AUTH_CONST.__objc_intobj: 0x44a0
   __AUTH_CONST.__objc_arrayobj: 0x1b00
   __AUTH_CONST.__objc_floatobj: 0x30

   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH.__objc_data: 0xeb0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x6ca0
+  __DATA.__objc_ivar: 0x6cb0
   __DATA.__data: 0x7940
-  __DATA.__bss: 0x948
+  __DATA.__bss: 0x958
   __DATA.__common: 0x9
   __DATA_DIRTY.__objc_data: 0xae10
   __DATA_DIRTY.__data: 0x1f8

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 32118
-  Symbols:   50040
-  CStrings:  51114
+  Functions: 32167
+  Symbols:   50068
+  CStrings:  51175
 
Symbols:
+ +[VCVideoFeatureListStringHelper safeDecompressedFLSFromData:]
+ -[AVConferenceXPCServer stripUnspoofableInboundKeysFromDictionary:]
+ -[LoopbackSocketTunnel dealloc]
+ -[VCAudioRelayIOController updateDirectionForClient:newDirection:]
+ -[VCDatagramChannelIDS idsChannel]
+ -[VCDatagramChannelIDS setIdsChannel:]
+ -[VCMediaAnalyzer dispatchedConfigureCaptureAnalysisSessionForAnalysisType:mediaProperties:resultsHandler:]
+ -[VCNetworkAgent clearMediaInformationAssertionLocked]
+ AppendBinaryBody
+ GCC_except_table106
+ GCC_except_table134
+ GCC_except_table178
+ GCC_except_table180
+ GCC_except_table182
+ GCC_except_table191
+ GCC_except_table196
+ GCC_except_table221
+ GCC_except_table258
+ GCC_except_table88
+ OBJC_IVAR_$_CameraConferenceSynchronizer._blockLock
+ OBJC_IVAR_$_LoopbackSocketTunnel._stop
+ OBJC_IVAR_$_LoopbackSocketTunnel._tid
+ OBJC_IVAR_$_VCDatagramChannelIDS._idsChannelLock
+ VCAudioRedBuilder_GetPrimaryPayloadAndAppendSamples
+ ___49-[VCMediaNegotiator localeWithMediaBlobLanguage:]_block_invoke
+ ___49-[VCMediaNegotiator mediaBlobLanguageWithLocale:]_block_invoke
+ ___50-[VCAudioRelayIOController updateClient:settings:]_block_invoke
+ ___53-[VCVideoCaptureServer getCaptureFrameRateForSource:]_block_invoke_2
+ ___67-[VCMediaAnalyzer configure:forAnalysisType:mediaProperties:error:]_block_invoke
+ ___block_descriptor_352_e8_32o_e5_v8?0l
+ ___block_descriptor_48_e8_32o40r_e517_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBdIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8l
+ ___block_descriptor_72_e8_32o40o48b56r_e5_v8?0l
+ ___copy_helper_block_e8_32o40o48b56r
+ ___destroy_helper_block_e8_32o40o48b56r
+ _objc_msgSend$dispatchedConfigureCaptureAnalysisSessionForAnalysisType:mediaProperties:resultsHandler:
+ _objc_msgSend$idsChannel
+ _objc_msgSend$safeDecompressedFLSFromData:
+ _objc_msgSend$setIdsChannel:
+ _objc_msgSend$stripUnspoofableInboundKeysFromDictionary:
+ _objc_msgSend$updateDirectionForClient:newDirection:
+ localeWithMediaBlobLanguage:.onceToken
+ mediaBlobLanguageWithLocale:.onceToken
- GCC_except_table125
- GCC_except_table126
- GCC_except_table177
- GCC_except_table179
- GCC_except_table181
- GCC_except_table187
- GCC_except_table195
- GCC_except_table220
- GCC_except_table257
- GCC_except_table75
- GCC_except_table86
- GCC_except_table95
- ___block_descriptor_344_e5_v8?0l
- ___block_descriptor_48_e8_32r40r_e517_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBdIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8l
CStrings:
+ " [%s] %s:%d %@(%p) AVCAuditToken decode bad length len=%lu expected=%lu"
+ " [%s] %s:%d %@(%p) AVCAuditToken decode rejected invalid token"
+ " [%s] %s:%d %@(%p) Dictionary endpoints count=%lu exceeds max=%d, rejecting config"
+ " [%s] %s:%d %@(%p) Dropping oversized active-stream update event with %lu active streams (capacity %d)"
+ " [%s] %s:%d %@(%p) XPC endpoints count=%zu exceeds max=%d, rejecting config"
+ " [%s] %s:%d %@(%p) setStreamIDs: rejecting oversized stream-ID list: count=%lu exceeds capacity=%d"
+ " [%s] %s:%d AVCAuditToken decode bad length len=%lu expected=%lu"
+ " [%s] %s:%d AVCAuditToken decode rejected invalid token"
+ " [%s] %s:%d Dictionary endpoints count=%lu exceeds max=%d, rejecting config"
+ " [%s] %s:%d Dropping oversized active-stream update event with %lu active streams (capacity %d)"
+ " [%s] %s:%d Failed to decompress feature list string"
+ " [%s] %s:%d Lost data packet count exceeds capacity, count=%d max=%d"
+ " [%s] %s:%d Received parity packet count exceeds capacity, count=%d max=%d"
+ " [%s] %s:%d XPC endpoints count=%zu exceeds max=%d, rejecting config"
+ " [%s] %s:%d compressedData length=%lu exceeds max=%d"
+ " [%s] %s:%d compressedData=%p length=%lu"
+ " [%s] %s:%d compressedData=%p length=0"
+ " [%s] %s:%d decompressedFLS has invalid prefix"
+ " [%s] %s:%d decompressedFLS length=%lu exceeds max=%d"
+ " [%s] %s:%d decompressedFLS=%p"
+ " [%s] %s:%d double free detected for pool=%p pointer=%p!"
+ " [%s] %s:%d setStreamIDs: rejecting oversized stream-ID list: count=%lu exceeds capacity=%d"
+ "+[VCVideoFeatureListStringHelper safeDecompressedFLSFromData:]"
+ "-[VCAudioTransmitter setStreamIDs:]"
+ "-[VCMediaAnalyzer dispatchedConfigureCaptureAnalysisSessionForAnalysisType:mediaProperties:resultsHandler:]"
+ "-[VCMediaNegotiationBlobV2SettingsU1(Utils) u1Config]"
+ "-[VCMediaStreamConfig extractRemoteEndpointsAndSSRC:]"
+ "-[VideoConference updatedConnectedPeers:]"
+ "-[VideoConference(AudioProcessing) updateMeter:forParticipant:atIndex:]"
+ "B40@0:8q16@24@?32"
+ "Cannot add remote endpoint, max number of remote endpoints reached"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: AppendBinaryBody NULL param"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: AppendBinaryBody failed(%08X)"
+ "SIP [%s] %s:%d /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: AppendBinaryBody overflow [headerLen=%d + bodySize=%d > capacity=%d]"
+ "T@\"IDSDatagramChannel\",N,V_idsChannel"
+ "T@\"NSString\",C,V_lastCalledApiName"
+ "Too many remote endpoints"
+ "VCAudioRedBuilder [%s] %s:%d Discarding RED payload that exceeds max UDP size, bufferSize=%u"
+ "VCVideoStream [%s] %s:%d %@(%p) Cannot add remote endpoint: at max=%d"
+ "VCVideoStream [%s] %s:%d %@(%p) repairStreamIDs count=%lu exceeds max=%d, rejecting config"
+ "VCVideoStream [%s] %s:%d Cannot add remote endpoint: at max=%d"
+ "VCVideoStream [%s] %s:%d repairStreamIDs count=%lu exceeds max=%d, rejecting config"
+ "VideoConference [%s] %s:%d %@(%p) dropped OOB participantIndex=%u max=%zu"
+ "VideoConference [%s] %s:%d %@(%p) rejected oversize newConnectedPeers count=%lu max=%zu"
+ "VideoConference [%s] %s:%d dropped OOB participantIndex=%u max=%zu"
+ "VideoConference [%s] %s:%d rejected oversize newConnectedPeers count=%lu max=%zu"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] FEC parity packet count out of bounds parityPacketsExpected=%d max=%d"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] number of symbols per packet must not be 0"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] parityIndex=%d out of range, startPosition=%d, numberOfSymbolsPerPacket=%d"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] startPosition=%d out of range, numberOfSymbolsPerPacket=%d"
+ "_blockLock"
+ "_idsChannelLock"
+ "_stop"
+ "_tid"
+ "clearMediaInformationAssertionLocked"
+ "dispatchedConfigureCaptureAnalysisSessionForAnalysisType:mediaProperties:resultsHandler:"
+ "en-US"
+ "idsChannel"
+ "safeDecompressedFLSFromData:"
+ "setIdsChannel:"
+ "stripUnspoofableInboundKeysFromDictionary:"
+ "updateDirectionForClient:newDirection:"
+ "{_VCAudioStreamTransportRealtimeContext=\"wrmInfo\"{tagWRMMetricsInfo=\"bInitialized\"B\"hRTPHandle\"^{tagHANDLE}\"dwReportInterval\"I\"dwWrmTime\"I\"dwPlaybackCount\"I\"dwPlaybackCountSpeech\"I\"dwErasureCount\"I\"dwErasureSilence\"I\"videoFrameErasureCount\"I\"dwTimeOfLastRRPacket\"I\"dwEstimatedRTTMilliSeconds\"I\"dwJitter\"I\"dwTotalPacketRecv\"I\"dwDTXPacketRecv\"I\"callId\"Q\"nominalJitterBufferDelay\"Q\"targetJitterQueueSize\"Q\"nFraction\"i\"reportWRMMetricsCallback\"^?\"wrmMetricsReportingContext\"{?=\"info\"^v\"retain\"^?\"release\"^?}\"wrmMetricsReportingLock\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"dwInternalTSRate\"I\"dwPacketSent\"I\"isCallAudioOnly\"I\"bwEstimation\"I\"targetBitrate\"I\"oneWayRelativeDelay\"I\"adaptationPacketLossPercentage\"I\"isLocalCellular\"I\"isVideoPaused\"I\"linkType\"Q\"primaryVideoPacketReceived\"I\"primaryAudioPacketReceived\"I\"totalVideoPacketReceived\"I\"totalAudioPacketReceived\"I\"totalVideoPacketExpected\"I\"totalAudioPacketExpected\"I}\"rtpHandle\"^{tagHANDLE}\"transport\"@\"VCAudioStreamTransport\"}"
- "T@\"NSString\",&,N,V_lastCalledApiName"
- "{_VCAudioStreamTransportRealtimeContext=\"wrmInfo\"{tagWRMMetricsInfo=\"bInitialized\"B\"hRTPHandle\"^{tagHANDLE}\"dwReportInterval\"I\"dwWrmTime\"I\"dwPlaybackCount\"I\"dwPlaybackCountSpeech\"I\"dwErasureCount\"I\"dwErasureSilence\"I\"videoFrameErasureCount\"I\"dwTimeOfLastRRPacket\"I\"dwEstimatedRTTMilliSeconds\"I\"dwJitter\"I\"dwTotalPacketRecv\"I\"dwDTXPacketRecv\"I\"callId\"Q\"nominalJitterBufferDelay\"Q\"targetJitterQueueSize\"Q\"nFraction\"i\"reportWRMMetricsCallback\"^?\"wrmMetricsReportingContext\"{?=\"info\"^v\"retain\"^?\"release\"^?}\"wrmMetricsReportingLock\"{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}\"dwInternalTSRate\"I\"dwPacketSent\"I\"isCallAudioOnly\"I\"bwEstimation\"I\"targetBitrate\"I\"oneWayRelativeDelay\"I\"adaptationPacketLossPercentage\"I\"isLocalCellular\"I\"isVideoPaused\"I\"linkType\"Q\"primaryVideoPacketReceived\"I\"primaryAudioPacketReceived\"I\"totalVideoPacketReceived\"I\"totalAudioPacketReceived\"I\"totalVideoPacketExpected\"I\"totalAudioPacketExpected\"I}\"rtpHandle\"^{tagHANDLE}}"
```
