## AVConference

> `/System/Library/PrivateFrameworks/AVConference.framework/AVConference`

```diff

-  __TEXT.__text: 0x7d1200
-  __TEXT.__objc_methlist: 0x3a8b0
-  __TEXT.__const: 0xc6c0
-  __TEXT.__cstring: 0x9e6f4
-  __TEXT.__oslogstring: 0x13dc25
+  __TEXT.__text: 0x7d4120
+  __TEXT.__objc_methlist: 0x3a8e8
+  __TEXT.__const: 0xc6b0
+  __TEXT.__cstring: 0x9ead7
+  __TEXT.__oslogstring: 0x13e750
   __TEXT.__gcc_except_tab: 0x2d08
   __TEXT.__ustring: 0x2d4
   __TEXT.__dlopen_cstrs: 0x56
-  __TEXT.__unwind_info: 0x123e0
+  __TEXT.__unwind_info: 0x12490
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7660
+  __DATA_CONST.__const: 0x7698
   __DATA_CONST.__objc_classlist: 0x14b8
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x510
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18bc0
+  __DATA_CONST.__objc_selrefs: 0x18bf0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x1268
   __DATA_CONST.__objc_arraydata: 0x27c8
-  __DATA_CONST.__got: 0x1a68
-  __AUTH_CONST.__const: 0x4468
-  __AUTH_CONST.__cfstring: 0x297e0
-  __AUTH_CONST.__objc_const: 0x6cd68
+  __DATA_CONST.__got: 0x1e30
+  __AUTH_CONST.__const: 0x4528
+  __AUTH_CONST.__cfstring: 0x298e0
+  __AUTH_CONST.__objc_const: 0x6cd98
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x52e0
   __AUTH_CONST.__objc_arrayobj: 0x1d88

   __AUTH_CONST.__objc_doubleobj: 0x1d0
   __AUTH_CONST.__objc_dictobj: 0x2d0
   __AUTH_CONST.__auth_got: 0x2c38
-  __AUTH.__objc_data: 0x2760
-  __DATA.__objc_ivar: 0x76a8
-  __DATA.__data: 0x80d8
-  __DATA.__bss: 0xef8
+  __AUTH.__data: 0xf8
+  __DATA.__objc_ivar: 0x76b8
+  __DATA.__data: 0x7d48
+  __DATA.__bss: 0x910
   __DATA.__common: 0x55
-  __DATA_DIRTY.__objc_data: 0xa7d0
-  __DATA_DIRTY.__data: 0x160
-  __DATA_DIRTY.__bss: 0x4c0
+  __DATA_DIRTY.__objc_data: 0xcf30
+  __DATA_DIRTY.__data: 0x420
+  __DATA_DIRTY.__bss: 0xaf0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /System/Library/PrivateFrameworks/FTServices.framework/FTServices
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
-  - /System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting

   - /usr/lib/libspindump.dylib
   - /usr/lib/libtailspin.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 35303
-  Symbols:   110846
-  CStrings:  39104
+  Functions: 35352
+  Symbols:   110985
+  CStrings:  39167
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__auth_got : content changed
Symbols:
+ +[VCHardwareSettings supportsHEVCDecodingForHomeKit]
+ -[AVAudioDevice isEligibleToBeDefaultDeviceForScope:]
+ -[AVCMediaStreamNegotiatorSettingsNearbySystemAudio setAudioDeviceUID]
+ -[VCHardwareSettingsEmbedded supportHEVCForHomeKit]
+ -[VCSessionParticipantLocal dispatchRemoteScreenAttributesDidChange:]
+ -[VCSessionParticipantLocal presenceConfigurationProviderHasVideoStreamInput:]
+ -[VCVideoCaptureServer _dispatchedNotifyFrameRateBeingThrottledForClients:newFrameRate:thermalLevelDidChange:powerLevelDidChange:]
+ -[VCVideoCaptureServer _dispatchedNotifyThermalChangeForClients:]
+ -[VCVideoStream onLocalDeviceOrientationDidChange]
+ -[VCVideoStream onRemoteScreenAspectRatiosDidChange:]
+ -[VCVideoStreamSendGroup onLocalDeviceOrientationDidChange]
+ -[VCVideoStreamSendGroup onRemoteScreenAttributesDidChange:]
+ -[VCVideoTransmitterBase onLocalDeviceOrientationDidChange]
+ -[VCVideoTransmitterBase onRemoteScreenAspectRatiosDidChange:]
+ -[VCVideoTransmitterDefault onLocalDeviceOrientationDidChange]
+ -[VCVideoTransmitterDefault onRemoteScreenAspectRatiosDidChange:]
+ GCC_except_table109
+ GCC_except_table122
+ GCC_except_table188
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table235
+ GCC_except_table244
+ GCC_except_table247
+ GCC_except_table250
+ GCC_except_table290
+ _LoadMediaAnalysis.frameworkLibrary
+ _LoadMediaAnalysis.loadPredicate
+ _LoadVideoProcessing.frameworkLibrary
+ _LoadVideoProcessing.loadPredicate
+ _OBJC_IVAR_$_AVCRateController._receiveTimeReportCount
+ _OBJC_IVAR_$_VCMediaControlInfoFaceTimeAudio._controlInfoJitterQueueSize
+ _OBJC_IVAR_$_VCRateControlAlgorithmBase._receiveJitterQueueSize
+ _OBJC_IVAR_$_VCRateSharingGroup._rateControlQueue
+ _OBJC_IVAR_$_VCScreenCapture._isROIRequiredInFrame
+ _OBJC_IVAR_$_VCSessionParticipantLocal._hksvHasVideoStreamInput
+ _OBJC_IVAR_$_VCVideoCaptureServer._previewImageRotationConverters
+ _OBJC_IVAR_$_VCVideoTransmitterDefault._encoderVisibleRectMatchesRemoteFOV
+ _OBJC_IVAR_$_VCVideoTransmitterDefault._hasReceivedRemoteScreenAttributesUpdate
+ _OBJC_IVAR_$_VCVideoTransmitterDefault._pendingAspectRatiosUpdateTrigger
+ _TPLocateSIPBody
+ _VCAbTestEnableGroupSessionLeavingAutoStop
+ _VCPCaptureAnalysisDurationKeyFunction
+ _VCPCaptureAnalysisSessionFunction
+ _VCPCaptureAnalysisSoundClassificationResultKeyFunction
+ _VCPCaptureAnalysisStartKeyFunction
+ _VCRTPInfoBuffer_Create
+ _VCRTPInfoBuffer_CreateElement
+ _VCRTPInfoBuffer_DestroyElement
+ _VCRTPInfoBuffer_InsertByTimestamp
+ _VCRTPInfoBuffer_PruneByJitterSize
+ _VideoTransmitter_SetAspectRatiosUpdateTrigger
+ __VCRTPInfoBufferClassRegister
+ __VCRTPInfoBufferFinalize
+ __VCRTPInfoBufferInit
+ __VCRTPInfoBuffer_LinkAfter
+ __VCRTPInfoBuffer_RemoveAllElements
+ __VideoReceiver_DequeueFromOrderedFrameForDecodeQueue
+ __VideoReceiver_DequeueFromOrderedFrameQueueForDisplay
+ __VideoReceiver_EnqueueDecodedFrameForDisplayToQueueInOrder
+ __VideoReceiver_EnqueueToOrderedQueue
+ ___50-[VCRateSharingGroup deregisterRateSharingClient:]_block_invoke
+ ___69-[VCSessionParticipantLocal dispatchRemoteScreenAttributesDidChange:]_block_invoke
+ ___LoadMediaAnalysis_block_invoke
+ ___LoadVideoProcessing_block_invoke
+ ___VCVideoCaptureServer_ApplyPressureLevelChanges_block_invoke_2
+ ___block_descriptor_40_e8_32o_e520_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8ls32l8
+ ___block_descriptor_40_e8_32o_e521_v16?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8ls32l8
+ ___block_descriptor_48_e8_32r40r_e520_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8lr32l8r40l8
+ _classVCPCaptureAnalysisSession
+ _constantVCPCaptureAnalysisDurationKey
+ _constantVCPCaptureAnalysisSoundClassificationResultKey
+ _constantVCPCaptureAnalysisStartKey
+ _getVCPCaptureAnalysisDurationKey
+ _getVCPCaptureAnalysisSessionClass
+ _getVCPCaptureAnalysisSoundClassificationResultKey
+ _getVCPCaptureAnalysisStartKey
+ _initVCPCaptureAnalysisDurationKey
+ _initVCPCaptureAnalysisSession
+ _initVCPCaptureAnalysisSoundClassificationResultKey
+ _initVCPCaptureAnalysisStartKey
+ _kVCExperimentEnableGroupSessionLeavingAutoStop
+ _kVCRTPInfoBufferClass
+ _objc_msgSend$_dispatchedNotifyFrameRateBeingThrottledForClients:newFrameRate:thermalLevelDidChange:powerLevelDidChange:
+ _objc_msgSend$_dispatchedNotifyThermalChangeForClients:
+ _objc_msgSend$canvasSize
+ _objc_msgSend$dispatchRemoteScreenAttributesDidChange:
+ _objc_msgSend$onLocalDeviceOrientationDidChange
+ _objc_msgSend$onRemoteScreenAspectRatiosDidChange:
+ _objc_msgSend$onRemoteScreenAttributesDidChange:
+ _objc_msgSend$presenceConfigurationProviderHasVideoStreamInput:
+ _objc_msgSend$setAudioDeviceUID
+ _objc_msgSend$supportHEVCForHomeKit
+ _objc_msgSend$supportsHEVCDecodingForHomeKit
- -[AVCMediaStreamNegotiatorSettingsNearbySystemAudio setAudioDeviceUIDForDeviceRole:]
- -[AVCVideoStreamConfig pdDecryptionContext]
- -[AVCVideoStreamConfig pdEncryptionContext]
- -[AVCVideoStreamConfig setPdDecryptionContext:]
- -[AVCVideoStreamConfig setPdEncryptionContext:]
- -[VCVideoStreamConfig deserializePDDecryptionContext]
- -[VCVideoStreamConfig pdDecryptionContext]
- -[VCVideoStreamConfig pdEncryptionContext]
- -[VCVideoStreamConfig setPdDecryptionContext:]
- -[VCVideoStreamConfig setPdEncryptionContext:]
- -[VCVideoTransmitterConfig pdEncryptionContext]
- -[VCVideoTransmitterConfig setPdEncryptionContext:]
- GCC_except_table104
- GCC_except_table155
- GCC_except_table183
- GCC_except_table185
- GCC_except_table187
- GCC_except_table205
- GCC_except_table230
- GCC_except_table239
- GCC_except_table242
- GCC_except_table245
- GCC_except_table285
- _OBJC_CLASS_$_VCPCaptureAnalysisSession
- _OBJC_IVAR_$_AVCVideoStreamConfig._pdDecryptionContext
- _OBJC_IVAR_$_AVCVideoStreamConfig._pdEncryptionContext
- _OBJC_IVAR_$_VCVideoCaptureServer._previewImageRotationConverter
- _OBJC_IVAR_$_VCVideoStreamConfig._pdDecryptionContext
- _OBJC_IVAR_$_VCVideoStreamConfig._pdEncryptionContext
- _OBJC_IVAR_$_VCVideoTransmitterConfig._pdEncryptionContext
- _VCPCaptureAnalysisDurationKey
- _VCPCaptureAnalysisSoundClassificationResultKey
- _VCPCaptureAnalysisStartKey
- ___block_descriptor_40_e8_32o_e520_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8ls32l8
- ___block_descriptor_40_e8_32o_e521_v16?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8ls32l8
- ___block_descriptor_48_e8_32r40r_e520_v208?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8lr32l8r40l8
- _objc_msgSend$deserializePDDecryptionContext
- _objc_msgSend$pdDecryptionContext
- _objc_msgSend$pdEncryptionContext
- _objc_msgSend$setAudioDeviceUIDForDeviceRole:
- _objc_msgSend$setPdEncryptionContext:
CStrings:
+ " [%s] %s:%d %@(%p) IDSDataChannelEventGroupSessionLeaving received"
+ " [%s] %s:%d %@(%p) _encoderVisibleRectMatchesRemoteFOV=%d"
+ " [%s] %s:%d %@(%p) new-path pass-through AR: portrait=%.0fx%.0f landscape=%.0fx%.0f"
+ " [%s] %s:%d %@(%p) skipping: nil remoteScreenAttributes"
+ " [%s] %s:%d %@(%p) skipping: zero ratio (orientation=%d)"
+ " [%s] %s:%d (%p) PixelBuffer became obsolete - frame index %d changed?"
+ " [%s] %s:%d (%p) PixelBuffer became obsolete after decode - frame index %d"
+ " [%s] %s:%d (%p) createPixelBufferForFrameIndex failed for frame %d"
+ " [%s] %s:%d Dropping IDS TCP link (type=%u) due to kVCDefaultDropIDSTCPLinks"
+ " [%s] %s:%d FRQ enqueue failed (%d), consecutive drops: %d"
+ " [%s] %s:%d IDSDataChannelEventGroupSessionLeaving received"
+ " [%s] %s:%d VCGetVCPacketWithVTPPacket failed with result=%x"
+ " [%s] %s:%d [AR_TX][%p] VisibleRectChanged: trigger=%s oldAR=%.3f newAR=%.3f oldRect=%s newRect=%s fPortrait=%d"
+ " [%s] %s:%d [AR_TX][%p] visibleRect shrink detected (prevArea=%.0f newArea=%.0f); requested keyframe"
+ " [%s] %s:%d _encoderVisibleRectMatchesRemoteFOV=%d"
+ " [%s] %s:%d buffer=%p _CFRuntimeCreateInstance failed"
+ " [%s] %s:%d new-path pass-through AR: portrait=%.0fx%.0f landscape=%.0fx%.0f"
+ " [%s] %s:%d outBuffer=NULL"
+ " [%s] %s:%d setInfo failed for controlInfo type=kVCMediaControlInfoTypeJitterQueueSize, for optionalControlInfo=%p in control info=%p for audio. error=%x"
+ " [%s] %s:%d skipping: nil remoteScreenAttributes"
+ " [%s] %s:%d skipping: zero ratio (orientation=%d)"
+ "### Failed to Soft Link: /System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis"
+ "### Failed to Soft Link: /System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing"
+ "%04X\t%u\t%u\t%u\t%u\t%u\t%u\t%u\t%u\t%04X\t%u\n"
+ "-[VCVideoStreamSendGroup onRemoteScreenAttributesDidChange:]"
+ "/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis"
+ "/System/Library/PrivateFrameworks/VideoProcessing.framework/VideoProcessing"
+ "2235.55.1"
+ "AVCRC [%s] %s:%d %@(%p) mode=%u, seq=%u, receiveTS=%u, reportTS=%u, isForMulticast=%u, endpointID=%u, reportCount=%u"
+ "AVCRC [%s] %s:%d mode=%u, seq=%u, receiveTS=%u, reportTS=%u, isForMulticast=%u, endpointID=%u, reportCount=%u"
+ "Group session leaving"
+ "LCTHO"
+ "SIP [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: body must not be NULL"
+ "SIP [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: bodyLen must not be NULL"
+ "SIP [%s] %s:%d /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AVConference/AVConference.subproj/Sources/SIP/Transport.c:%d: message must not be NULL"
+ "TPLocateSIPBody"
+ "VCAudioReceiver [%s] %s:%d @=@ Health: VCAudioReceiver VCAudioReceiver[%p] ParticipantID=%s erasure percentage=%.2f%% PLR percentage=%.2f%% current percentage:%.2f%% (rec:%u exp:%u, loss:%u) receiver(rtp=%u, bb=%u, unk=%u, dup=%u, drop=%u) jb(enc=%u, drop=%u) infobuf(rec=%u, exp:%u, drec=%u, dexp=%u)"
+ "VCAudioReceiver [%s] %s:%d Change shouldDeferLossWithInfoBuffer from old=%d to new=%d, headSeq=%u, tailSeq=%u, deferredTotalRecvCount=%d"
+ "VCAudioReceiver [%s] %s:%d VCAudioReceiver[%p] Failed to create the rtp info buffer"
+ "VCAudioReceiver [%s] %s:%d [%p] Cannot create info buffer element for seq=%u"
+ "VCAudioReceiver [%s] %s:%d receiver=%p, shouldDeferLoss=%u, prunedCount=%zu, isOOODetected=%d, deferredTotalRecvCount=%u, headSeq=%u, tailSeq=%u, seqDiff=%u, rtpBufferSize=%u, jitterQueueSize=%u, mediaTimestamp=%u, seq=%u, totalPacketReceived=%u"
+ "VCPCaptureAnalysisDurationKey"
+ "VCPCaptureAnalysisSession"
+ "VCPCaptureAnalysisSoundClassificationResultKey"
+ "VCPCaptureAnalysisStartKey"
+ "VCRTPInfoBufferClass"
+ "VCRTPInfoBuffer_Create"
+ "VCScreenCapture [%s] %s:%d No ROI attachment in the frame. Using the pixel buffer size as default ROI"
+ "VCSession [%s] %s:%d kVCTransportSessionGroupSessionLeaving received; A/B gate disabled or session is multiway, deferring to legacy AVCSession-stop"
+ "VCVideoCaptureServer [%s] %s:%d Failed to create VCImageRotationConverter cameraSessionType=%d"
+ "VideoTransmitter_SetAspectRatiosUpdateTrigger"
+ "_AVCRateController_PeriodicLogReceiveTimeReport"
+ "_RTCPParseVTPPacket"
+ "_RTPTransport_ParseVTPPacket"
+ "_VCAudioReceiver_UpdateRTPInfoBuffer"
+ "com.apple.AVConference.VCRateSharingGroup.rateControlQueue"
+ "connection-change"
+ "dropIDSTCPLinks"
+ "dual-capture-toggle"
+ "enableDeferredLossWithInfoBuffer"
+ "enableGroupSessionLeavingAutoStop"
+ "encoderVisibleRectMatchesRemoteFOV"
+ "initial"
+ "local-rotation"
+ "remote-screen-change"
+ "v16@?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8"
+ "v208@?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIddIII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIddIII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIddIII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8"
+ "vc-ab-testing-enable-group-session-leaving-auto-stop"
- " [%s] %s:%d %@(%p) pdDecryptionContext deserializing failed with error=%d"
- " [%s] %s:%d PixelBuffer became obsolete - frame index %d changed?"
- " [%s] %s:%d [AR_TX][%p] AspectRatio=%.3f, visibleRect changed from %s to %s, fPortrait = %d"
- " [%s] %s:%d pdDecryptionContext deserializing failed with error=%d"
- "%04X\t%u\t%u\t%u\t%u\t%u\t%u\t%u\t%04X\t%u\n"
- "-[VCVideoStreamConfig deserializePDDecryptionContext]"
- "2235.52.1.11.1"
- "VCAudioReceiver [%s] %s:%d @=@ Health: VCAudioReceiver VCAudioReceiver[%p] ParticipantID=%s erasure percentage=%.2f%% PLR percentage=%.2f%% current percentage:%.2f%% (rec:%u exp:%u, loss:%u) receiver(rtp=%u, bb=%u, unk=%u, dup=%u, drop=%u) jb(enc=%u, drop=%u)"
- "VCVideoCaptureServer [%s] %s:%d Failed to create VCImageRotationConverter"
- "v16@?0r^{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8"
- "v208@?0{tagVCStatisticsMessage=iidBBBB(?={?=IIIIIIIddddd[64c]i}{?=IIIIIIIIIIIIIddIIdIB{?=iIIIIdddII}{?=SBBI}{tagVCStatisticsECNStats=SS}{tagVCStatisticsECNStats=SS}BBI}{?=dddIIIIIQI}{?=IBBBIIdIB{?=iIIIIdddII}}{?=CIIIIIIIIIddddIIII}{?=IIId}{?=iIIIIdddII}{?=IIII}{?=IIIIIIBBIi}{?=IIIIfBBddIIIQ}{?=CCCCQQQIIIQiIS(?={?=CCSSCCCCCCCfBS[6I]CqSfffff}{?=CsscCCCCSSC})}{tagVCStatisticsVideoLossFeedback=ISCC}{tagVCStatisticsLocalRCEvent=ddI}{tagVCStatisticsReceiveTimeReport=IIISSIBBddIIII}{tagVCStatisticsAddRemoveEndPoint=IB})}8"
- "vcMediaStreamPDDecryptionContext"
- "vcMediaStreamPDEncryptionContext"

```
