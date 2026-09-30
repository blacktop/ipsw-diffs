## GenIEV1

> `/System/Library/VideoProcessors/GenIEV1.bundle/GenIEV1`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-761.0.0.0.3
-  __TEXT.__text: 0x10d70
-  __TEXT.__auth_stubs: 0x3b0
+764.22.5.122.2
+  __TEXT.__text: 0xa634
+  __TEXT.__auth_stubs: 0x3a0
   __TEXT.__objc_stubs: 0x1560
   __TEXT.__objc_methlist: 0xc2c
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0xdbc
-  __TEXT.__cstring: 0x11d6
-  __TEXT.__oslogstring: 0x25fa
+  __TEXT.__gcc_except_tab: 0x980
+  __TEXT.__const: 0x90
+  __TEXT.__cstring: 0xc13
   __TEXT.__objc_classname: 0x20d
   __TEXT.__objc_methname: 0x1c5a
   __TEXT.__objc_methtype: 0x9c0
-  __TEXT.__unwind_info: 0x370
+  __TEXT.__oslogstring: 0x4ea
+  __TEXT.__unwind_info: 0x338
   __DATA_CONST.__const: 0x148
   __DATA_CONST.__cfstring: 0x660
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__auth_got: 0x1e8
+  __DATA_CONST.__auth_got: 0x1e0
   __DATA_CONST.__got: 0x78
   __DATA.__objc_const: 0x2330
   __DATA.__objc_selrefs: 0x730

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 257
-  Symbols:   754
-  CStrings:  765
+  Functions: 245
+  Symbols:   759
+  CStrings:  621
 
