## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`

```diff

-650.0.0.122.4
-  __TEXT.__text: 0x1e5e5c
-  __TEXT.__auth_stubs: 0x15f0
-  __TEXT.__objc_methlist: 0xc714
-  __TEXT.__const: 0x2e80
-  __TEXT.__cstring: 0x27305
-  __TEXT.__oslogstring: 0x15f6e
-  __TEXT.__gcc_except_tab: 0x125c
-  __TEXT.__unwind_info: 0x2d08
+655.0.0.122.4
+  __TEXT.__text: 0x1e2a6c
+  __TEXT.__auth_stubs: 0x15e0
+  __TEXT.__objc_methlist: 0xc724
+  __TEXT.__const: 0x2e40
+  __TEXT.__cstring: 0x26c61
+  __TEXT.__oslogstring: 0x15791
+  __TEXT.__gcc_except_tab: 0x1264
+  __TEXT.__unwind_info: 0x2cc0
   __TEXT.__eh_frame: 0xc18
-  __TEXT.__objc_classname: 0x158e
-  __TEXT.__objc_methname: 0x21b9f
-  __TEXT.__objc_methtype: 0x9318
-  __TEXT.__objc_stubs: 0xc0c0
+  __TEXT.__objc_classname: 0x1572
+  __TEXT.__objc_methname: 0x218cf
+  __TEXT.__objc_methtype: 0x9175
+  __TEXT.__objc_stubs: 0xbe80
   __DATA_CONST.__got: 0xa98
   __DATA_CONST.__const: 0x750
-  __DATA_CONST.__objc_classlist: 0x590
+  __DATA_CONST.__objc_classlist: 0x588
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5d90
+  __DATA_CONST.__objc_selrefs: 0x5d08
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x478
+  __DATA_CONST.__objc_superrefs: 0x470
   __DATA_CONST.__objc_arraydata: 0x370
-  __AUTH_CONST.__auth_got: 0xb10
+  __AUTH_CONST.__auth_got: 0xb08
   __AUTH_CONST.__const: 0x6f0
-  __AUTH_CONST.__cfstring: 0x68c0
-  __AUTH_CONST.__objc_const: 0x1d640
-  __AUTH_CONST.__objc_intobj: 0xa20
+  __AUTH_CONST.__cfstring: 0x6800
+  __AUTH_CONST.__objc_const: 0x1d650
+  __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_doubleobj: 0x10f0
-  __AUTH.__objc_data: 0xb40
+  __AUTH_CONST.__objc_doubleobj: 0x1100
+  __AUTH.__objc_data: 0xaf0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x1680
+  __DATA.__objc_ivar: 0x167c
   __DATA.__data: 0x11ac0
-  __DATA.__common: 0x240
+  __DATA.__common: 0x220
   __DATA.__bss: 0xe0
   __DATA_DIRTY.__objc_data: 0x2c60
   __DATA_DIRTY.__data: 0x9

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3C67289C-12A0-3D86-A7AF-FDDB0EB8EB24
-  Functions: 6753
-  Symbols:   19753
-  CStrings:  12071
+  UUID: EA5A00A0-3E19-3CBA-987F-A1FA2B32C0E1
+  Functions: 6707
+  Symbols:   19605
+  CStrings:  11975
 
Symbols:
+ -[CMISmartStyleMetalRendererV1 _encodeImageReduction:inputTexture:inputROI:statsComputationROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:]
+ -[CMISmartStyleMetalRendererV1 _encodeImageReduction:inputTexture:inputROI:statsComputationROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:].cold.1
+ -[CMISmartStyleMetalRendererV1 setStatsComputationRect:]
+ -[CMISmartStyleMetalRendererV1 statsComputationRect]
+ -[CMISmartStylePixelBufferRendererV1 setStatsComputationRect:]
+ -[CMISmartStylePixelBufferRendererV1 statsComputationRect]
+ -[CMITiledInferenceProcessorTilePipelineStage networkInputPorts]
+ -[CMITiledInferenceProcessorTilePipelineStage networkOutputPorts]
+ -[FigMetalContext allowDebugShaders]
+ -[FigMetalContext isHarvestingShaders]
+ GCC_except_table81
+ GCC_except_table82
+ _OBJC_IVAR_$_CMISmartStyleMetalRendererV1._statsComputationRect
+ _OBJC_IVAR_$_CMISmartStylePixelBufferRendererV1._statsComputationRect
+ _OBJC_IVAR_$_FigMetalContext._disableDebugShaders
+ _OBJC_IVAR_$_FigMetalContext._isHarvesting
+ ___28-[CMMTLCommandBuffer commit]_block_invoke.1507
+ ___34-[CMIStyleEngineProcessor process]_block_invoke.703
+ ___97-[CMITiledInferenceProcessor runWithTileCount:withCompletionHandler:event:waitValue:signalValue:]_block_invoke.318
+ ___block_descriptor_56_e8_32s40r48r_e28_v16?0"<MTLCommandBuffer>"8lr40l8r48l8s32l8
+ ___block_literal_global.1509
+ _computeCroppedGridSize.cold.3
+ _computeCroppedGridSize.cold.4
+ _objc_msgSend$_encodeImageReduction:inputTexture:inputROI:statsComputationROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:
+ _objc_msgSend$getInputs
+ _objc_msgSend$getOutputs
+ _objc_msgSend$setStatsComputationRect:
- -[CMISmartStyleDebugOverlay .cxx_destruct]
- -[CMISmartStyleDebugOverlay _cachedTexturesFromPixelBuffer:usage:]
- -[CMISmartStyleDebugOverlay _cachedTexturesFromPixelBuffer:usage:].cold.1
- -[CMISmartStyleDebugOverlay _cachedTexturesFromPixelBuffer:usage:].cold.2
- -[CMISmartStyleDebugOverlay _cachedTexturesFromPixelBuffer:usage:].cold.3
- -[CMISmartStyleDebugOverlay _compileShaders]
- -[CMISmartStyleDebugOverlay _compileShaders].cold.1
- -[CMISmartStyleDebugOverlay _compileShaders].cold.10
- -[CMISmartStyleDebugOverlay _compileShaders].cold.11
- -[CMISmartStyleDebugOverlay _compileShaders].cold.12
- -[CMISmartStyleDebugOverlay _compileShaders].cold.13
- -[CMISmartStyleDebugOverlay _compileShaders].cold.14
- -[CMISmartStyleDebugOverlay _compileShaders].cold.2
- -[CMISmartStyleDebugOverlay _compileShaders].cold.3
- -[CMISmartStyleDebugOverlay _compileShaders].cold.4
- -[CMISmartStyleDebugOverlay _compileShaders].cold.5
- -[CMISmartStyleDebugOverlay _compileShaders].cold.6
- -[CMISmartStyleDebugOverlay _compileShaders].cold.7
- -[CMISmartStyleDebugOverlay _compileShaders].cold.8
- -[CMISmartStyleDebugOverlay _compileShaders].cold.9
- -[CMISmartStyleDebugOverlay _metalPixelFormatForPixelbuffer:]
- -[CMISmartStyleDebugOverlay _setVertexBufferForPosition:primaryCaptureRect:scale:isVideo:]
- -[CMISmartStyleDebugOverlay copyPixelBuffer:toPixelBuffer:commandBuffer:]
- -[CMISmartStyleDebugOverlay copyPixelBuffer:toPixelBuffer:commandBuffer:].cold.1
- -[CMISmartStyleDebugOverlay copyPixelBuffer:toPixelBuffer:commandBuffer:].cold.2
- -[CMISmartStyleDebugOverlay copyPixelBuffer:toPixelBuffer:commandBuffer:].cold.3
- -[CMISmartStyleDebugOverlay copyPixelBuffer:toPixelBuffer:commandBuffer:].cold.4
- -[CMISmartStyleDebugOverlay copyPixelBuffer:toPixelBuffer:commandBuffer:].cold.5
- -[CMISmartStyleDebugOverlay copyPixelBuffer:toPixelBuffer:commandBuffer:].cold.6
- -[CMISmartStyleDebugOverlay dealloc]
- -[CMISmartStyleDebugOverlay initWithOptionalCommandQueue:]
- -[CMISmartStyleDebugOverlay initWithOptionalCommandQueue:].cold.1
- -[CMISmartStyleDebugOverlay initWithOptionalCommandQueue:].cold.2
- -[CMISmartStyleDebugOverlay initWithOptionalCommandQueue:].cold.3
- -[CMISmartStyleDebugOverlay initWithOptionalCommandQueue:].cold.4
- -[CMISmartStyleDebugOverlay overlayIntegratedCoefficientsTexture:onPixelBuffer:position:scale:index:rotationToApply:primaryCaptureRect:commandBuffer:]
- -[CMISmartStyleDebugOverlay overlayIntegratedCoefficientsTexture:onPixelBuffer:position:scale:index:rotationToApply:primaryCaptureRect:commandBuffer:].cold.1
- -[CMISmartStyleDebugOverlay overlayIntegratedCoefficientsTexture:onPixelBuffer:position:scale:index:rotationToApply:primaryCaptureRect:commandBuffer:].cold.2
- -[CMISmartStyleDebugOverlay overlayMask:onPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransform:]
- -[CMISmartStyleDebugOverlay overlayMask:onPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransform:].cold.1
- -[CMISmartStyleDebugOverlay overlayMask:onPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransform:].cold.2
- -[CMISmartStyleDebugOverlay overlayMask:onPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransform:].cold.3
- -[CMISmartStyleDebugOverlay overlayPixelBuffer:onPixelBuffer:position:scale:rotationToApply:primaryCaptureRect:commandBuffer:]
- -[CMISmartStyleDebugOverlay overlayPixelBuffer:onPixelBuffer:position:scale:rotationToApply:primaryCaptureRect:commandBuffer:].cold.1
- -[CMISmartStyleDebugOverlay overlayPixelBuffer:onPixelBuffer:position:scale:rotationToApply:primaryCaptureRect:commandBuffer:].cold.2
- -[CMISmartStyleDebugOverlay overlayPixelBuffer:onPixelBuffer:position:scale:rotationToApply:primaryCaptureRect:commandBuffer:].cold.3
- -[CMISmartStyleDebugOverlay overlayPixelBuffer:onPixelBuffer:position:scale:rotationToApply:primaryCaptureRect:commandBuffer:].cold.4
- -[CMISmartStyleDebugOverlay overlayPixelBuffer:onPixelBuffer:position:scale:rotationToApply:primaryCaptureRect:commandBuffer:].cold.5
- -[CMISmartStyleMetalRendererV1 _encodeImageReduction:inputTexture:inputROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:]
- -[CMISmartStyleMetalRendererV1 _encodeImageReduction:inputTexture:inputROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:].cold.1
- GCC_except_table77
- GCC_except_table80
- _CFGetRetainCount
- _CMI_SMART_STYLE_DEBUG_OVERLAY_NOTE_VARIABLE
- _OBJC_CLASS_$_CMISmartStyleDebugOverlay
- _OBJC_IVAR_$_CMISmartStyleDebugOverlay._copyKernel
- _OBJC_IVAR_$_CMISmartStyleDebugOverlay._cvMetalTextureCacheRef
- _OBJC_IVAR_$_CMISmartStyleDebugOverlay._metalContext
- _OBJC_IVAR_$_CMISmartStyleDebugOverlay._overlayMaskPipelineState
- _OBJC_IVAR_$_CMISmartStyleDebugOverlay._renderPipelinesStates
- _OBJC_METACLASS_$_CMISmartStyleDebugOverlay
- __OBJC_$_INSTANCE_METHODS_CMISmartStyleDebugOverlay
- __OBJC_$_INSTANCE_VARIABLES_CMISmartStyleDebugOverlay
- __OBJC_CLASS_RO_$_CMISmartStyleDebugOverlay
- __OBJC_METACLASS_RO_$_CMISmartStyleDebugOverlay
- ___28-[CMMTLCommandBuffer commit]_block_invoke.1505
- ___34-[CMIStyleEngineProcessor process]_block_invoke.701
- ___97-[CMITiledInferenceProcessor runWithTileCount:withCompletionHandler:event:waitValue:signalValue:]_block_invoke.314
- ___block_descriptor_48_e8_32r40r_e29_v24?0"<MTLSharedEvent>"8Q16lr32l8r40l8
- ___block_literal_global.1507
- _computeCenterCropOffset.cold.2
- _getSensorDimensionsInBayerPixels
- _getSensorDimensionsInBayerPixels.cold.1
- _getSensorDimensionsInBayerPixels.cold.2
- _objc_msgSend$_cachedTexturesFromPixelBuffer:usage:
- _objc_msgSend$_encodeImageReduction:inputTexture:inputROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:
- _objc_msgSend$_metalPixelFormatForPixelbuffer:
- _objc_msgSend$_setVertexBufferForPosition:primaryCaptureRect:scale:isVideo:
- _objc_msgSend$drawPrimitives:vertexStart:vertexCount:
- _objc_msgSend$fragmentFunction
- _objc_msgSend$newRenderPipelineStateWithDescriptor:error:
- _objc_msgSend$setAlphaBlendOperation:
- _objc_msgSend$setBlendingEnabled:
- _objc_msgSend$setDestinationAlphaBlendFactor:
- _objc_msgSend$setDestinationRGBBlendFactor:
- _objc_msgSend$setFragmentBytes:length:atIndex:
- _objc_msgSend$setFragmentTexture:atIndex:
- _objc_msgSend$setLoadAction:
- _objc_msgSend$setRenderPipelineState:
- _objc_msgSend$setRgbBlendOperation:
- _objc_msgSend$setSourceAlphaBlendFactor:
- _objc_msgSend$setSourceRGBBlendFactor:
- _objc_msgSend$setStoreAction:
- _objc_msgSend$setVertexBuffer:offset:atIndex:
- _objc_msgSend$setWithArray:
- _objc_msgSend$vertexFunction
CStrings:
+ "-[CMISmartStyleMetalRendererV1 _encodeImageReduction:inputTexture:inputROI:statsComputationROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:]"
+ "<IOSurface %p> %lux%lu%@, '%@'%@%@"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_statsComputationRect"
+ "_disableDebugShaders"
+ "_encodeImageReduction:inputTexture:inputROI:statsComputationROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:"
+ "_isHarvesting"
+ "_statsComputationRect"
+ "allowDebugShaders"
+ "err = FigSignalErrorAt3(\"%s%s%s signalled err=%d (%s) (%s) at %s:%d\", gStyleEngineProcessorTrace.note.emitter, (CMIStyleEngineStatusResourcesNotReleased), \"CMIStyleEngineStatusResourcesNotReleased\", (\"FigMetalAllocator resources not correctly released\"), \"<<<< StyleEngineProcessor >>>>\", __FUNCTION__, \"CMIStyleEngineProcessor.m\", 3464, __builtin_return_address(0), 0) == 0 "
+ "i188@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGRect={CGPoint=dd}{CGSize=dd}}64{?=i{?=[3]}B}96@176I184"
+ "isHarvestingShaders"
+ "networkInputPorts"
+ "networkOutputPorts"
+ "setStatsComputationRect:"
+ "statsComputationRect"
+ "supportsAtomicFloat"
- "\n"
- " Please file a radar against 'CameraCapture Stills | all'."
- "-[CMISmartStyleDebugOverlay _cachedTexturesFromPixelBuffer:usage:]"
- "-[CMISmartStyleDebugOverlay _compileShaders]"
- "-[CMISmartStyleDebugOverlay _metalPixelFormatForPixelbuffer:]"
- "-[CMISmartStyleDebugOverlay copyPixelBuffer:toPixelBuffer:commandBuffer:]"
- "-[CMISmartStyleDebugOverlay initWithOptionalCommandQueue:]"
- "-[CMISmartStyleDebugOverlay overlayIntegratedCoefficientsTexture:onPixelBuffer:position:scale:index:rotationToApply:primaryCaptureRect:commandBuffer:]"
- "-[CMISmartStyleDebugOverlay overlayMask:onPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransform:]"
- "-[CMISmartStyleDebugOverlay overlayPixelBuffer:onPixelBuffer:position:scale:rotationToApply:primaryCaptureRect:commandBuffer:]"
- "-[CMISmartStyleMetalRendererV1 _encodeImageReduction:inputTexture:inputROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:]"
- "-[FigMetalHeapAllocator _releaseHeapEnforcingImmediateDealloc:]"
- "<<<< CMISmartStyleDebugOverlay >>>>"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: MetalContext is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: Pixel buffer %c%c%c%c format not supported"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: Shaders compilation failed."
- "<<<< CMISmartStyleDebugOverlay >>>> %s: Unable to cache pixel buffer texture"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: Unable to create a metal texture cache"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: Unable to get metal texture address"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: Unable to init CMISmartStyleDebugOverlay."
- "<<<< CMISmartStyleDebugOverlay >>>> %s: Unable to load the bundle for CMISmartStyleDebugOverlay."
- "<<<< CMISmartStyleDebugOverlay >>>> %s: _copyKernel is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: _renderPipelinesStates[COEFFICIENTS_OVERLAY_HDR] is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: _renderPipelinesStates[COEFFICIENTS_OVERLAY_HDR_PACKED] is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: _renderPipelinesStates[COEFFICIENTS_OVERLAY_SDR] is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: _renderPipelinesStates[OVERLAY_HDR] is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: _renderPipelinesStates[OVERLAY_HDR_PACKED] is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: _renderPipelinesStates[OVERLAY_RGB] is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: _renderPipelinesStates[OVERLAY_SDR] is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: fullRangeVertexDesc is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: inputOutputTexture is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: maskTexture is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: pipelineDescriptor is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: pipelineDescriptor.fragmentFunction is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: pipelineDescriptor.vertexFunction is nil"
- "<<<< CMISmartStyleDebugOverlay >>>> %s: pixelBuffer is NULL"
- "<<<< CMISmartStyleDebugOverlay >>>> Fig"
- "<<<< FigMetalAllocator >>>> %s: Releasing Metal heap -- retainCount:%lu, %@"
- "<<<< FigMetalAllocator >>>> %s: Retain count for Metal heap is higher than expected (%{public}lu).%{private}s label:%{public}@, %{private}@"
- "<IOSurface %p> %lux%lu%@, '%@' ID:%u"
- "@32@0:8^{__CVBuffer=}16Q24"
- "@64@0:816{CGRect={CGPoint=dd}{CGSize=dd}}24f56B60"
- "CMISmartStyleDebugOverlay"
- "CMISmartStyleDebugOverlay.m"
- "Could not bind destination pixel buffer"
- "Could not bind image pixel buffer"
- "Could not bind input pixel buffer"
- "Could not bind pixel buffer"
- "Could not bind source pixel buffer"
- "FragmentOverlay"
- "FragmentOverlayIntegratedCoefficients"
- "Q24@0:8^{__CVBuffer=}16"
- "Unable to create metal command encoder"
- "Unsupported pixel buffer format for input"
- "Unsupported pixel buffer format for output"
- "VertexPassthrough"
- "[7@\"<MTLRenderPipelineState>\"]"
- "_cachedTexturesFromPixelBuffer:usage:"
- "_copyKernel"
- "_cvMetalTextureCacheRef"
- "_encodeImageReduction:inputTexture:inputROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:"
- "_metalPixelFormatForPixelbuffer:"
- "_overlayMaskPipelineState"
- "_overlayMaskPipelineState is NULL"
- "_renderPipelinesStates"
- "_setVertexBufferForPosition:primaryCaptureRect:scale:isVideo:"
- "cmismartstyledebugoverlay_trace"
- "commandBufferToUse"
- "commandBufferToUse is NULL"
- "copyPixelBuffer:toPixelBuffer:commandBuffer:"
- "copyTexture"
- "destinationMetalFormat != MTLPixelFormatInvalid"
- "destinationTexture"
- "drawPrimitives:vertexStart:vertexCount:"
- "err = FigSignalErrorAt3(\"%s%s%s signalled err=%d (%s) (%s) at %s:%d\", gStyleEngineProcessorTrace.note.emitter, (CMIStyleEngineStatusResourcesNotReleased), \"CMIStyleEngineStatusResourcesNotReleased\", (\"FigMetalAllocator resources not correctly released\"), \"<<<< StyleEngineProcessor >>>>\", __FUNCTION__, \"CMIStyleEngineProcessor.m\", 3442, __builtin_return_address(0), 0) == 0 "
- "fragmentFunction"
- "i144@0:8^{__CVBuffer=}16^{__CVBuffer=}24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGRect={CGPoint=dd}{CGSize=dd}}64{?=[3]}96"
- "i156@0:8@16@24{CGRect={CGPoint=dd}{CGSize=dd}}32{?=i{?=[3]}B}64@144I152"
- "i40@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32"
- "i88@0:8^{__CVBuffer=}16^{__CVBuffer=}2432f40i44{CGRect={CGPoint=dd}{CGSize=dd}}48@80"
- "i92@0:8@16^{__CVBuffer=}2432f40i44i48{CGRect={CGPoint=dd}{CGSize=dd}}52@84"
- "imageTexture"
- "outputSensorDimensionsInBayerPixels != ((void *)0)"
- "outputSensorDimensionsInBayerPixels is NULL"
- "overlayIntegratedCoefficientsTexture:onPixelBuffer:position:scale:index:rotationToApply:primaryCaptureRect:commandBuffer:"
- "overlayMask:onPixelBuffer:primaryCaptureRect:inputCropRectWithinPrimaryCaptureRect:affineTransform:"
- "overlayPixelBuffer:onPixelBuffer:position:scale:rotationToApply:primaryCaptureRect:commandBuffer:"
- "setAlphaBlendOperation:"
- "setBlendingEnabled:"
- "setDestinationAlphaBlendFactor:"
- "setDestinationRGBBlendFactor:"
- "setFragmentBytes:length:atIndex:"
- "setFragmentTexture:atIndex:"
- "setLoadAction:"
- "setRenderPipelineState:"
- "setRgbBlendOperation:"
- "setSourceAlphaBlendFactor:"
- "setSourceRGBBlendFactor:"
- "setStoreAction:"
- "setVertexBuffer:offset:atIndex:"
- "setWithArray:"
- "smartStyleOverlayPersonMask"
- "sourceMetalFormat != MTLPixelFormatInvalid"
- "sourceTexture"
- "vertexFunction"

```
