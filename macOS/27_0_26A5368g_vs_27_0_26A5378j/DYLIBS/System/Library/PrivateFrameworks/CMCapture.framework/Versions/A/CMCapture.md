## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture`

```diff

-  __TEXT.__text: 0x556ffc
-  __TEXT.__objc_methlist: 0x288dc
-  __TEXT.__const: 0x143010
-  __TEXT.__cstring: 0x9839e
-  __TEXT.__oslogstring: 0xc80c4
-  __TEXT.__gcc_except_tab: 0x1fec
+  __TEXT.__text: 0x559314
+  __TEXT.__objc_methlist: 0x28994
+  __TEXT.__const: 0x143020
+  __TEXT.__cstring: 0x98852
+  __TEXT.__oslogstring: 0xc8807
+  __TEXT.__gcc_except_tab: 0x20b0
   __TEXT.__dlopen_cstrs: 0x290
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0xa4d0
+  __TEXT.__unwind_info: 0xa4e8
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5f30
+  __DATA_CONST.__const: 0x5f68
   __DATA_CONST.__objc_classlist: 0x1338
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x330
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x11c88
+  __DATA_CONST.__objc_selrefs: 0x11cf0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x11e0
-  __DATA_CONST.__objc_arraydata: 0x1610
-  __DATA_CONST.__got: 0x6068
-  __AUTH_CONST.__const: 0x5648
-  __AUTH_CONST.__cfstring: 0x41d20
-  __AUTH_CONST.__objc_const: 0x72300
+  __DATA_CONST.__objc_arraydata: 0x1620
+  __DATA_CONST.__got: 0x61e8
+  __AUTH_CONST.__const: 0x5678
+  __AUTH_CONST.__cfstring: 0x41ee0
+  __AUTH_CONST.__objc_const: 0x72560
   __AUTH_CONST.__objc_intobj: 0x3c48
-  __AUTH_CONST.__objc_arrayobj: 0x11d0
+  __AUTH_CONST.__objc_arrayobj: 0x11e8
   __AUTH_CONST.__objc_floatobj: 0x170
   __AUTH_CONST.__objc_doubleobj: 0x200
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__auth_got: 0x2178
-  __AUTH.__objc_data: 0x28a0
-  __DATA.__objc_ivar: 0x88d0
-  __DATA.__data: 0x2854
-  __DATA.__common: 0x19c0
-  __DATA.__bss: 0x1290
-  __DATA_DIRTY.__objc_data: 0x9790
-  __DATA_DIRTY.__data: 0x10a0
-  __DATA_DIRTY.__common: 0x1d0
-  __DATA_DIRTY.__bss: 0x9e0
+  __AUTH.__objc_data: 0x2620
+  __AUTH.__data: 0x110
+  __DATA.__objc_ivar: 0x8918
+  __DATA.__data: 0x282c
+  __DATA.__common: 0x1990
+  __DATA.__bss: 0x1258
+  __DATA_DIRTY.__objc_data: 0x9a10
+  __DATA_DIRTY.__data: 0xfb8
+  __DATA_DIRTY.__common: 0x200
+  __DATA_DIRTY.__bss: 0xa18
   - /System/Library/Frameworks/AVFAudio.framework/Versions/A/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 26390
-  Symbols:   58767
-  CStrings:  32051
+  Functions: 26387
+  Symbols:   58810
+  CStrings:  32098
 
Sections:
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__auth_got : content changed
Symbols:
+ +[FigCaptureCustomExposureConfiguration exposureConfigurationWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:requestID:]
+ -[BWDeferredBufferIntermediate compressionCropRect]
+ -[BWDeferredBufferIntermediate initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:compressionProfile:compressionCropRect:URL:]
+ -[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:portType:]
+ -[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]
+ -[BWFaceTrackingNode hasNonLiveConfigurationChanges]
+ -[BWFigVideoCaptureDevice _ubIsMacroFlashQSubSwitchingCaptureType:portType:sceneFlags:]
+ -[BWFigVideoCaptureDevice _updateExposureStateForAutofocusProperty:propertyValue:]
+ -[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:normalizedRectOfInterest:]
+ -[BWFigVideoCaptureStream lastZoomFactorQuadraSubPixelSwitchingSupported]
+ -[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]
+ -[BWGraph waitForStartOrCommitToCompleteWithWillBeStoppedImmediately:]
+ -[BWMultiStreamCameraSourceNode makeOutputsLiveWithWillBeStoppedImmediately:]
+ -[BWNondisruptiveSwitchingFormatSelector lastZoomFactorFormatIndexIgnoringZoomFactorAndQuadraSubPixelSceneMonitoring]
+ -[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:piecemealEncodingMode:]
+ -[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:camGazeInferenceType:]
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
+ -[FigCaptureCustomExposureConfiguration _initWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:requestID:]
+ -[FigCaptureSourceAttributes ispMBNRSupported]
+ FigCaptureMetadataGetManufacturerAndMarketingName.sPhysicalHardwareNameString
+ GCC_except_table104
+ GCC_except_table110
+ GCC_except_table144
+ GCC_except_table181
+ GCC_except_table244
+ GCC_except_table295
+ GCC_except_table337
+ GCC_except_table342
+ GCC_except_table347
+ GCC_except_table353
+ GCC_except_table393
+ GCC_except_table419
+ GCC_except_table436
+ GCC_except_table454
+ GCC_except_table505
+ GCC_except_table537
+ GCC_except_table554
+ GCC_except_table556
+ GCC_except_table561
+ GCC_except_table566
+ GCC_except_table568
+ GCC_except_table570
+ GCC_except_table65
+ GCC_except_table700
+ GCC_except_table76
+ GCC_except_table93
+ GCC_except_table97
+ OBJC_IVAR_$_BWDeferredBufferIntermediate._compressionCropRect
+ OBJC_IVAR_$_BWFaceDetectionNode._liveRotationDegrees
+ OBJC_IVAR_$_BWFaceDetectionNode._preparedRotationDegrees
+ OBJC_IVAR_$_BWFaceTrackingNode._liveRotationDegrees
+ OBJC_IVAR_$_BWFaceTrackingNode._preparedRotationDegrees
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._autofocusCachedPropertiesCounter
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._autofocusCachedPropertiesOrder
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._digitalFlashAvailableSceneByPortType
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._digitalFlashRecommendedSceneByPortType
+ OBJC_IVAR_$_BWFigVideoCaptureDevice._stationaryDigitalFlashRecommendedSceneByPortType
+ OBJC_IVAR_$_BWFileCoordinatorNode._firstAudioHasBeenProcessedForIndex
+ OBJC_IVAR_$_BWFileCoordinatorNode._haveSeenAudioWhenStartingForIndex
+ OBJC_IVAR_$_BWFileCoordinatorNode._lowLatencyCanTransitionEarlyToRecordingForIndex
+ OBJC_IVAR_$_BWSmartFramingPerceptionSinkNode._camGazeInferenceType
+ OBJC_IVAR_$_BWSmartStyleLearningNode._thumbnailsGenerationCommandQueue
+ OBJC_IVAR_$_BWStillImageCoordinatorRequest._shouldServiceBeforeGraphStop
+ OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashAvailableNormalizedSNRHysteresisLag
+ OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashAvailableNormalizedSNRThreshold
+ OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashRecommendedNormalizedSNRHysteresisLag
+ OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashRecommendedNormalizedSNRThreshold
+ OBJC_IVAR_$_BWUBCaptureParameters._stationaryDigitalFlashRecommendedNormalizedSNRHysteresisLag
+ OBJC_IVAR_$_BWUBCaptureParameters._stationaryDigitalFlashRecommendedNormalizedSNRThreshold
+ OBJC_IVAR_$_FigCaptureCameraSourcePipeline._usingVideoCaptureOutputNetworkCrossoverNodeForPreview
+ OBJC_IVAR_$_FigCaptureSourceAttributes._ispMBNRSupported
+ _BWPhotoEncoderPiecemealEncodingModeToShortString
+ _BWPhotoEncoderSupportsPiecemealEncoding
+ _BWUtilitiesSmartStyleTuningParameterVariantForCaptureType
+ _FigCaptureCurrentProcessIsBWCrucible
+ _FigImageControl_SetExposureAreaOfInterest
+ ___129-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:piecemealEncodingMode:]_block_invoke
+ ___278-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]_block_invoke
+ ___326-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]_block_invoke
+ ___63-[BWFigVideoCaptureDevice _setupAutofocusSampleBufferProcessor]_block_invoke
+ ___77-[BWMultiStreamCameraSourceNode makeOutputsLiveWithWillBeStoppedImmediately:]_block_invoke
+ ___91-[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:normalizedRectOfInterest:]_block_invoke
+ ___block_descriptor_40_e8_32o_e11_q24?0816l
+ ___block_descriptor_73_e8_32o40r48r56r64r_e5_v8?0l
+ ___copy_helper_block_e8_32o40r48r56r64r
+ ___destroy_helper_block_e8_32o40r48r56r64r
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
+ _mscsn_shouldReflectStillSampleBufferOnStreamingOutputs
+ _objc_msgSend$_initWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:requestID:
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
+ _objc_msgSend$setExposureModeCustomWithConfiguration:normalizedRectOfInterest:
+ _objc_msgSend$setShouldServiceBeforeGraphStop:
+ _objc_msgSend$shouldServiceBeforeGraphStop
+ _objc_msgSend$stationaryDigitalFlashRecommendedNormalizedSNRHysteresisLag
+ _objc_msgSend$stationaryDigitalFlashRecommendedNormalizedSNRThreshold
+ _objc_msgSend$transitionStateForMakeOutputsLiveWithWillBeStoppedImmediately:
+ _objc_msgSend$waitForStartOrCommitToCompleteWithWillBeStoppedImmediately:
+ initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:.onceToken
- +[FigCaptureCustomExposureConfiguration exposureConfigurationWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:normalizedRectOfInterest:requestID:]
- -[BWDeferredBufferIntermediate initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:compressionProfile:URL:]
- -[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:portType:]
- -[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]
- -[BWFigVideoCaptureDevice _updateExposureStateForAutofocusProperty:]
- -[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:]
- -[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]
- -[BWLearnSmartStyleRenderer _tuningParameterVariantForCaptureType:captureFlags:]
- -[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:]
- -[BWPortraitAutoSuggest _adjustMetadataOfSampleBuffer:]
- -[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:]
- -[BWSmartStyleTargetRenderer _tuningParameterVariantForCaptureType:captureFlags:]
- -[BWSourceNode transitionStateForMakeOutputsLiveIfNeeded]
- -[FigCaptureCustomExposureConfiguration _initWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:normalizedRectOfInterest:requestID:]
- -[FigCaptureCustomExposureConfiguration normalizedRectOfInterest]
- -[FigCaptureCustomExposureConfiguration sensorSpaceRectOfInterest]
- -[FigCaptureCustomExposureConfiguration setSensorSpaceRectOfInterest:]
- -[FigCaptureSourceExtendedAttributes ispMBNRSupported]
- GCC_except_table103
- GCC_except_table143
- GCC_except_table180
- GCC_except_table243
- GCC_except_table294
- GCC_except_table335
- GCC_except_table340
- GCC_except_table391
- GCC_except_table415
- GCC_except_table434
- GCC_except_table453
- GCC_except_table504
- GCC_except_table535
- GCC_except_table553
- GCC_except_table555
- GCC_except_table560
- GCC_except_table565
- GCC_except_table567
- GCC_except_table569
- GCC_except_table698
- GCC_except_table75
- GCC_except_table80
- GCC_except_table91
- GCC_except_table96
- OBJC_IVAR_$_BWFaceDetectionNode._rotationDegrees
- OBJC_IVAR_$_BWFigVideoCaptureDevice._isCachedExposureRectForSpotMetering
- OBJC_IVAR_$_BWStereoVideoCaptureSceneMonitor._wideMinimumValidFocusDistance
- OBJC_IVAR_$_FigCaptureCustomExposureConfiguration._normalizedRectOfInterest
- OBJC_IVAR_$_FigCaptureCustomExposureConfiguration._sensorSpaceRectOfInterest
- OBJC_IVAR_$_FigCaptureSourceExtendedAttributes._ispMBNRSupported
- _BWPhotoEncoderSupportsPiecemealEnocding
- _FigImageControl_SetAutoExposureAreaOfInterest
- _FigImageControl_SetSpotMeteringAreaOfInterest
- _OUTLINED_FUNCTION_721
- _OUTLINED_FUNCTION_722
- _OUTLINED_FUNCTION_723
- _OUTLINED_FUNCTION_724
- ___124-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:]_block_invoke
- ___256-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]_block_invoke
- ___306-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]_block_invoke
- ___56-[BWMultiStreamCameraSourceNode makeOutputsLiveIfNeeded]_block_invoke
- ___66-[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:]_block_invoke
- ___block_descriptor_65_e8_32o40r48r56r_e5_v8?0l
- ___copy_helper_block_e8_32o40r48r56r
- ___destroy_helper_block_e8_32o40r48r56r
- _kFigImageControlSampleBufferProcessorProperty_AutoExposureAreaOfInterest
- _kFigImageControlSampleBufferProcessorProperty_SpotMeteredExposureAreaOfInterest
- _kFigVideoStabilizationSampleBufferAttachmentKey_GPUTransformsParameters
- _kFigVirtualCaptureCardProperty_MaximumCapacity
- _objc_msgSend$_initWithExposureDuration:minFrameRate:maxFrameRate:ISO:useSpotMetering:normalizedRectOfInterest:requestID:
- _objc_msgSend$commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:portType:
- _objc_msgSend$commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:
- _objc_msgSend$initWithBuffer:tag:bufferType:captureFrameFlags:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:compressionProfile:URL:
- _objc_msgSend$initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:
- _objc_msgSend$initWithSinkID:captureDevice:inferenceScheduler:
- _objc_msgSend$inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:
- _objc_msgSend$panoModeEnabled
- _objc_msgSend$setExposureModeCustomWithConfiguration:
- _objc_msgSend$transitionStateForMakeOutputsLiveIfNeeded
- _objc_msgSend$waitForStartOrCommitToComplete
- _sGenerateTailspinForDroppedFrameEnabled
- initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:.onceToken
CStrings:
+ "%@ i:%.2f t:%.2f c:%.2f"
+ "%d capture request(s) were not serviced within %.2f seconds during graph stop"
+ "-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]"
+ "-[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:normalizedRectOfInterest:]"
+ "-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]"
+ "-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:cinematicAudioEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]_block_invoke"
+ "-[BWGraph waitForStartOrCommitToCompleteWithWillBeStoppedImmediately:]"
+ "-[BWMultiStreamCameraSourceNode makeOutputsLiveWithWillBeStoppedImmediately:]_block_invoke"
+ "-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:piecemealEncodingMode:]"
+ "-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:piecemealEncodingMode:]_block_invoke"
+ "-[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:camGazeInferenceType:]"
+ "-[FigCaptureCameraSourcePipeline _insertSmartFramingPerceptionSinkNodeOnOutputsBySourceDeviceType:pipelineConfiguration:inferenceScheduler:graph:outputNetworkType:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CMCaptureLocal/CMCaptureLocalSessionController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CameraViewfinder/FigCaptureSessionObserver.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureMetadataUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSession.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionPipelines.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionStateManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSource.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSourceBackingsProvider.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/CMCaptureUserNotification.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureCommon.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unknown flip %i"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unsupported rotation of %d degrees"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: rotationDegrees (%d) is invalid, must be 0/90/180/270. Returning kFigExifOrientation_0RowTop0ColLeft (%d)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigCapturePixelFormatUtilities.m %s: Unexpected plist value for a pixel format type: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Cannot look up key.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Not adding key.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Returning 0."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Key (%s) has already been registered. Not adding key.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: keyspace not found, has no name"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Common/FigRemoteQueue/FigRemoteQueue.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWDeviceMotionActivityDetector.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigCaptureDeviceVendor.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureDevice.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureStream.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFrameStatistics.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWGraph.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWInvalidFramesChecker.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing noise reduction and sharpening parameters"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing portType"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing sensorIDDictionary"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing MBNR parameters for type '%d' and gain '%.1f'"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing noise reduction and sharpening parameters for type '%d' and gain '%.1f'"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWPixelBufferPool.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing PortType"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing cameraInfo"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDDictionary"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDString"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil input for %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil portType for %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@ took %lld ms"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@..."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Couldn't find Deep Fusion HDR EV0 count for EIT '%f': %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Missing portType"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then Long-Without-Sphere threshold: %@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then SIFR-Main threshold: %@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Motion and focus scores RFS is specified, but weights are missing: %@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. SIFR-Main threshold should be smaller then Long-Without-Sphere threshold: %@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWVideoFormat.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWAudioSourceNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWCameraInfoMetadataNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDeferredCaptureController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDepthConverterNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFileCoordinatorNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFrameRateGovernorNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWImageQueueSinkNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWIrisStagingNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWLearnSmartStyleRenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWMultiStreamCameraSourceNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWOverCaptureSmartStyleApplyNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderController.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPiecemealEncodingNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewStitcherNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewTimeMachineSinkNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSensitiveContentAnalyzerSinkNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSmartStyleReversibilityRenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSmartStyleTargetRenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageCoordinatorNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageScalerNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSynchronizerNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVISNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVideoPIPOverlayNode.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWAggdDataReporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWCoreAnalyticsReporter.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFencedAnimationQueue.m %s: Fenced animation queue wait timeout occurred - not queuing animation"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFigVideoCaptureSynchronizedStreamsGroup.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWPixelBufferTransferRenderer.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWStillImageMetadataUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWUtilities.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/Autofocus/FigSampleBufferProcessor_Autofocus.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: %d motion-related log messages filtered out (max of 1/s displayed from FigCoreMotionDelegate)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration fused vector is computed incorrectly"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration vector is computed incorrectly"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Allocation error when retrieving motion data"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Closest motion sample for timestamp %f has timestamp %f, difference %f\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not find motion sample to get Quaternion.\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not lock the ringMutex\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Frame timestamp is %f, Sample timestamps in the ring buffer are from %f to %f\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Gravity is computed incorrectly"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Potential missing three motion samples: new timestamp %f, latest timestamp %f\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: no data semaphore was available to wait on"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on hallPositionIndex %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f]."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find motion sample to get Quaternion."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming default value of 1.0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming value of %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Frame timestamp is from %f to %f, Sample timestamps in the ring buffer are from %f to %f, get %d motion samples"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Motion Hardware Unavailable - prototype hardware detected"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: No valid baseZoomFactor found, will proceed with a value of 1.0f."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Time interval %f is not positive"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Too many motion samples for the array"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Using default focus characterization entry because an entry corresponding to the original requested values was not found."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: invalid micronsPerPixel value %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed computing scaling factor"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed extracting metadata"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed getting ISPFrameCorrectionShiftValues. Using value of 0"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Unsupported sag removal method"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: sagPosition memory allocation failed"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Could not parse motion data from ISP due to error: %d"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Failed to allocate and initialize VISRotationCorrectionEstimator"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Height is missing from visInputPixelBufferAttributes"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData from metadataDict"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PinholeCameraFocalLength in metadataDict"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PortType from metadataDict"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSize for portType: %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSizeInMicrons for port %@"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing portType in metadataDict"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: No motion samples for this frame. Skipping processing"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Overscan is 0 or less. l:%f r:%f t:%f b:%f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Timestamp %f is earlier than previous sample %f"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Width is missing from visInputPixelBufferAttributes"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: focalLength is null"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.ruyb6J/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: pole must be between 0 and 1"
+ "08:29:03"
+ "<%@: %p> lowLightEIT=%f, sifrMainEIT=%f, sifrGain=%f, lowLightHDRWithoutSIFR=%f, longWithoutSphere=%f, deepFusion=%f, rsmMainEIT=%f, rsmSIFRGain=%f, toneCurveBehavior=%d, preserveBlackLevel=%d, afWindows=%p, refMethod=%d, usePreviousSIFR=%d, motionAndFocusScoreWeights=%@, maxNumberOfFramesForAdaptiveBracketing=%d, dFlashAvailableEIT=%f, dFlashRecommendedEIT=%f, dFlashStationaryRecommendedEIT=%f, dFlashAvailableSNR=%f, dFlashAvailableSNRLag=%f, dFlashRecommendedSNR=%f, dFlashRecommendedSNRLag=%f, dFlashStationaryRecommendedSNR=%f, dFlashStationaryRecommendedSNRLag=%f, dFlashRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashAERelativeDiff=%f%@"
+ "<%@: %p> type:%@, serviceBeforeGraphStop:%d, requestedSettings:%@%@"
+ "<<< FigCaptureCustomExposureConfiguration >>> %s: ISO underflow! (%g)  Capped to baseISO %g"
+ "<<<< BWDeferredContainerIntermediate >>>> %s: Using crop rect '%@' for captureID:%lld"
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
+ "<<<< BWGraph >>>> %s: <%p> Called with willBeStoppedImmediately=%d"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: Forcing immediate transition for pending live configuration: portType=%{public}@ output=%{public}@: liveConfigID=%lld -> requestedConfigID=%lld"
+ "<<<< BWProResRawMetadataUtilities >>>> %s: Got stabilization transforms for sbuf with input dimensions %d x %d, output dimensions %d x %d, transform rows %d, transform columns %d and transform step %d"
+ "<<<< BWProResRawMetadataUtilities >>>> %s: stabilizationTransformsParametersData data: %@"
+ "<<<< BWSmartFramingPerceptionSinkNode >>>> %s: %p: camGazeInferenceType must be %@, got %@"
+ "<<<< BWSmartFramingPerceptionSinkNode >>>> %s: init failed sinkID = %@ captureDevice = %p camGazeInferenceType = %d"
+ "<<<< BWSmartStyleLearningNode >>>> %s: _thumbnailsGenerationCommandQueue is nil"
+ "<<<< BWSmartStyleLearningNode >>>> %s: smartStyleThumbnailsGenerationCompletionQueue is nil"
+ "<<<< BWSmartStyleLearningNode >>>> %s: smartStyleThumbnailsGenerationSubmissionQueue is nil"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: %@ took %.2fms"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: %d capture request(s) were not serviced within %.2f seconds during graph stop"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: Photo #%d - processing flags: %@ identifier %{public}@/%{public}@"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: Waiting until DidCapturePhoto callback is sent before completing request for captureID:%lld"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: Waiting up to %.2f seconds for %d in-flight capture request(s) to be serviced before stopping"
+ "<<<< BWStillImageProcessing >>>> %s: Piecemeal encoding is not supported for attachedMediaKey:%{public}@ captureID:%lld -- skipping piecemeal encoding"
+ "<<<< BWStillImageProcessing >>>> %s: Piecemeal encoding is not supported for mode '%@' and settings %@"
+ "<<<< BWUtilities >>>> %s: Using tuning type '%@' for '%@' with capture flags '%@'"
+ "<<<< FigCaptureCameraSourcePipeline >>>> %s: smartFramingPerceptionSinkNode initialized with camGazeInferenceType: %@"
+ "<<<< FigCaptureSession >>>> %s: called with '%@' which should never happen!"
+ "BWPhotoEncoderSupportsPiecemealEncoding"
+ "BWUtilitiesSmartStyleTuningParameterVariantForCaptureType"
+ "BusyReasons"
+ "Digital Flash Available - Scene ( Normalized QSum SNR )"
+ "Digital Flash Recommended - Scene ( Normalized QSum SNR )"
+ "DigitalFlashAvailable"
+ "DigitalFlashRecommended"
+ "ExposureAreaOfInterest"
+ "Jun 27 2026"
+ "LastShownBuild:BWCameraInfoMetadataNode.m:531"
+ "LastShownBuild:BWCameraInfoMetadataNode.m:703"
+ "LastShownBuild:BWCoreAnalyticsReporter.m:387"
+ "LastShownBuild:BWDeferredCaptureController.m:468"
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
+ "LastShownBuild:BWLearnSmartStyleRenderer.m:335"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:13588"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:2717"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4399"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4406"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4413"
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
+ "LastShownBuild:BWPixelBufferPool.m:651"
+ "LastShownBuild:BWSmartStyleTargetRenderer.m:626"
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
+ "LastShownBuild:BWUtilities.m:1065"
+ "LastShownBuild:BWVideoFormat.m:1484"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1533"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:6235"
+ "LastShownBuild:FigCaptureSession.m:10919"
+ "LastShownBuild:FigCaptureSession.m:11114"
+ "LastShownBuild:FigCaptureSession.m:12026"
+ "LastShownBuild:FigCaptureSession.m:18514"
+ "LastShownBuild:FigCaptureSession.m:20016"
+ "LastShownBuild:FigCaptureSession.m:20019"
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
+ "LastShownBuild:FigCaptureSession.m:992"
+ "LastShownBuild:FigCaptureSessionStateManager.m:351"
+ "LastShownBuild:FigCaptureSessionStateManager.m:378"
+ "LastShownBuild:FigCaptureSessionStateManager.m:511"
+ "LastShownBuild:FigCaptureSourceBackingsProvider.m:2728"
+ "LastShownBuild:FigSampleBufferProcessor_Autofocus.m:928"
+ "LastShownDate:BWCameraInfoMetadataNode.m:531"
+ "LastShownDate:BWCameraInfoMetadataNode.m:703"
+ "LastShownDate:BWCoreAnalyticsReporter.m:387"
+ "LastShownDate:BWDeferredCaptureController.m:468"
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
+ "LastShownDate:BWLearnSmartStyleRenderer.m:335"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:13588"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:2717"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4399"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4406"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4413"
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
+ "LastShownDate:BWPixelBufferPool.m:651"
+ "LastShownDate:BWSmartStyleTargetRenderer.m:626"
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
+ "LastShownDate:BWUtilities.m:1065"
+ "LastShownDate:BWVideoFormat.m:1484"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1533"
+ "LastShownDate:FigCaptureMetadataUtilities.m:6235"
+ "LastShownDate:FigCaptureSession.m:10919"
+ "LastShownDate:FigCaptureSession.m:11114"
+ "LastShownDate:FigCaptureSession.m:12026"
+ "LastShownDate:FigCaptureSession.m:18514"
+ "LastShownDate:FigCaptureSession.m:20016"
+ "LastShownDate:FigCaptureSession.m:20019"
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
+ "LastShownDate:FigCaptureSession.m:992"
+ "LastShownDate:FigCaptureSessionStateManager.m:351"
+ "LastShownDate:FigCaptureSessionStateManager.m:378"
+ "LastShownDate:FigCaptureSessionStateManager.m:511"
+ "LastShownDate:FigCaptureSourceBackingsProvider.m:2728"
+ "LastShownDate:FigSampleBufferProcessor_Autofocus.m:928"
+ "MaximumCapacityComponents"
+ "MaximumCapacityComponentsExcludingPurgeable"
+ "Notification_BusyReasons"
+ "Payload_BusyFlags"
+ "PurgeableSpace"
+ "Service requests before graph stop"
+ "ServiceAssetBundleFailure"
+ "SetCapacityOption_Replenish"
+ "Stationary Digital Flash Recommended - Scene ( Normalized QSum SNR )"
+ "StationaryDigitalFlashRecommended"
+ "com.apple.coremedia.smartstyle-thumbnails-generation-completion-metal-queue"
+ "com.apple.coremedia.smartstyle-thumbnails-generation-submission-metal-queue"
+ "compressionCropRect"
+ "description=CameraCapture-758.0.0.0.1"
+ "ub.scene.digitalFlashAvailableSNR"
+ "ub.scene.digitalFlashRecommendedSNR"
+ "ub.scene.stationaryDigitalFlashRecommendedSNR"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0a\xf0\xf0Q"
- "-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:]"
- "-[BWFigVideoCaptureDevice setExposureModeCustomWithConfiguration:]"
- "-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]"
- "-[BWFileCoordinatorNode initWithNumberOfVideoInputs:numberOfAudioInputs:numberOfMetadataInputs:numberOfActionOnlyOutputs:overCaptureEnabled:allowLowLatencyWhenPossible:useTrueVideoFileRecordingStaging:motionDataTimeMachine:videoRecordingPrimingQueueLimit:]_block_invoke"
- "-[BWGraph waitForStartOrCommitToComplete]"
- "-[BWLearnSmartStyleRenderer _tuningParameterVariantForCaptureType:captureFlags:]"
- "-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:]"
- "-[BWPhotoEncoderController inputForStillImageSettings:portType:portraitAdjustedImage:optionalSampleBuffer:forEarlyEncoding:]_block_invoke"
- "-[BWSmartFramingPerceptionSinkNode initWithSinkID:captureDevice:inferenceScheduler:]"
- "-[BWSmartStyleTargetRenderer _tuningParameterVariantForCaptureType:captureFlags:]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/CMCaptureLocal/CMCaptureLocalSessionController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/CameraViewfinder/FigCaptureSessionObserver.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureMetadataUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSession.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionPipelines.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionStateManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSource.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSourceBackingsProvider.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/CMCaptureUserNotification.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureCommon.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unknown flip %i"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unsupported rotation of %d degrees"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: rotationDegrees (%d) is invalid, must be 0/90/180/270. Returning kFigExifOrientation_0RowTop0ColLeft (%d)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigCapturePixelFormatUtilities.m %s: Unexpected plist value for a pixel format type: %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Cannot look up key.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Not adding key.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Returning 0."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Key (%s) has already been registered. Not adding key.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: keyspace not found, has no name"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Common/FigRemoteQueue/FigRemoteQueue.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWDeviceMotionActivityDetector.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigCaptureDeviceVendor.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureDevice.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureStream.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFrameStatistics.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWGraph.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWInvalidFramesChecker.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing noise reduction and sharpening parameters"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing portType"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing sensorIDDictionary"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing MBNR parameters for type '%d' and gain '%.1f'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing noise reduction and sharpening parameters for type '%d' and gain '%.1f'"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWPixelBufferPool.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing PortType"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing cameraInfo"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDDictionary"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDString"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil input for %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil portType for %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@ took %lld ms"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@..."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Couldn't find Deep Fusion HDR EV0 count for EIT '%f': %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Missing portType"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then Long-Without-Sphere threshold: %@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then SIFR-Main threshold: %@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Motion and focus scores RFS is specified, but weights are missing: %@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. SIFR-Main threshold should be smaller then Long-Without-Sphere threshold: %@."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWVideoFormat.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWAudioSourceNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWCameraInfoMetadataNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDeferredCaptureController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDepthConverterNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFileCoordinatorNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFrameRateGovernorNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWImageQueueSinkNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWIrisStagingNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWLearnSmartStyleRenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWMultiStreamCameraSourceNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWOverCaptureSmartStyleApplyNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderController.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPiecemealEncodingNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewStitcherNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewTimeMachineSinkNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSensitiveContentAnalyzerSinkNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSmartStyleReversibilityRenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSmartStyleTargetRenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageCoordinatorNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageScalerNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSynchronizerNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVISNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVideoPIPOverlayNode.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWAggdDataReporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWCoreAnalyticsReporter.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFencedAnimationQueue.m %s: Fenced animation queue wait timeout occurred - not queuing animation"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFigVideoCaptureSynchronizedStreamsGroup.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWPixelBufferTransferRenderer.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWStillImageMetadataUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWUtilities.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/Autofocus/FigSampleBufferProcessor_Autofocus.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: %d motion-related log messages filtered out (max of 1/s displayed from FigCoreMotionDelegate)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration fused vector is computed incorrectly"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration vector is computed incorrectly"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Allocation error when retrieving motion data"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Closest motion sample for timestamp %f has timestamp %f, difference %f\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not find motion sample to get Quaternion.\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not lock the ringMutex\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Frame timestamp is %f, Sample timestamps in the ring buffer are from %f to %f\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Gravity is computed incorrectly"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Potential missing three motion samples: new timestamp %f, latest timestamp %f\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: no data semaphore was available to wait on"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on hallPositionIndex %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f]."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find motion sample to get Quaternion."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming default value of 1.0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming value of %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Frame timestamp is from %f to %f, Sample timestamps in the ring buffer are from %f to %f, get %d motion samples"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Motion Hardware Unavailable - prototype hardware detected"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: No valid baseZoomFactor found, will proceed with a value of 1.0f."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Time interval %f is not positive"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Too many motion samples for the array"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Using default focus characterization entry because an entry corresponding to the original requested values was not found."
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: invalid micronsPerPixel value %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed computing scaling factor"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed extracting metadata"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed getting ISPFrameCorrectionShiftValues. Using value of 0"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Unsupported sag removal method"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: sagPosition memory allocation failed"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Could not parse motion data from ISP due to error: %d"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Failed to allocate and initialize VISRotationCorrectionEstimator"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Height is missing from visInputPixelBufferAttributes"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData from metadataDict"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PinholeCameraFocalLength in metadataDict"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PortType from metadataDict"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSize for portType: %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSizeInMicrons for port %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing portType in metadataDict"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: No motion samples for this frame. Skipping processing"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Overscan is 0 or less. l:%f r:%f t:%f b:%f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Timestamp %f is earlier than previous sample %f"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Width is missing from visInputPixelBufferAttributes"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: focalLength is null"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.rL6gI4/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: pole must be between 0 and 1"
- "21:50:13"
- "<%@: %p> lowLightEIT=%f, sifrMainEIT=%f, sifrGain=%f, lowLightHDRWithoutSIFR=%f, longWithoutSphere=%f, deepFusion=%f, rsmMainEIT=%f, rsmSIFRGain=%f, toneCurveBehavior=%d, preserveBlackLevel=%d, afWindows=%p, refMethod=%d, usePreviousSIFR=%d, motionAndFocusScoreWeights=%@, maxNumberOfFramesForAdaptiveBracketing=%d, dFlashAvailableEIT=%f, dFlashRecommendedEIT=%f, dFlashStationaryRecommendedEIT=%f, dFlashRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashAERelativeDiff=%f"
- "<%@: %p> type:%@, requestedSettings:%@%@"
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
- "<<<< BWLearnSmartStyleRenderer >>>> %s: [%@] Using tuning type '%@' for '%@' with capture flags '%@'"
- "<<<< BWMultiStreamCameraSourceNode >>>> %s: Camera ISP (%{public}@) dropped frame"
- "<<<< BWProResRawMetadataUtilities >>>> %s: Got GPU transforms for sbuf with input dimensions %d x %d, output dimensions %d x %d, transform rows %d, transform columns %d and transform step %d"
- "<<<< BWProResRawMetadataUtilities >>>> %s: gpuTransformsParametersData data: %@"
- "<<<< BWSmartFramingPerceptionSinkNode >>>> %s: init failed sinkID = %@ captureDevice = %p"
- "<<<< BWSmartStyleLearningNode >>>> %s: newSmartStyle is nil"
- "<<<< BWSmartStyleTargetRenderer >>>> %s: [%@] Using tuning type '%@' for '%@' with capture flags '%@'"
- "<<<< BWStillImageCoordinatorNode >>>> %s: Photo #%d - processing flags: %d identifier %{public}@/%{public}@"
- "<<<< FigCaptureSession >>>> %s: called with BWStillImageCaptureTypeNone which should never happen!"
- "AutoExposureAreaOfInterest"
- "BWPhotoEncoderSupportsPiecemealEnocding"
- "Camera ISP (%{public}@) dropped frame"
- "Frame drop coming from camera ISP"
- "Jun 17 2026"
- "LastShownBuild:BWCameraInfoMetadataNode.m:533"
- "LastShownBuild:BWCameraInfoMetadataNode.m:707"
- "LastShownBuild:BWCoreAnalyticsReporter.m:384"
- "LastShownBuild:BWDeferredCaptureController.m:423"
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
- "LastShownBuild:BWLearnSmartStyleRenderer.m:338"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:13591"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:2710"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4387"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4394"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4401"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:9367"
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
- "LastShownBuild:BWPixelBufferPool.m:653"
- "LastShownBuild:BWSmartStyleTargetRenderer.m:629"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1197"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1201"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1407"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1414"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1484"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1567"
- "LastShownBuild:BWStillImageCoordinatorNode.m:2171"
- "LastShownBuild:BWStillImageCoordinatorNode.m:3630"
- "LastShownBuild:BWStillImageCoordinatorNode.m:618"
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
- "LastShownBuild:BWUtilities.m:1071"
- "LastShownBuild:BWVideoFormat.m:1500"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1498"
- "LastShownBuild:FigCaptureMetadataUtilities.m:6185"
- "LastShownBuild:FigCaptureSession.m:10881"
- "LastShownBuild:FigCaptureSession.m:11073"
- "LastShownBuild:FigCaptureSession.m:11975"
- "LastShownBuild:FigCaptureSession.m:18463"
- "LastShownBuild:FigCaptureSession.m:19965"
- "LastShownBuild:FigCaptureSession.m:19968"
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
- "LastShownBuild:FigCaptureSession.m:990"
- "LastShownBuild:FigCaptureSessionStateManager.m:352"
- "LastShownBuild:FigCaptureSessionStateManager.m:384"
- "LastShownBuild:FigCaptureSessionStateManager.m:517"
- "LastShownBuild:FigCaptureSourceBackingsProvider.m:2730"
- "LastShownBuild:FigSampleBufferProcessor_Autofocus.m:929"
- "LastShownDate:BWCameraInfoMetadataNode.m:533"
- "LastShownDate:BWCameraInfoMetadataNode.m:707"
- "LastShownDate:BWCoreAnalyticsReporter.m:384"
- "LastShownDate:BWDeferredCaptureController.m:423"
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
- "LastShownDate:BWLearnSmartStyleRenderer.m:338"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:13591"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:2710"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4387"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4394"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4401"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:9367"
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
- "LastShownDate:BWPixelBufferPool.m:653"
- "LastShownDate:BWSmartStyleTargetRenderer.m:629"
- "LastShownDate:BWStillImageCoordinatorNode.m:1197"
- "LastShownDate:BWStillImageCoordinatorNode.m:1201"
- "LastShownDate:BWStillImageCoordinatorNode.m:1407"
- "LastShownDate:BWStillImageCoordinatorNode.m:1414"
- "LastShownDate:BWStillImageCoordinatorNode.m:1484"
- "LastShownDate:BWStillImageCoordinatorNode.m:1567"
- "LastShownDate:BWStillImageCoordinatorNode.m:2171"
- "LastShownDate:BWStillImageCoordinatorNode.m:3630"
- "LastShownDate:BWStillImageCoordinatorNode.m:618"
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
- "LastShownDate:BWUtilities.m:1071"
- "LastShownDate:BWVideoFormat.m:1500"
- "LastShownDate:FigCaptureMetadataUtilities.m:1498"
- "LastShownDate:FigCaptureMetadataUtilities.m:6185"
- "LastShownDate:FigCaptureSession.m:10881"
- "LastShownDate:FigCaptureSession.m:11073"
- "LastShownDate:FigCaptureSession.m:11975"
- "LastShownDate:FigCaptureSession.m:18463"
- "LastShownDate:FigCaptureSession.m:19965"
- "LastShownDate:FigCaptureSession.m:19968"
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
- "LastShownDate:FigCaptureSession.m:990"
- "LastShownDate:FigCaptureSessionStateManager.m:352"
- "LastShownDate:FigCaptureSessionStateManager.m:384"
- "LastShownDate:FigCaptureSessionStateManager.m:517"
- "LastShownDate:FigCaptureSourceBackingsProvider.m:2730"
- "LastShownDate:FigSampleBufferProcessor_Autofocus.m:929"
- "MinimumValidFocusDistance"
- "SpotMeteredExposureAreaOfInterest"
- "description=CameraCapture-753.0.0.121.4"
- "|___ fsbp_Autofocus ___| %s: Update spot metered exposure area = {%.3f/%.3f %.3fx%.3f}"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0Q\xf0\xf0!"

```
