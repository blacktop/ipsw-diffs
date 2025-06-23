## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-650.0.0.122.4
-  __TEXT.__text: 0x7c2ee0
-  __TEXT.__auth_stubs: 0x5090
-  __TEXT.__objc_methlist: 0x31e60
-  __TEXT.__const: 0x1508b0
-  __TEXT.__cstring: 0xd6db6
-  __TEXT.__oslogstring: 0x1235c8
-  __TEXT.__gcc_except_tab: 0x3d0c
+655.0.0.122.4
+  __TEXT.__text: 0x7d4e58
+  __TEXT.__auth_stubs: 0x50f0
+  __TEXT.__objc_methlist: 0x324e0
+  __TEXT.__const: 0x1508c0
+  __TEXT.__cstring: 0xdab92
+  __TEXT.__oslogstring: 0x127655
+  __TEXT.__gcc_except_tab: 0x3bfc
   __TEXT.__dlopen_cstrs: 0x6af
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0xe8c0
+  __TEXT.__unwind_info: 0xea30
   __TEXT.__eh_frame: 0x68
-  __TEXT.__objc_classname: 0x8061
-  __TEXT.__objc_methname: 0x9f793
-  __TEXT.__objc_methtype: 0x14f5f
-  __TEXT.__objc_stubs: 0x45500
-  __DATA_CONST.__got: 0x6578
-  __DATA_CONST.__const: 0xae48
-  __DATA_CONST.__objc_classlist: 0x1b18
+  __TEXT.__objc_classname: 0x813d
+  __TEXT.__objc_methname: 0xa08b8
+  __TEXT.__objc_methtype: 0x15574
+  __TEXT.__objc_stubs: 0x45bc0
+  __DATA_CONST.__got: 0x6638
+  __DATA_CONST.__const: 0xee10
+  __DATA_CONST.__objc_classlist: 0x1b38
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x590
+  __DATA_CONST.__objc_protolist: 0x5a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13e00
+  __DATA_CONST.__objc_selrefs: 0x13f98
   __DATA_CONST.__objc_protorefs: 0x68
-  __DATA_CONST.__objc_superrefs: 0x1980
-  __DATA_CONST.__objc_arraydata: 0x36c0
-  __AUTH_CONST.__auth_got: 0x2858
-  __AUTH_CONST.__const: 0x42b0
-  __AUTH_CONST.__cfstring: 0x4a720
-  __AUTH_CONST.__objc_const: 0x8ea08
-  __AUTH_CONST.__objc_intobj: 0x5610
-  __AUTH_CONST.__objc_arrayobj: 0x2730
+  __DATA_CONST.__objc_superrefs: 0x19a0
+  __DATA_CONST.__objc_arraydata: 0x36f0
+  __AUTH_CONST.__auth_got: 0x2888
+  __AUTH_CONST.__const: 0x4390
+  __AUTH_CONST.__cfstring: 0x4c7a0
+  __AUTH_CONST.__objc_const: 0x8f978
+  __AUTH_CONST.__objc_intobj: 0x5658
+  __AUTH_CONST.__objc_arrayobj: 0x2760
   __AUTH_CONST.__objc_floatobj: 0x240
   __AUTH_CONST.__objc_dictobj: 0x1770
   __AUTH_CONST.__objc_doubleobj: 0xa70
-  __AUTH.__objc_data: 0x2b70
-  __DATA.__objc_ivar: 0xa140
-  __DATA.__data: 0x5180
+  __AUTH.__objc_data: 0x2cb0
+  __DATA.__objc_ivar: 0xa248
+  __DATA.__data: 0x52f0
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x18b0
-  __DATA.__bss: 0x1988
+  __DATA.__common: 0x1920
+  __DATA.__bss: 0x21c8
   __DATA_DIRTY.__objc_data: 0xe380
   __DATA_DIRTY.__data: 0xf98
   __DATA_DIRTY.__common: 0xd00
-  __DATA_DIRTY.__bss: 0xbe0
+  __DATA_DIRTY.__bss: 0xc00
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: 16DA126A-BF8F-3E5B-AEEA-DD7A358D395E
-  Functions: 32647
-  Symbols:   109056
-  CStrings:  66167
+  UUID: 40EAA089-919E-3082-9528-1CE76330342E
+  Functions: 32890
+  Symbols:   109980
+  CStrings:  67058
 
