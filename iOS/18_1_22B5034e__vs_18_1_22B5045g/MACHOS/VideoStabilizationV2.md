## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

-580.2.0.0.0
-  __TEXT.__text: 0x48dc4
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_stubs: 0x2880
-  __TEXT.__objc_methlist: 0x1028
-  __TEXT.__objc_classname: 0x1d3
-  __TEXT.__objc_methname: 0x46d3
-  __TEXT.__objc_methtype: 0x1449
-  __TEXT.__const: 0x630
-  __TEXT.__oslogstring: 0xb2ac
-  __TEXT.__cstring: 0x7db8
-  __TEXT.__gcc_except_tab: 0x230
-  __TEXT.__unwind_info: 0x500
-  __DATA_CONST.__auth_got: 0x610
-  __DATA_CONST.__got: 0x628
+580.6.21.0.0
+  __TEXT.__text: 0x56e84
+  __TEXT.__auth_stubs: 0xcd0
+  __TEXT.__objc_stubs: 0x2f00
+  __TEXT.__objc_methlist: 0x10b8
+  __TEXT.__objc_classname: 0x1d5
+  __TEXT.__objc_methname: 0x5033
+  __TEXT.__objc_methtype: 0x14ad
+  __TEXT.__const: 0x690
+  __TEXT.__oslogstring: 0xcc23
+  __TEXT.__cstring: 0x8d93
+  __TEXT.__gcc_except_tab: 0x494
+  __TEXT.__unwind_info: 0x538
+  __DATA_CONST.__auth_got: 0x678
+  __DATA_CONST.__got: 0x730
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1e8
-  __DATA_CONST.__cfstring: 0x820
+  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x2718
   __DATA_CONST.__objc_dictobj: 0x960
   __DATA_CONST.__objc_arrayobj: 0x1680
-  __DATA.__objc_const: 0x48d0
-  __DATA.__objc_selrefs: 0xc58
-  __DATA.__objc_ivar: 0x3e0
+  __DATA.__objc_const: 0x4ce0
+  __DATA.__objc_selrefs: 0xe00
+  __DATA.__objc_ivar: 0x430
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x300
   __DATA.__common: 0x60

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 484
-  Symbols:   1644
-  CStrings:  2373
+  Functions: 514
+  Symbols:   1797
+  CStrings:  2640
 
