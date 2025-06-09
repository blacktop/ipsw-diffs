## AppleCVAPhoto

> `/System/Library/PrivateFrameworks/AppleCVAPhoto.framework/AppleCVAPhoto`

```diff

-576.100.2.0.0
-  __TEXT.__text: 0x4c714
-  __TEXT.__auth_stubs: 0xba0
+603.0.0.0.0
+  __TEXT.__text: 0x4c35c
+  __TEXT.__auth_stubs: 0xb80
   __TEXT.__init_offsets: 0x3c
-  __TEXT.__objc_methlist: 0x2bbc
-  __TEXT.__const: 0x920
-  __TEXT.__gcc_except_tab: 0x64e8
-  __TEXT.__cstring: 0x7b7b
-  __TEXT.__oslogstring: 0xe20
-  __TEXT.__unwind_info: 0x1028
-  __TEXT.__objc_classname: 0x626
-  __TEXT.__objc_methname: 0xc4da
-  __TEXT.__objc_methtype: 0x37c5
-  __TEXT.__objc_stubs: 0x4a80
+  __TEXT.__objc_methlist: 0x2c04
+  __TEXT.__const: 0x928
+  __TEXT.__gcc_except_tab: 0x63d4
+  __TEXT.__cstring: 0x773e
+  __TEXT.__oslogstring: 0xe4b
+  __TEXT.__unwind_info: 0x1038
+  __TEXT.__objc_classname: 0x628
+  __TEXT.__objc_methname: 0xc569
+  __TEXT.__objc_methtype: 0x3481
+  __TEXT.__objc_stubs: 0x49a0
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x588
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1850
+  __DATA_CONST.__objc_selrefs: 0x1828
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0x118
-  __AUTH_CONST.__auth_got: 0x5e8
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH_CONST.__const: 0x4e0
-  __AUTH_CONST.__cfstring: 0x5ee0
-  __AUTH_CONST.__objc_const: 0x8d30
+  __AUTH_CONST.__cfstring: 0x5c60
+  __AUTH_CONST.__objc_const: 0x8d50
   __AUTH_CONST.__objc_arrayobj: 0x168
-  __AUTH_CONST.__objc_intobj: 0xb70
+  __AUTH_CONST.__objc_intobj: 0xb88
   __AUTH_CONST.__objc_floatobj: 0x1f0
-  __AUTH_CONST.__objc_doubleobj: 0x4c0
+  __AUTH_CONST.__objc_doubleobj: 0x4e0
   __AUTH.__objc_data: 0xd70
-  __DATA.__objc_ivar: 0x9a8
+  __DATA.__objc_ivar: 0x9a4
   __DATA.__data: 0x610
-  __DATA.__bss: 0x708
+  __DATA.__bss: 0x6e8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
+  - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0AC678B6-8AC7-3767-AAD4-E3D23DE34737
-  Functions: 892
-  Symbols:   334
-  CStrings:  3589
+  UUID: C8340962-72BD-3B6B-B100-6723253209E6
+  Functions: 900
+  Symbols:   332
+  CStrings:  3550
 
Symbols:
+ _CGRectZero
+ _OBJC_CLASS_$_FigMetalContext
+ _OBJC_CLASS_$_MTLRenderPipelineColorAttachmentDescriptor
- _MTLCreateSystemDefaultDevice
- _NSUnderlyingErrorKey
- _OBJC_CLASS_$_MTLComputePipelineDescriptor
- _OBJC_CLASS_$_MTLRenderPipelineDescriptor
- __Znwm
CStrings:
+ "-[CVAMattingRequest initWithDisparityPostprocessingRequest:segmentationPixelBuffer:skinSegmentationPixelBuffer:primaryCaptureRect:applyRotation:destinationAlphaMattePixelBuffer:error:]"
+ "<"
+ "@\"<MTLDevice>\""
+ "@\"FigMetalContext\""
+ "@100@0:8r^{__CVBuffer=}16r^{__CVBuffer=}24^{__CVBuffer=}32r^{VideoMattingStaticParams=BBIIIIIIiiIfffffffffffIIiffff}40r^v48r^{VideoPostprocessingParams=BfBffB}56@64@72B80@84@?92"
+ "@104@0:8@16@24{?=QQQ}32{?=QQQ}56i80i84i88i92^@96"
+ "@192@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@40i48f52B56{CVAQuaternion=dddd}60{CVAVector=ddd}92{CVAVector=ddd}116@140f148f152{CGRect={CGPoint=dd}{CGSize=dd}}156B188"
+ "@40@0:8@16{CGSize=dd}24"
+ "@44@0:8@16@24i32^@36"
+ "@48@0:8@16Q24Q32^@40"
+ "@56@0:8@16Q24Q32f40f44^@48"
+ "@56@0:8@16{?=QQQ}24^@48"
+ "@56@0:8r^{VideoMattingStaticParams=BBIIIIIIiiIfffffffffffIIiffff}16f24f28f32B36^v40^@48"
+ "@92@0:8@16^{__CVBuffer=}24^{__CVBuffer=}32{CGRect={CGPoint=dd}{CGSize=dd}}40B72^{__CVBuffer=}76^@84"
+ "No parameterDefaultValues for parameter %@"
+ "TB,R,V_applyRotation"
+ "TB,R,V_cropDepthToPrimaryRect"
+ "_applyRotation"
+ "_cropDepthToPrimaryRect"
+ "_deadzoneInCinematic"
+ "_figMetalContext"
+ "applyRotation"
+ "commandQueue"
+ "computePipelineStateFor:constants:"
+ "cropDepthToPrimaryRect"
+ "encodeForegroundMaskToBuffer:disparity:inSegmentation:useSegmentationOnly:weight:foregroundMask:erodedForegroundMask:disparityMin:focusDisparity:hardness:minDistToDeweight:unconfidentWeight:dilateForegroundMask:foregroundMaskDilationRadius:properties:applyRotation:"
+ "encodeRelightKernelToCommandBuffer:isAfterPreviewStitcher:applyRotation:"
+ "encodeToCommandBuffer:srcColorTex:srcAlphaTex:dstForegroundTex:normalizedPrimaryCaptureRect:isAfterPreviewStitcher:applyRotation:"
+ "id<MTLTexture> metalTexture(__strong id<MTLDevice> _Nonnull, MTLPixelFormat, NSUInteger, NSUInteger, MTLResourceOptions, NSError *__autoreleasing * _Nullable)"
+ "initWithDisparityPostprocessingRequest:segmentationPixelBuffer:skinSegmentationPixelBuffer:primaryCaptureRect:applyRotation:destinationAlphaMattePixelBuffer:error:"
+ "initWithFigMetalContext:bufferWidth:bufferHeight:edgeVariance:stepSize:error:"
+ "initWithFigMetalContext:bufferWidth:bufferHeight:error:"
+ "initWithFigMetalContext:commandQueue:error:"
+ "initWithFigMetalContext:commandQueue:kernelSize:error:"
+ "initWithFigMetalContext:commandQueue:textureSize:alphaSize:kernelSize:infConvolutionDownsampling:laplacianLimitingDownsampling:laplacianLimitingBlurSize:error:"
+ "initWithFigMetalContext:error:"
+ "initWithFigMetalContext:textureSize:"
+ "initWithFigMetalContext:textureSize:error:"
+ "initWithSourceColorPixelBuffer:fixedPointDisparityPixelBuffer:destinationDisparityPixelBuffer:focusRegion:focusRegionType:currentFocusPosition:lockFocalPlane:sourceColorPixelBufferOrientation:sourceColorPixelBufferGravity:sourceColorPixelBufferGlobalMotion:facesArray:disparityNormalizationMultiplier:disparityNormalizationOffset:primaryCaptureRect:cropDepthToPrimaryCaptureRect:"
+ "initWithbundle:andOptionalCommandQueue:"
+ "library"
+ "pipelineLibrary"
+ "renderPipelineStateForVertexFunction:vertexDescriptor:fragmentFunction:constants:colorAttachmentDescriptorArrray:depthAttachmentPixelFormat:"
+ "renderWithSrcImage:srcAlpha:trustAlpha:isAfterPreviewStitcher:applyRotation:yuvSourceDownsampled:skinSegmentation:dstImage:faceKitProcessOutput:portraitStyleStrength:colorSim:disparity:focusDistance:singleCubeData:properties:callbackQueue:callback:"
+ "static void KernelReloader::assignAndWatchShader(__strong id<MTLRenderPipelineState>  _Nonnull * _Nonnull, FigMetalContext * _Nonnull __strong, MTLVertexDescriptor * _Nonnull __strong, NSArray<MTLRenderPipelineColorAttachmentDescriptor *> * _Nonnull __strong, MTLPixelFormat, NSError *__autoreleasing  _Nullable * _Nullable, NSString * _Nonnull __strong, NSString * _Nonnull __strong)"
+ "v100@0:8r^{__CVBuffer=}16r^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40r^{VideoMattingStaticParams=BBIIIIIIiiIfffffffffffIIiffff}48r^v56B64B68B72@76@84@?92"
+ "v108@0:8@16@24@32B40@44@52@60f68f72f76f80f84B88f92@96B104"
+ "v132@0:8^{__CVBuffer=}16^{__CVBuffer=}24B32B36B40@44^{__CVBuffer=}52^{__CVBuffer=}60@68f76@80@88f96@100@108@116@?124"
+ "v32@0:8@16B24B28"
+ "v88@0:8@16@24@32@40{CGRect={CGPoint=dd}{CGSize=dd}}48B80B84"
+ "{CVAPhotoMetalContext=\"figMetalContext\"@\"FigMetalContext\"\"device\"@\"<MTLDeviceSPI>\"\"commandQueue\"@\"<MTLCommandQueue>\"\"library\"@\"<MTLLibrary>\"\"pipelineLibrary\"@\"<MTLPipelineLibrarySPI>\"\"captureScope\"@\"<MTLCaptureScope>\"\"profiler\"{unique_ptr<CVAPerfEndTimeProfilerSet, std::default_delete<CVAPerfEndTimeProfilerSet>>=\"__ptr_\"^{CVAPerfEndTimeProfilerSet}}\"_alreadyInCaptureScope\"B}"
+ "{VideoMattingDynamicParams=\"updateRate\"f\"sdofDeltaCanonicalDisparity\"f\"alphaCoeffFilterColorStd\"f\"alphaGammaExponent\"f\"focusCanonicalDisparity\"f\"backgroundCanonicalDisparity\"f\"thresholdHardness\"f\"gravity\"{array<float, 3UL>=\"__elems_\"[3f]}\"alphaMatteDeltaCanonicalDisparity\"f\"primaryCaptureRect\"{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}\"doDisparityHoleFilling\"B\"applyRotation\"B}"
+ "{VideoMattingStaticParams=\"supportsForegroundBlur\"B\"deadzoneInCinematic\"B\"colorWidth\"I\"colorHeight\"I\"shiftWidth\"I\"shiftHeight\"I\"alphaWidth\"I\"alphaHeight\"I\"guidedFilterWidth\"i\"guidedFilterHeight\"i\"kernelSize\"I\"referenceShift\"f\"guidedFilterUnconfidentWeight\"f\"guidedFilterMinDistToDeweight\"f\"alphaMaxLaplacian\"f\"alphaContrastExponent\"f\"shiftFilterColorStd\"f\"shiftFilterUpdateRate\"f\"minimumConfidenceToKeepDisparity\"f\"maximumSimilarityToKeepDisparity\"f\"maxShiftFillingInconsistency\"f\"maxShiftFillingDistFromFg\"f\"maxDistToPushShiftEdgesFwd\"I\"maxDistToPushShiftEdgesRev\"I\"shiftPushingBgToFgShiftDifference\"i\"foregroundMaskDilationRadius\"f\"infConvolutionDownsampling\"f\"laplacianLimitingDownsampling\"f\"laplacianLimitingBlurSize\"f}"
+ "{unique_ptr<DisparityAutofocus, std::default_delete<DisparityAutofocus>>=\"__ptr_\"^{DisparityAutofocus}}"
+ "{unique_ptr<DisparityConversion, std::default_delete<DisparityConversion>>=\"__ptr_\"^{DisparityConversion}}"
+ "{unique_ptr<DisparityStatistics, std::default_delete<DisparityStatistics>>=\"__ptr_\"^{DisparityStatistics}}"
+ "{unique_ptr<FocusStatsPostprocessing, std::default_delete<FocusStatsPostprocessing>>=\"__ptr_\"^{FocusStatsPostprocessing}}"
+ "{unique_ptr<GeometricTransformation, std::default_delete<GeometricTransformation>>=\"__ptr_\"^{GeometricTransformation}}"
+ "{unique_ptr<SdofStateMachine, std::default_delete<SdofStateMachine>>=\"__ptr_\"^{SdofStateMachine}}"
+ "{unique_ptr<StageLightStateMachine, std::default_delete<StageLightStateMachine>>=\"__ptr_\"^{StageLightStateMachine}}"
+ "{unique_ptr<cva::FocusStateMachine, std::default_delete<cva::FocusStateMachine>>=\"__ptr_\"^{FocusStateMachine}}"
+ "{vector<FaceVertex, std::allocator<FaceVertex>>=\"__begin_\"^{FaceVertex}\"__end_\"^{FaceVertex}\"__cap_\"^{FaceVertex}}"
+ "{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__cap_\"^S}"
- "-[CVAMattingRequest initWithDisparityPostprocessingRequest:segmentationPixelBuffer:skinSegmentationPixelBuffer:primaryCaptureRect:destinationAlphaMattePixelBuffer:error:]"
- "-[CVAPortraitVideoPipeline_Impl makeMetalContextWithOptionalCommandQueue:error:]"
- "@100@0:8r^{__CVBuffer=}16r^{__CVBuffer=}24^{__CVBuffer=}32r^{VideoMattingStaticParams=BIIIIIIiiIfffffffffffIIiffff}40r^v48r^{VideoPostprocessingParams=BfBffB}56@64@72B80@84@?92"
- "@120@0:8@16@24@32@40{?=QQQ}48{?=QQQ}72i96i100i104i108^@112"
- "@156@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@40i48f52B56{CVAQuaternion=dddd}60{CVAVector=ddd}92{CVAVector=ddd}116@140f148f152"
- "@56@0:8@16@24@32@40^@48"
- "@56@0:8@16@24@32{CGSize=dd}40"
- "@56@0:8r^{VideoMattingStaticParams=BIIIIIIiiIfffffffffffIIiffff}16f24f28f32B36^v40^@48"
- "@60@0:8@16@24@32@40i48^@52"
- "@64@0:8@16@24@32Q40Q48^@56"
- "@72@0:8@16@24@32Q40Q48f56f60^@64"
- "@72@0:8@16@24@32{?=QQQ}40^@64"
- "Error creating metal library"
- "GaussianPyramid"
- "MPS-prewarming"
- "MPSImageBox"
- "MPSImageLanczosScale"
- "MTLCreateSystemDefaultDevice() is nil"
- "Metal shader compilation warnings: %s"
- "URLForResource:withExtension:"
- "Unable to create function (%@)"
- "Unable to create function (%@): %@"
- "[(_Nonnull id<MTLDeviceSPI>) newCommandQueue] is nil"
- "_isAfterPreviewStitcher"
- "alpha blend"
- "alphaMattingWithPostprocessedDisparity"
- "cvadepth-iOS"
- "device is nil"
- "disparityPostprocessingWithCanonicalDisparity"
- "encodeForegroundMaskToBuffer:disparity:inSegmentation:useSegmentationOnly:weight:foregroundMask:erodedForegroundMask:disparityMin:focusDisparity:hardness:minDistToDeweight:unconfidentWeight:dilateForegroundMask:foregroundMaskDilationRadius:properties:"
- "encodeRelightKernelToCommandBuffer:"
- "encodeToCommandBuffer:srcColorTex:srcAlphaTex:dstForegroundTex:normalizedPrimaryCaptureRect:isAfterPreviewStitcher:"
- "id<MTLComputePipelineState> computeKernel(__strong id<MTLLibrary> _Nonnull, __strong id<MTLPipelineLibrarySPI> _Nonnull, __strong id<MTLDeviceSPI> _Nonnull, NSString *__strong _Nonnull, NSError *__autoreleasing * _Nullable, MTLFunctionConstantValues * _Nullable __strong)"
- "id<MTLFunction> functionFromLibrary(__strong id<MTLLibrary> _Nonnull, __strong id<MTLPipelineLibrarySPI> _Nonnull, NSString *__strong _Nonnull, NSError *__autoreleasing * _Nullable, MTLFunctionConstantValues * _Nullable __strong)"
- "id<MTLTexture> metalTexture(__strong id<MTLDeviceSPI> _Nonnull, MTLPixelFormat, NSUInteger, NSUInteger, MTLResourceOptions, NSError *__autoreleasing * _Nullable)"
- "initWithDevice:library:pipelineLibrary:bufferWidth:bufferHeight:edgeVariance:stepSize:error:"
- "initWithDevice:library:pipelineLibrary:bufferWidth:bufferHeight:error:"
- "initWithDevice:library:pipelineLibrary:commandQueue:error:"
- "initWithDevice:library:pipelineLibrary:commandQueue:kernelSize:error:"
- "initWithDevice:library:pipelineLibrary:commandQueue:textureSize:alphaSize:kernelSize:infConvolutionDownsampling:laplacianLimitingDownsampling:laplacianLimitingBlurSize:error:"
- "initWithDevice:library:pipelineLibrary:error:"
- "initWithDevice:library:pipelineLibrary:textureSize:"
- "initWithDevice:library:pipelineLibrary:textureSize:error:"
- "initWithSourceColorPixelBuffer:fixedPointDisparityPixelBuffer:destinationDisparityPixelBuffer:focusRegion:focusRegionType:currentFocusPosition:lockFocalPlane:sourceColorPixelBufferOrientation:sourceColorPixelBufferGravity:sourceColorPixelBufferGlobalMotion:facesArray:disparityNormalizationMultiplier:disparityNormalizationOffset:"
- "library is nil"
- "metallib"
- "newCommandQueue"
- "newComputePipelineStateWithDescriptor:error:"
- "newFunctionWithName:"
- "newFunctionWithName:constantValues:pipelineLibrary:error:"
- "newLibraryWithURL:error:"
- "newRenderPipelineStateWithDescriptor:error:"
- "perf profiler"
- "renderContinuousWithSource"
- "renderWithSrcImage:srcAlpha:trustAlpha:isAfterPreviewStitcher:yuvSourceDownsampled:skinSegmentation:dstImage:faceKitProcessOutput:portraitStyleStrength:colorSim:disparity:focusDistance:singleCubeData:properties:callbackQueue:callback:"
- "segmentationAverage"
- "setComputeFunction:"
- "setDepthAttachmentPixelFormat:"
- "setFragmentFunction:"
- "setPipelineLibrary:"
- "setThreadGroupSizeIsMultipleOfThreadExecutionWidth:"
- "setVertexDescriptor:"
- "setVertexFunction:"
- "static void KernelReloader::assignAndWatchShader(__strong id<MTLRenderPipelineState>  _Nonnull * _Nonnull, id<MTLLibrary>  _Nonnull __strong, id<MTLPipelineLibrarySPI>  _Nullable __strong, id<MTLDeviceSPI>  _Nonnull __strong, MTLRenderPipelineDescriptor * _Nonnull __strong, NSError *__autoreleasing  _Nullable * _Nullable, NSString * _Nonnull __strong, NSString * _Nonnull __strong)"
- "v100@0:8r^{__CVBuffer=}16r^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40r^{VideoMattingStaticParams=BIIIIIIiiIfffffffffffIIiffff}48r^v56B64B68B72@76@84@?92"
- "v104@0:8@16@24@32B40@44@52@60f68f72f76f80f84B88f92@96"
- "v128@0:8^{__CVBuffer=}16^{__CVBuffer=}24B32B36@40^{__CVBuffer=}48^{__CVBuffer=}56@64f72@76@84f92@96@104@112@?120"
- "v84@0:8@16@24@32@40{CGRect={CGPoint=dd}{CGSize=dd}}48B80"
- "video relighting"
- "{CVAPhotoMetalContext=\"device\"@\"<MTLDeviceSPI>\"\"commandQueue\"@\"<MTLCommandQueue>\"\"library\"@\"<MTLLibrary>\"\"pipelineLibrary\"@\"<MTLPipelineLibrarySPI>\"\"captureScope\"@\"<MTLCaptureScope>\"\"profiler\"{unique_ptr<CVAPerfEndTimeProfilerSet, std::default_delete<CVAPerfEndTimeProfilerSet>>=\"__ptr_\"{__compressed_pair<CVAPerfEndTimeProfilerSet *, std::default_delete<CVAPerfEndTimeProfilerSet>>=\"__value_\"^{CVAPerfEndTimeProfilerSet}}}\"_alreadyInCaptureScope\"B}"
- "{VideoMattingDynamicParams=\"updateRate\"f\"sdofDeltaCanonicalDisparity\"f\"alphaCoeffFilterColorStd\"f\"alphaGammaExponent\"f\"focusCanonicalDisparity\"f\"backgroundCanonicalDisparity\"f\"thresholdHardness\"f\"gravity\"{array<float, 3UL>=\"__elems_\"[3f]}\"alphaMatteDeltaCanonicalDisparity\"f\"primaryCaptureRect\"{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}\"doDisparityHoleFilling\"B}"
- "{VideoMattingStaticParams=\"supportsForegroundBlur\"B\"colorWidth\"I\"colorHeight\"I\"shiftWidth\"I\"shiftHeight\"I\"alphaWidth\"I\"alphaHeight\"I\"guidedFilterWidth\"i\"guidedFilterHeight\"i\"kernelSize\"I\"referenceShift\"f\"guidedFilterUnconfidentWeight\"f\"guidedFilterMinDistToDeweight\"f\"alphaMaxLaplacian\"f\"alphaContrastExponent\"f\"shiftFilterColorStd\"f\"shiftFilterUpdateRate\"f\"minimumConfidenceToKeepDisparity\"f\"maximumSimilarityToKeepDisparity\"f\"maxShiftFillingInconsistency\"f\"maxShiftFillingDistFromFg\"f\"maxDistToPushShiftEdgesFwd\"I\"maxDistToPushShiftEdgesRev\"I\"shiftPushingBgToFgShiftDifference\"i\"foregroundMaskDilationRadius\"f\"infConvolutionDownsampling\"f\"laplacianLimitingDownsampling\"f\"laplacianLimitingBlurSize\"f}"
- "{unique_ptr<DisparityAutofocus, std::default_delete<DisparityAutofocus>>=\"__ptr_\"{__compressed_pair<DisparityAutofocus *, std::default_delete<DisparityAutofocus>>=\"__value_\"^{DisparityAutofocus}}}"
- "{unique_ptr<DisparityConversion, std::default_delete<DisparityConversion>>=\"__ptr_\"{__compressed_pair<DisparityConversion *, std::default_delete<DisparityConversion>>=\"__value_\"^{DisparityConversion}}}"
- "{unique_ptr<DisparityStatistics, std::default_delete<DisparityStatistics>>=\"__ptr_\"{__compressed_pair<DisparityStatistics *, std::default_delete<DisparityStatistics>>=\"__value_\"^{DisparityStatistics}}}"
- "{unique_ptr<FocusStatsPostprocessing, std::default_delete<FocusStatsPostprocessing>>=\"__ptr_\"{__compressed_pair<FocusStatsPostprocessing *, std::default_delete<FocusStatsPostprocessing>>=\"__value_\"^{FocusStatsPostprocessing}}}"
- "{unique_ptr<GeometricTransformation, std::default_delete<GeometricTransformation>>=\"__ptr_\"{__compressed_pair<GeometricTransformation *, std::default_delete<GeometricTransformation>>=\"__value_\"^{GeometricTransformation}}}"
- "{unique_ptr<SdofStateMachine, std::default_delete<SdofStateMachine>>=\"__ptr_\"{__compressed_pair<SdofStateMachine *, std::default_delete<SdofStateMachine>>=\"__value_\"^{SdofStateMachine}}}"
- "{unique_ptr<StageLightStateMachine, std::default_delete<StageLightStateMachine>>=\"__ptr_\"{__compressed_pair<StageLightStateMachine *, std::default_delete<StageLightStateMachine>>=\"__value_\"^{StageLightStateMachine}}}"
- "{unique_ptr<cva::FocusStateMachine, std::default_delete<cva::FocusStateMachine>>=\"__ptr_\"{__compressed_pair<cva::FocusStateMachine *, std::default_delete<cva::FocusStateMachine>>=\"__value_\"^{FocusStateMachine}}}"
- "{vector<FaceVertex, std::allocator<FaceVertex>>=\"__begin_\"^{FaceVertex}\"__end_\"^{FaceVertex}\"__end_cap_\"{__compressed_pair<FaceVertex *, std::allocator<FaceVertex>>=\"__value_\"^{FaceVertex}}}"
- "{vector<unsigned short, std::allocator<unsigned short>>=\"__begin_\"^S\"__end_\"^S\"__end_cap_\"{__compressed_pair<unsigned short *, std::allocator<unsigned short>>=\"__value_\"^S}}"

```
