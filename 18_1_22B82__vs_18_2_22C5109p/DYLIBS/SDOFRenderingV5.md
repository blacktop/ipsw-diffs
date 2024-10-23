## SDOFRenderingV5

> `/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5`

```diff

-580.14.5.0.0
-  __TEXT.__text: 0xfbe0
-  __TEXT.__auth_stubs: 0x480
-  __TEXT.__objc_methlist: 0x770
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x3ba8
-  __TEXT.__gcc_except_tab: 0xac
+587.60.6.0.0
+  __TEXT.__text: 0x14894
+  __TEXT.__auth_stubs: 0x4d0
+  __TEXT.__objc_methlist: 0x7a0
+  __TEXT.__const: 0x310
+  __TEXT.__cstring: 0x4f31
+  __TEXT.__oslogstring: 0xfb8
+  __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__dlopen_cstrs: 0x4d
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__unwind_info: 0x288
   __TEXT.__objc_classname: 0x11f
-  __TEXT.__objc_methname: 0x2489
-  __TEXT.__objc_methtype: 0x26e3
-  __TEXT.__objc_stubs: 0x1980
-  __DATA_CONST.__got: 0x108
+  __TEXT.__objc_methname: 0x24e0
+  __TEXT.__objc_methtype: 0x26f8
+  __TEXT.__objc_stubs: 0x1960
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x788
+  __DATA_CONST.__objc_selrefs: 0x790
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x250
+  __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x5e0
-  __AUTH_CONST.__objc_const: 0x14b8
+  __AUTH_CONST.__cfstring: 0x620
+  __AUTH_CONST.__objc_const: 0x1518
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x18c
+  __DATA.__objc_ivar: 0x194
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__common: 0x20
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 196
-  Symbols:   117
-  CStrings:  973
+  Functions: 200
+  Symbols:   122
+  CStrings:  1143
 
Symbols:
+ _FigGetUpTimeNanoseconds
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _os_log_type_enabled
- _FigSignalErrorAt
- _objc_release_x1
CStrings:
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "+[SDOFResources sharedInstance]_block_invoke"
+ "-[ControlLogicForXHLRB calculateXHLRBParamsWithInputMetadata:controlLogicParams:inputSlmParams:inputShiftMap:inputLuma:inputChroma:outputParams:]"
+ "-[ControlLogicForXHLRB enqueueControlLogicWithInputMetadata:controlLogicParams:inputSlmParams:inputShiftMap:inputLuma:inputChroma:outputParams:]"
+ "-[ControlLogicForXHLRB initWithMetalContext:]"
+ "-[ControlLogicForXHLRB loadShaders]"
+ "-[ControlLogicForXHLRB validateInputsWithInputMetadata:inputSlmParams:inputShiftMap:inputLuma:inputChroma:outputParams:]"
+ "-[FigDepthBlurEffectRenderingParametersV4_Builder initWithVersion:]"
+ "-[FigSDOFBlurMapRendering _prewarm:]"
+ "-[FigSDOFBlurMapRendering allocateResourcesForInputImageWidth:inputImageHeight:shiftMapWidth:shiftMapHeight:enableForegroundBlur:]"
+ "-[FigSDOFBlurMapRendering computeBlurMapWithImage:shiftMap:personSegmentationMask:hairSemanticSegmentationMask:glassesSemanticSegmentationMask:resultFaceAdjustedBlurMap:]"
+ "-[FigSDOFBlurMapRendering detectFacesOnTele:meta:to:maxFacesCount:facesCount:]"
+ "-[FigSDOFBlurMapRendering initWithCommandQueue:]"
+ "-[FigSDOFBlurMapRendering setOptionsInternal:isPrewarm:]"
+ "-[FigSDOFEffectRendering _prewarm:]"
+ "-[FigSDOFEffectRendering initWithCommandQueue:]"
+ "-[FigSDOFEffectRendering runSamplingWithImage:inputPixelBuffer:inputFaceAdjustedBlurMap:inputAlphaMask:inputGainMap:resultImage:]"
+ "-[FigSDOFEffectRendering setOptionsInternal:isPrewarm:]"
+ "-[FigSDOFRenderingTuningParameters calculateDynamicTuningParamsForSampleBuffer:dynamicParams:outSegmentationFusionConfig:outSimpleLensModelConfig:outBlurmapRefinementConfig:]"
+ "-[FigSDOFRenderingTuningParameters calculateXHLRBParamsForSampleBuffer:tuningParams:outParams:]"
+ "-[FigSDOFRenderingTuningParameters encodeParametersForSampleBuffer:captureType:]"
+ "-[FigSDOFRenderingTuningParameters initWithTuningDictionary:]"
+ "-[FigSDOFRenderingTuningParameters parameterSetForMode:]"
+ "-[FigSDOFRenderingTuningParametersSet initWithTuningDictionary:suffix:]"
+ "-[FigSDOFRenderingTuningParametersSet readHairNetConfig:]"
+ "-[FigSDOFRenderingTuningParametersSet readRenderingConfig:]"
+ "-[FigUtlROIProcessor processImage:orientation:rect:]"
+ "-[SDOFResources activateResources]"
+ "-[SDOFResources allocateResourcesUsingMetalContext:inputImageWidth:inputImageHeight:shiftMapWidth:shiftMapHeight:enableForegroundBlur:]"
+ "-[SDOFResources deactivateResources]"
+ "-[SDOFResources deallocateResources]"
+ "-[SimpleLensModel allocateResourcesForShiftMapWidth:shiftMapHeight:]"
+ "-[SimpleLensModel enqueueCalcWithSimpleLensParams:inputShiftMap:outputSlmParams:]"
+ "-[SimpleLensModel enqueueMinMaxWithInputShiftMapTex:]"
+ "-[SimpleLensModel enqueueSlmCalcWithInputShiftMap:slmParams:simpleLensParams:]"
+ "-[SimpleLensModel initWithMetalContext:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/SDOFRendering/Common/sdof_rendering_faces.m %!s(MISSING): Unknown rotation value for a landmark."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Smartcam/utilities/utl_roi.m %!s(MISSING): Scale must not be lower than 0.25 to make use of the MSR. You likely need to use a larger scratch buffer. Scale is %!f(MISSING)."
+ "<<<< SDOF (ControlLogicForXHLRB V5) >>>>"
+ "<<<< SDOF (SimpleLensModel V5) >>>>"
+ "<<<< SDOFRendering V5 >>>>"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Actual SDOF version used = %!d(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Error: failed to decode parameters data; default values will be used instead"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Error: failed to get parameters data; default values will be used"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Face detection failed. Continuing without face term."
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Faces detected: %!d(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): FocusRectangle: valid: %!d(MISSING), coords: %!f(MISSING), %!f(MISSING), %!f(MISSING), %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Foreground Blur resource allocation in SDOF bundle is %!s(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Output blur map has foreground blur enabled = %!s(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Rendering dict = %!@(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF Rendering Input Version: = %!d(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF Rendering Version Header: = %!d(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF tuning: %!s(MISSING) = %!d(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF tuning: %!s(MISSING) = %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF tuning: %!s(MISSING) = {Xb=%!f(MISSING), Xl=%!f(MISSING), Xn=%!f(MISSING), Xf=%!f(MISSING), Ybn=%!f(MISSING), Ybf=%!f(MISSING), Yln=%!f(MISSING), Ylf=%!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF tuning: %!s(MISSING) is not present"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRendering Rendering set with options %!@(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRendering: Did not get tuning parameters in options."
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRendering: Found tuning parameters dictionary, initializing tuning parameters."
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRendering: Tuning parameters after initialization is %!p(MISSING)."
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRenderingV5 computeBlurMapWithImage failed with err=%!d(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRenderingV5 runSamplingWithImage failed with err=%!d(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): The orientation we got from metadata is not supported. Orientation: %!d(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Time for face detection alone: %!l(MISSING)ld"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Total time in SDOFRenderingV5:encodeParametersForSampleBuffer: %!l(MISSING)ld ms"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Total time in computeBlurMapWithImage: %!l(MISSING)ld ms"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Total time in runSamplingWithImage: %!l(MISSING)ld ms"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Using provided metal command queue %!p(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Warning: Unable to parse NMP parameters - are these expected for this camera?"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): XXX HairNet dict = %!@(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): XXX Rendering dict = %!@(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): calculateXHLRBParamsForSampleBuffer failed with status %!d(MISSING), XHLRB will be disabled."
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): exposureLevel: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): focalLengthInPixels = %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): focusDistanceRatio: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): parameterSetForMode: mode=%!d(MISSING) not supported"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting additiveMaxBlur: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting disparityScalingFactor: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting hairAdditiveMaxBlur: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting hairSubtractiveMaxBlur: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting subtractiveMaxBlur: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): updateSegFusionParamsForSampleBuffer failed with status %!d(MISSING), will use bright light params."
+ "<<<< SDOFResources(V5) >>>>"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): Couldn't allocate SDOFResources singleton"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): Foreground blur enabled when creating resources = %!s(MISSING)"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): buffer1 old state = %!d(MISSING)"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): buffer2 old state = %!d(MISSING)"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): buffer3 old state = %!d(MISSING)"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): buffer4 old state = %!d(MISSING)"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): bufferLength = %!l(MISSING)u"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): referenceCount = %!d(MISSING)"
+ "@\"<MTLCommandQueue>\""
+ "DISABLED"
+ "ENABLED"
+ "FIGMETALCONTEXT_CHECK_ERRCODE"
+ "NO"
+ "T@\"<MTLCommandQueue>\",&,N,V_metalCommandQueue"
+ "YES"
+ "_blurMapRefinement_alphaMaskDelta is NULL"
+ "_blurMapRefinement_hairMaskDelta is NULL"
+ "_blurMapRefinement_intermediate is NULL"
+ "_blurMapSmoothing_intermediate_tex is NULL"
+ "_blurMapSmoothing_result_tex is NULL"
+ "_calc_kernel is NULL"
+ "_count_clipped_kernel is NULL"
+ "_disparityRefinement_blurmap_tex is NULL"
+ "_disparityRefinement_preproc_tex is NULL"
+ "_disparityRefinement_sampledD_tex is NULL"
+ "_disparityRefinement_weightsX_tex is NULL"
+ "_disparityRefinement_weightsY_tex is NULL"
+ "_faceMask_adjBlurmap_tex is NULL"
+ "_halfResRGBABuffer1 is NULL"
+ "_halfResRGBABuffer2 is NULL"
+ "_metalCommandQueue"
+ "_minMax0_kernel is NULL"
+ "_minMax1_kernel is NULL"
+ "_minMax2_kernel is NULL"
+ "_minMaxAtomic_buf is NULL"
+ "_minMaxResult_buf is NULL"
+ "_nClippedPixelsBuf is NULL"
+ "_prewarm:"
+ "_rendering_halfResRGBA1_tex is NULL"
+ "_rendering_halfResRGBA2_tex is NULL"
+ "_rendering_halfResRGBAsRGB1_texalias is NULL"
+ "_rendering_halfResRGBAsRGB2_texalias is NULL"
+ "_rendering_halfResRG_tex is NULL"
+ "_rendering_xhlrbProcessList_buf is NULL"
+ "_slm_mapping_buf is NULL"
+ "buffer is NULL"
+ "commandBuffer is NULL"
+ "computeEncoder is NULL"
+ "controlLogicParams is NULL"
+ "encoder is NULL"
+ "f\x12"
+ "h"
+ "inputAdjBlurMapTex is NULL"
+ "inputAlphaTex is NULL"
+ "inputChromaTex has incorrect height"
+ "inputChromaTex has incorrect pixel format"
+ "inputChromaTex has incorrect width"
+ "inputChromaTex is NULL"
+ "inputGainMapTex is NULL"
+ "inputImageChromaTex is NULL"
+ "inputImageLumaTex is NULL"
+ "inputLumaTex has incorrect pixel format"
+ "inputLumaTex is NULL"
+ "inputMetadata is NULL"
+ "inputSampleBuffer is NULL"
+ "inputSegmentationMaskTex is NULL"
+ "inputSemanticSegmentationGlassesMaskTex is NULL"
+ "inputSemanticSegmentationHairMaskTex is NULL"
+ "inputShiftMapTex has incorrect pixel format"
+ "inputShiftMapTex is NULL"
+ "inputSlmParamsBuf is NULL"
+ "kFigBaseObjectError_ParamErr"
+ "landmarkToC0"
+ "maybeValueFloat"
+ "maybeValueInt"
+ "metalCommandQueue"
+ "outputParams is NULL"
+ "outputParamsBuf has insufficient length"
+ "outputSlmParamsBuf is NULL"
+ "readDynamicParameter"
+ "resultAdjBlurMapTex is NULL"
+ "resultImage is NULL"
+ "resultImageChromaTex is NULL"
+ "resultImageLumaTex is NULL"
+ "sdof_rendering_trace"
+ "sdof_resources_trace"
+ "self is NULL"
+ "setMetalCommandQueue:"
+ "shiftMapTex has incorrect pixel format"
+ "simpleLensParams is NULL"
+ "tuningParameters is nil."
- "f\x11"
- "g"
- "metalDevice"
- "newCommandQueue"

```
