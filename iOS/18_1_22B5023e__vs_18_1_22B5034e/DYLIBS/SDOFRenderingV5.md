## SDOFRenderingV5

> `/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5`

```diff

-575.5.1.0.0
-  __TEXT.__text: 0xfb24
-  __TEXT.__auth_stubs: 0x480
+580.2.0.0.0
+  __TEXT.__text: 0x14714
+  __TEXT.__auth_stubs: 0x4d0
   __TEXT.__objc_methlist: 0x770
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x3ba8
-  __TEXT.__gcc_except_tab: 0xac
+  __TEXT.__const: 0x310
+  __TEXT.__cstring: 0x4f3c
+  __TEXT.__oslogstring: 0xfb8
+  __TEXT.__gcc_except_tab: 0xc8
   __TEXT.__dlopen_cstrs: 0x4d
-  __TEXT.__unwind_info: 0x280
+  __TEXT.__unwind_info: 0x288
   __TEXT.__objc_classname: 0x11f
   __TEXT.__objc_methname: 0x2489
   __TEXT.__objc_methtype: 0x26e3

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x788
   __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x250
+  __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x5e0
+  __AUTH_CONST.__cfstring: 0x620
   __AUTH_CONST.__objc_const: 0x14b8
   __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__objc_ivar: 0x18c
   __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__common: 0x20
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 196
-  Symbols:   117
-  CStrings:  973
+  Symbols:   122
+  CStrings:  1139
 
Symbols:
+ _fig_note_initialize_category_with_default_work_cf
+ _FigGetUpTimeNanoseconds
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _FigSignalErrorAt3
+ _os_log_type_enabled
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
- _FigSignalErrorAt
- _objc_release_x1
CStrings:
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Total time in computeBlurMapWithImage: %!l(MISSING)ld ms"
+ "_blurMapRefinement_alphaMaskDelta is NULL"
+ "landmarkToC0"
+ "<<<< SDOFRendering V5 >>>>"
+ "-[ControlLogicForXHLRB initWithMetalContext:]"
+ "<<<< SDOF (ControlLogicForXHLRB V5) >>>>"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Error: failed to decode parameters data; default values will be used instead"
+ "-[ControlLogicForXHLRB calculateXHLRBParamsWithInputMetadata:controlLogicParams:inputSlmParams:inputShiftMap:inputLuma:inputChroma:outputParams:]"
+ "-[FigSDOFRenderingTuningParameters initWithTuningDictionary:]"
+ "_rendering_halfResRGBAsRGB1_texalias is NULL"
+ "YES"
+ "controlLogicParams is NULL"
+ "inputAdjBlurMapTex is NULL"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting hairAdditiveMaxBlur: %!f(MISSING)"
+ "-[SimpleLensModel enqueueCalcWithSimpleLensParams:inputShiftMap:outputSlmParams:]"
+ "_minMax2_kernel is NULL"
+ "_disparityRefinement_sampledD_tex is NULL"
+ "-[SDOFResources deallocateResources]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF tuning: %!s(MISSING) is not present"
+ "inputChromaTex is NULL"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): buffer4 old state = %!d(MISSING)"
+ "_minMax0_kernel is NULL"
+ "inputChromaTex has incorrect width"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): bufferLength = %!l(MISSING)u"
+ "-[ControlLogicForXHLRB enqueueControlLogicWithInputMetadata:controlLogicParams:inputSlmParams:inputShiftMap:inputLuma:inputChroma:outputParams:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting additiveMaxBlur: %!f(MISSING)"
+ "NO"
+ "_rendering_halfResRG_tex is NULL"
+ "_rendering_halfResRGBAsRGB2_texalias is NULL"
+ "_minMax1_kernel is NULL"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/SDOFRendering/Common/sdof_rendering_faces.m %!s(MISSING): Unknown rotation value for a landmark."
+ "_slm_mapping_buf is NULL"
+ "-[FigSDOFBlurMapRendering detectFacesOnTele:meta:to:maxFacesCount:facesCount:]"
+ "-1"
+ "encoder is NULL"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): updateSegFusionParamsForSampleBuffer failed with status %!d(MISSING), will use bright light params."
+ "inputSemanticSegmentationGlassesMaskTex is NULL"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): buffer2 old state = %!d(MISSING)"
+ "-[SimpleLensModel enqueueMinMaxWithInputShiftMapTex:]"
+ "self is NULL"
+ "_disparityRefinement_preproc_tex is NULL"
+ "_rendering_halfResRGBA2_tex is NULL"
+ "-[FigSDOFRenderingTuningParameters calculateXHLRBParamsForSampleBuffer:tuningParams:outParams:]"
+ "-[FigSDOFRenderingTuningParameters parameterSetForMode:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Foreground Blur resource allocation in SDOF bundle is %!s(MISSING)"
+ "_disparityRefinement_blurmap_tex is NULL"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF tuning: %!s(MISSING) = %!f(MISSING)"
+ "sdof_resources_trace"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): XXX Rendering dict = %!@(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): calculateXHLRBParamsForSampleBuffer failed with status %!d(MISSING), XHLRB will be disabled."
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting hairSubtractiveMaxBlur: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Using provided metal command queue %!p(MISSING)"
+ "_disparityRefinement_weightsY_tex is NULL"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Smartcam/utilities/utl_roi.m %!s(MISSING): Scale must not be lower than 0.25 to make use of the MSR. You likely need to use a larger scratch buffer. Scale is %!f(MISSING)."
+ "-[SimpleLensModel enqueueSlmCalcWithInputShiftMap:slmParams:simpleLensParams:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Total time in runSamplingWithImage: %!l(MISSING)ld ms"
+ "inputChromaTex has incorrect pixel format"
+ "-[SDOFResources allocateResourcesUsingMetalContext:inputImageWidth:inputImageHeight:shiftMapWidth:shiftMapHeight:enableForegroundBlur:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRendering: Did not get tuning parameters in options."
+ "kFigBaseObjectError_ParamErr"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): Couldn't allocate SDOFResources singleton"
+ "-[FigSDOFEffectRendering runSamplingWithImage:inputPixelBuffer:inputFaceAdjustedBlurMap:inputAlphaMask:inputGainMap:resultImage:]"
+ "-[SDOFResources deactivateResources]"
+ "inputSlmParamsBuf is NULL"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF Rendering Input Version: = %!d(MISSING)"
+ "_count_clipped_kernel is NULL"
+ "_minMaxResult_buf is NULL"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRenderingV5 runSamplingWithImage failed with err=%!d(MISSING)"
+ "-[FigSDOFRenderingTuningParametersSet initWithTuningDictionary:suffix:]"
+ "inputChromaTex has incorrect height"
+ "inputGainMapTex is NULL"
+ "-[FigSDOFBlurMapRendering prewarmWithTuningParameters:]"
+ "inputMetadata is NULL"
+ "-[FigSDOFEffectRendering initWithCommandQueue:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): parameterSetForMode: mode=%!d(MISSING) not supported"
+ "DISABLED"
+ "resultImageLumaTex is NULL"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): referenceCount = %!d(MISSING)"
+ "%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)"
+ "-[SimpleLensModel allocateResourcesForShiftMapWidth:shiftMapHeight:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Warning: Unable to parse NMP parameters - are these expected for this camera?"
+ "-[FigUtlROIProcessor processImage:orientation:rect:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Total time in SDOFRenderingV5:encodeParametersForSampleBuffer: %!l(MISSING)ld ms"
+ "inputLumaTex has incorrect pixel format"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): XXX HairNet dict = %!@(MISSING)"
+ "_halfResRGBABuffer2 is NULL"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): buffer1 old state = %!d(MISSING)"
+ "inputShiftMapTex is NULL"
+ "-[FigSDOFBlurMapRendering allocateResourcesForInputImageWidth:inputImageHeight:shiftMapWidth:shiftMapHeight:enableForegroundBlur:]"
+ "-[FigSDOFBlurMapRendering computeBlurMapWithImage:shiftMap:personSegmentationMask:hairSemanticSegmentationMask:glassesSemanticSegmentationMask:resultFaceAdjustedBlurMap:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Rendering dict = %!@(MISSING)"
+ "-[FigSDOFBlurMapRendering setOptionsInternal:isPrewarm:]"
+ "outputSlmParamsBuf is NULL"
+ "simpleLensParams is NULL"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Face detection failed. Continuing without face term."
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Error: failed to get parameters data; default values will be used"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting subtractiveMaxBlur: %!f(MISSING)"
+ "_rendering_halfResRGBA1_tex is NULL"
+ "-[FigDepthBlurEffectRenderingParametersV4_Builder initWithVersion:]"
+ "maybeValueInt"
+ "-[FigSDOFRenderingTuningParameters encodeParametersForSampleBuffer:captureType:]"
+ "<<<< SDOF (SimpleLensModel V5) >>>>"
+ "resultImage is NULL"
+ "sdof_rendering_trace"
+ "-[ControlLogicForXHLRB loadShaders]"
+ "shiftMapTex has incorrect pixel format"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF Rendering Version Header: = %!d(MISSING)"
+ "buffer is NULL"
+ "inputAlphaTex is NULL"
+ "_nClippedPixelsBuf is NULL"
+ "commandBuffer is NULL"
+ "+[SDOFResources sharedInstance]_block_invoke"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Time for face detection alone: %!l(MISSING)ld"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Faces detected: %!d(MISSING)"
+ "-[FigSDOFEffectRendering setOptionsInternal:isPrewarm:]"
+ "inputSemanticSegmentationHairMaskTex is NULL"
+ "-[SimpleLensModel initWithMetalContext:]"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): Foreground blur enabled when creating resources = %!s(MISSING)"
+ "ENABLED"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRendering: Tuning parameters after initialization is %!p(MISSING)."
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRenderingV5 computeBlurMapWithImage failed with err=%!d(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRendering: Found tuning parameters dictionary, initializing tuning parameters."
+ "-[FigSDOFRenderingTuningParametersSet readRenderingConfig:]"
+ "_calc_kernel is NULL"
+ "readDynamicParameter"
+ "_faceMask_adjBlurmap_tex is NULL"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): resulting disparityScalingFactor: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): exposureLevel: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): FocusRectangle: valid: %!d(MISSING), coords: %!f(MISSING), %!f(MISSING), %!f(MISSING), %!f(MISSING)"
+ "inputImageChromaTex is NULL"
+ "inputSegmentationMaskTex is NULL"
+ "-[FigSDOFRenderingTuningParametersSet readHairNetConfig:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF tuning: %!s(MISSING) = %!d(MISSING)"
+ "_disparityRefinement_weightsX_tex is NULL"
+ "-[ControlLogicForXHLRB validateInputsWithInputMetadata:inputSlmParams:inputShiftMap:inputLuma:inputChroma:outputParams:]"
+ "_blurMapSmoothing_intermediate_tex is NULL"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Output blur map has foreground blur enabled = %!s(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOFRendering Rendering set with options %!@(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): The orientation we got from metadata is not supported. Orientation: %!d(MISSING)"
+ "inputSampleBuffer is NULL"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): focusDistanceRatio: %!f(MISSING)"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): focalLengthInPixels = %!f(MISSING)"
+ "-[FigSDOFBlurMapRendering initWithCommandQueue:]"
+ "<<<< SDOFResources(V5) >>>> %!s(MISSING): buffer3 old state = %!d(MISSING)"
+ "computeEncoder is NULL"
+ "outputParams is NULL"
+ "tuningParameters is nil."
+ "resultAdjBlurMapTex is NULL"
+ "_rendering_xhlrbProcessList_buf is NULL"
+ "-[FigSDOFEffectRendering prewarmWithTuningParameters:]"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): SDOF tuning: %!s(MISSING) = {Xb=%!f(MISSING), Xl=%!f(MISSING), Xn=%!f(MISSING), Xf=%!f(MISSING), Ybn=%!f(MISSING), Ybf=%!f(MISSING), Yln=%!f(MISSING), Ylf=%!f(MISSING)"
+ "_blurMapRefinement_hairMaskDelta is NULL"
+ "inputShiftMapTex has incorrect pixel format"
+ "<<<< SDOFRendering V5 >>>> %!s(MISSING): Actual SDOF version used = %!d(MISSING)"
+ "inputImageLumaTex is NULL"
+ "-[SDOFResources activateResources]"
+ "_blurMapSmoothing_result_tex is NULL"
+ "-[FigSDOFRenderingTuningParameters calculateDynamicTuningParamsForSampleBuffer:dynamicParams:outSegmentationFusionConfig:outSimpleLensModelConfig:outBlurmapRefinementConfig:]"
+ "_blurMapRefinement_intermediate is NULL"
+ "inputLumaTex is NULL"
+ "outputParamsBuf has insufficient length"
+ "maybeValueFloat"
+ "resultImageChromaTex is NULL"
+ "_halfResRGBABuffer1 is NULL"
+ "<<<< SDOFResources(V5) >>>>"
+ "_minMaxAtomic_buf is NULL"

```
