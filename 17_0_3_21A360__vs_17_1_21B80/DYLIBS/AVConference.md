## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-1965.73.1.6.0
-  __TEXT.__text: 0x6320b0
+2000.8.1.1.1
+  __TEXT.__text: 0x633550
   __TEXT.__auth_stubs: 0x4c40
-  __TEXT.__objc_methlist: 0x2aacc
-  __TEXT.__const: 0x7928
-  __TEXT.__cstring: 0x74457
-  __TEXT.__oslogstring: 0xd8f93
+  __TEXT.__objc_methlist: 0x2ab1c
+  __TEXT.__const: 0x7968
+  __TEXT.__cstring: 0x74625
+  __TEXT.__oslogstring: 0xd93a4
   __TEXT.__gcc_except_tab: 0x1f84
-  __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0xc61c
+  __TEXT.__ustring: 0x144
+  __TEXT.__unwind_info: 0xc64c
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_classname: 0x42d9
-  __TEXT.__objc_methname: 0x69076
-  __TEXT.__objc_methtype: 0x20d43
-  __TEXT.__objc_stubs: 0x428a0
-  __DATA_CONST.__got: 0x1100
-  __DATA_CONST.__const: 0x5948
+  __TEXT.__objc_methname: 0x6916a
+  __TEXT.__objc_methtype: 0x20e62
+  __TEXT.__objc_stubs: 0x42960
+  __DATA_CONST.__got: 0x1110
+  __DATA_CONST.__const: 0x5970
   __DATA_CONST.__objc_classlist: 0x1088
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x408
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x4ef10
-  __DATA_CONST.__objc_selrefs: 0x13180
+  __DATA_CONST.__objc_const: 0x4efc0
+  __DATA_CONST.__objc_selrefs: 0x131a8
   __DATA_CONST.__objc_arraydata: 0x1e38
-  __AUTH_CONST.__cfstring: 0x1f580
+  __AUTH_CONST.__cfstring: 0x1f620
   __AUTH_CONST.__objc_intobj: 0x39d8
   __AUTH_CONST.__objc_arrayobj: 0x14e8
   __AUTH_CONST.__objc_const: 0x0
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x150
-  __AUTH_CONST.__const: 0x2f8
+  __AUTH_CONST.__const: 0x358
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__auth_got: 0x2638
   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x1208
   __DATA.__objc_superrefs: 0xee8
-  __DATA.__objc_ivar: 0x5d4c
-  __DATA.__data: 0x6f90
+  __DATA.__objc_ivar: 0x5d58
+  __DATA.__data: 0x6f98
   __DATA.__bss: 0xa20
   __DATA.__common: 0x55
-  __DATA_DIRTY.__const: 0x2d58
+  __DATA_DIRTY.__const: 0x2cf8
   __DATA_DIRTY.__objc_const: 0xc980
   __DATA_DIRTY.__objc_data: 0xa550
   __DATA_DIRTY.__data: 0x150

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 33E45071-6B56-31D0-A1B7-0D6748F7240E
-  Functions: 28009
-  Symbols:   78746
-  CStrings:  47770
+  UUID: BBC1FF10-7831-31CA-8C11-2242EC92F2F8
+  Functions: 28027
+  Symbols:   78794
+  CStrings:  47805
 
