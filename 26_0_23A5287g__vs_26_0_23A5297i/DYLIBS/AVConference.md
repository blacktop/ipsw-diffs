## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-2145.53.2.0.0
-  __TEXT.__text: 0x78ec44
-  __TEXT.__auth_stubs: 0x55f0
-  __TEXT.__objc_methlist: 0x35748
-  __TEXT.__const: 0xc770
-  __TEXT.__cstring: 0x8e661
-  __TEXT.__oslogstring: 0x10ddef
-  __TEXT.__gcc_except_tab: 0x2adc
+2145.57.1.0.0
+  __TEXT.__text: 0x7902e0
+  __TEXT.__auth_stubs: 0x5600
+  __TEXT.__objc_methlist: 0x357c0
+  __TEXT.__const: 0xc760
+  __TEXT.__cstring: 0x8ea45
+  __TEXT.__oslogstring: 0x10e0e2
+  __TEXT.__gcc_except_tab: 0x2ae8
   __TEXT.__ustring: 0x1a8
-  __TEXT.__unwind_info: 0x107a8
+  __TEXT.__unwind_info: 0x107d8
   __TEXT.__objc_classname: 0x4eb2
-  __TEXT.__objc_methname: 0x7d221
-  __TEXT.__objc_methtype: 0x281fc
-  __TEXT.__objc_stubs: 0x4e720
+  __TEXT.__objc_methname: 0x7d491
+  __TEXT.__objc_methtype: 0x28248
+  __TEXT.__objc_stubs: 0x4e880
   __DATA_CONST.__got: 0x1a30
-  __DATA_CONST.__const: 0x6a08
+  __DATA_CONST.__const: 0x6a10
   __DATA_CONST.__objc_classlist: 0x12e8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x488
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16820
+  __DATA_CONST.__objc_selrefs: 0x16878
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x10e8
   __DATA_CONST.__objc_arraydata: 0x2628
-  __AUTH_CONST.__auth_got: 0x2b10
+  __AUTH_CONST.__auth_got: 0x2b18
   __AUTH_CONST.__const: 0x3bc8
-  __AUTH_CONST.__cfstring: 0x25f60
-  __AUTH_CONST.__objc_const: 0x62fc8
+  __AUTH_CONST.__cfstring: 0x26040
+  __AUTH_CONST.__objc_const: 0x63088
   __AUTH_CONST.__objc_intobj: 0x4968
   __AUTH_CONST.__objc_arrayobj: 0x1b30
   __AUTH_CONST.__objc_floatobj: 0x30
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH.__objc_data: 0x1360
-  __DATA.__objc_ivar: 0x6be4
+  __DATA.__objc_ivar: 0x6bf8
   __DATA.__data: 0x7870
-  __DATA.__bss: 0xd80
+  __DATA.__bss: 0xd28
   __DATA.__common: 0x55
   __DATA_DIRTY.__objc_data: 0xa9b0
   __DATA_DIRTY.__data: 0x160
-  __DATA_DIRTY.__bss: 0x3f8
+  __DATA_DIRTY.__bss: 0x468
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 51E3C80D-0014-33B9-BAB4-2A97670499F1
-  Functions: 31457
-  Symbols:   97051
-  CStrings:  56984
+  UUID: E813D7A2-B9D6-346B-BAA8-1455A2002CD6
+  Functions: 31480
+  Symbols:   97106
+  CStrings:  57034
 
