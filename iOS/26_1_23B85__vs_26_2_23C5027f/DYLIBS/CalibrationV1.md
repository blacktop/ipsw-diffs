## CalibrationV1

> `/System/Library/VideoProcessors/CalibrationV1.bundle/CalibrationV1`

```diff

-664.42.7.0.1
-  __TEXT.__text: 0x1cb34
-  __TEXT.__auth_stubs: 0x520
+664.60.5.0.1
+  __TEXT.__text: 0x1f828
+  __TEXT.__auth_stubs: 0x570
   __TEXT.__objc_methlist: 0xcac
-  __TEXT.__const: 0xe5c
-  __TEXT.__cstring: 0x32c8
-  __TEXT.__oslogstring: 0x74
-  __TEXT.__unwind_info: 0x3f8
+  __TEXT.__const: 0xe8c
+  __TEXT.__cstring: 0x39f6
+  __TEXT.__oslogstring: 0xcb8
+  __TEXT.__unwind_info: 0x408
   __TEXT.__objc_classname: 0xef
   __TEXT.__objc_methname: 0x33b6
   __TEXT.__objc_methtype: 0x16f7

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8e0
   __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x298
+  __AUTH_CONST.__auth_got: 0x2c0
   __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__cfstring: 0x9e0
   __AUTH_CONST.__objc_const: 0x19a0
   __AUTH.__objc_data: 0x280
   __DATA.__objc_ivar: 0x1ec
   __DATA.__data: 0xc0
   __DATA.__bss: 0x10
+  __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 22D97AE2-AA00-3315-B444-B276DE6FE8BD
-  Functions: 598
-  Symbols:   131
-  CStrings:  1066
+  UUID: 7C954B86-DB1E-36E7-AD31-B8DFAC109EAC
+  Functions: 601
+  Symbols:   136
+  CStrings:  1166
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _objc_retain
- _FigSignalErrorAtGM
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "-[Calibration computeCalibration]"
+ "-[Calibration computeInitialCalibration]"
+ "-[Calibration extractParametersFromReferenceMetadata:auxiliaryMetadata:options:adaptiveCorrectionConfig:useReferenceFrame:]"
+ "-[Calibration referenceMagnification]"
+ "-[DupDownscaleHalfConvert AllocateResources]"
+ "-[FigCalibration prewarmWithTuningParameters:]"
+ "-[FigCalibration process]"
+ "-[FigCalibration setOptions:]"
+ "-[PyrGPU _doRPDDownscale1WithCommandBuffer:in_tex:out_tex:scaling_factor:]"
+ "-[PyrGPU _downscale2XBelowWithCommandBuffer:in_tex:out_tex:scaling_factor:]"
+ "-[PyrGPU _downscale2XEqualWithCommandBuffer:in_tex:out_tex:scaling_factor:]"
+ "<<<< ADC >>>> %s: ADC tuning: %s = %d"
+ "<<<< ADC >>>> %s: ADC tuning: %s = %f"
+ "<<<< ADC >>>> %s: ADC tuning: %s is not present"
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
+ "<<<< CalibrationTuningParameters (V1) >>>> %s: %@"
+ "<<<< CalibrationTuningParameters (V1) >>>> %s: Level %d:%@ -> %d"
+ "<<<< CalibrationTuningParameters (V1) >>>> %s: Level %d:%@ -> %f"
+ "<<<< CalibrationTuningParameters (V1) >>>> %s: _readKeyFloat failed"
+ "<<<< CalibrationTuningParameters (V1) >>>> %s: _readKeyFloat_t failed"
+ "<<<< CalibrationTuningParameters (V1) >>>> %s: _readKeyInteger failed"
+ "<<<< FigCalibration (V1) >>>> %s: CalibrationV1 set with options %@"
+ "<<<< FigCalibration (V1) >>>> %s: CalibrationV1: Did not get tuning parameters in options."
+ "<<<< FigCalibration (V1) >>>> %s: CalibrationV1: Tuning parameters after initialization is %p."
+ "<<<< FigCalibration (V1) >>>> %s: Retrieving parameters for config %@"
+ "<<<< FigCalibration (V1) >>>> %s: Updated tuning parameters for %@"
+ "<<<< FigCalibration (V1) >>>> %s: _keypointsCount = %d"
+ "Dimensions of SensorRawValidBufferRect in the frame metadata must be non 0."
+ "Disparity tuning:Cannot find the key '%@' for the level %d in the plist."
+ "Disparity tuning:Cannot find the key '%@' in the plist."
+ "Distortion optical center could not be retrieved."
+ "Expected buffer scaling to be within (0.1, 10]."
+ "MetadataCalibratedForBackWideFieldOfView cannot be nil as we received overlap stream properties."
+ "MetadataCalibratedForNarrowerFieldOfView cannot be nil as we received overlap stream properties."
+ "Overlap's calibrationValidRadius cannot be nil, expected to be in DataCalibratedForNarrowerFieldOfView"
+ "PinholeCameraFocalLength is nil."
+ "Timestamp is invalid"
+ "Vaux_3x4 is NULL"
+ "Vref_3x4 is NULL"
+ "[SBP:DownscaleHalfConvert] %s: Context unavailable."
+ "_readKeyFloat"
+ "_readKeyFloat_t"
+ "_readKeyInteger"
+ "_readKeyValue"
+ "_scaleTuningInADCConfig"
+ "auxiliaryMetadata is nil."
+ "calibration_trace"
+ "calibrationv1_tuningparameters_trace"
+ "camInfoByPort is nil."
+ "cmdEnc is NULL"
+ "com.apple.coremedia"
+ "failed"
+ "figcalibration_trace"
+ "kCMBaseObjectError_ParamErr"
+ "maybeValueFloat"
+ "maybeValueFloat_t"
+ "maybeValueInt"
+ "optical center could not be retrieved."
+ "options is nil."
+ "pixelSizeMicrometers cannot be nil as calibration expects it."
+ "referenceMetadata is nil."
+ "sf_trace"
+ "succeeded"
+ "tuningParameters is nil."
- "%s signalled err=%d at <>:%d"

```
