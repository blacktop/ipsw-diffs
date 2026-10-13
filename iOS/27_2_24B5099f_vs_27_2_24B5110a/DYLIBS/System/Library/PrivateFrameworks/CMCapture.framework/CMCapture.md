## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-764.40.7.0.0
-  __TEXT.__text: 0x6805d0
-  __TEXT.__objc_methlist: 0x3dfa0
+764.42.8.0.0
+  __TEXT.__text: 0x6842a0
+  __TEXT.__objc_methlist: 0x3e180
   __TEXT.__const: 0x151800
-  __TEXT.__cstring: 0xafe64
-  __TEXT.__oslogstring: 0x545ce
+  __TEXT.__cstring: 0xb0599
+  __TEXT.__oslogstring: 0x54c86
   __TEXT.__gcc_except_tab: 0x3c74
   __TEXT.__ustring: 0x6ee
   __TEXT.__dlopen_cstrs: 0x7c9
-  __TEXT.__unwind_info: 0x18290
+  __TEXT.__unwind_info: 0x182f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x118e8
+  __DATA_CONST.__const: 0x118f8
   __DATA_CONST.__objc_classlist: 0x2048
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18d60
+  __DATA_CONST.__objc_selrefs: 0x18e40
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x1e78
-  __DATA_CONST.__objc_arraydata: 0x3cc8
-  __DATA_CONST.__got: 0x7908
-  __AUTH_CONST.__const: 0x4b00
-  __AUTH_CONST.__cfstring: 0x52ea0
-  __AUTH_CONST.__objc_const: 0xb1260
+  __DATA_CONST.__objc_arraydata: 0x3cd8
+  __DATA_CONST.__got: 0x79a8
+  __AUTH_CONST.__const: 0x4b40
+  __AUTH_CONST.__cfstring: 0x532e0
+  __AUTH_CONST.__objc_const: 0xb1658
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x6d08
-  __AUTH_CONST.__objc_arrayobj: 0x2d78
+  __AUTH_CONST.__objc_intobj: 0x6e58
+  __AUTH_CONST.__objc_arrayobj: 0x2d90
   __AUTH_CONST.__objc_floatobj: 0x2b0
   __AUTH_CONST.__objc_doubleobj: 0xb30
   __AUTH_CONST.__objc_dictobj: 0x17e8
-  __AUTH_CONST.__auth_got: 0x2f20
+  __AUTH_CONST.__auth_got: 0x2f28
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xcb98
-  __DATA.__data: 0x7f8
+  __DATA.__objc_ivar: 0xcbf4
+  __DATA.__data: 0x988
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x1860
   __DATA_DIRTY.__objc_data: 0x141e0
-  __DATA_DIRTY.__data: 0x67f8
+  __DATA_DIRTY.__data: 0x6678
   __DATA_DIRTY.__bss: 0x1260
   __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/Quagga.framework/Quagga
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
+  - /System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 39391
-  Symbols:   59374
-  CStrings:  21999
+  Functions: 39454
+  Symbols:   59487
+  CStrings:  22058
 
