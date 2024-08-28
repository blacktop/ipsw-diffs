## MattingV2

> `/System/Library/VideoProcessors/MattingV2.bundle/MattingV2`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0xda44
-  __TEXT.__auth_stubs: 0x480
+580.2.0.0.0
+  __TEXT.__text: 0x105d8
+  __TEXT.__auth_stubs: 0x4b0
   __TEXT.__objc_methlist: 0xa58
-  __TEXT.__cstring: 0x289b
-  __TEXT.__const: 0xda8
+  __TEXT.__cstring: 0x2dca
+  __TEXT.__const: 0xde0
+  __TEXT.__oslogstring: 0xf80
   __TEXT.__unwind_info: 0x260
   __TEXT.__objc_classname: 0xe3
   __TEXT.__objc_methname: 0x306c
   __TEXT.__objc_methtype: 0x955
-  __TEXT.__objc_stubs: 0x1680
+  __TEXT.__objc_stubs: 0x16a0
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x48

   __DATA_CONST.__objc_selrefs: 0x900
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x780
   __AUTH_CONST.__objc_const: 0x1a78

   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0xc0
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 233
-  Symbols:   108
-  CStrings:  860
+  Symbols:   111
+  CStrings:  927
 
Symbols:
+ _objc_retain_x26
+ _os_log_type_enabled
+ _FigSignalErrorAt3
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ __os_log_send_and_compose_impl
- _objc_retain_x24
- _objc_retain_x5
- _FigSignalErrorAt
CStrings:
+ "<<<< MattingV2 >>>> %!s(MISSING): Enabled outputs: %!@(MISSING)"
+ "kFigBaseObjectError_ParamErr"
+ "<<<< MattingV2 >>>> %!s(MISSING): Failed to create non-skin pixelBuffer for faceSegmentObservation (error: %!@(MISSING))"
+ "<<<< MattingV2 >>>> %!s(MISSING): WARNING: Failed to parse disparity refinement version from SDOFRenderingParameters. Falling back to disparity refinement version 0; options dictionary had following keys: %!@(MISSING)"
+ "<<<< MattingV2 >>>> %!s(MISSING): Encoding disparity refinement (version: %!d(MISSING))"
+ "-1"
+ "-[FocalPlaneV2 encodeFocalPlaneCalcOn:disparityTexture:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Failed to find key %!@(MISSING) in tuning parameters dictionary. Available keys: %!@(MISSING). Trying to continue parsing with the first key: %!@(MISSING) "
+ "<<<< MattingV2 >>>> %!s(MISSING): Failed to preallocate faceNonSkinTexture intermediate. Texture will be allocated on the fly."
+ "<<<< MattingV2 >>>> %!s(MISSING): Tuning parameters from plist received"
+ "<<<< MattingV2 >>>> %!s(MISSING): Encoding _addTexturesKernel (%!l(MISSING)ux%!l(MISSING)u) + (%!l(MISSING)ux%!l(MISSING)u) -> (%!l(MISSING)ux%!l(MISSING)u)"
+ "<<<< MattingV2 >>>> %!s(MISSING): Performance problem: Failed to bind MTLTexture to faceSegmentProbabilityPixelBuffer. Allocating intermediate texture and copying data on the CPU."
+ "<<<< MattingV2 >>>> %!s(MISSING): Disparity refinement enabled using version: %!d(MISSING)."
+ "<<<< MattingV2 >>>> %!s(MISSING): Allocating %!l(MISSING)ux%!l(MISSING)u constraints texture for %!@(MISSING)"
+ "-[FigMatting _allocateResources]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Encoding disparity refinement guide (%!l(MISSING)ux%!l(MISSING)u)"
+ "_readKeyWithDefault"
+ "<<<< MattingV2 >>>> %!s(MISSING): Using provided metal command queue %!p(MISSING)"
+ "-[MattingV2TuningParameters parseSemanticConfiguration:semanticKey:mattingConfiguration:]"
+ "-[FigMatting encodeAddTexturesToCommandBuffer:sourceTextureA:sourceTextureB:destinationTexture:thresholdBeginValue:thresholdEndValue:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Failed to perform disparity refinement. _refinedDisparityFilter or _preprocessedDisparity was nil"
+ "<<<< MattingV2 >>>> %!s(MISSING): Using syntheticFocusRectangle: (%!f(MISSING), %!f(MISSING)), %!f(MISSING) x %!f(MISSING)"
+ "inputDisparityTexture.height != outputDisparityTexture.height"
+ "<<<< MattingV2 >>>> %!s(MISSING): Encoding skin preprocessing"
+ "-[MattingV2TuningParameters initWithTuningDictionary:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Depth filter is enabled. Composing RGBD guide"
+ "<<<< MattingV2 >>>> %!s(MISSING): Allocation of resources succeeded. Size of allocated intermediates: %!l(MISSING)u KB"
+ "<<<< MattingV2 >>>> %!s(MISSING): Provided configurationVersion is unsupported. Defaulting to configuration 0."
+ "commandBuffer is NULL"
+ "<<<< MattingV2 >>>> %!s(MISSING): Allocating disparity refinement guide (%!l(MISSING)ux%!l(MISSING)u)"
+ "inputDisparityTexture.width != outputDisparityTexture.width"
+ "-[FigMatting encodeComposeRGBAGuideToCommandBuffer:rgbTexture:alphaTexture:destinationTexture:rgbWeight:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Provided configurationVersion is negative. Defaulting to configuration 0."
+ "<<<< MattingV2 >>>> %!s(MISSING): Performance note: Creating MTLTextureType2DArray texture view."
+ "-[Texture2DWrapper initWithTexture:textureArray:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Unexpected semantic output identifier: %!u(MISSING); no output configuration will be returned"
+ "<<<< MattingV2 >>>> %!s(MISSING): Unexpected FigMattingTuningConfiguration. Defaulting to FigMattingTuningConfigurationFine"
+ "-[FigMatting setOptions:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Matting tuning dictionary is not the same for %!@(MISSING) and %!@(MISSING). This is not supported. Will always use tuning parameters for: %!@(MISSING)"
+ "(Fig)"
+ "<<<< MattingV2 >>>> %!s(MISSING): Performance problem: No matching preallocated faceNonSkinTexture available. New texture will be allocated."
+ "inputDisparity has incorrect pixel format"
+ "<<<< MattingV2 >>>> %!s(MISSING): Breach of integration contract. Disparity refinement configurationVersion was 0, but FigMattingOutputRefinedDisparity was enabled. Performing disparity refinement anyway."
+ "<<<< MattingV2 >>>> %!s(MISSING): Encoding constraints computation for: %!@(MISSING)"
+ "-[FocalPlaneV2 encodeDisparityRefinementPreprocessingOn:alphaTexture:inputDisparityTexture:outputDisparityTexture:configuration:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Face observation had no faceSegments property. Maybe inference failed? Skipping this face!"
+ "-[FigMatting process]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Encoding disparity preprocessing"
+ "<<<< MattingV2 >>>> %!s(MISSING): Face segment observations provided: %!l(MISSING)u"
+ "<<<< MattingV2 >>>> %!s(MISSING): Failed to add semantic output %!d(MISSING) to output collection. Output will not be computed."
+ "encoder is NULL"
+ "-[FigMatting encodePreprocessSkinToCommandBuffer:inputSkinTexture:faceNonSkinTextures:outputSkinTexture:]"
+ "-[FocalPlaneV2 encodeMinMaxOn:inputTexture:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Encoding _composeRGBAGuideKernel rgb (%!l(MISSING)ux%!l(MISSING)u), a (%!l(MISSING)ux%!l(MISSING)u) -> rgba (%!l(MISSING)ux%!l(MISSING)u)"
+ "-[MattingV2TuningParameters getSemanticConfigurationsFor:mattingConfiguration:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Unsupported resolution mode %!u(MISSING). Falling back to %!u(MISSING)x%!u(MISSING)"
+ "-[FigMatting initWithCommandQueue:]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Encoding exclusion of non-skin for faceObservation: %!@(MISSING)"
+ "<<<< MattingV2 >>>> %!s(MISSING): Parsing semantic tuning parameters for outputKey: %!@(MISSING) "
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "<<<< MattingV2 >>>> %!s(MISSING): Encoding matting for collection: %!@(MISSING)"
+ "<<<< MattingV2 >>>>"
+ "<<<< MattingV2 >>>> %!s(MISSING): syntheticFocusRectangle was not set -- falling back to default value: (%!f(MISSING), %!f(MISSING)), %!f(MISSING) x %!f(MISSING)"
+ "-[FigMatting _prewarmMPSKernels]"
+ "<<<< MattingV2 >>>> %!s(MISSING): Incomplete or missing plist. Going with defaults."
+ "<<<< MattingV2 >>>> %!s(MISSING): Allocating resources. Enabled outputs: %!@(MISSING)"
+ "<<<< MattingV2 >>>> %!s(MISSING): Parsed unexpected tuning structure. The key %!@(MISSING) was not found in any of the specified dictionaries: %!@(MISSING). Defaulting to the value: %!@(MISSING)"

```
