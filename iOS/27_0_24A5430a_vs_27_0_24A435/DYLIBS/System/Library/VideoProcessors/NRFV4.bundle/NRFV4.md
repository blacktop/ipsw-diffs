## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

 764.22.13.0.0
-  __TEXT.__text: 0x25b84c
-  __TEXT.__objc_methlist: 0x13110
-  __TEXT.__const: 0x1031e0
-  __TEXT.__cstring: 0x3461a
-  __TEXT.__gcc_except_tab: 0x1680
-  __TEXT.__oslogstring: 0x209f4
+  __TEXT.__text: 0x27c54c
+  __TEXT.__objc_methlist: 0x14718
+  __TEXT.__const: 0x103260
+  __TEXT.__cstring: 0x36baa
+  __TEXT.__oslogstring: 0x21e64
+  __TEXT.__gcc_except_tab: 0x1850
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x5130
+  __TEXT.__unwind_info: 0x54d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1490
-  __DATA_CONST.__objc_classlist: 0xe38
-  __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x108
+  __DATA_CONST.__const: 0x14d8
+  __DATA_CONST.__objc_classlist: 0xf28
+  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x110
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f88
+  __DATA_CONST.__objc_selrefs: 0x77f0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0xb08
-  __DATA_CONST.__objc_arraydata: 0xf08
-  __DATA_CONST.__got: 0xf08
-  __AUTH_CONST.__const: 0x9a0
-  __AUTH_CONST.__cfstring: 0x146e0
-  __AUTH_CONST.__objc_const: 0x3b9c0
+  __DATA_CONST.__objc_superrefs: 0xbe8
+  __DATA_CONST.__objc_arraydata: 0xfe0
+  __DATA_CONST.__got: 0xf90
+  __AUTH_CONST.__const: 0x9c0
+  __AUTH_CONST.__cfstring: 0x15cc0
+  __AUTH_CONST.__objc_const: 0x40208
+  __AUTH_CONST.__objc_floatobj: 0x140
   __AUTH_CONST.__objc_doubleobj: 0xa0
-  __AUTH_CONST.__objc_arrayobj: 0xc30
-  __AUTH_CONST.__objc_intobj: 0xa20
-  __AUTH_CONST.__objc_floatobj: 0x90
+  __AUTH_CONST.__objc_arrayobj: 0xd68
+  __AUTH_CONST.__objc_intobj: 0xa38
   __AUTH_CONST.__objc_dictobj: 0x500
-  __AUTH_CONST.__auth_got: 0x868
-  __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x3f8c
-  __DATA.__data: 0xc68
-  __DATA.__common: 0x40
-  __DATA_DIRTY.__objc_data: 0x83e0
+  __AUTH_CONST.__auth_got: 0x880
+  __AUTH.__objc_data: 0x1220
+  __DATA.__objc_ivar: 0x4420
+  __DATA.__data: 0xcc8
+  __DATA.__common: 0x44
+  __DATA_DIRTY.__objc_data: 0x8570
   __DATA_DIRTY.__bss: 0x178
   __DATA_DIRTY.__common: 0xf8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 14435
-  Symbols:   17850
-  CStrings:  8544
+  Functions: 15236
+  Symbols:   19070
+  CStrings:  8999
 
