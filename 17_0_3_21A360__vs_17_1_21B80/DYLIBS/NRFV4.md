## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-458.3.12.1.0
-  __TEXT.__text: 0x1ecc7c
+465.15.2.0.0
+  __TEXT.__text: 0x1eed10
   __TEXT.__auth_stubs: 0xea0
-  __TEXT.__objc_methlist: 0xdddc
+  __TEXT.__objc_methlist: 0xde54
   __TEXT.__const: 0x102580
-  __TEXT.__cstring: 0x2b9f9
+  __TEXT.__cstring: 0x2bc7c
   __TEXT.__gcc_except_tab: 0xdc4
-  __TEXT.__oslogstring: 0x1ee71
+  __TEXT.__oslogstring: 0x1eec0
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x2d68
-  __TEXT.__objc_classname: 0x18a5d
-  __TEXT.__objc_methname: 0x2d178
-  __TEXT.__objc_methtype: 0x585ca
-  __TEXT.__objc_stubs: 0x12900
-  __DATA_CONST.__got: 0x7d8
+  __TEXT.__unwind_info: 0x2d7c
+  __TEXT.__objc_classname: 0x18a4d
+  __TEXT.__objc_methname: 0x2d4b2
+  __TEXT.__objc_methtype: 0x5863d
+  __TEXT.__objc_stubs: 0x12a40
+  __DATA_CONST.__got: 0x7e0
   __DATA_CONST.__const: 0x9f0
-  __DATA_CONST.__objc_classlist: 0xc88
+  __DATA_CONST.__objc_classlist: 0xc80
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x28210
-  __DATA_CONST.__objc_selrefs: 0x54b8
+  __DATA_CONST.__objc_const: 0x28278
+  __DATA_CONST.__objc_selrefs: 0x5510
   __DATA_CONST.__objc_arraydata: 0xc38
-  __AUTH_CONST.__objc_const: 0x8c48
-  __AUTH_CONST.__cfstring: 0x11400
+  __AUTH_CONST.__objc_const: 0x8c00
+  __AUTH_CONST.__cfstring: 0x11540
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x9f0
   __AUTH_CONST.__objc_arrayobj: 0x930

   __AUTH_CONST.__objc_dictobj: 0x500
   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH_CONST.__auth_got: 0x760
-  __AUTH.__objc_data: 0x7d50
+  __AUTH.__objc_data: 0x7d00
   __DATA.__objc_protorefs: 0x18
   __DATA.__objc_classrefs: 0xdd8
   __DATA.__objc_superrefs: 0x930
-  __DATA.__objc_ivar: 0x306c
+  __DATA.__objc_ivar: 0x307c
   __DATA.__data: 0x950
   __DATA.__common: 0x100
   __DATA.__bss: 0x170

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B63B725E-3EB9-3688-9F98-6CB4AB476640
-  Functions: 4769
-  Symbols:   18899
-  CStrings:  16611
+  UUID: 258A539D-776E-3D0F-AD20-215AA653DFC1
+  Functions: 4783
+  Symbols:   18936
+  CStrings:  16664
 
