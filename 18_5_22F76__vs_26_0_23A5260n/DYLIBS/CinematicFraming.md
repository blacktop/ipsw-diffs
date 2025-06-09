## CinematicFraming

> `/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x23ec4
-  __TEXT.__auth_stubs: 0x8a0
-  __TEXT.__objc_methlist: 0x24bc
-  __TEXT.__const: 0x620
-  __TEXT.__gcc_except_tab: 0xdbc
-  __TEXT.__cstring: 0x1ee7
+650.0.0.122.4
+  __TEXT.__text: 0x308b0
+  __TEXT.__auth_stubs: 0x8c0
+  __TEXT.__objc_methlist: 0x23fc
+  __TEXT.__const: 0x630
+  __TEXT.__gcc_except_tab: 0x121c
+  __TEXT.__oslogstring: 0x560d
+  __TEXT.__cstring: 0x3207
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x880
-  __TEXT.__objc_classname: 0x2de
-  __TEXT.__objc_methname: 0x7ba6
-  __TEXT.__objc_methtype: 0x21fd
-  __TEXT.__objc_stubs: 0x4460
-  __DATA_CONST.__got: 0x200
+  __TEXT.__unwind_info: 0x988
+  __TEXT.__objc_classname: 0x2dc
+  __TEXT.__objc_methname: 0x77b8
+  __TEXT.__objc_methtype: 0x21b4
+  __TEXT.__objc_stubs: 0x4300
+  __DATA_CONST.__got: 0x1f8
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x16e8
+  __DATA_CONST.__objc_selrefs: 0x1660
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x468
+  __AUTH_CONST.__auth_got: 0x478
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1700
-  __AUTH_CONST.__objc_const: 0x4fe0
+  __AUTH_CONST.__cfstring: 0x16a0
+  __AUTH_CONST.__objc_const: 0x4de0
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_ivar: 0x5a0
+  __DATA.__objc_ivar: 0x570
   __DATA.__data: 0x3a0
+  __DATA.__common: 0x50
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x7d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A22B4C86-8930-399F-9B93-29894167FDBD
-  Functions: 828
-  Symbols:   3079
-  CStrings:  1948
+  UUID: EF6B0F9C-B14D-3552-B672-D08FCAA32210
+  Functions: 841
+  Symbols:   3128
+  CStrings:  2245
 
Symbols:
+ -[CinematicFramingSessionInputMetadata _validateCalibrationDictionary:].cold.1
+ -[CinematicFramingSessionInputMetadata _validateCalibrationDictionary:].cold.2
+ -[CinematicFramingSessionInputMetadata _validateCalibrationDictionary:].cold.3
+ -[CinematicFramingSessionInputMetadata _validateCalibrationDictionary:].cold.4
+ -[CinematicFramingSessionInputMetadata _validateCalibrationDictionary:].cold.5
+ -[CinematicFramingSessionInputMetadata _validateCalibrationDictionary:].cold.6
+ -[DeskCamRenderingSession rectangleForZoomFactorValue:]
+ -[DeskCamRenderingSession trapezoidForZoomFactorValue:]
+ -[DeskCamSession rectangleForZoomFactorValue:]
+ -[DeskCamSession trapezoidForZoomFactorValue:]
+ -[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:].cold.1
+ -[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:].cold.2
+ -[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:].cold.3
+ -[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:].cold.4
+ -[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:].cold.5
+ -[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:].cold.6
+ -[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:].cold.7
+ -[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:].cold.8
+ -[SubjectSelectionSession _initGaze].cold.1
+ -[SubjectSelectionSession _initGaze].cold.2
+ -[SubjectSelectionSession _initGaze].cold.3
+ -[SubjectSelectionSession _initGaze].cold.4
+ -[SubjectSelectionSession _initGaze].cold.5
+ -[SubjectSelectionSession _initGaze].cold.6
+ -[SubjectSelectionSession _initGaze].cold.7
+ -[SubjectSelectionSession _runGazeInference:faceRect:gazeScore:].cold.1
+ -[SubjectSelectionSession _runGazeInference:faceRect:gazeScore:].cold.2
+ -[SubjectSelectionSession _runGazeInference:faceRect:gazeScore:].cold.3
+ -[SubjectSelectionSession initWithCurrentProcessIsCameraCaptureDaemon:].cold.1
+ -[VCCamera _calculateEffectiveFocalLengthFromFOV:]
+ -[VCCamera _calculateFOVFromEffectiveFocalLength:]
+ -[VCCamera _calculateValidImageCircleRadius]
+ -[VCCamera fisheyeFactor]
+ -[VCCamera setFisheyeFactor:]
+ GCC_except_table19
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table24
+ GCC_except_table25
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table35
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table53
+ GCC_except_table55
+ _CinematicFramingTrace
+ _DeskCamTrace
+ _FigSignalErrorAt3
+ _OBJC_IVAR_$_VCCamera._fisheyeFactor
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _SubjectSelectionTrace
+ _VirtualCameraTrace
+ __ZN15SpringAnimationIdLm4EE6updateEd
+ __ZNK15SpringAnimationIdLm4EE12currentForceEv
+ __os_log_send_and_compose_impl
+ __readFloat
+ _acosf
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _gFigCinematicFramingKalmanFilter
+ _objc_msgSend$GPUEndTime
+ _objc_msgSend$GPUStartTime
+ _objc_msgSend$_calculateEffectiveFocalLengthFromFOV:
+ _objc_msgSend$_calculateFOVFromEffectiveFocalLength:
+ _objc_msgSend$_calculateValidImageCircleRadius
+ _objc_msgSend$debugDescription
+ _objc_msgSend$isFrontCamera
+ _objc_msgSend$rectangleForZoomFactorValue:
+ _objc_msgSend$setFisheyeFactor:
+ _objc_msgSend$setZoomFOV:
+ _objc_msgSend$trapezoidForZoomFactorValue:
+ _objc_retain_x28
+ _os_log_type_enabled
+ _sinf
- -[CinematicFramingRenderer _fisheyeStrengthForDisplayRect:]
- -[CinematicFramingSession initWithOutputDimensions:].cold.1
- -[CinematicFramingSession initWithOutputDimensions:].cold.2
- -[CinematicFramingSession init].cold.2
- -[CinematicFramingSession processPixelBuffer:outputPixelBuffer:].cold.1
- -[CinematicFramingSessionFramingParameters horizontalMinAbsoluteDifferenceThreshold]
- -[CinematicFramingSessionFramingParameters horizontalMinRelativeDifferenceThreshold]
- -[CinematicFramingSessionFramingParameters minCropSize]
- -[CinematicFramingSessionFramingParameters setHorizontalMinAbsoluteDifferenceThreshold:]
- -[CinematicFramingSessionFramingParameters setHorizontalMinRelativeDifferenceThreshold:]
- -[CinematicFramingSessionFramingParameters setMinCropSize:]
- -[CinematicFramingSessionFramingParameters setTopMarginFractionRelaxed:]
- -[CinematicFramingSessionFramingParameters setTopMarginFractionTight:]
- -[CinematicFramingSessionFramingParameters setWidthPaddingAdditive:]
- -[CinematicFramingSessionFramingParameters setWidthPaddingMultiplierNoFocusRelaxed:]
- -[CinematicFramingSessionFramingParameters setWidthPaddingMultiplierNoFocusTight:]
- -[CinematicFramingSessionFramingParameters topMarginFractionRelaxed]
- -[CinematicFramingSessionFramingParameters topMarginFractionTight]
- -[CinematicFramingSessionFramingParameters widthPaddingAdditive]
- -[CinematicFramingSessionFramingParameters widthPaddingMultiplierNoFocusRelaxed]
- -[CinematicFramingSessionFramingParameters widthPaddingMultiplierNoFocusTight]
- -[DeskCamRenderingSession _initializeMetal].cold.6
- -[DeskCamSession processPixelBuffer:withMetadata:outputPixelBuffer:].cold.1
- -[DeskCamSession processPixelBuffer:withMetadata:outputPixelBuffer:].cold.2
- -[VCCamera _updateModelFisheyeProperties]
- -[VCCamera setStereographicFisheyeStrength:]
- -[VCCamera stereographicFisheyeStrength]
- -[VCProcessor auxiliaryStreamCamera]
- -[VCProcessor cameraSwitchingDelegate]
- -[VCProcessor checkCameraSwitchingWithAuxilaryStreamMetadata:]
- -[VCProcessor setAuxilaryStreamCamera:]
- -[VCProcessor setCameraSwitchingDelegate:]
- GCC_except_table31
- GCC_except_table32
- GCC_except_table58
- GCC_except_table70
- _FigSignalErrorAt
- _OBJC_IVAR_$_CinematicFramingRenderer._stereographicFisheyeF
- _OBJC_IVAR_$_CinematicFramingRenderer._stereographicFisheyeMaxStrength
- _OBJC_IVAR_$_CinematicFramingSessionFramingParameters.horizontalMinAbsoluteDifferenceThreshold
- _OBJC_IVAR_$_CinematicFramingSessionFramingParameters.horizontalMinRelativeDifferenceThreshold
- _OBJC_IVAR_$_CinematicFramingSessionFramingParameters.minCropSize
- _OBJC_IVAR_$_CinematicFramingSessionFramingParameters.topMarginFractionRelaxed
- _OBJC_IVAR_$_CinematicFramingSessionFramingParameters.topMarginFractionTight
- _OBJC_IVAR_$_CinematicFramingSessionFramingParameters.widthPaddingAdditive
- _OBJC_IVAR_$_CinematicFramingSessionFramingParameters.widthPaddingMultiplierNoFocusRelaxed
- _OBJC_IVAR_$_CinematicFramingSessionFramingParameters.widthPaddingMultiplierNoFocusTight
- _OBJC_IVAR_$_VCCamera._stereographicFisheyeStrength
- _OBJC_IVAR_$_VCProcessor._auxiliaryStreamCamera
- _OBJC_IVAR_$_VCProcessor._cameraSwitchingDelegate
- __ZN15SpringAnimationIdLm6EE6updateEd
- ___stack_chk_fail
- ___stack_chk_guard
- __simd_atan2_f4
- __simd_tan_f4
- _memcpy
- _objc_msgSend$_fisheyeStrengthForDisplayRect:
- _objc_msgSend$_updateModelFisheyeProperties
- _objc_msgSend$horizontalMinAbsoluteDifferenceThreshold
- _objc_msgSend$horizontalMinRelativeDifferenceThreshold
- _objc_msgSend$minCropSize
- _objc_msgSend$processor:wantsActiveStreamPortType:
- _objc_msgSend$setHorizontalMinAbsoluteDifferenceThreshold:
- _objc_msgSend$setHorizontalMinRelativeDifferenceThreshold:
- _objc_msgSend$setMinCropSize:
- _objc_msgSend$setStereographicFisheyeStrength:
- _objc_msgSend$setTopMarginFractionRelaxed:
- _objc_msgSend$setTopMarginFractionTight:
- _objc_msgSend$setWidthPaddingAdditive:
- _objc_msgSend$setWidthPaddingMultiplierNoFocusRelaxed:
- _objc_msgSend$setWidthPaddingMultiplierNoFocusTight:
- _objc_msgSend$superWideToWideSwitchMargin
- _objc_msgSend$topMarginFractionRelaxed
- _objc_msgSend$topMarginFractionTight
- _objc_msgSend$wideToSuperWideSwitchMargin
- _objc_msgSend$widthPaddingAdditive
- _objc_msgSend$widthPaddingMultiplierNoFocusRelaxed
- _objc_msgSend$widthPaddingMultiplierNoFocusTight
- _objc_retain_x27
- _tan
CStrings:
+ "  fisheyeFactor  : %g      \n"
+ "  focalLength    : %g      \n"
+ "  forwardGeometricDistortionPolynomial    : "
+ "  geometricDistortionCalibration : %@\n"
+ "  geometricDistortionCalibration : %@ \n"
+ "  inverseGeometricDistortionPolynomial    : "
+ "  pixelSize                               : %g          \n"
+ "  rotation       : % 6.3f % 6.3f % 6.3f \n"
+ "  translation    : % 6.3f % 6.3f % 6.3f \n"
+ "% 6.4f "
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "-[AnimationEngine driveAnimationAtTime:withConstraints:withMultiplier:]"
+ "-[CinematicFramingDirector updateWithMetadata:]"
+ "-[CinematicFramingRenderer _createComputePipelinesForShaders:]"
+ "-[CinematicFramingRenderer _filterDetectionsInInputImageCoordinates:trackType:]"
+ "-[CinematicFramingRenderer _rotationMatrixForDisplayRect:]"
+ "-[CinematicFramingRenderer finish]"
+ "-[CinematicFramingRenderer initializeMetal]"
+ "-[CinematicFramingRenderer processBuffer:cropRect:outputPixelBuffer:]"
+ "-[CinematicFramingRenderer registerCalibrationData:]"
+ "-[CinematicFramingSession initWithOutputDimensions:]"
+ "-[CinematicFramingSession init]"
+ "-[CinematicFramingSession processPixelBuffer:outputPixelBuffer:]"
+ "-[CinematicFramingSession processWithMetadata:]"
+ "-[CinematicFramingSession setFramingStyle:]"
+ "-[CinematicFramingSession setOutputFramingRectOfInterest:]"
+ "-[CinematicFramingSessionInputMetadata _validateCalibrationDictionary:]"
+ "-[CinematicFramingSessionInputMetadata initWithDetectedObjectsInfo:calibrationData:timestamp:aspectRatio:sensorID:filteredFaceIDs:filteredBodyIDs:calibrationDistortionCoefficientsSupported:calibrationValidMaxRadiusSupported:]"
+ "-[CinematicFramingSessionOptions optionsForFramingStyle:]"
+ "-[CinematicTracker processDetections:ofType:atTime:]"
+ "-[CinematicTracker processFaceDetections:bodyDetections:atTime:inView:]"
+ "-[CinematicTracker removeTrackOfType:atIndex:atTime:]"
+ "-[CinematicTracker updateBodyFacePairsAtTime:]"
+ "-[DeskCamRenderingSession _allocateTextures]"
+ "-[DeskCamRenderingSession _compileComputeShader:]"
+ "-[DeskCamRenderingSession _filterAutoZoomScalingFactor:]"
+ "-[DeskCamRenderingSession _filterDeskEdgeDetectorEndPoints::]"
+ "-[DeskCamRenderingSession _initializeMetal]"
+ "-[DeskCamRenderingSession _newBufferWithLength:options:label:]"
+ "-[DeskCamRenderingSession _shiftFramingSpaceRectangleToExploitSensorSpace:]"
+ "-[DeskCamRenderingSession _updateDeskEdgeDetectionDataInOutputSpace]"
+ "-[DeskCamRenderingSession _updatePitchAndRoll]"
+ "-[DeskCamRenderingSession _updatePitch]"
+ "-[DeskCamRenderingSession _updateRoll]"
+ "-[DeskCamRenderingSession _viewportScaleMultiplier]"
+ "-[DeskCamRenderingSession autoZoomValue]"
+ "-[DeskCamRenderingSession dealloc]"
+ "-[DeskCamRenderingSession initWithOutputDimensions:portType:deviceType:isFrontFacingCamera:]"
+ "-[DeskCamRenderingSession processBuffer:outputPixelBuffer:]"
+ "-[DeskCamRenderingSession registerBodyDetections:]"
+ "-[DeskCamRenderingSession registerCameraCalibrationDictionary:]"
+ "-[DeskCamRenderingSession registerGravity:]"
+ "-[DeskCamSession initWithOutputDimensions:portType:deviceModelName:]"
+ "-[DeskCamSession processPixelBuffer:withMetadata:outputPixelBuffer:]"
+ "-[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:]"
+ "-[DeskCamSessionInputMetadata initWithDetectedObjectsInfo:cameraCalibrationData:cameraOrientation:timestamp:aspectRatio:sensorID:gravity:]"
+ "-[SceneFramingEngine computeViewportFromDeadband:]"
+ "-[SceneFramingEngine setFramingStyle:]"
+ "-[SceneFramingEngine updateDeadbandWithSubjectRect:atTime:]"
+ "-[SceneFramingEngine updateTargetViewportForFloatingWithTracks:atTime:]"
+ "-[SubjectSelectionSession _initGaze]"
+ "-[SubjectSelectionSession _runGazeDetection:faceObjects:selectedFaceRects:]"
+ "-[SubjectSelectionSession _runGazeInference:faceRect:gazeScore:]"
+ "-[SubjectSelectionSession _updateDetectionRects:bodyObjects:timestamp:]"
+ "-[SubjectSelectionSession initWithCurrentProcessIsCameraCaptureDaemon:]"
+ "-[SubjectSelectionSession processPixelBuffer:timestamp:detectedObjects:usedFaceIDs:usedBodyIDs:]"
+ "-[VCCamera initWithDictionary:]"
+ "-[VCCamera setFisheyeFactor:]"
+ "-[VCCamera updateWithCalibration:]"
+ "-[VCCameraAnimator updateToTime:]"
+ "-[VCCameraAnimator(Presets) configureWithPreset:]"
+ "-[VCProcessor _bindCVPixleBuffer:usage:]"
+ "-[VCProcessor _cachedTexturesFromPixelBuffer:usage:]"
+ "-[VCProcessor _confineOutputCameraToInputCameraFrustum:]"
+ "-[VCProcessor _createRenderTargetForOutputLumaTex:outputChromaTex:renderTargetLumaTex:renderTargetChromaTex:]"
+ "-[VCProcessor _encodeRenderTargetResolve:renderTargetLumaTex:renderTargetChromaTex:outputLumaTex:outputChromaTex:]"
+ "-[VCProcessor _getBaseZoomFactor:]"
+ "-[VCProcessor _getEquivalentOutputCameraFocalLength:rotation:forViewport:]"
+ "-[VCProcessor _getGravityVectorForCamera:fromMetadata:]"
+ "-[VCProcessor _metalTextureFormatFromPixelBufferFormat:forPlane:]"
+ "-[VCProcessor _processStill]"
+ "-[VCProcessor _processVideo]"
+ "-[VCProcessor _render]"
+ "-[VCProcessor _setOutputPixelBufferAttachments]"
+ "-[VCProcessor _updateAutoFraming]"
+ "-[VCProcessor _updateManualFramingStateMetadata]"
+ "-[VCProcessor _updateOutputCameraAnimation]"
+ "-[VCProcessor _updateOutputCameraFisheyeEffect]"
+ "-[VCProcessor _updateOutputCameraForRollCorrection]"
+ "-[VCProcessor adjustToFrameCurrentScene]"
+ "-[VCProcessor continueRotatingToPoint:]"
+ "-[VCProcessor prewarm]"
+ "-[VCProcessor process]"
+ "-[VCProcessor resetOutputCamera]"
+ "-[VCProcessor setAutoFramingEnabled:]"
+ "-[VCProcessor setManualFramingDefaultVideoZoomFactor:]"
+ "-[VCProcessor setMetalCommandQueue:]"
+ "-[VCProcessor setOutputCameraDefaultRotation:]"
+ "-[VCProcessor setOutputROI:]"
+ "-[VCProcessor setVideoZoomFactor:]"
+ "-[VCProcessor setup]"
+ "-[VCProcessor startRotatingFromPoint:]"
+ "-[VCShaders initWithContext:]"
+ "-[VCTuningParameters init]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CinematicFraming/CinematicFraming/Common/CinematicFramingShared.m %s: pixel buffer chroma %c%c%c%c format not supported"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CinematicFraming/CinematicFraming/Common/CinematicFramingShared.m %s: pixel buffer luma %c%c%c%c format not supported"
+ "<<<< AnimationEngine >>>> %s: Unsupported option: %zu"
+ "<<<< CinematicFramingDirector >>>> %s: Updating rectangle animator without valid initial state!"
+ "<<<< CinematicFramingRenderer >>>> %s: Failed to create metal library: %@"
+ "<<<< CinematicFramingRenderer >>>> %s: No calibration data for frame!"
+ "<<<< CinematicFramingRenderer >>>> %s: Unable to create metal texture cache: %d"
+ "<<<< CinematicFramingRenderer >>>> %s: Warning: Metal pixel format 0x%08x is not supported on this device"
+ "<<<< CinematicFramingRenderer >>>> %s: [CF] [FrameUndistortionSession registerCalibrationData:]\ncalibrationDataDict: %s"
+ "<<<< CinematicFramingRenderer >>>> %s: [CF] gravityInCameraSpace (after rotation): < %.2f %.2f %.2f >"
+ "<<<< CinematicFramingRenderer >>>> %s: [CF] gravityInCameraSpace: < %.2f %.2f %.2f >"
+ "<<<< CinematicFramingRenderer >>>> %s: [CF] gravityInFramingSpace: < %.2f %.2f %.2f >"
+ "<<<< CinematicFramingRenderer >>>> %s: [Kalman filter] Type: %d. Count: %d."
+ "<<<< CinematicFramingRenderer >>>> %s: cmdBuffer GPU time: %.4f "
+ "<<<< CinematicFramingSession >>>> %s:  Setting invalid framing style %d, ignored"
+ "<<<< CinematicFramingSession >>>> %s: Bundle is nil"
+ "<<<< CinematicFramingSession >>>> %s: Error while processing pixel buffer (%d)"
+ "<<<< CinematicFramingSession >>>> %s: Ignoring invalid outputFramingRectOfInterest."
+ "<<<< CinematicFramingSession >>>> %s: Invalid output dimension for CinematicFramingSession."
+ "<<<< CinematicFramingSession >>>> %s: Loading tuning plist from %@"
+ "<<<< CinematicFramingSession >>>> %s: Options is nil"
+ "<<<< CinematicFramingSession >>>> %s: Unsupported port type for CinematicFramingSession."
+ "<<<< CinematicFramingSession >>>> %s: [CF] [CinematicFramingSession processWithMetadata:]\nmetadata: %s "
+ "<<<< CinematicFramingSession >>>> %s: director is nil"
+ "<<<< CinematicFramingSession >>>> %s: renderer is nil"
+ "<<<< CinematicFramingSession >>>> %s: setFramingStyle: %d"
+ "<<<< CinematicFramingSession >>>> %s: setOutputFramingRectOfInterest: <%.2f %.2f %.2f %.2f>"
+ "<<<< CinematicFramingSessionInputMetadata >>>> %s: Calibration data is missing, no fallback calibration available for sensor ID %x"
+ "<<<< CinematicFramingSessionInputMetadata >>>> %s: Calibration data is missing, using static fallback calibration for sensor ID %x"
+ "<<<< CinematicFramingSessionInputMetadata >>>> %s: CinematicFramingSessionInputMetadata: Failed to get cameraIntrinsicMatrix from calibrationData dictionary (%d)."
+ "<<<< CinematicFramingSessionInputMetadata >>>> %s: CinematicFramingSessionInputMetadata: Failed to get cameraIntrinsicMatrixReferenceDimensions from calibrationData dictionary (%d)."
+ "<<<< CinematicFramingSessionInputMetadata >>>> %s: CinematicFramingSessionInputMetadata: Failed to get pixelSize from calibrationData dictionary (%d)."
+ "<<<< CinematicFramingSessionInputMetadata >>>> %s: CinematicFramingSessionInputMetadata: calibrationDictionary is nil."
+ "<<<< CinematicFramingSessionOptions >>>> %s: Invalid framing style %d"
+ "<<<< CinematicTracker >>>> %s: [%07.3f sec] Created a new track: %ld of type: %ld with detection oid: %ld"
+ "<<<< CinematicTracker >>>> %s: [%07.3f sec] Pairing body track: %ld with face track: %ld"
+ "<<<< CinematicTracker >>>> %s: [%07.3f sec] Removing dangling stub track: %ld"
+ "<<<< CinematicTracker >>>> %s: [%07.3f sec] Removing track: %ld due to lack of detections"
+ "<<<< CinematicTracker >>>> %s: [%07.3f sec] Unpairing body track: %ld and face track: %ld"
+ "<<<< CinematicTracker >>>> %s: [%07.3f sec] Unpairing track: %ld and track: %ld"
+ "<<<< CinematicTracker >>>> %s: [%07.3f sec] Updating tid: %ld with new detection oid: %ld"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not allocate blurredRGBLowResTexture"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not allocate lineDetectionController.auxiliaryTexture"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not allocate lineDetectionController.cumRowSum"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not allocate lineDetectionController.inputTexture"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not allocate lineDetectionController.rowSums"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not allocate lineDetectionController.rowSumsTexture"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not allocate lineDetectionController.spans"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not allocate warpedRGBLowResTexture"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not allocate warpedRGBTexture"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not create bundle"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not create command queue"
+ "<<<< DeskCamRenderingSession >>>> %s: Could not create metal library: %@"
+ "<<<< DeskCamRenderingSession >>>> %s: Metal device is nil"
+ "<<<< DeskCamRenderingSession >>>> %s: Metal library is nil"
+ "<<<< DeskCamRenderingSession >>>> %s: No calibration data for frame!"
+ "<<<< DeskCamRenderingSession >>>> %s: Unable to create metal texture cache: %d"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskCam][_updateDeskEdgeDetectionDataInOutputSpace] rowIndex: %d"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>_shiftFramingSpaceRectangleToExploitSensorSpace] No vertical shift applied."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>_shiftFramingSpaceRectangleToExploitSensorSpace] Vertical shift applied: %.4f."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>_updateDeskEdgeDetectionDataInOutputSpace] Transform matrix inverse is not valid."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>_updateDeskEdgeDetectionDataInOutputSpace] Transform matrix is not valid."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>_updatePitchAndRoll] Gravity vector: [%.4f, %.4f, %.4f]. Pitch: %.4f. Roll: %.4f."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>_updatePitchAndRoll] Port type: %@. Is front facing camera: %d. Camera orientation: %d."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>_updatePitch] Pitch angle value and pitch refinement value: %f, %f"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>_updateRoll] Gravity vector: [%.4f, %.4f, %.4f].Camera Orientation: %d. Roll: %.4f."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>_viewportScaleMultiplier] rollAngleDistanceToPortraitOrientation: %.4f, rollAngleDistanceToLandscapeOrientation: %.4f, viewportScaleMultiplier %.4f"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue] normalizedPointInOutputCropRect: (%.4f, %.4f)."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue]: Auto zoom value %.4f."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal] autoZoomScalingFactor 1: %.4f, DominantLineYX [%.2f, %.2f]"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal] autoZoomScalingFactor 2: %.4f, DominantLineYX [%.2f, %.2f]"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal] autoZoomScalingFactor 3 after Hysteresis: %.4f"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal][States]: Do not update (state: %d -> %d): abs( deltaZoomfactor ) < smallChangeThresh && smallChangeObservationDuration == 0. _autoZoomScalingFactor = %.4f, autoZoomScalingFactor = %.4f, deltaZoomfactor = %.4f, smallChangeObservationDuration = %d, largeChangeObservationDuration = %d, smallSteadyErrorObservationDuration = %d"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal][States]: Do not update (state: %d): abs( deltaZoomfactor ) > largeChangeThresh] && largeChangeObservationDuration > 0. _autoZoomScalingFactor = %.4f, autoZoomScalingFactor = %.4f, deltaZoomfactor = %.4f, smallChangeObservationDuration = %d, largeChangeObservationDuration = %d, smallSteadyErrorObservationDuration = %d"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal][States]: Do not update (state: %d): abs( deltaZoomfactor ) is within [smallChangeThresh, largeChangeThresh] && do not statisfy SNAPPING condition. _autoZoomScalingFactor = %.4f, autoZoomScalingFactor = %.4f, deltaZoomfactor = %.4f, smallChangeObservationDuration = %d, largeChangeObservationDuration = %d, smallSteadyErrorObservationDuration = (%d -> %d)"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal][States]: Updating (state: %d -> %d): abs( deltaZoomfactor ) > largeChangeThresh] && largeChangeObservationDuration == 0. _autoZoomScalingFactor = %.4f, autoZoomScalingFactor = %.4f, deltaZoomfactor = %.4f, newAutoZoomScalingFactor = %.4f, smallChangeObservationDuration = %d, largeChangeObservationDuration = %d, smallSteadyErrorObservationDuration = %d"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal][States]: Updating (state: %d): abs( deltaZoomfactor ) < smallChangeThresh && smallChangeObservationDuration > 0. _autoZoomScalingFactor = %.4f, autoZoomScalingFactor = %.4f, deltaZoomfactor = %.4f, newAutoZoomScalingFactor = %.4f, smallChangeObservationDuration = %d, largeChangeObservationDuration = %d, smallSteadyErrorObservationDuration = %d"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal][States]: Updating (state: %d): abs( deltaZoomfactor ) is within [smallChangeThresh, largeChangeThresh] and updating. _autoZoomScalingFactor = %.4f, autoZoomScalingFactor = %.4f, deltaZoomfactor = %.4f, newAutoZoomScalingFactor = %.4f, smallChangeObservationDuration = %d, largeChangeObservationDuration = %d, smallSteadyErrorObservationDuration = %d"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal][States]: abs( deltaZoomfactor ) is within [smallChangeThresh, largeChangeThresh] && do not update (state: %d). Waiting to SNAP: meanDeltaZoomFactor (%.4f) > errorMarginToCatch (%.4f) && varDeltaZoomFactor (%.5f) < errorVarThresh (%.5f): _autoZoomScalingFactor  = %.4f, autoZoomScalingFactor = %.4f, deltaZoomfactor = %.4f, newAutoZoomScalingFactor = %.4f, smallChangeObservationDuration = %d, largeChangeObservationDuration = %d, smallSteadyErrorObservationDuration = %d"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>autoZoomValue][Temporal][States]: abs( deltaZoomfactor ) is within [smallChangeThresh, largeChangeThresh] && do not update. SNAPPED (state: %d -> %d): meanDeltaZoomFactor (%.4f) > errorMarginToCatch (%.4f) && varDeltaZoomFactor (%.5f) < errorVarThresh (%.5f), start updating: _autoZoomScalingFactor  = %.4f, autoZoomScalingFactor = %.4f, deltaZoomfactor = %.4f, newAutoZoomScalingFactor = %.4f, smallChangeObservationDuration = %d, largeChangeObservationDuration = %d, smallSteadyErrorObservationDuration = (%d -> %d)"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>init] Configuration: Is front facing camera = %d. Camera orientation = %d."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>registerFaceDetections:bodyDetections:handDetections:] Subject rectangle in framing space: (%.4f, %.4f, %.4f, %.4f)."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>registerFaceDetections:bodyDetections:handDetections:] Subject rectangle in sensor space: (%.4f, %.4f, %.4f, %.4f)."
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][>registerGravity] Raw gravity vector: %f, %f, %f. Alpha: %f"
+ "<<<< DeskCamRenderingSession >>>> %s: [DeskView][_filterDeskEdgeDetectorEndPoints]: (%.4f, %.4f)"
+ "<<<< DeskCamRenderingSession >>>> %s: cmdBuffer GPU time: %.4f "
+ "<<<< DeskCamRenderingSession >>>> %s: cmdBuffer GPU time: %.4f ms "
+ "<<<< DeskCamSession >>>> %s: Bundle is nil"
+ "<<<< DeskCamSession >>>> %s: Error processing buffer: %d"
+ "<<<< DeskCamSession >>>> %s: Options is nil"
+ "<<<< DeskCamSession >>>> %s: Output type %d is not supported"
+ "<<<< DeskCamSession >>>> %s: renderingSession is nil"
+ "<<<< DeskCamSessionInputMetadata >>>> %s: Calibration data is missing for sensor ID %x, defaulting to PA"
+ "<<<< DeskCamSessionInputMetadata >>>> %s: DeskCamSessionInputMetadata: Failed to get cameraIntrinsicMatrix from calibrationData dictionary (%d)."
+ "<<<< DeskCamSessionInputMetadata >>>> %s: DeskCamSessionInputMetadata: Failed to get cameraIntrinsicMatrixReferenceDimensions from calibrationData dictionary (%d)."
+ "<<<< DeskCamSessionInputMetadata >>>> %s: DeskCamSessionInputMetadata: Failed to get distortionCalibrationMaxRadiusInPixels from calibrationData dictionary (%d)."
+ "<<<< DeskCamSessionInputMetadata >>>> %s: DeskCamSessionInputMetadata: Failed to get inverseLensDistortionCoefficients from calibrationData dictionary (%d)."
+ "<<<< DeskCamSessionInputMetadata >>>> %s: DeskCamSessionInputMetadata: Failed to get lensDistortionCenter from calibrationData dictionary (%d)."
+ "<<<< DeskCamSessionInputMetadata >>>> %s: DeskCamSessionInputMetadata: Failed to get lensDistortionCoefficients from calibrationData dictionary (%d)."
+ "<<<< DeskCamSessionInputMetadata >>>> %s: DeskCamSessionInputMetadata: Failed to get pixelSize from calibrationData dictionary (%d)."
+ "<<<< DeskCamSessionInputMetadata >>>> %s: DeskCamSessionInputMetadata: calibrationDictionary is nil."
+ "<<<< Kalman Filter >>>> %s: 'height' filter is nil"
+ "<<<< Kalman Filter >>>> %s: 'width' filter is nil"
+ "<<<< Kalman Filter >>>> %s: 'x' filter is nil"
+ "<<<< Kalman Filter >>>> %s: 'y' filter is nil"
+ "<<<< Kalman Filter >>>> %s: Covariance x: %f. y: %f. w: %f. h: %f"
+ "<<<< Kalman Filter >>>> %s: Filter is nil"
+ "<<<< Kalman Filter >>>> %s: Updating filter with mismatched oid: [filter oid: %d <== observation oid: %d]"
+ "<<<< SceneFramingEngine >>>> %s: Inconsistency in size calculation to ensure subjects fit in deadband!"
+ "<<<< SceneFramingEngine >>>> %s: Newsroom target viewport offset (%f, %f), scale (%f), isFront: %d"
+ "<<<< SceneFramingEngine >>>> %s: Restrict viewport:(%f, %f), maxAllowViewportWidth:%f, framingSpaceBounds:(%f, %f, %f, %f)"
+ "<<<< SceneFramingEngine >>>> %s: Warning: More than one subject track available in Floating framing, was subject selection session configured to single subject mode?"
+ "<<<< SceneFramingEngine >>>> %s: [CF] drift ended, duration: %.4f, offset: %.4f, shouldRecenter: %d"
+ "<<<< SceneFramingEngine >>>> %s: [CF] subjectIsStationary: %d, framingIsIdeal: %d"
+ "<<<< SceneFramingEngine >>>> %s: [CF] timeSincePreviousRecentering: %.4fs"
+ "<<<< SceneFramingEngine >>>> %s: [CF] timeSinceSubjectBecameStationary: %.4fs"
+ "<<<< SubjectSelectionSession >>>> %s:  Remove body %@"
+ "<<<< SubjectSelectionSession >>>> %s:  Remove face %@"
+ "<<<< SubjectSelectionSession >>>> %s: CamGaze descriptor v2 not available: %@"
+ "<<<< SubjectSelectionSession >>>> %s: CamGaze network model not found in VisionCore"
+ "<<<< SubjectSelectionSession >>>> %s: Cannot determine selection for %f sec. Fallback to select all objects"
+ "<<<< SubjectSelectionSession >>>> %s: Configuring source crop failed (%d)"
+ "<<<< SubjectSelectionSession >>>> %s: Fail to retrieve gaze descriptor v1 (error: %@)"
+ "<<<< SubjectSelectionSession >>>> %s: Fail to retrieve gaze input descriptor"
+ "<<<< SubjectSelectionSession >>>> %s: Fail to retrieve gaze output descriptor"
+ "<<<< SubjectSelectionSession >>>> %s: Failed to init gaze"
+ "<<<< SubjectSelectionSession >>>> %s: Loading %@"
+ "<<<< SubjectSelectionSession >>>> %s: Select foreground body %@, size: %f x %f, threshold: %f"
+ "<<<< SubjectSelectionSession >>>> %s: Select foreground face %@, size: %f x %f, threshold: %f"
+ "<<<< SubjectSelectionSession >>>> %s: Start tracking face ID %d"
+ "<<<< SubjectSelectionSession >>>> %s: SubjectSelection init _enableGazeSelection: %d, _gazeElapsedThreshold: %.3f, _gazeScoreThreshold: %.3f"
+ "<<<< SubjectSelectionSession >>>> %s: Unable to add espresso network %@"
+ "<<<< SubjectSelectionSession >>>> %s: Unable to bind espresso buffer"
+ "<<<< SubjectSelectionSession >>>> %s: Unable to bind gaze output"
+ "<<<< SubjectSelectionSession >>>> %s: Unable to build espresso plan"
+ "<<<< SubjectSelectionSession >>>> %s: Unable to create an intermediate input pixel buffer"
+ "<<<< SubjectSelectionSession >>>> %s: Unable to create video toolbox transfer session"
+ "<<<< SubjectSelectionSession >>>> %s: Unable to execute gaze network"
+ "<<<< SubjectSelectionSession >>>> %s: Update last gazed face %@ to %@"
+ "<<<< SubjectSelectionSession >>>> %s: Update last used body %@ to %@"
+ "<<<< SubjectSelectionSession >>>> %s: Update last used face %@ to %@"
+ "<<<< SubjectSelectionSession >>>> %s: VTPixelTransferSessionTransferImage failed (%d)"
+ "<<<< SubjectSelectionSession >>>> %s: VisionCore is not available. Using default parameters."
+ "<<<< SubjectSelectionSession >>>> %s: _espressoContext is NULL"
+ "<<<< SubjectSelectionSession >>>> %s: _espressoPlan is NULL"
+ "<<<< SubjectSelectionSession >>>> %s: espresso ANE init failed. Fallback to MPS."
+ "<<<< VCCamera >>>> %s: Failed to get <IntrinsicMatrix> from calibrationData dictionary"
+ "<<<< VCCamera >>>> %s: Failed to get <IntrinsicMatrixReferenceDimensions> from calibrationData dictionary"
+ "<<<< VCCamera >>>> %s: Failed to get <PixelSize> from calibrationData dictionary"
+ "<<<< VCCamera >>>> %s: Geometric calibration data not provided, or is invalid for %@. GDC will be disabled"
+ "<<<< VCCamera >>>> %s: Invalid dictionary representation of VCCamera: %@"
+ "<<<< VCCamera >>>> %s: Invalid fisheye factor: %f"
+ "<<<< VCCamera >>>> %s: calibrationDict is nil."
+ "<<<< VCCameraAnimator >>>> %s: Animation cannot be updated without valid current time!"
+ "<<<< VCCameraAnimator >>>> %s: Invalid preset %lu"
+ "<<<< VCDefaultsController >>>> %s: Failed to load plist %@"
+ "<<<< VCDefaultsController >>>> %s: Failed to read %@ from tuning dictionary"
+ "<<<< VCProcessor >>>>"
+ "<<<< VCProcessor >>>> %s: CenterStageViewport: { cx=%.2f, cy=%.2f, hfov=%.2f, vfov=%.2f }"
+ "<<<< VCProcessor >>>> %s: Command queue already created, metalCommandQueue should be set before -setup"
+ "<<<< VCProcessor >>>> %s: Failed get or create transport layer attachment"
+ "<<<< VCProcessor >>>> %s: Failed to allocate intermediate texture for AA resolve"
+ "<<<< VCProcessor >>>> %s: Failed to allocate render target textures"
+ "<<<< VCProcessor >>>> %s: Failed to apply fisheye effect."
+ "<<<< VCProcessor >>>> %s: Failed to bind input pixel buffer as texture"
+ "<<<< VCProcessor >>>> %s: Failed to bind output pixel buffer as texture"
+ "<<<< VCProcessor >>>> %s: Failed to bind pixel buffer %p [%d] to texture"
+ "<<<< VCProcessor >>>> %s: Failed to confine output camera."
+ "<<<< VCProcessor >>>> %s: Failed to create copy of detectedObjectsInfo to update"
+ "<<<< VCProcessor >>>> %s: Failed to create metal allocator for VCProcessor"
+ "<<<< VCProcessor >>>> %s: Failed to create metal context for VCProcessor"
+ "<<<< VCProcessor >>>> %s: Failed to create render target textures"
+ "<<<< VCProcessor >>>> %s: Failed to encode downsample for AA resolve"
+ "<<<< VCProcessor >>>> %s: Failed to encode render"
+ "<<<< VCProcessor >>>> %s: Failed to encode render target resolve"
+ "<<<< VCProcessor >>>> %s: Failed to get base zoom factor for port type %@"
+ "<<<< VCProcessor >>>> %s: Failed to get camera info for port type %@"
+ "<<<< VCProcessor >>>> %s: Failed to load kernel %s"
+ "<<<< VCProcessor >>>> %s: Failed to load shaders required by VCProcessor"
+ "<<<< VCProcessor >>>> %s: Failed to load tuning parameters"
+ "<<<< VCProcessor >>>> %s: Failed to perform roll correction."
+ "<<<< VCProcessor >>>> %s: Failed to render virtual camera view."
+ "<<<< VCProcessor >>>> %s: Failed to set metadata attachment."
+ "<<<< VCProcessor >>>> %s: Failed to setup CinematicFramingSession"
+ "<<<< VCProcessor >>>> %s: Failed to update auto framing."
+ "<<<< VCProcessor >>>> %s: Failed to update inputCamera with metadata."
+ "<<<< VCProcessor >>>> %s: Failed to update manual framing state metadata."
+ "<<<< VCProcessor >>>> %s: Failed to update manual framing."
+ "<<<< VCProcessor >>>> %s: Failed to update output camera animation."
+ "<<<< VCProcessor >>>> %s: FisheyeEffectStrength:%.2f, FisheyeFactor:%.2f zoomFOV:%f"
+ "<<<< VCProcessor >>>> %s: Ignoring invalid outputFramingRectOfInterest."
+ "<<<< VCProcessor >>>> %s: Impossible to confine output camera."
+ "<<<< VCProcessor >>>> %s: InputCamera  : %@"
+ "<<<< VCProcessor >>>> %s: Invalid outputDimensions in config"
+ "<<<< VCProcessor >>>> %s: Metadata has a 0 length gravity vector "
+ "<<<< VCProcessor >>>> %s: No rotation applied for zoom factor 1"
+ "<<<< VCProcessor >>>> %s: Only biplanar YUV input is supported"
+ "<<<< VCProcessor >>>> %s: Only biplanar YUV output is supported"
+ "<<<< VCProcessor >>>> %s: OutputCamera : %@"
+ "<<<< VCProcessor >>>> %s: Pixel buffer %c%c%c%c format not supported"
+ "<<<< VCProcessor >>>> %s: Processing failed with calibration: %@"
+ "<<<< VCProcessor >>>> %s: Setting manualFramingDefaultVideoZoomFactor to 0 or less is not allowed."
+ "<<<< VCProcessor >>>> %s: Setting videoZoomFactor to 0 or less is not allowed."
+ "<<<< VCProcessor >>>> %s: Unable to cache pixel buffer texture"
+ "<<<< VCProcessor >>>> %s: Unable to create a metal texture cache"
+ "<<<< VCProcessor >>>> %s: Unable to get metal texture address"
+ "<<<< VCProcessor >>>> %s: Unknown processing type %d"
+ "<<<< VCProcessor >>>> %s: [VCP] gInputCamera: < %.2f %.2f %.2f >"
+ "<<<< VCProcessor >>>> %s: [VCP] gOutputCamera: < %.2f %.2f %.2f >"
+ "<<<< VCProcessor >>>> %s: [VCP] gOutputImage: < %.2f %.2f >"
+ "<<<< VCProcessor >>>> %s: [VCP] gOutputImageRef: < %.2f %.2f >"
+ "<<<< VCProcessor >>>> %s: _inputCamera is nil"
+ "<<<< VCProcessor >>>> %s: _inputMetadata is nil"
+ "<<<< VCProcessor >>>> %s: _inputPixelBuffer is nil"
+ "<<<< VCProcessor >>>> %s: _outputCamera is nil"
+ "<<<< VCProcessor >>>> %s: _outputPixelBuffer is nil"
+ "<<<< VCProcessor >>>> %s: adjustToFrameCurrentScene"
+ "<<<< VCProcessor >>>> %s: cmdEncoder is nil"
+ "<<<< VCProcessor >>>> %s: continueRotatingToPoint: %.2f, %.2f"
+ "<<<< VCProcessor >>>> %s: one-shot framing duration: %.2f"
+ "<<<< VCProcessor >>>> %s: one-shot framing finished!"
+ "<<<< VCProcessor >>>> %s: pixelBuffer is NULL"
+ "<<<< VCProcessor >>>> %s: reset duration: %.2f"
+ "<<<< VCProcessor >>>> %s: reset finished!"
+ "<<<< VCProcessor >>>> %s: resetOutputCamera"
+ "<<<< VCProcessor >>>> %s: setAutoFramingEnabled: %d"
+ "<<<< VCProcessor >>>> %s: setManualFramingDefaultVideoZoomFactor: %.2f"
+ "<<<< VCProcessor >>>> %s: setOutputCameraDefaultRotation: (%.2f, %.2f, %.2f)"
+ "<<<< VCProcessor >>>> %s: setOutputROI: <%.2f %.2f %.2f %.2f>"
+ "<<<< VCProcessor >>>> %s: setVideoZoomFactor: %.2f"
+ "<<<< VCProcessor >>>> %s: startRotatingFromPoint: %.2f, %.2f"
+ "<<<< VCProcessor >>>> %s: textures is nil"
+ "CinematicFraming"
+ "CinematicFramingRenderer.finish"
+ "CinematicFramingRenderer.processBuffer"
+ "ComputeSizeToFitSubjectsInDeadband"
+ "DeskCam"
+ "Fig"
+ "FisheyeFactor"
+ "GPUEndTime"
+ "GPUStartTime"
+ "No"
+ "SubjectSelection"
+ "T^{?=fff{?=[4]}{?=[4]}Bf{?=ffffffff}{?=ffffffff}ff},R,N"
+ "Tf,N,V_fisheyeFactor"
+ "Tf,N,V_focalLength"
+ "T{?={?=[3]}{?=[3]}Bfi{?=ffffffff}{?=ffffffff}},R,N,V_calibrationParameters"
+ "VCCamera<%p>\n"
+ "VCProcessor.mm"
+ "Virtual"
+ "VirtualCamera"
+ "Yes"
+ "^{?=fff{?=[4]}{?=[4]}Bf{?=ffffffff}{?=ffffffff}ff}16@0:8"
+ "_calculateEffectiveFocalLengthFromFOV:"
+ "_calculateFOVFromEffectiveFocalLength:"
+ "_calculateValidImageCircleRadius"
+ "_fisheyeFactor"
+ "_readFloat"
+ "cachedTexturesFromPixelBuffer"
+ "cinematic_framing_kalman_filter_trace"
+ "cmdBuffer is NULL"
+ "com.apple.coremedia"
+ "fisheyeFactor"
+ "i24@0:8^{?={?=fff{?=[4]}{?=[4]}Bf{?=ffffffff}{?=ffffffff}ff}{?=fff{?=[4]}{?=[4]}Bf{?=ffffffff}{?=ffffffff}ff}{?=}{?=}}16"
+ "rectangleForZoomFactorValue:"
+ "setFisheyeFactor:"
+ "trapezoidForZoomFactorValue:"
+ "v296@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48{?={?=[3]}{?=[3]}Bfi{?=ffffffff}{?=ffffffff}}80@288"
+ "{?=\"sensorSize\"\"intrinsicMatrix\"{?=\"columns\"[3]}\"intrinsicMatrixT\"{?=\"columns\"[3]}\"hasGeometricDistortionCalibration\"B\"lensDistortionCenter\"\"mmFactor\"f\"distortionCalibrationValidMaxRadiusInPixels\"i\"inverseGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"forwardGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}}"
+ "{?=\"sensorSize\"\"principalPoint\"\"focalLength\"f\"fisheyeFactor\"f\"validImageCircleRadius\"f\"extrinsicMatrix\"{?=\"columns\"[4]}\"inverseExtrinsicMatrix\"{?=\"columns\"[4]}\"hasGeometricDistortionCalibration\"B\"mmFactor\"f\"geometricDistortionCenter\"\"forwardGeometricDistortion\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"inverseGeometricDistortion\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"calibrationRadiusDistorted\"f\"calibrationRadiusUndistorted\"f}"
+ "{?={?=[3]}{?=[3]}Bfi{?=ffffffff}{?=ffffffff}}16@0:8"
+ "{?={?={?=[3]}{?=[3]}i}{?=[3]}{?={?=[3]}{?=[3]}Bfi{?=ffffffff}{?=ffffffff}}iB}16@0:8"
+ "{?={?=}}20@0:8f16"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}256@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{?={?=[3]}{?=[3]}Bfi{?=ffffffff}{?=ffffffff}}48"
+ "{SpringAnimation<double, 4UL>=\"stiffness\"d\"mass\"d\"dampRatio\"d\"targetValue\"{NDVector<double, 4UL>=\"arr\"[4d]}\"currValue\"{NDVector<double, 4UL>=\"arr\"[4d]}\"velocity\"{NDVector<double, 4UL>=\"arr\"[4d]}\"duration\"d}"
+ "\xa5\xf0\xd3"
+ "\xf0\xf0\x93"
- "  FOV         : %g deg            \n"
- "  focalLength    : %g , %g \n"
- "  forwardGeometricDistortionPolynomial    : %@          \n"
- "  inverseGeometricDistortionPolynomial    : %@          \n"
- "  pixelSize      : %g      \n"
- "  portType    : %@                \n"
- "  rotation       : %6.2f %6.2f %6.2f \n"
- "  rotation    : %6.2f %6.2f %6.2f \n"
- "  sensorID    : 0x%x              \n"
- "  sensorSize  : %g x %g           \n"
- "  stereographicFisheyeStrength : %.2f \n"
- "  translation    : %6.2f %6.2f %6.2f \n"
- "  translation : %6.2f %6.2f %6.2f \n"
- "  zoomFactor  : %g                \n"
- "  zoomedFOV   : %g deg            \n"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CinematicFraming/CinematicFraming/Common/CinematicFramingShared.m Fig"
- "@\"<VCProcessorCameraSwitchingDelegate>\""
- "StereographicFisheyeStrength"
- "T,N,V_focalLength"
- "T^{?={?=[3]}{?=[3]}f{?=[4]}{?=[4]}Bi{?=ffffffff}i{?=ffffffff}f},R,N"
- "Tf,N,V_stereographicFisheyeStrength"
- "Tf,N,VhorizontalMinAbsoluteDifferenceThreshold"
- "Tf,N,VhorizontalMinRelativeDifferenceThreshold"
- "Tf,N,VminCropSize"
- "Tf,N,VtopMarginFractionRelaxed"
- "Tf,N,VtopMarginFractionTight"
- "Tf,N,VwidthPaddingAdditive"
- "Tf,N,VwidthPaddingMultiplierNoFocusRelaxed"
- "Tf,N,VwidthPaddingMultiplierNoFocusTight"
- "T{?={?=[3]}Bfi{?=ffffffff}{?=ffffffff}},R,N,V_calibrationParameters"
- "VCCamera<%p> {\n"
- "^{?={?=[3]}{?=[3]}f{?=[4]}{?=[4]}Bi{?=ffffffff}i{?=ffffffff}f}16@0:8"
- "_auxiliaryStreamCamera"
- "_cameraSwitchingDelegate"
- "_fisheyeStrengthForDisplayRect:"
- "_stereographicFisheyeF"
- "_stereographicFisheyeMaxStrength"
- "_stereographicFisheyeStrength"
- "_updateModelFisheyeProperties"
- "auxiliaryStreamCamera"
- "cameraSwitchingDelegate"
- "checkCameraSwitchingWithAuxilaryStreamMetadata:"
- "horizontalMinAbsoluteDifferenceThreshold"
- "horizontalMinRelativeDifferenceThreshold"
- "i24@0:8^{?={?={?=[3]}{?=[3]}f{?=[4]}{?=[4]}Bi{?=ffffffff}i{?=ffffffff}f}{?={?=[3]}{?=[3]}f{?=[4]}{?=[4]}Bi{?=ffffffff}i{?=ffffffff}f}{?=}{?=}}16"
- "minCropSize"
- "processor:wantsActiveStreamPortType:"
- "setAuxilaryStreamCamera:"
- "setCameraSwitchingDelegate:"
- "setHorizontalMinAbsoluteDifferenceThreshold:"
- "setHorizontalMinRelativeDifferenceThreshold:"
- "setMinCropSize:"
- "setStereographicFisheyeStrength:"
- "setTopMarginFractionRelaxed:"
- "setTopMarginFractionTight:"
- "setWidthPaddingAdditive:"
- "setWidthPaddingMultiplierNoFocusRelaxed:"
- "setWidthPaddingMultiplierNoFocusTight:"
- "stereographicFisheyeStrength"
- "topMarginFractionRelaxed"
- "topMarginFractionTight"
- "v248@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48{?={?=[3]}Bfi{?=ffffffff}{?=ffffffff}}80@240"
- "widthPaddingAdditive"
- "widthPaddingMultiplierNoFocusRelaxed"
- "widthPaddingMultiplierNoFocusTight"
- "{?=\"referenceSensorSize\"\"intrinsicMatrix\"{?=\"columns\"[3]}\"inverseIntrinsicMatrix\"{?=\"columns\"[3]}\"mmFactor\"f\"extrinsicMatrix\"{?=\"columns\"[4]}\"inverseExtrinsicMatrix\"{?=\"columns\"[4]}\"hasGeometricDistortionCalibration\"B\"geometricDistortionCenter\"\"forwardGeometricDistortionCalibrationRadius\"i\"forwardGeometricDistortion\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"inverseGeometricDistortionCalibrationRadius\"i\"inverseGeometricDistortion\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"stereographicFisheyeStrength\"f}"
- "{?=\"sensorSize\"\"intrinsicMatrixT\"{?=\"columns\"[3]}\"hasGeometricDistortionCalibration\"B\"lensDistortionCenter\"\"mmFactor\"f\"distortionCalibrationValidMaxRadiusInPixels\"i\"inverseGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"forwardGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}}"
- "{?={?=[3]}Bfi{?=ffffffff}{?=ffffffff}}16@0:8"
- "{?={?={?=[3]}{?=[3]}i}{?=[3]}{?={?=[3]}Bfi{?=ffffffff}{?=ffffffff}}ffiB}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}208@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{?={?=[3]}Bfi{?=ffffffff}{?=ffffffff}}48"
- "{SpringAnimation<double, 6UL>=\"stiffness\"d\"mass\"d\"dampRatio\"d\"targetValue\"{NDVector<double, 6UL>=\"arr\"[6d]}\"currValue\"{NDVector<double, 6UL>=\"arr\"[6d]}\"velocity\"{NDVector<double, 6UL>=\"arr\"[6d]}\"duration\"d}"
- "}\n"
- "\xf0r"
- "\xf0\xf0\xf0s"

```
