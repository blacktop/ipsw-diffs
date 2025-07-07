## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2145.50.1.0.0
-  __TEXT.__text: 0x78bd88
+2145.53.2.0.0
+  __TEXT.__text: 0x78ec44
   __TEXT.__auth_stubs: 0x55f0
-  __TEXT.__objc_methlist: 0x356d0
-  __TEXT.__const: 0xc730
-  __TEXT.__cstring: 0x8e250
-  __TEXT.__oslogstring: 0x10ca8f
-  __TEXT.__gcc_except_tab: 0x2a80
+  __TEXT.__objc_methlist: 0x35748
+  __TEXT.__const: 0xc770
+  __TEXT.__cstring: 0x8e661
+  __TEXT.__oslogstring: 0x10ddef
+  __TEXT.__gcc_except_tab: 0x2adc
   __TEXT.__ustring: 0x1a8
-  __TEXT.__unwind_info: 0x106a8
+  __TEXT.__unwind_info: 0x107a8
   __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7d10d
-  __TEXT.__objc_methtype: 0x2816a
-  __TEXT.__objc_stubs: 0x4e640
-  __DATA_CONST.__got: 0x1a40
-  __DATA_CONST.__const: 0x69b8
+  __TEXT.__objc_methname: 0x7d221
+  __TEXT.__objc_methtype: 0x281fc
+  __TEXT.__objc_stubs: 0x4e720
+  __DATA_CONST.__got: 0x1a30
+  __DATA_CONST.__const: 0x6a08
   __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x167e0
+  __DATA_CONST.__objc_selrefs: 0x16820
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
   __AUTH_CONST.__auth_got: 0x2b10
   __AUTH_CONST.__const: 0x3bc8
-  __AUTH_CONST.__cfstring: 0x25e00
-  __AUTH_CONST.__objc_const: 0x62f68
+  __AUTH_CONST.__cfstring: 0x25f60
+  __AUTH_CONST.__objc_const: 0x62fc8
   __AUTH_CONST.__objc_intobj: 0x4968
   __AUTH_CONST.__objc_arrayobj: 0x1b30
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0x6bd8
+  __DATA.__objc_ivar: 0x6be4
   __DATA.__data: 0x7870
   __DATA.__bss: 0xd80
   __DATA.__common: 0x55

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: E06201C6-A294-3DD4-8883-ED8FB0B5766A
-  Functions: 31444
-  Symbols:   96993
-  CStrings:  56855
+  UUID: 51E3C80D-0014-33B9-BAB4-2A97670499F1
+  Functions: 31457
+  Symbols:   97051
+  CStrings:  56984
 
