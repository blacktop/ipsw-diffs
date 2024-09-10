## VideoStabilizationV2

> `/System/Library/VideoProcessors/VideoStabilizationV2.bundle/VideoStabilizationV2`

```diff

-575.14.1.0.0
-  __TEXT.__text: 0x29ed4
-  __TEXT.__auth_stubs: 0xba0
-  __TEXT.__objc_stubs: 0x27c0
-  __TEXT.__objc_methlist: 0x1028
-  __TEXT.__objc_classname: 0x1d3
-  __TEXT.__objc_methname: 0x46cd
-  __TEXT.__objc_methtype: 0x1449
-  __TEXT.__cstring: 0x3c22
-  __TEXT.__const: 0x5e0
-  __TEXT.__gcc_except_tab: 0x16c
-  __TEXT.__unwind_info: 0x4b8
-  __DATA_CONST.__auth_got: 0x5e0
-  __DATA_CONST.__got: 0x628
+575.15.1.0.0
+  __TEXT.__text: 0x32c24
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_stubs: 0x2e40
+  __TEXT.__objc_methlist: 0x10b8
+  __TEXT.__objc_classname: 0x1d5
+  __TEXT.__objc_methname: 0x5020
+  __TEXT.__objc_methtype: 0x14ad
+  __TEXT.__cstring: 0x487b
+  __TEXT.__const: 0x670
+  __TEXT.__gcc_except_tab: 0x3a0
+  __TEXT.__unwind_info: 0x4f8
+  __DATA_CONST.__auth_got: 0x658
+  __DATA_CONST.__got: 0x728
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x1e8
-  __DATA_CONST.__cfstring: 0x740
+  __DATA_CONST.__const: 0x238
+  __DATA_CONST.__cfstring: 0x900
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x2718
   __DATA_CONST.__objc_dictobj: 0x960
   __DATA_CONST.__objc_arrayobj: 0x1680
-  __DATA.__objc_const: 0x48d0
-  __DATA.__objc_selrefs: 0xc50
-  __DATA.__objc_ivar: 0x3e0
+  __DATA.__objc_const: 0x4ce0
+  __DATA.__objc_selrefs: 0xdf8
+  __DATA.__objc_ivar: 0x430
   __DATA.__objc_data: 0x460
   __DATA.__data: 0x300
   __DATA.__bss: 0x24

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 478
-  Symbols:   1621
-  CStrings:  1460
+  Functions: 508
+  Symbols:   1775
+  CStrings:  1631
 
Symbols:
+ _objc_msgSend$setMemSize:
+ _objc_msgSend$texture2DDescriptorWithPixelFormat:width:height:mipmapped:
+ _kFigVideoStabilizationSampleBufferAttachmentKey_OutputSmartStyleDeltaMapSampleBuffer
+ _objc_msgSend$arrayWithObjects:count:
+ _CVBufferRemoveAttachment
+ _FigGetCFPreferenceBooleanWithDefault
+ _kFigVideoStabilizationSampleBufferProcessorOption_SmartStyleMemoryPoolId
+ GCC_except_table38
+ _kFigCaptureSampleBufferAttachmentKey_SmartStyleFutureLearnedCoefficientsArray
+ _objc_msgSend$setGlobalLinearSystemMixFactor:
+ __runSmartStyleReverseLearningAndComputeDeltaMap
+ _CGRectGetMidX
+ _ldexpf
+ _kFigCaptureSampleBufferMetadata_SmartStyleIsIdentityCoefficients
+ _objc_msgSend$setupWithDescriptor:
+ _objc_msgSend$setOutputStyledPixelBuffer:
+ OBJC_IVAR_$_affineGPUMetal._fbsEdgeThresholdLuma
+ OBJC_IVAR_$_affineGPUMetal._fbsDeltaThresholdChroma
+ OBJC_IVAR_$_affineGPUMetal._attachmentIsLinearThumbnail
+ __block_literal_global.142
+ _objc_msgSend$setWireMemory:
+ ___87-[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]_block_invoke
+ _objc_msgSend$_getBlurDeltaMapBordersShaderParameters:pipelineIndexToUse:
+ -[VISWrapper setSmartStyleReversibilityProcessingEnabled:]
+ _objc_msgSend$setTexture:atIndex:
+ _kFigCaptureStreamMetadataOutputKey_SkyMask
+ _CMIGetPixelFormatInfo
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingUnstyledThumbnail
+ _objc_retain_x24
+ _kFigCaptureSampleBufferMetadata_SmartStyleLearnedCoefficientsAreFiltered
+ _kFigCaptureStreamMetadataOutputKey_PostColorProcessingThumbnail
+ _CMIGetYCCFromRGBConversionMatrix
+ _objc_msgSend$styleEngineConfiguration
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingLinearThumbnail
+ -[VISProcessorV2 setSmartStyleReversibilityProcessingEnabled:]
+ _objc_msgSend$_allocatePyramidWithPixelFormat:bottomLevelWidth:bottomLevelHeight:scaleFactor:includeBottomLevel:minimumDimension:
+ _objc_msgSend$smartStyleRenderingEnabled
+ _objc_retain_x25
+ -[VISConfigurationV2 smartStyleRenderingEnabled]
+ __runSmartStyleReverseLearning
+ __runSmartStyleApplyOnUnstabilizedImage
+ _objc_msgSend$setInputMetadataDict:
+ -[VISConfigurationV2 smartStyleReversibilityEnabled]
+ GCC_except_table21
+ _objc_msgSend$setInputOutput:
+ _objc_msgSend$setImageblockWidth:height:
+ OBJC_IVAR_$_affineGPUMetal._forwardCoefficients
+ _objc_msgSend$setExternalMemoryResource:
+ _objc_msgSend$initWithOptionalMetalCommandQueue:useCase:processingType:optionalExternalMemoryResource:
+ renderWithPixelBuffer:metadata:pixelBufferValidRect:ltmLUT:outputPixelBuffer:isAttachmentRendering:.ditherSeed
+ _objc_msgSend$outputIntegratedStyleCoefficientsTexture
+ OBJC_IVAR_$_affineGPUMetal._intermediateOutputUnstyledPixelBuffer
+ _sbp_gvs_createStabilizedAttachmentsPixelBuffers
+ OBJC_IVAR_$_affineGPUMetal._smoothedChromaPyramid
+ _kFigCaptureStreamMetadataOutputKey_HumanFullBodiesMask
+ _kFigVideoStabilizationSampleBufferAttachmentKey_OutputSmartStyleUnstyledEnabled
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingReverseLearnedCoefficients
+ OBJC_IVAR_$_VISConfigurationV2._smartStyleReversibilityEnabled
+ _CMIGetPixelBufferYCCMatrix
+ _objc_msgSend$smartStyleMemoryPoolId
+ -[VISConfigurationV2 smartStyleMemoryPoolId]
+ _objc_msgSend$resetCoefficientsFilter
+ _objc_msgSend$setTemporalFilterInputBufferSize:
+ _CMIGetRGBFromYCCConversionMatrix
+ _objc_msgSend$learnTransformFrom:to:outputCoefficients:outputIntegratedCoefficients:
+ _kFigCaptureStreamMetadataOutputKey_HumanHairMask
+ __block_literal_global.140
+ _objc_msgSend$utilities
+ _CGRectGetMidY
+ _kFigVideoStabilizationPixelBufferAttachmentKey_OutputSmartStyleDeltaMapPixelBuffer
+ _kFigVideoStabilizationPixelBufferAttachmentKey_OutputSmartStyleUnstyledPixelBuffer
+ __removeSmartStyleAttachments
+ OBJC_IVAR_$_VISConfigurationV2._smartStyleRenderingEnabled
+ OBJC_IVAR_$_VISProcessorV2._smartStyleReversibilityProcessingEnabled
+ -[VISProcessorV2 smartStyleReversibilityProcessingEnabled]
+ _objc_msgSend$setMemoryPoolId:
+ _objc_msgSend$_blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:
+ _CMIGetYCCFromRGBConversionMatrixForPixelBuffer
+ _objc_msgSend$smartStyleReversibilityEnabled
+ _objc_msgSend$setAllocatorBackend:
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _objc_msgSend$initWithDevice:allocatorType:
+ _objc_msgSend$metalDevice
+ _kFigVideoStabilizationSampleBufferProcessorOption_SmartStyleReversibilityEnabled
+ _objc_msgSend$getRequiredInputBufferSizeForFilterType:
+ _objc_msgSend$setInputUnstyledThumbnailPixelBuffer:
+ _objc_msgSend$setMetalSharedEvent:
+ _objc_msgSend$setSmartStyleReversibilityProcessingEnabled:
+ OBJC_IVAR_$_affineGPUMetal._fbsDeltaThresholdLuma
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingLearnedCoefficients
+ _OBJC_CLASS_$_CMISmartStyleUtilitiesV1
+ -[VISConfigurationV2 setSmartStyleRenderingEnabled:]
+ __enqueueCoefficientsForSmartStyleFilterForwardLearningFromCoefficientsSampleBuffer
+ __block_literal_global.72
+ OBJC_IVAR_$_affineGPUMetal._ditherStrengthChroma
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _AffineTransformArrayApplyOnAttachment
+ __block_literal_global.127
+ _kFigCaptureSampleBufferMetadata_FinalCropRectFromSource
+ _objc_msgSend$supportsFamily:
+ _CMTimeCompare
+ __block_literal_global.129
+ _OBJC_CLASS_$_FigMetalAllocatorBackendDescriptor
+ OBJC_IVAR_$_affineGPUMetal._ditherNoStyle
+ _objc_msgSend$filterCoefficientsForFrameWithMetadata:pts:filterType:toPixelBuffer:
+ __runSmartStyleFilterForwardLearning
+ _objc_msgSend$getDefaultProcessorConfigurationForStreaming
+ ___invert_f4
+ -[VISWrapper smartStyleReversibilityProcessingEnabled]
+ OBJC_IVAR_$_affineGPUMetal._reverseCoefficients
+ _objc_msgSend$computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficients:outputDeltaMapPixelBuffer:
+ OBJC_IVAR_$_affineGPUMetal._inputChromaPyramid
+ _OBJC_CLASS_$_CMIExternalMemoryResource
+ OBJC_IVAR_$_affineGPUMetal._smoothedLumaPyramid
+ __shouldBypassSmartStyle
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingStyledThumbnail
+ -[VISConfigurationV2 setSmartStyleReversibilityEnabled:]
+ -[affineGPUMetal _allocatePyramidWithPixelFormat:bottomLevelWidth:bottomLevelHeight:scaleFactor:includeBottomLevel:minimumDimension:]
+ _kFigCaptureStreamMetadataOutputKey_HumanSkinsMask
+ _OBJC_CLASS_$_NSArray
+ __updateSmartStyleGlobalMixFactor
+ _objc_msgSend$addObjectsFromArray:
+ _kFigCaptureSampleBufferMetadata_SmartStyleAppliedOnThisFrame
+ _objc_msgSend$process
+ _objc_retain_x26
+ _objc_msgSend$lastObject
+ _kFigCaptureSampleBufferAttachmentKey_SmartStyleMetalEvent
+ __runSmartStyleApplyOnUnstabilizedThumbnail
+ _objc_msgSend$setInputUnstyledPixelBuffer:
+ _objc_msgSend$globalLinearSystemMixFactor
+ _objc_msgSend$enqueueCoefficientsForFiltering:withMetadata:pts:
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingIntegratedReverseLearnedCoefficients
+ OBJC_IVAR_$_affineGPUMetal._inputLumaPyramid
+ __enqueueCoefficientsForSmartStyleFilterForwardLearning
+ OBJC_IVAR_$_VISWrapper._smartStyleReversibilityProcessingEnabled
+ -[VISConfigurationV2 setSmartStyleMemoryPoolId:]
+ OBJC_IVAR_$_affineGPUMetal._fbsEdgeThresholdChroma
+ _kCMTimeNegativeInfinity
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingIntegratedForwardLearnedCoefficients
+ _ensureValidBufferRectIsCompatibleWithGPU
+ ___87-[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]_block_invoke_2
+ _objc_msgSend$arrayWithArray:
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingDeltaMap
+ _OBJC_CLASS_$_FigMetalAllocatorBackend
+ _objc_msgSend$setInputStyleCoefficientsPixelBuffer:
+ _objc_msgSend$setInstanceLabel:
+ __runSmartStyleIntegrate
+ OBJC_IVAR_$_affineGPUMetal._ditherStrengthLuma
+ _objc_msgSend$configuration
+ _kFigCaptureSampleBufferMetadata_SmartStyleLearnedRect
+ -[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]
+ __setAttachedMediaToSampleBuffer
+ _objc_msgSend$firstObject
+ _objc_msgSend$initWithOptionalMetalCommandQueue:
+ GCC_except_table26
+ _kFigVideoStabilizationSampleBufferProcessorOption_SmartStyleRenderingEnabled
+ OBJC_IVAR_$_VISConfigurationV2._smartStyleMemoryPoolId
+ _objc_msgSend$setPrimaryCaptureRect:
- GCC_except_table35
- __block_literal_global.62
- __block_literal_global.105
- GCC_except_table23
- __block_literal_global.103
CStrings:
+ "setSmartStyleReversibilityProcessingEnabled:"
+ "setupWithDescriptor:"
+ "_smartStyleRenderingEnabled"
+ "attachmentsToTransform"
+ "Unable to bind output delta map pixel buffer"
+ "\x92\x11\x15\x17"
+ "Blur copy pipeline is nil"
+ "_inputChromaPyramid is NULL"
+ "com.apple.coremedia"
+ "backend"
+ "firstObject"
+ "setInstanceLabel:"
+ "texture is nil"
+ "initWithDevice:allocatorType:"
+ "numberWithUnsignedLongLong:"
+ "descriptor is nil"
+ "Could not create FigMetalAllocatorBackend"
+ "_inputChromaPyramid"
+ "cvErr == kCVReturnSuccess"
+ "Unable to bind input unstyled blur pixel buffer"
+ "_smartStyleMemoryPoolId"
+ "\x0f\x0f\x0f\x0f\v\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa2\x12\x12\x12\x12\x12\x12\x12\x12\x12c\x122"
+ "computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficients:outputDeltaMapPixelBuffer:"
+ "_ditherNoStyle"
+ "TB,N,V_smartStyleRenderingEnabled"
+ "outputSampleBuffer"
+ "ctx && derivedVectors"
+ "attachedMedia"
+ "OutputSmartStyleDeltaMapPixelBuffer"
+ "smartStyleMemoryPoolId"
+ "_fbsEdgeThresholdLuma"
+ "setSmartStyleMemoryPoolId:"
+ "initWithOptionalMetalCommandQueue:"
+ "_attachmentIsLinearThumbnail"
+ "_ditherStrengthLuma"
+ "_pipelineComputeStates[DOWNSAMPLE_4X]"
+ "SmartStyleProcessor"
+ "initWithOptionalMetalCommandQueue:useCase:processingType:optionalExternalMemoryResource:"
+ "v24@0:8^{?=Ciiiiiii[4^{__CVBuffer}][4^{__CVBuffer}]}16"
+ "setMemoryPoolId:"
+ "( (storage->transformContext.platform) == kTransformGPU )"
+ "Could not create FigMetalAllocatorBackendDescriptor"
+ "_allocatePyramidWithPixelFormat:bottomLevelWidth:bottomLevelHeight:scaleFactor:includeBottomLevel:minimumDimension:"
+ "_fbsEdgeThresholdChroma"
+ "setSmartStyleReversibilityEnabled:"
+ "VIS-SmartStyle-FigMetalAllocatorBackend"
+ "smartStyleRenderingEnabled"
+ "i40@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32"
+ "setTemporalFilterInputBufferSize:"
+ "rectValid"
+ "/AppleInternal/VideoProcessors/%!@(MISSING).bundle"
+ "setWireMemory:"
+ "_ditherStrengthChroma"
+ "attachedMediaDict"
+ "inputStabilizedStyledPixelBuffer"
+ "lastObject"
+ "_inputLumaPyramid is NULL"
+ "inputUnstabilizedUnstyledPixelBuffer"
+ "learnTransformFrom:to:outputCoefficients:outputIntegratedCoefficients:"
+ "Unable to get output delta map color matrix"
+ "Failed to setup FigMetalAllocatorBackend"
+ "Unable to cache blur previous texture 2 for delta map"
+ "TB,N,V_smartStyleReversibilityEnabled"
+ "setOutputStyledPixelBuffer:"
+ "inputSyledPixelBuffer"
+ "inputStabilizedUnstyledPixelBuffer"
+ "styleEngineConfiguration"
+ "Input pixel buffer does not have YCbCr matrix type specified in attachments"
+ "_smartStyleReversibilityProcessingEnabled"
+ "_smoothedChromaPyramid is NULL"
+ "setInputOutput:"
+ "Unable to cache blur tmp texture 0 for delta map"
+ "_smoothedLumaPyramid is NULL"
+ "inputUnstyledThumbnailSampleBuffer"
+ "futureCoefficientsSampleBuffer"
+ "inputTextures.count <= 2"
+ "_pipelineComputeStates[BILATERAL_REMIX]"
+ "commandEncoder"
+ "_fbsDeltaThresholdLuma"
+ "inputStyledThumbnailSampleBuffer"
+ "smartStyle.video.reversibilityUses4x3Spotlights"
+ "setMetalSharedEvent:"
+ "inputUnstyledThumbnailPixelBuffer"
+ "VIS-Apply"
+ "AttachmentName"
+ "setSmartStyleRenderingEnabled:"
+ "storage->blurBorderConfig.workDeltaMapPixelBuffer[bufferIdx]"
+ "arrayWithArray:"
+ "@60@0:8Q16Q24Q32Q40B48Q52"
+ "outputDeltaMapPixelBuffer is NULL"
+ "setInputUnstyledThumbnailPixelBuffer:"
+ "tex"
+ "globalLinearSystemMixFactor"
+ "inputLearnedCoefficientsSampleBuffer"
+ "inputUnstyledPixelBuffer is NULL"
+ "inputPixelBuffer is nil"
+ "setAllocatorBackend:"
+ "Unable to get cached destination delta map metal texture"
+ "Unable to allocate intermediate pixel buffer to stabilize unstyled frame"
+ "_smoothedLumaPyramid"
+ "TB,N,V_smartStyleReversibilityProcessingEnabled"
+ "getRequiredInputBufferSizeForFilterType:"
+ "CMISmartStyleProcessorInputOutputV%!d(MISSING)"
+ "setMemSize:"
+ "( outputYCCMatrixType != kCMIYCCMatrixTypeUnspecified ) && ( outputYCCMatrixType != kCMIYCCMatrixTypeUnsupported )"
+ "pyramidArray is nil"
+ "outputIntegratedStyleCoefficientsTexture"
+ "setPrimaryCaptureRect:"
+ "OutputSmartStyleUnstyledPixelBuffer"
+ "inputMetadataDict"
+ "getDefaultProcessorConfigurationForStreaming"
+ "setInputUnstyledPixelBuffer:"
+ "_smoothedChromaPyramid"
+ "enqueueCoefficientsForFiltering:withMetadata:pts:"
+ "Unable to get cached destination unstyled metal texture"
+ "scaleFactor must be above 0"
+ "outputDeltaMapPixelBuffer"
+ "attachedMediaDict is nil"
+ "r"
+ "storage->smartStyleContext.renderingEnabled"
+ "scaleFactor > 0"
+ "metalDevice"
+ "smartStyleReversibilityEnabled"
+ "supportsFamily:"
+ "TQ,N,V_smartStyleMemoryPoolId"
+ "_inputLumaPyramid"
+ "inputOutput"
+ "CMIFastBilateralSmoothing_Remix"
+ "_forwardCoefficients"
+ "finalCrecRectValid"
+ "CMIFastBilateralSmoothing_Downsample4x"
+ "_blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:"
+ "_smartStyleReversibilityEnabled"
+ "smartStyleExternalMem"
+ "Unable to cache blur previous texture 1 for delta map"
+ "setGlobalLinearSystemMixFactor:"
+ "inputStyledThumbnailPixelBuffer"
+ "inputSyledPixelBuffer is NULL"
+ "smartStyleReversibilityProcessingEnabled"
+ "addObjectsFromArray:"
+ "_fbsDeltaThresholdChroma"
+ "desc"
+ "( inputYCCMatrixType != kCMIYCCMatrixTypeUnspecified ) && ( inputYCCMatrixType != kCMIYCCMatrixTypeUnsupported )"
+ "inputLearnedCoefficientsPixelBuffer"
+ "setInputStyleCoefficientsPixelBuffer:"
+ "[3@\"<MTLComputePipelineState>\"]"
+ "setImageblockWidth:height:"
+ "resetCoefficientsFilter"
+ "setTexture:atIndex:"
+ "destSampleBuffer"
+ "Unable to get deltamap blur borders pipeline"
+ "_reverseCoefficients"
+ "dispatchThreads:threadsPerThreadgroup:"
+ "filterCoefficientsForFrameWithMetadata:pts:filterType:toPixelBuffer:"
+ "pyramidArray"
+ "Unable to cache blur previous texture 0 for delta map"
+ "inputUnstyledPixelBuffer"
+ "( parentInputSize[0] > 0 ) && ( parentInputSize[1] > 0 ) && ( parentOutputSize[0] > 0 ) && ( parentOutputSize[1] > 0 )"
+ "Output pixel buffer does not have YCbCr matrix type specified in attachments"
+ "setInputMetadataDict:"
+ "VIS-Integrate"
+ "_intermediateOutputUnstyledPixelBuffer"
+ "Unable to bind input styled blur pixel buffer"
+ "sampleBufferToStyle"
+ "SmartStyle"
+ "inputSampleBuffer is nil"
+ "arrayWithObjects:count:"
+ "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
+ "utilities"
+ "Could not create CMIExternalMemoryResource"
- "\x0f\x0f\x0f\x0f\x05\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa2\x12\x12\x12\x12\x12\x12\x12\x12\x12c\x12"
- "[1@\"<MTLComputePipelineState>\"]"
- "\x92\x11\x1c"
- "v24@0:8^{?=Ciiiiiii[4^{__CVBuffer}]}16"

```