Symbols:
+ +[RawDFDetectors srShouldUseMotionScoreBasedOnEvm:andSRTuning:]
+ +[RawDFDetectors srShouldUseMotionScoreBasedOnEvm:andSRTuning:logIntermediates:]
+ -[H13FastBayerProcConfig(LSC) _allocateLSCGainDataWithLSCConfig:inputFrame:data:lscGridData:]
+ -[H13FastBayerProcConfig(LSC) _computeALSProfileTableWithALSModel:illuminant:alsStrength:alsGridWidth:alsGridHeight:alsOutput:alsOutputWidth:alsOutputHeight:]
+ -[H13FastBayerProcConfig(LSC) _generateLSCGainMapWithLSCMetadata:inputFrame:data:lscGridData:auxFrame:]
+ -[H13FastBayerProcConfig(LSC) getLensShadingModulationWeightFromFrame:]
+ -[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationConfigForInputFrame:pdpConfig:blackLevelEstimationConfig:]
+ -[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationEnabledForInputFrame:enabled:]
+ -[H13FastRawScaleShaders blackLevelCorrection]
+ -[H13FastRawScaleShaders blackLevelEstimationQuadra]
+ -[H13FastRawScaleShaders blackLevelEstimation]
+ -[RawNightModeFusionMetalStage fuseInputFramesTile:withGGMaxFusionWeights:withGreenGhostThreshold:withInputWeightPyramidTile:withInputAccPyramid:withFramePyramidTile:withAccumPyramidTile:withClippingMaskPyrTexArray:withScratchPyrTexArray:toScratchTex:forBandIndex:tilePaddingSize:outputPyrBandOffset:outputTileSize:scratchOffset:encodeToContext:isFirstBatch:nonReferenceFrameCount:fusionParams:]
+ -[RawNightModeFusionMetalStage writeOutToAccumulator:fromScratchAccumulator:outputPyrBandOffset:scratchOffset:tilePaddingSize:outputTileSize:encodeToContext:isFirstBatch:bandIndex:]
+ -[RawNightModeGreenGhost applyInpaintWithDownscaledRGB:propagatedRGB:propagatedGradient:outputRGB:params:]
+ -[RawNightModeInferenceTiledConfig ktraceID]
+ -[RawNightModeInferenceTiledConfig setKtraceID:]
+ -[RawNightModePostFusionInference scratchPyramidTexArray]
+ -[RawNightModePostFusionInference setScratchPyramidTexArray:]
+ GCC_except_table23
+ _OBJC_CLASS_$_FigRegWarpPPGPUTuningParams
+ _OBJC_IVAR_$_H13FastRawScaleShaders._blackLevelCorrection
+ _OBJC_IVAR_$_H13FastRawScaleShaders._blackLevelEstimation
+ _OBJC_IVAR_$_H13FastRawScaleShaders._blackLevelEstimationQuadra
+ _OBJC_IVAR_$_RawNightModeInferenceTiledConfig._ktraceID
+ _OBJC_IVAR_$_RawNightModePostFusionInference._scratchPyramidTexArray
+ __OBJC_$_INSTANCE_METHODS_H13FastRawScaleConfig(RFPN|BlackLevelShading|PDP|GOC|BlackLevelEstimation|ShadingFPNR|PDC|DMA|CAR)
+ ___115-[CMIRawNightModeRegistrationStage processConstrainedNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.300
+ ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.228
+ ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke_2.244
+ ___50-[RawNightModeTiledInferenceProvider runInference]_block_invoke_2
+ ___50-[RawNightModeTiledInferenceProvider runInference]_block_invoke_3
+ ___block_literal_global.224
+ ___block_literal_global.230
+ ___block_literal_global.247
+ ___block_literal_global.87
+ __unnamed_array_storage.100
+ __unnamed_array_storage.104
+ __unnamed_array_storage.107
+ __unnamed_array_storage.115
+ __unnamed_array_storage.118
+ __unnamed_array_storage.133
+ __unnamed_array_storage.134
+ __unnamed_array_storage.143
+ __unnamed_array_storage.144
+ __unnamed_array_storage.147
+ __unnamed_array_storage.151
+ __unnamed_array_storage.189
+ __unnamed_array_storage.190
+ __unnamed_array_storage.193
+ __unnamed_array_storage.371
+ __unnamed_array_storage.86
+ __unnamed_array_storage.99
+ _fillSensorRawDecodeConfig
+ _kFigCaptureStreamMetadata_AdaptiveLensShadingStrength
+ _objc_msgSend$_allocateLSCGainDataWithLSCConfig:inputFrame:data:lscGridData:
+ _objc_msgSend$_computeALSProfileTableWithALSModel:illuminant:alsStrength:alsGridWidth:alsGridHeight:alsOutput:alsOutputWidth:alsOutputHeight:
+ _objc_msgSend$_generateLSCGainMapWithLSCMetadata:inputFrame:data:lscGridData:auxFrame:
+ _objc_msgSend$applyInpaintWithDownscaledRGB:propagatedRGB:propagatedGradient:outputRGB:params:
+ _objc_msgSend$blackLevelCorrection
+ _objc_msgSend$blackLevelEstimation
+ _objc_msgSend$blackLevelEstimationQuadra
+ _objc_msgSend$fuseInputFramesTile:withGGMaxFusionWeights:withGreenGhostThreshold:withInputWeightPyramidTile:withInputAccPyramid:withFramePyramidTile:withAccumPyramidTile:withClippingMaskPyrTexArray:withScratchPyrTexArray:toScratchTex:forBandIndex:tilePaddingSize:outputPyrBandOffset:outputTileSize:scratchOffset:encodeToContext:isFirstBatch:nonReferenceFrameCount:fusionParams:
+ _objc_msgSend$getBlackLevelEstimationConfigForInputFrame:pdpConfig:blackLevelEstimationConfig:
+ _objc_msgSend$getBlackLevelEstimationEnabledForInputFrame:enabled:
+ _objc_msgSend$getLensShadingModulationWeightFromFrame:
+ _objc_msgSend$ktraceID
+ _objc_msgSend$setKtraceID:
+ _objc_msgSend$setScratchPyramidTexArray:
+ _objc_msgSend$srShouldUseMotionScoreBasedOnEvm:andSRTuning:
+ _objc_msgSend$srShouldUseMotionScoreBasedOnEvm:andSRTuning:logIntermediates:
+ _objc_msgSend$writeOutToAccumulator:fromScratchAccumulator:outputPyrBandOffset:scratchOffset:tilePaddingSize:outputTileSize:encodeToContext:isFirstBatch:bandIndex:
- -[CMIRawNightModeRegWarpTuningParams maxNumberOfPyramidLevels]
- -[CMIRawNightModeRegWarpTuningParams readPlist:]
- -[H13FastBayerProcConfig(LSC) _allocateLSCGainDataWithLSCConfig:metadata:data:lscGridData:]
- -[H13FastBayerProcConfig(LSC) _computeALSProfileTableWithALSModel:illuminant:alsGridWidth:alsGridHeight:alsOutput:alsOutputWidth:alsOutputHeight:]
- -[H13FastBayerProcConfig(LSC) _generateLSCGainMapWithLSCMetadata:metadata:data:lscGridData:auxFrame:]
- -[RawNightModeFusionMetalStage fuseInputFramesTile:withGGMaxFusionWeights:withGreenGhostThreshold:withInputWeightPyramidTile:withInputAccPyramid:withFramePyramidTile:withAccumPyramidTile:withClippingMaskPyrTexArray:toOutputPyramidBandTex:forBandIndex:tilePaddingSize:outputPyrBandOffset:outputTileSize:encodeToContext:isFirstBatch:nonReferenceFrameCount:fusionParams:]
- -[RawNightModeGreenGhost applyInpaintWithDownscaledRGB:propagatedRGB:propagatedGradient:maskPreInpainting:outputRGB:params:]
- GCC_except_table25
- _OBJC_CLASS_$_CMIRawNightModeRegWarpTuningParams
- _OBJC_IVAR_$_CMIRawNightModeRegWarpTuningParams._maxNumberOfPyramidLevels
- _OBJC_METACLASS_$_CMIRawNightModeRegWarpTuningParams
- __OBJC_$_INSTANCE_METHODS_CMIRawNightModeRegWarpTuningParams
- __OBJC_$_INSTANCE_METHODS_H13FastRawScaleConfig(RFPN|BlackLevelShading|PDP|GOC|ShadingFPNR|PDC|DMA|CAR)
- __OBJC_$_INSTANCE_VARIABLES_CMIRawNightModeRegWarpTuningParams
- __OBJC_$_PROP_LIST_CMIRawNightModeRegWarpTuningParams
- __OBJC_CLASS_RO_$_CMIRawNightModeRegWarpTuningParams
- __OBJC_METACLASS_RO_$_CMIRawNightModeRegWarpTuningParams
- ___115-[CMIRawNightModeRegistrationStage processConstrainedNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.314
- ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.242
- ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke_2.258
- ___block_literal_global.238
- ___block_literal_global.261
- ___block_literal_global.82
- ___block_literal_global.85
- __unnamed_array_storage.106
- __unnamed_array_storage.121
- __unnamed_array_storage.122
- __unnamed_array_storage.127
- __unnamed_array_storage.128
- __unnamed_array_storage.131
- __unnamed_array_storage.132
- __unnamed_array_storage.136
- __unnamed_array_storage.169
- __unnamed_array_storage.174
- __unnamed_array_storage.177
- __unnamed_array_storage.368
- __unnamed_array_storage.74
- __unnamed_array_storage.75
- _objc_msgSend$_allocateLSCGainDataWithLSCConfig:metadata:data:lscGridData:
- _objc_msgSend$_computeALSProfileTableWithALSModel:illuminant:alsGridWidth:alsGridHeight:alsOutput:alsOutputWidth:alsOutputHeight:
- _objc_msgSend$_generateLSCGainMapWithLSCMetadata:metadata:data:lscGridData:auxFrame:
- _objc_msgSend$applyInpaintWithDownscaledRGB:propagatedRGB:propagatedGradient:maskPreInpainting:outputRGB:params:
- _objc_msgSend$fuseInputFramesTile:withGGMaxFusionWeights:withGreenGhostThreshold:withInputWeightPyramidTile:withInputAccPyramid:withFramePyramidTile:withAccumPyramidTile:withClippingMaskPyrTexArray:toOutputPyramidBandTex:forBandIndex:tilePaddingSize:outputPyrBandOffset:outputTileSize:encodeToContext:isFirstBatch:nonReferenceFrameCount:fusionParams:
- _objc_msgSend$maxNumberOfPyramidLevels
- _objc_msgSend$setMaxNumberOfPyramidLevels:
CStrings:
+ "+[RawDFDetectors srShouldUseMotionScoreBasedOnEvm:andSRTuning:logIntermediates:]"
+ "<<<< RawDFDetectors >>>> %s: evm nil"
+ "<<<< RawDFDetectors >>>> %s: srTuning nil"
+ "@\"FigRegWarpPPGPUTuningParams\""
+ "B36@0:8@16@24B32"
+ "BlackLevelEstimation"
+ "FocusPixelScaling"
+ "H13FastRawScale::blackLevelCorrection"
+ "H13FastRawScale::blackLevelEstimation"
+ "H13FastRawScale::blackLevelEstimationQuadra"
+ "H13FastRawScaleConfig+BlackLevelEstimation.m"
+ "InlierDeltaThreshold"
+ "LensShadingModulation"
+ "MaxInlierValue"
+ "MaxOPBErrorRatio"
+ "MinPerceivableAdjustment"
+ "NeighborsDeltaThreshold"
+ "T@\"<MTLComputePipelineState>\",R,N,V_blackLevelCorrection"
+ "T@\"<MTLComputePipelineState>\",R,N,V_blackLevelEstimation"
+ "T@\"<MTLComputePipelineState>\",R,N,V_blackLevelEstimationQuadra"
+ "T@\"FigRegWarpPPGPUTuningParams\",&,V_regwarpTuningParams"
+ "T@\"NSMutableArray\",&,N,V_scratchPyramidTexArray"
+ "TQ,N,V_ktraceID"
+ "_allocateLSCGainDataWithLSCConfig:inputFrame:data:lscGridData:"
+ "_blackLevelCorrection"
+ "_blackLevelEstimation"
+ "_blackLevelEstimationQuadra"
+ "_computeALSProfileTableWithALSModel:illuminant:alsStrength:alsGridWidth:alsGridHeight:alsOutput:alsOutputWidth:alsOutputHeight:"
+ "_generateLSCGainMapWithLSCMetadata:inputFrame:data:lscGridData:auxFrame:"
+ "_ktraceID"
+ "_scratchPyramidTexArray"
+ "applyInpaintWithDownscaledRGB:propagatedRGB:propagatedGradient:outputRGB:params:"
+ "blackLevelCorrection"
+ "blackLevelEstimation"
+ "blackLevelEstimationConfig->grids[gridIdx].enabled"
+ "blackLevelEstimationQuadra"
+ "fuseInputFramesTile:withGGMaxFusionWeights:withGreenGhostThreshold:withInputWeightPyramidTile:withInputAccPyramid:withFramePyramidTile:withAccumPyramidTile:withClippingMaskPyrTexArray:withScratchPyrTexArray:toScratchTex:forBandIndex:tilePaddingSize:outputPyrBandOffset:outputTileSize:scratchOffset:encodeToContext:isFirstBatch:nonReferenceFrameCount:fusionParams:"
+ "getBlackLevelEstimationConfigForInputFrame:pdpConfig:blackLevelEstimationConfig:"
+ "getBlackLevelEstimationEnabledForInputFrame:enabled:"
+ "getLensShadingModulationWeightFromFrame:"
+ "i136@0:8@16@24f32[4@]36[4@]44[16@]52[3@]60[4@]68[4@]76@84i9296100104108@112B120I124^{RawNightModeFusionParams=fBffBff}128"
+ "i40@0:8@16r^{?=[16{?=BC}]BCCiiSSiSS}24^{?=[4{?=BC}]fffff}32"
+ "i60@0:8@16@24f32S36S40^f44S52S56"
+ "i64@0:8@16@2432364044@48B56i60"
+ "ktraceID"
+ "outputPyrBandTex.height == scratchAccumulatorTex.height"
+ "scratchAccumulationTex"
+ "scratchAccumulationTexArray"
+ "scratchAccumulationTex_Band%d_%d"
+ "scratchPyrTexArray[b]"
+ "scratchPyramidTexArray"
+ "scratchTex"
+ "setKtraceID:"
+ "setScratchPyramidTexArray:"
+ "srShouldUseMotionScoreBasedOnEvm:andSRTuning:"
+ "srShouldUseMotionScoreBasedOnEvm:andSRTuning:logIntermediates:"
+ "writeOutToAccumulator:fromScratchAccumulator:outputPyrBandOffset:scratchOffset:tilePaddingSize:outputTileSize:encodeToContext:isFirstBatch:bandIndex:"
- "\x19"
- "@\"CMIRawNightModeRegWarpTuningParams\""
- "CMIRawNightModeRegWarpTuningParams"
- "MaxNumberOfPyramidLevels"
- "T@\"CMIRawNightModeRegWarpTuningParams\",&,V_regwarpTuningParams"
- "TI,R,N,V_maxNumberOfPyramidLevels"
- "_allocateLSCGainDataWithLSCConfig:metadata:data:lscGridData:"
- "_computeALSProfileTableWithALSModel:illuminant:alsGridWidth:alsGridHeight:alsOutput:alsOutputWidth:alsOutputHeight:"
- "_generateLSCGainMapWithLSCMetadata:metadata:data:lscGridData:auxFrame:"
- "_maxNumberOfPyramidLevels"
- "applyInpaintWithDownscaledRGB:propagatedRGB:propagatedGradient:maskPreInpainting:outputRGB:params:"
- "fuseInputFramesTile:withGGMaxFusionWeights:withGreenGhostThreshold:withInputWeightPyramidTile:withInputAccPyramid:withFramePyramidTile:withAccumPyramidTile:withClippingMaskPyrTexArray:toOutputPyramidBandTex:forBandIndex:tilePaddingSize:outputPyrBandOffset:outputTileSize:encodeToContext:isFirstBatch:nonReferenceFrameCount:fusionParams:"
- "ggMaskPreInpainting"
- "i124@0:8@16@24f32[4@]36[4@]44[16@]52[3@]60[4@]68@76i84889296@100B108I112^{RawNightModeFusionParams=fBffBff}116"
- "i56@0:8@16@24S32S36^f40S48S52"
- "maxNumberOfPyramidLevels"
- "outputPyrBandTex"
- "setMaxNumberOfPyramidLevels:"

```
