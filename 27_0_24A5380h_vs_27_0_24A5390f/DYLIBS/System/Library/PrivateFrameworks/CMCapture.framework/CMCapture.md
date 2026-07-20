## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

### Sections with Same Size but Changed Content

- `__TEXT.__dlopen_cstrs`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_floatobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-758.0.0.122.2
-  __TEXT.__text: 0x8c4fc0
-  __TEXT.__objc_methlist: 0x3a578
-  __TEXT.__const: 0x151770
-  __TEXT.__cstring: 0xff0b4
-  __TEXT.__oslogstring: 0x16645a
-  __TEXT.__gcc_except_tab: 0x4a94
+761.0.0.0.3
+  __TEXT.__text: 0x8cddc4
+  __TEXT.__objc_methlist: 0x3a9a8
+  __TEXT.__const: 0x151768
+  __TEXT.__cstring: 0xffc93
+  __TEXT.__oslogstring: 0x168211
+  __TEXT.__gcc_except_tab: 0x4be4
   __TEXT.__dlopen_cstrs: 0x7ad
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x11eb0
+  __TEXT.__unwind_info: 0x11f50
   __TEXT.__eh_frame: 0x38
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11328
-  __DATA_CONST.__objc_classlist: 0x1ef8
+  __DATA_CONST.__const: 0x11378
+  __DATA_CONST.__objc_classlist: 0x1f08
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x628
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x174f0
+  __DATA_CONST.__objc_selrefs: 0x176b0
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x1d10
+  __DATA_CONST.__objc_superrefs: 0x1d20
   __DATA_CONST.__objc_arraydata: 0x3bc8
-  __DATA_CONST.__got: 0x7058
-  __AUTH_CONST.__const: 0x4a58
-  __AUTH_CONST.__cfstring: 0x590a0
-  __AUTH_CONST.__objc_const: 0xa67d0
+  __DATA_CONST.__got: 0x7078
+  __AUTH_CONST.__const: 0x4ad8
+  __AUTH_CONST.__cfstring: 0x593a0
+  __AUTH_CONST.__objc_const: 0xa7038
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x6540
+  __AUTH_CONST.__objc_intobj: 0x6528
   __AUTH_CONST.__objc_arrayobj: 0x2c70
   __AUTH_CONST.__objc_floatobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x1798
   __AUTH_CONST.__objc_doubleobj: 0xab0
-  __AUTH_CONST.__auth_got: 0x2db0
-  __AUTH.__objc_data: 0x3b10
+  __AUTH_CONST.__auth_got: 0x2db8
+  __AUTH.__objc_data: 0x3bb0
   __AUTH.__data: 0x110
-  __DATA.__objc_ivar: 0xbdb0
+  __DATA.__objc_ivar: 0xbe64
   __DATA.__data: 0x5958
   __DATA.__crash_info: 0x148
-  __DATA.__common: 0x2c40
+  __DATA.__common: 0x2c90
   __DATA.__bss: 0x2df8
   __DATA_DIRTY.__objc_data: 0xfaa0
   __DATA_DIRTY.__data: 0xf98

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 41535
-  Symbols:   66932
-  CStrings:  38813
+  Functions: 41663
+  Symbols:   67152
+  CStrings:  38929
 
