## CinematicFraming

> `/System/Library/PrivateFrameworks/CinematicFraming.framework/CinematicFraming`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0x21748
-  __TEXT.__auth_stubs: 0x850
+580.2.0.0.0
+  __TEXT.__text: 0x2f378
+  __TEXT.__auth_stubs: 0x890
   __TEXT.__objc_methlist: 0x214c
-  __TEXT.__const: 0x540
-  __TEXT.__gcc_except_tab: 0xd4c
-  __TEXT.__cstring: 0x1d3c
+  __TEXT.__const: 0x588
+  __TEXT.__gcc_except_tab: 0x1784
+  __TEXT.__oslogstring: 0x423f
+  __TEXT.__cstring: 0x3191
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__unwind_info: 0x820
+  __TEXT.__unwind_info: 0x900
   __TEXT.__objc_classname: 0x2ca
-  __TEXT.__objc_methname: 0x7940
+  __TEXT.__objc_methname: 0x7958
   __TEXT.__objc_methtype: 0x1eb2
-  __TEXT.__objc_stubs: 0x42c0
+  __TEXT.__objc_stubs: 0x4360
   __DATA_CONST.__got: 0x200
   __DATA_CONST.__const: 0xf0
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15e0
+  __DATA_CONST.__objc_selrefs: 0x15f0
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_arraydata: 0xf0
-  __AUTH_CONST.__auth_got: 0x440
+  __AUTH_CONST.__auth_got: 0x460
   __AUTH_CONST.__const: 0x40
-  __AUTH_CONST.__cfstring: 0x1680
+  __AUTH_CONST.__cfstring: 0x1740
   __AUTH_CONST.__objc_const: 0x5438
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0xf0

   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x588
   __DATA.__data: 0x360
+  __DATA.__common: 0x50
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x7d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 753
-  Symbols:   977
-  CStrings:  1738
+  Functions: 754
+  Symbols:   982
+  CStrings:  2050
 
