## DisparityV5

> `/System/Library/VideoProcessors/DisparityV5.bundle/DisparityV5`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x28984
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x112c
-  __TEXT.__cstring: 0x5a11
-  __TEXT.__const: 0xf30
-  __TEXT.__unwind_info: 0x518
+650.0.0.122.4
+  __TEXT.__text: 0x2c558
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_methlist: 0x116c
+  __TEXT.__cstring: 0x69a8
+  __TEXT.__const: 0xf70
+  __TEXT.__oslogstring: 0xef9
+  __TEXT.__unwind_info: 0x580
   __TEXT.__objc_classname: 0x15a
-  __TEXT.__objc_methname: 0x4b64
+  __TEXT.__objc_methname: 0x4bef
   __TEXT.__objc_methtype: 0x2122
-  __TEXT.__objc_stubs: 0x2120
-  __DATA_CONST.__got: 0x1b0
-  __DATA_CONST.__const: 0x68
+  __TEXT.__objc_stubs: 0x2100
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__const: 0x88
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd68
+  __DATA_CONST.__objc_selrefs: 0xd60
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x19a0
-  __AUTH_CONST.__objc_const: 0x2838
+  __AUTH_CONST.__auth_got: 0x350
+  __AUTH_CONST.__const: 0x320
+  __AUTH_CONST.__cfstring: 0x1a20
+  __AUTH_CONST.__objc_const: 0x2898
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __DATA.__objc_ivar: 0x324
+  __DATA.__objc_ivar: 0x32c
   __DATA.__data: 0x120
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x3c0
+  __DATA_DIRTY.__common: 0x50
+  __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E6EABCA9-B557-35E1-A043-7034D7D46BEB
-  Functions: 813
-  Symbols:   166
-  CStrings:  1803
+  UUID: CE1056E8-193D-3CFD-A6B8-475F4B51069B
+  Functions: 839
+  Symbols:   173
+  CStrings:  1968
 
