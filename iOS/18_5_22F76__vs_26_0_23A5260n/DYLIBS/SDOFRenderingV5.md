## SDOFRenderingV5

> `/System/Library/VideoProcessors/SDOFRenderingV5.bundle/SDOFRenderingV5`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x10ef4
-  __TEXT.__auth_stubs: 0x490
-  __TEXT.__objc_methlist: 0x7a0
-  __TEXT.__const: 0x2f0
-  __TEXT.__cstring: 0x3ba5
-  __TEXT.__gcc_except_tab: 0xa0
+650.0.0.122.4
+  __TEXT.__text: 0x1547c
+  __TEXT.__auth_stubs: 0x4a0
+  __TEXT.__objc_methlist: 0x6f0
+  __TEXT.__const: 0x310
+  __TEXT.__cstring: 0x4b3c
+  __TEXT.__oslogstring: 0x16aa
+  __TEXT.__gcc_except_tab: 0x74
   __TEXT.__dlopen_cstrs: 0x4d
-  __TEXT.__unwind_info: 0x2d0
-  __TEXT.__objc_classname: 0x11f
-  __TEXT.__objc_methname: 0x24e0
-  __TEXT.__objc_methtype: 0x26f8
-  __TEXT.__objc_stubs: 0x1960
-  __DATA_CONST.__got: 0x118
+  __TEXT.__unwind_info: 0x2f0
+  __TEXT.__objc_classname: 0x10a
+  __TEXT.__objc_methname: 0x2286
+  __TEXT.__objc_methtype: 0x25c7
+  __TEXT.__objc_stubs: 0x1900
+  __DATA_CONST.__got: 0x108
   __DATA_CONST.__const: 0xc0
-  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x790
-  __DATA_CONST.__objc_superrefs: 0x50
-  __AUTH_CONST.__auth_got: 0x258
+  __DATA_CONST.__objc_selrefs: 0x738
+  __DATA_CONST.__objc_superrefs: 0x48
+  __AUTH_CONST.__auth_got: 0x260
   __AUTH_CONST.__const: 0x100
-  __AUTH_CONST.__cfstring: 0x5e0
-  __AUTH_CONST.__objc_const: 0x1518
+  __AUTH_CONST.__cfstring: 0x640
+  __AUTH_CONST.__objc_const: 0x1298
   __AUTH_CONST.__objc_intobj: 0x18
-  __DATA.__objc_ivar: 0x194
+  __DATA.__objc_ivar: 0x164
   __DATA.__bss: 0x20
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA_DIRTY.__objc_data: 0x2d0
+  __DATA_DIRTY.__common: 0x20
   __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 47DBF948-E38B-36DF-9DB1-3CD4A4CF052F
-  Functions: 394
-  Symbols:   118
-  CStrings:  1018
+  UUID: 0C989720-F9ED-3437-87BF-C6B105C09409
+  Functions: 364
+  Symbols:   117
+  CStrings:  1134
 
