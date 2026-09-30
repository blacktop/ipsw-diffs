## IntelligentDistortionCorrectionV1

> `/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1`

```diff

-664.2.10.0.0
-  __TEXT.__text: 0x15bb0
-  __TEXT.__auth_stubs: 0x3d0
+664.40.10.122.3
+  __TEXT.__text: 0x18b30
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_methlist: 0xd8c
-  __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x42f2
-  __TEXT.__unwind_info: 0x278
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0x5009
+  __TEXT.__oslogstring: 0x20fb
+  __TEXT.__unwind_info: 0x290
   __TEXT.__objc_classname: 0x66e
   __TEXT.__objc_methname: 0x2d46
   __TEXT.__objc_methtype: 0x3357

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x790
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1f0
-  __AUTH_CONST.__cfstring: 0xd60
+  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__cfstring: 0xd80
   __AUTH_CONST.__objc_const: 0x1620
   __DATA.__objc_ivar: 0x144
   __DATA.__data: 0x180
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x190
+  __DATA_DIRTY.__common: 0x30
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D4A8B08D-9B40-358F-8ACF-68C7CEA52193
-  Functions: 483
-  Symbols:   121
-  CStrings:  1108
+  UUID: 421D8944-AACF-3D12-9A49-C92518ED652E
+  Functions: 472
+  Symbols:   125
+  CStrings:  1228
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _os_log_type_enabled
- _FigSignalErrorAtGM
- _objc_retain_x25
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "-[EdgeDrawingLineDetector memoryAllocationHandler:memoryAllocationParameters:sharedMemoryBuffer:sharedMetalBufferOffset:sharedMetalBufferSize:]"
+ "-[EdgeDrawingLineDetector runTraceBackward:anchorPoint:initialGradDir:sharedMemoryPtr:]"
+ "-[EdgeDrawingLineDetector runTraceForward:anchorPoint:initialGradDir:sharedMemoryPtr:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 determineWorkingBufferRequirements:maximumInputImageWidth:maximumInputImageHeight:maximumSegmentationMaskWidth:maximumSegmentationMaskHeight:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 memoryAllocationHandler:memoryAllocationParameters:sharedMetalBuffer:sharedMetalBufferOffset:sharedMetalBufferSize:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 prepareInputImagePixelBuffer:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 prepareSegmentationMaskPixelBuffer:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 process]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 setSharedMetalBuffer:offset:size:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 setup]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 subProcessIntelligentDistortion:cpwProcessingErrors:]"
+ "-[FigIntelligentDistortionCorrectionProcessorV1 undistortSegmentationMask]"
+ "-[IDC_RegionOfInterestTracker getCropData]"
+ "-[IDC_RegionOfInterestTracker getRoiData]"
+ "-[IdcContentPreservingWarping memoryAllocationHandler:paddedMeshWidth:paddedMeshHeight:memoryAllocationParameters:sharedMemoryBuffer:sharedMetalBufferOffset:sharedMetalBufferSize:]"
+ "-[IdcContentPreservingWarping process:maximumInputImageWidth:maximumInputImageHeight:maximumSegmentationMaskWidth:maximumSegmentationMaskHeight:meshWidth:meshHeight:paddedMeshWidth:paddedMeshHeight:segmentationMaskTex:extendedMeshTex:invertedMeshTex:detectedLines:executionErrorInformation:]"
+ "-[IntelligentDistortionCorrection_Utilities extractBundleConfigurationParameters:cameraInfo:tuningParameters:imageInfo:]"
+ "-[IntelligentDistortionCorrection_Utilities extractCameraDictionaryOptions:topEntry:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities extractDistortionOptions:parentEntry:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities extractFloat:name:value:mandatory:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities extractImageOptions:imageInfo:portType:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities extractUint:name:value:mandatory:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities testGenericObject:withName:classType:className:cumulativeError:]"
+ "-[IntelligentDistortionCorrection_Utilities warpAndOrUndistortPrimaryAsset:inputImageTexture:inputMeshTexture:outputImageTexture:roiTracker:inputImageMetadataDictionary:]"
+ "-[IntelligentDistortionCorrection_Utilities warpAndOrUndistortSecondaryAsset:inputImageTexture:inputMeshTexture:normalizedInputCrop:primaryImageDimensions:inputHorizontalSecondaryToPrimaryScaleFactor:inputVerticalSecondaryToPrimaryScaleFactor:inputHorizontalSecondaryToPrimaryShift:inputVerticalSecondaryToPrimaryShift:outputImageTexture:outputHorizontalAdditionalScaleFactor:outputVerticalAdditionalScaleFactor:roiTracker:isDepthData:commandBuffer:sensorInputCropRect:]"
+ "[Intelligent Distortion Correction Processor] %s:  segmentationMaskTex.height (%u) must be between 32 and %u.\n"
+ "[Intelligent Distortion Correction Processor] %s:  segmentationMaskTex.width (%u) must be between 32 and %u.\n"
+ "[Intelligent Distortion Correction Processor] %s: 'BasePolynomial' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'DynamicPolynomial' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'GeometricDistortionCoefficients' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'Height' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'OpticalCenterOffset' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'PixelSize' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'PortType' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'RawSensorHeight' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'RawSensorWidth' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'Width' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'X' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'Y' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'cameraDictionary' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'curveFalloffMu' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'curveFalloffSigma' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'digitalZoomRatio' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'dynamicDistortionFactor' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'imageInfo' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: 'quadraBinningFactor' parsing aborted."
+ "[Intelligent Distortion Correction Processor] %s: CholeskySolver is %d, was expecting %d"
+ "[Intelligent Distortion Correction Processor] %s: Could not extract CameraDictionary"
+ "[Intelligent Distortion Correction Processor] %s: Could not extract cameraInfo"
+ "[Intelligent Distortion Correction Processor] %s: Could not extract cameraOptionsDictionary"
+ "[Intelligent Distortion Correction Processor] %s: Could not extract classifier options"
+ "[Intelligent Distortion Correction Processor] %s: Could not extract distortion options"
+ "[Intelligent Distortion Correction Processor] %s: Could not extract imageInfo"
+ "[Intelligent Distortion Correction Processor] %s: Could not extract line detector options"
+ "[Intelligent Distortion Correction Processor] %s: Could not extract tuningParameters"
+ "[Intelligent Distortion Correction Processor] %s: Could not extract warping options"
+ "[Intelligent Distortion Correction Processor] %s: Curve #%u does not contain %u floats."
+ "[Intelligent Distortion Correction Processor] %s: Curve #%u has errors."
+ "[Intelligent Distortion Correction Processor] %s: Curve #%u, entry %u has errors."
+ "[Intelligent Distortion Correction Processor] %s: Entry #%u: field 'classificationHandling' has errors."
+ "[Intelligent Distortion Correction Processor] %s: Entry #%u: key 'curveOption' = %d is out of range [0..%d]."
+ "[Intelligent Distortion Correction Processor] %s: Entry #%u: key 'curveOption' has errors."
+ "[Intelligent Distortion Correction Processor] %s: Entry #%u: key 'distortionTarget' has errors"
+ "[Intelligent Distortion Correction Processor] %s: Entry #%u: key 'gated' has errors."
+ "[Intelligent Distortion Correction Processor] %s: Entry 'classifications' has 0 entries"
+ "[Intelligent Distortion Correction Processor] %s: Entry 'curves' has 0 sub-entries."
+ "[Intelligent Distortion Correction Processor] %s: Failed to undistort inputSegmentationMaskTexture"
+ "[Intelligent Distortion Correction Processor] %s: GDC has been done in the ISP. Setting inputImageDimensions->valid to inputImageDimensions->full"
+ "[Intelligent Distortion Correction Processor] %s: Key 'BasePolynomial' does not contain 2x8 floats."
+ "[Intelligent Distortion Correction Processor] %s: Key 'DynamicPolynomial' does not contain 2x8 floats."
+ "[Intelligent Distortion Correction Processor] %s: Mandatory key '%@' is missing"
+ "[Intelligent Distortion Correction Processor] %s: Mandatory parameter '%@' is nil"
+ "[Intelligent Distortion Correction Processor] %s: Mesh dimensions: %d x %d"
+ "[Intelligent Distortion Correction Processor] %s: Missing synchronizeData!"
+ "[Intelligent Distortion Correction Processor] %s: Object '%@' was expected to be of type 'NSNumber'"
+ "[Intelligent Distortion Correction Processor] %s: Parser did not find sensor rect metadata. Setting inputImageDimensions->sensor to inputImageDimensions->valid"
+ "[Intelligent Distortion Correction Processor] %s: Parser did not find valid buffer rect metadata. Setting inputImageDimensions->valid to inputImageDimensions->full"
+ "[Intelligent Distortion Correction Processor] %s: Property '%@' is expected to be of type '%@'"
+ "[Intelligent Distortion Correction Processor] %s: Scaling factor is %f"
+ "[Intelligent Distortion Correction Processor] %s: Scaling factor is %f. Optical center is not modified"
+ "[Intelligent Distortion Correction Processor] %s: The %d-th argument is wrong in ssyevx_ call"
+ "[Intelligent Distortion Correction Processor] %s: The %d-th eigenvector failed to converge"
+ "[Intelligent Distortion Correction Processor] %s: The 9-th parameter is too small: elem8=%f"
+ "[Intelligent Distortion Correction Processor] %s: Too many curves:%u. Only the first %u curves will be read."
+ "[Intelligent Distortion Correction Processor] %s: Too many entries:%u. Only the first %u entries will be read"
+ "[Intelligent Distortion Correction Processor] %s: Transform estimation mesh dimensions: %d x %d"
+ "[Intelligent Distortion Correction Processor] %s: Unable to add point backward!. Trace aborted."
+ "[Intelligent Distortion Correction Processor] %s: Unable to add point forward! Trace aborted."
+ "[Intelligent Distortion Correction Processor] %s: Unexpected external GDC source (%d). Please file a radar against 'Distortion Correction | All'"
+ "[Intelligent Distortion Correction Processor] %s: Unknown rotation value."
+ "[Intelligent Distortion Correction Processor] %s: Updated optical center from (%f,%f) to (%f,%f)"
+ "[Intelligent Distortion Correction Processor] %s: Using provided metal command queue %p"
+ "[Intelligent Distortion Correction Processor] %s: [determineWorkingBufferRequirements] shared metal buffer size: %lu bytes"
+ "[Intelligent Distortion Correction Processor] %s: [memoryAllocationHandler] Invalid call parameter configuration"
+ "[Intelligent Distortion Correction Processor] %s: [setSharedMetalBuffer] shared metal buffer pointer: %p offset: %lu size: %lu"
+ "[Intelligent Distortion Correction Processor] %s: _lowResSegmentationMask dimensions exceed configuration parameters (_lowResSegmentationMask dims: %lu x %lu) vs. (configuration dims: %d x %d)"
+ "[Intelligent Distortion Correction Processor] %s: _lowResSegmentationMask must be at least 16 pixels wide and 16 lines high (dims: %lu x %lu)"
+ "[Intelligent Distortion Correction Processor] %s: esGenerationErrorCount = %d"
+ "[Intelligent Distortion Correction Processor] %s: executionErrorInformation pointer NULL"
+ "[Intelligent Distortion Correction Processor] %s: gdcForwardPolynomial is nil, but usePrecomputedPolynomialsAndOpticalCenterOffset is true. This is not expected. Please file a radar to 'CameraCapture Stills | all'."
+ "[Intelligent Distortion Correction Processor] %s: gdcForwardPolynomial.bytes is nil."
+ "[Intelligent Distortion Correction Processor] %s: gdcInversePolynomial is nil, but usePrecomputedPolynomialsAndOpticalCenterOffset is true. This is not expected. Please file a radar to 'CameraCapture Stills | all'."
+ "[Intelligent Distortion Correction Processor] %s: gpuStatus[%u] is %u, was expecting %lu"
+ "[Intelligent Distortion Correction Processor] %s: inputImageDimensions->crop dimensions are larger than inputImageDimensions->sensor. Is this a fish-eye image?"
+ "[Intelligent Distortion Correction Processor] %s: memoryAllocationHandler: bad call. "
+ "[Intelligent Distortion Correction Processor] %s: meshProcessingErrorCount = %d"
+ "[Intelligent Distortion Correction Processor] %s: numberOfLines capped to maximum configured value (%u --> %u).\n"
+ "[Intelligent Distortion Correction Processor] %s: valid > full"
+ "[Intelligent Distortion Correction Processor] %s: validHeight (%u) must be between 32 and %u.\n"
+ "[Intelligent Distortion Correction Processor] %s: validWidth (%u) must be between 32 and %u.\n"
+ "[Intelligent Distortion Correction Processor] %s: validateExtendedMeshErrorFlag = %d"
+ "c0SensorToRotatedOrientation"
+ "idc_note_level"
+ "primaryImageDimensions.height is NULL"
+ "primaryImageDimensions.width is NULL"
+ "privEstimateHomographyTransform"
+ "roi is NULL"
+ "rotatedC0toSensorOrientation"
- "%s signalled err=%d at <>:%d"

```
