## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

 664.2.10.0.0
-  __TEXT.__text: 0x57c2c4
-  __TEXT.__auth_stubs: 0x5090
-  __TEXT.__objc_methlist: 0x32448
-  __TEXT.__const: 0x150850
-  __TEXT.__cstring: 0x8c436
-  __TEXT.__oslogstring: 0x3983f
-  __TEXT.__gcc_except_tab: 0x2a6c
+  __TEXT.__text: 0x5abbf0
+  __TEXT.__auth_stubs: 0x52a0
+  __TEXT.__objc_methlist: 0x336c0
+  __TEXT.__const: 0x1510a0
+  __TEXT.__cstring: 0x905da
+  __TEXT.__oslogstring: 0x3c474
+  __TEXT.__gcc_except_tab: 0x2adc
   __TEXT.__dlopen_cstrs: 0x65d
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0xdff0
+  __TEXT.__unwind_info: 0xe4e8
   __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x812f
-  __TEXT.__objc_methname: 0xa00eb
-  __TEXT.__objc_methtype: 0x15875
-  __TEXT.__objc_stubs: 0x45060
-  __DATA_CONST.__got: 0x6640
-  __DATA_CONST.__const: 0xdc78
-  __DATA_CONST.__objc_classlist: 0x1b30
+  __TEXT.__objc_classname: 0x833f
+  __TEXT.__objc_methname: 0xa4bd5
+  __TEXT.__objc_methtype: 0x16128
+  __TEXT.__objc_stubs: 0x47200
+  __DATA_CONST.__got: 0x6860
+  __DATA_CONST.__const: 0xe790
+  __DATA_CONST.__objc_classlist: 0x1b98
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x5a8
+  __DATA_CONST.__objc_protolist: 0x5c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13dd0
+  __DATA_CONST.__objc_selrefs: 0x145a8
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x1998
-  __DATA_CONST.__objc_arraydata: 0x3660
-  __AUTH_CONST.__auth_got: 0x2858
-  __AUTH_CONST.__const: 0x4048
-  __AUTH_CONST.__cfstring: 0x42000
-  __AUTH_CONST.__objc_const: 0x8f2f8
-  __AUTH_CONST.__objc_intobj: 0x5568
-  __AUTH_CONST.__objc_arrayobj: 0x26e8
+  __DATA_CONST.__objc_superrefs: 0x1a00
+  __DATA_CONST.__objc_arraydata: 0x37c0
+  __AUTH_CONST.__auth_got: 0x2960
+  __AUTH_CONST.__const: 0x41e0
+  __AUTH_CONST.__cfstring: 0x43a80
+  __AUTH_CONST.__objc_const: 0x92a50
+  __AUTH_CONST.__objc_intobj: 0x5aa8
+  __AUTH_CONST.__objc_arrayobj: 0x2838
   __AUTH_CONST.__objc_floatobj: 0x250
   __AUTH_CONST.__objc_dictobj: 0x1770
-  __AUTH_CONST.__objc_doubleobj: 0xa70
-  __AUTH.__objc_data: 0x2da0
-  __DATA.__objc_ivar: 0xa198
-  __DATA.__data: 0x5228
+  __AUTH_CONST.__objc_doubleobj: 0xa90
+  __AUTH.__objc_data: 0x31b0
+  __DATA.__objc_ivar: 0xa65c
+  __DATA.__data: 0x5460
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0xa60
-  __DATA.__bss: 0x20c0
+  __DATA.__common: 0xb20
+  __DATA.__bss: 0x2650
   __DATA_DIRTY.__objc_data: 0xe240
-  __DATA_DIRTY.__data: 0x1060
+  __DATA_DIRTY.__data: 0x1088
   __DATA_DIRTY.__common: 0x780
   __DATA_DIRTY.__bss: 0xc60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 19C2219C-0B9D-31D6-8ABE-6F65EFED4067
-  Functions: 30103
-  Symbols:   98730
-  CStrings:  49736
+  UUID: 0879F558-F057-3BA7-9C18-4441BD86E30C
+  Functions: 30899
+  Symbols:   101362
+  CStrings:  51110
 
