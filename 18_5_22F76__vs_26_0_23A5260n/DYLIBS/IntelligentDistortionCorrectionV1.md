## IntelligentDistortionCorrectionV1

> `/System/Library/VideoProcessors/IntelligentDistortionCorrectionV1.bundle/IntelligentDistortionCorrectionV1`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x15678
-  __TEXT.__auth_stubs: 0x3d0
+650.0.0.122.4
+  __TEXT.__text: 0x188fc
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_methlist: 0xd2c
-  __TEXT.__const: 0x1d0
-  __TEXT.__cstring: 0x42cb
-  __TEXT.__unwind_info: 0x270
+  __TEXT.__const: 0x190
+  __TEXT.__cstring: 0x5009
+  __TEXT.__oslogstring: 0x20fb
+  __TEXT.__unwind_info: 0x290
   __TEXT.__objc_classname: 0x66e
-  __TEXT.__objc_methname: 0x2a54
-  __TEXT.__objc_methtype: 0x3134
-  __TEXT.__objc_stubs: 0x10e0
-  __DATA_CONST.__got: 0x120
+  __TEXT.__objc_methname: 0x2c53
+  __TEXT.__objc_methtype: 0x32c3
+  __TEXT.__objc_stubs: 0x1100
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0x48
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x768
+  __DATA_CONST.__objc_selrefs: 0x770
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1f0
-  __AUTH_CONST.__cfstring: 0xd60
+  __AUTH_CONST.__auth_got: 0x210
+  __AUTH_CONST.__cfstring: 0xd80
   __AUTH_CONST.__objc_const: 0x1580
   __DATA.__objc_ivar: 0x13c
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
-  UUID: 77C44A42-DE4D-3C89-B156-9A8DB29CF3B6
-  Functions: 476
-  Symbols:   122
-  CStrings:  1093
+  UUID: 7AC7D6AD-8E09-389A-AE30-92892E029EAB
+  Functions: 467
+  Symbols:   125
+  CStrings:  1220
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _objc_retain_x6
+ _os_log_type_enabled
- _FigSignalErrorAt
- ___stack_chk_fail
- ___stack_chk_guard
- _objc_retain_x25
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "( _rt.inputSegmentationMaskTexture.width <= _currentMax.segmentationMaskDimensions.x ) && ( _rt.inputSegmentationMaskTexture.height <= _currentMax.segmentationMaskDimensions.y )"
+ "( _rt.inputSegmentationMaskTexture.width >= 16 ) && ( _rt.inputSegmentationMaskTexture.height >= 16 )"
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
+ "0 == ( ( _currentMax.meshDimensions.x - _transformCenterMeshDimensions.x ) & 0x01 )"
+ "0 == ( ( _currentMax.meshDimensions.y - _transformCenterMeshDimensions.y ) & 0x01 )"
+ "16@0:8"
+ "Mesh is too small"
+ "T,N"
+ "T,N,V_inputImageAppliedScalingFactors"
+ "[Intelligent Distortion Correction Processor]"
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
+ "_inputImageAppliedScalingFactors"
+ "c0SensorToRotatedOrientation"
+ "computeSizeOfSharedMetalBuffer:maximumInputImageWidth:maximumInputImageHeight:maximumSegmentationMaskWidth:maximumSegmentationMaskHeight:meshWidth:meshHeight:paddedMeshWidth:paddedMeshHeight:"
+ "fillEdParameters:meshWidth:meshHeight:"
+ "i56@0:8^{?=Q}16I24I28I32I36I40I44I48I52"
+ "i80@0:8^{?=Q}16I24I28{?=IIIIII}32@56Q64Q72"
+ "i96@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16I24I28I32I36I40I44I48I52@56@64@72^{?=IIQ@}80^{?=@[4I]}88"
+ "idc_note_level"
+ "inputImageAppliedScalingFactors"
+ "memoryAllocationHandler:paddedMeshWidth:paddedMeshHeight:memoryAllocationParameters:sharedMemoryBuffer:sharedMetalBufferOffset:sharedMetalBufferSize:"
+ "meshDimensions.x >= 2 && meshDimensions.y >= 2"
+ "primaryImageDimensions.height is NULL"
+ "primaryImageDimensions.width is NULL"
+ "privEstimateHomographyTransform"
+ "process:maximumInputImageWidth:maximumInputImageHeight:maximumSegmentationMaskWidth:maximumSegmentationMaskHeight:meshWidth:meshHeight:paddedMeshWidth:paddedMeshHeight:segmentationMaskTex:extendedMeshTex:invertedMeshTex:detectedLines:executionErrorInformation:"
+ "roi is NULL"
+ "rotatedC0toSensorOrientation"
+ "setInputImageAppliedScalingFactors:"
+ "v24@0:816"
+ "v32@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16I24I28"
+ "{?=\"finalImageDimensions\"\"replicatePixels\"B\"digitalZoomRatio\"f\"inputImageAppliedScalingFactors\"\"pixelSize\"f\"opticalCenterOffset\"\"dynamicDistortionFactor\"f\"quadraBinningFactor\"I\"gdcForwardPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"gdcInversePolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"doUndistortion\"B\"stereoRectificationInverseHomography\"{?=\"columns\"[3]}\"applyStereoRectificationHomography\"B\"useBilinearInterpolation\"B\"precomputedGDCPolynomials\"B\"classifier\"{?=\"maskGatingThreshold\"I\"maximumFaceRectangleThreshold\"I\"minimumFaceRectangleThreshold\"I\"centerRadiusThreshold\"I\"centerRadiusScale\"f\"centerMaskThreshold\"I}\"barrelDistortionPolynomial\"[6f]\"inputImageDimensions\"{?=\"full\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"valid\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"sensor\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"crop\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}}\"outputImageDimensions\"{?=\"full\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}}\"segmentationMaskBoundingRectangle\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"lineDetector\"{?=\"downscaleFactor\"I\"gradientMagnitudeThreshold\"f\"gradientNormalizationRadius\"I\"anchorScanInterval\"I\"lineFitInitialLength\"I\"lineFitErrorThreshold\"f\"lineMergeDeviationThreshold\"f\"lineMergeDistanceThreshold\"f\"minimumLineLength\"I\"segmentationMaskDilationRadius\"I}\"contentPreservingWarping\"{?=\"esWeight1\"f\"esWeight2\"f\"edWeight\"f\"elWeight\"f\"pareDownConstant\"I\"segmentationMaskErosionRadius\"I}\"applyAdjustedEsWeights\"B\"numCurveOptions\"I\"curveOptions\"[10{?=\"coefficients\"[7f]}]\"numClassificationOptions\"I\"classificationOptions\"[10{?=\"gated\"B\"curveOption\"i\"distortionTarget\"f}]\"curveFalloffMu\"f\"curveFalloffSigma\"f}"
+ "{?=\"inputImageDimensions\"\"segmentationMaskDimensions\"\"meshDimensions\"\"invertedMeshDimensions\"\"paddedMeshDimensions\"}"
+ "{?=\"parameters\"{?=\"inputToFullImageScalingCoefs\"\"fullImageToSensorImageOffset\"\"sensorImagePosToMeshCellPosScalingFactor\"\"finalImageDims\"\"replicatePixels\"B\"outputSecondaryToPrimaryCoef\"\"inputScalingCoef\"\"inputShift\"\"inputPrimaryToSecondaryCoef\"\"digitalZoomRatio\"\"isDepthData\"B\"geometricDistortionCommon\"{?=\"center\"\"mmFactor\"f}\"inverseGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"forwardGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"doUndistortion\"B\"haveMesh\"B\"aspectRatio\"f\"stereoRectificationInverseHomography\"{?=\"columns\"[3]}\"applyStereoRectificationHomography\"B\"useBilinearInterpolation\"B}\"primaryOutputImageWidth\"I\"primaryOutputImageHeight\"I\"roi\"@\"<MTLBuffer>\"}"
- "0 == ( ( meshDimensions.x - _transformCenterMeshDimensions.x ) & 0x01 )"
- "0 == ( ( meshDimensions.y - _transformCenterMeshDimensions.y ) & 0x01 )"
- "TB,N,V_generateMask"
- "_generateMask"
- "_lowResSegmentationMask dimensions exceed configuration parameters"
- "_lowResSegmentationMask must be at least 16 pixels wide and 16 lines high"
- "_rt.inputSegmentationMaskTexture.width <= _currentMax.segmentationMaskDimensions.x && _rt.inputSegmentationMaskTexture.height <= _currentMax.segmentationMaskDimensions.y"
- "_rt.inputSegmentationMaskTexture.width >= 16 && _rt.inputSegmentationMaskTexture.height >= 16"
- "computeSizeOfSharedMetalBuffer:maximumSegmentationMaskWidth:maximumSegmentationMaskHeight:"
- "fillEdParameters:"
- "generateMask"
- "i32@0:8^{?=Q}16I24I28"
- "i56@0:8^{?=Q}16{?=II}24@32Q40Q48"
- "i64@0:8^{?=BfffI{?=ffffffff}{?=ffffffff}B{?=[3]}BBB{?=IIIIfI}[6f]{?={?=iiiiii}{?=iiiiii}{?=iiiiii}{?=iiiiii}}{?={?=iiiiii}}{?=iiiiii}{?=IfIIIfffII}{?=ffffII}BI[10{?=[7f]}]I[10{?=Bif}]ff}16@24@32@40^{?=IIQ@}48^{?=@[4I]}56"
- "process:segmentationMaskTex:extendedMeshTex:invertedMeshTex:detectedLines:executionErrorInformation:"
- "setGenerateMask:"
- "{?=\"finalImageDimensions\"\"replicatePixels\"B\"digitalZoomRatio\"f\"pixelSize\"f\"opticalCenterOffset\"\"dynamicDistortionFactor\"f\"quadraBinningFactor\"I\"gdcForwardPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"gdcInversePolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"doUndistortion\"B\"stereoRectificationInverseHomography\"{?=\"columns\"[3]}\"applyStereoRectificationHomography\"B\"useBilinearInterpolation\"B\"precomputedGDCPolynomials\"B\"classifier\"{?=\"maskGatingThreshold\"I\"maximumFaceRectangleThreshold\"I\"minimumFaceRectangleThreshold\"I\"centerRadiusThreshold\"I\"centerRadiusScale\"f\"centerMaskThreshold\"I}\"barrelDistortionPolynomial\"[6f]\"inputImageDimensions\"{?=\"full\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"valid\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"sensor\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"crop\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}}\"outputImageDimensions\"{?=\"full\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}}\"segmentationMaskBoundingRectangle\"{?=\"x0\"i\"y0\"i\"x1\"i\"y1\"i\"width\"i\"height\"i}\"lineDetector\"{?=\"downscaleFactor\"I\"gradientMagnitudeThreshold\"f\"gradientNormalizationRadius\"I\"anchorScanInterval\"I\"lineFitInitialLength\"I\"lineFitErrorThreshold\"f\"lineMergeDeviationThreshold\"f\"lineMergeDistanceThreshold\"f\"minimumLineLength\"I\"segmentationMaskDilationRadius\"I}\"contentPreservingWarping\"{?=\"esWeight1\"f\"esWeight2\"f\"edWeight\"f\"elWeight\"f\"pareDownConstant\"I\"segmentationMaskErosionRadius\"I}\"applyAdjustedEsWeights\"B\"numCurveOptions\"I\"curveOptions\"[10{?=\"coefficients\"[7f]}]\"numClassificationOptions\"I\"classificationOptions\"[10{?=\"gated\"B\"curveOption\"i\"distortionTarget\"f}]\"curveFalloffMu\"f\"curveFalloffSigma\"f}"
- "{?=\"parameters\"{?=\"inputToFullImageScalingCoefs\"\"fullImageToSensorImageOffset\"\"sensorImagePosToMeshCellPosScalingFactor\"\"finalImageDims\"\"replicatePixels\"B\"outputSecondaryToPrimaryCoef\"\"inputScalingCoef\"\"inputShift\"\"inputPrimaryToSecondaryCoef\"\"isDepthData\"B\"geometricDistortionCommon\"{?=\"center\"\"mmFactor\"f}\"inverseGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"forwardGeometricDistortionPolynomial\"{?=\"c0\"f\"c2\"f\"c4\"f\"c6\"f\"c8\"f\"c10\"f\"c12\"f\"c14\"f}\"doUndistortion\"B\"haveMesh\"B\"aspectRatio\"f\"stereoRectificationInverseHomography\"{?=\"columns\"[3]}\"applyStereoRectificationHomography\"B\"useBilinearInterpolation\"B}\"primaryOutputImageWidth\"I\"primaryOutputImageHeight\"I\"roi\"@\"<MTLBuffer>\"}"
- "{?=\"segmentationMaskDimensions\"}"

```
