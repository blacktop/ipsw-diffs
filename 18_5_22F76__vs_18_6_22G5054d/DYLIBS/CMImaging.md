## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x18eb58
-  __TEXT.__auth_stubs: 0x1310
+587.140.7.122.2
+  __TEXT.__text: 0x176bac
+  __TEXT.__auth_stubs: 0x1360
   __TEXT.__objc_methlist: 0xa60c
-  __TEXT.__const: 0x2b80
-  __TEXT.__cstring: 0x14bdb
-  __TEXT.__gcc_except_tab: 0xb3c
-  __TEXT.__oslogstring: 0x4b9e
+  __TEXT.__const: 0x2980
+  __TEXT.__cstring: 0x22793
+  __TEXT.__oslogstring: 0x12016
+  __TEXT.__gcc_except_tab: 0xe0c
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__unwind_info: 0x2540
-  __TEXT.__eh_frame: 0xc18
+  __TEXT.__unwind_info: 0x2470
+  __TEXT.__eh_frame: 0x2c8
   __TEXT.__objc_classname: 0x11eb
-  __TEXT.__objc_methname: 0x1ce1a
+  __TEXT.__objc_methname: 0x1ce42
   __TEXT.__objc_methtype: 0x7e86
-  __TEXT.__objc_stubs: 0x9620
+  __TEXT.__objc_stubs: 0x96c0
   __DATA_CONST.__got: 0x948
   __DATA_CONST.__const: 0x848
   __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4dc0
+  __DATA_CONST.__objc_selrefs: 0x4dd0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x2e0
-  __AUTH_CONST.__auth_got: 0x9a0
+  __AUTH_CONST.__auth_got: 0x9c0
   __AUTH_CONST.__const: 0x650
-  __AUTH_CONST.__cfstring: 0x5260
+  __AUTH_CONST.__cfstring: 0x5660
   __AUTH_CONST.__objc_const: 0x18a38
   __AUTH_CONST.__objc_intobj: 0x5e8
   __AUTH_CONST.__objc_arrayobj: 0x90

   __AUTH.__data: 0x8
   __DATA.__objc_ivar: 0x12ec
   __DATA.__data: 0x11348
-  __DATA.__common: 0x140
+  __DATA.__common: 0x1f0
   __DATA.__bss: 0xc0
   __DATA_DIRTY.__objc_data: 0x2bc0
   __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__common: 0xc0
   __DATA_DIRTY.__bss: 0xb0
-  __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 540EF310-1157-3728-98CC-E5C839065DD6
-  Functions: 5722
-  Symbols:   16204
-  CStrings:  8467
+  UUID: 76D423B8-9435-3BC0-B559-A25C1D782F52
+  Functions: 5489
+  Symbols:   16186
+  CStrings:  10233
 
