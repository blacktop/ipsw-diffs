## MattingV2

> `/System/Library/VideoProcessors/MattingV2.bundle/MattingV2`

```diff

-587.60.10.122.3
-  __TEXT.__text: 0x10788
-  __TEXT.__auth_stubs: 0x4b0
+587.60.14.122.2
+  __TEXT.__text: 0xdbf4
+  __TEXT.__auth_stubs: 0x480
   __TEXT.__objc_methlist: 0xa58
-  __TEXT.__cstring: 0x2df8
-  __TEXT.__const: 0xde8
-  __TEXT.__oslogstring: 0xf80
+  __TEXT.__cstring: 0x28ae
+  __TEXT.__const: 0xdb0
   __TEXT.__unwind_info: 0x260
   __TEXT.__objc_classname: 0xe3
   __TEXT.__objc_methname: 0x306c
   __TEXT.__objc_methtype: 0x955
-  __TEXT.__objc_stubs: 0x16a0
+  __TEXT.__objc_stubs: 0x1680
   __DATA_CONST.__got: 0xd8
   __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_classlist: 0x48

   __DATA_CONST.__objc_selrefs: 0x900
   __DATA_CONST.__objc_superrefs: 0x38
   __DATA_CONST.__objc_arraydata: 0x38
-  __AUTH_CONST.__auth_got: 0x260
+  __AUTH_CONST.__auth_got: 0x248
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x7e0
   __AUTH_CONST.__objc_const: 0x1a78

   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0xc0
-  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 233
-  Symbols:   111
-  CStrings:  930
+  Symbols:   108
+  CStrings:  863
 
Symbols:
+ _FigSignalErrorAt
+ _objc_retain_x24
+ _objc_retain_x5
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _objc_retain_x26
- _os_log_type_enabled
CStrings:
- "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
- "(Fig)"
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
- "<<<< MattingV2 >>>>"
- "<<<< MattingV2 >>>> %!s(MISSING): Allocating %!l(MISSING)ux%!l(MISSING)u constraints texture for %!@(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Allocating disparity refinement guide (%!l(MISSING)ux%!l(MISSING)u)"
- "<<<< MattingV2 >>>> %!s(MISSING): Allocating resources. Enabled outputs: %!@(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Allocation of resources succeeded. Size of allocated intermediates: %!l(MISSING)u KB"
- "<<<< MattingV2 >>>> %!s(MISSING): Breach of integration contract. Disparity refinement configurationVersion was 0, but FigMattingOutputRefinedDisparity was enabled. Performing disparity refinement anyway."
- "<<<< MattingV2 >>>> %!s(MISSING): Depth filter is enabled. Composing RGBD guide"
- "<<<< MattingV2 >>>> %!s(MISSING): Disparity refinement enabled using version: %!d(MISSING)."
- "<<<< MattingV2 >>>> %!s(MISSING): Enabled outputs: %!@(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Encoding _addTexturesKernel (%!l(MISSING)ux%!l(MISSING)u) + (%!l(MISSING)ux%!l(MISSING)u) -> (%!l(MISSING)ux%!l(MISSING)u)"
- "<<<< MattingV2 >>>> %!s(MISSING): Encoding _composeRGBAGuideKernel rgb (%!l(MISSING)ux%!l(MISSING)u), a (%!l(MISSING)ux%!l(MISSING)u) -> rgba (%!l(MISSING)ux%!l(MISSING)u)"
- "<<<< MattingV2 >>>> %!s(MISSING): Encoding constraints computation for: %!@(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Encoding disparity preprocessing"
- "<<<< MattingV2 >>>> %!s(MISSING): Encoding disparity refinement (version: %!d(MISSING))"
- "<<<< MattingV2 >>>> %!s(MISSING): Encoding disparity refinement guide (%!l(MISSING)ux%!l(MISSING)u)"
- "<<<< MattingV2 >>>> %!s(MISSING): Encoding exclusion of non-skin for faceObservation: %!@(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Encoding matting for collection: %!@(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Encoding skin preprocessing"
- "<<<< MattingV2 >>>> %!s(MISSING): Face observation had no faceSegments property. Maybe inference failed? Skipping this face!"
- "<<<< MattingV2 >>>> %!s(MISSING): Face segment observations provided: %!l(MISSING)u"
- "<<<< MattingV2 >>>> %!s(MISSING): Failed to add semantic output %!d(MISSING) to output collection. Output will not be computed."
- "<<<< MattingV2 >>>> %!s(MISSING): Failed to create non-skin pixelBuffer for faceSegmentObservation (error: %!@(MISSING))"
- "<<<< MattingV2 >>>> %!s(MISSING): Failed to find key %!@(MISSING) in tuning parameters dictionary. Available keys: %!@(MISSING). Trying to continue parsing with the first key: %!@(MISSING) "
- "<<<< MattingV2 >>>> %!s(MISSING): Failed to perform disparity refinement. _refinedDisparityFilter or _preprocessedDisparity was nil"
- "<<<< MattingV2 >>>> %!s(MISSING): Failed to preallocate faceNonSkinTexture intermediate. Texture will be allocated on the fly."
- "<<<< MattingV2 >>>> %!s(MISSING): Incomplete or missing plist. Going with defaults."
- "<<<< MattingV2 >>>> %!s(MISSING): Matting tuning dictionary is not the same for %!@(MISSING) and %!@(MISSING). This is not supported. Will always use tuning parameters for: %!@(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Parsed unexpected tuning structure. The key %!@(MISSING) was not found in any of the specified dictionaries: %!@(MISSING). Defaulting to the value: %!@(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Parsing semantic tuning parameters for outputKey: %!@(MISSING) "
- "<<<< MattingV2 >>>> %!s(MISSING): Performance note: Creating MTLTextureType2DArray texture view."
- "<<<< MattingV2 >>>> %!s(MISSING): Performance problem: Failed to bind MTLTexture to faceSegmentProbabilityPixelBuffer. Allocating intermediate texture and copying data on the CPU."
- "<<<< MattingV2 >>>> %!s(MISSING): Performance problem: No matching preallocated faceNonSkinTexture available. New texture will be allocated."
- "<<<< MattingV2 >>>> %!s(MISSING): Provided configurationVersion is negative. Defaulting to configuration 0."
- "<<<< MattingV2 >>>> %!s(MISSING): Provided configurationVersion is unsupported. Defaulting to configuration 0."
- "<<<< MattingV2 >>>> %!s(MISSING): Tuning parameters from plist received"
- "<<<< MattingV2 >>>> %!s(MISSING): Unexpected FigMattingTuningConfiguration. Defaulting to FigMattingTuningConfigurationFine"
- "<<<< MattingV2 >>>> %!s(MISSING): Unexpected semantic output identifier: %!u(MISSING); no output configuration will be returned"
- "<<<< MattingV2 >>>> %!s(MISSING): Unsupported resolution mode %!u(MISSING). Falling back to %!u(MISSING)x%!u(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Using provided metal command queue %!p(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): Using syntheticFocusRectangle: (%!f(MISSING), %!f(MISSING)), %!f(MISSING) x %!f(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): WARNING: Failed to parse disparity refinement version from SDOFRenderingParameters. Falling back to disparity refinement version 0; options dictionary had following keys: %!@(MISSING)"
- "<<<< MattingV2 >>>> %!s(MISSING): syntheticFocusRectangle was not set -- falling back to default value: (%!f(MISSING), %!f(MISSING)), %!f(MISSING) x %!f(MISSING)"
- "FIGMETALCONTEXT_CHECK_ERRCODE"
- "_readKeyWithDefault"
- "commandBuffer is NULL"
- "encoder is NULL"
- "inputDisparity has incorrect pixel format"
- "inputDisparityTexture.height != outputDisparityTexture.height"
- "inputDisparityTexture.width != outputDisparityTexture.width"
- "kFigBaseObjectError_ParamErr"

```
