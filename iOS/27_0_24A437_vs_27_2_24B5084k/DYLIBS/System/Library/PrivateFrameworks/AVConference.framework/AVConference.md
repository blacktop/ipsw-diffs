## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2235.63.1.2.0
-  __TEXT.__text: 0x7d4a88
-  __TEXT.__objc_methlist: 0x3ac00
-  __TEXT.__const: 0xc690
-  __TEXT.__cstring: 0x9f9f5
-  __TEXT.__oslogstring: 0x141d50
-  __TEXT.__gcc_except_tab: 0x2d04
+2260.9.1.0.0
+  __TEXT.__text: 0x7d5e08
+  __TEXT.__objc_methlist: 0x3ab38
+  __TEXT.__const: 0xc680
+  __TEXT.__cstring: 0x9f767
+  __TEXT.__oslogstring: 0x1431d7
+  __TEXT.__gcc_except_tab: 0x2dbc
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x1b708
+  __TEXT.__unwind_info: 0x1b6a8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x77e0
-  __DATA_CONST.__objc_classlist: 0x14b8
+  __DATA_CONST.__const: 0x77f8
+  __DATA_CONST.__objc_classlist: 0x14b0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x510
+  __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18d98
+  __DATA_CONST.__objc_selrefs: 0x18dd0
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x1268
+  __DATA_CONST.__objc_superrefs: 0x1260
   __DATA_CONST.__objc_arraydata: 0x27d8
-  __DATA_CONST.__got: 0x1e40
-  __AUTH_CONST.__const: 0x4608
-  __AUTH_CONST.__cfstring: 0x29d00
-  __AUTH_CONST.__objc_const: 0x6d128
+  __DATA_CONST.__got: 0x1e48
+  __AUTH_CONST.__const: 0x4588
+  __AUTH_CONST.__cfstring: 0x29de0
+  __AUTH_CONST.__objc_const: 0x6d0e8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x52f8
   __AUTH_CONST.__objc_arrayobj: 0x1d88
+  __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__objc_doubleobj: 0x200
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH_CONST.__auth_got: 0x2c38
+  __AUTH_CONST.__auth_got: 0x2c60
   __AUTH.__data: 0xf8
-  __DATA.__objc_ivar: 0x7714
-  __DATA.__data: 0x7d48
+  __DATA.__objc_ivar: 0x772c
+  __DATA.__data: 0x7ce8
   __DATA.__common: 0x55
-  __DATA_DIRTY.__objc_data: 0xcf30
+  __DATA_DIRTY.__objc_data: 0xcee0
   __DATA_DIRTY.__data: 0x420
-  __DATA_DIRTY.__bss: 0xae0
+  __DATA_DIRTY.__bss: 0xab0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35501
-  Symbols:   53136
-  CStrings:  34072
+  Functions: 35478
+  Symbols:   53127
+  CStrings:  34109
 