Symbols:
+ +[BWInferenceLazyVideoRequirement initialize]
+ +[BWStandardResolutionAttachmentNode initialize]
+ +[FigCaptureCustomFocusConfiguration focusConfigurationWithLensPosition:clampToHyperfocal:requestID:]
+ +[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByDeviceType:position:requestID:featuresEnabled:]
+ +[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByPortType:requestID:featuresEnabled:]
+ -[BWCameraStreamingMonitor _getClientInfoForTCCIdentity:clientPID:]
+ -[BWCompressedShotBufferNode _compressionOptionsWithCropRect:pixelFormat:preserveBorderRows:]
+ -[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:preserveTorchState:unsynchronizedStreamsStopSupported:]
+ -[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:unsynchronizedStreamsStopSupported:]
+ -[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:preserveTorchState:unsynchronizedStreamsStopSupported:]
+ -[BWFigCaptureSession stillImageCoordinator:didSelectVitalityMode:forSettings:]
+ -[BWFigCaptureStream didStop]
+ -[BWFigCaptureStream willStop]
+ -[BWFigVideoCaptureDevice lastKnownSubjectGazingState]
+ -[BWFigVideoCaptureDevice portTypesWithSoftISPClientBracketEnabled]
+ -[BWFigVideoCaptureDevice restoreLastKnownSubjectGazingState:]
+ -[BWFigVideoCaptureDevice setPortTypesWithSoftISPClientBracketEnabled:]
+ -[BWFigVideoCaptureDevice setShutterSoundRelaxationTrueVideoTransitionActive:]
+ -[BWFigVideoCaptureDevice shutterSoundRelaxationTrueVideoTransitionActive]
+ -[BWInferenceFaceQualityCropDescriptor initWithFaceIndex:boundingBoxScalingFactor:isDeviceOriented:]
+ -[BWIrisMovieGenerator disableVitalityForSettingsID:]
+ -[BWIrisMovieInfo setVitalityDisabled:]
+ -[BWIrisMovieInfo vitalityDisabled]
+ -[BWLandmarksInferenceConfiguration inferenceInputAttachedMediaKey]
+ -[BWLandmarksInferenceConfiguration setInferenceInputAttachedMediaKey:]
+ -[BWLearnedMattingInferenceConfiguration inferenceInputAttachedMediaKey]
+ -[BWLearnedMattingInferenceConfiguration initWithInferenceType:]
+ -[BWLearnedMattingInferenceConfiguration setInferenceInputAttachedMediaKey:]
+ -[BWMattingV2InferenceConfiguration inferenceInputAttachedMediaKey]
+ -[BWMattingV2InferenceConfiguration initWithInferenceType:]
+ -[BWMattingV2InferenceConfiguration setInferenceInputAttachedMediaKey:]
+ -[BWNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processHDRErrorRecovery:processOriginalImage:processLinearImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:]
+ -[BWNRFProcessorRequest initWithConfiguration:input:output:rawNightModeOutputFrame:deepFusionOutput:processErrorRecoveryFrame:processErrorRecoveryProxy:processHDRErrorRecovery:processOriginalImage:processLinearImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:inferencesAvailable:processSmartStyleRenderingInput:delegate:]
+ -[BWPersonSemanticsConfiguration dealloc]
+ -[BWPersonSemanticsConfiguration inferenceInputAttachedMediaKey]
+ -[BWPersonSemanticsConfiguration initWithInferenceType:]
+ -[BWPersonSemanticsConfiguration setInferenceInputAttachedMediaKey:]
+ -[BWPhotoDecompressor preserveBorderRows]
+ -[BWPhotoDecompressor setPreserveBorderRows:]
+ -[BWPhotoEncoderController _adjustAspectRatio:settings:applyOutputAspectRatioOverride:]
+ -[BWPhotoEncoderController _cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:applyOutputAspectRatioOverride:]
+ -[BWPhotonicEngineNodeConfiguration setSoftISPClientBracketEnabled:]
+ -[BWPhotonicEngineNodeConfiguration softISPClientBracketEnabled]
+ -[BWQuickTimeMovieFileSinkNode disableVitalityForSettingsID:]
+ -[BWStandardResolutionAttachmentNode _releaseResources]
+ -[BWStandardResolutionAttachmentNode dealloc]
+ -[BWStandardResolutionAttachmentNode didReachEndOfDataForConfigurationID:input:]
+ -[BWStandardResolutionAttachmentNode didSelectFormat:forInput:forAttachedMediaKey:]
+ -[BWStandardResolutionAttachmentNode handleNodeError:forInput:]
+ -[BWStandardResolutionAttachmentNode initWithStandardResolutionAttachedMediaKey:]
+ -[BWStandardResolutionAttachmentNode nodeSubType]
+ -[BWStandardResolutionAttachmentNode nodeType]
+ -[BWStandardResolutionAttachmentNode prepareForCurrentConfigurationToBecomeLive]
+ -[BWStandardResolutionAttachmentNode renderSampleBuffer:forInput:]
+ -[BWStillImageCoordinatorNode _didSelectVitalityMode:forSettings:]
+ -[BWStillImageCoordinatorNode node:didSelectVitalityMode:forSettings:]
+ -[BWStillImageFilterNode _emitMergedSampleBufferIfReadyForCaptureState:]
+ -[BWStillImageFilterNode _emitSampleBufferAsync:withNote:captureState:]
+ -[BWStillImageFilterNode _propagateAttachedMediaAndInferenceResultsFromStandardResToSampleBuffer:captureState:]
+ -[BWStillImageFilterNode _updateAndCachePortraitDataForBuffer:requestedSettings:renderContext:]
+ -[BWStillImageFilterNodeCaptureState _reset]
+ -[BWStillImageFilterNodeCaptureState attachedMediaFromStandardResolutionImage]
+ -[BWStillImageFilterNodeCaptureState blurMapRenderErrorFromStandardResolutionImage]
+ -[BWStillImageFilterNodeCaptureState blurredGainMapSbuf]
+ -[BWStillImageFilterNodeCaptureState commonEffectsSbuf]
+ -[BWStillImageFilterNodeCaptureState consumed]
+ -[BWStillImageFilterNodeCaptureState dealloc]
+ -[BWStillImageFilterNodeCaptureState description]
+ -[BWStillImageFilterNodeCaptureState faceAdjustedBlurMapFromStandardResolutionImage]
+ -[BWStillImageFilterNodeCaptureState inferenceResultsFromStandardResolutionImage]
+ -[BWStillImageFilterNodeCaptureState initWithExpectedSbufEmits:]
+ -[BWStillImageFilterNodeCaptureState learnedCoefficientsSbuf]
+ -[BWStillImageFilterNodeCaptureState portraitStillImageAuxDepthMetadata]
+ -[BWStillImageFilterNodeCaptureState releaseStashedAttachedMediaAndInferenceResultsFromStandardRes]
+ -[BWStillImageFilterNodeCaptureState releaseStyledUnstyledSynchronizationBuffers]
+ -[BWStillImageFilterNodeCaptureState sbufEmitted]
+ -[BWStillImageFilterNodeCaptureState setAttachedMediaFromStandardResolutionImage:]
+ -[BWStillImageFilterNodeCaptureState setBlurMapRenderErrorFromStandardResolutionImage:]
+ -[BWStillImageFilterNodeCaptureState setBlurredGainMapSbuf:]
+ -[BWStillImageFilterNodeCaptureState setCommonEffectsSbuf:]
+ -[BWStillImageFilterNodeCaptureState setFaceAdjustedBlurMapFromStandardResolutionImage:]
+ -[BWStillImageFilterNodeCaptureState setInferenceResultsFromStandardResolutionImage:]
+ -[BWStillImageFilterNodeCaptureState setLearnedCoefficientsSbuf:]
+ -[BWStillImageFilterNodeCaptureState setPortraitStillImageAuxDepthMetadata:]
+ -[BWStillImageFilterNodeCaptureState setStyledFullResolutionSbuf:]
+ -[BWStillImageFilterNodeCaptureState setUnneeded:]
+ -[BWStillImageFilterNodeCaptureState setUnstyledFullResolutionSbuf:]
+ -[BWStillImageFilterNodeCaptureState stashMediaFromRenderedBlurMap:]
+ -[BWStillImageFilterNodeCaptureState styledFullResolutionSbuf]
+ -[BWStillImageFilterNodeCaptureState transferManager]
+ -[BWStillImageFilterNodeCaptureState unneeded]
+ -[BWStillImageFilterNodeCaptureState unstyledFullResolutionSbuf]
+ -[BWStillImageFilterNodeRenderContext captureState]
+ -[BWStillImageFilterNodeRenderContext setCaptureState:]
+ -[BWStreamingCameraCalibrationDataNode configurationWithID:updatedFormat:didBecomeLiveForInput:]
+ -[BWStreamingCameraCalibrationDataNode hasNonLiveConfigurationChanges]
+ -[BWStreamingCameraCalibrationDataNode makeCurrentConfigurationLive]
+ -[BWTemporalFilterNode _prepareVTTemporalFilterSession]
+ -[BWTemporalFilterNode didReachEndOfDataForConfigurationID:input:]
+ -[BWTemporalFilterNode hasNonLiveConfigurationChanges]
+ -[BWUBCaptureParameters digitalFlashBacklitRecommendFlashNormalizedSNRHysteresisLag]
+ -[BWUBCaptureParameters digitalFlashBacklitRecommendFlashNormalizedSNRThreshold]
+ -[BWUBCaptureParameters digitalFlashRecommendFlashNormalizedSNRHysteresisLag]
+ -[BWUBCaptureParameters digitalFlashRecommendFlashNormalizedSNRThreshold]
+ -[FigCaptureAncillaryDataHIDTransmitter openDeviceWithUsagePage:vendor:product:error:]
+ -[FigCaptureAncillaryDataHIDTransmitter setTargetProduct:]
+ -[FigCaptureAncillaryDataHIDTransmitter setTargetVendor:]
+ -[FigCaptureAncillaryDataHIDTransmitter targetProduct]
+ -[FigCaptureAncillaryDataHIDTransmitter targetVendor]
+ -[FigCaptureCameraCalibrationDataSinkPipeline _buildCameraCalibrationDataSinkPipelineWithConfiguration:sourceOutput:graph:cameraInfoByPortType:additionalRotationDegrees:clientAuditToken:delegate:]
+ -[FigCaptureCameraCalibrationDataSinkPipeline initWithConfiguration:sourceOutput:graph:name:cameraInfoByPortType:additionalRotationDegrees:clientAuditToken:delegate:]
+ -[FigCaptureCustomFocusConfiguration _initWithLensPosition:clampToHyperfocal:requestID:]
+ -[FigCaptureCustomWhiteBalanceConfiguration _initWithGainsByPortType:requestID:featuresEnabled:]
+ -[FigCapturePhotonicEngineSinkPipeline _addLandmarksInferenceToNode:withInferenceInputAttachedMediaKey:]
+ -[FigCapturePhotonicEngineSinkPipeline _addMattingInferenceToNode:mattingVersion:learnedMattingEnabled:learnedMattingVersion:mainImageDownscalingFactor:targetAspectRatio:appliesFinalCropRect:enabledSemantics:metalCommandQueue:mattingSensorConfigurationsByPortType:clientIsCameraOrDerivative:requiredAdditionalInferenceOutputBuffers:stillImageFusionScheme:inferenceInputAttachedMediaKey:]
+ -[FigCapturePhotonicEngineSinkPipeline _createPersonSemanticsInferenceConfigurationWithPipelineConfiguration:personSegmentationEnabled:appliesFinalCropRect:]
+ -[FigCaptureSessionConfiguration reasonForNotEqualingConfigurationIgnoringConfigurationID:]
+ -[FigCaptureSessionStateManager sessionClearNonSystemInterruption]
+ -[FigCaptureStillImageSettings outputAspectRatioOverride]
+ -[FigCaptureStillImageSettings setOutputAspectRatioOverride:]
+ -[TrackedSubject _updateGazeStatesUsingGazeProbabilitiesData:gazeScoreOut:]
+ -[TrackedSubject initWithGroupID:significanceDetectionThreshold:smartFramingSceneMonitorMode:isPet:]
+ GCC_except_table100
+ GCC_except_table158
+ GCC_except_table187
+ GCC_except_table220
+ GCC_except_table322
+ GCC_except_table350
+ GCC_except_table352
+ GCC_except_table408
+ GCC_except_table409
+ GCC_except_table688
+ GCC_except_table77
+ _BWNodeSubTypeStandardResolutionAttachment
+ _CGRectInfinite
+ _CMILSCOISAdaptation_convertV3LSCTableToV2LSCTableWithAperture
+ _OBJC_CLASS_$_BWStandardResolutionAttachmentNode
+ _OBJC_CLASS_$_BWStillImageFilterNodeCaptureState
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._consecutiveNotGazingFrameCount
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._digitalFlashBacklitRecommendFlashSceneByPortType
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._digitalFlashRecommendFlashSceneByPortType
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._portTypesWithSoftISPClientBracketEnabled
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._shutterSoundRelaxationTrueVideoTransitionActive
+ _OBJC_IVAR_$_BWFigVideoCaptureStream._temporalNoiseReductionRawEnabled
+ _OBJC_IVAR_$_BWInferenceFaceQualityCropDescriptor._deviceOriented
+ _OBJC_IVAR_$_BWIrisMovieInfo._vitalityDisabled
+ _OBJC_IVAR_$_BWLandmarksInferenceConfiguration._inferenceInputAttachedMediaKey
+ _OBJC_IVAR_$_BWLearnedMattingInferenceConfiguration._inferenceInputAttachedMediaKey
+ _OBJC_IVAR_$_BWMattingV2InferenceConfiguration._inferenceInputAttachedMediaKey
+ _OBJC_IVAR_$_BWNRFProcessorRequest._processHDRErrorRecovery
+ _OBJC_IVAR_$_BWPersonSemanticsConfiguration._inferenceInputAttachedMediaKey
+ _OBJC_IVAR_$_BWPhotoDecompressor._preserveBorderRows
+ _OBJC_IVAR_$_BWPhotonicEngineNodeConfiguration._softISPClientBracketEnabled
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._pendingVitalityDisabledSettingsIDs
+ _OBJC_IVAR_$_BWRealtimeCinematographyNode._firstFramePTS
+ _OBJC_IVAR_$_BWRealtimeCinematographyNode._frameCount
+ _OBJC_IVAR_$_BWRealtimeCinematographyNode._halfRatePreviewTimeThresholdSeconds
+ _OBJC_IVAR_$_BWRealtimeCinematographyNode._thermalConstraintActive
+ _OBJC_IVAR_$_BWRealtimeCinematographyNode._thermalMonitor
+ _OBJC_IVAR_$_BWSmartCropNode._rtscProcessorInitQueue
+ _OBJC_IVAR_$_BWStandardResolutionAttachmentNode._formatDescription
+ _OBJC_IVAR_$_BWStandardResolutionAttachmentNode._pixelBufferProvider
+ _OBJC_IVAR_$_BWStandardResolutionAttachmentNode._standardResAttachedMediaKey
+ _OBJC_IVAR_$_BWStandardResolutionAttachmentNode._standardResolutionDimensions
+ _OBJC_IVAR_$_BWStandardResolutionAttachmentNode._transferSession
+ _OBJC_IVAR_$_BWStillImageFilterNode._captureStateByCaptureIdentifier
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._attachedMediaFromStandardResolutionImage
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._blurMapRenderErrorFromStandardResolutionImage
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._blurredGainMapSbuf
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._commonEffectsSbuf
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._consumed
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._faceAdjustedBlurMapFromStandardResolutionImage
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._inferenceResultsFromStandardResolutionImage
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._learnedCoefficientsSbuf
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._pendingSbufEmits
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._portraitStillImageAuxDepthMetadata
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._styledFullResolutionSbuf
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._transferManager
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._unneeded
+ _OBJC_IVAR_$_BWStillImageFilterNodeCaptureState._unstyledFullResolutionSbuf
+ _OBJC_IVAR_$_BWStillImageFilterNodeRenderContext._captureState
+ _OBJC_IVAR_$_BWStreamingCameraCalibrationDataNode._liveRotationDegrees
+ _OBJC_IVAR_$_BWStreamingCameraCalibrationDataNode._preparedRotationDegrees
+ _OBJC_IVAR_$_BWTemporalFilterNode._liveSessionHeight
+ _OBJC_IVAR_$_BWTemporalFilterNode._liveSessionInputPixelFormat
+ _OBJC_IVAR_$_BWTemporalFilterNode._liveSessionOutputPixelFormat
+ _OBJC_IVAR_$_BWTemporalFilterNode._liveSessionWidth
+ _OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashBacklitRecommendFlashNormalizedSNRHysteresisLag
+ _OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashBacklitRecommendFlashNormalizedSNRThreshold
+ _OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashRecommendFlashNormalizedSNRHysteresisLag
+ _OBJC_IVAR_$_BWUBCaptureParameters._digitalFlashRecommendFlashNormalizedSNRThreshold
+ _OBJC_IVAR_$_FigCaptureAncillaryDataHIDTransmitter._targetProduct
+ _OBJC_IVAR_$_FigCaptureAncillaryDataHIDTransmitter._targetVendor
+ _OBJC_IVAR_$_FigCaptureCameraCalibrationDataSinkPipeline._mirroringEnabled
+ _OBJC_IVAR_$_FigCaptureCameraCalibrationDataSinkPipeline._rotationDegrees
+ _OBJC_IVAR_$_FigCaptureCameraCalibrationDataSinkPipeline._streamingCameraCalibrationDataNode
+ _OBJC_IVAR_$_FigCaptureCustomFocusConfiguration._clampToHyperfocalLogicalLensPositionEnabled
+ _OBJC_IVAR_$_FigCaptureCustomWhiteBalanceConfiguration._featuresEnabled
+ _OBJC_IVAR_$_FigCaptureDeferredProcessingEngine._lastJobQoS
+ _OBJC_IVAR_$_FigCaptureStillImageSettings._outputAspectRatioOverride
+ _OBJC_METACLASS_$_BWStandardResolutionAttachmentNode
+ _OBJC_METACLASS_$_BWStillImageFilterNodeCaptureState
+ __OBJC_$_CLASS_METHODS_BWInferenceLazyVideoRequirement
+ __OBJC_$_CLASS_METHODS_BWStandardResolutionAttachmentNode
+ __OBJC_$_INSTANCE_METHODS_BWStandardResolutionAttachmentNode
+ __OBJC_$_INSTANCE_METHODS_BWStillImageFilterNodeCaptureState
+ __OBJC_$_INSTANCE_VARIABLES_BWStandardResolutionAttachmentNode
+ __OBJC_$_INSTANCE_VARIABLES_BWStillImageFilterNodeCaptureState
+ __OBJC_$_PROP_LIST_BWStillImageFilterNodeCaptureState
+ __OBJC_CLASS_RO_$_BWStandardResolutionAttachmentNode
+ __OBJC_CLASS_RO_$_BWStillImageFilterNodeCaptureState
+ __OBJC_METACLASS_RO_$_BWStandardResolutionAttachmentNode
+ __OBJC_METACLASS_RO_$_BWStillImageFilterNodeCaptureState
+ ___250-[BWRealtimeCinematographyNode initWithObjectMetadataIdentifiers:cachedSimulatedAperture:captureDevice:tuningParameters:videoDepthConfiguration:smartStyleLearningEnabled:highResolutionInputEnabled:transformCinematographyDetectionsForMovieFileOutput:]_block_invoke
+ ___26-[BWSmartCropNode dealloc]_block_invoke
+ ___47-[BWSmartCropNode renderSampleBuffer:forInput:]_block_invoke
+ ___54-[BWStillImageFilterNode renderSampleBuffer:forInput:]_block_invoke
+ ___59-[BWPhotonicEngineNodeResourceCoordinator releaseResources]_block_invoke_2
+ ___59-[BWPhotonicEngineNodeResourceCoordinator releaseResources]_block_invoke_3
+ ___59-[BWPhotonicEngineNodeResourceCoordinator releaseResources]_block_invoke_4
+ ___61-[BWSmartCropNode prepareForCurrentConfigurationToBecomeLive]_block_invoke
+ ___66-[BWTemporalFilterNode didReachEndOfDataForConfigurationID:input:]_block_invoke
+ ___66-[FigCaptureSessionStateManager sessionClearNonSystemInterruption]_block_invoke
+ ___67-[BWCameraStreamingMonitor _getClientInfoForTCCIdentity:clientPID:]_block_invoke
+ ___67-[BWCameraStreamingMonitor _getClientInfoForTCCIdentity:clientPID:]_block_invoke_2
+ ___70-[BWStillImageCoordinatorNode node:didSelectVitalityMode:forSettings:]_block_invoke
+ ___71-[BWStillImageFilterNode _emitSampleBufferAsync:withNote:captureState:]_block_invoke
+ ___block_descriptor_40_e8_32o_e61_v32?0"NSString"8"BWStillImageFilterNodeCaptureState"16^B24ls32l8
+ ___captureSession_teardownGraph_block_invoke
+ ___captureSession_teardownGraph_block_invoke_2
+ _gBWInferenceLazyVideoRequirementTrace
+ _gBWStandardResolutionAttachmentNode
+ _kCMPhotoCompressionOption_ExtractAndStoreBorderRowsSeparately
+ _kCMPhotoDecompressionOption_ApplyBorderRows
+ _kFigCaptureSourceWhiteBalanceOperationKey_FeaturesEnabled
+ _kFigQuickTimeMetadataKey_LivePhotoVitalityDisabled
+ _kFigVirtualCaptureCardProperty_InitialCapacityOverhead
+ _objc_msgSend$_adjustAspectRatio:settings:applyOutputAspectRatioOverride:
+ _objc_msgSend$_cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:applyOutputAspectRatioOverride:
+ _objc_msgSend$_initWithGainsByPortType:requestID:featuresEnabled:
+ _objc_msgSend$_initWithLensPosition:clampToHyperfocal:requestID:
+ _objc_msgSend$_updateGazeStatesUsingGazeProbabilitiesData:gazeScoreOut:
+ _objc_msgSend$attachedMediaFromStandardResolutionImage
+ _objc_msgSend$beginIrisMovieCaptureTime
+ _objc_msgSend$blurMapRenderErrorFromStandardResolutionImage
+ _objc_msgSend$blurredGainMapSbuf
+ _objc_msgSend$captureState
+ _objc_msgSend$commonEffectsSbuf
+ _objc_msgSend$consumed
+ _objc_msgSend$didStop
+ _objc_msgSend$digitalFlashBacklitRecommendFlashNormalizedSNRHysteresisLag
+ _objc_msgSend$digitalFlashBacklitRecommendFlashNormalizedSNRThreshold
+ _objc_msgSend$digitalFlashRecommendFlashNormalizedSNRHysteresisLag
+ _objc_msgSend$digitalFlashRecommendFlashNormalizedSNRThreshold
+ _objc_msgSend$disableVitalityForSettingsID:
+ _objc_msgSend$enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processHDRErrorRecovery:processOriginalImage:processLinearImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:
+ _objc_msgSend$faceAdjustedBlurMapFromStandardResolutionImage
+ _objc_msgSend$faceId
+ _objc_msgSend$hyperfocalLogicalFocusLensPosition
+ _objc_msgSend$inferenceInputAttachedMediaKey
+ _objc_msgSend$inferenceResultsFromStandardResolutionImage
+ _objc_msgSend$initWithExpectedSbufEmits:
+ _objc_msgSend$initWithFaceIndex:boundingBoxScalingFactor:isDeviceOriented:
+ _objc_msgSend$initWithGroupID:significanceDetectionThreshold:smartFramingSceneMonitorMode:isPet:
+ _objc_msgSend$invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:unsynchronizedStreamsStopSupported:
+ _objc_msgSend$lastKnownSubjectGazingState
+ _objc_msgSend$learnedCoefficientsSbuf
+ _objc_msgSend$openDeviceWithUsagePage:vendor:product:error:
+ _objc_msgSend$outputAspectRatioOverride
+ _objc_msgSend$portTypesWithSoftISPClientBracketEnabled
+ _objc_msgSend$portraitStillImageAuxDepthMetadata
+ _objc_msgSend$reasonForNotEqualingConfigurationIgnoringConfigurationID:
+ _objc_msgSend$releaseStashedAttachedMediaAndInferenceResultsFromStandardRes
+ _objc_msgSend$releaseStyledUnstyledSynchronizationBuffers
+ _objc_msgSend$restoreLastKnownSubjectGazingState:
+ _objc_msgSend$sbufEmitted
+ _objc_msgSend$sessionClearNonSystemInterruption
+ _objc_msgSend$setBlurMapRenderErrorFromStandardResolutionImage:
+ _objc_msgSend$setBlurredGainMapSbuf:
+ _objc_msgSend$setCaptureState:
+ _objc_msgSend$setCommonEffectsSbuf:
+ _objc_msgSend$setInferenceInputAttachedMediaKey:
+ _objc_msgSend$setLearnedCoefficientsSbuf:
+ _objc_msgSend$setOutputAspectRatioOverride:
+ _objc_msgSend$setPortTypesWithSoftISPClientBracketEnabled:
+ _objc_msgSend$setShutterSoundRelaxationTrueVideoTransitionActive:
+ _objc_msgSend$setStyledFullResolutionSbuf:
+ _objc_msgSend$setTargetVendor:
+ _objc_msgSend$setUnneeded:
+ _objc_msgSend$setUnstyledFullResolutionSbuf:
+ _objc_msgSend$setVitalityDisabled:
+ _objc_msgSend$stashMediaFromRenderedBlurMap:
+ _objc_msgSend$stillImageCoordinator:didSelectVitalityMode:forSettings:
+ _objc_msgSend$styledFullResolutionSbuf
+ _objc_msgSend$subjectRelightingEnabled
+ _objc_msgSend$transferManager
+ _objc_msgSend$unneeded
+ _objc_msgSend$unstyledFullResolutionSbuf
+ _objc_msgSend$vitalityDisabled
+ _objc_msgSend$willStop
+ _vcc_getInitialCapacityOverhead
- +[FigCaptureCustomFocusConfiguration focusConfigurationWithLensPosition:requestID:]
- +[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByDeviceType:position:requestID:]
- +[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByPortType:requestID:]
- -[BWCameraStreamingMonitor _getClientInfoForTCCIdentity:clientPID:sessionIsPrewarming:]
- -[BWCompressedShotBufferNode _compressionOptionsWithCropRect:pixelFormat:]
- -[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:preserveTorchState:]
- -[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:]
- -[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:preserveTorchState:]
- -[BWFigCaptureStream synchronizedStreamsGroupDidStop]
- -[BWFigCaptureStream synchronizedStreamsGroupWillStop]
- -[BWInferenceFaceQualityCropDescriptor initWithFaceIndex:boundingBoxScalingFactor:]
- -[BWNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processOriginalImage:processLinearImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:]
- -[BWNRFProcessorRequest initWithConfiguration:input:output:rawNightModeOutputFrame:deepFusionOutput:processErrorRecoveryFrame:processErrorRecoveryProxy:processOriginalImage:processLinearImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:inferencesAvailable:processSmartStyleRenderingInput:delegate:]
- -[BWPhotoEncoderController _adjustAspectRatio:settings:]
- -[BWPhotoEncoderController _cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:]
- -[BWStillImageFilterNode _emitMergedSampleBufferIfReady]
- -[BWStillImageFilterNode _emitSampleBufferAsync:withNote:]
- -[BWStillImageFilterNode _propagateAttachedMediaAndInferenceResultsFromStandardResToSampleBuffer:]
- -[BWStillImageFilterNode _releaseStashedAttachedMediaAndInferenceResultsFromStandardRes]
- -[BWStillImageFilterNode _releaseStyledUnstyledSynchronizationBuffers]
- -[BWStillImageFilterNode _updateAndCachePortraitDataForBuffer:requestedSettings:]
- -[BWTemporalFilterNode didReachEndOfDataForInput:]
- -[FigCaptureAncillaryDataHIDTransmitter openDeviceWithUsagePage:usage:error:]
- -[FigCaptureAncillaryDataHIDTransmitter setTargetUsage:]
- -[FigCaptureAncillaryDataHIDTransmitter targetUsage]
- -[FigCaptureCameraCalibrationDataSinkPipeline _buildCameraCalibrationDataSinkPipelineWithConfiguration:sourceOutput:graph:cameraInfoByPortType:clientAuditToken:delegate:]
- -[FigCaptureCameraCalibrationDataSinkPipeline initWithConfiguration:sourceOutput:graph:name:cameraInfoByPortType:clientAuditToken:delegate:]
- -[FigCaptureCustomFocusConfiguration _initWithLensPosition:requestID:]
- -[FigCaptureCustomWhiteBalanceConfiguration _initWithGainsByPortType:requestID:]
- -[FigCapturePhotonicEngineSinkPipeline _addLandmarksInferenceToNode:]
- -[FigCapturePhotonicEngineSinkPipeline _addMattingInferenceToNode:mattingVersion:learnedMattingEnabled:learnedMattingVersion:mainImageDownscalingFactor:targetAspectRatio:appliesFinalCropRect:enabledSemantics:metalCommandQueue:mattingSensorConfigurationsByPortType:clientIsCameraOrDerivative:requiredAdditionalInferenceOutputBuffers:stillImageFusionScheme:]
- -[FigCaptureSessionStateManager clearNonSystemInterruption]
- -[TrackedSubject _updateGazeStatesUsingGazeProbabilitiesData:gazeScoreOut:gazeScoreFilteredOut:]
- -[TrackedSubject initWithGroupID:significanceDetectionThreshold:gazeFilteringStrength:smartFramingSceneMonitorMode:isPet:]
- -[TrackedSubject isSignificantFiltered]
- GCC_except_table157
- GCC_except_table186
- GCC_except_table217
- GCC_except_table319
- GCC_except_table340
- GCC_except_table347
- GCC_except_table349
- GCC_except_table406
- GCC_except_table686
- GCC_except_table89
- _OBJC_IVAR_$_BWStillImageFilterNode._attachedMediaFromStandardResolutionImage
- _OBJC_IVAR_$_BWStillImageFilterNode._blurMapRenderErrorFromStandardResolutionImage
- _OBJC_IVAR_$_BWStillImageFilterNode._blurredGainMapSbuf
- _OBJC_IVAR_$_BWStillImageFilterNode._commonEffectsSbuf
- _OBJC_IVAR_$_BWStillImageFilterNode._faceAdjustedBlurMapFromStandardResolutionImage
- _OBJC_IVAR_$_BWStillImageFilterNode._inferenceResultsFromStandardResolutionImage
- _OBJC_IVAR_$_BWStillImageFilterNode._learnedCoefficientsSbuf
- _OBJC_IVAR_$_BWStillImageFilterNode._portraitStillImageAuxDepthMetadata
- _OBJC_IVAR_$_BWStillImageFilterNode._styledFullResolutionSbuf
- _OBJC_IVAR_$_BWStillImageFilterNode._transferManager
- _OBJC_IVAR_$_BWStillImageFilterNode._unstyledFullResolutionSbuf
- _OBJC_IVAR_$_BWStreamingCameraCalibrationDataNode._rotationDegrees
- _OBJC_IVAR_$_FigCaptureAncillaryDataHIDTransmitter._targetUsage
- _OBJC_IVAR_$_SubjectSelection._gazeFilteringStrength
- _OBJC_IVAR_$_TrackedSubject._gazeFilteringStrength
- _OBJC_IVAR_$_TrackedSubject._gazeScoreFiltered
- _OBJC_IVAR_$_TrackedSubject._isSignificantFiltered
- _OUTLINED_FUNCTION_733
- _OUTLINED_FUNCTION_734
- ___50-[BWTemporalFilterNode didReachEndOfDataForInput:]_block_invoke
- ___58-[BWStillImageFilterNode _emitSampleBufferAsync:withNote:]_block_invoke
- ___59-[FigCaptureSessionStateManager clearNonSystemInterruption]_block_invoke
- _objc_msgSend$_adjustAspectRatio:settings:
- _objc_msgSend$_cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:
- _objc_msgSend$_initWithGainsByPortType:requestID:
- _objc_msgSend$_initWithLensPosition:requestID:
- _objc_msgSend$_updateGazeStatesUsingGazeProbabilitiesData:gazeScoreOut:gazeScoreFilteredOut:
- _objc_msgSend$clearNonSystemInterruption
- _objc_msgSend$enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processOriginalImage:processLinearImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:
- _objc_msgSend$initWithFaceIndex:boundingBoxScalingFactor:
- _objc_msgSend$initWithGroupID:significanceDetectionThreshold:gazeFilteringStrength:smartFramingSceneMonitorMode:isPet:
- _objc_msgSend$invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:
- _objc_msgSend$openDeviceWithUsagePage:usage:error:
- _objc_msgSend$setTargetUsage:
- _objc_msgSend$synchronizedStreamsGroupDidStop
- _objc_msgSend$synchronizedStreamsGroupWillStop
CStrings:
+ " AROverride:%.3f"
+ " backgroundQoSTransition: {lastJobQoS:%@, currentJobQoS:%@}"
+ "!"
+ "%@ %p: captureID:%lld '%.4s'('%.4s')%@ %dx%d R:%d%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
+ "%@ %p: requestID:%d appliedFrameStatistics:%@ featuresEnabled:%@"
+ "(*modified by aspect-ratio override)"
+ "+[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByDeviceType:position:requestID:featuresEnabled:]"
+ "-[BWCameraStreamingMonitor _getClientInfoForTCCIdentity:clientPID:]"
+ "-[BWCompressedShotBufferNode _compressionOptionsWithCropRect:pixelFormat:preserveBorderRows:]"
+ "-[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:preserveTorchState:unsynchronizedStreamsStopSupported:]"
+ "-[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:unsynchronizedStreamsStopSupported:]"
+ "-[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:preserveTorchState:unsynchronizedStreamsStopSupported:]"
+ "-[BWFigCaptureSession stillImageCoordinator:didSelectVitalityMode:forSettings:]"
+ "-[BWFigCaptureStream didStop]"
+ "-[BWInferenceFaceQualityCropDescriptor rectForSampleBuffer:]"
+ "-[BWInferenceLazyVideoRequirement prepareForInputInferenceVideoFormat:]"
+ "-[BWIrisMovieGenerator disableVitalityForSettingsID:]"
+ "-[BWNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processHDRErrorRecovery:processOriginalImage:processLinearImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:]"
+ "-[BWPhotoEncoderController _cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:applyOutputAspectRatioOverride:]"
+ "-[BWQuickTimeMovieFileSinkNode dealloc]"
+ "-[BWQuickTimeMovieFileSinkNode disableVitalityForSettingsID:]"
+ "-[BWRealtimeCinematographyNode initWithObjectMetadataIdentifiers:cachedSimulatedAperture:captureDevice:tuningParameters:videoDepthConfiguration:smartStyleLearningEnabled:highResolutionInputEnabled:transformCinematographyDetectionsForMovieFileOutput:]_block_invoke"
+ "-[BWStandardResolutionAttachmentNode didSelectFormat:forInput:forAttachedMediaKey:]"
+ "-[BWStandardResolutionAttachmentNode handleNodeError:forInput:]"
+ "-[BWStandardResolutionAttachmentNode initWithStandardResolutionAttachedMediaKey:]"
+ "-[BWStandardResolutionAttachmentNode prepareForCurrentConfigurationToBecomeLive]"
+ "-[BWStandardResolutionAttachmentNode renderSampleBuffer:forInput:]"
+ "-[BWStillImageFilterNode _emitMergedSampleBufferIfReadyForCaptureState:]"
+ "-[BWStillImageFilterNode _emitSampleBufferAsync:withNote:captureState:]"
+ "-[BWStillImageFilterNode _emitSampleBufferAsync:withNote:captureState:]_block_invoke"
+ "-[BWStillImageFilterNode _updateAndCachePortraitDataForBuffer:requestedSettings:renderContext:]"
+ "-[BWTemporalFilterNode _prepareVTTemporalFilterSession]"
+ "-[BWTemporalFilterNode didReachEndOfDataForConfigurationID:input:]"
+ "-[BWTemporalFilterNode didReachEndOfDataForConfigurationID:input:]_block_invoke"
+ "-[FigCaptureAncillaryDataHIDTransmitter openDeviceWithUsagePage:vendor:product:error:]"
+ "-[FigCaptureCustomExposureConfiguration applyFrameStatistics:forPortTypes:primaryPortType:limitsByPortType:]"
+ "-[FigCapturePhotonicEngineSinkPipeline _addMattingInferenceToNode:mattingVersion:learnedMattingEnabled:learnedMattingVersion:mainImageDownscalingFactor:targetAspectRatio:appliesFinalCropRect:enabledSemantics:metalCommandQueue:mattingSensorConfigurationsByPortType:clientIsCameraOrDerivative:requiredAdditionalInferenceOutputBuffers:stillImageFusionScheme:inferenceInputAttachedMediaKey:]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStandardResolutionAttachmentNode.m"
+ "03:44:45"
+ "0420660d42bf570c07c108cda1c5525f4661f842"
+ "1905686"
+ "9fa40d7f1ad23d955216065bfcf66a95ad58a82a"
+ "<%@ %p>: captureID:%lld, captureType=%@, %@, errorRecovery=%d errorRecoveryProxy=%d hdrErrorRecovery=%d original=%d linear=%d tonemap=%d inferenceInput=%d semanticRendering=%d inferenceInputForProcessing=%d inferences=%d input:<%@ %p>"
+ "<%@ %p>: pendingEmits:%d, consumed:%d, blurMap:%@, attachedMediaKeys:%lu, inferenceResultsKeys:%lu, auxDepth:%p, gainMapSbuf:%p, blurMapErr:%@"
+ "<%@: %p> lowLightEIT=%f, sifrMainEIT=%f, sifrGain=%f, lowLightHDRWithoutSIFR=%f, longWithoutSphere=%f, deepFusion=%f, rsmMainEIT=%f, rsmSIFRGain=%f, toneCurveBehavior=%d, preserveBlackLevel=%d, afWindows=%p, refMethod=%d, usePreviousSIFR=%d, motionAndFocusScoreWeights=%@, maxNumberOfFramesForAdaptiveBracketing=%d, dFlashAvailableEIT=%f, dFlashRecommendedEIT=%f, dFlashStationaryRecommendedEIT=%f, dFlashAvailableSNR=%f, dFlashAvailableSNRLag=%f, dFlashRecommendedSNR=%f, dFlashRecommendedSNRLag=%f, dFlashStationaryRecommendedSNR=%f, dFlashStationaryRecommendedSNRLag=%f, dFlashBacklitRecommendFlashSNR=%f, dFlashBacklitRecommendFlashSNRLag=%f, dFlashRecommendFlashSNR=%f, dFlashRecommendFlashSNRLag=%f, dFlashRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashAERelativeDiff=%f%@"
+ "<<< FigCaptureCustomExposureConfiguration >>> %s: deferring lock to unknown ISO limits for %@ (primary %@); available limits: %@"
+ "<<< FigCaptureCustomExposureConfiguration >>> %s: deferring lock to unknown current ISO"
+ "<<< FigCaptureCustomExposureConfiguration >>> %s: deferring lock to unknown current duration"
+ "<<< FigCaptureCustomFocusConfiguration >>> %s: [%@] Clamping focus position '%d' to '%d' using hyper focal focus postion '%d'"
+ "<<< FigVirtualCaptureCard >>> %s: Overhead preference is negative, returning -1"
+ "<<< FigVirtualCaptureCard >>> %s: calling get initial capacity overhead %lld"
+ "<<<< BWCameraStreamingMonitor >>>> %s: Added %{public}@ to activeClientSessions."
+ "<<<< BWCameraStreamingMonitor >>>> %s: Removed %{public}@ from activeClientSessions."
+ "<<<< BWCameraStreamingMonitor >>>> %s: Update clientInfo %{public}@ (PID %i) to clientInfo %{public}@ (PID %i)"
+ "<<<< BWCameraStreamingMonitor >>>> %s: activeClientSessions: %{public}@"
+ "<<<< BWCameraStreamingMonitor >>>> %s: clientSession %{public}@ running: %i, containsVideoSource: %i, cameraAccessGranted: %i, activePortTypes: %{public}@"
+ "<<<< BWCameraStreamingMonitor >>>> %s: clientSessionsBySessionID: %{public}@"
+ "<<<< BWE5InferenceProvider >>>> %s: e5rt_execution_stream_operation_retain_input_port failed to retain port with binding name %@ : %s"
+ "<<<< BWE5InferenceProvider >>>> %s: e5rt_execution_stream_operation_retain_output_port failed to retain port with binding name %@ : %s"
+ "<<<< BWE5InferenceProvider >>>> %s: e5rt_io_port_bind_surface_object failed on input port with binding name %@ : %s"
+ "<<<< BWE5InferenceProvider >>>> %s: e5rt_io_port_bind_surface_object failed on output port with binding name %@ : %s"
+ "<<<< BWE5InferenceProvider >>>> %s: e5rt_io_port_release failed to release input port %@ : %s"
+ "<<<< BWE5InferenceProvider >>>> %s: e5rt_io_port_release failed to release output port %@ : %s"
+ "<<<< BWEspressoInferenceAdapter >>>> %s: BWInferenceTypePersonSemantics missing inferenceInputAttachedMediaKey, cannot resolve inference input, err: %d"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Tagging asset bundle frame not used by this capture to be discarded (captureFlags:%{public}@): %{private}@"
+ "<<<< BWGraph >>>> %s: <%p[%{public}d][%{public}@]> All %lu source nodes had deferred start enabled. Falling back to non-deferred start for <%p, %@, %{public}@> and continuing."
+ "<<<< BWGraph >>>> %s: Parent of shared pool output should have a prepared pool: attachedMediaKey=%{public}@ sharedPoolOutput=%{public}@ parentOutput=%{public}@ parentAttachedMediaKey=%{public}@"
+ "<<<< BWInferenceFaceQualityCropDescriptor >>>> %s: Could not determine crop rect because HVS full input pixel buffer dimensions are missing on sample buffer metadata"
+ "<<<< BWInferenceFaceQualityCropDescriptor >>>> %s: Could not determine crop rect because sample buffer metadata is missing"
+ "<<<< BWInferenceFaceQualityCropDescriptor >>>> Fig"
+ "<<<< BWInferenceLazyVideoRequirement >>>> %s: attachedMediaKey='%@' preparedByKey='%@' inputFormat=%@"
+ "<<<< BWInferenceLazyVideoRequirement >>>> %s: resolved videoFormat=%@"
+ "<<<< BWInferenceSchedulerFramebufferBuilder >>>> %s: [%@] Available outputs to search: %lu total entries"
+ "<<<< BWInferenceSchedulerFramebufferBuilder >>>> %s: [%@] Disconnected input at media key '%@': %@"
+ "<<<< BWInferenceSchedulerFramebufferBuilder >>>> %s: [%@] REJECTED output candidate at media key '%@': %@ provider=%@ — upscale=%d invalidContentMismatch=%d contentModeExceeded=%d cropMismatch=%d"
+ "<<<< BWInferenceSchedulerFramebufferBuilder >>>> %s: [%@] Scaling node search result at media key '%@': closestOutput=%@ videoInput=%@"
+ "<<<< BWInferenceSchedulerFramebufferBuilder >>>> %s: [%@] Searching for output to derive desired input at media key '%@': %@"
+ "<<<< BWInferenceSchedulerFramebufferBuilder >>>> %s: [%@] _addScalingNodes iteration %lu: %lu disconnected inputs remaining, %lu outputs available"
+ "<<<< BWIrisMovieGenerator >>>> %s: %p: Disabled vitality for %@"
+ "<<<< BWIrisMovieGenerator >>>> %s: %p: Disabling vitality for captureID:%lld"
+ "<<<< BWMattingInferenceAdapter >>>> %s: %@ configuration missing inferenceInputAttachedMediaKey, cannot resolve inference input, err: %d"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Applied pending vitality disable for %@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Disabled vitality for firstIrisMovieInfo %@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Disabled vitality for pendingIrisRefMovieRequests %@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: Disabling vitality for captureID:%lld"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: deallocating with %lu unhandled pending vitality disabled settingsIDs: %@"
+ "<<<< BWQuickTimeMovieFileSinkNode >>>> %s: %p %@: settingsID:%lld not found in sink node yet, adding to pending vitality disabled list"
+ "<<<< BWRealtimeCinematographyNode >>>> %s: Engaging half rate preview thermal constraint due to high thermal pressure"
+ "<<<< BWRealtimeCinematographyNode >>>> %s: Releasing half rate preview thermal constraint due to nominal thermal pressure"
+ "<<<< BWRealtimeCinematographyNode >>>> %s: Thermal handler called with thermal level %@"
+ "<<<< BWSmartFramingSceneMonitor >>>> %s: TrackedSubject scores: groupID (%@), gazeScore (%f), significanceScore (%f), isSignificant (%d)"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: %@: downscaling %p from %zux%zu to %dx%d"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: %@: passthrough %p at %zux%zu (within standard resolution %dx%d)"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: %@: received %p %.4lf (%zux%zu)"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: %@: resolution resolved to %@ for key %@"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: BWSampleBufferSetAttachedMediaFromPixelBuffer failed (%d), sbuf = %@"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: BWSampleBufferSetAttachedMediaFromPixelBuffer failed with err = %d, sbuf = %@"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: BWStandardResolutionAttachmentNode: failed to attach standard resolution buffer (err %d), sbuf = %@"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: VTPixelTransferSessionCreate failed with err = %d"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: VTPixelTransferSessionTransferImage failed (%d), sbuf = %@"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: [%@] Received a node error (err: %d) with captureID:%lld"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: attachedMediaKey must not be nil"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: newPixelBuffer is nil, sbuf = %@"
+ "<<<< BWStandardResolutionAttachmentNode >>>> %s: sbuf's pixelbuffer is nil, sbuf = %@"
+ "<<<< BWStandardResolutionAttachmentNode >>>> Fig"
+ "<<<< BWStillImageFilterNode >>>> %s: Created new captureState for key:%@ (expectedSbufEmits:%ld, dict size:%lu)"
+ "<<<< BWStillImageFilterNode >>>> %s: Decrementing pending sbuf emits with note: %@ (captureState:%@)"
+ "<<<< BWStillImageFilterNode >>>> %s: Missing captureRequestIdentifier"
+ "<<<< BWStillImageFilterNode >>>> %s: Missing portType"
+ "<<<< BWStillImageFilterNode >>>> %s: Portrait effects rendering complete for: %@"
+ "<<<< BWStillImageFilterNode >>>> %s: SmartStyle rendering complete for: %@, portrait filters requested: %d"
+ "<<<< BWStillImageFilterNode >>>> %s: Two pass rendering complete for: %@"
+ "<<<< BWStillImageFilterNode >>>> %s: Using existing captureState for key:%@ (dict size:%lu)"
+ "<<<< BWStillImageFilterNode >>>> %s: captureState cleanup on error: dropped key:%@ (dict size:%lu)"
+ "<<<< BWStillImageFilterNode >>>> %s: captureState cleanup on error: missing captureRequestIdentifier (%@) or portType (%@); dumping all state defensively"
+ "<<<< BWStillImageFilterNode >>>> %s: captureState cleanup: nothing to sweep for key:%@ (dict size:%lu)"
+ "<<<< BWStillImageFilterNode >>>> %s: captureState cleanup: swept %lu consumed/unneeded keys:%@ (dict size:%lu)"
+ "<<<< BWStillImageFilterNode >>>> %s: commonEffectsSbuf is NULL after common effects processing"
+ "<<<< BWStillImageMetadataUtilities >>>> %s: Missing noise parameters: ReadNoise_1x=%@, ReadNoise_8x=%@, ConversionGain=%@, AGC=%@"
+ "<<<< BWStillImageMetadataUtilities >>>> %s: SushiRAW LSC GainMap failed to convert V3 LSC gain grid to V2 (err:%{public}d, AD:%{public}.1f microns)"
+ "<<<< BWStillImageProcessing >>>> %s: [%@] outputRectWithinSensorCropRect %@ is not CFA aligned"
+ "<<<< BWTemporalFilterNode >>>> %s: %@ %@ is EOD (configurationID: %@)"
+ "<<<< BWTemporalFilterNode >>>> %s: %{private}@ ConfigurationID %lld is now live for video input and output"
+ "<<<< BWTemporalFilterNode >>>> %s: MCTF session is nil after init attempt"
+ "<<<< BWTiledEspressoInferenceAdapter >>>> %s: BWInferenceTypeLearnedMatting missing inferenceInputAttachedMediaKey, cannot resolve inference input, err: %d"
+ "<<<< BWVisionInferenceAdapter >>>> %s: BWInferenceTypeLandmarks missing inferenceInputAttachedMediaKey, cannot resolve inference input, err: %d"
+ "<<<< BWVisionInferenceProvider >>>> %s: [%@] Forwarding face with bounding box extending outside the image to %{public}@: with boundingBox:%{public}@ (intersectsImage:%d) alignedBoundingBox:%{public}@ (isBoundingBoxAligned:%d, intersectsImage:%d) usedISPFaces:%d roll:%{public}@ exifOrientation:%d faceId:%lu captureID:%lld"
+ "<<<< FigCaptureDeferredProcessingEngine >>>> %s: %@ graph: cameraParametersCompatible:%d portTypesMatch:%d, pipelineParametersCompatible:%d, captureTypesMatch:%d, deferredPhotoFinalDimensionsCompatible:%d, containerAndGraphSourceNodeOutputDimensionsMatch:%d, demosaicedRawMatch:%d, demosaicedRawAllowsGraphReuse:%d, ultraHighResolutionCaptureAllowsGraphReuse:%d, enhancedResolutionAllowsGraphReuse:%d, stereoPhotoMatch:%d, depthDataMatch:%d, portraitRenderingCompatible:%d, backgroundQoSTransitionAllowsGraphReuse:%d"
+ "<<<< FigCaptureDeferredProcessingEngine >>>> %s: Not re-using graph:%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
+ "<<<< FigCaptureMetadataUtilities >>>> %s: textOrientationExtraRotationDegrees: %d must be a multiple of 90"
+ "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: failed to connect outputForInferenceNode to inferenceNode.input"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ Disabling vitality in movie file sink nodes for captureID:%lld"
+ "<<<< FigCaptureSession >>>> %s: %{public}@ New configuration (%lld) differs from live configuration (%lld) due to: %{public}@"
+ "<<<< FigCaptureSessionAttachedSessionManager >>>> %s: Error(%d) starting session: %{public}@"
+ "BWInferenceFaceQualityCropDescriptor.m"
+ "BWStandardResolutionAttachmentNode.m"
+ "BWStandardResolutionAttachmentNode: failed to attach standard resolution buffer (err %d), sbuf = %@"
+ "BackgroundBlurNode - Still Image CrossOver"
+ "BackgroundBlurNode - Still Image FanOut"
+ "CameraCapture Stills Core"
+ "Digital Flash Backlit Recommend Regular Flash - Scene ( Normalized QSum SNR )"
+ "Digital Flash Recommend Regular Flash - Scene ( Normalized QSum SNR )"
+ "DigitalFlashBacklitRecommendRegularFlash"
+ "DigitalFlashRecommendRegularFlash"
+ "FeaturesEnabled"
+ "FigCaptureSessionStartDetachedSession"
+ "InitialCapacityOverhead"
+ "Jul 11 2026"
+ "LastShownBuild:BWDeferredCaptureController.m:488"
+ "LastShownBuild:BWE5InferenceProvider.m:870"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:1577"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3031"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3082"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3668"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3681"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10367"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10877"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11328"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11363"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11552"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11561"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11573"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11580"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11614"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11680"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11849"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:12788"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:15806"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:18640"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:19028"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:1984"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:19873"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20295"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20297"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20299"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22193"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23584"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23616"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:23772"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24530"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24776"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25133"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:6009"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7689"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7698"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8777"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8778"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:8797"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9086"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9900"
+ "LastShownBuild:BWFigVideoCaptureStream.m:3198"
+ "LastShownBuild:BWFigVideoCaptureStream.m:3878"
+ "LastShownBuild:BWFigVideoCaptureStream.m:4298"
+ "LastShownBuild:BWGraph.m:2691"
+ "LastShownBuild:BWGraph.m:3617"
+ "LastShownBuild:BWGraph.m:3620"
+ "LastShownBuild:BWGraph.m:3623"
+ "LastShownBuild:BWIrisStagingNode.m:3884"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:13642"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:2725"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4419"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4426"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:4433"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:9399"
+ "LastShownBuild:BWNRFProcessorController.m:1681"
+ "LastShownBuild:BWNRFProcessorController.m:1682"
+ "LastShownBuild:BWNRFProcessorController.m:2090"
+ "LastShownBuild:BWOverCaptureSmartStyleApplyNode.m:442"
+ "LastShownBuild:BWPhotoEncoderController.m:1306"
+ "LastShownBuild:BWPhotoEncoderController.m:1309"
+ "LastShownBuild:BWPhotoEncoderController.m:1700"
+ "LastShownBuild:BWPhotoEncoderController.m:1705"
+ "LastShownBuild:BWPhotoEncoderController.m:1954"
+ "LastShownBuild:BWPhotoEncoderController.m:2093"
+ "LastShownBuild:BWPhotoEncoderController.m:2109"
+ "LastShownBuild:BWPhotoEncoderController.m:2119"
+ "LastShownBuild:BWPhotoEncoderController.m:3279"
+ "LastShownBuild:BWPhotoEncoderController.m:4664"
+ "LastShownBuild:BWPhotoEncoderController.m:6426"
+ "LastShownBuild:BWPhotoEncoderManager.m:623"
+ "LastShownBuild:BWPhotoEncoderNode.m:389"
+ "LastShownBuild:BWPhotonicEngineNode.m:3721"
+ "LastShownBuild:BWPhotonicEngineNode.m:3736"
+ "LastShownBuild:BWPhotonicEngineNode.m:3838"
+ "LastShownBuild:BWPhotonicEngineNode.m:3863"
+ "LastShownBuild:BWPhotonicEngineNode.m:4929"
+ "LastShownBuild:BWPhotonicEngineNode.m:5656"
+ "LastShownBuild:BWPhotonicEngineNode.m:5681"
+ "LastShownBuild:BWPhotonicEngineNode.m:7777"
+ "LastShownBuild:BWPhotonicEngineNode.m:7779"
+ "LastShownBuild:BWPhotonicEngineNode.m:9281"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2465"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3961"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:405"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:423"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4268"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4475"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4484"
+ "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4492"
+ "LastShownBuild:BWPixelBufferTransferRenderer.m:642"
+ "LastShownBuild:BWPreviewStitcherNode.m:3375"
+ "LastShownBuild:BWSmartStyleTargetRenderer.m:630"
+ "LastShownBuild:BWStandardResolutionAttachmentNode.m:131"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1221"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1225"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1431"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1438"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1508"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1611"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:1622"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:2248"
+ "LastShownBuild:BWStillImageCoordinatorNode.m:3739"
+ "LastShownBuild:BWStillImageFilterNode.m:1499"
+ "LastShownBuild:BWStillImageFilterNode.m:703"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1008"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:1066"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:126"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2195"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2202"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2208"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2231"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:2419"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:3031"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:3061"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:658"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:876"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:990"
+ "LastShownBuild:BWStillImageMetadataUtilities.m:996"
+ "LastShownBuild:BWTiledE5InferenceProvider.m:886"
+ "LastShownBuild:BWTiledE5InferenceProvider.m:919"
+ "LastShownBuild:BWUBCaptureParameters.m:242"
+ "LastShownBuild:BWUBCaptureParameters.m:245"
+ "LastShownBuild:BWUBCaptureParameters.m:250"
+ "LastShownBuild:BWUBCaptureParameters.m:313"
+ "LastShownBuild:CMCaptureLocalSessionController.m:888"
+ "LastShownBuild:FigCaptureDeferredPhotoProcessor.m:1429"
+ "LastShownBuild:FigCaptureDeferredPhotoProcessor.m:1450"
+ "LastShownBuild:FigCaptureDeferredPhotoProcessor.m:1519"
+ "LastShownBuild:FigCaptureDeferredProcessingEngine.m:1760"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1539"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:6245"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1618"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1625"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1629"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1776"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1782"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1785"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1932"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3017"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3137"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3499"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3503"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3548"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4573"
+ "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4579"
+ "LastShownBuild:FigCaptureSession.m:10027"
+ "LastShownBuild:FigCaptureSession.m:10230"
+ "LastShownBuild:FigCaptureSession.m:10960"
+ "LastShownBuild:FigCaptureSession.m:11155"
+ "LastShownBuild:FigCaptureSession.m:12067"
+ "LastShownBuild:FigCaptureSession.m:18692"
+ "LastShownBuild:FigCaptureSession.m:20210"
+ "LastShownBuild:FigCaptureSession.m:20213"
+ "LastShownBuild:FigCaptureSession.m:27530"
+ "LastShownBuild:FigCaptureSession.m:4424"
+ "LastShownBuild:FigCaptureSession.m:5069"
+ "LastShownBuild:FigCaptureSession.m:9028"
+ "LastShownBuild:FigCaptureSession.m:9034"
+ "LastShownBuild:FigCaptureSession.m:9037"
+ "LastShownBuild:FigCaptureSession.m:9040"
+ "LastShownBuild:FigCaptureSession.m:9043"
+ "LastShownBuild:FigCaptureSession.m:9054"
+ "LastShownBuild:FigCaptureSession.m:9057"
+ "LastShownBuild:FigCaptureSession.m:9065"
+ "LastShownBuild:FigCaptureSession.m:9083"
+ "LastShownBuild:FigCaptureSession.m:9128"
+ "LastShownBuild:FigCaptureSession.m:9132"
+ "LastShownBuild:FigCaptureSession.m:9156"
+ "LastShownBuild:FigCaptureSession.m:9171"
+ "LastShownBuild:FigCaptureSession.m:9175"
+ "LastShownBuild:FigCaptureSession.m:9178"
+ "LastShownBuild:FigCaptureSession.m:9302"
+ "LastShownBuild:FigCaptureSession.m:9308"
+ "LastShownBuild:FigCaptureSession.m:9334"
+ "LastShownBuild:FigCaptureSession.m:9346"
+ "LastShownBuild:FigCaptureSession.m:9744"
+ "LastShownBuild:FigCaptureSession.m:995"
+ "LastShownBuild:FigCaptureSessionStateManager.m:515"
+ "LastShownBuild:FigCaptureSourceBackingsProvider.m:2732"
+ "LastShownBuild:FigCaptureSourceRemote.m:195"
+ "LastShownBuild:FigCaptureSourceRemote.m:225"
+ "LastShownBuild:FigCaptureSourceServer.m:1847"
+ "LastShownBuild:FigCaptureSourceServer.m:1872"
+ "LastShownBuild:FigSampleBufferProcessor_Autofocus.m:931"
+ "LastShownDate:BWDeferredCaptureController.m:488"
+ "LastShownDate:BWE5InferenceProvider.m:870"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:1577"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3031"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3082"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3668"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3681"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10367"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10877"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11328"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11363"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11552"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11561"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11573"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11580"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11614"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11680"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11849"
+ "LastShownDate:BWFigVideoCaptureDevice.m:12788"
+ "LastShownDate:BWFigVideoCaptureDevice.m:15806"
+ "LastShownDate:BWFigVideoCaptureDevice.m:18640"
+ "LastShownDate:BWFigVideoCaptureDevice.m:19028"
+ "LastShownDate:BWFigVideoCaptureDevice.m:1984"
+ "LastShownDate:BWFigVideoCaptureDevice.m:19873"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20295"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20297"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20299"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22193"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23584"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23616"
+ "LastShownDate:BWFigVideoCaptureDevice.m:23772"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24530"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24776"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25133"
+ "LastShownDate:BWFigVideoCaptureDevice.m:6009"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7689"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7698"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8777"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8778"
+ "LastShownDate:BWFigVideoCaptureDevice.m:8797"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9086"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9900"
+ "LastShownDate:BWFigVideoCaptureStream.m:3198"
+ "LastShownDate:BWFigVideoCaptureStream.m:3878"
+ "LastShownDate:BWFigVideoCaptureStream.m:4298"
+ "LastShownDate:BWGraph.m:2691"
+ "LastShownDate:BWGraph.m:3617"
+ "LastShownDate:BWGraph.m:3620"
+ "LastShownDate:BWGraph.m:3623"
+ "LastShownDate:BWIrisStagingNode.m:3884"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:13642"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:2725"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4419"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4426"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:4433"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:9399"
+ "LastShownDate:BWNRFProcessorController.m:1681"
+ "LastShownDate:BWNRFProcessorController.m:1682"
+ "LastShownDate:BWNRFProcessorController.m:2090"
+ "LastShownDate:BWOverCaptureSmartStyleApplyNode.m:442"
+ "LastShownDate:BWPhotoEncoderController.m:1306"
+ "LastShownDate:BWPhotoEncoderController.m:1309"
+ "LastShownDate:BWPhotoEncoderController.m:1700"
+ "LastShownDate:BWPhotoEncoderController.m:1705"
+ "LastShownDate:BWPhotoEncoderController.m:1954"
+ "LastShownDate:BWPhotoEncoderController.m:2093"
+ "LastShownDate:BWPhotoEncoderController.m:2109"
+ "LastShownDate:BWPhotoEncoderController.m:2119"
+ "LastShownDate:BWPhotoEncoderController.m:3279"
+ "LastShownDate:BWPhotoEncoderController.m:4664"
+ "LastShownDate:BWPhotoEncoderController.m:6426"
+ "LastShownDate:BWPhotoEncoderManager.m:623"
+ "LastShownDate:BWPhotoEncoderNode.m:389"
+ "LastShownDate:BWPhotonicEngineNode.m:3721"
+ "LastShownDate:BWPhotonicEngineNode.m:3736"
+ "LastShownDate:BWPhotonicEngineNode.m:3838"
+ "LastShownDate:BWPhotonicEngineNode.m:3863"
+ "LastShownDate:BWPhotonicEngineNode.m:4929"
+ "LastShownDate:BWPhotonicEngineNode.m:5656"
+ "LastShownDate:BWPhotonicEngineNode.m:5681"
+ "LastShownDate:BWPhotonicEngineNode.m:7777"
+ "LastShownDate:BWPhotonicEngineNode.m:7779"
+ "LastShownDate:BWPhotonicEngineNode.m:9281"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2465"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3961"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:405"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:423"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4268"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4475"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4484"
+ "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4492"
+ "LastShownDate:BWPixelBufferTransferRenderer.m:642"
+ "LastShownDate:BWPreviewStitcherNode.m:3375"
+ "LastShownDate:BWSmartStyleTargetRenderer.m:630"
+ "LastShownDate:BWStandardResolutionAttachmentNode.m:131"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1221"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1225"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1431"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1438"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1508"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1611"
+ "LastShownDate:BWStillImageCoordinatorNode.m:1622"
+ "LastShownDate:BWStillImageCoordinatorNode.m:2248"
+ "LastShownDate:BWStillImageCoordinatorNode.m:3739"
+ "LastShownDate:BWStillImageFilterNode.m:1499"
+ "LastShownDate:BWStillImageFilterNode.m:703"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1008"
+ "LastShownDate:BWStillImageMetadataUtilities.m:1066"
+ "LastShownDate:BWStillImageMetadataUtilities.m:126"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2195"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2202"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2208"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2231"
+ "LastShownDate:BWStillImageMetadataUtilities.m:2419"
+ "LastShownDate:BWStillImageMetadataUtilities.m:3031"
+ "LastShownDate:BWStillImageMetadataUtilities.m:3061"
+ "LastShownDate:BWStillImageMetadataUtilities.m:658"
+ "LastShownDate:BWStillImageMetadataUtilities.m:876"
+ "LastShownDate:BWStillImageMetadataUtilities.m:990"
+ "LastShownDate:BWStillImageMetadataUtilities.m:996"
+ "LastShownDate:BWTiledE5InferenceProvider.m:886"
+ "LastShownDate:BWTiledE5InferenceProvider.m:919"
+ "LastShownDate:BWUBCaptureParameters.m:242"
+ "LastShownDate:BWUBCaptureParameters.m:245"
+ "LastShownDate:BWUBCaptureParameters.m:250"
+ "LastShownDate:BWUBCaptureParameters.m:313"
+ "LastShownDate:CMCaptureLocalSessionController.m:888"
+ "LastShownDate:FigCaptureDeferredPhotoProcessor.m:1429"
+ "LastShownDate:FigCaptureDeferredPhotoProcessor.m:1450"
+ "LastShownDate:FigCaptureDeferredPhotoProcessor.m:1519"
+ "LastShownDate:FigCaptureDeferredProcessingEngine.m:1760"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1539"
+ "LastShownDate:FigCaptureMetadataUtilities.m:6245"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1618"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1625"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1629"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1776"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1782"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1785"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1932"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3017"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3137"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3499"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3503"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3548"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4573"
+ "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4579"
+ "LastShownDate:FigCaptureSession.m:10027"
+ "LastShownDate:FigCaptureSession.m:10230"
+ "LastShownDate:FigCaptureSession.m:10960"
+ "LastShownDate:FigCaptureSession.m:11155"
+ "LastShownDate:FigCaptureSession.m:12067"
+ "LastShownDate:FigCaptureSession.m:18692"
+ "LastShownDate:FigCaptureSession.m:20210"
+ "LastShownDate:FigCaptureSession.m:20213"
+ "LastShownDate:FigCaptureSession.m:27530"
+ "LastShownDate:FigCaptureSession.m:4424"
+ "LastShownDate:FigCaptureSession.m:5069"
+ "LastShownDate:FigCaptureSession.m:9028"
+ "LastShownDate:FigCaptureSession.m:9034"
+ "LastShownDate:FigCaptureSession.m:9037"
+ "LastShownDate:FigCaptureSession.m:9040"
+ "LastShownDate:FigCaptureSession.m:9043"
+ "LastShownDate:FigCaptureSession.m:9054"
+ "LastShownDate:FigCaptureSession.m:9057"
+ "LastShownDate:FigCaptureSession.m:9065"
+ "LastShownDate:FigCaptureSession.m:9083"
+ "LastShownDate:FigCaptureSession.m:9128"
+ "LastShownDate:FigCaptureSession.m:9132"
+ "LastShownDate:FigCaptureSession.m:9156"
+ "LastShownDate:FigCaptureSession.m:9171"
+ "LastShownDate:FigCaptureSession.m:9175"
+ "LastShownDate:FigCaptureSession.m:9178"
+ "LastShownDate:FigCaptureSession.m:9302"
+ "LastShownDate:FigCaptureSession.m:9308"
+ "LastShownDate:FigCaptureSession.m:9334"
+ "LastShownDate:FigCaptureSession.m:9346"
+ "LastShownDate:FigCaptureSession.m:9744"
+ "LastShownDate:FigCaptureSession.m:995"
+ "LastShownDate:FigCaptureSessionStateManager.m:515"
+ "LastShownDate:FigCaptureSourceBackingsProvider.m:2732"
+ "LastShownDate:FigCaptureSourceRemote.m:195"
+ "LastShownDate:FigCaptureSourceRemote.m:225"
+ "LastShownDate:FigCaptureSourceServer.m:1847"
+ "LastShownDate:FigCaptureSourceServer.m:1872"
+ "LastShownDate:FigSampleBufferProcessor_Autofocus.m:931"
+ "Parent of shared pool output should have a prepared pool: attachedMediaKey=%{public}@ sharedPoolOutput=%{public}@ parentOutput=%{public}@ parentAttachedMediaKey=%{public}@"
+ "ProductID"
+ "StandardResolution-%@"
+ "StandardResolutionAttachment"
+ "SushiRAW LSC GainMap failed to convert V3 LSC gain grid to V2 (err:%{public}d, AD:%{public}.1f microns)"
+ "VendorID"
+ "[graph connectOutput:backgroundBlurNode.stillImageOutput toInput:backgroundBlurStillImageFanOut.input pipelineStage:((void *)0)]"
+ "[super addNode:backgroundBlurStillImageFanOut error:&error]"
+ "_FigIsNotCurrentDispatchQueue( _workerQueue )"
+ "bwinferencelazyvideoRequirement_trace"
+ "bwstandardresolutionattachmentnode_trace"
+ "com.apple.GenerativePlaygroundApp.remoteUIExtension"
+ "com.apple.coremedia.BWSmartCropNode.rtscInit"
+ "description=CameraCapture-761.0.0.0.3"
+ "downscaledPixelBuffer"
+ "outputAspectRatioOverride"
+ "primaryPixelBuffer"
+ "regionalbehaviors/shutter-relaxation-enabled"
+ "reportedError"
+ "simu_getNoiseProfileFromSensorParams"
+ "standardResAttachedMediaKey"
+ "ub.scene.digitalFlashBacklitRecommendRegularFlashSNR"
+ "ub.scene.digitalFlashRecommendRegularFlashSNR"
+ "v32@?0@\"NSString\"8@\"BWStillImageFilterNodeCaptureState\"16^B24"
+ "vcc_getInitialCapacityOverhead"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xd1\xf0\xf0q"
- "%@ %p: captureID:%lld '%.4s'('%.4s')%@ %dx%d R:%d%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
- "%@ %p: requestID:%d appliedFrameStatistics:%@"
- "%@ outputRectInBufferCoordinates %@ is not contained in valid-relative validBufferRect %@"
- "%@ outputRectWithinSensorCropRect %@ is not CFA aligned"
- "(*modified by nonDestructiveCrop)"
- "+[FigCaptureCustomWhiteBalanceConfiguration whiteBalanceConfigurationWithGainsByDeviceType:position:requestID:]"
- "-[BWCameraStreamingMonitor _getClientInfoForTCCIdentity:clientPID:sessionIsPrewarming:]"
- "-[BWCompressedShotBufferNode _compressionOptionsWithCropRect:pixelFormat:]"
- "-[BWFaceAndInstanceSegmentationConfiguration initWithInferenceType:]"
- "-[BWFigCaptureDevice _invalidateSyncStreamGroupsAndControlledStreams:preserveTorchState:]"
- "-[BWFigCaptureDevice invalidateAndKeepFigCaptureDeviceAlive:streamsToRelinquishControl:preserveTorchState:]"
- "-[BWFigCaptureDeviceVendor _invalidate:keepFigCaptureDeviceAlive:preserveTorchState:]"
- "-[BWFigCaptureStream synchronizedStreamsGroupDidStop]"
- "-[BWNRFProcessorController enqueueInputForProcessing:delegate:processErrorRecoveryFrame:processErrorRecoveryProxy:processOriginalImage:processLinearImage:processToneMapping:processInferenceInputImage:clientBracketSequenceNumber:processSemanticRendering:provideInferenceInputImageForProcessing:processSmartStyleRenderingInput:inferencesAvailable:]"
- "-[BWPhotoEncoderController _cropRectForRequestedSettings:inputDimensions:outputDimensions:metadata:processingFlags:]"
- "-[BWStillImageFilterNode _emitMergedSampleBufferIfReady]"
- "-[BWStillImageFilterNode _emitSampleBufferAsync:withNote:]"
- "-[BWStillImageFilterNode _emitSampleBufferAsync:withNote:]_block_invoke"
- "-[BWStillImageFilterNode _updateAndCachePortraitDataForBuffer:requestedSettings:]"
- "-[BWTemporalFilterNode didReachEndOfDataForInput:]"
- "-[BWTemporalFilterNode didReachEndOfDataForInput:]_block_invoke"
- "-[BWTemporalFilterNode prepareForCurrentConfigurationToBecomeLive]"
- "-[FigCaptureAncillaryDataHIDTransmitter openDeviceWithUsagePage:usage:error:]"
- "-[FigCapturePhotonicEngineSinkPipeline _addMattingInferenceToNode:mattingVersion:learnedMattingEnabled:learnedMattingVersion:mainImageDownscalingFactor:targetAspectRatio:appliesFinalCropRect:enabledSemantics:metalCommandQueue:mattingSensorConfigurationsByPortType:clientIsCameraOrDerivative:requiredAdditionalInferenceOutputBuffers:stillImageFusionScheme:]"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/Graph/Inference/Espresso/Configurations/BWFaceAndInstanceSegmentationConfiguration.m %s: Loading FSINC 2.3. VisionCoreAPI for loading FSINC 2.4 is not available in the build, please update the build on the device to 24A299 or later."
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSoftISPProcessorController.m"
- "12:39:45"
- "35d99764922290cd3282a716ac682c12522b2e4d"
- "7e7f14e1c034455198842478f21e7fa57b4fcd87"
- "<%@ %p>: captureID:%lld, captureType=%@, %@, errorRecovery=%d errorRecoveryProxy=%d original=%d linear=%d tonemap=%d inferenceInput=%d semanticRendering=%d inferenceInputForProcessing=%d inferences=%d input:<%@ %p>"
- "<%@: %p> lowLightEIT=%f, sifrMainEIT=%f, sifrGain=%f, lowLightHDRWithoutSIFR=%f, longWithoutSphere=%f, deepFusion=%f, rsmMainEIT=%f, rsmSIFRGain=%f, toneCurveBehavior=%d, preserveBlackLevel=%d, afWindows=%p, refMethod=%d, usePreviousSIFR=%d, motionAndFocusScoreWeights=%@, maxNumberOfFramesForAdaptiveBracketing=%d, dFlashAvailableEIT=%f, dFlashRecommendedEIT=%f, dFlashStationaryRecommendedEIT=%f, dFlashAvailableSNR=%f, dFlashAvailableSNRLag=%f, dFlashRecommendedSNR=%f, dFlashRecommendedSNRLag=%f, dFlashStationaryRecommendedSNR=%f, dFlashStationaryRecommendedSNRLag=%f, dFlashRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashSNR=%f, dFlashBacklitRecommendRegularFlashAERelativeDiff=%f%@"
- "<<< FigCaptureCustomExposureConfiguration >>> %s: Unexpected use of invalid min ISO: %@ applied to %@"
- "<<< FigCaptureCustomExposureConfiguration >>> Fig"
- "<<<< BWCameraStreamingMonitor >>>> %s: Added %@ to activeClientSessions."
- "<<<< BWCameraStreamingMonitor >>>> %s: Removed %@ from activeClientSessions."
- "<<<< BWCameraStreamingMonitor >>>> %s: activeClientSessions: %@"
- "<<<< BWCameraStreamingMonitor >>>> %s: clientSession %@ running: %i, containsVideoSource: %i, cameraAccessGranted: %i, activePortTypes: %@"
- "<<<< BWCameraStreamingMonitor >>>> %s: clientSessionsBySessionID: %@"
- "<<<< BWCameraStreamingMonitor >>>> %s: update clientInfo for PID %i. \noldClientInfo: %@ \nnewClientInfo: %@"
- "<<<< BWE5InferenceProvider >>>> %s: e5rt_execution_stream_operation_retain_input_port failed"
- "<<<< BWE5InferenceProvider >>>> %s: e5rt_execution_stream_operation_retain_output_port failed"
- "<<<< BWE5InferenceProvider >>>> %s: e5rt_io_port_release failed"
- "<<<< BWSmartFramingSceneMonitor >>>> %s: TrackedSubject scores: groupID (%@), gazeScore (%f), significanceScore (%f), isSignificant (%d), gazeScoreF (%f), significanceScoreF (%f), isSignificantF (%d)"
- "<<<< BWStillImageFilterNode >>>> %s: _commonEffectsSbuf is NULL after common effects processing"
- "<<<< BWStillImageProcessing >>>> %s: %@ outputRectInBufferCoordinates %@ is not contained in valid-relative validBufferRect %@"
- "<<<< BWStillImageProcessing >>>> %s: %@ outputRectWithinSensorCropRect %@ is not CFA aligned"
- "<<<< BWTemporalFilterNode >>>> %s: %@ %@ is EOD"
- "<<<< BWTemporalFilterNode >>>> %s: Attempted to create a new MCTF session before the last one is invalidated"
- "<<<< BWTemporalFilterNode >>>> %s: ConfigurationID %lld is now live for input %@"
- "<<<< BWTemporalFilterNode >>>> %s: MCTF session is nil"
- "<<<< FigCaptureDeferredProcessingEngine >>>> %s: %@ graph: cameraParametersCompatible:%d portTypesMatch:%d, pipelineParametersCompatible:%d, captureTypesMatch:%d, deferredPhotoFinalDimensionsCompatible:%d, containerAndGraphSourceNodeOutputDimensionsMatch:%d, demosaicedRawMatch:%d, demosaicedRawAllowsGraphReuse:%d, ultraHighResolutionCaptureAllowsGraphReuse:%d, enhancedResolutionAllowsGraphReuse:%d, stereoPhotoMatch:%d, depthDataMatch:%d, portraitRenderingCompatible:%d"
- "<<<< FigCaptureDeferredProcessingEngine >>>> %s: Not re-using graph:%@%@%@%@%@%@%@%@%@%@%@%@%@%@"
- "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %s: failed to connect inferenceRouterNode.outputs[inferenceRouterConfiguration.inferenceOuputIndex] to inferenceNode.input"
- "FigCaptureCustomExposureConfiguration.m"
- "Jul  2 2026"
- "LastShownBuild:BWDeferredCaptureController.m:468"
- "LastShownBuild:BWE5InferenceProvider.m:862"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:1564"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3018"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3069"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3654"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3667"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10323"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10833"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11284"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11319"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11508"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11517"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11529"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11536"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11570"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11636"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11805"
- "LastShownBuild:BWFigVideoCaptureDevice.m:12727"
- "LastShownBuild:BWFigVideoCaptureDevice.m:15744"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18576"
- "LastShownBuild:BWFigVideoCaptureDevice.m:18964"
- "LastShownBuild:BWFigVideoCaptureDevice.m:1960"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19771"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20193"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20195"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20197"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22094"
- "LastShownBuild:BWFigVideoCaptureDevice.m:23484"
- "LastShownBuild:BWFigVideoCaptureDevice.m:23516"
- "LastShownBuild:BWFigVideoCaptureDevice.m:23672"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24430"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24676"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25033"
- "LastShownBuild:BWFigVideoCaptureDevice.m:5970"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7647"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7656"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8733"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8734"
- "LastShownBuild:BWFigVideoCaptureDevice.m:8753"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9042"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9856"
- "LastShownBuild:BWFigVideoCaptureStream.m:3193"
- "LastShownBuild:BWFigVideoCaptureStream.m:3854"
- "LastShownBuild:BWFigVideoCaptureStream.m:4274"
- "LastShownBuild:BWGraph.m:3582"
- "LastShownBuild:BWGraph.m:3585"
- "LastShownBuild:BWGraph.m:3598"
- "LastShownBuild:BWIrisStagingNode.m:3867"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:13588"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:2717"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4399"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4406"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:4413"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:9368"
- "LastShownBuild:BWNRFProcessorController.m:1670"
- "LastShownBuild:BWNRFProcessorController.m:1671"
- "LastShownBuild:BWNRFProcessorController.m:2069"
- "LastShownBuild:BWOverCaptureSmartStyleApplyNode.m:420"
- "LastShownBuild:BWPhotoEncoderController.m:1308"
- "LastShownBuild:BWPhotoEncoderController.m:1311"
- "LastShownBuild:BWPhotoEncoderController.m:1697"
- "LastShownBuild:BWPhotoEncoderController.m:1702"
- "LastShownBuild:BWPhotoEncoderController.m:1955"
- "LastShownBuild:BWPhotoEncoderController.m:2094"
- "LastShownBuild:BWPhotoEncoderController.m:2110"
- "LastShownBuild:BWPhotoEncoderController.m:2120"
- "LastShownBuild:BWPhotoEncoderController.m:3278"
- "LastShownBuild:BWPhotoEncoderController.m:4666"
- "LastShownBuild:BWPhotoEncoderController.m:6395"
- "LastShownBuild:BWPhotoEncoderManager.m:656"
- "LastShownBuild:BWPhotoEncoderNode.m:393"
- "LastShownBuild:BWPhotonicEngineNode.m:3711"
- "LastShownBuild:BWPhotonicEngineNode.m:3726"
- "LastShownBuild:BWPhotonicEngineNode.m:3828"
- "LastShownBuild:BWPhotonicEngineNode.m:3853"
- "LastShownBuild:BWPhotonicEngineNode.m:4916"
- "LastShownBuild:BWPhotonicEngineNode.m:5643"
- "LastShownBuild:BWPhotonicEngineNode.m:5668"
- "LastShownBuild:BWPhotonicEngineNode.m:7752"
- "LastShownBuild:BWPhotonicEngineNode.m:7754"
- "LastShownBuild:BWPhotonicEngineNode.m:9256"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:2447"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:391"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:3943"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:409"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4250"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4453"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4462"
- "LastShownBuild:BWPhotonicEngineNodeResourceCoordinator.m:4470"
- "LastShownBuild:BWPixelBufferTransferRenderer.m:639"
- "LastShownBuild:BWPreviewStitcherNode.m:3318"
- "LastShownBuild:BWSmartStyleTargetRenderer.m:626"
- "LastShownBuild:BWSoftISPProcessorController.m:2844"
- "LastShownBuild:BWSoftISPProcessorController.m:2907"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1209"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1213"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1419"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1426"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1496"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1599"
- "LastShownBuild:BWStillImageCoordinatorNode.m:1610"
- "LastShownBuild:BWStillImageCoordinatorNode.m:2229"
- "LastShownBuild:BWStillImageCoordinatorNode.m:3713"
- "LastShownBuild:BWStillImageFilterNode.m:1264"
- "LastShownBuild:BWStillImageFilterNode.m:525"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1040"
- "LastShownBuild:BWStillImageMetadataUtilities.m:120"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1911"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1918"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1924"
- "LastShownBuild:BWStillImageMetadataUtilities.m:1947"
- "LastShownBuild:BWStillImageMetadataUtilities.m:2714"
- "LastShownBuild:BWStillImageMetadataUtilities.m:2744"
- "LastShownBuild:BWStillImageMetadataUtilities.m:652"
- "LastShownBuild:BWStillImageMetadataUtilities.m:786"
- "LastShownBuild:BWStillImageMetadataUtilities.m:965"
- "LastShownBuild:BWStillImageMetadataUtilities.m:971"
- "LastShownBuild:BWStillImageMetadataUtilities.m:983"
- "LastShownBuild:BWTiledE5InferenceProvider.m:870"
- "LastShownBuild:BWTiledE5InferenceProvider.m:903"
- "LastShownBuild:BWUBCaptureParameters.m:222"
- "LastShownBuild:BWUBCaptureParameters.m:228"
- "LastShownBuild:BWUBCaptureParameters.m:231"
- "LastShownBuild:BWUBCaptureParameters.m:299"
- "LastShownBuild:CMCaptureLocalSessionController.m:878"
- "LastShownBuild:FigCaptureDeferredPhotoProcessor.m:1428"
- "LastShownBuild:FigCaptureDeferredPhotoProcessor.m:1445"
- "LastShownBuild:FigCaptureDeferredPhotoProcessor.m:1518"
- "LastShownBuild:FigCaptureDeferredProcessingEngine.m:1757"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1533"
- "LastShownBuild:FigCaptureMetadataUtilities.m:6235"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1617"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1623"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1628"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1775"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1781"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1784"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:1948"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3018"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3139"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3482"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3486"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:3531"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4509"
- "LastShownBuild:FigCapturePhotonicEngineSinkPipeline.m:4515"
- "LastShownBuild:FigCaptureSession.m:10189"
- "LastShownBuild:FigCaptureSession.m:10919"
- "LastShownBuild:FigCaptureSession.m:11114"
- "LastShownBuild:FigCaptureSession.m:12026"
- "LastShownBuild:FigCaptureSession.m:18514"
- "LastShownBuild:FigCaptureSession.m:20016"
- "LastShownBuild:FigCaptureSession.m:20019"
- "LastShownBuild:FigCaptureSession.m:27262"
- "LastShownBuild:FigCaptureSession.m:4414"
- "LastShownBuild:FigCaptureSession.m:5059"
- "LastShownBuild:FigCaptureSession.m:8996"
- "LastShownBuild:FigCaptureSession.m:9002"
- "LastShownBuild:FigCaptureSession.m:9005"
- "LastShownBuild:FigCaptureSession.m:9008"
- "LastShownBuild:FigCaptureSession.m:9011"
- "LastShownBuild:FigCaptureSession.m:9022"
- "LastShownBuild:FigCaptureSession.m:9025"
- "LastShownBuild:FigCaptureSession.m:9033"
- "LastShownBuild:FigCaptureSession.m:9051"
- "LastShownBuild:FigCaptureSession.m:9096"
- "LastShownBuild:FigCaptureSession.m:9100"
- "LastShownBuild:FigCaptureSession.m:9124"
- "LastShownBuild:FigCaptureSession.m:9139"
- "LastShownBuild:FigCaptureSession.m:9143"
- "LastShownBuild:FigCaptureSession.m:9146"
- "LastShownBuild:FigCaptureSession.m:9269"
- "LastShownBuild:FigCaptureSession.m:9275"
- "LastShownBuild:FigCaptureSession.m:9301"
- "LastShownBuild:FigCaptureSession.m:9313"
- "LastShownBuild:FigCaptureSession.m:9711"
- "LastShownBuild:FigCaptureSession.m:992"
- "LastShownBuild:FigCaptureSession.m:9994"
- "LastShownBuild:FigCaptureSessionStateManager.m:511"
- "LastShownBuild:FigCaptureSourceBackingsProvider.m:2728"
- "LastShownBuild:FigCaptureSourceRemote.m:194"
- "LastShownBuild:FigCaptureSourceRemote.m:224"
- "LastShownBuild:FigCaptureSourceServer.m:1814"
- "LastShownBuild:FigCaptureSourceServer.m:1839"
- "LastShownBuild:FigSampleBufferProcessor_Autofocus.m:928"
- "LastShownDate:BWDeferredCaptureController.m:468"
- "LastShownDate:BWE5InferenceProvider.m:862"
- "LastShownDate:BWFigCaptureDeviceVendor.m:1564"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3018"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3069"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3654"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3667"
- "LastShownDate:BWFigVideoCaptureDevice.m:10323"
- "LastShownDate:BWFigVideoCaptureDevice.m:10833"
- "LastShownDate:BWFigVideoCaptureDevice.m:11284"
- "LastShownDate:BWFigVideoCaptureDevice.m:11319"
- "LastShownDate:BWFigVideoCaptureDevice.m:11508"
- "LastShownDate:BWFigVideoCaptureDevice.m:11517"
- "LastShownDate:BWFigVideoCaptureDevice.m:11529"
- "LastShownDate:BWFigVideoCaptureDevice.m:11536"
- "LastShownDate:BWFigVideoCaptureDevice.m:11570"
- "LastShownDate:BWFigVideoCaptureDevice.m:11636"
- "LastShownDate:BWFigVideoCaptureDevice.m:11805"
- "LastShownDate:BWFigVideoCaptureDevice.m:12727"
- "LastShownDate:BWFigVideoCaptureDevice.m:15744"
- "LastShownDate:BWFigVideoCaptureDevice.m:18576"
- "LastShownDate:BWFigVideoCaptureDevice.m:18964"
- "LastShownDate:BWFigVideoCaptureDevice.m:1960"
- "LastShownDate:BWFigVideoCaptureDevice.m:19771"
- "LastShownDate:BWFigVideoCaptureDevice.m:20193"
- "LastShownDate:BWFigVideoCaptureDevice.m:20195"
- "LastShownDate:BWFigVideoCaptureDevice.m:20197"
- "LastShownDate:BWFigVideoCaptureDevice.m:22094"
- "LastShownDate:BWFigVideoCaptureDevice.m:23484"
- "LastShownDate:BWFigVideoCaptureDevice.m:23516"
- "LastShownDate:BWFigVideoCaptureDevice.m:23672"
- "LastShownDate:BWFigVideoCaptureDevice.m:24430"
- "LastShownDate:BWFigVideoCaptureDevice.m:24676"
- "LastShownDate:BWFigVideoCaptureDevice.m:25033"
- "LastShownDate:BWFigVideoCaptureDevice.m:5970"
- "LastShownDate:BWFigVideoCaptureDevice.m:7647"
- "LastShownDate:BWFigVideoCaptureDevice.m:7656"
- "LastShownDate:BWFigVideoCaptureDevice.m:8733"
- "LastShownDate:BWFigVideoCaptureDevice.m:8734"
- "LastShownDate:BWFigVideoCaptureDevice.m:8753"
- "LastShownDate:BWFigVideoCaptureDevice.m:9042"
- "LastShownDate:BWFigVideoCaptureDevice.m:9856"
- "LastShownDate:BWFigVideoCaptureStream.m:3193"
- "LastShownDate:BWFigVideoCaptureStream.m:3854"
- "LastShownDate:BWFigVideoCaptureStream.m:4274"
- "LastShownDate:BWGraph.m:3582"
- "LastShownDate:BWGraph.m:3585"
- "LastShownDate:BWGraph.m:3598"
- "LastShownDate:BWIrisStagingNode.m:3867"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:13588"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:2717"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4399"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4406"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:4413"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:9368"
- "LastShownDate:BWNRFProcessorController.m:1670"
- "LastShownDate:BWNRFProcessorController.m:1671"
- "LastShownDate:BWNRFProcessorController.m:2069"
- "LastShownDate:BWOverCaptureSmartStyleApplyNode.m:420"
- "LastShownDate:BWPhotoEncoderController.m:1308"
- "LastShownDate:BWPhotoEncoderController.m:1311"
- "LastShownDate:BWPhotoEncoderController.m:1697"
- "LastShownDate:BWPhotoEncoderController.m:1702"
- "LastShownDate:BWPhotoEncoderController.m:1955"
- "LastShownDate:BWPhotoEncoderController.m:2094"
- "LastShownDate:BWPhotoEncoderController.m:2110"
- "LastShownDate:BWPhotoEncoderController.m:2120"
- "LastShownDate:BWPhotoEncoderController.m:3278"
- "LastShownDate:BWPhotoEncoderController.m:4666"
- "LastShownDate:BWPhotoEncoderController.m:6395"
- "LastShownDate:BWPhotoEncoderManager.m:656"
- "LastShownDate:BWPhotoEncoderNode.m:393"
- "LastShownDate:BWPhotonicEngineNode.m:3711"
- "LastShownDate:BWPhotonicEngineNode.m:3726"
- "LastShownDate:BWPhotonicEngineNode.m:3828"
- "LastShownDate:BWPhotonicEngineNode.m:3853"
- "LastShownDate:BWPhotonicEngineNode.m:4916"
- "LastShownDate:BWPhotonicEngineNode.m:5643"
- "LastShownDate:BWPhotonicEngineNode.m:5668"
- "LastShownDate:BWPhotonicEngineNode.m:7752"
- "LastShownDate:BWPhotonicEngineNode.m:7754"
- "LastShownDate:BWPhotonicEngineNode.m:9256"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:2447"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:391"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:3943"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:409"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4250"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4453"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4462"
- "LastShownDate:BWPhotonicEngineNodeResourceCoordinator.m:4470"
- "LastShownDate:BWPixelBufferTransferRenderer.m:639"
- "LastShownDate:BWPreviewStitcherNode.m:3318"
- "LastShownDate:BWSmartStyleTargetRenderer.m:626"
- "LastShownDate:BWSoftISPProcessorController.m:2844"
- "LastShownDate:BWSoftISPProcessorController.m:2907"
- "LastShownDate:BWStillImageCoordinatorNode.m:1209"
- "LastShownDate:BWStillImageCoordinatorNode.m:1213"
- "LastShownDate:BWStillImageCoordinatorNode.m:1419"
- "LastShownDate:BWStillImageCoordinatorNode.m:1426"
- "LastShownDate:BWStillImageCoordinatorNode.m:1496"
- "LastShownDate:BWStillImageCoordinatorNode.m:1599"
- "LastShownDate:BWStillImageCoordinatorNode.m:1610"
- "LastShownDate:BWStillImageCoordinatorNode.m:2229"
- "LastShownDate:BWStillImageCoordinatorNode.m:3713"
- "LastShownDate:BWStillImageFilterNode.m:1264"
- "LastShownDate:BWStillImageFilterNode.m:525"
- "LastShownDate:BWStillImageMetadataUtilities.m:1040"
- "LastShownDate:BWStillImageMetadataUtilities.m:120"
- "LastShownDate:BWStillImageMetadataUtilities.m:1911"
- "LastShownDate:BWStillImageMetadataUtilities.m:1918"
- "LastShownDate:BWStillImageMetadataUtilities.m:1924"
- "LastShownDate:BWStillImageMetadataUtilities.m:1947"
- "LastShownDate:BWStillImageMetadataUtilities.m:2714"
- "LastShownDate:BWStillImageMetadataUtilities.m:2744"
- "LastShownDate:BWStillImageMetadataUtilities.m:652"
- "LastShownDate:BWStillImageMetadataUtilities.m:786"
- "LastShownDate:BWStillImageMetadataUtilities.m:965"
- "LastShownDate:BWStillImageMetadataUtilities.m:971"
- "LastShownDate:BWStillImageMetadataUtilities.m:983"
- "LastShownDate:BWTiledE5InferenceProvider.m:870"
- "LastShownDate:BWTiledE5InferenceProvider.m:903"
- "LastShownDate:BWUBCaptureParameters.m:222"
- "LastShownDate:BWUBCaptureParameters.m:228"
- "LastShownDate:BWUBCaptureParameters.m:231"
- "LastShownDate:BWUBCaptureParameters.m:299"
- "LastShownDate:CMCaptureLocalSessionController.m:878"
- "LastShownDate:FigCaptureDeferredPhotoProcessor.m:1428"
- "LastShownDate:FigCaptureDeferredPhotoProcessor.m:1445"
- "LastShownDate:FigCaptureDeferredPhotoProcessor.m:1518"
- "LastShownDate:FigCaptureDeferredProcessingEngine.m:1757"
- "LastShownDate:FigCaptureMetadataUtilities.m:1533"
- "LastShownDate:FigCaptureMetadataUtilities.m:6235"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1617"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1623"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1628"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1775"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1781"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1784"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:1948"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3018"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3139"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3482"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3486"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:3531"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4509"
- "LastShownDate:FigCapturePhotonicEngineSinkPipeline.m:4515"
- "LastShownDate:FigCaptureSession.m:10189"
- "LastShownDate:FigCaptureSession.m:10919"
- "LastShownDate:FigCaptureSession.m:11114"
- "LastShownDate:FigCaptureSession.m:12026"
- "LastShownDate:FigCaptureSession.m:18514"
- "LastShownDate:FigCaptureSession.m:20016"
- "LastShownDate:FigCaptureSession.m:20019"
- "LastShownDate:FigCaptureSession.m:27262"
- "LastShownDate:FigCaptureSession.m:4414"
- "LastShownDate:FigCaptureSession.m:5059"
- "LastShownDate:FigCaptureSession.m:8996"
- "LastShownDate:FigCaptureSession.m:9002"
- "LastShownDate:FigCaptureSession.m:9005"
- "LastShownDate:FigCaptureSession.m:9008"
- "LastShownDate:FigCaptureSession.m:9011"
- "LastShownDate:FigCaptureSession.m:9022"
- "LastShownDate:FigCaptureSession.m:9025"
- "LastShownDate:FigCaptureSession.m:9033"
- "LastShownDate:FigCaptureSession.m:9051"
- "LastShownDate:FigCaptureSession.m:9096"
- "LastShownDate:FigCaptureSession.m:9100"
- "LastShownDate:FigCaptureSession.m:9124"
- "LastShownDate:FigCaptureSession.m:9139"
- "LastShownDate:FigCaptureSession.m:9143"
- "LastShownDate:FigCaptureSession.m:9146"
- "LastShownDate:FigCaptureSession.m:9269"
- "LastShownDate:FigCaptureSession.m:9275"
- "LastShownDate:FigCaptureSession.m:9301"
- "LastShownDate:FigCaptureSession.m:9313"
- "LastShownDate:FigCaptureSession.m:9711"
- "LastShownDate:FigCaptureSession.m:992"
- "LastShownDate:FigCaptureSession.m:9994"
- "LastShownDate:FigCaptureSessionStateManager.m:511"
- "LastShownDate:FigCaptureSourceBackingsProvider.m:2728"
- "LastShownDate:FigCaptureSourceRemote.m:194"
- "LastShownDate:FigCaptureSourceRemote.m:224"
- "LastShownDate:FigCaptureSourceServer.m:1814"
- "LastShownDate:FigCaptureSourceServer.m:1839"
- "LastShownDate:FigSampleBufferProcessor_Autofocus.m:928"
- "description=CameraCapture-758.0.0.122.2"
- "primaryCameraStats.baseISO > 0.f"
- "primaryCameraStats.integrationTime > 0.f"
- "sourceNodesCount > _deferredStartSourceNodes.count"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb1\xf0\xf0Q"
```
