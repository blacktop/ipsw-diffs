## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-650.0.0.122.4
-  __TEXT.__text: 0x2d9054
-  __TEXT.__auth_stubs: 0xf20
-  __TEXT.__objc_methlist: 0x102d8
-  __TEXT.__const: 0x1027c8
-  __TEXT.__cstring: 0x5a241
-  __TEXT.__gcc_except_tab: 0x198c
-  __TEXT.__oslogstring: 0x4e548
+655.0.0.122.4
+  __TEXT.__text: 0x2dc95c
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x103b8
+  __TEXT.__const: 0x1027b8
+  __TEXT.__cstring: 0x5a9ed
+  __TEXT.__gcc_except_tab: 0x1d08
+  __TEXT.__oslogstring: 0x4f125
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x4d18
-  __TEXT.__objc_classname: 0x2db7
-  __TEXT.__objc_methname: 0x3134c
-  __TEXT.__objc_methtype: 0x15e82
-  __TEXT.__objc_stubs: 0x14dc0
+  __TEXT.__unwind_info: 0x4d38
+  __TEXT.__objc_classname: 0x2dc0
+  __TEXT.__objc_methname: 0x31757
+  __TEXT.__objc_methtype: 0x15ece
+  __TEXT.__objc_stubs: 0x14ee0
   __DATA_CONST.__got: 0xc10
-  __DATA_CONST.__const: 0x12b8
+  __DATA_CONST.__const: 0x1330
   __DATA_CONST.__objc_classlist: 0xc98
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60f0
+  __DATA_CONST.__objc_selrefs: 0x6170
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x9a0
   __DATA_CONST.__objc_arraydata: 0xe40
-  __AUTH_CONST.__auth_got: 0x7a8
+  __AUTH_CONST.__auth_got: 0x7d0
   __AUTH_CONST.__const: 0x7e0
-  __AUTH_CONST.__cfstring: 0x12f20
-  __AUTH_CONST.__objc_const: 0x32558
+  __AUTH_CONST.__cfstring: 0x13060
+  __AUTH_CONST.__objc_const: 0x32808
   __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0xae0
   __AUTH_CONST.__objc_intobj: 0xa50
   __AUTH_CONST.__objc_floatobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH.__objc_data: 0x9b0
-  __DATA.__objc_ivar: 0x34b8
+  __DATA.__objc_ivar: 0x34fc
   __DATA.__data: 0xb48
   __DATA.__common: 0x30
   __DATA.__bss: 0x14

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 402A7122-A9C2-341F-8ADE-0F618CAB0DFD
-  Functions: 12518
-  Symbols:   37732
-  CStrings:  23511
+  UUID: 59E94348-38D0-35BC-916C-B8E06FB9BEA1
+  Functions: 12554
+  Symbols:   37863
+  CStrings:  23630
 