Symbols:
+ +[VCMediaNegotiationBlobV2StreamGroup(Utils) homeKitCameraDefaultsForStreamGroupCamera:]
+ -[CannedEncodedVideoCapture reset]
+ -[CannedRawVideoCapture reset]
+ -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:hasSecondary:]
+ -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:]
+ -[VCAudioSessionAVAS dispatchedIsInputAvailable]
+ -[VCAudioStream reportingAudioJBRampStats]
+ -[VCAudioStreamSendGroupConfig enableSyncGroupReferenceTimestamp]
+ -[VCAudioStreamSendGroupConfig setEnableSyncGroupReferenceTimestamp:]
+ -[VCConnectionHealthMonitor resetStallDetectionStateAfterMonitoringResumed]
+ -[VCMockQRServer forwardOnePacketFromListenerSocket:listenerSourceIP:listenerSourcePort:forwarderSocketList:listenerParticipantID:]
+ -[VCMockQRServer stopPacketForwarders]
+ -[VCSessionPowerPolicy hasPrimaryCameraFrameRateMitigation]
+ -[VCSessionPowerPolicy hasSecondaryCameraFrameRateMitigation]
+ -[VCTransportSessionMultiLink handleListenerEvents:error:result:]
+ -[VCVideoCaptureServer publishCameraUIDChangedForCameraUID:cameraSessionType:]
+ -[VCVideoStream supportsMaxKeyFrameIntervalDuration]
+ -[VCVideoTransmitterConfig reinitEncoderOnFrameAspectRatioChangeEnabled]
+ -[VCVideoTransmitterConfig setReinitEncoderOnFrameAspectRatioChangeEnabled:]
+ -[VCVideoTransmitterConfig setVtLoggingIdentifier:]
+ -[VCVideoTransmitterConfig vtLoggingIdentifier]
+ GCC_except_table301
+ GCC_except_table38
+ _CVImageBufferGetColorSpace
+ _CVPixelBufferPoolFlush
+ _OBJC_IVAR_$_AVCPacketRelaySocketConnection._isMonitoring
+ _OBJC_IVAR_$_VCAVFoundationCapture._lastAttachPerFrameAR
+ _OBJC_IVAR_$_VCAudioStreamSendGroup._enableSyncGroupReferenceTimestamp
+ _OBJC_IVAR_$_VCAudioStreamSendGroupConfig._enableSyncGroupReferenceTimestamp
+ _OBJC_IVAR_$_VCAudioToolboxAudioComponentMock._activeInstances
+ _OBJC_IVAR_$_VCMockQRServer._forwarderQueue
+ _OBJC_IVAR_$_VCMockQRServer._forwarderSources
+ _OBJC_IVAR_$_VCRedundancyControlAlgorithmVideo._congestionKeepHistoryRatio
+ _OBJC_IVAR_$_VCRedundancyControlAlgorithmVideo._feedbackHistoryMaxLength
+ _OBJC_IVAR_$_VCRedundancyControlAlgorithmVideo._freezeStartTime
+ _OBJC_IVAR_$_VCVideoStreamRateAdaptationFeedbackOnly._rateControlFeedbackDrained
+ _OBJC_IVAR_$_VCVideoStreamReceiver._vtLoggingIdentifier
+ _OBJC_IVAR_$_VCVideoStreamSendGroup._hasModulatedTimestampBaseline
+ _OBJC_IVAR_$_VCVideoStreamSendGroup._lastModulatedTimestamp
+ _OBJC_IVAR_$_VCVideoStreamTransmitter._vtLoggingIdentifier
+ _OBJC_IVAR_$_VCVideoTransmitterConfig._reinitEncoderOnFrameAspectRatioChangeEnabled
+ _OBJC_IVAR_$_VCVideoTransmitterConfig._vtLoggingIdentifier
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _VCConnectionIDS_SetLocalLinkTechnology
+ _VCJitterBuffer_GetInitialRampMetrics
+ _VCMediaQueue_RecyclePacket
+ _VCRedundancyControllerVideoCongestionKeepHistoryRatio
+ _VCStringUtils_AddVTLoggingIdentifier
+ _VCStringUtils_CFStringNotEqual
+ _VCStringUtils_SetVTLoggingIdentifier
+ _VCVideoStreamConfig_SetVTLoggingIdentifier
+ _VTCompressionSessionCreateWithOptions
+ __OBJC_$_INSTANCE_VARIABLES_VCAudioToolboxAudioComponentMock
+ __VCMediaQueue_DrainPendingRecyclePackets
+ __VideoPacketBuffer_SetNeedRefresh
+ ___135-[VCMockQRServer startPacketForwarderWithListenerSocket:listenerSourceIP:listenerSourcePort:forwarderSocketList:listenerParticipantID:]_block_invoke
+ ___38-[VCAudioSessionAVAS isInputAvailable]_block_invoke
+ ___38-[VCAudioSessionAVAS isInputSupported]_block_invoke
+ ___38-[VCMockQRServer stopPacketForwarders]_block_invoke
+ ___62-[VCVideoStreamRateAdaptationFeedbackOnly startFeedbackSource]_block_invoke_2
+ ___78-[VCVideoCaptureServer publishCameraUIDChangedForCameraUID:cameraSessionType:]_block_invoke
+ ___86-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:]_block_invoke
+ ___block_descriptor_61_e8_32o40o48o_e5_v8?0ls32l8s40l8s48l8
+ _kForwarderQueueSpecificKey
+ _kVCXPCConnectionTimeoutQueueSpecificKey
+ _kVTCompressionSessionOption_LoggingIdentifier
+ _kVTDecompressionSessionOption_LoggingIdentifier
+ _nw_error_get_error_domain
+ _objc_msgSend$batchSetCameraUIDsPrimary:secondary:hasSecondary:
+ _objc_msgSend$batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:
+ _objc_msgSend$dispatchedIsInputAvailable
+ _objc_msgSend$enableSyncGroupReferenceTimestamp
+ _objc_msgSend$forwardOnePacketFromListenerSocket:listenerSourceIP:listenerSourcePort:forwarderSocketList:listenerParticipantID:
+ _objc_msgSend$handleListenerEvents:error:result:
+ _objc_msgSend$hasPrimaryCameraFrameRateMitigation
+ _objc_msgSend$hasSecondaryCameraFrameRateMitigation
+ _objc_msgSend$homeKitCameraDefaultsForStreamGroupCamera:
+ _objc_msgSend$publishCameraUIDChangedForCameraUID:cameraSessionType:
+ _objc_msgSend$reinitEncoderOnFrameAspectRatioChangeEnabled
+ _objc_msgSend$reportingAudioJBRampStats
+ _objc_msgSend$resetStallDetectionStateAfterMonitoringResumed
+ _objc_msgSend$setEnableSyncGroupReferenceTimestamp:
+ _objc_msgSend$setReinitEncoderOnFrameAspectRatioChangeEnabled:
+ _objc_msgSend$setVtLoggingIdentifier:
+ _objc_msgSend$setupLocalABTestSwitches
+ _objc_msgSend$setupLocalOnOffSwitches
+ _objc_msgSend$stopPacketForwarders
+ _objc_msgSend$supportsMaxKeyFrameIntervalDuration
+ _objc_msgSend$vtLoggingIdentifier
+ _xpc_copy_description
- -[AVCCaptionsClient initWithDelegate:translatorIdentifier:]
- -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:]
- -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]
- -[VCAudioCaptionsSpeechTranslator addToCaptionTasksWithError:]
- -[VCAudioCaptionsSpeechTranslator client:didReceiveTranscriptionResult:]
- -[VCAudioCaptionsSpeechTranslator client:didReceiveTranslationResult:]
- -[VCAudioCaptionsSpeechTranslator client:didStopTranslationWithError:]
- -[VCAudioCaptionsSpeechTranslator dealloc]
- -[VCAudioCaptionsSpeechTranslator destroyCaptions]
- -[VCAudioCaptionsSpeechTranslator finishCaptions]
- -[VCAudioCaptionsSpeechTranslator initWithDelegate:isLocal:taskIdentifier:reportingAgent:]
- -[VCAudioCaptionsSpeechTranslator initWithSpeechConfig:]
- -[VCAudioCaptionsSpeechTranslator packageAndSendTranscribedString:withTask:]
- -[VCAudioCaptionsSpeechTranslator packageAndSendTranslatedString:withTask:]
- -[VCAudioCaptionsSpeechTranslator pushSamples:numSamples:hostTime:]
- -[VCAudioCaptionsSpeechTranslator serverDidDisconnectForClient:]
- -[VCAudioCaptionsSpeechTranslator setUpCaptionsWithError:]
- -[VCAudioCaptionsSpeechTranslator setupTranslatorSharedWithError:]
- -[VCAudioCaptionsSpeechTranslator setupTranslatorStandaloneWithError:]
- -[VCAudioCaptionsSpeechTranslator shouldPushSamples]
- -[VCAudioCaptionsSpeechTranslator startCaptionsWithError:]
- -[VCAudioCaptionsSpeechTranslator stopCaptions]
- -[VCAudioCaptionsSpeechTranslator translationDidStartForClient:]
- -[VCAudioManager anyClientNeedsMicInputWithPreferredClient:]
- -[VCAudioManager updateMicAttributionForClient:shouldAdd:]
- -[VCTransportSessionMultiLink handleListenerEvents:error:]
- -[VCVideoStreamReceiver gatherInterframeDelayStats:]
- GCC_except_table300
- _OBJC_CLASS_$_VCAudioCaptionsSpeechTranslator
- _OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._currentSourceUpdateNumber
- _OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._currentTranslatedUpdateNumber
- _OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._isStarted
- _OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._transcriptionTimes
- _OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._translatorClient
- _OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._translatorConfiguration
- _OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._translatorStartDuration
- _OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._translatorStartTime
- _OBJC_IVAR_$_VCAudioManager._hasActiveMicClients
- _OBJC_IVAR_$_VCPowerManager._forceDisableThermal
- _OBJC_IVAR_$_VCVideoStreamReceiver._interframeDelayMonitor
- _OBJC_METACLASS_$_VCAudioCaptionsSpeechTranslator
- _VCAudioUnit_BasebandInstance
- _VCAudioUnit_DefaultOutputInstance
- _VCAudioUnit_RemoteIOInstance
- _VCAudioUnit_SystemAudioInstance
- _VCAudioUnit_VoiceProcessorInstance
- _VCFeatureFlagManager_HostAudioTranscriptionAnalysisServer
- _VCFeatureFlagManager_HostAudioTranscriptionAnalysisServer.flag
- _VCFeatureFlagManager_HostAudioTranscriptionAnalysisServer.onceToken
- _VCFeatureFlagManager_HostSpeechTranslationServer
- _VCFeatureFlagManager_HostSpeechTranslationServer.audioFlag
- _VCFeatureFlagManager_HostSpeechTranslationServer.onceToken
- _VCFeatureFlagManager_HostSpeechTranslationServer.videoFlag
- _VCSpeechTranslation_STSpeechTranslatorClientClass
- _VCSpeechTranslation_STSpeechTranslatorClientClass.onceToken
- _VCSpeechTranslation_STSpeechTranslatorClientClass.speechTranslatorClientClass
- _VCSpeechTranslation_STSpeechTranslatorConfigurationClass
- _VCSpeechTranslation_STSpeechTranslatorConfigurationClass.onceToken
- _VCSpeechTranslation_STSpeechTranslatorConfigurationClass.speechTranslatorConfigurationClass
- _VCSpeechTranslation_StartServer
- _VCVirtualAVCaptureDevice_OnMediaSample
- __OBJC_$_INSTANCE_METHODS_VCAudioCaptionsSpeechTranslator
- __OBJC_$_INSTANCE_VARIABLES_VCAudioCaptionsSpeechTranslator
- __OBJC_$_PROP_LIST_VCAudioCaptionsSpeechTranslator
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_STSpeechTranslatorClientDelegate
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_STSpeechTranslatorClientDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_STSpeechTranslatorClientDelegate
- __OBJC_$_PROTOCOL_REFS_STSpeechTranslatorClientDelegate
- __OBJC_CLASS_PROTOCOLS_$_VCAudioCaptionsSpeechTranslator
- __OBJC_CLASS_RO_$_VCAudioCaptionsSpeechTranslator
- __OBJC_LABEL_PROTOCOL_$_STSpeechTranslatorClientDelegate
- __OBJC_METACLASS_RO_$_VCAudioCaptionsSpeechTranslator
- __OBJC_PROTOCOL_$_STSpeechTranslatorClientDelegate
- __VCSpeechTranslation_LibraryHandle
- __VCSpeechTranslation_LibraryHandle.onceToken
- __VCVideoStreamSendGroup_SecondaryCameraTransfer
- ___39-[VCMockQRServer startPacketForwarders]_block_invoke
- ___70-[VCAudioCaptionsSpeechTranslator client:didReceiveTranslationResult:]_block_invoke
- ___70-[VCAudioCaptionsSpeechTranslator setupTranslatorStandaloneWithError:]_block_invoke
- ___72-[VCAudioCaptionsSpeechTranslator client:didReceiveTranscriptionResult:]_block_invoke
- ___73-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]_block_invoke
- ___78-[VCVideoCaptureServer dispatchedSetCaptureCameraWithToken:cameraSessionType:]_block_invoke_2
- ___VCFeatureFlagManager_HostAudioTranscriptionAnalysisServer_block_invoke
- ___VCFeatureFlagManager_HostSpeechTranslationServer_block_invoke
- ___VCSpeechTranslation_STSpeechTranslatorClientClass_block_invoke
- ___VCSpeechTranslation_STSpeechTranslatorConfigurationClass_block_invoke
- ____VCSpeechTranslation_LibraryHandle_block_invoke
- _objc_msgSend$anyClientNeedsMicInputWithPreferredClient:
- _objc_msgSend$batchSetCameraUIDsPrimary:secondary:
- _objc_msgSend$batchSetCameraUIDsPrimary:secondary:aspectRatio:
- _objc_msgSend$handleListenerEvents:error:
- _objc_msgSend$initWithDelegate:translatorIdentifier:direction:reportingSamplingUUID:
- _objc_msgSend$initWithSourceLocale:targetLocale:
- _objc_msgSend$initWithSourceLocale:targetLocale:omitTranslatedAudio:offlineMTModel:taskHint:
- _objc_msgSend$initWithTranslatorIdentifier:delegate:delegateQueue:
- _objc_msgSend$instancesRespondToSelector:
- _objc_msgSend$setOmitTranslatedAudio:
- _objc_msgSend$setProduceAudio:
- _objc_msgSend$translatorIdentifier
- _objc_msgSend$updateMicAttributionForClient:shouldAdd:
CStrings:
+ " [%s] %s:%d %@(%p) Applying mute property for audioSessionId=%d, isMuted=%d"
+ " [%s] %s:%d %@(%p) Capturing first modulatedTimestamp=%u baseline, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d %@(%p) Failed to allocate forwarder sources"
+ " [%s] %s:%d %@(%p) Failed to allocate inter frame delay monitor"
+ " [%s] %s:%d %@(%p) Failed to allocate socket list"
+ " [%s] %s:%d %@(%p) Failed to create forwarder queue"
+ " [%s] %s:%d %@(%p) Failed to create read source for socket=%d (participant=%@)"
+ " [%s] %s:%d %@(%p) Failed to create sockets from configuration"
+ " [%s] %s:%d %@(%p) Failed to extract RTP information from video packet for participant=%@"
+ " [%s] %s:%d %@(%p) Failed to find datagram channel for participant=%@, skipping packet"
+ " [%s] %s:%d %@(%p) Failed to forward packet to=%@:%d (participant=%@), errno=%d"
+ " [%s] %s:%d %@(%p) Failed to retain participant configuration"
+ " [%s] %s:%d %@(%p) Found matching datagram channel for participant=%@"
+ " [%s] %s:%d %@(%p) Found send key material for _latestSendKeyIndex=%@, returning MKI=%@, sendKeysCount=%d"
+ " [%s] %s:%d %@(%p) Keeping transactionID=%llu, already ahead of IDS baseline initialTransactionID=%llu"
+ " [%s] %s:%d %@(%p) NACK generated for SSRC=0x%X, NACK packet size=%zubytes, listener participant=%@"
+ " [%s] %s:%d %@(%p) NWConnection reported state=%d, errorDomain=%d, errorCode=%d"
+ " [%s] %s:%d %@(%p) No cached send key material for _latestSendKeyIndex=%@, sendKeysCount=%d"
+ " [%s] %s:%d %@(%p) No streamIDs found in packet, forwarding to all participants, new received bytes=%d, listened from=%@, participants who have to receive this packet are=%@"
+ " [%s] %s:%d %@(%p) Packet too short: receivedBytes=%d < headerSize=%d, dropping"
+ " [%s] %s:%d %@(%p) Participant=%@ has no entries in the subscription table"
+ " [%s] %s:%d %@(%p) Participant=%@ has no subscription matching packet stream IDs"
+ " [%s] %s:%d %@(%p) ProcessedBuffer: hasStreams=%d, streamIDCount=%d, streamIDs=%@"
+ " [%s] %s:%d %@(%p) ProcessedBuffer: participants who have to receive this packet are=%@"
+ " [%s] %s:%d %@(%p) Skipping the participant VCAudioIO start. isHomeKitVideo=%d"
+ " [%s] %s:%d %@(%p) Tracing number of bytes: receievedBytes=%d"
+ " [%s] %s:%d %@(%p) Tracing packet across the network, Mock QR Server received  RTP datagram size=%d, SSRC=0x%X, SeqNum=%u"
+ " [%s] %s:%d %@(%p) Trying to get the mockDatagramChannel, tempParticipantID value=%@"
+ " [%s] %s:%d %@(%p) Video frame is too old and modulated timestamp rolled backward – dropping frame. lastModulatedTimestamp=%u, modulatedTimestamp=%u, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d %@(%p) [FTDC] _videoCaptureSource=%d, _dualCaptureEnabled=%d, _dualCaptureReceiverEnabled=%d, _oneToOneModeEnabled=%d"
+ " [%s] %s:%d %@(%p) [FTDC] ignoring secondary aspectRatio=%d on the disable path"
+ " [%s] %s:%d %@(%p) [FTDC] ignoring secondary disable: dual capture already off"
+ " [%s] %s:%d %@(%p) [FTDC] primaryUID=%@, secondaryUID=%@, hasSecondary=%d, aspectRatio=%d, dualCaptureEnabled=%d"
+ " [%s] %s:%d %@(%p) error zero sampleBufferSize requested, maxSamplesPerFrame=%u, mBytesPerFrame=%u, audioPayloadsCount=%lu"
+ " [%s] %s:%d %@(%p) nw connection reported state=%d, errorDomain=%d, errorCode=%d"
+ " [%s] %s:%d %@(%p) recv failed: receivedBytes=%d, errno=%d, socket=%d"
+ " [%s] %s:%d %@(%p) setMicrophoneMuted:%d"
+ " [%s] %s:%d %@(%p) streamGroupID=%s, shouldSync=%d, hksvHasVideoStreamInput=%d"
+ " [%s] %s:%d Applying mute property for audioSessionId=%d, isMuted=%d"
+ " [%s] %s:%d Capturing first modulatedTimestamp=%u baseline, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d Failed [super init]"
+ " [%s] %s:%d Failed to allocate forwarder sources"
+ " [%s] %s:%d Failed to allocate inter frame delay monitor"
+ " [%s] %s:%d Failed to allocate socket list"
+ " [%s] %s:%d Failed to compose loggingIdentifier for streamToken=%ld"
+ " [%s] %s:%d Failed to create compressionSessionOptions"
+ " [%s] %s:%d Failed to create forwarder queue"
+ " [%s] %s:%d Failed to create read source for socket=%d (participant=%@)"
+ " [%s] %s:%d Failed to create sockets from configuration"
+ " [%s] %s:%d Failed to register stream group=%s for capture source ID=%d"
+ " [%s] %s:%d Failed to retain participant configuration"
+ " [%s] %s:%d Found send key material for _latestSendKeyIndex=%@, returning MKI=%@, sendKeysCount=%d"
+ " [%s] %s:%d Ignoring transitional linkTechnology=%u"
+ " [%s] %s:%d Invalid parameter: dictionary=%p key=%p identifier=%p"
+ " [%s] %s:%d Invalid parameter: identifier passed as NULL"
+ " [%s] %s:%d Invalid parameter: identifier=%p value=%p"
+ " [%s] %s:%d Keeping transactionID=%llu, already ahead of IDS baseline initialTransactionID=%llu"
+ " [%s] %s:%d NWConnection reported state=%d, errorDomain=%d, errorCode=%d"
+ " [%s] %s:%d No cached send key material for _latestSendKeyIndex=%@, sendKeysCount=%d"
+ " [%s] %s:%d Packet too short: receivedBytes=%d < headerSize=%d, dropping"
+ " [%s] %s:%d Redundancy unfrozen reason=%d isNetworkCongested=%d _offChannelTimeRatio=%2.3f freezeDuration=%2.3f keptHistory=%d"
+ " [%s] %s:%d SRTP verification failed (%X), consecutiveSRTPAuthFailures=%u, ssrc=%X"
+ " [%s] %s:%d Skipping the participant VCAudioIO start. isHomeKitVideo=%d"
+ " [%s] %s:%d SwitchManager: A/B testing turned off - using master local switch: %08X"
+ " [%s] %s:%d Timed out draining rate control feedback, source=%p"
+ " [%s] %s:%d Transport streams cleared, rtpTransportStream=%p, rtcpTransportStream=%p"
+ " [%s] %s:%d VTCompressionSessionCreateWithOptions failed (%d)"
+ " [%s] %s:%d Video frame is too old and modulated timestamp rolled backward – dropping frame. lastModulatedTimestamp=%u, modulatedTimestamp=%u, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d [%p] Adding %@=%@ to the codec session's dictionary"
+ " [%s] %s:%d [%p] Failed to create loggingIdentifier from vtLoggingIdentifier=%s"
+ " [%s] %s:%d [%p] InitialRamp Metrics: numPackets=%u numAudioPackets=%u hasSufficientAudio=%d numOOOPackets=%u maxOOODisplacementMs=%u avgOOODisplacementMs=%u"
+ " [%s] %s:%d [%p] InitialRamp OOO sn=%u prevSn=%u tsDelta=%u dispMs=%u numOOO=%u maxDispMs=%u"
+ " [%s] %s:%d [%p] InitialRamp START firstTs=%u windowEndTs=%u sampleRate=%u"
+ " [%s] %s:%d [%p] InitialRamp WINDOW CLOSED numPackets=%u numAudioPackets=%u numOOO=%u maxDispMs=%u sumDispMs=%.0f"
+ " [%s] %s:%d [%p] VideoTransmitter_CreateHandle wMTU[%d] bIsIPv6[%d] reinitOnFrameChangeEnabled[%s] reinitOnARChangeEnabled[%s]"
+ " [%s] %s:%d [FTDC] _videoCaptureSource=%d, _dualCaptureEnabled=%d, _dualCaptureReceiverEnabled=%d, _oneToOneModeEnabled=%d"
+ " [%s] %s:%d [FTDC] ignoring secondary aspectRatio=%d on the disable path"
+ " [%s] %s:%d [FTDC] ignoring secondary disable: dual capture already off"
+ " [%s] %s:%d [FTDC] primaryUID=%@, secondaryUID=%@, hasSecondary=%d, aspectRatio=%d, dualCaptureEnabled=%d"
+ " [%s] %s:%d [FTDC][PFAR] path=afterCapture, attach=%d, dualCaptureEnabled=%d, dualCaptureReceiverEnabled=%d, shouldAttachPerFrameAR=%d, frontCamera=%d, bufferWidth=%zu, bufferHeight=%zu"
+ " [%s] %s:%d [FTDC][PFAR] path=duringProcessEffect, attach=%d, dualCaptureEnabled=%d, dualCaptureReceiverEnabled=%d, shouldAttachPerFrameAR=%d, frontCamera=%d, bufferWidth=%zu, bufferHeight=%zu"
+ " [%s] %s:%d [HKSV3] came mediaSubtype='%s' did not match camera default, retried against HomeKit camera default. isValid=%d"
+ " [%s] %s:%d centerStageRectOfInterest rejected, centerStageEnabled=0, reason=%@"
+ " [%s] %s:%d error zero sampleBufferSize requested, maxSamplesPerFrame=%u, mBytesPerFrame=%u, audioPayloadsCount=%lu"
+ " [%s] %s:%d eventInfo has IDSDataChannelError, code = %u, ERROR = %@"
+ " [%s] %s:%d feedbackHistoryMaxLength=%2.3f congestionKeepHistoryRatio=%2.3f keepHistoryThreshold=%2.3f"
+ " [%s] %s:%d linkTechnology=%u"
+ " [%s] %s:%d loggingIdentifier=%s is %zu chars, over the %d VideoToolbox stores"
+ " [%s] %s:%d nw connection reported state=%d, errorDomain=%d, errorCode=%d"
+ " [%s] %s:%d recv failed: receivedBytes=%d, errno=%d, socket=%d"
+ " [%s] %s:%d recvmsg failed for socket=%d, errno=%d"
+ " [%s] %s:%d sampleOffset exceeds source sampleCount: sampleOffset=%u, source.sampleCount=%u"
+ " [%s] %s:%d self=%p, _mode=%d, _type=%d, algorithm=%s"
+ " [%s] %s:%d self=%p, redundancyPercentage=%u, previousRedundancyPercentage=%u, packetLossPercentageInput=%3.3f, _packetLossPercentage=%u, burstPacketLoss=%u, redundancyPercentageBasedOnPLR=%u, redundancyPercentageBasedOnBurstyLoss=%u"
+ " [%s] %s:%d setMicrophoneMuted:%d"
+ " [%s] %s:%d streamGroupID=%s is not an enumerated AVCStreamGroupID"
+ " [%s] %s:%d streamGroupID=%s streamInputID=%@ captureSourceID=%d"
+ " [%s] %s:%d streamGroupID=%s, shouldSync=%d, hksvHasVideoStreamInput=%d"
+ " [%s] %s:%d videoDecoder=%p decoded frame colorimetry changed to ColorPrimaries=%@ TransferFunction=%@ YCbCrMatrix=%@ for streamID=%d width=%d height=%d"
+ " [%s] %s:%d videoDecoder=%p decoded frame has no CGColorSpace attachment for streamID=%d width=%d height=%d"
+ "-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:]_block_invoke"
+ "-[VCAVFoundationCapture encodeProcessedPixelBuffer:time:imageData:processTime:]_block_invoke"
+ "-[VCAudioSessionAVAS isInputSupported]_block_invoke"
+ "-[VCConnectionManagerIDS updateLocalLinkTechnology:]"
+ "-[VCMockQRServer forwardOnePacketFromListenerSocket:listenerSourceIP:listenerSourcePort:forwarderSocketList:listenerParticipantID:]"
+ "-[VCMockQRServer initMockQRServer]"
+ "-[VCSessionParticipantLocal captureEncodingSize]"
+ "-[VCSessionParticipantLocal enableDualCaptureReceiver:]_block_invoke"
+ "-[VCTransportSessionMultiLink handleListenerEvents:error:result:]"
+ "2260.9.1"
+ "<%s:%p> Token (%d) Link (%d): %s <-> %s (%s, %s), priority %d, uplink bitrate cap (%u), downlink bitrate cap (%u), uplink audio only bitrate cap = (%u), uplink OneToOne bitrate cap = (%u), isLocalConstrained (%d), isRemoteConstrained (%d), isLocalExpensive (%d) isRemoteExpensive (%d) isLocalDelegated (%d) isRemoteDelegated (%d) isLocalUltraConstrained (%d) isRemoteUltraConstrained (%d) isVirtualRelayLink (%d) reportingIPVersion(%d) TransportLayerEncryption=%d relayProtocolStackDescrption(%@) channelDataBaseProtocolStackDescription(%@) _isHopByHopEncryptionSupported=%d localLinkTransport=%u localLinkTechnology=%u"
+ "AVC-CD/%ld"
+ "AVC-CE/%ld"
+ "AVC-SD/%ld"
+ "AVC-SE/%ld"
+ "AVCRC [%s] %s:%d [%p] ReportNetworkStatistics shouldReport=%d rttMs=%u arrivalTime=%f plr=%f plrAudio=%f plrVideo=%f (lastPlr=%f lastPlrAudio=%f lastPlrVideo=%f) burstPacketLoss=%u (lastBurst=%u) owrd=%u (lastOwrd=%u) isNetworkCongested=%d (lastCongested=%d) unconditional=%d"
+ "AVConferenceXPCServer [%s] %s:%d VCXPCServer: incoming request from PID=%d has no API key, event=%s"
+ "AVConferenceXPCServer: incoming request from PID=%d missing \"API\" key, event=%s"
+ "JBInitialRampAvgOOOTimeDisplacementMs"
+ "JBInitialRampHasSufficientAudioPackets"
+ "JBInitialRampMaxOOOTimeDisplacementMs"
+ "JBInitialRampNumAudioPackets"
+ "JBInitialRampNumOOOPackets"
+ "JBInitialRampNumPackets"
+ "Primary camera UID is required"
+ "SoundDec_Destroy"
+ "VCAudioReceiver [%s] %s:%d One or more input param(s) are NULL: audioReceiver=%p streamId=%p"
+ "VCAudioReceiver [%s] %s:%d VCAudioReceiver[%p] Could not allocate memory for Audio Frame"
+ "VCAudioStream [%s] %s:%d %@(%p) Reconfiguring VCAudioStream: transportCount=%lu->%lu localSSRC=%u->%u"
+ "VCAudioStream [%s] %s:%d Reconfiguring VCAudioStream: transportCount=%lu->%lu localSSRC=%u->%u"
+ "VCJitterBuffer_GetInitialRampMetrics"
+ "VCMediaQueue [%s] %s:%d Failed to recycle pending packet for mediaQueueStreamId=%u, status=%d"
+ "VCMediaStream [%s] %s:%d %@(%p) Last RTCP packet receive time:%f now:%f rtcpTimeoutEnabledTime=%f rtcpTimeoutInterval=%f. Triggering RTCP timeout"
+ "VCMediaStream [%s] %s:%d Last RTCP packet receive time:%f now:%f rtcpTimeoutEnabledTime=%f rtcpTimeoutInterval=%f. Triggering RTCP timeout"
+ "VCRC [%s] %s:%d Set feedback controlInfo [%p]: echoedSendTimestamp=%u bandwidthEstimation=%u videoBurstLoss=%u audioBurstLoss=%u videoReceivedPkts=%u audioReceivedPkts=%u totalReceivedKBytes=%u receiveQueueTarget=%u ecnECT1Count=%u ecnCECount=%u connectionStatsBlob=%u"
+ "VCRateControlSetFeedbackControlInfo"
+ "VCSoundDec [%s] %s:%d [%p] AudioConverterDispose failed, status=%d audioConv=%p"
+ "VCStringUtils_AddVTLoggingIdentifier"
+ "VCStringUtils_SetVTLoggingIdentifier"
+ "VCVideoCaptureServer [%s] %s:%d requested secondary aspectRatio=%d not applied: _avCapture=%p lacks batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:"
+ "VCVideoPlayer [%s] %s:%d VCVideoPlayer[%p] playbackClient[%p] Skipping avsync offset reporting. firstFramePresented=%d hostTimeForPlayout=%f externalSourcePlayoutTimeInSeconds=%f lastFrame.videoFrameTimeInSeconds=%f"
+ "VCVideoPlayer [%s] %s:%d VCVideoPlayer[%p] pthread_cond_timedwait_relative_np unexpected error=%d"
+ "VCVideoStreamConfig_SetVTLoggingIdentifier"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] Frame pool allocation failed, dropping packet seq=%d"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] Packet pool allocation failed, dropping packet seq=%d"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] Successfully assembled previously incomplete late frame timestamp=%u frameSequenceNumber=%u isFrameSequenceNumberValid=%d isRefreshFrame=%d hasRetransmittedPackets=%d"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] [recovery] Frame not submitted TS=%u seq=%u frameSequenceNumber=%d isFrameSequenceNumberValid=%d isRefreshFrame=%d isLTRPFrame=%d isIntraFrame=%d iLTRBits=0x%x hasRetransmittedPackets=%d isLate=%d keyFrameRequestReason=%s futureFramesSize=%u incompleteFramesSize=%u videoPacketsExpected=%u videoPacketsReceived=%u parityPacketsReceived=%u actualfecLevel=%.1f newestPreGapPacketAgeMs=%.1f"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] [recovery] Freeing frame TS=%u frameSequenceNumber=%d isFrameSequenceNumberValid=%d isLate=%d fScheduled=%d isFailedCompleteFrame=%d isLTRPFrame=%d isIntraFrame=%d hasRetransmittedPackets=%d fRecovered=%d frameFECStatus=%d"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] fNeedRefresh 0->1 reason=%s setTimeSec=%.3f isDecoderOutOfSync=%d"
+ "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] fNeedRefresh 1->0 (refresh satisfied) pendingReason=%s pendingForMs=%.1f"
+ "_AVCRateController_ReportNetworkStatistics"
+ "_VCJitterBuffer_CheckAndCloseRampMeasurement"
+ "_VCJitterBuffer_InitRampInfo"
+ "_VCJitterBuffer_MeasureRampOOO"
+ "_VCMediaQueue_DrainPendingRecyclePackets"
+ "_VideoDecoder_LogColorimetryAttachmentsChanged"
+ "_VideoPacketBuffer_SetNeedRefresh"
+ "_VideoPlayer_UpdateReportedAVSyncOffset"
+ "com.apple.AVConference.mockqrserver.forwarder"
+ "disableJitterBufferDump"
+ "disableVideoJitterBufferDump"
+ "i28@?0^{tagVCMediaPacket=iS^{OpaqueCMBlockBuffer}{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}i^v^?^{tagHANDLE}ddBBBBIIIIISIIIiIddBBBBBBBBBBiAB^{tagVCMediaPacket}}8S16S20s24"
+ "redundancyCongestionKeepHistoryRatio"
+ "vc-redundancy-controller-video-congestion-keep-history-ratio"
- " [%s] %s:%d %@ not available, falling back to basic initializer."
- " [%s] %s:%d %@(%p) %@ not available, falling back to basic initializer."
- " [%s] %s:%d %@(%p) Applying mute property for audioSessionId=%d, isMuted=%d (sessionMute=%@ _isMicrophoneMuted=%d hasActiveMicClients=%d)"
- " [%s] %s:%d %@(%p) Cannot find _latestSendKeyIndex '%@' in receive keys array of %d elements. Invalidating it..."
- " [%s] %s:%d %@(%p) Failed as Nil transcriptionProviderIdentifier passed to initialize SpeechTranslator"
- " [%s] %s:%d %@(%p) Failed to allocate delay monitor"
- " [%s] %s:%d %@(%p) Failed to create the _translatorClient for shared SpeechTranslator"
- " [%s] %s:%d %@(%p) Failed to create the _translatorClient for standalone SpeechTranslator"
- " [%s] %s:%d %@(%p) Failed to create the _translatorConfiguration for SpeechTranslator"
- " [%s] %s:%d %@(%p) Failed to create the converter. Captions will not be available with SpeechTranslator."
- " [%s] %s:%d %@(%p) Fatal error in STSpeechTranslator usage with caption operating mode not set for translator. Unexpected captionsOperatingMode=%@"
- " [%s] %s:%d %@(%p) Found _latestSendKeyIndex '%@' in send keys array of %d elements"
- " [%s] %s:%d %@(%p) Get error %@ from NWConnection with state: %d!"
- " [%s] %s:%d %@(%p) The server disconnected for the STSpeechTranslatorClient=%@"
- " [%s] %s:%d %@(%p) Translation started for STSpeechTranslatorClient=%@"
- " [%s] %s:%d %@(%p) Translation stopped for STSpeechTranslatorClient=%@ with error=%@"
- " [%s] %s:%d %@(%p) VCAudioCaptionsSpeechTranslator-init FAILED"
- " [%s] %s:%d %@(%p) Video frame is too old and modulated timestamp rolled backward – dropping frame. modulatedTimestamp=%u, frameTimeInSec=%f, rtpTimestampRate=%u"
- " [%s] %s:%d %@(%p) [FTDC] primaryUID=%@, secondaryUID=%@, aspectRatio=%d, dualCaptureEnabled=%d"
- " [%s] %s:%d %@(%p) _transcriptionTimes is nil"
- " [%s] %s:%d %@(%p) error zero sampleBufferSize requested"
- " [%s] %s:%d %@(%p) reportAndReset returned nil"
- " [%s] %s:%d %@(%p) setMicrophoneMuted=%d"
- " [%s] %s:%d %@(%p) skipping IFD stats: monitor=%p, param=%p"
- " [%s] %s:%d %@(%p) stopped a timer=%p that was already stop"
- " [%s] %s:%d @:@ VCAudioCaptionsSpeechTranslator-init Finished instance=%p Succeeded with frameworkType=%d"
- " [%s] %s:%d @:@ VCAudioCaptionsSpeechTranslator-init instance=%p"
- " [%s] %s:%d Applying mute property for audioSessionId=%d, isMuted=%d (sessionMute=%@ _isMicrophoneMuted=%d hasActiveMicClients=%d)"
- " [%s] %s:%d Cannot find _latestSendKeyIndex '%@' in receive keys array of %d elements. Invalidating it..."
- " [%s] %s:%d Failed as Nil transcriptionProviderIdentifier passed to initialize SpeechTranslator"
- " [%s] %s:%d Failed to allocate delay monitor"
- " [%s] %s:%d Failed to create the _translatorClient for shared SpeechTranslator"
- " [%s] %s:%d Failed to create the _translatorClient for standalone SpeechTranslator"
- " [%s] %s:%d Failed to create the _translatorConfiguration for SpeechTranslator"
- " [%s] %s:%d Failed to create the converter. Captions will not be available with SpeechTranslator."
- " [%s] %s:%d Failed to register stream group for capture source ID=%d"
- " [%s] %s:%d Failed to softlink VCSpeechTranslation framework and could not copy over error=%s, path=%s"
- " [%s] %s:%d Failed to softlink VCSpeechTranslation framework and could not find any error, path=%s"
- " [%s] %s:%d Failed to softlink VCSpeechTranslation framework with error=%s path=%s"
- " [%s] %s:%d Failed to start SpeechTranslation server with error=%@"
- " [%s] %s:%d Failed to start translator client. SpeechTranslator error=%@"
- " [%s] %s:%d Fatal error in STSpeechTranslator usage with caption operating mode not set for translator. Unexpected captionsOperatingMode=%@"
- " [%s] %s:%d Found _latestSendKeyIndex '%@' in send keys array of %d elements"
- " [%s] %s:%d Get error %@ from NWConnection with state: %d!"
- " [%s] %s:%d Get error %@ from nw connection with state: %d!"
- " [%s] %s:%d NOT hosting AudioTranscriptionAnalysis server."
- " [%s] %s:%d NOT hosting speech translation server."
- " [%s] %s:%d Redundancy unfrozen reason=%d isNetworkCongested=%d _offChannelTimeRatio=%2.3f"
- " [%s] %s:%d SRTP verification failed (%X)"
- " [%s] %s:%d Started SpeechTranslation server"
- " [%s] %s:%d SwitchManager: Non-seed build - using master local switch: %08X"
- " [%s] %s:%d The server disconnected for the STSpeechTranslatorClient=%@"
- " [%s] %s:%d Translation started for STSpeechTranslatorClient=%@"
- " [%s] %s:%d Translation stopped for STSpeechTranslatorClient=%@ with error=%@"
- " [%s] %s:%d Unexpected streamGroupID=%s"
- " [%s] %s:%d VCAudioCaptionsSpeechTranslator-init FAILED"
- " [%s] %s:%d VTCompressionSessionCreate failed (%d)"
- " [%s] %s:%d Video frame is too old and modulated timestamp rolled backward – dropping frame. modulatedTimestamp=%u, frameTimeInSec=%f, rtpTimestampRate=%u"
- " [%s] %s:%d Waiting for packet on socket=%d..."
- " [%s] %s:%d [%p] VideoTransmitter_CreateHandle wMTU[%d] bIsIPv6[%d] reinitEnabled[%s]"
- " [%s] %s:%d [FTDC] primaryUID=%@, secondaryUID=%@, aspectRatio=%d, dualCaptureEnabled=%d"
- " [%s] %s:%d _transcriptionTimes is nil"
- " [%s] %s:%d error zero sampleBufferSize requested"
- " [%s] %s:%d eventInfo has IDSDataChannelError, ERROR = %@"
- " [%s] %s:%d recvmsg failed for socket=%d"
- " [%s] %s:%d reportAndReset returned nil"
- " [%s] %s:%d setMicrophoneMuted=%d"
- " [%s] %s:%d skipping IFD stats: monitor=%p, param=%p"
- " [%s] %s:%d stopped a timer=%p that was already stop"
- "-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]_block_invoke"
- "-[VCAudioCaptionsSpeechTranslator addToCaptionTasksWithError:]"
- "-[VCAudioCaptionsSpeechTranslator client:didReceiveTranscriptionResult:]"
- "-[VCAudioCaptionsSpeechTranslator client:didReceiveTranslationResult:]"
- "-[VCAudioCaptionsSpeechTranslator client:didStopTranslationWithError:]"
- "-[VCAudioCaptionsSpeechTranslator dealloc]"
- "-[VCAudioCaptionsSpeechTranslator destroyCaptions]"
- "-[VCAudioCaptionsSpeechTranslator initWithDelegate:isLocal:taskIdentifier:reportingAgent:]"
- "-[VCAudioCaptionsSpeechTranslator packageAndSendTranscribedString:withTask:]"
- "-[VCAudioCaptionsSpeechTranslator packageAndSendTranslatedString:withTask:]"
- "-[VCAudioCaptionsSpeechTranslator pushSamples:numSamples:hostTime:]"
- "-[VCAudioCaptionsSpeechTranslator serverDidDisconnectForClient:]"
- "-[VCAudioCaptionsSpeechTranslator setUpCaptionsWithError:]"
- "-[VCAudioCaptionsSpeechTranslator setupTranslatorSharedWithError:]"
- "-[VCAudioCaptionsSpeechTranslator setupTranslatorStandaloneWithError:]"
- "-[VCAudioCaptionsSpeechTranslator setupTranslatorStandaloneWithError:]_block_invoke"
- "-[VCAudioCaptionsSpeechTranslator shouldPushSamples]"
- "-[VCAudioCaptionsSpeechTranslator startCaptionsWithError:]"
- "-[VCAudioCaptionsSpeechTranslator stopCaptions]"
- "-[VCAudioCaptionsSpeechTranslator translationDidStartForClient:]"
- "-[VCAudioSessionAVAS isInputSupported]"
- "-[VCDispatchTimer stop]"
- "-[VCTransportSessionMultiLink handleListenerEvents:error:]"
- "-[VCVideoStreamReceiver gatherInterframeDelayStats:]"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/Captions/VCAudioCaptionsSpeechTranslator.m"
- "/System/Library/PrivateFrameworks/SpeechTranslation.framework/SpeechTranslation"
- "2235.63.1.2"
- "<%s:%p> Token (%d) Link (%d): %s <-> %s (%s, %s), priority %d, uplink bitrate cap (%u), downlink bitrate cap (%u), uplink audio only bitrate cap = (%u), uplink OneToOne bitrate cap = (%u), isLocalConstrained (%d), isRemoteConstrained (%d), isLocalExpensive (%d) isRemoteExpensive (%d) isLocalDelegated (%d) isRemoteDelegated (%d) isLocalUltraConstrained (%d) isRemoteUltraConstrained (%d) isVirtualRelayLink (%d) reportingIPVersion(%d) TransportLayerEncryption=%d relayProtocolStackDescrption(%@) channelDataBaseProtocolStackDescription(%@) _isHopByHopEncryptionSupported=%d"
- "@:@ VCAudioCaptionsSpeechTranslator-init"
- "@:@ VCAudioCaptionsSpeechTranslator-init Finished"
- "AudioCallTranslation"
- "Fatal error in STSpeechTranslator usage. In SpeechTranslator module but translator operating mode is not set, captionsOperatingMode=%@"
- "HostAudioTranscriptionAnalysisServer"
- "STServerStart"
- "STSpeechTranslatorClient"
- "STSpeechTranslatorConfiguration"
- "VCAudioCaptionsSpeechTranslator.m"
- "VCAudioStream [%s] %s:%d %@(%p) Reconfiguring VCAudioStream with a different number of transports."
- "VCAudioStream [%s] %s:%d Reconfiguring VCAudioStream with a different number of transports."
- "VCFeatureFlagManager: HostAudioTranscriptionAnalysisServer=%d"
- "VCFeatureFlagManager: HostSpeechTranslationServer=%d (audioFlag=%d, videoFlag=%d)"
- "VCMediaStream [%s] %s:%d %@(%p) Last RTCP packet receive time:%f now:%f"
- "VCMediaStream [%s] %s:%d Last RTCP packet receive time:%f now:%f"
- "VCSpeechTranslation_STSpeechTranslatorClientClass"
- "VCSpeechTranslation_STSpeechTranslatorConfigurationClass"
- "VCSpeechTranslation_StartServer"
- "VCVideoCaptureServer [%s] %s:%d requested secondary aspectRatio=%d not applied: _avCapture=%p lacks batchSetCameraUIDsPrimary:secondary:aspectRatio:"
- "VideoCallTranslation"
- "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] Received NULL frame"
- "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] Successfully assembled previously incomplete late frame timestamp=%u frameSequenceNumber=%u isRefreshFrame=%d hasRetransmittedPackets=%d"
- "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] [recovery] Frame not submitted TS=%u seq=%u frameSequenceNumber=%d isRefreshFrame=%d isLTRPFrame=%d isIntraFrame=%d iLTRBits=0x%x hasRetransmittedPackets=%d isLate=%d keyFrameRequestReason=%s futureFramesSize=%u incompleteFramesSize=%u"
- "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] [recovery] Freeing frame TS=%u frameSequenceNumber=%d isLate=%d fScheduled=%d isFailedCompleteFrame=%d isLTRPFrame=%d isIntraFrame=%d hasRetransmittedPackets=%d"
- "_VCSpeechTranslation_LibraryHandle"
- "_VCSpeechTranslation_LibraryHandle_block_invoke"
- "enableInterframeDelay"
- "hostAudioTranscriptionAnalysisServer"
- "hostSpeechTranslationServer"
- "i28@?0^{tagVCMediaPacket=iS^{OpaqueCMBlockBuffer}{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}i^v^?^{tagHANDLE}ddBBBBIIIIISIIIiIddBBBBBBBBBBi^{tagVCMediaPacket}}8S16S20s24"
```