Symbols:
+ _FigSignalErrorAt3
+ _OBJC_CLASS_$_MTLRenderPipelineColorAttachmentDescriptor
+ __os_log_impl
+ __os_log_send_and_compose_impl
+ _dispatch_once
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _objc_release_x1
+ _objc_retain
+ _os_log_create
+ _os_log_type_enabled
- _FigSignalErrorAt
- _NSLog
- _OBJC_CLASS_$_MTLRenderPipelineDescriptor
- ___stack_chk_fail
- ___stack_chk_guard
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "(Fig)"
+ "-1"
+ "-[AdaptiveClamping _initShaders]"
+ "-[Calibration computeCalibration]"
+ "-[Calibration computeInitialCalibration]"
+ "-[Calibration extractParametersFromReferenceMetadata:auxiliaryMetadata:options:adaptiveCorrectionConfig:useReferenceFrame:]"
+ "-[Calibration referenceMagnification]"
+ "-[Demosaic convertLinearRGB:toLuma:]"
+ "-[Demosaic demosaic2x:rawImagePixelFormat:toLuma:toRGBA:]"
+ "-[Demosaic initWithMetalContext:]"
+ "-[Demosaic preProcessMetadata:cameraInfoByPortType:]"
+ "-[Demosaic resampleLuma:toLuma:magnification:preShift:]"
+ "-[DupDownscaleHalfConvert AllocateResources]"
+ "-[FigDisparityGenerator initWithCommandQueue:]"
+ "-[FigDisparityGenerator prewarmWithTuningParameters:]"
+ "-[FigDisparityGenerator process]"
+ "-[FigDisparityGenerator setOptions:]"
+ "-[GDCProcessor GDCDistort:to:parameters:commandBuffer:]"
+ "-[GDCProcessor GDCDistortPixelBuffer:toPixelBuffer:parameters:]"
+ "-[GDCProcessor GDCFrom:to:parameters:commandBuffer:]"
+ "-[GDCProcessor GDCFromPixelBuffer:toPixelBuffer:parameters:]"
+ "-[GDCProcessor compileShadersWithLib:]"
+ "-[GDCProcessor initMetal]"
+ "-[GDCProcessor initWithMetalContext:]"
+ "-[GDCProcessor setSamplers:]"
+ "-[LKTKeypointDetector _computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:]"
+ "-[LKTKeypointDetector _computeFeaturesWithCommandBuffer:in_tex:out_tex:]"
+ "-[LKTKeypointDetector _doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:]"
+ "-[LKTKeypointDetector _downscale2XWithCommandBuffer:in_tex:out_tex:]"
+ "-[LKTKeypointDetector _enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:]"
+ "-[LKTKeypointDetector _enqueueKeypointsFromFlowWithCommandBuffer:in_uv_fwd_tex:in_uv_bwd_tex:in_conf_fwd_tex:in_conf_bwd_tex:out_kpt_buf:out_kpt_conf:block_size:bidirectional_error:confidence_radial_weight:confidence_minimum:out_num_keypoints:]"
+ "-[LKTKeypointDetector _zeroFlowWithCommandBuffer:uv_tex:]"
+ "<<<< ADC >>>> %s: ADC tuning: %s = %d"
+ "<<<< ADC >>>> %s: ADC tuning: %s = %f"
+ "<<<< ADC >>>> %s: ADC tuning: %s is not present"
+ "<<<< Calibration >>>>"
+ "<<<< Calibration >>>> %s: Calibration: computing ADC full correction without distortion."
+ "<<<< Calibration >>>> %s: CalibrationValidRadius = %@"
+ "<<<< Calibration >>>> %s: DDF not found in metadata dictionary"
+ "<<<< Calibration >>>> %s: Derived FOV radius of input image buffer = %.5f mm"
+ "<<<< Calibration >>>> %s: Detected (%lu) *Deprecated* Overlap Calibration properties for %@"
+ "<<<< Calibration >>>> %s: Detected (%lu) Narrow Overlap Calibration properties for %@"
+ "<<<< Calibration >>>> %s: Detected (%lu) Overlap Calibration metadata for %@"
+ "<<<< Calibration >>>> %s: Detected bracketed capture; returning reference frame metadata for %@"
+ "<<<< Calibration >>>> %s: Disparity ADC pass 2 %s."
+ "<<<< Calibration >>>> %s: Extracting properties for %@"
+ "<<<< Calibration >>>> %s: Initializing calibration parameters for %@"
+ "<<<< Calibration >>>> %s: OIS shift (pixels) x:%f y:%f"
+ "<<<< Calibration >>>> %s: Optical centers loaded from metadata: (%f, %f)"
+ "<<<< Calibration >>>> %s: Pinhole focal length in pixels: %f"
+ "<<<< Calibration >>>> %s: Scaled ADC config by %.2fx from [scale tuning: %.2f and input factor: %.2f]"
+ "<<<< Calibration >>>> %s: Selected (%lu) Overlap Calibration properties for %@"
+ "<<<< Calibration >>>> %s: Using Buffer Scaling = [%f x %f]"
+ "<<<< Calibration >>>> %s: Using SensorRawValidBufferRect = [%f x %f] [%f x %f]"
+ "<<<< Calibration >>>> %s: Using ddf = %f"
+ "<<<< Calibration >>>> %s: Using distortionOpticalCenter = %f %f"
+ "<<<< Calibration >>>> %s: Using focalLength = %.5f"
+ "<<<< Calibration >>>> %s: Using opticalCenter = %@"
+ "<<<< Calibration >>>> %s: Using rawSensorSize = [%f x %f]"
+ "<<<< Calibration >>>> %s: View matrix for Auxiliary loaded from metadata:\n%10.7f %10.7f %10.7f %10.7f\n%10.7f %10.7f %10.7f %10.7f\n%10.7f %10.7f %10.7f %10.7f"
+ "<<<< Calibration >>>> %s: View matrix for Reference loaded from metadata:\n%10.7f %10.7f %10.7f %10.7f\n%10.7f %10.7f %10.7f %10.7f\n%10.7f %10.7f %10.7f %10.7f"
+ "<<<< Calibration >>>> %s: cameraViewMatrix = %@"
+ "<<<< Calibration >>>> %s: focalLengthPix of Auxiliary is 0, it should not happen"
+ "<<<< Calibration >>>> %s: gdcCoefficientsDict = %@"
+ "<<<< Calibration >>>> %s: pixelSizeMicrometers = %@"
+ "<<<< Disparity >>>>"
+ "<<<< Disparity >>>> %s: Cannot instantiate FigMetalContext for prewarming"
+ "<<<< Disparity >>>> %s: Computed inputRectificationRect: Origin - (%f, %f), Size - (%f, %f)"
+ "<<<< Disparity >>>> %s: Disparity set with options %@"
+ "<<<< Disparity >>>> %s: DisparityV5: Did not get tuning parameters in options."
+ "<<<< Disparity >>>> %s: DisparityV5: Tuning parameters after initialization is %p."
+ "<<<< Disparity >>>> %s: Retrieving parameters for config %@"
+ "<<<< Disparity >>>> %s: Updated tuning parameters for %@"
+ "<<<< Disparity >>>> %s: Using provided metal command queue %p"
+ "<<<< DisparityAdaptiveClamping >>>>"
+ "<<<< GDC >>>>"
+ "<<<< GDC >>>> %s: GDC : Only single plane input supported"
+ "<<<< STEREODISPARITY DEMOSAIC >>>>"
+ "<<<< STEREODISPARITY DEMOSAIC >>>> %s: Demosaic init completed with no error"
+ "<<<< STEREODISPARITY DEMOSAIC >>>> %s: Metadata for EV0 is missing for EV- reference inputs"
+ "<<<< STEREODISPARITY DEMOSAIC >>>> %s: Missing metadata fields to compute exposure for EV0/EV-, expecting ispDGain/sensorDGain/ExposureTime/AGC."
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %s: %@"
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %s: Level %d:%@ -> %d"
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %s: Level %d:%@ -> %f"
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %s: _readKeyFloat failed"
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %s: _readKeyFloat_t failed"
+ "<<<< StereoDisparityTuningParameters (V5) >>>> %s: _readKeyInteger failed"
+ "AGC is greater than the maximal value"
+ "Could not create samplers"
+ "Dimensions of SensorRawValidBufferRect in the frame metadata must be non 0."
+ "Disparity tuning:Cannot find the key '%@' for the level %d in the plist."
+ "Disparity tuning:Cannot find the key '%@' in the plist."
+ "Distortion optical center could not be retrieved."
+ "Expected buffer scaling to be within (0.1, 10]."
+ "MaxAnalogGain"
+ "MetadataCalibratedForBackWideFieldOfView cannot be nil as we received overlap stream properties."
+ "MetadataCalibratedForNarrowerFieldOfView cannot be nil as we received overlap stream properties."
+ "Overlap's calibrationValidRadius cannot be nil, expected to be in DataCalibratedForNarrowerFieldOfView"
+ "PinholeCameraFocalLength is nil."
+ "Tf,N,V_maxAnalogGain"
+ "Tf,R,N,V_maxAnalogGain"
+ "Timestamp is invalid"
+ "Unsupported bayer format"
+ "Vaux_3x4 is NULL"
+ "Vref_3x4 is NULL"
+ "[SBP:DownscaleHalfConvert] %s: Context unavailable."
+ "_auxHalfResRGBATexture is NULL"
+ "_demosaic:andPreshift:tuningParameters:"
+ "_maxAnalogGain"
+ "_maxAnalogGain > 0.0f"
+ "_maxAnalogGain not set"
+ "_metadataParameters.sensorAGC <= _maxAnalogGain"
+ "_mtlCommandQueue is NULL"
+ "_mtlDevice is NULL"
+ "_pipelineStates[DISPARITY_COMPUTE_CLAMPING] is NULL"
+ "_pipelineStates[DISPARITY_COMPUTE_CLAMPING_VALUES] is NULL"
+ "_pipelineStates[DISPARITY_COMPUTE_HISTOGRAM] is NULL"
+ "_pipelineStates[GDC] is NULL"
+ "_pipelineStates[GDC_DISTORT] is NULL"
+ "_readKeyFloat"
+ "_readKeyFloat_t"
+ "_readKeyInteger"
+ "_readKeyValue"
+ "_refHalfResRGBATexture is NULL"
+ "_samplers[BICUBIC_CLAMP_TO_EDGE] is NULL"
+ "_samplers[LINEAR_CLAMP_TO_EDGE] is NULL"
+ "_samplers[NEAREST_CLAMP_TO_EDGE] is NULL"
+ "_scaleTuningInADCConfig"
+ "arrayWithObjects:count:"
+ "auxiliaryMetadata is nil."
+ "calibration_trace"
+ "camInfoByPort is nil."
+ "cmdBuffer is NULL"
+ "cmdEnc is NULL"
+ "disparity_trace"
+ "disparityclamping_trace"
+ "downscaleCommandBuffer is NULL"
+ "failed"
+ "gdcCommandBuffer is NULL"
+ "inputTexture is NULL"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "legacyLog"
+ "maxAnalogGain"
+ "maybeValueFloat"
+ "maybeValueFloat_t"
+ "maybeValueInt"
+ "metalContext is NULL"
+ "metalLib is NULL"
+ "optical center could not be retrieved."
+ "options is nil."
+ "outputTexture is NULL"
+ "parameters is NULL"
+ "pixelSizeMicrometers cannot be nil as calibration expects it."
+ "readMaxAnalogGain:isUpdating:"
+ "referenceMetadata is nil."
+ "renderCommand is NULL"
+ "renderPassDescriptor is NULL"
+ "renderPipelineStateForVertexFunction:vertexDescriptor:fragmentFunction:constants:colorAttachmentDescriptorArrray:"
+ "samplerDescriptor is NULL"
+ "setDefaultMaxAnalogGain"
+ "setMaxAnalogGain:"
+ "sf_trace"
+ "stereodisparity_demosaic_trace"
+ "stereodisparity_tuningparameters_trace"
+ "succeeded"
+ "textureDescriptor is NULL"
+ "v8@?0"
- "AGC is greater than the maximal value 8.0"
- "_demosaic:andPreshift:"
- "_metadataParameters.sensorAGC <= agc_gains.y"
- "fullRangeVertexDesc"
- "newRenderPipelineStateWithDescriptor:error:"
- "pipelineLibrary"
- "setFragmentFunction:"
- "setPipelineLibrary:"
- "setVertexDescriptor:"
- "setVertexFunction:"

```