Symbols:
+ _FigGetUpTimeNanoseconds
+ _FigSignalErrorAt3
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _objc_retain_x28
+ _os_log_type_enabled
- _CVPixelBufferRelease
- _CreatePixelBuffer
- _FigSignalErrorAt
- _OBJC_CLASS_$_FigM2MController
- ___invert_d3
- ___stack_chk_fail
- ___stack_chk_guard
- _memcpy
- _objc_release_x1
CStrings:
+ "%c%c%c%c"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
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
+ "-[FigSDOFBlurMapRendering sanityChecksBlurMapWithImage:shiftMap:segmentationMask:semanticSegmentationHairMask:semanticSegmentationGlassesMask:resultFaceAdjBlurMap:]"
+ "-[FigSDOFBlurMapRendering setOptionsInternal:isPrewarm:]"
+ "-[FigSDOFEffectRendering _prewarm:]"
+ "-[FigSDOFEffectRendering initWithCommandQueue:]"
+ "-[FigSDOFEffectRendering runSamplingWithImage:inputPixelBuffer:inputFaceAdjustedBlurMap:inputAlphaMask:inputGainMap:resultImage:]"
+ "-[FigSDOFEffectRendering sanityChecksSamplingWithImage:inputFaceAdjustedBlurMap:inputAlphaMask:inputGainMap:resultImage:]"
+ "-[FigSDOFEffectRendering setOptionsInternal:isPrewarm:]"
+ "-[FigSDOFRenderingTuningParameters calculateDynamicTuningParamsForSampleBuffer:dynamicParams:outSegmentationFusionConfig:outSimpleLensModelConfig:outBlurmapRefinementConfig:]"
+ "-[FigSDOFRenderingTuningParameters calculateXHLRBParamsForSampleBuffer:tuningParams:outParams:]"
+ "-[FigSDOFRenderingTuningParameters encodeParametersForSampleBuffer:captureType:]"
+ "-[FigSDOFRenderingTuningParameters initWithTuningDictionary:]"
+ "-[FigSDOFRenderingTuningParameters parameterSetForMode:]"
+ "-[FigSDOFRenderingTuningParametersSet initWithTuningDictionary:suffix:]"
+ "-[FigSDOFRenderingTuningParametersSet readHairNetConfig:]"
+ "-[FigSDOFRenderingTuningParametersSet readRenderingConfig:]"
+ "-[SDOFResources activateResources]"
+ "-[SDOFResources allocateResourcesUsingMetalContext:inputImageWidth:inputImageHeight:shiftMapWidth:shiftMapHeight:enableForegroundBlur:]"
+ "-[SDOFResources deactivateResources]"
+ "-[SDOFResources deallocateResources]"
+ "-[SimpleLensModel allocateResourcesForShiftMapWidth:shiftMapHeight:]"
+ "-[SimpleLensModel enqueueCalcWithSimpleLensParams:inputShiftMap:outputSlmParams:]"
+ "-[SimpleLensModel enqueueMinMaxWithInputShiftMapTex:]"
+ "-[SimpleLensModel enqueueSlmCalcWithInputShiftMap:slmParams:simpleLensParams:]"
+ "-[SimpleLensModel initWithMetalContext:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/SDOFRendering/Common/sdof_rendering_faces.m %s: Unknown rotation value for a landmark."
+ "<<<< SDOF (ControlLogicForXHLRB V5) >>>>"
+ "<<<< SDOF (SimpleLensModel V5) >>>>"
+ "<<<< SDOFRendering V5 >>>>"
+ "<<<< SDOFRendering V5 >>>> %s: Actual SDOF version used = %d"
+ "<<<< SDOFRendering V5 >>>> %s: Error: failed to decode parameters data; default values will be used instead"
+ "<<<< SDOFRendering V5 >>>> %s: Error: failed to get parameters data; default values will be used"
+ "<<<< SDOFRendering V5 >>>> %s: Face detection failed. Continuing without face term."
+ "<<<< SDOFRendering V5 >>>> %s: Faces detected: %d"
+ "<<<< SDOFRendering V5 >>>> %s: FocusRectangle: valid: %d, coords: %f, %f, %f, %f"
+ "<<<< SDOFRendering V5 >>>> %s: Foreground Blur resource allocation in SDOF bundle is %s"
+ "<<<< SDOFRendering V5 >>>> %s: Output blur map has foreground blur enabled = %s"
+ "<<<< SDOFRendering V5 >>>> %s: Rendering dict = %@"
+ "<<<< SDOFRendering V5 >>>> %s: SDOF Rendering Input Version: = %d"
+ "<<<< SDOFRendering V5 >>>> %s: SDOF Rendering Version Header: = %d"
+ "<<<< SDOFRendering V5 >>>> %s: SDOF tuning: %s = %d"
+ "<<<< SDOFRendering V5 >>>> %s: SDOF tuning: %s = %f"
+ "<<<< SDOFRendering V5 >>>> %s: SDOF tuning: %s = {Xb=%f, Xl=%f, Xn=%f, Xf=%f, Ybn=%f, Ybf=%f, Yln=%f, Ylf=%f"
+ "<<<< SDOFRendering V5 >>>> %s: SDOF tuning: %s is not present"
+ "<<<< SDOFRendering V5 >>>> %s: SDOFRendering Rendering set with options %@"
+ "<<<< SDOFRendering V5 >>>> %s: SDOFRendering: Did not get tuning parameters in options."
+ "<<<< SDOFRendering V5 >>>> %s: SDOFRendering: Found tuning parameters dictionary, initializing tuning parameters."
+ "<<<< SDOFRendering V5 >>>> %s: SDOFRendering: Tuning parameters after initialization is %p."
+ "<<<< SDOFRendering V5 >>>> %s: SDOFRenderingV5 computeBlurMapWithImage failed with err=%d"
+ "<<<< SDOFRendering V5 >>>> %s: SDOFRenderingV5 runSamplingWithImage failed with err=%d"
+ "<<<< SDOFRendering V5 >>>> %s: The orientation we got from metadata is not supported. Orientation: %d"
+ "<<<< SDOFRendering V5 >>>> %s: Time for face detection alone: %lld"
+ "<<<< SDOFRendering V5 >>>> %s: Total time in SDOFRenderingV5:encodeParametersForSampleBuffer: %lld ms"
+ "<<<< SDOFRendering V5 >>>> %s: Total time in computeBlurMapWithImage: %lld ms"
+ "<<<< SDOFRendering V5 >>>> %s: Total time in runSamplingWithImage: %lld ms"
+ "<<<< SDOFRendering V5 >>>> %s: Using provided metal command queue %p"
+ "<<<< SDOFRendering V5 >>>> %s: Warning: Unable to parse NMP parameters - are these expected for this camera?"
+ "<<<< SDOFRendering V5 >>>> %s: XXX HairNet dict = %@"
+ "<<<< SDOFRendering V5 >>>> %s: XXX Rendering dict = %@"
+ "<<<< SDOFRendering V5 >>>> %s: calculateXHLRBParamsForSampleBuffer failed with status %d, XHLRB will be disabled."
+ "<<<< SDOFRendering V5 >>>> %s: exposureLevel: %f"
+ "<<<< SDOFRendering V5 >>>> %s: focalLengthInPixels = %f"
+ "<<<< SDOFRendering V5 >>>> %s: focusDistanceRatio: %f"
+ "<<<< SDOFRendering V5 >>>> %s: inputAlphaMask image has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: inputAlphaMask image is not uint8, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: inputFaceAdjustedBlurMap has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: inputFaceAdjustedBlurMap image is not one or two components uint8, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: inputGainMap image has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: inputGainMap image is not uint8, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: inputImageFull has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: inputImageFull is not YUV420, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: inputPixelBuffer has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: inputPixelBuffer is not YUV420, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: inputSegmentationMask has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: inputSegmentationMask image is not uint8, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: inputSemanticSegmentationGlassesMask has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: inputSemanticSegmentationGlassesMask image is not uint8, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: inputSemanticSegmentationHairMask has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: inputSemanticSegmentationHairMask image is not uint8, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: inputShiftmap has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: inputShiftmap image is not float16 nor DisparityFloat16, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: parameterSetForMode: mode=%d not supported"
+ "<<<< SDOFRendering V5 >>>> %s: resultFaceAdjustedBlurMap has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: resultFaceAdjustedBlurMap image is not one or two components uint8, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: resultImage has wrong size, expected:%lux%lu Got:%lux%lu"
+ "<<<< SDOFRendering V5 >>>> %s: resultImage is not YUV420, Got:%@"
+ "<<<< SDOFRendering V5 >>>> %s: resulting additiveMaxBlur: %f"
+ "<<<< SDOFRendering V5 >>>> %s: resulting disparityScalingFactor: %f"
+ "<<<< SDOFRendering V5 >>>> %s: resulting hairAdditiveMaxBlur: %f"
+ "<<<< SDOFRendering V5 >>>> %s: resulting hairSubtractiveMaxBlur: %f"
+ "<<<< SDOFRendering V5 >>>> %s: resulting subtractiveMaxBlur: %f"
+ "<<<< SDOFRendering V5 >>>> %s: updateSegFusionParamsForSampleBuffer failed with status %d, will use bright light params."
+ "<<<< SDOFResources(V5) >>>>"
+ "<<<< SDOFResources(V5) >>>> %s: Couldn't allocate SDOFResources singleton"
+ "<<<< SDOFResources(V5) >>>> %s: Foreground blur enabled when creating resources = %s"
+ "<<<< SDOFResources(V5) >>>> %s: buffer1 old state = %d"
+ "<<<< SDOFResources(V5) >>>> %s: buffer2 old state = %d"
+ "<<<< SDOFResources(V5) >>>> %s: buffer3 old state = %d"
+ "<<<< SDOFResources(V5) >>>> %s: buffer4 old state = %d"
+ "<<<< SDOFResources(V5) >>>> %s: bufferLength = %lu"
+ "<<<< SDOFResources(V5) >>>> %s: referenceCount = %d"
+ "DISABLED"
+ "ENABLED"
+ "NO"
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
+ "_minMax0_kernel is NULL"
+ "_minMax1_kernel is NULL"
+ "_minMax2_kernel is NULL"
+ "_minMaxAtomic_buf is NULL"
+ "_minMaxResult_buf is NULL"
+ "_nClippedPixelsBuf is NULL"
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
+ "kCMBaseObjectError_ParamErr"
+ "landmarkToC0"
+ "maybeValueFloat"
+ "maybeValueInt"
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
+ "shiftMapTex has incorrect pixel format"
+ "simpleLensParams is NULL"
+ "tuningParameters is nil."
- "( kCVPixelFormatType_OneComponent16Half == CVPixelBufferGetPixelFormatType(inputShiftmap) ) || ( kCVPixelFormatType_DisparityFloat16 == CVPixelBufferGetPixelFormatType(inputShiftmap) )"
- "@\"FigM2MController\""
- "@28@0:8i16i20I24"
- "B60@0:8^{__CVBuffer=}16i24{CGRect={CGPoint=dd}{CGSize=dd}}28"
- "Could not allocate m2m controller."
- "FigUtlROIProcessor"
- "Rectangle size out of range"
- "SDOFRendering: shiftmap is not float16 nor DisparityFloat16"
- "T^{__CVBuffer=},R,N,V_pixelBuffer"
- "Ti,R,N,V_height"
- "Ti,R,N,V_width"
- "T{?=[3]},R,N,V_originalToRoiMatrix"
- "T{?=[3]},R,N,V_roiToOriginalMatrix"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_roiRectangle"
- "Unknown rotation value. This can never happen."
- "^{__CVBuffer=}"
- "^{__CVBuffer=}16@0:8"
- "_height"
- "_m2m"
- "_orientation"
- "_originalHeight"
- "_originalRectangle"
- "_originalToRoiMatrix"
- "_originalWidth"
- "_pixelBuffer"
- "_roiInPixels"
- "_roiInPixels.size.width <= _width && _roiInPixels.size.height <= _height"
- "_roiRectangle"
- "_roiToOriginalMatrix"
- "_width"
- "alpha-mask image has wrong size"
- "alpha-mask image is not uint8."
- "b"
- "blurmap image has wrong size"
- "blurmap image is not uint8."
- "e == noErr"
- "face adj blur map is not uint8"
- "face adjusted blurmap image has wrong size"
- "gain map image has wrong size"
- "gain map image is not uint8."
- "image is not full res."
- "initWithWidth:height:pixelFormat:"
- "input image is not YUV420"
- "input image is not YUV420."
- "input image is not full res."
- "m2m rotation has failed."
- "originalToRoi:"
- "originalToRoiMatrix"
- "originalToRoiPixels:"
- "pixelBuffer"
- "processImage:orientation:rect:"
- "result image is not YUV420."
- "result image is not full res."
- "roiPixelBuffer is NULL."
- "roiRectangle"
- "roiToOriginal:"
- "roiToOriginalMatrix"
- "roiToOriginalPixels:"
- "scale >= 0.25f"
- "segmentation mask has wrong size"
- "segmentation mask is not uint8"
- "semantic segmentation glasses mask has wrong size"
- "semantic segmentation glasses mask is not uint8"
- "semantic segmentation hair mask has wrong size"
- "semantic segmentation hair mask is not uint8"
- "shiftmap image has wrong size"
- "transform:srcRect:dst:dstRect:rotate:sync_m2m:"
- "utl_roi.m"
- "{?=\"columns\"[3]}"
- "{?=[3]}16@0:8"
- "{CGPoint=dd}32@0:8{CGPoint=dd}16"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "\xa1"

```
