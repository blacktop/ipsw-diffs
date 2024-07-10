## CMImaging

> `/System/Library/PrivateFrameworks/CMImaging.framework/Versions/A/CMImaging`

```diff

-558.2.22.1.0
-  __TEXT.__text: 0x1258bc
+563.1.0.0.0
+  __TEXT.__text: 0x12658c
   __TEXT.__auth_stubs: 0x1050
-  __TEXT.__objc_methlist: 0x523c
+  __TEXT.__objc_methlist: 0x525c
   __TEXT.__const: 0x900
-  __TEXT.__cstring: 0x17dbe
-  __TEXT.__oslogstring: 0x10bb5
-  __TEXT.__gcc_except_tab: 0xb84
+  __TEXT.__cstring: 0x184e5
+  __TEXT.__oslogstring: 0x10a4d
+  __TEXT.__gcc_except_tab: 0xbdc
   __TEXT.__dlopen_cstrs: 0x4c
-  __TEXT.__unwind_info: 0x1890
+  __TEXT.__unwind_info: 0x1898
   __TEXT.__eh_frame: 0x1f0
-  __TEXT.__objc_classname: 0xf36
-  __TEXT.__objc_methname: 0x1703e
-  __TEXT.__objc_methtype: 0x71c0
-  __TEXT.__objc_stubs: 0x6da0
+  __TEXT.__objc_classname: 0xf38
+  __TEXT.__objc_methname: 0x16ee5
+  __TEXT.__objc_methtype: 0x7145
+  __TEXT.__objc_stubs: 0x6dc0
   __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__const: 0x1c0
   __DATA_CONST.__objc_classlist: 0x3c8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2a08
+  __DATA_CONST.__objc_selrefs: 0x2a18
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x2f0
   __DATA_CONST.__objc_arraydata: 0x1e0
   __AUTH_CONST.__auth_got: 0x838
-  __AUTH_CONST.__auth_ptr: 0x70
+  __AUTH_CONST.__auth_ptr: 0x68
   __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x3380
-  __AUTH_CONST.__objc_const: 0x19770
+  __AUTH_CONST.__cfstring: 0x3420
+  __AUTH_CONST.__objc_const: 0x19800
   __AUTH_CONST.__objc_intobj: 0x2a0
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH.__objc_data: 0x25d0
-  __DATA.__objc_ivar: 0xec0
+  __DATA.__objc_ivar: 0xecc
   __DATA.__data: 0xb08
   __DATA.__common: 0x190
   __DATA.__bss: 0xb8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2657
-  Symbols:   6111
-  CStrings:  2443
+  Functions: 2660
+  Symbols:   6118
+  CStrings:  2473
 
Symbols:
+ -[CMIStyleEngineConfiguration filterForInputIntegrationThumbnailCreation]
+ -[CMIStyleEngineConfiguration filterForInputLearningThumbnailCreation]
+ -[CMIStyleEngineConfiguration filterForInputLearningWeightsThumbnailCreation]
+ -[CMIStyleEngineConfiguration filterForInputResidualCorrectionThumbnailCreation]
+ -[CMIStyleEngineConfiguration filterForTargetLearningThumbnailCreation]
+ -[CMIStyleEngineConfiguration filterForTargetResidualCorrectionThumbnailCreation]
+ -[CMIStyleEngineConfiguration setFilterForInputIntegrationThumbnailCreation:]
+ -[CMIStyleEngineConfiguration setFilterForInputLearningThumbnailCreation:]
+ -[CMIStyleEngineConfiguration setFilterForInputLearningWeightsThumbnailCreation:]
+ -[CMIStyleEngineConfiguration setFilterForInputResidualCorrectionThumbnailCreation:]
+ -[CMIStyleEngineConfiguration setFilterForTargetLearningThumbnailCreation:]
+ -[CMIStyleEngineConfiguration setFilterForTargetResidualCorrectionThumbnailCreation:]
+ -[CMIStyleEngineDownScaler filter]
+ -[CMIStyleEngineDownScaler setFilter:]
+ -[CMIStyleEngineDownscaledTextureSource filter]
+ -[CMIStyleEngineDownscaledTextureSource initWithSourceTexture:filter:]
+ -[CMIStyleEngineIntegrateCoefficients globalSpatialExtrapolationRampFactor]
+ -[CMIStyleEngineIntegrateCoefficients globalSpatialExtrapolation]
+ -[CMIStyleEngineIntegrateCoefficients maxGlobalMixFactor]
+ -[CMIStyleEngineIntegrateCoefficients setGlobalSpatialExtrapolation:]
+ -[CMIStyleEngineIntegrateCoefficients setGlobalSpatialExtrapolationRampFactor:]
+ -[CMIStyleEngineIntegrateCoefficients setMaxGlobalMixFactor:]
+ -[CMIStyleEngineProcessor downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:filter:copyAttachments:gdcParams:]
+ -[CMIStyleEngineProcessor downScaleInputTexture:withInputCropRect:usingBoxSize:toOutputTexture:filter:gdcParams:]
+ -[CMISubjectRelightingStage _runSubjectRelighting:rgba:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:isChromaGainAdjusted:inputIsLinear:chromaBias:blackPoint:playBackCurve:]
+ OBJC_IVAR_$_CMIStyleEngineConfiguration._filterForInputIntegrationThumbnailCreation
+ OBJC_IVAR_$_CMIStyleEngineConfiguration._filterForInputLearningThumbnailCreation
+ OBJC_IVAR_$_CMIStyleEngineConfiguration._filterForInputLearningWeightsThumbnailCreation
+ OBJC_IVAR_$_CMIStyleEngineConfiguration._filterForInputResidualCorrectionThumbnailCreation
+ OBJC_IVAR_$_CMIStyleEngineConfiguration._filterForTargetLearningThumbnailCreation
+ OBJC_IVAR_$_CMIStyleEngineConfiguration._filterForTargetResidualCorrectionThumbnailCreation
+ OBJC_IVAR_$_CMIStyleEngineDownScaler._filter
+ OBJC_IVAR_$_CMIStyleEngineDownscaledTextureSource._filter
+ OBJC_IVAR_$_CMIStyleEngineIntegrateCoefficients._globalSpatialExtrapolation
+ OBJC_IVAR_$_CMIStyleEngineIntegrateCoefficients._globalSpatialExtrapolationRampFactor
+ OBJC_IVAR_$_CMIStyleEngineIntegrateCoefficients._maxGlobalMixFactor
+ __34-[CMIStyleEngineProcessor process]_block_invoke.572
+ ___320-[CMISubjectRelightingStage _runSubjectRelighting:rgba:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:isChromaGainAdjusted:inputIsLinear:chromaBias:blackPoint:playBackCurve:]_block_invoke
+ ___320-[CMISubjectRelightingStage _runSubjectRelighting:rgba:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:isChromaGainAdjusted:inputIsLinear:chromaBias:blackPoint:playBackCurve:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40w_e52_"<MTLTexture>"32?0"<MTLTexture>"8Q16"NSString"24l
+ _objc_msgSend$_runSubjectRelighting:rgba:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:isChromaGainAdjusted:inputIsLinear:chromaBias:blackPoint:playBackCurve:
+ _objc_msgSend$downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:filter:copyAttachments:gdcParams:
+ _objc_msgSend$downScaleInputTexture:withInputCropRect:usingBoxSize:toOutputTexture:filter:gdcParams:
+ _objc_msgSend$filter
+ _objc_msgSend$filterForInputIntegrationThumbnailCreation
+ _objc_msgSend$filterForInputLearningThumbnailCreation
+ _objc_msgSend$filterForInputLearningWeightsThumbnailCreation
+ _objc_msgSend$filterForInputResidualCorrectionThumbnailCreation
+ _objc_msgSend$filterForTargetLearningThumbnailCreation
+ _objc_msgSend$filterForTargetResidualCorrectionThumbnailCreation
+ _objc_msgSend$initWithSourceTexture:filter:
+ _objc_msgSend$setFilter:
+ _objc_msgSend$setFilterForInputIntegrationThumbnailCreation:
+ _objc_msgSend$setFilterForInputLearningThumbnailCreation:
+ _objc_msgSend$setFilterForInputLearningWeightsThumbnailCreation:
+ _objc_msgSend$setFilterForInputResidualCorrectionThumbnailCreation:
+ _objc_msgSend$setFilterForTargetLearningThumbnailCreation:
+ _objc_msgSend$setFilterForTargetResidualCorrectionThumbnailCreation:
+ _objc_msgSend$setGlobalSpatialExtrapolation:
+ _objc_msgSend$setGlobalSpatialExtrapolationRampFactor:
+ _objc_msgSend$setMaxGlobalMixFactor:
- +[CMIStyleEngineProcessor coefficientCountForSystemOrder:andTuning:globalSystem:]
- +[CMIStyleEngineProcessor coefficientPixelBufferSizeForSystemOrder:andTuning:]
- +[CMIStyleEngineProcessor coefficientPixelBufferSizeForSystemOrder:andTuning:globalSystem:float16:]
- -[CMIStyleEngineConfiguration setUseNearestScalingForInputIntegrationThumbnailCreation:]
- -[CMIStyleEngineConfiguration setUseNearestScalingForInputLearningThumbnailCreation:]
- -[CMIStyleEngineConfiguration setUseNearestScalingForInputLearningWeightsThumbnailCreation:]
- -[CMIStyleEngineConfiguration setUseNearestScalingForInputResidualCorrectionThumbnailCreation:]
- -[CMIStyleEngineConfiguration setUseNearestScalingForTargetLearningThumbnailCreation:]
- -[CMIStyleEngineConfiguration setUseNearestScalingForTargetResidualCorrectionThumbnailCreation:]
- -[CMIStyleEngineConfiguration useNearestScalingForInputIntegrationThumbnailCreation]
- -[CMIStyleEngineConfiguration useNearestScalingForInputLearningThumbnailCreation]
- -[CMIStyleEngineConfiguration useNearestScalingForInputLearningWeightsThumbnailCreation]
- -[CMIStyleEngineConfiguration useNearestScalingForInputResidualCorrectionThumbnailCreation]
- -[CMIStyleEngineConfiguration useNearestScalingForTargetLearningThumbnailCreation]
- -[CMIStyleEngineConfiguration useNearestScalingForTargetResidualCorrectionThumbnailCreation]
- -[CMIStyleEngineDownScaler nearestSampling]
- -[CMIStyleEngineDownScaler setNearestSampling:]
- -[CMIStyleEngineDownscaledTextureSource downscaledUsingNearest]
- -[CMIStyleEngineDownscaledTextureSource initWithSourceTexture:downscaledUsingNearest:]
- -[CMIStyleEngineProcessor downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:usingNearestSampling:copyAttachments:gdcParams:]
- -[CMIStyleEngineProcessor downScaleInputTexture:withInputCropRect:usingBoxSize:toOutputTexture:usingNearestSampling:gdcParams:]
- -[CMISubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]
- OBJC_IVAR_$_CMIStyleEngineConfiguration._useNearestScalingForInputIntegrationThumbnailCreation
- OBJC_IVAR_$_CMIStyleEngineConfiguration._useNearestScalingForInputLearningThumbnailCreation
- OBJC_IVAR_$_CMIStyleEngineConfiguration._useNearestScalingForInputLearningWeightsThumbnailCreation
- OBJC_IVAR_$_CMIStyleEngineConfiguration._useNearestScalingForInputResidualCorrectionThumbnailCreation
- OBJC_IVAR_$_CMIStyleEngineConfiguration._useNearestScalingForTargetLearningThumbnailCreation
- OBJC_IVAR_$_CMIStyleEngineConfiguration._useNearestScalingForTargetResidualCorrectionThumbnailCreation
- OBJC_IVAR_$_CMIStyleEngineDownScaler._nearestSampling
- OBJC_IVAR_$_CMIStyleEngineDownscaledTextureSource._downscaledUsingNearest
- __34-[CMIStyleEngineProcessor process]_block_invoke.581
- ___388-[CMISubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]_block_invoke
- ___388-[CMISubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]_block_invoke_2
- ___block_descriptor_48_e8_32s40w_e52_"<MTLTexture>"28?0"<MTLTexture>"8B16"NSString"20l
- _objc_msgSend$_runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:
- _objc_msgSend$coefficientCountForSystemOrder:andTuning:globalSystem:
- _objc_msgSend$coefficientPixelBufferSizeForSystemOrder:andTuning:globalSystem:float16:
- _objc_msgSend$downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:usingNearestSampling:copyAttachments:gdcParams:
- _objc_msgSend$downScaleInputTexture:withInputCropRect:usingBoxSize:toOutputTexture:usingNearestSampling:gdcParams:
- _objc_msgSend$downscaledUsingNearest
- _objc_msgSend$initWithSourceTexture:downscaledUsingNearest:
- _objc_msgSend$setNearestSampling:
- _objc_msgSend$setUseNearestScalingForInputIntegrationThumbnailCreation:
- _objc_msgSend$setUseNearestScalingForInputLearningThumbnailCreation:
- _objc_msgSend$setUseNearestScalingForInputLearningWeightsThumbnailCreation:
- _objc_msgSend$setUseNearestScalingForInputResidualCorrectionThumbnailCreation:
- _objc_msgSend$setUseNearestScalingForTargetLearningThumbnailCreation:
- _objc_msgSend$setUseNearestScalingForTargetResidualCorrectionThumbnailCreation:
- _objc_msgSend$useNearestScalingForInputIntegrationThumbnailCreation
- _objc_msgSend$useNearestScalingForInputLearningThumbnailCreation
- _objc_msgSend$useNearestScalingForInputLearningWeightsThumbnailCreation
- _objc_msgSend$useNearestScalingForInputResidualCorrectionThumbnailCreation
- _objc_msgSend$useNearestScalingForTargetLearningThumbnailCreation
- _objc_msgSend$useNearestScalingForTargetResidualCorrectionThumbnailCreation
CStrings:
+ "-[CMIStyleEngineProcessor downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:filter:copyAttachments:gdcParams:]"
+ "-[CMIStyleEngineProcessor downScaleInputTexture:withInputCropRect:usingBoxSize:toOutputTexture:filter:gdcParams:]"
+ "-[CMISubjectRelightingStage _runSubjectRelighting:rgba:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:isChromaGainAdjusted:inputIsLinear:chromaBias:blackPoint:playBackCurve:]"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMITiledInferenceProcessor.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/CreateLinearSystem/CMIStyleEngineCreateLinearSystem.m"
+ "/AppleInternal/Library/BuildRoots/d8c9c115-356a-11ef-b3f4-e2437461156c/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/CreateLinearSystem/CMIStyleEngineCreateLinearSystem.m Fig"
+ "@\"<MTLTexture>\"32@?0@\"<MTLTexture>\"8Q16@\"NSString\"24"
+ "ANST metadata is missing in SRL calculations"
+ "Filtered / antialiased downscale requires input size to be 2 or 4 * output size"
+ "GlobalBlendMaxGlobalMix"
+ "GlobalBlendOutsideLearningROI"
+ "GlobalBlendRampParameter"
+ "Stills"
+ "StyleEngine::DownScaleExact"
+ "StyleEngine::DownScaleExact4x"
+ "StyleEngine::DownScaleFiltered2x"
+ "StyleEngine::antiAlias"
+ "StyleEngine::simdShuffleFillSupported"
+ "StyleEngine::useQuadGroup"
+ "_computePipelineStates[DownScaleExactPipelineState_4x]"
+ "_computePipelineStates[DownScaleExactPipelineState_4x] is NULL"
+ "_computePipelineStates[DownScaleExactPipelineState_8x]"
+ "_computePipelineStates[DownScaleExactPipelineState_8x] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x]"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x_GDC]"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x_GDC] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x_antiAliased]"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x_antiAliased] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x_antiAliased_GDC]"
+ "_computePipelineStates[DownScaleFilteredPipelineState_2x_antiAliased_GDC] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x]"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x_GDC]"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x_GDC] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x_antiAliased]"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x_antiAliased] is NULL"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x_antiAliased_GDC]"
+ "_computePipelineStates[DownScaleFilteredPipelineState_4x_antiAliased_GDC] is NULL"
+ "_computePipelineStates[DownScalePipelineState_GDC_Quad]"
+ "_computePipelineStates[DownScalePipelineState_GDC_Quad] is NULL"
+ "_computePipelineStates[DownScalePipelineState_Quad]"
+ "_computePipelineStates[DownScalePipelineState_Quad] is NULL"
+ "_computePipelineStates[SimpleResizePipelineState]"
+ "_computePipelineStates[SimpleResizePipelineState] is NULL"
+ "_computePipelineStates[SimpleResizePipelineState_GDC]"
+ "_computePipelineStates[SimpleResizePipelineState_GDC] is NULL"
+ "err = CMIStyleEngineStatusIncorrectIO == 0 "
+ "err = FigSignalErrorAt3(\"%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)\", gStyleEngineProcessorTrace.note.emitter, (CMIStyleEngineStatusResourcesNotReleased), \"CMIStyleEngineStatusResourcesNotReleased\", (\"FigMetalAllocator resources not correctly released\"), \"<<<< StyleEngineProcessor >>>>\", __FUNCTION__, \"CMIStyleEngineProcessor.m\", 2899, __builtin_return_address(0), 0) == 0 "
+ "rgbaTexture"
- "-[CMIStyleEngineProcessor downScaleInputPixelBuffer:withInputCropRect:usingBoxSize:toOutputPixelBuffer:usingNearestSampling:copyAttachments:gdcParams:]"
- "-[CMIStyleEngineProcessor downScaleInputTexture:withInputCropRect:usingBoxSize:toOutputTexture:usingNearestSampling:gdcParams:]"
- "-[CMISubjectRelightingStage _runSubjectRelighting:luma:chroma:skinMask:personMask:instanceMasks:instanceMaskConfidences:skinToneClassification:validROI:expBias:faceExpRatio:exifOrientation:srlV2Plist:faceDataFromANST:toneMap:ltmChroma:gammaCurve:numFacesISPDetected:faceBoundingBoxesFromISP:isChromaGainAdjusted:inputIsLinear:chromaBias:mstmParams:mstmSRLParams:blackPoint:playBackCurve:]"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/CMITiledInferenceProcessor/Source/CMITiledInferenceProcessor.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/CreateLinearSystem/CMIStyleEngineCreateLinearSystem.m"
- "/AppleInternal/Library/BuildRoots/0d0c1d4c-2d6d-11ef-bfc3-a2cee5656455/Library/Caches/com.apple.xbs/Sources/CameraCapture_CMImaging/CMImaging/Sources/StyleEngine/ProcessingStages/CreateLinearSystem/CMIStyleEngineCreateLinearSystem.m Fig"
- "@\"<MTLTexture>\"28@?0@\"<MTLTexture>\"8B16@\"NSString\"20"
- "SpotlightCount_X"
- "SpotlightCount_Y"
- "StyleEngine::DownScale_Exact"
- "WeightPlaneCount"
- "_computePipelineStates[UpScalePipelineState]"
- "_computePipelineStates[UpScalePipelineState] is NULL"
- "_computePipelineStates[UpScalePipelineState_GDC]"
- "_computePipelineStates[UpScalePipelineState_GDC] is NULL"
- "err = FigSignalErrorAt3(\"%!s(MISSING)%!s(MISSING)%!s(MISSING) signalled err=%!d(MISSING) (%!s(MISSING)) (%!s(MISSING)) at %!s(MISSING):%!d(MISSING)\", gStyleEngineProcessorTrace.note.emitter, (CMIStyleEngineStatusResourcesNotReleased), \"CMIStyleEngineStatusResourcesNotReleased\", (\"FigMetalAllocator resources not correctly released\"), \"<<<< StyleEngineProcessor >>>>\", __FUNCTION__, \"CMIStyleEngineProcessor.m\", 2896, __builtin_return_address(0), 0) == 0 "
- "faces"
- "totalConfidence != 0"
- "v5"
- "zero confidence"

```
