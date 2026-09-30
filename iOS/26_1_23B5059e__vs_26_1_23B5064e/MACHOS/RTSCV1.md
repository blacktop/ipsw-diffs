## RTSCV1

> `/System/Library/VideoProcessors/RTSCV1.bundle/RTSCV1`

```diff

-664.40.15.122.3
-  __TEXT.__text: 0x128d0
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x1400
-  __TEXT.__objc_methlist: 0xd60
-  __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x17ec
-  __TEXT.__oslogstring: 0x21a8
-  __TEXT.__objc_methname: 0x2985
-  __TEXT.__objc_classname: 0x28a
-  __TEXT.__objc_methtype: 0x10c6
-  __TEXT.__gcc_except_tab: 0x618
-  __TEXT.__unwind_info: 0x428
-  __DATA_CONST.__auth_got: 0x350
+664.40.18.0.0
+  __TEXT.__text: 0xe330
+  __TEXT.__auth_stubs: 0x650
+  __TEXT.__objc_stubs: 0x1520
+  __TEXT.__objc_methlist: 0xde8
+  __TEXT.__const: 0x2d8
+  __TEXT.__cstring: 0x71a
+  __TEXT.__objc_methname: 0x2b78
+  __TEXT.__objc_classname: 0x2a3
+  __TEXT.__objc_methtype: 0x11c5
+  __TEXT.__gcc_except_tab: 0x318
+  __TEXT.__unwind_info: 0x3d0
+  __DATA_CONST.__auth_got: 0x338
   __DATA_CONST.__got: 0x1c0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__cfstring: 0x180
-  __DATA_CONST.__objc_classlist: 0x70
+  __DATA_CONST.__cfstring: 0x140
+  __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x68
+  __DATA_CONST.__objc_superrefs: 0x70
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA.__objc_const: 0x2408
-  __DATA.__objc_selrefs: 0x7a0
-  __DATA.__objc_ivar: 0x274
-  __DATA.__objc_data: 0x460
+  __DATA.__objc_const: 0x25c0
+  __DATA.__objc_selrefs: 0x7d8
+  __DATA.__objc_ivar: 0x294
+  __DATA.__objc_data: 0x4b0
   __DATA.__data: 0x180
   __DATA.__bss: 0xc
-  __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C3A8360-D40F-3D02-A5DD-06F702E7F2FE
-  Functions: 280
-  Symbols:   922
-  CStrings:  879
+  UUID: 56AC7008-20A4-364F-B643-6989DB5191F7
+  Functions: 306
+  Symbols:   952
+  CStrings:  710
 
Symbols:
+ -[RTSCProcessorV1 _processPreview].cold.1
+ -[RTSCProcessorV1 _processPreview].cold.2
+ -[RTSCProcessorV1 _processPreview].cold.3
+ -[RTSCProcessorV1 _processPreview].cold.4
+ -[RTSCProcessorV1 _processPreview].cold.5
+ -[RTSCProcessorV1 _processPreview].cold.6
+ -[RTSCProcessorV1 _processPreview].cold.7
+ -[RTSCProcessorV1 _processStill].cold.1
+ -[RTSCProcessorV1 _processVideo].cold.1
+ -[RTSCProcessorV1 _processVideo].cold.2
+ -[RTSCProcessorV1 _processVideo].cold.3
+ -[RTSCProcessorV1 _processVideo].cold.4
+ -[RTSCProcessorV1 _processVideo].cold.5
+ -[RTSCProcessorV1 _processVideo].cold.6
+ -[RTSCProcessorV1 _updateTransformAndMetadataForPreview]
+ -[RTSCProcessorV1 prewarm].cold.1
+ -[RTSCProcessorV1 process].cold.1
+ -[RTSCProcessorV1 process].cold.2
+ -[RTSCProcessorV1 process].cold.3
+ -[RTSCProcessorV1 setup].cold.1
+ -[RTSCProcessorV1 setup].cold.2
+ -[RTSCRealTimeStabilization _computeClampedRollingShutterTransformForBoundingRect:]
+ -[RTSCRealTimeStabilization _computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:rollingShutterTransform:]
+ -[RTSCRealTimeStabilization _extractMetadataAndMotionDataFromDictionary:calibration:cameraMetadata:cameraPose:oisOffset:sagOffset:].cold.10
+ -[RTSCRealTimeStabilization _extractMetadataAndMotionDataFromDictionary:calibration:cameraMetadata:cameraPose:oisOffset:sagOffset:].cold.8
+ -[RTSCRealTimeStabilization _extractMetadataAndMotionDataFromDictionary:calibration:cameraMetadata:cameraPose:oisOffset:sagOffset:].cold.9
+ -[RTSCRealTimeStabilization _updateRollingShutterModelWithMotionSample:cameraMetadata:currentPort:atTime:]
+ -[RTSCRealTimeStabilization _updateRollingShutterModelWithMotionSample:cameraMetadata:currentPort:atTime:].cold.1
+ -[RTSCRealTimeStabilization rollingShutterCompensationEnabled]
+ -[RTSCRealTimeStabilization setRollingShutterCompensationEnabled:]
+ -[RTSCRealTimeStabilization setStabilizationSmoothingDisabled:]
+ -[RTSCRealTimeStabilization stabilizationSmoothingDisabled]
+ -[RTSCRealTimeStabilization updateStabilizationHomographyUsingMetadata:inputCalibration:pixelBufferDimensions:outputFOVRect:].cold.2
+ -[RTSCRollingShutterModel fitNormalizedBackwardsTransformForBufferSize:limitFactor:]
+ -[RTSCRollingShutterModel init]
+ -[RTSCRollingShutterModel resetToCenterPosition:withPose:principalPoint:focalLength:]
+ -[RTSCRollingShutterModel updateModelAtRow:withPose:principalPoint:]
+ GCC_except_table39
+ GCC_except_table41
+ OBJC_IVAR_$_RTSCRealTimeStabilization._rollingShutterCompensationEnabled
+ OBJC_IVAR_$_RTSCRealTimeStabilization._rollingShutterModel
+ OBJC_IVAR_$_RTSCRealTimeStabilization._rollingShutterTransform
+ OBJC_IVAR_$_RTSCRealTimeStabilization._stabilizationSmoothingDisabled
+ OBJC_IVAR_$_RTSCRollingShutterModel._covarFit
+ OBJC_IVAR_$_RTSCRollingShutterModel._focalLength
+ OBJC_IVAR_$_RTSCRollingShutterModel._referencePartialProjection
+ OBJC_IVAR_$_RTSCRollingShutterModel._referencePosition
+ _CGRectIntersection
+ _CGRectUnion
+ _FigSignalErrorAtGM
+ _OBJC_CLASS_$_RTSCRollingShutterModel
+ _OBJC_METACLASS_$_RTSCRollingShutterModel
+ __OBJC_$_INSTANCE_METHODS_RTSCRollingShutterModel
+ __OBJC_$_INSTANCE_VARIABLES_RTSCRollingShutterModel
+ __OBJC_CLASS_RO_$_RTSCRollingShutterModel
+ __OBJC_METACLASS_RO_$_RTSCRollingShutterModel
+ _objc_msgSend$_computeClampedRollingShutterTransformForBoundingRect:
+ _objc_msgSend$_computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:rollingShutterTransform:
+ _objc_msgSend$_updateRollingShutterModelWithMotionSample:cameraMetadata:currentPort:atTime:
+ _objc_msgSend$_updateTransformAndMetadataForPreview
+ _objc_msgSend$fitNormalizedBackwardsTransformForBufferSize:limitFactor:
+ _objc_msgSend$resetToCenterPosition:withPose:principalPoint:focalLength:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setRollingShutterCompensationEnabled:
+ _objc_msgSend$setStabilizationSmoothingDisabled:
+ _objc_msgSend$updateModelAtRow:withPose:principalPoint:
- -[RTSCRealTimeStabilization _computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:]
- -[RTSCRealTimeStabilization _getCalibrationDataFromDictionary:cameraMetadata:].cold.1
- -[RTSCRealTimeStabilization _getCalibrationDataFromDictionary:cameraMetadata:].cold.2
- -[RTSCRealTimeStabilization _getCalibrationDataFromDictionary:cameraMetadata:].cold.3
- GCC_except_table14
- GCC_except_table17
- GCC_except_table19
- GCC_except_table20
- GCC_except_table21
- GCC_except_table22
- GCC_except_table24
- GCC_except_table35
- GCC_except_table4
- GCC_except_table40
- GCC_except_table7
- GCC_except_table8
- _FigMotionInitializeQuaternion
- _FigSignalErrorAt3
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- _OUTLINED_FUNCTION_6
- _OUTLINED_FUNCTION_7
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- _RTSCFaceReframingUtilitiesTrace
- _RTSCRealTimeStabilizationTrace
- _RTSCTrace
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_note_initialize_category_with_default_work_cf
- _objc_msgSend$_computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:
- _os_log_type_enabled
CStrings:
+ "%s signalled err=%d at <>:%d"
+ "@\"RTSCRollingShutterModel\""
+ "CVPixelBufferGetWidth( _outputPixelBuffer ) == CVPixelBufferGetWidth( _inputPixelBuffer ) && CVPixelBufferGetHeight( _outputPixelBuffer ) == CVPixelBufferGetHeight( _inputPixelBuffer )"
+ "RTSCRollingShutterModel"
+ "_computeClampedRollingShutterTransformForBoundingRect:"
+ "_computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:rollingShutterTransform:"
+ "_covarFit"
+ "_focalLength"
+ "_referencePartialProjection"
+ "_referencePosition"
+ "_rollingShutterModel"
+ "_rollingShutterTransform"
+ "_updateRollingShutterModelWithMotionSample:cameraMetadata:currentPort:atTime:"
+ "_updateTransformAndMetadataForPreview"
+ "didHaveMotionData"
+ "fitNormalizedBackwardsTransformForBufferSize:limitFactor:"
+ "i32@0:8@16^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}24"
+ "i32@0:8^{__CFDictionary=}16^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}24"
+ "i52@0:8{?=}16^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}32i40d44"
+ "i64@0:8^{__CFDictionary=}16@24^{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}32^{?=}40^48^56"
+ "resetToCenterPosition:withPose:principalPoint:focalLength:"
+ "setObject:forKeyedSubscript:"
+ "updateModelAtRow:withPose:principalPoint:"
+ "v236@0:8{RTSCameraSmoothingModel={?=}}16{?=[2]}48{RTSEllipse=}80f96{?=}100116{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}124"
+ "v44@0:8f16{?=}2036"
+ "v52@0:816{?=}2440f48"
+ "{?=[3]}232@0:8{RTSCameraSmoothingModel={?=}}16{?=}4864{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}72{?=[3]}184"
+ "{?=[3]}24@0:8r^{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "{?=[3]}28@0:816f24"
+ "{RTSCameraSmoothingModel={?=}}144@0:8{?=}16{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}32"
+ "{RTSCameraSmoothingModel={?=}}272@0:8{?=[2]}16{RTSEllipse=}48{RTSCameraSmoothingModel={?=}}64{RTSCameraSmoothingModel={?=}}96f128f132{?=}136152{RTSCameraMetadata=ffBdddd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}160"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x92c1"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "( -73465 )"
- "-[RTSCAdaptiveFilterStrength initWithMaxTimescale:minTimescale:transitionTime:]"
- "-[RTSCAutocovarianceDynamicsAnalyzer4DOF initWithTimeConstant:initialCovariance:]"
- "-[RTSCFaceReframingV1 _computeViewPortSmoothingTimescaleForViewPortMargins:predictedViewPortMargins:centeredViewPortMargins:faceBoxSize:]"
- "-[RTSCFaceReframingV1 _updateOffsetOfViewPortBox:withinBoundingRect:]"
- "-[RTSCFaceReframingV1 init]"
- "-[RTSCFaceTrackerV2 _getFaceOrientationInDictionary:asQuaternion:]"
- "-[RTSCFaceTrackerV2 initWithTimeConstant:]"
- "-[RTSCFaceTrackerV2 trackFaceBoxesWithDetectedObjects:atTime:bufferSize:changeFromPrevFrame:]"
- "-[RTSCKalmanFilter4DOF init]"
- "-[RTSCProcessorV1 _bindCVPixleBuffer:usage:]"
- "-[RTSCProcessorV1 _cachedTextureFromPixelBuffer:usage:]"
- "-[RTSCProcessorV1 _confineCropRectToValidImageCircle:]"
- "-[RTSCProcessorV1 _createRenderTargetForOutputTex:renderTargetTex:]"
- "-[RTSCProcessorV1 _encodeRenderTargetResolve:renderTargetTex:outputTex:]"
- "-[RTSCProcessorV1 _extractFinalCropRect]"
- "-[RTSCProcessorV1 _processPreview]"
- "-[RTSCProcessorV1 _processStill]"
- "-[RTSCProcessorV1 _processVideo]"
- "-[RTSCProcessorV1 _render]"
- "-[RTSCProcessorV1 _updateInputCameraCalibration]"
- "-[RTSCProcessorV1 _updateOutputFOV]"
- "-[RTSCProcessorV1 prepareToProcess:]"
- "-[RTSCProcessorV1 prewarm]"
- "-[RTSCProcessorV1 process]"
- "-[RTSCProcessorV1 setMetalCommandQueue:]"
- "-[RTSCProcessorV1 setOutputFOVPreset:]"
- "-[RTSCProcessorV1 setOutputROI:]"
- "-[RTSCProcessorV1 setup]"
- "-[RTSCRealTimeStabilization _clampStabilizedCamera:ToBoundingCorners:boundingEllipse:currentBoundingMargin:inputPose:oisOffset:cameraMetadata:]"
- "-[RTSCRealTimeStabilization _extractMetadataAndMotionDataFromDictionary:calibration:cameraMetadata:cameraPose:oisOffset:sagOffset:]"
- "-[RTSCRealTimeStabilization _findCameraModelWithinBoundingCorners:boundingEllipse:outsideBoundsModel:insideBoundsModel:outsideBoundsMargin:insideBoundsMargin:inputPose:oisOffset:cameraMetadata:]"
- "-[RTSCRealTimeStabilization _getAllMetadataFromDictionary:cameraMetadata:]"
- "-[RTSCRealTimeStabilization _getCalibrationDataFromDictionary:cameraMetadata:]"
- "-[RTSCRealTimeStabilization initWithCameraExtrinsics:faceReframingSettings:]"
- "-[RTSCRealTimeStabilization updateStabilizationHomographyUsingMetadata:inputCalibration:pixelBufferDimensions:outputFOVRect:]"
- "-[RTSCShadersV1 initWithContext:]"
- "-[RTSCSpringAnimation updateToTime:]"
- "-[RTSCSpringAnimation(Presets) configureWithPreset:]"
- "-[RTSCTuningParametersV1 initWithDictionary:]"
- "-[RTSCTuningParametersV1 init]"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on portIndex %d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCAutocovarianceDynamicsAnalyzer4DOF.m %s: Failed to initialize"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCKalmanFilter4DOF.m %s: Filter is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: maxTimescale is less than minTimescale. Forcing maxTimescale = minTimescale"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/RTSC/Bundle/Computation/RTSCStabilizationUtilities.m %s: minTimescale and transitionTime must be greater than zero"
- "<<<< RTSCFaceFramingUtilities >>>> %s: %@ is missing for face detection"
- "<<<< RTSCFaceFramingUtilities >>>> %s: Failed to initialize"
- "<<<< RTSCFaceFramingUtilities >>>> %s: Failed to initialized covarianceEstimator"
- "<<<< RTSCFaceFramingUtilities >>>> %s: Roll/Pitch/Yaw is missing for face detection"
- "<<<< RTSCFaceFramingUtilities >>>> %s: ViewPortMargin: [%f,%f,%f,%f]"
- "<<<< RTSCFaceFramingUtilities >>>> %s: finalTrackingTimescale: [%f,%f] \ttargetTrackingTimescale: [%f,%f] \tmaxTrackingTimescale: [%f,%f]"
- "<<<< RTSCProcessorV1 >>>> %s: Client specified FOV of %.2f is invalid, using max output FOV instead ( %2.f )"
- "<<<< RTSCProcessorV1 >>>> %s: Client specified FOV of %.2f is not feasible, clamping to max output FOV ( %2.f )"
- "<<<< RTSCProcessorV1 >>>> %s: Command queue already created, metalCommandQueue should be set before -setup"
- "<<<< RTSCProcessorV1 >>>> %s: Face Reframing FOV in tuning ( %.2f ) is not feasible, clamping to max output FOV ( %.2f )"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to allocate intermediate texture for AA resolve"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to allocate render target texture"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to bind input pixel buffer as texture"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to bind output pixel buffer as texture"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to bind pixel buffer %p to texture"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to create metal allocator for RTSCProcessor"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to create metal context for RTSCProcessor"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to encode downsample for AA resolve"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to encode render"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to get image circle center"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to get image circle radius"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to load kernel RTSC::Downsample"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to load kernel RTSC::Render"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to load kernel RTSC::ReplaceRegion"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to load shaders required by RTSCProcessor"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to load tuning parameters"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to update current and candidate framing crop rects"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to update input camera calibration"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to update output FOV crop"
- "<<<< RTSCProcessorV1 >>>> %s: Failed to update stabilization"
- "<<<< RTSCProcessorV1 >>>> %s: Forcing identity transform for preview. _rollingShutterCompensationEnabled %d. _stabilizationSmoothingDisabled %d"
- "<<<< RTSCProcessorV1 >>>> %s: Intrinsic matrix missing from calibration data"
- "<<<< RTSCProcessorV1 >>>> %s: Intrinsic matrix reference dimensions is missing from calibration data"
- "<<<< RTSCProcessorV1 >>>> %s: Invalid processing type for RTSCProcessor"
- "<<<< RTSCProcessorV1 >>>> %s: Natural FOV in tuning ( %.2f ) is not feasible, clamping to max output FOV ( %.2f )"
- "<<<< RTSCProcessorV1 >>>> %s: Pixel buffer %c%c%c%c format not supported"
- "<<<< RTSCProcessorV1 >>>> %s: Pixel size is missing from calibration data"
- "<<<< RTSCProcessorV1 >>>> %s: Pixel size value is invalid"
- "<<<< RTSCProcessorV1 >>>> %s: RTSCProcessor failed to render."
- "<<<< RTSCProcessorV1 >>>> %s: Unable to create cached CVMetalTextureRef from pixel buffer"
- "<<<< RTSCProcessorV1 >>>> %s: Unable to create metal texture cache"
- "<<<< RTSCProcessorV1 >>>> %s: Unable to get texture from CVMetalTextureRef"
- "<<<< RTSCProcessorV1 >>>> %s: Unexpected output FOV preset"
- "<<<< RTSCProcessorV1 >>>> %s: Unknown processing type %d"
- "<<<< RTSCProcessorV1 >>>> %s: Unsupported output FOV preset %lu"
- "<<<< RTSCProcessorV1 >>>> %s: _inputCalibrationData is nil"
- "<<<< RTSCProcessorV1 >>>> %s: _inputMetadata is nil"
- "<<<< RTSCProcessorV1 >>>> %s: _inputPixelBuffer is nil"
- "<<<< RTSCProcessorV1 >>>> %s: _outputPixelBuffer is nil"
- "<<<< RTSCProcessorV1 >>>> %s: cmdEncoder is nil"
- "<<<< RTSCProcessorV1 >>>> %s: cvMetalTextureCacheRef is nil"
- "<<<< RTSCProcessorV1 >>>> %s: enableFaceReframing is not supported for processingType: %d"
- "<<<< RTSCProcessorV1 >>>> %s: pixelBuffer is NULL"
- "<<<< RTSCProcessorV1 >>>> %s: setOutputROI: <%.2f %.2f %.2f %.2f>"
- "<<<< RTSCProcessorV1 >>>> %s: zoomOutForMultiSubjects is not supported for outputFOVPreset: %d"
- "<<<< RTSCProcessorV1 >>>> %s: zoomOutForMultiSubjects is not supported for processingType: %d"
- "<<<< RTSCRealTimeStabilization >>>> %s: Converged after %d iterations. Final margin: %e"
- "<<<< RTSCRealTimeStabilization >>>> %s: Failed extracting metadata"
- "<<<< RTSCRealTimeStabilization >>>> %s: Failed to converge. Final margin: %f"
- "<<<< RTSCRealTimeStabilization >>>> %s: Failed to get ImageCircle Center"
- "<<<< RTSCRealTimeStabilization >>>> %s: Failed to get ImageCircle Radius"
- "<<<< RTSCRealTimeStabilization >>>> %s: Failed to initialize"
- "<<<< RTSCRealTimeStabilization >>>> %s: Image circle radius is different in width (%f) and height (%f)"
- "<<<< RTSCRealTimeStabilization >>>> %s: Image circle radius is near or less than zero: %f"
- "<<<< RTSCRealTimeStabilization >>>> %s: Intrinsic matrix missing from calibration data"
- "<<<< RTSCRealTimeStabilization >>>> %s: Minimum transform is out of bounds! Unable to clamp"
- "<<<< RTSCRealTimeStabilization >>>> %s: Pixel size value is invalid"
- "<<<< RTSCRealTimeStabilization >>>> %s: Transform margins: [(%f,%f,%f),(%f,%f,%f),(%f,%f,%f),(%f,%f,%f)]"
- "<<<< RTSCSpringAnimation >>>> %s: Animation cannot be updated without valid current time!"
- "<<<< RTSCSpringAnimation >>>> %s: Invalid preset %lu"
- "<<<< RTSCTuningParametersV1 >>>> %s: Failed to get tuning parameter faceReframingOutputFOV from tuning plist"
- "<<<< RTSCTuningParametersV1 >>>> %s: Failed to get tuning parameter naturalOutputFOV from tuning plist"
- "<<<< RTSCTuningParametersV1 >>>> %s: Failed to get tuning parameter stabilizationReservedFOV from tuning plist"
- "<<<< RTSCTuningParametersV1 >>>> %s: Failed to load plist %@"
- "Could not extract ImageCircle"
- "Could not find any CropRect in the metadata dictionary!"
- "Did not find motion data for current capture time!"
- "Empty ISP motion data"
- "Empty sagPosition"
- "ExposureTime missing from metadata"
- "FigMotionComputeFramePTSOffsetFromISPCrop"
- "FigMotionComputeLensMovementAndSagForTimeStamp"
- "FigMotionComputeQuaternionForTimeStamp"
- "FigMotionGetISPHallData"
- "FigMotionGetISPMotionData"
- "FigMotionGetMotionDataFromISP"
- "FigMotionGetSensorValidCropRect"
- "FigMotionISPHallDataFromCFData"
- "FigMotionISPMotionDataFromCFData"
- "FigMotionInitializeQuaternion"
- "FigMotionInterpolateQuaternionsByAngle"
- "FigMotionNormalizeQuaternion"
- "FinalCropRect not found in metadata dictionary"
- "ISP Hall data size did not match expected number of bytes."
- "ISP Hall data version is not supported."
- "ISP motion data size did not match expected number of bytes."
- "ISP motion data version is not supported."
- "Invalid ISP Hall data"
- "Invalid ISP motion data"
- "Invalid input"
- "Invalid port type"
- "Missing OriginalPresentationTimeStamp"
- "NULL Hall sample count"
- "NULL metadata dictionary"
- "NULL port index"
- "NULL port type"
- "One or more parameters are NULL!"
- "Output data is null."
- "Quaternion length is too small!"
- "Quaternion pointer is null!"
- "RTSCTrace"
- "Raw sensor height is not strictly positive!"
- "RawCropRect found in metadata dictionary but malformed!"
- "RawSensorHeight is missing from metadata dictionary!"
- "RollingShutterSkew is missing from metadata dictionary!"
- "RollingShutterSkew missing from metadata"
- "SensorRawValidBufferRect found in metadata dictionary but malformed!"
- "SensorReadoutRect found in metadata dictionary but malformed!"
- "TotalSensorCropRect found in metadata dictionary but malformed!"
- "_computeHomographyForStabilizedCamera:inputPose:oisOffset:cameraMetadata:"
- "calibrationDict is missing"
- "cameraMetadata is missing"
- "cmdBuffer is NULL"
- "com.apple.coremedia"
- "i32@0:8@16^{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}24"
- "i32@0:8^{__CFDictionary=}16^{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}24"
- "i64@0:8^{__CFDictionary=}16@24^{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}32^{?=}40^48^56"
- "kCMBaseObjectError_Invalidated"
- "kCMBaseObjectError_ParamErr"
- "kCMBaseObjectError_UnsupportedOperation"
- "kCMBaseObjectError_UnsupportedVersion"
- "kCMBaseObjectError_ValueNotAvailable"
- "low_freq_error_logging"
- "metadataDict is missing"
- "pinhole camera focal length is missing"
- "portIndexFromPortType"
- "rts_computeReducedImageCircleForFaceFraming"
- "v220@0:8{RTSCameraSmoothingModel={?=}}16{?=[2]}48{RTSEllipse=}80f96{?=}100116{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}124"
- "{?=[3]}168@0:8{RTSCameraSmoothingModel={?=}}16{?=}4864{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}72"
- "{RTSCameraSmoothingModel={?=}}128@0:8{?=}16{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}32"
- "{RTSCameraSmoothingModel={?=}}256@0:8{?=[2]}16{RTSEllipse=}48{RTSCameraSmoothingModel={?=}}64{RTSCameraSmoothingModel={?=}}96f128f132{?=}136152{RTSCameraMetadata=ffBdd{CGRect={CGPoint=dd}{CGSize=dd}}{RTSEllipse=}}160"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\x94!"

```
