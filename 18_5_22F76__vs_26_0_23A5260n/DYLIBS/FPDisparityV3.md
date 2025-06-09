## FPDisparityV3

> `/System/Library/VideoProcessors/FPDisparityV3.bundle/FPDisparityV3`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x1a928
-  __TEXT.__auth_stubs: 0x4b0
+650.0.0.122.4
+  __TEXT.__text: 0x1d82c
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_methlist: 0x1544
-  __TEXT.__const: 0xd10
-  __TEXT.__cstring: 0x24c6
-  __TEXT.__unwind_info: 0x430
+  __TEXT.__const: 0xd48
+  __TEXT.__cstring: 0x3d92
+  __TEXT.__oslogstring: 0xa40
+  __TEXT.__unwind_info: 0x4b0
   __TEXT.__objc_classname: 0x279
-  __TEXT.__objc_methname: 0x4a81
+  __TEXT.__objc_methname: 0x4a96
   __TEXT.__objc_methtype: 0xd93
-  __TEXT.__objc_stubs: 0x2960
-  __DATA_CONST.__got: 0xd8
+  __TEXT.__objc_stubs: 0x2980
+  __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0xe0
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec8
+  __DATA_CONST.__objc_selrefs: 0xed0
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x260
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0xec0
+  __AUTH_CONST.__auth_got: 0x288
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0xf00
   __AUTH_CONST.__objc_const: 0x2ed0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x34c
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x10
+  __DATA.__common: 0x30
+  __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE6114BF-8E42-3A50-8CC2-653F9DC88E82
-  Functions: 701
-  Symbols:   112
-  CStrings:  1440
+  UUID: 222A056D-62BA-3B65-9CF0-B57EFA2DCF47
+  Functions: 727
+  Symbols:   116
+  CStrings:  1620
 
