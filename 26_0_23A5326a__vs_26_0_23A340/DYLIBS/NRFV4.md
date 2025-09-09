## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-664.2.8.0.1
-  __TEXT.__text: 0x25805c
-  __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_methlist: 0x103f0
-  __TEXT.__const: 0x102790
-  __TEXT.__cstring: 0x2fa03
-  __TEXT.__gcc_except_tab: 0x153c
-  __TEXT.__oslogstring: 0x253fc
+664.2.10.0.0
+  __TEXT.__text: 0x287d48
+  __TEXT.__auth_stubs: 0xf90
+  __TEXT.__objc_methlist: 0x11b48
+  __TEXT.__const: 0x1027f0
+  __TEXT.__cstring: 0x33305
+  __TEXT.__gcc_except_tab: 0x19b4
+  __TEXT.__oslogstring: 0x349c5
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x4890
-  __TEXT.__objc_classname: 0x2dc0
-  __TEXT.__objc_methname: 0x31888
-  __TEXT.__objc_methtype: 0x15efd
-  __TEXT.__objc_stubs: 0x14ee0
-  __DATA_CONST.__got: 0xc08
-  __DATA_CONST.__const: 0x12e0
-  __DATA_CONST.__objc_classlist: 0xc98
-  __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xf0
+  __TEXT.__unwind_info: 0x4dc8
+  __TEXT.__objc_classname: 0x31f1
+  __TEXT.__objc_methname: 0x33d34
+  __TEXT.__objc_methtype: 0x17110
+  __TEXT.__objc_stubs: 0x16200
+  __DATA_CONST.__got: 0xc28
+  __DATA_CONST.__const: 0x1380
+  __DATA_CONST.__objc_classlist: 0xd98
+  __DATA_CONST.__objc_catlist: 0x18
+  __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6170
+  __DATA_CONST.__objc_selrefs: 0x6690
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x9a0
-  __DATA_CONST.__objc_arraydata: 0xe40
-  __AUTH_CONST.__auth_got: 0x7d8
-  __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x12e60
-  __AUTH_CONST.__objc_const: 0x328c8
+  __DATA_CONST.__objc_superrefs: 0xa68
+  __DATA_CONST.__objc_arraydata: 0xea8
+  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__const: 0x820
+  __AUTH_CONST.__cfstring: 0x13920
+  __AUTH_CONST.__objc_const: 0x37238
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_arrayobj: 0xae0
+  __AUTH_CONST.__objc_arrayobj: 0xb40
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x550
-  __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x3510
-  __DATA.__data: 0xb48
+  __AUTH.__objc_data: 0x1220
+  __DATA.__objc_ivar: 0x3a24
+  __DATA.__data: 0xba8
   __DATA.__common: 0x20
   __DATA.__bss: 0x14
-  __DATA_DIRTY.__objc_data: 0x7440
+  __DATA_DIRTY.__objc_data: 0x75d0
   __DATA_DIRTY.__bss: 0x150
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 52110548-1F37-3EC3-94C9-4BC4B8FE383D
-  Functions: 12493
-  Symbols:   36735
-  CStrings:  18067
+  UUID: 7490E0F0-1715-3FEB-A880-C3AFE84696FE
+  Functions: 13362
+  Symbols:   39382
+  CStrings:  19267
 
