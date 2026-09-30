## MattingV2

> `/System/Library/VideoProcessors/MattingV2.bundle/MattingV2`

```diff

-664.40.15.122.3
-  __TEXT.__text: 0x11628
-  __TEXT.__auth_stubs: 0x4f0
+664.40.18.0.0
+  __TEXT.__text: 0xecac
+  __TEXT.__auth_stubs: 0x4c0
   __TEXT.__objc_methlist: 0xc04
-  __TEXT.__cstring: 0x2d4c
-  __TEXT.__const: 0xdf8
-  __TEXT.__oslogstring: 0x104a
+  __TEXT.__cstring: 0x284d
+  __TEXT.__const: 0xdc8
+  __TEXT.__oslogstring: 0xca
   __TEXT.__unwind_info: 0x2c0
   __TEXT.__objc_classname: 0xe3
   __TEXT.__objc_methname: 0x306c
   __TEXT.__objc_methtype: 0x955
-  __TEXT.__objc_stubs: 0x16a0
+  __TEXT.__objc_stubs: 0x1680
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x60
   __DATA_CONST.__objc_classlist: 0x48

   __DATA_CONST.__objc_selrefs: 0x998
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x700
   __AUTH_CONST.__objc_const: 0x1758

   __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0xc0
   __DATA.__bss: 0x20
-  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D90C14C0-8C76-349D-B667-5BC77F4E3A37
-  Functions: 364
-  Symbols:   114
-  CStrings:  984
+  UUID: A93B73DB-4EFB-368C-BA93-2BADB52BB034
+  Functions: 362
+  Symbols:   111
+  CStrings:  920
 
Symbols:
+ _FigSignalErrorAtGM
+ _objc_retain_x5
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _objc_retain_x26
CStrings:
+ "%s signalled err=%d at <>:%d"
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "( -73465 )"
- "-[FigMatting _allocateResources]"
- "-[FigMatting _prewarmMPSKernels]"
- "-[FigMatting encodeAddTexturesToCommandBuffer:sourceTextureA:sourceTextureB:destinationTexture:thresholdBeginValue:thresholdEndValue:]"
- "-[FigMatting encodeComposeRGBAGuideToCommandBuffer:rgbTexture:alphaTexture:destinationTexture:rgbWeight:]"
- "-[FigMatting encodePreprocessSkinToCommandBuffer:inputSkinTexture:faceNonSkinTextures:outputSkinTexture:]"
- "-[FigMatting initWithCommandQueue:]"
- "-[FigMatting process]"
- "-[FigMatting setOptions:]"
- "-[FocalPlaneV2 encodeDisparityRefinementPreprocessingOn:alphaTexture:inputDisparityTexture:outputDisparityTexture:configuration:]"
- "-[FocalPlaneV2 encodeFocalPlaneCalcOn:disparityTexture:]"
- "-[FocalPlaneV2 encodeMinMaxOn:inputTexture:]"
- "-[MattingV2TuningParameters getSemanticConfigurationsFor:mattingConfiguration:]"
- "-[MattingV2TuningParameters initWithTuningDictionary:]"
- "-[MattingV2TuningParameters parseSemanticConfiguration:semanticKey:mattingConfiguration:]"
- "-[Texture2DWrapper initWithTexture:textureArray:]"
- "<<<< MattingV2 >>>> %s: Allocating %lux%lu constraints texture for %@"
- "<<<< MattingV2 >>>> %s: Allocating disparity refinement guide (%lux%lu)"
- "<<<< MattingV2 >>>> %s: Allocating resources. Enabled outputs: %@"
- "<<<< MattingV2 >>>> %s: Allocation of resources succeeded. Size of allocated intermediates: %lu KB"
- "<<<< MattingV2 >>>> %s: Breach of integration contract. Disparity refinement configurationVersion was 0, but FigMattingOutputRefinedDisparity was enabled. Performing disparity refinement anyway."
- "<<<< MattingV2 >>>> %s: Depth filter is enabled. Composing RGBD guide"
- "<<<< MattingV2 >>>> %s: Disparity refinement enabled using version: %d."
- "<<<< MattingV2 >>>> %s: Enabled outputs: %@"
- "<<<< MattingV2 >>>> %s: Encoding _addTexturesKernel (%lux%lu) + (%lux%lu) -> (%lux%lu)"
- "<<<< MattingV2 >>>> %s: Encoding _composeRGBAGuideKernel rgb (%lux%lu), a (%lux%lu) -> rgba (%lux%lu)"
- "<<<< MattingV2 >>>> %s: Encoding constraints computation for: %@"
- "<<<< MattingV2 >>>> %s: Encoding disparity preprocessing"
- "<<<< MattingV2 >>>> %s: Encoding disparity refinement (version: %d)"
- "<<<< MattingV2 >>>> %s: Encoding disparity refinement guide (%lux%lu)"
- "<<<< MattingV2 >>>> %s: Encoding exclusion of non-skin for faceObservation: %@"
- "<<<< MattingV2 >>>> %s: Encoding matting for collection: %@"
- "<<<< MattingV2 >>>> %s: Encoding skin preprocessing"
- "<<<< MattingV2 >>>> %s: Face observation had no faceSegments property. Maybe inference failed? Skipping this face!"
- "<<<< MattingV2 >>>> %s: Face segment observations provided: %lu"
- "<<<< MattingV2 >>>> %s: Failed to add semantic output %d to output collection. Output will not be computed."
- "<<<< MattingV2 >>>> %s: Failed to create non-skin pixelBuffer for faceSegmentObservation (error: %@)"
- "<<<< MattingV2 >>>> %s: Failed to find key %@ in tuning parameters dictionary. Available keys: %@. Trying to continue parsing with the first key: %@ "
- "<<<< MattingV2 >>>> %s: Failed to perform disparity refinement. _refinedDisparityFilter or _preprocessedDisparity was nil"
- "<<<< MattingV2 >>>> %s: Failed to preallocate faceNonSkinTexture intermediate. Texture will be allocated on the fly."
- "<<<< MattingV2 >>>> %s: Incomplete or missing plist. Going with defaults."
- "<<<< MattingV2 >>>> %s: Matting tuning dictionary is not the same for %@ and %@. This is not supported. Will always use tuning parameters for: %@"
- "<<<< MattingV2 >>>> %s: Parsed unexpected tuning structure. The key %@ was not found in any of the specified dictionaries: %@. Defaulting to the value: %@"
- "<<<< MattingV2 >>>> %s: Parsing semantic tuning parameters for outputKey: %@ "
- "<<<< MattingV2 >>>> %s: Performance note: Creating MTLTextureType2DArray texture view."
- "<<<< MattingV2 >>>> %s: Performance problem: Failed to bind MTLTexture to faceSegmentProbabilityPixelBuffer. Allocating intermediate texture and copying data on the CPU."
- "<<<< MattingV2 >>>> %s: Performance problem: No matching preallocated faceNonSkinTexture available. New texture will be allocated."
- "<<<< MattingV2 >>>> %s: Provided configurationVersion is negative. Defaulting to configuration 0."
- "<<<< MattingV2 >>>> %s: Provided configurationVersion is unsupported. Defaulting to configuration 0."
- "<<<< MattingV2 >>>> %s: Tuning parameters from plist received"
- "<<<< MattingV2 >>>> %s: Unexpected FigMattingTuningConfiguration. Defaulting to FigMattingTuningConfigurationFine"
- "<<<< MattingV2 >>>> %s: Unexpected semantic output identifier: %u; no output configuration will be returned"
- "<<<< MattingV2 >>>> %s: Unsupported resolution mode %u. Falling back to %ux%u"
- "<<<< MattingV2 >>>> %s: Using provided metal command queue %p"
- "<<<< MattingV2 >>>> %s: Using syntheticFocusRectangle: (%.2f, %.2f), %.2f x %.2f"
- "<<<< MattingV2 >>>> %s: WARNING: Failed to parse disparity refinement version from SDOFRenderingParameters. Falling back to disparity refinement version 0; options dictionary had following keys: %@"
- "<<<< MattingV2 >>>> %s: syntheticFocusRectangle was not set -- falling back to default value: (%.2f, %.2f), %.2f x %.2f"
- "_readKeyWithDefault"
- "commandBuffer is NULL"
- "encoder is NULL"
- "inputDisparity has incorrect pixel format"
- "inputDisparityTexture.height != outputDisparityTexture.height"
- "inputDisparityTexture.width != outputDisparityTexture.width"
- "kCMBaseObjectError_ParamErr"

```