Symbols:
+ _FigSignalErrorAt3
+ __os_log_impl
+ __os_log_send_and_compose_impl
+ _fig_log_call_emit_and_clean_up_after_send_and_compose
+ _fig_log_emitter_get_os_log_and_send_and_compose_flags_and_os_log_type
+ _fig_note_initialize_category_with_default_work_cf
+ _os_log_create
+ _os_log_type_enabled
- _FigSignalErrorAt
- _NSLog
- ___stack_chk_fail
- ___stack_chk_guard
CStrings:
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( -73465 )"
+ "(Fig)"
+ "-[FPDisparityEstimator CreateKernelWithConst:constants:]"
+ "-[FPDisparityEstimator _allocateFPCostWorkBuffer:]"
+ "-[FPDisparityEstimator _computeCost:texGreenPixels:texOutputResU:texOutputHesU:level:resolutionScale:]"
+ "-[FPDisparityEstimator _computeFocusPixelDisparityFromResolution:box_cstr_range:disparity_scaling_factor:]"
+ "-[FPDisparityEstimator _costNCC:dynCfg:texDisparityIn:texGreenPixelsIn:texFocusPixelsIn:texTcLrcOut:resolutionScale:level:]"
+ "-[FPDisparityEstimator _debugInterpolate:texTcLrcIn:dynCfg:debugBuf:]"
+ "-[FPDisparityEstimator _doLocalRegularizationWithCommandBuffer:in_tex:level:parameters:]"
+ "-[FPDisparityEstimator _filterHorz:texTcLrcIn:texTcLrcOut:dynCfg:]"
+ "-[FPDisparityEstimator _filterVert:texTcLrcIn:texTcLrcOut:dynCfg:]"
+ "-[FPDisparityEstimator _generateCorrectionMap]"
+ "-[FPDisparityEstimator _interpolateAndAccumulate:texTcLrcIn:dynCfg:]"
+ "-[FPDisparityEstimator _proximityOperator:dynCfg:texDisparityIn:texOutputResUOut:texOutputHesUOut:level:]"
+ "-[FPDisparityEstimator _setCorrectionMapCoefficients:]"
+ "-[FPDisparityEstimator _setupFPPipelines]"
+ "-[FPDisparityEstimator allocateResources:]"
+ "-[FPDisparityEstimator computeFilterCurve:p3:array:]"
+ "-[FigFocusPixelDisparityGenerator _allocateTextures]"
+ "-[FigFocusPixelDisparityGenerator _computeDisparityQuality:]"
+ "-[FigFocusPixelDisparityGenerator _downscale2X420fTBGRAEqualWithCommandBuffer:in_Ytex:in_UVtex:out_tex:cropRect:]"
+ "-[FigFocusPixelDisparityGenerator _extractFocusPixelMetadata]"
+ "-[FigFocusPixelDisparityGenerator _initShaders]"
+ "-[FigFocusPixelDisparityGenerator _populateImagePyramidFrom420fPixelBuffer:cropRect:]"
+ "-[FigFocusPixelDisparityGenerator _populateImagePyramidFrom:]"
+ "-[FigFocusPixelDisparityGenerator _populateRawGreenChannelPyramid]"
+ "-[FigFocusPixelDisparityGenerator getFPBuffersSizeFromOptions:]"
+ "-[FigFocusPixelDisparityGenerator getFrameSizesFromOptions:]"
+ "-[FigFocusPixelDisparityGenerator getPatternDetailsFrom:outTypeName:outCountX:outCountY:outStartX:outStartY:outStepX:outStepY:]"
+ "-[FigFocusPixelDisparityGenerator getSequenceDetailsFrom:withName:outCount:outStart:outStep:]"
+ "-[FigFocusPixelDisparityGenerator process]"
+ "-[FigFocusPixelDisparityGenerator readSizeFromDictionary:toWidth:toHeight:]"
+ "-[FigFocusPixelDisparityGenerator setOptions:]"
+ "-[FocusPixelDisparityDemosaic demosaicGreenOnly:fromL00h:validRect:waitForCompletion:]"
+ "-[FocusPixelDisparityTuningParameters readFPDisparity_v3_Config:]"
+ "-[FocusPixelDisparityTuningParameters setDefaultFPDisparity_v3_Parameters]"
+ "-[HBFGPU _doBuildErrorMapWithCommandBuffer:in_res_tex:out_tex:]"
+ "-[HBFGPU _doComputeResidualErrorOffsetWithCommandBuffer:in_res_tex:]"
+ "-[HBFGPU _doComputeResidualErrorWithCommandBuffer:in_I0_u32_tex:in_I1_tex:in_uv_tex:out_tex:disparity_axis:]"
+ "-[HBFGPU _doOcclusionHandlingWithCommandBuffer:in_uv_old_tex:in_uv_new_tex:in_I0_u32_tex:in_I1_tex:out_tex:disparity_axis:disparity_scaling_factor:]"
+ "-[HBFGPU doFilterWithCommandBuffer:in_I_tex:in_J_u32_tex:in_W_tex:out_tex:disparity_scaling_factor:]"
+ "-[PyrGPU _doRPDDownscale1WithCommandBuffer:in_tex:out_tex:scaling_factor:]"
+ "-[PyrGPU _downscale2XBelowWithCommandBuffer:in_tex:out_tex:scaling_factor:]"
+ "-[PyrGPU downscale2XEqualWithCommandBuffer:in_u32_alias_tex:out_u32_alias_tex:]"
+ "-[TVL1_v3 _doUpscaleDualWithCommandBuffer:in_tex:out_tex:]"
+ "-[TVL1_v3 _doUpscaleSingleWithCommandBuffer:in_tex:out_tex:coeff:]"
+ "-[TVL1_v3 allocateResources]"
+ "-[TVL1_v3 doInitPrimalDualWithCommandBuffer:disparity_value:idx_swap_uv:idx_swap_p:level:]"
+ "-[TVL1_v3 doLocalRegularizationWithCommandBuffer:in_tex:level:parameters:]"
+ "-[TVL1_v3 doSolveChambollePrimalDualWithCommandBuffer:idx_swap_uv_in_out:idx_swap_p_in_out:in_res_tes:in_hes_tes:out_uv_tex:level:iterations:box_cstr_range:disparity_scaling_factor:parameters:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/FPDisparity/V3/FPDDemosaic/FPDDemosaicV3.m %s: 'inputRaw' image not even-sized"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/FPDisparity/V3/FPDDemosaic/FPDDemosaicV3.m %s: Creating cmdBuf failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Portrait/FPDisparity/V3/FPDDemosaic/FPDDemosaicV3.m %s: Creating cmdEnc failed"
+ "<<<< FPDisparityEstimator (V3) >>>>"
+ "<<<< FPDisparityEstimator (V3) >>>> %s: Filter too long"
+ "<<<< FPDisparityEstimator (V3) >>>> %s: Filter too short"
+ "<<<< FPDisparityEstimator (V3) >>>> %s: Generated correction map : Will apply disparity correction"
+ "<<<< FPDisparityEstimator (V3) >>>> %s: No correction map will be used."
+ "<<<< FPDisparityEstimator (V3) >>>> %s: Unable to create ComputePipelineState for kernel %@, %@"
+ "<<<< FPDisparityEstimator (V3) >>>> %s: Unable to create kernel %@"
+ "<<<< FPDisparityEstimator (V3) >>>> %s: correctionBasisCoefficients[%d]  = %f "
+ "<<<< FocusPixelDisparity >>>>"
+ "<<<< FocusPixelDisparity >>>> %s: Back or front count is zero."
+ "<<<< FocusPixelDisparity >>>> %s: DisparityQuality is %s "
+ "<<<< FocusPixelDisparity >>>> %s: Failed to compute disparity quality. Assuming low"
+ "<<<< FocusPixelDisparity >>>> %s: FocalPlaneCharacterizationCoefficients[%d]  = %f"
+ "<<<< FocusPixelDisparity >>>> %s: FocusPixelDisparityV3 set with options %@"
+ "<<<< FocusPixelDisparity >>>> %s: FocusPixelDisparityV3: Did not get tuning parameters in options."
+ "<<<< FocusPixelDisparity >>>> %s: FocusPixelDisparityV3: Found tuning parameters and camera info dictionaries, initializing tuning parameters."
+ "<<<< FocusPixelDisparity >>>> %s: FocusPixelDisparityV3: No FocalPlaneCharacterizationCoefficients available in CameraInfoByPortType"
+ "<<<< FocusPixelDisparity >>>> %s: FocusPixelDisparityV3: Tuning parameters after initialization is %p."
+ "<<<< FocusPixelDisparity >>>> %s: Got personSegmentationConfidencePixelBuffer"
+ "<<<< FocusPixelDisparity >>>> %s: Got personSegmentationPixelBuffer"
+ "<<<< FocusPixelDisparity >>>> %s: Green Level %u : %u x %u"
+ "<<<< FocusPixelDisparity >>>> %s: Level %d : %f x %f"
+ "<<<< FocusPixelDisparity >>>> %s: Unknown value focusPixelDirection(%u)"
+ "<<<< FocusPixelDisparity >>>> %s: _extractFocusPixelMetadata failed"
+ "<<<< FocusPixelDisparity >>>> %s: cameraInfoByPortType %@"
+ "<<<< FocusPixelDisparity >>>> %s: tuningParameters %@"
+ "<<<< FocusPixelDisparity Tuning >>>>"
+ "<<<< FocusPixelDisparity Tuning >>>> %s: Level %u:%@ -> %d"
+ "<<<< FocusPixelDisparity Tuning >>>> %s: Level %u:%@ -> %f"
+ "<<<< FocusPixelDisparity Tuning >>>> %s: plist Parsing failed"
+ "<unknown>"
+ "Could not create DISPARITY_QUALITY pipeline"
+ "Could not create DOWNSCALE_2X_402F_TO_BGRA pipeline"
+ "Creating cmdEnc failed"
+ "Disparity tuning:Cannot find the key '%@' for the level %d in the plist."
+ "Disparity tuning:Cannot find the key '%@' in the plist."
+ "FPCostParameters is nil"
+ "FPDisparityEstimator_trace"
+ "FPPostprocessingParameters is nil"
+ "FPPreprocessingParameters is nil"
+ "Failed to get Count from Pattern"
+ "Failed to get Pattern dict"
+ "Failed to get PixelType from Pattern"
+ "Failed to get Size Height"
+ "Failed to get Size Width"
+ "Failed to get Start from Pattern"
+ "Failed to get Step from Pattern"
+ "Failed to get sequance entry from Pattern"
+ "Failed to parse Pattern dict"
+ "FigFocusPixelDisparityFocusPixelTypeNotSupported"
+ "FigFocusPixelDisparityModuleConfigInvalid"
+ "Focus pixel type not supported"
+ "FocusPixels missing Patterns"
+ "H buffers sizes do not match"
+ "ModuleConfig has more focus pixel patterns than expected"
+ "Unable to create textureDesc"
+ "V buffers sizes do not match"
+ "_FPDisparityEstimator_Config is nil"
+ "_bufTcLrc1 is nil"
+ "_bufTcLrc2 is nil"
+ "_correctionMapGenerationPipelineState is nil"
+ "_costNCCPipelineState is nil"
+ "_costsBuffer is nil"
+ "_disparityCorrectionTex is nil"
+ "_filterHorzPipelineState is nil"
+ "_filterVertPipelineState is nil"
+ "_focusPixelViews[0] is nil"
+ "_focusPixelViews[1] is nil"
+ "_focusPixelViews[2] is nil"
+ "_focusPixelViews[3] is nil"
+ "_gChannelRescale is nil"
+ "_gChannelTexture is nil"
+ "_greenChannelPyramid is nil"
+ "_greenChannelPyramid[0] is nil"
+ "_interpolateAndAccumPipelineState is nil"
+ "_interpolateAndSetPipelineState is nil"
+ "_proximityOperatorPipelineState is nil"
+ "_pyramidReference is nil."
+ "_readKeyFloat"
+ "_readKeyInteger"
+ "_readKeyUint32"
+ "_readKeyValue"
+ "_regularizationPipelineState is nil"
+ "basisImagesTexture is nil"
+ "cmdBuf is NULL"
+ "cmdEnc is NULL"
+ "com.apple.coremedia"
+ "commandBuffer is NULL"
+ "costParameters is nil"
+ "defaultCostLevelParameters is nil"
+ "defaultFPCostParameters is nil"
+ "defaultHBFParameters is nil"
+ "defaultPostprocessingParameters is nil"
+ "defaultPreprocessingParameters is nil"
+ "defaultRegularizationParameters is nil"
+ "defaultsolverParameters is nil"
+ "dict is nil"
+ "disparitySize is NULL"
+ "fpd_trace"
+ "fpd_tuning_trace"
+ "greenSizeDict is NULL"
+ "hbfParameters is nil"
+ "high"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "legacyLog"
+ "levelParameters is nil"
+ "localizedDescription"
+ "low"
+ "mtlCommandBuffer is nil"
+ "pipelineDescriptor is nil"
+ "pipelineDescriptor.fragmentFunction is nil"
+ "pipelineDescriptor.vertexFunction is nil"
+ "pyramidLevelsParams is nil"
+ "rawSizeDict is NULL"
+ "regParameters is nil"
+ "renderCommand is nil"
+ "renderPassDescriptor is nil"
+ "sizesDict is NULL"
+ "solverParameters is nil"
+ "texTcLrc1 is nil"
+ "texTcLrc2 is nil"
+ "texTcLrc3 is nil"

```