Symbols:
+ +[LensShadingCorrectionConfig getLSCMetadata:lscMetadata:bounds:stageConfigMode:processingOptions:metalCtx:staticParameters:forAWB:].cold.50
+ +[LensShadingCorrectionConfig getLSCMetadata:lscMetadata:bounds:stageConfigMode:processingOptions:metalCtx:staticParameters:forAWB:].cold.51
+ -[CMIPostConfig glassesMask]
+ -[CMIPostConfig setGlassesMask:]
+ -[CMITuningPlist updateWithZoomRatio:]
+ -[DenoiseAndSharpeningPlist readBandData:].cold.33
+ -[DenoiseAndSharpeningPlist readBandData:].cold.34
+ -[DenoiseAndSharpeningPlist readBandData:].cold.35
+ -[DenoiseAndSharpeningPlist readBandData:].cold.36
+ -[DenoiseAndSharpeningPlist readBandData:].cold.37
+ -[DenoiseAndSharpeningPlist updateWithZoomRatio:]
+ -[DenoiseFusePipeline initWithContext:cameraInfo:nrfConfig:dasTuningOptions:toneMappingOptions:tuningParameters:deviceGeneration:].cold.25
+ -[GainValueArray updateWithZoomRatio:]
+ -[H13FastBayerProcStage(HOCLBin) runHOCLBinWithArgs:hoclBinConfig:hoclBinConfigForFlareCorrection:inputTexture:].cold.1
+ -[H13FastBayerProcStage(HOCLBin) runHOCLBinWithArgs:hoclBinConfig:hoclBinConfigForFlareCorrection:inputTexture:].cold.2
+ -[H13FastBayerProcStage(HOCLBin) runHOCLBinWithArgs:hoclBinConfig:hoclBinConfigForFlareCorrection:inputTexture:].cold.3
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:]
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.1
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.10
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.2
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.3
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.4
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.5
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.6
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.7
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.8
+ -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:].cold.9
+ -[LearnedNRProcessor generateGainMapIfNeeded].cold.5
+ -[LearnedNRProcessor prepareDownscaledInputWithBand0:downscaledInputSize:]
+ -[LearnedNRProcessor releaseDownscaledInput]
+ -[LearnedNRProcessor runDemosaicWithInputRawTex:outputImage:frame:completion:]
+ -[LearnedNRProcessor runDemosaicWithInputRawTex:outputImage:frame:completion:].cold.1
+ -[LearnedNRProcessor setupWithOptions:nrfConfig:].cold.12
+ -[NRFPlist updateWithZoomRatio:]
+ -[NRFProcessorInferenceResults lowResGlassesMask]
+ -[NRFProcessorInferenceResults setLowResGlassesMask:]
+ -[NRFProgressiveBracketingFrameParameters evZeroRatio]
+ -[NRFProgressiveBracketingFrameParameters initWithEVZeroRatio:integrationTime:gain:AGC:]
+ -[PostDemosaicTuningParams readPlistChromaSuppression:]
+ -[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:sourceMetadata:demosaicStage:downSampleStage:]
+ -[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:sourceMetadata:demosaicStage:downSampleStage:].cold.1
+ -[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:sourceMetadata:demosaicStage:downSampleStage:].cold.2
+ -[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy].cold.21
+ -[RawDFProxyBoundInferenceResults initWithResult:andMetal:].cold.7
+ -[RawDFProxyBoundInferenceResults lowResGlassesMask]
+ -[RawDFProxyBoundInferenceResults setLowResGlassesMask:]
+ -[RawProcFrames nRegisteredFrames]
+ -[RawProcFrames referenceFrameUniqueId]
+ -[RawProcFrames setNRegisteredFrames:]
+ -[RawProcFrames setReferenceFrameUniqueId:]
+ -[RawProcFrames setReferenceFrameUniqueId:].cold.1
+ -[RawProcFrames setReferenceFrameUniqueId:].cold.2
+ -[RawProcInputFrame allocateAndDemosaicLTMIn:]
+ -[RawProcInputFrame allocateAndDemosaicLTMIn:].cold.1
+ -[RawProcInputFrame allocateAndDemosaicLTMIn:].cold.2
+ -[RawProcInputFrame allocateAndDemosaicLTMIn:].cold.3
+ -[RawProcInputFrame ltmInDraftDemosaicRGBTexture]
+ -[RawProcInputFrame releaseLTMInTex]
+ -[SoftLTM computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:validBufferRect:]
+ -[SoftLTM computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:validBufferRect:].cold.1
+ -[SoftLTM computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:validBufferRect:].cold.2
+ -[SubjectRelightingShaders initWithMetalContext:].cold.12
+ -[SubjectRelightingShaders initWithMetalContext:].cold.13
+ -[SubjectRelightingShaders initWithMetalContext:].cold.14
+ -[SubjectRelightingShaders initWithMetalContext:].cold.15
+ -[SubjectRelightingShaders initWithMetalContext:].cold.16
+ -[SubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:glassesMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:]
+ -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:]
+ -[ToneMapSmoothingResources initWithMetalContext:width:height:mtlSubAllocatorID:srlVersion:].cold.10
+ -[ToneMapSmoothingResources skinMedianIPT]
+ -[ToneMappingShaders initWithMetal:].cold.18
+ -[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:skinMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:iptSkinMedian:]
+ -[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:skinMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:iptSkinMedian:].cold.1
+ -[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:skinMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:iptSkinMedian:].cold.2
+ GCC_except_table46
+ _FigGetUpTime
+ _OBJC_IVAR_$_BandDataDAS.chromaDenoiseMixingCoeffZoom
+ _OBJC_IVAR_$_BandDataDAS.lumaDenoiseMixingCoeffStaticSceneZoom
+ _OBJC_IVAR_$_BandDataDAS.lumaDenoiseMixingCoeffZoom
+ _OBJC_IVAR_$_BandDataDAS.lumaSharpeningScalingOnSkinZoom
+ _OBJC_IVAR_$_BandDataDAS.lumaSharpeningScalingOnSkyZoom
+ _OBJC_IVAR_$_CMIPostConfig._glassesMask
+ _OBJC_IVAR_$_DenoiseFusePipeline._rawDFDownsampleStage
+ _OBJC_IVAR_$_LearnedNRNetworkPreANEStage._metal
+ _OBJC_IVAR_$_LearnedNRProcessor._downscaledInput
+ _OBJC_IVAR_$_LearnedNRProcessor._rawDFDownsampleStage
+ _OBJC_IVAR_$_NRFProcessorInferenceResults._lowResGlassesMask
+ _OBJC_IVAR_$_NRFProgressiveBracketingFrameParameters._evZeroRatio
+ _OBJC_IVAR_$_RawDFProxyBoundInferenceResults._lowResGlassesMask
+ _OBJC_IVAR_$_RawProcInputFrame._ltmInDraftDemosaicRGBTexture
+ _OBJC_IVAR_$_SubjectRelightingShaders._srlV4Apply
+ _OBJC_IVAR_$_SubjectRelightingShaders._srlV4CalcCoefficients
+ _OBJC_IVAR_$_SubjectRelightingShaders._srlV4CalcPostSRLStats
+ _OBJC_IVAR_$_SubjectRelightingShaders._srlV4FaceHistogram
+ _OBJC_IVAR_$_SubjectRelightingShaders._srlV4GlobalHistogram
+ _OBJC_IVAR_$_ToneMapSmoothingResources._skinMedianIPT
+ _OBJC_IVAR_$_ToneMappingBuffers.glassesMask
+ _OBJC_IVAR_$_ToneMappingPlist.srlv4
+ _OBJC_IVAR_$_ToneMappingShaders._ltmApply
+ _OBJC_IVAR_$_ToneMappingShaders._ltmApplyBG
+ _OUTLINED_FUNCTION_45
+ ___274-[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:skinMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:iptSkinMedian:]_block_invoke
+ ___274-[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:skinMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:iptSkinMedian:]_block_invoke_2
+ ___33-[LearnedNRProcessor runPipeline]_block_invoke
+ ___394-[SubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:glassesMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:]_block_invoke
+ ___394-[SubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:glassesMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:]_block_invoke_2
+ ___58-[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy]_block_invoke.275
+ ___90-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:]_block_invoke
+ ___90-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:]_block_invoke.275
+ ___90-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:]_block_invoke_2
+ ___block_descriptor_48_e8_32r40r_e8_v12?0i8lr32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e8_v12?0i8ls32l8s40l8
+ ___block_literal_global.146
+ ___block_literal_global.162
+ ___block_literal_global.164
+ ___block_literal_global.166
+ ___block_literal_global.169
+ ___block_literal_global.171
+ ___block_literal_global.178
+ ___block_literal_global.180
+ ___block_literal_global.217
+ ___block_literal_global.219
+ ___block_literal_global.239
+ ___block_literal_global.241
+ ___block_literal_global.337
+ ___destructor_8_s0_s8_s16_s24_s32
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_wait
+ _kAMBNR_ChromaDenoiseMixingCoeffZoom
+ _kAMBNR_LumaDenoiseMixingCoeffStaticSceneZoom
+ _kAMBNR_LumaDenoiseMixingCoeffZoom
+ _kAMBNR_LumaSharpeningScalingOnSkinZoom
+ _kAMBNR_LumaSharpeningScalingOnSkyZoom
+ _objc_msgSend$_runSubjectRelighting:luma:chroma:skinMask:personMask:glassesMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:
+ _objc_msgSend$computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:validBufferRect:
+ _objc_msgSend$createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:sourceMetadata:demosaicStage:downSampleStage:
+ _objc_msgSend$glassesMask
+ _objc_msgSend$initWithEVZeroRatio:integrationTime:gain:AGC:
+ _objc_msgSend$lowResGlassesMask
+ _objc_msgSend$ltmInDraftDemosaicRGBTexture
+ _objc_msgSend$mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:skinMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:iptSkinMedian:
+ _objc_msgSend$nRegisteredFrames
+ _objc_msgSend$prepareDownscaledInputWithBand0:downscaledInputSize:
+ _objc_msgSend$processSFDForInputTexture:outLuma:outChroma:renderROI:completion:
+ _objc_msgSend$readPlistChromaSuppression:
+ _objc_msgSend$releaseDownscaledInput
+ _objc_msgSend$releaseLTMInTex
+ _objc_msgSend$runDemosaicWithInputRawTex:outputImage:frame:completion:
+ _objc_msgSend$runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:
+ _objc_msgSend$setGlassesMask:
+ _objc_msgSend$setReferenceFrameUniqueId:
+ _objc_msgSend$skinMedianIPT
+ _objc_msgSend$updateWithZoomRatio:
- -[DenoiseFusePipeline doGainMap:properties:output:outputHeadroom:nrfPlist:useFusedFrame:processingType:].cold.8
- -[DenoiseFusePipeline doGainMap:properties:output:outputHeadroom:nrfPlist:useFusedFrame:processingType:].cold.9
- -[DenoiseFusePipeline toneMapBandFrame:properties:sourceFrameType:sourceFrameIndex:ltcFrameIndex:gtcFrameIndex:nrfPlist:].cold.10
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:]
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.1
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.10
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.2
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.3
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.4
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.5
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.6
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.7
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.8
- -[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:].cold.9
- -[LearnedNRProcessor prepareBand1InputWithBand0:]
- -[LearnedNRProcessor runDemosaicWithInputRawTex:outputImage:frame:]
- -[LearnedNRProcessor runDemosaicWithInputRawTex:outputImage:frame:].cold.1
- -[LearnedNRProcessor runPipeline].cold.1
- -[LearnedNRProcessor runPipeline].cold.2
- -[LearnedNRProcessor runPipeline].cold.3
- -[LearnedNRProcessor runPipeline].cold.4
- -[LearnedNRProcessor runPipeline].cold.5
- -[LearnedNRProcessor runPipeline].cold.6
- -[LearnedNRProcessor runPipeline].cold.7
- -[LearnedNRProcessor runSemanticInferences].cold.3
- -[NRFProgressiveBracketingFrameParameters initWithIntegrationTime:gain:AGC:]
- -[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:gainMap:band0GainMapSourceTexture:outputGainMapSize:sourceMetadata:demosaicStage:downSampleStage:]
- -[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:gainMap:band0GainMapSourceTexture:outputGainMapSize:sourceMetadata:demosaicStage:downSampleStage:].cold.1
- -[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:gainMap:band0GainMapSourceTexture:outputGainMapSize:sourceMetadata:demosaicStage:downSampleStage:].cold.2
- -[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:gainMap:band0GainMapSourceTexture:outputGainMapSize:sourceMetadata:demosaicStage:downSampleStage:].cold.3
- -[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:gainMap:band0GainMapSourceTexture:outputGainMapSize:sourceMetadata:demosaicStage:downSampleStage:].cold.4
- -[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:gainMap:band0GainMapSourceTexture:outputGainMapSize:sourceMetadata:demosaicStage:downSampleStage:].cold.5
- -[RawProcFrames referenceFrameIndex]
- -[RawProcFrames setReferenceFrameIndex:]
- -[RawProcFrames setReferenceFrameIndex:].cold.1
- -[RawProcFrames setReferenceFrameIndex:].cold.2
- -[SoftLTM computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:]
- -[SoftLTM computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:].cold.1
- -[SoftLTM computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:].cold.2
- -[SubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]
- -[SubjectRelightingStage runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]
- -[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:]
- -[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:].cold.1
- -[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:].cold.2
- _OBJC_IVAR_$_DeepFusionProcessor._isMeteorPlusPlusEnabled
- _OBJC_IVAR_$_GainMapStage._isMeteorPlusPlusEnabled
- _OBJC_IVAR_$_LearnedNRProcessor._inferenceSourceImg
- _OBJC_IVAR_$_LearnedNRProcessor._nRegisteredFrames
- _OBJC_IVAR_$_NRFConfig._isMeteorPlusPlusEnabled
- _OBJC_IVAR_$_RawDFProcessor._nRegisteredFrames
- _OBJC_IVAR_$_ToneMappingShaders._ltmApplyShaders
- ___251-[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:]_block_invoke
- ___251-[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:]_block_invoke_2
- ___368-[SubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]_block_invoke
- ___368-[SubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]_block_invoke_2
- ___58-[RawDFProcessor _doDeepFusionSytheticRefererenceAndProxy]_block_invoke.273
- ___79-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:]_block_invoke
- ___79-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:]_block_invoke.275
- ___79-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:]_block_invoke_2
- ___block_literal_global.122
- ___block_literal_global.148
- ___block_literal_global.150
- ___block_literal_global.152
- ___block_literal_global.155
- ___block_literal_global.157
- ___block_literal_global.175
- ___block_literal_global.177
- ___block_literal_global.214
- ___block_literal_global.216
- ___block_literal_global.236
- ___block_literal_global.238
- ___block_literal_global.336
- _objc_msgSend$_runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:
- _objc_msgSend$computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:
- _objc_msgSend$createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:gainMap:band0GainMapSourceTexture:outputGainMapSize:sourceMetadata:demosaicStage:downSampleStage:
- _objc_msgSend$initWithIntegrationTime:gain:AGC:
- _objc_msgSend$mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:
- _objc_msgSend$prepareBand1InputWithBand0:
- _objc_msgSend$processSFDForInputTexture:outLuma:outChroma:renderROI:
- _objc_msgSend$runDemosaicWithInputRawTex:outputImage:frame:
- _objc_msgSend$runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:
- _objc_msgSend$runWithInput:output:minThreshold:maxThreshold:inputIsLinear:inputScaling:
- _objc_msgSend$runWithInputDownsampled:output:minThreshold:maxThreshold:inputIsLinear:inputScaling:
CStrings:
+ "! FigCapturePixelFormatHasRegroupedLayout( CVPixelBufferGetPixelFormatType( _rawThumbnailsPixelBuffer ) )"
+ "%@%@"
+ "-[CMITuningPlist updateWithZoomRatio:]"
+ "-[DenoiseAndSharpeningPlist updateWithZoomRatio:]"
+ "-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:completion:]"
+ "-[LearnedNRProcessor finishProcessing]"
+ "-[LearnedNRProcessor prepareDownscaledInputWithBand0:downscaledInputSize:]"
+ "-[LearnedNRProcessor runDemosaicWithInputRawTex:outputImage:frame:completion:]"
+ "-[NRFPlist updateWithZoomRatio:]"
+ "-[PostDemosaicTuningParams readPlistChromaSuppression:]"
+ "-[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:sourceMetadata:demosaicStage:downSampleStage:]"
+ "-[RawProcFrames setReferenceFrameUniqueId:]"
+ "-[RawProcInputFrame allocateAndDemosaicLTMIn:]"
+ "-[SubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:glassesMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:]"
+ "-[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:skinMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:iptSkinMedian:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Failed to allocate %{public}@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: Failed to init RawDFDownsampleStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: downSample simpleResampleWithInputTex chroma %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: downSample simpleResampleWithInputTex luma %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: found no matching pyramidLevel to use for toneMapBandFrame"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: DAS failed to update with zoom on err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Skipping update tuning with zoom, zoomRatio: %.2f,  updateTuningWithZoom Default: %@"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: Unexpected zoomRatio of %.2f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: ev0 DAS failed to update with zoom on err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/NRFOptionsV4.m %s: evm DAS failed to update with zoom on err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: Failed to init RawDFDownsampleStage"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: It's unfortuate that we need to downscale the input Band0 second time for generating the GainMap, please look into it."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: LearnedNRProcessor unexpected wait for network status, added Wait is = %.2f msecs"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: LearnedNRProcessor wait timed out"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: This is NOT a band1 downscale, resampling..."
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _downscaledInput not set right for gainMap"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _downscaledInput not set right for inferences"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _learnedNRNetworkStage failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: _learnedNRNetworkStage getFinalProcessingStatus failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: downSample simpleResampleWithInputTex chroma %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: downSample simpleResampleWithInputTex luma %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: inf or gainmap requested"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: learnedNRNetworkStage getFinalProcessingStatus (finish) status error (%d)"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: learnedNRNetworkStatus == nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: prepareDownscaledInputWithBand0 for GainMap failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: prepareDownscaledInputWithBand0 for Inferences failed with err = %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: processingType = %{public}d, numBracketsFused=%{public}d, nRegisteredFrames=%{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/PlistCommonV4.m %s: Empty implementation - NO OP"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/AMBNR/AMBNRPlistV4.m %s: Unexpected zoomRatio of %.2f"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/ToneMapping/ToneMappingPlistV4.m %s: Error: SRLv4 is selected but MSTMv2 parameters are missing in tuning plist"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: GTC ltm is NOT available"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: LTC ltm is NOT available"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: Setting referenceFrameIndex: %d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: processingType = %{public}d, numBracketsFused=%{public}d, nRegisteredFrames=%{public}d"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: Unexpected regwarpDims (0,0) "
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: cachedTexture %@ nil"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawProc/RawProcInputFrameV4.m %s: td nil"
+ "<<<< DeepFusionProcessor (NRF) >>>> %s: glassesMask is nil"
+ "<<<< RawProcFrames >>>> %s: Adding Reference frame input to inputFrames UniqueId: %d, _referenceFrameIndex: %d"
+ "<<<< RawProcFrames >>>> %s: _referenceFrameUniqueId %d is matched with _referenceFrameIndex %d"
+ "<<<< RawProcFrames >>>> %s: referenceFrameUniqueId cannot be set to a negative value"
+ "<<<< RawProcFrames >>>> %s: registration failed at setReferenceFrameUniqueId"
+ "@40@0:8d16d24f32i36"
+ "@56@0:8@16@24B32B36@40@48"
+ "CIC data may be corrupted"
+ "ChromaDenoiseMixingCoeffZoom"
+ "Double-height thumbnails with 'Interchange' format (regrouped layout) are not expected."
+ "Failed to create inputTexCopy texture"
+ "LSC data may be corrupted"
+ "LumaDenoiseMixingCoeffStaticSceneZoom"
+ "LumaDenoiseMixingCoeffZoom"
+ "LumaSharpeningScalingOnSkinZoom"
+ "LumaSharpeningScalingOnSkyZoom"
+ "SRLv4"
+ "T@\"<MTLBuffer>\",R,N,V_skinMedianIPT"
+ "T@\"<MTLTexture>\",&,N,V_glassesMask"
+ "T@\"<MTLTexture>\",&,N,V_lowResGlassesMask"
+ "T@\"<MTLTexture>\",R,N,V_ltmInDraftDemosaicRGBTexture"
+ "T^{__CVBuffer=},&,N,V_lowResGlassesMask"
+ "Td,R,N,V_evZeroRatio"
+ "Ti,N,V_nRegisteredFrames"
+ "Ti,N,V_referenceFrameUniqueId"
+ "\\d+(?:\\.\\d+)?"
+ "_blackSubtractAndAddingContrast is NULL"
+ "_calculateBlackWhiteStrengthCenter is NULL"
+ "_downscaledInput"
+ "_evZeroRatio"
+ "_glassesMask"
+ "_lowResGlassesMask"
+ "_lowResGlassesMask is NULL"
+ "_ltmApply"
+ "_ltmApply is NULL"
+ "_ltmApplyBG"
+ "_ltmApplyBG is NULL"
+ "_ltmInDraftDemosaicRGBTexture"
+ "_mstmCombineAndDownsampleMask is NULL"
+ "_mstmDiffusionEven is NULL"
+ "_mstmDiffusionOdd is NULL"
+ "_mstmDownsampleInitial is NULL"
+ "_mstmDownsampleMask is NULL"
+ "_mstmDownsampleSubsequent is NULL"
+ "_mstmPyramidRemixFinal is NULL"
+ "_mstmPyramidRemixIntermediate is NULL"
+ "_mstmV2First is NULL"
+ "_mstmV2Second is NULL"
+ "_mstmsApply is NULL"
+ "_runSubjectRelighting:luma:chroma:skinMask:personMask:glassesMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:"
+ "_sffFillFace is NULL"
+ "_sffTestFace is NULL"
+ "_skinMedianIPT"
+ "_skinMedianIPT is NULL"
+ "_srlV4Apply"
+ "_srlV4CalcCoefficients"
+ "_srlV4CalcPostSRLStats"
+ "_srlV4FaceHistogram"
+ "_srlV4GlobalHistogram"
+ "allocateAndDemosaicLTMIn:"
+ "bandDAS->chromaDenoiseMixingCoeffZoom = [[GainValueArray alloc] initWithArray:pairsArray]"
+ "bandDAS->lumaDenoiseMixingCoeffStaticSceneZoom = [[GainValueArray alloc] initWithArray:pairsArray]"
+ "bandDAS->lumaDenoiseMixingCoeffZoom = [[GainValueArray alloc] initWithArray:pairsArray]"
+ "bandDAS->lumaSharpeningScalingOnSkinZoom = [[GainValueArray alloc] initWithArray:pairsArray]"
+ "bandDAS->lumaSharpeningScalingOnSkyZoom = [[GainValueArray alloc] initWithArray:pairsArray]"
+ "bypassValidation || cicGridData.length == cicDataSize"
+ "bypassValidation || lscGridData.length == lscDataSize"
+ "chromaDenoiseMixingCoeffZoom"
+ "cicGridData.length >= sizeof( FigCaptureStreamLSCQuadraChannelImbalanceCorrectionGainGridVersion ) + sizeof( FigCaptureStreamLSCQuadraChannelImbalanceCorrectionGainGridVersion1 )"
+ "computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:validBufferRect:"
+ "createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:sourceMetadata:demosaicStage:downSampleStage:"
+ "draftDemDims.x > 0 && draftDemDims.y > 0"
+ "evZeroRatio"
+ "glassesMask"
+ "h13f.bayerProc.inputTexCopy"
+ "i140@0:8@16@24@32@40@48@56@64@72@80f88B92f96@100@108f116f120B124f128@132"
+ "i228@0:8i16@20@28@36@44@52@60@68@76{CGRect={CGPoint=dd}{CGSize=dd}}84f116f120i124^{?=fffffffffBffffffffffffBffffff}128@136@144@152Q160[10{?={CGRect={CGPoint=dd}{CGSize=dd}}SSS}]168B176B180f184@188@196@204@212@220"
+ "i32@0:8@16^{InferenceResultsBindings=@@@@@}24"
+ "i364@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128{CGRect={CGPoint=dd}{CGSize=dd}}136f168f172i176Q180[10{?={CGRect={CGPoint=dd}{CGSize=dd}}SSS}]188B196B200f204{?=fffffffffBffffffffffffBffffff}208@324@332@340@348@356"
+ "i48@0:8@16@24@32@?40"
+ "i64@0:8@16@2432@40@48@56"
+ "i96@0:8@16@24@32{?={?=QQQ}{?=QQQ}}40@?88"
+ "initWithEVZeroRatio:integrationTime:gain:AGC:"
+ "iptSkinMedianBuffer"
+ "kSoftISPProcessorError_LSCIncorrectDataSize"
+ "kSoftISPProcessorError_QuadraCICIncorrectDataSize"
+ "lowResGlassesMask"
+ "ltmInDraftDemosaicRGBTexture"
+ "lumaDenoiseMixingCoeffStaticSceneZoom"
+ "lumaDenoiseMixingCoeffZoom"
+ "lumaSharpeningScalingOnSkinZoom"
+ "lumaSharpeningScalingOnSkyZoom"
+ "mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:skinMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:iptSkinMedian:"
+ "nRegisteredFrames"
+ "prepareDownscaledInputWithBand0:downscaledInputSize:"
+ "processSFDForInputTexture:outLuma:outChroma:renderROI:completion:"
+ "readPlistChromaSuppression:"
+ "referenceFrameUniqueId"
+ "releaseDownscaledInput"
+ "releaseLTMInTex"
+ "runDemosaicWithInputRawTex:outputImage:frame:completion:"
+ "runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:glassesMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:iptSkinMedian:"
+ "setGlassesMask:"
+ "setLowResGlassesMask:"
+ "setNRegisteredFrames:"
+ "setReferenceFrameUniqueId:"
+ "skinMedianIPT"
+ "srlV4Apply"
+ "srlV4CalcCoefficients"
+ "srlV4CalcPostSRLStats"
+ "srlV4FaceSparseHistogram"
+ "srlV4GlobalSparseHistogram"
+ "srlv4"
+ "updateWithZoomRatio:"
+ "v24@0:8^{InferenceResultsBindings=@@@@@}16"
+ "v4"
+ "zoomRatio > 0"
+ "{InferenceResultsBindings=\"skinMask\"@\"<MTLTexture>\"\"skyMask\"@\"<MTLTexture>\"\"personMask\"@\"<MTLTexture>\"\"instanceMasks\"@\"NSArray\"\"glassesMask\"@\"<MTLTexture>\"}"
+ "\xf0\xf0Q"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xe1"
+ "\xf0\xf0\xf0\xf1"
- "( -73300 )"
- "( width <= inputTex.width ) && ( height <= inputTex.height )"
- "-[LearnedNRNetworkStage processSFDForInputTexture:outLuma:outChroma:renderROI:]"
- "-[LearnedNRProcessor prepareBand1InputWithBand0:]"
- "-[LearnedNRProcessor runDemosaicWithInputRawTex:outputImage:frame:]"
- "-[RawDFCommon createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:gainMap:band0GainMapSourceTexture:outputGainMapSize:sourceMetadata:demosaicStage:downSampleStage:]"
- "-[RawProcFrames setReferenceFrameIndex:]"
- "-[SubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]"
- "-[ToneMappingStage mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:]"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: DenoiseFusePipelineV4 goGainMap calling gainmap runWithInput"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: DenoiseFusePipelineV4 goGainMap setup for V3 gainmap"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: DenoiseFusePipelineV4 goGainMapOnSingleFrameLuma calling gainmap runWithInputDownsampled"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/IBP/DenoiseFusePipelineV4.m %s: _gainMapStage runWithInput failed, bailing (%d)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: inferenceSourceImg not set right"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: prepareBand1InputWithBand0 failed with err = %d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRProcessorV4.m %s: processingType = %{public}d, numBracketsFused=%{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/Tuning/LearnedNRTuningV4.m %s: entryParams semStylesPlist is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: RawDFProcessorV4 _doDeepFusionSytheticReferenceAndProxy calling gainmap runWithInput"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: _gainMapStage runWithInput failed, bailing (%d)"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: gainMapSourceImg is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: input lumaTex for gainMap is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/RawDFProcessorV4.m %s: processingType = %{public}d, numBracketsFused=%{public}d"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %s: entryParams SemStyles is nil"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %s: entryParams semStylesPlist is nil"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: DeepFusionProcessorV4 generateSyntheticReference calling gainmap runWithInput"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: _gainMapStage runWithInput failed, bailing (%d)"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: gainMapSourceImg is nil"
- "<<<< DeepFusionProcessor (NRF) >>>> %s: input lumaTex for gainMap is nil"
- "<<<< RawDFCommon >>>> %s: createSourceTexturesForInference: textures are NOT the same size."
- "<<<< RawDFCommon >>>> %s: outputGainMapSource must not be nil"
- "<<<< RawDFCommon >>>> %s: resampleWithInputTex should be used for smaller downscale ratios"
- "<<<< RawProcFrames >>>> %s: Adding Reference frame input to inputFrames %d"
- "<<<< RawProcFrames >>>> %s: referenceFrameIndex cannot be set to a negative value"
- "<<<< RawProcFrames >>>> %s: registration failed at setReferenceFrameIndex"
- "@32@0:8d16f24i28"
- "@48@0:8@16@24B32B36@40"
- "LTC ltm is NOT available"
- "ToneMappingV4::FunctionConstants"
- "_fusionConf.ltcFrameIndex >= 0 && _inputFrames.frames[_fusionConf.ltcFrameIndex].properties.meta.metadataHasLtmCurves"
- "_inferenceSourceImg"
- "_isMeteorPlusPlusEnabled"
- "_ltmApplyShaders"
- "_runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:"
- "bilateralGridOn"
- "cicGridData.length >= sizeof( FigCaptureStreamLSCQuadraChannelImbalanceCorrectionGainGrid )"
- "computeLTM:metadata:applyCCM:hasHRGainDownApplied:inputBufferRect:"
- "createSourceTexturesForInference:band0InferenceSourceTexture:outputInferenceSize:gainMap:band0GainMapSourceTexture:outputGainMapSize:sourceMetadata:demosaicStage:downSampleStage:"
- "i124@0:8@16@24@32@40@48@56@64@72f80B84f88@92@100f108f112B116f120"
- "i212@0:8i16@20@28@36@44@52@60@68{CGRect={CGPoint=dd}{CGSize=dd}}76f108f112i116^{?=fffffffffBffffffffffffBffffff}120@128@136@144Q152[10{?={CGRect={CGPoint=dd}{CGSize=dd}}SSS}]160B168B172f176@180@188@196@204"
- "i32@0:8@16^{InferenceResultsBindings=@@@@}24"
- "i348@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120{CGRect={CGPoint=dd}{CGSize=dd}}128f160f164i168Q172[10{?={CGRect={CGPoint=dd}{CGSize=dd}}SSS}]180B188B192f196{?=fffffffffBffffffffffffBffffff}200@316@324@332@340"
- "i88@0:8@16@2432@40@4856@64@72@80"
- "i88@0:8@16@24@32{?={?=QQQ}{?=QQQ}}40"
- "initWithIntegrationTime:gain:AGC:"
- "input and output width are different"
- "input texture is nil"
- "ltcGridOverlayOn"
- "mstmsApplyLumaGain:inputLuma:inputChroma:intermediateChroma:outputChroma:localGainMap:gammaCurve:personMask:chromaGainAdjPower:inputIsLinear:chromaBias:blackPoint:playbackCurve:saturationControl:frameGain:firstPass:hrGainDownRatio:"
- "nrf.has_flicker"
- "prepareBand1InputWithBand0:"
- "processSFDForInputTexture:outLuma:outChroma:renderROI:"
- "runDemosaicWithInputRawTex:outputImage:frame:"
- "runSubjectRelightingVersion:toneMap:luma:chroma:ltmChroma:skinMask:personMask:instanceMask0:instanceMask1:instanceMask2:instanceMask3:gammaCurve:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:srlV2Plist:mstmParams:mstmSRLParams:blackPoint:playBackCurve:"
- "spatialCCMGridOverlayOn"
- "v24@0:8^{InferenceResultsBindings=@@@@}16"
- "{InferenceResultsBindings=\"skinMask\"@\"<MTLTexture>\"\"skyMask\"@\"<MTLTexture>\"\"personMask\"@\"<MTLTexture>\"\"instanceMasks\"@\"NSArray\"}"
- "\xf0\xf0A"
- "\xf0\xf0\xf0\xe1"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc1"

```
