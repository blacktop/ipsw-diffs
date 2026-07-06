## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-  __TEXT.__text: 0x2d6e08
-  __TEXT.__objc_methlist: 0x128e8
-  __TEXT.__const: 0x1031a8
-  __TEXT.__cstring: 0x5d201
+  __TEXT.__text: 0x2e1444
+  __TEXT.__objc_methlist: 0x12e78
+  __TEXT.__const: 0x1031d8
+  __TEXT.__cstring: 0x5ec62
   __TEXT.__gcc_except_tab: 0x1cd8
-  __TEXT.__oslogstring: 0x4424f
+  __TEXT.__oslogstring: 0x442ad
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x55e0
+  __TEXT.__unwind_info: 0x5708
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x14e8
-  __DATA_CONST.__objc_classlist: 0xe00
+  __DATA_CONST.__const: 0x14f0
+  __DATA_CONST.__objc_classlist: 0xe18
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c20
+  __DATA_CONST.__objc_selrefs: 0x6f00
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xad0
+  __DATA_CONST.__objc_superrefs: 0xae8
   __DATA_CONST.__objc_arraydata: 0xf08
-  __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x980
-  __AUTH_CONST.__cfstring: 0x13a40
-  __AUTH_CONST.__objc_const: 0x3a068
+  __DATA_CONST.__got: 0xf00
+  __AUTH_CONST.__const: 0x9a0
+  __AUTH_CONST.__cfstring: 0x148c0
+  __AUTH_CONST.__objc_const: 0x3b168
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_arrayobj: 0xc60
+  __AUTH_CONST.__objc_arrayobj: 0xc30
   __AUTH_CONST.__objc_intobj: 0xa08
   __AUTH_CONST.__objc_floatobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x500
-  __AUTH_CONST.__auth_got: 0x868
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x3db4
+  __AUTH_CONST.__auth_got: 0x860
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x3f38
   __DATA.__data: 0xc68
   __DATA.__common: 0x50
   __DATA.__bss: 0x28
-  __DATA_DIRTY.__objc_data: 0x81b0
+  __DATA_DIRTY.__objc_data: 0x83e0
   __DATA_DIRTY.__bss: 0x178
   __DATA_DIRTY.__common: 0x128
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 15301
-  Symbols:   45849
-  CStrings:  16496
+  Functions: 15543
+  Symbols:   46543
+  CStrings:  16834
 
