## FRC

> `/System/Library/PrivateFrameworks/FRC.framework/FRC`

```diff

-178.0.0.0.0
-  __TEXT.__text: 0x284e4
-  __TEXT.__auth_stubs: 0xa40
-  __TEXT.__objc_methlist: 0x22a0
-  __TEXT.__const: 0x4f8
-  __TEXT.__cstring: 0x4195
-  __TEXT.__oslogstring: 0x271
+189.0.0.0.0
+  __TEXT.__text: 0x2b468
+  __TEXT.__auth_stubs: 0xab0
+  __TEXT.__objc_methlist: 0x2528
+  __TEXT.__const: 0x508
+  __TEXT.__cstring: 0x45ef
+  __TEXT.__oslogstring: 0x328
   __TEXT.__gcc_except_tab: 0xac
-  __TEXT.__unwind_info: 0x804
-  __TEXT.__objc_classname: 0x2d5
-  __TEXT.__objc_methname: 0x9078
-  __TEXT.__objc_methtype: 0x2de7
-  __TEXT.__objc_stubs: 0x46e0
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x430
-  __DATA_CONST.__objc_classlist: 0x120
+  __TEXT.__unwind_info: 0x878
+  __TEXT.__objc_classname: 0x2e9
+  __TEXT.__objc_methname: 0x9cec
+  __TEXT.__objc_methtype: 0x2e27
+  __TEXT.__objc_stubs: 0x4a80
+  __DATA_CONST.__got: 0x1d8
+  __DATA_CONST.__const: 0x458
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6250
-  __DATA_CONST.__objc_selrefs: 0x1668
-  __AUTH_CONST.__cfstring: 0x2980
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__const: 0x18
-  __AUTH_CONST.__auth_got: 0x530
-  __DATA.__objc_classrefs: 0x1f8
-  __DATA.__objc_superrefs: 0xe8
-  __DATA.__objc_ivar: 0x830
+  __DATA_CONST.__objc_const: 0x6a48
+  __DATA_CONST.__objc_selrefs: 0x17f0
+  __DATA_CONST.__objc_classrefs: 0x200
+  __DATA_CONST.__objc_superrefs: 0xf0
+  __AUTH_CONST.__cfstring: 0x2ce0
+  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__const: 0x58
+  __AUTH_CONST.__auth_got: 0x568
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x8c0
   __DATA.__data: 0x138
-  __DATA.__bss: 0x8
-  __DATA_DIRTY.__const: 0xa0
+  __DATA_DIRTY.__const: 0x60
   __DATA_DIRTY.__objc_const: 0xbc8
   __DATA_DIRTY.__objc_data: 0xb40
+  __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOSurface.framework/IOSurface
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/Vision.framework/Vision
   - /System/Library/PrivateFrameworks/CMCapture.framework/CMCapture

   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 575A8978-5B67-359C-9201-2E789F66C060
-  Functions: 865
-  Symbols:   3306
-  CStrings:  2502
+  UUID: 265B17B2-8D65-34C8-8F66-F7B9507B8C3D
+  Functions: 910
+  Symbols:   3485
+  CStrings:  2657
 
Symbols:
+ +[OpticalFlow use4xDownScale:]
+ -[FRCFrameInterpolator checkStreamingBufferConsistencyFirstFrame:secondFrame:]
+ -[FRCFrameInterpolator setStreamingMode:]
+ -[FRCFrameInterpolator setSynthesis:]
+ -[FRCFrameInterpolator setSynthesisOptionsFromDefaults]
+ -[FRCFrameInterpolator setTwoLayerSynthesis:]
+ -[FRCFrameInterpolator setTwoLayerSynthesisQuarterSizeDC:]
+ -[FRCFrameInterpolator setUseFlowConsistencyMap:]
+ -[FRCFrameInterpolator streamingMode]
+ -[FRCFrameInterpolator synthesis]
+ -[FRCFrameInterpolator twoLayerSynthesisQuarterSizeDC]
+ -[FRCFrameInterpolator twoLayerSynthesis]
+ -[FRCFrameInterpolator useFlowConsistencyMap]
+ -[FRCFrameSynthesizer flowHeight]
+ -[FRCFrameSynthesizer flowWidth]
+ -[FRCFrameSynthesizer updateFlowSize]
+ -[FlowConsistencyMap .cxx_destruct]
+ -[FlowConsistencyMap allocateLinearConsistencyMapWithWidth:height:]
+ -[FlowConsistencyMap computeMaxConsisnteciesForwardConsistencyMap:backwardConsistencyMap:]
+ -[FlowConsistencyMap createFlowConsistencyMapsWithForwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:]
+ -[FlowConsistencyMap createKernels]
+ -[FlowConsistencyMap encodeMapNormalizationToCommandBuffer:consisitencyMap:maxConsistency:]
+ -[FlowConsistencyMap encodeMapUpscalingToCommandBuffer:source:detination:]
+ -[FlowConsistencyMap encodeToCommandBuffer:forwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:]
+ -[FlowConsistencyMap encodeUnomalizedMapCreationToCommandBuffer:forwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:]
+ -[FlowConsistencyMap initWithDevice:commmandQueue:]
+ -[FlowConsistencyMap maxConsistency]
+ -[FlowConsistencyMap maxValueInTexture:]
+ -[FlowConsistencyMap setUseSIMD:]
+ -[FlowConsistencyMap useSIMD]
+ -[Forwarp encodeBlendWarpedFeaturesWithErrorMaskToCommandBuffer:first:second:forwardErrorMap:backwardErrorMap:forwarpConsistency:backwardConsistency:timeScale:destination:]
+ -[Forwarp encodeWarpAndBlendFeaturesWithErrorMaskToCommandBuffer:first:second:forwardFlow:backwardFlow:forwardErrorMap:backwardErrorMap:forwarpConsistency:backwardConsistency:timeScale:destination:]
+ -[Forwarp initWithDevice:commmandQueue:mode:]
+ -[LiteSynthesis frameSyncRequired]
+ -[OpticalFlow extractFeaturesFromFirst:second:]
+ -[Pyramid encode3x3GaussianFilterToCommandBuffer:source:destination:]
+ -[Pyramid encodeBicubicSubsampleTextureToCommandBuffer:source:destination:]
+ -[Pyramid encodeLayerBlendToCommandBuffer:baseLayer:toDestination:]
+ -[Pyramid encodeSubsampleTextureWith3x3GaussianToCommandBuffer:source:destination:]
+ -[Pyramid encodeSubsampleTextureWith5x5GaussianToCommandBuffer:source:destination:clampToEdge:]
+ -[Synthesis createConsistencyMapFormFirstImage:secondImage:flowForward:flowBackward:]
+ -[Synthesis createSubsampledInputsFromFirstFrame:secondImage:]
+ -[Synthesis encodeConsistencyMapCreationWithFlowToCommandBuffer:firstSource:secondSource:forwardFlow:backwardFlow:firstForwarpInput:secondForwarpInput:]
+ -[Synthesis encodeWarpPyramidToCommandBuffer:forwardFlow:backwardFlow:forwarpConsistency:backwardConsistency:timeScale:destination:]
+ -[Synthesis firstForwarpInput]
+ -[Synthesis frameSyncRequired]
+ -[Synthesis secondForwarpInput]
+ -[Synthesis setTwoLayerFlowSplatting:]
+ -[Synthesis setTwoLayerQuarterSizeDC:]
+ -[Synthesis setUseFlowConsistencyMap:]
+ -[Synthesis setUseFusedKernel:]
+ -[Synthesis twoLayerFlowSplattingFeatureLevelForLevel:]
+ -[Synthesis twoLayerFlowSplatting]
+ -[Synthesis twoLayerQuarterSizeDC]
+ -[Synthesis upscaleFlowsForward:backward:]
+ -[Synthesis useFlowConsistencyMap]
+ -[Synthesis useFusedKernel]
+ GCC_except_table29
+ _CFStringCompare
+ _CGColorSpaceEqualToColorSpace
+ _CVImageBufferCreateColorSpaceFromAttachments
+ _IOSurfaceGetBaseAddress
+ _IOSurfaceGetID
+ _IOSurfaceLock
+ _IOSurfaceUnlock
+ _OBJC_CLASS_$_FlowConsistencyMap
+ _OBJC_IVAR_$_FRCFrameInterpolator._firstPairInSession
+ _OBJC_IVAR_$_FRCFrameInterpolator._previousSecondIOSurfaceID
+ _OBJC_IVAR_$_FRCFrameInterpolator._streamingMode
+ _OBJC_IVAR_$_FRCFrameInterpolator._twoLayerSynthesis
+ _OBJC_IVAR_$_FRCFrameInterpolator._twoLayerSynthesisQuarterSizeDC
+ _OBJC_IVAR_$_FRCFrameInterpolator._useFlowConsistencyMap
+ _OBJC_IVAR_$_FRCFrameSynthesizer._flowHeight
+ _OBJC_IVAR_$_FRCFrameSynthesizer._flowWidth
+ _OBJC_IVAR_$_FlowConsistencyMap._consistencyComputeKernel
+ _OBJC_IVAR_$_FlowConsistencyMap._consistencyNormalizationKernel
+ _OBJC_IVAR_$_FlowConsistencyMap._consistencyUpscalingKernel
+ _OBJC_IVAR_$_FlowConsistencyMap._maxBuffer
+ _OBJC_IVAR_$_FlowConsistencyMap._useSIMD
+ _OBJC_IVAR_$_Forwarp._blendWarpedImagesWithMaskAndFlowConsistency
+ _OBJC_IVAR_$_Forwarp._synthesisMode
+ _OBJC_IVAR_$_Forwarp._warpAndBlendTextures
+ _OBJC_IVAR_$_Forwarp._warpAndBlendTexturesWithConsistency
+ _OBJC_IVAR_$_LiteSynthesis._frameSyncRequired
+ _OBJC_IVAR_$_Normalization._prevSecondStat
+ _OBJC_IVAR_$_Pyramid._bicubicSubsampleKernel
+ _OBJC_IVAR_$_Pyramid._gaussian3x3CoefficientBuffer
+ _OBJC_IVAR_$_Pyramid._gaussian3x3FilterKernel
+ _OBJC_IVAR_$_Pyramid._gaussian3x3SubsampleKernel
+ _OBJC_IVAR_$_Pyramid._supportsSIMDShuffle
+ _OBJC_IVAR_$_Pyramid._twoLayerBlendKernel
+ _OBJC_IVAR_$_Synthesis._blendedDCTexture
+ _OBJC_IVAR_$_Synthesis._filteredDCTexture
+ _OBJC_IVAR_$_Synthesis._firstForwarpInputWithConsistencyMap
+ _OBJC_IVAR_$_Synthesis._flowConsisteny
+ _OBJC_IVAR_$_Synthesis._frameSyncRequired
+ _OBJC_IVAR_$_Synthesis._fullSizeSplatting
+ _OBJC_IVAR_$_Synthesis._secondForwarpInputWithConsistencyMap
+ _OBJC_IVAR_$_Synthesis._twoLayerFlowSplatting
+ _OBJC_IVAR_$_Synthesis._twoLayerQuarterSizeDC
+ _OBJC_IVAR_$_Synthesis._useFlowConsistencyMap
+ _OBJC_IVAR_$_Synthesis._useFusedKernel
+ _OBJC_IVAR_$_Synthesis._warpedFeatureChannels
+ _OBJC_METACLASS_$_FlowConsistencyMap
+ __OBJC_$_CLASS_METHODS_OpticalFlow
+ __OBJC_$_INSTANCE_METHODS_FlowConsistencyMap
+ __OBJC_$_INSTANCE_VARIABLES_FlowConsistencyMap
+ __OBJC_$_PROP_LIST_FRCFrameSynthesizer
+ __OBJC_$_PROP_LIST_FlowConsistencyMap
+ __OBJC_CLASS_RO_$_FlowConsistencyMap
+ __OBJC_METACLASS_RO_$_FlowConsistencyMap
+ ___115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.92
+ ___115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke_2.93
+ ___85-[Synthesis createConsistencyMapFormFirstImage:secondImage:flowForward:flowBackward:]_block_invoke
+ ___block_descriptor_40_e8_32s_e28_v16?0"<MTLCommandBuffer>"8ls32l8
+ ___block_literal_global.42
+ ___block_literal_global.53
+ _kCGColorSpaceDisplayP3
+ _kCGColorSpaceITUR_2020
+ _kCGColorSpaceITUR_709
+ _kCMFormatDescriptionColorPrimaries_P3_D65
+ _kCMFormatDescriptionTransferFunction_ITU_R_2100_HLG
+ _kCVImageBufferColorPrimaries_ITU_R_2020
+ _kCVImageBufferTransferFunction_ITU_R_2100_HLG
+ _kCVImageBufferYCbCrMatrix_ITU_R_2020
+ _objc_msgSend$bufferBytesPerRow
+ _objc_msgSend$checkStreamingBufferConsistencyFirstFrame:secondFrame:
+ _objc_msgSend$computeMaxConsisnteciesForwardConsistencyMap:backwardConsistencyMap:
+ _objc_msgSend$copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:
+ _objc_msgSend$createConsistencyMapFormFirstImage:secondImage:flowForward:flowBackward:
+ _objc_msgSend$createKernels
+ _objc_msgSend$createSubsampledInputsFromFirstFrame:secondImage:
+ _objc_msgSend$encode3x3GaussianFilterToCommandBuffer:source:destination:
+ _objc_msgSend$encodeBicubicSubsampleTextureToCommandBuffer:source:destination:
+ _objc_msgSend$encodeBlendWarpedFeaturesWithErrorMaskToCommandBuffer:first:second:forwardErrorMap:backwardErrorMap:forwarpConsistency:backwardConsistency:timeScale:destination:
+ _objc_msgSend$encodeConsistencyMapCreationWithFlowToCommandBuffer:firstSource:secondSource:forwardFlow:backwardFlow:firstForwarpInput:secondForwarpInput:
+ _objc_msgSend$encodeLayerBlendToCommandBuffer:baseLayer:toDestination:
+ _objc_msgSend$encodeMapNormalizationToCommandBuffer:consisitencyMap:maxConsistency:
+ _objc_msgSend$encodeMapUpscalingToCommandBuffer:source:detination:
+ _objc_msgSend$encodeSubsampleTextureWith5x5GaussianToCommandBuffer:source:destination:clampToEdge:
+ _objc_msgSend$encodeToCommandBuffer:forwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:
+ _objc_msgSend$encodeUnomalizedMapCreationToCommandBuffer:forwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:
+ _objc_msgSend$encodeWarpAndBlendFeaturesWithErrorMaskToCommandBuffer:first:second:forwardFlow:backwardFlow:forwardErrorMap:backwardErrorMap:forwarpConsistency:backwardConsistency:timeScale:destination:
+ _objc_msgSend$encodeWarpPyramidToCommandBuffer:forwardFlow:backwardFlow:forwarpConsistency:backwardConsistency:timeScale:destination:
+ _objc_msgSend$extractFeaturesFromFirst:second:
+ _objc_msgSend$frameSyncRequired
+ _objc_msgSend$initWithDevice:commmandQueue:mode:
+ _objc_msgSend$iosurface
+ _objc_msgSend$level
+ _objc_msgSend$maxConsistency
+ _objc_msgSend$maxValueInTexture:
+ _objc_msgSend$newTextureViewWithPixelFormat:textureType:levels:slices:
+ _objc_msgSend$newTextureWithDescriptor:offset:bytesPerRow:
+ _objc_msgSend$setSynthesisOptionsFromDefaults
+ _objc_msgSend$setTwoLayerFlowSplatting:
+ _objc_msgSend$setTwoLayerQuarterSizeDC:
+ _objc_msgSend$setUseFlowConsistencyMap:
+ _objc_msgSend$twoLayerFlowSplattingFeatureLevelForLevel:
+ _objc_msgSend$upscaleFlowsForward:backward:
+ _readYUV10bit
+ _writeYUV10bit
- -[FRCFrameSynthesizer setFirstFrame:secondFrame:forwardFlow:backwardFlow:].cold.1
- -[FRCFrameSynthesizer synthesizeFrameForTimeScale:destination:].cold.1
- -[FRCOpticalFlowEstimator opticalFlowFrom:to:].cold.1
- -[FRCOpticalFlowEstimator opticalFlowFrom:to:flow:].cold.1
- -[FRCOpticalFlowEstimator opticalFlowsFrom:to:].cold.1
- -[FRCOpticalFlowEstimator opticalFlowsFrom:to:forwardFlow:backwardFlow:].cold.1
- -[Forwarp encodeBlendWarpedFeaturesWithErrorMaskToCommandBuffer:first:second:forwardErrorMap:backwardErrorMap:timeScale:destination:]
- -[Forwarp initWithDevice:commmandQueue:isLiteSynthesis:]
- -[OpticalFlow extractFeaturesFromFirst:second:outputFeatures:]
- -[OpticalFlow use4xDownScale:]
- -[Pyramid encodeSubsampleTextureToCommandBuffer:source:destination:clampToEdge:]
- GCC_except_table27
- _OBJC_IVAR_$_Forwarp._blendWarpedImagesWithSubsampledMaskTextures
- _OUTLINED_FUNCTION_0
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- ___115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke.89
- ___115-[FRCFrameInterpolator interpolateBetweenFirstFrame:secondFrame:timeScales:outputSize:outputPixelFormat:withError:]_block_invoke_2.90
- ___block_literal_global.45
- ___block_literal_global.52
- _objc_msgSend$encodeBlendWarpedFeaturesWithErrorMaskToCommandBuffer:first:second:forwardErrorMap:backwardErrorMap:timeScale:destination:
- _objc_msgSend$encodeSubsampleTextureToCommandBuffer:source:destination:clampToEdge:
- _objc_msgSend$extractFeaturesFromFirst:second:outputFeatures:
- _objc_msgSend$framePipeline
- _objc_msgSend$initWithDevice:commmandQueue:isLiteSynthesis:
CStrings:
+ "\x06O\x0f\x0f\xf0\xf0!\xf0v!"
+ "\x06\xf0\xc26\xa1\xa1"
+ "\n\x1a"
+ "\x0e"
+ ">> ERROR: Failed to create kernel: %@"
+ "@\"FlowConsistencyMap\""
+ "@40@0:8@16@24Q32"
+ "B32@0:8@16@24"
+ "Error! Texture is not made from a buffer"
+ "Error! buffer is not accessible"
+ "Failed to switch (%p) [usage:%d, 1/4 flow:%d, twoStage:%d, flow size (%ldx%ld)]."
+ "FeatureExtractor: Error !! Network execution Failed. (Usage:%ld)"
+ "FlowAdaptationDecoder: Error !! Network execution Failed. (Usage:%ld)"
+ "FlowAdaptationFeatureExtractor: Error !! Network execution Failed. (Usage:%ld)"
+ "FlowConsistencyMap"
+ "FlowEstimate Level:%d: Error !! Network execution Failed. (Usage:%ld)"
+ "GridNet: Error !! Network execution Failed. (Usage:%ld)\n"
+ "Initialization failed [usage:%ld (%ldx%ld), mode:%ld, synthesis mode:%ld]."
+ "Initialized successfully (%p) [usage:%d (%ldx%ld), mode:%d, synthesis mode:%d, temporal filtering:%d]."
+ "Initialized successfully (%p) [usage:%d, 1/4 flow:%d, twoStage:%d, flow size (%ldx%ld)]."
+ "Max values from atomic max %d\n"
+ "Max vlues from CPU %f\n"
+ "Normalization: Error! when firstInput is nil, firstOutput must be nil as well"
+ "Released (%p) [usage:%ld]"
+ "Synthesis: Max flow consistency %f\n"
+ "T@\"NSString\",?,R,C"
+ "T@,&,N,V_synthesis"
+ "TB,?,N"
+ "TB,N,V_streamingMode"
+ "TB,N,V_twoLayerFlowSplatting"
+ "TB,N,V_twoLayerQuarterSizeDC"
+ "TB,N,V_twoLayerSynthesis"
+ "TB,N,V_twoLayerSynthesisQuarterSizeDC"
+ "TB,N,V_useFlowConsistencyMap"
+ "TB,N,V_useFusedKernel"
+ "TB,N,V_useSIMD"
+ "TB,R,N,V_frameSyncRequired"
+ "TQ,?,N"
+ "Ti,?,N"
+ "TwoLayerSynthesisQuarterSizeDC"
+ "UseFlowConsistencyMap"
+ "UseTwoLayerSynthesis"
+ "[EpsressoModel] Cannot load Net file %@. Configuration: %s\n"
+ "[EpsressoModel] Error failed to create a context\n"
+ "[EspressoModel] Error failed to create a plan\n"
+ "[EspressoModel] build failure : %@. Configuration: %s"
+ "[FRC] Streaming Mode enabled."
+ "[FrameInterpolator] Disabling streaming mode."
+ "[FrameInterpolator] Error! In streaming mode, the first frame (IOSId %d) must be identical to the second frame (IOSId %d) of previous call"
+ "_bicubicSubsampleKernel"
+ "_blendWarpedImagesWithMaskAndFlowConsistency"
+ "_blendedDCTexture"
+ "_consistencyComputeKernel"
+ "_consistencyNormalizationKernel"
+ "_consistencyUpscalingKernel"
+ "_filteredDCTexture"
+ "_firstForwarpInputWithConsistencyMap"
+ "_firstPairInSession"
+ "_flowConsisteny"
+ "_frameSyncRequired"
+ "_fullSizeSplatting"
+ "_gaussian3x3SubsampleKernel"
+ "_maxBuffer"
+ "_prevSecondStat"
+ "_previousSecondIOSurfaceID"
+ "_secondForwarpInputWithConsistencyMap"
+ "_streamingMode"
+ "_twoLayerBlendKernel"
+ "_twoLayerFlowSplatting"
+ "_twoLayerQuarterSizeDC"
+ "_twoLayerSynthesis"
+ "_twoLayerSynthesisQuarterSizeDC"
+ "_useFlowConsistencyMap"
+ "_useFusedKernel"
+ "_useSIMD"
+ "_warpAndBlendTextures"
+ "_warpAndBlendTexturesWithConsistency"
+ "_warpedFeatureChannels"
+ "allocateLinearConsistencyMapWithWidth:height:"
+ "bicubic_subsample"
+ "blendWarpedImageWithErrorMapAndFlowConsistency"
+ "blend_two_layer_pyramid"
+ "bufferBytesPerRow"
+ "checkStreamingBufferConsistencyFirstFrame:secondFrame:"
+ "computeMaxConsisnteciesForwardConsistencyMap:backwardConsistencyMap:"
+ "convertFixedPointBuffer2Texture"
+ "copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:"
+ "createConsistencyMapFormFirstImage:secondImage:flowForward:flowBackward:"
+ "createFlowConsistencyMapsWithForwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:"
+ "createKernels"
+ "createSubsampledInputsFromFirstFrame:secondImage:"
+ "create_consistency_map"
+ "create_consistency_map_SIMD"
+ "encode3x3GaussianFilterToCommandBuffer:source:destination:"
+ "encodeBicubicSubsampleTextureToCommandBuffer:source:destination:"
+ "encodeBlendWarpedFeaturesWithErrorMaskToCommandBuffer:first:second:forwardErrorMap:backwardErrorMap:forwarpConsistency:backwardConsistency:timeScale:destination:"
+ "encodeConsistencyMapCreationWithFlowToCommandBuffer:firstSource:secondSource:forwardFlow:backwardFlow:firstForwarpInput:secondForwarpInput:"
+ "encodeLayerBlendToCommandBuffer:baseLayer:toDestination:"
+ "encodeMapNormalizationToCommandBuffer:consisitencyMap:maxConsistency:"
+ "encodeMapUpscalingToCommandBuffer:source:detination:"
+ "encodeSubsampleTextureWith3x3GaussianToCommandBuffer:source:destination:"
+ "encodeSubsampleTextureWith5x5GaussianToCommandBuffer:source:destination:clampToEdge:"
+ "encodeToCommandBuffer:forwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:"
+ "encodeUnomalizedMapCreationToCommandBuffer:forwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:"
+ "encodeWarpAndBlendFeaturesWithErrorMaskToCommandBuffer:first:second:forwardFlow:backwardFlow:forwardErrorMap:backwardErrorMap:forwarpConsistency:backwardConsistency:timeScale:destination:"
+ "encodeWarpPyramidToCommandBuffer:forwardFlow:backwardFlow:forwarpConsistency:backwardConsistency:timeScale:destination:"
+ "extractFeaturesFromFirst:second:"
+ "f24@0:8@16"
+ "f32@0:8@16@24"
+ "f48@0:8@16@24@32@40"
+ "firstForwarpInput"
+ "frameSyncRequired"
+ "gaussian3x3_filter"
+ "gaussian3x3_filter_SIMD"
+ "gaussian3x3_subsample"
+ "i20@0:8i16"
+ "initWithDevice:commmandQueue:mode:"
+ "iosurface"
+ "maxConsistency"
+ "maxValueInTexture:"
+ "newTextureViewWithPixelFormat:textureType:levels:slices:"
+ "newTextureWithDescriptor:offset:bytesPerRow:"
+ "normalized_consistency_map"
+ "secondForwarpInput"
+ "setStreamingMode:"
+ "setSynthesis:"
+ "setSynthesisOptionsFromDefaults"
+ "setTwoLayerFlowSplatting:"
+ "setTwoLayerQuarterSizeDC:"
+ "setTwoLayerSynthesis:"
+ "setTwoLayerSynthesisQuarterSizeDC:"
+ "setUseFlowConsistencyMap:"
+ "setUseFusedKernel:"
+ "setUseSIMD:"
+ "streamingMode"
+ "synthesis"
+ "twoLayerFlowSplatting"
+ "twoLayerFlowSplattingFeatureLevelForLevel:"
+ "twoLayerQuarterSizeDC"
+ "twoLayerSynthesis"
+ "twoLayerSynthesisQuarterSizeDC"
+ "updateOutputFloat"
+ "upscaleFlowsForward:backward:"
+ "upscale_consistency_map"
+ "useFlowConsistencyMap"
+ "useFusedKernel"
+ "useSIMD"
+ "v100@0:8@16@24@32@40@48@56@64@72@80f88@92"
+ "v72@0:8@16@24@32@40@48@56@64"
+ "v84@0:8@16@24@32@40@48@56@64f72@76"
+ "warpAndBlendImageWithErrorAndFlowConsistency"
+ "warpAndBlendWithErrorMap"
+ "{?=\"sum\"f\"sum_of_square\"f}"
- "\x06O\x0f\r\xf0\xf0\x11\xf0t"
- "\x06\xf0\xc26\xa1\x81"
- "\t"
- "\n\x18"
- "@36@0:8@16@24B32"
- "Cannot load Net file %@\n"
- "Error !! Network execution Failed"
- "Error !! Network execution Failed\n"
- "Error failed to crate a context\n"
- "Error failed to crate a plan\n"
- "Espresso model build failure : %@\n"
- "FlowAdaptationFeatureExtractor: Error !! Network execution Failed"
- "Initialized successfully [usage:%d (%ldx%ld), mode:%d, synthesis mode:%d, temporal filtering:%d]."
- "Initialized successfully [usage:%d, 1/4 flow:%d, twoStage:%d, flow size [%ldx%ld]."
- "Released."
- "TQ,N"
- "Ti,N"
- "[FRCFrameSynthesizer] Unsupported Configuration usage:%ld, qualityMode:%ld"
- "_blendWarpedImagesWithSubsampledMaskTextures"
- "blendWarpedImagesWithDownsampledErrorMapTextures"
- "encodeBlendWarpedFeaturesWithErrorMaskToCommandBuffer:first:second:forwardErrorMap:backwardErrorMap:timeScale:destination:"
- "encodeSubsampleTextureToCommandBuffer:source:destination:clampToEdge:"
- "extractFeaturesFromFirst:second:outputFeatures:"
- "initWithDevice:commmandQueue:isLiteSynthesis:"
- "v40@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}}^{__CVBuffer}^{__CVBuffer}}32"

```
