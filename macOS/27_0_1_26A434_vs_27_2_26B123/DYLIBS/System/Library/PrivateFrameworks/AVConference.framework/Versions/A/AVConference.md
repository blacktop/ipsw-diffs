## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/Versions/A/AVConference`

```diff

-2235.63.5.2.0
-  __TEXT.__text: 0x7c8d98
+2260.15.1.0.0
+  __TEXT.__text: 0x7cf584
   __TEXT.__realtime: 0xea4
-  __TEXT.__objc_methlist: 0x39ec8
-  __TEXT.__const: 0x184e8
-  __TEXT.__cstring: 0x9b912
-  __TEXT.__oslogstring: 0x140e5a
-  __TEXT.__gcc_except_tab: 0x3188
+  __TEXT.__objc_methlist: 0x3a090
+  __TEXT.__const: 0x184a8
+  __TEXT.__cstring: 0x9bd3c
+  __TEXT.__oslogstring: 0x143de9
+  __TEXT.__gcc_except_tab: 0x326c
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x12578
+  __TEXT.__unwind_info: 0x125e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3ec8
-  __DATA_CONST.__objc_classlist: 0x14a8
+  __DATA_CONST.__const: 0x3eb8
+  __DATA_CONST.__objc_classlist: 0x14a0
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x510
+  __DATA_CONST.__objc_protolist: 0x508
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x184d0
+  __DATA_CONST.__objc_selrefs: 0x18630
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA_CONST.__objc_superrefs: 0x1248
+  __DATA_CONST.__objc_superrefs: 0x1240
   __DATA_CONST.__objc_arraydata: 0x2790
-  __DATA_CONST.__got: 0x1b68
-  __AUTH_CONST.__const: 0x8a58
-  __AUTH_CONST.__cfstring: 0x290e0
-  __AUTH_CONST.__objc_const: 0x6c678
+  __DATA_CONST.__got: 0x1b08
+  __AUTH_CONST.__const: 0x8a08
+  __AUTH_CONST.__cfstring: 0x292a0
+  __AUTH_CONST.__objc_const: 0x6c908
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x4e00
   __AUTH_CONST.__objc_arrayobj: 0x1d58
+  __AUTH_CONST.__objc_doubleobj: 0x210
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__objc_doubleobj: 0x200
   __AUTH_CONST.__objc_dictobj: 0x2d0
-  __AUTH_CONST.__auth_got: 0x2b78
+  __AUTH_CONST.__auth_got: 0x2ba8
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x140
-  __AUTH.__data: 0xc8
-  __DATA.__objc_ivar: 0x7678
-  __DATA.__data: 0x7e50
-  __DATA.__bss: 0x9b8
+  __AUTH.__data: 0x8
+  __DATA.__objc_ivar: 0x76e0
+  __DATA.__data: 0x1e20
+  __DATA.__bss: 0xad8
   __DATA.__common: 0x9
-  __DATA_DIRTY.__objc_data: 0xcd50
-  __DATA_DIRTY.__data: 0x428
-  __DATA_DIRTY.__bss: 0x978
+  __DATA_DIRTY.__objc_data: 0xcd00
+  __DATA_DIRTY.__data: 0x6420
+  __DATA_DIRTY.__bss: 0x7e8
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35333
-  Symbols:   54513
-  CStrings:  33326
+  Functions: 35385
+  Symbols:   54612
+  CStrings:  33447
 
Symbols:
+ +[VCAVFoundationCapture isZoomSupportedForCaptureDevice:captureSource:]
+ +[VCAudioToolboxAudioComponentMock activeInstanceCount]
+ +[VCAudioToolboxAudioComponentMock isMockingSessionActive]
+ +[VCHardwareSettings supportsClientPreviewPresentationOrientation]
+ +[VCMediaNegotiationBlobV2StreamGroup(Utils) homeKitCameraDefaultsForStreamGroupCamera:]
+ +[VideoUtil dualCameraPrimary1280SquareEncodingSize]
+ -[AVCPreviewCameraSession setPreviewPresentationOrientation:]
+ -[AVConferencePreview setPreviewPresentationOrientation:]
+ -[CannedEncodedVideoCapture reset]
+ -[CannedRawVideoCapture reset]
+ -[VCAVFoundationCapture anyCameraConnectionEnabled]
+ -[VCAVFoundationCapture applyDualCaptureResolutionToPrimaryCamera]
+ -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:hasSecondary:]
+ -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:]
+ -[VCAVFoundationCapture bothCameraConnectionsDisabled]
+ -[VCAVFoundationCapture clearPreviewPresentationOrientation]
+ -[VCAVFoundationCapture clearRemotePresentationOrientation]
+ -[VCAVFoundationCapture initWithCaptureServer:protocolFunctions:width:height:frameRate:videoSourceToken:cinematicFramingEnabled:videoOrientation:capturePixelFormat:zoomFactor:remoteSupportsFullScreenReceive:videoPresentationOrientation:hasVideoPresentationOrientation:previewPresentationOrientation:hasPreviewPresentationOrientation:]
+ -[VCAVFoundationCapture isClientPreviewPresentationOrientationGoverning]
+ -[VCAVFoundationCapture secondaryCameraRequestSizeForAspectRatio:]
+ -[VCAVFoundationCapture setPreviewPresentationOrientation:]
+ -[VCAVFoundationCapture updateCameraZoomCapabilityForCaptureDeviceInput:captureSource:]
+ -[VCAVFoundationCapture updateDeviceOrientationMatchesReceiver:]
+ -[VCAVFoundationCapture vendableAspectRatio:landscapeOrderedAlternate:captureFormat:clientPreviewGoverns:]
+ -[VCAudioStream reportingAudioJBRampStats]
+ -[VCAudioStreamSendGroupConfig enableSyncGroupReferenceTimestamp]
+ -[VCAudioStreamSendGroupConfig setEnableSyncGroupReferenceTimestamp:]
+ -[VCAudioToolboxAudioComponentMock autorelease]
+ -[VCAudioToolboxAudioComponentMock release]
+ -[VCAudioToolboxAudioComponentMock retainCount]
+ -[VCAudioToolboxAudioComponentMock retain]
+ -[VCAudioTransmitterConfig setShouldCapBitrateForWatchRelay:]
+ -[VCAudioTransmitterConfig shouldCapBitrateForWatchRelay]
+ -[VCCallSession isRemoteWatchRelayDeviceWithDeviceType:]
+ -[VCConnectionHealthMonitor resetStallDetectionStateAfterMonitoringResumed]
+ -[VCCoreAudio_AudioUnitMock autorelease]
+ -[VCCoreAudio_AudioUnitMock beginSession]
+ -[VCCoreAudio_AudioUnitMock endSession]
+ -[VCCoreAudio_AudioUnitMock isMockingEnabled]
+ -[VCCoreAudio_AudioUnitMock release]
+ -[VCCoreAudio_AudioUnitMock retainCount]
+ -[VCCoreAudio_AudioUnitMock retain]
+ -[VCMediaRecorder hasConfiguredWriter]
+ -[VCMediaRecorderLocal localRecordingScreenAttributesDidChange:]
+ -[VCMediaRecorderLocal updateTargetScreenAttributesFromCaptureServer]
+ -[VCMockQRServer forwardOnePacketFromListenerSocket:listenerSourceIP:listenerSourcePort:forwarderSocketList:listenerParticipantID:]
+ -[VCMockQRServer stopPacketForwarders]
+ -[VCRTPHistory dealloc]
+ -[VCRemoteVideoState participantId]
+ -[VCRemoteVideoState setParticipantId:]
+ -[VCSession clearRemotePresentationOrientationOnCaptureServer]
+ -[VCSessionPowerPolicy hasPrimaryCameraFrameRateMitigation]
+ -[VCSessionPowerPolicy hasSecondaryCameraFrameRateMitigation]
+ -[VCTransportSessionMultiLink handleListenerEvents:error:result:]
+ -[VCVideoCaptureServer applyClientPreviewPresentationOrientationArguments:]
+ -[VCVideoCaptureServer clearPreviewPresentationOrientationRequestForDiedClient:]
+ -[VCVideoCaptureServer clearRemotePresentationOrientation]
+ -[VCVideoCaptureServer copyLocalRecordingScreenAttributesForVideoAttributes:]
+ -[VCVideoCaptureServer dispatchedClearPreviewPresentationOrientationRequest]
+ -[VCVideoCaptureServer dispatchedCopyLocalRecordingScreenAttributesForVideoAttributes:]
+ -[VCVideoCaptureServer dispatchedIsClientPreviewPresentationOrientationGoverning]
+ -[VCVideoCaptureServer handleClientPreviewPresentationOrientationMessage:]
+ -[VCVideoCaptureServer notifyClientsLocalRecordingScreenAttributesDidChange]
+ -[VCVideoCaptureServer publishCameraUIDChangedForCameraUID:cameraSessionType:]
+ -[VCVideoCaptureServer setPreviewPresentationOrientation:]
+ -[VCVideoCaptureServer setPreviewPresentationOrientation:requestingClientPID:]
+ -[VCVideoStream canReuseTransportsForStreamConfigs:]
+ -[VCVideoStream expectedTransportArrayCountForStreamConfigs:]
+ -[VCVideoStream supportsMaxKeyFrameIntervalDuration]
+ -[VCVideoStream transportArrayContainsRTXTransport]
+ -[VCVideoStream transportStreamCountForStreamConfig:]
+ -[VCVideoStream willCreateRTXTransportForStreamConfig:]
+ -[VCVideoStreamSendGroupConfig enableSyncGroupReferenceTimestamp]
+ -[VCVideoStreamSendGroupConfig setEnableSyncGroupReferenceTimestamp:]
+ -[VCVideoTransmitterConfig reinitEncoderOnFrameAspectRatioChangeEnabled]
+ -[VCVideoTransmitterConfig setReinitEncoderOnFrameAspectRatioChangeEnabled:]
+ -[VCVideoTransmitterConfig setVtLoggingIdentifier:]
+ -[VCVideoTransmitterConfig vtLoggingIdentifier]
+ GCC_except_table142
+ GCC_except_table146
+ GCC_except_table148
+ GCC_except_table178
+ GCC_except_table185
+ GCC_except_table219
+ GCC_except_table231
+ GCC_except_table233
+ GCC_except_table235
+ GCC_except_table253
+ GCC_except_table287
+ GCC_except_table290
+ GCC_except_table293
+ GCC_except_table336
+ GCC_except_table374
+ GCC_except_table464
+ OBJC_IVAR_$_AVCPacketRelaySocketConnection._isMonitoring
+ OBJC_IVAR_$_AVConferencePreview._preRegistrationCameraUIDToSession
+ OBJC_IVAR_$_AVConferencePreview._setPrimarySecondaryInFlightCount
+ OBJC_IVAR_$_VCAVFoundationCapture._dualCamPrimaryPrefers1280SquareCapture
+ OBJC_IVAR_$_VCAVFoundationCapture._dualCaptureRear1440x1080
+ OBJC_IVAR_$_VCAVFoundationCapture._hasPreviewPresentationOrientation
+ OBJC_IVAR_$_VCAVFoundationCapture._hasVideoPresentationOrientation
+ OBJC_IVAR_$_VCAVFoundationCapture._lastAttachPerFrameAR
+ OBJC_IVAR_$_VCAVFoundationCapture._previewPresentationOrientation
+ OBJC_IVAR_$_VCAudioStreamSendGroup._enableSyncGroupReferenceTimestamp
+ OBJC_IVAR_$_VCAudioStreamSendGroupConfig._enableSyncGroupReferenceTimestamp
+ OBJC_IVAR_$_VCAudioToolboxAudioComponentMock._activeInstances
+ OBJC_IVAR_$_VCAudioToolboxAudioComponentMock._instancesLock
+ OBJC_IVAR_$_VCAudioTransmitter._shouldCapBitrateForWatchRelay
+ OBJC_IVAR_$_VCAudioTransmitterConfig._shouldCapBitrateForWatchRelay
+ OBJC_IVAR_$_VCCoreAudio_AudioUnitMock._isImplicitPreferenceSession
+ OBJC_IVAR_$_VCMockIDSDatagramChannel._enqueueLock
+ OBJC_IVAR_$_VCMockIDSDatagramChannel._queueLock
+ OBJC_IVAR_$_VCMockQRServer._forwarderQueue
+ OBJC_IVAR_$_VCMockQRServer._forwarderSources
+ OBJC_IVAR_$_VCRedundancyControlAlgorithmVideo._congestionKeepHistoryRatio
+ OBJC_IVAR_$_VCRedundancyControlAlgorithmVideo._feedbackHistoryMaxLength
+ OBJC_IVAR_$_VCRedundancyControlAlgorithmVideo._freezeStartTime
+ OBJC_IVAR_$_VCRemoteVideoState._participantId
+ OBJC_IVAR_$_VCSession._remoteParticipantsMapLock
+ OBJC_IVAR_$_VCVideoCaptureServer._hasPreviewPresentationOrientationRequest
+ OBJC_IVAR_$_VCVideoCaptureServer._hasRemotePresentationOrientation
+ OBJC_IVAR_$_VCVideoCaptureServer._previewPresentationOrientationRequest
+ OBJC_IVAR_$_VCVideoCaptureServer._previewPresentationOrientationRequestPID
+ OBJC_IVAR_$_VCVideoCaptureServer._remotePresentationOrientation
+ OBJC_IVAR_$_VCVideoStreamRateAdaptationFeedbackOnly._rateControlFeedbackDrained
+ OBJC_IVAR_$_VCVideoStreamReceiver._vtLoggingIdentifier
+ OBJC_IVAR_$_VCVideoStreamSendGroup._enableSyncGroupReferenceTimestamp
+ OBJC_IVAR_$_VCVideoStreamSendGroup._hasModulatedTimestampBaseline
+ OBJC_IVAR_$_VCVideoStreamSendGroup._lastModulatedTimestamp
+ OBJC_IVAR_$_VCVideoStreamSendGroupConfig._enableSyncGroupReferenceTimestamp
+ OBJC_IVAR_$_VCVideoStreamTransmitter._vtLoggingIdentifier
+ OBJC_IVAR_$_VCVideoTransmitterConfig._reinitEncoderOnFrameAspectRatioChangeEnabled
+ OBJC_IVAR_$_VCVideoTransmitterConfig._vtLoggingIdentifier
+ VCMediaRecorderHistory_HasConfiguredWriter
+ VCVideoStreamConfig_SetVTLoggingIdentifier
+ _AVErrorDeviceKey
+ _CVImageBufferGetColorSpace
+ _CVPixelBufferPoolFlush
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _VCConnectionIDS_SetLocalLinkTechnology
+ _VCJitterBuffer_GetInitialRampMetrics
+ _VCMediaQueue_RecyclePacket
+ _VCMediaRecorderHistory_HasConfiguredWriter
+ _VCRedundancyControllerVideoCongestionKeepHistoryRatio
+ _VCStringUtils_AddVTLoggingIdentifier
+ _VCStringUtils_CFStringNotEqual
+ _VCStringUtils_SetVTLoggingIdentifier
+ _VCVideoCaptureServer_ClientPIDFromArguments
+ _VCVideoStreamConfig_SetVTLoggingIdentifier
+ _VTCompressionSessionCreateWithOptions
+ __44-[VCControlChannelMultiWay lastUsedMKIBytes]_block_invoke
+ __47-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_6
+ __62-[VCVideoStreamRateAdaptationFeedbackOnly startFeedbackSource]_block_invoke
+ __OBJC_$_INSTANCE_VARIABLES_VCAudioToolboxAudioComponentMock
+ __VCMediaQueue_DrainPendingRecyclePackets
+ __VideoPacketBuffer_SetNeedRefresh
+ ___135-[VCMockQRServer startPacketForwarderWithListenerSocket:listenerSourceIP:listenerSourcePort:forwarderSocketList:listenerParticipantID:]_block_invoke
+ ___38-[VCMockQRServer stopPacketForwarders]_block_invoke
+ ___44-[VCControlChannelMultiWay lastUsedMKIBytes]_block_invoke
+ ___57-[AVConferencePreview setPreviewPresentationOrientation:]_block_invoke
+ ___58-[VCVideoCaptureServer clearRemotePresentationOrientation]_block_invoke
+ ___59-[VCAVFoundationCapture clearRemotePresentationOrientation]_block_invoke
+ ___59-[VCAVFoundationCapture setPreviewPresentationOrientation:]_block_invoke
+ ___60-[VCAVFoundationCapture clearPreviewPresentationOrientation]_block_invoke
+ ___61-[AVCPreviewCameraSession setPreviewPresentationOrientation:]_block_invoke
+ ___66+[VCHardwareSettings supportsClientPreviewPresentationOrientation]_block_invoke
+ ___76-[VCVideoCaptureServer notifyClientsLocalRecordingScreenAttributesDidChange]_block_invoke
+ ___77-[VCVideoCaptureServer copyLocalRecordingScreenAttributesForVideoAttributes:]_block_invoke
+ ___78-[VCVideoCaptureServer publishCameraUIDChangedForCameraUID:cameraSessionType:]_block_invoke
+ ___78-[VCVideoCaptureServer setPreviewPresentationOrientation:requestingClientPID:]_block_invoke
+ ___80-[VCVideoCaptureServer clearPreviewPresentationOrientationRequestForDiedClient:]_block_invoke
+ ___86-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:]_block_invoke
+ ___VCMediaRecorderHistory_HasConfiguredWriter_block_invoke
+ ___block_descriptor_40_e8_32o_e232_v20?0i8^{FigRemoteOperation=iiQ^{__CFString}(?={?=^{__CFDictionary}^{__CFDictionary}}{?=^v^{__IOSurface}^{__IOSurface}}{?=^{opaqueCMSampleBuffer}Q^{__CFArray}}{?=^{opaqueCMFormatDescription}}{?=q^{opaqueCMFormatDescription}^IQ})}12l
+ ___block_descriptor_61_e8_32o40o48o_e5_v8?0l
+ _kForwarderQueueSpecificKey
+ _kVCXPCConnectionTimeoutQueueSpecificKey
+ _kVTCompressionSessionOption_LoggingIdentifier
+ _kVTDecompressionSessionOption_LoggingIdentifier
+ _nw_error_get_error_domain
+ _objc_getAssociatedObject
+ _objc_msgSend$activeInstanceCount
+ _objc_msgSend$anyCameraConnectionEnabled
+ _objc_msgSend$applyClientPreviewPresentationOrientationArguments:
+ _objc_msgSend$applyDualCaptureResolutionToPrimaryCamera
+ _objc_msgSend$batchSetCameraUIDsPrimary:secondary:hasSecondary:
+ _objc_msgSend$batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:
+ _objc_msgSend$bothCameraConnectionsDisabled
+ _objc_msgSend$canReuseTransportsForStreamConfigs:
+ _objc_msgSend$clearPreviewPresentationOrientation
+ _objc_msgSend$clearPreviewPresentationOrientationRequestForDiedClient:
+ _objc_msgSend$clearRemotePresentationOrientation
+ _objc_msgSend$clearRemotePresentationOrientationOnCaptureServer
+ _objc_msgSend$copyLocalRecordingScreenAttributesForVideoAttributes:
+ _objc_msgSend$dispatchedClearPreviewPresentationOrientationRequest
+ _objc_msgSend$dispatchedCopyLocalRecordingScreenAttributesForVideoAttributes:
+ _objc_msgSend$dispatchedIsClientPreviewPresentationOrientationGoverning
+ _objc_msgSend$dualCameraPrimary1280SquareEncodingSize
+ _objc_msgSend$enableSyncGroupReferenceTimestamp
+ _objc_msgSend$expectedTransportArrayCountForStreamConfigs:
+ _objc_msgSend$forwardOnePacketFromListenerSocket:listenerSourceIP:listenerSourcePort:forwarderSocketList:listenerParticipantID:
+ _objc_msgSend$handleClientPreviewPresentationOrientationMessage:
+ _objc_msgSend$handleListenerEvents:error:result:
+ _objc_msgSend$hasConfiguredWriter
+ _objc_msgSend$hasPrimaryCameraFrameRateMitigation
+ _objc_msgSend$hasSecondaryCameraFrameRateMitigation
+ _objc_msgSend$homeKitCameraDefaultsForStreamGroupCamera:
+ _objc_msgSend$initWithCaptureServer:protocolFunctions:width:height:frameRate:videoSourceToken:cinematicFramingEnabled:videoOrientation:capturePixelFormat:zoomFactor:remoteSupportsFullScreenReceive:videoPresentationOrientation:hasVideoPresentationOrientation:previewPresentationOrientation:hasPreviewPresentationOrientation:
+ _objc_msgSend$isClientPreviewPresentationOrientationGoverning
+ _objc_msgSend$isMockingEnabled
+ _objc_msgSend$isMockingSessionActive
+ _objc_msgSend$isRemoteWatchRelayDeviceWithDeviceType:
+ _objc_msgSend$isZoomSupportedForCaptureDevice:captureSource:
+ _objc_msgSend$localRecordingScreenAttributesDidChange:
+ _objc_msgSend$notifyClientsLocalRecordingScreenAttributesDidChange
+ _objc_msgSend$publishCameraUIDChangedForCameraUID:cameraSessionType:
+ _objc_msgSend$reinitEncoderOnFrameAspectRatioChangeEnabled
+ _objc_msgSend$reportingAudioJBRampStats
+ _objc_msgSend$resetStallDetectionStateAfterMonitoringResumed
+ _objc_msgSend$secondaryCameraRequestSizeForAspectRatio:
+ _objc_msgSend$setDictionary:
+ _objc_msgSend$setEnableSyncGroupReferenceTimestamp:
+ _objc_msgSend$setPreviewPresentationOrientation:
+ _objc_msgSend$setPreviewPresentationOrientation:requestingClientPID:
+ _objc_msgSend$setReinitEncoderOnFrameAspectRatioChangeEnabled:
+ _objc_msgSend$setShouldCapBitrateForWatchRelay:
+ _objc_msgSend$setVtLoggingIdentifier:
+ _objc_msgSend$shouldCapBitrateForWatchRelay
+ _objc_msgSend$stopPacketForwarders
+ _objc_msgSend$supportsClientPreviewPresentationOrientation
+ _objc_msgSend$supportsMaxKeyFrameIntervalDuration
+ _objc_msgSend$transportArrayContainsRTXTransport
+ _objc_msgSend$transportStreamCountForStreamConfig:
+ _objc_msgSend$updateCameraZoomCapabilityForCaptureDeviceInput:captureSource:
+ _objc_msgSend$updateDeviceOrientationMatchesReceiver:
+ _objc_msgSend$updateTargetScreenAttributesFromCaptureServer
+ _objc_msgSend$vendableAspectRatio:landscapeOrderedAlternate:captureFormat:clientPreviewGoverns:
+ _objc_msgSend$vtLoggingIdentifier
+ _objc_msgSend$willCreateRTXTransportForStreamConfig:
+ _objc_setAssociatedObject
+ _xpc_copy_description
+ supportsClientPreviewPresentationOrientation.onceToken
+ supportsClientPreviewPresentationOrientation.resolved
- +[VCHardwareSettings supportsSquarePreviewCapture]
- -[AVCCaptionsClient initWithDelegate:translatorIdentifier:]
- -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:]
- -[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]
- -[VCAVFoundationCapture initWithCaptureServer:protocolFunctions:width:height:frameRate:videoSourceToken:cinematicFramingEnabled:videoOrientation:capturePixelFormat:zoomFactor:remoteSupportsFullScreenReceive:videoPresentationOrientation:]
- -[VCAVFoundationCapture squarePreviewAdjustedRequestSizeForCaptureSize:]
- -[VCAVFoundationCapture updateCameraZoomCapabilityForCaptureDeviceInput:]
- -[VCAVFoundationCapture updateDeviceOrientationMatchesReceiver:videoPresentationOrientation:]
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
- -[VCAudioToolboxAudioComponentMock dealloc]
- -[VCCoreAudio_AudioUnitMock dealloc]
- -[VCTransportSessionMultiLink handleListenerEvents:error:]
- -[VCVideoCaptureServer copyLocalScreenAttributesForVideoAttributes:]
- -[VCVideoStreamReceiver gatherInterframeDelayStats:]
- GCC_except_table121
- GCC_except_table136
- GCC_except_table145
- GCC_except_table176
- GCC_except_table184
- GCC_except_table216
- GCC_except_table218
- GCC_except_table220
- GCC_except_table221
- GCC_except_table238
- GCC_except_table263
- GCC_except_table272
- GCC_except_table275
- GCC_except_table317
- GCC_except_table373
- GCC_except_table463
- OBJC_IVAR_$_VCAVFoundationCapture._clientRequestedSize
- OBJC_IVAR_$_VCAVFoundationCapture._configuringForCapture
- OBJC_IVAR_$_VCAVFoundationCapture._squarePreviewOverrideActive
- OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._currentSourceUpdateNumber
- OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._currentTranslatedUpdateNumber
- OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._isStarted
- OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._transcriptionTimes
- OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._translatorClient
- OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._translatorConfiguration
- OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._translatorStartDuration
- OBJC_IVAR_$_VCAudioCaptionsSpeechTranslator._translatorStartTime
- OBJC_IVAR_$_VCPowerManager._forceDisableThermal
- OBJC_IVAR_$_VCVideoStreamReceiver._interframeDelayMonitor
- VCFeatureFlagManager_HostAudioTranscriptionAnalysisServer
- VCFeatureFlagManager_HostAudioTranscriptionAnalysisServer.flag
- VCFeatureFlagManager_HostAudioTranscriptionAnalysisServer.onceToken
- VCFeatureFlagManager_HostSpeechTranslationServer
- VCFeatureFlagManager_HostSpeechTranslationServer.audioFlag
- VCFeatureFlagManager_HostSpeechTranslationServer.onceToken
- VCFeatureFlagManager_HostSpeechTranslationServer.videoFlag
- VCSpeechTranslation_STSpeechTranslatorClientClass
- VCSpeechTranslation_STSpeechTranslatorClientClass.onceToken
- VCSpeechTranslation_STSpeechTranslatorClientClass.speechTranslatorClientClass
- VCSpeechTranslation_STSpeechTranslatorConfigurationClass
- VCSpeechTranslation_STSpeechTranslatorConfigurationClass.onceToken
- VCSpeechTranslation_STSpeechTranslatorConfigurationClass.speechTranslatorConfigurationClass
- _OBJC_CLASS_$_VCAudioCaptionsSpeechTranslator
- _OBJC_METACLASS_$_VCAudioCaptionsSpeechTranslator
- _VCAudioUnit_BasebandInstance
- _VCAudioUnit_DefaultOutputInstance
- _VCAudioUnit_RemoteIOInstance
- _VCAudioUnit_SystemAudioInstance
- _VCAudioUnit_VoiceProcessorInstance
- _VCFeatureFlagManager_HostAudioTranscriptionAnalysisServer
- _VCFeatureFlagManager_HostSpeechTranslationServer
- _VCSpeechTranslation_LibraryHandle
- _VCSpeechTranslation_LibraryHandle.onceToken
- _VCSpeechTranslation_STSpeechTranslatorClientClass
- _VCSpeechTranslation_STSpeechTranslatorConfigurationClass
- _VCSpeechTranslation_StartServer
- _VCVideoStreamSendGroup_SecondaryCameraTransfer
- _VCVirtualAVCaptureDevice_OnMediaSample
- _VideoPacketBuffer_StartTrackingEvictedFrameStats
- __70-[VCAudioCaptionsSpeechTranslator setupTranslatorStandaloneWithError:]_block_invoke
- __78-[VCVideoCaptureServer dispatchedSetCaptureCameraWithToken:cameraSessionType:]_block_invoke
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
- __VCVideoStreamSendGroup_SecondaryCameraTransfer
- ___30-[VCSession participantForID:]_block_invoke
- ___39-[VCMockQRServer startPacketForwarders]_block_invoke
- ___50+[VCHardwareSettings supportsSquarePreviewCapture]_block_invoke
- ___70-[VCAudioCaptionsSpeechTranslator client:didReceiveTranslationResult:]_block_invoke
- ___70-[VCAudioCaptionsSpeechTranslator setupTranslatorStandaloneWithError:]_block_invoke
- ___72-[VCAudioCaptionsSpeechTranslator client:didReceiveTranscriptionResult:]_block_invoke
- ___73-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]_block_invoke
- ___VCFeatureFlagManager_HostAudioTranscriptionAnalysisServer_block_invoke
- ___VCFeatureFlagManager_HostSpeechTranslationServer_block_invoke
- ___VCSpeechTranslation_STSpeechTranslatorClientClass_block_invoke
- ___VCSpeechTranslation_STSpeechTranslatorConfigurationClass_block_invoke
- ____VCSpeechTranslation_LibraryHandle_block_invoke
- ___block_descriptor_40_e8_32o_e229_v20?0i8^{FigRemoteOperation=iiQ^{__CFString}(?={?=^{__CFDictionary}^{__CFDictionary}}{?=^v^{__IOSurface}^{__IOSurface}}{?=^{opaqueCMSampleBuffer}Q^{__CFArray}}{?=^{opaqueCMFormatDescription}}{?=q^{opaqueCMFormatDescription}})}12l
- __audioComponentMockLock
- __audioUnitMockLock
- __weakAudioComponentMockInstance
- __weakAudioUnitMockInstance
- _objc_loadWeakRetained
- _objc_msgSend$batchSetCameraUIDsPrimary:secondary:
- _objc_msgSend$batchSetCameraUIDsPrimary:secondary:aspectRatio:
- _objc_msgSend$copyLocalScreenAttributesForVideoAttributes:
- _objc_msgSend$handleListenerEvents:error:
- _objc_msgSend$initWithCaptureServer:protocolFunctions:width:height:frameRate:videoSourceToken:cinematicFramingEnabled:videoOrientation:capturePixelFormat:zoomFactor:remoteSupportsFullScreenReceive:videoPresentationOrientation:
- _objc_msgSend$initWithDelegate:translatorIdentifier:direction:reportingSamplingUUID:
- _objc_msgSend$initWithSourceLocale:targetLocale:
- _objc_msgSend$initWithSourceLocale:targetLocale:omitTranslatedAudio:offlineMTModel:taskHint:
- _objc_msgSend$initWithTranslatorIdentifier:delegate:delegateQueue:
- _objc_msgSend$instancesRespondToSelector:
- _objc_msgSend$setOmitTranslatedAudio:
- _objc_msgSend$setProduceAudio:
- _objc_msgSend$squarePreviewAdjustedRequestSizeForCaptureSize:
- _objc_msgSend$supportsSquarePreviewCapture
- _objc_msgSend$translatorIdentifier
- _objc_msgSend$updateCameraZoomCapabilityForCaptureDeviceInput:
- _objc_msgSend$updateDeviceOrientationMatchesReceiver:videoPresentationOrientation:
- supportsSquarePreviewCapture.onceToken
- supportsSquarePreviewCapture.resolved
CStrings:
+ " [%s] %s:%d %@(%p) Capturing first modulatedTimestamp=%u baseline, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d %@(%p) Failed to allocate forwarder sources"
+ " [%s] %s:%d %@(%p) Failed to allocate inter frame delay monitor"
+ " [%s] %s:%d %@(%p) Failed to allocate socket list"
+ " [%s] %s:%d %@(%p) Failed to allocate the active instances set"
+ " [%s] %s:%d %@(%p) Failed to create forwarder queue"
+ " [%s] %s:%d %@(%p) Failed to create read source for socket=%d (participant=%@)"
+ " [%s] %s:%d %@(%p) Failed to create sockets from configuration"
+ " [%s] %s:%d %@(%p) Failed to extract RTP information from video packet for participant=%@"
+ " [%s] %s:%d %@(%p) Failed to find datagram channel for participant=%@, skipping packet"
+ " [%s] %s:%d %@(%p) Failed to forward packet to=%@:%d (participant=%@), errno=%d"
+ " [%s] %s:%d %@(%p) Failed to init the instances lock"
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
+ " [%s] %s:%d %@(%p) Skipping, a writer is already composed for"
+ " [%s] %s:%d %@(%p) Tracing number of bytes: receievedBytes=%d"
+ " [%s] %s:%d %@(%p) Tracing packet across the network, Mock QR Server received  RTP datagram size=%d, SSRC=0x%X, SeqNum=%u"
+ " [%s] %s:%d %@(%p) Trying to get the mockDatagramChannel, tempParticipantID value=%@"
+ " [%s] %s:%d %@(%p) Video frame is too old and modulated timestamp rolled backward – dropping frame. lastModulatedTimestamp=%u, modulatedTimestamp=%u, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d %@(%p) [FTDC] All camera connections disabled, not starting session context=%@"
+ " [%s] %s:%d %@(%p) [FTDC] No desired secondary capture formats: no video device format matches width=%d, height=%d, aspectRatio=%d among %lu multicam candidates of %lu total"
+ " [%s] %s:%d %@(%p) [FTDC] No exact %dx%d rear format (picker chose %dx%d); falling back to %dx%d"
+ " [%s] %s:%d %@(%p) [FTDC] Primary connections video=%d metadata=%d"
+ " [%s] %s:%d %@(%p) [FTDC] _videoCaptureSource=%d, _dualCaptureEnabled=%d, _dualCaptureReceiverEnabled=%d, _oneToOneModeEnabled=%d"
+ " [%s] %s:%d %@(%p) [FTDC] ignoring secondary aspectRatio=%d on the disable path"
+ " [%s] %s:%d %@(%p) [FTDC] ignoring secondary disable: dual capture already off"
+ " [%s] %s:%d %@(%p) [FTDC] primaryUID=%@, secondaryUID=%@, hasSecondary=%d, aspectRatio=%d, dualCaptureEnabled=%d"
+ " [%s] %s:%d %@(%p) error zero sampleBufferSize requested, maxSamplesPerFrame=%u, mBytesPerFrame=%u, audioPayloadsCount=%lu"
+ " [%s] %s:%d %@(%p) nw connection reported state=%d, errorDomain=%d, errorCode=%d"
+ " [%s] %s:%d %@(%p) recv failed: receivedBytes=%d, errno=%d, socket=%d"
+ " [%s] %s:%d %@(%p) streamGroupID=%s, shouldSync=%d, hksvHasVideoStreamInput=%d"
+ " [%s] %s:%d %@(%p) width=%d, height=%d, frameRate=%d, sourceToken=0x%x, cinematicFramingEnabled=%d, orientation=%d, zoomFactor=%f, remoteSupportsFullScreenReceive=%d, videoPresentationOrientation=%d, hasVideoPresentationOrientation=%d, previewPresentationOrientation=%d, hasPreviewPresentationOrientation=%d"
+ " [%s] %s:%d Bad buffer length(%zu) for FaceTime audio media control info with header bitmap 0x%x, expecting %zu"
+ " [%s] %s:%d Bad buffer length(%zu) for FaceTime audio media control info, expecting %zu"
+ " [%s] %s:%d Capturing first modulatedTimestamp=%u baseline, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d Failed [super init]"
+ " [%s] %s:%d Failed to allocate _enqueueLock"
+ " [%s] %s:%d Failed to allocate _queueLock"
+ " [%s] %s:%d Failed to allocate forwarder sources"
+ " [%s] %s:%d Failed to allocate inter frame delay monitor"
+ " [%s] %s:%d Failed to allocate socket list"
+ " [%s] %s:%d Failed to allocate the active instances set"
+ " [%s] %s:%d Failed to compose loggingIdentifier for streamToken=%ld"
+ " [%s] %s:%d Failed to create compressionSessionOptions"
+ " [%s] %s:%d Failed to create forwarder queue"
+ " [%s] %s:%d Failed to create read source for socket=%d (participant=%@)"
+ " [%s] %s:%d Failed to create sockets from configuration"
+ " [%s] %s:%d Failed to init the instances lock"
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
+ " [%s] %s:%d Not enough buffer for ECN CE count"
+ " [%s] %s:%d Not enough buffer for ECN ECT1 count"
+ " [%s] %s:%d Not enough buffer for bandwidth estimation"
+ " [%s] %s:%d Not enough buffer for video burst loss"
+ " [%s] %s:%d Packet too short: receivedBytes=%d < headerSize=%d, dropping"
+ " [%s] %s:%d Redundancy unfrozen reason=%d isNetworkCongested=%d _offChannelTimeRatio=%2.3f freezeDuration=%2.3f keptHistory=%d"
+ " [%s] %s:%d SRTP verification failed (%X), consecutiveSRTPAuthFailures=%u, ssrc=%X"
+ " [%s] %s:%d Skipping the participant VCAudioIO start. isHomeKitVideo=%d"
+ " [%s] %s:%d Skipping, a writer is already composed for"
+ " [%s] %s:%d Timed out draining rate control feedback, source=%p"
+ " [%s] %s:%d Transport streams cleared, rtpTransportStream=%p, rtcpTransportStream=%p"
+ " [%s] %s:%d VCDTMFToneGenerator[%p] Initialize event=%d, powerLevel=%d, sampleRate=%d, tableAmplitude=%d, amplitude=%d"
+ " [%s] %s:%d VCHardwareSettings: clientPreviewPresentationOrientation support overridden by user default: outOfBox=%d override=%d"
+ " [%s] %s:%d VTCompressionSessionCreateWithOptions failed (%d)"
+ " [%s] %s:%d Video frame is too old and modulated timestamp rolled backward – dropping frame. lastModulatedTimestamp=%u, modulatedTimestamp=%u, frameTimeInSec=%f, rtpTimestampRate=%u"
+ " [%s] %s:%d [%p] Adding %@=%@ to the codec session's dictionary"
+ " [%s] %s:%d [%p] Failed to create loggingIdentifier from vtLoggingIdentifier=%s"
+ " [%s] %s:%d [%p] InitialRamp Metrics: numPackets=%u numAudioPackets=%u hasSufficientAudio=%d numOOOPackets=%u maxOOODisplacementMs=%u avgOOODisplacementMs=%u"
+ " [%s] %s:%d [%p] InitialRamp OOO sn=%u prevSn=%u tsDelta=%u dispMs=%u numOOO=%u maxDispMs=%u"
+ " [%s] %s:%d [%p] InitialRamp START firstTs=%u windowEndTs=%u sampleRate=%u"
+ " [%s] %s:%d [%p] InitialRamp WINDOW CLOSED numPackets=%u numAudioPackets=%u numOOO=%u maxDispMs=%u sumDispMs=%.0f"
+ " [%s] %s:%d [%p] VideoTransmitter_CreateHandle wMTU[%d] bIsIPv6[%d] reinitOnFrameChangeEnabled[%s] reinitOnARChangeEnabled[%s]"
+ " [%s] %s:%d [AR_TX] captureAspectRatio=%@, composeLandscapeOrderedRatio=%d, clientPreviewGoverns=%d, _videoPresentationOrientation=%d, _hasVideoPresentationOrientation=%d, _previewPresentationOrientation=%d, _hasPreviewPresentationOrientation=%d, _orientation=%d, _deviceOrientationMatchesReceiver=%d, _remotePreferFullBleed=%d, overrideByDefault=%d"
+ " [%s] %s:%d [AR_TX] client preview presentation orientation not honored, the active format cannot vend it. aspectRatio=%@, _previewPresentationOrientation=%d, _orientation=%d"
+ " [%s] %s:%d [AR_TX]_videoPresentationOrientation=%d, _hasVideoPresentationOrientation=%d, orientation=%d, _deviceOrientationMatchesReceiver=%d"
+ " [%s] %s:%d [FTDC] All camera connections disabled, not starting session context=%@"
+ " [%s] %s:%d [FTDC] No desired secondary capture formats: no video device format matches width=%d, height=%d, aspectRatio=%d among %lu multicam candidates of %lu total"
+ " [%s] %s:%d [FTDC] No exact %dx%d rear format (picker chose %dx%d); falling back to %dx%d"
+ " [%s] %s:%d [FTDC] Primary connections video=%d metadata=%d"
+ " [%s] %s:%d [FTDC] _dualCaptureSupported=%d, useVirtualCapture=%d"
+ " [%s] %s:%d [FTDC] _videoCaptureSource=%d, _dualCaptureEnabled=%d, _dualCaptureReceiverEnabled=%d, _oneToOneModeEnabled=%d"
+ " [%s] %s:%d [FTDC] ignoring secondary aspectRatio=%d on the disable path"
+ " [%s] %s:%d [FTDC] ignoring secondary disable: dual capture already off"
+ " [%s] %s:%d [FTDC] primaryUID=%@, secondaryUID=%@, hasSecondary=%d, aspectRatio=%d, dualCaptureEnabled=%d"
+ " [%s] %s:%d [FTDC][PFAR] path=afterCapture, attach=%d, dualCaptureEnabled=%d, dualCaptureReceiverEnabled=%d, shouldAttachPerFrameAR=%d, frontCamera=%d, bufferWidth=%zu, bufferHeight=%zu"
+ " [%s] %s:%d [FTDC][PFAR] path=duringProcessEffect, attach=%d, dualCaptureEnabled=%d, dualCaptureReceiverEnabled=%d, shouldAttachPerFrameAR=%d, frontCamera=%d, bufferWidth=%zu, bufferHeight=%zu"
+ " [%s] %s:%d [HKSV3] came mediaSubtype='%s' did not match camera default, retried against HomeKit camera default. isValid=%d"
+ " [%s] %s:%d _previewPresentationOrientation=%d, _hasPreviewPresentationOrientation=%d, _isPreviewing=%d, _isCapturing=%d"
+ " [%s] %s:%d _previewPresentationOrientation=%d, didChange=%d, _orientation=%d, _videoPresentationOrientation=%d, _hasVideoPresentationOrientation=%d, _isPreviewing=%d, _isCapturing=%d"
+ " [%s] %s:%d beginSession: %lu audio unit mock instance(s) carried over from a previous session"
+ " [%s] %s:%d beginSession: %lu component mock instance(s) leaked from a previous session (never disposed)"
+ " [%s] %s:%d centerStageRectOfInterest rejected, centerStageEnabled=0, reason=%@"
+ " [%s] %s:%d configureWithBuffer failed with error %08X for control info=%p, dropping it"
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
+ " [%s] %s:%d streamGroupID=%s is not an enumerated AVCStreamGroupID"
+ " [%s] %s:%d streamGroupID=%s streamInputID=%@ captureSourceID=%d"
+ " [%s] %s:%d streamGroupID=%s, shouldSync=%d, hksvHasVideoStreamInput=%d"
+ " [%s] %s:%d videoDecoder=%p decoded frame colorimetry changed to ColorPrimaries=%@ TransferFunction=%@ YCbCrMatrix=%@ for streamID=%d width=%d height=%d"
+ " [%s] %s:%d videoDecoder=%p decoded frame has no CGColorSpace attachment for streamID=%d width=%d height=%d"
+ " [%s] %s:%d wasClientGoverning=%d, _orientation=%d, _isPreviewing=%d, _isCapturing=%d"
+ " [%s] %s:%d width=%d, height=%d, frameRate=%d, sourceToken=0x%x, cinematicFramingEnabled=%d, orientation=%d, zoomFactor=%f, remoteSupportsFullScreenReceive=%d, videoPresentationOrientation=%d, hasVideoPresentationOrientation=%d, previewPresentationOrientation=%d, hasPreviewPresentationOrientation=%d"
+ "+[VCHardwareSettings supportsClientPreviewPresentationOrientation]_block_invoke"
+ "-[AVCPreviewCameraSession setPreviewPresentationOrientation:]_block_invoke"
+ "-[AVConferencePreview setPreviewPresentationOrientation:]"
+ "-[VCAVFoundationCapture applyDualCaptureResolutionToPrimaryCamera]"
+ "-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:]_block_invoke"
+ "-[VCAVFoundationCapture clearPreviewPresentationOrientation]_block_invoke"
+ "-[VCAVFoundationCapture clearRemotePresentationOrientation]_block_invoke"
+ "-[VCAVFoundationCapture encodeProcessedPixelBuffer:time:imageData:processTime:]_block_invoke"
+ "-[VCAVFoundationCapture initWithCaptureServer:protocolFunctions:width:height:frameRate:videoSourceToken:cinematicFramingEnabled:videoOrientation:capturePixelFormat:zoomFactor:remoteSupportsFullScreenReceive:videoPresentationOrientation:hasVideoPresentationOrientation:previewPresentationOrientation:hasPreviewPresentationOrientation:]"
+ "-[VCAVFoundationCapture setPreviewPresentationOrientation:]_block_invoke"
+ "-[VCAVFoundationCapture updateCameraZoomCapabilityForCaptureDeviceInput:captureSource:]"
+ "-[VCAVFoundationCapture updateDeviceOrientationMatchesReceiver:]"
+ "-[VCAVFoundationCapture vendableAspectRatio:landscapeOrderedAlternate:captureFormat:clientPreviewGoverns:]"
+ "-[VCAudioToolboxAudioComponentMock init]"
+ "-[VCConnectionManagerIDS updateLocalLinkTechnology:]"
+ "-[VCControlChannelMultiWay lastUsedMKIBytes]_block_invoke"
+ "-[VCCoreAudio_AudioUnitMock beginSession]"
+ "-[VCMediaRecorderLocal localRecordingScreenAttributesDidChange:]"
+ "-[VCMediaRecorderLocal updateTargetScreenAttributesFromCaptureServer]"
+ "-[VCMockQRServer forwardOnePacketFromListenerSocket:listenerSourceIP:listenerSourcePort:forwarderSocketList:listenerParticipantID:]"
+ "-[VCMockQRServer initMockQRServer]"
+ "-[VCSessionParticipantLocal captureEncodingSize]"
+ "-[VCSessionParticipantLocal enableDualCaptureReceiver:]_block_invoke"
+ "-[VCTransportSessionMultiLink handleListenerEvents:error:result:]"
+ "-[VCVideoCaptureServer applyClientPreviewPresentationOrientationArguments:]"
+ "-[VCVideoCaptureServer clearPreviewPresentationOrientationRequestForDiedClient:]_block_invoke"
+ "-[VCVideoCaptureServer clearRemotePresentationOrientation]"
+ "-[VCVideoCaptureServer clearRemotePresentationOrientation]_block_invoke"
+ "-[VCVideoCaptureServer dispatchedClearPreviewPresentationOrientationRequest]"
+ "-[VCVideoCaptureServer dispatchedCopyLocalRecordingScreenAttributesForVideoAttributes:]"
+ "-[VCVideoCaptureServer notifyClientsLocalRecordingScreenAttributesDidChange]"
+ "-[VCVideoCaptureServer notifyClientsLocalRecordingScreenAttributesDidChange]_block_invoke"
+ "-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_6"
+ "-[VCVideoCaptureServer setPreviewPresentationOrientation:requestingClientPID:]"
+ "2260.15.1"
+ "<%s:%p> Token (%d) Link (%d): %s <-> %s (%s, %s), priority %d, uplink bitrate cap (%u), downlink bitrate cap (%u), uplink audio only bitrate cap = (%u), uplink OneToOne bitrate cap = (%u), isLocalConstrained (%d), isRemoteConstrained (%d), isLocalExpensive (%d) isRemoteExpensive (%d) isLocalDelegated (%d) isRemoteDelegated (%d) isLocalUltraConstrained (%d) isRemoteUltraConstrained (%d) isVirtualRelayLink (%d) reportingIPVersion(%d) TransportLayerEncryption=%d relayProtocolStackDescrption(%@) channelDataBaseProtocolStackDescription(%@) _isHopByHopEncryptionSupported=%d localLinkTransport=%u localLinkTechnology=%u"
+ "AVC-CD/%ld"
+ "AVC-CE/%ld"
+ "AVC-SD/%ld"
+ "AVC-SE/%ld"
+ "AVCPreviewCameraSession [%s] %s:%d %@(%p) cameraUID=%@ orientation=%d"
+ "AVCPreviewCameraSession [%s] %s:%d cameraUID=%@ orientation=%d"
+ "AVCRC [%s] %s:%d [%p] ReportNetworkStatistics shouldReport=%d rttMs=%u arrivalTime=%f plr=%f plrAudio=%f plrVideo=%f (lastPlr=%f lastPlrAudio=%f lastPlrVideo=%f) burstPacketLoss=%u (lastBurst=%u) owrd=%u (lastOwrd=%u) isNetworkCongested=%d (lastCongested=%d) unconditional=%d"
+ "AVConferencePreview [%s] %s:%d %@(%p) orientation=%d"
+ "AVConferencePreview [%s] %s:%d orientation=%d"
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
+ "VCMediaRecorderHistory_HasConfiguredWriter"
+ "VCMediaStream [%s] %s:%d %@(%p) Last RTCP packet receive time:%f now:%f rtcpTimeoutEnabledTime=%f rtcpTimeoutInterval=%f. Triggering RTCP timeout"
+ "VCMediaStream [%s] %s:%d Last RTCP packet receive time:%f now:%f rtcpTimeoutEnabledTime=%f rtcpTimeoutInterval=%f. Triggering RTCP timeout"
+ "VCRC [%s] %s:%d Set feedback controlInfo [%p]: echoedSendTimestamp=%u bandwidthEstimation=%u videoBurstLoss=%u audioBurstLoss=%u videoReceivedPkts=%u audioReceivedPkts=%u totalReceivedKBytes=%u receiveQueueTarget=%u ecnECT1Count=%u ecnCECount=%u connectionStatsBlob=%u"
+ "VCRateControlSetFeedbackControlInfo"
+ "VCSoundDec [%s] %s:%d [%p] AudioConverterDispose failed, status=%d audioConv=%p"
+ "VCStringUtils_AddVTLoggingIdentifier"
+ "VCStringUtils_SetVTLoggingIdentifier"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) Discarding client preview presentation orientation request, unsupported by the hardware rule. previewPresentationOrientation=%d"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) Invalid previewPresentationOrientation=%d"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) Missing or non-numeric previewPresentationOrientation, class=%@"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) No local video attributes to derive recording screen attributes from"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) Notifying client=%p of class=%@"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) Retaining the remote presentation orientation at call end, unsupported by the hardware rule."
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) Retaining the request, the dying client did not make it. diedClientPID=%d, _previewPresentationOrientationRequestPID=%d, _previewPresentationOrientationRequest=%d, _hasPreviewPresentationOrientationRequest=%d"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) [AR_RX] videoOrientation=%d, screenOrientation=%d"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) _previewPresentationOrientationRequest=%d, _hasPreviewPresentationOrientationRequest=%d, _previewPresentationOrientationRequestPID=%d"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) _remotePresentationOrientation=%d, _hasRemotePresentationOrientation=%d, _previewPresentationOrientationRequest=%d, _hasPreviewPresentationOrientationRequest=%d"
+ "VCVideoCaptureServer [%s] %s:%d %@(%p) previewPresentationOrientation=%d, requestingClientPID=%d"
+ "VCVideoCaptureServer [%s] %s:%d Discarding client preview presentation orientation request, unsupported by the hardware rule. previewPresentationOrientation=%d"
+ "VCVideoCaptureServer [%s] %s:%d Invalid previewPresentationOrientation=%d"
+ "VCVideoCaptureServer [%s] %s:%d Missing or non-numeric previewPresentationOrientation, class=%@"
+ "VCVideoCaptureServer [%s] %s:%d No local video attributes to derive recording screen attributes from"
+ "VCVideoCaptureServer [%s] %s:%d Notifying client=%p of class=%@"
+ "VCVideoCaptureServer [%s] %s:%d Retaining the remote presentation orientation at call end, unsupported by the hardware rule."
+ "VCVideoCaptureServer [%s] %s:%d Retaining the request, the dying client did not make it. diedClientPID=%d, _previewPresentationOrientationRequestPID=%d, _previewPresentationOrientationRequest=%d, _hasPreviewPresentationOrientationRequest=%d"
+ "VCVideoCaptureServer [%s] %s:%d [AR_RX] videoOrientation=%d, screenOrientation=%d"
+ "VCVideoCaptureServer [%s] %s:%d _previewPresentationOrientationRequest=%d, _hasPreviewPresentationOrientationRequest=%d, _previewPresentationOrientationRequestPID=%d"
+ "VCVideoCaptureServer [%s] %s:%d _remotePresentationOrientation=%d, _hasRemotePresentationOrientation=%d, _previewPresentationOrientationRequest=%d, _hasPreviewPresentationOrientationRequest=%d"
+ "VCVideoCaptureServer [%s] %s:%d ignoring stale capture failure, failingCameraUID=%@, currentCameraUID=%@"
+ "VCVideoCaptureServer [%s] %s:%d previewPresentationOrientation=%d, requestingClientPID=%d"
+ "VCVideoCaptureServer [%s] %s:%d requested secondary aspectRatio=%d not applied: _avCapture=%p lacks batchSetCameraUIDsPrimary:secondary:hasSecondary:aspectRatio:"
+ "VCVideoPlayer [%s] %s:%d VCVideoPlayer[%p] playbackClient[%p] Skipping avsync offset reporting. firstFramePresented=%d hostTimeForPlayout=%f externalSourcePlayoutTimeInSeconds=%f lastFrame.videoFrameTimeInSeconds=%f"
+ "VCVideoPlayer [%s] %s:%d VCVideoPlayer[%p] pthread_cond_timedwait_relative_np unexpected error=%d"
+ "VCVideoStream [%s] %s:%d %@(%p) Rebuilding transports for reconfigure. currentCount=%u expectedCount=%u localSSRCChanged=%d canReuse=%d"
+ "VCVideoStream [%s] %s:%d Rebuilding transports for reconfigure. currentCount=%u expectedCount=%u localSSRCChanged=%d canReuse=%d"
+ "VCVideoStreamConfig_SetVTLoggingIdentifier"
+ "VideoPacketBuffer [%s] %s:%d /AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/Others/VideoPacketBuffer.c:%d: VideoPacketBuffer[%p] Reusing cached plaintext for re-assembled frame timestamp=%u frameSequenceNumber=%d isLate=%d"
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
+ "dualCamPrimaryPrefers1280SquareCapture"
+ "dualCaptureRear1440x1080"
+ "forceBDATCompressed"
+ "forceClientPreviewPresentationOrientation"
+ "i28@?0^{tagVCMediaPacket=iS^{OpaqueCMBlockBuffer}{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}i^v^?^{tagHANDLE}ddBBBBIIIIISIIIiIddBBBBBBBBBBiAB^{tagVCMediaPacket}}8S16S20s24"
+ "lcid"
+ "previewPresentationOrientation"
+ "previewSetPresentationOrientation"
+ "rcid"
+ "redundancyCongestionKeepHistoryRatio"
+ "secondary camera UID must differ from the primary camera UID"
+ "v20@?0i8^{FigRemoteOperation=iiQ^{__CFString}(?={?=^{__CFDictionary}^{__CFDictionary}}{?=^v^{__IOSurface}^{__IOSurface}}{?=^{opaqueCMSampleBuffer}Q^{__CFArray}}{?=^{opaqueCMFormatDescription}}{?=q^{opaqueCMFormatDescription}^IQ})}12"
+ "vc-redundancy-controller-video-congestion-keep-history-ratio"
- " [%s] %s:%d %@ not available, falling back to basic initializer."
- " [%s] %s:%d %@(%p) %@ not available, falling back to basic initializer."
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
- " [%s] %s:%d %@(%p) [FTDC] primaryUID=%@, secondaryUID=%@, aspectRatio=%d, dualCaptureEnabled=%d"
- " [%s] %s:%d %@(%p) _transcriptionTimes is nil"
- " [%s] %s:%d %@(%p) error zero sampleBufferSize requested"
- " [%s] %s:%d %@(%p) no streams available"
- " [%s] %s:%d %@(%p) reportAndReset returned nil"
- " [%s] %s:%d %@(%p) skipping IFD stats: monitor=%p, param=%p"
- " [%s] %s:%d %@(%p) stopped a timer=%p that was already stop"
- " [%s] %s:%d %@(%p) width=%d, height=%d, frameRate=%d, sourceToken=0x%x, cinematicFramingEnabled=%d, orientation=%d, zoomFactor=%f, remoteSupportsFullScreenReceive=%d, videoPresentationOrientation=%d"
- " [%s] %s:%d @:@ VCAudioCaptionsSpeechTranslator-init Finished instance=%p Succeeded with frameworkType=%d"
- " [%s] %s:%d @:@ VCAudioCaptionsSpeechTranslator-init instance=%p"
- " [%s] %s:%d Bad buffer length(%zu) for FaceTime audio media control info, expecting %u"
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
- " [%s] %s:%d The server disconnected for the STSpeechTranslatorClient=%@"
- " [%s] %s:%d Translation started for STSpeechTranslatorClient=%@"
- " [%s] %s:%d Translation stopped for STSpeechTranslatorClient=%@ with error=%@"
- " [%s] %s:%d Unexpected streamGroupID=%s"
- " [%s] %s:%d VCAudioCaptionsSpeechTranslator-init FAILED"
- " [%s] %s:%d VCDTMFToneGenerator[%p] Initialize event=%d, powerLevel=%d, sampleRate=%d"
- " [%s] %s:%d VCHardwareSettings: squarePreviewCapture support overridden by user default: outOfBox=%d override=%d"
- " [%s] %s:%d VTCompressionSessionCreate failed (%d)"
- " [%s] %s:%d Waiting for packet on socket=%d..."
- " [%s] %s:%d [%p] VideoTransmitter_CreateHandle wMTU[%d] bIsIPv6[%d] reinitEnabled[%s]"
- " [%s] %s:%d [AR_TX] _deviceOrientationMatchesReceiver=%d, _remotePreferFullBleed=%d, previewOnly=%d, prefersSquarePreview=%d, captureAspectRatio=%@, overrideByDefault=%d"
- " [%s] %s:%d [AR_TX]videoPresentationOrientation=%d, orientation=%d, _deviceOrientationMatchesReceiver=%d"
- " [%s] %s:%d [FTDC] _dualCaptureSupported=%d"
- " [%s] %s:%d [FTDC] primaryUID=%@, secondaryUID=%@, aspectRatio=%d, dualCaptureEnabled=%d"
- " [%s] %s:%d _transcriptionTimes is nil"
- " [%s] %s:%d error zero sampleBufferSize requested"
- " [%s] %s:%d eventInfo has IDSDataChannelError, ERROR = %@"
- " [%s] %s:%d no streams available"
- " [%s] %s:%d recvmsg failed for socket=%d"
- " [%s] %s:%d reportAndReset returned nil"
- " [%s] %s:%d skipping IFD stats: monitor=%p, param=%p"
- " [%s] %s:%d stopped a timer=%p that was already stop"
- " [%s] %s:%d width=%d, height=%d, frameRate=%d, sourceToken=0x%x, cinematicFramingEnabled=%d, orientation=%d, zoomFactor=%f, remoteSupportsFullScreenReceive=%d, videoPresentationOrientation=%d"
- "+[VCHardwareSettings supportsSquarePreviewCapture]_block_invoke"
- "-[VCAVFoundationCapture batchSetCameraUIDsPrimary:secondary:aspectRatio:]_block_invoke"
- "-[VCAVFoundationCapture initWithCaptureServer:protocolFunctions:width:height:frameRate:videoSourceToken:cinematicFramingEnabled:videoOrientation:capturePixelFormat:zoomFactor:remoteSupportsFullScreenReceive:videoPresentationOrientation:]"
- "-[VCAVFoundationCapture updateCameraZoomCapabilityForCaptureDeviceInput:]"
- "-[VCAVFoundationCapture updateDeviceOrientationMatchesReceiver:videoPresentationOrientation:]"
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
- "-[VCControlChannelMultiWay lastUsedMKIBytes]"
- "-[VCDispatchTimer stop]"
- "-[VCSessionUplinkVideoStreamController anchorStreamIDWithCappedVideoStreamIDs:]"
- "-[VCTransportSessionMultiLink handleListenerEvents:error:]"
- "-[VCVideoCaptureServer registerBlocksForServer]_block_invoke_5"
- "-[VCVideoStreamReceiver gatherInterframeDelayStats:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/Captions/VCAudioCaptionsSpeechTranslator.m"
- "/System/Library/PrivateFrameworks/SpeechTranslation.framework/SpeechTranslation"
- "2235.63.5.2"
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
- "VCVideoStream [%s] %s:%d %@(%p) Reconfiguring VCVideoStream with a different number of transports."
- "VCVideoStream [%s] %s:%d Reconfiguring VCVideoStream with a different number of transports."
- "VideoCallTranslation"
- "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] Received NULL frame"
- "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] Successfully assembled previously incomplete late frame timestamp=%u frameSequenceNumber=%u isRefreshFrame=%d hasRetransmittedPackets=%d"
- "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] [recovery] Frame not submitted TS=%u seq=%u frameSequenceNumber=%d isRefreshFrame=%d isLTRPFrame=%d isIntraFrame=%d iLTRBits=0x%x hasRetransmittedPackets=%d isLate=%d keyFrameRequestReason=%s futureFramesSize=%u incompleteFramesSize=%u"
- "VideoPacketBuffer [%s] %s:%d VideoPacketBuffer[%p] [recovery] Freeing frame TS=%u frameSequenceNumber=%d isLate=%d fScheduled=%d isFailedCompleteFrame=%d isLTRPFrame=%d isIntraFrame=%d hasRetransmittedPackets=%d"
- "_VCSpeechTranslation_LibraryHandle"
- "_VCSpeechTranslation_LibraryHandle_block_invoke"
- "enableInterframeDelay"
- "forceSquarePreviewCapture"
- "hostAudioTranscriptionAnalysisServer"
- "hostSpeechTranslationServer"
- "i28@?0^{tagVCMediaPacket=iS^{OpaqueCMBlockBuffer}{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}{tagVCIDSChannelDataFormat=[12S]CBSCBBQBBBS{?=SSSSS}BBBQBSBBBB}i^v^?^{tagHANDLE}ddBBBBIIIIISIIIiIddBBBBBBBBBBi^{tagVCMediaPacket}}8S16S20s24"
- "v20@?0i8^{FigRemoteOperation=iiQ^{__CFString}(?={?=^{__CFDictionary}^{__CFDictionary}}{?=^v^{__IOSurface}^{__IOSurface}}{?=^{opaqueCMSampleBuffer}Q^{__CFArray}}{?=^{opaqueCMFormatDescription}}{?=q^{opaqueCMFormatDescription}})}12"
```