Sections:
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[CMIRawNightModeLKTFlow _computeScalingFactor:dst_tex:scale_xy_inv:coeff:]
+ -[CMIRawNightModeLKTBlending .cxx_destruct]
+ -[CMIRawNightModeLKTBlending _encodeApplyLTMLumaEdgeGuideOnCmdBuffer:inLuma:outLuma:ltc:gtcFinal:ltmROI:ccm:scaleInput:ltmHardGain:]
+ -[CMIRawNightModeLKTBlending _encodeBlendingDecisionBilateralOnCmdBuffer:nccG:nccD:guide:out:denseThreshold:smoothstepLow:smoothstepHigh:sigmaSpatial:sigmaRange:halfWindow:]
+ -[CMIRawNightModeLKTBlending _encodeBlendingDecisionOnCmdBuffer:nccG:nccD:out:denseThreshold:smoothstepLow:smoothstepHigh:]
+ -[CMIRawNightModeLKTBlending _encodeBoxDownscaleOnCmdBuffer:inTex:outTex:]
+ -[CMIRawNightModeLKTBlending _encodeFlowToResidualShiftOnCmdBuffer:inFlow:outShift:homography:fullSize:]
+ -[CMIRawNightModeLKTBlending _encodePatchNCCOnCmdBuffer:texA:texB:outNCC:]
+ -[CMIRawNightModeLKTBlending _encodePatchSigmaOnCmdBuffer:texIn:outSigma:]
+ -[CMIRawNightModeLKTBlending _encodeWarpByFlowOnCmdBuffer:inLuma:inFlow:outLuma:]
+ -[CMIRawNightModeLKTBlending _encodeWarpByHomographyOnCmdBuffer:inLuma:hom:outLuma:]
+ -[CMIRawNightModeLKTBlending _newScratchTextureWithLabel:width:height:pixelFormat:]
+ -[CMIRawNightModeLKTBlending _setupPipelines]
+ -[CMIRawNightModeLKTBlending encodeGammaPrepassOnCmdBuffer:inLuma:outLuma:gamma:]
+ -[CMIRawNightModeLKTBlending encodeGammaPrepassRGBOnCmdBuffer:inRGB:outRGB:gamma:]
+ -[CMIRawNightModeLKTBlending encodeLCBDemosaicYRGBOnCmdBuffer:inBayer:firstPixel:outYRGB:]
+ -[CMIRawNightModeLKTBlending encodeRGBToYUVAOnCmdBuffer:inRGB:outYUVA:]
+ -[CMIRawNightModeLKTBlending encodeRevertLSCOnCmdBuffer:inLuma:lscGains:lscParams:outLuma:]
+ -[CMIRawNightModeLKTBlending encodeRevertLSCRGBOnCmdBuffer:inRGB:lscGains:lscParams:outRGB:]
+ -[CMIRawNightModeLKTBlending encodeYRGBToRGBAOnCmdBuffer:inYRGB:outRGBA:gain:]
+ -[CMIRawNightModeLKTBlending initWithMetalContext:]
+ -[CMIRawNightModeLKTBlending runFallbackBlendingOnCommandBuffer:shiftMap:blendingWeight:]
+ -[CMIRawNightModeLKTBlending runWithCommandBuffer:refLuma:nonRefLuma:lktFlow:homography:fullSize:nccBand:nccDenseThreshold:smoothstepLow:smoothstepHigh:filterType:sigmaSpatial:sigmaRange:toneMappingCurves:ltmROI:ccm:scaleInput:ltmHardGain:shiftMap:blendingWeight:]
+ -[CMIRawNightModeLKTFlow .cxx_destruct]
+ -[CMIRawNightModeLKTFlow _allocateGuidePyramidIfNeeded]
+ -[CMIRawNightModeLKTFlow _allocateTransientStorage]
+ -[CMIRawNightModeLKTFlow _computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:]
+ -[CMIRawNightModeLKTFlow _computeFeaturesWithCommandBuffer:in_tex:out_tex:]
+ -[CMIRawNightModeLKTFlow _computeOpticalFlowBidirectional]
+ -[CMIRawNightModeLKTFlow _createGuidePyramidWithCommandBuffer:in_tex:J_idx:]
+ -[CMIRawNightModeLKTFlow _createImagePyramidWithCommandBuffer:in_tex:I_idx:]
+ -[CMIRawNightModeLKTFlow _doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:]
+ -[CMIRawNightModeLKTFlow _downscale2XWithCommandBuffer:in_tex:out_tex:]
+ -[CMIRawNightModeLKTFlow _enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:]
+ -[CMIRawNightModeLKTFlow _enqueueFlowPostFilterWithCommandBuffer:in_flow:in_conf:in_guide:out_flow:]
+ -[CMIRawNightModeLKTFlow _enqueueFlowPostFilterYUVWithCommandBuffer:in_flow:in_conf:in_guide:out_flow:]
+ -[CMIRawNightModeLKTFlow _newAllocatorTextureWithLabel:width:height:pixelFormat:]
+ -[CMIRawNightModeLKTFlow _releaseGuidePyramid]
+ -[CMIRawNightModeLKTFlow _releaseInternalScratches]
+ -[CMIRawNightModeLKTFlow _releaseUserRefOutputs]
+ -[CMIRawNightModeLKTFlow _resolveSizesFromInput:height:]
+ -[CMIRawNightModeLKTFlow _setDefaultParameters]
+ -[CMIRawNightModeLKTFlow _setupPipelines]
+ -[CMIRawNightModeLKTFlow _zeroFlowWithCommandBuffer:uv_tex:]
+ -[CMIRawNightModeLKTFlow aux_size]
+ -[CMIRawNightModeLKTFlow conf_bwd]
+ -[CMIRawNightModeLKTFlow conf_fwd]
+ -[CMIRawNightModeLKTFlow dealloc]
+ -[CMIRawNightModeLKTFlow estimateFlowFromReference:target:]
+ -[CMIRawNightModeLKTFlow estimateFlowFromReference:target:refGuide:targetGuide:]
+ -[CMIRawNightModeLKTFlow flowPostFilterEnabled]
+ -[CMIRawNightModeLKTFlow flowPostFilterSigmaChroma]
+ -[CMIRawNightModeLKTFlow flowPostFilterSigmaColor]
+ -[CMIRawNightModeLKTFlow flowPostFilterSigmaConf]
+ -[CMIRawNightModeLKTFlow flowPostFilterYUVEnabled]
+ -[CMIRawNightModeLKTFlow initWithMetalContext:]
+ -[CMIRawNightModeLKTFlow lastScale]
+ -[CMIRawNightModeLKTFlow nscales]
+ -[CMIRawNightModeLKTFlow nwarpings]
+ -[CMIRawNightModeLKTFlow ref_size]
+ -[CMIRawNightModeLKTFlow reset]
+ -[CMIRawNightModeLKTFlow setFlowPostFilterEnabled:]
+ -[CMIRawNightModeLKTFlow setFlowPostFilterSigmaChroma:]
+ -[CMIRawNightModeLKTFlow setFlowPostFilterSigmaColor:]
+ -[CMIRawNightModeLKTFlow setFlowPostFilterSigmaConf:]
+ -[CMIRawNightModeLKTFlow setFlowPostFilterYUVEnabled:]
+ -[CMIRawNightModeLKTFlow setLastScale:]
+ -[CMIRawNightModeLKTFlow setNscales:]
+ -[CMIRawNightModeLKTFlow setNwarpings:]
+ -[CMIRawNightModeLKTFlow uv_bwd]
+ -[CMIRawNightModeLKTFlow uv_fwd]
+ -[CMIRawNightModeLKTFlow waitUntilCompleted]
+ -[CMIRawNightModeLKTRegistrationTuningParams applyLTMToEdgeGuide]
+ -[CMIRawNightModeLKTRegistrationTuningParams bidirectionalError]
+ -[CMIRawNightModeLKTRegistrationTuningParams blendingDownsampleGamma]
+ -[CMIRawNightModeLKTRegistrationTuningParams confidenceMinimum]
+ -[CMIRawNightModeLKTRegistrationTuningParams confidenceRadialWeight]
+ -[CMIRawNightModeLKTRegistrationTuningParams enabled]
+ -[CMIRawNightModeLKTRegistrationTuningParams filterType]
+ -[CMIRawNightModeLKTRegistrationTuningParams flowPostFilterEnabled]
+ -[CMIRawNightModeLKTRegistrationTuningParams flowPostFilterSigmaChroma]
+ -[CMIRawNightModeLKTRegistrationTuningParams flowPostFilterSigmaColor]
+ -[CMIRawNightModeLKTRegistrationTuningParams flowPostFilterSigmaConf]
+ -[CMIRawNightModeLKTRegistrationTuningParams flowPostFilterUseLCBDemosaic]
+ -[CMIRawNightModeLKTRegistrationTuningParams flowPostFilterYUVEnabled]
+ -[CMIRawNightModeLKTRegistrationTuningParams lastScale]
+ -[CMIRawNightModeLKTRegistrationTuningParams lumaGammaEnabled]
+ -[CMIRawNightModeLKTRegistrationTuningParams lumaGamma]
+ -[CMIRawNightModeLKTRegistrationTuningParams nccBand]
+ -[CMIRawNightModeLKTRegistrationTuningParams nccDenseThreshold]
+ -[CMIRawNightModeLKTRegistrationTuningParams nccPatchSize]
+ -[CMIRawNightModeLKTRegistrationTuningParams nscales]
+ -[CMIRawNightModeLKTRegistrationTuningParams nwarpings]
+ -[CMIRawNightModeLKTRegistrationTuningParams readPlist:]
+ -[CMIRawNightModeLKTRegistrationTuningParams revertLSC]
+ -[CMIRawNightModeLKTRegistrationTuningParams sigmaRange]
+ -[CMIRawNightModeLKTRegistrationTuningParams sigmaSpatial]
+ -[CMIRawNightModeLKTRegistrationTuningParams smoothstepHigh]
+ -[CMIRawNightModeLKTRegistrationTuningParams smoothstepLow]
+ -[CMIRawNightModeRegistrationStage _processReferenceForHybridLKT:gain:]
+ -[CMIRawNightModeRegistrationStage lktTuningParams]
+ -[CMIRawNightModeRegistrationStage processRegWarpLKTNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]
+ -[CMIRawNightModeRegistrationStage setLktTuningParams:]
+ -[H13FastRawScaleStage _getUseNominalCCMFromPreviewEnabledForFrame:enabled:]
+ -[LearnedDemosaicNetworkShared blackSpotMaskEnabled]
+ -[LearnedDemosaicNetworkShared correctDefectPixels]
+ -[LearnedDemosaicNetworkShared setBlackSpotMaskEnabled:]
+ -[LearnedDemosaicNetworkShared setCorrectDefectPixels:]
+ -[LearnedFusionNetworkStage lfType]
+ -[LearnedFusionNetworkStage setLfType:]
+ -[LearnedFusionNetworkStageShared setTileOverlap:]
+ -[LearnedFusionNetworkStageShared tileOverlap]
+ -[RawNightModeInputFrame baseTex]
+ -[RawNightModeInputFrame frameID]
+ -[RawNightModeInputFrame lscGainMapTexture]
+ -[RawNightModeInputFrame setLscGainMapTexture:]
+ -[RawNightModeProcessor extractLSCMetadataFromFrame:]
+ -[RawProcInputFrame setLscGainMapTexture:]
+ GCC_except_table24
+ _NRFLFTypePlistKey
+ _OBJC_CLASS_$_CMIRawNightModeLKTBlending
+ _OBJC_CLASS_$_CMIRawNightModeLKTFlow
+ _OBJC_CLASS_$_CMIRawNightModeLKTRegistrationTuningParams
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._applyLtmLumaEdgeGuidePipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._blendingDecisionBilateralPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._blendingDecisionPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._boxDownscalePipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._flowToShiftPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._gammaPrepassPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._gammaPrepassRGBPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._lcbDemosaicYRGBPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._metal
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._patchNCCPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._patchSigmaPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._revertLSCPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._revertLSCRGBPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._rgbToYUVAPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._warpByFlowPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._warpByHomographyPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._yrgbToRGBAPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTBlending._zeroTexturePipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._Adiagb_buf
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._C0_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._C1_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._G0_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._G1_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._I_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._Ixy_buf
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._J_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._aux_pyr_size
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._aux_size
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._commandQueue
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._conf_bwd_final_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._conf_bwd_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._conf_fwd_final_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._conf_fwd_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._downscale2xPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._featuresDerivativesPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._featuresPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._flowConsistencyPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._flowPostFilterEnabled
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._flowPostFilterPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._flowPostFilterSigmaChroma
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._flowPostFilterSigmaColor
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._flowPostFilterSigmaConf
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._flowPostFilterYUVEnabled
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._flowPostFilterYUVPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._idt_buf
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._lastScale
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._maxThreadExecutionWidth
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._memoryAllocated
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._mtlContext
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._nscales
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._nwarpings
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._ref_pyr_size
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._ref_size
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._solverBoxXAndAxbPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._solverBoxYPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._solverPrepareMatricesPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._uv_bwd_final_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._uv_bwd_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._uv_fwd_final_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._uv_fwd_tex
+ _OBJC_IVAR_$_CMIRawNightModeLKTFlow._zeroFlowPipeline
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._applyLTMToEdgeGuide
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._bidirectionalError
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._blendingDownsampleGamma
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._confidenceMinimum
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._confidenceRadialWeight
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._enabled
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._filterType
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._flowPostFilterEnabled
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._flowPostFilterSigmaChroma
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._flowPostFilterSigmaColor
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._flowPostFilterSigmaConf
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._flowPostFilterUseLCBDemosaic
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._flowPostFilterYUVEnabled
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._lastScale
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._lumaGamma
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._lumaGammaEnabled
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._nccBand
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._nccDenseThreshold
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._nccPatchSize
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._nscales
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._nwarpings
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._revertLSC
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._sigmaRange
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._sigmaSpatial
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._smoothstepHigh
+ _OBJC_IVAR_$_CMIRawNightModeLKTRegistrationTuningParams._smoothstepLow
+ _OBJC_IVAR_$_CMIRawNightModeRegistrationStage._gammaReferenceLumaTex
+ _OBJC_IVAR_$_CMIRawNightModeRegistrationStage._lkt
+ _OBJC_IVAR_$_CMIRawNightModeRegistrationStage._lktBlending
+ _OBJC_IVAR_$_CMIRawNightModeRegistrationStage._lktLSCParams
+ _OBJC_IVAR_$_CMIRawNightModeRegistrationStage._lktLSCParamsValid
+ _OBJC_IVAR_$_CMIRawNightModeRegistrationStage._lktTuningParams
+ _OBJC_IVAR_$_CMIRawNightModeRegistrationStage._lscRevertedReferenceLumaTex
+ _OBJC_IVAR_$_CMIRawNightModeRegistrationStage._referenceYUVATex
+ _OBJC_IVAR_$_LearnedDemosaicNetworkShared._blackSpotMaskEnabled
+ _OBJC_IVAR_$_LearnedDemosaicNetworkShared._correctDefectPixels
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._supportsBlackSpotMask
+ _OBJC_IVAR_$_LearnedFusionNetworkStage._lfType
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._tileOverlap
+ _OBJC_IVAR_$_RawNightModeProcessor._lktTuningParams
+ _OBJC_METACLASS_$_CMIRawNightModeLKTBlending
+ _OBJC_METACLASS_$_CMIRawNightModeLKTFlow
+ _OBJC_METACLASS_$_CMIRawNightModeLKTRegistrationTuningParams
+ __OBJC_$_CLASS_METHODS_CMIRawNightModeLKTFlow
+ __OBJC_$_INSTANCE_METHODS_CMIRawNightModeLKTBlending
+ __OBJC_$_INSTANCE_METHODS_CMIRawNightModeLKTFlow
+ __OBJC_$_INSTANCE_METHODS_CMIRawNightModeLKTRegistrationTuningParams
+ __OBJC_$_INSTANCE_VARIABLES_CMIRawNightModeLKTBlending
+ __OBJC_$_INSTANCE_VARIABLES_CMIRawNightModeLKTFlow
+ __OBJC_$_INSTANCE_VARIABLES_CMIRawNightModeLKTRegistrationTuningParams
+ __OBJC_$_PROP_LIST_CMIRawNightModeLKTFlow
+ __OBJC_$_PROP_LIST_CMIRawNightModeLKTRegistrationTuningParams
+ __OBJC_CLASS_RO_$_CMIRawNightModeLKTBlending
+ __OBJC_CLASS_RO_$_CMIRawNightModeLKTFlow
+ __OBJC_CLASS_RO_$_CMIRawNightModeLKTRegistrationTuningParams
+ __OBJC_METACLASS_RO_$_CMIRawNightModeLKTBlending
+ __OBJC_METACLASS_RO_$_CMIRawNightModeLKTFlow
+ __OBJC_METACLASS_RO_$_CMIRawNightModeLKTRegistrationTuningParams
+ ___114-[CMIRawNightModeRegistrationStage processRegWarpLKTNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke
+ _kNRF_LFType_LF12
+ _objc_msgSend$_allocateGuidePyramidIfNeeded
+ _objc_msgSend$_allocateTransientStorage
+ _objc_msgSend$_computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:
+ _objc_msgSend$_computeFeaturesWithCommandBuffer:in_tex:out_tex:
+ _objc_msgSend$_computeOpticalFlowBidirectional
+ _objc_msgSend$_computeScalingFactor:dst_tex:scale_xy_inv:coeff:
+ _objc_msgSend$_createGuidePyramidWithCommandBuffer:in_tex:J_idx:
+ _objc_msgSend$_createImagePyramidWithCommandBuffer:in_tex:I_idx:
+ _objc_msgSend$_doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:
+ _objc_msgSend$_downscale2XWithCommandBuffer:in_tex:out_tex:
+ _objc_msgSend$_encodeApplyLTMLumaEdgeGuideOnCmdBuffer:inLuma:outLuma:ltc:gtcFinal:ltmROI:ccm:scaleInput:ltmHardGain:
+ _objc_msgSend$_encodeBlendingDecisionBilateralOnCmdBuffer:nccG:nccD:guide:out:denseThreshold:smoothstepLow:smoothstepHigh:sigmaSpatial:sigmaRange:halfWindow:
+ _objc_msgSend$_encodeBlendingDecisionOnCmdBuffer:nccG:nccD:out:denseThreshold:smoothstepLow:smoothstepHigh:
+ _objc_msgSend$_encodeBoxDownscaleOnCmdBuffer:inTex:outTex:
+ _objc_msgSend$_encodeFlowToResidualShiftOnCmdBuffer:inFlow:outShift:homography:fullSize:
+ _objc_msgSend$_encodePatchNCCOnCmdBuffer:texA:texB:outNCC:
+ _objc_msgSend$_encodeWarpByFlowOnCmdBuffer:inLuma:inFlow:outLuma:
+ _objc_msgSend$_encodeWarpByHomographyOnCmdBuffer:inLuma:hom:outLuma:
+ _objc_msgSend$_enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:
+ _objc_msgSend$_enqueueFlowPostFilterWithCommandBuffer:in_flow:in_conf:in_guide:out_flow:
+ _objc_msgSend$_enqueueFlowPostFilterYUVWithCommandBuffer:in_flow:in_conf:in_guide:out_flow:
+ _objc_msgSend$_getUseNominalCCMFromPreviewEnabledForFrame:enabled:
+ _objc_msgSend$_newAllocatorTextureWithLabel:width:height:pixelFormat:
+ _objc_msgSend$_newScratchTextureWithLabel:width:height:pixelFormat:
+ _objc_msgSend$_processReferenceForHybridLKT:gain:
+ _objc_msgSend$_releaseGuidePyramid
+ _objc_msgSend$_releaseInternalScratches
+ _objc_msgSend$_releaseUserRefOutputs
+ _objc_msgSend$_resolveSizesFromInput:height:
+ _objc_msgSend$_setDefaultParameters
+ _objc_msgSend$_setupPipelines
+ _objc_msgSend$_zeroFlowWithCommandBuffer:uv_tex:
+ _objc_msgSend$applyLTMToEdgeGuide
+ _objc_msgSend$blackSpotMaskEnabled
+ _objc_msgSend$correctDefectPixels
+ _objc_msgSend$encodeGammaPrepassOnCmdBuffer:inLuma:outLuma:gamma:
+ _objc_msgSend$encodeGammaPrepassRGBOnCmdBuffer:inRGB:outRGB:gamma:
+ _objc_msgSend$encodeLCBDemosaicYRGBOnCmdBuffer:inBayer:firstPixel:outYRGB:
+ _objc_msgSend$encodeRGBToYUVAOnCmdBuffer:inRGB:outYUVA:
+ _objc_msgSend$encodeRevertLSCOnCmdBuffer:inLuma:lscGains:lscParams:outLuma:
+ _objc_msgSend$encodeRevertLSCRGBOnCmdBuffer:inRGB:lscGains:lscParams:outRGB:
+ _objc_msgSend$encodeYRGBToRGBAOnCmdBuffer:inYRGB:outRGBA:gain:
+ _objc_msgSend$estimateFlowFromReference:target:
+ _objc_msgSend$estimateFlowFromReference:target:refGuide:targetGuide:
+ _objc_msgSend$extractLSCMetadataFromFrame:
+ _objc_msgSend$filterType
+ _objc_msgSend$flowPostFilterEnabled
+ _objc_msgSend$flowPostFilterSigmaChroma
+ _objc_msgSend$flowPostFilterSigmaColor
+ _objc_msgSend$flowPostFilterSigmaConf
+ _objc_msgSend$flowPostFilterUseLCBDemosaic
+ _objc_msgSend$flowPostFilterYUVEnabled
+ _objc_msgSend$lastPathComponent
+ _objc_msgSend$lastScale
+ _objc_msgSend$lumaGamma
+ _objc_msgSend$lumaGammaEnabled
+ _objc_msgSend$nccBand
+ _objc_msgSend$nccDenseThreshold
+ _objc_msgSend$nscales
+ _objc_msgSend$nwarpings
+ _objc_msgSend$processRegWarpLKTNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:
+ _objc_msgSend$revertLSC
+ _objc_msgSend$runFallbackBlendingOnCommandBuffer:shiftMap:blendingWeight:
+ _objc_msgSend$runWithCommandBuffer:refLuma:nonRefLuma:lktFlow:homography:fullSize:nccBand:nccDenseThreshold:smoothstepLow:smoothstepHigh:filterType:sigmaSpatial:sigmaRange:toneMappingCurves:ltmROI:ccm:scaleInput:ltmHardGain:shiftMap:blendingWeight:
+ _objc_msgSend$scanInteger:
+ _objc_msgSend$scanString:intoString:
+ _objc_msgSend$setBlackSpotMaskEnabled:
+ _objc_msgSend$setCorrectDefectPixels:
+ _objc_msgSend$setFlowPostFilterEnabled:
+ _objc_msgSend$setFlowPostFilterSigmaChroma:
+ _objc_msgSend$setFlowPostFilterSigmaColor:
+ _objc_msgSend$setFlowPostFilterSigmaConf:
+ _objc_msgSend$setFlowPostFilterYUVEnabled:
+ _objc_msgSend$setLastScale:
+ _objc_msgSend$setLfType:
+ _objc_msgSend$setLktTuningParams:
+ _objc_msgSend$setNscales:
+ _objc_msgSend$setNwarpings:
+ _objc_msgSend$sigmaRange
+ _objc_msgSend$sigmaSpatial
+ _objc_msgSend$smoothstepHigh
+ _objc_msgSend$smoothstepLow
+ _objc_msgSend$uv_fwd
- -[LearnedDemosaicNetworkShared recoveryYUVImage]
- -[LearnedDemosaicNetworkShared setRecoveryYUVImage:]
- -[LearnedDemosaicNetworkStage defectCorrectionEITRatio]
- -[LearnedDemosaicNetworkStage recoveryYUVImage]
- -[LearnedDemosaicNetworkStage setDefectCorrectionEITRatio:]
- -[LearnedDemosaicNetworkStage setRecoveryYUVImage:]
- -[RawNightModeProcessor extractLSCMetadataFromReferenceFrame:]
- GCC_except_table23
- _OBJC_IVAR_$_LearnedDemosaicNetworkShared._recoveryYUVImage
- _OBJC_IVAR_$_LearnedDemosaicNetworkStage._defectCorrectionEITRatio
- _OBJC_IVAR_$_LearnedDemosaicNetworkStage._recoveryYUVImage
- _OBJC_IVAR_$_LearnedFusionProcessor._proxySyntheticReferenceTextureYUV
- _kFigCaptureSampleBufferAttachmentKey_SyntheticReferencePixelBuffer
- _objc_msgSend$defectCorrectionEITRatio
- _objc_msgSend$extractLSCMetadataFromReferenceFrame:
- _objc_msgSend$recoveryYUVImage
- _objc_msgSend$setDefectCorrectionEITRatio:
- _objc_msgSend$setRecoveryYUVImage:
- _objc_release_x11
CStrings:
+ "(dst_tex.width == src_tex.width) && (dst_tex.height == src_tex.height)"
+ "+[CMIRawNightModeLKTFlow _computeScalingFactor:dst_tex:scale_xy_inv:coeff:]"
+ "-[CMIRawNightModeLKTFlow _computeFeaturesDerivativesWithCommandBuffer:in_tex:out_tex:]"
+ "-[CMIRawNightModeLKTFlow _computeFeaturesWithCommandBuffer:in_tex:out_tex:]"
+ "-[CMIRawNightModeLKTFlow _doSolverWithCommandBuffer:scale:in_uv_tex:in_G0_tex:in_G1_tex:in_C0_tex:in_C1_tex:out_uv_tex:out_w_tex:]"
+ "-[CMIRawNightModeLKTFlow _downscale2XWithCommandBuffer:in_tex:out_tex:]"
+ "-[CMIRawNightModeLKTFlow _enqueueFlowConsistencyWithCommandBuffer:in_uv0_tex:in_uv1_tex:out_uv_tex:]"
+ "-[CMIRawNightModeLKTFlow _enqueueFlowPostFilterWithCommandBuffer:in_flow:in_conf:in_guide:out_flow:]"
+ "-[CMIRawNightModeLKTFlow _enqueueFlowPostFilterYUVWithCommandBuffer:in_flow:in_conf:in_guide:out_flow:]"
+ "-[CMIRawNightModeLKTFlow _zeroFlowWithCommandBuffer:uv_tex:]"
+ "-[CMIRawNightModeLKTRegistrationTuningParams readPlist:]"
+ "-[CMIRawNightModeRegistrationStage _processReferenceForHybridLKT:gain:]"
+ "-[CMIRawNightModeRegistrationStage processRegWarpLKTNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]"
+ "-[H13FastRawScaleStage _getUseNominalCCMFromPreviewEnabledForFrame:enabled:]"
+ "-[RawNightModeProcessor extractLSCMetadataFromFrame:]"
+ "0x0905"
+ "0x0954"
+ "<<<< LearnedDemosaicNetworkStage >>>> %s: LearnedDemosaic supportsBlackSpotMask = %d (path: %@)"
+ "<<<< LearnedDemosaicNetworkStage >>>> %s: _shared.inputRawTexture nil"
+ "<<<< LearnedFusionNetworkStage >>>> %s: tileCount: {%d, %d}, tileOverlap: %d"
+ "<<<< LearnedFusionProcessor >>>> %s: defect correction requested for non-quadra frame (quadraBinningFactor=%d) — bilinear-from-quadra kernel has no bayer counterpart"
+ "<<<< LearnedFusionProcessor >>>> %s: demosaic frame %d (%s), label=%s, correctDefectPixels=%d"
+ "<<<< RawDFProcessor >>>> %s: GrayGhost has been detected; bailing.."
+ "<<<< RawDFProcessor >>>> %s: LearnedHRNR Proxy: successfully ran detectors"
+ "<<<< RawNightMode >>>> %s: HybridLKT global registration completed for inputFrame %@, hasValidRegistration: %d"
+ "<<<< RawNightMode >>>> %s: processNonReferenceTexture failed (HybridLKT)"
+ "<<<< SoftISP >>>> %s: Updating metadata for crop: source dims:%@, rect:%@ -> dest dims:%@, rect:%@, spatialMetadataRequiresUpdate:%d"
+ "<<<< SoftISP >>>> %s: useNominalCCMFromPreview is %@"
+ "ApplyLTMToEdgeGuide"
+ "BidirectionalError"
+ "BlendingDownsampleGamma"
+ "CMIRawNIghtModeRegistrationStage::processRegWarpLKTNonReference_frame_%d"
+ "CMIRawNightModeLKTBlendingV4.m"
+ "CMIRawNightModeLKTFlowV4.m"
+ "CMIRawNightModeLKTRegistrationTuningParamsV4.m"
+ "ConfidenceMinimum"
+ "ConfidenceRadialWeight"
+ "EnableLumaGamma"
+ "Failed to allocate CMIRawNightModeLKTBlending"
+ "Failed to allocate CMIRawNightModeLKTFlow"
+ "Failed to allocate _gammaReferenceLumaTex"
+ "Failed to allocate _lscRevertedReferenceLumaTex"
+ "Failed to allocate _referenceYUVATex"
+ "Failed to allocate commandBuffer (HybridLKT ref prep)"
+ "Failed to allocate gammaNonRefLumaTex"
+ "Failed to allocate lscRevertedNonRefLumaTex"
+ "Failed to allocate nonRefRGBATex"
+ "Failed to allocate nonRefYRGBTex"
+ "Failed to allocate nonRefYUVATex"
+ "Failed to allocate referenceRGBATex"
+ "Failed to allocate referenceYRGBTex"
+ "FilterType"
+ "FlowPostFilterEnabled"
+ "FlowPostFilterSigmaChroma"
+ "FlowPostFilterSigmaColor"
+ "FlowPostFilterSigmaConf"
+ "FlowPostFilterUseLCBDemosaic"
+ "FlowPostFilterYUV"
+ "HybridLKT::ReferencePrep"
+ "HybridLKT::applyLtmLumaEdgeGuide"
+ "HybridLKT::blendingDecision"
+ "HybridLKT::blendingDecisionBilateral"
+ "HybridLKT::boxPyramid5x5Downscale"
+ "HybridLKT::flowToShiftW8"
+ "HybridLKT::gammaPrepass"
+ "HybridLKT::gammaPrepassRgb"
+ "HybridLKT::lktDownscale2x"
+ "HybridLKT::lktFeatures"
+ "HybridLKT::lktFeaturesDerivatives"
+ "HybridLKT::lktFlowConsistency"
+ "HybridLKT::lktFlowPostFilter"
+ "HybridLKT::lktFlowPostFilterYUV"
+ "HybridLKT::lktSolverBoxXAndAxb"
+ "HybridLKT::lktSolverBoxY"
+ "HybridLKT::lktSolverPrepareMatrices"
+ "HybridLKT::lktZeroFlow"
+ "HybridLKT::patchNcc5x5"
+ "HybridLKT::patchSigma5x5"
+ "HybridLKT::revertLsc"
+ "HybridLKT::revertLscRgb"
+ "HybridLKT::rgbToYuva"
+ "HybridLKT::warpLumaByFlow"
+ "HybridLKT::warpLumaByHomography"
+ "HybridLKT::yrgbToRgba"
+ "LCB::Pyramid::demosaicDownsampleBayerYRGB"
+ "LKT"
+ "LKT::Pyramid"
+ "LKT:ComputeFlow level %d"
+ "LKT:waitUntilCompleted"
+ "LastScale"
+ "LastShownBuild:RawNightModeProcessorV4.m:842"
+ "LastShownDate:RawNightModeProcessorV4.m:842"
+ "LumaGamma"
+ "NCCBand"
+ "NCCDenseThreshold"
+ "NCCPatchSize"
+ "NScales"
+ "NWarpings"
+ "RevertLSC"
+ "SigmaRange"
+ "SigmaSpatial"
+ "SmoothstepHigh"
+ "SmoothstepLow"
+ "Unable to create _lktTuningParams"
+ "UseNominalCCMFromPreview"
+ "Warning: ApplyLTMToEdgeGuide is missing; using default value"
+ "Warning: BidirectionalError is missing; using default value"
+ "Warning: BlendingDownsampleGamma is missing; using default value"
+ "Warning: ConfidenceMinimum is missing; using default value"
+ "Warning: ConfidenceRadialWeight is missing; using default value"
+ "Warning: EnableLumaGamma is missing; using default value"
+ "Warning: FlowPostFilterEnabled is missing; using default value"
+ "Warning: FlowPostFilterSigmaChroma is missing; using default value"
+ "Warning: FlowPostFilterSigmaColor is missing; using default value"
+ "Warning: FlowPostFilterSigmaConf is missing; using default value"
+ "Warning: FlowPostFilterUseLCBDemosaic is missing; using default value"
+ "Warning: FlowPostFilterYUV is missing; using default value"
+ "Warning: LKT is missing; using default value"
+ "Warning: LastScale is missing; using default value"
+ "Warning: LumaGamma is missing; using default value"
+ "Warning: NCCBand is missing; using default value"
+ "Warning: NCCDenseThreshold is missing; using default value"
+ "Warning: NCCPatchSize is missing; using default value"
+ "Warning: NScales is missing; using default value"
+ "Warning: NWarpings is missing; using default value"
+ "Warning: RevertLSC is missing; using default value"
+ "Warning: SigmaRange is missing; using default value"
+ "Warning: SigmaSpatial is missing; using default value"
+ "Warning: SmoothstepHigh is missing; using default value"
+ "Warning: SmoothstepLow is missing; using default value"
+ "_applyLtmLumaEdgeGuidePipeline"
+ "_blendingDecisionBilateralPipeline"
+ "_blendingDecisionPipeline"
+ "_boxDownscalePipeline"
+ "_downscale2xPipeline"
+ "_featuresDerivativesPipeline"
+ "_featuresPipeline"
+ "_flowConsistencyPipeline"
+ "_flowPostFilterPipeline"
+ "_flowPostFilterYUVPipeline"
+ "_flowToShiftPipeline"
+ "_gammaPrepassPipeline"
+ "_gammaPrepassRGBPipeline"
+ "_gammaReferenceLumaTex"
+ "_lcbDemosaicYRGBPipeline"
+ "_lkt"
+ "_lkt is nil"
+ "_lktBlending"
+ "_lktBlending is nil"
+ "_lktTuningParams"
+ "_lktTuningParams is nil"
+ "_lscRevertedReferenceLumaTex"
+ "_patchNCCPipeline"
+ "_patchSigmaPipeline"
+ "_referenceYUVATex"
+ "_revertLSCPipeline"
+ "_revertLSCRGBPipeline"
+ "_rgbToYUVAPipeline"
+ "_solverBoxXAndAxbPipeline"
+ "_solverBoxYPipeline"
+ "_solverPrepareMatricesPipeline"
+ "_warpByFlowPipeline"
+ "_warpByHomographyPipeline"
+ "_yrgbToRGBAPipeline"
+ "_zeroFlowPipeline"
+ "_zeroTexturePipeline"
+ "applyLtmLumaEdgeGuide"
+ "bilateral"
+ "black_spot_mask"
+ "blendingDecision"
+ "blendingDecisionBilateral"
+ "boxPyramid5x5Downscale"
+ "clearOutputs"
+ "commandBuffer is nil"
+ "demosaicDownsampleBayerYRGB"
+ "flowToShiftW8"
+ "frame.lscGainsTex"
+ "frame.lscGainsTex is NULL"
+ "gammaNonRefLumaTex"
+ "gammaPrepass"
+ "gammaPrepassRgb"
+ "gammaReferenceLumaTex"
+ "learnedfusion_demosaic_quadra-v"
+ "lkt_C0_tex_%d"
+ "lkt_C1_tex_%d"
+ "lkt_G0_tex_%d"
+ "lkt_G1_tex_%d"
+ "lkt_I_tex_aux_%d"
+ "lkt_I_tex_ref_%d"
+ "lkt_J_tex_aux_%d"
+ "lkt_J_tex_ref_%d"
+ "lkt_conf_bwd_tex_%d"
+ "lkt_conf_fwd_tex_%d"
+ "lkt_ltm_guide"
+ "lkt_lumaWarpD_lvl%d"
+ "lkt_lumaWarpD_lvl0"
+ "lkt_lumaWarpG_lvl%d"
+ "lkt_lumaWarpG_lvl0"
+ "lkt_ncc_D"
+ "lkt_ncc_G"
+ "lkt_refPyr_lvl%d"
+ "lkt_uv_bwd_tex_%d_%d"
+ "lkt_uv_fwd_tex_%d_%d"
+ "lscRevertedNonRefLumaTex"
+ "lscRevertedReferenceLumaTex"
+ "ltm_guide"
+ "nccBand >= 0 && nccBand < kLKTMaxPyramidLevels"
+ "ncc_D"
+ "ncc_G"
+ "nonRefRGBATex"
+ "nonRefYRGBTex"
+ "nonRefYUVATex"
+ "none"
+ "nrf.lf.demosaic.blackSpotMaskDilationRadius"
+ "nrf.lf.demosaic.blackSpotMaskEnabled"
+ "nrf.lf.demosaic.blackSpotMaskThreshold"
+ "nrf.lf.demosaic.zeroChannelHeuristicEnabled"
+ "patchNcc5x5"
+ "patchSigma5x5"
+ "processRegWarpLKTNonReference input frame is nil"
+ "processRegWarpLKTNonReference ref frame is nil"
+ "refLuma.width == lktFlow.width && refLuma.height == lktFlow.height"
+ "refLuma.width == nonRefLuma.width && refLuma.height == nonRefLuma.height"
+ "ref_pyr[level]"
+ "referenceRGBATex"
+ "referenceYRGBTex"
+ "referenceYUVATex"
+ "regwarpInputNonRefTexLKT"
+ "revertLsc"
+ "revertLscRgb"
+ "rgbToYuva"
+ "warpD_l0"
+ "warpD_pyr[level]"
+ "warpG_l0"
+ "warpG_pyr[level]"
+ "warpLumaByFlow"
+ "warpLumaByHomography"
+ "yrgbToRgba"
+ "\xf0\xf0\xf0\x81"
+ "\xf0\xf0\xf0\xf0\xf1"
- "-[RawNightModeProcessor extractLSCMetadataFromReferenceFrame:]"
- "5"
- "<<<< LearnedDemosaicNetworkStage >>>> %s: Recovery luma and chroma textures must both be nil or both be non-nil."
- "<<<< LearnedDemosaicNetworkStage >>>> %s: _recoveryYUVImage is nil in LearnedDemosaic updateParameters and conflicts with correctDefectPixels.."
- "<<<< LearnedFusionNetworkStage >>>> %s: tileCount: {%d, %d}"
- "<<<< LearnedFusionProcessor >>>> %s: DefectCorrectionEITRatio missing from SR metadata, defaulting to 1.0 (correctDefectPixels=%d, srMetadata=%p)"
- "<<<< LearnedFusionProcessor >>>> %s: DefectCorrectionEITRatio must be > 0"
- "<<<< LearnedFusionProcessor >>>> %s: DefectCorrectionEITRatio received from SR metadata: %f"
- "<<<< LearnedFusionProcessor >>>> %s: Received _proxySyntheticReferenceTextureYUV ( %d x %d ) for frame: %d"
- "<<<< LearnedFusionProcessor >>>> %s: _proxySyntheticReferenceTextureYUV is nil"
- "<<<< LearnedFusionProcessor >>>> %s: demosaic frame %d (%s), label=%s, correctDefectPixels=%d, eitRatio=%.3f"
- "LastShownBuild:RawNightModeProcessorV4.m:820"
- "LastShownDate:RawNightModeProcessorV4.m:820"
- "referenceFrame.lensShadingCorrectionGainMapParameters"
- "referenceFrame.lensShadingCorrectionGainMapParameters is NULL"
- "referenceFrame.lscGainsTex"
- "referenceFrame.lscGainsTex is NULL"
- "\xf0\xf0\xf0q"

```
