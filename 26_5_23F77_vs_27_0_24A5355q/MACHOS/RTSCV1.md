## RTSCV1

> `/System/Library/VideoProcessors/RTSCV1.bundle/RTSCV1`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0xd6ec
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_stubs: 0x1520
-  __TEXT.__objc_methlist: 0xde8
-  __TEXT.__const: 0x2d8
-  __TEXT.__cstring: 0x6ff
-  __TEXT.__objc_methname: 0x2b78
-  __TEXT.__objc_classname: 0x2a3
-  __TEXT.__objc_methtype: 0x11c5
-  __TEXT.__gcc_except_tab: 0x31c
-  __TEXT.__unwind_info: 0x3f0
-  __DATA_CONST.__auth_got: 0x328
-  __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__cfstring: 0x140
-  __DATA_CONST.__objc_classlist: 0x78
+748.0.0.122.2
+  __TEXT.__text: 0x15c48
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_stubs: 0x16e0
+  __TEXT.__objc_methlist: 0xf34
+  __TEXT.__const: 0x320
+  __TEXT.__cstring: 0x1cd5
+  __TEXT.__oslogstring: 0x2a2b
+  __TEXT.__objc_methname: 0x30fd
+  __TEXT.__objc_classname: 0x1c1
+  __TEXT.__objc_methtype: 0x1588
+  __TEXT.__gcc_except_tab: 0x664
+  __TEXT.__unwind_info: 0x4c0
+  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x25c0
-  __DATA.__objc_selrefs: 0x7d8
-  __DATA.__objc_ivar: 0x294
-  __DATA.__objc_data: 0x4b0
+  __DATA_CONST.__auth_got: 0x368
+  __DATA_CONST.__got: 0x198
+  __DATA_CONST.__auth_ptr: 0x8
+  __DATA.__objc_const: 0x2948
+  __DATA.__objc_selrefs: 0x878
+  __DATA.__objc_ivar: 0x2dc
+  __DATA.__objc_data: 0x500
   __DATA.__data: 0x180
   __DATA.__bss: 0xc
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 753C62D0-DA11-3C74-A21B-6F93897E1083
-  Functions: 319
-  Symbols:   966
-  CStrings:  708
+  UUID: 044100F0-2AED-3E5D-8B4F-B99C1A809AB9
+  Functions: 350
+  Symbols:   1057
+  CStrings:  973
 
