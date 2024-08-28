## DisparityV5

> `/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0x268e4
-  __TEXT.__auth_stubs: 0x610
+580.2.0.0.0
+  __TEXT.__text: 0x2a468
+  __TEXT.__auth_stubs: 0x670
   __TEXT.__objc_methlist: 0xf18
-  __TEXT.__cstring: 0x5a07
-  __TEXT.__const: 0xea0
-  __TEXT.__unwind_info: 0x4a0
+  __TEXT.__cstring: 0x69df
+  __TEXT.__const: 0xee0
+  __TEXT.__oslogstring: 0xdf9
+  __TEXT.__unwind_info: 0x4a8
   __TEXT.__objc_classname: 0x140
   __TEXT.__objc_methname: 0x4a28
   __TEXT.__objc_methtype: 0x2058

   __DATA_CONST.__objc_selrefs: 0xc98
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_got: 0x340
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x1940
+  __AUTH_CONST.__cfstring: 0x1a40
   __AUTH_CONST.__objc_const: 0x2a88
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_ivar: 0x320
   __DATA.__data: 0xc0
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 401
-  Symbols:   166
-  CStrings:  1584
+  Symbols:   172
+  CStrings:  1736
 
Symbols:
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ __os_log_send_and_compose_impl
+ _objc_retain
+ _fig_note_initialize_category_with_default_work_cf
+ _FigSignalErrorAt3
+ _os_log_type_enabled
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _FigSignalErrorAt
CStrings:
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): Level %!d(MISSING):%!@(MISSING) -> %!d(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Using Buffer Scaling = [%!f(MISSING) x %!f(MISSING)]"
+ "_scaleTuningInADCConfig"
+ "<<<< Disparity >>>>"
+ "<<<< Calibration >>>> %!s(MISSING): Selected (%!l(MISSING)u) Overlap Calibration properties for %!@(MISSING)"
+ "-[LKTKeypointDetector _enqueueKeypointsFromFlowWithCommandBuffer:in_uv_fwd_tex:in_uv_bwd_tex:in_conf_fwd_tex:in_conf_bwd_tex:out_kpt_buf:out_kpt_conf:block_size:bidirectional_error:confidence_radial_weight:confidence_minimum:out_num_keypoints:]"
+ "_readKeyFloat"
+ "stereodisparity_demosaic_trace"
+ "_refHalfResRGBATexture is NULL"
+ "<<<< STEREODISPARITY DEMOSAIC >>>> %!s(MISSING): Metadata for EV0 is missing for EV- reference inputs"
+ "pixelSizeMicrometers cannot be nil as calibration expects it."
+ "-[Demosaic resampleLuma:toLuma:magnification:preShift:]"
+ "<<<< Calibration >>>> %!s(MISSING): pixelSizeMicrometers = %!@(MISSING)"
+ "Disparity tuning:Cannot find the key '%!@(MISSING)' in the plist."
+ "disparityclamping_trace"
+ "<<<< Calibration >>>> %!s(MISSING): Detected (%!l(MISSING)u) Narrow Overlap Calibration properties for %!@(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Using opticalCenter = %!@(MISSING)"
+ "<<<< STEREODISPARITY DEMOSAIC >>>> %!s(MISSING): Missing metadata fields to compute exposure for EV0/EV-, expecting ispDGain/sensorDGain/ExposureTime/AGC."
+ "-[AdaptiveClamping _initShaders]"
+ "maybeValueInt"
+ "<<<< Calibration >>>> %!s(MISSING): View matrix for Auxiliary loaded from metadata:\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)"
+ "-[GDCProcessor GDCDistort:to:parameters:commandBuffer:]"
+ "_samplers[LINEAR_CLAMP_TO_EDGE] is NULL"
+ "Expected buffer scaling to be within (0.1, 10]."
+ "<<<< Calibration >>>> %!s(MISSING): Scaled ADC config by %!f(MISSING)x from [scale tuning: %!f(MISSING) and input factor: %!f(MISSING)]"
+ "_pipelineStates[GDC_DISTORT] is NULL"
+ "cmdBuffer is NULL"
+ "<<<< Disparity >>>> %!s(MISSING): Computed inputRectificationRect: Origin - (%!f(MISSING), %!f(MISSING)), Size - (%!f(MISSING), %!f(MISSING))"
+ "_pipelineStates[DISPARITY_COMPUTE_CLAMPING_VALUES] is NULL"
+ "<<<< Calibration >>>> %!s(MISSING): Using focalLength = %!f(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Calibration: computing ADC full correction without distortion."
+ "_readKeyValue"
+ "referenceMetadata is nil."
+ "<<<< ADC >>>> %!s(MISSING): ADC tuning: %!s(MISSING) is not present"
+ "-[Calibration referenceMagnification]"
+ "-[GDCProcessor initWithMetalContext:]"
+ "_samplers[BICUBIC_CLAMP_TO_EDGE] is NULL"
+ "-[FigDisparityGenerator setOptions:]"
+ "_auxHalfResRGBATexture is NULL"
+ "failed"
+ "maybeValueFloat"
+ "<<<< Calibration >>>> %!s(MISSING): View matrix for Reference loaded from metadata:\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)"
+ "-[DupDownscaleHalfConvert AllocateResources]"
+ "-[GDCProcessor GDCDistortPixelBuffer:toPixelBuffer:parameters:]"
+ "<<<< Calibration >>>> %!s(MISSING): Derived FOV radius of input image buffer = %!f(MISSING) mm"
+ "<<<< Calibration >>>> %!s(MISSING): Using ddf = %!f(MISSING)"
+ "camInfoByPort is nil."
+ "pipelineDescriptor is NULL"
+ "<<<< STEREODISPARITY DEMOSAIC >>>> %!s(MISSING): Demosaic init completed with no error"
+ "renderCommand is NULL"
+ "optical center could not be retrieved."
+ "options is nil."
+ "<<<< Calibration >>>> %!s(MISSING): Detected bracketed capture; returning reference frame metadata for %!@(MISSING)"
+ "MetadataCalibratedForBackWideFieldOfView cannot be nil as we received overlap stream properties."
+ "calibration_trace"
+ "_pipelineStates[DISPARITY_COMPUTE_HISTOGRAM] is NULL"
+ "<<<< Calibration >>>> %!s(MISSING): Detected (%!l(MISSING)u) Overlap Calibration metadata for %!@(MISSING)"
+ "_readKeyInteger"
+ "samplerDescriptor is NULL"
+ "Dimensions of SensorRawValidBufferRect in the frame metadata must be non 0."
+ "<<<< Disparity >>>> %!s(MISSING): DisparityV5: Did not get tuning parameters in options."
+ "downscaleCommandBuffer is NULL"
+ "<<<< Calibration >>>> %!s(MISSING): Optical centers loaded from metadata: (%!f(MISSING), %!f(MISSING))"
+ "-[GDCProcessor initMetal]"
+ "renderPassDescriptor is NULL"
+ "<<<< Disparity >>>> %!s(MISSING): Using provided metal command queue %!p(MISSING)"
+ "-[GDCProcessor setSamplers:]"
+ "<<<< Calibration >>>> %!s(MISSING): Initializing calibration parameters for %!@(MISSING)"
+ "<<<< Disparity >>>> %!s(MISSING): DisparityV5: Tuning parameters after initialization is %!p(MISSING)."
+ "Unsupported bayer format"
+ "<<<< Disparity >>>> %!s(MISSING): Updated tuning parameters for %!@(MISSING)"
+ "<<<< Disparity >>>> %!s(MISSING): Disparity set with options %!@(MISSING)"
+ "[SBP:DownscaleHalfConvert] %!s(MISSING): Context unavailable."
+ "-[Calibration computeCalibration]"
+ "Disparity tuning:Cannot find the key '%!@(MISSING)' for the level %!d(MISSING) in the plist."
+ "<<<< Calibration >>>> %!s(MISSING): Using SensorRawValidBufferRect = [%!f(MISSING) x %!f(MISSING)] [%!f(MISSING) x %!f(MISSING)]"
+ "-[GDCProcessor GDCFrom:to:parameters:commandBuffer:]"
+ "<<<< Calibration >>>> %!s(MISSING): focalLengthPix of Auxiliary is 0, it should not happen"
+ "metalLib is NULL"
+ "sf_trace"
+ "<<<< DisparityAdaptiveClamping >>>>"
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): _readKeyFloat failed"
+ "_pipelineStates[GDC] is NULL"
+ "-[Demosaic preProcessMetadata:cameraInfoByPortType:]"
+ "-[GDCProcessor compileShadersWithLib:]"
+ "<<<< Calibration >>>> %!s(MISSING): Using distortionOpticalCenter = %!f(MISSING) %!f(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Detected (%!l(MISSING)u) *Deprecated* Overlap Calibration properties for %!@(MISSING)"
+ "-[LKTKeypointDetector _computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:]"
+ "<<<< Calibration >>>> %!s(MISSING): Extracting properties for %!@(MISSING)"
+ "_mtlCommandQueue is NULL"
+ "<<<< Calibration >>>>"
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): %!@(MISSING)"
+ "Could not create samplers"
+ "<<<< GDC >>>>"
+ "<<<< GDC >>>> %!s(MISSING): GDC : Only single plane input supported"
+ "_samplers[NEAREST_CLAMP_TO_EDGE] is NULL"
+ "Overlap's calibrationValidRadius cannot be nil, expected to be in DataCalibratedForNarrowerFieldOfView"
+ "<<<< Calibration >>>> %!s(MISSING): CalibrationValidRadius = %!@(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): DDF not found in metadata dictionary"
+ "<<<< Calibration >>>> %!s(MISSING): cameraViewMatrix = %!@(MISSING)"
+ "-[LKTKeypointDetector _downscale2XWithCommandBuffer:in_tex:out_tex:]"
+ "<<<< Calibration >>>> %!s(MISSING): OIS shift (pixels) x:%!f(MISSING) y:%!f(MISSING)"
+ "-[LKTKeypointDetector _zeroFlowWithCommandBuffer:uv_tex:]"
+ "-[FigDisparityGenerator process]"
+ "<<<< Calibration >>>> %!s(MISSING): gdcCoefficientsDict = %!@(MISSING)"
+ "<<<< ADC >>>> %!s(MISSING): ADC tuning: %!s(MISSING) = %!f(MISSING)"
+ "<<<< ADC >>>> %!s(MISSING): ADC tuning: %!s(MISSING) = %!d(MISSING)"
+ "_mtlDevice is NULL"
+ "Vref_3x4 is NULL"
+ "stereodisparity_tuningparameters_trace"
+ "disparity_trace"
+ "(Fig)"
+ "<<<< Disparity >>>> %!s(MISSING): Retrieving parameters for config %!@(MISSING)"
+ "gdcCommandBuffer is NULL"
+ "MetadataCalibratedForNarrowerFieldOfView cannot be nil as we received overlap stream properties."
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): Level %!d(MISSING):%!@(MISSING) -> %!f(MISSING)"
+ "-[LKTKeypointDetector _enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:]"
+ "-1"
+ "succeeded"
+ "-[LKTKeypointDetector _computeFeaturesWithCommandBuffer:in_tex:out_tex:]"
+ "-[LKTKeypointDetector _doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:]"
+ "-[Demosaic convertLinearRGB:toLuma:]"
+ "inputTexture is NULL"
+ "kCMBaseObjectError_AllocationFailed"
+ "<<<< Calibration >>>> %!s(MISSING): Pinhole focal length in pixels: %!f(MISSING)"
+ "maybeValueFloat_t"
+ "metalContext is NULL"
+ "_readKeyFloat_t"
+ "kCMBaseObjectError_ParamErr"
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): _readKeyInteger failed"
+ "parameters is NULL"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "textureDescriptor is NULL"
+ "-[GDCProcessor GDCFromPixelBuffer:toPixelBuffer:parameters:]"
+ "<<<< Calibration >>>> %!s(MISSING): Disparity ADC pass 2 %!s(MISSING)."
+ "<<<< STEREODISPARITY DEMOSAIC >>>>"
+ "PinholeCameraFocalLength is nil."
+ "-[FigDisparityGenerator initWithCommandQueue:]"
+ "outputTexture is NULL"
+ "-[Calibration extractParametersFromReferenceMetadata:auxiliaryMetadata:options:adaptiveCorrectionConfig:useReferenceFrame:]"
+ "<<<< Calibration >>>> %!s(MISSING): Using rawSensorSize = [%!f(MISSING) x %!f(MISSING)]"
+ "auxiliaryMetadata is nil."
+ "-[Demosaic initWithMetalContext:]"
+ "-[Demosaic demosaic2x:rawImagePixelFormat:toLuma:toRGBA:]"
+ "Distortion optical center could not be retrieved."
+ "Vaux_3x4 is NULL"
+ "cmdEnc is NULL"
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): _readKeyFloat_t failed"
+ "Timestamp is invalid"
+ "_pipelineStates[DISPARITY_COMPUTE_CLAMPING] is NULL"
+ "kFigBaseObjectError_ParamErr"
+ "-[Calibration computeInitialCalibration]"

```