Symbols:
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _FigSignalErrorAt3
+ _os_log_type_enabled
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
- _FigSignalErrorAt
- _objc_retain_x27
CStrings:
+ "-[CinematicFramingSession processPixelBuffer:outputPixelBuffer:]"
+ "-[SubjectSelectionSession _updateDetectionRects:bodyObjects:timestamp:]"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): Error while processing pixel buffer (%!d(MISSING))"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to create metal context for VCProcessor"
+ "-[DeskCamRenderingSession registerGravity:]"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Loading %!@(MISSING)"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): No calibration data for frame!"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Cannot determine selection for %!f(MISSING) sec. Fallback to select all objects"
+ "-[CinematicFramingRenderer initializeMetal]"
+ "<<<< Kalman Filter >>>> %!s(MISSING): 'width' filter is nil"
+ "<<<< VCProcessor >>>> %!s(MISSING): textures is nil"
+ "cinematic_framing_kalman_filter_trace"
+ "<<<< VCProcessor >>>>"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): Failed to create metal library: %!@(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): startRotatingFromPoint: %!f(MISSING), %!f(MISSING)"
+ "<<<< SceneFramingEngine >>>> %!s(MISSING): [CF] timeSincePreviousRecentering: %!f(MISSING)s"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to update manual framing."
+ "-[SubjectSelectionSession _runGazeDetection:faceObjects:selectedFaceRects:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Ignoring invalid outputFramingRectOfInterest."
+ "GPUStartTime"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Could not create metal library: %!@(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to setup CinematicFramingSession"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Unable to bind espresso buffer"
+ "<<<< VCProcessor >>>> %!s(MISSING): _outputPixelBuffer is nil"
+ "<<<< VCProcessor >>>> %!s(MISSING): _inputPixelBuffer is nil"
+ "<<<< DeskCamSessionInputMetadata >>>> %!s(MISSING): DeskCamSessionInputMetadata: Failed to get inverseLensDistortionCoefficients from calibrationData dictionary (%!d(MISSING))."
+ "-[VCProcessor _updateManualFramingStateMetadata]"
+ "cachedTexturesFromPixelBuffer"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Fail to retrieve gaze descriptor v1 (error: %!@(MISSING))"
+ "com.apple.coremedia"
+ "-[DeskCamSession initWithOutputDimensions:portType:deviceModelName:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Setting manualFramingDefaultVideoZoomFactor to 0 or less is not allowed."
+ "<<<< VCProcessor >>>> %!s(MISSING): Setting videoZoomFactor to 0 or less is not allowed."
+ "<<<< VCProcessor >>>> %!s(MISSING): No rotation applied for zoom factor 1"
+ "<<<< VCProcessor >>>> %!s(MISSING): Unable to create a metal texture cache"
+ "<<<< VCCameraAnimator >>>> %!s(MISSING): Invalid preset %!l(MISSING)u"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Start tracking face ID %!d(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): Requested to switch to port type %!@(MISSING)"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): Ignoring invalid outputFramingRectOfInterest."
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): Bundle is nil"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Unable to bind gaze output"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to load kernel %!s(MISSING)"
+ "<<<< DeskCamSession >>>> %!s(MISSING): Error processing buffer: %!d(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): [VCP] gOutputImage: < %!f(MISSING) %!f(MISSING) >"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): [CF] [CinematicFramingRenderer _framingSpaceBoundsLandscapeLeft]\nreference dimension: [%!f(MISSING), %!f(MISSING)]\nintrinsic matrix: \n %!f(MISSING), %!f(MISSING), %!f(MISSING) \n %!f(MISSING), %!f(MISSING), %!f(MISSING) \n %!f(MISSING), %!f(MISSING), %!f(MISSING)\nfov bounds: [ %!f(MISSING), %!f(MISSING) ]"
+ "-[SubjectSelectionSession initWithCurrentProcessIsCameraCaptureDaemon:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Only biplanar YUV input is supported"
+ "<<<< VCProcessor >>>> %!s(MISSING): setManualFramingDefaultVideoZoomFactor: %!f(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): continueRotatingToPoint: %!f(MISSING), %!f(MISSING)"
+ "CinematicFraming"
+ "GPUEndTime"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): Configuration: stereographicFisheyeF           = %!f(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): _outputCamera is nil"
+ "-[SubjectSelectionSession _initGaze]"
+ "-[VCProcessor setAutoFramingEnabled:]"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): _espressoPlan is NULL"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>init] Configuration: Is front facing camera = %!d(MISSING). Camera orientation = %!d(MISSING)."
+ "-[CinematicFramingSessionInputMetadata _validateCalibrationDictionary:]"
+ "<<<< VCCamera >>>> %!s(MISSING): Failed to get <PixelSize> from calibrationData dictionary"
+ "<<<< CinematicFramingSessionInputMetadata >>>> %!s(MISSING): Calibration data is missing, no fallback calibration available for sensor ID %!x(MISSING)"
+ "<<<< Kalman Filter >>>> %!s(MISSING): 'y' filter is nil"
+ "<<<< CinematicTracker >>>> %!s(MISSING): [%!f(MISSING) sec] Updating tid: %!l(MISSING)d with new detection oid: %!l(MISSING)d"
+ "<<<< DeskCamSessionInputMetadata >>>> %!s(MISSING): DeskCamSessionInputMetadata: Failed to get pixelSize from calibrationData dictionary (%!d(MISSING))."
+ "-[DeskCamSession processPixelBuffer:withMetadata:outputPixelBuffer:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): cmdEncoder is nil"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): Invalid output dimension for CinematicFramingSession."
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Update last gazed face %!@(MISSING) to %!@(MISSING)"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Fail to retrieve gaze output descriptor"
+ "-[VCProcessor startRotatingFromPoint:]"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>_shiftFramingSpaceRectangleToExploitSensorSpace] No vertical shift applied."
+ "<<<< SceneFramingEngine >>>> %!s(MISSING): Warning: More than one subject track available in Floating framing, was subject selection session configured to single subject mode?"
+ "-[DeskCamSessionInputMetadata initWithDetectedObjectsInfo:cameraCalibrationData:cameraOrientation:timestamp:aspectRatio:sensorID:gravity:]"
+ "-[VCProcessor setOutputCameraDefaultRotation:]"
+ "-[CinematicFramingSession init]"
+ "-[CinematicTracker processFaceDetections:bodyDetections:atTime:inView:]"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): _espressoContext is NULL"
+ "SubjectSelection"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to update manual framing state metadata."
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): CamGaze descriptor v2 not available: %!@(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to allocate intermediate texture for AA resolve"
+ "-[CinematicFramingSession processWithMetadata:]"
+ "-[AnimationEngine driveAnimationAtTime:withConstraints:withMultiplier:]"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Unable to execute gaze network"
+ "-[VCProcessor _metalTextureFormatFromPixelBufferFormat:forPlane:]"
+ "-[CinematicFramingRenderer processBuffer:cropRect:outputPixelBuffer:]"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>_shiftFramingSpaceRectangleToExploitSensorSpace] Vertical shift applied: %!f(MISSING)."
+ "ComputeSizeToFitSubjectsInDeadband"
+ "<<<< DeskCamSession >>>> %!s(MISSING): Options is nil"
+ "-[VCProcessor _updateOutputCameraAnimation]"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): Options is nil"
+ "-[VCProcessor _createRenderTargetForOutputLumaTex:outputChromaTex:renderTargetLumaTex:renderTargetChromaTex:]"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): Warning: Metal pixel format 0x%!x(MISSING) is not supported on this device"
+ "<<<< VCProcessor >>>> %!s(MISSING): [VCP] gInputCamera: < %!f(MISSING) %!f(MISSING) %!f(MISSING) >"
+ "-[VCProcessor _processStill]"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING):  Remove body %!@(MISSING)"
+ "<<<< CinematicTracker >>>> %!s(MISSING): [%!f(MISSING) sec] Unpairing track: %!l(MISSING)d and track: %!l(MISSING)d"
+ "-[SceneFramingEngine setFramingStyle:]"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>_updatePitchAndRoll] Gravity vector: [%!f(MISSING), %!f(MISSING), %!f(MISSING)]. Pitch: %!f(MISSING). Roll: %!f(MISSING)."
+ "<<<< Kalman Filter >>>> %!s(MISSING): Covariance x: %!f(MISSING). y: %!f(MISSING). w: %!f(MISSING). h: %!f(MISSING)"
+ "-[DeskCamRenderingSession _allocateTextures]"
+ "-[DeskCamRenderingSession registerCameraCalibrationDictionary:]"
+ "-[CinematicFramingRenderer _createComputePipelinesForShaders:]"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): cmdBuffer GPU time: %!f(MISSING) "
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): VTPixelTransferSessionTransferImage failed (%!d(MISSING))"
+ "-[DeskCamRenderingSession _compileComputeShader:]"
+ "-[SceneFramingEngine computeViewportFromDeadband:]"
+ "-[SubjectSelectionSession processPixelBuffer:timestamp:detectedObjects:usedFaceIDs:usedBodyIDs:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CinematicFraming/CinematicFraming/Common/CinematicFramingShared.m %!s(MISSING): pixel buffer luma %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING) format not supported"
+ "<<<< DeskCamSession >>>> %!s(MISSING): Output type %!d(MISSING) is not supported"
+ "<<<< VCProcessor >>>> %!s(MISSING): Fisheye min/max strengthFOV:[%!f(MISSING), %!f(MISSING)], fisheyeStrength:%!f(MISSING), zoomFOV:%!f(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to bind pixel buffer %!p(MISSING) [%!d(MISSING)] to texture"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): director is nil"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to encode render target resolve"
+ "-[SubjectSelectionSession _runGazeInference:faceRect:gazeScore:]"
+ "<<<< CinematicTracker >>>> %!s(MISSING): [%!f(MISSING) sec] Pairing body track: %!l(MISSING)d with face track: %!l(MISSING)d"
+ "<<<< VCProcessor >>>> %!s(MISSING): CenterStageViewport: { cx=%!f(MISSING), cy=%!f(MISSING), hfov=%!f(MISSING), vfov=%!f(MISSING) }"
+ "-[VCProcessor _encodeRenderTargetResolve:renderTargetLumaTex:renderTargetChromaTex:outputLumaTex:outputChromaTex:]"
+ "-[CinematicTracker processDetections:ofType:atTime:]"
+ "-[CinematicFramingSession setFramingStyle:]"
+ "<<<< CinematicFramingSessionInputMetadata >>>> %!s(MISSING): CinematicFramingSessionInputMetadata: calibrationDictionary is nil."
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to render virtual camera view."
+ "-[VCCameraAnimator updateToTime:]"
+ "<<<< CinematicFramingSessionOptions >>>> %!s(MISSING): Invalid framing style %!d(MISSING)"
+ "<<<< CinematicTracker >>>> %!s(MISSING): [%!f(MISSING) sec] Removing track: %!l(MISSING)d due to lack of detections"
+ "<<<< DeskCamSessionInputMetadata >>>> %!s(MISSING): DeskCamSessionInputMetadata: Failed to get cameraIntrinsicMatrix from calibrationData dictionary (%!d(MISSING))."
+ "-[CinematicFramingRenderer initWithOutputDimensions:]"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): Loading tuning plist from %!@(MISSING)"
+ "-[DeskCamRenderingSession initWithOutputDimensions:portType:deviceType:isFrontFacingCamera:]"
+ "-[VCProcessor _getEquivalentOutputCameraFocalLength:rotation:forViewport:]"
+ "-[VCProcessor _render]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to update inputCamera with metadata."
+ "-[CinematicFramingRenderer _framingSpaceBoundsLandscapeLeft]"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Fail to retrieve gaze input descriptor"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Could not allocate blurredRGBLowResTexture"
+ "-[VCShaders initWithContext:]"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Unable to create metal texture cache: %!d(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): Impossible to confine output camera."
+ "<<<< VCProcessor >>>> %!s(MISSING): reset finished!"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed get or create transport layer attachment"
+ "-[VCProcessor _cachedTexturesFromPixelBuffer:usage:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to encode render"
+ "<<<< VCProcessor >>>> %!s(MISSING): Only biplanar YUV output is supported"
+ "<<<< VCProcessor >>>> %!s(MISSING): [VCP] gOutputImageRef: < %!f(MISSING) %!f(MISSING) >"
+ "<<<< VCCamera >>>> %!s(MISSING): Failed to get <IntrinsicMatrix> from calibrationData dictionary"
+ "<<<< VCProcessor >>>> %!s(MISSING): Unknown processing type %!d(MISSING)"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): [CF] [FrameUndistortionSession registerCalibrationData:]\ncalibrationDataDict: %!s(MISSING)"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>_updatePitchAndRoll] Port type: %!@(MISSING). Is front facing camera: %!d(MISSING). Camera orientation: %!d(MISSING)."
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Select foreground face %!@(MISSING), size: %!f(MISSING) x %!f(MISSING), threshold: %!f(MISSING)"
+ "VCProcessor.mm"
+ "-[CinematicFramingSessionInputMetadata initWithDetectedObjectsInfo:calibrationData:timestamp:aspectRatio:sensorID:filteredFaceIDs:filteredBodyIDs:calibrationDistortionCoefficientsSupported:calibrationValidMaxRadiusSupported:]"
+ "-[CinematicFramingDirector updateWithMetadata:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): setOutputCameraDefaultRotation: (%!f(MISSING), %!f(MISSING), %!f(MISSING))"
+ "<<<< CinematicTracker >>>> %!s(MISSING): [%!f(MISSING) sec] Unpairing body track: %!l(MISSING)d and face track: %!l(MISSING)d"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to create render target textures"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>registerGravity] Raw gravity vector: %!f(MISSING), %!f(MISSING), %!f(MISSING). Alpha: %!f(MISSING)"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Select foreground body %!@(MISSING), size: %!f(MISSING) x %!f(MISSING), threshold: %!f(MISSING)"
+ "_readFloat"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Update last used face %!@(MISSING) to %!@(MISSING)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CinematicFraming/CinematicFraming/Common/CinematicFramingShared.m %!s(MISSING): pixel buffer chroma %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING) format not supported"
+ "-[VCProcessor setVideoZoomFactor:]"
+ "<<<< DeskCamSessionInputMetadata >>>> %!s(MISSING): Calibration data is missing for sensor ID %!x(MISSING), defaulting to PA"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): cmdBuffer GPU time: %!f(MISSING) "
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to create copy of detectedObjectsInfo to update"
+ "-[VCProcessor setManualFramingDefaultVideoZoomFactor:]"
+ "-[CinematicFramingRenderer _filterDetectionsInInputImageCoordinates:trackType:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Pixel buffer %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING) format not supported"
+ "<<<< VCProcessor >>>> %!s(MISSING): Unable to get metal texture address"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING):  Setting invalid framing style %!d(MISSING), ignored"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Metal library is nil"
+ "<<<< CinematicFramingSessionInputMetadata >>>> %!s(MISSING): CinematicFramingSessionInputMetadata: Failed to get cameraIntrinsicMatrixReferenceDimensions from calibrationData dictionary (%!d(MISSING))."
+ "<<<< VCProcessor >>>> %!s(MISSING): Invalid outputDimensions in config"
+ "-[VCCamera initWithDictionary:]"
+ "-[VCCameraAnimator(Presets) configureWithPreset:]"
+ "<<<< DeskCamSessionInputMetadata >>>> %!s(MISSING): DeskCamSessionInputMetadata: Failed to get cameraIntrinsicMatrixReferenceDimensions from calibrationData dictionary (%!d(MISSING))."
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Update last used body %!@(MISSING) to %!@(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to encode downsample for AA resolve"
+ "<<<< SceneFramingEngine >>>> %!s(MISSING): Newsroom target viewport offset (%!f(MISSING), %!f(MISSING)), scale (%!f(MISSING)), isFront: %!d(MISSING)"
+ "DeskCam"
+ "<<<< SceneFramingEngine >>>> %!s(MISSING): [CF] subjectIsStationary: %!d(MISSING), framingIsIdeal: %!d(MISSING)"
+ "-[VCProcessor continueRotatingToPoint:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to allocate render target textures"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Could not allocate warpedRGBLowResTexture"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to load tuning parameters"
+ "-[DeskCamRenderingSession _viewportScaleMultiplier]"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): [CF] gravityInCameraSpace: < %!f(MISSING) %!f(MISSING) %!f(MISSING) >"
+ "<<<< SceneFramingEngine >>>> %!s(MISSING): Restrict viewport:(%!f(MISSING), %!f(MISSING)), maxAllowViewportWidth:%!f(MISSING), framingSpaceBounds:(%!f(MISSING), %!f(MISSING), %!f(MISSING), %!f(MISSING))"
+ "<<<< VCCamera >>>> %!s(MISSING): Geometric calibration data not provided, or is invalid for %!@(MISSING). GDC will be disabled"
+ "<<<< VCProcessor >>>> %!s(MISSING): Invalid tuning parameters for camera switching, hysteresis will be disabled! \nwideToSuperWideMargin: %!f(MISSING) superWideToWideMargin: %!f(MISSING) "
+ "cmdBuffer is NULL"
+ "-[CinematicFramingSessionOptions optionsForFramingStyle:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Command queue already created, metalCommandQueue should be set before -setup"
+ "<<<< DeskCamSession >>>> %!s(MISSING): renderingSession is nil"
+ "-[VCProcessor _bindCVPixleBuffer:usage:]"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Metal device is nil"
+ "-[CinematicFramingSession initWithOutputDimensions:]"
+ "-[VCCamera updateWithCalibration:]"
+ "<<<< SceneFramingEngine >>>> %!s(MISSING): [CF] timeSinceSubjectBecameStationary: %!f(MISSING)s"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): SubjectSelection init _enableGazeSelection: %!d(MISSING), _gazeElapsedThreshold: %!f(MISSING), _gazeScoreThreshold: %!f(MISSING)"
+ "-[VCProcessor checkCameraSwitchingWithAuxilaryStreamMetadata:]"
+ "-[DeskCamRenderingSession _updatePitchAndRoll]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to confine output camera."
+ "-[VCProcessor _updateOutputCameraFisheyeEffect]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to create metal allocator for VCProcessor"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to update auto framing."
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): Configuration: stereographicFisheyeMaxStrength = %!f(MISSING)"
+ "-[DeskCamRenderingSession _updatePitch]"
+ "<<<< VCDefaultsController >>>> %!s(MISSING): Failed to read %!@(MISSING) from tuning dictionary"
+ "<<<< VCProcessor >>>> %!s(MISSING): _inputMetadata is nil"
+ "-[DeskCamRenderingSession _shiftFramingSpaceRectangleToExploitSensorSpace:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): adjustToFrameCurrentScene"
+ "<<<< CinematicTracker >>>> %!s(MISSING): [%!f(MISSING) sec] Removing dangling stub track: %!l(MISSING)d"
+ "<<<< DeskCamSession >>>> %!s(MISSING): Bundle is nil"
+ "<<<< VCProcessor >>>> %!s(MISSING): setVideoZoomFactor: %!f(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): Unable to cache pixel buffer texture"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Configuring source crop failed (%!d(MISSING))"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): [CF] gravityInCameraSpace (after rotation): < %!f(MISSING) %!f(MISSING) %!f(MISSING) >"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to set metadata attachment."
+ "-[VCProcessor process]"
+ "-[CinematicFramingRenderer registerCalibrationData:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): pixelBuffer is NULL"
+ "-[VCProcessor _updateOutputCameraForRollCorrection]"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): [CF] [CinematicFramingSession processWithMetadata:]\nmetadata: %!s(MISSING) "
+ "<<<< VCProcessor >>>> %!s(MISSING): _inputCamera is nil"
+ "<<<< VCCamera >>>> %!s(MISSING): Failed to get <IntrinsicMatrixReferenceDimensions> from calibrationData dictionary"
+ "<<<< CinematicFramingSessionFramingParameters >>>> %!s(MISSING): Error retrieving framing parameter for key %!@(MISSING). Value is missing. Using default %!f(MISSING)."
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): [CF] gravityInFramingSpace: < %!f(MISSING) %!f(MISSING) %!f(MISSING) >"
+ "-[VCProcessor prewarm]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to bind output pixel buffer as texture"
+ "-[SceneFramingEngine updateTargetViewportForFloatingWithTracks:atTime:]"
+ "-[VCProcessor _updateAutoFraming]"
+ "-[VCProcessor setup]"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Unable to build espresso plan"
+ "PlistReadFloat"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Could not create bundle"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to update auxiliaryStreamCamera with metadata."
+ "-[DeskCamRenderingSession processBuffer:outputPixelBuffer:]"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): Unable to create metal texture cache: %!d(MISSING)"
+ "<<<< Kalman Filter >>>> %!s(MISSING): Updating filter with mismatched oid: [filter oid: %!d(MISSING) <== observation oid: %!d(MISSING)]"
+ "-[VCProcessor _getBaseZoomFactor:]"
+ "-[CinematicTracker updateBodyFacePairsAtTime:]"
+ "<<<< VCCamera >>>> %!s(MISSING): Invalid dictionary representation of VCCamera: %!@(MISSING)"
+ "-[DeskCamRenderingSession _initializeMetal]"
+ "-[DeskCamRenderingSession _newBufferWithLength:options:label:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to bind input pixel buffer as texture"
+ "<<<< AnimationEngine >>>> %!s(MISSING): Unsupported option: %!z(MISSING)u"
+ "<<<< VCProcessor >>>> %!s(MISSING): one-shot framing finished!"
+ "<<<< VCProcessor >>>> %!s(MISSING): setAutoFramingEnabled: %!d(MISSING)"
+ "VirtualCamera"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>_viewportScaleMultiplier] rollAngleDistanceToPortraitOrientation: %!f(MISSING), rollAngleDistanceToLandscapeOrientation: %!f(MISSING), viewportScaleMultiplier %!f(MISSING)"
+ "-[CinematicFramingRenderer finish]"
+ "<<<< CinematicFramingSessionInputMetadata >>>> %!s(MISSING): Calibration data is missing, using static fallback calibration for sensor ID %!x(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): one-shot framing duration: %!f(MISSING)"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Could not create command queue"
+ "<<<< SceneFramingEngine >>>> %!s(MISSING): [CF] drift ended, duration: %!f(MISSING), offset: %!f(MISSING), shouldRecenter: %!d(MISSING)"
+ "-[VCProcessor setMetalCommandQueue:]"
+ "<<<< VCDefaultsController >>>> %!s(MISSING): Failed to load plist %!@(MISSING)"
+ "-[CinematicFramingSession setOutputFramingRectOfInterest:]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to update output camera animation."
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): setOutputFramingRectOfInterest: <%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)>"
+ "<<<< CinematicFramingRenderer >>>> %!s(MISSING): [Kalman filter] Type: %!d(MISSING). Count: %!d(MISSING)."
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Unable to create video toolbox transfer session"
+ "<<<< DeskCamSessionInputMetadata >>>> %!s(MISSING): DeskCamSessionInputMetadata: Failed to get lensDistortionCenter from calibrationData dictionary (%!d(MISSING))."
+ "<<<< Kalman Filter >>>> %!s(MISSING): Filter is nil"
+ "<<<< SceneFramingEngine >>>> %!s(MISSING): Inconsistency in size calculation to ensure subjects fit in deadband!"
+ "<<<< DeskCamSessionInputMetadata >>>> %!s(MISSING): DeskCamSessionInputMetadata: Failed to get distortionCalibrationMaxRadiusInPixels from calibrationData dictionary (%!d(MISSING))."
+ "<<<< VCProcessor >>>> %!s(MISSING): [VCP] gOutputCamera: < %!f(MISSING) %!f(MISSING) %!f(MISSING) >"
+ "-[VCProcessor _setOutputPixelBufferAttachments]"
+ "<<<< CinematicFramingSessionInputMetadata >>>> %!s(MISSING): CinematicFramingSessionInputMetadata: Failed to get pixelSize from calibrationData dictionary (%!d(MISSING))."
+ "<<<< VCCameraAnimator >>>> %!s(MISSING): Animation cannot be updated without valid current time!"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING):  Remove face %!@(MISSING)"
+ "-[CinematicTracker removeTrackOfType:atIndex:atTime:]"
+ "<<<< CinematicTracker >>>> %!s(MISSING): [%!f(MISSING) sec] Created a new track: %!l(MISSING)d of type: %!l(MISSING)d with detection oid: %!l(MISSING)d"
+ "-[DeskCamRenderingSession _updateRoll]"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): No calibration data for frame!"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>_updatePitch] Pitch angle value and pitch refinement value: %!f(MISSING), %!f(MISSING)"
+ "<<<< VCCamera >>>> %!s(MISSING): calibrationDict is nil."
+ "-[DeskCamSessionInputMetadata _createCameraCalibrationDictionary:]"
+ "-[VCTuningParameters init]"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Unable to create an intermediate input pixel buffer"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to get base zoom factor for port type %!@(MISSING)"
+ "<<<< DeskCamSessionInputMetadata >>>> %!s(MISSING): DeskCamSessionInputMetadata: Failed to get lensDistortionCoefficients from calibrationData dictionary (%!d(MISSING))."
+ "<<<< CinematicFramingDirector >>>> %!s(MISSING): Updating rectangle animator without valid initial state!"
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): Could not allocate warpedRGBTexture"
+ "-[CinematicFramingRenderer _rotationMatrixForDisplayRect:]"
+ "-[VCProcessor adjustToFrameCurrentScene]"
+ "-1"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to load shaders required by VCProcessor"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): espresso ANE init failed. Fallback to MPS."
+ "<<<< DeskCamRenderingSession >>>> %!s(MISSING): [DeskView][>_updateRoll] Gravity vector: [%!f(MISSING), %!f(MISSING), %!f(MISSING)].Camera Orientation: %!d(MISSING). Roll: %!f(MISSING)."
+ "<<<< VCProcessor >>>> %!s(MISSING): setOutputROI: <%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)>"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to get camera info for port type %!@(MISSING)"
+ "<<<< VCProcessor >>>> %!s(MISSING): resetOutputCamera"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): renderer is nil"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Unable to add espresso network %!@(MISSING)"
+ "-[VCProcessor _processVideo]"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): setFramingStyle: %!d(MISSING)"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): Failed to init gaze"
+ "<<<< DeskCamSessionInputMetadata >>>> %!s(MISSING): DeskCamSessionInputMetadata: calibrationDictionary is nil."
+ "<<<< Kalman Filter >>>> %!s(MISSING): 'height' filter is nil"
+ "<<<< Kalman Filter >>>> %!s(MISSING): 'x' filter is nil"
+ "-[VCProcessor _confineOutputCameraToInputCameraFrustum:]"
+ "<<<< CinematicFramingSession >>>> %!s(MISSING): Unsupported port type for CinematicFramingSession."
+ "-[VCProcessor setOutputROI:]"
+ "-[VCProcessor resetOutputCamera]"
+ "<<<< VCProcessor >>>> %!s(MISSING): Failed to perform roll correction."
+ "<<<< VCProcessor >>>> %!s(MISSING): reset duration: %!f(MISSING)"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "<<<< CinematicFramingSessionInputMetadata >>>> %!s(MISSING): CinematicFramingSessionInputMetadata: Failed to get cameraIntrinsicMatrix from calibrationData dictionary (%!d(MISSING))."
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): CamGaze network model not found in VisionCore"
+ "-[SceneFramingEngine updateDeadbandWithSubjectRect:atTime:]"
+ "<<<< SubjectSelectionSession >>>> %!s(MISSING): VisionCore is not available. Using default parameters."
+ "-[DeskCamRenderingSession dealloc]"

```
