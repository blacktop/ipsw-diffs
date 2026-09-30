## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-  __TEXT.__text: 0x8c0df8
-  __TEXT.__objc_methlist: 0x3a488
-  __TEXT.__const: 0x151780
-  __TEXT.__cstring: 0xfe485
-  __TEXT.__oslogstring: 0x1651cd
-  __TEXT.__gcc_except_tab: 0x4988
+  __TEXT.__text: 0x8c4fc0
+  __TEXT.__objc_methlist: 0x3a578
+  __TEXT.__const: 0x151770
+  __TEXT.__cstring: 0xff0b4
+  __TEXT.__oslogstring: 0x16645a
+  __TEXT.__gcc_except_tab: 0x4a94
   __TEXT.__dlopen_cstrs: 0x7ad
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x11e60
+  __TEXT.__unwind_info: 0x11eb0
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11270
-  __DATA_CONST.__objc_classlist: 0x1ef0
+  __DATA_CONST.__const: 0x11328
+  __DATA_CONST.__objc_classlist: 0x1ef8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x628
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17478
+  __DATA_CONST.__objc_selrefs: 0x174f0
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x1d08
-  __DATA_CONST.__objc_arraydata: 0x3bb8
-  __DATA_CONST.__got: 0x6db8
+  __DATA_CONST.__objc_superrefs: 0x1d10
+  __DATA_CONST.__objc_arraydata: 0x3bc8
+  __DATA_CONST.__got: 0x7058
   __AUTH_CONST.__const: 0x4a58
-  __AUTH_CONST.__cfstring: 0x58da0
-  __AUTH_CONST.__objc_const: 0xa6388
+  __AUTH_CONST.__cfstring: 0x590a0
+  __AUTH_CONST.__objc_const: 0xa67d0
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x6558
-  __AUTH_CONST.__objc_arrayobj: 0x2c58
+  __AUTH_CONST.__objc_intobj: 0x6540
+  __AUTH_CONST.__objc_arrayobj: 0x2c70
   __AUTH_CONST.__objc_floatobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x1798
   __AUTH_CONST.__objc_doubleobj: 0xab0
-  __AUTH_CONST.__auth_got: 0x2da8
-  __AUTH.__objc_data: 0x4150
-  __DATA.__objc_ivar: 0xbd4c
-  __DATA.__data: 0x5980
+  __AUTH_CONST.__auth_got: 0x2db0
+  __AUTH.__objc_data: 0x3b10
+  __AUTH.__data: 0x110
+  __DATA.__objc_ivar: 0xbdb0
+  __DATA.__data: 0x5958
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x2c70
-  __DATA.__bss: 0x2e08
-  __DATA_DIRTY.__objc_data: 0xf410
-  __DATA_DIRTY.__data: 0x1080
-  __DATA_DIRTY.__common: 0x1b0
-  __DATA_DIRTY.__bss: 0x1558
+  __DATA.__common: 0x2c40
+  __DATA.__bss: 0x2df8
+  __DATA_DIRTY.__objc_data: 0xfaa0
+  __DATA_DIRTY.__data: 0xf98
+  __DATA_DIRTY.__common: 0x1e0
+  __DATA_DIRTY.__bss: 0x1588
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 41492
-  Symbols:   137217
-  CStrings:  50105
+  Functions: 41535
+  Symbols:   137388
+  CStrings:  50211
 