Symbols:
+ -[BWCameraStreamingMonitor _updateActiveClientSessionsForSessionID:clientSession:clientAuditToken:tccIdentity:mediaEnvironment:]
+ -[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]
+ -[BWDeferredCaptureContainerManager setUsesReducedPriorityFlushQueue:]
+ -[BWDeferredCaptureContainerManager usesReducedPriorityFlushQueue]
+ -[BWHVSScoringNode _shouldDropYUVInputSampleBufferForThermalMitigation:]
+ -[BWInferenceEngineControllerInput waitForAsyncProcessingAndReleaseImages]
+ -[BWMultiStreamCameraSourceNode setDeviceProximityDetectionDeviceTypes:]
+ -[BWMultiStreamCameraSourceNode setDeviceProximityDetectionTargetFrameRate:]
+ -[BWMultiStreamCameraSourceNode setLightSourceEstimationAmbientLuminance:]
+ -[BWMultiStreamCameraSourceNode setLightSourceEstimationTargetFrameRate:]
+ -[BWSecureMetadataOutputConfiguration deviceProximityDetectionDeviceTypes]
+ -[BWSecureMetadataOutputConfiguration deviceProximityDetectionEnabled]
+ -[BWSecureMetadataOutputConfiguration deviceProximityDetectionTargetFrameRate]
+ -[BWSecureMetadataOutputConfiguration lightSourceEstimationAmbientLuminance]
+ -[BWSecureMetadataOutputConfiguration lightSourceEstimationEnabled]
+ -[BWSecureMetadataOutputConfiguration lightSourceEstimationTargetFrameRate]
+ -[BWSecureMetadataOutputConfiguration perceptionTestModeEnabled]
+ -[BWSecureMetadataOutputConfiguration perceptionThumbnailChannelMetadataObjectTypes]
+ -[BWSecureMetadataOutputConfiguration perceptionThumbnailChannelTargetFrameRate]
+ -[BWSecureMetadataOutputConfiguration setDeviceProximityDetectionDeviceTypes:]
+ -[BWSecureMetadataOutputConfiguration setDeviceProximityDetectionEnabled:]
+ -[BWSecureMetadataOutputConfiguration setDeviceProximityDetectionTargetFrameRate:]
+ -[BWSecureMetadataOutputConfiguration setLightSourceEstimationAmbientLuminance:]
+ -[BWSecureMetadataOutputConfiguration setLightSourceEstimationEnabled:]
+ -[BWSecureMetadataOutputConfiguration setLightSourceEstimationTargetFrameRate:]
+ -[BWSecureMetadataOutputConfiguration setPerceptionTestModeEnabled:]
+ -[BWSecureMetadataOutputConfiguration setPerceptionThumbnailChannelMetadataObjectTypes:]
+ -[BWSecureMetadataOutputConfiguration setPerceptionThumbnailChannelTargetFrameRate:]
+ -[BWStillImageCoordinatorNode _calibrationCaptureSensorRawReleasedForRequest:]
+ -[BWVideoCompressorNode encoderPriorityInversionFixEnabled]
+ -[BWVideoCompressorNode setEncoderPriorityInversionFixEnabled:]
+ -[FigCaptureCameraSourcePipeline setDeviceProximityDetectionDeviceTypes:]
+ -[FigCaptureCameraSourcePipeline setDeviceProximityDetectionTargetFrameRate:]
+ -[FigCaptureCameraSourcePipeline setLightSourceEstimationAmbientLuminance:]
+ -[FigCaptureCameraSourcePipeline setLightSourceEstimationTargetFrameRate:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration bufferServicingPipelineStagePriority]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setBufferServicingPipelineStagePriority:]
+ -[FigCaptureSourceAttributes supportedMetadataIdentifiersForPerceptionThumbnailChannel]
+ -[FigMetadataObjectCaptureConnectionConfiguration deviceProximityDetectionDeviceTypes]
+ -[FigMetadataObjectCaptureConnectionConfiguration deviceProximityDetectionTargetFrameRate]
+ -[FigMetadataObjectCaptureConnectionConfiguration lightSourceEstimationAmbientLuminance]
+ -[FigMetadataObjectCaptureConnectionConfiguration lightSourceEstimationTargetFrameRate]
+ -[FigMetadataObjectCaptureConnectionConfiguration metadataIdentifiersForPerceptionThumbnailChannel]
+ -[FigMetadataObjectCaptureConnectionConfiguration perceptionTestModeEnabled]
+ -[FigMetadataObjectCaptureConnectionConfiguration setDeviceProximityDetectionDeviceTypes:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setDeviceProximityDetectionTargetFrameRate:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setLightSourceEstimationAmbientLuminance:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setLightSourceEstimationTargetFrameRate:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setMetadataIdentifiersForPerceptionThumbnailChannel:]
+ -[FigMetadataObjectCaptureConnectionConfiguration setPerceptionTestModeEnabled:]
+ GCC_except_table206
+ GCC_except_table240
+ GCC_except_table286
+ GCC_except_table348
+ GCC_except_table417
+ GCC_except_table418
+ GCC_except_table475
+ GCC_except_table527
+ GCC_except_table574
+ GCC_except_table576
+ GCC_except_table581
+ GCC_except_table584
+ GCC_except_table586
+ GCC_except_table588
+ GCC_except_table73
+ GCC_except_table82
+ _BWCreateSampleBufferWithDeviceProximityDetectionDictionary
+ _BWCreateSampleBufferWithLightSourceEstimationDictionary
+ _BWGetStillImageProcessingReducedFigThreadPriority
+ _FigCaptureClientApplicationIdentifierPerceptiond
+ _FigCaptureMetadataObjectConfigurationRequiresDeviceProximityDetection
+ _FigCaptureMetadataObjectConfigurationRequiresLightSourceEstimation
+ _FigCaptureSourceModulePersonalizationStatesByPosition
+ _FigCaptureSourceModulePersonalizationStatesByPosition.sOnceToken
+ _FigCaptureSourceModulePersonalizationStatesByPosition.sPersonalizationStatesByPosition
+ _FigCaptureSourceRemoteGetPersonalizationStateForPosition
+ _OBJC_IVAR_$_BWAssistiveOverlayNode._unpackedOutputPool
+ _OBJC_IVAR_$_BWCameraStreamingMonitorClientSession._activePortTypes
+ _OBJC_IVAR_$_BWDeferredCaptureContainerManager._flushQueueReducedPriority
+ _OBJC_IVAR_$_BWDeferredCaptureContainerManager._usesReducedPriorityFlushQueue
+ _OBJC_IVAR_$_BWHVSScoringNode._frameSkippingThermalMitigationEnabled
+ _OBJC_IVAR_$_BWHVSScoringNode._lastProcessedCaptureID
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._deviceProximityDetectionOutput
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._lightSourceEstimationOutput
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._deviceProximityDetectionDeviceTypes
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._deviceProximityDetectionEnabled
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._deviceProximityDetectionTargetFrameRate
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._lightSourceEstimationAmbientLuminance
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._lightSourceEstimationEnabled
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._lightSourceEstimationTargetFrameRate
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._perceptionTestModeEnabled
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._perceptionThumbnailChannelMetadataObjectTypes
+ _OBJC_IVAR_$_BWSecureMetadataOutputConfiguration._perceptionThumbnailChannelTargetFrameRate
+ _OBJC_IVAR_$_BWVideoCompressorNode._encoderPriorityInversionFixEnabled
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._bufferServicingPipelineStagePriority
+ _OBJC_IVAR_$_FigCaptureSourceAttributes._supportedMetadataIdentifiersForPerceptionThumbnailChannel
+ _OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._deviceProximityDetectionDeviceTypes
+ _OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._deviceProximityDetectionTargetFrameRate
+ _OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._lightSourceEstimationAmbientLuminance
+ _OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._lightSourceEstimationTargetFrameRate
+ _OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._metadataIdentifiersForPerceptionThumbnailChannel
+ _OBJC_IVAR_$_FigMetadataObjectCaptureConnectionConfiguration._perceptionTestModeEnabled
+ _SavageCamInterfaceCheckPersonalizationStatus
+ __OBJC_$_PROP_LIST_BWDeferredCaptureContainerManager
+ ___119-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]_block_invoke
+ ___59-[BWStillImageCoordinatorNode renderSampleBuffer:forInput:]_block_invoke_3
+ ___78-[BWStillImageCoordinatorNode _calibrationCaptureSensorRawReleasedForRequest:]_block_invoke
+ ___82-[FigCaptureSourceManager copySourcesWithType:clientAuditToken:clientIsBincompat:]_block_invoke
+ ___FigCaptureSourceModulePersonalizationStatesByPosition_block_invoke
+ ___block_descriptor_49_e8_32r40r_e35_v40?0^{__CFDictionary=}8{?=qiIq}16lr32l8r40l8
+ ___block_descriptor_97_e8_32o40o48o56b_e5_v8?0ls32l8s40l8s48l8s56l8
+ _captureSourceServer_handleCopyPersonalizationStateMessage
+ _cs_activePortTypesForCameraAttribution
+ _cs_activePortTypesForCameraAttributionForDevice
+ _cs_configurationContainsMultipleVideoSources
+ _cs_configurationNumberOfVideoSources
+ _fcu_personalizationStateForChannel
+ _kFigCaptureSampleBufferAttachmentKey_DeviceProximityDetection
+ _kFigCaptureSampleBufferAttachmentKey_LightSourceEstimation
+ _kFigCaptureSampleBufferMetadata_SmartFramingSuggestedFieldOfViewRectForSmartCrop
+ _kFigCaptureSourceAttributeKey_SupportedMetadataIdentifiersForPerceptionThumbnailChannel
+ _kFigCaptureSourceServerCopyPersonalizationStateMessagePayload_BackModulePersonalizationState
+ _kFigCaptureSourceServerCopyPersonalizationStateMessagePayload_FrontModulePersonalizationState
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureDeviceProximityDetectionConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureDeviceProximityDetectionEnabled
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureLightSourceEstimationConfiguration
+ _kFigCaptureStreamMetadataOutputConfigurationKey_SecureLightSourceEstimationEnabled
+ _kFigCaptureStreamMetadataOutputKey_SecureDetectedProximityDevices
+ _kFigCaptureStreamMetadataOutputKey_SecureLightSourceEstimation
+ _kFigCaptureStreamSecureDeviceProximityDetectionConfigurationKey_DeviceTypes
+ _kFigCaptureStreamSecureDeviceProximityDetectionConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamSecureFaceIDKey_FrameType
+ _kFigCaptureStreamSecureFaceIDKey_ProjectornMode
+ _kFigCaptureStreamSecureLightSourceEstimationConfigurationKey_AmbientLuminance
+ _kFigCaptureStreamSecureLightSourceEstimationConfigurationKey_TargetFrameRate
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_PerceptionTestModeEnabled
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_PerceptionThumbnailChannelMetadataObjectTypes
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_PerceptionThumbnailChannelTargetFrameRate
+ _kFigCaptureStreamSecureObjectDetectionConfigurationKey_TargetFrameRate
+ _kFigMetadataIdentifier_QuickTimeMetadataDeviceProximityDetection
+ _kFigMetadataIdentifier_QuickTimeMetadataLightSourceEstimation
+ _multiStreamCameraSourceNode_secureDeviceProximityDetectionServiceQueueCallback
+ _multiStreamCameraSourceNode_secureLightSourceEstimationServiceQueueCallback
- -[BWAssistiveOverlayNode _teardownRenderResources]
- -[BWAssistiveOverlayNode configurationWithID:updatedFormat:didBecomeLiveForInput:]
- -[BWAssistiveOverlayNode didReachEndOfDataForConfigurationID:input:]
- -[BWCameraStreamingMonitor _updateActiveClientSessionsForSessionID:clientSession:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:]
- -[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:completionHandler:]
- GCC_except_table205
- GCC_except_table239
- GCC_except_table282
- GCC_except_table346
- GCC_except_table353
- GCC_except_table414
- GCC_except_table415
- GCC_except_table469
- GCC_except_table521
- GCC_except_table568
- GCC_except_table570
- GCC_except_table575
- GCC_except_table578
- GCC_except_table580
- GCC_except_table582
- GCC_except_table80
- _OBJC_IVAR_$_BWAssistiveOverlayNode._hasPendingConfiguration
- _OBJC_IVAR_$_BWAssistiveOverlayNode._liveOutputVideoFormat
- _OBJC_IVAR_$_BWAssistiveOverlayNode._pendingOutputVideoFormat
- ___135-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:completionHandler:]_block_invoke
- ___49-[BWPhotonicEngineNode handleNodeError:forInput:]_block_invoke_2
- ___block_descriptor_105_e8_32o40o48o56o64b_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
- ___block_descriptor_48_e8_32r40r_e35_v40?0^{__CFDictionary=}8{?=qiIq}16lr32l8r40l8
- _cs_configurationContainsVideoSource
- _kFigCaptureStreamStreamingObjectDetectionConfigurationKey_TargetFrameRate
CStrings:
+ ", deviceProximityDetection:{deviceTypes: %@"
+ ", lightSourceEstimation:{ambientLuminance:%d"
+ ", metadataIdentifiersForPerception:%lu, testMode:%d"
+ ", targetFrameRate:%.2f}"
+ "-[BWAssistiveOverlayNode renderSampleBuffer:forInput:]"
+ "-[BWCameraStreamingMonitor _updateActiveClientSessionsForSessionID:clientSession:clientAuditToken:tccIdentity:mediaEnvironment:]"
+ "-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]_block_invoke"
+ "-[BWHVSScoringNode _handleYUVSampleBuffer:]"
+ "-[BWHVSScoringNode stopPersonalPhotographerSession]"
+ "-[BWPhotonicEngineNode handleNodeError:forInput:]_block_invoke"
+ "-[BWStillImageCoordinatorNode _calibrationCaptureSensorRawReleasedForRequest:]_block_invoke"
+ "<<<< BWAssistiveOverlayNode >>>> %s: Render path not available, emitting raw input"
+ "<<<< BWHVSScoringNode >>>> %s: Budget exhausted after frame %i, but Personal Photographer session sessionID:%u was already stopped, skipping duplicate finalization"
+ "<<<< BWHVSScoringNode >>>> %s: Ignoring stop: Personal Photographer session sessionID:%u already ended, skipping duplicate finalization"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: Received Face ID Result <rawFrameId: %@, metadataFrameId: %@, refFrameId: %@, frameType: %d, projectorMode: %d> %@"
+ "<<<< BWNRFProcessorController >>>> %s: Failed to allocate inference input pixel buffer for captureID:%lld (errorRecovery:%d, processInferenceInput:%d, inferenceInputForProcessing:%d)"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: SoftISPCal: Sensor raw released [%d / %d] for captureID:%lld"
+ "<<<< BWStillImageProcessingNode >>>> %s: Not emitting error %d for captureID:%lld; finishing processing of the current input instead"
+ "<<<< BWStillImageProcessingNode >>>> %s: The state has already been reset for %{public}@ input captureID:%{public}lld captureRequestIdentifier:%{public}@ (currentCaptureRequestIdentifier:%{public}@, currentCaptureID:%{public}lld), ignoring"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Device containing Reno suspended state changed, updating System Status activePortTypes: [%{public}@] -> [%{public}@]"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Increasing graph stop timeout of %@ to %d seconds for Personal Photographer under critical thermal pressure"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Received error %d during processing for captureID:%lld"
+ "<<<< FigCaptureSourceManager >>>> %s: Back wide module needs personalization, hiding %d source(s) that use it"
+ "AVMetadataObjectTypeDeviceProximityDetection"
+ "AVMetadataObjectTypeLightSourceEstimation"
+ "BWAssistiveOverlayNode unpacked output"
+ "DeviceProximityDetection"
+ "FigCaptureSourceRemoteGetPersonalizationStateForPosition"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10158"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10651"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11235"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11686"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11721"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11910"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11919"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11931"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11938"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11972"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:12038"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:12207"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:13103"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:13201"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:16366"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:19231"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:19619"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20502"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20926"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20928"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22831"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24231"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24263"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24419"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25173"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25198"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25447"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25804"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:6245"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7942"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7951"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9034"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9035"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9054"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9069"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9344"
+ "LastShownBuild:BWHVSScoringNode.m:1205"
+ "LastShownBuild:BWHVSScoringNode.m:2911"
+ "LastShownBuild:BWHVSScoringNode.m:2916"
+ "LastShownBuild:BWHVSScoringNode.m:2919"
+ "LastShownBuild:BWHVSScoringNode.m:2988"
+ "LastShownBuild:BWHVSScoringNode.m:3508"
+ "LastShownBuild:BWInferenceEngineController.m:220"
+ "LastShownBuild:BWInferenceEngineController.m:221"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:13942"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:13958"
+ "LastShownBuild:BWPhotonicEngineNode.m:2155"
+ "LastShownBuild:BWPhotonicEngineNode.m:2209"
+ "LastShownBuild:BWPhotonicEngineNode.m:2514"
+ "LastShownBuild:BWPhotonicEngineNode.m:2524"
+ "LastShownBuild:BWPhotonicEngineNode.m:3068"
+ "LastShownBuild:BWPhotonicEngineNode.m:3108"
+ "LastShownBuild:BWPhotonicEngineNode.m:3845"
+ "LastShownBuild:BWPhotonicEngineNode.m:3860"
+ "LastShownBuild:BWPhotonicEngineNode.m:3962"
+ "LastShownBuild:BWPhotonicEngineNode.m:3987"
+ "LastShownBuild:BWPhotonicEngineNode.m:5060"
+ "LastShownBuild:BWPhotonicEngineNode.m:5840"
+ "LastShownBuild:BWPhotonicEngineNode.m:5865"
+ "LastShownBuild:BWPhotonicEngineNode.m:7978"
+ "LastShownBuild:BWPhotonicEngineNode.m:7980"
+ "LastShownBuild:BWPhotonicEngineNode.m:9488"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1480"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1487"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1557"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1663"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1674"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:2320"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:3975"
+ "LastShownBuild:FigCaptureDeferredProcessingEngine.m:1792"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1719"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1725"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1726"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1730"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1878"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1884"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1887"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2034"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3130"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3250"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3251"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3424"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3427"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3617"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3621"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3667"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4694"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4700"
+ "LastShownBuild:FigCaptureSession.m:10100"
+ "LastShownBuild:FigCaptureSession.m:1018"
+ "LastShownBuild:FigCaptureSession.m:10444"
+ "LastShownBuild:FigCaptureSession.m:10652"
+ "LastShownBuild:FigCaptureSession.m:11477"
+ "LastShownBuild:FigCaptureSession.m:11672"
+ "LastShownBuild:FigCaptureSession.m:16120"
+ "LastShownBuild:FigCaptureSession.m:19509"
+ "LastShownBuild:FigCaptureSession.m:21074"
+ "LastShownBuild:FigCaptureSession.m:21077"
+ "LastShownBuild:FigCaptureSession.m:26454"
+ "LastShownBuild:FigCaptureSession.m:26467"
+ "LastShownBuild:FigCaptureSession.m:28547"
+ "LastShownBuild:FigCaptureSession.m:29556"
+ "LastShownBuild:FigCaptureSession.m:4631"
+ "LastShownBuild:FigCaptureSession.m:5282"
+ "LastShownBuild:FigCaptureSession.m:9376"
+ "LastShownBuild:FigCaptureSession.m:9382"
+ "LastShownBuild:FigCaptureSession.m:9385"
+ "LastShownBuild:FigCaptureSession.m:9388"
+ "LastShownBuild:FigCaptureSession.m:9391"
+ "LastShownBuild:FigCaptureSession.m:9402"
+ "LastShownBuild:FigCaptureSession.m:9405"
+ "LastShownBuild:FigCaptureSession.m:9413"
+ "LastShownBuild:FigCaptureSession.m:9431"
+ "LastShownBuild:FigCaptureSession.m:9476"
+ "LastShownBuild:FigCaptureSession.m:9480"
+ "LastShownBuild:FigCaptureSession.m:9504"
+ "LastShownBuild:FigCaptureSession.m:9519"
+ "LastShownBuild:FigCaptureSession.m:9523"
+ "LastShownBuild:FigCaptureSession.m:9526"
+ "LastShownBuild:FigCaptureSession.m:9650"
+ "LastShownBuild:FigCaptureSession.m:9656"
+ "LastShownBuild:FigCaptureSession.m:9682"
+ "LastShownBuild:FigCaptureSession.m:9694"
+ "LastShownBuild:FigCaptureSourceServer.m:2042"
+ "LastShownBuild:FigCaptureSourceServer.m:2067"
+ "LastShownBuild:FigCaptureUtilities.m:1139"
+ "LastShownBuild:FigCaptureUtilities.m:1265"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10158"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10651"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11235"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11686"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11721"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11910"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11919"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11931"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11938"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11972"
+ "LastShownDate:BWFigVideoCaptureDevice.m:12038"
+ "LastShownDate:BWFigVideoCaptureDevice.m:12207"
+ "LastShownDate:BWFigVideoCaptureDevice.m:13103"
+ "LastShownDate:BWFigVideoCaptureDevice.m:13201"
+ "LastShownDate:BWFigVideoCaptureDevice.m:16366"
+ "LastShownDate:BWFigVideoCaptureDevice.m:19231"
+ "LastShownDate:BWFigVideoCaptureDevice.m:19619"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20502"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20926"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20928"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22831"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24231"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24263"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24419"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25173"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25198"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25447"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25804"
+ "LastShownDate:BWFigVideoCaptureDevice.m:6245"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7942"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7951"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9034"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9035"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9054"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9069"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9344"
+ "LastShownDate:BWHVSScoringNode.m:1205"
+ "LastShownDate:BWHVSScoringNode.m:2911"
+ "LastShownDate:BWHVSScoringNode.m:2916"
+ "LastShownDate:BWHVSScoringNode.m:2919"
+ "LastShownDate:BWHVSScoringNode.m:2988"
+ "LastShownDate:BWHVSScoringNode.m:3508"
+ "LastShownDate:BWInferenceEngineController.m:220"
+ "LastShownDate:BWInferenceEngineController.m:221"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:13942"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:13958"
+ "LastShownDate:BWPhotonicEngineNode.m:2155"
+ "LastShownDate:BWPhotonicEngineNode.m:2209"
+ "LastShownDate:BWPhotonicEngineNode.m:2514"
+ "LastShownDate:BWPhotonicEngineNode.m:2524"
+ "LastShownDate:BWPhotonicEngineNode.m:3068"
+ "LastShownDate:BWPhotonicEngineNode.m:3108"
+ "LastShownDate:BWPhotonicEngineNode.m:3845"
+ "LastShownDate:BWPhotonicEngineNode.m:3860"
+ "LastShownDate:BWPhotonicEngineNode.m:3962"
+ "LastShownDate:BWPhotonicEngineNode.m:3987"
+ "LastShownDate:BWPhotonicEngineNode.m:5060"
+ "LastShownDate:BWPhotonicEngineNode.m:5840"
+ "LastShownDate:BWPhotonicEngineNode.m:5865"
+ "LastShownDate:BWPhotonicEngineNode.m:7978"
+ "LastShownDate:BWPhotonicEngineNode.m:7980"
+ "LastShownDate:BWPhotonicEngineNode.m:9488"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1480"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1487"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1557"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1663"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1674"
+ "LastShownDate:BWStillImageCoordinatorNode.m:2320"
+ "LastShownDate:BWStillImageCoordinatorNode.m:3975"
+ "LastShownDate:FigCaptureDeferredProcessingEngine.m:1792"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1719"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1725"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1726"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1730"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1878"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1884"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1887"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2034"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3130"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3250"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3251"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3424"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3427"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3617"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3621"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3667"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4694"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4700"
+ "LastShownDate:FigCaptureSession.m:10100"
+ "LastShownDate:FigCaptureSession.m:1018"
+ "LastShownDate:FigCaptureSession.m:10444"
+ "LastShownDate:FigCaptureSession.m:10652"
+ "LastShownDate:FigCaptureSession.m:11477"
+ "LastShownDate:FigCaptureSession.m:11672"
+ "LastShownDate:FigCaptureSession.m:16120"
+ "LastShownDate:FigCaptureSession.m:19509"
+ "LastShownDate:FigCaptureSession.m:21074"
+ "LastShownDate:FigCaptureSession.m:21077"
+ "LastShownDate:FigCaptureSession.m:26454"
+ "LastShownDate:FigCaptureSession.m:26467"
+ "LastShownDate:FigCaptureSession.m:28547"
+ "LastShownDate:FigCaptureSession.m:29556"
+ "LastShownDate:FigCaptureSession.m:4631"
+ "LastShownDate:FigCaptureSession.m:5282"
+ "LastShownDate:FigCaptureSession.m:9376"
+ "LastShownDate:FigCaptureSession.m:9382"
+ "LastShownDate:FigCaptureSession.m:9385"
+ "LastShownDate:FigCaptureSession.m:9388"
+ "LastShownDate:FigCaptureSession.m:9391"
+ "LastShownDate:FigCaptureSession.m:9402"
+ "LastShownDate:FigCaptureSession.m:9405"
+ "LastShownDate:FigCaptureSession.m:9413"
+ "LastShownDate:FigCaptureSession.m:9431"
+ "LastShownDate:FigCaptureSession.m:9476"
+ "LastShownDate:FigCaptureSession.m:9480"
+ "LastShownDate:FigCaptureSession.m:9504"
+ "LastShownDate:FigCaptureSession.m:9519"
+ "LastShownDate:FigCaptureSession.m:9523"
+ "LastShownDate:FigCaptureSession.m:9526"
+ "LastShownDate:FigCaptureSession.m:9650"
+ "LastShownDate:FigCaptureSession.m:9656"
+ "LastShownDate:FigCaptureSession.m:9682"
+ "LastShownDate:FigCaptureSession.m:9694"
+ "LastShownDate:FigCaptureSourceServer.m:2042"
+ "LastShownDate:FigCaptureSourceServer.m:2067"
+ "LastShownDate:FigCaptureUtilities.m:1139"
+ "LastShownDate:FigCaptureUtilities.m:1265"
+ "LightSourceEstimation"
+ "MachThreadPriorityForThreadEmittingFrames"
+ "SupportedMetadataIdentifiersForPerceptionThumbnailChannel"
+ "backModulePersonalizationState"
+ "bufferServicingPipelineStagePriority"
+ "bwmscsn_printMetadataPayload"
+ "com.apple.ClockFacePosters.DimensionalAnalogPosterExtension"
+ "com.apple.Motif"
+ "com.apple.MotifTools"
+ "com.apple.coremedia.deferred.containermanager.flush.reduced-priority"
+ "com.apple.fatool"
+ "com.apple.homepodsensed"
+ "com.apple.pebblefusiond"
+ "com.apple.peopleawarenessd"
+ "com.apple.perceptiond"
+ "com.apple.private.avfoundation.capture.query-module-sealed-state.allow"
+ "com.apple.private.cmcapture.frame-sender-server-broker"
+ "description=CameraCapture-764.42.8"
+ "deviceProximityDetection"
+ "deviceProximityDetectionDeviceTypes"
+ "deviceProximityDetectionSupported"
+ "deviceProximityDetectionTargetFrameRate"
+ "deviceProximityDetectionTargetFrameRate (%g -> %g)"
+ "frontModulePersonalizationState"
+ "lightSourceEstimation"
+ "lightSourceEstimationAmbientLuminance"
+ "lightSourceEstimationAmbientLuminance (%u -> %u)"
+ "lightSourceEstimationTargetFrameRate"
+ "lightSourceEstimationTargetFrameRate (%g -> %g)"
+ "lite_shareddata"
+ "metadataIdentifiersForPerceptionThumbnailChannel"
+ "perceptionTestModeEnabled"
+ "perceptionTestModeEnabled (%d -> %d)"
+ "perceptionThumbnailChannelSupported"
+ "tracked_faces"
- "-[BWCameraStreamingMonitor _updateActiveClientSessionsForSessionID:clientSession:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:]"
- "-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:completionHandler:]_block_invoke"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10162"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10655"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11239"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11690"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11725"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11914"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11923"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11935"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11942"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11976"
- "LastShownBuild:BWFigVideoCaptureDevice.m:12042"
- "LastShownBuild:BWFigVideoCaptureDevice.m:12211"
- "LastShownBuild:BWFigVideoCaptureDevice.m:13107"
- "LastShownBuild:BWFigVideoCaptureDevice.m:13205"
- "LastShownBuild:BWFigVideoCaptureDevice.m:16370"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19235"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19623"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20506"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20932"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20934"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22835"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24235"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24267"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24423"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25177"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25202"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25451"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25808"
- "LastShownBuild:BWFigVideoCaptureDevice.m:6249"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7946"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7955"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9038"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9039"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9058"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9073"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9348"
- "LastShownBuild:BWHVSScoringNode.m:1194"
- "LastShownBuild:BWHVSScoringNode.m:2806"
- "LastShownBuild:BWHVSScoringNode.m:2811"
- "LastShownBuild:BWHVSScoringNode.m:2814"
- "LastShownBuild:BWHVSScoringNode.m:2883"
- "LastShownBuild:BWHVSScoringNode.m:3403"
- "LastShownBuild:BWInferenceEngineController.m:196"
- "LastShownBuild:BWInferenceEngineController.m:197"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:13947"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:13963"
- "LastShownBuild:BWPhotonicEngineNode.m:2152"
- "LastShownBuild:BWPhotonicEngineNode.m:2206"
- "LastShownBuild:BWPhotonicEngineNode.m:2511"
- "LastShownBuild:BWPhotonicEngineNode.m:2521"
- "LastShownBuild:BWPhotonicEngineNode.m:3065"
- "LastShownBuild:BWPhotonicEngineNode.m:3102"
- "LastShownBuild:BWPhotonicEngineNode.m:3842"
- "LastShownBuild:BWPhotonicEngineNode.m:3857"
- "LastShownBuild:BWPhotonicEngineNode.m:3959"
- "LastShownBuild:BWPhotonicEngineNode.m:3984"
- "LastShownBuild:BWPhotonicEngineNode.m:5057"
- "LastShownBuild:BWPhotonicEngineNode.m:5837"
- "LastShownBuild:BWPhotonicEngineNode.m:5862"
- "LastShownBuild:BWPhotonicEngineNode.m:7975"
- "LastShownBuild:BWPhotonicEngineNode.m:7977"
- "LastShownBuild:BWPhotonicEngineNode.m:9485"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1465"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1472"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1542"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1648"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1659"
- "LastShownBuild:BWStillImageCoordinatorNode.m:2305"
- "LastShownBuild:BWStillImageCoordinatorNode.m:3946"
- "LastShownBuild:FigCaptureDeferredProcessingEngine.m:1791"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1711"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1717"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1718"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1722"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1870"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1876"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1879"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2026"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3122"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3242"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3243"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3416"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3419"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3609"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3613"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3659"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4686"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4692"
- "LastShownBuild:FigCaptureSession.m:10016"
- "LastShownBuild:FigCaptureSession.m:1017"
- "LastShownBuild:FigCaptureSession.m:10350"
- "LastShownBuild:FigCaptureSession.m:10558"
- "LastShownBuild:FigCaptureSession.m:11383"
- "LastShownBuild:FigCaptureSession.m:11578"
- "LastShownBuild:FigCaptureSession.m:15977"
- "LastShownBuild:FigCaptureSession.m:19384"
- "LastShownBuild:FigCaptureSession.m:20949"
- "LastShownBuild:FigCaptureSession.m:20952"
- "LastShownBuild:FigCaptureSession.m:26327"
- "LastShownBuild:FigCaptureSession.m:26340"
- "LastShownBuild:FigCaptureSession.m:28420"
- "LastShownBuild:FigCaptureSession.m:29423"
- "LastShownBuild:FigCaptureSession.m:4573"
- "LastShownBuild:FigCaptureSession.m:5224"
- "LastShownBuild:FigCaptureSession.m:9292"
- "LastShownBuild:FigCaptureSession.m:9298"
- "LastShownBuild:FigCaptureSession.m:9301"
- "LastShownBuild:FigCaptureSession.m:9304"
- "LastShownBuild:FigCaptureSession.m:9307"
- "LastShownBuild:FigCaptureSession.m:9318"
- "LastShownBuild:FigCaptureSession.m:9321"
- "LastShownBuild:FigCaptureSession.m:9329"
- "LastShownBuild:FigCaptureSession.m:9347"
- "LastShownBuild:FigCaptureSession.m:9392"
- "LastShownBuild:FigCaptureSession.m:9396"
- "LastShownBuild:FigCaptureSession.m:9420"
- "LastShownBuild:FigCaptureSession.m:9435"
- "LastShownBuild:FigCaptureSession.m:9439"
- "LastShownBuild:FigCaptureSession.m:9442"
- "LastShownBuild:FigCaptureSession.m:9566"
- "LastShownBuild:FigCaptureSession.m:9572"
- "LastShownBuild:FigCaptureSession.m:9598"
- "LastShownBuild:FigCaptureSession.m:9610"
- "LastShownBuild:FigCaptureSourceServer.m:1907"
- "LastShownBuild:FigCaptureSourceServer.m:1932"
- "LastShownBuild:FigCaptureUtilities.m:1133"
- "LastShownBuild:FigCaptureUtilities.m:1259"
- "LastShownDate:BWFigVideoCaptureDevice.m:10162"
- "LastShownDate:BWFigVideoCaptureDevice.m:10655"
- "LastShownDate:BWFigVideoCaptureDevice.m:11239"
- "LastShownDate:BWFigVideoCaptureDevice.m:11690"
- "LastShownDate:BWFigVideoCaptureDevice.m:11725"
- "LastShownDate:BWFigVideoCaptureDevice.m:11914"
- "LastShownDate:BWFigVideoCaptureDevice.m:11923"
- "LastShownDate:BWFigVideoCaptureDevice.m:11935"
- "LastShownDate:BWFigVideoCaptureDevice.m:11942"
- "LastShownDate:BWFigVideoCaptureDevice.m:11976"
- "LastShownDate:BWFigVideoCaptureDevice.m:12042"
- "LastShownDate:BWFigVideoCaptureDevice.m:12211"
- "LastShownDate:BWFigVideoCaptureDevice.m:13107"
- "LastShownDate:BWFigVideoCaptureDevice.m:13205"
- "LastShownDate:BWFigVideoCaptureDevice.m:16370"
- "LastShownDate:BWFigVideoCaptureDevice.m:19235"
- "LastShownDate:BWFigVideoCaptureDevice.m:19623"
- "LastShownDate:BWFigVideoCaptureDevice.m:20506"
- "LastShownDate:BWFigVideoCaptureDevice.m:20932"
- "LastShownDate:BWFigVideoCaptureDevice.m:20934"
- "LastShownDate:BWFigVideoCaptureDevice.m:22835"
- "LastShownDate:BWFigVideoCaptureDevice.m:24235"
- "LastShownDate:BWFigVideoCaptureDevice.m:24267"
- "LastShownDate:BWFigVideoCaptureDevice.m:24423"
- "LastShownDate:BWFigVideoCaptureDevice.m:25177"
- "LastShownDate:BWFigVideoCaptureDevice.m:25202"
- "LastShownDate:BWFigVideoCaptureDevice.m:25451"
- "LastShownDate:BWFigVideoCaptureDevice.m:25808"
- "LastShownDate:BWFigVideoCaptureDevice.m:6249"
- "LastShownDate:BWFigVideoCaptureDevice.m:7946"
- "LastShownDate:BWFigVideoCaptureDevice.m:7955"
- "LastShownDate:BWFigVideoCaptureDevice.m:9038"
- "LastShownDate:BWFigVideoCaptureDevice.m:9039"
- "LastShownDate:BWFigVideoCaptureDevice.m:9058"
- "LastShownDate:BWFigVideoCaptureDevice.m:9073"
- "LastShownDate:BWFigVideoCaptureDevice.m:9348"
- "LastShownDate:BWHVSScoringNode.m:1194"
- "LastShownDate:BWHVSScoringNode.m:2806"
- "LastShownDate:BWHVSScoringNode.m:2811"
- "LastShownDate:BWHVSScoringNode.m:2814"
- "LastShownDate:BWHVSScoringNode.m:2883"
- "LastShownDate:BWHVSScoringNode.m:3403"
- "LastShownDate:BWInferenceEngineController.m:196"
- "LastShownDate:BWInferenceEngineController.m:197"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:13947"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:13963"
- "LastShownDate:BWPhotonicEngineNode.m:2152"
- "LastShownDate:BWPhotonicEngineNode.m:2206"
- "LastShownDate:BWPhotonicEngineNode.m:2511"
- "LastShownDate:BWPhotonicEngineNode.m:2521"
- "LastShownDate:BWPhotonicEngineNode.m:3065"
- "LastShownDate:BWPhotonicEngineNode.m:3102"
- "LastShownDate:BWPhotonicEngineNode.m:3842"
- "LastShownDate:BWPhotonicEngineNode.m:3857"
- "LastShownDate:BWPhotonicEngineNode.m:3959"
- "LastShownDate:BWPhotonicEngineNode.m:3984"
- "LastShownDate:BWPhotonicEngineNode.m:5057"
- "LastShownDate:BWPhotonicEngineNode.m:5837"
- "LastShownDate:BWPhotonicEngineNode.m:5862"
- "LastShownDate:BWPhotonicEngineNode.m:7975"
- "LastShownDate:BWPhotonicEngineNode.m:7977"
- "LastShownDate:BWPhotonicEngineNode.m:9485"
- "LastShownDate:BWStillImageCoordinatorNode.m:1465"
- "LastShownDate:BWStillImageCoordinatorNode.m:1472"
- "LastShownDate:BWStillImageCoordinatorNode.m:1542"
- "LastShownDate:BWStillImageCoordinatorNode.m:1648"
- "LastShownDate:BWStillImageCoordinatorNode.m:1659"
- "LastShownDate:BWStillImageCoordinatorNode.m:2305"
- "LastShownDate:BWStillImageCoordinatorNode.m:3946"
- "LastShownDate:FigCaptureDeferredProcessingEngine.m:1791"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1711"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1717"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1718"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1722"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1870"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1876"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1879"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2026"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3122"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3242"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3243"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3416"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3419"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3609"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3613"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3659"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4686"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4692"
- "LastShownDate:FigCaptureSession.m:10016"
- "LastShownDate:FigCaptureSession.m:1017"
- "LastShownDate:FigCaptureSession.m:10350"
- "LastShownDate:FigCaptureSession.m:10558"
- "LastShownDate:FigCaptureSession.m:11383"
- "LastShownDate:FigCaptureSession.m:11578"
- "LastShownDate:FigCaptureSession.m:15977"
- "LastShownDate:FigCaptureSession.m:19384"
- "LastShownDate:FigCaptureSession.m:20949"
- "LastShownDate:FigCaptureSession.m:20952"
- "LastShownDate:FigCaptureSession.m:26327"
- "LastShownDate:FigCaptureSession.m:26340"
- "LastShownDate:FigCaptureSession.m:28420"
- "LastShownDate:FigCaptureSession.m:29423"
- "LastShownDate:FigCaptureSession.m:4573"
- "LastShownDate:FigCaptureSession.m:5224"
- "LastShownDate:FigCaptureSession.m:9292"
- "LastShownDate:FigCaptureSession.m:9298"
- "LastShownDate:FigCaptureSession.m:9301"
- "LastShownDate:FigCaptureSession.m:9304"
- "LastShownDate:FigCaptureSession.m:9307"
- "LastShownDate:FigCaptureSession.m:9318"
- "LastShownDate:FigCaptureSession.m:9321"
- "LastShownDate:FigCaptureSession.m:9329"
- "LastShownDate:FigCaptureSession.m:9347"
- "LastShownDate:FigCaptureSession.m:9392"
- "LastShownDate:FigCaptureSession.m:9396"
- "LastShownDate:FigCaptureSession.m:9420"
- "LastShownDate:FigCaptureSession.m:9435"
- "LastShownDate:FigCaptureSession.m:9439"
- "LastShownDate:FigCaptureSession.m:9442"
- "LastShownDate:FigCaptureSession.m:9566"
- "LastShownDate:FigCaptureSession.m:9572"
- "LastShownDate:FigCaptureSession.m:9598"
- "LastShownDate:FigCaptureSession.m:9610"
- "LastShownDate:FigCaptureSourceServer.m:1907"
- "LastShownDate:FigCaptureSourceServer.m:1932"
- "LastShownDate:FigCaptureUtilities.m:1133"
- "LastShownDate:FigCaptureUtilities.m:1259"
- "description=CameraCapture-764.40.7"
- "endpointPID != 0"
```
