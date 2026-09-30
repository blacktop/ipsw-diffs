## DisparityV5

> `/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`

```diff

-587.60.10.122.3
-  __TEXT.__text: 0x2a888
-  __TEXT.__auth_stubs: 0x670
+587.60.14.122.2
+  __TEXT.__text: 0x26c20
+  __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_methlist: 0xf28
-  __TEXT.__cstring: 0x6a46
-  __TEXT.__const: 0xee0
-  __TEXT.__oslogstring: 0xe43
-  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__cstring: 0x5a1a
+  __TEXT.__const: 0xea0
+  __TEXT.__unwind_info: 0x4a0
   __TEXT.__objc_classname: 0x15a
   __TEXT.__objc_methname: 0x4b64
   __TEXT.__objc_methtype: 0x2122

   __DATA_CONST.__objc_selrefs: 0xcb0
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x340
+  __AUTH_CONST.__auth_got: 0x310
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x1aa0
+  __AUTH_CONST.__cfstring: 0x19a0
   __AUTH_CONST.__objc_const: 0x2bf8
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_ivar: 0x324
   __DATA.__data: 0x120
-  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x3c0
-  __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 402
-  Symbols:   172
-  CStrings:  1760
+  Symbols:   166
+  CStrings:  1605
 
Symbols:
+ _FigSignalErrorAt
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_note_initialize_category_with_default_work_cf
- _objc_retain
- _os_log_type_enabled
CStrings:
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "(Fig)"
- "-1"
- "-[AdaptiveClamping _initShaders]"
- "-[Calibration computeCalibration]"
- "-[Calibration computeInitialCalibration]"
- "-[Calibration extractParametersFromReferenceMetadata:auxiliaryMetadata:options:adaptiveCorrectionConfig:useReferenceFrame:]"
- "-[Calibration referenceMagnification]"
- "-[Demosaic convertLinearRGB:toLuma:]"
- "-[Demosaic demosaic2x:rawImagePixelFormat:toLuma:toRGBA:]"
- "-[Demosaic initWithMetalContext:]"
- "-[Demosaic preProcessMetadata:cameraInfoByPortType:]"
- "-[Demosaic resampleLuma:toLuma:magnification:preShift:]"
- "-[DupDownscaleHalfConvert AllocateResources]"
- "-[FigDisparityGenerator initWithCommandQueue:]"
- "-[FigDisparityGenerator prewarmWithTuningParameters:]"
- "-[FigDisparityGenerator process]"
- "-[FigDisparityGenerator setOptions:]"
- "-[GDCProcessor GDCDistort:to:parameters:commandBuffer:]"
- "-[GDCProcessor GDCDistortPixelBuffer:toPixelBuffer:parameters:]"
- "-[GDCProcessor GDCFrom:to:parameters:commandBuffer:]"
- "-[GDCProcessor GDCFromPixelBuffer:toPixelBuffer:parameters:]"
- "-[GDCProcessor compileShadersWithLib:]"
- "-[GDCProcessor initMetal]"
- "-[GDCProcessor initWithMetalContext:]"
- "-[GDCProcessor setSamplers:]"
- "-[LKTKeypointDetector _computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:]"
- "-[LKTKeypointDetector _computeFeaturesWithCommandBuffer:in_tex:out_tex:]"
- "-[LKTKeypointDetector _doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:]"
- "-[LKTKeypointDetector _downscale2XWithCommandBuffer:in_tex:out_tex:]"
- "-[LKTKeypointDetector _enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:]"
- "-[LKTKeypointDetector _enqueueKeypointsFromFlowWithCommandBuffer:in_uv_fwd_tex:in_uv_bwd_tex:in_conf_fwd_tex:in_conf_bwd_tex:out_kpt_buf:out_kpt_conf:block_size:bidirectional_error:confidence_radial_weight:confidence_minimum:out_num_keypoints:]"
- "-[LKTKeypointDetector _zeroFlowWithCommandBuffer:uv_tex:]"
- "<<<< ADC >>>> %!s(MISSING): ADC tuning: %!s(MISSING) = %!d(MISSING)"
- "<<<< ADC >>>> %!s(MISSING): ADC tuning: %!s(MISSING) = %!f(MISSING)"
- "<<<< ADC >>>> %!s(MISSING): ADC tuning: %!s(MISSING) is not present"
- "<<<< Calibration >>>>"
- "<<<< Calibration >>>> %!s(MISSING): Calibration: computing ADC full correction without distortion."
- "<<<< Calibration >>>> %!s(MISSING): CalibrationValidRadius = %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): DDF not found in metadata dictionary"
- "<<<< Calibration >>>> %!s(MISSING): Derived FOV radius of input image buffer = %!f(MISSING) mm"
- "<<<< Calibration >>>> %!s(MISSING): Detected (%!l(MISSING)u) *Deprecated* Overlap Calibration properties for %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Detected (%!l(MISSING)u) Narrow Overlap Calibration properties for %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Detected (%!l(MISSING)u) Overlap Calibration metadata for %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Detected bracketed capture; returning reference frame metadata for %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Disparity ADC pass 2 %!s(MISSING)."
- "<<<< Calibration >>>> %!s(MISSING): Extracting properties for %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Initializing calibration parameters for %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): OIS shift (pixels) x:%!f(MISSING) y:%!f(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Optical centers loaded from metadata: (%!f(MISSING), %!f(MISSING))"
- "<<<< Calibration >>>> %!s(MISSING): Pinhole focal length in pixels: %!f(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Scaled ADC config by %!f(MISSING)x from [scale tuning: %!f(MISSING) and input factor: %!f(MISSING)]"
- "<<<< Calibration >>>> %!s(MISSING): Selected (%!l(MISSING)u) Overlap Calibration properties for %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Using Buffer Scaling = [%!f(MISSING) x %!f(MISSING)]"
- "<<<< Calibration >>>> %!s(MISSING): Using SensorRawValidBufferRect = [%!f(MISSING) x %!f(MISSING)] [%!f(MISSING) x %!f(MISSING)]"
- "<<<< Calibration >>>> %!s(MISSING): Using ddf = %!f(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Using distortionOpticalCenter = %!f(MISSING) %!f(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Using focalLength = %!f(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Using opticalCenter = %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): Using rawSensorSize = [%!f(MISSING) x %!f(MISSING)]"
- "<<<< Calibration >>>> %!s(MISSING): View matrix for Auxiliary loaded from metadata:\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): View matrix for Reference loaded from metadata:\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): cameraViewMatrix = %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): focalLengthPix of Auxiliary is 0, it should not happen"
- "<<<< Calibration >>>> %!s(MISSING): gdcCoefficientsDict = %!@(MISSING)"
- "<<<< Calibration >>>> %!s(MISSING): pixelSizeMicrometers = %!@(MISSING)"
- "<<<< Disparity >>>>"
- "<<<< Disparity >>>> %!s(MISSING): Cannot instantiate FigMetalContext for prewarming"
- "<<<< Disparity >>>> %!s(MISSING): Computed inputRectificationRect: Origin - (%!f(MISSING), %!f(MISSING)), Size - (%!f(MISSING), %!f(MISSING))"
- "<<<< Disparity >>>> %!s(MISSING): Disparity set with options %!@(MISSING)"
- "<<<< Disparity >>>> %!s(MISSING): DisparityV5: Did not get tuning parameters in options."
- "<<<< Disparity >>>> %!s(MISSING): DisparityV5: Tuning parameters after initialization is %!p(MISSING)."
- "<<<< Disparity >>>> %!s(MISSING): Retrieving parameters for config %!@(MISSING)"
- "<<<< Disparity >>>> %!s(MISSING): Updated tuning parameters for %!@(MISSING)"
- "<<<< Disparity >>>> %!s(MISSING): Using provided metal command queue %!p(MISSING)"
- "<<<< DisparityAdaptiveClamping >>>>"
- "<<<< GDC >>>>"
- "<<<< GDC >>>> %!s(MISSING): GDC : Only single plane input supported"
- "<<<< STEREODISPARITY DEMOSAIC >>>>"
- "<<<< STEREODISPARITY DEMOSAIC >>>> %!s(MISSING): Demosaic init completed with no error"
- "<<<< STEREODISPARITY DEMOSAIC >>>> %!s(MISSING): Metadata for EV0 is missing for EV- reference inputs"
- "<<<< STEREODISPARITY DEMOSAIC >>>> %!s(MISSING): Missing metadata fields to compute exposure for EV0/EV-, expecting ispDGain/sensorDGain/ExposureTime/AGC."
- "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): %!@(MISSING)"
- "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): Level %!d(MISSING):%!@(MISSING) -> %!d(MISSING)"
- "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): Level %!d(MISSING):%!@(MISSING) -> %!f(MISSING)"
- "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): _readKeyFloat failed"
- "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): _readKeyFloat_t failed"
- "<<<< StereoDisparityTuningParameters (V5) >>>> %!s(MISSING): _readKeyInteger failed"
- "Could not create samplers"
- "Dimensions of SensorRawValidBufferRect in the frame metadata must be non 0."
- "Disparity tuning:Cannot find the key '%!@(MISSING)' for the level %!d(MISSING) in the plist."
- "Disparity tuning:Cannot find the key '%!@(MISSING)' in the plist."
- "Distortion optical center could not be retrieved."
- "Expected buffer scaling to be within (0.1, 10]."
- "FIGMETALCONTEXT_CHECK_ERRCODE"
- "MetadataCalibratedForBackWideFieldOfView cannot be nil as we received overlap stream properties."
- "MetadataCalibratedForNarrowerFieldOfView cannot be nil as we received overlap stream properties."
- "Overlap's calibrationValidRadius cannot be nil, expected to be in DataCalibratedForNarrowerFieldOfView"
- "PinholeCameraFocalLength is nil."
- "Timestamp is invalid"
- "Unsupported bayer format"
- "Vaux_3x4 is NULL"
- "Vref_3x4 is NULL"
- "[SBP:DownscaleHalfConvert] %!s(MISSING): Context unavailable."
- "_auxHalfResRGBATexture is NULL"
- "_mtlCommandQueue is NULL"
- "_mtlDevice is NULL"
- "_pipelineStates[DISPARITY_COMPUTE_CLAMPING] is NULL"
- "_pipelineStates[DISPARITY_COMPUTE_CLAMPING_VALUES] is NULL"
- "_pipelineStates[DISPARITY_COMPUTE_HISTOGRAM] is NULL"
- "_pipelineStates[GDC] is NULL"
- "_pipelineStates[GDC_DISTORT] is NULL"
- "_readKeyFloat"
- "_readKeyFloat_t"
- "_readKeyInteger"
- "_readKeyValue"
- "_refHalfResRGBATexture is NULL"
- "_samplers[BICUBIC_CLAMP_TO_EDGE] is NULL"
- "_samplers[LINEAR_CLAMP_TO_EDGE] is NULL"
- "_samplers[NEAREST_CLAMP_TO_EDGE] is NULL"
- "_scaleTuningInADCConfig"
- "auxiliaryMetadata is nil."
- "calibration_trace"
- "camInfoByPort is nil."
- "cmdBuffer is NULL"
- "cmdEnc is NULL"
- "disparity_trace"
- "disparityclamping_trace"
- "downscaleCommandBuffer is NULL"
- "failed"
- "gdcCommandBuffer is NULL"
- "inputTexture is NULL"
- "kCMBaseObjectError_AllocationFailed"
- "kCMBaseObjectError_ParamErr"
- "kFigBaseObjectError_ParamErr"
- "maybeValueFloat"
- "maybeValueFloat_t"
- "maybeValueInt"
- "metalContext is NULL"
- "metalLib is NULL"
- "optical center could not be retrieved."
- "options is nil."
- "outputTexture is NULL"
- "parameters is NULL"
- "pipelineDescriptor is NULL"
- "pixelSizeMicrometers cannot be nil as calibration expects it."
- "referenceMetadata is nil."
- "renderCommand is NULL"
- "renderPassDescriptor is NULL"
- "samplerDescriptor is NULL"
- "sf_trace"
- "stereodisparity_demosaic_trace"
- "stereodisparity_tuningparameters_trace"
- "succeeded"
- "textureDescriptor is NULL"

```