Symbols:
+ +[CMINoiseModels _fpnrScalingFactor:darkCurrentNoiseCalibration:fpnrEnabled:].cold.1
+ +[CMINoiseModels _fpnrScalingFactor:darkCurrentNoiseCalibration:fpnrEnabled:].cold.2
+ +[CMINoiseModels _fpnrScalingFactor:darkCurrentNoiseCalibration:fpnrEnabled:].cold.3
+ +[CMINoiseModels _fpnrScalingFactor:darkCurrentNoiseCalibration:fpnrEnabled:].cold.4
+ +[CMINoiseModels _fpnrScalingFactor:darkCurrentNoiseCalibration:fpnrEnabled:].cold.5
+ +[CMINoiseModels _fpnrScalingFactor:darkCurrentNoiseCalibration:fpnrEnabled:].cold.6
+ +[CMINoiseModels _fpnrScalingFactor:darkCurrentNoiseCalibration:fpnrEnabled:].cold.7
+ +[CMINoiseModels _fpnrScalingFactor:darkCurrentNoiseCalibration:fpnrEnabled:].cold.8
+ +[CMINoiseModels _fpnrSpatialStdDev:darkCurrentNoiseCalibration:fpnrEnabled:].cold.1
+ +[CMINoiseModels _fpnrSpatialStdDev:darkCurrentNoiseCalibration:fpnrEnabled:].cold.2
+ +[CMIVNRProcessor getDefaultTuningParameters].cold.1
+ +[CMIVNRProcessor getDefaultTuningParameters].cold.2
+ +[CMIVNRProcessor getDefaultTuningParameters].cold.3
+ +[CMIVNRProcessor getTuningParametersForCurrentDevice].cold.1
+ +[CMIVNRProcessor getTuningParametersForCurrentDevice].cold.2
+ +[CMIVNRProcessor getTuningParametersForCurrentDevice].cold.3
+ +[CMIVNRProcessor getTuningParametersForCurrentDevice].cold.4
+ -[CMIFFTDimension initWithSize:iStride:oStride:primeFactors:].cold.1
+ -[CMIFFTExecutor _execute1DMixedRadix:dimension:layout:precision:direction:primeFactors:batchSize:].cold.1
+ -[CMIFFTExecutor _execute1DMixedRadix:dimension:layout:precision:direction:primeFactors:batchSize:].cold.2
+ -[CMIFFTExecutor _execute1DSingleRadix:dimension:layout:precision:direction:radix:batchSize:].cold.1
+ -[CMIFFTExecutor initWithContext:].cold.1
+ -[CMIFFTExecutor initWithContext:].cold.2
+ -[CMIFFTExecutor initWithContext:].cold.3
+ -[CMIFFTExecutor initWithContext:].cold.4
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.1
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.10
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.11
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.2
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.3
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.4
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.5
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.6
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.7
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.8
+ -[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:].cold.9
+ -[CMIFlexGTCStage initWithOptionalCommandQueue:].cold.1
+ -[CMIFlexGTCStage initWithOptionalCommandQueue:].cold.2
+ -[CMIFlexGTCStage initWithOptionalCommandQueue:].cold.3
+ -[CMIInferenceDeviceEspressoV1 init].cold.1
+ -[CMIInferenceDeviceEspressoV1 init].cold.2
+ -[CMIInferenceDeviceEspressoV1 init].cold.3
+ -[CMIInferenceNetworkIOPortEspressoV2 _getInfoFromEsop:portName:isInput:].cold.1
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.1
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.10
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.2
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.3
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.4
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.5
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.6
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.7
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.8
+ -[CMIInferenceNetworkInstanceEspressoV2 _allocateTexturesWithDevice:ports:useTextureArrays:outputTextureArray:].cold.9
+ -[CMIMetalResourceCache initWithMetalDevice:].cold.1
+ -[CMIMetalResourceCache initWithMetalDevice:].cold.2
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.1
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.10
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.11
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.12
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.13
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.14
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.2
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.3
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.4
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.5
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.6
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.7
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.8
+ -[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:].cold.9
+ -[CMIStyleEngineProcessor _bindAllInternalYUVTextures:].cold.1
+ -[CMIStyleEngineProcessor externalMemoryDescriptorForConfiguration:].cold.1
+ -[CMIStyleEngineProcessor externalMemoryDescriptorForConfiguration:].cold.2
+ -[CMIVNRProcessor initWithCommandQueue:].cold.1
+ -[CMIVNRProcessor initWithCommandQueue:].cold.2
+ -[CMIVNRProcessor initWithCommandQueue:].cold.3
+ -[CMIVNRProcessor initWithCommandQueue:].cold.4
+ -[CMIVNRProcessor prepareToProcess:prepareDescriptor:].cold.1
+ -[CMIVNRProcessor prepareToProcess:prepareDescriptor:].cold.2
+ -[CMIVNRProcessor prepareToProcess:prepareDescriptor:].cold.3
+ -[CMIVNRProcessor prepareToProcess:prepareDescriptor:].cold.4
+ -[CMIVNRProcessor prepareToProcess:prepareDescriptor:].cold.5
+ -[CMIVNRProcessor prepareToProcess:prepareDescriptor:].cold.6
+ -[CMIVNRProcessor prewarm].cold.1
+ -[CMIVNRProcessor waitUntilScheduledWithWorkloadName:].cold.1
+ -[CMIVNRProcessor(DeghostPropagate) propagateDeghostingScoresDownPyramid:].cold.1
+ -[CMIVNRProcessor(DeghostPropagate) propagateDeghostingScoresDownPyramid:].cold.2
+ -[CMIVNRProcessor(DeghostPropagate) propagateDeghostingScoresDownPyramid:].cold.3
+ -[CMIVNRProcessor(DeghostPropagate) propagateDeghostingScoresDownPyramid:].cold.4
+ -[CMIVNRProcessor(Fusion) fuseWithInputPyramid:deghostPyramid:previousOutputPyramid:outputPyramid:inputLuma:inputChroma:previousOutputLuma:previousOutputChroma:outputLuma:outputChroma:frameIdx:].cold.1
+ -[CMIVNRProcessor(PyramidGen) fillInputPyramid:previousOutputPyramid:deghostPyramid:inputLuma:inputChroma:previousOutputLuma:previousOutputChroma:].cold.1
+ -[CMIVNRProcessor(TextureBinding) bindTextureToPixelBuffer:plane:metalPixelFormat:usage:].cold.1
+ -[CMIVNRProcessor(TextureBinding) bindTextureToPixelBuffer:plane:metalPixelFormat:usage:].cold.2
+ -[CMIVNRProcessor(TextureBinding) bindTextureToPixelBuffer:plane:metalPixelFormat:usage:].cold.3
+ -[CMIVNRProcessor(TextureBinding) bindTextureToPixelBuffer:plane:metalPixelFormat:usage:].cold.4
+ -[CMIVNRProcessor(TextureBinding) bindTextureToPixelBuffer:plane:metalPixelFormat:usage:].cold.5
+ -[CMIVNRProcessor(TextureBinding) bindTextureToPixelBuffer:plane:metalPixelFormat:usage:].cold.6
+ -[FigM2MController init].cold.2
+ -[VNRGainValueArray initWithArray:].cold.1
+ -[VNRGainValueArray interpolateValueForGain:].cold.1
+ -[VNRGainValueArray interpolateValueForGain:].cold.2
+ -[VNRPyramid initWithMetalDevice:isForDeghosting:width:height:nLumaLevels:nChromaLevels:lumaStartingLevel:chromaStartingLevel:].cold.1
+ -[VNRPyramid initWithMetalDevice:isForDeghosting:width:height:nLumaLevels:nChromaLevels:lumaStartingLevel:chromaStartingLevel:].cold.2
+ -[VNRShaders createFusionShaderUsingMetalDevice:colorChannel:isFirstFrame:isTopBand:isBottomBand:].cold.1
+ -[VNRShaders initWithMetalDevice:].cold.1
+ -[VNRShaders initWithMetalDevice:].cold.2
+ -[VNRTuning initWithTuningParamsDict:].cold.1
+ -[VNRTuning initWithTuningParamsDict:].cold.10
+ -[VNRTuning initWithTuningParamsDict:].cold.11
+ -[VNRTuning initWithTuningParamsDict:].cold.2
+ -[VNRTuning initWithTuningParamsDict:].cold.3
+ -[VNRTuning initWithTuningParamsDict:].cold.4
+ -[VNRTuning initWithTuningParamsDict:].cold.5
+ -[VNRTuning initWithTuningParamsDict:].cold.6
+ -[VNRTuning initWithTuningParamsDict:].cold.7
+ -[VNRTuning initWithTuningParamsDict:].cold.8
+ -[VNRTuning initWithTuningParamsDict:].cold.9
+ -[VNRTuning updateWithGain:].cold.1
+ -[VNRTuning updateWithGain:].cold.2
+ -[VNRTuning updateWithGain:].cold.3
+ -[VNRTuning updateWithGain:].cold.4
+ -[VNRTuning updateWithGain:].cold.5
+ -[VNRTuning updateWithGain:].cold.6
+ -[VNRTuning updateWithGain:].cold.7
+ -[VNRTuning updateWithGain:].cold.8
+ -[VNRTuning updateWithGain:].cold.9
+ -[VNRTuningBand initWithTuningParamsDict:].cold.1
+ -[VNRTuningBand initWithTuningParamsDict:].cold.2
+ -[VNRTuningBand initWithTuningParamsDict:].cold.3
+ -[VNRTuningBand initWithTuningParamsDict:].cold.4
+ -[VNRTuningBand updateWithGain:].cold.1
+ -[VNRTuningBand updateWithGain:].cold.2
+ -[VNRTuningBand updateWithGain:].cold.3
+ GCC_except_table30
+ GCC_except_table31
+ _CMIGetRGBFromYCCConversionMatrixForPixelBuffer.cold.1
+ _CMIGetYCCFromRGBConversionMatrixForPixelBuffer.cold.1
+ _CMIShadingFPNCorrectionImageMetadataToShortString
+ _FigDebugIsInternalBuild
+ _FigGetUpTime
+ _FigHostTimeToNanoseconds
+ _FigMetalContextTrace
+ _FigSignalErrorAt3
+ _IOSurfaceGetHeight
+ _IOSurfaceGetWidth
+ _M2MControllerTrace
+ _MTLAllocator
+ _OUTLINED_FUNCTION_26
+ _StereoDisparityGDC
+ __PromotedConst.27
+ __PromotedConst.28
+ ___34-[CMIStyleEngineProcessor process]_block_invoke.596
+ ___69-[CMITiledInferenceProcessor runWithTileCount:withCompletionHandler:]_block_invoke.304
+ ___WritePixelBufferToFile_block_invoke.32
+ ___block_descriptor_64_e8_32s40s48w_e8_v16?08lw48l8s32l8s40l8
+ ___block_literal_global.135
+ ___block_literal_global.171
+ ___block_literal_global.173
+ ___block_literal_global.231
+ ___block_literal_global.58
+ ___block_literal_global.60
+ _calculateTotalGain.cold.1
+ _calculateTotalGain.cold.2
+ _calculateTotalGain.cold.3
+ _calculateTotalGain.cold.4
+ _gCMIColorManagement
+ _gCMIFlexGTCStage
+ _gMetalEventSynchronizerTrace
+ _gSSCHistogramTrace
+ _gSmartStyleCommonSettingsTrace
+ _gSmartStyleRendererUtils
+ _gStyleEngineConfigurationTrace
+ _gStyleEngineProcessorTrace
+ _gSubjectRelightingPlist
+ _gVNRTrace
+ _getFloatParameter
+ _getFloatValue
+ _getMTLTextureCompressionFeedbackAsString
+ _objc_msgSend$appendString:
+ _objc_msgSend$componentsJoinedByString:
+ _objc_msgSend$getFragmentCount
+ _objc_msgSend$kernelEndTime
+ _objc_msgSend$kernelStartTime
+ _stringForPixelFormat
- +[CMISmartStyleUtilitiesV1 defaultStyleForCastType:].cold.1
- +[RegWarpPP CheckParameters:imageWidth:imageHeight:imageFormat:].cold.2
- +[RegWarpPP CheckParameters:imageWidth:imageHeight:imageFormat:].cold.3
- -[CMIImmutableSmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:].cold.2
- -[CMIImmutableSmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:].cold.3
- -[CMIImmutableSmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:].cold.4
- -[CMIImmutableSmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:].cold.5
- -[CMISSIM _encodeSSIMCalculation:imageA:imageB:outputSSIMMap:].cold.2
- -[CMISSIM _loadKernel:name:functionConstants:].cold.1
- -[CMISSIM _loadKernel:name:functionConstants:].cold.2
- -[CMISSIM _setupMetalContextWithCommandQueue:].cold.5
- -[CMISSIM _validateConfiguration:].cold.1
- -[CMISSIM calculateWithImageA:imageB:outputSSIMMap:outputSSIMVal:].cold.3
- -[CMISSIM calculateWithImageA:imageB:outputSSIMMap:outputSSIMVal:].cold.4
- -[CMISSIM calculateWithImageA:imageB:outputSSIMMap:outputSSIMVal:].cold.5
- -[CMISSIM encodeToCommandBuffer:imageA:imageB:outputSSIMMap:outputSSIMVal:].cold.11
- -[CMISSIM encodeToCommandBuffer:imageA:imageB:outputSSIMMap:outputSSIMVal:].cold.12
- -[CMISSIM initWithOptionalCommandQueue:config:].cold.4
- -[CMISSIM initWithOptionalCommandQueue:config:].cold.5
- -[CMISmartStyleColorCubePoolV1 newColorCube].cold.1
- -[CMISmartStyleMetalRendererV1 _applyFinalRendering].cold.5
- -[CMISmartStyleMetalRendererV1 _encodeImageReduction:inputTexture:inputROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:].cold.2
- -[CMISmartStyleMetalRendererV1 _encodeLinear].cold.5
- -[CMISmartStyleMetalRendererV1 _populateStaticRenderParametersFromTuning:inputStatisticsByStatsKey:].cold.2
- -[CMISmartStyleMetalRendererV1 _populateStaticRenderParametersFromTuning:inputStatisticsByStatsKey:].cold.3
- -[CMISmartStyleMetalRendererV1 _populateStaticRenderParametersFromTuning:inputStatisticsByStatsKey:].cold.4
- -[CMISmartStyleMetalRendererV1 _populateStaticRenderParametersFromTuning:inputStatisticsByStatsKey:].cold.5
- -[CMISmartStyleMetalRendererV1 _runImageReductionAndUpdateBaseGain:].cold.2
- -[CMISmartStyleMetalRendererV1 _runImageReductionAndUpdateBaseGain:].cold.3
- -[CMISmartStyleMetalRendererV1 initWithMetalContext:].cold.7
- -[CMISmartStyleMetalRendererV1 initWithMetalContext:].cold.8
- -[CMISmartStyleMetalRendererV1 initWithMetalContext:].cold.9
- -[CMISmartStyleMetalRendererV1 process].cold.14
- -[CMISmartStyleMetalRendererV1 process].cold.15
- -[CMISmartStyleMetalRendererV1 process].cold.16
- -[CMISmartStyleMetalRendererV1 process].cold.17
- -[CMISmartStyleMetalRendererV1 process].cold.18
- -[CMISmartStyleMetalRendererV1 process].cold.19
- -[CMISmartStyleMetalRendererV1 process].cold.20
- -[CMISmartStyleMetalRendererV1 process].cold.21
- -[CMISmartStyleMetalRendererV1 process].cold.22
- -[CMISmartStyleMetalRendererV1 process].cold.23
- -[CMISmartStyleMetalRendererV1 process].cold.24
- -[CMISmartStyleMetalRendererV1 process].cold.25
- -[CMISmartStyleMetalRendererV1 process].cold.26
- -[CMISmartStyleProxyRendererV1 _bindInputPixelBuffersAsTextures].cold.1
- -[CMISmartStyleProxyRendererV1 _generateColorCubes].cold.3
- -[CMISmartStyleProxyRendererV1 _populateStaticRenderParameters:forInputStyle:fromTuning:].cold.1
- -[CMISmartStyleProxyRendererV1 _populateStaticRenderParameters:forInputStyle:fromTuning:].cold.2
- -[CMISmartStyleProxyRendererV1 _populateStaticRenderParameters:forInputStyle:fromTuning:].cold.3
- -[CMISmartStyleProxyRendererV1 _populateStaticRenderParameters:forInputStyle:fromTuning:].cold.4
- -[CMISmartStyleProxyRendererV1 _updateColorCubeCache].cold.1
- -[CMISmartStyleProxyRendererV1 _updateColorCubesFromTuning:].cold.3
- -[CMISmartStyleProxyRendererV1 _updateColorCubesFromTuning:].cold.4
- -[CMISmartStyleProxyRendererV1 process].cold.10
- -[CMISmartStyleProxyRendererV1 process].cold.5
- -[CMISmartStyleProxyRendererV1 process].cold.6
- -[CMISmartStyleProxyRendererV1 process].cold.7
- -[CMISmartStyleProxyRendererV1 process].cold.8
- -[CMISmartStyleProxyRendererV1 process].cold.9
- -[CMISmartStyleProxyRendererV1 setup].cold.10
- -[CMISmartStyleProxyRendererV1 setup].cold.11
- -[CMISmartStyleProxyRendererV1 setup].cold.9
- -[CMISmartStyleUtilitiesV1 computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficients:outputDeltaMapPixelBuffer:].cold.6
- -[CMISmartStyleUtilitiesV1 computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficients:outputDeltaMapPixelBuffer:].cold.7
- -[CMISmartStyleUtilitiesV1 computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficientsDict:outputDeltaMapPixelBuffer:].cold.6
- -[CMISmartStyleUtilitiesV1 computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficientsDict:outputDeltaMapPixelBuffer:].cold.7
- -[CMISmartStyleUtilitiesV1 computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficientsDict:outputDeltaMapPixelBuffer:].cold.8
- -[CMISmartStyleUtilitiesV1 computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficientsDict:outputDeltaMapPixelBuffer:].cold.9
- -[CMISmartStyleUtilitiesV1 computeOriginalUnstyledPixelBufferFrom:inputDeltaMapPixelBuffer:inputCoefficientsPixelBuffer:outputUnstyledPixelBuffer:].cold.8
- -[CMISmartStyleUtilitiesV1 computeOriginalUnstyledPixelBufferFrom:inputDeltaMapPixelBuffer:inputMetadataDict:outputUnstyledPixelBuffer:].cold.10
- -[CMISmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:].cold.2
- -[CMISmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:].cold.3
- -[CMISmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:].cold.4
- -[CMISmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:].cold.5
- -[CMISmartStyleV1 setCastIntensity:].cold.1
- -[CMISmartStyleV1 setCastType:].cold.1
- -[CMISmartStyleV1 setColorBias:].cold.1
- -[CMISmartStyleV1 setToneBias:].cold.1
- -[CMIStyleEngineCoefficientsFilter _calculateGlobalRemixFactorForWindow:filteredWindow:remixFactor:].cold.3
- -[CMIStyleEngineCoefficientsProcessor filterCoefficientsForFrameWithMetadata:pts:filterType:toPixelBuffer:toGlobalRemixFactor:].cold.11
- -[CMIStyleEngineCoefficientsRingBuffer initWithCapacity:].cold.2
- -[CMIStyleEngineCoefficientsRingBuffer initWithCapacity:].cold.3
- -[CMIStyleEngineCreateLinearSystem _setWeightPlane:term:priorScaleFactor:].cold.1
- -[CMIStyleEngineCreateLinearSystem _setWeightPlane:term:priorScaleFactor:].cold.2
- -[FigMetalAllocator newBufferWithDescriptor:].cold.2
- -[FigMetalAllocator newTextureWithDescriptor:].cold.2
- -[FigMetalAllocatorBackend newBufferWithDescriptor:sizeAlign:].cold.2
- -[FigMetalAllocatorBackend newTextureWithDescriptor:sizeAlign:].cold.2
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.10
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.11
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.12
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.13
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.14
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.15
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.16
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.17
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.18
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.19
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.2
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.3
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.4
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.5
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.6
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.7
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.8
- -[FigRegWarpPPGPUShaders initWithMetalContext:].cold.9
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.10
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.11
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.2
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.3
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.4
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.5
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.6
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.7
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.8
- -[NSArray(GainValueLookup) cmi_interpolateValueForGain:].cold.9
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.1
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.10
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.11
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.2
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.3
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.4
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.5
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.6
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.7
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.8
- -[NSArray(GainValueLookup) cmi_isValidGainValueArray].cold.9
- -[NSArray(GainValueLookup) cmi_selectValueForGain:].cold.10
- -[NSArray(GainValueLookup) cmi_selectValueForGain:].cold.2
- -[NSArray(GainValueLookup) cmi_selectValueForGain:].cold.3
- -[NSArray(GainValueLookup) cmi_selectValueForGain:].cold.4
- -[NSArray(GainValueLookup) cmi_selectValueForGain:].cold.5
- -[NSArray(GainValueLookup) cmi_selectValueForGain:].cold.6
- -[NSArray(GainValueLookup) cmi_selectValueForGain:].cold.7
- -[NSArray(GainValueLookup) cmi_selectValueForGain:].cold.8
- -[NSArray(GainValueLookup) cmi_selectValueForGain:].cold.9
- -[NSMutableDictionary(Merge) cmi_nonDestructiveMergeEntriesFromDictionary:].cold.2
- -[RegWarpPP processParameters:inputImage:].cold.14
- -[RegWarpPP processParameters:inputImage:].cold.15
- GCC_except_table0
- _FigSignalErrorAt
- __PromotedConst.21
- __PromotedConst.22
- __Z20get_sgemm_sme_kernelN3sme4blas8SCALARFPES1_
- __Z20get_ssyrk_sme_kernelN3sme4blas8SCALARFPES1_
- __Z27get_sgemm_sme_packed_kernelN3sme4blas8SCALARFPES1_
- __Z27get_ssyrk_sme_packed_kernelN3sme4blas8SCALARFPES1_
- __Z27get_strsm_sme_packed_kernelN3sme4blas8SCALARFPE
- __Z8sme_gemvbllfPKflS0_lfPff
- __ZN12_GLOBAL__N_112syrkT_kernelIfEEvmmmN3sme4blas8SCALARFPES3_bllT_PKS4_lS4_PS4_lS7_S7_
- __ZN12_GLOBAL__N_120syrkN_incache_kernelIfEEvN3sme4blas8SCALARFPES3_bllT_PKS4_lS4_PS4_l
- __ZN12_GLOBAL__N_121sme_transpose_alignedIfLb0EEEvllPKT_lPS1_l
- __ZN12_GLOBAL__N_121sme_transpose_alignedIfLb1EEEvllPKT_lPS1_l
- __ZN12_GLOBAL__N_122gemm_nn_incache_kernelIfEEvN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_lS7_
- __ZN12_GLOBAL__N_122gemm_nt_incache_kernelIfEEvN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_l
- __ZN12_GLOBAL__N_122gemm_tn_incache_kernelIfEEvN3sme4blas8SCALARFPES3_mmmlllT_PKS4_lS6_lS4_PS4_lS7_S7_
- __ZN12_GLOBAL__N_122gemm_tt_incache_kernelIfEEvN3sme4blas8SCALARFPES3_mlllT_PKS4_lS6_lS4_PS4_lS7_
- __ZN12_GLOBAL__N_124repack_unaligned_alignedIfLb0EEEvllPKT_lPS1_l
- __ZN12_GLOBAL__N_124trsm_blocked_left_kernelIfEEvN3sme4blas8SCALARFPEbbbllT_PKS4_lPS4_lllS7_S7_S7_S7_
- __ZN12_GLOBAL__N_125syrkN_outsidecache_kernelIfEEvmmmN3sme4blas8SCALARFPES3_bllT_PKS4_lS4_PS4_lS7_S7_
- __ZN12_GLOBAL__N_125trsm_blocked_right_kernelIfEEvN3sme4blas8SCALARFPEbbbllT_PKS4_lPS4_lllS7_S7_S7_S7_
- __ZN12_GLOBAL__N_127gemm_nn_outsidecache_kernelIfEEvbmmmN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_lS7_S7_
- __ZN12_GLOBAL__N_127gemm_nt_outsidecache_kernelIfEEvbmmmN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_lS7_S7_
- __ZN12_GLOBAL__N_127gemm_tn_outsidecache_kernelIfEEvbN3sme4blas8SCALARFPES3_mmmlllT_PKS4_lS6_lS4_PS4_lS7_S7_
- __ZN12_GLOBAL__N_127gemm_tt_outsidecache_kernelIfEEvbmmmN3sme4blas8SCALARFPES3_lllT_PKS4_lS6_lS4_PS4_lS7_S7_
- __ZN3sme10production10apply_betaIfLy0EEEvllT_PS2_l
- __ZN3sme10production10apply_betaIfLy1EEEvllT_PS2_l
- __ZN3sme10production10apply_betaIfLy2EEEvllT_PS2_l
- __ZN3sme10production10apply_betaIfLy3EEEvllT_PS2_l
- __ZN3sme10production13gemm_internalIfLb0ELi0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13gemm_internalIfLb0ELi1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13gemm_internalIfLb0ELi2EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13gemm_internalIfLb0ELi3EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13gemm_internalIfLb0ELi4EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13gemm_internalIfLb1ELi0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13gemm_internalIfLb1ELi1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13gemm_internalIfLb1ELi2EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13gemm_internalIfLb1ELi3EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13gemm_internalIfLb1ELi4EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb0ELi0EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb0ELi1EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb0ELi2EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb0ELi3EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb0ELi4EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb1ELi0EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb1ELi1EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb1ELi2EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb1ELi3EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production13syrk_internalIfLb1ELi4EEEvbllT_PKS2_lS2_PS2_l
- __ZN3sme10production15load_apply_betaIfLy0EEEvllT_PS2_l
- __ZN3sme10production19load_apply_beta_1x2IfLb1ELy0EEEvllT_PS2_l
- __ZN3sme10production19load_apply_beta_1x4IfLb0ELy0EEEvllT_PS2_l
- __ZN3sme10production19load_apply_beta_1x4IfLb1ELy0EEEvllT_PS2_l
- __ZN3sme10production19syrk_lower_dispatchIfLb0EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production19syrk_upper_dispatchIfLb0EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production20gemm_worker_dispatchIfLb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production20gemm_worker_dispatchIfLb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production20gemm_worker_dispatchIfLb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production21sme_trans_pack_singleEllPKflPf
- __ZN3sme10production21sme_transpose_alignedEllPKflPfl
- __ZN3sme10production23trsm_left_lower_fms_1x2IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x2IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x2IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x2IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x2IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x2IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x2IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x2IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x4IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x4IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x4IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x4IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x4IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x4IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x4IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_lower_fms_1x4IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x2IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x2IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x2IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x2IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x2IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x2IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x2IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x2IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x4IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x4IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x4IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x4IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x4IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x4IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x4IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production23trsm_left_upper_fms_1x4IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production24blocked_left_trsm_packedIfLb0ELi1EEEvbbllT_PKS2_PS2_lS5_
- __ZN3sme10production24blocked_left_trsm_packedIfLb0ELi3EEEvbbllT_PKS2_PS2_lS5_
- __ZN3sme10production24blocked_left_trsm_packedIfLb1ELi1EEEvbbllT_PKS2_PS2_lS5_
- __ZN3sme10production24blocked_left_trsm_packedIfLb1ELi3EEEvbbllT_PKS2_PS2_lS5_
- __ZN3sme10production24gemm_worker_1xN_dispatchIfLb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production24gemm_worker_1xN_dispatchIfLb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production24gemm_worker_Mx1_dispatchIfLb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production24gemm_worker_Mx1_dispatchIfLb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production24sme_no_trans_pack_singleEllPKflPf
- __ZN3sme10production24trsm_left_lower_dispatchIfLb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production24trsm_left_lower_dispatchIfLb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production24trsm_left_lower_dispatchIfLb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production24trsm_left_lower_dispatchIfLb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production24trsm_left_upper_dispatchIfLb0ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production24trsm_left_upper_dispatchIfLb0ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production24trsm_left_upper_dispatchIfLb1ELb0EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production24trsm_left_upper_dispatchIfLb1ELb1EEEvllPKT_S4_lS2_PS2_lS5_l
- __ZN3sme10production24trsm_right_lower_fms_2x1IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_2x1IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_2x1IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_2x1IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_2x1IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_2x1IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_2x1IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_2x1IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_4x1IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_4x1IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_4x1IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_4x1IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_4x1IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_4x1IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_4x1IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_lower_fms_4x1IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_2x1IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_2x1IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_2x1IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_2x1IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_2x1IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_2x1IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_2x1IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_2x1IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_4x1IfLb0ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_4x1IfLb0ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_4x1IfLb0ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_4x1IfLb0ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_4x1IfLb1ELb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_4x1IfLb1ELb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_4x1IfLb1ELb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production24trsm_right_upper_fms_4x1IfLb1ELb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production25blocked_right_trsm_packedIfLb0ELi1EEEvbbllT_PKS2_PS2_lS5_
- __ZN3sme10production25blocked_right_trsm_packedIfLb0ELi3EEEvbbllT_PKS2_PS2_lS5_
- __ZN3sme10production25blocked_right_trsm_packedIfLb1ELi1EEEvbbllT_PKS2_PS2_lS5_
- __ZN3sme10production25blocked_right_trsm_packedIfLb1ELi3EEEvbbllT_PKS2_PS2_lS5_
- __ZN3sme10production25gemm_alpha_beta_writebackIfLb0ELb0EEEvllT_S2_PS2_l
- __ZN3sme10production25gemm_alpha_beta_writebackIfLb0ELb1EEEvllT_S2_PS2_l
- __ZN3sme10production25gemm_alpha_beta_writebackIfLb1ELb0EEEvllT_S2_PS2_l
- __ZN3sme10production25gemm_alpha_beta_writebackIfLb1ELb1EEEvllT_S2_PS2_l
- __ZN3sme10production25syrk_alpha_beta_writebackIfLb0EEEvblT_S2_PS2_l
- __ZN3sme10production25syrk_alpha_beta_writebackIfLb1EEEvblT_S2_PS2_l
- __ZN3sme10production25trsm_right_lower_dispatchIfLb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production25trsm_right_lower_dispatchIfLb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production25trsm_right_lower_dispatchIfLb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production25trsm_right_lower_dispatchIfLb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production25trsm_right_upper_dispatchIfLb0ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production25trsm_right_upper_dispatchIfLb0ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production25trsm_right_upper_dispatchIfLb1ELb0EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production25trsm_right_upper_dispatchIfLb1ELb1EEEvllPKT_S4_lS2_PS2_l
- __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb0ELb0ELb0EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb0ELb0ELb1EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb0ELb1ELb0EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb0ELb1ELb1EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb1ELb0ELb1EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_lower_dispatch_fastpathIfLb1ELb1ELb1EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb0ELb0ELb0EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb0ELb0ELb1EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb0ELb1ELb0EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb0ELb1ELb1EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb1ELb0ELb1EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production28syrk_upper_dispatch_fastpathIfLb1ELb1ELb1EEEvllT_PKS2_lS2_PS2_l
- __ZN3sme10production29gemm_1xN_alpha_beta_writebackIfLb0EEEvllT_S2_PS2_l
- __ZN3sme10production29gemm_1xN_alpha_beta_writebackIfLb1EEEvllT_S2_PS2_l
- __ZN3sme10production29gemm_Mx1_alpha_beta_writebackIfLb0EEEvllT_S2_PS2_l
- __ZN3sme10production29gemm_Mx1_alpha_beta_writebackIfLb1EEEvllT_S2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb1ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb1ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb0ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production29gemm_worker_dispatch_fastpathIfLb1ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb1ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb1ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb0ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb1ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb1ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_1xN_dispatch_fastpathIfLb1ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb0ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb0ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb1ELb0ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb1ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb1ELb1ELb0EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb0ELb1ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb1ELb0ELb0ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production33gemm_worker_Mx1_dispatch_fastpathIfLb1ELb0ELb1ELb1EEEvlllT_PKS2_lS4_lS2_PS2_l
- __ZN3sme10production4trsmIfLi1EEEvbbbbllT_PKS2_PS2_lS5_
- __ZN3sme10production4trsmIfLi3EEEvbbbbllT_PKS2_PS2_lS5_
- __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL12gemvT_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvmllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_4xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvN_8xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_16xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_
- __ZN3sme4blasL17gemvN_32xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_
- __ZN4blas6memory13aligned_allocIfEENSt3__110unique_ptrIT_NS0_11custom_freeIS4_EEEEmm
- __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_0EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
- __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_1EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
- __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE1ELS2_3EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
- __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_0EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
- __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_1EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
- __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE2ELS2_3EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
- __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_0EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
- __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_1EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
- __ZZN3sme4blasL16gemvT_4xN_kernelIfLNS0_8SCALARFPE3ELS2_3EEEvllT_PKS3_lS5_S3_PS3_E16tabulaRasaSingle
- ___34-[CMIStyleEngineProcessor process]_block_invoke.496
- ___69-[CMITiledInferenceProcessor runWithTileCount:withCompletionHandler:]_block_invoke.300
- ___WritePixelBufferToFile_block_invoke_2
- ___arm_tpidr2_restore
- ___arm_tpidr2_save
- ___block_descriptor_56_e8_32s40w_e8_v16?08lw40l8s32l8
- ___block_literal_global.116
- ___block_literal_global.118
- ___block_literal_global.203
- ___block_literal_global.38
- ___block_literal_global.47
- ___block_literal_global.93
- ___gxx_personality_v0
- _do_abort
- _getBayerPatternForPixelBuffer.cold.1
- _rwppRegEngine_execute.cold.2
- _rwppRegEngine_reallocResources.cold.6
- _rwppRegEngine_reallocResources.cold.7
- _rwppRegEngine_reallocResources.cold.8
- _rwppRegEngine_reallocResources.cold.9
- _saxpby_base
- _saxpby_internal
- _sme_sgemm
- _sme_ssyrk
- _sme_strsm
- _sscal_internal
- _sset_internal
CStrings:
+ "  "
+ " '_inputLTMGainMapTextureMappedRegion' !=  input LTM Gain map image size"
+ " '_inputLightMapTextureMappedRegion' !=  input light map image size"
+ " '_inputLinearImageTextureMappedRegion' !=  input linear image size"
+ " '_inputLinearLightMapTextureMappedRegion' !=  input linear light map image size"
+ " '_inputPersonMaskTextureMappedRegion' !=  input person mask image size"
+ " '_inputSkinMaskTextureMappedRegion' !=  input skin mask image size"
+ " '_inputSkyMaskTextureMappedRegion' !=  input sky mask image size"
+ " '_outputImageTextureMappedRegion' !=  output image size"
+ " 'inputTextureMappedRegion' !=  input image size"
+ " | "
+ "%d"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "'imageSize' dimensions must be > 0"
+ "'inputImageRect' != input image size"
+ "'inputImageRect' and 'outputImageRect' do not intersect"
+ "'inputLinearSystemCoefficients' not set, required if processing type 'CMIStyleEngineProcessingTypeLearn' not set"
+ "'inputOriginalTexture' and 'inputDeltaMapTexture' cannot both be set for processing type 'CMIStyleEngineProcessingTypeApply'"
+ "'inputOriginalTexture' required if 'outputDeltaMapTexture' set for processing type 'CMIStyleEngineProcessingTypeApply'"
+ "'inputTexture' not set, required for processing type 'CMIStyleEngineProcessingTypeApply'"
+ "'inputThumbnailForIntegrationTexture' not set, required for processing type 'CMIStyleEngineProcessingTypeIntegration'"
+ "'inputThumbnailForLearningTexture' not set, required for processing type 'CMIStyleEngineProcessingTypeLearn'"
+ "'inputThumbnailForLearningTexture' size is smaller than size specified during prepareToProcess:"
+ "'inputThumbnailForLearningWeightsTexture' not set, required for processing type 'CMIStyleEngineProcessingTypeLearn'"
+ "'inputThumbnailForResidualCorrectionTexture' not set, required for processing type 'CMIStyleEngineProcessingTypeLearn'"
+ "'inputThumbnailForResidualCorrectionTexture' size is smaller than size specified during prepareToProcess:"
+ "'inputWeightPlaneTextures' array length does not match 'weightPlaneCount' set by configuration"
+ "'inputWeightPlaneTextures' size does not match 'inputThumbnailTexture'"
+ "'optionalInputImageRect' != optional input image size"
+ "'outputImageRect' != output image size"
+ "'outputLumaGradientTexture' size does not match output texture"
+ "'regionToRender' not contained within the intersection of 'inputImageRect' and 'outputImageRect'"
+ "'regionToRenderRect' not contained within the intersection of 'inputImageRect' and 'outputImageRect'"
+ "'targetThumbnailForLearningTexture' not set, required for processing type 'CMIStyleEngineProcessingTypeLearn'"
+ "'targetThumbnailForResidualCorrectionTexture' not set, required for processing type 'CMIStyleEngineProcessingTypeLearn'"
+ "( plane == 0 ) && ( slice == 0 ) is NULL"
+ "( slice == 0 ) is NULL"
+ "( slice == 0 ) || ( slice < IOSurfaceGetSliceCount( ioSurface ) ) is NULL"
+ "(External- %@)"
+ "(Fig)"
+ "(plane == 0) || (plane < IOSurfaceGetPlaneCount(ioSurface)) is NULL"
+ "*applyKernelPtr is NULL"
+ "++"
+ "+[CMIDistortionModel adjustCropRectangle:withGDCParams:]"
+ "+[CMIDistortionModel generateInverseScalingLUT:withGDCParams:]"
+ "+[CMIDistortionModel generateInverseScalingLUT:withGDCParams:metalCtx:]"
+ "+[CMIDistortionModel getGDCParams:cameraInfo:metadata:]"
+ "+[CMIMetalEventSynchronizer getSharedInstance]_block_invoke"
+ "+[CMINoiseModels _fpnrScalingFactor:darkCurrentNoiseCalibration:fpnrEnabled:]"
+ "+[CMINoiseModels _fpnrSpatialStdDev:darkCurrentNoiseCalibration:fpnrEnabled:]"
+ "+[CMISharpnessScore externalMemoryDescriptorForConfiguration:]"
+ "+[CMISmartStyleUtilitiesV1 computeLinearImageEncodingGainWithMetadata:]"
+ "+[CMISmartStyleUtilitiesV1 computeLinearImageExposureWithMetadata:outputBaseGain:outputBaselineExposure:]"
+ "+[CMISmartStyleUtilitiesV1 defaultStyleForCastType:]"
+ "+[CMISmartStyleUtilitiesV1 defaultStyleForCastType:]_block_invoke"
+ "+[CMISmartStyleUtilitiesV1 intermediateStyleRendererThumbnailSizeForUseCase:]"
+ "+[CMISmartStyleUtilitiesV1 makerNoteTagForSmartStyleCastType:smartStyleVersion:]"
+ "+[CMISmartStyleUtilitiesV1 makerNoteTagForSmartStyleTuningType:smartStyleVersion:]"
+ "+[CMISmartStyleUtilitiesV1 smartStyleCastForMakerNoteTag:smartStyleVersion:]"
+ "+[CMISmartStyleUtilitiesV1 smartStyleTuningForMakerNoteTag:smartStyleVersion:]"
+ "+[CMISubjectRelightingShared getSharedInstanceOrRelease:]"
+ "+[CMISubjectRelightingStage prewarmShaders:]"
+ "+[CMIVNRProcessor _productTypeFromMGGetProductType:]"
+ "+[CMIVNRProcessor getDefaultTuningParameters]"
+ "+[CMIVNRProcessor getTuningParametersForCurrentDevice]"
+ "+[FigRegWarpPPGPU prewarmShaders:]"
+ "+[FigRegWarpPPGPUShared getSharedInstanceOrRelease:]"
+ "+[RegWarpPP CheckParameters:imageWidth:imageHeight:imageFormat:]"
+ "+[RegWarpPP convertFromImageSizeToUnity:inMatrix:imgWidth:imgHeight:]"
+ "+[RegWarpPP convertFromUnityToImageSize:inMatrix:imgWidth:imgHeight:]"
+ ", "
+ "-1"
+ "-[CMIDistortionModel initWithGDCParams:]"
+ "-[CMIDistortionModel updateGDCParams:]"
+ "-[CMIFFTContext initWithDevice:]"
+ "-[CMIFFTContext initWithFigMetalContext:]"
+ "-[CMIFFTDimension initWithSize:iStride:oStride:primeFactors:]"
+ "-[CMIFFTEncode _encode1DBatchedGlobalSingleRadixTransform:inputBuffer:scratchBuffer:batchSize:depthBatchSize:bufferOffset:config:]"
+ "-[CMIFFTEncode _encode1DBatchedThreadgroupSingleRadixTransform:inputBuffer:scratchBuffer:batchSize:depthBatchSize:bufferOffset:config:typeStride:]"
+ "-[CMIFFTEncode initWithContext:]"
+ "-[CMIFFTExecutor _execute1DMixedRadix:dimension:layout:precision:direction:primeFactors:batchSize:]"
+ "-[CMIFFTExecutor _execute1DSingleRadix:dimension:layout:precision:direction:radix:batchSize:]"
+ "-[CMIFFTExecutor _execute1DTwoRadix:dimension:layout:precision:direction:primeFactors:batchSize:]"
+ "-[CMIFFTExecutor _execute2DTransform:dimensions:layout:precision:direction:]"
+ "-[CMIFFTExecutor initWithContext:]"
+ "-[CMIFFTTransformInternal initWithContext:nDim:sizes:istrides:ostrides:layout:precision:batchsize:]"
+ "-[CMIFlexGTCStage _compileShaders]"
+ "-[CMIFlexGTCStage computeFlexGTCWithSDRImage:gainMap:gainMapMetadata:config:cropRect:gainMapCropRect:]"
+ "-[CMIFlexGTCStage initWithOptionalCommandQueue:]"
+ "-[CMIImmutableSmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:]"
+ "-[CMIInferenceNetworkEspressoV1 allocateInstancesWithDevice:instanceCount:useTextureArrays:]"
+ "-[CMIInferenceNetworkEspressoV1 bindIOPortsWithInputNames:withOutputNames:]"
+ "-[CMIInferenceNetworkEspressoV2 _duplicateMainEsop:]"
+ "-[CMIInferenceNetworkEspressoV2 allocateInstancesWithDevice:instanceCount:useTextureArrays:]"
+ "-[CMIInferenceNetworkEspressoV2 bindIOPortsWithInputNames:withOutputNames:]"
+ "-[CMIInferenceNetworkEspressoV2 loadNetworkWithPath:]"
+ "-[CMIMetalEventSynchronizer _signalEventOnCommandBuffer:forKey:]"
+ "-[CMIMetalEventSynchronizer _signalEventOnCommandBuffer:forKey:]_block_invoke"
+ "-[CMIMetalEventSynchronizer _waitForEventOnCommandBuffer:forKey:]"
+ "-[CMIMetalResourceCache getBufferFromPixelBuffer:]"
+ "-[CMIMetalResourceCache getTextureFromPixelBuffer:planeIndex:pixelFormat:usage:]"
+ "-[CMIMetalResourceCache initWithMetalDevice:]"
+ "-[CMIRangeAllocator allocateWithSize:alignment:outputOffset:]"
+ "-[CMIRangeAllocator allocateWithSize:alignment:outputOffset:allocationHint:]"
+ "-[CMISRLHumanFace initWithFaceObject:]"
+ "-[CMISRLHumanFaceHistory filterSkinToneLevelsMedian]"
+ "-[CMISRLHumanFaceHistory filterSkinToneLevels]"
+ "-[CMISSIM _bindPixelBufferToTexture:usage:overrideFormat:planeIndex:lumaOnly:textuePtr:]"
+ "-[CMISSIM _encodeSSIMCalculation:imageA:imageB:outputSSIMMap:]"
+ "-[CMISSIM _encodeSSIMReduction:ssimMap:inPlace:outputSSIMVal:]"
+ "-[CMISSIM _loadKernel:name:functionConstants:]"
+ "-[CMISSIM _setupMetalContextWithCommandQueue:]"
+ "-[CMISSIM _validateConfiguration:]"
+ "-[CMISSIM calculateWithImageA:imageB:outputSSIMMap:outputSSIMVal:]"
+ "-[CMISSIM encodeToCommandBuffer:imageA:imageB:outputSSIMMap:outputSSIMVal:]"
+ "-[CMISSIM initWithOptionalCommandQueue:config:]"
+ "-[CMISSIMConfig init]"
+ "-[CMIShadingFPNCorrectionImage initWithCoder:]"
+ "-[CMISharpnessScore _blurImage:toImage:sourceComponent:binning:firstPixel:roi:]"
+ "-[CMISharpnessScore _calculateFromTexture:andFromRoi:sourceComponent:binning:firstPixel:toResult:]"
+ "-[CMISharpnessScore _computeClipValueWithHistogram:andRoi:toClipValue:]"
+ "-[CMISharpnessScore _computeSharpnessScore:outputTexture:sourceComponent:binning:firstPixel:roi:clipValueMetalBuffer:]"
+ "-[CMISharpnessScore calculateFromPixelBuffer:andFromRoi:sourceComponent:toResult:]"
+ "-[CMISharpnessScore initWithOptionalCommandQueue:externalMemoryResource:kernelWeights:]"
+ "-[CMISharpnessScore initWithOptionalCommandQueue:kernelWeights:]"
+ "-[CMISmartStyleColorCubePoolV1 _newColorCubeTextureWithLabel:]"
+ "-[CMISmartStyleColorCubePoolV1 newColorCube]"
+ "-[CMISmartStyleMetalRendererV1 _applyFinalRendering]"
+ "-[CMISmartStyleMetalRendererV1 _calculateCubicSplineToneCurve]"
+ "-[CMISmartStyleMetalRendererV1 _calculateDynamicRenderParameters]"
+ "-[CMISmartStyleMetalRendererV1 _calculateHistogramStatsWithImageTexture:linearImageTexture:personMaskTexture:skinMaskTexture:]"
+ "-[CMISmartStyleMetalRendererV1 _calculateHueSatLumLUTTexForAllCastTypesAndVariants]"
+ "-[CMISmartStyleMetalRendererV1 _checkROISpecificationForStatsCalculation]"
+ "-[CMISmartStyleMetalRendererV1 _checkROISpecification]"
+ "-[CMISmartStyleMetalRendererV1 _compileMetalShadersForProcessingType:]"
+ "-[CMISmartStyleMetalRendererV1 _convertLinearYCbCrToRGB:inputChromaTexture:outputRGBTexture:]"
+ "-[CMISmartStyleMetalRendererV1 _createGuideImageForInputTexture:outputGuideTexture:isInputLinear:isOutputLumaGuide:]"
+ "-[CMISmartStyleMetalRendererV1 _createGuideImage]"
+ "-[CMISmartStyleMetalRendererV1 _encodeImageReduction:inputTexture:inputROI:inputColorConversion:outputStatsBuffer:outputStatsBufferOffset:]"
+ "-[CMISmartStyleMetalRendererV1 _encodeLinear]"
+ "-[CMISmartStyleMetalRendererV1 _finalRenderRegion:]"
+ "-[CMISmartStyleMetalRendererV1 _newBufferWithLength:label:sharedAccess:]"
+ "-[CMISmartStyleMetalRendererV1 _newTexture2DWithFormat:width:height:usage:disableCompression:label:retainUntilPurge:useFigMetalAllocator:]"
+ "-[CMISmartStyleMetalRendererV1 _populatePreComputedStats:inputStatisticsByStatsType:inputStatisticsByStatsKey:]"
+ "-[CMISmartStyleMetalRendererV1 _populateStaticRenderParametersFromTuning:inputStatisticsByStatsKey:]"
+ "-[CMISmartStyleMetalRendererV1 _processLTMGainMap]"
+ "-[CMISmartStyleMetalRendererV1 _processSegmentationMasks]"
+ "-[CMISmartStyleMetalRendererV1 _releaseIntermediateResources]"
+ "-[CMISmartStyleMetalRendererV1 _runImageReductionAndUpdateBaseGain:]"
+ "-[CMISmartStyleMetalRendererV1 _setupStatsAndRenderParamBuffer]"
+ "-[CMISmartStyleMetalRendererV1 _updateRenderPipelineConfigForInputs]"
+ "-[CMISmartStyleMetalRendererV1 _upsampleLightMap]"
+ "-[CMISmartStyleMetalRendererV1 dealloc]"
+ "-[CMISmartStyleMetalRendererV1 initWithMetalContext:]"
+ "-[CMISmartStyleMetalRendererV1 inputLinearImageGainDownRatio]"
+ "-[CMISmartStyleMetalRendererV1 inputLinearImageRGBTexture]"
+ "-[CMISmartStyleMetalRendererV1 prewarm]"
+ "-[CMISmartStyleMetalRendererV1 process]"
+ "-[CMISmartStyleMetalRendererV1 setInputLinearImageGainDownRatio:]"
+ "-[CMISmartStyleMetalRendererV1 setInputLinearImageRGBTexture:]"
+ "-[CMISmartStyleMetalRendererV1 setInputStyle:]"
+ "-[CMISmartStyleMetalRendererV1 setup]"
+ "-[CMISmartStylePixelBufferRendererV1 _bindPixelBufferToTexture:usage:overrideMTLPixelFormatWithFormat:planeIndex:texturePtr:]"
+ "-[CMISmartStylePixelBufferRendererV1 _createGlobalToneCurveTexture]"
+ "-[CMISmartStylePixelBufferRendererV1 dealloc]"
+ "-[CMISmartStylePixelBufferRendererV1 finishProcessing]"
+ "-[CMISmartStylePixelBufferRendererV1 initWithOptionalMetalCommandQueue:allocator:]"
+ "-[CMISmartStylePixelBufferRendererV1 process]"
+ "-[CMISmartStylePixelBufferRendererV1 purgeResources]"
+ "-[CMISmartStylePixelBufferRendererV1 setInputGainMapPixelBuffer:]"
+ "-[CMISmartStylePixelBufferRendererV1 setup]"
+ "-[CMISmartStyleProxyRendererV1 _allocateParamsAndStatsBuffers]"
+ "-[CMISmartStyleProxyRendererV1 _bindInputPixelBuffersAsTextures]"
+ "-[CMISmartStyleProxyRendererV1 _bindPixelBufferToTexture:usage:overrideMTLPixelFormatWithFormat:planeIndex:texturePtr:]"
+ "-[CMISmartStyleProxyRendererV1 _calculateCubicSplineToneCurve]"
+ "-[CMISmartStyleProxyRendererV1 _calculateDynamicRenderParameters]"
+ "-[CMISmartStyleProxyRendererV1 _calculateHueSatLumLUTTexForAllCastTypesAndVariants]"
+ "-[CMISmartStyleProxyRendererV1 _compileMetalShadersForProcessingType:]"
+ "-[CMISmartStyleProxyRendererV1 _generateColorCubes]"
+ "-[CMISmartStyleProxyRendererV1 _newTexture2DWithFormat:width:height:usage:disableCompression:label:retainUntilPurge:useFigMetalAllocator:]"
+ "-[CMISmartStyleProxyRendererV1 _populateStaticRenderParameters:forInputStyle:fromTuning:]"
+ "-[CMISmartStyleProxyRendererV1 _renderWithColorCubes]"
+ "-[CMISmartStyleProxyRendererV1 _renderWithColorPriors]"
+ "-[CMISmartStyleProxyRendererV1 _updateColorCubeCache]"
+ "-[CMISmartStyleProxyRendererV1 _updateColorCubesFromTuning:]"
+ "-[CMISmartStyleProxyRendererV1 _updateStatsBuffer]"
+ "-[CMISmartStyleProxyRendererV1 dealloc]"
+ "-[CMISmartStyleProxyRendererV1 initWithOptionalMetalCommandQueue:]"
+ "-[CMISmartStyleProxyRendererV1 prepareToProcess:]"
+ "-[CMISmartStyleProxyRendererV1 process]"
+ "-[CMISmartStyleProxyRendererV1 setup]"
+ "-[CMISmartStyleUtilitiesV1 _setupStyleEngineForUseCase:useFloat16Coefficients:]"
+ "-[CMISmartStyleUtilitiesV1 computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficients:outputDeltaMapPixelBuffer:]"
+ "-[CMISmartStyleUtilitiesV1 computeDeltaMapForSourcePixelBuffer:targetPixelBuffer:coefficientsDict:outputDeltaMapPixelBuffer:]"
+ "-[CMISmartStyleUtilitiesV1 computeOriginalUnstyledPixelBufferFrom:inputDeltaMapPixelBuffer:inputCoefficientsPixelBuffer:outputUnstyledPixelBuffer:]"
+ "-[CMISmartStyleUtilitiesV1 computeOriginalUnstyledPixelBufferFrom:inputDeltaMapPixelBuffer:inputMetadataDict:outputUnstyledPixelBuffer:]"
+ "-[CMISmartStyleUtilitiesV1 interpolateCoefficientsFromStartFrameMetadataDict:startFrameTime:endFrameMetadataDict:endFrameTime:frameTimesToInterpolate:]"
+ "-[CMISmartStyleUtilitiesV1 learnTransformFrom:to:outputCoefficients:outputIntegratedCoefficients:]"
+ "-[CMISmartStyleV1 initWithCastType:castIntensity:toneBias:colorBias:]"
+ "-[CMISmartStyleV1 init]"
+ "-[CMISmartStyleV1 setCastIntensity:]"
+ "-[CMISmartStyleV1 setCastType:]"
+ "-[CMISmartStyleV1 setColorBias:]"
+ "-[CMISmartStyleV1 setToneBias:]"
+ "-[CMIStatistics getStatisticsFromPixelBuffer:withRoi:toResult:withOptionalChannelConfig:]"
+ "-[CMIStatistics getStatisticsFromTexture:withRoi:toResult:withOptionalChannelConfig:]"
+ "-[CMIStatistics initWithOptionalCommandQueue:]"
+ "-[CMIStyleEngineApplyStyle _compileShaders:]"
+ "-[CMIStyleEngineApplyStyle enqueueToCommandBuffer:]"
+ "-[CMIStyleEngineCoefficientConverter _compileShaders:]"
+ "-[CMIStyleEngineCoefficientConverter enqueueToCommandBuffer:]"
+ "-[CMIStyleEngineCoefficientsFilter _calculateGlobalRemixFactorForWindow:filteredWindow:remixFactor:]"
+ "-[CMIStyleEngineCoefficientsFilter filterCoefficientsFIR:forPts:to:]"
+ "-[CMIStyleEngineCoefficientsFilter filterCoefficientsIIR:filteredDataWindow:filterType:to:]"
+ "-[CMIStyleEngineCoefficientsProcessor _bindPixelBuffer:toBuffer:]"
+ "-[CMIStyleEngineCoefficientsProcessor enqueueCoefficientsForFiltering:withMetadata:pts:learnedStyle:]"
+ "-[CMIStyleEngineCoefficientsProcessor filterCoefficientsForFrameWithMetadata:pts:filterType:toPixelBuffer:toGlobalRemixFactor:]"
+ "-[CMIStyleEngineCoefficientsProcessor initWithBufferCount:coefficientsSynchronization:andOptionalMetalCommandQueue:]"
+ "-[CMIStyleEngineCoefficientsRingBuffer add:]"
+ "-[CMIStyleEngineCoefficientsRingBuffer getFramesDataWindowFrom:to:shouldRemoveOldData:forStyle:]"
+ "-[CMIStyleEngineCoefficientsRingBuffer initWithCapacity:]"
+ "-[CMIStyleEngineCoefficientsRingBuffer releaseResources]"
+ "-[CMIStyleEngineCoefficientsRingBuffer reset]"
+ "-[CMIStyleEngineCreateLinearSystem _compileShaders:]"
+ "-[CMIStyleEngineCreateLinearSystem _setWeightPlane:term:priorScaleFactor:]"
+ "-[CMIStyleEngineCreateLinearSystem enqueueToCommandBuffer:]"
+ "-[CMIStyleEngineCreateSpotlights _compileShaders:]"
+ "-[CMIStyleEngineCreateSpotlights enqueueToCommandBuffer:]"
+ "-[CMIStyleEngineCreateWeightPlanes _compileShaders:]"
+ "-[CMIStyleEngineCreateWeightPlanes enqueueToCommandBuffer:]"
+ "-[CMIStyleEngineDownScaler _compileShaders:]"
+ "-[CMIStyleEngineDownScaler enqueueToCommandBuffer:]"
+ "-[CMIStyleEngineIdentityCoefficientCreator _compileShaders:]"
+ "-[CMIStyleEngineIdentityCoefficientCreator enqueueToCommandBuffer:]"
+ "-[CMIStyleEngineIntegrateCoefficients _compileShaders:]"
+ "-[CMIStyleEngineIntegrateCoefficients _createSamplers:]"
+ "-[CMIStyleEngineIntegrateCoefficients enqueueToCommandBuffer:]"
+ "-[CMIStyleEngineProcessor _allocatePermanentResources]"
+ "-[CMIStyleEngineProcessor _bindAllInternalIOBuffers:]"
+ "-[CMIStyleEngineProcessor _bindAllInternalIOTextures:]"
+ "-[CMIStyleEngineProcessor _bindAllInternalYUVTextures:]"
+ "-[CMIStyleEngineProcessor _bindPixelBuffer:toBuffer:]"
+ "-[CMIStyleEngineProcessor _bindPixelBufferToTexture:usage:texturePtr:plane:]"
+ "-[CMIStyleEngineProcessor _bindTexture:toBuffer:]"
+ "-[CMIStyleEngineProcessor _bindYUV420PixelBufferToTextures:usage:lumaTexturePtr:chromaTexturePtr:]"
+ "-[CMIStyleEngineProcessor _checkConfigurationForTexture:buffers:]"
+ "-[CMIStyleEngineProcessor _checkIOTexturePair:]"
+ "-[CMIStyleEngineProcessor _checkIntegrationThumbnailTexture:]"
+ "-[CMIStyleEngineProcessor _checkLearningThumbnailTexturePair:]"
+ "-[CMIStyleEngineProcessor _checkLearningWeightThumbnailTexture:]"
+ "-[CMIStyleEngineProcessor _checkROISpecification:]"
+ "-[CMIStyleEngineProcessor _checkResidualCorrectionThumbnailTexturePair:]"
+ "-[CMIStyleEngineProcessor _createMetalStages]"
+ "-[CMIStyleEngineProcessor _setTuningParameters]"
+ "-[CMIStyleEngineProcessor dealloc]"
+ "-[CMIStyleEngineProcessor downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:filter:copyAttachments:gdcParams:]"
+ "-[CMIStyleEngineProcessor downScaleInputTexture:withInputCropRect:usingBoxSize:toOutputTexture:filter:gdcParams:]"
+ "-[CMIStyleEngineProcessor externalMemoryDescriptorForConfiguration:]"
+ "-[CMIStyleEngineProcessor finishProcessing]"
+ "-[CMIStyleEngineProcessor initWithOptionalMetalCommandQueue:withCoefficientSynchronization:]"
+ "-[CMIStyleEngineProcessor outputLinearSystemCoefficients]"
+ "-[CMIStyleEngineProcessor prepareToProcess:]"
+ "-[CMIStyleEngineProcessor prewarm]"
+ "-[CMIStyleEngineProcessor process]"
+ "-[CMIStyleEngineProcessor purgeResources]"
+ "-[CMIStyleEngineProcessor resetState]"
+ "-[CMIStyleEngineProcessor setup]"
+ "-[CMIStyleEngineSolveLinearSystem _compileShaders:]"
+ "-[CMIStyleEngineSolveLinearSystem enqueueToCommandBuffer:]"
+ "-[CMIStyleEngineSolveLinearSystemAccelerate _prewarmSolverRoutine]"
+ "-[CMIStyleEngineSolveLinearSystemAccelerate solveLinearSystem:]"
+ "-[CMIStyleEngineSolveLinearSystemGPU _compileSubClassShaders:]"
+ "-[CMIStyleEngineSolveLinearSystemGPU solveLinearSystem:]"
+ "-[CMIStyleEngineSolveLinearSystemMPS solveLinearSystem:]"
+ "-[CMISubjectRelightingShaders initWithMetalContext:]"
+ "-[CMISubjectRelightingShared getShaders:]"
+ "-[CMISubjectRelightingStage _copyCoeffsBufferWhenReady:]_block_invoke"
+ "-[CMISubjectRelightingStage _runSubjectRelighting:rgba:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:expBias:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:isChromaGainAdjusted:inputIsLinear:chromaBias:blackPoint:playBackCurve:]"
+ "-[CMISubjectRelightingStage initWithMetalContext:]"
+ "-[CMIVNRProcessor dealloc]"
+ "-[CMIVNRProcessor finishProcessing]"
+ "-[CMIVNRProcessor initWithCommandQueue:]"
+ "-[CMIVNRProcessor metalCommandBuffer]"
+ "-[CMIVNRProcessor prepareToProcess:]"
+ "-[CMIVNRProcessor prepareToProcess:prepareDescriptor:]"
+ "-[CMIVNRProcessor prewarm]"
+ "-[CMIVNRProcessor process]"
+ "-[CMIVNRProcessor purgeResources]"
+ "-[CMIVNRProcessor resetState]"
+ "-[CMIVNRProcessor setup]"
+ "-[CMIVNRProcessor waitUntilScheduledWithWorkloadName:]"
+ "-[CMIVNRProcessor(DeghostPropagate) propagateDeghostingScoresDownPyramid:]"
+ "-[CMIVNRProcessor(Fusion) fuseWithInputPyramid:deghostPyramid:previousOutputPyramid:outputPyramid:inputLuma:inputChroma:previousOutputLuma:previousOutputChroma:outputLuma:outputChroma:frameIdx:]"
+ "-[CMIVNRProcessor(PyramidGen) fillInputPyramid:previousOutputPyramid:deghostPyramid:inputLuma:inputChroma:previousOutputLuma:previousOutputChroma:]"
+ "-[CMIVNRProcessor(TextureBinding) bindTextureToPixelBuffer:plane:metalPixelFormat:usage:]"
+ "-[CMIWarpStage _compileShaders]"
+ "-[CMIWarpStage runGDC:outputTex:warpConfig:gdcParams:inverseGDC:]"
+ "-[CMIWarpStage runGDCWithInputLuma:inputChromaTex:outputLumaTex:outputChromaTex:warpConfig:gdcParams:inverseGDC:]"
+ "-[CMIWarpStage runWarpUsingTransform:inputBayerTex:firstPix:outputRGBTex:]"
+ "-[CMIWarpStage runWarpUsingTransform:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:inputFrameGDCParams:outputFrameGDCParams:]"
+ "-[CMIWarpStage runWarpUsingTransform:inputTex:outputTex:inputFrameGDCParams:outputFrameGDCParams:]"
+ "-[CMMTLCommandBuffer initWithCMMTLCommandQueue:unretained:]"
+ "-[CMMTLCommandQueue initWithCMMTLDevice:]"
+ "-[CMMTLCommandQueue initWithCMMTLDevice:descriptor:]"
+ "-[CMMTLCommandQueue initWithCMMTLDevice:maxCommandBufferCount:]"
+ "-[CMMTLDevice initWithLevel:]"
+ "-[FigM2MController _transform:srcRect:dst:dstRect:symmetricTransform:sync_m2m:]"
+ "-[FigM2MController init]"
+ "-[FigM2MController queryCapabilities]"
+ "-[FigM2MController transform:srcRect:dst:sync_m2m:]"
+ "-[FigMetalAllocator addExternalMetalBuffer:atSubAllocatorID:]"
+ "-[FigMetalAllocator forgoOwnership:]"
+ "-[FigMetalAllocator initWithDevice:allocatorType:]"
+ "-[FigMetalAllocator largestOccupiedOffset:]"
+ "-[FigMetalAllocator memSize:]"
+ "-[FigMetalAllocator newBufferDescriptor:]"
+ "-[FigMetalAllocator newBufferWithDescriptor:]"
+ "-[FigMetalAllocator newBufferWithDescriptor:subAllocatorID:]"
+ "-[FigMetalAllocator newTextureDescriptor:]"
+ "-[FigMetalAllocator newTextureWithDescriptor:]"
+ "-[FigMetalAllocator newTextureWithDescriptor:subAllocatorID:]"
+ "-[FigMetalAllocator purgeResources:]"
+ "-[FigMetalAllocator reset:]"
+ "-[FigMetalAllocator setForceDisableCompression:]"
+ "-[FigMetalAllocator setupWithDescriptor:]"
+ "-[FigMetalAllocator setupWithDescriptor:allocatorBackend:]"
+ "-[FigMetalAllocator usedSize:]"
+ "-[FigMetalAllocatorBackend initWithDevice:allocatorType:]"
+ "-[FigMetalAllocatorBackend makeBufferAliasable:]"
+ "-[FigMetalAllocatorBackend makeTextureAliasable:]"
+ "-[FigMetalAllocatorBackend newBufferWithDescriptor:sizeAlign:]"
+ "-[FigMetalAllocatorBackend newTextureWithDescriptor:sizeAlign:]"
+ "-[FigMetalAllocatorBackend setupWithDescriptor:]"
+ "-[FigMetalAllocatorBackend setupWithDescriptor:allocatorBackend:]"
+ "-[FigMetalAllocatorMetadata initWithFigMetalAllocator:]"
+ "-[FigMetalBufferAllocator bufferOffset:]"
+ "-[FigMetalBufferAllocator getSizeAndAlignForBufferDescriptor:]"
+ "-[FigMetalBufferAllocator initWithMetalUtils:]"
+ "-[FigMetalBufferAllocator newBufferWithDescriptor:offset:]"
+ "-[FigMetalBufferAllocator setupWithDescriptor:]"
+ "-[FigMetalContext CreateMetalTextureFromFile:pixelFormat:usage:width:height:]"
+ "-[FigMetalContext ReadMetalTextureFromFile:texture:mipmapLevel:]"
+ "-[FigMetalContext WriteMetalTextureToFile:texture:mipmapLevel:]"
+ "-[FigMetalContext _identifyGPU]"
+ "-[FigMetalContext bindIOSurfaceToMTL2DTexture:pixelFormat:usage:width:height:plane:slice:]"
+ "-[FigMetalContext bindPixelBufferToMTL2DTexture:pixelFormat:usage:plane:slice:]"
+ "-[FigMetalContext bindPixelBufferToMTL2DTexture:pixelFormat:usage:plane:slice:widthAlignmentFactor:heightAlignmentFactor:]"
+ "-[FigMetalContext bindPixelBufferToMTL2DTexture:pixelFormat:usage:textureSize:plane:slice:]"
+ "-[FigMetalContext bindPixelBufferToMTLBuffer:]"
+ "-[FigMetalContext commonInitWithOptionalCommandQueue:]"
+ "-[FigMetalContext computePipelineStateFor:constants:]"
+ "-[FigMetalContext create2DTextureFromBuffer:offset:stride:width:height:format:usage:]"
+ "-[FigMetalContext initRangeVertex]"
+ "-[FigMetalContext initWithFigMetalContext:andOptionalCommandQueue:]"
+ "-[FigMetalContext initWithLibraryData:ofSize:andOptionalCommandQueue:]"
+ "-[FigMetalContext initWithbundle:andOptionalCommandQueue:]"
+ "-[FigMetalContext initWithoutLibraryUsingOptionalCommandQueue:]"
+ "-[FigMetalContext init]"
+ "-[FigMetalContext prewarmInternalMetalShadersForFormatsList:]"
+ "-[FigMetalContext rebindTex:format:usage:plane:slice:xFactor:]"
+ "-[FigMetalContext setQueuePriority:]"
+ "-[FigMetalExecutionStatus init]"
+ "-[FigMetalHeapAllocator initWithMetalUtils:]"
+ "-[FigMetalHeapAllocator newTextureWithDescriptor:offset:]"
+ "-[FigMetalHeapAllocator setupWithDescriptor:]"
+ "-[FigMetalNoAliasingAllocator initWithMetalUtils:]"
+ "-[FigMetalTextureDescriptor init]"
+ "-[FigMetalTextureStub initWithDescriptor:]"
+ "-[FigMetalUtils texture2DFromBuffer:width:height:format:offset:usage:]"
+ "-[FigRegToolboxGPU allocateResources:imageWidth:imageHeight:gridWidth:gridHeight:templateRadius:searchRadius:minNCCThreshold:]"
+ "-[FigRegToolboxGPU computeTransform:transform:outputCorners:solverSelector:histogram:roi:]"
+ "-[FigRegToolboxGPU computeTransformInternal:solverKernel:solverOutputResults:histogram:roi:waitForCompletion:]"
+ "-[FigRegToolboxGPU initWithCommandQueue:]"
+ "-[FigRegToolboxGPU processReferenceImage:histogram:doWaitForIdle:]"
+ "-[FigRegToolboxGPU specialImageConverterA:outTexture1:outTexture2:outTexture3:doWaitForIdle:]"
+ "-[FigRegToolboxGPU warpTargetImage:outTexChma:inTexLuma:inTexChma:solverSelector:histogram:roi:doWaitForIdle:]"
+ "-[FigRegWarpPPGPU _detectCorners:roi:corners:pyrLevel:]"
+ "-[FigRegWarpPPGPU _determineNumPyrLevels:pyramid0Height:]"
+ "-[FigRegWarpPPGPU _newBufferWithLength:options:label:]"
+ "-[FigRegWarpPPGPU allocateResourcesWithWidth:height:]"
+ "-[FigRegWarpPPGPU computeHomography:referenceKeypoints:nonReferenceKeypoints:keypointsCount:]"
+ "-[FigRegWarpPPGPU processNonReferenceTexture:gdcParams:outputTransform:mapping:]"
+ "-[FigRegWarpPPGPU processReferenceTexture:gdcParams:regionOfInterest:numKeypoints:mapping:]"
+ "-[FigRegWarpPPGPUShaders initWithMetalContext:]"
+ "-[FigRegWarpPPGPUShared getShaders:]"
+ "-[FigRegWarpPPGPUTuningParams getMinCornerResponseThreshold:forBand:]"
+ "-[FigRegWarpPPGPUTuningParams readPlist:]"
+ "-[GDCTransform _legacyParametersToUniforms:withScale:andMode:]"
+ "-[GDCTransform initWithOptionalCommandQueue:]"
+ "-[GDCTransform transformFrom:to:withParameters:withScale:withMode:andCommandBuffer:]"
+ "-[NSArray(GainValueLookup) cmi_interpolateValueForGain:]"
+ "-[NSArray(GainValueLookup) cmi_isValidGainValueArray]"
+ "-[NSArray(GainValueLookup) cmi_selectValueForGain:]"
+ "-[NSMutableDictionary(Merge) cmi_nonDestructiveMergeEntriesFromDictionary:]"
+ "-[RegWarpPP allocateResources:imageHeight:imageFormat:externalMemory:externalMemorySize:]"
+ "-[RegWarpPP calculateHistEqLUT:fromHistogram:]"
+ "-[RegWarpPP calculateTotalCornerStrength:regionOfInterest:mapping:outTotalCornerStrength:]"
+ "-[RegWarpPP computeHomography:referenceKeypoints:nonReferenceKeypoints:keypointsCount:]"
+ "-[RegWarpPP getNonReferenceKeypoints:]"
+ "-[RegWarpPP getNormalizedPoints:numPairs:]"
+ "-[RegWarpPP getReferenceKeypoints:]"
+ "-[RegWarpPP initWithConfig:]"
+ "-[RegWarpPP processNonReference:gdcParams:seedTransform:outputTransform:mapping:]"
+ "-[RegWarpPP processParameters:inputImage:]"
+ "-[RegWarpPP processReference:gdcParams:regionOfInterest:numKeypoints:mapping:]"
+ "-[RegWarpPP releaseResources]"
+ "-[SSCHistogram _initShaders]"
+ "-[SSCHistogram singleComponentGPUHistogramInputPixelBuffer:validRect:outputHistogram:optionalChannelConfig:]"
+ "-[SSCHistogram singleComponentGPUHistogramInputTexture:validRect:outputHistogram:optionalChannelConfig:]"
+ "-[VNRGainValueArray initWithArray:]"
+ "-[VNRGainValueArray interpolateValueForGain:]"
+ "-[VNRPyramid initWithMetalDevice:isForDeghosting:width:height:nLumaLevels:nChromaLevels:lumaStartingLevel:chromaStartingLevel:]"
+ "-[VNRShaders createFusionShaderUsingMetalDevice:colorChannel:isFirstFrame:isTopBand:isBottomBand:]"
+ "-[VNRShaders initWithMetalDevice:]"
+ "-[VNRTuning initWithTuningParamsDict:]"
+ "-[VNRTuning updateWithGain:]"
+ "-[VNRTuningBand initWithTuningParamsDict:]"
+ "-[VNRTuningBand updateWithGain:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: CMIFFTContext is invalid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DBatched"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::StockhamMetal1DThreadgroup"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::applyTwiddles"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::realToComplexShim"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer2D"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::transposeBuffer3D"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not create pipeline sate for CMIFFT::unscrambleMixedRadix"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not get global FFT butterfly shader for radix:%zu precision:%d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTEncode.m %s: Could not initialise CMIFFTEncode object"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTContext is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: CMIFFTEncode object is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not allocate toDecrementFig array"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTDimension object"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Could not initialise CMIFFTExecutor object"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float layout type not valid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal float precision type not valid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal layout type is not valid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type is not valid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Executor/CMIFFTExecutor.m %s: Metal precision type not valid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTContext.m %s: Could not allocate CMIFFTContext super object"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIFFT/Interface/CMIFFTTransform.m %s: Could not initialise CMIFFTTransformInternal object"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing AGC"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing DarkCurrentTemperatureModelScaling"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ExposureTime"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionScalingFactor"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing FixedPatternNoiseReductionSpatialStdDev"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameAGC"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameExposureTime"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSensorTemperature"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing ReferenceDarkFrameSpatialStdDev"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMINoiseModels/CMINoiseModels.m %s: Metadata missing SensorTemperature"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: constantValues is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/CMISharpnessScore.m %s: externalMemoryDescriptor is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Can't determine MTLPixelFormats for binding to CVPixelBuffer - unsupported input pixel format = %c%c%c%c"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Failed to determine first pixel for versatile format"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unable to determine the first pixel type. Unsupported bayer input pixel format = %c%c%c%c"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMISharpnessScore/Common/CMICommon.m %s: Unrecognized BayerPattern: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV1.m %s: _allocateTexturesWithDevice failed %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV1.m %s: _getInfoFromNetwork failed %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV1.m %s: espresso_create_context return NULL."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV2.m %s: _allocateTexturesWithDevice failed %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV2.m %s: _createEventsWithDevice failed %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV2.m %s: _duplicateMainEsop failed %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV2.m %s: _getInfoFromEsop failed %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV2.m %s: _loadEsopWithPath failed %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV2.m %s: e5rt_tensor_desc_get_shape failed %s, %s."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMIInferenceDevice/CMIInferenceDeviceEspressoV2.m %s: getIOPort failed, %d."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMITiledInferenceProcessor.m"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMIWarpStage/CMIWarpStage.m %s: constantValues is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CMIResourceCache"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create CVMetalTextureCache"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create buffer from cache"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create residency set"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/GPUSupport/CMIMetalResourceCache.m %s: Unable to create texture from cache"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/ModuleCalibration/CMIShadingFPNCorrectionImage.m %s: Mismatch between encoded metadata and file system metadata. Encoded:%@. File system:%@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/RegWarpPP.m %s: Failed to compute forwardHmgrTransform from seed transform. Using identify matrix instead"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/RegWarpPP.m %s: RegWarpPP(_regEng) not initialized!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/RegWarpPP.m %s: _mtGroup is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/RegWarpPP.m %s: imageFormat (%x) is not supported"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/RegWarpPP.m %s: imageHeight is out of range %u <= %u <= 65535"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/RegWarpPP.m %s: imageWidth is out of range %u <= %u <= 65535"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/RegWarpPP.m %s: pyramidLevel0Height=%u < %u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/RegWarpPP.m %s: pyramidLevel0Width=%u < %u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/RegWarpPP.m %s: rwppRegEngine_init failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppGeomTransform.m %s: Not symmetric positive definite matrix"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppGeomTransform.m %s: The %d-th argument is wrong in sposv_ call"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppGeomTransform.m %s: The %d-th argument is wrong in ssyevx_ call"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppGeomTransform.m %s: The %d-th eigenvector failed to converge"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppGeomTransform.m %s: The 9-th parameter is too small: elem8=%f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppGeomTransform.m %s: not symmetric positive definite matrix"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppGeomTransform.m %s: the %d-th argument is wrong in sposv_ call"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: NonRefPyramid[%u]: Not enough external memory provided"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: NonRefPyramid[%u]: Unable to allocate memory"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: RefPyramid[%u]: Not enough external memory provided"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: RefPyramid[%u]: Unable to allocate memory"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: Registration only found %d inlier corners"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: RunThreads failed!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: internalBorderSize != 10"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: maxNumberOfPyramidLevels not in range 1..%u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: nccPatchRadius != 11"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: nccSearchRadius < 1 or nccSearchRadius > 5"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: numHorizontalBlocks < 2"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: numHorizontalBlocks x numVerticalBlocks > %u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: numThreads not in range %u..%u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: numVerticalBlocks < 2"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: ransacAdaptiveThresholdFactor < 1.0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: ransacMinNumInliers < 4"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/RegWarpPP/rwppRegistrationEngine.m %s: reCtxt is NULL"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/CreateLinearSystem/CMIStyleEngineCreateLinearSystem.m"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/CreateLinearSystem/CMIStyleEngineCreateLinearSystem.m %s: planeIndex (%u) >= weightPlaneCount (%u)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/CreateLinearSystem/CMIStyleEngineCreateLinearSystem.m %s: term (%u) >= CMIStyleEngineSecondOrderSystemNumberOfExpansionTerms (%u)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Cannot parse Rect"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected precondition. Should not be called on empty array."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/SubjectRelighting/CMISubjectRelightingANSTSkinToneLevelFilter.m %s: Unexpected type: None"
+ "<<<< (FigMetalAllocatorStategy) >>>> %s: Unknown allocator strategy"
+ "<<<< CMIColorManagement >>>> %s: CVPixelBuffer using gamma transfer function used without gamma value in attachments"
+ "<<<< CMIColorManagement >>>> %s: Could not find compatible pixel format with CSC YCbCr conversion support for %@"
+ "<<<< CMIColorManagement >>>> %s: Cound not find compatible pixel format with CSC support for transfer function %@"
+ "<<<< CMIColorManagement >>>> %s: Input pixel buffer does not have YCbCr matrix type specified in attachments"
+ "<<<< CMIColorManagement >>>> %s: Input pixel buffer format is not YCbCr"
+ "<<<< CMIColorManagement >>>> %s: Unsupported YCC matrix %@"
+ "<<<< CMIColorManagement >>>> %s: Unsupported YCC matrix type"
+ "<<<< CMIColorManagement >>>> %s: Unsupported YCbCr matrix type"
+ "<<<< CMIColorManagement >>>> %s: Unsupported color primaries"
+ "<<<< CMIColorManagement >>>> %s: Unsupported color primaries %@"
+ "<<<< CMIColorManagement >>>> %s: Unsupported illuminant type"
+ "<<<< CMIColorManagement >>>> %s: Unsupported named color space"
+ "<<<< CMIColorManagement >>>> %s: Unsupported transfer function %@"
+ "<<<< CMIFlexGTCStage >>>>"
+ "<<<< CMIFlexGTCStage >>>> %s: Cannot allocate command buffer"
+ "<<<< CMIFlexGTCStage >>>> %s: Cannot allocate command encoder"
+ "<<<< CMIFlexGTCStage >>>> %s: Cannot bind full-size SDR texture"
+ "<<<< CMIFlexGTCStage >>>> %s: Cannot bind gain map texture"
+ "<<<< CMIFlexGTCStage >>>> %s: Failed to set up flexRangeMetadataBuf"
+ "<<<< CMIFlexGTCStage >>>> %s: FlexGTC parameters struct is nil"
+ "<<<< CMIFlexGTCStage >>>> %s: The FlexRange alternate HDR headroom is mising"
+ "<<<< CMIFlexGTCStage >>>> %s: The FlexRange gamma value is mising"
+ "<<<< CMIFlexGTCStage >>>> %s: The FlexRange max gain map value is mising"
+ "<<<< CMIFlexGTCStage >>>> %s: The FlexRange min gain map value is mising"
+ "<<<< CMIFlexGTCStage >>>> %s: The gain map FlexRange dictionary metadata is mising"
+ "<<<< CMIFlexGTCStage >>>> %s: Unable to create CMIFlexGTCStage"
+ "<<<< CMIFlexGTCStage >>>> %s: Unable to init Metal context for CMIFlexGTCStage"
+ "<<<< CMIFlexGTCStage >>>> %s: gain map metadata is nil"
+ "<<<< CMIFlexGTCStage >>>> %s: input SDR Image pixel buffer is nil"
+ "<<<< CMIFlexGTCStage >>>> %s: input gain map pixel buffer is nil"
+ "<<<< CMISSIM >>>>"
+ "<<<< CMISSIM >>>> %s: Cannot find a valid threadgroup size to dispatch"
+ "<<<< CMISSIM >>>> %s: Could not create function %@ from metal library"
+ "<<<< CMISSIM >>>> %s: Failed to allocate SSIM map texture"
+ "<<<< CMISSIM >>>> %s: Failed to allocate reduction texture"
+ "<<<< CMISSIM >>>> %s: Failed to bind imageA pixel buffer as texture"
+ "<<<< CMISSIM >>>> %s: Failed to bind imageB pixel buffer as texture"
+ "<<<< CMISSIM >>>> %s: Failed to bind outputSSIMMap pixel buffer as texture"
+ "<<<< CMISSIM >>>> %s: Failed to create compute pipeline state for %@"
+ "<<<< CMISSIM >>>> %s: Failed to create shared buffer for outputSSIMVal"
+ "<<<< CMISSIM >>>> %s: Failed to encode SSIM calculation"
+ "<<<< CMISSIM >>>> %s: Failed to encode SSIM reduction"
+ "<<<< CMISSIM >>>> %s: Failed to load kernels for CMISSIM"
+ "<<<< CMISSIM >>>> %s: Failed to setup metal context for CMISSIM"
+ "<<<< CMISSIM >>>> %s: FigMetalAllocator setupWithDescriptor failed"
+ "<<<< CMISSIM >>>> %s: Input images have different component count"
+ "<<<< CMISSIM >>>> %s: Invalid configuration"
+ "<<<< CMISSIM >>>> %s: Mismatch texture size between imageA and imageB"
+ "<<<< CMISSIM >>>> %s: Unable to cache pixel buffer texture"
+ "<<<< CMISSIM >>>> %s: Unable to create metal context for CMISSIM"
+ "<<<< CMISSIM >>>> %s: Unable to get texture address"
+ "<<<< CMISSIM >>>> %s: Unable to initialize CMISSIM instance"
+ "<<<< CMISSIM >>>> %s: Unable to initialize CMISSIMConfig"
+ "<<<< CMISSIM >>>> %s: Unable to load the bundle for CMISSIM"
+ "<<<< CMISSIM >>>> %s: Unsupported pixel format"
+ "<<<< CMISSIM >>>> %s: Unsupported texture type for imageA"
+ "<<<< CMISSIM >>>> %s: Unsupported texture type for imageB"
+ "<<<< CMISSIM >>>> %s: Unsupported texture type for outputSSIMMap"
+ "<<<< CMISSIM >>>> %s: outputSSIMMap and outputSSIMVal can't both be null"
+ "<<<< CMISSIM >>>> %s: outputSSIMMap should have at least the same number of channels as input images"
+ "<<<< CMISSIM >>>> %s: outputSSIMMap size inconsistent with input images"
+ "<<<< CMISSIM >>>> %s: windowRadius %d is too big, max supported radius is: %d"
+ "<<<< CMISmartStyleUtilitiesV1 >>>>"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Bytes per coefficient mismatch"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Failed to create original"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Failed to generate Delta map"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Failed to purge resources in style engine processor (err:%d)"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Failed to setup style engine processor for useCase:%lu coefficientsUseFloat16:%d (err:%d)"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Invalid cast type %@"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Invalid cast type %@ for smart style version %u"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Invalid maker note tag %lu for smart style version %u"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Invalid smart style version %u"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Invalid tuning type %@ for smart style version %u"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: No frame to interpolate"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Reverse coefficients are missing"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Unexpected reverseCoefficients size"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Unknown processingType %lu"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Unknown useCase %lu"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: Unsuported _coefficientsPixelBufferBytesPerPixel"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: [SmartStyles] Error: Failed to load RendererTuning.plist - falling back to compiled in version"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: [SmartStyles] failed to initialize tuning params"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: _coefficientsPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: _intermediateStyleRendererPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: coefficients is nil"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: coefficients size is unexpected"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: coefficientsDict is nil"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: coefficientsPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: endFrameCoefficients is nil"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: endFrameGTCData is nil"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: endFrameMetadataDict is nil"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: finishProcessing failed"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: inputCoefficientsPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: inputDeltaMapPixelbuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: inputMetadataDict is nil"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: inputPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: inputStyledPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: outputCoefficients is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: outputDeltaMapPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: outputUnstyledPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: sourcePixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: startFrameCoefficients and endFrameCoefficients do not have the same size"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: startFrameCoefficients is nil"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: startFrameGTCData is nil"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: startFrameGtcLutTable and endFrameGtcLutTable do not have the same size"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: startFrameMetadataDict is nil"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: targetPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: targetThumbnailPixelBuffer is NULL"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: utilities not configured for application"
+ "<<<< CMISmartStyleUtilitiesV1 >>>> %s: utilities not configured for learning"
+ "<<<< CMIVNRProcessor >>>> %s: "
+ "<<<< CMIVNRProcessor >>>> %s: %d"
+ "<<<< CMIVNRProcessor >>>> %s: %p"
+ "<<<< CMIVNRProcessor >>>> %s: %p - exit"
+ "<<<< CMIVNRProcessor >>>> %s: %p - exit; err=%d"
+ "<<<< CMIVNRProcessor >>>> %s: %p - exit; metalCommandQueue=%p"
+ "<<<< CMIVNRProcessor >>>> %s: %p - frameIndex=%d inputPixelBuffer=%p inputMetadata:%p outputPixelBuffer:%p] - exit; err=%d"
+ "<<<< CMIVNRProcessor >>>> %s: %p - inputPixelBuffer=%p inputWidth=%d inputHeight=%d inputMetadata:%p outputPixelBuffer:%p] entry"
+ "<<<< CMIVNRProcessor >>>> %s: %p - inputWidth=%d, inputHeight=%d, tuningParameters=%p"
+ "<<<< CMIVNRProcessor >>>> %s: %p - tuning=%@"
+ "<<<< CMIVNRProcessor >>>> %s: AGC not found/invalid in metadata"
+ "<<<< CMIVNRProcessor >>>> %s: Attempted to wait on nil command buffer"
+ "<<<< CMIVNRProcessor >>>> %s: Bind pixel buffer has invalid height for plane %lu"
+ "<<<< CMIVNRProcessor >>>> %s: Bind pixel buffer has invalid width for plane %lu"
+ "<<<< CMIVNRProcessor >>>> %s: Binding plane index exceeds number of planes"
+ "<<<< CMIVNRProcessor >>>> %s: ChromaBands is nil"
+ "<<<< CMIVNRProcessor >>>> %s: Couldn't get reference to bundle"
+ "<<<< CMIVNRProcessor >>>> %s: Deghosting requires luma and chroma channels to have same width"
+ "<<<< CMIVNRProcessor >>>> %s: Deghosting requires luma channels count to 1 above chrome channels"
+ "<<<< CMIVNRProcessor >>>> %s: Failed parse tuning"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to allocate array for chroma bands"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to allocate array for luma bands"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to allocate chroma texture for pyramid"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to allocate function constants"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to allocate luma texture for pyramid"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to allocate storage for GVA"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to bind input chroma plane"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to bind input luma plane"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to bind output chroma plane"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to bind output luma plane"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate DeghostBoostFactor"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate DeghostBoostFactorScaling"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate DeghostPatchSigmaChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate DeghostPatchSigmaLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate DeghostPatchSigmaScaling"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate FusionStrengthChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate FusionStrengthLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate FusionStrengthScaling"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate GhostAttenuationBreakthroughSigmaChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate GhostAttenuationBreakthroughSigmaLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate GhostAttenuationChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to calculate GhostAttenuationLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for DeghostBoostFactor"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for DeghostBoostFactorScaling"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for DeghostPatchSigmaChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for DeghostPatchSigmaLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for DeghostPatchSigmaScaling"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for FusionStrengthChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for FusionStrengthLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for FusionStrengthScaling"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for GhostAttenuationBreakthroughSigmaChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for GhostAttenuationBreakthroughSigmaLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for GhostAttenuationChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create GVA for GhostAttenuationLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: deghostPropagateLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionBottomChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionBottomLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionInitialBottomChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionInitialBottomLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionInitialMidChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionInitialMidLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionInitialTopChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionInitialTopLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionMidChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionMidLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionTopChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: fusionTopLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: vnrChromaInDownsample"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: vnrChromaInOutDownsampleDeghost"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: vnrDeghostPropagateLumaChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: vnrLumaInDownsample"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: vnrLumaInOutDownsampleDeghost"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal compute pipeline state: vnrSimpleCopy"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create Metal fusion compute pipeline state: %s"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create a metal context"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create chroma band"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create chroma texture array"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create command buffer"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create command encoder for pyramid gen"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create fusion Metal function: %s"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create luma band"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create luma texture array"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create metal shaders"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create previous chroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create previous luma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create shaders for prewarming"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create texture descriptor"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to create texture from IOSurface"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to find correct tuning in plist"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to find valid plist"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to find valid product type"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to generate pyramids"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to get IOSurface for CVPixelBuffer"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to get a metal device"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to load Metal library function: vnrChromaInDownsample"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to load Metal library function: vnrChromaInOutDownsampleDeghost"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to load Metal library function: vnrDeghostPropagateLuma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to load Metal library function: vnrDeghostPropagateLumaChroma"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to load Metal library function: vnrLumaInDownsample"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to load Metal library function: vnrLumaInOutDownsampleDeghost"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to load Metal library function: vnrSimpleCopy"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to load Metal library: %s"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to load tuning plist"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to propagate deghosting scores"
+ "<<<< CMIVNRProcessor >>>> %s: Failed to run fusion"
+ "<<<< CMIVNRProcessor >>>> %s: Gain/Value array doesn't have a sufficient number of entries"
+ "<<<< CMIVNRProcessor >>>> %s: Gain/Value array has incorrect ordering"
+ "<<<< CMIVNRProcessor >>>> %s: Gain/Value array has odd number of entries"
+ "<<<< CMIVNRProcessor >>>> %s: Gain/Value array lookup failed for gain: %f"
+ "<<<< CMIVNRProcessor >>>> %s: Gain/Value arrays contains non-monotonically increasing gain values (gain[%u] >= gain[%u])"
+ "<<<< CMIVNRProcessor >>>> %s: GainValueArray is nil"
+ "<<<< CMIVNRProcessor >>>> %s: LumaBands is nil"
+ "<<<< CMIVNRProcessor >>>> %s: MG Product Type not supported for VNR"
+ "<<<< CMIVNRProcessor >>>> %s: NAN value passed to Gain/Value array lookup"
+ "<<<< CMIVNRProcessor >>>> %s: NSObject init failed"
+ "<<<< CMIVNRProcessor >>>> %s: NSObject init failed for VNRShaders"
+ "<<<< CMIVNRProcessor >>>> %s: Tried to bind nil pixel buffer"
+ "<<<< CMIVNRProcessor >>>> %s: Tried to bind to non-zero plane of non-planar pixel buffer"
+ "<<<< CMIVNRProcessor >>>> %s: Unable to initialize a VNR instance"
+ "<<<< CMIVNRProcessor >>>> %s: VNRTuning super init failed"
+ "<<<< CMIVNRProcessor >>>> %s: VNRTuningBand super init failed"
+ "<<<< CMIVNRProcessor >>>> %s: _inputMetadata is nil"
+ "<<<< CMIVNRProcessor >>>> %s: _inputPixelBuffer is NULL"
+ "<<<< CMIVNRProcessor >>>> %s: _outputPixelBuffer is NULL"
+ "<<<< CMIVNRProcessor >>>> %s: _prepareDescriptor is nil"
+ "<<<< CMIVNRProcessor >>>> %s: inputPixelBuffer and outputPixelBuffer heights don't match"
+ "<<<< CMIVNRProcessor >>>> %s: inputPixelBuffer and outputPixelBuffer widths don't match"
+ "<<<< CMIVNRProcessor >>>> %s: ispDGain not found/invalid in metadata"
+ "<<<< CMIVNRProcessor >>>> %s: ispDGainRangeExpansionFactor not found/invalid in metadata"
+ "<<<< CMIVNRProcessor >>>> %s: prepareDescriptor is nil"
+ "<<<< CMIVNRProcessor >>>> %s: prepareDescriptor.inputHeight should be > 0"
+ "<<<< CMIVNRProcessor >>>> %s: prepareDescriptor.inputWidth should be > 0"
+ "<<<< CMIVNRProcessor >>>> %s: sensorDGain not found/invalid in metadata"
+ "<<<< CMIVNRProcessor >>>> %s: tuningParameters is nil"
+ "<<<< FigM2MController >>>>"
+ "<<<< FigM2MController >>>> %s: IOSurfaceAcceleratorTransformSurface failed (err:%X)."
+ "<<<< FigM2MController >>>> %s: IOSurfaceAcceleratorTransformSurface failed with kIOReturnBadArgument: %lux%lu '%c%c%c%c' {{%lf, %lf}, {%lf, %lf}} --> %lux%lu '%c%c%c%c' {{%u, %u}, {%u, %u}}, runOptions:%@"
+ "<<<< FigM2MController >>>> %s: _supportsSymmetricScaling %i"
+ "<<<< FigM2MController >>>> %s: hTaps: %d, vTaps: %d, hPhases: %d, vPhases: %d, prePointBits: %d, postPointBits: %d"
+ "<<<< FigM2MController >>>> %s: phase %d {%@}"
+ "<<<< FigM2MController >>>> %s: scale: %f\n"
+ "<<<< FigMetalAllocator >>>>"
+ "<<<< FigMetalAllocator >>>> %s: %-40@ (l %4lu): size: %9lu"
+ "<<<< FigMetalAllocator >>>> %s: %-40@ (l: %4lu) offset: %10llu, size: %9lu, used: %10lu, maxFree: %10llu, fragFree%c %10llu/%u, peak: %10lu %s"
+ "<<<< FigMetalAllocator >>>> %s: %-40@ (l: %4lu) size: %9lu"
+ "<<<< FigMetalAllocator >>>> %s: %-40@ (t %s, w %4lu,%s%s%s fmt: %3d) compression: %10lu (%@), size: %9lu"
+ "<<<< FigMetalAllocator >>>> %s: %-40@ (t %s, w %4lu,%s%s%s fmt: %3d) offset: %10llu, compression: %10lu (%@), size: %9lu, used: %10lu, maxFree: %10llu, fragFree%c %10llu/%u, peak: %10lu %s"
+ "<<<< FigMetalAllocator >>>> %s: %-40@ (t %s, w %4lu,%s%s%s fmt: %3d): offset: %10lu, size: %9lu, used: %10lu, maxFree: %10llu, fragFree%c %10llu/%u %s"
+ "<<<< FigMetalAllocator >>>> %s: %-40@ (t %s, w %4lu,%s%s%s fmt: %3d): size: %9lu"
+ "<<<< FigMetalAllocator >>>> %s: %-40@ (w %4lu): offset: %10lu, size: %9lu, used: %10lu, maxFree: %10llu, fragFree%c %10llu/%u %s"
+ "<<<< FigMetalAllocator >>>> %s: -- %@"
+ "<<<< FigMetalAllocator >>>> %s: <Call Stack> forgoOwnership called on a resource <%@> which isn't managed by this allocator <%@> anymore:"
+ "<<<< FigMetalAllocator >>>> %s: Allocating %.1fMB metal buffer from IOSurface"
+ "<<<< FigMetalAllocator >>>> %s: Allocating %.1fMB native metal buffer"
+ "<<<< FigMetalAllocator >>>> %s: Calling getAllocatorMTLResourceSize on a texture < %@ > with no associated FigMetalAllocatorMetadata"
+ "<<<< FigMetalAllocator >>>> %s: Cannot increase the ref count of a nil metal resource"
+ "<<<< FigMetalAllocator >>>> %s: Created a new Metal heap -- wire:%d, %@"
+ "<<<< FigMetalAllocator >>>> %s: FigMetalAllocator's storage mode is *forced* to %u"
+ "<<<< FigMetalAllocator >>>> %s: Initializing allocator with external metal buffer (%.1fMB) "
+ "<<<< FigMetalAllocator >>>> %s: Invalid subAllocator ID ( %d )"
+ "<<<< FigMetalAllocator >>>> %s: MTLRangeAllocatorAllocate failed allocating %@ (size,alignment) = (%lu [%.1fMB], %lu). maxFree: %llu"
+ "<<<< FigMetalAllocator >>>> %s: Releasing Metal heap -- retainCount:%lu, %@"
+ "<<<< FigMetalAllocator >>>> %s: Setting forceDisableCompression = %d"
+ "<<<< FigMetalAllocator >>>> %s: Unexpected class for allocator"
+ "<<<< FigMetalAllocator >>>> %s: Unsupported API by FigMetalAllocatorBackend: %@"
+ "<<<< FigMetalAllocator >>>> %s: Unsupported by < %@ > allocator!"
+ "<<<< FigMetalAllocator >>>> %s: Using IOSurface memory pool for Metal Heap allocation (size: %d, pool id: %d)"
+ "<<<< FigMetalAllocator >>>> %s: [autoUseSubAllocators] Allocating %@ from subAllocator id %d"
+ "<<<< FigMetalAllocator >>>> %s: desc in nil"
+ "<<<< FigMetalAllocator >>>> %s: desc.label: %@ , memSize: %lu"
+ "<<<< FigMetalAllocator >>>> %s: memSize: %lu"
+ "<<<< FigMetalAllocator >>>> %s: nil buffer ( %@ )"
+ "<<<< FigMetalAllocator >>>> %s: nil texture ( %@ )"
+ "<<<< FigMetalAllocator >>>> %s: returned retBuffer is nil for %@"
+ "<<<< FigMetalAllocator >>>> %s: returned retTex is nil for %@"
+ "<<<< FigMetalAllocator >>>> %s: size 0 for buffer ( %@ )"
+ "<<<< FigMetalAllocator >>>> %s: size 0 for texture ( %@ )"
+ "<<<< FigMetalAllocator >>>> %s: subAllocatorID ( %d ) has maxContiguousFreeSize: %lu, not enough to allocate size: %lu for buffer: %@"
+ "<<<< FigMetalAllocator >>>> %s: subAllocatorID ( %d ) has maxContiguousFreeSize: %lu, not enough to allocate size: %lu for texture: %@"
+ "<<<< FigMetalAllocator >>>> %s: subAllocator[%d] has already been allocated"
+ "<<<< FigMetalAllocator >>>> %s: texture is nil"
+ "<<<< FigMetalContext >>>>"
+ "<<<< FigMetalContext >>>> %s: Could not guess width from pixel count (%lu)\n"
+ "<<<< FigMetalContext >>>> %s: Instantiating kernel: %@"
+ "<<<< FigMetalContext >>>> %s: Not all of %s was read\n"
+ "<<<< FigMetalContext >>>> %s: Resolved gpuName: %@"
+ "<<<< FigMetalContext >>>> %s: Something went wrong during fread to file\n"
+ "<<<< FigMetalContext >>>> %s: Something went wrong during fwrite to file\n"
+ "<<<< FigMetalContext >>>> %s: Unable to allocate memory\n"
+ "<<<< FigMetalContext >>>> %s: Unable to create the MTLLibrary (%@)"
+ "<<<< FigMetalContext >>>> %s: Unable to create the computePipelineState (%@)"
+ "<<<< FigMetalContext >>>> %s: Unable to create the function (%@)"
+ "<<<< FigMetalContext >>>> %s: Unable to fopen(\"%s\") for read\n"
+ "<<<< FigMetalContext >>>> %s: Unable to fopen(\"%s\") for writing\n"
+ "<<<< FigMetalContext >>>> %s: Unable to open file %s\n"
+ "<<<< FigMetalContext >>>> %s: filesize (%lu) does not match height (%lu) and stride (%lu)\n"
+ "<<<< FigMetalContext >>>> %s: gpu name: %@"
+ "<<<< FigMetalContext >>>> %s: gpu revision: %@"
+ "<<<< FigMetalContext >>>> %s: pixelBuffer layout is too small, Width_round_to_16 (%d)\tHeight_round_to_16 (%d), bytesPerRow (%d), extendedRows (%d)"
+ "<<<< FigMetalContext >>>> %s: prewarmInternalMetalShadersForFormatsList failed"
+ "<<<< FigMetalContext >>>> %s: rebindTex:..:xFactor: srcWidth %d doesn't divide xFactor %d"
+ "<<<< FigMetalContext >>>> %s: stat(\"%s\") failed\n"
+ "<<<< FigRegWarpPPGPU >>>>"
+ "<<<< FigRegWarpPPGPU >>>> %s: Couldn't build FigRegWarpPPGPU shaders!"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_affineMinSamplesSolverPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_boxFilterPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_copyImagePipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_cornerDetectionFinalPassHalfPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_cornerDetectionFinalPassShortPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_cornerDetectionFirstPass4x4HalfPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_cornerDetectionFirstPass4x4ShortPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_cornerMatchingPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_cornerResponseHalfPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_cornerResponseShortPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_downscaleImagePipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_homographyMinSamplesSolverPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_homographySolverUsingAllCornersPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_homographySolverUsingInliersPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_reorderCornersPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: FigRegWarpPPGPUShaders::_rigidMinSamplesSolverPipeline is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: Unable to init base class for FigRegWarpPPGPU"
+ "<<<< FigRegWarpPPGPU >>>> %s: Unable to init base class for FigRegWarpPPGPUShaders"
+ "<<<< FigRegWarpPPGPU >>>> %s: Unsupported pixelBuffer format (%c%c%c%c)"
+ "<<<< FigRegWarpPPGPU >>>> %s: constantValues is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: metal is nil"
+ "<<<< FigRegWarpPPGPU >>>> %s: numPyrLevels used by RegWarp: %u"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array contains NAN at gain[%u]: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array contains NAN at gain[0]: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array contains NAN at value[%u]: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array contains NAN at value[0]: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array contains invalid element at gain[%u]: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array contains invalid element at gain[0]: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array contains invalid element at value[%u]: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array contains invalid element at value[0]: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array doesn't have a sufficient number of entries: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array has incorrect ordering: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array has odd number of entries: %@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value array lookup failed for gain: %f, array=%@"
+ "<<<< GainValueLookup >>>> %s: Gain/Value arrays contains non-monotonically increasing gain values (gain[%u] >= gain[%u]): %@"
+ "<<<< GainValueLookup >>>> %s: Invalid gain encountered in Gain/Value array: %@"
+ "<<<< GainValueLookup >>>> %s: Invalid value encountered in Gain/Value array: %@"
+ "<<<< GainValueLookup >>>> %s: NAN value passed to Gain/Value array lookup"
+ "<<<< MetalEventSynchronizer >>>> %s: Added event/signal %p/%llu with key %p"
+ "<<<< MetalEventSynchronizer >>>> %s: Commandbuffer %p waiting on event/signal %p/%llu with key %p"
+ "<<<< MetalEventSynchronizer >>>> %s: Removed event/signal %p/%llu with key %p"
+ "<<<< MetalEventSynchronizer >>>> %s: Shared instance %p created"
+ "<<<< MetalEventSynchronizer >>>> %s: Signaled event %p with signal %llu on commandBuffer %p"
+ "<<<< MetalIntercept >>>>"
+ "<<<< MetalIntercept >>>> %s: CommandBuffer < %-120s > kernelTime: %fms, gpuTime: %fms"
+ "<<<< MetalIntercept >>>> %s: Fig MetalIntercept is set to < %s >"
+ "<<<< MetalIntercept >>>> %s: MTLIntercept notifyPostOnGPUError:   %d"
+ "<<<< MetalIntercept >>>> %s: MTLIntercept processTexture:         %d"
+ "<<<< MetalIntercept >>>> %s: MTLIntercept validateCommandBuffers: %d"
+ "<<<< MetalIntercept >>>> %s: MTLIntercept waitUntilCompleted:     %d"
+ "<<<< MetalIntercept >>>> %s: MTLIntercept waitUntilScheduled:     %d"
+ "<<<< MetalIntercept >>>> %s: MetalIntercept enabled with level = %d."
+ "<<<< MetalIntercept >>>> %s: waitUntilCompleted"
+ "<<<< MetalIntercept >>>> %s: waitUntilScheduled"
+ "<<<< NSMutableDictionary+Merge >>>> %s: dictionary merge failed; key/value already exists: %@"
+ "<<<< PixelBufferUtils >>>>"
+ "<<<< PixelBufferUtils >>>> %s: %s: cannot guess dimensions of packed 10-bit format"
+ "<<<< PixelBufferUtils >>>> %s: %s: cannot guess dimensions of planar surfaces"
+ "<<<< PixelBufferUtils >>>> %s: %s: could not guess dimensions\n"
+ "<<<< PixelBufferUtils >>>> %s: %s: filesize (%lu) is not divisible by pixelBlockSize (%lu), blockWidth (%lu), blockHeight (%lu)\n"
+ "<<<< PixelBufferUtils >>>> %s: %s: pixelCount (%lu) does not match filesize (%lu)\n"
+ "<<<< PixelBufferUtils >>>> %s: %s: width (%lu) and height (%lu) do not match pixelCount (%lu)\n"
+ "<<<< PixelBufferUtils >>>> %s: %s: width or height pointer parameter is NULL\n"
+ "<<<< PixelBufferUtils >>>> %s: Could not get pixel format type from file extension"
+ "<<<< PixelBufferUtils >>>> %s: Error: %s\n"
+ "<<<< PixelBufferUtils >>>> %s: No format description whatsoever of format %08x\n"
+ "<<<< PixelBufferUtils >>>> %s: No kCVPixelFormatBitsPerBlock entry in the description of format %08x plane %ld\n"
+ "<<<< PixelBufferUtils >>>> %s: Not enough data"
+ "<<<< PixelBufferUtils >>>> %s: Something went wrong at row %ld\n"
+ "<<<< PixelBufferUtils >>>> %s: Too much data"
+ "<<<< PixelBufferUtils >>>> %s: Unable to create CVPixelBuffer\n"
+ "<<<< PixelBufferUtils >>>> %s: Unable to create pixel buffer\n"
+ "<<<< PixelBufferUtils >>>> %s: Unable to fopen(\"%s\") for writing\n"
+ "<<<< PixelBufferUtils >>>> %s: Unable to lock pixelBuffer for writing\n"
+ "<<<< PixelBufferUtils >>>> %s: Unknown bayerPattern %d"
+ "<<<< PixelBufferUtils >>>> %s: bayerPatternStr.length (%lu) is larger or equal than outBayerPatternStrLen (%lu)"
+ "<<<< PixelBufferUtils >>>> %s: height is negative"
+ "<<<< PixelBufferUtils >>>> %s: pixelSize is zero"
+ "<<<< PixelBufferUtils >>>> %s: width is negative"
+ "<<<< SSCHistogram >>>>"
+ "<<<< SSCHistogram >>>> %s: pixelFormat not supported"
+ "<<<< STEREODISPARITY GDC >>>>"
+ "<<<< STEREODISPARITY GDC >>>> %s: Crop rect was not set properly or used normalized coordinates. Ignoring it."
+ "<<<< STEREODISPARITY GDC >>>> %s: GDC init completed with no error"
+ "<<<< STEREODISPARITY GDC >>>> %s: canvasResolution was set to size: [%f x %f]"
+ "<<<< STEREODISPARITY GDC >>>> %s: originalImageOrigin was set to origin: [%f, %f]"
+ "<<<< STEREODISPARITY GDC >>>> %s: originalImageResolution was set to size: [%f x %f]"
+ "<<<< STEREODISPARITY GDC >>>> %s: targetCropRect was set to - origin: [%f, %f] - size: [%f x %f]"
+ "<<<< SmartStyleMetalRenderer >>>>"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Called"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to allocate reduction pyramid band texture"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to apply final render"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to compute histogram and stats"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to compute rendering params from stats"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to create guide image"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to encode image reduction for input image"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to encode image reduction for input linear image"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to encode linear"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to populate precomputed stats"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to process LTM gain map"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to process segmentation masks"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to release intermediate resources"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to run image reduction"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to update render pipeline configuration for inputs"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Failed to upsample light map"
+ "<<<< SmartStyleMetalRenderer >>>> %s: FigMetalAllocator resources not correctly released"
+ "<<<< SmartStyleMetalRenderer >>>> %s: FigMetalAllocator setupWithDescriptor failed"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Invalid tuning type %@"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Out of memory in shared access allocator, falling back to device allocation instead"
+ "<<<< SmartStyleMetalRenderer >>>> %s: SmartStyleRenderer Failed to render"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Unsupported input style version %u"
+ "<<<< SmartStyleMetalRenderer >>>> %s: Use `inputLinearImageTexture` instead."
+ "<<<< SmartStyleMetalRenderer >>>> %s: [SmartStyles] Error: Failed to load RendererTuning.plist - falling back to compiled in version"
+ "<<<< SmartStyleMetalRenderer >>>> %s: [SmartStyles] Error: couldn't find cast adjustments for %@"
+ "<<<< SmartStyleMetalRenderer >>>> %s: [SmartStyles] Error: couldn't find color adjustments for %@"
+ "<<<< SmartStyleMetalRenderer >>>> %s: [SmartStyles] Error: couldn't find tone adjustments for %@"
+ "<<<< SmartStyleMetalRenderer >>>> %s: [SmartStyles] Processing with castType=%s castIntensity=%.2f tone=%.2f color=%.2f semanticStyleSceneType=%d personMasksValidHint=%f"
+ "<<<< SmartStyleMetalRenderer >>>> %s: [SmartStyles] Render pipeline config: upsamplePersonMask=%d createLTMGainMap=%d"
+ "<<<< SmartStyleMetalRenderer >>>> %s: [SmartStyles] failed to initialize tuning params with err=%d"
+ "<<<< SmartStyleMetalRenderer >>>> %s: inputLinearImageGainDownRatio is deprecated, replaced by inputLinearBaseGain which includes compensation for HRGainDown"
+ "<<<< SmartStyleMetalRenderer >>>> %s: inputSRLCurveParameter = %f, semanticStyleSceneType = %d"
+ "<<<< SmartStylePixelBufferRenderer >>>>"
+ "<<<< SmartStylePixelBufferRenderer >>>> %s: %p"
+ "<<<< SmartStylePixelBufferRenderer >>>> %s: %p - exit"
+ "<<<< SmartStylePixelBufferRenderer >>>> %s: FigMetalAllocator resources not correctly released"
+ "<<<< SmartStylePixelBufferRenderer >>>> %s: Input gain map pixel buffer is NULL"
+ "<<<< SmartStylePixelBufferRenderer >>>> %s: inputSRLCurveParameter = %f, semanticStyleSceneType = %d"
+ "<<<< SmartStyleProxyRenderer >>>>"
+ "<<<< SmartStyleProxyRenderer >>>> %s: %p"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Cannot find cached cube for input style"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to allocate new color cube"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to allocate new color cube (%lu)"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to bind %s as texture"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to calculate smart style adjustment parameters"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to configure color cube pool"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to generate color cubes"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to get cached cube for input style to update"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to render with color cubes"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to update color cube cache"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Failed to update color cubes"
+ "<<<< SmartStyleProxyRenderer >>>> %s: FigMetalAllocator resources not correctly released"
+ "<<<< SmartStyleProxyRenderer >>>> %s: FigMetalAllocator setupWithDescriptor failed"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Input style exceeds max input style count configured"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Invalid processing type"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Invalid tuning type %@"
+ "<<<< SmartStyleProxyRenderer >>>> %s: No input styles to process"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Unsupported smart style version in input styles"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Updated %d cubes"
+ "<<<< SmartStyleProxyRenderer >>>> %s: Using external memory resource %p "
+ "<<<< SmartStyleProxyRenderer >>>> %s: [SmartStyles] Error: couldn't find cast adjustments for %@"
+ "<<<< SmartStyleProxyRenderer >>>> %s: [SmartStyles] Error: couldn't find color adjustments for %@"
+ "<<<< SmartStyleProxyRenderer >>>> %s: [SmartStyles] Error: couldn't find tone adjustments for %@"
+ "<<<< SmartStyleProxyRenderer >>>> %s: [SmartStyles] Processing with castType=%s castIntensity=%.2f tone=%.2f color=%.2f currentSceneTypeForCubes=%d personMasksValidHint=%f"
+ "<<<< SmartStyleProxyRenderer >>>> %s: [SmartStyles] failed to initialize tuning params with err=%d"
+ "<<<< SmartStyleRendererPlist >>>> %s: Warning: Tuning parameter %@.%@ missing from tuning dictionary"
+ "<<<< SmartStyleRendererPlist >>>> %s: Warning: Tuning sub-array %@.%@ missing from tuning dictionary"
+ "<<<< SmartStyleRendererPlist >>>> %s: Warning: Tuning sub-dict %@.%@ missing from tuning dictionary"
+ "<<<< SmartStyleRendererUtils >>>> %s: Color primaries unspecified for color management due to missing / invalid tagging on pixel buffer %@"
+ "<<<< SmartStyleRendererUtils >>>> %s: Color primaries unsupported by CMIColorManagement found on %@"
+ "<<<< SmartStyleRendererUtils >>>> %s: Invalid stats type enum %d"
+ "<<<< SmartStyleRendererUtils >>>> %s: Transfer function unspecified for color management due to missing / invalid tagging on pixel buffer %@"
+ "<<<< SmartStyleRendererUtils >>>> %s: Transfer function unsupported by CMIColorManagement found on %@"
+ "<<<< SmartStyleRendererUtils >>>> %s: Unknown cast type string: %@"
+ "<<<< SmartStyleRendererUtils >>>> %s: Unknown semantic style scene type: %d"
+ "<<<< SmartStyleRendererUtils >>>> %s: Unknown tuning type string: %@"
+ "<<<< SmartStyleRendererUtils >>>> %s: YCC matrix unspecified for color management due to missing / invalid tagging on pixel buffer %@"
+ "<<<< SmartStyleRendererUtils >>>> %s: YCC matrix unsupported by CMIColorManagement found on %@"
+ "<<<< SmartStyleV1 >>>> %s: Failed to init SmartStyleV1 instance"
+ "<<<< SmartStyleV1 >>>> %s: Invalid cast intensity %f"
+ "<<<< SmartStyleV1 >>>> %s: Invalid cast type %@"
+ "<<<< SmartStyleV1 >>>> %s: Invalid color bias %f"
+ "<<<< SmartStyleV1 >>>> %s: Invalid tone bias %f"
+ "<<<< StyleEngineCoefficientProcessor >>>>"
+ "<<<< StyleEngineCoefficientProcessor >>>> %s: Unable to create CoefficientsRingData"
+ "<<<< StyleEngineCoefficientProcessor >>>> %s: Using CMIMetalEventSynchronizer %p"
+ "<<<< StyleEngineCoefficientProcessor >>>> %s: rect not valid in learnedROIRectDict!"
+ "<<<< StyleEngineCoefficientProcessor >>>> %s: remixFactor is NULL"
+ "<<<< StyleEngineCoefficientProcessor >>>> %s: ringData is nil"
+ "<<<< StyleEngineCoefficientRingBuffer >>>> %s: Coefficients window start PTS bigger then end PTS"
+ "<<<< StyleEngineCoefficientRingBuffer >>>> %s: CoefficientsRingBuffer add a data _inputIndex:%d"
+ "<<<< StyleEngineCoefficientRingBuffer >>>> %s: CoefficientsRingBuffer initialized with capacity:%d"
+ "<<<< StyleEngineCoefficientRingBuffer >>>> %s: CoefficientsRingBuffer reset"
+ "<<<< StyleEngineCoefficientRingBuffer >>>> %s: Unable to initialize CoefficientsRingBuffer. Capacity too big."
+ "<<<< StyleEngineCoefficientRingBuffer >>>> %s: Unable to initialize coefficients data array."
+ "<<<< StyleEngineCoefficientRingBuffer >>>> %s: dealloc %lu items"
+ "<<<< StyleEngineCoefficientRingBuffer >>>> %s: elapsed time:%lld ns"
+ "<<<< StyleEngineProcessor >>>>"
+ "<<<< StyleEngineProcessor >>>> %s: "
+ "<<<< StyleEngineProcessor >>>> %s: Error binding luma/chroma planes of %s with error: %d"
+ "<<<< StyleEngineProcessor >>>> %s: Failed to purge resources (err:%d)"
+ "<<<< StyleEngineProcessor >>>> %s: FigMetalAllocator resources not correctly released"
+ "<<<< StyleEngineProcessor >>>> %s: FigMetalAllocator size is: < %lu >"
+ "<<<< StyleEngineProcessor >>>> %s: MTLBuffer and CVPixelBufferRef bound to %s, only one must be set"
+ "<<<< StyleEngineProcessor >>>> %s: MTLBuffer and MTLTexture bound to %s, only one must be set"
+ "<<<< StyleEngineProcessor >>>> %s: MTLTexture and CVPixelBufferRef bound to %s, only one must be set"
+ "<<<< StyleEngineProcessor >>>> %s: Missing `ProcessingType` from configuration.processorSpecificOptions"
+ "<<<< StyleEngineProcessor >>>> %s: Setting-up StyleEngine FigMetalAllocator"
+ "<<<< StyleEngineProcessor >>>> %s: Using CMIMetalEventSynchronizer %p"
+ "<<<< StyleEngineProcessor >>>> %s: Using external memory resource %p "
+ "<<<< StyleEngineProcessor >>>> %s: Using provided metal command queue %p"
+ "<<<< SubjectRelightingPlist >>>> %s: Warning: %@ parameter missing from tuning dictionary"
+ "<<<< SubjectRelightingStage >>>>"
+ "<<<< SubjectRelightingStage >>>> %s: ANST metadata is missing in SRL calculations"
+ "<<<< SubjectRelightingStage >>>> %s: Couldn't build SubjectRelightingShared!"
+ "<<<< SubjectRelightingStage >>>> %s: Sizes do not match: sizeof(SubjectRelightingAllStats_t)=%zu; _lastComputedRelightingStats.length=%zu"
+ "Bands array size not matching MaxNumberOfPyramidLevels"
+ "BayerPattern attachment missing"
+ "Bundle is nil, cannot proceed"
+ "CIC data version is not compatible with OIS adaptation method version 1"
+ "CMIGetBaseRGBFromYCCConversionMatrix"
+ "CMIGetBaseYCCFromRGBConversionMatrix"
+ "CMIGetColorSpaceWithName"
+ "CMIGetMetalPixelFormatForPixelBuffer"
+ "CMIGetPixelBufferColorSpace"
+ "CMIGetPixelBufferYCCMatrix"
+ "CMIGetRGBFromYCCConversionMatrixForPixelBuffer"
+ "CMIGetXYZForIlluminant"
+ "CMIGetYCCFromRGBConversionMatrixForPixelBuffer"
+ "CMILSCOISAdaptationErrorAllocationFailed"
+ "CMILSCOISAdaptationErrorInvalidParam"
+ "CMILSCOISAdaptation_convertV2CICTableToV1CICTableWithOISOffset"
+ "CMILSCOISAdaptation_convertV2LSCTableToV1LSCTableWithOISOffset"
+ "CMILSCOISAdaptation_extrapAndCropCICWithOISOffset"
+ "CMILSCOISAdaptation_extrapAndCropLSCLumaOnlyWithOISOffset"
+ "CMISmartStyleRendererStatusInputError"
+ "CMISmartStyleRendererStatusRegionError"
+ "CMISmartStyleRendererStatusResourcesNotReleased"
+ "CMISmartStyleRendererStatusTextureCacheError"
+ "CMISmartStyleRendererStatusUnsupportedPixelFormat"
+ "CMIStyleEngineStatusCVMTLCacheError"
+ "CMIStyleEngineStatusIOSurfaceBufferBindingError"
+ "CMIStyleEngineStatusIncorrectAllocator"
+ "CMIStyleEngineStatusIncorrectIO"
+ "CMIStyleEngineStatusLinearSystemError"
+ "CMIStyleEngineStatusNoConfiguration"
+ "CMIStyleEngineStatusROISpecificationError"
+ "CMIStyleEngineStatusResourcesNotReleased"
+ "CMIStyleEngineStatusUnsupportedPixelFormat"
+ "CMIStyleEngineStatusUnsupportedProcessingType"
+ "CMIStyleEngineStatusUnsupportedTuningParamValue"
+ "CVPixelBufferRef should be IOSurface-backed"
+ "Cannot find GeometricDistortionCoefficients in cameraInfo"
+ "Cannot find OpticalCenter in metadataDict"
+ "Cannot init RangeVertex"
+ "CommandQueue device is nil. Weird ...."
+ "Common inits failed"
+ "CopyPixelBuffer"
+ "Could not allocate memory  for new CIC grid"
+ "Could not allocate memory  for new LSC grid"
+ "Could not allocate memory for expanded grid"
+ "Could not allocate memory for new LSC grid"
+ "Could not allocate memory for temporary Cropped Luma"
+ "Could not allocate memory for temporary Luma"
+ "Could not allocate memory for the new CIC grid"
+ "Could not create RGB to YUV ccm for outputPixelBuffer"
+ "Could not create YUV to RGB ccm for inputDeltaMapPixelBuffer"
+ "Could not create YUV to RGB ccm for inputOriginalPixelBuffer"
+ "Could not create YUV to RGB ccm for inputPixelBuffer"
+ "Create420PixelBufferFromPGMFiles"
+ "CreatePixelBufferExtendedFromCFData"
+ "CreatePixelBufferExtendedFromFile"
+ "CreatePixelBufferFromPGMFile"
+ "CreatePixelBufferWithAttributes"
+ "CreateSampleBuffer"
+ "DeriveImageWidthHeightFromFilesize"
+ "Either inputTexture or {inputLumaTexture, inputChromaTexture} must be set"
+ "Either outputTexture or {outputLumaTexture, outputChromaTexture} must be set"
+ "EndLambda must be >= 0"
+ "Engine nil"
+ "ExtLambda must be >= 0"
+ "External memory resource too low"
+ "FIGMETALCONTEXT_CHECK_ERRCODE"
+ "Failed creating CMISharpnessScore"
+ "Failed creating a FigMetalAllocator"
+ "Failed to allocate inputRadius"
+ "Failed to allocate inverseScaling"
+ "Failed to allocate redistortedRadius"
+ "Failed to allocate sampledUndistortedRadius"
+ "Failed to allocate texture descriptor."
+ "Failed to allocate uint16Buffer"
+ "Failed to allocate undistortedRadius"
+ "Failed to blur the input image."
+ "Failed to compute statistics."
+ "Failed to compute the sharpness score for the full image."
+ "Failed to compute the sharpness score."
+ "Failed to create command buffer."
+ "Failed to create compute command encoder for sharpness score! Please ensure your combination of sourceComponent + texture type is properly set up in 'initWithOptionalCommandQueue'"
+ "Failed to create compute command encoder."
+ "Failed to create inverseGDCLUT"
+ "Failed to create lutTexDesc"
+ "Failed to create metal texture."
+ "Failed to create texture from pixel buffer."
+ "Failed to extract BasePolynomial"
+ "Failed to extract DynamicPolynomial"
+ "Failed to extract PixelSize"
+ "Failed to extract RawSensorHeight"
+ "Failed to extract RawSensorWidth"
+ "Failed to extract distortionOpticalCenterX"
+ "Failed to extract distortionOpticalCenterY"
+ "Failed to init FigRegWarpPPGPUShaders"
+ "Failed to set default corner matching params"
+ "Failed to set normCoefs"
+ "Failed to set num of pyramid levels"
+ "Fig metal intercept cannot be instantiated with enablement level equal to FigMetalInterceptLevel_OFF"
+ "FigMetalAllocator resources not correctly released"
+ "FigMetalAllocator setupWithDescriptor:allocatorBackend failed"
+ "FigMetalDecRef"
+ "FigMetalIncRef"
+ "FigMetalInterceptLevel_DEFAULT"
+ "FigMetalInterceptLevel_FULL"
+ "Filter type not supported"
+ "IOSurface bytes per row not a multiple of 64"
+ "IOSurfaceAcceleratorCreate failed"
+ "IOsurface height is smaller than texture height"
+ "IOsurface width is smaller than texture width"
+ "Image height does not match configuration"
+ "Image pixel format does not match configuration"
+ "Image width does not match configuration"
+ "Input"
+ "Input and output pixel buffers require a different number of bound planes"
+ "Input coefficient buffer is too small"
+ "Input coefficient pixel buffer is too small"
+ "InputDeltaMap"
+ "InputOriginal"
+ "Invalid GPU priority"
+ "Invalid QuadraBinningFactor metadata value"
+ "Invalid surface plane"
+ "LSC data version is not compatible with OIS adaptation method version 1"
+ "LearningModulationOffset must be >= 0"
+ "LearningModulationStrength * LearningModulationOffset must be <= 1"
+ "LearningModulationStrength must be >= 0"
+ "Linear system could not be solved"
+ "Mandatory parameter image is nil"
+ "Metal allocator not provided or uninitialized"
+ "NULL pixelBuffer"
+ "Nil image statistics"
+ "Nil metadata dictionary"
+ "No allocator set. Please check the property 'allocator' of CMISharpnessScore"
+ "No configuration object set"
+ "No rect"
+ "No shaders data, cannot proceed"
+ "Not a 420 buffer"
+ "Not enough external memory provided"
+ "Not supported filtered type passed to filterCoefficientsIIR method"
+ "Number of valid keypoints between ref and nonref mismatches"
+ "Number of weight planes must be even if performing color split"
+ "One and only one of 'outputTexture' or 'outputDeltaMapTexture' must be set for processing type 'CMIStyleEngineProcessingTypeApply'"
+ "Output coefficient buffer is too small"
+ "Output coefficients metal buffer is NULL"
+ "Output threshold is nil"
+ "PCSFromRGBMatrix"
+ "PixelBufferLineIterator"
+ "RGBFromPCSMatrix"
+ "RegWarpPP(_regEng) not initialized!"
+ "ResidualScaleFactor must be >= 0"
+ "SSCHistogram_trace"
+ "SSRAttachColorManagementMetadata"
+ "SSRSceneTypeEnumFromSemanticStyleSceneType"
+ "SSRStatsTypeStringFromEnum"
+ "Spotlight count must be > 0"
+ "Stats calculation not requested, but light maps are not provided for rendering"
+ "Stats calculation not requested, but stats and light maps are not provided for rendering."
+ "Supported"
+ "Thumbnail size must be > 0"
+ "TikLambdaConstant must be >= 0"
+ "TikLambdaLinear must be >= 0"
+ "TikLambdaQuadratic must be >= 0"
+ "Too many planes found in srcPixelBuffer"
+ "TotalSensorCropCGRect is missing"
+ "TotalSensorCropCGRect is outside of SensorCropRect"
+ "Tuning undefined for the band"
+ "Unable fill filter buffer"
+ "Unable to allocate MTLBuffer for position"
+ "Unable to allocate MTLVertexDescriptor"
+ "Unable to allocate uncompressed pixel buffer"
+ "Unable to bind iosurface to buffer"
+ "Unable to cache pixel buffer buffer"
+ "Unable to cache pixel buffer texture"
+ "Unable to compute homography"
+ "Unable to create FigMetalContext"
+ "Unable to create MTLCommandQueue"
+ "Unable to create MTLDevice"
+ "Unable to create MTLLibrary"
+ "Unable to create MTLTexture"
+ "Unable to create MTLTextureDescriptor"
+ "Unable to create an m2m instance"
+ "Unable to create nonRefDistortionModel"
+ "Unable to create refDistortionModel"
+ "Unable to get buffer address"
+ "Unable to get dataWindow from the coefficients ring buffer"
+ "Unable to get dataWindow from the filtered coefficients ring buffer"
+ "Unable to get texture address"
+ "Unable to lock image"
+ "Unable to lock srcPixelBuffer for writing"
+ "Unable to open file for reading\n"
+ "Unable to parse PGM header\n"
+ "Unable to set weight plane constant prior scale factor"
+ "Unable to set weight plane linear prior scale factor"
+ "Unable to set weight plane quadratic prior scale factor"
+ "Unable to uncompress pixel buffer"
+ "Unsupported"
+ "Unsupported input texture type"
+ "Unsupported pixel format for input"
+ "Unsupported pixel format for output"
+ "Unsupported processing type"
+ "UnsupportedDevice"
+ "UnsupportedHeapTypeSparse"
+ "UnsupportedLinearLayout"
+ "UnsupportedOptOut"
+ "UnsupportedPixelFormat"
+ "UnsupportedSmallTexture"
+ "UnsupportedTextureType"
+ "UnsupportedTextureUsagePixelFormatView"
+ "UnsupportedTextureUsageShaderWrite"
+ "V:%d, m:%d.%d, f:%@, s:%@"
+ "Version:%d, modelVersion:%d.%d, firmwareVersion:%@, sensorSerialNumber:%@"
+ "Warning: MaxNumberOfPyramidLevels is missing; using default value"
+ "Warning: MinCornerResponseThreshold is missing; using default value"
+ "Warning: NormalizeCornerResponse is missing; using default value"
+ "Warning: PerformHistEq is missing; using default value"
+ "Warning: UseHalfPrecisionCornerResponse is missing; using default value"
+ "Weight plane color split strength must be >= 0"
+ "Weight plane count must be > 0"
+ "Weight plane count must be even when performing color split"
+ "Weight plane spatial filter weight must be >= 0"
+ "Weight plane standard-deviation for integration must be > 0"
+ "Weight plane standard-deviation for learning must be > 0"
+ "Weight plane standard-deviation must be > 0"
+ "Write420PixelBufferChannelToPGMFile"
+ "WriteFloat16PixelBufferChannelToPGMFile"
+ "WriteOneComponent8PixelBufferToPGMFile"
+ "WritePixelBufferToFile"
+ "Wrong CB plane size"
+ "Wrong CR plane size"
+ "[FigRegToolboxGPU]"
+ "_"
+ "_FlexGTCConvertSDRLA_NLGM_to_HDRLA is NULL"
+ "_FlexGTCDownsampleGM10_to_NLGM is NULL"
+ "_FlexGTCDownsampleGM8_to_NLGM is NULL"
+ "_FlexGTCDownsampleRGBA8_to_LA is NULL"
+ "_FlexGTCHistogramLumaAndGain is NULL"
+ "_YCbCrToRGBColorConversionPipelineState is NULL"
+ "_applyConvolutionShaderFloat[sourceComponent] is NULL"
+ "_applyStyle is NULL"
+ "_backendAllocator is nil"
+ "_backendAllocator.memSize == desc.memSize is NULL"
+ "_backendAllocator.memSize > 0 is NULL"
+ "_bgLTMGainMapTexture is NULL"
+ "_boxFilterPipeline threadgroup size beyond limit"
+ "_bufDesc is NULL"
+ "_bufferDescriptor is NULL"
+ "_checkStatusComputePipelineState is NULL"
+ "_coefficientConverterF16ToF32 is NULL"
+ "_coefficientConverterF32ToF16 is NULL"
+ "_coefficientsBuffer is NULL"
+ "_commandBuffer is NULL"
+ "_commandQueue is NULL"
+ "_computeClipValueWithHistogramShader is NULL"
+ "_computePipelineState[FillTexturePipelineState] is NULL"
+ "_computePipelineState[IntegrateComputePipelineState] is NULL"
+ "_computePipelineStates[AddPriorToLHSPipelineState] is NULL"
+ "_computePipelineStates[AddPriorToRHSPipelineState] is NULL"
+ "_computePipelineStates[AverageSystemsPipelineState] is NULL"
+ "_computePipelineStates[CalcPriorPipelineState] is NULL"
+ "_computePipelineStates[CreateF16PipelineState] is NULL"
+ "_computePipelineStates[CreateF32PipelineState] is NULL"
+ "_computePipelineStates[DownScaleExactPipelineState_1x] is NULL"
+ "_computePipelineStates[DownScaleExactPipelineState_2x] is NULL"
+ "_computePipelineStates[DownScaleExactPipelineState_4x] is NULL"
+ "_computePipelineStates[DownScaleExactPipelineState_8x] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x_GDC] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x_antiAliased] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x_antiAliased_GDC] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x_GDC] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x_antiAliased] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x_antiAliased_GDC] is NULL"
+ "_computePipelineStates[DownScalePipelineState] is NULL"
+ "_computePipelineStates[DownScalePipelineState_GDC] is NULL"
+ "_computePipelineStates[DownScalePipelineState_GDC_Quad] is NULL"
+ "_computePipelineStates[DownScalePipelineState_Quad] is NULL"
+ "_computePipelineStates[FactorizePipelineState] is NULL"
+ "_computePipelineStates[FillColorHistogramPipelineState] is NULL"
+ "_computePipelineStates[LHSIndependentSpotlightsPipelineState] is NULL"
+ "_computePipelineStates[LHSPipelineState] is NULL"
+ "_computePipelineStates[MakeWeightsPipelineState] is NULL"
+ "_computePipelineStates[NearestScalePipelineState] is NULL"
+ "_computePipelineStates[NearestScalePipelineState_GDC] is NULL"
+ "_computePipelineStates[NormalizePixelVectorsPipelineState] is NULL"
+ "_computePipelineStates[NormalizePlanesPipelineState] is NULL"
+ "_computePipelineStates[PairExpandWeightsPipelineState] is NULL"
+ "_computePipelineStates[PolyExpandInputPipelineState] is NULL"
+ "_computePipelineStates[PolyExpandTargetPipelineState] is NULL"
+ "_computePipelineStates[RHSPipelineState] is NULL"
+ "_computePipelineStates[SimpleResizePipelineState] is NULL"
+ "_computePipelineStates[SimpleResizePipelineState_GDC] is NULL"
+ "_computePipelineStates[SplitWeightPlanesByColorPipelineState] is NULL"
+ "_computePipelineStates[SubstitutionPipelineState] is NULL"
+ "_computePipelineStates[SumPlanesPipelineState] is NULL"
+ "_computePipelineStates[ThresholdHistogramPipelineState] is NULL"
+ "_copyImagePipeline threadgroup size beyond limit"
+ "_cornerDetectIntermediateTexture nil"
+ "_cornerDetectionFirstPass4x4Pipeline threadgroup size beyond limit"
+ "_cornerResponsePipeline threadgroup size beyond limit"
+ "_createGuidePipelineStateUsingImageBlock is NULL"
+ "_createGuidePipelineStateWithoutImageBlock is NULL"
+ "_createLTMGainMapPipelineStateUsingImageBlock is NULL"
+ "_createLTMGainMapPipelineStateWithoutImageBlock is NULL"
+ "_createLinearSystem is NULL"
+ "_createSpotlights is NULL"
+ "_createSpotlightsComputePipelineState is NULL"
+ "_createWeightPlanes is NULL"
+ "_cubicSplineToneCurveTexture is NULL"
+ "_currentResources is NULL"
+ "_desc is NULL"
+ "_device is NULL"
+ "_downScale is NULL"
+ "_downscaleImagePipeline threadgroup size beyond limit"
+ "_encodeLinearPipelineState is NULL"
+ "_failedCommandBuffers is NULL"
+ "_fgLTMGainMapTexture is NULL"
+ "_fgbgMatteTexture is NULL"
+ "_filterBuf is NULL"
+ "_gdcPipeline is NULL"
+ "_gdcYUVPipeline is NULL"
+ "_generateColorCubesPipelineState is NULL"
+ "_globalHistogramPipelineState is NULL"
+ "_globalStatsPipelineState is NULL"
+ "_guideTexture is NULL"
+ "_histogram is NULL"
+ "_hueSatLumLUTPipelineState is NULL"
+ "_identityCoefficientCreator is NULL"
+ "_imageReduction is NULL"
+ "_inputBuffer && _outputBuffer is NULL"
+ "_inputGlobalToneCurveTexture is NULL"
+ "_inputImageTexture is NULL"
+ "_inputLHSBuffer && _inputRHSBuffer && _outputCoefficients && _inputStatusBuffer is NULL"
+ "_inputLHSBuffer.length == ( order * lhsRowBytes * self.systemCount ) is NULL"
+ "_inputLHSBuffer.length == ( self.lhsSize * self.lhsSize * sizeof( float ) * self.systemCount ) is NULL"
+ "_inputLightMapTexture is NULL"
+ "_inputLinearImageTexture || ( _inputLinearImageLumaTexture && _inputLinearImageChromaTexture ) is NULL"
+ "_inputLinearLightMapTexture is NULL"
+ "_inputRHSBuffer.length == ( order * rhsRowBytes * self.systemCount ) is NULL"
+ "_inputRHSBuffer.length == ( self.lhsSize * self.rhsSize * sizeof( float ) * self.systemCount ) is NULL"
+ "_inputRHSBuffer.length == _outputCoefficients.length is NULL"
+ "_inputStatusBuffer.length == ( sizeof( int ) * self.systemCount ) is NULL"
+ "_inputTexture && _outputTexture is NULL"
+ "_inputTexture && _outputWeightPlanesTexture && _inputPlaneNormalisationBuffer is NULL"
+ "_inputThresholdCalculationBuffer is NULL"
+ "_inputThumbnailTexture && _inputWeightPlanesTexture && _outputLHSBuffer && _inputLHSDiagSumsBuffer && _targetThumbnailTexture && _outputRHSBuffer && _inputPriorFactorForLHSBuffer && _inputPriorFactorForRHSBuffer && _inputPolyExpandedInputBuffer && _inputPolyExpandedTargetTexture && _inputPairExpandedWeightsBuffer && _inputSpotlightTextureTopLeft && _inputSpotlightTextureTopEdge && _inputSpotlightTextureTopRight && _inputSpotlightTextureLeftEdge && _inputSpotlightTextureCentral && _inputSpotlightTextureRightEdge && _inputSpotlightTextureBottomLeft && _inputSpotlightTextureBottomEdge && _inputSpotlightTextureBottomRight is NULL"
+ "_integrateCoefficients is NULL"
+ "_integratedCoefficientsTexture is NULL"
+ "_interceptConfig is NULL"
+ "_internalSolverElemList nil"
+ "_internalTransformResults nil"
+ "_inverseGDCPipeline is NULL"
+ "_inverseGDCYUVPipeline is NULL"
+ "_kernel is NULL"
+ "_library is NULL"
+ "_linSysStatusFlagBuffer is NULL"
+ "_linearGuideTexture is NULL"
+ "_linearImageGlobalToneCurveTexture is NULL"
+ "_localHistogramStatsAll is NULL"
+ "_metalContext.allocator is NULL"
+ "_nccWorkStorage nil"
+ "_nonApplyComputePipelineStates[CalculateResidualPipelineState] is NULL"
+ "_nonApplyComputePipelineStates[FillLumaGradientHistogramPipelineState] is NULL"
+ "_nonApplyComputePipelineStates[FindMaxLumaGradient90ThPercentilePipelineState] is NULL"
+ "_nonReferencePyramidCorners[pyrLvl] is NULL"
+ "_nonReferencePyramidImage[pyrLvl] is NULL"
+ "_outputBuffer && _polynomialCount is NULL"
+ "_outputCodedLinearMetadata is NULL"
+ "_outputCodedLinearTexture is NULL"
+ "_outputImageTexture is NULL"
+ "_outputIntegratedCoefficientsTexture && _inputWeightPlanesTexture && _inputCoefficientsBuffer && _inputCoefficientsTexture is NULL"
+ "_params.imageSize.x && _params.imageSize.y && _params.spotlightCount.x && _params.spotlightCount.y && _outputSpotlightTextureTopLeft && _outputSpotlightTextureTopEdge && _outputSpotlightTextureTopRight && _outputSpotlightTextureLeftEdge && _outputSpotlightTextureCentral && _outputSpotlightTextureRightEdge && _outputSpotlightTextureBottomLeft && _outputSpotlightTextureBottomEdge && _outputSpotlightTextureBottomRight is NULL"
+ "_paramsBuf is NULL"
+ "_pipelineStates[SINGLE_COMPONENT_HISTOGRAM] is NULL"
+ "_pplnAffineSolver nil"
+ "_pplnCornerDetectionFinalPass nil"
+ "_pplnCornerDetectionFirstPass4x4 nil"
+ "_pplnCornerResponse nil"
+ "_pplnDownscale2to1 nil"
+ "_pplnDownscale2to1WithMapping nil"
+ "_pplnHomographySolver nil"
+ "_pplnNccMatch[] nil"
+ "_pplnRigidSolver nil"
+ "_pplnSimple3x3BoxFilter nil"
+ "_pplnSpecialImageConverterA nil"
+ "_pplnWarpImage nil"
+ "_pyramid1CornerResponse nil"
+ "_pyramid1Corners nil"
+ "_pyramid1Image[] nil"
+ "_pyramid1Initial nil"
+ "_pyramid2Corners nil"
+ "_pyramid2Image[] nil"
+ "_rangeAllocator is NULL"
+ "_reduceStep1Shader is NULL"
+ "_reduceStep2Shader is NULL"
+ "_referencePyramidCorners[pyrLvl] is NULL"
+ "_referencePyramidImage[pyrLvl] is NULL"
+ "_regEng nil"
+ "_renderSmartStylePipelineStateUsingImageBlock[0] is NULL"
+ "_renderSmartStylePipelineStateUsingImageBlock[1] is NULL"
+ "_renderSmartStylePipelineStateWithoutImageBlock[0] is NULL"
+ "_renderSmartStylePipelineStateWithoutImageBlock[1] is NULL"
+ "_renderWithColorCubesPipelineState[0] is NULL"
+ "_renderWithColorCubesPipelineState[1] is NULL"
+ "_renderWithColorPriorsPipelineState[0] is NULL"
+ "_renderWithColorPriorsPipelineState[1] is NULL"
+ "_renderingParamsFromStatsPipelineState is NULL"
+ "_resourcesAvailable is false"
+ "_rhsBuffer is NULL"
+ "_sampler[BiCubicSampler] is NULL"
+ "_sampler[BiLinearSampler] is NULL"
+ "_shaders is NULL"
+ "_sharedEventListener is NULL"
+ "_simpleDemosaicPipeline is NULL"
+ "_smallLightMapTexture is NULL"
+ "_smallLinearLightMapTexture is NULL"
+ "_solveLinearSystem is NULL"
+ "_srlApply is NULL"
+ "_srlCalcCoefficients is NULL"
+ "_srlCalcCoefficientsLivePhotos is NULL"
+ "_srlCalcPostSRLStats is NULL"
+ "_srlCoeffsBuffer is NULL"
+ "_srlFaceSparseHistogram is NULL"
+ "_srlFaceSparseHistogramLivePhotos is NULL"
+ "_srlFaceStatsBuffer is NULL"
+ "_srlGlobalSparseHistogram is NULL"
+ "_srlGlobalSparseHistogramLivePhotos is NULL"
+ "_srlGlobalStatsBuffer is NULL"
+ "_statistics is NULL"
+ "_statsBuf is NULL"
+ "_sumPersonAndSkinCounts is NULL"
+ "_texDesc is NULL"
+ "_textureDescriptor is NULL"
+ "_updateBaseGainWithStats is NULL"
+ "_utils is NULL"
+ "_warpPipeline is NULL"
+ "_warpWithGDCPipeline is NULL"
+ "accelRef is NULL"
+ "allocator is NULL"
+ "allocatorDesc is NULL"
+ "allocatorDescriptor is NULL"
+ "allocatorType == FigMetalAllocatorTypeHeap || allocatorType == FigMetalAllocatorTypeBuffer || allocatorType == FigMetalAllocatorTypeNoAliasing is NULL"
+ "appendString:"
+ "applyKernelPtr is NULL"
+ "bd is NULL"
+ "bd.length > 0 is NULL"
+ "blitEncoder is NULL"
+ "boxFilterBufferPointer: Not enough external memory provided"
+ "boxFilterBufferPointer: Unable to allocate memory"
+ "boxFilteredTexture is NULL"
+ "calculateTotalGain"
+ "cameraInfo is NULL"
+ "cameraInfo is nil"
+ "centerCropOffset is NULL"
+ "cmdBuf is NULL"
+ "cmdBuf nil"
+ "cmdBuffer is NULL"
+ "cmdEnc is NULL"
+ "cmdEnc nil"
+ "cmdEncoder is NULL"
+ "cmdbuf is NULL"
+ "cmissim_trace"
+ "coefficients_processor_trace"
+ "coefficients_ring_buffer_trace"
+ "commandBuffer is NULL"
+ "commandEncoder is NULL"
+ "commonInit inits failed"
+ "componentsJoinedByString:"
+ "computeCenterCropOffset"
+ "computeCroppedGridSize"
+ "computeEncoder is NULL"
+ "computeTransformInternal failed"
+ "computeTransformInternal() failed"
+ "config is NULL"
+ "constantValues nil"
+ "constants is NULL"
+ "context is nil, cannot proceed"
+ "cornerDetectIntermediateTexture is NULL"
+ "cornerResponseBufferPointer: Not enough external memory provided"
+ "cornerResponseBufferPointer: Unable to allocate memory"
+ "cornerResponseTexture is NULL"
+ "croppedGridSize is NULL"
+ "curve is NULL"
+ "dataBuffer is NULL"
+ "dataWindow from the coefficients ring buffer is empty"
+ "demosaicTex is NULL"
+ "desc.memSize > 0 is NULL"
+ "determineFirstPixel"
+ "determineFirstPixelForCVPixelFormat"
+ "determineFirstPixelForVersatileCVPixelBuffer"
+ "determineMTLPixelFormatsForCVPixelFormat"
+ "dstRect must be equivalent to the full destination buffer (or CGRectNull) when outputting a compressed pixel format."
+ "emptyCommandBuffer is NULL"
+ "encoder is NULL"
+ "err"
+ "err = FigSignalErrorAt3(\"%s%s%s signalled err=%d (%s) (%s) at %s:%d\", gStyleEngineProcessorTrace.note.emitter, (CMIStyleEngineStatusResourcesNotReleased), \"CMIStyleEngineStatusResourcesNotReleased\", (\"FigMetalAllocator resources not correctly released\"), \"<<<< StyleEngineProcessor >>>>\", __FUNCTION__, \"CMIStyleEngineProcessor.m\", 3020, __builtin_return_address(0), 0) == 0 "
+ "extrapolateAndCropSingleChannelGrid"
+ "factoriser is NULL"
+ "figmetalcontext_trace"
+ "filename is null"
+ "filter_coefficients"
+ "gdcParams is nil"
+ "getAllocatorMTLResourceSize"
+ "getBayerPatternForPixelBuffer"
+ "getDefaultStorageMode_block_invoke"
+ "getFloatParameter"
+ "getFloatValue"
+ "getMetalLumaFormat"
+ "getSensorDimensionsInBayerPixels"
+ "getSubArray"
+ "getSubDict"
+ "gridHeight outside allowed range"
+ "gridWidth outside allowed range"
+ "hd is NULL"
+ "heap is NULL"
+ "histEqLUT nil"
+ "histEqTex is NULL"
+ "histogram has all-zero values"
+ "histogram nil"
+ "hueSatLumLUTATex is NULL"
+ "hueSatLumLUTBTex is NULL"
+ "ibpErrCode_InternalError"
+ "ibpErrCode_MemoryAllocation"
+ "ibpErrCode_ObjectState"
+ "ibpErrCode_Parameter"
+ "ibpErrCode_ProcessFailed"
+ "image nil"
+ "imageHeight outside allowed range"
+ "imageWidth outside allowed range"
+ "imgFormat does not match configuration"
+ "imgHeight < 1"
+ "imgWidth < 1"
+ "inMatrix nil"
+ "inTexChma is not RG8Unorm"
+ "inTexLuma is not R8Unorm"
+ "inTextureLuma is not R8Unorm"
+ "indices is NULL"
+ "info >= 0 is NULL"
+ "inlierIndicesBuffer is NULL"
+ "inputROI not contained within inputTexture bounds"
+ "inputTexture must be set to calculate luma gradient based synthetic noise"
+ "integration spotlight ROI not contained within thumbnail size extent"
+ "inverseScalingLUT is NULL"
+ "ioSurface is NULL"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kCMISharpnessScoreError_AllocationFailed"
+ "kCMISharpnessScoreError_FailedToComputeSharpnessScore"
+ "kCMISharpnessScoreError_FailedToCreateCommandBuffer"
+ "kCMISharpnessScoreError_FailedToCreateComputeCommandEncoder"
+ "kCMISharpnessScoreError_FailedToCreateMetalTexture"
+ "kCMISharpnessScoreError_InvalidAllocator"
+ "kCMISharpnessScoreError_InvalidParameters"
+ "kCMISharpnessScoreError_InvalidRect"
+ "kCMIStatisticsError_FailedToBindPixelBuffer"
+ "kCMIStatisticsError_FailedToComputeStatistics"
+ "kCMIStatisticsError_FailedToCreateCommandBuffer"
+ "kCMIStatisticsError_FailedToCreateCommandEncoder"
+ "kFigBaseObjectError_AllocationFailed"
+ "kFigBaseObjectError_ParamErr"
+ "kFigBaseObjectError_UnsupportedOperation"
+ "keypoints nil"
+ "lhsDescriptor is NULL"
+ "lhsMatrix is NULL"
+ "linearStatsBuf is NULL"
+ "m2mcontroller_trace"
+ "metadata && outputBaselineExposure && outputBaseGain is NULL"
+ "metadata is NULL"
+ "metadata is nil"
+ "metal is nil"
+ "metalContext is NULL"
+ "metal_event_sync_trace"
+ "minNCCThreshold not between 0.0 and 1.0"
+ "mtlallocator_trace"
+ "newGlobalStatsBuffer is NULL"
+ "nonrefKeypoints is NULL"
+ "normNonReferenceCorners is NULL"
+ "normReferenceCorners is NULL"
+ "normalizedInputRectangle is invalid"
+ "numPyrLevel outside allowed range"
+ "outMatrix nil"
+ "outTexChma is not RG8Unorm"
+ "outTexLuma is not R8Unorm"
+ "outTotalCornerStrength nil"
+ "outputRGBTexture is NULL"
+ "outputSensorDimensionsInBayerPixels is NULL"
+ "p is NULL"
+ "params is NULL"
+ "pixel buffer is nil"
+ "pixelBuffer does not contain an IOSurface"
+ "pixelBuffer is null"
+ "pixelFormat not supported"
+ "plane < IOSurfaceGetPlaneCount(ioSurface) is NULL"
+ "plane == 0 is NULL"
+ "privEstimateAffineTransform"
+ "processNonReference::_convertTransform failed"
+ "processNonReference::constructPyramid failed"
+ "processReference::constructPyramid failed"
+ "processReference::detectCorners failed"
+ "pyramidLevel0Height exceeds configuration"
+ "pyramidLevel0Width exceeds configuration"
+ "queryCapabilities failed"
+ "refKeypoints is NULL"
+ "refinedResultBuffer is NULL"
+ "regionOfInterest.heihgt < 0"
+ "regionOfInterest.width < 0"
+ "regionOfInterest.x < 0"
+ "regionOfInterest.x >= image width"
+ "regionOfInterest.x+.width >= image width"
+ "regionOfInterest.y < 0"
+ "regionOfInterest.y >= image height"
+ "regionOfInterest.y+.height >= image height"
+ "resources NOT allocated"
+ "ret is NULL"
+ "rhsDescriptor is NULL"
+ "rhsMatrix is NULL"
+ "roi parameters has issues"
+ "rwppGeomTrans_estimateHomographyTransform"
+ "rwppGeomTrans_estimateRigidTransform"
+ "rwppGeomTrans_estimateRigidTransform2"
+ "rwppRegEngine_checkDefaults"
+ "rwppRegEngine_execute"
+ "rwppRegEngine_init"
+ "rwppRegEngine_reallocResources"
+ "rwppRunThreads"
+ "samplerDescriptor is NULL"
+ "searchRadius outside allowed range"
+ "self nil"
+ "self->subAllocator[subAllocatorID] is NULL"
+ "self.outputCoefficients && _outputStatus is NULL"
+ "self.rhsSize == CMIStyleEngineNumberOfTargetChannels is NULL"
+ "smallBgLTMGainMap is NULL"
+ "smallFgLTMGainMap is NULL"
+ "smart_style_pixel_buffer_render_trace"
+ "smart_style_proxy_render_trace"
+ "solutionMatrix is NULL"
+ "solver is NULL"
+ "solverParamsBuffer is NULL"
+ "solverResultsBuffer is NULL"
+ "solverSelector parameter has an invalid value"
+ "sourceComponent must be between 0 and 3"
+ "spotlightROI not contained within integrated coefficients extent"
+ "src is NULL."
+ "src/dstPixelBuffer have different width,height,format"
+ "srcPixelBuffer or dstPixelBuffer is NULL"
+ "statePtr && *statePtr is NULL"
+ "stereodisparity_gdc_trace"
+ "stride must be a multiple of pixelsize"
+ "style_engine_trace"
+ "subject_relighting_stage"
+ "td is NULL"
+ "td.desc.textureType == MTLTextureType2D || td.desc.textureType == MTLTextureType1D is NULL"
+ "templateRadius not one of 3,7,11"
+ "tex is NULL"
+ "texDesc is NULL"
+ "texDesc nil"
+ "texInTexture nil"
+ "texOutTexture1 nil"
+ "texOutTexture2 nil"
+ "texOutTexture3 nil"
+ "texture outside buffer bounds"
+ "textureDesc nil"
+ "textureDescriptor is NULL"
+ "thumbnailHDRLATexture is NULL"
+ "thumbnailNLGMTexture is NULL"
+ "thumbnailSDRLATexture is NULL"
+ "tmpBuffer is NULL"
+ "tmpData is NULL"
+ "transientMetalResources.activeInputs.activeWeightPlanesTexture is NULL"
+ "transientMetalResources.applicationResources.lumaGradientHistogramBuffer is NULL"
+ "transientMetalResources.applicationResources.maxLumaGradient90thPercentileBuffer is NULL"
+ "transientMetalResources.applicationResources.residualsTexture is NULL"
+ "transientMetalResources.inputThumbnailInstances.inputThumbnailTextureForLearning is NULL"
+ "transientMetalResources.inputThumbnailInstances.inputThumbnailTextureForResidualCorrection is NULL"
+ "transientMetalResources.inputThumbnailInstances.inputThumbnailTextureForWeightPlanesForIntegration is NULL"
+ "transientMetalResources.inputThumbnailInstances.inputThumbnailTextureForWeightPlanesForLearning is NULL"
+ "transientMetalResources.integrationResources.coefficientsTexture is NULL"
+ "transientMetalResources.solvingResources.linSysStatusBuffer is NULL"
+ "transientMetalResources.spotlightResources.spotlightBottomEdgeTexture is NULL"
+ "transientMetalResources.spotlightResources.spotlightBottomLeftTexture is NULL"
+ "transientMetalResources.spotlightResources.spotlightBottomRightTexture is NULL"
+ "transientMetalResources.spotlightResources.spotlightCentralTexture is NULL"
+ "transientMetalResources.spotlightResources.spotlightLeftEdgeTexture is NULL"
+ "transientMetalResources.spotlightResources.spotlightRightEdgeTexture is NULL"
+ "transientMetalResources.spotlightResources.spotlightTopEdgeTexture is NULL"
+ "transientMetalResources.spotlightResources.spotlightTopLeftTexture is NULL"
+ "transientMetalResources.spotlightResources.spotlightTopRightTexture is NULL"
+ "transientMetalResources.systemBuildupResources.lhsBuffer is NULL"
+ "transientMetalResources.systemBuildupResources.lhsDiagSumsBuffer is NULL"
+ "transientMetalResources.systemBuildupResources.pairExpandedWeightsBuffer is NULL"
+ "transientMetalResources.systemBuildupResources.polyExpandedInputBuffer is NULL"
+ "transientMetalResources.systemBuildupResources.polyExpandedTargetTexture is NULL"
+ "transientMetalResources.systemBuildupResources.priorFactorForLHSBuffer is NULL"
+ "transientMetalResources.systemBuildupResources.priorFactorForRHSBuffer is NULL"
+ "transientMetalResources.targetThumbnailInstances.targetThumbnailTextureForLearning is NULL"
+ "transientMetalResources.targetThumbnailInstances.targetThumbnailTextureForResidualCorrection is NULL"
+ "transientMetalResources.weightPlaneResources.weightPlaneNormalisationBuffer is NULL"
+ "transientMetalResources.weightPlaneResources.weightPlaneThresholdCalculationBuffer is NULL"
+ "uncroppedGrid is nil"
+ "vnrprocessor_trace"
+ "zoom spotlight ROI not normalised"
+ "zoomROI not normalised"
- "err = FigSignalErrorAt((CMIStyleEngineStatusResourcesNotReleased), ((void*)0), ((void*)0), ((void*)0), ((void*)0), ((void*)0), 0, 0) == 0 "

```