Symbols:
+ +[VCAudioIO stringForAudioType:]
+ +[VCAudioIO stringForAudioType:].cold.1
+ +[VCAudioIO terminateProcess:terminateSource:]
+ +[VCAudioSession stringForPlaybackMode:]
+ +[VCAudioSession stringForPlaybackMode:].cold.1
+ -[AVCSessionParticipant copyStateQueue]
+ -[AVCSessionParticipant isStateQueueSet]
+ -[AVCSessionParticipant setPropertyValue:forPropertyName:xpcKey:xpcMessageName:batchSupported:]
+ -[VCAudioInjector parseMediaTracksForAsset:].cold.9
+ -[VCAudioStream initWithClientPid:ssrc:transportSessionID:streamToken:experimentManager:logPrefix:]
+ -[VCMediaStream initWithTransportSessionID:localSSRC:streamToken:logPrefix:]
+ -[VCMediaStreamGroup startMediaStreams].cold.1
+ -[VCScreenCaptureManager startScreenShare:].cold.1
+ -[VCScreenCaptureManager stopScreenShare:].cold.1
+ -[VCScreenCaptureManager updateScreenCapture:withConfig:].cold.1
+ -[VCSession reportInitialThermalLevel]
+ -[VCVideoCaptureServer updateScreenCapture:withConfig:].cold.1
+ -[VCVideoStream initWithTransportSessionID:idsParticipantID:ssrc:streamToken:logPrefix:]
+ -[VCVideoTransmitterConfig logPrefix]
+ -[VCVideoTransmitterConfig setLogPrefix:]
+ GCC_except_table106
+ GCC_except_table110
+ GCC_except_table159
+ GCC_except_table161
+ GCC_except_table57
+ GCC_except_table60
+ GCC_except_table61
+ _OBJC_IVAR_$_AVCSessionParticipant._isLocal
+ _OBJC_IVAR_$_VCVideoTransmitterConfig._logPrefix
+ _OBJC_IVAR_$_VCVideoTransmitterDefault._logPrefix
+ _VCAudioBufferList_Allocate.cold.3
+ ___135-[VideoConference(SessionDelegate) session:receivedRemoteFrame:atTime:withScreenAttributes:videoAttributes:isFirstFrame:isVideoPaused:]_block_invoke.649
+ ___35-[VCVideoStream updateVideoConfig:]_block_invoke.192
+ ___36-[VCVideoStream setupReportingAgent]_block_invoke.261
+ ___43-[AVAudioClient setAudioSessionProperties:]_block_invoke.48
+ ___53-[VCSessionParticipantRemote setOneToOneModeEnabled:]_block_invoke.177
+ ___55-[AVAudioClient registerBlocksForDelegateNotifications]_block_invoke.107
+ ___55-[VCSessionParticipantRemote createAndResumeFetchTimer]_block_invoke.179
+ ___59-[VCVideoStream newSensitiveContentAnalyzerForParticipant:]_block_invoke.cold.4
+ ___60-[VCSessionParticipantRemote updateRemoteDeviceOrientation:]_block_invoke.180
+ ___64-[VCVideoStream newVideoTransmitterConfigWithVideoStreamConfig:]_block_invoke.18
+ ___71-[VCVideoCaptureServer newSensitiveContentAnalyzerWithParticipantUUID:]_block_invoke.cold.4
+ ___95-[AVCSessionParticipant setPropertyValue:forPropertyName:xpcKey:xpcMessageName:batchSupported:]_block_invoke
+ ____VCAnsweringMachine_DispatchFinishAnnouncementNotice_block_invoke.240
+ ___block_descriptor_tmp.234
+ ___block_descriptor_tmp.275
+ ___block_descriptor_tmp.287
+ ___block_descriptor_tmp.482
+ ___block_descriptor_tmp.546
+ ___block_descriptor_tmp.548
+ _objc_msgSend$initWithClientPid:ssrc:transportSessionID:streamToken:experimentManager:logPrefix:
+ _objc_msgSend$initWithTransportSessionID:idsParticipantID:ssrc:streamToken:logPrefix:
+ _objc_msgSend$initWithTransportSessionID:localSSRC:streamToken:logPrefix:
+ _objc_msgSend$initializeDisplayLinkWithError:
+ _objc_msgSend$isStateQueueSet
+ _objc_msgSend$reportInitialThermalLevel
+ _objc_msgSend$setPropertyValue:forPropertyName:xpcKey:xpcMessageName:batchSupported:
+ _objc_msgSend$stringForAudioType:
+ _objc_msgSend$stringForPlaybackMode:
+ _objc_msgSend$terminateProcess:terminateSource:
- -[AVCSessionParticipant setPropertyValue:forPropertyName:xpcKey:xpcMessageName:]
- -[VCAudioStream initWithClientPid:ssrc:transportSessionID:streamToken:experimentManager:]
- GCC_except_table105
- GCC_except_table109
- _VCAudioBufferList_CreateSampleBufferAllocateWithAllocator.cold.1
- __RTCPTransport_ParsePacket.cold.14
- __VideoTransmitter_CreateEncodingBufferAndSetOrientation.cold.1
- __VideoTransmitter_CreateRotatedPixelBufferForTallFormatCameraCapture.cold.1
- __VideoTransmitter_CreateRotatedPixelBufferForTallFormatCameraCapture.cold.2
- __VideoTransmitter_EncodeSingleImageVideo.cold.1
- __VideoTransmitter_EncodeSingleImageVideo.cold.2
- __VideoTransmitter_EncodeSingleImageVideo.cold.3
- ___135-[VideoConference(SessionDelegate) session:receivedRemoteFrame:atTime:withScreenAttributes:videoAttributes:isFirstFrame:isVideoPaused:]_block_invoke.646
- ___35-[VCVideoStream updateVideoConfig:]_block_invoke.188
- ___36-[VCVideoStream setupReportingAgent]_block_invoke.257
- ___43-[AVAudioClient setAudioSessionProperties:]_block_invoke_2
- ___50-[VCScreenCaptureManager registerBlocksForService]_block_invoke.cold.3
- ___53-[VCSessionParticipantRemote setOneToOneModeEnabled:]_block_invoke.174
- ___55-[AVAudioClient registerBlocksForDelegateNotifications]_block_invoke.106
- ___55-[VCSessionParticipantRemote createAndResumeFetchTimer]_block_invoke.176
- ___60-[VCSessionParticipantRemote updateRemoteDeviceOrientation:]_block_invoke.177
- ___64-[VCVideoStream newVideoTransmitterConfigWithVideoStreamConfig:]_block_invoke.14
- ___80-[AVCSessionParticipant setPropertyValue:forPropertyName:xpcKey:xpcMessageName:]_block_invoke
- ____VCAnsweringMachine_DispatchFinishAnnouncementNotice_block_invoke.237
- ___block_descriptor_tmp.240
- ___block_descriptor_tmp.281
- ___block_descriptor_tmp.293
- ___block_descriptor_tmp.479
- ___block_descriptor_tmp.542
- ___block_descriptor_tmp.544
- _objc_msgSend$initWithClientPid:ssrc:transportSessionID:streamToken:experimentManager:
- _objc_msgSend$setPropertyValue:forPropertyName:xpcKey:xpcMessageName:
- _objc_msgSend$stateQueue
CStrings:
+ " [%s] %s:%d %@(%p) Creating %s converter buffer with capacity=%u"
+ " [%s] %s:%d %@(%p) Failed to load the samples. result=%x"
+ " [%s] %s:%d %@(%p) Insufficient %s converter buffer capacity: %u < %u, releasing"
+ " [%s] %s:%d %@(%p) No delegate context"
+ " [%s] %s:%d %@(%p) SCVideoStreamAnalyzer begin succeeded for capture device input=%@"
+ " [%s] %s:%d %@(%p) SCVideoStreamAnalyzer endAnalysis"
+ " [%s] %s:%d %@(%p) Starting: %@"
+ " [%s] %s:%d %@(%p) Stopping: %@"
+ " [%s] %s:%d %@(%p) Update operation returned error=%@"
+ " [%s] %s:%d %@(%p) Updating: %@"
+ " [%s] %s:%d %@(%p) operatingMode=%d, audioType=%d"
+ " [%s] %s:%d @:@ AVCSession-initPrivateWithTransportToken (%p) transportToken[%@]"
+ " [%s] %s:%d @:@ VCAudioClient-init %p"
+ " [%s] %s:%d @:@ VCAudioIO-didStart (%p) Stream successfully started"
+ " [%s] %s:%d @:@ VCAudioIO-init (%p) %@"
+ " [%s] %s:%d @:@ VCAudioIO-startWithCompletionHandler (%p) Starting... audioController=%@, controllerClient=%@, delegate=%@ type=%d (%@)"
+ " [%s] %s:%d @:@ VCAudioManager-startAUIOWithProperties (%p) %@ AVAudioSession:[%u] Starting AUIO operatingMode[%d] deviceRole[%d] remoteCodecType[%s] remoteCodecRate[%f] isMicrophoneMuted[%d]"
+ " [%s] %s:%d @:@ VCAudioManager-startAUIOWithProperties (%p) %@ startAudioIO is completed"
+ " [%s] %s:%d @:@ VCAudioSession-startedClient (%p) Client:%p success=%d"
+ " [%s] %s:%d @:@ VCAudioSession-startingClient (%p) Client:%p playbackMode=%d (%@)"
+ " [%s] %s:%d @:@ VCAudioSessionAVAS-startSessionWithMediaProperties (%p) Created AVAudioSession=%p audioSessionID=%u"
+ " [%s] %s:%d @:@ VCAudioSessionAVAS-started (%p) AVAudioSession=%@ setActive=YES completed"
+ " [%s] %s:%d @:@ VCAudioSessionAVAS-starting (%p) audioSession=%@"
+ " [%s] %s:%d @:@ VCAudioSessionCMS-started (%p) VCCMSessionStub_CMSessionBeginInterruption result=%d"
+ " [%s] %s:%d @:@ VCAudioSessionCMS-starting (%p)"
+ " [%s] %s:%d @:@ VCConnectionManagerIDS-addConnection (%p)"
+ " [%s] %s:%d @:@ VCMediaStreamGroup-initialized (%p) %@"
+ " [%s] %s:%d @:@ VCMediaStreamGroup-startMediaStreams (%p) %@ Starting group. groupEntries=%@"
+ " [%s] %s:%d @:@ VCSession-startOneToOne (%p)"
+ " [%s] %s:%d @:@ VCSessionParticipant-startStreamGroups (%p) %@ Starting stream group. streamGroupID=%s, streamToken=%u"
+ " [%s] %s:%d @:@ VCSessionParticipantLocal-handleActiveConnectionChange (%p) %@ Active connection changed with new connection uplinkBitrateCap %d"
+ " [%s] %s:%d @:@ VCSessionParticipantLocal-initialized (%p) Participant init %@"
+ " [%s] %s:%d @:@ VCSystemAudioCaptureSession-initialized (%p) %@"
+ " [%s] %s:%d @:@ VCVideoStreamReceiver-initialized (%p) %s"
+ " [%s] %s:%d @:@ VCVideoTransmitterBase-initialized (%p) %@ capture = %dx%d, encode = %dx%d"
+ " [%s] %s:%d @:@ VCVideoTransmitterDefault-initialized (%p) %@"
+ " [%s] %s:%d @:@ VCVideoTransmitterDefault-startVideo (%p) %@"
+ " [%s] %s:%d @:@ VideoTransmitter-CreateHandle (%p) %s handle=0x%x"
+ " [%s] %s:%d @:@ VideoTransmitter-PacketizeAndTransmitEncodedVideoFrame (%p) Transmitting first key frame"
+ " [%s] %s:%d Creating %s converter buffer with capacity=%u"
+ " [%s] %s:%d Failed to allocate audio format description"
+ " [%s] %s:%d Failed to load the samples. result=%x"
+ " [%s] %s:%d Insufficient %s converter buffer capacity: %u < %u, releasing"
+ " [%s] %s:%d No delegate context"
+ " [%s] %s:%d SCVideoStreamAnalyzer begin succeeded for capture device input=%@"
+ " [%s] %s:%d SCVideoStreamAnalyzer endAnalysis"
+ " [%s] %s:%d Starting: %@"
+ " [%s] %s:%d Stopping: %@"
+ " [%s] %s:%d Unknown audio type=%d"
+ " [%s] %s:%d Unknown playbackMode=%d"
+ " [%s] %s:%d Update operation returned error=%@"
+ " [%s] %s:%d Updating: %@"
+ " [%s] %s:%d [%p] SCVideoStreamAnalyzer begin succeeded for decompressionSession=%p"
+ " [%s] %s:%d [%p] SCVideoStreamAnalyzer endAnalysis"
+ " [%s] %s:%d operatingMode=%d, audioType=%d"
+ "+[VCAudioIO stringForAudioType:]"
+ "+[VCAudioSession stringForPlaybackMode:]"
+ "-[AVAudioClient setAudioSessionProperties:]_block_invoke"
+ "-[AVCSessionParticipant setPropertyValue:forPropertyName:xpcKey:xpcMessageName:batchSupported:]"
+ "-[AVCSessionParticipant setPropertyValue:forPropertyName:xpcKey:xpcMessageName:batchSupported:]_block_invoke"
+ "-[VCAVFoundationCapture endSensitiveContentAnalysis]"
+ "-[VCAudioClient initWithProcessId:]"
+ "-[VCAudioIO dealloc]"
+ "-[VCAudioIO destroyBuffers]"
+ "-[VCScreenCaptureManager startScreenShare:]"
+ "-[VCScreenCaptureManager stopScreenShare:]"
+ "-[VCScreenCaptureManager updateScreenCapture:withConfig:]"
+ "-[VCVideoCaptureServer endSensitiveContentAnalysis]_block_invoke"
+ "-[VCVideoCaptureServer endSensitiveContentAnalyzerInterruption]_block_invoke"
+ "-[VCVideoCaptureServer startScreenShareCapture:]"
+ "-[VCVideoCaptureServer stopScreenShareCapture:]"
+ "-[VCVideoCaptureServer updateScreenCapture:withConfig:]"
+ "-[VCVideoStream initWithTransportSessionID:idsParticipantID:ssrc:streamToken:logPrefix:]"
+ "2145.53.2"
+ "@24@0:8^{?=i{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}iiIi@}16"
+ "@24@0:8^{tagVCVideoStreamReceiverConfig=^{tagHANDLE}@{tagVCVideoReceiverDelegateRealtimeInstanceVTable=^?^?}^{opaqueRTCReporting}Ii@B^v^?@[30c]}16"
+ "@24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}16"
+ "@40@0:8I16I20q24@32"
+ "@48@0:8I16Q20I28q32@40"
+ "@52@0:8i16I20I24q28@36@44"
+ "@72@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?[30c]}16@24r^{tagVCVideoReceiverDelegateRealtimeInstanceVTable=^?^?}32^{opaqueRTCReporting=}40@48^{tagHANDLE=i}56@64"
+ "@:@ AUIOCreateHandle"
+ "@:@ AUIOStart-AudioUnitStarted"
+ "@:@ AUIOStart-AudioUnitStarting"
+ "@:@ AVAudioClient-initializeAudioSession"
+ "@:@ AVAudioClient-startAudioSessionWithCompletionHandler"
+ "@:@ AVCSession-initPrivateWithTransportToken"
+ "@:@ VCAudioClient-init"
+ "@:@ VCAudioIO-didStart"
+ "@:@ VCAudioIO-init"
+ "@:@ VCAudioIO-startWithCompletionHandler"
+ "@:@ VCAudioManager-startAUIOWithProperties"
+ "@:@ VCAudioSession-startedClient"
+ "@:@ VCAudioSession-startingClient"
+ "@:@ VCAudioSessionAVAS-startSessionWithMediaProperties"
+ "@:@ VCAudioSessionAVAS-started"
+ "@:@ VCAudioSessionAVAS-starting"
+ "@:@ VCAudioSessionCMS-started"
+ "@:@ VCAudioSessionCMS-starting"
+ "@:@ VCConnectionManagerIDS-addConnection"
+ "@:@ VCMediaStream-handleEncryptionInfoChange"
+ "@:@ VCMediaStream-setup"
+ "@:@ VCMediaStreamGroup-initialized"
+ "@:@ VCMediaStreamGroup-startMediaStreams"
+ "@:@ VCSession-dispatchedAddParticipantWithConfig"
+ "@:@ VCSession-handleActiveConnectionChange"
+ "@:@ VCSession-startOneToOne"
+ "@:@ VCSessionParticipant-startStreamGroups"
+ "@:@ VCSessionParticipantLocal-handleActiveConnectionChange"
+ "@:@ VCSessionParticipantLocal-initialized"
+ "@:@ VCSessionParticipantRemote-initialized"
+ "@:@ VCSystemAudioCaptureSession-initialized"
+ "@:@ VCVideoStream-DidReceiveRemoteFrame"
+ "@:@ VCVideoStream-DidReceiveSampleBuffer"
+ "@:@ VCVideoStream-initialized"
+ "@:@ VCVideoStreamReceiver-initialized"
+ "@:@ VCVideoTransmitterBase-initialized"
+ "@:@ VCVideoTransmitterDefault-initialized"
+ "@:@ VCVideoTransmitterDefault-startVideo"
+ "@:@ VideoPacketBuffer-create"
+ "@:@ VideoPacketBuffer-created"
+ "@:@ VideoReceiver-CreateHandle"
+ "@:@ VideoTransmitter-CreateHandle"
+ "@:@ VideoTransmitter-PacketizeAndTransmitEncodedVideoFrame"
+ "AUIO [%s] %s:%d @:@ AUIOCreateHandle (%p) Successfully created the AUIO handle=%p"
+ "AUIO [%s] %s:%d @:@ AUIOCreateHandle (%p) audioIOType=%d"
+ "AUIO [%s] %s:%d @:@ AUIOStart-AudioUnitStarted AUIO=%p AudioOutputUnitStart() completed"
+ "AUIO [%s] %s:%d @:@ AUIOStart-AudioUnitStarting AUIO=%p AUIO Starting..."
+ "AVCAudioClient [%s] %s:%d @:@ AVAudioClient-initializeAudioSession (%p)"
+ "AVCAudioClient [%s] %s:%d @:@ AVAudioClient-setAudioSessionProperties (%p)"
+ "AVCAudioClient [%s] %s:%d @:@ AVAudioClient-startAudioSessionWithCompletionHandler (%p) %s startAudioSession call from client. processId=%d"
+ "B24@0:8^{?=i{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}iiIi@}16"
+ "B24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}16"
+ "Starting screen capture with screenShareDict=%s"
+ "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}},R,VaudioReceiver"
+ "T{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?[30c]},V_videoReceiverConfig"
+ "Updating screen capture with screenShareDict=%s"
+ "VCAudioIOAudioTypeCellularDownlink"
+ "VCAudioIOAudioTypeCellularUplink"
+ "VCAudioIOAudioTypeNull"
+ "VCAudioIOAudioTypeSiri"
+ "VCAudioIOAudioTypeSystem"
+ "VCAudioIOAudioTypeSystemHALPlugin"
+ "VCAudioIOAudioTypeVoice"
+ "VCAudioReceiver [%s] %s:%d @=@ Health: VCAudioReceiver ParticipantID=%s erasure percentage=%.2f%% PLR percentage=%.2f%% current percentage:%.2f%% (rec:%u exp:%u, loss:%u) receiver(rtp=%u, bb=%u, unk=%u, dup=%u, drop=%u) jb(enc=%u, drop=%u)"
+ "VCAudioSessionPlaybackModeSystemAudioInput"
+ "VCAudioSessionPlaybackModeSystemAudioOutput"
+ "VCAudioSessionPlaybackModeVoiceChat"
+ "VCMediaStream [%s] %s:%d @:@ VCMediaStream-handleEncryptionInfoChange (%p) %@"
+ "VCMediaStream [%s] %s:%d @:@ VCMediaStream-setup (%p) %@"
+ "VCSession [%s] %s:%d @:@ VCSession-dispatchedAddParticipantWithConfig Adding participant[%s]"
+ "VCSession [%s] %s:%d @:@ VCSession-handleActiveConnectionChange (%p) Connection changed to '%@'"
+ "VCSessionParticipantRemote [%s] %s:%d @:@ VCSessionParticipantRemote-initialized (%p) Participant init %@"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) SCVideoStreamAnalyzer continueStream"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) SCVideoStreamAnalyzer created for participant=%@"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) SCVideoStreamAnalyzer released"
+ "VCVideoCaptureServer [%s] %s:%d SCVideoStreamAnalyzer continueStream"
+ "VCVideoCaptureServer [%s] %s:%d SCVideoStreamAnalyzer created for participant=%@"
+ "VCVideoCaptureServer [%s] %s:%d SCVideoStreamAnalyzer released"
+ "VCVideoCaptureServer [%s] %s:%d Stopping screen capture for captureSourceID=%ld"
+ "VCVideoCaptureServer [%s] %s:%d didStart=%d"
+ "VCVideoCaptureServer [%s] %s:%d updateScreenCapture failed, error=%@"
+ "VCVideoStream [%s] %s:%d %@(%p) SCVideoStreamAnalyzer created for participant=%@"
+ "VCVideoStream [%s] %s:%d @:@ VCVideoStream-DidReceiveRemoteFrame (%p) receiver[%p] received first remote frame frameTime=%f"
+ "VCVideoStream [%s] %s:%d @:@ VCVideoStream-DidReceiveSampleBuffer VCVideoStream[%p] received first remote frame"
+ "VCVideoStream [%s] %s:%d @:@ VCVideoStream-initialized VCVideoStream[%p] init %@ queue=%p for idsParticipantID=%llu streamToken=%u transportSessionID=%d"
+ "VCVideoStream [%s] %s:%d SCVideoStreamAnalyzer created for participant=%@"
+ "VideoPacketBuffer [%s] %s:%d @:@ VideoPacketBuffer-create (%p) %s"
+ "VideoPacketBuffer [%s] %s:%d @:@ VideoPacketBuffer-created (%p) %s"
+ "VideoReceiver [%s] %s:%d @:@ VideoReceiver-CreateHandle Created VideoReceiver handle=%p for videoReceiver=%p, %s, videoReceiver->config.videoTSRate=%d, videoReceiver->config.enableJitterBufferInReceiver=%d, videoReceiver->config.enableJitterBufferInPlayer=%d, videoPlayerHandlePtr=%p"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}16@0:8"
+ "_VCVideoReceiverDefault_EndSensitiveContentAnalysisCallback"
+ "copyStateQueue"
+ "enableDecoderPrewarming"
+ "initWithClientPid:ssrc:transportSessionID:streamToken:experimentManager:logPrefix:"
+ "initWithTransportSessionID:idsParticipantID:ssrc:streamToken:logPrefix:"
+ "initWithTransportSessionID:localSSRC:streamToken:logPrefix:"
+ "isStateQueueSet"
+ "parent=%p"
+ "reportInitialThermalLevel"
+ "setPropertyValue:forPropertyName:xpcKey:xpcMessageName:batchSupported:"
+ "stop timed out"
+ "stringForAudioType:"
+ "stringForPlaybackMode:"
+ "terminateProcess:terminateSource:"
+ "v1640@0:8{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?[30c]}16"
+ "v24@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?[30c]}16"
+ "v24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}16"
+ "v32@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?[30c]}16@24"
+ "v52@0:8@16@24@32r*40B48"
+ "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}16@0:8"
+ "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}24@0:8i16i20"
+ "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}28@0:8I16r^{tagVCAudioIODelegateContext=@^?^vq@@}20"
+ "{tagVCVideoPacketBufferConfig=SIi^v[200c]iBB^{__CFAllocator}BBB{tagVCVideoPacketBufferFrameDecryptionCallbackContext=^v^?}{tagVCVideoPacketBufferEnqueueFailedFrameToJitterBufferCallbackContext=^v^?}B^{tagVCNACKGenerator}{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BBBB[30c]}24@0:8^{_RTPMediaPacket=iiiSIISBdBBBQ[12S]CC{?=iiBQ}Q{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}BBBC}16"
+ "{tagVCVideoReceiverConfig=\"streamCount\"I\"streamConfigs\"[9{tagVCVideoReceiverStreamConfig=\"streamInfo\"{tagVCVideoReceiverStreamIDInfo=\"streamID\"S\"repairStreamID\"S\"baseStreamID\"S\"subStreamCount\"I\"subStreamIDs\"[9S]\"subStreamRepairIDs\"[9S]}\"rtpHandle\"^{tagHANDLE}\"featureListStrings\"^{__CFDictionary}\"onDemandIDR\"B\"framerate\"S\"tileIndex\"C\"isOneToOne\"B\"isTemporalScalingEnabled\"B\"sframeCryptor\"^{tagVCCryptor}\"mediaControlInfoGenerator\"^v\"statisticsCollector\"^v\"mode\"i\"isLTRPEnabled\"B\"isRTCPForLossFeedbackEnabled\"B\"isRTCPForLTRPAckEnabled\"B\"ltrAckRTCPPacketType\"i\"shouldEnableMLEnhance\"B\"supportedMLEnhanceTypes\"I\"shouldEnableLossStats\"B\"afbRxFrontCameraEnabled\"B\"afbRxBackCameraEnabled\"B\"videoFrameMetadataSupportedVersion\"i\"fecHeaderVersion\"C\"fecLossFeedbackBitfieldLength\"S}]\"mode\"i\"jitterBufferMode\"i\"streamToken\"q\"audioTSRate\"i\"videoTSRate\"i\"enableFrameDiscontinuityStatus\"B\"enableVPBLogging\"i\"dumpID\"I\"enableControlByte\"i\"enableBitstreamCapture\"i\"enableRxDecodeYUVDump\"i\"enableUEP\"i\"enableRecvBitstreamDump\"i\"reportingParentID\"i\"shouldEnableFaceZoom\"B\"useDisplayLink\"B\"enableDeferredAssembly\"B\"deferredAssemblyOffset\"d\"callbackContext\"^v\"remoteFrameCallback\"^?\"sampleBufferCallback\"^?\"streamSwitchCallback\"^?\"keyFrameGenerationCallback\"^?\"sendLTRAckCallback\"^?\"ackLTRFrameCallback\"^?\"modeSwitchCallback\"^?\"idsParticipantID\"Q\"triggerSoundAlarmOnRTPReceive\"B\"decoderNumOfTiles\"S\"useInternalRTPThreading\"B\"useAssemblyThread\"B\"wrmInfo\"^{tagWRMMetricsInfo}\"maxDisplayRefreshRate\"I\"enableJitterBufferInReceiver\"B\"enableJitterBufferInPlayer\"B\"enableImmediateDecode\"B\"enableJitterBufferHighStartMode\"B\"enableDecodingStartAlignmentWithJBStart\"B\"isLTRPEnabled\"B\"isAsyncDecodingEnabled\"B\"isReceiverSideVCRCFeedbackEnabled\"B\"isVCRCStatsOnlyVideoBased\"B\"fecHeaderV1Enabled\"B\"fecHeaderVersion\"C\"enableQueueAlarmForDisplay\"B\"useRTCPForFIR\"B\"sendRTCP_PSFB_FIR\"B\"enableJBDynamicModeSwitch\"B\"useInternalClockForPresentation\"B\"mediaControlInfoGenerator\"^v\"isVariableSliceModeEnabled\"B\"streamSwitchEnabled\"B\"cvoExtensionID\"I\"videoJBEnabled\"B\"enableAVLooseSync\"B\"targetDisplayAlarmCount\"S\"jbTargetEstimatorSynchronizer\"^{tagVCJBTargetEstimatorSynchronizer}\"participantId\"^{__CFString}\"sessionId\"^{__CFString}\"streamGroupID\"I\"isReferenceFrameEnabled\"B\"isLateFrameRecoveryEnabled\"B\"enableHighWatermarkQueueDiscard\"B\"externalPresentationClockType\"i\"isServerPacketRetransmissionEnabled\"B\"isRTTBasedFIRThrottlingEnabled\"B\"nackGeneratorStoreBagsConfig\"{tagVCNACKGeneratorStoreBagsConfig=\"nackGeneratorStorebagConfigVersion\"C\"nackSeqNumAgingDuration\"f\"nackThrottlingBitRateLimitingMaxRatio\"f\"isExtraDelayForPacketRetransmissionsEnabled\"B\"nackThrottlingFactorBuckets\"[4f]\"nackThrottlingPlrBuckets\"[4f]\"nackGenerationMaxPLR\"f\"nackGenerationMaxRTT\"f\"rttForRTxFulfillmentWaitTime\"f\"rttForRTxFulfillmentMultiplier\"f\"rtxIncompleteFrameBufferDurationMultiplier\"f}\"forceZeroRegionOfInterestOrigin\"B\"isLateKeyFrameDetectionEnabled\"B\"cannedReplayContext\"^v\"rateAdaptation\"^v\"overlayToken\"q\"minPlaybackInterval\"d\"minRenderingDelay\"d\"noVideoDisplayedTimeoutSeconds\"d\"fixedJitterBufferSize\"d\"videoStallPercentageThreshold\"I\"reportVideoDegradedEvents\"B\"pdDecryptionContext\"^v\"pixelFormat\"I\"fecLossFeedbackBitfieldLength\"S\"useMultiImageDecoding\"B\"experimentManager\"^v\"enableInterleavedDecoding\"B\"numberOfInterleavedDecoders\"I\"beginSensitiveContentAnalysisCallback\"^?\"endSensitiveContentAnalysisCallback\"^?\"logPrefix\"[30c]}"
+ "{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?[30c]}16@0:8"
+ "{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?[30c]}24@0:8@16"
+ "{tagVCVideoStreamReceiverConfig=^{tagHANDLE}@{tagVCVideoReceiverDelegateRealtimeInstanceVTable=^?^?}^{opaqueRTCReporting}Ii@B^v^?@[30c]}28@0:8I16^{opaqueRTCReporting=}20"
- " [%s] %s:%d %@(%p) Active connection changed with new connection uplinkBitrateCap %d"
- " [%s] %s:%d %@(%p) CMSession:[%u] Starting AUIO operatingMode[%d] deviceRole[%d] remoteCodecType[%s] remoteCodecRate[%f] isMicrophoneMuted[%d]"
- " [%s] %s:%d %@(%p) Failed to stop video capture server error=%@"
- " [%s] %s:%d %@(%p) Participant init %@"
- " [%s] %s:%d %@(%p) Starting group. groupEntries=%@"
- " [%s] %s:%d %@(%p) Starting stream group. streamGroupID=%s, streamToken=%u"
- " [%s] %s:%d %@(%p) Starting... audioController=%@, controllerClient=%@, delegate=%@"
- " [%s] %s:%d %@(%p) Stream successfully started"
- " [%s] %s:%d %@(%p) capture = %dx%d, encode = %dx%d"
- " [%s] %s:%d %@(%p) startAudioIO is completed"
- " [%s] %s:%d %@(%p) transportToken[%@]"
- " [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/Others/RTCPTransport.c:%d: Invalid RTCP packet length"
- " [%s] %s:%d Active connection changed with new connection uplinkBitrateCap %d"
- " [%s] %s:%d CMSession:[%u] Starting AUIO operatingMode[%d] deviceRole[%d] remoteCodecType[%s] remoteCodecRate[%f] isMicrophoneMuted[%d]"
- " [%s] %s:%d Created AVAudioSession=%p audioSessionID=%u"
- " [%s] %s:%d Failed to create format description for audio buffer"
- " [%s] %s:%d Failed to stop video capture server error=%@"
- " [%s] %s:%d Participant init %@"
- " [%s] %s:%d Starting group. groupEntries=%@"
- " [%s] %s:%d Starting stream group. streamGroupID=%s, streamToken=%u"
- " [%s] %s:%d Starting... audioController=%@, controllerClient=%@, delegate=%@"
- " [%s] %s:%d Stream successfully started"
- " [%s] %s:%d VCCMSessionStub_CMSessionBeginInterruption result=%d"
- " [%s] %s:%d capture = %dx%d, encode = %dx%d"
- " [%s] %s:%d startAudioIO is completed"
- " [%s] %s:%d success=%d"
- " [%s] %s:%d transportToken[%@]"
- "-[AVAudioClient setAudioSessionProperties:]_block_invoke_2"
- "-[AVCSessionParticipant setPropertyValue:forPropertyName:xpcKey:xpcMessageName:]"
- "-[AVCSessionParticipant setPropertyValue:forPropertyName:xpcKey:xpcMessageName:]_block_invoke"
- "-[VCVideoStream initWithTransportSessionID:idsParticipantID:ssrc:streamToken:]"
- "2145.50.1"
- "@24@0:8^{?=i{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}iiIi}16"
- "@24@0:8^{tagVCVideoStreamReceiverConfig=^{tagHANDLE}@{tagVCVideoReceiverDelegateRealtimeInstanceVTable=^?^?}^{opaqueRTCReporting}Ii@B^v^?@}16"
- "@24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q}16"
- "@44@0:8i16I20I24q28@36"
- "@72@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?}16@24r^{tagVCVideoReceiverDelegateRealtimeInstanceVTable=^?^?}32^{opaqueRTCReporting=}40@48^{tagHANDLE=i}56@64"
- "@:@ AVAudioClient-initializeAudioSessionQ"
- "AUIO [%s] %s:%d /Library/Caches/com.apple.xbs/Sources/AVConference/AVConference.subproj/Sources/AUIO/AUIO.mm:%d: AUIO=%p AudioOutputUnitStart() completed"
- "AUIO [%s] %s:%d AUIO=%p AUIO Starting..."
- "AUIO [%s] %s:%d Successfully created the AUIO"
- "AVCAudioClient [%s] %s:%d %s startAudioSession call from client. processId=%d"
- "AVCAudioClient [%s] %s:%d @:@ AVAudioClient-initializeAudioSessionQ (%p)"
- "B24@0:8^{?=i{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}iiIi}16"
- "B24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q}16"
- "Starting Screen Capture with screenShareDict=%s"
- "T@\"NSObject<OS_dispatch_queue>\",N"
- "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}},R,VaudioReceiver"
- "T{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?},V_videoReceiverConfig"
- "Updating Screen Capture with screenShareDict=%s"
- "VCAudioBufferList_CreateSampleBufferAllocateWithAllocator"
- "VCAudioReceiver [%s] %s:%d @=@ Health: VCAudioReceiver ParticipantID=%s erasure percentage=%.2f%% PLR percentage=%.2f%% current percentage:%.2f%% (rec:%u exp:%u, loss:%u)"
- "VCSession [%s] %s:%d %@(%p) Adding participant[%s]"
- "VCSession [%s] %s:%d Adding participant[%s]"
- "VCSession [%s] %s:%d Connection changed to '%@'"
- "VCSessionParticipantRemote [%s] %s:%d %@(%p) Participant init %@"
- "VCSessionParticipantRemote [%s] %s:%d Participant init %@"
- "VCVideoCaptureServer [%s] %s:%d Start screen capture"
- "VCVideoStream [%s] %s:%d VCVideoStream[%p] init queue=%p for idsParticipantID=%llu streamToken=%u transportSessionID=%d"
- "VCVideoStream [%s] %s:%d VCVideoStream[%p] received first remote frame"
- "VCVideoStream [%s] %s:%d VCVideoStream[%p] received first remote frame frameTime=%f"
- "VTSCDSMAX"
- "VTSCRSMAX"
- "VideoReceiver [%s] %s:%d Created VideoReceiver handle=%p for videoReceiver=%p, videoReceiver->config.videoTSRate=%d, videoReceiver->config.enableJitterBufferInReceiver=%d, videoReceiver->config.enableJitterBufferInPlayer=%d, videoPlayerHandlePtr=%p"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}16@0:8"
- "initWithClientPid:ssrc:transportSessionID:streamToken:experimentManager:"
- "setPropertyValue:forPropertyName:xpcKey:xpcMessageName:"
- "v1608@0:8{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?}16"
- "v24@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?}16"
- "v24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q}16"
- "v32@0:8^{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?}16@24"
- "v48@0:8@16@24@32r*40"
- "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q}16@0:8"
- "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q}24@0:8i16i20"
- "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q}28@0:8I16r^{tagVCAudioIODelegateContext=@^?^vq@@}20"
- "{tagVCVideoPacketBufferConfig=SIi^v[200c]iBB^{__CFAllocator}BBB{tagVCVideoPacketBufferFrameDecryptionCallbackContext=^v^?}{tagVCVideoPacketBufferEnqueueFailedFrameToJitterBufferCallbackContext=^v^?}B^{tagVCNACKGenerator}{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BBBB}24@0:8^{_RTPMediaPacket=iiiSIISBdBBBQ[12S]CC{?=iiBQ}Q{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}{VCBlockBuffer_t=^{OpaqueCMBlockBuffer}Q*}BBBC}16"
- "{tagVCVideoReceiverConfig=\"streamCount\"I\"streamConfigs\"[9{tagVCVideoReceiverStreamConfig=\"streamInfo\"{tagVCVideoReceiverStreamIDInfo=\"streamID\"S\"repairStreamID\"S\"baseStreamID\"S\"subStreamCount\"I\"subStreamIDs\"[9S]\"subStreamRepairIDs\"[9S]}\"rtpHandle\"^{tagHANDLE}\"featureListStrings\"^{__CFDictionary}\"onDemandIDR\"B\"framerate\"S\"tileIndex\"C\"isOneToOne\"B\"isTemporalScalingEnabled\"B\"sframeCryptor\"^{tagVCCryptor}\"mediaControlInfoGenerator\"^v\"statisticsCollector\"^v\"mode\"i\"isLTRPEnabled\"B\"isRTCPForLossFeedbackEnabled\"B\"isRTCPForLTRPAckEnabled\"B\"ltrAckRTCPPacketType\"i\"shouldEnableMLEnhance\"B\"supportedMLEnhanceTypes\"I\"shouldEnableLossStats\"B\"afbRxFrontCameraEnabled\"B\"afbRxBackCameraEnabled\"B\"videoFrameMetadataSupportedVersion\"i\"fecHeaderVersion\"C\"fecLossFeedbackBitfieldLength\"S}]\"mode\"i\"jitterBufferMode\"i\"streamToken\"q\"audioTSRate\"i\"videoTSRate\"i\"enableFrameDiscontinuityStatus\"B\"enableVPBLogging\"i\"dumpID\"I\"enableControlByte\"i\"enableBitstreamCapture\"i\"enableRxDecodeYUVDump\"i\"enableUEP\"i\"enableRecvBitstreamDump\"i\"reportingParentID\"i\"shouldEnableFaceZoom\"B\"useDisplayLink\"B\"enableDeferredAssembly\"B\"deferredAssemblyOffset\"d\"callbackContext\"^v\"remoteFrameCallback\"^?\"sampleBufferCallback\"^?\"streamSwitchCallback\"^?\"keyFrameGenerationCallback\"^?\"sendLTRAckCallback\"^?\"ackLTRFrameCallback\"^?\"modeSwitchCallback\"^?\"idsParticipantID\"Q\"triggerSoundAlarmOnRTPReceive\"B\"decoderNumOfTiles\"S\"useInternalRTPThreading\"B\"useAssemblyThread\"B\"wrmInfo\"^{tagWRMMetricsInfo}\"maxDisplayRefreshRate\"I\"enableJitterBufferInReceiver\"B\"enableJitterBufferInPlayer\"B\"enableImmediateDecode\"B\"enableJitterBufferHighStartMode\"B\"enableDecodingStartAlignmentWithJBStart\"B\"isLTRPEnabled\"B\"isAsyncDecodingEnabled\"B\"isReceiverSideVCRCFeedbackEnabled\"B\"isVCRCStatsOnlyVideoBased\"B\"fecHeaderV1Enabled\"B\"fecHeaderVersion\"C\"enableQueueAlarmForDisplay\"B\"useRTCPForFIR\"B\"sendRTCP_PSFB_FIR\"B\"enableJBDynamicModeSwitch\"B\"useInternalClockForPresentation\"B\"mediaControlInfoGenerator\"^v\"isVariableSliceModeEnabled\"B\"streamSwitchEnabled\"B\"cvoExtensionID\"I\"videoJBEnabled\"B\"enableAVLooseSync\"B\"targetDisplayAlarmCount\"S\"jbTargetEstimatorSynchronizer\"^{tagVCJBTargetEstimatorSynchronizer}\"participantId\"^{__CFString}\"sessionId\"^{__CFString}\"streamGroupID\"I\"isReferenceFrameEnabled\"B\"isLateFrameRecoveryEnabled\"B\"enableHighWatermarkQueueDiscard\"B\"externalPresentationClockType\"i\"isServerPacketRetransmissionEnabled\"B\"isRTTBasedFIRThrottlingEnabled\"B\"nackGeneratorStoreBagsConfig\"{tagVCNACKGeneratorStoreBagsConfig=\"nackGeneratorStorebagConfigVersion\"C\"nackSeqNumAgingDuration\"f\"nackThrottlingBitRateLimitingMaxRatio\"f\"isExtraDelayForPacketRetransmissionsEnabled\"B\"nackThrottlingFactorBuckets\"[4f]\"nackThrottlingPlrBuckets\"[4f]\"nackGenerationMaxPLR\"f\"nackGenerationMaxRTT\"f\"rttForRTxFulfillmentWaitTime\"f\"rttForRTxFulfillmentMultiplier\"f\"rtxIncompleteFrameBufferDurationMultiplier\"f}\"forceZeroRegionOfInterestOrigin\"B\"isLateKeyFrameDetectionEnabled\"B\"cannedReplayContext\"^v\"rateAdaptation\"^v\"overlayToken\"q\"minPlaybackInterval\"d\"minRenderingDelay\"d\"noVideoDisplayedTimeoutSeconds\"d\"fixedJitterBufferSize\"d\"videoStallPercentageThreshold\"I\"reportVideoDegradedEvents\"B\"pdDecryptionContext\"^v\"pixelFormat\"I\"fecLossFeedbackBitfieldLength\"S\"useMultiImageDecoding\"B\"experimentManager\"^v\"enableInterleavedDecoding\"B\"numberOfInterleavedDecoders\"I\"beginSensitiveContentAnalysisCallback\"^?\"endSensitiveContentAnalysisCallback\"^?}"
- "{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?}16@0:8"
- "{tagVCVideoReceiverConfig=I[9{tagVCVideoReceiverStreamConfig={tagVCVideoReceiverStreamIDInfo=SSSI[9S][9S]}^{tagHANDLE}^{__CFDictionary}BSCBB^{tagVCCryptor}^v^viBBBiBIBBBiCS}]iiqiiBiIiiiiiiBBBd^v^?^?^?^?^?^?^?QBSBB^{tagWRMMetricsInfo}IBBBBBBBBBBCBBBBB^vBBIBBS^{tagVCJBTargetEstimatorSynchronizer}^{__CFString}^{__CFString}IBBBiBB{tagVCNACKGeneratorStoreBagsConfig=CffB[4f][4f]fffff}BB^v^vqddddIB^vISB^vBI^?^?}24@0:8@16"
- "{tagVCVideoStreamReceiverConfig=^{tagHANDLE}@{tagVCVideoReceiverDelegateRealtimeInstanceVTable=^?^?}^{opaqueRTCReporting}Ii@B^v^?@}28@0:8I16^{opaqueRTCReporting=}20"

```