Symbols:
+ +[FlareSourceDetector prewarmShaders:tuningParameters:]
+ +[FlareSourceDetectorInputFrame inputFrameAdaptingFrame:]
+ +[FlareSourceDetectorPlist initialize]
+ +[LCBCorrection prewarmWithMetalContext:]
+ +[LCBDetector prewarmWithMetalContext:]
+ +[LCBExtractor prewarmWithMetalContext:]
+ +[LCBFiltering prewarmWithMetalContext:]
+ +[LCBMitigation prewarmWithMetalContext:]
+ +[LCBPyramid prewarmWithMetalContext:]
+ +[UDNet prewarmShaders:]
+ +[UDNetNetworkStage prewarmShaders:]
+ +[UDNetPlist initialize]
+ -[CMILCBDatabase(TransformedEntry) transformedEntriesOnPyramidLevelWithConfig:]
+ -[CMILCBEntry(TransformedEntry) transformedToConfig:]
+ -[CMIPost setupUDNet:isQuadra:]
+ -[CMIPostConfig cameraInfoByPortType]
+ -[CMIPostConfig inputLSCMetadata]
+ -[CMIPostConfig inputLSCTexture]
+ -[CMIPostConfig inputMetadata]
+ -[CMIPostConfig setCameraInfoByPortType:]
+ -[CMIPostConfig setInputLSCMetadata:]
+ -[CMIPostConfig setInputLSCTexture:]
+ -[CMIPostConfig setInputMetadata:]
+ -[CMIPostConfig setUdNetPlist:]
+ -[CMIPostConfig udNetPlist]
+ -[FlareSourceDetector .cxx_destruct]
+ -[FlareSourceDetector getDetectionResultSync:]
+ -[FlareSourceDetector initWithMetalContext:error:]
+ -[FlareSourceDetector inputType]
+ -[FlareSourceDetector setInputType:]
+ -[FlareSourceDetector setTuningPlist:]
+ -[FlareSourceDetector startDetectionOnEv0:]
+ -[FlareSourceDetector tuningPlist]
+ -[FlareSourceDetectorInputFrame .cxx_destruct]
+ -[FlareSourceDetectorInputFrame auxDraftDemosaicLumaTexture]
+ -[FlareSourceDetectorInputFrame auxDraftDemosaicRGBTexture]
+ -[FlareSourceDetectorInputFrame baseTex]
+ -[FlareSourceDetectorInputFrame lscGainMapTexture]
+ -[FlareSourceDetectorInputFrame properties]
+ -[FlareSourceDetectorInputFrame setAuxDraftDemosaicLumaTexture:]
+ -[FlareSourceDetectorInputFrame setAuxDraftDemosaicRGBTexture:]
+ -[FlareSourceDetectorInputFrame setBaseTex:]
+ -[FlareSourceDetectorInputFrame setLscGainMapTexture:]
+ -[FlareSourceDetectorInputFrame setProperties:]
+ -[FlareSourceDetectorPlist .cxx_destruct]
+ -[FlareSourceDetectorPlist init]
+ -[FlareSourceDetectorPlist readPlist:]
+ -[H13FastBayerProcConfig(LCB) getLCBConfigForInputFrame:bounds:awb:]
+ -[H13FastBayerProcConfig(LCB) getLCBEnabledForInputFrame:processingOptions:lcbEnabled:]
+ -[LCBBlock .cxx_destruct]
+ -[LCBBlock createMetalBuffer:length:]
+ -[LCBBlock createMetalTexture:pixelFormat:width:height:]
+ -[LCBBlock initWithMetalContext:]
+ -[LCBBlock metalContext]
+ -[LCBBlockShaders .cxx_destruct]
+ -[LCBBlockShaders initWithMetalContext:]
+ -[LCBBlockShaders metalContext]
+ -[LCBConfig apertureRatio]
+ -[LCBConfig bayerSensorDimensions]
+ -[LCBConfig captureGravityVector]
+ -[LCBConfig captureTimeStamp]
+ -[LCBConfig clippingThreshold]
+ -[LCBConfig correctionEnabled]
+ -[LCBConfig darkPixelThreshold]
+ -[LCBConfig databaseUpdateEnabled]
+ -[LCBConfig defocusRadiusForIRCF]
+ -[LCBConfig defocusRadiusForLens]
+ -[LCBConfig defocusRadiusOffsetForIRCF]
+ -[LCBConfig defocusRadiusOffsetForLens]
+ -[LCBConfig defocusRadiusSlopeForIRCF]
+ -[LCBConfig defocusRadiusSlopeForLens]
+ -[LCBConfig detectionEnabled]
+ -[LCBConfig detectionLocalityThreshold]
+ -[LCBConfig detectionScoreDarkLower]
+ -[LCBConfig detectionScoreDarkUpper]
+ -[LCBConfig detectionScoreEdgeLower]
+ -[LCBConfig detectionScoreEdgeUpper]
+ -[LCBConfig detectionScoreImprovementLower]
+ -[LCBConfig detectionScoreImprovementUpper]
+ -[LCBConfig dimensionsForPyramidLevel:]
+ -[LCBConfig extractionEnabled]
+ -[LCBConfig firstPixel]
+ -[LCBConfig firstPyramidLevel]
+ -[LCBConfig focusLensPosition]
+ -[LCBConfig getCorrectionConfig:]
+ -[LCBConfig getDetectionExtractionConfig:forPyramidLevel:]
+ -[LCBConfig getPerFrameFilteringConfig:]
+ -[LCBConfig getPyramidConfig:]
+ -[LCBConfig getTemporalFilteringConfig:]
+ -[LCBConfig initWithTuningParameters:frameMetadata:cameraInfo:inputOffsetWithinSensorInBayerPixels:inputDimensionsInBayerPixels:cfaLayout:firstPixel:enableDetection:enableCorrection:awb:]
+ -[LCBConfig innerOuterVarEdgeLower]
+ -[LCBConfig innerOuterVarEdgeUpper]
+ -[LCBConfig inputDimensionsInBayerPixels]
+ -[LCBConfig inputOffsetInBayerPixels]
+ -[LCBConfig inputPyramidEnabled]
+ -[LCBConfig invertedAWBGains]
+ -[LCBConfig isQuadra]
+ -[LCBConfig lastPyramidLevel]
+ -[LCBConfig lowPassNPyramidLevels]
+ -[LCBConfig lumaConversionCoefficients]
+ -[LCBConfig maxCorrectionFeaturesUpdateAmount]
+ -[LCBConfig maxDetectionCount]
+ -[LCBConfig maxRadiusUpdateDecrement]
+ -[LCBConfig maxRadiusUpdateIncrement]
+ -[LCBConfig maximumCorrectionScaling]
+ -[LCBConfig maximumDetectionScoreForNoLCB]
+ -[LCBConfig maximumNumberOfCorrectionsPerLevel]
+ -[LCBConfig maximumNumberOfDetectionsPerLevel]
+ -[LCBConfig maximumNumberOfExtractionsPerLevel]
+ -[LCBConfig minCorrectionFeaturesLearningRate]
+ -[LCBConfig minimumConfidence]
+ -[LCBConfig minimumCorrectionScaling]
+ -[LCBConfig minimumDetectionCountForCorrection]
+ -[LCBConfig minimumDetectionScoreForLCB]
+ -[LCBConfig minimumGravityVectorChange]
+ -[LCBConfig minimumTimeDelta]
+ -[LCBConfig nPyramidLevels]
+ -[LCBConfig notStrongEdgeConfidenceLower]
+ -[LCBConfig notStrongEdgeConfidenceUpper]
+ -[LCBConfig notTooDarkConfidenceLower]
+ -[LCBConfig notTooDarkConfidenceScaling]
+ -[LCBConfig notTooDarkConfidenceUpper]
+ -[LCBConfig oisShiftScalingFactorForIRCF]
+ -[LCBConfig oisShiftScalingFactorForLens]
+ -[LCBConfig oisShift]
+ -[LCBConfig opticalCenterForIRCF]
+ -[LCBConfig opticalCenterForLens]
+ -[LCBConfig particleDistanceForIRCF]
+ -[LCBConfig particleDistanceForLens]
+ -[LCBConfig particleDistanceOffsetForIRCF]
+ -[LCBConfig particleDistanceOffsetForLens]
+ -[LCBConfig particleDistanceSlopeForIRCF]
+ -[LCBConfig particleDistanceSlopeForLens]
+ -[LCBConfig perFrameFilteringEnabled]
+ -[LCBConfig positionUpdateRate]
+ -[LCBConfig radiusLearningRate]
+ -[LCBConfig relativeToLensRadiusThreshold]
+ -[LCBConfig residualConfidenceDetailLower]
+ -[LCBConfig residualConfidenceDetailUpper]
+ -[LCBConfig residualConfidenceInOutVarLower]
+ -[LCBConfig residualConfidenceInOutVarUpper]
+ -[LCBConfig skipPyrLevel0]
+ -[LCBConfig useFullColor]
+ -[LCBCorrection .cxx_destruct]
+ -[LCBCorrection applyCorrectionMap:toRawFrame:config:error:]
+ -[LCBCorrection createCorrectionMapForLevel:filteredLCBsForLevel:correctionLUT:previousLevel:config:error:]
+ -[LCBCorrection initWithMetalContext:]
+ -[LCBCorrectionShaders .cxx_destruct]
+ -[LCBCorrectionShaders applyCorrection]
+ -[LCBCorrectionShaders createCorrection]
+ -[LCBCorrectionShaders initWithMetalContext:]
+ -[LCBDetection initWithDetectedLCB:]
+ -[LCBDetector .cxx_destruct]
+ -[LCBDetector initWithMetalContext:]
+ -[LCBDetector runDetectorOnTexture:levelIndex:loresTexture:loresLevelIndex:config:lscMetadata:error:]
+ -[LCBDetector runLocalMaximaFinderOnDetectorResult:levelIndex:config:error:]
+ -[LCBDetectorShaders .cxx_destruct]
+ -[LCBDetectorShaders initWithMetalContext:]
+ -[LCBDetectorShaders lcbDetector]
+ -[LCBDetectorShaders localMaximaFinder]
+ -[LCBExtractor .cxx_destruct]
+ -[LCBExtractor createRadiusLookUpTextureAndConfig:]
+ -[LCBExtractor initWithMetalContext:]
+ -[LCBExtractor runExtractorForEntries:inputTexture:levelIndex:loresTexture:loresLevelIndex:config:lscMetadata:error:]
+ -[LCBExtractorShaders .cxx_destruct]
+ -[LCBExtractorShaders initWithMetalContext:]
+ -[LCBExtractorShaders lcbExtractor]
+ -[LCBFiltering .cxx_destruct]
+ -[LCBFiltering initWithMetalContext:]
+ -[LCBFiltering perFrameFilteringWithTemporalLCBs:extractionResults:levelIndex:config:error:]
+ -[LCBFiltering temporalFilteringUpdateDatabase:detectionResultsForLevels:extractionSetForLevels:extractionResultsForLevels:config:didUpdateDatabase:error:]
+ -[LCBFilteringShaders .cxx_destruct]
+ -[LCBFilteringShaders clearLUT]
+ -[LCBFilteringShaders initWithMetalContext:]
+ -[LCBFilteringShaders perFrameFilterExtractedLCBs]
+ -[LCBMitigation .cxx_destruct]
+ -[LCBMitigation initWithMetalContext:]
+ -[LCBMitigation runOnInputYRGBTexture:inputPyramidLevel:targetSushiTexture:config:lscMetadata:lcbDatabase:didUpdateDatabase:error:]
+ -[LCBMitigation runOnSushiRawFrame:config:lscMetadata:lcbDatabase:didUpdateDatabase:error:]
+ -[LCBMitigationResult .cxx_destruct]
+ -[LCBMitigationResult corrections]
+ -[LCBMitigationResult description]
+ -[LCBMitigationResult detectionCountHistogram]
+ -[LCBMitigationResult initWithNumberOfDetections:numberOfCorrectionsOnIRCF:numberOfCorrectionsOnLens:corrections:detectionCountHistogram:]
+ -[LCBMitigationResult nLCBsCorrectedOnIRCF]
+ -[LCBMitigationResult nLCBsCorrectedOnLens]
+ -[LCBMitigationResult nLCBsDetected]
+ -[LCBPerFrameFilteringResults .cxx_destruct]
+ -[LCBPerFrameFilteringResults correctionLUT]
+ -[LCBPerFrameFilteringResults filteredLCBsBuf]
+ -[LCBPerFrameFilteringResults initWithFilteredLCBsBuf:correctionLUT:]
+ -[LCBPyramid .cxx_destruct]
+ -[LCBPyramid demosaicBayerToLuma:config:error:]
+ -[LCBPyramid demosaicBayerToLumaAndDownsample2x:config:error:]
+ -[LCBPyramid demosaicQuadraToLumaAndDownsample2x:config:error:]
+ -[LCBPyramid demosaicQuadraToLumaAndDownsample4x:config:error:]
+ -[LCBPyramid downsampleTexture:levelIndex:config:error:]
+ -[LCBPyramid initWithMetalContext:]
+ -[LCBPyramidShaders .cxx_destruct]
+ -[LCBPyramidShaders demosaicBayerYRGB]
+ -[LCBPyramidShaders demosaicBayer]
+ -[LCBPyramidShaders demosaicDownsampleBayerYRGB]
+ -[LCBPyramidShaders demosaicDownsampleBayer]
+ -[LCBPyramidShaders demosaicDownsampleQuadraYRGB]
+ -[LCBPyramidShaders demosaicDownsampleQuadra]
+ -[LCBPyramidShaders demosaicQuadraYRGB]
+ -[LCBPyramidShaders demosaicQuadra]
+ -[LCBPyramidShaders downsampleYRGB]
+ -[LCBPyramidShaders downsample]
+ -[LCBPyramidShaders initWithMetalContext:]
+ -[LCBTemporalFilteringResults .cxx_destruct]
+ -[LCBTemporalFilteringResults corrections]
+ -[LCBTemporalFilteringResults detectionCountHistogram]
+ -[LCBTemporalFilteringResults initWithNumberOfNewPositiveDetections:numberOfMatchedPositiveDetections:numberOfPositiveExtractions:numberOfNegativeExtractions:numberOfCorrectionsOnIRCF:numberOfCorrectionsOnLens:corrections:detectionCountHistogram:]
+ -[LCBTemporalFilteringResults numberOfCorrectionsOnIRCF]
+ -[LCBTemporalFilteringResults numberOfCorrectionsOnLens]
+ -[LCBTemporalFilteringResults numberOfMatchedPositiveDetections]
+ -[LCBTemporalFilteringResults numberOfNegativeExtractions]
+ -[LCBTemporalFilteringResults numberOfNewPositiveDetections]
+ -[LCBTemporalFilteringResults numberOfPositiveExtractions]
+ -[LCBTransformedEntry .cxx_destruct]
+ -[LCBTransformedEntry _setupCalculatedProperties]
+ -[LCBTransformedEntry currentConfig]
+ -[LCBTransformedEntry dictionaryRepresentation]
+ -[LCBTransformedEntry initWithDetectionOnPyramidLevel:positionInPyramid:pyramidRadius:config:]
+ -[LCBTransformedEntry initWithKey:position:radius:defocusRadius:particleDistance:apertureRatio:focusLensPosition:oisShift:opticalCenter:detectionCount:relativeToLens:lastDetectionGravityVector:lastDetectionTimeStamp:shouldCorrect:correctionFeatures:config:]
+ -[LCBTransformedEntry insideFrame]
+ -[LCBTransformedEntry opacityScaling]
+ -[LCBTransformedEntry overlapsDetection:]
+ -[LCBTransformedEntry pyramidLevel]
+ -[LCBTransformedEntry pyramidPosition]
+ -[LCBTransformedEntry pyramidRadius]
+ -[LCBTransformedEntry radiusScaling]
+ -[LCBTransformedEntry setCurrentConfig:]
+ -[LCBTransformedEntry withDetectionCountDecremented]
+ -[LCBTransformedEntry withDetectionCountIncrementedAndUpdatedFeatures:updatedRadius:]
+ -[LCBTransformedEntry withDifferentKey]
+ -[LCBTransformedEntry withUpdatedPosition:]
+ -[LearnedNRNetworkShared setUseFullStrength:]
+ -[LearnedNRNetworkShared useFullStrength]
+ -[LearnedNRNetworkStage setUseFullStrength:]
+ -[LearnedNRNetworkStage useFullStrength]
+ -[NSArray(TransformedEntry) transformedEntriesOnPyramidLevel:]
+ -[RawNightModeDeblurInference .cxx_destruct]
+ -[RawNightModeDeblurInference completionHandler]
+ -[RawNightModeDeblurInference initWithMetalContext:isQuadra:]
+ -[RawNightModeDeblurInference metalContext]
+ -[RawNightModeDeblurInference runInferenceWithInferenceData:]
+ -[RawNightModeDeblurInference setCompletionHandler:]
+ -[RawNightModeDeblurInferenceData .cxx_destruct]
+ -[RawNightModeDeblurInferenceData cameraInfoByPortType]
+ -[RawNightModeDeblurInferenceData inputNoiseMapTexture]
+ -[RawNightModeDeblurInferenceData inputRGBTexture]
+ -[RawNightModeDeblurInferenceData lscMetadata]
+ -[RawNightModeDeblurInferenceData lscTexture]
+ -[RawNightModeDeblurInferenceData metadata]
+ -[RawNightModeDeblurInferenceData outputCleanRGBTexture]
+ -[RawNightModeDeblurInferenceData outputRGBTexture]
+ -[RawNightModeDeblurInferenceData semanticMasks]
+ -[RawNightModeDeblurInferenceData setCameraInfoByPortType:]
+ -[RawNightModeDeblurInferenceData setInputNoiseMapTexture:]
+ -[RawNightModeDeblurInferenceData setInputRGBTexture:]
+ -[RawNightModeDeblurInferenceData setLscMetadata:]
+ -[RawNightModeDeblurInferenceData setLscTexture:]
+ -[RawNightModeDeblurInferenceData setMetadata:]
+ -[RawNightModeDeblurInferenceData setOutputCleanRGBTexture:]
+ -[RawNightModeDeblurInferenceData setOutputRGBTexture:]
+ -[RawNightModeDeblurInferenceData setSemanticMasks:]
+ -[RawNightModeDeblurInferenceData setSkipNoiseAddback:]
+ -[RawNightModeDeblurInferenceData setUdNetPlist:]
+ -[RawNightModeDeblurInferenceData skipNoiseAddback]
+ -[RawNightModeDeblurInferenceData udNetPlist]
+ -[RawNightModeDenoiseInferenceCMITIPSharedParameters updateParametersFromMetadata:cameraInfoByPortType:tuningParameters:lscGainMapParameters:firstPix:aeTargetGain:isQuadra:textureDimensions:skipAWBInversion:skipLSCInversion:clipNetworkInputs:]
+ -[RawNightModeDenoiseInferenceInputs clipNetworkInputs]
+ -[RawNightModeDenoiseInferenceInputs setClipNetworkInputs:]
+ -[RawNightModeDenoiseInferenceInputs setSkipAWBInversion:]
+ -[RawNightModeDenoiseInferenceInputs setSkipLSCInversion:]
+ -[RawNightModeDenoiseInferenceInputs skipAWBInversion]
+ -[RawNightModeDenoiseInferenceInputs skipLSCInversion]
+ -[RawNightModeFusionInference initWithMetalContext:isQuadra:isBarrington:isReno:requiresDarkCurrentNoiseModel:]
+ -[RawNightModeFusionInferenceData clipNetworkInputs]
+ -[RawNightModeFusionInferenceData setClipNetworkInputs:]
+ -[RawNightModeFusionInferenceData setSkipAWBInversion:]
+ -[RawNightModeFusionInferenceData setSkipLSCInversion:]
+ -[RawNightModeFusionInferenceData skipAWBInversion]
+ -[RawNightModeFusionInferenceData skipLSCInversion]
+ -[RawNightModeFusionMetalStage updateParametersFromMetadata:cameraInfoByPortType:lscGainMapParameters:tuningParameters:firstPix:isQuadra:requiresDarkCurrentNoiseModel:aeTargetGain:textureDimensions:skipAWBInversion:skipLSCInversion:clipNetworkInputs:]
+ -[RawNightModeProcessor _initRawNightModeDenoiseInference:isBarrington:isReno:isArgyleTripodMax:]
+ -[RawNightModeProcessor _initRawNightModeFusionInference:isBarrington:isReno:requiresDarkCurrentNoiseModel:]
+ -[RawNightModeProcessor _isReno:]
+ -[RawNightModeProcessor computeAdaptiveFusionTuningPlist:fromInputPlist:quadraBinningFactor:]
+ -[RawNightModeProcessor readAdaptiveFusionPostProcessingTuningsPlist:quadraBinningFactor:]
+ -[SoftISPBounds processingRegionWithinSensorInBayerPixels]
+ -[SoftISPCalibrationConfig(LCB) getLCBConfigForInputFrame:bounds:correctionEnabled:awb:]
+ -[SoftISPCalibrationConfig(LCB) getLCBEnabledForInputFrame:processingOptions:lcbEnabled:]
+ -[SoftISPOutputFrame setUpdatedLCBDatabase:]
+ -[SoftISPOutputFrame updatedLCBDatabase]
+ -[UDNet .cxx_destruct]
+ -[UDNet cameraInfoByPortType]
+ -[UDNet completionHandler]
+ -[UDNet hairMaskTexture]
+ -[UDNet initWithMetalContext:error:]
+ -[UDNet personMaskTexture]
+ -[UDNet runWithInputMetadata:udNetPlist:gainValue:inputRGBTexture:inputLSCTexture:inputLSCMetadata:outputLumaTexture:outputChromaTexture:]
+ -[UDNet runWithInputMetadata:udNetPlist:inputLumaTexture:inputChromaTexture:inputLSCTexture:inputLSCMetadata:outputLumaTexture:outputChromaTexture:]
+ -[UDNet runWithInputMetadata:udNetPlist:inputRGBTexture:inputNoiseMapTexture:inputLSCTexture:inputLSCMetadata:outputRGBTexture:outputCleanRGBTexture:skipNoiseAddback:]
+ -[UDNet setCameraInfoByPortType:]
+ -[UDNet setCompletionHandler:]
+ -[UDNet setHairMaskTexture:]
+ -[UDNet setPersonMaskTexture:]
+ -[UDNet setSkinMaskTexture:]
+ -[UDNet setSkyMaskTexture:]
+ -[UDNet setupWithNetworkType:isQuadra:]
+ -[UDNet skinMaskTexture]
+ -[UDNet skyMaskTexture]
+ -[UDNetNetworkParameters .cxx_destruct]
+ -[UDNetNetworkParameters addbackParams]
+ -[UDNetNetworkParameters gainValue]
+ -[UDNetNetworkParameters getTileCountForWidth:height:]
+ -[UDNetNetworkParameters getTileForIndex:]
+ -[UDNetNetworkParameters hairMaskTexture]
+ -[UDNetNetworkParameters hrGainDownRatio]
+ -[UDNetNetworkParameters initWithTileWidth:tileHeight:]
+ -[UDNetNetworkParameters inputChromaTexture]
+ -[UDNetNetworkParameters inputLumaTexture]
+ -[UDNetNetworkParameters inputNoiseMapTexture]
+ -[UDNetNetworkParameters inputNoiseScalingFactor]
+ -[UDNetNetworkParameters inputRGBTexture]
+ -[UDNetNetworkParameters lscGainsTexture]
+ -[UDNetNetworkParameters lscParams]
+ -[UDNetNetworkParameters networkType]
+ -[UDNetNetworkParameters noiseMapScalingBody]
+ -[UDNetNetworkParameters noiseMapScalingSkin]
+ -[UDNetNetworkParameters noiseMapScalingSky]
+ -[UDNetNetworkParameters noiseModel]
+ -[UDNetNetworkParameters numberOfTilesForHeight:]
+ -[UDNetNetworkParameters numberOfTilesForWidth:]
+ -[UDNetNetworkParameters outputChromaTexture]
+ -[UDNetNetworkParameters outputCleanRGBTexture]
+ -[UDNetNetworkParameters outputLumaTexture]
+ -[UDNetNetworkParameters outputRGBTexture]
+ -[UDNetNetworkParameters personMaskTexture]
+ -[UDNetNetworkParameters setAddbackParams:]
+ -[UDNetNetworkParameters setGainValue:]
+ -[UDNetNetworkParameters setHairMaskTexture:]
+ -[UDNetNetworkParameters setHrGainDownRatio:]
+ -[UDNetNetworkParameters setInputChromaTexture:]
+ -[UDNetNetworkParameters setInputLumaTexture:]
+ -[UDNetNetworkParameters setInputNoiseMapTexture:]
+ -[UDNetNetworkParameters setInputNoiseScalingFactor:]
+ -[UDNetNetworkParameters setInputRGBTexture:]
+ -[UDNetNetworkParameters setLscGainsTexture:]
+ -[UDNetNetworkParameters setLscParams:]
+ -[UDNetNetworkParameters setNetworkType:]
+ -[UDNetNetworkParameters setNoiseMapScalingBody:]
+ -[UDNetNetworkParameters setNoiseMapScalingSkin:]
+ -[UDNetNetworkParameters setNoiseMapScalingSky:]
+ -[UDNetNetworkParameters setNoiseModel:]
+ -[UDNetNetworkParameters setOutputChromaTexture:]
+ -[UDNetNetworkParameters setOutputCleanRGBTexture:]
+ -[UDNetNetworkParameters setOutputLumaTexture:]
+ -[UDNetNetworkParameters setOutputRGBTexture:]
+ -[UDNetNetworkParameters setPersonMaskTexture:]
+ -[UDNetNetworkParameters setSkinMaskTexture:]
+ -[UDNetNetworkParameters setSkipNoiseAddback:]
+ -[UDNetNetworkParameters setSkyMaskTexture:]
+ -[UDNetNetworkParameters setTileOverlapX:]
+ -[UDNetNetworkParameters setTileOverlapY:]
+ -[UDNetNetworkParameters skinMaskTexture]
+ -[UDNetNetworkParameters skipNoiseAddback]
+ -[UDNetNetworkParameters skyMaskTexture]
+ -[UDNetNetworkParameters tileHeight]
+ -[UDNetNetworkParameters tileOverlapX]
+ -[UDNetNetworkParameters tileOverlapY]
+ -[UDNetNetworkParameters tileStepHeight]
+ -[UDNetNetworkParameters tileStepWidth]
+ -[UDNetNetworkParameters tileWidth]
+ -[UDNetNetworkStage .cxx_destruct]
+ -[UDNetNetworkStage cameraInfoByPortType]
+ -[UDNetNetworkStage completionHandler]
+ -[UDNetNetworkStage gainValue]
+ -[UDNetNetworkStage hairMaskTexture]
+ -[UDNetNetworkStage initWithMetalContext:error:]
+ -[UDNetNetworkStage inputChromaTexture]
+ -[UDNetNetworkStage inputLumaTexture]
+ -[UDNetNetworkStage inputNoiseMapTexture]
+ -[UDNetNetworkStage inputRGBTexture]
+ -[UDNetNetworkStage lscMetadata]
+ -[UDNetNetworkStage lscTexture]
+ -[UDNetNetworkStage metadata]
+ -[UDNetNetworkStage outputChromaTexture]
+ -[UDNetNetworkStage outputCleanRGBTexture]
+ -[UDNetNetworkStage outputLumaTexture]
+ -[UDNetNetworkStage outputRGBTexture]
+ -[UDNetNetworkStage personMaskTexture]
+ -[UDNetNetworkStage prepareForNetworkType:isQuadra:]
+ -[UDNetNetworkStage run]
+ -[UDNetNetworkStage setCameraInfoByPortType:]
+ -[UDNetNetworkStage setCompletionHandler:]
+ -[UDNetNetworkStage setGainValue:]
+ -[UDNetNetworkStage setHairMaskTexture:]
+ -[UDNetNetworkStage setInputChromaTexture:]
+ -[UDNetNetworkStage setInputLumaTexture:]
+ -[UDNetNetworkStage setInputNoiseMapTexture:]
+ -[UDNetNetworkStage setInputRGBTexture:]
+ -[UDNetNetworkStage setLscMetadata:]
+ -[UDNetNetworkStage setLscTexture:]
+ -[UDNetNetworkStage setMetadata:]
+ -[UDNetNetworkStage setOutputChromaTexture:]
+ -[UDNetNetworkStage setOutputCleanRGBTexture:]
+ -[UDNetNetworkStage setOutputLumaTexture:]
+ -[UDNetNetworkStage setOutputRGBTexture:]
+ -[UDNetNetworkStage setPersonMaskTexture:]
+ -[UDNetNetworkStage setSkinMaskTexture:]
+ -[UDNetNetworkStage setSkipNoiseAddback:]
+ -[UDNetNetworkStage setSkyMaskTexture:]
+ -[UDNetNetworkStage setUdNetPList:]
+ -[UDNetNetworkStage skinMaskTexture]
+ -[UDNetNetworkStage skipNoiseAddback]
+ -[UDNetNetworkStage skyMaskTexture]
+ -[UDNetNetworkStage udNetPList]
+ -[UDNetPlist .cxx_destruct]
+ -[UDNetPlist init]
+ -[UDNetPlist readPlist:]
+ -[UDNetPostNetworkStage .cxx_destruct]
+ -[UDNetPostNetworkStage initWithMetalContext:]
+ -[UDNetPostNetworkStage networkParameters]
+ -[UDNetPostNetworkStage processTilePipelineStage:]
+ -[UDNetPostNetworkStage setNetworkParameters:]
+ -[UDNetPreNetworkStage .cxx_destruct]
+ -[UDNetPreNetworkStage initWithMetalContext:]
+ -[UDNetPreNetworkStage networkParameters]
+ -[UDNetPreNetworkStage processTilePipelineStage:]
+ -[UDNetPreNetworkStage setNetworkParameters:]
+ GCC_except_table28
+ _CMIDimensionsFromPixelBuffer
+ _OBJC_CLASS_$_CMILCBDatabase
+ _OBJC_CLASS_$_CMILCBEntry
+ _OBJC_CLASS_$_FlareSourceDetector
+ _OBJC_CLASS_$_FlareSourceDetectorInputFrame
+ _OBJC_CLASS_$_FlareSourceDetectorPlist
+ _OBJC_CLASS_$_LCBBlock
+ _OBJC_CLASS_$_LCBBlockShaders
+ _OBJC_CLASS_$_LCBConfig
+ _OBJC_CLASS_$_LCBCorrection
+ _OBJC_CLASS_$_LCBCorrectionShaders
+ _OBJC_CLASS_$_LCBDetection
+ _OBJC_CLASS_$_LCBDetector
+ _OBJC_CLASS_$_LCBDetectorShaders
+ _OBJC_CLASS_$_LCBExtractor
+ _OBJC_CLASS_$_LCBExtractorShaders
+ _OBJC_CLASS_$_LCBFiltering
+ _OBJC_CLASS_$_LCBFilteringShaders
+ _OBJC_CLASS_$_LCBMitigation
+ _OBJC_CLASS_$_LCBMitigationResult
+ _OBJC_CLASS_$_LCBPerFrameFilteringResults
+ _OBJC_CLASS_$_LCBPyramid
+ _OBJC_CLASS_$_LCBPyramidShaders
+ _OBJC_CLASS_$_LCBTemporalFilteringResults
+ _OBJC_CLASS_$_LCBTransformedEntry
+ _OBJC_CLASS_$_RawNightModeDeblurInference
+ _OBJC_CLASS_$_RawNightModeDeblurInferenceData
+ _OBJC_CLASS_$_UDNet
+ _OBJC_CLASS_$_UDNetNetworkParameters
+ _OBJC_CLASS_$_UDNetNetworkStage
+ _OBJC_CLASS_$_UDNetPlist
+ _OBJC_CLASS_$_UDNetPostNetworkStage
+ _OBJC_CLASS_$_UDNetPreNetworkStage
+ _OBJC_IVAR_$_CMIPost._udNetStage
+ _OBJC_IVAR_$_CMIPostConfig._cameraInfoByPortType
+ _OBJC_IVAR_$_CMIPostConfig._inputLSCMetadata
+ _OBJC_IVAR_$_CMIPostConfig._inputLSCTexture
+ _OBJC_IVAR_$_CMIPostConfig._inputMetadata
+ _OBJC_IVAR_$_CMIPostConfig._udNetPlist
+ _OBJC_IVAR_$_FlareSourceDetector._computeLocalMinPSO
+ _OBJC_IVAR_$_FlareSourceDetector._computeLumaAndDownsampleBayerR16PSO
+ _OBJC_IVAR_$_FlareSourceDetector._computeLumaAndDownsampleQuadPackedPSO
+ _OBJC_IVAR_$_FlareSourceDetector._countFlareSourcePixelsPSO
+ _OBJC_IVAR_$_FlareSourceDetector._downsampleLumaOnlyPSO
+ _OBJC_IVAR_$_FlareSourceDetector._evaluateGatePSO
+ _OBJC_IVAR_$_FlareSourceDetector._inflightEffectiveMinCount
+ _OBJC_IVAR_$_FlareSourceDetector._inputType
+ _OBJC_IVAR_$_FlareSourceDetector._metal
+ _OBJC_IVAR_$_FlareSourceDetector._pendingResultCommandBuffer
+ _OBJC_IVAR_$_FlareSourceDetector._resultBuffer
+ _OBJC_IVAR_$_FlareSourceDetector._tuningPlist
+ _OBJC_IVAR_$_FlareSourceDetectorInputFrame._auxDraftDemosaicLumaTexture
+ _OBJC_IVAR_$_FlareSourceDetectorInputFrame._auxDraftDemosaicRGBTexture
+ _OBJC_IVAR_$_FlareSourceDetectorInputFrame._baseTex
+ _OBJC_IVAR_$_FlareSourceDetectorInputFrame._lscGainMapTexture
+ _OBJC_IVAR_$_FlareSourceDetectorInputFrame._properties
+ _OBJC_IVAR_$_FlareSourceDetectorPlist.enableFlareSourceDetector
+ _OBJC_IVAR_$_FlareSourceDetectorPlist.localMinThreshold
+ _OBJC_IVAR_$_FlareSourceDetectorPlist.localWindowSize
+ _OBJC_IVAR_$_FlareSourceDetectorPlist.lumaGapThreshold
+ _OBJC_IVAR_$_FlareSourceDetectorPlist.minAreaRatio
+ _OBJC_IVAR_$_FlareSourceDetectorPlist.minPixelCount
+ _OBJC_IVAR_$_H13FastBayerProcStage._lcb
+ _OBJC_IVAR_$_LCBBlock._metalContext
+ _OBJC_IVAR_$_LCBBlockShaders._metalContext
+ _OBJC_IVAR_$_LCBConfig._apertureRatio
+ _OBJC_IVAR_$_LCBConfig._bayerSensorDimensions
+ _OBJC_IVAR_$_LCBConfig._captureGravityVector
+ _OBJC_IVAR_$_LCBConfig._captureTimeStamp
+ _OBJC_IVAR_$_LCBConfig._clippingThreshold
+ _OBJC_IVAR_$_LCBConfig._correctionEnabled
+ _OBJC_IVAR_$_LCBConfig._darkPixelThreshold
+ _OBJC_IVAR_$_LCBConfig._databaseUpdateEnabled
+ _OBJC_IVAR_$_LCBConfig._defocusRadiusForIRCF
+ _OBJC_IVAR_$_LCBConfig._defocusRadiusForLens
+ _OBJC_IVAR_$_LCBConfig._defocusRadiusOffsetForIRCF
+ _OBJC_IVAR_$_LCBConfig._defocusRadiusOffsetForLens
+ _OBJC_IVAR_$_LCBConfig._defocusRadiusSlopeForIRCF
+ _OBJC_IVAR_$_LCBConfig._defocusRadiusSlopeForLens
+ _OBJC_IVAR_$_LCBConfig._detectionEnabled
+ _OBJC_IVAR_$_LCBConfig._detectionLocalityThreshold
+ _OBJC_IVAR_$_LCBConfig._detectionScoreDarkLower
+ _OBJC_IVAR_$_LCBConfig._detectionScoreDarkUpper
+ _OBJC_IVAR_$_LCBConfig._detectionScoreEdgeLower
+ _OBJC_IVAR_$_LCBConfig._detectionScoreEdgeUpper
+ _OBJC_IVAR_$_LCBConfig._detectionScoreImprovementLower
+ _OBJC_IVAR_$_LCBConfig._detectionScoreImprovementUpper
+ _OBJC_IVAR_$_LCBConfig._extractionEnabled
+ _OBJC_IVAR_$_LCBConfig._firstPixel
+ _OBJC_IVAR_$_LCBConfig._firstPyramidLevel
+ _OBJC_IVAR_$_LCBConfig._focusLensPosition
+ _OBJC_IVAR_$_LCBConfig._innerOuterVarEdgeLower
+ _OBJC_IVAR_$_LCBConfig._innerOuterVarEdgeUpper
+ _OBJC_IVAR_$_LCBConfig._inputDimensionsInBayerPixels
+ _OBJC_IVAR_$_LCBConfig._inputOffsetInBayerPixels
+ _OBJC_IVAR_$_LCBConfig._inputPyramidEnabled
+ _OBJC_IVAR_$_LCBConfig._invertedAWBGains
+ _OBJC_IVAR_$_LCBConfig._isQuadra
+ _OBJC_IVAR_$_LCBConfig._lastPyramidLevel
+ _OBJC_IVAR_$_LCBConfig._lowPassNPyramidLevels
+ _OBJC_IVAR_$_LCBConfig._lumaConversionCoefficients
+ _OBJC_IVAR_$_LCBConfig._maxCorrectionFeaturesUpdateAmount
+ _OBJC_IVAR_$_LCBConfig._maxDetectionCount
+ _OBJC_IVAR_$_LCBConfig._maxRadiusUpdateDecrement
+ _OBJC_IVAR_$_LCBConfig._maxRadiusUpdateIncrement
+ _OBJC_IVAR_$_LCBConfig._maximumCorrectionScaling
+ _OBJC_IVAR_$_LCBConfig._maximumDetectionScoreForNoLCB
+ _OBJC_IVAR_$_LCBConfig._maximumNumberOfCorrectionsPerLevel
+ _OBJC_IVAR_$_LCBConfig._maximumNumberOfDetectionsPerLevel
+ _OBJC_IVAR_$_LCBConfig._maximumNumberOfExtractionsPerLevel
+ _OBJC_IVAR_$_LCBConfig._minCorrectionFeaturesLearningRate
+ _OBJC_IVAR_$_LCBConfig._minimumConfidence
+ _OBJC_IVAR_$_LCBConfig._minimumCorrectionScaling
+ _OBJC_IVAR_$_LCBConfig._minimumDetectionCountForCorrection
+ _OBJC_IVAR_$_LCBConfig._minimumDetectionScoreForLCB
+ _OBJC_IVAR_$_LCBConfig._minimumGravityVectorChange
+ _OBJC_IVAR_$_LCBConfig._minimumTimeDelta
+ _OBJC_IVAR_$_LCBConfig._nPyramidLevels
+ _OBJC_IVAR_$_LCBConfig._notStrongEdgeConfidenceLower
+ _OBJC_IVAR_$_LCBConfig._notStrongEdgeConfidenceUpper
+ _OBJC_IVAR_$_LCBConfig._notTooDarkConfidenceLower
+ _OBJC_IVAR_$_LCBConfig._notTooDarkConfidenceScaling
+ _OBJC_IVAR_$_LCBConfig._notTooDarkConfidenceUpper
+ _OBJC_IVAR_$_LCBConfig._oisShift
+ _OBJC_IVAR_$_LCBConfig._oisShiftScalingFactorForIRCF
+ _OBJC_IVAR_$_LCBConfig._oisShiftScalingFactorForLens
+ _OBJC_IVAR_$_LCBConfig._opticalCenterForIRCF
+ _OBJC_IVAR_$_LCBConfig._opticalCenterForLens
+ _OBJC_IVAR_$_LCBConfig._particleDistanceForIRCF
+ _OBJC_IVAR_$_LCBConfig._particleDistanceForLens
+ _OBJC_IVAR_$_LCBConfig._particleDistanceOffsetForIRCF
+ _OBJC_IVAR_$_LCBConfig._particleDistanceOffsetForLens
+ _OBJC_IVAR_$_LCBConfig._particleDistanceSlopeForIRCF
+ _OBJC_IVAR_$_LCBConfig._particleDistanceSlopeForLens
+ _OBJC_IVAR_$_LCBConfig._perFrameFilteringEnabled
+ _OBJC_IVAR_$_LCBConfig._positionUpdateRate
+ _OBJC_IVAR_$_LCBConfig._radiusLearningRate
+ _OBJC_IVAR_$_LCBConfig._relativeToLensRadiusThreshold
+ _OBJC_IVAR_$_LCBConfig._residualConfidenceDetailLower
+ _OBJC_IVAR_$_LCBConfig._residualConfidenceDetailUpper
+ _OBJC_IVAR_$_LCBConfig._residualConfidenceInOutVarLower
+ _OBJC_IVAR_$_LCBConfig._residualConfidenceInOutVarUpper
+ _OBJC_IVAR_$_LCBConfig._skipPyrLevel0
+ _OBJC_IVAR_$_LCBConfig._useFullColor
+ _OBJC_IVAR_$_LCBCorrection._shaders
+ _OBJC_IVAR_$_LCBCorrectionShaders._applyCorrection
+ _OBJC_IVAR_$_LCBCorrectionShaders._createCorrection
+ _OBJC_IVAR_$_LCBDetection._confidenceScore
+ _OBJC_IVAR_$_LCBDetection._detectionScore
+ _OBJC_IVAR_$_LCBDetection._improvementScore
+ _OBJC_IVAR_$_LCBDetection._localityScore
+ _OBJC_IVAR_$_LCBDetection._positionX
+ _OBJC_IVAR_$_LCBDetection._positionY
+ _OBJC_IVAR_$_LCBDetection._pyramidLevel
+ _OBJC_IVAR_$_LCBDetection._radius
+ _OBJC_IVAR_$_LCBDetector._shaders
+ _OBJC_IVAR_$_LCBDetectorShaders._lcbDetector
+ _OBJC_IVAR_$_LCBDetectorShaders._localMaximaFinder
+ _OBJC_IVAR_$_LCBExtractor._radiusLUT
+ _OBJC_IVAR_$_LCBExtractor._radiusLUTConfig
+ _OBJC_IVAR_$_LCBExtractor._shaders
+ _OBJC_IVAR_$_LCBExtractorShaders._lcbExtractor
+ _OBJC_IVAR_$_LCBFiltering._shaders
+ _OBJC_IVAR_$_LCBFilteringShaders._clearLUT
+ _OBJC_IVAR_$_LCBFilteringShaders._perFrameFilterExtractedLCBs
+ _OBJC_IVAR_$_LCBMitigation._correction
+ _OBJC_IVAR_$_LCBMitigation._detector
+ _OBJC_IVAR_$_LCBMitigation._extractor
+ _OBJC_IVAR_$_LCBMitigation._filtering
+ _OBJC_IVAR_$_LCBMitigation._metalContext
+ _OBJC_IVAR_$_LCBMitigation._pyramid
+ _OBJC_IVAR_$_LCBMitigationResult._corrections
+ _OBJC_IVAR_$_LCBMitigationResult._detectionCountHistogram
+ _OBJC_IVAR_$_LCBMitigationResult._nLCBsCorrectedOnIRCF
+ _OBJC_IVAR_$_LCBMitigationResult._nLCBsCorrectedOnLens
+ _OBJC_IVAR_$_LCBMitigationResult._nLCBsDetected
+ _OBJC_IVAR_$_LCBPerFrameFilteringResults._correctionLUT
+ _OBJC_IVAR_$_LCBPerFrameFilteringResults._filteredLCBsBuf
+ _OBJC_IVAR_$_LCBPyramid._shaders
+ _OBJC_IVAR_$_LCBPyramidShaders._demosaicBayer
+ _OBJC_IVAR_$_LCBPyramidShaders._demosaicBayerYRGB
+ _OBJC_IVAR_$_LCBPyramidShaders._demosaicDownsampleBayer
+ _OBJC_IVAR_$_LCBPyramidShaders._demosaicDownsampleBayerYRGB
+ _OBJC_IVAR_$_LCBPyramidShaders._demosaicDownsampleQuadra
+ _OBJC_IVAR_$_LCBPyramidShaders._demosaicDownsampleQuadraYRGB
+ _OBJC_IVAR_$_LCBPyramidShaders._demosaicQuadra
+ _OBJC_IVAR_$_LCBPyramidShaders._demosaicQuadraYRGB
+ _OBJC_IVAR_$_LCBPyramidShaders._downsample
+ _OBJC_IVAR_$_LCBPyramidShaders._downsampleYRGB
+ _OBJC_IVAR_$_LCBTemporalFilteringResults._corrections
+ _OBJC_IVAR_$_LCBTemporalFilteringResults._detectionCountHistogram
+ _OBJC_IVAR_$_LCBTemporalFilteringResults._numberOfCorrectionsOnIRCF
+ _OBJC_IVAR_$_LCBTemporalFilteringResults._numberOfCorrectionsOnLens
+ _OBJC_IVAR_$_LCBTemporalFilteringResults._numberOfMatchedPositiveDetections
+ _OBJC_IVAR_$_LCBTemporalFilteringResults._numberOfNegativeExtractions
+ _OBJC_IVAR_$_LCBTemporalFilteringResults._numberOfNewPositiveDetections
+ _OBJC_IVAR_$_LCBTemporalFilteringResults._numberOfPositiveExtractions
+ _OBJC_IVAR_$_LCBTransformedEntry._currentConfig
+ _OBJC_IVAR_$_LCBTransformedEntry._insideFrame
+ _OBJC_IVAR_$_LCBTransformedEntry._opacityScaling
+ _OBJC_IVAR_$_LCBTransformedEntry._pyramidLevel
+ _OBJC_IVAR_$_LCBTransformedEntry._pyramidPosition
+ _OBJC_IVAR_$_LCBTransformedEntry._pyramidRadius
+ _OBJC_IVAR_$_LCBTransformedEntry._radiusScaling
+ _OBJC_IVAR_$_LearnedHRNRProcessor._udNetStage
+ _OBJC_IVAR_$_LearnedNRNetworkPostANEStage._fullStrengthAddbackForRawInput
+ _OBJC_IVAR_$_LearnedNRNetworkShared._useFullStrength
+ _OBJC_IVAR_$_LearnedNRNetworkStage._useFullStrength
+ _OBJC_IVAR_$_NRFConfig._applySkinColorMitigationCCM
+ _OBJC_IVAR_$_NRFConfig._enableUDNet
+ _OBJC_IVAR_$_NRFPlist.flareSourceDetectorPlist
+ _OBJC_IVAR_$_NRFPlist.udNetPlist
+ _OBJC_IVAR_$_RawDFProcessor._flareSourceDetector
+ _OBJC_IVAR_$_RawDFProcessor._isFlareDetected
+ _OBJC_IVAR_$_RawDFProcessor._udNetStage
+ _OBJC_IVAR_$_RawNightModeDeblurInference._completionHandler
+ _OBJC_IVAR_$_RawNightModeDeblurInference._metalContext
+ _OBJC_IVAR_$_RawNightModeDeblurInference._udNet
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._cameraInfoByPortType
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._inputNoiseMapTexture
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._inputRGBTexture
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._lscMetadata
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._lscTexture
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._metadata
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._outputCleanRGBTexture
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._outputRGBTexture
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._semanticMasks
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._skipNoiseAddback
+ _OBJC_IVAR_$_RawNightModeDeblurInferenceData._udNetPlist
+ _OBJC_IVAR_$_RawNightModeDenoiseInferenceInputs._clipNetworkInputs
+ _OBJC_IVAR_$_RawNightModeDenoiseInferenceInputs._skipAWBInversion
+ _OBJC_IVAR_$_RawNightModeDenoiseInferenceInputs._skipLSCInversion
+ _OBJC_IVAR_$_RawNightModeFusionInferenceData._clipNetworkInputs
+ _OBJC_IVAR_$_RawNightModeFusionInferenceData._skipAWBInversion
+ _OBJC_IVAR_$_RawNightModeFusionInferenceData._skipLSCInversion
+ _OBJC_IVAR_$_RawNightModeProcessor._detectorsDone
+ _OBJC_IVAR_$_RawNightModeProcessor._flareSourceDetector
+ _OBJC_IVAR_$_RawNightModeProcessor._inferenceDeblur
+ _OBJC_IVAR_$_RawNightModeProcessor._isFlareDetected
+ _OBJC_IVAR_$_RawNightModeProcessor._rawDFDetectors
+ _OBJC_IVAR_$_RawNightModeProcessor._skipLSCInversion
+ _OBJC_IVAR_$_SoftISPCalibrationStage._lcb
+ _OBJC_IVAR_$_SoftISPOutputFrame._updatedLCBDatabase
+ _OBJC_IVAR_$_ToneMappingPlist.applySkinColorMitigationCCM
+ _OBJC_IVAR_$_UBProcessorV4._flareSourceDetector
+ _OBJC_IVAR_$_UBProcessorV4._isFlareDetected
+ _OBJC_IVAR_$_UDNet._cameraInfoByPortType
+ _OBJC_IVAR_$_UDNet._completionHandler
+ _OBJC_IVAR_$_UDNet._hairMaskTexture
+ _OBJC_IVAR_$_UDNet._metalContext
+ _OBJC_IVAR_$_UDNet._networkStage
+ _OBJC_IVAR_$_UDNet._networkTypeSetup
+ _OBJC_IVAR_$_UDNet._personMaskTexture
+ _OBJC_IVAR_$_UDNet._quadraPrepared
+ _OBJC_IVAR_$_UDNet._skinMaskTexture
+ _OBJC_IVAR_$_UDNet._skyMaskTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._addbackParams
+ _OBJC_IVAR_$_UDNetNetworkParameters._gainValue
+ _OBJC_IVAR_$_UDNetNetworkParameters._hairMaskTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._hrGainDownRatio
+ _OBJC_IVAR_$_UDNetNetworkParameters._inputChromaTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._inputLumaTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._inputNoiseMapTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._inputNoiseScalingFactor
+ _OBJC_IVAR_$_UDNetNetworkParameters._inputRGBTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._lscGainsTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._lscParams
+ _OBJC_IVAR_$_UDNetNetworkParameters._networkType
+ _OBJC_IVAR_$_UDNetNetworkParameters._noiseMapScalingBody
+ _OBJC_IVAR_$_UDNetNetworkParameters._noiseMapScalingSkin
+ _OBJC_IVAR_$_UDNetNetworkParameters._noiseMapScalingSky
+ _OBJC_IVAR_$_UDNetNetworkParameters._noiseModel
+ _OBJC_IVAR_$_UDNetNetworkParameters._outputChromaTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._outputCleanRGBTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._outputLumaTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._outputRGBTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._personMaskTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._skinMaskTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._skipNoiseAddback
+ _OBJC_IVAR_$_UDNetNetworkParameters._skyMaskTexture
+ _OBJC_IVAR_$_UDNetNetworkParameters._tileHeight
+ _OBJC_IVAR_$_UDNetNetworkParameters._tileOverlapX
+ _OBJC_IVAR_$_UDNetNetworkParameters._tileOverlapY
+ _OBJC_IVAR_$_UDNetNetworkParameters._tileWidth
+ _OBJC_IVAR_$_UDNetNetworkStage._cameraInfoByPortType
+ _OBJC_IVAR_$_UDNetNetworkStage._completionHandler
+ _OBJC_IVAR_$_UDNetNetworkStage._gainValue
+ _OBJC_IVAR_$_UDNetNetworkStage._hairMaskTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._inputChromaTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._inputLumaTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._inputNoiseMapTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._inputRGBTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._lscMetadata
+ _OBJC_IVAR_$_UDNetNetworkStage._lscTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._metadata
+ _OBJC_IVAR_$_UDNetNetworkStage._metalContext
+ _OBJC_IVAR_$_UDNetNetworkStage._networkParameters
+ _OBJC_IVAR_$_UDNetNetworkStage._outputChromaTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._outputCleanRGBTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._outputLumaTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._outputRGBTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._personMaskTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._skinMaskTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._skipNoiseAddback
+ _OBJC_IVAR_$_UDNetNetworkStage._skyMaskTexture
+ _OBJC_IVAR_$_UDNetNetworkStage._tiledInferenceProcessor
+ _OBJC_IVAR_$_UDNetNetworkStage._udNetPList
+ _OBJC_IVAR_$_UDNetPlist.addbackClampFactor
+ _OBJC_IVAR_$_UDNetPlist.addbackLumaAddbackThreshold
+ _OBJC_IVAR_$_UDNetPlist.addbackLumaAddbackWeight
+ _OBJC_IVAR_$_UDNetPlist.addbackNoiseScalingFactor
+ _OBJC_IVAR_$_UDNetPlist.enableUDNet
+ _OBJC_IVAR_$_UDNetPlist.inputNoiseScalingFactor
+ _OBJC_IVAR_$_UDNetPlist.inputNoiseScalingFactorBody
+ _OBJC_IVAR_$_UDNetPlist.inputNoiseScalingFactorSkin
+ _OBJC_IVAR_$_UDNetPlist.inputNoiseScalingFactorSky
+ _OBJC_IVAR_$_UDNetPlist.networkType
+ _OBJC_IVAR_$_UDNetPlist.tilePadding
+ _OBJC_IVAR_$_UDNetPostNetworkStage._metal
+ _OBJC_IVAR_$_UDNetPostNetworkStage._networkParameters
+ _OBJC_IVAR_$_UDNetPostNetworkStage._processOutputTileRGB
+ _OBJC_IVAR_$_UDNetPostNetworkStage._processOutputTileYUV
+ _OBJC_IVAR_$_UDNetPreNetworkStage._metal
+ _OBJC_IVAR_$_UDNetPreNetworkStage._networkParameters
+ _OBJC_IVAR_$_UDNetPreNetworkStage._processInputTileRGB
+ _OBJC_IVAR_$_UDNetPreNetworkStage._processInputTileYUV
+ _OBJC_METACLASS_$_CMILCBEntry
+ _OBJC_METACLASS_$_FlareSourceDetector
+ _OBJC_METACLASS_$_FlareSourceDetectorInputFrame
+ _OBJC_METACLASS_$_FlareSourceDetectorPlist
+ _OBJC_METACLASS_$_LCBBlock
+ _OBJC_METACLASS_$_LCBBlockShaders
+ _OBJC_METACLASS_$_LCBConfig
+ _OBJC_METACLASS_$_LCBCorrection
+ _OBJC_METACLASS_$_LCBCorrectionShaders
+ _OBJC_METACLASS_$_LCBDetection
+ _OBJC_METACLASS_$_LCBDetector
+ _OBJC_METACLASS_$_LCBDetectorShaders
+ _OBJC_METACLASS_$_LCBExtractor
+ _OBJC_METACLASS_$_LCBExtractorShaders
+ _OBJC_METACLASS_$_LCBFiltering
+ _OBJC_METACLASS_$_LCBFilteringShaders
+ _OBJC_METACLASS_$_LCBMitigation
+ _OBJC_METACLASS_$_LCBMitigationResult
+ _OBJC_METACLASS_$_LCBPerFrameFilteringResults
+ _OBJC_METACLASS_$_LCBPyramid
+ _OBJC_METACLASS_$_LCBPyramidShaders
+ _OBJC_METACLASS_$_LCBTemporalFilteringResults
+ _OBJC_METACLASS_$_LCBTransformedEntry
+ _OBJC_METACLASS_$_RawNightModeDeblurInference
+ _OBJC_METACLASS_$_RawNightModeDeblurInferenceData
+ _OBJC_METACLASS_$_UDNet
+ _OBJC_METACLASS_$_UDNetNetworkParameters
+ _OBJC_METACLASS_$_UDNetNetworkStage
+ _OBJC_METACLASS_$_UDNetPlist
+ _OBJC_METACLASS_$_UDNetPostNetworkStage
+ _OBJC_METACLASS_$_UDNetPreNetworkStage
+ __OBJC_$_CATEGORY_CMILCBDatabase_$_TransformedEntry
+ __OBJC_$_CATEGORY_CMILCBEntry_$_TransformedEntry
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CMILCBDatabase_$_TransformedEntry
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_CMILCBEntry_$_TransformedEntry
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSArray_$_TransformedEntry
+ __OBJC_$_CATEGORY_NSArray_$_TransformedEntry
+ __OBJC_$_CLASS_METHODS_FlareSourceDetector
+ __OBJC_$_CLASS_METHODS_FlareSourceDetectorInputFrame
+ __OBJC_$_CLASS_METHODS_FlareSourceDetectorPlist
+ __OBJC_$_CLASS_METHODS_LCBCorrection
+ __OBJC_$_CLASS_METHODS_LCBDetector
+ __OBJC_$_CLASS_METHODS_LCBExtractor
+ __OBJC_$_CLASS_METHODS_LCBFiltering
+ __OBJC_$_CLASS_METHODS_LCBMitigation
+ __OBJC_$_CLASS_METHODS_LCBPyramid
+ __OBJC_$_CLASS_METHODS_UDNet
+ __OBJC_$_CLASS_METHODS_UDNetNetworkStage
+ __OBJC_$_CLASS_METHODS_UDNetPlist
+ __OBJC_$_INSTANCE_METHODS_FlareSourceDetector
+ __OBJC_$_INSTANCE_METHODS_FlareSourceDetectorInputFrame
+ __OBJC_$_INSTANCE_METHODS_FlareSourceDetectorPlist
+ __OBJC_$_INSTANCE_METHODS_H13FastBayerProcConfig(LCB|HRD|SSC|RNF|FlareDetection|GOC|HR|HOCLBin|Huemap|AdaptiveImbalanceCorrection)
+ __OBJC_$_INSTANCE_METHODS_LCBBlock
+ __OBJC_$_INSTANCE_METHODS_LCBBlockShaders
+ __OBJC_$_INSTANCE_METHODS_LCBConfig
+ __OBJC_$_INSTANCE_METHODS_LCBCorrection
+ __OBJC_$_INSTANCE_METHODS_LCBCorrectionShaders
+ __OBJC_$_INSTANCE_METHODS_LCBDetection
+ __OBJC_$_INSTANCE_METHODS_LCBDetector
+ __OBJC_$_INSTANCE_METHODS_LCBDetectorShaders
+ __OBJC_$_INSTANCE_METHODS_LCBExtractor
+ __OBJC_$_INSTANCE_METHODS_LCBExtractorShaders
+ __OBJC_$_INSTANCE_METHODS_LCBFiltering
+ __OBJC_$_INSTANCE_METHODS_LCBFilteringShaders
+ __OBJC_$_INSTANCE_METHODS_LCBMitigation
+ __OBJC_$_INSTANCE_METHODS_LCBMitigationResult
+ __OBJC_$_INSTANCE_METHODS_LCBPerFrameFilteringResults
+ __OBJC_$_INSTANCE_METHODS_LCBPyramid
+ __OBJC_$_INSTANCE_METHODS_LCBPyramidShaders
+ __OBJC_$_INSTANCE_METHODS_LCBTemporalFilteringResults
+ __OBJC_$_INSTANCE_METHODS_LCBTransformedEntry
+ __OBJC_$_INSTANCE_METHODS_RawNightModeDeblurInference
+ __OBJC_$_INSTANCE_METHODS_RawNightModeDeblurInferenceData
+ __OBJC_$_INSTANCE_METHODS_SoftISPCalibrationConfig(LCB)
+ __OBJC_$_INSTANCE_METHODS_UDNet
+ __OBJC_$_INSTANCE_METHODS_UDNetNetworkParameters
+ __OBJC_$_INSTANCE_METHODS_UDNetNetworkStage
+ __OBJC_$_INSTANCE_METHODS_UDNetPlist
+ __OBJC_$_INSTANCE_METHODS_UDNetPostNetworkStage
+ __OBJC_$_INSTANCE_METHODS_UDNetPreNetworkStage
+ __OBJC_$_INSTANCE_VARIABLES_FlareSourceDetector
+ __OBJC_$_INSTANCE_VARIABLES_FlareSourceDetectorInputFrame
+ __OBJC_$_INSTANCE_VARIABLES_FlareSourceDetectorPlist
+ __OBJC_$_INSTANCE_VARIABLES_LCBBlock
+ __OBJC_$_INSTANCE_VARIABLES_LCBBlockShaders
+ __OBJC_$_INSTANCE_VARIABLES_LCBConfig
+ __OBJC_$_INSTANCE_VARIABLES_LCBCorrection
+ __OBJC_$_INSTANCE_VARIABLES_LCBCorrectionShaders
+ __OBJC_$_INSTANCE_VARIABLES_LCBDetection
+ __OBJC_$_INSTANCE_VARIABLES_LCBDetector
+ __OBJC_$_INSTANCE_VARIABLES_LCBDetectorShaders
+ __OBJC_$_INSTANCE_VARIABLES_LCBExtractor
+ __OBJC_$_INSTANCE_VARIABLES_LCBExtractorShaders
+ __OBJC_$_INSTANCE_VARIABLES_LCBFiltering
+ __OBJC_$_INSTANCE_VARIABLES_LCBFilteringShaders
+ __OBJC_$_INSTANCE_VARIABLES_LCBMitigation
+ __OBJC_$_INSTANCE_VARIABLES_LCBMitigationResult
+ __OBJC_$_INSTANCE_VARIABLES_LCBPerFrameFilteringResults
+ __OBJC_$_INSTANCE_VARIABLES_LCBPyramid
+ __OBJC_$_INSTANCE_VARIABLES_LCBPyramidShaders
+ __OBJC_$_INSTANCE_VARIABLES_LCBTemporalFilteringResults
+ __OBJC_$_INSTANCE_VARIABLES_LCBTransformedEntry
+ __OBJC_$_INSTANCE_VARIABLES_RawNightModeDeblurInference
+ __OBJC_$_INSTANCE_VARIABLES_RawNightModeDeblurInferenceData
+ __OBJC_$_INSTANCE_VARIABLES_UDNet
+ __OBJC_$_INSTANCE_VARIABLES_UDNetNetworkParameters
+ __OBJC_$_INSTANCE_VARIABLES_UDNetNetworkStage
+ __OBJC_$_INSTANCE_VARIABLES_UDNetPlist
+ __OBJC_$_INSTANCE_VARIABLES_UDNetPostNetworkStage
+ __OBJC_$_INSTANCE_VARIABLES_UDNetPreNetworkStage
+ __OBJC_$_PROP_LIST_FlareSourceDetector
+ __OBJC_$_PROP_LIST_FlareSourceDetectorInputFrame
+ __OBJC_$_PROP_LIST_LCBBlock
+ __OBJC_$_PROP_LIST_LCBBlockShaders
+ __OBJC_$_PROP_LIST_LCBConfig
+ __OBJC_$_PROP_LIST_LCBCorrection
+ __OBJC_$_PROP_LIST_LCBCorrectionShaders
+ __OBJC_$_PROP_LIST_LCBDetector
+ __OBJC_$_PROP_LIST_LCBDetectorShaders
+ __OBJC_$_PROP_LIST_LCBExtractor
+ __OBJC_$_PROP_LIST_LCBExtractorShaders
+ __OBJC_$_PROP_LIST_LCBFiltering
+ __OBJC_$_PROP_LIST_LCBFilteringShaders
+ __OBJC_$_PROP_LIST_LCBMitigationResult
+ __OBJC_$_PROP_LIST_LCBPerFrameFilteringResults
+ __OBJC_$_PROP_LIST_LCBPyramid
+ __OBJC_$_PROP_LIST_LCBPyramidShaders
+ __OBJC_$_PROP_LIST_LCBTemporalFilteringResults
+ __OBJC_$_PROP_LIST_LCBTransformedEntry
+ __OBJC_$_PROP_LIST_RawNightModeDeblurInference
+ __OBJC_$_PROP_LIST_RawNightModeDeblurInferenceData
+ __OBJC_$_PROP_LIST_UDNet
+ __OBJC_$_PROP_LIST_UDNetNetworkParameters
+ __OBJC_$_PROP_LIST_UDNetNetworkStage
+ __OBJC_$_PROP_LIST_UDNetPostNetworkStage
+ __OBJC_$_PROP_LIST_UDNetPreNetworkStage
+ __OBJC_$_PROTOCOL_CLASS_METHODS_LCBPrewarmableBlock
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LCBPrewarmableBlock
+ __OBJC_$_PROTOCOL_REFS_LCBPrewarmableBlock
+ __OBJC_CLASS_PROTOCOLS_$_FlareSourceDetectorInputFrame
+ __OBJC_CLASS_PROTOCOLS_$_LCBCorrection
+ __OBJC_CLASS_PROTOCOLS_$_LCBDetector
+ __OBJC_CLASS_PROTOCOLS_$_LCBExtractor
+ __OBJC_CLASS_PROTOCOLS_$_LCBFiltering
+ __OBJC_CLASS_PROTOCOLS_$_LCBPyramid
+ __OBJC_CLASS_PROTOCOLS_$_UDNetPostNetworkStage
+ __OBJC_CLASS_PROTOCOLS_$_UDNetPreNetworkStage
+ __OBJC_CLASS_RO_$_FlareSourceDetector
+ __OBJC_CLASS_RO_$_FlareSourceDetectorInputFrame
+ __OBJC_CLASS_RO_$_FlareSourceDetectorPlist
+ __OBJC_CLASS_RO_$_LCBBlock
+ __OBJC_CLASS_RO_$_LCBBlockShaders
+ __OBJC_CLASS_RO_$_LCBConfig
+ __OBJC_CLASS_RO_$_LCBCorrection
+ __OBJC_CLASS_RO_$_LCBCorrectionShaders
+ __OBJC_CLASS_RO_$_LCBDetection
+ __OBJC_CLASS_RO_$_LCBDetector
+ __OBJC_CLASS_RO_$_LCBDetectorShaders
+ __OBJC_CLASS_RO_$_LCBExtractor
+ __OBJC_CLASS_RO_$_LCBExtractorShaders
+ __OBJC_CLASS_RO_$_LCBFiltering
+ __OBJC_CLASS_RO_$_LCBFilteringShaders
+ __OBJC_CLASS_RO_$_LCBMitigation
+ __OBJC_CLASS_RO_$_LCBMitigationResult
+ __OBJC_CLASS_RO_$_LCBPerFrameFilteringResults
+ __OBJC_CLASS_RO_$_LCBPyramid
+ __OBJC_CLASS_RO_$_LCBPyramidShaders
+ __OBJC_CLASS_RO_$_LCBTemporalFilteringResults
+ __OBJC_CLASS_RO_$_LCBTransformedEntry
+ __OBJC_CLASS_RO_$_RawNightModeDeblurInference
+ __OBJC_CLASS_RO_$_RawNightModeDeblurInferenceData
+ __OBJC_CLASS_RO_$_UDNet
+ __OBJC_CLASS_RO_$_UDNetNetworkParameters
+ __OBJC_CLASS_RO_$_UDNetNetworkStage
+ __OBJC_CLASS_RO_$_UDNetPlist
+ __OBJC_CLASS_RO_$_UDNetPostNetworkStage
+ __OBJC_CLASS_RO_$_UDNetPreNetworkStage
+ __OBJC_LABEL_PROTOCOL_$_LCBPrewarmableBlock
+ __OBJC_METACLASS_RO_$_FlareSourceDetector
+ __OBJC_METACLASS_RO_$_FlareSourceDetectorInputFrame
+ __OBJC_METACLASS_RO_$_FlareSourceDetectorPlist
+ __OBJC_METACLASS_RO_$_LCBBlock
+ __OBJC_METACLASS_RO_$_LCBBlockShaders
+ __OBJC_METACLASS_RO_$_LCBConfig
+ __OBJC_METACLASS_RO_$_LCBCorrection
+ __OBJC_METACLASS_RO_$_LCBCorrectionShaders
+ __OBJC_METACLASS_RO_$_LCBDetection
+ __OBJC_METACLASS_RO_$_LCBDetector
+ __OBJC_METACLASS_RO_$_LCBDetectorShaders
+ __OBJC_METACLASS_RO_$_LCBExtractor
+ __OBJC_METACLASS_RO_$_LCBExtractorShaders
+ __OBJC_METACLASS_RO_$_LCBFiltering
+ __OBJC_METACLASS_RO_$_LCBFilteringShaders
+ __OBJC_METACLASS_RO_$_LCBMitigation
+ __OBJC_METACLASS_RO_$_LCBMitigationResult
+ __OBJC_METACLASS_RO_$_LCBPerFrameFilteringResults
+ __OBJC_METACLASS_RO_$_LCBPyramid
+ __OBJC_METACLASS_RO_$_LCBPyramidShaders
+ __OBJC_METACLASS_RO_$_LCBTemporalFilteringResults
+ __OBJC_METACLASS_RO_$_LCBTransformedEntry
+ __OBJC_METACLASS_RO_$_RawNightModeDeblurInference
+ __OBJC_METACLASS_RO_$_RawNightModeDeblurInferenceData
+ __OBJC_METACLASS_RO_$_UDNet
+ __OBJC_METACLASS_RO_$_UDNetNetworkParameters
+ __OBJC_METACLASS_RO_$_UDNetNetworkStage
+ __OBJC_METACLASS_RO_$_UDNetPlist
+ __OBJC_METACLASS_RO_$_UDNetPostNetworkStage
+ __OBJC_METACLASS_RO_$_UDNetPreNetworkStage
+ __OBJC_PROTOCOL_$_LCBPrewarmableBlock
+ ___24-[UDNetNetworkStage run]_block_invoke
+ ___24-[UDNetNetworkStage run]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e8_v12?0i8ls32l8
+ _cosf
+ _createRadiusLookUpTextureAndConfig:.circleRadiiSqrd
+ _determineEnablementParams
+ _effectiveApertureDiameterUmFromBrightnessLut
+ _enableFlareSourceDetectorOverride
+ _enableUDNetOverride
+ _kFigCaptureCameraInfoKey_IsQuadraSensor
+ _kFigCapturePropertyValue_ModuleSerialNumberString
+ _kFigCaptureSampleBufferMetadata_EffectiveApertureDiameter
+ _kFigCaptureSampleBufferMetadata_FocusAccelerometerVector
+ _kFigCaptureSampleBufferMetadata_LCBMitigation
+ _kFigCaptureSampleBufferMetadata_LCBMitigationKey_DetectionCountHistogram
+ _kFigCaptureSampleBufferMetadata_LCBMitigationKey_NumberCorrectedOnIRCF
+ _kFigCaptureSampleBufferMetadata_LCBMitigationKey_NumberCorrectedOnLens
+ _kFigCaptureSampleBufferMetadata_LCBMitigationKey_NumberDetected
+ _kFigCaptureSampleBufferMetadata_NRFFlareDiscrepancyDetected
+ _kFigCaptureStillImageProcessingMetadataKey_StillImageNRFProcessingFlags
+ _kFigCaptureStreamMetadata_ApertureDiameter
+ _kFigCaptureStreamMetadata_FocusLensPosition
+ _kNRF_FlareSourceDetector
+ _kNRF_LFType_LF24
+ _kNRF_LFType_LF48
+ _kNRF_UDNet
+ _objc_copyStruct
+ _objc_msgSend$_autoEnableDNRBypassIfNeeded
+ _objc_msgSend$_initRawNightModeDenoiseInference:isBarrington:isReno:isArgyleTripodMax:
+ _objc_msgSend$_initRawNightModeFusionInference:isBarrington:isReno:requiresDarkCurrentNoiseModel:
+ _objc_msgSend$_isReno:
+ _objc_msgSend$_setupCalculatedProperties
+ _objc_msgSend$addEntries:
+ _objc_msgSend$addbackParams
+ _objc_msgSend$allObjects
+ _objc_msgSend$apertureRatio
+ _objc_msgSend$applyCorrection
+ _objc_msgSend$applyCorrectionMap:toRawFrame:config:error:
+ _objc_msgSend$captureGravityVector
+ _objc_msgSend$captureTimeStamp
+ _objc_msgSend$clearLUT
+ _objc_msgSend$clipNetworkInputs
+ _objc_msgSend$cmi_simdFloat3ValueForKey:defaultValue:found:
+ _objc_msgSend$cmi_simdInt2ValueForXKey:yKey:defaultValue:found:
+ _objc_msgSend$completionHandler
+ _objc_msgSend$computeAdaptiveFusionTuningPlist:fromInputPlist:quadraBinningFactor:
+ _objc_msgSend$computeYUVNoiseMapWithNoiseLumaTex:noiseChromaTex:
+ _objc_msgSend$correctionEnabled
+ _objc_msgSend$correctionFeatures
+ _objc_msgSend$correctionLUT
+ _objc_msgSend$corrections
+ _objc_msgSend$createCorrection
+ _objc_msgSend$createCorrectionMapForLevel:filteredLCBsForLevel:correctionLUT:previousLevel:config:error:
+ _objc_msgSend$createMetalBuffer:length:
+ _objc_msgSend$createMetalTexture:pixelFormat:width:height:
+ _objc_msgSend$createRadiusLookUpTextureAndConfig:
+ _objc_msgSend$databaseUpdateEnabled
+ _objc_msgSend$defocusRadius
+ _objc_msgSend$defocusRadiusForIRCF
+ _objc_msgSend$defocusRadiusForLens
+ _objc_msgSend$deleteEntries:
+ _objc_msgSend$demosaicBayer
+ _objc_msgSend$demosaicBayerToLuma:config:error:
+ _objc_msgSend$demosaicBayerToLumaAndDownsample2x:config:error:
+ _objc_msgSend$demosaicBayerYRGB
+ _objc_msgSend$demosaicDownsampleBayer
+ _objc_msgSend$demosaicDownsampleBayerYRGB
+ _objc_msgSend$demosaicDownsampleQuadra
+ _objc_msgSend$demosaicDownsampleQuadraYRGB
+ _objc_msgSend$demosaicQuadra
+ _objc_msgSend$demosaicQuadraToLumaAndDownsample2x:config:error:
+ _objc_msgSend$demosaicQuadraToLumaAndDownsample4x:config:error:
+ _objc_msgSend$demosaicQuadraYRGB
+ _objc_msgSend$detectionCount
+ _objc_msgSend$detectionCountHistogram
+ _objc_msgSend$detectionEnabled
+ _objc_msgSend$dimensionsForPyramidLevel:
+ _objc_msgSend$downsampleRGBInPlaceIfNeeded:outputBuffer:
+ _objc_msgSend$downsampleRGBTexture:toRGBTexture:
+ _objc_msgSend$downsampleTexture:levelIndex:config:error:
+ _objc_msgSend$downsampleYRGB
+ _objc_msgSend$entries
+ _objc_msgSend$entriesByKey
+ _objc_msgSend$extractionEnabled
+ _objc_msgSend$filteredLCBsBuf
+ _objc_msgSend$firstPyramidLevel
+ _objc_msgSend$focusLensPosition
+ _objc_msgSend$gainValue
+ _objc_msgSend$generateKeyForPosition:radius:pyramidLevel:lastDetectionGravityVector:lastDetectionTimeStamp:
+ _objc_msgSend$generateNewKeyFromConflictingKey:
+ _objc_msgSend$getCorrectionConfig:
+ _objc_msgSend$getDetectionExtractionConfig:forPyramidLevel:
+ _objc_msgSend$getDetectionResultSync:
+ _objc_msgSend$getLCBConfigForInputFrame:bounds:awb:
+ _objc_msgSend$getLCBConfigForInputFrame:bounds:correctionEnabled:awb:
+ _objc_msgSend$getLCBEnabledForInputFrame:processingOptions:lcbEnabled:
+ _objc_msgSend$getPerFrameFilteringConfig:
+ _objc_msgSend$getPyramidConfig:
+ _objc_msgSend$getTileCountForWidth:height:
+ _objc_msgSend$hrGainDownRatio
+ _objc_msgSend$initForSensorID:moduleSerial:
+ _objc_msgSend$initWithDetectedLCB:
+ _objc_msgSend$initWithDetectionOnPyramidLevel:positionInPyramid:pyramidRadius:config:
+ _objc_msgSend$initWithFilteredLCBsBuf:correctionLUT:
+ _objc_msgSend$initWithKey:position:radius:defocusRadius:particleDistance:apertureRatio:focusLensPosition:oisShift:opticalCenter:detectionCount:relativeToLens:lastDetectionGravityVector:lastDetectionTimeStamp:shouldCorrect:correctionFeatures:config:
+ _objc_msgSend$initWithMetalContext:isQuadra:
+ _objc_msgSend$initWithMetalContext:isQuadra:isBarrington:isReno:requiresDarkCurrentNoiseModel:
+ _objc_msgSend$initWithNumberOfDetections:numberOfCorrectionsOnIRCF:numberOfCorrectionsOnLens:corrections:detectionCountHistogram:
+ _objc_msgSend$initWithNumberOfNewPositiveDetections:numberOfMatchedPositiveDetections:numberOfPositiveExtractions:numberOfNegativeExtractions:numberOfCorrectionsOnIRCF:numberOfCorrectionsOnLens:corrections:detectionCountHistogram:
+ _objc_msgSend$initWithTileWidth:tileHeight:
+ _objc_msgSend$initWithTuningParameters:frameMetadata:cameraInfo:inputOffsetWithinSensorInBayerPixels:inputDimensionsInBayerPixels:cfaLayout:firstPixel:enableDetection:enableCorrection:awb:
+ _objc_msgSend$inputChromaTexture
+ _objc_msgSend$inputDimensionsInBayerPixels
+ _objc_msgSend$inputLSCMetadata
+ _objc_msgSend$inputLSCTexture
+ _objc_msgSend$inputLumaTexture
+ _objc_msgSend$inputMetadata
+ _objc_msgSend$inputNoiseMapTexture
+ _objc_msgSend$inputNoiseScalingFactor
+ _objc_msgSend$inputOffsetInBayerPixels
+ _objc_msgSend$inputPyramidEnabled
+ _objc_msgSend$insideFrame
+ _objc_msgSend$key
+ _objc_msgSend$lastDetectionGravityVector
+ _objc_msgSend$lastDetectionTimeStamp
+ _objc_msgSend$lastPyramidLevel
+ _objc_msgSend$lcbDetector
+ _objc_msgSend$lcbExtractor
+ _objc_msgSend$localMaximaFinder
+ _objc_msgSend$lowPassNPyramidLevels
+ _objc_msgSend$lscMetadata
+ _objc_msgSend$lscTexture
+ _objc_msgSend$lumaConversionCoefficients
+ _objc_msgSend$maxCorrectionFeaturesUpdateAmount
+ _objc_msgSend$maxDetectionCount
+ _objc_msgSend$maxRadiusUpdateDecrement
+ _objc_msgSend$maxRadiusUpdateIncrement
+ _objc_msgSend$maximumDetectionScoreForNoLCB
+ _objc_msgSend$maximumNumberOfCorrectionsPerLevel
+ _objc_msgSend$maximumNumberOfDetectionsPerLevel
+ _objc_msgSend$maximumNumberOfExtractionsPerLevel
+ _objc_msgSend$metalContext
+ _objc_msgSend$minCorrectionFeaturesLearningRate
+ _objc_msgSend$minimumConfidence
+ _objc_msgSend$minimumDetectionCountForCorrection
+ _objc_msgSend$minimumDetectionScoreForLCB
+ _objc_msgSend$minimumGravityVectorChange
+ _objc_msgSend$minimumTimeDelta
+ _objc_msgSend$moduleSerial
+ _objc_msgSend$nLCBsCorrectedOnIRCF
+ _objc_msgSend$nLCBsCorrectedOnLens
+ _objc_msgSend$nLCBsDetected
+ _objc_msgSend$nPyramidLevels
+ _objc_msgSend$networkType
+ _objc_msgSend$noiseMapScalingBody
+ _objc_msgSend$noiseMapScalingSkin
+ _objc_msgSend$noiseMapScalingSky
+ _objc_msgSend$noiseModel
+ _objc_msgSend$notifyLCBDatabaseUpdated:forPortType:
+ _objc_msgSend$numberOfCorrectionsOnIRCF
+ _objc_msgSend$numberOfCorrectionsOnLens
+ _objc_msgSend$numberOfNewPositiveDetections
+ _objc_msgSend$numberOfPositiveExtractions
+ _objc_msgSend$oisShift
+ _objc_msgSend$oisShiftScalingFactorForIRCF
+ _objc_msgSend$oisShiftScalingFactorForLens
+ _objc_msgSend$opacityScaling
+ _objc_msgSend$opticalCenterForIRCF
+ _objc_msgSend$opticalCenterForLens
+ _objc_msgSend$outputCleanRGBTexture
+ _objc_msgSend$outputRGBTexture
+ _objc_msgSend$overlapsDetection:
+ _objc_msgSend$particleDistance
+ _objc_msgSend$particleDistanceForIRCF
+ _objc_msgSend$particleDistanceForLens
+ _objc_msgSend$perFrameFilterExtractedLCBs
+ _objc_msgSend$perFrameFilteringEnabled
+ _objc_msgSend$perFrameFilteringWithTemporalLCBs:extractionResults:levelIndex:config:error:
+ _objc_msgSend$position
+ _objc_msgSend$positionUpdateRate
+ _objc_msgSend$prepareForNetworkType:isQuadra:
+ _objc_msgSend$prewarmWithMetalContext:
+ _objc_msgSend$pyramidLevel
+ _objc_msgSend$pyramidPosition
+ _objc_msgSend$pyramidRadius
+ _objc_msgSend$radius
+ _objc_msgSend$radiusLearningRate
+ _objc_msgSend$readAdaptiveFusionPostProcessingTuningsPlist:quadraBinningFactor:
+ _objc_msgSend$relativeToLens
+ _objc_msgSend$relativeToLensRadiusThreshold
+ _objc_msgSend$replaceObjectAtIndex:withObject:
+ _objc_msgSend$reverseObjectEnumerator
+ _objc_msgSend$runDemosaicWithInputRawTex:outputRGBTexture:outputGain:frame:completion:
+ _objc_msgSend$runDetectorOnTexture:levelIndex:loresTexture:loresLevelIndex:config:lscMetadata:error:
+ _objc_msgSend$runExtractorForEntries:inputTexture:levelIndex:loresTexture:loresLevelIndex:config:lscMetadata:error:
+ _objc_msgSend$runLocalMaximaFinderOnDetectorResult:levelIndex:config:error:
+ _objc_msgSend$runOnInputYRGBTexture:inputPyramidLevel:targetSushiTexture:config:lscMetadata:lcbDatabase:didUpdateDatabase:error:
+ _objc_msgSend$runOnSushiRawFrame:config:lscMetadata:lcbDatabase:didUpdateDatabase:error:
+ _objc_msgSend$runWithInputMetadata:udNetPlist:gainValue:inputRGBTexture:inputLSCTexture:inputLSCMetadata:outputLumaTexture:outputChromaTexture:
+ _objc_msgSend$runWithInputMetadata:udNetPlist:inputLumaTexture:inputChromaTexture:inputLSCTexture:inputLSCMetadata:outputLumaTexture:outputChromaTexture:
+ _objc_msgSend$runWithInputMetadata:udNetPlist:inputRGBTexture:inputNoiseMapTexture:inputLSCTexture:inputLSCMetadata:outputRGBTexture:outputCleanRGBTexture:skipNoiseAddback:
+ _objc_msgSend$runWithTileCount:
+ _objc_msgSend$setAddbackParams:
+ _objc_msgSend$setClipNetworkInputs:
+ _objc_msgSend$setCompletionHandler:
+ _objc_msgSend$setGainValue:
+ _objc_msgSend$setHairMaskTexture:
+ _objc_msgSend$setHrGainDownRatio:
+ _objc_msgSend$setInputChromaTexture:
+ _objc_msgSend$setInputLSCMetadata:
+ _objc_msgSend$setInputLSCTexture:
+ _objc_msgSend$setInputLumaTexture:
+ _objc_msgSend$setInputMetadata:
+ _objc_msgSend$setInputNoiseMapTexture:
+ _objc_msgSend$setInputNoiseScalingFactor:
+ _objc_msgSend$setInputType:
+ _objc_msgSend$setLscGainMapTexture:
+ _objc_msgSend$setLscMetadata:
+ _objc_msgSend$setLscParams:
+ _objc_msgSend$setLscTexture:
+ _objc_msgSend$setNetworkType:
+ _objc_msgSend$setNoiseMapScalingBody:
+ _objc_msgSend$setNoiseMapScalingSkin:
+ _objc_msgSend$setNoiseMapScalingSky:
+ _objc_msgSend$setNoiseModel:
+ _objc_msgSend$setOutputCleanRGBTexture:
+ _objc_msgSend$setPersonMaskTexture:
+ _objc_msgSend$setSkinMaskTexture:
+ _objc_msgSend$setSkipAWBInversion:
+ _objc_msgSend$setSkipLSCInversion:
+ _objc_msgSend$setSkipNoiseAddback:
+ _objc_msgSend$setSkyMaskTexture:
+ _objc_msgSend$setTileOverlapX:
+ _objc_msgSend$setTileOverlapY:
+ _objc_msgSend$setTuningPlist:
+ _objc_msgSend$setUdNetPList:
+ _objc_msgSend$setUdNetPlist:
+ _objc_msgSend$setUpdatedLCBDatabase:
+ _objc_msgSend$setUseFullStrength:
+ _objc_msgSend$setupUDNet:isQuadra:
+ _objc_msgSend$setupWithNetworkType:isQuadra:
+ _objc_msgSend$shouldCorrect
+ _objc_msgSend$skipAWBInversion
+ _objc_msgSend$skipInferenceEnabled
+ _objc_msgSend$skipLSCInversion
+ _objc_msgSend$skipNoiseAddback
+ _objc_msgSend$skipPyrLevel0
+ _objc_msgSend$startDetectionOnEv0:
+ _objc_msgSend$temporalFilteringUpdateDatabase:detectionResultsForLevels:extractionSetForLevels:extractionResultsForLevels:config:didUpdateDatabase:error:
+ _objc_msgSend$transformedEntriesOnPyramidLevel:
+ _objc_msgSend$transformedEntriesOnPyramidLevelWithConfig:
+ _objc_msgSend$transformedToConfig:
+ _objc_msgSend$udNetPlist
+ _objc_msgSend$updateEntries:
+ _objc_msgSend$updateParametersFromMetadata:cameraInfoByPortType:lscGainMapParameters:tuningParameters:firstPix:isQuadra:requiresDarkCurrentNoiseModel:aeTargetGain:textureDimensions:skipAWBInversion:skipLSCInversion:clipNetworkInputs:
+ _objc_msgSend$updateParametersFromMetadata:cameraInfoByPortType:tuningParameters:lscGainMapParameters:firstPix:aeTargetGain:isQuadra:textureDimensions:skipAWBInversion:skipLSCInversion:clipNetworkInputs:
+ _objc_msgSend$updatedLCBDatabase
+ _objc_msgSend$useFullColor
+ _objc_msgSend$useFullStrength
+ _objc_msgSend$withDetectionCountDecremented
+ _objc_msgSend$withDetectionCountIncrementedAndUpdatedFeatures:updatedRadius:
+ _objc_msgSend$withUpdatedPosition:
+ _objc_setProperty_nonatomic_copy
- -[RawNightModeDenoiseInferenceCMITIPSharedParameters updateParametersFromMetadata:cameraInfoByPortType:tuningParameters:lscGainMapParameters:firstPix:aeTargetGain:isQuadra:textureDimensions:]
- -[RawNightModeFusionInference initWithMetalContext:isQuadra:isBarrington:requiresDarkCurrentNoiseModel:]
- -[RawNightModeFusionMetalStage updateParametersFromMetadata:cameraInfoByPortType:lscGainMapParameters:tuningParameters:firstPix:isQuadra:requiresDarkCurrentNoiseModel:aeTargetGain:textureDimensions:]
- -[RawNightModeProcessor _initRawNightModeDenoiseInference:isBarrington:isArgyleTripodMax:]
- -[RawNightModeProcessor _initRawNightModeFusionInference:isBarrington:requiresDarkCurrentNoiseModel:]
- GCC_except_table26
- __OBJC_$_INSTANCE_METHODS_H13FastBayerProcConfig(HRD|SSC|RNF|FlareDetection|GOC|HR|HOCLBin|Huemap|AdaptiveImbalanceCorrection)
- __OBJC_$_INSTANCE_METHODS_SoftISPCalibrationConfig
- _kFigCaptureStreamMetadata_AD
- _objc_msgSend$_initRawNightModeDenoiseInference:isBarrington:isArgyleTripodMax:
- _objc_msgSend$_initRawNightModeFusionInference:isBarrington:requiresDarkCurrentNoiseModel:
- _objc_msgSend$initWithMetalContext:isQuadra:isBarrington:requiresDarkCurrentNoiseModel:
- _objc_msgSend$updateParametersFromMetadata:cameraInfoByPortType:lscGainMapParameters:tuningParameters:firstPix:isQuadra:requiresDarkCurrentNoiseModel:aeTargetGain:textureDimensions:
- _objc_msgSend$updateParametersFromMetadata:cameraInfoByPortType:tuningParameters:lscGainMapParameters:firstPix:aeTargetGain:isQuadra:textureDimensions:
CStrings:
+ "! noiseModel.invalid"
+ "%@(nLCBsDetected=%d, nLCBsCorrectedOnIRCF=%d, nLCBsCorrectedOnLens=%d)"
+ "( processingType == NRF_ProcessingType_RawNightMode ) || ( processingType == NRF_ProcessingType_AdaptiveFusion )"
+ "+[UDNetNetworkStage prewarmShaders:]"
+ "-[FlareSourceDetector getDetectionResultSync:]"
+ "-[FlareSourceDetector initWithMetalContext:error:]"
+ "-[FlareSourceDetector startDetectionOnEv0:]"
+ "-[RawNightModeDenoiseInferenceCMITIPSharedParameters updateParametersFromMetadata:cameraInfoByPortType:tuningParameters:lscGainMapParameters:firstPix:aeTargetGain:isQuadra:textureDimensions:skipAWBInversion:skipLSCInversion:clipNetworkInputs:]"
+ "-[RawNightModeProcessor _autoEnableDNRBypassIfNeeded]"
+ "-[RawNightModeProcessor processInitialFrames:]"
+ "-[UDNet initWithMetalContext:error:]"
+ "-[UDNet runWithInputMetadata:udNetPlist:gainValue:inputRGBTexture:inputLSCTexture:inputLSCMetadata:outputLumaTexture:outputChromaTexture:]"
+ "-[UDNet runWithInputMetadata:udNetPlist:inputLumaTexture:inputChromaTexture:inputLSCTexture:inputLSCMetadata:outputLumaTexture:outputChromaTexture:]"
+ "-[UDNet runWithInputMetadata:udNetPlist:inputRGBTexture:inputNoiseMapTexture:inputLSCTexture:inputLSCMetadata:outputRGBTexture:outputCleanRGBTexture:skipNoiseAddback:]"
+ "-[UDNet setupWithNetworkType:isQuadra:]"
+ "-[UDNetNetworkStage initWithMetalContext:error:]"
+ "-[UDNetNetworkStage prepareForNetworkType:isQuadra:]"
+ "-[UDNetNetworkStage run]"
+ "-[UDNetPostNetworkStage initWithMetalContext:]"
+ "-[UDNetPostNetworkStage processTilePipelineStage:]"
+ "-[UDNetPreNetworkStage initWithMetalContext:]"
+ "-[UDNetPreNetworkStage processTilePipelineStage:]"
+ "0x0916"
+ "2"
+ "<<<< CMIPost >>>> %s: Running UDNet"
+ "<<<< CMIPost >>>> %s: _udnetStage nil"
+ "<<<< CMIPost >>>> %s: textureDescriptor is nil"
+ "<<<< CMIPost >>>> %s: udNetStage runWithInputMetadata failed with err=%d"
+ "<<<< FlareSourceDetector >>>> %s: [super init] is nil"
+ "<<<< FlareSourceDetector >>>> %s: _computeLocalMinPSO is nil"
+ "<<<< FlareSourceDetector >>>> %s: _computeLumaAndDownsampleBayerR16PSO is nil"
+ "<<<< FlareSourceDetector >>>> %s: _computeLumaAndDownsampleQuadPackedPSO is nil"
+ "<<<< FlareSourceDetector >>>> %s: _countFlareSourcePixelsPSO is nil"
+ "<<<< FlareSourceDetector >>>> %s: _downsampleLumaOnlyPSO is nil"
+ "<<<< FlareSourceDetector >>>> %s: _evaluateGatePSO is nil"
+ "<<<< FlareSourceDetector >>>> %s: cb nil"
+ "<<<< FlareSourceDetector >>>> %s: detection already in flight, must getDetectionResultSync before starting again"
+ "<<<< FlareSourceDetector >>>> %s: dsLuma alloc failed"
+ "<<<< FlareSourceDetector >>>> %s: enc nil"
+ "<<<< FlareSourceDetector >>>> %s: ev0 nil"
+ "<<<< FlareSourceDetector >>>> %s: ev0.baseTex nil"
+ "<<<< FlareSourceDetector >>>> %s: ev0.lscGainMapTexture nil"
+ "<<<< FlareSourceDetector >>>> %s: ev0.properties.meta.exposureParams nil"
+ "<<<< FlareSourceDetector >>>> %s: hr_gain_down_ratio must be > 0"
+ "<<<< FlareSourceDetector >>>> %s: localMin alloc failed"
+ "<<<< FlareSourceDetector >>>> %s: metalContext is nil"
+ "<<<< FlareSourceDetector >>>> %s: outIsFlareDetected nil"
+ "<<<< FlareSourceDetector >>>> %s: rawInput too small for downsample"
+ "<<<< FlareSourceDetector >>>> %s: result buffer alloc failed"
+ "<<<< FlareSourceDetector >>>> %s: td alloc failed"
+ "<<<< FlareSourceDetector >>>> Fig"
+ "<<<< FlareSourceDetectorPlist >>>> Fig"
+ "<<<< LearnedHRNRProcessor >>>> %s: Failed to init UDNet"
+ "<<<< LearnedHRNRProcessor >>>> %s: cannot bind lscGainMapTexture"
+ "<<<< LearnedNRNetworkStage >>>> %s: RGB output requires useFullStrength to be enabled"
+ "<<<< RawDFProcessor >>>> %s: Failed to init FlareSourceDetector (%d)"
+ "<<<< RawDFProcessor >>>> %s: FlareSourceDetector: isFlareDetected=%d"
+ "<<<< RawDFProcessor >>>> %s: _udNetStage is nil"
+ "<<<< RawDFProcessor >>>> %s: cannot bind lscGainMapTexture"
+ "<<<< RawDFProcessor >>>> %s: flareSourceDetector getDetectionResultSync failed: %d"
+ "<<<< RawDFTuning >>>> %s: flareSourceDetectorPlist readPlist failed"
+ "<<<< RawDFTuning >>>> %s: udnetPlist readPlist failed"
+ "<<<< RawNightMode >>>> %s: Flicker detected in EVM frame, aborting Adaptive Fusion"
+ "<<<< RawNightMode >>>> %s: RawNM AdaptiveFusion (no EVM) FlareSourceDetector: isFlareDetected=%d"
+ "<<<< RawNightMode >>>> %s: RawNightMode: auto-enabling DNR bypass for 2-frame AdaptiveFusion capture (reloading DNR TIP)"
+ "<<<< RawNightMode >>>> %s: flareSourceDetector getDetectionResultSync failed: %d"
+ "<<<< UBProcessor >>>> %s: Failed to build LumaChromaImage for FSD"
+ "<<<< UBProcessor >>>> %s: FlareSourceDetector: isFlareDetected=%d"
+ "<<<< UBProcessor >>>> %s: flareSourceDetector getDetectionResultSync failed: %d"
+ "<<<< UDNet >>>> %s: Reloading UDNet for networkType:%d"
+ "<<<< UDNet >>>> %s: _UDNetNetworkStage not valid!"
+ "<<<< UDNet >>>> %s: _cameraInfoByPortType is nil"
+ "<<<< UDNet >>>> %s: _metalContext is not valid"
+ "<<<< UDNet >>>> %s: inputChromaTexture is nil"
+ "<<<< UDNet >>>> %s: inputLSCMetadata is nil"
+ "<<<< UDNet >>>> %s: inputLSCTexture is nil"
+ "<<<< UDNet >>>> %s: inputLumaTexture is nil"
+ "<<<< UDNet >>>> %s: inputRGBTexture is nil"
+ "<<<< UDNet >>>> %s: metadata is nil"
+ "<<<< UDNet >>>> %s: outputChromaTexture is nil"
+ "<<<< UDNet >>>> %s: outputLumaTexture is nil"
+ "<<<< UDNet >>>> %s: outputRGBTexture is nil"
+ "<<<< UDNet >>>> %s: udNetPlist is nil"
+ "<<<< UDNet >>>> Fig"
+ "<<<< UDNetNetworkStage >>>>"
+ "<<<< UDNetNetworkStage >>>> %s: "
+ "<<<< UDNetNetworkStage >>>> %s: Detected unsupported input arguments"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to allocate CMITiledInferenceProcessorTilePipelineStage for UDNet"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to allocate network configuration"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to allocate postInferenceStage"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to allocate preInferenceStage"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to allocated CMITiledInferenceProcessorConfig"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to allocated UDNetSharedParameters"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to find UDNet network path"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to initialise _UDNetTiledInferenceProcessor"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to pre warm postInferenceStage"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to pre warm preInferenceStage"
+ "<<<< UDNetNetworkStage >>>> %s: Failed to run TIP for UDNet"
+ "<<<< UDNetNetworkStage >>>> %s: Noise Model is invalid"
+ "<<<< UDNetNetworkStage >>>> %s: Tile dimensions invalid (width=%d, height=%d)"
+ "<<<< UDNetNetworkStage >>>> %s: _networkParameters.inputChromaTexture is nil"
+ "<<<< UDNetNetworkStage >>>> %s: _networkParameters.inputLumaTexture is nil"
+ "<<<< UDNetNetworkStage >>>> %s: _networkParameters.inputNoiseMapTexture is nil"
+ "<<<< UDNetNetworkStage >>>> %s: _udNetPlist is nil"
+ "<<<< UDNetNetworkStage >>>> %s: commandEncoder is nil"
+ "<<<< UDNetNetworkStage >>>> %s: failed to allocate super"
+ "<<<< UDNetNetworkStage >>>> %s: failed to init super"
+ "<<<< UDNetNetworkStage >>>> %s: gainValue must be 1.0 for AdaptiveFusion, got %f"
+ "<<<< UDNetNetworkStage >>>> %s: metalContext not valid"
+ "<<<< UDNetNetworkStage >>>> %s: network type is not valid"
+ "<<<< UDNetNetworkStage >>>> %s: networkInput is nil"
+ "<<<< UDNetNetworkStage >>>> %s: networkOutputRGB is nil"
+ "<<<< UDNetNetworkStage >>>> Fig"
+ "<<<< UDNetPlist >>>> Fig"
+ "AdaptiveFusion"
+ "AdaptiveFusionParameters"
+ "AddbackClampFactor"
+ "AddbackLumaAddbackThreshold"
+ "AddbackLumaAddbackWeight"
+ "AddbackNoiseScalingFactor"
+ "ApplySkinColorMitigationCCM"
+ "Cannot bind lscGainMapTexture for referenceFrame"
+ "ClippingThreshold"
+ "DarkPixelThreshold"
+ "DeblurOutputCleanRGB"
+ "DeblurOutputRGB"
+ "DefocusRadiusOffsetForIRCF"
+ "DefocusRadiusOffsetForLens"
+ "DefocusRadiusSlopeForIRCF"
+ "DefocusRadiusSlopeForLens"
+ "DetectionLocalityThreshold"
+ "DetectionScoreDarkLower"
+ "DetectionScoreDarkUpper"
+ "DetectionScoreEdgeLower"
+ "DetectionScoreEdgeUpper"
+ "DetectionScoreImprovementLower"
+ "DetectionScoreImprovementUpper"
+ "Diameter"
+ "DownsizedNoise"
+ "DownsizedRGB"
+ "EffectiveApertureLut"
+ "EnableFlareSourceDetector"
+ "EnableUDNet"
+ "FirstPyramidLevel"
+ "FlareSourceDetected"
+ "FlareSourceDetector"
+ "FlareSourceDetector.SingleImageParameters"
+ "FlareSourceDetector::computeLocalMin"
+ "FlareSourceDetector::computeLumaAndDownsampleBayerR16"
+ "FlareSourceDetector::computeLumaAndDownsampleQuadPacked"
+ "FlareSourceDetector::countFlareSourcePixels"
+ "FlareSourceDetector::downsampleLumaOnly"
+ "FlareSourceDetector::evaluateGate"
+ "FlareSourceDetectorPlistV4.m"
+ "FlareSourceDetectorV4.m"
+ "H13FastBayerProcConfig+LCB.m"
+ "IgnoreMissingMetadataMask"
+ "InnerOuterVarEdgeLower"
+ "InnerOuterVarEdgeUpper"
+ "InputNoiseScalingFactor"
+ "InputNoiseScalingFactorBody"
+ "InputNoiseScalingFactorSkin"
+ "InputNoiseScalingFactorSky"
+ "LCB"
+ "LCB::Correction::applyCorrection"
+ "LCB::Correction::createCorrection"
+ "LCB::Detector::lcbDetector"
+ "LCB::Detector::localMaximaFinder"
+ "LCB::Extractor::lcbExtractor"
+ "LCB::Filtering::clearLUT"
+ "LCB::Filtering::perFrameFilterExtractedLCBs"
+ "LCB::Pyramid::demosaicBayer"
+ "LCB::Pyramid::demosaicBayerYRGB"
+ "LCB::Pyramid::demosaicDownsampleBayer"
+ "LCB::Pyramid::demosaicDownsampleQuadra"
+ "LCB::Pyramid::demosaicDownsampleQuadraYRGB"
+ "LCB::Pyramid::demosaicQuadra"
+ "LCB::Pyramid::demosaicQuadraYRGB"
+ "LCB::Pyramid::downsample"
+ "LCB::Pyramid::downsampleYRGB"
+ "LCBBlock.m"
+ "LCBConfig.m"
+ "LCBCorrection.m"
+ "LCBDB"
+ "LCBDetector.m"
+ "LCBExtractor.m"
+ "LCBFiltering.m"
+ "LCBMitigation.m"
+ "LCBPyramid.m"
+ "LCBTransformedEntry.m"
+ "LF24"
+ "LF48"
+ "LastPyramidLevel"
+ "LearnedNR::fullStrengthAddbackForRawInput"
+ "LocalMinThreshold"
+ "LocalWindowSize"
+ "LowPassNPyramidLevels"
+ "LumaCoefficientsB"
+ "LumaCoefficientsG"
+ "LumaCoefficientsR"
+ "LumaGapThreshold"
+ "MaxCorrectionFeaturesUpdateAmount"
+ "MaxDetectionCount"
+ "MaxRadiusUpdateDecrement"
+ "MaxRadiusUpdateIncrement"
+ "MaximumCorrectionScaling"
+ "MaximumDetectionScoreForNoLCB"
+ "MaximumNumberOfCorrectionsPerLevel"
+ "MaximumNumberOfDetectionsPerLevel"
+ "MaximumNumberOfExtractionsPerLevel"
+ "MinApertureRatioForCorrection"
+ "MinApertureRatioForDetection"
+ "MinAreaRatio"
+ "MinCorrectionFeaturesLearningRate"
+ "MinPixelCount"
+ "MinimumConfidence"
+ "MinimumCorrectionScaling"
+ "MinimumDetectionCountForCorrection"
+ "MinimumDetectionScoreForLCB"
+ "MinimumGravityVectorChange"
+ "MinimumTimeDelta"
+ "NetworkType"
+ "NotStrongEdgeConfidenceLower"
+ "NotStrongEdgeConfidenceUpper"
+ "NotTooDarkConfidenceLower"
+ "NotTooDarkConfidenceScaling"
+ "NotTooDarkConfidenceUpper"
+ "NumOfEntry"
+ "OISShiftScalingFactorForIRCF"
+ "OISShiftScalingFactorForLens"
+ "ParticleDistanceOffsetForIRCF"
+ "ParticleDistanceOffsetForLens"
+ "ParticleDistanceSlopeForIRCF"
+ "ParticleDistanceSlopeForLens"
+ "PositionUpdateRate"
+ "RadiusLearningRate"
+ "RawNightModeDeblurInferenceV4.m"
+ "RelativeToLensRadiusThreshold"
+ "ResidualConfidenceDetailLower"
+ "ResidualConfidenceDetailUpper"
+ "ResidualConfidenceInOutVarLower"
+ "ResidualConfidenceInOutVarUpper"
+ "SoftISPCalibrationConfig+LCB.m"
+ "UDNet"
+ "UDNet.SingleImageParameters"
+ "UDNet::processInputTileRGB"
+ "UDNet::processInputTileYUV"
+ "UDNet::processOutputTileRGB"
+ "UDNet::processOutputTileYUV"
+ "UDNetNetworkStageV4.m"
+ "UDNetPlistV4.m"
+ "UDNetV4.m"
+ "UseFullColor"
+ "VABrightnessAdjFactor"
+ "Z"
+ "_apertureRatio"
+ "_apertureRatio > 0.0f"
+ "_applyCorrection"
+ "_clearLUT"
+ "_computeLocalMinPSO"
+ "_computeLumaAndDownsampleBayerR16PSO"
+ "_computeLumaAndDownsampleQuadPackedPSO"
+ "_correction"
+ "_countFlareSourcePixelsPSO"
+ "_createCorrection"
+ "_demosaicBayer"
+ "_demosaicBayerYRGB"
+ "_demosaicDownsampleBayer"
+ "_demosaicDownsampleBayerYRGB"
+ "_demosaicDownsampleQuadra"
+ "_demosaicDownsampleQuadraYRGB"
+ "_demosaicQuadra"
+ "_demosaicQuadraYRGB"
+ "_detector"
+ "_dnrNetworkPath"
+ "_downsampleLumaOnlyPSO"
+ "_downsampleYRGB"
+ "_evaluateGatePSO"
+ "_extractor"
+ "_filtering"
+ "_flareSourceDetector"
+ "_fullStrengthAddbackForRawInput = [metal computePipelineStateFor:@\"LearnedNR::fullStrengthAddbackForRawInput\" constants:((void *)0) fault:&err]"
+ "_inferenceDeblur"
+ "_lcb"
+ "_lcbDetector"
+ "_lcbExtractor"
+ "_localMaximaFinder"
+ "_networkParameters.inputChromaTexture"
+ "_networkParameters.inputLumaTexture"
+ "_networkParameters.networkType != UDNetNetworkTypeAdaptiveFusion || fabsf( _networkParameters.gainValue - 1.0f ) < 1.19209290e-7F"
+ "_perFrameFilterExtractedLCBs"
+ "_processInputTileRGB"
+ "_processInputTileYUV"
+ "_processOutputTileRGB"
+ "_processOutputTileYUV"
+ "_pyramid"
+ "_radiusLUT"
+ "_resultBuffer"
+ "_udNetPList"
+ "apertureDiameter > 0.0"
+ "apertureRatio"
+ "band0PyramidTexture"
+ "blemishDatabase"
+ "combinedDetections"
+ "combinedDetectionsData"
+ "correctionFeatures"
+ "correctionLUT"
+ "correctionMapTex"
+ "correctionsArray"
+ "currentPyrTex"
+ "database"
+ "deblurInferenceData"
+ "deblurOutputCleanRGB"
+ "deblurOutputRGB"
+ "defocusRadius"
+ "deletedEntries"
+ "demosaicedYRGBTex"
+ "detectionCount"
+ "detectionCountHistogram"
+ "detectionCountHistogramRaw"
+ "detectionResultPyramid"
+ "detectionsBuf"
+ "detectorResultTexture"
+ "downsampledNoise"
+ "dsLuma = [_metal.device newTextureWithDescriptor:td.desc]"
+ "dsW > 0 && dsH > 0"
+ "e"
+ "enableDetection || enableCorrection"
+ "enc"
+ "entries"
+ "error == 0 "
+ "ev0.baseTex"
+ "ev0.lscGainMapTexture"
+ "ev0.properties.meta.exposureParams"
+ "ev0Image && ev0Image->lumaTex"
+ "exp->hr_gain_down_ratio > 0.0f"
+ "extractionInput"
+ "extractionResult->pyramidLevel == extractionInput.pyramidLevel"
+ "extractionResultPyramid"
+ "extractionSetForLevels.count == extractionResultsForLevels.count"
+ "extractionSetPyramid"
+ "extractionsBuf"
+ "failed to allocate _networkStage"
+ "filteredArray"
+ "filteredLCBsBuf"
+ "flareSourceDetectorResult"
+ "focusLensPosition"
+ "found || ( ignoreMissingMetadataMask & IgnoreMissingMetadataType_ApertureRatio )"
+ "found || ( ignoreMissingMetadataMask & IgnoreMissingMetadataType_BayerSensorDimensions )"
+ "found || ( ignoreMissingMetadataMask & IgnoreMissingMetadataType_FocusLensPosition )"
+ "found || ( ignoreMissingMetadataMask & IgnoreMissingMetadataType_GravityVector )"
+ "found || ( ignoreMissingMetadataMask & IgnoreMissingMetadataType_QuadraSensor )"
+ "frameMetadata"
+ "gainValueArray"
+ "inputChromaTexture"
+ "inputLSCMetadata"
+ "inputLSCTexture"
+ "inputLumaTexture"
+ "inputNoiseScalingFactor"
+ "inputPyrTex"
+ "inputPyramid"
+ "inputPyramidTexturesToRelease"
+ "inputRGBTexture"
+ "inputYRGBTexture"
+ "input_rgb"
+ "key"
+ "lastDetectionGravityVector"
+ "lastDetectionTimeStamp"
+ "lcb.iPyr_%02d"
+ "lcb.iPyr_00"
+ "lcb.iPyr_01"
+ "lcb.p%02d_corLUT"
+ "lcb.p%02d_corrMap"
+ "lcb.p%02d_detBuf"
+ "lcb.p%02d_detScores"
+ "lcb.p%02d_extBuf"
+ "lcb.p%02d_fbBuf"
+ "lcbArray"
+ "lcbArrayData"
+ "lcbConfig"
+ "lcbDet"
+ "lcbEnabled"
+ "levelIndex > 0"
+ "levelIndex >= 0"
+ "localMin = [_metal.device newTextureWithDescriptor:td.desc]"
+ "loresLevelIndex >= 0"
+ "loresPyrTex"
+ "loresTexture"
+ "lscGainMapTexture"
+ "m"
+ "matchedDetection"
+ "modified"
+ "n > 1 && x.count == n && y.count == n"
+ "nCombinedDetections < maxNCombinedDetections"
+ "nLCBs <= 255"
+ "networkFullPath"
+ "networkOutputRGB"
+ "networkParameters"
+ "networkPath"
+ "newCorrectionTex"
+ "newEntries"
+ "nightmode-deblur-bayer-reno-v"
+ "nightmode-deblur-quadra-reno-v"
+ "nightmode-dnr-bayer-reno-v"
+ "nightmode-dnr-quadra-reno-v"
+ "nightmode_dnr_bayer_reno_v"
+ "nightmode_dnr_quadra_reno_v"
+ "nightmode_fusion_bayer_reno_v"
+ "nightmode_fusion_quadra_reno_v"
+ "noiseChromaTexture"
+ "noiseLumaTexture"
+ "nrf.flare_result"
+ "oisErr == 0 "
+ "oisShift"
+ "opacityScaling"
+ "opticalCenter"
+ "outConfig"
+ "outIsFlareDetected"
+ "outputChromaTexture"
+ "outputImage->outputRGBTexture"
+ "outputLumaTexture"
+ "outputRGBTexture"
+ "output_noise"
+ "output_rgb"
+ "particleDistance"
+ "position"
+ "postNetworkStage"
+ "postProcInputYuvImage->chromaTex"
+ "postProcInputYuvImage->lumaTex"
+ "preNetworkStage"
+ "pyramidLevel"
+ "pyramidPosition"
+ "pyramidRadius"
+ "radiusScaling"
+ "rawFrame"
+ "relativeToLens"
+ "resultTex"
+ "ret"
+ "rlutTex"
+ "scoresTex"
+ "sfdDemosaicOutputRGBTex"
+ "shouldCorrect"
+ "simd_all( expectedLevelDimensions == simd_make_int2( (int)currentPyrTex.width, (int)currentPyrTex.height ) )"
+ "simd_all( simd_int( extractionResult->position ) == extractionInput.pyramidPosition )"
+ "stage.postInferenceStage"
+ "stage.preInferenceStage"
+ "success"
+ "targetSushiTexture"
+ "temporalFilteringResults"
+ "temporalLCBs"
+ "temporalLCBsData"
+ "temporalLCBsOnLevel"
+ "udNetPlist"
+ "udnet-bayer-v"
+ "udnet-quadra-v"
+ "udnet_allow_quadra_network"
+ "updatedEntries"
+ "\xf0\xf0\xf0q"
+ "\xf0\xf0\xf0\xc1"
+ "\xf0\xf0\xf0\xf0!"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0A"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf1"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf1"
- "( processingType == NRF_ProcessingType_RawNightMode )"
- "-[RawNightModeDenoiseInferenceCMITIPSharedParameters updateParametersFromMetadata:cameraInfoByPortType:tuningParameters:lscGainMapParameters:firstPix:aeTargetGain:isQuadra:textureDimensions:]"
- "\xf0\xf0\xf0a"
- "\xf0\xf0\xf0\x81"
- "\xf0\xf0\xf0\xe1"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xe1"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xd1"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf1"
```