Symbols:
+ -[RTSCFaceReframer .cxx_destruct]
+ -[RTSCFaceReframer _applyRotationAdjustmentsToReframingCorrection:stabilizationMetadata:cameraMetadata:]
+ -[RTSCFaceReframer _clampRotationCorrection:shiftCorrection:ToBoundingCorners:boundingEllipse:currentBoundingMargin:cameraMetadata:]
+ -[RTSCFaceReframer _computeFaceReframingRotationForMetadataDict:cameraMetadata:stabilizationMetadata:]
+ -[RTSCFaceReframer _computeHomographyForFramingCorrection:shiftCorrection:cameraMetadata:]
+ -[RTSCFaceReframer _computeHomographyFromRotation:focalLength:inputOpticalCenter:outputOpticalCenter:]
+ -[RTSCFaceReframer _extractCameraMetadata:fromMetadataDictionary:calibrationDictionary:]
+ -[RTSCFaceReframer _extractCameraMetadata:fromMetadataDictionary:calibrationDictionary:].cold.1
+ -[RTSCFaceReframer _extractCameraMetadata:fromMetadataDictionary:calibrationDictionary:].cold.2
+ -[RTSCFaceReframer _extractCameraMetadata:fromMetadataDictionary:calibrationDictionary:].cold.3
+ -[RTSCFaceReframer _findInterpolatedRotationCorrection:shiftCorrection:withinBoundingCorners:boundingEllipse:correctionBoundsMargin:cameraMetadata:]
+ -[RTSCFaceReframer _setDefaultParameters]
+ -[RTSCFaceReframer _updatePerturbationStatesWithTimestamp:]
+ -[RTSCFaceReframer dealloc]
+ -[RTSCFaceReframer faceReframingStrength]
+ -[RTSCFaceReframer framingHomography]
+ -[RTSCFaceReframer init]
+ -[RTSCFaceReframer nominalFaceFramingOffset]
+ -[RTSCFaceReframer reservedOverscan]
+ -[RTSCFaceReframer setFaceReframingStrength:]
+ -[RTSCFaceReframer setReservedOverscan:]
+ -[RTSCFaceReframer updateFramingHomographyUsingMetadata:inputCalibration:pixelBufferDimensions:outputFOVRect:stabilizationMetadata:]
+ -[RTSCFaceReframer updateFramingHomographyUsingMetadata:inputCalibration:pixelBufferDimensions:outputFOVRect:stabilizationMetadata:].cold.1
+ -[RTSCProcessorV1 faceReframingEnabled]
+ -[RTSCProcessorV1 outputRotation]
+ -[RTSCProcessorV1 renderingEnabled]
+ -[RTSCProcessorV1 setFaceReframingEnabled:]
+ -[RTSCProcessorV1 setRenderingEnabled:]
+ -[RTSCRealTimeStabilization _getCalibrationDataFromDictionary:cameraMetadata:].cold.1
+ -[RTSCRealTimeStabilization _getCalibrationDataFromDictionary:cameraMetadata:].cold.2
+ -[RTSCRealTimeStabilization _getCalibrationDataFromDictionary:cameraMetadata:].cold.3
+ -[RTSCRealTimeStabilization _updateRollingShutterModelWithMotionSample:cameraMetadata:hallPositionIndex:atTime:]
+ -[RTSCRealTimeStabilization _updateRollingShutterModelWithMotionSample:cameraMetadata:hallPositionIndex:atTime:].cold.1
+ -[RTSCRealTimeStabilization boundsClampingDisabled]
+ -[RTSCRealTimeStabilization initWithCameraExtrinsics:]
+ -[RTSCRealTimeStabilization motionBlurShimmerMitigationDisabled]
+ -[RTSCRealTimeStabilization setBoundsClampingDisabled:]
+ -[RTSCRealTimeStabilization setMotionBlurShimmerMitigationDisabled:]
+ -[RTSCRealTimeStabilization stabilizationMetadata]
+ -[RTSCRealTimeStabilization stabilizationRotation]
+ FigMotionComputeLensMovementAndSagForTimeStamp.cold.2
+ GCC_except_table14
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table36
+ GCC_except_table4
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table7
+ GCC_except_table8
+ OBJC_IVAR_$_RTSCFaceReframer._bufferHeight
+ OBJC_IVAR_$_RTSCFaceReframer._bufferWidth
+ OBJC_IVAR_$_RTSCFaceReframer._faceReframing
+ OBJC_IVAR_$_RTSCFaceReframer._framingHomography
+ OBJC_IVAR_$_RTSCFaceReframer._imageCenter
+ OBJC_IVAR_$_RTSCFaceReframer._isFirstFrame
+ OBJC_IVAR_$_RTSCFaceReframer._motionBlurFilter
+ OBJC_IVAR_$_RTSCFaceReframer._outputCropRect
+ OBJC_IVAR_$_RTSCFaceReframer._outputRotationPerturbation
+ OBJC_IVAR_$_RTSCFaceReframer._outputShiftPerturbation
+ OBJC_IVAR_$_RTSCFaceReframer._overscanReserveAngle
+ OBJC_IVAR_$_RTSCFaceReframer._prevInputPose
+ OBJC_IVAR_$_RTSCFaceReframer._prevOutputPose
+ OBJC_IVAR_$_RTSCFaceReframer._prevTimestamp
+ OBJC_IVAR_$_RTSCFaceReframer._reframingCorrection
+ OBJC_IVAR_$_RTSCProcessorV1._faceReframer
+ OBJC_IVAR_$_RTSCProcessorV1._faceReframingEnabled
+ OBJC_IVAR_$_RTSCProcessorV1._fallbackSuggestionFOV
+ OBJC_IVAR_$_RTSCProcessorV1._renderingEnabled
+ OBJC_IVAR_$_RTSCRealTimeStabilization._boundsClampingDisabled
+ OBJC_IVAR_$_RTSCRealTimeStabilization._motionBlurShimmerMitigationDisabled
+ OBJC_IVAR_$_RTSCRealTimeStabilization._rotationCorrection
+ OBJC_IVAR_$_RTSCRealTimeStabilization._shiftCorrection
+ OBJC_IVAR_$_RTSCRealTimeStabilization._stabilizationMetadata
+ _FigMotionInitializeQuaternion
+ _FigSignalErrorAt3
+ _OBJC_CLASS_$_RTSCFaceReframer
+ _OBJC_METACLASS_$_RTSCFaceReframer
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_37
+ _RTSCFaceReframerTrace
+ _RTSCFaceReframingUtilitiesTrace
+ _RTSCRealTimeStabilizationTrace
+ _RTSCTrace
+ __OBJC_$_INSTANCE_METHODS_RTSCFaceReframer
+ __OBJC_$_INSTANCE_VARIABLES_RTSCFaceReframer
+ __OBJC_$_PROP_LIST_RTSCFaceReframer
+ __OBJC_CLASS_RO_$_RTSCFaceReframer
+ __OBJC_METACLASS_RO_$_RTSCFaceReframer
+ __ZL20_simd_slerp_internal10simd_quatfS_f
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _fr_computeBoundingMarginsForHomography
+ _hallPositionIndexFromPortType
+ _kIdentityQuaternion
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_applyRotationAdjustmentsToReframingCorrection:stabilizationMetadata:cameraMetadata:
+ _objc_msgSend$_clampRotationCorrection:shiftCorrection:ToBoundingCorners:boundingEllipse:currentBoundingMargin:cameraMetadata:
+ _objc_msgSend$_computeFaceReframingRotationForMetadataDict:cameraMetadata:stabilizationMetadata:
+ _objc_msgSend$_computeHomographyForFramingCorrection:shiftCorrection:cameraMetadata:
+ _objc_msgSend$_extractCameraMetadata:fromMetadataDictionary:calibrationDictionary:
+ _objc_msgSend$_findInterpolatedRotationCorrection:shiftCorrection:withinBoundingCorners:boundingEllipse:correctionBoundsMargin:cameraMetadata:
+ _objc_msgSend$_setDefaultParameters
+ _objc_msgSend$_updatePerturbationStatesWithTimestamp:
+ _objc_msgSend$_updateRollingShutterModelWithMotionSample:cameraMetadata:hallPositionIndex:atTime:
+ _objc_msgSend$framingHomography
+ _objc_msgSend$initWithCameraExtrinsics:
+ _objc_msgSend$setBoundsClampingDisabled:
+ _objc_msgSend$setMotionBlurShimmerMitigationDisabled:
+ _objc_msgSend$setReservedOverscan:
+ _objc_msgSend$stabilizationMetadata
+ _objc_msgSend$stabilizationRotation
+ _objc_msgSend$updateFramingHomographyUsingMetadata:inputCalibration:pixelBufferDimensions:outputFOVRect:stabilizationMetadata:
+ _objc_retain_x3
+ _objc_retain_x8
+ _os_log_type_enabled
- -[RTSCMotionBlurFilter prevSamplingRate]
- -[RTSCProcessorV1 _processPreview].cold.2
- -[RTSCProcessorV1 _processPreview].cold.3
- -[RTSCProcessorV1 _processPreview].cold.4
- -[RTSCProcessorV1 _processPreview].cold.5
- -[RTSCProcessorV1 _processPreview].cold.6
- -[RTSCProcessorV1 _processPreview].cold.7
- -[RTSCProcessorV1 _processStill].cold.1
- -[RTSCProcessorV1 _processVideo].cold.1
- -[RTSCProcessorV1 _processVideo].cold.2
- -[RTSCProcessorV1 _processVideo].cold.3
- -[RTSCProcessorV1 _processVideo].cold.4
- -[RTSCProcessorV1 _processVideo].cold.5
- -[RTSCProcessorV1 _processVideo].cold.6
- -[RTSCProcessorV1 enableFaceReframing]
- -[RTSCProcessorV1 prewarm].cold.1
- -[RTSCProcessorV1 process].cold.1
- -[RTSCProcessorV1 process].cold.2
- -[RTSCProcessorV1 process].cold.3
- -[RTSCProcessorV1 setEnableFaceReframing:]
- -[RTSCProcessorV1 setup].cold.1
- -[RTSCProcessorV1 setup].cold.2
- -[RTSCRealTimeStabilization _extractMetadataAndMotionDataFromDictionary:calibration:cameraMetadata:cameraPose:oisOffset:sagOffset:].cold.10
- -[RTSCRealTimeStabilization _updateRollingShutterModelWithMotionSample:cameraMetadata:currentPort:atTime:]
- -[RTSCRealTimeStabilization _updateRollingShutterModelWithMotionSample:cameraMetadata:currentPort:atTime:].cold.1
- -[RTSCRealTimeStabilization faceReframingStrength]
- -[RTSCRealTimeStabilization initWithCameraExtrinsics:faceReframingSettings:]
- -[RTSCRealTimeStabilization nominalFaceFramingOffset]
- -[RTSCRealTimeStabilization setFaceReframingStrength:]
- -[RTSCRealTimeStabilization updateStabilizationHomographyUsingMetadata:inputCalibration:pixelBufferDimensions:outputFOVRect:].cold.2
- GCC_except_table26
- GCC_except_table33
- GCC_except_table38
- GCC_except_table41
- OBJC_IVAR_$_RTSCMotionBlurFilter._prevSamplingRate
- OBJC_IVAR_$_RTSCProcessorV1._enableFaceReframing
- OBJC_IVAR_$_RTSCRealTimeStabilization._faceReframing
- OBJC_IVAR_$_RTSCRealTimeStabilization._overscanReserveAngle
- OBJC_IVAR_$_RTSCRealTimeStabilization._prevCameraPose
- OBJC_IVAR_$_RTSCRealTimeStabilization._stabilizationCorrection
- _FigSignalErrorAtGM
- _kFigCapturePortType_BackFacingSparseTimeOfFlightCamera
- _kFigCapturePortType_BackFacingSuperWideCamera
- _kFigCapturePortType_FrontFacingCamera
- _kFigCapturePortType_FrontFacingInfraredCamera
- _kFigCapturePortType_FrontFacingSuperWideCamera
- _objc_msgSend$_updateRollingShutterModelWithMotionSample:cameraMetadata:currentPort:atTime:
- _objc_msgSend$faceCorrection
- _objc_msgSend$initWithCameraExtrinsics:faceReframingSettings:
- _portIndexFromPortType
- portIndexFromPortType.cold.1
- portIndexFromPortType.cold.2
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "-[RTSCAdaptiveFilterStrength initWithMaxTimescale:minTimescale:transitionTime:]"
+ "-[RTSCAutocovarianceDynamicsAnalyzer4DOF initWithTimeConstant:initialCovariance:]"
+ "-[RTSCFaceReframer _extractCameraMetadata:fromMetadataDictionary:calibrationDictionary:]"
+ "-[RTSCFaceReframer _findInterpolatedRotationCorrection:shiftCorrection:withinBoundingCorners:boundingEllipse:correctionBoundsMargin:cameraMetadata:]"
+ "-[RTSCFaceReframer _updatePerturbationStatesWithTimestamp:]"
+ "-[RTSCFaceReframer init]"
+ "-[RTSCFaceReframer updateFramingHomographyUsingMetadata:inputCalibration:pixelBufferDimensions:outputFOVRect:stabilizationMetadata:]"
+ "-[RTSCFaceReframingV1 _computeViewPortSmoothingTimescaleForViewPortMargins:predictedViewPortMargins:centeredViewPortMargins:faceBoxSize:]"
+ "-[RTSCFaceReframingV1 _updateOffsetOfViewPortBox:withinBoundingRect:]"
+ "-[RTSCFaceReframingV1 init]"
+ "-[RTSCFaceTrackerV2 _getFaceOrientationInDictionary:asQuaternion:]"
+ "-[RTSCFaceTrackerV2 initWithTimeConstant:]"
+ "-[RTSCFaceTrackerV2 trackFaceBoxesWithDetectedObjects:atTime:bufferSize:changeFromPrevFrame:]"
+ "-[RTSCKalmanFilter4DOF init]"
+ "-[RTSCProcessorV1 _bindCVPixleBuffer:usage:]"
+ "-[RTSCProcessorV1 _cachedTextureFromPixelBuffer:usage:]"
+ "-[RTSCProcessorV1 _confineCropRectToValidImageCircle:]"
+ "-[RTSCProcessorV1 _createRenderTargetForOutputTex:renderTargetTex:]"
+ "-[RTSCProcessorV1 _encodeRenderTargetResolve:renderTargetTex:outputTex:]"
+ "-[RTSCProcessorV1 _extractFinalCropRect]"
+ "-[RTSCProcessorV1 _processPreview]"
+ "-[RTSCProcessorV1 _processStill]"
+ "-[RTSCProcessorV1 _processVideo]"
+ "-[RTSCProcessorV1 _render]"
+ "-[RTSCProcessorV1 _updateInputCameraCalibration]"
+ "-[RTSCProcessorV1 _updateOutputFOV]"
+ "-[RTSCProcessorV1 _updateTransformAndMetadataForPreview]"
+ "-[RTSCProcessorV1 prepareToProcess:]"
+ "-[RTSCProcessorV1 prewarm]"
+ "-[RTSCProcessorV1 process]"
+ "-[RTSCProcessorV1 setMetalCommandQueue:]"
+ "-[RTSCProcessorV1 setOutputFOVPreset:]"
+ "-[RTSCProcessorV1 setOutputROI:]"
+ "-[RTSCProcessorV1 setup]"
+ "-[RTSCRealTimeStabilization _clampStabilizedCamera:ToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:]"
+ "-[RTSCRealTimeStabilization _computeClampedRollingShutterTransformForBoundingRect:]"
+ "-[RTSCRealTimeStabilization _extractMetadataAndMotionDataFromDictionary:calibration:cameraMetadata:cameraPose:oisOffset:sagOffset:]"
+ "-[RTSCRealTimeStabilization _findCameraModelWithinBoundingCorners:boundingEllipse:outsideBoundsModel:insideBoundsModel:outsideBoundsMargin:insideBoundsMargin:inputPose:oisOffset:cameraMetadata:]"
+ "-[RTSCRealTimeStabilization _getAllMetadataFromDictionary:cameraMetadata:]"
+ "-[RTSCRealTimeStabilization _getCalibrationDataFromDictionary:cameraMetadata:]"
+ "-[RTSCRealTimeStabilization initWithCameraExtrinsics:]"
+ "-[RTSCRealTimeStabilization updateStabilizationHomographyUsingMetadata:inputCalibration:pixelBufferDimensions:outputFOVRect:]"
+ "-[RTSCRollingShutterModel updateModelAtRow:withPose:principalPoint:]"
+ "-[RTSCShadersV1 initWithContext:]"
+ "-[RTSCSpringAnimation updateToTime:]"
+ "-[RTSCSpringAnimation(Presets) configureWithPreset:]"
+ "-[RTSCTuningParametersV1 initWithDictionary:]"
+ "-[RTSCTuningParametersV1 init]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on hallPositionIndex %d"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCAutocovarianceDynamicsAnalyzer4DOF.m %s: Failed to initialize"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCKalmanFilter4DOF.m %s: Filter is nil"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: Reference camera is not valid"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: maxTimescale is less than minTimescale. Forcing maxTimescale = minTimescale"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: minTimescale and transitionTime must be greater than zero"
+ "<<<< RTSCFaceFramingUtilities >>>> %s: %@ is missing for face detection"
+ "<<<< RTSCFaceFramingUtilities >>>> %s: Failed to initialize"
+ "<<<< RTSCFaceFramingUtilities >>>> %s: Failed to initialized covarianceEstimator"
+ "<<<< RTSCFaceFramingUtilities >>>> %s: Roll/Pitch/Yaw is missing for face detection"
+ "<<<< RTSCFaceFramingUtilities >>>> %s: ViewPortMargin: [%f,%f,%f,%f]"
+ "<<<< RTSCFaceFramingUtilities >>>> %s: finalTrackingTimescale: [%f,%f] \ttargetTrackingTimescale: [%f,%f] \tmaxTrackingTimescale: [%f,%f]"
+ "<<<< RTSCFaceReframer >>>>"
+ "<<<< RTSCFaceReframer >>>> %s: Converged after %d iterations. Final margin: %e"
+ "<<<< RTSCFaceReframer >>>> %s: Failed extracting metadata"
+ "<<<< RTSCFaceReframer >>>> %s: Failed to converge. Final margin: %f"
+ "<<<< RTSCFaceReframer >>>> %s: Failed to get ImageCircle Center"
+ "<<<< RTSCFaceReframer >>>> %s: Failed to get ImageCircle Radius"
+ "<<<< RTSCFaceReframer >>>> %s: Failed to initialize"
+ "<<<< RTSCFaceReframer >>>> %s: Image circle radius is different in width (%f) and height (%f)"
+ "<<<< RTSCFaceReframer >>>> %s: Image circle radius is near or less than zero: %f"
+ "<<<< RTSCFaceReframer >>>> %s: Intrinsic matrix missing from calibration data"
+ "<<<< RTSCFaceReframer >>>> %s: Minimum transform is out of bounds! Unable to clamp"
+ "<<<< RTSCFaceReframer >>>> %s: Transform margins: [(%f,%f,%f),(%f,%f,%f),(%f,%f,%f),(%f,%f,%f)]"
+ "<<<< RTSCFaceReframer >>>> %s: new timestamp is less then previous timestamp. Skipping update"
+ "<<<< RTSCFaceReframer >>>> Fig"
+ "<<<< RTSCProcessorV1 >>>> %s: Client specified FOV of %.2f is invalid, using max output FOV instead ( %2.f )"
+ "<<<< RTSCProcessorV1 >>>> %s: Client specified FOV of %.2f is not feasible, clamping to max output FOV ( %2.f )"
+ "<<<< RTSCProcessorV1 >>>> %s: Command queue already created, metalCommandQueue should be set before -setup"
+ "<<<< RTSCProcessorV1 >>>> %s: Face Reframing FOV in tuning ( %.2f ) is not feasible, clamping to max output FOV ( %.2f )"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to allocate intermediate texture for AA resolve"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to allocate render target texture"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to bind input pixel buffer as texture"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to bind output pixel buffer as texture"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to bind pixel buffer %p to texture"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to create metal allocator for RTSCProcessor"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to create metal context for RTSCProcessor"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to encode downsample for AA resolve"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to encode render"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to get image circle center"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to get image circle radius"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to load kernel RTSC::Downsample"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to load kernel RTSC::Render"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to load kernel RTSC::ReplaceRegion"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to load shaders required by RTSCProcessor"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to load tuning parameters"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to update current and candidate framing crop rects"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to update for preview"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to update input camera calibration"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to update output FOV crop"
+ "<<<< RTSCProcessorV1 >>>> %s: Failed to update stabilization"
+ "<<<< RTSCProcessorV1 >>>> %s: Intrinsic matrix missing from calibration data"
+ "<<<< RTSCProcessorV1 >>>> %s: Intrinsic matrix reference dimensions is missing from calibration data"
+ "<<<< RTSCProcessorV1 >>>> %s: Invalid processing type for RTSCProcessor"
+ "<<<< RTSCProcessorV1 >>>> %s: Natural FOV in tuning ( %.2f ) is not feasible, clamping to max output FOV ( %.2f )"
+ "<<<< RTSCProcessorV1 >>>> %s: Pixel buffer %c%c%c%c format not supported"
+ "<<<< RTSCProcessorV1 >>>> %s: Pixel size is missing from calibration data"
+ "<<<< RTSCProcessorV1 >>>> %s: Pixel size value is invalid"
+ "<<<< RTSCProcessorV1 >>>> %s: RTSCProcessor failed to render."
+ "<<<< RTSCProcessorV1 >>>> %s: Unable to create cached CVMetalTextureRef from pixel buffer"
+ "<<<< RTSCProcessorV1 >>>> %s: Unable to create metal texture cache"
+ "<<<< RTSCProcessorV1 >>>> %s: Unable to get texture from CVMetalTextureRef"
+ "<<<< RTSCProcessorV1 >>>> %s: Unable to update SensorRawValidBufferRect"
+ "<<<< RTSCProcessorV1 >>>> %s: Unexpected output FOV preset"
+ "<<<< RTSCProcessorV1 >>>> %s: Unknown processing type %d"
+ "<<<< RTSCProcessorV1 >>>> %s: Unsupported output FOV preset %lu"
+ "<<<< RTSCProcessorV1 >>>> %s: _inputCalibrationData is nil"
+ "<<<< RTSCProcessorV1 >>>> %s: _inputMetadata is nil"
+ "<<<< RTSCProcessorV1 >>>> %s: _inputPixelBuffer is nil"
+ "<<<< RTSCProcessorV1 >>>> %s: _outputPixelBuffer || !_renderingEnabled is nil"
+ "<<<< RTSCProcessorV1 >>>> %s: cmdEncoder is nil"
+ "<<<< RTSCProcessorV1 >>>> %s: cvMetalTextureCacheRef is nil"
+ "<<<< RTSCProcessorV1 >>>> %s: disabling stabilization bounds clamping"
+ "<<<< RTSCProcessorV1 >>>> %s: faceReframer failed to initialize"
+ "<<<< RTSCProcessorV1 >>>> %s: faceReframingEnabled is not supported for processingType: %d"
+ "<<<< RTSCProcessorV1 >>>> %s: pixelBuffer is NULL"
+ "<<<< RTSCProcessorV1 >>>> %s: setOutputROI: <%.2f %.2f %.2f %.2f>"
+ "<<<< RTSCProcessorV1 >>>> %s: stabilizer failed to initialize"
+ "<<<< RTSCProcessorV1 >>>> %s: zoomOutForMultiSubjects is not supported for outputFOVPreset: %d"
+ "<<<< RTSCProcessorV1 >>>> %s: zoomOutForMultiSubjects is not supported for processingType: %d"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Converged after %d iterations. Final margin: %e"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Failed extracting metadata"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Failed to converge. Final margin: %f"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Failed to get ImageCircle Center"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Failed to get ImageCircle Radius"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Failed to initialize"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Intrinsic matrix missing from calibration data"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Minimum transform is out of bounds! Unable to clamp"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Pixel size value is invalid"
+ "<<<< RTSCRealTimeStabilization >>>> %s: Transform margins: [(%f,%f,%f),(%f,%f,%f),(%f,%f,%f),(%f,%f,%f)]"
+ "<<<< RTSCRealTimeStabilization >>>> %s: boundingRect is smaller than outputCropRect"
+ "<<<< RTSCSpringAnimation >>>> %s: Animation cannot be updated without valid current time!"
+ "<<<< RTSCSpringAnimation >>>> %s: Invalid preset %lu"
+ "<<<< RTSCTuningParametersV1 >>>> %s: Failed to get tuning parameter faceReframingOutputFOV from tuning plist"
+ "<<<< RTSCTuningParametersV1 >>>> %s: Failed to get tuning parameter naturalOutputFOV from tuning plist"
+ "<<<< RTSCTuningParametersV1 >>>> %s: Failed to get tuning parameter stabilizationReservedFOV from tuning plist"
+ "<<<< RTSCTuningParametersV1 >>>> %s: Failed to load plist %@"
+ "@\"RTSCFaceReframer\""
+ "@64@0:8{?=[3]}16"
+ "Could not extract ImageCircle"
+ "Could not find any CropRect in the metadata dictionary!"
+ "Did not find motion data for current capture time!"
+ "Did not find motion data for startPTS!"
+ "Empty ISP motion data"
+ "Empty sagPosition"
+ "ExposureTime missing from metadata"
+ "FigMotionComputeFramePTSOffsetFromISPCrop"
+ "FigMotionComputeLensMovementAndSagForTimeStamp"
+ "FigMotionComputeQuaternionForTimeStamp"
+ "FigMotionGetISPHallData"
+ "FigMotionGetISPMotionData"
+ "FigMotionGetMotionDataFromISP"
+ "FigMotionGetSensorValidCropRect"
+ "FigMotionISPHallDataFromCFData"
+ "FigMotionISPMotionDataFromCFData"
+ "FigMotionInitializeQuaternion"
+ "FigMotionInterpolateQuaternionsByAngle"
+ "FigMotionNormalizeQuaternion"
+ "FinalCropRect not found in metadata dictionary"
+ "ISP Hall data size did not match expected number of bytes."
+ "ISP Hall data version is not supported."
+ "ISP motion data size did not match expected number of bytes."
+ "ISP motion data version is not supported."
+ "Invalid ISP Hall data"
+ "Invalid ISP motion data"
+ "Invalid hallPositionIndex"
+ "Invalid input"
+ "Missing OriginalPresentationTimeStamp"
+ "NULL metadata dictionary"
+ "One or more parameters are NULL!"
+ "Output buffer size must be same as input"
+ "Quaternion length is too small!"
+ "Quaternion pointer is null!"
+ "RTSCFaceReframer"
+ "RTSCFaceReframer.m"
+ "RTSCTrace"
+ "Raw sensor height is not strictly positive!"
+ "RawCropRect found in metadata dictionary but malformed!"
+ "RawSensorHeight is missing from metadata dictionary!"
+ "RollingShutterSkew is missing from metadata dictionary!"
+ "RollingShutterSkew missing from metadata"
+ "SensorRawValidBufferRect found in metadata dictionary but malformed!"
+ "SensorReadoutRect found in metadata dictionary but malformed!"
+ "T,R,N,V_filteredBlurVector"
+ "TB,N,V_boundsClampingDisabled"
+ "TB,N,V_faceReframingEnabled"
+ "TB,N,V_motionBlurShimmerMitigationDisabled"
+ "TB,N,V_renderingEnabled"
+ "TotalSensorCropRect found in metadata dictionary but malformed!"
+ "T{?=[3]},R,N,V_framingHomography"
+ "T{RTSCStabilizationMetadata=d{?=}{?=}},R,N,V_stabilizationMetadata"
+ "[2{?=\"vector\"}]"
+ "_applyRotationAdjustmentsToReframingCorrection:stabilizationMetadata:cameraMetadata:"
+ "_boundsClampingDisabled"
+ "_clampRotationCorrection:shiftCorrection:ToBoundingCorners:boundingEllipse:currentBoundingMargin:cameraMetadata:"
+ "_computeFaceReframingRotationForMetadataDict:cameraMetadata:stabilizationMetadata:"
+ "_computeHomographyForFramingCorrection:shiftCorrection:cameraMetadata:"
+ "_extractCameraMetadata:fromMetadataDictionary:calibrationDictionary:"
+ "_faceReframer"
+ "_faceReframingEnabled"
+ "_fallbackSuggestionFOV"
+ "_findInterpolatedRotationCorrection:shiftCorrection:withinBoundingCorners:boundingEllipse:correctionBoundsMargin:cameraMetadata:"
+ "_framingHomography"
+ "_motionBlurShimmerMitigationDisabled"
+ "_outputPixelBuffer || !_renderingEnabled"
+ "_outputRotationPerturbation"
+ "_outputShiftPerturbation"
+ "_prevInputPose"
+ "_prevTimestamp"
+ "_reframingCorrection"
+ "_renderingEnabled"
+ "_rotationCorrection"
+ "_setDefaultParameters"
+ "_shiftCorrection"
+ "_stabilizationMetadata"
+ "_updatePerturbationStatesWithTimestamp:"
+ "_updateRollingShutterModelWithMotionSample:cameraMetadata:hallPositionIndex:atTime:"
+ "aA"
+ "boundsClampingDisabled"
+ "calibrationDict is missing"
+ "cameraMetadata is missing"
+ "cmdBuffer is NULL"
+ "com.apple.coremedia"
+ "f156@0:8{?=}1632{?=[2]}40{RTSCEllipse=}72f88{FRCameraMetadata=f{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}92"
+ "faceReframingEnabled"
+ "fr_computeReducedImageCircleForFaceFraming"
+ "framingHomography"
+ "hallPositionIndex != kFigHallPositionIndex_None"
+ "i152@0:8@16@24{?=ii}32{CGRect={CGPoint=dd}{CGSize=dd}}40{RTSCStabilizationMetadata=d{?=}{?=}}72"
+ "i32@0:8@16^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}24"
+ "i32@0:8^{__CFDictionary=}16^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}24"
+ "i40@0:8^{FRCameraMetadata=f{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}16@24@32"
+ "i52@0:8{?=}16^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}32i40d44"
+ "i64@0:8^{__CFDictionary=}16@24^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}32^{?=}40^48^56"
+ "initWithCameraExtrinsics:"
+ "kCMBaseObjectError_Invalidated"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "kCMBaseObjectError_UnsupportedVersion"
+ "kCMBaseObjectError_ValueNotAvailable"
+ "low_freq_error_logging"
+ "metadataDict && calibrationDict && cameraMetadata"
+ "metadataDict is missing"
+ "motionBlurShimmerMitigationDisabled"
+ "outputRotation"
+ "pinhole camera focal length is missing"
+ "renderingEnabled"
+ "reservedOverscan"
+ "rts_addMotionDataToRing"
+ "setBoundsClampingDisabled:"
+ "setFaceReframingEnabled:"
+ "setMotionBlurShimmerMitigationDisabled:"
+ "setRenderingEnabled:"
+ "setReservedOverscan:"
+ "stabilizationMetadata"
+ "stabilizationRotation"
+ "updateFramingHomographyUsingMetadata:inputCalibration:pixelBufferDimensions:outputFOVRect:stabilizationMetadata:"
+ "v156@0:8{?=}1632{?=[2]}40{RTSCEllipse=}72f88{FRCameraMetadata=f{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}92"
+ "v236@0:8{RTSCameraSmoothingModel={?=}}16{?=[2]}48{RTSCEllipse=}80f96{?=}100116{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}124"
+ "{?=[3]}104@0:8{?=}1632{FRCameraMetadata=f{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}40"
+ "{?=[3]}232@0:8{RTSCameraSmoothingModel={?=}}16{?=}4864{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}72{?=[3]}184"
+ "{?=}168@0:8@16{FRCameraMetadata=f{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}24{RTSCStabilizationMetadata=d{?=}{?=}}88"
+ "{?=}176@0:8{?=}16{RTSCStabilizationMetadata=d{?=}{?=}}32{FRCameraMetadata=f{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}112"
+ "{RTSCStabilizationMetadata=\"timestamp\"d\"inputCameraPose\"{?=\"vector\"}\"motionBlurVector\"\"rotationCorrection\"{?=\"vector\"}\"shiftCorrection\"}"
+ "{RTSCStabilizationMetadata=d{?=}{?=}}16@0:8"
+ "{RTSCameraSmoothingModel={?=}}144@0:8{?=}16{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}32"
+ "{RTSCameraSmoothingModel={?=}}272@0:8{?=[2]}16{RTSCEllipse=}48{RTSCameraSmoothingModel={?=}}64{RTSCameraSmoothingModel={?=}}96f128f132{?=}136152{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSCEllipse=}}160"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb2c"
- "%s signalled err=%d at <>:%d"
- "@72@0:8{?=[3]}16{?=Bf}64"
- "TB,N,V_enableFaceReframing"
- "Tf,R,N,V_prevSamplingRate"
- "_enableFaceReframing"
- "_prevCameraPose"
- "_prevSamplingRate"
- "_stabilizationCorrection"
- "_updateRollingShutterModelWithMotionSample:cameraMetadata:currentPort:atTime:"
- "enableFaceReframing"
- "i32@0:8@16^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}24"
- "i32@0:8^{__CFDictionary=}16^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}24"
- "i52@0:8{?=}16^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}32i40d44"
- "i64@0:8^{__CFDictionary=}16@24^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}32^{?=}40^48^56"
- "initWithCameraExtrinsics:faceReframingSettings:"
- "portIndex"
- "portType"
- "prevSamplingRate"
- "setEnableFaceReframing:"
- "v236@0:8{RTSCameraSmoothingModel={?=}}16{?=[2]}48{RTSEllipse=}80f96{?=}100116{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}124"
- "{?=[3]}232@0:8{RTSCameraSmoothingModel={?=}}16{?=}4864{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}72{?=[3]}184"
- "{RTSCameraSmoothingModel={?=}}144@0:8{?=}16{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}32"
- "{RTSCameraSmoothingModel={?=}}272@0:8{?=[2]}16{RTSEllipse=}48{RTSCameraSmoothingModel={?=}}64{RTSCameraSmoothingModel={?=}}96f128f132{?=}136152{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}160"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x92c1"

```