Sections:
~ __TEXT.__dlopen_cstrs : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ +[FigCaptureCustomExposureConfiguration exposureConfigurationWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:requestID:]
+ -[BWDeferredBufferIntermediate compressionCropRect]
+ -[BWDeferredBufferIntermediate initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:compressionProfile:compressionCropRect:URL:]
+ -[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:portType:]
+ -[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]
+ -[BWE5InferenceProvider _configureANEExecutionPriorityOnEspressoStream]
+ -[BWEspressoE5InferenceCamGazePropagator allowsAsyncPropagation]
+ -[BWEspressoE5InferenceCamGazePropagator dealloc]
+ -[BWEspressoE5InferenceCamGazePropagator initWithCamGazeRequirement:camGazeSizeBytes:maxFaces:faceIndex:]
+ -[BWEspressoE5InferenceCamGazePropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:]
+ -[BWEspressoInferenceProvider _configureANEExecutionPriorityOnEspressoPlan]
+ -[BWFaceTrackingNode hasNonLiveConfigurationChanges]
+ -[BWFigVideoCaptureDevice _ubIsMacroFlashQSubSwitchingCaptureType:portType:sceneFlags:]
+ -[BWFigVideoCaptureDevice _updateExposureStateForAutofocusProperty:propertyValue:]
+ -[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:normalizedRectOfInterest:]
+ -[BWFigVideoCaptureStream lastZoomFactorQuadraSubPixelSwitchingSupported]
+ -[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]
+ -[BWGraph waitForStartOrCommitToCompleteWithWillBeStoppedImmediately:]
+ -[BWMultiFilterThumbnailNode didReachEndOfDataForConfigurationID:input:]
+ -[BWMultiStreamCameraSourceNode makeOutputsLiveWithWillBeStoppedImmediately:]
+ -[BWNondisruptiveSwitchingFormatSelector lastZoomFactorFormatIndexIgnoringZoomFactorAndQuadraSubPixelSceneMonitoring]
+ -[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:piecemealEncodingMode:]
+ -[BWPhotonicEngineNode _piecemealEncodeAttachedMediaByKey:primarySbuf:portType:piecemealEncodingMode:]
+ -[BWPhotonicEngineNodeResourceCoordinator _allocateMetalHeap:metalAllocatorDescriptor:settings:]
+ -[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:camGazeInferenceType:]
+ -[BWSoftISPProcessorController _addFrame:preparedMaxOutputDimensions:]
+ -[BWSoftISPProcessorController _outputBufferRectWithinSensorCropRectForFrame:preparedMaxOutputDimensions:]
+ -[BWSourceNode makeOutputsLiveWithWillBeStoppedImmediately:]
+ -[BWSourceNode transitionStateForMakeOutputsLiveWithWillBeStoppedImmediately:]
+ -[BWStillImageCoordinatorNode _shouldServiceRequest]
+ -[BWStillImageCoordinatorRequest setShouldServiceBeforeGraphStop:]
+ -[BWStillImageCoordinatorRequest shouldServiceBeforeGraphStop]
+ -[BWUBCaptureParameters digitalFlashAvailableNormalizedSNRHysteresisLag]
+ -[BWUBCaptureParameters digitalFlashAvailableNormalizedSNRThreshold]
+ -[BWUBCaptureParameters digitalFlashRecommendedNormalizedSNRHysteresisLag]
+ -[BWUBCaptureParameters digitalFlashRecommendedNormalizedSNRThreshold]
+ -[BWUBCaptureParameters stationaryDigitalFlashRecommendedNormalizedSNRHysteresisLag]
+ -[BWUBCaptureParameters stationaryDigitalFlashRecommendedNormalizedSNRThreshold]
+ -[FigCaptureCameraSourcePipeline _insertDockKitNodeWithPipelineConfiguration:videoOutputsBySourceDeviceType:graph:]
+ -[FigCaptureCustomExposureConfiguration _initWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:requestID:]
+ -[FigCaptureSourceAttributes ispMBNRSupported]
+ GCC_except_table103
+ GCC_except_table172
+ GCC_except_table191
+ GCC_except_table236
+ GCC_except_table283
+ GCC_except_table327
+ GCC_except_table332
+ GCC_except_table337
+ GCC_except_table343
+ GCC_except_table383
+ GCC_except_table422
+ GCC_except_table450
+ GCC_except_table499
+ GCC_except_table523
+ GCC_except_table544
+ GCC_except_table546
+ GCC_except_table551
+ GCC_except_table554
+ GCC_except_table556
+ GCC_except_table558
+ GCC_except_table686
+ GCC_except_table70
+ _BWPhotoEncoderPiecemealEncodingModeToShortString
+ _BWPhotoEncoderSupportsPiecemealEncoding
+ _BWUtilitiesSmartStyleTuningParameterVariantForCaptureType
+ _FigCFNumberCreateSInt64
+ _FigCaptureMetadataGetManufacturerAndMarketingName.sPhysicalHardwareNameString
+ _FigImageControl_SetExposureAreaOfInterest
+ _OBJC_CLASS_$_BWEspressoE5InferenceCamGazePropagator
+ _OBJC_IVAR_$_BWDeferredBufferIntermediate._compressionCropRect
+ _OBJC_IVAR_$_BWEspressoE5InferenceCamGazePropagator._camGazeOutputElementCount
+ _OBJC_IVAR_$_BWEspressoE5InferenceCamGazePropagator._camGazeRequirement
+ _OBJC_IVAR_$_BWEspressoE5InferenceCamGazePropagator._camGazeSizeBytes
+ _OBJC_IVAR_$_BWEspressoE5InferenceCamGazePropagator._faceIndex
+ _OBJC_IVAR_$_BWEspressoE5InferenceCamGazePropagator._maxFaces
+ _OBJC_IVAR_$_BWFaceDetectionNode._liveRotationDegrees
+ _OBJC_IVAR_$_BWFaceDetectionNode._preparedRotationDegrees
+ _OBJC_IVAR_$_BWFaceTrackingNode._liveRotationDegrees
+ _OBJC_IVAR_$_BWFaceTrackingNode._preparedRotationDegrees
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._autofocusCachedPropertiesCounter
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._autofocusCachedPropertiesOrder
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._digitalFlashAvailableSceneByPortType
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._digitalFlashRecommendedSceneByPortType
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._stationaryDigitalFlashRecommendedSceneByPortType
+ _OBJC_IVAR_$_BWFileCoordinatorNode._firstAudioHasBeenProcessedForIndex
+ _OBJC_IVAR_$_BWFileCoordinatorNode._haveSeenAudioWhenStartingForIndex
+ _OBJC_IVAR_$_BWFileCoordinatorNode._lowLatencyCanTransitionEarlyToRecordingForIndex
+ _OBJC_IVAR_$_BWNRFProcessorController._lastSelectedFusionMode
+ _OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._camGazeInferenceType
+ _OBJC_IVAR_$_BWSmartStyleLearningNode._thumbnailsGenerationCommandQueue
+ _OBJC_IVAR_$_BWStillImageCoordinatorRequest._shouldServiceBeforeGraphStop
+ _OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashAvailableNormalizedSNRHysteresisLag
+ _OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashAvailableNormalizedSNRThreshold
+ _OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashRecommendedNormalizedSNRHysteresisLag
+ _OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashRecommendedNormalizedSNRThreshold
+ _OBJC_IVAR_$_BWUBCaptureParameters._stationaryDigitalFlashRecommendedNormalizedSNRHysteresisLag
+ _OBJC_IVAR_$_BWUBCaptureParameters._stationaryDigitalFlashRecommendedNormalizedSNRThreshold
+ _OBJC_IVAR_$_FigCaptureCameraSourcePipeline._usingVideoCaptureOutputNetworkCrossoverNodeForPreview
+ _OBJC_IVAR_$_FigCaptureMemoryReporter._stuckMMAssertionStartTime
+ _OBJC_IVAR_$_FigCaptureMemoryReporter._ttrFiledForStuckMMAssertion
+ _OBJC_IVAR_$_FigCaptureSourceAttributes._ispMBNRSupported
+ _OBJC_METACLASS_$_BWEspressoE5InferenceCamGazePropagator
+ __OBJC_$_INSTANCE_METHODS_BWEspressoE5InferenceCamGazePropagator
+ __OBJC_$_INSTANCE_VARIABLES_BWEspressoE5InferenceCamGazePropagator
+ __OBJC_$_PROP_LIST_BWEspressoE5InferenceCamGazePropagator
+ __OBJC_CLASS_PROTOCOLS_$_BWEspressoE5InferenceCamGazePropagator
+ __OBJC_CLASS_RO_$_BWEspressoE5InferenceCamGazePropagator
+ __OBJC_METACLASS_RO_$_BWEspressoE5InferenceCamGazePropagator
+ ___129-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:piecemealEncodingMode:]_block_invoke
+ ___278-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]_block_invoke
+ ___326-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]_block_invoke
+ ___63-[BWFigVideoCaptureDevice _setupAutofocusSampleBufferProcessor]_block_invoke
+ ___77-[BWMultiStreamCameraSourceNode makeOutputsLiveWithWillBeStoppedImmediately:]_block_invoke
+ ___91-[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:normalizedRectOfInterest:]_block_invoke
+ ___block_descriptor_40_e8_32o_e11_q24?0816ls32l8
+ ___block_descriptor_65_e8_32b_e5_v8?0ls32l8
+ ___block_descriptor_69_e14_v24?0i8B12q16l
+ ___block_descriptor_73_e8_32o40r48r56r64r_e5_v8?0ls32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_80_e8_32o40r_e5_v8?0ls32l8r40l8
+ _initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:.onceToken
+ _kFigCaptureStreamProperty_RatioBehavior
+ _kFigImageControlSampleBufferProcessorProperty_ExposureAreaOfInterest
+ _kFigProVideoStorageNotificationPayloadKey_BusyFlags
+ _kFigProVideoStorageNotification_BusyReasons
+ _kFigProVideoStorageProperty_BusyReasons
+ _kFigVideoStabilizationSampleBufferAttachmentKey_StabilizationTransformsParameters
+ _kFigVirtualCaptureCardMaximumCapacityComponentsKey_MaximumCapacity
+ _kFigVirtualCaptureCardMaximumCapacityComponentsKey_PurgeableSpace
+ _kFigVirtualCaptureCardProperty_MaximumCapacityComponents
+ _kFigVirtualCaptureCardProperty_MaximumCapacityComponentsExcludingPurgeable
+ _kFigVirtualCaptureCardSetCapacityOption_ReplenishMode
+ _kFigVirtualCaptureCardXPCMsgParam_SetCapacityOptions
+ _mscsn_shouldReflectStillSampleBufferOnStreamingOutputs
+ _objc_msgSend$_initWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:requestID:
+ _objc_msgSend$blendWithAlphaMaskFilter
+ _objc_msgSend$commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:portType:
+ _objc_msgSend$commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:
+ _objc_msgSend$digitalFlashAvailableNormalizedSNRHysteresisLag
+ _objc_msgSend$digitalFlashAvailableNormalizedSNRThreshold
+ _objc_msgSend$digitalFlashRecommendedNormalizedSNRHysteresisLag
+ _objc_msgSend$digitalFlashRecommendedNormalizedSNRThreshold
+ _objc_msgSend$initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:compressionProfile:compressionCropRect:URL:
+ _objc_msgSend$initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:
+ _objc_msgSend$initWithSinkID:captureDevice:inferenceScheduler:camGazeInferenceType:
+ _objc_msgSend$inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:piecemealEncodingMode:
+ _objc_msgSend$lastZoomFactorFormatIndexIgnoringZoomFactorAndQuadraSubPixelSceneMonitoring
+ _objc_msgSend$lastZoomFactorQuadraSubPixelSwitchingSupported
+ _objc_msgSend$makeOutputsLiveWithWillBeStoppedImmediately:
+ _objc_msgSend$maximumHeight
+ _objc_msgSend$maximumWidth
+ _objc_msgSend$setExposureModeCustomWithConfiguration:normalizedRectOfInterest:
+ _objc_msgSend$setShouldServiceBeforeGraphStop:
+ _objc_msgSend$shouldServiceBeforeGraphStop
+ _objc_msgSend$stationaryDigitalFlashRecommendedNormalizedSNRHysteresisLag
+ _objc_msgSend$stationaryDigitalFlashRecommendedNormalizedSNRThreshold
+ _objc_msgSend$transitionStateForMakeOutputsLiveWithWillBeStoppedImmediately:
+ _objc_msgSend$waitForStartOrCommitToCompleteWithWillBeStoppedImmediately:
+ _vcc_copyMaximumCapacityComponents
+ _vcc_postBusyFlagsNotification
- +[FigCaptureCustomExposureConfiguration exposureConfigurationWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:normalizedRectOfInterest:requestID:]
- -[BWDeferredBufferIntermediate initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:compressionProfile:URL:]
- -[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:portType:]
- -[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]
- -[BWFigVideoCaptureDevice _updateExposureStateForAutofocusProperty:]
- -[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:]
- -[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]
- -[BWLearnSmartStyleRenderer _tuningParameterVariantForCaptureType:captureFlags:]
- -[BWMultiFilterThumbnailNode didReachEndOfDataForInput:]
- -[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:]
- -[BWPhotonicEngineNode _piecemealEncodeAttachedMediaByKey:primarySbuf:portType:]
- -[BWPortraitAutoSuggest _adjustMetadataOfSampleBuffer:]
- -[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:]
- -[BWSmartStyleRenderingProcessorController _tuningParameterVariantForCaptureType:captureFlags:]
- -[BWSmartStyleTargetRenderer _tuningParameterVariantForCaptureType:captureFlags:]
- -[BWSoftISPProcessorController _addFrame:]
- -[BWSoftISPProcessorController _outputBufferRectWithinSensorCropRectForFrame:]
- -[BWSourceNode transitionStateForMakeOutputsLiveIfNeeded]
- -[FigCaptureCameraSourcePipeline _insertDockKitNodeWithPipelineConfiguration:graph:]
- -[FigCaptureCustomExposureConfiguration _initWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:normalizedRectOfInterest:requestID:]
- -[FigCaptureCustomExposureConfiguration normalizedRectOfInterest]
- -[FigCaptureCustomExposureConfiguration sensorSpaceRectOfInterest]
- -[FigCaptureCustomExposureConfiguration setSensorSpaceRectOfInterest:]
- -[FigCaptureSourceExtendedAttributes ispMBNRSupported]
- GCC_except_table134
- GCC_except_table171
- GCC_except_table235
- GCC_except_table282
- GCC_except_table325
- GCC_except_table330
- GCC_except_table341
- GCC_except_table381
- GCC_except_table401
- GCC_except_table420
- GCC_except_table449
- GCC_except_table498
- GCC_except_table521
- GCC_except_table543
- GCC_except_table545
- GCC_except_table550
- GCC_except_table553
- GCC_except_table555
- GCC_except_table557
- GCC_except_table684
- GCC_except_table77
- GCC_except_table92
- _BWPhotoEncoderSupportsPiecemealEnocding
- _FigImageControl_SetAutoExposureAreaOfInterest
- _FigImageControl_SetSpotMeteringAreaOfInterest
- _OBJC_IVAR_$_BWFaceDetectionNode._rotationDegrees
- _OBJC_IVAR_$_BWFaceTrackingNode._rotationDegrees
- _OBJC_IVAR_$_BWFigVideoCaptureDevice._isCachedExposureRectForSpotMetering
- _OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._wideMinimumValidFocusDistance
- _OBJC_IVAR_$_FigCaptureCustomExposureConfiguration._normalizedRectOfInterest
- _OBJC_IVAR_$_FigCaptureCustomExposureConfiguration._sensorSpaceRectOfInterest
- _OBJC_IVAR_$_FigCaptureSourceExtendedAttributes._ispMBNRSupported
- _OUTLINED_FUNCTION_735
- _OUTLINED_FUNCTION_736
- _OUTLINED_FUNCTION_737
- _OUTLINED_FUNCTION_738
- _OUTLINED_FUNCTION_739
- _OUTLINED_FUNCTION_740
- _OUTLINED_FUNCTION_741
- ___124-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:]_block_invoke
- ___256-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]_block_invoke
- ___306-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]_block_invoke
- ___56-[BWMultiStreamCameraSourceNode makeOutputsLiveIfNeeded]_block_invoke
- ___66-[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:]_block_invoke
- ___block_descriptor_64_e14_v24?0i8B12q16l
- ___block_descriptor_65_e8_32o40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
- _initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:.onceToken
- _kFigImageControlSampleBufferProcessorProperty_AutoExposureAreaOfInterest
- _kFigImageControlSampleBufferProcessorProperty_SpotMeteredExposureAreaOfInterest
- _kFigVideoStabilizationSampleBufferAttachmentKey_GPUTransformsParameters
- _kFigVirtualCaptureCardProperty_MaximumCapacity
- _objc_msgSend$_initWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:normalizedRectOfInterest:requestID:
- _objc_msgSend$blendWithMaskFilter
- _objc_msgSend$commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:portType:
- _objc_msgSend$commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:
- _objc_msgSend$initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:compressionProfile:URL:
- _objc_msgSend$initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:
- _objc_msgSend$initWithSinkID:captureDevice:inferenceScheduler:
- _objc_msgSend$inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:
- _objc_msgSend$setExposureModeCustomWithConfiguration:
- _objc_msgSend$transitionStateForMakeOutputsLiveIfNeeded
- _objc_msgSend$waitForStartOrCommitToComplete
- _vcc_getMaximumCapacity
- _vcc_getSystemReserveSpace
CStrings:
+ "! ( storage->busyFlags & ( kFigProVideoStorageBusyFlag_AdjustingCapacity | kFigProVideoStorageBusyFlag_Replenishing ) )"
+ "! storage->busyFlags"
+ "%@ i:%.2f t:%.2f c:%.2f"
+ "%@ outputRectInBufferCoordinates %@ is not contained in valid-relative validBufferRect %@"
+ "%d capture request(s) were not serviced within %.2f seconds during graph stop"
+ "( storage->busyFlags & kFigProVideoStorageBusyFlag_Capturing ) || storage->isSaveCaptureFromCrashRecovery"
+ "-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]"
+ "-[BWE5InferenceProvider _configureANEExecutionPriorityOnEspressoStream]"
+ "-[BWEspressoE5InferenceCamGazePropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:]"
+ "-[BWEspressoInferenceCamGazePropagator propagateInferenceResultsToInferenceDictionary:usingStorage:inputSampleBuffer:propagationSampleBuffer:]"
+ "-[BWEspressoInferenceProvider _configureANEExecutionPriorityOnEspressoPlan]"
+ "-[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:normalizedRectOfInterest:]"
+ "-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]"
+ "-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]_block_invoke"
+ "-[BWGraph waitForStartOrCommitToCompleteWithWillBeStoppedImmediately:]"
+ "-[BWMultiStreamCameraSourceNode makeOutputsLiveWithWillBeStoppedImmediately:]_block_invoke"
+ "-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:piecemealEncodingMode:]"
+ "-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:piecemealEncodingMode:]_block_invoke"
+ "-[BWPhotonicEngineNode _piecemealEncodeAttachedMediaByKey:primarySbuf:portType:piecemealEncodingMode:]"
+ "-[BWPhotonicEngineNodeResourceCoordinator _allocateMetalHeap:metalAllocatorDescriptor:settings:]"
+ "-[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:camGazeInferenceType:]"
+ "-[BWSoftISPProcessorController _addFrame:preparedMaxOutputDimensions:]"
+ "-[BWSoftISPProcessorController _outputBufferRectWithinSensorCropRectForFrame:preparedMaxOutputDimensions:]"
+ "-[FigCaptureCameraSourcePipeline _insertSmartFramingPerceptionSinkNodeOnOutputsBySourceDeviceType:pipelineConfiguration:inferenceScheduler:graph:outputNetworkType:]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureMemoryReporter.m"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Propagation/BWEspressoE5InferenceCamGazePropagator.m %s: No detected faces or faceIndex %lu out of bounds (count: %lu)"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Propagation/BWEspressoE5InferenceCamGazePropagator.m %s: [CamGaze E5] e5rt_buffer_object_get_iosurface failed with error code %d error message %s"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Propagation/BWEspressoE5InferenceCamGazePropagator.m %s: [CamGaze E5] e5rt_io_port_retain_buffer_object failed with error code %d error message %s"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Propagation/BWEspressoE5InferenceCamGazePropagator.m %s: [CamGaze E5] tensorPort is NULL for camGaze requirement"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Propagation/BWEspressoInferenceCamGazePropagator.m %s: No detected faces or faceIndex %lu out of bounds (count: %lu)"
+ "12:39:45"
+ "35d99764922290cd3282a716ac682c12522b2e4d"
+ "7e7f14e1c034455198842478f21e7fa57b4fcd87"
+ "<%@: %p> lowLightEIT=%f, sifrMainEIT=%f, sifrGain=%f, lowLightHDRWithoutSIFR=%f, longWithoutSphere=%f, deepFusion=%f, rsmMainEIT=%f, rsmSIFRGain=%f, toneCurveBehavior=%d, preserveBlackLevel=%d, afWindows=%p, refMethod=%d, usePreviousSIFR=%d, motionAndFocusScoreWeights=%@, maxNumberOfFramesForAdaptiveBracketing=%d, dFlashAvailableEIT=%f, dFlashRecommendedEIT=%f, dFlashStationaryRecommendedEIT=%f, dFlashAvailableSNR=%f, dFlashAvailableSNRLag=%f, dFlashRecommendedSNR=%f, dFlashRecommendedSNRLag=%f, dFlashStationaryRecommendedSNR=%f, dFlashStationaryRecommendedSNRLag=%f, dFlashRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashAERelativeDiff=%f%@"
+ "<%@: %p> type:%@, serviceBeforeGraphStop:%d, requestedSettings:%@%@"
+ "<<< FigCaptureCustomExposureConfiguration >>> %s: ISO underflow! (%g)  Capped to baseISO %g"
+ "<<< FigVirtualCaptureCard >>> %s: Available space: filesystem=%lld, VCC=%lld, purgeable=%lld, immediatelyAvailable=%lld, totalAvailable=%lld (includePurgeableSpace=%d)"
+ "<<< FigVirtualCaptureCard >>> %s: Changing capacity from %lld to %lld (spaceRequiredForAllocation=%lld, immediatelyAvailable=%lld, totalAvailable=%lld, shouldPurge=%d, replenishMode=%d)"
+ "<<< FigVirtualCaptureCard >>> %s: Failed to fetch system reserve size"
+ "<<< FigVirtualCaptureCard >>> %s: Posted BusyReasonsChanged notification (busyReasons=0x%x)"
+ "<<< FigVirtualCaptureCard >>> %s: Preallocating %lld bytes, remainingCapacity %lld, overhead %lld"
+ "<<< FigVirtualCaptureCard >>> %s: Replenish target (%lld) does not exceed current FreeSpace (%lld); refusing non-growing replenish"
+ "<<< FigVirtualCaptureCard >>> %s: Returning maximumCapacity=%lld, purgeableSpace=%lld (totalAvailable=%lld, reserve=%lld, afterReserve=%lld, overhead=%lld)"
+ "<<< FigVirtualCaptureCard >>> %s: SetCapacity breakdown: clientCapacity=%lld, roundedCapacity=%lld, overhead=%lld, systemReserve=%lld, spaceRequired=%lld, replenishMode=%d"
+ "<<< FigVirtualCaptureCard >>> %s: SetCapacity called with capacity=%lld replenishMode=%d"
+ "<<< FigVirtualCaptureCard >>> %s: [%p] property %@ = 0x%x"
+ "<<<< BWDeferredContainerIntermediate >>>> %s: Using crop rect '%@' for captureID:%lld"
+ "<<<< BWE5InferenceProvider >>>> %s: Failed to configure ANEHW execution priority on stream (err:%d)"
+ "<<<< BWE5InferenceProvider >>>> %s: Failed to set ANE priority to %d (err:%d)"
+ "<<<< BWEspressoInferenceProvider >>>> %s: Failed to configure plan with ANEHW execution priority (%d)"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: The deferred container manager is currently unable to support deferred processing. Changing capture type to %{public}@."
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Using aperture behavior '%d'"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: _largestStagedSupportingAudioVideoStagedPTS %lld : %d (%7.4lf) later than master buffer... reset _masterStartingPTS and _lowLatencyCanTransitionEarlyRecording"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: audio for input %d, setting _haveSeenAudioWhenStartingForIndex[%d] to T, _haveSeenAudioWhenStarting = %c"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: culling buffer for input %d because its ending PTS %lld : %d (%7.4lf) <= masterStartingPTS %lld : %d (%7.4lf)"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: low latency mode enabled = %c (allow %c, cinematic audio %c, video %d, audio %d, master index %d)"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: low latency mode noted audio buffer for input %d starting at PTS %lld : %d (%7.4lf), setting _lowLatencyCanTransitionEarlyToRecordingForIndex[%d] to T, _lowLatencyCanTransitionEarlyToRecording = %c"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: running: low-latency, no need to trim first audio sample buffer for input %d (%lld : %d, %7.4lf)"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: running: low-latency, tried to trim first audio sample buffer for input %d, but got nothing back so dropping it (%lld : %d, %7.4lf)"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: running: low-latency, trimmed first audio sample buffer for input %d (%lld : %d, %7.4lf -> %lld : %d, %7.4lf)"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: stopping: low-latency, all audio queues have buffers, setting _lowLatencyCanTossExtraVideoWhenStopping to YES"
+ "<<<< BWFileCoordinatorNode >>>> %s: %p: trimming first audio for input %d, setting _firstAudioHasBeenProcessedForIndex[%d] to T, _firstAudioHasBeenProcessed = %c"
+ "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> Called with willBeStoppedImmediately=%d"
+ "<<<< BWInferenceVideoScalingProvider >>>> %s: Attempted to crop smaller height %g than allowed by MSR upscale limit %g (%gx) - likely rdar://104943722 - non-fatal, clamping to minimum height %gx and continuing\n%@ attempted: (crop {{%zu,%zu}, {%zu,%zu}} into %zu x %zu -> %zu x %zu) (%c%c%c%c ->  %c%c%c%c)"
+ "<<<< BWInferenceVideoScalingProvider >>>> %s: Attempting to crop smaller width %g than allowed by MSR upscale limit %g (%gx) - likely rdar://104943722 - non-fatal, clamping to minimum width %gx and continuing\n%@ attempted: (crop {{%zu,%zu}, {%zu,%zu}} into %zu x %zu -> %zu x %zu) (%c%c%c%c ->  %c%c%c%c)"
+ "<<<< BWMultiFilterThumbnailNode >>>> %s: Failed to load and configure filter bundle (%d)"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: Forcing immediate transition for pending live configuration: portType=%{public}@ output=%{public}@: liveConfigID=%lld -> requestedConfigID=%lld"
+ "<<<< BWProResRawMetadataUtilities >>>> %s: Got stabilization transforms for sbuf with input dimensions %d x %d, output dimensions %d x %d, transform rows %d, transform columns %d and transform step %d"
+ "<<<< BWProResRawMetadataUtilities >>>> %s: stabilizationTransformsParametersData data: %@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Cannot start recording: PVS is busy (flags=0x%x)"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: FigVirtualCaptureCardCopyProperty(BusyReasons) returned err = (%d)"
+ "<<<< BWSmartFramingPerceptionSinkNode >>>> %s: %p: camGazeInferenceType must be %@, got %@"
+ "<<<< BWSmartFramingPerceptionSinkNode >>>> %s: Failed to add %@ inference to BWInferenceEngine"
+ "<<<< BWSmartFramingPerceptionSinkNode >>>> %s: init failed sinkID = %@ captureDevice = %p camGazeInferenceType = %d"
+ "<<<< BWSmartStyleLearningNode >>>> %s: _thumbnailsGenerationCommandQueue is nil"
+ "<<<< BWSmartStyleLearningNode >>>> %s: smartStyleThumbnailsGenerationCompletionQueue is nil"
+ "<<<< BWSmartStyleLearningNode >>>> %s: smartStyleThumbnailsGenerationSubmissionQueue is nil"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: %@ took %.2fms"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: %d capture request(s) were not serviced within %.2f seconds during graph stop"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: Photo #%d - processing flags: %@ identifier %{public}@/%{public}@"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: Waiting until DidCapturePhoto callback is sent before completing request for captureID:%lld"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: Waiting up to %.2f seconds for %d in-flight capture request(s) to be serviced before stopping"
+ "<<<< BWStillImageProcessing >>>> %s: %@ outputRectInBufferCoordinates %@ is not contained in valid-relative validBufferRect %@"
+ "<<<< BWStillImageProcessing >>>> %s: Piecemeal encoding is not supported for attachedMediaKey:%{public}@ captureID:%lld -- skipping piecemeal encoding"
+ "<<<< BWStillImageProcessing >>>> %s: Piecemeal encoding is not supported for mode '%@' and settings %@"
+ "<<<< BWStillImageProcessing >>>> %s: [%@] Insufficient SoftISP output buffer to preserve full region required by GDC (minimumValidBufferRectForGDC %@, output clamped to %@ (prepared:%@)"
+ "<<<< BWUtilities >>>> %s: Using tuning type '%@' for '%@' with capture flags '%@'"
+ "<<<< FigCaptureCameraSourcePipeline >>>> %s: smartFramingPerceptionSinkNode initialized with camGazeInferenceType: %@"
+ "<<<< FigCaptureMemoryReporter >>>> %s: Model Manager assertion held for %.0f seconds without an active capture client"
+ "<<<< FigCaptureSession >>>> %s: called with '%@' which should never happen!"
+ "<<<< FigVirtualCaptureCardRemote >>>> %s: Error setting SetCapacity options: %d"
+ "<<<< FigVirtualCaptureCardServer >>>> %s: Error extracting options dictionary for SetCapacity: %d"
+ "AVGQIV52D6ZY6YNMNKTM3AFFHYPXPM"
+ "BWPhotoEncoderSupportsPiecemealEncoding"
+ "BWUtilitiesSmartStyleTuningParameterVariantForCaptureType"
+ "BusyReasons"
+ "Digital Flash Available - Scene ( Normalized QSum SNR )"
+ "Digital Flash Recommended - Scene ( Normalized QSum SNR )"
+ "DigitalFlashAvailable"
+ "DigitalFlashRecommended"
+ "Error converting busy reasons to bitmask"
+ "ExposureAreaOfInterest"
+ "Failed to compute maximum capacity components"
+ "Failed to compute maximum capacity components excluding purgeable"
+ "Failed to fetch system reserve size"
+ "Failed to query FreeSpace for replenish growth guard"
+ "Failed to query PVS free space for preallocating capacity"
+ "Jul  2 2026"
+ "LastShownBuild:BWCameraInfoMetadataNode.m:531"
+ "LastShownBuild:BWCameraInfoMetadataNode.m:703"
+ "LastShownBuild:BWCompressedShotBufferNode.m:124"
+ "LastShownBuild:BWCompressedShotBufferNode.m:332"
+ "LastShownBuild:BWCoreAnalyticsReporter.m:387"
+ "LastShownBuild:BWDeferredCaptureController.m:468"
+ "LastShownBuild:BWE5InferenceProvider.m:862"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10323"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10833"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11284"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11319"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11508"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11517"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11529"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11536"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11570"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11636"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11805"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:12727"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:15744"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18576"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18964"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:1960"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:19771"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20193"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20195"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20197"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22094"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23484"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23516"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23672"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24430"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24676"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25033"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:5970"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7647"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7656"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8733"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8734"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8753"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9042"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9856"
+ "LastShownBuild:BWFileCoordinatorNode.m:1337"
+ "LastShownBuild:BWFrameStatistics.m:805"
+ "LastShownBuild:BWGraph.m:3582"
+ "LastShownBuild:BWGraph.m:3585"
+ "LastShownBuild:BWGraph.m:3598"
+ "LastShownBuild:BWGraph.m:3601"
+ "LastShownBuild:BWGraph.m:3604"
+ "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1177"
+ "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1740"
+ "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:744"
+ "LastShownBuild:BWLearnSmartStyleRenderer.m:335"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:13588"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:2717"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4399"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4406"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4413"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:9368"
+ "LastShownBuild:BWNRFProcessorController.m:1670"
+ "LastShownBuild:BWNRFProcessorController.m:1671"
+ "LastShownBuild:BWNRFProcessorController.m:2069"
+ "LastShownBuild:BWPhotoEncoderController.m:1308"
+ "LastShownBuild:BWPhotoEncoderController.m:1311"
+ "LastShownBuild:BWPhotoEncoderController.m:1697"
+ "LastShownBuild:BWPhotoEncoderController.m:1702"
+ "LastShownBuild:BWPhotoEncoderController.m:1955"
+ "LastShownBuild:BWPhotoEncoderController.m:2094"
+ "LastShownBuild:BWPhotoEncoderController.m:2110"
+ "LastShownBuild:BWPhotoEncoderController.m:2120"
+ "LastShownBuild:BWPhotoEncoderController.m:3278"
+ "LastShownBuild:BWPhotoEncoderController.m:4666"
+ "LastShownBuild:BWPhotoEncoderController.m:6395"
+ "LastShownBuild:BWPhotonicEngineNode.m:1401"
+ "LastShownBuild:BWPhotonicEngineNode.m:1461"
+ "LastShownBuild:BWPhotonicEngineNode.m:1564"
+ "LastShownBuild:BWPhotonicEngineNode.m:1567"
+ "LastShownBuild:BWPhotonicEngineNode.m:1591"
+ "LastShownBuild:BWPhotonicEngineNode.m:2034"
+ "LastShownBuild:BWPhotonicEngineNode.m:2085"
+ "LastShownBuild:BWPhotonicEngineNode.m:2390"
+ "LastShownBuild:BWPhotonicEngineNode.m:2400"
+ "LastShownBuild:BWPhotonicEngineNode.m:2944"
+ "LastShownBuild:BWPhotonicEngineNode.m:2981"
+ "LastShownBuild:BWPhotonicEngineNode.m:2984"
+ "LastShownBuild:BWPhotonicEngineNode.m:3711"
+ "LastShownBuild:BWPhotonicEngineNode.m:3726"
+ "LastShownBuild:BWPhotonicEngineNode.m:3828"
+ "LastShownBuild:BWPhotonicEngineNode.m:3853"
+ "LastShownBuild:BWPhotonicEngineNode.m:4916"
+ "LastShownBuild:BWPhotonicEngineNode.m:5643"
+ "LastShownBuild:BWPhotonicEngineNode.m:5668"
+ "LastShownBuild:BWPhotonicEngineNode.m:750"
+ "LastShownBuild:BWPhotonicEngineNode.m:764"
+ "LastShownBuild:BWPhotonicEngineNode.m:771"
+ "LastShownBuild:BWPhotonicEngineNode.m:7752"
+ "LastShownBuild:BWPhotonicEngineNode.m:7754"
+ "LastShownBuild:BWPhotonicEngineNode.m:9256"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2447"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:391"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3943"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:409"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4250"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4453"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4462"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4470"
+ "LastShownBuild:BWPixelBufferPool.m:651"
+ "LastShownBuild:BWSmartStyleTargetRenderer.m:626"
+ "LastShownBuild:BWSoftISPProcessorController.m:2844"
+ "LastShownBuild:BWSoftISPProcessorController.m:2907"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1209"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1213"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1419"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1426"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1496"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1599"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1610"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:2229"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:3713"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:626"
+ "LastShownBuild:BWStillImageFilterNode.m:1264"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1040"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:120"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1911"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1918"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1924"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1947"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2714"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2744"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:652"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:786"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:965"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:971"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:983"
+ "LastShownBuild:BWUBCaptureParameters.m:222"
+ "LastShownBuild:BWUBCaptureParameters.m:228"
+ "LastShownBuild:BWUBCaptureParameters.m:231"
+ "LastShownBuild:BWUBCaptureParameters.m:236"
+ "LastShownBuild:BWUBCaptureParameters.m:299"
+ "LastShownBuild:BWUBNode.m:1030"
+ "LastShownBuild:BWUBNode.m:1033"
+ "LastShownBuild:BWUBNode.m:1050"
+ "LastShownBuild:BWUBNode.m:1192"
+ "LastShownBuild:BWUBNode.m:1201"
+ "LastShownBuild:BWUBNode.m:1470"
+ "LastShownBuild:BWUBNode.m:1901"
+ "LastShownBuild:BWUBNode.m:2119"
+ "LastShownBuild:BWUBNode.m:2122"
+ "LastShownBuild:BWUBNode.m:2209"
+ "LastShownBuild:BWUBNode.m:2522"
+ "LastShownBuild:BWUBNode.m:3593"
+ "LastShownBuild:BWUBNode.m:5573"
+ "LastShownBuild:BWUBNode.m:5972"
+ "LastShownBuild:BWUBNode.m:6289"
+ "LastShownBuild:BWUBNode.m:908"
+ "LastShownBuild:BWUBNode.m:935"
+ "LastShownBuild:BWUtilities.m:1065"
+ "LastShownBuild:BWVideoFormat.m:1484"
+ "LastShownBuild:FigCaptureMemoryReporter.m:513"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1533"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:6235"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3018"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3138"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3139"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3303"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3482"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3486"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3531"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4509"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4515"
+ "LastShownBuild:FigCaptureSession.m:10189"
+ "LastShownBuild:FigCaptureSession.m:10919"
+ "LastShownBuild:FigCaptureSession.m:11114"
+ "LastShownBuild:FigCaptureSession.m:12026"
+ "LastShownBuild:FigCaptureSession.m:18514"
+ "LastShownBuild:FigCaptureSession.m:20016"
+ "LastShownBuild:FigCaptureSession.m:20019"
+ "LastShownBuild:FigCaptureSession.m:27262"
+ "LastShownBuild:FigCaptureSession.m:4414"
+ "LastShownBuild:FigCaptureSession.m:5059"
+ "LastShownBuild:FigCaptureSession.m:8996"
+ "LastShownBuild:FigCaptureSession.m:9002"
+ "LastShownBuild:FigCaptureSession.m:9005"
+ "LastShownBuild:FigCaptureSession.m:9008"
+ "LastShownBuild:FigCaptureSession.m:9011"
+ "LastShownBuild:FigCaptureSession.m:9022"
+ "LastShownBuild:FigCaptureSession.m:9025"
+ "LastShownBuild:FigCaptureSession.m:9033"
+ "LastShownBuild:FigCaptureSession.m:9051"
+ "LastShownBuild:FigCaptureSession.m:9096"
+ "LastShownBuild:FigCaptureSession.m:9100"
+ "LastShownBuild:FigCaptureSession.m:9124"
+ "LastShownBuild:FigCaptureSession.m:9139"
+ "LastShownBuild:FigCaptureSession.m:9143"
+ "LastShownBuild:FigCaptureSession.m:9146"
+ "LastShownBuild:FigCaptureSession.m:9269"
+ "LastShownBuild:FigCaptureSession.m:9275"
+ "LastShownBuild:FigCaptureSession.m:9301"
+ "LastShownBuild:FigCaptureSession.m:9313"
+ "LastShownBuild:FigCaptureSession.m:9711"
+ "LastShownBuild:FigCaptureSession.m:992"
+ "LastShownBuild:FigCaptureSession.m:9994"
+ "LastShownBuild:FigCaptureSessionStateManager.m:351"
+ "LastShownBuild:FigCaptureSessionStateManager.m:378"
+ "LastShownBuild:FigCaptureSessionStateManager.m:511"
+ "LastShownBuild:FigCaptureSourceBackingsProvider.m:2728"
+ "LastShownBuild:FigSampleBufferProcessor_Autofocus.m:928"
+ "LastShownDate:BWCameraInfoMetadataNode.m:531"
+ "LastShownDate:BWCameraInfoMetadataNode.m:703"
+ "LastShownDate:BWCompressedShotBufferNode.m:124"
+ "LastShownDate:BWCompressedShotBufferNode.m:332"
+ "LastShownDate:BWCoreAnalyticsReporter.m:387"
+ "LastShownDate:BWDeferredCaptureController.m:468"
+ "LastShownDate:BWE5InferenceProvider.m:862"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10323"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10833"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11284"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11319"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11508"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11517"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11529"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11536"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11570"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11636"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11805"
+ "LastShownDate:BWFigVideoCaptureDevice.m:12727"
+ "LastShownDate:BWFigVideoCaptureDevice.m:15744"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18576"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18964"
+ "LastShownDate:BWFigVideoCaptureDevice.m:1960"
+ "LastShownDate:BWFigVideoCaptureDevice.m:19771"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20193"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20195"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20197"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22094"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23484"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23516"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23672"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24430"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24676"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25033"
+ "LastShownDate:BWFigVideoCaptureDevice.m:5970"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7647"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7656"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8733"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8734"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8753"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9042"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9856"
+ "LastShownDate:BWFileCoordinatorNode.m:1337"
+ "LastShownDate:BWFrameStatistics.m:805"
+ "LastShownDate:BWGraph.m:3582"
+ "LastShownDate:BWGraph.m:3585"
+ "LastShownDate:BWGraph.m:3598"
+ "LastShownDate:BWGraph.m:3601"
+ "LastShownDate:BWGraph.m:3604"
+ "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1177"
+ "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1740"
+ "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:744"
+ "LastShownDate:BWLearnSmartStyleRenderer.m:335"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:13588"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:2717"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4399"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4406"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4413"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:9368"
+ "LastShownDate:BWNRFProcessorController.m:1670"
+ "LastShownDate:BWNRFProcessorController.m:1671"
+ "LastShownDate:BWNRFProcessorController.m:2069"
+ "LastShownDate:BWPhotoEncoderController.m:1308"
+ "LastShownDate:BWPhotoEncoderController.m:1311"
+ "LastShownDate:BWPhotoEncoderController.m:1697"
+ "LastShownDate:BWPhotoEncoderController.m:1702"
+ "LastShownDate:BWPhotoEncoderController.m:1955"
+ "LastShownDate:BWPhotoEncoderController.m:2094"
+ "LastShownDate:BWPhotoEncoderController.m:2110"
+ "LastShownDate:BWPhotoEncoderController.m:2120"
+ "LastShownDate:BWPhotoEncoderController.m:3278"
+ "LastShownDate:BWPhotoEncoderController.m:4666"
+ "LastShownDate:BWPhotoEncoderController.m:6395"
+ "LastShownDate:BWPhotonicEngineNode.m:1401"
+ "LastShownDate:BWPhotonicEngineNode.m:1461"
+ "LastShownDate:BWPhotonicEngineNode.m:1564"
+ "LastShownDate:BWPhotonicEngineNode.m:1567"
+ "LastShownDate:BWPhotonicEngineNode.m:1591"
+ "LastShownDate:BWPhotonicEngineNode.m:2034"
+ "LastShownDate:BWPhotonicEngineNode.m:2085"
+ "LastShownDate:BWPhotonicEngineNode.m:2390"
+ "LastShownDate:BWPhotonicEngineNode.m:2400"
+ "LastShownDate:BWPhotonicEngineNode.m:2944"
+ "LastShownDate:BWPhotonicEngineNode.m:2981"
+ "LastShownDate:BWPhotonicEngineNode.m:2984"
+ "LastShownDate:BWPhotonicEngineNode.m:3711"
+ "LastShownDate:BWPhotonicEngineNode.m:3726"
+ "LastShownDate:BWPhotonicEngineNode.m:3828"
+ "LastShownDate:BWPhotonicEngineNode.m:3853"
+ "LastShownDate:BWPhotonicEngineNode.m:4916"
+ "LastShownDate:BWPhotonicEngineNode.m:5643"
+ "LastShownDate:BWPhotonicEngineNode.m:5668"
+ "LastShownDate:BWPhotonicEngineNode.m:750"
+ "LastShownDate:BWPhotonicEngineNode.m:764"
+ "LastShownDate:BWPhotonicEngineNode.m:771"
+ "LastShownDate:BWPhotonicEngineNode.m:7752"
+ "LastShownDate:BWPhotonicEngineNode.m:7754"
+ "LastShownDate:BWPhotonicEngineNode.m:9256"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2447"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:391"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3943"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:409"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4250"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4453"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4462"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4470"
+ "LastShownDate:BWPixelBufferPool.m:651"
+ "LastShownDate:BWSmartStyleTargetRenderer.m:626"
+ "LastShownDate:BWSoftISPProcessorController.m:2844"
+ "LastShownDate:BWSoftISPProcessorController.m:2907"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1209"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1213"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1419"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1426"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1496"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1599"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1610"
+ "LastShownDate:BWStillImageCoordinatorNode.m:2229"
+ "LastShownDate:BWStillImageCoordinatorNode.m:3713"
+ "LastShownDate:BWStillImageCoordinatorNode.m:626"
+ "LastShownDate:BWStillImageFilterNode.m:1264"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1040"
+ "LastShownDate:BWStillImageMetadataUtilities.m:120"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1911"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1918"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1924"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1947"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2714"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2744"
+ "LastShownDate:BWStillImageMetadataUtilities.m:652"
+ "LastShownDate:BWStillImageMetadataUtilities.m:786"
+ "LastShownDate:BWStillImageMetadataUtilities.m:965"
+ "LastShownDate:BWStillImageMetadataUtilities.m:971"
+ "LastShownDate:BWStillImageMetadataUtilities.m:983"
+ "LastShownDate:BWUBCaptureParameters.m:222"
+ "LastShownDate:BWUBCaptureParameters.m:228"
+ "LastShownDate:BWUBCaptureParameters.m:231"
+ "LastShownDate:BWUBCaptureParameters.m:236"
+ "LastShownDate:BWUBCaptureParameters.m:299"
+ "LastShownDate:BWUBNode.m:1030"
+ "LastShownDate:BWUBNode.m:1033"
+ "LastShownDate:BWUBNode.m:1050"
+ "LastShownDate:BWUBNode.m:1192"
+ "LastShownDate:BWUBNode.m:1201"
+ "LastShownDate:BWUBNode.m:1470"
+ "LastShownDate:BWUBNode.m:1901"
+ "LastShownDate:BWUBNode.m:2119"
+ "LastShownDate:BWUBNode.m:2122"
+ "LastShownDate:BWUBNode.m:2209"
+ "LastShownDate:BWUBNode.m:2522"
+ "LastShownDate:BWUBNode.m:3593"
+ "LastShownDate:BWUBNode.m:5573"
+ "LastShownDate:BWUBNode.m:5972"
+ "LastShownDate:BWUBNode.m:6289"
+ "LastShownDate:BWUBNode.m:908"
+ "LastShownDate:BWUBNode.m:935"
+ "LastShownDate:BWUtilities.m:1065"
+ "LastShownDate:BWVideoFormat.m:1484"
+ "LastShownDate:FigCaptureMemoryReporter.m:513"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1533"
+ "LastShownDate:FigCaptureMetadataUtilities.m:6235"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3018"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3138"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3139"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3303"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3482"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3486"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3531"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4509"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4515"
+ "LastShownDate:FigCaptureSession.m:10189"
+ "LastShownDate:FigCaptureSession.m:10919"
+ "LastShownDate:FigCaptureSession.m:11114"
+ "LastShownDate:FigCaptureSession.m:12026"
+ "LastShownDate:FigCaptureSession.m:18514"
+ "LastShownDate:FigCaptureSession.m:20016"
+ "LastShownDate:FigCaptureSession.m:20019"
+ "LastShownDate:FigCaptureSession.m:27262"
+ "LastShownDate:FigCaptureSession.m:4414"
+ "LastShownDate:FigCaptureSession.m:5059"
+ "LastShownDate:FigCaptureSession.m:8996"
+ "LastShownDate:FigCaptureSession.m:9002"
+ "LastShownDate:FigCaptureSession.m:9005"
+ "LastShownDate:FigCaptureSession.m:9008"
+ "LastShownDate:FigCaptureSession.m:9011"
+ "LastShownDate:FigCaptureSession.m:9022"
+ "LastShownDate:FigCaptureSession.m:9025"
+ "LastShownDate:FigCaptureSession.m:9033"
+ "LastShownDate:FigCaptureSession.m:9051"
+ "LastShownDate:FigCaptureSession.m:9096"
+ "LastShownDate:FigCaptureSession.m:9100"
+ "LastShownDate:FigCaptureSession.m:9124"
+ "LastShownDate:FigCaptureSession.m:9139"
+ "LastShownDate:FigCaptureSession.m:9143"
+ "LastShownDate:FigCaptureSession.m:9146"
+ "LastShownDate:FigCaptureSession.m:9269"
+ "LastShownDate:FigCaptureSession.m:9275"
+ "LastShownDate:FigCaptureSession.m:9301"
+ "LastShownDate:FigCaptureSession.m:9313"
+ "LastShownDate:FigCaptureSession.m:9711"
+ "LastShownDate:FigCaptureSession.m:992"
+ "LastShownDate:FigCaptureSession.m:9994"
+ "LastShownDate:FigCaptureSessionStateManager.m:351"
+ "LastShownDate:FigCaptureSessionStateManager.m:378"
+ "LastShownDate:FigCaptureSessionStateManager.m:511"
+ "LastShownDate:FigCaptureSourceBackingsProvider.m:2728"
+ "LastShownDate:FigSampleBufferProcessor_Autofocus.m:928"
+ "MaximumCapacityComponents"
+ "MaximumCapacityComponentsExcludingPurgeable"
+ "Model Manager assertion held for %.0f seconds without an active capture client"
+ "Notification_BusyReasons"
+ "PVS is busy"
+ "PVS is busy with SetCapacity or Replenish."
+ "PVS is not marked busy during capture."
+ "PVS requires recovery."
+ "Payload_BusyFlags"
+ "PurgeableSpace"
+ "Service requests before graph stop"
+ "ServiceAssetBundleFailure"
+ "SetCapacityOption_Replenish"
+ "SetCapacityOptions"
+ "Stationary Digital Flash Recommended - Scene ( Normalized QSum SNR )"
+ "StationaryDigitalFlashRecommended"
+ "VCPANEExecutionPriority"
+ "VCPANEVariantHint"
+ "ab9532c2ecb0fe92d726d43b0e45e4385dc4b09d"
+ "busyFlags == kFigProVideoStorageBusyFlag_None"
+ "busyReasonsValue >= 0"
+ "camGazeInferenceType == BWInferenceTypeCamGaze"
+ "capacity > freeSpace"
+ "com.apple.coremedia.smartstyle-thumbnails-generation-completion-metal-queue"
+ "com.apple.coremedia.smartstyle-thumbnails-generation-submission-metal-queue"
+ "compressionCropRect"
+ "description=CameraCapture-758.0.0.122.2"
+ "freeSpace >= 0"
+ "isAdjustingCapacity"
+ "maximumCapacityComponents"
+ "outPurgeableSpace >= 0"
+ "reserveErr == 0 "
+ "ub.scene.digitalFlashAvailableSNR"
+ "ub.scene.digitalFlashRecommendedSNR"
+ "ub.scene.stationaryDigitalFlashRecommendedSNR"
+ "vcc_copyMaximumCapacityComponents"
+ "vcc_postBusyFlagsNotification"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb1\xf0\xf0Q"
- "! storage->isBusy"
- "! vccIsBusy"
- "-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]"
- "-[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:]"
- "-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]"
- "-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]_block_invoke"
- "-[BWGraph waitForStartOrCommitToComplete]"
- "-[BWLearnSmartStyleRenderer _tuningParameterVariantForCaptureType:captureFlags:]"
- "-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:]"
- "-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:]_block_invoke"
- "-[BWPhotonicEngineNode _piecemealEncodeAttachedMediaByKey:primarySbuf:portType:]"
- "-[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:]"
- "-[BWSmartStyleRenderingProcessorController _tuningParameterVariantForCaptureType:captureFlags:]"
- "-[BWSmartStyleTargetRenderer _tuningParameterVariantForCaptureType:captureFlags:]"
- "-[BWSoftISPProcessorController _addFrame:]"
- "-[BWSoftISPProcessorController _outputBufferRectWithinSensorCropRectForFrame:]"
- "22:36:09"
- "3a57f7b63d39d44b01f8076a01393de403326e42"
- "40fddd6d92eab3d590b4a36dec7d4a84942e1b93"
- "<%@: %p> lowLightEIT=%f, sifrMainEIT=%f, sifrGain=%f, lowLightHDRWithoutSIFR=%f, longWithoutSphere=%f, deepFusion=%f, rsmMainEIT=%f, rsmSIFRGain=%f, toneCurveBehavior=%d, preserveBlackLevel=%d, afWindows=%p, refMethod=%d, usePreviousSIFR=%d, motionAndFocusScoreWeights=%@, maxNumberOfFramesForAdaptiveBracketing=%d, dFlashAvailableEIT=%f, dFlashRecommendedEIT=%f, dFlashStationaryRecommendedEIT=%f, dFlashRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashAERelativeDiff=%f"
- "<%@: %p> type:%@, requestedSettings:%@%@"
- "<<< FigVirtualCaptureCard >>> %s: Available space: filesystem=%lld, VCC=%lld, purgeable=%lld, immediatelyAvailable=%lld, totalAvailable=%lld"
- "<<< FigVirtualCaptureCard >>> %s: Changing capacity from %lld to %lld (spaceRequiredForAllocation=%lld, immediatelyAvailable=%lld, totalAvailable=%lld, shouldPurge=%d)"
- "<<< FigVirtualCaptureCard >>> %s: Failed to fetch system reserve space, defaulting to %llu"
- "<<< FigVirtualCaptureCard >>> %s: Preallocating %lld bytes, currentCapacity %lld, overhead %lld"
- "<<< FigVirtualCaptureCard >>> %s: Returning maximum capacity=%lld (totalAvailable=%lld, reserve=%lld, afterReserve=%lld, overhead=%lld)"
- "<<< FigVirtualCaptureCard >>> %s: SetCapacity breakdown: clientCapacity=%lld, roundedCapacity=%lld, overhead=%lld, systemReserve=%lld, spaceRequired=%lld"
- "<<< FigVirtualCaptureCard >>> %s: SetCapacity called with capacity=%lld"
- "<<<< BWE5InferenceProvider >>>> %s: Failed to set ANE priority using E5RT to %d (err:%d)"
- "<<<< BWFigVideoCaptureDevice >>>> %s: Can currently not defer an ultra high resolution Learned Fusion capture"
- "<<<< BWFigVideoCaptureDevice >>>> %s: The deferred container manager is currently unable to support deferred Deep Fusion. Changing capture type to WYSIWYG."
- "<<<< BWFigVideoCaptureDevice >>>> %s: The deferred container manager is currently unable to support deferred Learned Fusion. Changing capture type to WYSIWYG."
- "<<<< BWFigVideoCaptureDevice >>>> %s: The deferred container manager is currently unable to support deferred processing. Changing capture type to UB."
- "<<<< BWFileCoordinatorNode >>>> %s: %p: low latency mode enabled = %c (%c, %d, %d, %d)"
- "<<<< BWFileCoordinatorNode >>>> %s: %p: low latency mode noted audio buffer starting at PTS %lld : %d (%7.4lf), allowing video to be released"
- "<<<< BWFileCoordinatorNode >>>> %s: %p: running: low-latency, no need to trim first audio sample buffer (%lld : %d, %7.4lf)"
- "<<<< BWFileCoordinatorNode >>>> %s: %p: running: low-latency, tried to trim first audio sample buffer, but got nothing back so dropping it (%lld : %d, %7.4lf)"
- "<<<< BWFileCoordinatorNode >>>> %s: %p: running: low-latency, trimmed first audio sample buffer (%lld : %d, %7.4lf -> %lld : %d, %7.4lf)"
- "<<<< BWFileCoordinatorNode >>>> %s: %p: trimming first audio, setting _firstAudioHasBeenProcessed to T"
- "<<<< BWInferenceVideoScalingProvider >>>> %s: Attempted to crop smaller height %g than allowed by MSR upscale limit %g (%gx) - likely rdar://104943722\n%@ attempted: (crop {{%zu,%zu}, {%zu,%zu}} into %zu x %zu -> %zu x %zu) (%c%c%c%c ->  %c%c%c%c)"
- "<<<< BWInferenceVideoScalingProvider >>>> %s: Attempting to crop smaller width %g than allowed by MSR upscale limit %g (%gx) - likely rdar://104943722\n%@ attempted: (crop {{%zu,%zu}, {%zu,%zu}} into %zu x %zu -> %zu x %zu) (%c%c%c%c ->  %c%c%c%c)"
- "<<<< BWLearnSmartStyleRenderer >>>> %s: [%@] Using tuning type '%@' for '%@' with capture flags '%@'"
- "<<<< BWProResRawMetadataUtilities >>>> %s: Got GPU transforms for sbuf with input dimensions %d x %d, output dimensions %d x %d, transform rows %d, transform columns %d and transform step %d"
- "<<<< BWProResRawMetadataUtilities >>>> %s: gpuTransformsParametersData data: %@"
- "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Cannot start recording: VCC is busy"
- "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: FigVirtualCaptureCardCopyProperty(IsBusy) returned err = (%d)"
- "<<<< BWSmartFramingPerceptionSinkNode >>>> %s: Failed to add BWInferenceTypeCamGaze inference to BWInferenceEngine"
- "<<<< BWSmartFramingPerceptionSinkNode >>>> %s: init failed sinkID = %@ captureDevice = %p"
- "<<<< BWSmartStyleLearningNode >>>> %s: newSmartStyle is nil"
- "<<<< BWSmartStyleTargetRenderer >>>> %s: [%@] Using tuning type '%@' for '%@' with capture flags '%@'"
- "<<<< BWStillImageCoordinatorNode >>>> %s: Photo #%d - processing flags: %d identifier %{public}@/%{public}@"
- "<<<< BWStillImageProcessing >>>> %s: [%@] Using tuning type '%@' for '%@' with capture flags '%@'"
- "<<<< BWStillImageProcessingNode >>>> %s: Emitting '%{private}@' : %{private}@"
- "<<<< FigCaptureSession >>>> %s: called with BWStillImageCaptureTypeNone which should never happen!"
- "AutoExposureAreaOfInterest"
- "BWPhotoEncoderSupportsPiecemealEnocding"
- "Jun 17 2026"
- "LastShownBuild:BWCameraInfoMetadataNode.m:533"
- "LastShownBuild:BWCameraInfoMetadataNode.m:707"
- "LastShownBuild:BWCompressedShotBufferNode.m:122"
- "LastShownBuild:BWCompressedShotBufferNode.m:330"
- "LastShownBuild:BWCoreAnalyticsReporter.m:384"
- "LastShownBuild:BWDeferredCaptureController.m:423"
- "LastShownBuild:BWE5InferenceProvider.m:861"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10178"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10688"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11139"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11174"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11363"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11372"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11384"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11391"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11422"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11488"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11657"
- "LastShownBuild:BWFigVideoCaptureDevice.m:12568"
- "LastShownBuild:BWFigVideoCaptureDevice.m:15539"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18357"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18745"
- "LastShownBuild:BWFigVideoCaptureDevice.m:1887"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19477"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19972"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19974"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19976"
- "LastShownBuild:BWFigVideoCaptureDevice.m:21857"
- "LastShownBuild:BWFigVideoCaptureDevice.m:23240"
- "LastShownBuild:BWFigVideoCaptureDevice.m:23272"
- "LastShownBuild:BWFigVideoCaptureDevice.m:23412"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24170"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24416"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24771"
- "LastShownBuild:BWFigVideoCaptureDevice.m:5881"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7502"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7511"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8588"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8589"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8608"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8897"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9711"
- "LastShownBuild:BWFileCoordinatorNode.m:1319"
- "LastShownBuild:BWFrameStatistics.m:779"
- "LastShownBuild:BWGraph.m:3577"
- "LastShownBuild:BWGraph.m:3580"
- "LastShownBuild:BWGraph.m:3593"
- "LastShownBuild:BWGraph.m:3596"
- "LastShownBuild:BWGraph.m:3599"
- "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1174"
- "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:1737"
- "LastShownBuild:BWIntelligentDistortionCorrectionProcessorController.m:741"
- "LastShownBuild:BWLearnSmartStyleRenderer.m:338"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:13591"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:2710"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4387"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4394"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4401"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:9367"
- "LastShownBuild:BWNRFProcessorController.m:1667"
- "LastShownBuild:BWNRFProcessorController.m:1668"
- "LastShownBuild:BWNRFProcessorController.m:2066"
- "LastShownBuild:BWPhotoEncoderController.m:1256"
- "LastShownBuild:BWPhotoEncoderController.m:1259"
- "LastShownBuild:BWPhotoEncoderController.m:1645"
- "LastShownBuild:BWPhotoEncoderController.m:1650"
- "LastShownBuild:BWPhotoEncoderController.m:1903"
- "LastShownBuild:BWPhotoEncoderController.m:2042"
- "LastShownBuild:BWPhotoEncoderController.m:2058"
- "LastShownBuild:BWPhotoEncoderController.m:2068"
- "LastShownBuild:BWPhotoEncoderController.m:3227"
- "LastShownBuild:BWPhotoEncoderController.m:4615"
- "LastShownBuild:BWPhotoEncoderController.m:6344"
- "LastShownBuild:BWPhotonicEngineNode.m:1385"
- "LastShownBuild:BWPhotonicEngineNode.m:1445"
- "LastShownBuild:BWPhotonicEngineNode.m:1548"
- "LastShownBuild:BWPhotonicEngineNode.m:1551"
- "LastShownBuild:BWPhotonicEngineNode.m:1575"
- "LastShownBuild:BWPhotonicEngineNode.m:2018"
- "LastShownBuild:BWPhotonicEngineNode.m:2069"
- "LastShownBuild:BWPhotonicEngineNode.m:2370"
- "LastShownBuild:BWPhotonicEngineNode.m:2380"
- "LastShownBuild:BWPhotonicEngineNode.m:2924"
- "LastShownBuild:BWPhotonicEngineNode.m:2961"
- "LastShownBuild:BWPhotonicEngineNode.m:2964"
- "LastShownBuild:BWPhotonicEngineNode.m:3691"
- "LastShownBuild:BWPhotonicEngineNode.m:3706"
- "LastShownBuild:BWPhotonicEngineNode.m:3808"
- "LastShownBuild:BWPhotonicEngineNode.m:3833"
- "LastShownBuild:BWPhotonicEngineNode.m:4896"
- "LastShownBuild:BWPhotonicEngineNode.m:5615"
- "LastShownBuild:BWPhotonicEngineNode.m:5640"
- "LastShownBuild:BWPhotonicEngineNode.m:741"
- "LastShownBuild:BWPhotonicEngineNode.m:755"
- "LastShownBuild:BWPhotonicEngineNode.m:762"
- "LastShownBuild:BWPhotonicEngineNode.m:7724"
- "LastShownBuild:BWPhotonicEngineNode.m:7726"
- "LastShownBuild:BWPhotonicEngineNode.m:9225"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2445"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3947"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:395"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:413"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4219"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4422"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4431"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4439"
- "LastShownBuild:BWPixelBufferPool.m:653"
- "LastShownBuild:BWSmartStyleTargetRenderer.m:629"
- "LastShownBuild:BWSoftISPProcessorController.m:2869"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1197"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1201"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1407"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1414"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1484"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1567"
- "LastShownBuild:BWStillImageCoordinatorNode.m:2171"
- "LastShownBuild:BWStillImageCoordinatorNode.m:3630"
- "LastShownBuild:BWStillImageCoordinatorNode.m:618"
- "LastShownBuild:BWStillImageFilterNode.m:1261"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1039"
- "LastShownBuild:BWStillImageMetadataUtilities.m:119"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1816"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1823"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1829"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1852"
- "LastShownBuild:BWStillImageMetadataUtilities.m:2601"
- "LastShownBuild:BWStillImageMetadataUtilities.m:2631"
- "LastShownBuild:BWStillImageMetadataUtilities.m:651"
- "LastShownBuild:BWStillImageMetadataUtilities.m:785"
- "LastShownBuild:BWStillImageMetadataUtilities.m:964"
- "LastShownBuild:BWStillImageMetadataUtilities.m:970"
- "LastShownBuild:BWStillImageMetadataUtilities.m:982"
- "LastShownBuild:BWUBCaptureParameters.m:182"
- "LastShownBuild:BWUBCaptureParameters.m:188"
- "LastShownBuild:BWUBCaptureParameters.m:191"
- "LastShownBuild:BWUBCaptureParameters.m:196"
- "LastShownBuild:BWUBCaptureParameters.m:250"
- "LastShownBuild:BWUBNode.m:1024"
- "LastShownBuild:BWUBNode.m:1027"
- "LastShownBuild:BWUBNode.m:1044"
- "LastShownBuild:BWUBNode.m:1186"
- "LastShownBuild:BWUBNode.m:1195"
- "LastShownBuild:BWUBNode.m:1464"
- "LastShownBuild:BWUBNode.m:1894"
- "LastShownBuild:BWUBNode.m:2112"
- "LastShownBuild:BWUBNode.m:2115"
- "LastShownBuild:BWUBNode.m:2202"
- "LastShownBuild:BWUBNode.m:2515"
- "LastShownBuild:BWUBNode.m:3583"
- "LastShownBuild:BWUBNode.m:5560"
- "LastShownBuild:BWUBNode.m:5959"
- "LastShownBuild:BWUBNode.m:6276"
- "LastShownBuild:BWUBNode.m:902"
- "LastShownBuild:BWUBNode.m:929"
- "LastShownBuild:BWUtilities.m:1071"
- "LastShownBuild:BWVideoFormat.m:1500"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1498"
- "LastShownBuild:FigCaptureMetadataUtilities.m:6185"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3015"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3135"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3136"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3297"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3479"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3483"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3528"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4506"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4512"
- "LastShownBuild:FigCaptureSession.m:10156"
- "LastShownBuild:FigCaptureSession.m:10881"
- "LastShownBuild:FigCaptureSession.m:11073"
- "LastShownBuild:FigCaptureSession.m:11975"
- "LastShownBuild:FigCaptureSession.m:18463"
- "LastShownBuild:FigCaptureSession.m:19965"
- "LastShownBuild:FigCaptureSession.m:19968"
- "LastShownBuild:FigCaptureSession.m:27219"
- "LastShownBuild:FigCaptureSession.m:4396"
- "LastShownBuild:FigCaptureSession.m:5041"
- "LastShownBuild:FigCaptureSession.m:8963"
- "LastShownBuild:FigCaptureSession.m:8969"
- "LastShownBuild:FigCaptureSession.m:8972"
- "LastShownBuild:FigCaptureSession.m:8975"
- "LastShownBuild:FigCaptureSession.m:8978"
- "LastShownBuild:FigCaptureSession.m:8989"
- "LastShownBuild:FigCaptureSession.m:8992"
- "LastShownBuild:FigCaptureSession.m:9000"
- "LastShownBuild:FigCaptureSession.m:9018"
- "LastShownBuild:FigCaptureSession.m:9063"
- "LastShownBuild:FigCaptureSession.m:9067"
- "LastShownBuild:FigCaptureSession.m:9091"
- "LastShownBuild:FigCaptureSession.m:9106"
- "LastShownBuild:FigCaptureSession.m:9110"
- "LastShownBuild:FigCaptureSession.m:9113"
- "LastShownBuild:FigCaptureSession.m:9236"
- "LastShownBuild:FigCaptureSession.m:9242"
- "LastShownBuild:FigCaptureSession.m:9268"
- "LastShownBuild:FigCaptureSession.m:9280"
- "LastShownBuild:FigCaptureSession.m:9678"
- "LastShownBuild:FigCaptureSession.m:990"
- "LastShownBuild:FigCaptureSession.m:9961"
- "LastShownBuild:FigCaptureSessionStateManager.m:352"
- "LastShownBuild:FigCaptureSessionStateManager.m:384"
- "LastShownBuild:FigCaptureSessionStateManager.m:517"
- "LastShownBuild:FigCaptureSourceBackingsProvider.m:2730"
- "LastShownBuild:FigSampleBufferProcessor_Autofocus.m:929"
- "LastShownDate:BWCameraInfoMetadataNode.m:533"
- "LastShownDate:BWCameraInfoMetadataNode.m:707"
- "LastShownDate:BWCompressedShotBufferNode.m:122"
- "LastShownDate:BWCompressedShotBufferNode.m:330"
- "LastShownDate:BWCoreAnalyticsReporter.m:384"
- "LastShownDate:BWDeferredCaptureController.m:423"
- "LastShownDate:BWE5InferenceProvider.m:861"
- "LastShownDate:BWFigVideoCaptureDevice.m:10178"
- "LastShownDate:BWFigVideoCaptureDevice.m:10688"
- "LastShownDate:BWFigVideoCaptureDevice.m:11139"
- "LastShownDate:BWFigVideoCaptureDevice.m:11174"
- "LastShownDate:BWFigVideoCaptureDevice.m:11363"
- "LastShownDate:BWFigVideoCaptureDevice.m:11372"
- "LastShownDate:BWFigVideoCaptureDevice.m:11384"
- "LastShownDate:BWFigVideoCaptureDevice.m:11391"
- "LastShownDate:BWFigVideoCaptureDevice.m:11422"
- "LastShownDate:BWFigVideoCaptureDevice.m:11488"
- "LastShownDate:BWFigVideoCaptureDevice.m:11657"
- "LastShownDate:BWFigVideoCaptureDevice.m:12568"
- "LastShownDate:BWFigVideoCaptureDevice.m:15539"
- "LastShownDate:BWFigVideoCaptureDevice.m:18357"
- "LastShownDate:BWFigVideoCaptureDevice.m:18745"
- "LastShownDate:BWFigVideoCaptureDevice.m:1887"
- "LastShownDate:BWFigVideoCaptureDevice.m:19477"
- "LastShownDate:BWFigVideoCaptureDevice.m:19972"
- "LastShownDate:BWFigVideoCaptureDevice.m:19974"
- "LastShownDate:BWFigVideoCaptureDevice.m:19976"
- "LastShownDate:BWFigVideoCaptureDevice.m:21857"
- "LastShownDate:BWFigVideoCaptureDevice.m:23240"
- "LastShownDate:BWFigVideoCaptureDevice.m:23272"
- "LastShownDate:BWFigVideoCaptureDevice.m:23412"
- "LastShownDate:BWFigVideoCaptureDevice.m:24170"
- "LastShownDate:BWFigVideoCaptureDevice.m:24416"
- "LastShownDate:BWFigVideoCaptureDevice.m:24771"
- "LastShownDate:BWFigVideoCaptureDevice.m:5881"
- "LastShownDate:BWFigVideoCaptureDevice.m:7502"
- "LastShownDate:BWFigVideoCaptureDevice.m:7511"
- "LastShownDate:BWFigVideoCaptureDevice.m:8588"
- "LastShownDate:BWFigVideoCaptureDevice.m:8589"
- "LastShownDate:BWFigVideoCaptureDevice.m:8608"
- "LastShownDate:BWFigVideoCaptureDevice.m:8897"
- "LastShownDate:BWFigVideoCaptureDevice.m:9711"
- "LastShownDate:BWFileCoordinatorNode.m:1319"
- "LastShownDate:BWFrameStatistics.m:779"
- "LastShownDate:BWGraph.m:3577"
- "LastShownDate:BWGraph.m:3580"
- "LastShownDate:BWGraph.m:3593"
- "LastShownDate:BWGraph.m:3596"
- "LastShownDate:BWGraph.m:3599"
- "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1174"
- "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:1737"
- "LastShownDate:BWIntelligentDistortionCorrectionProcessorController.m:741"
- "LastShownDate:BWLearnSmartStyleRenderer.m:338"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:13591"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:2710"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4387"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4394"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4401"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:9367"
- "LastShownDate:BWNRFProcessorController.m:1667"
- "LastShownDate:BWNRFProcessorController.m:1668"
- "LastShownDate:BWNRFProcessorController.m:2066"
- "LastShownDate:BWPhotoEncoderController.m:1256"
- "LastShownDate:BWPhotoEncoderController.m:1259"
- "LastShownDate:BWPhotoEncoderController.m:1645"
- "LastShownDate:BWPhotoEncoderController.m:1650"
- "LastShownDate:BWPhotoEncoderController.m:1903"
- "LastShownDate:BWPhotoEncoderController.m:2042"
- "LastShownDate:BWPhotoEncoderController.m:2058"
- "LastShownDate:BWPhotoEncoderController.m:2068"
- "LastShownDate:BWPhotoEncoderController.m:3227"
- "LastShownDate:BWPhotoEncoderController.m:4615"
- "LastShownDate:BWPhotoEncoderController.m:6344"
- "LastShownDate:BWPhotonicEngineNode.m:1385"
- "LastShownDate:BWPhotonicEngineNode.m:1445"
- "LastShownDate:BWPhotonicEngineNode.m:1548"
- "LastShownDate:BWPhotonicEngineNode.m:1551"
- "LastShownDate:BWPhotonicEngineNode.m:1575"
- "LastShownDate:BWPhotonicEngineNode.m:2018"
- "LastShownDate:BWPhotonicEngineNode.m:2069"
- "LastShownDate:BWPhotonicEngineNode.m:2370"
- "LastShownDate:BWPhotonicEngineNode.m:2380"
- "LastShownDate:BWPhotonicEngineNode.m:2924"
- "LastShownDate:BWPhotonicEngineNode.m:2961"
- "LastShownDate:BWPhotonicEngineNode.m:2964"
- "LastShownDate:BWPhotonicEngineNode.m:3691"
- "LastShownDate:BWPhotonicEngineNode.m:3706"
- "LastShownDate:BWPhotonicEngineNode.m:3808"
- "LastShownDate:BWPhotonicEngineNode.m:3833"
- "LastShownDate:BWPhotonicEngineNode.m:4896"
- "LastShownDate:BWPhotonicEngineNode.m:5615"
- "LastShownDate:BWPhotonicEngineNode.m:5640"
- "LastShownDate:BWPhotonicEngineNode.m:741"
- "LastShownDate:BWPhotonicEngineNode.m:755"
- "LastShownDate:BWPhotonicEngineNode.m:762"
- "LastShownDate:BWPhotonicEngineNode.m:7724"
- "LastShownDate:BWPhotonicEngineNode.m:7726"
- "LastShownDate:BWPhotonicEngineNode.m:9225"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2445"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3947"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:395"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:413"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4219"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4422"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4431"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4439"
- "LastShownDate:BWPixelBufferPool.m:653"
- "LastShownDate:BWSmartStyleTargetRenderer.m:629"
- "LastShownDate:BWSoftISPProcessorController.m:2869"
- "LastShownDate:BWStillImageCoordinatorNode.m:1197"
- "LastShownDate:BWStillImageCoordinatorNode.m:1201"
- "LastShownDate:BWStillImageCoordinatorNode.m:1407"
- "LastShownDate:BWStillImageCoordinatorNode.m:1414"
- "LastShownDate:BWStillImageCoordinatorNode.m:1484"
- "LastShownDate:BWStillImageCoordinatorNode.m:1567"
- "LastShownDate:BWStillImageCoordinatorNode.m:2171"
- "LastShownDate:BWStillImageCoordinatorNode.m:3630"
- "LastShownDate:BWStillImageCoordinatorNode.m:618"
- "LastShownDate:BWStillImageFilterNode.m:1261"
- "LastShownDate:BWStillImageMetadataUtilities.m:1039"
- "LastShownDate:BWStillImageMetadataUtilities.m:119"
- "LastShownDate:BWStillImageMetadataUtilities.m:1816"
- "LastShownDate:BWStillImageMetadataUtilities.m:1823"
- "LastShownDate:BWStillImageMetadataUtilities.m:1829"
- "LastShownDate:BWStillImageMetadataUtilities.m:1852"
- "LastShownDate:BWStillImageMetadataUtilities.m:2601"
- "LastShownDate:BWStillImageMetadataUtilities.m:2631"
- "LastShownDate:BWStillImageMetadataUtilities.m:651"
- "LastShownDate:BWStillImageMetadataUtilities.m:785"
- "LastShownDate:BWStillImageMetadataUtilities.m:964"
- "LastShownDate:BWStillImageMetadataUtilities.m:970"
- "LastShownDate:BWStillImageMetadataUtilities.m:982"
- "LastShownDate:BWUBCaptureParameters.m:182"
- "LastShownDate:BWUBCaptureParameters.m:188"
- "LastShownDate:BWUBCaptureParameters.m:191"
- "LastShownDate:BWUBCaptureParameters.m:196"
- "LastShownDate:BWUBCaptureParameters.m:250"
- "LastShownDate:BWUBNode.m:1024"
- "LastShownDate:BWUBNode.m:1027"
- "LastShownDate:BWUBNode.m:1044"
- "LastShownDate:BWUBNode.m:1186"
- "LastShownDate:BWUBNode.m:1195"
- "LastShownDate:BWUBNode.m:1464"
- "LastShownDate:BWUBNode.m:1894"
- "LastShownDate:BWUBNode.m:2112"
- "LastShownDate:BWUBNode.m:2115"
- "LastShownDate:BWUBNode.m:2202"
- "LastShownDate:BWUBNode.m:2515"
- "LastShownDate:BWUBNode.m:3583"
- "LastShownDate:BWUBNode.m:5560"
- "LastShownDate:BWUBNode.m:5959"
- "LastShownDate:BWUBNode.m:6276"
- "LastShownDate:BWUBNode.m:902"
- "LastShownDate:BWUBNode.m:929"
- "LastShownDate:BWUtilities.m:1071"
- "LastShownDate:BWVideoFormat.m:1500"
- "LastShownDate:FigCaptureMetadataUtilities.m:1498"
- "LastShownDate:FigCaptureMetadataUtilities.m:6185"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3015"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3135"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3136"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3297"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3479"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3483"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3528"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4506"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4512"
- "LastShownDate:FigCaptureSession.m:10156"
- "LastShownDate:FigCaptureSession.m:10881"
- "LastShownDate:FigCaptureSession.m:11073"
- "LastShownDate:FigCaptureSession.m:11975"
- "LastShownDate:FigCaptureSession.m:18463"
- "LastShownDate:FigCaptureSession.m:19965"
- "LastShownDate:FigCaptureSession.m:19968"
- "LastShownDate:FigCaptureSession.m:27219"
- "LastShownDate:FigCaptureSession.m:4396"
- "LastShownDate:FigCaptureSession.m:5041"
- "LastShownDate:FigCaptureSession.m:8963"
- "LastShownDate:FigCaptureSession.m:8969"
- "LastShownDate:FigCaptureSession.m:8972"
- "LastShownDate:FigCaptureSession.m:8975"
- "LastShownDate:FigCaptureSession.m:8978"
- "LastShownDate:FigCaptureSession.m:8989"
- "LastShownDate:FigCaptureSession.m:8992"
- "LastShownDate:FigCaptureSession.m:9000"
- "LastShownDate:FigCaptureSession.m:9018"
- "LastShownDate:FigCaptureSession.m:9063"
- "LastShownDate:FigCaptureSession.m:9067"
- "LastShownDate:FigCaptureSession.m:9091"
- "LastShownDate:FigCaptureSession.m:9106"
- "LastShownDate:FigCaptureSession.m:9110"
- "LastShownDate:FigCaptureSession.m:9113"
- "LastShownDate:FigCaptureSession.m:9236"
- "LastShownDate:FigCaptureSession.m:9242"
- "LastShownDate:FigCaptureSession.m:9268"
- "LastShownDate:FigCaptureSession.m:9280"
- "LastShownDate:FigCaptureSession.m:9678"
- "LastShownDate:FigCaptureSession.m:990"
- "LastShownDate:FigCaptureSession.m:9961"
- "LastShownDate:FigCaptureSessionStateManager.m:352"
- "LastShownDate:FigCaptureSessionStateManager.m:384"
- "LastShownDate:FigCaptureSessionStateManager.m:517"
- "LastShownDate:FigCaptureSourceBackingsProvider.m:2730"
- "LastShownDate:FigSampleBufferProcessor_Autofocus.m:929"
- "MinimumValidFocusDistance"
- "SpotMeteredExposureAreaOfInterest"
- "VCC is busy"
- "VCC requires recovery."
- "cb85e4188c22fad08accc69478bf1b456af8b5ea"
- "description=CameraCapture-753.0.0.122.3"
- "isBusy"
- "newSmartStyle"
- "purgeableSpace >= 0"
- "vcc_getMaximumCapacity"
- "vcc_getSystemReserveSpace"
- "|___ fsbp_Autofocus ___| %s: Update spot metered exposure area = {%.3f/%.3f %.3fx%.3f}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa1\xf0\xf0!"

```
