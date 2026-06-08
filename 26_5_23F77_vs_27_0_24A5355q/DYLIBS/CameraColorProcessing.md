## CameraColorProcessing

> `/System/Library/PrivateFrameworks/CameraColorProcessing.framework/CameraColorProcessing`

```diff

-665.120.8.0.0
-  __TEXT.__text: 0x60690
-  __TEXT.__auth_stubs: 0x710
-  __TEXT.__objc_methlist: 0x1dbc
-  __TEXT.__const: 0x6b9c
-  __TEXT.__gcc_except_tab: 0x3d60
-  __TEXT.__cstring: 0x4f38
+748.0.0.122.2
+  __TEXT.__text: 0x8b240
+  __TEXT.__objc_methlist: 0x1f5c
+  __TEXT.__const: 0x6a64
+  __TEXT.__gcc_except_tab: 0x519c
+  __TEXT.__cstring: 0x8fbc
   __TEXT.__dlopen_cstrs: 0xf0
-  __TEXT.__oslogstring: 0x2415
-  __TEXT.__unwind_info: 0xc58
-  __TEXT.__eh_frame: 0x90
-  __TEXT.__objc_classname: 0x454
-  __TEXT.__objc_methname: 0x4bad
-  __TEXT.__objc_methtype: 0xc8e4
-  __TEXT.__objc_stubs: 0x2c40
-  __DATA_CONST.__got: 0x430
+  __TEXT.__oslogstring: 0xbe83
+  __TEXT.__unwind_info: 0xc50
+  __TEXT.__eh_frame: 0x98
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1b8
-  __DATA_CONST.__objc_classlist: 0xd0
+  __DATA_CONST.__objc_classlist: 0xd8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xdf8
-  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_selrefs: 0xf28
+  __DATA_CONST.__objc_superrefs: 0xa8
   __DATA_CONST.__objc_arraydata: 0x360
-  __AUTH_CONST.__auth_got: 0x3a0
-  __AUTH_CONST.__const: 0x5d8
-  __AUTH_CONST.__cfstring: 0x2a80
-  __AUTH_CONST.__objc_const: 0x49d8
+  __DATA_CONST.__got: 0x490
+  __AUTH_CONST.__const: 0x598
+  __AUTH_CONST.__cfstring: 0x2fa0
+  __AUTH_CONST.__objc_const: 0x4cf0
+  __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_intobj: 0x528
+  __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_ivar: 0x450
-  __DATA.__data: 0xff8
-  __DATA.__bss: 0x40
-  __DATA.__common: 0x400
+  __AUTH_CONST.__auth_got: 0x538
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x488
+  __DATA.__data: 0xcb8
+  __DATA.__bss: 0x8
   __DATA_DIRTY.__objc_data: 0x820
-  __DATA_DIRTY.__data: 0x1d0
-  __DATA_DIRTY.__bss: 0x790
-  __DATA_DIRTY.__common: 0x268
+  __DATA_DIRTY.__data: 0x4a8
+  __DATA_DIRTY.__bss: 0x7d0
+  __DATA_DIRTY.__common: 0x1668
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1C3D7EE2-531D-3924-8CAB-738DBBF02D62
-  Functions: 1079
-  Symbols:   3699
-  CStrings:  2279
+  UUID: 1912BEB8-ABAF-3EA8-872C-2482427B19A6
+  Functions: 1338
+  Symbols:   4420
+  CStrings:  2251
 
Symbols:
+ +[AWBAlgorithm calculateSTRBKeyFromWideCameraLatticeModel:moduleConfig:absoluteColorCalibrations:secondaryModuleConfig:secondaryAbsoluteColorCalibrations:].cold.1
+ +[LTMExtractMetadataV1 extractRectanglesFrom:validBufferRect:ltmGeometry:]
+ +[LTMExtractMetadataV1 extractRectanglesFrom:validBufferRect:ltmGeometry:].cold.1
+ +[LTMExtractMetadataV2 extractRectanglesFrom:validBufferRect:ltmGeometry:]
+ +[LTMExtractMetadataV2 extractRectanglesFrom:validBufferRect:ltmGeometry:].cold.1
+ +[LTMMetadataWriterV1 _addLocalClippingDataToMetadata:statistics:geometryData:].cold.2
+ -[ANSTInferenceWrapper .cxx_destruct]
+ -[ANSTInferenceWrapper _allocateClientIOPixelBuffers:inputPixelBufferFormat:inputPixelBufferAttributes:outputPixelBufferSize:outputPixelBufferFormat:outputPixelBufferAttributes:allocateOutputPixelBufferForConversion:]
+ -[ANSTInferenceWrapper _allocateClientIOPixelBuffers:inputPixelBufferFormat:inputPixelBufferAttributes:outputPixelBufferSize:outputPixelBufferFormat:outputPixelBufferAttributes:allocateOutputPixelBufferForConversion:].cold.1
+ -[ANSTInferenceWrapper _allocateClientIOPixelBuffers:inputPixelBufferFormat:inputPixelBufferAttributes:outputPixelBufferSize:outputPixelBufferFormat:outputPixelBufferAttributes:allocateOutputPixelBufferForConversion:].cold.2
+ -[ANSTInferenceWrapper _allocateClientIOPixelBuffers:inputPixelBufferFormat:inputPixelBufferAttributes:outputPixelBufferSize:outputPixelBufferFormat:outputPixelBufferAttributes:allocateOutputPixelBufferForConversion:].cold.3
+ -[ANSTInferenceWrapper _bindANSTEspressoV1ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:]
+ -[ANSTInferenceWrapper _bindANSTEspressoV1ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.1
+ -[ANSTInferenceWrapper _bindANSTEspressoV1ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.2
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:]
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.1
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.10
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.2
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.3
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.4
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.5
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.6
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.7
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.8
+ -[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:].cold.9
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:]
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.1
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.10
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.11
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.2
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.3
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.4
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.5
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.6
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.7
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.8
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:].cold.9
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPorts:ignoringDescriptorsNamed:]
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPorts:ignoringDescriptorsNamed:].cold.1
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPorts:ignoringDescriptorsNamed:].cold.2
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPorts:ignoringDescriptorsNamed:].cold.3
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPorts:ignoringDescriptorsNamed:].cold.4
+ -[ANSTInferenceWrapper _bindANSTEspressoV5IOPorts:ignoringDescriptorsNamed:].cold.5
+ -[ANSTInferenceWrapper _loadANSTEspressoV1NetworkFromURL:anstAssetType:]
+ -[ANSTInferenceWrapper _loadANSTEspressoV1NetworkFromURL:anstAssetType:].cold.1
+ -[ANSTInferenceWrapper _loadANSTEspressoV1NetworkFromURL:anstAssetType:].cold.2
+ -[ANSTInferenceWrapper _loadANSTEspressoV1NetworkFromURL:anstAssetType:].cold.3
+ -[ANSTInferenceWrapper _loadANSTEspressoV1NetworkFromURL:anstAssetType:].cold.4
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:]
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:].cold.1
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:].cold.2
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:].cold.3
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:].cold.4
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:].cold.5
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:].cold.6
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:].cold.7
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:].cold.8
+ -[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:].cold.9
+ -[ANSTInferenceWrapper _purgeResources]
+ -[ANSTInferenceWrapper _purgeResources].cold.1
+ -[ANSTInferenceWrapper anstInputTex]
+ -[ANSTInferenceWrapper anstOutputTex]
+ -[ANSTInferenceWrapper dealloc]
+ -[ANSTInferenceWrapper initWithMetalContext:]
+ -[ANSTInferenceWrapper loadANSTNetwork]
+ -[ANSTInferenceWrapper networkLoaded]
+ -[ANSTInferenceWrapper processANST]
+ -[ANSTInferenceWrapper processANST].cold.1
+ -[ANSTInferenceWrapper processANST].cold.2
+ -[ANSTInferenceWrapper processANST].cold.3
+ -[ANSTInferenceWrapper processANST].cold.4
+ -[ANSTInferenceWrapper processANST].cold.5
+ -[ANSTInferenceWrapper processANST].cold.6
+ -[ANSTInferenceWrapper processANST].cold.7
+ -[ANSTInferenceWrapper processANST].cold.8
+ -[ANSTInferenceWrapper processANST].cold.9
+ -[ANSTInferenceWrapper purgeANSTNetwork]
+ -[AWBAlgorithm configFlashMetadata:cameraInfo:moduleConfig:]
+ -[AdaptiveGain globalHistSourceROI]
+ -[AdaptiveGain setGlobalHistSourceROI:]
+ -[HazeEstimation prepareThumbnail:]
+ -[HazeEstimation prepareThumbnail:].cold.1
+ -[HazeEstimation prepareThumbnail:].cold.2
+ -[HazeEstimation purgeResources]
+ -[HazeEstimation run].cold.4
+ -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:]
+ -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:].cold.1
+ -[LTMExtractMetadataV2 copyRectanglesInformationFrom:toDriverInput:ltmGeometry:]
+ -[LTMExtractMetadataV2 extractRectanglesInformationFrom:toDriverInput:ltmGeometry:]
+ -[LTMGeometryDataV1 LTMProcessotInputTexToLTMInTexScale]
+ -[LTMGeometryDataV1 isPortraitOrientated]
+ -[LTMGeometryDataV1 setIsPortraitOrientated:]
+ -[LTMGeometryDataV1 setLTMProcessotInputTexToLTMInTexScale:]
+ -[LTMGeometryDataV2 LTMProcessotInputTexToLTMInTexScale]
+ -[LTMGeometryDataV2 isPortraitOrientated]
+ -[LTMGeometryDataV2 setIsPortraitOrientated:]
+ -[LTMGeometryDataV2 setLTMProcessotInputTexToLTMInTexScale:]
+ -[LTMIBPParams isFinalImage]
+ -[LTMIBPParams rectangles]
+ -[LTMIBPParams setIsFinalImage:]
+ -[LTMIBPParams setRectangles:]
+ -[LTMIBPParams setValidTextureRect:]
+ -[LTMIBPParams validTextureRect]
+ -[LTMProcessor createRGBAFloatFromLTMInTexture:]
+ -[LTMProcessor createRGBAFloatFromLTMInTexture:].cold.1
+ -[LTMProcessor createRGBAFloatFromLTMInTexture:].cold.2
+ -[LTMProcessor createRGBAFloatFromLTMInTexture:].cold.3
+ -[LTMProcessor process].cold.17
+ -[LTMStats calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:].cold.1
+ -[LTMStats calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:].cold.2
+ -[LTMStats finishCalculateHITHStatistics:optimized:].cold.1
+ -[LTMStats finishCalculateHITHStatistics:optimized:].cold.2
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:].cold.1
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:].cold.2
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:].cold.3
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:].cold.4
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:].cold.5
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:].cold.6
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:].cold.7
+ -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:].cold.8
+ -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:]
+ -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:].cold.1
+ -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:].cold.2
+ -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:].cold.3
+ GCC_except_table21
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table33
+ GCC_except_table48
+ _CGAffineTransformConcat
+ _CGAffineTransformMakeScale
+ _CVPixelBufferGetIOSurface
+ _FigCapturePortTypeIsFrontColorCamera
+ _FigSignalErrorAt3
+ _IOSurfaceGetAllocSize
+ _IOSurfaceGetBaseAddress
+ _IOSurfaceLock
+ _IOSurfaceUnlock
+ _OBJC_CLASS_$_ANSTInferenceWrapper
+ _OBJC_CLASS_$_FigMetalBufferDescriptor
+ _OBJC_IVAR_$_ANSTInferenceWrapper._anstInferenceDescriptor
+ _OBJC_IVAR_$_ANSTInferenceWrapper._anstInputPixelBuffer
+ _OBJC_IVAR_$_ANSTInferenceWrapper._anstInputTex
+ _OBJC_IVAR_$_ANSTInferenceWrapper._anstOutputPixelBuffer
+ _OBJC_IVAR_$_ANSTInferenceWrapper._anstOutputPixelBuffer8
+ _OBJC_IVAR_$_ANSTInferenceWrapper._anstOutputTex
+ _OBJC_IVAR_$_ANSTInferenceWrapper._anstVersion
+ _OBJC_IVAR_$_ANSTInferenceWrapper._e5rtExecutionStream
+ _OBJC_IVAR_$_ANSTInferenceWrapper._e5rtExecutionStreamOperation
+ _OBJC_IVAR_$_ANSTInferenceWrapper._espressoContext
+ _OBJC_IVAR_$_ANSTInferenceWrapper._espressoNetwork
+ _OBJC_IVAR_$_ANSTInferenceWrapper._espressoPlan
+ _OBJC_IVAR_$_ANSTInferenceWrapper._inputImageDescriptor
+ _OBJC_IVAR_$_ANSTInferenceWrapper._metalContext
+ _OBJC_IVAR_$_ANSTInferenceWrapper._outputSkinMapDescriptor
+ _OBJC_IVAR_$_AWBStatistics._anstInferenceWrapper
+ _OBJC_IVAR_$_AdaptiveGain._globalHistSourceROI
+ _OBJC_IVAR_$_LTMExtractMetadataV2._allowPortraitOrientationLTCGridOverride
+ _OBJC_IVAR_$_LTMGeometryDataV1._LTMProcessotInputTexToLTMInTexScale
+ _OBJC_IVAR_$_LTMGeometryDataV1._isPortraitOrientated
+ _OBJC_IVAR_$_LTMGeometryDataV2._LTMProcessotInputTexToLTMInTexScale
+ _OBJC_IVAR_$_LTMGeometryDataV2._isPortraitOrientated
+ _OBJC_IVAR_$_LTMIBPParams._isFinalImage
+ _OBJC_IVAR_$_LTMIBPParams._rectangles
+ _OBJC_IVAR_$_LTMIBPParams._validTextureRect
+ _OBJC_IVAR_$_LTMProcessor._LTMProcessotInputTexToLTMInTexScale
+ _OBJC_IVAR_$_LTMProcessor._adaptiveGainVersion
+ _OBJC_IVAR_$_LTMProcessor._enableFaceExposure
+ _OBJC_IVAR_$_LTMProcessor._enableFaceGlobalWeight
+ _OBJC_IVAR_$_LTMProcessor._enableHardGainForLowLight
+ _OBJC_IVAR_$_LTMProcessor._enableHiResThumbnail
+ _OBJC_IVAR_$_LTMProcessor._enableMultiFaceFATE
+ _OBJC_IVAR_$_LTMProcessor._faceExposureTargetSkinTone
+ _OBJC_IVAR_$_LTMProcessor._faceGlobalWeightBGOverride
+ _OBJC_IVAR_$_LTMProcessor._faceGlobalWeightOverride
+ _OBJC_IVAR_$_LTMProcessor._ltmRGBToRGBAFloat
+ _OBJC_METACLASS_$_ANSTInferenceWrapper
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_19
+ _OUTLINED_FUNCTION_20
+ _OUTLINED_FUNCTION_21
+ _OUTLINED_FUNCTION_22
+ _OUTLINED_FUNCTION_23
+ _OUTLINED_FUNCTION_24
+ _OUTLINED_FUNCTION_25
+ _OUTLINED_FUNCTION_26
+ _OUTLINED_FUNCTION_27
+ _OUTLINED_FUNCTION_28
+ _OUTLINED_FUNCTION_29
+ _OUTLINED_FUNCTION_30
+ _OUTLINED_FUNCTION_31
+ _OUTLINED_FUNCTION_32
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
+ __OBJC_$_INSTANCE_METHODS_ANSTInferenceWrapper
+ __OBJC_$_INSTANCE_VARIABLES_ANSTInferenceWrapper
+ __OBJC_$_PROP_LIST_AWBIBPParams.196
+ __OBJC_$_PROP_LIST_LTMIBPParams.220
+ __OBJC_CLASS_RO_$_ANSTInferenceWrapper
+ __OBJC_METACLASS_RO_$_ANSTInferenceWrapper
+ __ZL32_configTilesRuntimeWithValidRectP18AWBTileStatsConfigRK6CGRect.cold.1
+ __ZN10CAWBAFEH14C1EPKcP7CObject31CameraColorProcessingPlatformID
+ __ZN10CAWBAFEH14C2EPKcP7CObject31CameraColorProcessingPlatformID
+ __ZN11LTMDriverV29LTMDriver19computeFaceWeightV2EPK7sBTRectPK11sCIspFDRectiPfPKiff
+ __ZN11LTMDriverV29LTMDriver19fmapHFFFilterCoeffsE
+ __ZN11LTMDriverV29LTMDriver28HFFThumbnailDownscaleConvertEPK24sCLRProcHITHStat_SOFTISPP16sLtmComputeInputffibii
+ __ZN11LTMDriverV29LTMDriver29computeFaceWeightForToneHFFV2EPK7sBTRectPK11sCIspFDRectiPfPKi
+ __ZN11LTMDriverV29LTMDriver9filter3x3EPKfPfiiS2_S2_
+ __ZN12LTMComputeV110LTMCompute20ccmWithNewWhitePointEPfPKfff
+ __ZN12LTMComputeV210LTMCompute12allocateToneEPfS1_PKfPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPKNS_15sLtmFrameParamsES3_S3_S3_S3_S3_fffbbb
+ __ZN12LTMComputeV210LTMCompute16defaultHistHiResE
+ __ZN12LTMComputeV210LTMCompute19calculateSceneModelEPK16sLtmComputeInputPKNS_16sLtmTuningParamsEPNS_15sLtmFrameParamsEfPfS9_fPKf
+ __ZN12LTMComputeV210LTMCompute20ccmWithNewWhitePointEPfPKfff
+ __ZN12LTMComputeV210LTMCompute30calculateHighlightSceneModelV2EPK16sLtmComputeInputPKNS_16sLtmTuningParamsEbPKNS_15sLtmFrameParamsEPfSA_SA_
+ __ZN12LTMComputeV210LTMCompute9faceHistsE
+ __ZN15CAWBAFEFDAssist32ModifyColorHistogramProbApproachEP13fdAWBMetaDataPA4_tPjt.cold.1
+ __ZN30CAWBAFEPhotometerAssistPenroseC1Eb31CameraColorProcessingPlatformID
+ __ZN30CAWBAFEPhotometerAssistPenroseC2Eb31CameraColorProcessingPlatformID
+ __ZN7CAWBAFE12InitialResetEb.cold.1
+ __ZN7CAWBAFE25CalculateSkinWeightForSTFEbPfS0_S0_.cold.1
+ __ZN7CAWBAFEC2EPKcP7CObject31CameraColorProcessingPlatformID
+ __ZSt9terminatev
+ __ZZ74+[LTMExtractMetadataV1 extractRectanglesFrom:validBufferRect:ltmGeometry:]E9onceToken
+ __ZZ74+[LTMExtractMetadataV2 extractRectanglesFrom:validBufferRect:ltmGeometry:]E9onceToken
+ ___74+[LTMExtractMetadataV1 extractRectanglesFrom:validBufferRect:ltmGeometry:]_block_invoke
+ ___74+[LTMExtractMetadataV2 extractRectanglesFrom:validBufferRect:ltmGeometry:]_block_invoke
+ ___83-[LTMExtractMetadataV2 extractRectanglesInformationFrom:toDriverInput:ltmGeometry:]_block_invoke
+ ___block_literal_global.11
+ ___block_literal_global.116
+ ___block_literal_global.162
+ ___block_literal_global.43
+ ___clang_call_terminate
+ ___cxa_begin_catch
+ _e5rt_buffer_object_get_iosurface
+ _e5rt_buffer_object_release
+ _e5rt_e5_compiler_compile
+ _e5rt_e5_compiler_create
+ _e5rt_e5_compiler_options_create
+ _e5rt_e5_compiler_options_release
+ _e5rt_e5_compiler_release
+ _e5rt_execution_stream_create
+ _e5rt_execution_stream_encode_operation
+ _e5rt_execution_stream_execute_sync
+ _e5rt_execution_stream_operation_create_precompiled_compute_operation
+ _e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options
+ _e5rt_execution_stream_operation_get_input_names
+ _e5rt_execution_stream_operation_get_num_inputs
+ _e5rt_execution_stream_operation_get_num_outputs
+ _e5rt_execution_stream_operation_get_output_names
+ _e5rt_execution_stream_operation_release
+ _e5rt_execution_stream_operation_retain_input_port
+ _e5rt_execution_stream_operation_retain_output_port
+ _e5rt_execution_stream_release
+ _e5rt_get_last_error_message
+ _e5rt_io_port_bind_buffer_object
+ _e5rt_io_port_bind_surface_object
+ _e5rt_io_port_is_tensor
+ _e5rt_io_port_release
+ _e5rt_io_port_retain_surface_desc
+ _e5rt_io_port_retain_tensor_desc
+ _e5rt_precompiled_compute_op_create_options_create_with_program_function
+ _e5rt_precompiled_compute_op_create_options_release
+ _e5rt_program_function_release
+ _e5rt_program_library_release
+ _e5rt_program_library_retain_program_function
+ _e5rt_surface_desc_release
+ _e5rt_surface_object_alloc
+ _e5rt_surface_object_create_from_iosurface
+ _e5rt_surface_object_get_iosurface
+ _e5rt_surface_object_release
+ _e5rt_tensor_desc_alloc_buffer_object
+ _e5rt_tensor_desc_release
+ _kFigCapturePortType_RCamera
+ _kFigCaptureStreamMetadata_AEFaceAverage
+ _kFigCaptureStreamMetadata_AWBSkinCCMMixingFactor
+ _kFigCaptureStreamMetadata_DisplayStrobeCCTEstimate
+ _kFigCaptureStreamMetadata_FlashAmbientLuxLevel
+ _kFigCaptureStreamMetadata_FlashAmbientLuxLevelHigh
+ _kFigCaptureStreamMetadata_FlashAmbientLuxLevelLow
+ _kFigCaptureStreamMetadata_SkinColorCorrectionMitigationMatrix
+ _kFigCaptureStreamMetadata_SkinToneLevels
+ _objc_claimAutoreleasedReturnValue
+ _objc_enumerationMutation
+ _objc_msgSend$LTMProcessotInputTexToLTMInTexScale
+ _objc_msgSend$_allocateClientIOPixelBuffers:inputPixelBufferFormat:inputPixelBufferAttributes:outputPixelBufferSize:outputPixelBufferFormat:outputPixelBufferAttributes:allocateOutputPixelBufferForConversion:
+ _objc_msgSend$_bindANSTEspressoV1ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:
+ _objc_msgSend$_bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:
+ _objc_msgSend$_bindANSTEspressoV5IOPort:portName:
+ _objc_msgSend$_bindANSTEspressoV5IOPorts:ignoringDescriptorsNamed:
+ _objc_msgSend$_loadANSTEspressoV1NetworkFromURL:anstAssetType:
+ _objc_msgSend$_loadANSTEspressoV5NetworkFromURL:anstAssetType:
+ _objc_msgSend$_purgeResources
+ _objc_msgSend$anstInputTex
+ _objc_msgSend$anstOutputTex
+ _objc_msgSend$arrayWithObjects:count:
+ _objc_msgSend$assetType
+ _objc_msgSend$compareAWBMetadata:withReference:
+ _objc_msgSend$computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:
+ _objc_msgSend$configFlashMetadata:cameraInfo:moduleConfig:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copyRectanglesInformationFrom:toDriverInput:ltmGeometry:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$e5DescriptorWithConfiguration:error:
+ _objc_msgSend$e5FunctionName
+ _objc_msgSend$extractAWBMetadataFromRawMetadata:toDriverInput:
+ _objc_msgSend$extractRectanglesFrom:validBufferRect:ltmGeometry:
+ _objc_msgSend$extractRectanglesInformationFrom:toDriverInput:ltmGeometry:
+ _objc_msgSend$faceRectangles
+ _objc_msgSend$inputImageDescriptor
+ _objc_msgSend$inputTexToLTMInTexScale
+ _objc_msgSend$isPortraitOrientated
+ _objc_msgSend$loadANSTNetwork
+ _objc_msgSend$ltmROIRect
+ _objc_msgSend$name
+ _objc_msgSend$networkLoaded
+ _objc_msgSend$outputSkinMapDescriptor
+ _objc_msgSend$pixelBufferAttributes
+ _objc_msgSend$pixelFormatType
+ _objc_msgSend$prepareThumbnail:
+ _objc_msgSend$processANST
+ _objc_msgSend$purgeANSTNetwork
+ _objc_msgSend$rectangles
+ _objc_msgSend$sensorSpaceToTextureSpaceTransform
+ _objc_msgSend$setGlobalHistSourceROI:
+ _objc_msgSend$setIsPortraitOrientated:
+ _objc_msgSend$setLTMProcessotInputTexToLTMInTexScale:
+ _objc_msgSend$supportedVersionsForCurrentHardware
+ _objc_msgSend$usedSize
+ _objc_msgSend$validTextureRect
+ _objc_release_x9
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _skinCCM2DCoefficientDefault
+ _zeroInitializeIOSurface
+ _zeroInitializeIOSurface.cold.1
+ _zeroInitializeIOSurface.cold.2
+ _zeroInitializeIOSurface.cold.3
- +[LTMExtractMetadataV1 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]
- +[LTMExtractMetadataV1 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:].cold.1
- +[LTMExtractMetadataV2 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]
- +[LTMExtractMetadataV2 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:].cold.1
- +[LTMMetadataWriterV1 _addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:].cold.3
- +[LTMMetadataWriterV2 _addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:].cold.3
- -[AWBAlgorithm calculateEIT:result:]
- -[AWBAlgorithm configFlashRFCMetadata:cameraInfo:moduleConfig:]
- -[AWBAlgorithm process].cold.1
- -[AWBAlgorithm process].cold.2
- -[AWBProcessor prepareToProcess:].cold.1
- -[AWBProcessor prepareToProcess:].cold.2
- -[AWBProcessor prepareToProcess:].cold.3
- -[AWBProcessor prepareToProcess:].cold.4
- -[AWBProcessor prepareToProcess:].cold.5
- -[AWBProcessor prepareToProcess:].cold.6
- -[AWBProcessor prepareToProcess:].cold.7
- -[AWBProcessor prepareToProcess:].cold.8
- -[AWBProcessor process].cold.1
- -[AWBProcessor process].cold.2
- -[AWBProcessor process].cold.3
- -[AWBProcessor process].cold.4
- -[AWBProcessor process].cold.5
- -[AWBProcessor process].cold.6
- -[AWBProcessor process].cold.7
- -[HazeEstimation allocInternalData]
- -[HazeEstimation allocInternalData].cold.1
- -[HazeEstimation allocInternalData].cold.2
- -[HazeEstimation allocInternalData].cold.3
- -[HazeEstimation allocInternalData].cold.4
- -[HazeEstimation prepareThumbnail]
- -[HazeEstimation prepareThumbnail].cold.1
- -[HazeEstimation prepareThumbnail].cold.2
- -[HazeEstimation releaseTextures]
- -[LTMCurvesComputeV1 compute].cold.2
- -[LTMCurvesComputeV1 compute].cold.3
- -[LTMCurvesComputeV1 compute].cold.4
- -[LTMCurvesComputeV1 compute].cold.5
- -[LTMCurvesComputeV1 compute].cold.6
- -[LTMCurvesComputeV1 compute].cold.7
- -[LTMCurvesComputeV1 compute].cold.8
- -[LTMCurvesComputeV1 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:].cold.2
- -[LTMCurvesComputeV1 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:].cold.3
- -[LTMCurvesComputeV2 compute].cold.2
- -[LTMCurvesComputeV2 compute].cold.3
- -[LTMCurvesComputeV2 compute].cold.4
- -[LTMCurvesComputeV2 compute].cold.5
- -[LTMCurvesComputeV2 compute].cold.6
- -[LTMCurvesComputeV2 compute].cold.7
- -[LTMCurvesComputeV2 compute].cold.8
- -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:]
- -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:].cold.1
- -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:].cold.2
- -[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:].cold.3
- -[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:].cold.1
- -[LTMIBPParams inputBufferRect]
- -[LTMIBPParams setInputBufferRect:]
- -[LTMIBPParams setValidBufferRect:]
- -[LTMIBPParams validBufferRect]
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.1
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.10
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.2
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.3
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.4
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.5
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.6
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.7
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.8
- -[LTMProcessor setDehazeTuningParamsFrom:].cold.9
- -[LTMProcessor setLTMComputeTuningParams:from:].cold.1
- -[LTMProcessor setLTMComputeTuningParams:from:].cold.2
- -[LTMProcessor setLTMComputeTuningParams:from:].cold.3
- -[LTMProcessor setLTMComputeTuningParams:from:].cold.4
- -[LTMStats calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:]
- -[LTMStats calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:].cold.1
- -[LTMStats calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:].cold.2
- -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:]
- -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.1
- -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.2
- -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.3
- -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.4
- -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.5
- -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.6
- -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.7
- -[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:].cold.8
- -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:]
- -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:].cold.1
- -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:].cold.2
- -[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:].cold.3
- GCC_except_table49
- _FigSignalErrorAtGM
- _OBJC_IVAR_$_AWBAlgorithm._preFlashLuxLevel
- _OBJC_IVAR_$_AWBAlgorithm._preFlashLuxLevelHigh
- _OBJC_IVAR_$_AWBAlgorithm._preFlashLuxLevelLow
- _OBJC_IVAR_$_AWBStatistics._espressoContext
- _OBJC_IVAR_$_AWBStatistics._espressoNetwork
- _OBJC_IVAR_$_AWBStatistics._espressoPlan
- _OBJC_IVAR_$_HazeEstimation._device
- _OBJC_IVAR_$_HazeEstimation._hazeConfig
- _OBJC_IVAR_$_HazeEstimation._hazeInternalBuffer
- _OBJC_IVAR_$_HazeEstimation._thumbnailTexture
- _OBJC_IVAR_$_LTMCurvesComputeV1._globalHistStat
- _OBJC_IVAR_$_LTMCurvesComputeV1._localHistStat
- _OBJC_IVAR_$_LTMCurvesComputeV1._thumbnailStat
- _OBJC_IVAR_$_LTMCurvesComputeV2._enableCB
- _OBJC_IVAR_$_LTMCurvesComputeV2._enableFATE
- _OBJC_IVAR_$_LTMCurvesComputeV2._enableHiResLocalHistogram
- _OBJC_IVAR_$_LTMCurvesComputeV2._globalFaceHistStat
- _OBJC_IVAR_$_LTMCurvesComputeV2._globalHistStat
- _OBJC_IVAR_$_LTMCurvesComputeV2._localHistStat
- _OBJC_IVAR_$_LTMCurvesComputeV2._thumbnailStat
- _OBJC_IVAR_$_LTMIBPParams._inputBufferRect
- _OBJC_IVAR_$_LTMIBPParams._validBufferRect
- __OBJC_$_PROP_LIST_AWBIBPParams.197
- __OBJC_$_PROP_LIST_LTMIBPParams.212
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.1
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.2
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.3
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.4
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.5
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.6
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.7
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.8
- __ZL33convertANSTMaskFrom32FloatTo8UintP10__CVBufferS0_.cold.9
- __ZN10CAWBAFEH14C1EPKcP7CObjecti
- __ZN10CAWBAFEH14C2EPKcP7CObjecti
- __ZN11LTMDriverV29LTMDriver28HFFThumbnailDownscaleConvertEPK24sCLRProcHITHStat_SOFTISPP16sLtmComputeInputffib
- __ZN12LTMComputeV210LTMCompute11globalHist2E
- __ZN12LTMComputeV210LTMCompute12allocateToneEPfS1_PKfPKNS_16sLtmTuningParamsEPKNS_17sLtmDisplayParamsEPKNS_15sLtmFrameParamsES3_S3_S3_S3_S3_fffbb
- __ZN12LTMComputeV210LTMCompute23calculateSceneModelAlgoEPfS1_PK16sLtmComputeInputPKNS_16sLtmTuningParamsEPNS_15sLtmFrameParamsEffPKf
- __ZN30CAWBAFEPhotometerAssistPenroseC1Ebi
- __ZN30CAWBAFEPhotometerAssistPenroseC2Ebi
- __ZN7CAWBAFEC2EPKcP7CObjecti
- __ZZ62-[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:]E9onceToken
- __ZZ90+[LTMExtractMetadataV1 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]E9onceToken
- __ZZ90+[LTMExtractMetadataV2 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]E9onceToken
- ___127-[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:]_block_invoke
- ___62-[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:]_block_invoke
- ___62-[LTMExtractMetadataV2 extractFrom:toDriverInput:ltmGeometry:]_block_invoke.30
- ___90+[LTMExtractMetadataV1 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]_block_invoke
- ___90+[LTMExtractMetadataV2 extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:]_block_invoke
- ___block_literal_global.102
- ___block_literal_global.149
- ___block_literal_global.33
- ___block_literal_global.46
- ___block_literal_global.7
- _computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:.onceToken
- _objc_msgSend$calculateEIT:result:
- _objc_msgSend$calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:
- _objc_msgSend$computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:
- _objc_msgSend$configFlashRFCMetadata:cameraInfo:moduleConfig:
- _objc_msgSend$extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:
- _objc_msgSend$initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:
- _objc_msgSend$inputBufferRect
- _objc_msgSend$prepareThumbnail
- _objc_msgSend$startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:
- _objc_msgSend$validBufferRect
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "\t\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb6"
+ "%s%s%s signalled err=%d (%s) (%s) at %s:%d"
+ "'AGC' not found"
+ "'CurrentFrameRate' not found"
+ "'ExposureTime' not found"
+ "'GlobalShutterFlag' not found"
+ "'LuxLevel' not found"
+ "'anstSkinMask' pixel format must be a float or normalised unsigned type"
+ "'anstSkinMask' width/height must be >= ( 256 )/( 192 )"
+ "'awbStatsBuffer' failed allocation"
+ "'fullWindowStatsData' failed allocation"
+ "'ispDGain' not found"
+ "'metalContext' nil !"
+ "'sensorDGain' not found"
+ "'windowStatsData' failed allocation"
+ "( ! error ) && _anstInferenceDescriptor"
+ "( ! error ) && anstModelConfig"
+ "( ( ! driverMetaDataInput->enableDualLTC ) && ( ! isPortraitOrientated ) ) || driverMetaDataInput->enableDualLTC"
+ "( -73465 )"
+ "( cvErr == kCVReturnSuccess ) && _anstInputPixelBuffer"
+ "( cvErr == kCVReturnSuccess ) && _anstOutputPixelBuffer"
+ "( cvErr == kCVReturnSuccess ) && _anstOutputPixelBuffer8"
+ "( e5rtError == E5RT_ERROR_CODE_OK ) && _e5rtExecutionStream"
+ "( e5rtError == E5RT_ERROR_CODE_OK ) && _e5rtExecutionStreamOperation"
+ "+[AWBAlgorithm awbSensorCalibrationsLoad:idealColorCalibrations:to:]"
+ "+[AWBAlgorithm calculateSTRBKeyFromWideCamera:moduleConfig:secondaryModuleConfig:]"
+ "+[AWBAlgorithm calculateSTRBKeyFromWideCameraLatticeModel:moduleConfig:absoluteColorCalibrations:secondaryModuleConfig:secondaryAbsoluteColorCalibrations:]"
+ "+[AWBAlgorithm doAWBConfigLoad:to:]"
+ "+[AWBAlgorithm encodeSetFileIDForModuleConfig:setFileID:]"
+ "+[AWBAlgorithm getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:platformID:]"
+ "+[AWBAlgorithm populateSlaveConfigWithModuleConfigIfColorMatchingModelExistsInPrimaryAWBConfig:secondaryAWBConfig:secondaryIdealColorCals:secondaryAbsoluteColorCals:secondarySetFileID:secondarySensorConfig:]"
+ "+[AWBAlgorithm translateAWBGainsToSecondaryPortType:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:primaryRGain:primaryBGain:secondaryChannelID:secondaryRGain:secondaryBGain:]"
+ "+[AWBStatistics getTileStatsRegionWithMetadata:cropRectLTMInCoords:ltmInDownsamplingRatio:tileStatsRegionLTMInCoordsDictOut:]"
+ "+[FWPlatformIDUtilities getFWPlatformID]"
+ "+[GeometryUtilities getTransformCropRectFromSensorCoordsToValidBufferCoordsWithMetadata:validBufferRect:]"
+ "+[LTMExtractMetadataV1 extractCCMFromMetadata:toDriverInput:]"
+ "+[LTMExtractMetadataV1 extractRectanglesFrom:validBufferRect:ltmGeometry:]"
+ "+[LTMExtractMetadataV1 getTileStatsRegion:validBufferRect:toDriverInput:]"
+ "+[LTMExtractMetadataV2 extractCCMFromMetadata:toDriverInput:]"
+ "+[LTMExtractMetadataV2 extractRectanglesFrom:validBufferRect:ltmGeometry:]"
+ "+[LTMExtractMetadataV2 getTileStatsRegion:validBufferRect:ltmGeometryData:toDriverInput:]"
+ "+[LTMMetadataWriterV1 _addLocalHistToMetadata:statistics:geometryData:]"
+ "-1"
+ "-1 == 0 "
+ "-[ANSTInferenceWrapper _allocateClientIOPixelBuffers:inputPixelBufferFormat:inputPixelBufferAttributes:outputPixelBufferSize:outputPixelBufferFormat:outputPixelBufferAttributes:allocateOutputPixelBufferForConversion:]"
+ "-[ANSTInferenceWrapper _bindANSTEspressoV1ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:]"
+ "-[ANSTInferenceWrapper _bindANSTEspressoV5ClientIO:toInputImageDescriptorName:outputPixelBuffer:toOutputImageDescriptorName:]"
+ "-[ANSTInferenceWrapper _bindANSTEspressoV5IOPort:portName:]"
+ "-[ANSTInferenceWrapper _bindANSTEspressoV5IOPorts:ignoringDescriptorsNamed:]"
+ "-[ANSTInferenceWrapper _loadANSTEspressoV1NetworkFromURL:anstAssetType:]"
+ "-[ANSTInferenceWrapper _loadANSTEspressoV5NetworkFromURL:anstAssetType:]"
+ "-[ANSTInferenceWrapper _purgeResources]"
+ "-[ANSTInferenceWrapper initWithMetalContext:]"
+ "-[ANSTInferenceWrapper loadANSTNetwork]"
+ "-[ANSTInferenceWrapper processANST]"
+ "-[AWBAlgorithm _processSkyMask:skyMaskWidth:skyMaskHeight:cropRectFromSourceDict:]"
+ "-[AWBAlgorithm _updateHRGainDownRatioMetadata]"
+ "-[AWBAlgorithm awbConfigLoad:to:]"
+ "-[AWBAlgorithm calculateInternalAWBMetadataForMIWB:bGain:rSkinGain:bSkinGain:cct:internalMetadata:]"
+ "-[AWBAlgorithm configFlashMetadata:cameraInfo:moduleConfig:]"
+ "-[AWBAlgorithm configFlickerDetectionMetadata:moduleConfig:]"
+ "-[AWBAlgorithm initTuningParameters:]"
+ "-[AWBAlgorithm initWithAWBObject:]"
+ "-[AWBAlgorithm translateAWBGainsToSecondaryChannelID:secondaryChannelID:secondaryConfig:secondaryAWBParams:]"
+ "-[AWBProcessor internalSetupWithFWPlatformID:]"
+ "-[AWBStatistics _createShaders]"
+ "-[AWBStatistics configWindowsV2:metadata:tilesConfig:validRect:regionOfInterestRect:]"
+ "-[AdaptiveGain createShaders]"
+ "-[HazeEstimation createShaders]"
+ "-[HazeEstimation prepareThumbnail:]"
+ "-[HazeEstimation run]"
+ "-[LTMCurvesComputeV1 compute]"
+ "-[LTMCurvesComputeV2 compute]"
+ "-[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:]"
+ "-[LTMExtractMetadataV2 copyRectanglesInformationFrom:toDriverInput:ltmGeometry:]"
+ "-[LTMExtractMetadataV2 extractRectanglesInformationFrom:toDriverInput:ltmGeometry:]"
+ "-[LTMExtractMetadataV2 init]_block_invoke"
+ "-[LTMProcessor _prepareHighlightCompressionCurve]"
+ "-[LTMProcessor _printDefaultsLTMparam]"
+ "-[LTMProcessor _readDefaultsMetalAllocator]"
+ "-[LTMProcessor createRGBAFloatFromLTMInTexture:]"
+ "-[LTMProcessor setLTMComputeTuningParams:from:]"
+ "-[LTMProcessor setLTMTuningParamsFrom:]"
+ "-[LTMStats finishCalculateHITHStatistics:optimized:]"
+ "-[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:]"
+ "-[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:with:to:]"
+ "-[LTMStatsCompute createShaders:]"
+ "-[LTMStatsCompute initWithMetalContext:]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CameraCapture_CameraColorProcessing/CameraColorProcessing/Sources/AWBAlgorithm/FWPlatformIDUtilities.m %s: Unsupported device: %@ (this may be overridden with defaults write com.apple.coremedia softisp.awb.modelname <model>)"
+ "<<<< ANSTInferenceWrapper >>>>"
+ "<<<< ANSTInferenceWrapper >>>> %s: IOSurfaceRef invalid or NULL"
+ "<<<< ANSTInferenceWrapper >>>> %s: Loading ANST resources"
+ "<<<< ANSTInferenceWrapper >>>> %s: Loading ANST resources: %s"
+ "<<<< ANSTInferenceWrapper >>>> %s: Locking anstBuf32Float failed"
+ "<<<< ANSTInferenceWrapper >>>> %s: Locking anstBuf8 failed"
+ "<<<< ANSTInferenceWrapper >>>> %s: Purging ANST resources"
+ "<<<< ANSTInferenceWrapper >>>> %s: Source and destination pixel buffer sizes do not match"
+ "<<<< ANSTInferenceWrapper >>>> %s: _bindANSTEspressoV5IOPort failed"
+ "<<<< ANSTInferenceWrapper >>>> %s: anstBuf32Float is NULL"
+ "<<<< ANSTInferenceWrapper >>>> %s: anstBuf8 is NULL"
+ "<<<< ANSTInferenceWrapper >>>> %s: dstBufAddr is NULL"
+ "<<<< ANSTInferenceWrapper >>>> %s: err=%d"
+ "<<<< ANSTInferenceWrapper >>>> %s: srcBufAddr is NULL"
+ "<<<< ANSTInferenceWrapper >>>> Fig"
+ "<<<< AWBAlgorithm >>>> %s:  SkyMask is NOT available "
+ "<<<< AWBAlgorithm >>>> %s:  SkyMask is read, Dims: [%d, %d] \n"
+ "<<<< AWBAlgorithm >>>> %s:  _processSkyMask: Sky Mask is not available, not making any decision about sky \n"
+ "<<<< AWBAlgorithm >>>> %s:  _processSkyMask: skyPix=%d, totPix=%d, isSkyDet=%d, percSKyPx=%f \n"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Digital Flash Output: AWB Combo (Normalised) Gains = [%d,%d,%d]"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Digital Flash Output: AWB Combo Gains = [%d,%d,%d]"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Digital Flash Output: AWB Gains = [%d,%d,%d]"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Digital Flash Output: Fix enablement status [Skin-guided mixing factor | Additional face metadata] = %s"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Fallback Metadata Output: AWB Combo (Normalised) Gains = [%d,%d,%d]"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Fallback Metadata Output: AWB Combo Gains = [%d,%d,%d]"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Fallback Metadata Output: AWB Gains = [%d,%d,%d]"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Fallback Metadata Output: Fix enablement status [Skin-guided mixing factor | Additional face metadata] = %s"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Output: AWB Combo (Normalised) Gains = [%d,%d,%d]"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Output: AWB Combo Gains = [%d,%d,%d]"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Output: AWB Gains = [%d,%d,%d]"
+ "<<<< AWBAlgorithm >>>> %s: AWBAlgorithm Output: Fix enablement status [Skin-guided mixing factor | Additional face metadata] = %s"
+ "<<<< AWBAlgorithm >>>> %s: AWBFaceAssistedBehaviorMode_MatchProvidedSkinGains configured with:{%@}"
+ "<<<< AWBAlgorithm >>>> %s: Configuring metadata for FFC Flash"
+ "<<<< AWBAlgorithm >>>> %s: Configuring metadata for RFC Flash"
+ "<<<< AWBAlgorithm >>>> %s: Display strobe CCT not available, falling back to default value"
+ "<<<< AWBAlgorithm >>>> %s: Face rect missing"
+ "<<<< AWBAlgorithm >>>> %s: Failed to wrap around CAWBAFE object"
+ "<<<< AWBAlgorithm >>>> %s: Flash Calibration data isn't available, disabling the flash projection"
+ "<<<< AWBAlgorithm >>>> %s: ISP CCT %d --- SOFTISP CCT %d"
+ "<<<< AWBAlgorithm >>>> %s: ISP LuxLevel %d --- SOFTISP LuxLevel %d"
+ "<<<< AWBAlgorithm >>>> %s: ISP WBGs (%d, %d, %d)  --- SOFTISP WBGs (%d, %d, %d)"
+ "<<<< AWBAlgorithm >>>> %s: ISP combo WBGs (%d, %d, %d)  --- SOFTISP combo WBGs (%d, %d, %d)"
+ "<<<< AWBAlgorithm >>>> %s: ISP skin WBGs (%d, %d, %d)  --- SOFTISP skin WBGs (%d, %d, %d)"
+ "<<<< AWBAlgorithm >>>> %s: No ColorMatchingLatticeModel entries found in ModuleConfig"
+ "<<<< AWBAlgorithm >>>> %s: No ColorMatchingModel entries found in ModuleConfig, this is only expected for FFC"
+ "<<<< AWBAlgorithm >>>> %s: Trying to interpolate strobe key for wrong module. This is only supported for a single LED strobe module."
+ "<<<< AWBAlgorithm >>>> %s: Unable to support semantic AWB, falling back to FD-AWB"
+ "<<<< AWBAlgorithm >>>> %s: Unable to translate combo skin gains from Wide to SuperWide"
+ "<<<< AWBAlgorithm >>>> %s: Value for [%@][%@] not found in %@, using default value"
+ "<<<< AWBAlgorithm >>>> %s: gainDigiAE: ispDGain=%d (%.3fx) desiredIBLC=%.3f appliedIBLC=%.3f (max=%.3f) gainDigiAE=%u (%.3fx)"
+ "<<<< AWBAlgorithm >>>> %s: getInternalAWBMetadataForMIWB: Translating combo skin gains from Wide to SuperWide"
+ "<<<< AWBAlgorithm >>>> %s: getInternalAWBMetadataForMIWB: Unable to find bGain metadata value"
+ "<<<< AWBAlgorithm >>>> %s: getInternalAWBMetadataForMIWB: Unable to find bSkinGain metadata value"
+ "<<<< AWBAlgorithm >>>> %s: getInternalAWBMetadataForMIWB: Unable to find bSkinGainWide metadata value"
+ "<<<< AWBAlgorithm >>>> %s: getInternalAWBMetadataForMIWB: Unable to find cct metadata value"
+ "<<<< AWBAlgorithm >>>> %s: getInternalAWBMetadataForMIWB: Unable to find rGain metadata value"
+ "<<<< AWBAlgorithm >>>> %s: getInternalAWBMetadataForMIWB: Unable to find rSkinGain metadata value"
+ "<<<< AWBAlgorithm >>>> %s: getInternalAWBMetadataForMIWB: Unable to find rSkinGainWide metadata value"
+ "<<<< AWBAlgorithm >>>> %s: kCCPMetadata_daylightScore   %f"
+ "<<<< AWBAlgorithm >>>> %s: kCCPMetadata_skinMIWBWeight   %f"
+ "<<<< AWBAlgorithm >>>> %s: kCCPMetadata_skinNonComboBGain   %d"
+ "<<<< AWBAlgorithm >>>> %s: kCCPMetadata_skinNonComboRGain   %d"
+ "<<<< AWBAlgorithm >>>> %s: kCCPMetadata_skyMIWBBGain   %d"
+ "<<<< AWBAlgorithm >>>> %s: kCCPMetadata_skyMIWBRGain   %d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: %d "
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB RESET: CAWBAFE::CAWBAFE name(%s) isAWBSchemeSet=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB RESET: CAWBAFE::InitialReset"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB RESET: CAWBAFE::MinimalReset isAWBSchemeSet=%d awbScheme=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB RESET: CAWBAFE::~CAWBAFE"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB-Flash: isFlashOn=0x%x flashStatus= 0x%2x lux=%6d luxLow=%6d luxHigh=%6d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB-GW: CCMCoeff[2][0]= %d %d %d sum=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB-GW: GW-R=%.2f GW-G=%.2f GW-B=%.2f rn=%.2f bn=%.2f cct=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB-GW: bgCalGain=%.2f bgGain=%.2f totalBgGain=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB-GW: rgCalGain=%.2f rgGain=%.2f totalRgGain=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: AWB-GW: sumR=%.2f sumG=%.2f sumB=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: CC COEFs  %d %d %d "
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: Chg AWB sampling rate from %u (%.3f) to %u (%.3f Hz=every %.1fs)\n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: ChromaHist Sky=%.2f Tot=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: ChromaHist Top=%.2f Left=%.2f Tot=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: DFAWB: Projected down %.2f -> %.2f "
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: DFAWB: Projected right  %.2f -> %.2f "
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: DFAWB: dist=%.2f w_left=%.2f mixFactor=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: DFAWB: dist=%.2f w_top=%.2f mixFactor=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: MIWB: Unagi: Magenta Mitigation enabled: %d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: PreGain %d %d %d %d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: SemanticAWB:  ch=%d fn=%d mS=%d mP=%d bSMAWB=%d FdV=%d cmdFdV=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: SemanticAWB: ch=%u fn=%d semCh=%zu semFn=%d fdAWBVer=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: Set confidenceMap %p ch SemanticCh %zu frameCnt %u"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: Sky global WP rgLogRatio=%.2f bgLogRatio=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: Smoothing changed %d->%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: Smoothing changed %d->%d\n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: ]\n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.biasLEDRatioPoints : %+.5f %+.5f \n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.ccmModel     :   %+.5f %+.5f %+.5f %+.5f %+.5f \n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.distancePowerLuxWeight : %+.5f %+.5f \n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.distanceWeight         : %+.5f %+.5f \n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.ellipseModel :   %+.5f %+.5f %+.5f %+.5f %+.5f %.5f \n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.luxRatioWeight         : %+.5f %+.5f \n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.matrixRGBToXYZ:   %+.5f %+.5f %+.5f\n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.matrixXYZToRGB:   %+.5f %+.5f %+.5f\n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.useFlashCCMMixing          : %d\n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFlashProjectionConfig.useQuantileLuxLevels       : %d\n"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: awbFn=%d skin=%6.2f %6.2f white=%6.2f %6.2f num=%d "
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: bn_day=%6.2f %6d bn_low=%6.2f %6d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: cur=%d irR=%6.4f freqConf=%d dcR=%d lux=%.2f valid=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: dayLight_bgLogRatio = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: enableCCMDesatForSkinColors=%d maxCCMDesatForSkinPercent=%6.4f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: fd-AWB: faces=%d raw=%d %d stats=%d %d statsBin=%d %d "
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: fd-AWB: fdRect= %d %d %d %d, tile= %d %d %d %d "
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: initial sky bnLogRatioDistoDaylightWeight = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: initial sky rgLogRatio = %.2f bgLogRatio = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: initial sky rgLogRatioWeight = %.2f bgLogRatioWeight = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: initial sky rnLogRatioDistoDaylightWeight = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: lux=%.2f luxFactor=%.2f ccm=%.2f %.2f %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: meta{8}.CCM = ["
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: meta{8}.ComboWBGain = [%d,%d,%d], awbScheme=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: meta{8}.WBGain = [%d,%d,%d], awbScheme=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: meta{8}.normalizedWBGain = [%d,%d,%d], awbScheme=%d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: params->bgLogRatio = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: params->rgLogRatio = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: params->rgLogRatio = %.2f params->bgLogRatio = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: rn_left=%6.2f %6d  rn_middle=%6.2f %6d rn_right=%6.2f %6d rn_target = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: sky_CCT=%6d sky_cct_shift=%.2f sky_rgLogRatio_target = %.2f"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: sky_pos= %.2f %.2f sky_target_pos= %.2f %.2f cct = %d -> %d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: table index = %d"
+ "<<<< AWBAlgorithm::CAWBAFE >>>> %s: wpRgLogRatio=%f wpBgLogRatio=%f wpSkinRgLogRatio=%f wpSkinBgLogRatio=%f skinColorSampleNum=%d continuousFDTimes=%d skinColorSampleVariance=%f minDistSkinToWhiteMapping=%f"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist:                 normFactor      = %6.4f \n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist:       FD Rect Size = %6d %6d %6d %6d \n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist:    prevSkinColorCenter  = [%6.4f %6.4f] \n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist:    prevWhitePointCenter = [%6.4f %6.4f] \n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist:    tile float size = %6.4f %6.4f %6.4f %6.4f \n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist:    tile uint8 size = %6d %6d %6d %6d \n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist: # %d of %d faces \n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist: # of continuous faces   = %3d \n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist: prevColorHistMixWeight          = %6.4f \n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist: weightColorHistMinDist          = %6.4f (%6.4f)\n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist: weightColorHistOverlappingRatio = %6.4f (%6.4f)\n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist: weightColorHistSampleNum        = %6.4f (%6d)\n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: CAWBAFEFDAssist: weightColorHistSampleVariance   = %6.4f (%6.4f)\n"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: FDAWB_ANOD_PROB = %d, %f, %f, %f, count=%d"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: FaceSkinDetection skinRGBRatio = %6.2f %6.2f %6.2f %d"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: SemanticAWB: ch=%d fn=%d semFn=%d fdAWBVer=%d"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: Semantic_Tile = %d, %f, %f, %f"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: fdAWBMeta->fdAssistMatchProvidedSkinGains==%d matchProvidedSkinGains==%d"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: fdAWBMeta->matchSkinColorSampleNum==%d fdAWBMeta->matchContinuousFDTimes==%d fdAWBMeta->matchSkinColorSampleVariance==%f fdAWBMeta->matchMinDistSkinToWhiteMapping==%f"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: reflowedFDAWBMeta->skinColorSampleNum==%d reflowedFDAWBMeta->continuousFDTimes==%d reflowedFDAWBMeta->skinColorSampleVariance==%f reflowedFDAWBMeta->minDistSkinToWhiteMapping==%f"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: w0=%d w1=%d w2=%d"
+ "<<<< AWBAlgorithm::CAWBAFEFDAssist >>>> %s: y=%d x=%d RGBRatio=%6.2f %6.2f %6.2f skinColor=%6.2f %6.2f %6.2f maskTile=%6.4f "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: AWBGainsGrayStatus = %s"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: LEDMainFlash=%1d ratio=%6.4f pmCalibValid=%1d ambientlux=%d %d %d flashLux=%d %d %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: ambient ccm=%f %f %f flash ccm=%f %f %f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: ambient wbGain=%d %d flash wbGain=%d %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: ch= %d fn= %4d mS= %d mP= %d lux/rn/bn/wbGain= %6d %.2f %.2f %.2f %.2f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: ch=%d fn=%d awbFn=%d mS=%d mP=%d scheme=%d lux=%d luxFloat=%6.2f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: ch=%d fn=%d input.update=%d curPtr=%d pastSize=%d output.update=%d dayS=%6.4f lightS=%6.4f initialWP=%d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: ch=%d fn=%d isDefault=%d isValid=%d isBypass=%d isMatchSlave=%d bSlave=%d "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: ch=%d fn=%d rgGainWP=%.2f bgGainWP=%.2f gwRGain=%.2f gwGGain=%.2f gwBGain=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: ch=%d fn=%d rn=%6.2f bn=%6.2f rgGain=%d bgGain=%d cct=%d usePrev=%d isStable=%d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: AWB: ch=%hhu fn=%d lux=%d WBRGain=%d WBBGain=%d ccm[0]=%6d ccm[4]=%6d ccm[8]=%6d "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: Channel: %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: ColorCal gains rgGain=%f, bgGain=%f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: Fetched from STRB key R/G=%f B/G=%f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: LED ratio: %f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: M2S %hhu %u"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: M2S Lattice LogAWBGain %f %f %f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: M2S Linear %f %f %f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: MFAWB: ch=%d F=%p D=%p "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: MFAWB: fdAWBMetaData: ch=%d F=%p D=%p "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: MFAWB:ch=%d fn=%d mS=%d mP=%d isDef=%d isConv=%d isMS=%d rn=%6.2f %6.2f meta=%6.2f %6.2f day=%6.2f "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: New cc    : %6d %6d %6d %6d "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: Preview channel: %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: STRBkey version=%d, strb_rg=%.6f strb_bg=%.6f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: STRBkey version=%d, ww_rg=%.6f ww_bg=%.6f cw_rg=%.6f cw_bg=%.6f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: WP = %.2f %.2f -> %.2f %.2f mix=%.2f Final WP = %.2f %.2f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: WP=%6.4f %6.4f skinWP=%6.4f %6.4f ccmDesat=%6.4f "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: With ColorCal R/G=%f B/G=%f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: bgGainCoeff   = %6d %6d %6d \n"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: cct= %d -> %d ccGain= %d %d -> %d %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: ch=%d fn=%d awbFn=%d defaultAE=%lld currentAE=%lld lux=%d exLux=%f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: currentCH=%d wideCamSetFile=0x%x slaveCamID=%2d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: cw_rg=%f cw_bg=%f ww_rg=%f ww_bg=%f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: grayIndex = %.2f %.2f dist=%.2f weight=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: gw: [%.2f %.2f] -> [%.2f %.2f] idx= %.2f -> %.2f totalPxlCnt= %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: gw= %.2f %.2f -> %.2f %.2f rg2=%.2f bg2=%.2f dist=%.2f w=%.2f "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: lux = %.2f %.2f luxRatio=%.2f weight=%.2f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: lux = %d -> %.0f w=%.2f gray(gw|awb)= %.2f %.2f nonIR=%.2f %.2f "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: lux= %d -> %.0f param->lux = %d %d weight=%.2f "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: lux=%5d dist=%5.2f mix=%6.4f fdTimes=%d skinWP=%5.2f %5.2f mixedWP=%5.2f %5.2f \n"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: lux=%6d => %6.4f wpDist=%6.4f => %6.4f fdMixWeight=%6.4f => %6.4f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: lux=%d weight=%.2f dayScore=%.2f, dayWeight=%.2f coef=%d %.2f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: new: awbGain = %d %d ccGain=%d %d combo=%d %d "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: new: ccm=%d %d %d; %d %d %d; %d %d %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: new: rgLogRatio=%f bgLogRatio=%f cct=%d "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: new: slaveCh%d useSpatialCCM =%d isLEDMainFlashforAWB=%d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: rgGainCoeff   = %6d %6d %6d \n"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: slaveCameraID = %08x (%02zu / %02d)"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: slaveWBGain RGWBGain = %6f BGWBGain=%6f "
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: version=%d slaveCh=%d, set-file=0x%x masterGain=%d %d slaveGain=%6.2f %6.2f"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: wbGain      = %d %d %d %d -> %d %d %d %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: wbGainCombo = %d %d %d %d -> %d %d %d %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: wbGainNorm  = %d %d %d %d -> %d %d %d %d"
+ "<<<< AWBAlgorithm::CAWBAFEH14 >>>> %s: wp= %.2f %.2f -> %.2f %.2f ccGain = %.2f %.2f -> %.2f %.2f wbGain= %.2f %.2f -> %.2f %.2f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: ACLightHint(all)    = %.2f freqConf=%.0f %.2f dc=%.0f %.2f "
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: ACLightHint(non-IR) = %.2f freqConf=%.0f %.2f dc=%.0f %.2f irRatio=%.2f %.2f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: DCLightHint(non-IR) = %.2f freqConf=%.0f %.2f dc=%.0f %.2f irRatio=%.2f %.2f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: LightChangeScore = %6.4f lux=%6.4f %6.4f irRatio=%6.4f %6.4f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: LightStableScore = %4.2f->%4.2f conf=%4.2f luxV=%4.2f irF=%4.2f irV=%4.2f dcF=%4.2f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: Unsupported platformID (%d) - proceeding without photometer support"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: currPtr=%d pastSize=%d "
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: daylightScore    = %4.2f->%4.2f conf=%4.2f luxF=%4.2f irF=%4.2f dcF=%4.2f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: dcRatio  = %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: dcRatio :    filtered: %6.0f mean: %6.0f var: %8.4f "
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: externalLux = %6.0f %6.0f %6.0f %6.0f %6.0f %6.0f %6.0f %6.0f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: externalLux: filtered: %6.0f mean: %6.0f var: %8.4f "
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: freqConf = %6.0f %6.0f %6.0f %6.0f %6.0f %6.0f %6.0f %6.0f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: freqConf:    filtered: %6.1f mean: %6.1f var: %8.4f "
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: irRatio  = %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: irRatio :    filtered: %6.4f mean: %6.4f var: %8.4f "
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: luxLevel = %6d %6d %6d %6d %6d %6d %6d %6d"
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: luxLevel:    filtered: %6.0f mean: %6.0f var: %8.4f "
+ "<<<< AWBAlgorithm::CAWBAFEPhotometerAssistPenrose >>>> %s: state    = %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f %6.4f"
+ "<<<< AWBProcessor >>>> %s: Couldn't get AWB bundle."
+ "<<<< AWBProcessor >>>> %s: Prepare to process with ModuleConfig"
+ "<<<< AWBProcessor >>>> %s: Using provided metal command queue %p"
+ "<<<< AWBProcessor >>>> %s: figMetalAllocator resources not correctly released"
+ "<<<< AWBStats >>>> %s:     bitDepth = %5d"
+ "<<<< AWBStats >>>> %s:     endX                = %5d ( %5d )"
+ "<<<< AWBStats >>>> %s:     endX        = %5d ( %5d )"
+ "<<<< AWBStats >>>> %s:     endY                = %5d ( %5d )"
+ "<<<< AWBStats >>>> %s:     endY        = %5d ( %5d )"
+ "<<<< AWBStats >>>> %s:     horzInt , vertInt   = %5d, %5d"
+ "<<<< AWBStats >>>> %s:     startX              = %5d ( %5d )"
+ "<<<< AWBStats >>>> %s:     startX      = %5d ( %5d )"
+ "<<<< AWBStats >>>> %s:     startY              = %5d ( %5d )"
+ "<<<< AWBStats >>>> %s:     startY      = %5d ( %5d )"
+ "<<<< AWBStats >>>> %s:     xCropOffset      = %5d"
+ "<<<< AWBStats >>>> %s:     yCropOffset      = %5d"
+ "<<<< AWBStats >>>> %s:   colorHist ( assumed : CBinLog = 0, InpSel = 0, ColorHistClipBinThre = 0 !! ) :"
+ "<<<< AWBStats >>>> %s:   downsizeRatio      = %d"
+ "<<<< AWBStats >>>> %s:   tiles :"
+ "<<<< AWBStats >>>> %s: --- AWB STATS - Calculating ANST skin mask"
+ "<<<< AWBStats >>>> %s: --- AWB STATS - Processing externally provided skin mask"
+ "<<<< AWBStats >>>> %s: --- AWB STATS - Tile stats xTiles = %d, yTiles = %d"
+ "<<<< AWBStats >>>> %s: --- AWB STATS - Use of downsizeRatio = %d"
+ "<<<< AWBStats >>>> %s: --- AWB STATS - faceAssistedBehaviorMode = %d"
+ "<<<< AWBStats >>>> %s: --- AWB STATS - regionOfInterestRect = [ x=%f y=%f width=%f height=%f ]"
+ "<<<< AWBStats >>>> %s: --- AWB STATS - statsRegionOfInterestRect is too small to fit a [%d x %d] grid with a minimum tile size of 4. Falling back to validRect instead"
+ "<<<< AWBStats >>>> %s: --- AWB STATS - using statsRegionOfInterestRect = [ x=%f y=%f width=%f height=%f ]"
+ "<<<< AWBStats >>>> %s: ColorHistConfig after runtime config with validRect of ((%f, %f), (%f x %f)) : "
+ "<<<< AWBStats >>>> %s: ColorHistConfig after runtime config: "
+ "<<<< AWBStats >>>> %s: ColorHistConfig before runtime config: "
+ "<<<< AWBStats >>>> %s: LSCConfig after runtime config with sensorReadoutRect of ((%f, %f), (%f x %f)) : "
+ "<<<< AWBStats >>>> %s: LSCConfig after runtime config with validRect of ((%f, %f), (%f x %f)) : "
+ "<<<< AWBStats >>>> %s: TileStatsConfig after runtime config with validRect of ((%f, %f), (%f x %f)) : "
+ "<<<< AWBStats >>>> %s: TileStatsConfig before runtime config: "
+ "<<<< AWBStats >>>> %s: Warning: getting AbsoluteColorCalibration from legacy UnitInfo path"
+ "<<<< AWBStats >>>> %s: Warning: getting IdealColorCalibration from legacy SetFile path"
+ "<<<< AWBStats >>>> %s: it:%d ct:%d lgt:%d sim:%d sym:%d pesm:%d pism:%d fsmo:%d anl:%d fasm:%d"
+ "<<<< CameraColorProcessing >>>> %s: Normalization of TotalSensorCropRect failed"
+ "<<<< CameraColorProcessing >>>> %s: Normalization of valid buffer rect failed"
+ "<<<< CameraColorProcessing >>>> %s: RawSensorHeight not found"
+ "<<<< CameraColorProcessing >>>> %s: RawSensorWidth not found"
+ "<<<< CameraColorProcessing >>>> %s: TotalSensorCropRect not found"
+ "<<<< CameraColorProcessing >>>> %s: normalizedSensorRawValidBufferRect: {{%g, %g}, {%g, %g}}"
+ "<<<< CameraColorProcessing >>>> %s: normalizedValidBufferRect: {{%g, %g}, {%g, %g}}"
+ "<<<< CameraColorProcessing >>>> %s: totalSensorCropRectRawCoords: {{%g, %g}, {%g, %g}}"
+ "<<<< CameraColorProcessing >>>> %s: validBufferRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: \n---- LTM rectangles:\nCropRect   ( %f, %f ), ( %f, %f )\nSourceRect ( %f, %f ), ( %f, %f )\n--------------------------------------------------\n"
+ "<<<< LTMAlgorithm >>>> %s:    adaptiveGainMax:                       %f"
+ "<<<< LTMAlgorithm >>>> %s:    adaptiveGainRange:                     %f"
+ "<<<< LTMAlgorithm >>>> %s:    adaptiveGainVersion:                   %d"
+ "<<<< LTMAlgorithm >>>> %s:    adaptiveGainVersion:       %d"
+ "<<<< LTMAlgorithm >>>> %s:    adaptiveHCSlope:                       %f"
+ "<<<< LTMAlgorithm >>>> %s:    allowPortraitOrientationLTCGridOverride:             %d"
+ "<<<< LTMAlgorithm >>>> %s:    calcGlobalHistOnROI:                   %d"
+ "<<<< LTMAlgorithm >>>> %s:    computeCurvesWoFaceBoost:              %d"
+ "<<<< LTMAlgorithm >>>> %s:    computeHDRCurves:                      %d"
+ "<<<< LTMAlgorithm >>>> %s:    computeHDRCurvesWoFaceBoost:           %d"
+ "<<<< LTMAlgorithm >>>> %s:    doGlobalCCM:                           %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableAdaptiveGain %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableAdaptiveGain:                    %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableAdaptiveGain:        %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableAntiAliasing:                    %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableCB:                              %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableCB:                  %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableDualLTC:                         %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableDualLTC:             %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableFATE:                            %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableFATE:                %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableFaceExposure:                    %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableFaceExposure:        %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableFaceGlobalWeight:                %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableFaceGlobalWeight:    %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableHardGainForLowLight:             %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableHardGainForLowLight: %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableHiResLocalHistogram:             %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableHiResLocalHistogram: %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableHiResThumbnail:      %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableMultiFaceFATE:                   %d"
+ "<<<< LTMAlgorithm >>>> %s:    enableMultiFaceFATE:       %d"
+ "<<<< LTMAlgorithm >>>> %s:    enablePreLTMHazeCorrection:            %d"
+ "<<<< LTMAlgorithm >>>> %s:    faceExposureTargetI:                   %@"
+ "<<<< LTMAlgorithm >>>> %s:    faceExposureTargetII:                  %@"
+ "<<<< LTMAlgorithm >>>> %s:    faceExposureTargetIII:                 %@"
+ "<<<< LTMAlgorithm >>>> %s:    faceExposureTargetIV:                  %@"
+ "<<<< LTMAlgorithm >>>> %s:    faceExposureTargetV:                   %@"
+ "<<<< LTMAlgorithm >>>> %s:    faceExposureTargetVI:                  %@"
+ "<<<< LTMAlgorithm >>>> %s:    faceGlobalWeightBGOverride:            %f"
+ "<<<< LTMAlgorithm >>>> %s:    faceGlobalWeightOverride:              %f"
+ "<<<< LTMAlgorithm >>>> %s:    isAdaptiveHighlightCompressionEnabled: %d"
+ "<<<< LTMAlgorithm >>>> %s:    isHazeEstimationEnabled:               %d"
+ "<<<< LTMAlgorithm >>>> %s:    isHighlightCompressionEnabled:         %d"
+ "<<<< LTMAlgorithm >>>> %s:    ispDGainThreshold:                     %f"
+ "<<<< LTMAlgorithm >>>> %s:    minimumAdaptiveHC_SIFR:                %f"
+ "<<<< LTMAlgorithm >>>> %s: --- Haze estimation ---"
+ "<<<< LTMAlgorithm >>>> %s: ------- --------------- -------"
+ "<<<< LTMAlgorithm >>>> %s: ------- Haze estimation face detected: %d"
+ "<<<< LTMAlgorithm >>>> %s: Adaptive Highlight Compression Gain: %f"
+ "<<<< LTMAlgorithm >>>> %s: AdaptiveGain: %f"
+ "<<<< LTMAlgorithm >>>> %s: AdaptiveGainConstrained: %f"
+ "<<<< LTMAlgorithm >>>> %s: After AdaptiveGain - softIspDGain=%f - hardIspDGain=%f"
+ "<<<< LTMAlgorithm >>>> %s: Before AdaptiveGain - softIspDGain=%f - hardIspDGain=%f"
+ "<<<< LTMAlgorithm >>>> %s: Could not make a dictionary representation from valid buffer rect"
+ "<<<< LTMAlgorithm >>>> %s: Could not read HLG tuning params metadata"
+ "<<<< LTMAlgorithm >>>> %s: Could not read SDR tuning params metadata"
+ "<<<< LTMAlgorithm >>>> %s: Could not read adaptiveGainMax field"
+ "<<<< LTMAlgorithm >>>> %s: Could not read adaptiveGainRange field"
+ "<<<< LTMAlgorithm >>>> %s: Could not read adaptiveHCSlope field"
+ "<<<< LTMAlgorithm >>>> %s: Could not read digital flash HLG tuning params metadata"
+ "<<<< LTMAlgorithm >>>> %s: Could not read digital flash tuning params metadata"
+ "<<<< LTMAlgorithm >>>> %s: Could not read faceExposureTargetSkinTone field"
+ "<<<< LTMAlgorithm >>>> %s: Could not read ispDGainThreshold field"
+ "<<<< LTMAlgorithm >>>> %s: Could not read minimumAdaptiveHC_SIFR field"
+ "<<<< LTMAlgorithm >>>> %s: Enabling features for ltmAlgoVersion %d:"
+ "<<<< LTMAlgorithm >>>> %s: Exposure Ratio (before HighlightCompression): %f"
+ "<<<< LTMAlgorithm >>>> %s: Exposure Ratio (before overflow >80.0f): %f"
+ "<<<< LTMAlgorithm >>>> %s: Exposure Ratio (final): %f"
+ "<<<< LTMAlgorithm >>>> %s: Fail to extract metadata for LTM calculation"
+ "<<<< LTMAlgorithm >>>> %s: Fail to get FinalCropRectFromSource"
+ "<<<< LTMAlgorithm >>>> %s: Fail to process LTM"
+ "<<<< LTMAlgorithm >>>> %s: Fail to process haze estimator"
+ "<<<< LTMAlgorithm >>>> %s: Fail to run adaptiveGain"
+ "<<<< LTMAlgorithm >>>> %s: FigMetalAllocator WireMemory is < %s >"
+ "<<<< LTMAlgorithm >>>> %s: Haze r:%f g:%f b%f"
+ "<<<< LTMAlgorithm >>>> %s: Invoked shader allocation paths for prewarming: %@"
+ "<<<< LTMAlgorithm >>>> %s: LTM parameters:"
+ "<<<< LTMAlgorithm >>>> %s: LTM params rectangles information not valid"
+ "<<<< LTMAlgorithm >>>> %s: LTM's exposure tuning params not present in a plist"
+ "<<<< LTMAlgorithm >>>> %s: LTM-bundle: %@"
+ "<<<< LTMAlgorithm >>>> %s: LTMIn texture conversion failed"
+ "<<<< LTMAlgorithm >>>> %s: Missing LTM params rectangles information"
+ "<<<< LTMAlgorithm >>>> %s: Missing inputTexToLTMInTexScale"
+ "<<<< LTMAlgorithm >>>> %s: Missing kFigCaptureStreamMetadata_ColorCorrectionMatrix"
+ "<<<< LTMAlgorithm >>>> %s: Missing ltmROIRect"
+ "<<<< LTMAlgorithm >>>> %s: Missing metadata"
+ "<<<< LTMAlgorithm >>>> %s: Missing or incorrect CCM"
+ "<<<< LTMAlgorithm >>>> %s: Missing validTexureRect"
+ "<<<< LTMAlgorithm >>>> %s: No raw metadata for compare."
+ "<<<< LTMAlgorithm >>>> %s: The ltmRGBToRGBAFloat is nil"
+ "<<<< LTMAlgorithm >>>> %s: The texture descriptor is nil"
+ "<<<< LTMAlgorithm >>>> %s: Tried to scale height to less than %g: %g x %g to height %g fitting aspect %g"
+ "<<<< LTMAlgorithm >>>> %s: Tried to scale width to less than %g: %g x %g to width %g fitting aspect %g"
+ "<<<< LTMAlgorithm >>>> %s: Unexpected isPortraitOrientated in LTMv1"
+ "<<<< LTMAlgorithm >>>> %s: Use FinalCropRectFromSource metadata ROI as LTM rectangle"
+ "<<<< LTMAlgorithm >>>> %s: Using FinalCropRectFromSource metadata ROI as LTM rectangle"
+ "<<<< LTMAlgorithm >>>> %s: Using provided metal command queue %p"
+ "<<<< LTMAlgorithm >>>> %s: Using valid rect for configuring tileStatsRegion in LTM "
+ "<<<< LTMAlgorithm >>>> %s: Warning: LTM tuning params is nil"
+ "<<<< LTMAlgorithm >>>> %s: Warning: LTM's dehaze tuning params is nil"
+ "<<<< LTMAlgorithm >>>> %s: _cropRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: _sourceRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: colorCorrectedRGBATexture is nil"
+ "<<<< LTMAlgorithm >>>> %s: dehazedRGBATexture is nil"
+ "<<<< LTMAlgorithm >>>> %s: driverInputMetadata.CBVer: %d, driverInputMetadata.faceLTMVer: %d, _driverInputMetadata.useHiResLocalHistogram: %d"
+ "<<<< LTMAlgorithm >>>> %s: faceBiasScaler: %f"
+ "<<<< LTMAlgorithm >>>> %s: finalCropRectLTMInCoords: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: finalCropRectLTMInCoordsNormalized: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: gain: %f"
+ "<<<< LTMAlgorithm >>>> %s: inChromaTex.width: %lu, inChromaTex.height: %lu"
+ "<<<< LTMAlgorithm >>>> %s: inRGBAFloatTex.width: %lu, inRGBAFloatTex.height: %lu"
+ "<<<< LTMAlgorithm >>>> %s: linearCompressedRGBATexture is nil"
+ "<<<< LTMAlgorithm >>>> %s: mCropRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: mSourceRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: norm_haze_thresh:%f"
+ "<<<< LTMAlgorithm >>>> %s: rgbaFloatTexture is nil"
+ "<<<< LTMAlgorithm >>>> %s: tmpCropRect: {{%g, %g}, {%g, %g}}"
+ "<<<< LTMAlgorithm >>>> %s: wrong thumbnailHeight"
+ "<<<< LTMAlgorithm >>>> %s: wrong thumbnailWidth"
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
+ "<<<< LTMAlgorithmV1 >>>> %s: Fail to create LTM metadata"
+ "<<<< LTMAlgorithmV1 >>>> %s: Fail to process LTM compute"
+ "<<<< LTMAlgorithmV1 >>>> %s: Fail to process LTM compute for HLG"
+ "<<<< LTMAlgorithmV1 >>>> %s: Fail to process LTM driver"
+ "<<<< LTMAlgorithmV1 >>>> %s: FigCaptureLTMLookUpTables:"
+ "<<<< LTMAlgorithmV1 >>>> %s: FigCaptureLocalCCMLookUpTables:"
+ "<<<< LTMAlgorithmV1 >>>> %s: FigCaptureLocalHistogramClippingData:"
+ "<<<< LTMAlgorithmV1 >>>> %s: FigCaptureLocalHistograms:"
+ "<<<< LTMAlgorithmV1 >>>> %s: computeCurvesWoFaceBoost: %d"
+ "<<<< LTMAlgorithmV1 >>>> %s: computeHDRCurves: %d"
+ "<<<< LTMAlgorithmV1 >>>> %s: computeHDRCurvesWoFaceBoost: %d"
+ "<<<< LTMAlgorithmV1 >>>> %s: driverInputMetadata is nil"
+ "<<<< LTMAlgorithmV1 >>>> %s: procHITHStat is nil"
+ "<<<< LTMAlgorithmV1 >>>> %s: statsObj is nil"
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
+ "<<<< LTMAlgorithmV2 >>>> %s: Fail to create LTM metadata"
+ "<<<< LTMAlgorithmV2 >>>> %s: Fail to finishCalculateHITHStatistics"
+ "<<<< LTMAlgorithmV2 >>>> %s: Fail to process LTM compute"
+ "<<<< LTMAlgorithmV2 >>>> %s: Fail to process LTM compute for HLG"
+ "<<<< LTMAlgorithmV2 >>>> %s: Fail to process LTM driver"
+ "<<<< LTMAlgorithmV2 >>>> %s: FigCaptureLTMLookUpTables:"
+ "<<<< LTMAlgorithmV2 >>>> %s: FigCaptureLocalCCMLookUpTables:"
+ "<<<< LTMAlgorithmV2 >>>> %s: FigCaptureLocalHistogramClippingData:"
+ "<<<< LTMAlgorithmV2 >>>> %s: FigCaptureLocalHistograms:"
+ "<<<< LTMAlgorithmV2 >>>> %s: computeCurvesWoFaceBoost: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s: computeHDRCurves: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s: computeHDRCurvesWoFaceBoost: %d"
+ "<<<< LTMAlgorithmV2 >>>> %s: driverInputMetadata is nil"
+ "<<<< LTMAlgorithmV2 >>>> %s: procHITHStat is nil"
+ "<<<< LTMAlgorithmV2 >>>> %s: statsObj is nil"
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
+ "ANSTInferenceWrapper.m"
+ "AWB Config can't be null"
+ "AWB algoObj can't be null"
+ "AWB requires AbsoluteColorCalibrations in camera info to configure."
+ "AWB requires CSCConfig in module config to configure."
+ "AWB requires Correlated Color Temperature in metadata to configure."
+ "AWB requires ISP digital gain in metadata to configure."
+ "AWB requires IdealColorCalibrations in ModuleConfig to configure."
+ "AWB requires a known portType."
+ "AWB requires metadata to configure."
+ "AWBFaceAssistedBehaviorMode_CalculateSkinMask requested but unable to load ANSTKit!"
+ "AWBFaceAssistedBehaviorMode_MatchProvidedSkinGains requires faceAssistedSkinGainsToMatch to configure."
+ "AWBProcessor not configured"
+ "AbsoluteColorCalibrations missing from CameraInfo"
+ "AdaptiveGainVersion"
+ "B!C"
+ "Bitdepth not found"
+ "C1Max not found"
+ "C1Min not found"
+ "C1Offset not found"
+ "C1Scale not found"
+ "C2Max not found"
+ "C2Min not found"
+ "C2Offset not found"
+ "C2Scale not found"
+ "CAWBAFEPhotometerAssistPenrose"
+ "CCMCoef entry not found"
+ "CGRectMakeWithDictionaryRepresentation( (__bridge CFDictionaryRef)validTextureRectDict, &validBufferRect )"
+ "CSCChromaScale0 not found"
+ "CSCChromaScale1 not found"
+ "CSCCoef entry not found"
+ "CSCCoeff entry not found"
+ "CSCMax entry not found"
+ "CSCMin entry not found"
+ "CSCOffset entry not found"
+ "CSCOffsetIn entry not found"
+ "CSCOffsetOut entry not found"
+ "CalculateSkinTileANODProbMap"
+ "CalculateSkinWeightForSTF"
+ "CameraInfo missing AbsoluteColorCalibrations.HighCCT"
+ "CameraInfo missing AbsoluteColorCalibrations.LowCCT"
+ "ComputeAWBGains"
+ "ComputeAWBGainsCore"
+ "ComputeAWBGainsGrayworld"
+ "ComputeDigitalFlashAWBV1"
+ "ComputeDigitalFlashAWBV2"
+ "ComputeSkinColor_fdProbApproach"
+ "CondSel not found"
+ "Could not find AGC in metadata"
+ "Could not find exposureTime in metadata"
+ "Could not find range expansion factor in metadata"
+ "Could not find sensorDGain"
+ "Count entry not found"
+ "CountClipEnable not found"
+ "DBGain entry not found"
+ "DBMax entry not found"
+ "DBMin entry not found"
+ "DBOffset entry not found"
+ "Dawn"
+ "Enable not found"
+ "EnableFaceExposure"
+ "EnableFaceGlobalWeight"
+ "EnableHardGainForLowLight"
+ "EnableHiResThumbnail"
+ "EnableMultiFaceFATE"
+ "EndX not found"
+ "EndY not found"
+ "FaceSkinDetection"
+ "Failed to set up the allocator"
+ "FigMetalAllocator resources not correctly released"
+ "FigMetalAllocator setupWithDescriptor:allocatorBackend failed"
+ "Full image size cannot equal 0"
+ "GetFDAWBMetaData"
+ "GetInternalAWBMetaData"
+ "GetMetaData"
+ "GetOneFrameAWBMetaData"
+ "GetPhotometerAWBMetaData"
+ "GreenAverage not found"
+ "HighCCT missing from absoluteColorCal"
+ "HighCCT missing from idealColorCal"
+ "IOSurfaceGetBaseAddress failed"
+ "IOSurfaceLock failed"
+ "InitialReset"
+ "InterpCCMfromBases"
+ "IntervalX not found"
+ "IntervalY not found"
+ "Invalid QuadraBinningFactor metadata value"
+ "LSC gains has to be texture array for fast quadra kernel"
+ "LUT entry not found"
+ "LineDeltaC1 not found"
+ "LineDeltaC2 not found"
+ "LineMax not found"
+ "LineOffset not found"
+ "LowCCT missing from absoluteColorCal"
+ "LowCCT missing from idealColorCal"
+ "LumaMax not found"
+ "LumaMin not found"
+ "Max awbComboGain < AWB_GAIN_IDENTITY"
+ "MinimalReset"
+ "Missing AWBComboBGain"
+ "Missing AWBComboGGain"
+ "Missing AWBComboRGain"
+ "ModifyColorHistogramProbApproach"
+ "ModuleConfig missing AutoWhiteBalance parameters"
+ "ModuleConfig missing BoundingEllipsesModel parameters"
+ "ModuleConfig missing IdealColorCalibrations.HighCCT"
+ "ModuleConfig missing IdealColorCalibrations.LowCCT"
+ "ModuleConfig missing MatrixRGBToXYZ parameters"
+ "ModuleConfig missing MatrixXYZToRGB parameters"
+ "ModuleConfig missing UseFlashCCMMixing parameters"
+ "ModuleConfig missing UseQuantileLuxLevels parameters"
+ "ModuleConfig missing tuning table parameters"
+ "No LuxModel->Scale parameter in module config"
+ "No LuxModel->ScaleShift parameter in module config"
+ "OffsetIn entry not found"
+ "OffsetOut entry not found"
+ "Process"
+ "ProcessMatchSlaveAWB"
+ "ProjectFlashWP"
+ "Sensor layout not supported"
+ "SensorCropRect is missing"
+ "SetCCMDesatForSkinEnable"
+ "SetFDAWBMetaData"
+ "SetFaceAssistedAWBResultsForMatchProvidedSkinGains"
+ "SetFlashProjectionConfig"
+ "SetFlashStateForHistAWB"
+ "SetFlickerDetectionResult"
+ "SetInternalAWBMetaData"
+ "SetPhotometerAWBMetaData"
+ "SetSemanticConfidenceMap"
+ "SetSlaveCameraListColorMatchingModel"
+ "SetSmoothingSamplingRate"
+ "SmoothingActivate"
+ "StartX not found"
+ "StartY not found"
+ "StatSel not found"
+ "Sydney"
+ "The extents of the validRect lie outside the full-sized RAW bounds"
+ "The extents of the validRect lie outside the sensorReadoutRect"
+ "The regionOfInterestRectDict does not represent a valid CGRect"
+ "The regionOfInterestRectDict is not contained within the validRect"
+ "The sensorReadoutRectDict does not represent a valid CGRect"
+ "The validRectDict does not represent a valid CGRect"
+ "Unable to allocate AWBAlgorithm object"
+ "Unable to allocate output metadata"
+ "Unable to calculateInternalAWBMetadataForMIWB"
+ "Unable to configure AWB object"
+ "Unable to updateHRGainDownRatioMetadata"
+ "Unexpected ANST semantic mask size"
+ "Unexpected pipeline configuration, expected: fast pipeline and floating point input format, found: precise pipeline and fixed point input format?"
+ "Unexpected sky mask size"
+ "Unsupported ANSTISPInferenceVersion"
+ "Unsupported AWB stats thumbnail downsizeRatio."
+ "UpdateANODTileProbTable"
+ "UpdateColorInformation"
+ "UpdateSemanticTileProbTable"
+ "UseProvidedMatchSkinGains"
+ "Wrong valid rectangle dictionary"
+ "YThd entry not found"
+ "_AWBAlgorithmObj is NULL"
+ "_adaptiveGain is NULL"
+ "_allocateClientIOPixelBuffers failed"
+ "_anstInferenceDescriptor"
+ "_anstInferenceDescriptor is nil"
+ "_anstInferenceWrapper"
+ "_anstInputPixelBuffer is nil"
+ "_anstInputTex"
+ "_anstInputTex is nil"
+ "_anstOutputTex"
+ "_anstOutputTex is nil"
+ "_awbAlgo is NULL"
+ "_awbStats is NULL"
+ "_bindANSTEspressoV1ClientIO failed"
+ "_bindANSTEspressoV5ClientIO failed"
+ "_bindANSTEspressoV5IOPorts failed"
+ "_calcLTMStatisticsPipelineState is NULL"
+ "_calcLocalHistogramShift is NULL"
+ "_collectLocalHistHiResKernelPipelineState is NULL"
+ "_collectLocalHistKernelPipelineState is NULL"
+ "_computePipelineHazeThumbnailGeneration is NULL"
+ "_computePipelineHistogramGeneration is NULL"
+ "_configHistRuntimeWithValidRect"
+ "_configLSCRuntimeWithValidRect"
+ "_configStatsDownsizeRatioRuntimeWithValidRect"
+ "_configStatsROIRuntimeWithRegionOfInterestRect"
+ "_configTilesRuntimeWithValidRect"
+ "_esopBindInputSurfaceObject failed: %s"
+ "_esopBindOutputSurfaceObject failed: %s"
+ "_espressoContext is NULL"
+ "_espressoPlan is NULL"
+ "_globalFaceHistKernelPipelineState is NULL"
+ "_globalHistKernelPipelineState is NULL"
+ "_hazeEstimator is NULL"
+ "_hazeProperties is NULL"
+ "_inputImageDescriptor"
+ "_inputImageDescriptor is nil"
+ "_loadANSTEspressoV1NetworkFromURL failed"
+ "_loadANSTEspressoV5NetworkFromURL failed"
+ "_localHistAndThumKernelPipelineState is NULL"
+ "_localHistHiResAndThumKernelPipelineState is NULL"
+ "_metalContext is NULL"
+ "_outputSkinMapDescriptor"
+ "_outputSkinMapDescriptor is nil"
+ "_stats is NULL"
+ "absoluteColorCals is NULL"
+ "allocatorBackend is  nil"
+ "allocatorBackend offers memory pool of insufficient size for AWB"
+ "allocatorDesc is NULL"
+ "angleInfoRoll is NULL"
+ "anstBuf32FloatLocked = ( CVPixelBufferLockBaseAddress( anstBuf32Float, kCVPixelBufferLock_ReadOnly ) == kCVReturnSuccess )"
+ "anstBuf8Locked = ( CVPixelBufferLockBaseAddress( anstBuf8, 0 ) == kCVReturnSuccess )"
+ "anstModelConfig is nil"
+ "anstOutputPixelBuffer is nil"
+ "anstOutputPixelBuffer8 is nil"
+ "assetType > -1"
+ "assetType is < 0"
+ "assetURL is nil"
+ "awbConfigSecondarySensor is NULL"
+ "awbParams is NULL"
+ "bd"
+ "bd is NULL"
+ "calculateCCMDesatFactorForSkin"
+ "calculateGrayIndexFromGrayworld"
+ "calculateSTRBkeyFromWideCameraNew"
+ "calculateSlaveCameraWBGainNew"
+ "calculateSlaveCameraWBGainfromMatchingModel"
+ "cameraInfo is NULL"
+ "ccmConfig is NULL"
+ "ccmWithNewWhitePoint"
+ "cmdBuf is NULL"
+ "cmdEnc is NULL"
+ "colorMatchingForSensor is NULL"
+ "configAWBStatsDBV2"
+ "configCCM"
+ "configCSC2V2"
+ "configCSCV2"
+ "configColorHistV2"
+ "configGAMV2"
+ "configLSC"
+ "configLinearRGBToANSTInput"
+ "configPixFiltV2"
+ "configTilesV2"
+ "convertANSTMaskFrom32FloatTo8Uint"
+ "cscConfig is NULL"
+ "defaultHistWeightMultiplicator"
+ "disabled"
+ "driverInputMetadata"
+ "e5rtError == 0 "
+ "e5rt_buffer_object_get_iosurface failed: %s"
+ "e5rt_e5_compiler_compile failed: %s"
+ "e5rt_e5_compiler_create failed: %s"
+ "e5rt_e5_compiler_options_create failed: %s"
+ "e5rt_execution_stream_create failed: %s"
+ "e5rt_execution_stream_encode_operation failed: %s"
+ "e5rt_execution_stream_execute_sync failed: %s"
+ "e5rt_execution_stream_operation_create_precompiled_compute_operation failed: %s"
+ "e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options failed: %s"
+ "e5rt_execution_stream_operation_get_input_names failed: %s"
+ "e5rt_execution_stream_operation_get_num_inputs failed: %s"
+ "e5rt_execution_stream_operation_get_num_outputs failed: %s"
+ "e5rt_execution_stream_operation_get_output_names failed: %s"
+ "e5rt_execution_stream_operation_retain_input_port failed: %s"
+ "e5rt_execution_stream_operation_retain_output_port failed: %s"
+ "e5rt_io_port_bind_buffer_object failed: %s"
+ "e5rt_io_port_bind_surface_object failed: %s"
+ "e5rt_io_port_is_tensor failed: %s"
+ "e5rt_io_port_retain_surface_desc failed: %s"
+ "e5rt_io_port_retain_tensor_desc failed: %s"
+ "e5rt_precompiled_compute_op_create_options_create_with_program_function failed: %s"
+ "e5rt_program_library_retain_program_function failed: %s"
+ "e5rt_surface_object_alloc failed: %s"
+ "e5rt_surface_object_create_from_iosurface failed: %s"
+ "e5rt_surface_object_get_iosurface failed: %s"
+ "e5rt_surface_object_release failed: %s"
+ "e5rt_tensor_desc_alloc_buffer_object failed: %s"
+ "eitFound"
+ "enabled"
+ "err"
+ "espressoStatus == 0 "
+ "espresso_network_bind_cvpixelbuffer failed"
+ "espresso_plan_add_network failed"
+ "espresso_plan_build failed"
+ "espresso_plan_execute_sync failed"
+ "faceAssistedBehaviorMode unspecified, defaulting to AWBFaceAssistedBehaviorMode_UseFaceRectangle"
+ "faceDataDict is NULL"
+ "faceExposureTargetSkinTone"
+ "faceGlobalWeight"
+ "faceGlobalWeightBG"
+ "fcmu_aspectFitRectInsideRect"
+ "figTexDescr is NULL"
+ "filterHConfig is NULL"
+ "filterVConfig is NULL"
+ "flareConfidence"
+ "hazeInternalBuffer"
+ "hazeInternalBuffer is NULL"
+ "highlightContrastScale"
+ "highlightContrastScaleCB"
+ "histConfig is NULL"
+ "hrGainDownRatio < 1"
+ "idealColorCals is NULL"
+ "internalMIWBMetadata is NULL"
+ "internalMetadata is NULL"
+ "internalMetadata is nil"
+ "internalSpatialCCMMetadata is NULL"
+ "ispDGainMetadata is NULL"
+ "kCCPMetadata_continuousFDTimes unspecified"
+ "kCCPMetadata_minDistSkinToWhiteMapping unspecified"
+ "kCCPMetadata_skinColorSampleNum unspecified"
+ "kCCPMetadata_skinColorSampleVariance unspecified"
+ "kCCPMetadata_wpBgLogRatio unspecified"
+ "kCCPMetadata_wpRgLogRatio unspecified"
+ "kCCPMetadata_wpSkinBgLogRatio unspecified"
+ "kCCPMetadata_wpSkinRgLogRatio unspecified"
+ "kCMBaseObjectError_AllocationFailed"
+ "kCMBaseObjectError_ParamErr"
+ "kCMBaseObjectError_UnsupportedOperation"
+ "kCMBaseObjectError_UnsupportedVersion"
+ "kCMBaseObjectError_ValueNotAvailable"
+ "kFigCaptureStreamMetadata_HRGainDownRatio not set"
+ "localHistograms is NULL"
+ "metadata is NULL"
+ "mixLightCCMConfig is NULL"
+ "moduleConfig is NULL"
+ "pPointEntry is NULL"
+ "pSkinToWhiteLutEntry is NULL"
+ "params.rectangles"
+ "params.rectangles.faceRectangles"
+ "params.rectangles.inputTexToLTMInTexScale"
+ "params.rectangles.ltmROIRect"
+ "params.rectangles.validTextureRect"
+ "portNames"
+ "portNames is NULL"
+ "postTintConfig is NULL"
+ "previewMetadata is nil"
+ "previewMetadata kFigCaptureStreamMetadata_AWBComboBGain is nil"
+ "previewMetadata kFigCaptureStreamMetadata_AWBComboGGain is nil"
+ "previewMetadata kFigCaptureStreamMetadata_AWBComboRGain is nil"
+ "procHITHStat"
+ "projPoints is NULL"
+ "ratioConfig is NULL"
+ "reSizedAnstSkinMaskTex is NULL"
+ "scanner is NULL"
+ "schemeConfig is NULL"
+ "secondaryBGain is NULL"
+ "secondaryRGain is NULL"
+ "self is NULL"
+ "sensorClockFreqHz missing/zero; falling back to 1 MHz"
+ "setFileID is NULL"
+ "setFileOrigin is NULL"
+ "setSlaveCameraCSensorCalGain"
+ "statsObj"
+ "surfaceAddress"
+ "surfaceAllocSize > 0"
+ "thumbnailHeight >= ( 26 )"
+ "thumbnailWidth >= ( 34 )"
+ "trimScaleConfig is NULL"
+ "true"
+ "updateLuxLevelFromSceneChangeDetection"
+ "updatePhotometerDetectionOutput"
+ "wbTmRGBTex is NULL"
+ "xCoordinateConfig is NULL"
+ "xtoCCT is NULL"
+ "yThConfig is NULL"
+ "zeroInitializeIOSurface"
+ "~CAWBAFE"
- "! error"
- "#16@0:8"
- "%s signalled err=%d at <>:%d"
- "-[HazeEstimation prepareThumbnail]"
- "-[LTMCurvesComputeV2 initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:]"
- "-[LTMStats startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:]"
- "-[LTMStatsCompute computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:]"
- ".cxx_construct"
- ".cxx_destruct"
- "16@0:8"
- "40@0:8i16^20f28@32"
- "<<<< AWBStats >>>> %s: it:%d ct:%d lgt:%d sim:%d sym:%d pesm:%d pism:%d fsmo:%d ep:%d aipb:%d aopb:%d fasm:%d"
- "@\"<AWBIBPParams>\""
- "@\"<AWBIBPParams>\"16@0:8"
- "@\"<LTMExtractMetadataBase>\""
- "@\"<LTMGeometryDataBase>\""
- "@\"<LTMIBPParams>\""
- "@\"<MTLBuffer>\""
- "@\"<MTLCommandBuffer>\""
- "@\"<MTLCommandQueue>\""
- "@\"<MTLCommandQueue>\"16@0:8"
- "@\"<MTLComputePipelineState>\""
- "@\"<MTLDevice>\""
- "@\"<MTLTexture>\""
- "@\"<MTLTexture>\"16@0:8"
- "@\"AWBAlgorithm\""
- "@\"AWBStatistics\""
- "@\"AdaptiveGain\""
- "@\"CMIExternalMemoryDescriptor\"24@0:8@\"CMIExternalMemoryConfiguration\"16"
- "@\"CMIExternalMemoryResource\""
- "@\"CMIExternalMemoryResource\"16@0:8"
- "@\"FigMetalContext\""
- "@\"HazeEstimation\""
- "@\"HazeProperties\""
- "@\"LTMComputeRefV1\""
- "@\"LTMComputeRefV2\""
- "@\"LTMDriverRefV1\""
- "@\"LTMDriverRefV2\""
- "@\"LTMStats\""
- "@\"LTMStatsCompute\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSMutableDictionary\""
- "@\"NSMutableDictionary\"16@0:8"
- "@\"NSNumber\""
- "@\"NSNumber\"16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@20@0:8f16"
- "@24@0:8:16"
- "@24@0:8@\"FigMetalContext\"16"
- "@24@0:8@16"
- "@24@0:8^{_NSZone=}16"
- "@28@0:8@16f24"
- "@28@0:8@16i24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8Q16Q24"
- "@40@0:8:16@24@32"
- "@40@0:8@1624"
- "@40@0:8@16Q24Q32"
- "@48@0:8^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32@40"
- "@48@0:8^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32@40"
- "@68@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24@32@40B48B52B56B60B64"
- "@72@0:8@16{?=[3]}24"
- "@80@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24@32@40B48B52B56B60B64B68B72B76"
- "AWBAlgorithm"
- "AWBIBPParams"
- "AWBImageBufferProcessor"
- "AWBProcessor"
- "AWBStatistics"
- "AdaptiveGain"
- "B"
- "B16@0:8"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16"
- "B32@0:8@16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24"
- "B40@0:8@\"<LTMIBPParams>\"16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24@\"<LTMGeometryDataBase>\"32"
- "B40@0:8@16@24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32"
- "B40@0:8@16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24@32"
- "B48@0:8@16@24@32^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}40"
- "CGRectMakeWithDictionaryRepresentation( (__bridge CFDictionaryRef)validBufferRectDict, &validBufferRect )"
- "CVPixelBufferLockBaseAddress( anstBuf32Float, kCVPixelBufferLock_ReadOnly ) == kCVReturnSuccess"
- "CVPixelBufferLockBaseAddress( anstBuf8, 0 ) == kCVReturnSuccess"
- "CVPixelBufferUnlockBaseAddress( anstBuf32Float, kCVPixelBufferLock_ReadOnly ) == kCVReturnSuccess"
- "CVPixelBufferUnlockBaseAddress( anstBuf8, 0 ) == kCVReturnSuccess"
- "FWPlatformIDUtilities"
- "GPUEndTime"
- "GPUStartTime"
- "GeometryUtilities"
- "HazeEstimation"
- "HazeProperties"
- "I16@0:8"
- "ImageBufferProcessor"
- "LTMAlgorithmBase"
- "LTMComputeBaseV1"
- "LTMComputeBaseV2"
- "LTMComputeRefV1"
- "LTMComputeRefV2"
- "LTMCurvesComputeBase"
- "LTMCurvesComputeV1"
- "LTMCurvesComputeV2"
- "LTMDriverBaseV1"
- "LTMDriverBaseV2"
- "LTMDriverRefV1"
- "LTMDriverRefV2"
- "LTMExtractMetadataBase"
- "LTMExtractMetadataV1"
- "LTMExtractMetadataV2"
- "LTMGeometryDataBase"
- "LTMGeometryDataV1"
- "LTMGeometryDataV2"
- "LTMIBPParams"
- "LTMImageBufferProcessor"
- "LTMMetadataWriterV1"
- "LTMMetadataWriterV2"
- "LTMProcessor"
- "LTMStats"
- "LTMStatsCompute"
- "MetalImageBufferProcessor"
- "NSObject"
- "Q16@0:8"
- "S"
- "T#,R"
- "T,N,V_hazeValue"
- "T,N,V_hazeValueForLTM"
- "T@\"<AWBIBPParams>\",R,N"
- "T@\"<AWBIBPParams>\",R,N,V_awbParams"
- "T@\"<LTMIBPParams>\",R,N,V_ltmParams"
- "T@\"<MTLCommandQueue>\",&,N"
- "T@\"<MTLCommandQueue>\",&,N,V_metalCommandQueue"
- "T@\"<MTLTexture>\",&,N"
- "T@\"<MTLTexture>\",&,N,V_clippedTex"
- "T@\"<MTLTexture>\",&,N,V_imageTex"
- "T@\"<MTLTexture>\",&,N,V_inChromaTex"
- "T@\"<MTLTexture>\",&,N,V_inLumaTex"
- "T@\"<MTLTexture>\",&,N,V_inRGBAFloatTex"
- "T@\"<MTLTexture>\",&,N,V_inRGBImageUInt16Tex"
- "T@\"<MTLTexture>\",&,N,V_inputRGBTexture"
- "T@\"<MTLTexture>\",&,N,V_lscGainsTex"
- "T@\"<MTLTexture>\",&,N,V_skinMask"
- "T@\"<MTLTexture>\",&,N,V_skyMask"
- "T@\"CMIExternalMemoryResource\",?,&,N"
- "T@\"CMIExternalMemoryResource\",?,&,N,V_externalMemoryResource"
- "T@\"HazeProperties\",&,N,V_hazeProperties"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",&,N,V_hazeEstimation"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",&,N,V_cameraInfo"
- "T@\"NSDictionary\",&,N,V_faceAssistedSkinGainsToMatch"
- "T@\"NSDictionary\",&,N,V_inMetaData"
- "T@\"NSDictionary\",&,N,V_inputBufferRect"
- "T@\"NSDictionary\",&,N,V_metadata"
- "T@\"NSDictionary\",&,N,V_moduleConfig"
- "T@\"NSDictionary\",&,N,V_outMetaData"
- "T@\"NSDictionary\",&,N,V_regionOfInterestRectInBufferCoords"
- "T@\"NSDictionary\",&,N,V_secondaryCameraInfo"
- "T@\"NSDictionary\",&,N,V_secondaryModuleConfig"
- "T@\"NSDictionary\",&,N,V_stats"
- "T@\"NSDictionary\",&,N,V_tuningParameters"
- "T@\"NSDictionary\",&,N,V_validBufferRect"
- "T@\"NSDictionary\",&,N,V_validRectInBufferCoords"
- "T@\"NSDictionary\",&,N,V_validRectInSensorReadoutCoords"
- "T@\"NSDictionary\",&,N,VcameraInfoByPortType"
- "T@\"NSDictionary\",&,N,VtuningParameters"
- "T@\"NSMutableDictionary\",&,N"
- "T@\"NSMutableDictionary\",&,N,V_outputMetadata"
- "T@\"NSNumber\",&,N"
- "T@\"NSNumber\",&,N,V_cfaLayout"
- "T@\"NSNumber\",&,N,V_digitalFlash"
- "T@\"NSNumber\",&,N,V_downsizeFactor"
- "T@\"NSNumber\",&,N,V_faceAssistedBehaviorMode"
- "T@\"NSNumber\",&,N,V_firstPixel"
- "T@\"NSNumber\",&,N,V_lscMaxGain"
- "T@\"NSNumber\",&,N,V_lscModulationWeight"
- "T@\"NSNumber\",&,N,V_skipDemosaic"
- "T@\"NSNumber\",R,N,V_digitalFlash"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TB,?,R,N"
- "TB,N"
- "TB,N,V_calcGlobalHistOnROI"
- "TB,N,V_computeCurvesWoFaceBoost"
- "TB,N,V_computeHDRCurves"
- "TB,N,V_computeHDRCurvesWoFaceBoost"
- "TB,N,V_digitalFlash"
- "TB,N,V_doAdaptiveFaceBiasScaler"
- "TB,N,V_doGlobalCCM"
- "TB,N,V_doHazeEstimation"
- "TB,N,V_enableAntiAliasing"
- "TB,N,V_isAdaptiveHighlightCompressionEnabled"
- "TB,N,V_isHighlightCompressionEnabled"
- "TB,N,V_isSIFR"
- "TB,N,V_undoHRGainDownRatio"
- "TI,N,V_winRegionHeight"
- "TI,N,V_winRegionWidth"
- "TI,R,N,V_numTilesX"
- "TI,R,N,V_numTilesY"
- "TQ,R"
- "Tf,N"
- "Tf,N,V_adaptiveHCSlope"
- "Tf,N,V_deepZoomRatio"
- "Tf,N,V_evmExpRatio"
- "Tf,N,V_evtBkt"
- "Tf,N,V_haze_threshold_divider"
- "Tf,N,V_inputTextureDownsampleRatio"
- "Tf,N,V_ispDGainThreshold"
- "Tf,N,V_ispRes"
- "Tf,N,V_maxHazePercentile"
- "Tf,N,V_min_display_black"
- "Tf,N,V_minimumAdaptiveHC_SIFR"
- "Tf,N,V_reluC1"
- "Tf,N,V_reluC2"
- "Tf,N,V_reluC3"
- "Tf,N,V_reluC4"
- "Tf,N,V_reluC5"
- "Tf,N,V_sr_min"
- "Tf,N,V_sr_pow"
- "Tf,N,V_sr_sat"
- "Tf,N,V_sr_var"
- "Ti,N"
- "Ti,N,V_optimizationLevel"
- "Ti,N,V_rawSensorHeight"
- "Ti,N,V_rawSensorWidth"
- "T{?=III},N"
- "T{?=III},N,V_awbComboGains"
- "T{?=III},N,V_awbComboGainsNormalized"
- "T{?=III},N,V_awbGains"
- "T{?=III},R,N,V_awbComboGains"
- "T{?=III},R,N,V_awbComboGainsNormalized"
- "T{?=III},R,N,V_awbGains"
- "T{CGAffineTransform=dddddd},N,V_sensorSpaceToValidBufferSpaceTransform"
- "T{CGPoint=dd},N"
- "T{CGPoint=dd},N,V_deepZoomOrigin"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_tileStatsROIRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_cropRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_sourceRect"
- "T{CGSize=dd},R,N"
- "T{CGSize=dd},R,N,V_inputTextureSize"
- "T{SourceROI=IIII},N,V_hazeROI"
- "UTF8String"
- "Vv16@0:8"
- "[1024I]"
- "[12480S]"
- "[256I]"
- "[2I]"
- "[3264S]"
- "[4420S]"
- "^v"
- "^{CAWBAFE=^^?i^{CDualLEDsWhitePointProjector}{?=[9f][9f][6{?=fffff}]{?=[6f][6f][6f][6f][6f][6f]}[3{?=ff}][3{?=ff}][3{?=ff}][3{?=ff}]BB}^{CAWBAFEFDAssist}^{CAWBAFEPhotometerAssistPenrose}^{sPhotometerAWBMetadata}^{_FE_3A_Stats_H15}^{_FE_3A_Stats_H15}^{_TILE_Stat_Elem}^{_AEAWB_Stat_Elem}^{_HighResAWBAE_Stat_Elem}^I{sFEStatCSCConfig=[9s][9s][3s][3S][3S][2S]C}{sFEStatColorHistConfig=[15S][16C]SISI}ISSSBI[3I][3I][3[3i]][3[3i]]IBBBIIi[3S][3S]IffSfffffff{sAWBInternalParams=SSBBBffffffffffffffffffffI[1024I]}B{sAWBDigitalFlashSkyParams=iBffffffff}iBfff[1024I][1024I][6[4s]][3S][9s][2S][2S][13S][3S][32S]S*[1024C][6[1024C]][6s]CSSSSfSSSSB[3I]fSiBi[30[2s]]I[8[3S]]I[6[9s]]{sCSensorCalGain=SSSS}SSSSBI[4I]II{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}ffBBBBBfii[3I]^{fdAWBMetaData}[150[4S]]IBB{sWPStableZoneControlTable={sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}}BBCCQSS^{sMetaData}[3S]iBi[2f]f[30[2s]][6I][6I]B[6S]S[32S]B[192f]{sAWBTimelapseParams=BBI{sAWBTimelapseSmoothingState=ff[3f][3f]fffSB}}f{sCIspCmdChColorCalIdealSet=ISS(?=I{sCIspControllerCmdHdrChInfo=b16b15b1})SSSS}Bi{sUnagiParams=i}C}"
- "^{LTMCompute=^^?QBII^{sLtmTuningParams}[256f][257f]{sLtmDisplayParams=[257f][257f]f}f{sLtmFrameParams=[48f][48f]ff[257f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][256f][257f][3f]ffffffffffffffffffffffff}[5[2118f]][5B]}"
- "^{LTMCompute=^^?Q^{sLtmTuningParams}{sLtmDisplayParams=[65f][65f]f}{sLtmFrameParams=[48f][48f]ff[65f][64f][64f][64f][64f][64f][64f][64f][65f][3f]ffffffffffffffffffffff}[4[342f]][4B]}"
- "^{LTMDriver=^^?{sLtmComputeInput=[3072f][64f][1024f][48f][48f][64f][64f][65f][48f]ffffffffffffS[9f][192f]fffBB[48f]f}{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBiBif}C[6{LTMTuning=ffffffffffffffffffffffffffff}]B}iB}"
- "^{LTMDriver=^^?{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}BIIiB}"
- "^{_NSZone=}16@0:8"
- "^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16@0:8"
- "_adaptiveGainMax"
- "_adaptiveGainRange"
- "_adaptiveGainValue"
- "_adaptiveHCSlope"
- "_addAverageLTMToMetadata:curvesType:fromOutput:"
- "_addAverageLTMToMetadata:curvesType:fromOutput:ltcNumNodes:"
- "_addGlobalLTMLookUpTableAlignedToFinalCropRect:"
- "_addHazeCorrection:driverInputMetadata:"
- "_addHighlightCompression:driverInputMetadata:"
- "_addLTMCurveTypeToMetadata:driverInputMetadata:"
- "_addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:"
- "_addLTMCurvesToMetadata:curvesType:fromOutput:statistics:geometryData:isSIFR:ltcNumNodes:"
- "_addLTMEnabledToMetadata:"
- "_addLocalClippingDataToMetadata:statistics:geometryData:"
- "_addLocalHistToMetadata:statistics:geometryData:"
- "_addSoftDGainToMetadata:driverInputMetadata:"
- "_addSpatialCCMDataToMetadata:fromOutput:driverInputMetadata:"
- "_addSpatialCCMDataToMetadata:fromOutput:statistics:geometryData:driverInputMetadata:"
- "_adjustConfigToValidRectInBufferCoords:validRectInSensorReadoutCoords:regionOfInterestRectInBufferCoords:"
- "_allocatorForceSize"
- "_allocatorSetupComplete"
- "_allocatorWireMemory"
- "_applyGlobalCCM:globalCCM:"
- "_awbComboGains"
- "_awbComboGainsNormalized"
- "_awbGains"
- "_awbParams"
- "_awbStatCfg"
- "_calcGlobalHistOnROI"
- "_calculateComboGainsAndNormalizedGainsFromAWBGains:awbComboGains:colorCalGains:"
- "_cameraInfo"
- "_cfaLayout"
- "_clippedTex"
- "_commandQueue"
- "_compressHighlight:"
- "_computeCurvesWoFaceBoost"
- "_computeHDRCurves"
- "_computeHDRCurvesWoFaceBoost"
- "_computeInputs"
- "_computeInputsMetadata"
- "_computeOutput"
- "_createShaders"
- "_cropRect"
- "_deepZoomOrigin"
- "_deepZoomRatio"
- "_dehaze:hazeValues:"
- "_device"
- "_digitalFlash"
- "_doAdaptiveFaceBiasScaler"
- "_doGlobalCCM"
- "_doHazeEstimation"
- "_downsizeFactor"
- "_driverInputMetadata"
- "_enableAdaptiveGain"
- "_enableAntiAliasing"
- "_enableCB"
- "_enableDualLTC"
- "_enableFATE"
- "_enableHiResLocalHistogram"
- "_enablePreLTMHazeCorrection"
- "_espressoNetwork"
- "_evmExpRatio"
- "_evtBkt"
- "_externalMemoryResource"
- "_faceAssistedSkinGainsToMatch"
- "_faceBiasScaler"
- "_faceBiasScalerMin"
- "_faceBiasThreshold"
- "_faceBiasThresholdMin"
- "_fallbackGains"
- "_firstPixel"
- "_flashLuxLevel"
- "_flashRatio"
- "_flickerConfidence"
- "_flickerDetectionIRRatio"
- "_flickerDetectionStatus"
- "_forceDisableHR"
- "_forceDisableLTMFaceBoost"
- "_forceDisableLTMFaceExposureRatio"
- "_forceDisableLTMHazeCorrection"
- "_forceHighlightCompressionForEveryFrame"
- "_forceUseBt709"
- "_globalFaceHistStat"
- "_globalHistStat"
- "_hazeConfig"
- "_hazeConfigured"
- "_hazeEstimation"
- "_hazeInternalBuffer"
- "_hazeROI"
- "_hazeValue"
- "_hazeValueForLTM"
- "_haze_threshold_divider"
- "_imageTex"
- "_inChromaTex"
- "_inLumaTex"
- "_inMetaData"
- "_inRGBAFloatTex"
- "_inRGBImageUInt16Tex"
- "_inputBufferRect"
- "_inputRGBTexture"
- "_inputTextureDownsampleRatio"
- "_inputTextureRect"
- "_inputTextureSize"
- "_isAdaptiveHighlightCompressionEnabled"
- "_isDigitalFlash"
- "_isHazeEstimationEnabled"
- "_isHighlightCompressionEnabled"
- "_isNominalStrobe"
- "_isOptimized:"
- "_isSIFR"
- "_ispDGainThreshold"
- "_ispRes"
- "_ledType"
- "_loadANSTNetwork"
- "_localHistStat"
- "_lscGainsTex"
- "_lscMaxGain"
- "_lscModulationWeight"
- "_ltmCompute"
- "_ltmDriver"
- "_ltmStats"
- "_lumaParams"
- "_maxHazePercentile"
- "_metadata"
- "_metalCommandQueue"
- "_min_display_black"
- "_minimumAdaptiveHC_SIFR"
- "_minimumRect"
- "_moduleConfig"
- "_numTilesX"
- "_numTilesY"
- "_optimizationLevel"
- "_optimized"
- "_outMetaData"
- "_outputMetadata"
- "_params"
- "_photometerAWBDebug_externalLux"
- "_pmLEDCalibData"
- "_preFlashLuxLevel"
- "_preFlashLuxLevelHigh"
- "_preFlashLuxLevelLow"
- "_prepareHighlightCompressionCurve"
- "_printDefaultsLTMparam"
- "_procHITHStat"
- "_processSkyMask:skyMaskWidth:skyMaskHeight:cropRectFromSourceDict:"
- "_purgeANSTNetwork"
- "_rawSensorHeight"
- "_rawSensorWidth"
- "_readDefaultsDehaze"
- "_readDefaultsLTMparam"
- "_readDefaultsMetalAllocator"
- "_regionOfInterestRectInBufferCoords"
- "_reluC1"
- "_reluC2"
- "_reluC3"
- "_reluC4"
- "_reluC5"
- "_sMetaData"
- "_secondaryCameraInfo"
- "_secondaryModuleConfig"
- "_sensorClockFreqHz"
- "_sensorSpaceToValidBufferSpaceTransform"
- "_skinMask"
- "_skipDemosaic"
- "_skyMask"
- "_sourceRect"
- "_sr_min"
- "_sr_pow"
- "_sr_sat"
- "_sr_var"
- "_threadgroupSize"
- "_thumbnailStat"
- "_thumbnailTexture"
- "_tileStatsROIRect"
- "_tuningParameters"
- "_undoHRGainDownRatio"
- "_updateHRGainDownRatioMetadata"
- "_validBufferRect"
- "_validRectInBufferCoords"
- "_validRectInSensorReadoutCoords"
- "_winRegionHeight"
- "_winRegionWidth"
- "addCompletedHandler:"
- "addEntriesFromDictionary:"
- "addLTMMetadataTo:curvesType:fromLTMOutput:statistics:driverInputMetadata:geometryData:"
- "allocInternalData"
- "allocateResources"
- "allocator"
- "anstInferenceDescriptor"
- "anstInputPixelBuffer"
- "anstInputTex"
- "anstModelConfig"
- "anstOutputPixelBuffer"
- "anstOutputPixelBuffer8"
- "anstOutputTex"
- "arrayWithCapacity:"
- "arrayWithObjects:"
- "assetPath"
- "autorelease"
- "awbComboGains"
- "awbComboGainsNormalized"
- "awbConfigLoad:to:"
- "awbGains"
- "awbSensorCalibrationsLoad:idealColorCalibrations:to:"
- "bindPixelBufferToMTL2DTexture:pixelFormat:usage:plane:"
- "blitCommandEncoder"
- "boolValue"
- "bundleForClass:"
- "bytes"
- "calcExposureRatio:"
- "calcGlobalHistOnROI"
- "calculateEIT:result:"
- "calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:"
- "calculateHITHStatistics:ltmGeometry:optimized:enableAntiAliasing:calcGlobalHistOnROI:toDriverInputMetadata:andProcHITHStat:enableFATE:"
- "calculateHazeValues:pixels:thresh:properties:"
- "calculateInternalAWBMetadataForMIWB:bGain:rSkinGain:bSkinGain:cct:internalMetadata:"
- "calculateNonComboGainsFromComboGains:awbAlgorithm:gains:"
- "calculateSTRBKeyFromWideCamera:moduleConfig:secondaryModuleConfig:"
- "calculateSTRBKeyFromWideCameraLatticeModel:moduleConfig:absoluteColorCalibrations:secondaryModuleConfig:secondaryAbsoluteColorCalibrations:"
- "cameraInfoByPortType"
- "cfaLayout"
- "class"
- "clippedTex"
- "cmi_boolValueForKey:defaultValue:found:"
- "cmi_cgRectForKey:defaultValue:found:"
- "cmi_doubleValueForKey:defaultValue:found:"
- "cmi_floatValueForKey:defaultValue:found:"
- "cmi_intValueForKey:defaultValue:found:"
- "cmi_intValueFromArrayWithKey:forIndex:defaultValue:found:"
- "cmi_simdFloat4ValueForKey:defaultValue:found:"
- "cmi_unsignedIntValueForKey:defaultValue:found:"
- "commandQueue"
- "commit"
- "compareAWBMetadata:withReference:"
- "compute"
- "computeCommandEncoder"
- "computeCurvesWoFaceBoost"
- "computeGain:withTargetRange:"
- "computeHDRCurves"
- "computeHDRCurvesWoFaceBoost"
- "computeInputParametersForImageWidth:calcGlobalHistOnROI:enableAntiAliasing:enableDualLTC:enableFATE:with:to:"
- "computeLTM:withMetadata:to:"
- "computeLtmComputeInput:withMetadata:to:computeInputMetadata:"
- "computePipelineStateFor:constants:"
- "configFaceMetadata:awbParams:"
- "configFallbackMetadata:"
- "configFlashRFCMetadata:cameraInfo:moduleConfig:"
- "configFlickerDetectionMetadata:moduleConfig:"
- "configPortTypeMetadata:"
- "configWindowsV2:metadata:tilesConfig:validRect:regionOfInterestRect:"
- "configWithModuleConfig:metadata:cameraInfo:awbParams:"
- "configure"
- "conformsToProtocol:"
- "contents"
- "copy"
- "copyWithZone:"
- "count"
- "createIntermediateRGBAMetalTexture:width:height:"
- "createLTMInTextureFromLuma:chroma:"
- "createLTMInTextureFromRGBAFloatTex:undoScaleDown:"
- "createLTMMetadataFromLTMOutput:statistics:driverInputMetadata:geometryData:"
- "createShaders"
- "createShaders:"
- "cropRect"
- "currentHandler"
- "cvErr == kCVReturnSuccess"
- "dataWithBytes:length:"
- "dataWithLength:"
- "dealloc"
- "debugDescription"
- "deepZoomOrigin"
- "deepZoomRatio"
- "defaultConfigurationForVersion:withError:"
- "desc"
- "description"
- "descriptorWithConfiguration:error:"
- "device"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "digitalFlash"
- "dispatchThreadgroups:threadsPerThreadgroup:"
- "dispatchThreads:threadsPerThreadgroup:"
- "doAWBConfigLoad:to:"
- "doAdaptiveFaceBiasScaler"
- "doGlobalCCM"
- "doHazeEstimation"
- "doubleValue"
- "downsizeFactor"
- "enableAntiAliasing"
- "encodeLTMStatisticsCalculationOptimized:params:globalHistogram:globalFaceHistogram:localHistogram:thumbnail:"
- "encodeLTMStatisticsCalculationPrecise:paramsGlobalHist:globalHistogram:localHistogram:thumbnail:"
- "encodeSetFileIDForModuleConfig:setFileID:"
- "endEncoding"
- "estimateHaze:"
- "evmExpRatio"
- "evtBkt"
- "externalMemoryDescriptorForConfiguration:"
- "externalMemoryResource"
- "extractAWBMetadataFromMetadata:validBufferRect:ltmGeometryData:toDriverInput:"
- "extractAWBMetadataFromMetadata:validBufferRect:toDriverInput:"
- "extractAWBMetadataFromRawMetadata:toDriverInput:"
- "extractCCMFromMetadata:toDriverInput:"
- "extractFrom:toDriverInput:ltmGeometry:"
- "extractFromRawMetadata:toDriverInput:"
- "extractHRGainDownRatioFrom:"
- "extractRectanglesFrom:inputBufferRect:validBufferRect:ltmGeometry:"
- "f"
- "f16@0:8"
- "f24@0:8@\"NSDictionary\"16"
- "f24@0:8@16"
- "f24@0:8r^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16"
- "fillBuffer:range:value:"
- "fillProcHITHStat:with:"
- "finishCalculateHITHStatistics:optimized:"
- "finishProcessing"
- "firstPixel"
- "floatValue"
- "generateLinearRGBATexture:"
- "getBytes:bytesPerRow:fromRegion:mipmapLevel:"
- "getColorCalibrationsUsingIdealColorCalbrations:absoluteColorCalibrations:colorCalibrationsOut:awbConfig:"
- "getHITHStat"
- "getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:"
- "getInternalAWBMetadataForMIWB:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:platformID:"
- "getLTMTuningFromTuningParams:from:"
- "getTileStatsRegion:validBufferRect:ltmGeometryData:toDriverInput:"
- "getTileStatsRegion:validBufferRect:toDriverInput:"
- "getTileStatsRegionWithMetadata:cropRectLTMInCoords:ltmInDownsamplingRatio:tileStatsRegionLTMInCoordsDictOut:"
- "globalFaceHistStat"
- "globalHistStat"
- "handleFailureInFunction:file:lineNumber:description:"
- "hash"
- "hazeEstimation"
- "hazeProperties"
- "hazeROI"
- "hazeValue"
- "hazeValueForLTM"
- "haze_estimation_thumbnail_tex"
- "height"
- "i120@0:8@16@24@32@40@48@56^{?=BiiiiSS}64@72^@80@88^@96@104^I112"
- "i16@0:8"
- "i20@0:8I16"
- "i20@0:8i16"
- "i24@0:8@\"NSDictionary\"16"
- "i24@0:8@16"
- "i24@0:8^16"
- "i28@0:8^f16f24"
- "i28@0:8^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16B24"
- "i32@0:8@16@24"
- "i32@0:8@16^I24"
- "i32@0:8@16^Q24"
- "i32@0:8@16^{CAWBAFE=^^?i^{CDualLEDsWhitePointProjector}{?=[9f][9f][6{?=fffff}]{?=[6f][6f][6f][6f][6f][6f]}[3{?=ff}][3{?=ff}][3{?=ff}][3{?=ff}]BB}^{CAWBAFEFDAssist}^{CAWBAFEPhotometerAssistPenrose}^{sPhotometerAWBMetadata}^{_FE_3A_Stats_H15}^{_FE_3A_Stats_H15}^{_TILE_Stat_Elem}^{_AEAWB_Stat_Elem}^{_HighResAWBAE_Stat_Elem}^I{sFEStatCSCConfig=[9s][9s][3s][3S][3S][2S]C}{sFEStatColorHistConfig=[15S][16C]SISI}ISSSBI[3I][3I][3[3i]][3[3i]]IBBBIIi[3S][3S]IffSfffffff{sAWBInternalParams=SSBBBffffffffffffffffffffI[1024I]}B{sAWBDigitalFlashSkyParams=iBffffffff}iBfff[1024I][1024I][6[4s]][3S][9s][2S][2S][13S][3S][32S]S*[1024C][6[1024C]][6s]CSSSSfSSSSB[3I]fSiBi[30[2s]]I[8[3S]]I[6[9s]]{sCSensorCalGain=SSSS}SSSSBI[4I]II{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}ffBBBBBfii[3I]^{fdAWBMetaData}[150[4S]]IBB{sWPStableZoneControlTable={sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}}BBCCQSS^{sMetaData}[3S]iBi[2f]f[30[2s]][6I][6I]B[6S]S[32S]B[192f]{sAWBTimelapseParams=BBI{sAWBTimelapseSmoothingState=ff[3f][3f]fffSB}}f{sCIspCmdChColorCalIdealSet=ISS(?=I{sCIspControllerCmdHdrChInfo=b16b15b1})SSSS}Bi{sUnagiParams=i}C}24"
- "i32@0:8^{LTMTuning=ffffffffffffffffffffffffffff}16@24"
- "i32@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16@24"
- "i40@0:8@16@24@32"
- "i40@0:8@16@24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32"
- "i40@0:8^v16i24i28@32"
- "i40@0:8^{?=i(?={?=ffff}{?=ff}{?=ff})}16@24@32"
- "i40@0:8r^{sLtmComputeInput=[3072f][64f][1024f][48f][48f][64f][64f][65f][48f]ffffffffffffS[9f][192f]fffBB[48f]f}16r^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBiBif}C[6{LTMTuning=ffffffffffffffffffffffffffff}]B}24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}32"
- "i40@0:8r^{sLtmComputeInput_SOFTISP={sLtmComputeInput=ffff[12288f][256f][1024f][64f][48f][48f][256f][256f][256f][48f][192f][48f]fffffffffffffS[9f][192f]fff[192f][768f][192f]fff}BBf}16r^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}32"
- "i44@0:8[3I]16I24^{SensorConfigAWBParams={sCSensorCalIdeal=SSSS}{sCSensorCalAbs=SSSS}{sCSensorCalBias=SSSS}{sCSensorCalGain=SSSS}II{sCameraColorConfig=[9s][9s][2s][2I]S[6[9s]][8[3S]][30[2s]]}}28^{sSlaveCameraAWBParam=SSI[3I][3I][3[3i]]BQfffBBf{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}}36"
- "i44@0:8f16f20f24f28f32@36"
- "i48@0:8@16@24@32@40"
- "i48@0:8@16@24@32^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}40"
- "i48@0:8@16@24^@32@40"
- "i48@0:8r^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16r^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24^{sLtmComputeInput=[3072f][64f][1024f][48f][48f][64f][64f][65f][48f]ffffffffffffS[9f][192f]fffBB[48f]f}32^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBiBif}C[6{LTMTuning=ffffffffffffffffffffffffffff}]B}40"
- "i48@0:8r^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16r^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24^{sLtmComputeInput_SOFTISP={sLtmComputeInput=ffff[12288f][256f][1024f][64f][48f][48f][256f][256f][256f][48f][192f][48f]fffffffffffffS[9f][192f]fff[192f][768f][192f]fff}BBf}32^{sLtmComputeMeta_SOFTISP={sLtmComputeMeta=BBBBBBiCCB}[6{LTMTuning=ffffffffffffffffffffffffffff}]BCB}40"
- "i52@0:8{?=III}16{?=III}28{?=III}40"
- "i56@0:8@16B24B28B32B36^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}40^{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]B}{?=IIIIIIIIiBI}}48"
- "i56@0:8@16^{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]B}{?=IIIIIIIIiBI}}24@32@40@48"
- "i56@0:8^{?=BB[2i]iiii}16@24@32@40@48"
- "i56@0:8^{?=i(?={?=ffff}{?=ff}{?=ff})}16@24@32@40@48"
- "i60@0:8@16@24@32@40I48^{SensorConfigAWBParams={sCSensorCalIdeal=SSSS}{sCSensorCalAbs=SSSS}{sCSensorCalBias=SSSS}{sCSensorCalGain=SSSS}II{sCameraColorConfig=[9s][9s][2s][2I]S[6[9s]][8[3S]][30[2s]]}}52"
- "i60@0:8@16@24B32B36B40^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}44^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}52"
- "i60@0:8@16@24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32B40B44B48^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}52"
- "i64@0:8@16@24@32@40@48@56"
- "i64@0:8@16@24B32B36B40^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}44^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}52B60"
- "i64@0:8@16^{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]B}{?=IIIIIIIIiBI}}24@32@40@48@56"
- "i68@0:8@16@24@32@40@48@56i64"
- "i68@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24f56^@60"
- "i72@0:8@16@24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32B40B44B48B52B56B60^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}64"
- "i92@0:8@16@24@32@40@48@56f64f68I72^f76^f84"
- "imageTex"
- "inChromaTex"
- "inLumaTex"
- "inMetaData"
- "inRGBAFloatTex"
- "inRGBImageUInt16Tex"
- "init"
- "initTuningParameters:"
- "initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:"
- "initWith:HITH:geometryData:statsObj:optimized:digitalFlash:computeHDRCurves:computeCurvesWoFaceBoost:computeHDRCurvesWoFaceBoost:enhancedLocalHistogram:enableCB:enableFATE:"
- "initWithAWBObject:"
- "initWithCommandQueue:"
- "initWithDevice:allocatorType:"
- "initWithInputTextureWidth:height:"
- "initWithMetalContext:"
- "initWithMetalContext:platformID:"
- "initWithbundle:andOptionalCommandQueue:"
- "initialize"
- "inputBufferRect"
- "inputRGBTexture"
- "inputTextureDownsampleRatio"
- "inputTextureSize"
- "intValue"
- "internalSetupWithFWPlatformID:"
- "isAdaptiveHighlightCompressionEnabled"
- "isEqual:"
- "isEqualToString:"
- "isHighlightCompressionEnabled"
- "isKindOfClass:"
- "isLocalCCMEnabled:"
- "isMemberOfClass:"
- "isProxy"
- "isSIFR"
- "ispRes"
- "length"
- "localHistStat"
- "lscGainsTex"
- "lscMaxGain"
- "lscModulationWeight"
- "ltmParams"
- "maxHazePercentile"
- "maxTotalThreadsPerThreadgroup"
- "memSize"
- "metalCommandQueue"
- "mutableBytes"
- "mutableCopy"
- "newBufferDescriptor"
- "newBufferWithDescriptor:"
- "newBufferWithLength:options:"
- "newTextureDescriptor"
- "newTextureWithDescriptor:"
- "numTilesX"
- "numTilesY"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedShort:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "optimizationLevel"
- "outMetaData"
- "outputMetadata"
- "path"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pixelFormat"
- "pointerValue"
- "populateSlaveConfigWithModuleConfigIfColorMatchingModelExistsInPrimaryAWBConfig:secondaryAWBConfig:secondaryIdealColorCals:secondaryAbsoluteColorCals:secondarySetFileID:secondarySensorConfig:"
- "prepareThumbnail"
- "prepareToProcess:"
- "prewarm"
- "prewarmShaders"
- "prewarmWithTuningParameters:"
- "process"
- "process:clipped:lscGainsTex:validRectInBufferCoords:validRectInSensorReadoutCoords:awbStatsBuffer:awbTileStatsConfig:anstSkinMask:anstSkinMaskData:skyMaskTex:skyMaskData:regionOfInterestRectInBufferCoords:downsizeFactor:"
- "purgeResources"
- "rangeOfString:"
- "rawSensorHeight"
- "rawSensorWidth"
- "regionOfInterestRectInBufferCoords"
- "release"
- "releaseTextures"
- "removeAllObjects"
- "removeObjectForKey:"
- "replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:"
- "reset"
- "resetState"
- "respondsToSelector:"
- "result"
- "retain"
- "retainCount"
- "rewriteAntiAliasingCoefficients:"
- "run"
- "scanHexInt:"
- "scannerWithString:"
- "secondaryCameraInfo"
- "secondaryModuleConfig"
- "sensorClockFrequency"
- "sensorSpaceToValidBufferSpaceTransform"
- "setAdaptiveHCSlope:"
- "setAllocator:"
- "setArrayLength:"
- "setAwbComboGains:"
- "setAwbComboGainsNormalized:"
- "setAwbGains:"
- "setBuffer:offset:atIndex:"
- "setBytes:length:atIndex:"
- "setCalcGlobalHistOnROI:"
- "setCameraInfo:"
- "setCameraInfoByPortType:"
- "setCfaLayout:"
- "setClippedTex:"
- "setComputeCurvesWoFaceBoost:"
- "setComputeHDRCurves:"
- "setComputeHDRCurvesWoFaceBoost:"
- "setComputePipelineState:"
- "setCropRect:sourceRect:"
- "setDeepZoomOrigin:"
- "setDeepZoomRatio:"
- "setDehazeTuningParamsFrom:"
- "setDepth:"
- "setDigitalFlash:"
- "setDoAdaptiveFaceBiasScaler:"
- "setDoGlobalCCM:"
- "setDoHazeEstimation:"
- "setDownsizeFactor:"
- "setEnableAntiAliasing:"
- "setEvmExpRatio:"
- "setEvtBkt:"
- "setExternalMemoryResource:"
- "setFaceAssistedBehaviorMode:"
- "setFaceAssistedSkinGainsToMatch:"
- "setFirstPixel:"
- "setHazeEstimation:"
- "setHazeProperties:"
- "setHazeROI:"
- "setHazeValue:"
- "setHazeValueForLTM:"
- "setHaze_threshold_divider:"
- "setHeight:"
- "setImageTex:"
- "setImageblockWidth:height:"
- "setInChromaTex:"
- "setInLumaTex:"
- "setInMetaData:"
- "setInRGBAFloatTex:"
- "setInRGBImageUInt16Tex:"
- "setInputBufferRect:"
- "setInputRGBTexture:"
- "setInputTextureDownsampleRatio:"
- "setIsAdaptiveHighlightCompressionEnabled:"
- "setIsHighlightCompressionEnabled:"
- "setIsSIFR:"
- "setIspDGainThreshold:"
- "setIspRes:"
- "setLTMComputeTuningParams:from:"
- "setLTMTuningParamsFrom:"
- "setLabel:"
- "setLength:"
- "setLscGainsTex:"
- "setLscMaxGain:"
- "setLscModulationWeight:"
- "setMaxHazePercentile:"
- "setMemSize:"
- "setMetadata:"
- "setMetalCommandQueue:"
- "setMin_display_black:"
- "setMinimumAdaptiveHC_SIFR:"
- "setModuleConfig:"
- "setObject:atIndexedSubscript:"
- "setObject:forKeyedSubscript:"
- "setOptimizationLevel:"
- "setOutMetaData:"
- "setOutputMetadata:"
- "setPixelFormat:"
- "setRawSensorHeight:"
- "setRawSensorWidth:"
- "setRegionOfInterestRectInBufferCoords:"
- "setReluC1:"
- "setReluC2:"
- "setReluC3:"
- "setReluC4:"
- "setReluC5:"
- "setResourceOptions:"
- "setScanLocation:"
- "setSecondaryCameraInfo:"
- "setSecondaryModuleConfig:"
- "setSensorSpaceToValidBufferSpaceTransform:"
- "setSkinMask:"
- "setSkipDemosaic:"
- "setSkyMask:"
- "setSr_min:"
- "setSr_pow:"
- "setSr_sat:"
- "setSr_var:"
- "setStats:"
- "setStorageMode:"
- "setTexture:atIndex:"
- "setTextureType:"
- "setTileStatsROIRect:"
- "setTuningParameters:"
- "setUndoHRGainDownRatio:"
- "setUsage:"
- "setValidBufferRect:"
- "setValidRectInBufferCoords:"
- "setValidRectInSensorReadoutCoords:"
- "setWidth:"
- "setWinRegionHeight:"
- "setWinRegionWidth:"
- "setWireMemory:"
- "setup"
- "setupWithDescriptor:"
- "setupWithDescriptor:allocatorBackend:"
- "skinMask"
- "skipDemosaic"
- "skyMask"
- "sortedArrayUsingComparator:"
- "sourceRect"
- "startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:enhancedLocalHistogram:enableDualLTC:enableFATE:outputProcHITHStat:"
- "startCalculateHITHStatistics:ltmGeometry:inputDriverMetadata:optimized:enableAntiAliasing:calcGlobalHistOnROI:outputProcHITHStat:"
- "stats"
- "status"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "superclass"
- "supportsExternalMemoryResource"
- "td"
- "textureType"
- "threadExecutionWidth"
- "thumbnailStat"
- "tileStatsROIRect"
- "translateAWBGainsToSecondaryChannelID:secondaryChannelID:secondaryConfig:secondaryAWBParams:"
- "translateAWBGainsToSecondaryPortType:cameraInfo:metadata:validRect:secondaryModuleConfig:secondaryCameraInfo:primaryRGain:primaryBGain:secondaryChannelID:secondaryRGain:secondaryBGain:"
- "tuningParameters"
- "unagiUtils"
- "undoHRGainDownRatio"
- "unsignedCharValue"
- "unsignedIntValue"
- "unsignedShortValue"
- "usedSizeAll"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@\"<MTLCommandQueue>\"16"
- "v24@0:8@\"<MTLTexture>\"16"
- "v24@0:8@\"CMIExternalMemoryResource\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSMutableDictionary\"16"
- "v24@0:8@\"NSNumber\"16"
- "v24@0:8@16"
- "v24@0:8^I16"
- "v28@0:8{?=III}16"
- "v32@0:816"
- "v32@0:8@16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24"
- "v32@0:8^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}16^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}24"
- "v32@0:8{CGPoint=dd}16"
- "v32@0:8{SourceROI=IIII}16"
- "v36@0:8@16i24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}28"
- "v380@0:8^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}16{?={?=I[3I][3I]I}{?=BSIIII[4I][4f]}{?=BSIIII[4I][4f]}{?=BIIIIIIIIIIIIIIBIB[25I]B}{?=IIIIIIIIiBI}}24"
- "v40@0:8@16^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}24@32"
- "v40@0:8@16^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}24^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}32"
- "v40@0:8@16i24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}28I36"
- "v40@0:8[3I]16^{CAWBAFEH14=^^?i^{CDualLEDsWhitePointProjector}{?=[9f][9f][6{?=fffff}]{?=[6f][6f][6f][6f][6f][6f]}[3{?=ff}][3{?=ff}][3{?=ff}][3{?=ff}]BB}^{CAWBAFEFDAssist}^{CAWBAFEPhotometerAssistPenrose}^{sPhotometerAWBMetadata}^{_FE_3A_Stats_H15}^{_FE_3A_Stats_H15}^{_TILE_Stat_Elem}^{_AEAWB_Stat_Elem}^{_HighResAWBAE_Stat_Elem}^I{sFEStatCSCConfig=[9s][9s][3s][3S][3S][2S]C}{sFEStatColorHistConfig=[15S][16C]SISI}ISSSBI[3I][3I][3[3i]][3[3i]]IBBBIIi[3S][3S]IffSfffffff{sAWBInternalParams=SSBBBffffffffffffffffffffI[1024I]}B{sAWBDigitalFlashSkyParams=iBffffffff}iBfff[1024I][1024I][6[4s]][3S][9s][2S][2S][13S][3S][32S]S*[1024C][6[1024C]][6s]CSSSSfSSSSB[3I]fSiBi[30[2s]]I[8[3S]]I[6[9s]]{sCSensorCalGain=SSSS}SSSSBI[4I]II{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}ffBBBBBfii[3I]^{fdAWBMetaData}[150[4S]]IBB{sWPStableZoneControlTable={sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}{sTuningCurvePoint=I[8I][8I]}}BBCCQSS^{sMetaData}[3S]iBi[2f]f[30[2s]][6I][6I]B[6S]S[32S]B[192f]{sAWBTimelapseParams=BBI{sAWBTimelapseSmoothingState=ff[3f][3f]fffSB}}f{sCIspCmdChColorCalIdealSet=ISS(?=I{sCIspControllerCmdHdrChInfo=b16b15b1})SSSS}Bi{sUnagiParams=i}CBI[4{_sSlaveCameraListColorMatchingModel=Ii{?=iii}{?=iii}{?=C[2[81f]]}}][32f]}24[3I]32"
- "v48@0:8@16@24@32@40"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v56@0:8@16^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}24^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}32@40^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}48"
- "v56@0:8@16i24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}28^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}36@44B52"
- "v60@0:8@16i24^{sLtmComputeOutput=[3120f][65f][257f][257f][5184f][257f]fQfb1b1b1b1b1b3}28^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}36^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}44@52"
- "v60@0:8@16i24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}28^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}36@44B52I56"
- "v60@0:8@16i24^{sLtmComputeOutput=[49344f][257f][257f][257f]i[5184f][257f]fffb1b1b1b1b1b3[49344f]}28^{sCLRProcHITHStat_SOFTISP=I[6S]SSIISSSSSSSSCSISI^vII^vII^vII^vIIBIIIII}36^{sRefDriverInputs_SOFTISP=BSI(uBTColorEntry16=S{uBT88=CC})IffSSSSIfSBCCI(uBTColorEntry16=S{uBT88=CC})fBCBB{sBTRect=iiII}{sBTRect=iiII}[512S]f{sBTRect=iiII}{sAWBColorCorrectionMatrix_local=[9(uBTColorEntry16=S{uBT88=CC})]}B{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}{sBTRGGB16=(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})(uBTColorEntry16=S{uBT88=CC})}IC{sFaceInfo_SOFTISP=[10{sCIspFDRect=iiII}]II}BiBBfBBBB[6{LTMTuning=ffffffffffffffffffffffffffff}]BfCC}44@52"
- "v64@0:8{CGAffineTransform=dddddd}16"
- "v80@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48"
- "validBufferRect"
- "validRectInBufferCoords"
- "validRectInSensorReadoutCoords"
- "valueForKey:"
- "valueWithPointer:"
- "waitUntilCompleted"
- "width"
- "winRegionHeight"
- "winRegionWidth"
- "zone"
- "{?=\"LumShift\"I\"CoeffAvgY\"[3I]\"CoeffMaxY\"[3I]\"AvgYOffset\"I}"
- "{?=\"layout\"i\"firstPix\"C\"greenAverage\"C\"downsizeRatio\"C\"ispDGain\"f\"ccm\"{?=\"coeff\"{?=\"columns\"[3]}\"min\"\"max\"\"offsetIn\"\"offsetOut\"}\"gam\"{?=\"lut\"[257S]\"gammaOffsetIn\"\"gammaOffsetOut\"\"offsetIn\"S\"offsetOut\"S\"po2CfgMode\"i\"po2CfgExpand\"B\"po2CfgDenseLeft\"{?=\"flipOp\"B\"offOp\"B\"symmetric\"B\"maxCode\"i\"pivot1\"i\"lutLen\"S\"startExp\"S\"spacingStart\"S\"numIntervalArray\"[16S]\"log2NumIntervalArrayAdj\"[16S]}}\"csc\"{?=\"lin3x3\"{?=\"coeff\"{?=\"columns\"[3]}\"min\"\"max\"\"offsetIn\"\"offsetOut\"}\"scale\"}\"csc2\"{?=\"lin3x3\"{?=\"coeff\"{?=\"columns\"[3]}\"min\"\"max\"\"offsetIn\"\"offsetOut\"}\"scale\"}\"colorHist\"{?=\"enable\"B\"countClipEn\"B\"startX\"S\"startY\"S\"endX\"S\"endY\"S\"offsetC1\"f\"offsetC2\"f\"scaleC1\"f\"scaleC2\"f\"count\"[16S]\"yThd\"[16S]\"debiasGain\"\"debiasMax\"\"debiasMin\"\"debiasOffset\"}\"pixFilt\"[2{?=\"condSel\"C\"statSel\"C\"countClipEn\"B\"Ymin\"i\"Ymax\"i\"C1min\"i\"C1max\"i\"C2min\"i\"C2max\"i\"distMax\"I\"offset\"i\"C1delta\"i\"C2delta\"i}]\"debiasCfg\"[2{?=\"offset\"\"gain\"}]\"fastLSCCfg\"{AWBFastLSCConfig=\"enabled\"B\"gridWidth\"S\"gridHeight\"S\"gridMaxGain\"f\"modulationWeight\"f\"gridIntervalReciprocal\"\"yOffset\"(?=\"vec\"\"\"{?=\"gr\"S\"r\"S\"b\"S\"gb\"S})\"xCropOffset\"S\"yCropOffset\"S}\"windows\"[2{?=\"enable\"B\"bitDepth\"B\"pfSel\"[2i]\"startX\"i\"startY\"i\"endX\"i\"endY\"i}]\"tiles\"{?=\"bitDepth\"B\"startX\"i\"startY\"i\"endX\"i\"endY\"i\"horzInt\"S\"vertInt\"S}\"linearRGBToANSTInputCfg\"{AWBLinearRGBToANSTInputConfig=\"awbGains\"\"ccm\"{?=\"columns\"[3]}\"gtcRatio\"[257S]\"gtcFinal\"[257S]\"ltmHardGain\"f}\"regionOfInterestRect\"{?=\"startX\"S\"startY\"S\"endX\"S\"endY\"S}\"skipDemosaic\"B\"digitalFlashBehaviorMode\"i}"
- "{?=\"luma\"{?=\"LumShift\"I\"CoeffAvgY\"[3I]\"CoeffMaxY\"[3I]\"AvgYOffset\"I}\"globalHist\"{?=\"Enable\"B\"YHistSel\"S\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"Offset\"[4I]\"Scale\"[4f]}\"globalFaceHist\"{?=\"Enable\"B\"YHistSel\"S\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"Offset\"[4I]\"Scale\"[4f]}\"localHist\"{?=\"Enable\"B\"SelInput\"I\"LocalHistShift\"I\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"StrideX\"I\"StrideY\"I\"BlockSizeX\"I\"BlockSizeY\"I\"Offset\"I\"Scale\"I\"ThreLo\"I\"ThreHi\"I\"enableAntiAliasing\"B\"SubBin\"I\"ClipValidIdx\"B\"HistCoeff\"[25I]\"enableHiResLocalHistogram\"B}\"thumbnail\"{?=\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I\"BlockSizeX\"I\"BlockSizeY\"I\"OffsetX\"I\"OffsetY\"I\"genMethod\"i\"portraitOrientated\"B\"ThumbAvgRecipNumPix\"I}}"
- "{?=\"plan\"^v\"network_index\"i}"
- "{?=\"rGain\"I\"gGain\"I\"bGain\"I}"
- "{?=\"validAWBData\"B\"awbRGain\"@\"NSNumber\"\"awbGGain\"@\"NSNumber\"\"awbBGain\"@\"NSNumber\"\"awbComboRGain\"@\"NSNumber\"\"awbComboGGain\"@\"NSNumber\"\"awbComboBGain\"@\"NSNumber\"}"
- "{?=\"width\"Q\"height\"Q\"depth\"Q}"
- "{?=III}16@0:8"
- "{CGAffineTransform=\"a\"d\"b\"d\"c\"d\"d\"d\"tx\"d\"ty\"d}"
- "{CGAffineTransform=dddddd}16@0:8"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{HazeConfig=\"thumbnailSize\"}"
- "{SourceROI=\"StartX\"I\"StartY\"I\"EndX\"I\"EndY\"I}"
- "{SourceROI=IIII}16@0:8"
- "{sCLRProcHITHStat_SOFTISP=\"thumbnailWindow\"I\"thumbnailEnable\"[6S]\"thumbnailDownsampleX\"S\"thumbnailDownsampleY\"S\"thumbnailTotal\"I\"localHistWindow\"I\"localHistEnable\"S\"localHistBinSize\"S\"localHistBlockSizeX\"S\"localHistBlockSizeY\"S\"localHistStrideX\"S\"localHistStrideY\"S\"localHistNumHorBlocks\"S\"localHistNumVerBlocks\"S\"localHistCountBitShift\"C\"globalHistEnable\"S\"globalHistWindow\"I\"globalFaceHistEnable\"S\"globalFaceHistWindow\"I\"thumbnailStat\"^v\"thumbnailOffset\"I\"thumbnailStatSize\"I\"localHistStat\"^v\"localHistOffset\"I\"localHistStatSize\"I\"globalHistStat\"^v\"globalHistOffset\"I\"globalHistStatSize\"I\"globalFaceHistStat\"^v\"globalFaceHistOffset\"I\"globalFaceHistStatSize\"I\"calculatedOnPortraitOrientation\"B\"gridOriginX\"I\"gridOriginY\"I\"localHistogramOriginalTilePixelCount\"I\"localHistLowThreshold\"I\"localHistHighThreshold\"I}"
- "{sLtmComputeInput=\"localHist\"[3072f]\"averageLocalHist\"[64f]\"globalHist\"[1024f]\"tMaxArray\"[48f]\"nLumArray\"[48f]\"thumbnailHist\"[64f]\"thumbnailHistEV0\"[64f]\"thumbnailLumaHist\"[65f]\"faceWeightForTone\"[48f]\"sceneLux\"f\"bin0Ratio\"f\"pixelCountRatio\"f\"exposureRatio\"f\"exposureBias\"f\"preBiasExposureRatio\"f\"faceExposureRatio\"f\"darkExposureRatio\"f\"luminanceRatio\"f\"flareScale\"f\"rGainRatio\"f\"bGainRatio\"f\"gamutSizeIndex\"S\"ccm\"[9f]\"ccmWeights\"[192f]\"ccmMixFactor\"f\"eit\"f\"darkEit\"f\"LTMHazeCorrectionOff\"B\"useBt709\"B\"ltcGridScaleLogLumaThumb\"[48f]\"faceBiasScaler\"f}"
- "{sLtmComputeInput_SOFTISP=\"ltmComputeInput\"{sLtmComputeInput=\"rotationMagnitude\"f\"rotationMagnitudeDeltaIIR\"f\"rotationMagnitudeDeltaFiltered\"f\"thumbHistBlendingWeight\"f\"localHist\"[12288f]\"averageLocalHist\"[256f]\"globalHist\"[1024f]\"globalHist2\"[64f]\"tMaxArray\"[48f]\"nLumArray\"[48f]\"thumbnailHist\"[256f]\"thumbnailHistEV0\"[256f]\"thumbnailLumaHist\"[256f]\"faceWeightForTone\"[48f]\"fmapHFF\"[192f]\"faceWeightForHistBlend\"[48f]\"faceFraction\"f\"sceneLux\"f\"bin0Ratio\"f\"pixelCountRatio\"f\"exposureRatio\"f\"exposureBias\"f\"preBiasExposureRatio\"f\"faceExposureRatio\"f\"darkExposureRatio\"f\"luminanceRatio\"f\"flareScale\"f\"rGainRatio\"f\"bGainRatio\"f\"gamutSizeIndex\"S\"ccm\"[9f]\"ccmWeights\"[192f]\"ccmMixFactor\"f\"eit\"f\"darkEit\"f\"ltcGridScaleLogLumaThumb\"[192f]\"blendingMaskInputTh\"[768f]\"CBBrightMap\"[192f]\"CBLowlightDampWeight\"f\"faceBiasScaler\"f\"HFFDampWeight\"f}\"LTMHazeCorrectionOff\"B\"useBt709\"B\"totalGain\"f}"
- "{sLtmComputeMeta_SOFTISP=\"ltmComputeMeta\"{sLtmComputeMeta=\"useLinearLTCs\"B\"useSpatialCCM\"B\"useGlobalCCM\"B\"useDigitalFlash\"B\"useFlash\"B\"bSoftGainOnly\"B\"gammaCurve\"i\"faceLTMVer\"C\"CBVer\"C\"updateMixLUT\"B}\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"darkSceneLuxThreshold\"\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B\"channel\"C\"enableHiResLocalHistogram\"B}"
- "{sLtmComputeMeta_SOFTISP=\"ltmComputeMeta\"{sLtmComputeMeta=\"useLinearLTCs\"B\"useSpatialCCM\"B\"useGlobalCCM\"B\"useDigitalFlash\"B\"useFlash\"B\"gammaCurve\"i\"updateMixLUT\"B\"levelSmoothNumPasses\"i\"levelSmoothCenterWeight\"f}\"channel\"C\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"darkSceneLuxThreshold\"\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B}"
- "{sLtmComputeOutput=\"LTC\"[3120f]\"averageLTC\"[65f]\"globalLUT\"[257f]\"rgbToneCurve\"[257f]\"spatialCCM\"[5184f]\"WMixLUT\"[257f]\"midLuminance\"f\"eit\"Q\"encodedExpRatio\"f\"bWMixLUTUpdated\"b1\"bCCMUpdated\"b1\"bLTMUpdated\"b1\"bGlobalLUTUpdated\"b1\"bRgbToneCurveUpdated\"b1\"rsvd\"b3}"
- "{sLtmComputeOutput=\"LTC\"[49344f]\"averageLTC\"[257f]\"globalLUT\"[257f]\"rgbToneCurve\"[257f]\"rgbToneCurveInputMode\"i\"spatialCCM\"[5184f]\"WMixLUT\"[257f]\"midLuminance\"f\"eit\"f\"encodedExpRatio\"f\"bWMixLUTUpdated\"b1\"bCCMUpdated\"b1\"bLTMUpdated\"b1\"bGlobalLUTUpdated\"b1\"bRgbToneCurveUpdated\"b1\"rsvd\"b3\"LTCBright\"[49344f]}"
- "{sMetaData=\"metaValid\"B\"frameCount\"I\"timeStamp\"Q\"readOutTime\"I\"sensorHeight\"I\"sensorWidth\"I\"sensorArrayOutputRect\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"validDataRegion\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"blackLevel\"S\"rangeExpansionGain\"S\"frameRate\"I\"slotStep\"f\"channel\"C\"masterCam\"C\"masterCamPreview\"C\"previewMasterCh\"C\"pendingPreviewMasterCh\"Q\"binW\"C\"binH\"C\"maxLSgainUnadjusted\"I\"flash\"{sFlashMetaData=\"gStr\"I\"pT\"S\"flashCaptureCount\"S\"flashCapture\"C\"Ynl_str\"I\"Yn_str\"I\"ExpAdjRatio\"I\"flashStatusAE\"i\"flashStatusAWB\"i\"strobeStatus\"i\"flashCaptureSequence\"C\"bMultiCam\"B\"isNominalStrobe\"f\"ratio\"f\"ledType\"i\"pmLEDCalibData\"{sPerModuleLEDCalibData=\"version\"C\"isvalid\"C\"programID\"C\"cw_rg\"f\"cw_bg\"f\"ww_rg\"f\"ww_bg\"f\"ledWidePtrn_rg\"f\"ledWidePtrn_bg\"f\"ledSWidePtrn_rg\"f\"ledSWidePtrn_bg\"f\"ledTelePtrn_rg\"f\"ledTelePtrn_bg\"f\"strb_rg\"f\"strb_bg\"f}\"flashAuxFrameType\"I\"dualProcessFlashType\"i\"ltmSceneLux\"i\"internalFlashEn\"B\"externalFlash\"B}\"ae\"{sAEMetaData=\"request\"I\"status\"I\"counter\"S\"exposure\"Q\"exposureTime\"I\"pixelRate\"I\"gainAnal\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigiSensor\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigi\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigiAE\"S\"interGainAnal\"S\"interEIT\"Q\"vFrameSize\"I\"totalVMin\"I\"minVSizeForBracketing\"I\"flickerFreq\"I\"sceneBrightnessForLux\"I\"luxLevel\"f\"luxLevelLow\"S\"luxLevelHigh\"S\"preFlashLuxLevel\"S\"preFlashLuxLevelLow\"S\"preFlashLuxLevelHigh\"S\"inverseBinningGainFactor\"S\"maxHighAGC\"S\"flashAEDoneFlag\"C\"contextSwitchConfig\"I\"contextSwitchCompleted\"B\"sessionType\"I\"sessionState\"I\"bracketingMode\"C\"bracketingOisType\"C\"bracketingCapture\"C\"bracketingCaptureCount\"C\"bracketingCaptureFirst\"C\"bracketingCaptureLast\"C\"preBracketing\"C\"bracketingExpRatio\"I\"focusPos\"s\"bracketingCaptureDummy\"C\"bracketingCaptureDummyNeeded\"C\"flash\"{sAEFlashMetaData=\"Ynl_str\"I\"Yn_str\"I\"Yavg\"I\"Ytarget\"I\"ExpAdjRatio\"I\"slowSync\"B\"slowSyncFlashOnTime\"I\"exposureTime\"I\"SSFLeadingMargin\"I\"SSFTrailingMargin\"I}\"stable\"B\"limitsReached\"B\"drcSuspended\"B\"multiCam\"B\"aeAverage\"I\"aeTarget\"I\"aeMatrixHorCount\"S\"aeMatrixVerCount\"S\"aeMatrix\"[16[16I]]\"motionFromAEMatrix\"I\"currentEIT\"Q\"hdrRatio\"S\"ev0Ratio\"S\"expBias\"S\"realizedExpBias\"S\"aeMatrixMin\"I\"aeMatrixMax\"I\"expBiasCommandTag\"I\"manualExposureGainCommandTag\"I\"bracketingCaptureEVStop\"s\"fdAEParams\"{sCIspMetaDataFDExposureDebug=\"faceAverage\"i\"faceWeight\"i\"sceneXl\"i\"sceneXm\"i\"sceneXh\"i\"sceneTarget\"i\"scale\"i\"aeBlend\"i\"aeAverage\"i\"aeTarget\"i\"darkOutlierCount\"i\"brightOutlierCount\"i}\"meteringMode\"S\"flickerDebugParams\"{sFlickerDetectionDebugParams=\"detectStatus\"i\"count\"S\"freq\"[2I]\"confidence\"[2S]\"waveMatch\"[2S]}\"isoBase\"I\"luxCalcParams\"{sLuxCalcParams=\"scale\"I\"scaleShift\"I}\"pseudoYWeight\"[3S]\"panoExpRatio\"S\"strobePattern\"i\"strobeAux\"I\"strobeCurrent\"I\"bioCaptureGroup\"I\"fIDFlowType\"i\"maxPulseWidthLCUs\"[3I]\"slowSyncIsSlowSync\"B\"faceExpRatioFiltered\"f\"faceExpRatio\"f\"bodyAdjustRatio\"f\"flashLEDOffLux\"f\"flashPreflashLux\"f\"flashMixPercentage\"[512S]\"flashMainFlashLuxFull\"I\"bHDRPrebracketing\"B\"pairedStrobePattern\"i\"aeMode\"I\"repeatSequence\"i\"isSifrMode\"B\"isVHDRMode\"B\"HRDampingRatio\"f\"sifrRDOffset\"I\"exposureSifr\"Q\"exposureTimeSifr\"I\"gainAnalSifr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigiSensorSifr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigiSifr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"captureFrameType\"C\"sifrSkipRatio\"i\"sifrOffPrepare\"B\"isEV0RatioStable\"B\"splitPDOn\"B\"SphereRecenteringMode\"C\"overflowDGain\"I\"UBMisc\"{sCIspCmdUBParamsSetMiscData=\"analogGainLimit\"f\"awbReflow\"{sAWBReflowParam=\"bGenerateReflowAWB\"B\"bUsingSingleStillAWB\"B}}\"AEMisc\"{sCIspAEMiscData=\"nextAE\"{sNextAEParam=\"exposure\"Q\"exposureTime\"I\"gainAnal\"S\"gainDigiSensor\"S\"gainDigi\"S\"exposureSifr\"Q\"exposureTimeSifr\"I\"gainAnalSifr\"S\"gainDigiSensorSifr\"S\"gainDigiSifr\"S\"sifrSkipRatio\"i\"overflowDGain\"I\"hdrRatio\"S\"ev0Ratio\"S\"panoExpRatio\"S\"vHDROn\"B\"bracketingCapture\"C}}\"AEstatsContrastInsideFace\"f\"AEstatsContrastOutsideFace\"f\"videoHDRSwitchOn\"B\"chSyncExpRatios\"[6f]\"hdrScore\"f\"clippingDiscontinuity\"C\"extraSoftDGain\"B\"masterSyncOffset\"I}\"awb\"{sAWBMetaData=\"bFlashAWBDone\"B\"locked\"B\"request\"S\"status\"S\"awbGains\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"gains\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"gainsNormalized\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"eLensShadingMode\"i\"maxWBGainDown\"S\"maxColorCalGainDown\"S\"manualAWBGainCommandTag\"I\"manualCCTCommandTag\"I\"slaveCameraAWBParam\"[6{sSlaveCameraAWBParam=\"rgCalGain\"S\"bgCalGain\"S\"CCTestimate\"I\"wbGain\"[3I]\"comboWBGain\"[3I]\"ccm\"[3[3i]]\"valid\"B\"slaveCh\"Q\"pre_rgLogRatio\"f\"pre_bgLogRatio\"f\"daylightWeight\"f\"useSpatialCCM\"B\"isLEDMainFlashforAWB\"B\"flashProjMixWeighting\"f\"awbGainsFlashProj\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}}]\"pre_rgLogRatio\"f\"pre_bgLogRatio\"f\"daylightWeight\"f\"awbColorspace\"i\"useSpatialCCM\"B\"awbGainsSkinOnly\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"isSlowSyncMainFlashforAWB\"B\"isLEDMainFlashforAWB\"B\"flashProjMixWeighting\"f\"awbGainsFlashProj\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"hostMetadataUpdate\"B\"ccm\"{sAWBColorCorrectionMatrix=\"coeff\"[9(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})]}\"strobeWPointCCM\"{sAWBColorCorrectionMatrix=\"coeff\"[9(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})]}\"CCTEstimate\"I\"displayStrobeCCT\"S\"rgGain\"S\"bgGain\"S\"stable\"S\"usePrevFrameWP\"B\"useTileStats\"S\"firstWBGain\"[3S]\"sceneLuxLevel\"I\"sceneLuxLevelLow\"I\"sceneLuxLevelHigh\"I\"AWBLocked\"I\"ambientLuxLevel\"I\"ambientLuxLevelLow\"I\"ambientLuxLevelHigh\"I\"rawAverage\"[4I]\"isHistWPValid\"S\"fdAWBOutput\"S\"fdAWBChistMixFactor\"I\"fdRect\"[4I]\"grayworldWBGain\"[3S]\"RGBEstimate\"[3S]\"auxMeta\"(metaAux=\"all\"I\"\"{?=\"counter\"b8\"bracketCapture\"b1\"bracketCount\"b3\"flashCapture\"b1\"flashCaptureCount\"b3})\"initial_rgLogRatio\"I\"initial_bgLogRatio\"I\"isDefaultSetting\"B\"bBypassConvergenceFr\"B\"statFrameCount\"I\"isMatchedSlaveSetting\"B\"frameCount\"I\"lowCCTrgBias\"S\"lowCCTbgBias\"S\"hiCCTrgBias\"S\"hiCCTbgBias\"S\"syncTag\"I\"bForStatsSlaveCam\"C\"isValidOneFrameAWBSetting\"B\"singleAWBFrameCount\"I\"oneFrameAWB\"{sCameraAWBParam=\"awbGains\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"gains\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"gainsNormalized\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"maxWBGainDown\"S\"maxColorCalGainDown\"S\"CCTEstimate\"I\"rgGain\"S\"bgGain\"S\"ccm\"{sAWBColorCorrectionMatrix=\"coeff\"[9(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})]}\"awbGainsActual\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}}\"awbReflow\"{sAWBReflowParam=\"bGenerateReflowAWB\"B\"bUsingSingleStillAWB\"B}\"tileStatsRegionInRaw\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"isTileStatsRegionUpdated\"B\"semanticChannel\"Q\"semanticFrameCount\"I\"clrBE2DHistProb\"C\"clrBE2DHistFrameCount\"I\"fdAWBVersion\"C\"spatialCCMWeights\"[192f]}\"zoom\"{sZoomMetaData=\"fesOutputWidth\"S\"fesOutputHeight\"S\"ispInputWidth\"S\"ispInputHeight\"S\"isFEStatOTF\"B}\"isReprocessing\"B\"isReplay\"B\"tele2WideFOVDelta\"f\"wide2TeleFOVDelta\"f\"wide2SWideFOVDelta\"f\"sWide2WideFOVDelta\"f\"implicitFOVScaleSrcChToDestCh\"[6[6f]]\"FESOutputSize\"{sRectSize=\"width\"I\"height\"I}\"sensorCrop\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"DMACrop\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}}"
- "{sPerModuleLEDCalibData=\"version\"C\"isvalid\"C\"programID\"C\"cw_rg\"f\"cw_bg\"f\"ww_rg\"f\"ww_bg\"f\"ledWidePtrn_rg\"f\"ledWidePtrn_bg\"f\"ledSWidePtrn_rg\"f\"ledSWidePtrn_bg\"f\"ledTelePtrn_rg\"f\"ledTelePtrn_bg\"f\"strb_rg\"f\"strb_bg\"f}"
- "{sRefDriverInputs_SOFTISP=\"HROn\"B\"hrGainDownRatio\"S\"exposureTime\"I\"gainAnal\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gainDigi\"I\"hardIspDGain\"f\"softIspDGain\"f\"expBias\"S\"realizedExpBias\"S\"hdrRatio\"S\"ev0Ratio\"S\"overflowDGain\"I\"faceExpRatioFiltered\"f\"panoExpRatio\"S\"bLTMSingleFrameMode\"B\"ltmProcMode\"C\"bracketingMode\"C\"bracketingExpRatio\"I\"gainDigiSensor\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"luxLevel\"f\"useSpatialCCM\"B\"channel\"C\"flashStatus\"B\"isHLGMode\"B\"LTMGridConfig\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"localHistGridConfig\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"flashMixPercentage\"[512S]\"flashProjMixWeighting\"f\"tileStatsRegion\"{sBTRect=\"x\"i\"y\"i\"width\"I\"height\"I}\"ccm\"{sAWBColorCorrectionMatrix_local=\"coeff\"[9(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})]}\"isLEDMainFlashforAWB\"B\"awbGains\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsSkinOnly\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"awbGainsFlashProj\"{sBTRGGB16=\"r\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gr\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"gb\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})\"b\"(uBTColorEntry16=\"v16\"S\"v88\"{uBT88=\"fractional\"C\"integer\"C})}\"fdAWBChistMixFactor\"I\"awbColorspace\"C\"faceInfo\"{sFaceInfo_SOFTISP=\"rectArray\"[10{sCIspFDRect=\"x\"i\"y\"i\"width\"I\"height\"I}]\"primaryFaceIndex\"I\"numFaces\"I}\"forceDisableFaceBoost\"B\"gammaCurve\"i\"useHighlightCompression\"B\"useAdaptiveHighlightCompression\"B\"highlightCompressionGain\"f\"isSIFRFrame\"B\"LTMHazeCorrectionOff\"B\"useBt709\"B\"useHazeCorrection\"B\"hazeCorrection\"\"tuningParametersOverride\"[6{LTMTuning=\"histDampingExponentHighlight\"f\"histDampingExponentMax\"f\"hmaxHeadroom\"f\"maxPaddingRange\"f\"dispRangeActiveRatio\"f\"sceneBlackRatio\"f\"sceneBlackRatioDark\"f\"sceneBgOffset\"f\"desatStrength\"f\"minFlareDark\"f\"shadowSuppressBase\"f\"shadowSuppressMax\"f\"shadowSuppressEITAdj\"f\"minSceneLux\"f\"histSmoothingMax\"f\"smoothingStrength\"f\"dispRangeDarkRatio\"f\"sceneModelSmoothing\"f\"nonFaceRatioFloor\"f\"fstart\"f\"shadowDesat\"f\"darkSceneLux\"f\"darkSceneLuxThreshold\"\"ambientViewingLux\"f\"ambientViewingChromaticityX\"f\"ambientViewingChromaticityY\"f\"sceneBlackMax\"f\"dispLum\"f\"dispBlack\"f}]\"useTuningParametersOverride\"B\"faceBiasScaler\"f\"faceLTMVer\"C\"CBVer\"C}"

```
