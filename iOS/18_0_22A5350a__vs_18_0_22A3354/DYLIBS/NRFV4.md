## NRFV4

> `/System/Library/VideoProcessors/NRFV4.bundle/NRFV4`

```diff

-575.14.1.0.0
-  __TEXT.__text: 0x1ecb90
-  __TEXT.__auth_stubs: 0xe80
-  __TEXT.__objc_methlist: 0xe488
-  __TEXT.__const: 0x102618
-  __TEXT.__cstring: 0x2b95d
+575.15.1.0.0
+  __TEXT.__text: 0x1f5f08
+  __TEXT.__auth_stubs: 0xec0
+  __TEXT.__objc_methlist: 0xe700
+  __TEXT.__const: 0x1026a0
+  __TEXT.__cstring: 0x2c6de
   __TEXT.__gcc_except_tab: 0x16f4
-  __TEXT.__oslogstring: 0x21697
+  __TEXT.__oslogstring: 0x21d01
   __TEXT.__dlopen_cstrs: 0x10c
-  __TEXT.__unwind_info: 0x2c58
-  __TEXT.__objc_classname: 0x2ce8
-  __TEXT.__objc_methname: 0x2f3a2
-  __TEXT.__objc_methtype: 0x1502f
-  __TEXT.__objc_stubs: 0x13ba0
-  __DATA_CONST.__got: 0xa50
-  __DATA_CONST.__const: 0x11e0
-  __DATA_CONST.__objc_classlist: 0xc70
+  __TEXT.__unwind_info: 0x2cc0
+  __TEXT.__objc_classname: 0x2d52
+  __TEXT.__objc_methname: 0x2fe18
+  __TEXT.__objc_methtype: 0x1542d
+  __TEXT.__objc_stubs: 0x143e0
+  __DATA_CONST.__got: 0xab8
+  __DATA_CONST.__const: 0x1208
+  __DATA_CONST.__objc_classlist: 0xc98
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xd8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a30
+  __DATA_CONST.__objc_selrefs: 0x5ba0
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x970
-  __DATA_CONST.__objc_arraydata: 0xcc8
-  __AUTH_CONST.__auth_got: 0x750
+  __DATA_CONST.__objc_superrefs: 0x988
+  __DATA_CONST.__objc_arraydata: 0xd18
+  __AUTH_CONST.__auth_got: 0x770
   __AUTH_CONST.__auth_ptr: 0x20
   __AUTH_CONST.__const: 0x7a0
-  __AUTH_CONST.__cfstring: 0x117e0
-  __AUTH_CONST.__objc_const: 0x32ad0
-  __AUTH_CONST.__objc_doubleobj: 0x70
+  __AUTH_CONST.__cfstring: 0x12060
+  __AUTH_CONST.__objc_const: 0x33950
+  __AUTH_CONST.__objc_doubleobj: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x9c0
   __AUTH_CONST.__objc_intobj: 0x9d8
-  __AUTH_CONST.__objc_dictobj: 0x500
-  __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH.__objc_data: 0x870
-  __DATA.__objc_ivar: 0x31d8
-  __DATA.__data: 0xad0
-  __DATA.__common: 0x20
+  __AUTH_CONST.__objc_dictobj: 0x528
+  __AUTH_CONST.__objc_floatobj: 0x40
+  __AUTH.__objc_data: 0x960
+  __DATA.__objc_ivar: 0x32c4
+  __DATA.__data: 0xb30
+  __DATA.__common: 0x24
   __DATA.__bss: 0x1c
-  __DATA_DIRTY.__objc_data: 0x73f0
+  __DATA_DIRTY.__objc_data: 0x7490
   __DATA_DIRTY.__bss: 0x128
   __DATA_DIRTY.__common: 0xec
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 4897
-  Symbols:   5449
-  CStrings:  14844
+  Functions: 4945
+  Symbols:   5514
+  CStrings:  15113
 
Symbols:
+ _kFigCaptureSampleBufferMetadata_NoiseModelKey_SquaredNoise
+ _kFigCaptureStreamMetadata_AWBSkinGGain
+ _kFigCaptureSampleBufferMetadata_NoiseModelKey_SpatialSigma
+ _kFigCaptureStillImageProcessingMetadataKey_StereoPhotoPrimaryAWBMetadata
+ __simd_log2_f4
+ _objc_release_x11
+ _FigCaptureMetadataUtilitiesComputeDenormalizedStillImageCropRect
+ _kFigCaptureSampleBufferMetadata_NoiseModelKey_Version
+ _kFigCaptureStillImageProcessingMetadataKey_StereoPhotoFOV
+ _kFigCaptureSampleBufferMetadata_NoiseModelKey_ReadNoise
+ _kFigCaptureStreamMetadata_AWBSpatialCCMMixingFactor
+ _kFigCaptureStreamMetadata_AWBSkinRGain
+ _kFigCaptureSampleBufferMetadata_NoiseModelKey_ShotNoise
+ _FigCaptureMetadataUtilitiesPreventFurtherCropping
+ _kFigCaptureSampleBufferMetadata_NoiseModel
+ _OBJC_CLASS_$_NSInvocation
+ _kFigCaptureStreamMetadata_AWBSkinBGain
CStrings:
+ "skinColorSampleVariance"
+ "_computePipelineStates[GeneratePlainTargetPipelineState]"
+ "skinColorSampleNum"
+ "setEnableMIWB:"
+ "awbCSCCoef"
+ "supportsFaceAssistedSkinGainsToMatch"
+ "MIWB::transferStyle"
+ "denoiseSingleImage:linearOutput:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:inputFrameIndex:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:"
+ "MIWB::makeIlluminantMap"
+ "_skyMaskBlurredTex"
+ "Histogram"
+ "configureStyleEngine"
+ "cscConfig"
+ "miwb_sensThumbnailTex"
+ "cscCoef"
+ "minDistSkinToWhiteMapping"
+ "Failed to allocate StyleEngine externalMemoryResource"
+ "miwb_weightPlanesArrayTex"
+ "miredToC1:"
+ "TB,N,V_hazeAppliedInMIWB"
+ "TB,N,V_enableMIWB"
+ "setInputWeightPlaneTexture:"
+ "MIWBSkinNonComboRGain"
+ "MIWBSkinWeight"
+ "CSCCoef"
+ "i104@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@40I48^{__CVBuffer=}52@60@68@76@?84B92i96B100"
+ "_hazeAppliedInMIWB"
+ "_stfThumbnailTex"
+ "_miwbModuleConfigPlistDictByPortType"
+ "miwb_ignoreMapTex"
+ "tuningPlist"
+ "readModuleConfigPlist:"
+ "miwb_stfThumbnailTex"
+ "AWB secondaryCameraInfo not available with your SDK"
+ "_ignoreMapTex"
+ "_wpStatsBuffer"
+ "{IlluminantMapConfig=\"gaussianKernel\"{?=\"columns\"[3]}\"rgb2YCoeffs\"\"invRgb2YCoeffs\"\"ryb2c1c2Coeffs\"{?=\"columns\"[3]}\"offsetC1C2\"\"scaleC1C2\"\"invScaleC1C2\"\"miredConfig\"{MiredConfig=\"miredMin\"f\"miredMax\"f\"x2CctMin\"f\"x2CctMax\"f\"sortedX2CctToMired\"[8]\"sortedMiredToX2Cct\"[8]\"thetaPl\"\"distMultiplier\"f\"cctMired\"f\"cctHiThresh\"f\"cctLoThresh\"f\"kneeSlope\"f\"coolClip\"f\"warmClip\"f}\"rMatrix\"{?=\"columns\"[2]}}"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %!s(MISSING): onmPlist is nil"
+ "OutputNoiseModelPlist"
+ "@\"MIWBPlist\""
+ "inLinearLumaTex"
+ "ccmCoef.count == 9"
+ "wpRgLogRatio"
+ "_computePipelineStates[TransferStyleState]"
+ "miwb_skinMaskTex"
+ "MIWBSkyRGain"
+ "_blueMapPdfStatsBuffer"
+ "TB,N,V_configured"
+ "[8f]"
+ "outLinearLumaTex"
+ "setupMIWB:"
+ "awbParams.secondaryCameraInfo"
+ "miwb_skyMaskTex"
+ "deallocInternalResources"
+ "!\x11\x11!"
+ "-[DenoiseFusePipeline toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:]"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %!s(MISSING): %!@(MISSING) is nil"
+ "EnableMIWB"
+ "awbConfig[@\"Histogram\"][@\"Config\"][@\"C1Scale\"]"
+ "methodSignatureForSelector:"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %!s(MISSING): entryParams OutputNoiseModel is nil"
+ "offset2"
+ "miwb_finalTargetTex"
+ "_requestLinearMIWBAppliedOutput"
+ "_clusterTex"
+ "SquaredNoiseScalingFactor"
+ "SingleImageParametersForSambaQuadraLearnedNR"
+ "OutputNoiseModel"
+ "_c1c2Tex"
+ "@\"OutputNoiseModelPlist\""
+ "setMiwbOutputLumaTexture:"
+ "setInputThumbnailIsLinear:"
+ "xSortedMired"
+ "miwb_skyMaskBlurredTex"
+ "TB,N,V_requestLinearMIWBAppliedOutput"
+ "MIWBSkinNonComboBGain"
+ "MIWB.m"
+ "_sensThumbnailTex"
+ "getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:"
+ "24@0:816"
+ "_miwbStage.configured"
+ "DaylightScore"
+ "miwbOutputChromaTexture"
+ "miwb_clusterTex"
+ "_whitePointStats"
+ "squaredNoiseScalingFactor"
+ "setTargetThumbnailIsLinear:"
+ "_computePipelineStates[MakeIlluminantMapPipelineState]"
+ "setTarget:"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %!s(MISSING): MIWB readPlist failed"
+ "MIWB::generateThumTargetPlain"
+ "configWithFrameMetaData:miwbInputHasCCMApplied:"
+ "inLinearChromaTex"
+ "setMiwbOutputChromaTexture:"
+ "_computePipelineStates[GenerateThumbnailsPipelineState]"
+ "_enableMIWB"
+ "getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:"
+ "_\x0e"
+ "awbCCMCoef"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %!s(MISSING): Quadra bayer pattern must be BBGG or RRGG"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %!s(MISSING): OutputNoiseModel readPlist failed"
+ "SingleImageParametersForSambaLearnedNR"
+ "f32@0:8f16r^20i28"
+ "_linearOutputMIWBAppliedPixelBuffer"
+ "_skyMaskTex"
+ "xtoCCT[i][@\"Y\"]"
+ "MIWBSkyBGain"
+ "awbConfig[@\"CSC\"][@\"CSCOffset\"][1]"
+ "!\x11!1!\x11\x11"
+ "createShaders"
+ "miwbOutputLumaTexture"
+ "!\x11\x11\x111"
+ "AWB faceAssistedSkinGainsToMatch not available with your SDK"
+ "MIWBOutputMetadata"
+ "XToCCT"
+ "scale2"
+ "supportsCameraInfo"
+ "rgbToC1c2:"
+ "supportsSecondaryCameraInfoDict"
+ "MIWBModuleConfigPlist.m"
+ "_computePipelineStates"
+ "setConfigured:"
+ "SpatialSigma"
+ "_skinMaskBlurredTex"
+ "setHazeAppliedInMIWB:"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/CMIPost.m %!s(MISSING): _miwbStage nil"
+ "enableMIWB"
+ "yCorresX2cct"
+ "secondaryModuleConfig"
+ "-[DenoiseFusePipeline denoiseSingleImage:linearOutput:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:inputFrameIndex:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:]"
+ "OutputNoiseModelPlistV4.m"
+ "x2CCtLut"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %!s(MISSING): OutputNoiseModelPlist readPlist failed"
+ "{MiwbConfig=\"thumbnailSize\"\"hazeInputMatCCM\"{?=\"columns\"[3]}\"hazeOutputInvMatCCM\"{?=\"columns\"[3]}\"miwbInputInvMatCCM\"{?=\"columns\"[3]}\"miwbOutputMatCCM\"{?=\"columns\"[3]}\"matSkyCcm\"{?=\"columns\"[3]}\"matSkinCcm\"{?=\"columns\"[3]}\"globalWhitePoint\"\"skyWhitePoint\"\"skinWhitePoint\"\"coolStrength\"f\"warmStrength\"f\"whiteL\"f\"satMapFactor\"f\"blueSky\"f\"dayLightWeight\"f}"
+ "_miwbOutputLumaTexture"
+ "MIWB::ApplyStyle"
+ "wpSkinBgLogRatio"
+ "[8[3f]]"
+ "setRequestLinearMIWBAppliedOutput:"
+ "AwbOutputMetadata"
+ "C2Scale"
+ "CCT"
+ "CSC"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/CMIPost.m %!s(MISSING): %!@(MISSING) is nil"
+ "calculateBasicNoiseModelFromParams:"
+ "secondaryCameraInfo"
+ "invocationWithMethodSignature:"
+ "self->spatialSigma"
+ "_portTypeConfigured"
+ "MIWB"
+ "xtoCCT[i][@\"X\"]"
+ "miwb_skinMaskBlurredTex"
+ "MIWB::BlitBuffersToZero"
+ "CCMCoef"
+ "MIWBParameters"
+ "_illuminantConfig"
+ "-[MIWB initWithMetalContext:]"
+ "interpolateLinear1D:samples:nSamples:"
+ "outputNoiseModel"
+ "[4@\"<MTLComputePipelineState>\"]"
+ "canRunMIWB:"
+ "T^{__CVBuffer=},?,&,N,V_linearOutputMIWBAppliedPixelBuffer"
+ "miwbPlist"
+ "xtoCCT.count <= ( 8 )"
+ "Quadra bayer pattern must be BBGG or RRGG"
+ "_linearOutputMIWBAppliedMetadata"
+ "miwb_clusterFullTex"
+ "-[MIWB createTexture:label:]"
+ "ccmCoef"
+ "! CGRectIsNull( denormalizedZoomRect )"
+ "scale1"
+ "xSortedX2cct"
+ "MIWBModuleConfigPlist"
+ "[9f]"
+ "MIWB::CreateTarget"
+ "_AWBProcessor.awbParams.cameraInfo"
+ "ReadNoiseScalingFactor"
+ "inSkyMaskTex"
+ "readNoiseScalingFactor"
+ "T^{__CVBuffer=},&,N,V_linearOutputMIWBAppliedPixelBuffer"
+ "MIWB::generateInitialThumbnails"
+ "miwb_localIllMapTex"
+ "T@\"<MTLTexture>\",&,N,V_miwbOutputChromaTexture"
+ "_AWBProcessor.awbParams.moduleConfig"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %!s(MISSING): Unable to find module config for port %!@(MISSING)"
+ "T@\"NSMutableDictionary\",&,N,V_linearOutputMIWBAppliedMetadata"
+ "{WhitepointStats=\"gRgb\"\"bRgb\"}"
+ "self->squaredNoiseScalingFactor"
+ "setUseLiveMetalAllocations:"
+ "i124@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@40@48@56@64^{__CVBuffer=}72@80@88@96@?104B112i116B120"
+ "AWB secondaryModuleConfig not available with your SDK"
+ "faceAssistedSkinGainsToMatch"
+ "_weightPlanesArrayTex"
+ "_localIllMapTex"
+ "awbParams.faceAssistedSkinGainsToMatch"
+ "awbConfig[@\"CSC\"][@\"CSCOffset\"][2]"
+ "linearOutputMIWBAppliedPixelBuffer"
+ "MIWBPlist"
+ "awbConfig[@\"Histogram\"][@\"Config\"][@\"C2Scale\"]"
+ "c1ToMired:"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/RawDF/Tunning/RawDFTuningV4.m %!s(MISSING): MIWBPlist is nil"
+ "setLinearOutputMIWBAppliedPixelBuffer:"
+ "toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:"
+ "setArgument:atIndex:"
+ "wpBgLogRatio"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/MIWB/MIWB.m %!s(MISSING): Unable to initialize MIWB Stage"
+ "T@\"<MTLTexture>\",&,N,V_miwbOutputLumaTexture"
+ "i108@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@40^{__CVBuffer=}48^{__CVBuffer=}56@64@72@80@?88B96i100B104"
+ "awbConfig"
+ "self->shotNoiseScalingFactor"
+ "_miwbOutputChromaTexture"
+ "generateNoiseModelFromReferenceFrameMetadata:nFusedFrames:tuningPlist:"
+ "linearOutputMIWBAppliedMetadata"
+ "thisMIWBModuleConfigPlist"
+ "setSelector:"
+ "denoiseSingleImage:linearOutput:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:inputLuma:inputChroma:inputYCbCr:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:"
+ "xtoCCT[i][@\"CCT\"]"
+ "wpSkinRgLogRatio"
+ "( bayer == kCVVersatileSenselArray_QUADRA_BBGG ) || ( bayer == kCVVersatileSenselArray_QUADRA_RRGG )"
+ "denoiseSingleImage:linearOutput:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:input:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:"
+ "spatialSigma"
+ "getReturnValue:"
+ "shotNoiseScalingFactor"
+ "CMIPostMIWBMetadata"
+ "createTexture:label:"
+ "c1c2Torgb:"
+ "nFusedFrames > 0"
+ "invoke"
+ "awbParams.secondaryModuleConfig"
+ "awbParams.moduleConfig"
+ "@\"MIWB\""
+ "ShotNoiseScalingFactor"
+ "i96@0:8r^{FusionConfiguration=[5{?=[3]}]B[5{ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}]iiiiiiBBBBiBBB}16^@24@32@40^{__CVBuffer=}48@56^{__CVBuffer=}64@?72i80B84@88"
+ "yCorrespMird"
+ "awbParams.cameraInfo"
+ "( inputFrame.firstPixel == ( 2 ) ) || ( inputFrame.firstPixel == ( 1 ) )"
+ "AutoWhiteBalance"
+ "C1Scale"
+ "-[MIWB configWithFrameMetaData:miwbInputHasCCMApplied:]"
+ "offset1"
+ "supportsModuleConfig"
+ "_miwbConfig"
+ "! sensorNoiseModel.invalid"
+ "-[DenoiseFusePipeline denoiseSingleImage:linearOutput:linearOutputMIWBAppliedPixelBuffer:linearOutputMIWBAppliedMetadata:inputLuma:inputChroma:inputYCbCr:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:]"
+ "_miwbStage"
+ "supportsSecondaryModuleConfigDict"
+ "requestLinearMIWBAppliedOutput"
+ "setLinearOutputMIWBAppliedMetadata:"
+ "configured"
+ "hazeAppliedInMIWB"
+ "CSCOffset"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/CMIPost.m %!s(MISSING): tdMIWB is nil"
+ "stringWithString:"
+ "self->readNoiseScalingFactor"
+ "OutputNoiseModelV4.m"
+ "i80@0:8@16@24@32@4048@64@72"
+ "_clusterFullTex"
+ "cscCoef.count == 9"
+ "runWithInLinearLumaTex:inLinearChromaTex:inSkyMaskTex:inSkinMaskTex:inHazeCorrection:outLinearLumaTex:outLinearChromaTex:"
+ "_finalTargetTex"
+ "\x05\xf0\xf0\xf0\xf0\xf0\xf0n\x14"
+ "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/Post/CMIPost.m %!s(MISSING): MIWB configuration failed: %!d(MISSING)"
+ "allocInternalResources"
+ "32@0:816"
+ "_skinMaskTex"
+ "T@\"NSMutableDictionary\",?,&,N,V_linearOutputMIWBAppliedMetadata"
+ "_hasBeenSetup"
+ "miwb_c1c2Tex"
+ "outLinearChromaTex"
+ "continuousFDTimes"
- "inputFrame.firstPixel == ( 2 )"
- "i92@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40@48@56@64@?72B80i84B88"
- "i80@0:8r^{FusionConfiguration=[5{?=[3]}]B[5{ColorSpaceConversionParameters={?=[3]}{?=[3]}{?=[3]}{TransferFunctionParameters=fffff}{TransferFunctionParameters=fffff}fffBBBB}]iiiiiiBBBBiBBB}16^@24@32@40^{__CVBuffer=}48@?56i64B68@72"
- "-[DenoiseFusePipeline denoiseSingleImage:linearOutput:inputFrameIndex:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:]"
- "i108@0:8^{__CVBuffer=}16^{__CVBuffer=}24@32@40@48^{__CVBuffer=}56@64@72@80@?88B96i100B104"
- "!\x11\x111"
- "denoiseSingleImage:linearOutput:inputFrameIndex:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:"
- "-[DenoiseFusePipeline denoiseSingleImage:linearOutput:inputLuma:inputChroma:inputYCbCr:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:]"
- "-[DenoiseFusePipeline toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:]"
- "\x0f\x05"
- "i88@0:8^{__CVBuffer=}16^{__CVBuffer=}24I32^{__CVBuffer=}36@44@52@60@?68B76i80B84"
- "bayer == kCVVersatileSenselArray_QUADRA_BBGG"
- "denoiseSingleImage:linearOutput:input:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:"
- "toneMapAndDenoiseFusedFramesWithConfig:properties:nrfPlist:style:output:inferenceProvider:colorCubeFixType:isLowLight:gainMap:"
- "/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/NRF/V4/LearnedNR/LearnedNRNetworkStageV4.m %!s(MISSING): Quadra bayer pattern must be BBGG"
- "denoiseSingleImage:linearOutput:inputLuma:inputChroma:inputYCbCr:noiseMap:cfp:nrfPlist:style:inferenceProvider:defringeEnabled:colorCubeFixType:isLowLight:"
- "!\x11!"
- "Quadra bayer pattern must be BBGG"
- "!\x11!1!\x11"
- "_\f"

```