Symbols:
+ +[LogDumpUtility setFileOwnership:owner:]
+ +[VCWiFiUtils getInfraChannelNumber:is5Ghz:isPresent:]
+ -[VCAudioStream overlayToken]
+ -[VCAudioStream setOverlayToken:]
+ -[VCControlChannelDialog handshakeOperationQueue]
+ -[VCMediaStreamGroup mediaStream:didReceiveFlushRequestWithPayloads:]
+ -[VCSession vcSessionParticipantDidMediaReceiveFlushRequestWithPayloads:]
+ -[VCSession vcSessionParticipantDidMediaReceiveFlushRequestWithPayloads:].cold.1
+ -[VCSessionParticipant streamGroup:didReceiveFlushRequestWithPayloads:]
+ GCC_except_table137
+ _NSFileGroupOwnerAccountName
+ _NSFileOwnerAccountName
+ _OBJC_IVAR_$_VCAudioStream._overlayToken
+ _OBJC_IVAR_$_VCConnectionManager._overlayDetails
+ _OBJC_IVAR_$_VCSessionStatsController._statsRequestQueue
+ _VCAudioReceiver_SetOverlayToken
+ _VCAudioReceiver_SetOverlayToken.cold.1
+ _VCAudioStreamGroup_OverlayToken
+ _VCOverlaySourceTextHelper_appendAudioTextToString
+ _VCOverlaySourceTextHelper_appendAudioTextToString.cold.1
+ _VCOverlaySourceTextHelper_appendAudioTextToString.cold.2
+ __OBJC_$_PROP_LIST_VCVideoCaptureServer.695
+ __VCAudioReceiver_UpdateAudioOverlayStats
+ __VCConnectionManager_SetOverlayLinkDetails
+ __VCOverlaySourceTextHelper_appendLowVerbosityAudioTextToString
+ ___36-[VCVideoCaptureServer pausePreview]_block_invoke.308
+ ___48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.274
+ ___48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.278
+ ___49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.280
+ ___49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.284
+ ___49-[VCVideoCaptureServer sourceFrameRateDidChange:]_block_invoke.333
+ ___51-[VCVideoCaptureServer handleAVCaptureError:error:]_block_invoke.146
+ ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.171
+ ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.180
+ ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.193
+ ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.205
+ ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke_2.196
+ ___69-[VCMediaStreamGroup mediaStream:didReceiveFlushRequestWithPayloads:]_block_invoke
+ ___71-[VCSessionParticipant streamGroup:didReceiveFlushRequestWithPayloads:]_block_invoke
+ ___VCVideoCaptureServer_ApplyPressureLevelChanges_block_invoke.220
+ ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.706
+ ____VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.708
+ ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.700
+ ___block_descriptor_48_e8_32o40o_e38_v16?0"<VCMediaStreamGroupDelegate>"8ls32l8s40l8
+ ___block_descriptor_tmp.354
+ ___block_descriptor_tmp.400
+ ___block_descriptor_tmp.402
+ ___block_descriptor_tmp.61
+ ___block_literal_global.14
+ ___block_literal_global.312
+ ___block_literal_global.52
+ ___block_literal_global.54
+ _objc_msgSend$additionalFlushCountToOneToOneRateController:
+ _objc_msgSend$getInfraChannelNumber:is5Ghz:isPresent:
+ _objc_msgSend$setAttributes:ofItemAtPath:error:
+ _objc_msgSend$setFileOwnership:owner:
+ _objc_msgSend$streamGroup:didReceiveFlushRequestWithPayloads:
+ _objc_msgSend$stringByDeletingPathExtension
+ _objc_msgSend$vcSessionParticipantDidMediaReceiveFlushRequestWithPayloads:
- -[VCConnectionManager updateOverlaySource:isRemoteOnCellular:isRelay:]
- -[VCEmulatedNetworkQueue dequeuePacket:time:].cold.2
- -[VCImageQueue resetSlotForCALayerHostModeSwitch]
- GCC_except_table136
- GCC_except_table19
- __OBJC_$_PROP_LIST_VCVideoCaptureServer.692
- ___36-[VCVideoCaptureServer pausePreview]_block_invoke.305
- ___48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.271
- ___48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.275
- ___49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.277
- ___49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.281
- ___49-[VCVideoCaptureServer sourceFrameRateDidChange:]_block_invoke.330
- ___51-[VCVideoCaptureServer handleAVCaptureError:error:]_block_invoke.143
- ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.168
- ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.177
- ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.190
- ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke.202
- ___51-[VCVideoCaptureServer handleCaptureEvent:subType:]_block_invoke_2.193
- ___VCVideoCaptureServer_ApplyPressureLevelChanges_block_invoke.217
- ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.703
- ____VCVideoCaptureServer_ProcessFrameSizeChange_block_invoke.705
- ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.697
- ___block_descriptor_tmp.355
- ___block_descriptor_tmp.401
- ___block_descriptor_tmp.403
- ___block_descriptor_tmp.62
- ___block_literal_global.13
- ___block_literal_global.309
- ___block_literal_global.49
- _objc_msgSend$updateOverlaySource:isRemoteOnCellular:isRelay:
CStrings:
+ "\n\n\n"
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: read failed with error=%d"
+ " [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: write failed with error=%d"
+ " [%s] %s:%d Cannot add media packet=%p to VCMediaQueue!"
+ " [%s] %s:%d Control info inUseCounter increment failed for packet=%pand controlInfo=%p"
+ " [%s] %s:%d Could not decrement controlInfo inUseCounter for packet=%p when VCMQ and RTX failed to add packet"
+ " [%s] %s:%d Could not decrement controlInfo inUseCounter for packet=%pafter retaining it in VCMQ and RTX for controlInfo=%p"
+ " [%s] %s:%d Could not decrement controlInfo inUseCounter formediaPacketHistory=%p, with metadata=%p"
+ " [%s] %s:%d Could not update media packet history for packet=%pfor nackConsumer=%p"
+ " [%s] %s:%d Failed to change file attributes of file=%@, error=%@"
+ " [%s] %s:%d Incrementing counter for control info failed formediaPacketHistory=%p, metadata=%p, and ControlInfo=%p with seqNumHash=%d"
+ " [%s] %s:%d PacketCountInQueue is bad, size=%d, isLost=%d, seq=%u "
+ " [%s] %s:%d [VCOverlayManager] No displayString was found while appending audio text"
+ " [%s] %s:%d [VCOverlayManager] No textContext was found while appending audio text"
+ " [%s] %s:%d mediaPacketHistory retrieval failed for rtpInfo=%p with seqNumHash=%d"
+ " [%s] %s:%d sendUnreliableMessage: send message with transactionID=%@, size=%lu to remote participant=%@ which is part of session=%d"
+ "%sActive - %c:%c:%c%s\n"
+ "%sSample Rate: %d\n%sSample Count: %0.2f\n%sRed Level: %d\n%sCodec Payload: %d\n%sMediaStall Count: %d\n%sMediaStall Time: %0.2f"
+ "+[LogDumpUtility setFileOwnership:owner:]"
+ "-[VCSession vcSessionParticipantDidMediaReceiveFlushRequestWithPayloads:]"
+ "2000.8.1.1.1"
+ ":D"
+ "B40@0:8^i16^B24^B32"
+ "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BBq^{tagVCOverlaySource}},R,VaudioReceiver"
+ "VCAudioReceiver_SetOverlayToken"
+ "VCOverlaySourceTextHelper_appendAudioTextToString"
+ "VCSession [%s] %s:%d Flush baseband failed for payloads=%@"
+ "VideoHardwareTestCaptureFormatIsHDR"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BBq^{tagVCOverlaySource}}"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BBq^{tagVCOverlaySource}}16@0:8"
+ "_RTPTransportRetrieveMediaPacketHistory"
+ "_overlayDetails"
+ "_statsRequestQueue"
+ "com.apple.AVConference.vcsessionStatsController.requestQueue"
+ "getInfraChannelNumber:is5Ghz:isPresent:"
+ "handshakeOperationQueue"
+ "mobile"
+ "participant-%s-groupid_%s-VideoReceiver"
+ "setAttributes:ofItemAtPath:error:"
+ "setFileOwnership:owner:"
+ "streamGroup:didReceiveFlushRequestWithPayloads:"
+ "stringByDeletingPathExtension"
+ "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}B}16"
+ "v32@0:8@\"VCMediaStreamGroup\"16@\"NSArray\"24"
+ "vcSessionParticipantDidMediaReceiveFlushRequestWithPayloads:"
+ "videoCannedReplay"
+ "{tagVCOverlayInfoNetwork=\"primaryLocalIsOnCell\"B\"primaryRemoteIsOnCell\"B\"primaryIsRelay\"B\"isDuplicating\"B\"duplicatingLocalIsOnCell\"B\"duplicatingRemoteIsOnCell\"B\"duplicatingIsRelay\"B}"
- "\n\n"
- " [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: read failed"
- " [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/GKNATObserver.m:%d: callHTTPTestFromIPPort: write failed"
- " [%s] %s:%d Cannot add media packet to VCMediaQueue!"
- " [%s] %s:%d Could not update media packet history!"
- " [%s] %s:%d PacketCountInQueue is bad, size:%d"
- " [%s] %s:%d sendUnreliableMessage: send message to remote participant '%@' which is part of session '%d'"
- "%s(streamID: %d)\n%s%dx%d (VRA: %dx%d)\n%sFPS: %.01f\n"
- "%sL:%s, R:%s - Dup:%s over %s\n"
- "1965.73.1.6"
- "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}qB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB},R,VaudioReceiver"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}qB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB}"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}qB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB}16@0:8"
- "resetSlotForCALayerHostModeSwitch"
- "updateOverlaySource:isRemoteOnCellular:isRelay:"
- "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}qB}16"
- "vrdump"

```
