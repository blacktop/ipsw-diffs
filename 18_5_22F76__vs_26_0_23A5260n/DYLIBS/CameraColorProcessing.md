## CameraColorProcessing

> `/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`

```diff

-208.100.3.0.0
-  __TEXT.__text: 0x6c008
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_methlist: 0x18c4
-  __TEXT.__const: 0x5030
-  __TEXT.__gcc_except_tab: 0x5df0
-  __TEXT.__cstring: 0x6a84
+650.0.0.122.4
+  __TEXT.__text: 0x84140
+  __TEXT.__auth_stubs: 0x780
+  __TEXT.__objc_methlist: 0x1d64
+  __TEXT.__const: 0x694c
+  __TEXT.__gcc_except_tab: 0x4848
+  __TEXT.__cstring: 0x7d3e
   __TEXT.__dlopen_cstrs: 0xa0
-  __TEXT.__oslogstring: 0x98ff
-  __TEXT.__unwind_info: 0xa18
-  __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x485
-  __TEXT.__objc_methname: 0x4121
-  __TEXT.__objc_methtype: 0x8dc4
-  __TEXT.__objc_stubs: 0x2a60
+  __TEXT.__oslogstring: 0xb1dd
+  __TEXT.__unwind_info: 0xb68
+  __TEXT.__eh_frame: 0x90
+  __TEXT.__objc_classname: 0x43d
+  __TEXT.__objc_methname: 0x4935
+  __TEXT.__objc_methtype: 0xc26b
+  __TEXT.__objc_stubs: 0x2be0
   __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__objc_classlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd68
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_arraydata: 0xb0
-  __AUTH_CONST.__auth_got: 0x3f0
-  __AUTH_CONST.__const: 0x550
-  __AUTH_CONST.__cfstring: 0x4260
-  __AUTH_CONST.__objc_const: 0x3858
-  __AUTH_CONST.__objc_arrayobj: 0x90
-  __AUTH_CONST.__objc_intobj: 0x48
+  __DATA_CONST.__objc_selrefs: 0xdc8
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_arraydata: 0x280
+  __AUTH_CONST.__auth_got: 0x3d8
+  __AUTH_CONST.__const: 0x430
+  __AUTH_CONST.__cfstring: 0x2a00
+  __AUTH_CONST.__objc_const: 0x4968
+  __AUTH_CONST.__objc_intobj: 0x3f0
+  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_floatobj: 0x10
-  __DATA.__objc_ivar: 0x360
-  __DATA.__data: 0x8a0
-  __DATA_DIRTY.__objc_data: 0x550
+  __AUTH.__objc_data: 0x2d0
+  __DATA.__objc_ivar: 0x454
+  __DATA.__data: 0xfe8
+  __DATA.__common: 0x420
+  __DATA_DIRTY.__objc_data: 0x500
   __DATA_DIRTY.__data: 0x178
-  __DATA_DIRTY.__bss: 0x7d0
+  __DATA_DIRTY.__bss: 0x748
   __DATA_DIRTY.__common: 0x248
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B6760234-CA48-3C0B-ABAF-C013AE3A8C53
-  Functions: 875
-  Symbols:   3103
-  CStrings:  3027
+  UUID: 221F7A86-CD47-376E-A546-9DC0AD7B974B
+  Functions: 1007
+  Symbols:   3558
+  CStrings:  3070
 
Symbols:
+ +[AWBProcessor getTileStatsRegionWithMetadata:cropRectLTMInCoords:ltmInDownsamplingRatio:tileStatsRegionLTMInCoordsDictOut:]
+ +[AWBStatistics getTileStatsRegionWithMetadata:cropRectLTMInCoords:ltmInDownsamplingRatio:tileStatsRegionLTMInCoordsDictOut:]
+ +[GeometryUtilities getTransformCropRectFromSensorCoordsToValidBufferCoordsWithMetadata:validBufferRect:]
+ +[GeometryUtilities initialize]
+ +[LTMExtractMetadataV1 compareAWBMetadata:withReference:]
+ +[LTMExtractMetadataV1 extractAWBMetadataFromMetadata:validBufferRect:toDriverInput:]
+ +[LTMExtractMetadataV1 extractAWBMetadataFromRawMetadata:toDriverInput:]
+ +[LTMExtractMetadataV1 extractCCMFromMetadata:toDriverInput:]
+ +[LTMExtractMetadataV1 extractFromRawMetadata:toDriverInput:]
+ +[LTMExtractMetadataV1 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]
+ +[LTMExtractMetadataV1 getTileStatsRegion:validBufferRect:toDriverInput:]
+ +[LTMExtractMetadataV1 isLocalCCMEnabled:]
+ +[LTMExtractMetadataV2 compareAWBMetadata:withReference:]
+ +[LTMExtractMetadataV2 extractAWBMetadataFromMetadata:validBufferRect:ltmGeometryData:toDriverInput:]
+ +[LTMExtractMetadataV2 extractAWBMetadataFromRawMetadata:toDriverInput:]
+ +[LTMExtractMetadataV2 extractCCMFromMetadata:toDriverInput:]
+ +[LTMExtractMetadataV2 extractFromRawMetadata:toDriverInput:]
+ +[LTMExtractMetadataV2 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]
+ +[LTMExtractMetadataV2 getTileStatsRegion:validBufferRect:ltmGeometryData:toDriverInput:]
+ +[LTMExtractMetadataV2 isLocalCCMEnabled:]
+ +[LTMMetadataWriterV1 _addAverageLTMToMetadata:curvesType:fromOutput:]
+ +[LTMMetadataWriterV1 _addGlobalLTMLookUpTableAlignedToFinalCropRect:]
+ +[LTMMetadataWriterV1 _addHazeCorrection:driverInputMetadata:]
+ +[LTMMetadataWriterV1 _addHighlightCompression:driverInputMetadata:]
+ +[LTMMetadataWriterV1 _addLTMCurveTypeToMetadata:driverInputMetadata:]
+ +[LTMMetadataWriterV1 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:]
+ +[LTMMetadataWriterV1 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:].cold.1
+ +[LTMMetadataWriterV1 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:].cold.2
+ +[LTMMetadataWriterV1 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:].cold.3
+ +[LTMMetadataWriterV1 _addLTMEnabledToMetadata:]
+ +[LTMMetadataWriterV1 _addLocalClippingDataToMetadata:statistics:geometryData:]
+ +[LTMMetadataWriterV1 _addLocalClippingDataToMetadata:statistics:geometryData:].cold.1
+ +[LTMMetadataWriterV1 _addLocalHistToMetadata:statistics:geometryData:]
+ +[LTMMetadataWriterV1 _addLocalHistToMetadata:statistics:geometryData:].cold.1
+ +[LTMMetadataWriterV1 _addSoftDGainToMetadata:driverInputMetadata:]
+ +[LTMMetadataWriterV1 _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:]
+ +[LTMMetadataWriterV1 _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:].cold.1
+ +[LTMMetadataWriterV1 _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:].cold.2
+ +[LTMMetadataWriterV1 addLTMMetadataTo:curvesType:fromLTMOutput:statistics:driverInputMetadata:geometryData:]
+ +[LTMMetadataWriterV1 createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:]
+ +[LTMMetadataWriterV1 createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:].cold.1
+ +[LTMMetadataWriterV2 _addAverageLTMToMetadata:curvesType:fromOutput:ltcNumNodes:]
+ +[LTMMetadataWriterV2 _addGlobalLTMLookUpTableAlignedToFinalCropRect:]
+ +[LTMMetadataWriterV2 _addHazeCorrection:driverInputMetadata:]
+ +[LTMMetadataWriterV2 _addHighlightCompression:driverInputMetadata:]
+ +[LTMMetadataWriterV2 _addLTMCurveTypeToMetadata:driverInputMetadata:]
+ +[LTMMetadataWriterV2 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:ltcNumNodes:]
+ +[LTMMetadataWriterV2 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:ltcNumNodes:].cold.1
+ +[LTMMetadataWriterV2 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:ltcNumNodes:].cold.2
+ +[LTMMetadataWriterV2 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:ltcNumNodes:].cold.3
+ +[LTMMetadataWriterV2 _addLTMEnabledToMetadata:]
+ +[LTMMetadataWriterV2 _addLocalClippingDataToMetadata:statistics:geometryData:]
+ +[LTMMetadataWriterV2 _addLocalClippingDataToMetadata:statistics:geometryData:].cold.1
+ +[LTMMetadataWriterV2 _addLocalHistToMetadata:statistics:geometryData:]
+ +[LTMMetadataWriterV2 _addLocalHistToMetadata:statistics:geometryData:].cold.1
+ +[LTMMetadataWriterV2 _addSoftDGainToMetadata:driverInputMetadata:]
+ +[LTMMetadataWriterV2 _addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:]
+ +[LTMMetadataWriterV2 _addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:].cold.1
+ +[LTMMetadataWriterV2 _addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:].cold.2
+ +[LTMMetadataWriterV2 addLTMMetadataTo:curvesType:fromLTMOutput:statistics:driverInputMetadata:geometryData:]
+ +[LTMMetadataWriterV2 createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:]
+ +[LTMMetadataWriterV2 createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:].cold.1
+ -[AWBAlgorithm process].cold.2
+ -[AWBAlgorithm setTileStatsROIRect:]
+ -[AWBAlgorithm tileStatsROIRect]
+ -[AWBIBPParams lscModulationWeight]
+ -[AWBIBPParams setLscModulationWeight:]
+ -[AWBProcessor prepareToProcess:].cold.1
+ -[AWBProcessor prepareToProcess:].cold.2
+ -[AWBProcessor prepareToProcess:].cold.3
+ -[AWBProcessor prepareToProcess:].cold.4
+ -[AWBProcessor prepareToProcess:].cold.5
+ -[AWBProcessor prepareToProcess:].cold.6
+ -[AWBProcessor prepareToProcess:].cold.7
+ -[AWBProcessor prepareToProcess:].cold.8
+ -[AWBProcessor process].cold.1
+ -[AWBProcessor process].cold.2
+ -[AWBProcessor process].cold.3
+ -[AWBProcessor process].cold.4
+ -[AWBProcessor process].cold.5
+ -[AWBProcessor process].cold.6
+ -[AWBProcessor process].cold.7
+ -[AWBStatistics lscModulationWeight]
+ -[AWBStatistics setLscModulationWeight:]
+ -[AdaptiveGain .cxx_destruct]
+ -[AdaptiveGain allocInternalData]
+ -[AdaptiveGain allocInternalData].cold.1
+ -[AdaptiveGain computeGain:withTargetRange:]
+ -[AdaptiveGain computeGain:withTargetRange:].cold.1
+ -[AdaptiveGain computeGain:withTargetRange:].cold.2
+ -[AdaptiveGain configure]
+ -[AdaptiveGain createShaders]
+ -[AdaptiveGain createShaders].cold.1
+ -[AdaptiveGain initWithMetalContext:]
+ -[AdaptiveGain initWithMetalContext:].cold.1
+ -[AdaptiveGain initWithMetalContext:].cold.2
+ -[AdaptiveGain initWithMetalContext:].cold.3
+ -[AdaptiveGain inputRGBTexture]
+ -[AdaptiveGain releaseTextures]
+ -[AdaptiveGain setInputRGBTexture:]
+ -[HazeEstimation initWithMetalContext:].cold.1
+ -[HazeEstimation initWithMetalContext:].cold.2
+ -[HazeEstimation initWithMetalContext:].cold.3
+ -[HazeEstimation initWithMetalContext:].cold.4
+ -[HazeEstimation run].cold.1
+ -[HazeEstimation run].cold.2
+ -[HazeEstimation run].cold.3
+ -[LTMComputeRefV1 computeLTM:withMetadata:to:]
+ -[LTMComputeRefV1 init]
+ -[LTMComputeRefV2 computeLTM:withMetadata:to:]
+ -[LTMComputeRefV2 init]
+ -[LTMCurvesComputeV1 .cxx_destruct]
+ -[LTMCurvesComputeV1 compute]
+ -[LTMCurvesComputeV1 compute].cold.1
+ -[LTMCurvesComputeV1 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:]
+ -[LTMCurvesComputeV1 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:].cold.1
+ -[LTMCurvesComputeV1 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:].cold.2
+ -[LTMCurvesComputeV1 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:].cold.3
+ -[LTMCurvesComputeV2 .cxx_destruct]
+ -[LTMCurvesComputeV2 compute]
+ -[LTMCurvesComputeV2 compute].cold.1
+ -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:]
+ -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:].cold.1
+ -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:].cold.2
+ -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:].cold.3
+ -[LTMDriverRefV1 computeLtmComputeInput:withMetadata:to:computeInputMetadata:]
+ -[LTMDriverRefV1 dealloc]
+ -[LTMDriverRefV1 init]
+ -[LTMDriverRefV2 computeLtmComputeInput:withMetadata:to:computeInputMetadata:]
+ -[LTMDriverRefV2 dealloc]
+ -[LTMDriverRefV2 init]
+ -[LTMExtractMetadataV1 extractFrom:toDriverInput:ltmGeometry:]
+ -[LTMExtractMetadataV1 extractHRGainDownRatioFrom:]
+ -[LTMExtractMetadataV1 init]
+ -[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:]
+ -[LTMExtractMetadataV2 extractHRGainDownRatioFrom:]
+ -[LTMExtractMetadataV2 init]
+ -[LTMGeometryDataV1 copyWithZone:]
+ -[LTMGeometryDataV1 cropRect]
+ -[LTMGeometryDataV1 deepZoomOrigin]
+ -[LTMGeometryDataV1 initWithInputTextureWidth:height:]
+ -[LTMGeometryDataV1 initWithInputTextureWidth:height:].cold.1
+ -[LTMGeometryDataV1 initWithInputTextureWidth:height:].cold.2
+ -[LTMGeometryDataV1 inputTextureDownsampleRatio]
+ -[LTMGeometryDataV1 inputTextureSize]
+ -[LTMGeometryDataV1 setCropRect:sourceRect:]
+ -[LTMGeometryDataV1 setDeepZoomOrigin:]
+ -[LTMGeometryDataV1 setInputTextureDownsampleRatio:]
+ -[LTMGeometryDataV1 sourceRect]
+ -[LTMGeometryDataV2 copyWithZone:]
+ -[LTMGeometryDataV2 cropRect]
+ -[LTMGeometryDataV2 deepZoomOrigin]
+ -[LTMGeometryDataV2 deepZoomRatio]
+ -[LTMGeometryDataV2 initWithInputTextureWidth:height:]
+ -[LTMGeometryDataV2 initWithInputTextureWidth:height:].cold.1
+ -[LTMGeometryDataV2 initWithInputTextureWidth:height:].cold.2
+ -[LTMGeometryDataV2 inputTextureDownsampleRatio]
+ -[LTMGeometryDataV2 inputTextureSize]
+ -[LTMGeometryDataV2 rawSensorHeight]
+ -[LTMGeometryDataV2 rawSensorWidth]
+ -[LTMGeometryDataV2 sensorSpaceToValidBufferSpaceTransform]
+ -[LTMGeometryDataV2 setCropRect:sourceRect:]
+ -[LTMGeometryDataV2 setDeepZoomOrigin:]
+ -[LTMGeometryDataV2 setDeepZoomRatio:]
+ -[LTMGeometryDataV2 setInputTextureDownsampleRatio:]
+ -[LTMGeometryDataV2 setRawSensorHeight:]
+ -[LTMGeometryDataV2 setRawSensorWidth:]
+ -[LTMGeometryDataV2 setSensorSpaceToValidBufferSpaceTransform:]
+ -[LTMGeometryDataV2 sourceRect]
+ -[LTMIBPParams computeHDRCurvesWoFaceBoost]
+ -[LTMIBPParams inputBufferRect]
+ -[LTMIBPParams minimumAdaptiveHC_SIFR]
+ -[LTMIBPParams setComputeHDRCurvesWoFaceBoost:]
+ -[LTMIBPParams setInputBufferRect:]
+ -[LTMIBPParams setMinimumAdaptiveHC_SIFR:]
+ -[LTMIBPParams setUndoHRGainDownRatio:]
+ -[LTMIBPParams undoHRGainDownRatio]
+ -[LTMProcessor _compressHighlight:].cold.1
+ -[LTMProcessor _compressHighlight:].cold.2
+ -[LTMProcessor _compressHighlight:].cold.3
+ -[LTMProcessor _compressHighlight:].cold.4
+ -[LTMProcessor _compressHighlight:].cold.5
+ -[LTMProcessor _printDefaultsLTMparam]
+ -[LTMProcessor createLTMInTextureFromLuma:chroma:].cold.1
+ -[LTMProcessor createLTMInTextureFromLuma:chroma:].cold.2
+ -[LTMProcessor createLTMInTextureFromLuma:chroma:].cold.3
+ -[LTMProcessor createLTMInTextureFromRGBAFloatTex:undoScaleDown:]
+ -[LTMProcessor createLTMInTextureFromRGBAFloatTex:undoScaleDown:].cold.1
+ -[LTMProcessor createLTMInTextureFromRGBAFloatTex:undoScaleDown:].cold.2
+ -[LTMProcessor generateLinearRGBATexture:]
+ -[LTMProcessor generateLinearRGBATexture:].cold.1
+ -[LTMProcessor generateLinearRGBATexture:].cold.2
+ -[LTMProcessor generateLinearRGBATexture:].cold.3
+ -[LTMProcessor process].cold.1
+ -[LTMProcessor process].cold.10
+ -[LTMProcessor process].cold.11
+ -[LTMProcessor process].cold.12
+ -[LTMProcessor process].cold.13
+ -[LTMProcessor process].cold.14
+ -[LTMProcessor process].cold.2
+ -[LTMProcessor process].cold.3
+ -[LTMProcessor process].cold.4
+ -[LTMProcessor process].cold.5
+ -[LTMProcessor process].cold.6
+ -[LTMProcessor process].cold.7
+ -[LTMProcessor process].cold.8
+ -[LTMProcessor process].cold.9
+ -[LTMStats calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:]
+ -[LTMStats calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:].cold.1
+ -[LTMStats calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:].cold.2
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:]
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.1
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.2
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.3
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.4
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.5
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.6
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.7
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.8
+ -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:]
+ -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:].cold.1
+ -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:].cold.2
+ -[LTMStatsCompute createShaders:].cold.6
+ -[LTMStatsCompute createShaders:].cold.7
+ -[LTMStatsCompute createShaders:].cold.8
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:]
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.1
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.10
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.11
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.2
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.3
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.4
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.5
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.6
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.7
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.8
+ -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:].cold.9
+ -[LTMStatsCompute initWithMetalContext:].cold.1
+ -[LTMStatsCompute initWithMetalContext:].cold.2
+ GCC_except_table44
+ _CGAffineTransformIdentity
+ _CGAffineTransformInvert
+ _CGAffineTransformScale
+ _CGAffineTransformTranslate
+ _CGRectApplyAffineTransform
+ _CGRectCreateDictionaryRepresentation
+ _CGRectIsEmpty
+ _CGRectIsNull
+ _CGRectZero
+ _FigDebugAssert3
+ _GeometryUtilitiesGetFinalCropRect
+ _GeometryUtilitiesNormalizeCropRect
+ _OBJC_CLASS_$_AdaptiveGain
+ _OBJC_CLASS_$_GeometryUtilities
+ _OBJC_CLASS_$_LTMComputeRefV1
+ _OBJC_CLASS_$_LTMComputeRefV2
+ _OBJC_CLASS_$_LTMCurvesComputeV1
+ _OBJC_CLASS_$_LTMCurvesComputeV2
+ _OBJC_CLASS_$_LTMDriverRefV1
+ _OBJC_CLASS_$_LTMDriverRefV2
+ _OBJC_CLASS_$_LTMExtractMetadataV1
+ _OBJC_CLASS_$_LTMExtractMetadataV2
+ _OBJC_CLASS_$_LTMGeometryDataV1
+ _OBJC_CLASS_$_LTMGeometryDataV2
+ _OBJC_CLASS_$_LTMMetadataWriterV1
+ _OBJC_CLASS_$_LTMMetadataWriterV2
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_IVAR_$_AWBAlgorithm._tileStatsROIRect
+ _OBJC_IVAR_$_AWBIBPParams._lscModulationWeight
+ _OBJC_IVAR_$_AWBStatistics._lscModulationWeight
+ _OBJC_IVAR_$_AdaptiveGain._adaptiveGainValue
+ _OBJC_IVAR_$_AdaptiveGain._computePipelineHistogramGeneration
+ _OBJC_IVAR_$_AdaptiveGain._globalHistBuffer
+ _OBJC_IVAR_$_AdaptiveGain._inputRGBTexture
+ _OBJC_IVAR_$_AdaptiveGain._lumaParams
+ _OBJC_IVAR_$_AdaptiveGain._metalContext
+ _OBJC_IVAR_$_LTMComputeRefV1._ltmCompute
+ _OBJC_IVAR_$_LTMComputeRefV2._ltmCompute
+ _OBJC_IVAR_$_LTMCurvesComputeV1._computeCurvesWoFaceBoost
+ _OBJC_IVAR_$_LTMCurvesComputeV1._computeHDRCurves
+ _OBJC_IVAR_$_LTMCurvesComputeV1._computeHDRCurvesWoFaceBoost
+ _OBJC_IVAR_$_LTMCurvesComputeV1._computeInputs
+ _OBJC_IVAR_$_LTMCurvesComputeV1._computeInputsMetadata
+ _OBJC_IVAR_$_LTMCurvesComputeV1._computeLTM
+ _OBJC_IVAR_$_LTMCurvesComputeV1._computeOutput
+ _OBJC_IVAR_$_LTMCurvesComputeV1._driverInputMetadata
+ _OBJC_IVAR_$_LTMCurvesComputeV1._driverLTM
+ _OBJC_IVAR_$_LTMCurvesComputeV1._geometryData
+ _OBJC_IVAR_$_LTMCurvesComputeV1._globalHistStat
+ _OBJC_IVAR_$_LTMCurvesComputeV1._isDigitalFlash
+ _OBJC_IVAR_$_LTMCurvesComputeV1._localHistStat
+ _OBJC_IVAR_$_LTMCurvesComputeV1._ltmStats
+ _OBJC_IVAR_$_LTMCurvesComputeV1._optimized
+ _OBJC_IVAR_$_LTMCurvesComputeV1._procHITHStat
+ _OBJC_IVAR_$_LTMCurvesComputeV1._thumbnailStat
+ _OBJC_IVAR_$_LTMCurvesComputeV2._computeCurvesWoFaceBoost
+ _OBJC_IVAR_$_LTMCurvesComputeV2._computeHDRCurves
+ _OBJC_IVAR_$_LTMCurvesComputeV2._computeHDRCurvesWoFaceBoost
+ _OBJC_IVAR_$_LTMCurvesComputeV2._computeInputs
+ _OBJC_IVAR_$_LTMCurvesComputeV2._computeInputsMetadata
+ _OBJC_IVAR_$_LTMCurvesComputeV2._computeLTM
+ _OBJC_IVAR_$_LTMCurvesComputeV2._computeOutput
+ _OBJC_IVAR_$_LTMCurvesComputeV2._driverInputMetadata
+ _OBJC_IVAR_$_LTMCurvesComputeV2._driverLTM
+ _OBJC_IVAR_$_LTMCurvesComputeV2._enableCB
+ _OBJC_IVAR_$_LTMCurvesComputeV2._enableFATE
+ _OBJC_IVAR_$_LTMCurvesComputeV2._enableHiResLocalHistogram
+ _OBJC_IVAR_$_LTMCurvesComputeV2._geometryData
+ _OBJC_IVAR_$_LTMCurvesComputeV2._globalFaceHistStat
+ _OBJC_IVAR_$_LTMCurvesComputeV2._globalHistStat
+ _OBJC_IVAR_$_LTMCurvesComputeV2._isDigitalFlash
+ _OBJC_IVAR_$_LTMCurvesComputeV2._localHistStat
+ _OBJC_IVAR_$_LTMCurvesComputeV2._ltmStats
+ _OBJC_IVAR_$_LTMCurvesComputeV2._optimized
+ _OBJC_IVAR_$_LTMCurvesComputeV2._procHITHStat
+ _OBJC_IVAR_$_LTMCurvesComputeV2._thumbnailStat
+ _OBJC_IVAR_$_LTMDriverRefV1._ltmDriver
+ _OBJC_IVAR_$_LTMDriverRefV2._ltmDriver
+ _OBJC_IVAR_$_LTMExtractMetadataV1._faceBiasScaler
+ _OBJC_IVAR_$_LTMExtractMetadataV1._faceBiasScalerMin
+ _OBJC_IVAR_$_LTMExtractMetadataV1._faceBiasThreshold
+ _OBJC_IVAR_$_LTMExtractMetadataV1._faceBiasThresholdMin
+ _OBJC_IVAR_$_LTMExtractMetadataV1._forceDisableHR
+ _OBJC_IVAR_$_LTMExtractMetadataV1._forceDisableLTMFaceBoost
+ _OBJC_IVAR_$_LTMExtractMetadataV1._forceDisableLTMFaceExposureRatio
+ _OBJC_IVAR_$_LTMExtractMetadataV1._forceDisableLTMHazeCorrection
+ _OBJC_IVAR_$_LTMExtractMetadataV1._forceHighlightCompressionForEveryFrame
+ _OBJC_IVAR_$_LTMExtractMetadataV1._forceUseBt709
+ _OBJC_IVAR_$_LTMExtractMetadataV2._faceBiasScaler
+ _OBJC_IVAR_$_LTMExtractMetadataV2._faceBiasScalerMin
+ _OBJC_IVAR_$_LTMExtractMetadataV2._faceBiasThreshold
+ _OBJC_IVAR_$_LTMExtractMetadataV2._faceBiasThresholdMin
+ _OBJC_IVAR_$_LTMExtractMetadataV2._forceDisableHR
+ _OBJC_IVAR_$_LTMExtractMetadataV2._forceDisableLTMFaceBoost
+ _OBJC_IVAR_$_LTMExtractMetadataV2._forceDisableLTMFaceExposureRatio
+ _OBJC_IVAR_$_LTMExtractMetadataV2._forceDisableLTMHazeCorrection
+ _OBJC_IVAR_$_LTMExtractMetadataV2._forceHighlightCompressionForEveryFrame
+ _OBJC_IVAR_$_LTMExtractMetadataV2._forceUseBt709
+ _OBJC_IVAR_$_LTMGeometryDataV1._cropRect
+ _OBJC_IVAR_$_LTMGeometryDataV1._deepZoomOrigin
+ _OBJC_IVAR_$_LTMGeometryDataV1._inputTextureDownsampleRatio
+ _OBJC_IVAR_$_LTMGeometryDataV1._inputTextureRect
+ _OBJC_IVAR_$_LTMGeometryDataV1._inputTextureSize
+ _OBJC_IVAR_$_LTMGeometryDataV1._minimumRect
+ _OBJC_IVAR_$_LTMGeometryDataV1._sourceRect
+ _OBJC_IVAR_$_LTMGeometryDataV2._cropRect
+ _OBJC_IVAR_$_LTMGeometryDataV2._deepZoomOrigin
+ _OBJC_IVAR_$_LTMGeometryDataV2._deepZoomRatio
+ _OBJC_IVAR_$_LTMGeometryDataV2._inputTextureDownsampleRatio
+ _OBJC_IVAR_$_LTMGeometryDataV2._inputTextureRect
+ _OBJC_IVAR_$_LTMGeometryDataV2._inputTextureSize
+ _OBJC_IVAR_$_LTMGeometryDataV2._minimumRect
+ _OBJC_IVAR_$_LTMGeometryDataV2._rawSensorHeight
+ _OBJC_IVAR_$_LTMGeometryDataV2._rawSensorWidth
+ _OBJC_IVAR_$_LTMGeometryDataV2._sensorSpaceToValidBufferSpaceTransform
+ _OBJC_IVAR_$_LTMGeometryDataV2._sourceRect
+ _OBJC_IVAR_$_LTMIBPParams._computeHDRCurvesWoFaceBoost
+ _OBJC_IVAR_$_LTMIBPParams._inputBufferRect
+ _OBJC_IVAR_$_LTMIBPParams._minimumAdaptiveHC_SIFR
+ _OBJC_IVAR_$_LTMIBPParams._undoHRGainDownRatio
+ _OBJC_IVAR_$_LTMProcessor._adaptiveGain
+ _OBJC_IVAR_$_LTMProcessor._adaptiveGainMax
+ _OBJC_IVAR_$_LTMProcessor._adaptiveGainRange
+ _OBJC_IVAR_$_LTMProcessor._enableAdaptiveGain
+ _OBJC_IVAR_$_LTMProcessor._enableCB
+ _OBJC_IVAR_$_LTMProcessor._enableDualLTC
+ _OBJC_IVAR_$_LTMProcessor._enableFATE
+ _OBJC_IVAR_$_LTMProcessor._enableHiResLocalHistogram
+ _OBJC_IVAR_$_LTMProcessor.globalFaceHistStat
+ _OBJC_IVAR_$_LTMStats._globalFaceHistBuffer
+ _OBJC_IVAR_$_LTMStatsCompute._collectLocalHistHiResKernelPipelineState
+ _OBJC_IVAR_$_LTMStatsCompute._globalFaceHistKernelPipelineState
+ _OBJC_IVAR_$_LTMStatsCompute._localHistHiResAndThumKernelPipelineState
+ _OBJC_METACLASS_$_AdaptiveGain
+ _OBJC_METACLASS_$_GeometryUtilities
+ _OBJC_METACLASS_$_LTMComputeRefV1
+ _OBJC_METACLASS_$_LTMComputeRefV2
+ _OBJC_METACLASS_$_LTMCurvesComputeV1
+ _OBJC_METACLASS_$_LTMCurvesComputeV2
+ _OBJC_METACLASS_$_LTMDriverRefV1
+ _OBJC_METACLASS_$_LTMDriverRefV2
+ _OBJC_METACLASS_$_LTMExtractMetadataV1
+ _OBJC_METACLASS_$_LTMExtractMetadataV2
+ _OBJC_METACLASS_$_LTMGeometryDataV1
+ _OBJC_METACLASS_$_LTMGeometryDataV2
+ _OBJC_METACLASS_$_LTMMetadataWriterV1
+ _OBJC_METACLASS_$_LTMMetadataWriterV2
+ _UNAGI_NOTE_VARIABLE
+ __OBJC_$_CLASS_METHODS_AWBStatistics
+ __OBJC_$_CLASS_METHODS_GeometryUtilities
+ __OBJC_$_CLASS_METHODS_LTMExtractMetadataV1
+ __OBJC_$_CLASS_METHODS_LTMExtractMetadataV2
+ __OBJC_$_CLASS_METHODS_LTMMetadataWriterV1
+ __OBJC_$_CLASS_METHODS_LTMMetadataWriterV2
+ __OBJC_$_INSTANCE_METHODS_AdaptiveGain
+ __OBJC_$_INSTANCE_METHODS_LTMComputeRefV1
+ __OBJC_$_INSTANCE_METHODS_LTMComputeRefV2
+ __OBJC_$_INSTANCE_METHODS_LTMCurvesComputeV1
+ __OBJC_$_INSTANCE_METHODS_LTMCurvesComputeV2
+ __OBJC_$_INSTANCE_METHODS_LTMDriverRefV1
+ __OBJC_$_INSTANCE_METHODS_LTMDriverRefV2
+ __OBJC_$_INSTANCE_METHODS_LTMExtractMetadataV1
+ __OBJC_$_INSTANCE_METHODS_LTMExtractMetadataV2
+ __OBJC_$_INSTANCE_METHODS_LTMGeometryDataV1
+ __OBJC_$_INSTANCE_METHODS_LTMGeometryDataV2
+ __OBJC_$_INSTANCE_VARIABLES_AdaptiveGain
+ __OBJC_$_INSTANCE_VARIABLES_LTMComputeRefV1
+ __OBJC_$_INSTANCE_VARIABLES_LTMComputeRefV2
+ __OBJC_$_INSTANCE_VARIABLES_LTMCurvesComputeV1
+ __OBJC_$_INSTANCE_VARIABLES_LTMCurvesComputeV2
+ __OBJC_$_INSTANCE_VARIABLES_LTMDriverRefV1
+ __OBJC_$_INSTANCE_VARIABLES_LTMDriverRefV2
+ __OBJC_$_INSTANCE_VARIABLES_LTMExtractMetadataV1
+ __OBJC_$_INSTANCE_VARIABLES_LTMExtractMetadataV2
+ __OBJC_$_INSTANCE_VARIABLES_LTMGeometryDataV1
+ __OBJC_$_INSTANCE_VARIABLES_LTMGeometryDataV2
+ __OBJC_$_PROP_LIST_AWBIBPParams.197
+ __OBJC_$_PROP_LIST_AdaptiveGain
+ __OBJC_$_PROP_LIST_LTMComputeRefV1
+ __OBJC_$_PROP_LIST_LTMComputeRefV2
+ __OBJC_$_PROP_LIST_LTMDriverRefV1
+ __OBJC_$_PROP_LIST_LTMDriverRefV2
+ __OBJC_$_PROP_LIST_LTMExtractMetadataV1
+ __OBJC_$_PROP_LIST_LTMExtractMetadataV2
+ __OBJC_$_PROP_LIST_LTMGeometryDataBase
+ __OBJC_$_PROP_LIST_LTMGeometryDataV1
+ __OBJC_$_PROP_LIST_LTMGeometryDataV2
+ __OBJC_$_PROP_LIST_LTMIBPParams.212
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LTMComputeBaseV1
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LTMComputeBaseV2
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LTMDriverBaseV1
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LTMDriverBaseV2
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LTMExtractMetadataBase
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LTMGeometryDataBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LTMComputeBaseV1
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LTMComputeBaseV2
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LTMDriverBaseV1
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LTMDriverBaseV2
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LTMExtractMetadataBase
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LTMGeometryDataBase
+ __OBJC_$_PROTOCOL_REFS_LTMComputeBaseV1
+ __OBJC_$_PROTOCOL_REFS_LTMComputeBaseV2
+ __OBJC_$_PROTOCOL_REFS_LTMDriverBaseV1
+ __OBJC_$_PROTOCOL_REFS_LTMDriverBaseV2
+ __OBJC_$_PROTOCOL_REFS_LTMExtractMetadataBase
+ __OBJC_$_PROTOCOL_REFS_LTMGeometryDataBase
+ __OBJC_CLASS_PROTOCOLS_$_LTMComputeRefV1
+ __OBJC_CLASS_PROTOCOLS_$_LTMComputeRefV2
+ __OBJC_CLASS_PROTOCOLS_$_LTMCurvesComputeV1
+ __OBJC_CLASS_PROTOCOLS_$_LTMCurvesComputeV2
+ __OBJC_CLASS_PROTOCOLS_$_LTMDriverRefV1
+ __OBJC_CLASS_PROTOCOLS_$_LTMDriverRefV2
+ __OBJC_CLASS_PROTOCOLS_$_LTMExtractMetadataV1
+ __OBJC_CLASS_PROTOCOLS_$_LTMExtractMetadataV2
+ __OBJC_CLASS_PROTOCOLS_$_LTMGeometryDataV1
+ __OBJC_CLASS_PROTOCOLS_$_LTMGeometryDataV2
+ __OBJC_CLASS_RO_$_AdaptiveGain
+ __OBJC_CLASS_RO_$_GeometryUtilities
+ __OBJC_CLASS_RO_$_LTMComputeRefV1
+ __OBJC_CLASS_RO_$_LTMComputeRefV2
+ __OBJC_CLASS_RO_$_LTMCurvesComputeV1
+ __OBJC_CLASS_RO_$_LTMCurvesComputeV2
+ __OBJC_CLASS_RO_$_LTMDriverRefV1
+ __OBJC_CLASS_RO_$_LTMDriverRefV2
+ __OBJC_CLASS_RO_$_LTMExtractMetadataV1
+ __OBJC_CLASS_RO_$_LTMExtractMetadataV2
+ __OBJC_CLASS_RO_$_LTMGeometryDataV1
+ __OBJC_CLASS_RO_$_LTMGeometryDataV2
+ __OBJC_CLASS_RO_$_LTMMetadataWriterV1
+ __OBJC_CLASS_RO_$_LTMMetadataWriterV2
+ __OBJC_LABEL_PROTOCOL_$_LTMComputeBaseV1
+ __OBJC_LABEL_PROTOCOL_$_LTMComputeBaseV2
+ __OBJC_LABEL_PROTOCOL_$_LTMDriverBaseV1
+ __OBJC_LABEL_PROTOCOL_$_LTMDriverBaseV2
+ __OBJC_LABEL_PROTOCOL_$_LTMExtractMetadataBase
+ __OBJC_LABEL_PROTOCOL_$_LTMGeometryDataBase
+ __OBJC_METACLASS_RO_$_AdaptiveGain
+ __OBJC_METACLASS_RO_$_GeometryUtilities
+ __OBJC_METACLASS_RO_$_LTMComputeRefV1
+ __OBJC_METACLASS_RO_$_LTMComputeRefV2
+ __OBJC_METACLASS_RO_$_LTMCurvesComputeV1
+ __OBJC_METACLASS_RO_$_LTMCurvesComputeV2
+ __OBJC_METACLASS_RO_$_LTMDriverRefV1
+ __OBJC_METACLASS_RO_$_LTMDriverRefV2
+ __OBJC_METACLASS_RO_$_LTMExtractMetadataV1
+ __OBJC_METACLASS_RO_$_LTMExtractMetadataV2
+ __OBJC_METACLASS_RO_$_LTMGeometryDataV1
+ __OBJC_METACLASS_RO_$_LTMGeometryDataV2
+ __OBJC_METACLASS_RO_$_LTMMetadataWriterV1
+ __OBJC_METACLASS_RO_$_LTMMetadataWriterV2
+ __OBJC_PROTOCOL_$_LTMComputeBaseV1
+ __OBJC_PROTOCOL_$_LTMComputeBaseV2
+ __OBJC_PROTOCOL_$_LTMDriverBaseV1
+ __OBJC_PROTOCOL_$_LTMDriverBaseV2
+ __OBJC_PROTOCOL_$_LTMExtractMetadataBase
+ __OBJC_PROTOCOL_$_LTMGeometryDataBase
+ __ZL13configTilesV2P18AWBTileStatsConfigPK12NSDictionary
+ __ZL32_configTilesRuntimeWithValidRectP18AWBTileStatsConfigRK6CGRect
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.1
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.2
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.3
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.4
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.5
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.6
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.7
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.8
+ __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.9
+ __ZL45_configStatsDownsizeRatioRuntimeWithValidRectP14AWBStatsConfigPK12NSDictionaryj
+ __ZL46_configStatsROIRuntimeWithRegionOfInterestRectP14AWBStatsConfigPK12NSDictionaryS3_R6CGRect
+ __ZN10AuxCompute17CalcExposureRatioEPK24sRefDriverInputs_SOFTISP
+ __ZN10AuxCompute17CalcTotalGainDownEPK24sRefDriverInputs_SOFTISP
+ __ZN10AuxCompute21CalcLTMspatialCCMSizeEPK7sBTRectbP24sLTMSpatialCCMSizeConfig
+ __ZN10AuxCompute24CalcAntiAliasingSettingsEPbPjS1_P24sRefDriverInputs_SOFTISP
+ __ZN11LTMDriverV19LTMDriver11defaultHistE
+ __ZN11LTMDriverV19LTMDriver18GamutBoundaryRatioEPK24sCLRProcHITHStat_SOFTISP
+ __ZN11LTMDriverV19LTMDriver22ComputeGlobalHistogramEPK24sCLRProcHITHStat_SOFTISPP16sLtmComputeInput
+ __ZN11LTMDriverV19LTMDriver22ComputeLocalHistogramsEPK24sCLRProcHITHStat_SOFTISPP16sLtmComputeInput
+ __ZN11LTMDriverV19LTMDriver22UpdateColorInformationEP16sLtmComputeInputPK24sRefDriverInputs_SOFTISPPK24sCLRProcHITHStat_SOFTISP
+ __ZN11LTMDriverV19LTMDriver24ComputeLumaFromThumbnailEPK24sCLRProcHITHStat_SOFTISPfP16sLtmComputeInput
+ __ZN11LTMDriverV19LTMDriver24computeFaceWeightForToneEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput
+ __ZN11LTMDriverV19LTMDriver25ComputeThumbnailHistogramEPK24sCLRProcHITHStat_SOFTISPfP16sLtmComputeInput
+ __ZN11LTMDriverV19LTMDriver26ComputeSpatialCCMWeightMapEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput
+ __ZN11LTMDriverV19LTMDriver28HFFThumbnailDownscaleConvertEPK24sCLRProcHITHStat_SOFTISPP16sLtmComputeInput
+ __ZN11LTMDriverV19LTMDriver39CalculateSpatialCCMWeightMapForLEDFlashEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput
+ __ZN11LTMDriverV19LTMDriver7ProcessEPK24sCLRProcHITHStat_SOFTISPPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput
+ __ZN11LTMDriverV19LTMDriverC1Ev
+ __ZN11LTMDriverV19LTMDriverD0Ev
+ __ZN11LTMDriverV19LTMDriverD1Ev
+ __ZN11LTMDriverV29LTMDriver10average3x3EPKfPfii
+ __ZN11LTMDriverV29LTMDriver11defaultHistE
+ __ZN11LTMDriverV29LTMDriver16calcBlendingMaskEPfPKfiib
+ __ZN11LTMDriverV29LTMDriver16defaultHistHiResE
+ __ZN11LTMDriverV29LTMDriver17computeFaceWeightEPK7sBTRectP16sLtmComputeInputPK11sCIspFDRectiPfPKif
+ __ZN11LTMDriverV29LTMDriver18GamutBoundaryRatioEPK24sCLRProcHITHStat_SOFTISP
+ __ZN11LTMDriverV29LTMDriver19UpdateLocalMetaDataEPK24sRefDriverInputs_SOFTISP
+ __ZN11LTMDriverV29LTMDriver22ComputeLocalHistogramsEPK24sCLRProcHITHStat_SOFTISPP16sLtmComputeInputf
+ __ZN11LTMDriverV29LTMDriver22UpdateColorInformationEP16sLtmComputeInputPK24sRefDriverInputs_SOFTISPPK24sCLRProcHITHStat_SOFTISP
+ __ZN11LTMDriverV29LTMDriver22computeGlobalHistogramEPKjPfttjj
+ __ZN11LTMDriverV29LTMDriver24ComputeLumaFromThumbnailEPK24sCLRProcHITHStat_SOFTISPffP16sLtmComputeInput
+ __ZN11LTMDriverV29LTMDriver25ComputeThumbnailHistogramEPK24sCLRProcHITHStat_SOFTISPffP16sLtmComputeInput
+ __ZN11LTMDriverV29LTMDriver26ComputeSpatialCCMWeightMapEPK24sRefDriverInputs_SOFTISPbP16sLtmComputeInput
+ __ZN11LTMDriverV29LTMDriver27computeFaceWeightForToneHFFEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput
+ __ZN11LTMDriverV29LTMDriver28HFFThumbnailDownscaleConvertEPK24sCLRProcHITHStat_SOFTISPP16sLtmComputeInputffi
+ __ZN11LTMDriverV29LTMDriver39CalculateSpatialCCMWeightMapForLEDFlashEPK24sRefDriverInputs_SOFTISPP16sLtmComputeInput
+ __ZN11LTMDriverV29LTMDriver7ProcessEPK24sCLRProcHITHStat_SOFTISPPK24sRefDriverInputs_SOFTISPP24sLtmComputeInput_SOFTISP
+ __ZN11LTMDriverV29LTMDriverC1Eb
+ __ZN11LTMDriverV29LTMDriverD0Ev
+ __ZN11LTMDriverV29LTMDriverD1Ev
+ __ZN12CEnvironment8InstanceEv
+ __ZN12LTMComputeV110LTMCompute11adaptForHLGEP17sLtmComputeOutput
+ __ZN12LTMComputeV110LTMCompute11defaultHistE
+ __ZN12LTMComputeV110LTMCompute11interpolateEPKfS2_iS2_Pfi
+ __ZN12LTMComputeV110LTMCompute11interpolateEPKfS2_iS2_Pfif
+ __ZN12LTMComputeV110LTMCompute11invExpLutX4E
+ __ZN12LTMComputeV110LTMCompute12allocateToneEPfS1_PKfPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPKNS_15sLtmFrameParamsES3_S3_S3_S3_S3_fffbb
+ __ZN12LTMComputeV110LTMCompute12makeScaleGTCEPfPKfff
+ __ZN12LTMComputeV110LTMCompute14levelSmoothHFFEPfPKfiii
+ __ZN12LTMComputeV110LTMCompute15scaleToFitRangeEPfPKfS3_S3_fS3_fS3_
+ __ZN12LTMComputeV110LTMCompute15tuningParamsHLGE
+ __ZN12LTMComputeV110LTMCompute15tuningParamsSDRE
+ __ZN12LTMComputeV110LTMCompute16computeLocalLumaEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPNS_15sLtmFrameParamsE
+ __ZN12LTMComputeV110LTMCompute16localCurveInputsE
+ __ZN12LTMComputeV110LTMCompute17HFFspatialMapCalcEiPKfPfS3_
+ __ZN12LTMComputeV110LTMCompute17generateLinearLTCEPK16sLtmComputeInputPK15sLtmComputeMetaP17sLtmComputeOutput
+ __ZN12LTMComputeV110LTMCompute17globalCurveInputsE
+ __ZN12LTMComputeV110LTMCompute18generateSpatialLTCEPK16sLtmComputeInputPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput
+ __ZN12LTMComputeV110LTMCompute19HFFHighFreqModulateEiiPfS1_S1_S1_S1_
+ __ZN12LTMComputeV110LTMCompute19HFFspatialMapFilterEiiPfPKf
+ __ZN12LTMComputeV110LTMCompute19calculateSceneFlareEPKfiPiffPfS4_S4_
+ __ZN12LTMComputeV110LTMCompute19calculateSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEPNS_15sLtmFrameParamsE
+ __ZN12LTMComputeV110LTMCompute19calculateSpatialCCMEPK16sLtmComputeInputPK15sLtmComputeMetaP17sLtmComputeOutput
+ __ZN12LTMComputeV110LTMCompute19computeRGBToneCurveEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEPKNS_15sLtmFrameParamsEP17sLtmComputeOutput
+ __ZN12LTMComputeV110LTMCompute20ccmWithNewWhitePointEPfPKfff
+ __ZN12LTMComputeV110LTMCompute20computeThumbnailLumaEPK16sLtmComputeInputPNS_15sLtmFrameParamsE
+ __ZN12LTMComputeV110LTMCompute21calculateDisplayModelEffPKfPf
+ __ZN12LTMComputeV110LTMCompute21smoothHistogramMiddleEPKfPfiS2_ib
+ __ZN12LTMComputeV110LTMCompute21uniformLocalHistogramE
+ __ZN12LTMComputeV110LTMCompute24tuningParamsDigitalFlashE
+ __ZN12LTMComputeV110LTMCompute27tuningParamsDigitalFlashFFCE
+ __ZN12LTMComputeV110LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPNS_15sLtmFrameParamsE
+ __ZN12LTMComputeV110LTMCompute38calculateGlobalLUTandModifySceneModelsEmPK16sLtmComputeInputPK15sLtmComputeMetaPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPNS_15sLtmFrameParamsEP17sLtmComputeOutput
+ __ZN12LTMComputeV110LTMCompute4gpreE
+ __ZN12LTMComputeV110LTMCompute7ProcessEPK16sLtmComputeInputPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput
+ __ZN12LTMComputeV110LTMCompute9liftedGTCE
+ __ZN12LTMComputeV110LTMComputeC1Ei
+ __ZN12LTMComputeV110LTMComputeD0Ev
+ __ZN12LTMComputeV110LTMComputeD1Ev
+ __ZN12LTMComputeV116sLtmTuningParams10nFlareBinsE
+ __ZN12LTMComputeV116sLtmTuningParams15desaturationCCME
+ __ZN12LTMComputeV116sLtmTuningParams22ltc3x3HorzFilterCoeffsE
+ __ZN12LTMComputeV116sLtmTuningParams22ltc3x3VertFilterCoeffsE
+ __ZN12LTMComputeV210LTMCompute10histInterpEPKfS2_iS2_PfiS3_b
+ __ZN12LTMComputeV210LTMCompute11adaptForHLGEP17sLtmComputeOutput
+ __ZN12LTMComputeV210LTMCompute11defaultHistE
+ __ZN12LTMComputeV210LTMCompute11globalHist2E
+ __ZN12LTMComputeV210LTMCompute11interpolateEPKfS2_iS2_Pfi
+ __ZN12LTMComputeV210LTMCompute11interpolateEPKfS2_iS2_Pfif
+ __ZN12LTMComputeV210LTMCompute11invExpLutX4E
+ __ZN12LTMComputeV210LTMCompute12allocateToneEPfS1_PKfPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPKNS_15sLtmFrameParamsES3_S3_S3_S3_S3_fffbb
+ __ZN12LTMComputeV210LTMCompute12makeScaleGTCEPfPKfff
+ __ZN12LTMComputeV210LTMCompute14levelSmoothHFFEPfPKfS3_iii
+ __ZN12LTMComputeV210LTMCompute15LTCGridCalcAlgoEPK16sLtmComputeInputPK15sLtmComputeMetaP17sLtmComputeOutputfPKfSA_fSA_ff
+ __ZN12LTMComputeV210LTMCompute15applyCBBlendingEPfPKffS3_f
+ __ZN12LTMComputeV210LTMCompute15scaleToFitRangeEPfPKfS3_S3_fS3_fS3_
+ __ZN12LTMComputeV210LTMCompute15tuningParamsHLGE
+ __ZN12LTMComputeV210LTMCompute15tuningParamsSDRE
+ __ZN12LTMComputeV210LTMCompute16computeLocalLumaEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPNS_15sLtmFrameParamsE
+ __ZN12LTMComputeV210LTMCompute16levelSmoothHFFCBEPfPKfS3_iii
+ __ZN12LTMComputeV210LTMCompute17HFFspatialMapCalcEiPKfPfS3_
+ __ZN12LTMComputeV210LTMCompute17generateLinearLTCEPK16sLtmComputeInputPK15sLtmComputeMetaP17sLtmComputeOutput
+ __ZN12LTMComputeV210LTMCompute17globalCurveInputsE
+ __ZN12LTMComputeV210LTMCompute18generateSpatialLTCEPK24sLtmComputeInput_SOFTISPPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput
+ __ZN12LTMComputeV210LTMCompute19HFFHighFreqModulateEiiPfS1_S1_S1_S1_S1_S1_
+ __ZN12LTMComputeV210LTMCompute19HFFspatialMapFilterEiiPfPKf
+ __ZN12LTMComputeV210LTMCompute19calculateSceneFlareEPKfiPiffPfS4_S4_
+ __ZN12LTMComputeV210LTMCompute19calculateSpatialCCMEPK16sLtmComputeInputPK15sLtmComputeMetaP17sLtmComputeOutput
+ __ZN12LTMComputeV210LTMCompute19computeRGBToneCurveEPK24sLtmComputeInput_SOFTISPPKNS_16sLtmTuningParamsEPKNS_15sLtmFrameParamsEP17sLtmComputeOutput
+ __ZN12LTMComputeV210LTMCompute20ccmWithNewWhitePointEPfPKfff
+ __ZN12LTMComputeV210LTMCompute20computeThumbnailLumaEPK16sLtmComputeInputPNS_15sLtmFrameParamsE
+ __ZN12LTMComputeV210LTMCompute21calculateDisplayModelEffPKfPf
+ __ZN12LTMComputeV210LTMCompute21smoothHistogramMiddleEPKfPfiS2_ib
+ __ZN12LTMComputeV210LTMCompute21toneCurveArrayIndicesE
+ __ZN12LTMComputeV210LTMCompute23calculateSceneModelAlgoEPfS1_PK16sLtmComputeInputPKNS_16sLtmTuningParamsEPNS_15sLtmFrameParamsEffPKf
+ __ZN12LTMComputeV210LTMCompute24tuningParamsDigitalFlashE
+ __ZN12LTMComputeV210LTMCompute25upsampleHFFInterpsIndicesE
+ __ZN12LTMComputeV210LTMCompute27tuningParamsDigitalFlashFFCE
+ __ZN12LTMComputeV210LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPNS_15sLtmFrameParamsE14eLTMSceneModel
+ __ZN12LTMComputeV210LTMCompute38calculateGlobalLUTandModifySceneModelsEmPK16sLtmComputeInputPK15sLtmComputeMetaPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPNS_15sLtmFrameParamsEP17sLtmComputeOutput
+ __ZN12LTMComputeV210LTMCompute4InitEv
+ __ZN12LTMComputeV210LTMCompute4gpreE
+ __ZN12LTMComputeV210LTMCompute7ProcessEPK24sLtmComputeInput_SOFTISPPK23sLtmComputeMeta_SOFTISPP17sLtmComputeOutput
+ __ZN12LTMComputeV210LTMCompute9liftedGTCE
+ __ZN12LTMComputeV210LTMComputeC1Eib
+ __ZN12LTMComputeV210LTMComputeD0Ev
+ __ZN12LTMComputeV210LTMComputeD1Ev
+ __ZN12LTMComputeV216sLtmTuningParams10nFlareBinsE
+ __ZN12LTMComputeV216sLtmTuningParams14faceBiasScalerE
+ __ZN12LTMComputeV216sLtmTuningParams15desaturationCCME
+ __ZN12LTMComputeV216sLtmTuningParams22ltc3x3HorzFilterCoeffsE
+ __ZN12LTMComputeV216sLtmTuningParams22ltc3x3VertFilterCoeffsE
+ __ZN7CAWBAFE21GetMixedLightingScoreEPf
+ __ZN7CAWBAFE9GetSkyCCTEPj
+ __ZTIN11LTMDriverV19LTMDriverE
+ __ZTIN11LTMDriverV29LTMDriverE
+ __ZTIN12LTMComputeV110LTMComputeE
+ __ZTIN12LTMComputeV210LTMComputeE
+ __ZTSN11LTMDriverV19LTMDriverE
+ __ZTSN11LTMDriverV29LTMDriverE
+ __ZTSN12LTMComputeV110LTMComputeE
+ __ZTSN12LTMComputeV210LTMComputeE
+ __ZTVN11LTMDriverV19LTMDriverE
+ __ZTVN11LTMDriverV29LTMDriverE
+ __ZTVN12LTMComputeV110LTMComputeE
+ __ZTVN12LTMComputeV210LTMComputeE
+ __ZZN12LTMComputeV110LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPNS_15sLtmFrameParamsEE5bvec1
+ __ZZN12LTMComputeV110LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPNS_15sLtmFrameParamsEE5bvec2
+ __ZZN12LTMComputeV110LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPNS_15sLtmFrameParamsEE6xgHigh
+ __ZZN12LTMComputeV210LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPNS_15sLtmFrameParamsE14eLTMSceneModelE5bvec1
+ __ZZN12LTMComputeV210LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPNS_15sLtmFrameParamsE14eLTMSceneModelE5bvec2
+ __ZZN12LTMComputeV210LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPNS_15sLtmFrameParamsE14eLTMSceneModelE6xgHigh
+ ___62-[LTMExtractMetadataV1 extractFrom:toDriverInput:ltmGeometry:]_block_invoke
+ ___62-[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:]_block_invoke
+ ___block_literal_global.150
+ ___block_literal_global.211
+ _fig_note_initialize_category_with_default_work_cf
+ _kFigCaptureSampleBufferMetadata_FinalCropRect
+ _kFigCaptureStreamMetadata_QuadraBinningFactor
+ _kFigCaptureStreamMetadata_SensorCropRect
+ _kFigCaptureStreamMetadata_SensorID
+ _objc_autorelease
+ _objc_msgSend$_addAverageLTMToMetadata:curvesType:fromOutput:ltcNumNodes:
+ _objc_msgSend$_addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:ltcNumNodes:
+ _objc_msgSend$_addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:
+ _objc_msgSend$_printDefaultsLTMparam
+ _objc_msgSend$calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:
+ _objc_msgSend$cmi_unsignedIntValueForKey:defaultValue:found:
+ _objc_msgSend$compute
+ _objc_msgSend$computeGain:withTargetRange:
+ _objc_msgSend$computeHDRCurvesWoFaceBoost
+ _objc_msgSend$computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:
+ _objc_msgSend$createLTMInTextureFromRGBAFloatTex:undoScaleDown:
+ _objc_msgSend$deepZoomRatio
+ _objc_msgSend$encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:
+ _objc_msgSend$extractAWBMetadataFromMetadata:validBufferRect:ltmGeometryData:toDriverInput:
+ _objc_msgSend$extractHRGainDownRatioFrom:
+ _objc_msgSend$extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:
+ _objc_msgSend$generateLinearRGBATexture:
+ _objc_msgSend$getTileStatsRegion:validBufferRect:ltmGeometryData:toDriverInput:
+ _objc_msgSend$getTileStatsRegionWithMetadata:cropRectLTMInCoords:ltmInDownsamplingRatio:tileStatsRegionLTMInCoordsDictOut:
+ _objc_msgSend$getTransformCropRectFromSensorCoordsToValidBufferCoordsWithMetadata:validBufferRect:
+ _objc_msgSend$initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:
+ _objc_msgSend$initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:
+ _objc_msgSend$inputBufferRect
+ _objc_msgSend$lscModulationWeight
+ _objc_msgSend$minimumAdaptiveHC_SIFR
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$rawSensorHeight
+ _objc_msgSend$rawSensorWidth
+ _objc_msgSend$sensorSpaceToValidBufferSpaceTransform
+ _objc_msgSend$setComputeHDRCurvesWoFaceBoost:
+ _objc_msgSend$setDeepZoomRatio:
+ _objc_msgSend$setMinimumAdaptiveHC_SIFR:
+ _objc_msgSend$setRawSensorHeight:
+ _objc_msgSend$setRawSensorWidth:
+ _objc_msgSend$setSensorSpaceToValidBufferSpaceTransform:
+ _objc_msgSend$setTileStatsROIRect:
+ _objc_msgSend$startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:
+ _objc_msgSend$undoHRGainDownRatio
+ _objc_opt_isKindOfClass
+ _objc_release_x9
+ _objc_retain_x27
+ _objc_retain_x28
+ _stringFromCGRectDictionaryRepresentation
- +[LTMExtractMetadata compareAWBMetadata:withReference:]
- +[LTMExtractMetadata extractAWBMetadataFromMetadata:validBufferRect:toDriverInput:]
- +[LTMExtractMetadata extractAWBMetadataFromRawMetadata:toDriverInput:]
- +[LTMExtractMetadata extractCCMFromMetadata:toDriverInput:]
- +[LTMExtractMetadata extractFromRawMetadata:toDriverInput:]
- +[LTMExtractMetadata extractRectanglesFrom:validBufferRect:ltmGeometry:]
- +[LTMExtractMetadata getTileStatsRegion:validBufferRect:toDriverInput:]
- +[LTMExtractMetadata isLocalCCMEnabled:]
- +[LTMMetadataWriter _addAverageLTMToMetadata:curvesType:fromOutput:]
- +[LTMMetadataWriter _addGlobalLTMLookUpTableAlignedToFinalCropRect:]
- +[LTMMetadataWriter _addHazeCorrection:driverInputMetadata:]
- +[LTMMetadataWriter _addHighlightCompression:driverInputMetadata:]
- +[LTMMetadataWriter _addLTMCurveTypeToMetadata:driverInputMetadata:]
- +[LTMMetadataWriter _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:]
- +[LTMMetadataWriter _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:].cold.1
- +[LTMMetadataWriter _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:].cold.2
- +[LTMMetadataWriter _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:].cold.3
- +[LTMMetadataWriter _addLTMEnabledToMetadata:]
- +[LTMMetadataWriter _addLocalClippingDataToMetadata:statistics:geometryData:]
- +[LTMMetadataWriter _addLocalClippingDataToMetadata:statistics:geometryData:].cold.1
- +[LTMMetadataWriter _addLocalHistToMetadata:statistics:geometryData:]
- +[LTMMetadataWriter _addLocalHistToMetadata:statistics:geometryData:].cold.1
- +[LTMMetadataWriter _addSoftDGainToMetadata:driverInputMetadata:]
- +[LTMMetadataWriter _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:]
- +[LTMMetadataWriter _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:].cold.1
- +[LTMMetadataWriter _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:].cold.2
- +[LTMMetadataWriter addLTMMetadataTo:curvesType:fromLTMOutput:statistics:driverInputMetadata:geometryData:]
- +[LTMMetadataWriter createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:]
- +[LTMMetadataWriter createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:].cold.1
- -[AWBAlgorithm _applyDefaultWriteOverridesForAWBGains]
- -[AWBAlgorithm configWithSetFile:metadata:awbParams:]
- -[AWBAlgorithm setFileData]
- -[AWBIBPParams registers]
- -[AWBIBPParams setFileDict]
- -[AWBIBPParams setRegisters:]
- -[AWBIBPParams setSetFileDict:]
- -[AWBStatistics _createShaders].cold.9
- -[AWBStatistics configWithRegs:]
- -[AWBStatistics configWithRegs:metadata:cameraInfo:]
- -[AWBStatistics configWithSetFile:metadata:cameraInfo:]
- -[HazeEstimation getThumbnailTexture]
- -[HazeProperties getData]
- -[HazeProperties setData:]
- -[LTMComputeRef computeLTM:withMetadata:to:]
- -[LTMComputeRef init]
- -[LTMCurvesCompute .cxx_destruct]
- -[LTMCurvesCompute compute]
- -[LTMCurvesCompute compute].cold.1
- -[LTMCurvesCompute compute].cold.2
- -[LTMCurvesCompute compute].cold.3
- -[LTMCurvesCompute compute].cold.4
- -[LTMCurvesCompute initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:]
- -[LTMCurvesCompute initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:].cold.1
- -[LTMCurvesCompute initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:].cold.2
- -[LTMCurvesCompute initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:].cold.3
- -[LTMDriverRef computeLtmComputeInput:withMetadata:to:computeInputMetadata:]
- -[LTMDriverRef dealloc]
- -[LTMDriverRef init]
- -[LTMExtractMetadata extractFrom:toDriverInput:ltmGeometry:]
- -[LTMExtractMetadata init]
- -[LTMGeometryData copyWithZone:]
- -[LTMGeometryData cropRect]
- -[LTMGeometryData deepZoomOrigin]
- -[LTMGeometryData initWithInputTextureWidth:height:]
- -[LTMGeometryData initWithInputTextureWidth:height:].cold.1
- -[LTMGeometryData initWithInputTextureWidth:height:].cold.2
- -[LTMGeometryData inputTextureDownsampleRatio]
- -[LTMGeometryData inputTextureSize]
- -[LTMGeometryData setCropRect:sourceRect:]
- -[LTMGeometryData setDeepZoomOrigin:]
- -[LTMGeometryData setInputTextureDownsampleRatio:]
- -[LTMGeometryData sourceRect]
- -[LTMProcessor createLTMComputer]
- -[LTMProcessor createLTMInTextureFromRGBAFloatTex:]
- -[LTMProcessor generateLinearRGBATexture]
- -[LTMProcessor generateLinearRGBATexture].cold.1
- -[LTMProcessor generateLinearRGBATexture].cold.2
- -[LTMProcessor generateLinearRGBATexture].cold.3
- -[LTMProcessor initWithCommandQueue:].cold.10
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.20
- -[LTMProcessor setLTMComputeTuningParams:from:].cold.1
- -[LTMProcessor setLTMComputeTuningParams:from:].cold.2
- -[LTMProcessor setLTMComputeTuningParams:from:].cold.3
- -[LTMProcessor setLTMComputeTuningParams:from:].cold.4
- -[LTMProcessor setLTMComputeTuningParams:from:].cold.5
- -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:]
- -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:].cold.1
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:]
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.1
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.10
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.2
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.3
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.4
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.5
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.6
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.7
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.8
- -[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:].cold.9
- GCC_except_table48
- _CFGetTypeID
- _CFPreferencesCopyValue
- _CFRelease
- _CFStringCreateMutableCopy
- _CFStringGetTypeID
- _FigGetCFPreferenceBooleanWithDefault
- _FigGetCFPreferenceNumberWithDefault
- _FigProcessorDebugClass
- _FigProcessorDebugClass.cls
- _FigProcessorDebugClass.cold.1
- _FigProcessorDebugClass.onceToken
- _NSClassFromString
- _OBJC_CLASS_$_LTMComputeRef
- _OBJC_CLASS_$_LTMCurvesCompute
- _OBJC_CLASS_$_LTMDriverRef
- _OBJC_CLASS_$_LTMExtractMetadata
- _OBJC_CLASS_$_LTMGeometryData
- _OBJC_CLASS_$_LTMMetadataWriter
- _OBJC_IVAR_$_AWBAlgorithm._setFileData
- _OBJC_IVAR_$_AWBIBPParams._registers
- _OBJC_IVAR_$_AWBIBPParams._setFileDict
- _OBJC_IVAR_$_AWBStatistics._computeAWBStatsPipelineState
- _OBJC_IVAR_$_LTMComputeRef._ltmCompute
- _OBJC_IVAR_$_LTMCurvesCompute._LTMIsReady
- _OBJC_IVAR_$_LTMCurvesCompute._computeCurvesWoFaceBoost
- _OBJC_IVAR_$_LTMCurvesCompute._computeHDRCurves
- _OBJC_IVAR_$_LTMCurvesCompute._computeInputs
- _OBJC_IVAR_$_LTMCurvesCompute._computeInputsMetadata
- _OBJC_IVAR_$_LTMCurvesCompute._computeLTM
- _OBJC_IVAR_$_LTMCurvesCompute._computeOutput
- _OBJC_IVAR_$_LTMCurvesCompute._driverInputMetadata
- _OBJC_IVAR_$_LTMCurvesCompute._driverLTM
- _OBJC_IVAR_$_LTMCurvesCompute._geometryData
- _OBJC_IVAR_$_LTMCurvesCompute._globalHistStat
- _OBJC_IVAR_$_LTMCurvesCompute._isDigitalFlash
- _OBJC_IVAR_$_LTMCurvesCompute._localHistStat
- _OBJC_IVAR_$_LTMCurvesCompute._ltmStats
- _OBJC_IVAR_$_LTMCurvesCompute._optimized
- _OBJC_IVAR_$_LTMCurvesCompute._procHITHStat
- _OBJC_IVAR_$_LTMCurvesCompute._thumbnailStat
- _OBJC_IVAR_$_LTMDriverRef._ltmDriver
- _OBJC_IVAR_$_LTMExtractMetadata._faceBiasScaler
- _OBJC_IVAR_$_LTMExtractMetadata._faceBiasScalerMin
- _OBJC_IVAR_$_LTMExtractMetadata._faceBiasThreshold
- _OBJC_IVAR_$_LTMExtractMetadata._faceBiasThresholdMin
- _OBJC_IVAR_$_LTMExtractMetadata._forceDisableHR
- _OBJC_IVAR_$_LTMExtractMetadata._forceDisableLTMFaceBoost
- _OBJC_IVAR_$_LTMExtractMetadata._forceDisableLTMFaceExposureRatio
- _OBJC_IVAR_$_LTMExtractMetadata._forceDisableLTMHazeCorrection
- _OBJC_IVAR_$_LTMExtractMetadata._forceHighlightCompressionForEveryFrame
- _OBJC_IVAR_$_LTMExtractMetadata._forceUseBt709
- _OBJC_IVAR_$_LTMGeometryData._cropRect
- _OBJC_IVAR_$_LTMGeometryData._deepZoomOrigin
- _OBJC_IVAR_$_LTMGeometryData._inputTextureDownsampleRatio
- _OBJC_IVAR_$_LTMGeometryData._inputTextureRect
- _OBJC_IVAR_$_LTMGeometryData._inputTextureSize
- _OBJC_IVAR_$_LTMGeometryData._minimumRect
- _OBJC_IVAR_$_LTMGeometryData._sourceRect
- _OBJC_IVAR_$_LTMProcessor._computeInputs
- _OBJC_IVAR_$_LTMProcessor._computeInputsMetadata
- _OBJC_IVAR_$_LTMProcessor._computeLTM
- _OBJC_IVAR_$_LTMProcessor._computeOutput
- _OBJC_IVAR_$_LTMProcessor._driverLTM
- _OBJC_METACLASS_$_LTMComputeRef
- _OBJC_METACLASS_$_LTMCurvesCompute
- _OBJC_METACLASS_$_LTMDriverRef
- _OBJC_METACLASS_$_LTMExtractMetadata
- _OBJC_METACLASS_$_LTMGeometryData
- _OBJC_METACLASS_$_LTMMetadataWriter
- _OUTLINED_FUNCTION_14
- _OUTLINED_FUNCTION_15
- _OUTLINED_FUNCTION_16
- _OUTLINED_FUNCTION_17
- _OUTLINED_FUNCTION_18
- _OUTLINED_FUNCTION_19
- _OUTLINED_FUNCTION_20
- _OUTLINED_FUNCTION_21
- _OUTLINED_FUNCTION_22
- _OUTLINED_FUNCTION_23
- _OUTLINED_FUNCTION_24
- _OUTLINED_FUNCTION_25
- _OUTLINED_FUNCTION_26
- _OUTLINED_FUNCTION_27
- _OUTLINED_FUNCTION_28
- _OUTLINED_FUNCTION_29
- _OUTLINED_FUNCTION_30
- _OUTLINED_FUNCTION_31
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- _OUTLINED_FUNCTION_34
- _OUTLINED_FUNCTION_35
- _OUTLINED_FUNCTION_36
- _OUTLINED_FUNCTION_37
- _OUTLINED_FUNCTION_38
- _OUTLINED_FUNCTION_39
- _OUTLINED_FUNCTION_40
- _OUTLINED_FUNCTION_41
- _OUTLINED_FUNCTION_42
- _OUTLINED_FUNCTION_43
- _OUTLINED_FUNCTION_44
- _OUTLINED_FUNCTION_45
- _OUTLINED_FUNCTION_46
- _OUTLINED_FUNCTION_47
- _OUTLINED_FUNCTION_48
- _OUTLINED_FUNCTION_49
- _OUTLINED_FUNCTION_50
- _OUTLINED_FUNCTION_51
- _OUTLINED_FUNCTION_52
- __OBJC_$_CLASS_METHODS_LTMExtractMetadata
- __OBJC_$_CLASS_METHODS_LTMMetadataWriter
- __OBJC_$_INSTANCE_METHODS_LTMComputeRef
- __OBJC_$_INSTANCE_METHODS_LTMCurvesCompute
- __OBJC_$_INSTANCE_METHODS_LTMDriverRef
- __OBJC_$_INSTANCE_METHODS_LTMExtractMetadata
- __OBJC_$_INSTANCE_METHODS_LTMGeometryData
- __OBJC_$_INSTANCE_VARIABLES_LTMComputeRef
- __OBJC_$_INSTANCE_VARIABLES_LTMCurvesCompute
- __OBJC_$_INSTANCE_VARIABLES_LTMDriverRef
- __OBJC_$_INSTANCE_VARIABLES_LTMExtractMetadata
- __OBJC_$_INSTANCE_VARIABLES_LTMGeometryData
- __OBJC_$_PROP_LIST_AWBIBPParams.202
- __OBJC_$_PROP_LIST_LTMComputeRef
- __OBJC_$_PROP_LIST_LTMDriverRef
- __OBJC_$_PROP_LIST_LTMGeometryData
- __OBJC_$_PROP_LIST_LTMIBPParams.192
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LTMComputeBase
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LTMDriverBase
- __OBJC_$_PROTOCOL_METHOD_TYPES_LTMComputeBase
- __OBJC_$_PROTOCOL_METHOD_TYPES_LTMDriverBase
- __OBJC_$_PROTOCOL_REFS_LTMComputeBase
- __OBJC_$_PROTOCOL_REFS_LTMDriverBase
- __OBJC_CLASS_PROTOCOLS_$_LTMComputeRef
- __OBJC_CLASS_PROTOCOLS_$_LTMCurvesCompute
- __OBJC_CLASS_PROTOCOLS_$_LTMDriverRef
- __OBJC_CLASS_RO_$_LTMComputeRef
- __OBJC_CLASS_RO_$_LTMCurvesCompute
- __OBJC_CLASS_RO_$_LTMDriverRef
- __OBJC_CLASS_RO_$_LTMExtractMetadata
- __OBJC_CLASS_RO_$_LTMGeometryData
- __OBJC_CLASS_RO_$_LTMMetadataWriter
- __OBJC_LABEL_PROTOCOL_$_LTMComputeBase
- __OBJC_LABEL_PROTOCOL_$_LTMDriverBase
- __OBJC_METACLASS_RO_$_LTMComputeRef
- __OBJC_METACLASS_RO_$_LTMCurvesCompute
- __OBJC_METACLASS_RO_$_LTMDriverRef
- __OBJC_METACLASS_RO_$_LTMExtractMetadata
- __OBJC_METACLASS_RO_$_LTMGeometryData
- __OBJC_METACLASS_RO_$_LTMMetadataWriter
- __OBJC_PROTOCOL_$_LTMComputeBase
- __OBJC_PROTOCOL_$_LTMDriverBase
- __Z11SetFileLoadP7CAWBAFEPKvj
- __Z16print_awbStatCfgP14AWBStatsConfig
- __ZL10configCSC2P12AWBCSCConfigPK12NSDictionary
- __ZL11configTilesP18AWBTileStatsConfigPK12NSDictionary
- __ZL13configPixFiltP16AWBPixFiltConfigPK12NSDictionarym
- __ZL15configColorHistP18AWBColorHistConfigPK12NSDictionary
- __ZL16CMCaptureLibraryv
- __ZL16configAWBStatsDBP16AWBStatsDBConfigPK12NSDictionarym
- __ZL22FigProcessorDebugClassv
- __ZL22FigProcessorDebugClassv.cold.1
- __ZL35soft_FigCaptureGetModelSpecificNamev
- __ZL9configCCMP18AWBLinear3x3ConfigPK12NSDictionary
- __ZL9configCCMP18AWBLinear3x3ConfigPK12NSDictionaryS3_S3_fjPS1_
- __ZL9configCSCP12AWBCSCConfigPK12NSDictionary
- __ZL9configGAMP14AWBGammaConfigPK12NSDictionary
- __ZN10AuxCompute17CalcExposureRatioEPK16sRefDriverInputs
- __ZN10AuxCompute17CalcTotalGainDownEPK16sRefDriverInputs
- __ZN10AuxCompute21CalcLTMspatialCCMSizeEPK7sBTRectP24sLTMSpatialCCMSizeConfig
- __ZN10AuxCompute24CalcAntiAliasingSettingsEPbPjS1_P16sRefDriverInputs
- __ZN10CAWBAFEH1425ComputeAWBChromaHistogramEtt.cold.1
- __ZN10LTMCompute11adaptForHLGEP17sLtmComputeOutput
- __ZN10LTMCompute11defaultHistE
- __ZN10LTMCompute11interpolateEPKfS1_iS1_Pfi
- __ZN10LTMCompute11interpolateEPKfS1_iS1_Pfif
- __ZN10LTMCompute11invExpLutX4E
- __ZN10LTMCompute12allocateToneEPfS0_PKfPK16sLtmTuningParamsPK17sLtmDisplayParamsPK15sLtmFrameParamsS2_S2_S2_S2_S2_fffbb
- __ZN10LTMCompute12makeScaleGTCEPfPKfff
- __ZN10LTMCompute14levelSmoothHFFEPfPKfiii
- __ZN10LTMCompute15scaleToFitRangeEPfPKfS2_S2_fS2_fS2_
- __ZN10LTMCompute15tuningParamsHLGE
- __ZN10LTMCompute15tuningParamsSDRE
- __ZN10LTMCompute16computeLocalLumaEPK16sLtmComputeInputPK16sLtmTuningParamsPK17sLtmDisplayParamsP15sLtmFrameParams
- __ZN10LTMCompute16localCurveInputsE
- __ZN10LTMCompute17HFFspatialMapCalcEiPKfPfS2_
- __ZN10LTMCompute17generateLinearLTCEPK16sLtmComputeInputPK15sLtmComputeMetaP17sLtmComputeOutput
- __ZN10LTMCompute17globalCurveInputsE
- __ZN10LTMCompute18generateSpatialLTCEPK16sLtmComputeInputPK15sLtmComputeMetaP17sLtmComputeOutput
- __ZN10LTMCompute19HFFHighFreqModulateEiiPfS0_S0_S0_S0_
- __ZN10LTMCompute19HFFspatialMapFilterEiiPfPKf
- __ZN10LTMCompute19calculateSceneFlareEPKfiPiffPfS3_S3_
- __ZN10LTMCompute19calculateSceneModelEPK16sLtmComputeInputPK16sLtmTuningParamsP15sLtmFrameParams
- __ZN10LTMCompute19calculateSpatialCCMEPK16sLtmComputeInputPK15sLtmComputeMetaP17sLtmComputeOutput
- __ZN10LTMCompute19computeRGBToneCurveEPK16sLtmComputeInputPK16sLtmTuningParamsPK15sLtmFrameParamsP17sLtmComputeOutput
- __ZN10LTMCompute20ccmWithNewWhitePointEPfPKfff
- __ZN10LTMCompute20computeThumbnailLumaEPK16sLtmComputeInputP15sLtmFrameParams
- __ZN10LTMCompute21calculateDisplayModelEffPKfPf
- __ZN10LTMCompute21smoothHistogramMiddleEPKfPfiS1_ib
- __ZN10LTMCompute21uniformLocalHistogramE
- __ZN10LTMCompute24tuningParamsDigitalFlashE
- __ZN10LTMCompute27tuningParamsDigitalFlashFFCE
- __ZN10LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPK16sLtmTuningParamsbP15sLtmFrameParams
- __ZN10LTMCompute38calculateGlobalLUTandModifySceneModelsEmPK16sLtmComputeInputPK15sLtmComputeMetaPK16sLtmTuningParamsPK17sLtmDisplayParamsP15sLtmFrameParamsP17sLtmComputeOutput
- __ZN10LTMCompute4gpreE
- __ZN10LTMCompute7ProcessEPK16sLtmComputeInputPK15sLtmComputeMetaP17sLtmComputeOutput
- __ZN10LTMCompute9liftedGTCE
- __ZN10LTMComputeC1Ei
- __ZN10LTMComputeD0Ev
- __ZN10LTMComputeD1Ev
- __ZN15CAWBAFEFDAssist32CalculateSkinTileSemanticProbMapEmjPKhPK7sBTRectPK9sMetaDataPhb.cold.1
- __ZN16sLtmTuningParams10nFlareBinsE
- __ZN16sLtmTuningParams15desaturationCCME
- __ZN16sLtmTuningParams22ltc3x3HorzFilterCoeffsE
- __ZN16sLtmTuningParams22ltc3x3VertFilterCoeffsE
- __ZN7CAWBAFE12GetCSCConfigEP16sFEStatCSCConfig
- __ZN7CAWBAFE16SetSensorCalGainEP15sCSensorCalGain
- __ZN7CAWBAFE18GetColorHistConfigEP22sFEStatColorHistConfig
- __ZN9LTMDriver11defaultHistE
- __ZN9LTMDriver18GamutBoundaryRatioEPK16sCLRProcHITHStat
- __ZN9LTMDriver22ComputeGlobalHistogramEPK16sCLRProcHITHStatP16sLtmComputeInput
- __ZN9LTMDriver22ComputeLocalHistogramsEPK16sCLRProcHITHStatP16sLtmComputeInput
- __ZN9LTMDriver22UpdateColorInformationEP16sLtmComputeInputPK16sRefDriverInputsPK16sCLRProcHITHStat
- __ZN9LTMDriver24ComputeLumaFromThumbnailEPK16sCLRProcHITHStatfP16sLtmComputeInput
- __ZN9LTMDriver24computeFaceWeightForToneEPK16sRefDriverInputsP16sLtmComputeInput
- __ZN9LTMDriver25ComputeThumbnailHistogramEPK16sCLRProcHITHStatfP16sLtmComputeInput
- __ZN9LTMDriver26ComputeSpatialCCMWeightMapEPK16sRefDriverInputsP16sLtmComputeInput
- __ZN9LTMDriver28HFFThumbnailDownscaleConvertEPK16sCLRProcHITHStatP16sLtmComputeInput
- __ZN9LTMDriver39CalculateSpatialCCMWeightMapForLEDFlashEPK16sRefDriverInputsP16sLtmComputeInput
- __ZN9LTMDriver7ProcessEPK16sCLRProcHITHStatPK16sRefDriverInputsP16sLtmComputeInput
- __ZN9LTMDriverC1Ev
- __ZN9LTMDriverD0Ev
- __ZN9LTMDriverD1Ev
- __ZTI10LTMCompute
- __ZTI9LTMDriver
- __ZTS10LTMCompute
- __ZTS9LTMDriver
- __ZTV10LTMCompute
- __ZTV9LTMDriver
- __ZZL22FigProcessorDebugClassvE3cls
- __ZZL22FigProcessorDebugClassvE9onceToken
- __ZZL40getFigCapturePlatformIdentifierSymbolLocvE3ptr.0
- __ZZN10LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPK16sLtmTuningParamsbP15sLtmFrameParamsE5bvec1
- __ZZN10LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPK16sLtmTuningParamsbP15sLtmFrameParamsE5bvec2
- __ZZN10LTMCompute28calculateHighlightSceneModelEPK16sLtmComputeInputPK16sLtmTuningParamsbP15sLtmFrameParamsE6xgHigh
- ___107-[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:]_block_invoke
- ___107-[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:]_block_invoke_2
- ___115-[LTMStatsCompute encodeLTMStatisticsCalculationPrecise:paramsGlobalHist:globalHistogram:localHistogram:thumbnail:]_block_invoke
- ___115-[LTMStatsCompute encodeLTMStatisticsCalculationPrecise:paramsGlobalHist:globalHistogram:localHistogram:thumbnail:]_block_invoke_2
- ___237-[AWBStatistics process:clipped:lscGainsTex:validRectInBufferCoords:validRectInSensorReadoutCoords:awbStatsBuffer:awbTileStatsConfig:anstSkinMask:anstSkinMaskData:skyMaskTex:skyMaskData:regionOfInterestRectInBufferCoords:downsizeFactor:]_block_invoke_3
- ___237-[AWBStatistics process:clipped:lscGainsTex:validRectInBufferCoords:validRectInSensorReadoutCoords:awbStatsBuffer:awbTileStatsConfig:anstSkinMask:anstSkinMaskData:skyMaskTex:skyMaskData:regionOfInterestRectInBufferCoords:downsizeFactor:]_block_invoke_4
- ___FigProcessorDebugClass_block_invoke
- ____ZL22FigProcessorDebugClassv_block_invoke
- ____ZL40getFigCapturePlatformIdentifierSymbolLocv_block_invoke
- ___block_descriptor_32_e5_v8?0l
- ___block_literal_global.177
- ___block_literal_global.188
- ___block_literal_global.190
- ___block_literal_global.273
- ___block_literal_global.32
- ___block_literal_global.34
- ___block_literal_global.36
- ___block_literal_global.369
- ___block_literal_global.873
- ___invert_f3
- ___memcpy_chk
- ___stack_chk_fail
- ___stack_chk_guard
- _dispatch_once
- _fig_note_initialize_category_with_default_work
- _kCFPreferencesAnyHost
- _kCFPreferencesCurrentUser
- _kFigCaptureStreamMetadata_AEAverage
- _kFigCaptureStreamMetadata_AETarget
- _kFigCaptureStreamMetadata_LensShadingModulationWeight
- _kFigCaptureStreamPhotometerDetectedSignal_Frequency
- _objc_autoreleasePoolPop
- _objc_autoreleasePoolPush
- _objc_msgSend$_applyDefaultWriteOverridesForAWBGains
- _objc_msgSend$calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:
- _objc_msgSend$cmi_unsignedIntValueFromArrayWithKey:forIndex:defaultValue:found:
- _objc_msgSend$computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:
- _objc_msgSend$configWithRegs:
- _objc_msgSend$configWithRegs:metadata:cameraInfo:
- _objc_msgSend$configWithSetFile:metadata:awbParams:
- _objc_msgSend$configWithSetFile:metadata:cameraInfo:
- _objc_msgSend$containsObject:
- _objc_msgSend$createLTMInTextureFromRGBAFloatTex:
- _objc_msgSend$debugForModule:
- _objc_msgSend$encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:
- _objc_msgSend$extractRectanglesFrom:validBufferRect:ltmGeometry:
- _objc_msgSend$generateLinearRGBATexture
- _objc_msgSend$getData
- _objc_msgSend$hasPrefix:
- _objc_msgSend$initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:
- _objc_msgSend$objectWithName:data:
- _objc_msgSend$objectWithName:mutableData:
- _objc_msgSend$objectWithName:pixelBytes:width:height:stride:pixelFormat:
- _objc_msgSend$objectWithName:texture:
- _objc_msgSend$printCurrentStatus
- _objc_msgSend$registers
- _objc_msgSend$setFileDict
- _objc_msgSend$setInRGBImageUInt16Tex:
- _objc_msgSend$waitForIdle
- _objc_retainAutoreleaseReturnValue
- _useResourceLabels
CStrings:
+ "\t\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf6"
+ "\n"
+ "! CGRectIsEmpty( normalizedSensorRawValidBufferRect )"
+ "! CGRectIsEmpty( normalizedValidBufferRect )"
+ "%s assert: \"%s\" at %s (%s:%d) - %s%s(err=%d)"
+ "( -73465 )"
+ "( [[_stats objectForKey:@\"histStats\"] isKindOfClass:NSData.class] ) && ( [_stats[@\"histStats\"] length] == ( sizeof( AWBStatsColorHist ) ) )"
+ "( [[_stats objectForKey:@\"tileStats\"] isKindOfClass:NSData.class] ) && ( [_stats[@\"tileStats\"] length] == ( sizeof( AWBStatsTiles ) ) )"
+ "( [[_stats objectForKey:@\"windowStats\"] isKindOfClass:NSData.class] ) && ( [_stats[@\"windowStats\"] length] == ( ( sizeof( t_AEAWB_Stat_Elem_copy ) ) * (8) ) )"
+ "( anstSkinMask.pixelFormat == MTLPixelFormatR16Float || anstSkinMask.pixelFormat == MTLPixelFormatR32Float || anstSkinMask.pixelFormat == MTLPixelFormatR8Unorm || anstSkinMask.pixelFormat == MTLPixelFormatR16Unorm )"
+ "( anstSkinMask.width >= ( 256 ) || anstSkinMask.height >= ( 192 ) )"
+ "( cfg->downsizeRatio == 0 ) || ( cfg->downsizeRatio == ( 4 ) ) || ( cfg->downsizeRatio == ( 8 ) ) || ( cfg->downsizeRatio == ( 12 ) ) || ( cfg->downsizeRatio == ( 16 ) )"
+ "( srcBufWidth == dstBufWidth ) && ( srcBufHeight == dstBufHeight )"
+ "( x2 > x1 )"
+ "( y2 > y1 )"
+ "+[AWBStatistics getTileStatsRegionWithMetadata:cropRectLTMInCoords:ltmInDownsamplingRatio:tileStatsRegionLTMInCoordsDictOut:]"
+ "+[GeometryUtilities getTransformCropRectFromSensorCoordsToValidBufferCoordsWithMetadata:validBufferRect:]"
+ "+[LTMExtractMetadataV1 extractAWBMetadataFromMetadata:validBufferRect:toDriverInput:]"
+ "+[LTMExtractMetadataV1 extractCCMFromMetadata:toDriverInput:]"
+ "+[LTMExtractMetadataV1 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]"
+ "+[LTMExtractMetadataV1 getTileStatsRegion:validBufferRect:toDriverInput:]"
+ "+[LTMExtractMetadataV2 extractAWBMetadataFromMetadata:validBufferRect:ltmGeometryData:toDriverInput:]"
+ "+[LTMExtractMetadataV2 extractCCMFromMetadata:toDriverInput:]"
+ "+[LTMExtractMetadataV2 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]"
+ "+[LTMExtractMetadataV2 getTileStatsRegion:validBufferRect:ltmGeometryData:toDriverInput:]"
+ "+[LTMMetadataWriterV1 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:]"
+ "+[LTMMetadataWriterV1 _addLocalClippingDataToMetadata:statistics:geometryData:]"
+ "+[LTMMetadataWriterV1 _addLocalHistToMetadata:statistics:geometryData:]"
+ "+[LTMMetadataWriterV1 _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:]"
+ "+[LTMMetadataWriterV1 createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:]"
+ "+[LTMMetadataWriterV2 _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:ltcNumNodes:]"
+ "+[LTMMetadataWriterV2 _addLocalClippingDataToMetadata:statistics:geometryData:]"
+ "+[LTMMetadataWriterV2 _addLocalHistToMetadata:statistics:geometryData:]"
+ "+[LTMMetadataWriterV2 _addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:]"
+ "+[LTMMetadataWriterV2 createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:]"
+ "-[AWBStatistics _adjustConfigToValidRectInBufferCoords:validRectInSensorReadoutCoords:regionOfInterestRectInBufferCoords:]"
+ "-[AdaptiveGain allocInternalData]"
+ "-[AdaptiveGain computeGain:withTargetRange:]"
+ "-[AdaptiveGain createShaders]"
+ "-[AdaptiveGain initWithMetalContext:]"
+ "-[LTMComputeRefV1 computeLTM:withMetadata:to:]"
+ "-[LTMComputeRefV1 init]"
+ "-[LTMComputeRefV2 computeLTM:withMetadata:to:]"
+ "-[LTMComputeRefV2 init]"
+ "-[LTMCurvesComputeV1 compute]"
+ "-[LTMCurvesComputeV1 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:]"
+ "-[LTMCurvesComputeV2 compute]"
+ "-[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:]"
+ "-[LTMDriverRefV1 computeLtmComputeInput:withMetadata:to:computeInputMetadata:]"
+ "-[LTMDriverRefV1 init]"
+ "-[LTMDriverRefV2 computeLtmComputeInput:withMetadata:to:computeInputMetadata:]"
+ "-[LTMDriverRefV2 init]"
+ "-[LTMExtractMetadataV1 extractFrom:toDriverInput:ltmGeometry:]"
+ "-[LTMExtractMetadataV1 extractHRGainDownRatioFrom:]"
+ "-[LTMExtractMetadataV1 init]"
+ "-[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:]"
+ "-[LTMExtractMetadataV2 extractHRGainDownRatioFrom:]"
+ "-[LTMExtractMetadataV2 init]"
+ "-[LTMGeometryDataV1 initWithInputTextureWidth:height:]"
+ "-[LTMGeometryDataV1 setCropRect:sourceRect:]"
+ "-[LTMGeometryDataV2 initWithInputTextureWidth:height:]"
+ "-[LTMGeometryDataV2 setCropRect:sourceRect:]"
+ "-[LTMProcessor _printDefaultsLTMparam]"
+ "-[LTMProcessor createLTMInTextureFromRGBAFloatTex:undoScaleDown:]"
+ "-[LTMProcessor generateLinearRGBATexture:]"
+ "-[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:]"
+ "-[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:]"
+ "-[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:]"
+ "0"
+ "<<<< AWBAlgorithm >>>> %s: Flash Calibration data isn't available, disabling the flash projection"
+ "<<<< AWBAlgorithm >>>> %s: Unsupported device: %@ (this may be overridden with defaults write com.apple.coremedia softisp.awb.modelname <model>)"
+ "<<<< AWBAlgorithm >>>> %s: err=%d"
+ "<<<< AWBAlgorithm >>>> %s: fabm:{%@}"
+ "<<<< AWBAlgorithm >>>> %s: it:%d ct:%d lgt:%d sim:%d sym:%d fp:%d cl:%d dfa:%d dfl:%d sd:%d lmg:%d fabm:%d vrs:%@ vr:%@ roi:%@"
+ "<<<< AWBAlgorithm >>>> %s: ts=%d ws=%d hs=%d asm=%d sm=%d upfwp:%d scom:%d aom:%d mom:%d "
+ "<<<< AWBAlgorithm >>>> Fig"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: Unsupported platformID (%d) - proceeding without photometer support"
+ "<<<< AWBProcessor >>>> %s: Prepare to process with ModuleConfig"
+ "<<<< AWBProcessor >>>> %s: err=%d"
+ "<<<< AWBProcessor >>>> Fig"
+ "<<<< AWBStats >>>> %s: dfa:%d vrs:%@ vr:%@ roi:%@ sroi:%@"
+ "<<<< AWBStats >>>> %s: err=%d"
+ "<<<< AWBStats >>>> %s: it:%d ct:%d lgt:%d sim:%d sym:%d fp:%d cl:%d dfa:%d dfl:%d sd:%d lmg:%d fabm:%d vrs:%@ vr:%@ roi:%@"
+ "<<<< AWBStats >>>> %s: it:%d ct:%d lgt:%d sim:%d sym:%d pesm:%d pism:%d fsmo:%d ep:%d aipb:%d aopb:%d fasm:%d"
+ "<<<< AWBStats >>>> Fig"
+ "<<<< CameraColorProcessing >>>> %s: Normalization of TotalSensorCropRect failed"
+ "<<<< CameraColorProcessing >>>> %s: Normalization of valid buffer rect failed"
+ "<<<< CameraColorProcessing >>>> %s: RawSensorHeight not found"
+ "<<<< CameraColorProcessing >>>> %s: RawSensorWidth not found"
+ "<<<< CameraColorProcessing >>>> %s: TotalSensorCropRect not found"
+ "<<<< CameraColorProcessing >>>> %s: normalizedSensorRawValidBufferRect: {{%g, %g}, {%g, %g}}"
+ "<<<< CameraColorProcessing >>>> %s: normalizedValidBufferRect: {{%g, %g}, {%g, %g}}"
+ "<<<< CameraColorProcessing >>>> %s: totalSensorCropRectRawCoords: {{%g, %g}, {%g, %g}}"
+ "<<<< CameraColorProcessing >>>> %s: validBufferRect: {{%g, %g}, {%g, %g}}"
+ "<<<< CameraColorProcessing >>>> Fig"
+ "<<<< LTMAlgorithm >>>> %s:    adaptiveGainMax:                       %f"
+ "<<<< LTMAlgorithm >>>> %s:    adaptiveGainRange:                     %f"
+ "<<<< LTMAlgorithm >>>> %s:    adaptiveHCSlope:                       %f"
+ "<<<< LTMAlgorithm >>>> %s:    calcGlobalHistOnROI:                   %d"
+ "<<<< LTMAlgorithm >>>> %s:    computeCurvesWoFaceBoost:              %d"
+ "<<<< LTMAlgorithm >>>> %s:    computeHDRCurves:                      %d"
+ "<<<< LTMAlgorithm >>>> %s:    computeHDRCurvesWoFaceBoost:           %d"
+ "<<<< LTMAlgorithm >>>> %s:    doGlobalCCM:                           %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableAdaptiveGain %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableAdaptiveGain:                    %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableAntiAliasing:                    %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableCB:                              %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableCB:                  %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableDualLTC:                         %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableDualLTC:             %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableFATE:                            %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableFATE:                %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableHiResLocalHistogram:             %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableHiResLocalHistogram: %d"
+ "<<<< LTMAlgorithm >>>> %s:    enablePreLTMHazeCorrection:            %d"
+ "<<<< LTMAlgorithm >>>> %s:    isAdaptiveHighlightCompressionEnabled: %d"
+ "<<<< LTMAlgorithm >>>> %s:    isHazeEstimationEnabled:               %d"
+ "<<<< LTMAlgorithm >>>> %s:    isHighlightCompressionEnabled:         %d"
+ "<<<< LTMAlgorithm >>>> %s:    ispDGainThreshold:                     %f"
+ "<<<< LTMAlgorithm >>>> %s:    minimumAdaptiveHC_SIFR:                %f"
+ "<<<< LTMAlgorithm >>>> %s: AdaptiveGain: %f"
+ "<<<< LTMAlgorithm >>>> %s: AdaptiveGainConstrained: %f"
+ "<<<< LTMAlgorithm >>>> %s: After AdaptiveGain - softIspDGain=%f - hardIspDGain=%f"
+ "<<<< LTMAlgorithm >>>> %s: Before AdaptiveGain - softIspDGain=%f - hardIspDGain=%f"
+ "<<<< LTMAlgorithm >>>> %s: Could not make a dictionary representation from processing region rect"
+ "<<<< LTMAlgorithm >>>> %s: Could not make a dictionary representation from valid buffer rect"
+ "<<<< LTMAlgorithm >>>> %s: Could not read adaptiveGainMax field"
+ "<<<< LTMAlgorithm >>>> %s: Could not read adaptiveGainRange field"
+ "<<<< LTMAlgorithm >>>> %s: Could not read minimumAdaptiveHC_SIFR field"
+ "<<<< LTMAlgorithm >>>> %s: Enabling features for ltmAlgoVersion %d:"
+ "<<<< LTMAlgorithm >>>> %s: Exposure Ratio (before overflow >80.0f): %f"
+ "<<<< LTMAlgorithm >>>> %s: Exposure Ratio (final): %f"
+ "<<<< LTMAlgorithm >>>> %s: Fail to run adaptiveGain"
+ "<<<< LTMAlgorithm >>>> %s: Invoked shader allocation paths for prewarming: %@"
+ "<<<< LTMAlgorithm >>>> %s: LTM parameters:"
+ "<<<< LTMAlgorithm >>>> %s: Using FinalCropRectFromSource metadata ROI as LTM rectangle"
+ "<<<< LTMAlgorithm >>>> %s: Warning: LTM tuning params is nil"
+ "<<<< LTMAlgorithm >>>> %s: Warning: LTM's dehaze tuning params is nil"
+ "<<<< LTMAlgorithm >>>> %s: _cropRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: _sourceRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: finalCropRectLTMInCoords: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: finalCropRectLTMInCoordsNormalized: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: globalFaceHistBuffer is nil"
+ "<<<< LTMAlgorithm >>>> %s: mCropRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: mSourceRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: outStatsParams is nil"
+ "<<<< LTMAlgorithm >>>> %s: tmpCropRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> Fig"
+ "<<<< LTMAlgorithmV1 >>>>"
+ "<<<< LTMAlgorithmV1 >>>> %s:    bottomPadding:        %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    bottomPadding:      %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    ccmFixedPointBase:    %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    dataSize:                             %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    gridOriginX:                          %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    gridOriginY:                          %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    highInvalidBinIndex:                  %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    highThreshold:                        %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    highThresholdBinIndex:                %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    leftPadding:          %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    leftPadding:        %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    localHistogramBinSize:                %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    localHistogramBitShift:               %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    localHistogramOriginalTilePixelCount: %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lowInvalidBinIndex:                   %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lowThreshold:                         %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lowThresholdBinIndex:                 %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    ltmCurveEntryCount: %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lutsBytesPerColumn:   %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lutsBytesPerColumn: %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lutsBytesPerRow:      %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lutsBytesPerRow:    %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lutsCountX:           %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lutsCountX:         %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lutsCountY:           %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    lutsCountY:         %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    rightPadding:         %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    rightPadding:       %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileCountX:                           %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileCountY:                           %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileHeight:           %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileHeight:         %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileSizeX:                            %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileSizeY:                            %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileStrideX:                          %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileStrideY:                          %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileWidth:            %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    tileWidth:          %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    topPadding:           %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    topPadding:         %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    version:                              %d"
+ "<<<< LTMAlgorithmV1 >>>> %s:    version:            %d"
+ "<<<< LTMAlgorithmV1 >>>> %s: Can't allocate the metadata"
+ "<<<< LTMAlgorithmV1 >>>> %s: Fail to create LTM metadata"
+ "<<<< LTMAlgorithmV1 >>>> %s: Fail to process LTM compute"
+ "<<<< LTMAlgorithmV1 >>>> %s: Fail to process LTM compute for HLG"
+ "<<<< LTMAlgorithmV1 >>>> %s: Fail to process LTM driver"
+ "<<<< LTMAlgorithmV1 >>>> %s: FigCaptureLTMLookUpTables:"
+ "<<<< LTMAlgorithmV1 >>>> %s: FigCaptureLocalCCMLookUpTables:"
+ "<<<< LTMAlgorithmV1 >>>> %s: FigCaptureLocalHistogramClippingData:"
+ "<<<< LTMAlgorithmV1 >>>> %s: FigCaptureLocalHistograms:"
+ "<<<< LTMAlgorithmV1 >>>> %s: LTMCurvesCompute is nil"
+ "<<<< LTMAlgorithmV1 >>>> %s: _computeLTM is nil"
+ "<<<< LTMAlgorithmV1 >>>> %s: _driverLTM is nil"
+ "<<<< LTMAlgorithmV1 >>>> %s: clippingData malloc failed"
+ "<<<< LTMAlgorithmV1 >>>> %s: computeCurvesWoFaceBoost: %d"
+ "<<<< LTMAlgorithmV1 >>>> %s: computeHDRCurves: %d"
+ "<<<< LTMAlgorithmV1 >>>> %s: computeHDRCurvesWoFaceBoost: %d"
+ "<<<< LTMAlgorithmV1 >>>> %s: couldn't initialize LTMComputeRef instance"
+ "<<<< LTMAlgorithmV1 >>>> %s: couldn't initialize LTMDriverRef instance"
+ "<<<< LTMAlgorithmV1 >>>> %s: error of processing an LTMCompute"
+ "<<<< LTMAlgorithmV1 >>>> %s: error of processing an LTMDriver"
+ "<<<< LTMAlgorithmV1 >>>> %s: globalLUT malloc failed"
+ "<<<< LTMAlgorithmV1 >>>> %s: ltmLTC malloc failed"
+ "<<<< LTMAlgorithmV1 >>>> %s: rgbToneCurve malloc failed"
+ "<<<< LTMAlgorithmV1 >>>> %s: spatialCCM malloc failed"
+ "<<<< LTMAlgorithmV1 >>>> %s: spatialCCMData is nil"
+ "<<<< LTMAlgorithmV1 >>>> Fig"
+ "<<<< LTMAlgorithmV2 >>>>"
+ "<<<< LTMAlgorithmV2 >>>> %s:    bottomPadding:        %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    bottomPadding:      %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    ccmFixedPointBase:    %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    dataSize:                             %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    gridOriginX:                          %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    gridOriginY:                          %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    highInvalidBinIndex:                  %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    highThreshold:                        %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    highThresholdBinIndex:                %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    leftPadding:          %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    leftPadding:        %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    localHistogramBinSize:                %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    localHistogramBitShift:               %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    localHistogramOriginalTilePixelCount: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lowInvalidBinIndex:                   %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lowThreshold:                         %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lowThresholdBinIndex:                 %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    ltmCurveEntryCount: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lutsBytesPerColumn:   %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lutsBytesPerColumn: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lutsBytesPerRow:      %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lutsBytesPerRow:    %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lutsCountX:           %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lutsCountX:         %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lutsCountY:           %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    lutsCountY:         %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    rightPadding:         %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    rightPadding:       %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileCountX:                           %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileCountY:                           %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileHeight:           %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileHeight:         %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileSizeX:                            %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileSizeY:                            %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileStrideX:                          %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileStrideY:                          %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileWidth:            %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    tileWidth:          %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    topPadding:           %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    topPadding:         %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    version:                              %d"
+ "<<<< LTMAlgorithmV2 >>>> %s:    version:            %d"
+ "<<<< LTMAlgorithmV2 >>>> %s: Can't allocate the metadata"
+ "<<<< LTMAlgorithmV2 >>>> %s: Fail to create LTM metadata"
+ "<<<< LTMAlgorithmV2 >>>> %s: Fail to process LTM compute"
+ "<<<< LTMAlgorithmV2 >>>> %s: Fail to process LTM compute for HLG"
+ "<<<< LTMAlgorithmV2 >>>> %s: Fail to process LTM driver"
+ "<<<< LTMAlgorithmV2 >>>> %s: FigCaptureLTMLookUpTables:"
+ "<<<< LTMAlgorithmV2 >>>> %s: FigCaptureLocalCCMLookUpTables:"
+ "<<<< LTMAlgorithmV2 >>>> %s: FigCaptureLocalHistogramClippingData:"
+ "<<<< LTMAlgorithmV2 >>>> %s: FigCaptureLocalHistograms:"
+ "<<<< LTMAlgorithmV2 >>>> %s: LTMCurvesCompute is nil"
+ "<<<< LTMAlgorithmV2 >>>> %s: Unsupported localHistBinSize"
+ "<<<< LTMAlgorithmV2 >>>> %s: _computeLTM is nil"
+ "<<<< LTMAlgorithmV2 >>>> %s: _driverLTM is nil"
+ "<<<< LTMAlgorithmV2 >>>> %s: clippingData malloc failed"
+ "<<<< LTMAlgorithmV2 >>>> %s: computeCurvesWoFaceBoost: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s: computeHDRCurves: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s: computeHDRCurvesWoFaceBoost: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s: couldn't initialize LTMComputeRef instance"
+ "<<<< LTMAlgorithmV2 >>>> %s: couldn't initialize LTMDriverRef instance"
+ "<<<< LTMAlgorithmV2 >>>> %s: driverInputMetadata.CBVer: %d, driverInputMetadata.faceLTMVer: %d, computeInputsMetadata.enableHiResLocalHistogram: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s: error of processing an LTMCompute"
+ "<<<< LTMAlgorithmV2 >>>> %s: error of processing an LTMDriver"
+ "<<<< LTMAlgorithmV2 >>>> %s: globalLUT malloc failed"
+ "<<<< LTMAlgorithmV2 >>>> %s: ltmLTC malloc failed"
+ "<<<< LTMAlgorithmV2 >>>> %s: rgbToneCurve malloc failed"
+ "<<<< LTMAlgorithmV2 >>>> %s: spatialCCM malloc failed"
+ "<<<< LTMAlgorithmV2 >>>> %s: spatialCCMData is nil"
+ "<<<< LTMAlgorithmV2 >>>> Fig"
+ "<<<< LTMComputeV1 >>>> %s: AWB gain-ratio CCM: [ %.3f %.3f %.3f ]"
+ "<<<< LTMComputeV2 >>>> %s: AWB gain-ratio CCM: [ %.3f %.3f %.3f ]"
+ "<<<< LTMDriverV1 >>>> %s: awbGainsFlashProj.b=%d awbGains.b=%d bGainRatio=%.2f"
+ "<<<< LTMDriverV1 >>>> %s: awbGainsFlashProj.r=%d awbGains.r=%d rGainRatio=%.2f"
+ "<<<< LTMDriverV1 >>>> %s: awbGainsSkinOnly.b=%d awbGains.b=%d bGainRatio=%.2f"
+ "<<<< LTMDriverV1 >>>> %s: awbGainsSkinOnly.r=%d awbGains.r=%d rGainRatio=%.2f"
+ "<<<< LTMDriverV1 >>>> %s: ccmMixFactor=%.2f"
+ "<<<< LTMDriverV2 >>>> %s: awbGainsFlashProj.b=%d awbGains.b=%d bGainRatio=%.2f"
+ "<<<< LTMDriverV2 >>>> %s: awbGainsFlashProj.r=%d awbGains.r=%d rGainRatio=%.2f"
+ "<<<< LTMDriverV2 >>>> %s: awbGainsSkinOnly.b=%d awbGains.b=%d bGainRatio=%.2f"
+ "<<<< LTMDriverV2 >>>> %s: awbGainsSkinOnly.r=%d awbGains.r=%d rGainRatio=%.2f"
+ "<<<< LTMDriverV2 >>>> %s: ccmMixFactor=%.2f"
+ "@\"<LTMExtractMetadataBase>\""
+ "@\"<LTMGeometryDataBase>\""
+ "@\"AdaptiveGain\""
+ "@\"LTMComputeRefV1\""
+ "@\"LTMComputeRefV2\""
+ "@\"LTMDriverRefV1\""
+ "@\"LTMDriverRefV2\""
+ "@20@0:8f16"
+ "@28@0:8@16f24"
+ "@48@0:8^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32@40"
+ "@48@0:8^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32@40"
+ "@68@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24@32@40B48B52B56B60B64"
+ "@80@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24@32@40B48B52B56B60B64B68B72B76"
+ "AWB algorithm process failed"
+ "AWB statistics process failed"
+ "AWBAlgorithmObj->InitialReset()"
+ "AWBFaceAssistedBehaviorMode_CalculateSkinMask requested but unable to load ANSTKit!"
+ "AWBconfig is invalid"
+ "AdaptiveGain"
+ "AdaptiveGain.m"
+ "AdaptiveGain::histogramGeneration"
+ "AverageLTM_HLGWithoutFaceBoost"
+ "B24@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16"
+ "B32@0:8@16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24"
+ "B40@0:8@\"<LTMIBPParams>\"16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24@\"<LTMGeometryDataBase>\"32"
+ "B40@0:8@16@24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32"
+ "B40@0:8@16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24@32"
+ "B48@0:8@16@24@32^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}40"
+ "CAWBAFEPhotometerAssistPenrose"
+ "CGRectContainsRect( validRect, regionOfInterestRect )"
+ "CGRectContainsRect( validRectInBufferCoords, regionOfInterestRectInBufferCoords )"
+ "CGRectMakeWithDictionaryRepresentation( (__bridge CFDictionaryRef)inputBufferRectDict, &processingRegionRect )"
+ "CGRectMakeWithDictionaryRepresentation( (__bridge CFDictionaryRef)regionOfInterestRectDict, &regionOfInterestRect )"
+ "CGRectMakeWithDictionaryRepresentation( (__bridge CFDictionaryRef)tileStatsRegionLTMInCoordsDict, &tileStatsRegionLTMInCoords )"
+ "CGRectMakeWithDictionaryRepresentation( (__bridge CFDictionaryRef)validBufferRect, &validRectInBufferCoords )"
+ "CGRectMakeWithDictionaryRepresentation( (__bridge CFDictionaryRef)validBufferRectDict, &validBufferRect )"
+ "CGRectMakeWithDictionaryRepresentation( (__bridge CFDictionaryRef)validRectDict, &validRect )"
+ "CGRectNull"
+ "CVPixelBufferLockBaseAddress( anstBuf32Float, kCVPixelBufferLock_ReadOnly ) == kCVReturnSuccess"
+ "CVPixelBufferLockBaseAddress( anstBuf8, 0 ) == kCVReturnSuccess"
+ "CVPixelBufferUnlockBaseAddress( anstBuf32Float, kCVPixelBufferLock_ReadOnly ) == kCVReturnSuccess"
+ "CVPixelBufferUnlockBaseAddress( anstBuf8, 0 ) == kCVReturnSuccess"
+ "ComputeHDRCurvesWoFaceBoost"
+ "Could not allocate temporary colour calibration dict."
+ "D83"
+ "D84"
+ "EnableAdaptiveGain"
+ "EnableCB"
+ "EnableFATE"
+ "EnableHiResLocalHistogram"
+ "Failed to get ColorMatchingModel"
+ "Failed to get ColorMatchingModelDictEntry"
+ "Failed to get bgGainColorMatchingModel"
+ "Failed to get rgGainColorMatchingModel"
+ "Failed to initialize AWBAlgorithmObj"
+ "Failed to read AWB metadata when using spatial CCM"
+ "FigCFDictionaryGetCGRectIfPresent( (__bridge CFDictionaryRef)metadata, kFigCaptureStreamMetadata_TotalSensorCropRect, &totalSensorCropRectRawCoords )"
+ "Flash calibration data not valid."
+ "GeometryUtilities"
+ "GeometryUtilities.mm"
+ "GlobalLTMLookUpTable_HLGWithoutFaceBoost"
+ "GlobalToneCurveLookUpTable_HLGWithoutFaceBoost"
+ "Incorrect relu thresholds"
+ "Incorrect relu values"
+ "Invalid QuadraBinningFactor metadata value"
+ "J410"
+ "J411"
+ "J481"
+ "J482"
+ "J507"
+ "J508"
+ "J537"
+ "J538"
+ "J617"
+ "J618"
+ "J620"
+ "J621"
+ "J717"
+ "J718"
+ "J720"
+ "J721"
+ "LTMAlgoVersion"
+ "LTMComputeBaseV1"
+ "LTMComputeBaseV2"
+ "LTMComputeRefV1"
+ "LTMComputeRefV1.mm"
+ "LTMComputeRefV2"
+ "LTMComputeRefV2.mm"
+ "LTMCurvesComputeV1"
+ "LTMCurvesComputeV1.m"
+ "LTMCurvesComputeV2"
+ "LTMCurvesComputeV2.m"
+ "LTMDriverBaseV1"
+ "LTMDriverBaseV2"
+ "LTMDriverRefV1"
+ "LTMDriverRefV1.mm"
+ "LTMDriverRefV2"
+ "LTMDriverRefV2.mm"
+ "LTMExtractMetadataBase"
+ "LTMExtractMetadataV1"
+ "LTMExtractMetadataV1.mm"
+ "LTMExtractMetadataV2"
+ "LTMExtractMetadataV2.mm"
+ "LTMGeometryDataBase"
+ "LTMGeometryDataV1"
+ "LTMGeometryDataV1.m"
+ "LTMGeometryDataV2"
+ "LTMGeometryDataV2.m"
+ "LTMLookUpTables_HLGWithoutFaceBoost"
+ "LTMMetadataWriterV1"
+ "LTMMetadataWriterV1.m"
+ "LTMMetadataWriterV2"
+ "LTMMetadataWriterV2.m"
+ "LTMStats.m"
+ "Missing or incorrect global CCM"
+ "MixedLightingScore"
+ "SensorCropRect is missing"
+ "Setting downsizeRatio to AWB_STATS_DOWNSAMPLE_48MP but input is larger than 8448x6048"
+ "SkyCCT"
+ "SoftLTM::collectLocalHistHiResKernel"
+ "SoftLTM::globalFaceHistKernel"
+ "SoftLTM::localHistHiResAndThumbKernel"
+ "Strobe calibration data version not supported."
+ "T@\"NSDictionary\",&,N,V_inputBufferRect"
+ "T@\"NSNumber\",&,N,V_lscModulationWeight"
+ "TB,N,V_computeHDRCurvesWoFaceBoost"
+ "TB,N,V_undoHRGainDownRatio"
+ "Tf,N,V_deepZoomRatio"
+ "Tf,N,V_minimumAdaptiveHC_SIFR"
+ "Ti,N,V_rawSensorHeight"
+ "Ti,N,V_rawSensorWidth"
+ "T{CGAffineTransform=dddddd},N,V_sensorSpaceToValidBufferSpaceTransform"
+ "T{CGPoint=dd},N"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_tileStatsROIRect"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
+ "T{CGSize=dd},R,N"
+ "Unable to initialize AdaptiveGain"
+ "Unable to initialize HazeEstimation"
+ "Unable to updateHRGainDownRatioMetadata"
+ "Unexpected sky mask size"
+ "UpdateColorInformation"
+ "V59"
+ "Z"
+ "[12480S]"
+ "[256I]"
+ "[_stats[@\"anstSkinMask\"] length] == (256*192)"
+ "[_stats[@\"skyMaskData\"] length] == ( skyMaskWidth * skyMaskHeight )"
+ "^{CAWBAFE=^^?i^{CDualLEDsWhitePointProjector}{?=[9f][9f][6{?=fffff}]{?=[6f][6f][6f][6f][6f][6f]}[3{?=ff}][3{?=ff}][3{?=ff}][3{?=ff}]BB}^{CAWBAFEFDAssist}^{CAWBAFEPhotometerAssistPenrose}^{sPhotometerAWBMetadata}^{_FE_3A_Stats_H15}^{_FE_3A_Stats_H15}^{_TILE_Stat_Elem}^{_AEAWB_Stat_Elem}^{_HighResAWBAE_Stat_Elem}^I{sFEStatCSCConfig=[9s][9s][3s][3S][3S][2S]C}{sFEStatColorHistConfig=[15S][16C]SISI}ISSSBI[3I][3I][3[3i]][3[3i]]IBBBIIi[3S][3S]IffSfffffff{sAWBInternalParams=SSBBBffffffffffffffffffffI[1024I]}B{sAWBDigitalFlashSkyParams=iBffffffff}iBfff[1024I][1024I][6[4s]][3S][9s][2S][2S][13S][3S][32S]S*[1024C][6[1024C]][6s]CSSSSfSSSSB[3I]fSiBi[30[2s]]I[8[3S]]I[6[9s]]{sCSensorCalGain=SSSS}SSSSBI[4I]II{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}ffBBBBBfii[3I]^{fdAWBMetaData}[150[4S]]IBB{sWPStableZoneControlTable={sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}}BBCCQSS^{sMetaData}[3S]iBi[2f]f[30[2s]][6I][6I]B[6S]S[32S]B[192f]{sAWBTimelapseParams=BBI{sAWBTimelapseSmoothingState=ff[3f][3f]fffSB}}f{sCIspCmdChColorCalIdealSet=ISS(?=I{sCIspControllerCmdHdrChInfo=b16b15b1})SSSS}Bi{sUnagiParams=i}C}"
+ "^{LTMCompute=^^?QBII^{sLtmTuningParams}[256f][257f]{sLtmDisplayParams=[257f][257f]f}f{sLtmFrameParams=[48f][48f]ff[257f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][257f][3f]ffffffffffffffffffffffff}[5[2118f]][5B]}"
+ "^{LTMDriver=^^?{sLtmComputeInput=[3072f][64f][1024f][48f][48f][64f][64f][65f][48f]ffffffffffffS[9f][192f]fffBB[48f]f}{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBiBif}C[6{LTMTuning=ffffffffffffffffffffffffffff}]B}iB}"
+ "^{LTMDriver=^^?{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}BIIiB}"
+ "^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16@0:8"
+ "_AWBAlgorithmObj->InitialReset()"
+ "_adaptiveGain"
+ "_adaptiveGain is NULL"
+ "_adaptiveGainMax"
+ "_adaptiveGainRange"
+ "_adaptiveGainValue"
+ "_addAverageLTMToMetadata:curvesType:fromOutput:ltcNumNodes:"
+ "_addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:ltcNumNodes:"
+ "_addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:"
+ "_collectLocalHistHiResKernelPipelineState"
+ "_collectLocalHistHiResKernelPipelineState is NULL"
+ "_computeHDRCurvesWoFaceBoost"
+ "_computePipelineHistogramGeneration"
+ "_computePipelineHistogramGeneration is NULL"
+ "_deepZoomRatio"
+ "_enableAdaptiveGain"
+ "_enableCB"
+ "_enableDualLTC"
+ "_enableFATE"
+ "_enableHiResLocalHistogram"
+ "_fallbackGains.awbBGain"
+ "_fallbackGains.awbComboBGain"
+ "_fallbackGains.awbComboGGain"
+ "_fallbackGains.awbComboRGain"
+ "_fallbackGains.awbGGain"
+ "_fallbackGains.awbRGain"
+ "_globalFaceHistBuffer"
+ "_globalFaceHistKernelPipelineState"
+ "_globalFaceHistKernelPipelineState is NULL"
+ "_globalFaceHistStat"
+ "_hazeEstimator.hazePropertiesForLTM"
+ "_inputBufferRect"
+ "_localHistHiResAndThumKernelPipelineState"
+ "_localHistHiResAndThumKernelPipelineState is NULL"
+ "_lscModulationWeight"
+ "_ltmParams.outMetaData"
+ "_lumaParams"
+ "_metalContext.allocator"
+ "_metalContext.commandQueue"
+ "_minimumAdaptiveHC_SIFR"
+ "_outputMetadata[(id)kFigCaptureStreamMetadata_AWBComboBGain]"
+ "_outputMetadata[(id)kFigCaptureStreamMetadata_AWBComboGGain]"
+ "_outputMetadata[(id)kFigCaptureStreamMetadata_AWBComboRGain]"
+ "_outputMetadata[(id)kFigCaptureStreamMetadata_HRGainDownRatio]"
+ "_printDefaultsLTMparam"
+ "_rawSensorHeight"
+ "_rawSensorWidth"
+ "_sensorSpaceToValidBufferSpaceTransform"
+ "_tileStatsROIRect"
+ "_undoHRGainDownRatio"
+ "absoluteCalibrations"
+ "absoluteColorCalHighCCT"
+ "absoluteColorCalLowCCT"
+ "absoluteColorCalibrations"
+ "absoluteColorCals"
+ "absoluteColourCalibrations dictionary not valid"
+ "adaptiveGainMax"
+ "adaptiveGainRange"
+ "algoObj"
+ "allocatorBackend.memSize >= ( 1024 * 1024 * 2 )"
+ "allocatorDesc"
+ "allocatorDesc.memSize > 0"
+ "angleInfoRoll"
+ "anstBuf32Float"
+ "anstBuf8"
+ "anstBuf8 is NULL"
+ "anstInputPixelBuffer"
+ "anstInputTex"
+ "anstOutputPixelBuffer"
+ "anstOutputPixelBuffer8"
+ "anstOutputTex"
+ "anstSkinMaskData"
+ "assetPath"
+ "assetURL"
+ "awbAlgorithmFW->InitialReset()"
+ "awbAlgorithmSoftISP"
+ "awbConfig"
+ "awbConfigSecondarySensor"
+ "awbConfig[@\"CSC\"]"
+ "awbStatsBuffer"
+ "bail"
+ "bailBlock"
+ "bail_masks"
+ "base"
+ "base->offsets[CISP_META_DATA_INPUT]"
+ "baseURL"
+ "bgGainColorMatchingModel"
+ "blitEncoder"
+ "bundle"
+ "calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:"
+ "ccmConfig"
+ "ccmWithNewWhitePoint"
+ "cmdBuf"
+ "cmdEnc"
+ "cmi_unsignedIntValueForKey:defaultValue:found:"
+ "colorCalibrationsOut"
+ "colorCorrectedRGBATexture"
+ "colorMatchingForSensor"
+ "colorMatchingModelArray"
+ "colorMatchingModelDictEntry"
+ "colourCalibrations dictionary not valid"
+ "com.apple.cameracapture"
+ "commandEncoder"
+ "compressionCurveTex"
+ "compressionCurveTexDesc"
+ "computeGain:withTargetRange:"
+ "computeHDRCurvesWoFaceBoost"
+ "computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:"
+ "config"
+ "createLTMInTextureFromRGBAFloatTex:undoScaleDown:"
+ "cscConfig"
+ "curvesComputeLTM"
+ "cvErr == kCVReturnSuccess"
+ "deepZoomRatio"
+ "dehazedRGBATexture"
+ "driverMetaDataInput->hardIspDGain > 0"
+ "dstBufAddr"
+ "encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:"
+ "err == 0 "
+ "extractAWBMetadataFromMetadata:validBufferRect:ltmGeometryData:toDriverInput:"
+ "extractHRGainDownRatioFrom:"
+ "extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:"
+ "f24@0:8@\"NSDictionary\"16"
+ "f24@0:8@16"
+ "f24@0:8r^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16"
+ "face1RectDict"
+ "face2RectDict"
+ "faceAssistedSkinGainsToMatch.count"
+ "faceAssistedSkinGainsToMatch[(__bridge id)kCCPMetadata_continuousFDTimes]"
+ "faceAssistedSkinGainsToMatch[(__bridge id)kCCPMetadata_minDistSkinToWhiteMapping]"
+ "faceAssistedSkinGainsToMatch[(__bridge id)kCCPMetadata_skinColorSampleNum]"
+ "faceAssistedSkinGainsToMatch[(__bridge id)kCCPMetadata_skinColorSampleVariance]"
+ "faceAssistedSkinGainsToMatch[(__bridge id)kCCPMetadata_wpBgLogRatio]"
+ "faceAssistedSkinGainsToMatch[(__bridge id)kCCPMetadata_wpRgLogRatio]"
+ "faceAssistedSkinGainsToMatch[(__bridge id)kCCPMetadata_wpSkinBgLogRatio]"
+ "faceAssistedSkinGainsToMatch[(__bridge id)kCCPMetadata_wpSkinRgLogRatio]"
+ "faceDataDict"
+ "faceRectDict"
+ "failed to setup AWB allocator"
+ "figTexDescr"
+ "filterHConfig"
+ "filterVConfig"
+ "flashCalibrationData"
+ "found"
+ "fullWidth != 0 && fullHeight != 0"
+ "fullWindowStatsData"
+ "generateLinearRGBATexture:"
+ "geometryData.inputTextureSize.width != 0 && geometryData.inputTextureSize.height != 0"
+ "getTileStatsRegion:validBufferRect:ltmGeometryData:toDriverInput:"
+ "getTileStatsRegionWithMetadata:cropRectLTMInCoords:ltmInDownsamplingRatio:tileStatsRegionLTMInCoordsDictOut:"
+ "getTransformCropRectFromSensorCoordsToValidBufferCoordsWithMetadata:validBufferRect:"
+ "globalFaceHistStat"
+ "globalHist"
+ "globalHistBuffer"
+ "hasEyeCovering"
+ "hasFaceMask"
+ "highCCT"
+ "histConfig"
+ "hrGainDownRatio >= 1.0f"
+ "i28@0:8^f16f24"
+ "i28@0:8^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16B24"
+ "i32@0:8@16^{CAWBAFE=^^?i^{CDualLEDsWhitePointProjector}{?=[9f][9f][6{?=fffff}]{?=[6f][6f][6f][6f][6f][6f]}[3{?=ff}][3{?=ff}][3{?=ff}][3{?=ff}]BB}^{CAWBAFEFDAssist}^{CAWBAFEPhotometerAssistPenrose}^{sPhotometerAWBMetadata}^{_FE_3A_Stats_H15}^{_FE_3A_Stats_H15}^{_TILE_Stat_Elem}^{_AEAWB_Stat_Elem}^{_HighResAWBAE_Stat_Elem}^I{sFEStatCSCConfig=[9s][9s][3s][3S][3S][2S]C}{sFEStatColorHistConfig=[15S][16C]SISI}ISSSBI[3I][3I][3[3i]][3[3i]]IBBBIIi[3S][3S]IffSfffffff{sAWBInternalParams=SSBBBffffffffffffffffffffI[1024I]}B{sAWBDigitalFlashSkyParams=iBffffffff}iBfff[1024I][1024I][6[4s]][3S][9s][2S][2S][13S][3S][32S]S*[1024C][6[1024C]][6s]CSSSSfSSSSB[3I]fSiBi[30[2s]]I[8[3S]]I[6[9s]]{sCSensorCalGain=SSSS}SSSSBI[4I]II{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}ffBBBBBfii[3I]^{fdAWBMetaData}[150[4S]]IBB{sWPStableZoneControlTable={sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}}BBCCQSS^{sMetaData}[3S]iBi[2f]f[30[2s]][6I][6I]B[6S]S[32S]B[192f]{sAWBTimelapseParams=BBI{sAWBTimelapseSmoothingState=ff[3f][3f]fffSB}}f{sCIspCmdChColorCalIdealSet=ISS(?=I{sCIspControllerCmdHdrChInfo=b16b15b1})SSSS}Bi{sUnagiParams=i}C}24"
+ "i32@0:8^{LTMTuning=ffffffffffffffffffffffffffff}16@24"
+ "i32@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16@24"
+ "i40@0:8@16@24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32"
+ "i40@0:8r^{sLtmComputeInput=[3072f][64f][1024f][48f][48f][64f][64f][65f][48f]ffffffffffffS[9f][192f]fffBB[48f]f}16r^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBiBif}C[6{LTMTuning=ffffffffffffffffffffffffffff}]B}24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}32"
+ "i40@0:8r^{sLtmComputeInput_SOFTISP={sLtmComputeInput=ffff[12288f][256f][1024f][64f][48f][48f][256f][256f][256f][48f][192f][48f]fffffffffffffS[9f][192f]fff[192f][768f][192f]ff}BB}16r^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}32"
+ "i48@0:8@16@24@32^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}40"
+ "i48@0:8r^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16r^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24^{sLtmComputeInput=[3072f][64f][1024f][48f][48f][64f][64f][65f][48f]ffffffffffffS[9f][192f]fffBB[48f]f}32^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBiBif}C[6{LTMTuning=ffffffffffffffffffffffffffff}]B}40"
+ "i48@0:8r^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16r^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24^{sLtmComputeInput_SOFTISP={sLtmComputeInput=ffff[12288f][256f][1024f][64f][48f][48f][256f][256f][256f][48f][192f][48f]fffffffffffffS[9f][192f]fff[192f][768f][192f]ff}BB}32^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}40"
+ "i56@0:8@16B24B28B32B36^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}40^{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]B}{?=IIIIIIIIiBI}}48"
+ "i56@0:8@16^{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]B}{?=IIIIIIIIiBI}}24@32@40@48"
+ "i60@0:8@16@24B32B36B40^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}44^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}52"
+ "i60@0:8@16@24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32B40B44B48^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}52"
+ "i64@0:8@16@24B32B36B40^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}44^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}52B60"
+ "i64@0:8@16^{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]B}{?=IIIIIIIIiBI}}24@32@40@48@56"
+ "i68@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24f56^@60"
+ "i72@0:8@16@24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32B40B44B48B52B56B60^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}64"
+ "idealCalibrations"
+ "idealColorCalHighCCT"
+ "idealColorCalLowCCT"
+ "idealColorCalibrations"
+ "idealColorCals"
+ "idealColourCalibrations dictionary not valid"
+ "initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:"
+ "initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:"
+ "initialize"
+ "inputBufferRect"
+ "inputData->ev0Ratio > 0"
+ "inputData->gainDigi > 0"
+ "inputData->hdrRatio > 0"
+ "inputData->overflowDGain > 0"
+ "internalMIWBMetadata"
+ "internalMetadata"
+ "internalSpatialCCMMetadata"
+ "isValidAWBParams"
+ "ispDGainMetadata"
+ "linearCompressedRGBATexture"
+ "linearRGBATexture"
+ "linearRGBATexture && FigMetalIsValid( linearRGBATexture )"
+ "localHist"
+ "localHistBuffer"
+ "localHistTmpBuffer"
+ "localHistograms"
+ "lowCCT"
+ "lscGainData"
+ "lscGainsTex.textureType == MTLTextureType2DArray"
+ "lscModulationWeight"
+ "ltmMetadata"
+ "maxGain >= ( 1 << (12) )"
+ "metadata.count"
+ "metadata[(id)kFigCapturePropertyValue_ispDGain]"
+ "metadata[(id)kFigCaptureStreamMetadata_CCT]"
+ "metalContext"
+ "minimumAdaptiveHC_SIFR"
+ "mixLightCCMConfig"
+ "moduleConfig[@\"Exposure\"][@\"LuxModel\"][@\"Scale\"]"
+ "moduleConfig[@\"Exposure\"][@\"LuxModel\"][@\"ScaleShift\"]"
+ "newMetadata"
+ "objectForKey:"
+ "outStatsParams"
+ "pPointEntry"
+ "pSkinToWhiteLutEntry"
+ "postTintConfig"
+ "previewMetadata"
+ "previewMetadata[(id)kFigCaptureStreamMetadata_AWBComboBGain]"
+ "previewMetadata[(id)kFigCaptureStreamMetadata_AWBComboGGain]"
+ "previewMetadata[(id)kFigCaptureStreamMetadata_AWBComboRGain]"
+ "projConfig[@\"BoundingEllipsesModel\"][i]"
+ "projConfig[@\"BoundingEllipsesModel\"][i][j]"
+ "projConfig[@\"MatrixRGBToXYZ\"][i]"
+ "projConfig[@\"MatrixXYZToRGB\"][i]"
+ "projConfig[@\"UseFlashCCMMixing\"]"
+ "projConfig[@\"UseQuantileLuxLevels\"]"
+ "projPoints"
+ "r"
+ "ratioConfig"
+ "rawLSCData"
+ "rawSensorHeight"
+ "rawSensorWidth"
+ "rawSensorWidth && rawSensorHeight"
+ "reSizedAnstSkinMaskTex"
+ "result"
+ "ret"
+ "rgGainColorMatchingModel"
+ "rgbImageUInt16 && FigMetalIsValid( rgbImageUInt16 )"
+ "roiRectConverted"
+ "scanner"
+ "schemeConfig"
+ "secondaryBGain"
+ "secondaryRGain"
+ "sensorClockFrequency"
+ "sensorReadoutRectConverted"
+ "sensorSpaceToValidBufferSpaceTransform"
+ "setComputeHDRCurvesWoFaceBoost:"
+ "setDeepZoomRatio:"
+ "setFileID"
+ "setFileOrigin"
+ "setInputBufferRect:"
+ "setLscModulationWeight:"
+ "setMinimumAdaptiveHC_SIFR:"
+ "setRawSensorHeight:"
+ "setRawSensorWidth:"
+ "setSensorSpaceToValidBufferSpaceTransform:"
+ "setTileStatsROIRect:"
+ "setUndoHRGainDownRatio:"
+ "smallPixelsPtr"
+ "softisp.awb.spatialCCM.blueGainRatio"
+ "softisp.awb.spatialCCM.redGainRatio"
+ "srcBufAddr"
+ "startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:"
+ "statLTM"
+ "status == 0 "
+ "succeed"
+ "td"
+ "tempColorCalibrations"
+ "texData"
+ "thumbnail"
+ "thumbnailBuffer"
+ "tileStatsROIRect"
+ "tmpGainsArray"
+ "trimScaleConfig"
+ "tuningTable"
+ "tuningTable[j][@\"Index\"]"
+ "tuningTable[j][@\"Weight\"]"
+ "unagi_trace"
+ "undoHRGainDownRatio"
+ "v32@0:8@16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24"
+ "v32@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24"
+ "v380@0:8^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]B}{?=IIIIIIIIiBI}}24"
+ "v40@0:8@16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24@32"
+ "v40@0:8@16^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32"
+ "v40@0:8@16i24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}28I36"
+ "v48@0:8@16@24@32@40"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "v56@0:8@16^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}24^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}32@40^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}48"
+ "v56@0:8@16i24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}28^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}36@44B52"
+ "v60@0:8@16i24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}28^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}36^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}44@52"
+ "v60@0:8@16i24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}28^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}36@44B52I56"
+ "v60@0:8@16i24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}28^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}36^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}44@52"
+ "v64@0:8{CGAffineTransform=dddddd}16"
+ "validAreaToCanonicalThumbnailAreaRatio <= ( 16 )"
+ "validRectConverted"
+ "validRectInBufferCoords.size.width <= fullWidth && validRectInBufferCoords.size.height <= fullHeight"
+ "validRectInBufferCoords.size.width <= validRectInSensorReadoutCoords.size.width && validRectInBufferCoords.size.height <= validRectInSensorReadoutCoords.size.height"
+ "value"
+ "wbLogRatios=[%.3f, %.3f], wbSkinLogRatios=[%.3f, %.3f], continuousFDTimes=%d, skinColorSampleNum=%d, skinColorSampleVariance=%.3f, minDistSkinToWhiteMapping=%.3f"
+ "wbTmRGBTex"
+ "wblr=[%d, %d], wbslr=[%d, %d], cfdt=%d, scsn=%d, scsv=%d, mdstwm=%d"
+ "width >= ( 480 ) && height >= ( 320 )"
+ "windowStatsData"
+ "xCoordinateConfig"
+ "xtoCCT"
+ "yThConfig"
+ "{?=\"LumShift\"I\"CoeffAvgY\"[3I]\"CoeffMaxY\"[3I]\"AvgYOffset\"I}"
+ "{?=\"luma\"{?=\"LumShift\"I\"CoeffAvgY\"[3I]\"CoeffMaxY\"[3I]\"AvgYOffset\"I}\"globalHist\"{?=\"Enable\"B\"YHistSel\"S\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"Offset\"[4I]\"Scale\"[4f]}\"globalFaceHist\"{?=\"Enable\"B\"YHistSel\"S\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"Offset\"[4I]\"Scale\"[4f]}\"localHist\"{?=\"Enable\"B\"SelInput\"I\"LocalHistShift\"I\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"StrideX\"I\"StrideY\"I\"BlockSizeX\"I\"BlockSizeY\"I\"Offset\"I\"Scale\"I\"ThreLo\"I\"ThreHi\"I\"enableAntiAliasing\"B\"SubBin\"I\"ClipValidIdx\"B\"HistCoeff\"[25I]\"enableHiResLocalHistogram\"B}\"thumbnail\"{?=\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"BlockSizeX\"I\"BlockSizeY\"I\"OffsetX\"I\"OffsetY\"I\"genMethod\"i\"portraitOrientated\"B\"ThumbAvgRecipNumPix\"I}}"
+ "{CGAffineTransform=\"a\"d\"b\"d\"c\"d\"d\"d\"tx\"d\"ty\"d}"
+ "{CGAffineTransform=dddddd}16@0:8"
+ "{CGAffineTransform=dddddd}56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "{sCLRProcHITHStat_SOFTISP=\"thumbnailWindow\"I\"thumbnailEnable\"[6S]\"thumbnailDownsampleX\"S\"thumbnailDownsampleY\"S\"thumbnailTotal\"I\"localHistWindow\"I\"localHistEnable\"S\"localHistBinSize\"S\"localHistBlockSizeX\"S\"localHistBlockSizeY\"S\"localHistStrideX\"S\"localHistStrideY\"S\"localHistNumHorBlocks\"S\"localHistNumVerBlocks\"S\"localHistCountBitShift\"C\"globalHistEnable\"S\"globalHistWindow\"I\"globalFaceHistEnable\"S\"globalFaceHistWindow\"I\"thumbnailStat\"^v\"thumbnailOffset\"I\"thumbnailStatSize\"I\"localHistStat\"^v\"localHistOffset\"I\"localHistStatSize\"I\"globalHistStat\"^v\"globalHistOffset\"I\"globalHistStatSize\"I\"globalFaceHistStat\"^v\"globalFaceHistOffset\"I\"globalFaceHistStatSize\"I\"calculatedOnPortraitOrientation\"B\"gridOriginX\"I\"gridOriginY\"I\"localHistogramOriginalTilePixelCount\"I\"localHistLowThreshold\"I\"localHistHighThreshold\"I}"
+ "{sLtmComputeInput_SOFTISP=\"ltmComputeInput\"{sLtmComputeInput=\"rotationMagnitude\"f\"rotationMagnitudeDeltaIIR\"f\"rotationMagnitudeDeltaFiltered\"f\"thumbHistBlendingWeight\"f\"localHist\"[12288f]\"averageLocalHist\"[256f]\"globalHist\"[1024f]\"globalHist2\"[64f]\"tMaxArray\"[48f]\"nLumArray\"[48f]\"thumbnailHist\"[256f]\"thumbnailHistEV0\"[256f]\"thumbnailLumaHist\"[256f]\"faceWeightForTone\"[48f]\"fmapHFF\"[192f]\"faceWeightForHistBlend\"[48f]\"faceFraction\"f\"sceneLux\"f\"bin0Ratio\"f\"pixelCountRatio\"f\"exposureRatio\"f\"exposureBias\"f\"preBiasExposureRatio\"f\"faceExposureRatio\"f\"darkExposureRatio\"f\"luminanceRatio\"f\"flareScale\"f\"rGainRatio\"f\"bGainRatio\"f\"gamutSizeIndex\"S\"ccm\"[9f]\"ccmWeights\"[192f]\"ccmMixFactor\"f\"eit\"f\"darkEit\"f\"ltcGridScaleLogLumaThumb\"[192f]\"blendingMaskInputTh\"[768f]\"CBBrightMap\"[192f]\"CBLowlightDampWeight\"f\"faceBiasScaler\"f}\"LTMHazeCorrectionOff\"B\"useBt709\"B}"
+ "{sLtmComputeMeta_SOFTISP=\"ltmComputeMeta\"{sLtmComputeMeta=\"useLinearLTCs\"B\"useSpatialCCM\"B\"useGlobalCCM\"B\"useDigitalFlash\"B\"useFlash\"B\"bSoftGainOnly\"B\"gammaCurve\"i\"faceLTMVer\"C\"CBVer\"C\"updateMixLUT\"B}\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B\"channel\"C\"enableHiResLocalHistogram\"B}"
+ "{sLtmComputeMeta_SOFTISP=\"ltmComputeMeta\"{sLtmComputeMeta=\"useLinearLTCs\"B\"useSpatialCCM\"B\"useGlobalCCM\"B\"useDigitalFlash\"B\"useFlash\"B\"gammaCurve\"i\"updateMixLUT\"B\"levelSmoothNumPasses\"i\"levelSmoothCenterWeight\"f}\"channel\"C\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B}"
+ "{sLtmComputeOutput=\"LTC\"[49344f]\"averageLTC\"[257f]\"globalLUT\"[257f]\"rgbToneCurve\"[257f]\"rgbToneCurveInputMode\"i\"spatialCCM\"[5184f]\"WMixLUT\"[257f]\"midLuminance\"f\"eit\"f\"encodedExpRatio\"f\"bWMixLUTUpdated\"b1\"bCCMUpdated\"b1\"bLTMUpdated\"b1\"bGlobalLUTUpdated\"b1\"bRgbToneCurveUpdated\"b1\"rsvd\"b3\"LTCBright\"[49344f]}"
+ "{sRefDriverInputs_SOFTISP=\"HROn\"B\"hrGainDownRatio\"S\"exposureTime\"I\"gainAnal\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigi\"I\"hardIspDGain\"f\"softIspDGain\"f\"expBias\"S\"realizedExpBias\"S\"hdrRatio\"S\"ev0Ratio\"S\"overflowDGain\"I\"faceExpRatioFiltered\"f\"panoExpRatio\"S\"bLTMSingleFrameMode\"B\"ltmProcMode\"C\"bracketingMode\"C\"bracketingExpRatio\"I\"gainDigiSensor\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"luxLevel\"f\"useSpatialCCM\"B\"channel\"C\"flashStatus\"B\"isHLGMode\"B\"LTMGridConfig\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"localHistGridConfig\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"flashMixPercentage\"[512S]\"flashProjMixWeighting\"f\"tileStatsRegion\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"ccm\"{sAWBColorCorrectionMatrix_local=\"coeff\"[9(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})]}\"isLEDMainFlashforAWB\"B\"awbGains\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsSkinOnly\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsFlashProj\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"fdAWBChistMixFactor\"I\"awbColorspace\"C\"faceInfo\"{sFaceInfo_SOFTISP=\"rectArray\"[10{sCIspFDRect=\"x\"i\"y\"i\"width\"I\"height\"I}]\"primaryFaceIndex\"I\"numFaces\"I}\"forceDisableFaceBoost\"B\"gammaCurve\"i\"useHighlightCompression\"B\"useAdaptiveHighlightCompression\"B\"highlightCompressionGain\"f\"isSIFRFrame\"B\"LTMHazeCorrectionOff\"B\"useBt709\"B\"useHazeCorrection\"B\"hazeCorrection\"\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B\"faceBiasScaler\"f\"faceLTMVer\"C\"CBVer\"C}"
+ "{{%g, %g}, {%g, %g}}"
- "\tA\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc5"
- "'AEAverage' not found"
- "'AETarget' not found"
- "+[LTMExtractMetadata compareAWBMetadata:withReference:]"
- "+[LTMExtractMetadata extractAWBMetadataFromMetadata:validBufferRect:toDriverInput:]"
- "+[LTMExtractMetadata extractAWBMetadataFromRawMetadata:toDriverInput:]"
- "+[LTMExtractMetadata extractCCMFromMetadata:toDriverInput:]"
- "+[LTMExtractMetadata extractFromRawMetadata:toDriverInput:]"
- "+[LTMExtractMetadata extractRectanglesFrom:validBufferRect:ltmGeometry:]"
- "+[LTMExtractMetadata getTileStatsRegion:validBufferRect:toDriverInput:]"
- "+[LTMMetadataWriter _addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:]"
- "+[LTMMetadataWriter _addLocalClippingDataToMetadata:statistics:geometryData:]"
- "+[LTMMetadataWriter _addLocalHistToMetadata:statistics:geometryData:]"
- "+[LTMMetadataWriter _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:]"
- "+[LTMMetadataWriter createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:]"
- "-[AWBAlgorithm configWithSetFile:metadata:awbParams:]"
- "-[AWBProcessor purgeResources]"
- "-[AWBStatistics configWithRegs:]"
- "-[AWBStatistics configWithRegs:metadata:cameraInfo:]"
- "-[AWBStatistics configWithSetFile:metadata:cameraInfo:]"
- "-[LTMComputeRef computeLTM:withMetadata:to:]"
- "-[LTMComputeRef init]"
- "-[LTMCurvesCompute compute]"
- "-[LTMCurvesCompute initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:]"
- "-[LTMDriverRef computeLtmComputeInput:withMetadata:to:computeInputMetadata:]"
- "-[LTMDriverRef init]"
- "-[LTMExtractMetadata extractFrom:toDriverInput:ltmGeometry:]"
- "-[LTMExtractMetadata init]"
- "-[LTMGeometryData initWithInputTextureWidth:height:]"
- "-[LTMGeometryData setCropRect:sourceRect:]"
- "-[LTMProcessor createLTMComputer]"
- "-[LTMProcessor createLTMInTextureFromRGBAFloatTex:]"
- "-[LTMProcessor generateLinearRGBATexture]"
- "-[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:]"
- "-[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:]"
- "-[LTMStatsCompute encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:]"
- "<<<< AWBAlgorithm >>>> %s:                  %5d %5d %5d"
- "<<<< AWBAlgorithm >>>> %s:   C1Offset  = %5d"
- "<<<< AWBAlgorithm >>>> %s:   C1Scale   = %5d"
- "<<<< AWBAlgorithm >>>> %s:   C2Offset  = %5d"
- "<<<< AWBAlgorithm >>>> %s:   C2Scale   = %5d"
- "<<<< AWBAlgorithm >>>> %s:   CCMCoef[9]   = %5d %5d %5d"
- "<<<< AWBAlgorithm >>>> %s:   CSCChromaScale[2] = %5d %5d"
- "<<<< AWBAlgorithm >>>> %s:   CSCCoef[9]   = %5d %5d %5d"
- "<<<< AWBAlgorithm >>>> %s:   CSCMax[3]    = %5d %5d %5d"
- "<<<< AWBAlgorithm >>>> %s:   CSCMin[3]    = %5d %5d %5d"
- "<<<< AWBAlgorithm >>>> %s:   CSCOffset[3] = %5d %5d %5d"
- "<<<< AWBAlgorithm >>>> %s:   CSC_CS            = %5d"
- "<<<< AWBAlgorithm >>>> %s:   YThd[15]  = %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d"
- "<<<< AWBAlgorithm >>>> %s:   count[16] = %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d"
- "<<<< AWBAlgorithm >>>> %s:   numTilesX         = %d"
- "<<<< AWBAlgorithm >>>> %s:   numTilesY         = %d"
- "<<<< AWBAlgorithm >>>> %s:   winRegionWidth    = %3d ( %4d )"
- "<<<< AWBAlgorithm >>>> %s: --- ---------- ---"
- "<<<< AWBAlgorithm >>>> %s: --- CSCConfig ---"
- "<<<< AWBAlgorithm >>>> %s: --- ColorHistConfig ---"
- "<<<< AWBAlgorithm >>>> %s: --- ext ---"
- "<<<< AWBAlgorithm >>>> %s: --- sMetaData ---"
- "<<<< AWBAlgorithm >>>> %s: AWBFaceAssistedBehaviorMode_MatchProvidedSkinGains enabled"
- "<<<< AWBAlgorithm >>>> %s: Face rectangle clipped by valid buffer rect!"
- "<<<< AWBAlgorithm >>>> %s: ISP AWB     CCM[%d] (%f)  --- SOFTISP CCM[%d] (%f)"
- "<<<< AWBAlgorithm >>>> %s: ISP EIT %llu --- SOFTISP EIT %llu"
- "<<<< AWBAlgorithm >>>> %s: ISP RAWPROC CCM[%d] (%f)  --- SOFTISP CCM[%d] (%f)"
- "<<<< AWBAlgorithm >>>> %s: Platform identifier not supported!"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.aeAverage               = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.aeTarget                = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.exposureTime            = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.gainAnal.v16            = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.gainDigi.v16            = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.gainDigiSensor.v16      = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.luxLevel                = %12.6f"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.luxLevelHigh            = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.luxLevelLow             = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->ae.sceneBrightnessForLux   = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->awb.isDefaultSetting       = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->frameRate                  = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->isReplay                   = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->masterCam                  = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->masterCamPreview           = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->maxLSgainUnadjusted        = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->zoom.fesOutputHeight       = %12d"
- "<<<< AWBAlgorithm >>>> %s: pMetaData->zoom.fesOutputWidth        = %12d"
- "<<<< AWBAlgorithm >>>> %s: sizeAWBWindows[0]                     = %12d"
- "<<<< AWBProcessor >>>> %s: Prepare to process with registers"
- "<<<< AWBProcessor >>>> %s: Prepare to process without registers"
- "<<<< AWBStats >>>> %s:                    %5d %5d %5d"
- "<<<< AWBStats >>>> %s:     C1delta, C2delta    = %5d, %5d"
- "<<<< AWBStats >>>> %s:     C1min  , C1max      = %5d, %5d"
- "<<<< AWBStats >>>> %s:     C2min  , C2max      = %5d, %5d"
- "<<<< AWBStats >>>> %s:     YThd[16]    = %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d"
- "<<<< AWBStats >>>> %s:     Ymin   , Ymax       = %5d, %5d"
- "<<<< AWBStats >>>> %s:     coeff[9]     = %5d %5d %5d"
- "<<<< AWBStats >>>> %s:     condSel         = %5d"
- "<<<< AWBStats >>>> %s:     countClipEn         = %5d"
- "<<<< AWBStats >>>> %s:     countClipEn     = %5d"
- "<<<< AWBStats >>>> %s:     count[16] = %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d %3d"
- "<<<< AWBStats >>>> %s:     debiasGain[3]   = %7.5f %7.5f %7.5f"
- "<<<< AWBStats >>>> %s:     debiasMax[3]    = %7.5f %7.5f %7.5f"
- "<<<< AWBStats >>>> %s:     debiasMin[3]    = %7.5f %7.5f %7.5f"
- "<<<< AWBStats >>>> %s:     debiasOffset[3] = %7.5f %7.5f %7.5f"
- "<<<< AWBStats >>>> %s:     distMax             = %u"
- "<<<< AWBStats >>>> %s:     enable          = %5d"
- "<<<< AWBStats >>>> %s:     gain[3]     = %7.5f %7.5f %7.5f"
- "<<<< AWBStats >>>> %s:     gammaOffsetIn[3]          = %5d %5d %5d"
- "<<<< AWBStats >>>> %s:     gammaOffsetOut[3]         = %5d %5d %5d"
- "<<<< AWBStats >>>> %s:     lut[0, 1, ... , 255, 256] = %5d %5d ... %5d %5d"
- "<<<< AWBStats >>>> %s:     max[3]       = %7.5f %7.5f %7.5f"
- "<<<< AWBStats >>>> %s:     min[3]       = %7.5f %7.5f %7.5f"
- "<<<< AWBStats >>>> %s:     offset              = %5d"
- "<<<< AWBStats >>>> %s:     offsetC1    = %5d"
- "<<<< AWBStats >>>> %s:     offsetC2    = %5d"
- "<<<< AWBStats >>>> %s:     offsetIn                  = %5d"
- "<<<< AWBStats >>>> %s:     offsetIn[3]  = %7.5f %7.5f %7.5f"
- "<<<< AWBStats >>>> %s:     offsetOut                 = %5d"
- "<<<< AWBStats >>>> %s:     offsetOut[3] = %7.5f %7.5f %7.5f"
- "<<<< AWBStats >>>> %s:     offset[3]   = %5d %5d %5d"
- "<<<< AWBStats >>>> %s:     scaleC1     = %5d"
- "<<<< AWBStats >>>> %s:     scaleC2     = %5d"
- "<<<< AWBStats >>>> %s:     scale[2]     = %5d %5d"
- "<<<< AWBStats >>>> %s:     statSel         = %5d"
- "<<<< AWBStats >>>> %s:   Fix enablement status [IBLC gain cap | Clip pix pedestal] = %s"
- "<<<< AWBStats >>>> %s:   IBLC gain     = %f"
- "<<<< AWBStats >>>> %s:   ccm :"
- "<<<< AWBStats >>>> %s:   csc :"
- "<<<< AWBStats >>>> %s:   csc2 :"
- "<<<< AWBStats >>>> %s:   debiasCfg ( all other than ColorHist ) :"
- "<<<< AWBStats >>>> %s:   firstPix      = %d"
- "<<<< AWBStats >>>> %s:   gam :"
- "<<<< AWBStats >>>> %s:   greenAverage  = %d"
- "<<<< AWBStats >>>> %s:   ispDGain      = %f"
- "<<<< AWBStats >>>> %s:   pixFilt ( %d ) :"
- "<<<< AWBStats >>>> %s: --- AWBStatConfig ---"
- "<<<< AWBStats >>>> %s: Face rectangle clipped by valid buffer rect!"
- "<<<< LTMAlgorithm >>>> %s: \n---- Comparison the AWB metadata with AWB metadata from RawMetadata\nfdAWBChistMixFactor     awb:%d, raw:%d\nawbColorspace           awb:%d, raw:%d\nisLEDMainFlashforAWB    awb:%d, raw:%d\nawbGainsSkinOnly.r      awb:%d, raw:%d\nawbGainsSkinOnly.b      awb:%d, raw:%d\nawbGainsFlashProj.r     awb:%d, raw:%d\nawbGainsFlashProj.b     awb:%d, raw:%d\n--------------------------------------------------"
- "<<<< LTMAlgorithm >>>> %s:  ---- Configured vs ISP RawMetadata Tilestats Region ---- "
- "<<<< LTMAlgorithm >>>> %s:  tile.height   cfg:%d, isp:%d "
- "<<<< LTMAlgorithm >>>> %s:  tile.width    cfg:%d, isp:%d "
- "<<<< LTMAlgorithm >>>> %s:  tile.x        cfg:%d, isp:%d "
- "<<<< LTMAlgorithm >>>> %s:  tile.y        cfg:%d, isp:%d "
- "<<<< LTMAlgorithm >>>> %s: Can't allocate the metadata"
- "<<<< LTMAlgorithm >>>> %s: Exposure Ratio: %f"
- "<<<< LTMAlgorithm >>>> %s: Fail to create LTM metadata"
- "<<<< LTMAlgorithm >>>> %s: Fail to process LTM compute"
- "<<<< LTMAlgorithm >>>> %s: Fail to process LTM compute for HLG"
- "<<<< LTMAlgorithm >>>> %s: Fail to process LTM driver"
- "<<<< LTMAlgorithm >>>> %s: FigMetalAllocator size is forced to: < %lu >"
- "<<<< LTMAlgorithm >>>> %s: LTM tuning params is nil"
- "<<<< LTMAlgorithm >>>> %s: LTM's dehaze tuning params is nil"
- "<<<< LTMAlgorithm >>>> %s: LTM's figMetalAllocator resources not correctly released"
- "<<<< LTMAlgorithm >>>> %s: LTMCurvesCompute is nil"
- "<<<< LTMAlgorithm >>>> %s: Missing kCCPMetadata_tileStatsRegionInRaw"
- "<<<< LTMAlgorithm >>>> %s: Missing sCIspMetaDataSharedAE"
- "<<<< LTMAlgorithm >>>> %s: Missing sCIspMetaDataSharedAWB"
- "<<<< LTMAlgorithm >>>> %s: Using SOFTISP METADATA for configuring tileStatsRegion in LTM "
- "<<<< LTMAlgorithm >>>> %s: _computeLTM is nil"
- "<<<< LTMAlgorithm >>>> %s: _driverLTM is nil"
- "<<<< LTMAlgorithm >>>> %s: clippingData malloc failed"
- "<<<< LTMAlgorithm >>>> %s: couldn't initialize LTMComputeRef instance"
- "<<<< LTMAlgorithm >>>> %s: couldn't initialize LTMDriverRef instance"
- "<<<< LTMAlgorithm >>>> %s: error of processing an LTMCompute"
- "<<<< LTMAlgorithm >>>> %s: error of processing an LTMDriver"
- "<<<< LTMAlgorithm >>>> %s: globalLUT malloc failed"
- "<<<< LTMAlgorithm >>>> %s: ltmLTC malloc failed"
- "<<<< LTMAlgorithm >>>> %s: rawMetaData base address is NULL"
- "<<<< LTMAlgorithm >>>> %s: rgbToneCurve malloc failed"
- "<<<< LTMAlgorithm >>>> %s: spatialCCM malloc failed"
- "<<<< LTMAlgorithm >>>> %s: spatialCCMData is nil"
- "@\"LTMComputeRef\""
- "@\"LTMDriverRef\""
- "@\"LTMExtractMetadata\""
- "@\"LTMGeometryData\""
- "@\"NSData\""
- "@48@0:8^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}16^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}24^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}32@40"
- "@64@0:8^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}16^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}24@32@40B48B52B56B60"
- "AWB requires AbsoluteColorCalibrationData in setfile to configure."
- "AWB requires CSCConfig in setfile to configure."
- "AWB requires ColorCalIdeal in setfile to configure."
- "AWB requires register data to configure."
- "AWBAEConfig"
- "AWBAEConfig not found"
- "AWBAEStatsTileBitDepth"
- "AWBAEStatsTileBitDepth not found"
- "AWBAEStatsWindowBitDepth"
- "AWBAEStatsWindowBitDepth not found"
- "AWBAEWindowEndXY"
- "AWBAEWindowEndXY not found"
- "AWBAEWindowStartXY"
- "AWBAEWindowStartXY not found"
- "AWBAE_StatsDB_Gain"
- "AWBAE_StatsDB_Gain count incorrect"
- "AWBAE_StatsDB_Gain not found"
- "AbsoluteColorCalibrationData"
- "B24@0:8^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}16"
- "B32@0:8@16^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}24"
- "B40@0:8@16@24^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}32"
- "B40@0:8@16^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}24@32"
- "C1max"
- "C1max not found"
- "C1min"
- "C1min not found"
- "C2max"
- "C2max not found"
- "C2min"
- "C2min not found"
- "CCMCoeff"
- "CCMCoeff entry not found"
- "CCMMax"
- "CCMMax entry not found"
- "CCMMin"
- "CCMMin entry not found"
- "CCMOffsetIn"
- "CCMOffsetIn entry not found"
- "CCMOffsetOut"
- "CCMOffsetOut entry not found"
- "CSC2ChromaScale"
- "CSC2ChromaScale not found"
- "CSC2Coeff"
- "CSC2Coeff entry not found"
- "CSC2Max"
- "CSC2Max entry not found"
- "CSC2Min"
- "CSC2Min entry not found"
- "CSC2OffsetIn"
- "CSC2OffsetIn entry not found"
- "CSC2OffsetOut"
- "CSC2OffsetOut entry not found"
- "CSCChromaScale"
- "CSCChromaScale not found"
- "CSCConfig"
- "CameraColorProcessing_AWB_ResizedSkinMask"
- "CameraColorProcessing_AWB_WhiteBalancedTonemappedRGBThumbnail"
- "CameraColorProcessing_LTM_CompressHighlight"
- "CameraColorProcessing_LTM_CreateFromLuma"
- "CameraColorProcessing_LTM_CreateFromRGBA"
- "CameraColorProcessing_LTM_GlobaCCM_LTMIn"
- "CameraColorProcessing_LTM_HazeEstimation"
- "CameraColorProcessing_LTM_deHaze_LTMIn"
- "CameraColorProcessing_camYccDebugTex"
- "CameraColorProcessing_rgbLinearTex"
- "CameraColorProcessing_rgbcLinearTex"
- "CameraColorProcessing_srgbDebugTex"
- "CameraColorProcessing_srgbLinDebugTex"
- "CameraColorProcessing_yc1c2DebugTex"
- "ColorCalIdeal"
- "ColorHistConfig"
- "ColorHistCount"
- "ColorHistCount entry not found"
- "ColorHistDB_Gain"
- "ColorHistDB_Gain entry not found"
- "ColorHistDB_Max"
- "ColorHistDB_Max entry not found"
- "ColorHistDB_Min"
- "ColorHistDB_Min entry not found"
- "ColorHistDB_Offset"
- "ColorHistDB_Offset entry not found"
- "ColorHistOffsetC1"
- "ColorHistOffsetC1 not found"
- "ColorHistOffsetC2"
- "ColorHistOffsetC2 not found"
- "ColorHistRegionEndXY"
- "ColorHistRegionStartXY"
- "ColorHistScaleC1"
- "ColorHistScaleC1 not found"
- "ColorHistScaleC2"
- "ColorHistScaleC2 not found"
- "ColorHistYThd"
- "ColorHistYThd entry not found"
- "Config not found"
- "CountClipEn"
- "CountClipEn not found"
- "Dump3A.stats"
- "DumpsAEMetaData.data"
- "En"
- "En not found"
- "FIGMETALCONTEXT_CHECK_ERRCODE"
- "FigCapturePlatformID soft_FigCapturePlatformIdentifier()"
- "FigProcessorDebug"
- "FirstPix"
- "FirstPix not found"
- "Frame metadata did not contain LensShadingModulationWeight"
- "GammaLUT"
- "GammaLUT entry not found"
- "Gamma_offsetIn"
- "Gamma_offsetIn entry not found"
- "Gamma_offsetOut"
- "Gamma_offsetOut entry not found"
- "HorzInt"
- "HorzInt not found"
- "LTMComputeBase"
- "LTMComputeRef"
- "LTMCurvesCompute"
- "LTMDriverBase"
- "LTMDriverRef"
- "LTMExtractMetadata"
- "LTMGeometryData"
- "LTMInputTexture"
- "LTMInputTextureColorCorrected"
- "LTMInputTextureCompressed"
- "LTMMetadataWriter"
- "LTMMetadataWriter.m"
- "LTMStatisticsCalculation"
- "Max"
- "Max not found"
- "Min"
- "Min not found"
- "Missing sCIspMetaDataSharedAE"
- "Missing sCIspMetaDataSharedAWB"
- "PF0Sel"
- "PF0Sel not found"
- "PF1Sel"
- "PF1Sel not found"
- "PFC1Thd"
- "PFC1Thd not found"
- "PFC2Thd"
- "PFC2Thd not found"
- "PFConfig"
- "PFConfig not found"
- "PFLineDeltaC1"
- "PFLineDeltaC1 not found"
- "PFLineDeltaC2"
- "PFLineDeltaC2 not found"
- "PFLineOffset"
- "PFLineOffset not found"
- "PFLumaMinMax"
- "PFLumaMinMax not found"
- "Raw metadata missing."
- "Scale0"
- "Scale0 not found"
- "Scale1"
- "Scale1 not found"
- "SetFileData"
- "T@\"NSData\",R,N,V_setFileData"
- "T@\"NSDictionary\",&,N,V_registers"
- "T@\"NSDictionary\",&,N,V_setFileDict"
- "TileIntervals"
- "TileIntervals not found"
- "TileRegionEndXY"
- "TileRegionEndXY not found"
- "TileRegionStartXY"
- "TileRegionStartXY not found"
- "V"
- "VertInt"
- "VertInt not found"
- "[_stats[@\"histStats\"] length] == histStatsSizeInBytes is NULL"
- "[_stats[@\"tileStats\"] length] == tileStatsSizeInBytes is NULL"
- "[_stats[@\"windowStats\"] length] == windowStatsSizeInBytes is NULL"
- "^{CAWBAFE=^^?i^{CDualLEDsWhitePointProjector}{?=[9f][9f][6{?=fffff}]{?=[6f][6f][6f][6f][6f][6f]}[3{?=ff}][3{?=ff}][3{?=ff}][3{?=ff}]BB}^{CAWBAFEFDAssist}^{CAWBAFEPhotometerAssistPenrose}^{sPhotometerAWBMetadata}^{_FE_3A_Stats_H15}^{_FE_3A_Stats_H15}^{_TILE_Stat_Elem}^{_AEAWB_Stat_Elem}^{_HighResAWBAE_Stat_Elem}^I{sFEStatCSCConfig=[9s][9s][3s][3S][3S][2S]C}{sFEStatColorHistConfig=[15S][16C]SISI}ISSSBI[3I][3I][3[3i]][3[3i]]IBBBIIi[3S][3S]IffSffffff{sAWBInternalParams=SSBBBffffffffffffffffffffI[1024I]}B{sAWBDigitalFlashSkyParams=iBffffffff}iBfff[1024I][1024I][6[4s]][3S][9s][2S][2S][13S][3S][32S]S*[1024C][6[1024C]][6s]CSSSSfSSSSB[3I]fSiBi[30[2s]]I[8[3S]]I[6[9s]]{sCSensorCalGain=SSSS}SSSSBI[4I]II{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}ffBBBBBfii[3I]^{fdAWBMetaData}[150[4S]]IBB{sWPStableZoneControlTable={sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}}BBCCQSS^{sMetaData}[3S]iBi[2f]f[30[2s]][6I][6I]B[6S]S[32S]B[192f]{sAWBTimelapseParams=BBI{sAWBTimelapseSmoothingState=ff[3f][3f]fffSB}}f{sCIspCmdChColorCalIdealSet=ISS(?=I{sCIspControllerCmdHdrChInfo=b16b15b1})SSSS}Bi{sUnagiParams=i}C}"
- "^{LTMDriver=^^?{sLtmComputeInput=[3072f][64f][1024f][48f][48f][64f][64f][65f][48f]ffffffffffffS[9f][192f]fffBB[48f]f}{sLtmComputeMeta=BBBBBiBifC[6{LTMTuning=Bffffffffffffffffffffffffffff}]B}iB}"
- "^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}16@0:8"
- "_LTMIsReady"
- "_applyDefaultWriteOverridesForAWBGains"
- "_computeAWBStatsPipelineState"
- "_registers"
- "_setFileData"
- "_setFileDict"
- "_stats.count != 4"
- "ae_metadata"
- "anst_input"
- "anst_semantic_tiles"
- "anst_skin_mask"
- "anst_skin_mask_bytes"
- "awb-stat"
- "awbStats"
- "awb_input"
- "camYccDebugTex is NULL"
- "cmi_unsignedIntValueFromArrayWithKey:forIndex:defaultValue:found:"
- "computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:"
- "configAWBStatsDB"
- "configCSC"
- "configCSC2"
- "configColorHist"
- "configGAM"
- "configPixFilt"
- "configTiles"
- "configWindows"
- "configWithRegs:"
- "configWithRegs:metadata:cameraInfo:"
- "configWithSetFile:metadata:awbParams:"
- "configWithSetFile:metadata:cameraInfo:"
- "containsObject:"
- "createLTMComputer"
- "createLTMInTextureFromRGBAFloatTex:"
- "debugForModule:"
- "encodeLTMStatisticsCalculationOptimized:params:globalHistogram:localHistogram:thumbnail:"
- "extractRectanglesFrom:validBufferRect:ltmGeometry:"
- "f24@0:8r^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}16"
- "generateLinearRGBATexture"
- "getData"
- "getThumbnailTexture"
- "harvesting.enabled"
- "hasPrefix:"
- "hazeData"
- "hazeDataForLTM"
- "hazeThumbnailTexture"
- "highlightCompressionDataTexture"
- "i28@0:8^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}16B24"
- "i32@0:8@16^{CAWBAFE=^^?i^{CDualLEDsWhitePointProjector}{?=[9f][9f][6{?=fffff}]{?=[6f][6f][6f][6f][6f][6f]}[3{?=ff}][3{?=ff}][3{?=ff}][3{?=ff}]BB}^{CAWBAFEFDAssist}^{CAWBAFEPhotometerAssistPenrose}^{sPhotometerAWBMetadata}^{_FE_3A_Stats_H15}^{_FE_3A_Stats_H15}^{_TILE_Stat_Elem}^{_AEAWB_Stat_Elem}^{_HighResAWBAE_Stat_Elem}^I{sFEStatCSCConfig=[9s][9s][3s][3S][3S][2S]C}{sFEStatColorHistConfig=[15S][16C]SISI}ISSSBI[3I][3I][3[3i]][3[3i]]IBBBIIi[3S][3S]IffSffffff{sAWBInternalParams=SSBBBffffffffffffffffffffI[1024I]}B{sAWBDigitalFlashSkyParams=iBffffffff}iBfff[1024I][1024I][6[4s]][3S][9s][2S][2S][13S][3S][32S]S*[1024C][6[1024C]][6s]CSSSSfSSSSB[3I]fSiBi[30[2s]]I[8[3S]]I[6[9s]]{sCSensorCalGain=SSSS}SSSSBI[4I]II{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}ffBBBBBfii[3I]^{fdAWBMetaData}[150[4S]]IBB{sWPStableZoneControlTable={sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}}BBCCQSS^{sMetaData}[3S]iBi[2f]f[30[2s]][6I][6I]B[6S]S[32S]B[192f]{sAWBTimelapseParams=BBI{sAWBTimelapseSmoothingState=ff[3f][3f]fffSB}}f{sCIspCmdChColorCalIdealSet=ISS(?=I{sCIspControllerCmdHdrChInfo=b16b15b1})SSSS}Bi{sUnagiParams=i}C}24"
- "i32@0:8^{LTMTuning=Bffffffffffffffffffffffffffff}16@24"
- "i32@0:8^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}16@24"
- "i40@0:8@16@24^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}32"
- "i40@0:8r^{sLtmComputeInput=[3072f][64f][1024f][48f][48f][64f][64f][65f][48f]ffffffffffffS[9f][192f]fffBB[48f]f}16r^{sLtmComputeMeta=BBBBBiBifC[6{LTMTuning=Bffffffffffffffffffffffffffff}]B}24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}32"
- "i48@0:8@16B24B28^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}32^{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]}{?=IIIIIIIIiI}}40"
- "i48@0:8r^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}16r^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}24^{sLtmComputeInput=[3072f][64f][1024f][48f][48f][64f][64f][65f][48f]ffffffffffffS[9f][192f]fffBB[48f]f}32^{sLtmComputeMeta=BBBBBiBifC[6{LTMTuning=Bffffffffffffffffffffffffffff}]B}40"
- "i56@0:8@16^{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]}{?=IIIIIIIIiI}}24@32@40@48"
- "i60@0:8@16@24B32B36B40^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}44^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}52"
- "i60@0:8@16@24^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}32B40B44B48^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}52"
- "initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:"
- "lsc_tex"
- "ltm_LTC"
- "ltm_LTC_HLG"
- "ltm_LTC_HLG_SIFR"
- "ltm_LTC_SIFR"
- "ltm_LTC_withoutFaceBoost"
- "ltm_LTC_withoutFaceBoost_SIFR"
- "ltm_globalLUT"
- "ltm_globalLUT_HLG"
- "ltm_globalLUT_HLG_SIFR"
- "ltm_globalLUT_SIFR"
- "ltm_globalLUT_withoutFaceBoost"
- "ltm_globalLUT_withoutFaceBoost_SIFR"
- "ltm_rgbToneCurve"
- "ltm_rgbToneCurve_HLG"
- "ltm_rgbToneCurve_HLGS_SIFR"
- "ltm_rgbToneCurve_SIFR"
- "ltm_rgbToneCurve_withoutFaceBoost"
- "ltm_rgbToneCurve_withoutFaceBoost_SIFR"
- "ltm_stats_globalHist"
- "ltm_stats_globalHist_SIFR"
- "ltm_stats_localHist"
- "ltm_stats_localHist_SIFR"
- "ltm_stats_metadata"
- "ltm_stats_metadata_SIFR"
- "ltm_stats_thumbnail"
- "ltm_stats_thumbnail_SIFR"
- "miwb.magentaMitigation"
- "objectWithName:data:"
- "objectWithName:mutableData:"
- "objectWithName:pixelBytes:width:height:stride:pixelFormat:"
- "objectWithName:texture:"
- "photometerInfo is NULL"
- "portType is NULL"
- "printCurrentStatus"
- "print_SetFileConfigs"
- "print_awbStatCfg"
- "print_pMetaData"
- "registers"
- "rgbLinearTex is NULL"
- "rgbcLinDebugTex is NULL"
- "setData:"
- "setFileData"
- "setFileData nil or empty !!"
- "setFileDict"
- "setRegisters:"
- "setSetFileDict:"
- "sky_mask"
- "sky_mask_bytes"
- "softisp.awb"
- "softisp.awb.AWBBGain"
- "softisp.awb.AWBComboBGain"
- "softisp.awb.AWBComboBGainNormalized"
- "softisp.awb.AWBComboGGain"
- "softisp.awb.AWBComboGGainNormalized"
- "softisp.awb.AWBComboRGain"
- "softisp.awb.AWBComboRGainNormalized"
- "softisp.awb.AWBGGain"
- "softisp.awb.AWBRGain"
- "softisp.awb.AWBSkinBGain"
- "softisp.awb.AWBSkinGGain"
- "softisp.awb.AWBSkinRGain"
- "softisp.awb.CCTEstimate"
- "softisp.awb.aeLuxLevel"
- "softisp.awb.angleInfoRoll"
- "softisp.awb.bgLogRatio"
- "softisp.awb.ccm%d"
- "softisp.awb.cct"
- "softisp.awb.dngIlluminantHigh"
- "softisp.awb.dngIlluminantLow"
- "softisp.awb.ev0Ratio"
- "softisp.awb.faceRectHeight"
- "softisp.awb.faceRectWidth"
- "softisp.awb.faceRectX"
- "softisp.awb.faceRectY"
- "softisp.awb.faces"
- "softisp.awb.fdAWBChistMixFactor"
- "softisp.awb.flickerConfidenceAC"
- "softisp.awb.flickerConfidenceDC"
- "softisp.awb.flickerIRRatio"
- "softisp.awb.ispDGain"
- "softisp.awb.maxFaceIndex"
- "softisp.awb.modelname"
- "softisp.awb.photometerLuxLevel"
- "softisp.awb.platformID"
- "softisp.awb.rgLogRatio"
- "softisp.awb.useMetadataForCalibration"
- "softisp.ltm"
- "softisp.mtlallocator.size"
- "softisp.mtlallocator.wireMemory"
- "softisp.platformID.override"
- "softisp.softawb.allow_calculate_skin_mask"
- "softisp.softawb.digital_flash_version"
- "softisp.softawb.enableUnagiSkyFeedback"
- "softisp.softawb.face_assisted_mode"
- "softisp.softawb.maxSkinVarianceDiffSWideAndWide"
- "softisp.softawb.minSkinColorSampleNum"
- "softisp.softawb.mixAmbientWithFlashWP"
- "softisp.softawb.strobeBGain"
- "softisp.softawb.strobeRGain"
- "softisp.softawb.strobeWPointCCM.ccmDesatFactor"
- "softisp.softawb.strobeWPointCCM.luxLevel"
- "softisp.softawb.use_anod_rect_from_raw_metadata"
- "softisp.softawb.use_semantic_fd_awb"
- "softisp.softltm.adaptiveHCSlope"
- "softisp.softltm.calcGlobalHistOnROI"
- "softisp.softltm.computeCurvesWoFaceBoost"
- "softisp.softltm.computeHDRCurves"
- "softisp.softltm.doGlobalCCM"
- "softisp.softltm.dohaze"
- "softisp.softltm.enableAntiAliasing"
- "softisp.softltm.enablePreLTMHazeCorrection"
- "softisp.softltm.faceBiasScaler"
- "softisp.softltm.faceBiasScalerMin"
- "softisp.softltm.faceBiasThreshold"
- "softisp.softltm.faceBiasThresholdMin"
- "softisp.softltm.forceDisableHR"
- "softisp.softltm.forceDisableLTMFaceBoost"
- "softisp.softltm.forceDisableLTMFaceExposureRatio"
- "softisp.softltm.forceDisableLTMHazeCorrection"
- "softisp.softltm.forceHighlightCompressionForEveryFrame"
- "softisp.softltm.forceUseBt709"
- "softisp.softltm.isAdaptiveHighlightCompressionEnabled"
- "softisp.softltm.isHighlightCompressionEnabled"
- "softisp.softltm.ispDGainThreshold"
- "softisp.softltm.min_display_black"
- "softisp.softltm.min_display_black_forLTM"
- "softisp.softltm.reluC1"
- "softisp.softltm.reluC1_forLTM"
- "softisp.softltm.reluC2"
- "softisp.softltm.reluC2_forLTM"
- "softisp.softltm.reluC3"
- "softisp.softltm.reluC3_forLTM"
- "softisp.softltm.reluC4"
- "softisp.softltm.reluC4_forLTM"
- "softisp.softltm.reluC5"
- "softisp.softltm.reluC5_forLTM"
- "softisp.softltm.sr_min"
- "softisp.softltm.sr_min_forLTM"
- "softisp.softltm.sr_pow"
- "softisp.softltm.sr_pow_forLTM"
- "softisp.softltm.sr_sat"
- "softisp.softltm.sr_sat_forLTM"
- "softisp.softltm.sr_var"
- "softisp.softltm.sr_var_forLTM"
- "softisp.softltm.use_awb_tilestats_region"
- "spatial_ccm"
- "srgbDebugTex is NULL"
- "srgbLinDebugTex is NULL"
- "stats_camycc"
- "stats_header"
- "stats_hist"
- "stats_rgb"
- "stats_rgbc"
- "stats_srgb"
- "stats_srgblin"
- "stats_tiles"
- "stats_wbtm_rgb"
- "stats_windows"
- "stats_yc1c2"
- "tempNumber is NULL"
- "tileStatsConfig"
- "trimmed_chroma_hist"
- "v24@0:8^{?=ffffffffffffff}16"
- "v320@0:8^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}16{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]}{?=IIIIIIIIiI}}24"
- "v32@0:8@16^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}24"
- "v32@0:8^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}16^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}24"
- "v40@0:8@16@24@32"
- "v40@0:8@16^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}24@32"
- "v40@0:8@16^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}24^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}32"
- "v56@0:8@16i24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}28^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}36@44B52"
- "v60@0:8@16i24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}28^{sCLRProcHITHStat=I[6S]SSIISSSSSSSSCSI^vII^vII^vIIIIIII}36^{sRefDriverInputs=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBBffff[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo=[10{sCIspFDRect=iiII}]I}BiBBfBBBB[6{LTMTuning=Bffffffffffffffffffffffffffff}]Bf}44@52"
- "waitForIdle"
- "wbLogRatios=[%.3f, %.3f], wbSkinLogRatios=[%.3f, %.3f], continuousFDTimes=%d, skinColorSampleNum=%d"
- "yc1c2DebugTex is NULL"
- "{?=\"luma\"{?=\"LumShift\"I\"CoeffAvgY\"[3I]\"CoeffMaxY\"[3I]\"AvgYOffset\"I}\"globalHist\"{?=\"Enable\"B\"YHistSel\"S\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"Offset\"[4I]\"Scale\"[4f]}\"localHist\"{?=\"Enable\"B\"SelInput\"I\"LocalHistShift\"I\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"StrideX\"I\"StrideY\"I\"BlockSizeX\"I\"BlockSizeY\"I\"Offset\"I\"Scale\"I\"ThreLo\"I\"ThreHi\"I\"enableAntiAliasing\"B\"SubBin\"I\"ClipValidIdx\"B\"HistCoeff\"[25I]}\"thumbnail\"{?=\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"BlockSizeX\"I\"BlockSizeY\"I\"OffsetX\"I\"OffsetY\"I\"genMethod\"i\"ThumbAvgRecipNumPix\"I}}"
- "{?=ffffffffffffff}16@0:8"
- "{sCLRProcHITHStat=\"thumbnailWindow\"I\"thumbnailEnable\"[6S]\"thumbnailDownsampleX\"S\"thumbnailDownsampleY\"S\"thumbnailTotal\"I\"localHistWindow\"I\"localHistEnable\"S\"localHistBinSize\"S\"localHistBlockSizeX\"S\"localHistBlockSizeY\"S\"localHistStrideX\"S\"localHistStrideY\"S\"localHistNumHorBlocks\"S\"localHistNumVerBlocks\"S\"localHistCountBitShift\"C\"globalHistEnable\"S\"globalHistWindow\"I\"thumbnailStat\"^v\"thumbnailOffset\"I\"thumbnailStatSize\"I\"localHistStat\"^v\"localHistOffset\"I\"localHistStatSize\"I\"globalHistStat\"^v\"globalHistOffset\"I\"globalHistStatSize\"I\"gridOriginX\"I\"gridOriginY\"I\"localHistogramOriginalTilePixelCount\"I\"localHistLowThreshold\"I\"localHistHighThreshold\"I}"
- "{sLtmComputeMeta=\"useLinearLTCs\"B\"useSpatialCCM\"B\"useGlobalCCM\"B\"useDigitalFlash\"B\"useFlash\"B\"gammaCurve\"i\"updateMixLUT\"B\"levelSmoothNumPasses\"i\"levelSmoothCenterWeight\"f\"channel\"C\"tuningParametersOverride\"[6{LTMTuning=\"isValid\"B\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B}"
- "{sRefDriverInputs=\"HROn\"B\"hrGainDownRatio\"S\"exposureTime\"I\"gainAnal\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigi\"I\"hardIspDGain\"f\"softIspDGain\"f\"expBias\"S\"realizedExpBias\"S\"hdrRatio\"S\"ev0Ratio\"S\"overflowDGain\"I\"faceExpRatioFiltered\"f\"panoExpRatio\"S\"bLTMSingleFrameMode\"B\"ltmProcMode\"C\"bracketingMode\"C\"bracketingExpRatio\"I\"gainDigiSensor\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"luxLevel\"f\"useSpatialCCM\"B\"channel\"C\"flashStatus\"B\"isHLGMode\"B\"LTMGridConfigWidth\"f\"LTMGridConfigHeight\"f\"LTMGridConfigX\"f\"LTMGridConfigY\"f\"flashMixPercentage\"[512S]\"flashProjMixWeighting\"f\"tileStatsRegionInRaw\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"ccm\"{sAWBColorCorrectionMatrix_local=\"coeff\"[9(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})]}\"isLEDMainFlashforAWB\"B\"awbGains\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsSkinOnly\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsFlashProj\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"fdAWBChistMixFactor\"I\"awbColorspace\"C\"faceInfo\"{sFaceInfo=\"rectArray\"[10{sCIspFDRect=\"x\"i\"y\"i\"width\"I\"height\"I}]\"numFaces\"I}\"forceDisableFaceBoost\"B\"gammaCurve\"i\"useHighlightCompression\"B\"useAdaptiveHighlightCompression\"B\"highlightCompressionGain\"f\"isSIFRFrame\"B\"LTMHazeCorrectionOff\"B\"useBt709\"B\"useHazeCorrection\"B\"hazeCorrection\"\"tuningParametersOverride\"[6{LTMTuning=\"isValid\"B\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B\"faceBiasScaler\"f}"

```