Symbols:
+ +[BWMultiCamClientCompositingNode initialize]
+ +[BWSmartCropNode initialize]
+ +[BWSmartCropWarpingNode initialize]
+ +[BWSmartFramingPerceptionSinkNode initialize]
+ +[BWSmartFramingSceneMonitor initialize]
+ +[EGStillImageLearnedFusionNRFNode initialize]
+ +[EGStillImageLearnedFusionRoutingNode initialize]
+ +[FigExternalSyncDeviceDiscoverySessionManager initialize]
+ +[FigExternalSyncDeviceDiscoverySessionManager sharedFigExternalSyncDeviceDiscoverySessionManager]
+ +[FigExternalSyncDeviceDiscoverySessionManager sharedFigExternalSyncDeviceDiscoverySessionManager].cold.1
+ +[FigPulseGenerator anyCaptureSourceSupportsMSG]
+ +[FigPulseGenerator initialize]
+ +[FigPulseGenerator isSupported]
+ +[FigPulseGenerator isSupported].cold.1
+ +[FigPulseGenerator kV5XTriggerID]
+ +[FigPulseGenerator sharedFigPulseGenerator]
+ +[FigPulseGenerator sharedFigPulseGenerator].cold.1
+ -[AudioRemixSessionManager setMultiCamClientCompositingEnabled:]
+ -[AudioRemixSubscriber initWithSession:andNodeMetadataOutput:usePIPAIngestSignalingDomain:completionHandler:]
+ -[BWAudioConverterNode isMultiCamClientCompositingEnabled]
+ -[BWAudioConverterNode setMultiCamClientCompositingEnabled:]
+ -[BWAudioRemixAnalysisMetadataNode multiCamClientCompositingEnabled]
+ -[BWAudioRemixAnalysisMetadataNode setMultiCamClientCompositingEnabled:]
+ -[BWAudioSourceNode updateStereoAudioCapturePairedCameraBaseFieldOfView:zoomFactor:]
+ -[BWDeferredCaptureControllerInput _shouldDropSampleBufferIfNecessary:]
+ -[BWDeferredCaptureControllerInput _stashSampleBufferIfNecessary:]
+ -[BWDeferredCaptureControllerInput setLearnedFusionProxyGenerationUsedEVMinus:]
+ -[BWDeferredPipelineParameters cameraSensorOrientationCompensationDegreesCW]
+ -[BWDeferredPipelineParameters setCameraSensorOrientationCompensationDegreesCW:]
+ -[BWDeferredProcessingContainer hasBufferWithCaptureFrameFlags:portType:]
+ -[BWDepthConverterNode _scaleDepthValues:depthMetadata:sbuf:]
+ -[BWFigCaptureSession previewStitcherSmartFramingFieldOfViewTransitionAppliedZoomFactor:zoomFactor:]
+ -[BWFigVideoCaptureDevice _handleSmartFramingSuggestedFieldOfViewChangeIfNeeded:]
+ -[BWFigVideoCaptureDevice _smartFramingFieldOfViewRectsDictFromFieldsOfView:]
+ -[BWFigVideoCaptureDevice _updateSmartFramingFieldOfViewWithAspectRatio:zoomFactor:]
+ -[BWFigVideoCaptureDevice liveReconfigureForOutputAspectRatioCompleted:]
+ -[BWFigVideoCaptureDevice liveReconfigureForOutputAspectRatioFirstBufferReceived:forConfigurationID:]
+ -[BWFigVideoCaptureDevice liveReconfigureForOutputAspectRatioStarted:forConfigurationID:]
+ -[BWFigVideoCaptureDevice msgClock]
+ -[BWFigVideoCaptureDevice portTypesWithDigitalFlashZeroShutterLagEnabled]
+ -[BWFigVideoCaptureDevice pulseGenerator:updateSynchronizationClock:withError:]
+ -[BWFigVideoCaptureDevice pulseGenerator:updatedTriggerID:withLockState:]
+ -[BWFigVideoCaptureDevice pulseGenerator:updatedTriggerID:withOutOfBoundsError:]
+ -[BWFigVideoCaptureDevice pulseGenerator:updatedTriggerID:withSessionStoppedExitStatus:]
+ -[BWFigVideoCaptureDevice pulseGenerator:updatedTriggerID:withTriggerIsPresent:]
+ -[BWFigVideoCaptureDevice resetSmartFramingSceneMonitor]
+ -[BWFigVideoCaptureDevice setActiveVideoMinFrameDuration:activeVideoMaxFrameDuration:]
+ -[BWFigVideoCaptureDevice setMsgClock:]
+ -[BWFigVideoCaptureDevice setPortTypesWithDigitalFlashZeroShutterLagEnabled:]
+ -[BWFigVideoCaptureDevice setSmartCropCandidateFramingRects:]
+ -[BWFigVideoCaptureDevice setSmartCropSupported:]
+ -[BWFigVideoCaptureDevice setSmartFramingConfiguredFieldOfView:]
+ -[BWFigVideoCaptureDevice setSmartFramingEnabled:]
+ -[BWFigVideoCaptureDevice setSmartFramingEnabledFieldsOfView:]
+ -[BWFigVideoCaptureDevice setSmartFramingIsMonitoringScene:]
+ -[BWFigVideoCaptureDevice setSmartFramingRequiresSceneMonitoring:]
+ -[BWFigVideoCaptureDevice smartCropCandidateFramingRects]
+ -[BWFigVideoCaptureDevice smartCropSupported]
+ -[BWFigVideoCaptureDevice smartFramingConfiguredFieldOfView]
+ -[BWFigVideoCaptureDevice smartFramingEnabled]
+ -[BWFigVideoCaptureDevice smartFramingIsMonitoringScene]
+ -[BWFigVideoCaptureDevice smartFramingRequiresSceneMonitoring]
+ -[BWFigVideoCaptureDevice smartFramingSuggestedFieldOfView]
+ -[BWFigVideoCaptureDevice smartFramingZoomFactorsByFieldOfView]
+ -[BWFigVideoCaptureDevice updateSmartFramingCamGazeProbabilities:]
+ -[BWFigVideoCaptureDevice zoomCommandHandler:didApplyZoomFactor:zoomFactorWithoutFudge:targetZoomFactor:rampComplete:rampCommandID:].cold.1
+ -[BWFigVideoCaptureStream _setFrameRateRational:]
+ -[BWFigVideoCaptureStream activeVideoExternalSyncFrameRate]
+ -[BWFigVideoCaptureStream activeVideoLockedFrameRate]
+ -[BWFigVideoCaptureStream baseZoomFactorOverridesByAspectRatio]
+ -[BWFigVideoCaptureStream digitalFlashZeroShutterLagEnabled]
+ -[BWFigVideoCaptureStream fudgedBaseZoomFactorForAspectRatio:]
+ -[BWFigVideoCaptureStream setActiveVideoLockedFrameRate:activeVideoExternalSyncFrameRate:]
+ -[BWFigVideoCaptureStream setActiveVideoMinFrameDuration:activeVideoMaxFrameDuration:]
+ -[BWFigVideoCaptureStream setBaseZoomFactorOverridesByAspectRatio:]
+ -[BWFigVideoCaptureStream setDigitalFlashZeroShutterLagEnabled:]
+ -[BWFigVideoCaptureStream setMaximumFrameRate:].cold.1
+ -[BWInferenceEngineController _replaceAttachedSampleBuffer:attachedMediaKey:primarySampleBuffer:aspectRatio:]
+ -[BWIrisStagingNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:smartFramingEnabled:irisRequestDelegate:inferenceScheduler:]
+ -[BWLearnedNRProcessorController _landscapeCropInputFormat]
+ -[BWLearnedNRProcessorController _portraitCropInputFormat]
+ -[BWLearnedNRProcessorController _squareCropInputFormat]
+ -[BWLearnedNRProcessorControllerConfiguration landscapeCropOutputFormat]
+ -[BWLearnedNRProcessorControllerConfiguration portraitCropOutputFormat]
+ -[BWLearnedNRProcessorControllerConfiguration setLandscapeCropOutputFormat:]
+ -[BWLearnedNRProcessorControllerConfiguration setPortraitCropOutputFormat:]
+ -[BWLearnedNRProcessorControllerConfiguration setSquareCropOutputFormat:]
+ -[BWLearnedNRProcessorControllerConfiguration squareCropOutputFormat]
+ -[BWMotionAttachmentsNode initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:inputFormatIsProResRaw:errorOut:]
+ -[BWMotionAttachmentsNode initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:inputFormatIsProResRaw:errorOut:].cold.1
+ -[BWMovieLevelMetadataForProResRaw dealloc]
+ -[BWMovieLevelMetadataForProResRaw description]
+ -[BWMovieLevelMetadataForProResRaw init]
+ -[BWMovieLevelMetadataForProResRaw proResRawAugmentedMovieLevelMetadataWithMovieLevelMetadata:]
+ -[BWMovieLevelMetadataForProResRaw releaseRetainedProperties]
+ -[BWMovieLevelMetadataForProResRaw reset]
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:]
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.1
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.10
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.11
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.12
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.13
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.14
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.2
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.3
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.4
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.5
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.6
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.7
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.8
+ -[BWMovieLevelMetadataForProResRaw updateMetadataFromSampleBuffer:withCameraInfo:].cold.9
+ -[BWMultiCamClientCompositingNode _attemptMovieFileBufferPairing]
+ -[BWMultiCamClientCompositingNode _compositionPictureInPictureRectFromClientCompositingMetadata:]
+ -[BWMultiCamClientCompositingNode _compressionPictureInPictureRegionFromRect:]
+ -[BWMultiCamClientCompositingNode _copyCompositionPictureInPictureRectMetadataSampleBuffer:pts:]
+ -[BWMultiCamClientCompositingNode _handleMovieFileSampleBuffer:forInput:]
+ -[BWMultiCamClientCompositingNode _handleStillImageSampleBuffer:forInput:]
+ -[BWMultiCamClientCompositingNode _invokeClientCompositingCallbackForSettingsID:primarySampleBuffer:secondarySampleBuffer:outputSampleBufferOut:compositingMetadataOut:]
+ -[BWMultiCamClientCompositingNode _newSampleBufferWithOriginalPresentationTimesStamp:]
+ -[BWMultiCamClientCompositingNode _normalizedCompositionPictureInPictureRect:]
+ -[BWMultiCamClientCompositingNode _updateOutputSampleBufferDetectedFaces:withSecondarySampleBufferDetectedFaces:compositionPictureInPictureRect:]
+ -[BWMultiCamClientCompositingNode compositionPictureInPictureRectMetadataOutput]
+ -[BWMultiCamClientCompositingNode configurationWithID:updatedFormat:didBecomeLiveForInput:]
+ -[BWMultiCamClientCompositingNode dealloc]
+ -[BWMultiCamClientCompositingNode didReachEndOfDataForInput:]
+ -[BWMultiCamClientCompositingNode didSelectFormat:forInput:forAttachedMediaKey:]
+ -[BWMultiCamClientCompositingNode handleDroppedSample:forInput:]
+ -[BWMultiCamClientCompositingNode handleNodeError:forInput:]
+ -[BWMultiCamClientCompositingNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]
+ -[BWMultiCamClientCompositingNode handleStillImageReferenceFrameBracketedCaptureSequenceNumber:forInput:]
+ -[BWMultiCamClientCompositingNode initWithIndexOfInputProvidingOutputSampleBuffer:compositingStrategy:gainMapSupported:clientCompositingCallback:]
+ -[BWMultiCamClientCompositingNode nodeSubType]
+ -[BWMultiCamClientCompositingNode nodeType]
+ -[BWMultiCamClientCompositingNode renderSampleBuffer:forInput:]
+ -[BWMultiStreamCameraSourceNode _getImageCircleFromSampleBuffer:outputIndex:gdcEnabled:imageCircleCenterOut:imageCircleRadiusOut:]
+ -[BWMultiStreamCameraSourceNode _shouldEnableStreamPreviewOutputForNodeOutput:]
+ -[BWMultiStreamCameraSourceNode _updateOutputIDMappingsForStreamingOutputs].cold.4
+ -[BWMultiStreamCameraSourceNode setAspectRatio:]
+ -[BWMultiStreamCameraSourceNodeConfiguration adaptiveSensorCropForDynamicAspectRatioEnabled]
+ -[BWMultiStreamCameraSourceNodeConfiguration baseZoomFactorOverridesByAspectRatio]
+ -[BWMultiStreamCameraSourceNodeConfiguration dynamicAspectRatioEnabled]
+ -[BWMultiStreamCameraSourceNodeConfiguration externalSyncFrameRate]
+ -[BWMultiStreamCameraSourceNodeConfiguration lockedFrameRate]
+ -[BWMultiStreamCameraSourceNodeConfiguration proResRawCaptureEnabled]
+ -[BWMultiStreamCameraSourceNodeConfiguration sensorOutputLargerThanImageCircle]
+ -[BWMultiStreamCameraSourceNodeConfiguration setAdaptiveSensorCropForDynamicAspectRatioEnabled:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setBaseZoomFactorOverridesByAspectRatio:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setDynamicAspectRatioEnabled:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setExternalSyncFrameRate:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setLockedFrameRate:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setProResRawCaptureEnabled:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setSensorOutputLargerThanImageCircle:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setVisOverscanByAspectRatio:]
+ -[BWMultiStreamCameraSourceNodeConfiguration visOverscanByAspectRatio]
+ -[BWNRFProcessorController _processLearnedFusion]
+ -[BWNRFProcessorController _processLearnedHRNR]
+ -[BWNRFProcessorControllerConfiguration learnedFusionEnabled]
+ -[BWNRFProcessorControllerConfiguration learnedFusionInputFormat]
+ -[BWNRFProcessorControllerConfiguration setLearnedFusionEnabled:]
+ -[BWNRFProcessorControllerConfiguration setLearnedFusionInputFormat:]
+ -[BWOverCaptureSmartStyleApplyNode _loadAndConfigureSmartStyleBundle:]
+ -[BWOverCaptureSmartStyleApplyNode _loadAndConfigureSmartStyleBundle:].cold.1
+ -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:squareAspectRatioConfigEnabled:]
+ -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:squareAspectRatioConfigEnabled:].cold.1
+ -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:squareAspectRatioConfigEnabled:].cold.2
+ -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:squareAspectRatioConfigEnabled:].cold.3
+ -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:squareAspectRatioConfigEnabled:].cold.4
+ -[BWPhotonicEngineNode learnedFusionSupportedForPortType:]
+ -[BWPhotonicEngineNode setActiveAspectRatio:]
+ -[BWPhotonicEngineNodeConfiguration portTypesWithLearnedFusionEnabled]
+ -[BWPhotonicEngineNodeConfiguration setPortTypesWithLearnedFusionEnabled:]
+ -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:]
+ -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:].cold.1
+ -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:].cold.2
+ -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:].cold.3
+ -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:].cold.4
+ -[BWPreviewStitcherNode initWithStitchingDisabledAndZoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:]
+ -[BWPreviewStitcherNode setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:trueVideoTransitionReferenceSampleBuffer:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:fencePortSendRight:]
+ -[BWQuickTimeMovieFileSinkNode frontRearSimultaneousVideoRecording]
+ -[BWQuickTimeMovieFileSinkNode setFrontRearSimultaneousVideoRecording:]
+ -[BWRemoteQueueSinkNode movieLevelMetadata]
+ -[BWSmartCropNode _addMetadataInputsAndOutputsWithMetadataIdentifiers:]
+ -[BWSmartCropNode _addVideoCaptureInputAndOutput]
+ -[BWSmartCropNode _createCalibrationDictionaryFromSampleBuffer:]
+ -[BWSmartCropNode _createCalibrationDictionaryFromSampleBuffer:].cold.1
+ -[BWSmartCropNode _createCalibrationDictionaryFromSampleBuffer:].cold.2
+ -[BWSmartCropNode _createCalibrationDictionaryFromSampleBuffer:].cold.3
+ -[BWSmartCropNode _initRTSCProcessor]
+ -[BWSmartCropNode _initRTSCProcessor].cold.1
+ -[BWSmartCropNode _initRTSCProcessor].cold.2
+ -[BWSmartCropNode _initRTSCProcessor].cold.3
+ -[BWSmartCropNode _initRTSCProcessor].cold.4
+ -[BWSmartCropNode _isSampleBufferFromPrimaryStream:metadataDict:]
+ -[BWSmartCropNode _popHomography]
+ -[BWSmartCropNode _pushHomography:pts:]
+ -[BWSmartCropNode _supportedInputPixelFormats]
+ -[BWSmartCropNode _supportedOutputPixelFormats]
+ -[BWSmartCropNode _updateDetectedObjectsInfo:]
+ -[BWSmartCropNode _updateOutputRequirements]
+ -[BWSmartCropNode cinematicFramingControlsSuspended]
+ -[BWSmartCropNode cinematicFramingControls]
+ -[BWSmartCropNode configurationWithID:updatedFormat:didBecomeLiveForInput:]
+ -[BWSmartCropNode dealloc]
+ -[BWSmartCropNode detectionMetadataInput]
+ -[BWSmartCropNode detectionMetadataOutput]
+ -[BWSmartCropNode didChangeCenterStageFramingMode:]
+ -[BWSmartCropNode didChangeCenterStageMetadataDeliveryEnabled:]
+ -[BWSmartCropNode didChangeCenterStageRectOfInterest:]
+ -[BWSmartCropNode didReachEndOfDataForConfigurationID:input:]
+ -[BWSmartCropNode didSelectFormat:forInput:]
+ -[BWSmartCropNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxLossyCompressionLevel:cameraExtrinsicMatrix:processingMode:stillCaptureEnabled:objectMetadataIdentifiers:captureDevice:]
+ -[BWSmartCropNode isRegionOfInterestForCameraControlsFeedbackEnabled]
+ -[BWSmartCropNode nodeSubType]
+ -[BWSmartCropNode nodeType]
+ -[BWSmartCropNode outputDimensions]
+ -[BWSmartCropNode prepareForCurrentConfigurationToBecomeLive]
+ -[BWSmartCropNode regionOfInterestForCameraControlsChangedHandler]
+ -[BWSmartCropNode regionOfInterestForCameraControls]
+ -[BWSmartCropNode renderMetadataSampleBuffer:forInput:]
+ -[BWSmartCropNode renderSampleBuffer:forInput:]
+ -[BWSmartCropNode renderSampleBuffer:forInput:].cold.1
+ -[BWSmartCropNode renderVideoSampleBuffer:forInput:]
+ -[BWSmartCropNode restrictCenterStageFieldOfViewToWide:]
+ -[BWSmartCropNode rtscProcessor]
+ -[BWSmartCropNode setCinematicFramingControls:]
+ -[BWSmartCropNode setCinematicFramingControlsSuspended:]
+ -[BWSmartCropNode setOutputDimensions:]
+ -[BWSmartCropNode setRegionOfInterestForCameraControlsChangedHandler:]
+ -[BWSmartCropNode setRegionOfInterestForCameraControlsFeedbackEnabled:]
+ -[BWSmartCropNode setRtscProcessor:]
+ -[BWSmartCropNode smartCropHomographyDataForPTS:]
+ -[BWSmartCropWarpingNode _initRTSCProcessorWithOutputDimensions:]
+ -[BWSmartCropWarpingNode _updateDetectedObjectsInfo:]
+ -[BWSmartCropWarpingNode _updateOutputRequirements]
+ -[BWSmartCropWarpingNode activeAspectRatio]
+ -[BWSmartCropWarpingNode dealloc]
+ -[BWSmartCropWarpingNode didSelectFormat:forInput:forAttachedMediaKey:]
+ -[BWSmartCropWarpingNode initWithHomographyProvider:aspectRatio:formatDimensions:maxLossyCompressionLevel:]
+ -[BWSmartCropWarpingNode prepareForCurrentConfigurationToBecomeLive]
+ -[BWSmartCropWarpingNode renderSampleBuffer:forInput:]
+ -[BWSmartCropWarpingNode renderSampleBuffer:forInput:].cold.1
+ -[BWSmartCropWarpingNode setActiveAspectRatio:]
+ -[BWSmartFramingPerceptionSinkNode _waitForInferenceToComplete]
+ -[BWSmartFramingPerceptionSinkNode dealloc]
+ -[BWSmartFramingPerceptionSinkNode didReachEndOfDataForInput:]
+ -[BWSmartFramingPerceptionSinkNode hasNonLiveConfigurationChanges]
+ -[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:]
+ -[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:].cold.1
+ -[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:].cold.2
+ -[BWSmartFramingPerceptionSinkNode inputFormatForAttachedMediaKey:]
+ -[BWSmartFramingPerceptionSinkNode inputInferenceVideoFormatForAttachedMediaKey:]
+ -[BWSmartFramingPerceptionSinkNode inputVideoFormatForAttachedMediaKey:]
+ -[BWSmartFramingPerceptionSinkNode intermediateResourceTrackingAllowedForAttachedMediaKey:]
+ -[BWSmartFramingPerceptionSinkNode nodeSubType]
+ -[BWSmartFramingPerceptionSinkNode nodeType]
+ -[BWSmartFramingPerceptionSinkNode outputFormatForAttachedMediaKey:]
+ -[BWSmartFramingPerceptionSinkNode outputVideoFormatForAttachedMediaKey:]
+ -[BWSmartFramingPerceptionSinkNode prepareForCurrentConfigurationToBecomeLive]
+ -[BWSmartFramingPerceptionSinkNode renderSampleBuffer:forInput:]
+ -[BWSmartFramingSceneMonitor _getOptimalFieldOfViewKeyFromCumulativeFieldOfViewWeights:significantFaceOrBodyCount:]
+ -[BWSmartFramingSceneMonitor _reset]
+ -[BWSmartFramingSceneMonitor _resolveSuggestedFieldOfViewWithSampleBuffer:usingFieldsOfView:suggestedFieldOfViewOut:suggestedFieldOfViewRectOut:]
+ -[BWSmartFramingSceneMonitor _updateFieldOfViewWeightsUsingFaceRect:cumulativeFieldOfViewWeights:fieldsOfView:]
+ -[BWSmartFramingSceneMonitor dealloc]
+ -[BWSmartFramingSceneMonitor initWithDynamicFieldOfViewRectsEnabled:]
+ -[BWSmartFramingSceneMonitor reset]
+ -[BWSmartFramingSceneMonitor resolveSuggestedFieldOfViewRectWithSampleBuffer:fromFieldOfViewRects:suggestedFieldOfViewRectOut:]
+ -[BWSmartFramingSceneMonitor resolveSuggestedFieldOfViewRectWithSampleBuffer:fromFieldOfViewRects:suggestedFieldOfViewRectOut:].cold.1
+ -[BWSmartFramingSceneMonitor resolveSuggestedFieldOfViewRectWithSampleBuffer:fromFieldOfViewRects:suggestedFieldOfViewRectOut:].cold.2
+ -[BWSmartFramingSceneMonitor resolveSuggestedFieldOfViewWithSampleBuffer:suggestedFieldOfViewOut:]
+ -[BWSmartFramingSceneMonitor resolveSuggestedFieldOfViewWithSampleBuffer:suggestedFieldOfViewOut:].cold.1
+ -[BWSmartFramingSceneMonitor setSmartFramingCamGazeProbabilitiesByFaceGroupID:]
+ -[BWSmartFramingSceneMonitor setSmartFramingFieldOfViewRects:]
+ -[BWSmartFramingSceneMonitor setSmartFramingFieldOfViewRects:].cold.1
+ -[BWSmartFramingSceneMonitor setSmartFramingFieldOfViewRects:].cold.2
+ -[BWSmartStyleApplyNode _loadAndConfigureSmartStyleBundle:]
+ -[BWSmartStyleApplyNode _loadAndConfigureSmartStyleBundle:].cold.1
+ -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:squareAspectRatioConfigEnabled:]
+ -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:squareAspectRatioConfigEnabled:].cold.1
+ -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:squareAspectRatioConfigEnabled:].cold.2
+ -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:squareAspectRatioConfigEnabled:].cold.3
+ -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:squareAspectRatioConfigEnabled:].cold.4
+ -[BWSmartStyleLearningNode _initVMRefinerInference:]
+ -[BWSmartStyleLearningNode _initVMRefinerInference:].cold.1
+ -[BWSmartStyleLearningNode _initVMRefinerInference:].cold.2
+ -[BWSmartStyleLearningNode _initVMRefinerInference:].cold.3
+ -[BWSmartStyleLearningNode _initVMRefinerInference:].cold.4
+ -[BWSmartStyleLearningNode _initVMRefinerInference:].cold.5
+ -[BWSmartStyleLearningNode _loadAndConfigureSmartStyleBundle:]
+ -[BWSmartStyleLearningNode _loadAndConfigureSmartStyleBundle:].cold.1
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:]
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.1
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.10
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.11
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.2
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.3
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.4
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.5
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.6
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.7
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.8
+ -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:].cold.9
+ -[BWSoftISPProcessorControllerConfiguration learnedFusionEnabled]
+ -[BWSoftISPProcessorControllerConfiguration setLearnedFusionEnabled:]
+ -[BWStillImageCaptureSettings updateForLearnedFusionMissingEVMinus:missingHDRErrorRecoveryEVZero:]
+ -[BWStillImageCaptureStreamSettings updateForLearnedFusionMissingEVMinus:missingHDRErrorRecoveryEVZero:]
+ -[BWStillImageNodeConfiguration cameraSensorOrientationCompensationDegreesCW]
+ -[BWStillImageNodeConfiguration setCameraSensorOrientationCompensationDegreesCW:]
+ -[BWStreamingCVAFilterRenderer initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:secondaryStreamingPersonSegmentationEnabled:cropDepthToPrimaryCaptureAspectRatio:disableDepthAndSegmentationRotationInLandscape:]
+ -[BWStreamingFilterNode initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:smartStyleRenderingEnabled:portraitPreviewForegroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:sourceStillImageOutputPortTypes:squareAspectRatioConfigEnabled:cropDepthToPrimaryCaptureAspectRatio:disableDepthAndSegmentationRotationInLandscape:]
+ -[BWStreamingRaytracingSDOFRenderer _loadAndConfigureSmartStyleBundle:]
+ -[BWStreamingRaytracingSDOFRenderer initWithCaptureDevice:commandQueue:smartStyleRenderingEnabled:squareAspectRatioConfigEnabled:]
+ -[BWUBNode learnedFusionSupportedForPortType:]
+ -[BWVISNode initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:videoGreenGhostOfflineMetadataEnabled:videoGreenGhostOfflineLightSourceMaskEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:systemIsUnderCriticalThermalPressure:faceAwareVideoStabilizationEnabled:]
+ -[BWVISProcessorControllerConfiguration faceStabilizationEnabled]
+ -[BWVISProcessorControllerConfiguration faceStabilizationSigmaMultiplierForBiasTracking]
+ -[BWVISProcessorControllerConfiguration faceStabilizationSigmaMultiplierForFaceFiltering]
+ -[BWVISProcessorControllerConfiguration setFaceStabilizationEnabled:]
+ -[BWVISProcessorControllerConfiguration setFaceStabilizationSigmaMultiplierForBiasTracking:]
+ -[BWVISProcessorControllerConfiguration setFaceStabilizationSigmaMultiplierForFaceFiltering:]
+ -[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:].cold.19
+ -[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:].cold.20
+ -[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:].cold.21
+ -[BWVideoDepthInferenceConfiguration _monocularNetworkSupportsResolutionWithWidth:height:]
+ -[BWVideoDepthInferenceConfiguration colorFeaturesDimensions]
+ -[BWVideoDepthInferenceConfiguration colorFeaturesPixelFormat]
+ -[BWVideoDepthInferenceConfiguration disparityMultiplierFormat]
+ -[BWVideoDepthInferenceConfiguration getMonocularDepthScaleFactor:inputImageIsRotated:]
+ -[BWVideoDepthInferenceConfiguration loadMonocularVideoPipeline]
+ -[BWVideoDepthInferenceConfiguration monocularVideoInferenceDescriptor]
+ -[BWVideoDepthInferenceConfiguration sensorIDString]
+ -[BWVideoDepthNode renderSampleBuffer:forInput:].cold.1
+ -[BWVideoDepthNode renderSampleBuffer:forInput:].cold.2
+ -[EGStillImageLearnedFusionNRFNode _handleAnyErrorRecoveryLogicWithErr:]
+ -[EGStillImageLearnedFusionNRFNode _releaseErrorRecoveryResources]
+ -[EGStillImageLearnedFusionNRFNode attemptErrorRecoveryOutput]
+ -[EGStillImageLearnedFusionNRFNode dealloc]
+ -[EGStillImageLearnedFusionNRFNode fusionModeOutput]
+ -[EGStillImageLearnedFusionNRFNode hdrErrorRecoveryEVZeroInput]
+ -[EGStillImageLearnedFusionNRFNode inferenceInputImageOutput]
+ -[EGStillImageLearnedFusionNRFNode initWithName:stillImageSettings:nodeConfiguration:provideInferenceInputImageForProcessing:addSyncErrorRecoveryPorts:portType:delegate:]
+ -[EGStillImageLearnedFusionNRFNode primarySbufInputs]
+ -[EGStillImageLearnedFusionNRFNode processSmartStyleRenderingInput]
+ -[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingBuffer:metadata:type:captureFrameFlags:processorInput:err:]
+ -[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingInput:err:]
+ -[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingInput:err:].cold.1
+ -[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]
+ -[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:].cold.1
+ -[EGStillImageLearnedFusionNRFNode processorController:didSelectFusionMode:processorInput:]
+ -[EGStillImageLearnedFusionNRFNode processorController:willAddSampleBuffer:processorInput:]
+ -[EGStillImageLearnedFusionNRFNode processorInput]
+ -[EGStillImageLearnedFusionNRFNode queueManagedReceiveData:fromInput:]
+ -[EGStillImageLearnedFusionNRFNode queueManagedReceiveData:fromInput:].cold.1
+ -[EGStillImageLearnedFusionNRFNode referenceFrameInput]
+ -[EGStillImageLearnedFusionNRFNode sbufOutput]
+ -[EGStillImageLearnedFusionNRFNode setProcessSmartStyleRenderingInput:]
+ -[EGStillImageLearnedFusionRoutingNode dealloc]
+ -[EGStillImageLearnedFusionRoutingNode evMinusOutput]
+ -[EGStillImageLearnedFusionRoutingNode evZeroOutput]
+ -[EGStillImageLearnedFusionRoutingNode initWithName:numSampleBufferInputs:]
+ -[EGStillImageLearnedFusionRoutingNode longOutput]
+ -[EGStillImageLearnedFusionRoutingNode receiveData:fromInput:]
+ -[EGStillImageLearnedFusionRoutingNode sampleBufferInputs]
+ -[EGStillImageLearnedFusionRoutingNode secondEvZeroOutput]
+ -[FigCaptureCameraParameters monocularStreamingDepthType]
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:inferenceScheduler:].cold.35
+ -[FigCaptureCameraSourcePipeline liveReconfigureForOutputDimensions:aspectRatio:]
+ -[FigCaptureCameraSourcePipeline lowLatencyStabilizationEnabled]
+ -[FigCaptureCameraSourcePipeline rtscProcessorsBySourceDeviceType]
+ -[FigCaptureCameraSourcePipeline smartCropHomographyProvider]
+ -[FigCaptureCameraSourcePipelineConfiguration lowLatencyStabilizationEnabledInSourcePipeline]
+ -[FigCaptureCameraSourcePipelineConfiguration setLowLatencyStabilizationEnabledInSourcePipeline:]
+ -[FigCaptureCameraSourcePipelineConfiguration setMultiCamClientCompositingPrimaryCameraVideoStabilizationStrength:]
+ -[FigCaptureCameraSourcePipelineConfiguration setSmartFramingEnabled:]
+ -[FigCaptureIrisSinkConfiguration cameraSensorOrientationCompensationEnabled]
+ -[FigCaptureIrisSinkConfiguration multiCamClientCompositingEnabled]
+ -[FigCaptureIrisSinkConfiguration multiCamClientCompositingPrimaryConnectionID]
+ -[FigCaptureIrisSinkConfiguration setCameraSensorOrientationCompensationEnabled:]
+ -[FigCaptureIrisSinkConfiguration setMultiCamClientCompositingEnabled:]
+ -[FigCaptureIrisSinkConfiguration setMultiCamClientCompositingPrimaryConnectionID:]
+ -[FigCaptureMicSourcePipelineConfiguration micConfiguration]
+ -[FigCaptureMovieFileSinkConfiguration multiCamClientCompositingEnabled]
+ -[FigCaptureMovieFileSinkConfiguration multiCamClientCompositingPrimaryConnectionID]
+ -[FigCaptureMovieFileSinkConfiguration setMultiCamClientCompositingEnabled:]
+ -[FigCaptureMovieFileSinkConfiguration setMultiCamClientCompositingPrimaryConnectionID:]
+ -[FigCaptureMovieFileSinkPipeline initWithConfiguration:videoSourceCaptureOutputsByConnectionID:audioSourceCaptureOutput:audioSourceCinematicAudioCaptureOutput:smartCameraInferenceOutput:detectedObjectBoxedMetadataOutputs:objectDetectionSourceOutput:metadataSourcePipelineOutputs:graph:name:inferenceScheduler:captureDevicesByConnectionID:audioSourceDelegate:fileCoordinatorStatusDelegate:recordingStatusDelegate:irisRequestDelegate:multiCamClientCompositingCallback:masterClock:delayedCompressorCleanupEnabled:]
+ -[FigCaptureMovieFileSinkPipeline liveReconfigureForOutputDimensions:]
+ -[FigCaptureMovieFileSinkPipelineConfiguration setLowLatencyStabilizationEnabled:]
+ -[FigCaptureMovieFileSinkTailPipeline _buildMovieFileSinkTailPipeline:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:multiCamClientCompositingCallback:workgroup:]
+ -[FigCaptureMovieFileSinkTailPipeline initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:multiCamClientCompositingCallback:workgroup:]
+ -[FigCaptureMovieFileSinkTailPipeline initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:multiCamClientCompositingCallback:workgroup:].cold.1
+ -[FigCaptureMovieFileSinkTailPipeline smartCropNode]
+ -[FigCapturePhotonicEngineSinkPipeline _buildScaleAndEncodeSubPipelineWithPipelineStage:graph:nodeConfiguration:stillImageSinkPipelineWithConfiguration:sensorConfigurationsByPortType:supportsScaling:deferredPearlDepthProcessingEnabled:provideMeteorHeadroom:provideFlexGTC:providePostEncodeInferences:semanticDevelopmentVersion:constituentPhotoDeliveryEnabled:demosaicedRawEnabled:nonPropagatedMainImageDownscalingFactorByAttachedMediaKey:propagatedMainImageDownscalingFactorByAttachedMediaKey:scalingMainImageDownscalingFactorByAttachedMediaKey:inferenceScheduler:subPipelineInputOut:subPipelineOutputOut:cameraSupportsFlash:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:photoEncoderControllerOut:]
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:]
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.1
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.10
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.100
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.101
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.102
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.103
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.104
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.105
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.106
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.107
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.108
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.109
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.11
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.110
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.111
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.112
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.113
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.114
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.115
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.116
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.117
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.118
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.119
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.12
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.120
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.121
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.122
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.13
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.14
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.15
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.16
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.17
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.18
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.19
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.2
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.20
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.21
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.22
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.23
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.24
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.25
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.26
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.27
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.28
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.29
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.3
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.30
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.31
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.32
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.33
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.34
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.35
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.36
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.37
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.38
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.39
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.4
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.40
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.41
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.42
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.43
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.44
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.45
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.46
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.47
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.48
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.49
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.5
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.50
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.51
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.52
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.53
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.54
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.55
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.56
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.57
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.58
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.59
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.6
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.60
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.61
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.62
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.63
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.64
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.65
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.66
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.67
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.68
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.69
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.7
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.70
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.71
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.72
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.73
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.74
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.75
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.76
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.77
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.78
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.79
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.8
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.80
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.81
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.82
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.83
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.84
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.85
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.86
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.87
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.88
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.89
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.9
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.90
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.91
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.92
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.93
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.94
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.95
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.96
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.97
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.98
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:].cold.99
+ -[FigCapturePhotonicEngineSinkPipeline connectToSecondaryMultiCameraClientCompositingPipeline:]
+ -[FigCapturePhotonicEngineSinkPipeline initWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:isPrimaryStillImagePipeline:graph:name:]
+ -[FigCapturePhotonicEngineSinkPipeline initWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:isPrimaryStillImagePipeline:graph:name:].cold.1
+ -[FigCapturePhotonicEngineSinkPipeline liveReconfigureForAspectRatio:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration cameraSensorOrientationCompensationDegreesCW]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration learnedHRNRSupported]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration portTypesWithDigitalFlashZeroShutterLagEnabled]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration portTypesWithLearnedFusionEnabled]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setCameraSensorOrientationCompensationDegreesCW:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setLearnedHRNRSupported:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setPortTypesWithDigitalFlashZeroShutterLagEnabled:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setPortTypesWithLearnedFusionEnabled:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setSmartCropWarpingOutputDimensions:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration setSmartCropWarpingRequired:]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration smartCropWarpingOutputDimensions]
+ -[FigCapturePhotonicEngineSinkPipelineConfiguration smartCropWarpingRequired]
+ -[FigCapturePreviewSinkPipeline liveReconfigureForOutputDimensions:]
+ -[FigCapturePreviewSinkPipeline setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:fencePortSendRight:uniqueID:]
+ -[FigCapturePreviewSinkPipelineConfiguration setLowLatencyStabilizationEnabled:]
+ -[FigCapturePreviewSinkPipelineConfiguration setSingleCameraOverCaptureEnabled:]
+ -[FigCaptureSessionParsedCameraSourceConfiguration multiCamClientCompositingPrimaryCameraVideoStabilizationStrength]
+ -[FigCaptureSessionParsedCameraSourceConfiguration setMultiCamClientCompositingPrimaryCameraVideoStabilizationStrength:]
+ -[FigCaptureSourceConfiguration externalSyncFrameRate]
+ -[FigCaptureSourceConfiguration isExternalSyncDevicePulse]
+ -[FigCaptureSourceConfiguration isSmartFramingEnabled]
+ -[FigCaptureSourceConfiguration lockedFrameRate]
+ -[FigCaptureSourceConfiguration outputAspectRatioRequestID]
+ -[FigCaptureSourceConfiguration outputAspectRatio]
+ -[FigCaptureSourceConfiguration pulseGeneratorFrameRate]
+ -[FigCaptureSourceConfiguration setExternalSyncFrameRate:]
+ -[FigCaptureSourceConfiguration setLockedFrameRate:]
+ -[FigCaptureSourceConfiguration setOutputAspectRatio:]
+ -[FigCaptureSourceConfiguration setOutputAspectRatioRequestID:]
+ -[FigCaptureSourceConfiguration setSmartFramingEnabled:]
+ -[FigCaptureSourceVideoFormat _fieldOfViewForAspectRatio:horizontal:gdcEnabled:]
+ -[FigCaptureSourceVideoFormat _geometricDistortionCorrectedFieldOfViewCropMultiplier]
+ -[FigCaptureSourceVideoFormat horizontalFieldOfViewForAspectRatio:]
+ -[FigCaptureSourceVideoFormat horizontalGeometricDistortionCorrectedFieldOfViewForAspectRatio:]
+ -[FigCaptureSourceVideoFormat isDigitalFlashZeroShutterLagSupported]
+ -[FigCaptureSourceVideoFormat isDynamicAspectRatioSupported]
+ -[FigCaptureSourceVideoFormat isLearnedFusionSupported]
+ -[FigCaptureSourceVideoFormat isLearnedHRNRSupported]
+ -[FigCaptureSourceVideoFormat isLowLatencyStabilizationSupported]
+ -[FigCaptureSourceVideoFormat isSmartCropSupported]
+ -[FigCaptureSourceVideoFormat isSmartFramingSupported]
+ -[FigCaptureSourceVideoFormat isStillImageOutputDownscaledInHWISP]
+ -[FigCaptureSourceVideoFormat previewDimensionsForAspectRatio:]
+ -[FigCaptureSourceVideoFormat smartCropFormat]
+ -[FigCaptureSourceVideoFormat smartCropOutputDimensions]
+ -[FigCaptureSourceVideoFormat verticalFieldOfViewForAspectRatio:]
+ -[FigCaptureSourceVideoFormat verticalGeometricDistortionCorrectedFieldOfViewForAspectRatio:]
+ -[FigCaptureStillImageSinkConfiguration cameraSensorOrientationCompensationEnabled]
+ -[FigCaptureStillImageSinkConfiguration setCameraSensorOrientationCompensationEnabled:]
+ -[FigCaptureVISPipeline _recreateISPProcessingSessionForVISNode:withCaptureDevice:]
+ -[FigCaptureVISPipeline liveReconfigureForOutputDimensions:]
+ -[FigCaptureVideoDataSinkPipeline liveReconfigureForOutputDimensions:stabilizationCropDimensions:]
+ -[FigCaptureVideoDataSinkPipelineConfiguration setLowLatencyStabilizationEnabled:]
+ -[FigExternalSyncDevice _SSAMDeivceTerminatedService:]
+ -[FigExternalSyncDevice _setSSAMPortEnabled:]
+ -[FigExternalSyncDevice _setSSAMPortEnabled:].cold.1
+ -[FigExternalSyncDevice _setSSAMPortEnabled:].cold.2
+ -[FigExternalSyncDevice _setupSSAMInterestNotification]
+ -[FigExternalSyncDevice _setupSSAMInterestNotification].cold.1
+ -[FigExternalSyncDevice _setupSSAMInterestNotification].cold.2
+ -[FigExternalSyncDevice _setupSSAMInterestNotification].cold.3
+ -[FigExternalSyncDevice _teardownSSAMInterestNotification]
+ -[FigExternalSyncDevice dealloc]
+ -[FigExternalSyncDevice externalSyncDeviceDeviceIdentifer]
+ -[FigExternalSyncDevice forceCleanup]
+ -[FigExternalSyncDevice getDeviceInfoDict]
+ -[FigExternalSyncDevice initWithHpmEntID:ssamEntID:connectionState:vid:pid:]
+ -[FigExternalSyncDevice isConnected]
+ -[FigExternalSyncDevice isSSAMEnabled]
+ -[FigExternalSyncDeviceDiscoverySessionDelegateHandler externalSyncDeviceDiscoverySessionManager:connectedDevicesDidChange:]
+ -[FigExternalSyncDeviceDiscoverySessionDelegateHandler externalSyncDeviceDiscoverySessionManager:connectedDevicesDidChange:].cold.1
+ -[FigExternalSyncDeviceDiscoverySessionDelegateHandler forceCleanup]
+ -[FigExternalSyncDeviceDiscoverySessionDelegateHandler initWithSource:]
+ -[FigExternalSyncDeviceDiscoverySessionManager _addDevice:]
+ -[FigExternalSyncDeviceDiscoverySessionManager _currentDevices]
+ -[FigExternalSyncDeviceDiscoverySessionManager _forceNotifyDelegatesDevicesChanged]
+ -[FigExternalSyncDeviceDiscoverySessionManager _handleDeviceEvent:]
+ -[FigExternalSyncDeviceDiscoverySessionManager _removeDevice:]
+ -[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceDeviceManagmentMonitoring]
+ -[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceObservationNotifications]
+ -[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceObservationNotifications].cold.1
+ -[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceObservationNotifications].cold.2
+ -[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceObservationNotifications].cold.3
+ -[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceObservationNotifications].cold.4
+ -[FigExternalSyncDeviceDiscoverySessionManager _teardownDeviceDeviceManagmentMonitoring]
+ -[FigExternalSyncDeviceDiscoverySessionManager _teardownDeviceObservationNotifications]
+ -[FigExternalSyncDeviceDiscoverySessionManager currentDevices]
+ -[FigExternalSyncDeviceDiscoverySessionManager dealloc]
+ -[FigExternalSyncDeviceDiscoverySessionManager deviceDisconnectedEvent:]
+ -[FigExternalSyncDeviceDiscoverySessionManager init]
+ -[FigExternalSyncDeviceDiscoverySessionManager registerClient:delegate:]
+ -[FigExternalSyncDeviceDiscoverySessionManager unregisterAndCleanupClient:]
+ -[FigPulseGenerator .cxx_destruct]
+ -[FigPulseGenerator _configureFollowSync:assertDur:offset:]
+ -[FigPulseGenerator _configureLeaderSync:frameRate:assertDur:]
+ -[FigPulseGenerator _disciplineMSGTimeSyncClock:]
+ -[FigPulseGenerator _enabled]
+ -[FigPulseGenerator _followSyncConfig:config:]
+ -[FigPulseGenerator _followSyncInit:leader:trigger:]
+ -[FigPulseGenerator _getOrCreateTimeSyncMSGClockIdentifier:tsClockIdentifierOut:]
+ -[FigPulseGenerator _getTimeSyncClock:clockOut:]
+ -[FigPulseGenerator _getTimeSyncClock:clockOut:].cold.1
+ -[FigPulseGenerator _leaderSyncConfig:config:]
+ -[FigPulseGenerator _leaderSyncInit:trigger:]
+ -[FigPulseGenerator _notifyDelegate:withError:]
+ -[FigPulseGenerator _resetMsgSyncs]
+ -[FigPulseGenerator _resetState]
+ -[FigPulseGenerator _startSync:]
+ -[FigPulseGenerator _startSyncs:]
+ -[FigPulseGenerator _syncInterruptDisable:]
+ -[FigPulseGenerator _syncInterruptEnable:]
+ -[FigPulseGenerator _syncReset:]
+ -[FigPulseGenerator applySignalCompensationDelay:]
+ -[FigPulseGenerator dealloc]
+ -[FigPulseGenerator delegate]
+ -[FigPulseGenerator init]
+ -[FigPulseGenerator init].cold.1
+ -[FigPulseGenerator init].cold.2
+ -[FigPulseGenerator isEnabled]
+ -[FigPulseGenerator setDelegate:]
+ -[FigPulseGenerator startWithFrameRate:cmClock:clientAudioClockDeviceUIDOut:externalSync:]
+ -[FigPulseGenerator stopRunning]
+ -[TrackedFace _appendArray:withObject:restrictingLengthTo:]
+ -[TrackedFace _getMotionScoreUsingLargestFaceTrack:]
+ -[TrackedFace _updateGazeStatesUsingGazeProbabilitiesData:gazeConfidenceFilteredOut:gazeScoreFilteredOut:]
+ -[TrackedFace _updateGazeStatesUsingGazeProbabilitiesData:gazeConfidenceFilteredOut:gazeScoreFilteredOut:].cold.1
+ -[TrackedFace dealloc]
+ -[TrackedFace initWithFaceGroupID:signficanceDetectionThreshold:]
+ -[TrackedFace isPersistentlySignificant]
+ -[TrackedFace updateStatesIfNeededUsingFaceRect:faceSize:gazeProbabilitiesData:largestFaceTrack:largestFaceSize:totalDetectedFaceCount:currentPTS:isSignificantOut:]
+ GCC_except_table106
+ GCC_except_table113
+ GCC_except_table131
+ GCC_except_table133
+ GCC_except_table145
+ GCC_except_table162
+ GCC_except_table167
+ GCC_except_table185
+ GCC_except_table195
+ GCC_except_table219
+ GCC_except_table260
+ GCC_except_table278
+ GCC_except_table318
+ GCC_except_table325
+ GCC_except_table327
+ GCC_except_table347
+ GCC_except_table362
+ GCC_except_table363
+ GCC_except_table369
+ GCC_except_table384
+ GCC_except_table424
+ GCC_except_table467
+ GCC_except_table512
+ GCC_except_table513
+ GCC_except_table518
+ GCC_except_table521
+ GCC_except_table523
+ GCC_except_table525
+ GCC_except_table631
+ GCC_except_table89
+ GCC_except_table95
+ GCC_except_table98
+ _.compoundliteral.22
+ _.compoundliteral.33
+ _.compoundliteral.36
+ _.compoundliteral.40
+ _.compoundliteral.41
+ _.compoundliteral.46
+ _.compoundliteral.47
+ _.compoundliteral.56
+ _.compoundliteral.57
+ _.compoundliteral.60
+ _.compoundliteral.61
+ _.compoundliteral.62
+ _.compoundliteral.63
+ _.compoundliteral.87
+ _.compoundliteral.88
+ _.compoundliteral.89
+ _.compoundliteral.90
+ _.compoundliteral.91
+ _.compoundliteral.92
+ _.compoundliteral.93
+ _.compoundliteral.94
+ _BWCreateProResRawGDCMetadata
+ _BWDeviceModelHasCharleston
+ _BWDeviceModelIsD23Proto1
+ _BWDeviceModelIsD23Proto1.cold.1
+ _BWDeviceModelIsD23Proto1.identifyBuildPhaseOnceToken
+ _BWDeviceModelIsD23Proto1.isD23Proto1
+ _BWDroppedSampleReasonSmartCropFailure
+ _BWFigVideoCaptureDeviceFigPulseGeneratorUpdateNotification
+ _BWFigVideoCaptureDeviceLiveReconfigurationCompleteNotification
+ _BWFigVideoCaptureDeviceNotificationOutputAspectRatioRequestID
+ _BWFigVideoCaptureDeviceNotificationOutputAspectRatioRequestID_block_invoke.sHasReportedInvalidOrientation
+ _BWInferenceAttachedMediaKey_LandscapeCropLearnedNROutput
+ _BWInferenceAttachedMediaKey_PortraitCropLearnedNROutput
+ _BWInferenceAttachedMediaKey_SquareCropLearnedNROutput
+ _BWInferenceAttachmentKey_CamGazeRawProbabilities
+ _BWNodeSubTypeMultiCamClientCompositing
+ _BWNodeSubTypeSmartCrop
+ _BWNodeSubTypeSmartFramingPerceptionSinkNode
+ _BWSmartFramingSceneMonitorAspectRatioFromFieldOfView
+ _BWSmartFramingSceneMonitorFieldOfViewKeyFromType
+ _BWSmartFramingSceneMonitorFieldOfViewTypeFromKey
+ _BWSmartFramingSceneMonitorGetFieldOfView
+ _BWSmartFramingSceneMonitorNormalizedFieldOfViewRectFromFieldOfView
+ _BWSmartFramingSuggestedFieldOfViewChangedNotification
+ _BWUpdateFrameLevelMetadataForProResRaw
+ _BWUpdateFrameLevelMetadataForProResRaw.cold.1
+ _BWUpdateFrameLevelMetadataForProResRaw.cold.2
+ _BWUpdateFrameLevelMetadataForProResRaw.cold.3
+ _BWUpdateFrameLevelMetadataForProResRaw.cold.4
+ _BWUpdateFrameLevelMetadataForProResRaw.cold.5
+ _CC_SHA256
+ _CFUUIDGetConstantUUIDWithBytes
+ _CFUUIDGetUUIDBytes
+ _CGFloatNearlyEqualToFloatWithTolerance
+ _CMILSCOISAdaptation_extrapolateV2LSCTable
+ _CMPhotoScaleAndRotateSessionTransformImage
+ _D23
+ _FigBoxedMetadataAppendCGRect
+ _FigCFArrayGetFloat32AtIndex
+ _FigCFDictionaryGetCGPointIfPresent
+ _FigCFDictionaryGetCGSizeIfPresent
+ _FigCaptureClientApplicationIDIsFaceTimeVariant
+ _FigCaptureClientCompositingMetadataCompositionPictureInPictureRectKey
+ _FigCaptureClientCompositingMetadataCoreImageGainMapPropertiesKey
+ _FigCaptureConvertDimensionsForAspectRatio
+ _FigCaptureDenormalizePoint
+ _FigCaptureFrontDepthDataToRGBRotationAngle.sFrontDepthDataToRGBRotationAngle
+ _FigCaptureGetAspectRatioFractionalDimensionsForAspectRatio
+ _FigCaptureGetAspectRatioFromFractionalAspectRatio
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataForFrontAndBackCameraComposition
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithColorCorrectionTemperatureAndTintColorCorrectionMatrices
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithColorTranslationMatrices
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithExposureTime
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithFullFrameRatePlaybackIntent
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithISOSpeedRating
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithLSCGains
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithShutterSpeedAngle
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithWhiteBalanceCCT
+ _FigCaptureMetadataUtilitiesCreateMovieLevelMetadataWithWhiteBalanceFactors
+ _FigCaptureMetadataUtilitiesMatchOrientationOfSize
+ _FigCaptureMetadataUtiltiesCreateFlexRangeImagePropertiesFromGainMapMetadata
+ _FigCaptureMetadataUtiltiesCreateFlexRangeImagePropertiesFromGainMapMetadata.cold.1
+ _FigCaptureMetadataUtiltiesCreateFlexRangeImagePropertiesFromGainMapMetadata.cold.2
+ _FigCaptureMetadataUtiltiesCreateFlexRangeImagePropertiesFromGainMapMetadata.cold.3
+ _FigCaptureSessionRemoteSetClientCompositingSinkCallback
+ _FigCaptureSessionRemoteSetClientCompositingSinkCallback.cold.1
+ _FigCaptureSessionRemoteSetClientCompositingSinkCallback.cold.2
+ _FigCaptureSessionSetClientCompositingSinkCallback
+ _FigCaptureSmartFramingFieldOfViewLandscape
+ _FigCaptureSmartFramingFieldOfViewNone
+ _FigCaptureSmartFramingFieldOfViewPortrait
+ _FigCaptureSmartFramingFieldOfViewStringFromType
+ _FigCaptureSmartFramingFieldOfViewTypeFromString
+ _FigCaptureSmartFramingFieldOfViewZoomedOutLandscape
+ _FigCaptureSmartFramingFieldOfViewZoomedOutPortrait
+ _FigCaptureSourceFormatKey_AppleLog2SupportedForProRes
+ _FigCaptureSourceFormatKey_DigitalFlashZeroShutterLagSupported
+ _FigCaptureSourceFormatKey_DynamicAspectRatioSupported
+ _FigCaptureSourceFormatKey_LearnedFusionSupported
+ _FigCaptureSourceFormatKey_LearnedHRNRSupported
+ _FigCaptureSourceFormatKey_LowLatencyStabilizationSupported
+ _FigCaptureSourceFormatKey_SmartCropCaptureStreamFormat
+ _FigCaptureSourceFormatKey_SmartCropMaxFrameRateOverride
+ _FigCaptureSourceFormatKey_SmartCropOutputHeight
+ _FigCaptureSourceFormatKey_SmartCropOutputWidth
+ _FigCaptureSourceFormatKey_SmartCropSourceFormat
+ _FigCaptureSourceFormatKey_SmartCropSupported
+ _FigCaptureSourceFormatKey_SmartFramingSupported
+ _FigCaptureSourceIsSensorMountedInPortraitOrientation
+ _FigCaptureSourceRemoteCopyExternalSyncDeviceDiscoverySessionSource
+ _FigCaptureSourceRemoteCopyExternalSyncDeviceDiscoverySessionSource.cold.1
+ _FigCaptureSourceRemoteCopyExternalSyncDeviceDiscoverySessionSource.cold.2
+ _FigCaptureSourceRemoteCopyExternalSyncDeviceDiscoverySessionSource.cold.3
+ _FigCaptureSourceRemoteCopyExternalSyncDeviceDiscoverySessionSource.cold.4
+ _FigCaptureStringForAspectRatio
+ _FigExternalSyncDeviceDiscoverySessionCreate
+ _FigExternalSyncDeviceDiscoverySessionCreate.cold.1
+ _FigRemote_CreateSerializedAtomDataForSampleBufferWithOptions
+ _FigSmartStyleCastTypeBrightPop
+ _IOCreatePlugInInterfaceForService
+ _IODestroyPlugInInterface
+ _IOObjectConformsTo
+ _IORegistryEntryGetParentIterator
+ _IORegistryEntryIDMatching
+ _MSGAllocateSyncHandle
+ _MSGConfigureBaseSync
+ _MSGConfigureDerivedSync
+ _MSGCreate
+ _MSGEnableSyncInterrupt
+ _MSGInitBaseSync
+ _MSGInitDerivedSync
+ _MSGReleaseSyncHandle
+ _MSGResetSync
+ _MSGStartSync
+ _OBJC_CLASS_$_BWMovieLevelMetadataForProResRaw
+ _OBJC_CLASS_$_BWMultiCamClientCompositingNode
+ _OBJC_CLASS_$_BWSmartCropNode
+ _OBJC_CLASS_$_BWSmartCropWarpingNode
+ _OBJC_CLASS_$_BWSmartFramingPerceptionSinkNode
+ _OBJC_CLASS_$_BWSmartFramingSceneMonitor
+ _OBJC_CLASS_$_EGStillImageLearnedFusionNRFNode
+ _OBJC_CLASS_$_EGStillImageLearnedFusionRoutingNode
+ _OBJC_CLASS_$_FigExternalSyncDevice
+ _OBJC_CLASS_$_FigExternalSyncDeviceDiscoverySessionDelegateHandler
+ _OBJC_CLASS_$_FigExternalSyncDeviceDiscoverySessionManager
+ _OBJC_CLASS_$_FigPulseGenerator
+ _OBJC_CLASS_$_TrackedFace
+ _OBJC_IVAR_$_AudioRemixSessionManager._multiCamClientCompositingEnabled
+ _OBJC_IVAR_$_AudioRemixSubscriber._usePIPAIngestSignalingDomain
+ _OBJC_IVAR_$_BWAudioConverterNode._multiCamClientCompositingEnabled
+ _OBJC_IVAR_$_BWAudioRemixAnalysisMetadataNode._multiCamClientCompositingEnabled
+ _OBJC_IVAR_$_BWCompressedShotBufferNode._optimizedFieldOfViewProcessingCropEnabled
+ _OBJC_IVAR_$_BWDeferredCaptureControllerInput._learnedFusionProxyGenerationUsedEVMinus
+ _OBJC_IVAR_$_BWDeferredCaptureControllerInput._stashedLearnedFusionEVMinus
+ _OBJC_IVAR_$_BWDeferredCaptureControllerInput._stashedLearnedFusionErrorRecovery
+ _OBJC_IVAR_$_BWDeferredPipelineParameters._cameraSensorOrientationCompensationDegreesCW
+ _OBJC_IVAR_$_BWDepthConverterNode._disparityAPSScaling
+ _OBJC_IVAR_$_BWDepthConverterNode._monocularStillsPipeline
+ _OBJC_IVAR_$_BWDisparityPostProcessingInferenceProvider._previousAspectRatioIsLandscape
+ _OBJC_IVAR_$_BWDisparityPostProcessingInferenceProvider._resetTemporalStateOnAspectRatioChange
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._bufferPTSByConfigurationID
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._configurationIDByOutputAspectRatioRequestID
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._hasLearnedFusion
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._liveReconfigureForOutputAspectRatioLock
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._msgClock
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._nextOutputAspectRatioRequestIDToRemove
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._outputAspectRatioRequestIDByConfigurationID
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._portTypesWithDigitalFlashZeroShutterLagEnabled
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartCropCandidateFramingRects
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartCropSupported
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingAvoidsResolvingSuggestedFieldOfViewForFlashScene
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingConfiguredFieldOfView
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingEnabled
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingEnabledFieldsOfView
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingFlashScene
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingIsMonitoringScene
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingLock
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingRequiresSceneMonitoring
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingSceneMonitor
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingSuggestedFieldOfView
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._smartFramingZoomFactorsByFieldOfView
+ _OBJC_IVAR_$_BWFigVideoCaptureStream._activeVideoExternalSyncFrameRate
+ _OBJC_IVAR_$_BWFigVideoCaptureStream._activeVideoLockedFrameRate
+ _OBJC_IVAR_$_BWFigVideoCaptureStream._baseZoomFactorOverridesByAspectRatio
+ _OBJC_IVAR_$_BWFigVideoCaptureStream._digitalFlashZeroShutterLagEnabled
+ _OBJC_IVAR_$_BWInferenceVideoScalingProvider._disableRotationInLandscapeAspectRatio
+ _OBJC_IVAR_$_BWIrisStagingNode._smartFramingEnabled
+ _OBJC_IVAR_$_BWLearnedNRProcessorControllerConfiguration._landscapeCropOutputFormat
+ _OBJC_IVAR_$_BWLearnedNRProcessorControllerConfiguration._portraitCropOutputFormat
+ _OBJC_IVAR_$_BWLearnedNRProcessorControllerConfiguration._squareCropOutputFormat
+ _OBJC_IVAR_$_BWMemoryAnalyticsPayload._captureTypeLearnedFusion
+ _OBJC_IVAR_$_BWMotionAttachmentsNode._emitMotionAttachmentsSBufForOfflineProResRawVIS
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._cameraManufacturer
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._cameraModelName
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._cctAndTintColorMatrices
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._colorTranslationMatrices
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._currentFrameRate
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._exposureTime
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._isMetadataValid
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._isoSpeedRating
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._lscGains
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._shutterSpeedAngle
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._whiteBalanceCCT
+ _OBJC_IVAR_$_BWMovieLevelMetadataForProResRaw._whiteBalanceFactors
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._bufferSynchronizer
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._clientCompositingCallback
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._compositingStrategy
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._compositionPictureInPictureRectMetadataFormatDescription
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._compositionPictureInPictureRectMetadataLocalID
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._compositionPictureInPictureRectMetadataOutput
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._gainMapSupported
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._indexOfInputProvidingOutputSampleBuffer
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._movieSettings
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._outputGainMapPixelBufferPool
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._outputGainMapSampleBufferFormatDescription
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._outputPixelBufferPool
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._outputSampleBufferFormatDescription
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._primaryStillSampleBuffer
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._receivedNodeError
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._secondaryStillSampleBuffer
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._stillImageSettings
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._stillsInputLock
+ _OBJC_IVAR_$_BWMultiCamClientCompositingNode._thresholdToRemovePrimaryBufferDetectedFacesObscuredByPIP
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._aspectRatio
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._dynamicAspectRatioChangePending
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._dynamicAspectRatioGraphPrepared
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._dynamicAspectRatioLock
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._dynamicAspectRatioOutputConfigurations
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNode._dynamicAspectRatioVISOverscan
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._adaptiveSensorCropForDynamicAspectRatioEnabled
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._baseZoomFactorOverridesByAspectRatio
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._dynamicAspectRatioEnabled
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._externalSyncFrameRate
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._lockedFrameRate
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._proResRawCaptureEnabled
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._sensorOutputLargerThanImageCircle
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._visOverscanByAspectRatio
+ _OBJC_IVAR_$_BWNRFProcessorControllerConfiguration._learnedFusionEnabled
+ _OBJC_IVAR_$_BWNRFProcessorControllerConfiguration._learnedFusionInputFormat
+ _OBJC_IVAR_$_BWPhotonicEngineNodeConfiguration._portTypesWithLearnedFusionEnabled
+ _OBJC_IVAR_$_BWPhotonicEngineNodeResourceCoordinator._distortionCorrectionEnhancedResolutionOutputPool
+ _OBJC_IVAR_$_BWPreviewStitcherNode._limitCropRectWithinImageCircle
+ _OBJC_IVAR_$_BWPreviewStitcherNode._previousAspectRatioIsLandscape
+ _OBJC_IVAR_$_BWPreviewStitcherNode._sensorOrientationByPortType
+ _OBJC_IVAR_$_BWPreviewStitcherNode._singleCameraOverCaptureEnabled
+ _OBJC_IVAR_$_BWPreviewStitcherNode._singleCameraOverCaptureRemainingFramesUntilStopOverCaptureRendering
+ _OBJC_IVAR_$_BWPreviewStitcherNode._singleCameraOverCaptureShouldStopOverCaptureRendering
+ _OBJC_IVAR_$_BWPreviewStitcherNode._smartFramingConfiguredFieldOfView
+ _OBJC_IVAR_$_BWPreviewStitcherNode._smartFramingEnabled
+ _OBJC_IVAR_$_BWPreviewStitcherNode._smartFramingFieldOfViewTransitionNotifyAppliedZoomFactors
+ _OBJC_IVAR_$_BWPreviewStitcherNode._smartFramingPreviousTransitionTargetFieldOfView
+ _OBJC_IVAR_$_BWPreviewStitcherNode._smartFramingTransitionInProgress
+ _OBJC_IVAR_$_BWPreviewStitcherNode._smartFramingTransitionInterruptedByTrueVideoTransition
+ _OBJC_IVAR_$_BWPreviewStitcherNode._smartFramingTransitionPercentComplete
+ _OBJC_IVAR_$_BWPreviewStitcherNode._smartFramingTransitionTargetFieldOfView
+ _OBJC_IVAR_$_BWPreviewStitcherNode._smartFramingZoomFactorsByFieldOfView
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._cameraInfoForPortType
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._frontRearSimultaneousVideoRecording
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._movieLevelMetadataForProResRawFromFirstFrame
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._writeFirstFrameMetadataForProResRaw
+ _OBJC_IVAR_$_BWRemoteQueueSinkNode._cameraInfoByPortType
+ _OBJC_IVAR_$_BWRemoteQueueSinkNode._movieLevelMetadataForProResRaw
+ _OBJC_IVAR_$_BWRemoteQueueSinkNode._proresRawVideo
+ _OBJC_IVAR_$_BWSmartCropNode._bufferServicingLock
+ _OBJC_IVAR_$_BWSmartCropNode._cameraExtrinsicMatrix
+ _OBJC_IVAR_$_BWSmartCropNode._cameraInfoByPortType
+ _OBJC_IVAR_$_BWSmartCropNode._captureDevice
+ _OBJC_IVAR_$_BWSmartCropNode._detectionMetadataInput
+ _OBJC_IVAR_$_BWSmartCropNode._detectionMetadataIsLive
+ _OBJC_IVAR_$_BWSmartCropNode._detectionMetadataOutput
+ _OBJC_IVAR_$_BWSmartCropNode._horizontalSensorBinningFactor
+ _OBJC_IVAR_$_BWSmartCropNode._liveReconfigurationInProgress
+ _OBJC_IVAR_$_BWSmartCropNode._maxLossyCompressionLevel
+ _OBJC_IVAR_$_BWSmartCropNode._outputDimensions
+ _OBJC_IVAR_$_BWSmartCropNode._outputFormatDescription
+ _OBJC_IVAR_$_BWSmartCropNode._portTypes
+ _OBJC_IVAR_$_BWSmartCropNode._processingMode
+ _OBJC_IVAR_$_BWSmartCropNode._rtscProcessor
+ _OBJC_IVAR_$_BWSmartCropNode._stillCaptureEnabled
+ _OBJC_IVAR_$_BWSmartCropNode._stillHomographyByPTS
+ _OBJC_IVAR_$_BWSmartCropNode._stillHomographyQueueLock
+ _OBJC_IVAR_$_BWSmartCropNode._stillPTSQueue
+ _OBJC_IVAR_$_BWSmartCropNode._verticalSensorBinningFactor
+ _OBJC_IVAR_$_BWSmartCropNode._videoOutputFormatIsLive
+ _OBJC_IVAR_$_BWSmartCropWarpingNode._activeAspectRatio
+ _OBJC_IVAR_$_BWSmartCropWarpingNode._bufferServicingLock
+ _OBJC_IVAR_$_BWSmartCropWarpingNode._formatDimensions
+ _OBJC_IVAR_$_BWSmartCropWarpingNode._homographyProvider
+ _OBJC_IVAR_$_BWSmartCropWarpingNode._rtscProcessor
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._camGazeInferenceMajorVersion
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._captureDevice
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._faceGroupIDsForInference
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._inferenceEngine
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._inferenceLock
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._inferenceProcessingConfiguration
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._inferenceQueue
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._inferenceScheduler
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._inferenceSkipInterval
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._lastInferenceFramePTS
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._lastSampleBuffer
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._maxFaceCountForInference
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._previousInferenceComplete
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._cumulativeSuggestedFOVType
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._detectedObjectsInfo
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._detectedObjectsInfoPTS
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._faceRectExpansionScaleFactor
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._faceSignificanceDetectionThreshold
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._faceTracks
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._fieldsOfView
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._gazeProbabilitiesByFaceGroupID
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._lastFaceDetectionPTS
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._lastSuggestedFieldOfViewChangePTS
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._minimumRequiredSignificantFaceCount
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._noFaceDetectedZoomOutTimeInSeconds
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._optimalFOVHistory
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._optimalFOVHistoryPTS
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._suggestedFOVSlackDurationInSeconds
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._useDynamicFieldOfViewRects
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._viewsInAscendingFOV
+ _OBJC_IVAR_$_BWSmartFramingSceneMonitor._zoomInTransitionEnabled
+ _OBJC_IVAR_$_BWSoftISPProcessorControllerConfiguration._learnedFusionEnabled
+ _OBJC_IVAR_$_BWStillImageNodeConfiguration._cameraSensorOrientationCompensationDegreesCW
+ _OBJC_IVAR_$_BWStreamingCVAFilterRenderer._disableDepthAndSegmentationRotationInLandscape
+ _OBJC_IVAR_$_BWStreamingFilterNode._disableDepthAndSegmentationRotationInLandscape
+ _OBJC_IVAR_$_BWStreamingFilterNode._squareAspectRatioConfigEnabled
+ _OBJC_IVAR_$_BWVISNode._faceStabilizationEnabled
+ _OBJC_IVAR_$_BWVISNode._faceStabilizationSigmaMultiplierForBiasTracking
+ _OBJC_IVAR_$_BWVISNode._faceStabilizationSigmaMultiplierForFaceFiltering
+ _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._faceStabilizationEnabled
+ _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._faceStabilizationSigmaMultiplierForBiasTracking
+ _OBJC_IVAR_$_BWVISProcessorControllerConfiguration._faceStabilizationSigmaMultiplierForFaceFiltering
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._colorFeaturesDimensions
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._colorFeaturesPixelFormat
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._disparityMultiplierFormat
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._monocularDepthScaleFactor
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._monocularPipelineLock
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._monocularVideoInferenceDescriptor
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._monocularVideoPipeline
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._networkHeight
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._networkWidth
+ _OBJC_IVAR_$_BWVideoDepthInferenceConfiguration._sensorIDString
+ _OBJC_IVAR_$_BWVideoDepthNode._disparityAPSScaling
+ _OBJC_IVAR_$_BWVideoDepthNode._disparityMultiplierFormat
+ _OBJC_IVAR_$_BWVideoDepthNode._disparityMultiplierPixelBuffer
+ _OBJC_IVAR_$_BWVideoDepthNode._disparityScalingFactor
+ _OBJC_IVAR_$_BWVideoDepthNode._lastTimeStampWhenAPSComputed
+ _OBJC_IVAR_$_BWVideoDepthNode._networkInputIsRotated
+ _OBJC_IVAR_$_BWVideoDepthNode._previousAspectRatioIsLandscape
+ _OBJC_IVAR_$_BWVideoDepthNode._useMonocularInference
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._attemptErrorRecoveryOutput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._errorCodeTriggeringErrorRecovery
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._fusionModeOutput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._handleSyncErrorRecovery
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._hdrErrorRecoveryEVZeroInput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._inferenceInputImageOutput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._nodeConfiguration
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._nrfProcessorControllerErrorRecoveryInput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._nrfProcessorControllerInput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._portType
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._primarySbufInputs
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._processSmartStyleRenderingInput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._processorInput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._provideInferenceInputImageForProcessing
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._referenceFrameInput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._sbufOutput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._stashedNRFProcessorController
+ _OBJC_IVAR_$_EGStillImageLearnedFusionNRFNode._stillImageSettings
+ _OBJC_IVAR_$_EGStillImageLearnedFusionRoutingNode._evMinusOutput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionRoutingNode._evZeroOutput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionRoutingNode._longOutput
+ _OBJC_IVAR_$_EGStillImageLearnedFusionRoutingNode._sampleBufferInputs
+ _OBJC_IVAR_$_EGStillImageLearnedFusionRoutingNode._secondEvZeroOutput
+ _OBJC_IVAR_$_FigCaptureCameraParameters._monocularStreamingDepthParameters
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._lowLatencyStabilizationEnabled
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._smartCropHomographyProvider
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._smartCropNodesBySourceDeviceType
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipelineConfiguration._lowLatencyStabilizationEnabledInSourcePipeline
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipelineConfiguration._multiCamClientCompositingPrimaryCameraVideoStabilizationStrength
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipelineConfiguration._smartFramingEnabled
+ _OBJC_IVAR_$_FigCaptureIrisSinkConfiguration._cameraSensorOrientationCompensationEnabled
+ _OBJC_IVAR_$_FigCaptureIrisSinkConfiguration._multiCamClientCompositingEnabled
+ _OBJC_IVAR_$_FigCaptureIrisSinkConfiguration._multiCamClientCompositingPrimaryConnectionID
+ _OBJC_IVAR_$_FigCaptureMovieFileSinkConfiguration._multiCamClientCompositingEnabled
+ _OBJC_IVAR_$_FigCaptureMovieFileSinkConfiguration._multiCamClientCompositingPrimaryConnectionID
+ _OBJC_IVAR_$_FigCaptureMovieFileSinkPipelineConfiguration._lowLatencyStabilizationEnabled
+ _OBJC_IVAR_$_FigCaptureMovieFileSinkTailPipeline._smartCropNode
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipeline._dynamicAspectRatioChangeSource
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipeline._isPrimaryStillImagePipeline
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipeline._multiCamClientCompositingNode
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipeline._outputForSecondaryStillImagePipeline
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._cameraSensorOrientationCompensationDegreesCW
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._learnedHRNRSupported
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._portTypesWithDigitalFlashZeroShutterLagEnabled
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._portTypesWithLearnedFusionEnabled
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._smartCropWarpingOutputDimensions
+ _OBJC_IVAR_$_FigCapturePhotonicEngineSinkPipelineConfiguration._smartCropWarpingRequired
+ _OBJC_IVAR_$_FigCapturePreviewSinkPipeline._lowLatencyStabilizationNode
+ _OBJC_IVAR_$_FigCapturePreviewSinkPipeline._singleCameraOverCaptureEnabled
+ _OBJC_IVAR_$_FigCapturePreviewSinkPipelineConfiguration._lowLatencyStabilizationEnabled
+ _OBJC_IVAR_$_FigCapturePreviewSinkPipelineConfiguration._singleCameraOverCaptureEnabled
+ _OBJC_IVAR_$_FigCaptureSessionParsedCameraSourceConfiguration._multiCamClientCompositingPrimaryCameraVideoStabilizationStrength
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._externalSyncFrameRate
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._lockedFrameRate
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._outputAspectRatio
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._outputAspectRatioRequestID
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._smartFramingEnabled
+ _OBJC_IVAR_$_FigCaptureSourceVideoFormat._smartCropFormat
+ _OBJC_IVAR_$_FigCaptureStillImageSinkConfiguration._cameraSensorOrientationCompensationEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipeline._lowLatencyStabilizationNode
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipelineConfiguration._lowLatencyStabilizationEnabled
+ _OBJC_IVAR_$_FigExternalSyncDevice._externalSyncDeviceDeviceIdentifer
+ _OBJC_IVAR_$_FigExternalSyncDevice._hpmentid
+ _OBJC_IVAR_$_FigExternalSyncDevice._ioServiceNotificationPort
+ _OBJC_IVAR_$_FigExternalSyncDevice._pid
+ _OBJC_IVAR_$_FigExternalSyncDevice._queue
+ _OBJC_IVAR_$_FigExternalSyncDevice._serviceNotification
+ _OBJC_IVAR_$_FigExternalSyncDevice._ssamEnabled
+ _OBJC_IVAR_$_FigExternalSyncDevice._ssamentid
+ _OBJC_IVAR_$_FigExternalSyncDevice._usbConnected
+ _OBJC_IVAR_$_FigExternalSyncDevice._vid
+ _OBJC_IVAR_$_FigExternalSyncDeviceDiscoverySessionDelegateHandler._source
+ _OBJC_IVAR_$_FigExternalSyncDeviceDiscoverySessionDelegateHandler._sourceLock
+ _OBJC_IVAR_$_FigExternalSyncDeviceDiscoverySessionManager._activeClients
+ _OBJC_IVAR_$_FigExternalSyncDeviceDiscoverySessionManager._firstMatchIterator
+ _OBJC_IVAR_$_FigExternalSyncDeviceDiscoverySessionManager._ioServiceNotificationPort
+ _OBJC_IVAR_$_FigExternalSyncDeviceDiscoverySessionManager._managedExternalSyncDevices
+ _OBJC_IVAR_$_FigExternalSyncDeviceDiscoverySessionManager._observingSSAMEvents
+ _OBJC_IVAR_$_FigExternalSyncDeviceDiscoverySessionManager._queue
+ _OBJC_IVAR_$_FigExternalSyncDeviceDiscoverySessionManager._serviceNotification
+ _OBJC_IVAR_$_FigPulseGenerator._activeDerivedSyncConfig
+ _OBJC_IVAR_$_FigPulseGenerator._configureLock
+ _OBJC_IVAR_$_FigPulseGenerator._currentFrameRate
+ _OBJC_IVAR_$_FigPulseGenerator._delegate
+ _OBJC_IVAR_$_FigPulseGenerator._disciplinedMSGTimeSyncClock
+ _OBJC_IVAR_$_FigPulseGenerator._enabled
+ _OBJC_IVAR_$_FigPulseGenerator._hasNotifiedDelegateOfClockCreation
+ _OBJC_IVAR_$_FigPulseGenerator._isExternalSync
+ _OBJC_IVAR_$_FigPulseGenerator._msgHandleFront
+ _OBJC_IVAR_$_FigPulseGenerator._msgHandleLeader
+ _OBJC_IVAR_$_FigPulseGenerator._msgHandleRear
+ _OBJC_IVAR_$_FigPulseGenerator._timeSyncClockRef
+ _OBJC_IVAR_$_FigPulseGenerator._timeSyncMSGClockIdentifier
+ _OBJC_IVAR_$_TrackedFace._faceGroupID
+ _OBJC_IVAR_$_TrackedFace._faceRects
+ _OBJC_IVAR_$_TrackedFace._faceSizeScoreFiltered
+ _OBJC_IVAR_$_TrackedFace._faceSizes
+ _OBJC_IVAR_$_TrackedFace._firstSignificantTimeStamp
+ _OBJC_IVAR_$_TrackedFace._gazeConfidences
+ _OBJC_IVAR_$_TrackedFace._gazeScores
+ _OBJC_IVAR_$_TrackedFace._isPersistentlySignificant
+ _OBJC_IVAR_$_TrackedFace._isSignificant
+ _OBJC_IVAR_$_TrackedFace._significanceDetectionThreshold
+ _OBJC_METACLASS_$_BWMovieLevelMetadataForProResRaw
+ _OBJC_METACLASS_$_BWMultiCamClientCompositingNode
+ _OBJC_METACLASS_$_BWSmartCropNode
+ _OBJC_METACLASS_$_BWSmartCropWarpingNode
+ _OBJC_METACLASS_$_BWSmartFramingPerceptionSinkNode
+ _OBJC_METACLASS_$_BWSmartFramingSceneMonitor
+ _OBJC_METACLASS_$_EGStillImageLearnedFusionNRFNode
+ _OBJC_METACLASS_$_EGStillImageLearnedFusionRoutingNode
+ _OBJC_METACLASS_$_FigExternalSyncDevice
+ _OBJC_METACLASS_$_FigExternalSyncDeviceDiscoverySessionDelegateHandler
+ _OBJC_METACLASS_$_FigExternalSyncDeviceDiscoverySessionManager
+ _OBJC_METACLASS_$_FigPulseGenerator
+ _OBJC_METACLASS_$_TrackedFace
+ _OUTLINED_FUNCTION_364
+ _OUTLINED_FUNCTION_365
+ _OUTLINED_FUNCTION_366
+ _OUTLINED_FUNCTION_367
+ _OUTLINED_FUNCTION_368
+ _OUTLINED_FUNCTION_369
+ _OUTLINED_FUNCTION_370
+ _OUTLINED_FUNCTION_371
+ _OUTLINED_FUNCTION_372
+ _OUTLINED_FUNCTION_373
+ _OUTLINED_FUNCTION_374
+ _OUTLINED_FUNCTION_375
+ _OUTLINED_FUNCTION_376
+ _T2030
+ _TSNullClockIdentifier
+ _TimeSyncClockCreateAudioClockDeviceUID
+ _TimeSyncMSGAddClockInstance
+ _TimeSyncMSGClockInstanceIdentifier
+ _TimeSyncMSGRemoveClockInstance
+ _TimeSyncMSGStartExternalSync
+ _TimeSyncMSGStopExternalSync
+ _V53_V54
+ _V57
+ __OBJC_$_CLASS_METHODS_BWMultiCamClientCompositingNode
+ __OBJC_$_CLASS_METHODS_BWSmartCropNode
+ __OBJC_$_CLASS_METHODS_BWSmartCropWarpingNode
+ __OBJC_$_CLASS_METHODS_BWSmartFramingPerceptionSinkNode
+ __OBJC_$_CLASS_METHODS_BWSmartFramingSceneMonitor
+ __OBJC_$_CLASS_METHODS_EGStillImageLearnedFusionNRFNode
+ __OBJC_$_CLASS_METHODS_EGStillImageLearnedFusionRoutingNode
+ __OBJC_$_CLASS_METHODS_FigExternalSyncDeviceDiscoverySessionManager
+ __OBJC_$_CLASS_METHODS_FigPulseGenerator
+ __OBJC_$_INSTANCE_METHODS_BWMovieLevelMetadataForProResRaw
+ __OBJC_$_INSTANCE_METHODS_BWMultiCamClientCompositingNode
+ __OBJC_$_INSTANCE_METHODS_BWSmartCropNode
+ __OBJC_$_INSTANCE_METHODS_BWSmartCropWarpingNode
+ __OBJC_$_INSTANCE_METHODS_BWSmartFramingPerceptionSinkNode
+ __OBJC_$_INSTANCE_METHODS_BWSmartFramingSceneMonitor
+ __OBJC_$_INSTANCE_METHODS_EGStillImageLearnedFusionNRFNode
+ __OBJC_$_INSTANCE_METHODS_EGStillImageLearnedFusionRoutingNode
+ __OBJC_$_INSTANCE_METHODS_FigExternalSyncDevice
+ __OBJC_$_INSTANCE_METHODS_FigExternalSyncDeviceDiscoverySessionDelegateHandler
+ __OBJC_$_INSTANCE_METHODS_FigExternalSyncDeviceDiscoverySessionManager
+ __OBJC_$_INSTANCE_METHODS_FigPulseGenerator
+ __OBJC_$_INSTANCE_METHODS_TrackedFace
+ __OBJC_$_INSTANCE_VARIABLES_BWMovieLevelMetadataForProResRaw
+ __OBJC_$_INSTANCE_VARIABLES_BWMultiCamClientCompositingNode
+ __OBJC_$_INSTANCE_VARIABLES_BWSmartCropNode
+ __OBJC_$_INSTANCE_VARIABLES_BWSmartCropWarpingNode
+ __OBJC_$_INSTANCE_VARIABLES_BWSmartFramingPerceptionSinkNode
+ __OBJC_$_INSTANCE_VARIABLES_BWSmartFramingSceneMonitor
+ __OBJC_$_INSTANCE_VARIABLES_EGStillImageLearnedFusionNRFNode
+ __OBJC_$_INSTANCE_VARIABLES_EGStillImageLearnedFusionRoutingNode
+ __OBJC_$_INSTANCE_VARIABLES_FigExternalSyncDevice
+ __OBJC_$_INSTANCE_VARIABLES_FigExternalSyncDeviceDiscoverySessionDelegateHandler
+ __OBJC_$_INSTANCE_VARIABLES_FigExternalSyncDeviceDiscoverySessionManager
+ __OBJC_$_INSTANCE_VARIABLES_FigPulseGenerator
+ __OBJC_$_INSTANCE_VARIABLES_TrackedFace
+ __OBJC_$_PROP_LIST_BWDynamicAspectRatioChangeSource
+ __OBJC_$_PROP_LIST_BWMultiCamClientCompositingNode
+ __OBJC_$_PROP_LIST_BWSmartCropNode
+ __OBJC_$_PROP_LIST_BWSmartCropWarpingNode
+ __OBJC_$_PROP_LIST_BWSmartFramingPerceptionSinkNode
+ __OBJC_$_PROP_LIST_EGStillImageLearnedFusionNRFNode
+ __OBJC_$_PROP_LIST_EGStillImageLearnedFusionRoutingNode
+ __OBJC_$_PROP_LIST_FigExternalSyncDevice
+ __OBJC_$_PROP_LIST_FigExternalSyncDeviceDiscoverySessionDelegateHandler
+ __OBJC_$_PROP_LIST_FigPulseGenerator
+ __OBJC_$_PROP_LIST_TrackedFace
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BWDynamicAspectRatioChangeSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BWSmartCropHomographyProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_FigExternalSyncDeviceDiscoverySessionManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FigPulseGeneratorDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BWDynamicAspectRatioChangeSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BWSmartCropHomographyProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FigExternalSyncDeviceDiscoverySessionManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FigPulseGeneratorDelegate
+ __OBJC_$_PROTOCOL_REFS_BWDynamicAspectRatioChangeSource
+ __OBJC_$_PROTOCOL_REFS_BWSmartCropHomographyProvider
+ __OBJC_$_PROTOCOL_REFS_FigExternalSyncDeviceDiscoverySessionManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_FigPulseGeneratorDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BWSmartCropNode
+ __OBJC_CLASS_PROTOCOLS_$_BWSmartCropWarpingNode
+ __OBJC_CLASS_PROTOCOLS_$_BWSmartFramingPerceptionSinkNode
+ __OBJC_CLASS_PROTOCOLS_$_EGStillImageLearnedFusionNRFNode
+ __OBJC_CLASS_PROTOCOLS_$_FigExternalSyncDeviceDiscoverySessionDelegateHandler
+ __OBJC_CLASS_RO_$_BWMovieLevelMetadataForProResRaw
+ __OBJC_CLASS_RO_$_BWMultiCamClientCompositingNode
+ __OBJC_CLASS_RO_$_BWSmartCropNode
+ __OBJC_CLASS_RO_$_BWSmartCropWarpingNode
+ __OBJC_CLASS_RO_$_BWSmartFramingPerceptionSinkNode
+ __OBJC_CLASS_RO_$_BWSmartFramingSceneMonitor
+ __OBJC_CLASS_RO_$_EGStillImageLearnedFusionNRFNode
+ __OBJC_CLASS_RO_$_EGStillImageLearnedFusionRoutingNode
+ __OBJC_CLASS_RO_$_FigExternalSyncDevice
+ __OBJC_CLASS_RO_$_FigExternalSyncDeviceDiscoverySessionDelegateHandler
+ __OBJC_CLASS_RO_$_FigExternalSyncDeviceDiscoverySessionManager
+ __OBJC_CLASS_RO_$_FigPulseGenerator
+ __OBJC_CLASS_RO_$_TrackedFace
+ __OBJC_LABEL_PROTOCOL_$_BWDynamicAspectRatioChangeSource
+ __OBJC_LABEL_PROTOCOL_$_BWSmartCropHomographyProvider
+ __OBJC_LABEL_PROTOCOL_$_FigExternalSyncDeviceDiscoverySessionManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_FigPulseGeneratorDelegate
+ __OBJC_METACLASS_RO_$_BWMovieLevelMetadataForProResRaw
+ __OBJC_METACLASS_RO_$_BWMultiCamClientCompositingNode
+ __OBJC_METACLASS_RO_$_BWSmartCropNode
+ __OBJC_METACLASS_RO_$_BWSmartCropWarpingNode
+ __OBJC_METACLASS_RO_$_BWSmartFramingPerceptionSinkNode
+ __OBJC_METACLASS_RO_$_BWSmartFramingSceneMonitor
+ __OBJC_METACLASS_RO_$_EGStillImageLearnedFusionNRFNode
+ __OBJC_METACLASS_RO_$_EGStillImageLearnedFusionRoutingNode
+ __OBJC_METACLASS_RO_$_FigExternalSyncDevice
+ __OBJC_METACLASS_RO_$_FigExternalSyncDeviceDiscoverySessionDelegateHandler
+ __OBJC_METACLASS_RO_$_FigExternalSyncDeviceDiscoverySessionManager
+ __OBJC_METACLASS_RO_$_FigPulseGenerator
+ __OBJC_METACLASS_RO_$_TrackedFace
+ __OBJC_PROTOCOL_$_BWDynamicAspectRatioChangeSource
+ __OBJC_PROTOCOL_$_BWSmartCropHomographyProvider
+ __OBJC_PROTOCOL_$_FigExternalSyncDeviceDiscoverySessionManagerDelegate
+ __OBJC_PROTOCOL_$_FigPulseGeneratorDelegate
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.705
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.715
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke_2.706
+ ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.149
+ ___107-[BWFigCaptureSession stillImageCoordinator:didCancelMomentCaptureForSettingsID:streamingDisruptionEndPTS:]_block_invoke.101
+ ___107-[BWFigCaptureSession stillImageCoordinator:didCancelMomentCaptureForSettingsID:streamingDisruptionEndPTS:]_block_invoke.97
+ ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.657
+ ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.657.cold.1
+ ___115-[BWSmartFramingSceneMonitor _getOptimalFieldOfViewKeyFromCumulativeFieldOfViewWeights:significantFaceOrBodyCount:]_block_invoke
+ ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.677
+ ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.677.cold.1
+ ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.677.cold.2
+ ___145-[BWMultiCamClientCompositingNode _updateOutputSampleBufferDetectedFaces:withSecondarySampleBufferDetectedFaces:compositionPictureInPictureRect:]_block_invoke
+ ___145-[BWSmartFramingSceneMonitor _resolveSuggestedFieldOfViewWithSampleBuffer:usingFieldsOfView:suggestedFieldOfViewOut:suggestedFieldOfViewRectOut:]_block_invoke
+ ___32+[FigPulseGenerator isSupported]_block_invoke
+ ___396-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:]_block_invoke
+ ___396-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:]_block_invoke.1112
+ ___396-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:]_block_invoke.773
+ ___396-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:]_block_invoke.953
+ ___396-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:]_block_invoke_2
+ ___396-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:]_block_invoke_2.1147
+ ___407-[BWStreamingCVAFilterRenderer initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:secondaryStreamingPersonSegmentationEnabled:cropDepthToPrimaryCaptureAspectRatio:disableDepthAndSegmentationRotationInLandscape:]_block_invoke
+ ___44+[FigPulseGenerator sharedFigPulseGenerator]_block_invoke
+ ___46-[BWSmartCropNode _updateDetectedObjectsInfo:]_block_invoke
+ ___47-[BWSmartCropNode _supportedOutputPixelFormats]_block_invoke
+ ___49-[BWPhotonicEngineNode didSelectFormat:forInput:]_block_invoke
+ ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.391
+ ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke_2.394
+ ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.368
+ ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.371
+ ___53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.1058
+ ___53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.1058.cold.1
+ ___53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.1058.cold.2
+ ___53-[BWSmartCropWarpingNode _updateDetectedObjectsInfo:]_block_invoke
+ ___62-[FigExternalSyncDeviceDiscoverySessionManager currentDevices]_block_invoke
+ ___63-[BWSmartFramingPerceptionSinkNode _waitForInferenceToComplete]_block_invoke
+ ___64-[BWSmartFramingPerceptionSinkNode renderSampleBuffer:forInput:]_block_invoke
+ ___66-[BWPhotonicEngineNode didReachEndOfDataForConfigurationID:input:]_block_invoke_6
+ ___72-[BWCompressedShotBufferNode _copyRAWThumbnailsForSampleBufferIfNeeded:]_block_invoke_2
+ ___72-[BWCompressedShotBufferNode _copyRAWThumbnailsForSampleBufferIfNeeded:]_block_invoke_2.cold.1
+ ___72-[FigExternalSyncDeviceDiscoverySessionManager deviceDisconnectedEvent:]_block_invoke
+ ___72-[FigExternalSyncDeviceDiscoverySessionManager registerClient:delegate:]_block_invoke
+ ___73-[BWDeferredProcessingContainer hasBufferWithCaptureFrameFlags:portType:]_block_invoke
+ ___73-[BWPhotonicEngineNode _handleClientBracketFrameEmissionForSampleBuffer:]_block_invoke.415
+ ___75-[FigExternalSyncDeviceDiscoverySessionManager unregisterAndCleanupClient:]_block_invoke
+ ___84-[BWAudioSourceNode updateStereoAudioCapturePairedCameraBaseFieldOfView:zoomFactor:]_block_invoke
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.583
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.583.cold.1
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.584
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.584.cold.1
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.584.cold.2
+ ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.575
+ ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.575.cold.1
+ ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.626
+ ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.626.cold.1
+ ___98+[FigExternalSyncDeviceDiscoverySessionManager sharedFigExternalSyncDeviceDiscoverySessionManager]_block_invoke
+ ___BWDeviceModelIsD23Proto1_block_invoke
+ ___FigCaptureClientApplicationIDIsFaceTimeVariant_block_invoke
+ ___block_descriptor_40_e8_32o_e42_v24?0"NSMutableDictionary"8"NSString"16ls32l8
+ ___block_descriptor_48_e8_32o40o_e168_i72?0q8^{opaqueCMSampleBuffer=}16^{opaqueCMSampleBuffer=}24^{opaqueCMSampleBuffer=}32^{opaqueCMSampleBuffer=}40^{opaqueCMSampleBuffer=}48^{opaqueCMSampleBuffer=}56^64ls32l8s40l8
+ ___block_descriptor_48_e8_32o_e201_i80?0^{__CFString=}8q16^{opaqueCMSampleBuffer=}24^{opaqueCMSampleBuffer=}32^{opaqueCMSampleBuffer=}40^{opaqueCMSampleBuffer=}48^{opaqueCMSampleBuffer=}56^{opaqueCMSampleBuffer=}64r^^{__CFDictionary}72ls32l8
+ ___block_descriptor_56_e8_32o40o_e21_v16?0^{__CFString=}8ls32l8s40l8
+ ___block_descriptor_64_e8_32o40o48o56o_e38_v32?0"NSString"8"TrackedFace"16^B24ls32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_descriptor_80_e8_32o_e39_B24?0"NSDictionary"8"NSDictionary"16ls32l8
+ ___block_literal_global.1038
+ ___block_literal_global.1219
+ ___block_literal_global.1232
+ ___block_literal_global.126
+ ___block_literal_global.1269
+ ___block_literal_global.1272
+ ___block_literal_global.1280
+ ___block_literal_global.1291
+ ___block_literal_global.1301
+ ___block_literal_global.1304
+ ___block_literal_global.1327
+ ___block_literal_global.1329
+ ___block_literal_global.229
+ ___block_literal_global.240
+ ___block_literal_global.244
+ ___block_literal_global.246
+ ___block_literal_global.248
+ ___block_literal_global.265
+ ___block_literal_global.275
+ ___block_literal_global.298
+ ___block_literal_global.312
+ ___block_literal_global.317
+ ___block_literal_global.354
+ ___block_literal_global.359
+ ___block_literal_global.36
+ ___block_literal_global.393
+ ___block_literal_global.396
+ ___block_literal_global.404
+ ___block_literal_global.431
+ ___block_literal_global.545
+ ___block_literal_global.579
+ ___block_literal_global.584
+ ___block_literal_global.586
+ ___block_literal_global.588
+ ___block_literal_global.590
+ ___block_literal_global.618
+ ___block_literal_global.628
+ ___block_literal_global.649
+ ___block_literal_global.751
+ ___block_literal_global.753
+ ___block_literal_global.755
+ ___block_literal_global.757
+ ___block_literal_global.759
+ ___block_literal_global.761
+ ___block_literal_global.763
+ ___block_literal_global.765
+ ___block_literal_global.767
+ ___block_literal_global.769
+ ___block_literal_global.78
+ ___block_literal_global.8
+ ___block_literal_global.821
+ ___block_literal_global.827
+ ___block_literal_global.885
+ ___block_literal_global.978
+ ___bweia_monocularStillsPipelineForInferenceConfiguration_block_invoke
+ ___bwvdic_monocularVideoPipelineForNetworkDimensions_block_invoke
+ ___bwvdic_monocularVideoPipelineForNetworkDimensions_block_invoke.cold.1
+ ___bwvdic_monocularVideoPipelineForNetworkDimensions_block_invoke.cold.2
+ ___bwvdic_monocularVideoPipelineForNetworkDimensions_block_invoke.cold.3
+ ___captureSessionServer_configureCompositingSinkCallbackIfNecessary_block_invoke
+ ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.1367
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.1365
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.1361
+ ___captureSession_SetSectionProperty_block_invoke.1298
+ ___captureSession_createMultiCamClientCompositingCallback_block_invoke
+ ___captureSession_showCinematicFramingAlertIfApplicable_block_invoke.1203
+ ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1140
+ ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1144
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke.917
+ ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.918
+ ___captureSession_updateGraphConfiguration_block_invoke.728
+ ___captureSession_updateGraphConfiguration_block_invoke_2
+ ___captureSession_updateRunningCondition_block_invoke.688
+ ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1250
+ ___divti3
+ ___externalSyncDeviceDiscoverySession_postNotificationWithPayload_block_invoke
+ ___getADImageDimensionsClass_block_invoke
+ ___getADImageDimensionsClass_block_invoke.cold.1
+ ___getADMonocularStillsPipelineClass_block_invoke
+ ___getADMonocularStillsPipelineClass_block_invoke.cold.1
+ ___getADMonocularStillsPipelineParametersClass_block_invoke
+ ___getADMonocularStillsPipelineParametersClass_block_invoke.cold.1
+ ___getADMonocularVideoPipelineClass_block_invoke
+ ___getADMonocularVideoPipelineClass_block_invoke.cold.1
+ ___getADMonocularVideoPipelineParametersClass_block_invoke
+ ___getADMonocularVideoPipelineParametersClass_block_invoke.cold.1
+ ___multiStreamCameraSourceNode_outputSampleBuffer_block_invoke.1512
+ ___nrfp_createStateMachine_block_invoke_10
+ ___nrfp_createStateMachine_block_invoke_11
+ _bwdcc_learnedFusionErrorRecoveryPossible
+ _bweia_addRequirement_base
+ _bweia_addRequirement_cmm
+ _bweia_monocularStillsPipelineForInferenceConfiguration.sDescriptors
+ _bwvdic_monocularVideoPipelineForNetworkDimensions.sDescriptors
+ _captureSessionRemote_handleServerMessage
+ _captureSessionRemote_handleServerMessage.cold.1
+ _captureSessionRemote_handleServerMessage.cold.2
+ _captureSession_SetSectionProperty.onceToken.1299
+ _captureSession_buildGraphWithConfiguration.cold.30
+ _captureSession_commitInflightConfiguration.cold.10
+ _captureSession_commitInflightConfiguration.cold.5
+ _captureSession_commitInflightConfiguration.cold.6
+ _captureSession_commitInflightConfiguration.cold.7
+ _captureSession_commitInflightConfiguration.cold.8
+ _captureSession_commitInflightConfiguration.cold.9
+ _captureSession_createMultiCamClientCompositingCallback
+ _captureSession_liveReconfigureForOutputAspectRatioChange
+ _captureSession_updateGraphForCinematographyConfigurationChanges
+ _captureSession_updateGraphForCinematographyConfigurationChanges.cold.1
+ _captureSession_updateGraphForConnectionConfigurationEnabledChanges
+ _captureSession_updateGraphForMetadataConnectionConfigurationChanges
+ _captureSession_updateGraphForMetadataConnectionConfigurationChanges.cold.1
+ _captureSession_updateGraphForSourceConfigurationChanges
+ _captureSession_updateGraphForSourceConfigurationChanges.cold.1
+ _captureSession_updateGraphForStillImageSinkConfigurationChanges
+ _captureSession_updateGraphForStillImageSinkConfigurationChanges.cold.1
+ _captureSession_updateGraphForVideoDataSinkConfigurationChanges
+ _captureSession_updateGraphForVideoDataSinkConfigurationChanges.cold.1
+ _captureSourceServer_handleCopyExternalSyncDeviceDiscoverySessionSourceMessage
+ _captureSourceServer_handleCopyExternalSyncDeviceDiscoverySessionSourceMessage.cold.1
+ _captureSourceServer_handleCopyExternalSyncDeviceDiscoverySessionSourceMessage.cold.2
+ _captureSource_setPropertyInternal.cold.58
+ _captureSource_setPropertyInternal.cold.59
+ _cs_cameraSensorOrientationCompensationDegreesCW
+ _cs_configurePreviewStitcherNodeOutputTransformAndHistogramGeneration
+ _cs_pulseGeneratorFrameRate
+ _cs_rotateDepthMetadata
+ _cs_rotatePixelBuffer
+ _cs_rotatePixelBuffer.cold.1
+ _cs_rotatePixelBuffer.cold.2
+ _cs_rotatePixelBuffer.cold.3
+ _cs_rotatePixelBuffer.cold.4
+ _cs_rotatePixelBuffer.cold.5
+ _cs_rotatePixelBuffer.cold.6
+ _cs_shouldEnableLowLatencyStabilization
+ _cs_shouldSetCinematicFramingControlsWhileRunning
+ _csp_enableAdaptiveOverscanByVideoStabilizationMethods
+ _cspc_getMultiCamClientCompositingEnabledStates
+ _csr_addFlexRangeImageProperties
+ _csr_deserializeClientCompositingSampleBuffer
+ _csr_deserializeClientCompositingSampleBuffer.cold.1
+ _csr_deserializeClientCompositingSampleBuffer.cold.2
+ _csr_deserializeClientCompositingSampleBuffer.cold.3
+ _csr_deserializeClientCompositingSampleBuffer.cold.4
+ _csr_deserializeClientCompositingSampleBuffer.cold.5
+ _csr_serializeClientCompositingSampleBuffer
+ _externalSyncDeviceDiscoverySession_CopyDebugDescription
+ _externalSyncDeviceDiscoverySession_CopyProperty
+ _externalSyncDeviceDiscoverySession_Finalize
+ _externalSyncDeviceDiscoverySession_Invalidate
+ _externalSyncDeviceDiscoverySession_SetProperty
+ _gBWMultiCamClientCompositingNodeTrace
+ _gBWProResRawMetadataUtilities
+ _gBWSmartCropWarpingNodeTrace
+ _gBWSmartFramingPerceptionSinkNode
+ _gFigExternalSyncDeviceDiscoverySessionManagerTrace
+ _gFigPulseGeneratorTrace
+ _getADImageDimensionsClass
+ _getADImageDimensionsClass.softClass
+ _getADMonocularStillsPipelineClass
+ _getADMonocularStillsPipelineClass.softClass
+ _getADMonocularStillsPipelineParametersClass
+ _getADMonocularStillsPipelineParametersClass.softClass
+ _getADMonocularVideoPipelineClass
+ _getADMonocularVideoPipelineClass.softClass
+ _getADMonocularVideoPipelineParametersClass
+ _getADMonocularVideoPipelineParametersClass.softClass
+ _getColorTranslationMatrixFromCalibration
+ _getColorTranslationMatrixFromCalibration.CA_2800toD65
+ _invert3x3Matrix
+ _isSupported.result
+ _isSupported.sFigPulseGeneratorSupportedOnceToken
+ _kBWNodeSampleBufferAttachmentKey_ProResRawWhiteBalanceBlueFactor
+ _kBWNodeSampleBufferAttachmentKey_ProResRawWhiteBalanceRedFactor
+ _kBWNodeSampleBufferAttachmentKey_VideoGeometricDistortionCorrectionEnabled
+ _kBWProResRawPlanckianLocus
+ _kCFAllocatorSystemDefault
+ _kCIImageRepresentationISOGainMapAlternateHeadroom
+ _kCIImageRepresentationISOGainMapBaseHeadroom
+ _kCIImageRepresentationISOGainMapMax
+ _kCIImageRepresentationISOGainMapMin
+ _kCIImageRepresentationISOGainMapOffset
+ _kCMMetadataBaseDataType_RectF32
+ _kCMPhotoScaleAndRotateOption_SourceExifOrientation
+ _kCVImageBufferLogTransferFunction_AppleLog2
+ _kCVPixelBufferProResRAWKey_BlackLevel
+ _kCVPixelBufferProResRAWKey_ColorMatrix
+ _kCVPixelBufferProResRAWKey_GainFactor
+ _kCVPixelBufferProResRAWKey_MetadataExtension
+ _kCVPixelBufferProResRAWKey_RecommendedCrop
+ _kCVPixelBufferProResRAWKey_WhiteBalanceBlueFactor
+ _kCVPixelBufferProResRAWKey_WhiteBalanceCCT
+ _kCVPixelBufferProResRAWKey_WhiteBalanceRedFactor
+ _kCVPixelBufferProResRAWKey_WhiteLevel
+ _kFigAppleMakerNote_FrontAndBackCameraCompositionPictureInPictureRect
+ _kFigCaptureCameraInfoKey_ImageCircleRadius
+ _kFigCaptureFlatDictionaryAppleMakerNote_FrontAndBackCameraCompositionPictureInPictureRect
+ _kFigCaptureFlatDictionaryAppleMakerNote_FrontAndBackCameraCompositionPictureInPictureRect_opaque
+ _kFigCaptureFlatDictionaryAppleMakerNote_FrontAndBackCameraCompositionPictureInPictureRect_string
+ _kFigCaptureSampleBufferAttachmentKey_PrimaryPreviewSourceRectIsLandscape
+ _kFigCaptureSampleBufferMetadata_DetectedFacesArrayFilteredForCamGaze
+ _kFigCaptureSampleBufferMetadata_DetectedObjectsInfoFromSource
+ _kFigCaptureSampleBufferMetadata_FlexRangeImageProperties
+ _kFigCaptureSampleBufferMetadata_FlexRangeVersionTag
+ _kFigCaptureSampleBufferMetadata_FrontAndBackCameraCompositionPictureInPictureRect
+ _kFigCaptureSampleBufferMetadata_ImageCircle
+ _kFigCaptureSampleBufferMetadata_ImageCircleKey_Center
+ _kFigCaptureSampleBufferMetadata_ImageCircleKey_Radius
+ _kFigCaptureSampleBufferMetadata_SmartFramingConfiguredFieldOfView
+ _kFigCaptureSampleBufferMetadata_SmartFramingSuggestedFieldOfViewRectForSmartCrop
+ _kFigCaptureSessionMsgParam_SettingsID
+ _kFigCaptureSessionMsgParam_SinkID
+ _kFigCaptureSessionPreviewSinkPrimaryCaptureRectKey_SmartFramingTransitionPercentComplete
+ _kFigCaptureSessionPreviewSinkPrimaryCaptureRectKey_SmartFramingTransitionTargetFieldOfView
+ _kFigCaptureSessionVideoDataSinkProperty_MovieLevelMetadata
+ _kFigCaptureSinkClientCompositingCallback_OutputGainMapSampleBuffer_SerializedData
+ _kFigCaptureSinkClientCompositingCallback_OutputGainMapSampleBuffer_SerializedSurface
+ _kFigCaptureSinkClientCompositingCallback_OutputPTS
+ _kFigCaptureSinkClientCompositingCallback_OutputSampleBuffer_SerializedSurface
+ _kFigCaptureSinkClientCompositingCallback_PrimaryGainMapSampleBuffer_SerializedData
+ _kFigCaptureSinkClientCompositingCallback_PrimaryGainMapSampleBuffer_SerializedSurface
+ _kFigCaptureSinkClientCompositingCallback_PrimaryPTS
+ _kFigCaptureSinkClientCompositingCallback_PrimarySampleBuffer_SerializedSurface
+ _kFigCaptureSinkClientCompositingCallback_ReplyKey_CompositingMetadata
+ _kFigCaptureSinkClientCompositingCallback_SecondaryGainMapSampleBuffer_SerializedData
+ _kFigCaptureSinkClientCompositingCallback_SecondaryGainMapSampleBuffer_SerializedSurface
+ _kFigCaptureSinkClientCompositingCallback_SecondaryPTS
+ _kFigCaptureSinkClientCompositingCallback_SecondarySampleBuffer_SerializedSurface
+ _kFigCaptureSourceAttributeKeySmartFramingZoomFactorsByFieldOfViewKey_Landscape
+ _kFigCaptureSourceAttributeKeySmartFramingZoomFactorsByFieldOfViewKey_None
+ _kFigCaptureSourceAttributeKeySmartFramingZoomFactorsByFieldOfViewKey_Portrait
+ _kFigCaptureSourceAttributeKeySmartFramingZoomFactorsByFieldOfViewKey_ZoomedOutLandscape
+ _kFigCaptureSourceAttributeKeySmartFramingZoomFactorsByFieldOfViewKey_ZoomedOutPortrait
+ _kFigCaptureSourceAttributeKey_BaseZoomFactorOverridesByAspectRatio
+ _kFigCaptureSourceAttributeKey_CameraSensorOrientationCompensation
+ _kFigCaptureSourceAttributeKey_ExternalSyncMaxFrameRate
+ _kFigCaptureSourceAttributeKey_FaceAwareVideoStabilizationSupported
+ _kFigCaptureSourceAttributeKey_GeometricDistortionCorrectionForSmartCropEnabled
+ _kFigCaptureSourceAttributeKey_LearnedFusion
+ _kFigCaptureSourceAttributeKey_LockedFrameDurationMaxFrameRate
+ _kFigCaptureSourceAttributeKey_SensorOutputLargerThanImageCircle
+ _kFigCaptureSourceAttributeKey_SmartFramingZoomFactorsByFieldOfView
+ _kFigCaptureSourceExternalSyncDeviceDiscoverySessionProperty_CurrentExternalSyncDevices
+ _kFigCaptureSourceFrameDurationBoundsKey_FrameDurationMax
+ _kFigCaptureSourceFrameDurationBoundsKey_FrameDurationMin
+ _kFigCaptureSourceNotificationExternalSyncDeviceDiscoverySessionDevicesChangedPayloadKey_Firmware
+ _kFigCaptureSourceNotificationExternalSyncDeviceDiscoverySessionDevicesChangedPayloadKey_PID
+ _kFigCaptureSourceNotificationExternalSyncDeviceDiscoverySessionDevicesChangedPayloadKey_VID
+ _kFigCaptureSourceNotificationKey_DynamicAspectRatioRequestID
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_ClockID
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_Error
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_LockState
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_OutOfBounds
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_SessionStopped
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_State
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_Status
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_TriggerID
+ _kFigCaptureSourceNotificationPulseGeneratorStatusChangedPayloadKey_TriggerPreset
+ _kFigCaptureSourceNotification_ExternalSyncDeviceDiscoverySessionDevicesChanged
+ _kFigCaptureSourceNotification_LiveReconfigurationForDynamicAspectRatioComplete
+ _kFigCaptureSourceNotification_PulseGeneratorStatusChanged
+ _kFigCaptureSourceNotification_SmartFramingSuggestedFieldOfViewChanged
+ _kFigCaptureSourceProperty_EnabledSmartFramingFieldsOfView
+ _kFigCaptureSourceProperty_ExternalSyncDeviceSignalCompensationDelay
+ _kFigCaptureSourceProperty_FrameDurationBounds
+ _kFigCaptureSourceProperty_SmartFramingMonitorRunning
+ _kFigCaptureStreamAbsoluteColorCalibrationCCTKey_BGGain
+ _kFigCaptureStreamAbsoluteColorCalibrationCCTKey_RGGain
+ _kFigCaptureStreamAbsoluteColorCalibrationKey_HighCCT
+ _kFigCaptureStreamAbsoluteColorCalibrationKey_LowCCT
+ _kFigCaptureStreamDetectedObjectKey_GroupID
+ _kFigCaptureStreamMetadata_LensShadingModulationWeight
+ _kFigCaptureStreamMetadata_PostDemosaicGain
+ _kFigCaptureStreamMetadata_PreDemosaicGain
+ _kFigCaptureStreamMetadata_ProResRawTotalSensorCropRect
+ _kFigCaptureStreamMetadata_ProResRawValidBufferRect
+ _kFigCaptureStreamMetadata_TemporalHomographyMatrix
+ _kFigCaptureStreamProperty_ExternalSyncFrameRateRational
+ _kFigCaptureStreamProperty_FrameRateRangeRational
+ _kFigCaptureStreamProperty_MaximumFrameRateRational
+ _kFigCaptureStreamProperty_MinimumFrameRateRational
+ _kFigCaptureStreamVideoOutputID_ProResRaw
+ _kFigExternalSyncDeviceDiscoverySessionVTable
+ _kFigExternalSyncDeviceDiscoverySession_BaseClass
+ _kFigExternalSyncDeviceDiscoverySession_FigExternalSyncDeviceDiscoverySessionClass
+ _kFigMetadataIdentifier_QuickTimeMetadataFrontAndBackCameraCompositionPictureInPictureRect
+ _kFigQuickTimeMetadataKey_CameraISOSensitivity
+ _kFigQuickTimeMetadataKey_CameraLensIrisFNumber
+ _kFigQuickTimeMetadataKey_CameraShutterSpeedAngle
+ _kFigQuickTimeMetadataKey_CameraShutterSpeedTime
+ _kFigQuickTimeMetadataKey_CameraWhiteBalance
+ _kFigQuickTimeMetadataKey_WhiteBalanceByCCTColorMatrices
+ _kFigQuickTimeMetadataKey_WhiteBalanceByCCTWhiteBalanceFactors
+ _kFigQuicktimeMetadataKey_FrontAndBackCameraComposition
+ _kVTCompressionPictureInPictureRegion_BorderBottom
+ _kVTCompressionPictureInPictureRegion_BorderLeft
+ _kVTCompressionPictureInPictureRegion_BorderRight
+ _kVTCompressionPictureInPictureRegion_BorderTop
+ _kVTCompressionPictureInPictureRegion_Rectangle
+ _kVTCompressionPropertyKey_PictureInPictureRegion
+ _lnrpc_formatFromInputFormatsByResolutionFlavor.cold.4
+ _lnrpc_formatFromInputFormatsByResolutionFlavor.cold.5
+ _lnrpc_formatFromInputFormatsByResolutionFlavor.cold.6
+ _multiStreamCameraSourceNode_outputSampleBuffer.cold.13
+ _multiStreamCameraSourceNode_proresRawServiceQueueCallback
+ _objc_msgSend$_SSAMDeivceTerminatedService:
+ _objc_msgSend$_addDevice:
+ _objc_msgSend$_addMetadataInputsAndOutputsWithMetadataIdentifiers:
+ _objc_msgSend$_addVideoCaptureInputAndOutput
+ _objc_msgSend$_appendArray:withObject:restrictingLengthTo:
+ _objc_msgSend$_configureFollowSync:assertDur:offset:
+ _objc_msgSend$_configureLeaderSync:frameRate:assertDur:
+ _objc_msgSend$_createCalibrationDictionaryFromSampleBuffer:
+ _objc_msgSend$_currentDevices
+ _objc_msgSend$_disciplineMSGTimeSyncClock:
+ _objc_msgSend$_followSyncConfig:config:
+ _objc_msgSend$_followSyncInit:leader:trigger:
+ _objc_msgSend$_forceNotifyDelegatesDevicesChanged
+ _objc_msgSend$_getMotionScoreUsingLargestFaceTrack:
+ _objc_msgSend$_getOrCreateTimeSyncMSGClockIdentifier:tsClockIdentifierOut:
+ _objc_msgSend$_getTimeSyncClock:clockOut:
+ _objc_msgSend$_handleDeviceEvent:
+ _objc_msgSend$_initRTSCProcessor
+ _objc_msgSend$_initRTSCProcessorWithOutputDimensions:
+ _objc_msgSend$_initVMRefinerInference:
+ _objc_msgSend$_isSampleBufferFromPrimaryStream:metadataDict:
+ _objc_msgSend$_leaderSyncConfig:config:
+ _objc_msgSend$_leaderSyncInit:trigger:
+ _objc_msgSend$_loadAndConfigureSmartStyleBundle:
+ _objc_msgSend$_notifyDelegate:withError:
+ _objc_msgSend$_popHomography
+ _objc_msgSend$_pushHomography:pts:
+ _objc_msgSend$_removeDevice:
+ _objc_msgSend$_replaceAttachedSampleBuffer:attachedMediaKey:primarySampleBuffer:aspectRatio:
+ _objc_msgSend$_resetMsgSyncs
+ _objc_msgSend$_resetState
+ _objc_msgSend$_setSSAMPortEnabled:
+ _objc_msgSend$_setupDeviceDeviceManagmentMonitoring
+ _objc_msgSend$_setupDeviceObservationNotifications
+ _objc_msgSend$_setupSSAMInterestNotification
+ _objc_msgSend$_startSync:
+ _objc_msgSend$_startSyncs:
+ _objc_msgSend$_supportedInputPixelFormats
+ _objc_msgSend$_supportedOutputPixelFormats
+ _objc_msgSend$_syncInterruptDisable:
+ _objc_msgSend$_syncInterruptEnable:
+ _objc_msgSend$_syncReset:
+ _objc_msgSend$_teardownDeviceDeviceManagmentMonitoring
+ _objc_msgSend$_teardownDeviceObservationNotifications
+ _objc_msgSend$_teardownSSAMInterestNotification
+ _objc_msgSend$_updateDetectedObjectsInfo:
+ _objc_msgSend$_updateGazeStatesUsingGazeProbabilitiesData:gazeConfidenceFilteredOut:gazeScoreFilteredOut:
+ _objc_msgSend$_updateOutputRequirements
+ _objc_msgSend$_waitForInferenceToComplete
+ _objc_msgSend$activeAspectRatio
+ _objc_msgSend$activeVideoExternalSyncFrameRate
+ _objc_msgSend$activeVideoLockedFrameRate
+ _objc_msgSend$adaptiveSensorCropForDynamicAspectRatioEnabled
+ _objc_msgSend$addPrimaryBuffer:
+ _objc_msgSend$addSecondaryBuffer:
+ _objc_msgSend$anyCaptureSourceSupportsMSG
+ _objc_msgSend$appendData:
+ _objc_msgSend$applySignalCompensationDelay:
+ _objc_msgSend$attemptErrorRecoveryOutput
+ _objc_msgSend$baseZoomFactorOverridesByAspectRatio
+ _objc_msgSend$cameraSensorOrientationCompensationDegreesCW
+ _objc_msgSend$cameraSensorOrientationCompensationEnabled
+ _objc_msgSend$candidateFramingCropRects
+ _objc_msgSend$colorFeaturesDimensions
+ _objc_msgSend$colorFeaturesPixelFormat
+ _objc_msgSend$colorInputRotationChangesWithAspectRatio
+ _objc_msgSend$compositionPictureInPictureRectMetadataOutput
+ _objc_msgSend$connectToSecondaryMultiCameraClientCompositingPipeline:
+ _objc_msgSend$currentDevices
+ _objc_msgSend$depthValueInputPixelBuffer:bias:scaleFactor:
+ _objc_msgSend$detectionMetadataInput
+ _objc_msgSend$deviceDisconnectedEvent:
+ _objc_msgSend$disparityMultiplierFormat
+ _objc_msgSend$dockedTrackingActive
+ _objc_msgSend$dynamicAspectRatioEnabled
+ _objc_msgSend$evMinusOutput
+ _objc_msgSend$evZeroOutput
+ _objc_msgSend$externalSyncDeviceDeviceIdentifer
+ _objc_msgSend$externalSyncDeviceDiscoverySessionManager:connectedDevicesDidChange:
+ _objc_msgSend$externalSyncFrameRate
+ _objc_msgSend$faceStabilizationEnabled
+ _objc_msgSend$faceStabilizationSigmaMultiplierForBiasTracking
+ _objc_msgSend$faceStabilizationSigmaMultiplierForFaceFiltering
+ _objc_msgSend$forceCleanup
+ _objc_msgSend$fudgedBaseZoomFactorForAspectRatio:
+ _objc_msgSend$fusionModeOutput
+ _objc_msgSend$gatingInput
+ _objc_msgSend$getDefaultProcessorConfigurationForStills3x4
+ _objc_msgSend$getDefaultProcessorConfigurationForStillsReversibility3x4
+ _objc_msgSend$getDefaultProcessorConfigurationForStreamingAcceleratedSquareAspectRatio
+ _objc_msgSend$getDefaultProcessorConfigurationForStreamingSquareAspectRatio
+ _objc_msgSend$getDefaultProcessorConfigurationForStreamingSquareAspectRatioWithFilterType:
+ _objc_msgSend$getDeviceInfoDict
+ _objc_msgSend$getMetricScaleFactorForEFL:
+ _objc_msgSend$getMonocularDepthScaleFactor:inputImageIsRotated:
+ _objc_msgSend$getSynchronizedBufferPair
+ _objc_msgSend$getValidRadiusAfterGDCInImageCoord
+ _objc_msgSend$getValidRadiusInImageCoord
+ _objc_msgSend$hasCaptureFrameInfoWithMainFlags:sifrFlags:
+ _objc_msgSend$hdrErrorRecoveryEVZeroInput
+ _objc_msgSend$headPipeline
+ _objc_msgSend$horizontalFieldOfViewForAspectRatio:
+ _objc_msgSend$imageDimensionsWithWidth:height:
+ _objc_msgSend$initWithBasePoolCapacity:
+ _objc_msgSend$initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:
+ _objc_msgSend$initWithCaptureDevice:commandQueue:smartStyleRenderingEnabled:squareAspectRatioConfigEnabled:
+ _objc_msgSend$initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:smartStyleRenderingEnabled:portraitPreviewForegroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:sourceStillImageOutputPortTypes:squareAspectRatioConfigEnabled:cropDepthToPrimaryCaptureAspectRatio:disableDepthAndSegmentationRotationInLandscape:
+ _objc_msgSend$initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:secondaryStreamingPersonSegmentationEnabled:cropDepthToPrimaryCaptureAspectRatio:disableDepthAndSegmentationRotationInLandscape:
+ _objc_msgSend$initWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:isPrimaryStillImagePipeline:graph:name:
+ _objc_msgSend$initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:multiCamClientCompositingCallback:workgroup:
+ _objc_msgSend$initWithDynamicFieldOfViewRectsEnabled:
+ _objc_msgSend$initWithFaceGroupID:signficanceDetectionThreshold:
+ _objc_msgSend$initWithHpmEntID:ssamEntID:connectionState:vid:pid:
+ _objc_msgSend$initWithIndexOfInputProvidingOutputSampleBuffer:compositingStrategy:gainMapSupported:clientCompositingCallback:
+ _objc_msgSend$initWithMetalCommandQueue:renderingMethod:squareAspectRatioConfigEnabled:
+ _objc_msgSend$initWithMetalCommandQueue:squareAspectRatioConfigEnabled:
+ _objc_msgSend$initWithName:stillImageSettings:nodeConfiguration:provideInferenceInputImageForProcessing:addSyncErrorRecoveryPorts:portType:delegate:
+ _objc_msgSend$initWithNumber:
+ _objc_msgSend$initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:smartFramingEnabled:irisRequestDelegate:inferenceScheduler:
+ _objc_msgSend$initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxLossyCompressionLevel:cameraExtrinsicMatrix:processingMode:stillCaptureEnabled:objectMetadataIdentifiers:captureDevice:
+ _objc_msgSend$initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:
+ _objc_msgSend$initWithPortType:sensorIDString:
+ _objc_msgSend$initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:videoGreenGhostOfflineMetadataEnabled:videoGreenGhostOfflineLightSourceMaskEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:systemIsUnderCriticalThermalPressure:faceAwareVideoStabilizationEnabled:
+ _objc_msgSend$initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:inputFormatIsProResRaw:errorOut:
+ _objc_msgSend$initWithSession:andNodeMetadataOutput:usePIPAIngestSignalingDomain:completionHandler:
+ _objc_msgSend$initWithSinkID:captureDevice:inferenceScheduler:
+ _objc_msgSend$initWithStitchingDisabledAndZoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:
+ _objc_msgSend$isDigitalFlashZeroShutterLagSupported
+ _objc_msgSend$isDynamicAspectRatioSupported
+ _objc_msgSend$isExternalSyncDevicePulse
+ _objc_msgSend$isLearnedFusionSupported
+ _objc_msgSend$isLearnedHRNRSupported
+ _objc_msgSend$isPersistentlySignificant
+ _objc_msgSend$isSSAMEnabled
+ _objc_msgSend$isSmartCropSupported
+ _objc_msgSend$isSmartFramingEnabled
+ _objc_msgSend$isSmartFramingSupported
+ _objc_msgSend$isStillImageOutputDownscaledInHWISP
+ _objc_msgSend$isSupported
+ _objc_msgSend$kV5XTriggerID
+ _objc_msgSend$keysSortedByValueUsingComparator:
+ _objc_msgSend$landscapeCropOutputFormat
+ _objc_msgSend$learnedFusionEnabled
+ _objc_msgSend$learnedFusionInputFormat
+ _objc_msgSend$learnedFusionSupportedForPortType:
+ _objc_msgSend$learnedHRNRSupported
+ _objc_msgSend$liveReconfigureForAspectRatio:
+ _objc_msgSend$liveReconfigureForOutputAspectRatioCompleted:
+ _objc_msgSend$liveReconfigureForOutputAspectRatioFirstBufferReceived:forConfigurationID:
+ _objc_msgSend$liveReconfigureForOutputAspectRatioStarted:forConfigurationID:
+ _objc_msgSend$liveReconfigureForOutputDimensions:
+ _objc_msgSend$loadMonocularVideoPipeline
+ _objc_msgSend$lockedFrameRate
+ _objc_msgSend$longOutput
+ _objc_msgSend$monocularStreamingDepthType
+ _objc_msgSend$monocularVideoInferenceDescriptor
+ _objc_msgSend$multiCamClientCompositingEnabled
+ _objc_msgSend$multiCamClientCompositingPrimaryCameraVideoStabilizationStrength
+ _objc_msgSend$multiCamClientCompositingPrimaryConnectionID
+ _objc_msgSend$outputAspectRatio
+ _objc_msgSend$outputAspectRatioRequestID
+ _objc_msgSend$outputCameraIntrinsic
+ _objc_msgSend$outputScale
+ _objc_msgSend$portTypesWithDigitalFlashZeroShutterLagEnabled
+ _objc_msgSend$portTypesWithLearnedFusionEnabled
+ _objc_msgSend$portraitCropOutputFormat
+ _objc_msgSend$prepareForReconfigurationWithInputAspectRatio:
+ _objc_msgSend$previewDimensionsForAspectRatio:
+ _objc_msgSend$previewScalingFactorWithDisparityBuffer:sbuf:
+ _objc_msgSend$previewStitcherSmartFramingFieldOfViewTransitionAppliedZoomFactor:zoomFactor:
+ _objc_msgSend$primarySbufInputs
+ _objc_msgSend$proResRawAugmentedMovieLevelMetadataWithMovieLevelMetadata:
+ _objc_msgSend$proResRawCaptureEnabled
+ _objc_msgSend$pulseGenerator:updateSynchronizationClock:withError:
+ _objc_msgSend$pulseGenerator:updatedTriggerID:withLockState:
+ _objc_msgSend$pulseGenerator:updatedTriggerID:withOutOfBoundsError:
+ _objc_msgSend$pulseGenerator:updatedTriggerID:withSessionStoppedExitStatus:
+ _objc_msgSend$pulseGenerator:updatedTriggerID:withTriggerIsPresent:
+ _objc_msgSend$pulseGeneratorFrameRate
+ _objc_msgSend$referenceFrameAttachments
+ _objc_msgSend$registerClient:delegate:
+ _objc_msgSend$renderMetadataSampleBuffer:forInput:
+ _objc_msgSend$renderVideoSampleBuffer:forInput:
+ _objc_msgSend$renderingHomography
+ _objc_msgSend$resetSmartFramingSceneMonitor
+ _objc_msgSend$resolveSuggestedFieldOfViewRectWithSampleBuffer:fromFieldOfViewRects:suggestedFieldOfViewRectOut:
+ _objc_msgSend$resolveSuggestedFieldOfViewWithSampleBuffer:suggestedFieldOfViewOut:
+ _objc_msgSend$rtscProcessor
+ _objc_msgSend$scalerNode
+ _objc_msgSend$secondEvZeroOutput
+ _objc_msgSend$sensorOrientationByPortType
+ _objc_msgSend$sensorOutputLargerThanImageCircle
+ _objc_msgSend$setActiveAspectRatio:
+ _objc_msgSend$setActiveVideoLockedFrameRate:activeVideoExternalSyncFrameRate:
+ _objc_msgSend$setActiveVideoMinFrameDuration:activeVideoMaxFrameDuration:
+ _objc_msgSend$setAdaptiveSensorCropForDynamicAspectRatioEnabled:
+ _objc_msgSend$setBaseZoomFactorOverridesByAspectRatio:
+ _objc_msgSend$setCameraSensorOrientationCompensationDegreesCW:
+ _objc_msgSend$setCameraSensorOrientationCompensationEnabled:
+ _objc_msgSend$setColorInputRotationChangesWithAspectRatio:
+ _objc_msgSend$setConfiguresStreamingImageIntentForActionCamera:
+ _objc_msgSend$setDigitalFlashZeroShutterLagEnabled:
+ _objc_msgSend$setDynamicAspectRatioEnabled:
+ _objc_msgSend$setEnableFaceReframing:
+ _objc_msgSend$setExternalSyncFrameRate:
+ _objc_msgSend$setFaceStabilizationEnabled:
+ _objc_msgSend$setFaceStabilizationSigmaMultiplierForBiasTracking:
+ _objc_msgSend$setFaceStabilizationSigmaMultiplierForFaceFiltering:
+ _objc_msgSend$setFrontRearSimultaneousVideoRecording:
+ _objc_msgSend$setInFrameMixMode:
+ _objc_msgSend$setInputCalibrationData:
+ _objc_msgSend$setInputPTS:
+ _objc_msgSend$setIrisVISCleanOutputRect:
+ _objc_msgSend$setLandscapeCropOutputFormat:
+ _objc_msgSend$setLearnedFusionEnabled:
+ _objc_msgSend$setLearnedFusionInputFormat:
+ _objc_msgSend$setLearnedFusionProxyGenerationUsedEVMinus:
+ _objc_msgSend$setLearnedHRNRSupported:
+ _objc_msgSend$setLegacySensorOrientationRotationDegrees:
+ _objc_msgSend$setLockedFrameRate:
+ _objc_msgSend$setMsgClock:
+ _objc_msgSend$setMultiCamClientCompositingEnabled:
+ _objc_msgSend$setMultiCamClientCompositingPrimaryCameraVideoStabilizationStrength:
+ _objc_msgSend$setMultiCamClientCompositingPrimaryConnectionID:
+ _objc_msgSend$setOutputAspectRatio:
+ _objc_msgSend$setOutputAspectRatioRequestID:
+ _objc_msgSend$setOutputFOVPreset:
+ _objc_msgSend$setPortTypesWithDigitalFlashZeroShutterLagEnabled:
+ _objc_msgSend$setPortTypesWithLearnedFusionEnabled:
+ _objc_msgSend$setPortraitCropOutputFormat:
+ _objc_msgSend$setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:fencePortSendRight:uniqueID:
+ _objc_msgSend$setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:trueVideoTransitionReferenceSampleBuffer:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:fencePortSendRight:
+ _objc_msgSend$setProResRawCaptureEnabled:
+ _objc_msgSend$setProcessSmartStyleRenderingInput:
+ _objc_msgSend$setQuantizationFrameDuration:
+ _objc_msgSend$setReferenceFrameAttachments:
+ _objc_msgSend$setRenderingHomography:
+ _objc_msgSend$setRequestedDimensions:
+ _objc_msgSend$setRtscProcessor:
+ _objc_msgSend$setScalingAppliesCropOnInputResolution:
+ _objc_msgSend$setSecondaryStreamComplete:
+ _objc_msgSend$setSensorOutputLargerThanImageCircle:
+ _objc_msgSend$setSmartCropCandidateFramingRects:
+ _objc_msgSend$setSmartCropSupported:
+ _objc_msgSend$setSmartCropWarpingOutputDimensions:
+ _objc_msgSend$setSmartCropWarpingRequired:
+ _objc_msgSend$setSmartFramingCamGazeProbabilitiesByFaceGroupID:
+ _objc_msgSend$setSmartFramingEnabled:
+ _objc_msgSend$setSmartFramingEnabledFieldsOfView:
+ _objc_msgSend$setSmartFramingFieldOfViewRects:
+ _objc_msgSend$setSmartFramingIsMonitoringScene:
+ _objc_msgSend$setSmartFramingRequiresSceneMonitoring:
+ _objc_msgSend$setSquareCropOutputFormat:
+ _objc_msgSend$setStillImageOutputDimensionsOverride:
+ _objc_msgSend$setSushiRawDimensions:
+ _objc_msgSend$setVisOverscanByAspectRatio:
+ _objc_msgSend$setZoomOutForMultiSubjects:
+ _objc_msgSend$sharedFigExternalSyncDeviceDiscoverySessionManager
+ _objc_msgSend$sharedFigPulseGenerator
+ _objc_msgSend$shouldGraphLiveReconfigurationWait
+ _objc_msgSend$smartCropFormat
+ _objc_msgSend$smartCropHomographyDataForPTS:
+ _objc_msgSend$smartCropNode
+ _objc_msgSend$smartCropOutputDimensions
+ _objc_msgSend$smartCropSupported
+ _objc_msgSend$smartCropWarpingOutputDimensions
+ _objc_msgSend$smartCropWarpingRequired
+ _objc_msgSend$smartFramingConfiguredFieldOfView
+ _objc_msgSend$smartFramingEnabled
+ _objc_msgSend$smartFramingIsMonitoringScene
+ _objc_msgSend$smartFramingRequiresSceneMonitoring
+ _objc_msgSend$smartFramingZoomFactorsByFieldOfView
+ _objc_msgSend$squareCropOutputFormat
+ _objc_msgSend$startWithFrameRate:cmClock:clientAudioClockDeviceUIDOut:externalSync:
+ _objc_msgSend$stillImageCoordinator:updateSettingsAfterLiveReconfiguration:
+ _objc_msgSend$stillImageScalingFactorWithDisparityBuffer:sbuf:scaleFactorFromEFL:
+ _objc_msgSend$stopRunning
+ _objc_msgSend$supportedDimensions
+ _objc_msgSend$unregisterAndCleanupClient:
+ _objc_msgSend$updateForLearnedFusionMissingEVMinus:missingHDRErrorRecoveryEVZero:
+ _objc_msgSend$updateMetadataFromSampleBuffer:withCameraInfo:
+ _objc_msgSend$updateSmartFramingCamGazeProbabilities:
+ _objc_msgSend$updateStatesIfNeededUsingFaceRect:faceSize:gazeProbabilitiesData:largestFaceTrack:largestFaceSize:totalDetectedFaceCount:currentPTS:isSignificantOut:
+ _objc_msgSend$updateStereoAudioCapturePairedCameraBaseFieldOfView:zoomFactor:
+ _objc_msgSend$visOverscanByAspectRatio
+ _objc_msgSend$willLiveReconfigureGraph
+ _pg_lockLostCallback
+ _pg_outOfBoundsCallback
+ _pg_sessionStoppedCallback
+ _pg_triggerPresentCallback
+ _prrmu_appendPSIMData
+ _prrmu_createWhiteBalanceFactorsFromCalibrations.wbFactorCCTs
+ _psn_limitRectWithinImageCircle
+ _psp_rotationAngleForStreamingFilterInferences
+ _qtmfsn_movieRecordingIsProResRaw
+ _sDeviceUsesDepthMultiplier
+ _sSSAMDeviceChangeHandler
+ _sSSAMDeviceFoundCallback
+ _setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:trueVideoTransitionReferenceSampleBuffer:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:fencePortSendRight:.trueVideoTransitionExitObservedForSignpost
+ _sfsm_computeStandardDeviation
+ _sfsm_unpackFaceRectAndAdjustWithExpansionScaleFactor
+ _sharedFigExternalSyncDeviceDiscoverySessionManager.onceToken
+ _sharedFigExternalSyncDeviceDiscoverySessionManager.sFigExternalSyncDeviceDiscoverySessionManager
+ _sharedFigPulseGenerator.sFigPulseGenerator
+ _sharedFigPulseGenerator.sFigPulseGeneratorOnceToken
+ _simu_createWarpRectilinearDictionary
+ _simu_oisAdjustedOpticalCenter
+ _vp_irisVISCleanOutputRectForOutputDimensions
+ _writeMatrixArrayRefDataEntry
+ _xpc_dictionary_get_remote_connection
- -[AudioRemixSubscriber initWithSession:andNodeMetadataOutput:completionHandler:]
- -[BWIrisStagingNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:inferenceScheduler:]
- -[BWMotionAttachmentsNode initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:errorOut:]
- -[BWMotionAttachmentsNode initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:errorOut:].cold.1
- -[BWOverCaptureSmartStyleApplyNode _loadAndConfigureSmartStyleBundle]
- -[BWOverCaptureSmartStyleApplyNode _loadAndConfigureSmartStyleBundle].cold.1
- -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:]
- -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:].cold.1
- -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:].cold.2
- -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:].cold.3
- -[BWOverCaptureSmartStyleApplyNode initWithMetalCommandQueue:].cold.4
- -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:]
- -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:].cold.1
- -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:].cold.2
- -[BWPreviewStitcherNode initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:].cold.3
- -[BWPreviewStitcherNode initWithStitchingDisabledAndZoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:]
- -[BWPreviewStitcherNode setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:trueVideoTransitionReferenceSampleBuffer:fencePortSendRight:]
- -[BWSmartStyleApplyNode _loadAndConfigureSmartStyleBundle]
- -[BWSmartStyleApplyNode _loadAndConfigureSmartStyleBundle].cold.1
- -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:]
- -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:].cold.1
- -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:].cold.2
- -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:].cold.3
- -[BWSmartStyleApplyNode initWithMetalCommandQueue:renderingMethod:].cold.4
- -[BWSmartStyleLearningNode _initVMRefinerInference]
- -[BWSmartStyleLearningNode _initVMRefinerInference].cold.1
- -[BWSmartStyleLearningNode _initVMRefinerInference].cold.2
- -[BWSmartStyleLearningNode _initVMRefinerInference].cold.3
- -[BWSmartStyleLearningNode _initVMRefinerInference].cold.4
- -[BWSmartStyleLearningNode _initVMRefinerInference].cold.5
- -[BWSmartStyleLearningNode _loadAndConfigureSmartStyleBundle]
- -[BWSmartStyleLearningNode _loadAndConfigureSmartStyleBundle].cold.1
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:]
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.1
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.10
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.11
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.2
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.3
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.4
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.5
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.6
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.7
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.8
- -[BWSmartStyleLearningNode initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:].cold.9
- -[BWStreamingCVAFilterRenderer initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:secondaryStreamingPersonSegmentationEnabled:cropDepthToPrimaryCaptureAspectRatio:]
- -[BWStreamingFilterNode initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:smartStyleRenderingEnabled:portraitPreviewForegroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:sourceStillImageOutputPortTypes:cropDepthToPrimaryCaptureAspectRatio:]
- -[BWStreamingRaytracingSDOFRenderer _loadAndConfigureSmartStyleBundle]
- -[BWStreamingRaytracingSDOFRenderer initWithCaptureDevice:commandQueue:smartStyleRenderingEnabled:]
- -[BWVISNode initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:videoGreenGhostOfflineMetadataEnabled:videoGreenGhostOfflineLightSourceMaskEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:systemIsUnderCriticalThermalPressure:]
- -[FigCaptureMovieFileSinkPipeline initWithConfiguration:videoSourceCaptureOutputsByConnectionID:audioSourceCaptureOutput:audioSourceCinematicAudioCaptureOutput:smartCameraInferenceOutput:detectedObjectBoxedMetadataOutputs:objectDetectionSourceOutput:metadataSourcePipelineOutputs:graph:name:inferenceScheduler:captureDevicesByConnectionID:audioSourceDelegate:fileCoordinatorStatusDelegate:recordingStatusDelegate:irisRequestDelegate:masterClock:delayedCompressorCleanupEnabled:]
- -[FigCaptureMovieFileSinkTailPipeline _buildMovieFileSinkTailPipeline:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:workgroup:]
- -[FigCaptureMovieFileSinkTailPipeline initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:workgroup:]
- -[FigCaptureMovieFileSinkTailPipeline initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:workgroup:].cold.1
- -[FigCapturePhotonicEngineSinkPipeline _buildScaleAndEncodeSubPipelineWithPipelineStage:graph:nodeConfiguration:stillImageSinkPipelineWithConfiguration:sensorConfigurationsByPortType:supportsScaling:deferredPearlDepthProcessingEnabled:provideMeteorHeadroom:provideFlexGTC:providePostEncodeInferences:semanticDevelopmentVersion:constituentPhotoDeliveryEnabled:demosaicedRawEnabled:nonPropagatedMainImageDownscalingFactorByAttachedMediaKey:propagatedMainImageDownscalingFactorByAttachedMediaKey:scalingMainImageDownscalingFactorByAttachedMediaKey:inferenceScheduler:subPipelineInputOut:subPipelineOutputOut:cameraSupportsFlash:cinematicFramingStatesProvider:photoEncoderControllerOut:]
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.1
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.10
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.100
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.101
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.102
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.103
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.104
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.105
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.106
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.107
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.108
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.109
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.11
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.110
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.111
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.112
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.113
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.114
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.115
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.116
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.117
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.118
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.119
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.12
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.13
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.14
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.15
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.16
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.17
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.18
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.19
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.2
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.20
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.21
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.22
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.23
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.24
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.25
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.26
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.27
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.28
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.29
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.3
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.30
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.31
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.32
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.33
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.34
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.35
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.36
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.37
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.38
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.39
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.4
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.40
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.41
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.42
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.43
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.44
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.45
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.46
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.47
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.48
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.49
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.5
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.50
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.51
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.52
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.53
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.54
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.55
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.56
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.57
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.58
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.59
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.6
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.60
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.61
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.62
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.63
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.64
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.65
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.66
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.67
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.68
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.69
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.7
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.70
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.71
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.72
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.73
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.74
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.75
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.76
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.77
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.78
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.79
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.8
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.80
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.81
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.82
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.83
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.84
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.85
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.86
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.87
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.88
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.89
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.9
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.90
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.91
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.92
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.93
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.94
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.95
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.96
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.97
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.98
- -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.99
- -[FigCapturePhotonicEngineSinkPipeline initWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:name:]
- -[FigCapturePhotonicEngineSinkPipeline initWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:name:].cold.1
- -[FigCapturePreviewSinkPipeline setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:fencePortSendRight:uniqueID:]
- GCC_except_table112
- GCC_except_table116
- GCC_except_table128
- GCC_except_table130
- GCC_except_table144
- GCC_except_table157
- GCC_except_table165
- GCC_except_table177
- GCC_except_table183
- GCC_except_table194
- GCC_except_table217
- GCC_except_table258
- GCC_except_table261
- GCC_except_table300
- GCC_except_table306
- GCC_except_table308
- GCC_except_table343
- GCC_except_table344
- GCC_except_table345
- GCC_except_table365
- GCC_except_table381
- GCC_except_table407
- GCC_except_table449
- GCC_except_table493
- GCC_except_table494
- GCC_except_table499
- GCC_except_table502
- GCC_except_table504
- GCC_except_table506
- GCC_except_table58
- GCC_except_table618
- GCC_except_table79
- GCC_except_table83
- GCC_except_table88
- GCC_except_table94
- GCC_except_table97
- _.compoundliteral.23
- _.compoundliteral.28
- _.compoundliteral.29
- _.compoundliteral.31
- _.compoundliteral.34
- _.compoundliteral.48
- _.compoundliteral.49
- _.compoundliteral.52
- _.compoundliteral.53
- _.compoundliteral.54
- _.compoundliteral.55
- _.compoundliteral.64
- _.compoundliteral.65
- _.compoundliteral.68
- _.compoundliteral.69
- _.compoundliteral.70
- _.compoundliteral.71
- _.compoundliteral.72
- _.compoundliteral.73
- _.compoundliteral.74
- _.compoundliteral.75
- _BWFigVideoCaptureDeviceNotificationPortTypeKey_block_invoke.sHasReportedInvalidOrientation
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.702
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.712
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke_2.703
- ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.143
- ___107-[BWFigCaptureSession stillImageCoordinator:didCancelMomentCaptureForSettingsID:streamingDisruptionEndPTS:]_block_invoke.95
- ___107-[BWFigCaptureSession stillImageCoordinator:didCancelMomentCaptureForSettingsID:streamingDisruptionEndPTS:]_block_invoke.99
- ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.654
- ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.654.cold.1
- ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.674
- ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.674.cold.1
- ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.674.cold.2
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.1053
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.722
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.897
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke_2
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke_2.1083
- ___360-[BWStreamingCVAFilterRenderer initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:secondaryStreamingPersonSegmentationEnabled:cropDepthToPrimaryCaptureAspectRatio:]_block_invoke
- ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.356
- ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke_2.359
- ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.333
- ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.336
- ___53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.1017
- ___53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.1017.cold.1
- ___53-[BWMultiStreamCameraSourceNode _bringStreamUpToDate]_block_invoke.1017.cold.2
- ___73-[BWPhotonicEngineNode _handleClientBracketFrameEmissionForSampleBuffer:]_block_invoke.412
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.580
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.580.cold.1
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.581
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.581.cold.1
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.581.cold.2
- ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.572
- ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.572.cold.1
- ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.623
- ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.623.cold.1
- ___block_literal_global.1149
- ___block_literal_global.1162
- ___block_literal_global.1199
- ___block_literal_global.1202
- ___block_literal_global.1210
- ___block_literal_global.1221
- ___block_literal_global.1231
- ___block_literal_global.1234
- ___block_literal_global.1257
- ___block_literal_global.1259
- ___block_literal_global.192
- ___block_literal_global.206
- ___block_literal_global.219
- ___block_literal_global.221
- ___block_literal_global.225
- ___block_literal_global.259
- ___block_literal_global.269
- ___block_literal_global.291
- ___block_literal_global.292
- ___block_literal_global.315
- ___block_literal_global.330
- ___block_literal_global.358
- ___block_literal_global.361
- ___block_literal_global.369
- ___block_literal_global.380
- ___block_literal_global.384
- ___block_literal_global.4
- ___block_literal_global.537
- ___block_literal_global.539
- ___block_literal_global.541
- ___block_literal_global.542
- ___block_literal_global.543
- ___block_literal_global.576
- ___block_literal_global.606
- ___block_literal_global.638
- ___block_literal_global.712
- ___block_literal_global.714
- ___block_literal_global.716
- ___block_literal_global.718
- ___block_literal_global.720
- ___block_literal_global.722
- ___block_literal_global.724
- ___block_literal_global.726
- ___block_literal_global.75
- ___block_literal_global.779
- ___block_literal_global.811
- ___block_literal_global.864
- ___block_literal_global.93
- ___block_literal_global.938
- ___block_literal_global.98
- ___block_literal_global.998
- ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.1297
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.1295
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.1291
- ___captureSession_SetSectionProperty_block_invoke.1228
- ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1068
- ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1072
- ___captureSession_startObservingForAudiomxdDeath_block_invoke.876
- ___captureSession_startObservingForAudiomxdDeath_block_invoke_2.877
- ___captureSession_updateRunningCondition_block_invoke.677
- ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1180
- _bweia_addRequirement
- _captureSession_SetSectionProperty.onceToken.1229
- _captureSession_updateGraphConfiguration
- _captureSession_updateGraphConfiguration.cold.1
- _captureSession_updateGraphConfiguration.cold.10
- _captureSession_updateGraphConfiguration.cold.11
- _captureSession_updateGraphConfiguration.cold.2
- _captureSession_updateGraphConfiguration.cold.3
- _captureSession_updateGraphConfiguration.cold.4
- _captureSession_updateGraphConfiguration.cold.5
- _captureSession_updateGraphConfiguration.cold.6
- _captureSession_updateGraphConfiguration.cold.7
- _captureSession_updateGraphConfiguration.cold.8
- _captureSession_updateGraphConfiguration.cold.9
- _objc_msgSend$_initVMRefinerInference
- _objc_msgSend$_loadAndConfigureSmartStyleBundle
- _objc_msgSend$initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:
- _objc_msgSend$initWithCaptureDevice:commandQueue:smartStyleRenderingEnabled:
- _objc_msgSend$initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:smartStyleRenderingEnabled:portraitPreviewForegroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:sourceStillImageOutputPortTypes:cropDepthToPrimaryCaptureAspectRatio:
- _objc_msgSend$initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:secondaryStreamingPersonSegmentationEnabled:cropDepthToPrimaryCaptureAspectRatio:
- _objc_msgSend$initWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:name:
- _objc_msgSend$initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:workgroup:
- _objc_msgSend$initWithMetalCommandQueue:renderingMethod:
- _objc_msgSend$initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:inferenceScheduler:
- _objc_msgSend$initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:
- _objc_msgSend$initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:videoGreenGhostOfflineMetadataEnabled:videoGreenGhostOfflineLightSourceMaskEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:systemIsUnderCriticalThermalPressure:
- _objc_msgSend$initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:errorOut:
- _objc_msgSend$initWithSession:andNodeMetadataOutput:completionHandler:
- _objc_msgSend$initWithStitchingDisabledAndZoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:
- _objc_msgSend$setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:fencePortSendRight:uniqueID:
- _objc_msgSend$setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:trueVideoTransitionReferenceSampleBuffer:fencePortSendRight:
- _objc_retain_x11
- _setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:trueVideoTransitionReferenceSampleBuffer:fencePortSendRight:.trueVideoTransitionExitObservedForSignpost
- _vdsp_configureVideoDataRemoteQueueSinkNode
CStrings:
+ " Learned Fusion,"
+ "! ( mirroringNeeded || scalingNeeded || videoZoomNeeded || P3ToBT2020ConversionEnabled || deviceOrientationCorrectionNeeded || cropNeeded )"
+ "! _useDynamicFieldOfViewRects"
+ "! emitNodeError"
+ "! outputNodeError"
+ "%.2fdeg"
+ "%02x"
+ "%@ attached media correction"
+ "%@ was added to the graph but has no callback."
+ "%@-%@-Inference"
+ "%@: [%p] \nisoSpeedRating: %d \ncameraManufacturer: %@ \ncameraModelName: %@ \ncolorTranslationMatrices: %@ \nwhiteBalanceFactors: %@ \nshutterSpeedAngle: %f \nexposureTime: %f \nwhiteBalanceCCT: %d\n lscGains %@\n cctAndTintColorMatrices: %@\n"
+ "%@[0].%@"
+ "%dK"
+ "%f"
+ "%llu,%llu"
+ "&MSGAllocateSyncHandle != ((void*)0) && &MSGCreate != ((void*)0)"
+ "( ( landscapeCropVideoFormats.count == 0 ) || ( landscapeCropVideoFormats.count == 1 ) )"
+ "( ( lowCCTRGRatio > 0 ) && ( lowCCTBGRatio > 0 ) && ( highCCTRGRatio > 0 ) && ( highCCTBGRatio > 0 ) )"
+ "( ( portraitCropVideoFormats.count == 0 ) || ( portraitCropVideoFormats.count == 1 ) )"
+ "( ( squareCropVideoFormats.count == 0 ) || ( squareCropVideoFormats.count == 1 ) )"
+ "( [fieldOfViewRects count] == 2 )"
+ "( [homographyData length] == sizeof(simd_float3x3) )"
+ "( [smartFramingFieldOfViewRects count] >= 2 ) && ( [smartFramingFieldOfViewRects count] <= 4 )"
+ "( aspectRatio == FigCaptureAspectRatioDefault ) || self.isDynamicAspectRatioSupported"
+ "( inputDrivesVideoCapture || inputDrivesMetadataCapture )"
+ "( lscGridHeader->version == FigCaptureStreamLSCGainGridVersion_2 )"
+ "( movieFileVideoConnectionConfigurations.count == 2 )"
+ "( scaleDescriptorFormat.dimensions.width == 1 ) && ( scaleDescriptorFormat.dimensions.height == 1 )"
+ "( scaleDescriptorFormat.pixelFormat == kCVPixelFormatType_OneComponent16Half )"
+ "( stillImageConnectionConfigurations.count == 2 )"
+ "(externalSync:%@)"
+ "(locked:%@)"
+ "+[FigPulseGenerator isSupported]_block_invoke"
+ ", (bcRotation ON)"
+ ", (multiCamClientCompositing ON)"
+ ", Output Aspect Ratio RequestID: %lld"
+ ", Output Aspect Ratio: %d"
+ ", csoCompensation %d"
+ "-[BWDeferredCaptureControllerInput _shouldDropSampleBufferIfNecessary:]"
+ "-[BWDeferredCaptureControllerInput _stashSampleBufferIfNecessary:]"
+ "-[BWDeferredCaptureControllerInput setLearnedFusionProxyGenerationUsedEVMinus:]"
+ "-[BWFigVideoCaptureDevice _deviceDidStopStreaming]"
+ "-[BWFigVideoCaptureDevice _ubAdaptiveStillImageCaptureSettingsWithSettings:userInitiatedRequestPTS:captureType:captureFlags:sceneFlags:frameStatisticsByPortType:metadata:]"
+ "-[BWFigVideoCaptureDevice _updateSmartFramingFieldOfViewWithAspectRatio:zoomFactor:]"
+ "-[BWInferenceEngineController process]"
+ "-[BWMultiCamClientCompositingNode _invokeClientCompositingCallbackForSettingsID:primarySampleBuffer:secondarySampleBuffer:outputSampleBufferOut:compositingMetadataOut:]"
+ "-[BWMultiCamClientCompositingNode handleNodeError:forInput:]"
+ "-[BWMultiStreamCameraSourceNode makeCurrentConfigurationLive]"
+ "-[BWMultiStreamCameraSourceNode setAspectRatio:]"
+ "-[BWNRFProcessorController _processLearnedFusion]"
+ "-[BWNRFProcessorController _processLearnedHRNR]"
+ "-[BWNRFProcessorController _processSingleImage]"
+ "-[BWVISNode initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:videoGreenGhostOfflineMetadataEnabled:videoGreenGhostOfflineLightSourceMaskEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:systemIsUnderCriticalThermalPressure:faceAwareVideoStabilizationEnabled:]"
+ "-[EGStillImageLearnedFusionNRFNode _handleAnyErrorRecoveryLogicWithErr:]"
+ "-[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingBuffer:metadata:type:captureFrameFlags:processorInput:err:]"
+ "-[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingInput:err:]"
+ "-[EGStillImageLearnedFusionNRFNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]"
+ "-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:graph:]"
+ "-[FigExternalSyncDevice _SSAMDeivceTerminatedService:]"
+ "-[FigExternalSyncDevice _setSSAMPortEnabled:]"
+ "-[FigExternalSyncDeviceDiscoverySessionManager _addDevice:]"
+ "-[FigExternalSyncDeviceDiscoverySessionManager _forceNotifyDelegatesDevicesChanged]"
+ "-[FigExternalSyncDeviceDiscoverySessionManager _handleDeviceEvent:]"
+ "-[FigExternalSyncDeviceDiscoverySessionManager _removeDevice:]"
+ "-[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceDeviceManagmentMonitoring]"
+ "-[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceObservationNotifications]"
+ "-[FigExternalSyncDeviceDiscoverySessionManager registerClient:delegate:]_block_invoke"
+ "-[FigExternalSyncDeviceDiscoverySessionManager unregisterAndCleanupClient:]_block_invoke"
+ "-[FigPulseGenerator _disciplineMSGTimeSyncClock:]"
+ "-[FigPulseGenerator _getOrCreateTimeSyncMSGClockIdentifier:tsClockIdentifierOut:]"
+ "-[FigPulseGenerator _getTimeSyncClock:clockOut:]"
+ "-[FigPulseGenerator _notifyDelegate:withError:]"
+ "-[FigPulseGenerator _resetMsgSyncs]"
+ "-[FigPulseGenerator _resetState]"
+ "-[FigPulseGenerator _startSyncs:]"
+ "-[FigPulseGenerator applySignalCompensationDelay:]"
+ "-[FigPulseGenerator startWithFrameRate:cmClock:clientAudioClockDeviceUIDOut:externalSync:]"
+ "-[FigPulseGenerator stopRunning]"
+ "1560602"
+ "16:9"
+ "1:1"
+ "20:59:36"
+ "3:4"
+ "4:3"
+ "9:16"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Digital Flash: Captures with more than one group is too disruptive for Zero Shutter Lag capture"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Digital Flash: Total bracketed exposure time '%f' is too disruptive for Zero Shutter Lag capture"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Failed to stop FigPulseGenerator. Error (%d)"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Failed to stop pulse generator: %d"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Learned Fusion only supports RAW-only capture"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: The deferred container manager is currently unable to support deferred processing. Changing capture type to WYSIWYG (LearnedHRNR)."
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Time machine frames metadata invalid: Exposure times too different, '%f' vs '%f'"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Time machine frames metadata invalid: Highlight recovery is not enabled for all frames"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Unexpected EV0 count for Learned Fusion HDR capture. Expected: 2. Got: %d"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Updating SmartFramingFieldOfView to ( %@ )"
+ "<<<< BWIrisStagingNode >>>> %s: Marking buffer %.3f as cutting buffer because SmartFraming FoV doesn't match. lastStaged: %u current: %u."
+ "<<<< BWMultiCamClientCompositingNode >>>> %s: %{public}@ Received error %d for client compositing callback; emitting original primary buffer"
+ "<<<< BWMultiCamClientCompositingNode >>>> %s: %{public}@ Received node error from input %d: %@"
+ "<<<< BWMultiCamClientCompositingNode >>>> Fig"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: %{pubilc}@: Dynamic aspect ratio set to %@"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: %{public}@: Dynamic aspect ratio is pending, graph is ready"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: %{public}@[%{public}@]: Dynamic aspect ratio %{public}@ change %{public}@, graph is %{public}@, PTS %.3f"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: %{public}@[%{public}@]: Dynamic aspect ratio %{public}@ graph is NOT READY, discarding frame PTS %.3f"
+ "<<<< BWNRFProcessorController >>>> %s: The SIFR frame for Learned NR with SIFR is likely to have flicker (exposure time:%f, frequency:%f). Falling back to Learned NR with Main"
+ "<<<< BWProResRawMetadataUtilities >>>> Fig"
+ "<<<< BWSmartCropNode >>>> Fig"
+ "<<<< BWSmartCropWarpingNode >>>> Fig"
+ "<<<< BWSmartFramingPerceptionSinkNode >>>> Fig"
+ "<<<< BWSmartFramingSceneMonitor >>>> Fig"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: Aspect ratio has changed from '%{public}@' to '%{public}@' for captureID:%{public}lld. Updating settings"
+ "<<<< BWStillImageProcessing >>>> %s: %{public}@ took %.2fms"
+ "<<<< BWStillImageProcessing >>>> %s: Adding stashed Learned Fusion EV- Sample Buffer because proxy generation has resolved"
+ "<<<< BWStillImageProcessing >>>> %s: Adding stashed Learned Fusion Error Recovery Sample Buffer because proxy generation has resolved"
+ "<<<< BWStillImageProcessing >>>> %s: Dropping Learned Fusion EVMinus Sample Buffer because proxy generation did not use it: %@"
+ "<<<< BWStillImageProcessing >>>> %s: Dropping Learned Fusion ErrorRecovery Sample Buffer because proxy generation used the EV-: %@"
+ "<<<< BWStillImageProcessing >>>> %s: Rotating photos and Exif metadata with %d degrees for camera sensor orientation compensation"
+ "<<<< BWStillImageProcessing >>>> %s: Stashing Learned Fusion EVMinus Sample Buffer until we learn if proxy generation used it: %@"
+ "<<<< BWStillImageProcessing >>>> %s: Stashing Learned Fusion ErrorRecovery Sample Buffer until we learn if proxy generation used it: %@"
+ "<<<< FigCaptureCameraSourcePipeline >>>> %s: %{public}@: Image circle radius is not calibrated, dark corners may not be removed"
+ "<<<< FigCaptureSession >>>> %s: Delaying CenterStage Onboarding Alert for %u seconds"
+ "<<<< FigCaptureSession >>>> %s: Failed to commit live reconfiguration (error:%{public}@)"
+ "<<<< FigCaptureSession >>>> %s: Failed to create pixel buffer to rotate Preview %@ for backwards compatibility for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: Failed to get FigPulseGenerator CMClock. Error (%d)"
+ "<<<< FigCaptureSession >>>> %s: Failed to get FigPulseGenerator TimeSyncClock. Error (%d)"
+ "<<<< FigCaptureSession >>>> %s: Failed to get MSGClock for %@. Error (%d)"
+ "<<<< FigCaptureSession >>>> %s: Failed to rotate DepthData %@ for backwards compatibility for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: Failed to rotate GlassesMatte %@ for backwards compatibility for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: Failed to rotate HairMatte %@ for backwards compatibility for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: Failed to rotate MainImage %@ for backwards compatibility for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: Failed to rotate PortraitEffectsMatte %@ for backwards compatibility for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: Failed to rotate Preview %@ for backwards compatibility for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: Failed to rotate SkinMatte %@ for backwards compatibility for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: Failed to rotate TeethMatte %@ for backwards compatibility for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: Live Reconfiguring Mic Source for FoV %f zoomFactor %f: %{public}@"
+ "<<<< FigCaptureSession >>>> %s: Live Reconfiguring Movie File Output Pipeline to %{public}@ : %{public}@"
+ "<<<< FigCaptureSession >>>> %s: Live Reconfiguring Preview Pipeline to %{public}@. : %{public}@"
+ "<<<< FigCaptureSession >>>> %s: Live Reconfiguring Source Pipeline to %{public}@ : %{public}@"
+ "<<<< FigCaptureSession >>>> %s: Live Reconfiguring Still Image Sink Pipeline to %{public}@ : %{public}@"
+ "<<<< FigCaptureSession >>>> %s: Live Reconfiguring Video Data Output Pipeline to %{public}@ : %{public}@"
+ "<<<< FigCaptureSession >>>> %s: Live Reconfiguring to %{public}@"
+ "<<<< FigCaptureSession >>>> %s: Rotating photos and Exif metadata with %d degrees for camera sensor orientation compensation"
+ "<<<< FigCaptureSession >>>> %s: Using cached RTSCProcessor for new configuration. isAspectRatioUnchanged: %d isLowLatencyStabilizationUnchanged: %d isCenterStageUnchanged: %d"
+ "<<<< FigCaptureSession >>>> %s: kFigCaptureError_TimeSyncMSGDisciplineTimeout"
+ "<<<< FigCaptureVideoDataSinkPipeline >>>>"
+ "<<<< FigExternalSyncDeviceDiscoverySession >>>>"
+ "<<<< FigExternalSyncDeviceDiscoverySession >>>> %s: Not used externalSyncDeviceDiscoverySession_SetProperty %@"
+ "<<<< FigExternalSyncDeviceDiscoverySession >>>> Fig"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@ Finished settup up observations"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@ Notifying delegate:%{public}@"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@ Registering new client: %{public}@"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@ adding device: %{public}@"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@ notification of disconnect for %llu"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@ observingSSAMEvents%{public}d"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@ removing client: %{public}@"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@ removing device: %{public}@"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: %{public}@ updated ssamEnabled to %d"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: SSAMDeviceFoundCallback static called with iterator %d"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> %s: ioDiscoveryInterface %d"
+ "<<<< FigExternalSyncDeviceDiscoverySessionManager >>>> Fig"
+ "<<<< FigPulseGenerator >>>> %s: Failed to startSyncs error: (%d)"
+ "<<<< FigPulseGenerator >>>> %s: Invalid parameter: delay is not numeric. delay: (%@)"
+ "<<<< FigPulseGenerator >>>> %s: Invalid parameter: failed to convert delay to tick time. delay: (%@)"
+ "<<<< FigPulseGenerator >>>> %s: MSGConfigureDerivedSync failed for front camera: %d"
+ "<<<< FigPulseGenerator >>>> %s: MSGConfigureDerivedSync failed for rear camera: %d"
+ "<<<< FigPulseGenerator >>>> %s: Not entitled to use MSG"
+ "<<<< FigPulseGenerator >>>> %s: Received error while turning off sync interrupt, error: %d"
+ "<<<< FigPulseGenerator >>>> %s: Recovering from a lost state _timeSyncMSGClockIdentifier: %llu, tsClockToTeardown: 0x%016llx"
+ "<<<< FigPulseGenerator >>>> %s: TimeSyncClockCreateWithClockIdentifier returned NULL"
+ "<<<< FigPulseGenerator >>>> %s: TimeSyncClockDispose(%p)"
+ "<<<< FigPulseGenerator >>>> %s: TimeSyncMSGAddClockInstance returned clockId 0x%016llx"
+ "<<<< FigPulseGenerator >>>> %s: TimeSyncMSGAddClockInstance( %d, (%llu/%llu) ) failed"
+ "<<<< FigPulseGenerator >>>> %s: TimeSyncMSGRemoveClockInstance failed to stop"
+ "<<<< FigPulseGenerator >>>> %s: TimeSyncMSGStartExternalSync failed to start, error: %d, tried for %.2f seconds. frameRate: %d/%d, toleranceExternalTriggerNs: %llu, toleranceSyncOutputNs: %llu, timeoutNs: %lld"
+ "<<<< FigPulseGenerator >>>> %s: TimeSyncMSGStopExternalSync failed to stop, error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: called"
+ "<<<< FigPulseGenerator >>>> %s: called with: tsClockIdentifier: 0x%016llx, error: %d while: _hasNotifiedDelegateOfClockCreation: %@, delegate: (%p)"
+ "<<<< FigPulseGenerator >>>> %s: called, frameRate: %@, wantsCMClock: %@, wantsTimeSyncClock: %@ isExternalSync: %@"
+ "<<<< FigPulseGenerator >>>> %s: created timeSyncClockRef: %p"
+ "<<<< FigPulseGenerator >>>> %s: failed configuring FrontCameraCluster follow frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed configuring RearCameraCluster follow frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed configuring leader frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed follow init on kV5XRearCameraCluster frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed follow init ot kV5XFrontCameraCluster frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed for front handler, error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed for lead handler, error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed for rear handler, error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed getOrCreateTimeSyncMSGClockIdentifier frameRate: %@, isExternalSync: %@, error: (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed leader init on kV5XLeader frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed starting interrupt on Leader frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed starting sync FrontCameraCluster frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed starting sync Leader frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed starting sync RearCameraCluster frameRate: %@ error (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed to create CMClock from TSClockIdentifier frameRate: %@, isExternalSync: %@, error: (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed to create TimeSyncClock from TSClockIdentifier frameRate: %@, isExternalSync: %@, error: (%d)"
+ "<<<< FigPulseGenerator >>>> %s: failed to discpline frameRate: %@, isExternalSync: %@, error: (%d)"
+ "<<<< FigPulseGenerator >>>> %s: frame rate changed, starting syncs"
+ "<<<< FigPulseGenerator >>>> %s: frameRate %@ not a valid rational"
+ "<<<< FigPulseGenerator >>>> %s: notifying delgate: tsClockIdentifier: 0x%016llx, error: %d"
+ "<<<< FigPulseGenerator >>>> %s: returning error %d"
+ "<<<< FigPulseGenerator >>>> %s: returning success"
+ "<<<< FigPulseGenerator >>>> %s: succeeded frameRate: %@"
+ "<<<< FigPulseGenerator >>>> %s: succeeded frameRate: (%d/%d). Disciplining: %.2f seconds (toleranceExternalTriggerNs: %llu, toleranceSyncOutputNs: %llu)"
+ "<<<< FigPulseGenerator >>>> Fig"
+ "<FigExternalSyncDevice %p retainCount: %ld%s allocator: %p, "
+ "@\"<BWDynamicAspectRatioChangeSource>\""
+ "@\"<BWSmartCropHomographyProvider>\""
+ "@\"<FigPulseGeneratorDelegate>\""
+ "@\"<RTSCProcessor>\""
+ "@\"ADEspressoMonocularVideoInferenceDescriptor\""
+ "@\"ADMonocularStillsPipeline\""
+ "@\"ADMonocularVideoPipeline\""
+ "@\"BWDisparityAPSScaling\""
+ "@\"BWMovieLevelMetadataForProResRaw\""
+ "@\"BWMultiCamClientCompositingNode\""
+ "@\"BWNRFProcessorController\""
+ "@\"BWPairedBufferSynchronizer\""
+ "@\"BWSmartCropNode\""
+ "@\"BWSmartFramingSceneMonitor\""
+ "@\"NSData\"40@0:8{?=qiIq}16"
+ "@108@0:8@16{?=ii}24B32i36@40B48B52B56@60@68B76B80B84f88B92B96B100B104"
+ "@116@0:8{?=ii}16@24i32i36i40{?=[3]}44i92B96@100@108"
+ "@132@0:8@16@24@32@40@48@56@64@72@80@88@96@?104B112@116@124"
+ "@136@0:8Q16Q24Q32i40B44B48B52B56f60B64i68B72B76f80f84i88@92@100B108B112B116@120@128"
+ "@184@0:8@16i24i28@32f40f44i48I52i56B60B64i68f72i76B80B84B88i92{CGRect={CGPoint=dd}{CGSize=dd}}96@128f136@140@148f156B160B164B168B172B176B180"
+ "@32@0:8@16i24B28"
+ "@36@0:8I16s20B24@?28"
+ "@44@0:8@16@24B32@?36"
+ "@48@0:8Q16B24B28@32B40i44"
+ "@52@0:8Q16Q24B32Q36Q44"
+ "@64@0:8@16@24@32B40B44@48@56"
+ "@72@0:8B16f20B24B28B32@36@44B52B56B60B64B68"
+ "@76@0:8@16B24B28i32B36B40@44I52B56i60B64B68B72"
+ "@88@0:8@16i24B28B32B36B40B44@48I56B60i64@68B76B80B84"
+ "@92@0:8@16@24@32@40i48i52f56i60i64I68B72B76B80^i84"
+ "@96@0:8@16Q24Q32@40@48@56@64@72@?80@88"
+ "ADImageDimensions"
+ "ADMonocularStillsPipeline"
+ "ADMonocularStillsPipelineParameters"
+ "ADMonocularVideoPipeline"
+ "ADMonocularVideoPipelineParameters"
+ "AlternateHeadroom"
+ "AppleGamut/AppleLog/BT2020"
+ "AppleHPMARM"
+ "AppleLog2SupportedForProRes"
+ "Aspect ratio crop landscape LearnedNR output allocator"
+ "Aspect ratio crop portrait LearnedNR output allocator"
+ "Aspect ratio crop square LearnedNR output allocator"
+ "Aug 26 2025"
+ "B40@0:8{?=(?={?=ii}f)i}16{?=(?={?=ii}f)i}28"
+ "BWDynamicAspectRatioChangeSource"
+ "BWMovieLevelMetadataForProResRaw"
+ "BWMultiCamClientCompositingNode"
+ "BWMultiCamClientCompositingNode.m"
+ "BWProResRawMetadataUtilities.m"
+ "BWSmartCropHomographyProvider"
+ "BWSmartCropNode"
+ "BWSmartCropNode.m"
+ "BWSmartCropWarpingNode"
+ "BWSmartCropWarpingNode.m"
+ "BWSmartFramingPerceptionSinkNode"
+ "BWSmartFramingPerceptionSinkNode.m"
+ "BWSmartFramingSceneMonitor"
+ "BWSmartFramingSceneMonitor.m"
+ "BaseHeadroom"
+ "BaseZoomFactorOverridesByAspectRatio"
+ "BrightPop"
+ "CGPointMakeWithDictionaryRepresentation( (CFDictionaryRef)distortionOpticalCenterDictionary, &dynamicDistortedOpticalCenterV2 )"
+ "CGPointMakeWithDictionaryRepresentation( (CFDictionaryRef)opticalCenterDictionary, &staticDistortedOpticalCenter )"
+ "CMM monocular depth is requested but not supported on this device!"
+ "CamGazeRawProbability"
+ "CameraIntrinsicMatrix not found"
+ "CameraSensorOrientationCompensation"
+ "CaptureSessionVideoDataSinkProperty_MovieLevelMetadata"
+ "Center Stage (SmartCrop)"
+ "ChannelMetadata"
+ "Class getADImageDimensionsClass(void)_block_invoke"
+ "Class getADMonocularStillsPipelineClass(void)_block_invoke"
+ "Class getADMonocularStillsPipelineParametersClass(void)_block_invoke"
+ "Class getADMonocularVideoPipelineClass(void)_block_invoke"
+ "Class getADMonocularVideoPipelineParametersClass(void)_block_invoke"
+ "CompositingMetadata"
+ "CompositionPictureInPictureRect"
+ "CompositionPictureInPictureRectMetadata"
+ "CoreImageGainMapProperties"
+ "Correct inference attached media aspect ratio"
+ "CurrentExternalSyncDevices"
+ "D23"
+ "DONE"
+ "DigitalFlashZeroShutterLagSupported"
+ "Distortion Correction Enhanced Resolution output pool (%@)"
+ "DynamicAspectRatioRequestID"
+ "DynamicAspectRatioSupported"
+ "EGStillImageLearnedFusionNRFNode"
+ "EGStillImageLearnedFusionRoutingNode"
+ "EnabledSmartFramingFieldsOfView"
+ "ExternalSyncDeviceDiscoverySession"
+ "ExternalSyncDeviceDiscoverySessionUpdateFirmware"
+ "ExternalSyncDeviceDiscoverySessionUpdateNotification"
+ "ExternalSyncDeviceDiscoverySessionUpdatePID"
+ "ExternalSyncDeviceDiscoverySessionUpdateVID"
+ "ExternalSyncDeviceSignalCompensationDelay"
+ "ExternalSyncMaxFrameRate"
+ "F%.2f"
+ "FaceAwareVideoStabilizationSupported"
+ "FacePriority"
+ "FaceStabilizationTunings"
+ "Failed to add Video Depth Monocular CMM inference to the inference engine"
+ "Failed to create an inference engine"
+ "Failed to create disparityMultiplierPixelBuffer"
+ "Failed to get FigPulseGenerator CMClock. Error (%d)"
+ "Failed to get FigPulseGenerator TimeSyncClock. Error (%d)"
+ "Failed to get MSGClock for %@. Error (%d)"
+ "Failed to get output scale descriptor (maybe due to SDK/build mismatch)"
+ "Failed to stop FigPulseGenerator. Error (%d)"
+ "FieldOfViewLandscape"
+ "FieldOfViewNone"
+ "FieldOfViewPortrait"
+ "FieldOfViewZoomedOutLandscape"
+ "FieldOfViewZoomedOutPortrait"
+ "FigCaptureSourceRemoteCopyExternalSyncDeviceDiscoverySessionSource"
+ "FigExternalSyncDevice"
+ "FigExternalSyncDeviceDiscoverySession.m"
+ "FigExternalSyncDeviceDiscoverySessionDelegateHandler"
+ "FigExternalSyncDeviceDiscoverySessionManager"
+ "FigExternalSyncDeviceDiscoverySessionManager.m"
+ "FigExternalSyncDeviceDiscoverySessionManagerDelegate"
+ "FigPulseGenerator"
+ "FigPulseGenerator.m"
+ "FigPulseGeneratorDelegate"
+ "FigPulseGeneratorUpdate"
+ "FrameDurationBounds"
+ "FrameDurationMax"
+ "FrameDurationMin"
+ "Full 1:1"
+ "Genlock"
+ "GlassesMatte"
+ "Graph live reconfiguration"
+ "H18"
+ "H18 Camera"
+ "HDRToneMap"
+ "HairMatte"
+ "IODeviceTree:/arm-io/isp"
+ "IOPortTransportProtocolCCUSBPDSSAM"
+ "IOPortTransportStateCC"
+ "LFD"
+ "LandscapeCropLearnedNROutput"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20280"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7012"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7023"
+ "LastShownBuild:FigCaptureSession.m:13567"
+ "LastShownBuild:FigCaptureSession.m:4755"
+ "LastShownBuild:FigCaptureSession.m:947"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20280"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7012"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7023"
+ "LastShownDate:FigCaptureSession.m:13567"
+ "LastShownDate:FigCaptureSession.m:4755"
+ "LastShownDate:FigCaptureSession.m:947"
+ "Learned Fusion only supports RAW-only capture"
+ "LearnedFusion"
+ "LearnedFusionRouting"
+ "LearnedFusionSupported"
+ "LearnedHRNRAddFrameFailure"
+ "LearnedHRNRFailure"
+ "LearnedHRNRSupported"
+ "LearnedHRSIFRFailure"
+ "Live reconfiguring BWSmartFramingPerceptionSinkNode with changing formats is not supported"
+ "LiveReconfigurationComplete"
+ "LiveReconfigurationForDynamicAspectRatioComplete"
+ "LockedFrameDurationMaxFrameRate"
+ "Low Latency Stabilization"
+ "LowLatencyStabilizationSupported"
+ "MainImage"
+ "MonaDepth"
+ "MonocularStreamingDepth"
+ "Movie File Client Compositing"
+ "Multi Cam Client Compositing Gain Map Output"
+ "Multi Cam Client Compositing Output"
+ "MultiCamClientCompositing"
+ "NOT READY"
+ "OnDemand-CaptureSessionRotationOutput-%@"
+ "Output scale dimensions must be (1, 1)"
+ "Output scale pixel format must be float16"
+ "OutputAspectRatioRequestID"
+ "OutputGainMapSampleBuffer_SerializedData"
+ "OutputGainMapSampleBuffer_SerializedSurface"
+ "OutputPTS"
+ "OutputSampleBuffer_SerializedSurface"
+ "PENDING"
+ "Portrait Matte Media scaler"
+ "PortraitCropLearnedNROutput"
+ "PortraitEffectsMatte"
+ "PrimaryGainMapSampleBuffer_SerializedData"
+ "PrimaryGainMapSampleBuffer_SerializedSurface"
+ "PrimaryPTS"
+ "PrimarySampleBuffer_SerializedSurface"
+ "ProResRawWhiteBalanceBlueFactor"
+ "ProResRawWhiteBalanceRedFactor"
+ "ProcessingLearnedFusion"
+ "ProcessingLearnedHRNR"
+ "Product ID (SOP)"
+ "PulseGeneratorError"
+ "PulseGeneratorUpdateClockID"
+ "PulseGeneratorUpdateLockState"
+ "PulseGeneratorUpdateNotification"
+ "PulseGeneratorUpdateOutOfBounds"
+ "PulseGeneratorUpdateSessionStopped"
+ "PulseGeneratorUpdateState"
+ "PulseGeneratorUpdateStatus"
+ "PulseGeneratorUpdateTriggerID"
+ "PulseGeneratorUpdateTriggerPreset"
+ "READY"
+ "RTSC"
+ "RTSCProcessorV%d"
+ "Sample buffer metadata not found"
+ "SecondaryGainMapSampleBuffer_SerializedData"
+ "SecondaryGainMapSampleBuffer_SerializedSurface"
+ "SecondaryPTS"
+ "SecondarySampleBuffer_SerializedSurface"
+ "SensorOutputLargerThanImageCircle"
+ "SigmaMultiplierForBiasTracking"
+ "SigmaMultiplierForFaceFiltering"
+ "SinkID"
+ "SkinMatte"
+ "SmartCrop"
+ "SmartCrop Warper"
+ "SmartCropCaptureStreamFormat"
+ "SmartCropFailure"
+ "SmartCropMaxFrameRateOverride"
+ "SmartCropOutputHeight"
+ "SmartCropOutputWidth"
+ "SmartCropSourceFormat"
+ "SmartCropSupported"
+ "SmartFramingFieldOfViewChangedNotification"
+ "SmartFramingMonitorRunning"
+ "SmartFramingPerceptionSink"
+ "SmartFramingSuggestedFieldOfViewChanged"
+ "SmartFramingSupported"
+ "SmartFramingTransitionPercentComplete"
+ "SmartFramingTransitionTargetFieldOfView"
+ "SmartFramingZoomFactorsByFieldOfView"
+ "SoftISP_%@"
+ "SquareCropLearnedNROutput"
+ "Still Image Client Compositing"
+ "Still pipelines live reconfiguration"
+ "T2030"
+ "T@\"<FigPulseGeneratorDelegate>\",W,N,V_delegate"
+ "T@\"ADEspressoMonocularVideoInferenceDescriptor\",R,N,V_monocularVideoInferenceDescriptor"
+ "T@\"BWNodeOutput\",R,V_compositionPictureInPictureRectMetadataOutput"
+ "T@\"BWSmartCropNode\",R,N,V_smartCropNode"
+ "T@\"BWVideoFormat\",&,N,V_landscapeCropOutputFormat"
+ "T@\"BWVideoFormat\",&,N,V_learnedFusionInputFormat"
+ "T@\"BWVideoFormat\",&,N,V_portraitCropOutputFormat"
+ "T@\"BWVideoFormat\",&,N,V_squareCropOutputFormat"
+ "T@\"BWVideoFormat\",R,N,V_disparityMultiplierFormat"
+ "T@\"EGInput\",R,N,V_hdrErrorRecoveryEVZeroInput"
+ "T@\"EGOutput\",R,N,V_attemptErrorRecoveryOutput"
+ "T@\"EGOutput\",R,N,V_evMinusOutput"
+ "T@\"EGOutput\",R,N,V_evZeroOutput"
+ "T@\"EGOutput\",R,N,V_fusionModeOutput"
+ "T@\"EGOutput\",R,N,V_longOutput"
+ "T@\"EGOutput\",R,N,V_secondEvZeroOutput"
+ "T@\"NSArray\",&,N,V_portTypesWithDigitalFlashZeroShutterLagEnabled"
+ "T@\"NSArray\",&,N,V_portTypesWithLearnedFusionEnabled"
+ "T@\"NSArray\",&,N,V_smartCropCandidateFramingRects"
+ "T@\"NSArray\",R,N,V_primarySbufInputs"
+ "T@\"NSDictionary\",&,N,V_baseZoomFactorOverridesByAspectRatio"
+ "T@\"NSDictionary\",&,N,V_visOverscanByAspectRatio"
+ "T@\"NSDictionary\",&,V_baseZoomFactorOverridesByAspectRatio"
+ "T@\"NSDictionary\",R,N,V_smartFramingZoomFactorsByFieldOfView"
+ "T@\"NSString\",C,N,V_multiCamClientCompositingPrimaryConnectionID"
+ "T@\"NSString\",R,N,V_externalSyncDeviceDeviceIdentifer"
+ "T@,&,N,V_rtscProcessor"
+ "TB,N,GisSmartFramingEnabled,V_smartFramingEnabled"
+ "TB,N,V_adaptiveSensorCropForDynamicAspectRatioEnabled"
+ "TB,N,V_cameraSensorOrientationCompensationEnabled"
+ "TB,N,V_dynamicAspectRatioEnabled"
+ "TB,N,V_faceStabilizationEnabled"
+ "TB,N,V_frontRearSimultaneousVideoRecording"
+ "TB,N,V_learnedFusionEnabled"
+ "TB,N,V_learnedHRNRSupported"
+ "TB,N,V_multiCamClientCompositingEnabled"
+ "TB,N,V_proResRawCaptureEnabled"
+ "TB,N,V_processSmartStyleRenderingInput"
+ "TB,N,V_sensorOutputLargerThanImageCircle"
+ "TB,N,V_smartCropSupported"
+ "TB,N,V_smartCropWarpingRequired"
+ "TB,N,V_smartFramingEnabled"
+ "TB,N,V_smartFramingRequiresSceneMonitoring"
+ "TB,R,GisLearnedFusionSupported"
+ "TB,R,GisLearnedHRNRSupported"
+ "TB,R,GisSmartCropSupported"
+ "TB,R,N,GisConnected,V_usbConnected"
+ "TB,R,N,GisDynamicAspectRatioSupported"
+ "TB,R,N,GisEnabled,V_enabled"
+ "TB,R,N,GisLowLatencyStabilizationSupported"
+ "TB,R,N,GisSSAMEnabled,V_ssamEnabled"
+ "TB,R,N,GisSmartFramingSupported"
+ "TB,R,N,GisStillImageOutputDownscaledInHWISP"
+ "TB,R,N,V_isPersistentlySignificant"
+ "TI,R,N,V_colorFeaturesPixelFormat"
+ "T^{OpaqueCMClock=},V_msgClock"
+ "Tail %d Secondary VIS Pipeline"
+ "TeethMatte"
+ "Tf,N,V_faceStabilizationSigmaMultiplierForBiasTracking"
+ "Tf,N,V_faceStabilizationSigmaMultiplierForFaceFiltering"
+ "Ti,N,V_cameraSensorOrientationCompensationDegreesCW"
+ "Ti,N,V_multiCamClientCompositingPrimaryCameraVideoStabilizationStrength"
+ "Ti,N,V_outputAspectRatio"
+ "Ti,N,V_smartFramingConfiguredFieldOfView"
+ "Ti,V_activeAspectRatio"
+ "Tq,N,V_outputAspectRatioRequestID"
+ "TrackedFace"
+ "Type"
+ "T{?=(?={?=ii}f)i},N,V_externalSyncFrameRate"
+ "T{?=(?={?=ii}f)i},N,V_lockedFrameRate"
+ "T{?=(?={?=ii}f)i},R,N"
+ "T{?=(?={?=ii}f)i},R,N,V_activeVideoExternalSyncFrameRate"
+ "T{?=(?={?=ii}f)i},R,N,V_activeVideoLockedFrameRate"
+ "T{?=ii},N,V_smartCropWarpingOutputDimensions"
+ "T{?=ii},R,N,V_colorFeaturesDimensions"
+ "Unable to create an inference processing configuration"
+ "Using compositing strategy %d with gain maps which is not supported!"
+ "V53"
+ "V53-V54"
+ "V54"
+ "V57"
+ "Vendor ID (SOP)"
+ "Video Capture"
+ "Video capture/SmartFraming Inference Splitter"
+ "VideoGeometricDistortionCorrectionEnabled"
+ "[(id)propertyValue isKindOfClass:[NSArray class]]"
+ "[RTSCProcessor prepareToProcess:] failed"
+ "[RTSCProcessor prewarm] failed"
+ "[RTSCProcessor setup] failed"
+ "[graph connectOutput:detectedObjectsOutputsBySourceDeviceType[underlyingDeviceType] toInput:smartCropNode.detectionMetadataInput pipelineStage:((void *)0)]"
+ "[graph connectOutput:previousMultiCamClientCompositingSecondaryVideoOutput toInput:multiCamClientCompositingNode.inputs[1] pipelineStage:tailCompressorPipelineStage]"
+ "[graph connectOutput:previousMultiCamCompositionPictureInPictureRectMetadataOutput toInput:_movieFileSinkNode.inputs[curMovieFileTrackIndex] pipelineStage:tailPipelineConfiguration.movieFilePipelineStage]"
+ "[graph connectOutput:previousOutput toInput:smartCropNode.input pipelineStage:previewPipelineStage]"
+ "[graph connectOutput:previousOutput toInput:smartCropNode.input pipelineStage:videoDataPipelineStage]"
+ "[graph connectOutput:previousVideoOutput toInput:multiCamClientCompositingNode.input pipelineStage:tailCompressorPipelineStage]"
+ "[graph connectOutput:previousVideoOutput toInput:smartCropNode.input pipelineStage:tailPipelineStage]"
+ "[graph connectOutput:smartFramingPerceptionOutput toInput:smartFramingPerceptionSinkNode.input pipelineStage:pipelineStage]"
+ "[graph connectOutput:videoOutput toInput:splitterNode.input pipelineStage:((void *)0)]"
+ "[parentPipeline addNode:multiCamClientCompositingNode error:&error]"
+ "[parentPipeline addNode:smartCropNode error:&error]"
+ "[super addNode:_multiCamClientCompositingNode error:&error]"
+ "[super addNode:matteMediaScalerNode error:&error]"
+ "[super addNode:smartCropNode error:&error]"
+ "[super addNode:smartCropWarpingNode error:&error]"
+ "[super addNode:smartFramingPerceptionSinkNode error:&error]"
+ "^{SyncHandle=}"
+ "_SSAMDeivceTerminatedService:"
+ "_activeClients"
+ "_activeDerivedSyncConfig"
+ "_activeVideoExternalSyncFrameRate"
+ "_activeVideoLockedFrameRate"
+ "_adaptiveSensorCropForDynamicAspectRatioEnabled"
+ "_addDevice:"
+ "_addMetadataInputsAndOutputsWithMetadataIdentifiers:"
+ "_addVideoCaptureInputAndOutput"
+ "_appendArray:withObject:restrictingLengthTo:"
+ "_attemptErrorRecoveryOutput"
+ "_baseZoomFactorOverridesByAspectRatio"
+ "_bufferPTSByConfigurationID"
+ "_bufferSynchronizer"
+ "_camGazeInferenceMajorVersion"
+ "_cameraInfoForPortType"
+ "_cameraModelName"
+ "_cameraSensorOrientationCompensationDegreesCW"
+ "_cameraSensorOrientationCompensationEnabled"
+ "_captureTypeLearnedFusion"
+ "_cctAndTintColorMatrices"
+ "_clientCompositingCallback"
+ "_colorFeaturesDimensions"
+ "_colorFeaturesPixelFormat"
+ "_colorTranslationMatrices"
+ "_compositingStrategy"
+ "_compositionPictureInPictureRectMetadataFormatDescription"
+ "_compositionPictureInPictureRectMetadataLocalID"
+ "_compositionPictureInPictureRectMetadataOutput"
+ "_configurationIDByOutputAspectRatioRequestID"
+ "_configureFollowSync:assertDur:offset:"
+ "_configureLeaderSync:frameRate:assertDur:"
+ "_configureLock"
+ "_createCalibrationDictionaryFromSampleBuffer:"
+ "_cumulativeSuggestedFOVType"
+ "_currentDevices"
+ "_detectedObjectsInfo"
+ "_detectedObjectsInfoPTS"
+ "_detectionMetadataIsLive"
+ "_digitalFlashZeroShutterLagEnabled"
+ "_disableDepthAndSegmentationRotationInLandscape"
+ "_disableRotationInLandscapeAspectRatio"
+ "_disciplineMSGTimeSyncClock:"
+ "_disciplinedMSGTimeSyncClock"
+ "_disparityAPSScaling"
+ "_disparityMultiplierFormat"
+ "_disparityMultiplierPixelBuffer"
+ "_disparityScalingFactor"
+ "_distortionCorrectionEnhancedResolutionOutputPool"
+ "_dynamicAspectRatioChangePending"
+ "_dynamicAspectRatioChangeSource"
+ "_dynamicAspectRatioEnabled"
+ "_dynamicAspectRatioGraphPrepared"
+ "_dynamicAspectRatioLock"
+ "_dynamicAspectRatioOutputConfigurations"
+ "_dynamicAspectRatioVISOverscan"
+ "_emitMotionAttachmentsSBufForOfflineProResRawVIS"
+ "_errorCodeTriggeringErrorRecovery"
+ "_evMinusOutput"
+ "_evZeroOutput"
+ "_exposureTime"
+ "_externalSyncDeviceDeviceIdentifer"
+ "_externalSyncFrameRate"
+ "_faceGroupID"
+ "_faceGroupIDsForInference"
+ "_faceRectExpansionScaleFactor"
+ "_faceRects"
+ "_faceSignificanceDetectionThreshold"
+ "_faceSizeScoreFiltered"
+ "_faceSizes"
+ "_faceStabilizationEnabled"
+ "_faceStabilizationSigmaMultiplierForBiasTracking"
+ "_faceStabilizationSigmaMultiplierForFaceFiltering"
+ "_faceTracks"
+ "_fieldsOfView"
+ "_firstMatchIterator"
+ "_firstSignificantTimeStamp"
+ "_followSyncConfig:config:"
+ "_followSyncInit:leader:trigger:"
+ "_forceNotifyDelegatesDevicesChanged"
+ "_formatDimensions"
+ "_frontRearSimultaneousVideoRecording"
+ "_fusionModeOutput"
+ "_gainMapSupported"
+ "_gazeConfidences"
+ "_gazeProbabilitiesByFaceGroupID"
+ "_gazeScores"
+ "_getMotionScoreUsingLargestFaceTrack:"
+ "_getOrCreateTimeSyncMSGClockIdentifier:tsClockIdentifierOut:"
+ "_getTimeSyncClock:clockOut:"
+ "_handleDeviceEvent:"
+ "_handleSyncErrorRecovery"
+ "_hasLearnedFusion"
+ "_hasNotifiedDelegateOfClockCreation"
+ "_hdrErrorRecoveryEVZeroInput"
+ "_homographyProvider"
+ "_hpmentid"
+ "_inferenceProcessingConfiguration"
+ "_inferenceSkipInterval"
+ "_initRTSCProcessor"
+ "_initRTSCProcessorWithOutputDimensions:"
+ "_initVMRefinerInference:"
+ "_ioServiceNotificationPort"
+ "_isExternalSync"
+ "_isMetadataValid"
+ "_isPersistentlySignificant"
+ "_isPrimaryStillImagePipeline"
+ "_isSampleBufferFromPrimaryStream:metadataDict:"
+ "_isSignificant"
+ "_isoSpeedRating"
+ "_landscapeCropOutputFormat"
+ "_lastFaceDetectionPTS"
+ "_lastInferenceFramePTS"
+ "_lastSuggestedFieldOfViewChangePTS"
+ "_lastTimeStampWhenAPSComputed"
+ "_leaderSyncConfig:config:"
+ "_leaderSyncInit:trigger:"
+ "_learnedFusionEnabled"
+ "_learnedFusionInputFormat"
+ "_learnedFusionProxyGenerationUsedEVMinus"
+ "_learnedHRNRSupported"
+ "_limitCropRectWithinImageCircle"
+ "_liveReconfigurationInProgress"
+ "_liveReconfigureForOutputAspectRatioLock"
+ "_loadAndConfigureSmartStyleBundle:"
+ "_lockedFrameRate"
+ "_longOutput"
+ "_lowLatencyStabilizationEnabled"
+ "_lowLatencyStabilizationEnabledInSourcePipeline"
+ "_lowLatencyStabilizationNode"
+ "_lscGains"
+ "_managedExternalSyncDevices"
+ "_maxFaceCountForInference"
+ "_minimumRequiredSignificantFaceCount"
+ "_monocularDepthScaleFactor"
+ "_monocularPipelineLock"
+ "_monocularStillsPipeline"
+ "_monocularStreamingDepthParameters"
+ "_monocularVideoInferenceDescriptor"
+ "_monocularVideoPipeline"
+ "_movieLevelMetadataForProResRaw"
+ "_movieLevelMetadataForProResRawFromFirstFrame"
+ "_movieSettings"
+ "_msgClock"
+ "_msgHandleFront"
+ "_msgHandleLeader"
+ "_msgHandleRear"
+ "_multiCamClientCompositingEnabled"
+ "_multiCamClientCompositingNode"
+ "_multiCamClientCompositingPrimaryCameraVideoStabilizationStrength"
+ "_multiCamClientCompositingPrimaryConnectionID"
+ "_networkHeight"
+ "_networkInputIsRotated"
+ "_networkWidth"
+ "_nextOutputAspectRatioRequestIDToRemove"
+ "_noFaceDetectedZoomOutTimeInSeconds"
+ "_notifyDelegate:withError:"
+ "_nrfProcessorControllerErrorRecoveryInput"
+ "_nrfProcessorControllerInput"
+ "_observingSSAMEvents"
+ "_optimalFOVHistory"
+ "_optimalFOVHistoryPTS"
+ "_optimizedFieldOfViewProcessingCropEnabled"
+ "_outputAspectRatioRequestID"
+ "_outputAspectRatioRequestIDByConfigurationID"
+ "_outputForSecondaryStillImagePipeline"
+ "_outputGainMapPixelBufferPool"
+ "_outputGainMapSampleBufferFormatDescription"
+ "_outputSampleBufferFormatDescription"
+ "_popHomography"
+ "_portTypesWithDigitalFlashZeroShutterLagEnabled"
+ "_portTypesWithLearnedFusionEnabled"
+ "_portraitCropOutputFormat"
+ "_previousAspectRatioIsLandscape"
+ "_previousInferenceComplete"
+ "_primarySbufInputs"
+ "_primaryStillSampleBuffer"
+ "_proResRawCaptureEnabled"
+ "_proresRawVideo"
+ "_pushHomography:pts:"
+ "_receivedNodeError"
+ "_removeDevice:"
+ "_replaceAttachedSampleBuffer:attachedMediaKey:primarySampleBuffer:aspectRatio:"
+ "_resetMsgSyncs"
+ "_resetState"
+ "_resetTemporalStateOnAspectRatioChange"
+ "_rtscProcessor"
+ "_secondEvZeroOutput"
+ "_secondaryStillSampleBuffer"
+ "_sensorOutputLargerThanImageCircle"
+ "_setSSAMPortEnabled:"
+ "_setupDeviceDeviceManagmentMonitoring"
+ "_setupDeviceObservationNotifications"
+ "_setupSSAMInterestNotification"
+ "_shutterSpeedAngle"
+ "_significanceDetectionThreshold"
+ "_singleCameraOverCaptureEnabled"
+ "_singleCameraOverCaptureEnabled ? _smartFramingEnabled : __objc_yes"
+ "_singleCameraOverCaptureRemainingFramesUntilStopOverCaptureRendering"
+ "_singleCameraOverCaptureShouldStopOverCaptureRendering"
+ "_smartCropCandidateFramingRects"
+ "_smartCropFormat"
+ "_smartCropHomographyProvider"
+ "_smartCropNode"
+ "_smartCropNodesBySourceDeviceType"
+ "_smartCropSupported"
+ "_smartCropWarpingOutputDimensions"
+ "_smartCropWarpingRequired"
+ "_smartFramingAvoidsResolvingSuggestedFieldOfViewForFlashScene"
+ "_smartFramingConfiguredFieldOfView"
+ "_smartFramingEnabled"
+ "_smartFramingEnabledFieldsOfView"
+ "_smartFramingFieldOfViewTransitionNotifyAppliedZoomFactors"
+ "_smartFramingFlashScene"
+ "_smartFramingIsMonitoringScene"
+ "_smartFramingLock"
+ "_smartFramingPreviousTransitionTargetFieldOfView"
+ "_smartFramingRequiresSceneMonitoring"
+ "_smartFramingSceneMonitor"
+ "_smartFramingSuggestedFieldOfView"
+ "_smartFramingTransitionInProgress"
+ "_smartFramingTransitionInterruptedByTrueVideoTransition"
+ "_smartFramingTransitionPercentComplete"
+ "_smartFramingTransitionTargetFieldOfView"
+ "_smartFramingZoomFactorsByFieldOfView"
+ "_sourceLock"
+ "_squareAspectRatioConfigEnabled"
+ "_squareCropOutputFormat"
+ "_ssamEnabled"
+ "_ssamentid"
+ "_startSync:"
+ "_startSyncs:"
+ "_stashedLearnedFusionEVMinus"
+ "_stashedLearnedFusionErrorRecovery"
+ "_stashedNRFProcessorController"
+ "_stillCaptureEnabled"
+ "_stillHomographyByPTS"
+ "_stillHomographyQueueLock"
+ "_stillPTSQueue"
+ "_stillsInputLock"
+ "_suggestedFOVSlackDurationInSeconds"
+ "_syncInterruptDisable:"
+ "_syncInterruptEnable:"
+ "_syncReset:"
+ "_teardownDeviceDeviceManagmentMonitoring"
+ "_teardownDeviceObservationNotifications"
+ "_teardownSSAMInterestNotification"
+ "_thresholdToRemovePrimaryBufferDetectedFacesObscuredByPIP"
+ "_timeSyncClockRef"
+ "_timeSyncClockRef != ((void*)0)"
+ "_timeSyncMSGClockIdentifier"
+ "_updateDetectedObjectsInfo:"
+ "_updateGazeStatesUsingGazeProbabilitiesData:gazeConfidenceFilteredOut:gazeScoreFilteredOut:"
+ "_updateOutputRequirements"
+ "_usbConnected"
+ "_useDynamicFieldOfViewRects"
+ "_useMonocularInference"
+ "_usePIPAIngestSignalingDomain"
+ "_vid"
+ "_viewsInAscendingFOV"
+ "_visOverscanByAspectRatio"
+ "_waitForInferenceToComplete"
+ "_whiteBalanceCCT"
+ "_whiteBalanceFactors"
+ "_writeFirstFrameMetadataForProResRaw"
+ "_zoomInTransitionEnabled"
+ "activeAspectRatio"
+ "activeVideoExternalSyncFrameRate"
+ "activeVideoLockedFrameRate"
+ "adaptiveSensorCropForDynamicAspectRatioEnabled"
+ "anyCaptureSourceSupportsMSG"
+ "appendData:"
+ "applySignalCompensationDelay:"
+ "attemptErrorRecovery"
+ "attemptErrorRecoveryOutput"
+ "baseZoomFactorOverridesByAspectRatio"
+ "bw_prores_raw_metadata_utilities_trace"
+ "bwsmartcropwarpingnode_trace"
+ "calibrationIlluminants.count == 2"
+ "cam-connections-scheme"
+ "cameraSensorOrientationCompensationDegreesCW"
+ "cameraSensorOrientationCompensationEnabled"
+ "candidateFramingCropRects"
+ "captureSession_liveReconfigureForOutputAspectRatioChange"
+ "captureSession_showCinematicFramingAlertIfApplicable_block_invoke"
+ "captureTypeLearnedFusion"
+ "colorCalibrations"
+ "colorCalibrations.count == 2"
+ "colorFeaturesDimensions"
+ "colorFeaturesPixelFormat"
+ "colorMatrices.count == 2"
+ "com.apple.TelephonyUtilities"
+ "com.apple.bwgraph.preview.smartFramingPerception"
+ "com.apple.cameracapture.figexternalsyncdevice"
+ "com.apple.coremedia.capture.perception"
+ "com.apple.coremedia.externalSyncDeviceDiscoverySession.notificationQueue"
+ "com.apple.figexternalsyncdevicediscoverysessionmanager"
+ "com.apple.gdc"
+ "com.apple.lsc"
+ "com.apple.private.master-sync-generator.user-access"
+ "com.apple.proresraw.lscdata"
+ "com.apple.proresraw.whitebalance.byccttint.colormatrices"
+ "com.apple.quicktime.full-frame-rate-playback-intent"
+ "com.apple.vdd"
+ "compositionPictureInPictureRectMetadataOutput"
+ "connectToSecondaryMultiCameraClientCompositingPipeline:"
+ "count > 2"
+ "cropRectDict"
+ "cs_getMasterClockAndType"
+ "csp_configureMultiStreamCameraNode"
+ "currentDevices"
+ "deviceDisconnectedEvent:"
+ "deviceSupportsCMM == __objc_yes"
+ "digitalFlashZeroShutterLagEnabled"
+ "disparityMultiplierFormat"
+ "dynamicAspectRatioEnabled"
+ "dynamicAspectRatioSupported"
+ "evMinus"
+ "evMinusOutput"
+ "evZero"
+ "evZeroOutput"
+ "externalSyncDeviceDeviceIdentifer"
+ "externalSyncDeviceDiscoverySessionManager:connectedDevicesDidChange:"
+ "externalSyncDeviceDiscoverySession_SetProperty"
+ "externalSyncFrameRate"
+ "externalSyncMaxFrameRate"
+ "f20@0:8i16"
+ "f28@0:8^{opaqueCMSampleBuffer=}16B24"
+ "faceStabilizationEnabled"
+ "faceStabilizationSigmaMultiplierForBiasTracking"
+ "faceStabilizationSigmaMultiplierForFaceFiltering"
+ "figexternalsyncdevicediscoverysessionmanager_trace"
+ "figpulsegenerator_trace"
+ "forceCleanup"
+ "frontRearSimultaneousVideoRecording"
+ "fsqr"
+ "fudgedBaseZoomFactorForAspectRatio:"
+ "fusionModeOutput"
+ "gazeSampleCount > 0"
+ "gdcCoefficentArray"
+ "geometricDistortionCorrectionForSmartCropEnabled"
+ "getDefaultProcessorConfigurationForStills3x4"
+ "getDefaultProcessorConfigurationForStillsReversibility3x4"
+ "getDefaultProcessorConfigurationForStreamingAcceleratedSquareAspectRatio"
+ "getDefaultProcessorConfigurationForStreamingAcceleratedSquareAspectRatioWithFilterType:"
+ "getDefaultProcessorConfigurationForStreamingSquareAspectRatio"
+ "getDefaultProcessorConfigurationForStreamingSquareAspectRatioWithFilterType:"
+ "getDeviceInfoDict"
+ "getMetricScaleFactorForEFL:"
+ "getMonocularDepthScaleFactor:inputImageIsRotated:"
+ "getValidRadiusAfterGDCInImageCoord"
+ "getValidRadiusInImageCoord"
+ "hdrErrorRecoveryEVZero"
+ "hdrErrorRecoveryEVZeroInput"
+ "highCCM.count == 9"
+ "horizontalFieldOfViewForAspectRatio:"
+ "horizontalGeometricDistortionCorrectedFieldOfViewForAspectRatio:"
+ "http://ns.apple.com/HDRToneMap/1.0/"
+ "i24@0:8^{SyncHandle=}16"
+ "i28@0:8^{SyncHandle=}16C24"
+ "i28@0:8{?=(?={?=ii}f)i}16"
+ "i32@0:8Q16^@24"
+ "i32@0:8^{SyncHandle=}16I24C28"
+ "i32@0:8^{opaqueCMSampleBuffer=}16^i24"
+ "i36@0:8{?=(?={?=ii}f)i}16^Q28"
+ "i40@0:8@16^f24^f32"
+ "i40@0:8^{SyncHandle=}16q24Q32"
+ "i40@0:8^{opaqueCMSampleBuffer=}16@24^{CGRect={CGPoint=dd}{CGSize=dd}}32"
+ "i44@0:8^{SyncHandle=}16{?=(?={?=ii}f)i}24Q36"
+ "i48@0:8{?=(?={?=ii}f)i}16^^{OpaqueCMClock}28^@36B44"
+ "i72@0:8^{SyncHandle=}16{applemsg_sync_base_config=IBI{applemsg_time=qSSS}{applemsg_time=qSSS}}24"
+ "i72@0:8^{SyncHandle=}16{applemsg_sync_derived_config=IBSIS{applemsg_time=qSSS}{applemsg_time=qSSS}}24"
+ "i72@?0q8^{opaqueCMSampleBuffer=}16^{opaqueCMSampleBuffer=}24^{opaqueCMSampleBuffer=}32^{opaqueCMSampleBuffer=}40^{opaqueCMSampleBuffer=}48^{opaqueCMSampleBuffer=}56^@64"
+ "i80@?0^{__CFString=}8q16^{opaqueCMSampleBuffer=}24^{opaqueCMSampleBuffer=}32^{opaqueCMSampleBuffer=}40^{opaqueCMSampleBuffer=}48^{opaqueCMSampleBuffer=}56^{opaqueCMSampleBuffer=}64r^^{__CFDictionary}72"
+ "iOS 26.0"
+ "imageCircleCenterOut"
+ "imageCircleRadiusOut"
+ "imageDimensionsWithWidth:height:"
+ "initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:"
+ "initWithCaptureDevice:commandQueue:smartStyleRenderingEnabled:squareAspectRatioConfigEnabled:"
+ "initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:smartStyleRenderingEnabled:portraitPreviewForegroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:sourceStillImageOutputPortTypes:squareAspectRatioConfigEnabled:cropDepthToPrimaryCaptureAspectRatio:disableDepthAndSegmentationRotationInLandscape:"
+ "initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:secondaryStreamingPersonSegmentationEnabled:cropDepthToPrimaryCaptureAspectRatio:disableDepthAndSegmentationRotationInLandscape:"
+ "initWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:smartCropHomographyProvider:multiCamClientCompositingCallback:isPrimaryStillImagePipeline:graph:name:"
+ "initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:multiCamClientCompositingCallback:workgroup:"
+ "initWithDynamicFieldOfViewRectsEnabled:"
+ "initWithFaceGroupID:signficanceDetectionThreshold:"
+ "initWithHpmEntID:ssamEntID:connectionState:vid:pid:"
+ "initWithIndexOfInputProvidingOutputSampleBuffer:compositingStrategy:gainMapSupported:clientCompositingCallback:"
+ "initWithMetalCommandQueue:renderingMethod:squareAspectRatioConfigEnabled:"
+ "initWithMetalCommandQueue:squareAspectRatioConfigEnabled:"
+ "initWithName:stillImageSettings:nodeConfiguration:provideInferenceInputImageForProcessing:addSyncErrorRecoveryPorts:portType:delegate:"
+ "initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:smartFramingEnabled:irisRequestDelegate:inferenceScheduler:"
+ "initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxLossyCompressionLevel:cameraExtrinsicMatrix:processingMode:stillCaptureEnabled:objectMetadataIdentifiers:captureDevice:"
+ "initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:squareAspectRatioConfigEnabled:subjectRelightingPreviewVersion:"
+ "initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:videoGreenGhostOfflineMetadataEnabled:videoGreenGhostOfflineLightSourceMaskEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:systemIsUnderCriticalThermalPressure:faceAwareVideoStabilizationEnabled:"
+ "initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:inputFormatIsProResRaw:errorOut:"
+ "initWithSession:andNodeMetadataOutput:usePIPAIngestSignalingDomain:completionHandler:"
+ "initWithSinkID:captureDevice:inferenceScheduler:"
+ "initWithStitchingDisabledAndZoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:propagateDepth:propagateStyles:smartFramingZoomFactorsByFieldOfView:sensorOrientationByPortType:singleCameraOverCaptureEnabled:parallaxMitigationBasedOnZoomFactorEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:"
+ "inputCalibrationData"
+ "inputSampleBufferMetadata != ((void *)0)"
+ "isConnected"
+ "isDigitalFlashZeroShutterLagSupported"
+ "isDynamicAspectRatioSupported"
+ "isExternalSyncDevicePulse"
+ "isLearnedFusionSupported"
+ "isLearnedHRNRSupported"
+ "isLowLatencyStabilizationSupported"
+ "isMultiCamClientCompositingEnabled"
+ "isPersistentlySignificant"
+ "isProResRawAvailable"
+ "isSSAMEnabled"
+ "isSmartCropSupported"
+ "isSmartFramingEnabled"
+ "isSmartFramingSupported"
+ "isStillImageOutputDownscaledInHWISP"
+ "isSupported"
+ "iterator"
+ "kCIImageRepresentationISOGainMapGamma"
+ "kV5XTriggerID"
+ "kernelReturn == 0 "
+ "keysSortedByValueUsingComparator:"
+ "landscapeCropOutputFormat"
+ "landscapeCropOutputFormatVideoRequirement"
+ "lcrp"
+ "learnedFusionEnabled"
+ "learnedFusionInputFormat"
+ "learnedFusionSupported"
+ "learnedFusionSupportedForPortType:"
+ "learnedHRNRSupported"
+ "learnedfusion"
+ "lf"
+ "liveReconfigureForAspectRatio:"
+ "liveReconfigureForOutputAspectRatioCompleted:"
+ "liveReconfigureForOutputAspectRatioFirstBufferReceived:forConfigurationID:"
+ "liveReconfigureForOutputAspectRatioStarted:forConfigurationID:"
+ "liveReconfigureForOutputDimensions:"
+ "loadMonocularVideoPipeline"
+ "lockStatus == 0 "
+ "lockedFrameDurationMaxFrameRate"
+ "lockedFrameRate"
+ "long"
+ "longOutput"
+ "lowCCM.count == 9"
+ "lowLatencyStabilizationSupported"
+ "matchingDictionary"
+ "monocularStreamingDepthType"
+ "monocularVideoInferenceDescriptor"
+ "msgClock"
+ "msgResult == 0 "
+ "multiCamClientCompositingEnabled"
+ "multiCamClientCompositingNode"
+ "multiCamClientCompositingPrimaryCameraVideoStabilizationStrength"
+ "multiCamClientCompositingPrimaryConnectionID"
+ "newSession"
+ "opticalCenterOffsetDictionary"
+ "outputAspectRatio"
+ "outputAspectRatioRequestID"
+ "outputCameraIntrinsic"
+ "outputScale"
+ "pcrp"
+ "portTypesWithDigitalFlashZeroShutterLagEnabled"
+ "portTypesWithLearnedFusionEnabled"
+ "portraitCropOutputFormat"
+ "portraitCropOutputFormatVideoRequirement"
+ "previewDimensionsForAspectRatio:"
+ "previewStitcherSmartFramingFieldOfViewTransitionAppliedZoomFactor:zoomFactor:"
+ "primaryMovieFileVideoConnectionConfiguration"
+ "primarySbufInputs"
+ "proResRawAugmentedMovieLevelMetadataWithMovieLevelMetadata:"
+ "proResRawCaptureEnabled"
+ "pulseGenerator:updateSynchronizationClock:withError:"
+ "pulseGenerator:updatedTriggerID:withLockState:"
+ "pulseGenerator:updatedTriggerID:withOutOfBoundsError:"
+ "pulseGenerator:updatedTriggerID:withSessionStoppedExitStatus:"
+ "pulseGenerator:updatedTriggerID:withTriggerIsPresent:"
+ "pulseGeneratorFrameRate"
+ "referenceDimensionsDict != ((void *)0)"
+ "referenceDimensionsDict could not be created"
+ "registerClient:delegate:"
+ "renderMetadataSampleBuffer:forInput:"
+ "renderVideoSampleBuffer:forInput:"
+ "renderingHomography"
+ "requiredFormat.isDynamicAspectRatioSupported"
+ "resetSmartFramingSceneMonitor"
+ "resolveSuggestedFieldOfViewRectWithSampleBuffer:fromFieldOfViewRects:suggestedFieldOfViewRectOut:"
+ "resolveSuggestedFieldOfViewWithSampleBuffer:suggestedFieldOfViewOut:"
+ "result == 0 "
+ "rotatedPixelBuffer"
+ "rtscProcessor"
+ "sSSAMDeviceFoundCallback"
+ "scaleDescriptorFormat != ((void *)0)"
+ "secondEvZero"
+ "secondEvZeroOutput"
+ "secondaryVISPipeline"
+ "selfObj"
+ "sensorOutputLargerThanImageCircle"
+ "service"
+ "setActiveAspectRatio:"
+ "setActiveVideoLockedFrameRate:activeVideoExternalSyncFrameRate:"
+ "setActiveVideoMinFrameDuration:activeVideoMaxFrameDuration:"
+ "setAdaptiveSensorCropForDynamicAspectRatioEnabled:"
+ "setBaseZoomFactorOverridesByAspectRatio:"
+ "setCameraSensorOrientationCompensationDegreesCW:"
+ "setCameraSensorOrientationCompensationEnabled:"
+ "setDigitalFlashZeroShutterLagEnabled:"
+ "setDynamicAspectRatioEnabled:"
+ "setEnableFaceReframing:"
+ "setExternalSyncFrameRate:"
+ "setFaceStabilizationEnabled:"
+ "setFaceStabilizationSigmaMultiplierForBiasTracking:"
+ "setFaceStabilizationSigmaMultiplierForFaceFiltering:"
+ "setFrontRearSimultaneousVideoRecording:"
+ "setInFrameMixMode:"
+ "setInputCalibrationData:"
+ "setInputPTS:"
+ "setLandscapeCropOutputFormat:"
+ "setLearnedFusionEnabled:"
+ "setLearnedFusionInputFormat:"
+ "setLearnedFusionProxyGenerationUsedEVMinus:"
+ "setLearnedHRNRSupported:"
+ "setLockedFrameRate:"
+ "setMsgClock:"
+ "setMultiCamClientCompositingEnabled:"
+ "setMultiCamClientCompositingPrimaryCameraVideoStabilizationStrength:"
+ "setMultiCamClientCompositingPrimaryConnectionID:"
+ "setOutputAspectRatio:"
+ "setOutputAspectRatioRequestID:"
+ "setOutputFOVPreset:"
+ "setPortTypesWithDigitalFlashZeroShutterLagEnabled:"
+ "setPortTypesWithLearnedFusionEnabled:"
+ "setPortraitCropOutputFormat:"
+ "setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:fencePortSendRight:uniqueID:"
+ "setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:trueVideoTransitionReferenceSampleBuffer:smartFramingTransitionPercentComplete:smartFramingTransitionTargetFieldOfView:fencePortSendRight:"
+ "setProResRawCaptureEnabled:"
+ "setProcessSmartStyleRenderingInput:"
+ "setRenderingHomography:"
+ "setRequestedDimensions:"
+ "setRtscProcessor:"
+ "setSensorOutputLargerThanImageCircle:"
+ "setSmartCropCandidateFramingRects:"
+ "setSmartCropSupported:"
+ "setSmartCropWarpingOutputDimensions:"
+ "setSmartCropWarpingRequired:"
+ "setSmartFramingCamGazeProbabilitiesByFaceGroupID:"
+ "setSmartFramingConfiguredFieldOfView:"
+ "setSmartFramingEnabled:"
+ "setSmartFramingEnabledFieldsOfView:"
+ "setSmartFramingFieldOfViewRects:"
+ "setSmartFramingIsMonitoringScene:"
+ "setSmartFramingRequiresSceneMonitoring:"
+ "setSquareCropOutputFormat:"
+ "setVisOverscanByAspectRatio:"
+ "setZoomOutForMultiSubjects:"
+ "settingsIDNumber"
+ "sharedFigExternalSyncDeviceDiscoverySessionManager"
+ "sharedFigPulseGenerator"
+ "smartCropBail"
+ "smartCropCandidateFramingRects"
+ "smartCropFormat"
+ "smartCropHomographyDataForPTS:"
+ "smartCropNode"
+ "smartCropNode.detectionMetadataInput"
+ "smartCropNode.detectionMetadataOutput"
+ "smartCropOutputDimensions"
+ "smartCropSupported"
+ "smartCropWarpingOutputDimensions"
+ "smartCropWarpingOutputDimensionsHeight"
+ "smartCropWarpingOutputDimensionsWidth"
+ "smartCropWarpingRequired"
+ "smartFramingConfiguredFieldOfView"
+ "smartFramingEnabled"
+ "smartFramingIsMonitoringScene"
+ "smartFramingRequiresSceneMonitoring"
+ "smartFramingSuggestedFieldOfView"
+ "smartFramingSupported"
+ "smartFramingZoomFactorsByFieldOfView"
+ "sqrc"
+ "squareCropOutputFormat"
+ "squareCropOutputFormatVideoRequirement"
+ "ssamEnabled"
+ "startWithFrameRate:cmClock:clientAudioClockDeviceUIDOut:externalSync:"
+ "stillImageOutputDownscaledInHWISP"
+ "stopRunning"
+ "supportedDimensions"
+ "timeSyncResult == 0 "
+ "unregisterAndCleanupClient:"
+ "updateForLearnedFusionMissingEVMinus:missingHDRErrorRecoveryEVZero:"
+ "updateMetadataFromSampleBuffer:withCameraInfo:"
+ "updateSmartFramingCamGazeProbabilities:"
+ "updateStatesIfNeededUsingFaceRect:faceSize:gazeProbabilitiesData:largestFaceTrack:largestFaceSize:totalDetectedFaceCount:currentPTS:isSignificantOut:"
+ "updateStereoAudioCapturePairedCameraBaseFieldOfView:zoomFactor:"
+ "updatedDetectedObjectsInfo"
+ "usbConnected"
+ "v112@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16f48@52@60f68q72{?=qiIq}80^B104"
+ "v24@?0@\"NSMutableDictionary\"8@\"NSString\"16"
+ "v28@0:8Q16i24"
+ "v32@0:8@\"BWPreviewStitcherNode\"16d24"
+ "v32@0:8@\"FigExternalSyncDeviceDiscoverySessionManager\"16@\"NSArray\"24"
+ "v32@0:8@\"FigPulseGenerator\"16I24B28"
+ "v32@0:8@\"FigPulseGenerator\"16I24I28"
+ "v32@0:8@16I24B28"
+ "v32@0:8@16I24I28"
+ "v32@0:8@16d24"
+ "v32@0:8q16q24"
+ "v32@?0@\"NSString\"8@\"TrackedFace\"16^B24"
+ "v36@0:8@\"FigPulseGenerator\"16I24q28"
+ "v36@0:8@\"FigPulseGenerator\"16Q24i32"
+ "v36@0:8@16I24q28"
+ "v44@0:8^{opaqueCMSampleBuffer=}16@24^{opaqueCMSampleBuffer=}32i40"
+ "v56@0:8{?=[8I]}16@48"
+ "v76@0:8d16{CGPoint=dd}24d40^{opaqueCMSampleBuffer=}48d56i64@68"
+ "v76@0:8d16{CGPoint=dd}24d40d48i56@60q68"
+ "v88@0:8{?=[3]}16{?=qiIq}64"
+ "verticalFieldOfViewForAspectRatio:"
+ "verticalGeometricDistortionCorrectedFieldOfViewForAspectRatio:"
+ "video-depth-monocular-cmm"
+ "videoOutputsBySourceDeviceType.count == 1"
+ "videodepthmonocularcmm"
+ "visOverscanByAspectRatio"
+ "{?=ii}20@0:8i16"
+ "{applemsg_sync_derived_config=\"timer_sel\"I\"repeat\"B\"frame_skip\"S\"polarity\"I\"start_base_frame\"S\"assert_duration\"{applemsg_time=\"whole\"q\"frac\"S\"remainder_numerator\"S\"remainder_denominator\"S}\"offset\"{applemsg_time=\"whole\"q\"frac\"S\"remainder_numerator\"S\"remainder_denominator\"S}}"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xd1\xf0\xf0!"
+ "\xf1"
- "-[BWVISNode initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:videoGreenGhostOfflineMetadataEnabled:videoGreenGhostOfflineLightSourceMaskEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:systemIsUnderCriticalThermalPressure:]"
- "-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]"
- "22:56:21"
- "@112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
- "@132@0:8Q16Q24Q32i40B44B48B52B56f60B64i68B72B76f80f84i88@92@100B108B112@116@124"
- "@180@0:8@16i24i28@32f40f44i48I52i56B60B64i68f72i76B80B84B88i92{CGRect={CGPoint=dd}{CGSize=dd}}96@128f136@140@148f156B160B164B168B172B176"
- "@44@0:8Q16B24B28@32i40"
- "@52@0:8B16f20B24B28B32B36B40B44B48"
- "@72@0:8@16B24B28i32B36B40@44I52B56i60B64B68"
- "@80@0:8@16i24B28B32B36B40B44@48I56B60i64@68B76"
- "@88@0:8@16@24@32@40i48i52f56i60i64I68B72B76^i80"
- "@88@0:8@16Q24Q32@40@48@56@64@72@80"
- "@88@0:8@16{?=ii}24B32i36@40B48B52B56B60B64f68B72B76B80B84"
- "Aug 27 2025"
- "_initVMRefinerInference"
- "_loadAndConfigureSmartStyleBundle"
- "initWithCameraInfoByPortType:sensorBinningFactor:inputBuffersHaveHorizontalOverscanOnly:registrationType:registrationMetalCommandQueue:excludeStaticComponentFromAlignmentShifts:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:zoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:"
- "initWithCaptureDevice:commandQueue:smartStyleRenderingEnabled:"
- "initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:smartStyleRenderingEnabled:portraitPreviewForegroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:sourceStillImageOutputPortTypes:cropDepthToPrimaryCaptureAspectRatio:"
- "initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:depthFilterRenderingIsAfterPreviewStitcher:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:secondaryStreamingPersonSegmentationEnabled:cropDepthToPrimaryCaptureAspectRatio:"
- "initWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:name:"
- "initWithConfiguration:tailIndex:numTailPipelines:graph:parentPipeline:captureDevicesByConnectionID:inferenceScheduler:recordingStatusDelegate:workgroup:"
- "initWithMetalCommandQueue:renderingMethod:"
- "initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:inferenceScheduler:"
- "initWithOutputs:masksRefinerEnabled:propagateMasks:ispSMGProcessingSession:subjectRelightingPreviewVersion:"
- "initWithSensorIDDict:stabilizationMethod:stabilizationType:ispProcessingSession:maxSupportedFrameRate:activeMaxFrameRate:gpuPriority:metalSubmissionAndCompletionQueuePriority:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:zoomSmoothingEnabled:applyFrameCropOffset:motionMetadataPreloadingEnabled:visExecutionMode:livePhotoCleanOutputRect:cameraInfoByPortType:cvisExtendedLookAheadDuration:distortionCorrectionEnabledPortTypes:distortionCompensationEnabledPortTypes:minDistanceForBravoParallaxShift:videoGreenGhostOfflineMetadataEnabled:videoGreenGhostOfflineLightSourceMaskEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:attachStabilizedOutputCameraTrajectory:systemIsUnderCriticalThermalPressure:"
- "initWithSensorIDDictionaryByPortType:cameraInfoByPortType:tuningParameters:activePortTypes:horizontalSensorBinningFactor:verticalSensorBinningFactor:maxSupportedFrameRate:motionAttachmentsMode:motionAttachmentsSource:motionCallbackThreadPriority:provideSourceVideoWithMotionAttachmentsOutput:provideOfflineVISMotionDataOutput:errorOut:"
- "initWithSession:andNodeMetadataOutput:completionHandler:"
- "initWithStitchingDisabledAndZoomPIPOverlayEnabled:zoomPIPMinimumUIZoomFactor:zoomPIPSingleStreamModeEnabled:propagateDepth:propagateStyles:parallaxMitigationBasedOnZoomFactorEnabled:preallocateOutputBufferPool:primaryCaptureRectCenterYPixelOffsetEnabled:propagatePrimaryPreviewSource:"
- "setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:fencePortSendRight:uniqueID:"
- "setPrimaryCaptureRectAspectRatio:center:trueVideoTransitionPercentComplete:trueVideoTransitionReferenceSampleBuffer:fencePortSendRight:"
- "v64@0:8d16{CGPoint=dd}24d40@48q56"
- "v64@0:8d16{CGPoint=dd}24d40^{opaqueCMSampleBuffer=}48@56"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0!\xf0\xf0!"

```