Symbols:
+ +[VCHardwareSettings shouldCameraEffectsFrontCameraMirror]
+ -[AVCScreenCaptureConfiguration description]
+ -[VCAVFoundationCapture updateCenterStageMetadataDeliveryEnabled]
+ -[VCAudioIOControllerClient prefersRealtimeCatchUp]
+ -[VCAudioIOControllerClient setPrefersRealtimeCatchUp:]
+ -[VCAudioRelay forwardOneBlockSizeFromIO:toIO:withConverter:withHostTime:]
+ -[VCAudioRelayIO isRealtimeCatchUpEnabled]
+ -[VCAudioRelayIO setRealtimeCatchUpEnabled:]
+ -[VCAudioStream shouldEnableFixedJitterBufferInitialOvershootResiliency]
+ -[VCMediaStream shouldFinalizeAggregationOnStop]
+ -[VCRateControlMLEnrollment init].cold.6
+ -[VCRateControlMLEnrollment isEnrollmentDisabledByStorebagSwitch]
+ -[VCScreenCapture newIdleBlackFrameWithAttributes:]
+ GCC_except_table100
+ GCC_except_table107
+ _OBJC_IVAR_$_VCAVFoundationCapture._cameraEffectsFrontCameraMirrored
+ _OBJC_IVAR_$_VCAudioIOControllerClient._prefersRealtimeCatchUp
+ _OBJC_IVAR_$_VCAudioRelayIO._realtimeCatchUpEnabled
+ _OBJC_IVAR_$_VCScreenCapture._nonIdleFramesDropped
+ _OBJC_IVAR_$_VCVideoStream._isListeningForThermalEvents
+ _VCAudioBufferList_GetSamplesAreLate
+ _VCAudioBufferList_GetSamplesAreLate.cold.1
+ _VCAudioBufferList_SetSamplesAreLate
+ _VCAudioBufferList_SetSamplesAreLate.cold.1
+ _VCCameraStatusUtil_RotationAngleForCameraStatusBits
+ _VCRateControlDisableMLEnrollment
+ _VCReporting_FlushReportingSession
+ _VCViewpointCorrection_PrepareProcessDictionary
+ __OBJC_$_PROP_LIST_VCVideoCaptureServer.863
+ __VCNetworkConditionMonitor_triggerNetworkConditionCallback.cold.1
+ __VCScreenCapture_CreateFrameInternal
+ __VCScreenCapture_CreateFrameInternal.cold.1
+ __VCScreenCapture_CreateFrameInternal.cold.2
+ __VCScreenCapture_CreateFrameInternal.cold.3
+ __VCScreenCapture_CreateFrameInternal.cold.4
+ __VCScreenCapture_CreateFrameInternal.cold.5
+ __VideoReceiver_DequeueAndDecode.cold.18
+ ___29-[VCTransportSessionIDS stop]_block_invoke_2
+ ___36-[VCVideoCaptureServer pausePreview]_block_invoke.367
+ ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.107
+ ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.109
+ ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.111
+ ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.116
+ ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.121
+ ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.130
+ ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.137
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.198
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.199
+ ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.199.cold.1
+ ___48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.318
+ ___48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.322
+ ___49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.324
+ ___49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.328
+ ___49-[VCVideoCaptureServer sourceFrameRateDidChange:]_block_invoke.406
+ ___50-[AVCScreenCapture registerBlocksForNotifications]_block_invoke.108
+ ___50-[AVCScreenCapture registerBlocksForNotifications]_block_invoke.113
+ ___50-[AVCScreenCapture registerBlocksForNotifications]_block_invoke.88
+ ___50-[AVCScreenCapture registerBlocksForNotifications]_block_invoke.98
+ ___64-[VCMediaStream handleMediaCallbackNotification:inData:outData:]_block_invoke.232
+ ___71-[VCVideoCaptureServer newSensitiveContentAnalyzerWithParticipantUUID:]_block_invoke.403
+ ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.874
+ ____VCVideoCaptureServer_ProcessPreviewFrameSizeChange_block_invoke.876
+ ____VCVideoCaptureServer_ProcessPreviewFrameSizeChange_block_invoke.878
+ ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.868
+ ___block_descriptor_tmp.485
+ ___block_descriptor_tmp.549
+ ___block_descriptor_tmp.551
+ ___block_literal_global.118
+ ___block_literal_global.123
+ ___block_literal_global.132
+ ___block_literal_global.371
+ _kFigCaptureSampleBufferAttachmentKey_CinematicFramingStereographicFisheyeFactor
+ _objc_msgSend$forwardOneBlockSizeFromIO:toIO:withConverter:withHostTime:
+ _objc_msgSend$isEnrollmentDisabledByStorebagSwitch
+ _objc_msgSend$isMirrored
+ _objc_msgSend$isRealtimeCatchUpEnabled
+ _objc_msgSend$newIdleBlackFrameWithAttributes:
+ _objc_msgSend$prefersRealtimeCatchUp
+ _objc_msgSend$setPrefersRealtimeCatchUp:
+ _objc_msgSend$setRealtimeCatchUpEnabled:
+ _objc_msgSend$shouldCameraEffectsFrontCameraMirror
+ _objc_msgSend$shouldEnableFixedJitterBufferInitialOvershootResiliency
+ _objc_msgSend$shouldFinalizeAggregationOnStop
+ _objc_msgSend$updateCenterStageMetadataDeliveryEnabled
- -[VCScreenCapture processAndSendIdleBlackFrame]
- GCC_except_table106
- GCC_except_table110
- _VCViewpointCorrection_CorrectViewpoint.cold.10
- _VCViewpointCorrection_CorrectViewpoint.cold.11
- _VCViewpointCorrection_CorrectViewpoint.cold.3
- _VCViewpointCorrection_CorrectViewpoint.cold.4
- _VCViewpointCorrection_CorrectViewpoint.cold.5
- _VCViewpointCorrection_CorrectViewpoint.cold.6
- _VCViewpointCorrection_CorrectViewpoint.cold.7
- _VCViewpointCorrection_CorrectViewpoint.cold.8
- _VCViewpointCorrection_CorrectViewpoint.cold.9
- __OBJC_$_PROP_LIST_VCVideoCaptureServer.860
- __VCScreenCapture_handleFrameInternal
- __VCScreenCapture_handleFrameInternal.cold.1
- __VCScreenCapture_handleFrameInternal.cold.2
- __VCScreenCapture_handleFrameInternal.cold.3
- __VCScreenCapture_handleFrameInternal.cold.4
- __VCScreenCapture_handleFrameInternal.cold.5
- __VCViewpointCorrection_CreateCameraIntrinsicsArray.fallbackIntrinsics
- __VCViewpointCorrection_CreateCameraIntrinsicsArray.format
- ___36-[VCVideoCaptureServer pausePreview]_block_invoke.364
- ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.104
- ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.106
- ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.108
- ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.113
- ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.118
- ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.127
- ___48-[VCAudioClientManager registerBlocksForService]_block_invoke.134
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke.192
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.193
- ___48-[VCMediaStream setPause:withCompletionHandler:]_block_invoke_2.193.cold.1
- ___48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.315
- ___48-[VCVideoCaptureServer setLocalVideoAttributes:]_block_invoke.319
- ___49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.321
- ___49-[VCVideoCaptureServer setLocalScreenAttributes:]_block_invoke.325
- ___49-[VCVideoCaptureServer sourceFrameRateDidChange:]_block_invoke.403
- ___50-[AVCScreenCapture registerBlocksForNotifications]_block_invoke.105
- ___50-[AVCScreenCapture registerBlocksForNotifications]_block_invoke.110
- ___50-[AVCScreenCapture registerBlocksForNotifications]_block_invoke.85
- ___50-[AVCScreenCapture registerBlocksForNotifications]_block_invoke.95
- ___64-[VCMediaStream handleMediaCallbackNotification:inData:outData:]_block_invoke.226
- ___71-[VCVideoCaptureServer newSensitiveContentAnalyzerWithParticipantUUID:]_block_invoke.400
- ____VCVideoCaptureServer_DidReceiveFirstPreviewFrame_block_invoke.871
- ____VCVideoCaptureServer_ProcessPreviewFrameSizeChange_block_invoke.873
- ____VCVideoCaptureServer_ProcessPreviewFrameSizeChange_block_invoke.875
- ____VCVideoCaptureServer_SendSnapshotFromFrame_block_invoke.865
- ___block_descriptor_tmp.482
- ___block_descriptor_tmp.546
- ___block_descriptor_tmp.548
- ___block_literal_global.120
- ___block_literal_global.129
- ___block_literal_global.368
- _kFigCaptureSampleBufferAttachmentKey_CinematicFramingStereographicFisheyeStrength
- _objc_msgSend$processAndSendIdleBlackFrame
- _sVC_CVAViewpointCorrection_EnableCorrection
- _sVC_CVAViewpointCorrection_Image
- _sVC_CVAViewpointCorrection_Intrinsics
- _sVC_CVAViewpointCorrection_StereographicFisheyeStrength
- _sVC_CVAViewpointCorrection_Timestamp
- _sVC_CVAViewpointCorrection_VirtualCameraExtrinsics
CStrings:
+ " [%s] %s:%d %@(%p) _captureFormatPrefer16By9ForSquare=%d, _cameraEffectsFrontCameraMirrored=%d"
+ " [%s] %s:%d NetworkConditionMonitor: didUpdateNetworkConditionContext is NULL"
+ " [%s] %s:%d VCRCML enrollment disabled through storebags"
+ " [%s] %s:%d Viewpoint Correction is not supported"
+ " [%s] %s:%d _captureFormatPrefer16By9ForSquare=%d, _cameraEffectsFrontCameraMirrored=%d"
+ " [%s] %s:%d isFrontCamera=%d, _effectsApplied=%d, _supportNoDepthMemoji=%d, _frontCameraSupportsFullBleedCapture=%d"
+ "-[VCAVFoundationCapture updateCenterStageMetadataDeliveryEnabled]"
+ "2145.57.1"
+ "@24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@B}16"
+ "B24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@B}16"
+ "ContentRotationAngle"
+ "Existing settings: %s"
+ "Got notification for setAudioSessionProperties %s on client [%p]"
+ "Requested settings: %s"
+ "Stop ramping up due to RTThreshold=%.2f"
+ "SystemAudioCaptureConfigExcludedPids"
+ "TB,N,GisRealtimeCatchUpEnabled,V_realtimeCatchUpEnabled"
+ "TB,N,V_prefersRealtimeCatchUp"
+ "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}},R,VaudioReceiver"
+ "T{tagVCRateControlAlgorithmConfig=I^Iiii[3i]iiiiiiiiiiiidddddddddddddddiiidddddddddddIIIII[5d]BBBBBBBBBBBBBBBBiBddididddidiiddidddddddddddddddddddddBdiiBiddddddIIdddddIIIdddi{tagVCRateControlCongestionLevel={tagVCRateControlCongestionLevelThresholds=[5d][5d]}{tagVCRateControlCongestionLevelThresholds=[5d][5d]}}iBBB},R,N"
+ "T{tagVCRateControlAlgorithmConfig=I^Iiii[3i]iiiiiiiiiiiidddddddddddddddiiidddddddddddIIIII[5d]BBBBBBBBBBBBBBBBiBddididddidiiddidddddddddddddddddddddBdiiBiddddddIIdddddIIIdddi{tagVCRateControlCongestionLevel={tagVCRateControlCongestionLevelThresholds=[5d][5d]}{tagVCRateControlCongestionLevelThresholds=[5d][5d]}}iBBB},R,N,V_config"
+ "VCAudioBufferList_GetSamplesAreLate"
+ "VCAudioBufferList_SetSamplesAreLate"
+ "VCAudioPlayer [%s] %s:%d Audio Player initialized with format=%s samplesPerFrame=%u useFloats=%{BOOL}d bufferQueueManagementMode=%d timescaleAlgorithm=%d dtmfTonePlaybackEnabled=%d minJitterBufferQueueSize=%d dtmfEventCallbacksEnabled=%d enableEnhancedJBAdaptations=%d isFixedJitterBufferInitialOvershootResiliencyEnabled=%{bool}d"
+ "VCAudioPlayer [%s] %s:%d jitterQueueSize=%d and averageQueueSize=%f exceed desiredQueueSize=%d by threshold=%d. Marking samples at timestamp=%llu late. audioPulls=%u highAverageQueueSizeCount=%d"
+ "VCAudioPlayer [%s] %s:%d jitterQueueSize=%d averageQueueSize=%f sharedQueueSize=%f desiredQueueSize=%d threshold=%d timestamp=%f holeDetectionThreshold=%f audioPulls=%u highAverageQueueSizeCount=%d"
+ "VCMediaStream [%s] %s:%d %@(%p) Finalizing aggregation on stop"
+ "VCMediaStream [%s] %s:%d Finalizing aggregation on stop"
+ "VCScreenCapture [%s] %s:%d First non idle frame received after last idle frame. PresentationTime=%f, interArrivalTime=%f "
+ "VCScreenCapture [%s] %s:%d Frame PresentationTime %f going backwards with respect to previous frame PresentationTime %f. Dropping frame with total frames dropped=%u"
+ "VCViewpointCorrection_PrepareProcessDictionary"
+ "VideoReceiver [%s] %s:%d VideoReceiver[%p] Failed to allocate rotation angle attachment"
+ "^{opaqueCMSampleBuffer=}24@0:8^{?=BBiBBiC}16"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}"
+ "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}16@0:8"
+ "_VCAudioPlayer_MarkOvershootingFrames"
+ "_VCNetworkConditionMonitor_triggerNetworkConditionCallback"
+ "_VCScreenCapture_CreateFrameInternal"
+ "_VideoReceiver_PrepareSampleBufferAttachmentArray"
+ "_cameraEffectsFrontCameraMirrored"
+ "_isListeningForThermalEvents"
+ "_nonIdleFramesDropped"
+ "_prefersRealtimeCatchUp"
+ "_realtimeCatchUpEnabled"
+ "config=%s"
+ "enable720pThermalLightMitigation"
+ "forceHardwareRuleCameraEffectsFrontCameraMirrored"
+ "forwardOneBlockSizeFromIO:toIO:withConverter:withHostTime:"
+ "inDelegate=%s config=%s"
+ "isEnrollmentDisabledByStorebagSwitch"
+ "isMirrored"
+ "isRealtimeCatchUpEnabled"
+ "kCVAViewpointCorrection_StereographicFisheyeFactor"
+ "newIdleBlackFrameWithAttributes:"
+ "prefersRealtimeCatchUp"
+ "rateControlRampUpRTTThreshold"
+ "realtimeCatchUpEnabled"
+ "setPrefersRealtimeCatchUp:"
+ "setRealtimeCatchUpEnabled:"
+ "shouldCameraEffectsFrontCameraMirror"
+ "shouldEnableFixedJitterBufferInitialOvershootResiliency"
+ "shouldFinalizeAggregationOnStop"
+ "updateCenterStageMetadataDeliveryEnabled"
+ "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBBB}16"
+ "v24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@B}16"
+ "vc-vcrcml-disable-enrollment"
+ "{ %@ height=%u, width=%u, frameRate=%u, isWindowed=%d, screenCaptureDisplayID=%u, isCursorCaptured=%d, excludedApplicationBundleIDs=%@, excludedAudioAuditTokens=%@, shouldRunInProcess=%d,  selectiveSharingPort=%u, selectiveScreenUUID=%@, displayMode=%lu, pdProtectionOptions=%llu }"
+ "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@B}16@0:8"
+ "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@B}24@0:8i16i20"
+ "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@B}28@0:8I16r^{tagVCAudioIODelegateContext=@^?^vq@@}20"
+ "{tagVCRateControlAlgorithmConfig=\"serverBagProfileNumber\"I\"tierBitrates\"^I\"initialTierIndex\"i\"maxTierIndex\"i\"minTierIndex\"i\"softMaxTierIndex\"[3i]\"lowestNonEmergencyTierIndex\"i\"lowestNonEmergencyTierIndexWiFi\"i\"lowestEffectiveBWETierIndex\"i\"lowestTierIndexReactToNoServerActivity\"i\"rampUpTierNumber\"i\"rampDownTierNumber\"i\"rampUpAdditionalTierAtInitial\"i\"rampDownAdditionalTierAtInitial\"i\"rampDownBurstyLossThreshold\"i\"lowestTierForBurstyLossRampDown\"i\"lowestTierToEnableRateLimited\"i\"audioOnlyNoRateLimitedTierThreshold\"i\"rampDownNOWRDThreshold\"d\"rampDownNOWRDAccThreshold\"d\"rampDownAggressiveNOWRDThreshold\"d\"rampDownAggressiveNOWRDAccThreshold\"d\"rampDownConstantOWRDDuration\"d\"rampDownOvershootDuration\"d\"rampDownOvershootNextTierRatio\"d\"rampUpFrozenDuration\"d\"rampUpSettleDuration\"d\"rampUpOWRDThreshold\"d\"rampUpNOWRDThreshold\"d\"rampUpNOWRDAccThreshold\"d\"rampUpOverBandwidthCalmDuration\"d\"rampUpBlockedTimeout\"d\"rampUpRTTThreshold\"d\"rampUpOverBandwidthTierNumber\"i\"rampDownLossEventThreshold\"i\"rampDownLossEventBadTrendThreshold\"i\"rampDownLossEventThresholdRatio\"d\"rampDownLossEventWindowDuration\"d\"rampDownLossEventNOWRDThreshold\"d\"rampUpFrozenPLRThreshold\"d\"rampUpRateLimitedRatio\"d\"unstableRateLimitedDuration\"d\"congestionWaitDuration\"d\"owrdWindowDuration\"d\"owrdShortWindowDuration\"d\"minimumNOWRDTimeDifference\"d\"owrdInitialRampUpReadyDuration\"d\"owrdHistorySize\"I\"owrdMininumHistorySize\"I\"fastRampDownBitrateRange\"I\"fastRampUpBitrateRange\"I\"consecutiveRampDownThresholdForCongestion\"I\"continuousRampUpTimeFactor\"[5d]\"bytesInFlightAdaptationEnabled\"B\"useContinuousAdaptationAlgorithm\"B\"receivedBandwidthEstimationEnabled\"B\"basebandAdaptationEnabled\"B\"rateLimitedEnabled\"B\"randomRampUpFrozenDurationEnabled\"B\"oscillationAvoidanceEnabled\"B\"fastRampUpEnabled\"B\"blockRampUpInSaturatedNetworkEnabled\"B\"blockRampUpInBluetoothCoexEnabled\"B\"wifiEmergencyTiersEnabled\"B\"burstyTrafficEnabled\"B\"spatialTrafficEnabled\"B\"lowLatencyWANEnabled\"B\"lowBandwidthOptimizationEnabled\"B\"rampDownToActualSendBitrate\"B\"rampDownToActualSendBitrateMinTier\"i\"rampDownSuppressionEnabled\"B\"rampDownSuppressionMinRTT\"d\"rampDownSuppressionFactor\"d\"fastRampUpHighestTier\"i\"fastRampUpRTTRatio\"d\"fastRampUpTierGap\"i\"fastRampUpNetworkStableDuration\"d\"networkSaturatedRTTToMinRTTRatio\"d\"networkSaturatedOWRDToMinRTTRatio\"d\"networkSaturatedPersistFeedbackNumber\"i\"networkSaturatedRTTDecreasingThreshold\"d\"oscillationAvoidanceTierChangeThreshold\"i\"oscillationAvoidanceTiersHitThreshold\"i\"oscillationAvoidanceDurationRatio\"d\"oscillationAvoidanceDurationRatioAggressive\"d\"stabilizationScheme\"i\"rampDownNBDCDThreshold\"d\"rampDownAggressiveNBDCDThreshold\"d\"rampDownNormalizedQueuingDelayThreshold\"d\"rampDownMediumQueuingDelayThreshold\"d\"rampDownHighQueuingDelayThreshold\"d\"rampDownEmergencyTierCoolDownTime\"d\"rampDownWiFiEmergencyTierCoolDownTime\"d\"rampDownNWConnectionAvgDelayThresholdMin\"d\"rampDownNWConnectionAvgDelayThresholdMax\"d\"rampDownContinuousTierSpeedFactor\"d\"rampUpContinuousTierSpeedFactor\"d\"rampUpNBDCDThreshold\"d\"rampUpQueuingDelayThreshold\"d\"rampUpNBDCDCoolDownTime\"d\"rampUpAudioFractionCoolDownTime\"d\"basebandRATSwitchCoolDownTime\"d\"basebandAdaptationCrossTrafficRatio\"d\"rampUpNetworkUnstableCoolDownTime\"d\"autoResumeDurationAfterPaused\"d\"pauseOffChannelHighRatio\"d\"unpauseOffChannelLowRatio\"d\"oscillationDetectionEnabled\"B\"oscillationCoolDownTime\"d\"oscillationDeviationTierNumber\"i\"oscillationDeviationCountThreshold\"i\"preventBasebandRampDownCloseToKeyFrame\"B\"basebandRampDownSlowDownFactor\"i\"networkUnstableRTTThreshold\"d\"networkUnstablePLRThreshold\"d\"packetLossRateThresholdInitial\"d\"packetLossRateThresholdMin\"d\"packetLossRateThresholdMax\"d\"packetLossRateThresholdTarget\"d\"rampUpUplinkBLERThreshold\"I\"rampDownUplinkBLERThreshold\"I\"rampUpUplinkBLERDuration\"d\"rampDownUplinkBLERDuration\"d\"rampDownECNCERatioLow\"d\"rampDownECNCERatioMedium\"d\"rampDownECNCERatioHigh\"d\"rampDownECNBitrateHigh\"I\"rampDownECNBitrateMedium\"I\"rampDownECNBitrateLow\"I\"ceRatioDurationToRTTFactor\"d\"ceRatioDurationMin\"d\"ceRatioDurationMax\"d\"smartBrakeStrategy\"i\"congestionLevel\"{tagVCRateControlCongestionLevel=\"nowrdAcc\"{tagVCRateControlCongestionLevelThresholds=\"rampDown\"[5d]\"blockRampUp\"[5d]}\"bytesInFlight\"{tagVCRateControlCongestionLevelThresholds=\"rampDown\"[5d]\"blockRampUp\"[5d]}}\"machineLearningMode\"i\"machineLearningInitialRampUpOnly\"B\"maxBitrateOnlyConfig\"B\"minBitrateOnlyConfig\"B}"
+ "{tagVCRateControlAlgorithmConfig=I^Iiii[3i]iiiiiiiiiiiidddddddddddddddiiidddddddddddIIIII[5d]BBBBBBBBBBBBBBBBiBddididddidiiddidddddddddddddddddddddBdiiBiddddddIIdddddIIIdddi{tagVCRateControlCongestionLevel={tagVCRateControlCongestionLevelThresholds=[5d][5d]}{tagVCRateControlCongestionLevelThresholds=[5d][5d]}}iBBB}16@0:8"
- " [%s] %s:%d %@(%p) _captureFormatPrefer16By9ForSquare=%d"
- " [%s] %s:%d : %@"
- " [%s] %s:%d Existing settings: %@"
- " [%s] %s:%d Got notification for setAudioSessionProperties %@ on client [%p]"
- " [%s] %s:%d Requested settings: %@"
- " [%s] %s:%d _captureFormatPrefer16By9ForSquare=%d"
- " [%s] %s:%d config=%@"
- " [%s] %s:%d inDelegate=%@ config=%@"
- "2145.53.2"
- "@24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}16"
- "B24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}16"
- "T^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}},R,VaudioReceiver"
- "T{tagVCRateControlAlgorithmConfig=I^Iiii[3i]iiiiiiiiiiiiddddddddddddddiiidddddddddddIIIII[5d]BBBBBBBBBBBBBBBBiBddididddidiiddidddddddddddddddddddddBdiiBiddddddIIdddddIIIdddi{tagVCRateControlCongestionLevel={tagVCRateControlCongestionLevelThresholds=[5d][5d]}{tagVCRateControlCongestionLevelThresholds=[5d][5d]}}iBBB},R,N"
- "T{tagVCRateControlAlgorithmConfig=I^Iiii[3i]iiiiiiiiiiiiddddddddddddddiiidddddddddddIIIII[5d]BBBBBBBBBBBBBBBBiBddididddidiiddidddddddddddddddddddddBdiiBiddddddIIdddddIIIdddi{tagVCRateControlCongestionLevel={tagVCRateControlCongestionLevelThresholds=[5d][5d]}{tagVCRateControlCongestionLevelThresholds=[5d][5d]}}iBBB},R,N,V_config"
- "VCAudioPlayer [%s] %s:%d Audio Player initialized with format=%s samplesPerFrame=%u useFloats=%{BOOL}d bufferQueueManagementMode=%d timescaleAlgorithm=%d dtmfTonePlaybackEnabled=%d minJitterBufferQueueSize=%d dtmfEventCallbacksEnabled=%d enableEnhancedJBAdaptations=%d"
- "VCScreenCapture [%s] %s:%d First non idle frame received within 1/120 sec of the last idle frame, not adding frame capture signpost. PresentationTime=%f, interArrivalTime=%f "
- "VCScreenCapture [%s] %s:%d Frame PresentationTime %f going backwards with respect to previous frame PresentationTime %f. Dropping frame and not adding frame capture signpost."
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}"
- "^{tagVCAudioReceiver={tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}^v^{opaqueVCJitterBuffer}B{tagVCAudioFrameFormat={AudioStreamBasicDescription=dIIIIIIII}I}d{?=qiIq}{?=qiIq}I^{tagVCRealTimeThread}{tagVCAudioReceiverReportingTask=^{opaqueRTCReporting}i^{tagHANDLE}B}BB{_opaque_pthread_mutex_t=q[56c]}{_opaque_pthread_mutex_t=q[56c]}{tagVCAudioDecoderList=^{tagDecoderSettings}I}I{tagVCAudioReceiverStatistics=AIIIIIQQQfAIAIAIAIAIAIAIAI}^{tagWRMMetricsInfo}^?{tagVCAudioReceiverCallbackContext=^v^?^?}^?{tagVCAudioReceiverCallbackContext=^v^?^?}I[2{_RTCPPacketList=(tagNTP=Q{?=II})C[10^{tagRTCPPACKET}]^{OpaqueCMBlockBuffer}*QI[1472C][12S]CBQ{?=^{_RTCPPacketList}}}]dII[300{tagPacketHistoryInfo=ISIBB}]SS{_opaque_pthread_mutex_t=q[56c]}^{tagVCAudioReceiverStream}SSdBSS{_VCAudioCodecModeChangeEvent=iiiI{EVSRFParams=II}}BSSSIBBQB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}{tagVCJitterBufferWRMReportingMetrics=IIIIQQII}^vBdiddId^{tagVCAudioIssueDetector}ii[128I][128I]IIIi^{tagVCAudioDump}{tagVCAudioDumpPayloadInfo=BiBB^{AudioStreamBasicDescription}}BB^{tagVCAudioFrameDelay}dq^{tagVCOverlaySource}BdId{tagVCAudioReceiverInactiveFrameDetectionInfo=BBIf}}16@0:8"
- "_VCScreenCapture_handleFrameInternal"
- "kCVAViewpointCorrection_StereographicFisheyeStrength"
- "processAndSendIdleBlackFrame"
- "v24@0:8^{tagVCAudioReceiverConfig=I[4{tagVCAudioReceiverStream=^{tagHANDLE}SBB^{tagVCCryptor}iB^{tagVCAudioReceiver}^v^v}]^vIiIiiB^{opaqueRTCReporting}iB^{__CFString}^{__CFString}SBBBBBiB^v^?^?^?^?^{tagVCJBTargetEstimatorSynchronizer}^v^vIBIiBBQBB^{__CFString}BBBBiBB}16"
- "v24@0:8r^{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}16"
- "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}16@0:8"
- "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}24@0:8i16i20"
- "{tagVCAudioIOConfiguration=IIiiICB@iIIBQIqqQBB{tagVCAudioIODelegateContext=@^?^vq@@}{tagVCAudioIODelegateContext=@^?^vq@@}@BB@q@}28@0:8I16r^{tagVCAudioIODelegateContext=@^?^vq@@}20"
- "{tagVCRateControlAlgorithmConfig=\"serverBagProfileNumber\"I\"tierBitrates\"^I\"initialTierIndex\"i\"maxTierIndex\"i\"minTierIndex\"i\"softMaxTierIndex\"[3i]\"lowestNonEmergencyTierIndex\"i\"lowestNonEmergencyTierIndexWiFi\"i\"lowestEffectiveBWETierIndex\"i\"lowestTierIndexReactToNoServerActivity\"i\"rampUpTierNumber\"i\"rampDownTierNumber\"i\"rampUpAdditionalTierAtInitial\"i\"rampDownAdditionalTierAtInitial\"i\"rampDownBurstyLossThreshold\"i\"lowestTierForBurstyLossRampDown\"i\"lowestTierToEnableRateLimited\"i\"audioOnlyNoRateLimitedTierThreshold\"i\"rampDownNOWRDThreshold\"d\"rampDownNOWRDAccThreshold\"d\"rampDownAggressiveNOWRDThreshold\"d\"rampDownAggressiveNOWRDAccThreshold\"d\"rampDownConstantOWRDDuration\"d\"rampDownOvershootDuration\"d\"rampDownOvershootNextTierRatio\"d\"rampUpFrozenDuration\"d\"rampUpSettleDuration\"d\"rampUpOWRDThreshold\"d\"rampUpNOWRDThreshold\"d\"rampUpNOWRDAccThreshold\"d\"rampUpOverBandwidthCalmDuration\"d\"rampUpBlockedTimeout\"d\"rampUpOverBandwidthTierNumber\"i\"rampDownLossEventThreshold\"i\"rampDownLossEventBadTrendThreshold\"i\"rampDownLossEventThresholdRatio\"d\"rampDownLossEventWindowDuration\"d\"rampDownLossEventNOWRDThreshold\"d\"rampUpFrozenPLRThreshold\"d\"rampUpRateLimitedRatio\"d\"unstableRateLimitedDuration\"d\"congestionWaitDuration\"d\"owrdWindowDuration\"d\"owrdShortWindowDuration\"d\"minimumNOWRDTimeDifference\"d\"owrdInitialRampUpReadyDuration\"d\"owrdHistorySize\"I\"owrdMininumHistorySize\"I\"fastRampDownBitrateRange\"I\"fastRampUpBitrateRange\"I\"consecutiveRampDownThresholdForCongestion\"I\"continuousRampUpTimeFactor\"[5d]\"bytesInFlightAdaptationEnabled\"B\"useContinuousAdaptationAlgorithm\"B\"receivedBandwidthEstimationEnabled\"B\"basebandAdaptationEnabled\"B\"rateLimitedEnabled\"B\"randomRampUpFrozenDurationEnabled\"B\"oscillationAvoidanceEnabled\"B\"fastRampUpEnabled\"B\"blockRampUpInSaturatedNetworkEnabled\"B\"blockRampUpInBluetoothCoexEnabled\"B\"wifiEmergencyTiersEnabled\"B\"burstyTrafficEnabled\"B\"spatialTrafficEnabled\"B\"lowLatencyWANEnabled\"B\"lowBandwidthOptimizationEnabled\"B\"rampDownToActualSendBitrate\"B\"rampDownToActualSendBitrateMinTier\"i\"rampDownSuppressionEnabled\"B\"rampDownSuppressionMinRTT\"d\"rampDownSuppressionFactor\"d\"fastRampUpHighestTier\"i\"fastRampUpRTTRatio\"d\"fastRampUpTierGap\"i\"fastRampUpNetworkStableDuration\"d\"networkSaturatedRTTToMinRTTRatio\"d\"networkSaturatedOWRDToMinRTTRatio\"d\"networkSaturatedPersistFeedbackNumber\"i\"networkSaturatedRTTDecreasingThreshold\"d\"oscillationAvoidanceTierChangeThreshold\"i\"oscillationAvoidanceTiersHitThreshold\"i\"oscillationAvoidanceDurationRatio\"d\"oscillationAvoidanceDurationRatioAggressive\"d\"stabilizationScheme\"i\"rampDownNBDCDThreshold\"d\"rampDownAggressiveNBDCDThreshold\"d\"rampDownNormalizedQueuingDelayThreshold\"d\"rampDownMediumQueuingDelayThreshold\"d\"rampDownHighQueuingDelayThreshold\"d\"rampDownEmergencyTierCoolDownTime\"d\"rampDownWiFiEmergencyTierCoolDownTime\"d\"rampDownNWConnectionAvgDelayThresholdMin\"d\"rampDownNWConnectionAvgDelayThresholdMax\"d\"rampDownContinuousTierSpeedFactor\"d\"rampUpContinuousTierSpeedFactor\"d\"rampUpNBDCDThreshold\"d\"rampUpQueuingDelayThreshold\"d\"rampUpNBDCDCoolDownTime\"d\"rampUpAudioFractionCoolDownTime\"d\"basebandRATSwitchCoolDownTime\"d\"basebandAdaptationCrossTrafficRatio\"d\"rampUpNetworkUnstableCoolDownTime\"d\"autoResumeDurationAfterPaused\"d\"pauseOffChannelHighRatio\"d\"unpauseOffChannelLowRatio\"d\"oscillationDetectionEnabled\"B\"oscillationCoolDownTime\"d\"oscillationDeviationTierNumber\"i\"oscillationDeviationCountThreshold\"i\"preventBasebandRampDownCloseToKeyFrame\"B\"basebandRampDownSlowDownFactor\"i\"networkUnstableRTTThreshold\"d\"networkUnstablePLRThreshold\"d\"packetLossRateThresholdInitial\"d\"packetLossRateThresholdMin\"d\"packetLossRateThresholdMax\"d\"packetLossRateThresholdTarget\"d\"rampUpUplinkBLERThreshold\"I\"rampDownUplinkBLERThreshold\"I\"rampUpUplinkBLERDuration\"d\"rampDownUplinkBLERDuration\"d\"rampDownECNCERatioLow\"d\"rampDownECNCERatioMedium\"d\"rampDownECNCERatioHigh\"d\"rampDownECNBitrateHigh\"I\"rampDownECNBitrateMedium\"I\"rampDownECNBitrateLow\"I\"ceRatioDurationToRTTFactor\"d\"ceRatioDurationMin\"d\"ceRatioDurationMax\"d\"smartBrakeStrategy\"i\"congestionLevel\"{tagVCRateControlCongestionLevel=\"nowrdAcc\"{tagVCRateControlCongestionLevelThresholds=\"rampDown\"[5d]\"blockRampUp\"[5d]}\"bytesInFlight\"{tagVCRateControlCongestionLevelThresholds=\"rampDown\"[5d]\"blockRampUp\"[5d]}}\"machineLearningMode\"i\"machineLearningInitialRampUpOnly\"B\"maxBitrateOnlyConfig\"B\"minBitrateOnlyConfig\"B}"
- "{tagVCRateControlAlgorithmConfig=I^Iiii[3i]iiiiiiiiiiiiddddddddddddddiiidddddddddddIIIII[5d]BBBBBBBBBBBBBBBBiBddididddidiiddidddddddddddddddddddddBdiiBiddddddIIdddddIIIdddi{tagVCRateControlCongestionLevel={tagVCRateControlCongestionLevelThresholds=[5d][5d]}{tagVCRateControlCongestionLevelThresholds=[5d][5d]}}iBBB}16@0:8"

```
