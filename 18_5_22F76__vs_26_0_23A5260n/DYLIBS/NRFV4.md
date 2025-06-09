## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-587.122.6.0.2
-  __TEXT.__text: 0x21fff4
-  __TEXT.__auth_stubs: 0xef0
-  __TEXT.__objc_methlist: 0xfd48
-  __TEXT.__const: 0x1026e0
-  __TEXT.__cstring: 0x2ccc4
-  __TEXT.__gcc_except_tab: 0x14e8
-  __TEXT.__oslogstring: 0x21c9c
+650.0.0.122.4
+  __TEXT.__text: 0x2d9054
+  __TEXT.__auth_stubs: 0xf20
+  __TEXT.__objc_methlist: 0x102d8
+  __TEXT.__const: 0x1027c8
+  __TEXT.__cstring: 0x5a241
+  __TEXT.__gcc_except_tab: 0x198c
+  __TEXT.__oslogstring: 0x4e548
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x4238
-  __TEXT.__objc_classname: 0x2d67
-  __TEXT.__objc_methname: 0x30552
-  __TEXT.__objc_methtype: 0x15610
-  __TEXT.__objc_stubs: 0x14780
-  __DATA_CONST.__got: 0xad8
-  __DATA_CONST.__const: 0x1210
+  __TEXT.__unwind_info: 0x4d18
+  __TEXT.__objc_classname: 0x2db7
+  __TEXT.__objc_methname: 0x3134c
+  __TEXT.__objc_methtype: 0x15e82
+  __TEXT.__objc_stubs: 0x14dc0
+  __DATA_CONST.__got: 0xc10
+  __DATA_CONST.__const: 0x12b8
   __DATA_CONST.__objc_classlist: 0xc98
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xe0
+  __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5f00
+  __DATA_CONST.__objc_selrefs: 0x60f0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x988
-  __DATA_CONST.__objc_arraydata: 0xd30
-  __AUTH_CONST.__auth_got: 0x788
-  __AUTH_CONST.__const: 0x7c0
-  __AUTH_CONST.__cfstring: 0x12280
-  __AUTH_CONST.__objc_const: 0x311f0
+  __DATA_CONST.__objc_superrefs: 0x9a0
+  __DATA_CONST.__objc_arraydata: 0xe40
+  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__const: 0x7e0
+  __AUTH_CONST.__cfstring: 0x12f20
+  __AUTH_CONST.__objc_const: 0x32558
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_arrayobj: 0x9d8
-  __AUTH_CONST.__objc_intobj: 0xa20
-  __AUTH_CONST.__objc_dictobj: 0x528
-  __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x32e8
-  __DATA.__data: 0xb30
-  __DATA.__common: 0x20
-  __DATA.__bss: 0x4
-  __DATA_DIRTY.__objc_data: 0x7530
+  __AUTH_CONST.__objc_arrayobj: 0xae0
+  __AUTH_CONST.__objc_intobj: 0xa50
+  __AUTH_CONST.__objc_floatobj: 0x60
+  __AUTH_CONST.__objc_dictobj: 0x550
+  __AUTH.__objc_data: 0x9b0
+  __DATA.__objc_ivar: 0x34b8
+  __DATA.__data: 0xb48
+  __DATA.__common: 0x30
+  __DATA.__bss: 0x14
+  __DATA_DIRTY.__objc_data: 0x7440
   __DATA_DIRTY.__bss: 0x150
-  __DATA_DIRTY.__common: 0xf0
+  __DATA_DIRTY.__common: 0x130
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6863DF08-C069-3D81-AB11-96D229A00498
-  Functions: 11371
-  Symbols:   35840
-  CStrings:  17451
+  UUID: 402A7122-A9C2-341F-8ADE-0F618CAB0DFD
+  Functions: 12518
+  Symbols:   37732
+  CStrings:  23511
 
Symbols:
+ +[ChromaticAberrationRecoveryConfig getCARConfigForInputFrame:staticParameters:bounds:carConfig:].cold.13
+ +[ChromaticAberrationRecoveryConfig getCARConfigForInputFrame:staticParameters:bounds:carConfig:].cold.14
+ +[LensShadingCorrectionConfig getLSCMetadata:lscMetadata:bounds:stageConfigMode:processingOptions:metalCtx:staticParameters:forAWB:].cold.49
+ +[PyramidStage prewarmShaders:].cold.2
+ +[PyramidStageShared compileShader:lumaWrite:chromaWrite:error:]
+ +[PyramidStageShared compileShader:lumaWrite:chromaWrite:error:].cold.1
+ +[RawDFLanczos prewarmShaders:]
+ +[RawDFLanczos prewarmShaders:].cold.1
+ +[RawDFNetworkStage prewarmShaders:].cold.5
+ +[RawDFNetworkStage prewarmShaders:].cold.6
+ +[RawDFNetworkStageTuningParams calculateShaderUniformsForNetworkPipeline:tuningParams:networkType:frameMeta:textureDimensions:outNetworkUniforms:].cold.1
+ +[RawDFNetworkStageTuningParams calculateShaderUniformsForNetworkPipeline:tuningParams:networkType:frameMeta:textureDimensions:outNetworkUniforms:].cold.2
+ +[RawDFNetworkStageTuningParams calculateShaderUniformsForNetworkPipeline:tuningParams:networkType:frameMeta:textureDimensions:outNetworkUniforms:].cold.3
+ +[RawDFNetworkStageTuningParams calculateShaderUniformsForNetworkPipeline:tuningParams:networkType:frameMeta:textureDimensions:outNetworkUniforms:].cold.4
+ +[RawDFNetworkStageTuningParams calculateShaderUniformsForNetworkPipeline:tuningParams:networkType:frameMeta:textureDimensions:outNetworkUniforms:].cold.5
+ +[RawDFNetworkStageTuningParams calculateShaderUniformsForNetworkPipeline:tuningParams:networkType:frameMeta:textureDimensions:outNetworkUniforms:].cold.6
+ +[RawDFProxyStage fillFrameProperties:withEvmProperties:withEv0Properties:].cold.1
+ +[RawDFProxyStage fillFrameProperties:withEvmProperties:withEv0Properties:].cold.2
+ +[RawDFSyntheticLongStage fillFrameProperties:withEv0Properties:withLongProperties:ev0Count:].cold.1
+ +[RawDFSyntheticLongStage fillFrameProperties:withEv0Properties:withLongProperties:ev0Count:].cold.2
+ +[RawDFSyntheticLongStage fillFrameProperties:withEv0Properties:withLongProperties:ev0Count:].cold.3
+ +[RawDFSyntheticLongStage fillFrameProperties:withEv0Properties:withLongProperties:ev0Count:].cold.4
+ +[RawDFSyntheticReferenceShadersCRG isValidFunctionConstantCombo:]
+ +[RawDFSyntheticReferenceStageCRG prewarmShaders:]
+ +[RawNightModeInferenceCommon getLSCParams:fromMetadata:fromCameraInfoByPortType:fromLSCGainMapParameters:].cold.10
+ +[RawProcInputFrame getMetalFormat:]
+ +[RawProcInputFrame isVersatileRegroupedRawFormat:]
+ +[RegDense getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:outRegDenseMapProperties:]
+ +[RegDense getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:outRegDenseMapProperties:].cold.1
+ +[RegDense getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:outRegDenseMapProperties:].cold.2
+ +[RegDense getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:outRegDenseMapProperties:].cold.3
+ +[RegDense getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:outRegDenseMapProperties:].cold.4
+ +[SoftLTM copyTotalSensorCropRectFrom:to:]
+ -[BilateralGrid solverPcg:].cold.14
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.1
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.10
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.11
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.12
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.2
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.3
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.4
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.5
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.6
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.7
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.8
+ -[BilateralGrid solverfilter:target:confidence:output:].cold.9
+ -[BilateralGrid solverfilterWithGuide:target:confidence:ltc_tex:gtcRatio_tex:gtcFinal_tex:ltmROI:output:].cold.1
+ -[BilateralGrid solverfilterWithGuide:target:confidence:ltc_tex:gtcRatio_tex:gtcFinal_tex:ltmROI:output:].cold.2
+ -[BilateralGrid solverfilterWithGuide:target:confidence:ltc_tex:gtcRatio_tex:gtcFinal_tex:ltmROI:output:].cold.3
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.10
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.11
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.12
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.13
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.3
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.4
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.5
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.6
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.7
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.8
+ -[CMIDraftDemosaicStage initWithMetalContext:].cold.9
+ -[CMIPost getSrlBoostedLTMasNSData:]
+ -[CMIRawNightModeRegistrationStage prepareWithImageWidth:imageHeight:registrationType:gdcMode:cameraInfoByPortType:].cold.7
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.1
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.10
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.11
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.12
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.13
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.14
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.15
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.16
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.17
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.18
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.19
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.2
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.20
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.21
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.22
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.23
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.24
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.25
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.26
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.27
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.28
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.29
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.3
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.30
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.31
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.32
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.33
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.34
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.35
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.4
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.5
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.6
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.7
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.8
+ -[CMISoftwareFlashRenderingProcessorV2 process].cold.9
+ -[CMISoftwareFlashRenderingProcessorV2 requiredMetalAllocatorMemorySize]
+ -[CMITiledInferenceProcessorStage getFinalProcessingStatus]
+ -[CMITiledInferenceProcessorStage init]
+ -[CMITiledInferenceProcessorStage resetFinalProcessingStatus]
+ -[CMITiledInferenceProcessorStage runProcessor:withTileCount:]
+ -[DeepFusionPrepareDescriptor description]
+ -[DeepFusionProcessor _demosaicAndProcessFrame:toTexture:withWarpFrame:].cold.1
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.1
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.10
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.11
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.12
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.13
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.14
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.15
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.2
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.3
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.4
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.5
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.6
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.7
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.8
+ -[DeepFusionProcessor _finalizeQuadraSfdStep1:].cold.9
+ -[DeepFusionProcessor _initiateQuadraEVZeroBackgroundProcessing].cold.1
+ -[DeepFusionProcessor _initiateQuadraEVZeroBackgroundProcessing].cold.2
+ -[DeepFusionProcessor _initiateQuadraEVZeroBackgroundProcessing].cold.3
+ -[DeepFusionProcessor _initiateQuadraEVZeroBackgroundProcessing].cold.4
+ -[DeepFusionProcessor _initiateQuadraEVZeroBackgroundProcessing].cold.5
+ -[DeepFusionProcessor _initiateQuadraEVZeroBackgroundProcessing].cold.6
+ -[DeepFusionProcessor _initiateQuadraEVZeroBackgroundProcessing].cold.7
+ -[DeepFusionProcessor _initiateQuadraEVZeroBackgroundProcessing].cold.8
+ -[DeepFusionProcessor _initiateQuadraEVZeroBackgroundProcessing].cold.9
+ -[DeepFusionProcessor _registerImages:].cold.1
+ -[DeepFusionProcessor _setupPostConfig:isForEnhancedRes:].cold.1
+ -[DeepFusionProcessor _setupPostConfig:isForEnhancedRes:].cold.2
+ -[DeepFusionProcessor createDraftDemosaicTextureForFrame:outputROI:].cold.4
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.1
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.10
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.11
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.12
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.13
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.14
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.15
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.16
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.17
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.18
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.19
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.2
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.20
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.21
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.22
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.23
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.24
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.3
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.4
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.5
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.6
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.7
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.8
+ -[DeepFusionProcessor generateSyntheticLongToOutput:].cold.9
+ -[DeepFusionProcessor generateSyntheticReference:].cold.1
+ -[DeepFusionProcessor generateSyntheticReference:].cold.10
+ -[DeepFusionProcessor generateSyntheticReference:].cold.2
+ -[DeepFusionProcessor generateSyntheticReference:].cold.3
+ -[DeepFusionProcessor generateSyntheticReference:].cold.4
+ -[DeepFusionProcessor generateSyntheticReference:].cold.5
+ -[DeepFusionProcessor generateSyntheticReference:].cold.6
+ -[DeepFusionProcessor generateSyntheticReference:].cold.7
+ -[DeepFusionProcessor generateSyntheticReference:].cold.8
+ -[DeepFusionProcessor generateSyntheticReference:].cold.9
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.1
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.10
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.11
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.12
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.13
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.14
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.15
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.2
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.3
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.4
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.5
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.6
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.7
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.8
+ -[DeepFusionProcessor generateSyntheticReferenceWithSIFR:].cold.9
+ -[DeepFusionProcessor setupWithOptions:].cold.1
+ -[DeepFusionProcessor setupWithOptions:].cold.10
+ -[DeepFusionProcessor setupWithOptions:].cold.11
+ -[DeepFusionProcessor setupWithOptions:].cold.2
+ -[DeepFusionProcessor setupWithOptions:].cold.3
+ -[DeepFusionProcessor setupWithOptions:].cold.4
+ -[DeepFusionProcessor setupWithOptions:].cold.5
+ -[DeepFusionProcessor setupWithOptions:].cold.6
+ -[DeepFusionProcessor setupWithOptions:].cold.7
+ -[DeepFusionProcessor setupWithOptions:].cold.8
+ -[DeepFusionProcessor setupWithOptions:].cold.9
+ -[DenoiseFusePipeline addFrame:cfp:processingType:createPyramid:batchCount:].cold.1
+ -[DenoiseFusePipeline addFrame:cfp:processingType:createPyramid:batchCount:].cold.2
+ -[DenoiseFusePipeline addFrame:cfp:processingType:createPyramid:batchCount:].cold.3
+ -[DenoiseFusePipeline addFrame:cfp:processingType:createPyramid:batchCount:].cold.4
+ -[DenoiseFusePipeline addFrame:cfp:processingType:createPyramid:batchCount:].cold.5
+ -[DenoiseFusePipeline addFrame:cfp:processingType:createPyramid:batchCount:].cold.6
+ -[DenoiseFusePipeline convertHLGToSDRWithInputPixelBuffer:outputImage:]
+ -[DenoiseFusePipeline convertHLGToSDRWithInputPixelBuffer:outputImage:].cold.1
+ -[DenoiseFusePipeline convertHLGToSDRWithInputPixelBuffer:outputImage:].cold.2
+ -[DenoiseFusePipeline convertHLGToSDRWithInputPixelBuffer:outputImage:].cold.3
+ -[DenoiseFusePipeline convertHLGToSDRWithInputPixelBuffer:outputImage:].cold.4
+ -[DenoiseFusePipeline denoiseSingleImage:linearOutput:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:input:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:].cold.1
+ -[DenoiseFusePipeline denoiseSingleImage:linearOutput:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:input:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:].cold.2
+ -[DenoiseFusePipeline denoiseSingleImage:linearOutput:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:input:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:].cold.3
+ -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:]
+ -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:].cold.1
+ -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:].cold.2
+ -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:].cold.3
+ -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:].cold.4
+ -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:].cold.5
+ -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:].cold.6
+ -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:].cold.7
+ -[DenoiseFusePipeline getSrlBoostedLTMasNSData:]
+ -[DenoiseFusePipeline isLTMOnFinalEnabled:]
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:]
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.1
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.10
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.2
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.3
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.4
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.5
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.6
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.7
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.8
+ -[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:].cold.9
+ -[DenoiseFusePipeline toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:].cold.1
+ -[DenoiseFusePipeline toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:].cold.2
+ -[DenoiseFusePipeline toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:].cold.3
+ -[DenoiseFusePipeline toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:].cold.4
+ -[DenoiseFusePipeline toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:].cold.5
+ -[DenoiseFusePipeline toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:].cold.6
+ -[DenoiseFusePipeline toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:].cold.7
+ -[DenoiseFusePipeline waitForSFDToFinishWithFrameIndex:frameProperties:].cold.1
+ -[DenoiseFusePipeline waitForSFDToFinishWithFrameIndex:frameProperties:].cold.2
+ -[DenoiseRemixFragmentShader initWithMetal:vertName:fragName:pixelFormat:pixelFormat2:]
+ -[DenoiseRemixFragmentShader initWithMetal:vertName:fragName:pixelFormat:pixelFormat2:].cold.1
+ -[DenoiseRemixFragmentShader initWithMetal:vertName:fragName:pixelFormat:pixelFormat2:].cold.2
+ -[DenoiseRemixShaders initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:]
+ -[DenoiseRemixShaders initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:].cold.1
+ -[DenoiseRemixShaders initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:].cold.2
+ -[DenoiseRemixShaders initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:].cold.3
+ -[DenoiseRemixShaders initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:].cold.4
+ -[DenoiseRemixShaders initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:].cold.5
+ -[DenoiseRemixShaders initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:].cold.6
+ -[DenoiseRemixShaders initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:].cold.7
+ -[DisparityConfig determineDemosaicParameters:inputFrame:bounds:].cold.10
+ -[DisparityConfig determineDemosaicParameters:inputFrame:bounds:].cold.9
+ -[DisparityStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[DisparityStage runWithArgs:].cold.5
+ -[DisparityStage validateInputFrame:config:].cold.2
+ -[GDCStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[GDCStage runWithArgs:].cold.10
+ -[GDCStage runWithArgs:].cold.11
+ -[GDCStage runWithArgs:].cold.12
+ -[GDCStage runWithArgs:].cold.13
+ -[GDCStage runWithArgs:].cold.14
+ -[GDCStage runWithArgs:].cold.15
+ -[GDCStage runWithArgs:].cold.16
+ -[GDCStage runWithArgs:].cold.7
+ -[GDCStage runWithArgs:].cold.8
+ -[GDCStage runWithArgs:].cold.9
+ -[GDCStage validateInputFrame:config:].cold.2
+ -[GainMapShaders initWithMetal:].cold.14
+ -[GainMapShaders initWithMetal:].cold.15
+ -[GainMapShaders initWithMetal:].cold.16
+ -[GainMapShaders initWithMetal:].cold.17
+ -[GainMapShaders initWithMetal:].cold.18
+ -[GainMapShaders initWithMetal:].cold.19
+ -[GainMapShaders initWithMetal:].cold.20
+ -[GainMapStage computeAverageCurve:withLTM:ltmGridX:ltmGridY:andGTC:andLtmHardGain:]
+ -[GainMapStage computeGainMapWithInput:secondInput:HLGLumaAInput:output:properties:mpconfig:]
+ -[GainMapStage computeGainMapWithInput:secondInput:HLGLumaAInput:output:properties:mpconfig:].cold.1
+ -[GainMapStage computeGainMapWithInput:secondInput:HLGLumaAInput:output:properties:mpconfig:].cold.2
+ -[GainMapStage computeGainMapWithInput:secondInput:HLGLumaAInput:output:properties:mpconfig:].cold.3
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:]
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.1
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.10
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.11
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.12
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.13
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.14
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.2
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.3
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.4
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.5
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.6
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.7
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.8
+ -[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:].cold.9
+ -[GainMapStage flexRangeMetadataDictionary:mppHeadroom:newHeadroom:fullRange:]
+ -[GainMapStage normalizeLTMTable:ltmGridX:ltmGridY:ltmBinsNumber:]
+ -[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:]
+ -[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.1
+ -[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.2
+ -[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.3
+ -[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.4
+ -[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.5
+ -[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.6
+ -[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.7
+ -[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.8
+ -[GainMapStage setGainMapConfig:tuning:frameMetadata:width:height:isLinear:hasHDR:]
+ -[GainMapStage setGainMapConfig:tuning:frameMetadata:width:height:isLinear:hasHDR:].cold.1
+ -[GainMapStage setGainMapConfig:tuning:frameMetadata:width:height:isLinear:hasHDR:].cold.2
+ -[GainMapStage setGainMapConfig:tuning:frameMetadata:width:height:isLinear:hasHDR:].cold.3
+ -[GainMapStage setGainMapConfig:tuning:frameMetadata:width:height:isLinear:hasHDR:].cold.4
+ -[H13FastBayerProcConfig(HR) determineHPBLUTFromRegisters:hpbLUT:].cold.4
+ -[H13FastBayerProcConfig(HR) determineHPBLUTFromRegisters:hpbLUT:].cold.5
+ -[H13FastBayerProcConfig(HR) determineMixClipLUTFromInputFrame:mixClipLUT:].cold.2
+ -[H13FastBayerProcConfig(HR) determineMixClipLUTFromInputFrame:mixClipLUT:].cold.3
+ -[H13FastBayerProcConfig(HR) determineSoftClipLUTFromRegisters:softClipLUT:].cold.4
+ -[H13FastBayerProcConfig(HR) determineSoftClipLUTFromRegisters:softClipLUT:].cold.5
+ -[H13FastBayerProcConfig(Huemap) getHuemapMotionCompensationConfigForInputFrame:huemapMotionCompensationConfig:].cold.9
+ -[H13FastBayerProcStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13FastBayerProcStage isSSCAccountedForInBytesRequiredForConfig:]
+ -[H13FastBayerProcStage validateInputFrame:config:].cold.2
+ -[H13FastBayerProcStage(DraftDemosaic) runDraftDemosaicWithArgs:inputTexture:outputFrame:outputMetadata:isQuadra:].cold.10
+ -[H13FastBayerProcStage(DraftDemosaic) runDraftDemosaicWithArgs:inputTexture:outputFrame:outputMetadata:isQuadra:].cold.11
+ -[H13FastBayerProcStage(DraftDemosaic) runDraftDemosaicWithArgs:inputTexture:outputFrame:outputMetadata:isQuadra:].cold.12
+ -[H13FastBayerProcStage(DraftDemosaic) runDraftDemosaicWithArgs:inputTexture:outputFrame:outputMetadata:isQuadra:].cold.13
+ -[H13FastCanvasStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13FastCanvasStage validateInputFrame:config:].cold.2
+ -[H13FastDemosaicStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13FastDemosaicStage runWithArgs:].cold.10
+ -[H13FastDemosaicStage runWithArgs:].cold.4
+ -[H13FastDemosaicStage runWithArgs:].cold.5
+ -[H13FastDemosaicStage runWithArgs:].cold.6
+ -[H13FastDemosaicStage runWithArgs:].cold.7
+ -[H13FastDemosaicStage runWithArgs:].cold.8
+ -[H13FastDemosaicStage runWithArgs:].cold.9
+ -[H13FastDemosaicStage validateInputFrame:config:].cold.2
+ -[H13FastDemosaicStageMetal createIntermediateMetalTexture:pixelFormat:width:height:].cold.2
+ -[H13FastDemosaicStageMetal runWithInputTex:demosaicConfig:outputSize:outputTexY:outputTexUV:commandBuffer:].cold.2
+ -[H13FastDemosaicStageMetal runWithInputTex:demosaicConfig:outputSize:outputTexY:outputTexUV:commandBuffer:].cold.3
+ -[H13FastDemosaicStageMetal runWithInputTex:demosaicConfig:outputSize:outputTexY:outputTexUV:commandBuffer:].cold.4
+ -[H13FastDemosaicStageMetal runWithInputTex:demosaicConfig:outputSize:outputTexY:outputTexUV:commandBuffer:].cold.5
+ -[H13FastLTMStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13FastLTMStage runWithArgs:].cold.1
+ -[H13FastLTMStage runWithArgs:].cold.10
+ -[H13FastLTMStage runWithArgs:].cold.11
+ -[H13FastLTMStage runWithArgs:].cold.12
+ -[H13FastLTMStage runWithArgs:].cold.13
+ -[H13FastLTMStage runWithArgs:].cold.14
+ -[H13FastLTMStage runWithArgs:].cold.15
+ -[H13FastLTMStage runWithArgs:].cold.16
+ -[H13FastLTMStage runWithArgs:].cold.17
+ -[H13FastLTMStage runWithArgs:].cold.18
+ -[H13FastLTMStage runWithArgs:].cold.19
+ -[H13FastLTMStage runWithArgs:].cold.2
+ -[H13FastLTMStage runWithArgs:].cold.20
+ -[H13FastLTMStage runWithArgs:].cold.21
+ -[H13FastLTMStage runWithArgs:].cold.3
+ -[H13FastLTMStage runWithArgs:].cold.4
+ -[H13FastLTMStage runWithArgs:].cold.5
+ -[H13FastLTMStage runWithArgs:].cold.6
+ -[H13FastLTMStage runWithArgs:].cold.7
+ -[H13FastLTMStage runWithArgs:].cold.8
+ -[H13FastLTMStage runWithArgs:].cold.9
+ -[H13FastLTMStage validateInputFrame:config:].cold.2
+ -[H13FastLumaSharpeningStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13FastLumaSharpeningStage runWithArgs:].cold.5
+ -[H13FastLumaSharpeningStage validateInputFrame:config:].cold.2
+ -[H13FastOutlierPixelCorrectionStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13FastOutlierPixelCorrectionStage runWithArgs:].cold.8
+ -[H13FastOutlierPixelCorrectionStage validateInputFrame:config:].cold.2
+ -[H13FastOutlierPixelCorrectionStageMetal runWithConfig:inputTex:outputTex:].cold.5
+ -[H13FastPostDemosaicProcConfig(PostDemosaic) getPostDemosaicProcConfigForInputFrame:postDemosaicProcConfig:chromaSuppressionConfig:].cold.5
+ -[H13FastPostDemosaicProcMetal createIntermediateMetalTexture:pixelFormat:width:height:].cold.2
+ -[H13FastPostDemosaicProcStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13FastPostDemosaicProcStage createIntermediateMetalTexture:pixelFormat:width:height:].cold.2
+ -[H13FastPostDemosaicProcStage runWithArgs:].cold.4
+ -[H13FastPostDemosaicProcStage runWithArgs:].cold.5
+ -[H13FastPostDemosaicProcStage runWithArgs:].cold.6
+ -[H13FastPostDemosaicProcStage runWithArgs:].cold.7
+ -[H13FastPostDemosaicProcStage runWithArgs:].cold.8
+ -[H13FastPostDemosaicProcStage validateInputFrame:config:].cold.2
+ -[H13FastRawMBNRStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13FastRawMBNRStage validateInputFrame:config:].cold.2
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.10
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.11
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.12
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.13
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.14
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.15
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.16
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.17
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.18
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.19
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.20
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.21
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.22
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.23
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.24
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.25
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.26
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.27
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.28
+ -[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:].cold.9
+ -[H13FastRawScaleConfig(ABLEST) getABLESTEnabledForInputFrame:enabled:].cold.7
+ -[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationConfigForInputFrame:pdpConfig:blackLevelEstimationConfig:].cold.10
+ -[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationConfigForInputFrame:pdpConfig:blackLevelEstimationConfig:].cold.11
+ -[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationConfigForInputFrame:pdpConfig:blackLevelEstimationConfig:].cold.7
+ -[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationConfigForInputFrame:pdpConfig:blackLevelEstimationConfig:].cold.8
+ -[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationConfigForInputFrame:pdpConfig:blackLevelEstimationConfig:].cold.9
+ -[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationEnabledForInputFrame:enabled:].cold.5
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:]
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:].cold.1
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:].cold.2
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:].cold.3
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:].cold.4
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:].cold.5
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:].cold.6
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionEnabledForInputFrame:enabled:]
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionEnabledForInputFrame:enabled:].cold.1
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionEnabledForInputFrame:enabled:].cold.2
+ -[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionEnabledForInputFrame:enabled:].cold.3
+ -[H13FastRawScaleConfig(PDP) getPDPGainsForInputFrame:pdpGainsTex:].cold.15
+ -[H13FastRawScaleShaders focusPixelDeltaBlurMap]
+ -[H13FastRawScaleShaders focusPixelDeltaMap]
+ -[H13FastRawScaleShaders focusPixelExtractionQuadra]
+ -[H13FastRawScaleShaders focusPixelExtraction]
+ -[H13FastRawScaleShaders hazeCorrectionQuadra]
+ -[H13FastRawScaleShaders hazeCorrection]
+ -[H13FastRawScaleShaders hazeDetection]
+ -[H13FastRawScaleShaders hazeDomination]
+ -[H13FastRawScaleShaders maxScaling]
+ -[H13FastRawScaleShaders rgbThumbnailQuadra]
+ -[H13FastRawScaleShaders rgbThumbnail]
+ -[H13FastRawScaleShaders sumTexture]
+ -[H13FastRawScaleStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13FastRawScaleStage runWithArgs:].cold.41
+ -[H13FastRawScaleStage runWithArgs:].cold.42
+ -[H13FastRawScaleStage runWithArgs:].cold.43
+ -[H13FastRawScaleStage validateInputFrame:config:].cold.2
+ -[H13FastRawScaleStage(ABLEST) runABLESTWithConfig:inOutTexture:].cold.13
+ -[H13FastRawScaleStage(FPExtract) copySashimiTextureToAuxiliaryWithConfig:inputTexture:].cold.12
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:]
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:].cold.1
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:].cold.2
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:].cold.3
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:].cold.4
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:].cold.5
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:].cold.6
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:].cold.7
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:].cold.8
+ -[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:].cold.9
+ -[H13UtilityConvertStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[H13UtilityConvertStage runWithArgs:].cold.7
+ -[H13UtilityConvertStage runWithArgs:].cold.8
+ -[H13UtilityConvertStage validateInputFrame:config:].cold.2
+ -[LearnedNRBoundInferenceResults .cxx_destruct]
+ -[LearnedNRBoundInferenceResults initWithResult:andMetal:]
+ -[LearnedNRBoundInferenceResults initWithResult:andMetal:].cold.1
+ -[LearnedNRBoundInferenceResults initWithResult:andMetal:].cold.2
+ -[LearnedNRBoundInferenceResults initWithResult:andMetal:].cold.3
+ -[LearnedNRBoundInferenceResults initWithResult:andMetal:].cold.4
+ -[LearnedNRBoundInferenceResults initWithResult:andMetal:].cold.5
+ -[LearnedNRBoundInferenceResults initWithResult:andMetal:].cold.6
+ -[LearnedNRBoundInferenceResults instanceMasks]
+ -[LearnedNRBoundInferenceResults personMask]
+ -[LearnedNRBoundInferenceResults setInstanceMasks:]
+ -[LearnedNRBoundInferenceResults setPersonMask:]
+ -[LearnedNRBoundInferenceResults setSkinMask:]
+ -[LearnedNRBoundInferenceResults setSkyMask:]
+ -[LearnedNRBoundInferenceResults skinMask]
+ -[LearnedNRBoundInferenceResults skyMask]
+ -[LearnedNRNetworkConfig deviceGeneration]
+ -[LearnedNRNetworkConfig init]
+ -[LearnedNRNetworkConfig isQuadra]
+ -[LearnedNRNetworkConfig setDeviceGeneration:]
+ -[LearnedNRNetworkConfig setIsQuadra:]
+ -[LearnedNRNetworkShared networkModel]
+ -[LearnedNRNetworkShared setNetworkModel:]
+ -[LearnedNRNetworkShared setTileOverlap:]
+ -[LearnedNRNetworkShared tileOverlap]
+ -[LearnedNRNetworkStage _getTotalGainFromMetadata:]
+ -[LearnedNRNetworkStage getTileOverlapForGain:table:]
+ -[LearnedNRNetworkStage initWithContext:cameraInfo:config:]
+ -[LearnedNRNetworkStage initWithContext:cameraInfo:config:].cold.1
+ -[LearnedNRNetworkStage initWithContext:cameraInfo:config:].cold.2
+ -[LearnedNRNetworkStage initWithContext:cameraInfo:config:].cold.3
+ -[LearnedNRNetworkStage initWithContext:cameraInfo:config:].cold.4
+ -[LearnedNRNetworkStage initWithContext:cameraInfo:config:].cold.5
+ -[LearnedNRNetworkStage initWithContext:cameraInfo:config:].cold.6
+ -[LearnedNRNetworkStage initWithContext:cameraInfo:config:].cold.7
+ -[LearnedNRNetworkStage initWithContext:cameraInfo:config:].cold.8
+ -[LearnedNRNetworkStage updateParametersFromMetadata:outputGain:bayerPattern:lscGainMapBuffer:lscGainMapParameters:]
+ -[LearnedNRNetworkStage updateParametersFromMetadata:outputGain:bayerPattern:lscGainMapBuffer:lscGainMapParameters:].cold.1
+ -[LearnedNRNetworkStage updateParametersFromMetadata:outputGain:bayerPattern:lscGainMapBuffer:lscGainMapParameters:].cold.2
+ -[LearnedNRNetworkStage updateParametersFromMetadata:outputGain:bayerPattern:lscGainMapBuffer:lscGainMapParameters:].cold.3
+ -[LearnedNRNetworkStage updateParametersFromMetadata:outputGain:bayerPattern:lscGainMapBuffer:lscGainMapParameters:].cold.4
+ -[LearnedNRNetworkTuningParams readPlist:].cold.6
+ -[LearnedNRNetworkTuningParams readPlist:].cold.7
+ -[LearnedNRProcessor .cxx_destruct]
+ -[LearnedNRProcessor _isGainMapSupported]
+ -[LearnedNRProcessor _isSemanticStylesSupported]
+ -[LearnedNRProcessor _prepareOutputMetadata:]
+ -[LearnedNRProcessor _prepareOutputMetadata:].cold.1
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:]
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.1
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.10
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.2
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.3
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.4
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.5
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.6
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.7
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.8
+ -[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:].cold.9
+ -[LearnedNRProcessor addFrame:]
+ -[LearnedNRProcessor addFrame:].cold.1
+ -[LearnedNRProcessor addFrame:].cold.2
+ -[LearnedNRProcessor addFrame:].cold.3
+ -[LearnedNRProcessor addInputResource:]
+ -[LearnedNRProcessor addInputResource:].cold.1
+ -[LearnedNRProcessor addInputResource:].cold.2
+ -[LearnedNRProcessor addInputResource:].cold.3
+ -[LearnedNRProcessor addInputResource:].cold.4
+ -[LearnedNRProcessor addInputResource:].cold.5
+ -[LearnedNRProcessor addToSidecar:forKey:]
+ -[LearnedNRProcessor allocatorBackend]
+ -[LearnedNRProcessor applyOverrides]
+ -[LearnedNRProcessor batchCount]
+ -[LearnedNRProcessor bindResourcesForProcessingType:prepareDescriptor:]
+ -[LearnedNRProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:]
+ -[LearnedNRProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:].cold.1
+ -[LearnedNRProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:].cold.2
+ -[LearnedNRProcessor cameraInfoByPortType]
+ -[LearnedNRProcessor cntBracketSampleBuffers]
+ -[LearnedNRProcessor dealloc]
+ -[LearnedNRProcessor defringingTuningByPortType]
+ -[LearnedNRProcessor delegate]
+ -[LearnedNRProcessor description]
+ -[LearnedNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:]
+ -[LearnedNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.1
+ -[LearnedNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.2
+ -[LearnedNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.3
+ -[LearnedNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:]
+ -[LearnedNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.1
+ -[LearnedNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.2
+ -[LearnedNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.3
+ -[LearnedNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.4
+ -[LearnedNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.5
+ -[LearnedNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.6
+ -[LearnedNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.7
+ -[LearnedNRProcessor doRedFaceFix]
+ -[LearnedNRProcessor enableGreenGhostMitigation]
+ -[LearnedNRProcessor finishProcessing]
+ -[LearnedNRProcessor finishScheduling]
+ -[LearnedNRProcessor generateGainMapIfNeeded]
+ -[LearnedNRProcessor generateGainMapIfNeeded].cold.1
+ -[LearnedNRProcessor generateGainMapIfNeeded].cold.2
+ -[LearnedNRProcessor generateGainMapIfNeeded].cold.3
+ -[LearnedNRProcessor generateGainMapIfNeeded].cold.4
+ -[LearnedNRProcessor initWithCommandQueue:]
+ -[LearnedNRProcessor initWithCommandQueue:].cold.1
+ -[LearnedNRProcessor maximumNumberOfReferenceFrameCandidatesToHoldForProcessing]
+ -[LearnedNRProcessor metalCommandQueue]
+ -[LearnedNRProcessor output]
+ -[LearnedNRProcessor prepareBand1InputWithBand0:]
+ -[LearnedNRProcessor prepareToProcess:]
+ -[LearnedNRProcessor prepareToProcess:prepareDescriptor:]
+ -[LearnedNRProcessor prepareToProcess:prepareDescriptor:].cold.1
+ -[LearnedNRProcessor prepareToProcess:prepareDescriptor:].cold.2
+ -[LearnedNRProcessor prepareToProcess:prepareDescriptor:].cold.3
+ -[LearnedNRProcessor prepareToProcess:prepareDescriptor:].cold.4
+ -[LearnedNRProcessor prewarmWithTuningParameters:]
+ -[LearnedNRProcessor prewarm]
+ -[LearnedNRProcessor prewarm].cold.1
+ -[LearnedNRProcessor prewarm].cold.2
+ -[LearnedNRProcessor process]
+ -[LearnedNRProcessor process].cold.1
+ -[LearnedNRProcessor process].cold.2
+ -[LearnedNRProcessor process].cold.3
+ -[LearnedNRProcessor process].cold.4
+ -[LearnedNRProcessor process].cold.5
+ -[LearnedNRProcessor processingType]
+ -[LearnedNRProcessor purgeResources]
+ -[LearnedNRProcessor referenceFrameCandidatesCount]
+ -[LearnedNRProcessor referenceFrameHasEVMinus]
+ -[LearnedNRProcessor referenceFrameIndex]
+ -[LearnedNRProcessor regWarpInput]
+ -[LearnedNRProcessor resetInternalState]
+ -[LearnedNRProcessor resetState]
+ -[LearnedNRProcessor runDemosaicWithInputRawTex:outputImage:frame:]
+ -[LearnedNRProcessor runDemosaicWithInputRawTex:outputImage:frame:].cold.1
+ -[LearnedNRProcessor runPipeline]
+ -[LearnedNRProcessor runPipeline].cold.1
+ -[LearnedNRProcessor runPipeline].cold.2
+ -[LearnedNRProcessor runPipeline].cold.3
+ -[LearnedNRProcessor runPipeline].cold.4
+ -[LearnedNRProcessor runPipeline].cold.5
+ -[LearnedNRProcessor runPipeline].cold.6
+ -[LearnedNRProcessor runPipeline].cold.7
+ -[LearnedNRProcessor runSemanticInferences]
+ -[LearnedNRProcessor runSemanticInferences].cold.1
+ -[LearnedNRProcessor runSemanticInferences].cold.2
+ -[LearnedNRProcessor runSemanticInferences].cold.3
+ -[LearnedNRProcessor semanticStyleProperties]
+ -[LearnedNRProcessor setAllocatorBackend:]
+ -[LearnedNRProcessor setCameraInfoByPortType:]
+ -[LearnedNRProcessor setDefringingTuningByPortType:]
+ -[LearnedNRProcessor setDelegate:]
+ -[LearnedNRProcessor setDoRedFaceFix:]
+ -[LearnedNRProcessor setEnableGreenGhostMitigation:]
+ -[LearnedNRProcessor setLinearOutputMetadata:]
+ -[LearnedNRProcessor setLinearOutputMetadata:].cold.1
+ -[LearnedNRProcessor setLinearOutputMetadata:].cold.2
+ -[LearnedNRProcessor setMaximumNumberOfReferenceFrameCandidatesToHoldForProcessing:]
+ -[LearnedNRProcessor setMetalCommandQueue:]
+ -[LearnedNRProcessor setOutput:]
+ -[LearnedNRProcessor setProcessingType:]
+ -[LearnedNRProcessor setReferenceFrameCandidatesCount:]
+ -[LearnedNRProcessor setReferenceFrameHasEVMinus:]
+ -[LearnedNRProcessor setReferenceFrameIndex:]
+ -[LearnedNRProcessor setRegWarpInput:]
+ -[LearnedNRProcessor setSemanticStyleProperties:]
+ -[LearnedNRProcessor setSharedRegWarpBuffer:]
+ -[LearnedNRProcessor setSkipDenoising:]
+ -[LearnedNRProcessor setSrlEnabled:]
+ -[LearnedNRProcessor setStfAllowed:]
+ -[LearnedNRProcessor setTuningParameters:]
+ -[LearnedNRProcessor setTuningParams:]
+ -[LearnedNRProcessor setTuningParamsPlist:]
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:]
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.1
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.10
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.11
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.2
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.3
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.4
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.5
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.6
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.7
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.8
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.9
+ -[LearnedNRProcessor setup]
+ -[LearnedNRProcessor sharedRegWarpBuffer]
+ -[LearnedNRProcessor skipDenoising]
+ -[LearnedNRProcessor srlEnabled]
+ -[LearnedNRProcessor stfAllowed]
+ -[LearnedNRProcessor supportsInputPixelFormat:]
+ -[LearnedNRProcessor supportsInputPixelFormat:].cold.1
+ -[LearnedNRProcessor supportsInputPixelFormat:].cold.2
+ -[LearnedNRProcessor tuningParameters]
+ -[LearnedNRProcessor tuningParamsPlist]
+ -[LearnedNRProcessor tuningParams]
+ -[LearnedNRProcessor(Tuning) prepareTuning:]
+ -[LearnedNRProcessor(Tuning) prepareTuning:].cold.1
+ -[LearnedNRProcessor(Tuning) prepareTuning:].cold.2
+ -[LearnedNRProcessor(Tuning) prepareTuning:].cold.3
+ -[LocalToneMappingStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[LocalToneMappingStage createIntermediateMetalTexture:pixelFormat:width:height:].cold.2
+ -[LocalToneMappingStage runWithArgs:].cold.10
+ -[LocalToneMappingStage runWithArgs:].cold.11
+ -[LocalToneMappingStage runWithArgs:].cold.12
+ -[LocalToneMappingStage runWithArgs:].cold.13
+ -[LocalToneMappingStage runWithArgs:].cold.6
+ -[LocalToneMappingStage runWithArgs:].cold.7
+ -[LocalToneMappingStage runWithArgs:].cold.8
+ -[LocalToneMappingStage runWithArgs:].cold.9
+ -[LocalToneMappingStage validateInputFrame:config:].cold.2
+ -[MIWB _configForMiwbV2:miwbInputHasCCMApplied:]
+ -[MIWB _configForMiwbV2:miwbInputHasCCMApplied:].cold.1
+ -[NRFBackgroundLearnedNR initWithContext:cameraInfo:config:]
+ -[NRFBackgroundLearnedNR initWithContext:cameraInfo:config:].cold.1
+ -[NRFConcurrentProcessing waitForBackgroundTaskToComplete:].cold.1
+ -[NRFConcurrentProcessing waitForBackgroundTaskToComplete:].cold.2
+ -[NRFFrameMetadata HDRltmCurvesForBackground]
+ -[NRFFrameMetadata init].cold.7
+ -[NRFFrameMetadata metadataHasHDRLtmCurvesForBackground]
+ -[NRFFrameMetadata setMetadataHasHDRLtmCurvesForBackground:]
+ -[NRFProcessorV4 externalMemoryDescriptorForConfiguration:].cold.1
+ -[NRFProcessorV4 externalMemoryDescriptorForConfiguration:].cold.2
+ -[NRFProcessorV4 externalMemoryDescriptorForConfiguration:].cold.3
+ -[NRFProcessorV4 prepareToProcess:prepareDescriptor:].cold.1
+ -[NRFProcessorV4 prepareToProcess:prepareDescriptor:].cold.2
+ -[NRFProcessorV4 prepareToProcess:prepareDescriptor:].cold.3
+ -[NRFProcessorV4 prepareToProcess:prepareDescriptor:].cold.4
+ -[NRFProcessorV4 prepareToProcess:prepareDescriptor:].cold.5
+ -[NRFProcessorV4 prepareToProcess:prepareDescriptor:].cold.6
+ -[NRFProcessorV4 prepareToProcess:prepareDescriptor:].cold.7
+ -[NRFRawNightModeOutputFrame addCompletionHandlerToCommandBuffer:].cold.1
+ -[NRFRawNightModeOutputFrame bindTexturesForConfig:metalContext:].cold.21
+ -[PyramidStage runWithFilters:pyramid:].cold.2
+ -[QuadraBinStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[QuadraBinStage auxiliaryPixelFormatForAuxiliaryType:inputPixelFormat:outputCompressionLevel:].cold.1
+ -[QuadraBinStage auxiliaryPixelFormatsForInputPixelFormat:outputCompressionLevel:]
+ -[RawDFCommon _createLowerBandTextureFromTexture:requestedBand:].cold.1
+ -[RawDFCommon _createLowerBandTextureFromTexture:requestedBand:].cold.2
+ -[RawDFDetectors .cxx_destruct]
+ -[RawDFDetectors flickerDetection]
+ -[RawDFDetectors getDetectorsResultsSync:]
+ -[RawDFDetectors getDetectorsResultsSync:].cold.1
+ -[RawDFDetectors getDetectorsResultsSync:].cold.2
+ -[RawDFDetectors getDetectorsResultsSync:].cold.3
+ -[RawDFDetectors getMotionDetectionSyncResult:]
+ -[RawDFDetectors getMotionDetectionSyncResult:].cold.1
+ -[RawDFDetectors getMotionDetectionSyncResult:].cold.2
+ -[RawDFDetectors grayGhostDetection]
+ -[RawDFDetectors initWithMetalContext:]
+ -[RawDFDetectors initWithMetalContext:].cold.1
+ -[RawDFDetectors motionDetection]
+ -[RawDFDetectors rawDFColorMatchStage]
+ -[RawDFDetectors rawDFDownsampleStage]
+ -[RawDFDetectors reset]
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:]
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.1
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.10
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.11
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.12
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.13
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.14
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.15
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.16
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.17
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.18
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.19
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.2
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.20
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.21
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.3
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.4
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.5
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.6
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.7
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.8
+ -[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:].cold.9
+ -[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:]
+ -[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:].cold.1
+ -[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:].cold.2
+ -[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:].cold.3
+ -[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:].cold.4
+ -[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:].cold.5
+ -[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:].cold.6
+ -[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:].cold.7
+ -[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:].cold.8
+ -[RawDFDetectors setFlickerDetection:]
+ -[RawDFDetectors setGrayGhostDetection:]
+ -[RawDFDetectors setMotionDetection:]
+ -[RawDFDetectors setRawDFColorMatchStage:]
+ -[RawDFDetectors setRawDFDownsampleStage:]
+ -[RawDFDetectors setTuning:]
+ -[RawDFDetectors tuning]
+ -[RawDFProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.7
+ -[RawDFProcessor _generateSyntheticRefererence:outputNoiseDivisor:withDetectorsOutput:].cold.1
+ -[RawDFProcessor _generateSyntheticRefererence:outputNoiseDivisor:withDetectorsOutput:].cold.2
+ -[RawDFProcessor _generateSyntheticRefererence:outputNoiseDivisor:withDetectorsOutput:].cold.3
+ -[RawDFProcessor _generateSyntheticRefererence:outputNoiseDivisor:withDetectorsOutput:].cold.4
+ -[RawDFProcessor _generateSyntheticRefererence:outputNoiseDivisor:withDetectorsOutput:].cold.5
+ -[RawDFProcessor _generateSyntheticRefererence:outputNoiseDivisor:withDetectorsOutput:].cold.6
+ -[RawDFProcessor _generateSyntheticRefererence:outputNoiseDivisor:withDetectorsOutput:].cold.7
+ -[RawDFProcessor _preprocessFrame:].cold.1
+ -[RawDFProcessor _preprocessFrame:].cold.2
+ -[RawDFProcessor addInputResource:].cold.10
+ -[RawDFProcessor regWarpInput]
+ -[RawDFProcessor setRegWarpInput:]
+ -[RawDFProcessor setRegWarpInput:].cold.1
+ -[RawDFProcessor(Tuning) prepareTuning:processingTypes:]
+ -[RawDFProcessor(Tuning) prepareTuning:processingTypes:].cold.1
+ -[RawDFProcessor(Tuning) prepareTuning:processingTypes:].cold.2
+ -[RawDFProcessor(Tuning) prepareTuning:processingTypes:].cold.3
+ -[RawDFProcessor(Tuning) prepareTuning:processingTypes:].cold.4
+ -[RawDFProcessor(Tuning) prepareTuning:processingTypes:].cold.5
+ -[RawDFProxyShaders initWithMetal:].cold.1
+ -[RawDFSynRefDSR .cxx_destruct]
+ -[RawDFSynRefDSR fusionWeights]
+ -[RawDFSynRefDSR initWithShaders:name:group:evmPyramid:ev0Pyramid:lscGainsTex:]
+ -[RawDFSynRefDSR initWithShaders:name:group:evmPyramid:ev0Pyramid:lscGainsTex:].cold.1
+ -[RawDFSynRefDSR output]
+ -[RawDFSynRefDSR prepareWithFrameProperties:srPlist:]
+ -[RawDFSynRefDSR prepareWithFrameProperties:srPlist:].cold.1
+ -[RawDFSynRefDSR prepareWithFrameProperties:srPlist:].cold.2
+ -[RawDFSynRefDSRPass .cxx_destruct]
+ -[RawDFSynRefDSRPass dsrUp]
+ -[RawDFSynRefDSRPass ev0Up]
+ -[RawDFSynRefDSRPass ev0]
+ -[RawDFSynRefDSRPass evmUp]
+ -[RawDFSynRefDSRPass evm]
+ -[RawDFSynRefDSRPass fusionWeights]
+ -[RawDFSynRefDSRPass getThreadsToDispatch:]
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:]
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.1
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.10
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.2
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.3
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.4
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.5
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.6
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.7
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.8
+ -[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:].cold.9
+ -[RawDFSynRefDSRPass output]
+ -[RawDFSynRefDSRPass prepareWithFrameProperties:srPlist:]
+ -[RawDFSynRefDSRPass prepareWithFrameProperties:srPlist:].cold.1
+ -[RawDFSynRefDSRPass render:]
+ -[RawDFSynRefDSRPass render:].cold.1
+ -[RawDFSynRefHR .cxx_destruct]
+ -[RawDFSynRefHR ev0]
+ -[RawDFSynRefHR evm]
+ -[RawDFSynRefHR fusionWeights]
+ -[RawDFSynRefHR initWithShaders:name:group:]
+ -[RawDFSynRefHR initWithShaders:name:group:].cold.1
+ -[RawDFSynRefHR initWithShaders:name:group:].cold.2
+ -[RawDFSynRefHR initWithShaders:name:group:].cold.3
+ -[RawDFSynRefHR initWithShaders:name:group:].cold.4
+ -[RawDFSynRefHR initWithShaders:name:group:].cold.5
+ -[RawDFSynRefHR initWithShaders:name:group:].cold.6
+ -[RawDFSynRefHR output]
+ -[RawDFSynRefHR prepareWithFrameProperties:srPlist:]
+ -[RawDFSynRefHR render:]
+ -[RawDFSynRefHR render:].cold.1
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.1
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.10
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.11
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.12
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.13
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.14
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.15
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.16
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.17
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.18
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.2
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.3
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.4
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.5
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.6
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.7
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.8
+ -[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:].cold.9
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.1
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.10
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.11
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.12
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.13
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.14
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.2
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.3
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.4
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.5
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.6
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.7
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.8
+ -[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:].cold.9
+ -[RawDFSyntheticReferenceShaders initWithMetal:].cold.2
+ -[RawDFSyntheticReferenceShadersCRG .cxx_destruct]
+ -[RawDFSyntheticReferenceShadersCRG getKernel:]
+ -[RawDFSyntheticReferenceShadersCRG getKernel:configFlags:]
+ -[RawDFSyntheticReferenceShadersCRG initWithMetal:]
+ -[RawDFSyntheticReferenceShadersCRG initWithMetal:].cold.1
+ -[RawDFSyntheticReferenceShadersCRG initWithMetal:].cold.2
+ -[RawDFSyntheticReferenceStage fillFrameProperties:withEvmProperties:withEv0Properties:]
+ -[RawDFSyntheticReferenceStage fillFrameProperties:withEvmProperties:withEv0Properties:].cold.1
+ -[RawDFSyntheticReferenceStage fillFrameProperties:withEvmProperties:withEv0Properties:].cold.2
+ -[RawDFSyntheticReferenceStage fillFrameProperties:withEvmProperties:withEv0Properties:].cold.3
+ -[RawDFSyntheticReferenceStageCRG .cxx_destruct]
+ -[RawDFSyntheticReferenceStageCRG fillFrameProperties:withEvmProperties:withEv0Properties:]
+ -[RawDFSyntheticReferenceStageCRG fillFrameProperties:withEvmProperties:withEv0Properties:].cold.1
+ -[RawDFSyntheticReferenceStageCRG fillFrameProperties:withEvmProperties:withEv0Properties:].cold.2
+ -[RawDFSyntheticReferenceStageCRG fillFrameProperties:withEvmProperties:withEv0Properties:].cold.3
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:]
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.1
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.10
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.11
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.12
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.13
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.14
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.15
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.16
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.17
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.18
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.19
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.2
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.3
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.4
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.5
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.6
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.7
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.8
+ -[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:].cold.9
+ -[RawDFSyntheticReferenceStageCRG initWithMetalContext:]
+ -[RawDFSyntheticReferenceStageCRG initWithMetalContext:].cold.1
+ -[RawDFSyntheticReferenceStageCRG initWithMetalContext:].cold.2
+ -[RawDFSyntheticReferenceStageCRG initWithMetalContext:].cold.3
+ -[RawDFSyntheticReferenceUnpackShaders initWithMetal:].cold.1
+ -[RawDFZoomStage processFrame:inputTex:inputOrigin:outputTex:outputOrigin:doZoom:].cold.1
+ -[RawDFZoomStage processFrame:inputTex:inputOrigin:outputTex:outputOrigin:doZoom:].cold.2
+ -[RawDFZoomStage processFrame:inputTex:inputOrigin:outputTex:outputOrigin:doZoom:].cold.3
+ -[RawDFZoomStage processFrame:inputTex:inputOrigin:outputTex:outputOrigin:doZoom:].cold.4
+ -[RawDFZoomStage processFrame:inputTex:inputOrigin:outputTex:outputOrigin:doZoom:].cold.5
+ -[RawDFZoomStage processFrame:inputTex:inputOrigin:outputTex:outputOrigin:doZoom:].cold.6
+ -[RawNightModeConfig validateInputFrame:].cold.1
+ -[RawNightModeConfig validateInputFrame:].cold.2
+ -[RawNightModeConfig validateInputFrame:].cold.3
+ -[RawNightModeConfig validateInputFrame:].cold.4
+ -[RawNightModeConfig validateOutputFrame:].cold.1
+ -[RawNightModeConfig validateOutputFrame:].cold.2
+ -[RawNightModeConfig validateOutputFrame:].cold.3
+ -[RawNightModeConfig validateOutputFrame:].cold.4
+ -[RawNightModeConfig validateOutputFrame:].cold.5
+ -[RawNightModeConfig validateOutputFrame:].cold.6
+ -[RawNightModeConfig validateOutputFrame:].cold.7
+ -[RawNightModeDenoiseMetalStage getHighlightSmoothingParametersFrom:fromGain:highlightSmoothingParameters:].cold.7
+ -[RawNightModeDenoiseMetalStage getHighlightSmoothingParametersFrom:fromGain:highlightSmoothingParameters:].cold.8
+ -[RawNightModeDenoiseMetalStage getHighlightSmoothingParametersFrom:fromGain:highlightSmoothingParameters:].cold.9
+ -[RawNightModeInputFrame calculateNormalisedFaceScore].cold.5
+ -[RawNightModeInputFrame initWithSampleBuffer:cameraInfoByPortType:].cold.1
+ -[RawNightModeInputFrame initWithSampleBuffer:cameraInfoByPortType:].cold.2
+ -[RawNightModeInputFrame initWithSampleBuffer:cameraInfoByPortType:].cold.3
+ -[RawNightModeInputFrame initWithSampleBuffer:cameraInfoByPortType:].cold.4
+ -[RawNightModeMultiFrameOutlierPixelCorrection createShaderWithOptions:error:]
+ -[RawNightModeProcessor addFrame:].cold.18
+ -[RawNightModeProcessor regWarpInput]
+ -[RawNightModeProcessor runAWBOnOutputFrame:].cold.9
+ -[RawNightModeProcessor setRegWarpInput:]
+ -[RawNightModeTiledInferenceProvider allocateMemory].cold.10
+ -[RawNightModeTiledInferenceProvider allocateMemory].cold.11
+ -[RawNightModeTiledInferenceProvider allocateMemory].cold.12
+ -[RawNightModeTiledInferenceProvider allocateMemory].cold.13
+ -[RawNightModeTiledInferenceProvider allocateMemory].cold.14
+ -[RawNightModeTiledInferenceProvider allocateMemory].cold.15
+ -[RawNightModeTiledInferenceProvider allocateMemory].cold.7
+ -[RawNightModeTiledInferenceProvider allocateMemory].cold.8
+ -[RawNightModeTiledInferenceProvider allocateMemory].cold.9
+ -[RawNightModeTiledInferenceProvider runInference].cold.10
+ -[RawNightModeTiledInferenceProvider runInference].cold.9
+ -[RawNightModeTiledInferenceProvider setup].cold.11
+ -[RawProcFrames .cxx_destruct]
+ -[RawProcFrames _verifyConsistentMetadataWithFrame:]
+ -[RawProcFrames addFrame:]
+ -[RawProcFrames addFrame:].cold.1
+ -[RawProcFrames addFrame:].cold.2
+ -[RawProcFrames dealloc]
+ -[RawProcFrames doRegistration]
+ -[RawProcFrames finalizeFrames]
+ -[RawProcFrames frames]
+ -[RawProcFrames initWithMetalContext:]
+ -[RawProcFrames initWithMetalContext:].cold.1
+ -[RawProcFrames initWithMetalContext:].cold.2
+ -[RawProcFrames initWithMetalContext:].cold.3
+ -[RawProcFrames init]
+ -[RawProcFrames longFrame]
+ -[RawProcFrames ltcFrame]
+ -[RawProcFrames purgeResources]
+ -[RawProcFrames referenceFrameIndex]
+ -[RawProcFrames referenceFrame]
+ -[RawProcFrames regWarpInput]
+ -[RawProcFrames registerImages:]
+ -[RawProcFrames registerImages:].cold.1
+ -[RawProcFrames registerImages:].cold.2
+ -[RawProcFrames registerImages:].cold.3
+ -[RawProcFrames registerImages:].cold.4
+ -[RawProcFrames registerImages:].cold.5
+ -[RawProcFrames registrationPipelineRWPP]
+ -[RawProcFrames releaseFrames]
+ -[RawProcFrames releaseRgbTextures]
+ -[RawProcFrames setDoRegistration:]
+ -[RawProcFrames setReferenceFrameIndex:]
+ -[RawProcFrames setReferenceFrameIndex:].cold.1
+ -[RawProcFrames setReferenceFrameIndex:].cold.2
+ -[RawProcFrames setRegWarpInput:]
+ -[RawProcFrames setRegWarpInput:].cold.1
+ -[RawProcFrames setRegWarpInput:].cold.2
+ -[RawProcFrames setRegistrationPipelineRWPP:]
+ -[RawProcFrames sifrFrame]
+ -[RawProcInputFrame .cxx_destruct]
+ -[RawProcInputFrame _checkRgbTexConfig:]
+ -[RawProcInputFrame _checkRgbTexConfig:].cold.1
+ -[RawProcInputFrame _checkRgbTexConfig:].cold.2
+ -[RawProcInputFrame _checkRgbTexConfig:].cold.3
+ -[RawProcInputFrame _checkRgbTexConfig:].cold.4
+ -[RawProcInputFrame allocateAndDemosaic:]
+ -[RawProcInputFrame allocateAndDemosaic:].cold.1
+ -[RawProcInputFrame allocateAndDemosaic:].cold.2
+ -[RawProcInputFrame allocateRGB]
+ -[RawProcInputFrame allocateRGB].cold.1
+ -[RawProcInputFrame auxDraftDemosaicLumaTexture]
+ -[RawProcInputFrame auxDraftDemosaicPixelBuffer]
+ -[RawProcInputFrame auxDraftDemosaicRGBTexture]
+ -[RawProcInputFrame baseTex]
+ -[RawProcInputFrame bayerPattern]
+ -[RawProcInputFrame bindingMetalFormat]
+ -[RawProcInputFrame cameraInfo]
+ -[RawProcInputFrame checkAndSetRgbTex:]
+ -[RawProcInputFrame checkAndSetRgbTex:].cold.1
+ -[RawProcInputFrame commonInitWithMetalContext:cameraInfo:inputFrame:metadata:uniqueFrameId:]
+ -[RawProcInputFrame commonInitWithMetalContext:cameraInfo:inputFrame:metadata:uniqueFrameId:].cold.1
+ -[RawProcInputFrame commonInitWithMetalContext:cameraInfo:inputPixelBuffer:metadata:uniqueFrameId:]
+ -[RawProcInputFrame commonInitWithMetalContext:cameraInfo:inputPixelBuffer:metadata:uniqueFrameId:].cold.1
+ -[RawProcInputFrame commonInitWithMetalContext:cameraInfo:inputSamplebuffer:uniqueFrameId:]
+ -[RawProcInputFrame commonInit]
+ -[RawProcInputFrame dealloc]
+ -[RawProcInputFrame demosaicWithStage:]
+ -[RawProcInputFrame demosaicWithStage:].cold.1
+ -[RawProcInputFrame demosaicWithStage:].cold.2
+ -[RawProcInputFrame demosaicWithStage:].cold.3
+ -[RawProcInputFrame demosaicWithStage:].cold.4
+ -[RawProcInputFrame gdcParameters]
+ -[RawProcInputFrame getDescForRGB]
+ -[RawProcInputFrame getGDCParametersWithCameraInfoByPortType]
+ -[RawProcInputFrame getGDCParametersWithCameraInfoByPortType].cold.1
+ -[RawProcInputFrame heightAlignment]
+ -[RawProcInputFrame height]
+ -[RawProcInputFrame initFrameProperties]
+ -[RawProcInputFrame initFrameProperties].cold.1
+ -[RawProcInputFrame initFrameProperties].cold.2
+ -[RawProcInputFrame initFrameProperties].cold.3
+ -[RawProcInputFrame initWithMetalContext:cameraInfo:inputFrame:metadata:uniqueFrameId:]
+ -[RawProcInputFrame initWithMetalContext:cameraInfo:inputPixelBuffer:metadata:uniqueFrameId:]
+ -[RawProcInputFrame initWithMetalContext:cameraInfo:inputSampleBuffer:uniqueFrameId:]
+ -[RawProcInputFrame init]
+ -[RawProcInputFrame lscGainMapBuffer]
+ -[RawProcInputFrame lscGainMapParameters]
+ -[RawProcInputFrame metadata]
+ -[RawProcInputFrame pixelBufferFormat]
+ -[RawProcInputFrame pixelBuffer]
+ -[RawProcInputFrame properties]
+ -[RawProcInputFrame pyramid]
+ -[RawProcInputFrame releaseBaseTex]
+ -[RawProcInputFrame releaseRgbTex]
+ -[RawProcInputFrame rgbTex]
+ -[RawProcInputFrame sensorHeight]
+ -[RawProcInputFrame sensorWidth]
+ -[RawProcInputFrame setBindingMetalFormat:]
+ -[RawProcInputFrame setHeightAlignment:]
+ -[RawProcInputFrame setProperties:]
+ -[RawProcInputFrame setStrideAlignment:]
+ -[RawProcInputFrame strideAlignment]
+ -[RawProcInputFrame uniqueFrameId]
+ -[RawProcInputFrame width]
+ -[RegDense prepareWithImageWidth:imageHeight:allocateTextures:]
+ -[RegDense prepareWithImageWidth:imageHeight:allocateTextures:].cold.1
+ -[RegDense prepareWithImageWidth:imageHeight:allocateTextures:].cold.2
+ -[RegDense prepareWithImageWidth:imageHeight:allocateTextures:].cold.3
+ -[RegDense prepareWithImageWidth:imageHeight:allocateTextures:].cold.4
+ -[RegDense prepareWithImageWidth:imageHeight:allocateTextures:].cold.5
+ -[RegDense prepareWithImageWidth:imageHeight:allocateTextures:].cold.6
+ -[RegDenseShaders initWithMetal:].cold.10
+ -[RegDenseShaders initWithMetal:].cold.11
+ -[RegDenseShaders initWithMetal:].cold.6
+ -[RegDenseShaders initWithMetal:].cold.7
+ -[RegDenseShaders initWithMetal:].cold.8
+ -[RegDenseShaders initWithMetal:].cold.9
+ -[RegPyrFusion prepareWithImageWidth:imageHeight:]
+ -[RegPyrFusion prepareWithImageWidth:imageHeight:].cold.1
+ -[RegPyrFusion registerImagesWithReference:nonRef:refTexlvl1:nonRefTexlvl1:shiftMap:confidenceMap:].cold.22
+ -[RegPyrFusionShaders createPipelineStateWithMetal:vShaderName:fShaderName:outputColorMetalFormat:]
+ -[RegPyrFusionShaders createPipelineStateWithMetal:vShaderName:fShaderName:outputColorMetalFormat:constantValues:]
+ -[RegWarpStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[SoftISPConfig validateOutputFrame:].cold.1
+ -[SoftISPConfig validateOutputFrame:].cold.2
+ -[SoftISPInputFrame hasRegroupedLayout]
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.1
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.10
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.11
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.12
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.13
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.14
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.15
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.16
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.17
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.18
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.19
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.2
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.20
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.21
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.22
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.23
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.24
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.25
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.26
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.27
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.28
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.29
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.3
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.30
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.31
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.32
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.4
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.5
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.6
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.7
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.8
+ -[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:].cold.9
+ -[SoftISPKernelWithFunctionConstants _loadWithMetalContext:kernelName:functionConstantNamespace:paramCombinations:].cold.10
+ -[SoftISPKernelWithFunctionConstants _loadWithMetalContext:kernelName:functionConstantNamespace:paramCombinations:].cold.11
+ -[SoftISPKernelWithFunctionConstants _loadWithMetalContext:kernelName:functionConstantNamespace:paramCombinations:].cold.9
+ -[SoftISPKernelWithFunctionConstants _loadWithMetalContext:kernelName:functionConstantNamespace:paramValues:].cold.9
+ -[SoftISPOutputFrame addCompletionHandlerToCommandBuffer:].cold.1
+ -[SoftISPOutputFrame allocateTexturesForConfig:metalContext:].cold.5
+ -[SoftISPPipeline auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[SoftISPPipeline auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:].cold.1
+ -[SoftISPPipeline auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:].cold.2
+ -[SoftISPPipeline auxiliaryPixelFormatForAuxiliaryType:inputPixelFormat:outputCompressionLevel:].cold.3
+ -[SoftISPPipeline initWithGraph:metal:staticParameters:].cold.7
+ -[SoftISPPipeline outputPixelFormatForInputPixelFormat:outputCompressionLevel:].cold.2
+ -[SoftISPPipeline outputPixelFormatForInputPixelFormat:outputCompressionLevel:].cold.3
+ -[SoftISPPipeline runWithArgs:].cold.10
+ -[SoftISPProcessor addFrame:uniqueID:processingOptions:].cold.6
+ -[SoftISPProcessor auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:alignmentOut:]
+ -[SoftISPProcessor auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:alignmentOut:].cold.1
+ -[SoftISPProcessor auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:alignmentOut:].cold.2
+ -[SoftISPProcessor auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:alignmentOut:].cold.3
+ -[SoftISPProcessor processIfPossible].cold.1
+ -[SoftISPProcessor process].cold.1
+ -[SoftLTM calculateLTMOnDraftDemosaicEV0Frame:evmFrame:]
+ -[SoftLTM calculateLTMOnDraftDemosaicEV0Frame:evmFrame:].cold.1
+ -[SoftLTM calculateLTMOnDraftDemosaicEV0Frame:evmFrame:].cold.2
+ -[SoftLTM calculateLTMOnDraftDemosaicEV0Frame:evmFrame:].cold.3
+ -[SoftLTM calculateLTMOnDraftDemosaicEV0Frame:evmFrame:].cold.4
+ -[SoftLTM computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:]
+ -[SoftLTM computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:].cold.1
+ -[SoftLTM computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:].cold.2
+ -[SoftLTM initWithMetalContext:]
+ -[SoftLTM initWithMetalContext:].cold.1
+ -[SoftLTM initWithMetalContext:].cold.2
+ -[SoftLTM initWithMetalContext:].cold.3
+ -[SoftLTM isLTMOnFinalEnabled:]
+ -[SoftLTM processLTMMetadata:toDarkestFrameMetadata:toEV0FrameMetadata:]
+ -[SoftLTM processLTMMetadata:toDarkestFrameMetadata:toEV0FrameMetadata:].cold.1
+ -[ToneMappingCurves initWithWithContext:].cold.14
+ -[ToneMappingStage getSrlBoostedLTMasNSData:]
+ -[ToneMappingStage getSrlBoostedLTMasNSData:].cold.1
+ -[ToneMappingStage getSrlBoostedLTMasNSData:].cold.2
+ -[ToneMappingStage isHighResLTMGrid:]
+ -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:]
+ -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:].cold.1
+ -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:].cold.2
+ -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:].cold.3
+ -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:].cold.4
+ -[UBProcessorV4 _multiFrameProcessing].cold.1
+ -[UBProcessorV4 _process].cold.1
+ -[UBProcessorV4 _process].cold.2
+ -[UBProcessorV4 _process].cold.3
+ -[UBProcessorV4 _process].cold.4
+ -[UBProcessorV4 _process].cold.5
+ -[UBProcessorV4 _registerImages:].cold.1
+ -[UBProcessorV4 _registerImages:].cold.10
+ -[UBProcessorV4 _registerImages:].cold.11
+ -[UBProcessorV4 _registerImages:].cold.12
+ -[UBProcessorV4 _registerImages:].cold.2
+ -[UBProcessorV4 _registerImages:].cold.3
+ -[UBProcessorV4 _registerImages:].cold.4
+ -[UBProcessorV4 _registerImages:].cold.5
+ -[UBProcessorV4 _registerImages:].cold.6
+ -[UBProcessorV4 _registerImages:].cold.7
+ -[UBProcessorV4 _registerImages:].cold.8
+ -[UBProcessorV4 _registerImages:].cold.9
+ -[UBProcessorV4 getTuningFrom:forCaptureType:]
+ -[UBProcessorV4 regWarpInput]
+ -[UBProcessorV4 setRegWarpInput:]
+ GCC_except_table19
+ GCC_except_table2
+ GCC_except_table20
+ _CFAutorelease
+ _CMIDimensionsFromTexture
+ _CMIGetMetalPixelFormatForPixelBuffer
+ _CMILSCOISAdaptation_convertV1CICTableToV1CICTableWithOISOffset
+ _CMIPixelFormatIsVersatileRaw
+ _CMIStringFromCGRect
+ _CMIStringFromDimensions
+ _CMIStringFromTexture
+ _CRGRegisterTextureStruct
+ _DeepFusionBufferTypeToString
+ _FigCaptureNormalizedFocusWindowFromMetadata
+ _FigCapturePixelFormatEquivalentRegroupedLayoutPixelFormat
+ _FigCapturePixelFormatHasRegroupedLayout
+ _FigCapturePixelFormatIs420
+ _FigCapturePixelFormatIs422
+ _FigCapturePixelFormatIsTenBit
+ _FigCapturePixelFormatIsYCbCr
+ _FigCaptureSetNormalizedFocusWindowToMetadata
+ _FigCaptureTransformRectToCoordinateSpaceOfRect
+ _FigGetCFPreferenceDoubleWithDefault
+ _FigSignalErrorAt3
+ _NRFRegisterTextureStructs
+ _OBJC_CLASS_$_CMIInferenceResourceDescriptor
+ _OBJC_CLASS_$_CMITileEngine
+ _OBJC_CLASS_$_CMITiledInferenceProcessorStage
+ _OBJC_CLASS_$_CMInferenceUtils
+ _OBJC_CLASS_$_CRGDerivedDimensions
+ _OBJC_CLASS_$_CRGExplicitPixelFormat
+ _OBJC_CLASS_$_CRGExternalInput
+ _OBJC_CLASS_$_CRGExternalOutput
+ _OBJC_CLASS_$_CRGGraph
+ _OBJC_CLASS_$_CRGGroup
+ _OBJC_CLASS_$_CRGInputDescriptor
+ _OBJC_CLASS_$_CRGNode
+ _OBJC_CLASS_$_CRGOutputConstraints
+ _OBJC_CLASS_$_CRGOutputDescriptor
+ _OBJC_CLASS_$_CRGPlanConstraints
+ _OBJC_CLASS_$_CRGStaticSupportROI
+ _OBJC_CLASS_$_CRGTextureDescriptor
+ _OBJC_CLASS_$_FigCaptureCameraParameters
+ _OBJC_CLASS_$_LearnedNRBoundInferenceResults
+ _OBJC_CLASS_$_LearnedNRNetworkConfig
+ _OBJC_CLASS_$_LearnedNRProcessor
+ _OBJC_CLASS_$_MTLRenderPipelineColorAttachmentDescriptor
+ _OBJC_CLASS_$_RawDFSynRefDSR
+ _OBJC_CLASS_$_RawDFSynRefDSRPass
+ _OBJC_CLASS_$_RawDFSynRefHR
+ _OBJC_CLASS_$_RawDFSyntheticReferenceShadersCRG
+ _OBJC_CLASS_$_RawDFSyntheticReferenceStageCRG
+ _OBJC_CLASS_$_RawProcFrames
+ _OBJC_CLASS_$_RawProcInputFrame
+ _OBJC_IVAR_$_CMIDraftDemosaicStage._draftDemosaicToRGBMultiChannelBayerPipeline
+ _OBJC_IVAR_$_CMIDraftDemosaicStage._draftDemosaicToRGBMultiChannelQuadra2xPipeline
+ _OBJC_IVAR_$_CMIDraftDemosaicStage._draftDemosaicToRGBMultiChannelQuadra4xPipeline
+ _OBJC_IVAR_$_CMIDraftDemosaicStage._draftDemosaicToRGBSingleChannelBayerPipeline
+ _OBJC_IVAR_$_CMIDraftDemosaicStage._draftDemosaicToRGBSingleChannelQuadra2xPipeline
+ _OBJC_IVAR_$_CMIDraftDemosaicStage._draftDemosaicToRGBSingleChannelQuadra4xPipeline
+ _OBJC_IVAR_$_CMITiledInferenceProcessorStage._completions
+ _OBJC_IVAR_$_CMITiledInferenceProcessorStage._errorCount
+ _OBJC_IVAR_$_CMITiledInferenceProcessorStage._runs
+ _OBJC_IVAR_$_DeepFusionProcessor._rawDFDetectors
+ _OBJC_IVAR_$_DenoiseFusePipeline._HLGLumaATex
+ _OBJC_IVAR_$_GainMapShaders._MPPComponentMax
+ _OBJC_IVAR_$_GainMapShaders._MPPComputeRWTMOConstants
+ _OBJC_IVAR_$_GainMapShaders._MPPConvertHLGToSDRAndHLGLumaA420
+ _OBJC_IVAR_$_GainMapShaders._MPPConvertHLGToSDRAndHLGLumaA422
+ _OBJC_IVAR_$_GainMapShaders._MPPGainMap420LumaA
+ _OBJC_IVAR_$_GainMapShaders._MPPGainMapMax
+ _OBJC_IVAR_$_GainMapShaders._MPPHLGComputeMaxComponent
+ _OBJC_IVAR_$_GainMapShaders._MPPLog
+ _OBJC_IVAR_$_GainMapShaders._MPPSetEDRToMax
+ _OBJC_IVAR_$_GainMapStage._gainMapCommandBuffer
+ _OBJC_IVAR_$_GainMapStage._isFlexFullRange
+ _OBJC_IVAR_$_GainMapStage._isHLGStillCase
+ _OBJC_IVAR_$_GainMapStage._useHardGainAverageLTM
+ _OBJC_IVAR_$_H13FastRawScaleShaders._focusPixelDeltaBlurMap
+ _OBJC_IVAR_$_H13FastRawScaleShaders._focusPixelDeltaMap
+ _OBJC_IVAR_$_H13FastRawScaleShaders._focusPixelExtraction
+ _OBJC_IVAR_$_H13FastRawScaleShaders._focusPixelExtractionQuadra
+ _OBJC_IVAR_$_H13FastRawScaleShaders._hazeCorrection
+ _OBJC_IVAR_$_H13FastRawScaleShaders._hazeCorrectionQuadra
+ _OBJC_IVAR_$_H13FastRawScaleShaders._hazeDetection
+ _OBJC_IVAR_$_H13FastRawScaleShaders._hazeDomination
+ _OBJC_IVAR_$_H13FastRawScaleShaders._maxScaling
+ _OBJC_IVAR_$_H13FastRawScaleShaders._rgbThumbnail
+ _OBJC_IVAR_$_H13FastRawScaleShaders._rgbThumbnailQuadra
+ _OBJC_IVAR_$_H13FastRawScaleShaders._sumTexture
+ _OBJC_IVAR_$_LearnedNRBoundInferenceResults._instanceMasks
+ _OBJC_IVAR_$_LearnedNRBoundInferenceResults._personMask
+ _OBJC_IVAR_$_LearnedNRBoundInferenceResults._skinMask
+ _OBJC_IVAR_$_LearnedNRBoundInferenceResults._skyMask
+ _OBJC_IVAR_$_LearnedNRNetworkConfig._deviceGeneration
+ _OBJC_IVAR_$_LearnedNRNetworkConfig._isQuadra
+ _OBJC_IVAR_$_LearnedNRNetworkShared._networkModel
+ _OBJC_IVAR_$_LearnedNRNetworkShared._tileOverlap
+ _OBJC_IVAR_$_LearnedNRNetworkStage._stageConfig
+ _OBJC_IVAR_$_LearnedNRNetworkTuningParams.lumaAddBackLSCModulationTuning
+ _OBJC_IVAR_$_LearnedNRNetworkTuningParams.networkModel
+ _OBJC_IVAR_$_LearnedNRNetworkTuningParams.tileOverlapParameters
+ _OBJC_IVAR_$_LearnedNRProcessor._addFrameCount
+ _OBJC_IVAR_$_LearnedNRProcessor._allocatorBackend
+ _OBJC_IVAR_$_LearnedNRProcessor._allocatorSetupComplete
+ _OBJC_IVAR_$_LearnedNRProcessor._batchCount
+ _OBJC_IVAR_$_LearnedNRProcessor._cameraInfoByPortType
+ _OBJC_IVAR_$_LearnedNRProcessor._cntBracketSampleBuffers
+ _OBJC_IVAR_$_LearnedNRProcessor._colorConvertStage
+ _OBJC_IVAR_$_LearnedNRProcessor._compressionLevel
+ _OBJC_IVAR_$_LearnedNRProcessor._defringingTuningByPortType
+ _OBJC_IVAR_$_LearnedNRProcessor._delegate
+ _OBJC_IVAR_$_LearnedNRProcessor._demosaicStage
+ _OBJC_IVAR_$_LearnedNRProcessor._doRedFaceFix
+ _OBJC_IVAR_$_LearnedNRProcessor._enableGreenGhostMitigation
+ _OBJC_IVAR_$_LearnedNRProcessor._fusionMode
+ _OBJC_IVAR_$_LearnedNRProcessor._gainMapStage
+ _OBJC_IVAR_$_LearnedNRProcessor._inferenceSourceImg
+ _OBJC_IVAR_$_LearnedNRProcessor._inputFrames
+ _OBJC_IVAR_$_LearnedNRProcessor._isShaderHarvesting
+ _OBJC_IVAR_$_LearnedNRProcessor._lastHeight
+ _OBJC_IVAR_$_LearnedNRProcessor._lastPixelFormat
+ _OBJC_IVAR_$_LearnedNRProcessor._lastWidth
+ _OBJC_IVAR_$_LearnedNRProcessor._learnedNRNetworkStage
+ _OBJC_IVAR_$_LearnedNRProcessor._maximumNumberOfReferenceFrameCandidatesToHoldForProcessing
+ _OBJC_IVAR_$_LearnedNRProcessor._metal
+ _OBJC_IVAR_$_LearnedNRProcessor._metalCommandQueue
+ _OBJC_IVAR_$_LearnedNRProcessor._nRegisteredFrames
+ _OBJC_IVAR_$_LearnedNRProcessor._nrfConfig
+ _OBJC_IVAR_$_LearnedNRProcessor._nrfPlist
+ _OBJC_IVAR_$_LearnedNRProcessor._output
+ _OBJC_IVAR_$_LearnedNRProcessor._post
+ _OBJC_IVAR_$_LearnedNRProcessor._processingType
+ _OBJC_IVAR_$_LearnedNRProcessor._processorOutput
+ _OBJC_IVAR_$_LearnedNRProcessor._processorOutputGainMapHeadroom
+ _OBJC_IVAR_$_LearnedNRProcessor._pyramidStage
+ _OBJC_IVAR_$_LearnedNRProcessor._rawDFCommon
+ _OBJC_IVAR_$_LearnedNRProcessor._rawDFInferenceGen
+ _OBJC_IVAR_$_LearnedNRProcessor._referenceFrameCandidatesCount
+ _OBJC_IVAR_$_LearnedNRProcessor._referenceFrameHasEVMinus
+ _OBJC_IVAR_$_LearnedNRProcessor._referenceFrameIndex
+ _OBJC_IVAR_$_LearnedNRProcessor._regWarpInput
+ _OBJC_IVAR_$_LearnedNRProcessor._requestTuningParams
+ _OBJC_IVAR_$_LearnedNRProcessor._semanticStyleProperties
+ _OBJC_IVAR_$_LearnedNRProcessor._sharedMetalBuffer
+ _OBJC_IVAR_$_LearnedNRProcessor._sidecar
+ _OBJC_IVAR_$_LearnedNRProcessor._skipDenoising
+ _OBJC_IVAR_$_LearnedNRProcessor._softLTMStage
+ _OBJC_IVAR_$_LearnedNRProcessor._srlEnabled
+ _OBJC_IVAR_$_LearnedNRProcessor._stfAllowed
+ _OBJC_IVAR_$_LearnedNRProcessor._tuningParameters
+ _OBJC_IVAR_$_LearnedNRProcessor._tuningParams
+ _OBJC_IVAR_$_LearnedNRProcessor._tuningParamsPlist
+ _OBJC_IVAR_$_LearnedNRProcessor._useDraftDemForInferenceAndGainMap
+ _OBJC_IVAR_$_LearnedNRProcessor._usingExternalSharedMetalBuffer
+ _OBJC_IVAR_$_LearnedNRProcessor.sharedRegWarpBuffer
+ _OBJC_IVAR_$_NRFConfig._learnedNRSubProcessorEnabled
+ _OBJC_IVAR_$_NRFFrameMetadata._HDRltmCurvesForBackground
+ _OBJC_IVAR_$_NRFFrameMetadata._metadataHasHDRLtmCurvesForBackground
+ _OBJC_IVAR_$_NRFPlist.ev0RefDenoising
+ _OBJC_IVAR_$_NRFPlist.evmRefDenoising
+ _OBJC_IVAR_$_NRFProcessorV4._deviceGeneration
+ _OBJC_IVAR_$_RawDFDetectors._colorMatchingEnabled
+ _OBJC_IVAR_$_RawDFDetectors._ev0RegHomography
+ _OBJC_IVAR_$_RawDFDetectors._evmHRGainDownRatio
+ _OBJC_IVAR_$_RawDFDetectors._evmRegHomography
+ _OBJC_IVAR_$_RawDFDetectors._flickerDetection
+ _OBJC_IVAR_$_RawDFDetectors._grayGhostDetection
+ _OBJC_IVAR_$_RawDFDetectors._greentTintCorrectionOrFlickerDetectionInputEV0
+ _OBJC_IVAR_$_RawDFDetectors._greentTintCorrectionOrFlickerDetectionInputEVM
+ _OBJC_IVAR_$_RawDFDetectors._metal
+ _OBJC_IVAR_$_RawDFDetectors._motionDetection
+ _OBJC_IVAR_$_RawDFDetectors._mustRunDetection
+ _OBJC_IVAR_$_RawDFDetectors._rawDFColorMatchStage
+ _OBJC_IVAR_$_RawDFDetectors._rawDFDownsampleStage
+ _OBJC_IVAR_$_RawDFDetectors._requestedSyntheticReferenceMode
+ _OBJC_IVAR_$_RawDFDetectors._runMotionDetector
+ _OBJC_IVAR_$_RawDFDetectors._scaleEv0Brightness
+ _OBJC_IVAR_$_RawDFDetectors._scaleEvmBrightness
+ _OBJC_IVAR_$_RawDFDetectors._tuning
+ _OBJC_IVAR_$_RawDFDetectors._useMotionDetector
+ _OBJC_IVAR_$_RawDFProcessor._rawDFDetectors
+ _OBJC_IVAR_$_RawDFProcessor._srlEnabled
+ _OBJC_IVAR_$_RawDFSynRefDSR._fusionWeights
+ _OBJC_IVAR_$_RawDFSynRefDSR._output
+ _OBJC_IVAR_$_RawDFSynRefDSR._passes
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._band
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._bandConsts
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._dsrUp
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._ev0
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._ev0Up
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._evm
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._evmUp
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._frameProperies
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._fusionWeights
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._lscGainsTex
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._output
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._shaders
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._sizeGranularity
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._textureArgsFinal
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._textureArgsMain
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._textureArgsUp
+ _OBJC_IVAR_$_RawDFSynRefDSRPass._topBand
+ _OBJC_IVAR_$_RawDFSynRefHR._bandConsts
+ _OBJC_IVAR_$_RawDFSynRefHR._ev0
+ _OBJC_IVAR_$_RawDFSynRefHR._evm
+ _OBJC_IVAR_$_RawDFSynRefHR._frameProperties
+ _OBJC_IVAR_$_RawDFSynRefHR._fusionWeights
+ _OBJC_IVAR_$_RawDFSynRefHR._output
+ _OBJC_IVAR_$_RawDFSynRefHR._shaders
+ _OBJC_IVAR_$_RawDFSynRefHR._sizeGranularity
+ _OBJC_IVAR_$_RawDFSynRefHR._textureArgs
+ _OBJC_IVAR_$_RawDFSyntheticReferenceShadersCRG._kernel
+ _OBJC_IVAR_$_RawDFSyntheticReferenceShadersCRG._kernelWithFunctionConstant
+ _OBJC_IVAR_$_RawDFSyntheticReferenceStageCRG._metal
+ _OBJC_IVAR_$_RawDFSyntheticReferenceStageCRG._shaders
+ _OBJC_IVAR_$_RawNightModeProcessor._deviceGeneration
+ _OBJC_IVAR_$_RawNightModeProcessor._regWarpInput
+ _OBJC_IVAR_$_RawProcFrames._doRegistration
+ _OBJC_IVAR_$_RawProcFrames._draftDemosaicStage
+ _OBJC_IVAR_$_RawProcFrames._frames
+ _OBJC_IVAR_$_RawProcFrames._longFrameIndex
+ _OBJC_IVAR_$_RawProcFrames._metal
+ _OBJC_IVAR_$_RawProcFrames._nRegisteredFrames
+ _OBJC_IVAR_$_RawProcFrames._referenceFrameIndex
+ _OBJC_IVAR_$_RawProcFrames._referenceFrameUniqueId
+ _OBJC_IVAR_$_RawProcFrames._regWarpInput
+ _OBJC_IVAR_$_RawProcFrames._regWarpInputTex
+ _OBJC_IVAR_$_RawProcFrames._registrationPipelineRWPP
+ _OBJC_IVAR_$_RawProcFrames._sifrFrameIndex
+ _OBJC_IVAR_$_RawProcInputFrame._auxDraftDemosaicLumaTexture
+ _OBJC_IVAR_$_RawProcInputFrame._auxDraftDemosaicPixelBuffer
+ _OBJC_IVAR_$_RawProcInputFrame._auxDraftDemosaicRGBTexture
+ _OBJC_IVAR_$_RawProcInputFrame._baseTex
+ _OBJC_IVAR_$_RawProcInputFrame._bayerPattern
+ _OBJC_IVAR_$_RawProcInputFrame._bindingMetalFormat
+ _OBJC_IVAR_$_RawProcInputFrame._cameraInfo
+ _OBJC_IVAR_$_RawProcInputFrame._gdcParameters
+ _OBJC_IVAR_$_RawProcInputFrame._height
+ _OBJC_IVAR_$_RawProcInputFrame._heightAlignment
+ _OBJC_IVAR_$_RawProcInputFrame._isVeratileRegroupedPixelFormat
+ _OBJC_IVAR_$_RawProcInputFrame._lscGainMapBuffer
+ _OBJC_IVAR_$_RawProcInputFrame._lscGainMapParameters
+ _OBJC_IVAR_$_RawProcInputFrame._metadata
+ _OBJC_IVAR_$_RawProcInputFrame._metal
+ _OBJC_IVAR_$_RawProcInputFrame._pixelBuffer
+ _OBJC_IVAR_$_RawProcInputFrame._pixelBufferFormat
+ _OBJC_IVAR_$_RawProcInputFrame._properties
+ _OBJC_IVAR_$_RawProcInputFrame._pyramid
+ _OBJC_IVAR_$_RawProcInputFrame._rgbTex
+ _OBJC_IVAR_$_RawProcInputFrame._sampleBuffer
+ _OBJC_IVAR_$_RawProcInputFrame._sensorHeight
+ _OBJC_IVAR_$_RawProcInputFrame._sensorWidth
+ _OBJC_IVAR_$_RawProcInputFrame._strideAlignment
+ _OBJC_IVAR_$_RawProcInputFrame._uniqueFrameId
+ _OBJC_IVAR_$_RawProcInputFrame._width
+ _OBJC_IVAR_$_SRLv2Plist.minDarken_I
+ _OBJC_IVAR_$_SRLv2Plist.minDarken_II
+ _OBJC_IVAR_$_SRLv2Plist.minDarken_III
+ _OBJC_IVAR_$_SRLv2Plist.minDarken_IV
+ _OBJC_IVAR_$_SRLv2Plist.minDarken_V
+ _OBJC_IVAR_$_SRLv2Plist.minDarken_VI
+ _OBJC_IVAR_$_SoftISPInputFrame._hasRegroupedLayout
+ _OBJC_IVAR_$_SoftISPInputFrame._pixelFormat
+ _OBJC_IVAR_$_SoftLTM._metal
+ _OBJC_IVAR_$_ToneMappingShaders._ltmApplyShaders
+ _OBJC_METACLASS_$_CMITiledInferenceProcessorStage
+ _OBJC_METACLASS_$_CRGNode
+ _OBJC_METACLASS_$_LearnedNRBoundInferenceResults
+ _OBJC_METACLASS_$_LearnedNRNetworkConfig
+ _OBJC_METACLASS_$_LearnedNRProcessor
+ _OBJC_METACLASS_$_RawDFSynRefDSR
+ _OBJC_METACLASS_$_RawDFSynRefDSRPass
+ _OBJC_METACLASS_$_RawDFSynRefHR
+ _OBJC_METACLASS_$_RawDFSyntheticReferenceShadersCRG
+ _OBJC_METACLASS_$_RawDFSyntheticReferenceStageCRG
+ _OBJC_METACLASS_$_RawProcFrames
+ _OBJC_METACLASS_$_RawProcInputFrame
+ _SoftISPRectEqualToRect
+ __OBJC_$_CLASS_METHODS_RawDFLanczos
+ __OBJC_$_CLASS_METHODS_RawDFSyntheticReferenceShadersCRG
+ __OBJC_$_CLASS_METHODS_RawDFSyntheticReferenceStageCRG
+ __OBJC_$_CLASS_METHODS_RawProcInputFrame
+ __OBJC_$_INSTANCE_METHODS_CMITiledInferenceProcessorStage
+ __OBJC_$_INSTANCE_METHODS_H13FastRawScaleConfig(PDC|SyntheticThumbnail|RFPN|BlackLevelEstimation|DMA|PDP|HOCL|ABLEST|HazeCorrection|GOC|ShadingFPNR|BlackLevelShading)
+ __OBJC_$_INSTANCE_METHODS_H13FastRawScaleStage(SyntheticThumbnail|HazeCorrection|FPExtract|Vision|ABLEST|PDC)
+ __OBJC_$_INSTANCE_METHODS_LearnedNRBoundInferenceResults
+ __OBJC_$_INSTANCE_METHODS_LearnedNRNetworkConfig
+ __OBJC_$_INSTANCE_METHODS_LearnedNRProcessor(Tuning)
+ __OBJC_$_INSTANCE_METHODS_RawDFDetectors
+ __OBJC_$_INSTANCE_METHODS_RawDFSynRefDSR
+ __OBJC_$_INSTANCE_METHODS_RawDFSynRefDSRPass
+ __OBJC_$_INSTANCE_METHODS_RawDFSynRefHR
+ __OBJC_$_INSTANCE_METHODS_RawDFSyntheticReferenceShadersCRG
+ __OBJC_$_INSTANCE_METHODS_RawDFSyntheticReferenceStageCRG
+ __OBJC_$_INSTANCE_METHODS_RawProcFrames
+ __OBJC_$_INSTANCE_METHODS_RawProcInputFrame
+ __OBJC_$_INSTANCE_VARIABLES_CMITiledInferenceProcessorStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedNRBoundInferenceResults
+ __OBJC_$_INSTANCE_VARIABLES_LearnedNRNetworkConfig
+ __OBJC_$_INSTANCE_VARIABLES_LearnedNRProcessor
+ __OBJC_$_INSTANCE_VARIABLES_RawDFDetectors
+ __OBJC_$_INSTANCE_VARIABLES_RawDFSynRefDSR
+ __OBJC_$_INSTANCE_VARIABLES_RawDFSynRefDSRPass
+ __OBJC_$_INSTANCE_VARIABLES_RawDFSynRefHR
+ __OBJC_$_INSTANCE_VARIABLES_RawDFSyntheticReferenceShadersCRG
+ __OBJC_$_INSTANCE_VARIABLES_RawDFSyntheticReferenceStageCRG
+ __OBJC_$_INSTANCE_VARIABLES_RawProcFrames
+ __OBJC_$_INSTANCE_VARIABLES_RawProcInputFrame
+ __OBJC_$_PROP_LIST_LearnedNRBoundInferenceResults
+ __OBJC_$_PROP_LIST_LearnedNRNetworkConfig
+ __OBJC_$_PROP_LIST_LearnedNRProcessor
+ __OBJC_$_PROP_LIST_RawDFDetectors
+ __OBJC_$_PROP_LIST_RawDFSynRefDSR
+ __OBJC_$_PROP_LIST_RawDFSynRefDSRPass
+ __OBJC_$_PROP_LIST_RawDFSynRefHR
+ __OBJC_$_PROP_LIST_RawDFSyntheticReferenceStage
+ __OBJC_$_PROP_LIST_RawDFSyntheticReferenceStageCRG
+ __OBJC_$_PROP_LIST_RawProcFrames
+ __OBJC_$_PROP_LIST_RawProcInputFrame
+ __OBJC_$_PROTOCOL_CLASS_METHODS_RawDFSyntheticReferenceStage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRGRenderProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CRGRenderProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_RawDFSyntheticReferenceStage
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRGRenderProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_RawDFSyntheticReferenceStage
+ __OBJC_$_PROTOCOL_REFS_CRGRenderProvider
+ __OBJC_$_PROTOCOL_REFS_RawDFSyntheticReferenceStage
+ __OBJC_CLASS_PROTOCOLS_$_LearnedNRProcessor
+ __OBJC_CLASS_PROTOCOLS_$_RawDFSynRefDSRPass
+ __OBJC_CLASS_PROTOCOLS_$_RawDFSynRefHR
+ __OBJC_CLASS_PROTOCOLS_$_RawDFSyntheticReferenceStage
+ __OBJC_CLASS_PROTOCOLS_$_RawDFSyntheticReferenceStageCRG
+ __OBJC_CLASS_RO_$_CMITiledInferenceProcessorStage
+ __OBJC_CLASS_RO_$_LearnedNRBoundInferenceResults
+ __OBJC_CLASS_RO_$_LearnedNRNetworkConfig
+ __OBJC_CLASS_RO_$_LearnedNRProcessor
+ __OBJC_CLASS_RO_$_RawDFSynRefDSR
+ __OBJC_CLASS_RO_$_RawDFSynRefDSRPass
+ __OBJC_CLASS_RO_$_RawDFSynRefHR
+ __OBJC_CLASS_RO_$_RawDFSyntheticReferenceShadersCRG
+ __OBJC_CLASS_RO_$_RawDFSyntheticReferenceStageCRG
+ __OBJC_CLASS_RO_$_RawProcFrames
+ __OBJC_CLASS_RO_$_RawProcInputFrame
+ __OBJC_LABEL_PROTOCOL_$_CRGRenderProvider
+ __OBJC_LABEL_PROTOCOL_$_RawDFSyntheticReferenceStage
+ __OBJC_METACLASS_RO_$_CMITiledInferenceProcessorStage
+ __OBJC_METACLASS_RO_$_LearnedNRBoundInferenceResults
+ __OBJC_METACLASS_RO_$_LearnedNRNetworkConfig
+ __OBJC_METACLASS_RO_$_LearnedNRProcessor
+ __OBJC_METACLASS_RO_$_RawDFSynRefDSR
+ __OBJC_METACLASS_RO_$_RawDFSynRefDSRPass
+ __OBJC_METACLASS_RO_$_RawDFSynRefHR
+ __OBJC_METACLASS_RO_$_RawDFSyntheticReferenceShadersCRG
+ __OBJC_METACLASS_RO_$_RawDFSyntheticReferenceStageCRG
+ __OBJC_METACLASS_RO_$_RawProcFrames
+ __OBJC_METACLASS_RO_$_RawProcInputFrame
+ __OBJC_PROTOCOL_$_CRGRenderProvider
+ __OBJC_PROTOCOL_$_RawDFSyntheticReferenceStage
+ __ZN3CRG20getStructInfoForTypeI28RawDFDeepShadowRecoveryUpTexEEP7NSArrayIP20CRGTextureDescriptorEv
+ __ZN3CRG20getStructInfoForTypeI30RawDFDeepShadowRecoveryMainTexEEP7NSArrayIP20CRGTextureDescriptorEv
+ __ZN3CRG20getStructInfoForTypeI30RawDFHighlightRecoveryTexturesEEP7NSArrayIP20CRGTextureDescriptorEv
+ __ZN3CRG20getStructInfoForTypeI31RawDFDeepShadowRecoveryFinalTexEEP7NSArrayIP20CRGTextureDescriptorEv
+ __ZTAXtlN3CRG13StringLiteralILm14EEEtlA14_cLc102ELc117ELc115ELc105ELc111ELc110ELc87ELc101ELc105ELc103ELc104ELc116ELc115EEEE
+ __ZTAXtlN3CRG13StringLiteralILm4EEEtlA4_cLc101ELc118ELc109EEEE
+ __ZTAXtlN3CRG13StringLiteralILm4EEEtlA4_cLc101ELc118ELc48EEEE
+ __ZTAXtlN3CRG13StringLiteralILm6EEEtlA6_cLc100ELc115ELc114ELc85ELc112EEEE
+ __ZTAXtlN3CRG13StringLiteralILm6EEEtlA6_cLc101ELc118ELc109ELc85ELc112EEEE
+ __ZTAXtlN3CRG13StringLiteralILm6EEEtlA6_cLc101ELc118ELc48ELc85ELc112EEEE
+ __ZTAXtlN3CRG13StringLiteralILm7EEEtlA7_cLc111ELc117ELc116ELc112ELc117ELc116EEEE
+ ___105-[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:]_block_invoke
+ ___105-[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:]_block_invoke_2
+ ___115-[CMIRawNightModeRegistrationStage processConstrainedNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.363
+ ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.270
+ ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke_2.288
+ ___121-[RawDFSyntheticReferenceStage _doHighlightRecovery:noiseDivisorOutputTex:evmPyramid:ev0Pyramid:frameProperties:srPlist:]_block_invoke.33
+ ___125-[RawDFProxyStage generateOutputNoiseMapLuma:outputNoiseMapChroma:lscGainsTex:ev0:evm:noiseDivisorOutputTex:frameProperties:]_block_invoke.26
+ ___134-[RawDFSyntheticReferenceStage _doDeepShadowRecovery:noiseDivisorOutputTex:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:srPlist:]_block_invoke.37
+ ___137-[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:]_block_invoke.37
+ ___150-[RegDense runWithReferenceTex:nonReferenceTex:warpedTex:relativeBrightness:homography:regDenseParams:alwaysDense:refWeightsLevel:nonRefWeightsLevel:]_block_invoke.166
+ ___189-[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:]_block_invoke
+ ___189-[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:]_block_invoke_2
+ ___216-[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:]_block_invoke.39
+ ___284-[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:]_block_invoke
+ ___284-[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:]_block_invoke_2
+ ___31-[UBProcessorV4 _nrfFuseImages]_block_invoke.276
+ ___58-[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy]_block_invoke.273
+ ___62-[CMITiledInferenceProcessorStage runProcessor:withTileCount:]_block_invoke
+ ___79-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:]_block_invoke.275
+ ___79-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:]_block_invoke_2
+ ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke.41
+ ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke.44
+ ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke_2.46
+ ___98-[DefringeStage defringePyramid:outputPyramid:chromaScratch:quadraBinningFactor:tuningParameters:]_block_invoke.64
+ ___block_descriptor_220_e16_192s200s208s_e19_"NSDictionary"8?0ls192l8s200l8s208l8
+ ___block_literal_global.106
+ ___block_literal_global.108
+ ___block_literal_global.118
+ ___block_literal_global.121
+ ___block_literal_global.122
+ ___block_literal_global.125
+ ___block_literal_global.127
+ ___block_literal_global.131
+ ___block_literal_global.150
+ ___block_literal_global.152
+ ___block_literal_global.155
+ ___block_literal_global.157
+ ___block_literal_global.165
+ ___block_literal_global.175
+ ___block_literal_global.177
+ ___block_literal_global.183
+ ___block_literal_global.214
+ ___block_literal_global.216
+ ___block_literal_global.235
+ ___block_literal_global.236
+ ___block_literal_global.238
+ ___block_literal_global.247
+ ___block_literal_global.252
+ ___block_literal_global.254
+ ___block_literal_global.258
+ ___block_literal_global.260
+ ___block_literal_global.266
+ ___block_literal_global.272
+ ___block_literal_global.292
+ ___block_literal_global.293
+ ___block_literal_global.336
+ ___block_literal_global.36
+ ___getCameraCaptureLegacyLog_block_invoke
+ ___gxx_personality_v0
+ __os_log_impl
+ _calculate3DThreadgroupSize
+ _calculate3DThreadgroupSize.cold.1
+ _colorspace_updateFwdCsc
+ _compareHRConfig.cold.10
+ _compareHRConfig.cold.11
+ _compareHRConfig.cold.2
+ _compareHRConfig.cold.3
+ _compareHRConfig.cold.4
+ _compareHRConfig.cold.5
+ _compareHRConfig.cold.6
+ _compareHRConfig.cold.7
+ _compareHRConfig.cold.8
+ _compareHRConfig.cold.9
+ _createScaledRectDict
+ _createScaledRectDict.cold.1
+ _gLearnedNRMetalStageTrace
+ _gNightModeDenoiseMetalStageTrace
+ _gNightModeFusionMetalStageTrace
+ _gNightModeTripodFusionMetalStageTrace
+ _gNightModeTripodPreFusionTrace
+ _getCameraCaptureLegacyLog.cameraCaptureLegacyLog
+ _getCameraCaptureLegacyLog.cameraCaptureLegacyLogOnceToken
+ _getFloatValue
+ _getHDRLTMCurvesForBackgroundFromMetadata
+ _getIntParameter
+ _getLTM_lutsCountX
+ _getLTM_lutsCountY
+ _getMaxLSCGainFromLSCGridData
+ _getMaxLSCGainFromLSCGridData.cold.1
+ _getMaxLSCGainFromLSCGridData.cold.2
+ _getMaxLSCGainFromLSCGridData.cold.3
+ _isCompatibleProcessingTypeSensorPortAndRawDFTuningType
+ _kCVImageBufferColorPrimariesKey
+ _kCVImageBufferColorPrimaries_P3_D65
+ _kCVImageBufferTransferFunction_ITU_R_2100_HLG
+ _kFigCaptureCameraInfoKey_AbsoluteColorCalibrations
+ _kFigCaptureCameraInfoKey_HybridOCLRedBlueCrosstalkGrid
+ _kFigCaptureSampleBufferMetadata_GlobalLTMLookUpTable_HLGWithoutFaceBoost
+ _kFigCaptureSampleBufferMetadata_GlobalToneCurveLookUpTable_HLGWithoutFaceBoost
+ _kFigCaptureSampleBufferMetadata_LTMLookUpTables_HLGWithoutFaceBoost
+ _kFigCaptureSampleBufferMetadata_PurpleHazeDetection
+ _kFigCaptureSampleBufferMetadata_PurpleHazeDetectionKey_PurpleHazeDetected
+ _kFigCaptureSampleBufferMetadata_PurpleHazeDetectionKey_PurpleHazePixelCount
+ _kFigCaptureSampleBufferMetadata_PurpleHazeDetectionKey_PurpleHazePurpleness
+ _kFigCaptureSampleBufferMetadata_PurpleHazeDetectionKey_PurpleHazeStrength
+ _kFigCaptureStreamAbsoluteColorCalibrationCCTKey_BGGain
+ _kFigCaptureStreamAbsoluteColorCalibrationCCTKey_RGGain
+ _kFigCaptureStreamAbsoluteColorCalibrationKey_HighCCT
+ _kFigCaptureStreamMetadata_ColorCorrectionMatrixDesaturationStrength
+ _kFigCaptureStreamMetadata_FocusRegion
+ _kFigCaptureStreamMetadata_NominalColorCorrectionMatrix
+ _kFigCaptureStreamMetadata_PurpleHazeMitigationEnabled
+ _kLensShadingCorrectionGainMapParametersKey_CropOriginX
+ _kLensShadingCorrectionGainMapParametersKey_CropOriginY
+ _kLensShadingCorrectionGainMapParametersKey_GridIntervalReciprocalX
+ _kLensShadingCorrectionGainMapParametersKey_GridIntervalReciprocalY
+ _kLensShadingCorrectionGainMapParametersKey_SensorDimensionHeight
+ _kLensShadingCorrectionGainMapParametersKey_SensorDimensionWidth
+ _kNRF_Default
+ _kNRF_SkipHardGainLumaHD
+ _kNRF_UseFlexFullRange
+ _kNRF_UseHardGainAverageLTM
+ _kNRF_UseIspDGainSoftLog
+ _kNRF_UseLuxLevelMetadata
+ _mtlutl_getEquivalentRegroupedLayoutMetalPixelFormat
+ _objc_msgSend$HDRltmCurvesForBackground
+ _objc_msgSend$_getTotalGainFromMetadata:
+ _objc_msgSend$_processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:
+ _objc_msgSend$auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:
+ _objc_msgSend$calculateLTMOnDraftDemosaicEV0Frame:evmFrame:
+ _objc_msgSend$commonInit
+ _objc_msgSend$compile
+ _objc_msgSend$compileShader:lumaWrite:chromaWrite:error:
+ _objc_msgSend$computeAverageCurve:withLTM:ltmGridX:ltmGridY:andGTC:andLtmHardGain:
+ _objc_msgSend$computeGainMapWithInput:secondInput:HLGLumaAInput:output:properties:mpconfig:
+ _objc_msgSend$computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:
+ _objc_msgSend$computePipelineStateFor:constants:fault:
+ _objc_msgSend$convertHLGToSDRWithInputPixelBuffer:outputImage:
+ _objc_msgSend$convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:
+ _objc_msgSend$copyTotalSensorCropRectFrom:to:
+ _objc_msgSend$createPipelineStateWithMetal:vShaderName:fShaderName:outputColorMetalFormat:
+ _objc_msgSend$createPipelineStateWithMetal:vShaderName:fShaderName:outputColorMetalFormat:constantValues:
+ _objc_msgSend$createShaderWithOptions:error:
+ _objc_msgSend$daylightScore
+ _objc_msgSend$deviceGeneration
+ _objc_msgSend$dispatchInfo
+ _objc_msgSend$dispatchThreads
+ _objc_msgSend$doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:
+ _objc_msgSend$dsrUp
+ _objc_msgSend$ev0
+ _objc_msgSend$ev0Up
+ _objc_msgSend$evm
+ _objc_msgSend$evmUp
+ _objc_msgSend$finalizeFrames
+ _objc_msgSend$flexRangeMetadataDictionary:mppHeadroom:newHeadroom:fullRange:
+ _objc_msgSend$focusPixelDeltaBlurMap
+ _objc_msgSend$focusPixelDeltaMap
+ _objc_msgSend$focusPixelExtraction
+ _objc_msgSend$focusPixelExtractionQuadra
+ _objc_msgSend$fromPort:
+ _objc_msgSend$fromPort:withScale:
+ _objc_msgSend$fusionWeights
+ _objc_msgSend$generateGainMapIfNeeded
+ _objc_msgSend$getDescForRGB
+ _objc_msgSend$getDetectorsResultsSync:
+ _objc_msgSend$getGDCParametersWithCameraInfoByPortType
+ _objc_msgSend$getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:
+ _objc_msgSend$getHazeCorrectionEnabledForInputFrame:enabled:
+ _objc_msgSend$getMotionDetectionSyncResult:
+ _objc_msgSend$getNetworkPath:isE5:
+ _objc_msgSend$getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:outRegDenseMapProperties:
+ _objc_msgSend$getSrlBoostedLTMasNSData:
+ _objc_msgSend$getThreadsToDispatch:
+ _objc_msgSend$getTileOverlapForGain:table:
+ _objc_msgSend$getTuningFrom:forCaptureType:
+ _objc_msgSend$hazeCorrection
+ _objc_msgSend$hazeCorrectionQuadra
+ _objc_msgSend$hazeDetection
+ _objc_msgSend$hazeDomination
+ _objc_msgSend$heapBufferSizeAndAlignWithLength:options:
+ _objc_msgSend$heapTextureSizeAndAlignWithDescriptor:
+ _objc_msgSend$initWithContext:cameraInfo:config:
+ _objc_msgSend$initWithGroup:
+ _objc_msgSend$initWithMetal:vertName:fragName:pixelFormat:pixelFormat2:
+ _objc_msgSend$initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:
+ _objc_msgSend$initWithName:group:
+ _objc_msgSend$initWithShaders:lscGainsTex:name:group:band:topBand:
+ _objc_msgSend$initWithShaders:name:group:
+ _objc_msgSend$initWithShaders:name:group:evmPyramid:ev0Pyramid:lscGainsTex:
+ _objc_msgSend$inputNCHWR16FloatTextureDescriptorWithName:
+ _objc_msgSend$inputName:roi:
+ _objc_msgSend$inputWithDescriptor:
+ _objc_msgSend$isHighResLTMGrid:
+ _objc_msgSend$isLTMOnFinalEnabled:
+ _objc_msgSend$isSSCAccountedForInBytesRequiredForConfig:
+ _objc_msgSend$largestOccupiedOffset
+ _objc_msgSend$localizedDescription
+ _objc_msgSend$localizedFailureReason
+ _objc_msgSend$ltcFrame
+ _objc_msgSend$maxScaling
+ _objc_msgSend$metadataHasHDRLtmCurvesForBackground
+ _objc_msgSend$mtlPixelFormat:
+ _objc_msgSend$networkModel
+ _objc_msgSend$newOutputAuxiliaryPixelBufferForUniqueID:pixelFormat:width:height:alignment:
+ _objc_msgSend$normalizeLTMTable:ltmGridX:ltmGridY:ltmBinsNumber:
+ _objc_msgSend$originAlignment:
+ _objc_msgSend$outputNCHWR16FloatTextureDescriptorWithName:
+ _objc_msgSend$outputName:dimensions:pixelFormat:
+ _objc_msgSend$outputName:dimensions:pixelFormat:constraints:
+ _objc_msgSend$outputSize
+ _objc_msgSend$outputWithDescriptor:
+ _objc_msgSend$performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:
+ _objc_msgSend$planSolutionWithConstraints:graph:error:
+ _objc_msgSend$prepareBand1InputWithBand0:
+ _objc_msgSend$prepareTuning:processingTypes:
+ _objc_msgSend$prepareWithFrameProperties:srPlist:
+ _objc_msgSend$prepareWithImageWidth:imageHeight:allocateTextures:
+ _objc_msgSend$processLTMMetadata:toDarkestFrameMetadata:toEV0FrameMetadata:
+ _objc_msgSend$registerImages:
+ _objc_msgSend$releaseFrames
+ _objc_msgSend$renderAll
+ _objc_msgSend$renderPipelineStateForVertexFunction:vertexDescriptor:fragmentFunction:constants:colorAttachmentDescriptorArrray:
+ _objc_msgSend$rgbThumbnail
+ _objc_msgSend$rgbThumbnailQuadra
+ _objc_msgSend$runDemosaicWithInputRawTex:outputImage:frame:
+ _objc_msgSend$runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:
+ _objc_msgSend$runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:
+ _objc_msgSend$runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:
+ _objc_msgSend$runPipeline
+ _objc_msgSend$runSemanticInferences
+ _objc_msgSend$runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:
+ _objc_msgSend$setApplicator:
+ _objc_msgSend$setDeviceGeneration:
+ _objc_msgSend$setDispatchInfoBuffer:atIndex:
+ _objc_msgSend$setDoRegistration:
+ _objc_msgSend$setFlickerDetection:
+ _objc_msgSend$setGainMapConfig:tuning:frameMetadata:width:height:isLinear:hasHDR:
+ _objc_msgSend$setGrayGhostDetection:
+ _objc_msgSend$setInputBufferRect:
+ _objc_msgSend$setLinearSystemBuilder:
+ _objc_msgSend$setLscModulationWeight:
+ _objc_msgSend$setMetadataHasHDRLtmCurvesForBackground:
+ _objc_msgSend$setMotionDetection:
+ _objc_msgSend$setName:
+ _objc_msgSend$setNetworkInputDescriptors:
+ _objc_msgSend$setNetworkModel:
+ _objc_msgSend$setNetworkOutputDescriptors:
+ _objc_msgSend$setPixelsPerThread:
+ _objc_msgSend$setRawDFColorMatchStage:
+ _objc_msgSend$setRawDFDownsampleStage:
+ _objc_msgSend$setRegWarpInput:
+ _objc_msgSend$setRegistrationPipelineRWPP:
+ _objc_msgSend$setSource:
+ _objc_msgSend$setTextureArgs:encoder:atBufferIndex:
+ _objc_msgSend$setTileCount:
+ _objc_msgSend$setTileOverlap:
+ _objc_msgSend$sizeGranularity:
+ _objc_msgSend$startSFDWithInputSampleBuffer:outputImage:tuning:
+ _objc_msgSend$staticThreadgroupMemoryLength
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$sumTexture
+ _objc_msgSend$symmetricBorder:
+ _objc_msgSend$textureArgsWithStructName:
+ _objc_msgSend$updateParametersFromMetadata:outputGain:bayerPattern:lscGainMapBuffer:lscGainMapParameters:
+ _objc_msgSend$waitUntilScheduled
+ _objc_msgSend$writeAlignment:
+ _os_log_create
+ _print_grid_stats.cold.1
- +[DeepFusionCommon calculateReadNoise:]
- +[DeepFusionCommon fillRawNoiseModelParameters:exposureParams:]
- +[DeepFusionCommon getLumaPedestalWithProperties:plistSource:]
- +[DeepFusionCommon intermediateVersion]
- +[DeepFusionCommon networkVersion]
- +[PyramidStageShared compileShader:lumaWrite:chromaWrite:]
- +[PyramidStageShared compileShader:lumaWrite:chromaWrite:].cold.1
- +[RawDFDetectors runDetectorsToOutput:withRequestedSyntheticReferenceMode:withEv0:withEvm:withSRTuning:withDownSampleStage:withColorMatchStage:withMotionDetection:withgrayGhostDetection:withFlickerDetection:]
- +[RawDFDetectors runMotionToOutput:withRefFrame:withOtherFrame:withPyramidBand:withTuningParams:withMotionDetection:]
- +[RawDFInputFrame getMetalFormat:]
- +[RawDFInputFrame isVersatileRegroupedRawFormat:]
- +[RawDFNetworkCommon allocateBuffersForNetwork:bindMode:bindBuffers:descriptions:textures:pixelBuffers:numBuffers:pixelFormat:metalContext:]
- +[RawDFNetworkCommon allocateBuffersForNetwork:bindMode:bindBuffers:descriptions:textures:pixelBuffers:numBuffers:pixelFormat:metalContext:].cold.1
- +[RawDFNetworkCommon allocateBuffersForNetwork:bindMode:bindBuffers:descriptions:textures:pixelBuffers:numBuffers:pixelFormat:metalContext:].cold.2
- +[RawDFNetworkCommon allocateBuffersForNetwork:bindMode:bindBuffers:descriptions:textures:pixelBuffers:numBuffers:pixelFormat:metalContext:].cold.3
- +[RawDFNetworkCommon loadEspressoNetworkFromPath:andStoreNetwork:andPlan:espressoContext:]
- +[RawDFNetworkCommon loadEspressoNetworkFromPath:andStoreNetwork:andPlan:espressoContext:].cold.1
- +[RawDFNetworkCommon loadEspressoNetworkFromPath:andStoreNetwork:andPlan:espressoContext:].cold.2
- +[RawDFNetworkCommon platformIdentifier]
- +[RawDFPowerBlurStage prewarmShaders:]
- +[RawDFSyntheticReferenceStage fillFrameProperties:withEvmProperties:withEv0Properties:]
- +[RawNightModeDemWarpStage prewarmShaders:]
- +[RawNightModeDemWarpStage prewarmShaders:].cold.1
- +[RawNightModeDemWarpStage prewarmShaders:].cold.2
- +[RawNightModeInferenceCommon getRawNightModeNetworkBasePath]
- +[RawNightModeInferenceCommon getRawNightModeNetworkPathFromBasePath:fromNetworkName:]
- +[RegDense getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:]
- -[AMBNRStage greenGhostMitigationWithExposure:faceLandMarks:ev0FrameMetadata:evmFrameMetadata:greenGhostBrightLightTuning:greenGhostIsRunning:gainMap:].cold.7
- -[AMBNRStage greenGhostMitigationWithExposure:faceLandMarks:ev0FrameMetadata:evmFrameMetadata:greenGhostBrightLightTuning:greenGhostIsRunning:gainMap:].cold.8
- -[BilateralGridShaders createBasicComputeShader:metal:]
- -[BilateralGridShaders initWithMetal:normalizeGridConfidence:].cold.20
- -[BilateralGridShaders initWithMetal:normalizeGridConfidence:].cold.21
- -[BilateralGridShaders initWithMetal:normalizeGridConfidence:].cold.22
- -[BlinkDetectionShaders initWithMetal:].cold.2
- -[CMIDraftDemosaicStage _compileShaders]
- -[CMIDraftDemosaicStage _compileShaders].cold.1
- -[CMIDraftDemosaicStage _compileShaders].cold.2
- -[CMIDraftDemosaicStage _compileShaders].cold.3
- -[CMIDraftDemosaicStage _compileShaders].cold.4
- -[CMIDraftDemosaicStage _compileShaders].cold.5
- -[CMIDraftDemosaicStage _compileShaders].cold.6
- -[CMIDraftDemosaicStage runWithInputTex:outputTex:cfaLayout:gain:inputCropOrigin:inputCropSize:outputCropOrigin:outputCropSize:lscGainsTex:params:].cold.3
- -[CMIRawNightModeRegistrationStage _compileShaders].cold.17
- -[CMIRawNightModeRegistrationStage _compileShaders].cold.18
- -[CMIRawNightModeRegistrationStage _compileShaders].cold.19
- -[CMIRawNightModeRegistrationStage _compileShaders].cold.20
- -[CMISoftwareFlashRenderingProcessorV2 prepareToProcess:].cold.6
- -[CZDemosaicShader initWithMetalContext:].cold.3
- -[DeepFusionProcessor _preprocessSyntheticReferenceFrame]
- -[DeepFusionProcessor _preprocessSyntheticReferenceFrame].cold.1
- -[DeepFusionProcessor _preprocessSyntheticReferenceFrame].cold.2
- -[DeepFusionProcessor _preprocessSyntheticReferenceFrame].cold.3
- -[DeepFusionProcessor _preprocessSyntheticReferenceFrame].cold.4
- -[DeepFusionProcessor addInputResource:type:].cold.5
- -[DeepFusionProcessor finishProcessing].cold.1
- -[DeepFusionProcessor finishProcessing].cold.2
- -[DeepFusionProcessor prepareToProcess:prepareDescriptor:].cold.16
- -[DeepFusionProcessor prepareToProcess:prepareDescriptor:].cold.17
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.1
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.10
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.11
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.12
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.13
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.2
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.3
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.4
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.5
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.6
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.7
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.8
- -[DeepFusionProcessor prewarmWithTuningParameters:].cold.9
- -[DeepFusionProcessor process].cold.19
- -[DeepFusionProcessor process].cold.20
- -[DeepFusionProcessor(Tuning) prepareTuning:].cold.7
- -[DefringeStage initWithMetalContext:].cold.2
- -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:]
- -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:].cold.1
- -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:].cold.2
- -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:].cold.3
- -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:].cold.4
- -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:].cold.5
- -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:].cold.6
- -[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:].cold.7
- -[DenoiseFusePipeline downsampleUpperBandFrame:sourceFrameIndex:].cold.4
- -[DenoiseFusePipeline initWithContext:cameraInfo:nrfConfig:dasTuningOptions:toneMappingOptions:tuningParameters:deviceGeneration:].cold.25
- -[DenoiseFusePipeline selectNRFFusionReferenceFrame:ev0FrameIndex:evmProperties:ev0Properties:nrfPlist:].cold.1
- -[DenoiseFusePipeline startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:]
- -[DenoiseFusePipeline startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:].cold.1
- -[DenoiseFusePipeline startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:].cold.2
- -[DenoiseFusePipeline startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:].cold.3
- -[DenoiseFusePipeline startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:].cold.4
- -[DenoiseFusePipeline startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:].cold.5
- -[DenoiseFusePipeline startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:].cold.6
- -[DenoiseFusePipeline startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:].cold.7
- -[DenoiseRemixFragmentShader initWithMetal:vertFunc:fragName:pixelFormat:pixelFormat2:]
- -[DenoiseRemixFragmentShader initWithMetal:vertFunc:fragName:pixelFormat:pixelFormat2:].cold.1
- -[DenoiseRemixFragmentShader initWithMetal:vertFunc:fragName:pixelFormat:pixelFormat2:].cold.2
- -[DenoiseRemixFragmentShader initWithMetal:vertFunc:fragName:pixelFormat:pixelFormat2:].cold.3
- -[DenoiseRemixFragmentShader initWithMetal:vertFunc:fragName:pixelFormat:pixelFormat2:].cold.4
- -[DenoiseRemixShaders initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:]
- -[DenoiseRemixShaders initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:].cold.1
- -[DenoiseRemixShaders initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:].cold.2
- -[DenoiseRemixShaders initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:].cold.3
- -[DenoiseRemixShaders initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:].cold.4
- -[DenoiseRemixShaders initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:].cold.5
- -[DenoiseRemixShaders initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:].cold.6
- -[DenoiseRemixShaders initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:].cold.7
- -[DisparityShaders initWithMetalContext:].cold.2
- -[DisparityShaders initWithMetalContext:].cold.3
- -[DisparityShaders initWithMetalContext:].cold.4
- -[DisparityStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[FuseRemixFragmentShader initWithMetal:fragName:pixelFormat:noisePixelFormat:isFirstBatch:isLastBatch:usePatchBasedFusion:useGpuCSC:ggmEnabled:].cold.4
- -[FuseRemixFragmentShader initWithMetal:fragName:pixelFormat:noisePixelFormat:isFirstBatch:isLastBatch:usePatchBasedFusion:useGpuCSC:ggmEnabled:].cold.5
- -[FuseRemixFragmentShader initWithMetal:fragName:pixelFormat:noisePixelFormat:isFirstBatch:isLastBatch:usePatchBasedFusion:useGpuCSC:ggmEnabled:].cold.6
- -[FusionNetworkPostANEStage initWithMetal:].cold.2
- -[GDCStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[GainMapStage allocateLTMTable:globalLTMCurve:gtcCurve:highlightCompressionCurve:hazeCorrection:texturesWithLTMCurves:HDR:].cold.10
- -[GainMapStage computeAverageCurve:withLTM:andGTC:]
- -[GainMapStage computeGainMapWithInput:secondInput:output:properties:mpconfig:]
- -[GainMapStage extractAndComputeAverageCurve:fromCurves:].cold.3
- -[GainMapStage flexRangeMetadataDictionary:mppHeadroom:newHeadroom:]
- -[GainMapStage normalizeLTMTable:]
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:]
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.1
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.10
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.11
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.12
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.13
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.14
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.15
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.16
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.17
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.18
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.2
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.3
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.4
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.5
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.6
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.7
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.8
- -[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:].cold.9
- -[GainMapStage setGainMapConfig:tuning:frameMetadata:width:height:isLinear:]
- -[GainMapStage setGainMapConfig:tuning:frameMetadata:width:height:isLinear:].cold.1
- -[GainMapStage setGainMapConfig:tuning:frameMetadata:width:height:isLinear:].cold.2
- -[GuidedFilterShaders initWithMetalContext:].cold.6
- -[H13FastAWB configForInputFrame:bounds:processingOptions:staticParameters:registers:].cold.14
- -[H13FastBayerProcConfig(HR) loadSoftClipLUTForInputFrame:hrConfig:toTexture:].cold.9
- -[H13FastBayerProcShaders initWithMetalContext:].cold.10
- -[H13FastBayerProcShaders initWithMetalContext:].cold.11
- -[H13FastBayerProcShaders initWithMetalContext:].cold.12
- -[H13FastBayerProcShaders initWithMetalContext:].cold.13
- -[H13FastBayerProcShaders initWithMetalContext:].cold.14
- -[H13FastBayerProcShaders initWithMetalContext:].cold.15
- -[H13FastBayerProcShaders initWithMetalContext:].cold.16
- -[H13FastBayerProcShaders initWithMetalContext:].cold.17
- -[H13FastBayerProcShaders initWithMetalContext:].cold.18
- -[H13FastBayerProcShaders initWithMetalContext:].cold.19
- -[H13FastBayerProcShaders initWithMetalContext:].cold.2
- -[H13FastBayerProcShaders initWithMetalContext:].cold.20
- -[H13FastBayerProcShaders initWithMetalContext:].cold.21
- -[H13FastBayerProcShaders initWithMetalContext:].cold.22
- -[H13FastBayerProcShaders initWithMetalContext:].cold.23
- -[H13FastBayerProcShaders initWithMetalContext:].cold.24
- -[H13FastBayerProcShaders initWithMetalContext:].cold.25
- -[H13FastBayerProcShaders initWithMetalContext:].cold.26
- -[H13FastBayerProcShaders initWithMetalContext:].cold.27
- -[H13FastBayerProcShaders initWithMetalContext:].cold.28
- -[H13FastBayerProcShaders initWithMetalContext:].cold.29
- -[H13FastBayerProcShaders initWithMetalContext:].cold.3
- -[H13FastBayerProcShaders initWithMetalContext:].cold.30
- -[H13FastBayerProcShaders initWithMetalContext:].cold.31
- -[H13FastBayerProcShaders initWithMetalContext:].cold.4
- -[H13FastBayerProcShaders initWithMetalContext:].cold.5
- -[H13FastBayerProcShaders initWithMetalContext:].cold.6
- -[H13FastBayerProcShaders initWithMetalContext:].cold.7
- -[H13FastBayerProcShaders initWithMetalContext:].cold.8
- -[H13FastBayerProcShaders initWithMetalContext:].cold.9
- -[H13FastBayerProcStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13FastBayerProcStage initWithMetalContext:staticParameters:].cold.9
- -[H13FastBayerProcStage(DraftDemosaic) shouldRunDraftDemosaic:].cold.1
- -[H13FastCanvasShaders initWithMetalContext:].cold.2
- -[H13FastCanvasShaders initWithMetalContext:].cold.3
- -[H13FastCanvasStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13FastDemosaicShaders initWithMetalContext:].cold.10
- -[H13FastDemosaicShaders initWithMetalContext:].cold.11
- -[H13FastDemosaicShaders initWithMetalContext:].cold.12
- -[H13FastDemosaicShaders initWithMetalContext:].cold.13
- -[H13FastDemosaicShaders initWithMetalContext:].cold.2
- -[H13FastDemosaicShaders initWithMetalContext:].cold.3
- -[H13FastDemosaicShaders initWithMetalContext:].cold.4
- -[H13FastDemosaicShaders initWithMetalContext:].cold.5
- -[H13FastDemosaicShaders initWithMetalContext:].cold.6
- -[H13FastDemosaicShaders initWithMetalContext:].cold.7
- -[H13FastDemosaicShaders initWithMetalContext:].cold.8
- -[H13FastDemosaicShaders initWithMetalContext:].cold.9
- -[H13FastDemosaicStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13FastLTMShaders initWithMetalContext:].cold.2
- -[H13FastLTMShaders initWithMetalContext:].cold.3
- -[H13FastLTMShaders initWithMetalContext:].cold.4
- -[H13FastLTMShaders initWithMetalContext:].cold.5
- -[H13FastLTMShaders initWithMetalContext:].cold.6
- -[H13FastLTMShaders initWithMetalContext:].cold.7
- -[H13FastLTMStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13FastLumaSharpeningShaders initWithMetalContext:].cold.2
- -[H13FastLumaSharpeningShaders initWithMetalContext:].cold.3
- -[H13FastLumaSharpeningStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13FastOutlierPixelCorrectionShaders initWithMetalContext:].cold.2
- -[H13FastOutlierPixelCorrectionShaders initWithMetalContext:].cold.3
- -[H13FastOutlierPixelCorrectionStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.10
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.11
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.12
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.2
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.3
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.4
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.5
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.6
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.7
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.8
- -[H13FastPostDemosaicProcShaders initWithMetalContext:].cold.9
- -[H13FastPostDemosaicProcStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13FastPowerBlurConfig _calculateReadNoise:]
- -[H13FastPowerBlurConfig getPowerBlurConfigForInputFrame:PowerBlurConfig:enablePowerBlur:]
- -[H13FastPowerBlurConfig initWithStaticParameters:prepareDescriptor:outputPixelFormat:]
- -[H13FastPowerBlurConfig initWithStaticParameters:prepareDescriptor:outputPixelFormat:].cold.1
- -[H13FastPowerBlurConfig initWithStaticParameters:prepareDescriptor:outputPixelFormat:].cold.2
- -[H13FastPowerBlurConfig initWithStaticParameters:prepareDescriptor:outputPixelFormat:].cold.3
- -[H13FastPowerBlurConfig initWithStaticParameters:prepareDescriptor:outputPixelFormat:].cold.4
- -[H13FastPowerBlurConfig initWithStaticParameters:prepareDescriptor:outputPixelFormat:].cold.5
- -[H13FastPowerBlurShaders .cxx_destruct]
- -[H13FastPowerBlurShaders applyPowerBlur]
- -[H13FastPowerBlurShaders initWithMetalContext:]
- -[H13FastPowerBlurShaders initWithMetalContext:].cold.1
- -[H13FastPowerBlurShaders initWithMetalContext:].cold.2
- -[H13FastPowerBlurShaders remosaicRGB]
- -[H13FastPowerBlurShaders remosaicYUV]
- -[H13FastPowerBlurShaders resampleHalfSizeToFullSizeRGB]
- -[H13FastPowerBlurShaders resampleHalfSizeToFullSizeYUV]
- -[H13FastPowerBlurShaders resampleRawAndCreateHighFrequencyMap]
- -[H13FastPowerBlurStage .cxx_destruct]
- -[H13FastPowerBlurStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13FastPowerBlurStage auxiliaryPixelFormatForAuxiliaryType:inputPixelFormat:outputCompressionLevel:]
- -[H13FastPowerBlurStage bytesRequiredForConfig:]
- -[H13FastPowerBlurStage configForPrepareDescriptor:outputCompressionLevel:]
- -[H13FastPowerBlurStage configForPrepareDescriptor:outputCompressionLevel:].cold.1
- -[H13FastPowerBlurStage createArgsWithConfig:bounds:inputFrame:outputFrame:]
- -[H13FastPowerBlurStage createIntermediateMetalDeviceTexture:withPixelFormat:width:height:]
- -[H13FastPowerBlurStage createIntermediateMetalDeviceTexture:withPixelFormat:width:height:].cold.1
- -[H13FastPowerBlurStage createIntermediateMetalDeviceTexture:withPixelFormat:width:height:].cold.2
- -[H13FastPowerBlurStage initWithMetalContext:staticParameters:]
- -[H13FastPowerBlurStage initWithMetalContext:staticParameters:].cold.1
- -[H13FastPowerBlurStage initWithMetalContext:staticParameters:].cold.2
- -[H13FastPowerBlurStage initWithMetalContext:staticParameters:].cold.3
- -[H13FastPowerBlurStage initWithMetalContext:staticParameters:].cold.4
- -[H13FastPowerBlurStage initWithMetalContext:staticParameters:].cold.5
- -[H13FastPowerBlurStage metal]
- -[H13FastPowerBlurStage outputDownscaleFactor]
- -[H13FastPowerBlurStage outputPixelFormatForInputPixelFormat:outputCompressionLevel:]
- -[H13FastPowerBlurStage runWithArgs:]
- -[H13FastPowerBlurStage runWithArgs:].cold.1
- -[H13FastPowerBlurStage runWithArgs:].cold.2
- -[H13FastPowerBlurStage runWithArgs:].cold.3
- -[H13FastPowerBlurStage runWithArgs:].cold.4
- -[H13FastPowerBlurStage runWithArgs:].cold.5
- -[H13FastPowerBlurStage runWithArgs:].cold.6
- -[H13FastPowerBlurStage runWithArgs:].cold.7
- -[H13FastPowerBlurStage runWithArgs:].cold.8
- -[H13FastPowerBlurStage runWithArgs:].cold.9
- -[H13FastPowerBlurStage staticParameters]
- -[H13FastPowerBlurStage validateInputFrame:config:]
- -[H13FastPowerBlurStage validateInputFrame:config:].cold.1
- -[H13FastPowerBlurStageArgs .cxx_destruct]
- -[H13FastPowerBlurStageArgs bounds]
- -[H13FastPowerBlurStageArgs config]
- -[H13FastPowerBlurStageArgs dealloc]
- -[H13FastPowerBlurStageArgs initWithConfig:bounds:inputFrame:outputFrame:]
- -[H13FastPowerBlurStageArgs initWithConfig:bounds:inputFrame:outputFrame:].cold.1
- -[H13FastPowerBlurStageArgs initWithConfig:bounds:inputFrame:outputFrame:].cold.2
- -[H13FastPowerBlurStageArgs initWithConfig:bounds:inputFrame:outputFrame:].cold.3
- -[H13FastPowerBlurStageArgs initWithConfig:bounds:inputFrame:outputFrame:].cold.4
- -[H13FastPowerBlurStageArgs initWithConfig:bounds:inputFrame:outputFrame:].cold.5
- -[H13FastPowerBlurStageArgs initWithConfig:bounds:inputFrame:outputFrame:].cold.6
- -[H13FastPowerBlurStageArgs initWithConfig:bounds:inputFrame:outputFrame:].cold.7
- -[H13FastPowerBlurStageArgs inputChromaTex]
- -[H13FastPowerBlurStageArgs inputFrame]
- -[H13FastPowerBlurStageArgs inputLumaTex]
- -[H13FastPowerBlurStageArgs outputChromaTex]
- -[H13FastPowerBlurStageArgs outputFrame]
- -[H13FastPowerBlurStageArgs outputLumaTex]
- -[H13FastPowerBlurStageArgs setBounds:]
- -[H13FastPowerBlurStageArgs setConfig:]
- -[H13FastPowerBlurStageArgs setInputChromaTex:]
- -[H13FastPowerBlurStageArgs setInputFrame:]
- -[H13FastPowerBlurStageArgs setInputLumaTex:]
- -[H13FastPowerBlurStageArgs setOutputChromaTex:]
- -[H13FastPowerBlurStageArgs setOutputFrame:]
- -[H13FastPowerBlurStageArgs setOutputLumaTex:]
- -[H13FastPowerBlurStageMetal .cxx_destruct]
- -[H13FastPowerBlurStageMetal _applyPowerBlurWithParams:halfResATex:halfResBTex:commandBuffer:]
- -[H13FastPowerBlurStageMetal _applyPowerBlurWithParams:halfResATex:halfResBTex:commandBuffer:].cold.1
- -[H13FastPowerBlurStageMetal _applyPowerBlurWithParams:halfResATex:halfResBTex:commandBuffer:].cold.2
- -[H13FastPowerBlurStageMetal _remosaicRgbWithParams:inputTex:lscGainsTex:outputTex:commandBuffer:]
- -[H13FastPowerBlurStageMetal _remosaicRgbWithParams:inputTex:lscGainsTex:outputTex:commandBuffer:].cold.1
- -[H13FastPowerBlurStageMetal _remosaicRgbWithParams:inputTex:lscGainsTex:outputTex:commandBuffer:].cold.2
- -[H13FastPowerBlurStageMetal _remosaicYuvWithParams:inputLumaTex:inputChromaTex:lscGainsTex:outputTex:commandBuffer:]
- -[H13FastPowerBlurStageMetal _remosaicYuvWithParams:inputLumaTex:inputChromaTex:lscGainsTex:outputTex:commandBuffer:].cold.1
- -[H13FastPowerBlurStageMetal _remosaicYuvWithParams:inputLumaTex:inputChromaTex:lscGainsTex:outputTex:commandBuffer:].cold.2
- -[H13FastPowerBlurStageMetal _resampleHalfSizeToFullSizeRgbWithParams:inputTex:halfResTex:outputTex:commandBuffer:]
- -[H13FastPowerBlurStageMetal _resampleHalfSizeToFullSizeRgbWithParams:inputTex:halfResTex:outputTex:commandBuffer:].cold.1
- -[H13FastPowerBlurStageMetal _resampleHalfSizeToFullSizeRgbWithParams:inputTex:halfResTex:outputTex:commandBuffer:].cold.2
- -[H13FastPowerBlurStageMetal _resampleHalfSizeToFullSizeYuvWithParams:inputLumaTex:inputChromaTex:halfResTex:outputLumaTex:outputChromaTex:commandBuffer:]
- -[H13FastPowerBlurStageMetal _resampleHalfSizeToFullSizeYuvWithParams:inputLumaTex:inputChromaTex:halfResTex:outputLumaTex:outputChromaTex:commandBuffer:].cold.1
- -[H13FastPowerBlurStageMetal _resampleHalfSizeToFullSizeYuvWithParams:inputLumaTex:inputChromaTex:halfResTex:outputLumaTex:outputChromaTex:commandBuffer:].cold.2
- -[H13FastPowerBlurStageMetal _resampleRawAndCreateHighFrequencyMapWithParams:rawTex:halfResTex:commandBuffer:]
- -[H13FastPowerBlurStageMetal _resampleRawAndCreateHighFrequencyMapWithParams:rawTex:halfResTex:commandBuffer:].cold.1
- -[H13FastPowerBlurStageMetal _resampleRawAndCreateHighFrequencyMapWithParams:rawTex:halfResTex:commandBuffer:].cold.2
- -[H13FastPowerBlurStageMetal _validateThreadsPerThreadgroup:forPipeline:]
- -[H13FastPowerBlurStageMetal initWithMetalContext:]
- -[H13FastPowerBlurStageMetal initWithMetalContext:].cold.1
- -[H13FastPowerBlurStageMetal initWithMetalContext:].cold.2
- -[H13FastPowerBlurStageMetal initWithMetalContext:].cold.3
- -[H13FastPowerBlurStageMetal metal]
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:]
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.1
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.10
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.11
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.12
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.2
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.3
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.4
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.5
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.6
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.7
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.8
- -[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:].cold.9
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:]
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.1
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.10
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.2
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.3
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.4
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.5
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.6
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.7
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.8
- -[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:].cold.9
- -[H13FastPowerBlurStageMetal setMetal:]
- -[H13FastPowerBlurStageMetal shaders]
- -[H13FastRawMBNRShaders initWithMetalContext:].cold.10
- -[H13FastRawMBNRShaders initWithMetalContext:].cold.2
- -[H13FastRawMBNRShaders initWithMetalContext:].cold.3
- -[H13FastRawMBNRShaders initWithMetalContext:].cold.4
- -[H13FastRawMBNRShaders initWithMetalContext:].cold.5
- -[H13FastRawMBNRShaders initWithMetalContext:].cold.6
- -[H13FastRawMBNRShaders initWithMetalContext:].cold.7
- -[H13FastRawMBNRShaders initWithMetalContext:].cold.8
- -[H13FastRawMBNRShaders initWithMetalContext:].cold.9
- -[H13FastRawMBNRStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13FastRawScaleConfig(PDC) configurePDCArgs:forInputFrame:forOutputFrame:bounds:metalCtx:pdpConfig:].cold.61
- -[H13FastRawScaleConfig(PDC) configurePDCArgs:forInputFrame:forOutputFrame:bounds:metalCtx:pdpConfig:].cold.62
- -[H13FastRawScaleConfig(PDC) configurePDCArgs:forInputFrame:forOutputFrame:bounds:metalCtx:pdpConfig:].cold.63
- -[H13FastRawScaleConfig(PDC) configurePDCArgs:forInputFrame:forOutputFrame:bounds:metalCtx:pdpConfig:].cold.64
- -[H13FastRawScaleConfig(PDC) configurePDCArgs:forInputFrame:forOutputFrame:bounds:metalCtx:pdpConfig:].cold.65
- -[H13FastRawScaleShaders initWithMetalContext:].cold.10
- -[H13FastRawScaleShaders initWithMetalContext:].cold.11
- -[H13FastRawScaleShaders initWithMetalContext:].cold.12
- -[H13FastRawScaleShaders initWithMetalContext:].cold.13
- -[H13FastRawScaleShaders initWithMetalContext:].cold.14
- -[H13FastRawScaleShaders initWithMetalContext:].cold.15
- -[H13FastRawScaleShaders initWithMetalContext:].cold.16
- -[H13FastRawScaleShaders initWithMetalContext:].cold.17
- -[H13FastRawScaleShaders initWithMetalContext:].cold.18
- -[H13FastRawScaleShaders initWithMetalContext:].cold.19
- -[H13FastRawScaleShaders initWithMetalContext:].cold.2
- -[H13FastRawScaleShaders initWithMetalContext:].cold.20
- -[H13FastRawScaleShaders initWithMetalContext:].cold.21
- -[H13FastRawScaleShaders initWithMetalContext:].cold.22
- -[H13FastRawScaleShaders initWithMetalContext:].cold.23
- -[H13FastRawScaleShaders initWithMetalContext:].cold.24
- -[H13FastRawScaleShaders initWithMetalContext:].cold.25
- -[H13FastRawScaleShaders initWithMetalContext:].cold.26
- -[H13FastRawScaleShaders initWithMetalContext:].cold.27
- -[H13FastRawScaleShaders initWithMetalContext:].cold.28
- -[H13FastRawScaleShaders initWithMetalContext:].cold.29
- -[H13FastRawScaleShaders initWithMetalContext:].cold.3
- -[H13FastRawScaleShaders initWithMetalContext:].cold.30
- -[H13FastRawScaleShaders initWithMetalContext:].cold.31
- -[H13FastRawScaleShaders initWithMetalContext:].cold.32
- -[H13FastRawScaleShaders initWithMetalContext:].cold.33
- -[H13FastRawScaleShaders initWithMetalContext:].cold.34
- -[H13FastRawScaleShaders initWithMetalContext:].cold.35
- -[H13FastRawScaleShaders initWithMetalContext:].cold.36
- -[H13FastRawScaleShaders initWithMetalContext:].cold.4
- -[H13FastRawScaleShaders initWithMetalContext:].cold.5
- -[H13FastRawScaleShaders initWithMetalContext:].cold.6
- -[H13FastRawScaleShaders initWithMetalContext:].cold.7
- -[H13FastRawScaleShaders initWithMetalContext:].cold.8
- -[H13FastRawScaleShaders initWithMetalContext:].cold.9
- -[H13FastRawScaleStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[H13UtilityConvertShaders initWithMetalContext:inputPixelFormat:outputPixelFormat:].cold.3
- -[H13UtilityConvertShaders initWithMetalContext:inputPixelFormat:outputPixelFormat:].cold.4
- -[H13UtilityConvertShaders initWithMetalContext:inputPixelFormat:outputPixelFormat:].cold.5
- -[H13UtilityConvertStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[LearnedNRNetworkShaders initWithMetal:].cold.2
- -[LearnedNRNetworkStage availableImagingNetworksWithExtension:]
- -[LearnedNRNetworkStage getNetworkPath].cold.1
- -[LearnedNRNetworkStage getNetworkPath].cold.2
- -[LearnedNRNetworkStage getNetworkPath].cold.3
- -[LearnedNRNetworkStage initWithContext:cameraInfo:isQuadra:deviceGeneration:]
- -[LearnedNRNetworkStage initWithContext:cameraInfo:isQuadra:deviceGeneration:].cold.1
- -[LearnedNRNetworkStage initWithContext:cameraInfo:isQuadra:deviceGeneration:].cold.2
- -[LearnedNRNetworkStage initWithContext:cameraInfo:isQuadra:deviceGeneration:].cold.3
- -[LearnedNRNetworkStage initWithContext:cameraInfo:isQuadra:deviceGeneration:].cold.4
- -[LearnedNRNetworkStage initWithContext:cameraInfo:isQuadra:deviceGeneration:].cold.5
- -[LearnedNRNetworkStage initWithContext:cameraInfo:isQuadra:deviceGeneration:].cold.6
- -[LearnedNRNetworkStage initWithContext:cameraInfo:isQuadra:deviceGeneration:].cold.7
- -[LocalToneMappingStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[NRFBackgroundLearnedNR initWithContext:cameraInfo:isQuadra:deviceGeneration:]
- -[NRFBackgroundLearnedNR initWithContext:cameraInfo:isQuadra:deviceGeneration:].cold.1
- -[NRFProcessorV4 setupWithOptions:].cold.12
- -[QuadraBinShaders initWithMetalContext:].cold.2
- -[QuadraBinShaders initWithMetalContext:].cold.3
- -[QuadraBinStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[QuadraBinStage runWithArgs:].cold.14
- -[QuadraBinStage validateInputFrame:config:].cold.5
- -[RawDFCommon _allocateAndFillLumaChromaImage:withSourceRGB:withSourceMetadata:withAllocatorLabel:demosaicStage:].cold.5
- -[RawDFDeferredFrames addFrame:inputCMITexture:metadata:frameType:uniqueFrameId:processFrame:].cold.2
- -[RawDFFrames .cxx_destruct]
- -[RawDFFrames addFrame:]
- -[RawDFFrames frames]
- -[RawDFFrames getFrameWithUniqueFrameId:]
- -[RawDFFrames initWithMetalContext:]
- -[RawDFFrames initWithMetalContext:].cold.1
- -[RawDFFrames initWithMetalContext:].cold.2
- -[RawDFFrames init]
- -[RawDFFrames referenceFrameIndex]
- -[RawDFFrames referenceFrame]
- -[RawDFFrames releaseAll]
- -[RawDFFrames releaseRgbTextures]
- -[RawDFFrames setReferenceFrameIndex:]
- -[RawDFFrames setReferenceFrameIndex:].cold.1
- -[RawDFFrames sifrFrameIndex]
- -[RawDFFrames sifrFrame]
- -[RawDFInputFrame .cxx_destruct]
- -[RawDFInputFrame _checkRgbTexConfig:]
- -[RawDFInputFrame _checkRgbTexConfig:].cold.1
- -[RawDFInputFrame _checkRgbTexConfig:].cold.2
- -[RawDFInputFrame _checkRgbTexConfig:].cold.3
- -[RawDFInputFrame _checkRgbTexConfig:].cold.4
- -[RawDFInputFrame allocateAndDemosaic:]
- -[RawDFInputFrame allocateAndDemosaic:].cold.1
- -[RawDFInputFrame allocateAndDemosaic:].cold.2
- -[RawDFInputFrame allocateRGB]
- -[RawDFInputFrame allocateRGB].cold.1
- -[RawDFInputFrame auxDraftDemosaicLumaTexture]
- -[RawDFInputFrame auxDraftDemosaicPixelBuffer]
- -[RawDFInputFrame auxDraftDemosaicRGBTexture]
- -[RawDFInputFrame baseTex]
- -[RawDFInputFrame bayerPattern]
- -[RawDFInputFrame bindingMetalFormat]
- -[RawDFInputFrame cameraInfo]
- -[RawDFInputFrame checkAndSetRgbTex:]
- -[RawDFInputFrame checkAndSetRgbTex:].cold.1
- -[RawDFInputFrame commonInitWithMetalContext:cameraInfo:inputFrame:metadata:uniqueFrameId:]
- -[RawDFInputFrame commonInitWithMetalContext:cameraInfo:inputFrame:metadata:uniqueFrameId:].cold.1
- -[RawDFInputFrame commonInitWithMetalContext:cameraInfo:inputPixelBuffer:metadata:uniqueFrameId:]
- -[RawDFInputFrame commonInitWithMetalContext:cameraInfo:inputPixelBuffer:metadata:uniqueFrameId:].cold.1
- -[RawDFInputFrame commonInitWithMetalContext:cameraInfo:inputSamplebuffer:uniqueFrameId:]
- -[RawDFInputFrame dealloc]
- -[RawDFInputFrame demosaicWithStage:]
- -[RawDFInputFrame demosaicWithStage:].cold.1
- -[RawDFInputFrame demosaicWithStage:].cold.2
- -[RawDFInputFrame demosaicWithStage:].cold.3
- -[RawDFInputFrame demosaicWithStage:].cold.4
- -[RawDFInputFrame gdcParameters]
- -[RawDFInputFrame getGDCParametersWithCameraInfoByPortType:]
- -[RawDFInputFrame getGDCParametersWithCameraInfoByPortType:withMetadata:]
- -[RawDFInputFrame getGDCParametersWithCameraInfoByPortType:withMetadata:].cold.1
- -[RawDFInputFrame getGDCParametersWithCameraInfoByPortType:withMetadata:].cold.2
- -[RawDFInputFrame getGDCParametersWithCameraInfoByPortType:withMetadata:].cold.3
- -[RawDFInputFrame hasStandardMetadata]
- -[RawDFInputFrame heightAlignment]
- -[RawDFInputFrame height]
- -[RawDFInputFrame initFrameProperties]
- -[RawDFInputFrame initFrameProperties].cold.1
- -[RawDFInputFrame initFrameProperties].cold.2
- -[RawDFInputFrame initWithMetalContext:cameraInfo:inputFrame:metadata:uniqueFrameId:]
- -[RawDFInputFrame initWithMetalContext:cameraInfo:inputPixelBuffer:metadata:uniqueFrameId:]
- -[RawDFInputFrame initWithMetalContext:cameraInfo:inputSampleBuffer:uniqueFrameId:]
- -[RawDFInputFrame init]
- -[RawDFInputFrame lscGainMapBuffer]
- -[RawDFInputFrame lscGainMapParameters]
- -[RawDFInputFrame metadata]
- -[RawDFInputFrame pixelBufferFormat]
- -[RawDFInputFrame pixelBuffer]
- -[RawDFInputFrame prepareInputFrame]
- -[RawDFInputFrame properties]
- -[RawDFInputFrame pyramid]
- -[RawDFInputFrame releaseBaseTex]
- -[RawDFInputFrame releaseRgbTex]
- -[RawDFInputFrame rgbTex]
- -[RawDFInputFrame sensorHeight]
- -[RawDFInputFrame sensorWidth]
- -[RawDFInputFrame setBindingMetalFormat:]
- -[RawDFInputFrame setHeightAlignment:]
- -[RawDFInputFrame setProperties:]
- -[RawDFInputFrame setStrideAlignment:]
- -[RawDFInputFrame strideAlignment]
- -[RawDFInputFrame uniqueFrameId]
- -[RawDFInputFrame width]
- -[RawDFNetworkPreprocessShaders initWithMetal:isV2:].cold.3
- -[RawDFNetworkStage availableImagingNetworksWithExtension:]
- -[RawDFNetworkStage getFilePathForNetworkIdentifier:withExtension:]
- -[RawDFNetworkStage getFilePathForNetworkIdentifier:withExtension:].cold.1
- -[RawDFNetworkStage getFilePathForNetworkIdentifier:withExtension:].cold.2
- -[RawDFPowerBlurStage .cxx_destruct]
- -[RawDFPowerBlurStage convertRawDFNoiseModel:toPowerBlurNoiseModel:]
- -[RawDFPowerBlurStage initWithMetalContext:]
- -[RawDFPowerBlurStage initWithMetalContext:].cold.1
- -[RawDFPowerBlurStage initWithMetalContext:].cold.2
- -[RawDFPowerBlurStage initWithMetalContext:].cold.3
- -[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:]
- -[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:].cold.1
- -[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:].cold.2
- -[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:].cold.3
- -[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:].cold.4
- -[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:].cold.5
- -[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:].cold.6
- -[RawDFPowerBlurStage setTuningParams:]
- -[RawDFPowerBlurStage tuningParams]
- -[RawDFPowerBlurTuningParams isEnabledForFrameType:]
- -[RawDFPowerBlurTuningParams readPlist:]
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.21
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.22
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.23
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.24
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.25
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.26
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.27
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.28
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.29
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.30
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.31
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.32
- -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.33
- -[RawDFProcessor _downscaleRoiForRegistration:]
- -[RawDFProcessor _processInputFrame:]
- -[RawDFProcessor _processInputFrame:].cold.1
- -[RawDFProcessor _processInputFrame:].cold.2
- -[RawDFProcessor _processInputFrame:].cold.3
- -[RawDFProcessor _processInputFrame:].cold.4
- -[RawDFProcessor _registerImages:]
- -[RawDFProcessor _registerImages:].cold.1
- -[RawDFProcessor _registerImages:].cold.2
- -[RawDFProcessor _registerImages:].cold.3
- -[RawDFProcessor _registerImages:].cold.4
- -[RawDFProcessor _setupFusionConfig].cold.4
- -[RawDFProcessor _setupFusionConfig].cold.5
- -[RawDFProcessor _setupFusionConfig].cold.6
- -[RawDFProcessor _verifyConsistentMetadataWithFrame:]
- -[RawDFProcessor initWithCommandQueue:].cold.10
- -[RawDFProcessor initWithCommandQueue:].cold.11
- -[RawDFProcessor initWithCommandQueue:].cold.12
- -[RawDFProcessor initWithCommandQueue:].cold.13
- -[RawDFProcessor initWithCommandQueue:].cold.14
- -[RawDFProcessor initWithCommandQueue:].cold.15
- -[RawDFProcessor initWithCommandQueue:].cold.16
- -[RawDFProcessor initWithCommandQueue:].cold.17
- -[RawDFProcessor initWithCommandQueue:].cold.18
- -[RawDFProcessor initWithCommandQueue:].cold.19
- -[RawDFProcessor initWithCommandQueue:].cold.2
- -[RawDFProcessor initWithCommandQueue:].cold.20
- -[RawDFProcessor initWithCommandQueue:].cold.21
- -[RawDFProcessor initWithCommandQueue:].cold.3
- -[RawDFProcessor initWithCommandQueue:].cold.4
- -[RawDFProcessor initWithCommandQueue:].cold.5
- -[RawDFProcessor initWithCommandQueue:].cold.6
- -[RawDFProcessor initWithCommandQueue:].cold.7
- -[RawDFProcessor initWithCommandQueue:].cold.8
- -[RawDFProcessor initWithCommandQueue:].cold.9
- -[RawDFProcessor processingType]
- -[RawDFProcessor regwarpInputSurface]
- -[RawDFProcessor setProcessingType:]
- -[RawDFProcessor setReferenceFrameIndex:].cold.1
- -[RawDFProcessor setRegwarpInputSurface:]
- -[RawDFProcessor setRegwarpInputSurface:].cold.1
- -[RawDFProcessor setRegwarpInputSurface:].cold.2
- -[RawDFProcessor(Tuning) prepareTuning:]
- -[RawDFProcessor(Tuning) prepareTuning:].cold.1
- -[RawDFProcessor(Tuning) prepareTuning:].cold.2
- -[RawDFProcessor(Tuning) prepareTuning:].cold.3
- -[RawDFProcessor(Tuning) prepareTuning:].cold.4
- -[RawDFProcessor(Tuning) prepareTuning:].cold.5
- -[RawDFProcessor(Tuning) prepareTuning:].cold.6
- -[RawDFSyntheticReferenceStage packSyntheticReference:toOutputTex:]
- -[RawDFSyntheticReferenceStage packSyntheticReference:toOutputTex:].cold.1
- -[RawDFSyntheticReferenceStage packSyntheticReference:toOutputTex:].cold.2
- -[RawDFSyntheticReferenceStage packSyntheticReference:toOutputTex:].cold.3
- -[RawDFZoomShaders initWithMetal:].cold.4
- -[RawNightModeDemWarpStage .cxx_destruct]
- -[RawNightModeDemWarpStage _isBayer:]
- -[RawNightModeDemWarpStage initWithMetalContext:]
- -[RawNightModeDemWarpStage initWithMetalContext:].cold.1
- -[RawNightModeDemWarpStage initWithMetalContext:].cold.2
- -[RawNightModeDemWarpStage initWithMetalContext:].cold.3
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:]
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:]
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.1
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.10
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.2
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.3
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.4
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.5
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.6
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.7
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.8
- -[RawNightModeDemWarpStage runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:].cold.9
- -[RawNightModeDenoiseInference initWithMetalContext:isQuadra:isBarrington:isArgyleTripodMax:].cold.13
- -[RawNightModeFusionInference initWithMetalContext:isQuadra:isBarrington:requiresDarkCurrentNoiseModel:].cold.13
- -[RawNightModeFusionMetalStage compileShaders].cold.14
- -[RawNightModeMultiFrameOutlierPixelCorrection createShaderWithOptions:]
- -[RawNightModeProcessor initWithCommandQueue:].cold.20
- -[RawNightModeProcessor regwarpInputSurface]
- -[RawNightModeProcessor runDemWarpOnFrame:outputTexture:label:]
- -[RawNightModeProcessor setRegwarpInputSurface:]
- -[RegDense prepareWithImageWidth:imageHeight:]
- -[RegDense prepareWithRegDenseParams:imageWidth:imageHeight:]
- -[RegDense prepareWithRegDenseParams:imageWidth:imageHeight:].cold.1
- -[RegDense prepareWithRegDenseParams:imageWidth:imageHeight:].cold.2
- -[RegDense prepareWithRegDenseParams:imageWidth:imageHeight:].cold.3
- -[RegDense prepareWithRegDenseParams:imageWidth:imageHeight:].cold.4
- -[RegDense prepareWithRegDenseParams:imageWidth:imageHeight:].cold.5
- -[RegDense prepareWithRegDenseParams:imageWidth:imageHeight:].cold.6
- -[RegDense runWithReferenceTex:nonReferenceTex:warpedTex:relativeBrightness:homography:regDenseParams:alwaysDense:refWeightsLevel:nonRefWeightsLevel:].cold.8
- -[RegPyrFusionShaders createPipelineStateWithMetal:vFunction:fShaderName:outputColorMetalFormat:]
- -[RegPyrFusionShaders createPipelineStateWithMetal:vFunction:fShaderName:outputColorMetalFormat:constantValues:]
- -[RegPyrFusionShaders createPipelineStateWithMetal:vFunction:fShaderName:outputColorMetalFormat:constantValues:].cold.1
- -[RegPyrFusionShaders createPipelineStateWithMetal:vFunction:fShaderName:outputColorMetalFormat:constantValues:].cold.2
- -[RegPyrFusionShaders createPipelineStateWithMetal:vFunction:fShaderName:outputColorMetalFormat:constantValues:].cold.3
- -[RegPyrFusionShaders initWithMetal:].cold.16
- -[RegWarpShaders initWithMetalContext:].cold.2
- -[RegWarpShaders initWithMetalContext:].cold.3
- -[RegWarpStage auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[SemanticStylesShaders initWithMetalContext:].cold.7
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.10
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.11
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.12
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.13
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.14
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.15
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.4
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.5
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.6
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.7
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.8
- -[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:].cold.9
- -[SoftISPPipeline auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:]
- -[SoftISPPipeline auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:].cold.1
- -[SoftISPPipeline auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:].cold.2
- -[SoftISPProcessor auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:]
- -[SoftISPProcessor auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:].cold.1
- -[SoftISPProcessor auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:].cold.2
- -[SoftISPProcessor auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:].cold.3
- -[SoftLTM computeLTM:metadata:applyCCM:]
- -[SoftLTM computeLTM:metadata:applyCCM:].cold.1
- -[SoftLTM computeLTM:metadata:applyCCM:].cold.2
- -[SoftLTM initWithCommandQueue:]
- -[SoftLTM initWithCommandQueue:].cold.1
- -[SoftLTM initWithCommandQueue:].cold.2
- -[SoftLTM processLTMMetadata:toDarkestFrame:toEV0Frame:].cold.1
- -[SoftLTM rawDFSoftLTMMode]
- -[SubjectRelightingShaders initWithMetalContext:].cold.12
- -[ToneMappingCurves regularizeLocalToneCurves:mask:tcrParams:imageDims:].cold.3
- -[ToneMappingCurves setToneCurvesWithLTC:GTC:backgroundCurves:colorCorrectionMatrix:enableUTM:dump:].cold.14
- -[ToneMappingCurves setToneCurvesWithLTC:GTC:backgroundCurves:colorCorrectionMatrix:enableUTM:dump:].cold.15
- -[ToneMappingShaders initWithMetal:].cold.18
- -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:]
- -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:].cold.1
- -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:].cold.2
- -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:].cold.3
- -[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:].cold.4
- -[UBProcessorV4 _bindRegWarpPPWithWidth:height:pixelFormat:].cold.6
- -[UBProcessorV4 _isMetadataConsistentWithFirstFrame].cold.3
- -[UBProcessorV4 _nrfFuseImages].cold.13
- -[UBProcessorV4 _nrfFuseImages].cold.14
- -[UBProcessorV4 _perFrameProcessing:input:cfp:].cold.15
- -[UBProcessorV4 _perFrameProcessing:input:cfp:].cold.16
- -[UBProcessorV4 _processInferenceImage:sourceFrameType:sourceFrameIndex:ltcFrameIndex:gtcFrameIndex:originalWidth:originalHeight:].cold.6
- -[UBProcessorV4 _processInferenceImage:sourceFrameType:sourceFrameIndex:ltcFrameIndex:gtcFrameIndex:originalWidth:originalHeight:].cold.7
- -[UBProcessorV4 addFrame:].cold.9
- -[UBProcessorV4 calculateBackingBufferSizeForDesc:nrfConfig:processingType:metal:].cold.3
- -[UBProcessorV4 initWithCommandQueue:].cold.1
- -[UBProcessorV4 regwarpInputSurface]
- -[UBProcessorV4 setOutput:].cold.4
- -[UBProcessorV4 setReferenceFrameIndex:].cold.1
- -[UBProcessorV4 setReferenceFrameIndex:].cold.2
- -[UBProcessorV4 setRegwarpInputSurface:]
- -[UBProcessorV4 setRegwarpInputSurface:].cold.1
- -[UBProcessorV4 verifyIOSurfaceCompression:]
- -[UBProcessorV4 verifyIOSurfaceCompression:].cold.1
- -[UBProcessorV4 verifyIOSurfaceCompression:].cold.2
- GCC_except_table18
- GCC_except_table21
- _CFArrayGetValueAtIndex
- _CFDictionaryGetValue
- _CFNumberGetValue
- _CMILSCOISAdaptation_extrapAndCropCICWithOISOffset
- _CMILSCOISAdaptation_extrapAndCropLSCLumaOnlyWithOISOffset
- _CVPixelBufferCreateWithIOSurface
- _CVPixelFormatDescriptionCreateWithPixelFormatType
- _FigCaptureCFCreatePropertyList
- _FigCapturePlatformGetVariant
- _FigSignalErrorAt
- _GetPixelSizeInBytes
- _GetPixelSizeInBytes.cold.1
- _IOSurfaceGetCompressionTypeOfPlane
- _IOSurfaceGetHeight
- _IOSurfaceGetWidth
- _NSLog
- _OBJC_CLASS_$_DeepFusionCommon
- _OBJC_CLASS_$_H13FastPowerBlurConfig
- _OBJC_CLASS_$_H13FastPowerBlurShaders
- _OBJC_CLASS_$_H13FastPowerBlurStage
- _OBJC_CLASS_$_H13FastPowerBlurStageArgs
- _OBJC_CLASS_$_H13FastPowerBlurStageMetal
- _OBJC_CLASS_$_MTLRenderPipelineDescriptor
- _OBJC_CLASS_$_NSFileManager
- _OBJC_CLASS_$_RawDFFrames
- _OBJC_CLASS_$_RawDFInputFrame
- _OBJC_CLASS_$_RawDFPowerBlurStage
- _OBJC_CLASS_$_RawDFPowerBlurTuningParams
- _OBJC_CLASS_$_RawNightModeDemWarpStage
- _OBJC_IVAR_$_DFPlist.powerBlurTuning
- _OBJC_IVAR_$_DeepFusionProcessor._networkVersion
- _OBJC_IVAR_$_DeepFusionProcessor._rawDFPowerBlurStage
- _OBJC_IVAR_$_DeepFusionProcessor._rawDFSoftLTMMode
- _OBJC_IVAR_$_DenoiseFusePipeline._deepFusionEnabled
- _OBJC_IVAR_$_DenoiseFusePipeline._ubFusionEnabled
- _OBJC_IVAR_$_GainMapStage._currentCommandBuffer
- _OBJC_IVAR_$_H13FastPowerBlurShaders._applyPowerBlur
- _OBJC_IVAR_$_H13FastPowerBlurShaders._remosaicRGB
- _OBJC_IVAR_$_H13FastPowerBlurShaders._remosaicYUV
- _OBJC_IVAR_$_H13FastPowerBlurShaders._resampleHalfSizeToFullSizeRGB
- _OBJC_IVAR_$_H13FastPowerBlurShaders._resampleHalfSizeToFullSizeYUV
- _OBJC_IVAR_$_H13FastPowerBlurShaders._resampleRawAndCreateHighFrequencyMap
- _OBJC_IVAR_$_H13FastPowerBlurStage._metal
- _OBJC_IVAR_$_H13FastPowerBlurStage._outputDownscaleFactor
- _OBJC_IVAR_$_H13FastPowerBlurStage._shaders
- _OBJC_IVAR_$_H13FastPowerBlurStage._stageMetal
- _OBJC_IVAR_$_H13FastPowerBlurStage._staticParameters
- _OBJC_IVAR_$_H13FastPowerBlurStageArgs._bounds
- _OBJC_IVAR_$_H13FastPowerBlurStageArgs._config
- _OBJC_IVAR_$_H13FastPowerBlurStageArgs._inputChromaTex
- _OBJC_IVAR_$_H13FastPowerBlurStageArgs._inputFrame
- _OBJC_IVAR_$_H13FastPowerBlurStageArgs._inputLumaTex
- _OBJC_IVAR_$_H13FastPowerBlurStageArgs._outputChromaTex
- _OBJC_IVAR_$_H13FastPowerBlurStageArgs._outputFrame
- _OBJC_IVAR_$_H13FastPowerBlurStageArgs._outputLumaTex
- _OBJC_IVAR_$_H13FastPowerBlurStageMetal._metal
- _OBJC_IVAR_$_H13FastPowerBlurStageMetal._shaders
- _OBJC_IVAR_$_NRFConfig._enableDeepFusion
- _OBJC_IVAR_$_NRFConfig._enableUBFusion
- _OBJC_IVAR_$_NRFConfig._swfrEnabled
- _OBJC_IVAR_$_NRFPlist.powerBlurTuning
- _OBJC_IVAR_$_NRFPlist.proxyAssetEV0RefDenoising
- _OBJC_IVAR_$_NRFPlist.proxyAssetEVMRefDenoising
- _OBJC_IVAR_$_RawDFFrames._frames
- _OBJC_IVAR_$_RawDFFrames._metal
- _OBJC_IVAR_$_RawDFFrames._referenceFrameIndex
- _OBJC_IVAR_$_RawDFFrames._referenceFrameUniqueId
- _OBJC_IVAR_$_RawDFFrames._sifrFrameIndex
- _OBJC_IVAR_$_RawDFInputFrame._auxDraftDemosaicLumaTexture
- _OBJC_IVAR_$_RawDFInputFrame._auxDraftDemosaicPixelBuffer
- _OBJC_IVAR_$_RawDFInputFrame._auxDraftDemosaicRGBTexture
- _OBJC_IVAR_$_RawDFInputFrame._baseTex
- _OBJC_IVAR_$_RawDFInputFrame._bayerPattern
- _OBJC_IVAR_$_RawDFInputFrame._bindingMetalFormat
- _OBJC_IVAR_$_RawDFInputFrame._cameraInfo
- _OBJC_IVAR_$_RawDFInputFrame._gdcParameters
- _OBJC_IVAR_$_RawDFInputFrame._hasStandardMetadata
- _OBJC_IVAR_$_RawDFInputFrame._height
- _OBJC_IVAR_$_RawDFInputFrame._heightAlignment
- _OBJC_IVAR_$_RawDFInputFrame._isVeratileRegroupedPixelFormat
- _OBJC_IVAR_$_RawDFInputFrame._lscGainMapBuffer
- _OBJC_IVAR_$_RawDFInputFrame._lscGainMapParameters
- _OBJC_IVAR_$_RawDFInputFrame._metadata
- _OBJC_IVAR_$_RawDFInputFrame._metal
- _OBJC_IVAR_$_RawDFInputFrame._pixelBuffer
- _OBJC_IVAR_$_RawDFInputFrame._pixelBufferFormat
- _OBJC_IVAR_$_RawDFInputFrame._properties
- _OBJC_IVAR_$_RawDFInputFrame._pyramid
- _OBJC_IVAR_$_RawDFInputFrame._rgbTex
- _OBJC_IVAR_$_RawDFInputFrame._sampleBuffer
- _OBJC_IVAR_$_RawDFInputFrame._sensorHeight
- _OBJC_IVAR_$_RawDFInputFrame._sensorWidth
- _OBJC_IVAR_$_RawDFInputFrame._strideAlignment
- _OBJC_IVAR_$_RawDFInputFrame._uniqueFrameId
- _OBJC_IVAR_$_RawDFInputFrame._width
- _OBJC_IVAR_$_RawDFPowerBlurStage._metal
- _OBJC_IVAR_$_RawDFPowerBlurStage._stageMetal
- _OBJC_IVAR_$_RawDFPowerBlurStage._tuningParams
- _OBJC_IVAR_$_RawDFPowerBlurTuningParams.defaultTuning
- _OBJC_IVAR_$_RawDFPowerBlurTuningParams.quadraTuning
- _OBJC_IVAR_$_RawDFProcessor._deepFusionSyntheticReferenceReferenceIsSIFR
- _OBJC_IVAR_$_RawDFProcessor._draftDemosaicStage
- _OBJC_IVAR_$_RawDFProcessor._fusionOptions
- _OBJC_IVAR_$_RawDFProcessor._maxBlinkDetectScore
- _OBJC_IVAR_$_RawDFProcessor._maxCornerScore
- _OBJC_IVAR_$_RawDFProcessor._maxFocusScore
- _OBJC_IVAR_$_RawDFProcessor._memoryRequirements
- _OBJC_IVAR_$_RawDFProcessor._minGyroScore
- _OBJC_IVAR_$_RawDFProcessor._rawDFPowerBlurStage
- _OBJC_IVAR_$_RawDFProcessor._rawDFSoftLTMMode
- _OBJC_IVAR_$_RawDFProcessor._regWarpInputTex
- _OBJC_IVAR_$_RawDFProcessor._regwarpInputSurface
- _OBJC_IVAR_$_RawDFProcessor._saveInputFramesToDisk
- _OBJC_IVAR_$_RawDFProcessor._srlEnable
- _OBJC_IVAR_$_RawDFProcessor._useSyntheticReferenceForInferences
- _OBJC_IVAR_$_RawNightModeDemWarpStage._demWarpPipelineBayer
- _OBJC_IVAR_$_RawNightModeDemWarpStage._demWarpPipelineQuadra
- _OBJC_IVAR_$_RawNightModeDemWarpStage._metal
- _OBJC_IVAR_$_RawNightModeProcessor._demWarp
- _OBJC_IVAR_$_RawNightModeProcessor._regwarpInputSurface
- _OBJC_IVAR_$_SoftLTM._metalContext
- _OBJC_IVAR_$_SoftLTM._softLtmRawDFMode
- _OBJC_IVAR_$_ToneMappingShaders._ltmApply
- _OBJC_IVAR_$_ToneMappingShaders._ltmApplyBG
- _OBJC_IVAR_$_UBProcessorV4._regwarpInputSurface
- _OBJC_METACLASS_$_DeepFusionCommon
- _OBJC_METACLASS_$_H13FastPowerBlurConfig
- _OBJC_METACLASS_$_H13FastPowerBlurShaders
- _OBJC_METACLASS_$_H13FastPowerBlurStage
- _OBJC_METACLASS_$_H13FastPowerBlurStageArgs
- _OBJC_METACLASS_$_H13FastPowerBlurStageMetal
- _OBJC_METACLASS_$_RawDFFrames
- _OBJC_METACLASS_$_RawDFInputFrame
- _OBJC_METACLASS_$_RawDFPowerBlurStage
- _OBJC_METACLASS_$_RawDFPowerBlurTuningParams
- _OBJC_METACLASS_$_RawNightModeDemWarpStage
- _OUTLINED_FUNCTION_100
- _OUTLINED_FUNCTION_101
- _OUTLINED_FUNCTION_102
- _OUTLINED_FUNCTION_103
- _OUTLINED_FUNCTION_104
- _OUTLINED_FUNCTION_105
- _OUTLINED_FUNCTION_106
- _OUTLINED_FUNCTION_107
- _OUTLINED_FUNCTION_108
- _OUTLINED_FUNCTION_109
- _OUTLINED_FUNCTION_110
- _OUTLINED_FUNCTION_111
- _OUTLINED_FUNCTION_112
- _OUTLINED_FUNCTION_113
- _OUTLINED_FUNCTION_114
- _OUTLINED_FUNCTION_115
- _OUTLINED_FUNCTION_116
- _OUTLINED_FUNCTION_117
- _OUTLINED_FUNCTION_118
- _OUTLINED_FUNCTION_119
- _OUTLINED_FUNCTION_120
- _OUTLINED_FUNCTION_121
- _OUTLINED_FUNCTION_122
- _OUTLINED_FUNCTION_123
- _OUTLINED_FUNCTION_124
- _OUTLINED_FUNCTION_125
- _OUTLINED_FUNCTION_126
- _OUTLINED_FUNCTION_127
- _OUTLINED_FUNCTION_128
- _OUTLINED_FUNCTION_129
- _OUTLINED_FUNCTION_130
- _OUTLINED_FUNCTION_45
- _OUTLINED_FUNCTION_46
- _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_48
- _OUTLINED_FUNCTION_49
- _OUTLINED_FUNCTION_50
- _OUTLINED_FUNCTION_51
- _OUTLINED_FUNCTION_52
- _OUTLINED_FUNCTION_53
- _OUTLINED_FUNCTION_54
- _OUTLINED_FUNCTION_55
- _OUTLINED_FUNCTION_56
- _OUTLINED_FUNCTION_57
- _OUTLINED_FUNCTION_58
- _OUTLINED_FUNCTION_59
- _OUTLINED_FUNCTION_60
- _OUTLINED_FUNCTION_61
- _OUTLINED_FUNCTION_62
- _OUTLINED_FUNCTION_63
- _OUTLINED_FUNCTION_64
- _OUTLINED_FUNCTION_65
- _OUTLINED_FUNCTION_66
- _OUTLINED_FUNCTION_67
- _OUTLINED_FUNCTION_68
- _OUTLINED_FUNCTION_69
- _OUTLINED_FUNCTION_70
- _OUTLINED_FUNCTION_71
- _OUTLINED_FUNCTION_72
- _OUTLINED_FUNCTION_73
- _OUTLINED_FUNCTION_74
- _OUTLINED_FUNCTION_75
- _OUTLINED_FUNCTION_76
- _OUTLINED_FUNCTION_77
- _OUTLINED_FUNCTION_78
- _OUTLINED_FUNCTION_79
- _OUTLINED_FUNCTION_80
- _OUTLINED_FUNCTION_81
- _OUTLINED_FUNCTION_82
- _OUTLINED_FUNCTION_83
- _OUTLINED_FUNCTION_84
- _OUTLINED_FUNCTION_85
- _OUTLINED_FUNCTION_86
- _OUTLINED_FUNCTION_87
- _OUTLINED_FUNCTION_88
- _OUTLINED_FUNCTION_89
- _OUTLINED_FUNCTION_90
- _OUTLINED_FUNCTION_91
- _OUTLINED_FUNCTION_92
- _OUTLINED_FUNCTION_93
- _OUTLINED_FUNCTION_94
- _OUTLINED_FUNCTION_95
- _OUTLINED_FUNCTION_96
- _OUTLINED_FUNCTION_97
- _OUTLINED_FUNCTION_98
- _OUTLINED_FUNCTION_99
- _PDCSetKernel.cold.1
- __OBJC_$_CLASS_METHODS_DeepFusionCommon
- __OBJC_$_CLASS_METHODS_RawDFInputFrame
- __OBJC_$_CLASS_METHODS_RawDFPowerBlurStage
- __OBJC_$_CLASS_METHODS_RawNightModeDemWarpStage
- __OBJC_$_INSTANCE_METHODS_H13FastPowerBlurConfig
- __OBJC_$_INSTANCE_METHODS_H13FastPowerBlurShaders
- __OBJC_$_INSTANCE_METHODS_H13FastPowerBlurStage
- __OBJC_$_INSTANCE_METHODS_H13FastPowerBlurStageArgs
- __OBJC_$_INSTANCE_METHODS_H13FastPowerBlurStageMetal
- __OBJC_$_INSTANCE_METHODS_H13FastRawScaleConfig(PDC|SyntheticThumbnail|RFPN|BlackLevelEstimation|DMA|PDP|HOCL|ABLEST|GOC|ShadingFPNR|BlackLevelShading)
- __OBJC_$_INSTANCE_METHODS_H13FastRawScaleStage(SyntheticThumbnail|FPExtract|Vision|ABLEST|PDC)
- __OBJC_$_INSTANCE_METHODS_RawDFFrames
- __OBJC_$_INSTANCE_METHODS_RawDFInputFrame
- __OBJC_$_INSTANCE_METHODS_RawDFPowerBlurStage
- __OBJC_$_INSTANCE_METHODS_RawDFPowerBlurTuningParams
- __OBJC_$_INSTANCE_METHODS_RawNightModeDemWarpStage
- __OBJC_$_INSTANCE_VARIABLES_H13FastPowerBlurShaders
- __OBJC_$_INSTANCE_VARIABLES_H13FastPowerBlurStage
- __OBJC_$_INSTANCE_VARIABLES_H13FastPowerBlurStageArgs
- __OBJC_$_INSTANCE_VARIABLES_H13FastPowerBlurStageMetal
- __OBJC_$_INSTANCE_VARIABLES_RawDFFrames
- __OBJC_$_INSTANCE_VARIABLES_RawDFInputFrame
- __OBJC_$_INSTANCE_VARIABLES_RawDFPowerBlurStage
- __OBJC_$_INSTANCE_VARIABLES_RawDFPowerBlurTuningParams
- __OBJC_$_INSTANCE_VARIABLES_RawNightModeDemWarpStage
- __OBJC_$_PROP_LIST_H13FastPowerBlurShaders
- __OBJC_$_PROP_LIST_H13FastPowerBlurStage
- __OBJC_$_PROP_LIST_H13FastPowerBlurStageArgs
- __OBJC_$_PROP_LIST_H13FastPowerBlurStageMetal
- __OBJC_$_PROP_LIST_RawDFFrames
- __OBJC_$_PROP_LIST_RawDFInputFrame
- __OBJC_$_PROP_LIST_RawDFPowerBlurStage
- __OBJC_CLASS_PROTOCOLS_$_H13FastPowerBlurStage
- __OBJC_CLASS_PROTOCOLS_$_H13FastPowerBlurStageArgs
- __OBJC_CLASS_RO_$_DeepFusionCommon
- __OBJC_CLASS_RO_$_H13FastPowerBlurConfig
- __OBJC_CLASS_RO_$_H13FastPowerBlurShaders
- __OBJC_CLASS_RO_$_H13FastPowerBlurStage
- __OBJC_CLASS_RO_$_H13FastPowerBlurStageArgs
- __OBJC_CLASS_RO_$_H13FastPowerBlurStageMetal
- __OBJC_CLASS_RO_$_RawDFFrames
- __OBJC_CLASS_RO_$_RawDFInputFrame
- __OBJC_CLASS_RO_$_RawDFPowerBlurStage
- __OBJC_CLASS_RO_$_RawDFPowerBlurTuningParams
- __OBJC_CLASS_RO_$_RawNightModeDemWarpStage
- __OBJC_METACLASS_RO_$_DeepFusionCommon
- __OBJC_METACLASS_RO_$_H13FastPowerBlurConfig
- __OBJC_METACLASS_RO_$_H13FastPowerBlurShaders
- __OBJC_METACLASS_RO_$_H13FastPowerBlurStage
- __OBJC_METACLASS_RO_$_H13FastPowerBlurStageArgs
- __OBJC_METACLASS_RO_$_H13FastPowerBlurStageMetal
- __OBJC_METACLASS_RO_$_RawDFFrames
- __OBJC_METACLASS_RO_$_RawDFInputFrame
- __OBJC_METACLASS_RO_$_RawDFPowerBlurStage
- __OBJC_METACLASS_RO_$_RawDFPowerBlurTuningParams
- __OBJC_METACLASS_RO_$_RawNightModeDemWarpStage
- ___115-[CMIRawNightModeRegistrationStage processConstrainedNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.301
- ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke.229
- ___119-[CMIRawNightModeRegistrationStage processRegWarpRegDenseNonReference:reference:nonRefLumaTex:shiftMap:blendingWeight:]_block_invoke_2.245
- ___121-[RawDFSyntheticReferenceStage _doHighlightRecovery:noiseDivisorOutputTex:evmPyramid:ev0Pyramid:frameProperties:srPlist:]_block_invoke.27
- ___125-[RawDFProxyStage generateOutputNoiseMapLuma:outputNoiseMapChroma:lscGainsTex:ev0:evm:noiseDivisorOutputTex:frameProperties:]_block_invoke.21
- ___134-[RawDFSyntheticReferenceStage _doDeepShadowRecovery:noiseDivisorOutputTex:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:srPlist:]_block_invoke.31
- ___137-[RawDFSyntheticLongStage fuseRefEv0Pyramid:withEv0Pyramids:frameProperties:slPlist:lscGainsTex:outputSyntheticEv0:outputWeightsPyramid:]_block_invoke.29
- ___150-[RegDense runWithReferenceTex:nonReferenceTex:warpedTex:relativeBrightness:homography:regDenseParams:alwaysDense:refWeightsLevel:nonRefWeightsLevel:]_block_invoke_2
- ___175-[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:]_block_invoke
- ___175-[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:]_block_invoke_2
- ___216-[RawDFSyntheticLongStage fuseRefSyntheticEv0Pyramid:withLongPyramid:syntheticEv0WeightsPyramid:frameProperties:slPlist:lscGainsTex:outputSyntheticLong:outputNoiseDivisorSyntheticEv0:outputNoiseDivisorSyntheticLong:]_block_invoke.31
- ___274-[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:]_block_invoke
- ___274-[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:]_block_invoke_2
- ___31-[UBProcessorV4 _nrfFuseImages]_block_invoke.210
- ___58-[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy]_block_invoke.258
- ___82-[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:]_block_invoke
- ___82-[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:]_block_invoke.37
- ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke.24
- ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke_2.27
- ___94-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke_3
- ___98-[DefringeStage defringePyramid:outputPyramid:chromaScratch:quadraBinningFactor:tuningParameters:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e19_"NSDictionary"8?0ls32l8
- ___block_literal_global.105
- ___block_literal_global.107
- ___block_literal_global.110
- ___block_literal_global.112
- ___block_literal_global.128
- ___block_literal_global.135
- ___block_literal_global.137
- ___block_literal_global.140
- ___block_literal_global.142
- ___block_literal_global.146
- ___block_literal_global.161
- ___block_literal_global.163
- ___block_literal_global.166
- ___block_literal_global.168
- ___block_literal_global.185
- ___block_literal_global.187
- ___block_literal_global.192
- ___block_literal_global.199
- ___block_literal_global.201
- ___block_literal_global.206
- ___block_literal_global.208
- ___block_literal_global.225
- ___block_literal_global.231
- ___block_literal_global.241
- ___block_literal_global.248
- ___block_literal_global.30
- ___block_literal_global.81
- ___block_literal_global.87
- ___block_literal_global.88
- ___block_literal_global.90
- ___block_literal_global.99
- ___stack_chk_fail
- ___stack_chk_guard
- __generateLSCGainMapWithLSCMetadata.cold.29
- _colorspace_setCustomCscMatrix
- _createPipelines.cold.289
- _createPipelines.cold.290
- _createPipelines.cold.291
- _createPipelines.cold.292
- _createPipelines.cold.293
- _createPipelines.cold.294
- _createPipelines.cold.295
- _createPipelines.cold.296
- _createPipelines.cold.297
- _createPipelines.cold.298
- _createPipelines.cold.299
- _createPipelines.cold.300
- _createPipelines.cold.301
- _createPipelines.cold.302
- _createPipelines.cold.303
- _createPipelines.cold.304
- _createPipelines.cold.305
- _createPipelines.cold.306
- _createPipelines.cold.307
- _createPipelines.cold.308
- _createPipelines.cold.309
- _createPipelines.cold.310
- _createPipelines.cold.311
- _createPipelines.cold.312
- _createPipelines.cold.313
- _createPipelines.cold.314
- _createPipelines.cold.315
- _createPipelines.cold.316
- _createPipelines.cold.317
- _createPipelines.cold.318
- _createPipelines.cold.319
- _createPipelines.cold.320
- _createPipelines.cold.321
- _createPipelines.cold.322
- _createPipelines.cold.323
- _createPipelines.cold.324
- _createPipelines.cold.325
- _createPipelines.cold.326
- _createPipelines.cold.327
- _createPipelines.cold.328
- _createPipelines.cold.329
- _createPipelines.cold.330
- _createPipelines.cold.331
- _createPipelines.cold.332
- _createPipelines.cold.333
- _createPipelines.cold.334
- _createPipelines.cold.335
- _createPipelines.cold.336
- _createPipelines.cold.337
- _createPipelines.cold.338
- _createPipelines.cold.339
- _createPipelines.cold.340
- _createPipelines.cold.341
- _createPipelines.cold.342
- _createPipelines.cold.343
- _createPipelines.cold.344
- _createPipelines.cold.345
- _createPipelines.cold.346
- _createPipelines.cold.347
- _createPipelines.cold.348
- _createPipelines.cold.349
- _createPipelines.cold.350
- _createPipelines.cold.351
- _createPipelines.cold.352
- _createPipelines.cold.353
- _createPipelines.cold.354
- _createPipelines.cold.355
- _createPipelines.cold.356
- _createPipelines.cold.357
- _createPipelines.cold.358
- _createPipelines.cold.359
- _createPipelines.cold.360
- _createPipelines.cold.361
- _createPipelines.cold.362
- _createPipelines.cold.363
- _createPipelines.cold.364
- _createPipelines.cold.365
- _createPipelines.cold.366
- _createPipelines.cold.367
- _createPipelines.cold.368
- _createPipelines.cold.369
- _createPipelines.cold.370
- _createPipelines.cold.371
- _createPipelines.cold.372
- _createPipelines.cold.373
- _createPipelines.cold.374
- _espresso_network_bind_buffer
- _espresso_plan_get_error_info
- _getLTMCurvesFromMetadataWithKeys.cold.8
- _isCompatibleSensorPortAndRawDFTuningType
- _isRawDFPowerBlurEnabled
- _isRawDFQuadraFrameType
- _isVersatilePixelFormat
- _kACNetworkInputs
- _kACNetworkOutputs
- _kCVPixelFormatBitsPerBlock
- _kDFOpt2NetworkInputs
- _kDFOpt2NetworkOutputs
- _kFusionNetworkInputs
- _kFusionNetworkOutputs
- _kSFDNetworkInputs
- _kSFDNetworkOutputs
- _loadKernel
- _objc_msgSend$_applyPowerBlurWithParams:halfResATex:halfResBTex:commandBuffer:
- _objc_msgSend$_calculateReadNoise:
- _objc_msgSend$_isBayer:
- _objc_msgSend$_preprocessSyntheticReferenceFrame
- _objc_msgSend$_remosaicRgbWithParams:inputTex:lscGainsTex:outputTex:commandBuffer:
- _objc_msgSend$_remosaicYuvWithParams:inputLumaTex:inputChromaTex:lscGainsTex:outputTex:commandBuffer:
- _objc_msgSend$_resampleHalfSizeToFullSizeRgbWithParams:inputTex:halfResTex:outputTex:commandBuffer:
- _objc_msgSend$_resampleHalfSizeToFullSizeYuvWithParams:inputLumaTex:inputChromaTex:halfResTex:outputLumaTex:outputChromaTex:commandBuffer:
- _objc_msgSend$_resampleRawAndCreateHighFrequencyMapWithParams:rawTex:halfResTex:commandBuffer:
- _objc_msgSend$_validateThreadsPerThreadgroup:forPipeline:
- _objc_msgSend$applyPowerBlur
- _objc_msgSend$auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:
- _objc_msgSend$availableImagingNetworksWithExtension:
- _objc_msgSend$compileShader:lumaWrite:chromaWrite:
- _objc_msgSend$computeAverageCurve:withLTM:andGTC:
- _objc_msgSend$computeGainMapWithInput:secondInput:output:properties:mpconfig:
- _objc_msgSend$computeLTM:metadata:applyCCM:
- _objc_msgSend$containsString:
- _objc_msgSend$contentsOfDirectoryAtPath:error:
- _objc_msgSend$convertRawDFNoiseModel:toPowerBlurNoiseModel:
- _objc_msgSend$copyLTM_HLG_Metadata:
- _objc_msgSend$createBasicComputeShader:metal:
- _objc_msgSend$createPipelineStateWithMetal:vFunction:fShaderName:outputColorMetalFormat:
- _objc_msgSend$createPipelineStateWithMetal:vFunction:fShaderName:outputColorMetalFormat:constantValues:
- _objc_msgSend$createShaderWithOptions:
- _objc_msgSend$defaultManager
- _objc_msgSend$doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:
- _objc_msgSend$flexRangeMetadataDictionary:mppHeadroom:newHeadroom:
- _objc_msgSend$fragmentFunction
- _objc_msgSend$fullRangeVertexDesc
- _objc_msgSend$getFilePathForNetworkIdentifier:withExtension:
- _objc_msgSend$getGDCParametersWithCameraInfoByPortType:
- _objc_msgSend$getGDCParametersWithCameraInfoByPortType:withMetadata:
- _objc_msgSend$getPowerBlurConfigForInputFrame:PowerBlurConfig:enablePowerBlur:
- _objc_msgSend$getRawNightModeNetworkBasePath
- _objc_msgSend$getRawNightModeNetworkPathFromBasePath:fromNetworkName:
- _objc_msgSend$getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:
- _objc_msgSend$hasStandardMetadata
- _objc_msgSend$hasSuffix:
- _objc_msgSend$initWithContext:cameraInfo:isQuadra:deviceGeneration:
- _objc_msgSend$initWithMetal:vertFunc:fragName:pixelFormat:pixelFormat2:
- _objc_msgSend$initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:
- _objc_msgSend$initWithPattern:options:error:
- _objc_msgSend$isEnabledForFrameType:
- _objc_msgSend$maxThreadsPerThreadgroup
- _objc_msgSend$networkVersion
- _objc_msgSend$newFunctionWithName:constantValues:error:
- _objc_msgSend$newFunctionWithName:constantValues:pipelineLibrary:error:
- _objc_msgSend$newOutputAuxiliaryPixelBufferForUniqueID:pixelFormat:width:height:
- _objc_msgSend$newRenderPipelineStateWithDescriptor:error:
- _objc_msgSend$normalizeLTMTable:
- _objc_msgSend$numberOfMatchesInString:options:range:
- _objc_msgSend$packSyntheticReference:toOutputTex:
- _objc_msgSend$performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:
- _objc_msgSend$pipelineLibrary
- _objc_msgSend$platformIdentifier
- _objc_msgSend$prepareInputFrame
- _objc_msgSend$prepareWithRegDenseParams:imageWidth:imageHeight:
- _objc_msgSend$processLTM_HLG_Metadata:toDarkestFrame:toEV0Frame:
- _objc_msgSend$rawDFSoftLTMMode
- _objc_msgSend$remosaicRGB
- _objc_msgSend$remosaicYUV
- _objc_msgSend$resampleHalfSizeToFullSizeRGB
- _objc_msgSend$resampleHalfSizeToFullSizeYUV
- _objc_msgSend$resampleRawAndCreateHighFrequencyMap
- _objc_msgSend$runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:
- _objc_msgSend$runDetectorsToOutput:withRequestedSyntheticReferenceMode:withEv0:withEvm:withSRTuning:withDownSampleStage:withColorMatchStage:withMotionDetection:withgrayGhostDetection:withFlickerDetection:
- _objc_msgSend$runMotionToOutput:withRefFrame:withOtherFrame:withPyramidBand:withTuningParams:withMotionDetection:
- _objc_msgSend$runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:
- _objc_msgSend$runWithConfig:inputTex:outputTex:lscGainsTex:
- _objc_msgSend$runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:
- _objc_msgSend$runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:
- _objc_msgSend$sensorHeight
- _objc_msgSend$sensorWidth
- _objc_msgSend$setAllocationHint:
- _objc_msgSend$setBindingMetalFormat:
- _objc_msgSend$setFragmentFunction:
- _objc_msgSend$setGainMapConfig:tuning:frameMetadata:width:height:isLinear:
- _objc_msgSend$setHeightAlignment:
- _objc_msgSend$setPipelineLibrary:
- _objc_msgSend$setRegisters:
- _objc_msgSend$setRegwarpInputSurface:
- _objc_msgSend$setStrideAlignment:
- _objc_msgSend$setThreadgroupMemoryLength:atIndex:
- _objc_msgSend$setVertexDescriptor:
- _objc_msgSend$setVertexFunction:
- _objc_msgSend$startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:
- _objc_msgSend$syntheticReferenceFusionMapPixelBuffer
- _objc_msgSend$syntheticReferencePixelBuffer
- _objc_msgSend$verifyIOSurfaceCompression:
- _objc_msgSend$vertexFunction
- _objc_release_x4
CStrings:
+ " AUTO"
+ " forced OFF"
+ " forced ON"
+ "! ( postDilateThreshold && postDilateSubtract ) is NULL"
+ "! CMIPixelFormatIsVersatileRaw( pixFmt, __objc_yes ) || bayerPattern"
+ "! perBlockAverageLumaPyramid"
+ "! perBlockShiftCostsPyramid"
+ "! perBlockShiftWeightsPyramid"
+ "%@_%d"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "( ! gainMap ) || ( [(id<MTLTextureSPI>)gainMap isCompressed] == false ) is NULL"
+ "( ( width % AMBNR_LUMA_LVL0_FACTOR ) == 0 ) && ( ( height % AMBNR_LUMA_LVL0_FACTOR ) == 0 ) is NULL"
+ "( -73244 )"
+ "( -73245 )"
+ "( -73246 )"
+ "( -73247 )"
+ "( -73251 )"
+ "( -73253 )"
+ "( -73254 )"
+ "( -73255 )"
+ "( -73257 )"
+ "( -73259 )"
+ "( -73260 )"
+ "( -73261 )"
+ "( -73264 )"
+ "( -73265 )"
+ "( -73267 )"
+ "( -73270 )"
+ "( -73273 )"
+ "( -73275 )"
+ "( -73283 )"
+ "( -73288 )"
+ "( -73291 )"
+ "( -73295 )"
+ "( -73297 )"
+ "( -73300 )"
+ "( -73320 )"
+ "( -73326 )"
+ "( -73331 )"
+ "( -73338 )"
+ "( -73339 )"
+ "( -73341 )"
+ "( -73342 )"
+ "( -73344 )"
+ "( -73345 )"
+ "( -73349 )"
+ "( -73353 )"
+ "( -73355 )"
+ "( -73360 )"
+ "( -73361 )"
+ "( -73363 )"
+ "( -73365 )"
+ "( -73367 )"
+ "( -73371 )"
+ "( -73373 )"
+ "( -73374 )"
+ "( -73376 )"
+ "( -73377 )"
+ "( -73379 )"
+ "( -73381 )"
+ "( -73382 )"
+ "( -73383 )"
+ "( -73384 )"
+ "( -73391 )"
+ "( -73419 )"
+ "( -73425 )"
+ "( -73426 )"
+ "( -73436 )"
+ "( -73437 )"
+ "( -73445 )"
+ "( -73450 )"
+ "( -73465 )"
+ "( ltmBinsC == ( 33 ) ) || ( ltmBinsC == ( 65 ) ) || ( ltmBinsC == ( 257 ) )"
+ "( ltmBinsC_BG == ( 33 ) ) || ( ltmBinsC_BG == ( 65 ) ) || ( ltmBinsC_BG == ( 257 ) )"
+ "( width <= inputRGBTex.width ) && ( height <= inputRGBTex.height )"
+ "(?={?=II})40@0:8i16I20I24I28^I32"
+ "(?={?=II})44@0:8i16i20I24I28I32^I36"
+ "(Fig)"
+ "**accumulator = nil"
+ "*outputTex is NULL"
+ "*texture is NULL"
+ "+[BilateralGrid prewarmShaders:]"
+ "+[BilateralGridShared getSharedInstanceOrRelease:]"
+ "+[BlinkDetectionStageShared getSharedInstanceOrRelease:]"
+ "+[CMIImagePyramidShared getSharedInstanceOrRelease:]"
+ "+[CMIRawNightModeRegistrationStage prewarmShaders:]"
+ "+[CMISoftwareFlashRenderingCommon getStrobeWhiteBalanceGains:metadata:outputVector:]"
+ "+[ChromaticAberrationRecoveryConfig getCARConfigForInputFrame:staticParameters:bounds:carConfig:]"
+ "+[ColorConvertStageShared getSharedInstanceOrRelease:]"
+ "+[DeepFusionLaplacianPyramidShared getSharedInstanceOrRelease:]"
+ "+[DefringeStage prewarmShaders:tuningParameters:]"
+ "+[DenoiseAndSharpeningPlist initialize]"
+ "+[DenoiseFusePipelineShared getSharedInstanceOrRelease:]"
+ "+[FusionPlist initialize]"
+ "+[FusionRemixStageShared getSharedInstanceOrRelease:]"
+ "+[GainMapShared getSharedInstanceOrRelease:]"
+ "+[GainMapStage prewarmShaders:]"
+ "+[GrayGhostDetectionShared getSharedInstanceOrRelease:]"
+ "+[GuidedFilter prewarmShaders:]"
+ "+[H13FastBayerProcStage createIntermediateMetalTexture:label:pixelFormat:width:height:compressed:]"
+ "+[H13FastPostDemosaicProcConfigMetal getChromaSuppressionConfigInputFrameMetadata:tuningControls:chromaSuppressionConfig:]"
+ "+[LensShadingCorrectionConfig getLSCMetadata:lscMetadata:bounds:stageConfigMode:processingOptions:metalCtx:staticParameters:forAWB:]"
+ "+[LumaChromaImage bindYCbCrMetalTextureWithMetalContext:pixelBuffer:pixelFormat:textureToBind:alignmentFactor:]"
+ "+[MotionDetection fillMotionDetectionParameters:withNRFPlist:]"
+ "+[MotionDetectionShared getSharedInstanceOrRelease:]"
+ "+[NRFMonitor sharedInstance]_block_invoke"
+ "+[OutliersRemovalShared getSharedInstanceOrRelease:]"
+ "+[OutputNoiseModel generateNoiseModelFromReferenceFrameMetadata:nFusedFrames:tuningPlist:]"
+ "+[PyramidStage prewarmShaders:]"
+ "+[PyramidStageShared compileShader:kernelType:]"
+ "+[PyramidStageShared compileShader:lumaWrite:chromaWrite:error:]"
+ "+[PyramidStageShared getSharedInstanceOrRelease:]"
+ "+[PyramidStorage allocatePyramidWithMetalContext:label:width:height:isFP16:createLuma:createChroma:startingLevel:testSize:pyramid:]"
+ "+[PyramidStorage allocatePyramidWithWidth:height:allocLevel0:levels:texUsage:mtlSubAllocatorID:label:lumaFormat:chromaFormat:outPyramid:metal:]"
+ "+[PyramidStorage pyramidMemorySize:height:overlapLevels:allocLevel0:levels:lumaFormat:chromaFormat:outSize:metal:]"
+ "+[RawDFCommon getRegwarpSurfaceDimensionsForInputWidth:height:]"
+ "+[RawDFLanczos prewarmShaders:]"
+ "+[RawNightModeGreenGhost prewarmShaders:]"
+ "+[RawNightModeInferenceCommon getLSCParams:fromMetadata:fromCameraInfoByPortType:fromLSCGainMapParameters:]"
+ "+[RawNightModeInferenceCommon getTilePadding:forGain:]"
+ "+[RawNightModeProcessor createMetalTextureWithMetalContext:label:width:height:pixelFormat:compressionDisabled:]"
+ "+[RawNightModeProcessor populateLSCWBGParamsFromMetadata:cameraInfoByPortType:lscGainMapParameters:params:]"
+ "+[RawNightModeProcessor populateWBGParamsFromMetadata:params:]"
+ "+[RegDense getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:outRegDenseMapProperties:]"
+ "+[RegDenseShared getSharedInstanceOrRelease:]"
+ "+[RegPyrFusionShared getSharedInstanceOrRelease:]"
+ "+[RegWarpHelperShared getSharedInstanceOrRelease:]"
+ "+[SemanticStylesShared getSharedInstanceOrRelease:]"
+ "+[SemanticStylesStage prewarmShaders:]"
+ "+[SingleColorCubeCorrectionStageShared getSharedInstanceOrRelease:]"
+ "+[SubjectRelightingShared getSharedInstanceOrRelease:]"
+ "+[SubjectRelightingStage prewarmShaders:]"
+ "+[TextureUtilsShared getSharedInstanceOrRelease:]"
+ "+[ToneMappingPlist initialize]"
+ "+[ToneMappingShared getSharedInstanceOrRelease:]"
+ "+[VideoDefringingTuningParameters _validateTuning:mode:parameterKey:]"
+ "+[WarpStageShared getSharedInstanceOrRelease:]"
+ "-1"
+ "-[AMBNRStage computeConfiguration:staticScene:dasPlist:nmPlist:isLowLight:sensorCropRatio:zoomFactor:]"
+ "-[AMBNRStage selectBlurKernelSize:]"
+ "-[AMBNRStage setResourcesWithOutput:inputPyramid:noiseMapPyramid:sharpeningPyramid:localGainMapTex:denoisingOptions:]"
+ "-[BilateralGrid allocGridTexture:label:]"
+ "-[BilateralGrid allocateTextures]"
+ "-[BilateralGrid blurAndNormalize:grid_tmp_tex:]"
+ "-[BilateralGrid buildWithGuideAndConfidence:target:confidence:grid_tex:ltc_tex:gtcRatio_tex:gtcFinal_tex:ltmROI:]"
+ "-[BilateralGrid config:height:space_sigma:range_sigma:solver:]"
+ "-[BilateralGrid initWithContext:normalizeGridConfidence:]"
+ "-[BilateralGrid setupWithConfig:width:height:]"
+ "-[BilateralGrid solverBistochastize:]"
+ "-[BilateralGrid solverPcg:]"
+ "-[BilateralGrid solverfilter:target:confidence:output:]"
+ "-[BilateralGrid solverfilterWithGuide:target:confidence:ltc_tex:gtcRatio_tex:gtcFinal_tex:ltmROI:output:]"
+ "-[BilateralGrid upsample:grid_tex:conf_tex:ltc_tex:gtcRatio_tex:gtcFinal_tex:ltmROI:output:]"
+ "-[BilateralGridShared getShaders:normalizeGridConfidence:]"
+ "-[BlinkDetectionPlist applyOverrides]"
+ "-[BlinkDetectionShaders initWithMetal:]"
+ "-[BlinkDetectionStage init:]"
+ "-[BlinkDetectionStage runOnLumaBand1:lumaBand2:lumaBand3:withFaces:facesCount:plist:resultScore:frameIdx:]"
+ "-[BlinkDetectionStageShared getShaders:]"
+ "-[CMIImagePyramid initWithMetalContext:descriptor:]"
+ "-[CMIImagePyramidDescriptor _isValidWithLogError:]"
+ "-[CMIRawNightModeConstrainedRegistrationTuningParams readPlist:]"
+ "-[CMIRawNightModeRegistrationStage _compileShaders]"
+ "-[CMIRawNightModeRegistrationStage _downsampleLuma:outputLuma:]"
+ "-[CMIRawNightModeRegistrationStage _fuseConfidenceMap:toBlendingWeight:]"
+ "-[CMIRawNightModeRegistrationStage _getDraftDemosaicParamsForInputFrame:draftDemosaicParams:]"
+ "-[CMIRawNightModeRegistrationStage _getWarpConfigForInputFrame:warpConfig:]"
+ "-[CMIRawNightModeRegistrationStage createMetalTexture:width:height:depth:pixelFormat:]"
+ "-[CMIRawNightModeRegistrationStage createMetalTexture:width:height:pixelFormat:compressed:]"
+ "-[CMIRawNightModeRegistrationStage initWithMetalContext:]"
+ "-[CMIRawNightModeRegistrationStage prepareWithImageWidth:imageHeight:registrationType:gdcMode:cameraInfoByPortType:]"
+ "-[CMIRawNightModeRegistrationStage processNonReference:reference:shiftMap:blendingWeight:]"
+ "-[CMIRawNightModeRegistrationStage processReference:]"
+ "-[CMISoftwareFlashRenderingCoreV2 applyWithAmbientLumaTexture:ambientChromaTexture:flashLumaTexture:flashChromaTexture:ambientYUVOffsets:flashYUVOffsets:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:skinMaskTexture:personMaskTexture:ambientWhitePoint:flashWhitePoint:strobeWhitePoint:ambientWhitePointTuned:strobeWhitePointTuned:ambientIntegrationTime:flashIntegrationTime:cropRect:LSCCropRect:fullSizeDimensions:outputLumaTexture:outputChromaTexture:]"
+ "-[CMISoftwareFlashRenderingProcessorV2 addFrame:metadata:frameType:frameParams:]"
+ "-[CMISoftwareFlashRenderingProcessorV2 calculateWhitePoints:outputFlashWhitePoint:outputStrobeWhitePoint:outputAmbientWhitePointTuned:outputStrobeWhitePointTuned:]"
+ "-[CMISoftwareFlashRenderingProcessorV2 encodeCoreAnalyticsIntermediate:flashWhitePoint:strobeWhitePoint:ambientWhitePointTuned:strobeWhitePointTuned:cropRect:]"
+ "-[CMISoftwareFlashRenderingProcessorV2 encodeSoftwareFlashRendering:flashWhitePoint:strobeWhitePoint:ambientWhitePointTuned:strobeWhitePointTuned:cropRect:LSCCropRect:fullSizeCropRect:]"
+ "-[CMISoftwareFlashRenderingProcessorV2 externalMemoryDescriptorForConfiguration:]"
+ "-[CMISoftwareFlashRenderingProcessorV2 prepareToProcess:]"
+ "-[CMISoftwareFlashRenderingProcessorV2 process]"
+ "-[CMISoftwareFlashRenderingProcessorV2 purgeResources]"
+ "-[CMISoftwareFlashRenderingProcessorV2 requiredMetalAllocatorMemorySize]"
+ "-[CMISoftwareFlashRenderingProcessorV2 setup]"
+ "-[CMISoftwareFlashRenderingRegistrationV2 initWithMetalContext:]"
+ "-[CMISoftwareFlashRenderingRegistrationV2 prepareToProcess:]"
+ "-[CMISoftwareFlashRenderingRegistrationV2 registerImage:referenceLumaTexture:]"
+ "-[CMISoftwareFlashRenderingStrobeCorrectionV2 applyStrobeCorrection:ambientComponentRGBTexture:strobeComponentRGBTexture:ambientLSCGainsTexture:flashLSCGainsTexture:ambientLSCMaxGain:flashLSCMaxGain:lscCropRect:fullSizeDimensions:outputAmbientCorrectedRGBTexture:outputStrobeCorrectedRGBTexture:]"
+ "-[CMISoftwareFlashRenderingStyleTransferV2 applyStyleTransferWithBufferClearing:inputChromaTexture:sourceRGBTexture:targetRGBTexture:skinMaskTexture:personMaskTexture:inputYUVOffsets:cropRect:appliedWhitePoint:outputSpatialWhitePointsRBTexture:outputLumaTexture:outputChromaTexture:]"
+ "-[CMISoftwareFlashRenderingStyleTransferV2 finishProcessing]"
+ "-[CMISoftwareFlashRenderingWhiteBalanceAmbientV2 encodeWhiteBalanceAmbientApply:ambientSensorRGBATexture:strobeSensorRGBATexture:ambientWhitePoint:strobeWhitePoint:ambientWhitePointTuned:outputAmbientBalancedRGBTexture:]"
+ "-[CMITiledInferenceProcessorStage getFinalProcessingStatus]"
+ "-[CMITiledInferenceProcessorStage runProcessor:withTileCount:]"
+ "-[CZDemosaicShader initWithMetalContext:]"
+ "-[CZDemosaicStage initWithMetalContext:]"
+ "-[ChromaticAberrationRecovery runCARWithArgs:targetTexture:]"
+ "-[ColorConvertStage _convertColor:lumaPedestal:hazeCorrection:inputLuma:inputChroma:outputLuma:outputChroma:]"
+ "-[ColorConvertStage convertColor:hazeCorrection:inputYCbCr:outputLuma:outputChroma:]"
+ "-[ColorConvertStage extractLinearBufferWithLumaInput:chromaInput:lumaAlignmentFactor:chromaAlignmentFactor:inputIsLinear:removeChromaBias:lumaPedestal:hazeCorrection:exposureParams:ccm:output:]"
+ "-[ColorConvertStage initWithMetalContext:]"
+ "-[ColorConvertStageShared getShaders:]"
+ "-[ColorCubeCorrectionShaders initWithMetal:]"
+ "-[ColorCubeCorrectionStage init:]"
+ "-[ColorCubeCorrectionStage runOnLuma:andChroma:withMask:outChroma:colorCubeFixType:]"
+ "-[ColorCubeCorrectionStage setMaskedSkyCubeVersion:]"
+ "-[DeepFusionDeferredProcessingPlist readBandData:into:]"
+ "-[DeepFusionDeferredProcessingPlist readChromaBoostBandData:into:key:]"
+ "-[DeepFusionDeferredProcessingPlist readDarkEdgeSuppressionBandData:into:]"
+ "-[DeepFusionDeferredProcessingPlist readDesaturationData:into:]"
+ "-[DeepFusionDeferredProcessingPlist readHaloSuppressionBandData:into:]"
+ "-[DeepFusionDeferredProcessingPlist readPlist:]"
+ "-[DeepFusionGaussianPyramid _performGaussianPyramid:inputTex:textureArray:]"
+ "-[DeepFusionGaussianPyramid _validateInputs:inTex:]"
+ "-[DeepFusionGaussianPyramid computeUsing:inTex:]"
+ "-[DeepFusionLaplacianPyramid _performLaplacianPyramid:inputTextures:destinationTextures:upsamplingFilter:]"
+ "-[DeepFusionLaplacianPyramid _validateInputs:gaussianPyramid:]"
+ "-[DeepFusionLaplacianPyramid computeUsing:gaussianPyramid:upsamplingFilter:]"
+ "-[DeepFusionLaplacianPyramid upsampleUsing:inputTex:outputTexUpsampled:upsamplingFilter:]"
+ "-[DeepFusionLaplacianPyramidShared getShaders:]"
+ "-[DeepFusionProcessor _setupPostConfig:isForEnhancedRes:]"
+ "-[DeepFusionProcessor dealloc]"
+ "-[DeepFusionProcessor externalMemoryDescriptorForConfiguration:]"
+ "-[DeepFusionProcessor initWithContext:]"
+ "-[DeepFusionProcessor prewarmWithTuningParameters:]"
+ "-[DeepFusionProcessor printHomography:]"
+ "-[DeepFusionProcessor setFusionMode:]"
+ "-[DeepFusionPyramidBaseClass allocateTextures:]"
+ "-[DeepFusionPyramidBaseClass initWithMetalContext:]"
+ "-[DefringeStage defringePyramid:outputPyramid:chromaScratch:quadraBinningFactor:tuningParameters:]"
+ "-[DenoiseAndSharpeningPlist applyOverrides]"
+ "-[DenoiseAndSharpeningPlist readBandData:]"
+ "-[DenoiseFusePipeline _getPyramidLevel:withWidth:withHeight:]"
+ "-[DenoiseFusePipeline _runInferenceProvider:]"
+ "-[DenoiseFusePipeline addFrame:cfp:processingType:createPyramid:batchCount:]"
+ "-[DenoiseFusePipeline addFrameWithInputLuma:inputChroma:inputYCbCr:cfp:processingType:createPyramid:batchCount:]"
+ "-[DenoiseFusePipeline allocateCoallesedFusionInputPyramidsForWidth:height:levels:frames:]"
+ "-[DenoiseFusePipeline baseLayer:]"
+ "-[DenoiseFusePipeline convertHLGToSDRWithInputPixelBuffer:outputImage:]"
+ "-[DenoiseFusePipeline createPyramidForFrame:cfp:]"
+ "-[DenoiseFusePipeline denoiseSingleImage:linearOutput:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:input:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:]"
+ "-[DenoiseFusePipeline doGainMap:properties:output:outputHeadroom:nrfPlist:useFusedFrame:processingType:]"
+ "-[DenoiseFusePipeline doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:]"
+ "-[DenoiseFusePipeline downsampleUpperBandFrame:sourceFrameIndex:]"
+ "-[DenoiseFusePipeline fuseFramesWithConfig:properties:nrfPlist:batchN:isLastBatch:usePatchBasedFusion:isLowLight:]"
+ "-[DenoiseFusePipeline nrfFusionDenseRegister:ev0FrameIndex:evmProperties:ev0Properties:]"
+ "-[DenoiseFusePipeline startSFDWithInputSampleBuffer:outputImage:tuning:]"
+ "-[DenoiseFusePipelineShared getShaders:]"
+ "-[DenoiseRemixFragmentShader initWithMetal:vertName:fragName:pixelFormat:pixelFormat2:]"
+ "-[DenoiseRemixShaders initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:]"
+ "-[DenoiseRemixStage initWithContext:numPyrLevels:]"
+ "-[DenoiseRemixStage runShader:shader:desc:lumaConfig:chromaConfig:maskTransform:]"
+ "-[DenoiseRemixStage setResourcesWithOutputPyramid:noiseMapPyramid:sharpeningPyramid:localGainMapTex:denoisingOptions:]"
+ "-[DisparityConfig determineDemosaicParameters:inputFrame:bounds:]"
+ "-[DisparityShaders initWithMetalContext:]"
+ "-[DisparityStage initWithMetalContext:staticParameters:]"
+ "-[DisparityStage runWithArgs:]"
+ "-[DisparityStage validateInputFrame:config:]"
+ "-[DisparityStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[FigMetalAllocator setupWithDescriptor:allocatorBackend:] failed"
+ "-[FrameSelectionPlist _setModelWeights:weights:]"
+ "-[FrameSelectionPlist _setModelWeights:weights:]_block_invoke"
+ "-[FrameSelectionPlist readPlist:]"
+ "-[FuseRemixFragmentShader initWithMetal:fragName:pixelFormat:noisePixelFormat:isFirstBatch:isLastBatch:usePatchBasedFusion:useGpuCSC:ggmEnabled:]"
+ "-[FuseRemixShaders initWithMetal:pixelFormatLuma:pixelFormatChroma:]"
+ "-[FusionPlist applyOverrides]"
+ "-[FusionRemixStage computeFusionParams:properties:config:fusionMode:staticScene:isLowLight:]"
+ "-[FusionRemixStage computeGrayGhostCount:ev0Bands:evmProperties:ev0Properties:atBand:nrfPlist:size:]"
+ "-[FusionRemixStage correctGTC:]"
+ "-[FusionRemixStage detectFlicker:ev0Bands:evmProperties:ev0Properties:height:]"
+ "-[FusionRemixStage initBandFusion:nrfConfig:isPrewarm:]"
+ "-[FusionRemixStage prepareForFusion:config:fusedPyramid:properties:nrfPlist:staticScene:isLowLight:]"
+ "-[FusionRemixStage runFusionForBandIndex:config:oldFusedUpTex:oldFusedTex:fusedUpTex:fusedTex:accWeightTex:bandFusionParams:fragmentBufferIndex:processLuma:processTopBand:computeSpecialMap:inputs:simMapTex:confidence:noiseMap:batchN:isFirstBatch:isLastBatch:usePatchBasedFusion:minVarWeightSum:outputChromaBias:ggMaxFusionWeights:]"
+ "-[FusionRemixStage runImageFusion:config:fusedPyramid:accWeightPyramid:buffers:nrfPlist:confidence:batchN:isLastBatch:isLowLight:usePatchBasedFusion:outputChromaBias:]"
+ "-[FusionRemixStage runStationaryFusionWithParams:inputs:fusedLumaTex:fusedChromaTex:noiseMapLumaTex:noiseMapChromaTex:accWeightLumaTex:accWeightChromaTex:inferenceLumaTex:inferenceChromaTex:batchN:]"
+ "-[FusionRemixStage selectNRFFusionReferenceFrame:ev0Bands:evmProperties:ev0Properties:nrfPlist:outputFusionMode:staticScene:motionDetection:grayGhostDetection:]"
+ "-[FusionRemixStageShared getShaders:fp16:]"
+ "-[FusionRemixUniforms initWithMetal:heap:]"
+ "-[GDCConfig getWarpConfigForInputFrame:bounds:warpConfig:]"
+ "-[GDCStage createIntermediateMetalTexture:pixelFormat:width:height:]"
+ "-[GDCStage initWithMetalContext:staticParameters:]"
+ "-[GDCStage runWithArgs:]"
+ "-[GDCStage validateInputFrame:config:]"
+ "-[GDCStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[GainMapShaders initWithMetal:]"
+ "-[GainMapShared getShaders:]"
+ "-[GainMapStage allocateLTMTable:globalLTMCurve:gtcCurve:highlightCompressionCurve:hazeCorrection:texturesWithLTMCurves:HDR:]"
+ "-[GainMapStage computeGainMapWithInput:secondInput:HLGLumaAInput:output:properties:mpconfig:]"
+ "-[GainMapStage convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:]"
+ "-[GainMapStage initWithMetalContext:]"
+ "-[GainMapStage runWithInput:output:minThreshold:maxThreshold:inputIsLinear:inputScaling:]"
+ "-[GainMapStage runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:]"
+ "-[GainMapStage runWithInputDownsampled:output:minThreshold:maxThreshold:inputIsLinear:inputScaling:]"
+ "-[GainMapStage setGainMapConfig:tuning:frameMetadata:width:height:isLinear:hasHDR:]"
+ "-[GainValueArray initWithArray:]"
+ "-[GlobalDistortionCorrectionByPortType initWithDictionary:]"
+ "-[GrayGhostDetection initWithMetalContext:]"
+ "-[GrayGhostDetection runGrayGhostDetection:ev0Bands:evmProperties:ev0Properties:hasChromaBias:atBand:params:]"
+ "-[GrayGhostDetection runGrayGhostDetectionWithRGBEvmTexture:withRGBEv0Texture:evmProperties:ev0Properties:params:]"
+ "-[GrayGhostDetectionShared getShaders:]"
+ "-[GreenGhostBrightLightStage GhostMitigationWithPyr:outputImage:tuning:faceLandMarks:ev0FrameMetadata:roi:gainMap:]"
+ "-[GreenGhostBrightLightStage applyRepairWithLuma:chroma:lumaBase:chromaBase:mask:output:params:gainMap:]"
+ "-[GreenGhostBrightLightStage computeRepairValuesWithLuma:chroma:mask:maskBinary:params:]"
+ "-[GreenGhostBrightLightStage cropLuma:chroma:outputLuma:outputChroma:]"
+ "-[GreenGhostBrightLightStage detectionWithLuma:chroma:outputMask:outputMaskBinary:params:]"
+ "-[GreenGhostBrightLightStage initWithMetalContext:]"
+ "-[GreenGhostBrightLightStage processRepairValues]"
+ "-[GreenGhostBrightLightStage refineMask:outputMask:outputMaskBinary:params:]"
+ "-[GreenGhostBrightLightStage repairPyr:chroma:mask:maskBinary:output:params:gainMap:]"
+ "-[GreenGhostBrightLightStage unCropMaskCropped1:maskCropped2:maskOutput1:maskOutput2:]"
+ "-[GreenGhostCommon blobDetection:output:params:]"
+ "-[GreenGhostCommon boxFilter:withRadius:output:]"
+ "-[GreenGhostCommon brightnessDetectionInput:output:params:processingROIInfo:]"
+ "-[GreenGhostCommon combineBrightnessMask:blobMask:greenMask:output:]"
+ "-[GreenGhostCommon compileDilateVerticalShaders]"
+ "-[GreenGhostCommon detectionWithLuma:croppedLuma:chroma:outputMask:params:processingROIInfo:]"
+ "-[GreenGhostCommon dilateTexture:withNormalizedRadius:withThreshold:subtractTexture:output:]"
+ "-[GreenGhostCommon downscaleInput:output:]"
+ "-[GreenGhostCommon erodeTexture:withNormalizedRadius:output:]"
+ "-[GreenGhostCommon extractFaceBodyBoundariesFromFaceLandMarks:ev0FrameMetadata:imgSize:faceBoundaryPaddingRatio:bodyBoundaryPaddingRatio:output:]"
+ "-[GreenGhostCommon greenDetectionLuma:chroma:output:params:processingROIInfo:]"
+ "-[GreenGhostCommon initWithMetalContext:]"
+ "-[GreenGhostLowLightStage allocateFusionWeightTexturesWithWidth:height:]"
+ "-[GreenGhostLowLightStage applyInpaintWithDownscaledLuma:propagatedLuma:downscaledChroma:propagatedChroma:propagatedGradient:maskPreInpainting:outputLuma:outputChroma:params:]"
+ "-[GreenGhostLowLightStage canMitigationProceedWithMaxMaskAverage:]"
+ "-[GreenGhostLowLightStage computeFusionWeightsRefLuma:refChroma:otherLuma:otherChroma:maskMBBinary:innerMask:relativeBrightness:homography:output:params:]"
+ "-[GreenGhostLowLightStage computeTemporalVariationsRefImg:OtherImg:refProperties:otherProperties:params:]"
+ "-[GreenGhostLowLightStage detectionWithRefPyramid:otherPyramid:refDetection:refProperties:otherProperties:maskMBBinary:params:]"
+ "-[GreenGhostLowLightStage fuseRefPyramid:withOtherPyramid:refProperties:otherProperties:currentFusionWeights:relativeBrightness:]"
+ "-[GreenGhostLowLightStage fuseRefPyramid:withOtherPyramid:refProperties:otherProperties:maskMBBinary:params:]"
+ "-[GreenGhostLowLightStage guidedFilter:withGuideLuma:guideChroma:params:output:]"
+ "-[GreenGhostLowLightStage initWithMetalContext:]"
+ "-[GreenGhostLowLightStage inpaintLuma:andChroma:tuningParams:]"
+ "-[GreenGhostLowLightStage mixFusedTexturesWithRefLuma:refChroma:refProperties:tuningParams:]"
+ "-[GreenGhostLowLightStage prepareFusionRefLuma:refChroma:otherLuma:otherChroma:maskMBBinary:relativeBrightness:homography:output:params:]"
+ "-[GreenGhostLowLightStage prepareInpaintingWithLuma:andChroma:outputLuma:outputChroma:outputGradient:params:]"
+ "-[GreenGhostLowLightStage propagateLuma:chroma:gradient:outputLuma:outputChroma:outputGradient:params:]"
+ "-[GreenGhostLowLightStage refineDetectionWithGuideLuma:guideChroma:params:output:]"
+ "-[GreenGhostLowLightStage releaseTextures]"
+ "-[GreenGhostLowLightStage reset]"
+ "-[GreenGhostLowLightStage updateFusionWeights:]"
+ "-[GreenGhostLowLightStage updateMaskAndComputeGradientForLuma:output:params:]"
+ "-[GuidedFilter createIntermediateTextureWithFormat:width:height:usage:label:]"
+ "-[GuidedFilter encodeToCommandBuffer:inputTexture:guideTexture:outputTexture:kernelRadius:epsilon:]"
+ "-[GuidedFilter initWithMetalContext:]"
+ "-[GuidedFilterShaders initWithMetalContext:]"
+ "-[GuidedFilterShared getShaders:]"
+ "-[H13FastAWB compareAWBComboGains:]"
+ "-[H13FastAWB initWithMetalContext:]"
+ "-[H13FastAWB run:lscGainsTex:hrEnabled:auxEnabled:updatedMetadata:]"
+ "-[H13FastBayerProcConfig(FlareDetection) getFlareCorrectionConfigForInputFrame:flareCorrectionConfig:]"
+ "-[H13FastBayerProcConfig(FlareDetection) updateHOCLBinConfigForFlare:hoclBinConfig:]"
+ "-[H13FastBayerProcConfig(GOC) determineGOCConfigForInputFrame:lscConfig:hrEnabled:awbComputedGains:processingOptions:gocConfig:]"
+ "-[H13FastBayerProcConfig(GOC) determineGOCConfigFromRegistersForInputFrame:lscConfig:hrEnabled:gocConfig:]"
+ "-[H13FastBayerProcConfig(GOC) getGOCConfigForInputFrame:gocConfig:lscConfig:hrEnabled:awbComputedGains:processingOptions:]"
+ "-[H13FastBayerProcConfig(HOCLBin) getHOCLBinConfigForInputFrame:staticParameters:hoclBinConfig:]"
+ "-[H13FastBayerProcConfig(HR) determineHPBLUTFromRegisters:hpbLUT:]"
+ "-[H13FastBayerProcConfig(HR) determineHPPPInBlendLUTFromRegisters:hpppInBlendLUT:]"
+ "-[H13FastBayerProcConfig(HR) determineHRConfigFromInputFrame:bounds:hrConfig:awbComputedGains:]"
+ "-[H13FastBayerProcConfig(HR) determineHRConfigFromRegistersForInputFrame:hrConfig:]"
+ "-[H13FastBayerProcConfig(HR) determineHREnabledForProcessingOptions:hrEnabled:]"
+ "-[H13FastBayerProcConfig(HR) determineHREnabledFromRegisters:hrEnabled:]"
+ "-[H13FastBayerProcConfig(HR) determineInBlendLUTFromRegisters:inBlendLUT:]"
+ "-[H13FastBayerProcConfig(HR) determineMixClipLUTFromInputFrame:mixClipLUT:]"
+ "-[H13FastBayerProcConfig(HR) determineMixClipLUTFromRegisters:mixClipLUT:]"
+ "-[H13FastBayerProcConfig(HR) determineRcvLUTFromRegisters:rcvLUT:]"
+ "-[H13FastBayerProcConfig(HR) determineSoftClipLUTFromInputFrame:hrConfig:softClipLUT:]"
+ "-[H13FastBayerProcConfig(HR) determineSoftClipLUTFromRegisters:softClipLUT:]"
+ "-[H13FastBayerProcConfig(HR) getHRConfigForInputFrame:bounds:awbComputedGains:lscConfig:hrConfig:outputMetadata:]"
+ "-[H13FastBayerProcConfig(HR) getHREnabledForInputFrame:processingOptions:hrEnabled:]"
+ "-[H13FastBayerProcConfig(HR) loadHPBLUTForInputFrame:toTexture:]"
+ "-[H13FastBayerProcConfig(HR) loadHPPPInBlendLUTForInputFrame:toTexture:]"
+ "-[H13FastBayerProcConfig(HR) loadInBlendLUTForInputFrame:hrConfig:toTexture:]"
+ "-[H13FastBayerProcConfig(HR) loadMixClipLUTForInputFrame:toTexture:]"
+ "-[H13FastBayerProcConfig(HR) loadRcvLUTForInputFrame:hrConfig:toTexture:]"
+ "-[H13FastBayerProcConfig(HR) loadSoftClipLUTForInputFrame:hrConfig:toTexture:]"
+ "-[H13FastBayerProcConfig(HRD) checkSymmetricalFiltersForConfig:]"
+ "-[H13FastBayerProcConfig(HRD) generateHRDConfigForInputFrame:processingOptions:hrdConfig:overwriteSubGnuforFlare:]"
+ "-[H13FastBayerProcConfig(HRD) generateHRDConfigFromRegistersForInputFrame:hrdConfig:]"
+ "-[H13FastBayerProcConfig(HRD) generateHRDEnabledFromRegistersDict:hrdEnabled:]"
+ "-[H13FastBayerProcConfig(HRD) getHRDConfigForInputFrame:processingOptions:hrdConfig:overwriteSubGnuforFlare:]"
+ "-[H13FastBayerProcConfig(HRD) getHRDEnabledForInputFrame:hrdEnabled:]"
+ "-[H13FastBayerProcConfig(Huemap) getFrontEndConfigForInputFrame:bounds:frontEndThumbnailConfig:gocConfig:]"
+ "-[H13FastBayerProcConfig(Huemap) getHuemapConfigForInputFrame:huemapConfig:gocConfig:]"
+ "-[H13FastBayerProcConfig(Huemap) getHuemapFepConfigForInputFrame:huemapFepConfig:gocConfig:]"
+ "-[H13FastBayerProcConfig(Huemap) getHuemapMotionCompensationConfigForInputFrame:huemapMotionCompensationConfig:]"
+ "-[H13FastBayerProcConfig(Huemap) getMotionCompensationEnabledForInputFrame:mcEnabled:]"
+ "-[H13FastBayerProcConfig(Huemap) getSyntheticConfigForInputFrame:syntheticThumbnailConfig:lscConfig:awbGains:isQuadra:]"
+ "-[H13FastBayerProcConfig(RNF) getRNFConfigForInputFrame:bounds:processingOptions:rnfConfig:]"
+ "-[H13FastBayerProcShaders initWithMetalContext:]"
+ "-[H13FastBayerProcStage auxiliaryPixelFormatForAuxiliaryType:inputPixelFormat:outputCompressionLevel:]"
+ "-[H13FastBayerProcStage initWithMetalContext:staticParameters:]"
+ "-[H13FastBayerProcStage prepareLSCMetadata:withArgs:forAWB:]"
+ "-[H13FastBayerProcStage processPreHRWithConfig:inputTex:outputTex:lscMetadata:hrEnabled:wbgEnabled:lscEnabled:outputFrame:awbComputedGains:]"
+ "-[H13FastBayerProcStage runAWBWithArgs:awbComputedGOCGains:updatedMetadata:lscGainsTex:inputTex:auxEnabled:hrEnabled:]"
+ "-[H13FastBayerProcStage runWithArgs:]"
+ "-[H13FastBayerProcStage validateInputFrame:config:]"
+ "-[H13FastBayerProcStage(DraftDemosaic) _getWarpConfigForInputFrame:bounds:warpConfig:]"
+ "-[H13FastBayerProcStage(DraftDemosaic) _shouldApplyGDC:]"
+ "-[H13FastBayerProcStage(DraftDemosaic) runDraftDemosaicWithArgs:inputTexture:outputFrame:outputMetadata:isQuadra:]"
+ "-[H13FastBayerProcStage(FlareDetection) runFlareDetectionWithConfig:inputTex:flareDetectionConfig:lscMetadata:outputMetadata:]"
+ "-[H13FastBayerProcStage(HOCLBin) runHOCLBinWithArgs:hoclBinConfig:hoclBinConfigForFlareCorrection:inputTexture:]"
+ "-[H13FastBayerProcStage(HR) dispatchHRCreateHuemapThumbnailsWithInputTexture:outputTexture:config:args:]"
+ "-[H13FastBayerProcStage(HR) dispatchHRDGnuCorrectionWithInputTexture:outputTextures:lscMetadata:config:hrdConfigForFlareCorrection:args:isQuadra:gnuEnabled:]"
+ "-[H13FastBayerProcStage(HR) dispatchHRDRedBlueFilterWithTextures:config:args:isQuadra:]"
+ "-[H13FastBayerProcStage(HR) dispatchHRPreprocessDSLUTWithInputTexture:outputTexture:config:args:]"
+ "-[H13FastBayerProcStage(HR) dispatchHRWithInputTextures:outputTexture:hrdConfig:hrConfig:args:isQuadra:]"
+ "-[H13FastBayerProcStage(HR) runHRWithInputTextures:outputTexture:outputMetadata:isFinalOutput:isQuadra:runHR:args:lscMetadata:awbComputedGains:hrdConfigForFlareCorrection:]"
+ "-[H13FastBayerProcStage(Huemap) createThumbnailTextureArray:width:height:]"
+ "-[H13FastBayerProcStage(Huemap) dispatchHuemapGenerationInputTexture:outputTexture:config:args:isQuadra:]"
+ "-[H13FastBayerProcStage(Huemap) dispatchHuemapMotionCompensationWithSifr:ev0:outputTexture:config:args:lscMetadata:]"
+ "-[H13FastBayerProcStage(Huemap) dispatchHuemapWithInputTexture:outputTexture:config:args:lscMetadata:]"
+ "-[H13FastBayerProcStage(Huemap) runHuemapGenerateInputThumbnailWithInputTexture:outputTexture:lscConfig:isSifr:args:awbComputedGains:isQuadra:]"
+ "-[H13FastBayerProcStage(Huemap) runHuemapGenerationWithInputTexture:outputTexture:lscConfig:args:awbComputedGains:lscMetadata:applyLscToThumbnailsIfNecessary:]"
+ "-[H13FastBayerProcStage(Huemap) runHuemapMotionCompensationWithSifrTexture:ev0ThumbnailTexture:outputTexture:args:lscMetadata:]"
+ "-[H13FastBayerProcStage(SSC) initSSC]"
+ "-[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:]"
+ "-[H13FastBayerProcStage(SSC) runSSCWithArgs:inputTexture:outputMetadata:firstPixel:isQuadra:]_block_invoke_3"
+ "-[H13FastBayerProcStage(SSC) sharpnessScoreInstance]"
+ "-[H13FastBayerProcStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[H13FastCanvasShaders initWithMetalContext:]"
+ "-[H13FastCanvasStage createIntermediateMetalDeviceTexture:withPixelFormat:width:height:]"
+ "-[H13FastCanvasStage initWithMetalContext:staticParameters:]"
+ "-[H13FastCanvasStage runWithArgs:]"
+ "-[H13FastCanvasStage validateInputFrame:config:]"
+ "-[H13FastCanvasStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[H13FastCanvasStageMetal encodeWithCanvasQueueRGB:inputTex:outputTex:]"
+ "-[H13FastCanvasStageMetal encodeWithCanvasQueueYUV:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:]"
+ "-[H13FastCanvasStageMetal initWithMetalContext:]"
+ "-[H13FastDemosaicConfig(Demosaic) getDemosaicConfigForInputFrame:demosaicConfig:]"
+ "-[H13FastDemosaicConfigMetal(Demosaic) getDemosaicConfigForInputFrameMetadata:cameraInfoByPortType:applyCCM:zeroBias:demosaicConfig:]"
+ "-[H13FastDemosaicConfigMetal(Demosaic) getQDEMNoiseSuppressionLUT:adaptiveGradPushDLUT:adaptiveGradPushHVLUT:qdemConfig:]"
+ "-[H13FastDemosaicShaders initWithMetalContext:]"
+ "-[H13FastDemosaicStage createIntermediateMetalTexture:pixelFormat:width:height:]"
+ "-[H13FastDemosaicStage initWithMetalContext:staticParameters:outputGammaEncoded:]"
+ "-[H13FastDemosaicStage runWithArgs:]"
+ "-[H13FastDemosaicStage validateInputFrame:config:]"
+ "-[H13FastDemosaicStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[H13FastDemosaicStageMetal convertRGBToYUV:demosaicConfig:outputTexY:outputTexUV:commandBuffer:]"
+ "-[H13FastDemosaicStageMetal convertRGBToYUV:inputMetadata:zeroBias:cameraInfoByPortType:outputTexY:outputTexUV:]"
+ "-[H13FastDemosaicStageMetal createIntermediateMetalTexture:pixelFormat:width:height:]"
+ "-[H13FastDemosaicStageMetal initWithMetalContext:]"
+ "-[H13FastDemosaicStageMetal runQuadraWithInputTex:demosaicConfig:outputRGBATex:outputLumaTex:outputChromaTex:outputRGB:outputSize:commandBuffer:]"
+ "-[H13FastDemosaicStageMetal runWithInputTex:demosaicConfig:outputRGBATex:outputSize:]"
+ "-[H13FastDemosaicStageMetal runWithInputTex:demosaicConfig:outputSize:outputTexY:outputTexUV:commandBuffer:]"
+ "-[H13FastDemosaicStageMetal runWithInputTex:inputCropRect:inputMetadata:firstPix:zeroBias:cfaLayout:cameraInfoByPortType:outputRGBATex:outputCropRect:]"
+ "-[H13FastLTMConfig getLTMSettingsForInputFrame:]"
+ "-[H13FastLTMShaders initWithMetalContext:]"
+ "-[H13FastLTMStage createIntermediateRGBAMetalTexture:width:height:]"
+ "-[H13FastLTMStage initWithMetalContext:staticParameters:error:]"
+ "-[H13FastLTMStage runWithArgs:]"
+ "-[H13FastLTMStage validateInputFrame:config:]"
+ "-[H13FastLTMStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[H13FastLumaSharpeningConfig getLumaSharpeningConfigForInputFrame:lumaSharpeningConfig:]"
+ "-[H13FastLumaSharpeningShaders initWithMetalContext:]"
+ "-[H13FastLumaSharpeningStage createIntermediateMetalDeviceTexture:withPixelFormat:width:height:]"
+ "-[H13FastLumaSharpeningStage initWithMetalContext:staticParameters:]"
+ "-[H13FastLumaSharpeningStage runWithArgs:]"
+ "-[H13FastLumaSharpeningStage validateInputFrame:config:]"
+ "-[H13FastLumaSharpeningStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[H13FastLumaSharpeningStageMetal encodeWithConfig:inputTex:outputTex:isRGB:allowUnclampedOutputs:sourceSize:destOrigin:]"
+ "-[H13FastLumaSharpeningStageMetal initWithMetalContext:]"
+ "-[H13FastOutlierPixelCorrectionConfig getOutlierPixelCorrectionConfig:forInputFrame:]"
+ "-[H13FastOutlierPixelCorrectionShaders initWithMetalContext:]"
+ "-[H13FastOutlierPixelCorrectionStage createIntermediateMetalTexture:pixelFormat:width:height:compressed:]"
+ "-[H13FastOutlierPixelCorrectionStage initWithMetalContext:staticParameters:]"
+ "-[H13FastOutlierPixelCorrectionStage runWithArgs:]"
+ "-[H13FastOutlierPixelCorrectionStage validateInputFrame:config:]"
+ "-[H13FastOutlierPixelCorrectionStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[H13FastOutlierPixelCorrectionStageMetal initWithMetalContext:]"
+ "-[H13FastOutlierPixelCorrectionStageMetal runWithConfig:inputTex:outputTex:]"
+ "-[H13FastPostDemosaicProcConfig(PostDemosaic) getPostDemosaicProcConfigForInputFrame:postDemosaicProcConfig:chromaSuppressionConfig:]"
+ "-[H13FastPostDemosaicProcMetal createIntermediateMetalTexture:pixelFormat:width:height:]"
+ "-[H13FastPostDemosaicProcMetal initWithMetalContext:]"
+ "-[H13FastPostDemosaicProcMetal runWithInputLumaTex:inputChromaTex:postDemosaicProcConfig:chromaSuppressionConfig:outputSize:outputLumaTex:outputChromaTex:commandBuffer:outputFrame:isQuadra:]"
+ "-[H13FastPostDemosaicProcMetal runWithTextureArray:inputCropRect:inputMetadata:controls:outputCropRect:blacklevel:]"
+ "-[H13FastPostDemosaicProcMetal runWithTextureArray:postDemosaicProcConfig:chromaSupressionConfig:outputSize:]"
+ "-[H13FastPostDemosaicProcShaders initWithMetalContext:]"
+ "-[H13FastPostDemosaicProcStage createIntermediateMetalTexture:pixelFormat:width:height:]"
+ "-[H13FastPostDemosaicProcStage initWithMetalContext:staticParameters:]"
+ "-[H13FastPostDemosaicProcStage runWithArgs:]"
+ "-[H13FastPostDemosaicProcStage validateInputFrame:config:]"
+ "-[H13FastPostDemosaicProcStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) getBayerMBNRSettingsForInputFrame:rawMBNRConfig:totalGain:band:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) getChromaMBNRSettingsForInputFrame:rawMBNRConfig:totalGain:band:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) getEnabledForInputFrame:isEnabled:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) getLSCGainsForInputFrame:lscGridSize:lscGainsTex:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) getLSCGridDimensions:portType:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) getMBNRSettingsForInputFrame:rawMBNRConfig:totalGain:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) getNoiseModelForInputFrame:outputFrame:noiseConfig:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) getRawMBNRConfigForInputFrame:bounds:lscGainMapParameters:rawMBNRConfig:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) updateNoiseModelForInputFrame:noiseConfig:totalGain:band:]"
+ "-[H13FastRawMBNRConfig(RawMBNR) updateRawMBNRConfigForInputFrame:bounds:band:rawMBNRConfig:]"
+ "-[H13FastRawMBNRShaders initWithMetalContext:]"
+ "-[H13FastRawMBNRStage bypassRawMBNRWithArgs:]"
+ "-[H13FastRawMBNRStage bytesRequiredForConfig:]"
+ "-[H13FastRawMBNRStage createIntermediateMetalDeviceTexture:withPixelFormat:width:height:]"
+ "-[H13FastRawMBNRStage createIntermediateMetalTexture:withPixelFormat:width:height:]"
+ "-[H13FastRawMBNRStage generatePyramidFromTexture:outputPyramid:startLevel:numLevels:pyramidName:]"
+ "-[H13FastRawMBNRStage getNoiseMapForInputTexture:bayerNoise:inputFrame:outputFrame:bounds:h13FastConfig:lscGainsTex:]"
+ "-[H13FastRawMBNRStage initWithMetalContext:staticParameters:]"
+ "-[H13FastRawMBNRStage runRawMBNROnInputTexture:outputTexture:bayerNoise:inputFrame:outputFrame:bounds:h13FastConfig:lscGainsTex:]"
+ "-[H13FastRawMBNRStage runWithArgs:]"
+ "-[H13FastRawMBNRStage validateInputFrame:config:]"
+ "-[H13FastRawMBNRStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[H13FastRawScaleConfig(ABLEST) getABLESTConfigForInputFrame:pdpConfig:ablestConfig:]"
+ "-[H13FastRawScaleConfig(ABLEST) getABLESTEnabledForInputFrame:enabled:]"
+ "-[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationConfigForInputFrame:pdpConfig:blackLevelEstimationConfig:]"
+ "-[H13FastRawScaleConfig(BlackLevelEstimation) getBlackLevelEstimationEnabledForInputFrame:enabled:]"
+ "-[H13FastRawScaleConfig(BlackLevelShading) getBlackLevelShadingConfigForInputFrame:blackLevelShadingConfig:]"
+ "-[H13FastRawScaleConfig(BlackLevelShading) getBlackLevelShadingCorrectionTextureForInputFrame:]"
+ "-[H13FastRawScaleConfig(DMA) getDMAInputConfigForInputFrame:dmaInputConfig:]"
+ "-[H13FastRawScaleConfig(GOC) generateGOCConfigFromInputFrameMetadata:toGocConfig:]"
+ "-[H13FastRawScaleConfig(GOC) getBLCGOCConfigForInputFrame:gocConfig:]"
+ "-[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:]"
+ "-[H13FastRawScaleConfig(HazeCorrection) getHazeCorrectionEnabledForInputFrame:enabled:]"
+ "-[H13FastRawScaleConfig(PDC) _createDetectionLutTexsWithArgs:metalCtx:]"
+ "-[H13FastRawScaleConfig(PDC) _createFlatLUTTexWithData:lutSize:metalCtx:destArgs:]"
+ "-[H13FastRawScaleConfig(PDC) _createQuadraStaticDefectTableWithLocations:defectLocationCount:metalCtx:destArgs:]"
+ "-[H13FastRawScaleConfig(PDC) _createStaticDefectTableWithLocations:defectLocationCount:metalCtx:destArgs:inputFrame:]"
+ "-[H13FastRawScaleConfig(PDC) _createXtalkTexWithData:metalCtx:pdcArgs:pdcXtalkConfig:neighborCount:]"
+ "-[H13FastRawScaleConfig(PDC) _fillProcessFocusPixelsConfigWithPDPConfig:args:gainAdj:]"
+ "-[H13FastRawScaleConfig(PDC) _filterStaticDefectTableWithLocations:defectLocationCount:fromDefectLocations:defectLocationCountToRemove:outputFilteredDefectLocations:filteredDefectLocationCount:]"
+ "-[H13FastRawScaleConfig(PDC) configureFromMetadataPDCArgs:forInputFrame:forOutputFrame:metalCtx:pdpConfig:bounds:]"
+ "-[H13FastRawScaleConfig(PDC) configureFromRegistersPDCArgs:forInputFrame:metalCtx:pdpConfig:]"
+ "-[H13FastRawScaleConfig(PDP) generatePDPConfigFromInputFrameMetadata:bounds:toPdpConfig:]"
+ "-[H13FastRawScaleConfig(PDP) getPDPConfigForInputFrame:bounds:pdpConfig:]"
+ "-[H13FastRawScaleConfig(PDP) getPDPGainsForInputFrame:pdpGainsTex:]"
+ "-[H13FastRawScaleConfig(RFPN) getRFPNConfigForInputFrame:rFPNConfig:]"
+ "-[H13FastRawScaleConfig(ShadingFPNR) getShadingFPNCorrectionTextureForInputFrame:]"
+ "-[H13FastRawScaleConfig(ShadingFPNR) getShadingFPNRConfigForInputFrame:shadingFPNRConfig:]"
+ "-[H13FastRawScaleConfig(SyntheticThumbnail) getSyntheticThumbnailConfigForInputFrame:bounds:syntheticThumbnailConfig:]"
+ "-[H13FastRawScaleShaders initWithMetalContext:]"
+ "-[H13FastRawScaleStage createIntermediate1DMetalTexture:pixelFormat:length:]"
+ "-[H13FastRawScaleStage createIntermediateMetalTexture:pixelFormat:width:height:]"
+ "-[H13FastRawScaleStage initWithMetalContext:staticParameters:]"
+ "-[H13FastRawScaleStage runWithArgs:]"
+ "-[H13FastRawScaleStage validateInputFrame:config:]"
+ "-[H13FastRawScaleStage(ABLEST) runABLESTWithConfig:inOutTexture:]"
+ "-[H13FastRawScaleStage(FPExtract) _extractFocusPixelsForAuxType:config:inputTexture:arguments:]"
+ "-[H13FastRawScaleStage(FPExtract) copySashimiTextureToAuxiliaryWithConfig:inputTexture:]"
+ "-[H13FastRawScaleStage(FPExtract) runFPExtractWithConfig:inputTexture:]"
+ "-[H13FastRawScaleStage(HazeCorrection) runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:]"
+ "-[H13FastRawScaleStage(PDC) runPDCWithArgs:inputTex:outputTex:]"
+ "-[H13FastRawScaleStage(PDC) runQuadraPDCWithArgs:inputTex:outputTex:]"
+ "-[H13FastRawScaleStage(SyntheticThumbnail) runSyntheticThumbnailWithSensorDecodedTexture:thumbnailTexture:syntheticThumbnailConfig:processFocusPixelsConfig:quadraFPGrid:isQuadra:]"
+ "-[H13FastRawScaleStage(Vision) getConfigFromInputFrame:config:]"
+ "-[H13FastRawScaleStage(Vision) preparePixelBuffer:forRegion:ofImage:withOutputFrame:config:]"
+ "-[H13FastRawScaleStage(Vision) runFaceDetectionOnPixelBuffer:withMetadataToUpdate:config:pts:]_block_invoke"
+ "-[H13FastRawScaleStage(Vision) runVisionWithArgs:inputTex:metadataToUpdate:]"
+ "-[H13FastRawScaleStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[H13UtilityConvertConfig getConfigForInputFrame:outputFrame:config:]"
+ "-[H13UtilityConvertConfig initWithStaticParameters:prepareDescriptor:inputPixelFormat:outputPixelFormat:outputCompressionLevel:]"
+ "-[H13UtilityConvertShaders initWithMetalContext:inputPixelFormat:outputPixelFormat:]"
+ "-[H13UtilityConvertStage createIntermediateMetalTexture:width:height:pixelFormat:]"
+ "-[H13UtilityConvertStage initWithMetalContext:staticParameters:inputPixelFormat:outputPixelFormat:]"
+ "-[H13UtilityConvertStage outputPixelFormatForInputPixelFormat:outputCompressionLevel:]"
+ "-[H13UtilityConvertStage runConvertFromTex:outputTexture:args:config:outputOffset:]"
+ "-[H13UtilityConvertStage runWithArgs:]"
+ "-[H13UtilityConvertStage validateInputFrame:config:]"
+ "-[H13UtilityConvertStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[LSCGainsPlist getTextureMaxValueForPortType:]"
+ "-[LSCGainsPlist initWithDictionary:metal:]"
+ "-[LearnedNRBoundInferenceResults initWithResult:andMetal:]"
+ "-[LearnedNRMetalStage _bindYuvBuffer:toLumaTexture:chromaTexture:withUsage:]"
+ "-[LearnedNRMetalStage _estimateGainFromMetadata:considerHighlightCompression:]"
+ "-[LearnedNRMetalStage clearBuffer:]"
+ "-[LearnedNRMetalStage createRawTile:fromInputRaw:tileStart:cmdBuffer:]"
+ "-[LearnedNRMetalStage createRawTile:fromInputYuv:tileStart:cmdBuffer:]"
+ "-[LearnedNRMetalStage initWithCommandQueue:cameraInfo:tuningParameters:isQuadra:]"
+ "-[LearnedNRMetalStage updateParametersFromMetadata:lscSampleBuffer:]"
+ "-[LearnedNRMetalStage writeRgbTile:toYuvBuffer:intermediateLumaBuffer:intermediateDeltaBuffer:origRawInputBuffer:srcStart:dstStart:size:cmdBuffer:]"
+ "-[LearnedNRMetalStage writeRgbTile:toYuvBuffer:intermediateLumaBuffer:intermediateDeltaBuffer:origYuvInputBuffer:srcStart:dstStart:size:cmdBuffer:]"
+ "-[LearnedNRNetworkStage initWithContext:cameraInfo:config:]"
+ "-[LearnedNRNetworkStage updateParametersFromMetadata:outputGain:bayerPattern:lscGainMapBuffer:lscGainMapParameters:]"
+ "-[LearnedNRProcessor _prepareOutputMetadata:]"
+ "-[LearnedNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:]"
+ "-[LearnedNRProcessor addFrame:]"
+ "-[LearnedNRProcessor addInputResource:]"
+ "-[LearnedNRProcessor bindResourcesForProcessingType:prepareDescriptor:]"
+ "-[LearnedNRProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:]"
+ "-[LearnedNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:]"
+ "-[LearnedNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:]"
+ "-[LearnedNRProcessor generateGainMapIfNeeded]"
+ "-[LearnedNRProcessor initWithCommandQueue:]"
+ "-[LearnedNRProcessor prepareBand1InputWithBand0:]"
+ "-[LearnedNRProcessor prepareToProcess:]"
+ "-[LearnedNRProcessor prepareToProcess:prepareDescriptor:]"
+ "-[LearnedNRProcessor prewarm]"
+ "-[LearnedNRProcessor process]"
+ "-[LearnedNRProcessor resetState]"
+ "-[LearnedNRProcessor runDemosaicWithInputRawTex:outputImage:frame:]"
+ "-[LearnedNRProcessor runPipeline]"
+ "-[LearnedNRProcessor runSemanticInferences]"
+ "-[LearnedNRProcessor setLinearOutputMetadata:]"
+ "-[LearnedNRProcessor setOutput:]"
+ "-[LearnedNRProcessor setReferenceFrameIndex:]"
+ "-[LearnedNRProcessor setupWithOptions:nrfConfig:]"
+ "-[LearnedNRProcessor supportsInputPixelFormat:]"
+ "-[LearnedNRProcessor(Tuning) prepareTuning:]"
+ "-[LearnedNRTuningParams readPlist:]"
+ "-[LocalToneMappingConfig getLocalToneCurveDimsForOutputFrame:width:height:lumaEntries:]"
+ "-[LocalToneMappingConfig getToneMappingConfigForInputFrame:outputFrame:bounds:config:localCurves:globalLumaCurve:perComponentCurve:]"
+ "-[LocalToneMappingStage configForPrepareDescriptor:outputCompressionLevel:]"
+ "-[LocalToneMappingStage createDeviceMetalTexture:textureType:pixelFormat:width:height:depth:]"
+ "-[LocalToneMappingStage createIntermediateMetalTexture:pixelFormat:width:height:]"
+ "-[LocalToneMappingStage runWithArgs:]"
+ "-[LocalToneMappingStage validateInputFrame:config:]"
+ "-[LocalToneMappingStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[LumaChromaImage bindYCbCrTexture:alignmentFactor:]"
+ "-[LumaChromaImage initWithContext:pixelBuffer:lumaAlignmentFactor:chromaAlignmentFactor:]"
+ "-[MIWB _configForMiwbV2:miwbInputHasCCMApplied:]"
+ "-[MIWB allocInternalResources]"
+ "-[MIWB canRunMIWB:]"
+ "-[MIWB interpolateLinear1D:samples:nSamples:]"
+ "-[MIWB runWithInLinearLumaTex:inLinearChromaTex:inSkyMaskTex:inSkinMaskTex:inHazeCorrection:outLinearLumaTex:outLinearChromaTex:]"
+ "-[MIWB setupWithOptions:]"
+ "-[MIWBModuleConfigPlist readModuleConfigPlist:]"
+ "-[MSTMv2Plist readPlist:]"
+ "-[MSTMv3BandData readPlist:]"
+ "-[MSTMv3Plist readPlist:]"
+ "-[MotionDetection initWithMetalContext:]"
+ "-[MotionDetection startMotionDetectionWithParams:evm:ev0:evmProperties:ev0Properties:evmHomography:ev0Homography:useFullImage:]"
+ "-[MotionDetectionShared getShaders:]"
+ "-[NRFBackgroundLearnedNR initWithContext:cameraInfo:config:]"
+ "-[NRFCompletionStatus init]"
+ "-[NRFConcurrentProcessing _forkBackgroundCommandQueue]"
+ "-[NRFConcurrentProcessing _joinBackgroundCommandQueue]"
+ "-[NRFConcurrentProcessing _signalBackgroundComplete]"
+ "-[NRFConfig initWithDefaults:]"
+ "-[NRFMonitor addInstance]"
+ "-[NRFMonitor releaseAllNRFSingletons]"
+ "-[NRFMonitor removeInstance]"
+ "-[NRFPrepareDescriptor init]"
+ "-[NRFProcessorV4 allocateResources:]"
+ "-[NRFProcessorV4 determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:]"
+ "-[NRFProcessorV4 externalMemoryDescriptorForConfiguration:]"
+ "-[NRFProcessorV4 getOptions:]"
+ "-[NRFProcessorV4 initWithCommandQueue:subProcessorType:]"
+ "-[NRFProcessorV4 prepareToProcess:]"
+ "-[NRFProcessorV4 prepareToProcess:prepareDescriptor:]"
+ "-[NRFProcessorV4 prewarm]"
+ "-[NRFProcessorV4 processingTypeToSubProcessorType:]"
+ "-[NRFProcessorV4 resetState]"
+ "-[NRFProcessorV4 setOutput:]"
+ "-[NRFProcessorV4 setupWithOptions:]"
+ "-[NRFProgressiveBracketingParameters _preprocessAEThumbnailFromStatistics:bitMask:bitShift:processedThumbnail:]"
+ "-[NRFProgressiveBracketingParameters _selectBracketsAndComputeExposureTimeWithOption:statistics:getAllInfo:updateDecision:minTotalExposureTime:]"
+ "-[NRFProgressiveBracketingParameters computeTotalIntegrationTimeWithStatistics:forMode:]"
+ "-[NRFProgressiveBracketingParameters currentBracketingParametersForGroup:]"
+ "-[NRFRawNightModeOutputFrame addCompletionHandlerToCommandBuffer:]"
+ "-[NRFRawNightModeOutputFrame bindTexturesForConfig:metalContext:]"
+ "-[OutliersRemovalShaders initWithMetal:]"
+ "-[OutliersRemovalShared getShaders:]"
+ "-[OutliersRemovalStage initWithMetalContext:]"
+ "-[OutliersRemovalStage runWithInput:output:gamma:]"
+ "-[OutputNoiseModelPlist readPlist:]"
+ "-[PatchBasedFusionParametersLUTs readPlist:]"
+ "-[PostDemosaicTuningParams readPlist:]"
+ "-[PostDemosaicTuningParams updateConfigWithGain:]"
+ "-[PyramidStage initWithOptions:context:]"
+ "-[PyramidStage runGPUWithFilters:doShift:pyramid:]"
+ "-[PyramidStage runM2MWithFilters:pyramid:]"
+ "-[PyramidStage runWithFilters:pyramid:]"
+ "-[PyramidStageShared getRec709DownsamplePipelineState:kernelType:]"
+ "-[PyramidStorage clearLevel:]"
+ "-[PyramidStorage setLumaTexture:chromaTexture:level:metal:]"
+ "-[PyramidStorage setLumaTexture:level:]"
+ "-[PyramidStorage setPixelBuffer:level:texUsage:metal:alignDims:]"
+ "-[PyramidStorage setPixelBufferFloat16:chromaBuffer:level:metal:]"
+ "-[QDEMTuningParams readPlist:]"
+ "-[QuadraBinConfig initWithStaticParameters:prepareDescriptor:outputCompressionLevel:downstreamStage:]"
+ "-[QuadraBinShaders initWithMetalContext:]"
+ "-[QuadraBinStage auxiliaryPixelFormatForAuxiliaryType:inputPixelFormat:outputCompressionLevel:]"
+ "-[QuadraBinStage bytesRequiredForConfig:]"
+ "-[QuadraBinStage createIntermediateMetalTexture:pixelFormat:width:height:]"
+ "-[QuadraBinStage initWithDownstreamStage:metalContext:staticParameters:]"
+ "-[QuadraBinStage runWithArgs:]"
+ "-[QuadraBinStage validateInputFrame:config:]"
+ "-[QuadraBinStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[RawDFDetectors getDetectorsResultsSync:]"
+ "-[RawDFDetectors getMotionDetectionSyncResult:]"
+ "-[RawDFDetectors initWithMetalContext:]"
+ "-[RawDFDetectors runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:]"
+ "-[RawDFDetectors runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:]"
+ "-[RawDFFlickerDetectorStage detectFlickerWithEVMLuma:withEV0Luma:evmProperties:ev0Properties:]"
+ "-[RawDFProcessor _processSIFRandRefEV0IfPossible:]"
+ "-[RawDFProcessor _setupFusionConfig]"
+ "-[RawDFProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:]"
+ "-[RawDFProcessor prepareToProcess:]"
+ "-[RawDFProcessor prewarm]"
+ "-[RawDFProcessor resetState]"
+ "-[RawDFProcessor setFusionMode:]"
+ "-[RawDFProcessor setOutput:]"
+ "-[RawDFProcessor setSharedRegWarpBuffer:]"
+ "-[RawDFProcessor(Tuning) prepareTuning:processingTypes:]"
+ "-[RawDFSynRefDSR initWithShaders:name:group:evmPyramid:ev0Pyramid:lscGainsTex:]"
+ "-[RawDFSynRefDSR prepareWithFrameProperties:srPlist:]"
+ "-[RawDFSynRefDSRPass initWithShaders:lscGainsTex:name:group:band:topBand:]"
+ "-[RawDFSynRefDSRPass prepareWithFrameProperties:srPlist:]"
+ "-[RawDFSynRefDSRPass render:]"
+ "-[RawDFSynRefHR initWithShaders:name:group:]"
+ "-[RawDFSynRefHR render:]"
+ "-[RawDFSyntheticReferenceShadersCRG initWithMetal:]"
+ "-[RawDFSyntheticReferenceStage fillFrameProperties:withEvmProperties:withEv0Properties:]"
+ "-[RawDFSyntheticReferenceStageCRG fillFrameProperties:withEvmProperties:withEv0Properties:]"
+ "-[RawDFSyntheticReferenceStageCRG genereteSyntheticReference:noiseDivisorOutputTex:mode:lscGainsTex:evmPyramid:ev0Pyramid:frameProperties:tuning:]"
+ "-[RawDFSyntheticReferenceStageCRG initWithMetalContext:]"
+ "-[RawNMReferenceFrameSelector initWithMetal:]"
+ "-[RawNMReferenceFrameSelector legacyAnalyseNewFrame:frameIndex:]"
+ "-[RawNightModeBatch populateInferenceInputs:first:last:]"
+ "-[RawNightModeConfig validateInputFrame:]"
+ "-[RawNightModeConfig validateOutputFrame:]"
+ "-[RawNightModeDenoiseInference initWithMetalContext:isQuadra:isBarrington:isArgyleTripodMax:]"
+ "-[RawNightModeDenoiseInference runInferenceWithInferenceData:]"
+ "-[RawNightModeDenoiseMetalStage createNetworkInputTile:fromInputRgbImage:fromNoiseMap:withLSCGainsMap:tileStart:encodeToContext:]"
+ "-[RawNightModeDenoiseMetalStage generateAddbackClippingMapPyr:outputClippingMapTex:tileCoordOffset:fullCoordOffset:outputTileSize:addbackModulationParams:withCommandBuffer:metalContext:]"
+ "-[RawNightModeDenoiseMetalStage getHighlightSmoothingParametersFrom:fromGain:highlightSmoothingParameters:]"
+ "-[RawNightModeDenoiseMetalStage getNoiseMapScalingFrom:fromGain:noiseMapScaling:]"
+ "-[RawNightModeDenoiseMetalStage initWithCommandQueue:]"
+ "-[RawNightModeDenoiseMetalStage updateParametersFromMetadata:cameraInfoByPortType:tuningParameters:lscGainMapParameters:firstPix:aeTargetGain:isQuadra:]"
+ "-[RawNightModeDenoiseMetalStage writeDenoisedRgbTile:withDenoisedLumaPyrBands:withNoisyLumaPyrBands:withLumaAddbackPyrBands:withSnrMapPyrBands:withSkyMaskPyrBands:withSkinMaskPyrBands:withBodyMaskPyrBands:withAddbackClippingPyrBands:withLocalDNRBiasPyrBands:withNoisyRgbImage:withNoiseMap:withLSCGainsMap:withSkyMask:withPersonMask:withSkinMask:withHairMask:withOPCTexture:withDnrBiasBuffer:toOutputLuma:toOutputChroma:toOutputClippingMap:toOutputBand3DenoisedLumaMap:toOutputLocalBiasMap:tileCoordOffset:fullCoordOffset:outputTileSize:tileIndex:encodeToContext:]"
+ "-[RawNightModeFusionInference getFusionParams:withTuningParameters:gain:]"
+ "-[RawNightModeFusionInference initWithMetalContext:isQuadra:isBarrington:requiresDarkCurrentNoiseModel:]"
+ "-[RawNightModeFusionInferenceData init]"
+ "-[RawNightModeFusionInferencePyramid init]"
+ "-[RawNightModeFusionMetalStage fuseInputFramesTile:withGGMaxFusionWeights:withGreenGhostThreshold:withInputWeightPyramidTile:withInputAccPyramid:withFramePyramidTile:withAccumPyramidTile:withClippingMaskPyrTexArray:withScratchPyrTexArray:toScratchTex:forBandIndex:tilePaddingSize:outputPyrBandOffset:outputTileSize:scratchOffset:encodeToContext:isFirstBatch:nonReferenceFrameCount:fusionParams:]"
+ "-[RawNightModeFusionMetalStage getNoiseMapScalingFrom:fromGain:noiseMapScaling:]"
+ "-[RawNightModeFusionMetalStage initWithCommandQueue:]"
+ "-[RawNightModeFusionMetalStage updateNoiseMapWithWeightPyramidTile:withNetworkInputTileTexForRefNoise:withInputFusedBand1:noiseMapAccumulationTex:tileCoordOffset:fullCoordOffset:outputTileSize:encodeToContext:isFirstBatch:nonReferenceFrameCount:]"
+ "-[RawNightModeFusionMetalStage updateParametersFromMetadata:cameraInfoByPortType:lscGainMapParameters:tuningParameters:firstPix:isQuadra:requiresDarkCurrentNoiseModel:aeTargetGain:]"
+ "-[RawNightModeFusionMetalStage writeOutToAccumulator:fromScratchAccumulator:outputPyrBandOffset:scratchOffset:tilePaddingSize:outputTileSize:encodeToContext:isFirstBatch:bandIndex:]"
+ "-[RawNightModeFusionMetalStage zeroPyramidsWithContext:withFusionPyramids:withAccumPyramidTile:]"
+ "-[RawNightModeGreenGhost applyInpaintWithDownscaledRGB:propagatedRGB:propagatedGradient:outputRGB:params:]"
+ "-[RawNightModeGreenGhost canMitigationProceedWithMaxMaskAverage:]"
+ "-[RawNightModeGreenGhost computeFusionWeightsNonRefLuma:nonRefChroma:maskMBBinary:nonRefProperties:output:params:]"
+ "-[RawNightModeGreenGhost computeLSCWBGParams]"
+ "-[RawNightModeGreenGhost computeTemporalVariationsNonRefLuma:nonRefProperties:params:]"
+ "-[RawNightModeGreenGhost defineSensorType]"
+ "-[RawNightModeGreenGhost fuseNonRefFrame:downscaledLuma:downscaledChroma:maskMBBinary:output:params:]"
+ "-[RawNightModeGreenGhost guidedFilter:withGuideLuma:guideChroma:params:output:]"
+ "-[RawNightModeGreenGhost mixRefFrameWithAccumulator:]"
+ "-[RawNightModeGreenGhost prepareFrame:outputLuma:outputChroma:]"
+ "-[RawNightModeGreenGhost prepareInpaintWithInputTexture:outputRGBTexture:outputGradidentTexture:params:]"
+ "-[RawNightModeGreenGhost propagateRGB:gradient:outputRGB:outputGradient:params:]"
+ "-[RawNightModeGreenGhost refineMaskWithGuideLuma:guideChroma:params:maskMBBinary:]"
+ "-[RawNightModeGreenGhost residualCorrectionOfAccumulator:]"
+ "-[RawNightModeGreenGhost runFusionWithNonRefFrame:fusionWeights:output:params:]"
+ "-[RawNightModeGreenGhost updateFusionWeights:]"
+ "-[RawNightModeGreenGhost updateMaskComputeGradientsFor:outputMask:outputGradient:params:]"
+ "-[RawNightModeInputFrame bindTexturesWithConfig:metalContext:]"
+ "-[RawNightModeInputFrame calculateNormalisedFaceScore]"
+ "-[RawNightModeInputFrame calculateNormalisedGlobalScore]"
+ "-[RawNightModeInputFrame initFrameProperties]"
+ "-[RawNightModeInputFrame initWithSampleBuffer:cameraInfoByPortType:]"
+ "-[RawNightModeMultiFrameOutlierPixelCorrectionTuningParams readPlist:]"
+ "-[RawNightModePostDemosaic initWithMetalContext:]"
+ "-[RawNightModePostDemosaicTuningParams getPostDemosaicTuning]"
+ "-[RawNightModePostDemosaicTuningParams readPlist:]"
+ "-[RawNightModePostNetworkTuningParams getAddBackParams:forBand:gain:]"
+ "-[RawNightModePostNetworkTuningParams getBiasCorrectionParams:gain:]"
+ "-[RawNightModePostNetworkTuningParams getOutlierPixelCorrectionParameters:]"
+ "-[RawNightModePostNetworkTuningParams readPlist:]"
+ "-[RawNightModeProcessor _initRawNightModeDenoiseInference:isBarrington:isArgyleTripodMax:]"
+ "-[RawNightModeProcessor _initRawNightModeFusionInference:isBarrington:requiresDarkCurrentNoiseModel:]"
+ "-[RawNightModeProcessor _initRawNightModeTripodFusion:requiresDarkCurrentNoiseModel:]"
+ "-[RawNightModeProcessor _populateInferenceFusionData:withBatch:first:last:]"
+ "-[RawNightModeProcessor allocateResourcesForAccumulator:width:height:label:]"
+ "-[RawNightModeProcessor computeInferenceInputImage:outputLumaTexture:outputChromaTexture:]"
+ "-[RawNightModeProcessor computeYUVNoiseMap]"
+ "-[RawNightModeProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:]"
+ "-[RawNightModeProcessor extractLSCMetadataFromReferenceFrame:]"
+ "-[RawNightModeProcessor initWithCommandQueue:]"
+ "-[RawNightModeProcessor prewarm]"
+ "-[RawNightModeProcessor processInitialFrames:]"
+ "-[RawNightModeProcessor resetState]"
+ "-[RawNightModeProcessor runAWBOnOutputFrame:]"
+ "-[RawNightModeProcessor runLTMOnOutputFrame:]"
+ "-[RawNightModeProcessor runTripodFusionForBatch:isLast:referenceFrame:]"
+ "-[RawNightModeProcessor sendFrame:toReferenceFrameSelector:]"
+ "-[RawNightModeProcessor setOutput:]"
+ "-[RawNightModeProcessor setupWithOptions:nrfConfig:]"
+ "-[RawNightModeTiledInferenceProvider runInference]"
+ "-[RawNightModeTripodFusion updateParametersFromMetadata:tuningParameters:params:]"
+ "-[RawNightModeTripodFusionMetalStage createInputTile:fromInputFrames:fromShiftMaps:fromBlendWeights:withLSCGainsMap:withParams:tileStart:encodeToContext:]"
+ "-[RawNightModeTripodFusionMetalStage fuseFramesTiles:toAccumulator:noiseMap:withParams:tileCoordOffset:fullCoordOffset:outputTileSize:encodeToContext:isFirstBatch:isLastBatch:nonReferenceFrameCount:totalFrameCount:]"
+ "-[RawNightModeTripodFusionMetalStage initWithCommandQueue:]"
+ "-[RawProcFrames _verifyConsistentMetadataWithFrame:]"
+ "-[RawProcFrames addFrame:]"
+ "-[RawProcFrames initWithMetalContext:]"
+ "-[RawProcFrames registerImages:]"
+ "-[RawProcFrames setReferenceFrameIndex:]"
+ "-[RawProcFrames setRegWarpInput:]"
+ "-[RawProcInputFrame _checkRgbTexConfig:]"
+ "-[RawProcInputFrame allocateRGB]"
+ "-[RawProcInputFrame commonInitWithMetalContext:cameraInfo:inputFrame:metadata:uniqueFrameId:]"
+ "-[RawProcInputFrame commonInitWithMetalContext:cameraInfo:inputPixelBuffer:metadata:uniqueFrameId:]"
+ "-[RawProcInputFrame commonInitWithMetalContext:cameraInfo:inputSamplebuffer:uniqueFrameId:]"
+ "-[RawProcInputFrame commonInit]"
+ "-[RawProcInputFrame demosaicWithStage:]"
+ "-[RawProcInputFrame getGDCParametersWithCameraInfoByPortType]"
+ "-[RawProcInputFrame initFrameProperties]"
+ "-[RegDense initWithMetalContext:bicubicWarping:useMirroredRepeat:]"
+ "-[RegDense prepareWithImageWidth:imageHeight:allocateTextures:]"
+ "-[RegDense pyramidConfidence:input:]"
+ "-[RegDense runWithReferenceImage:nonReferenceImage:warpedImage:relativeBrightness:homography:regDenseParams:alwaysDense:refWeightsLevel:nonRefWeightsLevel:]"
+ "-[RegDense warpAdditionalImage:warpedImage:homography:hybridReg:alwaysDense:]"
+ "-[RegDenseShaders initWithMetal:]"
+ "-[RegDenseShared getShaders:]"
+ "-[RegPyrFusion basicSearchWithCommandBuffer:renderPassDesc:refDerivTex:nonRefDerivTex:prevShiftMap:nextShiftMap:homography:pyrLevel:]"
+ "-[RegPyrFusion bilinearScaleWithCommandBuffer:renderPassDesc:refTexIn:refTexOut:nonRefTexIn:nonRefTexOut:pyrLevel:]"
+ "-[RegPyrFusion confidenceMapWithCommandBuffer:renderPassDesc:shiftMap:confidenceOut:]"
+ "-[RegPyrFusion fusionWithCommandBuffer:refTex:refDerivTex:nonRefDerivTex:prevShiftMap:nextShiftMap:homography:pyrLevel:]"
+ "-[RegPyrFusion generateDerivativesWithCommandBuffer:renderPassDesc:inputTex:outputTex:]"
+ "-[RegPyrFusion initWithMetalContext:]"
+ "-[RegPyrFusion prepareWithImageWidth:imageHeight:]"
+ "-[RegPyrFusion registerImagesWithReference:nonRef:refTexlvl1:nonRefTexlvl1:shiftMap:confidenceMap:]"
+ "-[RegPyrFusion selectionWithCommandBuffer:renderPassDesc:refDerivTex:nonRefDerivTex:prevShiftMap:nextShiftMap:homography:pyrLevel:]"
+ "-[RegPyrFusion setupPyramidScalersUsingCalib]"
+ "-[RegPyrFusion smoothShiftMapWithCommandBuffer:renderPassDesc:input:output:]"
+ "-[RegPyrFusionShaders createPipelineStateWithMetal:vShaderName:fShaderName:outputColorMetalFormat:constantValues:]"
+ "-[RegPyrFusionShaders initWithMetal:]"
+ "-[RegPyrFusionShared getShaders:]"
+ "-[RegWarpConfig(Demosaic) getDemosaicConfigForInputFrame:demosaicConfig:]"
+ "-[RegWarpConfig(RegWarp) getValidBufferRect:forInputFrame:withWidth:andHeight:]"
+ "-[RegWarpHelper convertInput10BitPixBuf:downsampledOutput8BitPixBuf:mtlCommandBuffer:]"
+ "-[RegWarpHelper initWithMetal:]"
+ "-[RegWarpHelperShared getShaders:]"
+ "-[RegWarpShaders initWithMetalContext:]"
+ "-[RegWarpStage allocateResources:]"
+ "-[RegWarpStage configForPrepareDescriptor:outputCompressionLevel:]"
+ "-[RegWarpStage createMetalTexture:width:height:pixelFormat:]"
+ "-[RegWarpStage initWithMetalContext:staticParameters:]"
+ "-[RegWarpStage runWithArgs:]"
+ "-[RegWarpStage validateInputFrame:config:]"
+ "-[RegWarpStageArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[SemanticStylesPlist bgTuningForSceneType:]"
+ "-[SemanticStylesPlist readPlist:]"
+ "-[SemanticStylesShaders initWithMetalContext:]"
+ "-[SemanticStylesShared getShaders:]"
+ "-[SemanticStylesStage calculateHistogramStatsWithLumaTex:chromaTex:]"
+ "-[SemanticStylesStage createGuideImage:]"
+ "-[SemanticStylesStage initWithMetalContext:]"
+ "-[SemanticStylesStage newTexture2DWithFormat:width:height:usage:disableCompression:label:]"
+ "-[SemanticStylesStage processPersonMaskTex:skinMaskTex:skyMaskTex:]"
+ "-[SemanticStylesStage renderWithLumaTex:chromaTex:outLumaTex:outChromaTex:gainMapTex:outputGainMapTex:]"
+ "-[SemanticStylesStage upsampleLightMap]"
+ "-[SingleColorCubeCorrectionStage init:alternateCubeSize:alternateCubeData:defaultCubeSize:defaultCubeData:]"
+ "-[SingleColorCubeCorrectionStage load3DTextureFromData:cubeSize:metal:outTexture:]"
+ "-[SingleColorCubeCorrectionStage runOnLuma:andChroma:withMask:outChroma:]"
+ "-[SingleColorCubeCorrectionStageShared getShaders:]"
+ "-[SoftISPBounds initWithInputFrame:outputFrame:quadraBinned:]"
+ "-[SoftISPConfig validateInputFrame:]"
+ "-[SoftISPConfig validateOutputFrame:]"
+ "-[SoftISPConnection initFromStage:fromProperty:toStage:toProperty:isNullable:]"
+ "-[SoftISPGraph addConnectionFromStage:fromProperty:toStage:toProperty:isNullable:]"
+ "-[SoftISPGraph addStage:withName:]"
+ "-[SoftISPGraph executionOrder]"
+ "-[SoftISPGraph init]"
+ "-[SoftISPInputFrame bindTexturesForConfig:metalContext:]"
+ "-[SoftISPInputFrame initBinnedQuadraVariantOf:inputTexture:]"
+ "-[SoftISPInputFrame initWithSampleBuffer:uniqueID:processingOptions:]"
+ "-[SoftISPKernelWithFunctionConstants _calculateParameterOffsetAndSize:functionConstantNamespace:]"
+ "-[SoftISPKernelWithFunctionConstants _dataKeyFromParams:]"
+ "-[SoftISPKernelWithFunctionConstants _loadWithMetalContext:kernelName:functionConstantNamespace:paramCombinations:]"
+ "-[SoftISPKernelWithFunctionConstants _loadWithMetalContext:kernelName:functionConstantNamespace:paramValues:]"
+ "-[SoftISPKernelWithFunctionConstants _verifyFunctionConstants:]"
+ "-[SoftISPKernelWithFunctionConstants _verifyParamValues:forFunction:functionConstantNamespace:]"
+ "-[SoftISPModuleCalibration initWithCMIModuleCalibration:metalContext:]"
+ "-[SoftISPModuleCalibration_BlackLevelShadingCorrection initWithBlackLevelShadingCorrectionThumbnails:metalContext:]"
+ "-[SoftISPModuleCalibration_BlackLevelShadingThumbnail initWithThumbnailDict:metalContext:]"
+ "-[SoftISPModuleCalibration_ShadingFPNCorrection initWithShadingFPNCorrectionImage:metalContext:]"
+ "-[SoftISPOutputFrame addCompletionHandlerToCommandBuffer:]"
+ "-[SoftISPOutputFrame allocateTexturesForConfig:metalContext:]"
+ "-[SoftISPOutputFrame bindTexturesForConfig:metalContext:]"
+ "-[SoftISPOutputFrame initWithInputFrame:maximumOutputDimensions:outputDownscaleFactor:parentProcessor:]"
+ "-[SoftISPOutputFrame resource]"
+ "-[SoftISPPipeline applyConnectionToArgsForStage:pipelineArgs:currentStageArgs:currentStageOutputConnections:]"
+ "-[SoftISPPipeline applyInputConnectionsToArgsForStage:pipelineArgs:]"
+ "-[SoftISPPipeline applyOutputConnectionsToArgsForStage:pipelineArgs:]"
+ "-[SoftISPPipeline auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:]"
+ "-[SoftISPPipeline auxiliaryPixelFormatForAuxiliaryType:inputPixelFormat:outputCompressionLevel:]"
+ "-[SoftISPPipeline bytesRequiredForConfig:]"
+ "-[SoftISPPipeline createArgsForStage:pipelineArgs:]"
+ "-[SoftISPPipeline initWithGraph:metal:staticParameters:]"
+ "-[SoftISPPipeline outputPixelFormatForInputPixelFormat:outputCompressionLevel:]"
+ "-[SoftISPPipeline runWithArgs:]"
+ "-[SoftISPPipeline setReferenceFrameByUniqueID:]"
+ "-[SoftISPPipeline validateInputFrame:config:]"
+ "-[SoftISPPipelineArgs initWithConfig:bounds:inputFrame:outputFrame:]"
+ "-[SoftISPPipelineConfig initWithStaticParameters:prepareDescriptor:outputCompressionLevel:graph:]"
+ "-[SoftISPProcessor _clearInputFrames]"
+ "-[SoftISPProcessor _processInputFrame:isFinalPass:]"
+ "-[SoftISPProcessor _readDefaults]"
+ "-[SoftISPProcessor addFrame:uniqueID:processingOptions:]"
+ "-[SoftISPProcessor auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:alignmentOut:]"
+ "-[SoftISPProcessor auxiliaryPixelFormatForPipeline:auxiliaryType:inputPixelFormat:]"
+ "-[SoftISPProcessor externalMemoryDescriptorForConfiguration:]"
+ "-[SoftISPProcessor outputDownscaleFactorForPipeline:]"
+ "-[SoftISPProcessor outputPixelFormatForPipeline:inputPixelFormat:]"
+ "-[SoftISPProcessor prepareToProcess:prepareDescriptor:]"
+ "-[SoftISPProcessor processIfPossible]"
+ "-[SoftISPProcessor process]"
+ "-[SoftISPProcessor resetState]"
+ "-[SoftISPProcessor setCameraInfoByPortType:]"
+ "-[SoftISPProcessor setReferenceFrameByUniqueID:]"
+ "-[SoftISPProcessor setup]"
+ "-[SoftISPStaticParameters _generateSoftISPTuningParameters]"
+ "-[SoftISPStaticParameters _initModuleCalibrationByPortType:]"
+ "-[SoftISPStaticParameters cameraInfoForInputFrameMetadata:]"
+ "-[SoftISPStaticParameters dimensionsForSensorInBayerPixelsInMetadata:]"
+ "-[SoftISPStaticParameters dimensionsForSensorInMetadata:]"
+ "-[SoftISPStaticParameters firstPixelForSensorID:]"
+ "-[SoftISPStaticParameters initWithCameraInfoByPortType:tuningParameters:moduleCalibrationByPortType:metalContext:deviceGeneration:]"
+ "-[SoftISPStaticParameters moduleConfigForInputFrameMetadata:]"
+ "-[SoftISPStaticParameters moduleConfigForPortType:]"
+ "-[SoftISPStaticParameters tuningFlagForProcessingOption:tuningType:metadata:]"
+ "-[SoftISPStaticParameters tuningParametersForInputFrameMetadata:tuningType:]"
+ "-[SoftLTM initWithMetalContext:]"
+ "-[SoftLTM processLTMMetadata:toDarkestFrameMetadata:toEV0FrameMetadata:]"
+ "-[SoftLTM setupIBPTuningParameters:with:]"
+ "-[SubjectRelightingShaders initWithMetalContext:]"
+ "-[SubjectRelightingShared getShaders:]"
+ "-[SubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]"
+ "-[SubjectRelightingStage initWithMetalContext:]"
+ "-[SyntheticLongPlist readBandData:]"
+ "-[SyntheticLongPlist readPlist:]"
+ "-[SyntheticReferencePlist _readDeepShadowRecoveryBandData:]"
+ "-[SyntheticReferencePlist _readHighlightRecoveryBandData:]"
+ "-[TextureUtils _fillTexturePaddedArea10BitPacked:roi:fullWidth:fullHeight:]"
+ "-[TextureUtils _fillTexturePaddedArea:roi:]"
+ "-[TextureUtils clearTexture:]"
+ "-[TextureUtils fillPaddedAreaInFrame:roi:didExtend:]"
+ "-[TextureUtils initWithMetalContext:]"
+ "-[TextureUtilsShared getShaders:]"
+ "-[ToneMapSmoothingBandData readPlist:]"
+ "-[ToneMapSmoothingPlist readPlist:]"
+ "-[ToneMapSmoothingResources allocateResourcesForWidth:height:useMaskPyramid:]"
+ "-[ToneMapSmoothingResources initWithMetalContext:width:height:mtlSubAllocatorID:srlVersion:]"
+ "-[ToneMappingCurves estimateMaskRegionInTiles:]"
+ "-[ToneMappingCurves initWithWithContext:]"
+ "-[ToneMappingCurves regularizeLocalToneCurves:mask:tcrParams:imageDims:]"
+ "-[ToneMappingCurves updateToneCurveAllocationsWithLTC:]"
+ "-[ToneMappingPlist applyOverrides]"
+ "-[ToneMappingPlist readPlist:]"
+ "-[ToneMappingShaders initWithMetal:]"
+ "-[ToneMappingShared getShaders:]"
+ "-[ToneMappingStage calculateBlackWhiteContrastCenter:contrastParam:curves:]"
+ "-[ToneMappingStage getSrlBoostedLTMasNSData:]"
+ "-[ToneMappingStage initWithContext:mtlSuballocatorID:]"
+ "-[ToneMappingStage performBlackSubtractionWithBlackWhiteParams:maxContrastStrength:inOutTex:curves:]"
+ "-[ToneMappingStage performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:]"
+ "-[ToneMappingStage performToneMapSmoothing:luma:mask:auxMask:skyMask:tmPlist:ev0FrameMetadata:useMaskPyramid:firstPass:]"
+ "-[ToneMappingStage setupSTFProcessor:]"
+ "-[UBProcessorV4 _appendFrames:cfp:]"
+ "-[UBProcessorV4 _bindRegWarpPPWithWidth:height:pixelFormat:]"
+ "-[UBProcessorV4 _downsampleImageForRegistration:outputImage:]"
+ "-[UBProcessorV4 _isMetadataConsistentWithFirstFrame]"
+ "-[UBProcessorV4 _multiFrameProcessing]"
+ "-[UBProcessorV4 _processInferenceImage:sourceFrameType:sourceFrameIndex:ltcFrameIndex:gtcFrameIndex:originalWidth:originalHeight:]"
+ "-[UBProcessorV4 _processSIFRandRefEV0IfPossible:]"
+ "-[UBProcessorV4 bindResourcesForProcessingType:prepareDescriptor:]"
+ "-[UBProcessorV4 calculateBackingBufferSizeForDesc:nrfConfig:processingType:metal:]"
+ "-[UBProcessorV4 determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:]"
+ "-[UBProcessorV4 determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:]"
+ "-[UBProcessorV4 getOptions:]"
+ "-[UBProcessorV4 getProcessingTypeKey:metadata:separateHWISP:]"
+ "-[UBProcessorV4 prepareToProcess:]"
+ "-[UBProcessorV4 prewarm]"
+ "-[UBProcessorV4 resetState]"
+ "-[UBProcessorV4 sanityCheckHomographyForBracketIndex:]"
+ "-[UBProcessorV4 setFusionMode:]"
+ "-[UBProcessorV4 setOutput:]"
+ "-[UBProcessorV4 setProgressiveBatchSize:]"
+ "-[UBProcessorV4 setReferenceFrameIndex:]"
+ "-[UBProcessorV4 setSharedRegWarpBuffer:]"
+ "-[UBProcessorV4 setupWithOptions:nrfConfig:]"
+ "-[UBProcessorV4 updateEV0ReferenceFrameIfNecessary]"
+ "-[WarpShaders initWithMetal:]"
+ "-[WarpStage runWarpUsingTransform:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:]"
+ "-[WarpStage runWarpUsingTransform:inputYCbCrTex:inputCscParams:outputLinearLumaTex:outputLinearChromaTex:]"
+ "-[WarpStageShared getShaders:]"
+ "-[ZimmerDEMTuningParams readPlist:]"
+ "/#2"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Defringing/VideoDefringingTuningParameters.m %s: missing required param: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/RegWarpHelper/RegWarpHelper.m %s: Couldn't build RegWarpHelper shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/RegWarpHelper/RegWarpHelper.m %s: Unable to init base class for RegWarpHelperShaders"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/RegWarpHelper/RegWarpHelper.m %s: metal is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/BlinkDetection/BlinkDetectionStageV4.m %s: BD> %s idx %d: x=%f y=%f w=%f h=%f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/BlinkDetection/BlinkDetectionStageV4.m %s: BD> Blink detection:\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/BlinkDetection/BlinkDetectionStageV4.m %s: BD> face idx %d: x=%f y=%f w=%f h=%f  confidence=%d roll=%d yaw=%d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/BlinkDetection/BlinkDetectionStageV4.m %s: Couldn't build BlinkDetection shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/BlinkDetection/BlinkDetectionStageV4.m %s: Unable to create BlinkDetectionShaders"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/BilateralGrid/BilateralGridV4.m %s: BilateralGrid %s using FigMetalAllocator"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/BilateralGrid/BilateralGridV4.m %s: Couldn't build BilateralGridShared shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/BilateralGrid/BilateralGridV4.m %s: Unable to init 'BilateralGridShaders'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/BilateralGrid/BilateralGridV4.m %s: failed to allocate BilateralGrid textures"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/CMITiledInferenceProcessorStageV4.m %s: %s completion errors reported."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/CMITiledInferenceProcessorStageV4.m %s: %s runs not reported complete."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/CMITiledInferenceProcessorStageV4.m %s: runWithTileCount failed error (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/ColorConvert/ColorConvertV4.m %s: Couldn't build ColorConvertStage shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/ColorConvert/ColorConvertV4.m %s: Unable to create ColorConvertStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/ColorConvert/ColorConvertV4.m %s: convertColor"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/ColorConvert/ColorConvertV4.m %s: convertColorAndDownsample"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/ColorConvert/ColorConvertV4.m %s: convertColorYCbCr"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/ColorConvert/ColorConvertV4.m %s: extractAndDownsampleLinearWithLumaInput output dimensions match input, using legacy path."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Demosaic/CMIDemosaicStageV4.m %s: firstPix = %d, cfaLayout = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Demosaic/CZDemosaicStageV4.m %s: Failed to allocate CZDemosaic metal shader"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Demosaic/CZDemosaicStageV4.m %s: metal nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Demosaic/CZDemosaicStageV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Dense/RegDenseV4.m %s: Couldn't build RegDenseShared shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Dense/RegDenseV4.m %s: Running RegDense with mode: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Dense/RegDenseV4.m %s: Unable to create RegDense"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Dense/RegDenseV4.m %s: _confPipeline = nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Dense/RegDenseV4.m %s: constantValues is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Dense/RegDenseV4.m %s: runWithReferenceTex:.. has failed!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/DraftDemosaic/CMIDraftDemosaicStageV4.m %s: Output crop %{public}@ doesn't fit in the output texture with %{public}@ dimensions : %{private}@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/DraftDemosaic/CMIDraftDemosaicStageV4.m %s: divFactor = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/DraftDemosaic/CMIDraftDemosaicStageV4.m %s: getDraftDemMode draftDemosaicStage is using draftDemMode = %d (cfaLayout = %d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/DraftDemosaic/CMIDraftDemosaicStageV4.m %s: inputDims {%d, %d}"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/DraftDemosaic/CMIDraftDemosaicStageV4.m %s: outputDims {%d, %d}"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/DraftDemosaic/CMIDraftDemosaicStageV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/FaceDetectionUtilsV4.m %s: exifOrientation (%d) is invalid. Returning 0 degrees/not mirrored"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/GreenGhost/GreenGhostCommonV4.m %s: No faces or human bodies were detected."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/GreenGhost/GreenGhostCommonV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/GreenGhost/GreenGhostV4.m %s: Clipping data version <%d> is not supported."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/GreenGhost/GreenGhostV4.m %s: FigCaptureLocalHistogramClippingDataV%u is not supported."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/GreenGhost/GreenGhostV4.m %s: FigCaptureLocalHistogramClippingDataV1:"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/GreenGhost/GreenGhostV4.m %s: FigCaptureLocalHistogramClippingDataV1: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/GreenGhost/GreenGhostV4.m %s: FigCaptureLocalHistogramClippingDataV1: localHistogramClippingData (highThresholdBin):"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/GuidedFilter/GuidedFilterV4.m %s: metal nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/GuidedFilter/GuidedFilterV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/TextureUtilsV4.m %s: Buffer layout is too small, Width_round_to_16 (%d)\tHeight_round_to_16 (%d), bytesPerRow (%d), extendedRows (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/TextureUtilsV4.m %s: Couldn't build TextureUtils shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/TextureUtilsV4.m %s: Unable to create TextureUtils"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/TextureUtilsV4.m %s: fillPaddedAreaInFrame is doing nothing since ROI covers the full buffer and its divisible by 16 already"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/TextureUtilsV4.m %s: fillPaddedAreaInFrame is running, it's doing something..."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/ConcurrentProcessing/NRFConcurrentProcessingV4.m %s: _backgroundContext.allocator.largestOccupiedOffset = %lu"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/ConcurrentProcessing/NRFConcurrentProcessingV4.m %s: _joinBackgroundCommandQueue setupWithDescriptor failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/ConcurrentProcessing/NRFConcurrentProcessingV4.m %s: background task returned error, %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:                  (%f, %f, %f)\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:     x1:     %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:     x1: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:     x2:     %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:     x2: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:     y1:     %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:     y1: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:     y2:     %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:     y2: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  ADRCExposureGain %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  AlternateHDRHeadroom %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  AlternateOffsetConstant %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  BaselineHDRHeadroom %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  BaselineOffsetConstant %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  EDR %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  EDR_correction_on %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  GainMapHeadroom %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  GainMapMax %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  GainMapMin %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  Gamma %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  HDRLumaAPosScaling (%f, %f)\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  HL_starting_point %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  M++ Headroom %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  MeteorPlusGainMapAverage %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  MeteorPlusGainMapHeadroom %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  chromaBias %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  chromaPosScaling (%f, %f)\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  clipEnd %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  clipPower %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  clipStart %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  clipThresh %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  colorCorrection (%f, %f, %f)\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  dclip (%f, %f, %f, %f)\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  dhist_max_gnorm %.1f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  divisionEpsilon %.8f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  dw_change_max_for_mids_th1 %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  dw_change_max_for_mids_th2 %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  dw_change_max_for_mids_top %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  eps_for_log %.12f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  exposureBiasFactor %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  hdr_mix %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  ht_top_thr1 %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  ht_top_thr2 %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  ht_total_recip %.12f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  isLinear %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  lowThresh %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  ltmHardGain %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  ltm_roi (%d, %d, %d, %d)\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  lumaPosScaling (%f, %f)\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  meanThresh %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  newHeadroom %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  thr_HL %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  topThresh %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  x1_dw_change_for_mids %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s:  x2_dw_change_for_mids %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: -------------------------------- config --------------------------------\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: -------------------------------- end config --------------------------------\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: Couldn't build GainMapShared!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: Denominator exceeds specified bit width!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: EDR_base %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: EDR_correct %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: EDR_correct_low  %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: EDR_correct_lux  %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: EDR_correct_soft %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: Failed to set up RWTMOConstantsBuf"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: Failed to set up maxBuf"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: GainMapStageV4 computeGainMapWithInput: missing HDR metadata, falling back to SDR metadata"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: HDR lumaA input image size [%dx%d]\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: HDRAverage[%d] %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: HLG Stills case\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: HL_ind                      %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: HL_starting_point           %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: Illegal texture input configuration for gain map RunWithInput"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: RGB case\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: Using LuxLevel Metadata - %f lux\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: YCCTex %d x %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: YCbCr case\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: _gainMapCommandBuffer is nil or hasn't yet been committed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: _gainMapStage runWithInput failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: aeAGC %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: aeShutterTime %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: allocateLTMTable: for HDR failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: allocateLTMTable: for SDR failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: clipEnd:    %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: clipPower:  %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: clipStart:  %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: clipThresh: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: convertHLGYTexture: _metalContext %p"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dclip:\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dhist.hi:  %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dhist.low: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dhist.max_gnorm %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dhist.mid: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: divisionEpsilon             %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dlow:\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dlux:\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dsoft:\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dw_change_max_for_mids_th1: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dw_change_max_for_mids_th2: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: dw_change_max_for_mids_top: %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: eps_for_log:                %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: expBias %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: exposureBiasFactor:         %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: final hdr_mix %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: flexRangeGainMapMetadata\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: fullContrastBoost:          %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: gain map v4 computation begun"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: gain map v4 computation completed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: gain_log %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: gammaBoost:                 %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: has LTM tables/curves for HDR\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: has LTM tables/curves for SDR\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: hdr_mix_max_x1:             %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: hdr_mix_max_x2:             %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: hdr_mix_max_y1:             %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: hdr_mix_max_y2:             %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: ht_top_thr1                 %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: ht_top_thr2                 %d\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: ht_use_contrast:            %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: ht_use_gamma:               %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: input image size [%dx%d]\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: ispDGainOld %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: ltm_avg %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: ltm_change_Hls_max %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: ltm_change_Hls_thresh:      %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: lux_log %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: new EDR %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: nil metalContext"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: outputCbCrTex %d x %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: outputHLGLumaATex %d x %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: outputYTex %d x %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: requested gain map size [%dx%d]\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: second input image size [%dx%d]\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: shadow_val:                 %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: softDGain %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: soft_log %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: thr_HL:                     %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: using _MPPConvertHLGToSDRAndHLGLumaA420"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: x1_dw_change_for_mids:      %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GainMap/GainMapStageV4.m %s: x2_dw_change_for_mids:      %f\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GreenGhostLowLight/GreenGhostLowLightStageV4.m %s: GreenGhost LowLight releaseTextures"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GreenGhostLowLight/GreenGhostLowLightStageV4.m %s: Low-light green ghost mitigation is not running, because tripod mode is detected."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GreenGhostLowLight/GreenGhostLowLightStageV4.m %s: Low-light green ghost mitigation maskAverage = %.2f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GreenGhostLowLight/GreenGhostLowLightStageV4.m %s: Resetting low light green ghost mitigation"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/GreenGhostLowLight/GreenGhostLowLightStageV4.m %s: _maskMB is nil, which means we didn't do any mitigation work yet and the detection is not reliable (non-reference frames are too blurry or didn't register correctly), so inpainting will be skipped too"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: BilateralGrid is not used, not allocating resources"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Calculate a haze correction."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Couldn't build DenoiseFusePipeline shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: DenoiseFusePipelineV4 doGainMap: calling computeGainMapWithInput"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: DenoiseFusePipelineV4 doGainMapOnSingleFrameLuma calling computeGainMapWithInput"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: DenoiseFusePipelineV4 goGainMap calling gainmap runWithInput"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: DenoiseFusePipelineV4 goGainMap setup for V3 gainmap"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: DenoiseFusePipelineV4 goGainMapOnSingleFrameLuma calling gainmap runWithInputDownsampled"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Failed to tap-out pre-tonemapped output as linear, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Initializing backgroundMetal support for LearnedNR"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: NRF denoiseSingleImage has semantics: %i"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: NRFLearnedNRBackground memSize: (%.2fMB), usedSizeAll: (%.2fMB), largestOccupiedOffset: (%.2fMB)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: NRFProcessorInferenceResultsProvider encountered an error, continuing without use of inference results."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: NRFProcessorInferenceResultsProvider returned nil, continuing without use of inference results."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: No pyramid level found size (%d,%d) requested"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Pyramid level %d of size (%d,%d) found for size (%d,%d) requested"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Setting up BilateralGrid resources"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Setting up backgroundMetal.allocator to memsize: %lu "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Unable to bind Y plane of source pixel buffer to metal texture"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Unable to create DenoiseFusePipeline"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Unable to select reference frame for NRF"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: _gainMapStage runWithInput failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: addFrameWithInputLuma failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: bindYCbCrMetalTextureWithMetalContext failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: boundInferenceResults is nil; continuing without use of inference results"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: computeGainMapWithLuma failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: convertColor failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: converting HLG to SDR %s HLG pixel buffer -- _metal %p"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: maskedSkyCubeVersion: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: mustAllocate = %d; width %d=%d, height %d=%d pixFmt 0x%x=0x%x"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: output buffer shouldn't be aliased at this stage!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: outputImage->chromaTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: outputImage->lumaTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: pixel buffer be provided for HLG texture"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: pyramidLevel not valid for sourceFrameIndex:%d, dimensions:%ux%u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: setupLearnedNRTaskWithInputFrame failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: setupSTFProcessor failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: startBackgroundTask failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: waitForBackgroundTaskToComplete failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/LSCGainsPlistV4.m %s: Unable to create LSCGainsPlist"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/LSCGainsPlistV4.m %s: _lscGainsByPortType must be defined"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: ADRCExposureRealizedGain must not be 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: AWBRGain: %d, AWBBGain: %d, AWBGGain: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Failed allocating _HDRltmCurvesForBackground"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: HREnabled: %s, HRGainDownRatio: %g "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Loading metadata: could not find DetectedObjectsInfo"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Loading metadata: could not find DetectedObjectsInfo/HumanBodies"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Loading metadata: could not find DetectedObjectsInfo/HumanBodies/ObjectsArray"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Loading metadata: could not find DetectedObjectsInfo/HumanBodiesObjectsArray/Rect for item %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Loading metadata: could not find DetectedObjectsInfo/HumanBodiesObjectsArray/Rect values for item %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Loading metadata: could not find DetectedObjectsInfo/HumanFaces"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Loading metadata: could not find DetectedObjectsInfo/HumanFaces/ObjectsArray"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Loading metadata: could not find DetectedObjectsInfo/HumanFacesObjectsArray/Rect for item %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Loading metadata: could not find DetectedObjectsInfo/HumanFacesObjectsArray/Rect values for item %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Missing kFigCaptureStreamMetadata_AWBCombo*Gain keys"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Original ltmSoftGain = %0.4f, new estimated ltmSoftGain = %0.4f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: TEMP! fixing quadraInverseBinningGainFactor to 1.2"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: UB ValidBufferRect is: < x: %f, y: %f, w: %f, h: %f >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: ValidBufferRect is outside the image bound"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: Warning: ltmSoftGain out of range: %f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: _estimateGainFromMetadata: globalLTM->lutEntry count has unexpected value"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: awbInternalMetadata i.e., metadata[MIWBOutputMetadata] not found"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: estimateGainFromMetadata: averageLTMCurve invalid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: exposure time: %f, gain: %f, red_gain: %f, blue_gain: %f, average focus score: %f, exposure bias: %f is_long: %d lsModulationWeight: %f "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: gtcLastLuma is invalid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: isp_digital_gain: %f, hard_gain: %f "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: lsModulationWeight must be <= 1.0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: no metadata dictionary present ... using default exposure and gain values"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: objectsArray.count (%d) is larger than MAX_N_BODIES (%d), so limiting bodies count to (%d) only"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: objectsArray.count (%d) is larger than MAX_N_FACES (%d), so limiting faces count to (%d) only"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: properties is NULL"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: quadraBinningFactor: %d, quadraInverseBinningGainFactor: %f "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFMetadataV4.m %s: targetLumaPreGHC is not above 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Defaults writes override: motionDetectionOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Defaults writes override: preWarpInputsOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Failed to parse entries for key = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: GainValueArray has already been set"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Overriding Blink Detection confidence threshold value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Overriding Blink Detection left eye weight value; was '%f', now '%f'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Overriding Blink Detection mode value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Overriding Blink Detection mouth weight value; was '%f', now '%f'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Overriding Blink Detection right eye weight value; was '%f', now '%f'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Overriding Blink Detection strength value; was '%f', now '%f'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Overriding enableMotionDetection value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Overriding hybridRegistrationMode value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Overriding preWarpInputs value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Parsing RFS/BFR weights; unrecognized key: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Unable to create GlobalDistortionCorrectionPlist"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: getNRFTuningForSensor, starting iterating on NRF processing types: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: getNRFTuningForSensor, starting iterating on tuningParamsKey: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: getNRFTuningForSensor: No dictionary options found for %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: getNRFTuningForSensor: get_calibration_data() failed while extracting UB parameters"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: getNRFTuningForSensor: key (sensor id) %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: handle_per_reference_band_data failed since corresponding item isn't a dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: must have even number of entries"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: processing data with key = '%@' is nil or unused"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFSingletonsV4.m %s: Flushing IOUnifiedAddressTranslator with small dummy allocation"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFSingletonsV4.m %s: NRFSingletonsReleaseAll"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: %{private}@ Processor process: processingType (%{public}d): %{private}s(errCode=%{public}d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: %{private}@ addFrame (%{public}d): %{private}s(%{public}d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Cannot create inputFrame for frame index: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Cannot create metal context"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Cannot find ev0InputFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Cannot find ltcInputFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Cannot instantiate FigMetalContext for prewarming"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Could not prepareToProcess the softLTM stage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Demosaic is using < %s > "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Doesn't support input pixelFormat"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: DraftDemosaicAuxiliaryBuffer availability is: < %d >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Failed to allocate %{public}@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Failed to bind resources"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Failed to init CMIDemosaicStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Failed to init CMIPost"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Failed to init GainMapStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Failed to init RawDFInferenceGen"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Failed to tap-out pre-tonemapped output as linear, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Generating Gain Map for Final."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Generating Input for Inference."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Invalid class for LearnedNRProcessor output!!!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Invalid reference frame Index"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: LTM recalculate on a final image"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: LearnedNR compressionLevel: < %d >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: LearnedNR failed setting up allocator with error = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: LearnedNR tuning: tuningMode=%@ (isQSUB=%d), captureType=%@ (isStereoPhotoFrame=%d, isProRaw=%d), frameType=%@ (isEVM=%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: LearnedNR: isVideoAspectRatio %d, aspectRatioMultiplier %f, desc.width %d, desc.height %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: MakerNoteFlag = 0x%x"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: NRF's memSize: (%.2fMB), usedSizeAll: (%.2fMB), largestOccupiedOffset: (%.2fMB)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: NRFProcessor process: received"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: No input reference frame "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: No support for planar pixelFormat"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: PyramidStorage allocatePyramidWithWidth failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: PyramidStorage setLumaTexture: failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Running _processInferenceImage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: SensorID mismatch for input image and tuning parameters. Input image has: %@,  while tuning plist has:\n %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Unable to create LearnedNRProcessor"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Unable to create PyramidStage_NRF"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Unable to create RawDFCommon"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Unable to create softLTM"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Unable to initialize NRFConfig"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Use [NRFProcessor prepareToProcess:prepareDescriptor:] instead of this API"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Using DraftDemosaicAuxiliaryBuffer for registration"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Using provided metal command queue %p"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: [LearnedNRProcessor runPipeline]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _allocateAndFillLumaChromaImage failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _metalCommandQueue is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _nrfPlist->denoiseAndSharpening = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _nrfPlist->noiseModel           = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _nrfPlist->outputNoiseModel     = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _nrfPlist->toneMapping          = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _processInferenceImage failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _pyramidStage runGPUWithFilters: failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: bayerParams->networkModel : %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: bindTexture is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: calling computeGainMapWithInput"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: computeGainMapWithLuma failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: computeLTMFromLuma final fail"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: gainMap plist nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: gainMapOutputTexture failed to bind"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: gainmap computed, notifying delegate with pixelbuffer only, no metadata"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: generateGainMapIfNeeded failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: gtcFrameProperties nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: inference results bindings cannot be missing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: inference results cannot be missing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: inferenceInputPixelBuffer is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: inferenceInputPixelBuffer nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: inferenceMetadata nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: inferenceSourceImg not set right"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: input frame cannot be both EVM and Long at the same time"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: instanceMask is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: ltcFrameProperties nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: missing referenceFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: mustAllocate = %d; width %d=%d, height %d=%d pixFmt 0x%x=0x%x"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: nrfPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: originalWidth > 0 && originalHeight > 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: pixel buffer format is invalid for gain map"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: pixelBuffer is nil "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: pixelFormatDesc is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: postConfig is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: postProcOutput is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: prepareBand1InputWithBand0 failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: prepareToProcesss:prepareDescriptor: called for dimensions: (%d x %d), cmiResourceEnabled: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: process called without addFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: processInferenceImage failed with error: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: processSFDForInputTexture failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: processingType %d, denoiseFusePipelineSize: %lu"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: processingType = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: processingType = %{public}d, numBracketsFused=%{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: quadraParams->networkModel : %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: reference draftInferenceRGBTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: referenceFrame draftInferenceRGBTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: resetState is called"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: runDemosaicWithInputRawTex failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: runPostWithConfig failed with (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: runSemanticInferences failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: setupSTFProcessor failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: sourceFrameLumaChromaImage nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: sourceFrameProperties nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: td is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: updateParametersFromMetadata failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/NRFBackgroundLearnedNRV4.m %s: convertYUV420toRGB failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/NRFBackgroundLearnedNRV4.m %s: processSFDForInputTexture failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/NRFBackgroundLearnedNRV4.m %s: updateParametersFromMetadata failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: %@ networkPath is nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Cannot prewarm LearnedNRNetworkPostANEStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Cannot prewarm LearnedNRNetworkPreANEStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Cannot prewarm LearnedNRNetworkShaders"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Configuration expects a quadra frame but quadraBinningFactor is missing or inconsistent"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Couldn't determine CameraInfo from metadata"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to create _postStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to create _preStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to create _shaders."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to create _shared."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to create config."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to create proc."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to create stage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to get LearnedNR network path."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to initialize LearnedNRNetworkStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to load LSCGains texture"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Failed to load LSCGainsPlist"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: GlobalHighlightCompression count is incorrect"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: LSC buffer has unexpected pixel format"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: LearnedNR completion errors reported."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: LearnedNR runs not reported complete."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: LearnedNRNetworkStage tuningParams must be set."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Loading LearnedNR (SFD) network from path: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Median luma = %0.4f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Median luma after average local & global tone curves applied = %0.4f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Median luma after average local tone curve applied = %0.4f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Modulated noise std = %.2f, addBack = %.2f, addBackBand0 = %.2f, addBackClipToSNR = %.2f, addBackLSCModulation = %.2f, applyLSCModulationWeight = %d, isVersion2 = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Original totalGain = %0.4f, estimated totalGain = %0.4f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Quadra bayer pattern must be BBGG or RRGG"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Read and shot noise must be positive"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: SensorDimensions nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: SensorDimensions.height nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: SensorDimensions.width nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Temporarily recovering from loading LearnedNR bayer v4 network back to v3"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Temporarily recovering from loading LearnedNR quadra v3 network back to: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Tone curve enum not available"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Unable to create texture %s."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Unable to read lumaAddBackBand0Tuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Unable to read lumaAddBackClipToSNRTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Unable to read lumaAddBackLSCModulationTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Unable to read lumaAddBackTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Unable to read readNoiseModulationTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Unable to read shotNoiseModulationTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Unable to read tileOverlapParameters"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: Unsupported bayer pattern"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: GlobalLTMLookUpTable has unexpected size"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: count0 (%f) >= count1 (%f)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: countM (%f) < count0 (%f)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: countM (%f) > count1 (%f)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: failed to estimate median luma. medianCount=%u, globalHist[0]=%u, globalHist[1]=%u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: globalLTM is NULL"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: globalLTM->lutEntry count has unexpected value"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: header.version = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: localHistogramBinSize = %u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: localHistograms is NULL"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: ltmLuma out of bounds (%f)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: medianLuma out of bounds (%f)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: missing AverageLTM"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: missing GlobalLTMLookUpTable"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: missing LocalHistograms"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: tileGrid.tileCountX = %u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: unexpected AverageLTM.count"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: unexpected size = %u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _postStage nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _preStage nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _shared nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _stageConfig nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _tiledInferenceProcessor nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _tiledInferenceProcessor runWithTileCount failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _tuningParams is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: _tuningParams->networkModel is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: bayerPattern nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: cameraInfoByPortType nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: commandBuffer nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: computeEncoder nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: encoder nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: inputRaw nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: invalid deviceGeneration %u."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: invalid inputRaw dimensions."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: invalid inputRaw pixelFormat."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: invalid outChroma dimensions."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: invalid outChroma pixelFormat."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: invalid outLuma dimensions."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: invalid outLuma pixelFormat."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: lscScale = (%.4f %.4f) lscOffset = (%.4f %.4f)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: metadata nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: metal nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: outChroma nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: outLuma nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: self.shared.frameProperties nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: setupTiledInferenceProcessor failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: sfdNetConfig.networkPath = %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Network/LearnedNRNetworkStageV4.m %s: td nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: DefaultSensorIDs dictionary is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: Failed to parse defringing tuning for port type: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: Loading tuning for: < Port: %@, sensorID: %@, tuningType: %@ >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: MIWB readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: MIWBPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: OutputNoiseModelPlist readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: _tuningParams dictionary is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: denoiseAndSharpening readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: dictForZoom is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: entryParams DenoiseAndSharpening is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: entryParams NoiseModel is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: entryParams ToneMapping is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: entryParams semStylesPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: failure to extract GainMapPlist parameters"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: greenGhostBrightLightTuningParams readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: learnedNRTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: noiseModelPlist readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: nrfPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: onmPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: parametersForMode is nil for %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: parametersForMode1x is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: qdemTuning is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: qdemTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: quadraLearnedNRTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: semStylesPlist readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: sensorID is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: sensorIDAsNumber is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: toneMapping readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: zimmerDEMTuning is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: zimmerDEMTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/MotionDetection/GrayGhostDetectionV4.m %s: Couldn't build GrayGhostDetection shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/MotionDetection/GrayGhostDetectionV4.m %s: Unable to create GrayGhostDetection"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/MotionDetection/GrayGhostDetectionV4.m %s: relativeBrightness = %f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/MotionDetection/MotionDetectionV4.m %s: Couldn't build MotionDetection shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/MotionDetection/MotionDetectionV4.m %s: Running motionDetection"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/MotionDetection/MotionDetectionV4.m %s: Unable to create MotionDetection"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/OutputNoiseModel/OutputNoiseModelV4.m %s: OutputNoiseModel: ltmGain = %0.3f, totalGain = %0.3f, readNoiseScalingFactor = %f, shotNoiseScalingFactor = %f, squaredNoiseScalingFactor = %f, spatialSigma = %f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/PlistCommonV4.m %s: Warning: %@ parameter missing from tuning dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Defaults writes override: enableBandZeroDenoisingOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Defaults writes override: enableBilateralRegressionOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Defaults writes override: enableDitheringOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Defaults writes override: enableLowVarSharpeningOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Overriding enableBandZeroDenoising value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Overriding enableBilateralRegression value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Overriding enableDithering value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Overriding enableLowVarSharpening value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: Defringing (CAC) is being applied: ( %{public}f )"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: Defringing (CAC) is disabled"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: Defringing (CAC) is enabled, however, it's not being applied: ( %{public}f )"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: Failed to copy tmpOutputImg->chromaTex to _outputImg->chromaTex"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: Failed to copy tmpOutputImg->lumaTex to _outputImg->lumaTex"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: Green Ghost mitigation is NOT running, as the green ghost location cannot be determined"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: Green Ghost mitigation is running and it's NOT using clipping data."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: UB: luma/chroma blur kernel size is hard coded to 5.0, are you sure?"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: gain: %f, band %d, blue_boost: %f, flatness_boost: %f, flatness_threshold: %f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/Defringe/DefringeStageV4.m %s: quadraBinningFactor = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/DenoiseRemixStageV4.m %s: Texture ( %@ ) : RG8Unorm only supports LL1 and LL3 compression. Since LL2 is requested, we are falling back to LL1"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/DenoiseRemixStageV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/OutliersRemovalStageV4.m %s: Couldn't build OutliersRemovalShared!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/OutliersRemovalStageV4.m %s: Unable to create OutliersRemovalStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/OutliersRemovalStageV4.m %s: metal nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/OutliersRemovalStageV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/CMIPost.m %s: GGM is < %{private}s(%{public}d) >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/CMIPost.m %s: colorCubeFixType: %d, maskedSkyCubeVersion: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ColorCubeCorrectionStage/ColorCubeCorrectionStageV4.m %s: Applying Color Cube Fix"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ColorCubeCorrectionStage/ColorCubeCorrectionStageV4.m %s: Couldn't build ColorCube shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ColorCubeCorrectionStage/ColorCubeCorrectionStageV4.m %s: Failed to initialize ColorCubeCorrectionStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ColorCubeCorrectionStage/ColorCubeCorrectionStageV4.m %s: Failed to set masked sky cube version for ColorCubeCorrectionStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ColorCubeCorrectionStage/ColorCubeCorrectionStageV4.m %s: colorCubeFix not implemented for colorCubeFixType = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ColorCubeCorrectionStage/ColorCubeCorrectionStageV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %s: MIWB: Global gains are invalid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %s: MIWB: Linear Interp 1D: X values aren't monotonic increasing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %s: MIWB: Skin gains are invalid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %s: MIWB: configuring for %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %s: MIWB: has been already configured for %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %s: MIWB:Spatial Stills case? prevPort: %@, currPort: %@, preserveSensorIndependtConfigData"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesPlistV4.m %s: [SemStyles] Invalid scene type %u used for querying background tuning, using default tuning parameters."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesPlistV4.m %s: [SemStyles] Warning: Background tuning parameters missing from tuning dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesPlistV4.m %s: [SemStyles] Warning: Foreground tuning parameters missing from tuning dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesPlistV4.m %s: [SemStyles] Warning: Tone bias remap tuning parameters missing from tuning dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesPlistV4.m %s: [SemStyles] Warning: Tuning parameter %@.%@ missing from tuning dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesPlistV4.m %s: [SemStyles] Warning: Tuning parameters for %@ missing from tuning dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesStageV4.m %s: Converted \"%@\" to SSSceneType: %d (0=Indoor, 1=Outdoor, 2=Sunset, 3=Food)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesStageV4.m %s: Couldn't build SemanticStylesShared!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesStageV4.m %s: Unexpected scene type value"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesStageV4.m %s: Unhandled sceneType: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesStageV4.m %s: WARNING: [SemStyles] One or more inference masks are missing - using fallback behavior"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesStageV4.m %s: metalContext nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SemanticStyles/SemanticStylesStageV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SubjectRelighting/SubjectRelightingStageV4.m %s: Couldn't build SubjectRelightingShared!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SubjectRelighting/SubjectRelightingStageV4.m %s: metalContext nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/SubjectRelighting/SubjectRelightingStageV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingBuffersV4.m %s: Unable to lock pixelBuffer for writing\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingBuffersV4.m %s: Warning: Tone curve regularization is skipped, as it is not defined for dual capture modes like CTM for stills."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingBuffersV4.m %s: hazeCorrectionValid: false"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Defaults writes override: applyHRGainDownToLocalGainMapOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Defaults writes override: globalContrastOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Defaults writes override: localContrastOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Defaults writes override: mstmOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Defaults writes override: sffOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Defaults writes override: stfOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Defaults writes override: tcrOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Defaults writes override: utmOverride= %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Error: MSTM disabled due to missing tuning parameters; set 'nrf_trace' default to '1' to see more information"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Error: SFF disabled due to missing tuning parameters; set 'nrf_trace' default to '1' to see more information"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Error: SRL disabled due to missing tuning parameters; set 'nrf_trace' default to '1' to see more information"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Error: SRLv2 is selected but its parameters are missing in tuning plist"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Error: SRLv3 is selected but MSTMv2 parameters are missing in tuning plist"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Error: This version of SRL is not supported"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Error: Tone Curve Regularization disabled due to missing tuning parameters; set 'nrf_trace' default to '1' to see more information"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Error: UTM disabled due to missing parameters"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Overriding applyHRGainDownToLocalGainMap value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Overriding enableGlobalContrast value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Overriding enableLocalContrast value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Overriding enableMSTM value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Overriding enableSFF value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Overriding enableSTF value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Overriding enableTCR value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Overriding enableUTM value; was '%d', now '%d'"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Warning: %@ parameter missing from tuning dictionary"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m %s: Couldn't build ToneMapping shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m %s: Performing black subtraction and adding contrast on HDR FusedBand #0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m %s: Performing black subtraction and global contrast enhance on Tone-mapped band-0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m %s: Received face landmarks: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m %s: STF process failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m %s: Tone mapping Quality: %d enableMSTM %d enableSRL %d enableSTF %d LTMOutputMode_FinalLuma %d chromaGainAdjustmentPower %f inputIsLinear %d chromaBias %f gridScaleFactor {%f,%f} enableUTM %d utmForegroundFactor %f utmBackgroundFactor %f facesCount %d faceLandmarksCount %d spatialCCMTexValid %d ltmBinsX: %d ltmBinsY: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m %s: Unable to create ToneMappingStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m %s: Unsupported outputMode: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingV4.m %s: LTM curves not found."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingV4.m %s: _estimateGainFromMetadata: unexpected AverageLTM.count"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingV4.m %s: hazeCorrectionValid:%s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/ProgressiveBracketing/NRFProgressiveBracketingParametersV4.m %s: AE thumbnail is empty."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/ProgressiveBracketing/NRFProgressiveBracketingParametersV4.m %s: Lens shading profile not found in camera plist"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/ProgressiveBracketing/NRFProgressiveBracketingParametersV4.m %s: Missing processedThumbnail"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/ProgressiveBracketing/NRFProgressiveBracketingParametersV4.m %s: Unsupported NRFProgressiveBracketingMode"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFApplyNetworkWeightsV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkPreprocessV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageTuningParamsV4.m %s: fillRawNoiseModelParameters (long) failed with error (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageTuningParamsV4.m %s: fillRawNoiseModelParameters (ref) failed with error (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageTuningParamsV4.m %s: fillRawNoiseModelParameters (synthLong) failed with error (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: ArtifactCorrectionNetwork is: < %s >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: Cannot prewarm DeepFusionGaussianPyramid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: Cannot prewarm DeepFusionLaplacianPyramid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: RawDF network type < %s > is already loaded."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: RawDFNetworkStage loading < %s > network"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: Setting up network stages for network type < %s >."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: acNetworkPath nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: fusionNetworkPath nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFLanczos.m %s: Failed to prewarm shaders for RawDFLanczos. "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Cannot instantiate FigMetalContext for prewarming"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Do not run registration as there is no SIFR frame provided"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: DraftDemosaicAuxiliaryBuffer availability is: < %d >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to apply YSH stage for frame %d "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to apply mirror stage for frame %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to apply zoom stage for frame %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to init RawDFDetectors"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to obtain LTM metadata for linearMIWBAppliedOutput"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to preprocess reference frame (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to preprocess sifr frame (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to tap-out pre-tonemapped output as linear, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Generate Sythetic Refererence"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Generating Gain Map for Proxy."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Generating Input for Inference."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Invalid class for RawDFProcessor output!!!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Invalid reference frame Index"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: LTM draftDem inputs status: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: MakerNoteFlag = 0x%x"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Multi-frame processing now"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: NRF's memSize: (%.2fMB), usedSizeAll: (%.2fMB), largestOccupiedOffset: (%.2fMB)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: NRFProcessor process: received"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Prep stages for (T: %d ): (LS: %d), (ZM: %d), (MR: %d), (PSTPLC: %d), (ZM: %.1f), (PSS: %d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Preprocess Refererence Frames"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: RawDF compressionLevel: < %d >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: RawDFProcessorV4 _doDeepFusionSytheticReferenceAndProxy calling computeGainMapWithInput"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: RawDFProcessorV4 _doDeepFusionSytheticReferenceAndProxy calling gainmap runWithInput"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: RawDFProcessorV4 _doDeepFusionSytheticReferenceAndProxy successed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: RawDFProxyStage fillFrameProperties failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Regwarp setup dimensions are: ( %d , %d )"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Running _processInferenceImage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: SensorID mismatch for input image and tuning parameters. Input image has: %@,  while tuning plist has:\n %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Setting shared regwarp buffer"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Unable to create RawDFProcessor"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Unexpected fusionMode %d (FIX ME)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Use [NRFProcessor prepareToProcess:prepareDescriptor:] instead of this API"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Using DraftDemosaicAuxiliaryBuffer for registration"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Using provided metal command queue %p"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: [RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _gainMapStage runWithInput failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _generateSyntheticRefererence:... failed with err %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _inputFrames cannot be nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _inputFrames.referenceFrame must not be nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _metalCommandQueue is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _nrfPlist->denoiseAndSharpening = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _nrfPlist->ev0RefDenoising   = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _nrfPlist->evmRefDenoising   = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _nrfPlist->noiseModel           = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _nrfPlist->outputNoiseModel     = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _nrfPlist->syntheticReference          = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _nrfPlist->toneMapping          = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _populateDeepFusionMetadata failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _processInferenceImage failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _regWarpApplyGDC: %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: allocateAndDemosaic SIFR frame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: allocateAndDemosaic reference EV0 frame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: computeGainMapWithLuma failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: createSourceTexturesForInference failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: detectors getDetectorsResultsSync failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: detectors runDetectorsWithRequestedSyntheticReferenceMode failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: draftDemosaicAvailable: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: ev0InputFrame is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: ev0Pyramid allocateWithLabel failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: ev0Pyramid configureWithDescriptor failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: ev0Pyramid generate failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: ev0Pyramid setTexture failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: evmPyramid allocateWithLabel failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: evmPyramid configureWithDescriptor failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: evmPyramid generate failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: fillFrameProperties failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: frame (%d) post dem failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: gainmap computed, notifying delegate with pixelbuffer only, no metadata"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: generateOutputNoiseMapLuma failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: genereteSyntheticReference failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: hasEVM: %d ( %s using EVM )"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: ltcInputFrame is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: memSize (MB):  uncompressed ( %u ), compressed ( %u )"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: mustAllocate = %d; width %d=%d, height %d=%d pixFmt 0x%x=0x%x"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: prepareToProcesss:prepareDescriptor: called for dimensions: (%d x %d), cmiResourceEnabled: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: processInferenceImage failed with error: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: processingType %d, denoiseFusePipelineSize: %lu"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: processingType = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: rawdf.crg: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: resetState is called"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: runWarpUsingTransform failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: rwppUserConfig {\n  numThreads %d\n  numHorizontalBlocks %d\n  numVerticalBlocks %d\n  nccSearchRadius %d\n  nccPatchRadius %d\n  internalBorderSize %d\n  ransacAdaptiveThresholdFactor %f\n  ransacMinMatchingScoreAccepted %f\n  maxNumberOfPyramidLevels %d\n}\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: setting UB fusion reference to %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: setupSTFProcessor failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: shouldProcessFrame failed with err=%d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: tuningMode - %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: useDraftDemosaic: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %s: Loading tuning for: < Port: %@, sensorID: %@, rawDFType: %@ >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %s: syntheticLong readPlist: has failed for mode: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %s: syntheticLongDict is nil for sensorPort: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Binding _auxDraftDemosaicLumaTexture has failed for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Binding _auxDraftDemosaicRGBTexture has failed for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Binding frame uniqueFrameId %d with fmt=%d "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Cannot bind _baseTex for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Failed allocate for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Failed to alloc CMIImagePyramid for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: GDC params already allocated."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Raw input brackets (ColorSpace_Configurable)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Unable to allocate GDC params for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Unable to allocate NRFFrameProperties for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Unable to get GDC params for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Unable to initialize NRFFrameProperties for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: _isVeratileRegroupedPixelFormat = %d for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: _metadata is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: _properties cannot be nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: _properties.meta cannot be nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: _rgbTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: demosaicStage is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: inputFrame.texture cannot be nil for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: loadFrameMetadata failed for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: metal is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: nil inputSampleBuffer for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: pixelBuffer is nil for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: pixelBufferFormat cannot be 0 : %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: rgbTex height does not match base height"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: rgbTex nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: rgbTex unexpected format"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: rgbTex width does not match base width"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: sensorIDNumber cannot be nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: td is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: uniqueFrameId cannot be negative: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/FusionRemixStageV4.m %s: Couldn't build Fusion shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/FusionRemixStageV4.m %s: Giving-up running motion detection because of SIFR exposure"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/FusionRemixStageV4.m %s: HWCSC had to revert to SWCSC (slower) in Fusion!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/FusionRemixStageV4.m %s: Motion scene %s detected, score: %f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/FusionRemixStageV4.m %s: MotionDetection is %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/FusionRemixStageV4.m %s: Running UB fusion reference selection"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/FusionRemixStageV4.m %s: Static scene was detected, score: %f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/FusionRemixStageV4.m %s: Unable to create FuseRemixShaders"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/FusionRemixStageV4.m %s: Unable to create FusionRemixStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/WarpStageV4.m %s: Couldn't build Warp shaders!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/StabilizedImageFusion/WarpStageV4.m %s: self nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: \n==========\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Cannot instantiate FigMetalContext for prewarming"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: ColorSpace_Configurable"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: ColorSpace_Configurable does not support kFigCaptureStreamStillImageCaptureToneCurve_Default"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: ColorSpace_LegacySqrt"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: ColorSpace_LegacyTonemapped"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: ColorSpace_LegacyTonemapped - default"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: DefaultSensorIDs dictionary is NULL, bailing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Dense registration hasn't happened, that's not supposed to happen!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Draft demosaic pixel format not matching RegWarp input format"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Either options dict, tuningParams, tuningParamsPlist, _nrfConfig are NULL, bailing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Entering fusion"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Error getting fusing tuning params for sensor id %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Error: downsampleUpperBandFrame failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Error: fusion failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Error: toneMapBandFrame failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Error: tonemap and denoise failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed Bilateral Grid (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed [rwpp allocateResources:imageHeight:imageFormat:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed _isMetadataConsistentWithFirstFrame (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed _processSIFRandEV0 (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed _processSIFRandEV0IfPossible (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed _processSIFRandRefEV0IfPossible (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed _registerImages (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed denoising (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed homography sanityCheck for bracket index (%d) !! corner (%d, %d) shift distance: (%.2f)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed image registration (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed to addFrame (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed to addFrame with err=(%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed to create defringing tuning for port type %@."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed to parse defringing tuning for port type: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed to prepare inference image (_processInferenceImage): (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed to register non-ref bracket frame: %d (batch=%d, isEVM=%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed to tap-out pre-tonemapped output as linear, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Floating point input brackets (ColorSpace_Configurable)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Invalid class for NRF output!!!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Invalid reference frame Index"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: LTM recalculate on a final image"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: MakerNoteFlag = 0x%x"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Metadata mismatch detected between frames 0 and %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Mismatch: extendFrameROI (w=%d, h=%d) differs from noExtendFrameROI (w=%d, h=%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Multi-frame processing now"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: NRF output's compression footprint is ( %d )"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: NRF's memSize: (%.2fMB), usedSizeAll: (%.2fMB), largestOccupiedOffset: (%.2fMB)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: NRFProcessor process: received"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: No UBParameters found for this portType: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: No defringing tuning parameters for this frame and port type %@, correction will not be applied."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Prepared inference image for SingleImage processing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Processing non-reference frame %d with RegWarp++"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Processing reference frame %d with RegWarp++"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Progressive fusion batch size has been set to %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Received bracketed frame number %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Receiving EV0/pre-bracketing frame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: RegWarp++ reference image numKeypoints %u"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Registering frame %d (batch %d) with Identity matrix"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Running _processInferenceImage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Scaling homography to extended bits since contentExtended is True"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Selected color cube fix type:%d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: SensorID mismatch for input image and tuning parameters. Input image has: %@,  while tuning plist has:\n %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: SensorID not found in plist; no default sensorID specified in plist. Using first sensorID (%@) in plist"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Setting shared regwarp buffer"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Stationary fusion active, RegWarp is disabled"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Total non reference images %d in warping and fusion"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: UB (mode %d) supports up to %d bracket frames, so far %d were passed in!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: UBProcessor compressionLevel: < %d >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Unable to create %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Unexpected processingType = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Unknown _processingType: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Unknown registration method (%d).  Using Identity matrices..."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Unsupported processingType = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Use [NRFProcessor prepareToProcess:prepareDescriptor:] instead of this API"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Use attached auxiliary pixel buffer for RegWarp (frame %d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Use attached auxiliary pixel buffer for RegWarp (reference frame %d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Using provided metal command queue %p"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Warning: failed to generate inference input early. Will try again once all frames are present."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: _metalCommandQueue is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: _nrfPlist->denoiseAndSharpening = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: _nrfPlist->fusion               = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: _nrfPlist->noiseModel           = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: _nrfPlist->outputNoiseModel     = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: _nrfPlist->toneMapping          = %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: _setupFusionConfig failed (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: addFrameWithInputLuma failed with err=(%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: convertHLGToSDRWithInputSampleBuffer failed with err=(%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: doHazeEstimation failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: frame0Props contentExtended ( %d ) != currFrameProps.contentExtended ( %d )"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: gainmap computed, notifying delegate with pixelbuffer only, no metadata"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: greenGhostMitigationMakerNote.status = 0x%x"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: noiseReducedBufferProvided: < %s >, inferenceInputBufferProvided: < %s >, gainMapOutputBufferProvided < %s > , delegateRespondsToInferenceResults: < %s >, enableInference: < %s >"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: pedestalLevel = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: prepareToProcesss:prepareDescriptor: called for dimensions: (%d x %d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: processSingleImageWithMetadata failed with err=%d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: processingType %d, descriptorDimensions: %dx%d denoiseFusePipelineSize: %lu"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: processingType %d, resolutionMultiplier %f, desc.width %d, desc.height %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: processingType = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: resetState is called"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: rwppUserConfig {\n  numThreads %d\n  numHorizontalBlocks %d\n  numVerticalBlocks %d\n  nccSearchRadius %d\n  nccPatchRadius %d\n  internalBorderSize %d\n  ransacAdaptiveThresholdFactor %f\n  ransacMinMatchingScoreAccepted %f\n  maxNumberOfPyramidLevels %d\n}\n"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: setProgressiveBatchSize called with value %d, which is outside the range [2 , %d]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: setting UB fusion reference to %s"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: single image HLG: addFrameWithInputLuma failed with err=(%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: single image HLG: inputImage->chromaTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: single image HLG: inputImage->lumaTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: single image HLG: only 10-bit images are supported"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: single image HLG: only 4:2:0 or 4:2:2 subsampling is supported"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: single image HLG: only YCbCr format is supported"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: single image HLG: only planar pixel buffers are supported"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: single image HLG: td is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: srlStatus = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: startSFDWithInputSampleBuffer failed with err=(%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: toneCurve = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: updateEV0ReferenceFrameIfNecessary failed (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: xformx3x3->coef[%d] = %f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Utilities/FigCaptureLTMLookUpTablesUtilities.m %s: Encountered unsupported value (%d) for FigCaptureLTMLookUpTables.v1.lutsCurveEntryCount"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Utilities/FigCaptureLTMLookUpTablesUtilities.m %s: Encountered unsupported value (%d) for FigCaptureLTMLookUpTables.v2.lutsCurveEntryCount"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Utilities/FigCaptureLTMLookUpTablesUtilities.m %s: Support for FigCaptureLTMLookUpTables V%d struct not yet implemented"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Utilities/FigCaptureLTMLookUpTablesUtilities.m %s: Tried to get CCM pointer from struct without CCM data"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Utilities/FigCaptureLTMLookUpTablesUtilities.m %s: Tried to get LTM curves pointer from CCM struct"
+ "0x0972"
+ "36@0:8i16i20r^(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})24f32"
+ "40@0:8i16i20r^(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})2432"
+ "<%@ %p> dimensions:%@, cmiResourceEnabled:%d"
+ "<<<< CMIImagePyramid >>>> %s: Couldn't build CMIImagePyramid shaders!"
+ "<<<< CMIImagePyramid >>>> %s: Image Pyramid allocation with label: %@"
+ "<<<< CMIImagePyramid >>>> %s: configureWithDescriptor failed, bailing (%d)"
+ "<<<< CMIImagePyramid >>>> %s: desc.levelCount should be non-zero!"
+ "<<<< CMIImagePyramid >>>> %s: desc.type invalid!"
+ "<<<< CMIImagePyramid >>>> %s: desc.width and desc.height should be a multiple of 2^(levelCount-1))!"
+ "<<<< CMIImagePyramid >>>> %s: desc.width and desc.height should be non-zero!"
+ "<<<< CMISoftwareFlashRendering >>>>"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Ambient LSC max gain: %f"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Ambient integration time: %f"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Ambient sensor space conversion. [WhitePoint: R: %.3f, G: %.3f, B: %.3f] [IntegrationTimeScale, %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Ambient spatial white points. [AmbientShadow: Edge0: %.3f,Edge1: %.3f] [StrobeSaturation: Edge0: %.3f,Edge1: %.3f] [StrobeAmbientMinRatio: Edge0: %.3f,Edge1: %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Ambient white balance gains: [R:%.3f, G:%.3f, B:%.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Applying global ambient white balancing."
+ "<<<< CMISoftwareFlashRendering >>>> %s: Applying spatial ambient multi-illuminant white balancing."
+ "<<<< CMISoftwareFlashRendering >>>> %s: Blend spatial white points. [CorrectionStrength: %.3f, SpatialLikelihood: %.3f, CoarseLikelihood: %.3f, AmbientLikelihood: %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: CMIStyleEngineProcessor linear system could not be solved, fallback to SpeedMode transfer"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Calculated full silicon size dimensions: [Width:%d Height:%d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Construct the balanced flash thumbnail from balanced ambient and strobe components."
+ "<<<< CMISoftwareFlashRendering >>>> %s: CoreAnalytics. [CorrectionStrength: Foreground:%d Background:%d] [CorrectionDirection: Foreground:%f Background:%f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Create learning modulation mask. [ModulationWeights: Person: %.3f, Skin: %.3f, SkinGap: %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Create person thumbnail for style transfer learning. [InputMask: Width: %d, Height: %d] [OutputThumbnail: Width: %d, Height: %d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Create skin thumbnail for style transfer learning. [InputMask: Width: %d, Height: %d] [OutputThumbnail: Width: %d, Height: %d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Create source transfer learning thumbnail. [InputSource: Width: %d, Height: %d] [OutputThumbnail: Width: %d, Height: %d, Sharpness:%.3f, SigmaToFilterScale:%.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Create target transfer learning thumbnail. [InputTarget: Width: %d, Height: %d] [OutputThumbnail: Width: %d, Height: %d, Sharpness:%.3f, SigmaToFilterScale:%.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Decompose the strobe component image from the flash and ambient sensor space images"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Failed to get inferences (err:%d)"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Failed to purge resources on the core processor: %@"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Filtering coarse ambient spatial white points. [GaussianSigma: %.3f, SigmaToFilterScale: %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Finished processing."
+ "<<<< CMISoftwareFlashRendering >>>> %s: Flash LSC gains compensation. [FlashLSCMaxGain: %.3f, BaseLSCMaxGain: %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Flash LSC max gain: %f"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Flash Sensor Crop Rectangle. [Sizes: Width:%d Height:%d] [Offsets: X:%d Y:%d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Flash integration time: %f"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Flash sensor space conversion. [WhitePoint: R: %.3f, G: %.3f, B: %.3f] [IntegrationTimeScale: %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Flash white balance gains: [R:%.3f, G:%.3f, B:%.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: GDC Crop Rectangle (Pixel Co-ordinates). [Sizes: Width:%d Height:%d] [Offsets: X:%d Y:%d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Inference generation failed (err:%d)"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Initializing SWFR allocator with size: %lu, descriptor: %@"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Input texture sizes. Ambient: [Width: %d, Height: %d] Flash: [Width: %d, Height: %d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: LSC Crop Rectangle. [Sizes: Width:%d Height:%d] [Offsets: X:%d Y:%d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Metal allocator has already been set up"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Morphological Black Top-Hat for Skin Gap. [KernelSize: %d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: No delegate available to ask for inferences (err:%d)"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Preference tuned ambient white point: [R:.3%f, G:%.3f, B:%.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Preference tuned strobe white point: [R:.3%f, G:%.3f, B:%.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Prepared memory size on the external metal allocator is too small (required:%lu bytes, got:%lu bytes)"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Received QSub capture. Assuming 2x crop."
+ "<<<< CMISoftwareFlashRendering >>>> %s: Register ambient bracket to flash bracket"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Registration of Luma frames. Homography: [%.3f, %.3f, %.3f; %.3f, %.3f, %.3f; %.3f, %.3f, %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: SWFR Crop Rectangle. [Sizes: Width:%d Height:%d] [Offsets: X:%d Y:%d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Setting up SoftwareFlashRendering with provided metal command queue."
+ "<<<< CMISoftwareFlashRendering >>>> %s: Strobe beam profile correction. [CorrectionScale: Min: %.3f, Max: %.3f] [Component: Edge0: %.3f, Edge1: %.3f] [MixFactor: %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Strobe calibration data version not supported."
+ "<<<< CMISoftwareFlashRendering >>>> %s: Strobe white balance gains: [R:%.3f, G:%.3f, B:%.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Style transfer (MainAlgo). [ClippingCorrection: Enabled:%@, Gain:%.3f, Exponent:%.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Style transfer (SpeedMode). [ClippingCorrection: Enabled:%@, Gain:%.3f, Exponent:%.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Style transfer tonal and white balancing changes to full resolution."
+ "<<<< CMISoftwareFlashRendering >>>> %s: Thumbnail ambient frame. [Luma: Width: %d, Height: %d] [Chroma: Width: %d, Height: %d] [ThumbnailOutput: Width: %d, Height: %d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Thumbnail flash frame. [Luma: Width: %d, Height: %d] [Chroma: Width: %d, Height: %d] [ThumbnailOutput: Width: %d, Height: %d]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: Using external metal allocator (size:%lu MB)"
+ "<<<< CMISoftwareFlashRendering >>>> %s: White balance the ambient component. [AmbientWhitePoint: R: %.3f, G: %.3f, B: %.3f] [StrobeWhitePoint: R: %.3f, G: %.3f, B: %.3f] [AmbientWhitePointTuned: R: %.3f, G: %.3f, B: %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: White balance the strobe component. [StrobeWhitePoint: R: %.3f, G: %.3f, B: %.3f]"
+ "<<<< CMISoftwareFlashRendering >>>> %s: addFrame called with unsupported frameType:%d"
+ "<<<< CMISoftwareFlashRendering >>>> %s: externalMemoryDescriptor is nil"
+ "<<<< CMISoftwareFlashRendering >>>> %s: prepareToProcess for %d"
+ "<<<< Deep Fusion Processor(NRF) >>>>"
+ "<<<< Deep Fusion Processor(NRF) >>>> %s: Couldn't build DeepFusionLaplacianPyramidShared shaders!"
+ "<<<< Deep Fusion Processor(NRF) >>>> %s: Unable to create %s"
+ "<<<< DeepFusionProcessor (NRF) >>>>"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: \n==========\n"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: (EV0 motion score frame selection) refHR = %d, otherHR = %d, otherUniqueID = %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Allocating private sharedRegWarpBuffer with %dMB of space"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: DeepFusionProcessor usedSizeAll: (%.2fMB), memSize: (%.2fMB), largestOccupiedOffset: (%.2fMB), Res:( %d x %d )"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: DeepFusionProcessorV4 generateSyntheticReference calling computeGainMapWithInput"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: DeepFusionProcessorV4 generateSyntheticReference calling gainmap runWithInput"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Defaults writes override: _applyColorCube2FixOverride= %s"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Defaults writes override: _applyColorCubeFixOverride= %s"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: DenoiseRemixStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: DraftDemosaicAuxiliaryBuffer availability is: < %d >"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Error: convertRGBToYUV failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to add nonRefEv0Frame %d as an externalAllocator"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to apply YSH stage for frame %d (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to apply mirror stage for frame %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to apply zoom stage for frame %d (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to init RawDFDetectors"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to obtain LTM metadata for linearMIWBAppliedOutput"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to set rgbTex back for frame inputFrame_%d, bailing(%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: FigMetalAllocator WireMemory is < %s >"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: FigMetalAllocator uses < %s > as backend storage"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Generate Sythetic Refererence"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Generating Gain Map for Final."
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Generating Input for Inference."
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Generating Input for Quadra Inference."
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Inferences has not been provided as input, let's obtain the ones we've computed here"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Initializing DeepFusionProcessor allocator with memSize: %lu (%.2fMB), type: %d, compressionLevel: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Initiate Quadra SFD (background)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: LTM calculation result not found in syntheticReference metadata, calculating LTM from scratch."
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: LTM recalculate on a final image"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: LearnedNRNetworkStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Output resolution is: ( %d x %d )"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Post: Final"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Post: SFD"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Prep stages for (T: %d ): (LS: %d), (ZM: %d), (MR: %d), (WRP: %d), (PSTPLC: %d), (ZM: %.1f), (PSS: %d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Prepared memory size on the external metal allocator is too small (required:%lu bytes, got:%lu bytes)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Processing SyntheticReference from scratch, detectors: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Processing SyntheticReference with attached SR metadata"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: PyramidStage_NRF prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RawDFCommon prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RawDFDetectors getMotionDetectionSyncResult failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RawDFDetectors runMotionWithRefFrame failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RawDFFlickerDetectorStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RawDFLumaSharpenStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RawDFNetworkStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RawDFPostDemosaicStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RawDFZoomStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Receiving buffer type < %@ , UniqueFrameId: %d >"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Receiving frame type < %@ , UniqueFrameId: %d >"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RegDense prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RegWarp HistEq < %s >"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: RegWarp++ reference image numKeypoints %u"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Registered inputFrame with UniqueFrameId: %d, hasValidRegistration: %d, numKeypoints: %u (isReference = %d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Regwarp setup dimensions are: ( %d , %d )"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Resetting _allocatorSetupComplete as setupSize: ( %.2fMB ) is greater than _metal.allocator.memSize:  ( %.2fMB )"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Running _processInferenceImage"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Scaling the global homography of the quadra frame due to intermediate zoom applied to the quadra frame. Scalefactor=[%.3f,%.3f]"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: SemanticStylesStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Setting up tunning with sensorID: %@, tuningMode: %{public}@, intermediateZoom: %{public}.2f"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Skip Processing SyntheticReference as it has been provided as input"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Skipping the registration for EVM as _hasEVM says NO"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Skipping the registration for EVM as hompgraphy has been provided"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Step 1 : Finalize Quadra SFD)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Step 2: Finalize Quadra SFD"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: SubjectReglightingStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: ToneMappingStage prewarmShaders failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Use LTM calculated in RawDFProcessor."
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Using Regwarp < %s >"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Using a haze correction recalculated on a final image."
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Using existing sharedRegWarpBuffer with %dMB of space, %dMB required."
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Using external metal allocator (size:%lu MB)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Warning: Allocating new private sharedRegWarpBuffer with %dMB of space, previous buffer was %dMB."
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Warning: Sky mask is missing! Tone Curve Regularization is skipped. Resulting image will have degraded image quality!"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: Warning: metadata practicalFocalLength was not found, trying to override the value !"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: We have applied intermediate zoom to quadra SFD output. We are copying src region=[%ld,%ld,%ld,%ld] to dst texture of size=[%dx%d]"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: [NRFProcessor _allocateRegWarpPPWithWidth] failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: [SoftLTM prepareToProcess:] failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _aggressiveMemoryOptimizations = %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _draftDemosaicStage failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _finalizeQuadraSfdStep1 failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _finalizeQuadraSfdStep2WithInput failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _gainMapStage runWithInput failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _keepReferenceEv0RGB = %d ( [ %lu x %lu ], processingMode = %d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _processInferenceImage failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _regWarpApplyGDC: %s"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: _setupPostConfig isForEnhancedRes:%d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: addFrame frameType < %@ , uniqueFrameId: %d >"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: backgroundLearnedNR final status error (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: calculation LTM on frames failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: computeGainMapWithLuma failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: createSourceTexturesForInference failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: createSourceTexturesForInference for QuadraSFD failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: detectors getDetectorsResultsSync failed with err = %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: detectors runDetectorsWithRequestedSyntheticReferenceMode failed with err = %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: dsrMode: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: ev0Frame.pyramid allocateLevel:%d failed, uniqueFrameId:%d,  bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: ev0Frame.pyramid uniqueFrameId=%d configureWithDescriptor failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: ev0Pyramid allocateLevel:0 failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: ev0Pyramid allocateWithLabel failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: ev0Pyramid configureWithDescriptor failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: ev0Pyramid generate failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: ev0Pyramid setTexture failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: evmPyramid allocateLevel:0 failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: evmPyramid allocateWithLabel failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: evmPyramid configureWithDescriptor failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: evmPyramid generate failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: externalMemoryDescriptor is nil"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: fillFrameProperties failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: frame (%d) checkAndSetRgbTex failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: frame (%d) dem failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: frame (%d) failed to allocated RGB"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: frame (%d) post dem failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: genereteSyntheticReference failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: greenGhostMitigationMakerNote.status = 0x%x"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: hasEVM: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: inputFrame_%d generate failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: longFrame.pyramid allocateLevel:0 failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: longFrame.pyramid uniqueFrameId=%d configureWithDescriptor failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: longFrame_%d generate failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: maskedSkyCubeVersion mismatch"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: nrfMonitorActive: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: outputWeightsPyramid releaseTextureAtLevel:0, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: outputWidth = %d, outputHeight = %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: practicalFocalLength is overriden to 3000"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: practicalFocalLength is overriden to 6000"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: prepareToProcesss:prepareDescriptor: called for dimensions: (%d x %d), processingMode: %d, cmiResourceEnabled: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: processFrameForRegistration failed for nonReference frame"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: processFrameForRegistration failed for reference Frame"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: processInferenceImage failed with error: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: pyramid (outputWeightsPyramid) allocateWithLabel failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: pyramid (outputWeightsPyramid) configureWithDescriptor failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: pyramid (syntheticEV0Pyramid) allocateWithLabel failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: pyramid (syntheticEV0Pyramid) configureWithDescriptor failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: pyramid (syntheticEV0Pyramid) generate failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: pyramid (syntheticEV0Pyramid) setTexture:atLevel: failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: rawDFNetworkStage final status error (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: roi: {x:%f, y:%f, w:%f, h:%f}, imageWidth: %zu, imageHeight: %zu"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: runWarpUsingTransform failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: runWarpUsingTransform inputFrame_%d has failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: runWithReferenceTex Long and syntheticEV0 has failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: rwppUserConfig {\n  numThreads %d\n  numHorizontalBlocks %d\n  numVerticalBlocks %d\n  nccSearchRadius %d\n  nccPatchRadius %d\n  internalBorderSize %d\n  ransacAdaptiveThresholdFactor %f\n  ransacMinMatchingScoreAccepted %f\n  maxNumberOfPyramidLevels %d\n}\n"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: setting DeepFusion fusion reference to %s"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: setupLearnedNRTaskWithInputFrame failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: setupSTFProcessor failed, bailing (%d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: shouldProcessFrame failed with err=%d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: srlVersion mismatch"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: startBackgroundTask failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: staticGyroMotionThreshold for EV0s_LONG : %f, gyroScore: %f, hasMotion: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: staticSceneMotionThreshold for EV0s : %f, motionScore: %f, hasMotion: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: staticSceneMotionThreshold for EV0s_LONG : %f, motionScore: %f, hasMotion: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: syntheticReferenceMode mode is <%s> "
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: tuningMode - %@, binningFactor: %d"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: useDenseReg is: < %d > (hasEVM: %d)"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: waitForBackgroundTaskToComplete failed"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: xformx3x3->coef[%d] = %f"
+ "<<<< LearnedNRMetalStage >>>>"
+ "<<<< LearnedNRMetalStage >>>> %s: GlobalHighlightCompression count is incorrect"
+ "<<<< LearnedNRMetalStage >>>> %s: LearnedNRProcessor initialized"
+ "<<<< LearnedNRMetalStage >>>> %s: Median luma = %0.4f"
+ "<<<< LearnedNRMetalStage >>>> %s: Median luma after average local & global tone curves applied = %0.4f"
+ "<<<< LearnedNRMetalStage >>>> %s: Median luma after average local tone curve applied = %0.4f"
+ "<<<< LearnedNRMetalStage >>>> %s: Modulated noise std = %.2f, addBack = %.2f, addBackBand0 = %.2f, addBackClipToSNR = %.2f, addBackLSCModulation = %.2f, applyLSCModulationWeight = %d, isVersion2 = %d"
+ "<<<< LearnedNRMetalStage >>>> %s: Original totalGain = %0.4f, estimated totalGain = %0.4f"
+ "<<<< LearnedNRMetalStage >>>> %s: Tone curve enum not available"
+ "<<<< LearnedNRMetalStage >>>> %s: Unexpected luma chroma format for buffer %@"
+ "<<<< LearnedNRMetalStage >>>> %s: Warning: Couldn't load tuning parameters from PList"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: GlobalLTMLookUpTable has unexpected size"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: count0 (%f) >= count1 (%f)"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: countM (%f) < count0 (%f)"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: countM (%f) > count1 (%f)"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: failed to estimate median luma. medianCount=%u, globalHist[0]=%u, globalHist[1]=%u"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: globalLTM is NULL"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: globalLTM->lutEntry count has unexpected value"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: header.version = %d"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: localHistogramBinSize = %u"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: localHistograms is NULL"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: ltmLuma out of bounds (%f)"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: medianLuma out of bounds (%f)"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: missing AverageLTM"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: missing GlobalLTMLookUpTable"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: missing LocalHistograms"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: tileGrid.tileCountX = %u"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: unexpected AverageLTM.count"
+ "<<<< LearnedNRMetalStage >>>> %s: _estimateGainFromMetadata: unexpected size = %u"
+ "<<<< LearnedNRMetalStage >>>> %s: lscScale = (%.4f %.4f) lscOffset = (%.4f %.4f)"
+ "<<<< NRF >>>>"
+ "<<<< NRF >>>> %s: Allocate transaction %p"
+ "<<<< NRF >>>> %s: Allocating private sharedRegWarpBuffer with %dMB of space"
+ "<<<< NRF >>>> %s: Basic stats for process: system_time = %d.%06ds"
+ "<<<< NRF >>>> %s: Basic stats for process: user_time = %d.%06ds "
+ "<<<< NRF >>>> %s: Cannot instantiate FigMetalContext for prewarming"
+ "<<<< NRF >>>> %s: Couldn't allocate NRFMonitor!"
+ "<<<< NRF >>>> %s: DefaultSensorIDs dictionary is NULL, bailing"
+ "<<<< NRF >>>> %s: ERROR: A memory exception occured"
+ "<<<< NRF >>>> %s: Either options dict, tuningParams, tuningParamsPlist, _nrfConfig are NULL, bailing"
+ "<<<< NRF >>>> %s: Error getting fusing tuning params for sensor id %@"
+ "<<<< NRF >>>> %s: Failed to create a metal allocator backend with"
+ "<<<< NRF >>>> %s: Failed to create defringing tuning for port type %@."
+ "<<<< NRF >>>> %s: Failed to determine working buffer requirements (err:%d) with prepareDescriptorByProcessingType: %@"
+ "<<<< NRF >>>> %s: Failed to parse defringing tuning for port type: %@"
+ "<<<< NRF >>>> %s: Failed to setup metal allocator backend with: %@ (err:%d)"
+ "<<<< NRF >>>> %s: Invalid class for NRF output!!!"
+ "<<<< NRF >>>> %s: No UBParameters found for this portType: %@"
+ "<<<< NRF >>>> %s: Prepared memory size on the external metal allocator is too small (required:%lu bytes, got:%lu bytes)"
+ "<<<< NRF >>>> %s: Preparing for processing that requires more memory (%lu) than what the processor is currently set up with (%lu)"
+ "<<<< NRF >>>> %s: Preparing for processingType:%d with: %@"
+ "<<<< NRF >>>> %s: Release transaction %p"
+ "<<<< NRF >>>> %s: Required memory size is unexpectedly 0"
+ "<<<< NRF >>>> %s: SensorID not found in plist; no default sensorID specified in plist. Using first sensorID (%@) in plist"
+ "<<<< NRF >>>> %s: Setting up NRF backend allocator with size: %lu (%.2fMB), descriptor: %@"
+ "<<<< NRF >>>> %s: Time stats for process: system_time = %d.%06ds"
+ "<<<< NRF >>>> %s: Time stats for process: user_time = %d.%06ds"
+ "<<<< NRF >>>> %s: UB instances count = %d"
+ "<<<< NRF >>>> %s: UB instances count is %d, should not happen"
+ "<<<< NRF >>>> %s: Unable to create MetalContext"
+ "<<<< NRF >>>> %s: Unable to create NRF"
+ "<<<< NRF >>>> %s: Unable to create NRFPrepareDescriptor"
+ "<<<< NRF >>>> %s: Unable to setup options for %@"
+ "<<<< NRF >>>> %s: Unsupported processingType = %d "
+ "<<<< NRF >>>> %s: Use [NRFProcessor prepareToProcess:prepareDescriptor:] instead of this API"
+ "<<<< NRF >>>> %s: Using existing sharedRegWarpBuffer with %dMB of space, %dMB required."
+ "<<<< NRF >>>> %s: Using external metal allocator (size:%lu MB)"
+ "<<<< NRF >>>> %s: Using externally allocated sharedRegWarpBuffer with %dMB of space"
+ "<<<< NRF >>>> %s: Using provided metal command queue %p"
+ "<<<< NRF >>>> %s: VM stats for host: active = %'lu bytes"
+ "<<<< NRF >>>> %s: VM stats for host: free = %'lu bytes"
+ "<<<< NRF >>>> %s: VM stats for host: inactive = %'lu bytes"
+ "<<<< NRF >>>> %s: VM stats for host: wired = %'lu bytes"
+ "<<<< NRF >>>> %s: VM stats for process: device = %'llu, device_peak = %'llu"
+ "<<<< NRF >>>> %s: VM stats for process: external = %'llu, external_peak = %'llu"
+ "<<<< NRF >>>> %s: VM stats for process: internal = %'llu, internal_peak = %'llu"
+ "<<<< NRF >>>> %s: VM stats for process: page_size = %'d"
+ "<<<< NRF >>>> %s: VM stats for process: phys_footprint = %'llu"
+ "<<<< NRF >>>> %s: VM stats for process: region_count = %'d"
+ "<<<< NRF >>>> %s: VM stats for process: resident_size = %'llu, resident_size_peak = %'llu"
+ "<<<< NRF >>>> %s: VM stats for process: reusable = %'llu, reusable_peak = %'llu"
+ "<<<< NRF >>>> %s: VM stats for process: virtual_size = %'llu"
+ "<<<< NRF >>>> %s: Warning: Allocating new private sharedRegWarpBuffer with %dMB of space, previous buffer was %dMB."
+ "<<<< NRF >>>> %s: _memoryRequirements.sharedMetalBufferSizeRequested is 0"
+ "<<<< NRF >>>> %s: _metalCommandQueue is nil"
+ "<<<< NRF >>>> %s: _nrfConfig->_quadraSupportEnabled = %d"
+ "<<<< NRF >>>> %s: currentMemInfo.sharedMetalBufferSizeRequested is 0 for %d"
+ "<<<< NRF >>>> %s: determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType failed"
+ "<<<< NRF >>>> %s: determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType failed for %d"
+ "<<<< NRF >>>> %s: externalMemoryDescriptor is nil"
+ "<<<< NRF >>>> %s: failed to get required metal allocator memory size"
+ "<<<< NRF >>>> %s: options cmi_dictionary is NULL, bailing"
+ "<<<< NRF >>>> %s: prepareDescriptor (desc) is nil"
+ "<<<< NRF >>>> %s: prepareDescriptor is nil"
+ "<<<< NRF >>>> %s: prepareDescriptorByProcessingType is nil"
+ "<<<< NRF >>>> %s: processingType %d, currentMemInfo.sharedMetalBufferSizeRequested: %lu"
+ "<<<< NRF >>>> %s: resetState is called"
+ "<<<< NRF >>>> %s: rwppUserConfig {\n  numThreads %d\n  numHorizontalBlocks %d\n  numVerticalBlocks %d\n  nccSearchRadius %d\n  nccPatchRadius %d\n  internalBorderSize %d\n  ransacAdaptiveThresholdFactor %f\n  ransacMinMatchingScoreAccepted %f\n  maxNumberOfPyramidLevels %d\n}\n"
+ "<<<< NRFConfig >>>> %s: Allocate MTLBuffer using %s"
+ "<<<< NRFConfig >>>> %s: Allocate resources on setup is %s"
+ "<<<< NRFConfig >>>> %s: Depth is %s"
+ "<<<< NRFConfig >>>> %s: FigMetalAllocator WireMemory is < %s >"
+ "<<<< NRFConfig >>>> %s: NRFConfig %s provided with setup default values"
+ "<<<< NRFConfig >>>> %s: Registration Method = %s"
+ "<<<< NRFConfig >>>> %s: UB IBP loaded in panorama mode"
+ "<<<< NRFConfig >>>> %s: _ctxCreateSynchronization = %ld"
+ "<<<< NRFConfig >>>> %s: _isAsynchronous = %d"
+ "<<<< NRFConfig >>>> %s: _learnedNRProcessingTypeEnabled = %d"
+ "<<<< NRFConfig >>>> %s: defaultOptions = %@"
+ "<<<< NRFConfig >>>> %s: flicker detection is %s"
+ "<<<< NRFConfig >>>> %s: gray ghost detection is %s"
+ "<<<< NRFConfig >>>> %s: learnedNRSubProcessorEnabled = %d"
+ "<<<< NRFConfig >>>> %s: motion detection is %s"
+ "<<<< NRF_SoftLTM >>>>"
+ "<<<< NRF_SoftLTM >>>> %s: Reusing ltmProcessor external backend metal allocator:%p"
+ "<<<< NRF_SoftLTM >>>> %s: ltmProcessor external backend metal allocator currently:%p, attempting to set to:%p"
+ "<<<< NRF_SoftLTM >>>> %s: metal is nil"
+ "<<<< NightModeDenoiseMetalStage >>>>"
+ "<<<< NightModeDenoiseMetalStage >>>> %s: Incorrect offset pixel correction skip config detected"
+ "<<<< NightModeDenoiseMetalStage >>>> %s: NightModeDenoiseMetalStage initialized"
+ "<<<< NightModeFusionMetalStage >>>>"
+ "<<<< NightModeFusionMetalStage >>>> %s: NightModeFusionMetalStage initialized"
+ "<<<< NightModeTripodFusionMetalStage >>>>"
+ "<<<< NightModeTripodFusionMetalStage >>>> %s: NightModeTripodFusionMetalStage initialized"
+ "<<<< PyramidStage_NRF >>>>"
+ "<<<< PyramidStage_NRF >>>> %s: Couldn't build Pyramid shaders!"
+ "<<<< PyramidStage_NRF >>>> %s: Invalid level index! "
+ "<<<< PyramidStage_NRF >>>> %s: Unable to allocate constants"
+ "<<<< PyramidStage_NRF >>>> %s: Unable to create PyramidStage_NRF"
+ "<<<< PyramidStage_NRF >>>> %s: kernelType not valid."
+ "<<<< RawDF - YSH >>>>"
+ "<<<< RawDF - YSH >>>> %s: RawDF Ysh is Disabled!"
+ "<<<< RawDF - Zoom >>>>"
+ "<<<< RawDF - Zoom >>>> %s: applyMirrorWithParams failed"
+ "<<<< RawDF - Zoom >>>> %s: applyZoomWithParams failed"
+ "<<<< RawDF - Zoom >>>> %s: frame: %d , shouldApplyZoom = %d, shouldApplyMirror = %d"
+ "<<<< RawDF - Zoom >>>> %s: metal nil"
+ "<<<< RawDF - Zoom >>>> %s: self nil"
+ "<<<< RawDF - Zoom >>>> %s: updateMetadataAndPropertiesForFrame failed"
+ "<<<< RawDFColorMatch >>>>"
+ "<<<< RawDFColorMatch >>>> %s: colorAdjustment.blueScaleOffset  {scale: %f, offset: %f}"
+ "<<<< RawDFColorMatch >>>> %s: colorAdjustment.greenScaleOffset {scale: %f, offset: %f}"
+ "<<<< RawDFColorMatch >>>> %s: colorAdjustment.redScaleOffset   {scale: %f, offset: %f}"
+ "<<<< RawDFColorMatch >>>> %s: scaleEv0Brightness: %f, scaleEvmBrightness: %f, evmHRGainDownRatio: %f"
+ "<<<< RawDFCommon >>>> %s: Error: convertRGBToYUV failed, bailing (%d)"
+ "<<<< RawDFCommon >>>> %s: Generating Low-Res Luma Chroma Image for Reference Frame."
+ "<<<< RawDFCommon >>>> %s: RegwarpDims ResourceSetupDimensions for : < %d , %d > : ( %d , %d )"
+ "<<<< RawDFCommon >>>> %s: RegwarpDims SurfaceDimensions for : < %d , %d > : ( %d , %d )"
+ "<<<< RawDFCommon >>>> %s: _allocateAndFillLumaChromaImage failed, bailing (%d)"
+ "<<<< RawDFCommon >>>> %s: createSourceTexturesForInference: textures are NOT the same size."
+ "<<<< RawDFCommon >>>> %s: pyramid (sourcePyramid) allocateWithLabel failed, bailing (%d)"
+ "<<<< RawDFCommon >>>> %s: pyramid (sourcePyramid) configureWithDescriptor failed, bailing (%d)"
+ "<<<< RawDFCommon >>>> %s: pyramid (sourcePyramid) generate failed, bailing (%d)"
+ "<<<< RawDFCommon >>>> %s: pyramid (sourcePyramid) setTexture:atLevel: failed, bailing (%d)"
+ "<<<< RawDFDetectors >>>> %s: Forcing FusionMode using (withForcedFusionMode) to mode %d"
+ "<<<< RawDFDetectors >>>> %s: Use motion detection decision: evmEit = %f, evmEitLowerThresh = %f, evmEitUpperThresh %f, useMotionDetector = %d"
+ "<<<< RawDFDetectors >>>> %s: _runMotionDetector didn't run therefore no score is available"
+ "<<<< RawDFDetectors >>>> %s: colorMatchEvmWithLowResEv0 failed, bailing (%d)"
+ "<<<< RawDFDetectors >>>> %s: detectFlicker failed running, bailing (%d)"
+ "<<<< RawDFDetectors >>>> %s: evmColorAdjustment.b{* %f, + %f}"
+ "<<<< RawDFDetectors >>>> %s: evmColorAdjustment.g{* %f, + %f}"
+ "<<<< RawDFDetectors >>>> %s: evmColorAdjustment.r{* %f, + %f}"
+ "<<<< RawDFDetectors >>>> %s: flickerDetection failed getting flicker result, bailing (%d)"
+ "<<<< RawDFDetectors >>>> %s: getMotionDetectionSyncResult failed"
+ "<<<< RawDFDetectors >>>> %s: grayGhostScore = %f (thresh = %f) hasGrayGhost= %d, useMotionDetector = %d, motionScore = %f (thresh = %f) hasMotion = %d, hasFlicker= %d (flickerRatio: %f)"
+ "<<<< RawDFDetectors >>>> %s: grayGhostingDetectionBand = %d"
+ "<<<< RawDFDetectors >>>> %s: metalContext cannot be nil"
+ "<<<< RawDFDetectors >>>> %s: motionDetectionScore is nil"
+ "<<<< RawDFDetectors >>>> %s: motionScore = %f"
+ "<<<< RawDFDetectors >>>> %s: requestedSyntheticReferenceMode is NULL."
+ "<<<< RawDFDetectors >>>> %s: runGrayGhostDetectionWithRGBEvmTexture failed, bailing (%d)"
+ "<<<< RawDFDetectors >>>> %s: srMode is RawDFSyntheticReferenceMode_DeepShadowRecovery"
+ "<<<< RawDFDetectors >>>> %s: srMode is RawDFSyntheticReferenceMode_HighlightRecovery"
+ "<<<< RawDFDetectors >>>> %s: startMotionDetection failed, bailing (%d)"
+ "<<<< RawDFDetectors >>>> %s: useDraftDemosaic = %d"
+ "<<<< RawDFDownsample >>>>"
+ "<<<< RawDFDownsample >>>> %s: Running RawDFDownsampleStage generateWithInputTexture"
+ "<<<< RawDFDownsample >>>> %s: inputTexture:(%d, %d)"
+ "<<<< RawDFDownsample >>>> %s: request: downsampleLevel = %d, type = %d, label = %s"
+ "<<<< RawDFFlickerDetector >>>>"
+ "<<<< RawDFFlickerDetector >>>> %s: flickerCount: neg:%u pos:%u sum:%u countBalance:%f"
+ "<<<< RawDFInferenceGen >>>>"
+ "<<<< RawDFInferenceGen >>>> %s: Running _processInferenceImage"
+ "<<<< RawDFProxy >>>>"
+ "<<<< RawDFProxy >>>> %s: Running RawDFProxyStage generateNoiseMap"
+ "<<<< RawDFProxy >>>> %s: fillRawNoiseModelParameters (ev0) failed, bailing (%d)"
+ "<<<< RawDFProxy >>>> %s: fillRawNoiseModelParameters (evm) failed, bailing (%d)"
+ "<<<< RawDFSynLong >>>>"
+ "<<<< RawDFSynLong >>>> %s: Allocating fusion weights (outputWeightsPyramid not provided)"
+ "<<<< RawDFSynLong >>>> %s: _fillConstants failed."
+ "<<<< RawDFSynLong >>>> %s: _fillConstantsForBand failed."
+ "<<<< RawDFSynLong >>>> %s: enableShadowBoost = %d"
+ "<<<< RawDFSynLong >>>> %s: ev0Count = %d"
+ "<<<< RawDFSynLong >>>> %s: fillRawNoiseModelParameters (ev0) failed, bailing (%d)"
+ "<<<< RawDFSynLong >>>> %s: fillRawNoiseModelParameters (long) failed, bailing (%d)"
+ "<<<< RawDFSynLong >>>> %s: kernelRawDFFuseEv0s thread group size (%d, %d) is greater than supported maximum, reducing..."
+ "<<<< RawDFSynLong >>>> %s: reduced kernelRawDFFuseEv0s thread group size (%d, %d)."
+ "<<<< RawDFSynLong >>>> %s: syntheticEv0WeightsPyramid is nil; proceeding without prior fusion weights"
+ "<<<< RawDFSynRef >>>>"
+ "<<<< RawDFSynRef >>>> %s: DSR.dispatch[%d] {w, h} = {%d, %d}, groups = {%d, %d} threads = {%d, %d} extra = {%d, %d} lm.size = %d, maxThreads = %d"
+ "<<<< RawDFSynRef >>>> %s: RawDFSyntheticReferenceStage"
+ "<<<< RawDFSynRef >>>> %s: Running RawDFSyntheticReferenceStage _doDeepShadowRecovery"
+ "<<<< RawDFSynRef >>>> %s: Running RawDFSyntheticReferenceStage _doHighlightRecovery"
+ "<<<< RawDFSynRef >>>> %s: _doHighlightRecovery failed, bailing (%d)"
+ "<<<< RawDFSynRef >>>> %s: ev0Properties NULL"
+ "<<<< RawDFSynRef >>>> %s: evmEv0RelativeBrightness = %f"
+ "<<<< RawDFSynRef >>>> %s: evmProperties NULL"
+ "<<<< RawDFSynRef >>>> %s: fillRawNoiseModelParameters (ev0) failed, bailing (%d)"
+ "<<<< RawDFSynRef >>>> %s: fillRawNoiseModelParameters (evm) failed, bailing (%d)"
+ "<<<< RawDFSynRefCRG >>>> %s: CRG plan failed: %@."
+ "<<<< RawDFSynRefCRG >>>> %s: RawDFSyntheticReferenceStageCRG"
+ "<<<< RawDFSynRefCRG >>>> %s: Unable to allocate constants."
+ "<<<< RawDFSynRefCRG >>>> %s: Unable to create RawDFSyntheticReferenceStage."
+ "<<<< RawDFSynRefCRG >>>> %s: _passes"
+ "<<<< RawDFSynRefCRG >>>> %s: _shaders nil."
+ "<<<< RawDFSynRefCRG >>>> %s: dsr nil"
+ "<<<< RawDFSynRefCRG >>>> %s: dsr prepareWithFrameProperties failed (%d)."
+ "<<<< RawDFSynRefCRG >>>> %s: dsrUp nil."
+ "<<<< RawDFSynRefCRG >>>> %s: ev0 nil"
+ "<<<< RawDFSynRefCRG >>>> %s: ev0 nil."
+ "<<<< RawDFSynRefCRG >>>> %s: ev0Ext nil"
+ "<<<< RawDFSynRefCRG >>>> %s: ev0Properties NULL"
+ "<<<< RawDFSynRefCRG >>>> %s: ev0Pyramid nil"
+ "<<<< RawDFSynRefCRG >>>> %s: ev0PyramidCRG nil"
+ "<<<< RawDFSynRefCRG >>>> %s: ev0Up nil."
+ "<<<< RawDFSynRefCRG >>>> %s: evm nil"
+ "<<<< RawDFSynRefCRG >>>> %s: evm nil."
+ "<<<< RawDFSynRefCRG >>>> %s: evmExt nil"
+ "<<<< RawDFSynRefCRG >>>> %s: evmProperties NULL"
+ "<<<< RawDFSynRefCRG >>>> %s: evmPyramid nil"
+ "<<<< RawDFSynRefCRG >>>> %s: evmPyramidCRG nil"
+ "<<<< RawDFSynRefCRG >>>> %s: evmUp nil."
+ "<<<< RawDFSynRefCRG >>>> %s: execution nil"
+ "<<<< RawDFSynRefCRG >>>> %s: fillRawNoiseModelParameters (ev0) failed, bailing (%d)"
+ "<<<< RawDFSynRefCRG >>>> %s: fillRawNoiseModelParameters (evm) failed, bailing (%d)"
+ "<<<< RawDFSynRefCRG >>>> %s: frameProperties NULL"
+ "<<<< RawDFSynRefCRG >>>> %s: fusionWeights nil."
+ "<<<< RawDFSynRefCRG >>>> %s: graph nil"
+ "<<<< RawDFSynRefCRG >>>> %s: groupNRF nil"
+ "<<<< RawDFSynRefCRG >>>> %s: groupRawDF nil"
+ "<<<< RawDFSynRefCRG >>>> %s: groupSR nil"
+ "<<<< RawDFSynRefCRG >>>> %s: hr nil"
+ "<<<< RawDFSynRefCRG >>>> %s: hr prepareWithFrameProperties failed (%d)."
+ "<<<< RawDFSynRefCRG >>>> %s: kernelRawDFDeepShadowRecovery nil."
+ "<<<< RawDFSynRefCRG >>>> %s: kernelRawDFHighlightRecovery nil."
+ "<<<< RawDFSynRefCRG >>>> %s: lscGainsTex nil"
+ "<<<< RawDFSynRefCRG >>>> %s: maxTotalThreadsPerThreadgroup (%d) < required (%d)."
+ "<<<< RawDFSynRefCRG >>>> %s: metal NULL."
+ "<<<< RawDFSynRefCRG >>>> %s: mode (%d) not valid."
+ "<<<< RawDFSynRefCRG >>>> %s: noise nil"
+ "<<<< RawDFSynRefCRG >>>> %s: noiseDivisorOutputTex nil"
+ "<<<< RawDFSynRefCRG >>>> %s: output nil"
+ "<<<< RawDFSynRefCRG >>>> %s: output nil."
+ "<<<< RawDFSynRefCRG >>>> %s: params nil."
+ "<<<< RawDFSynRefCRG >>>> %s: pass %d nil"
+ "<<<< RawDFSynRefCRG >>>> %s: passes nil"
+ "<<<< RawDFSynRefCRG >>>> %s: planConstraints nil"
+ "<<<< RawDFSynRefCRG >>>> %s: renderAll (%d) failed."
+ "<<<< RawDFSynRefCRG >>>> %s: shaders nil."
+ "<<<< RawDFSynRefCRG >>>> %s: syntheticReferenceOutputTex nil"
+ "<<<< RawDFSynRefCRG >>>> %s: textureArgs nil."
+ "<<<< RawDFSynRefCRG >>>> %s: textureArgsFinal nil."
+ "<<<< RawDFSynRefCRG >>>> %s: textureArgsMain nil."
+ "<<<< RawDFSynRefCRG >>>> %s: textureArgsUp nil."
+ "<<<< RawDFSynRefCRG >>>> %s: top nil"
+ "<<<< RawDFSynRefCRG >>>> %s: tuning nil"
+ "<<<< RawDFSynRefCRG >>>> Fig"
+ "<<<< RawNightMode >>>>"
+ "<<<< RawNightMode >>>> %s: Calculated lscNormalizationDims: (%d, %d)"
+ "<<<< RawNightMode >>>> %s: Cannot instantiate FigMetalContext for prewarming"
+ "<<<< RawNightMode >>>> %s: Computed RFS Index = %u"
+ "<<<< RawNightMode >>>> %s: DNR bias (RGB) to be corrected: (%f, %f, %f)"
+ "<<<< RawNightMode >>>> %s: DNR network used: %@"
+ "<<<< RawNightMode >>>> %s: Fusion network used: %@"
+ "<<<< RawNightMode >>>> %s: Initializing RawNightModeProcessor metal allocator descriptor with size:%lu, compressionLevel:%d"
+ "<<<< RawNightMode >>>> %s: Input pixel format mismatch. Got:%c%c%c%c. Expected:%c%c%c%c"
+ "<<<< RawNightMode >>>> %s: Invalid class for NRF output!!!"
+ "<<<< RawNightMode >>>> %s: LTM recalculate on a final image"
+ "<<<< RawNightMode >>>> %s: NULL sbuf provided"
+ "<<<< RawNightMode >>>> %s: Output pixel format mismatch. Got:%c%c%c%c. Expected:%c%c%c%c"
+ "<<<< RawNightMode >>>> %s: Person/Skin/Hair mask textures not detected. DISABLING SEMANTIC ADDBACK FOR BODY REGION"
+ "<<<< RawNightMode >>>> %s: Raw Night Mode output's compression footprint is ( %d )"
+ "<<<< RawNightMode >>>> %s: Raw input brackets (ColorSpace_Configurable)"
+ "<<<< RawNightMode >>>> %s: RawNM GGM maskAverage = %.5f"
+ "<<<< RawNightMode >>>> %s: RawNM GGM will not continue, as the detected region is too large to repair."
+ "<<<< RawNightMode >>>> %s: Registration disabled, not using dense warping"
+ "<<<< RawNightMode >>>> %s: Resetting Raw Night Mode processor"
+ "<<<< RawNightMode >>>> %s: Skin mask textures not detected. DISABLING SEMANTIC ADDBACK FOR SKIN REGION"
+ "<<<< RawNightMode >>>> %s: Sky mask textures not detected. DISABLING SEMANTIC ADDBACK FOR SKY REGION"
+ "<<<< RawNightMode >>>> %s: Unable to allocate NRFFrameProperties"
+ "<<<< RawNightMode >>>> %s: Unable to allocate gdcParams"
+ "<<<< RawNightMode >>>> %s: Unable to create RawNightModeProcessor"
+ "<<<< RawNightMode >>>> %s: Unable to initialize NRFFrameProperties"
+ "<<<< RawNightMode >>>> %s: Using provided metal command queue %p"
+ "<<<< RawNightMode >>>> %s: _maskMB is nil, which means multi-frame detection was never performed (because all non-reference frames were either too blurry or didn't register correctly),  so inpainting will be skipped too."
+ "<<<< RawNightMode >>>> %s: _metalCommandQueue is nil"
+ "<<<< RawNightMode >>>> %s: addCompletionHandlerForOutputFrame; cmdBuf is nil"
+ "<<<< RawNightMode >>>> %s: cameraInfoByPortType is nil"
+ "<<<< RawNightMode >>>> %s: constrainedRegCalcWarpedMismatch2D.maxTotalThreadsPerThreadgroup insufficient"
+ "<<<< RawNightMode >>>> %s: constrainedRegCreatePriorShifts.maxTotalThreadsPerThreadgroup insufficient"
+ "<<<< RawNightMode >>>> %s: constrainedRegDownsample2D.maxTotalThreadsPerThreadgroup insufficient"
+ "<<<< RawNightMode >>>> %s: constrainedRegWarpDownsample2D.maxTotalThreadsPerThreadgroup insufficient"
+ "<<<< RawNightMode >>>> %s: metal nil"
+ "<<<< RawNightMode >>>> %s: sbuf missing metadata"
+ "<<<< RawNightMode >>>> %s: sbuf missing pixel buffer"
+ "<<<< RawNightMode >>>> %s: self nil"
+ "<<<< RawNightMode >>>> %s: width: %d, height: %d, sharedMetalBufferSize: %lu"
+ "<<<< RawProcFrames >>>> %s: \n==========\n"
+ "<<<< RawProcFrames >>>> %s: %{private}@ registerImages < %{private}s(%{public}d) >"
+ "<<<< RawProcFrames >>>> %s: Adding Long frame input to inputFrames %d"
+ "<<<< RawProcFrames >>>> %s: Adding Reference frame input to inputFrames %d"
+ "<<<< RawProcFrames >>>> %s: Adding SIFR frame input to inputFrames %d"
+ "<<<< RawProcFrames >>>> %s: Cannot bind regWarpInputTex"
+ "<<<< RawProcFrames >>>> %s: Failed to init CMIDraftDemosaicStage"
+ "<<<< RawProcFrames >>>> %s: Metadata mismatch detected between frames 0 and %d"
+ "<<<< RawProcFrames >>>> %s: Mismatch: (frame0Props->meta.sensorID == currFrameProps->meta.sensorID)"
+ "<<<< RawProcFrames >>>> %s: Processing non-reference frame %d with RegWarp++"
+ "<<<< RawProcFrames >>>> %s: Processing reference frame %d with RegWarp++"
+ "<<<< RawProcFrames >>>> %s: RawProcFrames didn't store uniqueFrameId: %{public}d"
+ "<<<< RawProcFrames >>>> %s: RegWarp++ reference image numKeypoints %u"
+ "<<<< RawProcFrames >>>> %s: Soft Failure: failed to register non-ref bracket frame: %d (batch=%d, isEVM=%d)"
+ "<<<< RawProcFrames >>>> %s: Total non reference images %d in warping and fusion"
+ "<<<< RawProcFrames >>>> %s: Unable to update reference frame ROI"
+ "<<<< RawProcFrames >>>> %s: _frames is nil"
+ "<<<< RawProcFrames >>>> %s: _regWarpInput cannot be nil"
+ "<<<< RawProcFrames >>>> %s: _registrationPipelineRWPP cannot be nil"
+ "<<<< RawProcFrames >>>> %s: bound _regWarpInputTex { %d, %d }"
+ "<<<< RawProcFrames >>>> %s: metal is nil"
+ "<<<< RawProcFrames >>>> %s: no frames have been registered!"
+ "<<<< RawProcFrames >>>> %s: referenceFrameIndex cannot be set to a negative value"
+ "<<<< RawProcFrames >>>> %s: registration failed at setReferenceFrameIndex"
+ "<<<< RawProcFrames >>>> %s: xformx3x3->coef[%d] = %f"
+ "<<<< RawProcFrames >>>> Fig"
+ "<<<< RegPyrFusion >>>>"
+ "<<<< RegPyrFusion >>>> %s: Cannot normalize homography, something is really bad going on!"
+ "<<<< RegPyrFusion >>>> %s: Couldn't build Fusion shaders!"
+ "<<<< RegPyrFusion >>>> %s: Invalid dimensions provided to RegPyrFusion prepare"
+ "<<<< RegPyrFusion >>>> %s: Unable to create metal pipeline state using fragment shader: %@ "
+ "<<<< RegPyrFusion >>>> %s: Unable to init 'RegPyrFusionShaders'"
+ "<<<< RegPyrFusion >>>> %s: Unable to setup Pyramid scaler parameters. Most probably something is wrong with input Calibration data"
+ "<<<< RegPyrFusion >>>> %s: constantValues is nil"
+ "<<<< RegPyrFusion >>>> %s: fusionWithCommandBuffer failed"
+ "<<<< RegPyrFusion >>>> %s: selectionWithCommandBuffer failed"
+ "<<<< SoftISP >>>>"
+ "<<<< SoftISP >>>> %s:  ---  RBG Gains = [         %5d , %5d , %5d ] ( computed ) ---\n"
+ "<<<< SoftISP >>>> %s:  --- AWB computed gains application point ---\n"
+ "<<<< SoftISP >>>> %s:  --- GRBG Gains = [ %5d , %5d , %5d , %5d ] ( from registers ) ---\n"
+ "<<<< SoftISP >>>> %s:  --- SoftISP RawMBNR: Deriving LSC from CameraInfoByPortType ---\n"
+ "<<<< SoftISP >>>> %s:  --- SoftISP RawMBNR: Deriving LSC from lscPixelBuffer ---\n"
+ "<<<< SoftISP >>>> %s:  trace"
+ "<<<< SoftISP >>>> %s:  trace : hrEnabled = %d"
+ "<<<< SoftISP >>>> %s: %@ is nil"
+ "<<<< SoftISP >>>> %s: %s generated [%d] combinations (from function constants) "
+ "<<<< SoftISP >>>> %s: Allocating %d bytes for scratch memory."
+ "<<<< SoftISP >>>> %s: Allocating outputTex with uniqueID: %d >"
+ "<<<< SoftISP >>>> %s: Applying gain value of < %.2f > to draftDemosaic output"
+ "<<<< SoftISP >>>> %s: Auxiliary type not supported. Skipping"
+ "<<<< SoftISP >>>> %s: Bad input pixel format: %d"
+ "<<<< SoftISP >>>> %s: Bad output pixel format: %d"
+ "<<<< SoftISP >>>> %s: Black level shading correction is %@"
+ "<<<< SoftISP >>>> %s: Building line base-index buffer."
+ "<<<< SoftISP >>>> %s: CameraInfo not found"
+ "<<<< SoftISP >>>> %s: Can't determine MTLPixelFormats for binding to CVPixelBuffer - unsupported input pixel format = %c%c%c%c"
+ "<<<< SoftISP >>>> %s: Capture SensorID (0x%04X) doesn't match the SensorID in the ModuleConfig (0x%04X)"
+ "<<<< SoftISP >>>> %s: Coeff value (%d) out of 12-bit range."
+ "<<<< SoftISP >>>> %s: Compensating xtalk map gain from QSub to QSum."
+ "<<<< SoftISP >>>> %s: Compensating xtalk map gain from QSum to QSub."
+ "<<<< SoftISP >>>> %s: Could not get internal AWB metadata for MIWB: miwbErr = %d. MIWB won't be run."
+ "<<<< SoftISP >>>> %s: Decision path 1"
+ "<<<< SoftISP >>>> %s: Decision path 2"
+ "<<<< SoftISP >>>> %s: Decision path 2.1"
+ "<<<< SoftISP >>>> %s: Decision path 2.2"
+ "<<<< SoftISP >>>> %s: Decision path 3"
+ "<<<< SoftISP >>>> %s: Decision path 4"
+ "<<<< SoftISP >>>> %s: Decision path 4.1"
+ "<<<< SoftISP >>>> %s: Decision path 4.1b"
+ "<<<< SoftISP >>>> %s: Decision path 4.2"
+ "<<<< SoftISP >>>> %s: Decision path 4.2.1"
+ "<<<< SoftISP >>>> %s: Decision path 4.2.2"
+ "<<<< SoftISP >>>> %s: Decision path 5"
+ "<<<< SoftISP >>>> %s: Decision path 5.1"
+ "<<<< SoftISP >>>> %s: Decision path 5.2"
+ "<<<< SoftISP >>>> %s: Decision path 5.3"
+ "<<<< SoftISP >>>> %s: Decision path 5.4"
+ "<<<< SoftISP >>>> %s: Decision path 6"
+ "<<<< SoftISP >>>> %s: Decision path 6.1"
+ "<<<< SoftISP >>>> %s: Decision path 6.2"
+ "<<<< SoftISP >>>> %s: Decision path 7"
+ "<<<< SoftISP >>>> %s: Decision path 7.1"
+ "<<<< SoftISP >>>> %s: Decision path 7.1.1"
+ "<<<< SoftISP >>>> %s: Decision path 7.1.2"
+ "<<<< SoftISP >>>> %s: Downstream stage input frame validation failed"
+ "<<<< SoftISP >>>> %s: Draft Demosaic is enabled. Input texture size: (%u, %u)"
+ "<<<< SoftISP >>>> %s: Error of computed noise model using metadata, max: %f, max (relative): %f%%"
+ "<<<< SoftISP >>>> %s: Failed to allocate 10To8 LUT"
+ "<<<< SoftISP >>>> %s: Failed to allocate 8to10 LUT"
+ "<<<< SoftISP >>>> %s: Failed to allocate 8to12 LUT"
+ "<<<< SoftISP >>>> %s: Failed to allocate CMIWarpStage"
+ "<<<< SoftISP >>>> %s: Failed to allocate adaptiveGradPushD LUT"
+ "<<<< SoftISP >>>> %s: Failed to allocate adaptiveGradPushHV LUT"
+ "<<<< SoftISP >>>> %s: Failed to allocate internal stage metal"
+ "<<<< SoftISP >>>> %s: Failed to allocate metal shaders"
+ "<<<< SoftISP >>>> %s: Failed to allocate noiseSuppressStrength LUT"
+ "<<<< SoftISP >>>> %s: Failed to create AWB instance"
+ "<<<< SoftISP >>>> %s: Failed to create H13FastSashimiDisparityPipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13FastSashimiPipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_QBin_Sushi_Fast_RawMBNR_LTM_1C pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_QBin_Sushi_Fast_RawMBNR_YUV pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_Fp16 QDEM RawMBNR LTM pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_Fp16 pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_LTM pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_RawMBNR pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_RawMBNR_Fp16 pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_RawMBNR_LTM_1C pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_RawMBNR_YUV pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_RawMBNR_YUVLTM pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_RawMBNR_YUVLTM_Debug pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_RawMBNR_YUV_GDC pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_RegWarp pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_YUV pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create H13_Sushi_Fast_YUV_Quadra pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create RawNightMode pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create SoftISPPipelineType_H13_QBin_Sushi_Fast_RawMBNR_LTM_YUV pipeline"
+ "<<<< SoftISP >>>> %s: Failed to create _blackLevelShadingThumbnail"
+ "<<<< SoftISP >>>> %s: Failed to create applyLTMStage"
+ "<<<< SoftISP >>>> %s: Failed to create bayerProcStage"
+ "<<<< SoftISP >>>> %s: Failed to create canvasStage"
+ "<<<< SoftISP >>>> %s: Failed to create computeLTMStage"
+ "<<<< SoftISP >>>> %s: Failed to create convertStage"
+ "<<<< SoftISP >>>> %s: Failed to create convertToFp16Stage"
+ "<<<< SoftISP >>>> %s: Failed to create convertToU16Stage"
+ "<<<< SoftISP >>>> %s: Failed to create demYUVStage"
+ "<<<< SoftISP >>>> %s: Failed to create disparityStage"
+ "<<<< SoftISP >>>> %s: Failed to create gdcYUVStage"
+ "<<<< SoftISP >>>> %s: Failed to create lumaSharpeningStage"
+ "<<<< SoftISP >>>> %s: Failed to create opcStage"
+ "<<<< SoftISP >>>> %s: Failed to create postDemProcStage"
+ "<<<< SoftISP >>>> %s: Failed to create rawMBNRStage"
+ "<<<< SoftISP >>>> %s: Failed to create rawScaleStage"
+ "<<<< SoftISP >>>> %s: Failed to create regWarpStage"
+ "<<<< SoftISP >>>> %s: Failed to create texDesc"
+ "<<<< SoftISP >>>> %s: Failed to demosaic input texture into Y and UV outputs"
+ "<<<< SoftISP >>>> %s: Failed to determine first pixel for versatile format"
+ "<<<< SoftISP >>>> %s: Failed to get LTMProcessor class"
+ "<<<< SoftISP >>>> %s: Failed to get ThumbnailData"
+ "<<<< SoftISP >>>> %s: Failed to get analogGain"
+ "<<<< SoftISP >>>> %s: Failed to get biasValues"
+ "<<<< SoftISP >>>> %s: Failed to get config for %@ from pipeline type %d"
+ "<<<< SoftISP >>>> %s: Failed to get exposureTime"
+ "<<<< SoftISP >>>> %s: Failed to get maxValue"
+ "<<<< SoftISP >>>> %s: Failed to get minValue"
+ "<<<< SoftISP >>>> %s: Failed to get temperature"
+ "<<<< SoftISP >>>> %s: Failed to get thumbnail height"
+ "<<<< SoftISP >>>> %s: Failed to get thumbnail width"
+ "<<<< SoftISP >>>> %s: Failed to init _car"
+ "<<<< SoftISP >>>> %s: Failed to init _flareDetectionResultBuffer"
+ "<<<< SoftISP >>>> %s: Failed to initialize SSC"
+ "<<<< SoftISP >>>> %s: Failed to register non-reference frame: %llu"
+ "<<<< SoftISP >>>> %s: Failed to run post-demosaic proc stage"
+ "<<<< SoftISP >>>> %s: FigCaptureStreamDefectivePixels version = %d."
+ "<<<< SoftISP >>>> %s: FigMetalAllocator WireMemory is < %s >"
+ "<<<< SoftISP >>>> %s: Fill buffers."
+ "<<<< SoftISP >>>> %s: Filtered defects count doesn't match expected value. Defects are potentially not in scan order. Use unfiltered defect locations."
+ "<<<< SoftISP >>>> %s: Fixed pattern noise reduction is %@, Scaling Factor: %f"
+ "<<<< SoftISP >>>> %s: FlareDetection is < %@ >"
+ "<<<< SoftISP >>>> %s: FocusPixelMap V1"
+ "<<<< SoftISP >>>> %s: FocusPixelMap V2"
+ "<<<< SoftISP >>>> %s: GDC is applied to Draft Demosaic pixel buffer"
+ "<<<< SoftISP >>>> %s: GOC gains updated with AWB results"
+ "<<<< SoftISP >>>> %s: Generating V1 CIC table with OIS Adaptation"
+ "<<<< SoftISP >>>> %s: Generating V1 LSC table with OIS Adaptation"
+ "<<<< SoftISP >>>> %s: GrGbGNU is < %@ >, grGbGnuMode: %d"
+ "<<<< SoftISP >>>> %s: H13CommonLTM::ltmDownsampleRGB_2x is nil"
+ "<<<< SoftISP >>>> %s: H13Fast::convertI17ToF16 is nil"
+ "<<<< SoftISP >>>> %s: H13Fast::convertScaledToI17 is nil"
+ "<<<< SoftISP >>>> %s: H13Fast::convertToU16 is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::_hrdGnuCorrection failed"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::calcuateFlareDetectionResult is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::generateFlareMapPerThreadgroup is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hoclBin failed"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrGenerateHuemapThumbnails is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrHighlightRecoveryQuadra_FirstPixB is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrHighlightRecoveryQuadra_FirstPixGB is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrHighlightRecoveryQuadra_FirstPixGR is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrHighlightRecoveryQuadra_FirstPixR is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrHighlightRecovery_FirstPixB is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrHighlightRecovery_FirstPixGB is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrHighlightRecovery_FirstPixGR is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrHighlightRecovery_FirstPixR is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrPreprocessDSLUT is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrdGnuCorrectionQuadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrdRedBlueFilter is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::hrdRedBlueFilterQuadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::huemap is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::huemapMotionCompensation is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::huemapThumbnailGeneration0 is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::huemapThumbnailGeneration0Quadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::preHR failed"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::preHRQuadra failed"
+ "<<<< SoftISP >>>> %s: H13FastBayerProc::summarizeFlareMap is nil"
+ "<<<< SoftISP >>>> %s: H13FastCanvas::clone failed"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::convertToSingleChannel is nil"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::ispQDEMGreenStage is nil"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::ispQDEMRedBlueStage (RGB) is nil"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::ispQDEMRedBlueStage (YCbCr) is nil"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::zimmerDemosaicStage_Bayer_RB_RGB is nil"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::zimmerDemosaicStage_Stacked_BGGR_RGB is nil"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::zimmerDemosaicStage_Stacked_BGGR_YCbCr is nil"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::zimmerDemosaicStage_Stacked_RGGB_RGB is nil"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::zimmerDemosaicStage_Stacked_RGGB_YCbCr is nil"
+ "<<<< SoftISP >>>> %s: H13FastDemosaic::zimmerDemosaicYUVPackStage is nil"
+ "<<<< SoftISP >>>> %s: H13FastLTM::ltmDemosaic is nil"
+ "<<<< SoftISP >>>> %s: H13FastLTM::ltmDemosaicQuadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastLTM::ltmDemosaicQuadra4Channel is nil"
+ "<<<< SoftISP >>>> %s: H13FastLTM::ltmDownsampleYCbCrToRGB is nil"
+ "<<<< SoftISP >>>> %s: H13FastLumaSharpening::lumaSharpening failed"
+ "<<<< SoftISP >>>> %s: H13FastOutlierPixelCorrection::outlierPixelCorrection failed"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_RGB_to_YCC is nil"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_YCC4202YUV420 is nil"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_chromaSuppression_CCUV (2x) is nil"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_chromaSuppression_CCUV is nil"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_chromaSuppression_RGB is nil"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_chromaSuppression_filterQCC (2x) is nil"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_chromaSuppression_filterQCC is nil"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_directionalLowpass_RGB is nil"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_directionalLowpass_YCbCr is nil"
+ "<<<< SoftISP >>>> %s: H13FastPostDemosaicProc::postDemosaicProcStage_dotFix failed"
+ "<<<< SoftISP >>>> %s: H13FastRawMBNR::denoiseBayerAndStepDown failed"
+ "<<<< SoftISP >>>> %s: H13FastRawMBNR::denoiseChromaAndStepDown failed"
+ "<<<< SoftISP >>>> %s: H13FastRawMBNR::denoiseChromaAndStepDownAndRegenBayer failed"
+ "<<<< SoftISP >>>> %s: H13FastRawMBNR::downscale2x is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawMBNR::lowPassBayer failed"
+ "<<<< SoftISP >>>> %s: H13FastRawMBNR::lowPassBayerAndDownscale2x failed"
+ "<<<< SoftISP >>>> %s: H13FastRawMBNR::noiseLookup is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawMBNR::regenerateBayer failed"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::advBLESTApplyCorrection is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::advBLESTCalcMeanCorrection is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::advBLESTFilterEstimate is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::advBLESTFilterMeans is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::advBLESTHorizontalMeanBL is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::advBLESTInitialEstimate is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::advBLESTUpdateCorrection is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::advBLESTVerticalMeanBL is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::blackLevelCorrection is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::blackLevelEstimation is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::blackLevelEstimationQuadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::downscale is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::downscaleQuadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::extractFocusPixels is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::focusPixelDeltaBlurMap is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::focusPixelDeltaMap is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::focusPixelExtraction is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::focusPixelExtractionQuadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::generateSashimiCopy is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::generateSyntheticThumbnail is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::generateSyntheticThumbnailQuadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::hazeCorrection is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::hazeCorrectionQuadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::hazeDetection is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::hazeDomination is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::hoclXtalkCorrectionKernel is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::maxScaling is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::pdcDetectionCorrectionScan failed"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::pdcMarkStaticDefects is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::pdcStaticDefectReplace is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::pdcWriteStaticDefectLookup is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::pdcWriteStaticDefectReplace is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::processFocusPixelBlock failed"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::processFocusPixelBlockPairs failed"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::processFocusPixelBlockPairsFixedCenterIndex failed"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::qhoclXtalkCorrectionKernel is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::qpdcCorrectStaticDefectsKernel is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::qpdcDynamicCorrectKernel is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::qpdcDynamicDetectKernel failed"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::qpdcFocusPixelCorrectionKernel is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::qpdcReplaceStaticDefectsKernel is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::qpdcWriteCorrectedStaticDefectsKernel is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::rgbThumbnail is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::rgbThumbnailQuadra is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::sensorRawDecode is nil"
+ "<<<< SoftISP >>>> %s: H13FastRawScale::sumTexture is nil"
+ "<<<< SoftISP >>>> %s: H13UtilityConvertConfig: unsupported input pixel format: %d"
+ "<<<< SoftISP >>>> %s: H13UtilityConvertStage: outputPixelFormat not supported"
+ "<<<< SoftISP >>>> %s: HOCLBin parameters are overwriten by FlareDetector for HOCLBinMode2x2 binning."
+ "<<<< SoftISP >>>> %s: HR.HPBLUT mismatch; maxErr=%d"
+ "<<<< SoftISP >>>> %s: HR.HPPPInBlendLUT mismatch, maxErr=%f"
+ "<<<< SoftISP >>>> %s: HR.InBlendLUT mismatch; maxErr=%f"
+ "<<<< SoftISP >>>> %s: HR.MixClipLUT mismatch; maxErr=%f"
+ "<<<< SoftISP >>>> %s: HR.RcvLUT mismatch; maxErr=%f"
+ "<<<< SoftISP >>>> %s: HR.softClipLUT mismatch, maxError = %f"
+ "<<<< SoftISP >>>> %s: Haze correction is %@"
+ "<<<< SoftISP >>>> %s: Initialized using provided metal command queue %p"
+ "<<<< SoftISP >>>> %s: Initializing allocator with memSize: (%lu) (bytesRequired: %lu)"
+ "<<<< SoftISP >>>> %s: Input pixel format mismatch. Got:%c%c%c%c. Expected:%c%c%c%c"
+ "<<<< SoftISP >>>> %s: Invalid config"
+ "<<<< SoftISP >>>> %s: Invalid output first pixel; firstPix = %d, pixFmt=BayerUInt16"
+ "<<<< SoftISP >>>> %s: Invalid thumbnail size"
+ "<<<< SoftISP >>>> %s: LSC grid size is < %4d, %4d >, Xtalk LUT grid size is < %4d, %4d >"
+ "<<<< SoftISP >>>> %s: LTM is disabled in processing options for frame with ID '%llu'"
+ "<<<< SoftISP >>>> %s: LTMProcessor external backend metal allocator currently:%p, attempting to set to:%p"
+ "<<<< SoftISP >>>> %s: Legacy parsing of HighlightThdLUT being used."
+ "<<<< SoftISP >>>> %s: Loading from kFigCaptureCameraInfoKey_DefectivePixelTable."
+ "<<<< SoftISP >>>> %s: MTLPixelFormat %d not supported for RegWarp input"
+ "<<<< SoftISP >>>> %s: Mismatch between pdcConfig->corrBoundEnDP0 from metadata %d vs %d from registers"
+ "<<<< SoftISP >>>> %s: Mismatch between pdcConfig->corrBoundEnDP1 from metadata %d vs %d from registers"
+ "<<<< SoftISP >>>> %s: Mismatch between pdcConfig->dirIntEnDP0 from metadata %d vs %d from registers"
+ "<<<< SoftISP >>>> %s: Mismatch between pdcConfig->dirIntEnDP1 from metadata %d vs %d from registers"
+ "<<<< SoftISP >>>> %s: Mismatch between pdcConfig->popThdSpe from metadata %d vs %d from registers"
+ "<<<< SoftISP >>>> %s: NULL sbuf provided"
+ "<<<< SoftISP >>>> %s: New SoftISPInputFrame"
+ "<<<< SoftISP >>>> %s: New SoftISPOutputFrame"
+ "<<<< SoftISP >>>> %s: No 'strength' for YSH. A blit is being performed instead."
+ "<<<< SoftISP >>>> %s: No lens shading info, continue without LSC."
+ "<<<< SoftISP >>>> %s: No parameter 'A' in 'mixClipLUTParams'"
+ "<<<< SoftISP >>>> %s: No parameter 'B' in 'mixClipLUTParams'"
+ "<<<< SoftISP >>>> %s: No parameter 'C' in 'mixClipLUTParams'"
+ "<<<< SoftISP >>>> %s: No static defect table found."
+ "<<<< SoftISP >>>> %s: Not able to find flash LSC info, skip flash LSC"
+ "<<<< SoftISP >>>> %s: OIS shift = (%f, %f)"
+ "<<<< SoftISP >>>> %s: OutlierPixelCorrection is < %s >"
+ "<<<< SoftISP >>>> %s: Output height mismatch (max:%d, got:%lu)"
+ "<<<< SoftISP >>>> %s: Output pixel format mismatch. Got:%c%c%c%c. Expected:%c%c%c%c"
+ "<<<< SoftISP >>>> %s: Output width mismatch (max:%d, got:%lu)"
+ "<<<< SoftISP >>>> %s: Overriding precision to 10."
+ "<<<< SoftISP >>>> %s: PDC Crosstalk LUT mismatch. metadata: %d vs register: %d slice %zu index %zu\n"
+ "<<<< SoftISP >>>> %s: PDC tuning decision inputs: gainDigital = %f, gainAnalog = %f, totalGain = %f, lux = %f, integrationTime = %f, isFlashEnabled = %d"
+ "<<<< SoftISP >>>> %s: PDP Gain Mismatch between register value gr:%d rb:%d and gr:%d rb:%d from metadata. At location slice %zu n %zu. Cumulative maxDiff %d diffCount %d"
+ "<<<< SoftISP >>>> %s: PortType not found in metadata"
+ "<<<< SoftISP >>>> %s: PostDem DotFix: %d, DirectionalLowPass: %d, ChromaSuppression: %d (supportsInPlaceOperation:  %d)"
+ "<<<< SoftISP >>>> %s: PostDemosaic enableChromaSuppression is < %s >"
+ "<<<< SoftISP >>>> %s: PostDemosaic enableDirectionalLowpass is < %s >"
+ "<<<< SoftISP >>>> %s: PostDemosaic enableDotFix is < %s >"
+ "<<<< SoftISP >>>> %s: Prepared memory size on the external metal allocator is too small (required:%lu bytes, got:%lu bytes)"
+ "<<<< SoftISP >>>> %s: Purging AWB resources"
+ "<<<< SoftISP >>>> %s: QuadraBin::quadraBin is nil"
+ "<<<< SoftISP >>>> %s: RawMBNR isn't setup for processing resolution higher than 12MP, processingResolutionIsLessThan12MP = %d, isEnabled = %d"
+ "<<<< SoftISP >>>> %s: RegWarp++ reference image numKeypoints: %u\n"
+ "<<<< SoftISP >>>> %s: Removed duplicates: %d, new count = %d"
+ "<<<< SoftISP >>>> %s: Reusing LTMProcessor external backend metal allocator:%p"
+ "<<<< SoftISP >>>> %s: SensorCropRect missing"
+ "<<<< SoftISP >>>> %s: SensorDimensions are 0,0 for unrecognized sensor: 0x%04x"
+ "<<<< SoftISP >>>> %s: SensorID missing"
+ "<<<< SoftISP >>>> %s: SensorID not found in metadata"
+ "<<<< SoftISP >>>> %s: SensorRawValidBufferRect is not set in the metadata. Use the full frame as the validBufferRect."
+ "<<<< SoftISP >>>> %s: SensorRawValidBufferRect: (%f, %f, %f, %f)\n"
+ "<<<< SoftISP >>>> %s: SensorReadoutRect missing"
+ "<<<< SoftISP >>>> %s: Shading FPNR correction is %@"
+ "<<<< SoftISP >>>> %s: SoftISP RawMBNR: Force dimensions to 12MP for 48MP maximumOutputDimensions"
+ "<<<< SoftISP >>>> %s: SoftISPBounds for SensorID: 0x%04d"
+ "<<<< SoftISP >>>> %s: SoftISPDisparity::demosaicBayerToARGB is nil"
+ "<<<< SoftISP >>>> %s: SoftISPDisparity::demosaicQuadraBayerToARGB is nil"
+ "<<<< SoftISP >>>> %s: SoftISPRegWarp::demosaicQuarterLuma is nil"
+ "<<<< SoftISP >>>> %s: Static Defect Pass Count:%d"
+ "<<<< SoftISP >>>> %s: Static Defect Processing pass:%d defects:%d"
+ "<<<< SoftISP >>>> %s: Static defect table count: %d"
+ "<<<< SoftISP >>>> %s: Static defect table count: %d in %d quads"
+ "<<<< SoftISP >>>> %s: Static defect table count: %d, width=%d, height=%d, scaleFactor=%d"
+ "<<<< SoftISP >>>> %s: Static xtalk correction constrainedToLSC is < %@ >"
+ "<<<< SoftISP >>>> %s: StaticXtalkCorrect is < %@ >"
+ "<<<< SoftISP >>>> %s: SubGNU is < %@ >, subGnuMode: %d"
+ "<<<< SoftISP >>>> %s: SubGnu parameters for flare is used as FlareDetector returns positive."
+ "<<<< SoftISP >>>> %s: Tuning parameters for the PortType is nil"
+ "<<<< SoftISP >>>> %s: Unable to determine input first pixel; firstPix = %d, pixFmt=BayerUInt16"
+ "<<<< SoftISP >>>> %s: Unable to determine the first pixel type. Unsupported bayer input pixel format = %c%c%c%c"
+ "<<<< SoftISP >>>> %s: Unrecognized BayerPattern: %d"
+ "<<<< SoftISP >>>> %s: Unsupported bayer input pixel format = %c%c%c%c"
+ "<<<< SoftISP >>>> %s: Unsupported focus pixel type: %@"
+ "<<<< SoftISP >>>> %s: Unsupported pipeline type: %d"
+ "<<<< SoftISP >>>> %s: Unsupported pixel format: %c%c%c%c"
+ "<<<< SoftISP >>>> %s: Unsupported tuning type. Use WYSIWYG tunings instead."
+ "<<<< SoftISP >>>> %s: Using SoftISP AWB mode:%d. Setting AWB Digital Flash behavior mode:%d and face assisted behavior mode:%d"
+ "<<<< SoftISP >>>> %s: Using external metal allocator (size:%lu MB)"
+ "<<<< SoftISP >>>> %s: Vision failed to perform a request; error: %@"
+ "<<<< SoftISP >>>> %s: Vision failed to perform requests; error: %@"
+ "<<<< SoftISP >>>> %s: Warning: ABLEST not supported for Qsub - skipping"
+ "<<<< SoftISP >>>> %s: Warning: BScaling is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: Canvas queue not available."
+ "<<<< SoftISP >>>> %s: Warning: DesaturationBlendFactor is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: DesaturationLimit is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: DesaturationStrength is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: Encountered an unexpected error with kFigCaptureCameraInfoKey_DefectivePixels, reverting to fallback from kFigCaptureCameraInfoKey_DefectivePixelTable. This is expected behavior on pre-EVT devices."
+ "<<<< SoftISP >>>> %s: Warning: ExcludeDarkPixelThreshold is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: HOCL static xtalk grid size doesn't match LSC grid size. Static xtalk correction disabled."
+ "<<<< SoftISP >>>> %s: Warning: HazeCorrectionScaling is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: HazeCountThreshold is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: Luma Sharpening settings not available in SoftISPTuning.plist"
+ "<<<< SoftISP >>>> %s: Warning: MaxHazeThreshold is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: MinHazeThreshold is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: No 'OpticalCenter' found in metadata. Fallback to the sensor center."
+ "<<<< SoftISP >>>> %s: Warning: Ourlier Pixel Correction settings not available in SoftISPTuning.plist"
+ "<<<< SoftISP >>>> %s: Warning: PDC couldn't obtain AWB gains - defaulting to unity gain - some IQ degradation may occur"
+ "<<<< SoftISP >>>> %s: Warning: PDC couldn't obtain WB gains - defaulting to unity gain - some IQ degradation may occur"
+ "<<<< SoftISP >>>> %s: Warning: PurplenessThreshold is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: RScaling is missing; using default value"
+ "<<<< SoftISP >>>> %s: Warning: SSC failed and this should not happen. Please file a radar to 'Camera GPU Imaging' immediately."
+ "<<<< SoftISP >>>> %s: Warning: There is no LCA model available for sensorID %d. Please file a radar if you think this is a bug!"
+ "<<<< SoftISP >>>> %s: Warning: alphaMax mismatch (%f != %f)"
+ "<<<< SoftISP >>>> %s: Warning: alphaRatio mismatch (%f != %f)"
+ "<<<< SoftISP >>>> %s: Warning: cDist mismatch (%f != %f)"
+ "<<<< SoftISP >>>> %s: Warning: ceilingGain mismatch (%f != %f)"
+ "<<<< SoftISP >>>> %s: Warning: changing the cameraInfoByPortType is unsupported"
+ "<<<< SoftISP >>>> %s: Warning: clipLevelOffset mismatch ([%f, %f, %f, %f] != [%f, %f, %f, %f])"
+ "<<<< SoftISP >>>> %s: Warning: couldn't determine BayerPattern value for versatile output pixelbuffer"
+ "<<<< SoftISP >>>> %s: Warning: gridIntervalRecip mismatch ([%f, %f] != [%f, %f])"
+ "<<<< SoftISP >>>> %s: Warning: gridOffset mismatch ([%f, %f] != [%f, %f])"
+ "<<<< SoftISP >>>> %s: Warning: hpppCoeff mismatch ([%f, %f, %f] != [%f, %f, %f])"
+ "<<<< SoftISP >>>> %s: Warning: maxClip mismatch (%f != %f)"
+ "<<<< SoftISP >>>> %s: Warning: maxClipRecip mismatch (%f != %f)"
+ "<<<< SoftISP >>>> %s: Warning: maxLevel mismatch ([%f, %f, %f, %f] != [%f, %f, %f, %f])"
+ "<<<< SoftISP >>>> %s: Warning: rgbClipGain mismatch (%f != %f)"
+ "<<<< SoftISP >>>> %s: Warning: unprocessed input frame: TM=%d, B=%d, SIFR=%d, PB=%d"
+ "<<<< SoftISP >>>> %s: _draftDemosaicBayer is nil"
+ "<<<< SoftISP >>>> %s: _draftDemosaicQuadra2x is nil"
+ "<<<< SoftISP >>>> %s: _huemapThumbnailDownscalingFactor = %u"
+ "<<<< SoftISP >>>> %s: _metal is nil"
+ "<<<< SoftISP >>>> %s: addCompletionHandlerForOutputFrame; cmdBuf is nil"
+ "<<<< SoftISP >>>> %s: awbRegionOfInterestRectWithinSensorCropRect = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: awbRegionOfInterestWithinSensorInReadoutPixels = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: cfaLayout = %u, cfaPatternSize = %u"
+ "<<<< SoftISP >>>> %s: constantValues is nil"
+ "<<<< SoftISP >>>> %s: correctionType = %d."
+ "<<<< SoftISP >>>> %s: crop rect origin must be >= 0"
+ "<<<< SoftISP >>>> %s: crosstalk bitDepth:%d precision:%d"
+ "<<<< SoftISP >>>> %s: crosstalk: Convert QSub to QSum Xtlak for neighborTypeIndex:%d, with neighborTypeIndexOther:%d"
+ "<<<< SoftISP >>>> %s: crosstalk[%d][%d] width: %2d height %2d bitDepth:%d precision:%d"
+ "<<<< SoftISP >>>> %s: defectivePixelsData.length = %d, info->index = %d, info->count = %d"
+ "<<<< SoftISP >>>> %s: defectivePixelsData.length = %d, infoLag->index = %d, infoLag->count = %d"
+ "<<<< SoftISP >>>> %s: defects count before filtering = %d, defects count after filtering = %d, lag defects count = %d"
+ "<<<< SoftISP >>>> %s: externalMemoryDescriptor is nil"
+ "<<<< SoftISP >>>> %s: frameID = { captureIndex: %u, sensorID: 0x%04x, timeMachineIndex: %d, bracketedCaptureIndex: %d, isSIFR: %u, isPB: %u }"
+ "<<<< SoftISP >>>> %s: frameID = { captureIndex: %u, sensorID: 0x%04x, timeMachineIndex: %d, bracketedCaptureIndex: %d, isSIFR: %u, isPB: %u, tuningType: %d }"
+ "<<<< SoftISP >>>> %s: gain[%d] width: %2d height %2d"
+ "<<<< SoftISP >>>> %s: getCompressedPixelFormat compressionRatio = %d not valid"
+ "<<<< SoftISP >>>> %s: getCompressedPixelFormat uncompressedFormat=%d not supported for Lossless"
+ "<<<< SoftISP >>>> %s: getCompressedPixelFormat uncompressedFormat=%d not supported for Lossy50"
+ "<<<< SoftISP >>>> %s: getCompressedPixelFormat uncompressedFormat=%d not supported for Lossy62"
+ "<<<< SoftISP >>>> %s: getCompressedPixelFormat uncompressedFormat=%d not supported for Lossy75"
+ "<<<< SoftISP >>>> %s: highQualityProcessingRectWithinSensorCropRect = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: highQualitySensorReadoutRect = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: hiqhQualityProcessingRegionWithinOutputBufferInPixels = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: interp X LUT not monotonically increasing"
+ "<<<< SoftISP >>>> %s: isInScanOrder : %d, count : %d"
+ "<<<< SoftISP >>>> %s: linesPerThreadgroup: %d, verticalSections = %d"
+ "<<<< SoftISP >>>> %s: maxPasses:%d"
+ "<<<< SoftISP >>>> %s: maximumOutputDimensions = { Width: %u, Height: %u }, outputDownscaleFactor = %u"
+ "<<<< SoftISP >>>> %s: metal nil"
+ "<<<< SoftISP >>>> %s: neighborCount: %d"
+ "<<<< SoftISP >>>> %s: nil processingOptions provided"
+ "<<<< SoftISP >>>> %s: outputBufferRectWithinSensorCropRect = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: pdcCorrectStaticDefects count:%d"
+ "<<<< SoftISP >>>> %s: pdcDetectionCorrectionScan: dispatch groups = %d, tg = %d, tot.threads = %d, tot.pix = %d, over = %d"
+ "<<<< SoftISP >>>> %s: pdcDetectionCorrectionScan: lm.size = %d, maxThreads = %d"
+ "<<<< SoftISP >>>> %s: pipelineBlackLevel = %d, pipelineFootRoom = %d, pipelineHeadRoom = %d"
+ "<<<< SoftISP >>>> %s: prepareDescriptorByPipelineType is nil"
+ "<<<< SoftISP >>>> %s: prepareToProcesss:prepareDescriptor: called for type=%d, max dimensions: (%lu x %lu)"
+ "<<<< SoftISP >>>> %s: processFocusPixelBlock groups:{%d, %d} tgSize:{%d, %d}"
+ "<<<< SoftISP >>>> %s: processFocusPixelBlock numBlocks:%lu defectsPerBlock:%lu blocksPerThreadgroup:%lu"
+ "<<<< SoftISP >>>> %s: processingRectWithinSensorCropRect = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: processingRegionWithinInputBufferInPixels = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: processingRegionWithinOutputBufferInPixels = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: processingRegionWithinSensorInBayerPixels = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: processingRegionWithinSensorInReadoutPixels = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: quadraBinningFactor = %u"
+ "<<<< SoftISP >>>> %s: rFPN correction is %@"
+ "<<<< SoftISP >>>> %s: rawThumbnailsPixelBuffer = %p, rawThumbnailMetadata = %p"
+ "<<<< SoftISP >>>> %s: rawThumbnailsPixelBufferMain = %p, rawThumbnailMetadata = %p"
+ "<<<< SoftISP >>>> %s: rawThumbnailsPixelBufferSIFR = %p, rawThumbnailMetadataSIFR = %p"
+ "<<<< SoftISP >>>> %s: resetState is called"
+ "<<<< SoftISP >>>> %s: rwppUserConfig {\n  numThreads %d\n  numHorizontalBlocks %d\n  numVerticalBlocks %d\n  nccSearchRadius %d\n  nccPatchRadius %d\n  internalBorderSize %d\n  ransacAdaptiveThresholdFactor %f\n  ransacMinMatchingScoreAccepted %f\n  maxNumberOfPyramidLevels %d\n}\n"
+ "<<<< SoftISP >>>> %s: sbuf missing metadata"
+ "<<<< SoftISP >>>> %s: sbuf missing pixel buffer"
+ "<<<< SoftISP >>>> %s: sensorCropRect = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: sensorReadoutRect = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: sensorSize:              { %4d, %4d }"
+ "<<<< SoftISP >>>> %s: sensorSizeBayerPixels:   { %4d, %4d }"
+ "<<<< SoftISP >>>> %s: sensorSizeReadoutPixels: { %4d, %4d }"
+ "<<<< SoftISP >>>> %s: stageName < %@ >, bytesRequiredForConfig: (%.2f MB) ( %d x %d )"
+ "<<<< SoftISP >>>> %s: staticDefectCount count:%d"
+ "<<<< SoftISP >>>> %s: staticDefectPassCounts[%d]: %d"
+ "<<<< SoftISP >>>> %s: tgBuffer size = %d, sizeof(ScanThreadGroupInfo) = %d"
+ "<<<< SoftISP >>>> %s: transform[%d] = %f"
+ "<<<< SoftISP >>>> %s: tuningParameters not found"
+ "<<<< SoftISP >>>> %s: uncorrectedSensorBlackLevel = %d, uncorrectedSensorHeadRoom = %d, sensorBlackLevel = [%d, %d, %d, %d], averageSensorBlackLevel = %d, sensorHeadRoom = %d"
+ "<<<< SoftISP >>>> %s: uniqueID = %llu, PTS = %f"
+ "<<<< SoftISP >>>> %s: validBufferRect = { X: %d, Y: %d, Width: %u, Height: %u }"
+ "<<<< SoftISP >>>> %s: xtalkShift: %d"
+ "<unknown>"
+ "@\"<CRGInput>\""
+ "@\"<CRGOutput>\""
+ "@\"<CRGTextureArgs>\""
+ "@\"<MTLTexture>\"24@0:8@\"MTLTextureViewDescriptor\"16"
+ "@\"<RawDFSyntheticReferenceStage>\""
+ "@\"LearnedNRNetworkConfig\""
+ "@\"RawDFDetectors\""
+ "@\"RawDFSyntheticReferenceShadersCRG\""
+ "@\"RawProcFrames\""
+ "@\"RawProcInputFrame\""
+ "@24@0:8^(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})16"
+ "@24@0:8r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16"
+ "@32@0:8^{RawNightModeMultiFrameOutlierPixelCorrectionOptions=ii}16^i24"
+ "@40@0:8@16B24B28^i32"
+ "@48@0:8@16@24B32B36@40"
+ "@56@0:8@16@24@32@40i48B52"
+ "@60@0:8{?=(?=If)(?=If)fBfBf}16f44^f48B56"
+ "@64@0:8@16@24@32@40@48@56"
+ "AGC is greater than the maximal value 8.0"
+ "AGC is smaller than the minimal value 1.0"
+ "AGC missing from SIFR metadata"
+ "AGC missing from metadata"
+ "AGC not found"
+ "AGC not in the metadata"
+ "ALS LSC table has invalid size"
+ "AMBNRNoiseModelV4.m"
+ "AUTO"
+ "AWB not configured"
+ "AWB requires metadata to configure."
+ "AWB requires metadata."
+ "AWBBGain"
+ "AWBBGain not found"
+ "AWBComboBGain not found"
+ "AWBComboGGain not found"
+ "AWBComboRGain not found"
+ "AWBGGain"
+ "AWBGGain not found"
+ "AWBProcessor failed process"
+ "AWBRGain"
+ "AWBRGain not found"
+ "AdaptiveDLUT data missing"
+ "AdaptiveGradPushD data produced invalid LUT"
+ "AdaptiveGradPushHV data produced invalid LUT"
+ "AdaptiveHRLUT data missing"
+ "Allocate resources failed"
+ "AntiMazingGain is not a number"
+ "AntiMazingGain is not on the range [0.0 ... 100.0] - 0 means off and 100 means full suppression"
+ "AntiMazingThresh1 is not a number"
+ "AntiMazingThresh1 is not on the range [0.0 ... 0.2] - default is 0.023"
+ "AntiMazingThresh2 is not a number"
+ "AntiMazingThresh2 is not on the range [0.0 ... 20.0] - default is 5.0"
+ "Args invalid"
+ "Args not found"
+ "Attempted to set CameraInfoByPortType to nil"
+ "Aux frame can not be enabled for SIFR frames"
+ "Auxiliary pixel buffer has insufficient height"
+ "Auxiliary pixel buffer has insufficient width"
+ "Auxiliary pixel buffer provided by system not big enough to accommodate pattern copy."
+ "Auxiliary pixel format mismatch for the same auxiliary type"
+ "B24@0:8(?={?=II})16"
+ "B24@0:8r^(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})16"
+ "BScaling"
+ "Bad focus pixel location in calculating FPCORRECTIONCOEFF"
+ "Bad focusShape, check layoutType"
+ "Bad input chroma texture pixel format to Post Demosaic Proc"
+ "Bad input luma texture pixel format to Post Demosaic Proc"
+ "Bad input texture pixel format to Demosaic"
+ "Bad input texture pixel format to post-demosaic proc"
+ "Bad output chroma texture pixel format to Post Demosaic Proc"
+ "Bad output luma texture pixel format to Post Demosaic Proc"
+ "Bands array is NULL"
+ "Batch metadata doesn't have a Count"
+ "BayerPattern attachment missing"
+ "BayerPhase is nil"
+ "BayerProc addStage failed"
+ "BayerProc did not receive synthetic thumbnail"
+ "BayerProcHR section missing"
+ "BayerProcHR.HPBPLUT array missing"
+ "BayerProcHR.SoftClipLUT array missing"
+ "BayerProcHRD section missing"
+ "BayerProcLSC section missing"
+ "BayerProcWBG section missing"
+ "BayerProcWBG.Gain section missing"
+ "BilateralGrid run failed"
+ "BilateralGrid: width <= 0 or height <= 0"
+ "BlendClippedHueEn not found"
+ "BlendHPPPTargetEn not found"
+ "BlendInputEn not found"
+ "Blue not found"
+ "BlueFIRmix not found"
+ "BlueFIRmix.Slope not found"
+ "BlueFIRmix.Threshold not found"
+ "BlueHorizClampEn not found"
+ "BlueHorizFIRShift not found"
+ "BlueHorizMinSharpEn not found"
+ "BlueHorizMinSharpFactor not found"
+ "BlueVertClampEn not found"
+ "BlueVertFIRShift not found"
+ "BlueVertMinSharpEn not found"
+ "BlurFrameRejectionRegressionWeightLongFrame readPlist failed"
+ "BlurFrameRejectionRegressionWeightShortFrame readPlist failed"
+ "Both luma and chroma format are invalid"
+ "Bounds nil"
+ "Bracket metadata is null"
+ "Brackets must all have the same inputColorSpace, bailing!"
+ "Bypass not found"
+ "BypassBlueFIRMix not found"
+ "BypassBlueHorizFIR not found"
+ "BypassBlueVertFIR not found"
+ "BypassRedFIRMix not found"
+ "BypassRedHorizFIR not found"
+ "BypassRedVertFIR not found"
+ "CAR model has an unkown layout. Did anything change?"
+ "CAR model should have all first components = 0.0. Did anything change?"
+ "CAR not supported."
+ "CAR not supported. No 'ChromaticAberration->Lateral' in tuningParams"
+ "CAR not supported. No 'RadialModel' or 'RadialOrder' in tuningParams"
+ "CDist not found"
+ "CFA layout is invalid."
+ "CMIMultiChannelBayerToQuarterRGB"
+ "CMIMultiChannelQuadraToRGB2xBBGG"
+ "CMIMultiChannelQuadraToRGB4x"
+ "CMISingleChannelBayerToQuarterRGB"
+ "CMISingleChannelQuadraToRGB2xBBGG"
+ "CMISingleChannelQuadraToRGB4x"
+ "CMISoftwareFlashRenderingStatusMetalAllocationFailed"
+ "CMITiledInferenceProcessorStage"
+ "CMITiledInferenceProcessorStageV4.m"
+ "CPU"
+ "CRGRenderProvider"
+ "CameraInfo Dict not configured"
+ "CameraInfo does not contain pixel size info."
+ "Can't allocate rawData for quadra texture copy"
+ "Can't bind pixel buffer to MTLBuffer (metalBuffer[THUMBNAILS_INDEX_MAIN])"
+ "Can't bind pixel buffer to MTLBuffer (metalBuffer[THUMBNAILS_INDEX_SIFR])"
+ "Can't get BlackLevelShadingConfig config; input frame is nil"
+ "Can't get BlackLevelShadingConfig config; return pointer is NULL"
+ "Can't get CAR params; no moduleConfig present"
+ "Can't get CARConfig; bounds is nil"
+ "Can't get CARConfig; input frame is nil"
+ "Can't get CARConfig; return pointer is NULL"
+ "Can't get CMIWarpConfig; bounds is nil"
+ "Can't get CMIWarpConfig; frame is nil"
+ "Can't get CMIWarpConfig; input frame is nil"
+ "Can't get CMIWarpConfig; return pointer is NULL"
+ "Can't get DMAInput config; can't determine companding mode"
+ "Can't get DMAInput config; input frame is nil"
+ "Can't get DMAInput config; return pointer is NULL"
+ "Can't get DemosaicConfig from cfgMTL"
+ "Can't get DemosaicConfig; input frame is nil"
+ "Can't get DemosaicConfig; return pointer is NULL"
+ "Can't get FrontEndProcessorConfig; input frame is nil"
+ "Can't get FrontEndProcessorThumbnailConfig; gocConfig pointer is NULL"
+ "Can't get FrontEndProcessorThumbnailConfig; input frame is nil"
+ "Can't get FrontEndProcessorThumbnailConfig; return pointer is NULL"
+ "Can't get GOCConfig; input frame is nil"
+ "Can't get GOCConfig; lscConfig is NULL"
+ "Can't get GOCConfig; return pointer is NULL"
+ "Can't get HR Enabled status; return pointer is NULL"
+ "Can't get HRConfig; awbComputedGains invalid"
+ "Can't get HRConfig; input frame is nil"
+ "Can't get HRConfig; lscConfig is NULL"
+ "Can't get HRConfig; return pointer is NULL"
+ "Can't get HRDConfig; input frame is nil"
+ "Can't get HRDConfig; return pointer is NULL"
+ "Can't get HRDEnabled status; input frame is nil"
+ "Can't get HRDEnabled status; return pointer is NULL"
+ "Can't get HuemapConfig; gocConfig pointer is NULL"
+ "Can't get HuemapConfig; input frame is nil"
+ "Can't get HuemapConfig; return pointer is NULL"
+ "Can't get HuemapFepConfig; return pointer is NULL"
+ "Can't get HuemapMotionCompensationConfig; input frame is nil"
+ "Can't get HuemapMotionCompensationConfig; return pointer is NULL"
+ "Can't get LSCConfig; bounds is nil"
+ "Can't get LSCConfig; input frame is nil"
+ "Can't get PDCConfig; input frame is nil"
+ "Can't get PDCConfig; return pointer is NULL"
+ "Can't get PDP gains; input frame is nil"
+ "Can't get PDP gains; no FocusPixels entry present in moduleConfig"
+ "Can't get PDP gains; no moduleConfig present"
+ "Can't get PDP gains; return pointer is NULL"
+ "Can't get PDPConfig; input frame is nil"
+ "Can't get PDPConfig; return pointer is NULL"
+ "Can't get PostDemosaicProcConfig; input frame is nil"
+ "Can't get PostDemosaicProcConfig; return pointer is NULL"
+ "Can't get RFPNConfig config; input frame is nil"
+ "Can't get RFPNConfig config; return pointer is NULL"
+ "Can't get RNFConfig; bounds is nil"
+ "Can't get RNFConfig; input frame is nil"
+ "Can't get RNFConfig; return pointer is NULL"
+ "Can't get ShadingFPNCorrection texture; input frame is nil"
+ "Can't get ShadingFPNR config; input frame is nil"
+ "Can't get ShadingFPNR config; return pointer is NULL"
+ "Can't get SimpleDemosaicConfig; input frame is nil"
+ "Can't get SimpleDemosaicConfig; return pointer is NULL"
+ "Can't get SyntheticThumbnailConfig; input frame is nil"
+ "Can't get SyntheticThumbnailConfig; return pointer is NULL"
+ "Can't get cameraInfoByPortType; return pointer is NULL"
+ "Can't get chromaSuppressionConfig; return pointer is NULL"
+ "Can't get flareDetectionConfig; return pointer is NULL"
+ "Can't get frame metadata"
+ "Can't get hoclBinConfig; input frame is nil"
+ "Can't get hoclBinConfig; return pointer is NULL"
+ "Can't get input frame; input frame is nil"
+ "Can't get lscGainMapParameters"
+ "Can't get mcEnabled; return pointer is NULL"
+ "Can't get processing options"
+ "Can't get tuningParams"
+ "Can't have both BlackLevelEstimation and ABLEST enabled"
+ "Can't load HPBLUT; input frame is nil"
+ "Can't load HPBLUT; tex is nil"
+ "Can't load LUT; input frame is nil"
+ "Can't load LUT; tex is nil"
+ "Can't load SoftClipLUT; input frame is nil"
+ "Can't load SoftClipLUT; tex is nil"
+ "Can't read focal length info"
+ "Cannot compute blending weights"
+ "Cannot compute blending weights (low light)"
+ "Cannot createPyramidForFrame"
+ "Cannot enable compression with MTLBuffer backend "
+ "Cannot expect linear output for already tone-mapped inputs"
+ "Cannot process non-reference frame before reference frame is processed"
+ "Cannot set texture Y/UV for pyramid"
+ "Cannot use band 0 for GrayGhostDetection."
+ "CeilingGain not found"
+ "ChromaDenoiseChromaThresholdGain is missing or not array"
+ "ChromaDenoiseLumaThresholdGain is missing or not array"
+ "ChromaDenoiseMixingCoeff is missing or not array"
+ "ChromaDenoiseRolloffWindow is missing or not array"
+ "ChromaticAberrationRecoveryConfig.m"
+ "ClipLevelOffset not found"
+ "Clipping data does not have a high threshold bin (clipping stat is not available)."
+ "CoeffBLF array count incorrect"
+ "CoeffBLF array not found"
+ "CoeffBLF count incorrect"
+ "CoeffBLF not found"
+ "ColorCorrectionMatrix not found in input frame metadata"
+ "Combination in paramCombinations contains fewer than 2 entries."
+ "Config invalid"
+ "Config is NULL"
+ "Config is not SoftISPPipelineConfig instance"
+ "Config not found"
+ "Config section missing"
+ "Config2 not found"
+ "Configuration expects a quadra frame but quadraBinningFactor is missing or inconsistent"
+ "Conflicting tone mapping for input brackets"
+ "ConversionGain not found"
+ "ConversionGain not in the metadata"
+ "Convert addStage failed"
+ "ConvertToFp16 addStage failed"
+ "CorrBoundEnDP0 not found"
+ "CorrBoundEnDP1 not found"
+ "CorrBoundEnFP not found"
+ "CorrBoundFactor not found"
+ "Corrupted Rect metadata."
+ "Could not allocate Raw Night Mode TIP Espresso callback queue"
+ "Could not allocate accumulator 0 pyramid"
+ "Could not allocate chroma suppression texture"
+ "Could not allocate command buffer"
+ "Could not allocate defringe pyramid"
+ "Could not allocate guided filter output texture"
+ "Could not allocate second rgba pyramid texture"
+ "Could not allocate tempInputSurfaces"
+ "Could not allocate tempOutputSurfaces"
+ "Could not bind texture to pixelBuffer Y plane"
+ "Could not find LSCGains table in cameraInfo dict"
+ "Could not find Raw Night Mode Denoise network!"
+ "Could not get pointer to metadataGainData"
+ "Could not get pointer to registerGainData"
+ "Could not prepareToProcess the softLTM stage."
+ "Could not retrieve firstPix from CVPixelBuffer"
+ "Could not set resources for denoise remix"
+ "Couldn't allocate NoiseMap0"
+ "Couldn't allocate _maskMB."
+ "Couldn't allocate _maxVariationTex."
+ "Couldn't allocate accumulator band label"
+ "Couldn't allocate gg _maskSB texture"
+ "Couldn't allocate gg currentFusionWeights"
+ "Couldn't allocate gg diffTex"
+ "Couldn't allocate gg gradient texture"
+ "Couldn't allocate gg innerMask"
+ "Couldn't allocate gg innerMask texture"
+ "Couldn't allocate gg intermediateFusionWeights"
+ "Couldn't allocate gg intermediateMask texture"
+ "Couldn't allocate gg maskMBBinary texture"
+ "Couldn't allocate gg non-reference frame chroma texture"
+ "Couldn't allocate gg non-reference frame luma texture"
+ "Couldn't allocate gg outerMask"
+ "Couldn't allocate gg reference frame chroma texture"
+ "Couldn't allocate gg reference frame luma texture"
+ "Couldn't allocate ggDilatedMask texture"
+ "Couldn't allocate ggDownscaledRGBTexture"
+ "Couldn't allocate ggIntermediateMask texture"
+ "Couldn't allocate ggPropagatedGradient texture"
+ "Couldn't allocate ggPropagatedRGBTexture"
+ "Couldn't allocate inferenceData"
+ "Couldn't allocate intermMask1."
+ "Couldn't allocate intermMask2."
+ "Couldn't allocate intermTex."
+ "Couldn't determine CameraInfo from metadata"
+ "Couldn't determine FirstPix"
+ "Couldn't determine cfaLayout"
+ "Couldn't determine first pixel from input or output pixel buffer"
+ "Couldn't determine firstPix"
+ "Couldn't determine sensor dimensions"
+ "Couldn't determine the CFA layout"
+ "Couldn't determine the companding mode"
+ "Couldn't determine the first pixel"
+ "Couldn't find NonBinning noise model"
+ "Couldn't find global sharpness score"
+ "Couldn't get DefaultSensorIDs"
+ "Couldn't get class bundle."
+ "Couldn't get commandBuffer"
+ "Couldn't match BayerPhase"
+ "Couldn't parse sensor ID in CameraSetup.plist"
+ "Couldn't prepareToProcess [AWBProcessor]"
+ "Couldn't setup AWB Processor in Raw Night Mode Processor"
+ "Couldn't setup [AWBProcessor]"
+ "DeepFusionBufferType_EVMinus"
+ "DeepFusionBufferType_EVZero"
+ "DeepFusionBufferType_InferenceInput"
+ "DeepFusionBufferType_Long"
+ "DeepFusionBufferType_QuadraEVZero"
+ "DeepFusionBufferType_QuadraForEnhancedResInferenceInput"
+ "DeepFusionBufferType_ReferenceEVZero"
+ "DeepFusionBufferType_SyntheticLong"
+ "DeepFusionBufferType_SyntheticLong_FusionMap"
+ "DeepFusionBufferType_SyntheticLong_LongFusionMap"
+ "DeepFusionBufferType_SyntheticReference"
+ "DeepFusionBufferType_SyntheticReference_FusionMap"
+ "DeepFusionPostEspressoPlist params is nil."
+ "DeepFusionPostEspressoPlist readBandData failed"
+ "DeepFusionPostEspressoPlist readBandData failed (unexpected model name count)."
+ "DeepFusionPostEspressoPlist readBandData failed for given model."
+ "DeepFusionPostEspressoPlist readChromaBoostBandData failed"
+ "DeepFusionPostEspressoPlist readDesaturationData failed"
+ "DefringeStage was not allocated/enabled"
+ "DenoiseFusePipeline_downsampleUpperBandFrame"
+ "DenseRegistrationMotionScoreThreshold readPlist failed"
+ "Derived config != regdump"
+ "Derived config (blfKnee) != register"
+ "Derived config (blfSlope) != register"
+ "Derived config (coeffBLF) != register"
+ "Derived config (firstPix) != register"
+ "Derived config (nmLutType) != register"
+ "Derived config (optCenter) != register"
+ "Derived config (prescale) != register"
+ "Derived config (radScale) != register"
+ "Derived config (zeroBias) != register"
+ "DesaturationBlendFactor"
+ "DesaturationLimit"
+ "DesaturationStrength"
+ "DespThd0LUT entry not found"
+ "DespThd1LUT entry not found"
+ "DespThd2LUT entry not found"
+ "DespeckleDynamicCorrect not found"
+ "Destination property not found in unresolved properties"
+ "DiagGradMode not found"
+ "DirIntEnDP0 not found"
+ "DirIntEnDP1 not found"
+ "DirIntEnFP not found"
+ "Downstream stage failed to run"
+ "Draft demosaic only support downscaleFactor of 2"
+ "DynamicCorrect not found"
+ "DynamicDetect not found"
+ "DynamicThd0LUT entry not found"
+ "DynamicThd1LUT entry not found"
+ "DynamicThd2LUT entry not found"
+ "EV- is not present"
+ "EV0 is not present"
+ "EV0.AGC not found"
+ "EV0.ExposureTime not found"
+ "EV0BlurThreshold readPlist failed"
+ "EVM"
+ "EVM exists, however, no LTC attached"
+ "EVM frame registration has failed, bailing!"
+ "Early bail from addFrame: since _aggregateErr is in an unexpected bad state."
+ "Empty ISP Hall data"
+ "EnableLTMOnFinal"
+ "Error in calculating CMINoiseModels noise model for YUV noise map"
+ "Error: Input sbuf is NULL"
+ "Exceeds maximum number of frames that can be fused."
+ "ExcludeDarkPixelThreshold"
+ "Expected BodyAddBackWeight to be an NSArray, but it is not."
+ "Expected CMIModuleCalibration object"
+ "Expected LSCAddBackModulationWeight to be an NSArray, but it is not."
+ "Expected LumaAddBackWeight to be an NSArray, but it is not."
+ "Expected SkinAddBackWeight to be an NSArray, but it is not."
+ "Expected V1 GIC Grid Data"
+ "Expected V1 LSC Grid Data"
+ "Expected V2 LSC Grid Data"
+ "Expected ZNVM key in dictionary, but not found."
+ "Expected awbRegionOfInterestWithinSensorInReadoutPixels.origin must be multiple of cfaPatternSize"
+ "Expected awbRegionOfInterestWithinSensorInReadoutPixels.size must be multiple of cfaPatternSize"
+ "Expected grid to be enabled"
+ "Expected hiqhQualityProcessingRegionWithinOutputBufferInPixels.origin to be >= 0"
+ "Expected hiqhQualityProcessingRegionWithinOutputBufferInPixels.size+origin to be <= outputFrame.maximumOutputDimensions"
+ "Expected processingRegionWithinInputBufferInPixels.origin must be multiple of cfaPatternSize"
+ "Expected processingRegionWithinInputBufferInPixels.origin to be >= 0"
+ "Expected processingRegionWithinInputBufferInPixels.size must be multiple of cfaPatternSize"
+ "Expected processingRegionWithinInputBufferInPixels.size+origin to be <= inputFrame.sensorCropRect.size"
+ "Expected processingRegionWithinOutputBufferInPixels.origin to be >= 0"
+ "Expected processingRegionWithinOutputBufferInPixels.size+origin to be <= outputFrame.maximumOutputDimensions"
+ "Expected processingRegionWithinSensorInReadoutPixels.origin must be multiple of cfaPatternSize"
+ "Expected processingRegionWithinSensorInReadoutPixels.size must be multiple of cfaPatternSize"
+ "Expected sensorReadoutRect.origin.x must be multiple of cfaPatternSize"
+ "Expected sensorReadoutRect.origin.y must be multiple of cfaPatternSize"
+ "Expected sensorReadoutRect.size.height must be multiple of cfaPatternSize"
+ "Expected sensorReadoutRect.size.width must be multiple of cfaPatternSize"
+ "Expected validBufferRect.origin.x must be multiple of cfaPatternSize"
+ "Expected validBufferRect.origin.y must be multiple of cfaPatternSize"
+ "Expected validBufferRect.size.height must be multiple of cfaPatternSize"
+ "Expected validBufferRect.size.width must be multiple of cfaPatternSize"
+ "Expected xtalkLutTex.arrayLength to be 128"
+ "Expecting 420f format for inference output pixel buffer"
+ "Expecting HF20 format for RawNightMode output pixelBuffer."
+ "Expecting HF20 format for noiseMapPixelBuffer."
+ "Expecting HF20 output."
+ "Exposure metadata missing AGC"
+ "Exposure metadata missing GainDigital"
+ "ExposureTime missing in metadata"
+ "FPBlueMode not found"
+ "FPCWeightFactor not found"
+ "FPCorrFlatDetectEn not found"
+ "FPCorrFlatMode not found"
+ "FPCorrectionEnable not found"
+ "FPCrosstalkEnable not found"
+ "FPDiagMode not found"
+ "FPFlatThdLUT entry not found"
+ "FPNR model has invalid metadata"
+ "FPRedMode not found"
+ "FPUseBlue not found"
+ "FPUseRed not found"
+ "FPXtalkCoeffLUT entry not found"
+ "FPXtalkFlatDetectEn not found"
+ "FPXtalkFlatDetectEn not supported."
+ "Face detection failed"
+ "FaceRects"
+ "Failed to allocate ABLEST horizontalCorrection"
+ "Failed to allocate ABLEST meanCorrection"
+ "Failed to allocate ABLEST verticalCorrection"
+ "Failed to allocate FP-BLEST v2 blackLevelEstimate"
+ "Failed to allocate FP-BLEST v2 filteredHorizontalBlackLevelEstimate"
+ "Failed to allocate FP-BLEST v2 filteredVerticalBlackLevelEstimate"
+ "Failed to allocate FP-BLEST v2 horizontalBlackLevelEstimate"
+ "Failed to allocate FP-BLEST v2 intialBlackLevelEstimate"
+ "Failed to allocate FP-BLEST v2 verticalBlackLevelEstimate"
+ "Failed to allocate H13FastPostDemosaicProcMetal stage"
+ "Failed to allocate MetalContext."
+ "Failed to allocate MultiFrameOPC_output"
+ "Failed to allocate RawNightModeBatch"
+ "Failed to allocate RawNightModeConfig object"
+ "Failed to allocate RegWarpPP"
+ "Failed to allocate _toneMappingCurves"
+ "Failed to allocate alsTable intermediate memory"
+ "Failed to allocate arrGainRatio"
+ "Failed to allocate arrLSC"
+ "Failed to allocate band for accumulator pyramid"
+ "Failed to allocate blendingWeight"
+ "Failed to allocate calibrationByPortType"
+ "Failed to allocate confidenceMap"
+ "Failed to allocate costWeights_level0"
+ "Failed to allocate costWeights_levelX"
+ "Failed to allocate crossBilateralGrid"
+ "Failed to allocate currentShifts"
+ "Failed to allocate deltaBlurMap"
+ "Failed to allocate deltaMap"
+ "Failed to allocate emptyCalibration"
+ "Failed to allocate flash table intermediate memory"
+ "Failed to allocate flashLSCPixelBuffer pixel buffer"
+ "Failed to allocate fpLeft"
+ "Failed to allocate fpRight"
+ "Failed to allocate hazeDominationMap"
+ "Failed to allocate hpbLUT"
+ "Failed to allocate inference textures array"
+ "Failed to allocate inputSampleBuffers array."
+ "Failed to allocate internalTempTex"
+ "Failed to allocate lscPixelBuffer pixel buffer"
+ "Failed to allocate luma4xNonRef"
+ "Failed to allocate luma4xRef"
+ "Failed to allocate lumaHists"
+ "Failed to allocate lumaWinAvg_level0"
+ "Failed to allocate lumaWinAvg_levelX"
+ "Failed to allocate lutF16"
+ "Failed to allocate lutF32"
+ "Failed to allocate memory for RawNM Denoise tiled inference provider."
+ "Failed to allocate memory for RawNM Fusion tiled inference provider."
+ "Failed to allocate mismatch2xTex"
+ "Failed to allocate mismatch4xTex"
+ "Failed to allocate noise map textures array"
+ "Failed to allocate nonReferenceLumaTex"
+ "Failed to allocate output frame"
+ "Failed to allocate outputTex"
+ "Failed to allocate pdcArgs"
+ "Failed to allocate pdpGainsTex"
+ "Failed to allocate previousShifts"
+ "Failed to allocate pyramid object"
+ "Failed to allocate rawMBNR.bypass"
+ "Failed to allocate referenceLumaTex"
+ "Failed to allocate regWarpInput"
+ "Failed to allocate regWarpInput pixel buffer"
+ "Failed to allocate regwarpInputTex"
+ "Failed to allocate resources for RegWarpPP"
+ "Failed to allocate rgbThumbnail"
+ "Failed to allocate shaders"
+ "Failed to allocate shadowHPBLUT"
+ "Failed to allocate shadowLutF32"
+ "Failed to allocate shiftCosts_level0"
+ "Failed to allocate shiftCosts_levelX"
+ "Failed to allocate shiftMap"
+ "Failed to allocate staticXtalkGrid"
+ "Failed to allocate syntheticThumbnail"
+ "Failed to allocate texture"
+ "Failed to allocate texture descriptor"
+ "Failed to allocate textures array"
+ "Failed to allocate tm.globalLumaCurve"
+ "Failed to allocate tm.localCurves"
+ "Failed to allocate tm.perComponentCurve"
+ "Failed to allocate xtalkTableData"
+ "Failed to bind SIFR raw thumbnail"
+ "Failed to bind correction image"
+ "Failed to bind input cv pixel buffer"
+ "Failed to bind input frame texture"
+ "Failed to bind main EV0 raw thumbnail"
+ "Failed to bind output cv pixel buffer"
+ "Failed to bind output frame chroma texture"
+ "Failed to bind output frame luma texture"
+ "Failed to bind output frame noise map chroma texture"
+ "Failed to bind output frame noise map luma texture"
+ "Failed to bind output frame texture"
+ "Failed to bind outputTex to draftDemosaicPixelBuffer"
+ "Failed to bind outputTex to extractedFPPixBuf"
+ "Failed to bind outputTex to sashimiTex"
+ "Failed to bind resources"
+ "Failed to bind temporary texture demosaicLumaTex"
+ "Failed to bind textures for input frame"
+ "Failed to bind textures for output frame"
+ "Failed to calculate LTM"
+ "Failed to calculate linear RGB texture"
+ "Failed to copy warped chroma back to input."
+ "Failed to copy warped luma back to input."
+ "Failed to create AWBProcessor"
+ "Failed to create BlacklevelShadingCorrection"
+ "Failed to create CMIResourceMetal"
+ "Failed to create ConvertOutput texture"
+ "Failed to create HOCL static xtalk LUT texture"
+ "Failed to create HOCL xtalk LUT texture"
+ "Failed to create LSCGainsTex"
+ "Failed to create LTM shader"
+ "Failed to create LTMProcessor"
+ "Failed to create Metal allocator"
+ "Failed to create PDC FlatThd LUT texture"
+ "Failed to create PDC staticDefectPerLineIndexBase buffer"
+ "Failed to create PDC staticDefectProcessIndexList buffer"
+ "Failed to create PDC staticDefectTable buffer"
+ "Failed to create PDC temporary texture dynamicDefects"
+ "Failed to create PDC xtalk LUT texture"
+ "Failed to create QuadraShadingFPNCorrection"
+ "Failed to create ShadingFPNCorrection"
+ "Failed to create args for stage"
+ "Failed to create bayerNoise texture"
+ "Failed to create binnedTex texture"
+ "Failed to create bounds object"
+ "Failed to create calibration instance for module"
+ "Failed to create command buffer"
+ "Failed to create command encoder"
+ "Failed to create config for downstream stage"
+ "Failed to create config for stage"
+ "Failed to create corrected static defect buffer"
+ "Failed to create demosaicTex"
+ "Failed to create detectionDynDesp0LutTex texture"
+ "Failed to create detectionDynDesp12LutTex texture"
+ "Failed to create detectionHighlightThdTex texture"
+ "Failed to create device texture"
+ "Failed to create dotDetectedTex texture"
+ "Failed to create downstream args"
+ "Failed to create filteredQCCTex texture"
+ "Failed to create flare map  texture"
+ "Failed to create flashLSCGainsTex"
+ "Failed to create flashTexDesc"
+ "Failed to create gocOutputTex texture"
+ "Failed to create highPassGrGb texture"
+ "Failed to create highPassGrGbFiltered texture"
+ "Failed to create inference data"
+ "Failed to create input frame object"
+ "Failed to create intermediate texture"
+ "Failed to create intermediateGreenTex texture"
+ "Failed to create intermediateRGBTex texture"
+ "Failed to create lowPassYUV texture"
+ "Failed to create lowPassYUV2 texture"
+ "Failed to create lowPassYUVNoise texture"
+ "Failed to create lscGainsTex texture for 'LSC from CameraInfoByPortType'"
+ "Failed to create lscGainsTex texture from lscPixelBuffer"
+ "Failed to create mutable copy of metadata"
+ "Failed to create mutable copy of output metadata"
+ "Failed to create mutable processing options"
+ "Failed to create nextPyramidLevel texture"
+ "Failed to create outputChromaTex texture"
+ "Failed to create outputLumaTex texture"
+ "Failed to create outputTex texture"
+ "Failed to create pdpGainLUTTexDesc"
+ "Failed to create pipeline arguments"
+ "Failed to create postDemosaicTuningParams"
+ "Failed to create qdemInputTex texture"
+ "Failed to create qdemTuningParams"
+ "Failed to create quadra binning stage"
+ "Failed to create reconstructedTex texture"
+ "Failed to create scaledLinearOutputTex texture"
+ "Failed to create static defect side buffer"
+ "Failed to create tempChromaYCC texture for chroma suppression"
+ "Failed to create tempDotDetectedTex texture"
+ "Failed to create tempLumaTex texture"
+ "Failed to create texDesc"
+ "Failed to create texture descriptor"
+ "Failed to create tgBuffer buffer"
+ "Failed to create zimmerDEMTuningParams"
+ "Failed to determine binned bounds"
+ "Failed to determine binned input frame"
+ "Failed to determine bytesRequiredForConfig for stage"
+ "Failed to determine memory requirements"
+ "Failed to find AGC"
+ "Failed to find AWBComboBGain"
+ "Failed to find AWBComboGGain"
+ "Failed to find AWBComboRGain"
+ "Failed to find CameraInfo."
+ "Failed to find ChromaDenoiseMixingCoeff"
+ "Failed to find ConversionGain"
+ "Failed to find LensShadingModulationWeight"
+ "Failed to find ModuleConfig."
+ "Failed to find ReadNoise_1x"
+ "Failed to find ReadNoise_8x"
+ "Failed to find camera info"
+ "Failed to find camera port metadata"
+ "Failed to find focusPixelCFAComp in tuning parameters"
+ "Failed to find rawMBNR tuning parameters"
+ "Failed to generate bayerNoisePyramid"
+ "Failed to generate highPassGrGbPyramid"
+ "Failed to get HRD GNU pipeline state"
+ "Failed to get Pattern dict"
+ "Failed to get PixelType from Pattern"
+ "Failed to get X dict from Pattern"
+ "Failed to get X.Count from Pattern"
+ "Failed to get X.Start from Pattern"
+ "Failed to get X.Step from Pattern"
+ "Failed to get Y dict from Pattern"
+ "Failed to get Y.Count from Pattern"
+ "Failed to get Y.Start from Pattern"
+ "Failed to get Y.Step from Pattern"
+ "Failed to get a metadata"
+ "Failed to get computeEncoder"
+ "Failed to get config for stage"
+ "Failed to get denoiseBayerAndStepDown pipeline state"
+ "Failed to get denoiseChromaAndStepDown pipeline state"
+ "Failed to get height from LTMLookUpTables"
+ "Failed to get lowPassBayerAndDownscale2x pipeline state"
+ "Failed to get lumaSharpening kernel with function constant"
+ "Failed to get module config"
+ "Failed to get nLumaPoints from LTMLookUpTables"
+ "Failed to get pdcCorrectStaticDefects pipeline state"
+ "Failed to get pipeline state ispQDEMGreenStage"
+ "Failed to get pixel buffer for draft demosaic"
+ "Failed to get pixel buffer for focus pixel extraction."
+ "Failed to get pixel buffer for sashimi raw."
+ "Failed to get post demosaic dot fix pipeline state"
+ "Failed to get preHR compute pipeline state"
+ "Failed to get stage from dict"
+ "Failed to get width from LTMLookUpTables"
+ "Failed to inialise CMIExternalMemoryResource for SoftAWB"
+ "Failed to init CMIRawNightModeRegistrationStage"
+ "Failed to init RawNightModeGreenGhost"
+ "Failed to load LSCGains texture"
+ "Failed to load pdcDetectionCorrectionScan pipeline state"
+ "Failed to parse HPBPLUT array"
+ "Failed to parse SoftClipLUT array"
+ "Failed to prepare batch for raw night mode tripod fusion"
+ "Failed to process reference frame"
+ "Failed to read BlueHorizFIR"
+ "Failed to read BlueVertFIR"
+ "Failed to read HPPPInBlendLUT"
+ "Failed to read InBlendLUT"
+ "Failed to read MixClipLUT"
+ "Failed to read RcvLUT"
+ "Failed to read RedHorizFIR"
+ "Failed to read RedVertFIR"
+ "Failed to read SimDemCoeffBonGr"
+ "Failed to read SimDemCoeffBonR"
+ "Failed to read SimDemCoeffGbonR"
+ "Failed to read SimDemCoeffGronB"
+ "Failed to read SimDemCoeffRonB"
+ "Failed to read SimDemCoeffRonGb"
+ "Failed to register EVM frame; multi-frame processing can not continue."
+ "Failed to replacedRBfpTex texture"
+ "Failed to run network. Did you configure the TIP correctly?"
+ "Failed to run progressive raw night mode fusion inference"
+ "Failed to run progressive raw night mode tripod fusion"
+ "Failed to setup YSH"
+ "Failed to validate input frame"
+ "Failed to validate output frame"
+ "FigCaptureStreamDefectivePixels version not supported."
+ "FigCaptureStreamStillImageCaptureToneCurve enum not recognized."
+ "FigMetalAllocator (background) setupWithDescriptor failed"
+ "FigMetalAllocator addExternalMetalBuffer:atSubAllocatorID: failed"
+ "FigMetalAllocator allocation failed"
+ "FigMetalAllocator setupWithDescriptor failed"
+ "FigMetalAllocator setupWithDescriptor:allocatorBackend failed"
+ "FigMetalAllocator_LearnedNR"
+ "Filtered defect count doesn't match expected output count"
+ "Filtered defect count is greater than allocated buffer"
+ "FilteredChromaAlpha readPlist failed"
+ "FilteringOutlierThreshold not found in ABLEST tuning params"
+ "Final LSC and CIC table sizes mismatch"
+ "FirstPix not found"
+ "Flare correction configuration is nil"
+ "Flash LSC table has invalid height"
+ "Flash LSC table has invalid values"
+ "Flash LSC table has invalid width"
+ "Focus Pixel grid configuration contains locations with more than 1 neighboring focus pixel. This is not currently supported."
+ "Focus Pixel grid configuration exceeds maximum count, FPB_MAX_COUNT may need increasing."
+ "Focus pixel count not multiple 2."
+ "Focus pixel grid not in quad strcuture"
+ "Focus pixel grids are closer than 8 pixels"
+ "Focus pixel grids in a quad don't have identical intervals"
+ "Focus pixel list has partial neighbors. This is not currently supported."
+ "Focus pixel type not supported"
+ "Focus pixels not on blue"
+ "FocusPixelMap has more gain values than the expected"
+ "FocusPixelMap has more gain values than the expected 96"
+ "FocusPixelMap not found"
+ "FocusPixelMap version unsupported"
+ "FocusPixelScaling not found in ABLEST tuning params"
+ "FocusPixelScaling not found in BlackLevelEstimation tuning params"
+ "FocusPixels missing Layout"
+ "FocusPixels missing Patterns"
+ "FocusPixels section missing from ModuleConfig"
+ "Forcing ref frame selection when no best frame available"
+ "Function constant type not supported"
+ "Fusion parameters not set"
+ "G"
+ "GNUEnable not found"
+ "GNUMaxLUT count incorrect"
+ "GNUMaxLUT has invalid contents"
+ "GNUMaxLUT not found"
+ "GPU"
+ "GTC ltm is NOT available"
+ "GTCCurve is NULL"
+ "GVA lookup failed for BoostFactor"
+ "GVA lookup failed for BoostThreshold"
+ "GVA lookup failed for ChromaDenoiseLumaThresholdGain"
+ "GVA lookup failed for ChromaDenoiseRolloffWindow"
+ "GVA lookup failed for HighPassGreenBoostFactor"
+ "GVA lookup failed for HighPassMixingCoeff"
+ "GVA lookup failed for LumaDenoiseRolloffWindow"
+ "GVA lookup failed for LumaDenoiseThresholdGain"
+ "GVA lookup failed for LumaDenoiseThresholdGainHighPass"
+ "GVA lookup failed for SpecificLensShadingFactor"
+ "Gain not found"
+ "Gain not found/valid"
+ "Gain value error."
+ "GainBypassThd not found"
+ "GainGridOffset not found"
+ "GainIntXRecip/GainIntYRecip not found"
+ "GainLUT missing"
+ "GainLUT.count incorrect"
+ "GainShift not found/valid"
+ "GainShift value error."
+ "Gamma in plist not valid"
+ "GammaMultiFrame array length should be even number"
+ "GammaSingleFrame array length should be even number"
+ "GaussianNRLUT data missing"
+ "GlobalCorrectionWeight not found in ABLEST tuning params"
+ "GlobalLTMLookUpTable not found in metadata"
+ "GlobalMax not found in ABLEST tuning params"
+ "GlobalToneCurveLookUpTable not found in metadata"
+ "GraMaxCenter entry not found"
+ "GraMaxCorner entry not found"
+ "GraMaxEdge entry not found"
+ "Grad not found"
+ "Grad2 not found"
+ "GradEqualEn not found"
+ "GradEqualEn not supported."
+ "GreenSelBlue not found"
+ "GreenSelRed not found"
+ "GridConfig section missing"
+ "GridEn not found"
+ "GridIntervalRecipX not found"
+ "GridIntervalRecipX/Y not found"
+ "GridIntervalRecipY not found"
+ "GridIntervalX/Y not found"
+ "GridMaxGain field is missing"
+ "GridMaxGain is missing"
+ "GridNumPix section missing"
+ "GridNumPix.X/Y not found"
+ "GridOffsetX not found"
+ "GridOffsetY not found"
+ "GridStart section missing"
+ "GridStart.X/Y not found"
+ "H13FastAWB cannot allocate"
+ "H13FastAWB input metal backend allocator nil"
+ "H13FastAWB input metal commandQueue nil"
+ "H13FastAWB input metal context nil"
+ "H13FastLTMStage input metal backend allocator nil"
+ "H13FastRawScale::focusPixelDeltaBlurMap"
+ "H13FastRawScale::focusPixelDeltaMap"
+ "H13FastRawScale::focusPixelExtraction"
+ "H13FastRawScale::focusPixelExtractionQuadra"
+ "H13FastRawScale::hazeCorrection"
+ "H13FastRawScale::hazeCorrectionQuadra"
+ "H13FastRawScale::hazeDetection"
+ "H13FastRawScale::hazeDomination"
+ "H13FastRawScale::maxScaling"
+ "H13FastRawScale::rgbThumbnail"
+ "H13FastRawScale::rgbThumbnailQuadra"
+ "H13FastRawScale::sumTexture"
+ "H13FastRawScaleConfig+DMA.m"
+ "H13FastRawScaleConfig+HazeCorrection.m"
+ "H13FastRawScaleStage+HazeCorrection.m"
+ "HDRltmCurvesForBackground"
+ "HLGMaxTex"
+ "HLGMaxTex is NULL"
+ "HOCL static xtalk LUT size is invalid"
+ "HOCL static xtalk data may be corrupted"
+ "HOCL static xtalk grid size can not be smaller than LSC grid size"
+ "HPBLUT texture has wrong width"
+ "HPPPCoeff not found"
+ "HPPPInBlendLUT missing from registers"
+ "HR config mismatch"
+ "HR is enabled without HRD"
+ "HRD blue horizontal filter not symmetrical"
+ "HRD blue vertical filter not symmetrical"
+ "HRD red horizontal filter not symmetrical"
+ "HRD red vertical filter not symmetrical"
+ "HRD.blueFIRMix.slope mismatch"
+ "HRD.blueFIRMix.threshold mismatch"
+ "HRD.blueHorizFIR mismatch"
+ "HRD.blueHorizFIRShift mismatch"
+ "HRD.blueHorizMinSharpFactor mismatch"
+ "HRD.blueVertFIR mismatch"
+ "HRD.blueVertFIRShift mismatch"
+ "HRD.blueVertMinSharpFactor mismatch"
+ "HRD.config.blueHorizClampEn mismatch"
+ "HRD.config.blueHorizMinSharpEn mismatch"
+ "HRD.config.blueVertClampEn mismatch"
+ "HRD.config.blueVertMinSharpEn mismatch"
+ "HRD.config.bypassBlueFIRMix mismatch"
+ "HRD.config.bypassBlueHorizFIR mismatch"
+ "HRD.config.bypassBlueVertFIR mismatch"
+ "HRD.config.bypassRedFIRMix mismatch"
+ "HRD.config.bypassRedHorizFIR mismatch"
+ "HRD.config.bypassRedVertFIR mismatch"
+ "HRD.config.gnuEnable mismatch"
+ "HRD.config.redHorizClampEn mismatch"
+ "HRD.config.redHorizMinSharpEn mismatch"
+ "HRD.config.redVertClampEn mismatch"
+ "HRD.config.redVertMinSharpEn mismatch"
+ "HRD.config.simDemMaxSel mismatch"
+ "HRD.config.simDemModeBonGr mismatch"
+ "HRD.config.simDemModeGbonR mismatch"
+ "HRD.config.simDemModeGronB mismatch"
+ "HRD.config.simDemModeRonGb mismatch"
+ "HRD.firstPix mismatch"
+ "HRD.gnuMaxOffset mismatch"
+ "HRD.gnuMaxScale mismatch"
+ "HRD.redFIRMix.slope mismatch"
+ "HRD.redFIRMix.threshold mismatch"
+ "HRD.redHorizFIR mismatch"
+ "HRD.redHorizFIRShift mismatch"
+ "HRD.redHorizMinSharpFactor mismatch"
+ "HRD.redVertFIR mismatch"
+ "HRD.redVertFIRShift mismatch"
+ "HRD.redVertMinSharpFactor mismatch"
+ "HRD.simDemCoeffBonGr mismatch"
+ "HRD.simDemCoeffBonR mismatch"
+ "HRD.simDemCoeffGbonR mismatch"
+ "HRD.simDemCoeffGronB mismatch"
+ "HRD.simDemCoeffRonB mismatch"
+ "HRD.simDemCoeffRonGb mismatch"
+ "HRD.simDemHFScale.scaleBH mismatch"
+ "HRD.simDemHFScale.scaleBV mismatch"
+ "HRD.simDemHFScale.scaleRH mismatch"
+ "HRD.simDemHFScale.scaleRV mismatch"
+ "HazeCorrection"
+ "HazeCorrectionMaxScaling"
+ "HazeCorrectionScaling"
+ "HazeCountThreshold"
+ "HighPassMixingCoeff is missing or not array"
+ "Highlight Smoothing Luma Contrast Threshold is not an NSArray"
+ "Highlight Smoothing Luma Max Threshold is not an NSArray"
+ "Highlight smoothing sigma is not an NSArray"
+ "HighlightMaxDef.Center not found"
+ "HighlightMaxDef.Corner not found"
+ "HighlightMaxDef.Edge not found"
+ "HighlightMaxSpe.Center not found"
+ "HighlightMaxSpe.Corner not found"
+ "HighlightMaxSpe.Edge not found"
+ "HighlightThdLUT entry not found"
+ "HorizontalCorrectionWeight not found in ABLEST tuning params"
+ "HorizontalMax not found in ABLEST tuning params"
+ "I32@0:8@16@24"
+ "IMX190 not supported"
+ "IMX237 not supported"
+ "IOSurface"
+ "IOSurfaceGetBulkAttachments failed"
+ "ISP Hall data size did not match expected number of bytes."
+ "Identity"
+ "InBlendLUT missing from registers"
+ "Incompatible pixel format"
+ "Incompatible pyramid sizes"
+ "Inference failed"
+ "InlierThreshold not found in ABLEST tuning params"
+ "InlierThreshold not found in BlackLevelEstimation tuning params"
+ "Input frame is NULL"
+ "Input frame is missing pixelbuffer"
+ "Input frame is nil"
+ "Input frame metadata is nil"
+ "Input frame missing metadata"
+ "Input height mismatch"
+ "Input pixel buffer is not planar."
+ "Input pixel buffer not supported"
+ "Input pixel format not supported by Fast QDEM"
+ "Input registers NULL"
+ "Input surface not valid"
+ "Input textures already bound"
+ "Input tile Pixel Buffer Format not specified"
+ "Input tile metal pixel format not specified"
+ "Input to process inference is already tonemapped and that is not supported."
+ "Input width mismatch"
+ "InputTex must be half size of upsamplingFilter."
+ "Insufficient allocator memory"
+ "InterpGain section missing"
+ "Invalid AGC"
+ "Invalid ALS LSC u0 parameter"
+ "Invalid ALS LSC u1 parameter"
+ "Invalid ALS profile ID"
+ "Invalid AWB gains"
+ "Invalid CFA layout"
+ "Invalid Modulation Weight: Value outside of the range 0..1"
+ "Invalid Modulation Weight: baseModulation is less than 0. SCREENERS: This is an unexpected metadata and should go to BWGraph or HwISP team for further action."
+ "Invalid Modulation Weight: luxLevel is less than 0. SCREENERS: This is an unexpected metadata and should go to BWGraph or HwISP team for further action."
+ "Invalid Modulation Weight: modulationFactorPerLuxLevel is less than 0"
+ "Invalid OPC Skip configuration"
+ "Invalid QuadraBinningFactor metadata value"
+ "Invalid ReadNoise8x"
+ "Invalid ReadNoise_1x"
+ "Invalid YCbCr pixel format."
+ "Invalid auxiliary type"
+ "Invalid auxiliary type entry in processingOptions"
+ "Invalid conversion gain"
+ "Invalid fusion mode during prepareForFusion"
+ "Invalid input frame"
+ "Invalid metal context provided for texture creation"
+ "Invalid output auxiliary pixbuf"
+ "Invalid output frame"
+ "Invalid output pixbuf"
+ "Invalid prepare descriptor"
+ "Invalid pyramid level"
+ "Invalid sensorDGain"
+ "Invalid size for CIC table"
+ "Kernel does not have a functionConstantsDictionary"
+ "Kernel does not have function constants, functionConstants.count == 0"
+ "LSC Grid data is NULL"
+ "LSC buffer has unexpected pixel format"
+ "LSC flashPercentageLow >= flashPercentageHigh"
+ "LSC lowLightLuxLow >= lowLightLuxHigh"
+ "LSC pixel buffer not provided"
+ "LTC ltm is NOT available"
+ "LTMLookUpTables empty"
+ "LTMLookUpTables missing from metadata"
+ "LTMLookUpTables not found in metadata"
+ "LTMTable is NULL"
+ "LUT destHeight invald"
+ "LUT destWidth invald"
+ "LUT height invalid"
+ "LUT texture has wrong width"
+ "LUT width invalid"
+ "LearnedNR"
+ "LearnedNRBoundInferenceResults"
+ "LearnedNRNetworkConfig"
+ "LearnedNRNetworkTuningParams (Quadra) readPlist failed"
+ "LearnedNRNetworkTuningParams readPlist failed"
+ "LearnedNRPRocessor metal.allocator is leaking memory"
+ "LearnedNRProcessor"
+ "LearnedNRProcessorV4.m"
+ "LearnedNRTuningV4.m"
+ "Lens Shading Modulation is not in the range 0..1"
+ "LensShadingModulationWeight is missing"
+ "LensShadingModulationWeight not found"
+ "Limits of fragment buffer is reached!"
+ "Local Tone Curves not available. These must be available for Raw Night Mode."
+ "Luma Global Tone Curve not available. This must be populated for Raw Night Mode."
+ "LumaDenoiseRolloffWindow is missing or not array"
+ "LumaDenoiseThresholdGain is missing or not array"
+ "LumaDenoiseThresholdGainHighPass is missing or not array"
+ "M2M scaler doesn't support hf20 input"
+ "M2MController init failed"
+ "MIWBParameters readPlist failed"
+ "MPPComponentMax"
+ "MPPComputeRWTMOConstants"
+ "MPPConvertHLGToSDRAndHLGLumaA420"
+ "MPPGainMap420LumaA"
+ "MPPGainMapMax"
+ "MPPHLGComputeMaxComponent"
+ "MPPLog"
+ "MPPSetEDRToMax"
+ "MTLBuffer"
+ "MTLDevice"
+ "MTLHeap"
+ "MTLNoAliasing"
+ "Max not found/valid"
+ "Max value error."
+ "MaxClip not found"
+ "MaxHazeThreshold"
+ "MaxInlierValue not found in ABLEST tuning params"
+ "MaxInlierValue not found in BlackLevelEstimation tuning params"
+ "MaxLevel not found"
+ "MaxOPBErrorRatio not found in ABLEST tuning params"
+ "MaxOPBErrorRatio not found in BlackLevelEstimation tuning params"
+ "MaximumTotalGain"
+ "Memory not initialized"
+ "Metadata does not contain camera info."
+ "Metadata missing AGC"
+ "Metadata missing ExposureTime"
+ "Metadata missing SensorBlackLevel"
+ "Metadata missing SensorBlackLevelResidualFiltered"
+ "Metadata missing SensorBlackLevelResidualInstantaneous"
+ "Metadata missing SensorTemperature"
+ "Metadata missing ispDGain"
+ "Metadata not found"
+ "Metal context nil"
+ "Metal queue is nil"
+ "Min not found/valid"
+ "Min value error."
+ "MinDarken_I"
+ "MinDarken_II"
+ "MinDarken_III"
+ "MinDarken_IV"
+ "MinDarken_V"
+ "MinDarken_VI"
+ "MinExposureTime not found in ABLEST tuning params"
+ "MinHazeThreshold"
+ "MinPerceivableAdjustment not found in ABLEST tuning params"
+ "MinPerceivableAdjustment not found in BlackLevelEstimation tuning params"
+ "Mismatch between prepare heights in options"
+ "Mismatch between prepare pixel formats in options"
+ "Mismatch between prepare widths in options"
+ "Mismatch: !frame0Props.contentExtended || ((frame0Props.extendedDimensions[0] == currFrameProps.extendedDimensions[0])"
+ "Mismatch: (frame0Props.meta.sensorID == currFrameProps.meta.sensorID)"
+ "Missing ALS LSC d parameter"
+ "Missing ALS LSC mean parameter"
+ "Missing ALS LSC r parameter"
+ "Missing ALS LSC rScale parameter"
+ "Missing ALS LSC u parameter"
+ "Missing ALS LSC uMin parameter"
+ "Missing ALS R/B illuminants"
+ "Missing ALS models"
+ "Missing Addback tuning parameter"
+ "Missing AddbackModulationEnabled tuning parameter"
+ "Missing CIC data in CIC table metadata"
+ "Missing ClippingLowerBound tuning parameter"
+ "Missing ClippingUpperBound tuning parameter"
+ "Missing EnableSNRModulation tuning parameter"
+ "Missing Fusion NoiseMapScaling tuning parameter"
+ "Missing HR parameter"
+ "Missing Highlight Smoothing Luma Contrast Threshold tuning parameter"
+ "Missing Highlight Smoothing Luma Max Threshold tuning parameter"
+ "Missing Highlight Smoothing Pixels Above Max tuning parameter"
+ "Missing Highlight Smoothing Window Width tuning parameter"
+ "Missing Highlight Smoothing enabled tuning parameter"
+ "Missing Highlight Smoothing sigma tuning parameter"
+ "Missing LumaAddBackWeight tuning parameter"
+ "Missing NoiseMapScaling tuning parameter"
+ "Missing OPC Enabled tuning parameter"
+ "Missing OPC Gamma tuning parameter"
+ "Missing OPC Window Size tuning parameter"
+ "Missing OutlierPixelCorrection tuning parameter"
+ "Missing Post Demosaic Chroma Suppression parameters"
+ "Missing Post Demosaic tuning parameters"
+ "Missing PostNetwork tuning parameter"
+ "Missing PreNetwork tuning parameter"
+ "Missing Skip tuning parameter"
+ "Missing TileData metadata"
+ "Missing TileHeight metadata"
+ "Missing TileWidth metadata"
+ "Missing cameraInfoByPortType"
+ "Missing greenGhostThreshold tuning parameter."
+ "MixClipLUT missing from registers"
+ "ModelSwitchGainThreshold readPlist failed"
+ "ModuleConfig doesn't have LensShading entry"
+ "ModuleConfig doesn't have LensShading.Maps entry"
+ "ModuleConfig doesn't have LensShading.Maps.BayerPhase entry"
+ "ModuleConfig for FocusPixels->Layout->Type missing"
+ "ModuleConfig has more focus pixel patterns than expected"
+ "ModuleConfig is missing Sensor section"
+ "ModuleConfig is nil"
+ "ModuleConfig missing FocusPixels"
+ "ModuleConfig not found in tuning params"
+ "ModuleConfig.Sensor is missing NoiseModels section"
+ "More textures than expected in inferenceTextures"
+ "More textures than expected in input textures"
+ "More textures than expected in noiseMapTextures"
+ "Mul3x3by3x3by3x3"
+ "NOT"
+ "NRF"
+ "NRFProcessorV4 metal.allocator is leaking memory"
+ "NRFSingletonsReleaseAll"
+ "NULL MetalContext"
+ "Neighboring focus pixels to Red/Blue can only be Green (bayer layout)."
+ "NeighborsDeltaThreshold not found in ABLEST tuning params"
+ "NeighborsDeltaThreshold not found in BlackLevelEstimation tuning params"
+ "NetworkModel"
+ "NmLutType not found"
+ "No ALS profile info"
+ "No Bands in Synthetic Reference DeepShadowRecover"
+ "No Bands in Synthetic Reference HighlightRecover"
+ "No CIC table in camera metadata"
+ "No DarkEdgeSuppressionPlist Bands"
+ "No DeepFusionPostEspressoPlist Bands"
+ "No DeepFusionPostEspressoPlist Desaturation data."
+ "No DeepFusionPostEspressoPlist value for key chroma boost"
+ "No FaceRects dictionary in metadata"
+ "No FaceScores dictionary in metadata"
+ "No HOCL static xtalk data in Module Config"
+ "No HaloSuppressionPlist Bands"
+ "No LSC Gains"
+ "No LSC Gains data"
+ "No LSC Gains data in camera metadata"
+ "No LSC Gains in camera metadata"
+ "No LSC gains in table of size 0"
+ "No Metal allocator"
+ "No SIFR frame available for current frame, but HR is requested"
+ "No SharpnessScore dictionary in metadata"
+ "No Synthetic Long Bands"
+ "No Synthetic Reference DeepShadowRecover"
+ "No Synthetic Reference HighlightRecover"
+ "No batch metadata dictionary provided to inference"
+ "No cameraInfo found for portType not found in cameraInfoByPortType"
+ "No denoiseAndSharpening tuning parameters, no processing to be done"
+ "No ev0RefDenoising tuning parameters found for denoise and sharpening, no processing to be done"
+ "No evmRefDenoising tuning parameters found for denoise and sharpening, no processing to be done"
+ "No frame metadata available"
+ "No input textures"
+ "No metadata dictionary present, failed to set parameters"
+ "No metadata found for Main raw thumbnail pixelbuffer"
+ "No metadata found for SIFR raw thumbnail pixelbuffer"
+ "No metadata found for raw thumbnails pixelbuffer (Main + SIFR)"
+ "No metadata on inputFrame"
+ "No noise map pixel buffer"
+ "No reference frame chosen after looking at 'referenceFrameCandidatesCount' frames."
+ "No reference frame for metadata"
+ "No sharpness score dictionary in metadata"
+ "No tuning parameters found for denoise and sharpening, no processing to be done"
+ "No tuning parameters found for ev0RefDenoising, no processing can be done"
+ "No tuning parameters found for evmRefDenoising, no processing can be done"
+ "No tuning parameters found for fusion, no processing to be done"
+ "No tuning parameters found for noise model, no processing to be done"
+ "No tuning parameters found for syntheticReference, no processing can be done"
+ "No tuning parameters found for toneMapping, no processing to be done"
+ "Noise model variant not recognized."
+ "Noise reduction must be processed to produce a linear output"
+ "NoiseMapScaling is not of the expected format (NSArray)"
+ "NoiseModel missing ConversionGain"
+ "NoiseModel missing ReadNoise_1x"
+ "NoiseModel missing ReadNoise_8x"
+ "NoiseSuppression data produced invalid LUT"
+ "Non-reference gdcParams = nil"
+ "NonGreenMode not found"
+ "NormTargetHueEn not found"
+ "NormalizedValues field is missing"
+ "NormalizedValues is missing"
+ "Not able to allocate intermediate alsGainmapB"
+ "Not able to allocate intermediate alsGainmapR"
+ "Not able to allocate intermediate baseLSCTable"
+ "Not able to allocate intermediate finalLSCTable"
+ "Not able to allocate intermediate flashLSCTable"
+ "Not able to allocate quadra table"
+ "Not enough source params"
+ "ON"
+ "Offset1 not found/valid"
+ "Offset1 value error."
+ "Offset2 not found/valid"
+ "Offset2 value error."
+ "One or more stages could not be resolved"
+ "Only FIRSTPIX_R or FIRSTPIX_B supported"
+ "OptCenter section missing"
+ "OpticalCenter not found"
+ "OutlierPixelCorrection addStage failed"
+ "Output compression not supported by ToneMapping stage"
+ "Output frame is NULL"
+ "Output frame is missing noise map"
+ "Output frame is missing pixelbuffer"
+ "Output height mismatch"
+ "Output height of noise map should be the same as the output frame"
+ "Output pixelBuffer is nil"
+ "Output surface not valid"
+ "Output textures already bound"
+ "Output tile Pixel Buffer Format not specified"
+ "Output tile metal pixel format not specified"
+ "Output width mismatch"
+ "Output width of noise map should be the same as the output frame"
+ "OutputNoiseModelPlist readPlist failed"
+ "PDC Crosstalk LUTs differ"
+ "PDC process failed"
+ "PDC requires register data."
+ "PDC: Unexpected size of resized crosstalk map"
+ "PDCSetKernel"
+ "PDP section missing"
+ "PDP unexpected resized gain map"
+ "PDPClipMax not found"
+ "PDPClipMin not found"
+ "PDPOffsetIn not found"
+ "PDPOffsetOut not found"
+ "ParamBLF section missing"
+ "ParamBLF.Knee not found"
+ "ParamBLF.Slope not found"
+ "Parsing RFS/BFR weights; required key 'CornerWeight' missing."
+ "Parsing RFS/BFR weights; required key 'FocusWeight' missing."
+ "Parsing RFS/BFR weights; required key 'GyroWeight' missing."
+ "PatchBasedFusionParametersLUTs readPlist failed"
+ "PavMode not found"
+ "PhfCrossChanEn not found"
+ "PhfDirEn not found"
+ "PhfMode > 0 not supported."
+ "PhfMode not found"
+ "Pipeline couldn't validate input frame"
+ "Pipeline did not attach a completion handler to output"
+ "Pipeline init fail"
+ "Pipeline run failed"
+ "Pixel format mismatch between graph outputs"
+ "PopMode not found"
+ "PortType not found"
+ "PortType not found in metadata"
+ "PostCorrectionOffsetB not found in ABLEST tuning params"
+ "PostCorrectionOffsetGb not found in ABLEST tuning params"
+ "PostCorrectionOffsetGr not found in ABLEST tuning params"
+ "PostCorrectionOffsetR not found in ABLEST tuning params"
+ "PostDemProc addStage failed"
+ "Prescale section missing"
+ "PrescaleX not found"
+ "ProRaw"
+ "Property not found"
+ "Property not found or nil"
+ "PurplenessThreshold"
+ "QDEM tuning parameters not set"
+ "Quadra binning requires input frame to have quadra CFA layout"
+ "RBRepCoeff entry not found"
+ "RGB Global Tone Curve not available. This most be populated for Raw Night Mode."
+ "RGBADest should be the same as textureArray[1] at this point"
+ "RGBADest should not be the same as nextAvailableFullSizeTexture"
+ "RGBclipGain not found"
+ "RNF process failed"
+ "RNF section missing"
+ "RScaling"
+ "RadGainLUT count incorrect"
+ "RadGainLUT not found"
+ "RadScale not found"
+ "RawCompanding value incorrect"
+ "RawDFDeepShadowRecoveryFinalTex"
+ "RawDFDeepShadowRecoveryMainTex"
+ "RawDFDeepShadowRecoveryUpTex"
+ "RawDFHighlightRecoveryTextures"
+ "RawDFNetworkPreprocessV4.m"
+ "RawDFSynRefDSR"
+ "RawDFSynRefDSRPass"
+ "RawDFSynRefHR"
+ "RawDFSyntheticReferenceCRG::%s"
+ "RawDFSyntheticReferenceShadersCRG"
+ "RawDFSyntheticReferenceStageCRG"
+ "RawDFSyntheticReferenceStageCRGV4.m"
+ "RawMBNRStage addStage failed"
+ "RawNM Config not provided"
+ "RawNM TIP Config not specified"
+ "RawNM TIP network urls not specified"
+ "RawNM TIP not provided with metal context"
+ "RawNM TIP post inference plugin not provided"
+ "RawNM TIP pre inference plugin not provided"
+ "RawNM networks urls count not equal to 1"
+ "RawNightModeInferenceAllocationError"
+ "RawNightModeInferenceConfigurationError"
+ "RawNightModeInferenceEspressoError"
+ "RawNightModeInferenceMemoryError"
+ "RawNightModeInferenceOtherError"
+ "RawNightModeInferenceTiledProvider: RawNM Denoise Inference FAILED"
+ "RawNoiseFilterShadowBoost in plist not valid"
+ "RawNoiseFilterStrength in plist not valid"
+ "RawProcFrames"
+ "RawProcFramesV4.m"
+ "RawProcInputFrame"
+ "RawProcInputFrameV4.m"
+ "RawSensorHeight is missing"
+ "RawSensorWidth is missing"
+ "RcvLUT missing from registers"
+ "Read and shot noise must be positive"
+ "ReadNoise_1x not found"
+ "ReadNoise_1x not in the metadata"
+ "ReadNoise_8x not found"
+ "ReadNoise_8x not in the metadata"
+ "RecovMethod not found"
+ "Red not found"
+ "RedFIRmix not found"
+ "RedFIRmix.Slope not found"
+ "RedFIRmix.Threshold not found"
+ "RedHorizClampEn not found"
+ "RedHorizFIRShift not found"
+ "RedHorizMinSharpEn not found"
+ "RedHorizMinSharpFactor not found"
+ "RedVertClampEn not found"
+ "RedVertFIRShift not found"
+ "RedVertMinSharpEn not found"
+ "RedVertMinSharpFactor not found"
+ "Reference frame cannot be a EVM frame"
+ "Reference frame index must be different than preB index"
+ "Reference frame must not be invalid, bailing!"
+ "Reference frame selector candidates should only containg the reference frame for tripod mode"
+ "Reference gdcParams = nil"
+ "ReferenceFrameSelector should only receive one frame when in Tripod mode"
+ "ReferenceSelectionRegressionWeightLongFrame readPlist failed"
+ "ReferenceSelectionRegressionWeightShortFrame readPlist failed"
+ "RegWarp++"
+ "RegWarpConfig+RegWarp.m"
+ "Registers NULL"
+ "Registers nil"
+ "ReportMemoryException"
+ "Requested pipeline not found in supported set"
+ "RsclProcBLC0 not found"
+ "RsclProcPDC0 not found"
+ "SCHueRefChannel not found"
+ "SCREENERS: No valid data in LSCGainGrid in the CameraInfoByPortType (maxGain is not > 0). Should go to bwgraph team for further action"
+ "SFD"
+ "SIFR Frame ID does not match EVO frame ID"
+ "SIFR.AGC not found"
+ "SIFR.ExposureTime not found"
+ "SIFRMetadata missing"
+ "SR"
+ "SSC memory isn't accounted for, cannot run"
+ "STF Processor setup failed"
+ "SensorBlackLevel missing from SIFR metadata"
+ "SensorBlackLevel missing from metadata"
+ "SensorCropRect is missing"
+ "SensorDimensions height is missing"
+ "SensorDimensions nil"
+ "SensorDimensions width is missing"
+ "SensorDimensions.height nil"
+ "SensorDimensions.width nil"
+ "SensorID not found"
+ "SensorReadoutRect is missing"
+ "SensorReadoutRect missing"
+ "ShadingFPNCorrection.Metadata is missing BlackLevelResidualRef"
+ "ShadingFPNCorrection.Metadata is missing BlackLevelResidualTemperatureGrowthFactor"
+ "ShadingFPNCorrection.Metadata is missing BlackLevelResidualZero"
+ "ShadingFPNCorrection.Metadata is missing CalibrationSpatialStdDev"
+ "ShadingFPNCorrection.Metadata is missing CalibrationTemporalStdDev"
+ "ShadingFPNCorrection.Metadata is missing DCOffsetRef"
+ "ShadingFPNCorrection.Metadata is missing DCOffsetTemperatureGrowthFactor"
+ "ShadingFPNCorrection.Metadata is missing DCOffsetZero"
+ "ShadingFPNCorrection.Metadata is missing FPNMaxValue"
+ "ShadingFPNCorrection.Metadata is missing FPNMinValue"
+ "ShadingFPNCorrection.Metadata is missing FPNTemperatureGrowthFactor"
+ "ShadingFPNCorrection.Metadata is missing ModelAnalogGain"
+ "ShadingFPNCorrection.Metadata is missing ModelExposureTime"
+ "ShadingFPNCorrection.Metadata is missing ModelTemperature"
+ "ShadingFPNCorrection.Metadata is missing NDarkFramesUsedInCalibration"
+ "ShadingFPNCorrection.Metadata is missing ShadingMaxValue"
+ "ShadingFPNCorrection.Metadata is missing ShadingMinValue"
+ "ShadingFPNCorrection.Metadata is missing ShadingTemperatureGrowthFactor"
+ "Sharpness Score allocation failed"
+ "Sharpness Score calculation failed."
+ "SimDemHFScale not found"
+ "SimDemHFScale.ScaleBH not found"
+ "SimDemHFScale.ScaleBV not found"
+ "SimDemHFScale.ScaleRH not found"
+ "SimDemHFScale.ScaleRV not found"
+ "SimDemMaxSel not found"
+ "SimDemModeBonGr not found"
+ "SimDemModeGbonR not found"
+ "SimDemModeGronB not found"
+ "SimDemModeRonGb not found"
+ "Sizes of input and output buffers do not match!"
+ "Skip tuning params can only be 1 or 2"
+ "SkipHardGainLumaHD"
+ "SkipMultiFrame tuning params can only be 1 or 2"
+ "SkipSingleFrame tuning params can only be 1 or 2"
+ "SmoothStrengthD array length should be even number"
+ "SmoothStrengthD in plist not valid"
+ "SmoothStrengthHV array length should be even number"
+ "SmoothStrengthHV in plist not valid"
+ "SmoothingHSigma not found in ABLEST tuning params"
+ "SmoothingVSigma not found in ABLEST tuning params"
+ "SoftClipEn not found"
+ "SoftClipLUT texture has wrong width"
+ "SoftISP AGC not found"
+ "SoftISP ExposureTime not found"
+ "SoftISP LuxLevel not found"
+ "SoftISP Sensor NoiseModels not found"
+ "SoftISP ispDGain not found"
+ "SoftISP sensorDGain not found"
+ "SoftISPBounds.m"
+ "SoftISPGraph super init failed"
+ "SoftISPProcessor metal.allocator is leaking memory"
+ "Spe not found"
+ "SpecificLensShadingFactor is missing or not array"
+ "Stage has invalid output downscale factor"
+ "Stage has invalid output pixel format"
+ "Stage input property has multiple sources"
+ "Stage name is not unique"
+ "Stage not found in graph"
+ "Stage not found in pipeline config"
+ "StdDevLUT array count incorrect"
+ "StdDevLUT array not found"
+ "StdDevLUT count incorrect"
+ "StdDevLUT not found"
+ "StrongEdgeDetectionThreshold is missing"
+ "StrongEdgeFusionWeightsModulationStrength is missing"
+ "SubjectRelightingStage runSubjectRelighting failed"
+ "Subsampling not found in ABLEST tuning params"
+ "Super init failed"
+ "Synthetic Long readBandData failed"
+ "Synthetic Thumbnail: input frame is nil"
+ "Synthetic Thumbnail: lscConfig is nil"
+ "Synthetic Thumbnail: thumbnailConfig is nil"
+ "T@\"<CRGInput>\",R,N,V_dsrUp"
+ "T@\"<CRGInput>\",R,N,V_ev0"
+ "T@\"<CRGInput>\",R,N,V_ev0Up"
+ "T@\"<CRGInput>\",R,N,V_evm"
+ "T@\"<CRGInput>\",R,N,V_evmUp"
+ "T@\"<CRGOutput>\",R,N,V_fusionWeights"
+ "T@\"<CRGOutput>\",R,N,V_output"
+ "T@\"<MTLComputePipelineState>\",R,N,V_focusPixelDeltaBlurMap"
+ "T@\"<MTLComputePipelineState>\",R,N,V_focusPixelDeltaMap"
+ "T@\"<MTLComputePipelineState>\",R,N,V_focusPixelExtraction"
+ "T@\"<MTLComputePipelineState>\",R,N,V_focusPixelExtractionQuadra"
+ "T@\"<MTLComputePipelineState>\",R,N,V_hazeCorrection"
+ "T@\"<MTLComputePipelineState>\",R,N,V_hazeCorrectionQuadra"
+ "T@\"<MTLComputePipelineState>\",R,N,V_hazeDetection"
+ "T@\"<MTLComputePipelineState>\",R,N,V_hazeDomination"
+ "T@\"<MTLComputePipelineState>\",R,N,V_maxScaling"
+ "T@\"<MTLComputePipelineState>\",R,N,V_rgbThumbnail"
+ "T@\"<MTLComputePipelineState>\",R,N,V_rgbThumbnailQuadra"
+ "T@\"<MTLComputePipelineState>\",R,N,V_sumTexture"
+ "T@\"FigWiredMemory\",&,N,VsharedRegWarpBuffer"
+ "T@\"GrayGhostDetection\",&,N,V_grayGhostDetection"
+ "T@\"MotionDetection\",&,N,V_motionDetection"
+ "T@\"NSArray\",R,N,V_frames"
+ "T@\"NSString\",&,N,V_networkModel"
+ "T@\"RawDFColorMatchStage\",&,N,V_rawDFColorMatchStage"
+ "T@\"RawDFDownsampleStage\",&,N,V_rawDFDownsampleStage"
+ "T@\"RawDFFlickerDetectorStage\",&,N,V_flickerDetection"
+ "T@\"RawProcInputFrame\",R,N"
+ "T@\"RawProcInputFrame\",R,N,V_longFrame"
+ "T@\"RawProcInputFrame\",R,N,V_quadraFrame"
+ "T@\"RawProcInputFrame\",R,N,V_referenceEv0Frame"
+ "T@\"RawProcInputFrame\",R,N,V_sifrFrame"
+ "T@\"RawProcInputFrame\",R,N,V_syntheticReferenceFrame"
+ "T@\"RawProcInputFrame\",R,N,V_syntheticReferenceFusionMap"
+ "T@\"RegWarpPP\",&,N,V_registrationPipelineRWPP"
+ "T@\"SyntheticReferencePlist\",&,N,V_tuning"
+ "TB,N,V_doRegistration"
+ "TB,N,V_metadataHasHDRLtmCurvesForBackground"
+ "TI,N,V_tileOverlap"
+ "TIP Espresso context not in invalid state."
+ "TQ,N,V_deviceGeneration"
+ "T^{__CVBuffer=},N"
+ "T^{__CVBuffer=},N,V_regWarpInput"
+ "T^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB},R,N"
+ "T^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB},R,N,V_HDRltmCurves"
+ "T^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB},R,N,V_HDRltmCurvesForBackground"
+ "T^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB},R,N,V_ltmCurves"
+ "T^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB},R,N,V_ltmCurvesForBackground"
+ "Thd not found"
+ "The _postDemosaicTuningDictionary is not valid/nil. Can not read tuning"
+ "The difference between PDP Gain Maps is too large"
+ "The focus pixel map for crosstalk was larger than expected"
+ "The focus pixel map for crosstalk was larger than the expected 64"
+ "The lag defect pixel count should be <= total defect count"
+ "The size of the blendingWeight doesn't match the image size"
+ "The sorted focus pixel list is not the same count as the unsorted list."
+ "Threadgroup size is too big!"
+ "Thumbnail start isn't multiple of 2"
+ "Tile Coord Offset != 0"
+ "Tile Padding is nil/NULL"
+ "Tile padding is neither an NSNumber or NSArray"
+ "TileData has invalid size"
+ "TileHeight not supported"
+ "TileOverlap"
+ "TileWidth not supported"
+ "ToneCurve does not match the first frame."
+ "ToneMappingStage mstmsApplyLumaGain failed"
+ "ToneMappingStage performLTM failed"
+ "ToneMappingStage performSmallFaceFix failed"
+ "ToneMappingStage performToneMapSmoothing failed"
+ "ToneMappingV4::FunctionConstants"
+ "Too many difference in the PDP Gain Map."
+ "Too many frames to fuse"
+ "Too many non-reference frames"
+ "Too many pyramid levels!"
+ "Tuning error: chromaDenoiseMixingCoeff has to be >= 1.0"
+ "Tuning error: lumaDenoiseMixingCoeff   has to be >= 1.0"
+ "Type not found"
+ "T{LearnedNRUniforms={ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}fffffffffffffBBB},N,V_frameProperties"
+ "UB requires an EV0 bracket frame"
+ "Unable perform gaussian pyramid operation."
+ "Unable perform laplacian pyramid operation."
+ "Unable to allocate resources"
+ "Unable to calculate working buffer size"
+ "Unable to create BilateralGrid"
+ "Unable to create CMIDraftDemosaicStage"
+ "Unable to create CMIRawNightModeRegistrationStage"
+ "Unable to create CMIWarpStage"
+ "Unable to create FigRegWarpPPGPU"
+ "Unable to create FusionRemix Stage"
+ "Unable to create RawNMReferenceFrameSelector"
+ "Unable to create RawNightModeFusionInferenceData instance"
+ "Unable to create RawNightModeFusionInferencePyramid instance"
+ "Unable to create RawNightModeGreenGhost"
+ "Unable to create RegDense"
+ "Unable to create RegPyrFusion"
+ "Unable to create RegPyrFusion Stage"
+ "Unable to create RegWarpPP"
+ "Unable to create _awbProcessor"
+ "Unable to create _chromaSuppression"
+ "Unable to create _chromaSuppressionTuningParams"
+ "Unable to create _cmiGuidedFilter"
+ "Unable to create _colorConvertStage"
+ "Unable to create _constrainedRegistrationTuningParams"
+ "Unable to create _inferenceFusion"
+ "Unable to create _learnedNRNetworkStage"
+ "Unable to create _multiFrameOPCTuningParams"
+ "Unable to create _postNetworkTuningParams"
+ "Unable to create _registrationStage"
+ "Unable to create _regwarpTuningParams"
+ "Unable to create _softLTMStage"
+ "Unable to create _textureUtils"
+ "Unable to create _tripodFusion"
+ "Unable to create blit command encoder to populate level 0 of gaussian pyramid."
+ "Unable to create command encoder to perform gaussian pyramid with 5x5 box blur/bilinear pyramid process."
+ "Unable to create command encoder to perform gaussian pyramid."
+ "Unable to create command encoder to perform laplacian pyramid subtraction process."
+ "Unable to create framesAwaitingFusion array"
+ "Unable to determine execution order"
+ "Unable to fuse images"
+ "Unable to init 'BilateralGrid'"
+ "Unable to init 'DenoiseRemixFragmentShader'"
+ "Unable to init 'FuseRemixFragmentShader'"
+ "Unable to init 'FusionRemixUniforms'"
+ "Unable to init 'LumaChromaImage'"
+ "Unable to init 'RegDenseShaders'"
+ "Unable to init 'ToneMappingCurves'"
+ "Unable to initialize LearnedNRProcessor"
+ "Unable to initialize NRFConfig"
+ "Unable to initialize RawDFProcessor"
+ "Unable to initialize RawNightModeProcessor"
+ "Unable to initialize UBProcessor"
+ "Unable to initialize night mode denoise inference"
+ "Unable to initialize night mode fusion inference"
+ "Unable to initialize night mode tripod fusion"
+ "Unable to obtain output format"
+ "Unable to obtain sensor dimensions"
+ "Unable to read LimitMaxGainForeground"
+ "Unable to read MaskedAlpha"
+ "Unable to read MaskedDetailMix"
+ "Unable to read MaskedDetailMix for MSTMv3"
+ "Unable to read MaskedLambda"
+ "Unable to read MinGainRatio"
+ "Unable to read ReadNoiseScaling"
+ "Unable to read ShotNoiseScalingFactor"
+ "Unable to read SkyMaskedDetailMix"
+ "Unable to read SkyMaskedLambda"
+ "Unable to read SmoothingStrength"
+ "Unable to read SpatialSigma"
+ "Unable to read SquaredNoiseScalingFactor"
+ "Unable to read UnmaskedDetailMix"
+ "Unable to read UnmaskedLambda"
+ "Unable to read lumaAddBackBand0Tuning"
+ "Unable to read lumaAddBackClipToSNRTuning"
+ "Unable to read lumaAddBackLSCModulationTuning"
+ "Unable to read lumaAddBackTuning"
+ "Unable to read readNoiseModulationTuning"
+ "Unable to read shotNoiseModulationTuning"
+ "Unable to run RegPyrFusion"
+ "Unable to run green ghost inpainting."
+ "Unable to run green ghost reference mixing."
+ "Unable to set lvl 0 for _nonRefPyr"
+ "Unable to set lvl 0 for _refPyr"
+ "Unable to validate inputs for use with laplacian pyramid."
+ "Unabled to create _inferenceDenoise"
+ "Uneable to create _multiFrameOPC"
+ "Uneable to create _semanticMasks"
+ "Unknown frame type specified"
+ "Unknown input pixel format"
+ "Unknown output pixel format"
+ "Unsupported Bilateral Grid configuration"
+ "Unsupported CFA layout."
+ "Unsupported auxiliary pixel buffer alignment"
+ "Unsupported auxiliary pixel buffer format"
+ "Unsupported bit depth"
+ "Unsupported companding mode"
+ "Unsupported function constant type"
+ "Unsupported pipeline type"
+ "Unsupported: output size is not even"
+ "UseFlexFullRange"
+ "UseHardGainAverageLTM"
+ "UseIspDGainSoftLog"
+ "UseLuxLevelMetadata"
+ "UseSobelDetailModulation"
+ "ValidBufferRect is missing"
+ "ValidBufferRect is missing for RawThumbnail"
+ "Versatile GGBB sensor layout not supported"
+ "Versatile GGRR sensor layout not supported"
+ "VerticalCorrectionWeight not found in ABLEST tuning params"
+ "VerticalMax not found in ABLEST tuning params"
+ "Warning: AWB gains mismatch"
+ "Warning: BilateralChromaSigma is missing; using default value"
+ "Warning: BilateralLowerWeightThreshold is missing; using default value"
+ "Warning: BilateralLumaSigma is missing; using default value"
+ "Warning: BilateralUpperWeightThreshold is missing; using default value"
+ "Warning: ChromaDesatSmoothMixBlend1 is missing; using default value"
+ "Warning: ChromaDesatSmoothMixBlend2 is missing; using default value"
+ "Warning: ChromaDesatSmoothMixLuma1 is missing; using default value"
+ "Warning: ChromaDesatSmoothMixLuma2 is missing; using default value"
+ "Warning: ChromaGray[0] is missing; using default value"
+ "Warning: ChromaGray[1] is missing; using default value"
+ "Warning: ChromaSuppression params is missing; using default value"
+ "Warning: ColorGradientStrength is missing; using default value"
+ "Warning: Constrained is missing; using default value"
+ "Warning: CostLumaDownsampleGamma is missing; using default value"
+ "Warning: DeghostingThreshold is missing; using default value"
+ "Warning: DeghostingThresholdRadius is missing; using default value"
+ "Warning: Demosaic is missing; using default value"
+ "Warning: DiagonalWeight is missing; using default value"
+ "Warning: DiagonalWeightParams[0] is missing; using default value"
+ "Warning: DiagonalWeightParams[1] is missing; using default value"
+ "Warning: DiagonalWeightParams[2] is missing; using default value"
+ "Warning: DirectionalFilterAlways is missing; using default value"
+ "Warning: DirectionalLowpass params is missing; using default value"
+ "Warning: DotDetectThreshold is missing; using default value"
+ "Warning: DotFix is missing; using default value"
+ "Warning: DraftDemosaic is missing; using default value"
+ "Warning: DraftDemosaic::ApplyGDC is missing; using default value"
+ "Warning: EdgeAdaptiveThreshold is missing; using default value"
+ "Warning: EnableAdaptiveGradPushD is missing; using default value"
+ "Warning: EnableAdaptiveGradPushHV is missing; using default value"
+ "Warning: EnableChromaSuppression is missing; using default value"
+ "Warning: EnableDirectionalLowpass is missing; using default value"
+ "Warning: EnableDotFix is missing; using default value"
+ "Warning: EnableGaussianNR is missing; using default value"
+ "Warning: EnableNoiseSuppression is missing; using default value"
+ "Warning: Enabled is missing; using default value"
+ "Warning: FlareDetection is missing; using default value"
+ "Warning: GFilterAlphaClampMax is missing; using default value"
+ "Warning: GFilterAlphaClampMin is missing; using default value"
+ "Warning: GNU is missing; using default value"
+ "Warning: Gamma is missing; using default value"
+ "Warning: GammaMultiFrame is missing; using default value"
+ "Warning: GammaSingleFrame is missing; using default value"
+ "Warning: GaussianD1Strength is missing; using default value"
+ "Warning: GaussianD2Strength is missing; using default value"
+ "Warning: GaussianHStrength is missing; using default value"
+ "Warning: GaussianVStrength is missing; using default value"
+ "Warning: GradComp is missing; using default value"
+ "Warning: GradientDivisor is missing; using default value"
+ "Warning: GradientPushD is missing; using default value"
+ "Warning: GradientPushHV is missing; using default value"
+ "Warning: GradientShiftD is missing; using default value"
+ "Warning: GradientShiftHV is missing; using default value"
+ "Warning: GradientThresholdC is missing; using default value"
+ "Warning: GradientThresholdE is missing; using default value"
+ "Warning: GuidedFilterAlpha is missing; using default value"
+ "Warning: HFDetailBasedSuppressionSlopeEnd is missing; using default value"
+ "Warning: HFDetailBasedSuppressionSlopeStart is missing; using default value"
+ "Warning: HR is missing; using default value"
+ "Warning: HRD is missing; using default value"
+ "Warning: HueBasedSuppressionStrength is missing; using default value"
+ "Warning: HybridBlendingMaskDownsampleGamma is missing; using default value"
+ "Warning: HybridBlendingMaskLumaMismatchGamma is missing; using default value"
+ "Warning: HybridBlendingMaskLumaMismatchSigma is missing; using default value"
+ "Warning: ImageDownsampleGamma is missing; using default value"
+ "Warning: LSC is missing; using default value"
+ "Warning: LocalMotionRejectionSigma is missing; using default value"
+ "Warning: LocalMotionRejectionWeightDownsampleGamma is missing; using default value"
+ "Warning: LocalSharpClip is missing; using default value"
+ "Warning: LumaBasedSuppressionStrength1 is missing; using default value"
+ "Warning: LumaBasedSuppressionStrength2 is missing; using default value"
+ "Warning: LumaBasedSuppressionStrengthLuma1 is missing; using default value"
+ "Warning: LumaBasedSuppressionStrengthLuma2 is missing; using default value"
+ "Warning: LumaCorrectionChromaSigma is missing; using default value"
+ "Warning: LumaCorrectionMaxStrength is missing; using default value"
+ "Warning: MinimumPreviousShiftDistance is missing; using default value"
+ "Warning: MinimumPreviousShiftUpdateDistance is missing; using default value"
+ "Warning: Missing SoftISPTuning is missing; using default value"
+ "Warning: ModulationHigh is missing; using default value"
+ "Warning: ModulationLow is missing; using default value"
+ "Warning: ModulationSlope is missing; using default value"
+ "Warning: MultiFrameOutlierPixelCorrection is missing; using default value"
+ "Warning: NoiseLUT is missing; using default value"
+ "Warning: OPC is missing; using default value"
+ "Warning: OvershootMitigation is missing; using default value"
+ "Warning: PDC is missing; using default value"
+ "Warning: PDP is missing; using default value"
+ "Warning: Per module SoftISPTuning is missing; using default value"
+ "Warning: PhiKnee is missing; using default value"
+ "Warning: PhiSlope is missing; using default value"
+ "Warning: PostDemosaic is missing; using default value"
+ "Warning: QDEM is missing; using default value"
+ "Warning: RNF is missing; using default value"
+ "Warning: RawNoiseFilterShadowBoost is missing; using default value"
+ "Warning: RegularizationLumaSigma is missing; using default value"
+ "Warning: RegularizationSharpness is missing; using default value"
+ "Warning: SADGamma is missing; using default value"
+ "Warning: SharpScaling is missing; using default value"
+ "Warning: Skip is missing; using default value"
+ "Warning: SkipMultiFrame is missing; using default value"
+ "Warning: SkipSingleFrame is missing; using default value"
+ "Warning: SmoothStrengthD is missing; using default value"
+ "Warning: SmoothStrengthHV is missing; using default value"
+ "Warning: StrongEdgeFusionWeightsModulation is missing; using default value"
+ "Warning: TopBandWeightModulation is missing; using default value"
+ "Warning: UseEnlargedHFLumaSupport is missing; using default value"
+ "Warning: UseLocalMaxForNoiseModel is missing; using default value"
+ "Warning: UseSparseChromaSampling is missing; using default value"
+ "Warning: alphaMax is missing; using default value"
+ "Warning: alphaMin is missing; using default value"
+ "Warning: antiMazingGain is missing; using default value"
+ "Warning: antiMazingThresh1 is missing; using default value"
+ "Warning: antiMazingThresh2 is missing; using default value"
+ "Warning: attenuationEnabled is missing; using default value"
+ "Warning: bound is missing; using default value"
+ "Warning: bypassThd is missing; using default value"
+ "Warning: clampEnabled is missing; using default value"
+ "Warning: clampMode is missing; using default value"
+ "Warning: clampScaling is missing; using default value"
+ "Warning: d0 is missing; using default value"
+ "Warning: firStrength is missing; using default value"
+ "Warning: firstPix mismatch"
+ "Warning: flareHOCLBin is missing; using default value"
+ "Warning: flareSubGNU is missing; using default value"
+ "Warning: flashPercentageHigh is missing; using default value"
+ "Warning: flashPercentageLow is missing; using default value"
+ "Warning: gain mismatch"
+ "Warning: gainBypassThreshold is missing; using default value"
+ "Warning: gnuMaxLutK is missing; using default value"
+ "Warning: gnuOffset is missing; using default value"
+ "Warning: gnuStrength is missing; using default value"
+ "Warning: hoclBinMode is missing; using default value"
+ "Warning: input frame already processed"
+ "Warning: inputOffset mismatch"
+ "Warning: ispVersion is missing; using default value"
+ "Warning: lowLightLuxHigh is missing; using default value"
+ "Warning: lowLightLuxLow is missing; using default value"
+ "Warning: maxClamp mismatch"
+ "Warning: outputOffset mismatch"
+ "Warning: pfmSelect is missing; using default value"
+ "Warning: popThdSpe is missing; using default value"
+ "Warning: popThdThd is missing; using default value"
+ "Warning: rawNoiseFilterStrength is missing; using default value"
+ "Warning: rawNoiseFilterStrengthValue is missing; using default value"
+ "Warning: sharpeningControl is missing; using default value"
+ "Warning: strengthFromBlue is missing; using default value"
+ "Warning: strengthFromRed is missing; using default value"
+ "We aren't expecting CMIResouce to be enabled while sharedExternalMemory is off"
+ "White Balance Gain minimum should not be zero"
+ "Wrong band index!"
+ "X0 not found"
+ "XtalkGridOffset not found"
+ "XtalkIntXRecip/XtalkIntYRecip not found"
+ "XtalkShift not found"
+ "Y0 not found"
+ "YCCTex"
+ "YCCTex is NULL"
+ "Zero levels would be allocated/aliased"
+ "ZeroBias not found"
+ "ZimmerDEM tuning parameters not set"
+ "[(id<MTLTextureSPI>)fusionWeights isCompressed] == false is NULL"
+ "[1@\"<MTLComputePipelineState>\"]"
+ "[4@\"<NRFSubProcessor>\"]"
+ "[DenoiseFusePipeline allocateResourcesIfNeededForDesc:didAllocate:] failed"
+ "[NRFProcessor _allocateRegWarpPPWithWidth] failed"
+ "[NRFProcessor _bindRegWarpPPWithWidth] failed"
+ "[SemStyles] Failed to compute histogram and stats"
+ "[SemStyles] Failed to create guide image"
+ "[SemStyles] Failed to process segmentation mattes"
+ "[SemStyles] Failed to render"
+ "[SemStyles] Failed to upsample light map"
+ "[[DeepFusionGaussianPyramid alloc] initWithMetalContext:metal withFilter:GaussianSeparable]"
+ "[[DeepFusionLaplacianPyramid alloc] initWithMetalContext:metal]"
+ "[_stfOutputLTCs contents] is NULL"
+ "[self _compileShaders] == 0 "
+ "^{LearnedNRUniforms={ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}fffffffffffffBBB}16@0:8"
+ "^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}"
+ "^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16@0:8"
+ "_A_tex is NULL"
+ "_HDRltmCurvesForBackground"
+ "_HLGLumaATex"
+ "_HLGLumaATex is NULL"
+ "_MPPComponentMax"
+ "_MPPComputeRWTMOConstants"
+ "_MPPConvertHLGToSDRAndHLGLumaA420"
+ "_MPPConvertHLGToSDRAndHLGLumaA422"
+ "_MPPGainMap420LumaA"
+ "_MPPGainMapMax"
+ "_MPPHLGComputeMaxComponent"
+ "_MPPLog"
+ "_MPPSetEDRToMax"
+ "_accWeightPyramid is NULL"
+ "_addPreviousPyramidLevel = [metal computePipelineStateFor:@\"addPreviousPyramidLevel\" constants:((void *)0) fault:&err]"
+ "_allocateLSCGainDataWithLSCConfig"
+ "_alpha_buf is NULL"
+ "_applyNetworkDeghosting = [metal computePipelineStateFor:@\"applyNetworkDeghosting\" constants:((void *)0) fault:&err]"
+ "_assignedDestinationNames is NULL"
+ "_awbProcessor is NULL"
+ "_backgroundMetal.allocator already defined"
+ "_backgroundMetal.allocator is NULL"
+ "_band"
+ "_bandConsts"
+ "_basicSearchLumaPipelineState is NULL"
+ "_bgBistochastizeFinal = [metal computePipelineStateFor:@\"bg_bistochastize_final\" constants:((void *)0) fault:&err]"
+ "_bgBistochastizeInit = [metal computePipelineStateFor:@\"bg_bistochastize_init\" constants:((void *)0) fault:&err]"
+ "_bgBistochastizeIter = [metal computePipelineStateFor:@\"bg_bistochastize_iter\" constants:((void *)0) fault:&err]"
+ "_bgBlur[blurSelector] = [metal computePipelineStateFor:@\"bg_blur\" constants:constantValues fault:&err]"
+ "_bgNormalize = [metal computePipelineStateFor:@\"bg_norm\" constants:constantValues fault:&err]"
+ "_bgSolverInit1 = [metal computePipelineStateFor:@\"bg_solver_init1\" constants:((void *)0) fault:&err]"
+ "_bgSolverInit2 = [metal computePipelineStateFor:@\"bg_solver_init2\" constants:((void *)0) fault:&err]"
+ "_bgSolverPcgIter0 = [metal computePipelineStateFor:@\"bg_solver_pcg_iter0\" constants:((void *)0) fault:&err]"
+ "_bgSolverPcgIter1 = [metal computePipelineStateFor:@\"bg_solver_pcg_iter1\" constants:((void *)0) fault:&err]"
+ "_bgSolverPcgIter2 = [metal computePipelineStateFor:@\"bg_solver_pcg_iter2\" constants:((void *)0) fault:&err]"
+ "_bgSolverPcgIter3 = [metal computePipelineStateFor:@\"bg_solver_pcg_iter3\" constants:((void *)0) fault:&err]"
+ "_bgSplat[toneMappingGuideEnabled] = [metal computePipelineStateFor:@\"bg_splat\" constants:toneMappingConstant[toneMappingGuideEnabled] fault:&err]"
+ "_bgUpsample16 is NULL"
+ "_bgUpsample16ToneMapped is NULL"
+ "_bgUpsample8 is NULL"
+ "_bilateralGrid is NULL"
+ "_bilinearScalePipelineState is NULL"
+ "_bistochast_m_tex is NULL"
+ "_bistochast_n_tex is NULL"
+ "_blackPoint is NULL"
+ "_blackWhiteStrengthCenter is NULL"
+ "_blendingWeight is NULL"
+ "_blinkDetectionResultBuffer is NULL"
+ "_blueMapPdfStatsBuffer is NULL"
+ "_bypassGTCTex is NULL"
+ "_c1c2Tex is NULL"
+ "_cameraInfoByPortType = nil"
+ "_ccDownsample = [metal computePipelineStateFor:@\"ccDownsample\" constants:((void *)0) fault:&err]"
+ "_clusterFullTex is NULL"
+ "_clusterTex is NULL"
+ "_colorMatchingEnabled"
+ "_computeALSProfileTableWithALSModel"
+ "_computeGrayGhostCount = [metal computePipelineStateFor:@\"computeGrayGhostCount\" constants:((void *)0) fault:&err]"
+ "_computeGrayGhostCountRGB = [metal computePipelineStateFor:@\"computeGrayGhostCountRGB\" constants:((void *)0) fault:&err]"
+ "_confidenceDilate is NULL"
+ "_confidenceErode is NULL"
+ "_confidenceMap is NULL"
+ "_confidenceStageOne is NULL"
+ "_confidence_solved_tex is NULL"
+ "_configForMiwbV2:miwbInputHasCCMApplied:"
+ "_connectionsByDestinationStage is NULL"
+ "_connectionsBySourceStage is NULL"
+ "_constrainedRegistrationParams not set"
+ "_convertColor = [metal computePipelineStateFor:@\"convertColor\" constants:((void *)0) fault:&err]"
+ "_convertColorAndDownsample = [metal computePipelineStateFor:@\"convertColorAndDownsample\" constants:((void *)0) fault:&err]"
+ "_convertColorYCbCr = [metal computePipelineStateFor:@\"convertColorYCbCr\" constants:((void *)0) fault:&err]"
+ "_convertYUV420toRGB = [metal computePipelineStateFor:@\"LearnedNR::convertYUV420toRGB\" constants:((void *)0) fault:&err]"
+ "_createTileForQuadraInput = [metal computePipelineStateFor:@\"LearnedNR::createTileForQuadra\" constants:((void *)0) fault:&err]"
+ "_createTileForRawInput = [metal computePipelineStateFor:@\"LearnedNR::createTileForRawInput\" constants:((void *)0) fault:&err]"
+ "_currentFlickerDetectionBuffer is NULL"
+ "_currentFlickerDetectionBuffer not nil, must get result before running again."
+ "_czDemosaicStage = [metal computePipelineStateFor:@\"czDemosaicStage\" constants:((void *)0) fault:&err]"
+ "_d0_tex is NULL"
+ "_d1_tex is NULL"
+ "_denoiseChroma is NULL"
+ "_denoiseLumaDenoiseRemixChroma is NULL"
+ "_denoiseRemixLuma is NULL"
+ "_denoiseRemixLumaChroma is NULL"
+ "_derivPipelineState = [metal computePipelineStateFor:@\"regpyr_deriv_compute\" constants:((void *)0) fault:&err]"
+ "_derivSobelPipelineState is NULL"
+ "_doRegistration"
+ "_downsampleAndConvert10To8 = [metal computePipelineStateFor:@\"rwppDownsampleAndConvert10To8\" constants:((void *)0) fault:&err]"
+ "_downsampleLuma inputLumaTex is nil"
+ "_downsampleLuma outputLumaTex is nil"
+ "_downsamplePipeline.maxTotalThreadsPerThreadgroup too small"
+ "_downsampleRGBToLuma = [metal computePipelineStateFor:@\"downsampleRGBToLuma\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicMultiChannelBayerPipeline = [_metal computePipelineStateFor:@\"CMIMultiChannelBayerToQuarterLuma\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicMultiChannelQuadra2xPipeline = [_metal computePipelineStateFor:@\"CMIMultiChannelQuadraToLuma2xBBGG\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicMultiChannelQuadra4xPipeline = [_metal computePipelineStateFor:@\"CMIMultiChannelQuadraToLuma4x\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicSingleChannelBayerPipeline = [_metal computePipelineStateFor:@\"CMISingleChannelBayerToQuarterLuma\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicSingleChannelQuadra2xPipeline = [_metal computePipelineStateFor:@\"CMISingleChannelQuadraToLuma2xBBGG\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicSingleChannelQuadra4xPipeline = [_metal computePipelineStateFor:@\"CMISingleChannelQuadraToLuma4x\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicToRGBMultiChannelBayerPipeline"
+ "_draftDemosaicToRGBMultiChannelBayerPipeline = [_metal computePipelineStateFor:@\"CMIMultiChannelBayerToQuarterRGB\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicToRGBMultiChannelQuadra2xPipeline"
+ "_draftDemosaicToRGBMultiChannelQuadra2xPipeline = [_metal computePipelineStateFor:@\"CMIMultiChannelQuadraToRGB2xBBGG\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicToRGBMultiChannelQuadra4xPipeline"
+ "_draftDemosaicToRGBMultiChannelQuadra4xPipeline = [_metal computePipelineStateFor:@\"CMIMultiChannelQuadraToRGB4x\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicToRGBSingleChannelBayerPipeline"
+ "_draftDemosaicToRGBSingleChannelBayerPipeline = [_metal computePipelineStateFor:@\"CMISingleChannelBayerToQuarterRGB\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicToRGBSingleChannelQuadra2xPipeline"
+ "_draftDemosaicToRGBSingleChannelQuadra2xPipeline = [_metal computePipelineStateFor:@\"CMISingleChannelQuadraToRGB2xBBGG\" constants:((void *)0) fault:&err]"
+ "_draftDemosaicToRGBSingleChannelQuadra4xPipeline"
+ "_draftDemosaicToRGBSingleChannelQuadra4xPipeline = [_metal computePipelineStateFor:@\"CMISingleChannelQuadraToRGB4x\" constants:((void *)0) fault:&err]"
+ "_dsrUp"
+ "_ev0"
+ "_ev0RegHomography"
+ "_ev0Up"
+ "_evm"
+ "_evmHRGainDownRatio"
+ "_evmRegHomography"
+ "_evmUp"
+ "_fgbgMatteTex is NULL"
+ "_filterDenoise = [metal computePipelineStateFor:@\"filterDenoise\" constants:((void *)0) fault:&err]"
+ "_filterDenoiseLumaOnly = [metal computePipelineStateFor:@\"filterDenoiseLumaOnly\" constants:((void *)0) fault:&err]"
+ "_finalTargetTex is NULL"
+ "_flickerCountBuffer is NULL"
+ "_focusPixelDeltaBlurMap"
+ "_focusPixelDeltaMap"
+ "_focusPixelExtraction"
+ "_focusPixelExtractionQuadra"
+ "_fragUniBufInt is NULL"
+ "_fragUniBufSBP is NULL"
+ "_frameProperies"
+ "_fuseBlendingWeighPipeline.maxTotalThreadsPerThreadgroup too small"
+ "_fuseConfidenceMap blendingWeight is nil"
+ "_fuseConfidenceMap confidenceMap is nil"
+ "_fusedBand is NULL"
+ "_fusedBand->textureUV[lvl] is NULL"
+ "_fusedBand->textureY[lvl] is NULL"
+ "_fusionBuffers is NULL"
+ "_fusionConf.ltcFrameIndex >= 0 && _inputFrames.frames[_fusionConf.ltcFrameIndex].properties.meta.metadataHasLtmCurves"
+ "_fusionWeights"
+ "_fusionXLumaPipelineState is NULL"
+ "_fusionYLumaPipelineState is NULL"
+ "_gainMapCommandBuffer"
+ "_generateLSCGainMapWithLSCMetadata"
+ "_generateSparseBlendingMapPipeline = [metal computePipelineStateFor:@\"generateSparseBlendingMap\" constants:((void *)0) fault:&err]"
+ "_getALSProfileIDFromMetadata"
+ "_getBlendingWeightLowLightPipeline = [metal computePipelineStateFor:@\"getBlendingWeightLowLight\" constants:((void *)0) fault:&err]"
+ "_getBlendingWeightPipeline = [metal computePipelineStateFor:@\"getBlendingWeight\" constants:((void *)0) fault:&err]"
+ "_getLTM_ltmCurveAndCCMEntryCounts"
+ "_getLensShadingModulationWeightFromFrame"
+ "_getTotalGainFromMetadata:"
+ "_ggFusionWeightsAcc = nil"
+ "_ggFusionWeightsAcc is NULL"
+ "_ggMaxFusionWeights = nil"
+ "_ggMaxFusionWeights is NULL"
+ "_globalDistortionCorrectionByPortType is NULL"
+ "_grayGhostCountBuffer is NULL"
+ "_grayGhostDetection is NULL"
+ "_greentTintCorrectionOrFlickerDetectionInputEV0"
+ "_greentTintCorrectionOrFlickerDetectionInputEVM"
+ "_grid_tex is NULL"
+ "_guideTex is NULL"
+ "_guidedFilter is NULL"
+ "_hasRegroupedLayout"
+ "_hasconverged_buf is NULL"
+ "_hazeCorrectionQuadra"
+ "_hazeDetection"
+ "_hazeDomination"
+ "_highlightCompression is NULL"
+ "_ignoreMapTex is NULL"
+ "_inferenceSourceImg"
+ "_initialDownScalePipelineState is NULL"
+ "_initialDownScaleRGBPipelineState is NULL"
+ "_inputBands->bands[i]->textureUV[lvl] is NULL"
+ "_inputBands->bands[i]->textureY[lvl] is NULL"
+ "_inputConnections is NULL"
+ "_inputFrames cannot be nil"
+ "_inputFrames is NULL"
+ "_internalHeap is NULL"
+ "_isFlexFullRange"
+ "_isHLGStillCase"
+ "_kernelWithFunctionConstant[i][comboFlags]"
+ "_kernel[i]"
+ "_l0_buf is NULL"
+ "_l1_buf is NULL"
+ "_learnedNRNetworkStage"
+ "_learnedNRSubProcessorEnabled"
+ "_lightMapSmallTex is NULL"
+ "_lightMapTex is NULL"
+ "_localIllMapTex is NULL"
+ "_longFrameIndex"
+ "_lscGainsTex is nil"
+ "_ltcBinsBackgroundTexD4x is NULL"
+ "_ltcBinsTexD3x is NULL"
+ "_ltcBinsTexD4x is NULL"
+ "_ltcGTCFinalBackgroundTex is NULL"
+ "_ltcGTCFinalTex is NULL"
+ "_ltcGTCRatioBackgroundTex is NULL"
+ "_ltcGTCRatioTex is NULL"
+ "_ltmApplyShaders"
+ "_lumaAddbackForRawInput = [metal computePipelineStateFor:@\"LearnedNR::lumaAddbackForRawInput\" constants:((void *)0) fault:&err]"
+ "_lumaHistogram is NULL"
+ "_maskMB is NULL"
+ "_maskMB.width % 2 == 0 && _maskMB.height % 2 == 0 is NULL"
+ "_maskSB is NULL"
+ "_maxScaling"
+ "_maxVariationTex is NULL"
+ "_max_grid_confidence is NULL"
+ "_metadataHasHDRLtmCurvesForBackground"
+ "_metal is NULL"
+ "_metal.allocator already defined"
+ "_metal.allocator is NULL"
+ "_metal.allocator is nil"
+ "_metalContext.allocator is NULL"
+ "_metalExecutionStatus is NULL"
+ "_miwbModuleConfigPlistDictByPortType is NULL"
+ "_miwbStage.configured is NULL"
+ "_moduleConfig is NULL"
+ "_motionDetectDiffGradient = [metal computePipelineStateFor:@\"motionDetectDiffGradient\" constants:((void *)0) fault:&err]"
+ "_motionDetectDilate = [metal computePipelineStateFor:@\"motionDetectDilate\" constants:((void *)0) fault:&err]"
+ "_motionDetectGenClippingMapAndDownscale = [metal computePipelineStateFor:@\"kernelMotionDetectGenClippingMapAndDownscale\" constants:((void *)0) fault:&err]"
+ "_motionDetectGenClippingMapAndDownscaleLinear = [metal computePipelineStateFor:@\"kernelMotionDetectGenClippingMapAndDownscaleLinear\" constants:((void *)0) fault:&err]"
+ "_motionDetectGradient = [metal computePipelineStateFor:@\"motionDetectGradient\" constants:((void *)0) fault:&err]"
+ "_motionDetectLL = [metal computePipelineStateFor:@\"motionDetectLL\" constants:((void *)0) fault:&err]"
+ "_motionDetectLLDownscale = [metal computePipelineStateFor:@\"motionDetectLLDownscale\" constants:((void *)0) fault:&err]"
+ "_motionDetectLLSumReduce = [metal computePipelineStateFor:@\"motionDetectLLSumReduce\" constants:((void *)0) fault:&err]"
+ "_motionDetectMaxTileAvg = [metal computePipelineStateFor:@\"motionDetectMaxTileAvg\" constants:((void *)0) fault:&err]"
+ "_motionDetectScore is NULL"
+ "_motionDetectWarp = [metal computePipelineStateFor:@\"motionDetectWarp\" constants:((void *)0) fault:&err]"
+ "_motionDetection is NULL"
+ "_mstmTuningParams is NULL"
+ "_mstmv2TuningParams is NULL"
+ "_mustRunDetection"
+ "_networkModel"
+ "_nonRefPyr is NULL"
+ "_nonRefPyr->textureY[lvl] is NULL"
+ "_nrfConfig is nil"
+ "_nrfPlist->ev0RefDenoising"
+ "_nrfPlist->evmRefDenoising"
+ "_numTilesOverThreshold is NULL"
+ "_outputAsMTLBuffer is NULL"
+ "_outputConnections is NULL"
+ "_paramsBuf is NULL"
+ "_passes"
+ "_patchDistances is NULL"
+ "_pendingResultCommandBuffer not nil, must get result before running again."
+ "_personMask is NULL"
+ "_pipeline is NULL"
+ "_pipelineStates[PROGRAM_COMPUTE_REPAIRVALS] = [_metal computePipelineStateFor:[self functionNameForProgram:PROGRAM_COMPUTE_REPAIRVALS] constants:((void *)0) fault:&err]"
+ "_pipelineStates[PROGRAM_CROP] = [_metal computePipelineStateFor:[self functionNameForProgram:PROGRAM_CROP] constants:((void *)0) fault:&err]"
+ "_pipelineStates[PROGRAM_PROCESS_REPAIRVALS] = [_metal computePipelineStateFor:[self functionNameForProgram:PROGRAM_PROCESS_REPAIRVALS] constants:((void *)0) fault:&err]"
+ "_pipelineStates[PROGRAM_REFINE_MASK] = [_metal computePipelineStateFor:[self functionNameForProgram:PROGRAM_REFINE_MASK] constants:((void *)0) fault:&err]"
+ "_pipelineStates[PROGRAM_REPAIR] = [_metal computePipelineStateFor:[self functionNameForProgram:PROGRAM_REPAIR] constants:((void *)0) fault:&err]"
+ "_pipelineStates[PROGRAM_UNCROP] = [_metal computePipelineStateFor:[self functionNameForProgram:PROGRAM_UNCROP] constants:((void *)0) fault:&err]"
+ "_playbackCurve is NULL"
+ "_postNetworkTuningParams is missing"
+ "_processDenoisedRgbForRawInput = [metal computePipelineStateFor:@\"LearnedNR::processDenoisedRgbForRawInput\" constants:((void *)0) fault:&err]"
+ "_processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:calldelegate:inferenceMetadata:"
+ "_processorOutput"
+ "_processorOutputGainMapHeadroom"
+ "_pyr is NULL"
+ "_pyr->textureUV[chroma_level] is NULL"
+ "_pyrConfidence is NULL"
+ "_pyrHomographyTeleIsRef[lvl] is NULL"
+ "_pyrHomographyWideIsRef[lvl] is NULL"
+ "_pyrRoiScaleLevel0[CAMERA_TELE] is NULL"
+ "_pyrRoiScaleLevel0[CAMERA_WIDE] is NULL"
+ "_pyrScaleParamLevel0[CAMERA_TELE] is NULL"
+ "_pyrScaleParamLevel0[CAMERA_WIDE] is NULL"
+ "_pyrScaleParams[lvl] is NULL"
+ "_q_tex is NULL"
+ "_rawDFDetectors"
+ "_rawNightModeTuningParameters is nil"
+ "_rawNightModeTuningParameters[LowLightGreenGhost] is nil"
+ "_refChroma is NULL"
+ "_refPyr is NULL"
+ "_refPyr->textureY[lvl] is NULL"
+ "_referenceLSCGainsTex is nil"
+ "_referenceLumaTex is nil"
+ "_regDense is NULL"
+ "_regWarpGPU is NULL"
+ "_remixLuma is NULL"
+ "_repairValues is NULL"
+ "_requestedSyntheticReferenceMode"
+ "_residual0_tex is NULL"
+ "_residual1_tex is NULL"
+ "_residual_buf is NULL"
+ "_rgbThumbnail"
+ "_rgbThumbnailQuadra"
+ "_runMotionDetector"
+ "_scaleEv0Brightness"
+ "_scaleEvmBrightness"
+ "_selectionLumaPipelineState is NULL"
+ "_semanticStylesStage is NULL"
+ "_sensThumbnailTex is NULL"
+ "_setupFusionConfig failed."
+ "_sffDescriptorsBuffer is NULL"
+ "_sffNThreadGroupsBuffer is NULL"
+ "_shaders is NULL"
+ "_shaders->_MPPGainMapAdjust is NULL"
+ "_shaders->_MPPGainMapAdjustFlexRange is NULL"
+ "_shaders->_MPPGainMapMax"
+ "_shaders->_MPPGainMapMax is NULL"
+ "_shaders->_MPPHistExtract is NULL"
+ "_shaders->_MPPHistogram is NULL"
+ "_shaders->_MPPLog"
+ "_shaders->_MPPLog is NULL"
+ "_shaders->_MPPLogGainMapMinMax is NULL"
+ "_shaders->_MPPSetEDRToMax"
+ "_shaders->_MPPSetEDRToMax is NULL"
+ "_shaders->_gainMapDownsampledFilter is NULL"
+ "_shaders->_gainMapFilter is NULL"
+ "_shaders->_ssCalculateGlobalHistogram is NULL"
+ "_shaders->_ssCalculateGlobalStats is NULL"
+ "_shaders->_ssCalculateLocalHistogramStats is NULL"
+ "_shaders->_ssCreateGuide is NULL"
+ "_shaders->_ssRenderAdjustments is NULL"
+ "_sharedEvent is NULL"
+ "_sharedEventListener is NULL"
+ "_sharpeningPyramid->textureY[luma_level] is NULL"
+ "_shiftMap is NULL"
+ "_sizeGranularity"
+ "_skinMask is NULL"
+ "_skinMaskBlurredTex is NULL"
+ "_skinMaskTex is NULL"
+ "_skyMask is NULL"
+ "_skyMaskBlurredTex is NULL"
+ "_skyMaskTex is NULL"
+ "_smoothPipelineState is NULL"
+ "_spatialCCMTex is NULL"
+ "_srlOnMSTMTuningParams is NULL"
+ "_srlV2CoeffsBuffer is NULL"
+ "_srlV2FaceStatsBuffer is NULL"
+ "_srlV2GlobalStatsBuffer is NULL"
+ "_stageConfig"
+ "_stagesByName is NULL"
+ "_statsBuf is NULL"
+ "_stfOutputLTCs is NULL"
+ "_stfProcessor is NULL"
+ "_stfThumbnailTex is NULL"
+ "_styleEngineProcessor is NULL"
+ "_subProcessors[NRFSubProcessorType_LearnedNR]"
+ "_subjectRelight is NULL"
+ "_sumLumaChromaMask is NULL"
+ "_sumMaskBuffer is NULL"
+ "_sumTexture"
+ "_textureArgs"
+ "_textureArgsFinal"
+ "_textureArgsMain"
+ "_textureArgsUp"
+ "_textureUtils is NULL"
+ "_tileOverlap"
+ "_tmp_grid_tex is NULL"
+ "_toneMapSmoothingResources allocateResourcesForWidth failed"
+ "_toneMappingCurves is NULL"
+ "_topBand"
+ "_tuningParams is NULL"
+ "_uniforms is NULL"
+ "_uniformsHeap is NULL"
+ "_uniforms[i] is NULL"
+ "_uniforms_UV[lvl] is NULL"
+ "_uniforms_Y[lvl] is NULL"
+ "_unregularizedForegroundLTC is NULL"
+ "_unregularizedLTC is NULL"
+ "_untileAndConvert444To420 = [metal computePipelineStateFor:@\"untileAndConvert444To420\" constants:((void *)0) fault:&err]"
+ "_useDraftDemForInferenceAndGainMap"
+ "_useHardGainAverageLTM"
+ "_useMotionDetector"
+ "_vertexUniBufSBP is NULL"
+ "_warpAdditionalFrameWithBlendingWeightPipeline[i] = [metal computePipelineStateFor:@\"warpAdditionalFrameWithBlendingWeight\" constants:constantValues fault:&err]"
+ "_warpPipeline[i] = [metal computePipelineStateFor:@\"warpFrame\" constants:constantValues fault:&err]"
+ "_warpRGBAWithBlendingWeightAndConfidencePipeline[i] = [metal computePipelineStateFor:@\"warpRGBAFrameWithBlendingWeightAndConfidence\" constants:constantValues fault:&err]"
+ "_warpWithBlendingWeightAndConfidencePipeline[i] = [metal computePipelineStateFor:@\"warpFrameWithBlendingWeightAndConfidence\" constants:constantValues fault:&err]"
+ "_warpWithBlendingWeightPipeline[i] = [metal computePipelineStateFor:@\"warpFrameWithBlendingWeight\" constants:constantValues fault:&err]"
+ "_warpWithConfidencePipeline[i] = [metal computePipelineStateFor:@\"warpFrameWithConfidence\" constants:constantValues fault:&err]"
+ "_weightPlanesArrayTex is NULL"
+ "_wpStatsBuffer is NULL"
+ "_x0_tex is NULL"
+ "_x1_tex is NULL"
+ "ablestConfig is NULL"
+ "accumulateMaxComponentShader"
+ "accumulateMaxComponentShader is NULL"
+ "accumulation of weights texture is nil"
+ "accumulator = nil"
+ "accumulatorBand0Texture is NULL"
+ "activeLine too large."
+ "activeLineCount too large."
+ "addConnection (BayerProc -> rawMBNR) failed"
+ "addConnection (DEM(Luma) -> postDemProc) failed"
+ "addConnection (GDC -> LTM) failed"
+ "addConnection (GDC(Chroma) -> Output(Chroma)) failed"
+ "addConnection (GDC(Luma) -> Output(Luma)) failed"
+ "addConnection (Input -> RawScale) failed"
+ "addConnection (RawScale -> BayerProc) failed"
+ "addConnection (YSH -> GDC(Luma)) failed"
+ "addConnection (postDemProc(Chroma) -> GDC(Chroma)) failed"
+ "addConnection (postDemProc(Luma) -> YSH) failed"
+ "addConnection (rawMBNR -> DEM) failed"
+ "addConnection 1 failed"
+ "addConnection 10 failed"
+ "addConnection 11 failed"
+ "addConnection 12 failed"
+ "addConnection 13 failed"
+ "addConnection 14 failed"
+ "addConnection 17 failed"
+ "addConnection 18 failed"
+ "addConnection 2 failed"
+ "addConnection 3 failed"
+ "addConnection 4 failed"
+ "addConnection 5 failed"
+ "addConnection 6 failed"
+ "addConnection 7 failed"
+ "addConnection 8 failed"
+ "addConnection 9 failed"
+ "addConnection SyntheticThumbnail for (RawScale -> BayerProc) failed"
+ "addConnection failed"
+ "addFrame requires a valid frame"
+ "addbackClippingPyrTextures allocation failed"
+ "addbackParams is NULL"
+ "alignment == 4"
+ "allocateBufsIfNeeded"
+ "allocation of sharedRegWarpBuffer failed"
+ "allocationInfo argument nil"
+ "allocatorBackend is  nil"
+ "allocatorDesc is NULL"
+ "alphaRatio not found"
+ "analogGain must be above 0"
+ "applyLTMStage addStage failed"
+ "applyOverrides failed"
+ "args is nil"
+ "args.bounds is nil"
+ "args.flatThdLutTex is NULL"
+ "args.inputFrame is nil"
+ "args.outputFrame is nil"
+ "args.pdpGainTex is NULL"
+ "args.staticDefectTable is NULL"
+ "args.xtalkLutTex is NULL"
+ "argsForStage nil"
+ "array not found"
+ "auto"
+ "auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:alignmentOut:"
+ "auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:alignmentOut:"
+ "auxiliaryPixelFormats is NULL"
+ "awbComputedGOCGains invalid"
+ "awbComputedGains invalid"
+ "awbConfig is NULL"
+ "awbConfig[@\"CSC\"][@\"CSCOffset\"][1] is NULL"
+ "awbConfig[@\"CSC\"][@\"CSCOffset\"][2] is NULL"
+ "awbConfig[@\"Histogram\"][@\"Config\"][@\"C1Scale\"] is NULL"
+ "awbConfig[@\"Histogram\"][@\"Config\"][@\"C2Scale\"] is NULL"
+ "backgroundCommandBuffer is NULL"
+ "band0 of accumulator has not been allocated"
+ "band0FusionStrength should be a NSArray"
+ "band_data->lumaFusionStrength->ev0->sparse_static_scene is NULL"
+ "baseModulation >= 0.0f"
+ "basePolynomialData is NULL"
+ "batch = nil"
+ "batch is nil"
+ "batch metadata doesn't have firstLast flags"
+ "batch.accumulator is nil"
+ "batch.accumulator.bandTextures[x] is nil"
+ "bayerProc addStage failed"
+ "bd is NULL"
+ "biasParams is NULL"
+ "bilateralGridOn"
+ "blackLevelEstimationConfig is NULL"
+ "blackLevelShadingCorrectionThumbnails is incorrect class"
+ "blackLevelShadingCorrectionThumbnails is nil"
+ "blacklevelShadingCorrection is nil"
+ "blinkDetectionComputePipeline = [metal computePipelineStateFor:@\"BlinkDetection\" constants:((void *)0) fault:&err]"
+ "blinkDetectionPlist readPlist failed"
+ "blitEnc is NULL"
+ "blitEncoder is NULL"
+ "blobMask is NULL"
+ "block size too big or small"
+ "blockIndex too large."
+ "blueVertMinSharpFactor not found"
+ "blurredTex1 is NULL"
+ "blurredTex2 is NULL"
+ "bodyMaskPyrTextures allocation failed"
+ "bounds is NULL"
+ "bounds is nil"
+ "bounds nil"
+ "bounds nil on h13Args"
+ "brightnessMask is NULL"
+ "buffer is NULL"
+ "bufs->fusedChromaTex is NULL"
+ "bufs->fusedLumaTex is NULL"
+ "bufs->noiseMapChromaTex is NULL"
+ "bufs->noiseMapLumaTex is NULL"
+ "bufs->outLumaTex is NULL"
+ "bufs->simMapTex is NULL"
+ "but no"
+ "calculate3DThreadgroupSize"
+ "calculateDerivedAdjustmentParameters"
+ "calculateLTMOnDraftDemosaicEV0Frame:evmFrame:"
+ "calculateOISOffset"
+ "calibration is nil"
+ "cameraInfo is NULL"
+ "cameraInfo not available for calculating OIS offset"
+ "cameraInfoByPortType is NULL"
+ "cameraInfoByPortType is nil"
+ "cameraInfoByPortType property needs to be set before prepareToProcess."
+ "canvas addStage failed"
+ "cb is NULL"
+ "ccmCoef is NULL"
+ "ccmCoef.count == 9 is NULL"
+ "chroma texture pixel format not recognized"
+ "chromaScratch is not valid"
+ "chromaTex is NULL"
+ "chroma_out is NULL"
+ "cicGrid type is expected to be version 1"
+ "cicGridData.length is smaller than header struct"
+ "cmdBuf is NULL"
+ "cmdBuffer is NULL"
+ "cmdEnc is NULL"
+ "cmdEnc nil"
+ "cmdEncoder is NULL"
+ "cmdbuf is NULL"
+ "cmeanTex is NULL"
+ "coeffTex is NULL"
+ "coeffs NULL"
+ "colorCubeFix called with ColorCubeFixType_noFix"
+ "command buffer cannot be nil"
+ "command buffer for computing pyramids is nil."
+ "commandBuf is NULL"
+ "commandBuffer is NULL"
+ "commandEncoder is NULL"
+ "commandEncoder nil"
+ "commonInit"
+ "compand10To8"
+ "compareGOCConfig"
+ "compareHRConfig"
+ "compile"
+ "compileShader:lumaWrite:chromaWrite:error:"
+ "completionStatus.commandBuffer is NULL"
+ "compute gray ghost failed"
+ "computeAverageCurve:withLTM:ltmGridX:ltmGridY:andGTC:andLtmHardGain:"
+ "computeEnc is NULL"
+ "computeEncoder is NULL"
+ "computeFusionParams failed."
+ "computeGainMapWithInput:secondInput:HLGLumaAInput:output:properties:mpconfig:"
+ "computeLTM addConnection failed"
+ "computeLTM addStage failed"
+ "computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:"
+ "computeLTMStage init failed"
+ "computeMaxComponentShader"
+ "computeMaxComponentShader is NULL"
+ "computePipelineStateFor:constants:fault:"
+ "computeRWTMOConstantsShader"
+ "computeRWTMOConstantsShader is NULL"
+ "computeShader"
+ "computeShader is NULL"
+ "confidenceMap is NULL"
+ "confidence_tex is NULL"
+ "config NULL"
+ "config is NULL"
+ "config is nil"
+ "config nil"
+ "config object must be instance of SoftISPPipelineConfig"
+ "config.enableBlendClippedHue mismatch"
+ "config.enableBlendHPPPTarget mismatch"
+ "config.enableBlendInput mismatch"
+ "config.enableNormTargetHue mismatch"
+ "config.enableSoftClip mismatch"
+ "config.greenSelBlue mismatch"
+ "config.greenSelRed mismatch"
+ "config.ignoreLSC mismatch"
+ "config.recovMethod mismatch"
+ "config.scHueRefChannel mismatch"
+ "connection init failed"
+ "connections is NULL"
+ "connectionsFromCurrentStage nil"
+ "connectionsToPropagate is NULL"
+ "constantValues is NULL"
+ "constrainedRegApplyGrid.maxTotalThreadsPerThreadgroup insufficient"
+ "context is NULL"
+ "convertHLGToSDRWithInputPixelBuffer:outputImage:"
+ "convertHLGYCCTexture:toSDRYTexture:CbCrTexture:andHLGLumaATexture:isP3Input:"
+ "convertStage addStage failed"
+ "convertToU16Stage addStage failed"
+ "copyTotalSensorCropRectFrom:to:"
+ "correctionType out of bounds."
+ "cps is NULL"
+ "cps is nil"
+ "createFastQBinSushiRawMBNRYUVPipeline"
+ "createH13FastRawNightModePipeline"
+ "createH13FastSashimiDisparityPipeline"
+ "createH13FastSashimiPipeline"
+ "createH13FastSushiPipeline"
+ "createH13FastSushiPipeline1C"
+ "createH13FastSushiPipelineLTM"
+ "createH13FastSushiQuadraRawMBNRLTMPipeline1C"
+ "createH13FastSushiRawMBNRPipeline"
+ "createH13FastSushiRawMBNRPipeline1C"
+ "createH13FastSushiRawMBNRPipelineLTM1C"
+ "createH13FastSushiRawMBNRYUVDebugPipeline"
+ "createH13FastSushiRawMBNRYUVGDCPipeline"
+ "createH13FastSushiRawMBNRYUVPipeline"
+ "createH13FastSushiRegWarpPipeline"
+ "createH13FastSushiYUVPipeline"
+ "createH13FastSushiYUVQuadraPipeline"
+ "createH13QBinFastSushiRawMBNRPipelineLTM1C"
+ "createH13QBinFastSushiRawMBNRYUVLTMPipeline"
+ "createPipelineStateWithMetal:vShaderName:fShaderName:outputColorMetalFormat:"
+ "createPipelineStateWithMetal:vShaderName:fShaderName:outputColorMetalFormat:constantValues:"
+ "createPipelines"
+ "createShaderWithOptions:error:"
+ "cropGridPattern"
+ "cropOISEnabledLSCCICGridForFrame"
+ "croppedChroma is NULL"
+ "croppedLuma is NULL"
+ "crosstalk bitDepth is not consistent"
+ "crosstalk bitDepth not found in xtalk map headers"
+ "crosstalk precision is not consistent"
+ "crosstalk precision not found in xtalk map headers"
+ "cscCoef is NULL"
+ "cscCoef.count == 9 is NULL"
+ "cscConfig is NULL"
+ "cscParams is NULL"
+ "current config not set"
+ "current pipeline not set"
+ "currentFusionWeights is NULL"
+ "currentStage nil"
+ "currentStageArgs nil"
+ "darkEdgeSuppressionTuning readPlist failed"
+ "decompand8To10ToU16"
+ "decompand8To12To10ToU16"
+ "defectLocationCount should be > 0"
+ "defectLocationCountToRemove is nil"
+ "defectLocationCountToRemove should be > 0"
+ "defectLocations is nil"
+ "defectTable is NULL"
+ "defectivePixelsData.length is smaller than header struct, cannot read."
+ "deghostingThresholdRadius should be > 0"
+ "delegate not set"
+ "deltaBlurMap"
+ "deltaMap"
+ "demYUV addStage failed"
+ "demosaicParameters is NULL"
+ "denoiseAndSharpening readPlist failed"
+ "denoiseSingleImage expects input height to match pyramid levels count"
+ "denoiseSingleImage expects input width to match pyramid levels count"
+ "denoiseSingleImage expects output height to match pyramid levels count"
+ "denoiseSingleImage expects output width to match pyramid levels count"
+ "denoisedLumaPyrTexArray[b] is NULL"
+ "denoisedLumaPyrTextures allocation failed"
+ "denoisedRgbTileTex is NULL"
+ "denoisingOptions is NULL"
+ "desc is NULL"
+ "destinationPropertyName is NULL"
+ "destinationStageName is NULL"
+ "destinationUniqueName is NULL"
+ "detect flicker scene failed"
+ "determineCFALayout"
+ "determineCFALayoutForVersatileCVPixelBufferWithBayerPattern"
+ "determineCFALayoutWithBayerPattern"
+ "determineCompandingMode"
+ "determineCompressedOutputPixelFormat"
+ "determineFirstPixel"
+ "determineFirstPixelForCVPixelFormat"
+ "determineFirstPixelForVersatileCVPixelBuffer"
+ "determineFirstPixelForVersatileCVPixelBufferWithBayerPattern"
+ "determineFirstPixelWithBayerPattern"
+ "determineInputBitDepth"
+ "determineMTLPixelFormatsForCVPixelFormat"
+ "determineNonCompandedPixelFormat"
+ "diffTex is NULL"
+ "dilateTex is nil"
+ "disparityStage addStage failed"
+ "dispatchInfo"
+ "dispatchThreads"
+ "div_serial_intN"
+ "doGainMap failed"
+ "doGainMapOnSingleFrameLuma:chroma:HDRLumaA:properties:output:outputHeadroom:nrfPlist:"
+ "doHazeEstimation failed"
+ "doRegistration"
+ "downsampleM2M failed"
+ "downscaledChroma is NULL"
+ "downscaledLuma is NULL"
+ "dsr"
+ "dsrUp"
+ "dstChromaTex is NULL"
+ "dstLumaTex is NULL"
+ "enableBlendClippedHue != 1"
+ "enableBlendHPPPTarget != 1"
+ "enableBlendInput != 1"
+ "enableNormTargetHue != 1"
+ "enableSoftClip != 1"
+ "encoder is NULL"
+ "entry is not a NSNumber"
+ "entryDefaultSensorIDs is NULL"
+ "equalBayerWeights is missing"
+ "err"
+ "err = [self _compileShaders] == 0 "
+ "err = [self compileShaders] == 0 "
+ "err == noErr is NULL"
+ "espresso context not in valid state"
+ "estimateLTMSoftGainFromFrameProperties"
+ "ev0RefDenoising"
+ "ev0Up"
+ "ev0_pyr_%d"
+ "evmRefDenoising"
+ "evmTex is NULL"
+ "evmUp"
+ "evm_pyr_%d"
+ "expected GlobalLTMLookUpTable to have 257 bins"
+ "expected lumaBaseAddr < chromaBaseAddr"
+ "exposureGain evaluated to 0"
+ "exposureTime not found"
+ "externalMemoryResource is NULL"
+ "faceBodyBoundaries is NULL"
+ "faceRects"
+ "facesScores.count is different than faceRects.count"
+ "false"
+ "filteredDefectLocations allocation failed"
+ "finalLscGridSize.x == finalCicGridSize.x && finalLscGridSize.y == finalCicGridSize.y"
+ "finalizeFrames"
+ "firstFrame.properties is NULL"
+ "firstPix mismatch"
+ "firstPix only supports R/B"
+ "firstPixelFromBayerPhase"
+ "flexRangeMetadataDictionary:mppHeadroom:newHeadroom:fullRange:"
+ "flicker scene detected, return EV0"
+ "flickerDetection"
+ "flushIOUnifiedAddressTranslatorWithDummyBuffer"
+ "focusPixelBlockLayout.size.y > 32 not currently supported."
+ "focusPixelDeltaBlurMap"
+ "focusPixelDeltaMap"
+ "focusPixelExtraction"
+ "focusPixelExtractionQuadra"
+ "forced enabled"
+ "foregroundLTCs is NULL"
+ "format should be 420v"
+ "fpLeft"
+ "fpRight"
+ "frame = nil"
+ "frame is NULL"
+ "frame is nil"
+ "frame metadata dict is nil"
+ "frame object is nil"
+ "frame pixelBuffer is nil"
+ "frame properties is NULL"
+ "frame textures is NULL"
+ "frameSelectionPlist readPlist failed"
+ "framesTilesTexture is NULL"
+ "fromPort:"
+ "fromPort:withScale:"
+ "function constant type (from Metal) not supported."
+ "functionConstantName not found in valueDictionary"
+ "fusedBands->textureUV[1] is NULL"
+ "fusedBands->textureUV[band] is NULL"
+ "fusedBands->textureY[1] is NULL"
+ "fusedBands->textureY[band] is NULL"
+ "fusion->lensShadingFactorLUT is NULL"
+ "fusion->nonShadowDenseBlendStrength is NULL"
+ "fusion->shadowDenseBlendStrength is NULL"
+ "fusionData readPlist failed"
+ "fusionDataObj is NULL"
+ "fusionParams is nil"
+ "fusionRemixStage runFusionForBandIndex (similarity map) failed"
+ "fusionRemixStage runFusionForBandIndex failed"
+ "fusionTuningParams is nil"
+ "fusionWeights"
+ "fusion_update_band_data"
+ "gainMapOutputTexture is NULL"
+ "gainMapTexHalf is NULL"
+ "gaussian1D"
+ "gdcYUV addStage failed"
+ "genHorizFirH14"
+ "genVertFir"
+ "generateGOCConfigFromRegistersDict"
+ "generateGainMapIfNeeded"
+ "generateLSCGainsRGBAFromCameraInfoByPortType"
+ "generatePDPConfigFromRegistersDict"
+ "generatePDPGainsFromInputFrameMetadata"
+ "generatePDPGainsFromRegistersDict"
+ "generateRNFConfigFromInputFrameMetadata"
+ "generateRNFConfigFromRegisters"
+ "geometricDistortionCoefficients is NULL"
+ "getAffineTransformFromExifOrientation"
+ "getBayerMBNRSettingsForBandFromTuningParams"
+ "getBlackLevelShadingThumbnail"
+ "getChromaMBNRSettingsForBandFromTuningParams"
+ "getClippingDataFromMetadata"
+ "getDescForRGB"
+ "getDetectorsResultsSync:"
+ "getExposureParameters"
+ "getFloatParameter"
+ "getFloatValue"
+ "getGDCParametersWithCameraInfoByPortType"
+ "getHazeCorrectionConfigForInputFrame:pdpConfig:hazeCorrectionConfig:"
+ "getHazeCorrectionEnabledForInputFrame:enabled:"
+ "getIntParameter"
+ "getLSCConfigForInputFrame"
+ "getLSCGainsForInputFrame"
+ "getLTMCurvesFromMetadataWithKeys"
+ "getLTM_data"
+ "getLTM_leftPadding"
+ "getLTM_lutsBytesPerColumn"
+ "getLTM_lutsBytesPerRow"
+ "getLTM_lutsCountX"
+ "getLTM_lutsCountY"
+ "getLTM_spatialCCMEntry"
+ "getLTM_tileHeight"
+ "getLTM_tileWidth"
+ "getLTM_topPadding"
+ "getLTM_validHeight"
+ "getLTM_validWidth"
+ "getLocalMaxForNoiseModelEnabled"
+ "getLumaChromaNoiseThreshold"
+ "getMBNRSettingsFromTuningParams"
+ "getMaxLSCGainFromLSCGridData"
+ "getMotionDetectionSyncResult:"
+ "getNRFTuningForSensor"
+ "getNRFTuningForSensor: sensor ID key is either NULL or not containing a valid hex representation, bailing"
+ "getNetworkPath:isE5:"
+ "getNoiseBayerBoostForBandFromTuningParams"
+ "getROIMetadata"
+ "getRawNoiseFilterShadowBoost"
+ "getRawNoiseFilterStrength"
+ "getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:outRegDenseMapProperties:"
+ "getSrlBoostedLTMasNSData:"
+ "getSubDict"
+ "getThreadsToDispatch:"
+ "getTileOverlapForGain:table:"
+ "getTuning failed"
+ "getTuningFrom:forCaptureType:"
+ "gfIntermTex is NULL"
+ "gicDataHeader->version == FigCaptureStreamHybridOCLRedBlueCrosstalkGridVersion_1"
+ "globalLTMCurve is NULL"
+ "globalLtmLut NULL"
+ "globalLumaCurve nil"
+ "globalToneCurveLut NULL"
+ "gnuOutputTexs.grgbGNUTex is NULL"
+ "gnuOutputTexs.outputTex is NULL"
+ "gocConfig NULL"
+ "gpu only supports box filter"
+ "gradient is NULL"
+ "graph is NULL"
+ "graph nil"
+ "grayGhostDetection"
+ "greenGhostBrightLightTuningParams readPlist failed"
+ "greenGhostLowLightTuningParams readPlist failed"
+ "greenMask is NULL"
+ "gridLeft and gridRight have different intervals"
+ "gridLeft or gridRight is not available"
+ "gtcFrameIndex not valid"
+ "guideTex is NULL"
+ "guide_tex is NULL"
+ "h13Args nil"
+ "h13Args.bounds is nil"
+ "h13Args.inputFrame is nil"
+ "haloSuppressionTuning readPlist failed"
+ "handle_per_reference_band_data"
+ "has been"
+ "hasn't been"
+ "hazeAdjustedGTC is NULL"
+ "hazeCorrectionConfig is NULL"
+ "hazeCorrectionQuadra"
+ "hazeDetection"
+ "hazeDomination"
+ "hazeDominationMap"
+ "hd is NULL"
+ "heapBufferSizeAndAlignWithLength:options:"
+ "heapTextureSizeAndAlignWithDescriptor:"
+ "height NULL"
+ "height is 0"
+ "height must be a multiple of 2"
+ "height of textureArray[1] should match textureArray[0]"
+ "highQualitySensorReadoutRect falls outside height of sensorReadoutRect"
+ "highQualitySensorReadoutRect falls outside width of sensorReadoutRect"
+ "highlight is not a NSNumber"
+ "highlightCompressionCurve is NULL"
+ "highlightElement count is not 1"
+ "highlightElement is not a NSArray"
+ "highlightTuning readPlist failed"
+ "highlightTuningObj is NULL"
+ "histogramBuf is NULL"
+ "hoclXtalkBypassThd"
+ "host_statistics(HOST_VM_INFO) failed"
+ "hpbLUT NULL"
+ "hpbLUTTex is NULL"
+ "hpbLUTTexDesc is NULL"
+ "hpppCoeff not 1/3"
+ "hpppInBlendLUTTex is NULL"
+ "hr"
+ "hr.enabled mismatch"
+ "hrConfig is nil"
+ "hrInputTexs.dsLUTTex is NULL"
+ "hrd.enabled mismatch"
+ "i100@0:8r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}24r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}32{?=[3]}40B88@92"
+ "i128@0:8@16@24@32@40@48@56@64@72@80@88@96104^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffffB}120"
+ "i208@0:8@16@24{?=[3]}3280@96f104{?=[3]}108i156f160B164f168172@180@188f196f200B204"
+ "i212@0:8i16@20@28@36@44@52@60@68{CGRect={CGPoint=dd}{CGSize=dd}}76f108f112i116^{?=fffffffffBffffffffffffBffffff}120@128@136@144Q152[10{?={CGRect={CGPoint=dd}{CGSize=dd}}SSS}]160B168B172f176@180@188@196@204"
+ "i24@0:8@\"<CRGNodeRender>\"16"
+ "i24@0:8^{?=iffBBB{?=}}16"
+ "i24@0:8r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16"
+ "i32@0:8@1624"
+ "i32@0:8@16^{?=BB         [5[5 ]]B  {CMINoiseModel=iffff}}24"
+ "i32@0:8@16^{?=fffffffffffffffffffff[3f]ffffffffffffffIIfIffIffffffffffBBBBB}24"
+ "i32@0:8@16^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}}24"
+ "i32@0:8[65f]16r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}24"
+ "i32@0:8r^{?=f{RawDFSyntheticReferenceConsts=ff{RawDFRawNoiseModelParameters=ffffff}{RawDFRawNoiseModelParameters=ffffff}}}16@24"
+ "i348@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120{CGRect={CGPoint=dd}{CGSize=dd}}128f160f164i168Q172[10{?={CGRect={CGPoint=dd}{CGSize=dd}}SSS}]180B188B192f196{?=fffffffffBffffffffffffBffffff}200@316@324@332@340"
+ "i36@0:8^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}16@24B32"
+ "i40@0:8@16r^{?=[16{?=BC}]BCCiiSSiSS}24^{?={?=BC}{?=BC}ffCffffffIff}32"
+ "i40@0:8@16r^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}}24@32"
+ "i40@0:8@16r^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}}24^f32"
+ "i40@0:8^{?=f{RawDFSyntheticReferenceConsts=ff{RawDFRawNoiseModelParameters=ffffff}{RawDFRawNoiseModelParameters=ffffff}}}16@\"NRFFrameProperties\"24@\"NRFFrameProperties\"32"
+ "i40@0:8^{opaqueCMSampleBuffer=}16@24@32"
+ "i44@0:8@16^{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}24B32^{GOCConfig=BIB}36"
+ "i44@0:8^i16B24@28@36"
+ "i44@0:8r^{?={?=BC}{?=BC}ffCffffffIff}16@24B32@36"
+ "i48@0:8@16@24Q32r^{?=fffffffffB}40"
+ "i48@0:8@16@24^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}}32@40"
+ "i48@0:8Q16Q24^{RegDenseParameters=fff^{NoiseModel}ii@@B}32^{RegDenseMapProperties={RegDenseMapProperty=Q}{RegDenseMapProperty=Q}{RegDenseMapProperty=Q}}40"
+ "i48@0:8r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16^{__CVBuffer=}24@3240"
+ "i52@0:8@16f24@28^{__CVBuffer=}36@44"
+ "i56@0:8@16@24^@32@40^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}48"
+ "i56@0:8@16@24^{FlareDetectionConfig=SSffSfIBB}32^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}40@48"
+ "i56@0:8@16@24^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}}3240"
+ "i56@0:8@16@24^{HuemapConfig=ffffBBBBS}32@40^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}48"
+ "i56@0:8^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffffB}16@24@32I40I44B48B52"
+ "i60@0:8@16^{SyntheticThumbnailConfig=S{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}}24^{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}3240B56"
+ "i60@0:8^{?=@@@@@@@@@@}16@24^{HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}32^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}}40@48B56"
+ "i64@0:8@16@24@32@40@48^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffffB}56"
+ "i64@0:8@16@24@32^{HuemapMotionCompensationConfig=ffffBBBBSfSfffffS}40@48^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}56"
+ "i68@0:8@16@24@32@40^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}48@56B64"
+ "i68@0:8@16^{GOCConfig=BIB}24^{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}32B4044@60"
+ "i68@0:8@16^{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}24B3236@52^{GOCConfig=BIB}60"
+ "i68@0:8^@16^@24^@32^@40^48r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=S{?=ssSSSSSS}SSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}56B64"
+ "i72@0:8@16@2432r^{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}48^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}}56@64"
+ "i72@0:8@16@24@32@40@48^f56@64"
+ "i72@0:8@16^@24^{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}32B40@4452B68"
+ "i72@0:8@16^{?=@@}24^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}32^{HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}40^{HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}48@56B64B68"
+ "i72@0:8@16^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}24@32i40@44@52@60B68"
+ "i76@0:8@\"<MTLTexture>\"16@\"<MTLTexture>\"24i32@\"<MTLTexture>\"36@\"CMIImagePyramid\"44@\"CMIImagePyramid\"52r^{?=f{RawDFSyntheticReferenceConsts=ff{RawDFRawNoiseModelParameters=ffffff}{RawDFRawNoiseModelParameters=ffffff}}}60@\"SyntheticReferencePlist\"68"
+ "i76@0:8@16^@24^{LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}32@4048^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}64B72"
+ "i84@0:8@16@24@32^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}40B48B52B56@6068"
+ "i84@0:8^{__CVBuffer=}16@24@32@40@48Q56Q64B72@76"
+ "i92@0:8^{?=@@@}16@24@32B40B44B48@52^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}6068^{HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}84"
+ "i96@0:8r^{?=BB         [5[5 ]]B  {CMINoiseModel=iffff}}16@24@32B40B44{?=QQQ}48{?=QQQ}72"
+ "ibpErrCode_InternalError"
+ "ibpErrCode_MemoryAllocation"
+ "ibpErrCode_Parameter"
+ "ignoreLSC not found"
+ "imageHeight > 0"
+ "imageHeight must be greater than zero"
+ "imageWidth > 0"
+ "imageWidth must be greater than zero"
+ "inBlendLUTTex is NULL"
+ "inLinearChromaTex is NULL"
+ "inLinearLumaTex is NULL"
+ "inOutBuffer is NULL"
+ "inOutTexture is NULL"
+ "inSkyMaskTex is NULL"
+ "inTexUV is NULL"
+ "inTexY is NULL"
+ "incorrect array count for LP textures."
+ "incorrect array count for textures."
+ "incorrect basePolynomialData length"
+ "inf_pyr"
+ "inferenceDenoiseData is nil"
+ "inferenceDenoiseData.inputs is nil"
+ "inferenceDenoiseData.inputs.inputRGBTexture is nil"
+ "inferenceDenoiseData.inputs.noiseMapTexture is nil"
+ "inferenceDenoiseData.inputs.outputChromaTexture is nil"
+ "inferenceDenoiseData.inputs.outputLumaTexture is nil"
+ "inferenceDenoiseData.inputs.postNetworkTuningParams is nil"
+ "inferenceDenoiseData.inputs.semanticMasks is nil"
+ "inferenceDenoiseData.outputs is nil"
+ "inferenceFusionData is nil"
+ "inferenceFusionData.inputs.noiseMapTexture is nil"
+ "inferenceFusionData.inputs.nonReferenceFrameSampleBuffers count should be < NUM_FRAMES"
+ "inferenceFusionData.inputs.nonReferenceFrameSampleBuffers is nil"
+ "inferenceFusionData.inputs.nonReferenceFrameSampleBuffers[x] is nil"
+ "inferenceFusionData.inputs.pyramid is nil"
+ "inferenceFusionData.inputs.pyramid.bandTextures count should be 4"
+ "inferenceFusionData.inputs.pyramid.bandTextures[x] is nil"
+ "inferenceFusionData.inputs.referenceFrameSampleBuffer is NULL"
+ "inferenceFusionData.lscGainMapParameters is nil"
+ "inferenceFusionData.lscGainsTexture is nil"
+ "inferenceInputPixelBuffer is NULL"
+ "inferenceInputs = nil"
+ "inferenceResultsBindings"
+ "info->count is 0."
+ "info->index + info->count are out of range of the source NSData."
+ "info->type does not match correctionType."
+ "infoLag->index + infoLag->count are out of range of the source NSData."
+ "initFrameProperties failed."
+ "initWithContext:cameraInfo:config:"
+ "initWithGroup:"
+ "initWithMetal:vertName:fragName:pixelFormat:pixelFormat2:"
+ "initWithMetal:vertName:pixelFormatLuma:pixelFormatChroma:"
+ "initWithName:group:"
+ "initWithShaders:lscGainsTex:name:group:band:topBand:"
+ "initWithShaders:name:group:"
+ "initWithShaders:name:group:evmPyramid:ev0Pyramid:lscGainsTex:"
+ "innerMask is NULL"
+ "input RGBA texture is nil"
+ "input and output crop rectangles have differing sizes"
+ "input and output dimensions are incompatible"
+ "input frame cannot be both EVM and Long at the same time"
+ "input frame doesn't have registers"
+ "input frame is NULL"
+ "input frame metadata is nil"
+ "input frame registers missing"
+ "input gaussian pyramid is nil."
+ "input must be planar."
+ "input must have 2 planes."
+ "input options NULL"
+ "input pixelFormat should be RGBA16Float"
+ "input pyramid needs to be at least 2 levels deep"
+ "input sample buffer NULL"
+ "input texture for computing pyramids is nil."
+ "input texture from gaussian pyramid is nil."
+ "input tuning parameters should not be nil"
+ "inputChroma is NULL"
+ "inputChromaTex is nil"
+ "inputChromaTex texture is nil"
+ "inputCscParams is NULL"
+ "inputFrame couldn't be allocated"
+ "inputFrame is NULL"
+ "inputFrame is nil"
+ "inputFrame nil"
+ "inputFrame textures not bound"
+ "inputFrame.cfaLayout is invalid"
+ "inputFrame.metadata is nil"
+ "inputFrame.registers nil"
+ "inputImageTex is NULL"
+ "inputImg is NULL"
+ "inputLuma is NULL"
+ "inputLumaTex is nil"
+ "inputLumaTex texture is nil"
+ "inputLumaTex_band1 is NULL"
+ "inputLumaTex_band2 is NULL"
+ "inputLumaTex_band3 is NULL"
+ "inputNCHWR16FloatTextureDescriptorWithName:"
+ "inputName:roi:"
+ "inputNoiseMapTex is NULL"
+ "inputPixBuf nil"
+ "inputPyramid->textureUV is not valid"
+ "inputPyramid->textureY[band0 + 1] is not valid"
+ "inputPyramid->textureY[band1 + 1] is not valid"
+ "inputRGBTex is nil"
+ "inputRGBTex.pixelFormat == MTLPixelFormatRGBA16Float || inputRGBTex.pixelFormat == (MTLPixelFormat)MTLPixelFormatYCBCR8_420_2P_sRGB"
+ "inputStageName nil"
+ "inputTex is NULL"
+ "inputTex is nil"
+ "inputTex nil"
+ "inputTexture is nil"
+ "inputWithDescriptor:"
+ "inputYCbCr is NULL"
+ "inputs->bands[i]->textureYCbCrBand0 is NULL"
+ "interimDxy is NULL"
+ "intermBrightnessTex is NULL"
+ "intermGreenTex is NULL"
+ "intermMask is NULL"
+ "intermMask1 is NULL"
+ "intermMask2 is NULL"
+ "intermTex is NULL"
+ "intermediateChroma is NULL"
+ "intermediateDeltaBuffer is NULL"
+ "intermediateFusionWeights is NULL"
+ "intermediateLumaBuffer is NULL"
+ "internal textures are nil."
+ "interpClamp"
+ "interpExtrap"
+ "interpolateReadNoiseVar"
+ "invalid firstPix"
+ "invalid processingType - must be NRF_ProcessingType_RawNightMode"
+ "ioSurface is NULL"
+ "iosurface not valid"
+ "is"
+ "is not"
+ "isEnabled is NULL"
+ "isHighResLTMGrid:"
+ "isLTMOnFinalEnabled:"
+ "isSSCAccountedForInBytesRequiredForConfig:"
+ "ispDGain not found"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_PropertyNotFound"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "kFigCaptureStreamMetadata_DefectivePixelsCorrectionType not found."
+ "kFigCaptureStreamStillImageCaptureToneCurve_Rec709 not supported for legacy color space modes."
+ "kFigGNRSampleBufferProcessorError_RegistrationError"
+ "kRawNMReferenceFrameSelector_Error"
+ "kRawNightModeProcessorError_AllocationFailed"
+ "kRawNightModeProcessorError_BadConfig"
+ "kRawNightModeProcessorError_BindInputTexFail"
+ "kRawNightModeProcessorError_BindOutputTexFail"
+ "kRawNightModeProcessorError_FrameSampleBufferInvalid"
+ "kRawNightModeProcessorError_InferenceFail"
+ "kRawNightModeProcessorError_InferenceNetworkInvalid"
+ "kRawNightModeProcessorError_InputFrameBadCFALayout"
+ "kRawNightModeProcessorError_InputFrameBadFirstPix"
+ "kRawNightModeProcessorError_InputFrameConfigMismatch"
+ "kRawNightModeProcessorError_InputFrameNoPixBuf"
+ "kRawNightModeProcessorError_InputFrameNull"
+ "kRawNightModeProcessorError_InputTexturesAlreadyBound"
+ "kRawNightModeProcessorError_InvalidProcessingType"
+ "kRawNightModeProcessorError_InvalidTuningParameter"
+ "kRawNightModeProcessorError_LSCGainMapParametersMissing"
+ "kRawNightModeProcessorError_MaxThreadgroupSizeTooSmall"
+ "kRawNightModeProcessorError_MetadataError"
+ "kRawNightModeProcessorError_Metal"
+ "kRawNightModeProcessorError_NoCameraInfo"
+ "kRawNightModeProcessorError_NoPortType"
+ "kRawNightModeProcessorError_NoSensorCropRectInMetadata"
+ "kRawNightModeProcessorError_NoSensorReadoutRectInMetadata"
+ "kRawNightModeProcessorError_NoValidBufferRectInMetadata"
+ "kRawNightModeProcessorError_NoiseModelError"
+ "kRawNightModeProcessorError_OutputFrameConfigMismatch"
+ "kRawNightModeProcessorError_OutputFrameNoNoiseMap"
+ "kRawNightModeProcessorError_OutputFrameNoPixBuf"
+ "kRawNightModeProcessorError_OutputFrameNotSet"
+ "kRawNightModeProcessorError_OutputFrameNull"
+ "kRawNightModeProcessorError_OutputTexturesAlreadyBound"
+ "kRawNightModeProcessorError_ParamErr"
+ "kRawNightModeProcessorError_SensorDimensionsNotFound"
+ "kRawNightModeProcessorError_SharpnessScore"
+ "kRawNightModeProcessorError_TripodFusionBatchPrepFail"
+ "kRawNightModeProcessorError_TripodFusionFail"
+ "kRawNightModeProcessorError_TripodFusionParametersMissing"
+ "kRawNightModeProcessorError_TripodFusionTileOffsetNotZero"
+ "kRawNightModeProcessorError_TripodFusionTooManyFrames"
+ "kRawNightModeProcessorError_TripodFusionTooManyFramesInBatch"
+ "kRawNightModeProcessorError_TripodModeRefFrameSelectionWrong"
+ "kRawNightModeProcessorError_TuningParameterMissing"
+ "kSoftISPProcessorError_AWBGainsInvalid"
+ "kSoftISPProcessorError_AWBMetadataMissing"
+ "kSoftISPProcessorError_AWBNotConfigured"
+ "kSoftISPProcessorError_AWBProcessorCreationFailed"
+ "kSoftISPProcessorError_AWBProcessorSetupFailed"
+ "kSoftISPProcessorError_AddFrameCreateInputFrameObjFail"
+ "kSoftISPProcessorError_AddFrameNilProcessingOptions"
+ "kSoftISPProcessorError_AddFrameNilSampleBuf"
+ "kSoftISPProcessorError_AllocationFailed"
+ "kSoftISPProcessorError_ArgsNotFound"
+ "kSoftISPProcessorError_AuxiliaryPixelFormatMismatch"
+ "kSoftISPProcessorError_BLESTFocusPixelConfigInvalid"
+ "kSoftISPProcessorError_BadArgs"
+ "kSoftISPProcessorError_BadConfig"
+ "kSoftISPProcessorError_BadGraph"
+ "kSoftISPProcessorError_BindDraftDemosaicPixBufFail"
+ "kSoftISPProcessorError_BindFocusPixelPixBufFail"
+ "kSoftISPProcessorError_BindInputTexFail"
+ "kSoftISPProcessorError_BindOutputTexFail"
+ "kSoftISPProcessorError_BinnedBoundsNil"
+ "kSoftISPProcessorError_BinnedInputFrameNil"
+ "kSoftISPProcessorError_BoundsNull"
+ "kSoftISPProcessorError_CARConfigFromMetadataFail"
+ "kSoftISPProcessorError_CameraInfoByPortTypeNil"
+ "kSoftISPProcessorError_CameraInfoInvalid"
+ "kSoftISPProcessorError_ComputePipelineStateCreateFailed"
+ "kSoftISPProcessorError_ConfigFromMetadataAndRegistersNotMatch"
+ "kSoftISPProcessorError_ConfigNotFound"
+ "kSoftISPProcessorError_ConfigNotSet"
+ "kSoftISPProcessorError_ConnectionsNil"
+ "kSoftISPProcessorError_CouldNotDetermineFirstPixel"
+ "kSoftISPProcessorError_CreateArgsFailed"
+ "kSoftISPProcessorError_CreateBoundsFailed"
+ "kSoftISPProcessorError_DEMConfigFromRegistersFail"
+ "kSoftISPProcessorError_DelegateNotSet"
+ "kSoftISPProcessorError_DemosaicConfigTuningParamsFail"
+ "kSoftISPProcessorError_DetermineStageMemoryFailed"
+ "kSoftISPProcessorError_FaceDetectionFailed"
+ "kSoftISPProcessorError_FocusPixelTypeNotSupported"
+ "kSoftISPProcessorError_FrameHasIncompleteDependencies"
+ "kSoftISPProcessorError_FunctionConstantCountMismatch"
+ "kSoftISPProcessorError_FunctionConstantInvalidCombo"
+ "kSoftISPProcessorError_FunctionConstantInvalidKernel"
+ "kSoftISPProcessorError_FunctionConstantInvalidKey"
+ "kSoftISPProcessorError_FunctionConstantInvalidParamName"
+ "kSoftISPProcessorError_FunctionConstantUnexpectedError"
+ "kSoftISPProcessorError_FunctionConstantUnsupportedType"
+ "kSoftISPProcessorError_FunctionConstantValueMissing"
+ "kSoftISPProcessorError_GICIncorrectDataSize"
+ "kSoftISPProcessorError_GICWrongTableVersion"
+ "kSoftISPProcessorError_GOCConfigCompareRegistersMetadataFail"
+ "kSoftISPProcessorError_GOCConfigFromMetadataFail"
+ "kSoftISPProcessorError_GOCConfigFromRegistersFail"
+ "kSoftISPProcessorError_GetAuxPixBufFail"
+ "kSoftISPProcessorError_GetHRDGNUPipelineStateFail"
+ "kSoftISPProcessorError_GetOutputPixBufFail"
+ "kSoftISPProcessorError_GetPreHRComputePipelineStateFail"
+ "kSoftISPProcessorError_HRConfigCompareRegistersMetadataFail"
+ "kSoftISPProcessorError_HRConfigFromMetadataFail"
+ "kSoftISPProcessorError_HRConfigFromRegistersFail"
+ "kSoftISPProcessorError_HRDConfigCompareRegistersMetadataFail"
+ "kSoftISPProcessorError_HRDConfigFromRegistersFail"
+ "kSoftISPProcessorError_HRDFirFiltersNotSymmetrical"
+ "kSoftISPProcessorError_InitGetBundleFail"
+ "kSoftISPProcessorError_InputFrameNoCCM"
+ "kSoftISPProcessorError_InputFrameNoMetadata"
+ "kSoftISPProcessorError_InputFrameNoPixBuf"
+ "kSoftISPProcessorError_InputFrameNull"
+ "kSoftISPProcessorError_InputTexMissing"
+ "kSoftISPProcessorError_InputTexturesAlreadyBound"
+ "kSoftISPProcessorError_InputTexturesNotBound"
+ "kSoftISPProcessorError_InvalidAWBGains"
+ "kSoftISPProcessorError_InvalidAuxiliaryType"
+ "kSoftISPProcessorError_InvalidCommandBuffer"
+ "kSoftISPProcessorError_InvalidCommandEncoder"
+ "kSoftISPProcessorError_InvalidDraftDemosaicPixelBuffer"
+ "kSoftISPProcessorError_InvalidFocusPixelPixelBuffer"
+ "kSoftISPProcessorError_InvalidLUT"
+ "kSoftISPProcessorError_InvalidOutputDownscaleFactor"
+ "kSoftISPProcessorError_InvalidPixelFormat"
+ "kSoftISPProcessorError_InvalidPrepareDescriptor"
+ "kSoftISPProcessorError_InvalidProcesingOption"
+ "kSoftISPProcessorError_InvalidStageConfigurationMode"
+ "kSoftISPProcessorError_LSCBadHallDataLength"
+ "kSoftISPProcessorError_LSCCICSizeMismatch"
+ "kSoftISPProcessorError_LSCConfigCameraInfoByPortFail"
+ "kSoftISPProcessorError_LSCConfigFromRegistersFail"
+ "kSoftISPProcessorError_LSCConfigInvalidModulationWeight"
+ "kSoftISPProcessorError_LSCConfigNoGainsTable"
+ "kSoftISPProcessorError_LSCGainMapParametersMissing"
+ "kSoftISPProcessorError_LSCInvalidPixelSize"
+ "kSoftISPProcessorError_LSCMetadataMissing"
+ "kSoftISPProcessorError_LSCMissingHallData"
+ "kSoftISPProcessorError_LSCWrongTableVersion"
+ "kSoftISPProcessorError_LTMProcessorSetupFailed"
+ "kSoftISPProcessorError_MaxThreadsPerTGInsufficient"
+ "kSoftISPProcessorError_MetadataError"
+ "kSoftISPProcessorError_MetalCtxAllocFail"
+ "kSoftISPProcessorError_MetalQueueNil"
+ "kSoftISPProcessorError_ModuleConfigInvalid"
+ "kSoftISPProcessorError_ModuleConfigNull"
+ "kSoftISPProcessorError_NoErr"
+ "kSoftISPProcessorError_OPCConfigFromMetadataFail"
+ "kSoftISPProcessorError_OpenCalibrationFail"
+ "kSoftISPProcessorError_OpenFPNCorrectionFail"
+ "kSoftISPProcessorError_OutputAllocationFailed"
+ "kSoftISPProcessorError_OutputFrameMissingCommandBuffer"
+ "kSoftISPProcessorError_OutputFrameNull"
+ "kSoftISPProcessorError_OutputPixFmtMismatch"
+ "kSoftISPProcessorError_OutputTexMissing"
+ "kSoftISPProcessorError_OutputTexturesAlreadyBound"
+ "kSoftISPProcessorError_OutputTexturesNotBound"
+ "kSoftISPProcessorError_PDCConfigCompareRegistersMetadataFail"
+ "kSoftISPProcessorError_PDCConfigFromMetadataFail"
+ "kSoftISPProcessorError_PDCConfigFromRegistersFail"
+ "kSoftISPProcessorError_PDCCreateTextureFail"
+ "kSoftISPProcessorError_PDCFocusPixelConfigInvalid"
+ "kSoftISPProcessorError_PDCProcessingFailed"
+ "kSoftISPProcessorError_PDPConfigCompareRegistersMetadataFail"
+ "kSoftISPProcessorError_PDPConfigFromRegistersFail"
+ "kSoftISPProcessorError_PDPGainsFromMetadataFail"
+ "kSoftISPProcessorError_PDPGainsFromRegistersFail"
+ "kSoftISPProcessorError_ParamErr"
+ "kSoftISPProcessorError_PipelineNotSet"
+ "kSoftISPProcessorError_PipelinesCreateFail"
+ "kSoftISPProcessorError_PipelinesNotInitialised"
+ "kSoftISPProcessorError_PixelBufferAttachmentMissing"
+ "kSoftISPProcessorError_PostDemGetDotFixPipelineStateFail"
+ "kSoftISPProcessorError_PostDemosaicConfigFromMetadataFail"
+ "kSoftISPProcessorError_ProcessFrameBadConfig"
+ "kSoftISPProcessorError_PropertyNotFound"
+ "kSoftISPProcessorError_QDEMConfigInvalidAdaptiveDLUT"
+ "kSoftISPProcessorError_QDEMConfigInvalidAdaptiveHVLUT"
+ "kSoftISPProcessorError_QDEMConfigInvalidGaussianNRLUT"
+ "kSoftISPProcessorError_QDEMTuningParamsNotSet"
+ "kSoftISPProcessorError_RAWMBNRConfigTuningParamsFail"
+ "kSoftISPProcessorError_RAWMBNRProcessingFailed"
+ "kSoftISPProcessorError_RNFConfigFromMetadataFail"
+ "kSoftISPProcessorError_RNFConfigFromRegistersFail"
+ "kSoftISPProcessorError_RNFProcessingFailed"
+ "kSoftISPProcessorError_RawMBNRGetPipelineStateFail"
+ "kSoftISPProcessorError_RawThumbnailMetadataMissing"
+ "kSoftISPProcessorError_RawThumbnailValidBufferRectNil"
+ "kSoftISPProcessorError_RegWarpProcessingReferenceFailed"
+ "kSoftISPProcessorError_SIFRFrameIDMismatch"
+ "kSoftISPProcessorError_SIFRNotFoundForEV0"
+ "kSoftISPProcessorError_SensorDimensionsNotFound"
+ "kSoftISPProcessorError_SensorIDMismatch"
+ "kSoftISPProcessorError_SensorNotSupported"
+ "kSoftISPProcessorError_StageInputHasMultipleSources"
+ "kSoftISPProcessorError_StageNameNotUnique"
+ "kSoftISPProcessorError_StageNotFound"
+ "kSoftISPProcessorError_SynthThumbnailFocusPixelConfigInvalid"
+ "kSoftISPProcessorError_TexNull"
+ "kSoftISPProcessorError_ToneMappingConfigFail"
+ "kSoftISPProcessorError_TuningParamErr"
+ "kSoftISPProcessorError_UnknownErr"
+ "kSoftISPProcessorError_UnsupportedAuxiliaryPixelFormat"
+ "kSoftISPProcessorError_UnsupportedBitDepth"
+ "kSoftISPProcessorError_UnsupportedCompandingMode"
+ "kSoftISPProcessorError_UnsupportedCropValue"
+ "kSoftISPProcessorError_UnsupportedFirstPixel"
+ "kSoftISPProcessorError_UnsupportedInputPixelFormat"
+ "kSoftISPProcessorError_UnsupportedOperation"
+ "kSoftISPProcessorError_UnsupportedPipelineType"
+ "kSoftISPProcessorError_UnsupportedProtocol"
+ "kSoftISPProcessorError_UnsupportedQuadraFocusPixelGrid"
+ "kSoftISPProcessorError_UnsupportedSensorLayout"
+ "kSoftISPProcessorError_UnsupportedValueForFastHR"
+ "kSoftISPProcessorError_ValueNotAvailable"
+ "kSoftISPProcessorError_WBGOCConfigFromRegistersFail"
+ "kSoftISPProcessorError_YSHSetupFailed"
+ "kernel has function constants that require entries in paramCombinations"
+ "kernel not found in library"
+ "kernelName is nil"
+ "kernelRawDFFuseEv0s nil."
+ "key is nil"
+ "label = nil"
+ "largestOccupiedOffset"
+ "learnednoisereduction-quadra-%@"
+ "learnednoisereduction_bayer_v4"
+ "learnednoisereduction_quadra_v3"
+ "learnednrmetalstage_trace"
+ "left eye"
+ "legacyLog"
+ "lensShadingCorrectionGainMapParameters is NULL"
+ "lensShadingCorrectionGainMapParameters is nil"
+ "lensShadingModulationWeight >= 0.0f && lensShadingModulationWeight <= 1.0f"
+ "linearChromaTex is NULL"
+ "linearLumaTex is NULL"
+ "loadAWBMetadataforMIWB"
+ "loadFaceAndBodyRects"
+ "loadLCAModelCoefficientsFromMetadata"
+ "loadLCAModelCoefficientsHardcoded"
+ "localCurves nil"
+ "localDNRBiasPyrTextures allocation failed"
+ "localX too large."
+ "localizedDescription"
+ "localizedFailureReason"
+ "logGainMapTexHalf is NULL"
+ "lscConfig NULL"
+ "lscConfig is NULL"
+ "lscGainMapParameters is NULL"
+ "lscGainTexture is nil"
+ "lscGainsTex = nil"
+ "lscGainsTex is nil"
+ "lscGainsTexForAWB is NULL"
+ "lscGridData is NULL"
+ "lscGridHeight is NULL"
+ "lscGridWidth is NULL"
+ "lscMetadata is NULL"
+ "lscMetadata is nil"
+ "lscPixelBuffer is NULL"
+ "ltcFrame"
+ "ltcFrameIndex cannot be negative"
+ "ltcFrameIndex not valid"
+ "ltcGridOverlayOn"
+ "ltmLTC is NULL"
+ "ltmLut NULL"
+ "ltmParams.undoHRGainDownRatio"
+ "ltmStruct is NULL"
+ "luma texture pixel format not recognized"
+ "lumaDenoiseMixingCoeffStaticScene is missing"
+ "lumaDenoiseThresholdGainStaticScene is missing"
+ "lumaEntries NULL"
+ "lumaLowVarDetailsLevelStaticScene is missing"
+ "lumaLowVarSharpeningStrengthStaticScene is missing"
+ "lumaSharpenTuning readPlist failed"
+ "lumaSharpening addStage failed"
+ "lumaTex is NULL"
+ "lumaWithAddbackPyrTexArray[b] is NULL"
+ "lumaWithAddbackPyrTextures allocation failed"
+ "luma_out is NULL"
+ "lutTexture is nil"
+ "luxLevel >= 0.0f"
+ "mainCommandBuffer is NULL"
+ "mapStringToPixelType"
+ "mask height mismatch"
+ "mask is NULL"
+ "mask width mismatch"
+ "maskBinary is NULL"
+ "maskBinaryCropped is NULL"
+ "maskCropped is NULL"
+ "maskDilated is NULL"
+ "maskIn.width % 2 == 0 && maskIn.height % 2 == 0 is NULL"
+ "maskIntermediate is NULL"
+ "maskMB and/or maxVariationTex are nil"
+ "maskMB and/or maxVariationTex are nil."
+ "maskMBBinary is NULL"
+ "maskOutput1.width % 2 == 0 && maskOutput1.height % 2 == 0 is NULL"
+ "maskPreInpainting is NULL"
+ "maskSurround is NULL"
+ "maskSurroundNarrow is NULL"
+ "maxLSCGainRecip must be above 0"
+ "maxScaling"
+ "memoryAllocationInfo is NULL"
+ "metadata NULL"
+ "metadata is NULL"
+ "metadata is nil"
+ "metadata nil"
+ "metadata nil "
+ "metadataHasHDRLtmCurvesForBackground"
+ "metal context param is NULL"
+ "metal is NULL"
+ "metal is nil"
+ "metalContext is NULL"
+ "metalContext is nil"
+ "metalCtx is nil"
+ "midSize must be > 0"
+ "minDarken_I"
+ "minDarken_II"
+ "minDarken_III"
+ "minDarken_IV"
+ "minDarken_V"
+ "minDarken_VI"
+ "missing metadataEV0"
+ "missing metadataEVM"
+ "mixClipLUTTex is NULL"
+ "mode is set to tripod, but this method is for non-tripod processing"
+ "modulationFactorPerLuxLevel >= 0.0f"
+ "moduleConfig is NULL"
+ "moduleConfig is nil"
+ "motion detection failed"
+ "motionDetectClippingMap is NULL"
+ "motionDetectClippingMapDilated is NULL"
+ "motionDetectDownsampledEV0 is NULL"
+ "motionDetectDownsampledEVM is NULL"
+ "motionDetectGradientEV0 is NULL"
+ "motionDetectGradientEVM is NULL"
+ "motionDetectScoreMap is NULL"
+ "motionDetectWarpedEVM is NULL"
+ "motionDetection"
+ "motionDetectionParameters NULL"
+ "mouth"
+ "mtlCommandBuffer is NULL"
+ "mtlPixelFormat:"
+ "mutableConfigForStages is nil"
+ "name is NULL"
+ "neighborCount not supported, must be 4 or 8"
+ "neighborFocusPixelIndex out of range (neighborFocusPixelIndex >= totalCount)."
+ "networkModel"
+ "newOutputAuxiliaryPixelBufferForUniqueID:pixelFormat:width:height:alignment:"
+ "newTextureViewWithDescriptor:"
+ "nextShiftMap is NULL"
+ "nightmodedenoisemetalstage_trace"
+ "nightmodefusionmetalstage_trace"
+ "nightmodetripodfusionmetalstage_trace"
+ "no EV- homography"
+ "no EV0 homography"
+ "no frames have been registered!"
+ "noise"
+ "noise texture is nil"
+ "noiseMap is nil"
+ "noiseMapAccumulatorTexture is nil"
+ "noiseMapChroma is NULL"
+ "noiseMapLuma is NULL"
+ "noiseMapPyramid is NULL"
+ "noiseMapTex is NULL"
+ "noiseModel readPlist failed"
+ "noiseTuning readPlist failed"
+ "noisyLumaPyrTexArray[b] is NULL"
+ "noisyLumaPyrTextures allocation failed"
+ "noisyRgbTex is NULL"
+ "nonRefDerivTex is NULL"
+ "nonRefImg is NULL"
+ "nonRefTexlvl1 is NULL"
+ "normalizeLTMTable:ltmGridX:ltmGridY:ltmBinsNumber:"
+ "nrf.has_flicker"
+ "nrf.rawdf.draft_ltm"
+ "nrf.softltm.ltm_on_final"
+ "nrfConfig is NULL"
+ "nrfConfig->_allocatorType != FigMetalAllocatorTypeBuffer || nrfConfig->_compressionLevel < FigMetalAllocatorCompressionLossless is NULL"
+ "nrfFusionDenseRegister failed"
+ "nrfFusionOutput not set"
+ "nrfPlist nil"
+ "nrfPlist->fusion nil"
+ "numPyrLevels > 0 is NULL"
+ "numThreadGroups too large"
+ "offsetX value out of range"
+ "offsetY value out of range"
+ "old value texture is nil"
+ "opcTexture is NULL"
+ "opticalCenterOffset is NULL"
+ "optionsTuningParameters is NULL"
+ "order is NULL"
+ "origChromaTex is NULL"
+ "origLumaTex is NULL"
+ "origRawTex is NULL"
+ "originAlignment:"
+ "originalLscGridHeader->version == FigCaptureStreamLSCGainGridVersion_1"
+ "outLUT NULL"
+ "outLinearChromaTex is NULL"
+ "outLinearLumaTex is NULL"
+ "outPyramid is NULL"
+ "outPyramid->textureUV[lvl] is NULL"
+ "outPyramid->textureY[lvl] is NULL"
+ "outRegDenseMapProperties"
+ "outRegDenseMapProperties is NULL"
+ "outSize is NULL"
+ "outTex is NULL"
+ "outTex.width % 2 == 0 && outTex.height % 2 == 0 is NULL"
+ "outerMask is NULL"
+ "output (chroma) pixelFormat invalid"
+ "output (luma) pixelFormat invalid"
+ "output chroma pixelFormat invalid"
+ "output frame has not yet been set"
+ "output frame metadata is nil"
+ "output luma pixelFormat invalid"
+ "output luma texture (band 0) must be provided"
+ "output pixelFormat invalid"
+ "output pixelFormat should be RGBA16Float"
+ "output pyramid needs to be at least 2 levels deep"
+ "output.width % 2 == 0 && output.height % 2 == 0 is NULL"
+ "outputBuffer is NULL"
+ "outputCbCrTex"
+ "outputCbCrTex is NULL"
+ "outputChroma is NULL"
+ "outputChromaTex is NULL"
+ "outputChromaTex is nil"
+ "outputChromaTex texture is nil"
+ "outputFilteredDefectLocationCount should be > 0"
+ "outputFilteredDefectLocations is NULL"
+ "outputFrame is NULL"
+ "outputFrame is missing metadata"
+ "outputFrame is nil"
+ "outputFrame nil"
+ "outputFrame textures not bound"
+ "outputHLGLumaATex"
+ "outputHLGLumaATex is NULL"
+ "outputImage->lumaTex"
+ "outputImg is NULL"
+ "outputImg->lumaTex texture (band 0) must be provided"
+ "outputLuma is NULL"
+ "outputLumaTex is NULL"
+ "outputLumaTex is nil"
+ "outputLumaTex texture is nil"
+ "outputNCHWR16FloatTextureDescriptorWithName:"
+ "outputName:dimensions:pixelFormat:"
+ "outputName:dimensions:pixelFormat:constraints:"
+ "outputPyramid->textureUV is not valid"
+ "outputRGBATex is nil"
+ "outputSize"
+ "outputStageName nil"
+ "outputTex is NULL"
+ "outputTexUV is nil"
+ "outputTexUV texture is nil"
+ "outputTexY is nil"
+ "outputTexY texture is nil"
+ "outputTileTex is NULL"
+ "outputWithDescriptor:"
+ "outputYTex"
+ "outputYTex is NULL"
+ "output_tex is NULL"
+ "p is NULL"
+ "pMaxGain"
+ "pMaxGain is NULL"
+ "pShift NULL"
+ "paramValues missing a value"
+ "params GainMap dictionary is nil"
+ "params is NULL"
+ "params is nil"
+ "params missing function constant name"
+ "passCountTotal != count"
+ "patchBasedFusionParameters is NULL"
+ "pdcArgs is NULL"
+ "pdpConfig is NULL"
+ "pdpLUT allocation failure"
+ "pdpLUTData alloc failed"
+ "pdpLUTDataPtr NULL"
+ "perComponentCurve nil"
+ "performBlackSubtractionWithBlackWhiteParams failed"
+ "performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:enableUTM:"
+ "pipeline is NULL"
+ "pipelineState creation failed"
+ "pipelines have not been initialised"
+ "pipelines have not been initialised - cameraInfoByPort property needs to be set first."
+ "pixel buffer allocation failed"
+ "pixel buffer height should be 1/8th of inputTex"
+ "pixel buffer is nil"
+ "pixel buffer not valid"
+ "pixel buffer size is 0"
+ "pixel buffer width should be 1/8th of inputTex"
+ "pixel format mismatch between scratch and pyramid"
+ "pixelBuffer is NULL"
+ "pixelFormat of textureArray[1] should match textureArray[0]"
+ "pixelSizeInMicrons must not be 0"
+ "placeHoldertexDesc is NULL"
+ "planSolutionWithConstraints:graph:error:"
+ "populateLSCConfigWithGridData"
+ "populateLSCConfigWithInputFrame"
+ "populateLSCConfigWithRegisters"
+ "populateQuadraFPGrid failed"
+ "post inference plugin not valid"
+ "postDemosaicProcStage_chromaSuppression_RGB.maxTotalThreadsPerThreadgroup too small"
+ "postDemosaicProcStage_chromaSuppression_filterQCC.maxTotalThreadsPerThreadgroup too small"
+ "postDemosaicProcStage_directionalLowpass_RGB.maxTotalThreadsPerThreadgroup too small"
+ "postDemosaicProcStage_dotFix.maxTotalThreadsPerThreadgroup too small"
+ "pre inference plugin not valid"
+ "precision compensation out of range"
+ "prepare"
+ "prepareBand1InputWithBand0:"
+ "prepareDescriptor is NULL"
+ "prepareForFusion failed"
+ "prepareTuning:processingTypes:"
+ "prepareWithFrameProperties:srPlist:"
+ "prepareWithImageWidth:imageHeight:allocateTextures:"
+ "prevShiftMap is NULL"
+ "previous band fusion result texture is nil"
+ "previousFusedLumaTex is NULL"
+ "process called without addFrame"
+ "processInputFrames failed"
+ "processInputFrames failed on final pass"
+ "processLTMMetadata:toDarkestFrameMetadata:toEV0FrameMetadata:"
+ "processNonReference input frame is nil"
+ "processReference input frame is nil"
+ "processRegWarpRegDenseNonReference input frame is nil"
+ "processRegWarpRegDenseNonReference ref frame is nil"
+ "processingOptions is NULL"
+ "processingOptions is nil"
+ "propagatedChroma is NULL"
+ "propagatedGradient is NULL"
+ "propagatedLuma is NULL"
+ "propagatedLumaIntermediate is NULL"
+ "props is NULL"
+ "pyr->textureUV[lvl] is NULL"
+ "pyr->textureUV[out_chroma_level] is NULL"
+ "pyr->textureY[luma_level] is NULL"
+ "pyr->textureY[lvl] is NULL"
+ "pyr_height must be a multiple of 2"
+ "pyr_width  must be a multiple of 2"
+ "pyramid buffers not set"
+ "pyramid is NULL"
+ "pyramid luma and chroma textures should be of same type (u8/fp16) "
+ "pyramidLevel not valid"
+ "pyramidStage_NRF runGPU failed"
+ "pyramidStage_NRF runM2M failed"
+ "qdemConfig is nil"
+ "quadra_curve"
+ "r^{?=f{RawDFSyntheticReferenceConsts=ff{RawDFRawNoiseModelParameters=ffffff}{RawDFRawNoiseModelParameters=ffffff}}}"
+ "rawDFColorMatchStage"
+ "rawDFDownsampleStage"
+ "rawFullTex is NULL"
+ "rawMBNR process failed"
+ "rawScale addStage failed"
+ "rawTileTex is NULL"
+ "rcvLUTTex is NULL"
+ "readFocalLengthPixelSize"
+ "recipX value out of range"
+ "recipY value out of range"
+ "recovMethod != 1"
+ "redBlueFilterTextures.hrBypassTex is NULL"
+ "redBlueFilterTextures.outRBTex is NULL"
+ "redBlueTexture is NULL"
+ "refDerivTex is NULL"
+ "refImg is NULL"
+ "refTexlvl1 is NULL"
+ "reference frame LSC params = nil"
+ "reference frame is nil"
+ "reference frame metadata = nil"
+ "reference frame metadata is nil"
+ "reference frame object is nil"
+ "reference frame sampleBuffer is NULL"
+ "reference pixel buffer is NULL"
+ "referenceFrame is nil"
+ "referenceFrame.lensShadingCorrectionGainMapParameters is NULL"
+ "referenceFrame.lscGainsTex is NULL"
+ "regDPCCorrectionCoeff array count incorrect"
+ "regDPCCorrectionCoeff count incorrect"
+ "regDPCCorrectionCoeff not found"
+ "regDenseParams"
+ "regDenseParams is NULL"
+ "regFPCorrectionCoeff array count incorrect"
+ "regFPCorrectionCoeff count incorrect"
+ "regFPCorrectionCoeff not found"
+ "regGraMax not found"
+ "regHighlightMaxDef not found"
+ "regHighlightMaxSpe not found"
+ "regHighlightThdLUT count incorrect"
+ "regHighlightThdLUT not found"
+ "regPopThd not found"
+ "regWarp addStage failed"
+ "regWarpInput"
+ "regdense: Input must be different from output"
+ "regdense: Input size must match output size"
+ "registerImages:"
+ "registers missing"
+ "registrationPipelineRWPP"
+ "releaseFrames"
+ "render:"
+ "renderAll"
+ "renderEncoder is NULL"
+ "renderPassDesc is NULL"
+ "renderPipelineStateForVertexFunction:vertexDescriptor:fragmentFunction:constants:colorAttachmentDescriptorArrray:"
+ "resetState failed"
+ "resizeFocusPixelMap"
+ "result is NULL"
+ "retSize must not be 0"
+ "return pointer (enabled) is NULL"
+ "return pointer is NULL"
+ "rgbThumbnail"
+ "rgbThumbnailQuadra"
+ "rgbTileTex is NULL"
+ "right eye"
+ "rnfConfig is NULL"
+ "roi is NULL"
+ "rp is NULL"
+ "rpDesc is NULL"
+ "runDemosaicWithInputRawTex:outputImage:frame:"
+ "runDetectorsWithRequestedSyntheticReferenceMode:colorMatchingEnabled:withEv0:withEvm:"
+ "runHazeCorrectionWithConfig:inOutTexture:isQuadra:outputMetadata:"
+ "runMotionWithRefFrame:withOtherFrame:withPyramidBand:withTuningParams:"
+ "runPipeline"
+ "runProcessor:withTileCount:"
+ "runSemanticInferences"
+ "runToneMapping failed"
+ "runWithInput:secondInput:HDRLumaAInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:"
+ "sampleBuffer EV0 is NULL"
+ "sampleBuffer EVM is NULL"
+ "scHueRefChannel != 0"
+ "scaleParam is NULL"
+ "sceneTypeForRendering"
+ "scorePtr is NULL"
+ "scratch NULL."
+ "scratchLumaAsChroma is NULL"
+ "selectNRFFusionReferenceFrame failed"
+ "self = [super init]"
+ "self is NULL"
+ "self->boostedLumaMotionThreshold is NULL"
+ "self->boundsMapLimit is NULL"
+ "self->fusionBoostMatchedTexture is NULL"
+ "self->lowResMotionThreshold is NULL"
+ "self->nccHighLimitMatchedTexture is NULL"
+ "self->nccLowLimitMatchedTexture is NULL"
+ "self->pixelBuffer is NULL"
+ "self->sadThreshold is NULL"
+ "self->shadowLimit is NULL"
+ "self->textureUV[lvl] is NULL"
+ "self->textureY[lvl] is NULL"
+ "self->yCbCrTex is NULL"
+ "self.bandTextures is nil"
+ "self.nonReferenceInputFrames"
+ "self.pyramid is nil"
+ "semanticStylesPlist readPlist failed"
+ "sensorCropRect is missing"
+ "sensorDGain not in the metadata"
+ "sensorID is NULL"
+ "sensorReadoutRect falls outside height of sensorCropRect"
+ "sensorReadoutRect falls outside width of sensorCropRect"
+ "setApplicator:"
+ "setCustomFilter failed"
+ "setDispatchInfoBuffer:atIndex:"
+ "setDoRegistration:"
+ "setFlickerDetection:"
+ "setGainMapConfig:tuning:frameMetadata:width:height:isLinear:hasHDR:"
+ "setGrayGhostDetection:"
+ "setInputBufferRect:"
+ "setLinearSystemBuilder:"
+ "setLscModulationWeight:"
+ "setMetadataHasHDRLtmCurvesForBackground:"
+ "setMotionDetection:"
+ "setName:"
+ "setNetworkInputDescriptors:"
+ "setNetworkModel:"
+ "setNetworkOutputDescriptors:"
+ "setPixelsPerThread:"
+ "setRawDFColorMatchStage:"
+ "setRawDFDownsampleStage:"
+ "setRegWarpInput:"
+ "setRegistrationPipelineRWPP:"
+ "setSource:"
+ "setTextureArgs:encoder:atBufferIndex:"
+ "setTileCount:"
+ "setTileOverlap:"
+ "shaders is NULL"
+ "shaders required non existent."
+ "shaders[idx] is NULL"
+ "shadingFPNCorrectionImage is incorrect class"
+ "shadingFPNCorrectionImage is nil"
+ "shadingFPNCorrectionTex must be R8Unorm"
+ "shadingFPNCorrectionTex must be RG8Unorm"
+ "sharpeningPyramid is NULL"
+ "shiftMap is NULL"
+ "shiftMapWeight is NULL"
+ "shouldn't overwrite input"
+ "sigmaSqrd must exceed 0"
+ "sizeGranularity:"
+ "skinMaskPyrTextures allocation failed"
+ "skyMaskPyrTextures allocation failed"
+ "smallTex is NULL"
+ "snrMapPyrTexArray[b] is NULL"
+ "snrMapTextures allocation failed"
+ "softClipLUT NULL"
+ "softClipLUT deriv0Denominator == 0"
+ "softClipLUT is NULL"
+ "softClipLUTTex is NULL"
+ "softClipLUTTexDesc is NULL"
+ "softisp.mem_scale.bayerproc"
+ "softisp.mem_scale.rawmbnr"
+ "sortedIndex >= totalCount."
+ "sorted[i] out of range."
+ "sourceFrameIndex not valid"
+ "sourceFrameType must be UBReferenceFrame"
+ "sourcePropertyName is NULL"
+ "sourceStageName is NULL"
+ "sparseBlendingMap is NULL"
+ "sparseTextureTier"
+ "spatialCCMGridOverlayOn"
+ "specified destination stage doesn't exist"
+ "specified source stage doesn't exist"
+ "srcChromaTex is NULL"
+ "srcData is nil"
+ "srcLumaTex is NULL"
+ "stage is NULL"
+ "stage runWithArgs failed"
+ "stageConfigMode invalid"
+ "startSFDWithInputSampleBuffer:outputImage:tuning:"
+ "staticParameters is NULL"
+ "staticThreadgroupMemoryLength"
+ "stfParams.lastSTFCommandBuffer is NULL"
+ "stfTuningParameters is NULL"
+ "stringWithCString:encoding:"
+ "subProcessotType >= 0 is NULL"
+ "sumTexture"
+ "supportsInPlaceOperation = false, internalTempTex should be nil"
+ "supportsInPlaceOperation = false, textureArray should have 2 textures"
+ "supportsInPlaceOperation = true, textureArray should have 1 or 2 textures"
+ "symmetricBorder:"
+ "syntheticReferencePlist readPlist failed"
+ "table is nil"
+ "tableIndex >= defect count."
+ "tableIndex did not reach count."
+ "target_tex is NULL"
+ "task_info(TASK_BASIC_INFO) failed"
+ "task_info(TASK_THREAD_TIMES_INFO) failed"
+ "task_info(TASK_VM_INFO) failed"
+ "td is NULL"
+ "td2 is NULL"
+ "tdChroma is NULL"
+ "tdLuma is NULL"
+ "tdNoCompress is NULL"
+ "tdOut is NULL"
+ "tdSub is NULL"
+ "tdmp is NULL"
+ "tempAccWeightChromaTex is NULL"
+ "tempAccWeightLumaTex is NULL"
+ "tempTex is nil"
+ "tex is NULL"
+ "texDesc is NULL"
+ "texture heights do not match."
+ "texture is NULL"
+ "texture not valid"
+ "texture widths do not match."
+ "textureArgsWithStructName:"
+ "textureArray is nil"
+ "textureI is NULL"
+ "textures must not have a dimensions > 0"
+ "the reference frame should never be processed as a non-ref frame"
+ "theFinalFlexRangeShader is NULL"
+ "theShader is NULL"
+ "thread too large."
+ "thumbnailDict is nil"
+ "tileDeltaTex is NULL"
+ "tileLumaTex is NULL"
+ "tileOverlap"
+ "tileOverlapParameters"
+ "tileTex is NULL"
+ "tmpChromaTex is NULL"
+ "tmpLTMStruct is NULL"
+ "tmpLumaTex is NULL"
+ "tmpOutputImg is NULL"
+ "tmpOutputImg->chromaTex is NULL"
+ "tmpOutputImg->lumaTex is NULL"
+ "tmpTex is NULL"
+ "toneMapping parameters not set"
+ "toneMapping readPlist failed"
+ "toneMappingConstant[toneMappingGuideEnabled] is NULL"
+ "totalCombinations is not the same as result count from _addCombos"
+ "transformAndAddPortion"
+ "true"
+ "tuningControls is NULL"
+ "tuningParameters is NULL"
+ "tuningParameters is nil"
+ "tuningParams = nil"
+ "tuningParams is nil"
+ "unable to create GainMapPlist object"
+ "unable to create config"
+ "undoHRGainDownRatio"
+ "unrecognized hybrid registration mode"
+ "unresolvedDestinationPropertiesForStage is NULL"
+ "unsupported first pixel"
+ "updateParametersFromMetadata:outputGain:bayerPattern:lscGainMapBuffer:lscGainMapParameters:"
+ "v1"
+ "v24@0:8^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}16"
+ "v24@0:8r^{?={LSCConfig=BSSfIBff(?={?=SSSS})(?=[4]{?=})[4]}@@}16"
+ "v320@0:8{LearnedNRUniforms={ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}fffffffffffffBBB}16"
+ "v36@0:8^S16S24S28S32"
+ "v52@0:8[65f]16r^S24S32S36r^S40f48"
+ "validBufferRect falls outside height of input pixel buffer"
+ "validBufferRect falls outside height of sensorCropRect"
+ "validBufferRect falls outside width of input pixel buffer"
+ "validBufferRect falls outside width of sensorCropRect"
+ "verifyConfig"
+ "verifyQuadraFPGrid"
+ "waitUntilScheduled"
+ "warpedImage->chromaTex is NULL"
+ "warpedImage->lumaTex is NULL"
+ "warpedImg is NULL"
+ "warpedImg->chromaTex is NULL"
+ "was"
+ "wasn't"
+ "weightlum_curve"
+ "width  must be a multiple of 2"
+ "width NULL"
+ "width is 0"
+ "width of textureArray[1] should match textureArray[0]"
+ "widths do not match"
+ "winSize must be odd valued"
+ "winSize must exceed 0"
+ "with"
+ "writeAlignment:"
+ "wrong image dimensions"
+ "xtalkCoeffMax"
+ "xtalkLutTex nil"
+ "xtalkTable.length > 0 && xtalkTable.length == gicDataHeadSize + gridHeightFull * gridWidthFull * gridDepth * sizeof( Float32 )"
+ "xtoCCT.count <= MAX_X2CCTLUT_ENTRIES is NULL"
+ "xtoCCT[i][@\"CCT\"] is NULL"
+ "xtoCCT[i][@\"X\"] is NULL"
+ "xtoCCT[i][@\"Y\"] is NULL"
+ "y > 0 && z > 0"
+ "y denominator is 0"
+ "{?=\"dlux_x1\"f\"dlux_y1\"f\"dlux_x2\"f\"dlux_y2\"f\"dsoft_x1\"f\"dsoft_y1\"f\"dsoft_x2\"f\"dsoft_y2\"f\"dlow_x1\"f\"dlow_y1\"f\"dlow_x2\"f\"dlow_y2\"f\"diso_x1\"f\"diso_y1\"f\"diso_x2\"f\"diso_y2\"f\"dhist_low\"f\"dhist_mid\"f\"dhist_hi\"f\"dhist_max_gnorm\"f\"hdr_ref\"f\"hdr_mix\"[3f]\"clipped_pixels_thresh\"f\"clipping_compression_start\"f\"clipping_compression_end\"f\"dclip_x1\"f\"dclip_y1\"f\"dclip_x2\"f\"dclip_y2\"f\"clip_power\"f\"base_EDR\"f\"hdr_mix_max_y1\"f\"hdr_mix_max_y2\"f\"hdr_mix_max_x1\"f\"hdr_mix_max_x2\"f\"shadow_val\"f\"HL_ind\"I\"HL_starting_point\"I\"thr_HL\"f\"ht_top_thr1\"I\"dw_change_max_for_mids_top\"f\"dw_change_max_for_mids_th1\"f\"ht_top_thr2\"I\"dw_change_max_for_mids_th2\"f\"eps_for_log\"f\"x1_dw_change_for_mids\"f\"x2_dw_change_for_mids\"f\"exposureBiasFactor\"f\"fullContrastBoost\"f\"ht_use_contrast\"f\"gammaBoost\"f\"ht_use_gamma\"f\"ltm_change_Hls_thresh\"f\"use_luxlevel_metadata\"B\"use_flex_fullrange\"B\"skip_hard_gain_lumaHD\"B\"use_ispDGain_softlog\"B\"use_hard_gain_averageLTM\"B}"
+ "{?=\"lscConfig\"{LSCConfig=\"enabled\"B\"cropOrigin\"\"sensorDimension\"\"gridWidth\"S\"gridHeight\"S\"gridMaxGainReciprocal\"f\"gridIntervalReciprocal\"\"firstPix\"I\"isQuadra\"B\"flashMixingWeight\"f\"modulationWeight\"f\"yOffset\"(?=\"vec\"\"\"{?=\"gr\"S\"r\"S\"b\"S\"gb\"S})\"yOffsetQuadra\"(?=\"vec\"[4]\"\"{?=\"gr\"\"r\"\"b\"\"gb\"})\"quadraPixelOriginByChannel\"[4]}\"lscCenterCropOffset\"\"lscGainsTex\"@\"<MTLTexture>\"\"flashLSCGainsTex\"@\"<MTLTexture>\"}"
+ "{?=\"outputOffset\"\"dotFixOn\"B\"localSharpClip\"B\"dotDetectThreshold\" \"strength\" \"phiSlope\" \"phiKnee\" \"sharpScaling\" \"overshootMitigation\" \"modulationLow\" \"modulationHigh\" \"modulationSlope\" \"sharpeningKernel\"[5[5 ]]\"useSobelDetailModulation\"B\"whiteBalanceGainY\" \"hrGainDownRatio\" \"noiseModel\"{CMINoiseModel=\"invalid\"i\"shotNoiseVariance\"f\"readNoiseVariance\"f\"darkCurrentNoiseVariance\"f\"quantizationNoiseVariance\"f}}"
+ "{?=QQQ}24@0:816"
+ "{LearnedNRUniforms=\"whiteBalanceGains\"\"cscParams\"{ColorSpaceConversionParameters=\"cscMatrixFwd\"{?=\"columns\"[3]}\"cscMatrix\"{?=\"columns\"[3]}\"colorCorrectionMatrix\"{?=\"columns\"[3]}\"transferFunctionFwd\"{TransferFunctionParameters=\"linearScale\"f\"linearThreshold\"f\"nonLinearScale\"f\"nonLinearBias\"f\"nonLinearPower\"f}\"transferFunctionInv\"{TransferFunctionParameters=\"linearScale\"f\"linearThreshold\"f\"nonLinearScale\"f\"nonLinearBias\"f\"nonLinearPower\"f}\"finalScaleFwd\"f\"finalScale\"f\"chromaBias\"f\"outputToLinearYCbCr\"B\"clampNegativesToZero\"B\"applyColorCorrection\"B\"useGpuCSC\"B}\"lscScale\"\"lscOffset\"\"lscNormalization\"f\"lscModulationWeight\"f\"photonScaledReadNoiseStd\"f\"sensorScaledShotNoiseVar\"f\"modulatedPhotonScaledReadNoiseStd\"f\"modulatedSensorScaledShotNoiseVar\"f\"lumaAddBackWeight\"f\"lumaAddBackBand0Weight\"f\"lumaAddBackClipToSNR\"f\"lumaAddBackLSCModulation\"f\"preNetworkScale\"f\"postNetworkScale\"f\"outputGain\"f\"isQuadra\"B\"isVersion2\"B\"rotateTile180\"B}"
+ "{LearnedNRUniforms={ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}fffffffffffffBBB}16@0:8"
+ "{MiwbConfig=\"thumbnailSize\"\"hazeInputMatCCM\"{?=\"columns\"[3]}\"hazeOutputInvMatCCM\"{?=\"columns\"[3]}\"miwbInputInvMatCCM\"{?=\"columns\"[3]}\"miwbOutputMatCCM\"{?=\"columns\"[3]}\"matSkyCcm\"{?=\"columns\"[3]}\"matSkinCcm\"{?=\"columns\"[3]}\"globalWhitePoint\"\"skyWhitePoint\"\"skinWhitePoint\"\"coolStrength\"f\"warmStrength\"f\"whiteL\"f\"satMapFactor\"f\"blueSky\"f\"dayLightWeight\"f\"indoorWeight\"f\"useIndoorMiwbV2\"B}"
+ "{RawDFDeepShadowRecoveryBandConsts=\"ev0DeepShadowSmoothStepStart\"f\"ev0DeepShadowSmoothStepEnd\"f\"clrMatchThresholdStart\"f\"clrMatchThresholdEnd\"f\"edgeMatchThresholdStart\"f\"edgeMatchThresholdEnd\"f\"shadowSigmaCorrectionNode0\"f\"shadowSigmaCorrectionNode1\"f\"edgeThresholdStart\"f\"edgeThresholdEnd\"f\"edgeGhostBoostStrength\"f}"
+ "{RawDFHighlightRecoveryBandConsts=\"sifrHighSnrSmoothStepStart\"f\"sifrHighSnrSmoothStepEnd\"f\"ev0BrightnessSmoothStepStart\"f\"ev0BrightnessSmoothStepEnd\"f\"ev0SifrMatchThreshold\"f}"
+ "\x84"
+ "\xf0\xf0A"
+ "\xf0\xf0\xf0T"
+ "\xf0\xf0\xf0\xe1"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc1"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0A"
- "! isVersatilePixelFormat( pixFmt ) || bayerPattern"
- "%@G"
- "%s/%s"
- "( ( ( ltmBinsX == ( 8 ) ) && ( ltmBinsY == ( 6 ) ) ) || ( ( ltmBinsX == ( 16 ) ) && ( ltmBinsY == ( 12 ) ) ) ) && ( ltmBinsC == ( 65 ) )"
- "( ( _ltmBinsX == ( 8 ) ) && ( _ltmBinsY == ( 6 ) ) ) || ( ( _ltmBinsX == ( 16 ) ) && ( _ltmBinsY == ( 12 ) ) )"
- "( ( ltmBinsX == ( 8 ) ) && ( ltmBinsY == ( 6 ) ) ) || ( ( ltmBinsX == ( 16 ) ) && ( ltmBinsY == ( 12 ) ) )"
- "( ( ltmBinsX_BG == ( 8 ) ) && ( ltmBinsY_BG == ( 6 ) ) ) || ( ( ltmBinsX_BG == ( 16 ) ) && ( ltmBinsY_BG == ( 12 ) ) )"
- "( ( ltmLutNBinsX == ( 8 ) ) && ( ltmLutNBinsY == ( 6 ) ) ) || ( ( ltmLutNBinsX == ( 16 ) ) && ( ltmLutNBinsY == ( 12 ) ) )"
- "( inputFrameGDCParams && outputFrameGDCParams ) || ( ! inputFrameGDCParams && ! outputFrameGDCParams )"
- "( ltmBinsC == ( 33 ) ) || ( ltmBinsC == ( 65 ) )"
- "( ltmBinsC_BG == ( 33 ) ) || ( ltmBinsC_BG == ( 65 ) )"
- "( ltmBinsX == ( 8 ) ) && ( ltmBinsY == ( 6 ) ) && ( ltmBinsC == ( 65 ) )"
- "( pixelSizeInBits % 8 ) == 0"
- "( width < inputRGBTex.width ) && ( height < inputRGBTex.height )"
- "(?={?=II})32@0:8i16I20I24I28"
- "(?={?=II})36@0:8i16i20I24I28I32"
- "+[RawDFDetectors runDetectorsToOutput:withRequestedSyntheticReferenceMode:withEv0:withEvm:withSRTuning:withDownSampleStage:withColorMatchStage:withMotionDetection:withgrayGhostDetection:withFlickerDetection:]"
- "+[RawDFDetectors runMotionToOutput:withRefFrame:withOtherFrame:withPyramidBand:withTuningParams:withMotionDetection:]"
- "+[RawDFNetworkCommon allocateBuffersForNetwork:bindMode:bindBuffers:descriptions:textures:pixelBuffers:numBuffers:pixelFormat:metalContext:]"
- "+[RawDFNetworkCommon loadEspressoNetworkFromPath:andStoreNetwork:andPlan:espressoContext:]"
- "+[RawDFPowerBlurStage prewarmShaders:]"
- "-[ACNetworkPostANEStage initWithMetal:]"
- "-[CMIDraftDemosaicStage _compileShaders]"
- "-[CMIImagePyramidShaders initWithMetal:]"
- "-[DeepFusionProcessor _preprocessSyntheticReferenceFrame]"
- "-[DeepFusionProcessorShaders initWithMetal:]"
- "-[DenoiseFusePipeline startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:]"
- "-[GainMapStage computeGainMapWithInput:secondInput:output:properties:mpconfig:]"
- "-[GainMapStage runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:]"
- "-[H13FastPowerBlurConfig getPowerBlurConfigForInputFrame:PowerBlurConfig:enablePowerBlur:]"
- "-[H13FastPowerBlurShaders initWithMetalContext:]"
- "-[H13FastPowerBlurStageMetal _applyPowerBlurWithParams:halfResATex:halfResBTex:commandBuffer:]"
- "-[H13FastPowerBlurStageMetal _remosaicRgbWithParams:inputTex:lscGainsTex:outputTex:commandBuffer:]"
- "-[H13FastPowerBlurStageMetal _remosaicYuvWithParams:inputLumaTex:inputChromaTex:lscGainsTex:outputTex:commandBuffer:]"
- "-[H13FastPowerBlurStageMetal _resampleHalfSizeToFullSizeRgbWithParams:inputTex:halfResTex:outputTex:commandBuffer:]"
- "-[H13FastPowerBlurStageMetal _resampleHalfSizeToFullSizeYuvWithParams:inputLumaTex:inputChromaTex:halfResTex:outputLumaTex:outputChromaTex:commandBuffer:]"
- "-[H13FastPowerBlurStageMetal _resampleRawAndCreateHighFrequencyMapWithParams:rawTex:halfResTex:commandBuffer:]"
- "-[H13FastPowerBlurStageMetal _validateThreadsPerThreadgroup:forPipeline:]"
- "-[H13FastPowerBlurStageMetal runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:]"
- "-[H13FastPowerBlurStageMetal runWithConfig:inputTex:outputTex:lscGainsTex:]"
- "-[LearnedNRNetworkPostANEStage initWithMetal:]"
- "-[LearnedNRNetworkPreANEStage initWithMetal:]"
- "-[LearnedNRNetworkShaders initWithMetal:]"
- "-[LearnedNRNetworkStage initWithContext:cameraInfo:isQuadra:deviceGeneration:]"
- "-[LearnedNRNetworkStage updateParametersFromMetadata:bayerPattern:lscGainMapBuffer:lscGainMapParameters:]"
- "-[NRFBackgroundLearnedNR initWithContext:cameraInfo:isQuadra:deviceGeneration:]"
- "-[RawDFColorMatchShaders initWithMetal:]"
- "-[RawDFDownsampleShaders initWithMetal:]"
- "-[RawDFFlickerDetectorShaders initWithMetal:]"
- "-[RawDFFrames addFrame:]"
- "-[RawDFFrames initWithMetalContext:]"
- "-[RawDFFrames setReferenceFrameIndex:]"
- "-[RawDFInputFrame _checkRgbTexConfig:]"
- "-[RawDFInputFrame allocateRGB]"
- "-[RawDFInputFrame commonInitWithMetalContext:cameraInfo:inputFrame:metadata:uniqueFrameId:]"
- "-[RawDFInputFrame commonInitWithMetalContext:cameraInfo:inputPixelBuffer:metadata:uniqueFrameId:]"
- "-[RawDFInputFrame commonInitWithMetalContext:cameraInfo:inputSamplebuffer:uniqueFrameId:]"
- "-[RawDFInputFrame demosaicWithStage:]"
- "-[RawDFInputFrame getGDCParametersWithCameraInfoByPortType:withMetadata:]"
- "-[RawDFInputFrame initFrameProperties]"
- "-[RawDFInputFrame prepareInputFrame]"
- "-[RawDFNetworkStage getFilePathForNetworkIdentifier:withExtension:]"
- "-[RawDFPowerBlurStage initWithMetalContext:]"
- "-[RawDFPowerBlurStage runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:]"
- "-[RawDFPowerBlurTuningParams readPlist:]"
- "-[RawDFProcessor _processInputFrame:]"
- "-[RawDFProcessor _registerImages:]"
- "-[RawDFProcessor _verifyConsistentMetadataWithFrame:]"
- "-[RawDFProcessor setRegwarpInputSurface:]"
- "-[RawDFProcessor(Tuning) prepareTuning:]"
- "-[RawDFProxyShaders initWithMetal:]"
- "-[RawDFSyntheticReferenceStage packSyntheticReference:toOutputTex:]"
- "-[RawDFSyntheticReferenceUnpackShaders initWithMetal:]"
- "-[RawNightModeProcessor runDemWarpOnFrame:outputTexture:label:]"
- "-[SoftLTM initWithCommandQueue:]"
- "-[SoftLTM processLTMMetadata:toDarkestFrame:toEV0Frame:]"
- "-[UBProcessorV4 setRegwarpInputSurface:]"
- "-[UBProcessorV4 verifyIOSurfaceCompression:]"
- ".bundle"
- ".net"
- "/"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/RegWarpHelper/RegWarpHelper.m %s: Failed to create downsampleRGBToLuma"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/ColorConvert/ColorConvertV4.m Fig"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/Demosaic/CZDemosaicStageV4.m Fig"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/DraftDemosaic/CMIDraftDemosaicStageV4.m %s: Failed to create _draftDemosaicMultiChannelBayerPipeline"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/DraftDemosaic/CMIDraftDemosaicStageV4.m %s: Failed to create _draftDemosaicSingleChannelBayerPipeline"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/CMIImagingStages/DraftDemosaic/CMIDraftDemosaicStageV4.m %s: Output crop doesn't fit in the output texture"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Cannot prewarm LearnedNRNetworkPostANEStage"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Cannot prewarm LearnedNRNetworkPreANEStage"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Cannot prewarm LearnedNRNetworkShaders"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Configuration expects a quadra frame but quadraBinningFactor is missing or inconsistent"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Couldn't determine CameraInfo from metadata"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Device identifier could not be found."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to create _postStage."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to create _preStage."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to create _shaders."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to create _shared."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to create config."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to create proc."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to create reg exp for finding Espresso models for %@/%@ (error:%@).  All model loading will fail!"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to create stage."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to get LearnedNR network path."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to initialize LearnedNRNetworkShaders"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to initialize LearnedNRNetworkStage."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to load LSCGains texture"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Failed to load LSCGainsPlist"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: GlobalHighlightCompression count is incorrect"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: LSC buffer has unexpected pixel format"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: LearnedNR completion errors reported."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: LearnedNR runs not reported complete."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: LearnedNRNetworkStage tuningParams must be set."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Platform identifier could not be found."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Quadra bayer pattern must be BBGG or RRGG"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Read and shot noise must be positive"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: SensorDimensions nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: SensorDimensions.height nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: SensorDimensions.width nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to create pipeline state for LearnedNR::convertYUV420toRGB"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to create pipeline state for createTileForQuadra"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to create pipeline state for createTileForRawInput"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to create pipeline state for lumaAddbackForRawInput"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to create pipeline state for processDenoisedRgbForRawInput"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to create texture %s."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to read lumaAddBackBand0Tuning"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to read lumaAddBackClipToSNRTuning"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to read lumaAddBackTuning"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to read readNoiseModulationTuning"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unable to read shotNoiseModulationTuning"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: Unsupported bayer pattern"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: GlobalLTMLookUpTable has unexpected size"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: count0 (%f) >= count1 (%f)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: countM (%f) < count0 (%f)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: countM (%f) > count1 (%f)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: failed to estimate median luma. medianCount=%u, globalHist[0]=%u, globalHist[1]=%u"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: globalLTM is NULL"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: globalLTM->lutEntry count has unexpected value"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: header.version = %d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: localHistogramBinSize = %u"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: localHistograms is NULL"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: ltmLuma out of bounds (%f)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: medianLuma out of bounds (%f)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: missing AverageLTM"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: missing GlobalLTMLookUpTable"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: missing LocalHistograms"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: tileGrid.tileCountX = %u"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: unexpected AverageLTM.count"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _estimateGainFromMetadata: unexpected size = %u"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _postStage nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _preStage nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _shared nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: _tiledInferenceProcessor nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: bayerPattern nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: cameraInfoByPortType nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: commandBuffer nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: computeEncoder nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: encoder nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: failed to find leanednoisereduction network."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: inputRaw nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: invalid inputRaw dimensions."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: invalid inputRaw pixelFormat."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: invalid outChroma dimensions."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: invalid outChroma pixelFormat."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: invalid outLuma dimensions."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: invalid outLuma pixelFormat."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: metadata nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: metal nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: outChroma nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: outLuma nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: self.shared.frameProperties nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %s: td nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: CAC is being applied: ( %{public}f )"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRStageV4.m %s: CAC is enabled, however, it's not being applied: ( %{public}f )"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %s: Unable to initialize MIWB Stage"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingBuffersV4.m Fig"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m %s: Tone mapping Quality: %d enableMSTM %d enableSRL %d enableSTF %d LTMOutputMode_FinalLuma %d chromaGainAdjustmentPower %f inputIsLinear %d chromaBias %f gridScaleFactor {%f,%f} enableUTM %d utmForegroundFactor %f utmBackgroundFactor %f facesCount %d faceLandmarksCount %d spatialCCMTexValid %d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingStageV4.m Fig"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFApplyNetworkWeightsV4.m %s: Failed to initialize RawDFApplyNetworkWeightsShaders"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFApplyNetworkWeightsV4.m %s: Unable to create pipeline state for addPreviousPyramidLevel"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFApplyNetworkWeightsV4.m %s: Unable to create pipeline state for applyNetworkDeghosting"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFApplyNetworkWeightsV4.m %s: Unable to create pipeline state for filterDenoise"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFApplyNetworkWeightsV4.m %s: Unable to create pipeline state for filterDenoiseLumaOnly"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFApplyNetworkWeightsV4.m %s: Unable to create pipeline state for untileAndConvert444To420"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: Failed to add network to espresso plan with error: %s"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: Failed to bind fusion network input buffer %s"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: Failed to build espresso plan"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: Failed to create espresso plan"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: Fusion input MTLTexture NULL."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: Unable to create fusion network input PixelBuffer with error: %i"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: invalid fusion espresso input height"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: invalid fusion espresso input width"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: pixelBuffers[%d] is already allocated"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkCommonV4.m %s: pixelBuffers[%d] is nil."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkPreprocessV4.m %s: Failed to initialize RawDFNetworkPreprocessShaders"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkPreprocessV4.m %s: Unable to create pipeline state for estimateNoiseAndTileSyntheticLong"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkPreprocessV4.m %s: Unable to create pipeline state for estimateNoiseAndTileSyntheticReference"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: Device identifier could not be found."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: Failed to get platform identifier."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: Unable to create pipeline state for acn postprocessing shader"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: Unable to create pipeline state for acn preprocessing shader"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Deferred/Network/RawDFNetworkStageV4.m %s: failed to find < %s > network."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Binding _auxDraftDemosaicLumaTexture has failed for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Binding _auxDraftDemosaicRGBTexture has failed for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Cannot bind _baseTex for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Cannot get metal format for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Failed allocate for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Failed to alloc CMIImagePyramid for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: GDC params already allocated."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Unable to allocate GDC params for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Unable to allocate NRFFrameProperties for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Unable to get GDC params for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: Unable to initialize NRFFrameProperties for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: _metadata is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: _properties cannot be nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: _properties.meta cannot be nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: _rgbTex is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: demosaicStage is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: frame needs standard metadata to get GDC params."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: inputFrame.texture cannot be nil for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: loadFrameMetadata failed for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: metadata nil, required to get GDC params."
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: metal is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: nil inputSampleBuffer for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: pixelBuffer is nil for frame: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: pixelBufferFormat cannot be 0 : %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: rgbTex height does not match base height"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: rgbTex nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: rgbTex unexpected format"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: rgbTex width does not match base width"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: td is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFInputFrameV4.m %s: uniqueFrameId cannot be negative: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: %{private}@ registerImages < %{private}s(%{public}d) >"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Cannot bind regWarpInputTex"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to Create regWarpInput for RawDF"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to init CMIDraftDemosaicStage"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Failed to init RawDFPowerBlurStage "
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Invalid currentInputFrame "
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Metadata mismatch detected between frames 0 and %d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Mismatch: (frame0Props->meta.sensorID == currFrameProps->meta.sensorID)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Prep stages for (T: %d ): (PB: %d), (LS: %d), (ZM: %d), (MR: %d), (PSTPLC: %d), (ZM: %.1f), (PSS: %d)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: RawDFFrames didn't store uniqueFrameId: %{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Soft Failure: failed to register non-ref bracket frame: %d (batch=%d, isEVM=%d)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Unable to update reference frame ROI"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _deepFusionOutput not set"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _deepFusionOutput.syntheticReferencePixelBuffer nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _frames is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: computeLTM fail"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: metal is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: no frames have been registered!"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: noiseDivisorOutputTex bind failed"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: referenceFrameIndex cannot be set to a negative value"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: registration failed at setReferenceFrameIndex"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: softLTMStage computeLTM finds source image as nil "
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: syntheticReferenceOutputTex nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %s: entryParams PowerBlur is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %s: powerBlurTuning readPlist failed"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: Failed to Create regWarpInput for UBProcessorV4"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/UB/UBProcessorV4.m %s: td is nil"
- "/System/Library/ImagingNetworks"
- "36@0:8i16i20r^(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})24f32"
- "40@0:8i16i20r^(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})2432"
- "<<<< CMIImagePyramid >>>> %s: Unable to create pipeline state for _downscale2x"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed prepareing frame: %d"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to create pipeline state for RawDF::brightnessMatch"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to create pipeline state for RawDF::computeAMBNRDenoiseBoostMap"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: Failed to init RDFPBLR"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: Prep stages for (T: %d ): (PB: %d), (LS: %d), (ZM: %d), (MR: %d), (WRP: %d), (PSTPLC: %d), (ZM: %.1f), (PSS: %d)"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: SifrMetadata not found in SR metadata."
- "<<<< DeepFusionProcessor (NRF) >>>> %s: _cameraInfoByPortType nil"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: _sifrMetadata cannot be nil"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: loadFrameMetadata failed for sifrMetadataDict"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: syntheticReference.metadata not valid"
- "<<<< RawDF - PowerBlur >>>> %s: Failed to allocate/init shaders."
- "<<<< RawDF - PowerBlur >>>> %s: Failed to initialize RawDFPowerBlurStage."
- "<<<< RawDF - PowerBlur >>>> %s: Failed to prewarm shaders for RawDFPowerBlurStage. "
- "<<<< RawDF - PowerBlur >>>> %s: Power Blur radius must be between 1 and %d"
- "<<<< RawDF - PowerBlur >>>> %s: _metal nil."
- "<<<< RawDF - PowerBlur >>>> %s: _stageMetal nil."
- "<<<< RawDF - PowerBlur >>>> %s: _tuningParams nil."
- "<<<< RawDF - PowerBlur >>>> %s: fillRawNoiseModelParameters failed "
- "<<<< RawDF - PowerBlur >>>> %s: frameMetadata nil."
- "<<<< RawDF - PowerBlur >>>> %s: frameProperties nil."
- "<<<< RawDF - PowerBlur >>>> %s: inputTex nil."
- "<<<< RawDF - PowerBlur >>>> %s: lscGainsTex nil."
- "<<<< RawDF - PowerBlur >>>> %s: outputTex nil."
- "<<<< RawDF - PowerBlur >>>> Fig"
- "<<<< RawDF - Zoom >>>> %s: Failed to init RawDFZoomShaders"
- "<<<< RawDF - Zoom >>>> %s: Unable to create pipeline state for kernelRawDFZoomApplyMirror"
- "<<<< RawDF - Zoom >>>> %s: Unable to create pipeline state for kernelRawDFZoomApplyZoom"
- "<<<< RawDFColorMatch >>>> %s: Unable to create kernelRawDFColorAdjustmentInplace"
- "<<<< RawDFColorMatch >>>> %s: Unable to create kernelRawDFPickRandomSamples"
- "<<<< RawDFDetectors >>>> %s: detectorsOutput NULL."
- "<<<< RawDFDownsample >>>> %s: Unable to create kernelRawDFDownsample"
- "<<<< RawDFDownsample >>>> %s: Unable to create kernelRawDFResample"
- "<<<< RawDFFlickerDetector >>>> %s: Unable to create pipeline state for kernelRawDFDetectFlicker"
- "<<<< RawDFProxy >>>> %s: Unable to create pipeline state for %s"
- "<<<< RawDFSynLong >>>> %s: Unable to create pipeline state for %s flags:%x"
- "<<<< RawDFSynRef >>>> %s: Unable to create kernelRawDFSyntheticReferenceUnpack"
- "<<<< RawDFSynRef >>>> %s: Unable to create pipeline state for %s"
- "<<<< RawDFSynRef >>>> %s: Unable to create pipeline state for %s flags:%x"
- "<<<< RawDFSynRef >>>> %s: kernelRawDFPackSyntheticReference nil."
- "<<<< RawDFSynRef >>>> %s: syntheticReference nil"
- "<<<< RawNightMode >>>> %s: Executing Dem Warp on frame %{private}@"
- "<<<< RawNightMode >>>> %s: Unable to create RawNightModeMultiFrameOutlierPixelCorrection"
- "<<<< RawNightMode >>>> %s: metal is nil"
- "<<<< SoftISP >>>> %s: (threadsPerThreadgroup.width(%lu) * threadsPerThreadgroup.height(%lu) * threadsPerThreadgroup.depth(%lu))(%lu) must be <= %lu. (kernel threadgroup size limit)"
- "<<<< SoftISP >>>> %s: (threadsPerThreadgroup.width(%lu) * threadsPerThreadgroup.height(%lu) * threadsPerThreadgroup.depth(%lu))(%lu) must not be 0."
- "<<<< SoftISP >>>> %s: Failed to init RawDFPowerBlurShaders"
- "<<<< SoftISP >>>> %s: Power Blur radius must be between 1 and %d"
- "<<<< SoftISP >>>> %s: cmdEncoder nil."
- "<<<< SoftISP >>>> %s: halfResA nil."
- "<<<< SoftISP >>>> %s: halfResBTex nil."
- "<<<< SoftISP >>>> %s: inputChromaTex nil."
- "<<<< SoftISP >>>> %s: inputLumaTex nil."
- "<<<< SoftISP >>>> %s: inputTex and outputTex are not the same size."
- "<<<< SoftISP >>>> %s: inputTex nil."
- "<<<< SoftISP >>>> %s: lscGainsTex nil."
- "<<<< SoftISP >>>> %s: outputChromaTex nil."
- "<<<< SoftISP >>>> %s: outputLumaTex nil."
- "<<<< SoftISP >>>> %s: outputTex nil."
- "<<<< SoftISP >>>> %s: params nil."
- "<<<< SoftISP >>>> %s: threadsPerThreadgroup.depth(%lu) must be <= %lu."
- "<<<< SoftISP >>>> %s: threadsPerThreadgroup.height(%lu) must be <= %lu."
- "<<<< SoftISP >>>> %s: threadsPerThreadgroup.width(%lu) must be <= %lu."
- "<<<< SoftISP >>>> %s: tmpTex nil."
- "@\"H13FastPowerBlurShaders\""
- "@\"H13FastPowerBlurStageMetal\""
- "@\"RawDFFrames\""
- "@\"RawDFInputFrame\""
- "@\"RawDFPowerBlurStage\""
- "@\"RawDFPowerBlurTuningParams\""
- "@\"RawNightModeDemWarpStage\""
- "@24@0:8^{RawNightModeMultiFrameOutlierPixelCorrectionOptions=ii}16"
- "@24@0:8r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16"
- "@32@0:8r*16@24"
- "@40@0:8@16@24B32i36"
- "@56@0:8{?=(?=If)(?=If)fBfBf}16f44^f48"
- "B32@0:8^{DeepFusionRawNoiseModelParameters=ffffCf}16r^{exposureParameters=ffffffffffffffffffffffffBBBfBfffif}24"
- "CPB"
- "CameraSetup.plist"
- "ColorMatchThreshold"
- "Error while creating bright-light green-ghost pipeline state."
- "Error while creating common green-ghost pipeline state."
- "Error while creating low-light green-ghost pipeline state."
- "Failed to compile shaders"
- "Failed to create rwppDownsampleAndConvert10To8"
- "H13FastPowerBlur::PowerBlur_%s"
- "H13FastPowerBlurConfig"
- "H13FastPowerBlurConfig.m"
- "H13FastPowerBlurShaders"
- "H13FastPowerBlurShaders.m"
- "H13FastPowerBlurStage"
- "H13FastPowerBlurStage.m"
- "H13FastPowerBlurStageArgs"
- "H13FastPowerBlurStageArgs.m"
- "H13FastPowerBlurStageMetal"
- "HighFrequencyNoiseThreshold"
- "IspStats0"
- "LTM LUT has incorrect dimensions"
- "LTM grid has unsupported dimensions"
- "OISAdaptation"
- "OISAdaptationMethod"
- "PowerBlur"
- "Radius"
- "RawDFFrames"
- "RawDFInputFrame"
- "RawDFInputFrameV4.m"
- "RawDFLanczos: cannot instantiate _lanczos3_half4_sqr2"
- "RawDFPowerBlurStage"
- "RawDFPowerBlurStageV4.m"
- "RawDFPowerBlurTuningParams"
- "RawNightModeDemWarpStage"
- "RawNightModeDemWarpStageV4.m"
- "SifrMetadata"
- "T@\"<MTLComputePipelineState>\",R,N,V_applyPowerBlur"
- "T@\"<MTLComputePipelineState>\",R,N,V_remosaicRGB"
- "T@\"<MTLComputePipelineState>\",R,N,V_remosaicYUV"
- "T@\"<MTLComputePipelineState>\",R,N,V_resampleHalfSizeToFullSizeRGB"
- "T@\"<MTLComputePipelineState>\",R,N,V_resampleHalfSizeToFullSizeYUV"
- "T@\"<MTLComputePipelineState>\",R,N,V_resampleRawAndCreateHighFrequencyMap"
- "T@\"H13FastPowerBlurShaders\",R,N,V_shaders"
- "T@\"NSMutableArray\",R,N,V_frames"
- "T@\"RawDFInputFrame\",R,N"
- "T@\"RawDFInputFrame\",R,N,V_longFrame"
- "T@\"RawDFInputFrame\",R,N,V_quadraFrame"
- "T@\"RawDFInputFrame\",R,N,V_referenceEv0Frame"
- "T@\"RawDFInputFrame\",R,N,V_sifrFrame"
- "T@\"RawDFInputFrame\",R,N,V_syntheticReferenceFrame"
- "T@\"RawDFInputFrame\",R,N,V_syntheticReferenceFusionMap"
- "T@\"RawDFPowerBlurTuningParams\",&,N,V_tuningParams"
- "TB,R,N,V_hasStandardMetadata"
- "T^{__IOSurface=},N"
- "T^{__IOSurface=},N,V_regwarpInputSurface"
- "T^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB},R,N"
- "T^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB},R,N,V_HDRltmCurves"
- "T^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB},R,N,V_ltmCurves"
- "T^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB},R,N,V_ltmCurvesForBackground"
- "Ti,R,N,V_sifrFrameIndex"
- "T{LearnedNRUniforms={ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}ffffffffffffBBB},N,V_frameProperties"
- "Unable to create ColorCubeCorrectionShaders"
- "Unable to init base class for GuidedFilterShaders"
- "Unable to init base class for SemanticStylesShaders"
- "Unable to init base class for SubjectRelightingShaders"
- "Wrong LTC dimensions."
- "[3@\"<NRFSubProcessor>\"]"
- "[currentInputFrame prepareInputFrame] == 0 "
- "^.+(\\.|_)(%@G|%@)(\\.|_).+$"
- "^.+(\\.|_)(%@|%@)(\\.|_).+$"
- "^{LearnedNRUniforms={ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}ffffffffffffBBB}16@0:8"
- "^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}"
- "^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16@0:8"
- "_applyPowerBlur"
- "_applyPowerBlurWithParams:halfResATex:halfResBTex:commandBuffer:"
- "_bgBlur[blurSelector]"
- "_bgSplat[toneMappingGuideEnabled]"
- "_calculateReadNoise:"
- "_currentCommandBuffer"
- "_deepFusionEnabled"
- "_deepFusionSyntheticReferenceReferenceIsSIFR"
- "_demWarp"
- "_demWarpPipelineBayer"
- "_demWarpPipelineBayer.maxTotalThreadsPerThreadgroup >= imageBlockWidth * imageBlockHeight"
- "_demWarpPipelineQuadra"
- "_demWarpPipelineQuadra.maxTotalThreadsPerThreadgroup >= imageBlockWidth * imageBlockHeight"
- "_enableDeepFusion"
- "_enableUBFusion"
- "_hasStandardMetadata"
- "_isBayer:"
- "_ltmApply"
- "_ltmApplyBG"
- "_multiFrameOutlierPixelCorrectionSkip11PipelineState is nil"
- "_multiFrameOutlierPixelCorrectionSkip12PipelineState is nil"
- "_multiFrameOutlierPixelCorrectionSkip21PipelineState is nil"
- "_multiFrameOutlierPixelCorrectionSkip22PipelineState is nil"
- "_networkVersion"
- "_nrfConfig->_compressionLevel >= (int)compressionFootprint"
- "_nrfPlist->proxyAssetEV0RefDenoising"
- "_nrfPlist->proxyAssetEVMRefDenoising"
- "_pipelineStates[PROGRAM_COMPUTE_REPAIRVALS]"
- "_pipelineStates[PROGRAM_CROP]"
- "_pipelineStates[PROGRAM_PROCESS_REPAIRVALS]"
- "_pipelineStates[PROGRAM_REPAIR]"
- "_pipelineStates[PROGRAM_UNCROP]"
- "_preprocessSyntheticReferenceFrame"
- "_rawDFPowerBlurStage"
- "_rawDFSoftLTMMode"
- "_regwarpInputSurface"
- "_remosaicRGB"
- "_remosaicRgbWithParams:inputTex:lscGainsTex:outputTex:commandBuffer:"
- "_remosaicYUV"
- "_remosaicYuvWithParams:inputLumaTex:inputChromaTex:lscGainsTex:outputTex:commandBuffer:"
- "_resampleHalfSizeToFullSizeRGB"
- "_resampleHalfSizeToFullSizeRgbWithParams:inputTex:halfResTex:outputTex:commandBuffer:"
- "_resampleHalfSizeToFullSizeYUV"
- "_resampleHalfSizeToFullSizeYuvWithParams:inputLumaTex:inputChromaTex:halfResTex:outputLumaTex:outputChromaTex:commandBuffer:"
- "_resampleRawAndCreateHighFrequencyMap"
- "_resampleRawAndCreateHighFrequencyMapWithParams:rawTex:halfResTex:commandBuffer:"
- "_softLtmRawDFMode"
- "_srlEnable"
- "_swfrEnabled"
- "_ubFusionEnabled"
- "_useSyntheticReferenceForInferences"
- "_validateThreadsPerThreadgroup:forPipeline:"
- "_warpAdditionalFrameWithBlendingWeightPipeline[i]"
- "_warpPipeline[i]"
- "_warpRGBAWithBlendingWeightAndConfidencePipeline[i]"
- "_warpWithBlendingWeightAndConfidencePipeline[i]"
- "_warpWithBlendingWeightPipeline[i]"
- "_warpWithConfidencePipeline[i]"
- "allocateBuffersForNetwork:bindMode:bindBuffers:descriptions:textures:pixelBuffers:numBuffers:pixelFormat:metalContext:"
- "applyPowerBlur"
- "auxiliaryPixelBufferSizeForAuxiliaryType:inputPixelFormat:width:height:"
- "auxiliaryPixelBufferSizeForPipeline:auxiliaryType:inputPixelFormat:width:height:"
- "availableImagingNetworksWithExtension:"
- "baseNetworkPath"
- "centerCropOffsetX"
- "centerCropOffsetY"
- "compileShader:lumaWrite:chromaWrite:"
- "computeAverageCurve:withLTM:andGTC:"
- "computeGainMapWithInput:secondInput:output:properties:mpconfig:"
- "computeLTM:metadata:applyCCM:"
- "containsString:"
- "contentsOfDirectoryAtPath:error:"
- "convertRawDFNoiseModel:toPowerBlurNoiseModel:"
- "createBasicComputeShader:metal:"
- "createPipelineStateWithMetal:vFunction:fShaderName:outputColorMetalFormat:"
- "createPipelineStateWithMetal:vFunction:fShaderName:outputColorMetalFormat:constantValues:"
- "createShaderWithOptions:"
- "deep_fusion_version"
- "defaultManager"
- "defaultTuning"
- "demWarpBayer"
- "demWarpQuadra"
- "demWarpStage"
- "doGainMapOnSingleFrameLuma:chroma:properties:output:outputHeadroom:nrfPlist:"
- "err = [self _validateThreadsPerThreadgroup:threadsPerThreadgroup forPipeline:pipeline] == 0 "
- "espresso.bundle"
- "espresso.net"
- "f24@0:8r^{?=fff}16"
- "f32@0:8r^{exposureParameters=ffffffffffffffffffffffffBBBfBfffif}16@24"
- "flexRangeMetadataDictionary:mppHeadroom:newHeadroom:"
- "fragFunc"
- "fragFuncToneMapped"
- "fragmentFunction"
- "fullRangeVertexDesc"
- "getFilePathForNetworkIdentifier:withExtension:"
- "getFrameWithUniqueFrameId:"
- "getGDCParametersWithCameraInfoByPortType:"
- "getGDCParametersWithCameraInfoByPortType:withMetadata:"
- "getLumaPedestalWithProperties:plistSource:"
- "getPowerBlurConfigForInputFrame:PowerBlurConfig:enablePowerBlur:"
- "getRawNightModeNetworkBasePath"
- "getRawNightModeNetworkPathFromBasePath:fromNetworkName:"
- "getRegDenseMapPropertiesWithImageWidth:imageHeight:regDenseParams:"
- "h13f.powerblur.outputChromaTex"
- "h13f.powerblur.outputLumaTex"
- "hasStandardMetadata"
- "hasSuffix:"
- "homography || shiftMap"
- "i100@0:8r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}24r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}32{?=[3]}40B88@92"
- "i120@0:8@16@24@32@40@48@56@64@72@80@8896^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffff}112"
- "i204@0:8@16@24{?=[3]}3280@96f104{?=[3]}108i156f160B164f168172@180@188f196f200"
- "i212@0:8i16@20@28@36@44@52@60@68{CGRect={CGPoint=dd}{CGSize=dd}}76f108f112i116^{?=fffffffffBffffffffffffB}120@128@136@144Q152[10{?={CGRect={CGPoint=dd}{CGSize=dd}}SSS}]160B168B172f176@180@188@196@204"
- "i24@0:8^{__IOSurface=}16"
- "i24@0:8r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16"
- "i324@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120{CGRect={CGPoint=dd}{CGSize=dd}}128f160f164i168Q172[10{?={CGRect={CGPoint=dd}{CGSize=dd}}SSS}]180B188B192f196{?=fffffffffBffffffffffffB}200@292@300@308@316"
- "i32@0:8@16^{?=BB         [5[5 ]]}24"
- "i32@0:8@16^{?=fffffffffffffffffffff[3f]ffffffffffffffIIfIffIffffffffff}24"
- "i32@0:8@16^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}}24"
- "i32@0:8[65f]16r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}24"
- "i36@0:8^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}16@24B32"
- "i40@0:8@16^{?=Sff{?=fffff}ff(?=)(?=)}24^B32"
- "i40@0:8@16r^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}}24@32"
- "i40@0:8@16r^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}}24^f32"
- "i40@0:8^{RegDenseParameters=fff^{NoiseModel}ii@@B}16Q24Q32"
- "i44@0:8@16^{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}24B32^{GOCConfig=BIB}36"
- "i48@0:8@16@24^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}}32@40"
- "i48@0:8@16^{?=^vi}24^^v32^^v40"
- "i48@0:8^{opaqueCMSampleBuffer=}16@24@32@40"
- "i48@0:8r^{?=Sff{?=fffff}ff(?=)(?=)}16@24@32@40"
- "i48@0:8r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}16^{__CVBuffer=}24@3240"
- "i48@0:8{?=QQQ}16@40"
- "i52@0:8@16i24@28@36@44"
- "i52@0:8^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffff}16@24@32I40I44B48"
- "i56@0:8@16@24@32@40^{?=BBffff{?=[3]}ffIIIfffffffIfIffIffffffff}48"
- "i56@0:8@16@24^@32@40^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}48"
- "i56@0:8@16@24^{FlareDetectionConfig=SSffSfIBB}32^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}40@48"
- "i56@0:8@16@24^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}}3240"
- "i56@0:8@16@24^{HuemapConfig=ffffBBBBS}32@40^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}48"
- "i56@0:8r^{?=Sff{?=fffff}ff(?=)(?=)}16@24@32@40@48"
- "i60@0:8@16^{SyntheticThumbnailConfig=S{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}}24^{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}3240B56"
- "i60@0:8@16i24@28r^{?=[3]}36@44@52"
- "i60@0:8^{?=@@@@@@@@@@}16@24^{HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}32^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}}40@48B56"
- "i64@0:8@16@24@32@40^f48@56"
- "i64@0:8@16@24@32^{HuemapMotionCompensationConfig=ffffBBBBSfSfffffS}40@48^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}56"
- "i64@0:8^{?=iffBBB{?=}}16@24@32Q40r^{?=fffffffffB}48@56"
- "i64@0:8r^{?=Sff{?=fffff}ff(?=)(?=)}16@24@32@40@48@56"
- "i68@0:8@16@24@32@40^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}48@56B64"
- "i68@0:8@16^{GOCConfig=BIB}24^{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}32B4044@60"
- "i68@0:8@16^{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}24B3236@52^{GOCConfig=BIB}60"
- "i68@0:8^@16^@24^@32^@40^48r^{ltmCurves=(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]})(?=S[18242c][110616c]{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSS[0S]}{?=SSSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSS[0S]}{?=SSSSSSSSSSSs[0{?={?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}{?=sss}}]}){?=S[0S]}[257S]{?=S[0S]}[257S]f[65f]B[257S]BfB}56B64"
- "i72@0:8@16@2432r^{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}48^{HRConfig={?=iiSSBBBBBBB}Sfffffffff{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}}56@64"
- "i72@0:8@16^@24^{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}32B40@4452B68"
- "i72@0:8@16^{?=@@}24^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}32^{HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}40^{HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}48@56B64B68"
- "i72@0:8@16^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}24@32i40@44@52@60B68"
- "i72@0:8r^{?=Sff{?=fffff}ff(?=)(?=)}16@24@32@40@48@56@64"
- "i76@0:8@16^@24^{LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}32@4048^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}64B72"
- "i76@0:8@16i24@28r^{?=[3]}36@44@52^{?=ff[8f][8f]f}60^{?=ff[8f][8f]f}68"
- "i76@0:8^{?=^vi}16i24B28r^{NameAndSize=*QQ}32^@40^^{__CVBuffer}48Q56I64@68"
- "i84@0:8@16@24@32^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}40B48B52B56@6068"
- "i92@0:8^{?=@@@}16@24@32B40B44B48@52^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}6068^{HRDConfig=i{?=BBBBBBBBBBBBBBBBBBBBBBBii}{?=ffff}fffffff[5f]ff[7f]ff[5f]ff[7f]{?=ff}{?=ff}}84"
- "i96@0:8^{?=iffBBB{?=}}16^i24@32@40@48@56@64@72@80@88"
- "i96@0:8r^{?=BB         [5[5 ]]}16@24@32B40B44{?=QQQ}48{?=QQQ}72"
- "imaging_networks_path"
- "initWithContext:cameraInfo:isQuadra:deviceGeneration:"
- "initWithMetal:vertFunc:fragName:pixelFormat:pixelFormat2:"
- "initWithMetal:vertFunc:pixelFormatLuma:pixelFormatChroma:"
- "initWithPattern:options:error:"
- "inputRGBTex.pixelFormat == MTLPixelFormatRGBA16Float"
- "inputTex.pixelFormat == MTLPixelFormatRGBA16Float"
- "intermediateVersion"
- "isEnabledForFrameType:"
- "learnednoisereduction-quadra-v2"
- "loadEspressoNetworkFromPath:andStoreNetwork:andPlan:espressoContext:"
- "maxThreadsPerThreadgroup"
- "networkVersion"
- "newFunctionWithName:constantValues:error:"
- "newFunctionWithName:constantValues:pipelineLibrary:error:"
- "newOutputAuxiliaryPixelBufferForUniqueID:pixelFormat:width:height:"
- "newRenderPipelineStateWithDescriptor:error:"
- "normalizeLTMTable:"
- "numberOfMatchesInString:options:range:"
- "originalCicGridHeader->version == FigCaptureStreamLSCQuadraChannelImbalanceCorrectionGainGridVersion_1"
- "outputRGBTex"
- "outputRGBTex.pixelFormat == MTLPixelFormatRGBA16Float"
- "packSyntheticReference:toOutputTex:"
- "performLTM:bilateralGrid:bilateralGridHomography:detailEnhance:darkestFrameMetadata:scaleInput:colorCorrection:outputMode:chromaGainAdjPower:inputIsLinear:chromaBias:gridScaleFactor:personMask:highlightCompression:utmForegroundFactor:utmBackgroundFactor:"
- "pipelineDescriptor"
- "pipelineDescriptor.fragmentFunction"
- "pipelineDescriptor.vertexFunction"
- "pipelineLibrary"
- "pixelSizeInBytes > 0"
- "powerBlurTuning"
- "prepareInputFrame"
- "prepareWithRegDenseParams:imageWidth:imageHeight:"
- "proxyAssetEV0RefDenoising"
- "proxyAssetEVMRefDenoising"
- "quadraTuning"
- "rawDFSoftLTMMode"
- "registersIspStats.count"
- "regwarpInputSurface"
- "remosaicRGB"
- "remosaicYUV"
- "renderPipelineDesc"
- "resampleHalfSizeToFullSizeRGB"
- "resampleHalfSizeToFullSizeYUV"
- "resampleRawAndCreateHighFrequencyMap"
- "runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:"
- "runDemWarpInputTex:firstPix:outputRGBTex:withHomography:shiftMap:blendingWeight:inputFrameGDCParams:outputFrameGDCParams:"
- "runDemWarpOnFrame:outputTexture:label:"
- "runDetectorsToOutput:withRequestedSyntheticReferenceMode:withEv0:withEvm:withSRTuning:withDownSampleStage:withColorMatchStage:withMotionDetection:withgrayGhostDetection:withFlickerDetection:"
- "runMotionToOutput:withRefFrame:withOtherFrame:withPyramidBand:withTuningParams:withMotionDetection:"
- "runWithConfig:inputLumaTex:inputChromaTex:outputLumaTex:outputChromaTex:lscGainsTex:"
- "runWithConfig:inputTex:outputTex:lscGainsTex:"
- "runWithInput:secondInput:output:SDRLTMTable:HDRLTMTable:SDRGlobalLTMCurve:HDRGlobalLTMCurve:SDRGTCCurve:HDRGTCCurve:highlightCompression:hazeCorrection:config:"
- "runWithInputFrame:frameType:inputTex:lscGainsTex:outputTex:"
- "setAllocationHint:"
- "setFragmentFunction:"
- "setGainMapConfig:tuning:frameMetadata:width:height:isLinear:"
- "setPipelineLibrary:"
- "setRegisters:"
- "setRegwarpInputSurface:"
- "setThreadgroupMemoryLength:atIndex:"
- "setVertexDescriptor:"
- "setVertexFunction:"
- "sifrFrameIndex"
- "startSFDWithInputSampleBuffer:inputMetadata:outputImage:tuning:"
- "v24@0:8^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}16"
- "v24@0:8r^{?={LSCConfig=BSSfIBf(?={?=SSSS})(?=[4]{?=})[4]}@@}16"
- "v320@0:8{LearnedNRUniforms={ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}ffffffffffffBBB}16"
- "v32@0:8^{RawDFRawNoiseModelParameters=ffffff}16^{?=fffff}24"
- "v40@0:8[65f]16r^S24r^S32"
- "verifyIOSurfaceCompression:"
- "vertFunc"
- "vertexFunction"
- "{?=\"dlux_x1\"f\"dlux_y1\"f\"dlux_x2\"f\"dlux_y2\"f\"dsoft_x1\"f\"dsoft_y1\"f\"dsoft_x2\"f\"dsoft_y2\"f\"dlow_x1\"f\"dlow_y1\"f\"dlow_x2\"f\"dlow_y2\"f\"diso_x1\"f\"diso_y1\"f\"diso_x2\"f\"diso_y2\"f\"dhist_low\"f\"dhist_mid\"f\"dhist_hi\"f\"dhist_max_gnorm\"f\"hdr_ref\"f\"hdr_mix\"[3f]\"clipped_pixels_thresh\"f\"clipping_compression_start\"f\"clipping_compression_end\"f\"dclip_x1\"f\"dclip_y1\"f\"dclip_x2\"f\"dclip_y2\"f\"clip_power\"f\"base_EDR\"f\"hdr_mix_max_y1\"f\"hdr_mix_max_y2\"f\"hdr_mix_max_x1\"f\"hdr_mix_max_x2\"f\"shadow_val\"f\"HL_ind\"I\"HL_starting_point\"I\"thr_HL\"f\"ht_top_thr1\"I\"dw_change_max_for_mids_top\"f\"dw_change_max_for_mids_th1\"f\"ht_top_thr2\"I\"dw_change_max_for_mids_th2\"f\"eps_for_log\"f\"x1_dw_change_for_mids\"f\"x2_dw_change_for_mids\"f\"exposureBiasFactor\"f\"fullContrastBoost\"f\"ht_use_contrast\"f\"gammaBoost\"f\"ht_use_gamma\"f\"ltm_change_Hls_thresh\"f}"
- "{?=\"lscConfig\"{LSCConfig=\"enabled\"B\"cropOrigin\"\"sensorDimension\"\"gridWidth\"S\"gridHeight\"S\"gridMaxGainReciprocal\"f\"gridIntervalReciprocal\"\"firstPix\"I\"isQuadra\"B\"flashMixingWeight\"f\"yOffset\"(?=\"vec\"\"\"{?=\"gr\"S\"r\"S\"b\"S\"gb\"S})\"yOffsetQuadra\"(?=\"vec\"[4]\"\"{?=\"gr\"\"r\"\"b\"\"gb\"})\"quadraPixelOriginByChannel\"[4]}\"lscCenterCropOffset\"\"lscGainsTex\"@\"<MTLTexture>\"\"flashLSCGainsTex\"@\"<MTLTexture>\"}"
- "{?=\"outputOffset\"\"dotFixOn\"B\"localSharpClip\"B\"dotDetectThreshold\" \"strength\" \"phiSlope\" \"phiKnee\" \"sharpScaling\" \"overshootMitigation\" \"modulationLow\" \"modulationHigh\" \"modulationSlope\" \"sharpeningKernel\"[5[5 ]]}"
- "{LearnedNRUniforms=\"whiteBalanceGains\"\"cscParams\"{ColorSpaceConversionParameters=\"cscMatrixFwd\"{?=\"columns\"[3]}\"cscMatrix\"{?=\"columns\"[3]}\"colorCorrectionMatrix\"{?=\"columns\"[3]}\"transferFunctionFwd\"{TransferFunctionParameters=\"linearScale\"f\"linearThreshold\"f\"nonLinearScale\"f\"nonLinearBias\"f\"nonLinearPower\"f}\"transferFunctionInv\"{TransferFunctionParameters=\"linearScale\"f\"linearThreshold\"f\"nonLinearScale\"f\"nonLinearBias\"f\"nonLinearPower\"f}\"finalScaleFwd\"f\"finalScale\"f\"chromaBias\"f\"outputToLinearYCbCr\"B\"clampNegativesToZero\"B\"applyColorCorrection\"B\"useGpuCSC\"B}\"lscScale\"\"lscOffset\"\"lscNormalization\"f\"lscModulationWeight\"f\"photonScaledReadNoiseStd\"f\"sensorScaledShotNoiseVar\"f\"modulatedPhotonScaledReadNoiseStd\"f\"modulatedSensorScaledShotNoiseVar\"f\"lumaAddBackWeight\"f\"lumaAddBackBand0Weight\"f\"lumaAddBackClipToSNR\"f\"lumaAddBackLSCModulation\"f\"preNetworkScale\"f\"postNetworkScale\"f\"isQuadra\"B\"isVersion2\"B\"rotateTile180\"B}"
- "{LearnedNRUniforms={ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}ffffffffffffBBB}16@0:8"
- "{MiwbConfig=\"thumbnailSize\"\"hazeInputMatCCM\"{?=\"columns\"[3]}\"hazeOutputInvMatCCM\"{?=\"columns\"[3]}\"miwbInputInvMatCCM\"{?=\"columns\"[3]}\"miwbOutputMatCCM\"{?=\"columns\"[3]}\"matSkyCcm\"{?=\"columns\"[3]}\"matSkinCcm\"{?=\"columns\"[3]}\"globalWhitePoint\"\"skyWhitePoint\"\"skinWhitePoint\"\"coolStrength\"f\"warmStrength\"f\"whiteL\"f\"satMapFactor\"f\"blueSky\"f\"dayLightWeight\"f}"
- "{RawDFPowerBlurTuningParamsSpecific=\"enabled\"B\"radius\"S\"colorMatchThreshold\"f\"highFreqNoiseThreshold\"f}"
- "{RegDenseMapProperties={RegDenseMapProperty=Q}{RegDenseMapProperty=Q}{RegDenseMapProperty=Q}}40@0:8Q16Q24^{RegDenseParameters=fff^{NoiseModel}ii@@B}32"
- "\x83"
- "\xf0\xf0\x84"
- "\xf0\xf0\xf0\xd1"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0q"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf1"

```
