## CalibrationV1

> `/System/Library/VideoProcessors/CalibrationV1.bundle/CalibrationV1`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0x1b3c4
-  __TEXT.__auth_stubs: 0x4d0
+580.2.0.0.0
+  __TEXT.__text: 0x1e634
+  __TEXT.__auth_stubs: 0x530
   __TEXT.__objc_methlist: 0xb00
-  __TEXT.__const: 0xe34
-  __TEXT.__cstring: 0x32aa
-  __TEXT.__unwind_info: 0x398
+  __TEXT.__const: 0xe64
+  __TEXT.__cstring: 0x3a28
+  __TEXT.__oslogstring: 0xc44
+  __TEXT.__unwind_info: 0x3a8
   __TEXT.__objc_classname: 0xef
   __TEXT.__objc_methname: 0x33b6
   __TEXT.__objc_methtype: 0x16f7

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x848
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x270
+  __AUTH_CONST.__auth_got: 0x2a0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x920
+  __AUTH_CONST.__cfstring: 0xa00
   __AUTH_CONST.__objc_const: 0x1cc0
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x1ec
   __DATA.__data: 0xc0
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 298
-  Symbols:   127
-  CStrings:  988
+  Symbols:   133
+  CStrings:  1085
 
Symbols:
+ _fig_note_initialize_category_with_default_work_cf
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _objc_retain
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _os_log_type_enabled
- _FigSignalErrorAt
CStrings:
+ "<<<< Calibration >>>> %!s(MISSING): Using focalLength = %!f(MISSING)"
+ "Distortion optical center could not be retrieved."
+ "<<<< Calibration >>>> %!s(MISSING): Detected bracketed capture; returning reference frame metadata for %!@(MISSING)"
+ "[SBP:DownscaleHalfConvert] %!s(MISSING): Context unavailable."
+ "<<<< Calibration >>>> %!s(MISSING): Using rawSensorSize = [%!f(MISSING) x %!f(MISSING)]"
+ "<<<< Calibration >>>> %!s(MISSING): Using distortionOpticalCenter = %!f(MISSING) %!f(MISSING)"
+ "Vref_3x4 is NULL"
+ "kFigBaseObjectError_ParamErr"
+ "PinholeCameraFocalLength is nil."
+ "Disparity tuning:Cannot find the key '%!@(MISSING)' for the level %!d(MISSING) in the plist."
+ "<<<< FigCalibration (V1) >>>> %!s(MISSING): _keypointsCount = %!d(MISSING)"
+ "failed"
+ "-[FigCalibration prewarmWithTuningParameters:]"
+ "MetadataCalibratedForNarrowerFieldOfView cannot be nil as we received overlap stream properties."
+ "<<<< Calibration >>>> %!s(MISSING): Detected (%!l(MISSING)u) Narrow Overlap Calibration properties for %!@(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Derived FOV radius of input image buffer = %!f(MISSING) mm"
+ "<<<< FigCalibration (V1) >>>> %!s(MISSING): CalibrationV1: Did not get tuning parameters in options."
+ "_scaleTuningInADCConfig"
+ "_readKeyValue"
+ "<<<< Calibration >>>> %!s(MISSING): View matrix for Auxiliary loaded from metadata:\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)"
+ "Dimensions of SensorRawValidBufferRect in the frame metadata must be non 0."
+ "<<<< FigCalibration (V1) >>>> %!s(MISSING): Retrieving parameters for config %!@(MISSING)"
+ "<<<< Calibration >>>>"
+ "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): Level %!d(MISSING):%!@(MISSING) -> %!f(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Using Buffer Scaling = [%!f(MISSING) x %!f(MISSING)]"
+ "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): _readKeyFloat_t failed"
+ "<<<< ADC >>>> %!s(MISSING): ADC tuning: %!s(MISSING) is not present"
+ "-[PyrGPU _doRPDDownscale1WithCommandBuffer:in_tex:out_tex:scaling_factor:]"
+ "<<<< FigCalibration (V1) >>>> %!s(MISSING): CalibrationV1: Tuning parameters after initialization is %!p(MISSING)."
+ "Overlap's calibrationValidRadius cannot be nil, expected to be in DataCalibratedForNarrowerFieldOfView"
+ "-[Calibration extractParametersFromReferenceMetadata:auxiliaryMetadata:options:adaptiveCorrectionConfig:useReferenceFrame:]"
+ "<<<< Calibration >>>> %!s(MISSING): View matrix for Reference loaded from metadata:\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)\n%!f(MISSING) %!f(MISSING) %!f(MISSING) %!f(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Selected (%!l(MISSING)u) Overlap Calibration properties for %!@(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): pixelSizeMicrometers = %!@(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): DDF not found in metadata dictionary"
+ "<<<< ADC >>>> %!s(MISSING): ADC tuning: %!s(MISSING) = %!f(MISSING)"
+ "options is nil."
+ "<<<< Calibration >>>> %!s(MISSING): Using ddf = %!f(MISSING)"
+ "-[FigCalibration setOptions:]"
+ "<<<< ADC >>>> %!s(MISSING): ADC tuning: %!s(MISSING) = %!d(MISSING)"
+ "MetadataCalibratedForBackWideFieldOfView cannot be nil as we received overlap stream properties."
+ "succeeded"
+ "tuningParameters is nil."
+ "maybeValueFloat"
+ "-[FigCalibration process]"
+ "-[PyrGPU _downscale2XEqualWithCommandBuffer:in_tex:out_tex:scaling_factor:]"
+ "referenceMetadata is nil."
+ "<<<< Calibration >>>> %!s(MISSING): focalLengthPix of Auxiliary is 0, it should not happen"
+ "-[Calibration computeInitialCalibration]"
+ "camInfoByPort is nil."
+ "<<<< Calibration >>>> %!s(MISSING): OIS shift (pixels) x:%!f(MISSING) y:%!f(MISSING)"
+ "_readKeyFloat"
+ "<<<< Calibration >>>> %!s(MISSING): CalibrationValidRadius = %!@(MISSING)"
+ "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): _readKeyFloat failed"
+ "auxiliaryMetadata is nil."
+ "-[PyrGPU _downscale2XBelowWithCommandBuffer:in_tex:out_tex:scaling_factor:]"
+ "<<<< FigCalibration (V1) >>>> %!s(MISSING): CalibrationV1 set with options %!@(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Detected (%!l(MISSING)u) *Deprecated* Overlap Calibration properties for %!@(MISSING)"
+ "Vaux_3x4 is NULL"
+ "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): %!@(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Initializing calibration parameters for %!@(MISSING)"
+ "<<<< FigCalibration (V1) >>>>"
+ "-[DupDownscaleHalfConvert AllocateResources]"
+ "figcalibration_trace"
+ "-[Calibration referenceMagnification]"
+ "<<<< Calibration >>>> %!s(MISSING): cameraViewMatrix = %!@(MISSING)"
+ "<<<< FigCalibration (V1) >>>> %!s(MISSING): Updated tuning parameters for %!@(MISSING)"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Scaled ADC config by %!f(MISSING)x from [scale tuning: %!f(MISSING) and input factor: %!f(MISSING)]"
+ "<<<< Calibration >>>> %!s(MISSING): Pinhole focal length in pixels: %!f(MISSING)"
+ "sf_trace"
+ "_readKeyInteger"
+ "calibrationv1_tuningparameters_trace"
+ "-[Calibration computeCalibration]"
+ "cmdEnc is NULL"
+ "pixelSizeMicrometers cannot be nil as calibration expects it."
+ "calibration_trace"
+ "maybeValueInt"
+ "<<<< Calibration >>>> %!s(MISSING): Calibration: computing ADC full correction without distortion."
+ "<<<< Calibration >>>> %!s(MISSING): Using SensorRawValidBufferRect = [%!f(MISSING) x %!f(MISSING)] [%!f(MISSING) x %!f(MISSING)]"
+ "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): Level %!d(MISSING):%!@(MISSING) -> %!d(MISSING)"
+ "<<<< Calibration >>>> %!s(MISSING): Using opticalCenter = %!@(MISSING)"
+ "com.apple.coremedia"
+ "-1"
+ "<<<< Calibration >>>> %!s(MISSING): Disparity ADC pass 2 %!s(MISSING)."
+ "Disparity tuning:Cannot find the key '%!@(MISSING)' in the plist."
+ "<<<< Calibration >>>> %!s(MISSING): Detected (%!l(MISSING)u) Overlap Calibration metadata for %!@(MISSING)"
+ "Expected buffer scaling to be within (0.1, 10]."
+ "Timestamp is invalid"
+ "maybeValueFloat_t"
+ "<<<< Calibration >>>> %!s(MISSING): Optical centers loaded from metadata: (%!f(MISSING), %!f(MISSING))"
+ "(Fig)"
+ "<<<< Calibration >>>> %!s(MISSING): gdcCoefficientsDict = %!@(MISSING)"
+ "_readKeyFloat_t"
+ "<<<< Calibration >>>> %!s(MISSING): Extracting properties for %!@(MISSING)"
+ "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): _readKeyInteger failed"
+ "optical center could not be retrieved."

```