Symbols:
+ _FigSignalErrorAtGM
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _fig_log_get_emitter
- GCC_except_table19
- GCC_except_table7
- _FigSignalErrorAt3
- _NSStringFromClass
- _objc_retain_x23
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "( -73465 )"
- "-[GenIENetworkDecoder initWithShared:]"
- "-[GenIEPostProcessShadersV1 initWithContext:parameters:]"
- "-[GenIEPostProcessV1 _applyGaussianFilter:inputTex:outputTex:kernelSize:sigma:]"
- "-[GenIEPostProcessV1 _applyGaussianFilterTwoPass:kernel:inputTex:outputTex:kernelSize:weights:]"
- "-[GenIEPostProcessV1 _computeLumaGainCurveLUT]"
- "-[GenIEPostProcessV1 _copyEnhancedToOutputTexture]"
- "-[GenIEPostProcessV1 _modulateStrength]"
- "-[GenIEPostProcessV1 _removeLowFreqDiff]"
- "-[GenIEPostProcessV1 _textureAddBack]"
- "-[GenIEPostProcessV1 initWithMetalContext:parameters:]"
- "-[GenIEPostProcessV1 prewarm]"
- "-[GenIEPostProcessV1 runWithOriginalTex:enhancedTex:outputTex:]"
- "-[GenIEProcessorV1 _bindCVPixleBuffer:usage:useCSCForYCCConversion:useCSCForTransferFunction:]"
- "-[GenIEProcessorV1 copyWithInputTex:outputTex:]"
- "-[GenIEProcessorV1 prepareToProcess:]"
- "-[GenIEProcessorV1 prewarm]"
- "-[GenIEProcessorV1 process]"
- "-[GenIEProcessorV1 setMetalCommandQueue:]"
- "-[GenIEProcessorV1 setup]"
- "-[GenIEProcessorV1 zoomWithInputTex:outputTex:inputCropRect:outputCropRect:]"
- "-[GenIEShadersV1 initWithContext:]"
- "-[GenIETuningParametersV1 _getPostProcessingParameters:]"
- "-[GenIETuningParametersV1 initWithDictionary:]"
- "-[GenIETuningParametersV1 init]"
- "-[GenIeAEMPreStage processTilePipelineStage:]"
- "-[GenIeDecoderPreStage processTilePipelineStage:]"
- "-[GenIeDenoiserPreStage processTilePipelineStage:]"
- "-[GenIeEncoderPreStage processTilePipelineStage:]"
- "<<<< GenIEPostProcessV1 >>>> %s: Cannot operate in-place with single pass Gaussian filter (kernel size: %u)"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed in computing luma gain curve LUT"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed in remove low frequency diff"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed in texture add back"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture blendMask"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture blendMaskPreFilter"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture detailsGainMap"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture enhancedLowPass"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture enhancedLowPass2"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture enhancedSmoothedTex"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture for Gaussian filtering"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture lowPassIntermediate"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture lumaGainMap"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture lumaGainMapPreFilter"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture originalLowPass"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture originalLowPass2"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate intermediate texture originalSmoothedTex"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to allocate lumaGainCurveLUT"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to apply Gaussian smoothing for enhancedLowPass"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to apply Gaussian smoothing for enhancedLowPass2"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to apply Gaussian smoothing for originalLowPass"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to apply Gaussian smoothing for originalLowPass2"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to apply Gaussian smoothing to detailsGainMap"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to apply low pass filtering for enhanced"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to apply low pass filtering for original"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to apply smoothing for enhanced"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to apply smoothing for original"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to copy to output texture"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to get compiled GaussianFilter for kernel size: %u"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to load kernel %s"
- "<<<< GenIEPostProcessV1 >>>> %s: Failed to load shaders required by %@"
- "<<<< GenIEPostProcessV1 >>>> %s: Inconsistent size between enhancedTex and outputTex"
- "<<<< GenIEPostProcessV1 >>>> %s: Metal context is nil"
- "<<<< GenIEPostProcessV1 >>>> %s: Parameters is nil"
- "<<<< GenIEPostProcessV1 >>>> %s: Shaders or parameters not loaded, likely not prewarmed or prewarm failed"
- "<<<< GenIEPostProcessV1 >>>> %s: Single pass Gaussian cannot operate in-place"
- "<<<< GenIEProcessorV1 >>>> %s: Command queue already created, metalCommandQueue should be set before -setup"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to bind input pixel buffer as RGB texture"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to bind input pixel buffer as YCC texture"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to bind output pixel buffer as RGB texture"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to bind output pixel buffer as texture"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to bind pixel buffer %p to texture"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to create metal allocator for %@"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to create metal context for %@"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to create network stage"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to create post process stage"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to find metal pixel format with CSC YCC conversion support"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to load kernel GenIE::copy"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to load kernel GenIE::zoom"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to load shaders required by %@"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to load tuning parameters"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to prewarm post processing stage"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to run GenIE post processing"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to run network, bailing (%d)"
- "<<<< GenIEProcessorV1 >>>> %s: Failed to setup network, bailing (%d)"
- "<<<< GenIEProcessorV1 >>>> %s: Invalid processing type for GenIEProcessor"
- "<<<< GenIEProcessorV1 >>>> %s: Pixel buffer %c%c%c%c format not supported"
- "<<<< GenIEProcessorV1 >>>> %s: Running PostProcessing"
- "<<<< GenIEProcessorV1 >>>> %s: Unknown processing type %d"
- "<<<< GenIEProcessorV1 >>>> %s: _inputPixelBuffer is nil"
- "<<<< GenIEProcessorV1 >>>> %s: _outputPixelBuffer is nil"
- "<<<< GenIEProcessorV1 >>>> %s: cmdEncoder is nil"
- "<<<< GenIEProcessorV1 >>>> %s: exifOrientation = %d"
- "<<<< GenIEProcessorV1 >>>> %s: inputCropOrigin:  {%d, %d}"
- "<<<< GenIEProcessorV1 >>>> %s: inputCropSize:    {%d, %d}"
- "<<<< GenIEProcessorV1 >>>> %s: inputPixelBufferCropRect .origin:{%.0f,%.0f} .size:{%.0f,%.0f}"
- "<<<< GenIEProcessorV1 >>>> %s: outputCropOrigin: {%d, %d}"
- "<<<< GenIEProcessorV1 >>>> %s: outputCropRect .origin:{%.0f,%.0f} .size:{%.0f,%.0f}"
- "<<<< GenIEProcessorV1 >>>> %s: outputCropSize:   {%d, %d}"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get module parameters for LowPassFilter"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get module parameters for ModulateStrength"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get module parameters for RemoveLowFreqDiff"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get module parameters for TextureAddBack"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter blendMaskSmoothingKernelSize from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter blendMaskSmoothingSigma from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter censusTransformOffset from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter deltaDecreaseStart from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter deltaMax from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter detailsGainMapSmoothingKernelSize from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter detailsGainMapSmoothingSigma from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter kernelSize from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter lumaGainCurveLUT from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter lumaGainMapSmoothingKernelSize from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter lumaGainMapSmoothingSigma from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get parameter sigma from plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get post processing parameters from tuning"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get tuning parameter sharpenAmount from tuning plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to get tuning parameter sharpenSigma from tuning plist"
- "<<<< GenIETuningParametersV1 >>>> %s: Failed to load plist %@"
- "<<<< GenIETuningParametersV1 >>>> %s: Invalid lumaGainCurveLUT array, must contain even number of entries with a total count of less than %lu"
- "<<<< GenIETuningParametersV1 >>>> %s: PostProcessing section not found in tuning plist"
- "<<<< GenIEV1 >>>> %s: AEM failed, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: Cannot proceed without the aem, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: Cannot proceed without the encoder, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: Failed to load aem network %s, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: Failed to load decoder network %s, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: Failed to load denoiser network %s, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: Failed to load encoder network %s, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: _defaultCommonTileBorder: {%d,%d}"
- "<<<< GenIEV1 >>>> %s: _defaultLazyLoadModels:%d"
- "<<<< GenIEV1 >>>> %s: _defaultNormalizationFactor: %f"
- "<<<< GenIEV1 >>>> %s: _defaultUseDenoiser:%d"
- "<<<< GenIEV1 >>>> %s: decoder failed, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: decoderHasAdditionalInputs:%d"
- "<<<< GenIEV1 >>>> %s: denoiser failed, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: encoder failed, bailing (%d)"
- "<<<< GenIEV1 >>>> %s: feature.shape:[%d, %d]"
- "<<<< GenIEV1 >>>> %s: latent.shape:[%d, %d, %d]"
- "<<<< GenIEV1 >>>> %s: loadTIPWithConfig failed, %d."
- "<<<< GenIEV1 >>>> %s: loadWithConfig failed, %d."
- "<<<< GenIEV1 >>>> %s: tile(%u, %u)"
- "<<<< GenIEV1 >>>> %s: tileCount: (%d, %d)"
- "_context.commandBuffer is NULL"
- "cmdBuffer is NULL"
- "self is NULL"
```
