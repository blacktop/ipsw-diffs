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
+ _objc_msgSend$_blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:
+ _objc_retain_x25
+ _objc_msgSend$supportsFamily:
+ __block_literal_global.140
+ _FigGetCFPreferenceBooleanWithDefault
+ _objc_msgSend$configuration
+ _objc_msgSend$metalDevice
+ OBJC_IVAR_$_affineGPUMetal._forwardCoefficients
+ _objc_msgSend$addObjectsFromArray:
+ _kFigVideoStabilizationSampleBufferProcessorOption_SmartStyleReversibilityEnabled
+ OBJC_IVAR_$_VISConfigurationV2._smartStyleRenderingEnabled
+ _CMIGetPixelFormatInfo
+ _kFigCaptureSampleBufferAttachmentKey_SmartStyleMetalEvent
+ _kFigCaptureSampleBufferMetadata_SmartStyleLearnedRect
+ __block_literal_global.127
+ _OBJC_CLASS_$_CMISmartStyleUtilitiesV1
+ _objc_msgSend$setMemSize:
+ ___invert_f4
+ _objc_msgSend$setExternalMemoryResource:
+ GCC_except_table38
+ __block_literal_global.129
+ _objc_msgSend$getDefaultProcessorConfigurationForStreaming
+ _objc_msgSend$filterCoefficientsForFrameWithMetadata:pts:filterType:toPixelBuffer:
+ _kFigVideoStabilizationSampleBufferAttachmentKey_OutputSmartStyleDeltaMapSampleBuffer
+ _objc_msgSend$globalLinearSystemMixFactor
+ _objc_msgSend$styleEngineConfiguration
+ _kFigVideoStabilizationPixelBufferAttachmentKey_OutputSmartStyleUnstyledPixelBuffer
+ _objc_msgSend$process
+ _kFigVideoStabilizationPixelBufferAttachmentKey_OutputSmartStyleDeltaMapPixelBuffer
+ _kFigVideoStabilizationSampleBufferProcessorOption_SmartStyleRenderingEnabled
+ __runSmartStyleFilterForwardLearning
+ _CMIGetYCCFromRGBConversionMatrixForPixelBuffer
+ _objc_msgSend$smartStyleMemoryPoolId
+ _OBJC_CLASS_$_FigMetalAllocatorBackendDescriptor
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingDeltaMap
+ _kFigCaptureSampleBufferMetadata_SmartStyleLearnedCoefficientsAreFiltered
+ _kFigCaptureStreamMetadataOutputKey_SkyMask
+ -[affineGPUMetal _allocatePyramidWithPixelFormat:bottomLevelWidth:bottomLevelHeight:scaleFactor:includeBottomLevel:minimumDimension:]
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingStyledThumbnail
+ OBJC_IVAR_$_VISConfigurationV2._smartStyleReversibilityEnabled
+ _CMIGetPixelBufferYCCMatrix
+ -[VISWrapper smartStyleReversibilityProcessingEnabled]
+ _objc_msgSend$outputIntegratedStyleCoefficientsTexture
+ _objc_msgSend$setOutputStyledPixelBuffer:
+ _objc_retain_x24
+ _objc_msgSend$setInstanceLabel:
+ _objc_msgSend$setInputUnstyledPixelBuffer:
+ _CGRectGetMidY
+ _objc_msgSend$setWireMemory:
+ OBJC_IVAR_$_affineGPUMetal._fbsEdgeThresholdLuma
+ OBJC_IVAR_$_affineGPUMetal._smoothedLumaPyramid
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingIntegratedReverseLearnedCoefficients
+ __enqueueCoefficientsForSmartStyleFilterForwardLearningFromCoefficientsSampleBuffer
+ -[VISConfigurationV2 setSmartStyleReversibilityEnabled:]
+ __removeSmartStyleAttachments
+ _objc_msgSend$setInputUnstyledThumbnailPixelBuffer:
+ _objc_msgSend$smartStyleRenderingEnabled
+ __runSmartStyleReverseLearningAndComputeDeltaMap
+ _kFigCaptureSampleBufferMetadata_FinalCropRectFromSource
+ -[VISProcessorV2 setSmartStyleReversibilityProcessingEnabled:]
+ OBJC_IVAR_$_affineGPUMetal._inputLumaPyramid
+ -[VISProcessorV2 smartStyleReversibilityProcessingEnabled]
+ _objc_msgSend$numberWithUnsignedLongLong:
+ _objc_msgSend$enqueueCoefficientsForFiltering:withMetadata:pts:
+ _kFigCaptureStreamMetadataOutputKey_HumanSkinsMask
+ _objc_msgSend$lastObject
+ __runSmartStyleReverseLearning
+ _objc_msgSend$setMetalSharedEvent:
+ OBJC_IVAR_$_affineGPUMetal._fbsEdgeThresholdChroma
+ _CMTimeCompare
+ OBJC_IVAR_$_affineGPUMetal._ditherStrengthChroma
+ __block_literal_global.142
+ _kFigCaptureSampleBufferMetadata_SmartStyleIsIdentityCoefficients
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingLinearThumbnail
+ renderWithPixelBuffer:metadata:pixelBufferValidRect:ltmLUT:outputPixelBuffer:isAttachmentRendering:.ditherSeed
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingUnstyledThumbnail
+ OBJC_IVAR_$_affineGPUMetal._intermediateOutputUnstyledPixelBuffer
+ _CVBufferRemoveAttachment
+ ___87-[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]_block_invoke_2
+ OBJC_IVAR_$_VISConfigurationV2._smartStyleMemoryPoolId
+ -[VISConfigurationV2 smartStyleReversibilityEnabled]
+ OBJC_IVAR_$_affineGPUMetal._ditherNoStyle
+ _objc_msgSend$smartStyleReversibilityEnabled
+ _kFigCaptureStreamMetadataOutputKey_PostColorProcessingThumbnail
+ _objc_msgSend$setInputOutput:
+ _objc_msgSend$arrayWithArray:
+ _objc_msgSend$setGlobalLinearSystemMixFactor:
+ _objc_msgSend$_allocatePyramidWithPixelFormat:bottomLevelWidth:bottomLevelHeight:scaleFactor:includeBottomLevel:minimumDimension:
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingReverseLearnedCoefficients
+ OBJC_IVAR_$_VISWrapper._smartStyleReversibilityProcessingEnabled
+ OBJC_IVAR_$_affineGPUMetal._reverseCoefficients
+ GCC_except_table21
+ _objc_msgSend$resetCoefficientsFilter
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingIntegratedForwardLearnedCoefficients
+ -[VISConfigurationV2 setSmartStyleRenderingEnabled:]
+ _kCMTimeNegativeInfinity
+ _OBJC_CLASS_$_NSArray
+ ___87-[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]_block_invoke
+ _objc_msgSend$setInputMetadataDict:
+ OBJC_IVAR_$_affineGPUMetal._inputChromaPyramid
+ _kFigCaptureSampleBufferMetadata_SmartStyleAppliedOnThisFrame
+ __block_literal_global.72
+ _kFigCaptureStreamMetadataOutputKey_HumanHairMask
+ __enqueueCoefficientsForSmartStyleFilterForwardLearning
+ _OBJC_CLASS_$_FigMetalAllocatorBackend
+ _kFigVideoStabilizationSampleBufferProcessorOption_SmartStyleMemoryPoolId
+ _objc_msgSend$setupWithDescriptor:
+ OBJC_IVAR_$_affineGPUMetal._fbsDeltaThresholdLuma
+ __runSmartStyleApplyOnUnstabilizedImage
+ _objc_msgSend$texture2DDescriptorWithPixelFormat:width:height:mipmapped:
+ _OBJC_CLASS_$_CMIExternalMemoryResource
+ _objc_msgSend$setInputStyleCoefficientsPixelBuffer:
+ _CMIGetYCCFromRGBConversionMatrix
+ __runSmartStyleApplyOnUnstabilizedThumbnail
+ OBJC_IVAR_$_affineGPUMetal._smoothedChromaPyramid
+ _ldexpf
+ _objc_msgSend$getRequiredInputBufferSizeForFilterType:
+ _objc_msgSend$computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficients:outputDeltaMapPixelBuffer:
+ _CGRectGetMidX
+ _objc_msgSend$setMemoryPoolId:
+ _objc_msgSend$setPrimaryCaptureRect:
+ GCC_except_table26
+ _objc_msgSend$arrayWithObjects:count:
+ _kFigVideoStabilizationSampleBufferAttachmentKey_OutputSmartStyleUnstyledEnabled
+ _objc_msgSend$initWithDevice:allocatorType:
+ _objc_msgSend$setImageblockWidth:height:
+ -[VISWrapper setSmartStyleReversibilityProcessingEnabled:]
+ OBJC_IVAR_$_affineGPUMetal._fbsDeltaThresholdChroma
+ _objc_msgSend$utilities
+ __updateSmartStyleGlobalMixFactor
+ _objc_msgSend$setAllocatorBackend:
+ OBJC_IVAR_$_affineGPUMetal._ditherStrengthLuma
+ _kFigCaptureSampleBufferAttachedMediaKey_SmartStyleStreamingLearnedCoefficients
+ _sbp_gvs_createStabilizedAttachmentsPixelBuffers
+ _ensureValidBufferRectIsCompatibleWithGPU
+ -[affineGPUMetal _blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:]
+ _objc_msgSend$setTemporalFilterInputBufferSize:
+ _CMIGetRGBFromYCCConversionMatrix
+ __setAttachedMediaToSampleBuffer
+ OBJC_IVAR_$_VISProcessorV2._smartStyleReversibilityProcessingEnabled
+ __shouldBypassSmartStyle
+ _kFigCaptureStreamMetadataOutputKey_HumanFullBodiesMask
+ _objc_msgSend$_getBlurDeltaMapBordersShaderParameters:pipelineIndexToUse:
+ _objc_msgSend$firstObject
+ -[VISConfigurationV2 setSmartStyleMemoryPoolId:]
+ -[VISConfigurationV2 smartStyleRenderingEnabled]
+ _objc_msgSend$learnTransformFrom:to:outputCoefficients:outputIntegratedCoefficients:
+ OBJC_IVAR_$_affineGPUMetal._attachmentIsLinearThumbnail
+ _objc_msgSend$initWithOptionalMetalCommandQueue:
+ _AffineTransformArrayApplyOnAttachment
+ _objc_msgSend$initWithOptionalMetalCommandQueue:useCase:processingType:optionalExternalMemoryResource:
+ _objc_msgSend$setSmartStyleReversibilityProcessingEnabled:
+ _objc_retain_x26
+ -[VISConfigurationV2 smartStyleMemoryPoolId]
+ __runSmartStyleIntegrate
+ _kFigCaptureSampleBufferAttachmentKey_SmartStyleFutureLearnedCoefficientsArray
+ _objc_msgSend$setTexture:atIndex:
- __block_literal_global.103
- __block_literal_global.105
- __block_literal_global.62
- GCC_except_table35
- GCC_except_table23
CStrings:
+ "CMIFastBilateralSmoothing_Remix"
+ "VIS-Apply"
+ "inputUnstyledThumbnailPixelBuffer"
+ "Unable to cache blur previous texture 2 for delta map"
+ "_fbsEdgeThresholdChroma"
+ "cvErr == kCVReturnSuccess"
+ "resetCoefficientsFilter"
+ "inputStabilizedStyledPixelBuffer"
+ "TB,N,V_smartStyleReversibilityProcessingEnabled"
+ "outputDeltaMapPixelBuffer"
+ "( inputYCCMatrixType != kCMIYCCMatrixTypeUnspecified ) && ( inputYCCMatrixType != kCMIYCCMatrixTypeUnsupported )"
+ "setMemoryPoolId:"
+ "_ditherStrengthLuma"
+ "Unable to cache blur previous texture 1 for delta map"
+ "globalLinearSystemMixFactor"
+ "_inputChromaPyramid is NULL"
+ "commandEncoder"
+ "smartStyleExternalMem"
+ "inputOutput"
+ "pyramidArray is nil"
+ "setTexture:atIndex:"
+ "learnTransformFrom:to:outputCoefficients:outputIntegratedCoefficients:"
+ "_smoothedLumaPyramid"
+ "_intermediateOutputUnstyledPixelBuffer"
+ "tex"
+ "inputStabilizedUnstyledPixelBuffer"
+ "inputUnstyledPixelBuffer is NULL"
+ "TB,N,V_smartStyleReversibilityEnabled"
+ "_forwardCoefficients"
+ "setImageblockWidth:height:"
+ "inputStyledThumbnailSampleBuffer"
+ "attachmentsToTransform"
+ "Unable to get deltamap blur borders pipeline"
+ "smartStyleMemoryPoolId"
+ "setInputUnstyledPixelBuffer:"
+ "Unable to get cached destination delta map metal texture"
+ "setWireMemory:"
+ "initWithOptionalMetalCommandQueue:useCase:processingType:optionalExternalMemoryResource:"
+ "getRequiredInputBufferSizeForFilterType:"
+ "initWithOptionalMetalCommandQueue:"
+ "inputTextures.count <= 2"
+ "SmartStyleProcessor"
+ "setSmartStyleReversibilityProcessingEnabled:"
+ "setSmartStyleReversibilityEnabled:"
+ "setInputUnstyledThumbnailPixelBuffer:"
+ "_attachmentIsLinearThumbnail"
+ "inputUnstyledThumbnailSampleBuffer"
+ "( parentInputSize[0] > 0 ) && ( parentInputSize[1] > 0 ) && ( parentOutputSize[0] > 0 ) && ( parentOutputSize[1] > 0 )"
+ "computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficients:outputDeltaMapPixelBuffer:"
+ "( (storage->transformContext.platform) == kTransformGPU )"
+ "_inputLumaPyramid"
+ "scaleFactor must be above 0"
+ "setGlobalLinearSystemMixFactor:"
+ "getDefaultProcessorConfigurationForStreaming"
+ "arrayWithArray:"
+ "setSmartStyleRenderingEnabled:"
+ "inputMetadataDict"
+ "smartStyleReversibilityEnabled"
+ "Could not create FigMetalAllocatorBackendDescriptor"
+ "setPrimaryCaptureRect:"
+ "storage->blurBorderConfig.workDeltaMapPixelBuffer[bufferIdx]"
+ "CMISmartStyleProcessorInputOutputV%!d(MISSING)"
+ "_smartStyleMemoryPoolId"
+ "_smoothedLumaPyramid is NULL"
+ "setMetalSharedEvent:"
+ "CMIFastBilateralSmoothing_Downsample4x"
+ "Unable to cache blur previous texture 0 for delta map"
+ "AttachmentName"
+ "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
+ "outputSampleBuffer"
+ "[3@\"<MTLComputePipelineState>\"]"
+ "\x0f\x0f\x0f\x0f\v\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa2\x12\x12\x12\x12\x12\x12\x12\x12\x12c\x122"
+ "ctx && derivedVectors"
+ "enqueueCoefficientsForFiltering:withMetadata:pts:"
+ "_pipelineComputeStates[BILATERAL_REMIX]"
+ "setInstanceLabel:"
+ "smartStyle.video.reversibilityUses4x3Spotlights"
+ "inputLearnedCoefficientsPixelBuffer"
+ "_inputChromaPyramid"
+ "futureCoefficientsSampleBuffer"
+ "inputSyledPixelBuffer"
+ "setInputOutput:"
+ "_smoothedChromaPyramid is NULL"
+ "arrayWithObjects:count:"
+ "i40@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32"
+ "setInputMetadataDict:"
+ "setOutputStyledPixelBuffer:"
+ "Unable to allocate intermediate pixel buffer to stabilize unstyled frame"
+ "Unable to bind input styled blur pixel buffer"
+ "_reverseCoefficients"
+ "desc"
+ "scaleFactor > 0"
+ "_blurDeltaMapBordersFromStyledPixelBuffer:withUnstyledPixelBuffer:to:"
+ "VIS-Integrate"
+ "setupWithDescriptor:"
+ "inputSampleBuffer is nil"
+ "Could not create FigMetalAllocatorBackend"
+ "rectValid"
+ "destSampleBuffer"
+ "smartStyleRenderingEnabled"
+ "descriptor is nil"
+ "inputSyledPixelBuffer is NULL"
+ "_allocatePyramidWithPixelFormat:bottomLevelWidth:bottomLevelHeight:scaleFactor:includeBottomLevel:minimumDimension:"
+ "backend"
+ "metalDevice"
+ "finalCrecRectValid"
+ "lastObject"
+ "utilities"
+ "addObjectsFromArray:"
+ "Blur copy pipeline is nil"
+ "Unable to get cached destination unstyled metal texture"
+ "_fbsEdgeThresholdLuma"
+ "SmartStyle"
+ "setAllocatorBackend:"
+ "storage->smartStyleContext.renderingEnabled"
+ "attachedMediaDict"
+ "r"
+ "styleEngineConfiguration"
+ "Could not create CMIExternalMemoryResource"
+ "\x92\x11\x15\x17"
+ "_fbsDeltaThresholdLuma"
+ "dispatchThreads:threadsPerThreadgroup:"
+ "texture is nil"
+ "initWithDevice:allocatorType:"
+ "OutputSmartStyleDeltaMapPixelBuffer"
+ "Output pixel buffer does not have YCbCr matrix type specified in attachments"
+ "setMemSize:"
+ "setSmartStyleMemoryPoolId:"
+ "outputDeltaMapPixelBuffer is NULL"
+ "/AppleInternal/VideoProcessors/%!@(MISSING).bundle"
+ "_ditherStrengthChroma"
+ "inputUnstyledPixelBuffer"
+ "Unable to bind input unstyled blur pixel buffer"
+ "Input pixel buffer does not have YCbCr matrix type specified in attachments"
+ "attachedMedia"
+ "smartStyleReversibilityProcessingEnabled"
+ "setInputStyleCoefficientsPixelBuffer:"
+ "_smartStyleReversibilityProcessingEnabled"
+ "com.apple.coremedia"
+ "Unable to cache blur tmp texture 0 for delta map"
+ "attachedMediaDict is nil"
+ "pyramidArray"
+ "inputStyledThumbnailPixelBuffer"
+ "v24@0:8^{?=Ciiiiiii[4^{__CVBuffer}][4^{__CVBuffer}]}16"
+ "Unable to bind output delta map pixel buffer"
+ "_fbsDeltaThresholdChroma"
+ "outputIntegratedStyleCoefficientsTexture"
+ "Failed to setup FigMetalAllocatorBackend"
+ "inputUnstabilizedUnstyledPixelBuffer"
+ "_smartStyleRenderingEnabled"
+ "firstObject"
+ "( outputYCCMatrixType != kCMIYCCMatrixTypeUnspecified ) && ( outputYCCMatrixType != kCMIYCCMatrixTypeUnsupported )"
+ "_inputLumaPyramid is NULL"
+ "@60@0:8Q16Q24Q32Q40B48Q52"
+ "TB,N,V_smartStyleRenderingEnabled"
+ "inputLearnedCoefficientsSampleBuffer"
+ "numberWithUnsignedLongLong:"
+ "_ditherNoStyle"
+ "VIS-SmartStyle-FigMetalAllocatorBackend"
+ "OutputSmartStyleUnstyledPixelBuffer"
+ "_smartStyleReversibilityEnabled"
+ "inputPixelBuffer is nil"
+ "_smoothedChromaPyramid"
+ "TQ,N,V_smartStyleMemoryPoolId"
+ "_pipelineComputeStates[DOWNSAMPLE_4X]"
+ "filterCoefficientsForFrameWithMetadata:pts:filterType:toPixelBuffer:"
+ "supportsFamily:"
+ "Unable to get output delta map color matrix"
+ "sampleBufferToStyle"
+ "setTemporalFilterInputBufferSize:"
- "[1@\"<MTLComputePipelineState>\"]"
- "\x92\x11\x1c"
- "v24@0:8^{?=Ciiiiiii[4^{__CVBuffer}]}16"
- "\x0f\x0f\x0f\x0f\x05\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xa2\x12\x12\x12\x12\x12\x12\x12\x12\x12c\x12"

```
