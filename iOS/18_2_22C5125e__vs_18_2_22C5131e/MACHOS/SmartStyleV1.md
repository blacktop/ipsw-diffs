## SmartStyleV1

> `/System/Library/VideoProcessors/SmartStyleV1.bundle/SmartStyleV1`

```diff

-587.60.10.122.3
-  __TEXT.__text: 0x115dc
-  __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_stubs: 0x1da0
-  __TEXT.__objc_methlist: 0xa40
-  __TEXT.__const: 0x68
-  __TEXT.__objc_methname: 0x4206
-  __TEXT.__cstring: 0x2d72
-  __TEXT.__oslogstring: 0x209a
+587.60.14.122.2
+  __TEXT.__text: 0xa7b8
+  __TEXT.__auth_stubs: 0x420
+  __TEXT.__objc_stubs: 0x1e20
+  __TEXT.__objc_methlist: 0xa70
+  __TEXT.__objc_methname: 0x4301
+  __TEXT.__cstring: 0x14db
   __TEXT.__objc_classname: 0x25e
   __TEXT.__objc_methtype: 0x10c6
-  __TEXT.__unwind_info: 0x1a0
-  __DATA_CONST.__auth_got: 0x230
+  __TEXT.__const: 0x28
+  __TEXT.__unwind_info: 0x180
+  __DATA_CONST.__auth_got: 0x218
   __DATA_CONST.__got: 0x180
   __DATA_CONST.__const: 0x40
-  __DATA_CONST.__cfstring: 0x2e0
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0xc0
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x3610
-  __DATA.__objc_selrefs: 0x960
-  __DATA.__objc_ivar: 0x1b4
+  __DATA.__objc_const: 0x3710
+  __DATA.__objc_selrefs: 0x980
+  __DATA.__objc_ivar: 0x1bc
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x3c0
   __DATA.__common: 0x60

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 214
-  Symbols:   816
-  CStrings:  1020
+  Functions: 218
+  Symbols:   823
+  CStrings:  828
 
Symbols:
+ -[CMISmartStyleProcessorInputOutputV1 outputImageStatisticsExtended]
+ -[CMISmartStyleProcessorInputOutputV1 personMasksValidHint]
+ -[CMISmartStyleProcessorInputOutputV1 setOutputImageStatisticsExtended:]
+ -[CMISmartStyleProcessorInputOutputV1 setPersonMasksValidHint:]
+ OBJC_IVAR_$_CMISmartStyleProcessorInputOutputV1._outputImageStatisticsExtended
+ OBJC_IVAR_$_CMISmartStyleProcessorInputOutputV1._personMasksValidHint
+ _FigSignalErrorAt
+ _fig_log_get_emitter
+ _objc_msgSend$outputImageStatisticsExtended
+ _objc_msgSend$personMasksValidHint
+ _objc_msgSend$setOutputImageStatisticsExtended:
+ _objc_msgSend$setPersonMasksValidHint:
+ _objc_retain_x22
+ _objc_retain_x24
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_note_initialize_category_with_default_work_cf
- _objc_retain_x26
- _os_log_type_enabled
CStrings:
+ "2B\x91b\x12"
+ "T@\"NSMutableDictionary\",&,N,V_outputImageStatisticsExtended"
+ "Tf,N,V_personMasksValidHint"
+ "_outputImageStatisticsExtended"
+ "_personMasksValidHint"
+ "outputImageStatisticsExtended"
+ "personMasksValidHint"
+ "setOutputImageStatisticsExtended:"
+ "setPersonMasksValidHint:"
- "\"B\x91a\x12"
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "-1"
- "-[CMISmartStyleOvercaptureThumbnailGenerator _bindPixelBufferToMTL2DTexture:pixelFormat:usage:plane:]"
- "-[CMISmartStyleOvercaptureThumbnailGenerator _metalPixelFormatForPixelbuffer:]"
- "-[CMISmartStyleOvercaptureThumbnailGenerator generateOvercaptureIntegrationThumbnailFromPreviewThumbnailPixelBuffer:stitcherOutputPixelBuffer:outputOvercaptureIntegrationThumbnailPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransformForPreviewThumbnailPixelBuffer:optionalCommandBuffer:]"
- "-[CMISmartStyleOvercaptureThumbnailGenerator initWithOptionalCommandQueue:]"
- "-[CMISmartStyleProcessorInputOutputV1 init]"
- "-[CMISmartStyleProcessorInputOutputV1 setInputSmartStyle:]"
- "-[CMISmartStyleProcessorStillImageConfigurationV1 init]"
- "-[CMISmartStyleProcessorStreamingConfigurationV1 init]"
- "-[CMISmartStyleProcessorUtilitiesV1 _cachedTexturesFromPixelBuffer:usage:]"
- "-[CMISmartStyleProcessorUtilitiesV1 _compileShaders]"
- "-[CMISmartStyleProcessorUtilitiesV1 _computeLinearThumbnailValidRegion:]"
- "-[CMISmartStyleProcessorUtilitiesV1 blitPixelBuffer:toPixelBuffer:]"
- "-[CMISmartStyleProcessorUtilitiesV1 createIdentityTransformCoefficients:]"
- "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:]"
- "-[CMISmartStyleProcessorUtilitiesV1 createLinearThumbnailFromMetadata:preLTMThumbnailPixelBuffer:postLTMThumbnailPixelBuffer:cameraInfo:applyGDC:cropToPreLTMBounds:toPixelBuffer:]"
- "-[CMISmartStyleProcessorUtilitiesV1 getPreLTMValidROIFromMetadata:inputPreLTMThumbnailPixelBuffer:outputRect:]"
- "-[CMISmartStyleProcessorUtilitiesV1 initWithStyleEngine:temporalFilterBufferSize:withMetalContext:]"
- "-[CMISmartStyleProcessorUtilitiesV1 runFPRejectionOnMask:originalMask:]"
- "-[CMISmartStyleProcessorUtilitiesV1 undistortMask:inputPixelBuffer:inputMetadata:cameraInfo:toPixelBuffer:]"
- "-[CMISmartStyleProcessorV1 _configureInputLinearPixelBufferForPixelBufferRenderer:withinputLinearCropRect:]"
- "-[CMISmartStyleProcessorV1 _configureInputUnstyledPixelBufferForPixelBufferRenderer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:]"
- "-[CMISmartStyleProcessorV1 _configureOutputStyledThumbnailPixelBufferForPixelBufferRenderer:unstyledThumbnailPixelBuffer:]"
- "-[CMISmartStyleProcessorV1 _configureStyleEngineInputUnstyledThumbnailPixelBuffer:withinputUnstyledCropRect:inputUnstyledThumbnailPixelBuffer:withinputUnstyledThumbnailCropRect:inputUnstyledThumbnailUsedForTargetGenerationPixelBuffer:withInputUnstyledThumbnailUsedForTargetGenerationCropRect:]"
- "-[CMISmartStyleProcessorV1 _configureStyleEngineTargetThumbnailPixelBuffer:inputTargetThumbnailPixelBuffer:]"
- "-[CMISmartStyleProcessorV1 _requestedMemSize:]"
- "-[CMISmartStyleProcessorV1 externalMemoryDescriptorForConfiguration:]"
- "-[CMISmartStyleProcessorV1 finishProcessing]"
- "-[CMISmartStyleProcessorV1 initWithOptionalMetalCommandQueue:]"
- "-[CMISmartStyleProcessorV1 init]"
- "-[CMISmartStyleProcessorV1 prepareToProcess:]"
- "-[CMISmartStyleProcessorV1 prewarm]"
- "-[CMISmartStyleProcessorV1 process]"
- "-[CMISmartStyleProcessorV1 purgeResources]"
- "-[CMISmartStyleProcessorV1 resetState]"
- "-[CMISmartStyleProcessorV1 setup]"
- "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>>"
- "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %!s(MISSING): MetalContext is nil"
- "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %!s(MISSING): Pixel buffer %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING) format not supported"
- "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %!s(MISSING): Shaders compilation failed."
- "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %!s(MISSING): Unable to init CMISmartStyleOvercaptureThumbnailGenerator."
- "<<<< CMISmartStyleOvercaptureThumbnailGenerator >>>> %!s(MISSING): Unable to load the bundle for CMISmartStyleOvercaptureThumbnailGenerator."
- "<<<< CMISmartStyleProcessor >>>>"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : Shifting inputImageRect.origin by deltaMapRegionToRenderRect.origin = ( %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : deltaMapRegionToRenderRect = ( %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : imageSize = ( %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : inputImageRect = ( %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : inputOriginalImageRect = ( %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : inputReferenceForDeltaMapComputationCropRect = ( %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : inputUnstyledCropRect = ( %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : outputDeltaMapCropRect = ( %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : outputImageRect = ( %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): %!p(MISSING) : outputStyledCropRect = ( %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) ; %!d(MISSING) )"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Already prepared to process processingType: %!d(MISSING)"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Found Styles metal event in metadata in CMISmartStyleProcessorV1 instance %!@(MISSING)"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Metal command queue is nil"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): MetalContext is nil"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Setting up SmartStyleProcessor with provided metal command queue."
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Smart style engine processor failed to prepare to process (err:%!d(MISSING))"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): SmartStyle Processor (label:%!@(MISSING)) is requesting memory of size:%!z(MISSING)u"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Unable to initialize a smart style processor configuration"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Unable to initialize a smart style processor input output"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Unable to initialize a smart style processor instance"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Unable to load the bundle for smart style processor."
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Unexpected state: after receiving valid masks curve parameter must stay valid"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Unsupported Smart Style version %!d(MISSING)"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): Using external metal allocator (size:%!l(MISSING)u MB)"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): _smartStylePixelBufferRenderer is nil"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): _styleEngineProcessor is nil"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): _subjectRelightingStage is nil"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): _utilities is nil"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): externalMemoryDescriptor is nil"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): prepareToProcess for %!d(MISSING)"
- "<<<< CMISmartStyleProcessor >>>> %!s(MISSING): requesting GPU metal heap size without preparing to process for processor (label:%!@(MISSING)), requesting the max size:%!z(MISSING)u "
- "<<<< CMISmartStyleProcessorUtilities >>>>"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Clipping data has invalid threshold bin index"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Clipping data is NULL"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Clipping header dataSize is invalid"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Clipping header is NULL"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Clipping metadata is NULL"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Failed to bind original mask pixel buffer as texture"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Failed to bind refined mask pixel buffer as texture"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Failed to create identity transform coefficients, err = %!d(MISSING)"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Invalud clipping data grid size"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Pixel buffer %!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING) format not supported"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): PreLTM thumbnail size height sent is too big"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): PreLTM thumbnail size width sent is too big"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Style engine processor is nil. Unable to init a smart style processor utilities"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Unable to apply GDC correction linear thumbnail as cameraInfo is nil, bypassing GDC correction"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Unable to cache pixel buffer texture"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Unable to create a metal texture cache"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Unable to get GDC params, bypassing GDC correction"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Unable to get metal texture address"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): Unable to initialize a smart style processor instance"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): _coefficientsProcessor is nil. Unable to init a smart style processor utilities."
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): blitEncoder is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): cameraInfo is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): commandBuffer is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): commandEncoder is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): gridOriginX should be >= 0"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): gridOriginX+extentX should be lower than rawSensorWidth"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): gridOriginY should be >= 0"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): gridOriginY+extentY should be lower than rawSensorHeight"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputLinearThumbnailData doesn't contain blue channel"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputLinearThumbnailData doesn't contain green channel"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputLinearThumbnailData doesn't contain red channel"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputLinearThumbnailData has wrong size"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputLinearThumbnailData is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputMaskPixelBuffer is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputMaskTexture is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputMetadata is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputOutputPreLTMThumbnailTexture is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputPixelBuffer is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputPostLTMThumbnailPixelBuffer is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputPostLTMThumbnailTexture is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputPreLTMPixelBuffer is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputPreLTMThumbnailBuffer is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): inputTexture for blit is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): metal context is nil. Unable to init a smart style processor utilities."
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): outputMaskTexture is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): outputPixelBuffer is NULL"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): outputTexture for blit is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): outputTexture is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): pixelBuffer is NULL"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): postLTMThumbnailTexture is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): preLTM thumbnail size coming from ISP is %!d(MISSING)x%!d(MISSING)"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): preLTMThumbnail (%!d(MISSING),%!d(MISSING)) - ROI is (%!f(MISSING),%!f(MISSING),%!f(MISSING),%!f(MISSING))"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): preLTMThumbnail ROI computed with clipping metadata is (%!f(MISSING),%!f(MISSING),%!f(MISSING),%!f(MISSING))"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): preLTMThumbnail ROI computed with fallback clipping metadata is (%!f(MISSING),%!f(MISSING),%!f(MISSING),%!f(MISSING))"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): preLTMThumbnail ROI computed with mapped sensor rect metadata is (%!f(MISSING),%!f(MISSING),%!f(MISSING),%!f(MISSING))"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): preLTMThumbnailTexture is nil"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): rawSensorHeight is 0"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): rawSensorWidth is 0"
- "<<<< CMISmartStyleProcessorUtilities >>>> %!s(MISSING): totalSensorCropRect metadata not found"
- "CMISmartStyleRendererStatusInputError"
- "CMISmartStyleRendererStatusRenderingFailed"
- "CMISmartStyleStatusConfigurationFailed"
- "CMISmartStyleStatusInputError"
- "CMISmartStyleStatusOtherAllocationFailed"
- "CMISmartStyleStatusOtherError"
- "CMISmartStyleStatusRenderingError"
- "CMISmartStyleStatusStyleEngineError"
- "Could not bind destination pixel buffer"
- "Could not bind source pixel buffer"
- "Downscaling input linear pixel buffer to the linear thumbnail pixel buffer failed"
- "Downscaling input target pixel buffer to style engine input target styled thumbnail pixel buffer failed"
- "Downscaling input unstyled pixel buffer to the style renderer unstyled thumbnail pixel buffer failed"
- "Downscaling style renderer styled output to style engine input target thumbnail pixel buffer failed"
- "Downscaling style renderer unstyled thumbnail to style engine input unstyled thumbnail pixel buffer failed"
- "FIGMETALCONTEXT_CHECK_ERRCODE"
- "Failed to load tuning parameters"
- "FigMetalAllocator setupWithDescriptor failed"
- "FigMetalAllocator setupWithDescriptor:allocatorBackend failed"
- "Input target thumbnail pixel buffer dimensions don;t match StyleEngine thumbnail configuration"
- "Renderer failed to prewarm"
- "Renderer failed to reset state"
- "Smart style configuration is not conforming to still or streaming configuration"
- "Smart style configuration is not set"
- "Smart style renderer failed to prepare to process"
- "Smart style renderer failed to process"
- "Style engine failed to prewarm"
- "Style engine failed to process"
- "Style engine failed to purge resources"
- "Style engine failed to reset state"
- "Style engine failed to setup"
- "Style engine setup failed"
- "Style processor subprocessors need to be on the same command queue"
- "Style renderer failed to purge resources"
- "Style renderer failed to setup"
- "Unable to cache pixel buffer texture"
- "Unable to create an intermediate buffer to for unstyled input thumbnail for style engine learning"
- "Unable to create an intermediate buffer to produce styled rendering"
- "Unable to find unstyled buffer to produce styled rendering"
- "Unable to get texture address"
- "Unsupported pixel buffer format for input"
- "Unsupported pixel buffer format for output"
- "Unsupported processing type"
- "_cmImagingAllocator is NULL"
- "_createLinearThumbnailCroppedToPreLTMPipelineState is NULL"
- "_createLinearThumbnailCroppedToPreLTMPipelineStateWithGDC is NULL"
- "_createLinearThumbnailPipelineState is NULL"
- "_createLinearThumbnailPipelineStateWithGDC is NULL"
- "_extractLinearThumbnailPipelineState is NULL"
- "_maskFalsePositiveRejectionPipelineState is NULL"
- "_maskUndistortPipelineState is NULL"
- "allocatorBackend is  nil"
- "allocatorDesc is NULL"
- "cmismartstyleovercapturethumbnailgenerator_trace"
- "cmismartstyleprocessor_trace"
- "cmismartstyleprocessorutilities_trace"
- "commandBuffer is NULL"
- "commandBufferToUse is NULL"
- "computeEncoder is NULL"
- "err"
- "input SRL pixel buffer is NULL"
- "inputLinearPixelBuffer is NULL"
- "kFigBaseObjectError_ParamErr"
- "refinedMaskTexture.height == originalMaskTexture.height is NULL"
- "refinedMaskTexture.width == originalMaskTexture.width is NULL"

```