Symbols:
+ _objc_msgSend$setInstanceLabel:
+ _CMIGetPixelFormatInfo
+ _kFigCaptureStreamMetadataOutputKey_PostColorProcessingThumbnail
+ _objc_msgSend$texture2DDescriptorWithPixelFormat:width:height:mipmapped:
+ _kFigCaptureSampleBufferMetadata_FinalCropRectFromSource
+ __runSmartStyleReverseLearning
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingDeltaMap
+ _kCMTimeNegativeInfinity
+ _CMIGetYCCFromRGBConversionMatrix
+ -[VISConfigurationV2 setSmartStyleMemoryPoolId:]
+ ___87-[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]_block_invoke
+ _objc_msgSend$setTexture:atIndex:
+ _CMIGetYCCFromRGBConversionMatrixForPixelBuffer
+ _objc_msgSend$globalLinearSystemMixFactor
+ __shouldBypassSmartStyle
+ _objc_msgSend$arrayWithObjects:count:
+ _AffineTransformArrayApplyOnAttachment
+ -[VISConfigurationV2 setSmartStyleRenderingEnabled:]
+ _objc_msgSend$setInputStyleCoefficientsPixelBuffer:
+ OBJC_IVAR_$_VISWrapper._smartStyleReversibilityProcessingEnabled
+ _objc_msgSend$computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficients:outputDeltaMapPixelBuffer:
+ OBJC_IVAR_$_affineGPUMetal._attachmentIsLinearThumbnail
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingIntegratedForwardLearnedCoefficients
+ _OBJC_CLASS_$_FigMetalAllocatorBackend
+ _objc_msgSend$setOutputStyledPixelBuffer:
+ _kFigCaptureSampleBufferMetadata_SmartStyleIsIdentityCoefficients
+ _objc_msgSend$initWithOptionalMetalCommandQueue:
+ _objc_msgSend$smartStyleMemoryPoolId
+ OBJC_IVAR_$_affineGPUMetal._inputChromaPyramid
+ GCC_except_table38
+ ___87-[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]_block_invoke_2
+ _kFigVideoStabilizationSampleBufferAttachmentKey_OutputSmartStyleDeltaMapSampleBuffer
+ OBJC_IVAR_$_affineGPUMetal._fbsDeltaThresholdLuma
+ __updateSmartStyleGlobalMixFactor
+ _CMIGetPixelBufferYCCMatrix
+ OBJC_IVAR_$_affineGPUMetal._ditherStrengthChroma
+ _objc_msgSend$lastObject
+ OBJC_IVAR_$_affineGPUMetal._fbsDeltaThresholdChroma
+ _objc_msgSend$setSmartStyleReversibilityProcessingEnabled:
+ _kFigCaptureSampleBufferMetadata_SmartStyleLearnedCoefficientsAreFiltered
+ _objc_msgSend$metalDevice
+ __runSmartStyleIntegrate
+ _objc_msgSend$setMetalSharedEvent:
+ _objc_msgSend$_blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:
+ renderWithPixelBuffer:metadata:pixelBufferValidRect:ltmLUT:outputPixelBuffer:isAttachmentRendering:.ditherSeed
+ __block_literal_global.165
+ _objc_msgSend$styleEngineConfiguration
+ _OBJC_CLASS_$_CMISmartStyleUtilitiesV1
+ _objc_msgSend$getDefaultProcessorConfigurationForStreaming
+ _OBJC_CLASS_$_FigMetalAllocatorBackendDescriptor
+ _objc_msgSend$supportsFamily:
+ _kFigCaptureStreamMetadataOutputKey_HumanSkinsMask
+ _objc_msgSend$setPrimaryCaptureRect:
+ -[VISConfigurationV2 smartStyleReversibilityEnabled]
+ OBJC_IVAR_$_VISConfigurationV2._smartStyleRenderingEnabled
+ _objc_msgSend$initWithDevice:allocatorType:
+ __block_literal_global.91
+ __runSmartStyleApplyOnUnstabilizedImage
+ _kFigCaptureSampleBufferMetadata_SmartStyleAppliedOnThisFrame
+ __block_literal_global.163
+ _objc_msgSend$setWireMemory:
+ GCC_except_table26
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingIntegratedReverseLearnedCoefficients
+ _OBJC_CLASS_$_NSArray
+ _objc_msgSend$arrayWithArray:
+ _kFigCaptureSampleBufferAttachmentKey_SmartStyleMetalEvent
+ _objc_msgSend$setImageblockWidth:height:
+ OBJC_IVAR_$_affineGPUMetal._inputLumaPyramid
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingLinearThumbnail
+ _objc_msgSend$initWithOptionalMetalCommandQueue:useCase:processingType:optionalExternalMemoryResource:
+ __enqueueCoefficientsForSmartStyleFilterForwardLearningFromCoefficientsSampleBuffer
+ _objc_msgSend$getRequiredInputBufferSizeForFilterType:
+ OBJC_IVAR_$_VISConfigurationV2._smartStyleMemoryPoolId
+ _objc_msgSend$configuration
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _kFigVideoStabilizationPixelBufferAttachmentKey_OutputSmartStyleUnstyledPixelBuffer
+ _objc_msgSend$resetCoefficientsFilter
+ OBJC_IVAR_$_affineGPUMetal._ditherNoStyle
+ _FigGetCFPreferenceBooleanWithDefault
+ -[VISConfigurationV2 smartStyleMemoryPoolId]
+ __setAttachedMediaToSampleBuffer
+ OBJC_IVAR_$_affineGPUMetal._fbsEdgeThresholdLuma
+ _sbp_gvs_createStabilizedAttachmentsPixelBuffers
+ ___invert_f4
+ _objc_msgSend$setupWithDescriptor:
+ _objc_retain_x26
+ _OBJC_CLASS_$_CMIExternalMemoryResource
+ _objc_msgSend$setTemporalFilterInputBufferSize:
+ __enqueueCoefficientsForSmartStyleFilterForwardLearning
+ __runSmartStyleApplyOnUnstabilizedThumbnail
+ _objc_msgSend$_getBlurDeltaMapBordersShaderParameters:pipelineIndexToUse:
+ _objc_msgSend$filterCoefficientsForFrameWithMetadata:pts:filterType:toPixelBuffer:
+ OBJC_IVAR_$_affineGPUMetal._ditherStrengthLuma
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingLearnedCoefficients
+ _CMIGetRGBFromYCCConversionMatrix
+ _objc_msgSend$setInputUnstyledPixelBuffer:
+ _objc_msgSend$setInputMetadataDict:
+ _kFigCaptureStreamMetadataOutputKey_HumanHairMask
+ __removeSmartStyleAttachments
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingReverseLearnedCoefficients
+ _objc_msgSend$setMemoryPoolId:
+ _kFigCaptureSampleBufferAttachmentKey_SmartStyleCoefficientStyle
+ _objc_msgSend$smartStyleReversibilityEnabled
+ -[VISWrapper smartStyleReversibilityProcessingEnabled]
+ _ensureValidBufferRectIsCompatibleWithGPU
+ _kFigCaptureSampleBufferAttachmentKey_SmartStyleFutureLearnedCoefficientsArray
+ -[VISConfigurationV2 setSmartStyleReversibilityEnabled:]
+ _objc_msgSend$addObjectsFromArray:
+ -[VISWrapper setSmartStyleReversibilityProcessingEnabled:]
+ _objc_msgSend$enqueueCoefficientsForFiltering:withMetadata:pts:learnedStyle:
+ __block_literal_global.152
+ _objc_msgSend$setAllocatorBackend:
+ _objc_msgSend$utilities
+ __runSmartStyleReverseLearningAndComputeDeltaMap
+ __runSmartStyleFilterForwardLearning
+ _objc_msgSend$setExternalMemoryResource:
+ _CGRectGetMidX
+ _objc_msgSend$outputIntegratedStyleCoefficientsTexture
+ _kFigCaptureStreamMetadataOutputKey_SkyMask
+ _kFigCaptureSampleBufferMetadata_SmartStyleLearnedRect
+ _CVBufferRemoveAttachment
+ _objc_msgSend$setInputUnstyledThumbnailPixelBuffer:
+ _kFigVideoStabilizationPixelBufferAttachmentKey_OutputSmartStyleDeltaMapPixelBuffer
+ OBJC_IVAR_$_affineGPUMetal._smoothedLumaPyramid
+ -[VISConfigurationV2 smartStyleRenderingEnabled]
+ GCC_except_table21
+ -[affineGPUMetal _allocatePyramidWithPixelFormat:bottomLevelWidth:bottomLevelHeight:scaleFactor:includeBottomLevel:minimumDimension:]
+ OBJC_IVAR_$_VISConfigurationV2._smartStyleReversibilityEnabled
+ OBJC_IVAR_$_VISProcessorV2._smartStyleReversibilityProcessingEnabled
+ _objc_msgSend$process
+ OBJC_IVAR_$_affineGPUMetal._forwardCoefficients
+ _objc_msgSend$smartStyleRenderingEnabled
+ -[VISProcessorV2 setSmartStyleReversibilityProcessingEnabled:]
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingUnstyledThumbnail
+ OBJC_IVAR_$_affineGPUMetal._reverseCoefficients
+ _objc_msgSend$setInputOutput:
+ -[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]
+ _objc_msgSend$setGlobalLinearSystemMixFactor:
+ __block_literal_global.150
+ _kFigVideoStabilizationSampleBufferAttachmentKey_OutputSmartStyleUnstyledEnabled
+ OBJC_IVAR_$_affineGPUMetal._intermediateOutputUnstyledPixelBuffer
+ _kFigVideoStabilizationSampleBufferProcessorOption_SmartStyleReversibilityEnabled
+ _objc_msgSend$setMemSize:
+ _kFigVideoStabilizationSampleBufferProcessorOption_SmartStyleMemoryPoolId
+ OBJC_IVAR_$_affineGPUMetal._fbsEdgeThresholdChroma
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingStyledThumbnail
+ _ldexpf
+ OBJC_IVAR_$_affineGPUMetal._smoothedChromaPyramid
+ _kFigCaptureStreamMetadataOutputKey_HumanFullBodiesMask
+ _kFigVideoStabilizationSampleBufferProcessorOption_SmartStyleRenderingEnabled
+ -[VISProcessorV2 smartStyleReversibilityProcessingEnabled]
+ _objc_msgSend$firstObject
+ _CMTimeCompare
+ _objc_msgSend$learnTransformFrom:to:outputCoefficients:outputIntegratedCoefficients:
+ _CGRectGetMidY
+ _objc_msgSend$_allocatePyramidWithPixelFormat:bottomLevelWidth:bottomLevelHeight:scaleFactor:includeBottomLevel:minimumDimension:
+ _objc_msgSend$numberWithUnsignedLongLong:
- __block_literal_global.81
- __block_literal_global.125
- __block_literal_global.127
- GCC_except_table23
- GCC_except_table35
CStrings:
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputPixelBuffer is NULL"
+ "setInputUnstyledPixelBuffer:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Failed to update smart style global mix factor"
+ "_removeSmartStyleAttachments"
+ "scaleFactor must be above 0"
+ "setGlobalLinearSystemMixFactor:"
+ "Unable to bind input unstyled blur pixel buffer"
+ "inputUnstabilizedUnstyledPixelBuffer"
+ "setTexture:atIndex:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to get smart style processor input output class"
+ "inputUnstyledPixelBuffer is NULL"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): [smartStyleApplyProcessor finishProcessing] failed, err = %!d(MISSING)"
+ "AttachmentName"
+ "_runSmartStyleIntegrate"
+ "setSmartStyleRenderingEnabled:"
+ "smartStyleReversibilityProcessingEnabled"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputUnstyledThumbnailPixelBuffer is NULL"
+ "setSmartStyleMemoryPoolId:"
+ "attachedMedia"
+ "inputSampleBuffer is nil"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): VISConfiguration: smartStyleReversibilityProcessingEnabled = %!s(MISSING)"
+ "_inputChromaPyramid"
+ "initWithOptionalMetalCommandQueue:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputMetadataDict is nil"
+ "inputStyledThumbnailPixelBuffer"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to allocate outputFilteredForwardLearnedCoefficientsPixelBuffer "
+ "smartStyleExternalMem"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): [smartStyleIntegrateProcessor prepareToProcess] failed, err = %!d(MISSING)"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to apply style on unstabilized image"
+ "CMIFastBilateralSmoothing_Remix"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputSampleBuffer is NULL"
+ "inputStabilizedUnstyledPixelBuffer"
+ "setMetalSharedEvent:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create a smart style integrate processor configuration"
+ "setImageblockWidth:height:"
+ "inputPixelBuffer is nil"
+ "Failed to setup FigMetalAllocatorBackend"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Failed to enqueue coefficients from inputSampleBuffer"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Only GPU platform can stabilize attachments"
+ "_smartStyleMemoryPoolId"
+ "inputLearnedCoefficientsPixelBuffer"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): outputDeltaMapPixelBuffer is NULL"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputUnstabilizedUnstyledPixelBuffer is NULL"
+ "outputDeltaMapPixelBuffer"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create timing info for outputFilteredForwardLearnedCoefficientsTimingInfo"
+ "Unable to cache blur tmp texture 0 for delta map"
+ "styleEngineConfiguration"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): NULL argument"
+ "setMemoryPoolId:"
+ "_smartStyleReversibilityEnabled"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): attachmentsToTransform is nil"
+ "VIS-SmartStyle-FigMetalAllocatorBackend"
+ "[3@\"<MTLComputePipelineState>\"]"
+ "rectValid"
+ "_inputLumaPyramid"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create a smart style apply processor"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create a smart style apply processor configuration"
+ "scaleFactor > 0"
+ "metalDevice"
+ "TQ,N,V_smartStyleMemoryPoolId"
+ "_smartStyleRenderingEnabled"
+ "_smoothedLumaPyramid is NULL"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to perform smart style reverse learning"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): [smartStyleApplyProcessor process] failed, err = %!d(MISSING)"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Failed to enqueue coefficients from futureCoefficientsSampleBuffer"
+ "setMemSize:"
+ "_reverseCoefficients"
+ "destSampleBuffer"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): sampleBufferToStyle is NULL"
+ "setPrimaryCaptureRect:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Update filtered coefficients to sbuf=%!p(MISSING)"
+ "lastObject"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to remove all smart style attachments from source sample buffer"
+ "Could not create CMIExternalMemoryResource"
+ "SmartStyleProcessor"
+ "filterCoefficientsForFrameWithMetadata:pts:filterType:toPixelBuffer:"
+ "_blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to allocate outputStyledThumbnailPixelBuffer"
+ "_fbsEdgeThresholdChroma"
+ "Unable to allocate intermediate pixel buffer to stabilize unstyled frame"
+ "/AppleInternal/VideoProcessors/%!@(MISSING).bundle"
+ "Unable to bind output delta map pixel buffer"
+ "_smoothedLumaPyramid"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Bundle loading failed"
+ "utilities"
+ "r"
+ "desc"
+ "( outputYCCMatrixType != kCMIYCCMatrixTypeUnspecified ) && ( outputYCCMatrixType != kCMIYCCMatrixTypeUnsupported )"
+ "_fbsEdgeThresholdLuma"
+ "_inputChromaPyramid is NULL"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Input arguments are NULL"
+ "initWithDevice:allocatorType:"
+ "TB,N,V_smartStyleReversibilityProcessingEnabled"
+ "inputUnstyledPixelBuffer"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): [smartStyleApplyProcessor prepareToProcess] failed, err = %!d(MISSING)"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to remove all smart style attachments from destination sample buffer"
+ "inputSyledPixelBuffer"
+ "_pipelineComputeStates[BILATERAL_REMIX]"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Error creating output delta map sample buffer (%!d(MISSING))"
+ "commandEncoder"
+ "outputSampleBuffer"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable buffer coefficients for temporal filtering"
+ "attachedMediaDict is nil"
+ "futureCoefficientsSampleBuffer is NULL"
+ "SmartStyle"
+ "_estimateStabilizedROICenter"
+ "firstObject"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to get timing info of input attachment sample buffer"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputLearnedCoefficientsPixelBuffer is NULL"
+ "setInputStyleCoefficientsPixelBuffer:"
+ "dispatchThreads:threadsPerThreadgroup:"
+ "( inputYCCMatrixType != kCMIYCCMatrixTypeUnspecified ) && ( inputYCCMatrixType != kCMIYCCMatrixTypeUnsupported )"
+ "_pipelineComputeStates[DOWNSAMPLE_4X] is NULL"
+ "pyramidArray"
+ "Unable to bind input styled blur pixel buffer"
+ "Unable to get cached destination delta map metal texture"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): attachedMedia is nil"
+ "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
+ "_runSmartStyleApplyOnUnstabilizedThumbnail"
+ "tex"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputStyledThumbnailPixelBuffer is NULL"
+ "setupWithDescriptor:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): metadataDict is nil"
+ "attachedMediaDict"
+ "inputUnstyledThumbnailPixelBuffer"
+ "_ditherNoStyle"
+ "inputMetadataDict"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputStabilizedUnstyledPixelBuffer is NULL"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to remove all smart style attachments"
+ "_smoothedChromaPyramid"
+ "descriptor is nil"
+ "addObjectsFromArray:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputStyledThumbnailSampleBuffer is NULL"
+ "Output pixel buffer does not have YCbCr matrix type specified in attachments"
+ "setTemporalFilterInputBufferSize:"
+ "Unable to cache blur previous texture 1 for delta map"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to allocate outputReverseLearnedCoefficientsPixelBuffer "
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): [smartStyleIntegrateProcessor process] failed, err = %!d(MISSING)"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Stabilize attachment %!@(MISSING)"
+ "Failed allocating work buffer for delta map"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create timing info for outputReverseLearnedCoefficientsTimingInfo"
+ "storage->smartStyleContext.renderingEnabled"
+ "setSmartStyleReversibilityProcessingEnabled:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Failed computing delta map"
+ "sampleBufferToStyle"
+ "\x92\x11\x15\x17"
+ "computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficients:outputDeltaMapPixelBuffer:"
+ "texture is nil"
+ "_runSmartStyleFilterForwardLearning"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to learn reverse style transform"
+ "storage->blurBorderConfig.workDeltaMapPixelBuffer[bufferIdx]"
+ "Unable to cache blur previous texture 0 for delta map"
+ "setAllocatorBackend:"
+ "\x0f\x0f\x0f\x0f\v\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa2\x12\x12\x12\x12\x12\x12\x12\x12\x12c\x122"
+ "setInputOutput:"
+ "Blur copy pipeline is nil"
+ "arrayWithObjects:count:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to filter smart style coefficients"
+ "initWithOptionalMetalCommandQueue:useCase:processingType:optionalExternalMemoryResource:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create smart style shared memory"
+ "Unable to get output delta map color matrix"
+ "finalCrecRectValid"
+ "_fbsDeltaThresholdChroma"
+ "ctx && derivedVectors"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputOutput is nil"
+ "smartStyleRenderingEnabled"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): [smartStyleIntegrateProcessor setup] failed, err = %!d(MISSING)"
+ "setOutputStyledPixelBuffer:"
+ "_runSmartStyleApplyOnUnstabilizedImage"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create a smart style integrate processor"
+ "_enqueueCoefficientsForSmartStyleFilterForwardLearningFromCoefficientsSampleBuffer"
+ "-[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]"
+ "TB,N,V_smartStyleReversibilityEnabled"
+ "outputDeltaMapPixelBuffer is NULL"
+ "smartStyleReversibilityEnabled"
+ "_ditherStrengthChroma"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Failed to render the attachment transformation"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to integrate smart style coefficients"
+ "setInputMetadataDict:"
+ "cvErr == kCVReturnSuccess"
+ "( (storage->transformContext.platform) == kTransformGPU )"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create outputReverseLearnedCoefficientsSampleBuffer"
+ "Could not create FigMetalAllocatorBackend"
+ "OutputSmartStyleUnstyledPixelBuffer"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): [smartStyleApplyProcessor setup] failed, err = %!d(MISSING)"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputLearnedCoefficientsSampleBuffer is NULL"
+ "_loadAndConfigureSmartStyle"
+ "_enqueueCoefficientsForSmartStyleFilterForwardLearning"
+ "inputOutput"
+ "setInputUnstyledThumbnailPixelBuffer:"
+ "_pipelineComputeStates[BILATERAL_REMIX] is NULL"
+ "FIGMETALCONTEXT_CHECK_ERRCODE"
+ "inputLearnedCoefficientsSampleBuffer"
+ "backend"
+ "_runSmartStyleReverseLearningAndComputeDeltaMap"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create a smart style utilities to learn"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Learned ROI rect not valid"
+ "inputTextures.count <= 2"
+ "outputIntegratedStyleCoefficientsTexture"
+ "_attachmentIsLinearThumbnail"
+ "inputSyledPixelBuffer is NULL"
+ "_ditherStrengthLuma"
+ "_intermediateOutputUnstyledPixelBuffer"
+ "CMISmartStyleProcessorInputOutputV%!d(MISSING)"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Loading Smart Style Bundle: %!s(MISSING)"
+ "<<<< affineGPUMetalV2 >>>> %!s(MISSING): shaders used=%!s(MISSING)"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): destSampleBuffer is NULL"
+ "globalLinearSystemMixFactor"
+ "_runSmartStyleReverseLearning"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to allocate output attachement pixel buffer"
+ "commandEncoder is NULL"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): outputSampleBuffer is NULL"
+ "setInstanceLabel:"
+ "_smoothedChromaPyramid is NULL"
+ "Unable to get deltamap blur borders pipeline"
+ "Input pixel buffer does not have YCbCr matrix type specified in attachments"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to allocate outputStyledThumbnailSampleBuffer"
+ "getRequiredInputBufferSizeForFilterType:"
+ "learnTransformFrom:to:outputCoefficients:outputIntegratedCoefficients:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create a smart style utilities to apply"
+ "sbp_gvs_createStabilizedAttachmentsPixelBuffers"
+ "VIS-Apply"
+ "( parentInputSize[0] > 0 ) && ( parentInputSize[1] > 0 ) && ( parentOutputSize[0] > 0 ) && ( parentOutputSize[1] > 0 )"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to apply style on unstabilized thumbnail"
+ "arrayWithArray:"
+ "futureCoefficientsSampleBuffer"
+ "_smartStyleReversibilityProcessingEnabled"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to get timing info of inputUnstyledThumbnailSampleBuffer"
+ "pyramidArray is nil"
+ "_pipelineComputeStates[DOWNSAMPLE_4X]"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to stabilize attachments"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Invalid final crop rect from metadata"
+ "numberWithUnsignedLongLong:"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to enqueue coefficients"
+ "setSmartStyleReversibilityEnabled:"
+ "setWireMemory:"
+ "i40@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to create outputFilteredForwardLearnedCoefficientsSampleBuffer"
+ "Unable to get cached destination unstyled metal texture"
+ "_inputLumaPyramid is NULL"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Error creating output attachment sample buffer (%!d(MISSING))"
+ "attachmentsToTransform"
+ "_allocatePyramidWithPixelFormat:bottomLevelWidth:bottomLevelHeight:scaleFactor:includeBottomLevel:minimumDimension:"
+ "resetCoefficientsFilter"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputStabilizedStyledPixelBuffer is NULL"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): inputUnstyledThumbnailSampleBuffer is NULL"
+ "CMIFastBilateralSmoothing_Downsample4x"
+ "inputStabilizedStyledPixelBuffer"
+ "SmartStyle reversibility is supported only if SmartStyle rendering is enabled"
+ "smartStyle.video.reversibilityUses4x3Spotlights"
+ "getDefaultProcessorConfigurationForStreaming"
+ "TB,N,V_smartStyleRenderingEnabled"
+ "@60@0:8Q16Q24Q32Q40B48Q52"
+ "_fbsDeltaThresholdLuma"
+ "Unable to cache blur previous texture 2 for delta map"
+ "inputUnstyledThumbnailSampleBuffer"
+ "_forwardCoefficients"
+ "_updateSmartStyleGlobalMixFactor"
+ "inputStyledThumbnailSampleBuffer"
+ "Could not create FigMetalAllocatorBackendDescriptor"
+ "OutputSmartStyleDeltaMapPixelBuffer"
+ "smartStyleMemoryPoolId"
+ "v24@0:8^{?=Ciiiiiii[4^{__CVBuffer}][4^{__CVBuffer}]}16"
+ "supportsFamily:"
+ "VIS-Integrate"
+ "<<<< GyroVideoStabilizationV2 >>>> %!s(MISSING): Unable to perform smart style reverse learning + delta map generation"
+ "enqueueCoefficientsForFiltering:withMetadata:pts:learnedStyle:"
- "v24@0:8^{?=Ciiiiiii[4^{__CVBuffer}]}16"
- "\x92\x11\x1c"
- "\x0f\x0f\x0f\x0f\x05\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa2\x12\x12\x12\x12\x12\x12\x12\x12\x12c\x12"
- "-1"
- "[1@\"<MTLComputePipelineState>\"]"

```