Symbols:
+ +[BWAdaptiveBracketingFrameParameters frameParametersWithEVZeroRatio:integrationTimeInMicroseconds:gain:maxAGC:]
+ +[BWAdaptiveBracketingFrameParameters frameParametersWithEVZeroRatio:integrationTimeInSeconds:gain:maxAGC:]
+ +[BWAdaptiveBracketingFrameParameters supportsSecureCoding]
+ +[BWDroppedSample newDroppedSampleWithReason:pts:backPressureSemaphoresToIgnore:]
+ +[BWInferenceSharedE5ANEMemoryProvider initialize]
+ +[BWInferenceSharedE5ANEMemoryProvider resourceCategory]
+ +[BWInferenceSharedResourceManager initialize]
+ +[BWInferenceSharedResourceManager resourceCategory]
+ +[BWNodeStillImagePrewarmMessage newMessageWithStillImageSettings:resourceConfig:]
+ +[BWPiecemealEncodingNode initialize]
+ +[BWPrewarmResourceConfiguration newResourceConfigWithSharedMetalAllocator:]
+ +[BWStillImageCaptureSettings initialize]
+ +[BWVideoDepthInferenceConfiguration pceDisparityColorInferenceDescriptorForVideoDepthLayout:inputSource:]
+ -[BWAdaptiveBracketingFrameParameters encodeWithCoder:]
+ -[BWAdaptiveBracketingFrameParameters evZeroRatio]
+ -[BWAdaptiveBracketingFrameParameters initWithCoder:]
+ -[BWAdaptiveBracketingFrameParameters integrationTimeInMicroseconds]
+ -[BWAudioRemixAnalysisMetadataNode _sendRemixMetadataSampleBuffer]
+ -[BWCompressedShotBufferNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]
+ -[BWDeepZoomInferenceProvider propagateInferenceResultForOutputRequirement:storage:propagationSampleBuffer:].cold.9
+ -[BWDepthConverterNode _removeConsumedAttachedMediaFromSampleBuffer:]
+ -[BWDerectificationInferenceProvider prewarmingSharedResourceType]
+ -[BWDerectificationInferenceProvider sharedResourcePreparator]
+ -[BWDeskCamNode deskViewTrapezoidDidUpdate]
+ -[BWDeskCamNode setDeskViewCameraZoomFactor:]
+ -[BWDisparityFilteringInferenceProvider prewarmingSharedResourceType]
+ -[BWDisparityFilteringInferenceProvider sharedResourcePreparator]
+ -[BWDisparityPostProcessingInferenceProvider prewarmingSharedResourceType]
+ -[BWDisparityPostProcessingInferenceProvider sharedResourcePreparator]
+ -[BWE5InferenceProvider _prepareWithSharedANEMemoryProvider:]
+ -[BWE5InferenceProvider prepareForExecutionWithSharedANEMemoryProvider:]
+ -[BWE5InferenceProvider prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:]
+ -[BWE5InferenceProvider prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:]
+ -[BWE5InferenceProvider prewarmingSharedResourceType]
+ -[BWE5InferenceProvider sharedResourcePreparator]
+ -[BWE5InferenceProvider sharedResourceType]
+ -[BWE5MultipleLayoutInferenceProvider _prepareWithSharedANEMemoryProvider:]
+ -[BWE5MultipleLayoutInferenceProvider prepareForExecutionWithSharedANEMemoryProvider:]
+ -[BWE5MultipleLayoutInferenceProvider prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:]
+ -[BWE5MultipleLayoutInferenceProvider prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:]
+ -[BWE5MultipleLayoutInferenceProvider prewarmingSharedResourceType]
+ -[BWE5MultipleLayoutInferenceProvider sharedResourcePreparator]
+ -[BWE5MultipleLayoutInferenceProvider sharedResourceType]
+ -[BWEspressoInferenceProvider prewarmingSharedResourceType]
+ -[BWEspressoInferenceProvider sharedResourcePreparator]
+ -[BWFaceTrackingNode configurationWithID:updatedFormat:didBecomeLiveForInput:]
+ -[BWFigCaptureDevice supportsISPProcessingSessionType:error:]
+ -[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:type:]
+ -[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:type:].cold.1
+ -[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:type:].cold.2
+ -[BWFigCaptureISPProcessingSession type]
+ -[BWFigVideoCaptureDevice _configureZoomFudgingWithAspectRatio:]
+ -[BWFigVideoCaptureDevice _ubAdaptiveStillImageCaptureSettingsWithSettings:userInitiatedRequestPTS:captureType:captureFlags:sceneFlags:frameStatisticsByPortType:metadata:]
+ -[BWFigVideoCaptureDevice _ubFramesMetadataHasSIFRSkip:]
+ -[BWFigVideoCaptureDevice _ubUpdateCurrentAdaptiveBracketedCaptureParamsForCaptureStreamSettings:frameStatistics:timeMachineFrameSelection:]
+ -[BWFigVideoCaptureDevice setTeleAutoVideoFrameRateAllows24FPS:]
+ -[BWFigVideoCaptureDevice teleAutoVideoFrameRateAllows24FPS]
+ -[BWFigVideoCaptureStream deliverSushiRaw]
+ -[BWFigVideoCaptureSynchronizedStreamsGroup ispBaseZoomFactorsByPortType]
+ -[BWInferenceDepthScalingProvider prewarmingSharedResourceType]
+ -[BWInferenceDepthScalingProvider sharedResourcePreparator]
+ -[BWInferenceEngine _configureInferenceCachingPolicyForEligibleAdapters:]
+ -[BWInferenceFusionTrackerScalingProvider prewarmingSharedResourceType]
+ -[BWInferenceFusionTrackerScalingProvider sharedResourcePreparator]
+ -[BWInferenceScheduler setSharedE5ANEMemoryProvider:]
+ -[BWInferenceScheduler sharedE5ANEMemoryProvider]
+ -[BWInferenceSchedulerGraphInputNode sharedResourcePreparator]
+ -[BWInferenceSchedulerInference prepareForExecutionWithSharedANEMemoryProvider:]
+ -[BWInferenceSchedulerInference prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:]
+ -[BWInferenceSchedulerInference sharedResourcePreparator]
+ -[BWInferenceSchedulerInference sharedResourceType]
+ -[BWInferenceSchedulerScaler sharedResourcePreparator]
+ -[BWInferenceSharedE5ANEMemoryProvider completeANEMemoryProviderCreationForNetwork:wasSuccessful:]
+ -[BWInferenceSharedE5ANEMemoryProvider dealloc]
+ -[BWInferenceSharedE5ANEMemoryProvider description]
+ -[BWInferenceSharedE5ANEMemoryProvider fetchANEMemoryProviderForNetwork:]
+ -[BWInferenceSharedE5ANEMemoryProvider fetchANEMemoryProviderForNetwork:].cold.1
+ -[BWInferenceSharedE5ANEMemoryProvider fetchANEMemoryProviderForNetwork:].cold.2
+ -[BWInferenceSharedE5ANEMemoryProvider init]
+ -[BWInferenceSharedE5ANEMemoryProvider registerANEMemoryProvider:forNetwork:]
+ -[BWInferenceSharedResourceManager _purgeAllSharedResources]
+ -[BWInferenceSharedResourceManager dealloc]
+ -[BWInferenceSharedResourceManager description]
+ -[BWInferenceSharedResourceManager finalizeResourceCreationAttemptForCategory:]
+ -[BWInferenceSharedResourceManager init]
+ -[BWInferenceSharedResourceManager retrieveSharedResourceForResourceCategoryAndLockIfNotAvailable:]
+ -[BWInferenceSharedResourceManager stashSharedResource:forResourceCategory:]
+ -[BWInferenceVideoScalingProvider prewarmingSharedResourceType]
+ -[BWInferenceVideoScalingProvider sharedResourcePreparator]
+ -[BWIrisStagingNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:inferenceScheduler:]
+ -[BWLearnedMattingInferenceProvider reconcileWithPlaceholderProvider:]
+ -[BWMattingInferenceProvider prewarmingSharedResourceType]
+ -[BWMattingInferenceProvider sharedResourcePreparator]
+ -[BWMattingV2InferenceProvider prewarmingSharedResourceType]
+ -[BWMattingV2InferenceProvider sharedResourcePreparator]
+ -[BWMovieFileOutputAnalyticsPayload setVideoDeghostingStatistics:]
+ -[BWMovieFileOutputAnalyticsPayload videoDeghostingStatistics]
+ -[BWMultiStreamCameraSourceNode _updateZoomForOutputIndex:sampleBuffer:additionalScaleFactor:deliverSushiRaw:]
+ -[BWNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:]
+ -[BWNRFProcessorController inputReceivedProcessedRawErrorRecoveryFrame:proxy:]
+ -[BWNRFProcessorInput setProcessedRawErrorRecoveryFrame:proxy:]
+ -[BWNRFProcessorRequest initWithConfiguration:input:output:rawNightModeOutputFrame:deepFusionOutput:processErrorRecoveryFrame:processErrorRecoveryProxy:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:inferencesAvailable:processSmartStyleRenderingInput:delegate:]
+ -[BWNRFProcessorRequest keepFramesUntilReferenceFrameSelected]
+ -[BWNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]
+ -[BWNodeConnection bypassed]
+ -[BWNodeConnection suspended]
+ -[BWNodeOutput emitStillImagePrewarmMessageWithSettings:resourceConfig:]
+ -[BWNodeStillImagePrewarmMessage _initWithStillImageSettings:resourceConfig:]
+ -[BWNodeStillImagePrewarmMessage resourceConfig]
+ -[BWOpticalFlowInferenceProvider prewarmingSharedResourceType]
+ -[BWOpticalFlowInferenceProvider sharedResourcePreparator]
+ -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:]
+ -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:].cold.1
+ -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:].cold.2
+ -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:].cold.3
+ -[BWPhotoEncoderController _encodePrimarySbuf:metadata:processingFlags:primaryImageHandleInOut:]
+ -[BWPhotoEncoderController _outputDimensionsForSbuf:primaryImageMetadata:sourceDimensions:requestedStillImageCaptureSettings:isStereoPhotoCapture:isPrimaryFrame:]
+ -[BWPhotoEncoderController inputReceivedSbufForPiecemealEncoding:sbuf:attachedMediaKey:primaryImageMetadata:processingFlags:]
+ -[BWPhotoEncoderControllerInput addSbufForPiecemealEncoding:attachedMediakey:primaryImageMetadata:processingFlags:]
+ -[BWPhotoEncoderControllerInput releaseStashedAttachedMediaSampleBuffers]
+ -[BWPhotoEncoderControllerInput releaseStashedSamplebufferForAttachedMediaKey:]
+ -[BWPhotoEncoderControllerInput stashSampleBuffer:forAttachedMediaKey:]
+ -[BWPhotoEncoderControllerInput stashedAttachedMediaKeys]
+ -[BWPhotoEncoderControllerInput stashedSampleBufferForAttachedMediaKey:]
+ -[BWPhotoEncoderNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]
+ -[BWPhotonicEngineNode _processRawErrorRecoveryFrameWithNRFProcessorInput:processErrorRecoveryProxy:failureMetadata:]
+ -[BWPhotonicEngineNode _propagateSushiRawDNGDictionaryWithOutputSampleBuffer:requestedDimensions:aspectRatio:gdcRequested:]
+ -[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]
+ -[BWPhotonicEngineNode processorController:processRawErrorRecoveryFrameForProcessorInput:processErrorRecoveryProxy:failureMetadata:]
+ -[BWPhotonicEngineNodeResourceCoordinator adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderForPortType:]
+ -[BWPiecemealEncodingNode _releaseResources]
+ -[BWPiecemealEncodingNode dealloc]
+ -[BWPiecemealEncodingNode didReachEndOfDataForConfigurationID:input:]
+ -[BWPiecemealEncodingNode didSelectFormat:forInput:]
+ -[BWPiecemealEncodingNode initWithNodeConfiguration:]
+ -[BWPiecemealEncodingNode nodeType]
+ -[BWPiecemealEncodingNode renderSampleBuffer:forInput:]
+ -[BWPiecemealEncodingNode renderSampleBuffer:forInput:].cold.1
+ -[BWPiecemealEncodingNode renderSampleBuffer:forInput:].cold.2
+ -[BWPiecemealEncodingNode renderSampleBuffer:forInput:].cold.3
+ -[BWPiecemealEncodingNode renderSampleBuffer:forInput:].cold.4
+ -[BWPiecemealEncodingNode renderSampleBuffer:forInput:].cold.5
+ -[BWPiecemealEncodingNode sharePhotoEncoderControllerForPiecemealEncoding:]
+ -[BWPreviewStabilizationNode initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:minimumSupportedUIZoomFactor:]
+ -[BWPreviewStabilizationNode initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:minimumSupportedUIZoomFactor:].cold.1
+ -[BWPreviewStitcherNode _applyBrightnessCompensationToImage:referenceImage:bounds:compensationLevel:]
+ -[BWPreviewStitcherNode _renderCameraTransitionRampToPixelBuffer:bounds:withWiderCameraPixelBuffer:narrowerCameraPixelBuffer:zoomingIn:progress:narrowerCameraBounds:narrowerCameraShift:featherEdges:rampCameraTransition:renderEnhancedFeathering:narrowerCameraEdgeExpansionRamp:qsubToQsumEdgeOpacityRamp:qsubToQsumEdgeOpacityRampFromProgress:renderBrightnessCompensation:]
+ -[BWPreviewStitcherNode emitSampleBufferSemaphore]
+ -[BWPreviewStitcherNode handleDroppedSample:forInput:]
+ -[BWPreviewStitcherNode setEmitSampleBufferSemaphore:]
+ -[BWPrewarmResourceConfiguration dealloc]
+ -[BWPrewarmResourceConfiguration initWithSharedMetalAllocatorBackend:]
+ -[BWPrewarmResourceConfiguration sharedMetalAllocatorBackend]
+ -[BWQuickTimeMovieFileSinkNode _collectVideoDeghostingStatisticsFromDictionary:]
+ -[BWRealtimeCinematographyNode _frameCaptureIDAndPTSForSampleBuffer:captureIDOut:bufferPTSOut:]
+ -[BWRealtimeCinematographyNode _updateFromQueue:sampleBufferOut:captureID:bufferPTS:]
+ -[BWRectificationInferenceProvider prewarmingSharedResourceType]
+ -[BWRectificationInferenceProvider sharedResourcePreparator]
+ -[BWSmartStyleRenderingProcessorController _getDenormalizedFinalCropRectFromSourceForPixelBuffer:metadata:]
+ -[BWSmartStyleRenderingProcessorControllerConfiguration depthDataDeliveryEnabled]
+ -[BWSmartStyleRenderingProcessorControllerConfiguration setDepthDataDeliveryEnabled:]
+ -[BWStillImageBufferRouterNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]
+ -[BWStillImageCaptureStreamSettings adaptiveBracketingFrameParametersForFrame:]
+ -[BWStillImageCaptureStreamSettings adaptiveTimeMachineBracketedCaptureParams]
+ -[BWStillImageCaptureStreamSettings addAdaptiveBracketingFrameParameters:timeMachineBracketedCaptureParams:preBracketFrameCaptureParams:unifiedBracketedCaptureParams:captureFrameInfos:]
+ -[BWStillImageCaptureStreamSettings addAdaptiveBracketingMetadataIfNeededForFrame:]
+ -[BWStillImageCaptureStreamSettings expectedAdaptiveBracketedTimeMachineFrameCaptureCountUsingGroup:]
+ -[BWStillImageCaptureStreamSettings initWithPortType:captureType:captureFlags:referenceFrameIndex:adaptiveBracketingParameters:sphereOffsets:]
+ -[BWStillImageCaptureStreamSettings isFirstAdaptiveBracketingFrame:]
+ -[BWStillImageFilterNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]
+ -[BWStillImageFrameCoordinatorNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]
+ -[BWStillImageSettings initWithRequestedSettings:captureSettings:processingSettings:].cold.1
+ -[BWStreamingFilterNode handleDroppedSample:forInput:]
+ -[BWStreamingFilterNode(Configuration) previewFilterBackpressureSemaphore]
+ -[BWStreamingFilterNode(Configuration) setPreviewFilterBackpressureSemaphore:]
+ -[BWSubjectRelightingCalculator initWithInferenceScheduler:]
+ -[BWTiledEspressoInferenceConfiguration pipelineProcessingContext]
+ -[BWTiledEspressoInferenceConfiguration setPipelineProcessingContext:]
+ -[BWTiledEspressoInferenceProvider prewarmingSharedResourceType]
+ -[BWTiledEspressoInferenceProvider sharedResourcePreparator]
+ -[BWTiledInferenceProvider prewarmingSharedResourceType]
+ -[BWTiledInferenceProvider sharedResourcePreparator]
+ -[BWUBCaptureParameters upscaledEnhancedResolutionEffectiveIntegrationTimeThreshold]
+ -[BWUBNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]
+ -[BWVISNode setIspProcessingSession:]
+ -[BWVariableFrameRateSelector _loadDefaultsWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:teleAutoVideoFrameRateAllows24FPS:]
+ -[BWVariableFrameRateSelector initWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:teleAutoVideoFrameRateAllows24FPS:]
+ -[BWVideoDepthInferenceConfiguration initWithConcurrencyWidth:videoDepthLayout:captureDevice:requiresCroppingOfDepthBuffer:requiresVerticalFlipOfDepthBuffer:backpressureEvent:].cold.1
+ -[BWVideoDepthNode prepareForCurrentConfigurationToBecomeLive].cold.1
+ -[BWVideoProcessingInferenceAdapter _generateInferenceProviderCacheKeyWithAttributes:]
+ -[BWVideoProcessingInferenceAdapter _newInferenceProviderWithType:analysisType:executionTarget:configuration:preventionReasons:resourceProvider:additionalCacheAttributes:]
+ -[BWVideoProcessingInferenceProvider prepareForSubmissionWithWorkQueue:].cold.1
+ -[BWVideoProcessingInferenceProvider prewarmingSharedResourceType]
+ -[BWVideoProcessingInferenceProvider sharedResourcePreparator]
+ -[BWVisionInferenceProvider prewarmingSharedResourceType]
+ -[BWVisionInferenceProvider sharedResourcePreparator]
+ -[CMCaptureLocalSessionController videoCameraSourceAttributes]
+ -[CMInferenceUtils _getNetworkPath:isE5:fsNetworks:]
+ -[CMInferenceUtils _getNetworkPath:isE5:fsNetworks:].cold.1
+ -[CMInferenceUtils init].cold.3
+ -[CMInferenceUtils init].cold.4
+ -[FigCaptureCameraParameters previewStabilizationParameters]
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:]
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.1
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.10
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.11
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.12
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.13
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.14
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.15
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.16
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.17
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.18
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.19
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.2
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.20
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.21
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.22
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.23
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.24
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.25
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.26
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.27
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.28
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.29
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.3
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.30
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.31
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.32
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.33
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.4
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.5
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.6
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.7
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.8
+ -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:].cold.9
+ -[FigCaptureCameraSourcePipeline _buildVideoCaptureOutputNetwork:previewOutputsBySourceDeviceType:stillImageOutputsByPortType:lightSourceMaskOutputsBySourceDeviceType:keypointDescriptorDataOutputsBySourceDeviceType:pipelineConfiguration:graph:videoCaptureDimensions:numberOfSecondaryFramesToSkip:rtscProcessorsBySourceDeviceType:]
+ -[FigCaptureCameraSourcePipeline cameraConfiguration]
+ -[FigCaptureCameraSourcePipeline initWithConfiguration:captureDevice:graph:name:renderDelegate:ispFastSwitchEnabled:rtscProcessorsBySourceDeviceType:error:]
+ -[FigCaptureCameraSourcePipeline isKeypointDescriptorDataOnVideoCaptureOutputsEnabledForSourceDeviceType:]
+ -[FigCaptureCameraSourcePipeline isLightSourceMaskOnVideoCaptureOutputsEnabledForSourceDeviceType:]
+ -[FigCaptureMovieFileSinkPipelineConfiguration setVideoGreenGhostOfflineMetadataEnabled:]
+ -[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:].cold.49
+ -[FigCapturePreviewSinkPipeline _metalCommandQueueWithNamePrefix:priority:]
+ -[FigCapturePreviewSinkPipeline _metalCompletionQueue]
+ -[FigCapturePreviewSinkPipeline _metalSubmissionQueue]
+ -[FigCaptureSessionParsedConfiguration connectionConfigurationsToBuild]
+ -[FigCaptureSourceCommonSettings teleAutoVideoFrameRateAllows24FPS]
+ -[FigCaptureSourceStreamsContainer switchOverZoomFactorsWithoutFudge]
+ -[FigCaptureSourceVideoFormat geometricDistortionCorrectedFieldOfView].cold.1
+ -[FigCaptureStillImageSettings resetDimensions]
+ -[FigCaptureStillImageSinkPipelineSessionStorage stillImageConnectionConfigurationForStillImageSinkPipeline:]
+ -[FigCaptureVISPipeline _buildVISPipelineWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:videoGreenGhostOfflineMetadataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:visProcessingSemaphore:]
+ -[FigCaptureVISPipeline _newVISNodeWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:pipelineStage:captureDevice:outputDimensions:irisVISCleanOutputRectOut:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:videoGreenGhostOfflineMetadataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:visProcessingSemaphore:]
+ -[FigCaptureVISPipeline initWithUpstreamOutput:graph:name:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:videoGreenGhostOfflineMetadataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:visProcessingSemaphore:]
+ GCC_except_table302
+ GCC_except_table306
+ GCC_except_table310
+ GCC_except_table316
+ GCC_except_table318
+ GCC_except_table354
+ GCC_except_table357
+ GCC_except_table377
+ GCC_except_table379
+ GCC_except_table393
+ GCC_except_table629
+ GCC_except_table82
+ GCC_except_table89
+ _.compoundliteral.34
+ _.compoundliteral.35
+ _.compoundliteral.37
+ _.compoundliteral.38
+ _.compoundliteral.39
+ _.compoundliteral.40
+ _.compoundliteral.76
+ _.compoundliteral.77
+ _.compoundliteral.79
+ _.compoundliteral.80
+ _.compoundliteral.81
+ _.compoundliteral.82
+ _.compoundliteral.83
+ _.compoundliteral.94
+ _BWCreateSushiRawDNGDictionary.cold.14
+ _BWCreateSushiRawDNGDictionary.cold.15
+ _BWInferenceSharedResourceTypeDescription
+ _BWPhotoEncoderSmartStylesAttachedMediaKeysForPiecemealEncoding
+ _BWPhotoEncoderSupportsPiecemealEnocding
+ _CMCaptureGestaltGetDeviceFeatures
+ _CMCaptureGestaltGetExperimentalCFPreferenceDoubleWithCFStringKeyAndDefault
+ _CMCaptureGestaltGetExperimentalCFPreferenceNumberWithCFStringKeyAndDefault
+ _CMCaptureGestaltGetExperimentalCFPreferenceStringWithCFStringKeyAndDefault
+ _CMCaptureGestaltGetIntegerAnswer
+ _CMCaptureGestaltGetIntegerAnswer.cold.1
+ _CMCaptureGestaltGetStringAnswer
+ _CMCaptureGestaltGetStringAnswer.cold.1
+ _CMGQFirstSupportedReleaseVersion
+ _CMGQFrontFacingCameraFocalLengthIn35mm
+ _CMGQRearFacingSuperWideCameraFocalLengthIn35mm
+ _CMGQRearFacingTeleCameraFocalLengthIn35mm
+ _CMGQRearFacingWideCameraFocalLengthIn35mm
+ _D16_D17
+ _D27_D28
+ _D37_D38
+ _D421_D431
+ _D47_D48
+ _D49
+ _D52g_D53g
+ _D53p
+ _D54p
+ _D63_D64
+ _D73_D74
+ _D79
+ _D83
+ _D84
+ _D93_D94
+ _FigCaptureClientApplicationIDIsVoiceOver
+ _FigCaptureClientApplicationIDIsVoiceOver.cold.1
+ _FigCaptureClientApplicationIDIsVoiceOver.cold.2
+ _FigCaptureClientApplicationIDIsVoiceOver.cold.3
+ _FigCaptureClientApplicationIDIsVoiceOver.onceToken
+ _FigCaptureClientApplicationIDIsVoiceOver.sMatchedBundleIdentifiers
+ _FigCaptureMetadataUtilitiesGetFinalCropRectForSushiRaw
+ _FigCaptureNominalFocalLengthIn35mmFilmForPortType
+ _J171a_J172a
+ _J181_J182
+ _J210_J211_J217_J218
+ _J255_J256
+ _J271_J272
+ _J305
+ _J307_J308
+ _J310_J311
+ _J317_J317x_J318_J318x_J320_J320x_J321_J321x
+ _J407_J408
+ _J410_J411
+ _J417_J418_J420_J421
+ _J481_J482
+ _J507_J508_J537_J538
+ _J517_J517x_J518_J518x_J522_J522x_J523_J523x
+ _J607_J608_J637_J638
+ _J617_J618_J620_J621
+ _J717_J718_J720_J721
+ _N104
+ _OBJC_CLASS_$_BWInferenceSharedE5ANEMemoryProvider
+ _OBJC_CLASS_$_BWInferenceSharedResourceManager
+ _OBJC_CLASS_$_BWPiecemealEncodingNode
+ _OBJC_CLASS_$_BWPrewarmResourceConfiguration
+ _OBJC_CLASS_$_CIColorKernel
+ _OBJC_IVAR_$_BWAdaptiveBracketingFrameParameters._evZeroRatio
+ _OBJC_IVAR_$_BWDeskCamNode._deskViewCameraZoomFactor
+ _OBJC_IVAR_$_BWFigCaptureISPProcessingSession._type
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._lastStillZeroShutterLagFailureReason
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._teleAutoVideoFrameRateAllows24FPS
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._whiteBalanceGainsDeferredCommandID
+ _OBJC_IVAR_$_BWFigVideoCaptureSynchronizedStreamsGroup._ispBaseZoomFactorsByPortType
+ _OBJC_IVAR_$_BWInferenceScheduler._sharedE5ANEMemoryProvider
+ _OBJC_IVAR_$_BWInferenceSharedE5ANEMemoryProvider._networkListLock
+ _OBJC_IVAR_$_BWInferenceSharedE5ANEMemoryProvider._networksUsingE5ANEMemoryProvider
+ _OBJC_IVAR_$_BWInferenceSharedResourceManager._conditionVariablesTrackedByResourceCategory
+ _OBJC_IVAR_$_BWInferenceSharedResourceManager._resourceCreationMutex
+ _OBJC_IVAR_$_BWInferenceSharedResourceManager._resourcesBeingCreated
+ _OBJC_IVAR_$_BWInferenceSharedResourceManager._sharedResourceDirectoryByCategory
+ _OBJC_IVAR_$_BWInferenceSharedResourceManager._sharedResourceDirectoryRWLock
+ _OBJC_IVAR_$_BWIrisStagingNode._inferenceScheduler
+ _OBJC_IVAR_$_BWIrisStagingNode._minimumPrerollFrames
+ _OBJC_IVAR_$_BWMovieFileOutputAnalyticsPayload._videoDeghostingStatistics
+ _OBJC_IVAR_$_BWNRFProcessorRequest._processErrorRecoveryProxy
+ _OBJC_IVAR_$_BWNodeStillImagePrewarmMessage._resourceConfig
+ _OBJC_IVAR_$_BWPhotoEncoderControllerInput._stashedAttachedMediaSampleBuffersLock
+ _OBJC_IVAR_$_BWPhotonicEngineNodeResourceCoordinator._adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderByPortType
+ _OBJC_IVAR_$_BWPhotonicEngineNodeResourceCoordinator._resourceCoordinatorLock
+ _OBJC_IVAR_$_BWPiecemealEncodingNode._nodeConfiguration
+ _OBJC_IVAR_$_BWPiecemealEncodingNode._photoEncoderController
+ _OBJC_IVAR_$_BWPreviewGyroStabilization._ispMotionDataGroupDelay
+ _OBJC_IVAR_$_BWPreviewStabilizationNode._minimumSupportedUIZoomFactor
+ _OBJC_IVAR_$_BWPreviewStabilizationNode._photoModeFullStrengthUIZoomFactor
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionBorderEdgeFeatheringEnabled
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionBrightnessCompensationEnabled
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionBrightnessCompensationInsetPercentage
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionEdgeFeatheringBorderInsetFactor
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionEdgeFeatheringZoomInEndSigma
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionEdgeFeatheringZoomInStartSigma
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionEdgeFeatheringZoomInTeleEdgeExpansionFrameDuration
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionEdgeFeatheringZoomInTeleEdgeExpansionStartFrameFill
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionEdgeFeatheringZoomOutEndSigma
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionEdgeFeatheringZoomOutQsubToQsumEdgeOpacityRampFrameDuration
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionEdgeFeatheringZoomOutStartSigma
+ _OBJC_IVAR_$_BWPreviewStitcherNode._cameraTransitionEnhancedEdgeFeatheringEnabled
+ _OBJC_IVAR_$_BWPreviewStitcherNode._emitSampleBufferSemaphore
+ _OBJC_IVAR_$_BWPreviewStitcherNode._lastFrameDroppedByBackpressure
+ _OBJC_IVAR_$_BWPreviewStitcherNode._metalCompletionQueue
+ _OBJC_IVAR_$_BWPreviewStitcherNode._metalSubmissionQueue
+ _OBJC_IVAR_$_BWPreviewStitcherNode._triggerRegistrationForNondisruptiveSwitching
+ _OBJC_IVAR_$_BWPrewarmResourceConfiguration._sharedMetalAllocatorBackend
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._videoDeghostingStatistics
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._videoDeghostingStatisticsExtracted
+ _OBJC_IVAR_$_BWRealtimeCinematographyNode._usePTSToSyncPreviewAndCaptureFrames
+ _OBJC_IVAR_$_BWSmartStyleRenderingProcessorController._depthDataDeliveryEnabled
+ _OBJC_IVAR_$_BWSmartStyleRenderingProcessorControllerConfiguration._depthDataDeliveryEnabled
+ _OBJC_IVAR_$_BWStillImageCaptureStreamSettings._adaptiveBracketingFrameParameters
+ _OBJC_IVAR_$_BWStillImageCaptureStreamSettings._adaptiveTimeMachineBracketedCaptureParams
+ _OBJC_IVAR_$_BWStreamingFilterNode._previewFilterBackpressureSemaphore
+ _OBJC_IVAR_$_BWSubjectRelightingCalculator._inferenceScheduler
+ _OBJC_IVAR_$_BWTiledEspressoInferenceConfiguration._pipelineProcessingContext
+ _OBJC_IVAR_$_BWUBCaptureParameters._upscaledEnhancedResolutionEffectiveIntegrationTimeThreshold
+ _OBJC_IVAR_$_BWVariableFrameRateSelector._teleAutoVideoFrameRateAllows24FPS
+ _OBJC_IVAR_$_BWVideoDepthNode._nodePrepared
+ _OBJC_IVAR_$_BWVideoDepthNode._videoDepthConfiguration
+ _OBJC_IVAR_$_CMInferenceUtils._platformRegExpPatternV1
+ _OBJC_IVAR_$_CMInferenceUtils._platformRegExpPatternV2
+ _OBJC_IVAR_$_FigCaptureCameraParameters._previewStabilizationParameters
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._sourceDeviceTypesWithKeypointDescriptorDataEnabledOnVideoCaptureOutputs
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._sourceDeviceTypesWithLightSourceMaskEnabledOnVideoCaptureOutputs
+ _OBJC_IVAR_$_FigCaptureMovieFileSinkPipelineConfiguration._videoGreenGhostOfflineMetadataEnabled
+ _OBJC_IVAR_$_FigCapturePreviewSinkPipeline._metalCompletionQueue
+ _OBJC_IVAR_$_FigCapturePreviewSinkPipeline._metalSubmissionQueue
+ _OBJC_IVAR_$_FigCaptureSessionParsedConfiguration._connectionConfigurationsToBuild
+ _OBJC_IVAR_$_FigCaptureSourceCommonSettings._teleAutoVideoFrameRateAllows24FPS
+ _OBJC_IVAR_$_FigCaptureSourceStreamsContainer._baseZoomFactorsByPortTypeWithoutFudge
+ _OBJC_IVAR_$_FigCaptureVISPipeline._captureDevice
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkPipeline._videoDataCopierNode
+ _OBJC_METACLASS_$_BWInferenceSharedE5ANEMemoryProvider
+ _OBJC_METACLASS_$_BWInferenceSharedResourceManager
+ _OBJC_METACLASS_$_BWPiecemealEncodingNode
+ _OBJC_METACLASS_$_BWPrewarmResourceConfiguration
+ _OUTLINED_FUNCTION_565
+ _OUTLINED_FUNCTION_566
+ _OUTLINED_FUNCTION_567
+ _OUTLINED_FUNCTION_568
+ _OUTLINED_FUNCTION_569
+ _OUTLINED_FUNCTION_570
+ _OUTLINED_FUNCTION_571
+ _OUTLINED_FUNCTION_572
+ _OUTLINED_FUNCTION_573
+ _V59
+ __OBJC_$_CLASS_METHODS_BWInferenceSharedE5ANEMemoryProvider
+ __OBJC_$_CLASS_METHODS_BWInferenceSharedResourceManager
+ __OBJC_$_CLASS_METHODS_BWPiecemealEncodingNode
+ __OBJC_$_CLASS_METHODS_BWPrewarmResourceConfiguration
+ __OBJC_$_CLASS_METHODS_BWVideoDepthInferenceConfiguration
+ __OBJC_$_CLASS_PROP_LIST_BWAdaptiveBracketingFrameParameters
+ __OBJC_$_INSTANCE_METHODS_BWInferenceSharedE5ANEMemoryProvider
+ __OBJC_$_INSTANCE_METHODS_BWInferenceSharedResourceManager
+ __OBJC_$_INSTANCE_METHODS_BWPiecemealEncodingNode
+ __OBJC_$_INSTANCE_METHODS_BWPrewarmResourceConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_BWInferenceSharedE5ANEMemoryProvider
+ __OBJC_$_INSTANCE_VARIABLES_BWInferenceSharedResourceManager
+ __OBJC_$_INSTANCE_VARIABLES_BWPiecemealEncodingNode
+ __OBJC_$_INSTANCE_VARIABLES_BWPrewarmResourceConfiguration
+ __OBJC_$_PROP_LIST_BWInferenceSharedResourcePreparatory
+ __OBJC_$_PROP_LIST_BWPrewarmResourceConfiguration
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BWInferenceSharedResourcePreparatory
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BWInferenceSharedResourcePrewarmer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_DeskCamSessionDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BWInferenceSharedResourcePreparatory
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BWInferenceSharedResourcePrewarmer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_DeskCamSessionDelegate
+ __OBJC_$_PROTOCOL_REFS_BWInferenceSharedResourcePreparatory
+ __OBJC_$_PROTOCOL_REFS_BWInferenceSharedResourcePrewarmer
+ __OBJC_$_PROTOCOL_REFS_DeskCamSessionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BWAdaptiveBracketingFrameParameters
+ __OBJC_CLASS_RO_$_BWInferenceSharedE5ANEMemoryProvider
+ __OBJC_CLASS_RO_$_BWInferenceSharedResourceManager
+ __OBJC_CLASS_RO_$_BWPiecemealEncodingNode
+ __OBJC_CLASS_RO_$_BWPrewarmResourceConfiguration
+ __OBJC_LABEL_PROTOCOL_$_BWInferenceSharedResourcePreparatory
+ __OBJC_LABEL_PROTOCOL_$_BWInferenceSharedResourcePrewarmer
+ __OBJC_LABEL_PROTOCOL_$_DeskCamSessionDelegate
+ __OBJC_METACLASS_RO_$_BWInferenceSharedE5ANEMemoryProvider
+ __OBJC_METACLASS_RO_$_BWInferenceSharedResourceManager
+ __OBJC_METACLASS_RO_$_BWPiecemealEncodingNode
+ __OBJC_METACLASS_RO_$_BWPrewarmResourceConfiguration
+ __OBJC_PROTOCOL_$_BWInferenceSharedResourcePreparatory
+ __OBJC_PROTOCOL_$_BWInferenceSharedResourcePrewarmer
+ __OBJC_PROTOCOL_$_DeskCamSessionDelegate
+ ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.369
+ ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.373
+ ___101-[BWPreviewStitcherNode _applyBrightnessCompensationToImage:referenceImage:bounds:compensationLevel:]_block_invoke
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.783
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.783.cold.1
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.784
+ ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.793
+ ___106+[BWVideoDepthInferenceConfiguration pceDisparityColorInferenceDescriptorForVideoDepthLayout:inputSource:]_block_invoke
+ ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.723
+ ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.723.cold.1
+ ___117-[BWPhotonicEngineNode _processRawErrorRecoveryFrameWithNRFProcessorInput:processErrorRecoveryProxy:failureMetadata:]_block_invoke
+ ___117-[BWPhotonicEngineNode _processRawErrorRecoveryFrameWithNRFProcessorInput:processErrorRecoveryProxy:failureMetadata:]_block_invoke.cold.1
+ ___125-[BWPhotoEncoderController inputReceivedSbufForPiecemealEncoding:sbuf:attachedMediaKey:primaryImageMetadata:processingFlags:]_block_invoke
+ ___133-[BWInferenceScheduler _processJobsFromFramebuffer:usingInputSampleBuffer:inferencePropagationHandler:atExecutionTime:forConnection:]_block_invoke.125
+ ___133-[BWInferenceScheduler _processJobsFromFramebuffer:usingInputSampleBuffer:inferencePropagationHandler:atExecutionTime:forConnection:]_block_invoke.125.cold.1
+ ___137-[BWInferenceScheduler performInferencesForConnection:usingInputSampleBuffer:attachingResultsToSampleBuffer:skippingInferencesWithTypes:]_block_invoke.113
+ ___137-[BWInferenceScheduler performInferencesForConnection:usingInputSampleBuffer:attachingResultsToSampleBuffer:skippingInferencesWithTypes:]_block_invoke_2.114
+ ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.749
+ ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.749.cold.1
+ ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.749.cold.2
+ ___141-[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:]_block_invoke
+ ___165-[BWCameraStreamingMonitor _updateCameraStreamingMonitorInfoWithStreaming:cameraAccessGranted:clientAuditToken:tccIdentity:updateStreamingStatus:updateAccessStatus:]_block_invoke.47
+ ___165-[BWCameraStreamingMonitor _updateCameraStreamingMonitorInfoWithStreaming:cameraAccessGranted:clientAuditToken:tccIdentity:updateStreamingStatus:updateAccessStatus:]_block_invoke_2.48
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.1064
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.1090
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.728
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.886
+ ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.908
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.257
+ ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.269
+ ___47-[BWInferenceSharedResourceManager description]_block_invoke
+ ___47-[BWPhotonicEngineNode _ubInferenceInputRouter]_block_invoke.881
+ ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.389
+ ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.390
+ ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.396
+ ___50-[BWTemporalFilterNode didReachEndOfDataForInput:]_block_invoke
+ ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.364
+ ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.367
+ ___59-[BWStillImageCoordinatorNode renderSampleBuffer:forInput:]_block_invoke.84
+ ___60-[BWInferenceSharedResourceManager _purgeAllSharedResources]_block_invoke
+ ___60-[BWInferenceSharedResourceManager _purgeAllSharedResources]_block_invoke_2
+ ___62-[BWFigVideoCaptureDevice _setupStillImageCaptureStateMachine]_block_invoke.584
+ ___62-[BWFigVideoCaptureDevice _setupStillImageCaptureStateMachine]_block_invoke.587
+ ___62-[BWFigVideoCaptureDevice setRegionOfInterestWithoutOverscan:]_block_invoke
+ ___68-[BWFigVideoCaptureDevice _suspendTimeMachineWithCompletionHandler:]_block_invoke.551
+ ___70-[BWPhotoEncoderController prepareForCurrentConfigurationToBecomeLive]_block_invoke.222
+ ___72-[BWUBNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke
+ ___72-[BWUBNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke.149
+ ___73-[BWPhotonicEngineNode _handleClientBracketFrameEmissionForSampleBuffer:]_block_invoke.465
+ ___78-[BWFaceTrackingNode configurationWithID:updatedFormat:didBecomeLiveForInput:]_block_invoke
+ ___79-[BWStillImageCaptureStreamSettings adaptiveBracketingFrameParametersForFrame:]_block_invoke
+ ___80-[BWFigVideoCaptureDevice _sendInitialValuesToPortraitEffectPropertiesDelegate:]_block_invoke.1055
+ ___80-[BWFigVideoCaptureDevice _updateStateUsingVideoSampleBuffer:fromCaptureStream:]_block_invoke.309
+ ___80-[BWFigVideoCaptureDevice _updateStateUsingVideoSampleBuffer:fromCaptureStream:]_block_invoke.309.cold.1
+ ___80-[BWFigVideoCaptureDevice _updateStateUsingVideoSampleBuffer:fromCaptureStream:]_block_invoke.311
+ ___84-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke
+ ___84-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke.309
+ ___84-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke.310
+ ___84-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke.319
+ ___84-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke_2
+ ___86-[BWStillImageFilterNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.643
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.643.cold.1
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.644
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.644.cold.1
+ ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.644.cold.2
+ ___90-[BWCompressedShotBufferNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke
+ ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.635
+ ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.635.cold.1
+ ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.686
+ ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.686.cold.1
+ ___FigCaptureClientApplicationIDIsVoiceOver_block_invoke
+ ___block_descriptor_32_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8l
+ ___block_descriptor_32_e25_v32?0"NSString"816^B24l
+ ___block_descriptor_32_e40_v16?0"STMutableMediaStatusDomainData"8l
+ ___block_descriptor_32_e55_B24?0"BWStillImageCaptureFrameInfo"8"NSDictionary"16l
+ ___block_descriptor_33_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8l
+ ___block_descriptor_40_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8l
+ ___block_descriptor_40_e8_32o_e125_B72?0{BWCachedADPCEDisparityColorInferenceDescriptorRequirements=I{CGSize=dd}}8I40B44"NSString"48"NSString"56"NSArray"64ls32l8
+ ___block_descriptor_40_e8_32o_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8ls32l8
+ ___block_descriptor_40_e8_32o_e25_v32?0"NSString"816^B24ls32l8
+ ___block_descriptor_40_e8_32r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr32l8
+ ___block_descriptor_42_e5_v8?0l
+ ___block_descriptor_44_e8_v12?0B8l
+ ___block_descriptor_48_e8_32b_e8_v12?0B8ls32l8
+ ___block_descriptor_48_e8_32o40r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8ls32l8r40l8
+ ___block_descriptor_48_e8_32r40r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr32l8
+ ___block_descriptor_52_e5_v8?0l
+ ___block_descriptor_56_e8_32o40r48r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr40l8s32l8r48l8
+ ___block_descriptor_56_e8_32o40r_e173_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBB^{OpaqueFigSimpleMutex}BB}8lr40l8s32l8
+ ___block_descriptor_64_e8_32o40o48r_e5_v8?0ls32l8r48l8s40l8
+ ___block_descriptor_65_e8_32o40o48o56r_e32_v16?0"UNNotificationSettings"8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_84_e8_32o40o48o56o64r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8
+ ___block_descriptor_96_e8_32o40o_e5_v8?0ls32l8s40l8
+ ___block_literal_global.111
+ ___block_literal_global.115
+ ___block_literal_global.122
+ ___block_literal_global.1246
+ ___block_literal_global.1275
+ ___block_literal_global.1324
+ ___block_literal_global.1347
+ ___block_literal_global.1359
+ ___block_literal_global.1363
+ ___block_literal_global.1389
+ ___block_literal_global.1401
+ ___block_literal_global.1406
+ ___block_literal_global.1411
+ ___block_literal_global.1454
+ ___block_literal_global.146
+ ___block_literal_global.159
+ ___block_literal_global.172
+ ___block_literal_global.198
+ ___block_literal_global.258
+ ___block_literal_global.259
+ ___block_literal_global.269
+ ___block_literal_global.277
+ ___block_literal_global.281
+ ___block_literal_global.288
+ ___block_literal_global.301
+ ___block_literal_global.392
+ ___block_literal_global.419
+ ___block_literal_global.453
+ ___block_literal_global.509
+ ___block_literal_global.551
+ ___block_literal_global.553
+ ___block_literal_global.556
+ ___block_literal_global.577
+ ___block_literal_global.581
+ ___block_literal_global.586
+ ___block_literal_global.590
+ ___block_literal_global.608
+ ___block_literal_global.640
+ ___block_literal_global.677
+ ___block_literal_global.682
+ ___block_literal_global.716
+ ___block_literal_global.753
+ ___block_literal_global.755
+ ___block_literal_global.757
+ ___block_literal_global.759
+ ___block_literal_global.761
+ ___block_literal_global.763
+ ___block_literal_global.765
+ ___block_literal_global.769
+ ___block_literal_global.772
+ ___block_literal_global.805
+ ___block_literal_global.865
+ ___captureSession_Invalidate_block_invoke.1331
+ ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.1451
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.1449
+ ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.1444
+ ___captureSession_IrisStillImageSinkEndMomentCapture_block_invoke.1452
+ ___captureSession_SetConfiguration_block_invoke.1386
+ ___captureSession_SetSectionProperty_block_invoke.1355
+ ___captureSession_SetSectionProperty_block_invoke.1357
+ ___captureSession_SetSectionProperty_block_invoke.1361
+ ___captureSession_startDeferredGraphSetupOnWorkerQueueAfter_block_invoke.1256
+ ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke.1198
+ ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke_2.1199
+ ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1165
+ ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1169
+ ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1293
+ ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1303
+ ___cmcapturegestalt_buildDataBase_block_invoke
+ ___cmcapturegestalt_getAVFBringupDefaultOverride_block_invoke
+ ___fcru_promptOpenTapToRadar_block_invoke.81
+ ___nrfp_createStateMachine_block_invoke.751
+ ___rqReceiverSetSource_block_invoke.108
+ ___rqSenderFinalize_block_invoke.55
+ ___ubp_createStateMachine_block_invoke.545
+ _captureSession_SetSectionProperty.onceToken.1356
+ _captureSession_buildGraphWithConfiguration.cold.30
+ _captureSession_createCameraSourcePipelineConfigurationFromParsedConfiguration.cold.3
+ _cmcapturegestalt_buildDataBase.onceToken
+ _cmcapturegestalt_getAVFBringupDefaultOverride
+ _cmcapturegestalt_getAVFBringupDefaultOverride.cold.1
+ _cmcapturegestalt_getAVFBringupDefaultOverride.sAVFCaptureBringupDefaultOverrides
+ _cmcapturegestalt_getAVFBringupDefaultOverride.sLoadBringupDefaultOverridesOnceToken
+ _devices
+ _e5rt_ane_memory_provider_create
+ _e5rt_ane_memory_provider_release
+ _e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options
+ _e5rt_precompiled_compute_op_create_options_release
+ _e5rt_precompiled_compute_op_create_options_set_allocate_intermediate_buffers
+ _e5rt_precompiled_compute_op_create_options_set_custom_ane_memory_provider
+ _e5rt_precompiled_compute_op_create_options_set_operation_name
+ _gBWBWStillImageCaptureSettingsTrace
+ _gBWInferenceSharedE5ANEMemoryProvider
+ _gBWInferenceSharedResourceManager
+ _gBWPiecemealEncodingNodeTrace
+ _gBWVideoProcessingInferenceAdapterTrace
+ _gCMCaptureGestaltTrace
+ _kCIInputExtentKey
+ _kFigAppleMakerNote_FirstSupportedReleaseVersion
+ _kFigAppleMakerNote_NominalFocalLengthIn35mmFilm
+ _kFigCaptureDeviceProperty_SupportedISPProcessingSessionTypes
+ _kFigCaptureFlatDictionaryAppleMakerNote_FirstSupportedReleaseVersion
+ _kFigCaptureFlatDictionaryAppleMakerNote_FirstSupportedReleaseVersion_opaque
+ _kFigCaptureFlatDictionaryAppleMakerNote_FirstSupportedReleaseVersion_string
+ _kFigCaptureFlatDictionaryAppleMakerNote_NominalFocalLengthIn35mmFilm
+ _kFigCaptureFlatDictionaryAppleMakerNote_NominalFocalLengthIn35mmFilm_opaque
+ _kFigCaptureFlatDictionaryAppleMakerNote_NominalFocalLengthIn35mmFilm_string
+ _kFigCaptureSampleBufferMetadata_FinalCropRectForSushiRaw
+ _kFigCaptureSourceAttributeKey_BravoSwitchOverVideoZoomFactorsWithoutFudge
+ _kFigCaptureSourceAttributeKey_MidFrameSynchronizationNotSupported
+ _kFigCaptureStreamMetadata_SensorAccess
+ _kFigCaptureStreamMetadata_SynchronizedStreamsCameraControlsStatisticsPrimaryPortType
+ _kFigCaptureStreamTimeOfFlightAssistedAutoFocusEstimatorResultsKey_DropEventCount
+ _kFigCaptureStreamTimeOfFlightAssistedAutoFocusEstimatorResultsKey_DropMaxAccel
+ _kFigCaptureStreamTimeOfFlightAssistedAutoFocusEstimatorResultsKey_DropMinAccel
+ _kFigCaptureStreamTimeOfFlightAssistedAutoFocusEstimatorResultsKey_DropStatus
+ _kFigCaptureStreamTimeOfFlightAssistedAutoFocusEstimatorResultsKey_PowerOnEventCount
+ _kFigCaptureStreamTimeOfFlightAssistedAutoFocusEstimatorResultsKey_TrainingFDRDelta
+ _kFigCaptureStreamTimeOfFlightAssistedAutoFocusEstimatorResultsKey_TrainingPersistentDelta
+ _kFigCaptureVideoDeghostingSampleBufferAttachmentKey_VideoDeghostingStatistics
+ _kFigCaptureVideoDeghostingStatisticsKey_AverageGhostArea
+ _kFigCaptureVideoDeghostingStatisticsKey_AverageGhostCount
+ _kFigCaptureVideoDeghostingStatisticsKey_Enabled
+ _kFigCaptureVideoDeghostingStatisticsKey_OpticalCenterEstConfidence
+ _kFigCaptureVideoDeghostingStatisticsKey_OpticalCenterOffsetMag
+ _kFigCaptureVideoDeghostingStatisticsKey_OpticalCenterOffsetX
+ _kFigCaptureVideoDeghostingStatisticsKey_OpticalCenterOffsetY
+ _kFigCaptureVideoDeghostingStatisticsKey_Version
+ _objc_msgSend$_encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:
+ _objc_msgSend$_encodePrimarySbuf:metadata:processingFlags:primaryImageHandleInOut:
+ _objc_msgSend$_getNetworkPath:isE5:fsNetworks:
+ _objc_msgSend$_initWithStillImageSettings:resourceConfig:
+ _objc_msgSend$_outputDimensionsForSbuf:primaryImageMetadata:sourceDimensions:requestedStillImageCaptureSettings:isStereoPhotoCapture:isPrimaryFrame:
+ _objc_msgSend$adaptiveBracketingFrameParametersForFrame:
+ _objc_msgSend$addAdaptiveBracketingFrameParameters:timeMachineBracketedCaptureParams:preBracketFrameCaptureParams:unifiedBracketedCaptureParams:captureFrameInfos:
+ _objc_msgSend$addAdaptiveBracketingMetadataIfNeededForFrame:
+ _objc_msgSend$addSbufForPiecemealEncoding:attachedMediakey:primaryImageMetadata:processingFlags:
+ _objc_msgSend$applyWithExtent:arguments:
+ _objc_msgSend$bypassed
+ _objc_msgSend$completeANEMemoryProviderCreationForNetwork:wasSuccessful:
+ _objc_msgSend$connectionConfigurationsToBuild
+ _objc_msgSend$deskViewCameraZoomFactor
+ _objc_msgSend$emitStillImagePrewarmMessageWithSettings:resourceConfig:
+ _objc_msgSend$enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:
+ _objc_msgSend$evZeroRatio
+ _objc_msgSend$expectedAdaptiveBracketedTimeMachineFrameCaptureCountUsingGroup:
+ _objc_msgSend$fetchANEMemoryProviderForNetwork:
+ _objc_msgSend$finalizeResourceCreationAttemptForCategory:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$frameParametersWithEVZeroRatio:integrationTimeInSeconds:gain:maxAGC:
+ _objc_msgSend$handleStillImagePrewarmWithSettings:resourceConfig:forInput:
+ _objc_msgSend$imageByClampingToExtent
+ _objc_msgSend$initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:minimumSupportedUIZoomFactor:
+ _objc_msgSend$initWithFigCaptureISPProcessingSession:type:
+ _objc_msgSend$initWithInferenceScheduler:
+ _objc_msgSend$initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:inferenceScheduler:
+ _objc_msgSend$initWithPortType:captureType:captureFlags:referenceFrameIndex:adaptiveBracketingParameters:sphereOffsets:
+ _objc_msgSend$initWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:teleAutoVideoFrameRateAllows24FPS:
+ _objc_msgSend$inputAlphaVideoRequirement
+ _objc_msgSend$inputImageVideoRequirement
+ _objc_msgSend$inputReceivedProcessedRawErrorRecoveryFrame:proxy:
+ _objc_msgSend$inputReceivedSbufForPiecemealEncoding:sbuf:attachedMediaKey:primaryImageMetadata:processingFlags:
+ _objc_msgSend$integrationTimeInMicroseconds
+ _objc_msgSend$integrationTimeInSeconds
+ _objc_msgSend$isFirstAdaptiveBracketingFrame:
+ _objc_msgSend$ispBaseZoomFactorsByPortType
+ _objc_msgSend$kernelWithString:
+ _objc_msgSend$maximumNumberOfReferenceFrameCandidatesToHoldForProcessing
+ _objc_msgSend$newDroppedSampleWithReason:pts:backPressureSemaphoresToIgnore:
+ _objc_msgSend$newMessageWithStillImageSettings:resourceConfig:
+ _objc_msgSend$newResourceConfigWithSharedMetalAllocator:
+ _objc_msgSend$operatingSystemVersionString
+ _objc_msgSend$outputAlphaVideoRequirement
+ _objc_msgSend$outputFormatDescription
+ _objc_msgSend$outputLowResSegmentationCloneFormatDescription
+ _objc_msgSend$outputLowResSegmentationCloneVideoRequirement
+ _objc_msgSend$pceDisparityColorInferenceDescriptorForVideoDepthLayout:inputSource:
+ _objc_msgSend$pointerValue
+ _objc_msgSend$prepareForExecutionWithSharedANEMemoryProvider:
+ _objc_msgSend$prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:
+ _objc_msgSend$previewStabilizationParameters
+ _objc_msgSend$prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:
+ _objc_msgSend$prewarmingSharedResourceType
+ _objc_msgSend$processorController:processRawErrorRecoveryFrameForProcessorInput:processErrorRecoveryProxy:failureMetadata:
+ _objc_msgSend$rangeOfString:options:
+ _objc_msgSend$registerANEMemoryProvider:forNetwork:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$resetDimensions
+ _objc_msgSend$resourceCategory
+ _objc_msgSend$resourceConfig
+ _objc_msgSend$retrieveSharedResourceForResourceCategoryAndLockIfNotAvailable:
+ _objc_msgSend$setInputImageAppliedOffsets:
+ _objc_msgSend$setLowResGlassesMask:
+ _objc_msgSend$setMaximumNumberOfReferenceFrameCandidatesToHoldForProcessing:
+ _objc_msgSend$setPreviewFilterBackpressureSemaphore:
+ _objc_msgSend$setProcessedRawErrorRecoveryFrame:proxy:
+ _objc_msgSend$setTeleAutoVideoFrameRateAllows24FPS:
+ _objc_msgSend$setUseDeepTransferAccommodations:
+ _objc_msgSend$setVideoDeghostingStatistics:
+ _objc_msgSend$sharedE5ANEMemoryProvider
+ _objc_msgSend$sharedMetalAllocatorBackend
+ _objc_msgSend$sharedResourcePreparator
+ _objc_msgSend$sharedResourceType
+ _objc_msgSend$shouldCacheInferenceProvider
+ _objc_msgSend$stashSharedResource:forResourceCategory:
+ _objc_msgSend$stillImageConnectionConfigurationForStillImageSinkPipeline:
+ _objc_msgSend$stringByStandardizingPath
+ _objc_msgSend$supportsISPProcessingSessionType:error:
+ _objc_msgSend$teleAutoVideoFrameRateAllows24FPS
+ _objc_msgSend$upscaledEnhancedResolutionEffectiveIntegrationTimeThreshold
+ _pceDisparityColorInferenceDescriptorForVideoDepthLayout:inputSource:.sDescriptors
+ _pen_clapDimensionsFromPixelBuffer
+ _proc_name
+ _pthread_cond_broadcast
+ _rqSenderEnqueue.cold.4
+ _sCMCaptureGestaltBoolDataBase
+ _sCMCaptureGestaltFloatDataBase
+ _sCMCaptureGestaltIntegerDataBase
+ _sCMCaptureGestaltStringDataBase
- +[BWAdaptiveBracketingFrameParameters frameParametersWithIntegrationTimeInMicroseconds:gain:maxAGC:]
- +[BWAdaptiveBracketingFrameParameters frameParametersWithIntegrationTimeInSeconds:gain:maxAGC:]
- +[BWNodeStillImagePrewarmMessage newMessageWithStillImageSettings:]
- +[BWStreamingCVAFilterRenderer supportsCroppingDepthToPrimaryCaptureAspectRatio]
- +[BWStreamingFilterNode supportsCroppingDepthToPrimaryCaptureAspectRatio]
- -[BWAdaptiveBracketingFrameParameters integrationTimeInMiroseconds]
- -[BWBackgroundBlurNode captureDevice]
- -[BWBackgroundBlurNode setCaptureDevice:]
- -[BWCompressedShotBufferNode handleStillImagePrewarmWithSettings:forInput:]
- -[BWDeskCamNode didChangeDeskViewCameraZoomFactor:]
- -[BWE5InferenceProvider _prepare]
- -[BWE5MultipleLayoutInferenceProvider _prepare]
- -[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:]
- -[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:].cold.1
- -[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:].cold.2
- -[BWFigVideoCaptureDevice _configureZoomFudging]
- -[BWFigVideoCaptureDevice _ubAdaptiveStillImageCaptureSettingsWithID:captureType:captureFlags:sceneFlags:frameStatisticsByPortType:]
- -[BWFigVideoCaptureDevice _ubUpdateCurrentAdaptiveBracketedCaptureParamsForCaptureStreamSettings:frameStatistics:]
- -[BWIrisStagingNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:]
- -[BWMultiStreamCameraSourceNode _updateZoomForOutputIndex:sampleBuffer:additionalScaleFactor:]
- -[BWNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:]
- -[BWNRFProcessorController inputReceivedProcessedRawErrorRecoveryFrame:]
- -[BWNRFProcessorInput setProcessedRawErrorRecoveryFrame:]
- -[BWNRFProcessorRequest initWithConfiguration:input:output:rawNightModeOutputFrame:deepFusionOutput:processErrorRecoveryFrame:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:inferencesAvailable:processSmartStyleRenderingInput:delegate:]
- -[BWNode handleStillImagePrewarmWithSettings:forInput:]
- -[BWNodeOutput emitStillImagePrewarmMessageWithSettings:]
- -[BWNodeStillImagePrewarmMessage _initWithStillImageSettings:]
- -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:usedContainerOptionsOut:usedEncodingOptionsOut:mainImageHandleInOut:]
- -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:usedContainerOptionsOut:usedEncodingOptionsOut:mainImageHandleInOut:].cold.1
- -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:usedContainerOptionsOut:usedEncodingOptionsOut:mainImageHandleInOut:].cold.2
- -[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:usedContainerOptionsOut:usedEncodingOptionsOut:mainImageHandleInOut:].cold.3
- -[BWPhotoEncoderController inputReceivedNewAuxMedia:auxSbuf:attachedMediaKey:primaryImageMetadata:processingFlags:]
- -[BWPhotoEncoderControllerInput addAuxSbuf:attachedMediakey:primaryImageMetadata:processingFlags:]
- -[BWPhotoEncoderControllerInput stashedAttacheMediaSampleBuffersByAttachedMediaKey]
- -[BWPhotoEncoderNode handleStillImagePrewarmWithSettings:forInput:]
- -[BWPhotonicEngineNode _processRawErrorRecoveryFrameWithNRFProcessorInput:failureMetadata:]
- -[BWPhotonicEngineNode _propagateSushiRawDNGDictionaryWithOutputSampleBuffer:requestedDimensions:aspectRatio:requiresGDCInformation:]
- -[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]
- -[BWPhotonicEngineNode processorController:processRawErrorRecoveryFrameForProcessorInput:failureMetadata:]
- -[BWPreviewStabilizationNode initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:]
- -[BWPreviewStabilizationNode initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:].cold.1
- -[BWPreviewStitcherNode _renderCameraTransitionRampToPixelBuffer:bounds:withWiderCameraPixelBuffer:narrowerCameraPixelBuffer:zoomingIn:progress:narrowerCameraBounds:narrowerCameraShift:featherEdges:rampCameraTransition:renderEnhancedFeathering:narrowerCameraEdgeExpansionRamp:qsubToQsumEdgeOpacityRamp:qsubToQsumEdgeOpacityRampFromProgress:]
- -[BWRealtimeCinematographyNode _updateFromQueue:sampleBufferOut:captureID:]
- -[BWStillImageBufferRouterNode handleStillImagePrewarmWithSettings:forInput:]
- -[BWStillImageCaptureStreamSettings addAdaptiveUnifiedBracketedCaptureParams:preBracketFrameCaptureParams:bracketedCaptureFrameInfos:]
- -[BWStillImageCaptureStreamSettings initWithPortType:captureType:captureFlags:adaptiveBracketingParameters:sphereOffsets:]
- -[BWStillImageCoordinatorNode _renderSampleBuffer:forInput:attemptToCompleteRequest:]
- -[BWStillImageFilterNode handleStillImagePrewarmWithSettings:forInput:]
- -[BWStillImageFrameCoordinatorNode handleStillImagePrewarmWithSettings:forInput:]
- -[BWSubjectRelightingCalculator init]
- -[BWUBNode handleStillImagePrewarmWithSettings:forInput:]
- -[BWVariableFrameRateSelector _loadDefaultsWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:]
- -[BWVariableFrameRateSelector initWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:]
- -[CMCaptureLocalSessionController cinematicFramingVirtualCameraConfiguration]
- -[CMCaptureLocalSessionController supportedSourceFormats]
- -[CMInferenceUtils _getNetworkPath:isE5:embedPlatformDeviceID:fsNetworks:]
- -[CMInferenceUtils _getNetworkPathWithBasenamePredicate:isE5:embedPlatformDeviceID:fsNetworks:]
- -[CMInferenceUtils _getNetworkPathWithBasenamePredicate:isE5:embedPlatformDeviceID:fsNetworks:].cold.1
- -[CMInferenceUtils _getNetworkPathWithBasenamePredicate:isE5:embedPlatformDeviceID:fsNetworks:].cold.2
- -[CMInferenceUtils _getNetworkPathWithBasenamePredicate:isE5:embedPlatformDeviceID:fsNetworks:].cold.3
- -[CMInferenceUtils getNetworkPathForBasenamePredicate:isE5:]
- -[CMInferenceUtils getNetworkPathForBasenamePredicate:isE5:].cold.1
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:]
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.1
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.10
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.11
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.12
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.13
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.14
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.15
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.16
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.17
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.18
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.19
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.2
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.20
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.21
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.22
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.23
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.24
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.25
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.26
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.27
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.28
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.29
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.3
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.30
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.31
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.32
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.33
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.4
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.5
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.6
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.7
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.8
- -[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:].cold.9
- -[FigCaptureCameraSourcePipeline _buildVideoCaptureOutputNetwork:previewOutputsBySourceDeviceType:stillImageOutputsByPortType:lightSourceMaskOutputsBySourceDeviceType:keypointDescriptorDataOutputsBySourceDeviceType:pipelineConfiguration:graph:videoCaptureDimensions:numberOfSecondaryFramesToSkip:]
- -[FigCaptureCameraSourcePipeline initWithConfiguration:captureDevice:graph:name:renderDelegate:ispFastSwitchEnabled:error:]
- -[FigCaptureCameraSourcePipeline isLightSourceMaskAndKeypointDescriptorDataOnVideoCaptureOutputsEnabledForSourceDeviceType:]
- -[FigCaptureCameraSourcePipeline maxFrameRateClientOverride]
- -[FigCaptureCinematographyPipelineConfiguration setSmartStyleReversibilityEnabled:]
- -[FigCaptureCinematographyPipelineConfiguration smartStyleLearningEnabled]
- -[FigCapturePreviewSinkPipeline _metalCommandQueueWithName:priority:]
- -[FigCapturePreviewSinkPipeline _metalSubmissionAndCompletionQueue]
- -[FigCaptureSourceVideoFormat _geometricDistortionCorrectedFieldOfViewCropMultiplier]
- -[FigCaptureSourceVideoFormat clientMaxContinuousZoomFactorForDepthDataDelivery]
- -[FigCaptureStillImageSettings copyWithSwappedDimensions]
- -[FigCaptureVISPipeline _buildVISPipelineWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:visProcessingSemaphore:]
- -[FigCaptureVISPipeline _newVISNodeWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:pipelineStage:captureDevice:outputDimensions:irisVISCleanOutputRectOut:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:visProcessingSemaphore:]
- -[FigCaptureVISPipeline initWithUpstreamOutput:graph:name:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:visProcessingSemaphore:]
- GCC_except_table301
- GCC_except_table305
- GCC_except_table309
- GCC_except_table315
- GCC_except_table317
- GCC_except_table352
- GCC_except_table356
- GCC_except_table376
- GCC_except_table378
- GCC_except_table392
- GCC_except_table58
- GCC_except_table626
- GCC_except_table79
- GCC_except_table85
- _.compoundliteral.31
- _.compoundliteral.32
- _.compoundliteral.52
- _.compoundliteral.53
- _.compoundliteral.58
- _.compoundliteral.59
- _.compoundliteral.63
- _.compoundliteral.64
- _.compoundliteral.65
- _.compoundliteral.66
- _.compoundliteral.69
- _.compoundliteral.70
- _.compoundliteral.71
- _.compoundliteral.74
- _BWPhotonicEngineUtilitiesSmartStylesAttachedMediaKeysForPiecemealEncoding
- _OBJC_IVAR_$_BWBackgroundBlurNode._captureDevice
- _OBJC_IVAR_$_BWFigVideoCaptureDevice._attachCameraControlsStatisticsPrimaryPortType
- _OBJC_IVAR_$_BWPhotonicEngineNode._prewarming
- _OBJC_IVAR_$_BWPhotonicEngineNode._prewarmingLock
- _OBJC_IVAR_$_BWPreviewStitcherNode._metalSubmissionAndCompletionQueue
- _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._sourceDeviceTypesWithLightSourceMaskAndKeypointDescriptorDataEnabledOnVideoCaptureOutputs
- _OBJC_IVAR_$_FigCapturePreviewSinkPipeline._metalSubmissionAndCompletionQueue
- ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.368
- ___100-[BWPhotonicEngineNode processorController:didFinishProcessingSampleBuffer:type:processorInput:err:]_block_invoke.372
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.780
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.780.cold.1
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.781
- ___104-[BWPhotonicEngineNode _setupProcessingStateForInferenceWithSettings:portType:inferenceInputBufferType:]_block_invoke.790
- ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.720
- ___108-[BWPhotonicEngineNode _setupProcessingStateForDeepZoomWithSettings:sequenceNumber:portType:processingPlan:]_block_invoke.720.cold.1
- ___108-[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:]_block_invoke
- ___115-[BWPhotoEncoderController inputReceivedNewAuxMedia:auxSbuf:attachedMediaKey:primaryImageMetadata:processingFlags:]_block_invoke
- ___133-[BWInferenceScheduler _processJobsFromFramebuffer:usingInputSampleBuffer:inferencePropagationHandler:atExecutionTime:forConnection:]_block_invoke.120
- ___133-[BWInferenceScheduler _processJobsFromFramebuffer:usingInputSampleBuffer:inferencePropagationHandler:atExecutionTime:forConnection:]_block_invoke.120.cold.1
- ___137-[BWInferenceScheduler performInferencesForConnection:usingInputSampleBuffer:attachingResultsToSampleBuffer:skippingInferencesWithTypes:]_block_invoke.108
- ___137-[BWInferenceScheduler performInferencesForConnection:usingInputSampleBuffer:attachingResultsToSampleBuffer:skippingInferencesWithTypes:]_block_invoke_2.109
- ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.746
- ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.746.cold.1
- ___138-[BWPhotonicEngineNode _setupProcessingStateForScalerIfNeededWithSettings:sequenceNumber:portType:preNoiseReductionScaler:processingPlan:]_block_invoke.746.cold.2
- ___165-[BWCameraStreamingMonitor _updateCameraStreamingMonitorInfoWithStreaming:cameraAccessGranted:clientAuditToken:tccIdentity:updateStreamingStatus:updateAccessStatus:]_block_invoke.46
- ___165-[BWCameraStreamingMonitor _updateCameraStreamingMonitorInfoWithStreaming:cameraAccessGranted:clientAuditToken:tccIdentity:updateStreamingStatus:updateAccessStatus:]_block_invoke_2.47
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.1061
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.1087
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.727
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.885
- ___334-[FigCapturePhotonicEngineSinkPipeline _buildStillImageSinkPipelineWithConfiguration:captureDevice:sourceOutputsByPortType:sourceSensorRawOutputsByPortType:highResStillImageDimensions:supplementalPointCloudCaptureDevice:supplementalPointCloudSourceOutput:captureStatusDelegate:inferenceScheduler:cinematicFramingStatesProvider:graph:]_block_invoke.907
- ___40-[BWPhotoEncoderController _processSbuf]_block_invoke.258
- ___47-[BWPhotonicEngineNode _ubInferenceInputRouter]_block_invoke.878
- ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.393
- ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.394
- ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.400
- ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.368
- ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.371
- ___57-[BWUBNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke
- ___57-[BWUBNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke.149
- ___62-[BWFigVideoCaptureDevice _setupStillImageCaptureStateMachine]_block_invoke.590
- ___62-[BWFigVideoCaptureDevice _setupStillImageCaptureStateMachine]_block_invoke.593
- ___68-[BWFigVideoCaptureDevice _suspendTimeMachineWithCompletionHandler:]_block_invoke.557
- ___69-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke
- ___69-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke.309
- ___69-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke.310
- ___69-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke.319
- ___69-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke_2
- ___70-[BWPhotoEncoderController prepareForCurrentConfigurationToBecomeLive]_block_invoke.223
- ___71-[BWStillImageFilterNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke
- ___73-[BWPhotonicEngineNode _handleClientBracketFrameEmissionForSampleBuffer:]_block_invoke.464
- ___74-[CMInferenceUtils _getNetworkPath:isE5:embedPlatformDeviceID:fsNetworks:]_block_invoke
- ___75-[BWCompressedShotBufferNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke
- ___80-[BWFigVideoCaptureDevice _sendInitialValuesToPortraitEffectPropertiesDelegate:]_block_invoke.1061
- ___80-[BWFigVideoCaptureDevice _updateStateUsingVideoSampleBuffer:fromCaptureStream:]_block_invoke.310
- ___80-[BWFigVideoCaptureDevice _updateStateUsingVideoSampleBuffer:fromCaptureStream:]_block_invoke.310.cold.1
- ___80-[BWFigVideoCaptureDevice _updateStateUsingVideoSampleBuffer:fromCaptureStream:]_block_invoke.312
- ___85-[BWStillImageCoordinatorNode _renderSampleBuffer:forInput:attemptToCompleteRequest:]_block_invoke
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.640
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.640.cold.1
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.641
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.641.cold.1
- ___88-[BWPhotonicEngineNode _setupProcessingStateForFlashCaptureWithSettings:processingPlan:]_block_invoke.641.cold.2
- ___91-[BWPhotonicEngineNode _processRawErrorRecoveryFrameWithNRFProcessorInput:failureMetadata:]_block_invoke
- ___91-[BWPhotonicEngineNode _processRawErrorRecoveryFrameWithNRFProcessorInput:failureMetadata:]_block_invoke.cold.1
- ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.632
- ___94-[BWPhotonicEngineNode _setupProcessingStateForSingleImageCaptureWithSettings:processingPlan:]_block_invoke.632.cold.1
- ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.683
- ___97-[BWPhotonicEngineNode _setupProcessingStateForColorConstancyCaptureWithSettings:processingPlan:]_block_invoke.683.cold.1
- ___block_descriptor_32_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8l
- ___block_descriptor_33_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8l
- ___block_descriptor_40_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8l
- ___block_descriptor_40_e8_32o_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8ls32l8
- ___block_descriptor_40_e8_32r_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8lr32l8
- ___block_descriptor_40_e8_32s_e18_B16?0"NSString"8ls32l8
- ___block_descriptor_48_e8_32o40r_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8ls32l8r40l8
- ___block_descriptor_48_e8_32o_e79_B48?0"ADEspressoImageDescriptor"8I16B20"NSString"24"NSString"32"NSArray"40ls32l8
- ___block_descriptor_48_e8_32r40r_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8lr32l8r40l8
- ___block_descriptor_48_e8_32r_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8lr32l8
- ___block_descriptor_56_e8_32o40r48r_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8lr40l8s32l8r48l8
- ___block_descriptor_56_e8_32o40r_e150_i16?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}q^{__CFString}i^{OpaqueFigCaptureSource}fi^{OpaqueFigFlashlight}iBBBBB}8lr40l8s32l8
- ___block_descriptor_64_e40_v16?0"STMutableMediaStatusDomainData"8l
- ___block_descriptor_64_e8_32o40o48o56r_e32_v16?0"UNNotificationSettings"8ls32l8s40l8s48l8r56l8
- ___block_descriptor_tmp.100
- ___block_descriptor_tmp.102
- ___block_descriptor_tmp.49
- ___block_descriptor_tmp.56
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.69
- ___block_descriptor_tmp.91
- ___block_descriptor_tmp.97
- ___block_descriptor_tmp.98
- ___block_literal_global.1243
- ___block_literal_global.1272
- ___block_literal_global.1318
- ___block_literal_global.132
- ___block_literal_global.1344
- ___block_literal_global.1356
- ___block_literal_global.136
- ___block_literal_global.1360
- ___block_literal_global.1373
- ___block_literal_global.1385
- ___block_literal_global.1390
- ___block_literal_global.1395
- ___block_literal_global.1438
- ___block_literal_global.144
- ___block_literal_global.157
- ___block_literal_global.170
- ___block_literal_global.195
- ___block_literal_global.244
- ___block_literal_global.267
- ___block_literal_global.274
- ___block_literal_global.284
- ___block_literal_global.307
- ___block_literal_global.310
- ___block_literal_global.423
- ___block_literal_global.445
- ___block_literal_global.503
- ___block_literal_global.550
- ___block_literal_global.585
- ___block_literal_global.587
- ___block_literal_global.589
- ___block_literal_global.592
- ___block_literal_global.596
- ___block_literal_global.604
- ___block_literal_global.653
- ___block_literal_global.658
- ___block_literal_global.67
- ___block_literal_global.692
- ___block_literal_global.703
- ___block_literal_global.731
- ___block_literal_global.745
- ___block_literal_global.748
- ___block_literal_global.752
- ___block_literal_global.754
- ___block_literal_global.756
- ___block_literal_global.758
- ___block_literal_global.760
- ___block_literal_global.762
- ___block_literal_global.764
- ___block_literal_global.846
- ___block_literal_global.856
- ___captureSession_Invalidate_block_invoke.1328
- ___captureSession_IrisStillImageSinkCancelMomentCapture_block_invoke.1435
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToMovieRecording_block_invoke.1433
- ___captureSession_IrisStillImageSinkCommitMomentCaptureToStillImageCapture_block_invoke.1428
- ___captureSession_IrisStillImageSinkEndMomentCapture_block_invoke.1436
- ___captureSession_SetConfiguration_block_invoke.1370
- ___captureSession_SetSectionProperty_block_invoke.1351
- ___captureSession_SetSectionProperty_block_invoke.1352
- ___captureSession_SetSectionProperty_block_invoke.1358
- ___captureSession_startDeferredGraphSetupOnWorkerQueueAfter_block_invoke.1253
- ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke.1195
- ___captureSession_startMonitoringAudioPlaybackAndRouteChangeNotifications_block_invoke_2.1196
- ___captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke.1166
- ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1290
- ___captureSession_updateSessionStateWithApplicationAndLayoutState_block_invoke.1300
- ___csu_createVideoCaptureSourceAttributesForStreamsContainer_block_invoke
- ___fcru_promptOpenTapToRadar_block_invoke.72
- ___nrfp_createStateMachine_block_invoke.746
- ___rqReceiverSetSource_block_invoke.101
- ___rqSenderFinalize_block_invoke.57
- ___ubp_createStateMachine_block_invoke.539
- _captureSession_SetSectionProperty.onceToken.1353
- _captureSession_teardownGraph.cold.1
- _captureSession_teardownGraph.cold.2
- _captureSession_teardownGraph.cold.3
- _csu_createVideoCaptureSourceAttributesForStreamsContainer.onceToken
- _e5rt_execution_stream_operation_create_precompiled_compute_operation
- _objc_msgSend$_encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:usedContainerOptionsOut:usedEncodingOptionsOut:mainImageHandleInOut:
- _objc_msgSend$_getNetworkPath:isE5:embedPlatformDeviceID:fsNetworks:
- _objc_msgSend$_getNetworkPathWithBasenamePredicate:isE5:embedPlatformDeviceID:fsNetworks:
- _objc_msgSend$addAdaptiveUnifiedBracketedCaptureParams:preBracketFrameCaptureParams:bracketedCaptureFrameInfos:
- _objc_msgSend$addAuxSbuf:attachedMediakey:primaryImageMetadata:processingFlags:
- _objc_msgSend$cameraCaptureAttributions
- _objc_msgSend$clientMaxContinuousZoomFactorForDepthDataDelivery
- _objc_msgSend$copyWithSwappedDimensions
- _objc_msgSend$didChangeDeskViewCameraZoomFactor:
- _objc_msgSend$emitStillImagePrewarmMessageWithSettings:
- _objc_msgSend$enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:
- _objc_msgSend$frameParametersWithIntegrationTimeInSeconds:gain:maxAGC:
- _objc_msgSend$handleStillImagePrewarmWithSettings:forInput:
- _objc_msgSend$initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:
- _objc_msgSend$initWithFigCaptureISPProcessingSession:
- _objc_msgSend$initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:
- _objc_msgSend$initWithPortType:captureType:captureFlags:adaptiveBracketingParameters:sphereOffsets:
- _objc_msgSend$initWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:
- _objc_msgSend$inputReceivedNewAuxMedia:auxSbuf:attachedMediaKey:primaryImageMetadata:processingFlags:
- _objc_msgSend$inputReceivedProcessedRawErrorRecoveryFrame:
- _objc_msgSend$integrationTimeInMiroseconds
- _objc_msgSend$isLensSmudgeDetectionSupported
- _objc_msgSend$newMessageWithStillImageSettings:
- _objc_msgSend$processorController:processRawErrorRecoveryFrameForProcessorInput:failureMetadata:
- _objc_msgSend$removeCameraCaptureAttribution:
- _objc_msgSend$setProcessedRawErrorRecoveryFrame:
- _objc_msgSend$stashedAttacheMediaSampleBuffersByAttachedMediaKey
- _objc_msgSend$supportsCroppingDepthToPrimaryCaptureAspectRatio
- _os_release
- _os_retain
CStrings:
+ "\n..."
+ "  Identifier: %@ -> [Registered resource]\n"
+ "  ZSL failure: %@\n"
+ " with capture settings ID '%lld'"
+ "! CGRectIsNull( rawDenormalizedActiveRect )"
+ "%@\n\n"
+ "%@ | Networks Using E5ANEMemoryProvider: %@"
+ "%@%@\n  Flags: %@\n  %@\n%@"
+ "%@: %p: created pixel transfer session %@"
+ "%s %s: %s"
+ "( outputIndex > -1 ) && ( outputIndex < 22 )"
+ "+[BWVideoDepthInferenceConfiguration pceDisparityColorInferenceDescriptorForVideoDepthLayout:inputSource:]"
+ "-[BWAudioRemixAnalysisMetadataNode _sendRemixMetadataSampleBuffer]"
+ "-[BWE5InferenceProvider _prepareWithSharedANEMemoryProvider:]"
+ "-[BWE5InferenceProvider prewarmUsingLimitedMemory:]"
+ "-[BWE5InferenceProvider prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:]"
+ "-[BWE5MultipleLayoutInferenceProvider _prepareWithSharedANEMemoryProvider:]"
+ "-[BWE5MultipleLayoutInferenceProvider prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:]"
+ "-[BWFigCaptureDeviceVendor _updateTofAFEstimatorResultsForStream:totalStreamingDuration:]"
+ "-[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:type:]"
+ "-[BWFigVideoCaptureDevice _configureZoomFudgingWithAspectRatio:]"
+ "-[BWFigVideoCaptureDevice _ubAdaptiveStillImageCaptureSettingsWithSettings:userInitiatedRequestPTS:captureType:captureFlags:sceneFlags:frameStatisticsByPortType:metadata:]"
+ "-[BWFigVideoCaptureDevice _ubUpdateCurrentAdaptiveBracketedCaptureParamsForCaptureStreamSettings:frameStatistics:timeMachineFrameSelection:]"
+ "-[BWFigVideoCaptureDevice setDeskViewAutoExposureAreaOfInterest:]_block_invoke"
+ "-[BWFigVideoCaptureDevice setRegionOfInterestWithoutOverscan:]_block_invoke"
+ "-[BWInferenceEngine _configureInferenceCachingPolicyForEligibleAdapters:]"
+ "-[BWInferenceSchedulerInference prepareForExecutionWithSharedANEMemoryProvider:]"
+ "-[BWInferenceSchedulerInference prepareForExecution]"
+ "-[BWInferenceSchedulerInference prepareForSubmissionWithWorkQueue:]"
+ "-[BWInferenceSchedulerInference prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:]"
+ "-[BWInferenceSchedulerInference sharedResourceType]"
+ "-[BWInferenceSharedE5ANEMemoryProvider completeANEMemoryProviderCreationForNetwork:wasSuccessful:]"
+ "-[BWInferenceSharedE5ANEMemoryProvider fetchANEMemoryProviderForNetwork:]"
+ "-[BWInferenceSharedE5ANEMemoryProvider registerANEMemoryProvider:forNetwork:]"
+ "-[BWInferenceSharedResourceManager _purgeAllSharedResources]"
+ "-[BWInferenceSharedResourceManager retrieveSharedResourceForResourceCategoryAndLockIfNotAvailable:]"
+ "-[BWIrisStagingNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:inferenceScheduler:]"
+ "-[BWLearnedMattingInferenceProvider reconcileWithPlaceholderProvider:]"
+ "-[BWMultiStreamCameraSourceNode _updateZoomForOutputIndex:sampleBuffer:additionalScaleFactor:deliverSushiRaw:]"
+ "-[BWNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:]"
+ "-[BWNRFProcessorController inputReceivedProcessedRawErrorRecoveryFrame:proxy:]"
+ "-[BWNRFProcessorInput setKeepFrames:]"
+ "-[BWNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]"
+ "-[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:]"
+ "-[BWPhotoEncoderController inputReceivedSbufForPiecemealEncoding:sbuf:attachedMediaKey:primaryImageMetadata:processingFlags:]_block_invoke"
+ "-[BWPhotoEncoderControllerInput addSbufForPiecemealEncoding:attachedMediakey:primaryImageMetadata:processingFlags:]"
+ "-[BWPhotoEncoderNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]"
+ "-[BWPhotonicEngineNode _processRawErrorRecoveryFrameWithNRFProcessorInput:processErrorRecoveryProxy:failureMetadata:]"
+ "-[BWPhotonicEngineNode _propagateSushiRawDNGDictionaryWithOutputSampleBuffer:requestedDimensions:aspectRatio:gdcRequested:]"
+ "-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]"
+ "-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke"
+ "-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke_2"
+ "-[BWPiecemealEncodingNode renderSampleBuffer:forInput:]"
+ "-[BWPreviewStabilizationNode initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:minimumSupportedUIZoomFactor:]"
+ "-[BWPreviewStitcherNode _renderCameraTransitionRampToPixelBuffer:bounds:withWiderCameraPixelBuffer:narrowerCameraPixelBuffer:zoomingIn:progress:narrowerCameraBounds:narrowerCameraShift:featherEdges:rampCameraTransition:renderEnhancedFeathering:narrowerCameraEdgeExpansionRamp:qsubToQsumEdgeOpacityRamp:qsubToQsumEdgeOpacityRampFromProgress:renderBrightnessCompensation:]"
+ "-[BWQuickTimeMovieFileSinkNode _collectVideoDeghostingStatisticsFromDictionary:]"
+ "-[BWSmartStyleRenderingProcessorController _getDenormalizedFinalCropRectFromSourceForPixelBuffer:metadata:]"
+ "-[BWStillImageCaptureStreamSettings adaptiveBracketingFrameParametersForFrame:]"
+ "-[BWStillImageCaptureStreamSettings addAdaptiveBracketingMetadataIfNeededForFrame:]"
+ "-[BWTemporalFilterNode didReachEndOfDataForInput:]_block_invoke"
+ "-[BWTiledEspressoInferenceProvider reconcileWithPlaceholderProvider:]"
+ "-[BWUBNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]"
+ "-[BWUBNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:]_block_invoke"
+ "-[BWVISNode setIspProcessingSession:]"
+ "-[BWVariableFrameRateSelector _loadDefaultsWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:teleAutoVideoFrameRateAllows24FPS:]"
+ "-[BWVideoDepthNode initWithInferenceScheduler:captureDevice:videoDepthConfiguration:extraDepthOutputRetainedBufferCount:error:]"
+ "-[BWVideoProcessingInferenceAdapter _generateInferenceProviderCacheKeyWithAttributes:]"
+ "-[BWVideoProcessingInferenceAdapter _newInferenceProviderWithType:analysisType:executionTarget:configuration:preventionReasons:resourceProvider:additionalCacheAttributes:]"
+ "-[BWVideoProcessingInferenceAdapter inferenceProviderForType:version:configuration:resourceProvider:status:]"
+ "-[BWVideoProcessingInferenceProvider executeOnSampleBuffer:usingStorage:withExecutionTime:completionHandler:]"
+ "-[BWVideoProcessingInferenceProvider prepareForExecution]"
+ "-[BWVideoProcessingInferenceProvider prepareForSubmissionWithWorkQueue:]"
+ "-[BWVideoProcessingInferenceProvider reconcileWithPlaceholderProvider:]"
+ "-[BWVideoProcessingInferenceProvider submitForSampleBuffer:usingStorage:withSubmissionTime:workQueue:completionHandler:]"
+ "-[CMInferenceUtils _getNetworkPath:isE5:fsNetworks:]"
+ "-[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:rtscProcessorsBySourceDeviceType:]"
+ "-[FigCaptureCameraSourcePipeline _buildVideoCaptureOutputNetwork:previewOutputsBySourceDeviceType:stillImageOutputsByPortType:lightSourceMaskOutputsBySourceDeviceType:keypointDescriptorDataOutputsBySourceDeviceType:pipelineConfiguration:graph:videoCaptureDimensions:numberOfSecondaryFramesToSkip:rtscProcessorsBySourceDeviceType:]"
+ "-[FigCaptureCameraSourcePipeline initWithConfiguration:captureDevice:graph:name:renderDelegate:ispFastSwitchEnabled:rtscProcessorsBySourceDeviceType:error:]"
+ "-[FigCaptureVISPipeline _buildVISPipelineWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:videoGreenGhostOfflineMetadataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:visProcessingSemaphore:]"
+ ".E5.espresso.bundle"
+ ".espresso.net"
+ ".metal-completion-queue"
+ ".metal-submission-queue"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/CMCaptureGestaltUtilities.m %s: %@ AVFCapture bringup default overrides %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigRemoteQueue/FigRemoteQueue.m"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Espresso/E5/BWE5InferenceProvider.m"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Portrait/BWVideoDepthInferenceConfiguration.m %s: Failed to get an ADPCEDisparityColorInferenceDescriptor"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Portrait/BWVideoDepthInferenceConfiguration.m %s: Unknown videoDepthLayout %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Portrait/BWVideoDepthInferenceConfiguration.m %s: inputSource %lu exceeds max index %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Portrait/BWVideoDepthInferenceConfiguration.m %s: videoDepthLayout %d exceeds max index %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPiecemealEncodingNode.m"
+ "/System/Library/ImagingNetworks"
+ "0b375d5ed4492d4d99ab68a3739d0791bdbe51b3"
+ "1598312"
+ "23:44:01"
+ "24995aa5493516159e61853986ebe7769210ed10"
+ "<%@ %p> deviceOriented:%d applyHorizontalFlip:%d videoContentMode:%ld includesInvalidContent:%ld cropDescriptor:%@ underlyingVideoFormat:%@ rotationDegrees:%d landscapeOriented:%d"
+ "<%@ %p>: captureID:%lld, captureType=%@, %@, errorRecovery=%d errorRecoveryProxy=%d original=%d tonemap=%d inferenceInput=%d semanticRendering=%d inferenceInputForProcessing=%d inferences=%d input:<%@ %p>"
+ "<<<< BWAudioRemixAnalysisMetadataNode >>>> %s: back from finishAndGetResultsBlockingWithStartingPTS:%.4lf andEndingPTS:%.4lf"
+ "<<<< BWAudioRemixAnalysisMetadataNode >>>> %s: calling finishAndGetResultsBlockingWithStartingPTS:%.4lf andEndingPTS:%.4lf"
+ "<<<< BWBackgroundBlurNode >>>> %s: %@ is EOD for configurationID: %@"
+ "<<<< BWBravoStreamSelector >>>>"
+ "<<<< BWBravoStreamSelector >>>> %s: %@"
+ "<<<< BWBravoStreamSelector >>>> %s: %@%s"
+ "<<<< BWCameraStreamingMonitor >>>> %s: Send camera streaming OFF message to SystemStatus"
+ "<<<< BWDeepFusionProcessorController >>>> %s: Low res glasses mask available: %@"
+ "<<<< BWDeepFusionProcessorController >>>> %s: No low res glasses mask available."
+ "<<<< BWDeepZoomInferenceProvider >>>> %s: scalerZoomFactor (%f,%f) is unexpectedly unachieveable"
+ "<<<< BWDeepZoomProcessorController >>>> %s: Deep Zoom was not possible, err = %d, fallback and emit the input buffer instead (%@), still image scaler will perform the required zoom."
+ "<<<< BWE5InferenceProvider >>>> %s: Cannot cache provider %@ with custom identifier %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
+ "<<<< BWE5InferenceProvider >>>> %s: Failed to register an ANE E5RT Memory Provider for network:(%@) continuing preparation without it"
+ "<<<< BWE5InferenceProvider >>>> %s: Inference pipeline has unexpectedly fallen back to the legacy prewarming path for provider <%@> of type: %@ and will not be set up to share ANEF intra-backend memory buffers across E5RT executions during this invocation for this provider. This should not have occured."
+ "<<<< BWE5InferenceProvider >>>> %s: Inference pipeline has unexpectedly fallen back to the legacy prewarming path for provider <%@> of type: %@ and will not be set up to share ANEF intra-backend memory buffers across this E5RT execution during this invocation for this provider. This should not have occured. Filed a bug to the CameraCapture Inference | All component."
+ "<<<< BWE5InferenceProvider >>>> %s: Prewarming provider <%@> of type: %@ being prewarmed with limitedMemory: %d and E5RT shared memory resource: %@"
+ "<<<< BWE5InferenceProvider >>>> %s: Provider <%@> of type: %@ created a brand new E5RT memory provider and registered it with the shared E5RT Memory Provider: %@"
+ "<<<< BWE5InferenceProvider >>>> %s: Provider <%@> of type: %@ reused E5RT memory provider from the shared E5RT Memory Provider: %@"
+ "<<<< BWE5InferenceProvider >>>> Fig"
+ "<<<< BWE5MultipleLayoutInferenceProvider >>>> %s: Cannot cache provider %@ with custom identifier %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
+ "<<<< BWE5MultipleLayoutInferenceProvider >>>> %s: Failed to register an ANE E5RT Memory Provider for network:(%@) continuing preparation without it"
+ "<<<< BWE5MultipleLayoutInferenceProvider >>>> %s: Prewarming provider <%@> of type: %@ being prewarmed with limitedMemory: %d and E5RT shared memory resource: %@"
+ "<<<< BWE5MultipleLayoutInferenceProvider >>>> %s: Provider <%@> of type: %@ created a brand new E5RT memory provider and registered it with the shared E5RT Memory Provider: %@"
+ "<<<< BWE5MultipleLayoutInferenceProvider >>>> %s: Provider <%@> of type: %@ reused E5RT memory provider from the shared E5RT Memory Provider: %@"
+ "<<<< BWEspressoInferenceAdapter >>>> %s: Failed to get an ADPCEDisparityColorInferenceDescriptor"
+ "<<<< BWEspressoInferenceProvider >>>> %s: Cannot cache provider %@ with custom identifier %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: %@ tofAFEstimatorResults %@"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Digital Flash total exposure time: %f"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Found '%@' reference frame using method '%d'. ReferenceFrameIndex: %d. SIFRReferenceFrameIndex:%d. Selected range: %d-%d (%d-%d)"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Setting fusion face detection AE ROI to [x:%.3f,y:%.3f,w:%.3f,h:%.3f]"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Zero Shutter Lag capture failed due to '%{public}@'"
+ "<<<< BWFigVideoCaptureStream >>>> %s: %@: Not setting max exposure duration. Relying on stream default. "
+ "<<<< BWFigVideoCaptureStream >>>> %s: %@: Setting max exposure duration to %lld/%ds, %.1fms"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Can't update max exposure duration before streaming starts. Ignoring."
+ "<<<< BWFigVideoCaptureStream >>>> %s: Frame with PTS '%.3f' is (partially) invalid due to loss of sensor access (reason: %@)"
+ "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Created with priority: %d, state transition timeout: %d seconds"
+ "<<<< BWInferenceEngine >>>> %s: All eligible inference adapters on the engine have been configured with the caching policy"
+ "<<<< BWInferenceEngine >>>> %s: Configured <%@: %@> inference provider caching state to :%d"
+ "<<<< BWInferenceEngine >>>> %s: Configuring eligible inference adapters on the engine with the caching policy: shouldAdapterCacheInferences:%d"
+ "<<<< BWInferenceEngine >>>> %s: Failed to prewarm inference provider %@ of type: %@"
+ "<<<< BWInferenceEngine >>>> %s: Prewarming provider <%@> of type: %@ using prewarm mechanism: %@"
+ "<<<< BWInferenceScalingRequirement >>>> %s: Attempting to control height dimension for intermediate with integer factor: %zu total height: %zu"
+ "<<<< BWInferenceScalingRequirement >>>> %s: Overriding calculated sequential intermediate format dimensions from (%zux%zu) to (%dx%d)"
+ "<<<< BWInferenceSchedulerInference >>>> %s: Inference scheduler attempted to call preparation on a provider that didn't advertise itself as executable. Hence this job will not be prepared so the pipeline will not produce inferences for type:(%@)"
+ "<<<< BWInferenceSchedulerInference >>>> %s: Inference scheduler attempted to call preparation on a provider that didn't advertise itself as sharedResourcePreparator. Hence this job will not be prepared so the pipeline will not produce inferences for type:(%@)"
+ "<<<< BWInferenceSchedulerInference >>>> %s: Inference scheduler attempted to call preparation on a provider that didn't advertise itself as submittable. Hence this job will not be prepared so the pipeline will not produce inferences for type:(%@)"
+ "<<<< BWInferenceSchedulerInference >>>> %s: Inference scheduler attempted to call the executable preparation scheme on a provider that didn't advertise itself as sharedResourcePreparator. Hence this job will not be prepared so the pipeline will not produce inferences for type:(%@)"
+ "<<<< BWInferenceSchedulerInference >>>> %s: Inference scheduler attempted to call the submittable preparation scheme on a provider that didn't advertise itself as sharedResourcePreparator. Hence this job will not be prepared so the pipeline will not produce inferences for type:(%@)"
+ "<<<< BWInferenceSharedE5ANEMemoryProvider >>>> %s: <%@> missing resource category type"
+ "<<<< BWInferenceSharedE5ANEMemoryProvider >>>> %s: E5 Network %@ intra-backend intermediates are being reused through E5 ANE memory provider"
+ "<<<< BWInferenceSharedE5ANEMemoryProvider >>>> %s: E5 Network %@ now registered to share intra-backend intermediates through E5 ANE memory provider"
+ "<<<< BWInferenceSharedE5ANEMemoryProvider >>>> %s: Missing E5 ANE memory provider for network %@"
+ "<<<< BWInferenceSharedE5ANEMemoryProvider >>>> %s: Missing network name while attempting to fetch the E5 ANE memory provider"
+ "<<<< BWInferenceSharedE5ANEMemoryProvider >>>> %s: Resource manager did not have a shared resource for resource category %@"
+ "<<<< BWInferenceSharedResourceManager >>>> %s: Shared resource manager cleaning up all shared resouces it is currently tracking"
+ "<<<< BWInferenceSharedResourceManager >>>> %s: Shared resource manager retrieves resource: %@ for category %@"
+ "<<<< BWInferenceSharedResourceManager >>>> %s: The first designated thread successfully created the resource, allowing other threads who were racing with the designator earlier to just retrieve the resource now"
+ "<<<< BWInferenceSharedResourceManager >>>> %s: The previous designated thread responsible for creating the resource failed to do so, allowing other threads to become the designated creator thread"
+ "<<<< BWInferenceVideoScalingProvider >>>> %s: Inference video scaling provider given pixel buffer with size (w:%f h:%f) exceeding attached valid rect size (w:%f h:%f) but not configured to apply a crop, attempting to get to output video format:(%@)"
+ "<<<< BWLearnedMattingInferenceProvider >>>> %s: Cannot cache provider %@ with custom identifier %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
+ "<<<< BWLearnedMattingInferenceProvider >>>> %s: Cannot cache provider %@ with type %@ as its type does not match the placeholder provider %@ with type :%@ we are trying to move requirements from"
+ "<<<< BWMattingV2InferenceProvider >>>> %s: Cannot cache provider %@ with custom identifier %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: %@: Node output %@ streaming : %d retainedBufferCount = %d"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: %{public}@: %@ %@ %lld / %d"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: %{public}@: Discontinuity! %@ %.3f"
+ "<<<< BWNRFProcessorController >>>> %s: Ignoring input received processed raw as not processing the error recovery %s for '%@"
+ "<<<< BWNRFProcessorController >>>> %s: Keep frames has been set to NO. Releasing frames:%lu"
+ "<<<< BWNRFProcessorController >>>> %s: No glasses mask returned by semantic segmentation."
+ "<<<< BWNRFProcessorController >>>> %s: Providing glasses mask to NRF processor: %@"
+ "<<<< BWNRFProcessorController >>>> %s: Set error recovery frame '%@' for %@"
+ "<<<< BWNRFProcessorController >>>> %s: Setting 'maximumNumberOfReferenceFrameCandidatesToHoldForProcessing' to '%d' (ZSL:%d)"
+ "<<<< BWPhotoEncoderNode >>>> %s: Received sbuf for captureID:%{public}lld (identifier:%{private}@) while processing capture with identifier:%{private}@, flushing current input. This is not fatal but should be extremely rare."
+ "<<<< BWPhotoEncoderUtilities >>>> %s: Piecemeal encoding is only supported for smart style captures"
+ "<<<< BWPhotoEncoderUtilities >>>> %s: Piecemeal encoding not supported for constituent captures"
+ "<<<< BWPhotoEncoderUtilities >>>> %s: Piecemeal encoding not supported for raw captures"
+ "<<<< BWPiecemealEncodingNode >>>> %s: Attempting piecemeal encoding of primary image for: %@"
+ "<<<< BWPiecemealEncodingNode >>>> %s: Failed to get metadata from primary sbuf"
+ "<<<< BWPiecemealEncodingNode >>>> %s: Failed to get still image settings from primary sbuf"
+ "<<<< BWPiecemealEncodingNode >>>> %s: Failed to handle input image for captureID:%lld, client will not get an image back (err: %d)"
+ "<<<< BWPiecemealEncodingNode >>>> %s: No photo encoder controller available for piecemeal encoding"
+ "<<<< BWPiecemealEncodingNode >>>> %s: No photo encoder controller input available for piecemeal encoding"
+ "<<<< BWPiecemealEncodingNode >>>> %s: No primary sbuf for piecemeal encoding"
+ "<<<< BWPiecemealEncodingNode >>>> %s: Piecemeal encoding is not supported for settings %@"
+ "<<<< BWPiecemealEncodingNode >>>> %s: Piecemeal encoding the %@: %@ with encoderControllerInput: %@"
+ "<<<< BWPiecemealEncodingNode >>>> %s: Piecemeal encoding the Primary image %@ with encoderControllerInput: %@,"
+ "<<<< BWPiecemealEncodingNode >>>> %s: Standard res deep fusion frame is not encoded as primary image for: %@"
+ "<<<< BWPiecemealEncodingNode >>>> %s: Unstyled frame is not encoded as primary image for: %@"
+ "<<<< BWPiecemealEncodingNode >>>> %s: non processed reference frame is not encoded as primary image for: %@"
+ "<<<< BWPiecemealEncodingNode >>>> %s: portType %@ doesn't match primary portType %@, not eligible for piecemeal encoding"
+ "<<<< BWPixelTransferNode >>>> %s: %@"
+ "<<<< BWPixelTransferNode >>>> %s: %@%s"
+ "<<<< BWPreviewStitcherNode >>>> %s: Adjusting brightness of narrower camera to match wider camera"
+ "<<<< BWPreviewStitcherNode >>>> %s: Adjusting brightness of wider camera to match narrower camera"
+ "<<<< BWPreviewStitcherNode >>>> %s: Cleared camera transition ramp up because totalZoom dropped below narrowerCameraBaseZoomFactor"
+ "<<<< BWPreviewStitcherNode >>>> %s: Dropping preview frame due to preview stitcher backpressure"
+ "<<<< BWPreviewStitcherNode >>>> %s: Dropping preview stitcher frame until output connection is resumed"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: ignoring settings max file duration of %lf seconds"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: VideoDeghostingStatistics: %@"
+ "<<<< BWSmartStyleLearningNode >>>> %s: Error checking supported ISP processing session types: %d"
+ "<<<< BWStillImageCaptureSettings >>>> %s: Failed to compute gain for '%@' (err:%d)"
+ "<<<< BWStillImageCaptureSettings >>>> %s: Failed to find adaptive frame parameters for '%@'"
+ "<<<< BWStillImageCaptureSettings >>>> %s: Missing capture frame infos"
+ "<<<< BWStillImageCaptureSettings >>>> %s: TM%i: Changed ispDGain from '%f / %d' (ET:%f, EIT:%f) to '%f / %d' (EIT:%f, Adaptive Bracketing ET:%f, EIT:%f, EV0Ratio:%f)"
+ "<<<< BWStillImageCaptureSettings >>>> %s: The number of frame parameters and capture frame infos for adaptive bracketing group '%d' does not match"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: Missing settings in BWStillImageCoordinatorAddAttachmentsToSampleBuffer()%@"
+ "<<<< BWStillImageFrameCoordinatorNode >>>> %s: Overriding FinalCropRect %@ with %@ for captureID:%lld"
+ "<<<< BWStillImageFrameCoordinatorNode >>>> %s: Overriding MinimumValidBufferRectForGDC %@ with %@ for captureID:%lld"
+ "<<<< BWStillImageFrameCoordinatorNode >>>> %s: Updated FinalCropRect is larger than ValidBufferRect (%{public}@ vs. %{public}@), processing might produce corrupted photos for captureID:%{public}lld"
+ "<<<< BWStillImageFrameCoordinatorNode >>>> %s: Updated MinimumValidBufferRectForGDC is larger than ValidBufferRect (%{public}@ vs. %{public}@), processing might produce corrupted photos for captureID:%{public}lld"
+ "<<<< BWStillImageMetadataUtilities >>>> %s: Optical center = %@"
+ "<<<< BWStillImageMetadataUtilities >>>> %s: SushiRAW DNG dictionary requested with rawDimensions:%@, rawPixelFormat:%@, requestedDimensions:%@, sushiRawBlackBorderingEnabled:%d, gdcRequested:%d, quadraBinningFactor:%d"
+ "<<<< BWStillImageMetadataUtilities >>>> %s: WarpRectilinear2 = %@"
+ "<<<< BWStillImageMetadataUtilities >>>> %s: coeffs[%d] = %.2f"
+ "<<<< BWStillImageMetadataUtilities >>>> %s: cropZoomScale: %.2f"
+ "<<<< BWStillImageProcessing >>>> %s: Failed to get inputLinearROIRect for captureID:%lld"
+ "<<<< BWStillImageProcessing >>>> %s: Piecemeal encoding is not supported for settings %@"
+ "<<<< BWStillImageProcessing >>>> %s: Previosuly encoded primary image, skip now!"
+ "<<<< BWStillImageProcessing >>>> %s: Processing with InputImageAppliedOffsets: (%.4f,%.4f)"
+ "<<<< BWStillImageProcessing >>>> %s: [%@] Processing with OptimizedProcessingForZoomFOV: %@ (%@, AspectRatio:%.3lf)"
+ "<<<< BWStillImageProcessingNode >>>> %s: Processing raw error recovery %s for captureID:%lld"
+ "<<<< BWStillImageProcessingNode >>>> %s: Proxy error recovery processing is not supported for '%@'. Falling back to processing mode '%d'"
+ "<<<< BWStreamingFilterNode >>>> %s: Processing PTS %f renderListForFrame:%@%@"
+ "<<<< BWTiledEspressoInferenceAdapter >>>> %s: Tiled espresso provider was not already cached, hence created a brand new one: %@"
+ "<<<< BWTiledEspressoInferenceProvider >>>> %s: Cannot cache provider %@ with custom identifier %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
+ "<<<< BWTiledEspressoInferenceProvider >>>> %s: Cannot cache provider %@ with type %@ as its type does not match the placeholder provider %@ with type :%@ we are trying to move requirements from"
+ "<<<< BWUtilities >>>> %s: %@: Nondisruptive switching format too close to each other and additional overscan requested, using format index with wider zoom factor %@ at narrower zoom factor %@"
+ "<<<< BWVISNode >>>> %s: %@: Setting ISP procession session: %@ -> %@."
+ "<<<< BWVideoDepthNode >>>> %s: videoDepthConfiguration is nil"
+ "<<<< BWVideoProcessingInferenceAdapter >>>> %s: Cannot create cache key for video processing inference provider caching: cacheKeyAttributes are invalid"
+ "<<<< BWVideoProcessingInferenceAdapter >>>> %s: Could not create inference provider for type: %@"
+ "<<<< BWVideoProcessingInferenceAdapter >>>> %s: Could not create new provider of type (%d)"
+ "<<<< BWVideoProcessingInferenceAdapter >>>> %s: Unable to create a provider of type: %d as a cache key could not be generated for it"
+ "<<<< BWVideoProcessingInferenceAdapter >>>> %s: Video processing provider was not already cached, hence created a brand new one: %@"
+ "<<<< BWVideoProcessingInferenceProvider >>>> %s: Cannot cache provider %@ with custom identifier %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
+ "<<<< BWVideoProcessingInferenceProvider >>>> %s: Cannot cache provider %@ with type %@ as its type does not match the placeholder provider %@ with type :%@ we are trying to move requirements from"
+ "<<<< BWVideoProcessingInferenceProvider >>>> %s: Failed to instantiate VCPCaptureAnalysisSession. Motion Analysis Inferences will fail."
+ "<<<< BWVideoProcessingInferenceProvider >>>> %s: Input Pixel Buffer was missing while trying to execute inference of type: %@"
+ "<<<< BWVideoProcessingInferenceProvider >>>> %s: Prewarming VCPCaptureAnalysisSession failed with error (%d)"
+ "<<<< BWVideoProcessingInferenceProvider >>>> %s: Provider of type: %@ is not configured to handle multiple input video requirements during execution (%@)"
+ "<<<< BWVideoProcessingInferenceProvider >>>> %s: Provider of type: %@ is not configured to handle multiple input video requirements during submission (%@)"
+ "<<<< BWVideoProcessingInferenceProvider >>>> %s: VideoProcessing returned error: %@"
+ "<<<< BWVisionInferenceProvider >>>> %s: Cannot cache provider %@ with custom identifier %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
+ "<<<< CMCaptureGestalt >>>> %s: DeviceFeatures versions Spreadsheet = %@, Header = %@, Source = %@"
+ "<<<< CMInferenceUtils >>>> %s: CMINF: Bailing with err = %d"
+ "<<<< CMInferenceUtils >>>> %s: CMINF: Cannot build platformRegexExpPattern for isE5: %d, error:%@"
+ "<<<< CMInferenceUtils >>>> %s: CMINF: Cannot read list of v1 networks"
+ "<<<< CMInferenceUtils >>>> %s: CMINF: Cannot read list of v2/e5rt networks"
+ "<<<< CMInferenceUtils >>>> %s: CMINF: Failed to create reg exp for baseName: %@, isE5: %d (error:%@)"
+ "<<<< CMInferenceUtils >>>> %s: CMINF: Failed to get device identifier."
+ "<<<< CMInferenceUtils >>>> %s: CMINF: Failed to get platform identifier."
+ "<<<< CMInferenceUtils >>>> %s: CMINF: No matches found for networkBaseName \"%@\" in %@ list. Bailing..."
+ "<<<< CMInferenceUtils >>>> %s: CMINF: bailing..."
+ "<<<< CMInferenceUtils >>>> %s: CMINF: failed to find < %s > network at < %s >, isE5 : %d"
+ "<<<< CMInferenceUtils >>>> %s: CMINF: fsNetworks nil"
+ "<<<< CMInferenceUtils >>>> %s: CMINF: networkBaseName cannot be nil or empty (isE5: %d)"
+ "<<<< CMInferenceUtils >>>> %s: CMINF: platformRegExpPattern is nil for isE5: %d"
+ "<<<< CMInferenceUtils >>>> %s: CMINF:%lu files match basename \"%@\" in (%@ list ), %@"
+ "<<<< CMInferenceUtils >>>> Fig"
+ "<<<< FigCaptureCameraSourcePipeline >>>> %s: %@: Low light video: %s"
+ "<<<< FigCaptureCameraSourcePipeline >>>> %s: %{public}@: Variable frame rate video: %s / %s"
+ "<<<< FigCaptureMicSourcePipeline >>>> %s: warning: audio playing to the built-in speaker but the application does not allow the mic node to change the audio session's cinematic configuration to mono"
+ "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: Sharing photo encoder controller: %@ with piecemeal encoding node to enable piecemeal encoding of main image"
+ "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: failed to connect previousOutput to piecemealEncodingNode.input"
+ "<<<< FigCapturePowerLog >>>> %s: Missing camera stop power event"
+ "<<<< FigCaptureRadarUtils >>>> %s: Notification center not authorized -- status: %ld -- skipping TTR notification because we are about to crash the process and we don't want to wait for a modal dialog"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ %@"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ %@%s"
+ "<<<< FigCaptureSession >>>> %s: (%p) prewarmReason: %@, prewarmReasonAllowsHighPriorityLaunch %d, deviceIsLocked: %d, prewarmStatus = %s,  highPriorityLaunch: %d"
+ "<<<< FigCaptureSession >>>> %s: Committed configuration same as live one. Will not update session status to Running"
+ "<<<< FigCaptureSession >>>> %s: Error checking supported ISP processing session types: %d"
+ "<<<< FigCaptureSession >>>> %s: playingApplicationID: %@ is not camera nor is it voice-over"
+ "<<<< FigCaptureSourceBackingsProvider >>>> %s: Enabling SemanticStyleRenderingSupported"
+ "<<<< FigRemoteQueue >>>> %s: A %s timeout occurred while sending frames from %{public}s to %{public}s (%d consecutive, %zu mapped)"
+ "<<<< FigRemoteQueue >>>> %s: A %s timeout occurred while sending frames from %{public}s to %{public}s (%d consecutive, %zu mapped) -- no radar requested"
+ "<<<< FigRemoteQueue >>>> %s: Registering surface id %d timed out from %s, signalling with %d"
+ "<<<< FigRemoteQueue >>>> %s: restoring incoming voucher %p"
+ "@\"<BWInferenceSharedResourcePreparatory>\"16@0:8"
+ "@\"BWInferenceSharedE5ANEMemoryProvider\""
+ "@\"BWPrewarmResourceConfiguration\""
+ "@\"NSRegularExpression\""
+ "@132@0:8Q16Q24Q32i40B44B48B52B56f60B64i68B72B76f80f84i88@92@100B108B112@116@124"
+ "@28@0:8^{OpaqueFigCaptureISPProcessingSession=}16i24"
+ "@36@0:8@16B24B28f32"
+ "@36@0:8d16i24f28i32"
+ "@40@0:8d16d24f32i36"
+ "@56@0:8@16{?=qiIq}24@48"
+ "A %s timeout occurred while sending frames from %{public}s to %{public}s (%d consecutive, %zu mapped)"
+ "AVFCaptureBringupDefaultOverrides"
+ "AVGQ3FYMJTRW4LUXTNAFCC6XVFTDHA"
+ "AVGQ3J3FEVOOCNOKKTK3XQPUQ47DYY"
+ "AVGQ4UHSO4KRGIJFZHZ3EAGDMAK6CA"
+ "AVGQ5RTE3RTRZZFRGK7IDFEQC7NFBE"
+ "AVGQ6HD7ZNZD33DG7SG4DOHIPW4SUQ"
+ "AVGQAJT7KNQJHRRDW5Q5QTGETOLK2E"
+ "AVGQB7LQTMQIRMWVL3QHSIGQY3YFAA"
+ "AVGQBGWR3YSZWCQ7BKUUAOT5CCLHHE"
+ "AVGQBPMGIAYPLJA32XFRAAWDO5G4G4"
+ "AVGQBWQSOG5QWWG276TG2HH4RGJZDA"
+ "AVGQCACKZRYIKJ5BE2QI3FAY65ZYJA"
+ "AVGQCB54MH3XAXNGTVD2SAMOV5WWOQ"
+ "AVGQDINRSVRALL7UYNXKHVSIWKZLRA"
+ "AVGQDJVGPJA65CJA2ZPQZL4GRPYDYA"
+ "AVGQGYSWMQKMTMQOUYQ2AKUCKEN6AA"
+ "AVGQHDDMQ6RTH76PQ2HVCQ4MSWG63Q"
+ "AVGQHSSMVIQNR3MAPIGELAQM7DWP4U"
+ "AVGQIDWZFGNLZOQVZINTCD5JZM57DE"
+ "AVGQIIPQVVOWR6BFMGVVBAM7ZDTIW4"
+ "AVGQJQYPVTLPCNY4PHM26XACLZH4PU"
+ "AVGQKYDMKTE2UUKHJCGGZGQNYH5GDE"
+ "AVGQL72SILMBLRSKPL2V4VLPUD2TDU"
+ "AVGQLBZEVZETJU77LU4MEZH4LWJ54M"
+ "AVGQMZMLNHBX4MFF5QD4PJWZFEVCEI"
+ "AVGQN46I2BPHSDKPVN3YSGNPHPTAPE"
+ "AVGQODGWLXGASKA4RNU2OP6Z44TGZ4"
+ "AVGQOKRXQZPHFZ4X2XCPOHTANZXNGM"
+ "AVGQPEABAPB242SGF4J5L26EX5YTKA"
+ "AVGQQ4PFVIJ6WPTAHHYTAR5J5O7YNA"
+ "AVGQQIBUFDUYMZTKVBF36FTLQON3DY"
+ "AVGQSN3QUOWTBFYIVAQOVNQEVK6G4M"
+ "AVGQT42HZJM7T4BHFEGWILGWIJSNEQ"
+ "AVGQVNFDPYA37ZIZPRZOSYS4KMQIJ4"
+ "AVGQVYXTSFZ3R7TURIB5WPPITDPJLY"
+ "AVGQX3DWIDHL6QYY3OCER3G5UEM2QU"
+ "AVGQYPHR3FTUAZCCTEYFPSINLTE7DI"
+ "AdaptiveBracketingOriginalIspDGain"
+ "An error occurred while I was...\n\n%@Called from: %s:%d\nOperating system: %@\nProcess name: %@\nProcess ID: %d\nTime of error: %@"
+ "B24@?0@\"BWStillImageCaptureFrameInfo\"8@\"NSDictionary\"16"
+ "B28@0:8i16^i20"
+ "B72@?0{BWCachedADPCEDisparityColorInferenceDescriptorRequirements=I{CGSize=dd}@}8I40B44@\"NSString\"48@\"NSString\"56@\"NSArray\"64"
+ "BWE5InferenceProvider.m"
+ "BWInferenceResourceManager\nTotal Resources: %lu\n"
+ "BWInferenceSharedE5ANEMemoryProvider"
+ "BWInferenceSharedResourceManager"
+ "BWInferenceSharedResourcePreparatory"
+ "BWInferenceSharedResourcePrewarmer"
+ "BWPhotoEncoderSupportsPiecemealEnocding"
+ "BWPiecemealEncodingNode"
+ "BWPrewarmResourceConfiguration"
+ "BWStillImageCoordinatorAddAttachmentsToSampleBuffer"
+ "BWStillImageSettings.m"
+ "BWVideoDepthInferenceConfiguration.m"
+ "BravoSwitchOverVideoZoomFactorsWithoutFudge"
+ "BringupDefaultOverrides.plist"
+ "CIAreaAverage"
+ "CMGQAggregateDevicePhotoZoomFactor"
+ "CMGQAggregateDeviceVideoZoomFactor"
+ "CMGQBravoCameraVideoCapture4kMaxFPS"
+ "CMGQCameraAppUIVersion"
+ "CMGQCameraCapability"
+ "CMGQCameraFlashCapability"
+ "CMGQCameraFrontFlashCapability"
+ "CMGQCameraHDR10BitVideoCaptureMaxFPS"
+ "CMGQCameraHDR2Capability"
+ "CMGQCameraHDRVersion"
+ "CMGQCameraLiveEffectsCapability"
+ "CMGQCameraMaxBurstLength"
+ "CMGQCaptureSessionMaxMultiCamRGBStreamsSupported"
+ "CMGQCaptureSessionSupportsMultiCamCapture"
+ "CMGQDefaultVariableFrameRateVideoMaxFPS"
+ "CMGQDeviceHasAggregateCamera"
+ "CMGQDeviceSupportsAutoLowLightVideo"
+ "CMGQDeviceSupportsBravoCamera"
+ "CMGQDeviceSupportsBravoPortrait"
+ "CMGQDeviceSupportsCameraCaptureOnTouchDown"
+ "CMGQDeviceSupportsCameraDeferredProcessing"
+ "CMGQDeviceSupportsCinematicVideo"
+ "CMGQDeviceSupportsContentAwareDistortionCorrection"
+ "CMGQDeviceSupportsDeferredPortraitRendering"
+ "CMGQDeviceSupportsDepthWithDeepFusion"
+ "CMGQDeviceSupportsExposureBiasWithoutExposureLock"
+ "CMGQDeviceSupportsExtendedEnhancedCinematicVideoStabilization"
+ "CMGQDeviceSupportsFrontFacingCameraMirroredVideo"
+ "CMGQDeviceSupportsFrontFacingCameraNightMode"
+ "CMGQDeviceSupportsFrontFacingCameraSmartHDR"
+ "CMGQDeviceSupportsFrontFacingCameraSuperWide"
+ "CMGQDeviceSupportsFrontFacingCameraZoomToggle"
+ "CMGQDeviceSupportsFrontPortrait"
+ "CMGQDeviceSupportsHDREV0Capture"
+ "CMGQDeviceSupportsLinearDNG"
+ "CMGQDeviceSupportsLivePhotoAuto"
+ "CMGQDeviceSupportsMomentCapture"
+ "CMGQDeviceSupportsP3ColorspaceVideoRecording"
+ "CMGQDeviceSupportsPortraitIntensityAdjustments"
+ "CMGQDeviceSupportsPortraitLightEffectFilters"
+ "CMGQDeviceSupportsProResVideo"
+ "CMGQDeviceSupportsResponsiveShutter"
+ "CMGQDeviceSupportsSemanticDevelopment"
+ "CMGQDeviceSupportsSemanticStyles"
+ "CMGQDeviceSupportsSingleCameraPortrait"
+ "CMGQDeviceSupportsSpatialOverCapture"
+ "CMGQDeviceSupportsStageLightPortraitPreview"
+ "CMGQDeviceSupportsStereoAudioRecording"
+ "CMGQDeviceSupportsStudioLightPortraitPreview"
+ "CMGQDeviceSupportsSuperWideAutoMacro"
+ "CMGQDeviceSupportsTimelapseNightMode"
+ "CMGQDeviceSupportsTrueVideo"
+ "CMGQDeviceSupportsVariableFrameRateVideo"
+ "CMGQDeviceSupportsWideBravoCamera"
+ "CMGQDeviceSupportsWideBravoPortrait"
+ "CMGQDeviceSupportsWideBravoPortraitNightMode"
+ "CMGQDeviceSupportsZoomPictureInPicture"
+ "CMGQFirstSupportedReleaseVersion"
+ "CMGQFrontFacingCameraAutoHDRCapability"
+ "CMGQFrontFacingCameraBurstCapability"
+ "CMGQFrontFacingCameraCapability"
+ "CMGQFrontFacingCameraFocalLengthIn35mm"
+ "CMGQFrontFacingCameraHDRCapability"
+ "CMGQFrontFacingCameraHDROnCapability"
+ "CMGQFrontFacingCameraHFRCapability"
+ "CMGQFrontFacingCameraHFRVideoCapture1080pMaxFPS"
+ "CMGQFrontFacingCameraHFRVideoCapture720pMaxFPS"
+ "CMGQFrontFacingCameraMaxPhotoZoomFactor"
+ "CMGQFrontFacingCameraMaxVideoZoomFactor"
+ "CMGQFrontFacingCameraPortraitModeCapability"
+ "CMGQFrontFacingCameraSingleCameraPortrait"
+ "CMGQFrontFacingCameraStageLightPortraitCaptureCapability"
+ "CMGQFrontFacingCameraStillDurationForBurst"
+ "CMGQFrontFacingCameraSupportsCinematicVideo"
+ "CMGQFrontFacingCameraSupportsCinematicVideo4K"
+ "CMGQFrontFacingCameraSupportsPortraitAutoSuggest"
+ "CMGQFrontFacingCameraVideoCapture1080pMaxFPS"
+ "CMGQFrontFacingCameraVideoCapture4kMaxFPS"
+ "CMGQFrontFacingCameraVideoCapture720pMaxFPS"
+ "CMGQHEVCEncodingCapability"
+ "CMGQHasAppleNeuralEngine"
+ "CMGQMedusaOverlayAppCapability"
+ "CMGQMinimumDiskSpaceReserved"
+ "CMGQPanoramaCameraCapability"
+ "CMGQPearlCameraCapability"
+ "CMGQPhotosPostEffectsCapability"
+ "CMGQPipelinedStillImageProcessingCapability"
+ "CMGQRearFacingAggregateDeviceMaxCinematicZoomFactor"
+ "CMGQRearFacingAggregateDeviceMaxPortraitZoomFactor"
+ "CMGQRearFacingCamera60fpsVideoCaptureCapability"
+ "CMGQRearFacingCameraAutoHDRCapability"
+ "CMGQRearFacingCameraBurstCapability"
+ "CMGQRearFacingCameraCapability"
+ "CMGQRearFacingCameraFocusPixelCalibrationCapability"
+ "CMGQRearFacingCameraHDRCapability"
+ "CMGQRearFacingCameraHDROnCapability"
+ "CMGQRearFacingCameraHFRCapability"
+ "CMGQRearFacingCameraHFRVideoCapture1080pMaxFPS"
+ "CMGQRearFacingCameraHFRVideoCapture4kMaxFPS"
+ "CMGQRearFacingCameraHFRVideoCapture720pMaxFPS"
+ "CMGQRearFacingCameraMaxPhotoZoomFactor"
+ "CMGQRearFacingCameraMaxVideoZoomFactor"
+ "CMGQRearFacingCameraPortraitModeCapability"
+ "CMGQRearFacingCameraStageLightPortraitCaptureCapability"
+ "CMGQRearFacingCameraStillDurationForBurst"
+ "CMGQRearFacingCameraSuperWideCameraCapability"
+ "CMGQRearFacingCameraSupportsCinematicVideo"
+ "CMGQRearFacingCameraSupportsCinematicVideo4K"
+ "CMGQRearFacingCameraSupportsPortraitAutoSuggest"
+ "CMGQRearFacingCameraTimeOfFlightCameraCapability"
+ "CMGQRearFacingCameraVideoCapture1080pMaxFPS"
+ "CMGQRearFacingCameraVideoCapture4kMaxFPS"
+ "CMGQRearFacingCameraVideoCapture720pMaxFPS"
+ "CMGQRearFacingLowLightCameraCapability"
+ "CMGQRearFacingSuperWideCameraFocalLengthIn35mm"
+ "CMGQRearFacingTeleCameraFocalLengthIn35mm"
+ "CMGQRearFacingTelephotoCameraCapability"
+ "CMGQRearFacingWideCameraFocalLengthIn35mm"
+ "CMGQRearWideCameraDisplayCustomZoomStops"
+ "CMGQSphereCapability"
+ "CMGQSuperBravoCameraVideoCapture1080pMaxFPS"
+ "CMGQSuperBravoCameraVideoCapture4kMaxFPS"
+ "CMGQSuperWideCameraToWideCameraRelativeZoomFactor"
+ "CMGQSupportsIrisCapture"
+ "CMGQTorchMaxBeamWidth"
+ "CMGQTorchMinBeamWidth"
+ "CMGQVideoCameraCapability"
+ "CMGQVideoStillsCapability"
+ "CMGQWideBravoCameraVideoCapture4kMaxFPS"
+ "CMGQWideCameraToTelephotoCameraRelativeZoomFactor"
+ "CMInferenceUtils.m"
+ "CameraCapture Inference"
+ "Cisco-Systems.Spark"
+ "CurrentPrimary %@, PTS %.3f, zoomFactor %f, RecommendedPrimary %@, debugOverlayInfo %@"
+ "D16-D17"
+ "D27-D28"
+ "D37-D38"
+ "D421-D431"
+ "D47-D48"
+ "D52g-D53g"
+ "D63-D64"
+ "D73-D74"
+ "D93-D94"
+ "DFlashHR"
+ "DeskCamSessionDelegate"
+ "DigitalFlashEVZeroRatio"
+ "DigitalFlashExposureTime"
+ "DigitalFlashTimeMachineHighlightRecoveryMismatch"
+ "DigitalFlashTooDisruptive"
+ "E5"
+ "E5RT memory provider"
+ "E5RT_ERROR_CODE_OK == st"
+ "Failed to setup processor coordinator -- all processing will fail!"
+ "FigCaptureClientApplicationIDIsVoiceOver"
+ "FigRemoteQueue.m"
+ "ISPMotionDataGroupDelay"
+ "If you are still in this state or can reproduce, run `ddt %s; ddt %s` on the device (as root) while in this state and attach/paste results to the radar."
+ "Inference pipeline has unexpectedly fallen back to the legacy prewarming path for provider <%@> of type: %@ and will not be set up to share ANEF intra-backend memory buffers across E5RT executions during this invocation for this provider. This should not have occured."
+ "J171a-J172a"
+ "J181-J182"
+ "J210-J211-J217-J218"
+ "J255-J256"
+ "J271-J272"
+ "J305"
+ "J307-J308"
+ "J310-J311"
+ "J317-J317x-J318-J318x-J320-J320x-J321-J321x"
+ "J407-J408"
+ "J410-J411"
+ "J417-J418-J420-J421"
+ "J481-J482"
+ "J507-J508-J537-J538"
+ "J517-J517x-J518-J518x-J522-J522x-J523-J523x"
+ "J607-J608-J637-J638"
+ "J617-J618-J620-J621"
+ "J717-J718-J720-J721"
+ "Jun 18 2025"
+ "LastShownBuild:BWAudioSourceNode.m:1018"
+ "LastShownBuild:BWDeepZoomInferenceProvider.m:467"
+ "LastShownBuild:BWDeepZoomInferenceProvider.m:546"
+ "LastShownBuild:BWDeepZoomProcessorController.m:1064"
+ "LastShownBuild:BWDeferredProcessorController.m:872"
+ "LastShownBuild:BWDeferredProcessorController.m:916"
+ "LastShownBuild:BWDepthConverterNode.m:1059"
+ "LastShownBuild:BWE5InferenceProvider.m:573"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:1443"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:2817"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:2868"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3452"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3462"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10173"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10208"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10406"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10418"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10425"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10452"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10512"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10654"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11526"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:14601"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:17232"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:1741"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:17619"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18260"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18541"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18543"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:21437"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:21469"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:21608"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22438"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22762"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:5286"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7803"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7804"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8026"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8828"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9271"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9722"
+ "LastShownBuild:BWFigVideoCaptureStream.m:3283"
+ "LastShownBuild:BWFigVideoCaptureStream.m:3694"
+ "LastShownBuild:BWFigVideoCaptureSynchronizedStreamsGroup.m:402"
+ "LastShownBuild:BWGraph.m:3118"
+ "LastShownBuild:BWGraph.m:3168"
+ "LastShownBuild:BWGraph.m:3180"
+ "LastShownBuild:BWGraph.m:3237"
+ "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1152"
+ "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1659"
+ "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:725"
+ "LastShownBuild:BWIrisStagingNode.m:3833"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:12482"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:2474"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:3899"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:3906"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:3913"
+ "LastShownBuild:BWNRFProcessorController.m:1588"
+ "LastShownBuild:BWNRFProcessorController.m:1589"
+ "LastShownBuild:BWNRFProcessorController.m:4425"
+ "LastShownBuild:BWPhotoEncoderController.m:1017"
+ "LastShownBuild:BWPhotoEncoderController.m:1020"
+ "LastShownBuild:BWPhotoEncoderController.m:1384"
+ "LastShownBuild:BWPhotoEncoderController.m:1389"
+ "LastShownBuild:BWPhotoEncoderController.m:1616"
+ "LastShownBuild:BWPhotoEncoderController.m:1737"
+ "LastShownBuild:BWPhotoEncoderController.m:1753"
+ "LastShownBuild:BWPhotoEncoderController.m:3368"
+ "LastShownBuild:BWPhotoEncoderController.m:4050"
+ "LastShownBuild:BWPhotoEncoderController.m:5407"
+ "LastShownBuild:BWPhotonicEngineNode.m:1254"
+ "LastShownBuild:BWPhotonicEngineNode.m:1314"
+ "LastShownBuild:BWPhotonicEngineNode.m:1417"
+ "LastShownBuild:BWPhotonicEngineNode.m:1420"
+ "LastShownBuild:BWPhotonicEngineNode.m:1444"
+ "LastShownBuild:BWPhotonicEngineNode.m:1824"
+ "LastShownBuild:BWPhotonicEngineNode.m:1875"
+ "LastShownBuild:BWPhotonicEngineNode.m:2105"
+ "LastShownBuild:BWPhotonicEngineNode.m:2115"
+ "LastShownBuild:BWPhotonicEngineNode.m:2559"
+ "LastShownBuild:BWPhotonicEngineNode.m:2580"
+ "LastShownBuild:BWPhotonicEngineNode.m:2583"
+ "LastShownBuild:BWPhotonicEngineNode.m:3260"
+ "LastShownBuild:BWPhotonicEngineNode.m:3275"
+ "LastShownBuild:BWPhotonicEngineNode.m:3386"
+ "LastShownBuild:BWPhotonicEngineNode.m:3410"
+ "LastShownBuild:BWPhotonicEngineNode.m:4446"
+ "LastShownBuild:BWPhotonicEngineNode.m:5142"
+ "LastShownBuild:BWPhotonicEngineNode.m:5160"
+ "LastShownBuild:BWPhotonicEngineNode.m:597"
+ "LastShownBuild:BWPhotonicEngineNode.m:611"
+ "LastShownBuild:BWPhotonicEngineNode.m:618"
+ "LastShownBuild:BWPhotonicEngineNode.m:7094"
+ "LastShownBuild:BWPhotonicEngineNode.m:7096"
+ "LastShownBuild:BWPhotonicEngineNode.m:8537"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2359"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:370"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:382"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3834"
+ "LastShownBuild:BWPhotonicEngineNodeUtilities.m:1222"
+ "LastShownBuild:BWPiecemealEncodingNode.m:152"
+ "LastShownBuild:BWSmartStyleRenderingProcessorController.m:826"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1088"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:3389"
+ "LastShownBuild:BWStillImageFilterNode.m:1022"
+ "LastShownBuild:BWStillImageFilterNode.m:585"
+ "LastShownBuild:BWStillImageFilterNode.m:598"
+ "LastShownBuild:BWStillImageFrameCoordinatorNode.m:566"
+ "LastShownBuild:BWStillImageFrameCoordinatorNode.m:585"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1246"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1253"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1259"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1277"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1956"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1986"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:758"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:930"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:987"
+ "LastShownBuild:BWUBCaptureParameters.m:186"
+ "LastShownBuild:BWUBCaptureParameters.m:192"
+ "LastShownBuild:BWUBCaptureParameters.m:195"
+ "LastShownBuild:BWUBCaptureParameters.m:200"
+ "LastShownBuild:BWUBCaptureParameters.m:256"
+ "LastShownBuild:BWUBNode.m:5923"
+ "LastShownBuild:BWUtilities.m:940"
+ "LastShownBuild:BWVISNode.m:2291"
+ "LastShownBuild:BWVISNode.m:2309"
+ "LastShownBuild:BWVISNode.m:434"
+ "LastShownBuild:BWVisionInferenceProvider.m:389"
+ "LastShownBuild:BWVisionInferenceProvider.m:433"
+ "LastShownBuild:CMCaptureLocalSessionController.m:746"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1287"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:5462"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1442"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1448"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1449"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1453"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1569"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1575"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1578"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1739"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2716"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2802"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2803"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2975"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2978"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3149"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3152"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3197"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4104"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4110"
+ "LastShownBuild:FigCaptureSession.m:10660"
+ "LastShownBuild:FigCaptureSession.m:17041"
+ "LastShownBuild:FigCaptureSession.m:17874"
+ "LastShownBuild:FigCaptureSession.m:21239"
+ "LastShownBuild:FigCaptureSession.m:21274"
+ "LastShownBuild:FigCaptureSession.m:23468"
+ "LastShownBuild:FigCaptureSession.m:4090"
+ "LastShownBuild:FigCaptureSession.m:7991"
+ "LastShownBuild:FigCaptureSession.m:7994"
+ "LastShownBuild:FigCaptureSession.m:8005"
+ "LastShownBuild:FigCaptureSession.m:8008"
+ "LastShownBuild:FigCaptureSession.m:8018"
+ "LastShownBuild:FigCaptureSession.m:8036"
+ "LastShownBuild:FigCaptureSession.m:8050"
+ "LastShownBuild:FigCaptureSession.m:8063"
+ "LastShownBuild:FigCaptureSession.m:8067"
+ "LastShownBuild:FigCaptureSession.m:8070"
+ "LastShownBuild:FigCaptureSession.m:8164"
+ "LastShownBuild:FigCaptureSession.m:8169"
+ "LastShownBuild:FigCaptureSession.m:8177"
+ "LastShownBuild:FigCaptureSession.m:8181"
+ "LastShownBuild:FigCaptureSession.m:8592"
+ "LastShownBuild:FigCaptureSession.m:8859"
+ "LastShownBuild:FigCaptureSession.m:9685"
+ "LastShownBuild:FigCaptureSession.m:9840"
+ "LastShownBuild:FigCaptureSessionPipelines.m:630"
+ "LastShownBuild:FigCaptureSource.m:1463"
+ "LastShownBuild:FigCaptureSource.m:1467"
+ "LastShownBuild:FigCaptureSourceBackingsProvider.m:2519"
+ "LastShownBuild:FigCaptureSourceServer.m:1947"
+ "LastShownBuild:FigCaptureUtilities.m:991"
+ "LastShownBuild:FigRemoteQueue.m:1079"
+ "LastShownDate:BWAudioSourceNode.m:1018"
+ "LastShownDate:BWDeepZoomInferenceProvider.m:467"
+ "LastShownDate:BWDeepZoomInferenceProvider.m:546"
+ "LastShownDate:BWDeepZoomProcessorController.m:1064"
+ "LastShownDate:BWDeferredProcessorController.m:872"
+ "LastShownDate:BWDeferredProcessorController.m:916"
+ "LastShownDate:BWDepthConverterNode.m:1059"
+ "LastShownDate:BWE5InferenceProvider.m:573"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:1443"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:2817"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:2868"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3452"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3462"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10173"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10208"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10406"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10418"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10425"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10452"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10512"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10654"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11526"
+ "LastShownDate:BWFigVideoCaptureDevice.m:14601"
+ "LastShownDate:BWFigVideoCaptureDevice.m:17232"
+ "LastShownDate:BWFigVideoCaptureDevice.m:1741"
+ "LastShownDate:BWFigVideoCaptureDevice.m:17619"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18260"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18541"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18543"
+ "LastShownDate:BWFigVideoCaptureDevice.m:21437"
+ "LastShownDate:BWFigVideoCaptureDevice.m:21469"
+ "LastShownDate:BWFigVideoCaptureDevice.m:21608"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22438"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22762"
+ "LastShownDate:BWFigVideoCaptureDevice.m:5286"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7803"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7804"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8026"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8828"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9271"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9722"
+ "LastShownDate:BWFigVideoCaptureStream.m:3283"
+ "LastShownDate:BWFigVideoCaptureStream.m:3694"
+ "LastShownDate:BWFigVideoCaptureSynchronizedStreamsGroup.m:402"
+ "LastShownDate:BWGraph.m:3118"
+ "LastShownDate:BWGraph.m:3168"
+ "LastShownDate:BWGraph.m:3180"
+ "LastShownDate:BWGraph.m:3237"
+ "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1152"
+ "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1659"
+ "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:725"
+ "LastShownDate:BWIrisStagingNode.m:3833"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:12482"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:2474"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:3899"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:3906"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:3913"
+ "LastShownDate:BWNRFProcessorController.m:1588"
+ "LastShownDate:BWNRFProcessorController.m:1589"
+ "LastShownDate:BWNRFProcessorController.m:4425"
+ "LastShownDate:BWPhotoEncoderController.m:1017"
+ "LastShownDate:BWPhotoEncoderController.m:1020"
+ "LastShownDate:BWPhotoEncoderController.m:1384"
+ "LastShownDate:BWPhotoEncoderController.m:1389"
+ "LastShownDate:BWPhotoEncoderController.m:1616"
+ "LastShownDate:BWPhotoEncoderController.m:1737"
+ "LastShownDate:BWPhotoEncoderController.m:1753"
+ "LastShownDate:BWPhotoEncoderController.m:3368"
+ "LastShownDate:BWPhotoEncoderController.m:4050"
+ "LastShownDate:BWPhotoEncoderController.m:5407"
+ "LastShownDate:BWPhotonicEngineNode.m:1254"
+ "LastShownDate:BWPhotonicEngineNode.m:1314"
+ "LastShownDate:BWPhotonicEngineNode.m:1417"
+ "LastShownDate:BWPhotonicEngineNode.m:1420"
+ "LastShownDate:BWPhotonicEngineNode.m:1444"
+ "LastShownDate:BWPhotonicEngineNode.m:1824"
+ "LastShownDate:BWPhotonicEngineNode.m:1875"
+ "LastShownDate:BWPhotonicEngineNode.m:2105"
+ "LastShownDate:BWPhotonicEngineNode.m:2115"
+ "LastShownDate:BWPhotonicEngineNode.m:2559"
+ "LastShownDate:BWPhotonicEngineNode.m:2580"
+ "LastShownDate:BWPhotonicEngineNode.m:2583"
+ "LastShownDate:BWPhotonicEngineNode.m:3260"
+ "LastShownDate:BWPhotonicEngineNode.m:3275"
+ "LastShownDate:BWPhotonicEngineNode.m:3386"
+ "LastShownDate:BWPhotonicEngineNode.m:3410"
+ "LastShownDate:BWPhotonicEngineNode.m:4446"
+ "LastShownDate:BWPhotonicEngineNode.m:5142"
+ "LastShownDate:BWPhotonicEngineNode.m:5160"
+ "LastShownDate:BWPhotonicEngineNode.m:597"
+ "LastShownDate:BWPhotonicEngineNode.m:611"
+ "LastShownDate:BWPhotonicEngineNode.m:618"
+ "LastShownDate:BWPhotonicEngineNode.m:7094"
+ "LastShownDate:BWPhotonicEngineNode.m:7096"
+ "LastShownDate:BWPhotonicEngineNode.m:8537"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2359"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:370"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:382"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3834"
+ "LastShownDate:BWPhotonicEngineNodeUtilities.m:1222"
+ "LastShownDate:BWPiecemealEncodingNode.m:152"
+ "LastShownDate:BWSmartStyleRenderingProcessorController.m:826"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1088"
+ "LastShownDate:BWStillImageCoordinatorNode.m:3389"
+ "LastShownDate:BWStillImageFilterNode.m:1022"
+ "LastShownDate:BWStillImageFilterNode.m:585"
+ "LastShownDate:BWStillImageFilterNode.m:598"
+ "LastShownDate:BWStillImageFrameCoordinatorNode.m:566"
+ "LastShownDate:BWStillImageFrameCoordinatorNode.m:585"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1246"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1253"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1259"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1277"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1956"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1986"
+ "LastShownDate:BWStillImageMetadataUtilities.m:758"
+ "LastShownDate:BWStillImageMetadataUtilities.m:930"
+ "LastShownDate:BWStillImageMetadataUtilities.m:987"
+ "LastShownDate:BWUBCaptureParameters.m:186"
+ "LastShownDate:BWUBCaptureParameters.m:192"
+ "LastShownDate:BWUBCaptureParameters.m:195"
+ "LastShownDate:BWUBCaptureParameters.m:200"
+ "LastShownDate:BWUBCaptureParameters.m:256"
+ "LastShownDate:BWUBNode.m:5923"
+ "LastShownDate:BWUtilities.m:940"
+ "LastShownDate:BWVISNode.m:2291"
+ "LastShownDate:BWVISNode.m:2309"
+ "LastShownDate:BWVISNode.m:434"
+ "LastShownDate:BWVisionInferenceProvider.m:389"
+ "LastShownDate:BWVisionInferenceProvider.m:433"
+ "LastShownDate:CMCaptureLocalSessionController.m:746"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1287"
+ "LastShownDate:FigCaptureMetadataUtilities.m:5462"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1442"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1448"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1449"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1453"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1569"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1575"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1578"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1739"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2716"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2802"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2803"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2975"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2978"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3149"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3152"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3197"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4104"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4110"
+ "LastShownDate:FigCaptureSession.m:10660"
+ "LastShownDate:FigCaptureSession.m:17041"
+ "LastShownDate:FigCaptureSession.m:17874"
+ "LastShownDate:FigCaptureSession.m:21239"
+ "LastShownDate:FigCaptureSession.m:21274"
+ "LastShownDate:FigCaptureSession.m:23468"
+ "LastShownDate:FigCaptureSession.m:4090"
+ "LastShownDate:FigCaptureSession.m:7991"
+ "LastShownDate:FigCaptureSession.m:7994"
+ "LastShownDate:FigCaptureSession.m:8005"
+ "LastShownDate:FigCaptureSession.m:8008"
+ "LastShownDate:FigCaptureSession.m:8018"
+ "LastShownDate:FigCaptureSession.m:8036"
+ "LastShownDate:FigCaptureSession.m:8050"
+ "LastShownDate:FigCaptureSession.m:8063"
+ "LastShownDate:FigCaptureSession.m:8067"
+ "LastShownDate:FigCaptureSession.m:8070"
+ "LastShownDate:FigCaptureSession.m:8164"
+ "LastShownDate:FigCaptureSession.m:8169"
+ "LastShownDate:FigCaptureSession.m:8177"
+ "LastShownDate:FigCaptureSession.m:8181"
+ "LastShownDate:FigCaptureSession.m:8592"
+ "LastShownDate:FigCaptureSession.m:8859"
+ "LastShownDate:FigCaptureSession.m:9685"
+ "LastShownDate:FigCaptureSession.m:9840"
+ "LastShownDate:FigCaptureSessionPipelines.m:630"
+ "LastShownDate:FigCaptureSource.m:1463"
+ "LastShownDate:FigCaptureSource.m:1467"
+ "LastShownDate:FigCaptureSourceBackingsProvider.m:2519"
+ "LastShownDate:FigCaptureSourceServer.m:1947"
+ "LastShownDate:FigCaptureUtilities.m:991"
+ "LastShownDate:FigRemoteQueue.m:1079"
+ "MOC %p: <%@>%@ -> <%@> E:%d MetadataIdentifiers:{%@}%@%@%@%@%@%@%@%@%@%@%@%@"
+ "MetadataTimeMachineMetadataForPTSRangeMissing"
+ "MetadataTimeMachineWaitUntilCapacityTimeout"
+ "MidFrameSynchronizationNotSupported"
+ "MinimumSupportedUIZoomFactor"
+ "Missing camera stop power event"
+ "Missing requested settings"
+ "Missing settings in BWStillImageCoordinatorAddAttachmentsToSampleBuffer()%@"
+ "NOT "
+ "New configuration: %{public}@"
+ "No resources currently stored.\n"
+ "Receiving sbuf media {%@}"
+ "ResolutionFlavor:%d"
+ "Stored Resources:\n"
+ "Subclasses of the shared resource manager must override this method to provide a valid resource category"
+ "T@\"<BWInferenceSharedResourcePreparatory>\",R,N"
+ "T@\"BWInferenceSharedE5ANEMemoryProvider\",&,V_sharedE5ANEMemoryProvider"
+ "T@\"BWPrewarmResourceConfiguration\",R,V_resourceConfig"
+ "T@\"FigMetalAllocatorBackend\",R,V_sharedMetalAllocatorBackend"
+ "T@\"NSArray\",R,N,V_connectionConfigurationsToBuild"
+ "T@\"NSDictionary\",R,N,V_ispBaseZoomFactorsByPortType"
+ "T@\"NSDictionary\",R,N,V_previewStabilizationParameters"
+ "T@\"NSObject<OS_dispatch_semaphore>\",N"
+ "TB,N,V_teleAutoVideoFrameRateAllows24FPS"
+ "TB,R,N,V_teleAutoVideoFrameRateAllows24FPS"
+ "T^{BWCoreAnalyticsMovieRecordingVideoDeghostingStatistics=Biddffff},N,V_videoDeghostingStatistics"
+ "Td,R,N,V_upscaledEnhancedResolutionEffectiveIntegrationTimeThreshold"
+ "TeleAutoVideoFrameRateAllows24FPS"
+ "UpEnRes"
+ "Updated FinalCropRect is larger than ValidBufferRect (%{public}@ vs. %{public}@), processing might produce corrupted photos for captureID:%{public}lld"
+ "Updated MinimumValidBufferRectForGDC is larger than ValidBufferRect (%{public}@ vs. %{public}@), processing might produce corrupted photos for captureID:%{public}lld"
+ "UpscaledEnhancedResolutionEffectiveIntegrationTimeThreshold"
+ "V1"
+ "[22{BWStreamOutputStorage=\"type\"i\"flags\"I\"ready\"B\"enabled\"B\"nodeOutput\"@\"BWNodeOutput\"\"simpleQueue\"^{opaqueCMSimpleQueue}\"bufferServicingQueue\"@\"NSObject<OS_dispatch_queue>\"\"bufferServicingQueueCallback\"^?\"cachedFormatDescription\"^{opaqueCMFormatDescription}\"lastEmittedPTS\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"frameCounter\"@\"FigCaptureFrameCounter\"\"retainedBufferCount\"i\"streamRetainedBufferCount\"i\"internalPixelBufferPool\"@\"BWPixelBufferPool\"\"bufferPoolOwnedByAnotherNode\"B\"bytesPerRowAlignmentRequirement\"i\"planeAlignmentRequirement\"i\"sensorInterfaceRawPixelFormat\"I\"sashimiRawPixelFormat\"I\"sushiRawPixelFormat\"I\"outputDimensions\"{?=\"width\"i\"height\"i}\"cropRect\"{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}\"lastISPAppliedZoomFactor\"f\"ioSurfaceCompressionRatioStats\"@\"BWStats\"\"pixelBufferCompressionType\"i\"totalCompressedDataSize\"Q\"totalUncompressedDataSize\"Q\"lumaCompressionHistogram\"[16Q]\"chromaCompressionHistogram\"[16Q]\"universalCompressionNumberOfSamples\"I\"lastUniversalCompressionSamplePTS\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"pixelFormatIsTenBit\"B\"pixelFormatIs420\"B\"pixelFormatIsLossyCompression\"B\"prefetchEnabled\"B\"incrementalPrefetchEnabled\"B\"prevSceneIlluminationValue\"I\"prevSceneIlluminationValueCaptureID\"i}]"
+ "[super addNode:piecemealEncodingNode error:&error]"
+ "^%@$"
+ "^{BWCachedADPCEDisparityColorInferenceDescriptor=q{?=ii}{?=ii}{?=ii}IIf@@{BWCachedADPCEDisparityColorInferenceDescriptorRequirements=I{CGSize=dd}@}{BWCachedADPCEDisparityColorInferenceDescriptorRequirements=I{CGSize=dd}@}{BWCachedADPCEDisparityColorInferenceDescriptorRequirements=I{CGSize=dd}@}{BWCachedADPCEDisparityColorInferenceDescriptorRequirements=I{CGSize=dd}@}{BWCachedADPCEDisparityColorInferenceDescriptorRequirements=I{CGSize=dd}@}{BWCachedADPCEDisparityColorInferenceDescriptorRequirements=I{CGSize=dd}@}}28@0:8i16Q20"
+ "^{BWCoreAnalyticsMovieRecordingVideoDeghostingStatistics=Biddffff}"
+ "^{BWCoreAnalyticsMovieRecordingVideoDeghostingStatistics=Biddffff}16@0:8"
+ "^{e5rt_ane_memory_provider=}24@0:8@16"
+ "_adLayoutForVideoDepthLayout"
+ "_adaptiveBracketingDigitalFlashTotalIntegrationTimesProviderByPortType"
+ "_adaptiveTimeMachineBracketedCaptureParams"
+ "_baseZoomFactorsByPortTypeWithoutFudge"
+ "_cameraTransitionBorderEdgeFeatheringEnabled"
+ "_cameraTransitionBrightnessCompensationEnabled"
+ "_cameraTransitionBrightnessCompensationInsetPercentage"
+ "_cameraTransitionEdgeFeatheringBorderInsetFactor"
+ "_cameraTransitionEdgeFeatheringZoomInEndSigma"
+ "_cameraTransitionEdgeFeatheringZoomInStartSigma"
+ "_cameraTransitionEdgeFeatheringZoomInTeleEdgeExpansionFrameDuration"
+ "_cameraTransitionEdgeFeatheringZoomInTeleEdgeExpansionStartFrameFill"
+ "_cameraTransitionEdgeFeatheringZoomOutEndSigma"
+ "_cameraTransitionEdgeFeatheringZoomOutQsubToQsumEdgeOpacityRampFrameDuration"
+ "_cameraTransitionEdgeFeatheringZoomOutStartSigma"
+ "_cameraTransitionEnhancedEdgeFeatheringEnabled"
+ "_conditionVariablesTrackedByResourceCategory"
+ "_connectionConfigurationsToBuild"
+ "_encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:mainImageHandleInOut:"
+ "_encodePrimarySbuf:metadata:processingFlags:primaryImageHandleInOut:"
+ "_evZeroRatio"
+ "_getNetworkPath:isE5:fsNetworks:"
+ "_initWithStillImageSettings:resourceConfig:"
+ "_ispBaseZoomFactorsByPortType"
+ "_ispMotionDataGroupDelay"
+ "_lastFrameDroppedByBackpressure"
+ "_lastStillZeroShutterLagFailureReason"
+ "_minimumPrerollFrames"
+ "_minimumSupportedUIZoomFactor"
+ "_networkListLock"
+ "_networksUsingE5ANEMemoryProvider"
+ "_nodePrepared"
+ "_outputDimensionsForSbuf:primaryImageMetadata:sourceDimensions:requestedStillImageCaptureSettings:isStereoPhotoCapture:isPrimaryFrame:"
+ "_photoModeFullStrengthUIZoomFactor"
+ "_platformRegExpPatternV1"
+ "_platformRegExpPatternV2"
+ "_previewFilterBackpressureSemaphore"
+ "_previewStabilizationParameters"
+ "_processErrorRecoveryProxy"
+ "_resourceConfig"
+ "_resourceCoordinatorLock"
+ "_resourceCreationMutex"
+ "_resourcesBeingCreated"
+ "_sharedE5ANEMemoryProvider"
+ "_sharedResourceDirectoryByCategory"
+ "_sharedResourceDirectoryRWLock"
+ "_sourceDeviceTypesWithKeypointDescriptorDataEnabledOnVideoCaptureOutputs"
+ "_sourceDeviceTypesWithLightSourceMaskEnabledOnVideoCaptureOutputs"
+ "_stashedAttachedMediaSampleBuffersLock"
+ "_teleAutoVideoFrameRateAllows24FPS"
+ "_triggerRegistrationForNondisruptiveSwitching"
+ "_upscaledEnhancedResolutionEffectiveIntegrationTimeThreshold"
+ "_usePTSToSyncPreviewAndCaptureFrames"
+ "_videoDataCopierNode"
+ "_videoDeghostingStatistics"
+ "_videoDeghostingStatisticsExtracted"
+ "_whiteBalanceGainsDeferredCommandID"
+ "adaptiveBracketingFrameParameters"
+ "adaptiveBracketingFrameParametersForFrame:"
+ "adaptiveTimeMachineBracketedCaptureParams"
+ "addAdaptiveBracketingFrameParameters:timeMachineBracketedCaptureParams:preBracketFrameCaptureParams:unifiedBracketedCaptureParams:captureFrameInfos:"
+ "addAdaptiveBracketingMetadataIfNeededForFrame:"
+ "addSbufForPiecemealEncoding:attachedMediakey:primaryImageMetadata:processingFlags:"
+ "applyWithExtent:arguments:"
+ "bwinferencesharede5anememoryprovider_trace"
+ "bwinferencesharedresourcemanager_trace"
+ "bwpiecemealencodingnode_trace"
+ "bwstillimagesettings_trace"
+ "bypassed"
+ "captureSession_startMonitoringForFigAssetWriterWritingVideoNotificationIfNecessary_block_invoke_2"
+ "cmcapturegestalt_buildDataBase_block_invoke"
+ "cmcapturegestalt_getAVFBringupDefaultOverride_block_invoke"
+ "cmcapturegestalt_trace"
+ "com.apple.Stickers.UserGenerated.MessagesExtension"
+ "com.apple.coremedia.metal-submission-queue"
+ "com.apple.coremedia.previewsink.metal-completion-queue"
+ "com.apple.coremedia.previewsink.personsegmentation"
+ "com.apple.coremedia.previewsink.pocketdetection"
+ "com.apple.coremedia.previewsink.registration"
+ "com.apple.quicktime.apple-maker-note.97"
+ "com.apple.quicktime.apple-maker-note.98"
+ "com.microsoft.teams2"
+ "completeANEMemoryProviderCreationForNetwork:wasSuccessful:"
+ "connectionConfigurationsToBuild"
+ "description=CameraCapture-655.0.0.122.4"
+ "descriptor != ((void *)0)"
+ "deskViewTrapezoidDidUpdate"
+ "dropEventCount"
+ "dropMaxAccel"
+ "dropMinAccel"
+ "dropStatus"
+ "e5_shared_resource"
+ "e5rt_ane_memory_provider_create fails to create an instance of the ane memory provider"
+ "e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options fails"
+ "e5rt_precompiled_compute_op_create_options_create fails"
+ "e5rt_precompiled_compute_op_create_options_release fails to release create options"
+ "e5rt_precompiled_compute_op_create_options_set_custom_ane_memory_provider failed on create options for 3:4 network variant"
+ "e5rt_precompiled_compute_op_create_options_set_custom_ane_memory_provider failed on create options for 4:3 network variant"
+ "e5rt_precompiled_compute_op_create_options_set_custom_ane_memory_provider fails"
+ "ed6240ee295d09fa1ebcb64acd38b914cbb5013c"
+ "emitStillImagePrewarmMessageWithSettings:resourceConfig:"
+ "enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:"
+ "evZeroRatio"
+ "expectedAdaptiveBracketedTimeMachineFrameCaptureCountUsingGroup:"
+ "fetchANEMemoryProviderForNetwork:"
+ "finalizeResourceCreationAttemptForCategory:"
+ "firstMatchInString:options:range:"
+ "frameParametersWithEVZeroRatio:integrationTimeInMicroseconds:gain:maxAGC:"
+ "frameParametersWithEVZeroRatio:integrationTimeInSeconds:gain:maxAGC:"
+ "handleStillImagePrewarmWithSettings:resourceConfig:forInput:"
+ "i116@0:8i16^{__CVBuffer=}20{?=ii}28I36@40@48@56@64{CGRect={CGPoint=dd}{CGSize=dd}}72B104^q108"
+ "i16@?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}@q^{__CFString}@i@@@@^{OpaqueFigCaptureSource}f@@@i^{OpaqueFigFlashlight}@iBBB^{OpaqueFigSimpleMutex}@BB}8"
+ "i24@0:8@\"BWInferenceSharedE5ANEMemoryProvider\"16"
+ "i28@0:8B16@\"BWInferenceSharedE5ANEMemoryProvider\"20"
+ "i28@0:8B16@20"
+ "i32@0:8@\"NSObject<OS_dispatch_queue>\"16@\"BWInferenceSharedE5ANEMemoryProvider\"24"
+ "i32@0:8^{e5rt_ane_memory_provider=}16@24"
+ "i44@0:8@\"BWNRFProcessorController\"16@\"BWNRFProcessorInput\"24B32@\"NSDictionary\"36"
+ "i44@0:8@16@24B32@36"
+ "i44@0:8^{opaqueCMSampleBuffer=}16@24I32^q36"
+ "i72@0:8@16@24B32B36B40B44B48i52B56B60B64B68"
+ "iOS 12.1"
+ "iOS 12.2"
+ "iOS 13.0"
+ "iOS 13.4"
+ "iOS 14.0"
+ "iOS 14.1"
+ "iOS 14.5"
+ "iOS 15.0"
+ "iOS 15.4"
+ "iOS 16.0"
+ "iOS 17.0"
+ "iOS 17.4"
+ "iOS 18.0"
+ "iOS 18.3"
+ "imageByClampingToExtent"
+ "initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:minimumSupportedUIZoomFactor:"
+ "initWithFigCaptureISPProcessingSession:type:"
+ "initWithInferenceScheduler:"
+ "initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:inferenceScheduler:"
+ "initWithPortType:captureType:captureFlags:referenceFrameIndex:adaptiveBracketingParameters:sphereOffsets:"
+ "initWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:teleAutoVideoFrameRateAllows24FPS:"
+ "inputImageAppliedOffsets"
+ "inputReceivedProcessedRawErrorRecoveryFrame:proxy:"
+ "inputReceivedSbufForPiecemealEncoding:sbuf:attachedMediaKey:primaryImageMetadata:processingFlags:"
+ "inputSource < ADPCEDisparityColorInputSourceCount"
+ "integrationTimeInMicroseconds"
+ "isFirstAdaptiveBracketingFrame:"
+ "ispBaseZoomFactorsByPortType"
+ "kernel vec4 AdjustGamma ( __sample a, __sample gamma, float adjPerc ) { \n   float adjGamma = 1.0 + ( gamma.x - 1.0 ) * adjPerc; \n   a.rgb = sign( a.rgb ) * pow( abs( a.rgb ), vec3( adjGamma ) ); \n   return a; }"
+ "kernel vec4 ComputeGamma ( __sample twoY, float edgeRatio ) __attribute__((outputFormat(kCIFormatRh))) { \n   float avX = twoY.x * edgeRatio; \n   float avY = twoY.y * edgeRatio; \n   float gamma = log( avY ) / log( avX ); \n   return vec4(gamma, 0.0, 0.0, 1.0); }"
+ "kernel vec4 TwoY ( __sample a, __sample b, float width, float height, float xOffset, float yOffset, float widthInset, float heightInset ) __attribute__((outputFormat(kCIFormatRGh))) { \n   vec2 dc = destCoord(); \n   dc.x -= xOffset; \n   dc.y -= yOffset; \n   if ( ( dc.x > widthInset ) && ( dc.x < ( width - widthInset - 1.0 ) ) && ( dc.y > heightInset ) && ( dc.y < ( height - heightInset - 1.0 ) ) ) return vec4( 0.0 ); \n   vec3 Y = vec3( 0.299, 0.587, 0.114 ); \n\t return vec4( dot( a.rgb, Y ), dot( b.rgb, Y ), 0.0, ( a.a * b.a ) ); }"
+ "kernelWithString:"
+ "maximumNumberOfReferenceFrameCandidatesToHoldForProcessing"
+ "metalPreviewCompletionDispatchQueue"
+ "metalPreviewSubmissionDispatchQueue"
+ "midFrameSynchronizationNotSupported"
+ "msp_configureMicNode"
+ "newDroppedSampleWithReason:pts:backPressureSemaphoresToIgnore:"
+ "newMessageWithStillImageSettings:resourceConfig:"
+ "newResourceConfigWithSharedMetalAllocator:"
+ "no shared resource type"
+ "operatingSystemVersionString"
+ "pceDisparityColorInferenceDescriptorForVideoDepthLayout:inputSource:"
+ "pid-%d"
+ "pointerValue"
+ "powerOnEventCount"
+ "prepareForExecutionWithSharedANEMemoryProvider:"
+ "prepareForSubmissionWithWorkQueue:sharedANEMemoryProvider:"
+ "previewFilterBackpressureSemaphore"
+ "previewStabilizationParameters"
+ "prewarmUsingLimitedMemory:sharedE5ANEMemoryProvider:"
+ "prewarmingSharedResourceType"
+ "processorController:processRawErrorRecoveryFrameForProcessorInput:processErrorRecoveryProxy:failureMetadata:"
+ "rangeOfString:options:"
+ "receiver"
+ "registerANEMemoryProvider:forNetwork:"
+ "regularExpressionWithPattern:options:error:"
+ "resetDimensions"
+ "resourceCategory"
+ "resourceConfig"
+ "retrieveSharedResourceForResourceCategoryAndLockIfNotAvailable:"
+ "rqSenderEnqueue-Timeout"
+ "scalerZoomFactor (%f,%f) is unexpectedly unachieveable"
+ "setInputImageAppliedOffsets:"
+ "setLowResGlassesMask:"
+ "setMaximumNumberOfReferenceFrameCandidatesToHoldForProcessing:"
+ "setPreviewFilterBackpressureSemaphore:"
+ "setProcessedRawErrorRecoveryFrame:proxy:"
+ "setSharedE5ANEMemoryProvider:"
+ "setTeleAutoVideoFrameRateAllows24FPS:"
+ "setUseDeepTransferAccommodations:"
+ "setVideoDeghostingStatistics:"
+ "sharedE5ANEMemoryProvider"
+ "sharedMetalAllocatorBackend"
+ "sharedResourcePreparator"
+ "sharedResourceType"
+ "stashSharedResource:forResourceCategory:"
+ "stillImageConnectionConfigurationForStillImageSinkPipeline:"
+ "stringByStandardizingPath"
+ "supportsISPProcessingSessionType:error:"
+ "teleAutoVideoFrameRateAllows24FPS"
+ "trainingFDRDelta"
+ "trainingPersistentDelta"
+ "tvOS 17.0"
+ "unknown shared resource type"
+ "upscaledEnhancedResolutionEffectiveIntegrationTimeThreshold"
+ "useDeepTransferAccommodations"
+ "v24@0:8^{BWCoreAnalyticsMovieRecordingVideoDeghostingStatistics=Biddffff}16"
+ "v28@0:8@\"BWNRFProcessorInput\"16B24"
+ "v56@0:8@16@24@32@40@48"
+ "videoCameraSourceAttributes"
+ "videoDeghostingAverageGhostArea"
+ "videoDeghostingAverageGhostCount"
+ "videoDeghostingEnabled"
+ "videoDeghostingOpticalCenterEstConfidence"
+ "videoDeghostingOpticalCenterOffsetMag"
+ "videoDeghostingOpticalCenterOffsetX"
+ "videoDeghostingOpticalCenterOffsetY"
+ "videoDeghostingStatistics"
+ "videoDeghostingVersion"
+ "videoDepthLayout < BWVideoDepthLayoutCount"
+ "{?=ii}56@0:8^{opaqueCMSampleBuffer=}16@24{?=ii}32@40B48B52"
+ "{BWCoreAnalyticsMovieRecordingVideoDeghostingStatistics=\"enabled\"B\"version\"i\"averageGhostArea\"d\"averageGhostCount\"d\"opticalCenterOffsetMag\"f\"opticalCenterOffsetX\"f\"opticalCenterOffsetY\"f\"opticalCenterEstConfidence\"f}"
+ "{_opaque_pthread_cond_t=q[40c]}"
- "%@%@\n  Flags: %@\n  %@\n"
- "( outputIndex > -1 ) && ( outputIndex < 21 )"
- "-[BWE5InferenceProvider _prepare]"
- "-[BWE5MultipleLayoutInferenceProvider _prepare]"
- "-[BWFigCaptureISPProcessingSession initWithFigCaptureISPProcessingSession:]"
- "-[BWFigVideoCaptureDevice _configureZoomFudging]"
- "-[BWFigVideoCaptureDevice _ubAdaptiveStillImageCaptureSettingsWithID:captureType:captureFlags:sceneFlags:frameStatisticsByPortType:]"
- "-[BWFigVideoCaptureDevice _ubUpdateCurrentAdaptiveBracketedCaptureParamsForCaptureStreamSettings:frameStatistics:]"
- "-[BWIrisStagingNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:]"
- "-[BWMultiStreamCameraSourceNode _updateZoomForOutputIndex:sampleBuffer:additionalScaleFactor:]"
- "-[BWNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:]"
- "-[BWNRFProcessorController inputReceivedProcessedRawErrorRecoveryFrame:]"
- "-[BWNode handleStillImagePrewarmWithSettings:forInput:]"
- "-[BWPhotoEncoderController _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:usedContainerOptionsOut:usedEncodingOptionsOut:mainImageHandleInOut:]"
- "-[BWPhotoEncoderController inputReceivedNewAuxMedia:auxSbuf:attachedMediaKey:primaryImageMetadata:processingFlags:]_block_invoke"
- "-[BWPhotoEncoderControllerInput addAuxSbuf:attachedMediakey:primaryImageMetadata:processingFlags:]"
- "-[BWPhotoEncoderNode handleStillImagePrewarmWithSettings:forInput:]"
- "-[BWPhotonicEngineNode _processRawErrorRecoveryFrameWithNRFProcessorInput:failureMetadata:]"
- "-[BWPhotonicEngineNode _propagateSushiRawDNGDictionaryWithOutputSampleBuffer:requestedDimensions:aspectRatio:requiresGDCInformation:]"
- "-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]"
- "-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke"
- "-[BWPhotonicEngineNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke_2"
- "-[BWPreviewStabilizationNode initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:]"
- "-[BWPreviewStitcherNode _renderCameraTransitionRampToPixelBuffer:bounds:withWiderCameraPixelBuffer:narrowerCameraPixelBuffer:zoomingIn:progress:narrowerCameraBounds:narrowerCameraShift:featherEdges:rampCameraTransition:renderEnhancedFeathering:narrowerCameraEdgeExpansionRamp:qsubToQsumEdgeOpacityRamp:qsubToQsumEdgeOpacityRampFromProgress:]"
- "-[BWStillImageCoordinatorNode _renderSampleBuffer:forInput:attemptToCompleteRequest:]"
- "-[BWUBNode handleStillImagePrewarmWithSettings:forInput:]"
- "-[BWUBNode handleStillImagePrewarmWithSettings:forInput:]_block_invoke"
- "-[BWVariableFrameRateSelector _loadDefaultsWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:]"
- "-[CMInferenceUtils _getNetworkPathWithBasenamePredicate:isE5:embedPlatformDeviceID:fsNetworks:]"
- "-[CMInferenceUtils getNetworkPathForBasenamePredicate:isE5:]"
- "-[FigCaptureCameraSourcePipeline _buildMultiStreamCameraSourcePipeline:graph:renderDelegate:fastModeSwitch:]"
- "-[FigCaptureCameraSourcePipeline _buildVideoCaptureOutputNetwork:previewOutputsBySourceDeviceType:stillImageOutputsByPortType:lightSourceMaskOutputsBySourceDeviceType:keypointDescriptorDataOutputsBySourceDeviceType:pipelineConfiguration:graph:videoCaptureDimensions:numberOfSecondaryFramesToSkip:]"
- "-[FigCaptureCameraSourcePipeline initWithConfiguration:captureDevice:graph:name:renderDelegate:ispFastSwitchEnabled:error:]"
- "-[FigCaptureVISPipeline _buildVISPipelineWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:visProcessingSemaphore:]"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigRemoteQueue/FigRemoteQueue.c"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageCaptureSettings.m %s: Missing capture frame infos"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Portrait/BWVideoDepthInferenceConfiguration.m %s: Unknown layout %d"
- "/System/Library/ImagingNetworks/"
- "04:14:07"
- "<%@ %p> deviceOriented:%d applyHorizontalFlip:%d videoContentMode:%ld includesInvalidContent:%ld cropDesciptor:%@ underlyingVideoFormat:%@ rotationDegrees:%d landscapeOriented:%d"
- "<%@ %p>: captureID:%lld, captureType=%@, %@, errorRecovery=%d original=%d tonemap=%d inferenceInput=%d semanticRendering=%d inferenceInputForProcessing=%d inferences=%d input:<%@ %p>"
- "<<<< BWBackgroundBlurNode >>>> %s: EOD received for configurationID %@ input %@"
- "<<<< BWBravoStreamSelector >>>> %s: CurrentPrimary %@, PTS %.3f, zoomFactor %f, RecommendedPrimary %@, debugOverlayInfo %@"
- "<<<< BWCameraStreamingMonitor >>>> %s: Send camera streaming OFF message to SystemStatus for %u"
- "<<<< BWE5InferenceProvider >>>> %s: Cannot cache provider %@ with custom identifer %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
- "<<<< BWE5InferenceProvider >>>> %s: Failed to create precompiled compute execution stream operation for %@"
- "<<<< BWE5MultipleLayoutInferenceProvider >>>> %s: Cannot cache provider %@ with custom identifer %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
- "<<<< BWEspressoInferenceAdapter >>>> %s: Unsupported layout %d for provider of type %d"
- "<<<< BWEspressoInferenceProvider >>>> %s: Cannot cache provider %@ with custom identifer %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
- "<<<< BWFigVideoCaptureDevice >>>> %s: Digital Flash total integration time: %f"
- "<<<< BWFigVideoCaptureDevice >>>> %s: Found reference frame using method '%d'. ReferenceFrameIndex: %d. SIFRReferenceFrameIndex:%d. Selected range: %d-%d (%d-%d)"
- "<<<< BWFigVideoCaptureDevice >>>> %s: Zero Shutter Lag capture failed due to '%@'"
- "<<<< BWFigVideoCaptureStream >>>> %s: %@: Not sending max exposure duration of kCMTimeInvalid down to stream. Relying on stream default. "
- "<<<< BWFigVideoCaptureStream >>>> %s: %@: Setting maxIntegrationTime to %lld / %ds, %.1fms"
- "<<<< BWFigVideoCaptureStream >>>> %s: Can't update maxExposureDuration before streaming starts. Ignoring."
- "<<<< BWFigVideoCaptureStream >>>> %s: Frame with PTS '%.3f' is (partially) invalid due to loss of sensor access"
- "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Created with priority %d"
- "<<<< BWInferenceEngine >>>> %s: Failed to prewarm inference provider %@"
- "<<<< BWInferenceEngine >>>> %s: Prewarming %@"
- "<<<< BWInferenceScalingRequirement >>>> %s: Attempting to control height dimension for intermediate with interger factor: %zu total height: %zu"
- "<<<< BWInferenceScalingRequirement >>>> %s: Overriding calcutated sequential intermediate format dimensions from (%zux%zu) to (%dx%d)"
- "<<<< BWInferenceVideoScalingProvider >>>> %s: Inference video scaling provider given pixel buffer with size (w:%f h:%f) exceeding attached valid rect size (w:%f h:%f) but not configured to apply a crop"
- "<<<< BWMattingV2InferenceProvider >>>> %s: Cannot cache provider %@ with custom identifer %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
- "<<<< BWMultiStreamCameraSourceNode >>>> %s: %@ %@ %@ %lld / %d"
- "<<<< BWMultiStreamCameraSourceNode >>>> %s: Discontinuity! %@ %.3f"
- "<<<< BWMultiStreamCameraSourceNode >>>> %s: Node output %@ streaming : %d retainedBufferCount = %d"
- "<<<< BWNRFProcessorController >>>> %s: Failed to add frame to NRF processor for '%@' (err=%d). Found error recovery frame: %d"
- "<<<< BWNRFProcessorController >>>> %s: Found error recovery frame '%d' for %@"
- "<<<< BWNRFProcessorController >>>> %s: Ignoring input received processed raw as not processing the error recovery for '%@"
- "<<<< BWPhotoEncoderNode >>>> %s: Received sbuf for captureID:%{public}lld (identifier:%{private}@) while processing capture with identifier:%{private}@, flushing current input"
- "<<<< BWPixelTransferNode >>>> %s: %@: %p: created pixel transfer session %@"
- "<<<< BWStillImageMetadataUtilities >>>> %s: SushiRAW DNG dictionary requested with rawDimensions:%@, rawPixelFormat:%@, requestedDimensions:%@, sushiRawBlackBorderingEnabled:%d, requiresGDCInformation:%d, quadraBinningFactor:%d"
- "<<<< BWStillImageProcessing >>>> %s: Piecemeal encoding not supported for constituent captures"
- "<<<< BWStillImageProcessing >>>> %s: Piecemeal encoding not supported for raw captures"
- "<<<< BWStillImageProcessingNode >>>> %s: Processing raw error recovery frame for captureID:%lld"
- "<<<< BWStillImageProcessingNode >>>> %s: Setting up resource coordinator"
- "<<<< BWStreamingFilterNode >>>> %s: Processing renderListForFrame:%@%@"
- "<<<< BWVideoProcessingInferenceProvider >>>> %s: VideoProcessing returned error %@"
- "<<<< BWVisionInferenceProvider >>>> %s: Cannot cache provider %@ with custom identifer %@ as its identifier does not match the placeholder provider %@ with custom identifier :%@ we are trying to move requirements from"
- "<<<< CMInferenceUtils >>>> %s: Cannot read list of v1 networks"
- "<<<< CMInferenceUtils >>>> %s: Cannot read list of v2/e5rt networks"
- "<<<< CMInferenceUtils >>>> %s: Failed to create reg exp for finding E5/espresso model filesystem URL for %@/%@ (error:%@)!"
- "<<<< CMInferenceUtils >>>> %s: Failed to get device identifier."
- "<<<< CMInferenceUtils >>>> %s: Failed to get platform identifier."
- "<<<< CMInferenceUtils >>>> %s: failed to find < %s > network at < %s >, isE5 : %d"
- "<<<< CMInferenceUtils >>>> %s: failed to find network at < %s >, isE5 : %d"
- "<<<< CMInferenceUtils >>>> %s: fsNetworks nil"
- "<<<< CMInferenceUtils >>>> %s: missing network basename predicate"
- "<<<< FigCaptureCameraSourcePipeline >>>> %s: Low light video: %s"
- "<<<< FigCaptureCameraSourcePipeline >>>> %s: Variable frame rate video: %s / %s"
- "<<<< FigCapturePowerLog >>>> %s: Missing camera stop power event. Camera Streaming Power Events: %@"
- "<<<< FigCaptureSession >>>> %s:    connection: %{public}@"
- "<<<< FigCaptureSession >>>> %s: %{public}@ New configuration: %{public}@"
- "<<<< FigCaptureSession >>>> %s: (%p) prewarmReason: %@, prewarmReasonAllowsHighPriorityLaunch %d, deviceIsLocked: %d, highPriorityLaunch: %d"
- "<<<< FigCaptureSession >>>> %s: Committed configuration same as live one."
- "<<<< FigCaptureSession >>>> %s: Force enable lens smudge detection."
- "<<<< FigCaptureSession >>>> %s: playingApplicationID: %@ is not camera"
- "<<<< FigRemoteQueue >>>> %s: Registering surface id %d timed out, signalling with %d"
- "<<<< FigRemoteQueue >>>> %s: restored incoming voucher %p"
- "@124@0:8Q16Q24Q32i40B44B48B52B56f60B64i68B72B76f80f84i88@92@100B108B112@116"
- "@24@0:8^{OpaqueFigCaptureISPProcessingSession=}16"
- "@28@0:8@?16B24"
- "@28@0:8i16f20i24"
- "@32@0:8@16B24B28"
- "@32@0:8d16f24i28"
- "@40@0:8@?16B24B28@32"
- "@52@0:8@16i24Q28@36@44"
- "An error occurred while I was...\n\nCalled from: %s:%d\nProcess name: %@\nProcess ID: %d\nTime of error: %@"
- "B16@?0@\"NSString\"8"
- "B48@?0@\"ADEspressoImageDescriptor\"8I16B20@\"NSString\"24@\"NSString\"32@\"NSArray\"40"
- "CameraControlsStatsPrimaryPortType"
- "Failed to setup resource coordinator -- all processing will fail! Check logs from -[BWPhotonicEngineNodeResourceCoordinator setupProcessorControllersAndPixelBufferPools] for details"
- "FigRemoteQueue.c"
- "LastShownBuild:BWAudioSourceNode.m:1011"
- "LastShownBuild:BWDeepZoomInferenceProvider.m:521"
- "LastShownBuild:BWDeepZoomProcessorController.m:1045"
- "LastShownBuild:BWDeferredProcessorController.m:862"
- "LastShownBuild:BWDeferredProcessorController.m:906"
- "LastShownBuild:BWDepthConverterNode.m:1062"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:1441"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:2815"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:2866"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3449"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3458"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10164"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10199"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10388"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10409"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10416"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10443"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10503"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10645"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11516"
- "LastShownBuild:BWFigVideoCaptureDevice.m:14554"
- "LastShownBuild:BWFigVideoCaptureDevice.m:17151"
- "LastShownBuild:BWFigVideoCaptureDevice.m:1734"
- "LastShownBuild:BWFigVideoCaptureDevice.m:17532"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18167"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18448"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18450"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21080"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21112"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21251"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22083"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22407"
- "LastShownBuild:BWFigVideoCaptureDevice.m:5273"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7795"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7796"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8018"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8820"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9263"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9713"
- "LastShownBuild:BWFigVideoCaptureStream.m:3263"
- "LastShownBuild:BWFigVideoCaptureStream.m:3675"
- "LastShownBuild:BWFigVideoCaptureSynchronizedStreamsGroup.m:398"
- "LastShownBuild:BWGraph.m:3114"
- "LastShownBuild:BWGraph.m:3164"
- "LastShownBuild:BWGraph.m:3176"
- "LastShownBuild:BWGraph.m:3230"
- "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1139"
- "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1641"
- "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:723"
- "LastShownBuild:BWIrisStagingNode.m:3821"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:12280"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:2421"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:3836"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:3843"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:3850"
- "LastShownBuild:BWNRFProcessorController.m:1574"
- "LastShownBuild:BWNRFProcessorController.m:1575"
- "LastShownBuild:BWNRFProcessorController.m:4398"
- "LastShownBuild:BWPhotoEncoderController.m:1361"
- "LastShownBuild:BWPhotoEncoderController.m:1366"
- "LastShownBuild:BWPhotoEncoderController.m:1593"
- "LastShownBuild:BWPhotoEncoderController.m:1714"
- "LastShownBuild:BWPhotoEncoderController.m:1730"
- "LastShownBuild:BWPhotoEncoderController.m:3248"
- "LastShownBuild:BWPhotoEncoderController.m:3922"
- "LastShownBuild:BWPhotoEncoderController.m:5275"
- "LastShownBuild:BWPhotoEncoderController.m:968"
- "LastShownBuild:BWPhotoEncoderController.m:971"
- "LastShownBuild:BWPhotoEncoderNode.m:369"
- "LastShownBuild:BWPhotonicEngineNode.m:1253"
- "LastShownBuild:BWPhotonicEngineNode.m:1313"
- "LastShownBuild:BWPhotonicEngineNode.m:1416"
- "LastShownBuild:BWPhotonicEngineNode.m:1419"
- "LastShownBuild:BWPhotonicEngineNode.m:1443"
- "LastShownBuild:BWPhotonicEngineNode.m:1822"
- "LastShownBuild:BWPhotonicEngineNode.m:1879"
- "LastShownBuild:BWPhotonicEngineNode.m:2109"
- "LastShownBuild:BWPhotonicEngineNode.m:2119"
- "LastShownBuild:BWPhotonicEngineNode.m:2563"
- "LastShownBuild:BWPhotonicEngineNode.m:2584"
- "LastShownBuild:BWPhotonicEngineNode.m:2587"
- "LastShownBuild:BWPhotonicEngineNode.m:3266"
- "LastShownBuild:BWPhotonicEngineNode.m:3281"
- "LastShownBuild:BWPhotonicEngineNode.m:3392"
- "LastShownBuild:BWPhotonicEngineNode.m:3416"
- "LastShownBuild:BWPhotonicEngineNode.m:4449"
- "LastShownBuild:BWPhotonicEngineNode.m:5145"
- "LastShownBuild:BWPhotonicEngineNode.m:5163"
- "LastShownBuild:BWPhotonicEngineNode.m:601"
- "LastShownBuild:BWPhotonicEngineNode.m:615"
- "LastShownBuild:BWPhotonicEngineNode.m:622"
- "LastShownBuild:BWPhotonicEngineNode.m:7077"
- "LastShownBuild:BWPhotonicEngineNode.m:7079"
- "LastShownBuild:BWPhotonicEngineNode.m:8518"
- "LastShownBuild:BWPhotonicEngineNode.m:8529"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2301"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:345"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:357"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3776"
- "LastShownBuild:BWPhotonicEngineNodeUtilities.m:1244"
- "LastShownBuild:BWSmartStyleRenderingProcessorController.m:808"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1089"
- "LastShownBuild:BWStillImageFilterNode.m:1030"
- "LastShownBuild:BWStillImageFilterNode.m:589"
- "LastShownBuild:BWStillImageFilterNode.m:606"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1210"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1217"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1223"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1241"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1920"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1950"
- "LastShownBuild:BWStillImageMetadataUtilities.m:739"
- "LastShownBuild:BWStillImageMetadataUtilities.m:911"
- "LastShownBuild:BWStillImageMetadataUtilities.m:967"
- "LastShownBuild:BWUBCaptureParameters.m:182"
- "LastShownBuild:BWUBCaptureParameters.m:188"
- "LastShownBuild:BWUBCaptureParameters.m:191"
- "LastShownBuild:BWUBCaptureParameters.m:196"
- "LastShownBuild:BWUBCaptureParameters.m:251"
- "LastShownBuild:BWUtilities.m:932"
- "LastShownBuild:BWVISNode.m:2172"
- "LastShownBuild:BWVISNode.m:2190"
- "LastShownBuild:BWVISNode.m:431"
- "LastShownBuild:BWVisionInferenceProvider.m:379"
- "LastShownBuild:BWVisionInferenceProvider.m:423"
- "LastShownBuild:CMCaptureLocalSessionController.m:724"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1286"
- "LastShownBuild:FigCaptureMetadataUtilities.m:5418"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1411"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1417"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1418"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1422"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1538"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1544"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1547"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1708"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2680"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2755"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2756"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2928"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:2931"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3102"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3105"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3150"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4052"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4058"
- "LastShownBuild:FigCaptureSession.m:10580"
- "LastShownBuild:FigCaptureSession.m:16848"
- "LastShownBuild:FigCaptureSession.m:17675"
- "LastShownBuild:FigCaptureSession.m:21044"
- "LastShownBuild:FigCaptureSession.m:21079"
- "LastShownBuild:FigCaptureSession.m:23364"
- "LastShownBuild:FigCaptureSession.m:4078"
- "LastShownBuild:FigCaptureSession.m:7962"
- "LastShownBuild:FigCaptureSession.m:7968"
- "LastShownBuild:FigCaptureSession.m:7971"
- "LastShownBuild:FigCaptureSession.m:7982"
- "LastShownBuild:FigCaptureSession.m:7995"
- "LastShownBuild:FigCaptureSession.m:8013"
- "LastShownBuild:FigCaptureSession.m:8028"
- "LastShownBuild:FigCaptureSession.m:8041"
- "LastShownBuild:FigCaptureSession.m:8045"
- "LastShownBuild:FigCaptureSession.m:8048"
- "LastShownBuild:FigCaptureSession.m:8142"
- "LastShownBuild:FigCaptureSession.m:8147"
- "LastShownBuild:FigCaptureSession.m:8155"
- "LastShownBuild:FigCaptureSession.m:8159"
- "LastShownBuild:FigCaptureSession.m:8570"
- "LastShownBuild:FigCaptureSession.m:8837"
- "LastShownBuild:FigCaptureSession.m:9642"
- "LastShownBuild:FigCaptureSession.m:9797"
- "LastShownBuild:FigCaptureSessionPipelines.m:617"
- "LastShownBuild:FigCaptureSource.m:1460"
- "LastShownBuild:FigCaptureSource.m:1464"
- "LastShownBuild:FigCaptureSourceBackingsProvider.m:2471"
- "LastShownBuild:FigCaptureSourceServer.m:1897"
- "LastShownBuild:FigCaptureUtilities.m:971"
- "LastShownDate:BWAudioSourceNode.m:1011"
- "LastShownDate:BWDeepZoomInferenceProvider.m:521"
- "LastShownDate:BWDeepZoomProcessorController.m:1045"
- "LastShownDate:BWDeferredProcessorController.m:862"
- "LastShownDate:BWDeferredProcessorController.m:906"
- "LastShownDate:BWDepthConverterNode.m:1062"
- "LastShownDate:BWFigCaptureDeviceVendor.m:1441"
- "LastShownDate:BWFigCaptureDeviceVendor.m:2815"
- "LastShownDate:BWFigCaptureDeviceVendor.m:2866"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3449"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3458"
- "LastShownDate:BWFigVideoCaptureDevice.m:10164"
- "LastShownDate:BWFigVideoCaptureDevice.m:10199"
- "LastShownDate:BWFigVideoCaptureDevice.m:10388"
- "LastShownDate:BWFigVideoCaptureDevice.m:10409"
- "LastShownDate:BWFigVideoCaptureDevice.m:10416"
- "LastShownDate:BWFigVideoCaptureDevice.m:10443"
- "LastShownDate:BWFigVideoCaptureDevice.m:10503"
- "LastShownDate:BWFigVideoCaptureDevice.m:10645"
- "LastShownDate:BWFigVideoCaptureDevice.m:11516"
- "LastShownDate:BWFigVideoCaptureDevice.m:14554"
- "LastShownDate:BWFigVideoCaptureDevice.m:17151"
- "LastShownDate:BWFigVideoCaptureDevice.m:1734"
- "LastShownDate:BWFigVideoCaptureDevice.m:17532"
- "LastShownDate:BWFigVideoCaptureDevice.m:18167"
- "LastShownDate:BWFigVideoCaptureDevice.m:18448"
- "LastShownDate:BWFigVideoCaptureDevice.m:18450"
- "LastShownDate:BWFigVideoCaptureDevice.m:21080"
- "LastShownDate:BWFigVideoCaptureDevice.m:21112"
- "LastShownDate:BWFigVideoCaptureDevice.m:21251"
- "LastShownDate:BWFigVideoCaptureDevice.m:22083"
- "LastShownDate:BWFigVideoCaptureDevice.m:22407"
- "LastShownDate:BWFigVideoCaptureDevice.m:5273"
- "LastShownDate:BWFigVideoCaptureDevice.m:7795"
- "LastShownDate:BWFigVideoCaptureDevice.m:7796"
- "LastShownDate:BWFigVideoCaptureDevice.m:8018"
- "LastShownDate:BWFigVideoCaptureDevice.m:8820"
- "LastShownDate:BWFigVideoCaptureDevice.m:9263"
- "LastShownDate:BWFigVideoCaptureDevice.m:9713"
- "LastShownDate:BWFigVideoCaptureStream.m:3263"
- "LastShownDate:BWFigVideoCaptureStream.m:3675"
- "LastShownDate:BWFigVideoCaptureSynchronizedStreamsGroup.m:398"
- "LastShownDate:BWGraph.m:3114"
- "LastShownDate:BWGraph.m:3164"
- "LastShownDate:BWGraph.m:3176"
- "LastShownDate:BWGraph.m:3230"
- "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1139"
- "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1641"
- "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:723"
- "LastShownDate:BWIrisStagingNode.m:3821"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:12280"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:2421"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:3836"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:3843"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:3850"
- "LastShownDate:BWNRFProcessorController.m:1574"
- "LastShownDate:BWNRFProcessorController.m:1575"
- "LastShownDate:BWNRFProcessorController.m:4398"
- "LastShownDate:BWPhotoEncoderController.m:1361"
- "LastShownDate:BWPhotoEncoderController.m:1366"
- "LastShownDate:BWPhotoEncoderController.m:1593"
- "LastShownDate:BWPhotoEncoderController.m:1714"
- "LastShownDate:BWPhotoEncoderController.m:1730"
- "LastShownDate:BWPhotoEncoderController.m:3248"
- "LastShownDate:BWPhotoEncoderController.m:3922"
- "LastShownDate:BWPhotoEncoderController.m:5275"
- "LastShownDate:BWPhotoEncoderController.m:968"
- "LastShownDate:BWPhotoEncoderController.m:971"
- "LastShownDate:BWPhotoEncoderNode.m:369"
- "LastShownDate:BWPhotonicEngineNode.m:1253"
- "LastShownDate:BWPhotonicEngineNode.m:1313"
- "LastShownDate:BWPhotonicEngineNode.m:1416"
- "LastShownDate:BWPhotonicEngineNode.m:1419"
- "LastShownDate:BWPhotonicEngineNode.m:1443"
- "LastShownDate:BWPhotonicEngineNode.m:1822"
- "LastShownDate:BWPhotonicEngineNode.m:1879"
- "LastShownDate:BWPhotonicEngineNode.m:2109"
- "LastShownDate:BWPhotonicEngineNode.m:2119"
- "LastShownDate:BWPhotonicEngineNode.m:2563"
- "LastShownDate:BWPhotonicEngineNode.m:2584"
- "LastShownDate:BWPhotonicEngineNode.m:2587"
- "LastShownDate:BWPhotonicEngineNode.m:3266"
- "LastShownDate:BWPhotonicEngineNode.m:3281"
- "LastShownDate:BWPhotonicEngineNode.m:3392"
- "LastShownDate:BWPhotonicEngineNode.m:3416"
- "LastShownDate:BWPhotonicEngineNode.m:4449"
- "LastShownDate:BWPhotonicEngineNode.m:5145"
- "LastShownDate:BWPhotonicEngineNode.m:5163"
- "LastShownDate:BWPhotonicEngineNode.m:601"
- "LastShownDate:BWPhotonicEngineNode.m:615"
- "LastShownDate:BWPhotonicEngineNode.m:622"
- "LastShownDate:BWPhotonicEngineNode.m:7077"
- "LastShownDate:BWPhotonicEngineNode.m:7079"
- "LastShownDate:BWPhotonicEngineNode.m:8518"
- "LastShownDate:BWPhotonicEngineNode.m:8529"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2301"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:345"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:357"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3776"
- "LastShownDate:BWPhotonicEngineNodeUtilities.m:1244"
- "LastShownDate:BWSmartStyleRenderingProcessorController.m:808"
- "LastShownDate:BWStillImageCoordinatorNode.m:1089"
- "LastShownDate:BWStillImageFilterNode.m:1030"
- "LastShownDate:BWStillImageFilterNode.m:589"
- "LastShownDate:BWStillImageFilterNode.m:606"
- "LastShownDate:BWStillImageMetadataUtilities.m:1210"
- "LastShownDate:BWStillImageMetadataUtilities.m:1217"
- "LastShownDate:BWStillImageMetadataUtilities.m:1223"
- "LastShownDate:BWStillImageMetadataUtilities.m:1241"
- "LastShownDate:BWStillImageMetadataUtilities.m:1920"
- "LastShownDate:BWStillImageMetadataUtilities.m:1950"
- "LastShownDate:BWStillImageMetadataUtilities.m:739"
- "LastShownDate:BWStillImageMetadataUtilities.m:911"
- "LastShownDate:BWStillImageMetadataUtilities.m:967"
- "LastShownDate:BWUBCaptureParameters.m:182"
- "LastShownDate:BWUBCaptureParameters.m:188"
- "LastShownDate:BWUBCaptureParameters.m:191"
- "LastShownDate:BWUBCaptureParameters.m:196"
- "LastShownDate:BWUBCaptureParameters.m:251"
- "LastShownDate:BWUtilities.m:932"
- "LastShownDate:BWVISNode.m:2172"
- "LastShownDate:BWVISNode.m:2190"
- "LastShownDate:BWVISNode.m:431"
- "LastShownDate:BWVisionInferenceProvider.m:379"
- "LastShownDate:BWVisionInferenceProvider.m:423"
- "LastShownDate:CMCaptureLocalSessionController.m:724"
- "LastShownDate:FigCaptureMetadataUtilities.m:1286"
- "LastShownDate:FigCaptureMetadataUtilities.m:5418"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1411"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1417"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1418"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1422"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1538"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1544"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1547"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1708"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2680"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2755"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2756"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2928"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:2931"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3102"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3105"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3150"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4052"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4058"
- "LastShownDate:FigCaptureSession.m:10580"
- "LastShownDate:FigCaptureSession.m:16848"
- "LastShownDate:FigCaptureSession.m:17675"
- "LastShownDate:FigCaptureSession.m:21044"
- "LastShownDate:FigCaptureSession.m:21079"
- "LastShownDate:FigCaptureSession.m:23364"
- "LastShownDate:FigCaptureSession.m:4078"
- "LastShownDate:FigCaptureSession.m:7962"
- "LastShownDate:FigCaptureSession.m:7968"
- "LastShownDate:FigCaptureSession.m:7971"
- "LastShownDate:FigCaptureSession.m:7982"
- "LastShownDate:FigCaptureSession.m:7995"
- "LastShownDate:FigCaptureSession.m:8013"
- "LastShownDate:FigCaptureSession.m:8028"
- "LastShownDate:FigCaptureSession.m:8041"
- "LastShownDate:FigCaptureSession.m:8045"
- "LastShownDate:FigCaptureSession.m:8048"
- "LastShownDate:FigCaptureSession.m:8142"
- "LastShownDate:FigCaptureSession.m:8147"
- "LastShownDate:FigCaptureSession.m:8155"
- "LastShownDate:FigCaptureSession.m:8159"
- "LastShownDate:FigCaptureSession.m:8570"
- "LastShownDate:FigCaptureSession.m:8837"
- "LastShownDate:FigCaptureSession.m:9642"
- "LastShownDate:FigCaptureSession.m:9797"
- "LastShownDate:FigCaptureSessionPipelines.m:617"
- "LastShownDate:FigCaptureSource.m:1460"
- "LastShownDate:FigCaptureSource.m:1464"
- "LastShownDate:FigCaptureSourceBackingsProvider.m:2471"
- "LastShownDate:FigCaptureSourceServer.m:1897"
- "LastShownDate:FigCaptureUtilities.m:971"
- "MOC %p: <%@>%@ -> <%@> E:%d MetadataIdentifiers:{%@}%@%@%@%@%@%@%@%@%@%@%@"
- "May 30 2025"
- "Missing camera stop power event. Camera Streaming Power Events: %@"
- "NOT"
- "QSubFlavor:%d"
- "Received sbuf for captureID:%{public}lld (identifier:%{private}@) while processing capture with identifier:%{private}@, flushing current input"
- "Receiving aux media {%@}"
- "T@\"BWFigCaptureISPProcessingSession\",R,N,V_ispProcessingSession"
- "T@\"NSMutableDictionary\",R,N,V_stashedAttacheMediaSampleBuffersByAttachedMediaKey"
- "TB,R,V_hasSuccessfullySetupProcessorControllersAndMemoryResources"
- "[21{BWStreamOutputStorage=\"type\"i\"flags\"I\"ready\"B\"enabled\"B\"nodeOutput\"@\"BWNodeOutput\"\"simpleQueue\"^{opaqueCMSimpleQueue}\"bufferServicingQueue\"@\"NSObject<OS_dispatch_queue>\"\"bufferServicingQueueCallback\"^?\"cachedFormatDescription\"^{opaqueCMFormatDescription}\"lastEmittedPTS\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"frameCounter\"@\"FigCaptureFrameCounter\"\"retainedBufferCount\"i\"streamRetainedBufferCount\"i\"internalPixelBufferPool\"@\"BWPixelBufferPool\"\"bufferPoolOwnedByAnotherNode\"B\"bytesPerRowAlignmentRequirement\"i\"planeAlignmentRequirement\"i\"sensorInterfaceRawPixelFormat\"I\"sashimiRawPixelFormat\"I\"sushiRawPixelFormat\"I\"outputDimensions\"{?=\"width\"i\"height\"i}\"cropRect\"{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}\"lastISPAppliedZoomFactor\"f\"ioSurfaceCompressionRatioStats\"@\"BWStats\"\"pixelBufferCompressionType\"i\"totalCompressedDataSize\"Q\"totalUncompressedDataSize\"Q\"lumaCompressionHistogram\"[16Q]\"chromaCompressionHistogram\"[16Q]\"universalCompressionNumberOfSamples\"I\"lastUniversalCompressionSamplePTS\"{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}\"pixelFormatIsTenBit\"B\"pixelFormatIs420\"B\"pixelFormatIsLossyCompression\"B\"prefetchEnabled\"B\"incrementalPrefetchEnabled\"B\"prevSceneIlluminationValue\"I\"prevSceneIlluminationValueCaptureID\"i}]"
- "_attachCameraControlsStatisticsPrimaryPortType"
- "_encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:usedContainerOptionsOut:usedEncodingOptionsOut:mainImageHandleInOut:"
- "_getNetworkPath:isE5:embedPlatformDeviceID:fsNetworks:"
- "_getNetworkPathWithBasenamePredicate:isE5:embedPlatformDeviceID:fsNetworks:"
- "_metalSubmissionAndCompletionQueue"
- "_prewarming"
- "_prewarmingLock"
- "_sourceDeviceTypesWithLightSourceMaskAndKeypointDescriptorDataEnabledOnVideoCaptureOutputs"
- "addAdaptiveUnifiedBracketedCaptureParams:preBracketFrameCaptureParams:bracketedCaptureFrameInfos:"
- "addAuxSbuf:attachedMediakey:primaryImageMetadata:processingFlags:"
- "cameraCaptureAttributions"
- "cinematicFramingVirtualCameraConfiguration"
- "clientMaxContinuousZoomFactorForDepthDataDelivery"
- "com.apple.coremedia.previewsink.personsegmentation-metal-command-queue"
- "com.apple.coremedia.previewsink.pocketdetection-metal-command-queue"
- "com.apple.coremedia.previewsink.registration-metal-command-queue"
- "copyWithSwappedDimensions"
- "description=CameraCapture-650.0.0.122.4"
- "didChangeDeskViewCameraZoomFactor:"
- "emitStillImagePrewarmMessageWithSettings:"
- "enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processOriginalImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:"
- "frameParametersWithIntegrationTimeInMicroseconds:gain:maxAGC:"
- "frameParametersWithIntegrationTimeInSeconds:gain:maxAGC:"
- "getNetworkPathForBasenamePredicate:isE5:"
- "handleStillImagePrewarmWithSettings:forInput:"
- "i132@0:8i16^{__CVBuffer=}20{?=ii}28I36@40@48@56@64{CGRect={CGPoint=dd}{CGSize=dd}}72B104^@108^@116^q124"
- "i16@?0^{FigCaptureSourceStorage=qiCC{?=[8I]}^{OpaqueFigSimpleMutex}@q^{__CFString}@i@@@@^{OpaqueFigCaptureSource}f@@@i^{OpaqueFigFlashlight}@iBBB@BB}8"
- "i40@0:8@\"BWNRFProcessorController\"16@\"BWNRFProcessorInput\"24@\"NSDictionary\"32"
- "i68@0:8@16@24B32B36B40B44i48B52B56B60B64"
- "initWithCameraInfoByPortType:forStillImagePreview:updateFinalCropRectWithStabilizationShift:"
- "initWithFigCaptureISPProcessingSession:"
- "initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:autoTrimMethod:vitalityScoringEnabled:captureDeviceHasOverCaptureEnabled:overCaptureEnabled:depthEnabled:videoStabilizationOverscanOverride:sequenceAdjusterEnabled:visMotionMetadataPreloadingMode:frameReconstructionEnabled:subjectRelightingEnabled:intermediateJPEGCompressionQuality:intermediateJPEGCompressionRate:maxLossyCompressionLevel:temporaryMovieDirectoryURL:cameraInfoByPortType:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:irisRequestDelegate:"
- "initWithPortType:captureType:captureFlags:adaptiveBracketingParameters:sphereOffsets:"
- "initWithPortTypes:forParameters:frameRateSwitchBasedOnMotionDisabled:"
- "inputReceivedNewAuxMedia:auxSbuf:attachedMediaKey:primaryImageMetadata:processingFlags:"
- "inputReceivedProcessedRawErrorRecoveryFrame:"
- "integrationTimeInMiroseconds"
- "metalPreviewDispatchQueue"
- "newMessageWithStillImageSettings:"
- "processorController:processRawErrorRecoveryFrameForProcessorInput:failureMetadata:"
- "removeCameraCaptureAttribution:"
- "setProcessedRawErrorRecoveryFrame:"
- "setupResourceCoordinator"
- "stashedAttacheMediaSampleBuffersByAttachedMediaKey"
- "supportedSourceFormats"
- "supportsCroppingDepthToPrimaryCaptureAspectRatio"

```
