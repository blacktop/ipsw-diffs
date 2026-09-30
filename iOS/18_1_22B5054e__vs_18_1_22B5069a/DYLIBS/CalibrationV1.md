## CalibrationV1

> `/System/Library/VideoProcessors/CalibrationV1.bundle/CalibrationV1`

```diff

-580.11.21.1.0
-  __TEXT.__text: 0x1e640
-  __TEXT.__auth_stubs: 0x530
+580.14.3.0.0
+  __TEXT.__text: 0x1b3d0
+  __TEXT.__auth_stubs: 0x4d0
   __TEXT.__objc_methlist: 0xb00
-  __TEXT.__const: 0xe64
-  __TEXT.__cstring: 0x3a43
-  __TEXT.__oslogstring: 0xc44
-  __TEXT.__unwind_info: 0x3a8
+  __TEXT.__const: 0xe34
+  __TEXT.__cstring: 0x32aa
+  __TEXT.__unwind_info: 0x398
   __TEXT.__objc_classname: 0xef
   __TEXT.__objc_methname: 0x33b6
   __TEXT.__objc_methtype: 0x16f7

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x848
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x2a0
+  __AUTH_CONST.__auth_got: 0x270
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0xa00
+  __AUTH_CONST.__cfstring: 0x920
   __AUTH_CONST.__objc_const: 0x1cc0
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x1ec
   __DATA.__data: 0xc0
-  __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 298
-  Symbols:   133
-  CStrings:  1085
+  Symbols:   127
+  CStrings:  988
 
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
- "-[Calibration computeCalibration]"
- "-[Calibration computeInitialCalibration]"
- "-[Calibration extractParametersFromReferenceMetadata:auxiliaryMetadata:options:adaptiveCorrectionConfig:useReferenceFrame:]"
- "-[Calibration referenceMagnification]"
- "-[DupDownscaleHalfConvert AllocateResources]"
- "-[FigCalibration prewarmWithTuningParameters:]"
- "-[FigCalibration process]"
- "-[FigCalibration setOptions:]"
- "-[PyrGPU _doRPDDownscale1WithCommandBuffer:in_tex:out_tex:scaling_factor:]"
- "-[PyrGPU _downscale2XBelowWithCommandBuffer:in_tex:out_tex:scaling_factor:]"
- "-[PyrGPU _downscale2XEqualWithCommandBuffer:in_tex:out_tex:scaling_factor:]"
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
- "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): %!@(MISSING)"
- "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): Level %!d(MISSING):%!@(MISSING) -> %!d(MISSING)"
- "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): Level %!d(MISSING):%!@(MISSING) -> %!f(MISSING)"
- "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): _readKeyFloat failed"
- "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): _readKeyFloat_t failed"
- "<<<< CalibrationTuningParameters (V1) >>>> %!s(MISSING): _readKeyInteger failed"
- "<<<< FigCalibration (V1) >>>>"
- "<<<< FigCalibration (V1) >>>> %!s(MISSING): CalibrationV1 set with options %!@(MISSING)"
- "<<<< FigCalibration (V1) >>>> %!s(MISSING): CalibrationV1: Did not get tuning parameters in options."
- "<<<< FigCalibration (V1) >>>> %!s(MISSING): CalibrationV1: Tuning parameters after initialization is %!p(MISSING)."
- "<<<< FigCalibration (V1) >>>> %!s(MISSING): Retrieving parameters for config %!@(MISSING)"
- "<<<< FigCalibration (V1) >>>> %!s(MISSING): Updated tuning parameters for %!@(MISSING)"
- "<<<< FigCalibration (V1) >>>> %!s(MISSING): _keypointsCount = %!d(MISSING)"
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
- "Vaux_3x4 is NULL"
- "Vref_3x4 is NULL"
- "[SBP:DownscaleHalfConvert] %!s(MISSING): Context unavailable."
- "_readKeyFloat"
- "_readKeyFloat_t"
- "_readKeyInteger"
- "_readKeyValue"
- "_scaleTuningInADCConfig"
- "auxiliaryMetadata is nil."
- "calibration_trace"
- "calibrationv1_tuningparameters_trace"
- "camInfoByPort is nil."
- "cmdEnc is NULL"
- "com.apple.coremedia"
- "failed"
- "figcalibration_trace"
- "kFigBaseObjectError_ParamErr"
- "maybeValueFloat"
- "maybeValueFloat_t"
- "maybeValueInt"
- "optical center could not be retrieved."
- "options is nil."
- "pixelSizeMicrometers cannot be nil as calibration expects it."
- "referenceMetadata is nil."
- "sf_trace"
- "succeeded"
- "tuningParameters is nil."

```
