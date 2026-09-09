## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/CMImaging`

```diff

 764.22.13.0.0
-  __TEXT.__text: 0x1ac778
-  __TEXT.__objc_methlist: 0xd3ac
-  __TEXT.__cstring: 0x18f29
-  __TEXT.__const: 0x2f00
-  __TEXT.__gcc_except_tab: 0x1210
-  __TEXT.__oslogstring: 0x4780
-  __TEXT.__unwind_info: 0x3058
+  __TEXT.__text: 0x1f422c
+  __TEXT.__objc_methlist: 0x112a4
+  __TEXT.__cstring: 0x2330a
+  __TEXT.__const: 0x7140
+  __TEXT.__gcc_except_tab: 0x14a8
+  __TEXT.__oslogstring: 0x4caa
+  __TEXT.__dlopen_cstrs: 0x50
+  __TEXT.__unwind_info: 0x3aa0
   __TEXT.__eh_frame: 0x6e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x9c0
-  __DATA_CONST.__objc_classlist: 0x5f8
+  __DATA_CONST.__const: 0x1b40
+  __DATA_CONST.__objc_classlist: 0x768
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x1b0
+  __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6248
+  __DATA_CONST.__objc_selrefs: 0x7858
   __DATA_CONST.__objc_protorefs: 0x30
-  __DATA_CONST.__objc_superrefs: 0x4c8
-  __DATA_CONST.__objc_arraydata: 0x410
-  __DATA_CONST.__got: 0xc50
-  __AUTH_CONST.__const: 0x810
-  __AUTH_CONST.__cfstring: 0x6760
-  __AUTH_CONST.__objc_const: 0x1f178
-  __AUTH_CONST.__objc_intobj: 0xba0
-  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __DATA_CONST.__objc_superrefs: 0x5d0
+  __DATA_CONST.__objc_arraydata: 0x6a8
+  __DATA_CONST.__got: 0xe78
+  __AUTH_CONST.__const: 0xc30
+  __AUTH_CONST.__cfstring: 0x8da0
+  __AUTH_CONST.__objc_const: 0x27a78
+  __AUTH_CONST.__objc_intobj: 0xfc0
+  __AUTH_CONST.__objc_arrayobj: 0x138
+  __AUTH_CONST.__objc_floatobj: 0xe0
   __AUTH_CONST.__objc_dictobj: 0xa0
-  __AUTH_CONST.__objc_doubleobj: 0x1130
-  __AUTH_CONST.__auth_got: 0xbe0
+  __AUTH_CONST.__objc_doubleobj: 0x1300
+  __AUTH_CONST.__auth_got: 0xc40
+  __AUTH.__objc_data: 0xcd0
   __AUTH.__data: 0x8
-  __DATA.__objc_ivar: 0x17e0
-  __DATA.__data: 0x12d90
-  __DATA.__common: 0x100
-  __DATA_DIRTY.__objc_data: 0x3bb0
-  __DATA_DIRTY.__common: 0x100
-  __DATA_DIRTY.__bss: 0x1d8
+  __DATA.__objc_ivar: 0x2030
+  __DATA.__data: 0x12f98
+  __DATA.__common: 0x1e0
+  __DATA_DIRTY.__objc_data: 0x3d40
+  __DATA_DIRTY.__common: 0x120
+  __DATA_DIRTY.__bss: 0x1e8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7306
-  Symbols:   10341
-  CStrings:  3300
+  Functions: 9565
+  Symbols:   13418
+  CStrings:  4339
 
Symbols:
+ +[CMILCBDatabase initialize]
+ +[CMILCBDatabase supportsSecureCoding]
+ +[CMILCBEntry generateKeyForPosition:radius:pyramidLevel:lastDetectionGravityVector:lastDetectionTimeStamp:]
+ +[CMILCBEntry generateNewKeyFromConflictingKey:]
+ +[CMILCBEntry initialize]
+ +[CMILCBEntry supportsSecureCoding]
+ +[CMISmartStyleUtilitiesV1 defaultStyleForCastType:smartStyleRenderingVersion:]
+ +[CMISmartStyleUtilitiesV1 defaultStyleForCastType:textureStyleVersion:]
+ +[CMITextureStyle initStandardTextureStyle]
+ +[CMITextureStyle initWithPresetName:intensity:grain:]
+ +[CMITextureStyleTuningLookup _cacheKeyForHardwareModel:portType:captureMode:preset:captureType:]
+ +[CMITextureStyleTuningLookup _interpolateFrom:to:t:]
+ +[CMITextureStyleTuningLookup _loadTuningPlistIfNeeded]
+ +[CMITextureStyleTuningLookup _loadTuningPlist]
+ +[CMITextureStyleTuningLookup _mergeTuningDictionary:forCaptureType:]
+ +[CMITextureStyleTuningLookup _normalizedCaptureTypeForPresetDict:requestedCaptureType:]
+ +[CMITextureStyleTuningLookup blendedTuningFrom:to:intensity:blendThreshold:effectiveIntensityOut:]
+ +[CMITextureStyleTuningLookup defaultTextureStyleForPresetName:]
+ +[CMITextureStyleTuningLookup defaultTextureStyleForSmartStyleCastType:]
+ +[CMITextureStyleTuningLookup initialize]
+ +[CMITextureStyleTuningLookup reloadTuningPlist]
+ +[CMITextureStyleTuningLookup tuningDictionary:withFilmGrainFromTuning:]
+ +[CMITextureStyleTuningLookup tuningDictionaryForHardwareModel:portType:captureMode:preset:captureType:]
+ +[CMITextureStyleTuningLookup tuningDictionaryForMetadata:]
+ +[CMITextureStylesBloom initialize]
+ +[CMITextureStylesDiffusion initialize]
+ +[CMITextureStylesFaceLandmark landmarkFromDictionary:]
+ +[CMITextureStylesFastGaussian calculateGaussianDimsWithWidth:height:radius:nSamples:targetBlurRadius:pWorkWidth:pWorkHeight:pFinalSigma:pKernelRadius:]
+ +[CMITextureStylesFastGaussian calculateGaussianDimsWithWidth:height:sigma:nSamples:targetBlurRadius:pWorkWidth:pWorkHeight:pFinalSigma:pKernelRadius:fastMode:]
+ +[CMITextureStylesFilmGrainProcessorV1 initialize]
+ +[CMITextureStylesFilter calculateIdealRadius:andDownSamplingScale:forImageSize:andTargetFullScaleRadius:]
+ +[CMITextureStylesFilter calculateRadiusForSigma:]
+ +[CMITextureStylesGaussianGuidedFilterV3 calculateGuidedFilterDimsWithFullImageWidth:fullImageHeight:sigma:blurRadius:pMediumResWidth:pMediumResHeight:pLowResWidth:pLowResHeight:pMediumToLow:pMediumSampling:pOutputBlurRadius:]
+ +[CMITextureStylesGlow initialize]
+ +[CMITextureStylesGuidedFilter supportedRadii]
+ +[CMITextureStylesHalation initialize]
+ +[CMITextureStylesMattify dictOfZeroInitializedStats]
+ +[CMITextureStylesMattify initialize]
+ +[CMITextureStylesPersonInputData initialize]
+ +[CMITextureStylesPersonInputData metadataFormatVersion]
+ +[CMITextureStylesPersonInputData personDataFromDictionary:]
+ +[CMITextureStylesPersonInputData personDataFromDictionary:forKeys:]
+ +[CMITextureStylesPersonInputDataUtilities convertUnitOfAngleInPersonInputDataArrayToDegrees:]
+ +[CMITextureStylesPersonInputDataUtilities convertUnitOfAngleInPersonInputDataArrayToRadians:]
+ +[CMITextureStylesPersonInputDataUtilities dictionaryRepresentationsFromFigLivePhotoMetadata:]
+ +[CMITextureStylesPersonInputDataUtilities faceDiagonalRatioForFaceSize:imageSize:]
+ +[CMITextureStylesPersonInputDataUtilities initialize]
+ +[CMITextureStylesPersonInputDataUtilities normalizePersonInputDataArray:toCropRect:]
+ +[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromDetectedFaces:]
+ +[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromDictionaryRepresentations:keys:]
+ +[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]
+ +[CMITextureStylesPersonInputDataUtilities softFadeGatingForFaceSize:imageSize:lowerBound:upperBound:]
+ +[CMITextureStylesPersonInputDataUtilities sortPersonInputDataArrayByFaceSize:maxCount:]
+ +[CMITextureStylesProcessor APIVersion]
+ +[CMITextureStylesProcessor computeAuxTextureRegionInCropSpaceWithAuxTextureSize:auxCropRect:fullImageSize:]
+ +[CMITextureStylesProcessor computeAuxTextureRegionInCropSpaceWithAuxTextureSize:fullImageSize:]
+ +[CMITextureStylesProcessor computeAuxTextureRegionInCropSpaceWithPixelBuffer:auxCropRect:fullImageSize:]
+ +[CMITextureStylesProcessor computeAuxTextureRegionInCropSpaceWithPixelBuffer:fullImageSize:]
+ +[CMITextureStylesProcessor computeAuxTextureRegionInCropSpaceWithTexture:auxCropRect:fullImageSize:]
+ +[CMITextureStylesProcessor computeAuxTextureRegionInCropSpaceWithTexture:fullImageSize:]
+ +[CMITextureStylesProcessor effectTypeToEffectName:]
+ +[CMITextureStylesProcessor effectTypeToZeroInitializedStats:]
+ +[CMITextureStylesProcessor getRequiredMemorySize]
+ +[CMITextureStylesProcessor initialize]
+ +[CMITextureStylesProcessor presetNameToPresetValue:]
+ +[CMITextureStylesProcessor presetValueToPresetName:]
+ +[CMITextureStylesSkinSmoothStandalone dictOfZeroInitializedStats]
+ +[CMITextureStylesSkinSmoothStandalone initialize]
+ +[CMITextureStylesUnderEyeBrighten dictOfZeroInitializedStats]
+ +[CMITextureStylesUnderEyeBrighten initialize]
+ -[CMILCBDatabase .cxx_destruct]
+ -[CMILCBDatabase addEntries:]
+ -[CMILCBDatabase copyWithZone:]
+ -[CMILCBDatabase count]
+ -[CMILCBDatabase deleteEntries:]
+ -[CMILCBDatabase detectionIteration]
+ -[CMILCBDatabase encodeWithCoder:]
+ -[CMILCBDatabase entriesByKey]
+ -[CMILCBDatabase entries]
+ -[CMILCBDatabase exportLCBsForCaptureStream]
+ -[CMILCBDatabase initForSensorID:moduleSerial:]
+ -[CMILCBDatabase initWithCoder:]
+ -[CMILCBDatabase moduleSerial]
+ -[CMILCBDatabase sensorID]
+ -[CMILCBDatabase updateEntries:]
+ -[CMILCBEntry .cxx_destruct]
+ -[CMILCBEntry apertureRatio]
+ -[CMILCBEntry computeMinMaxCorrectionFeatureValues]
+ -[CMILCBEntry correctionFeatures]
+ -[CMILCBEntry defocusRadius]
+ -[CMILCBEntry detectionCount]
+ -[CMILCBEntry dictionaryRepresentation]
+ -[CMILCBEntry encodeWithCoder:]
+ -[CMILCBEntry focusLensPosition]
+ -[CMILCBEntry initWithCoder:]
+ -[CMILCBEntry initWithEntry:]
+ -[CMILCBEntry initWithKey:position:radius:defocusRadius:particleDistance:apertureRatio:focusLensPosition:oisShift:opticalCenter:detectionCount:relativeToLens:lastDetectionGravityVector:lastDetectionTimeStamp:shouldCorrect:correctionFeatures:]
+ -[CMILCBEntry key]
+ -[CMILCBEntry lastDetectionGravityVector]
+ -[CMILCBEntry lastDetectionTimeStamp]
+ -[CMILCBEntry maxCorrectionFeatureValue]
+ -[CMILCBEntry minCorrectionFeatureValue]
+ -[CMILCBEntry oisShift]
+ -[CMILCBEntry opticalCenter]
+ -[CMILCBEntry particleDistance]
+ -[CMILCBEntry position]
+ -[CMILCBEntry radius]
+ -[CMILCBEntry relativeToLens]
+ -[CMILCBEntry shouldCorrect]
+ -[CMILCBEntry withDifferentKey]
+ -[CMISmartStyleUtilitiesV1 enableDeltaMapDetailEnhancement]
+ -[CMISmartStyleUtilitiesV1 inputSkinMaskPixelBuffer]
+ -[CMISmartStyleUtilitiesV1 setEnableDeltaMapDetailEnhancement:]
+ -[CMISmartStyleUtilitiesV1 setInputSkinMaskPixelBuffer:]
+ -[CMIStyleEngineApplyStyle inputFaceNormalizedRects]
+ -[CMIStyleEngineApplyStyle inputSkinMaskFlipHorizontal]
+ -[CMIStyleEngineApplyStyle inputSkinMaskFlipVertical]
+ -[CMIStyleEngineApplyStyle inputSkinMaskICR]
+ -[CMIStyleEngineApplyStyle inputSkinMaskPCR]
+ -[CMIStyleEngineApplyStyle inputSkinMaskRotationDegrees]
+ -[CMIStyleEngineApplyStyle inputSkinMaskTexture]
+ -[CMIStyleEngineApplyStyle inputSkinSmoothingParameters]
+ -[CMIStyleEngineApplyStyle resetSkinSmoothState]
+ -[CMIStyleEngineApplyStyle setInputFaceNormalizedRects:]
+ -[CMIStyleEngineApplyStyle setInputSkinMaskFlipHorizontal:]
+ -[CMIStyleEngineApplyStyle setInputSkinMaskFlipVertical:]
+ -[CMIStyleEngineApplyStyle setInputSkinMaskICR:]
+ -[CMIStyleEngineApplyStyle setInputSkinMaskPCR:]
+ -[CMIStyleEngineApplyStyle setInputSkinMaskRotationDegrees:]
+ -[CMIStyleEngineApplyStyle setInputSkinMaskTexture:]
+ -[CMIStyleEngineApplyStyle setInputSkinSmoothingParameters:]
+ -[CMIStyleEngineApplyStyle setSkinMaskPurpose:]
+ -[CMIStyleEngineApplyStyle skinMaskPurpose]
+ -[CMIStyleEngineProcessor inputFaceNormalizedRects]
+ -[CMIStyleEngineProcessor inputSkinMaskFlipHorizontal]
+ -[CMIStyleEngineProcessor inputSkinMaskFlipVertical]
+ -[CMIStyleEngineProcessor inputSkinMaskICR]
+ -[CMIStyleEngineProcessor inputSkinMaskPCR]
+ -[CMIStyleEngineProcessor inputSkinMaskRotationDegrees]
+ -[CMIStyleEngineProcessor inputSkinSmoothingParameters]
+ -[CMIStyleEngineProcessor setInputFaceNormalizedRects:]
+ -[CMIStyleEngineProcessor setInputSkinMaskFlipHorizontal:]
+ -[CMIStyleEngineProcessor setInputSkinMaskFlipVertical:]
+ -[CMIStyleEngineProcessor setInputSkinMaskICR:]
+ -[CMIStyleEngineProcessor setInputSkinMaskPCR:]
+ -[CMIStyleEngineProcessor setInputSkinMaskRotationDegrees:]
+ -[CMIStyleEngineProcessor setInputSkinSmoothingParameters:]
+ -[CMIStyleEngineProcessor setSkinMaskPurpose:]
+ -[CMIStyleEngineProcessor skinMaskPurpose]
+ -[CMITSMattifyPerPersonIntermediatesAndStats .cxx_destruct]
+ -[CMITSTextureAndFullImageRegion .cxx_destruct]
+ -[CMITSTextureAndFullImageRegion dealloc]
+ -[CMITSTextureAndFullImageRegion fullImageRegion]
+ -[CMITSTextureAndFullImageRegion setFullImageRegion:]
+ -[CMITSTextureAndFullImageRegion setTexture:]
+ -[CMITSTextureAndFullImageRegion texture]
+ -[CMITSUEBPerPersonData .cxx_destruct]
+ -[CMITextureStyle .cxx_destruct]
+ -[CMITextureStyle debugDescription]
+ -[CMITextureStyle description]
+ -[CMITextureStyle grain]
+ -[CMITextureStyle hash]
+ -[CMITextureStyle intensity]
+ -[CMITextureStyle isEqual:]
+ -[CMITextureStyle preset]
+ -[CMITextureStylesBloom .cxx_destruct]
+ -[CMITextureStylesBloom _compileShaders]
+ -[CMITextureStylesBloom _configureColorConversion:forTexture:isOutput:]
+ -[CMITextureStylesBloom _updateColorManagementForInputOutput:]
+ -[CMITextureStylesBloom _validateInputsAndParameters]
+ -[CMITextureStylesBloom allocator]
+ -[CMITextureStylesBloom calculateStats]
+ -[CMITextureStylesBloom cameraInfoByPortType]
+ -[CMITextureStylesBloom computeMinimumInputRegionInFullImageCoords:]
+ -[CMITextureStylesBloom finishProcessing]
+ -[CMITextureStylesBloom fullImageSize]
+ -[CMITextureStylesBloom initWithOptionalMetalContext:]
+ -[CMITextureStylesBloom inputOutput]
+ -[CMITextureStylesBloom instanceID]
+ -[CMITextureStylesBloom metalCommandQueue]
+ -[CMITextureStylesBloom parameters]
+ -[CMITextureStylesBloom personData]
+ -[CMITextureStylesBloom prepareToProcess:]
+ -[CMITextureStylesBloom prewarm]
+ -[CMITextureStylesBloom process]
+ -[CMITextureStylesBloom purgeResources]
+ -[CMITextureStylesBloom regionToRender]
+ -[CMITextureStylesBloom resetState]
+ -[CMITextureStylesBloom scaleParametersWithIntensity:]
+ -[CMITextureStylesBloom setAllocator:]
+ -[CMITextureStylesBloom setCameraInfoByPortType:]
+ -[CMITextureStylesBloom setFullImageSize:]
+ -[CMITextureStylesBloom setInputOutput:]
+ -[CMITextureStylesBloom setInstanceID:]
+ -[CMITextureStylesBloom setMetalCommandQueue:]
+ -[CMITextureStylesBloom setParameters:]
+ -[CMITextureStylesBloom setPersonData:]
+ -[CMITextureStylesBloom setRegionToRender:]
+ -[CMITextureStylesBloom setTuningParameters:]
+ -[CMITextureStylesBloom setup]
+ -[CMITextureStylesBloom supportsExternalMemoryResource]
+ -[CMITextureStylesBloom supportsInPlaceRendering]
+ -[CMITextureStylesBloom tuningParameters]
+ -[CMITextureStylesBloomIO .cxx_destruct]
+ -[CMITextureStylesBloomIO inputImage]
+ -[CMITextureStylesBloomIO inputSkinMask]
+ -[CMITextureStylesBloomIO outputImage]
+ -[CMITextureStylesBloomIO setInputImage:]
+ -[CMITextureStylesBloomIO setInputSkinMask:]
+ -[CMITextureStylesBloomIO setOutputImage:]
+ -[CMITextureStylesBloomParameters _floatFromDict:key:default:]
+ -[CMITextureStylesBloomParameters brightness]
+ -[CMITextureStylesBloomParameters copyWithZone:]
+ -[CMITextureStylesBloomParameters initWithTuningDictionary:]
+ -[CMITextureStylesBloomParameters init]
+ -[CMITextureStylesBloomParameters inputTextureROI]
+ -[CMITextureStylesBloomParameters lightMapGamma]
+ -[CMITextureStylesBloomParameters lightMapInvert]
+ -[CMITextureStylesBloomParameters setBrightness:]
+ -[CMITextureStylesBloomParameters setDefaults]
+ -[CMITextureStylesBloomParameters setInputTextureROI:]
+ -[CMITextureStylesBloomParameters setLightMapGamma:]
+ -[CMITextureStylesBloomParameters setLightMapInvert:]
+ -[CMITextureStylesBloomParameters setSigmaGlare:]
+ -[CMITextureStylesBloomParameters setSkinMask:]
+ -[CMITextureStylesBloomParameters setStrength:]
+ -[CMITextureStylesBloomParameters sigmaGlare]
+ -[CMITextureStylesBloomParameters skinMask]
+ -[CMITextureStylesBloomParameters strength]
+ -[CMITextureStylesBloomParameters validate]
+ -[CMITextureStylesDiffusion .cxx_destruct]
+ -[CMITextureStylesDiffusion _applyMeteorToInput:gainMap:gain:mixFactor:outputMixed:commandBuffer:]
+ -[CMITextureStylesDiffusion _calculateBlurSigma:]
+ -[CMITextureStylesDiffusion _calculateFullScaleBlurRadius:]
+ -[CMITextureStylesDiffusion _compileShaders]
+ -[CMITextureStylesDiffusion _configureColorConversion:forTexture:isOutput:]
+ -[CMITextureStylesDiffusion _createIntermediateTextures:inputRegion:blurredSize:]
+ -[CMITextureStylesDiffusion _releaseIntermediateTextures]
+ -[CMITextureStylesDiffusion _renderDiffusionWithInput:blurred:skinMask:personMask:output:diffusionParameters:commandBuffer:]
+ -[CMITextureStylesDiffusion _rescale:toLinearRGB:commandBuffer:]
+ -[CMITextureStylesDiffusion _updateColorManagementForInputTexture:outputTexture:]
+ -[CMITextureStylesDiffusion _validateInputsAndParameters]
+ -[CMITextureStylesDiffusion allocator]
+ -[CMITextureStylesDiffusion calculateStats]
+ -[CMITextureStylesDiffusion cameraInfoByPortType]
+ -[CMITextureStylesDiffusion computeMinimumInputRegionInFullImageCoords:]
+ -[CMITextureStylesDiffusion finishProcessing]
+ -[CMITextureStylesDiffusion fullImageSize]
+ -[CMITextureStylesDiffusion initWithOptionalMetalContext:]
+ -[CMITextureStylesDiffusion inputOutput]
+ -[CMITextureStylesDiffusion instanceID]
+ -[CMITextureStylesDiffusion metalCommandQueue]
+ -[CMITextureStylesDiffusion parameters]
+ -[CMITextureStylesDiffusion personData]
+ -[CMITextureStylesDiffusion prepareToProcess:]
+ -[CMITextureStylesDiffusion prewarm]
+ -[CMITextureStylesDiffusion process]
+ -[CMITextureStylesDiffusion purgeResources]
+ -[CMITextureStylesDiffusion regionToRender]
+ -[CMITextureStylesDiffusion resetState]
+ -[CMITextureStylesDiffusion scaleParametersWithIntensity:]
+ -[CMITextureStylesDiffusion setAllocator:]
+ -[CMITextureStylesDiffusion setCameraInfoByPortType:]
+ -[CMITextureStylesDiffusion setFullImageSize:]
+ -[CMITextureStylesDiffusion setInputOutput:]
+ -[CMITextureStylesDiffusion setInstanceID:]
+ -[CMITextureStylesDiffusion setMetalCommandQueue:]
+ -[CMITextureStylesDiffusion setParameters:]
+ -[CMITextureStylesDiffusion setPersonData:]
+ -[CMITextureStylesDiffusion setRegionToRender:]
+ -[CMITextureStylesDiffusion setTuningParameters:]
+ -[CMITextureStylesDiffusion setup]
+ -[CMITextureStylesDiffusion supportsExternalMemoryResource]
+ -[CMITextureStylesDiffusion supportsInPlaceRendering]
+ -[CMITextureStylesDiffusion tuningParameters]
+ -[CMITextureStylesDiffusionIO .cxx_destruct]
+ -[CMITextureStylesDiffusionIO inputGainMap]
+ -[CMITextureStylesDiffusionIO inputImage]
+ -[CMITextureStylesDiffusionIO inputPersonMask]
+ -[CMITextureStylesDiffusionIO inputSkinMask]
+ -[CMITextureStylesDiffusionIO outputImage]
+ -[CMITextureStylesDiffusionIO setInputGainMap:]
+ -[CMITextureStylesDiffusionIO setInputImage:]
+ -[CMITextureStylesDiffusionIO setInputPersonMask:]
+ -[CMITextureStylesDiffusionIO setInputSkinMask:]
+ -[CMITextureStylesDiffusionIO setOutputImage:]
+ -[CMITextureStylesDiffusionParameters _floatFromDict:key:default:]
+ -[CMITextureStylesDiffusionParameters bg]
+ -[CMITextureStylesDiffusionParameters bw3Gamma]
+ -[CMITextureStylesDiffusionParameters copyWithZone:]
+ -[CMITextureStylesDiffusionParameters difSat]
+ -[CMITextureStylesDiffusionParameters diffuseColor]
+ -[CMITextureStylesDiffusionParameters faceTempering]
+ -[CMITextureStylesDiffusionParameters fogStrength]
+ -[CMITextureStylesDiffusionParameters gaussianBlurSigma]
+ -[CMITextureStylesDiffusionParameters grading]
+ -[CMITextureStylesDiffusionParameters highlight]
+ -[CMITextureStylesDiffusionParameters hueRotate]
+ -[CMITextureStylesDiffusionParameters initWithTuningDictionary:]
+ -[CMITextureStylesDiffusionParameters init]
+ -[CMITextureStylesDiffusionParameters lift]
+ -[CMITextureStylesDiffusionParameters maxRGB]
+ -[CMITextureStylesDiffusionParameters meteorHeadroomMixFactor]
+ -[CMITextureStylesDiffusionParameters meteorHeadroom]
+ -[CMITextureStylesDiffusionParameters naturalResolution]
+ -[CMITextureStylesDiffusionParameters person]
+ -[CMITextureStylesDiffusionParameters saturation]
+ -[CMITextureStylesDiffusionParameters setBg:]
+ -[CMITextureStylesDiffusionParameters setBw3Gamma:]
+ -[CMITextureStylesDiffusionParameters setDefaults]
+ -[CMITextureStylesDiffusionParameters setDifSat:]
+ -[CMITextureStylesDiffusionParameters setDiffuseColor:]
+ -[CMITextureStylesDiffusionParameters setFaceTempering:]
+ -[CMITextureStylesDiffusionParameters setFogStrength:]
+ -[CMITextureStylesDiffusionParameters setGaussianBlurSigma:]
+ -[CMITextureStylesDiffusionParameters setGrading:]
+ -[CMITextureStylesDiffusionParameters setHighlight:]
+ -[CMITextureStylesDiffusionParameters setHueRotate:]
+ -[CMITextureStylesDiffusionParameters setLift:]
+ -[CMITextureStylesDiffusionParameters setMaxRGB:]
+ -[CMITextureStylesDiffusionParameters setMeteorHeadroom:]
+ -[CMITextureStylesDiffusionParameters setMeteorHeadroomMixFactor:]
+ -[CMITextureStylesDiffusionParameters setNaturalResolution:]
+ -[CMITextureStylesDiffusionParameters setPerson:]
+ -[CMITextureStylesDiffusionParameters setSaturation:]
+ -[CMITextureStylesDiffusionParameters setShDarken:]
+ -[CMITextureStylesDiffusionParameters setSlBG:]
+ -[CMITextureStylesDiffusionParameters setSlBright:]
+ -[CMITextureStylesDiffusionParameters setSlDark:]
+ -[CMITextureStylesDiffusionParameters setSlPerson:]
+ -[CMITextureStylesDiffusionParameters setSlSkin:]
+ -[CMITextureStylesDiffusionParameters setSoftLight:]
+ -[CMITextureStylesDiffusionParameters setSpbHL:]
+ -[CMITextureStylesDiffusionParameters setStrength:]
+ -[CMITextureStylesDiffusionParameters shDarken]
+ -[CMITextureStylesDiffusionParameters slBG]
+ -[CMITextureStylesDiffusionParameters slBright]
+ -[CMITextureStylesDiffusionParameters slDark]
+ -[CMITextureStylesDiffusionParameters slPerson]
+ -[CMITextureStylesDiffusionParameters slSkin]
+ -[CMITextureStylesDiffusionParameters softLight]
+ -[CMITextureStylesDiffusionParameters spbHL]
+ -[CMITextureStylesDiffusionParameters strength]
+ -[CMITextureStylesDiffusionParameters validate]
+ -[CMITextureStylesDownSampler .cxx_destruct]
+ -[CMITextureStylesDownSampler _compileShaders]
+ -[CMITextureStylesDownSampler downSampleInput:output:commandBuffer:]
+ -[CMITextureStylesDownSampler downSampleInput:output:encoder:]
+ -[CMITextureStylesDownSampler initWithMetalContext:]
+ -[CMITextureStylesDownSampler rescaleInput:output:commandBuffer:]
+ -[CMITextureStylesDownSampler rescaleInput:output:encoder:]
+ -[CMITextureStylesEffectDescriptor .cxx_destruct]
+ -[CMITextureStylesEffectDescriptor copyWithZone:]
+ -[CMITextureStylesEffectDescriptor description]
+ -[CMITextureStylesEffectDescriptor hash]
+ -[CMITextureStylesEffectDescriptor initWithtype:parameters:]
+ -[CMITextureStylesEffectDescriptor isEqual:]
+ -[CMITextureStylesEffectDescriptor parameters]
+ -[CMITextureStylesEffectDescriptor setSkipRendering:]
+ -[CMITextureStylesEffectDescriptor skipRendering]
+ -[CMITextureStylesEffectDescriptor type]
+ -[CMITextureStylesFaceLandmark copyWithZone:]
+ -[CMITextureStylesFaceLandmark dictionaryRepresentation]
+ -[CMITextureStylesFaceLandmark error]
+ -[CMITextureStylesFaceLandmark initWithPoint:error:]
+ -[CMITextureStylesFaceLandmark point]
+ -[CMITextureStylesFastGaussian .cxx_destruct]
+ -[CMITextureStylesFastGaussian _compileShaders]
+ -[CMITextureStylesFastGaussian _createTexture:]
+ -[CMITextureStylesFastGaussian _dispatch:pipelineState:width:height:]
+ -[CMITextureStylesFastGaussian initWithMetalContext:]
+ -[CMITextureStylesFastGaussian makeTexture:h:fmt:label:]
+ -[CMITextureStylesFastGaussian processTexture:outputTexture:radius:commandBuffer:]
+ -[CMITextureStylesFastGaussian processTexture:outputTexture:sigma:commandBuffer:fastMode:]
+ -[CMITextureStylesFastGaussian runOn:sigma:nSamples:targetBlurRadius:outTexture:commandBuffer:fastMode:]
+ -[CMITextureStylesFilmGrainIO .cxx_destruct]
+ -[CMITextureStylesFilmGrainIO brightnessValue]
+ -[CMITextureStylesFilmGrainIO inputImage]
+ -[CMITextureStylesFilmGrainIO inputPersonImage]
+ -[CMITextureStylesFilmGrainIO inputSkinImage]
+ -[CMITextureStylesFilmGrainIO inputSkyImage]
+ -[CMITextureStylesFilmGrainIO outputImage]
+ -[CMITextureStylesFilmGrainIO setBrightnessValue:]
+ -[CMITextureStylesFilmGrainIO setInputImage:]
+ -[CMITextureStylesFilmGrainIO setInputPersonImage:]
+ -[CMITextureStylesFilmGrainIO setInputSkinImage:]
+ -[CMITextureStylesFilmGrainIO setInputSkyImage:]
+ -[CMITextureStylesFilmGrainIO setOutputImage:]
+ -[CMITextureStylesFilmGrainParameters _floatFromDict:key:default:]
+ -[CMITextureStylesFilmGrainParameters _gainBasedFloatFromDict:key:totalGain:default:]
+ -[CMITextureStylesFilmGrainParameters _unsignedIntegerFromDict:key:default:]
+ -[CMITextureStylesFilmGrainParameters amplitudeDecay]
+ -[CMITextureStylesFilmGrainParameters amplitude]
+ -[CMITextureStylesFilmGrainParameters backgroundStrength]
+ -[CMITextureStylesFilmGrainParameters bvHigh]
+ -[CMITextureStylesFilmGrainParameters bvLowScale]
+ -[CMITextureStylesFilmGrainParameters bvLow]
+ -[CMITextureStylesFilmGrainParameters contrastBoost]
+ -[CMITextureStylesFilmGrainParameters copyWithZone:]
+ -[CMITextureStylesFilmGrainParameters darkScale]
+ -[CMITextureStylesFilmGrainParameters description]
+ -[CMITextureStylesFilmGrainParameters frequencyGap]
+ -[CMITextureStylesFilmGrainParameters grainBlurRadius]
+ -[CMITextureStylesFilmGrainParameters grainSelectivity]
+ -[CMITextureStylesFilmGrainParameters hueMix]
+ -[CMITextureStylesFilmGrainParameters imageGuidedFilterEpsilon]
+ -[CMITextureStylesFilmGrainParameters imageGuidedFilterRadius]
+ -[CMITextureStylesFilmGrainParameters initWithTuningDictionary:]
+ -[CMITextureStylesFilmGrainParameters initWithTuningDictionary:totalGain:]
+ -[CMITextureStylesFilmGrainParameters init]
+ -[CMITextureStylesFilmGrainParameters naturalResolution]
+ -[CMITextureStylesFilmGrainParameters octaves]
+ -[CMITextureStylesFilmGrainParameters personStrength]
+ -[CMITextureStylesFilmGrainParameters saturation]
+ -[CMITextureStylesFilmGrainParameters seed]
+ -[CMITextureStylesFilmGrainParameters setAmplitude:]
+ -[CMITextureStylesFilmGrainParameters setAmplitudeDecay:]
+ -[CMITextureStylesFilmGrainParameters setBackgroundStrength:]
+ -[CMITextureStylesFilmGrainParameters setBvHigh:]
+ -[CMITextureStylesFilmGrainParameters setBvLow:]
+ -[CMITextureStylesFilmGrainParameters setBvLowScale:]
+ -[CMITextureStylesFilmGrainParameters setContrastBoost:]
+ -[CMITextureStylesFilmGrainParameters setDarkScale:]
+ -[CMITextureStylesFilmGrainParameters setDefaults]
+ -[CMITextureStylesFilmGrainParameters setFrequencyGap:]
+ -[CMITextureStylesFilmGrainParameters setGrainBlurRadius:]
+ -[CMITextureStylesFilmGrainParameters setGrainSelectivity:]
+ -[CMITextureStylesFilmGrainParameters setHueMix:]
+ -[CMITextureStylesFilmGrainParameters setImageGuidedFilterEpsilon:]
+ -[CMITextureStylesFilmGrainParameters setImageGuidedFilterRadius:]
+ -[CMITextureStylesFilmGrainParameters setNaturalResolution:]
+ -[CMITextureStylesFilmGrainParameters setOctaves:]
+ -[CMITextureStylesFilmGrainParameters setPersonStrength:]
+ -[CMITextureStylesFilmGrainParameters setSaturation:]
+ -[CMITextureStylesFilmGrainParameters setSeed:]
+ -[CMITextureStylesFilmGrainParameters setShadowLift:]
+ -[CMITextureStylesFilmGrainParameters setSkinStrength:]
+ -[CMITextureStylesFilmGrainParameters setSkyStrength:]
+ -[CMITextureStylesFilmGrainParameters setStrength:]
+ -[CMITextureStylesFilmGrainParameters setTileSize:]
+ -[CMITextureStylesFilmGrainParameters setZoom:]
+ -[CMITextureStylesFilmGrainParameters shadowLift]
+ -[CMITextureStylesFilmGrainParameters skinStrength]
+ -[CMITextureStylesFilmGrainParameters skyStrength]
+ -[CMITextureStylesFilmGrainParameters strength]
+ -[CMITextureStylesFilmGrainParameters tileSize]
+ -[CMITextureStylesFilmGrainParameters validate]
+ -[CMITextureStylesFilmGrainParameters zoom]
+ -[CMITextureStylesFilmGrainProcessorV1 .cxx_destruct]
+ -[CMITextureStylesFilmGrainProcessorV1 _compileShaders]
+ -[CMITextureStylesFilmGrainProcessorV1 _configureColorConversion:forTexture:isOutput:]
+ -[CMITextureStylesFilmGrainProcessorV1 _encodeGrainBlendWithInputImageUsingParams:commandBuffer:inputOutput:]
+ -[CMITextureStylesFilmGrainProcessorV1 _shaderForFilterRadius:]
+ -[CMITextureStylesFilmGrainProcessorV1 _updateColorManagementForInputTexture:outputImageTexture:]
+ -[CMITextureStylesFilmGrainProcessorV1 allocator]
+ -[CMITextureStylesFilmGrainProcessorV1 calculateStats]
+ -[CMITextureStylesFilmGrainProcessorV1 cameraInfoByPortType]
+ -[CMITextureStylesFilmGrainProcessorV1 computeMinimumInputRegionInFullImageCoords:]
+ -[CMITextureStylesFilmGrainProcessorV1 dealloc]
+ -[CMITextureStylesFilmGrainProcessorV1 finishProcessing]
+ -[CMITextureStylesFilmGrainProcessorV1 fullImageSize]
+ -[CMITextureStylesFilmGrainProcessorV1 initWithOptionalMetalContext:]
+ -[CMITextureStylesFilmGrainProcessorV1 inputOutput]
+ -[CMITextureStylesFilmGrainProcessorV1 instanceID]
+ -[CMITextureStylesFilmGrainProcessorV1 metalCommandQueue]
+ -[CMITextureStylesFilmGrainProcessorV1 metalShaderParamsFromDynamicParameters:brightnessValue:]
+ -[CMITextureStylesFilmGrainProcessorV1 parameters]
+ -[CMITextureStylesFilmGrainProcessorV1 personData]
+ -[CMITextureStylesFilmGrainProcessorV1 prepareToProcess:]
+ -[CMITextureStylesFilmGrainProcessorV1 prewarm]
+ -[CMITextureStylesFilmGrainProcessorV1 process]
+ -[CMITextureStylesFilmGrainProcessorV1 purgeResources]
+ -[CMITextureStylesFilmGrainProcessorV1 regionToRender]
+ -[CMITextureStylesFilmGrainProcessorV1 resetState]
+ -[CMITextureStylesFilmGrainProcessorV1 scaleParametersWithIntensity:]
+ -[CMITextureStylesFilmGrainProcessorV1 setAllocator:]
+ -[CMITextureStylesFilmGrainProcessorV1 setCameraInfoByPortType:]
+ -[CMITextureStylesFilmGrainProcessorV1 setFullImageSize:]
+ -[CMITextureStylesFilmGrainProcessorV1 setInputOutput:]
+ -[CMITextureStylesFilmGrainProcessorV1 setInstanceID:]
+ -[CMITextureStylesFilmGrainProcessorV1 setMetalCommandQueue:]
+ -[CMITextureStylesFilmGrainProcessorV1 setParameters:]
+ -[CMITextureStylesFilmGrainProcessorV1 setPersonData:]
+ -[CMITextureStylesFilmGrainProcessorV1 setRegionToRender:]
+ -[CMITextureStylesFilmGrainProcessorV1 setTuningParameters:]
+ -[CMITextureStylesFilmGrainProcessorV1 setup]
+ -[CMITextureStylesFilmGrainProcessorV1 supportsExternalMemoryResource]
+ -[CMITextureStylesFilmGrainProcessorV1 supportsInPlaceRendering]
+ -[CMITextureStylesFilmGrainProcessorV1 tuningParameters]
+ -[CMITextureStylesFilter .cxx_destruct]
+ -[CMITextureStylesFilter _compileShaders]
+ -[CMITextureStylesFilter _guidedFilterInput:guide:outputA:outputB:radius:sigma:epsilon:type:commandBuffer:]
+ -[CMITextureStylesFilter _guidedFilterInput:guide:outputA:outputB:radius:sigma:epsilon:type:encoder:]
+ -[CMITextureStylesFilter _shaderForFilterType:radius:]
+ -[CMITextureStylesFilter calculateIdealRadius:andDownSamplingScale:forImageSize:andTargetFullScaleRadius:]
+ -[CMITextureStylesFilter calculateRadiusForSigma:]
+ -[CMITextureStylesFilter gaussianFilterInput:output:radius:sigma:commandBuffer:]
+ -[CMITextureStylesFilter gaussianFilterInput:output:radius:sigma:encoder:]
+ -[CMITextureStylesFilter guidedFilterInput:guide:outputA:outputB:radius:sigma:epsilon:commandBuffer:]
+ -[CMITextureStylesFilter guidedFilterInput:guide:outputA:outputB:radius:sigma:epsilon:encoder:]
+ -[CMITextureStylesFilter initWithMetalContext:]
+ -[CMITextureStylesFilter weightedGuidedFilterInput:guide:outputA:outputB:radius:sigma:epsilon:commandBuffer:]
+ -[CMITextureStylesFilter weightedGuidedFilterInput:guide:outputA:outputB:radius:sigma:epsilon:encoder:]
+ -[CMITextureStylesGaussianFilter .cxx_destruct]
+ -[CMITextureStylesGaussianFilter _compileShaders]
+ -[CMITextureStylesGaussianFilter encodeGaussianBlur2DWithCommandBuffer:input:output:radius:]
+ -[CMITextureStylesGaussianFilter encodeGaussianBlurWithCommandBuffer:input:output:kernel:kernelSize:]
+ -[CMITextureStylesGaussianFilter encodeGaussianBlurWithCommandBuffer:input:output:radius:]
+ -[CMITextureStylesGaussianFilter encodeSIMDGaussianBlurWithCommandBuffer:input:output:radius:]
+ -[CMITextureStylesGaussianFilter encodeSIMDMaskedDownsampledGaussianBlurWithCommandBuffer:input:output:skinMask:radius:]
+ -[CMITextureStylesGaussianFilter initWithMetalContext:]
+ -[CMITextureStylesGaussianGuidedFilterV3 .cxx_destruct]
+ -[CMITextureStylesGaussianGuidedFilterV3 _compileShaders]
+ -[CMITextureStylesGaussianGuidedFilterV3 _createTexture:]
+ -[CMITextureStylesGaussianGuidedFilterV3 _dispatch:pipelineState:width:height:]
+ -[CMITextureStylesGaussianGuidedFilterV3 initWithMetalContext:]
+ -[CMITextureStylesGaussianGuidedFilterV3 make:h:fmt:label:]
+ -[CMITextureStylesGaussianGuidedFilterV3 runWithInput:skinMask:instanceMask:highlightRetention:sigma:eps:blurRadius:fullImageSize:fullImageOffset:outputTexture:commandBuffer:]
+ -[CMITextureStylesGlow .cxx_destruct]
+ -[CMITextureStylesGlow _compileShaders]
+ -[CMITextureStylesGlow _configureColorConversion:forTexture:isOutput:]
+ -[CMITextureStylesGlow _createGlobalToneCurveTextureFromGTCData:encoder:toneCurveTextureOut:]
+ -[CMITextureStylesGlow _releaseIntermediateTextures]
+ -[CMITextureStylesGlow _updateColorManagementForInputOutput:]
+ -[CMITextureStylesGlow _validateInputsAndParameters]
+ -[CMITextureStylesGlow allocator]
+ -[CMITextureStylesGlow calculateStats]
+ -[CMITextureStylesGlow cameraInfoByPortType]
+ -[CMITextureStylesGlow computeMinimumInputRegionInFullImageCoords:]
+ -[CMITextureStylesGlow dealloc]
+ -[CMITextureStylesGlow finishProcessing]
+ -[CMITextureStylesGlow fullImageSize]
+ -[CMITextureStylesGlow initWithOptionalMetalContext:]
+ -[CMITextureStylesGlow inputOutput]
+ -[CMITextureStylesGlow instanceID]
+ -[CMITextureStylesGlow metalCommandQueue]
+ -[CMITextureStylesGlow parameters]
+ -[CMITextureStylesGlow personData]
+ -[CMITextureStylesGlow prepareToProcess:]
+ -[CMITextureStylesGlow prewarm]
+ -[CMITextureStylesGlow process]
+ -[CMITextureStylesGlow purgeResources]
+ -[CMITextureStylesGlow regionToRender]
+ -[CMITextureStylesGlow resetState]
+ -[CMITextureStylesGlow scaleParametersWithIntensity:]
+ -[CMITextureStylesGlow setAllocator:]
+ -[CMITextureStylesGlow setCameraInfoByPortType:]
+ -[CMITextureStylesGlow setFullImageSize:]
+ -[CMITextureStylesGlow setInputOutput:]
+ -[CMITextureStylesGlow setInstanceID:]
+ -[CMITextureStylesGlow setMetalCommandQueue:]
+ -[CMITextureStylesGlow setParameters:]
+ -[CMITextureStylesGlow setPersonData:]
+ -[CMITextureStylesGlow setRegionToRender:]
+ -[CMITextureStylesGlow setStreamingMode:]
+ -[CMITextureStylesGlow setTuningParameters:]
+ -[CMITextureStylesGlow setup]
+ -[CMITextureStylesGlow streamingMode]
+ -[CMITextureStylesGlow supportsExternalMemoryResource]
+ -[CMITextureStylesGlow supportsInPlaceRendering]
+ -[CMITextureStylesGlow tuningParameters]
+ -[CMITextureStylesGlowIO .cxx_destruct]
+ -[CMITextureStylesGlowIO inputImage]
+ -[CMITextureStylesGlowIO inputLinearImage]
+ -[CMITextureStylesGlowIO inputLinearMetadata]
+ -[CMITextureStylesGlowIO inputMask]
+ -[CMITextureStylesGlowIO outputImage]
+ -[CMITextureStylesGlowIO setInputImage:]
+ -[CMITextureStylesGlowIO setInputLinearImage:]
+ -[CMITextureStylesGlowIO setInputLinearMetadata:]
+ -[CMITextureStylesGlowIO setInputMask:]
+ -[CMITextureStylesGlowIO setOutputImage:]
+ -[CMITextureStylesGlowParameters .cxx_destruct]
+ -[CMITextureStylesGlowParameters _boolFromDict:key:default:]
+ -[CMITextureStylesGlowParameters _floatFromDict:key:default:]
+ -[CMITextureStylesGlowParameters baselineExposure]
+ -[CMITextureStylesGlowParameters brightnessMask]
+ -[CMITextureStylesGlowParameters brightness]
+ -[CMITextureStylesGlowParameters contrastMask]
+ -[CMITextureStylesGlowParameters contrast]
+ -[CMITextureStylesGlowParameters copyWithZone:]
+ -[CMITextureStylesGlowParameters gammaMask]
+ -[CMITextureStylesGlowParameters gamma]
+ -[CMITextureStylesGlowParameters initWithTuningDictionary:]
+ -[CMITextureStylesGlowParameters init]
+ -[CMITextureStylesGlowParameters inputTextureROI]
+ -[CMITextureStylesGlowParameters lightMapGamma]
+ -[CMITextureStylesGlowParameters lightMapMax]
+ -[CMITextureStylesGlowParameters linearImageHighKey]
+ -[CMITextureStylesGlowParameters linearMixForBG]
+ -[CMITextureStylesGlowParameters linearMixForSkin]
+ -[CMITextureStylesGlowParameters preserveColorfulnessMask]
+ -[CMITextureStylesGlowParameters preserveColorfulness]
+ -[CMITextureStylesGlowParameters saturationFromSmartStyle]
+ -[CMITextureStylesGlowParameters saturationMask]
+ -[CMITextureStylesGlowParameters saturation]
+ -[CMITextureStylesGlowParameters setBaselineExposure:]
+ -[CMITextureStylesGlowParameters setBrightness:]
+ -[CMITextureStylesGlowParameters setBrightnessMask:]
+ -[CMITextureStylesGlowParameters setContrast:]
+ -[CMITextureStylesGlowParameters setContrastMask:]
+ -[CMITextureStylesGlowParameters setDefaults]
+ -[CMITextureStylesGlowParameters setGamma:]
+ -[CMITextureStylesGlowParameters setGammaMask:]
+ -[CMITextureStylesGlowParameters setInputTextureROI:]
+ -[CMITextureStylesGlowParameters setLightMapGamma:]
+ -[CMITextureStylesGlowParameters setLightMapMax:]
+ -[CMITextureStylesGlowParameters setLinearImageHighKey:]
+ -[CMITextureStylesGlowParameters setLinearMixForBG:]
+ -[CMITextureStylesGlowParameters setLinearMixForSkin:]
+ -[CMITextureStylesGlowParameters setPreserveColorfulness:]
+ -[CMITextureStylesGlowParameters setPreserveColorfulnessMask:]
+ -[CMITextureStylesGlowParameters setSaturation:]
+ -[CMITextureStylesGlowParameters setSaturationFromSmartStyle:]
+ -[CMITextureStylesGlowParameters setSaturationMask:]
+ -[CMITextureStylesGlowParameters setStatistics:]
+ -[CMITextureStylesGlowParameters setStrength:]
+ -[CMITextureStylesGlowParameters setStrengthMask:]
+ -[CMITextureStylesGlowParameters setUseStatistics:]
+ -[CMITextureStylesGlowParameters statistics]
+ -[CMITextureStylesGlowParameters strengthMask]
+ -[CMITextureStylesGlowParameters strength]
+ -[CMITextureStylesGlowParameters useStatistics]
+ -[CMITextureStylesGlowParameters validate]
+ -[CMITextureStylesGuidedFilter .cxx_destruct]
+ -[CMITextureStylesGuidedFilter _abShaderForRadius:]
+ -[CMITextureStylesGuidedFilter _compileShaders]
+ -[CMITextureStylesGuidedFilter encodeRunWithCommandBuffer:guide:input:output:radius:epsilon:]
+ -[CMITextureStylesGuidedFilter initWithMetalContext:]
+ -[CMITextureStylesHalation .cxx_destruct]
+ -[CMITextureStylesHalation _calculateBlurSigma:]
+ -[CMITextureStylesHalation _calculateFullScaleBlurRadius:]
+ -[CMITextureStylesHalation _compileShaders]
+ -[CMITextureStylesHalation _computeAsymLumMaskWithInput:personMask:outputMask:halationParameters:brightnessValue:commandBuffer:]
+ -[CMITextureStylesHalation _configureColorConversion:forTexture:isOutput:]
+ -[CMITextureStylesHalation _createIntermediateTexturesWithInputRegion:firstBlurSize:secondBlurSize:]
+ -[CMITextureStylesHalation _halationFinalRendererWithInput:halationMask:skinMask:personMask:output:parameters:commandBuffer:]
+ -[CMITextureStylesHalation _releaseIntermediateTextures]
+ -[CMITextureStylesHalation _substractFg:bg:output:commandBuffer:]
+ -[CMITextureStylesHalation _updateColorManagementForInputTexture:outputTexture:]
+ -[CMITextureStylesHalation _validateInputsAndParameters]
+ -[CMITextureStylesHalation allocator]
+ -[CMITextureStylesHalation calculateStats]
+ -[CMITextureStylesHalation cameraInfoByPortType]
+ -[CMITextureStylesHalation computeMinimumInputRegionInFullImageCoords:]
+ -[CMITextureStylesHalation finishProcessing]
+ -[CMITextureStylesHalation fullImageSize]
+ -[CMITextureStylesHalation initWithOptionalMetalContext:]
+ -[CMITextureStylesHalation inputOutput]
+ -[CMITextureStylesHalation instanceID]
+ -[CMITextureStylesHalation metalCommandQueue]
+ -[CMITextureStylesHalation parameters]
+ -[CMITextureStylesHalation personData]
+ -[CMITextureStylesHalation prepareToProcess:]
+ -[CMITextureStylesHalation prewarm]
+ -[CMITextureStylesHalation process]
+ -[CMITextureStylesHalation purgeResources]
+ -[CMITextureStylesHalation regionToRender]
+ -[CMITextureStylesHalation resetState]
+ -[CMITextureStylesHalation scaleParametersWithIntensity:]
+ -[CMITextureStylesHalation setAllocator:]
+ -[CMITextureStylesHalation setCameraInfoByPortType:]
+ -[CMITextureStylesHalation setFullImageSize:]
+ -[CMITextureStylesHalation setInputOutput:]
+ -[CMITextureStylesHalation setInstanceID:]
+ -[CMITextureStylesHalation setMetalCommandQueue:]
+ -[CMITextureStylesHalation setParameters:]
+ -[CMITextureStylesHalation setPersonData:]
+ -[CMITextureStylesHalation setRegionToRender:]
+ -[CMITextureStylesHalation setTuningParameters:]
+ -[CMITextureStylesHalation setup]
+ -[CMITextureStylesHalation supportsExternalMemoryResource]
+ -[CMITextureStylesHalation supportsInPlaceRendering]
+ -[CMITextureStylesHalation tuningParameters]
+ -[CMITextureStylesHalationIO .cxx_destruct]
+ -[CMITextureStylesHalationIO brightnessValue]
+ -[CMITextureStylesHalationIO inputGainMap]
+ -[CMITextureStylesHalationIO inputHDRImage]
+ -[CMITextureStylesHalationIO inputImage]
+ -[CMITextureStylesHalationIO inputLightMap]
+ -[CMITextureStylesHalationIO inputPersonMask]
+ -[CMITextureStylesHalationIO inputSkinMask]
+ -[CMITextureStylesHalationIO outputImage]
+ -[CMITextureStylesHalationIO setBrightnessValue:]
+ -[CMITextureStylesHalationIO setInputGainMap:]
+ -[CMITextureStylesHalationIO setInputHDRImage:]
+ -[CMITextureStylesHalationIO setInputImage:]
+ -[CMITextureStylesHalationIO setInputLightMap:]
+ -[CMITextureStylesHalationIO setInputPersonMask:]
+ -[CMITextureStylesHalationIO setInputSkinMask:]
+ -[CMITextureStylesHalationIO setOutputImage:]
+ -[CMITextureStylesHalationParameters _floatFromDict:key:default:]
+ -[CMITextureStylesHalationParameters bg]
+ -[CMITextureStylesHalationParameters bvHigh]
+ -[CMITextureStylesHalationParameters bvLow]
+ -[CMITextureStylesHalationParameters bvThresholdDeltaLowScale]
+ -[CMITextureStylesHalationParameters copyWithZone:]
+ -[CMITextureStylesHalationParameters faceTempering]
+ -[CMITextureStylesHalationParameters halationChroma]
+ -[CMITextureStylesHalationParameters halationHue]
+ -[CMITextureStylesHalationParameters initWithTuningDictionary:]
+ -[CMITextureStylesHalationParameters init]
+ -[CMITextureStylesHalationParameters inputInnerKnot0]
+ -[CMITextureStylesHalationParameters inputInnerKnot1]
+ -[CMITextureStylesHalationParameters inputLowerBound]
+ -[CMITextureStylesHalationParameters inputLowerCoeffA]
+ -[CMITextureStylesHalationParameters inputLowerCoeffB]
+ -[CMITextureStylesHalationParameters inputOuterKnot0]
+ -[CMITextureStylesHalationParameters inputOuterKnot1]
+ -[CMITextureStylesHalationParameters inputSpread]
+ -[CMITextureStylesHalationParameters inputTextureROI]
+ -[CMITextureStylesHalationParameters inputThresholdDelta]
+ -[CMITextureStylesHalationParameters inputUpperCoeffA]
+ -[CMITextureStylesHalationParameters inputUpperCoeffB]
+ -[CMITextureStylesHalationParameters maskBlurSigma]
+ -[CMITextureStylesHalationParameters maxRGB]
+ -[CMITextureStylesHalationParameters meteorHeadroomMixFactor]
+ -[CMITextureStylesHalationParameters meteorHeadroom]
+ -[CMITextureStylesHalationParameters naturalResolution]
+ -[CMITextureStylesHalationParameters person]
+ -[CMITextureStylesHalationParameters setBg:]
+ -[CMITextureStylesHalationParameters setBvHigh:]
+ -[CMITextureStylesHalationParameters setBvLow:]
+ -[CMITextureStylesHalationParameters setBvThresholdDeltaLowScale:]
+ -[CMITextureStylesHalationParameters setDefaults]
+ -[CMITextureStylesHalationParameters setFaceTempering:]
+ -[CMITextureStylesHalationParameters setHalationChroma:]
+ -[CMITextureStylesHalationParameters setHalationHue:]
+ -[CMITextureStylesHalationParameters setInputInnerKnot0:]
+ -[CMITextureStylesHalationParameters setInputInnerKnot1:]
+ -[CMITextureStylesHalationParameters setInputLowerBound:]
+ -[CMITextureStylesHalationParameters setInputLowerCoeffA:]
+ -[CMITextureStylesHalationParameters setInputLowerCoeffB:]
+ -[CMITextureStylesHalationParameters setInputOuterKnot0:]
+ -[CMITextureStylesHalationParameters setInputOuterKnot1:]
+ -[CMITextureStylesHalationParameters setInputSpread:]
+ -[CMITextureStylesHalationParameters setInputTextureROI:]
+ -[CMITextureStylesHalationParameters setInputThresholdDelta:]
+ -[CMITextureStylesHalationParameters setInputUpperCoeffA:]
+ -[CMITextureStylesHalationParameters setInputUpperCoeffB:]
+ -[CMITextureStylesHalationParameters setMaskBlurSigma:]
+ -[CMITextureStylesHalationParameters setMaxRGB:]
+ -[CMITextureStylesHalationParameters setMeteorHeadroom:]
+ -[CMITextureStylesHalationParameters setMeteorHeadroomMixFactor:]
+ -[CMITextureStylesHalationParameters setNaturalResolution:]
+ -[CMITextureStylesHalationParameters setPerson:]
+ -[CMITextureStylesHalationParameters setStrength:]
+ -[CMITextureStylesHalationParameters strength]
+ -[CMITextureStylesHalationParameters validate]
+ -[CMITextureStylesMattify .cxx_destruct]
+ -[CMITextureStylesMattify _calculateExtendedFaceROI:leftCheekROI:rightCheekROI:triangleVerticesLeft:triangleVerticesRight:]
+ -[CMITextureStylesMattify _calculateMasks:warpedMaskAggregate:extendedFaceROI:leftCheekROI:rightCheekROI:triangleVerticesLeft:triangleVerticesRight:]
+ -[CMITextureStylesMattify _calculateStats:validMask:warpedMaskAggregate:statsBuffer:]
+ -[CMITextureStylesMattify _compileShaders]
+ -[CMITextureStylesMattify _freePersonIntermediatesAndStats:]
+ -[CMITextureStylesMattify _processApply]
+ -[CMITextureStylesMattify allocator]
+ -[CMITextureStylesMattify calculateStats]
+ -[CMITextureStylesMattify cameraInfoByPortType]
+ -[CMITextureStylesMattify computeMinimumInputRegionInFullImageCoords:]
+ -[CMITextureStylesMattify dealloc]
+ -[CMITextureStylesMattify encodeDownsampledGaussianBlurWithCommandBuffer:inputImage:outputDownsampledAndBlurredImage:outputImage:downsampleFactor:downsampleSigma:stopAfterDownsample:cropAndDownsampleSkipLevelCount:cropAndDownsampleBoxFilter:]
+ -[CMITextureStylesMattify finishProcessing]
+ -[CMITextureStylesMattify fullImageSize]
+ -[CMITextureStylesMattify initWithOptionalMetalContext:]
+ -[CMITextureStylesMattify inputOutput]
+ -[CMITextureStylesMattify instanceID]
+ -[CMITextureStylesMattify metalCommandQueue]
+ -[CMITextureStylesMattify parameters]
+ -[CMITextureStylesMattify personData]
+ -[CMITextureStylesMattify prepareToProcess:]
+ -[CMITextureStylesMattify prewarm]
+ -[CMITextureStylesMattify process]
+ -[CMITextureStylesMattify purgeResources]
+ -[CMITextureStylesMattify regionToRender]
+ -[CMITextureStylesMattify resetState]
+ -[CMITextureStylesMattify scaleParametersWithIntensity:]
+ -[CMITextureStylesMattify setAllocator:]
+ -[CMITextureStylesMattify setCameraInfoByPortType:]
+ -[CMITextureStylesMattify setFullImageSize:]
+ -[CMITextureStylesMattify setInputOutput:]
+ -[CMITextureStylesMattify setInstanceID:]
+ -[CMITextureStylesMattify setMetalCommandQueue:]
+ -[CMITextureStylesMattify setParameters:]
+ -[CMITextureStylesMattify setPersonData:]
+ -[CMITextureStylesMattify setRegionToRender:]
+ -[CMITextureStylesMattify setSkipRendering:]
+ -[CMITextureStylesMattify setStreamingMode:]
+ -[CMITextureStylesMattify setTuningParameters:]
+ -[CMITextureStylesMattify setup]
+ -[CMITextureStylesMattify skipRendering]
+ -[CMITextureStylesMattify streamingMode]
+ -[CMITextureStylesMattify supportsExternalMemoryResource]
+ -[CMITextureStylesMattify supportsInPlaceRendering]
+ -[CMITextureStylesMattify tuningParameters]
+ -[CMITextureStylesMattifyIO .cxx_destruct]
+ -[CMITextureStylesMattifyIO inputEarMask]
+ -[CMITextureStylesMattifyIO inputFaceMask]
+ -[CMITextureStylesMattifyIO inputGlassesMask]
+ -[CMITextureStylesMattifyIO inputImage]
+ -[CMITextureStylesMattifyIO inputInstanceMask]
+ -[CMITextureStylesMattifyIO inputLipsMask]
+ -[CMITextureStylesMattifyIO inputNoseMask]
+ -[CMITextureStylesMattifyIO inputSkinMask]
+ -[CMITextureStylesMattifyIO inputTattoosMask]
+ -[CMITextureStylesMattifyIO outputImage]
+ -[CMITextureStylesMattifyIO outputPersonStats]
+ -[CMITextureStylesMattifyIO setInputEarMask:]
+ -[CMITextureStylesMattifyIO setInputFaceMask:]
+ -[CMITextureStylesMattifyIO setInputGlassesMask:]
+ -[CMITextureStylesMattifyIO setInputImage:]
+ -[CMITextureStylesMattifyIO setInputInstanceMask:]
+ -[CMITextureStylesMattifyIO setInputLipsMask:]
+ -[CMITextureStylesMattifyIO setInputNoseMask:]
+ -[CMITextureStylesMattifyIO setInputSkinMask:]
+ -[CMITextureStylesMattifyIO setInputTattoosMask:]
+ -[CMITextureStylesMattifyIO setOutputImage:]
+ -[CMITextureStylesMattifyIO setOutputPersonStats:]
+ -[CMITextureStylesMattifyParameters blendColorImageAverageColorMixFactor]
+ -[CMITextureStylesMattifyParameters copyWithZone:]
+ -[CMITextureStylesMattifyParameters darknessDiffSmoothstepLowerBound]
+ -[CMITextureStylesMattifyParameters darknessDiffSmoothstepUpperBound]
+ -[CMITextureStylesMattifyParameters editingStrength]
+ -[CMITextureStylesMattifyParameters fracMaskHighlightsHeadroom]
+ -[CMITextureStylesMattifyParameters fracMaskHighlightsNormFactor]
+ -[CMITextureStylesMattifyParameters hueDiffMeanTermSmoothstepLowerBound]
+ -[CMITextureStylesMattifyParameters hueDiffMeanTermSmoothstepUpperBound]
+ -[CMITextureStylesMattifyParameters hueDiffSmoothstepLowerBound]
+ -[CMITextureStylesMattifyParameters hueDiffSmoothstepUpperBound]
+ -[CMITextureStylesMattifyParameters imageTextureFactor]
+ -[CMITextureStylesMattifyParameters imageTextureThreshold]
+ -[CMITextureStylesMattifyParameters initWithTuningDictionary:]
+ -[CMITextureStylesMattifyParameters init]
+ -[CMITextureStylesMattifyParameters largeBlurRadiusFaceDiagonalFactor]
+ -[CMITextureStylesMattifyParameters lightnessEditFactor]
+ -[CMITextureStylesMattifyParameters lightnessEditHeadroom]
+ -[CMITextureStylesMattifyParameters setBlendColorImageAverageColorMixFactor:]
+ -[CMITextureStylesMattifyParameters setDarknessDiffSmoothstepLowerBound:]
+ -[CMITextureStylesMattifyParameters setDarknessDiffSmoothstepUpperBound:]
+ -[CMITextureStylesMattifyParameters setDefaults]
+ -[CMITextureStylesMattifyParameters setEditingStrength:]
+ -[CMITextureStylesMattifyParameters setFracMaskHighlightsHeadroom:]
+ -[CMITextureStylesMattifyParameters setFracMaskHighlightsNormFactor:]
+ -[CMITextureStylesMattifyParameters setHueDiffMeanTermSmoothstepLowerBound:]
+ -[CMITextureStylesMattifyParameters setHueDiffMeanTermSmoothstepUpperBound:]
+ -[CMITextureStylesMattifyParameters setHueDiffSmoothstepLowerBound:]
+ -[CMITextureStylesMattifyParameters setHueDiffSmoothstepUpperBound:]
+ -[CMITextureStylesMattifyParameters setImageTextureFactor:]
+ -[CMITextureStylesMattifyParameters setImageTextureThreshold:]
+ -[CMITextureStylesMattifyParameters setLargeBlurRadiusFaceDiagonalFactor:]
+ -[CMITextureStylesMattifyParameters setLightnessEditFactor:]
+ -[CMITextureStylesMattifyParameters setLightnessEditHeadroom:]
+ -[CMITextureStylesMattifyParameters setSmallBlurRadiusFaceDiagonalFactor:]
+ -[CMITextureStylesMattifyParameters setTextureRestoreScalingFactor:]
+ -[CMITextureStylesMattifyParameters setTextureRestoreSmoothstepLowerBound:]
+ -[CMITextureStylesMattifyParameters setTextureRestoreSmoothstepUpperBound:]
+ -[CMITextureStylesMattifyParameters setTextureRestoreStrengthFactor:]
+ -[CMITextureStylesMattifyParameters smallBlurRadiusFaceDiagonalFactor]
+ -[CMITextureStylesMattifyParameters textureRestoreScalingFactor]
+ -[CMITextureStylesMattifyParameters textureRestoreSmoothstepLowerBound]
+ -[CMITextureStylesMattifyParameters textureRestoreSmoothstepUpperBound]
+ -[CMITextureStylesMattifyParameters textureRestoreStrengthFactor]
+ -[CMITextureStylesMattifyParameters validate]
+ -[CMITextureStylesPersonInputData .cxx_destruct]
+ -[CMITextureStylesPersonInputData convertDegreesToRadians]
+ -[CMITextureStylesPersonInputData convertRadiansToDegrees]
+ -[CMITextureStylesPersonInputData copyWithZone:]
+ -[CMITextureStylesPersonInputData dictionaryRepresentationForKeys:]
+ -[CMITextureStylesPersonInputData dictionaryRepresentation]
+ -[CMITextureStylesPersonInputData faceID]
+ -[CMITextureStylesPersonInputData faceLandmarkType]
+ -[CMITextureStylesPersonInputData faceLandmarks]
+ -[CMITextureStylesPersonInputData facePitch]
+ -[CMITextureStylesPersonInputData faceROIAndLandmarksROIRelativeScalingROI]
+ -[CMITextureStylesPersonInputData faceROI]
+ -[CMITextureStylesPersonInputData faceRoll]
+ -[CMITextureStylesPersonInputData faceSkinROI]
+ -[CMITextureStylesPersonInputData faceYaw]
+ -[CMITextureStylesPersonInputData imageStats]
+ -[CMITextureStylesPersonInputData init]
+ -[CMITextureStylesPersonInputData instanceMaskReferenceKey]
+ -[CMITextureStylesPersonInputData instanceMask]
+ -[CMITextureStylesPersonInputData instanceROI]
+ -[CMITextureStylesPersonInputData normalizeRelativeToCropRect:]
+ -[CMITextureStylesPersonInputData setFaceID:]
+ -[CMITextureStylesPersonInputData setFaceLandmarkType:]
+ -[CMITextureStylesPersonInputData setFaceLandmarks:]
+ -[CMITextureStylesPersonInputData setFacePitch:]
+ -[CMITextureStylesPersonInputData setFaceROI:]
+ -[CMITextureStylesPersonInputData setFaceRoll:]
+ -[CMITextureStylesPersonInputData setFaceSkinROI:]
+ -[CMITextureStylesPersonInputData setFaceYaw:]
+ -[CMITextureStylesPersonInputData setImageStats:]
+ -[CMITextureStylesPersonInputData setInstanceMask:]
+ -[CMITextureStylesPersonInputData setInstanceMaskReferenceKey:]
+ -[CMITextureStylesPersonInputData setInstanceROI:]
+ -[CMITextureStylesPersonInputData setUnitOfAngle:]
+ -[CMITextureStylesPersonInputData unitOfAngle]
+ -[CMITextureStylesProcessor .cxx_destruct]
+ -[CMITextureStylesProcessor _allocateRenderBufferForRegion:currentInput:outputPtr:]
+ -[CMITextureStylesProcessor _bindIOBuffers:andPerPersonTextureAndFullImageRegionArray:]
+ -[CMITextureStylesProcessor _bindIOImages:]
+ -[CMITextureStylesProcessor _bindIOImages:andPerPersonTextureAndFullImageRegionArray:]
+ -[CMITextureStylesProcessor _bindImageTile:toTextureAndFullImageRegion:withUsage:label:]
+ -[CMITextureStylesProcessor _bindPerPersonImages:]
+ -[CMITextureStylesProcessor _bindPixelBufferToTexture:usage:overrideMTLPixelFormatWithFormat:planeIndex:textureCache:]
+ -[CMITextureStylesProcessor _calculateAllImageRectIntersections:ioTextureDict:perPersonTextureAndFullImageRegionArray:]
+ -[CMITextureStylesProcessor _calculateFullImageSize:ioTextureDict:]
+ -[CMITextureStylesProcessor _calculatePaddedRegionToRender:perPersonData:roiData:paddedRegionToRenderOut:]
+ -[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]
+ -[CMITextureStylesProcessor _createMemoryResource]
+ -[CMITextureStylesProcessor _denormalizePersonData:ioTextureDict:roiData:]
+ -[CMITextureStylesProcessor _getEffectRendererByType:]
+ -[CMITextureStylesProcessor _instanceLabel:]
+ -[CMITextureStylesProcessor _prepareEffectsToRender]
+ -[CMITextureStylesProcessor _preparePerPersonData]
+ -[CMITextureStylesProcessor _scaleIntensityForEffects:]
+ -[CMITextureStylesProcessor _selectOutputBufferForRegion:rendersInPlace:ioTextureDict:currentInput:intermediateTextureAndFullImageRegions:intermediateTextureAndFullImageRegionCount:currentOutputPtr:]
+ -[CMITextureStylesProcessor _setROIData:]
+ -[CMITextureStylesProcessor _setROIData:ioTextureDict:perPersonTextureAndFullImageRegionArray:]
+ -[CMITextureStylesProcessor _setROIData:perPersonTextureAndFullImageRegionArray:roiData:calculatePaddedRegionToRender:]
+ -[CMITextureStylesProcessor _validateUserSettings:]
+ -[CMITextureStylesProcessor brightnessValue]
+ -[CMITextureStylesProcessor cameraInfoByPortType]
+ -[CMITextureStylesProcessor computeMinimumInputRegionInFullImageCoords:]
+ -[CMITextureStylesProcessor dealloc]
+ -[CMITextureStylesProcessor effectsToRender]
+ -[CMITextureStylesProcessor enableSkinSmoothingMultiPersonBlending]
+ -[CMITextureStylesProcessor externalMemoryResource]
+ -[CMITextureStylesProcessor finishProcessing]
+ -[CMITextureStylesProcessor fullImageSize]
+ -[CMITextureStylesProcessor initWithOptionalMetalCommandQueue:]
+ -[CMITextureStylesProcessor init]
+ -[CMITextureStylesProcessor inputImage]
+ -[CMITextureStylesProcessor inputLinearImageMetadata]
+ -[CMITextureStylesProcessor inputLinearImage]
+ -[CMITextureStylesProcessor inputMasks]
+ -[CMITextureStylesProcessor inputMeteorGainMap]
+ -[CMITextureStylesProcessor inputPersonData]
+ -[CMITextureStylesProcessor inputPingPongImageForRendering]
+ -[CMITextureStylesProcessor inputSkinSmoothingFaceDetections]
+ -[CMITextureStylesProcessor label]
+ -[CMITextureStylesProcessor memoryResource]
+ -[CMITextureStylesProcessor metalCommandQueue]
+ -[CMITextureStylesProcessor needsIntermediateRenderingBuffer]
+ -[CMITextureStylesProcessor outputImage]
+ -[CMITextureStylesProcessor outputPersonImageStats]
+ -[CMITextureStylesProcessor outputSkinSmoothingLargeBlurGuidedFilterA]
+ -[CMITextureStylesProcessor outputSkinSmoothingLargeBlurGuidedFilterB]
+ -[CMITextureStylesProcessor outputSkinSmoothingProcessedMask]
+ -[CMITextureStylesProcessor outputSkinSmoothingSmallBlur]
+ -[CMITextureStylesProcessor outputSkinSmoothingStats]
+ -[CMITextureStylesProcessor outputSkinSmoothingTextureAddback]
+ -[CMITextureStylesProcessor prepareToProcess:]
+ -[CMITextureStylesProcessor prewarm]
+ -[CMITextureStylesProcessor process]
+ -[CMITextureStylesProcessor purgeResources]
+ -[CMITextureStylesProcessor regionToRender]
+ -[CMITextureStylesProcessor resetState]
+ -[CMITextureStylesProcessor setBrightnessValue:]
+ -[CMITextureStylesProcessor setCameraInfoByPortType:]
+ -[CMITextureStylesProcessor setEffectsToRender:]
+ -[CMITextureStylesProcessor setEnableSkinSmoothingMultiPersonBlending:]
+ -[CMITextureStylesProcessor setExternalMemoryResource:]
+ -[CMITextureStylesProcessor setFullImageSize:]
+ -[CMITextureStylesProcessor setInputImage:]
+ -[CMITextureStylesProcessor setInputLinearImage:]
+ -[CMITextureStylesProcessor setInputLinearImageMetadata:]
+ -[CMITextureStylesProcessor setInputMasks:]
+ -[CMITextureStylesProcessor setInputMeteorGainMap:]
+ -[CMITextureStylesProcessor setInputPersonData:]
+ -[CMITextureStylesProcessor setInputPingPongImageForRendering:]
+ -[CMITextureStylesProcessor setInputSkinSmoothingFaceDetections:]
+ -[CMITextureStylesProcessor setLabel:]
+ -[CMITextureStylesProcessor setMemoryResource:]
+ -[CMITextureStylesProcessor setMetalCommandQueue:]
+ -[CMITextureStylesProcessor setOutputImage:]
+ -[CMITextureStylesProcessor setOutputPersonImageStats:]
+ -[CMITextureStylesProcessor setOutputSkinSmoothingLargeBlurGuidedFilterA:]
+ -[CMITextureStylesProcessor setOutputSkinSmoothingLargeBlurGuidedFilterB:]
+ -[CMITextureStylesProcessor setOutputSkinSmoothingProcessedMask:]
+ -[CMITextureStylesProcessor setOutputSkinSmoothingSmallBlur:]
+ -[CMITextureStylesProcessor setOutputSkinSmoothingStats:]
+ -[CMITextureStylesProcessor setOutputSkinSmoothingTextureAddback:]
+ -[CMITextureStylesProcessor setRegionToRender:]
+ -[CMITextureStylesProcessor setShouldFlushCVMTLCachesOnResetState:]
+ -[CMITextureStylesProcessor setStreamingMode:]
+ -[CMITextureStylesProcessor setTextureStyleIntensity:]
+ -[CMITextureStylesProcessor setTuningParameters:]
+ -[CMITextureStylesProcessor setup]
+ -[CMITextureStylesProcessor shouldFlushCVMTLCachesOnResetState]
+ -[CMITextureStylesProcessor streamingMode]
+ -[CMITextureStylesProcessor supportsExternalMemoryResource]
+ -[CMITextureStylesProcessor textureStyleIntensity]
+ -[CMITextureStylesProcessor tuningParameters]
+ -[CMITextureStylesProcessor waitForSchedule]
+ -[CMITextureStylesPyramid .cxx_destruct]
+ -[CMITextureStylesPyramid dealloc]
+ -[CMITextureStylesPyramid dereference]
+ -[CMITextureStylesPyramid initWithImage:maxLevels:allocator:encoder:shader:]
+ -[CMITextureStylesPyramid initWithImage:maxLevels:pixelFormat:allocator:encoder:shader:]
+ -[CMITextureStylesPyramid nLevels]
+ -[CMITextureStylesPyramid objectAtIndexedSubscript:]
+ -[CMITextureStylesPyramidFactory .cxx_destruct]
+ -[CMITextureStylesPyramidFactory _compileShaders]
+ -[CMITextureStylesPyramidFactory createPyramidWithImage:maxLevels:encoder:]
+ -[CMITextureStylesPyramidFactory createPyramidWithImage:maxLevels:pixelFormat:encoder:]
+ -[CMITextureStylesPyramidFactory initWithMetalContext:]
+ -[CMITextureStylesSkinSmoothIO .cxx_destruct]
+ -[CMITextureStylesSkinSmoothIO allPersonDataForBlending]
+ -[CMITextureStylesSkinSmoothIO bodyMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO brightnessValue]
+ -[CMITextureStylesSkinSmoothIO earsMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO externalFaceRoughnessStatsOutput]
+ -[CMITextureStylesSkinSmoothIO externalLargeBlurGuidedFilterAOutput]
+ -[CMITextureStylesSkinSmoothIO externalLargeBlurGuidedFilterBOutput]
+ -[CMITextureStylesSkinSmoothIO externalSmallBlurOutput]
+ -[CMITextureStylesSkinSmoothIO externalTextureAddbackOutput]
+ -[CMITextureStylesSkinSmoothIO eyebrowsMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO faceSkinMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO glassesMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO hairMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO handsMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO inputFaceRect]
+ -[CMITextureStylesSkinSmoothIO inputImage]
+ -[CMITextureStylesSkinSmoothIO inputSkinMaskAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO instanceMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO lipsMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO outputImage]
+ -[CMITextureStylesSkinSmoothIO outputPersonStats]
+ -[CMITextureStylesSkinSmoothIO outputProcessedSkinMask]
+ -[CMITextureStylesSkinSmoothIO personMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO setAllPersonDataForBlending:]
+ -[CMITextureStylesSkinSmoothIO setBodyMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setBrightnessValue:]
+ -[CMITextureStylesSkinSmoothIO setEarsMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setExternalFaceRoughnessStatsOutput:]
+ -[CMITextureStylesSkinSmoothIO setExternalLargeBlurGuidedFilterAOutput:]
+ -[CMITextureStylesSkinSmoothIO setExternalLargeBlurGuidedFilterBOutput:]
+ -[CMITextureStylesSkinSmoothIO setExternalSmallBlurOutput:]
+ -[CMITextureStylesSkinSmoothIO setExternalTextureAddbackOutput:]
+ -[CMITextureStylesSkinSmoothIO setEyebrowsMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setFaceSkinMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setGlassesMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setHairMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setHandsMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setInputFaceRect:]
+ -[CMITextureStylesSkinSmoothIO setInputImage:]
+ -[CMITextureStylesSkinSmoothIO setInputSkinMaskAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setInstanceMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setLipsMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setOutputImage:]
+ -[CMITextureStylesSkinSmoothIO setOutputPersonStats:]
+ -[CMITextureStylesSkinSmoothIO setOutputProcessedSkinMask:]
+ -[CMITextureStylesSkinSmoothIO setPersonMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setTattoosMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO setTeethMaskTextureAndFullImageRegion:]
+ -[CMITextureStylesSkinSmoothIO tattoosMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothIO teethMaskTextureAndFullImageRegion]
+ -[CMITextureStylesSkinSmoothParameters copyWithZone:]
+ -[CMITextureStylesSkinSmoothParameters degrungeBody]
+ -[CMITextureStylesSkinSmoothParameters degrunge]
+ -[CMITextureStylesSkinSmoothParameters detailSize]
+ -[CMITextureStylesSkinSmoothParameters enableTextureAddback]
+ -[CMITextureStylesSkinSmoothParameters eyeProtection]
+ -[CMITextureStylesSkinSmoothParameters eyebrows]
+ -[CMITextureStylesSkinSmoothParameters fastMode]
+ -[CMITextureStylesSkinSmoothParameters gFContrast]
+ -[CMITextureStylesSkinSmoothParameters gFRadius]
+ -[CMITextureStylesSkinSmoothParameters hairClothes]
+ -[CMITextureStylesSkinSmoothParameters hairTxFloor]
+ -[CMITextureStylesSkinSmoothParameters handsAndEars]
+ -[CMITextureStylesSkinSmoothParameters highlightRetention]
+ -[CMITextureStylesSkinSmoothParameters hlBlurStrength]
+ -[CMITextureStylesSkinSmoothParameters hlTextureRestore]
+ -[CMITextureStylesSkinSmoothParameters initWithTuningDictionary:]
+ -[CMITextureStylesSkinSmoothParameters initWithTuningDictionary:totalGain:]
+ -[CMITextureStylesSkinSmoothParameters init]
+ -[CMITextureStylesSkinSmoothParameters lipContrast]
+ -[CMITextureStylesSkinSmoothParameters lipCrease]
+ -[CMITextureStylesSkinSmoothParameters lipHighlights]
+ -[CMITextureStylesSkinSmoothParameters lipNegClar]
+ -[CMITextureStylesSkinSmoothParameters maxDarknessTrigger]
+ -[CMITextureStylesSkinSmoothParameters minDarknessTrigger]
+ -[CMITextureStylesSkinSmoothParameters minTexture]
+ -[CMITextureStylesSkinSmoothParameters nightModeSharpness]
+ -[CMITextureStylesSkinSmoothParameters nightMode]
+ -[CMITextureStylesSkinSmoothParameters plusGreenGuide]
+ -[CMITextureStylesSkinSmoothParameters poresBody]
+ -[CMITextureStylesSkinSmoothParameters pores]
+ -[CMITextureStylesSkinSmoothParameters roughSamples]
+ -[CMITextureStylesSkinSmoothParameters setDefaults]
+ -[CMITextureStylesSkinSmoothParameters setDegrunge:]
+ -[CMITextureStylesSkinSmoothParameters setDegrungeBody:]
+ -[CMITextureStylesSkinSmoothParameters setDetailSize:]
+ -[CMITextureStylesSkinSmoothParameters setEnableTextureAddback:]
+ -[CMITextureStylesSkinSmoothParameters setEyeProtection:]
+ -[CMITextureStylesSkinSmoothParameters setEyebrows:]
+ -[CMITextureStylesSkinSmoothParameters setFastMode:]
+ -[CMITextureStylesSkinSmoothParameters setGFContrast:]
+ -[CMITextureStylesSkinSmoothParameters setGFRadius:]
+ -[CMITextureStylesSkinSmoothParameters setHairClothes:]
+ -[CMITextureStylesSkinSmoothParameters setHairTxFloor:]
+ -[CMITextureStylesSkinSmoothParameters setHandsAndEars:]
+ -[CMITextureStylesSkinSmoothParameters setHighlightRetention:]
+ -[CMITextureStylesSkinSmoothParameters setHlBlurStrength:]
+ -[CMITextureStylesSkinSmoothParameters setHlTextureRestore:]
+ -[CMITextureStylesSkinSmoothParameters setLipContrast:]
+ -[CMITextureStylesSkinSmoothParameters setLipCrease:]
+ -[CMITextureStylesSkinSmoothParameters setLipHighlights:]
+ -[CMITextureStylesSkinSmoothParameters setLipNegClar:]
+ -[CMITextureStylesSkinSmoothParameters setMaxDarknessTrigger:]
+ -[CMITextureStylesSkinSmoothParameters setMinDarknessTrigger:]
+ -[CMITextureStylesSkinSmoothParameters setMinTexture:]
+ -[CMITextureStylesSkinSmoothParameters setNightMode:]
+ -[CMITextureStylesSkinSmoothParameters setNightModeSharpness:]
+ -[CMITextureStylesSkinSmoothParameters setPlusGreenGuide:]
+ -[CMITextureStylesSkinSmoothParameters setPores:]
+ -[CMITextureStylesSkinSmoothParameters setPoresBody:]
+ -[CMITextureStylesSkinSmoothParameters setRoughSamples:]
+ -[CMITextureStylesSkinSmoothParameters setStrongTextureProtect:]
+ -[CMITextureStylesSkinSmoothParameters setTattooSmoothing:]
+ -[CMITextureStylesSkinSmoothParameters setTattooWeight:]
+ -[CMITextureStylesSkinSmoothParameters setTeeth:]
+ -[CMITextureStylesSkinSmoothParameters setTextureClamp:]
+ -[CMITextureStylesSkinSmoothParameters setTextureDetectScale:]
+ -[CMITextureStylesSkinSmoothParameters setTextureRestore:]
+ -[CMITextureStylesSkinSmoothParameters setVarTexture:]
+ -[CMITextureStylesSkinSmoothParameters strongTextureProtect]
+ -[CMITextureStylesSkinSmoothParameters tattooSmoothing]
+ -[CMITextureStylesSkinSmoothParameters tattooWeight]
+ -[CMITextureStylesSkinSmoothParameters teeth]
+ -[CMITextureStylesSkinSmoothParameters textureClamp]
+ -[CMITextureStylesSkinSmoothParameters textureDetectScale]
+ -[CMITextureStylesSkinSmoothParameters textureRestore]
+ -[CMITextureStylesSkinSmoothParameters validate]
+ -[CMITextureStylesSkinSmoothParameters varTexture]
+ -[CMITextureStylesSkinSmoothStandalone .cxx_destruct]
+ -[CMITextureStylesSkinSmoothStandalone _allocateStatsBuffers]
+ -[CMITextureStylesSkinSmoothStandalone _calculateBlurEstimate]
+ -[CMITextureStylesSkinSmoothStandalone _calculateFaceRoughnessFromImage:smallBlurTextureAndFullImageRegion:faceSkinMaskTextureAndFullImageRegion:skinMaskTextureAndFullImageRegion:faceRect:roughSamples:commandBuffer:]
+ -[CMITextureStylesSkinSmoothStandalone _compileShaders]
+ -[CMITextureStylesSkinSmoothStandalone _computeTextureAmountFromInput:skinMask:personMask:faceMask:otherSkinMask:hairTxFloor:textureDetectScale:strongTextureProtect:textureBlurSigma:commandBuffer:fastMode:]
+ -[CMITextureStylesSkinSmoothStandalone _copyStatsBuffer:toHeapBufferOut:commandBuffer:]
+ -[CMITextureStylesSkinSmoothStandalone _createLargeBlurFromInputs:params:sigma:epsilon:filterRadius:downScaleFactor:commandBuffer:statsBuffer:]
+ -[CMITextureStylesSkinSmoothStandalone _createSmallBlurFromInput:sigma:filterRadius:downScaleFactor:commandBuffer:]
+ -[CMITextureStylesSkinSmoothStandalone _createTexture:label:]
+ -[CMITextureStylesSkinSmoothStandalone _createUncompressedTexture:label:]
+ -[CMITextureStylesSkinSmoothStandalone _packPrecomputedMasks:blendingParams:commandBuffer:packedMasks:faceDerived:]
+ -[CMITextureStylesSkinSmoothStandalone _performFinalBlending:parameters:smallBlurTextureAndFullImageRegion:statsBuffer:processedSkinMaskOverride:commandBuffer:]
+ -[CMITextureStylesSkinSmoothStandalone _popStatsBufferFromBufferPool]
+ -[CMITextureStylesSkinSmoothStandalone _processMultiPersonSkinMask:inputOutput:]
+ -[CMITextureStylesSkinSmoothStandalone _processSkinMask:inputMask:outputMask:maskFullImageRegion:personDataArray:]
+ -[CMITextureStylesSkinSmoothStandalone _returnStatsBufferToBufferPool:]
+ -[CMITextureStylesSkinSmoothStandalone _writeIntermediatesToExternalOutputs:]
+ -[CMITextureStylesSkinSmoothStandalone allocator]
+ -[CMITextureStylesSkinSmoothStandalone calculateStats]
+ -[CMITextureStylesSkinSmoothStandalone cameraInfoByPortType]
+ -[CMITextureStylesSkinSmoothStandalone computeMinimumInputRegionInFullImageCoords:]
+ -[CMITextureStylesSkinSmoothStandalone finishProcessing]
+ -[CMITextureStylesSkinSmoothStandalone fullImageSize]
+ -[CMITextureStylesSkinSmoothStandalone initWithOptionalMetalContext:]
+ -[CMITextureStylesSkinSmoothStandalone inputOutput]
+ -[CMITextureStylesSkinSmoothStandalone instanceID]
+ -[CMITextureStylesSkinSmoothStandalone metalCommandQueue]
+ -[CMITextureStylesSkinSmoothStandalone parameters]
+ -[CMITextureStylesSkinSmoothStandalone personData]
+ -[CMITextureStylesSkinSmoothStandalone prepareToProcess:]
+ -[CMITextureStylesSkinSmoothStandalone prewarm]
+ -[CMITextureStylesSkinSmoothStandalone process]
+ -[CMITextureStylesSkinSmoothStandalone purgeResources]
+ -[CMITextureStylesSkinSmoothStandalone regionToRender]
+ -[CMITextureStylesSkinSmoothStandalone resetState]
+ -[CMITextureStylesSkinSmoothStandalone scaleParametersWithIntensity:]
+ -[CMITextureStylesSkinSmoothStandalone setAllocator:]
+ -[CMITextureStylesSkinSmoothStandalone setCameraInfoByPortType:]
+ -[CMITextureStylesSkinSmoothStandalone setFullImageSize:]
+ -[CMITextureStylesSkinSmoothStandalone setInputOutput:]
+ -[CMITextureStylesSkinSmoothStandalone setInstanceID:]
+ -[CMITextureStylesSkinSmoothStandalone setMetalCommandQueue:]
+ -[CMITextureStylesSkinSmoothStandalone setParameters:]
+ -[CMITextureStylesSkinSmoothStandalone setPersonData:]
+ -[CMITextureStylesSkinSmoothStandalone setRegionToRender:]
+ -[CMITextureStylesSkinSmoothStandalone setStreamingMode:]
+ -[CMITextureStylesSkinSmoothStandalone setTuningParameters:]
+ -[CMITextureStylesSkinSmoothStandalone setup]
+ -[CMITextureStylesSkinSmoothStandalone ss_validateFaceSizeAndBlurParameters:fullImageSize:regionToRender:params:]
+ -[CMITextureStylesSkinSmoothStandalone streamingMode]
+ -[CMITextureStylesSkinSmoothStandalone supportsExternalMemoryResource]
+ -[CMITextureStylesSkinSmoothStandalone supportsInPlaceRendering]
+ -[CMITextureStylesSkinSmoothStandalone tuningParameters]
+ -[CMITextureStylesTextureCopy .cxx_destruct]
+ -[CMITextureStylesTextureCopy _compileShaders]
+ -[CMITextureStylesTextureCopy copyFromInputTexture:withInputROI:toOutputTexture:withOutputROI:encodedTo:]
+ -[CMITextureStylesTextureCopy copyFromInputTexture:withInputROI:toOutputTexture:withOutputROI:enqueuedTo:]
+ -[CMITextureStylesTextureCopy initWithMetalContext:]
+ -[CMITextureStylesTextureWarping .cxx_destruct]
+ -[CMITextureStylesTextureWarping _compileShaders]
+ -[CMITextureStylesTextureWarping _shaderForOutputPixelFormat:]
+ -[CMITextureStylesTextureWarping initWithMetalContext:]
+ -[CMITextureStylesTextureWarping processInput:output:triangleVertices:textureCoords:commandBuffer:]
+ -[CMITextureStylesUnderEyeBrighten .cxx_destruct]
+ -[CMITextureStylesUnderEyeBrighten _allocateStatsBuffers]
+ -[CMITextureStylesUnderEyeBrighten _brightenRegion:params:isLeftEye:roi:warpedUnderEyeReferenceMask:statsBuffer:taperedBrightnessMix:yawFactor:filterSigma:commandBuffer:regionToRender:instanceID:]
+ -[CMITextureStylesUnderEyeBrighten _calculateBlurEstimate]
+ -[CMITextureStylesUnderEyeBrighten _calculateStats:warpedUnderEyeReferenceMask:roi:regionToRender:statsBuffer:isLeftEye:commandBuffer:instanceID:]
+ -[CMITextureStylesUnderEyeBrighten _calculateVarianceBasedStrengthTaper:maximumUnimodalVariance:unimodalVarianceFalloff:maximumBimodalVariance:bimodalVarianceFalloff:commandBuffer:instanceID:]
+ -[CMITextureStylesUnderEyeBrighten _compileShaders]
+ -[CMITextureStylesUnderEyeBrighten _createWarpedReferenceMaskFromROI:isLeftEye:referenceMask:triangleVertices:textureCoords:maskFilterSigma:outputMask:commandBuffer:instanceID:]
+ -[CMITextureStylesUnderEyeBrighten _freeWarpedMasksAndStatsForPerson:]
+ -[CMITextureStylesUnderEyeBrighten _popStatsBuffer]
+ -[CMITextureStylesUnderEyeBrighten _removeWarpedMasksAndStatsForPerson:]
+ -[CMITextureStylesUnderEyeBrighten _returnStatsBuffer:]
+ -[CMITextureStylesUnderEyeBrighten allocator]
+ -[CMITextureStylesUnderEyeBrighten calculateStats]
+ -[CMITextureStylesUnderEyeBrighten cameraInfoByPortType]
+ -[CMITextureStylesUnderEyeBrighten computeMinimumInputRegionInFullImageCoords:]
+ -[CMITextureStylesUnderEyeBrighten dealloc]
+ -[CMITextureStylesUnderEyeBrighten finishProcessing]
+ -[CMITextureStylesUnderEyeBrighten fullImageSize]
+ -[CMITextureStylesUnderEyeBrighten initWithOptionalMetalContext:]
+ -[CMITextureStylesUnderEyeBrighten inputOutput]
+ -[CMITextureStylesUnderEyeBrighten instanceID]
+ -[CMITextureStylesUnderEyeBrighten metalCommandQueue]
+ -[CMITextureStylesUnderEyeBrighten parameters]
+ -[CMITextureStylesUnderEyeBrighten personData]
+ -[CMITextureStylesUnderEyeBrighten prepareToProcess:]
+ -[CMITextureStylesUnderEyeBrighten prewarm]
+ -[CMITextureStylesUnderEyeBrighten process]
+ -[CMITextureStylesUnderEyeBrighten purgeResources]
+ -[CMITextureStylesUnderEyeBrighten regionToRender]
+ -[CMITextureStylesUnderEyeBrighten resetState]
+ -[CMITextureStylesUnderEyeBrighten scaleParametersWithIntensity:]
+ -[CMITextureStylesUnderEyeBrighten setAllocator:]
+ -[CMITextureStylesUnderEyeBrighten setCameraInfoByPortType:]
+ -[CMITextureStylesUnderEyeBrighten setFullImageSize:]
+ -[CMITextureStylesUnderEyeBrighten setInputOutput:]
+ -[CMITextureStylesUnderEyeBrighten setInstanceID:]
+ -[CMITextureStylesUnderEyeBrighten setMetalCommandQueue:]
+ -[CMITextureStylesUnderEyeBrighten setParameters:]
+ -[CMITextureStylesUnderEyeBrighten setPersonData:]
+ -[CMITextureStylesUnderEyeBrighten setRegionToRender:]
+ -[CMITextureStylesUnderEyeBrighten setSkipRendering:]
+ -[CMITextureStylesUnderEyeBrighten setTuningParameters:]
+ -[CMITextureStylesUnderEyeBrighten setup]
+ -[CMITextureStylesUnderEyeBrighten skipRendering]
+ -[CMITextureStylesUnderEyeBrighten supportsExternalMemoryResource]
+ -[CMITextureStylesUnderEyeBrighten supportsInPlaceRendering]
+ -[CMITextureStylesUnderEyeBrighten tuningParameters]
+ -[CMITextureStylesUnderEyeBrightenIO .cxx_destruct]
+ -[CMITextureStylesUnderEyeBrightenIO brightnessValue]
+ -[CMITextureStylesUnderEyeBrightenIO inputEarMask]
+ -[CMITextureStylesUnderEyeBrightenIO inputFaceMask]
+ -[CMITextureStylesUnderEyeBrightenIO inputGlassesMask]
+ -[CMITextureStylesUnderEyeBrightenIO inputHairMask]
+ -[CMITextureStylesUnderEyeBrightenIO inputImage]
+ -[CMITextureStylesUnderEyeBrightenIO inputInstanceMask]
+ -[CMITextureStylesUnderEyeBrightenIO inputLipMask]
+ -[CMITextureStylesUnderEyeBrightenIO inputNoseMask]
+ -[CMITextureStylesUnderEyeBrightenIO inputTattooMask]
+ -[CMITextureStylesUnderEyeBrightenIO outputImage]
+ -[CMITextureStylesUnderEyeBrightenIO outputPersonStats]
+ -[CMITextureStylesUnderEyeBrightenIO setBrightnessValue:]
+ -[CMITextureStylesUnderEyeBrightenIO setInputEarMask:]
+ -[CMITextureStylesUnderEyeBrightenIO setInputFaceMask:]
+ -[CMITextureStylesUnderEyeBrightenIO setInputGlassesMask:]
+ -[CMITextureStylesUnderEyeBrightenIO setInputHairMask:]
+ -[CMITextureStylesUnderEyeBrightenIO setInputImage:]
+ -[CMITextureStylesUnderEyeBrightenIO setInputInstanceMask:]
+ -[CMITextureStylesUnderEyeBrightenIO setInputLipMask:]
+ -[CMITextureStylesUnderEyeBrightenIO setInputNoseMask:]
+ -[CMITextureStylesUnderEyeBrightenIO setInputTattooMask:]
+ -[CMITextureStylesUnderEyeBrightenIO setOutputImage:]
+ -[CMITextureStylesUnderEyeBrightenIO setOutputPersonStats:]
+ -[CMITextureStylesUnderEyeBrightenParameters _boolFromDict:key:default:]
+ -[CMITextureStylesUnderEyeBrightenParameters _floatFromDict:key:default:]
+ -[CMITextureStylesUnderEyeBrightenParameters averageColorMix]
+ -[CMITextureStylesUnderEyeBrightenParameters bimodalVarianceFalloff]
+ -[CMITextureStylesUnderEyeBrightenParameters blendConditionFilterScale]
+ -[CMITextureStylesUnderEyeBrightenParameters brightnessMix]
+ -[CMITextureStylesUnderEyeBrightenParameters colorBlendFilterScale]
+ -[CMITextureStylesUnderEyeBrightenParameters copyWithZone:]
+ -[CMITextureStylesUnderEyeBrightenParameters dominantYawTapering]
+ -[CMITextureStylesUnderEyeBrightenParameters hueMaskFilterScale]
+ -[CMITextureStylesUnderEyeBrightenParameters initWithTuningDictionary:]
+ -[CMITextureStylesUnderEyeBrightenParameters init]
+ -[CMITextureStylesUnderEyeBrightenParameters maskThreshold]
+ -[CMITextureStylesUnderEyeBrightenParameters maxDarknessTrigger]
+ -[CMITextureStylesUnderEyeBrightenParameters maxFaceFrac]
+ -[CMITextureStylesUnderEyeBrightenParameters maxHueTolerance]
+ -[CMITextureStylesUnderEyeBrightenParameters maximumBimodalVariance]
+ -[CMITextureStylesUnderEyeBrightenParameters maximumUnimodalVariance]
+ -[CMITextureStylesUnderEyeBrightenParameters minDarknessTrigger]
+ -[CMITextureStylesUnderEyeBrightenParameters minFaceFrac]
+ -[CMITextureStylesUnderEyeBrightenParameters minHueTolerance]
+ -[CMITextureStylesUnderEyeBrightenParameters minTextureAddBack]
+ -[CMITextureStylesUnderEyeBrightenParameters nightModeSharpness]
+ -[CMITextureStylesUnderEyeBrightenParameters nightMode]
+ -[CMITextureStylesUnderEyeBrightenParameters regionMaskThreshold]
+ -[CMITextureStylesUnderEyeBrightenParameters setAverageColorMix:]
+ -[CMITextureStylesUnderEyeBrightenParameters setBimodalVarianceFalloff:]
+ -[CMITextureStylesUnderEyeBrightenParameters setBlendConditionFilterScale:]
+ -[CMITextureStylesUnderEyeBrightenParameters setBrightnessMix:]
+ -[CMITextureStylesUnderEyeBrightenParameters setColorBlendFilterScale:]
+ -[CMITextureStylesUnderEyeBrightenParameters setDefaults]
+ -[CMITextureStylesUnderEyeBrightenParameters setDominantYawTapering:]
+ -[CMITextureStylesUnderEyeBrightenParameters setHueMaskFilterScale:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMaskThreshold:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMaxDarknessTrigger:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMaxFaceFrac:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMaxHueTolerance:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMaximumBimodalVariance:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMaximumUnimodalVariance:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMinDarknessTrigger:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMinFaceFrac:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMinHueTolerance:]
+ -[CMITextureStylesUnderEyeBrightenParameters setMinTextureAddBack:]
+ -[CMITextureStylesUnderEyeBrightenParameters setNightMode:]
+ -[CMITextureStylesUnderEyeBrightenParameters setNightModeSharpness:]
+ -[CMITextureStylesUnderEyeBrightenParameters setRegionMaskThreshold:]
+ -[CMITextureStylesUnderEyeBrightenParameters setTextureAddBackFilterScale:]
+ -[CMITextureStylesUnderEyeBrightenParameters setTextureAddBackScale:]
+ -[CMITextureStylesUnderEyeBrightenParameters setUnimodalVarianceFalloff:]
+ -[CMITextureStylesUnderEyeBrightenParameters setYawFallOff:]
+ -[CMITextureStylesUnderEyeBrightenParameters setYawOffset:]
+ -[CMITextureStylesUnderEyeBrightenParameters textureAddBackFilterScale]
+ -[CMITextureStylesUnderEyeBrightenParameters textureAddBackScale]
+ -[CMITextureStylesUnderEyeBrightenParameters unimodalVarianceFalloff]
+ -[CMITextureStylesUnderEyeBrightenParameters validate]
+ -[CMITextureStylesUnderEyeBrightenParameters yawFallOff]
+ -[CMITextureStylesUnderEyeBrightenParameters yawOffset]
+ -[CMITiledInferenceProcessorConfig bufferCountDualANE]
+ -[CMITiledInferenceProcessorConfig setBufferCountDualANE:]
+ -[NSArray(CMILCB) arrayContainingDictionaryRepresentations]
+ GCC_except_table111
+ GCC_except_table115
+ GCC_except_table28
+ GCC_except_table34
+ GCC_except_table47
+ GCC_except_table51
+ GCC_except_table95
+ GCC_except_table96
+ GCC_except_table98
+ GCC_except_table99
+ _CGPointZero
+ _CGRectIntersectsRect
+ _CGRectUnion
+ _CMCaptureLibrary
+ _CMCaptureLibraryCore.frameworkLibrary
+ _CMITSdiagonalLengthOfSize
+ _CMITSfullImageRectToTextureRect
+ _CMITSidealDispatchSize
+ _CMITSidealThreadGroupSize
+ _CMITSpointDenormalizedToRect
+ _CMITSpointNormalizedToRect
+ _CMITSrectDenormalizedToRect
+ _CMITSrectExpandedByPadding
+ _CMITSrectNormalizedToRect
+ _CMITSsetTextureAndNormalizedRectOnEncoder
+ _CMITStexturesAreIdentical
+ _CMITextureStylePresetNameFilmic
+ _CMITextureStylePresetNameGlowy
+ _CMITextureStylePresetNameSoft
+ _CMITextureStylePresetNameStandard
+ _CMITextureStylePresetNameStudio
+ _CMITextureStylesPersonInputData_NOTE_VARIABLE
+ _FASTGAUSSIAN_NOTE_VARIABLE
+ _FigGetCFPreferenceBooleanWithDefault
+ _GUIDEDFILTERV3_NOTE_VARIABLE
+ _Mattify_CONFIGURATION_NOTE_VARIABLE
+ _NSStringFromClass
+ _OBJC_CLASS_$_CMILCBDatabase
+ _OBJC_CLASS_$_CMILCBEntry
+ _OBJC_CLASS_$_CMITSMattifyPerPersonIntermediatesAndStats
+ _OBJC_CLASS_$_CMITSTextureAndFullImageRegion
+ _OBJC_CLASS_$_CMITSUEBPerPersonData
+ _OBJC_CLASS_$_CMITextureStyle
+ _OBJC_CLASS_$_CMITextureStyleTuningLookup
+ _OBJC_CLASS_$_CMITextureStylesBloom
+ _OBJC_CLASS_$_CMITextureStylesBloomIO
+ _OBJC_CLASS_$_CMITextureStylesBloomParameters
+ _OBJC_CLASS_$_CMITextureStylesDiffusion
+ _OBJC_CLASS_$_CMITextureStylesDiffusionIO
+ _OBJC_CLASS_$_CMITextureStylesDiffusionParameters
+ _OBJC_CLASS_$_CMITextureStylesDownSampler
+ _OBJC_CLASS_$_CMITextureStylesEffectDescriptor
+ _OBJC_CLASS_$_CMITextureStylesFaceLandmark
+ _OBJC_CLASS_$_CMITextureStylesFastGaussian
+ _OBJC_CLASS_$_CMITextureStylesFilmGrainIO
+ _OBJC_CLASS_$_CMITextureStylesFilmGrainParameters
+ _OBJC_CLASS_$_CMITextureStylesFilmGrainProcessorV1
+ _OBJC_CLASS_$_CMITextureStylesFilter
+ _OBJC_CLASS_$_CMITextureStylesGaussianFilter
+ _OBJC_CLASS_$_CMITextureStylesGaussianGuidedFilterV3
+ _OBJC_CLASS_$_CMITextureStylesGlow
+ _OBJC_CLASS_$_CMITextureStylesGlowIO
+ _OBJC_CLASS_$_CMITextureStylesGlowParameters
+ _OBJC_CLASS_$_CMITextureStylesGuidedFilter
+ _OBJC_CLASS_$_CMITextureStylesHalation
+ _OBJC_CLASS_$_CMITextureStylesHalationIO
+ _OBJC_CLASS_$_CMITextureStylesHalationParameters
+ _OBJC_CLASS_$_CMITextureStylesMattify
+ _OBJC_CLASS_$_CMITextureStylesMattifyIO
+ _OBJC_CLASS_$_CMITextureStylesMattifyParameters
+ _OBJC_CLASS_$_CMITextureStylesPersonInputData
+ _OBJC_CLASS_$_CMITextureStylesPersonInputDataUtilities
+ _OBJC_CLASS_$_CMITextureStylesProcessor
+ _OBJC_CLASS_$_CMITextureStylesPyramid
+ _OBJC_CLASS_$_CMITextureStylesPyramidFactory
+ _OBJC_CLASS_$_CMITextureStylesSkinSmoothIO
+ _OBJC_CLASS_$_CMITextureStylesSkinSmoothParameters
+ _OBJC_CLASS_$_CMITextureStylesSkinSmoothStandalone
+ _OBJC_CLASS_$_CMITextureStylesTextureCopy
+ _OBJC_CLASS_$_CMITextureStylesTextureWarping
+ _OBJC_CLASS_$_CMITextureStylesUnderEyeBrighten
+ _OBJC_CLASS_$_CMITextureStylesUnderEyeBrightenIO
+ _OBJC_CLASS_$_CMITextureStylesUnderEyeBrightenParameters
+ _OBJC_CLASS_$_MTLRenderPipelineColorAttachmentDescriptor
+ _OBJC_CLASS_$_NSConstantFloatNumber
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_IVAR_$_CMILCBDatabase._detectionIteration
+ _OBJC_IVAR_$_CMILCBDatabase._entriesByKey
+ _OBJC_IVAR_$_CMILCBDatabase._moduleSerial
+ _OBJC_IVAR_$_CMILCBDatabase._sensorID
+ _OBJC_IVAR_$_CMILCBEntry._apertureRatio
+ _OBJC_IVAR_$_CMILCBEntry._correctionFeatures
+ _OBJC_IVAR_$_CMILCBEntry._defocusRadius
+ _OBJC_IVAR_$_CMILCBEntry._detectionCount
+ _OBJC_IVAR_$_CMILCBEntry._focusLensPosition
+ _OBJC_IVAR_$_CMILCBEntry._key
+ _OBJC_IVAR_$_CMILCBEntry._lastDetectionGravityVector
+ _OBJC_IVAR_$_CMILCBEntry._lastDetectionTimeStamp
+ _OBJC_IVAR_$_CMILCBEntry._maxCorrectionFeatureValue
+ _OBJC_IVAR_$_CMILCBEntry._minCorrectionFeatureValue
+ _OBJC_IVAR_$_CMILCBEntry._oisShift
+ _OBJC_IVAR_$_CMILCBEntry._opticalCenter
+ _OBJC_IVAR_$_CMILCBEntry._particleDistance
+ _OBJC_IVAR_$_CMILCBEntry._position
+ _OBJC_IVAR_$_CMILCBEntry._radius
+ _OBJC_IVAR_$_CMILCBEntry._relativeToLens
+ _OBJC_IVAR_$_CMILCBEntry._shouldCorrect
+ _OBJC_IVAR_$_CMISmartStyleUtilitiesV1._enableDeltaMapDetailEnhancement
+ _OBJC_IVAR_$_CMISmartStyleUtilitiesV1._enhanceDetailDefaults
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._filteredGFSigma
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._inputFaceNormalizedRects
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._inputSkinMaskFlipHorizontal
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._inputSkinMaskFlipVertical
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._inputSkinMaskICR
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._inputSkinMaskPCR
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._inputSkinMaskRotationDegrees
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._inputSkinMaskTexture
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._inputSkinSmoothingParameters
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._proxyCoeff
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._proxyMean
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._skinSmoothGuidedAvgPipeline
+ _OBJC_IVAR_$_CMIStyleEngineApplyStyle._skinSmoothGuidedCoeffPipeline
+ _OBJC_IVAR_$_CMIStyleEngineProcessor._inputFaceNormalizedRects
+ _OBJC_IVAR_$_CMIStyleEngineProcessor._inputSkinMaskFlipHorizontal
+ _OBJC_IVAR_$_CMIStyleEngineProcessor._inputSkinMaskFlipVertical
+ _OBJC_IVAR_$_CMIStyleEngineProcessor._inputSkinMaskICR
+ _OBJC_IVAR_$_CMIStyleEngineProcessor._inputSkinMaskPCR
+ _OBJC_IVAR_$_CMIStyleEngineProcessor._inputSkinMaskRotationDegrees
+ _OBJC_IVAR_$_CMIStyleEngineProcessor._inputSkinMaskTexture
+ _OBJC_IVAR_$_CMIStyleEngineProcessor._inputSkinSmoothingParameters
+ _OBJC_IVAR_$_CMITSMattifyPerPersonIntermediatesAndStats._extendedFaceROI
+ _OBJC_IVAR_$_CMITSMattifyPerPersonIntermediatesAndStats._statsBuffer
+ _OBJC_IVAR_$_CMITSMattifyPerPersonIntermediatesAndStats._validMask
+ _OBJC_IVAR_$_CMITSMattifyPerPersonIntermediatesAndStats._warpedMaskAggregate
+ _OBJC_IVAR_$_CMITSTextureAndFullImageRegion._fullImageRegion
+ _OBJC_IVAR_$_CMITSTextureAndFullImageRegion._texture
+ _OBJC_IVAR_$_CMITSUEBPerPersonData._eyeROI
+ _OBJC_IVAR_$_CMITSUEBPerPersonData._statsBuffer
+ _OBJC_IVAR_$_CMITSUEBPerPersonData._warpedReferenceMasks
+ _OBJC_IVAR_$_CMITextureStyle._grain
+ _OBJC_IVAR_$_CMITextureStyle._intensity
+ _OBJC_IVAR_$_CMITextureStyle._preset
+ _OBJC_IVAR_$_CMITextureStylesBloom._cameraInfoByPortType
+ _OBJC_IVAR_$_CMITextureStylesBloom._colorManagement
+ _OBJC_IVAR_$_CMITextureStylesBloom._fullImageSize
+ _OBJC_IVAR_$_CMITextureStylesBloom._generateBloomPipelineState
+ _OBJC_IVAR_$_CMITextureStylesBloom._inputOutput
+ _OBJC_IVAR_$_CMITextureStylesBloom._instanceID
+ _OBJC_IVAR_$_CMITextureStylesBloom._metalContext
+ _OBJC_IVAR_$_CMITextureStylesBloom._parameters
+ _OBJC_IVAR_$_CMITextureStylesBloom._personData
+ _OBJC_IVAR_$_CMITextureStylesBloom._regionToRender
+ _OBJC_IVAR_$_CMITextureStylesBloom._tuningParameters
+ _OBJC_IVAR_$_CMITextureStylesBloomIO._inputImage
+ _OBJC_IVAR_$_CMITextureStylesBloomIO._inputSkinMask
+ _OBJC_IVAR_$_CMITextureStylesBloomIO._outputImage
+ _OBJC_IVAR_$_CMITextureStylesBloomParameters._brightness
+ _OBJC_IVAR_$_CMITextureStylesBloomParameters._inputTextureROI
+ _OBJC_IVAR_$_CMITextureStylesBloomParameters._lightMapGamma
+ _OBJC_IVAR_$_CMITextureStylesBloomParameters._lightMapInvert
+ _OBJC_IVAR_$_CMITextureStylesBloomParameters._sigmaGlare
+ _OBJC_IVAR_$_CMITextureStylesBloomParameters._skinMask
+ _OBJC_IVAR_$_CMITextureStylesBloomParameters._strength
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._applyDiffusion
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._applyMeteor
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._cameraInfoByPortType
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._colorManagement
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._filterer
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._fullImageSize
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._inputOutput
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._inputRescaled
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._instanceID
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._metalContext
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._meteorMixed
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._outputBlurredImage
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._parameters
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._personData
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._regionToRender
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._rescale420ToRGBA
+ _OBJC_IVAR_$_CMITextureStylesDiffusion._tuningParameters
+ _OBJC_IVAR_$_CMITextureStylesDiffusionIO._inputGainMap
+ _OBJC_IVAR_$_CMITextureStylesDiffusionIO._inputImage
+ _OBJC_IVAR_$_CMITextureStylesDiffusionIO._inputPersonMask
+ _OBJC_IVAR_$_CMITextureStylesDiffusionIO._inputSkinMask
+ _OBJC_IVAR_$_CMITextureStylesDiffusionIO._outputImage
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._bg
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._bw3Gamma
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._difSat
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._diffuseColor
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._faceTempering
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._fogStrength
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._gaussianBlurSigma
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._grading
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._highlight
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._hueRotate
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._lift
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._maxRGB
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._meteorHeadroom
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._meteorHeadroomMixFactor
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._naturalResolution
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._person
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._saturation
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._shDarken
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._slBG
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._slBright
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._slDark
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._slPerson
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._slSkin
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._softLight
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._spbHL
+ _OBJC_IVAR_$_CMITextureStylesDiffusionParameters._strength
+ _OBJC_IVAR_$_CMITextureStylesDownSampler._context
+ _OBJC_IVAR_$_CMITextureStylesDownSampler._pyramidFactory
+ _OBJC_IVAR_$_CMITextureStylesDownSampler._shaders
+ _OBJC_IVAR_$_CMITextureStylesEffectDescriptor._parameters
+ _OBJC_IVAR_$_CMITextureStylesEffectDescriptor._skipRendering
+ _OBJC_IVAR_$_CMITextureStylesEffectDescriptor._type
+ _OBJC_IVAR_$_CMITextureStylesFaceLandmark._error
+ _OBJC_IVAR_$_CMITextureStylesFaceLandmark._point
+ _OBJC_IVAR_$_CMITextureStylesFastGaussian._context
+ _OBJC_IVAR_$_CMITextureStylesFastGaussian._shaders
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainIO._brightnessValue
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainIO._inputImage
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainIO._inputPersonImage
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainIO._inputSkinImage
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainIO._inputSkyImage
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainIO._outputImage
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._amplitude
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._amplitudeDecay
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._backgroundStrength
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._bvHigh
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._bvLow
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._bvLowScale
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._contrastBoost
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._darkScale
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._frequencyGap
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._grainBlurRadius
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._grainSelectivity
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._hueMix
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._imageGuidedFilterEpsilon
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._imageGuidedFilterRadius
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._naturalResolution
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._octaves
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._personStrength
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._saturation
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._seed
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._shadowLift
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._skinStrength
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._skyStrength
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._strength
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._tileSize
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainParameters._zoom
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._cameraInfoByPortType
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._colorManagement
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._fullImageSize
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._grainBlendPipeline
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._inputOutput
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._instanceID
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._metalContext
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._parameters
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._personData
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._regionToRender
+ _OBJC_IVAR_$_CMITextureStylesFilmGrainProcessorV1._tuningParameters
+ _OBJC_IVAR_$_CMITextureStylesFilter._context
+ _OBJC_IVAR_$_CMITextureStylesFilter._shaders
+ _OBJC_IVAR_$_CMITextureStylesGaussianFilter._context
+ _OBJC_IVAR_$_CMITextureStylesGaussianFilter._shaders
+ _OBJC_IVAR_$_CMITextureStylesGaussianGuidedFilterV3._context
+ _OBJC_IVAR_$_CMITextureStylesGaussianGuidedFilterV3._shaders
+ _OBJC_IVAR_$_CMITextureStylesGlow._cameraInfoByPortType
+ _OBJC_IVAR_$_CMITextureStylesGlow._colorManagement
+ _OBJC_IVAR_$_CMITextureStylesGlow._fakeStatsBuffer
+ _OBJC_IVAR_$_CMITextureStylesGlow._fillToneCurvePipelineState
+ _OBJC_IVAR_$_CMITextureStylesGlow._frameCount
+ _OBJC_IVAR_$_CMITextureStylesGlow._fullImageSize
+ _OBJC_IVAR_$_CMITextureStylesGlow._generateGlowPipelineState
+ _OBJC_IVAR_$_CMITextureStylesGlow._inputOutput
+ _OBJC_IVAR_$_CMITextureStylesGlow._instanceID
+ _OBJC_IVAR_$_CMITextureStylesGlow._metalContext
+ _OBJC_IVAR_$_CMITextureStylesGlow._parameters
+ _OBJC_IVAR_$_CMITextureStylesGlow._personData
+ _OBJC_IVAR_$_CMITextureStylesGlow._regionToRender
+ _OBJC_IVAR_$_CMITextureStylesGlow._streamingMode
+ _OBJC_IVAR_$_CMITextureStylesGlow._tuningParameters
+ _OBJC_IVAR_$_CMITextureStylesGlowIO._inputImage
+ _OBJC_IVAR_$_CMITextureStylesGlowIO._inputLinearImage
+ _OBJC_IVAR_$_CMITextureStylesGlowIO._inputLinearMetadata
+ _OBJC_IVAR_$_CMITextureStylesGlowIO._inputMask
+ _OBJC_IVAR_$_CMITextureStylesGlowIO._outputImage
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._baselineExposure
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._brightness
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._brightnessMask
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._contrast
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._contrastMask
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._gamma
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._gammaMask
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._inputTextureROI
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._lightMapGamma
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._lightMapMax
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._linearImageHighKey
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._linearMixForBG
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._linearMixForSkin
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._preserveColorfulness
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._preserveColorfulnessMask
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._saturation
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._saturationFromSmartStyle
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._saturationMask
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._statistics
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._strength
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._strengthMask
+ _OBJC_IVAR_$_CMITextureStylesGlowParameters._useStatistics
+ _OBJC_IVAR_$_CMITextureStylesGuidedFilter._context
+ _OBJC_IVAR_$_CMITextureStylesGuidedFilter._shaders
+ _OBJC_IVAR_$_CMITextureStylesHalation._applyHalation
+ _OBJC_IVAR_$_CMITextureStylesHalation._asymLumaMask
+ _OBJC_IVAR_$_CMITextureStylesHalation._blurredSubtractMask
+ _OBJC_IVAR_$_CMITextureStylesHalation._cameraInfoByPortType
+ _OBJC_IVAR_$_CMITextureStylesHalation._colorManagement
+ _OBJC_IVAR_$_CMITextureStylesHalation._filterer
+ _OBJC_IVAR_$_CMITextureStylesHalation._fullImageSize
+ _OBJC_IVAR_$_CMITextureStylesHalation._generateLumAsymMask
+ _OBJC_IVAR_$_CMITextureStylesHalation._halationMask
+ _OBJC_IVAR_$_CMITextureStylesHalation._inputOutput
+ _OBJC_IVAR_$_CMITextureStylesHalation._instanceID
+ _OBJC_IVAR_$_CMITextureStylesHalation._metalContext
+ _OBJC_IVAR_$_CMITextureStylesHalation._parameters
+ _OBJC_IVAR_$_CMITextureStylesHalation._personData
+ _OBJC_IVAR_$_CMITextureStylesHalation._regionToRender
+ _OBJC_IVAR_$_CMITextureStylesHalation._subtractBlendMode
+ _OBJC_IVAR_$_CMITextureStylesHalation._subtractMask
+ _OBJC_IVAR_$_CMITextureStylesHalation._tuningParameters
+ _OBJC_IVAR_$_CMITextureStylesHalationIO._brightnessValue
+ _OBJC_IVAR_$_CMITextureStylesHalationIO._inputGainMap
+ _OBJC_IVAR_$_CMITextureStylesHalationIO._inputHDRImage
+ _OBJC_IVAR_$_CMITextureStylesHalationIO._inputImage
+ _OBJC_IVAR_$_CMITextureStylesHalationIO._inputLightMap
+ _OBJC_IVAR_$_CMITextureStylesHalationIO._inputPersonMask
+ _OBJC_IVAR_$_CMITextureStylesHalationIO._inputSkinMask
+ _OBJC_IVAR_$_CMITextureStylesHalationIO._outputImage
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._bg
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._bvHigh
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._bvLow
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._bvThresholdDeltaLowScale
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._faceTempering
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._halationChroma
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._halationHue
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputInnerKnot0
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputInnerKnot1
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputLowerBound
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputLowerCoeffA
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputLowerCoeffB
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputOuterKnot0
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputOuterKnot1
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputSpread
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputTextureROI
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputThresholdDelta
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputUpperCoeffA
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._inputUpperCoeffB
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._maskBlurSigma
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._maxRGB
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._meteorHeadroom
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._meteorHeadroomMixFactor
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._naturalResolution
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._person
+ _OBJC_IVAR_$_CMITextureStylesHalationParameters._strength
+ _OBJC_IVAR_$_CMITextureStylesMattify._blurProcessor
+ _OBJC_IVAR_$_CMITextureStylesMattify._cameraInfoByPortType
+ _OBJC_IVAR_$_CMITextureStylesMattify._context
+ _OBJC_IVAR_$_CMITextureStylesMattify._fullImageSize
+ _OBJC_IVAR_$_CMITextureStylesMattify._inputOutput
+ _OBJC_IVAR_$_CMITextureStylesMattify._instanceID
+ _OBJC_IVAR_$_CMITextureStylesMattify._parameters
+ _OBJC_IVAR_$_CMITextureStylesMattify._perPersonIntermediatesAndStats
+ _OBJC_IVAR_$_CMITextureStylesMattify._personData
+ _OBJC_IVAR_$_CMITextureStylesMattify._pyramidFactory
+ _OBJC_IVAR_$_CMITextureStylesMattify._regionToRender
+ _OBJC_IVAR_$_CMITextureStylesMattify._shadersWithConstants
+ _OBJC_IVAR_$_CMITextureStylesMattify._shadersWithoutConstants
+ _OBJC_IVAR_$_CMITextureStylesMattify._skipRendering
+ _OBJC_IVAR_$_CMITextureStylesMattify._streamingMode
+ _OBJC_IVAR_$_CMITextureStylesMattify._textureCopier
+ _OBJC_IVAR_$_CMITextureStylesMattify._tuningParameters
+ _OBJC_IVAR_$_CMITextureStylesMattify._warper
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._inputEarMask
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._inputFaceMask
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._inputGlassesMask
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._inputImage
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._inputInstanceMask
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._inputLipsMask
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._inputNoseMask
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._inputSkinMask
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._inputTattoosMask
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._outputImage
+ _OBJC_IVAR_$_CMITextureStylesMattifyIO._outputPersonStats
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._blendColorImageAverageColorMixFactor
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._darknessDiffSmoothstepLowerBound
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._darknessDiffSmoothstepUpperBound
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._editingStrength
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._fracMaskHighlightsHeadroom
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._fracMaskHighlightsNormFactor
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._hueDiffMeanTermSmoothstepLowerBound
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._hueDiffMeanTermSmoothstepUpperBound
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._hueDiffSmoothstepLowerBound
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._hueDiffSmoothstepUpperBound
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._imageTextureFactor
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._imageTextureThreshold
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._largeBlurRadiusFaceDiagonalFactor
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._lightnessEditFactor
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._lightnessEditHeadroom
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._smallBlurRadiusFaceDiagonalFactor
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._textureRestoreScalingFactor
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._textureRestoreSmoothstepLowerBound
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._textureRestoreSmoothstepUpperBound
+ _OBJC_IVAR_$_CMITextureStylesMattifyParameters._textureRestoreStrengthFactor
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._faceID
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._faceLandmarkType
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._faceLandmarks
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._facePitch
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._faceROI
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._faceROIAndLandmarksROIRelativeScalingROI
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._faceRoll
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._faceSkinROI
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._faceYaw
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._imageStats
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._instanceMask
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._instanceMaskReferenceKey
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._instanceROI
+ _OBJC_IVAR_$_CMITextureStylesPersonInputData._unitOfAngle
+ _OBJC_IVAR_$_CMITextureStylesProcessor._bloom
+ _OBJC_IVAR_$_CMITextureStylesProcessor._brightnessValue
+ _OBJC_IVAR_$_CMITextureStylesProcessor._bufferCache
+ _OBJC_IVAR_$_CMITextureStylesProcessor._cameraInfoByPortType
+ _OBJC_IVAR_$_CMITextureStylesProcessor._diffusion
+ _OBJC_IVAR_$_CMITextureStylesProcessor._effectsToRender
+ _OBJC_IVAR_$_CMITextureStylesProcessor._enableSkinSmoothingMultiPersonBlending
+ _OBJC_IVAR_$_CMITextureStylesProcessor._externalMemoryResource
+ _OBJC_IVAR_$_CMITextureStylesProcessor._filmGrain
+ _OBJC_IVAR_$_CMITextureStylesProcessor._fullImageSize
+ _OBJC_IVAR_$_CMITextureStylesProcessor._glow
+ _OBJC_IVAR_$_CMITextureStylesProcessor._halation
+ _OBJC_IVAR_$_CMITextureStylesProcessor._inputImage
+ _OBJC_IVAR_$_CMITextureStylesProcessor._inputLinearImage
+ _OBJC_IVAR_$_CMITextureStylesProcessor._inputLinearImageMetadata
+ _OBJC_IVAR_$_CMITextureStylesProcessor._inputMasks
+ _OBJC_IVAR_$_CMITextureStylesProcessor._inputMeteorGainMap
+ _OBJC_IVAR_$_CMITextureStylesProcessor._inputPersonData
+ _OBJC_IVAR_$_CMITextureStylesProcessor._inputPingPongImageForRendering
+ _OBJC_IVAR_$_CMITextureStylesProcessor._inputSkinSmoothingFaceDetections
+ _OBJC_IVAR_$_CMITextureStylesProcessor._label
+ _OBJC_IVAR_$_CMITextureStylesProcessor._mattify
+ _OBJC_IVAR_$_CMITextureStylesProcessor._memoryResource
+ _OBJC_IVAR_$_CMITextureStylesProcessor._metalContext
+ _OBJC_IVAR_$_CMITextureStylesProcessor._outputImage
+ _OBJC_IVAR_$_CMITextureStylesProcessor._outputPersonImageStats
+ _OBJC_IVAR_$_CMITextureStylesProcessor._outputSkinSmoothingLargeBlurGuidedFilterA
+ _OBJC_IVAR_$_CMITextureStylesProcessor._outputSkinSmoothingLargeBlurGuidedFilterB
+ _OBJC_IVAR_$_CMITextureStylesProcessor._outputSkinSmoothingProcessedMask
+ _OBJC_IVAR_$_CMITextureStylesProcessor._outputSkinSmoothingSmallBlur
+ _OBJC_IVAR_$_CMITextureStylesProcessor._outputSkinSmoothingStats
+ _OBJC_IVAR_$_CMITextureStylesProcessor._outputSkinSmoothingTextureAddback
+ _OBJC_IVAR_$_CMITextureStylesProcessor._regionToRender
+ _OBJC_IVAR_$_CMITextureStylesProcessor._shouldFlushCVMTLCachesOnResetState
+ _OBJC_IVAR_$_CMITextureStylesProcessor._skinSmoothStandalone
+ _OBJC_IVAR_$_CMITextureStylesProcessor._streamingMode
+ _OBJC_IVAR_$_CMITextureStylesProcessor._textureCache
+ _OBJC_IVAR_$_CMITextureStylesProcessor._textureCopier
+ _OBJC_IVAR_$_CMITextureStylesProcessor._textureStyleIntensity
+ _OBJC_IVAR_$_CMITextureStylesProcessor._tuningParameters
+ _OBJC_IVAR_$_CMITextureStylesProcessor._underEyeBrighten
+ _OBJC_IVAR_$_CMITextureStylesPyramid._levels
+ _OBJC_IVAR_$_CMITextureStylesPyramidFactory._context
+ _OBJC_IVAR_$_CMITextureStylesPyramidFactory._shaders
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._allPersonDataForBlending
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._bodyMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._brightnessValue
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._earsMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._externalFaceRoughnessStatsOutput
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._externalLargeBlurGuidedFilterAOutput
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._externalLargeBlurGuidedFilterBOutput
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._externalSmallBlurOutput
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._externalTextureAddbackOutput
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._eyebrowsMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._faceSkinMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._glassesMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._hairMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._handsMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._inputFaceRect
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._inputImage
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._inputSkinMaskAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._instanceMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._lipsMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._outputImage
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._outputPersonStats
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._outputProcessedSkinMask
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._personMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._tattoosMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothIO._teethMaskTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._degrunge
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._degrungeBody
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._detailSize
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._enableTextureAddback
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._eyeProtection
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._eyebrows
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._fastMode
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._gFContrast
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._gFRadius
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._hairClothes
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._hairTxFloor
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._handsAndEars
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._highlightRetention
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._hlBlurStrength
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._hlTextureRestore
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._lipContrast
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._lipCrease
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._lipHighlights
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._lipNegClar
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._maxDarknessTrigger
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._minDarknessTrigger
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._minTexture
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._nightMode
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._nightModeSharpness
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._plusGreenGuide
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._pores
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._poresBody
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._roughSamples
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._strongTextureProtect
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._tattooSmoothing
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._tattooWeight
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._teeth
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._textureClamp
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._textureDetectScale
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._textureRestore
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothParameters._varTexture
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._applyBlobToSingleFace
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._blurredTextureAmountTexture
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._cameraInfoByPortType
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._context
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._downSampler
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._enableMultiPersonBlending
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._filterer
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._fullImageSize
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._guidedFilterATextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._guidedFilterBTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._inputOutput
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._instanceID
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._internalProcessedSkinMask
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._parameters
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._personData
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._regionToRender
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._shaders
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._skipLargeBlurCompute
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._skipSmallBlurCompute
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._smallBlurTextureAndFullImageRegion
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._statsBuffer
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._statsBufferPool
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._streamingMode
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._syntheticSkinTexture
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._textureCopier
+ _OBJC_IVAR_$_CMITextureStylesSkinSmoothStandalone._tuningParameters
+ _OBJC_IVAR_$_CMITextureStylesTextureCopy._context
+ _OBJC_IVAR_$_CMITextureStylesTextureCopy._shaders
+ _OBJC_IVAR_$_CMITextureStylesTextureWarping._context
+ _OBJC_IVAR_$_CMITextureStylesTextureWarping._shaders
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._cameraInfoByPortType
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._context
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._downSampler
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._filterer
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._fullImageSize
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._inputOutput
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._instanceID
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._parameters
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._perPersonData
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._personData
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._regionToRender
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._shaders
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._skipRendering
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._statsBuffers
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._textureCopier
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._tuningParameters
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrighten._warper
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._brightnessValue
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._inputEarMask
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._inputFaceMask
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._inputGlassesMask
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._inputHairMask
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._inputImage
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._inputInstanceMask
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._inputLipMask
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._inputNoseMask
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._inputTattooMask
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._outputImage
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenIO._outputPersonStats
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._averageColorMix
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._bimodalVarianceFalloff
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._blendConditionFilterScale
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._brightnessMix
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._colorBlendFilterScale
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._dominantYawTapering
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._hueMaskFilterScale
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._maskThreshold
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._maxDarknessTrigger
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._maxFaceFrac
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._maxHueTolerance
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._maximumBimodalVariance
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._maximumUnimodalVariance
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._minDarknessTrigger
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._minFaceFrac
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._minHueTolerance
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._minTextureAddBack
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._nightMode
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._nightModeSharpness
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._regionMaskThreshold
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._textureAddBackFilterScale
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._textureAddBackScale
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._unimodalVarianceFalloff
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._yawFallOff
+ _OBJC_IVAR_$_CMITextureStylesUnderEyeBrightenParameters._yawOffset
+ _OBJC_IVAR_$_CMITiledInferenceProcessorConfig._bufferCountDualANE
+ _OBJC_METACLASS_$_CMILCBDatabase
+ _OBJC_METACLASS_$_CMILCBEntry
+ _OBJC_METACLASS_$_CMITSMattifyPerPersonIntermediatesAndStats
+ _OBJC_METACLASS_$_CMITSTextureAndFullImageRegion
+ _OBJC_METACLASS_$_CMITSUEBPerPersonData
+ _OBJC_METACLASS_$_CMITextureStyle
+ _OBJC_METACLASS_$_CMITextureStyleTuningLookup
+ _OBJC_METACLASS_$_CMITextureStylesBloom
+ _OBJC_METACLASS_$_CMITextureStylesBloomIO
+ _OBJC_METACLASS_$_CMITextureStylesBloomParameters
+ _OBJC_METACLASS_$_CMITextureStylesDiffusion
+ _OBJC_METACLASS_$_CMITextureStylesDiffusionIO
+ _OBJC_METACLASS_$_CMITextureStylesDiffusionParameters
+ _OBJC_METACLASS_$_CMITextureStylesDownSampler
+ _OBJC_METACLASS_$_CMITextureStylesEffectDescriptor
+ _OBJC_METACLASS_$_CMITextureStylesFaceLandmark
+ _OBJC_METACLASS_$_CMITextureStylesFastGaussian
+ _OBJC_METACLASS_$_CMITextureStylesFilmGrainIO
+ _OBJC_METACLASS_$_CMITextureStylesFilmGrainParameters
+ _OBJC_METACLASS_$_CMITextureStylesFilmGrainProcessorV1
+ _OBJC_METACLASS_$_CMITextureStylesFilter
+ _OBJC_METACLASS_$_CMITextureStylesGaussianFilter
+ _OBJC_METACLASS_$_CMITextureStylesGaussianGuidedFilterV3
+ _OBJC_METACLASS_$_CMITextureStylesGlow
+ _OBJC_METACLASS_$_CMITextureStylesGlowIO
+ _OBJC_METACLASS_$_CMITextureStylesGlowParameters
+ _OBJC_METACLASS_$_CMITextureStylesGuidedFilter
+ _OBJC_METACLASS_$_CMITextureStylesHalation
+ _OBJC_METACLASS_$_CMITextureStylesHalationIO
+ _OBJC_METACLASS_$_CMITextureStylesHalationParameters
+ _OBJC_METACLASS_$_CMITextureStylesMattify
+ _OBJC_METACLASS_$_CMITextureStylesMattifyIO
+ _OBJC_METACLASS_$_CMITextureStylesMattifyParameters
+ _OBJC_METACLASS_$_CMITextureStylesPersonInputData
+ _OBJC_METACLASS_$_CMITextureStylesPersonInputDataUtilities
+ _OBJC_METACLASS_$_CMITextureStylesProcessor
+ _OBJC_METACLASS_$_CMITextureStylesPyramid
+ _OBJC_METACLASS_$_CMITextureStylesPyramidFactory
+ _OBJC_METACLASS_$_CMITextureStylesSkinSmoothIO
+ _OBJC_METACLASS_$_CMITextureStylesSkinSmoothParameters
+ _OBJC_METACLASS_$_CMITextureStylesSkinSmoothStandalone
+ _OBJC_METACLASS_$_CMITextureStylesTextureCopy
+ _OBJC_METACLASS_$_CMITextureStylesTextureWarping
+ _OBJC_METACLASS_$_CMITextureStylesUnderEyeBrighten
+ _OBJC_METACLASS_$_CMITextureStylesUnderEyeBrightenIO
+ _OBJC_METACLASS_$_CMITextureStylesUnderEyeBrightenParameters
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_101
+ _OUTLINED_FUNCTION_102
+ _OUTLINED_FUNCTION_103
+ _OUTLINED_FUNCTION_104
+ _OUTLINED_FUNCTION_105
+ _OUTLINED_FUNCTION_106
+ _OUTLINED_FUNCTION_107
+ _OUTLINED_FUNCTION_108
+ _OUTLINED_FUNCTION_109
+ _OUTLINED_FUNCTION_110
+ _OUTLINED_FUNCTION_111
+ _OUTLINED_FUNCTION_112
+ _OUTLINED_FUNCTION_113
+ _OUTLINED_FUNCTION_114
+ _OUTLINED_FUNCTION_115
+ _OUTLINED_FUNCTION_116
+ _OUTLINED_FUNCTION_117
+ _OUTLINED_FUNCTION_118
+ _OUTLINED_FUNCTION_119
+ _OUTLINED_FUNCTION_120
+ _OUTLINED_FUNCTION_121
+ _OUTLINED_FUNCTION_122
+ _OUTLINED_FUNCTION_123
+ _OUTLINED_FUNCTION_124
+ _OUTLINED_FUNCTION_33
+ _OUTLINED_FUNCTION_34
+ _OUTLINED_FUNCTION_35
+ _OUTLINED_FUNCTION_36
+ _OUTLINED_FUNCTION_37
+ _OUTLINED_FUNCTION_38
+ _OUTLINED_FUNCTION_39
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ _OUTLINED_FUNCTION_44
+ _OUTLINED_FUNCTION_45
+ _OUTLINED_FUNCTION_46
+ _OUTLINED_FUNCTION_47
+ _OUTLINED_FUNCTION_48
+ _OUTLINED_FUNCTION_49
+ _OUTLINED_FUNCTION_50
+ _OUTLINED_FUNCTION_51
+ _OUTLINED_FUNCTION_52
+ _OUTLINED_FUNCTION_53
+ _OUTLINED_FUNCTION_54
+ _OUTLINED_FUNCTION_55
+ _OUTLINED_FUNCTION_56
+ _OUTLINED_FUNCTION_57
+ _OUTLINED_FUNCTION_58
+ _OUTLINED_FUNCTION_59
+ _OUTLINED_FUNCTION_60
+ _OUTLINED_FUNCTION_61
+ _OUTLINED_FUNCTION_62
+ _OUTLINED_FUNCTION_63
+ _OUTLINED_FUNCTION_64
+ _OUTLINED_FUNCTION_65
+ _OUTLINED_FUNCTION_66
+ _OUTLINED_FUNCTION_67
+ _OUTLINED_FUNCTION_68
+ _OUTLINED_FUNCTION_69
+ _OUTLINED_FUNCTION_70
+ _OUTLINED_FUNCTION_71
+ _OUTLINED_FUNCTION_72
+ _OUTLINED_FUNCTION_73
+ _OUTLINED_FUNCTION_74
+ _OUTLINED_FUNCTION_75
+ _OUTLINED_FUNCTION_76
+ _OUTLINED_FUNCTION_77
+ _OUTLINED_FUNCTION_79
+ _OUTLINED_FUNCTION_80
+ _OUTLINED_FUNCTION_81
+ _OUTLINED_FUNCTION_82
+ _OUTLINED_FUNCTION_83
+ _OUTLINED_FUNCTION_84
+ _OUTLINED_FUNCTION_85
+ _OUTLINED_FUNCTION_86
+ _OUTLINED_FUNCTION_87
+ _OUTLINED_FUNCTION_88
+ _OUTLINED_FUNCTION_89
+ _OUTLINED_FUNCTION_90
+ _OUTLINED_FUNCTION_91
+ _OUTLINED_FUNCTION_92
+ _OUTLINED_FUNCTION_93
+ _OUTLINED_FUNCTION_94
+ _OUTLINED_FUNCTION_95
+ _OUTLINED_FUNCTION_96
+ _OUTLINED_FUNCTION_97
+ _OUTLINED_FUNCTION_98
+ _OUTLINED_FUNCTION_99
+ _SKINSMOOTH_CONFIGURATION_NOTE_VARIABLE
+ __MergedGlobals
+ __OBJC_$_CLASS_METHODS_CMILCBDatabase
+ __OBJC_$_CLASS_METHODS_CMILCBEntry
+ __OBJC_$_CLASS_METHODS_CMITextureStyle
+ __OBJC_$_CLASS_METHODS_CMITextureStyleTuningLookup
+ __OBJC_$_CLASS_METHODS_CMITextureStylesBloom
+ __OBJC_$_CLASS_METHODS_CMITextureStylesDiffusion
+ __OBJC_$_CLASS_METHODS_CMITextureStylesFaceLandmark
+ __OBJC_$_CLASS_METHODS_CMITextureStylesFastGaussian
+ __OBJC_$_CLASS_METHODS_CMITextureStylesFilmGrainProcessorV1
+ __OBJC_$_CLASS_METHODS_CMITextureStylesFilter
+ __OBJC_$_CLASS_METHODS_CMITextureStylesGaussianGuidedFilterV3
+ __OBJC_$_CLASS_METHODS_CMITextureStylesGlow
+ __OBJC_$_CLASS_METHODS_CMITextureStylesGuidedFilter
+ __OBJC_$_CLASS_METHODS_CMITextureStylesHalation
+ __OBJC_$_CLASS_METHODS_CMITextureStylesMattify
+ __OBJC_$_CLASS_METHODS_CMITextureStylesPersonInputData
+ __OBJC_$_CLASS_METHODS_CMITextureStylesPersonInputDataUtilities
+ __OBJC_$_CLASS_METHODS_CMITextureStylesProcessor
+ __OBJC_$_CLASS_METHODS_CMITextureStylesSkinSmoothStandalone
+ __OBJC_$_CLASS_METHODS_CMITextureStylesUnderEyeBrighten
+ __OBJC_$_CLASS_PROP_LIST_CMILCBDatabase
+ __OBJC_$_CLASS_PROP_LIST_CMILCBEntry
+ __OBJC_$_CLASS_PROP_LIST_CMITextureStylesGuidedFilter
+ __OBJC_$_CLASS_PROP_LIST_CMITextureStylesProcessor
+ __OBJC_$_INSTANCE_METHODS_CMILCBDatabase
+ __OBJC_$_INSTANCE_METHODS_CMILCBEntry
+ __OBJC_$_INSTANCE_METHODS_CMITSMattifyPerPersonIntermediatesAndStats
+ __OBJC_$_INSTANCE_METHODS_CMITSTextureAndFullImageRegion
+ __OBJC_$_INSTANCE_METHODS_CMITSUEBPerPersonData
+ __OBJC_$_INSTANCE_METHODS_CMITextureStyle
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesBloom
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesBloomIO
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesBloomParameters
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesDiffusion
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesDiffusionIO
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesDiffusionParameters
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesDownSampler
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesEffectDescriptor
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesFaceLandmark
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesFastGaussian
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesFilmGrainIO
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesFilmGrainParameters
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesFilmGrainProcessorV1
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesFilter
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesGaussianFilter
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesGaussianGuidedFilterV3
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesGlow
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesGlowIO
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesGlowParameters
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesGuidedFilter
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesHalation
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesHalationIO
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesHalationParameters
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesMattify
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesMattifyIO
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesMattifyParameters
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesPersonInputData
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesProcessor
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesPyramid
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesPyramidFactory
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesSkinSmoothIO
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesSkinSmoothParameters
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesSkinSmoothStandalone
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesTextureCopy
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesTextureWarping
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesUnderEyeBrighten
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesUnderEyeBrightenIO
+ __OBJC_$_INSTANCE_METHODS_CMITextureStylesUnderEyeBrightenParameters
+ __OBJC_$_INSTANCE_METHODS_NSArray(GainValueLookup|Getters|Comprehension|CMILCB)
+ __OBJC_$_INSTANCE_VARIABLES_CMILCBDatabase
+ __OBJC_$_INSTANCE_VARIABLES_CMILCBEntry
+ __OBJC_$_INSTANCE_VARIABLES_CMITSMattifyPerPersonIntermediatesAndStats
+ __OBJC_$_INSTANCE_VARIABLES_CMITSTextureAndFullImageRegion
+ __OBJC_$_INSTANCE_VARIABLES_CMITSUEBPerPersonData
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStyle
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesBloom
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesBloomIO
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesBloomParameters
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesDiffusion
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesDiffusionIO
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesDiffusionParameters
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesDownSampler
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesEffectDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesFaceLandmark
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesFastGaussian
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesFilmGrainIO
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesFilmGrainParameters
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesFilmGrainProcessorV1
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesFilter
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesGaussianFilter
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesGaussianGuidedFilterV3
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesGlow
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesGlowIO
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesGlowParameters
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesGuidedFilter
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesHalation
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesHalationIO
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesHalationParameters
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesMattify
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesMattifyIO
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesMattifyParameters
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesPersonInputData
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesProcessor
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesPyramid
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesPyramidFactory
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesSkinSmoothIO
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesSkinSmoothParameters
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesSkinSmoothStandalone
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesTextureCopy
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesTextureWarping
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesUnderEyeBrighten
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesUnderEyeBrightenIO
+ __OBJC_$_INSTANCE_VARIABLES_CMITextureStylesUnderEyeBrightenParameters
+ __OBJC_$_PROP_LIST_CMILCBDatabase
+ __OBJC_$_PROP_LIST_CMILCBEntry
+ __OBJC_$_PROP_LIST_CMITSTextureAndFullImageRegion
+ __OBJC_$_PROP_LIST_CMITextureStyle
+ __OBJC_$_PROP_LIST_CMITextureStylesBloom
+ __OBJC_$_PROP_LIST_CMITextureStylesBloomIO
+ __OBJC_$_PROP_LIST_CMITextureStylesBloomParameters
+ __OBJC_$_PROP_LIST_CMITextureStylesDiffusion
+ __OBJC_$_PROP_LIST_CMITextureStylesDiffusionIO
+ __OBJC_$_PROP_LIST_CMITextureStylesDiffusionParameters
+ __OBJC_$_PROP_LIST_CMITextureStylesEffectDescriptor
+ __OBJC_$_PROP_LIST_CMITextureStylesEffectRenderer
+ __OBJC_$_PROP_LIST_CMITextureStylesFaceLandmark
+ __OBJC_$_PROP_LIST_CMITextureStylesFilmGrainIO
+ __OBJC_$_PROP_LIST_CMITextureStylesFilmGrainParameters
+ __OBJC_$_PROP_LIST_CMITextureStylesFilmGrainProcessorV1
+ __OBJC_$_PROP_LIST_CMITextureStylesGlow
+ __OBJC_$_PROP_LIST_CMITextureStylesGlowIO
+ __OBJC_$_PROP_LIST_CMITextureStylesGlowParameters
+ __OBJC_$_PROP_LIST_CMITextureStylesHalation
+ __OBJC_$_PROP_LIST_CMITextureStylesHalationIO
+ __OBJC_$_PROP_LIST_CMITextureStylesHalationParameters
+ __OBJC_$_PROP_LIST_CMITextureStylesMattify
+ __OBJC_$_PROP_LIST_CMITextureStylesMattifyIO
+ __OBJC_$_PROP_LIST_CMITextureStylesMattifyParameters
+ __OBJC_$_PROP_LIST_CMITextureStylesPersonInputData
+ __OBJC_$_PROP_LIST_CMITextureStylesProcessor
+ __OBJC_$_PROP_LIST_CMITextureStylesPyramid
+ __OBJC_$_PROP_LIST_CMITextureStylesSkinSmoothIO
+ __OBJC_$_PROP_LIST_CMITextureStylesSkinSmoothParameters
+ __OBJC_$_PROP_LIST_CMITextureStylesSkinSmoothStandalone
+ __OBJC_$_PROP_LIST_CMITextureStylesUnderEyeBrighten
+ __OBJC_$_PROP_LIST_CMITextureStylesUnderEyeBrightenIO
+ __OBJC_$_PROP_LIST_CMITextureStylesUnderEyeBrightenParameters
+ __OBJC_$_PROP_LIST_CMITileable
+ __OBJC_$_PROTOCOL_CLASS_METHODS_OPT_CMITextureStylesEffectRenderer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CMITextureStylesEffectParameters
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CMITextureStylesEffectRenderer
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CMITileable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CMITextureStylesEffectParameters
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CMITextureStylesEffectRenderer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CMITextureStylesEffectParameters
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CMITextureStylesEffectRenderer
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CMITileable
+ __OBJC_$_PROTOCOL_REFS_CMITextureStylesEffectInputOutput
+ __OBJC_$_PROTOCOL_REFS_CMITextureStylesEffectParameters
+ __OBJC_$_PROTOCOL_REFS_CMITextureStylesEffectRenderer
+ __OBJC_$_PROTOCOL_REFS_CMITextureStylesFilmGrainProcessor
+ __OBJC_$_PROTOCOL_REFS_CMITileable
+ __OBJC_CLASS_PROTOCOLS_$_CMILCBDatabase
+ __OBJC_CLASS_PROTOCOLS_$_CMILCBEntry
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesBloom
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesBloomIO
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesBloomParameters
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesDiffusion
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesDiffusionIO
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesDiffusionParameters
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesEffectDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesFaceLandmark
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesFilmGrainIO
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesFilmGrainParameters
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesFilmGrainProcessorV1
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesGlow
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesGlowIO
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesGlowParameters
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesHalation
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesHalationIO
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesHalationParameters
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesMattify
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesMattifyIO
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesMattifyParameters
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesPersonInputData
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesProcessor
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesSkinSmoothIO
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesSkinSmoothParameters
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesSkinSmoothStandalone
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesUnderEyeBrighten
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesUnderEyeBrightenIO
+ __OBJC_CLASS_PROTOCOLS_$_CMITextureStylesUnderEyeBrightenParameters
+ __OBJC_CLASS_RO_$_CMILCBDatabase
+ __OBJC_CLASS_RO_$_CMILCBEntry
+ __OBJC_CLASS_RO_$_CMITSMattifyPerPersonIntermediatesAndStats
+ __OBJC_CLASS_RO_$_CMITSTextureAndFullImageRegion
+ __OBJC_CLASS_RO_$_CMITSUEBPerPersonData
+ __OBJC_CLASS_RO_$_CMITextureStyle
+ __OBJC_CLASS_RO_$_CMITextureStyleTuningLookup
+ __OBJC_CLASS_RO_$_CMITextureStylesBloom
+ __OBJC_CLASS_RO_$_CMITextureStylesBloomIO
+ __OBJC_CLASS_RO_$_CMITextureStylesBloomParameters
+ __OBJC_CLASS_RO_$_CMITextureStylesDiffusion
+ __OBJC_CLASS_RO_$_CMITextureStylesDiffusionIO
+ __OBJC_CLASS_RO_$_CMITextureStylesDiffusionParameters
+ __OBJC_CLASS_RO_$_CMITextureStylesDownSampler
+ __OBJC_CLASS_RO_$_CMITextureStylesEffectDescriptor
+ __OBJC_CLASS_RO_$_CMITextureStylesFaceLandmark
+ __OBJC_CLASS_RO_$_CMITextureStylesFastGaussian
+ __OBJC_CLASS_RO_$_CMITextureStylesFilmGrainIO
+ __OBJC_CLASS_RO_$_CMITextureStylesFilmGrainParameters
+ __OBJC_CLASS_RO_$_CMITextureStylesFilmGrainProcessorV1
+ __OBJC_CLASS_RO_$_CMITextureStylesFilter
+ __OBJC_CLASS_RO_$_CMITextureStylesGaussianFilter
+ __OBJC_CLASS_RO_$_CMITextureStylesGaussianGuidedFilterV3
+ __OBJC_CLASS_RO_$_CMITextureStylesGlow
+ __OBJC_CLASS_RO_$_CMITextureStylesGlowIO
+ __OBJC_CLASS_RO_$_CMITextureStylesGlowParameters
+ __OBJC_CLASS_RO_$_CMITextureStylesGuidedFilter
+ __OBJC_CLASS_RO_$_CMITextureStylesHalation
+ __OBJC_CLASS_RO_$_CMITextureStylesHalationIO
+ __OBJC_CLASS_RO_$_CMITextureStylesHalationParameters
+ __OBJC_CLASS_RO_$_CMITextureStylesMattify
+ __OBJC_CLASS_RO_$_CMITextureStylesMattifyIO
+ __OBJC_CLASS_RO_$_CMITextureStylesMattifyParameters
+ __OBJC_CLASS_RO_$_CMITextureStylesPersonInputData
+ __OBJC_CLASS_RO_$_CMITextureStylesPersonInputDataUtilities
+ __OBJC_CLASS_RO_$_CMITextureStylesProcessor
+ __OBJC_CLASS_RO_$_CMITextureStylesPyramid
+ __OBJC_CLASS_RO_$_CMITextureStylesPyramidFactory
+ __OBJC_CLASS_RO_$_CMITextureStylesSkinSmoothIO
+ __OBJC_CLASS_RO_$_CMITextureStylesSkinSmoothParameters
+ __OBJC_CLASS_RO_$_CMITextureStylesSkinSmoothStandalone
+ __OBJC_CLASS_RO_$_CMITextureStylesTextureCopy
+ __OBJC_CLASS_RO_$_CMITextureStylesTextureWarping
+ __OBJC_CLASS_RO_$_CMITextureStylesUnderEyeBrighten
+ __OBJC_CLASS_RO_$_CMITextureStylesUnderEyeBrightenIO
+ __OBJC_CLASS_RO_$_CMITextureStylesUnderEyeBrightenParameters
+ __OBJC_LABEL_PROTOCOL_$_CMITextureStylesEffectInputOutput
+ __OBJC_LABEL_PROTOCOL_$_CMITextureStylesEffectParameters
+ __OBJC_LABEL_PROTOCOL_$_CMITextureStylesEffectRenderer
+ __OBJC_LABEL_PROTOCOL_$_CMITextureStylesFilmGrainProcessor
+ __OBJC_LABEL_PROTOCOL_$_CMITileable
+ __OBJC_METACLASS_RO_$_CMILCBDatabase
+ __OBJC_METACLASS_RO_$_CMILCBEntry
+ __OBJC_METACLASS_RO_$_CMITSMattifyPerPersonIntermediatesAndStats
+ __OBJC_METACLASS_RO_$_CMITSTextureAndFullImageRegion
+ __OBJC_METACLASS_RO_$_CMITSUEBPerPersonData
+ __OBJC_METACLASS_RO_$_CMITextureStyle
+ __OBJC_METACLASS_RO_$_CMITextureStyleTuningLookup
+ __OBJC_METACLASS_RO_$_CMITextureStylesBloom
+ __OBJC_METACLASS_RO_$_CMITextureStylesBloomIO
+ __OBJC_METACLASS_RO_$_CMITextureStylesBloomParameters
+ __OBJC_METACLASS_RO_$_CMITextureStylesDiffusion
+ __OBJC_METACLASS_RO_$_CMITextureStylesDiffusionIO
+ __OBJC_METACLASS_RO_$_CMITextureStylesDiffusionParameters
+ __OBJC_METACLASS_RO_$_CMITextureStylesDownSampler
+ __OBJC_METACLASS_RO_$_CMITextureStylesEffectDescriptor
+ __OBJC_METACLASS_RO_$_CMITextureStylesFaceLandmark
+ __OBJC_METACLASS_RO_$_CMITextureStylesFastGaussian
+ __OBJC_METACLASS_RO_$_CMITextureStylesFilmGrainIO
+ __OBJC_METACLASS_RO_$_CMITextureStylesFilmGrainParameters
+ __OBJC_METACLASS_RO_$_CMITextureStylesFilmGrainProcessorV1
+ __OBJC_METACLASS_RO_$_CMITextureStylesFilter
+ __OBJC_METACLASS_RO_$_CMITextureStylesGaussianFilter
+ __OBJC_METACLASS_RO_$_CMITextureStylesGaussianGuidedFilterV3
+ __OBJC_METACLASS_RO_$_CMITextureStylesGlow
+ __OBJC_METACLASS_RO_$_CMITextureStylesGlowIO
+ __OBJC_METACLASS_RO_$_CMITextureStylesGlowParameters
+ __OBJC_METACLASS_RO_$_CMITextureStylesGuidedFilter
+ __OBJC_METACLASS_RO_$_CMITextureStylesHalation
+ __OBJC_METACLASS_RO_$_CMITextureStylesHalationIO
+ __OBJC_METACLASS_RO_$_CMITextureStylesHalationParameters
+ __OBJC_METACLASS_RO_$_CMITextureStylesMattify
+ __OBJC_METACLASS_RO_$_CMITextureStylesMattifyIO
+ __OBJC_METACLASS_RO_$_CMITextureStylesMattifyParameters
+ __OBJC_METACLASS_RO_$_CMITextureStylesPersonInputData
+ __OBJC_METACLASS_RO_$_CMITextureStylesPersonInputDataUtilities
+ __OBJC_METACLASS_RO_$_CMITextureStylesProcessor
+ __OBJC_METACLASS_RO_$_CMITextureStylesPyramid
+ __OBJC_METACLASS_RO_$_CMITextureStylesPyramidFactory
+ __OBJC_METACLASS_RO_$_CMITextureStylesSkinSmoothIO
+ __OBJC_METACLASS_RO_$_CMITextureStylesSkinSmoothParameters
+ __OBJC_METACLASS_RO_$_CMITextureStylesSkinSmoothStandalone
+ __OBJC_METACLASS_RO_$_CMITextureStylesTextureCopy
+ __OBJC_METACLASS_RO_$_CMITextureStylesTextureWarping
+ __OBJC_METACLASS_RO_$_CMITextureStylesUnderEyeBrighten
+ __OBJC_METACLASS_RO_$_CMITextureStylesUnderEyeBrightenIO
+ __OBJC_METACLASS_RO_$_CMITextureStylesUnderEyeBrightenParameters
+ __OBJC_PROTOCOL_$_CMITextureStylesEffectInputOutput
+ __OBJC_PROTOCOL_$_CMITextureStylesEffectParameters
+ __OBJC_PROTOCOL_$_CMITextureStylesEffectRenderer
+ __OBJC_PROTOCOL_$_CMITextureStylesFilmGrainProcessor
+ __OBJC_PROTOCOL_$_CMITileable
+ __Z48CMITSsetImageBlockAlignedROIOnEncoderAndDispatchP30CMITSTextureAndFullImageRegion6CGRectPU34objcproto23MTLComputePipelineState11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectm
+ __Z48CMITSsetImageBlockAlignedROIOnEncoderAndDispatchP30CMITSTextureAndFullImageRegion6CGRectPU34objcproto23MTLComputePipelineState11objc_objectPU35objcproto24MTLComputeCommandEncoder11objc_objectmb
+ __ZL26tsf_findBestRadiusAndScale6CGSizefPi.onceToken
+ __ZL26tsf_findBestRadiusAndScale6CGSizefPi.sortedFilterRadii
+ __ZL26tsf_findBestRadiusAndScaleP7NSArrayIP8NSNumberEffPimm
+ ___123-[CMITextureStylesMattify _calculateExtendedFaceROI:leftCheekROI:rightCheekROI:triangleVerticesLeft:triangleVerticesRight:]_block_invoke
+ ___123-[CMITextureStylesMattify _calculateExtendedFaceROI:leftCheekROI:rightCheekROI:triangleVerticesLeft:triangleVerticesRight:]_block_invoke_2
+ ___161+[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]_block_invoke
+ ___161+[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]_block_invoke_2
+ ___161+[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]_block_invoke_3
+ ___161+[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]_block_invoke_4
+ ___161+[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]_block_invoke_5
+ ___161+[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]_block_invoke_6
+ ___161+[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]_block_invoke_7
+ ___161+[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]_block_invoke_8
+ ___161+[CMITextureStylesPersonInputDataUtilities personInputDataArrayFromLivePhotoMetadataAndStatsTracks:faceAttitudesMetadataTrack:effectsStatsTrack:effectsToRender:]_block_invoke_9
+ ___242-[CMITextureStylesMattify encodeDownsampledGaussianBlurWithCommandBuffer:inputImage:outputDownsampledAndBlurredImage:outputImage:downsampleFactor:downsampleSigma:stopAfterDownsample:cropAndDownsampleSkipLevelCount:cropAndDownsampleBoxFilter:]_block_invoke_2
+ ___31-[CMITextureStylesGlow process]_block_invoke
+ ___31-[CMITextureStylesGlow process]_block_invoke_2
+ ___32-[CMITextureStylesBloom process]_block_invoke
+ ___32-[CMITextureStylesBloom process]_block_invoke_2
+ ___34-[CMITextureStylesMattify process]_block_invoke
+ ___34-[CMITextureStylesMattify process]_block_invoke_2
+ ___34-[CMITextureStylesMattify process]_block_invoke_3
+ ___35-[CMITextureStylesHalation process]_block_invoke
+ ___35-[CMITextureStylesHalation process]_block_invoke_2
+ ___36-[CMITextureStylesDiffusion process]_block_invoke
+ ___36-[CMITextureStylesDiffusion process]_block_invoke_2
+ ___40-[CMITextureStylesMattify _processApply]_block_invoke_2
+ ___40-[CMITextureStylesMattify _processApply]_block_invoke_3
+ ___43-[CMITextureStylesUnderEyeBrighten process]_block_invoke
+ ___43-[CMITextureStylesUnderEyeBrighten process]_block_invoke_2
+ ___43-[CMITextureStylesUnderEyeBrighten process]_block_invoke_3
+ ___44-[CMILCBDatabase exportLCBsForCaptureStream]_block_invoke
+ ___44-[CMILCBDatabase exportLCBsForCaptureStream]_block_invoke_2
+ ___47-[CMITextureStylesFilmGrainProcessorV1 process]_block_invoke
+ ___47-[CMITextureStylesFilmGrainProcessorV1 process]_block_invoke_2
+ ___47-[CMITextureStylesSkinSmoothStandalone process]_block_invoke
+ ___47-[CMITextureStylesSkinSmoothStandalone process]_block_invoke_2
+ ___47-[CMITextureStylesSkinSmoothStandalone process]_block_invoke_3
+ ___55+[CMITextureStyleTuningLookup _loadTuningPlistIfNeeded]_block_invoke
+ ___62-[CMITextureStylesTextureWarping _shaderForOutputPixelFormat:]_block_invoke
+ ___63-[CMITextureStylesPersonInputData normalizeRelativeToCropRect:]_block_invoke
+ ___64+[CMITextureStyleTuningLookup defaultTextureStyleForPresetName:]_block_invoke
+ ___64-[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]_block_invoke
+ ___64-[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]_block_invoke_2
+ ___64-[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]_block_invoke_3
+ ___64-[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]_block_invoke_4
+ ___64-[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]_block_invoke_5
+ ___64-[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]_block_invoke_6
+ ___64-[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]_block_invoke_7
+ ___64-[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]_block_invoke_8
+ ___64-[CMITextureStylesProcessor _createEffectProcessorsAndUtilities]_block_invoke_9
+ ___67-[CMITextureStylesPersonInputData dictionaryRepresentationForKeys:]_block_invoke
+ ___68+[CMITextureStylesPersonInputData personDataFromDictionary:forKeys:]_block_invoke
+ ___72+[CMITextureStyleTuningLookup defaultTextureStyleForSmartStyleCastType:]_block_invoke
+ ___79+[CMISmartStyleUtilitiesV1 defaultStyleForCastType:smartStyleRenderingVersion:]_block_invoke
+ ___79+[CMISmartStyleUtilitiesV1 defaultStyleForCastType:smartStyleRenderingVersion:]_block_invoke_2
+ ___85+[CMITextureStylesPersonInputDataUtilities normalizePersonInputDataArray:toCropRect:]_block_invoke
+ ___88+[CMITextureStylesPersonInputDataUtilities sortPersonInputDataArrayByFaceSize:maxCount:]_block_invoke
+ ___94+[CMITextureStylesPersonInputDataUtilities convertUnitOfAngleInPersonInputDataArrayToDegrees:]_block_invoke
+ ___94+[CMITextureStylesPersonInputDataUtilities convertUnitOfAngleInPersonInputDataArrayToRadians:]_block_invoke
+ ___CMCaptureLibraryCore_block_invoke
+ ____ZL25tsp_denormalizePersonDataP7NSArrayIP28CMITextureStylesFaceLandmarkE6CGSize_block_invoke
+ ____ZL26tsf_findBestRadiusAndScale6CGSizefPi_block_invoke
+ ___allIOTextureKeys_block_invoke
+ ___block_descriptor_32_e15_B32?08Q16^B24l
+ ___block_descriptor_32_e25_B24?08"NSDictionary"16l
+ ___block_descriptor_32_e74_"CMITextureStylesPersonInputData"16?0"CMITextureStylesPersonInputData"8l
+ ___block_descriptor_32_e8_I12?0I8l
+ ___block_descriptor_32_e8_i16?0Q8l
+ ___block_descriptor_40_e8_32bs_e31_B40?0{CGSize=dd}8{CGSize=dd}24ls32l8
+ ___block_descriptor_40_e8_32bs_e41_"NSArray"32?0"NSArray"8"NSArray"16Q24ls32l8
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_40_e8_32s_e45_v32?0"CMITextureStylesFaceLandmark"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e48_v32?0"CMITextureStylesPersonInputData"8Q16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e8_B16?08ls32l8
+ ___block_descriptor_40_e8_32s_e8_i12?0i8ls32l8
+ ___block_descriptor_48_e68_"CMITextureStylesFaceLandmark"16?0"CMITextureStylesFaceLandmark"8l
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e29_v32?0"NSDictionary"8Q16^B24ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e29_v32?0"NSDictionary"8Q16^B24ls32l8
+ ___block_descriptor_56_e8_32s40r48r_e8_v16?08lr40l8r48l8s32l8
+ ___block_descriptor_64_e74_"CMITextureStylesPersonInputData"16?0"CMITextureStylesPersonInputData"8l
+ ___block_descriptor_64_e8_32s40r48r56w_e8_v16?08lr40l8r48l8s32l8w56l8
+ ___block_descriptor_72_e8_32s_e68_"CMITextureStylesFaceLandmark"16?0"CMITextureStylesFaceLandmark"8ls32l8
+ ___destructor_8_s0_s8_s24
+ ___getFigLivePhotoMetadataComputeDeserializationSizeSymbolLoc_block_invoke
+ ___getFigLivePhotoMetadataDeserializeIntoBufferSymbolLoc_block_invoke
+ ___mat_generateTrianglesAndComputeROI_block_invoke
+ ___mat_generateTrianglesAndComputeROI_block_invoke_2
+ ___sincosf_stret
+ ___ueb_generateTrianglesAndComputeROI_block_invoke
+ ___ueb_generateTrianglesAndComputeROI_block_invoke_2
+ __computeSkinMaskTransform
+ __hasStats
+ __loadDefaultUserBiasByCastType
+ __packStats
+ __sl_dlopen
+ _allIOTextureKeys
+ _allIOTextureKeys.keys
+ _allIOTextureKeys.onceToken
+ _audit_stringCMCapture
+ _defaultStyleForCastType:smartStyleRenderingVersion:.defaultUserBiasByCastTypeNoTextureStyles
+ _defaultStyleForCastType:smartStyleRenderingVersion:.defaultUserBiasByCastTypeWithTextureStyles
+ _defaultStyleForCastType:smartStyleRenderingVersion:.smartStyleOnceToken
+ _defaultStyleForCastType:smartStyleRenderingVersion:.textureStyleOnceToken
+ _defaultTextureStyleForPresetName:.onlyOnce
+ _defaultTextureStyleForPresetName:.presetDefaults
+ _defaultTextureStyleForSmartStyleCastType:.onlyOnce
+ _defaultTextureStyleForSmartStyleCastType:.rendererDefaults
+ _dispatch_group_async
+ _e5rt_precompiled_compute_op_create_options_set_anef_intermediate_buffer_size_hint
+ _fmod
+ _gCMILCBTrace
+ _gTextureStylesFilmGrainTrace
+ _gTextureStylesSkinSmoothTrace
+ _getFigLivePhotoMetadataComputeDeserializationSizeSymbolLoc.ptr
+ _getFigLivePhotoMetadataDeserializeIntoBufferSymbolLoc.ptr
+ _hypot
+ _kBloomParameterEntries
+ _kCMITextureStyleTuningBlendPreset_Key
+ _kCMITextureStyleTuningBlendThreshold_Key
+ _kCMITextureStyleTuningFilmGrainEffect_Key
+ _kCMITextureStyleTuningFilmGrainSeed_Key
+ _kCMITextureStyleTuningGrainSourcePreset_Key
+ _kCMITextureStylesMinFaceDiagonalRatio
+ _kCMITextureStylesPersonInputDataKey_faceAnglePitch
+ _kCMITextureStylesPersonInputDataKey_faceAngleRoll
+ _kCMITextureStylesPersonInputDataKey_faceAngleYaw
+ _kCMITextureStylesPersonInputDataKey_faceID
+ _kCMITextureStylesPersonInputDataKey_faceLandmarkType
+ _kCMITextureStylesPersonInputDataKey_faceLandmark_error
+ _kCMITextureStylesPersonInputDataKey_faceLandmark_point
+ _kCMITextureStylesPersonInputDataKey_faceLandmarks
+ _kCMITextureStylesPersonInputDataKey_faceROI
+ _kCMITextureStylesPersonInputDataKey_faceROIAndLandmarksROIRelativeScalingROI
+ _kCMITextureStylesPersonInputDataKey_faceSkinROI
+ _kCMITextureStylesPersonInputDataKey_faceUnitOfAngle
+ _kCMITextureStylesPersonInputDataKey_imageStats
+ _kCMITextureStylesPersonInputDataKey_instanceMaskReferenceKey
+ _kCMITextureStylesPersonInputDataKey_instanceROI
+ _kCMITextureStylesSoftGatingLowerBoundStreaming
+ _kCMITextureStylesSoftGatingUpperBoundStreaming
+ _kCMITextureStylesStatsKey_MattifyAverageFaceColor
+ _kCMITextureStylesStatsKey_MattifyFaceID
+ _kCMITextureStylesStatsKey_MattifyHighlightsToMaskRatio
+ _kCMITextureStylesStatsKey_MattifySkipPerson
+ _kCMITextureStylesStatsKey_SkinSmoothAverageFaceColour
+ _kCMITextureStylesStatsKey_SkinSmoothFaceID
+ _kCMITextureStylesStatsKey_SkinSmoothFaceRoughness
+ _kCMITextureStylesStatsKey_SkinSmoothSkipPerson
+ _kCMITextureStylesStatsKey_UEBFaceID
+ _kCMITextureStylesStatsKey_UEBLeftEyeAverageColor
+ _kCMITextureStylesStatsKey_UEBLeftEyeIsBiModal
+ _kCMITextureStylesStatsKey_UEBLeftEyeLumaVariance
+ _kCMITextureStylesStatsKey_UEBRightEyeAverageColor
+ _kCMITextureStylesStatsKey_UEBRightEyeIsBiModal
+ _kCMITextureStylesStatsKey_UEBRightEyeLumaVariance
+ _kCMITextureStylesStreamingMaxFaceCount
+ _kDiffusionParameterEntries
+ _kFaceLandmarkIndicies
+ _kFigCaptureStreamLCBEntryKey_ApertureRatio
+ _kFigCaptureStreamLCBEntryKey_CenterX
+ _kFigCaptureStreamLCBEntryKey_CenterY
+ _kFigCaptureStreamLCBEntryKey_CorrectionFeaturesBlue
+ _kFigCaptureStreamLCBEntryKey_CorrectionFeaturesGreen
+ _kFigCaptureStreamLCBEntryKey_CorrectionFeaturesRed
+ _kFigCaptureStreamLCBEntryKey_CorrectionFeaturesSpatialScalingFactor
+ _kFigCaptureStreamLCBEntryKey_DetectionConfidence
+ _kFigCaptureStreamLCBEntryKey_DetectionScore
+ _kFigCaptureStreamLCBEntryKey_DetectionSource
+ _kFigCaptureStreamLCBEntryKey_FocusPosition
+ _kFigCaptureStreamLCBEntryKey_OISShiftX
+ _kFigCaptureStreamLCBEntryKey_OISShiftY
+ _kFigCaptureStreamLCBEntryKey_PatchData
+ _kFigCaptureStreamLCBEntryKey_PatchHeight
+ _kFigCaptureStreamLCBEntryKey_PatchOriginX
+ _kFigCaptureStreamLCBEntryKey_PatchOriginY
+ _kFigCaptureStreamLCBEntryKey_PatchSpatialDownscalingFactor
+ _kFigCaptureStreamLCBEntryKey_PatchType
+ _kFigCaptureStreamLCBEntryKey_PatchWidth
+ _kFigCaptureStreamLCBEntryKey_Radius
+ _kFigCaptureStreamLCBEntryKey_Type
+ _kFigCaptureStreamLCBKey_DetectionIteration
+ _kFigCaptureStreamLCBKey_Entries
+ _kFigCaptureStreamLCBKey_MaximumGain
+ _kFigCaptureStreamLCBKey_MaximumOISStroke
+ _kFigCaptureStreamLCBKey_MinimumGain
+ _kFigCaptureStreamLCBKey_ModuleSerial
+ _kFigCaptureStreamLCBKey_SensorID
+ _kFigCaptureStreamLCBKey_Version
+ _kFigCaptureStreamMetadata_AngleInfoPitch
+ _kFigCaptureStreamMetadata_AngleInfoYaw
+ _kGlowParameterEntries
+ _kHalationParameterEntries
+ _kIOSurfaceAGXUseNearestChromaFiltering
+ _kLeftEyeLandmarkIndices
+ _kParameterEntries
+ _kRightEyeLandmarkIndices
+ _kSyntheticSkinTextureData
+ _kSyntheticSkinTextureSize
+ _ldexpf
+ _mat_generateTrianglesAndComputeROI
+ _mat_packStats
+ _objc_msgSend$_applyMeteorToInput:gainMap:gain:mixFactor:outputMixed:commandBuffer:
+ _objc_msgSend$_boolFromDict:key:default:
+ _objc_msgSend$_cacheKeyForHardwareModel:portType:captureMode:preset:captureType:
+ _objc_msgSend$_calculateBlurSigma:
+ _objc_msgSend$_calculateFullScaleBlurRadius:
+ _objc_msgSend$_computeAsymLumMaskWithInput:personMask:outputMask:halationParameters:brightnessValue:commandBuffer:
+ _objc_msgSend$_createGlobalToneCurveTextureFromGTCData:encoder:toneCurveTextureOut:
+ _objc_msgSend$_createIntermediateTextures:inputRegion:blurredSize:
+ _objc_msgSend$_createIntermediateTexturesWithInputRegion:firstBlurSize:secondBlurSize:
+ _objc_msgSend$_encodeGrainBlendWithInputImageUsingParams:commandBuffer:inputOutput:
+ _objc_msgSend$_floatFromDict:key:default:
+ _objc_msgSend$_gainBasedFloatFromDict:key:totalGain:default:
+ _objc_msgSend$_halationFinalRendererWithInput:halationMask:skinMask:personMask:output:parameters:commandBuffer:
+ _objc_msgSend$_interpolateFrom:to:t:
+ _objc_msgSend$_loadTuningPlist
+ _objc_msgSend$_loadTuningPlistIfNeeded
+ _objc_msgSend$_mergeTuningDictionary:forCaptureType:
+ _objc_msgSend$_normalizedCaptureTypeForPresetDict:requestedCaptureType:
+ _objc_msgSend$_releaseIntermediateTextures
+ _objc_msgSend$_renderDiffusionWithInput:blurred:skinMask:personMask:output:diffusionParameters:commandBuffer:
+ _objc_msgSend$_rescale:toLinearRGB:commandBuffer:
+ _objc_msgSend$_shaderForFilterRadius:
+ _objc_msgSend$_substractFg:bg:output:commandBuffer:
+ _objc_msgSend$_unsignedIntegerFromDict:key:default:
+ _objc_msgSend$_updateColorManagementForInputOutput:
+ _objc_msgSend$_updateColorManagementForInputTexture:outputImageTexture:
+ _objc_msgSend$_updateColorManagementForInputTexture:outputTexture:
+ _objc_msgSend$_validateInputsAndParameters
+ _objc_msgSend$allPersonDataForBlending
+ _objc_msgSend$amplitude
+ _objc_msgSend$amplitudeDecay
+ _objc_msgSend$aneCount
+ _objc_msgSend$apertureRatio
+ _objc_msgSend$averageColorMix
+ _objc_msgSend$backgroundStrength
+ _objc_msgSend$base64EncodedStringWithOptions:
+ _objc_msgSend$baselineExposure
+ _objc_msgSend$bg
+ _objc_msgSend$bimodalVarianceFalloff
+ _objc_msgSend$blendColorImageAverageColorMixFactor
+ _objc_msgSend$blendConditionFilterScale
+ _objc_msgSend$bodyMaskTextureAndFullImageRegion
+ _objc_msgSend$brightness
+ _objc_msgSend$brightnessMask
+ _objc_msgSend$brightnessMix
+ _objc_msgSend$brightnessValue
+ _objc_msgSend$bufferCountDualANE
+ _objc_msgSend$bundleWithIdentifier:
+ _objc_msgSend$bvHigh
+ _objc_msgSend$bvLow
+ _objc_msgSend$bvLowScale
+ _objc_msgSend$bvThresholdDeltaLowScale
+ _objc_msgSend$bw3Gamma
+ _objc_msgSend$calculateGaussianDimsWithWidth:height:sigma:nSamples:targetBlurRadius:pWorkWidth:pWorkHeight:pFinalSigma:pKernelRadius:fastMode:
+ _objc_msgSend$calculateGuidedFilterDimsWithFullImageWidth:fullImageHeight:sigma:blurRadius:pMediumResWidth:pMediumResHeight:pLowResWidth:pLowResHeight:pMediumToLow:pMediumSampling:pOutputBlurRadius:
+ _objc_msgSend$calculateIdealRadius:andDownSamplingScale:forImageSize:andTargetFullScaleRadius:
+ _objc_msgSend$calculateRadiusForSigma:
+ _objc_msgSend$calculateStats
+ _objc_msgSend$cmi_arrayByApplyingComprehension:
+ _objc_msgSend$colorBlendFilterScale
+ _objc_msgSend$computeAuxTextureRegionInCropSpaceWithAuxTextureSize:auxCropRect:fullImageSize:
+ _objc_msgSend$computeMinMaxCorrectionFeatureValues
+ _objc_msgSend$computeMinimumInputRegionInFullImageCoords:
+ _objc_msgSend$contrast
+ _objc_msgSend$contrastBoost
+ _objc_msgSend$contrastMask
+ _objc_msgSend$convertDegreesToRadians
+ _objc_msgSend$convertRadiansToDegrees
+ _objc_msgSend$convertUnitOfAngleInPersonInputDataArrayToRadians:
+ _objc_msgSend$copyFromInputTexture:withInputROI:toOutputTexture:withOutputROI:encodedTo:
+ _objc_msgSend$copyFromInputTexture:withInputROI:toOutputTexture:withOutputROI:enqueuedTo:
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$correctionFeatures
+ _objc_msgSend$createPyramidWithImage:maxLevels:encoder:
+ _objc_msgSend$createPyramidWithImage:maxLevels:pixelFormat:encoder:
+ _objc_msgSend$darkScale
+ _objc_msgSend$darknessDiffSmoothstepLowerBound
+ _objc_msgSend$darknessDiffSmoothstepUpperBound
+ _objc_msgSend$dataWithContentsOfURL:options:error:
+ _objc_msgSend$debugDescription
+ _objc_msgSend$decodeBoolForKey:
+ _objc_msgSend$decodeDictionaryWithKeysOfClass:objectsOfClass:forKey:
+ _objc_msgSend$decodeDoubleForKey:
+ _objc_msgSend$decodeFloatForKey:
+ _objc_msgSend$defaultStyleForCastType:smartStyleRenderingVersion:
+ _objc_msgSend$defocusRadius
+ _objc_msgSend$degrunge
+ _objc_msgSend$degrungeBody
+ _objc_msgSend$detailSize
+ _objc_msgSend$detectionCount
+ _objc_msgSend$dictOfZeroInitializedStats
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$dictionaryRepresentationForKeys:
+ _objc_msgSend$dictionaryRepresentationsFromFigLivePhotoMetadata:
+ _objc_msgSend$difSat
+ _objc_msgSend$diffuseColor
+ _objc_msgSend$dominantYawTapering
+ _objc_msgSend$downSampleInput:output:encoder:
+ _objc_msgSend$drawPrimitives:vertexStart:vertexCount:
+ _objc_msgSend$earsMaskTextureAndFullImageRegion
+ _objc_msgSend$editingStrength
+ _objc_msgSend$effectTypeToEffectName:
+ _objc_msgSend$effectTypeToZeroInitializedStats:
+ _objc_msgSend$enableTextureAddback
+ _objc_msgSend$encodeBool:forKey:
+ _objc_msgSend$encodeDouble:forKey:
+ _objc_msgSend$encodeFloat:forKey:
+ _objc_msgSend$encodeGaussianBlurWithCommandBuffer:input:output:kernel:kernelSize:
+ _objc_msgSend$encodeSIMDGaussianBlurWithCommandBuffer:input:output:radius:
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$externalFaceRoughnessStatsOutput
+ _objc_msgSend$externalLargeBlurGuidedFilterAOutput
+ _objc_msgSend$externalLargeBlurGuidedFilterBOutput
+ _objc_msgSend$externalMemoryResource
+ _objc_msgSend$externalSmallBlurOutput
+ _objc_msgSend$externalTextureAddbackOutput
+ _objc_msgSend$eyeProtection
+ _objc_msgSend$eyebrows
+ _objc_msgSend$eyebrowsMaskTextureAndFullImageRegion
+ _objc_msgSend$faceDiagonalRatioForFaceSize:imageSize:
+ _objc_msgSend$faceID
+ _objc_msgSend$faceLandmarkType
+ _objc_msgSend$faceLandmarks
+ _objc_msgSend$facePitch
+ _objc_msgSend$faceROI
+ _objc_msgSend$faceROIAndLandmarksROIRelativeScalingROI
+ _objc_msgSend$faceRoll
+ _objc_msgSend$faceSkinMaskTextureAndFullImageRegion
+ _objc_msgSend$faceSkinROI
+ _objc_msgSend$faceTempering
+ _objc_msgSend$faceYaw
+ _objc_msgSend$fastMode
+ _objc_msgSend$filteredArrayUsingPredicate:
+ _objc_msgSend$focusLensPosition
+ _objc_msgSend$fogStrength
+ _objc_msgSend$fracMaskHighlightsHeadroom
+ _objc_msgSend$fracMaskHighlightsNormFactor
+ _objc_msgSend$frequencyGap
+ _objc_msgSend$fullImageRegion
+ _objc_msgSend$gFContrast
+ _objc_msgSend$gFRadius
+ _objc_msgSend$gamma
+ _objc_msgSend$gammaMask
+ _objc_msgSend$gaussianBlurSigma
+ _objc_msgSend$gaussianFilterInput:output:radius:sigma:commandBuffer:
+ _objc_msgSend$gaussianFilterInput:output:radius:sigma:encoder:
+ _objc_msgSend$generateNewKeyFromConflictingKey:
+ _objc_msgSend$glassesMaskTextureAndFullImageRegion
+ _objc_msgSend$grading
+ _objc_msgSend$grain
+ _objc_msgSend$grainBlurRadius
+ _objc_msgSend$grainSelectivity
+ _objc_msgSend$hairClothes
+ _objc_msgSend$hairMaskTextureAndFullImageRegion
+ _objc_msgSend$hairTxFloor
+ _objc_msgSend$halationChroma
+ _objc_msgSend$halationHue
+ _objc_msgSend$handsAndEars
+ _objc_msgSend$handsMaskTextureAndFullImageRegion
+ _objc_msgSend$highlight
+ _objc_msgSend$highlightRetention
+ _objc_msgSend$hlBlurStrength
+ _objc_msgSend$hlTextureRestore
+ _objc_msgSend$hueDiffMeanTermSmoothstepLowerBound
+ _objc_msgSend$hueDiffMeanTermSmoothstepUpperBound
+ _objc_msgSend$hueDiffSmoothstepLowerBound
+ _objc_msgSend$hueDiffSmoothstepUpperBound
+ _objc_msgSend$hueMaskFilterScale
+ _objc_msgSend$hueMix
+ _objc_msgSend$hueRotate
+ _objc_msgSend$imageGuidedFilterEpsilon
+ _objc_msgSend$imageGuidedFilterRadius
+ _objc_msgSend$imageStats
+ _objc_msgSend$imageTextureFactor
+ _objc_msgSend$imageTextureThreshold
+ _objc_msgSend$indexesOfObjectsPassingTest:
+ _objc_msgSend$initStandardTextureStyle
+ _objc_msgSend$initWithArray:copyItems:
+ _objc_msgSend$initWithBase64EncodedString:options:
+ _objc_msgSend$initWithEntry:
+ _objc_msgSend$initWithImage:maxLevels:allocator:encoder:shader:
+ _objc_msgSend$initWithImage:maxLevels:pixelFormat:allocator:encoder:shader:
+ _objc_msgSend$initWithKey:position:radius:defocusRadius:particleDistance:apertureRatio:focusLensPosition:oisShift:opticalCenter:detectionCount:relativeToLens:lastDetectionGravityVector:lastDetectionTimeStamp:shouldCorrect:correctionFeatures:
+ _objc_msgSend$initWithOptionalMetalContext:
+ _objc_msgSend$initWithPoint:error:
+ _objc_msgSend$initWithPresetName:intensity:grain:
+ _objc_msgSend$initWithTuningDictionary:totalGain:
+ _objc_msgSend$initWithtype:parameters:
+ _objc_msgSend$inputEarMask
+ _objc_msgSend$inputFaceMask
+ _objc_msgSend$inputFaceRect
+ _objc_msgSend$inputGainMap
+ _objc_msgSend$inputGlassesMask
+ _objc_msgSend$inputHDRImage
+ _objc_msgSend$inputHairMask
+ _objc_msgSend$inputInnerKnot1
+ _objc_msgSend$inputInstanceMask
+ _objc_msgSend$inputLinearImage
+ _objc_msgSend$inputLinearMetadata
+ _objc_msgSend$inputLipMask
+ _objc_msgSend$inputLipsMask
+ _objc_msgSend$inputLowerCoeffA
+ _objc_msgSend$inputLowerCoeffB
+ _objc_msgSend$inputMask
+ _objc_msgSend$inputNoseMask
+ _objc_msgSend$inputOuterKnot1
+ _objc_msgSend$inputOutput
+ _objc_msgSend$inputPersonImage
+ _objc_msgSend$inputPersonMask
+ _objc_msgSend$inputSkinImage
+ _objc_msgSend$inputSkinMask
+ _objc_msgSend$inputSkinMaskAndFullImageRegion
+ _objc_msgSend$inputSkyImage
+ _objc_msgSend$inputSpread
+ _objc_msgSend$inputTattooMask
+ _objc_msgSend$inputTattoosMask
+ _objc_msgSend$inputThresholdDelta
+ _objc_msgSend$inputUpperCoeffA
+ _objc_msgSend$inputUpperCoeffB
+ _objc_msgSend$instanceMask
+ _objc_msgSend$instanceMaskTextureAndFullImageRegion
+ _objc_msgSend$instanceROI
+ _objc_msgSend$intensity
+ _objc_msgSend$key
+ _objc_msgSend$landmarkFromDictionary:
+ _objc_msgSend$largeBlurRadiusFaceDiagonalFactor
+ _objc_msgSend$lastDetectionGravityVector
+ _objc_msgSend$lastDetectionTimeStamp
+ _objc_msgSend$lift
+ _objc_msgSend$lightMapGamma
+ _objc_msgSend$lightMapInvert
+ _objc_msgSend$lightMapMax
+ _objc_msgSend$lightnessEditFactor
+ _objc_msgSend$lightnessEditHeadroom
+ _objc_msgSend$linearImageHighKey
+ _objc_msgSend$linearMixForBG
+ _objc_msgSend$linearMixForSkin
+ _objc_msgSend$lipContrast
+ _objc_msgSend$lipCrease
+ _objc_msgSend$lipHighlights
+ _objc_msgSend$lipNegClar
+ _objc_msgSend$lipsMaskTextureAndFullImageRegion
+ _objc_msgSend$maskBlurSigma
+ _objc_msgSend$maskThreshold
+ _objc_msgSend$maxCorrectionFeatureValue
+ _objc_msgSend$maxDarknessTrigger
+ _objc_msgSend$maxFaceFrac
+ _objc_msgSend$maxHueTolerance
+ _objc_msgSend$maxRGB
+ _objc_msgSend$maximumBimodalVariance
+ _objc_msgSend$maximumUnimodalVariance
+ _objc_msgSend$memoryResource
+ _objc_msgSend$metalCommandQueue
+ _objc_msgSend$metalShaderParamsFromDynamicParameters:brightnessValue:
+ _objc_msgSend$meteorHeadroom
+ _objc_msgSend$meteorHeadroomMixFactor
+ _objc_msgSend$minCorrectionFeatureValue
+ _objc_msgSend$minDarknessTrigger
+ _objc_msgSend$minFaceFrac
+ _objc_msgSend$minHueTolerance
+ _objc_msgSend$minTexture
+ _objc_msgSend$minTextureAddBack
+ _objc_msgSend$nLevels
+ _objc_msgSend$naturalResolution
+ _objc_msgSend$nightMode
+ _objc_msgSend$nightModeSharpness
+ _objc_msgSend$normalizeRelativeToCropRect:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$numberWithUnsignedShort:
+ _objc_msgSend$objectsAtIndexes:
+ _objc_msgSend$octaves
+ _objc_msgSend$oisShift
+ _objc_msgSend$opticalCenter
+ _objc_msgSend$outputPersonStats
+ _objc_msgSend$outputProcessedSkinMask
+ _objc_msgSend$parameters
+ _objc_msgSend$particleDistance
+ _objc_msgSend$person
+ _objc_msgSend$personDataFromDictionary:forKeys:
+ _objc_msgSend$personInputDataArrayFromDictionaryRepresentations:keys:
+ _objc_msgSend$personMaskTextureAndFullImageRegion
+ _objc_msgSend$personStrength
+ _objc_msgSend$plusGreenGuide
+ _objc_msgSend$point
+ _objc_msgSend$pores
+ _objc_msgSend$poresBody
+ _objc_msgSend$position
+ _objc_msgSend$predicateWithBlock:
+ _objc_msgSend$preserveColorfulness
+ _objc_msgSend$preserveColorfulnessMask
+ _objc_msgSend$preset
+ _objc_msgSend$processInput:output:triangleVertices:textureCoords:commandBuffer:
+ _objc_msgSend$processTexture:outputTexture:sigma:commandBuffer:fastMode:
+ _objc_msgSend$radius
+ _objc_msgSend$regionInFullImageCoords
+ _objc_msgSend$regionMaskThreshold
+ _objc_msgSend$relativeToLens
+ _objc_msgSend$renderPipelineStateForVertexFunction:vertexDescriptor:fragmentFunction:constants:colorAttachmentDescriptorArrray:
+ _objc_msgSend$rescaleInput:output:encoder:
+ _objc_msgSend$resetSkinSmoothState
+ _objc_msgSend$roughSamples
+ _objc_msgSend$saturation
+ _objc_msgSend$saturationFromSmartStyle
+ _objc_msgSend$saturationMask
+ _objc_msgSend$scaleParametersWithIntensity:
+ _objc_msgSend$seed
+ _objc_msgSend$setAllPersonDataForBlending:
+ _objc_msgSend$setAllocatorBackend:
+ _objc_msgSend$setBodyMaskTextureAndFullImageRegion:
+ _objc_msgSend$setBrightnessMix:
+ _objc_msgSend$setDefaults
+ _objc_msgSend$setDegrunge:
+ _objc_msgSend$setDegrungeBody:
+ _objc_msgSend$setEarsMaskTextureAndFullImageRegion:
+ _objc_msgSend$setEditingStrength:
+ _objc_msgSend$setEnableTextureAddback:
+ _objc_msgSend$setEnforceImmediateDealloc:
+ _objc_msgSend$setExternalFaceRoughnessStatsOutput:
+ _objc_msgSend$setExternalLargeBlurGuidedFilterAOutput:
+ _objc_msgSend$setExternalLargeBlurGuidedFilterBOutput:
+ _objc_msgSend$setExternalSmallBlurOutput:
+ _objc_msgSend$setExternalTextureAddbackOutput:
+ _objc_msgSend$setEyebrowsMaskTextureAndFullImageRegion:
+ _objc_msgSend$setFaceID:
+ _objc_msgSend$setFaceLandmarkType:
+ _objc_msgSend$setFaceLandmarks:
+ _objc_msgSend$setFacePitch:
+ _objc_msgSend$setFaceROI:
+ _objc_msgSend$setFaceRoll:
+ _objc_msgSend$setFaceSkinMaskTextureAndFullImageRegion:
+ _objc_msgSend$setFaceSkinROI:
+ _objc_msgSend$setFaceYaw:
+ _objc_msgSend$setFastMode:
+ _objc_msgSend$setFragmentTexture:atIndex:
+ _objc_msgSend$setFullImageRegion:
+ _objc_msgSend$setFullImageSize:
+ _objc_msgSend$setGlassesMaskTextureAndFullImageRegion:
+ _objc_msgSend$setHairClothes:
+ _objc_msgSend$setHairMaskTextureAndFullImageRegion:
+ _objc_msgSend$setHalationHue:
+ _objc_msgSend$setHandsMaskTextureAndFullImageRegion:
+ _objc_msgSend$setHlBlurStrength:
+ _objc_msgSend$setImageStats:
+ _objc_msgSend$setInputEarMask:
+ _objc_msgSend$setInputFaceMask:
+ _objc_msgSend$setInputFaceNormalizedRects:
+ _objc_msgSend$setInputFaceRect:
+ _objc_msgSend$setInputGainMap:
+ _objc_msgSend$setInputGlassesMask:
+ _objc_msgSend$setInputHDRImage:
+ _objc_msgSend$setInputHairMask:
+ _objc_msgSend$setInputInnerKnot0:
+ _objc_msgSend$setInputInstanceMask:
+ _objc_msgSend$setInputLinearImage:
+ _objc_msgSend$setInputLinearMetadata:
+ _objc_msgSend$setInputLipMask:
+ _objc_msgSend$setInputLipsMask:
+ _objc_msgSend$setInputLowerBound:
+ _objc_msgSend$setInputMask:
+ _objc_msgSend$setInputNoseMask:
+ _objc_msgSend$setInputOuterKnot0:
+ _objc_msgSend$setInputOutput:
+ _objc_msgSend$setInputPersonImage:
+ _objc_msgSend$setInputPersonMask:
+ _objc_msgSend$setInputSkinImage:
+ _objc_msgSend$setInputSkinMask:
+ _objc_msgSend$setInputSkinMaskAndFullImageRegion:
+ _objc_msgSend$setInputSkinMaskFlipHorizontal:
+ _objc_msgSend$setInputSkinMaskFlipVertical:
+ _objc_msgSend$setInputSkinMaskICR:
+ _objc_msgSend$setInputSkinMaskPCR:
+ _objc_msgSend$setInputSkinMaskRotationDegrees:
+ _objc_msgSend$setInputSkinSmoothingParameters:
+ _objc_msgSend$setInputSkyImage:
+ _objc_msgSend$setInputSpread:
+ _objc_msgSend$setInputTattooMask:
+ _objc_msgSend$setInputTattoosMask:
+ _objc_msgSend$setInputTextureROI:
+ _objc_msgSend$setInstanceID:
+ _objc_msgSend$setInstanceMask:
+ _objc_msgSend$setInstanceMaskReferenceKey:
+ _objc_msgSend$setInstanceMaskTextureAndFullImageRegion:
+ _objc_msgSend$setInstanceROI:
+ _objc_msgSend$setLinearImageHighKey:
+ _objc_msgSend$setLinearMixForBG:
+ _objc_msgSend$setLinearMixForSkin:
+ _objc_msgSend$setLipContrast:
+ _objc_msgSend$setLipNegClar:
+ _objc_msgSend$setLipsMaskTextureAndFullImageRegion:
+ _objc_msgSend$setLoadAction:
+ _objc_msgSend$setMaskBlurSigma:
+ _objc_msgSend$setMaxRGB:
+ _objc_msgSend$setMemoryResource:
+ _objc_msgSend$setMetalCommandQueue:
+ _objc_msgSend$setNightMode:
+ _objc_msgSend$setOutputPersonStats:
+ _objc_msgSend$setOutputProcessedSkinMask:
+ _objc_msgSend$setParameters:
+ _objc_msgSend$setPersonData:
+ _objc_msgSend$setPersonMaskTextureAndFullImageRegion:
+ _objc_msgSend$setPores:
+ _objc_msgSend$setPoresBody:
+ _objc_msgSend$setPreserveColorfulness:
+ _objc_msgSend$setPreserveColorfulnessMask:
+ _objc_msgSend$setRenderPipelineState:
+ _objc_msgSend$setRoughSamples:
+ _objc_msgSend$setSaturationFromSmartStyle:
+ _objc_msgSend$setSigmaGlare:
+ _objc_msgSend$setSkinMaskPurpose:
+ _objc_msgSend$setSkipRendering:
+ _objc_msgSend$setSoftLight:
+ _objc_msgSend$setStatistics:
+ _objc_msgSend$setStorageMode:
+ _objc_msgSend$setStoreAction:
+ _objc_msgSend$setStreamingMode:
+ _objc_msgSend$setStrength:
+ _objc_msgSend$setStrengthMask:
+ _objc_msgSend$setTattoosMaskTextureAndFullImageRegion:
+ _objc_msgSend$setTeethMaskTextureAndFullImageRegion:
+ _objc_msgSend$setTileSize:
+ _objc_msgSend$setTriangleFillMode:
+ _objc_msgSend$setUnitOfAngle:
+ _objc_msgSend$setUseStatistics:
+ _objc_msgSend$setValue:forKey:
+ _objc_msgSend$setVertexBytes:length:atIndex:
+ _objc_msgSend$setViewport:
+ _objc_msgSend$setWithArray:
+ _objc_msgSend$shDarken
+ _objc_msgSend$shadowLift
+ _objc_msgSend$shouldCorrect
+ _objc_msgSend$sigmaGlare
+ _objc_msgSend$skinMask
+ _objc_msgSend$skinStrength
+ _objc_msgSend$skipRendering
+ _objc_msgSend$skyStrength
+ _objc_msgSend$slBG
+ _objc_msgSend$slBright
+ _objc_msgSend$slDark
+ _objc_msgSend$slPerson
+ _objc_msgSend$slSkin
+ _objc_msgSend$smallBlurRadiusFaceDiagonalFactor
+ _objc_msgSend$softFadeGatingForFaceSize:imageSize:lowerBound:upperBound:
+ _objc_msgSend$softLight
+ _objc_msgSend$sortPersonInputDataArrayByFaceSize:maxCount:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$spbHL
+ _objc_msgSend$statistics
+ _objc_msgSend$strength
+ _objc_msgSend$strengthMask
+ _objc_msgSend$strongTextureProtect
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$supportsInPlaceRendering
+ _objc_msgSend$tattooSmoothing
+ _objc_msgSend$tattooWeight
+ _objc_msgSend$tattoosMaskTextureAndFullImageRegion
+ _objc_msgSend$teeth
+ _objc_msgSend$teethMaskTextureAndFullImageRegion
+ _objc_msgSend$textureAddBackFilterScale
+ _objc_msgSend$textureAddBackScale
+ _objc_msgSend$textureClamp
+ _objc_msgSend$textureDetectScale
+ _objc_msgSend$textureRestore
+ _objc_msgSend$textureRestoreScalingFactor
+ _objc_msgSend$textureRestoreSmoothstepLowerBound
+ _objc_msgSend$textureRestoreSmoothstepUpperBound
+ _objc_msgSend$textureRestoreStrengthFactor
+ _objc_msgSend$tuningDictionaryForHardwareModel:portType:captureMode:preset:captureType:
+ _objc_msgSend$unimodalVarianceFalloff
+ _objc_msgSend$unsignedLongValue
+ _objc_msgSend$useStatistics
+ _objc_msgSend$validate
+ _objc_msgSend$valueForKey:
+ _objc_msgSend$varTexture
+ _objc_msgSend$weightedGuidedFilterInput:guide:outputA:outputB:radius:sigma:epsilon:encoder:
+ _objc_msgSend$withDifferentKey
+ _objc_msgSend$yawFallOff
+ _objc_msgSend$yawOffset
+ _objc_msgSend$zoom
+ _objc_retain_x6
+ _sCacheLock
+ _sLoadOnceToken
+ _sMergedCache
+ _sReloadLock
+ _sTuningPlist
+ _ss_calculateBlurSigma
+ _ss_calculateBoundingBox
+ _ss_calculateEyeROI
+ _tc_defaultROI
+ _tc_defaultTextureROI
+ _ueb_generateTrianglesAndComputeROI
+ _ueb_getPaddedROIForFilterSigma
+ _ueb_packStats
- GCC_except_table91
- GCC_except_table94
- __OBJC_$_INSTANCE_METHODS_NSArray(GainValueLookup|Getters|Comprehension)
- ___52+[CMISmartStyleUtilitiesV1 defaultStyleForCastType:]_block_invoke
- _defaultStyleForCastType:.defaultUserBiasByCastType
- _defaultStyleForCastType:.onceToken
CStrings:
+ "\v"
+ "\f\xf0\xb1\""
+ "! CGRectIsEmpty( *boundingBoxOut )"
+ "! CGRectIsEmpty( *eyeROIOut )"
+ "! CGRectIsEmpty( _personData.faceROI )"
+ "! CGRectIsEmpty( allImageRectIntersections )"
+ "! CGRectIsEmpty( bounds )"
+ "! CGRectIsEmpty( eyeROI )"
+ "! CGRectIsEmpty( inputROI )"
+ "! CGRectIsEmpty( regionToRender )"
+ "! CGRectIsEmpty( roi )"
+ "! CGRectIsEmpty( roiData->regionToRender )"
+ "! CGRectIsNull( _personData.faceROI )"
+ "! CGRectIsNull( _regionToRender ) && ! CGRectIsEmpty( _regionToRender )"
+ "! CGRectIsNull( extendedFaceROI )"
+ "! CGRectIsNull( inputOutput.inputFaceRect )"
+ "! CGRectIsNull( intermediatesAndStats->_extendedFaceROI )"
+ "! CGRectIsNull( rect )"
+ "! __CGSizeEqualToSize( roiData->fullImageSize, CGSizeZero )"
+ "! _metalContext.allocator.usedSizeAll"
+ "%@:%@:%@:%@:%@"
+ "( ! CGRectIsNull( _personData.faceROI ) ) && ( ! CGRectIsEmpty( _personData.faceROI ) )"
+ "( ( personData.faceLandmarkType != CMITextureStylesFaceLandmarkType_Invalid ) && personData.faceLandmarks ) || ( personData.faceLandmarkType == CMITextureStylesFaceLandmarkType_Invalid )"
+ "( _streamingMode ) || ( ( _personData.faceLandmarks && ( _personData.faceLandmarkType != CMITextureStylesFaceLandmarkType_Invalid ) ) )"
+ "( _streamingMode ) || ( _personData.faceLandmarks && ( _personData.faceLandmarkType != CMITextureStylesFaceLandmarkType_Invalid ) && ( ! CGRectIsEmpty( _personData.faceROI ) ) && io.inputFaceMask.texture )"
+ "( _streamingMode ) || ( triangleVerticesLeft && triangleVerticesRight && ( ! CGRectIsNull( leftCheekROI ) ) && ( ! CGRectIsNull( rightCheekROI ) ) )"
+ "( blurInputTex.width == outputDownsampledAndBlurredImage.texture.width ) && ( blurInputTex.height == outputDownsampledAndBlurredImage.texture.height )"
+ "( dictionary && [dictionary isKindOfClass:[NSDictionary class]] )"
+ "( features.count >= 76 ) && ( landmarksType == CMITextureStylesFaceLandmarkType_Vision76 )"
+ "( outputDownsampledAndBlurredImage.texture.width == outputImage.texture.width ) && ( outputDownsampledAndBlurredImage.texture.height == outputImage.texture.height )"
+ "*heapBufferOut"
+ "*outputPtr"
+ "-[CMITextureStylesFastGaussian _createTexture:]"
+ "-[CMITextureStylesFastGaussian runOn:sigma:nSamples:targetBlurRadius:outTexture:commandBuffer:fastMode:]"
+ "-[CMITextureStylesGaussianGuidedFilterV3 _createTexture:]"
+ "-[CMITextureStylesGaussianGuidedFilterV3 runWithInput:skinMask:instanceMask:highlightRetention:sigma:eps:blurRadius:fullImageSize:fullImageOffset:outputTexture:commandBuffer:]"
+ "-[CMITextureStylesSkinSmoothStandalone _createTexture:label:]"
+ "-[CMITextureStylesSkinSmoothStandalone _createUncompressedTexture:label:]"
+ "-[CMITextureStylesUnderEyeBrighten calculateStats]"
+ "-[CMITextureStylesUnderEyeBrighten process]"
+ "0 == _outputPersonImageStats.count"
+ "1#"
+ "<%@: %p %@>"
+ "<%@: %p, effect type: %ld, configuration: %@>"
+ "<%@: %p, strength=%.2f, octaves=%u, saturation=%.2f>"
+ "<<<< CMILCB >>>>"
+ "<<<< CMILCB >>>> Fig"
+ "<<<< CMITIP >>>> %s: e5rt_execution_stream_set_ane_execution_priority failed to set E5RT_ANE_EXECUTION_PRIORITY_PRIORITY_6, %s."
+ "<<<< CMITIP >>>> %s: e5rt_precompiled_compute_op_create_options_set_anef_intermediate_buffer_size_hint failed to set 1x for kANEFClientIntermediateBufferSize %s, %s."
+ "<<<< CMITIP >>>> %s: e5rt_precompiled_compute_op_create_options_set_anef_intermediate_buffer_size_hint failed to set 2x for kANEFClientIntermediateBufferSize %s, %s."
+ "<<<< CMITextureStyles::Bloom >>>>"
+ "<<<< CMITextureStyles::Bloom >>>> Fig"
+ "<<<< CMITextureStyles::CMITextureStylesPersonInputData >>>> Fig"
+ "<<<< CMITextureStyles::Diffusion >>>>"
+ "<<<< CMITextureStyles::Diffusion >>>> Fig"
+ "<<<< CMITextureStyles::FastGaussian >>>>"
+ "<<<< CMITextureStyles::FastGaussian >>>> %s: %@ is nil"
+ "<<<< CMITextureStyles::FastGaussian >>>> %s: provided output texture doesn't meet requirements"
+ "<<<< CMITextureStyles::FastGaussian >>>> Fig"
+ "<<<< CMITextureStyles::FilmGrain >>>>"
+ "<<<< CMITextureStyles::FilmGrain >>>> Fig"
+ "<<<< CMITextureStyles::Glow >>>>"
+ "<<<< CMITextureStyles::Glow >>>> Fig"
+ "<<<< CMITextureStyles::GuidedFilterV3 >>>>"
+ "<<<< CMITextureStyles::GuidedFilterV3 >>>> %s: %@ is nil"
+ "<<<< CMITextureStyles::GuidedFilterV3 >>>> %s: Failed to calculate guided filter dimensions"
+ "<<<< CMITextureStyles::GuidedFilterV3 >>>> Fig"
+ "<<<< CMITextureStyles::Halation >>>>"
+ "<<<< CMITextureStyles::Halation >>>> Fig"
+ "<<<< CMITextureStyles::Mattify >>>>"
+ "<<<< CMITextureStyles::Mattify >>>> Fig"
+ "<<<< CMITextureStyles::MattifyStandaloneDynamicParameters >>>> Fig"
+ "<<<< CMITextureStyles::SkinSmoothStandalone >>>>"
+ "<<<< CMITextureStyles::SkinSmoothStandalone >>>> %s: %@ is nil"
+ "<<<< CMITextureStyles::SkinSmoothStandalone >>>> %s: chinIndex is greater than number of features"
+ "<<<< CMITextureStyles::SkinSmoothStandalone >>>> %s: chinPoint is not finite"
+ "<<<< CMITextureStyles::SkinSmoothStandalone >>>> %s: features are nil"
+ "<<<< CMITextureStyles::SkinSmoothStandalone >>>> %s: foreheadPoint is not finite"
+ "<<<< CMITextureStyles::SkinSmoothStandalone >>>> %s: noseTopIndex is greater than number of features"
+ "<<<< CMITextureStyles::SkinSmoothStandalone >>>> %s: point is not finite"
+ "<<<< CMITextureStyles::SkinSmoothStandalone >>>> Fig"
+ "<<<< CMITextureStyles::SkinSmoothStandaloneDynamicParameters >>>> Fig"
+ "<<<< CMITextureStyles::UEB >>>>"
+ "<<<< CMITextureStyles::UEB >>>> Fig"
+ "<<<< CMITextureStylesEffectDescriptor >>>>"
+ "<<<< CMITextureStylesEffectDescriptor >>>> Fig"
+ "<<<< TextureStylesProcessor >>>>"
+ "<<<< TextureStylesProcessor >>>> Fig"
+ "<<<< TextureStylesTuningLookup >>>> Fig"
+ "@\"CMITextureStylesFaceLandmark\"16@?0@\"CMITextureStylesFaceLandmark\"8"
+ "@\"CMITextureStylesPersonInputData\"16@?0@\"CMITextureStylesPersonInputData\"8"
+ "@\"NSArray\"32@?0@\"NSArray\"8@\"NSArray\"16Q24"
+ "@max.intValue"
+ "@min.intValue"
+ "A="
+ "AverageFaceColor"
+ "B16@?0@8"
+ "B24@?0@8@\"NSDictionary\"16"
+ "B32@?0@8Q16^B24"
+ "B40@?0{CGSize=dd}8{CGSize=dd}24"
+ "BlendPreset"
+ "BlendThreshold"
+ "Bloom"
+ "Bloom::GenerateBloom"
+ "CGRectContainsRect( CGRectMake( 0, 0, roiData->fullImageSize.width, roiData->fullImageSize.height ), roiData->regionToRender )"
+ "CGRectContainsRect( allImageRectIntersections, roiData->regionToRender )"
+ "CMILCBDatabase.m"
+ "CMILCBEntry.m"
+ "CMITS:SkinSmoothStandalone:DownScaledTex"
+ "CMITS:SkinSmoothStandalone:DownScaledTex2"
+ "CMITS:SkinSmoothStandalone:FaceDerived"
+ "CMITS:SkinSmoothStandalone:InternalProcessedMask"
+ "CMITS:SkinSmoothStandalone:PrecomputedMasks"
+ "CMITS:SkinSmoothStandalone:SmallBlurTex"
+ "CMITS:SkinSmoothStandalone:TABBlurredTex"
+ "CMITS:SkinSmoothStandalone:gfTexA"
+ "CMITS:SkinSmoothStandalone:gfTexB"
+ "CMITS:SkinSmoothStandalone:guideTex"
+ "CMITS:SkinSmoothStandalone:weightedTex"
+ "CMITextureStylesBloom.m"
+ "CMITextureStylesDiffusion.m"
+ "CMITextureStylesDownSampler.m"
+ "CMITextureStylesDownSampler::DownSample"
+ "CMITextureStylesDownSampler::Rescale"
+ "CMITextureStylesEffectDescriptor.m"
+ "CMITextureStylesFaceLandmarkType_Vision76 == featuresType"
+ "CMITextureStylesFastGaussian.m"
+ "CMITextureStylesFastGaussian::downsample_area_pow2"
+ "CMITextureStylesFastGaussian::downsample_nearest2d"
+ "CMITextureStylesFastGaussian::gaussian_h"
+ "CMITextureStylesFastGaussian::gaussian_v"
+ "CMITextureStylesFilmGrain::GrainBlend"
+ "CMITextureStylesFilmGrainProcessorV1.m"
+ "CMITextureStylesFilter.m"
+ "CMITextureStylesFilter::Gaussian"
+ "CMITextureStylesFilter::Guided"
+ "CMITextureStylesFilter::SelfGuided"
+ "CMITextureStylesFilter::WeightedGuided"
+ "CMITextureStylesGaussianFilter.m"
+ "CMITextureStylesGaussianFilter::GaussianBlur"
+ "CMITextureStylesGaussianFilter::GaussianBlur2dShared"
+ "CMITextureStylesGaussianFilter::GaussianBlurHorizontal"
+ "CMITextureStylesGaussianFilter::GaussianBlurVertical"
+ "CMITextureStylesGaussianFilter::SimdGaussianBlur"
+ "CMITextureStylesGaussianGuidedFilterV3.m"
+ "CMITextureStylesGaussianGuidedFilterV3::build_lr_from_full"
+ "CMITextureStylesGaussianGuidedFilterV3::guided_lr_2d"
+ "CMITextureStylesGaussianGuidedFilterV3::upsample_apply_to_mr"
+ "CMITextureStylesGeometry.m"
+ "CMITextureStylesGlow.m"
+ "CMITextureStylesGuidedFilter.m"
+ "CMITextureStylesGuidedFilter::ComputeGuided"
+ "CMITextureStylesHalation.m"
+ "CMITextureStylesMattify.m"
+ "CMITextureStylesMattify::ApplyRegionAddbackAndEditingStrength"
+ "CMITextureStylesMattify::BoxDownsample"
+ "CMITextureStylesMattify::CalculateAverageColor"
+ "CMITextureStylesMattify::CalculateBlendCondition"
+ "CMITextureStylesMattify::CalculateFracMaskHighlights"
+ "CMITextureStylesMattify::CalculateHistogramR"
+ "CMITextureStylesMattify::CalculateHistogramRGBA"
+ "CMITextureStylesMattify::CalculateQuantiles"
+ "CMITextureStylesMattify::CalculateValidMask"
+ "CMITextureStylesMattify::CopyStats"
+ "CMITextureStylesMattify::CreateExclusionMask"
+ "CMITextureStylesMattify::CropAndBoxDownsample"
+ "CMITextureStylesMattify::CropAndReSample"
+ "CMITextureStylesMattify::GenerateHistogramInputColorImage"
+ "CMITextureStylesMattify::GenerateMin3GrayHistogramInputImage"
+ "CMITextureStylesMattify::GenerateStrengthHistogramInputImages"
+ "CMITextureStylesMattify::ReSample"
+ "CMITextureStylesMattify::ScaleByValidMask"
+ "CMITextureStylesMattify::styleEngineThumbnailMode"
+ "CMITextureStylesMattifyParameters.m"
+ "CMITextureStylesMattify_process_%03d"
+ "CMITextureStylesPersonInputData.m"
+ "CMITextureStylesPersonInputDataUtilities.m"
+ "CMITextureStylesProcessor-FigMetalAllocator"
+ "CMITextureStylesProcessor-FigMetalAllocatorBackend"
+ "CMITextureStylesProcessor.m"
+ "CMITextureStylesPyramid.m"
+ "CMITextureStylesPyramid::DownSample"
+ "CMITextureStylesSkinSmoothParameters.m"
+ "CMITextureStylesSkinSmoothStandalone.m"
+ "CMITextureStylesSkinSmoothenStandalone::computeFaceRoughnessKernel"
+ "CMITextureStylesSkinSmoothenStandalone::computeTextureAmountKernel"
+ "CMITextureStylesSkinSmoothenStandalone::copyStatsKernel"
+ "CMITextureStylesSkinSmoothenStandalone::createWeightedAndGuideImages"
+ "CMITextureStylesSkinSmoothenStandalone::downSample"
+ "CMITextureStylesSkinSmoothenStandalone::finalBlendingKernel"
+ "CMITextureStylesSkinSmoothenStandalone::finalBlendingKernelInPlace"
+ "CMITextureStylesSkinSmoothenStandalone::multiPersonSkinMaskBlending"
+ "CMITextureStylesSkinSmoothenStandalone::packPrecomputedMasksKernel"
+ "CMITextureStylesTextureCopy.m"
+ "CMITextureStylesTextureCopy::Copy"
+ "CMITextureStylesTextureWarping.m"
+ "CMITextureStylesTextureWarping::FragmentWarp"
+ "CMITextureStylesTextureWarping::VertexWarp"
+ "CMITextureStylesTuningLookup.m"
+ "CMITextureStylesUnderEyeBrighten.m"
+ "CMITextureStylesUnderEyeBrighten::AverageColor"
+ "CMITextureStylesUnderEyeBrighten::Brighten"
+ "CMITextureStylesUnderEyeBrighten::CalculateLumaVarianceAndInferDistributionModality"
+ "CMITextureStylesUnderEyeBrighten::CalculateVarianceBasedStrengthTaper"
+ "CMITextureStylesUnderEyeBrighten::CopyStats"
+ "CMITextureStylesUnderEyeBrighten::CreateEyeMask"
+ "CMITextureStylesUnderEyeBrighten::CreateHueMask"
+ "CMITextureStylesUnderEyeBrighten::FinalMix"
+ "CMITextureStylesUnderEyeBrighten::SumColorAndFillLumaHistogram"
+ "CMImagingBundle"
+ "Cannot find CMImaging bundle."
+ "CaptureMode"
+ "CaptureType"
+ "CaptureTypeOverrides"
+ "CopyFromInputTexture"
+ "CopyFromIntermediateTexture"
+ "Could not allocate _inputRescaled"
+ "Could not allocate _meteorMixed"
+ "Could not allocate _outputBlurredImage"
+ "Could not allocate asymLumaMaskTexture"
+ "Could not allocate blurredSubtractMaskTexture"
+ "Could not allocate halationMaskTexture"
+ "Could not allocate inputRescaledTexture"
+ "Could not allocate meteorMixedTexture"
+ "Could not allocate outputBlurredImageTexture"
+ "Could not allocate subtractMaskTexture"
+ "Could not compile FillToneCurve"
+ "Could not compile GenerateBloom"
+ "Could not compile GenerateDiffusion"
+ "Could not compile GenerateGlow"
+ "Could not compile Halation"
+ "Could not compile applyMeteor"
+ "Could not compile lumAsymMask"
+ "Could not compile rescale420ToRBGA"
+ "Could not compile subtractBlendMode"
+ "Could not create intermediates"
+ "Could not create synthetic skin texture"
+ "Could not init CMITextureStylesBloom"
+ "Could not init CMITextureStylesBloom FigMetalContext"
+ "Could not init CMITextureStylesDiffusion"
+ "Could not init CMITextureStylesDiffusion FigMetalContext"
+ "Could not init CMITextureStylesGlow"
+ "Could not init CMITextureStylesGlow FigMetalContext"
+ "Could not init CMITextureStylesHalation"
+ "Could not init CMITextureStylesHalation FigMetalContext"
+ "Could not init CMITextureStylesSkinSmoothStandalone"
+ "Could not init CMITextureStylesSkinSmoothStandalone FigMetalContext"
+ "DC"
+ "Diffusion"
+ "Diffusion Parameters is nil"
+ "Diffusion::GenerateDiffusion"
+ "Diffusion::applyMeteor"
+ "Diffusion::rescale420ToRBGA"
+ "F10b"
+ "F10g"
+ "F10r"
+ "F3b"
+ "F3g"
+ "F3r"
+ "F4b"
+ "F4g"
+ "F4r"
+ "F5b"
+ "F5g"
+ "F5r"
+ "F6b"
+ "F6g"
+ "F6r"
+ "F7b"
+ "F7g"
+ "F7r"
+ "F8b"
+ "F8g"
+ "F8r"
+ "F9b"
+ "F9g"
+ "F9r"
+ "Failed to compile shaders"
+ "Failed to deserialize TextureStyleTuning.plist"
+ "Failed to read TextureStyleTuning.plist"
+ "Fast-Gaussian-Area2D"
+ "Fast-Gaussian-Area2D-Capping-Pixels"
+ "Fast-Gaussian-Horz"
+ "Fast-Gaussian-Nearest"
+ "Fast-Gaussian-Vert"
+ "FigLivePhotoMetadataComputeDeserializationSize"
+ "FigLivePhotoMetadataDeserializeIntoBuffer"
+ "FilmGrain"
+ "FilmGrainSeed"
+ "Filmic"
+ "GVx"
+ "GVy"
+ "GVz"
+ "Gaussian-GuidedFilterV3-BuildLrFromFull"
+ "Gaussian-GuidedFilterV3-GuidedLr2D"
+ "Gaussian-GuidedFilterV3-Upsample"
+ "GaussianGuidedV3-Alr"
+ "GaussianGuidedV3-Blr"
+ "GaussianGuidedV3-lrX"
+ "GaussianGuidedV3-lrY"
+ "GlobalGrainSourcePreset"
+ "Glow"
+ "Glow::FillToneCurve"
+ "Glow::GenerateGlow"
+ "Glowy"
+ "Grain"
+ "Halation"
+ "Halation::Halation"
+ "Halation::lumAsymMask"
+ "Halation::subtractBlendMode"
+ "HardwareModel"
+ "HighlightsToMaskRatio"
+ "I12@?0I8"
+ "Input dictA is nil"
+ "Input dictB is nil"
+ "Input linear texture is missing color management metadata"
+ "Input linear texture is nil"
+ "Input texture is missing color management metadata"
+ "Input texture is nil"
+ "Inputs are not valid"
+ "Intensity"
+ "K"
+ "LeftEyeAverageColor"
+ "LeftEyeIsBiModal"
+ "LeftEyeLumaVariance"
+ "LinearImageHighKey"
+ "Mattify"
+ "Missing metadataDict."
+ "OSStatus soft_FigLivePhotoMetadataComputeDeserializationSize(const void *, size_t, FigLivePhotoMetadataVersion, FigLivePhotoMetadataVersion * _Nullable, FigLivePhotoMetadataVersion *, size_t *)"
+ "OSStatus soft_FigLivePhotoMetadataDeserializeIntoBuffer(const void *, size_t, FigLivePhotoMetadataVersion, size_t, FigLivePhotoMetadata *)"
+ "OX"
+ "OY"
+ "OriginalRangeMax metadata is missing."
+ "OriginalRangeMin metadata is missing."
+ "Ouput texture is nil"
+ "Output texture is missing color management metadata"
+ "Output texture is nil"
+ "Ping Pong Image For Rendering"
+ "PortType"
+ "Preset"
+ "Px"
+ "Py"
+ "R2L"
+ "RendererTuningWithTextureStyles"
+ "RightEyeAverageColor"
+ "RightEyeIsBiModal"
+ "RightEyeLumaVariance"
+ "SkinSmooth-Compute-Texture-Amount"
+ "SkinSmooth-ComputeRoughness"
+ "SkinSmooth-CopyStats"
+ "SkinSmooth-DownScale"
+ "SkinSmooth-FinalBlending"
+ "SkinSmooth-FinalBlendingInPlace"
+ "SkinSmooth-LargeBlur"
+ "SkinSmooth-PackPrecomputedMasks"
+ "SkinSmooth-ProcessMask"
+ "SkinSmoothAverageFaceColour"
+ "SkinSmoothFaceRoughness"
+ "SkinSmoothSkipPerson"
+ "SkinSmoothingStandalone"
+ "SkipPerson"
+ "SmartStyleCastToTexturePresetMapping"
+ "SmartStyleToTextureStyleMapping"
+ "Soft"
+ "Studio"
+ "StyleEngine::SkinSmoothGuidedAvg"
+ "StyleEngine::SkinSmoothGuidedCoeff"
+ "Subject too small to process, skipping effect"
+ "TS"
+ "Texture"
+ "TextureStyleTuning"
+ "TextureStyleTuning.plist not found in CMImaging bundle."
+ "Threshold out of valid range (0, 1)"
+ "Unable to allocate a metal context"
+ "Unable to initialize CMITextureStylesFilmGrainProcessorV1"
+ "UnderEyeBrightening"
+ "[_inputOutput isKindOfClass:CMITextureStylesBloomIO.class]"
+ "[_inputOutput isKindOfClass:CMITextureStylesDiffusionIO.class]"
+ "[_inputOutput isKindOfClass:CMITextureStylesFilmGrainIO.class]"
+ "[_inputOutput isKindOfClass:CMITextureStylesGlowIO.class]"
+ "[_inputOutput isKindOfClass:CMITextureStylesHalationIO.class]"
+ "[_inputOutput isKindOfClass:CMITextureStylesMattifyIO.class]"
+ "[_inputOutput isKindOfClass:CMITextureStylesSkinSmoothIO.class]"
+ "[_inputOutput isKindOfClass:CMITextureStylesUnderEyeBrightenIO.class]"
+ "[_metalContext.allocator setupWithDescriptor:allocatorDesc allocatorBackend:memoryResource.allocatorBackend] == 0 "
+ "[_parameters isKindOfClass:CMITextureStylesBloomParameters.class]"
+ "[_parameters isKindOfClass:CMITextureStylesDiffusionParameters.class]"
+ "[_parameters isKindOfClass:CMITextureStylesFilmGrainParameters.class]"
+ "[_parameters isKindOfClass:CMITextureStylesGlowParameters.class]"
+ "[_parameters isKindOfClass:CMITextureStylesHalationParameters.class]"
+ "[_parameters isKindOfClass:CMITextureStylesSkinSmoothParameters.class]"
+ "[_parameters isKindOfClass:CMITextureStylesUnderEyeBrightenParameters.class]"
+ "[_parameters isKindOfClass:[CMITextureStylesMattifyParameters class]]"
+ "[_parameters validate] == 0 "
+ "[e isKindOfClass:CMILCBEntry.class]"
+ "[effect isKindOfClass:CMITextureStylesMattify.class]"
+ "[self _compileShaders] == 0 "
+ "__CGSizeEqualToSize( inputROI.size, outputROI.size )"
+ "_applyDiffusion"
+ "_applyHalation"
+ "_applyMeteor"
+ "_asymLumaMask"
+ "_blurProcessor"
+ "_blurredSubtractMask"
+ "_context"
+ "_downSampler"
+ "_entriesByKey"
+ "_fillToneCurvePipelineState"
+ "_filterer"
+ "_fullImageSize.width > 0 && _fullImageSize.height > 0"
+ "_generateBloomPipelineState"
+ "_generateGlowPipelineState"
+ "_generateLumAsymMask"
+ "_grainBlendPipeline[Shader_10] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_11] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_1] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_2] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_3] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_4] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_5] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_6] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_7] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_8] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_grainBlendPipeline[Shader_9] = [_metalContext computePipelineStateFor:@ \"CMITextureStylesFilmGrain::GrainBlend\" constants:constants]"
+ "_guidedFilterATextureAndFullImageRegion"
+ "_guidedFilterBTextureAndFullImageRegion"
+ "_halationMask"
+ "_inputOutput"
+ "_inputRescaled"
+ "_metalContext.commandBuffer"
+ "_meteorMixed"
+ "_moduleSerial"
+ "_outputBlurredImage"
+ "_parameters"
+ "_perPersonData"
+ "_perPersonIntermediatesAndStats"
+ "_personData.faceLandmarks"
+ "_pyramidFactory"
+ "_rescale420ToRGBA"
+ "_sensorID"
+ "_shadersWithConstants[Shader_ApplyRegionAddbackAndEditingStrength][styleEngineThumbnailModeValI] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"ApplyRegionAddbackAndEditingStrength\" constants:constants]"
+ "_shadersWithConstants[Shader_CalculateBlendCondition][styleEngineThumbnailModeValI] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CalculateBlendCondition\" constants:constants]"
+ "_shadersWithConstants[Shader_CalculateValidMask][styleEngineThumbnailModeValI] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CalculateValidMask\" constants:constants]"
+ "_shadersWithoutConstants[Shader_BoxDownsample] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"BoxDownsample\" constants:constants]"
+ "_shadersWithoutConstants[Shader_CalculateAverageColor] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CalculateAverageColor\" constants:constants]"
+ "_shadersWithoutConstants[Shader_CalculateFracMaskHighlights] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CalculateFracMaskHighlights\" constants:constants]"
+ "_shadersWithoutConstants[Shader_CalculateHistogramRGBA] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CalculateHistogramRGBA\" constants:constants]"
+ "_shadersWithoutConstants[Shader_CalculateHistogramR] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CalculateHistogramR\" constants:constants]"
+ "_shadersWithoutConstants[Shader_CalculateQuantiles] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CalculateQuantiles\" constants:constants]"
+ "_shadersWithoutConstants[Shader_CopyStats] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CopyStats\" constants:constants]"
+ "_shadersWithoutConstants[Shader_CreateExclusionMask] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CreateExclusionMask\" constants:constants]"
+ "_shadersWithoutConstants[Shader_CropAndBoxDownsample] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CropAndBoxDownsample\" constants:constants]"
+ "_shadersWithoutConstants[Shader_CropAndReSample] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"CropAndReSample\" constants:constants]"
+ "_shadersWithoutConstants[Shader_GenerateHistogramInputColorImage] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"GenerateHistogramInputColorImage\" constants:constants]"
+ "_shadersWithoutConstants[Shader_GenerateMin3GrayHistogramInputImage] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"GenerateMin3GrayHistogramInputImage\" constants:constants]"
+ "_shadersWithoutConstants[Shader_GenerateStrengthHistogramInputImages] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"GenerateStrengthHistogramInputImages\" constants:constants]"
+ "_shadersWithoutConstants[Shader_ReSample] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"ReSample\" constants:constants]"
+ "_shadersWithoutConstants[Shader_ScaleByValidMask] = [_context computePipelineStateFor:@ \"CMITextureStylesMattify::\" \"ScaleByValidMask\" constants:constants]"
+ "_shaders[Shader_AverageColor] = [_context computePipelineStateFor:@ \"CMITextureStylesUnderEyeBrighten::\" \"AverageColor\" constants:constants]"
+ "_shaders[Shader_Brighten] = [_context computePipelineStateFor:@ \"CMITextureStylesUnderEyeBrighten::\" \"Brighten\" constants:constants]"
+ "_shaders[Shader_CalculateLumaVarianceAndInferDistributionModality] = [_context computePipelineStateFor:@ \"CMITextureStylesUnderEyeBrighten::\" \"CalculateLumaVarianceAndInferDistributionModality\" constants:constants]"
+ "_shaders[Shader_CalculateVarianceBasedStrengthTaper] = [_context computePipelineStateFor:@ \"CMITextureStylesUnderEyeBrighten::\" \"CalculateVarianceBasedStrengthTaper\" constants:constants]"
+ "_shaders[Shader_CopyStats] = [_context computePipelineStateFor:@ \"CMITextureStylesUnderEyeBrighten::\" \"CopyStats\" constants:constants]"
+ "_shaders[Shader_Copy] = [_context computePipelineStateFor:@ \"CMITextureStylesTextureCopy::\" \"Copy\" constants:constants]"
+ "_shaders[Shader_CreateEyeMask] = [_context computePipelineStateFor:@ \"CMITextureStylesUnderEyeBrighten::\" \"CreateEyeMask\" constants:constants]"
+ "_shaders[Shader_CreateHueMask] = [_context computePipelineStateFor:@ \"CMITextureStylesUnderEyeBrighten::\" \"CreateHueMask\" constants:constants]"
+ "_shaders[Shader_DownSample] = [_context computePipelineStateFor:@ \"CMITextureStylesDownSampler::\" \"DownSample\" constants:constants]"
+ "_shaders[Shader_DownSample] = [_context computePipelineStateFor:@ \"CMITextureStylesPyramid::\" \"DownSample\" constants:constants]"
+ "_shaders[Shader_FinalMix] = [_context computePipelineStateFor:@ \"CMITextureStylesUnderEyeBrighten::\" \"FinalMix\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_10] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_11] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_1] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_2] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_3] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_4] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_5] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_6] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_7] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_8] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GAUSSIAN_SHADER_NAME_9] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Gaussian\" constants:constants]"
+ "_shaders[Shader_GF_SHADER_10] = [_context computePipelineStateFor:@ \"CMITextureStylesGuidedFilter::\" \"ComputeGuided\" constants:constants]"
+ "_shaders[Shader_GF_SHADER_11] = [_context computePipelineStateFor:@ \"CMITextureStylesGuidedFilter::\" \"ComputeGuided\" constants:constants]"
+ "_shaders[Shader_GF_SHADER_4] = [_context computePipelineStateFor:@ \"CMITextureStylesGuidedFilter::\" \"ComputeGuided\" constants:constants]"
+ "_shaders[Shader_GF_SHADER_5] = [_context computePipelineStateFor:@ \"CMITextureStylesGuidedFilter::\" \"ComputeGuided\" constants:constants]"
+ "_shaders[Shader_GF_SHADER_6] = [_context computePipelineStateFor:@ \"CMITextureStylesGuidedFilter::\" \"ComputeGuided\" constants:constants]"
+ "_shaders[Shader_GF_SHADER_7] = [_context computePipelineStateFor:@ \"CMITextureStylesGuidedFilter::\" \"ComputeGuided\" constants:constants]"
+ "_shaders[Shader_GF_SHADER_8] = [_context computePipelineStateFor:@ \"CMITextureStylesGuidedFilter::\" \"ComputeGuided\" constants:constants]"
+ "_shaders[Shader_GF_SHADER_9] = [_context computePipelineStateFor:@ \"CMITextureStylesGuidedFilter::\" \"ComputeGuided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_10] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_11] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_1] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_2] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_3] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_4] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_5] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_6] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_7] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_8] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GUIDED_SHADER_NAME_9] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"Guided\" constants:constants]"
+ "_shaders[Shader_GaussianBlur2dShared] = [_context computePipelineStateFor:@ \"CMITextureStylesGaussianFilter::\" \"GaussianBlur2dShared\" constants:constants]"
+ "_shaders[Shader_GaussianBlurHorizontal] = [_context computePipelineStateFor:@ \"CMITextureStylesGaussianFilter::\" \"GaussianBlurHorizontal\" constants:constants]"
+ "_shaders[Shader_GaussianBlurVertical] = [_context computePipelineStateFor:@ \"CMITextureStylesGaussianFilter::\" \"GaussianBlurVertical\" constants:constants]"
+ "_shaders[Shader_GaussianBlur] = [_context computePipelineStateFor:@ \"CMITextureStylesGaussianFilter::\" \"GaussianBlur\" constants:constants]"
+ "_shaders[Shader_MTLPixelFormatR16Float] = [_context renderPipelineStateForVertexFunction:@\"CMITextureStylesTextureWarping::VertexWarp\" vertexDescriptor:((void *)0) fragmentFunction:@\"CMITextureStylesTextureWarping::FragmentWarp\" constants:((void *)0) colorAttachmentDescriptorArrray:@[desc]]"
+ "_shaders[Shader_Rescale] = [_context computePipelineStateFor:@ \"CMITextureStylesDownSampler::\" \"Rescale\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_10] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_11] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_1] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_2] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_3] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_4] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_5] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_6] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_7] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_8] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SELF_GUIDED_SHADER_NAME_9] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"SelfGuided\" constants:constants]"
+ "_shaders[Shader_SimdGaussianBlur] = [_context computePipelineStateFor:@ \"CMITextureStylesGaussianFilter::\" \"SimdGaussianBlur\" constants:constants]"
+ "_shaders[Shader_SumColorAndFillLumaHistogram] = [_context computePipelineStateFor:@ \"CMITextureStylesUnderEyeBrighten::\" \"SumColorAndFillLumaHistogram\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_10] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_11] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_1] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_2] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_3] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_4] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_5] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_6] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_7] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_8] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_WEIGHTED_GUIDED_SHADER_NAME_9] = [_context computePipelineStateFor:@ \"CMITextureStylesFilter::\" \"WeightedGuided\" constants:constants]"
+ "_shaders[Shader_build_lr_from_full] = [_context computePipelineStateFor:@ \"CMITextureStylesGaussianGuidedFilterV3::\" \"build_lr_from_full\" constants:((void *)0)]"
+ "_shaders[Shader_computeFaceRoughnessKernel]"
+ "_shaders[Shader_computeTextureAmountKernel]"
+ "_shaders[Shader_copyStatsKernel]"
+ "_shaders[Shader_createWeightedAndGuideImages]"
+ "_shaders[Shader_downSample]"
+ "_shaders[Shader_downsample_area_pow2] = [_context computePipelineStateFor:@ \"CMITextureStylesFastGaussian::\" \"downsample_area_pow2\" constants:((void *)0)]"
+ "_shaders[Shader_downsample_nearest2d] = [_context computePipelineStateFor:@ \"CMITextureStylesFastGaussian::\" \"downsample_nearest2d\" constants:((void *)0)]"
+ "_shaders[Shader_finalBlendingKernelInPlace]"
+ "_shaders[Shader_finalBlendingKernel]"
+ "_shaders[Shader_gaussian_h] = [_context computePipelineStateFor:@ \"CMITextureStylesFastGaussian::\" \"gaussian_h\" constants:((void *)0)]"
+ "_shaders[Shader_gaussian_v] = [_context computePipelineStateFor:@ \"CMITextureStylesFastGaussian::\" \"gaussian_v\" constants:((void *)0)]"
+ "_shaders[Shader_guided_lr_2d] = [_context computePipelineStateFor:@ \"CMITextureStylesGaussianGuidedFilterV3::\" \"guided_lr_2d\" constants:((void *)0)]"
+ "_shaders[Shader_multiPersonSkinMaskBlending]"
+ "_shaders[Shader_packPrecomputedMasksKernel]"
+ "_shaders[Shader_upsample_apply_to_mr] = [_context computePipelineStateFor:@ \"CMITextureStylesGaussianGuidedFilterV3::\" \"upsample_apply_to_mr\" constants:((void *)0)]"
+ "_skinSmoothGuidedAvgPipeline"
+ "_skinSmoothGuidedCoeffPipeline"
+ "_smallBlurTextureAndFullImageRegion"
+ "_statsBuffer"
+ "_statsBufferPool"
+ "_statsBuffers"
+ "_subtractBlendMode"
+ "_subtractMask"
+ "_syntheticSkinTexture"
+ "_textureCopier"
+ "_warper"
+ "aR"
+ "addPersonData"
+ "amplitude"
+ "amplitudeDecay"
+ "apertureRatio"
+ "arrayOfDicts"
+ "averageColorMix"
+ "averageFaceColor && [averageFaceColor isKindOfClass:NSArray.class] && ( 3 == averageFaceColor.count ) && [averageFaceColor[0] isKindOfClass:NSNumber.class] && [averageFaceColor[1] isKindOfClass:NSNumber.class] && [averageFaceColor[2] isKindOfClass:NSNumber.class]"
+ "avg && [avg isKindOfClass:NSArray.class] && ( 3 == avg.count ) && [avg[0] isKindOfClass:NSNumber.class] && [avg[1] isKindOfClass:NSNumber.class] && [avg[2] isKindOfClass:NSNumber.class]"
+ "backgroundStrength"
+ "baseGain"
+ "baseGain is <= 0."
+ "baseGain metadata is missing."
+ "baseGain.floatValue >= 1.19209290e-7F"
+ "baselineExposure"
+ "benc"
+ "bg"
+ "bimodalVarianceFalloff"
+ "blendColorImageAverageColorMixFactor"
+ "blendConditionFilterScale"
+ "bloom"
+ "blurHPS"
+ "blurInputTex"
+ "blurOutputTex"
+ "blurVPS"
+ "blurredTex"
+ "body mask (non-face)"
+ "boxDownsamplePS"
+ "brightness"
+ "brightnessMask"
+ "brightnessMix"
+ "bvHigh"
+ "bvLow"
+ "bvLowScale"
+ "bvThresholdDeltaLowScale"
+ "bw3Gamma"
+ "captureMode"
+ "captureMode is nil"
+ "captureType"
+ "captureType is nil"
+ "cmd"
+ "colorBlendFilterScale"
+ "colorManagementMetadata"
+ "com.apple.CMImaging"
+ "common"
+ "computeMinimumInputRegionInFullImageCoordsOut"
+ "computedMinimumInputRegionInFullImageCoordsOut"
+ "contrast"
+ "contrastBoost"
+ "contrastMask"
+ "correctionFeatures"
+ "cropAndDownsamplePS"
+ "croppedAndPartiallyDownsampledTex"
+ "croppedRescaledMattifyExcludeMask"
+ "croppedRescaledRefPersonUnderEyeMask"
+ "curAD > 0"
+ "currentInput.texture != currentOutput.texture"
+ "currentOutput"
+ "currentOutputPtr"
+ "cvReturn == 0 "
+ "dR"
+ "darkScale"
+ "darknessDiffSmoothstepLowerBound"
+ "darknessDiffSmoothstepUpperBound"
+ "defaultTexture"
+ "defocusRadius"
+ "degrunge"
+ "degrungeBody"
+ "desc"
+ "detailSize"
+ "detectionCount"
+ "dictA"
+ "dictB"
+ "difSat"
+ "diffuseColor"
+ "diffusion"
+ "dominantYawTapering"
+ "downScaledIm"
+ "downScaledTex"
+ "ear mask"
+ "editingStrength"
+ "effect"
+ "effect && effectDesc.parameters"
+ "effectsToRender.count"
+ "enableTextureAddback"
+ "entries"
+ "entry"
+ "entry.correctionFeatures"
+ "error"
+ "eye mask"
+ "eyeIndices[i] < features.count"
+ "eyeProtection"
+ "eyebrows"
+ "fP"
+ "face mask"
+ "faceAttitudeDictsByFaceID"
+ "faceID"
+ "faceLandmarkType"
+ "faceLandmarks"
+ "facePitch"
+ "faceROI"
+ "faceROIAndLandmarksROIRelativeScalingROI"
+ "faceROIDictsByFaceID"
+ "faceROIDictsFromLivePhotoInfoTrack"
+ "faceRoll"
+ "faceSkinROI"
+ "faceTempering"
+ "faceUnitOfAngle"
+ "faceYaw"
+ "fast-gauss-area2d"
+ "fast-gauss-area2d-capping-pixels"
+ "fast-gauss-nearest"
+ "fast-gauss-tmpH"
+ "features.count >= 74"
+ "figLivePhotoMetadataDecodedBinaryData"
+ "figLivePhotoMetadataPlaceholder != ((void*)0)"
+ "figLivePhotoMetadataPlaceholder->version >= kFigLivePhotoMetadataVersion1"
+ "filmGrain"
+ "filterRadius"
+ "filterScale >= 1.f"
+ "firstFilterRadius"
+ "firstFilterScale >= 1.f"
+ "focusLensPosition"
+ "fogStrength"
+ "fracMaskHighlightsHeadroom"
+ "fracMaskHighlightsNormFactor"
+ "frequencyGap"
+ "gFContrast"
+ "gFRadius"
+ "gain"
+ "gain metadata is missing."
+ "gamma"
+ "gammaMask"
+ "gauss2D"
+ "gaussianBlurSigma"
+ "gfDimsOkay"
+ "gfTexA"
+ "gfTexB"
+ "glow"
+ "grading"
+ "grainBlurRadius"
+ "grainSelectivity"
+ "gtcData && ! [gtcData isEqual:NSNull.null]"
+ "gtcData count is too big"
+ "gtcData count is too small"
+ "gtcData data length is too small"
+ "gtcData is nil/NSNull"
+ "gtcData.length >= ( ( 1 + gtcLength ) * sizeof( uint16_t ) )"
+ "gtcData.length >= sizeof( uint16_t )"
+ "gtcLength <= 256"
+ "gtcLength >= 64"
+ "gtcTexture"
+ "guide"
+ "guideTex"
+ "hairClothes"
+ "hairTxFloor"
+ "halation"
+ "halationChroma"
+ "halationHue"
+ "halationParameters is nil"
+ "hands mask"
+ "handsAndEars"
+ "hardwareModel"
+ "hardwareModel is nil"
+ "height"
+ "highlight"
+ "highlightRetention"
+ "highlightsToMaskRatio && [highlightsToMaskRatio isKindOfClass:NSNumber.class]"
+ "histogramBuffer"
+ "histogramColor"
+ "histogramImageHighlights"
+ "histogramMin3Gray"
+ "histogramWarpedMaskBinary"
+ "hlBlurStrength"
+ "hlTextureRestore"
+ "hueDiffMeanTermSmoothstepLowerBound"
+ "hueDiffMeanTermSmoothstepUpperBound"
+ "hueDiffSmoothstepLowerBound"
+ "hueDiffSmoothstepUpperBound"
+ "hueMaskFilterScale"
+ "hueMix"
+ "hueRotate"
+ "i12@?0i8"
+ "i16@?0Q8"
+ "imageGuidedFilterEpsilon"
+ "imageGuidedFilterRadius"
+ "imageStats"
+ "imageTextureFactor"
+ "imageTextureThreshold"
+ "input Meteor Gain Map"
+ "input Person mask"
+ "input Sky mask"
+ "input eyebrows mask"
+ "input glasses mask"
+ "input hair mask"
+ "input linear"
+ "input teeth mask"
+ "input.height == guide.height"
+ "input.height == output.height"
+ "input.height == outputA.height"
+ "input.height == outputB.height"
+ "input.texture"
+ "input.width == guide.width"
+ "input.width == output.width"
+ "input.width == outputA.width"
+ "input.width == outputB.width"
+ "inputBodyMask"
+ "inputDownsampledTex"
+ "inputEarMask"
+ "inputEyeMask"
+ "inputEyebrowsMask"
+ "inputFaceMask"
+ "inputGlassesMask"
+ "inputHairMask"
+ "inputHandsMask"
+ "inputInnerKnot0"
+ "inputInnerKnot1"
+ "inputIrisMask"
+ "inputLinear"
+ "inputLipsMask"
+ "inputLowerBound"
+ "inputLowerCoeffA"
+ "inputLowerCoeffB"
+ "inputMeteorGainMap"
+ "inputMouthMask"
+ "inputNoseMask"
+ "inputOuterKnot0"
+ "inputOuterKnot1"
+ "inputOutput.inputImage.texture"
+ "inputOutput.inputLinearImage.texture"
+ "inputOutput.inputSkinMaskAndFullImageRegion.texture"
+ "inputOutput.outputImage.texture"
+ "inputPersonMask"
+ "inputPingPongImageForRendering"
+ "inputReferenceMaskTexture"
+ "inputReferenceMaskTextureCoords"
+ "inputReferenceMaskTriangleVertices"
+ "inputSkinMask"
+ "inputSkyMask"
+ "inputSpread"
+ "inputTattoosMask"
+ "inputTeethMask"
+ "inputThresholdDelta"
+ "inputUpperCoeffA"
+ "inputUpperCoeffB"
+ "instanceMaskReferenceKey"
+ "instanceROI"
+ "intermediateTextureAndFullImageRegions"
+ "intermediatesAndStats"
+ "internalMaskTexture"
+ "io.inputFaceMask.texture"
+ "io.inputImage.texture"
+ "io.inputInstanceMask.texture"
+ "io.outputImage.texture"
+ "ioTextureDict[kIOTextureKey_Input].texture"
+ "ioTextureDict[kIOTextureKey_Output].texture"
+ "iris mask"
+ "kCMBaseObjectError_Invalidated != err"
+ "kFaceLandmarkIndicies[i] < features.count"
+ "key"
+ "largeBlurRadiusFaceDiagonalFactor"
+ "lastDetectionGravityVector"
+ "lastDetectionTimeStamp"
+ "lcb_trace"
+ "leftAvgCol && [leftAvgCol isKindOfClass:NSArray.class] && ( 3 == leftAvgCol.count ) && [leftAvgCol[0] isKindOfClass:NSNumber.class] && [leftAvgCol[1] isKindOfClass:NSNumber.class] && [leftAvgCol[2] isKindOfClass:NSNumber.class]"
+ "leftIsBiModal && [leftIsBiModal isKindOfClass:NSNumber.class]"
+ "leftVariance && [leftVariance isKindOfClass:NSNumber.class]"
+ "lift"
+ "lightMapGamma"
+ "lightMapInvert"
+ "lightMapMax"
+ "lightnessEditFactor"
+ "lightnessEditHeadroom"
+ "lipContrast"
+ "lipCrease"
+ "lipHighlights"
+ "lipNegClar"
+ "lips mask"
+ "lr_x && lr_y && A_lr && b_lr"
+ "maskBlurSigma"
+ "maskThreshold"
+ "mattify"
+ "mattifyIO"
+ "maxDarknessTrigger"
+ "maxFaceFrac"
+ "maxHueTolerance"
+ "maxLevels"
+ "maxRGB"
+ "maximumBimodalVariance"
+ "maximumUnimodalVariance"
+ "memoryResource = self.memoryResource ?: ( self.memoryResource = [self _createMemoryResource] )"
+ "memoryResource.allocatorBackend.memSize >= allocatorDesc.memSize"
+ "metadataDict"
+ "meteorHeadroom"
+ "meteorHeadroomMixFactor"
+ "minDarknessTrigger"
+ "minFaceFrac"
+ "minHueTolerance"
+ "minTexture"
+ "minTextureAddBack"
+ "moduleSerial"
+ "mouth mask"
+ "nLevels"
+ "naturalResolution"
+ "new"
+ "newE"
+ "newInstance"
+ "nightMode"
+ "nightModeSharpness"
+ "nose mask"
+ "oX"
+ "oY"
+ "octaves"
+ "oisShift"
+ "opticalCenter"
+ "originalRangeMax"
+ "originalRangeMin"
+ "outExtendedFaceROI"
+ "outLeftCheekROI"
+ "outRightCheekROI"
+ "outTriangleVerticesLeft"
+ "outTriangleVerticesRight"
+ "output texture is missing color management metadata"
+ "outputA"
+ "outputB"
+ "outputMattifyStats"
+ "outputPtr"
+ "outputRectPtr"
+ "outputSkinSmoothingStats"
+ "outputTexture.pixelFormat == MTLPixelFormatRGBA16Float"
+ "outputTexture.width == mrW && outputTexture.height == mrH"
+ "outputTexturePtr"
+ "outputUEBStats"
+ "pD"
+ "paddedRegionToRenderOut"
+ "parameters"
+ "parameters is nil"
+ "particleDistance"
+ "peopleDataDictsByFaceID"
+ "perPersonIntermediatesAndStats"
+ "person"
+ "person %u instance mask"
+ "personData"
+ "personData->_statsBuffer"
+ "personStrength"
+ "plistData"
+ "plistDict"
+ "plistURL"
+ "plusGreenGuide"
+ "point"
+ "pointDict && errorNum"
+ "pores"
+ "poresBody"
+ "portType"
+ "portType is nil"
+ "position"
+ "preserveColorfulness"
+ "preserveColorfulnessMask"
+ "preset"
+ "preset is nil"
+ "preset:%@ intensity:%.3f grain:%.3f"
+ "pyramid"
+ "quantileBins"
+ "radius"
+ "radiusPtr"
+ "regionMaskThreshold"
+ "relativeToLens"
+ "rightAvgCol && [rightAvgCol isKindOfClass:NSArray.class] && ( 3 == rightAvgCol.count ) && [rightAvgCol[0] isKindOfClass:NSNumber.class] && [rightAvgCol[1] isKindOfClass:NSNumber.class] && [rightAvgCol[2] isKindOfClass:NSNumber.class]"
+ "rightIsBiModal && [rightIsBiModal isKindOfClass:NSNumber.class]"
+ "rightVariance && [rightVariance isKindOfClass:NSNumber.class]"
+ "roiData->fullImageSize.width && roiData->fullImageSize.height"
+ "rough && [rough isKindOfClass:NSNumber.class]"
+ "s"
+ "sC"
+ "sTuningPlist"
+ "sTuningPlist is nil. Check loading of tuning plist."
+ "saturation"
+ "saturationMask"
+ "scaleIsGood"
+ "scalePtr"
+ "secondFilterRadius"
+ "secondFilterScale >= 1.f"
+ "seed"
+ "selectedShader"
+ "self._allocateStatsBuffers == 0 "
+ "self._compileShaders == 0 "
+ "self.metalCommandQueue"
+ "sensorID"
+ "shDarken"
+ "shadowLift"
+ "sharedMemorySize <= cmd.device.maxThreadgroupMemoryLength"
+ "shouldCorrect"
+ "sigma > 0.0f && nSamples > 0 && targetBlurRadius > 0.0f"
+ "sigmaGlare"
+ "simdGaussPipeline"
+ "skinSmoothStandalone"
+ "skinStrength"
+ "skip && [skip isKindOfClass:NSNumber.class]"
+ "skyStrength"
+ "slBG"
+ "slBright"
+ "slDark"
+ "slPerson"
+ "slSkin"
+ "smallBlurRadiusFaceDiagonalFactor"
+ "smallBlurTex"
+ "softLight"
+ "softlink:r:path:/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture"
+ "sortedFilterRadii"
+ "spbHL"
+ "ss_calculateBoundingBox"
+ "ss_calculateFaceROI"
+ "ss_calculateUpDir"
+ "statsBuffer"
+ "strength"
+ "strengthMask"
+ "strongTextureProtect"
+ "sumColorBuffer"
+ "tattooSmoothing"
+ "tattooWeight"
+ "tattoos mask"
+ "tc_roiIsValid( inputROI, inputTexture )"
+ "tc_roiIsValid( outputROI, outputTexture )"
+ "teeth"
+ "temp"
+ "tempStats.faceRoughness >= 0.0f && tempStats.faceRoughness <= 1.0f && __tg_isfinite((__typeof__(__tg_promote((tempStats.faceRoughness))))(tempStats.faceRoughness))"
+ "textureAddBackFilterScale"
+ "textureAddBackScale"
+ "textureClamp"
+ "textureCopier"
+ "textureDetectScale"
+ "textureRestore"
+ "textureRestoreScalingFactor"
+ "textureRestoreSmoothstepLowerBound"
+ "textureRestoreSmoothstepUpperBound"
+ "textureRestoreStrengthFactor"
+ "textureStyle.mattify.editingROIFudgeFactor"
+ "textureStyle.mattify.useFallbackExtendedFaceROI"
+ "textureStyle.mattify.usePeakMemoryOptims"
+ "threshold > 0.0f && threshold < 1.0f"
+ "tileSize"
+ "tmpArea"
+ "tmpDownScaleFactor >= 1.f"
+ "tmpFilterRadius"
+ "tmpNearest"
+ "tmpTex"
+ "triangleVertices"
+ "triangleVerticesOut || roiOut"
+ "triangleVerticesX"
+ "triangleVerticesXY"
+ "triangleVerticesY"
+ "tuningParamsDictByCaptureMode"
+ "tuningParamsDictByEffectType"
+ "tuningParamsDictByPortType"
+ "tuningParamsDictByPreset"
+ "type"
+ "uebIO"
+ "ueb_generateTrianglesAndComputeROI( _personData.faceLandmarks, _personData.faceLandmarkType, UEBEyeIndex_Left == eyeIndex, ((void*)0), &eyeROI ) == 0 "
+ "underEyeBrighten"
+ "unimodalVarianceFalloff"
+ "upsamplePS"
+ "v"
+ "v32@?0@\"CMITextureStylesFaceLandmark\"8Q16^B24"
+ "v32@?0@\"CMITextureStylesPersonInputData\"8Q16^B24"
+ "v32@?0@\"NSDictionary\"8Q16^B24"
+ "validMask"
+ "value.count == 4"
+ "varTexture"
+ "version == 4"
+ "vertexData"
+ "void *CMCaptureLibrary(void)"
+ "warpedMaskAggregate"
+ "warpedTex"
+ "warpedUnderEyeReferenceMask.texture"
+ "weightedTex"
+ "width"
+ "x"
+ "y"
+ "yawFallOff"
+ "yawOffset"
+ "zoom"
+ "\x91"
+ "\xf0a"
```