Symbols:
+ +[LearnedDemosaicNetworkStage prewarmShaders:]
+ +[LearnedDemosaicNetworkStage prewarmShaders:].cold.1
+ +[LearnedDemosaicNetworkStage prewarmShaders:].cold.2
+ +[LearnedFusionDeghostingMitigation prewarmShaders:]
+ +[LearnedFusionDeghostingMitigation prewarmShaders:].cold.1
+ +[LearnedFusionHighlightMitigation prewarmShaders:]
+ +[LearnedFusionHighlightMitigation prewarmShaders:].cold.1
+ +[LearnedFusionNetworkStage prewarmShaders:]
+ +[LearnedFusionNetworkStage prewarmShaders:].cold.1
+ +[LearnedFusionNetworkStage prewarmShaders:].cold.2
+ +[LearnedHRNRNetworkPostStage prewarmShaders:tuningParameters:]
+ +[LearnedHRNRNetworkPostStage prewarmShaders:tuningParameters:].cold.1
+ +[LearnedHRNRNetworkPreStage prewarmShaders:tuningParameters:]
+ +[LearnedHRNRNetworkPreStage prewarmShaders:tuningParameters:].cold.1
+ +[LearnedHRNRNetworkSharedParameters rotate180ForBayerPattern:]
+ +[LearnedHRNRNetworkStage prewarmShaders:tuningParameters:]
+ +[LearnedHRNRNetworkStage prewarmShaders:tuningParameters:].cold.1
+ +[LearnedHRNRNetworkStage prewarmShaders:tuningParameters:].cold.2
+ +[LearnedHRNRNetworkStage prewarmShaders:tuningParameters:].cold.3
+ +[LearnedHRNRTileScheduler prewarmShaders:tuningParameters:]
+ +[LearnedHRNRTileScheduler prewarmShaders:tuningParameters:].cold.1
+ -[CMITiledInferenceProcessorTilePipelineStage(LearnedHRNR) initLearnedHRNRWithMetalContext:forQuadra:error:]
+ -[CMITiledInferenceProcessorTilePipelineStage(LearnedHRNR) initLearnedHRNRWithMetalContext:forQuadra:error:].cold.1
+ -[CMITiledInferenceProcessorTilePipelineStage(LearnedHRNR) initLearnedHRNRWithMetalContext:forQuadra:error:].cold.2
+ -[LearnedDemosaicNetworkPostANEStage .cxx_destruct]
+ -[LearnedDemosaicNetworkPostANEStage consts]
+ -[LearnedDemosaicNetworkPostANEStage initWithMetal:]
+ -[LearnedDemosaicNetworkPostANEStage initWithMetal:].cold.1
+ -[LearnedDemosaicNetworkPostANEStage outputDemosaicRgbTexture]
+ -[LearnedDemosaicNetworkPostANEStage processTilePipelineStage:]
+ -[LearnedDemosaicNetworkPostANEStage processTilePipelineStage:].cold.1
+ -[LearnedDemosaicNetworkPostANEStage setOutputDemosaicRgbTexture:]
+ -[LearnedDemosaicNetworkPreANEStage .cxx_destruct]
+ -[LearnedDemosaicNetworkPreANEStage initWithMetal:]
+ -[LearnedDemosaicNetworkPreANEStage initWithMetal:].cold.1
+ -[LearnedDemosaicNetworkPreANEStage processTilePipelineStage:]
+ -[LearnedDemosaicNetworkPreANEStage processTilePipelineStage:].cold.1
+ -[LearnedDemosaicNetworkPreANEStage processTilePipelineStage:].cold.2
+ -[LearnedDemosaicNetworkPreANEStage processTilePipelineStage:].cold.3
+ -[LearnedDemosaicNetworkShared .cxx_destruct]
+ -[LearnedDemosaicNetworkShared demosaicNetworkParameters]
+ -[LearnedDemosaicNetworkShared getDemosaicNetworkParameters]
+ -[LearnedDemosaicNetworkShared getTileCount]
+ -[LearnedDemosaicNetworkShared getTileForIndex:]
+ -[LearnedDemosaicNetworkShared inputLSCGainsTexture]
+ -[LearnedDemosaicNetworkShared inputRawTexture]
+ -[LearnedDemosaicNetworkShared isQuadra]
+ -[LearnedDemosaicNetworkShared metal]
+ -[LearnedDemosaicNetworkShared setDemosaicNetworkParameters:]
+ -[LearnedDemosaicNetworkShared setInputLSCGainsTexture:]
+ -[LearnedDemosaicNetworkShared setInputRawTexture:]
+ -[LearnedDemosaicNetworkShared setIsQuadra:]
+ -[LearnedDemosaicNetworkShared setMetal:]
+ -[LearnedDemosaicNetworkStage .cxx_destruct]
+ -[LearnedDemosaicNetworkStage _getInterpolatedGainFromTuningParams:gain:]
+ -[LearnedDemosaicNetworkStage _getTotalGainFromMetadata:]
+ -[LearnedDemosaicNetworkStage getNetworkPath]
+ -[LearnedDemosaicNetworkStage getNetworkPath].cold.1
+ -[LearnedDemosaicNetworkStage initWithContext:cameraInfo:isQuadra:]
+ -[LearnedDemosaicNetworkStage initWithContext:cameraInfo:isQuadra:].cold.1
+ -[LearnedDemosaicNetworkStage initWithContext:cameraInfo:isQuadra:].cold.2
+ -[LearnedDemosaicNetworkStage initWithContext:cameraInfo:isQuadra:].cold.3
+ -[LearnedDemosaicNetworkStage initWithContext:cameraInfo:isQuadra:].cold.4
+ -[LearnedDemosaicNetworkStage initWithContext:cameraInfo:isQuadra:].cold.5
+ -[LearnedDemosaicNetworkStage initWithContext:cameraInfo:isQuadra:].cold.6
+ -[LearnedDemosaicNetworkStage initWithContext:cameraInfo:isQuadra:].cold.7
+ -[LearnedDemosaicNetworkStage processingOptions]
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:]
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.1
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.10
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.11
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.12
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.13
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.14
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.2
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.3
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.4
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.5
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.6
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.7
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.8
+ -[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:].cold.9
+ -[LearnedDemosaicNetworkStage setTuningParams:]
+ -[LearnedDemosaicNetworkStage setupNetwork]
+ -[LearnedDemosaicNetworkStage setupNetwork].cold.1
+ -[LearnedDemosaicNetworkStage setupNetwork].cold.2
+ -[LearnedDemosaicNetworkStage setupNetwork].cold.3
+ -[LearnedDemosaicNetworkStage setupNetwork].cold.4
+ -[LearnedDemosaicNetworkStage setupNetwork].cold.5
+ -[LearnedDemosaicNetworkStage setupNetwork].cold.6
+ -[LearnedDemosaicNetworkStage setupNetwork].cold.7
+ -[LearnedDemosaicNetworkStage tuningParams]
+ -[LearnedDemosaicNetworkStage updateNoiseModelParametersFromMetadata:demosaicNetworkParams:]
+ -[LearnedDemosaicNetworkStage updateNoiseModelParametersFromMetadata:demosaicNetworkParams:].cold.1
+ -[LearnedDemosaicNetworkStage updateNoiseModelParametersFromMetadata:demosaicNetworkParams:].cold.2
+ -[LearnedDemosaicNetworkStage updateNoiseModelParametersFromMetadata:demosaicNetworkParams:].cold.3
+ -[LearnedDemosaicNetworkStage updateNoiseModelParametersFromMetadata:demosaicNetworkParams:].cold.4
+ -[LearnedDemosaicNetworkStage updateNoiseModelParametersFromMetadata:demosaicNetworkParams:].cold.5
+ -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:]
+ -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:].cold.1
+ -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:].cold.2
+ -[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:].cold.3
+ -[LearnedDemosaicNetworkStageBase .cxx_destruct]
+ -[LearnedDemosaicNetworkStageBase setShared:]
+ -[LearnedDemosaicNetworkStageBase shared]
+ -[LearnedDemosaicNetworkTuningParams .cxx_destruct]
+ -[LearnedDemosaicNetworkTuningParams readPlist:]
+ -[LearnedFusionBoundInferenceResults .cxx_destruct]
+ -[LearnedFusionBoundInferenceResults initWithResult:andMetal:]
+ -[LearnedFusionBoundInferenceResults initWithResult:andMetal:].cold.1
+ -[LearnedFusionBoundInferenceResults initWithResult:andMetal:].cold.2
+ -[LearnedFusionBoundInferenceResults initWithResult:andMetal:].cold.3
+ -[LearnedFusionBoundInferenceResults initWithResult:andMetal:].cold.4
+ -[LearnedFusionBoundInferenceResults initWithResult:andMetal:].cold.5
+ -[LearnedFusionBoundInferenceResults initWithResult:andMetal:].cold.6
+ -[LearnedFusionBoundInferenceResults instanceMasks]
+ -[LearnedFusionBoundInferenceResults personMask]
+ -[LearnedFusionBoundInferenceResults setInstanceMasks:]
+ -[LearnedFusionBoundInferenceResults setPersonMask:]
+ -[LearnedFusionBoundInferenceResults setSkinMask:]
+ -[LearnedFusionBoundInferenceResults setSkyMask:]
+ -[LearnedFusionBoundInferenceResults skinMask]
+ -[LearnedFusionBoundInferenceResults skyMask]
+ -[LearnedFusionChromaSuppression .cxx_destruct]
+ -[LearnedFusionChromaSuppression initWithMetalContext:]
+ -[LearnedFusionChromaSuppression initWithMetalContext:].cold.1
+ -[LearnedFusionChromaSuppression initWithMetalContext:].cold.2
+ -[LearnedFusionChromaSuppression lfChromaSuppressionTuningParams]
+ -[LearnedFusionChromaSuppression setLfChromaSuppressionTuningParams:]
+ -[LearnedFusionChromaSuppression suppressChroma:lumaTexture:outputChromaTexture:inputMetadata:]
+ -[LearnedFusionChromaSuppression suppressChroma:lumaTexture:outputChromaTexture:inputMetadata:].cold.1
+ -[LearnedFusionChromaSuppression suppressChroma:lumaTexture:outputChromaTexture:inputMetadata:].cold.2
+ -[LearnedFusionChromaSuppression suppressChroma:lumaTexture:outputChromaTexture:inputMetadata:].cold.3
+ -[LearnedFusionChromaSuppressionTuningParams .cxx_destruct]
+ -[LearnedFusionChromaSuppressionTuningParams chromaSuppressionEnabled]
+ -[LearnedFusionChromaSuppressionTuningParams postDemosaicTuningParams]
+ -[LearnedFusionChromaSuppressionTuningParams readPlist:]
+ -[LearnedFusionChromaSuppressionTuningParams readPlist:].cold.1
+ -[LearnedFusionChromaSuppressionTuningParams readPlist:].cold.2
+ -[LearnedFusionChromaSuppressionTuningParams readPlist:].cold.3
+ -[LearnedFusionChromaSuppressionTuningParams readPlist:].cold.4
+ -[LearnedFusionConfig .cxx_destruct]
+ -[LearnedFusionConfig _processSyntheticReferenceMetadataFromReferenceEV0]
+ -[LearnedFusionConfig _processSyntheticReferenceMetadataFromReferenceEV0].cold.1
+ -[LearnedFusionConfig _processSyntheticReferenceMetadataFromReferenceEV0].cold.2
+ -[LearnedFusionConfig _processSyntheticReferenceMetadataFromReferenceEV0].cold.3
+ -[LearnedFusionConfig _processSyntheticReferenceMetadataFromReferenceEV0].cold.4
+ -[LearnedFusionConfig _processSyntheticReferenceMetadataFromReferenceEV0].cold.5
+ -[LearnedFusionConfig detectorsOutput]
+ -[LearnedFusionConfig ev0Frame]
+ -[LearnedFusionConfig hasEVM]
+ -[LearnedFusionConfig initWithFrames:]
+ -[LearnedFusionConfig longFrame]
+ -[LearnedFusionConfig ltmMetadata]
+ -[LearnedFusionConfig mainFrame]
+ -[LearnedFusionConfig runDetectors]
+ -[LearnedFusionConfig setDetectorsOutput:]
+ -[LearnedFusionConfig setEv0Frame:]
+ -[LearnedFusionConfig setHasEVM:]
+ -[LearnedFusionConfig setLongFrame:]
+ -[LearnedFusionConfig setLtmMetadata:]
+ -[LearnedFusionConfig setMainFrame:]
+ -[LearnedFusionConfig setRunDetectors:]
+ -[LearnedFusionDeghostingMitigation .cxx_destruct]
+ -[LearnedFusionDeghostingMitigation _compileShaders]
+ -[LearnedFusionDeghostingMitigation _compileShaders].cold.1
+ -[LearnedFusionDeghostingMitigation addFrame:isMainFrame:]
+ -[LearnedFusionDeghostingMitigation buildPyramidForFrame:withLabel:]
+ -[LearnedFusionDeghostingMitigation ev0FrameExposureParameters]
+ -[LearnedFusionDeghostingMitigation ev0ModulationMap]
+ -[LearnedFusionDeghostingMitigation generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:]
+ -[LearnedFusionDeghostingMitigation generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:].cold.1
+ -[LearnedFusionDeghostingMitigation generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:].cold.2
+ -[LearnedFusionDeghostingMitigation generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:].cold.3
+ -[LearnedFusionDeghostingMitigation generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:].cold.4
+ -[LearnedFusionDeghostingMitigation generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:].cold.5
+ -[LearnedFusionDeghostingMitigation generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:].cold.6
+ -[LearnedFusionDeghostingMitigation generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:].cold.7
+ -[LearnedFusionDeghostingMitigation generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:].cold.8
+ -[LearnedFusionDeghostingMitigation generateModulationMaps]
+ -[LearnedFusionDeghostingMitigation generateModulationMaps].cold.1
+ -[LearnedFusionDeghostingMitigation generateModulationMaps].cold.2
+ -[LearnedFusionDeghostingMitigation generateModulationMaps].cold.3
+ -[LearnedFusionDeghostingMitigation generateModulationMaps].cold.4
+ -[LearnedFusionDeghostingMitigation generateModulationMaps].cold.5
+ -[LearnedFusionDeghostingMitigation generateModulationMaps].cold.6
+ -[LearnedFusionDeghostingMitigation generateModulationMaps].cold.7
+ -[LearnedFusionDeghostingMitigation generateModulationMaps].cold.8
+ -[LearnedFusionDeghostingMitigation generateModulationMaps].cold.9
+ -[LearnedFusionDeghostingMitigation hasAllFrames]
+ -[LearnedFusionDeghostingMitigation initWithMetalContext:]
+ -[LearnedFusionDeghostingMitigation initWithMetalContext:].cold.1
+ -[LearnedFusionDeghostingMitigation initWithMetalContext:].cold.2
+ -[LearnedFusionDeghostingMitigation initWithMetalContext:].cold.3
+ -[LearnedFusionDeghostingMitigation longFrameExposureParameters]
+ -[LearnedFusionDeghostingMitigation longModulationMap]
+ -[LearnedFusionDeghostingMitigation mainFrameExposureParameters]
+ -[LearnedFusionDeghostingMitigation process]
+ -[LearnedFusionDeghostingMitigation process].cold.1
+ -[LearnedFusionDeghostingMitigation process].cold.2
+ -[LearnedFusionDeghostingMitigation reset]
+ -[LearnedFusionDeghostingMitigation setEv0FrameExposureParameters:]
+ -[LearnedFusionDeghostingMitigation setEv0ModulationMap:]
+ -[LearnedFusionDeghostingMitigation setLongFrameExposureParameters:]
+ -[LearnedFusionDeghostingMitigation setLongModulationMap:]
+ -[LearnedFusionDeghostingMitigation setMainFrameExposureParameters:]
+ -[LearnedFusionDeghostingMitigation setTuningParams:]
+ -[LearnedFusionDeghostingMitigation tuningParams]
+ -[LearnedFusionDeghostingMitigationTuningParams .cxx_destruct]
+ -[LearnedFusionDeghostingMitigationTuningParams readPlist:]
+ -[LearnedFusionDeghostingMitigationTuningParams readPlist:].cold.1
+ -[LearnedFusionDeghostingMitigationTuningParams readPlist:].cold.2
+ -[LearnedFusionDeghostingMitigationTuningParams readPlist:].cold.3
+ -[LearnedFusionHighlightMitigation .cxx_destruct]
+ -[LearnedFusionHighlightMitigation _compileShaders]
+ -[LearnedFusionHighlightMitigation _compileShaders].cold.1
+ -[LearnedFusionHighlightMitigation initWithMetalContext:]
+ -[LearnedFusionHighlightMitigation initWithMetalContext:].cold.1
+ -[LearnedFusionHighlightMitigation initWithMetalContext:].cold.2
+ -[LearnedFusionHighlightMitigation initWithMetalContext:].cold.3
+ -[LearnedFusionHighlightMitigation mitigateHighlightsWithInOutQuadraTexture:]
+ -[LearnedFusionHighlightMitigation mitigateHighlightsWithInOutQuadraTexture:].cold.1
+ -[LearnedFusionHighlightMitigation mitigateHighlightsWithInOutQuadraTexture:].cold.2
+ -[LearnedFusionHighlightMitigation mitigateHighlightsWithInOutQuadraTexture:].cold.3
+ -[LearnedFusionHighlightMitigation mitigateHighlightsWithInOutQuadraTexture:].cold.4
+ -[LearnedFusionHighlightMitigation mitigateHighlightsWithInOutQuadraTexture:].cold.5
+ -[LearnedFusionNetworkParameters .cxx_destruct]
+ -[LearnedFusionNetworkParameters applyDeghostingModulationForEv0LongNoises]
+ -[LearnedFusionNetworkParameters ev0DeghostingModulationMap]
+ -[LearnedFusionNetworkParameters ev0Exposure]
+ -[LearnedFusionNetworkParameters ev0RgbTex]
+ -[LearnedFusionNetworkParameters ev0TuningParams]
+ -[LearnedFusionNetworkParameters evmExposure]
+ -[LearnedFusionNetworkParameters evmRawBayerPattern]
+ -[LearnedFusionNetworkParameters evmRawTex]
+ -[LearnedFusionNetworkParameters evmRgbTex]
+ -[LearnedFusionNetworkParameters evmTuningParams]
+ -[LearnedFusionNetworkParameters lensShadingParams]
+ -[LearnedFusionNetworkParameters lensShading]
+ -[LearnedFusionNetworkParameters longDeghostingModulationMap]
+ -[LearnedFusionNetworkParameters longExposure]
+ -[LearnedFusionNetworkParameters longRgbTex]
+ -[LearnedFusionNetworkParameters longTuningParams]
+ -[LearnedFusionNetworkParameters personMaskTex]
+ -[LearnedFusionNetworkParameters setApplyDeghostingModulationForEv0LongNoises:]
+ -[LearnedFusionNetworkParameters setEv0DeghostingModulationMap:]
+ -[LearnedFusionNetworkParameters setEv0Exposure:]
+ -[LearnedFusionNetworkParameters setEv0RgbTex:]
+ -[LearnedFusionNetworkParameters setEv0TuningParams:]
+ -[LearnedFusionNetworkParameters setEvmExposure:]
+ -[LearnedFusionNetworkParameters setEvmRawBayerPattern:]
+ -[LearnedFusionNetworkParameters setEvmRawTex:]
+ -[LearnedFusionNetworkParameters setEvmRgbTex:]
+ -[LearnedFusionNetworkParameters setEvmTuningParams:]
+ -[LearnedFusionNetworkParameters setLensShading:]
+ -[LearnedFusionNetworkParameters setLensShadingParams:]
+ -[LearnedFusionNetworkParameters setLongDeghostingModulationMap:]
+ -[LearnedFusionNetworkParameters setLongExposure:]
+ -[LearnedFusionNetworkParameters setLongRgbTex:]
+ -[LearnedFusionNetworkParameters setLongTuningParams:]
+ -[LearnedFusionNetworkParameters setPersonMaskTex:]
+ -[LearnedFusionNetworkParameters setSkinMaskTex:]
+ -[LearnedFusionNetworkParameters setSkyMaskTex:]
+ -[LearnedFusionNetworkParameters skinMaskTex]
+ -[LearnedFusionNetworkParameters skyMaskTex]
+ -[LearnedFusionNetworkPostANEStage .cxx_destruct]
+ -[LearnedFusionNetworkPostANEStage consts]
+ -[LearnedFusionNetworkPostANEStage initWithMetal:]
+ -[LearnedFusionNetworkPostANEStage initWithMetal:].cold.1
+ -[LearnedFusionNetworkPostANEStage initWithMetal:].cold.2
+ -[LearnedFusionNetworkPostANEStage processTilePipelineStage:]
+ -[LearnedFusionNetworkPostANEStage processTilePipelineStage:].cold.1
+ -[LearnedFusionNetworkPostANEStage processTilePipelineStage:].cold.2
+ -[LearnedFusionNetworkPostANEStage setShared:]
+ -[LearnedFusionNetworkPostANEStage shared]
+ -[LearnedFusionNetworkPreANEStage .cxx_destruct]
+ -[LearnedFusionNetworkPreANEStage consts]
+ -[LearnedFusionNetworkPreANEStage initWithMetal:]
+ -[LearnedFusionNetworkPreANEStage initWithMetal:].cold.1
+ -[LearnedFusionNetworkPreANEStage processTilePipelineStage:]
+ -[LearnedFusionNetworkPreANEStage processTilePipelineStage:].cold.1
+ -[LearnedFusionNetworkPreANEStage setShared:]
+ -[LearnedFusionNetworkPreANEStage shared]
+ -[LearnedFusionNetworkStage .cxx_destruct]
+ -[LearnedFusionNetworkStage _fillNoiseScaleFactors:noiseScaleFactors:gain:]
+ -[LearnedFusionNetworkStage _getInterpolatedGainFromTuningParams:key:gain:]
+ -[LearnedFusionNetworkStage fillRawNoiseModelParameters:exposureParams:]
+ -[LearnedFusionNetworkStage fillRawNoiseModelParameters:exposureParams:].cold.1
+ -[LearnedFusionNetworkStage fillRawNoiseModelParameters:exposureParams:].cold.2
+ -[LearnedFusionNetworkStage initWithMetal:]
+ -[LearnedFusionNetworkStage initWithMetal:].cold.1
+ -[LearnedFusionNetworkStage initWithMetal:].cold.2
+ -[LearnedFusionNetworkStage runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:]
+ -[LearnedFusionNetworkStage setTuningParams:]
+ -[LearnedFusionNetworkStage setupNetwork]
+ -[LearnedFusionNetworkStage tuningParams]
+ -[LearnedFusionNetworkStageShared .cxx_destruct]
+ -[LearnedFusionNetworkStageShared ev0DeghostingModulationMap]
+ -[LearnedFusionNetworkStageShared getTileCount]
+ -[LearnedFusionNetworkStageShared getTileForIndex:]
+ -[LearnedFusionNetworkStageShared inputLensShading]
+ -[LearnedFusionNetworkStageShared inputRawEvm]
+ -[LearnedFusionNetworkStageShared inputRgbEv0]
+ -[LearnedFusionNetworkStageShared inputRgbEvm]
+ -[LearnedFusionNetworkStageShared inputRgbLong]
+ -[LearnedFusionNetworkStageShared longDeghostingModulationMap]
+ -[LearnedFusionNetworkStageShared metal]
+ -[LearnedFusionNetworkStageShared outputChroma]
+ -[LearnedFusionNetworkStageShared outputLuma]
+ -[LearnedFusionNetworkStageShared personMaskTex]
+ -[LearnedFusionNetworkStageShared setEv0DeghostingModulationMap:]
+ -[LearnedFusionNetworkStageShared setInputLensShading:]
+ -[LearnedFusionNetworkStageShared setInputRawEvm:]
+ -[LearnedFusionNetworkStageShared setInputRgbEv0:]
+ -[LearnedFusionNetworkStageShared setInputRgbEvm:]
+ -[LearnedFusionNetworkStageShared setInputRgbLong:]
+ -[LearnedFusionNetworkStageShared setLongDeghostingModulationMap:]
+ -[LearnedFusionNetworkStageShared setMetal:]
+ -[LearnedFusionNetworkStageShared setOutputChroma:]
+ -[LearnedFusionNetworkStageShared setOutputLuma:]
+ -[LearnedFusionNetworkStageShared setPersonMaskTex:]
+ -[LearnedFusionNetworkStageShared setSkinMaskTex:]
+ -[LearnedFusionNetworkStageShared setSkyMaskTex:]
+ -[LearnedFusionNetworkStageShared skinMaskTex]
+ -[LearnedFusionNetworkStageShared skyMaskTex]
+ -[LearnedFusionNetworkTuningParams .cxx_destruct]
+ -[LearnedFusionNetworkTuningParams readPlist:]
+ -[LearnedFusionNetworkTuningParams readPlist:].cold.1
+ -[LearnedFusionNetworkTuningParams readPlist:].cold.2
+ -[LearnedFusionNetworkTuningParams readPlist:].cold.3
+ -[LearnedFusionNetworkTuningParams readPlist:].cold.4
+ -[LearnedFusionNetworkTuningParams readPlist:].cold.5
+ -[LearnedFusionNetworkTuningParams readPlist:].cold.6
+ -[LearnedFusionNetworkTuningParams readPlist:].cold.7
+ -[LearnedFusionNetworkTuningParams readPlist:].cold.8
+ -[LearnedFusionNetworkTuningParams readPlist:].cold.9
+ -[LearnedFusionProcessingOptions demosaicedImageHasHRGainApplied]
+ -[LearnedFusionProcessingOptions demosaicedImageHasLSCApplied]
+ -[LearnedFusionProcessingOptions initWithOutputHasLSCApplied:hasHRGainApplied:]
+ -[LearnedFusionProcessor .cxx_destruct]
+ -[LearnedFusionProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:]
+ -[LearnedFusionProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.1
+ -[LearnedFusionProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.2
+ -[LearnedFusionProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.3
+ -[LearnedFusionProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.4
+ -[LearnedFusionProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.5
+ -[LearnedFusionProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.6
+ -[LearnedFusionProcessor _getLscGainsTexAndParameters:lscGainsTex:lscGainsParameters:]
+ -[LearnedFusionProcessor _getLscGainsTexAndParameters:lscGainsTex:lscGainsParameters:].cold.1
+ -[LearnedFusionProcessor _getLscGainsTexAndParameters:lscGainsTex:lscGainsParameters:].cold.2
+ -[LearnedFusionProcessor _getLscGainsTexAndParameters:lscGainsTex:lscGainsParameters:].cold.3
+ -[LearnedFusionProcessor _getLscGainsTexAndParameters:lscGainsTex:lscGainsParameters:].cold.4
+ -[LearnedFusionProcessor _isGainMapSupported]
+ -[LearnedFusionProcessor _isSemanticStylesSupported]
+ -[LearnedFusionProcessor _prepareOutputMetadata:]
+ -[LearnedFusionProcessor _prepareOutputMetadata:].cold.1
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:]
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.1
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.2
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.3
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.4
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.5
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.6
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.7
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.8
+ -[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.9
+ -[LearnedFusionProcessor addFrame:]
+ -[LearnedFusionProcessor addFrame:].cold.1
+ -[LearnedFusionProcessor addFrame:].cold.2
+ -[LearnedFusionProcessor addFrame:].cold.3
+ -[LearnedFusionProcessor addInputResource:]
+ -[LearnedFusionProcessor addInputResource:].cold.1
+ -[LearnedFusionProcessor addInputResource:].cold.10
+ -[LearnedFusionProcessor addInputResource:].cold.11
+ -[LearnedFusionProcessor addInputResource:].cold.2
+ -[LearnedFusionProcessor addInputResource:].cold.3
+ -[LearnedFusionProcessor addInputResource:].cold.4
+ -[LearnedFusionProcessor addInputResource:].cold.5
+ -[LearnedFusionProcessor addInputResource:].cold.6
+ -[LearnedFusionProcessor addInputResource:].cold.7
+ -[LearnedFusionProcessor addInputResource:].cold.8
+ -[LearnedFusionProcessor addInputResource:].cold.9
+ -[LearnedFusionProcessor addToSidecar:forKey:]
+ -[LearnedFusionProcessor allocatorBackend]
+ -[LearnedFusionProcessor applyOverrides]
+ -[LearnedFusionProcessor batchCount]
+ -[LearnedFusionProcessor bindResourcesForProcessingType:prepareDescriptor:]
+ -[LearnedFusionProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:]
+ -[LearnedFusionProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:].cold.1
+ -[LearnedFusionProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:].cold.2
+ -[LearnedFusionProcessor cameraInfoByPortType]
+ -[LearnedFusionProcessor cntBracketSampleBuffers]
+ -[LearnedFusionProcessor dealloc]
+ -[LearnedFusionProcessor defringingTuningByPortType]
+ -[LearnedFusionProcessor delegate]
+ -[LearnedFusionProcessor description]
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:]
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.1
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.2
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.3
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.4
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:]
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.1
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.2
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.3
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.4
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.5
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.6
+ -[LearnedFusionProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.7
+ -[LearnedFusionProcessor doRedFaceFix]
+ -[LearnedFusionProcessor enableGreenGhostMitigation]
+ -[LearnedFusionProcessor finishProcessing]
+ -[LearnedFusionProcessor finishProcessing].cold.1
+ -[LearnedFusionProcessor finishProcessing].cold.2
+ -[LearnedFusionProcessor finishScheduling]
+ -[LearnedFusionProcessor generateGainMapIfNeeded]
+ -[LearnedFusionProcessor generateGainMapIfNeeded].cold.1
+ -[LearnedFusionProcessor generateGainMapIfNeeded].cold.2
+ -[LearnedFusionProcessor generateGainMapIfNeeded].cold.3
+ -[LearnedFusionProcessor generateGainMapIfNeeded].cold.4
+ -[LearnedFusionProcessor getDeghostingModulationMaps:longDeghostingModulationMap:]
+ -[LearnedFusionProcessor initWithCommandQueue:]
+ -[LearnedFusionProcessor maximumNumberOfReferenceFrameCandidatesToHoldForProcessing]
+ -[LearnedFusionProcessor metalCommandQueue]
+ -[LearnedFusionProcessor output]
+ -[LearnedFusionProcessor prepareToProcess:]
+ -[LearnedFusionProcessor prepareToProcess:prepareDescriptor:]
+ -[LearnedFusionProcessor prepareToProcess:prepareDescriptor:].cold.1
+ -[LearnedFusionProcessor prepareToProcess:prepareDescriptor:].cold.2
+ -[LearnedFusionProcessor prewarmWithTuningParameters:]
+ -[LearnedFusionProcessor prewarm]
+ -[LearnedFusionProcessor process]
+ -[LearnedFusionProcessor process].cold.1
+ -[LearnedFusionProcessor process].cold.2
+ -[LearnedFusionProcessor process].cold.3
+ -[LearnedFusionProcessor process].cold.4
+ -[LearnedFusionProcessor processingType]
+ -[LearnedFusionProcessor purgeResources]
+ -[LearnedFusionProcessor referenceFrameCandidatesCount]
+ -[LearnedFusionProcessor referenceFrameHasEVMinus]
+ -[LearnedFusionProcessor referenceFrameIndex]
+ -[LearnedFusionProcessor regWarpInput]
+ -[LearnedFusionProcessor reportFusionReferenceFrame:]
+ -[LearnedFusionProcessor resetInternalState]
+ -[LearnedFusionProcessor resetState]
+ -[LearnedFusionProcessor runChromaSuppressionWithInOutFusedImage:]
+ -[LearnedFusionProcessor runChromaSuppressionWithInOutFusedImage:].cold.1
+ -[LearnedFusionProcessor runChromaSuppressionWithInOutFusedImage:].cold.2
+ -[LearnedFusionProcessor runDetectors]
+ -[LearnedFusionProcessor runDetectors].cold.1
+ -[LearnedFusionProcessor runDetectors].cold.2
+ -[LearnedFusionProcessor runDetectors].cold.3
+ -[LearnedFusionProcessor runHighlightMitigation]
+ -[LearnedFusionProcessor runHighlightMitigation].cold.1
+ -[LearnedFusionProcessor runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:]
+ -[LearnedFusionProcessor runLearnedDemosaicNetworkStage]
+ -[LearnedFusionProcessor runPipeline]
+ -[LearnedFusionProcessor runSemanticInferences]
+ -[LearnedFusionProcessor runSemanticInferences].cold.1
+ -[LearnedFusionProcessor runSemanticInferences].cold.2
+ -[LearnedFusionProcessor runSemanticInferences].cold.3
+ -[LearnedFusionProcessor semanticStyleProperties]
+ -[LearnedFusionProcessor setAllocatorBackend:]
+ -[LearnedFusionProcessor setCameraInfoByPortType:]
+ -[LearnedFusionProcessor setDefringingTuningByPortType:]
+ -[LearnedFusionProcessor setDelegate:]
+ -[LearnedFusionProcessor setDoRedFaceFix:]
+ -[LearnedFusionProcessor setEnableGreenGhostMitigation:]
+ -[LearnedFusionProcessor setFusionMode:]
+ -[LearnedFusionProcessor setLinearOutputMetadata:]
+ -[LearnedFusionProcessor setLinearOutputMetadata:].cold.1
+ -[LearnedFusionProcessor setLinearOutputMetadata:].cold.2
+ -[LearnedFusionProcessor setMaximumNumberOfReferenceFrameCandidatesToHoldForProcessing:]
+ -[LearnedFusionProcessor setMetalCommandQueue:]
+ -[LearnedFusionProcessor setOutput:]
+ -[LearnedFusionProcessor setProcessingType:]
+ -[LearnedFusionProcessor setReferenceFrameCandidatesCount:]
+ -[LearnedFusionProcessor setReferenceFrameHasEVMinus:]
+ -[LearnedFusionProcessor setReferenceFrameIndex:]
+ -[LearnedFusionProcessor setRegWarpInput:]
+ -[LearnedFusionProcessor setSemanticStyleProperties:]
+ -[LearnedFusionProcessor setSharedRegWarpBuffer:]
+ -[LearnedFusionProcessor setSkipDenoising:]
+ -[LearnedFusionProcessor setSrlEnabled:]
+ -[LearnedFusionProcessor setTuningParameters:]
+ -[LearnedFusionProcessor setTuningParams:]
+ -[LearnedFusionProcessor setTuningParamsPlist:]
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:]
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.1
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.10
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.11
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.12
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.13
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.14
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.2
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.3
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.4
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.5
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.6
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.7
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.8
+ -[LearnedFusionProcessor setupWithOptions:nrfConfig:].cold.9
+ -[LearnedFusionProcessor setup]
+ -[LearnedFusionProcessor sharedRegWarpBuffer]
+ -[LearnedFusionProcessor skipDenoising]
+ -[LearnedFusionProcessor srlEnabled]
+ -[LearnedFusionProcessor supportsInputPixelFormat:]
+ -[LearnedFusionProcessor supportsInputPixelFormat:].cold.1
+ -[LearnedFusionProcessor supportsInputPixelFormat:].cold.2
+ -[LearnedFusionProcessor tuningParameters]
+ -[LearnedFusionProcessor tuningParamsPlist]
+ -[LearnedFusionProcessor tuningParams]
+ -[LearnedFusionProcessor warpWrtMainFrame:label:]
+ -[LearnedFusionProcessor warpWrtMainFrame:label:].cold.1
+ -[LearnedFusionProcessor warpWrtMainFrame:label:].cold.2
+ -[LearnedFusionProcessor warpWrtMainFrame:label:].cold.3
+ -[LearnedFusionProcessor(Tuning) prepareTuning:withProcessingMode:]
+ -[LearnedFusionProcessor(Tuning) prepareTuning:withProcessingMode:].cold.1
+ -[LearnedFusionProcessor(Tuning) prepareTuning:withProcessingMode:].cold.2
+ -[LearnedFusionProcessor(Tuning) prepareTuning:withProcessingMode:].cold.3
+ -[LearnedFusionProcessor(Tuning) prepareTuning:withProcessingMode:].cold.4
+ -[LearnedHRNRBoundInferenceResults .cxx_destruct]
+ -[LearnedHRNRBoundInferenceResults initWithResult:andMetal:]
+ -[LearnedHRNRBoundInferenceResults initWithResult:andMetal:].cold.1
+ -[LearnedHRNRBoundInferenceResults initWithResult:andMetal:].cold.2
+ -[LearnedHRNRBoundInferenceResults initWithResult:andMetal:].cold.3
+ -[LearnedHRNRBoundInferenceResults initWithResult:andMetal:].cold.4
+ -[LearnedHRNRBoundInferenceResults initWithResult:andMetal:].cold.5
+ -[LearnedHRNRBoundInferenceResults initWithResult:andMetal:].cold.6
+ -[LearnedHRNRBoundInferenceResults instanceMasks]
+ -[LearnedHRNRBoundInferenceResults personMask]
+ -[LearnedHRNRBoundInferenceResults setInstanceMasks:]
+ -[LearnedHRNRBoundInferenceResults setPersonMask:]
+ -[LearnedHRNRBoundInferenceResults setSkinMask:]
+ -[LearnedHRNRBoundInferenceResults setSkyMask:]
+ -[LearnedHRNRBoundInferenceResults skinMask]
+ -[LearnedHRNRBoundInferenceResults skyMask]
+ -[LearnedHRNRNetworkConfig deviceGeneration]
+ -[LearnedHRNRNetworkConfig init]
+ -[LearnedHRNRNetworkConfig isQuadra]
+ -[LearnedHRNRNetworkConfig setDeviceGeneration:]
+ -[LearnedHRNRNetworkConfig setIsQuadra:]
+ -[LearnedHRNRNetworkPostStage .cxx_destruct]
+ -[LearnedHRNRNetworkPostStage initWithMetal:error:]
+ -[LearnedHRNRNetworkPostStage initWithMetal:error:].cold.1
+ -[LearnedHRNRNetworkPostStage initWithMetal:error:].cold.2
+ -[LearnedHRNRNetworkPostStage output]
+ -[LearnedHRNRNetworkPostStage processTilePipelineStage:]
+ -[LearnedHRNRNetworkPostStage processTilePipelineStage:].cold.1
+ -[LearnedHRNRNetworkPostStage processTilePipelineStage:].cold.2
+ -[LearnedHRNRNetworkPostStage setOutput:]
+ -[LearnedHRNRNetworkPostStage setSharedParameters:]
+ -[LearnedHRNRNetworkPostStage sharedParameters]
+ -[LearnedHRNRNetworkPostStageOutput .cxx_destruct]
+ -[LearnedHRNRNetworkPostStageOutput bayerPattern]
+ -[LearnedHRNRNetworkPostStageOutput outputGainRatio]
+ -[LearnedHRNRNetworkPostStageOutput output]
+ -[LearnedHRNRNetworkPostStageOutput setBayerPattern:]
+ -[LearnedHRNRNetworkPostStageOutput setOutput:]
+ -[LearnedHRNRNetworkPostStageOutput setOutputGainRatio:]
+ -[LearnedHRNRNetworkPostStageOutput setTileIndicesToRun:]
+ -[LearnedHRNRNetworkPostStageOutput tileIndicesToRun]
+ -[LearnedHRNRNetworkPreStage .cxx_destruct]
+ -[LearnedHRNRNetworkPreStage _projectEv0ToEvm:]
+ -[LearnedHRNRNetworkPreStage copyEv0ToOutput:]
+ -[LearnedHRNRNetworkPreStage initWithMetal:error:]
+ -[LearnedHRNRNetworkPreStage initWithMetal:error:].cold.1
+ -[LearnedHRNRNetworkPreStage initWithMetal:error:].cold.2
+ -[LearnedHRNRNetworkPreStage initWithMetal:error:].cold.3
+ -[LearnedHRNRNetworkPreStage initWithMetal:error:].cold.4
+ -[LearnedHRNRNetworkPreStage initWithMetal:error:].cold.5
+ -[LearnedHRNRNetworkPreStage input]
+ -[LearnedHRNRNetworkPreStage processTilePipelineStage:]
+ -[LearnedHRNRNetworkPreStage processTilePipelineStage:].cold.1
+ -[LearnedHRNRNetworkPreStage processTilePipelineStage:].cold.2
+ -[LearnedHRNRNetworkPreStage setInput:]
+ -[LearnedHRNRNetworkPreStage setSharedParameters:]
+ -[LearnedHRNRNetworkPreStage sharedParameters]
+ -[LearnedHRNRNetworkPreStageInput .cxx_destruct]
+ -[LearnedHRNRNetworkPreStageInput bayerPattern]
+ -[LearnedHRNRNetworkPreStageInput ev0Metadata]
+ -[LearnedHRNRNetworkPreStageInput ev0ToEvmHomography]
+ -[LearnedHRNRNetworkPreStageInput ev0]
+ -[LearnedHRNRNetworkPreStageInput evmMetadata]
+ -[LearnedHRNRNetworkPreStageInput evm]
+ -[LearnedHRNRNetworkPreStageInput hdrMask]
+ -[LearnedHRNRNetworkPreStageInput setBayerPattern:]
+ -[LearnedHRNRNetworkPreStageInput setEv0:]
+ -[LearnedHRNRNetworkPreStageInput setEv0Metadata:]
+ -[LearnedHRNRNetworkPreStageInput setEv0ToEvmHomography:]
+ -[LearnedHRNRNetworkPreStageInput setEvm:]
+ -[LearnedHRNRNetworkPreStageInput setEvmMetadata:]
+ -[LearnedHRNRNetworkPreStageInput setHdrMask:]
+ -[LearnedHRNRNetworkPreStageInput setTileIndicesToRun:]
+ -[LearnedHRNRNetworkPreStageInput tileIndicesToRun]
+ -[LearnedHRNRNetworkSharedParameters initWithTileWidth:tileHeight:tileOverlap:]
+ -[LearnedHRNRNetworkSharedParameters numberOfTilesForHeight:]
+ -[LearnedHRNRNetworkSharedParameters numberOfTilesForWidth:]
+ -[LearnedHRNRNetworkSharedParameters setTileHeight:]
+ -[LearnedHRNRNetworkSharedParameters setTileOverlap:]
+ -[LearnedHRNRNetworkSharedParameters setTileWidth:]
+ -[LearnedHRNRNetworkSharedParameters tileHeight]
+ -[LearnedHRNRNetworkSharedParameters tileOverlap]
+ -[LearnedHRNRNetworkSharedParameters tileStepHeight]
+ -[LearnedHRNRNetworkSharedParameters tileStepWidth]
+ -[LearnedHRNRNetworkSharedParameters tileWidth]
+ -[LearnedHRNRNetworkStage .cxx_destruct]
+ -[LearnedHRNRNetworkStage _reloadNetworkForQuadra:]
+ -[LearnedHRNRNetworkStage _reloadNetworkForQuadra:].cold.1
+ -[LearnedHRNRNetworkStage _reloadNetworkForQuadra:].cold.2
+ -[LearnedHRNRNetworkStage computeTileScheduleAsyncForEv0:error:]
+ -[LearnedHRNRNetworkStage computeTileScheduleAsyncForEv0:error:].cold.1
+ -[LearnedHRNRNetworkStage initWithMetalContext:config:error:]
+ -[LearnedHRNRNetworkStage initWithMetalContext:config:error:].cold.1
+ -[LearnedHRNRNetworkStage initWithMetalContext:config:error:].cold.2
+ -[LearnedHRNRNetworkStage initWithMetalContext:config:error:].cold.3
+ -[LearnedHRNRNetworkStage initWithMetalContext:config:error:].cold.4
+ -[LearnedHRNRNetworkStage initWithMetalContext:config:error:].cold.5
+ -[LearnedHRNRNetworkStage runLearnedHRNROnEv0:evm:tileSchedule:error:executionStatus:completion:]
+ -[LearnedHRNRPlist .cxx_destruct]
+ -[LearnedHRNRProcessor .cxx_destruct]
+ -[LearnedHRNRProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:]
+ -[LearnedHRNRProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.1
+ -[LearnedHRNRProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.2
+ -[LearnedHRNRProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.3
+ -[LearnedHRNRProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.4
+ -[LearnedHRNRProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.5
+ -[LearnedHRNRProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:].cold.6
+ -[LearnedHRNRProcessor _isGainMapSupported]
+ -[LearnedHRNRProcessor _isSemanticStylesSupported]
+ -[LearnedHRNRProcessor _prepareOutputMetadata:]
+ -[LearnedHRNRProcessor _prepareOutputMetadata:].cold.1
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:]
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.1
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.2
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.3
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.4
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.5
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.6
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.7
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.8
+ -[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:].cold.9
+ -[LearnedHRNRProcessor addFrame:]
+ -[LearnedHRNRProcessor addFrame:].cold.1
+ -[LearnedHRNRProcessor addFrame:].cold.2
+ -[LearnedHRNRProcessor addFrame:].cold.3
+ -[LearnedHRNRProcessor addFrame:].cold.4
+ -[LearnedHRNRProcessor addFrame:].cold.5
+ -[LearnedHRNRProcessor addInputResource:]
+ -[LearnedHRNRProcessor addInputResource:].cold.1
+ -[LearnedHRNRProcessor addInputResource:].cold.2
+ -[LearnedHRNRProcessor addInputResource:].cold.3
+ -[LearnedHRNRProcessor addInputResource:].cold.4
+ -[LearnedHRNRProcessor addInputResource:].cold.5
+ -[LearnedHRNRProcessor addInputResource:].cold.6
+ -[LearnedHRNRProcessor addToSidecar:forKey:]
+ -[LearnedHRNRProcessor allocatorBackend]
+ -[LearnedHRNRProcessor applyOverrides]
+ -[LearnedHRNRProcessor batchCount]
+ -[LearnedHRNRProcessor bindResourcesForProcessingType:prepareDescriptor:]
+ -[LearnedHRNRProcessor bindResourcesForProcessingType:prepareDescriptor:].cold.1
+ -[LearnedHRNRProcessor bindResourcesForProcessingType:prepareDescriptor:].cold.2
+ -[LearnedHRNRProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:]
+ -[LearnedHRNRProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:].cold.1
+ -[LearnedHRNRProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:].cold.2
+ -[LearnedHRNRProcessor cameraInfoByPortType]
+ -[LearnedHRNRProcessor checkNetworkStatusWithLabel:statusGroup:status:]
+ -[LearnedHRNRProcessor cntBracketSampleBuffers]
+ -[LearnedHRNRProcessor dealloc]
+ -[LearnedHRNRProcessor defringingTuningByPortType]
+ -[LearnedHRNRProcessor delegate]
+ -[LearnedHRNRProcessor description]
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:]
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.1
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.2
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.3
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:].cold.4
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:]
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.1
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.2
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.3
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.4
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.5
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.6
+ -[LearnedHRNRProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:].cold.7
+ -[LearnedHRNRProcessor doRedFaceFix]
+ -[LearnedHRNRProcessor enableGreenGhostMitigation]
+ -[LearnedHRNRProcessor finishProcessing]
+ -[LearnedHRNRProcessor finishScheduling]
+ -[LearnedHRNRProcessor generateGainMapIfNeeded]
+ -[LearnedHRNRProcessor generateGainMapIfNeeded].cold.1
+ -[LearnedHRNRProcessor generateGainMapIfNeeded].cold.2
+ -[LearnedHRNRProcessor generateGainMapIfNeeded].cold.3
+ -[LearnedHRNRProcessor generateGainMapIfNeeded].cold.4
+ -[LearnedHRNRProcessor initWithCommandQueue:]
+ -[LearnedHRNRProcessor maximumNumberOfReferenceFrameCandidatesToHoldForProcessing]
+ -[LearnedHRNRProcessor metalCommandQueue]
+ -[LearnedHRNRProcessor output]
+ -[LearnedHRNRProcessor prepareToProcess:]
+ -[LearnedHRNRProcessor prepareToProcess:prepareDescriptor:]
+ -[LearnedHRNRProcessor prepareToProcess:prepareDescriptor:].cold.1
+ -[LearnedHRNRProcessor prepareToProcess:prepareDescriptor:].cold.2
+ -[LearnedHRNRProcessor prepareToProcess:prepareDescriptor:].cold.3
+ -[LearnedHRNRProcessor prepareToProcess:prepareDescriptor:].cold.4
+ -[LearnedHRNRProcessor prewarmWithTuningParameters:]
+ -[LearnedHRNRProcessor prewarm]
+ -[LearnedHRNRProcessor prewarm].cold.1
+ -[LearnedHRNRProcessor prewarm].cold.2
+ -[LearnedHRNRProcessor process]
+ -[LearnedHRNRProcessor process].cold.1
+ -[LearnedHRNRProcessor process].cold.2
+ -[LearnedHRNRProcessor process].cold.3
+ -[LearnedHRNRProcessor process].cold.4
+ -[LearnedHRNRProcessor process].cold.5
+ -[LearnedHRNRProcessor processingType]
+ -[LearnedHRNRProcessor purgeResources]
+ -[LearnedHRNRProcessor referenceFrameCandidatesCount]
+ -[LearnedHRNRProcessor referenceFrameHasEVMinus]
+ -[LearnedHRNRProcessor referenceFrameIndex]
+ -[LearnedHRNRProcessor regWarpInput]
+ -[LearnedHRNRProcessor reportFusionReferenceFrame:]
+ -[LearnedHRNRProcessor resetInternalState]
+ -[LearnedHRNRProcessor resetState]
+ -[LearnedHRNRProcessor runDemosaicWithInputRawTex:outputImage:frame:completion:]
+ -[LearnedHRNRProcessor runDetectors]
+ -[LearnedHRNRProcessor runPipeline]
+ -[LearnedHRNRProcessor runSemanticInferences]
+ -[LearnedHRNRProcessor runSemanticInferences].cold.1
+ -[LearnedHRNRProcessor runSemanticInferences].cold.2
+ -[LearnedHRNRProcessor runSemanticInferences].cold.3
+ -[LearnedHRNRProcessor runSemanticInferences].cold.4
+ -[LearnedHRNRProcessor semanticStyleProperties]
+ -[LearnedHRNRProcessor setAllocatorBackend:]
+ -[LearnedHRNRProcessor setCameraInfoByPortType:]
+ -[LearnedHRNRProcessor setDefringingTuningByPortType:]
+ -[LearnedHRNRProcessor setDelegate:]
+ -[LearnedHRNRProcessor setDoRedFaceFix:]
+ -[LearnedHRNRProcessor setEnableGreenGhostMitigation:]
+ -[LearnedHRNRProcessor setFusionMode:]
+ -[LearnedHRNRProcessor setLinearOutputMetadata:]
+ -[LearnedHRNRProcessor setLinearOutputMetadata:].cold.1
+ -[LearnedHRNRProcessor setLinearOutputMetadata:].cold.2
+ -[LearnedHRNRProcessor setMaximumNumberOfReferenceFrameCandidatesToHoldForProcessing:]
+ -[LearnedHRNRProcessor setMetalCommandQueue:]
+ -[LearnedHRNRProcessor setOutput:]
+ -[LearnedHRNRProcessor setProcessingType:]
+ -[LearnedHRNRProcessor setReferenceFrameCandidatesCount:]
+ -[LearnedHRNRProcessor setReferenceFrameHasEVMinus:]
+ -[LearnedHRNRProcessor setReferenceFrameIndex:]
+ -[LearnedHRNRProcessor setRegWarpInput:]
+ -[LearnedHRNRProcessor setSemanticStyleProperties:]
+ -[LearnedHRNRProcessor setSharedRegWarpBuffer:]
+ -[LearnedHRNRProcessor setSkipDenoising:]
+ -[LearnedHRNRProcessor setSrlEnabled:]
+ -[LearnedHRNRProcessor setTuningParameters:]
+ -[LearnedHRNRProcessor setTuningParams:]
+ -[LearnedHRNRProcessor setTuningParamsPlist:]
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:]
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.1
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.10
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.11
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.12
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.2
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.3
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.4
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.5
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.6
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.7
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.8
+ -[LearnedHRNRProcessor setupWithOptions:nrfConfig:].cold.9
+ -[LearnedHRNRProcessor setup]
+ -[LearnedHRNRProcessor sharedRegWarpBuffer]
+ -[LearnedHRNRProcessor skipDenoising]
+ -[LearnedHRNRProcessor srlEnabled]
+ -[LearnedHRNRProcessor supportsInputPixelFormat:]
+ -[LearnedHRNRProcessor supportsInputPixelFormat:].cold.1
+ -[LearnedHRNRProcessor supportsInputPixelFormat:].cold.2
+ -[LearnedHRNRProcessor tuningParameters]
+ -[LearnedHRNRProcessor tuningParamsPlist]
+ -[LearnedHRNRProcessor tuningParams]
+ -[LearnedHRNRProcessor(Tuning) prepareTuning:]
+ -[LearnedHRNRProcessor(Tuning) prepareTuning:].cold.1
+ -[LearnedHRNRProcessor(Tuning) prepareTuning:].cold.2
+ -[LearnedHRNRProcessor(Tuning) prepareTuning:].cold.3
+ -[LearnedHRNRProcessor(Tuning) prepareTuning:].cold.4
+ -[LearnedHRNRTileScheduler .cxx_destruct]
+ -[LearnedHRNRTileScheduler _computeHdrMaskForEv0:hdrMask:onCommandBuffer:]
+ -[LearnedHRNRTileScheduler initWithMetalContext:error:]
+ -[LearnedHRNRTileScheduler initWithMetalContext:error:].cold.1
+ -[LearnedHRNRTileScheduler initWithMetalContext:error:].cold.2
+ -[LearnedHRNRTileScheduler initWithMetalContext:error:].cold.3
+ -[LearnedHRNRTileScheduler initWithMetalContext:error:].cold.4
+ -[LearnedHRNRTileScheduler initWithMetalContext:error:].cold.5
+ -[LearnedHRNRTileScheduler runOnEv0:sharedParameters:hdrMask:error:]
+ -[LearnedHRNRTileScheduler runOnEv0:sharedParameters:hdrMask:error:].cold.1
+ -[NRFProcessorV4 setupWithOptions:].cold.14
+ -[NRFProcessorV4 setupWithOptions:].cold.15
+ -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.26
+ -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.27
+ GCC_except_table27
+ GCC_except_table51
+ _OBJC_CLASS_$_CMIFuture
+ _OBJC_CLASS_$_LearnedDemosaicNetworkPostANEStage
+ _OBJC_CLASS_$_LearnedDemosaicNetworkPreANEStage
+ _OBJC_CLASS_$_LearnedDemosaicNetworkShared
+ _OBJC_CLASS_$_LearnedDemosaicNetworkStage
+ _OBJC_CLASS_$_LearnedDemosaicNetworkStageBase
+ _OBJC_CLASS_$_LearnedDemosaicNetworkTuningParams
+ _OBJC_CLASS_$_LearnedFusionBoundInferenceResults
+ _OBJC_CLASS_$_LearnedFusionChromaSuppression
+ _OBJC_CLASS_$_LearnedFusionChromaSuppressionTuningParams
+ _OBJC_CLASS_$_LearnedFusionConfig
+ _OBJC_CLASS_$_LearnedFusionDeghostingMitigation
+ _OBJC_CLASS_$_LearnedFusionDeghostingMitigationTuningParams
+ _OBJC_CLASS_$_LearnedFusionHighlightMitigation
+ _OBJC_CLASS_$_LearnedFusionNetworkParameters
+ _OBJC_CLASS_$_LearnedFusionNetworkPostANEStage
+ _OBJC_CLASS_$_LearnedFusionNetworkPreANEStage
+ _OBJC_CLASS_$_LearnedFusionNetworkStage
+ _OBJC_CLASS_$_LearnedFusionNetworkStageShared
+ _OBJC_CLASS_$_LearnedFusionNetworkTuningParams
+ _OBJC_CLASS_$_LearnedFusionProcessingOptions
+ _OBJC_CLASS_$_LearnedFusionProcessor
+ _OBJC_CLASS_$_LearnedHRNRBoundInferenceResults
+ _OBJC_CLASS_$_LearnedHRNRNetworkConfig
+ _OBJC_CLASS_$_LearnedHRNRNetworkPostStage
+ _OBJC_CLASS_$_LearnedHRNRNetworkPostStageOutput
+ _OBJC_CLASS_$_LearnedHRNRNetworkPreStage
+ _OBJC_CLASS_$_LearnedHRNRNetworkPreStageInput
+ _OBJC_CLASS_$_LearnedHRNRNetworkSharedParameters
+ _OBJC_CLASS_$_LearnedHRNRNetworkStage
+ _OBJC_CLASS_$_LearnedHRNRPlist
+ _OBJC_CLASS_$_LearnedHRNRProcessor
+ _OBJC_CLASS_$_LearnedHRNRTileScheduler
+ _OBJC_CLASS_$_MTLCommandQueueDescriptor
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_IVAR_$_LearnedDemosaicNetworkPostANEStage._consts
+ _OBJC_IVAR_$_LearnedDemosaicNetworkPostANEStage._outputDemosaicRgbTexture
+ _OBJC_IVAR_$_LearnedDemosaicNetworkPostANEStage._writeDemosaicedTileToFullImage
+ _OBJC_IVAR_$_LearnedDemosaicNetworkPreANEStage._readInputTileFromQuadraImage
+ _OBJC_IVAR_$_LearnedDemosaicNetworkShared._demosaicNetworkParameters
+ _OBJC_IVAR_$_LearnedDemosaicNetworkShared._inputLSCGainsTexture
+ _OBJC_IVAR_$_LearnedDemosaicNetworkShared._inputRawTexture
+ _OBJC_IVAR_$_LearnedDemosaicNetworkShared._isQuadra
+ _OBJC_IVAR_$_LearnedDemosaicNetworkShared._metal
+ _OBJC_IVAR_$_LearnedDemosaicNetworkShared._numTiles
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._cameraInfoByPortType
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._hasBeenConfigured
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._metal
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._postStage
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._preStage
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._processingOptions
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._shared
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._tiledInferenceProcessor
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStage._tuningParams
+ _OBJC_IVAR_$_LearnedDemosaicNetworkStageBase._shared
+ _OBJC_IVAR_$_LearnedDemosaicNetworkTuningParams.ev0Tuning
+ _OBJC_IVAR_$_LearnedDemosaicNetworkTuningParams.evmTuning
+ _OBJC_IVAR_$_LearnedDemosaicNetworkTuningParams.longTuning
+ _OBJC_IVAR_$_LearnedDemosaicNetworkTuningParams.referenceEv0Tuning
+ _OBJC_IVAR_$_LearnedFusionBoundInferenceResults._instanceMasks
+ _OBJC_IVAR_$_LearnedFusionBoundInferenceResults._personMask
+ _OBJC_IVAR_$_LearnedFusionBoundInferenceResults._skinMask
+ _OBJC_IVAR_$_LearnedFusionBoundInferenceResults._skyMask
+ _OBJC_IVAR_$_LearnedFusionChromaSuppression._lfChromaSuppressionTuningParams
+ _OBJC_IVAR_$_LearnedFusionChromaSuppression._metal
+ _OBJC_IVAR_$_LearnedFusionChromaSuppression._stageMetal
+ _OBJC_IVAR_$_LearnedFusionChromaSuppressionTuningParams._chromaSuppressionEnabled
+ _OBJC_IVAR_$_LearnedFusionChromaSuppressionTuningParams._postDemosaicTuningParams
+ _OBJC_IVAR_$_LearnedFusionConfig._detectorsOutput
+ _OBJC_IVAR_$_LearnedFusionConfig._ev0Frame
+ _OBJC_IVAR_$_LearnedFusionConfig._hasEVM
+ _OBJC_IVAR_$_LearnedFusionConfig._inputFrames
+ _OBJC_IVAR_$_LearnedFusionConfig._longFrame
+ _OBJC_IVAR_$_LearnedFusionConfig._ltmMetadata
+ _OBJC_IVAR_$_LearnedFusionConfig._mainFrame
+ _OBJC_IVAR_$_LearnedFusionConfig._runDetectors
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._ev0Frame
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._ev0FrameExposureParameters
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._ev0ModulationMap
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._hasEv0Frame
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._hasLongFrame
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._hasMainFrame
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._longFrame
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._longFrameExposureParameters
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._longModulationMap
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._mainFrame
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._mainFrameExposureParameters
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._metal
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._shaders
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigation._tuningParams
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigationTuningParams.decayRateTuning
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigationTuningParams.lumaCutoffTuning
+ _OBJC_IVAR_$_LearnedFusionDeghostingMitigationTuningParams.lumaEdgeCutoffTuning
+ _OBJC_IVAR_$_LearnedFusionHighlightMitigation._metal
+ _OBJC_IVAR_$_LearnedFusionHighlightMitigation._shaders
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._applyDeghostingModulationForEv0LongNoises
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._ev0DeghostingModulationMap
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._ev0Exposure
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._ev0RgbTex
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._ev0TuningParams
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._evmExposure
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._evmRawBayerPattern
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._evmRawTex
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._evmRgbTex
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._evmTuningParams
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._lensShading
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._lensShadingParams
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._longDeghostingModulationMap
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._longExposure
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._longRgbTex
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._longTuningParams
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._personMaskTex
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._skinMaskTex
+ _OBJC_IVAR_$_LearnedFusionNetworkParameters._skyMaskTex
+ _OBJC_IVAR_$_LearnedFusionNetworkPostANEStage._consts
+ _OBJC_IVAR_$_LearnedFusionNetworkPostANEStage._postApplyLumaAddbackNetwork
+ _OBJC_IVAR_$_LearnedFusionNetworkPostANEStage._postCalcLumaAddbackNetwork
+ _OBJC_IVAR_$_LearnedFusionNetworkPostANEStage._shared
+ _OBJC_IVAR_$_LearnedFusionNetworkPreANEStage._consts
+ _OBJC_IVAR_$_LearnedFusionNetworkPreANEStage._preNetwork
+ _OBJC_IVAR_$_LearnedFusionNetworkPreANEStage._shared
+ _OBJC_IVAR_$_LearnedFusionNetworkStage._postFusionStage
+ _OBJC_IVAR_$_LearnedFusionNetworkStage._preFusionStage
+ _OBJC_IVAR_$_LearnedFusionNetworkStage._processor
+ _OBJC_IVAR_$_LearnedFusionNetworkStage._shared
+ _OBJC_IVAR_$_LearnedFusionNetworkStage._tuningParams
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._ev0DeghostingModulationMap
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._inputLensShading
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._inputRawEvm
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._inputRgbEv0
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._inputRgbEvm
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._inputRgbLong
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._longDeghostingModulationMap
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._metal
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._numTiles
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._outputChroma
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._outputLuma
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._personMaskTex
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._skinMaskTex
+ _OBJC_IVAR_$_LearnedFusionNetworkStageShared._skyMaskTex
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.ev0Tuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.evmTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.longTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.lumaAddBackBand0Tuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.lumaAddBackClipToSNRTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.lumaAddBackLSCModulationTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.lumaAddBackMaxNoiseFactorTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.lumaAddBackPersonSlopeTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.lumaAddBackPowerDenomNoiseFactorTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.lumaAddBackSkinSlopeTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.lumaAddBackSkySlopeTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.lumaAddBackTuning
+ _OBJC_IVAR_$_LearnedFusionNetworkTuningParams.referenceEv0Tuning
+ _OBJC_IVAR_$_LearnedFusionProcessingOptions._demosaicedImageHasHRGainApplied
+ _OBJC_IVAR_$_LearnedFusionProcessingOptions._demosaicedImageHasLSCApplied
+ _OBJC_IVAR_$_LearnedFusionProcessor._addFrameCount
+ _OBJC_IVAR_$_LearnedFusionProcessor._allocatorBackend
+ _OBJC_IVAR_$_LearnedFusionProcessor._allocatorSetupComplete
+ _OBJC_IVAR_$_LearnedFusionProcessor._batchCount
+ _OBJC_IVAR_$_LearnedFusionProcessor._cameraInfoByPortType
+ _OBJC_IVAR_$_LearnedFusionProcessor._cntBracketSampleBuffers
+ _OBJC_IVAR_$_LearnedFusionProcessor._colorConvertStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._compressionLevel
+ _OBJC_IVAR_$_LearnedFusionProcessor._defringingTuningByPortType
+ _OBJC_IVAR_$_LearnedFusionProcessor._delegate
+ _OBJC_IVAR_$_LearnedFusionProcessor._demosaicProcessingOptions
+ _OBJC_IVAR_$_LearnedFusionProcessor._demosaicStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._denoiseBoostMap
+ _OBJC_IVAR_$_LearnedFusionProcessor._doRedFaceFix
+ _OBJC_IVAR_$_LearnedFusionProcessor._enableGreenGhostMitigation
+ _OBJC_IVAR_$_LearnedFusionProcessor._flickerDetection
+ _OBJC_IVAR_$_LearnedFusionProcessor._fusionConfig
+ _OBJC_IVAR_$_LearnedFusionProcessor._gainMapStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._grayGhostDetection
+ _OBJC_IVAR_$_LearnedFusionProcessor._inputFrames
+ _OBJC_IVAR_$_LearnedFusionProcessor._isShaderHarvesting
+ _OBJC_IVAR_$_LearnedFusionProcessor._lastHeight
+ _OBJC_IVAR_$_LearnedFusionProcessor._lastPixelFormat
+ _OBJC_IVAR_$_LearnedFusionProcessor._lastWidth
+ _OBJC_IVAR_$_LearnedFusionProcessor._learnedDesmosaicStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._learnedFusionChromaSuppressionStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._learnedFusionDeghostingMitigationStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._learnedFusionHighlightMitigationStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._learnedFusionNetworkStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._lscGainsPlist
+ _OBJC_IVAR_$_LearnedFusionProcessor._lscGainsTex
+ _OBJC_IVAR_$_LearnedFusionProcessor._maximumNumberOfReferenceFrameCandidatesToHoldForProcessing
+ _OBJC_IVAR_$_LearnedFusionProcessor._metal
+ _OBJC_IVAR_$_LearnedFusionProcessor._metalCommandQueue
+ _OBJC_IVAR_$_LearnedFusionProcessor._motionDetection
+ _OBJC_IVAR_$_LearnedFusionProcessor._nrfConfig
+ _OBJC_IVAR_$_LearnedFusionProcessor._nrfPlist
+ _OBJC_IVAR_$_LearnedFusionProcessor._output
+ _OBJC_IVAR_$_LearnedFusionProcessor._post
+ _OBJC_IVAR_$_LearnedFusionProcessor._processingType
+ _OBJC_IVAR_$_LearnedFusionProcessor._processorOutput
+ _OBJC_IVAR_$_LearnedFusionProcessor._processorOutputGainMapHeadroom
+ _OBJC_IVAR_$_LearnedFusionProcessor._rawDFCommon
+ _OBJC_IVAR_$_LearnedFusionProcessor._rawDFDetectors
+ _OBJC_IVAR_$_LearnedFusionProcessor._rawDFDownsampleStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._rawDFInferenceGen
+ _OBJC_IVAR_$_LearnedFusionProcessor._referenceFrameCandidatesCount
+ _OBJC_IVAR_$_LearnedFusionProcessor._referenceFrameHasEVMinus
+ _OBJC_IVAR_$_LearnedFusionProcessor._referenceFrameIndex
+ _OBJC_IVAR_$_LearnedFusionProcessor._regWarpApplyGDC
+ _OBJC_IVAR_$_LearnedFusionProcessor._regWarpInput
+ _OBJC_IVAR_$_LearnedFusionProcessor._registrationPipelineRWPP
+ _OBJC_IVAR_$_LearnedFusionProcessor._registrationPipelineRWPPConfig
+ _OBJC_IVAR_$_LearnedFusionProcessor._regwarpHasBeenSetup
+ _OBJC_IVAR_$_LearnedFusionProcessor._requestTuningParams
+ _OBJC_IVAR_$_LearnedFusionProcessor._semanticStyleProperties
+ _OBJC_IVAR_$_LearnedFusionProcessor._sharedMetalBuffer
+ _OBJC_IVAR_$_LearnedFusionProcessor._sharedRegWarpBuffer
+ _OBJC_IVAR_$_LearnedFusionProcessor._sidecar
+ _OBJC_IVAR_$_LearnedFusionProcessor._skipDenoising
+ _OBJC_IVAR_$_LearnedFusionProcessor._softLTMStage
+ _OBJC_IVAR_$_LearnedFusionProcessor._srlEnabled
+ _OBJC_IVAR_$_LearnedFusionProcessor._tuningParameters
+ _OBJC_IVAR_$_LearnedFusionProcessor._tuningParams
+ _OBJC_IVAR_$_LearnedFusionProcessor._tuningParamsPlist
+ _OBJC_IVAR_$_LearnedFusionProcessor._usingExternalSharedMetalBuffer
+ _OBJC_IVAR_$_LearnedFusionProcessor._warpStage
+ _OBJC_IVAR_$_LearnedHRNRBoundInferenceResults._instanceMasks
+ _OBJC_IVAR_$_LearnedHRNRBoundInferenceResults._personMask
+ _OBJC_IVAR_$_LearnedHRNRBoundInferenceResults._skinMask
+ _OBJC_IVAR_$_LearnedHRNRBoundInferenceResults._skyMask
+ _OBJC_IVAR_$_LearnedHRNRNetworkConfig._deviceGeneration
+ _OBJC_IVAR_$_LearnedHRNRNetworkConfig._isQuadra
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStage._copyBayerTileOut
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStage._copyQuadraTileOut
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStage._metal
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStage._output
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStage._quadraInputs
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStage._sharedParameters
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStage._tileCount
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStageOutput._bayerPattern
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStageOutput._output
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStageOutput._outputGainRatio
+ _OBJC_IVAR_$_LearnedHRNRNetworkPostStageOutput._tileIndicesToRun
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._copyBayerTileIn
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._copyHdrMask
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._copyQuadraTileIn
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._copyWithGain
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._createWarpField
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._ev0EvmHomography
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._gainRatioFloat
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._input
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._metal
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._quadraInputs
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._sharedParameters
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStage._tileCount
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStageInput._bayerPattern
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStageInput._ev0
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStageInput._ev0Metadata
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStageInput._ev0ToEvmHomography
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStageInput._evm
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStageInput._evmMetadata
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStageInput._hdrMask
+ _OBJC_IVAR_$_LearnedHRNRNetworkPreStageInput._tileIndicesToRun
+ _OBJC_IVAR_$_LearnedHRNRNetworkSharedParameters._tileHeight
+ _OBJC_IVAR_$_LearnedHRNRNetworkSharedParameters._tileOverlap
+ _OBJC_IVAR_$_LearnedHRNRNetworkSharedParameters._tileWidth
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._crossQueueEvent
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._crossQueueEventValue
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._forQuadra
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._hdrMask
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._learnedHRNRPostStage
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._learnedHRNRPreStage
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._learnedHRNRTileScheduler
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._learnedHRNRTiledInferenceProcessor
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._lowLatencyMetal
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._networkSetupIsComplete
+ _OBJC_IVAR_$_LearnedHRNRNetworkStage._parentQueue
+ _OBJC_IVAR_$_LearnedHRNRPlist.defringingTuningParameters
+ _OBJC_IVAR_$_LearnedHRNRPlist.denoiseAndSharpening
+ _OBJC_IVAR_$_LearnedHRNRPlist.gainMap
+ _OBJC_IVAR_$_LearnedHRNRPlist.greenGhostBrightLightTuning
+ _OBJC_IVAR_$_LearnedHRNRPlist.miwbPlist
+ _OBJC_IVAR_$_LearnedHRNRPlist.noiseModel
+ _OBJC_IVAR_$_LearnedHRNRPlist.outputNoiseModel
+ _OBJC_IVAR_$_LearnedHRNRPlist.qdemTuning
+ _OBJC_IVAR_$_LearnedHRNRPlist.semanticStyles
+ _OBJC_IVAR_$_LearnedHRNRPlist.toneMapping
+ _OBJC_IVAR_$_LearnedHRNRPlist.zimmerDEMTuning
+ _OBJC_IVAR_$_LearnedHRNRProcessor._addFrameCount
+ _OBJC_IVAR_$_LearnedHRNRProcessor._allocatorBackend
+ _OBJC_IVAR_$_LearnedHRNRProcessor._allocatorSetupComplete
+ _OBJC_IVAR_$_LearnedHRNRProcessor._batchCount
+ _OBJC_IVAR_$_LearnedHRNRProcessor._cameraInfoByPortType
+ _OBJC_IVAR_$_LearnedHRNRProcessor._cntBracketSampleBuffers
+ _OBJC_IVAR_$_LearnedHRNRProcessor._colorConvertStage
+ _OBJC_IVAR_$_LearnedHRNRProcessor._compressionLevel
+ _OBJC_IVAR_$_LearnedHRNRProcessor._defringingTuningByPortType
+ _OBJC_IVAR_$_LearnedHRNRProcessor._delegate
+ _OBJC_IVAR_$_LearnedHRNRProcessor._demosaicStage
+ _OBJC_IVAR_$_LearnedHRNRProcessor._doRedFaceFix
+ _OBJC_IVAR_$_LearnedHRNRProcessor._draftDemosaicStage
+ _OBJC_IVAR_$_LearnedHRNRProcessor._enableGreenGhostMitigation
+ _OBJC_IVAR_$_LearnedHRNRProcessor._flickerDetection
+ _OBJC_IVAR_$_LearnedHRNRProcessor._fusionMode
+ _OBJC_IVAR_$_LearnedHRNRProcessor._gainMapStage
+ _OBJC_IVAR_$_LearnedHRNRProcessor._grayGhostDetection
+ _OBJC_IVAR_$_LearnedHRNRProcessor._inputFrames
+ _OBJC_IVAR_$_LearnedHRNRProcessor._isShaderHarvesting
+ _OBJC_IVAR_$_LearnedHRNRProcessor._lastHeight
+ _OBJC_IVAR_$_LearnedHRNRProcessor._lastPixelFormat
+ _OBJC_IVAR_$_LearnedHRNRProcessor._lastWidth
+ _OBJC_IVAR_$_LearnedHRNRProcessor._learnedHRNRNetworkStage
+ _OBJC_IVAR_$_LearnedHRNRProcessor._learnedHRNRTileSchedule
+ _OBJC_IVAR_$_LearnedHRNRProcessor._learnedNRNetworkStage
+ _OBJC_IVAR_$_LearnedHRNRProcessor._lscGainsPlist
+ _OBJC_IVAR_$_LearnedHRNRProcessor._lscGainsTex
+ _OBJC_IVAR_$_LearnedHRNRProcessor._maximumNumberOfReferenceFrameCandidatesToHoldForProcessing
+ _OBJC_IVAR_$_LearnedHRNRProcessor._metal
+ _OBJC_IVAR_$_LearnedHRNRProcessor._metalCommandQueue
+ _OBJC_IVAR_$_LearnedHRNRProcessor._motionDetection
+ _OBJC_IVAR_$_LearnedHRNRProcessor._nrfConfig
+ _OBJC_IVAR_$_LearnedHRNRProcessor._nrfPlist
+ _OBJC_IVAR_$_LearnedHRNRProcessor._output
+ _OBJC_IVAR_$_LearnedHRNRProcessor._post
+ _OBJC_IVAR_$_LearnedHRNRProcessor._processingType
+ _OBJC_IVAR_$_LearnedHRNRProcessor._processorOutput
+ _OBJC_IVAR_$_LearnedHRNRProcessor._processorOutputGainMapHeadroom
+ _OBJC_IVAR_$_LearnedHRNRProcessor._rawDFCommon
+ _OBJC_IVAR_$_LearnedHRNRProcessor._rawDFDetectors
+ _OBJC_IVAR_$_LearnedHRNRProcessor._rawDFDownsampleStage
+ _OBJC_IVAR_$_LearnedHRNRProcessor._rawDFInferenceGen
+ _OBJC_IVAR_$_LearnedHRNRProcessor._referenceFrameCandidatesCount
+ _OBJC_IVAR_$_LearnedHRNRProcessor._referenceFrameHasEVMinus
+ _OBJC_IVAR_$_LearnedHRNRProcessor._referenceFrameIndex
+ _OBJC_IVAR_$_LearnedHRNRProcessor._regWarpApplyGDC
+ _OBJC_IVAR_$_LearnedHRNRProcessor._regWarpInput
+ _OBJC_IVAR_$_LearnedHRNRProcessor._registrationPipelineRWPP
+ _OBJC_IVAR_$_LearnedHRNRProcessor._registrationPipelineRWPPConfig
+ _OBJC_IVAR_$_LearnedHRNRProcessor._regwarpHasBeenSetup
+ _OBJC_IVAR_$_LearnedHRNRProcessor._requestTuningParams
+ _OBJC_IVAR_$_LearnedHRNRProcessor._semanticStyleProperties
+ _OBJC_IVAR_$_LearnedHRNRProcessor._sharedMetalBuffer
+ _OBJC_IVAR_$_LearnedHRNRProcessor._sharedRegWarpBuffer
+ _OBJC_IVAR_$_LearnedHRNRProcessor._sidecar
+ _OBJC_IVAR_$_LearnedHRNRProcessor._skipDenoising
+ _OBJC_IVAR_$_LearnedHRNRProcessor._softLTMStage
+ _OBJC_IVAR_$_LearnedHRNRProcessor._srlEnabled
+ _OBJC_IVAR_$_LearnedHRNRProcessor._tuningParameters
+ _OBJC_IVAR_$_LearnedHRNRProcessor._tuningParams
+ _OBJC_IVAR_$_LearnedHRNRProcessor._tuningParamsPlist
+ _OBJC_IVAR_$_LearnedHRNRProcessor._usingExternalSharedMetalBuffer
+ _OBJC_IVAR_$_LearnedHRNRTileScheduler._completionEvent
+ _OBJC_IVAR_$_LearnedHRNRTileScheduler._completionEventListener
+ _OBJC_IVAR_$_LearnedHRNRTileScheduler._hdrMaskV2BlurX
+ _OBJC_IVAR_$_LearnedHRNRTileScheduler._hdrMaskV2BlurYAndSoftThreshold
+ _OBJC_IVAR_$_LearnedHRNRTileScheduler._hdrMaskV2InitialMask
+ _OBJC_IVAR_$_LearnedHRNRTileScheduler._metal
+ _OBJC_IVAR_$_LearnedHRNRTileScheduler._nextCompletionEventValue
+ _OBJC_IVAR_$_LearnedHRNRTileScheduler._skipTile
+ _OBJC_IVAR_$_LearnedHRNRTileScheduler._tileClipCount
+ _OBJC_IVAR_$_NRFPlist.quadraLearnedDemosaicTuning
+ _OBJC_IVAR_$_NRFPlist.quadraLearnedFusionDeghostingTuningParams
+ _OBJC_IVAR_$_NRFPlist.quadraLearnedFusionPostFusionTuning
+ _OBJC_IVAR_$_NRFPlist.quadraLearnedFusionTuning
+ _OBJC_METACLASS_$_LearnedDemosaicNetworkPostANEStage
+ _OBJC_METACLASS_$_LearnedDemosaicNetworkPreANEStage
+ _OBJC_METACLASS_$_LearnedDemosaicNetworkShared
+ _OBJC_METACLASS_$_LearnedDemosaicNetworkStage
+ _OBJC_METACLASS_$_LearnedDemosaicNetworkStageBase
+ _OBJC_METACLASS_$_LearnedDemosaicNetworkTuningParams
+ _OBJC_METACLASS_$_LearnedFusionBoundInferenceResults
+ _OBJC_METACLASS_$_LearnedFusionChromaSuppression
+ _OBJC_METACLASS_$_LearnedFusionChromaSuppressionTuningParams
+ _OBJC_METACLASS_$_LearnedFusionConfig
+ _OBJC_METACLASS_$_LearnedFusionDeghostingMitigation
+ _OBJC_METACLASS_$_LearnedFusionDeghostingMitigationTuningParams
+ _OBJC_METACLASS_$_LearnedFusionHighlightMitigation
+ _OBJC_METACLASS_$_LearnedFusionNetworkParameters
+ _OBJC_METACLASS_$_LearnedFusionNetworkPostANEStage
+ _OBJC_METACLASS_$_LearnedFusionNetworkPreANEStage
+ _OBJC_METACLASS_$_LearnedFusionNetworkStage
+ _OBJC_METACLASS_$_LearnedFusionNetworkStageShared
+ _OBJC_METACLASS_$_LearnedFusionNetworkTuningParams
+ _OBJC_METACLASS_$_LearnedFusionProcessingOptions
+ _OBJC_METACLASS_$_LearnedFusionProcessor
+ _OBJC_METACLASS_$_LearnedHRNRBoundInferenceResults
+ _OBJC_METACLASS_$_LearnedHRNRNetworkConfig
+ _OBJC_METACLASS_$_LearnedHRNRNetworkPostStage
+ _OBJC_METACLASS_$_LearnedHRNRNetworkPostStageOutput
+ _OBJC_METACLASS_$_LearnedHRNRNetworkPreStage
+ _OBJC_METACLASS_$_LearnedHRNRNetworkPreStageInput
+ _OBJC_METACLASS_$_LearnedHRNRNetworkSharedParameters
+ _OBJC_METACLASS_$_LearnedHRNRNetworkStage
+ _OBJC_METACLASS_$_LearnedHRNRPlist
+ _OBJC_METACLASS_$_LearnedHRNRProcessor
+ _OBJC_METACLASS_$_LearnedHRNRTileScheduler
+ __OBJC_$_CATEGORY_CMITiledInferenceProcessorTilePipelineStage_$_LearnedHRNR
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CMITiledInferenceProcessorTilePipelineStage_$_LearnedHRNR
+ __OBJC_$_CLASS_METHODS_LearnedDemosaicNetworkStage
+ __OBJC_$_CLASS_METHODS_LearnedFusionDeghostingMitigation
+ __OBJC_$_CLASS_METHODS_LearnedFusionHighlightMitigation
+ __OBJC_$_CLASS_METHODS_LearnedFusionNetworkStage
+ __OBJC_$_CLASS_METHODS_LearnedHRNRNetworkPostStage
+ __OBJC_$_CLASS_METHODS_LearnedHRNRNetworkPreStage
+ __OBJC_$_CLASS_METHODS_LearnedHRNRNetworkSharedParameters
+ __OBJC_$_CLASS_METHODS_LearnedHRNRNetworkStage
+ __OBJC_$_CLASS_METHODS_LearnedHRNRTileScheduler
+ __OBJC_$_INSTANCE_METHODS_LearnedDemosaicNetworkPostANEStage
+ __OBJC_$_INSTANCE_METHODS_LearnedDemosaicNetworkPreANEStage
+ __OBJC_$_INSTANCE_METHODS_LearnedDemosaicNetworkShared
+ __OBJC_$_INSTANCE_METHODS_LearnedDemosaicNetworkStage
+ __OBJC_$_INSTANCE_METHODS_LearnedDemosaicNetworkStageBase
+ __OBJC_$_INSTANCE_METHODS_LearnedDemosaicNetworkTuningParams
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionBoundInferenceResults
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionChromaSuppression
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionChromaSuppressionTuningParams
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionConfig
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionDeghostingMitigation
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionDeghostingMitigationTuningParams
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionHighlightMitigation
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionNetworkParameters
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionNetworkPostANEStage
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionNetworkPreANEStage
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionNetworkStage
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionNetworkStageShared
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionNetworkTuningParams
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionProcessingOptions
+ __OBJC_$_INSTANCE_METHODS_LearnedFusionProcessor(Tuning)
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRBoundInferenceResults
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRNetworkConfig
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRNetworkPostStage
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRNetworkPostStageOutput
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRNetworkPreStage
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRNetworkPreStageInput
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRNetworkSharedParameters
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRNetworkStage
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRPlist
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRProcessor(Tuning)
+ __OBJC_$_INSTANCE_METHODS_LearnedHRNRTileScheduler
+ __OBJC_$_INSTANCE_VARIABLES_LearnedDemosaicNetworkPostANEStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedDemosaicNetworkPreANEStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedDemosaicNetworkShared
+ __OBJC_$_INSTANCE_VARIABLES_LearnedDemosaicNetworkStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedDemosaicNetworkStageBase
+ __OBJC_$_INSTANCE_VARIABLES_LearnedDemosaicNetworkTuningParams
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionBoundInferenceResults
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionChromaSuppression
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionChromaSuppressionTuningParams
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionConfig
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionDeghostingMitigation
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionDeghostingMitigationTuningParams
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionHighlightMitigation
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionNetworkParameters
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionNetworkPostANEStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionNetworkPreANEStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionNetworkStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionNetworkStageShared
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionNetworkTuningParams
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionProcessingOptions
+ __OBJC_$_INSTANCE_VARIABLES_LearnedFusionProcessor
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRBoundInferenceResults
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRNetworkConfig
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRNetworkPostStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRNetworkPostStageOutput
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRNetworkPreStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRNetworkPreStageInput
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRNetworkSharedParameters
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRNetworkStage
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRPlist
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRProcessor
+ __OBJC_$_INSTANCE_VARIABLES_LearnedHRNRTileScheduler
+ __OBJC_$_PROP_LIST_LearnedDemosaicNetworkPostANEStage
+ __OBJC_$_PROP_LIST_LearnedDemosaicNetworkPreANEStage
+ __OBJC_$_PROP_LIST_LearnedDemosaicNetworkShared
+ __OBJC_$_PROP_LIST_LearnedDemosaicNetworkStage
+ __OBJC_$_PROP_LIST_LearnedDemosaicNetworkStageBase
+ __OBJC_$_PROP_LIST_LearnedFusionBoundInferenceResults
+ __OBJC_$_PROP_LIST_LearnedFusionChromaSuppression
+ __OBJC_$_PROP_LIST_LearnedFusionChromaSuppressionTuningParams
+ __OBJC_$_PROP_LIST_LearnedFusionConfig
+ __OBJC_$_PROP_LIST_LearnedFusionDeghostingMitigation
+ __OBJC_$_PROP_LIST_LearnedFusionNetworkParameters
+ __OBJC_$_PROP_LIST_LearnedFusionNetworkPostANEStage
+ __OBJC_$_PROP_LIST_LearnedFusionNetworkPreANEStage
+ __OBJC_$_PROP_LIST_LearnedFusionNetworkStage
+ __OBJC_$_PROP_LIST_LearnedFusionNetworkStageShared
+ __OBJC_$_PROP_LIST_LearnedFusionProcessingOptions
+ __OBJC_$_PROP_LIST_LearnedFusionProcessor
+ __OBJC_$_PROP_LIST_LearnedHRNRBoundInferenceResults
+ __OBJC_$_PROP_LIST_LearnedHRNRNetworkConfig
+ __OBJC_$_PROP_LIST_LearnedHRNRNetworkPostStage
+ __OBJC_$_PROP_LIST_LearnedHRNRNetworkPostStageOutput
+ __OBJC_$_PROP_LIST_LearnedHRNRNetworkPreStage
+ __OBJC_$_PROP_LIST_LearnedHRNRNetworkPreStageInput
+ __OBJC_$_PROP_LIST_LearnedHRNRNetworkSharedParameters
+ __OBJC_$_PROP_LIST_LearnedHRNRProcessor
+ __OBJC_$_PROTOCOL_CLASS_METHODS_Prewarmable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_Prewarmable
+ __OBJC_CLASS_PROTOCOLS_$_LearnedDemosaicNetworkPostANEStage
+ __OBJC_CLASS_PROTOCOLS_$_LearnedDemosaicNetworkPreANEStage
+ __OBJC_CLASS_PROTOCOLS_$_LearnedFusionNetworkPostANEStage
+ __OBJC_CLASS_PROTOCOLS_$_LearnedFusionNetworkPreANEStage
+ __OBJC_CLASS_PROTOCOLS_$_LearnedFusionProcessor
+ __OBJC_CLASS_PROTOCOLS_$_LearnedHRNRNetworkPostStage
+ __OBJC_CLASS_PROTOCOLS_$_LearnedHRNRNetworkPreStage
+ __OBJC_CLASS_PROTOCOLS_$_LearnedHRNRNetworkStage
+ __OBJC_CLASS_PROTOCOLS_$_LearnedHRNRProcessor
+ __OBJC_CLASS_PROTOCOLS_$_LearnedHRNRTileScheduler
+ __OBJC_CLASS_RO_$_LearnedDemosaicNetworkPostANEStage
+ __OBJC_CLASS_RO_$_LearnedDemosaicNetworkPreANEStage
+ __OBJC_CLASS_RO_$_LearnedDemosaicNetworkShared
+ __OBJC_CLASS_RO_$_LearnedDemosaicNetworkStage
+ __OBJC_CLASS_RO_$_LearnedDemosaicNetworkStageBase
+ __OBJC_CLASS_RO_$_LearnedDemosaicNetworkTuningParams
+ __OBJC_CLASS_RO_$_LearnedFusionBoundInferenceResults
+ __OBJC_CLASS_RO_$_LearnedFusionChromaSuppression
+ __OBJC_CLASS_RO_$_LearnedFusionChromaSuppressionTuningParams
+ __OBJC_CLASS_RO_$_LearnedFusionConfig
+ __OBJC_CLASS_RO_$_LearnedFusionDeghostingMitigation
+ __OBJC_CLASS_RO_$_LearnedFusionDeghostingMitigationTuningParams
+ __OBJC_CLASS_RO_$_LearnedFusionHighlightMitigation
+ __OBJC_CLASS_RO_$_LearnedFusionNetworkParameters
+ __OBJC_CLASS_RO_$_LearnedFusionNetworkPostANEStage
+ __OBJC_CLASS_RO_$_LearnedFusionNetworkPreANEStage
+ __OBJC_CLASS_RO_$_LearnedFusionNetworkStage
+ __OBJC_CLASS_RO_$_LearnedFusionNetworkStageShared
+ __OBJC_CLASS_RO_$_LearnedFusionNetworkTuningParams
+ __OBJC_CLASS_RO_$_LearnedFusionProcessingOptions
+ __OBJC_CLASS_RO_$_LearnedFusionProcessor
+ __OBJC_CLASS_RO_$_LearnedHRNRBoundInferenceResults
+ __OBJC_CLASS_RO_$_LearnedHRNRNetworkConfig
+ __OBJC_CLASS_RO_$_LearnedHRNRNetworkPostStage
+ __OBJC_CLASS_RO_$_LearnedHRNRNetworkPostStageOutput
+ __OBJC_CLASS_RO_$_LearnedHRNRNetworkPreStage
+ __OBJC_CLASS_RO_$_LearnedHRNRNetworkPreStageInput
+ __OBJC_CLASS_RO_$_LearnedHRNRNetworkSharedParameters
+ __OBJC_CLASS_RO_$_LearnedHRNRNetworkStage
+ __OBJC_CLASS_RO_$_LearnedHRNRPlist
+ __OBJC_CLASS_RO_$_LearnedHRNRProcessor
+ __OBJC_CLASS_RO_$_LearnedHRNRTileScheduler
+ __OBJC_LABEL_PROTOCOL_$_Prewarmable
+ __OBJC_METACLASS_RO_$_LearnedDemosaicNetworkPostANEStage
+ __OBJC_METACLASS_RO_$_LearnedDemosaicNetworkPreANEStage
+ __OBJC_METACLASS_RO_$_LearnedDemosaicNetworkShared
+ __OBJC_METACLASS_RO_$_LearnedDemosaicNetworkStage
+ __OBJC_METACLASS_RO_$_LearnedDemosaicNetworkStageBase
+ __OBJC_METACLASS_RO_$_LearnedDemosaicNetworkTuningParams
+ __OBJC_METACLASS_RO_$_LearnedFusionBoundInferenceResults
+ __OBJC_METACLASS_RO_$_LearnedFusionChromaSuppression
+ __OBJC_METACLASS_RO_$_LearnedFusionChromaSuppressionTuningParams
+ __OBJC_METACLASS_RO_$_LearnedFusionConfig
+ __OBJC_METACLASS_RO_$_LearnedFusionDeghostingMitigation
+ __OBJC_METACLASS_RO_$_LearnedFusionDeghostingMitigationTuningParams
+ __OBJC_METACLASS_RO_$_LearnedFusionHighlightMitigation
+ __OBJC_METACLASS_RO_$_LearnedFusionNetworkParameters
+ __OBJC_METACLASS_RO_$_LearnedFusionNetworkPostANEStage
+ __OBJC_METACLASS_RO_$_LearnedFusionNetworkPreANEStage
+ __OBJC_METACLASS_RO_$_LearnedFusionNetworkStage
+ __OBJC_METACLASS_RO_$_LearnedFusionNetworkStageShared
+ __OBJC_METACLASS_RO_$_LearnedFusionNetworkTuningParams
+ __OBJC_METACLASS_RO_$_LearnedFusionProcessingOptions
+ __OBJC_METACLASS_RO_$_LearnedFusionProcessor
+ __OBJC_METACLASS_RO_$_LearnedHRNRBoundInferenceResults
+ __OBJC_METACLASS_RO_$_LearnedHRNRNetworkConfig
+ __OBJC_METACLASS_RO_$_LearnedHRNRNetworkPostStage
+ __OBJC_METACLASS_RO_$_LearnedHRNRNetworkPostStageOutput
+ __OBJC_METACLASS_RO_$_LearnedHRNRNetworkPreStage
+ __OBJC_METACLASS_RO_$_LearnedHRNRNetworkPreStageInput
+ __OBJC_METACLASS_RO_$_LearnedHRNRNetworkSharedParameters
+ __OBJC_METACLASS_RO_$_LearnedHRNRNetworkStage
+ __OBJC_METACLASS_RO_$_LearnedHRNRPlist
+ __OBJC_METACLASS_RO_$_LearnedHRNRProcessor
+ __OBJC_METACLASS_RO_$_LearnedHRNRTileScheduler
+ __OBJC_PROTOCOL_$_Prewarmable
+ ___35-[LearnedHRNRProcessor runPipeline]_block_invoke
+ ___35-[LearnedHRNRProcessor runPipeline]_block_invoke.188
+ ___35-[LearnedHRNRProcessor runPipeline]_block_invoke.202
+ ___35-[LearnedHRNRProcessor runPipeline]_block_invoke_2
+ ___37-[LearnedFusionProcessor runPipeline]_block_invoke
+ ___37-[LearnedFusionProcessor runPipeline]_block_invoke.276
+ ___51-[LearnedHRNRProcessor reportFusionReferenceFrame:]_block_invoke
+ ___51-[LearnedHRNRProcessor reportFusionReferenceFrame:]_block_invoke_2
+ ___53-[LearnedFusionProcessor reportFusionReferenceFrame:]_block_invoke
+ ___53-[LearnedFusionProcessor reportFusionReferenceFrame:]_block_invoke_2
+ ___68-[LearnedHRNRTileScheduler runOnEv0:sharedParameters:hdrMask:error:]_block_invoke
+ ___97-[LearnedHRNRNetworkStage runLearnedHRNROnEv0:evm:tileSchedule:error:executionStatus:completion:]_block_invoke
+ ___97-[LearnedHRNRNetworkStage runLearnedHRNROnEv0:evm:tileSchedule:error:executionStatus:completion:]_block_invoke.148
+ ___97-[LearnedHRNRNetworkStage runLearnedHRNROnEv0:evm:tileSchedule:error:executionStatus:completion:]_block_invoke.153
+ ___block_descriptor_36_e28_v16?0"<MTLCommandBuffer>"8l
+ ___block_descriptor_48_e8_32s40w_e29_v24?0"<MTLSharedEvent>"8Q16lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e28_v16?0"<MTLCommandBuffer>"8ls32l8
+ ___block_descriptor_56_e8_32bs40r48r_e8_v12?0i8lr40l8r48l8s32l8
+ _getTuningForLFTypeAndMode
+ _kFigCaptureStillImageProcessingMetadataKey_DocumentScanning
+ _kNRF_SyntheticReference
+ _objc_msgSend$_computeHdrMaskForEv0:hdrMask:onCommandBuffer:
+ _objc_msgSend$_fillNoiseScaleFactors:noiseScaleFactors:gain:
+ _objc_msgSend$_getInterpolatedGainFromTuningParams:gain:
+ _objc_msgSend$_getInterpolatedGainFromTuningParams:key:gain:
+ _objc_msgSend$_getLscGainsTexAndParameters:lscGainsTex:lscGainsParameters:
+ _objc_msgSend$_projectEv0ToEvm:
+ _objc_msgSend$_reloadNetworkForQuadra:
+ _objc_msgSend$addFrame:isMainFrame:
+ _objc_msgSend$allocateAndDemosaicLTMIn:
+ _objc_msgSend$allocateIOBuffers
+ _objc_msgSend$applyDeghostingModulationForEv0LongNoises
+ _objc_msgSend$buildPyramidForFrame:withLabel:
+ _objc_msgSend$checkNetworkStatusWithLabel:statusGroup:status:
+ _objc_msgSend$computeTileScheduleAsyncForEv0:error:
+ _objc_msgSend$consts
+ _objc_msgSend$copyEv0ToOutput:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$demosaicedImageHasHRGainApplied
+ _objc_msgSend$demosaicedImageHasLSCApplied
+ _objc_msgSend$detectorsOutput
+ _objc_msgSend$ev0DeghostingModulationMap
+ _objc_msgSend$ev0Exposure
+ _objc_msgSend$ev0Frame
+ _objc_msgSend$ev0Metadata
+ _objc_msgSend$ev0RgbTex
+ _objc_msgSend$ev0ToEvmHomography
+ _objc_msgSend$ev0TuningParams
+ _objc_msgSend$evmExposure
+ _objc_msgSend$evmMetadata
+ _objc_msgSend$evmRawBayerPattern
+ _objc_msgSend$evmRawTex
+ _objc_msgSend$evmRgbTex
+ _objc_msgSend$evmTuningParams
+ _objc_msgSend$executionStatus
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$generateGainMapIfNeeded
+ _objc_msgSend$generateModulationMaps
+ _objc_msgSend$generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:
+ _objc_msgSend$getDeghostingModulationMaps:longDeghostingModulationMap:
+ _objc_msgSend$getDemosaicNetworkParameters
+ _objc_msgSend$hasAllFrames
+ _objc_msgSend$hasEVM
+ _objc_msgSend$hdrMask
+ _objc_msgSend$initLearnedHRNRWithMetalContext:forQuadra:error:
+ _objc_msgSend$initWithContext:cameraInfo:isQuadra:
+ _objc_msgSend$initWithFrames:
+ _objc_msgSend$initWithMetal:error:
+ _objc_msgSend$initWithMetalContext:config:error:
+ _objc_msgSend$initWithMetalContext:error:
+ _objc_msgSend$initWithOutputHasLSCApplied:hasHRGainApplied:
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$initWithTileWidth:tileHeight:tileOverlap:
+ _objc_msgSend$inputLensShading
+ _objc_msgSend$inputRawEvm
+ _objc_msgSend$inputRgbEv0
+ _objc_msgSend$inputRgbEvm
+ _objc_msgSend$inputRgbLong
+ _objc_msgSend$lensShading
+ _objc_msgSend$lensShadingParams
+ _objc_msgSend$longDeghostingModulationMap
+ _objc_msgSend$longExposure
+ _objc_msgSend$longRgbTex
+ _objc_msgSend$longTuningParams
+ _objc_msgSend$ltmMetadata
+ _objc_msgSend$mainFrame
+ _objc_msgSend$mitigateHighlightsWithInOutQuadraTexture:
+ _objc_msgSend$networkInputPorts
+ _objc_msgSend$newCommandQueueWithDescriptor:
+ _objc_msgSend$numberOfTilesForHeight:
+ _objc_msgSend$numberOfTilesForWidth:
+ _objc_msgSend$outputDemosaicRgbTexture
+ _objc_msgSend$outputGainRatio
+ _objc_msgSend$personMaskTex
+ _objc_msgSend$postDemosaicTuningParams
+ _objc_msgSend$postInferenceStage
+ _objc_msgSend$preInferenceStage
+ _objc_msgSend$prepareTuning:withProcessingMode:
+ _objc_msgSend$rotate180ForBayerPattern:
+ _objc_msgSend$runChromaSuppressionWithInOutFusedImage:
+ _objc_msgSend$runDemosaicWithInputRawTexture:outputRgbTexture:
+ _objc_msgSend$runDetectors
+ _objc_msgSend$runHighlightMitigation
+ _objc_msgSend$runLearnedDemosaicNetworkStage
+ _objc_msgSend$runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:
+ _objc_msgSend$runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:
+ _objc_msgSend$runLearnedHRNROnEv0:evm:tileSchedule:error:executionStatus:completion:
+ _objc_msgSend$runOnEv0:sharedParameters:hdrMask:error:
+ _objc_msgSend$runProcessor:withTileCount:
+ _objc_msgSend$runWithTileCount:withCompletionHandler:event:waitValue:signalValue:
+ _objc_msgSend$setApplyDeghostingModulationForEv0LongNoises:
+ _objc_msgSend$setBayerPattern:
+ _objc_msgSend$setDisableIOFencing:
+ _objc_msgSend$setEnableLowLatencySignalSharedEvent:
+ _objc_msgSend$setEnableLowLatencyWaitSharedEvent:
+ _objc_msgSend$setEv0:
+ _objc_msgSend$setEv0DeghostingModulationMap:
+ _objc_msgSend$setEv0Exposure:
+ _objc_msgSend$setEv0FrameExposureParameters:
+ _objc_msgSend$setEv0Metadata:
+ _objc_msgSend$setEv0ModulationMap:
+ _objc_msgSend$setEv0RgbTex:
+ _objc_msgSend$setEv0ToEvmHomography:
+ _objc_msgSend$setEv0TuningParams:
+ _objc_msgSend$setEvm:
+ _objc_msgSend$setEvmExposure:
+ _objc_msgSend$setEvmMetadata:
+ _objc_msgSend$setEvmRawBayerPattern:
+ _objc_msgSend$setEvmRawTex:
+ _objc_msgSend$setEvmRgbTex:
+ _objc_msgSend$setEvmTuningParams:
+ _objc_msgSend$setHdrMask:
+ _objc_msgSend$setInput:
+ _objc_msgSend$setInputLensShading:
+ _objc_msgSend$setInputRawEvm:
+ _objc_msgSend$setInputRgbEv0:
+ _objc_msgSend$setInputRgbEvm:
+ _objc_msgSend$setInputRgbLong:
+ _objc_msgSend$setLensShading:
+ _objc_msgSend$setLensShadingParams:
+ _objc_msgSend$setLfChromaSuppressionTuningParams:
+ _objc_msgSend$setLongDeghostingModulationMap:
+ _objc_msgSend$setLongExposure:
+ _objc_msgSend$setLongFrameExposureParameters:
+ _objc_msgSend$setLongModulationMap:
+ _objc_msgSend$setLongRgbTex:
+ _objc_msgSend$setLongTuningParams:
+ _objc_msgSend$setLtmMetadata:
+ _objc_msgSend$setMainFrameExposureParameters:
+ _objc_msgSend$setOutputDemosaicRgbTexture:
+ _objc_msgSend$setOutputGainRatio:
+ _objc_msgSend$setPersonMaskTex:
+ _objc_msgSend$setRegistrationPolicy:
+ _objc_msgSend$setSharedParameters:
+ _objc_msgSend$setSkinMaskTex:
+ _objc_msgSend$setSkyMaskTex:
+ _objc_msgSend$setTileIndicesToRun:
+ _objc_msgSend$setUseTextureArrays:
+ _objc_msgSend$setValue:
+ _objc_msgSend$setupNetwork
+ _objc_msgSend$sharedParameters
+ _objc_msgSend$skinMaskTex
+ _objc_msgSend$skyMaskTex
+ _objc_msgSend$stringForKey:
+ _objc_msgSend$suppressChroma:lumaTexture:outputChromaTexture:inputMetadata:
+ _objc_msgSend$textureDescriptorWithName:direction:layout:pixelFormat:
+ _objc_msgSend$tileIndicesToRun
+ _objc_msgSend$tileOverlap
+ _objc_msgSend$tileStepHeight
+ _objc_msgSend$tileStepWidth
+ _objc_msgSend$updateNoiseModelParametersFromMetadata:demosaicNetworkParams:
+ _objc_msgSend$updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:
+ _objc_msgSend$valueWaitingUpToTimeout:status:
+ _objc_msgSend$warpWrtMainFrame:label:
+ _objc_retainAutoreleasedReturnValue
CStrings:
+ "! _hasEv0Frame"
+ "! _hasLongFrame"
+ "! _hasMainFrame"
+ "! _processorOutput.gainMapOutputPixelBuffer"
+ "! _processorOutput.inferenceInputPixelBuffer"
+ "*error = [self _computeHdrMaskForEv0:ev0 hdrMask:hdrMask onCommandBuffer:cb] == 0 "
+ "+[LearnedDemosaicNetworkStage prewarmShaders:]"
+ "+[LearnedFusionDeghostingMitigation prewarmShaders:]"
+ "+[LearnedFusionHighlightMitigation prewarmShaders:]"
+ "+[LearnedFusionNetworkStage prewarmShaders:]"
+ "-[CMITiledInferenceProcessorTilePipelineStage(LearnedHRNR) initLearnedHRNRWithMetalContext:forQuadra:error:]"
+ "-[LearnedDemosaicNetworkPostANEStage processTilePipelineStage:]"
+ "-[LearnedDemosaicNetworkPreANEStage processTilePipelineStage:]"
+ "-[LearnedDemosaicNetworkStage getNetworkPath]"
+ "-[LearnedDemosaicNetworkStage initWithContext:cameraInfo:isQuadra:]"
+ "-[LearnedDemosaicNetworkStage runDemosaicWithInputRawTexture:outputRgbTexture:]"
+ "-[LearnedDemosaicNetworkStage setupNetwork]"
+ "-[LearnedDemosaicNetworkStage updateNoiseModelParametersFromMetadata:demosaicNetworkParams:]"
+ "-[LearnedDemosaicNetworkStage updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:]"
+ "-[LearnedDemosaicNetworkTuningParams readPlist:]"
+ "-[LearnedFusionBoundInferenceResults initWithResult:andMetal:]"
+ "-[LearnedFusionConfig _processSyntheticReferenceMetadataFromReferenceEV0]"
+ "-[LearnedFusionConfig initWithFrames:]"
+ "-[LearnedFusionDeghostingMitigation addFrame:isMainFrame:]"
+ "-[LearnedFusionDeghostingMitigation buildPyramidForFrame:withLabel:]"
+ "-[LearnedFusionDeghostingMitigation generateModulationMaps]"
+ "-[LearnedFusionDeghostingMitigation initWithMetalContext:]"
+ "-[LearnedFusionDeghostingMitigation process]"
+ "-[LearnedFusionDeghostingMitigationTuningParams readPlist:]"
+ "-[LearnedFusionHighlightMitigation initWithMetalContext:]"
+ "-[LearnedFusionHighlightMitigation mitigateHighlightsWithInOutQuadraTexture:]"
+ "-[LearnedFusionNetworkPostANEStage processTilePipelineStage:]"
+ "-[LearnedFusionNetworkPreANEStage processTilePipelineStage:]"
+ "-[LearnedFusionNetworkStage fillRawNoiseModelParameters:exposureParams:]"
+ "-[LearnedFusionNetworkStage initWithMetal:]"
+ "-[LearnedFusionNetworkStage runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:]"
+ "-[LearnedFusionNetworkStage setupNetwork]"
+ "-[LearnedFusionNetworkTuningParams readPlist:]"
+ "-[LearnedFusionProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:]"
+ "-[LearnedFusionProcessor _prepareOutputMetadata:]"
+ "-[LearnedFusionProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:]"
+ "-[LearnedFusionProcessor addFrame:]"
+ "-[LearnedFusionProcessor addInputResource:]"
+ "-[LearnedFusionProcessor bindResourcesForProcessingType:prepareDescriptor:]"
+ "-[LearnedFusionProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:]"
+ "-[LearnedFusionProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:]"
+ "-[LearnedFusionProcessor determineWorkingBufferRequirementsWithPrepareDescriptorByProcessingType:nrfConfig:memoryAllocationInfo:]"
+ "-[LearnedFusionProcessor finishProcessing]"
+ "-[LearnedFusionProcessor generateGainMapIfNeeded]"
+ "-[LearnedFusionProcessor initWithCommandQueue:]"
+ "-[LearnedFusionProcessor prepareToProcess:prepareDescriptor:]"
+ "-[LearnedFusionProcessor prewarm]"
+ "-[LearnedFusionProcessor process]"
+ "-[LearnedFusionProcessor runChromaSuppressionWithInOutFusedImage:]"
+ "-[LearnedFusionProcessor runDetectors]"
+ "-[LearnedFusionProcessor runHighlightMitigation]"
+ "-[LearnedFusionProcessor runLearnedDemosaicNetworkStage]"
+ "-[LearnedFusionProcessor runPipeline]"
+ "-[LearnedFusionProcessor runSemanticInferences]"
+ "-[LearnedFusionProcessor setLinearOutputMetadata:]"
+ "-[LearnedFusionProcessor setReferenceFrameIndex:]"
+ "-[LearnedFusionProcessor setupWithOptions:nrfConfig:]"
+ "-[LearnedFusionProcessor supportsInputPixelFormat:]"
+ "-[LearnedFusionProcessor warpWrtMainFrame:label:]"
+ "-[LearnedFusionProcessor(Tuning) prepareTuning:withProcessingMode:]"
+ "-[LearnedHRNRBoundInferenceResults initWithResult:andMetal:]"
+ "-[LearnedHRNRNetworkPostStage initWithMetal:error:]"
+ "-[LearnedHRNRNetworkPostStage processTilePipelineStage:]"
+ "-[LearnedHRNRNetworkPostStage setOutput:]"
+ "-[LearnedHRNRNetworkPreStage initWithMetal:error:]"
+ "-[LearnedHRNRNetworkPreStage processTilePipelineStage:]"
+ "-[LearnedHRNRNetworkPreStage setInput:]"
+ "-[LearnedHRNRNetworkStage _reloadNetworkForQuadra:]"
+ "-[LearnedHRNRNetworkStage computeTileScheduleAsyncForEv0:error:]"
+ "-[LearnedHRNRNetworkStage initWithMetalContext:config:error:]"
+ "-[LearnedHRNRNetworkStage runLearnedHRNROnEv0:evm:tileSchedule:error:executionStatus:completion:]"
+ "-[LearnedHRNRNetworkStage runLearnedHRNROnEv0:evm:tileSchedule:error:executionStatus:completion:]_block_invoke"
+ "-[LearnedHRNRProcessor _allocateRegWarpPPWithWidth:height:pixelFormat:]"
+ "-[LearnedHRNRProcessor _prepareOutputMetadata:]"
+ "-[LearnedHRNRProcessor _processInferenceImage:sourceFrameLumaChromaImage:sourceFrameProperties:ltcFrameProperties:gtcFrameProperties:originalWidth:originalHeight:]"
+ "-[LearnedHRNRProcessor addFrame:]"
+ "-[LearnedHRNRProcessor addInputResource:]"
+ "-[LearnedHRNRProcessor bindResourcesForProcessingType:prepareDescriptor:]"
+ "-[LearnedHRNRProcessor calculateBackingBufferSizeForDesc:nrfConfig:metal:]"
+ "-[LearnedHRNRProcessor determineWorkingBufferRequirementsToProcess:prepareDescriptor:nrfConfig:denoiseFusePipelineSize:rwppSize:rwppInputWidth:rwppInputHeight:]"
+ "-[LearnedHRNRProcessor finishProcessing]"
+ "-[LearnedHRNRProcessor generateGainMapIfNeeded]"
+ "-[LearnedHRNRProcessor initWithCommandQueue:]"
+ "-[LearnedHRNRProcessor prepareToProcess:prepareDescriptor:]"
+ "-[LearnedHRNRProcessor process]"
+ "-[LearnedHRNRProcessor runDemosaicWithInputRawTex:outputImage:frame:completion:]"
+ "-[LearnedHRNRProcessor runDetectors]"
+ "-[LearnedHRNRProcessor runPipeline]"
+ "-[LearnedHRNRProcessor runSemanticInferences]"
+ "-[LearnedHRNRProcessor setLinearOutputMetadata:]"
+ "-[LearnedHRNRProcessor setupWithOptions:nrfConfig:]"
+ "-[LearnedHRNRProcessor supportsInputPixelFormat:]"
+ "-[LearnedHRNRProcessor(Tuning) prepareTuning:]"
+ "-[LearnedHRNRTileScheduler _computeHdrMaskForEv0:hdrMask:onCommandBuffer:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: %@ is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: Cannot prewarm LearnedFusionDeghostingMitigation"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: Failed to initialize %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: LearnedFusionDeghostingMitigation: All frames aren't availabe for process!!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: LearnedFusionDeghostingMitigation: Unrecognized frame type!!"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: Metal context nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: Unable to read decayRateTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: Unable to read lumaCutoffTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: Unable to read lumaEdgeCutoffTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: ev0Pyramid doesn't have enough levels, it has: %lu levels, required levels: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: ev0Pyramid is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: longPyramid doesn't have enough levels, it has: %lu levels, required levels: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: longPyramid is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: mainPyramid doesn't have enough levels, it has: %lu levels, required levels: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: mainPyramid is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/DeghostingMitigation/LearnedFusionDeghostingMitigationV4.m %s: pyramidDesc is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/HighlightMitigation/LearnedFusionHighlightMitigationV4.m %s: Cannot prewarm LearnedFusionHighlightMitigation"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/HighlightMitigation/LearnedFusionHighlightMitigationV4.m %s: Failed to initialize %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/HighlightMitigation/LearnedFusionHighlightMitigationV4.m %s: Metal context nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/HighlightMitigation/LearnedFusionHighlightMitigationV4.m %s: highlightMitigatedQuadraTexture is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/HighlightMitigation/LearnedFusionHighlightMitigationV4.m %s: td is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: %{private}@ Processor process: processingType (%{public}d): %{private}s(errCode=%{public}d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: %{private}@ addFrame (%{public}d): %{private}s(%{public}d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: %{private}@ finishProcessing: %{private}s(err=%{public}d), stage = %{private}@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Cannot create inputFrame for frame index: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Cannot create metal context"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Cannot find ev0InputFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Cannot find ltcInputFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Cannot instantiate FigMetalContext for prewarming"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Could not prepareToProcess the softLTM stage, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Doesn't support input pixelFormat"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Error: Input inputResource is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed [rwpp allocateResources:imageHeight:imageFormat:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed allocate warped for frame: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to allocate %{public}@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to allocate RegWarpPP"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to bind resources, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init CMIDemosaicStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init CMIPost"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init CMIWarpStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init GainMapStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init GrayGhostDetection"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init LearnedFusionNetworkStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init MotionDetection"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init RawDFDownsampleStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init RawDFFlickerDetectorStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init RawDFInferenceGen"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to init learnedFusionChromaSuppressionStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Failed to regularize tone curves %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Flicker has been detected but not reported earlier, why!? bailing.."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Invalid reference frame Index"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: LF only supports QSUB"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: LFP metal.allocator is leaking memory"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: LSC gains texture is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Mismatch between prepare heights in options"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Mismatch between prepare pixel formats in options"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Mismatch between prepare widths in options"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Missing cameraInfoByPortType"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: No ev0RefDenoising tuning parameters found for denoise and sharpening, no processing to be done"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: No evmRefDenoising tuning parameters found for denoise and sharpening, no processing to be done"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: No quadraLearnedDemosaicTuning tuning parameters found, no processing to be done"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: No quadraLearnedFusionPostFusionTuning tuning parameters found, no processing to be done"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: No support for planar pixelFormat"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: No tuning parameters found for noise model, no processing to be done"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: No tuning parameters found for toneMapping, no processing to be done"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: SensorID mismatch for input image and tuning parameters. Input image has: %@, while tuning plist has:\n %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unable to calculate working buffer size"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unable to create LearnedFusionProcessor"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unable to create RawDFCommon"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unable to create RawProcFrames"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unable to create _colorConvertStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unable to create _lscGainsPlist"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unable to create _metal.allocator"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unable to create softLTM"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unable to initialize NRFConfig"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unexpected Allocator type"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unexpected frame count %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unexpected regwarpDims (0,0) "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unexpected setup regwarpDims (0,0)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: Unexpected setup regwarpDims (0,0) "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _demosaicProcessingOptions is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _fusionConfig is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _inputFrames.referenceFrame must not be nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _learnedDesmosaicStage is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _learnedFusionDeghostingMitigationStage is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _learnedFusionHighlightMitigationStage is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _metalCommandQueue is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _referenceFrameHasEVMinus is False, but _fusionConfig.hasEVM is True. This isn't right"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: _sharedRegWarpBuffer nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: allocatorDesc nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: bindTexture is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: calculateLTMReferenceEV0Frame failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: computeLTMFromLuma: chroma: final fail"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: darkestFrame draftInferenceRGBTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: darkestFrame is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: darkestFrame not having valid registration"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: denoiseFusePipelineSize 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: ev0 not having valid registration"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: ev0InputFrame is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: evm not having valid registration"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: frame is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: frame.uniqueFrameId:%d does not have valid registration"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: frame.uniqueFrameId:%d registration not complete"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: frame.uniqueFrameId:%d rgbTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: gainMap plist nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: gainMapOutputPixelBuffer is missing while expected"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: gainMapOutputTexture failed to bind"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: gtcFrameProperties nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: hasEVM and input sifr are in conflict"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: height 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: inference results bindings cannot be missing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: inference results cannot be missing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: inferenceInputPixelBuffer is missing while expected"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: inferenceInputPixelBuffer nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: input frame cannot be both EVM and Long at the same time"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: instanceMask is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: learnedDemosaicStage setupNetwork failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: learnedFusionNetworkStage setupNetwork failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: learnedFusionOutput is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: ltcFrameProperties nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: ltcInputFrame is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: mainFrame draftInferenceRGBTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: memoryAllocationInfo nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: missing EVMHomographyOriginalBeforeZoomUpdate in syntheticReference metadata"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: missing _longFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: missing ltmMetadata in syntheticReference metadata"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: missing referenceFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: nrfConfig nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: nrfPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: optionsTuningParameters nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: originalWidth > 0 && originalHeight > 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: output init failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: peakMemorySize must not be 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: pixel buffer format is invalid for gain map"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: pixelBuffer is nil "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: pixelFormat 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: pixelFormatDesc is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: postConfig is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: postProcOutput is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: process called without addFrame (no frames)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: processingType = %{public}d, numBracketsFused=%{public}d, nRegisteredFrames=%{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: quadraLearnedFusionPostFusionTuning is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: refFrame is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: refFrame.uniqueFrameId:%d does not have valid registration"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: refFrame.uniqueFrameId:%d registration not complete"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: refFrame.uniqueFrameId:%d rgbTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: referenceEv0Frame not valid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: referenceEv0Frame.metadata not valid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: referenceFrameIndex not set"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: runHighlightMitigation can be only run on quadra mainFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: runPostWithConfig failed with (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: setupWithDescriptor failed, bailing (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: sourceFrameLumaChromaImage nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: sourceFrameProperties nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: stfTuningParameters nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: td is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/LearnedFusionProcessorV4.m %s: width 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Cannot prewarm LearnedDemosaicNetworkPostANEStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Cannot prewarm LearnedDemosaicNetworkPreANEStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Error updating noise config from metadata"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to create _postStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to create _preStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to create _shared."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to create _tiledInferenceProcessor."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to create config."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to create stage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to find AGC"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to find ConversionGain"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to find ReadNoise_1x"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to find ReadNoise_8x"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to get LearnedDemosaic network path."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Failed to initialize LearnedDemosaicNetworkStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: LearnedDemosaicNetworkStage 'setupNetwork' needs to be called before."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: LearnedDemosaicNetworkStage hasn't been configured, updateParametersFromMetadata() needs to be called prior to this function."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: LearnedDemosaicNetworkStage supports only quadra at the moment."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Metadata missing SensorBlackLevel"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Network isn't availabe for non quadra type"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Only QSUB mode is supported"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Quadra bayer pattern must be BBGG or RRGG"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: Unable to read %@ %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: _postStage nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: _preStage nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: _processingOptions nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: _shared.demosaicNetworkParameters nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: _tiledInferenceProcessor nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: bayerPattern nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: cameraInfoByPortType nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: commandBuffer nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: encoder nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: getDemosaicNetworkParameters returns nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: inputRaw nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: invalid inputRawTexture dimensions."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: invalid inputRawTexture pixelFormat."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: invalid outputRgbTexture dimensions."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: invalid outputRgbTexture pixelFormat."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: lscGainsTexture is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: metadata nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: metal nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: outputRgbTexture nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: self.shared._demosaicNetworkParameters nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: self.shared.demosaicNetworkParameters nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedDemosaicNetworkStageV4.m %s: self.shared.isQuadra should be true."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Cannot prewarm LearnedFusionNetworkPostANEStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Cannot prewarm LearnedFusionNetworkPreANEStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Demosaiced RGB images need to have HRGainDownRatio Reverted"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Demosaiced RGB images need to have LSC reverted"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Failed to create _fusionStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Failed to create _shared."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Failed to create config."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Failed to create fusionStage.networkConfig."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Failed to create postFusionStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Failed to create preFusionStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Failed to create proc."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Failed to initialize LearnedFusionNetworkStage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to create texture %s."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read %@ %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read lumaAddBackBand0Tuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read lumaAddBackClipToSNRTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read lumaAddBackLSCModulationTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read lumaAddBackMaxNoiseFactorTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read lumaAddBackPersonSlopeTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read lumaAddBackPowerDenomNoiseFactorTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read lumaAddBackSkinSlopeTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read lumaAddBackSkySlopeTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: Unable to read lumaAddBackTuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: _processor not created, was setupNetwork called?"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: _shared nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: computeEncoder nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: exposureParams NULL."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: noiseParams NULL."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Networks/LearnedFusionNetworkStageV4.m %s: td nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: DefaultSensorIDs dictionary is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: Defringing tuning is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: Failed to parse defringing tuning"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: MIWB readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: MIWBPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: OutputNoiseModelPlist readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: _tuningParams dictionary is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: denoiseAndSharpening %@ readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: dictForZoom is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: entryParams DenoiseAndSharpening is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: entryParams NoiseModel is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: entryParams SyntheticReference is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: entryParams ToneMapping is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: failure to extract GainMapPlist parameters"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: greenGhostBrightLightTuningParams readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: lfParametersForProcessingMode is nil for %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: noiseModelPlist readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: nrfPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: onmPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: parametersDictMode1x is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: parametersDictMode2x is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: qdemTuning is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: qdemTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: quadraLearnedDemosaicTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: quadraLearnedFusion readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: quadraLearnedFusionDeghostingTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: quadraLearnedFusionPostFusionTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: semStylesPlist readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: sensorID is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: sensorIDAsNumber is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedFusion/Tuning/LearnedFusionTuningV4.m %s: toneMapping readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: %{private}@ Processor process: processingType (%{public}d): %{private}s(errCode=%{public}d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: %{private}@ addFrame (%{public}d): %{private}s(%{public}d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Cannot create inputFrame for frame index: %{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Cannot create metal context"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Cannot find ev0InputFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Cannot find ltcInputFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Could not prepareToProcess the softLTM stage."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Doesn't support input pixelFormat"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: EV0 draftInferenceRGBTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed [rwpp allocateResources:imageHeight:imageFormat:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to allocate %{public}@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to allocate RegWarpPP"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to bind resources"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to init CMIDemosaicStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to init CMIDraftDemosaicStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to init CMIPost"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to init GainMapStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to init GrayGhostDetection"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to init MotionDetection"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to init RawDFDownsampleStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to init RawDFFlickerDetectorStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Failed to init RawDFInferenceGen"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: GrayGhost has been detected; bailing.."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: LSC gains texture is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: No input reference frame "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: No support for planar pixelFormat"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: RawDF failed setting up allocator with error = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: SIFR frame %{public}@ available"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Unable to create RawDFCommon"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Unable to create softLTM"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Unable to initialize NRFConfig"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Unexpected Allocator type"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Unexpected regwarpDims (0,0) "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: Unexpected setup regwarpDims (0,0) "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: bindTexture is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: calculateLTMReferenceEV0Frame failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: computeLTMFromLuma fail"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: darkestFrame is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: ev0 not having valid registration"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: evm not having valid registration"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: gainMap plist nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: gainMapOutputTexture failed to bind"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: gtcFrameProperties nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: inference results bindings cannot be missing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: inference results cannot be missing"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: inferenceInputPixelBuffer is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: inferenceInputPixelBuffer nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: input frame cannot be both EVM and Long at the same time"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: instanceMask is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: learnedNRNetworkStage getFinalProcessingStatus (finish) status error (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: lensShadingCorrectionGainMapParameters is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: lscGainMapSbuf is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: ltcFrameProperties nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: missing referenceFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: missing sifrFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: nrfPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: originalWidth > 0 && originalHeight > 0"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: pixel buffer format is invalid for gain map"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: pixelBuffer is nil "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: pixelFormatDesc is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: postConfig is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: postProcOutput is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: process called without addFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: processLTMMetadata fail"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: processingType = %{public}d, numBracketsFused=%{public}d, nRegisteredFrames=%{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: referenceFrame draftInferenceRGBTex is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: runPostWithConfig failed with (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: sourceFrameLumaChromaImage nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: sourceFrameProperties nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/LearnedHRNRProcessorV4.m %s: td is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/CMITiledInferenceProcessorTilePipelineStage+LearnedHRNRV4.m %s: [super init] failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/CMITiledInferenceProcessorTilePipelineStage+LearnedHRNRV4.m %s: initLearnedHRNRWithMetalContext missing network bundle at %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPostStageV4.m %s: Expected output pixel format to be R16Float for LearnedHRNRPostStageOutput.output"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPostStageV4.m %s: No output bayer pattern given"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPostStageV4.m %s: Unsupported bayer pattern %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPostStageV4.m %s: _output invalid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPostStageV4.m %s: encoder nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPostStageV4.m %s: nil metal context"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPostStageV4.m %s: self is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPreStageV4.m %s: _input invalid"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPreStageV4.m %s: encoder nil."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPreStageV4.m %s: nil metal context"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPreStageV4.m %s: tile index out of range"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkPreStageV4.m %s: unsupported bayer pattern %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: Cannot allocate %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: Failed to allocate %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: Failed to init _learnedHRNRTiledInferenceProcessor"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: Registration homographies unavailable"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: Tile dimensions invalid (width=%d, height=%d, overlap=%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: Unable to create command queue"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: Unable to create metal context"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: Unexpected hrnr post stage class"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: Unexpected hrnr pre stage class"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: _learnedHRNRTiledInferenceProcessor allocateIOBuffers failed %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: _learnedHRNRTiledInferenceProcessor loadWithConfig failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: _learnedHRNRTiledInferenceProcessor runWithTileCount failed %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: _learnedHRNRTiledInferenceProcessor runWithTileCount failed to complete %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: tile schedule not ready (%ld)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Network/LearnedHRNRNetworkStageV4.m %s: tileSchedule is nil but required"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: DefaultSensorIDs dictionary is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: Failed to parse defringing tuning for port type: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: MIWB readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: MIWBPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: Missing tuning for %@ , %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: OutputNoiseModelPlist readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: _tuningParams dictionary is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: denoiseAndSharpening readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: dictForZoom is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: entryParams DenoiseAndSharpening is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: entryParams NoiseModel is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: entryParams SyntheticReference is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: entryParams ToneMapping is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: failure to extract GainMapPlist parameters"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: greenGhostBrightLightTuningParams readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: learnedNRTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: noiseModelPlist readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: nrfPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: onmPlist is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: parametersDictForMode is nil for %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: parametersDictMode1x is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: qdemTuning is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: qdemTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: quadraLearnedNRTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: semStylesPlist readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: sensorID is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: sensorIDAsNumber is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: toneMapping readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: zimmerDEMTuning is nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedHRNR/Tuning/LearnedHRNRTuningV4.m %s: zimmerDEMTuning readPlist failed"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: LF cannot request other than EVM fusionMode when EVM is present"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: bailing LF Proxy since EVM has no valid registration"
+ "@\"CMIFuture\""
+ "@\"LearnedDemosaicNetworkPostANEStage\""
+ "@\"LearnedDemosaicNetworkPreANEStage\""
+ "@\"LearnedDemosaicNetworkShared\""
+ "@\"LearnedDemosaicNetworkStage\""
+ "@\"LearnedDemosaicNetworkTuningParams\""
+ "@\"LearnedFusionChromaSuppression\""
+ "@\"LearnedFusionChromaSuppressionTuningParams\""
+ "@\"LearnedFusionConfig\""
+ "@\"LearnedFusionDeghostingMitigation\""
+ "@\"LearnedFusionDeghostingMitigationTuningParams\""
+ "@\"LearnedFusionHighlightMitigation\""
+ "@\"LearnedFusionNetworkPostANEStage\""
+ "@\"LearnedFusionNetworkPreANEStage\""
+ "@\"LearnedFusionNetworkStage\""
+ "@\"LearnedFusionNetworkStageShared\""
+ "@\"LearnedFusionNetworkTuningParams\""
+ "@\"LearnedFusionProcessingOptions\""
+ "@\"LearnedHRNRNetworkPostStage\""
+ "@\"LearnedHRNRNetworkPostStageOutput\""
+ "@\"LearnedHRNRNetworkPreStage\""
+ "@\"LearnedHRNRNetworkPreStageInput\""
+ "@\"LearnedHRNRNetworkSharedParameters\""
+ "@\"LearnedHRNRNetworkStage\""
+ "@\"LearnedHRNRTileScheduler\""
+ "@28@0:8i16i20i24"
+ "@32@0:8@16^i24"
+ "@36@0:8@16B24^i28"
+ "@48@0:8@16@24@32^i40"
+ "@64@0:8@16@24@32^i40@48@?56"
+ "Band0Weight"
+ "CMITiledInferenceProcessorTilePipelineStage+LearnedHRNRV4.m"
+ "CVPixelBufferGetPixelFormatType( frame.lscGainMapBuffer ) == kCVPixelFormatType_64RGBAHalf"
+ "ClipToSNR"
+ "DeghostingMitigation"
+ "DocumentScanning"
+ "EV0RefParameters"
+ "EV0_other"
+ "EV0_ref"
+ "EVMRefParameters"
+ "FigMetalAllocator_LearnedFusion"
+ "HRNR"
+ "LONG"
+ "LSC buffer has unexpected pixel format"
+ "LSC buffer nil"
+ "LSCModulation"
+ "LSCOffsetX"
+ "LSCOffsetY"
+ "LSCScaleX"
+ "LSCScaleY"
+ "LearnedDemosaic"
+ "LearnedDemosaicNetworkPostANEStage"
+ "LearnedDemosaicNetworkPreANEStage"
+ "LearnedDemosaicNetworkShared"
+ "LearnedDemosaicNetworkStage"
+ "LearnedDemosaicNetworkStage::readInputTileFromQuadraImage"
+ "LearnedDemosaicNetworkStage::writeDemosaicedTileToFullImage"
+ "LearnedDemosaicNetworkStageBase"
+ "LearnedDemosaicNetworkStageV4.m"
+ "LearnedDemosaicNetworkTuningParams"
+ "LearnedFusion"
+ "LearnedFusion::postNetworkApplyLumaAddback"
+ "LearnedFusion::postNetworkCaluclateLumaAddback"
+ "LearnedFusion::preNetwork"
+ "LearnedFusionBoundInferenceResults"
+ "LearnedFusionChromaSuppression"
+ "LearnedFusionChromaSuppressionTuningParams"
+ "LearnedFusionChromaSuppressionV4.m"
+ "LearnedFusionCommon"
+ "LearnedFusionConfig"
+ "LearnedFusionDeghostingMitigation"
+ "LearnedFusionDeghostingMitigation::generateModulationMaps"
+ "LearnedFusionDeghostingMitigationTuningParams"
+ "LearnedFusionDeghostingMitigationV4.m"
+ "LearnedFusionHighlightMitigation"
+ "LearnedFusionHighlightMitigation::modulatehighlights"
+ "LearnedFusionHighlightMitigationV4.m"
+ "LearnedFusionNetworkParameters"
+ "LearnedFusionNetworkPostANEStage"
+ "LearnedFusionNetworkPreANEStage"
+ "LearnedFusionNetworkStage"
+ "LearnedFusionNetworkStageShared"
+ "LearnedFusionNetworkStageV4.m"
+ "LearnedFusionNetworkTuningParams"
+ "LearnedFusionPostNet"
+ "LearnedFusionPreNet"
+ "LearnedFusionProcessingOptions"
+ "LearnedFusionProcessor"
+ "LearnedFusionProcessorV4.m"
+ "LearnedFusionTuningV4.m"
+ "LearnedFusion_Quadra2x"
+ "LearnedHRNR"
+ "LearnedHRNR::copyBayerTileIn_planar"
+ "LearnedHRNR::copyBayerTileOut_planar"
+ "LearnedHRNR::copyHdrMask"
+ "LearnedHRNR::copyQuadraTileIn_planar"
+ "LearnedHRNR::copyQuadraTileOut_planar"
+ "LearnedHRNR::copyWithGain"
+ "LearnedHRNR::createWarpField_planar"
+ "LearnedHRNR::hdrMask_v2_blurX"
+ "LearnedHRNR::hdrMask_v2_blurYAndSoftThreshold"
+ "LearnedHRNR::hdrMask_v2_initialMask"
+ "LearnedHRNR::skipTile"
+ "LearnedHRNRBoundInferenceResults"
+ "LearnedHRNRNetworkConfig"
+ "LearnedHRNRNetworkPostStage"
+ "LearnedHRNRNetworkPostStageOutput"
+ "LearnedHRNRNetworkPostStageV4.m"
+ "LearnedHRNRNetworkPreStage"
+ "LearnedHRNRNetworkPreStage.copyEv0ToOutput"
+ "LearnedHRNRNetworkPreStageInput"
+ "LearnedHRNRNetworkPreStageV4.m"
+ "LearnedHRNRNetworkSharedParameters"
+ "LearnedHRNRNetworkStage"
+ "LearnedHRNRNetworkStageV4.m"
+ "LearnedHRNRPlist"
+ "LearnedHRNRProcessor"
+ "LearnedHRNRProcessorV4.m"
+ "LearnedHRNRTileScheduler"
+ "LearnedHRNRTuningV4.m"
+ "LumaAddBack"
+ "MaxNoiseFactor"
+ "PersonSlope"
+ "PostFusion"
+ "PowerDenomNoiseFactor"
+ "Prewarmable"
+ "Proxy_EVMinus"
+ "Proxy_EVZero"
+ "ReferenceEV0"
+ "SkinSlope"
+ "SkySlope"
+ "Soft Error: LearnedFusionDeghostingMitigation: addFrame: _hasEv0Frame is already true (ev0 frame is being added more than once, replacing the earlier one )"
+ "Soft Error: LearnedFusionDeghostingMitigation: addFrame: _hasLongFrame is already true (long frame is being added more than once, replacing the earlier one )"
+ "Soft Error: LearnedFusionDeghostingMitigation: addFrame: _hasMainFrame is already true (main frame is being added more than once, replacing the earlier one )"
+ "T@\"<MTLTexture>\",&,N,V_ev0"
+ "T@\"<MTLTexture>\",&,N,V_ev0DeghostingModulationMap"
+ "T@\"<MTLTexture>\",&,N,V_ev0ModulationMap"
+ "T@\"<MTLTexture>\",&,N,V_ev0RgbTex"
+ "T@\"<MTLTexture>\",&,N,V_evm"
+ "T@\"<MTLTexture>\",&,N,V_evmRawTex"
+ "T@\"<MTLTexture>\",&,N,V_evmRgbTex"
+ "T@\"<MTLTexture>\",&,N,V_hdrMask"
+ "T@\"<MTLTexture>\",&,N,V_lensShading"
+ "T@\"<MTLTexture>\",&,N,V_longDeghostingModulationMap"
+ "T@\"<MTLTexture>\",&,N,V_longModulationMap"
+ "T@\"<MTLTexture>\",&,N,V_longRgbTex"
+ "T@\"<MTLTexture>\",&,N,V_output"
+ "T@\"<MTLTexture>\",&,N,V_outputDemosaicRgbTexture"
+ "T@\"<MTLTexture>\",&,N,V_personMaskTex"
+ "T@\"<MTLTexture>\",&,N,V_skinMaskTex"
+ "T@\"<MTLTexture>\",&,N,V_skyMaskTex"
+ "T@\"<MTLTexture>\",W,N,V_ev0DeghostingModulationMap"
+ "T@\"<MTLTexture>\",W,N,V_inputLensShading"
+ "T@\"<MTLTexture>\",W,N,V_inputRawEvm"
+ "T@\"<MTLTexture>\",W,N,V_inputRgbEv0"
+ "T@\"<MTLTexture>\",W,N,V_inputRgbEvm"
+ "T@\"<MTLTexture>\",W,N,V_inputRgbLong"
+ "T@\"<MTLTexture>\",W,N,V_longDeghostingModulationMap"
+ "T@\"<MTLTexture>\",W,N,V_outputChroma"
+ "T@\"<MTLTexture>\",W,N,V_outputLuma"
+ "T@\"<MTLTexture>\",W,N,V_personMaskTex"
+ "T@\"<MTLTexture>\",W,N,V_skinMaskTex"
+ "T@\"<MTLTexture>\",W,N,V_skyMaskTex"
+ "T@\"LearnedDemosaicNetworkShared\",&,N,V_shared"
+ "T@\"LearnedFusionChromaSuppressionTuningParams\",&,N,V_lfChromaSuppressionTuningParams"
+ "T@\"LearnedFusionDeghostingMitigationTuningParams\",&,N,V_tuningParams"
+ "T@\"LearnedFusionNetworkStageShared\",&,N,V_shared"
+ "T@\"LearnedFusionNetworkTuningParams\",&,N,V_tuningParams"
+ "T@\"LearnedFusionProcessingOptions\",R,N,V_processingOptions"
+ "T@\"LearnedHRNRNetworkPostStageOutput\",W,N,V_output"
+ "T@\"LearnedHRNRNetworkPreStageInput\",W,N,V_input"
+ "T@\"LearnedHRNRNetworkSharedParameters\",&,N,V_sharedParameters"
+ "T@\"NRFFrameMetadata\",&,N,V_ev0Metadata"
+ "T@\"NRFFrameMetadata\",&,N,V_evmMetadata"
+ "T@\"NSArray\",&,N,V_tileIndicesToRun"
+ "T@\"NSDictionary\",&,N,V_ev0TuningParams"
+ "T@\"NSDictionary\",&,N,V_evmTuningParams"
+ "T@\"NSDictionary\",&,N,V_lensShadingParams"
+ "T@\"NSDictionary\",&,N,V_longTuningParams"
+ "T@\"NSDictionary\",&,N,V_ltmMetadata"
+ "T@\"NSDictionary\",&,N,V_tuningParams"
+ "T@\"NSNumber\",&,N,V_bayerPattern"
+ "T@\"NSNumber\",&,N,V_evmRawBayerPattern"
+ "T@\"PostDemosaicTuningParams\",R,N,V_postDemosaicTuningParams"
+ "T@\"RawProcInputFrame\",&,N,V_ev0Frame"
+ "T@\"RawProcInputFrame\",&,N,V_longFrame"
+ "T@\"RawProcInputFrame\",&,N,V_mainFrame"
+ "TB,N,V_applyDeghostingModulationForEv0LongNoises"
+ "TB,N,V_hasEVM"
+ "TB,N,V_runDetectors"
+ "TB,R,N,V_demosaicedImageHasHRGainApplied"
+ "TB,R,N,V_demosaicedImageHasLSCApplied"
+ "Tf,N,V_outputGainRatio"
+ "Ti,N,V_tileHeight"
+ "Ti,N,V_tileOverlap"
+ "Ti,N,V_tileWidth"
+ "T{?=[3]},N,V_ev0ToEvmHomography"
+ "T{?=iffBBB{?=}},N,V_detectorsOutput"
+ "T{LearnedDemosaicNetworkStageUniforms=BB{?=ff}{?=f{?=ffff}{?=ffff}}},N,V_demosaicNetworkParameters"
+ "T{exposureParameters=ffffffffffffffffffffffffBBBfBfffif},N,V_ev0Exposure"
+ "T{exposureParameters=ffffffffffffffffffffffffBBBfBfffif},N,V_ev0FrameExposureParameters"
+ "T{exposureParameters=ffffffffffffffffffffffffBBBfBfffif},N,V_evmExposure"
+ "T{exposureParameters=ffffffffffffffffffffffffBBBfBfffif},N,V_longExposure"
+ "T{exposureParameters=ffffffffffffffffffffffffBBBfBfffif},N,V_longFrameExposureParameters"
+ "T{exposureParameters=ffffffffffffffffffffffffBBBfBfffif},N,V_mainFrameExposureParameters"
+ "Weight"
+ "[6@\"<NRFSubProcessor>\"]"
+ "[[LearnedFusionNetworkPostANEStage alloc] initWithMetal:metal]"
+ "[[LearnedFusionNetworkPreANEStage alloc] initWithMetal:metal]"
+ "[[LearnedHRNRNetworkPostStage alloc] initWithMetal:metal error:&err]"
+ "[[LearnedHRNRNetworkPreStage alloc] initWithMetal:metal error:&error]"
+ "[[LearnedHRNRTileScheduler alloc] initWithMetalContext:metal error:&error]"
+ "\\d+(?:\\.\\d+)?o?"
+ "^{?=Bffffffffff{?=ff}{?=ffff}}16@0:8"
+ "^{?=fBB}16@0:8"
+ "^{?={?=fffff{?=ffff}}{?=fffff{?=ffff}}{?=fffff{?=ffff}}fff{?=ffff}{?=ffff}{?=ffff}{?=ff}{?=B}}16@0:8"
+ "^{LearnedDemosaicNetworkStageUniforms=BB{?=ff}{?=f{?=ffff}{?=ffff}}}16@0:8"
+ "_applyDeghostingModulationForEv0LongNoises"
+ "_completionEvent"
+ "_completionEventListener"
+ "_computeHdrMaskForEv0:hdrMask:onCommandBuffer:"
+ "_consts"
+ "_copyBayerTileIn"
+ "_copyBayerTileIn = [metal computePipelineStateFor:@\"LearnedHRNR::copyBayerTileIn_planar\" constants:((void *)0) fault:error]"
+ "_copyBayerTileOut"
+ "_copyBayerTileOut = [metal computePipelineStateFor:@\"LearnedHRNR::copyBayerTileOut_planar\" constants:((void *)0) fault:error]"
+ "_copyHdrMask"
+ "_copyHdrMask = [metal computePipelineStateFor:@\"LearnedHRNR::copyHdrMask\" constants:((void *)0) fault:error]"
+ "_copyQuadraTileIn"
+ "_copyQuadraTileIn = [metal computePipelineStateFor:@\"LearnedHRNR::copyQuadraTileIn_planar\" constants:((void *)0) fault:error]"
+ "_copyQuadraTileOut"
+ "_copyQuadraTileOut = [metal computePipelineStateFor:@\"LearnedHRNR::copyQuadraTileOut_planar\" constants:((void *)0) fault:error]"
+ "_copyWithGain"
+ "_copyWithGain = [metal computePipelineStateFor:@\"LearnedHRNR::copyWithGain\" constants:((void *)0) fault:error]"
+ "_createWarpField"
+ "_createWarpField = [metal computePipelineStateFor:@\"LearnedHRNR::createWarpField_planar\" constants:((void *)0) fault:error]"
+ "_crossQueueEvent"
+ "_crossQueueEventValue"
+ "_demosaicNetworkParameters"
+ "_demosaicProcessingOptions"
+ "_demosaicedImageHasHRGainApplied"
+ "_demosaicedImageHasLSCApplied"
+ "_denoiseBoostMap"
+ "_detectorsOutput"
+ "_ev0DeghostingModulationMap"
+ "_ev0EvmHomography"
+ "_ev0Exposure"
+ "_ev0Frame"
+ "_ev0Frame && _ev0Frame.rgbTex"
+ "_ev0Frame.rgbTex.width >> ( 3 ) == _ev0ModulationMap.width && _ev0Frame.rgbTex.height >> ( 3 ) == _ev0ModulationMap.height"
+ "_ev0FrameExposureParameters"
+ "_ev0Metadata"
+ "_ev0ModulationMap"
+ "_ev0ModulationMap && _ev0ModulationMap.pixelFormat == MTLPixelFormatR16Float"
+ "_ev0RgbTex"
+ "_ev0ToEvmHomography"
+ "_ev0TuningParams"
+ "_evmExposure"
+ "_evmMetadata"
+ "_evmRawBayerPattern"
+ "_evmRawTex"
+ "_evmRgbTex"
+ "_evmTuningParams"
+ "_fillNoiseScaleFactors:noiseScaleFactors:gain:"
+ "_forQuadra"
+ "_fusionConfig"
+ "_gainRatioFloat"
+ "_getInterpolatedGainFromTuningParams:gain:"
+ "_getInterpolatedGainFromTuningParams:key:gain:"
+ "_getLscGainsTexAndParameters:lscGainsTex:lscGainsParameters:"
+ "_hasBeenConfigured"
+ "_hasEv0Frame"
+ "_hasMainFrame"
+ "_hdrMask"
+ "_hdrMaskV2BlurX"
+ "_hdrMaskV2BlurX = [metalContext computePipelineStateFor:@\"LearnedHRNR::hdrMask_v2_blurX\" constants:((void *)0) fault:error]"
+ "_hdrMaskV2BlurYAndSoftThreshold"
+ "_hdrMaskV2BlurYAndSoftThreshold = [metalContext computePipelineStateFor:@\"LearnedHRNR::hdrMask_v2_blurYAndSoftThreshold\" constants:((void *)0) fault:error]"
+ "_hdrMaskV2InitialMask"
+ "_hdrMaskV2InitialMask = [metalContext computePipelineStateFor:@\"LearnedHRNR::hdrMask_v2_initialMask\" constants:((void *)0) fault:error]"
+ "_input"
+ "_inputLensShading"
+ "_inputRawEvm"
+ "_inputRgbEv0"
+ "_inputRgbEvm"
+ "_inputRgbLong"
+ "_learnedDesmosaicStage"
+ "_learnedFusionChromaSuppressionStage"
+ "_learnedFusionDeghostingMitigationStage"
+ "_learnedFusionHighlightMitigationStage"
+ "_learnedFusionNetworkStage"
+ "_learnedHRNRNetworkStage"
+ "_learnedHRNRPostStage"
+ "_learnedHRNRPreStage"
+ "_learnedHRNRTileSchedule"
+ "_learnedHRNRTileSchedule = [_learnedHRNRNetworkStage computeTileScheduleAsyncForEv0:_inputFrames.referenceFrame error:&err]"
+ "_learnedHRNRTileScheduler"
+ "_learnedHRNRTileScheduler = [[LearnedHRNRTileScheduler alloc] initWithMetalContext:_lowLatencyMetal error:error]"
+ "_learnedHRNRTiledInferenceProcessor"
+ "_lensShading"
+ "_lensShadingParams"
+ "_lfChromaSuppressionTuningParams"
+ "_longDeghostingModulationMap"
+ "_longExposure"
+ "_longFrame && _longFrame.rgbTex"
+ "_longFrame.rgbTex.width >> ( 3 ) == _longModulationMap.width && _longFrame.rgbTex.height >> ( 3 ) == _longModulationMap.height"
+ "_longFrameExposureParameters"
+ "_longModulationMap"
+ "_longModulationMap && _longModulationMap.pixelFormat == MTLPixelFormatR16Float"
+ "_longRgbTex"
+ "_longTuningParams"
+ "_lowLatencyMetal"
+ "_mainFrame"
+ "_mainFrame && _mainFrame.rgbTex"
+ "_mainFrameExposureParameters"
+ "_metal = metal"
+ "_networkSetupIsComplete"
+ "_nextCompletionEventValue"
+ "_outputDemosaicRgbTexture"
+ "_outputGainRatio"
+ "_parentQueue"
+ "_personMaskTex"
+ "_postApplyLumaAddbackNetwork"
+ "_postApplyLumaAddbackNetwork = [metal computePipelineStateFor:@\"LearnedFusion::postNetworkApplyLumaAddback\" constants:((void *)0) fault:&err]"
+ "_postCalcLumaAddbackNetwork"
+ "_postCalcLumaAddbackNetwork = [metal computePipelineStateFor:@\"LearnedFusion::postNetworkCaluclateLumaAddback\" constants:((void *)0) fault:&err]"
+ "_postFusionStage"
+ "_preFusionStage"
+ "_preNetwork"
+ "_preNetwork = [metal computePipelineStateFor:@\"LearnedFusion::preNetwork\" constants:((void *)0) fault:&err]"
+ "_processor"
+ "_projectEv0ToEvm:"
+ "_quadraInputs"
+ "_readInputTileFromQuadraImage"
+ "_readInputTileFromQuadraImage = [metal computePipelineStateFor:@\"LearnedDemosaicNetworkStage::readInputTileFromQuadraImage\" constants:((void *)0) fault:&err]"
+ "_reloadNetworkForQuadra:"
+ "_shaders[Shader_generateModulationMaps] = [_metal computePipelineStateFor:@ \"LearnedFusionDeghostingMitigation::\" \"generateModulationMaps\" constants:((void *)0)]"
+ "_shaders[Shader_modulatehighlights] = [_metal computePipelineStateFor:@ \"LearnedFusionHighlightMitigation::\" \"modulatehighlights\" constants:((void *)0)]"
+ "_sharedParameters"
+ "_skipTile"
+ "_skipTile = [metalContext computePipelineStateFor:@\"LearnedHRNR::skipTile\" constants:((void *)0) fault:error]"
+ "_subProcessors[NRFSubProcessorType_LearnedFusion]"
+ "_subProcessors[NRFSubProcessorType_LearnedHRNR]"
+ "_tileClipCount"
+ "_tileCount"
+ "_tileIndicesToRun"
+ "_writeDemosaicedTileToFullImage"
+ "_writeDemosaicedTileToFullImage = [metal computePipelineStateFor:@\"LearnedDemosaicNetworkStage::writeDemosaicedTileToFullImage\" constants:((void *)0) fault:&err]"
+ "a"
+ "addFrame:isMainFrame:"
+ "allocateIOBuffers"
+ "applyDeghostingModulationForEv0LongNoises"
+ "buildPyramidForFrame:withLabel:"
+ "checkNetworkStatusWithLabel:statusGroup:status:"
+ "computeTileScheduleAsyncForEv0:error:"
+ "consts"
+ "copyEv0ToOutput:"
+ "crnetOutputRaw"
+ "decayRateTuning"
+ "decayRateTuning && decayRateTuning->length >= 1"
+ "defaultManager"
+ "defaultTuningDict"
+ "demosaicNetworkParameters"
+ "demosaicedImageHasHRGainApplied"
+ "demosaicedImageHasLSCApplied"
+ "demosaiced_image"
+ "detectorsOutput"
+ "error = [LearnedHRNRNetworkPostStage prewarmShaders:metal tuningParameters:tuningParameters] == 0 "
+ "error = [LearnedHRNRNetworkPreStage prewarmShaders:metal tuningParameters:tuningParameters] == 0 "
+ "error = [LearnedHRNRTileScheduler prewarmShaders:metal tuningParameters:tuningParameters] == 0 "
+ "ev0DeghostingModulationMap"
+ "ev0Exposure"
+ "ev0Frame"
+ "ev0Frame && ev0Frame.rgbTex"
+ "ev0FrameExposureParameters"
+ "ev0Metadata"
+ "ev0ModulationMap"
+ "ev0Pyramid"
+ "ev0RgbTex"
+ "ev0ToEvmHomography"
+ "ev0Tuning"
+ "ev0TuningParams"
+ "ev0_crop_1"
+ "evmExposure"
+ "evmMetadata"
+ "evmRawBayerPattern"
+ "evmRawTex"
+ "evmRgbTex"
+ "evmTuning"
+ "evmTuningParams"
+ "evm_crop_1"
+ "executionStatus"
+ "f28@0:8@16f24"
+ "f36@0:8@16@24f32"
+ "fileExistsAtPath:"
+ "frame.lscGainMapBuffer"
+ "fused_image"
+ "gainMapOutputPixelBuffer is provided while unexpected"
+ "generateGainMapIfNeeded"
+ "generateModulationMaps"
+ "generateModulationMapsFromMainFrame:ev0Frame:longFrame:ev0ModulationMap:longModulationMap:"
+ "getDeghostingModulationMaps:longDeghostingModulationMap:"
+ "getDemosaicNetworkParameters"
+ "getTuningForLHRNRTuningTypeAndZoomFactor"
+ "hasAllFrames"
+ "hasEVM"
+ "hdrMask"
+ "hrnrSynchronizer"
+ "i32@0:8@\"FigMetalContext\"16@\"NSDictionary\"24"
+ "i32@0:8@16^{LearnedDemosaicNetworkStageUniforms=BB{?=ff}{?=f{?=ffff}{?=ffff}}}24"
+ "i32@0:8^{?=fffff{?=ffff}}16r^{exposureParameters=ffffffffffffffffffffffffBBBfBfffif}24"
+ "image"
+ "inOutQuadraTexture"
+ "inferenceInputPixelBuffer is provided while unexpected"
+ "initLearnedHRNRWithMetalContext:forQuadra:error:"
+ "initWithContext:cameraInfo:isQuadra:"
+ "initWithFrames:"
+ "initWithMetal:error:"
+ "initWithMetalContext:config:error:"
+ "initWithMetalContext:error:"
+ "initWithOutputHasLSCApplied:hasHRGainApplied:"
+ "initWithSuiteName:"
+ "initWithTileWidth:tileHeight:tileOverlap:"
+ "inputLensShading"
+ "inputRawEvm"
+ "inputRgbEv0"
+ "inputRgbEvm"
+ "inputRgbLong"
+ "learnedfusion_fusion-v1.1"
+ "learnedfusion_sfdem-v1.1"
+ "learnedhrnr-BCHW-quadra-v"
+ "learnedhrnr-BCHW-v"
+ "learnedhrnr.tileskipping"
+ "lensShadingParams"
+ "lfChromaSuppressionTuningParams"
+ "longDeghostingModulationMap"
+ "longExposure"
+ "longFrame && longFrame.rgbTex"
+ "longFrameExposureParameters"
+ "longModulationMap"
+ "longPyramid"
+ "longRgbTex"
+ "longTuning"
+ "longTuningParams"
+ "long_image"
+ "long_noise"
+ "lowLatencyQueue"
+ "lscGainsParameters"
+ "lscGainsParameters Address is nil"
+ "lscGainsTex Address is nil"
+ "lumaAddBackBand0Tuning && lumaAddBackBand0Tuning->length >= 1"
+ "lumaAddBackClipToSNRTuning && lumaAddBackClipToSNRTuning->length >= 1"
+ "lumaAddBackLSCModulationTuning && lumaAddBackLSCModulationTuning->length >= 1"
+ "lumaAddBackMaxNoiseFactorTuning"
+ "lumaAddBackMaxNoiseFactorTuning && lumaAddBackMaxNoiseFactorTuning->length >= 1"
+ "lumaAddBackPersonSlopeTuning"
+ "lumaAddBackPowerDenomNoiseFactorTuning"
+ "lumaAddBackPowerDenomNoiseFactorTuning && lumaAddBackPowerDenomNoiseFactorTuning->length >= 1"
+ "lumaAddBackSkinSlopeTuning"
+ "lumaAddBackSkinSlopeTuning && lumaAddBackSkinSlopeTuning->length >= 1"
+ "lumaAddBackSkySlopeTuning"
+ "lumaAddBackTuning && lumaAddBackTuning->length >= 1"
+ "lumaCutoffTuning"
+ "lumaCutoffTuning && lumaCutoffTuning->length >= 1"
+ "lumaEdgeCutoffTuning"
+ "lumaEdgeCutoffTuning && lumaEdgeCutoffTuning->length >= 1"
+ "mainFrame"
+ "mainFrame && mainFrame.rgbTex"
+ "mainFrameExposureParameters"
+ "mainPyramid"
+ "maskTmp = [_metal.allocator newTextureWithDescriptor:td]"
+ "mask_crop_1"
+ "medium_image"
+ "medium_noise"
+ "mitigateHighlightsWithInOutQuadraTexture:"
+ "networkInputPorts"
+ "newCommandQueueWithDescriptor:"
+ "nrf.learnedhrnr.draft_ltm"
+ "nrf.learnedhrnr.networkBundlePath"
+ "nrf.learnedhrnr.quadraNetworkBundlePath"
+ "numberOfTilesForHeight:"
+ "numberOfTilesForWidth:"
+ "out_img"
+ "outputDemosaicRgbTexture"
+ "outputGainRatio"
+ "outputImage->chromaTex"
+ "params.personMaskTex"
+ "params.skinMaskTex"
+ "params.skyMaskTex"
+ "person inference mask is nil, fusion network won't be using any person mask tuning"
+ "personMaskTex"
+ "plistDict"
+ "postDemosaicTuningParams"
+ "postInferenceStage"
+ "preInferenceStage"
+ "prepareTuning:withProcessingMode:"
+ "quadraLearnedDemosaicTuning"
+ "quadraLearnedFusionDeghostingTuningParams"
+ "quadraLearnedFusionPostFusionTuning"
+ "quadraLearnedFusionTuning"
+ "referenceEv0Tuning"
+ "reference_image"
+ "reference_noise"
+ "rotate180ForBayerPattern:"
+ "runChromaSuppressionWithInOutFusedImage:"
+ "runDemosaicWithInputRawTexture:outputRgbTexture:"
+ "runDetectors"
+ "runHighlightMitigation"
+ "runLearnedDemosaicNetworkStage"
+ "runLearnedDemosaicNetworkStageOnGivenFrame:label:tuningParams:"
+ "runLearnedFusionWithParams:outputLumaTexture:outputChromaTexture:processingOptions:"
+ "runLearnedHRNROnEv0:evm:tileSchedule:error:executionStatus:completion:"
+ "runOnEv0:sharedParameters:hdrMask:error:"
+ "runWithTileCount:withCompletionHandler:event:waitValue:signalValue:"
+ "sampling_grid_1"
+ "self._compileShaders == 0 "
+ "self.postInferenceStage"
+ "self.preInferenceStage"
+ "setApplyDeghostingModulationForEv0LongNoises:"
+ "setBayerPattern:"
+ "setDemosaicNetworkParameters:"
+ "setDetectorsOutput:"
+ "setDisableIOFencing:"
+ "setEnableLowLatencySignalSharedEvent:"
+ "setEnableLowLatencyWaitSharedEvent:"
+ "setEv0:"
+ "setEv0DeghostingModulationMap:"
+ "setEv0Exposure:"
+ "setEv0Frame:"
+ "setEv0FrameExposureParameters:"
+ "setEv0Metadata:"
+ "setEv0ModulationMap:"
+ "setEv0RgbTex:"
+ "setEv0ToEvmHomography:"
+ "setEv0TuningParams:"
+ "setEvm:"
+ "setEvmExposure:"
+ "setEvmMetadata:"
+ "setEvmRawBayerPattern:"
+ "setEvmRawTex:"
+ "setEvmRgbTex:"
+ "setEvmTuningParams:"
+ "setHasEVM:"
+ "setHdrMask:"
+ "setInput:"
+ "setInputLensShading:"
+ "setInputRawEvm:"
+ "setInputRgbEv0:"
+ "setInputRgbEvm:"
+ "setInputRgbLong:"
+ "setLensShading:"
+ "setLensShadingParams:"
+ "setLfChromaSuppressionTuningParams:"
+ "setLongDeghostingModulationMap:"
+ "setLongExposure:"
+ "setLongFrame:"
+ "setLongFrameExposureParameters:"
+ "setLongModulationMap:"
+ "setLongRgbTex:"
+ "setLongTuningParams:"
+ "setLtmMetadata:"
+ "setMainFrame:"
+ "setMainFrameExposureParameters:"
+ "setOutputDemosaicRgbTexture:"
+ "setOutputGainRatio:"
+ "setPersonMaskTex:"
+ "setRunDetectors:"
+ "setSharedParameters:"
+ "setSkinMaskTex:"
+ "setSkyMaskTex:"
+ "setTileIndicesToRun:"
+ "setUseTextureArrays:"
+ "setValue:"
+ "setupNetwork"
+ "sharedParameters"
+ "skin inference is nil, fusion network won't be using any skin mask tuning"
+ "skinMaskTex"
+ "sky inference mask is nil, fusion network won't be using any sky mask tuning"
+ "skyMaskTex"
+ "stringForKey:"
+ "suppressChroma:lumaTexture:outputChromaTexture:inputMetadata:"
+ "textureDescriptorWithName:direction:layout:pixelFormat:"
+ "tileIndicesToRun"
+ "tileSchedule = [_learnedHRNRTileScheduler runOnEv0:ev0Frame sharedParameters:_learnedHRNRPreStage.sharedParameters hdrMask:_hdrMask error:error]"
+ "tileStepHeight"
+ "tileStepWidth"
+ "tuningDict[key]"
+ "updateNoiseModelParametersFromMetadata:demosaicNetworkParams:"
+ "updateParametersFromMetadata:bayerPattern:lscGainsTexture:lscGainParameters:"
+ "v112@0:8{LearnedDemosaicNetworkStageUniforms=BB{?=ff}{?=f{?=ffff}{?=ffff}}}16"
+ "v144@0:8{exposureParameters=ffffffffffffffffffffffffBBBfBfffif}16"
+ "v36@0:8@16^{?=ffff}24f32"
+ "v40@0:8@16^@24^@32"
+ "v56@0:8{?=iffBBB{?=}}16"
+ "valueWaitingUpToTimeout:status:"
+ "warpWrtMainFrame:label:"
+ "{?=\"ev0NoiseParams\"{?=\"whiteBalanceGains\"\"analogGain\"f\"conversionGain\"f\"sensorBlackLevel\"f\"lsModulationWeight\"f\"hrGainDownRatio\"f\"noiseVariances\"{?=\"readNoiseVariance\"f\"shotNoiseVariance\"f\"normalisedShotNoiseVariance\"f\"normalisedReadNoiseVariance\"f}}\"evmNoiseParams\"{?=\"whiteBalanceGains\"\"analogGain\"f\"conversionGain\"f\"sensorBlackLevel\"f\"lsModulationWeight\"f\"hrGainDownRatio\"f\"noiseVariances\"{?=\"readNoiseVariance\"f\"shotNoiseVariance\"f\"normalisedShotNoiseVariance\"f\"normalisedReadNoiseVariance\"f}}\"longNoiseParams\"{?=\"whiteBalanceGains\"\"analogGain\"f\"conversionGain\"f\"sensorBlackLevel\"f\"lsModulationWeight\"f\"hrGainDownRatio\"f\"noiseVariances\"{?=\"readNoiseVariance\"f\"shotNoiseVariance\"f\"normalisedShotNoiseVariance\"f\"normalisedReadNoiseVariance\"f}}\"ev0EitRatio\"f\"evmEitRatio\"f\"longEitRatio\"f\"ev0NoiseScaleFactors\"{?=\"lscNoiseFactor\"f\"globalNoiseFactor\"f\"lumaPowerDenomNoiseFactor\"f\"lumaMaxNoiseFactor\"f}\"evmNoiseScaleFactors\"{?=\"lscNoiseFactor\"f\"globalNoiseFactor\"f\"lumaPowerDenomNoiseFactor\"f\"lumaMaxNoiseFactor\"f}\"longNoiseScaleFactors\"{?=\"lscNoiseFactor\"f\"globalNoiseFactor\"f\"lumaPowerDenomNoiseFactor\"f\"lumaMaxNoiseFactor\"f}\"lscParams\"{?=\"lscScale\"\"lscOffset\"\"lscNormalization\"f\"lscModulationWeight\"f}\"deghostingMitigationConsts\"{?=\"modulateEv0LongNoises\"B}}"
+ "{?=\"outGain\"f\"rotateTile180\"B\"isQuadra\"B}"
+ "{?=\"rotate180\"B\"hrGainDownRatio\"f\"lumaAddBackWeight\"f\"lumaAddBackBand0Weight\"f\"lumaAddBackClipToSNR\"f\"lumaAddBackLSCModulation\"f\"lumaPowerDenomNoiseFactor\"f\"lumaMaxNoiseFactor\"f\"lumaAddBackSkinSlopeFactor\"f\"lumaAddBackSkySlopeFactor\"f\"lumaAddBackPersonSlopeFactor\"f\"whiteBalanceGains\"\"lscParams\"{?=\"lscScale\"\"lscOffset\"\"lscNormalization\"f\"lscModulationWeight\"f}\"lumaAddbackNoiseVars\"{?=\"readNoiseVariance\"f\"shotNoiseVariance\"f\"normalisedShotNoiseVariance\"f\"normalisedReadNoiseVariance\"f}}"
+ "{?=iffBBB{?=}}16@0:8"
+ "{?=}24@0:816"
+ "{DemosaicNetworkTile=}24@0:816"
+ "{LearnedDemosaicNetworkStageUniforms=\"whiteBalanceGains\"\"isQuadra\"B\"rotateTile180\"B\"lscParams\"{?=\"lscScale\"\"lscOffset\"\"lscNormalization\"f\"lscModulationWeight\"f}\"noiseModelParams\"{?=\"hrGainDownRatio\"f\"noiseVariances\"{?=\"readNoiseVariance\"f\"shotNoiseVariance\"f\"normalisedShotNoiseVariance\"f\"normalisedReadNoiseVariance\"f}\"noiseScaleFactors\"{?=\"lscNoiseFactor\"f\"globalNoiseFactor\"f\"lumaPowerDenomNoiseFactor\"f\"lumaMaxNoiseFactor\"f}}}"
+ "{LearnedDemosaicNetworkStageUniforms=BB{?=ff}{?=f{?=ffff}{?=ffff}}}16@0:8"
+ "{exposureParameters=\"gain\"f\"red_gain\"f\"blue_gain\"f\"red_combo_gain\"f\"blue_combo_gain\"f\"analog_gain\"f\"isp_digital_gain\"f\"isp_digital_gain_prev\"f\"hard_gain\"f\"ltm_soft_gain\"f\"ADRC_exp_gain\"f\"ISOBase\"f\"hr_gain_down_ratio\"f\"exposure_time\"f\"average_focus_score\"f\"normalized_snr\"f\"frame_exposure_bias\"f\"exposure_bias\"f\"rem_exposure_bias\"f\"read_noise_1x\"f\"read_noise_8x\"f\"conversion_gain\"f\"sensor_black_level\"f\"lsModulationWeight\"f\"is_long\"B\"ae_locked\"B\"hr_enabled\"B\"luxLevel\"f\"ltm_locked\"B\"AETargetGain\"f\"face_exp_ratio\"f\"CCT\"f\"quadraBinningFactor\"i\"quadraInverseBinningGainFactor\"f}"
+ "{exposureParameters=ffffffffffffffffffffffffBBBfBfffif}16@0:8"
+ "\xf0\xf0\xf0a"
+ "\xf0\xf0\xf0\xb1"
- "[4@\"<NRFSubProcessor>\"]"
- "\xf0\xf0\xe1"

```
