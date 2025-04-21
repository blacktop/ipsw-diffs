## SDOFRenderingV5

> `/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5`

```diff

-587.120.5.0.0
-  __TEXT.__text: 0x15a98
-  __TEXT.__auth_stubs: 0x4e0
+587.122.6.0.2
+  __TEXT.__text: 0x10ef4
+  __TEXT.__auth_stubs: 0x490
   __TEXT.__objc_methlist: 0x7a0
-  __TEXT.__const: 0x310
-  __TEXT.__cstring: 0x4f2e
-  __TEXT.__oslogstring: 0xfb8
-  __TEXT.__gcc_except_tab: 0xbc
+  __TEXT.__const: 0x2f0
+  __TEXT.__cstring: 0x3ba5
+  __TEXT.__gcc_except_tab: 0xa0
   __TEXT.__dlopen_cstrs: 0x4d
-  __TEXT.__unwind_info: 0x320
+  __TEXT.__unwind_info: 0x2d0
   __TEXT.__objc_classname: 0x11f
   __TEXT.__objc_methname: 0x24e0
   __TEXT.__objc_methtype: 0x26f8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x790
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x280
+  __AUTH_CONST.__auth_got: 0x258
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x620
+  __AUTH_CONST.__cfstring: 0x5e0
   __AUTH_CONST.__objc_const: 0x1518
   __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__objc_ivar: 0x194
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x320
-  __DATA_DIRTY.__common: 0x20
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 410
-  Symbols:   123
-  CStrings:  1143
+  Functions: 394
+  Symbols:   118
+  CStrings:  977
 
Symbols:
+ _FigSignalErrorAt
+ _objc_release_x1
- _FigGetUpTimeNanoseconds
- _FigSignalErrorAt3
- __os_log_send_and_compose_impl
- _fig_log_call_emit_and_clean_up_after_send_and_compose
- _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _fig_note_initialize_category_with_default_work_cf
- _os_log_type_enabled
CStrings:
- "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
- "+[SDOFResources sharedInstance]_block_invoke"
- "-[ControlLogicForXHLRB calculateXHLRBParamsWithInputMetadata:controlLogicParams:inputSlmParams:inputShiftMap:inputLuma:inputChroma:outputParams:]"
- "-[ControlLogicForXHLRB enqueueControlLogicWithInputMetadata:controlLogicParams:inputSlmParams:inputShiftMap:inputLuma:inputChroma:outputParams:]"
- "-[ControlLogicForXHLRB initWithMetalContext:]"
- "-[ControlLogicForXHLRB loadShaders]"
- "-[ControlLogicForXHLRB validateInputsWithInputMetadata:inputSlmParams:inputShiftMap:inputLuma:inputChroma:outputParams:]"
- "-[FigDepthBlurEffectRenderingParametersV4_Builder initWithVersion:]"
- "-[FigSDOFBlurMapRendering _prewarm:]"
- "-[FigSDOFBlurMapRendering allocateResourcesForInputImageWidth:inputImageHeight:shiftMapWidth:shiftMapHeight:enableForegroundBlur:]"
- "-[FigSDOFBlurMapRendering computeBlurMapWithImage:shiftMap:personSegmentationMask:hairSemanticSegmentationMask:glassesSemanticSegmentationMask:resultFaceAdjustedBlurMap:]"
- "-[FigSDOFBlurMapRendering detectFacesOnTele:meta:to:maxFacesCount:facesCount:]"
- "-[FigSDOFBlurMapRendering initWithCommandQueue:]"
- "-[FigSDOFBlurMapRendering setOptionsInternal:isPrewarm:]"
- "-[FigSDOFEffectRendering _prewarm:]"
- "-[FigSDOFEffectRendering initWithCommandQueue:]"
- "-[FigSDOFEffectRendering runSamplingWithImage:inputPixelBuffer:inputFaceAdjustedBlurMap:inputAlphaMask:inputGainMap:resultImage:]"
- "-[FigSDOFEffectRendering setOptionsInternal:isPrewarm:]"
- "-[FigSDOFRenderingTuningParameters calculateDynamicTuningParamsForSampleBuffer:dynamicParams:outSegmentationFusionConfig:outSimpleLensModelConfig:outBlurmapRefinementConfig:]"
- "-[FigSDOFRenderingTuningParameters calculateXHLRBParamsForSampleBuffer:tuningParams:outParams:]"
- "-[FigSDOFRenderingTuningParameters encodeParametersForSampleBuffer:captureType:]"
- "-[FigSDOFRenderingTuningParameters initWithTuningDictionary:]"
- "-[FigSDOFRenderingTuningParameters parameterSetForMode:]"
- "-[FigSDOFRenderingTuningParametersSet initWithTuningDictionary:suffix:]"
- "-[FigSDOFRenderingTuningParametersSet readHairNetConfig:]"
- "-[FigSDOFRenderingTuningParametersSet readRenderingConfig:]"
- "-[FigUtlROIProcessor processImage:orientation:rect:]"
- "-[SDOFResources activateResources]"
- "-[SDOFResources allocateResourcesUsingMetalContext:inputImageWidth:inputImageHeight:shiftMapWidth:shiftMapHeight:enableForegroundBlur:]"
- "-[SDOFResources deactivateResources]"
- "-[SDOFResources deallocateResources]"
- "-[SimpleLensModel allocateResourcesForShiftMapWidth:shiftMapHeight:]"
- "-[SimpleLensModel enqueueCalcWithSimpleLensParams:inputShiftMap:outputSlmParams:]"
- "-[SimpleLensModel enqueueMinMaxWithInputShiftMapTex:]"
- "-[SimpleLensModel enqueueSlmCalcWithInputShiftMap:slmParams:simpleLensParams:]"
- "-[SimpleLensModel initWithMetalContext:]"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/SDOFRendering/Common/sdof_rendering_faces.m %s: Unknown rotation value for a landmark."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Smartcam/utilities/utl_roi.m %s: Scale must not be lower than 0.25 to make use of the MSR. You likely need to use a larger scratch buffer. Scale is %f."
- "<<<< SDOF (ControlLogicForXHLRB V5) >>>>"
- "<<<< SDOF (SimpleLensModel V5) >>>>"
- "<<<< SDOFRendering V5 >>>>"
- "<<<< SDOFRendering V5 >>>> %s: Actual SDOF version used = %d"
- "<<<< SDOFRendering V5 >>>> %s: Error: failed to decode parameters data; default values will be used instead"
- "<<<< SDOFRendering V5 >>>> %s: Error: failed to get parameters data; default values will be used"
- "<<<< SDOFRendering V5 >>>> %s: Face detection failed. Continuing without face term."
- "<<<< SDOFRendering V5 >>>> %s: Faces detected: %d"
- "<<<< SDOFRendering V5 >>>> %s: FocusRectangle: valid: %d, coords: %f, %f, %f, %f"
- "<<<< SDOFRendering V5 >>>> %s: Foreground Blur resource allocation in SDOF bundle is %s"
- "<<<< SDOFRendering V5 >>>> %s: Output blur map has foreground blur enabled = %s"
- "<<<< SDOFRendering V5 >>>> %s: Rendering dict = %@"
- "<<<< SDOFRendering V5 >>>> %s: SDOF Rendering Input Version: = %d"
- "<<<< SDOFRendering V5 >>>> %s: SDOF Rendering Version Header: = %d"
- "<<<< SDOFRendering V5 >>>> %s: SDOF tuning: %s = %d"
- "<<<< SDOFRendering V5 >>>> %s: SDOF tuning: %s = %f"
- "<<<< SDOFRendering V5 >>>> %s: SDOF tuning: %s = {Xb=%f, Xl=%f, Xn=%f, Xf=%f, Ybn=%f, Ybf=%f, Yln=%f, Ylf=%f"
- "<<<< SDOFRendering V5 >>>> %s: SDOF tuning: %s is not present"
- "<<<< SDOFRendering V5 >>>> %s: SDOFRendering Rendering set with options %@"
- "<<<< SDOFRendering V5 >>>> %s: SDOFRendering: Did not get tuning parameters in options."
- "<<<< SDOFRendering V5 >>>> %s: SDOFRendering: Found tuning parameters dictionary, initializing tuning parameters."
- "<<<< SDOFRendering V5 >>>> %s: SDOFRendering: Tuning parameters after initialization is %p."
- "<<<< SDOFRendering V5 >>>> %s: SDOFRenderingV5 computeBlurMapWithImage failed with err=%d"
- "<<<< SDOFRendering V5 >>>> %s: SDOFRenderingV5 runSamplingWithImage failed with err=%d"
- "<<<< SDOFRendering V5 >>>> %s: The orientation we got from metadata is not supported. Orientation: %d"
- "<<<< SDOFRendering V5 >>>> %s: Time for face detection alone: %lld"
- "<<<< SDOFRendering V5 >>>> %s: Total time in SDOFRenderingV5:encodeParametersForSampleBuffer: %lld ms"
- "<<<< SDOFRendering V5 >>>> %s: Total time in computeBlurMapWithImage: %lld ms"
- "<<<< SDOFRendering V5 >>>> %s: Total time in runSamplingWithImage: %lld ms"
- "<<<< SDOFRendering V5 >>>> %s: Using provided metal command queue %p"
- "<<<< SDOFRendering V5 >>>> %s: Warning: Unable to parse NMP parameters - are these expected for this camera?"
- "<<<< SDOFRendering V5 >>>> %s: XXX HairNet dict = %@"
- "<<<< SDOFRendering V5 >>>> %s: XXX Rendering dict = %@"
- "<<<< SDOFRendering V5 >>>> %s: calculateXHLRBParamsForSampleBuffer failed with status %d, XHLRB will be disabled."
- "<<<< SDOFRendering V5 >>>> %s: exposureLevel: %f"
- "<<<< SDOFRendering V5 >>>> %s: focalLengthInPixels = %f"
- "<<<< SDOFRendering V5 >>>> %s: focusDistanceRatio: %f"
- "<<<< SDOFRendering V5 >>>> %s: parameterSetForMode: mode=%d not supported"
- "<<<< SDOFRendering V5 >>>> %s: resulting additiveMaxBlur: %f"
- "<<<< SDOFRendering V5 >>>> %s: resulting disparityScalingFactor: %f"
- "<<<< SDOFRendering V5 >>>> %s: resulting hairAdditiveMaxBlur: %f"
- "<<<< SDOFRendering V5 >>>> %s: resulting hairSubtractiveMaxBlur: %f"
- "<<<< SDOFRendering V5 >>>> %s: resulting subtractiveMaxBlur: %f"
- "<<<< SDOFRendering V5 >>>> %s: updateSegFusionParamsForSampleBuffer failed with status %d, will use bright light params."
- "<<<< SDOFResources(V5) >>>>"
- "<<<< SDOFResources(V5) >>>> %s: Couldn't allocate SDOFResources singleton"
- "<<<< SDOFResources(V5) >>>> %s: Foreground blur enabled when creating resources = %s"
- "<<<< SDOFResources(V5) >>>> %s: buffer1 old state = %d"
- "<<<< SDOFResources(V5) >>>> %s: buffer2 old state = %d"
- "<<<< SDOFResources(V5) >>>> %s: buffer3 old state = %d"
- "<<<< SDOFResources(V5) >>>> %s: buffer4 old state = %d"
- "<<<< SDOFResources(V5) >>>> %s: bufferLength = %lu"
- "<<<< SDOFResources(V5) >>>> %s: referenceCount = %d"
- "DISABLED"
- "ENABLED"
- "FIGMETALCONTEXT_CHECK_ERRCODE"
- "NO"
- "YES"
- "_blurMapRefinement_alphaMaskDelta is NULL"
- "_blurMapRefinement_hairMaskDelta is NULL"
- "_blurMapRefinement_intermediate is NULL"
- "_blurMapSmoothing_intermediate_tex is NULL"
- "_blurMapSmoothing_result_tex is NULL"
- "_calc_kernel is NULL"
- "_count_clipped_kernel is NULL"
- "_disparityRefinement_blurmap_tex is NULL"
- "_disparityRefinement_preproc_tex is NULL"
- "_disparityRefinement_sampledD_tex is NULL"
- "_disparityRefinement_weightsX_tex is NULL"
- "_disparityRefinement_weightsY_tex is NULL"
- "_faceMask_adjBlurmap_tex is NULL"
- "_halfResRGBABuffer1 is NULL"
- "_halfResRGBABuffer2 is NULL"
- "_minMax0_kernel is NULL"
- "_minMax1_kernel is NULL"
- "_minMax2_kernel is NULL"
- "_minMaxAtomic_buf is NULL"
- "_minMaxResult_buf is NULL"
- "_nClippedPixelsBuf is NULL"
- "_rendering_halfResRGBA1_tex is NULL"
- "_rendering_halfResRGBA2_tex is NULL"
- "_rendering_halfResRGBAsRGB1_texalias is NULL"
- "_rendering_halfResRGBAsRGB2_texalias is NULL"
- "_rendering_halfResRG_tex is NULL"
- "_rendering_xhlrbProcessList_buf is NULL"
- "_slm_mapping_buf is NULL"
- "buffer is NULL"
- "commandBuffer is NULL"
- "computeEncoder is NULL"
- "controlLogicParams is NULL"
- "encoder is NULL"
- "inputAdjBlurMapTex is NULL"
- "inputAlphaTex is NULL"
- "inputChromaTex has incorrect height"
- "inputChromaTex has incorrect pixel format"
- "inputChromaTex has incorrect width"
- "inputChromaTex is NULL"
- "inputGainMapTex is NULL"
- "inputImageChromaTex is NULL"
- "inputImageLumaTex is NULL"
- "inputLumaTex has incorrect pixel format"
- "inputLumaTex is NULL"
- "inputMetadata is NULL"
- "inputSampleBuffer is NULL"
- "inputSegmentationMaskTex is NULL"
- "inputSemanticSegmentationGlassesMaskTex is NULL"
- "inputSemanticSegmentationHairMaskTex is NULL"
- "inputShiftMapTex has incorrect pixel format"
- "inputShiftMapTex is NULL"
- "inputSlmParamsBuf is NULL"
- "kFigBaseObjectError_ParamErr"
- "landmarkToC0"
- "maybeValueFloat"
- "maybeValueInt"
- "outputParams is NULL"
- "outputParamsBuf has insufficient length"
- "outputSlmParamsBuf is NULL"
- "readDynamicParameter"
- "resultAdjBlurMapTex is NULL"
- "resultImage is NULL"
- "resultImageChromaTex is NULL"
- "resultImageLumaTex is NULL"
- "sdof_rendering_trace"
- "sdof_resources_trace"
- "self is NULL"
- "shiftMapTex has incorrect pixel format"
- "simpleLensParams is NULL"
- "tuningParameters is nil."

```
