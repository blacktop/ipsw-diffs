## IntelligentDistortionCorrectionV1

> `/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1`

```diff

-580.14.5.0.0
-  __TEXT.__text: 0x13530
-  __TEXT.__auth_stubs: 0x3d0
+587.60.6.0.0
+  __TEXT.__text: 0x17070
+  __TEXT.__auth_stubs: 0x420
   __TEXT.__objc_methlist: 0x854
-  __TEXT.__const: 0x1d0
-  __TEXT.__cstring: 0x42b9
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__const: 0x200
+  __TEXT.__cstring: 0x4f18
+  __TEXT.__oslogstring: 0x1fab
+  __TEXT.__unwind_info: 0x210
   __TEXT.__objc_classname: 0x66e
   __TEXT.__objc_methname: 0x2a54
   __TEXT.__objc_methtype: 0x3134

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6a8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__auth_got: 0x218
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__cfstring: 0xd60
+  __AUTH_CONST.__cfstring: 0xd80
   __AUTH_CONST.__objc_const: 0x1ed0
   __DATA.__objc_ivar: 0x13c
   __DATA.__data: 0x180
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__common: 0x30
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 195
-  Symbols:   122
-  CStrings:  990
+  Symbols:   127
+  CStrings:  1108
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _os_log_type_enabled
- _FigSignalErrorAt
CStrings:
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "-[EdgeDrawingLineDetector memoryAllocationHandler:memoryAllocationParameters:sharedMemoryBuffer:sharedMetalBufferOffset:sharedMetalBufferSize:]"
+ "-[EdgeDrawingLineDetector runTraceBackward:anchorPoint:initialGradDir:sharedMemoryPtr:]"
+ "-[EdgeDrawingLineDetector runTraceForward:anchorPoint:initialGradDir:sharedMemoryPtr:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 determineWorkingBufferRequirements:maximumInputImageWidth:maximumInputImageHeight:maximumSegmentationMaskWidth:maximumSegmentationMaskHeight:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 memoryAllocationHandler:memoryAllocationParameters:sharedMetalBuffer:sharedMetalBufferOffset:sharedMetalBufferSize:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 prepareInputImagePixelBuffer:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 process]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 setSharedMetalBuffer:offset:size:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 setup]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 subProcessIntelligentDistortion:cpwProcessingErrors:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 undistortSegmentationMask]"
+ "-[IDC_RegionOfInterestTracker getCropData]"
+ "-[IDC_RegionOfInterestTracker getRoiData]"
+ "-[IdcContentPreservingWarping memoryAllocationHandler:memoryAllocationParameters:sharedMemoryBuffer:sharedMetalBufferOffset:sharedMetalBufferSize:]"
+ "-[IdcContentPreservingWarping process:segmentationMaskTex:extendedMeshTex:invertedMeshTex:detectedLines:executionErrorInformation:]"
+ "-[IntelligentDistortionCorrection_Utilities extractBundleConfigurationParameters:cameraInfo:tuningParameters:imageInfo:]"
+ "-[IntelligentDistortionCorrection_Utilities extractCameraDictionaryOptions:topEntry:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities extractDistortionOptions:parentEntry:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities extractFloat:name:value:mandatory:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities extractImageOptions:imageInfo:portType:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities extractUint:name:value:mandatory:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities testGenericObject:withName:classType:className:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities warpAndOrUndistortPrimaryAsset:inputImageTexture:inputMeshTexture:outputImageTexture:roiTracker:inputImageMetadataDictionary:]"
+ "-[IntelligentDistortionCorrection_Utilities warpAndOrUndistortSecondaryAsset:inputImageTexture:inputMeshTexture:normalizedInputCrop:primaryImageDimensions:inputHorizontalSecondaryToPrimaryScaleFactor:inputVerticalSecondaryToPrimaryScaleFactor:inputHorizontalSecondaryToPrimaryShift:inputVerticalSecondaryToPrimaryShift:outputImageTexture:outputHorizontalAdditionalScaleFactor:outputVerticalAdditionalScaleFactor:roiTracker:isDepthData:commandBuffer:sensorInputCropRect:]"
+ "FIGMETALCONTEXT_CHECK_ERRCODE"
+ "[Intelligent Distortion Correction Processor]"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING):  segmentationMaskTex.height (%!u(MISSING)) must be between 32 and %!u(MISSING).\n"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING):  segmentationMaskTex.width (%!u(MISSING)) must be between 32 and %!u(MISSING).\n"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'BasePolynomial' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'DynamicPolynomial' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'GeometricDistortionCoefficients' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'Height' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'OpticalCenterOffset' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'PixelSize' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'PortType' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'RawSensorHeight' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'RawSensorWidth' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'Width' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'X' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'Y' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'cameraDictionary' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'curveFalloffMu' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'curveFalloffSigma' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'digitalZoomRatio' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'dynamicDistortionFactor' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'imageInfo' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): 'quadraBinningFactor' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): CholeskySolver is %!d(MISSING), was expecting %!d(MISSING)"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Could not extract CameraDictionary"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Could not extract cameraInfo"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Could not extract cameraOptionsDictionary"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Could not extract classfier options"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Could not extract distortion options"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Could not extract imageInfo"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Could not extract line detector options"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Could not extract tuningParameters"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Could not extract warping options"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Curve #%!u(MISSING) does not contain %!u(MISSING) floats."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Curve #%!u(MISSING) has errors."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Curve #%!u(MISSING), entry %!u(MISSING) has errors."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Entry #%!u(MISSING): field 'classificationHandling' has errors."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Entry #%!u(MISSING): key 'curveOption' = %!d(MISSING) is out of range [0..%!d(MISSING)]."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Entry #%!u(MISSING): key 'curveOption' has errors."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Entry #%!u(MISSING): key 'distortionTarget' has errors"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Entry #%!u(MISSING): key 'gated' has errors."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Entry 'classifications' has 0 entries"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Entry 'curves' has 0 sub-entries."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Failed to undistort inputSegmentationMaskTexture"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): GDC has been done in the ISP. Setting inputImageDimensions->valid to inputImageDimensions->full"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Key 'BasePolynomial' does not contain 2x8 floats."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Key 'DynamicPolynomial' does not contain 2x8 floats."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Mandatory key '%!@(MISSING)' is missing"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Mandatory parameter '%!@(MISSING)' is nil"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Mesh dimensions: %!d(MISSING) x %!d(MISSING)"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Missing synchronizeData!"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Object '%!@(MISSING)' was expected to be of type 'NSNumber'"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Parser did not find sensor rect metadata. Setting inputImageDimensions->sensor to inputImageDimensions->valid"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Parser did not find valid buffer rect metadata. Setting inputImageDimensions->valid to inputImageDimensions->full"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Property '%!@(MISSING)' is expected to be of type '%!@(MISSING)'"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Scaling factor is %!f(MISSING)"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Scaling factor is %!f(MISSING). Optical center is not modified"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): The %!d(MISSING)-th argument is wrong in ssyevx_ call"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): The %!d(MISSING)-th eigenvector failed to converge"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): The 9-th parameter is too small: elem8=%!f(MISSING)"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Too many curves:%!u(MISSING). Only the first %!u(MISSING) curves will be read."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Too many entries:%!u(MISSING). Only the first %!u(MISSING) entries will be read"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Transform estimation mesh dimensions: %!d(MISSING) x %!d(MISSING)"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Unable to add point backward!. Trace aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Unable to add point forward! Trace aborted."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Unexpected external GDC source (%!d(MISSING)). Please file a radar against 'Distortion Correction | All'"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Unknown rotation value."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Updated optical center from (%!f(MISSING),%!f(MISSING)) to (%!f(MISSING),%!f(MISSING))"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): Using provided metal command queue %!p(MISSING)"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): [determineWorkingBufferRequirements] shared metal buffer size: %!l(MISSING)u bytes"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): [memoryAllocationHandler] Invalid call parameter configuration"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): [setSharedMetalBuffer] shared metal buffer pointer: %!p(MISSING) offset: %!l(MISSING)u size: %!l(MISSING)u"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): esGenerationErrorCount = %!d(MISSING)"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): executionErrorInformation pointer NULL"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): gdcForwardPolynomial is nil, but usePrecomputedPolynomialsAndOpticalCenterOffset is true. This is not expected. Please file a radar to 'CameraCapture Stills | all'."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): gdcForwardPolynomial.bytes is nil."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): gdcInversePolynomial is nil, but usePrecomputedPolynomialsAndOpticalCenterOffset is true. This is not expected. Please file a radar to 'CameraCapture Stills | all'."
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): gpuStatus[%!u(MISSING)] is %!u(MISSING), was expecting %!l(MISSING)u"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): inputImageDimensions->crop dimensions are larger than inputImageDimensions->sensor. Is this a fish-eye image?"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): memoryAllocationHandler: bad call. "
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): meshProcessingErrorCount = %!d(MISSING)"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): numberOfLines capped to maximum configured value (%!u(MISSING) --> %!u(MISSING)).\n"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): valid > full"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): validHeight (%!u(MISSING)) must be between 32 and %!u(MISSING).\n"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): validWidth (%!u(MISSING)) must be between 32 and %!u(MISSING).\n"
+ "[Intelligent Distortion Correction Processor] %!s(MISSING): validateExtendedMeshErrorFlag = %!d(MISSING)"
+ "c0SensorToRotatedOrientation"
+ "idc_note_level"
+ "primaryImageDimensions.height is NULL"
+ "primaryImageDimensions.width is NULL"
+ "privEstimateHomographyTransform"
+ "roi is NULL"
+ "rotatedC0toSensorOrientation"

```
