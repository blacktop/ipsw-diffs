## CoreImage

> `/System/Library/Frameworks/CoreImage.framework/CoreImage`

```diff

-1510.120.2.0.0
-  __TEXT.__text: 0x2be034
-  __TEXT.__auth_stubs: 0x2fa0
-  __TEXT.__objc_methlist: 0x154d0
-  __TEXT.__const: 0xe428
-  __TEXT.__gcc_except_tab: 0x58dc
-  __TEXT.__cstring: 0x84cf9
-  __TEXT.__oslogstring: 0x9db2
-  __TEXT.__dlopen_cstrs: 0x398
-  __TEXT.__runtimeheader: 0xb8ec
+1566.0.0.0.0
+  __TEXT.__text: 0x2d8cec
+  __TEXT.__auth_stubs: 0x2ef0
+  __TEXT.__objc_methlist: 0x14ee8
+  __TEXT.__const: 0xbe98
+  __TEXT.__gcc_except_tab: 0x5df4
+  __TEXT.__cstring: 0x87593
+  __TEXT.__oslogstring: 0xa3fd
+  __TEXT.__dlopen_cstrs: 0x313
+  __TEXT.__runtimeheader: 0xda3c
   __TEXT.__cikl2metal_pre: 0x47f
-  __TEXT.__unwind_info: 0x7058
+  __TEXT.__grain: 0x105040
+  __TEXT.__unwind_info: 0x6fe0
   __TEXT.__eh_frame: 0x208
-  __TEXT.__objc_classname: 0x29e3
-  __TEXT.__objc_methname: 0x21645
-  __TEXT.__objc_methtype: 0x6bc0
-  __TEXT.__objc_stubs: 0x12060
-  __DATA_CONST.__got: 0xa10
-  __DATA_CONST.__const: 0x6bf0
-  __DATA_CONST.__objc_classlist: 0x1010
+  __TEXT.__objc_classname: 0x2a59
+  __TEXT.__objc_methname: 0x202fe
+  __TEXT.__objc_methtype: 0x66c9
+  __TEXT.__objc_stubs: 0x104c0
+  __DATA_CONST.__got: 0xa70
+  __DATA_CONST.__const: 0x7510
+  __DATA_CONST.__objc_classlist: 0x1038
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x8e88
+  __DATA_CONST.__objc_selrefs: 0x88c0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x368
-  __DATA_CONST.__objc_arraydata: 0x1400
-  __AUTH_CONST.__auth_got: 0x17e8
-  __AUTH_CONST.__const: 0xba20
-  __AUTH_CONST.__cfstring: 0x196c0
-  __AUTH_CONST.__objc_const: 0x2b208
-  __AUTH_CONST.__objc_doubleobj: 0x2940
-  __AUTH_CONST.__objc_intobj: 0xd38
-  __AUTH_CONST.__objc_dictobj: 0x438
-  __AUTH_CONST.__objc_floatobj: 0x2d0
-  __AUTH_CONST.__objc_arrayobj: 0x198
-  __AUTH.__objc_data: 0x9920
-  __AUTH.__data: 0x1e090
+  __DATA_CONST.__objc_superrefs: 0x330
+  __DATA_CONST.__objc_arraydata: 0x1490
+  __AUTH_CONST.__auth_got: 0x1790
+  __AUTH_CONST.__const: 0xcc00
+  __AUTH_CONST.__cfstring: 0x19ea0
+  __AUTH_CONST.__objc_const: 0x2a528
+  __AUTH_CONST.__objc_intobj: 0xd98
+  __AUTH_CONST.__objc_dictobj: 0x410
+  __AUTH_CONST.__objc_doubleobj: 0x29b0
+  __AUTH_CONST.__objc_floatobj: 0x2e0
+  __AUTH_CONST.__objc_arrayobj: 0x1b0
+  __AUTH.__objc_data: 0x9ab0
+  __AUTH.__data: 0x1de50
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x20a0
-  __DATA.__data: 0x57f8
-  __DATA.__bss: 0x3818
-  __DATA.__common: 0x50
+  __DATA.__objc_ivar: 0x1f0c
+  __DATA.__data: 0x5798
+  __DATA.__bss: 0x37c0
+  __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x4
-  __DATA_DIRTY.__crash_info: 0x40
-  __DATA_DIRTY.__bss: 0x5f8
-  __DATA_DIRTY.__common: 0x1d0
+  __DATA_DIRTY.__crash_info: 0x148
+  __DATA_DIRTY.__bss: 0x650
+  __DATA_DIRTY.__common: 0x1e8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/ColorSync.framework/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 135DC7DD-D744-387C-8445-7906BF64AA6E
-  Functions: 13875
-  Symbols:   43161
-  CStrings:  18156
+  UUID: 2E1B1319-85CC-332B-96BF-36EF1F515139
+  Functions: 13913
+  Symbols:   43130
+  CStrings:  17992
 
Symbols:
+ +[CIAreaAverageMaximumRed customAttributes]
+ +[CIAreaAverageProcessor onlyUsesMetal]
+ +[CIBarcodeDetector messageStringFromDescriptor:]
+ +[CIBarcodeDetector messageStringFromDescriptor:].cold.1
+ +[CIBarcodeDetector messageStringFromDescriptor:].cold.2
+ +[CIBlurredRoundedRectangleGenerator customAttributes]
+ +[CIContext isMetalAvailable]
+ +[CIContext isOpenCLAvailable]
+ +[CIConvolutionProcessor onlyUsesMetal]
+ +[CIDisparitySmoothingProcessor onlyUsesMetal]
+ +[CIFaceMaskKernel onlyUsesMetal]
+ +[CIFilter(Builtins) areaAverageMaximumRedFilter]
+ +[CIFilter(Builtins) blurredRoundedRectangleGeneratorFilter]
+ +[CIFilter(Builtins) distanceGradientFromRedMaskFilter]
+ +[CIFilter(Builtins) roundedQRCodeGeneratorFilter]
+ +[CIFilter(Builtins) signedDistanceGradientFromRedMaskFilter]
+ +[CIFilter(Builtins) systemToneMapFilter]
+ +[CIFocalPlaneProcessor onlyUsesMetal]
+ +[CIHighlightRecoveryProcessor onlyUsesMetal]
+ +[CIImage(CIImageProcessor) imageWithExtent:processorDescription:argumentDigest:outputFormat:options:processor:]
+ +[CIImage(CIImageProcessor) imageWithExtent:processorDescription:argumentDigest:outputFormat:options:processor:].cold.1
+ +[CIImage(CIImageProcessor) imageWithExtent:processorDescription:argumentDigest:outputFormat:options:processor:].cold.2
+ +[CIImageProcessorKernel _call_formatForInputAtIndex:arguments:]
+ +[CIImageProcessorKernel _call_outputFormatWithArguments:]
+ +[CIImageProcessorKernel applyWithExtents:inputs:arguments:error:]
+ +[CIImageProcessorKernel onlyUsesMetal]
+ +[CIImageProcessorKernel outputFormatAtIndex:arguments:]
+ +[CIImageProcessorKernel processWithInputs:arguments:outputs:error:]
+ +[CIIntegralImageProcessorGPU onlyUsesMetal]
+ +[CIIntegralImageProcessorGPU synchronizeInputs]
+ +[CIKernel kernelsWithString:andCIKernelLibrary:messageLog:].cold.1
+ +[CIKernelLibrary(Internal) internalBinaryArchiveWithName:device:]
+ +[CIKernelLibrary(Internal) internalBinaryArchiveWithName:device:].cold.1
+ +[CIKernelLibrary(Internal) internalBinaryArchiveWithName:device:].cold.2
+ +[CIMattingRGBDProcessor onlyUsesMetal]
+ +[CIMedianProcessor onlyUsesMetal]
+ +[CIMorphologyProcessor onlyUsesMetal]
+ +[CISignedDistanceGradientFromRedMask customAttributes]
+ +[CISystemToneMap customAttributes]
+ +[CIToneMapInternal customAttributes]
+ +[CUIGlow customAttributes]
+ -[CIAreaAverageMaximumRed _reduce1X4]
+ -[CIAreaAverageMaximumRed _reduce2X2]
+ -[CIAreaAverageMaximumRed _reduce4X1]
+ -[CIAreaAverageMaximumRed _reduce4X4]
+ -[CIAreaAverageMaximumRed _reduceCrop]
+ -[CIAreaAverageMaximumRed outputImage]
+ -[CIAreaHistogram _inputsAreOK].cold.1
+ -[CIAreaHistogram _inputsAreOK].cold.2
+ -[CIAreaHistogram _inputsAreOK].cold.3
+ -[CIAreaHistogram outputData].cold.1
+ -[CIBarcodeDetector featuresInImage:options:].cold.1
+ -[CIBarcodeDetector initWithContext:options:].cold.1
+ -[CIBlendKernel extentType]
+ -[CIBlurredRoundedRectangleGenerator inputColor]
+ -[CIBlurredRoundedRectangleGenerator inputExtent]
+ -[CIBlurredRoundedRectangleGenerator inputRadius]
+ -[CIBlurredRoundedRectangleGenerator inputSigma]
+ -[CIBlurredRoundedRectangleGenerator inputSmoothness]
+ -[CIBlurredRoundedRectangleGenerator outputImage]
+ -[CIBlurredRoundedRectangleGenerator setInputColor:]
+ -[CIBlurredRoundedRectangleGenerator setInputExtent:]
+ -[CIBlurredRoundedRectangleGenerator setInputRadius:]
+ -[CIBlurredRoundedRectangleGenerator setInputSigma:]
+ -[CIBlurredRoundedRectangleGenerator setInputSmoothness:]
+ -[CIColorKernel preservesOpacity]
+ -[CIConstColor copyWithZone:]
+ -[CIContext(CIRenderDestination) _startTaskToRender:toDestination:forPrepareRender:forClear:error:].cold.10
+ -[CIContext(CIRenderDestination) _startTaskToRender:toDestination:forPrepareRender:forClear:error:].cold.7
+ -[CIContext(CIRenderDestination) _startTaskToRender:toDestination:forPrepareRender:forClear:error:].cold.8
+ -[CIContext(CIRenderDestination) _startTaskToRender:toDestination:forPrepareRender:forClear:error:].cold.9
+ -[CIContext(CalculateHDRStats) calculateHDRStatsForCGImage:]
+ -[CIContext(CalculateHDRStats) calculateHDRStatsForCVPixelBuffer:]
+ -[CIContext(CalculateHDRStats) calculateHDRStatsForIOSurface:]
+ -[CIContext(CalculateHDRStats) calculateHDRStatsForImage:]
+ -[CIContext(CalculateHDRStats) calculateHDRStatsForImage:].cold.1
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:]
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.1
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.10
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.11
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.12
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.13
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.14
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.15
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.2
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.3
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.4
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.5
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.6
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.7
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.8
+ -[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:].cold.9
+ -[CIContext(ImageRepresentation) _addDepthMap:session:imageHandle:options:]
+ -[CIContext(ImageRepresentation) _addDepthMap:session:imageHandle:options:].cold.1
+ -[CIContext(ImageRepresentation) _addGainMap:session:imageHandle:containerFormat:options:orientation:]
+ -[CIContext(ImageRepresentation) _addGainMap:session:imageHandle:containerFormat:options:orientation:].cold.1
+ -[CIContext(ImageRepresentation) _addGainMap:session:imageHandle:containerFormat:options:orientation:].cold.2
+ -[CIContext(ImageRepresentation) _addGainMap:session:imageHandle:containerFormat:options:orientation:].cold.3
+ -[CIContext(ImageRepresentation) _addGainMap:session:imageHandle:containerFormat:options:orientation:].cold.4
+ -[CIContext(ImageRepresentation) _addPortraitMatte:session:imageHandle:options:]
+ -[CIContext(ImageRepresentation) _addPortraitMatte:session:imageHandle:options:].cold.1
+ -[CIContext(ImageRepresentation) _addPortraitMatte:session:imageHandle:options:].cold.2
+ -[CIContext(ImageRepresentation) _addPortraitMatte:session:imageHandle:options:].cold.3
+ -[CIContext(ImageRepresentation) _addSemanticImages:session:imageHandle:options:]
+ -[CIContext(ImageRepresentation) _addSemanticImages:session:imageHandle:options:].cold.1
+ -[CIContext(ImageRepresentation) _addSemanticImages:session:imageHandle:options:].cold.2
+ -[CIContext(ImageRepresentation) _addSemanticImages:session:imageHandle:options:].cold.3
+ -[CIContext(ImageRepresentation) _addSemanticImages:session:imageHandle:options:].cold.4
+ -[CIContext(ImageRepresentation) _addSemanticImages:session:imageHandle:options:].cold.5
+ -[CIContext(ImageRepresentation) _dataRepresentationOfImage:UTIType:format:premultiplied:colorSpace:options:addAuxData:keysToMerge:error:].cold.1
+ -[CIContext(ImageRepresentation) _dataRepresentationOfImage:UTIType:format:premultiplied:colorSpace:options:addAuxData:keysToMerge:error:].cold.2
+ -[CIContext(ImageRepresentationPrivate) gainMapImageForSDR:HDR:colorSpace:rgbGainmap:]
+ -[CIContext(Internal) _internalFallbackCL]
+ -[CIContext(createCGImage) createCGImage:fromRect:format:colorSpace:deferred:calculateHDRStats:]
+ -[CIImage _imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:constrainedHigh:]
+ -[CIImage _imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:constrainedHigh:].cold.1
+ -[CIImage _imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:constrainedHigh:].cold.2
+ -[CIImage _originalIOSurface]
+ -[CIImage _setOriginalSurface:options:]
+ -[CIImage contentAverageLightLevel]
+ -[CIImage imageByInsertingTiledIntermediate]
+ -[CIImage imageBySettingContentAverageLightLevel:]
+ -[CIImage imageBySettingContentAverageLightLevel:].cold.1
+ -[CIImage imageBySettingContentHeadroom:]
+ -[CIImage imageBySettingContentHeadroom:].cold.1
+ -[CIImage imageBySettingDepthData:]
+ -[CIImage imageBySettingDepthData:].cold.1
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:]
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:].cold.1
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:].cold.2
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:].cold.3
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:].cold.4
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:].cold.5
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:].cold.6
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:].cold.7
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:].cold.8
+ -[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:].cold.9
+ -[CIImage(CIImageProvider) initWithImageTextureProvider:width:height:format:colorSpace:options:]
+ -[CIImage(QuicklookSupport) _dotStringRepresentation]
+ -[CIImageProcessorInOut initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:]
+ -[CIImageProcessorInOut initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:].cold.1
+ -[CIImageProcessorInput baseAddress].cold.3
+ -[CIImageProcessorInput initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:]
+ -[CIImageProcessorInput initWithSurface:texture:digest:allowSRGB:bounds:roiTileIndex:roiTileCount:onlyMetal:context:]
+ -[CIImageProcessorInput surface]
+ -[CIImageProcessorInput surface].cold.1
+ -[CIImageProcessorOutput baseAddress].cold.3
+ -[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:tileTask:]
+ -[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:tileTask:].cold.1
+ -[CIImageProcessorOutput surface]
+ -[CIImageProcessorOutput surface].cold.1
+ -[CIKMeans outputImage].cold.3
+ -[CIKMeans outputImage].cold.4
+ -[CIKernel _initWithString:andCIKernelLibrary:usingCruftCompatibility:isInternal:].cold.8
+ -[CIKernel preservesOpacity]
+ -[CIKernelLibrary refelectionWithFunctionName:]
+ -[CIPhotoGrain outputImage].cold.1
+ -[CIReductionFilter offsetAndCrop].cold.1
+ -[CIReductionFilter offsetAndCrop].cold.2
+ -[CIRenderDestination _render:withContext:].cold.1
+ -[CIRenderDestination captureTraceURL]
+ -[CIRenderDestination setCaptureTraceURL:]
+ -[CIRoundedRectangleGenerator inputSmoothness]
+ -[CIRoundedRectangleGenerator setInputSmoothness:]
+ -[CIRoundedRectangleStrokeGenerator inputSmoothness]
+ -[CIRoundedRectangleStrokeGenerator setInputSmoothness:]
+ -[CISignedDistanceGradientFromRedMask inputImage]
+ -[CISignedDistanceGradientFromRedMask inputMaximumDistance]
+ -[CISignedDistanceGradientFromRedMask outputImage]
+ -[CISignedDistanceGradientFromRedMask outputImage].cold.1
+ -[CISignedDistanceGradientFromRedMask outputImage].cold.2
+ -[CISignedDistanceGradientFromRedMask setInputImage:]
+ -[CISignedDistanceGradientFromRedMask setInputMaximumDistance:]
+ -[CISystemToneMap inputDisplayHeadroom]
+ -[CISystemToneMap inputImage]
+ -[CISystemToneMap inputPreferredDynamicRange]
+ -[CISystemToneMap outputImage]
+ -[CISystemToneMap setInputDisplayHeadroom:]
+ -[CISystemToneMap setInputImage:]
+ -[CISystemToneMap setInputPreferredDynamicRange:]
+ -[CIToneMapInternal inputHighlightsTradeOffRatio]
+ -[CIToneMapInternal inputImage]
+ -[CIToneMapInternal inputMinimumGammaAdjustment]
+ -[CIToneMapInternal inputMinimumSDRExposure]
+ -[CIToneMapInternal inputOffsetAnchor]
+ -[CIToneMapInternal inputPreferredDynamicRange]
+ -[CIToneMapInternal inputSourceHeadroom]
+ -[CIToneMapInternal inputStopAnchor]
+ -[CIToneMapInternal inputTargetHeadroom]
+ -[CIToneMapInternal outputImage]
+ -[CIToneMapInternal outputValue:]
+ -[CIToneMapInternal setInputHighlightsTradeOffRatio:]
+ -[CIToneMapInternal setInputImage:]
+ -[CIToneMapInternal setInputMinimumGammaAdjustment:]
+ -[CIToneMapInternal setInputMinimumSDRExposure:]
+ -[CIToneMapInternal setInputOffsetAnchor:]
+ -[CIToneMapInternal setInputPreferredDynamicRange:]
+ -[CIToneMapInternal setInputSourceHeadroom:]
+ -[CIToneMapInternal setInputStopAnchor:]
+ -[CIToneMapInternal setInputTargetHeadroom:]
+ -[CIToneMapInternal srcHeadroom]
+ -[CIToneMapInternal targetHeadroom]
+ -[CIWarpKernel preservesOpacity]
+ -[CUIClampHDR inputImage]
+ -[CUIClampHDR inputMaxComponent]
+ -[CUIClampHDR outputImage]
+ -[CUIClampHDR setInputImage:]
+ -[CUIClampHDR setInputMaxComponent:]
+ -[CUIComputeNormals inputImage]
+ -[CUIComputeNormals outputImage]
+ -[CUIComputeNormals setInputImage:]
+ -[CUIDfDxDfDy inputChannel]
+ -[CUIDfDxDfDy inputImage]
+ -[CUIDfDxDfDy outputImage]
+ -[CUIDfDxDfDy setInputChannel:]
+ -[CUIDfDxDfDy setInputImage:]
+ -[CUIFWidth inputImage]
+ -[CUIFWidth outputImage]
+ -[CUIFWidth setInputImage:]
+ -[CUIGatherSDF inputAbove]
+ -[CUIGatherSDF inputBelow]
+ -[CUIGatherSDF inputImage]
+ -[CUIGatherSDF outputImage]
+ -[CUIGatherSDF setInputAbove:]
+ -[CUIGatherSDF setInputBelow:]
+ -[CUIGatherSDF setInputImage:]
+ -[CUIGlassHighlight _kernel]
+ -[CUIGlassHighlight outputImage]
+ -[CUIGlassHighlightFromAlpha _kernel]
+ -[CUIGlassHighlightFromAlpha outputImage]
+ -[CUIGlassHighlightInternal _kernel]
+ -[CUIGlassHighlightInternal inputAngleSinCos]
+ -[CUIGlassHighlightInternal inputBiasAmount]
+ -[CUIGlassHighlightInternal inputColor]
+ -[CUIGlassHighlightInternal inputCurvature]
+ -[CUIGlassHighlightInternal inputHeight]
+ -[CUIGlassHighlightInternal inputImage]
+ -[CUIGlassHighlightInternal inputInset]
+ -[CUIGlassHighlightInternal inputSDFScaleFactor]
+ -[CUIGlassHighlightInternal inputSDFZeroValue]
+ -[CUIGlassHighlightInternal inputSpread]
+ -[CUIGlassHighlightInternal outputImage]
+ -[CUIGlassHighlightInternal setInputAngleSinCos:]
+ -[CUIGlassHighlightInternal setInputBiasAmount:]
+ -[CUIGlassHighlightInternal setInputColor:]
+ -[CUIGlassHighlightInternal setInputCurvature:]
+ -[CUIGlassHighlightInternal setInputHeight:]
+ -[CUIGlassHighlightInternal setInputImage:]
+ -[CUIGlassHighlightInternal setInputInset:]
+ -[CUIGlassHighlightInternal setInputSDFScaleFactor:]
+ -[CUIGlassHighlightInternal setInputSDFZeroValue:]
+ -[CUIGlassHighlightInternal setInputSpread:]
+ -[CUIGlow inputBiasAmount]
+ -[CUIGlow inputColor]
+ -[CUIGlow inputImage]
+ -[CUIGlow inputMaskOpposite]
+ -[CUIGlow inputRadius]
+ -[CUIGlow inputSDFScale]
+ -[CUIGlow inputSDFZero]
+ -[CUIGlow outputImage]
+ -[CUIGlow setInputBiasAmount:]
+ -[CUIGlow setInputColor:]
+ -[CUIGlow setInputImage:]
+ -[CUIGlow setInputMaskOpposite:]
+ -[CUIGlow setInputRadius:]
+ -[CUIGlow setInputSDFScale:]
+ -[CUIGlow setInputSDFZero:]
+ -[CUINarrowBlur15 inputImage]
+ -[CUINarrowBlur15 outputImage]
+ -[CUINarrowBlur15 setInputImage:]
+ -[CUISDFClamp inputFrame]
+ -[CUISDFClamp inputImage]
+ -[CUISDFClamp outputImage]
+ -[CUISDFClamp setInputFrame:]
+ -[CUISDFClamp setInputImage:]
+ -[CUISDFFill inputBias]
+ -[CUISDFFill inputImage]
+ -[CUISDFFill inputScale]
+ -[CUISDFFill outputImage]
+ -[CUISDFFill setInputBias:]
+ -[CUISDFFill setInputImage:]
+ -[CUISDFFill setInputScale:]
+ -[CUIShapeAwareGradientMask inputBorderWidth]
+ -[CUIShapeAwareGradientMask inputImage]
+ -[CUIShapeAwareGradientMask inputLength]
+ -[CUIShapeAwareGradientMask inputLightDirection]
+ -[CUIShapeAwareGradientMask inputMinOpacity]
+ -[CUIShapeAwareGradientMask inputOpaqueEnd]
+ -[CUIShapeAwareGradientMask inputSDFScale]
+ -[CUIShapeAwareGradientMask inputSDFZero]
+ -[CUIShapeAwareGradientMask outputImage]
+ -[CUIShapeAwareGradientMask setInputBorderWidth:]
+ -[CUIShapeAwareGradientMask setInputImage:]
+ -[CUIShapeAwareGradientMask setInputLength:]
+ -[CUIShapeAwareGradientMask setInputLightDirection:]
+ -[CUIShapeAwareGradientMask setInputMinOpacity:]
+ -[CUIShapeAwareGradientMask setInputOpaqueEnd:]
+ -[CUIShapeAwareGradientMask setInputSDFScale:]
+ -[CUIShapeAwareGradientMask setInputSDFZero:]
+ -[CUISignedDistanceField _remappingKernel]
+ -[CUISignedDistanceField inputImage]
+ -[CUISignedDistanceField inputMaxDistance]
+ -[CUISignedDistanceField outputImage]
+ -[CUISignedDistanceField setInputImage:]
+ -[CUISignedDistanceField setInputMaxDistance:]
+ -[CUISimplifiedShapeAwareGradientMask inputBorderWidth]
+ -[CUISimplifiedShapeAwareGradientMask inputBounds]
+ -[CUISimplifiedShapeAwareGradientMask inputContourOpacityBounds]
+ -[CUISimplifiedShapeAwareGradientMask inputImage]
+ -[CUISimplifiedShapeAwareGradientMask inputOpacityBounds]
+ -[CUISimplifiedShapeAwareGradientMask inputSDFScale]
+ -[CUISimplifiedShapeAwareGradientMask inputSDFZero]
+ -[CUISimplifiedShapeAwareGradientMask outputImage]
+ -[CUISimplifiedShapeAwareGradientMask setInputBorderWidth:]
+ -[CUISimplifiedShapeAwareGradientMask setInputBounds:]
+ -[CUISimplifiedShapeAwareGradientMask setInputContourOpacityBounds:]
+ -[CUISimplifiedShapeAwareGradientMask setInputImage:]
+ -[CUISimplifiedShapeAwareGradientMask setInputOpacityBounds:]
+ -[CUISimplifiedShapeAwareGradientMask setInputSDFScale:]
+ -[CUISimplifiedShapeAwareGradientMask setInputSDFZero:]
+ -[DOTRenderer stringContents]
+ GCC_except_table113
+ GCC_except_table115
+ GCC_except_table118
+ GCC_except_table129
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table154
+ GCC_except_table156
+ GCC_except_table158
+ GCC_except_table159
+ GCC_except_table160
+ GCC_except_table161
+ GCC_except_table171
+ GCC_except_table177
+ GCC_except_table183
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table192
+ GCC_except_table196
+ GCC_except_table197
+ GCC_except_table200
+ GCC_except_table208
+ GCC_except_table220
+ GCC_except_table221
+ GCC_except_table223
+ GCC_except_table228
+ GCC_except_table230
+ GCC_except_table238
+ GCC_except_table240
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table254
+ GCC_except_table261
+ GCC_except_table265
+ GCC_except_table278
+ GCC_except_table281
+ GCC_except_table284
+ GCC_except_table285
+ GCC_except_table289
+ GCC_except_table307
+ GCC_except_table313
+ GCC_except_table317
+ GCC_except_table322
+ GCC_except_table327
+ GCC_except_table332
+ GCC_except_table337
+ GCC_except_table354
+ GCC_except_table403
+ GCC_except_table408
+ GCC_except_table420
+ GCC_except_table421
+ GCC_except_table433
+ GCC_except_table434
+ GCC_except_table461
+ GCC_except_table462
+ GCC_except_table464
+ GCC_except_table76
+ _AVFCaptureLibrary
+ _AVFCaptureLibrary.cold.1
+ _AVFCaptureLibraryCore.frameworkLibrary
+ _ArchiveLibraryUsingDescriptor
+ _CGCFDictionaryGetFloatWithDefault
+ _CGColorSpaceCreateWithID
+ _CGColorSpaceGetID
+ _CGImageCreateCopyWithContentHeadroom
+ _CGImageGetContentAverageLightLevelNits
+ _CIGVRendererCreateDOTRenderer
+ _CIGVRendererFlushRender
+ _CIGVRendererGetString
+ _CIMetalTextureWriteToFile
+ _CIRAWDecoderVersion9
+ _CIRAWDecoderVersion9DNG
+ _CI_ALLOW_UBER_SHADER_COMPILATION
+ _CI_ARCHIVE_USAGE_MODE
+ _CI_CACHE_TILE_SIZE
+ _CI_ENABLE_METAL_FUNCTION_ATTRIBUTES
+ _CI_ENABLE_UBER_SHADER
+ _CI_USE_AIR_UBER_SHADER
+ _CI_WAIT_BEFORE_SWITCHING_TO_UBER
+ _ContextIsUsable
+ _ContextIsUsable.cold.1
+ _ContextIsUsable.cold.2
+ _CopyAnyImagePeakNonVolatileList
+ _CopyAnyImagePeakNonVolatileList.cold.1
+ _CopyContextPeakNonVolatileList
+ _CopyContextPeakNonVolatileList.cold.1
+ _CoreImageBuildVersionString
+ _CreateDirectProvider
+ _CreateUberComputePipelineState
+ _CreateUberComputePipelineState.cold.1
+ _FOSL_DAG_CODEGEN
+ _FutharkLibraryCore
+ _FutharkLibraryCore.frameworkLibrary
+ _GetPixelBufferCleanAperture
+ _GetSurfaceCleanAperture
+ _IOSurfaceGetTypeID
+ _OBJC_CLASS_$_CIAreaAverageMaximumRed
+ _OBJC_CLASS_$_CIBlurredRoundedRectangleGenerator
+ _OBJC_CLASS_$_CISignedDistanceGradientFromRedMask
+ _OBJC_CLASS_$_CISystemToneMap
+ _OBJC_CLASS_$_CIToneMapInternal
+ _OBJC_CLASS_$_CUIClampHDR
+ _OBJC_CLASS_$_CUIComputeNormals
+ _OBJC_CLASS_$_CUIDfDxDfDy
+ _OBJC_CLASS_$_CUIFWidth
+ _OBJC_CLASS_$_CUIGatherSDF
+ _OBJC_CLASS_$_CUIGlassHighlight
+ _OBJC_CLASS_$_CUIGlassHighlightFromAlpha
+ _OBJC_CLASS_$_CUIGlassHighlightInternal
+ _OBJC_CLASS_$_CUIGlow
+ _OBJC_CLASS_$_CUINarrowBlur15
+ _OBJC_CLASS_$_CUISDFClamp
+ _OBJC_CLASS_$_CUISDFFill
+ _OBJC_CLASS_$_CUIShapeAwareGradientMask
+ _OBJC_CLASS_$_CUISignedDistanceField
+ _OBJC_CLASS_$_CUISimplifiedShapeAwareGradientMask
+ _OBJC_CLASS_$_MTLCaptureDescriptor
+ _OBJC_CLASS_$_MTLFunctionStitchingFunctionNodeSPI
+ _OBJC_CLASS_$_MTLLinkedFunctions
+ _OBJC_CLASS_$_MTLVisibleFunctionTableDescriptor
+ _OBJC_CLASS_$__MTLBinaryArchive
+ _OBJC_IVAR_$_CIBlurredRoundedRectangleGenerator.inputColor
+ _OBJC_IVAR_$_CIBlurredRoundedRectangleGenerator.inputExtent
+ _OBJC_IVAR_$_CIBlurredRoundedRectangleGenerator.inputRadius
+ _OBJC_IVAR_$_CIBlurredRoundedRectangleGenerator.inputSigma
+ _OBJC_IVAR_$_CIBlurredRoundedRectangleGenerator.inputSmoothness
+ _OBJC_IVAR_$_CIImageProcessorInOut._onlyMetal
+ _OBJC_IVAR_$_CIRenderDestination.captureTraceURL
+ _OBJC_IVAR_$_CIRoundedRectangleGenerator.inputSmoothness
+ _OBJC_IVAR_$_CIRoundedRectangleStrokeGenerator.inputSmoothness
+ _OBJC_IVAR_$_CISignedDistanceGradientFromRedMask.inputImage
+ _OBJC_IVAR_$_CISignedDistanceGradientFromRedMask.inputMaximumDistance
+ _OBJC_IVAR_$_CISystemToneMap.inputDisplayHeadroom
+ _OBJC_IVAR_$_CISystemToneMap.inputImage
+ _OBJC_IVAR_$_CISystemToneMap.inputPreferredDynamicRange
+ _OBJC_IVAR_$_CIToneMapInternal.inputHighlightsTradeOffRatio
+ _OBJC_IVAR_$_CIToneMapInternal.inputImage
+ _OBJC_IVAR_$_CIToneMapInternal.inputMinimumGammaAdjustment
+ _OBJC_IVAR_$_CIToneMapInternal.inputMinimumSDRExposure
+ _OBJC_IVAR_$_CIToneMapInternal.inputOffsetAnchor
+ _OBJC_IVAR_$_CIToneMapInternal.inputPreferredDynamicRange
+ _OBJC_IVAR_$_CIToneMapInternal.inputSourceHeadroom
+ _OBJC_IVAR_$_CIToneMapInternal.inputStopAnchor
+ _OBJC_IVAR_$_CIToneMapInternal.inputTargetHeadroom
+ _OBJC_IVAR_$_CUIClampHDR.inputImage
+ _OBJC_IVAR_$_CUIClampHDR.inputMaxComponent
+ _OBJC_IVAR_$_CUIComputeNormals.inputImage
+ _OBJC_IVAR_$_CUIDfDxDfDy.inputChannel
+ _OBJC_IVAR_$_CUIDfDxDfDy.inputImage
+ _OBJC_IVAR_$_CUIFWidth.inputImage
+ _OBJC_IVAR_$_CUIGatherSDF.inputAbove
+ _OBJC_IVAR_$_CUIGatherSDF.inputBelow
+ _OBJC_IVAR_$_CUIGatherSDF.inputImage
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputAngleSinCos
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputBiasAmount
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputColor
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputCurvature
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputHeight
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputImage
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputInset
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputSDFScaleFactor
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputSDFZeroValue
+ _OBJC_IVAR_$_CUIGlassHighlightInternal.inputSpread
+ _OBJC_IVAR_$_CUIGlow.inputBiasAmount
+ _OBJC_IVAR_$_CUIGlow.inputColor
+ _OBJC_IVAR_$_CUIGlow.inputImage
+ _OBJC_IVAR_$_CUIGlow.inputMaskOpposite
+ _OBJC_IVAR_$_CUIGlow.inputRadius
+ _OBJC_IVAR_$_CUIGlow.inputSDFScale
+ _OBJC_IVAR_$_CUIGlow.inputSDFZero
+ _OBJC_IVAR_$_CUINarrowBlur15.inputImage
+ _OBJC_IVAR_$_CUISDFClamp.inputFrame
+ _OBJC_IVAR_$_CUISDFClamp.inputImage
+ _OBJC_IVAR_$_CUISDFFill.inputBias
+ _OBJC_IVAR_$_CUISDFFill.inputImage
+ _OBJC_IVAR_$_CUISDFFill.inputScale
+ _OBJC_IVAR_$_CUIShapeAwareGradientMask.inputBorderWidth
+ _OBJC_IVAR_$_CUIShapeAwareGradientMask.inputImage
+ _OBJC_IVAR_$_CUIShapeAwareGradientMask.inputLength
+ _OBJC_IVAR_$_CUIShapeAwareGradientMask.inputLightDirection
+ _OBJC_IVAR_$_CUIShapeAwareGradientMask.inputMinOpacity
+ _OBJC_IVAR_$_CUIShapeAwareGradientMask.inputOpaqueEnd
+ _OBJC_IVAR_$_CUIShapeAwareGradientMask.inputSDFScale
+ _OBJC_IVAR_$_CUIShapeAwareGradientMask.inputSDFZero
+ _OBJC_IVAR_$_CUISignedDistanceField.inputImage
+ _OBJC_IVAR_$_CUISignedDistanceField.inputMaxDistance
+ _OBJC_IVAR_$_CUISimplifiedShapeAwareGradientMask.inputBorderWidth
+ _OBJC_IVAR_$_CUISimplifiedShapeAwareGradientMask.inputBounds
+ _OBJC_IVAR_$_CUISimplifiedShapeAwareGradientMask.inputContourOpacityBounds
+ _OBJC_IVAR_$_CUISimplifiedShapeAwareGradientMask.inputImage
+ _OBJC_IVAR_$_CUISimplifiedShapeAwareGradientMask.inputOpacityBounds
+ _OBJC_IVAR_$_CUISimplifiedShapeAwareGradientMask.inputSDFScale
+ _OBJC_IVAR_$_CUISimplifiedShapeAwareGradientMask.inputSDFZero
+ _OBJC_IVAR_$_DOTRenderer.contents
+ _OBJC_METACLASS_$_CIAreaAverageMaximumRed
+ _OBJC_METACLASS_$_CIBlurredRoundedRectangleGenerator
+ _OBJC_METACLASS_$_CISignedDistanceGradientFromRedMask
+ _OBJC_METACLASS_$_CISystemToneMap
+ _OBJC_METACLASS_$_CIToneMapInternal
+ _OBJC_METACLASS_$_CUIClampHDR
+ _OBJC_METACLASS_$_CUIComputeNormals
+ _OBJC_METACLASS_$_CUIDfDxDfDy
+ _OBJC_METACLASS_$_CUIFWidth
+ _OBJC_METACLASS_$_CUIGatherSDF
+ _OBJC_METACLASS_$_CUIGlassHighlight
+ _OBJC_METACLASS_$_CUIGlassHighlightFromAlpha
+ _OBJC_METACLASS_$_CUIGlassHighlightInternal
+ _OBJC_METACLASS_$_CUIGlow
+ _OBJC_METACLASS_$_CUINarrowBlur15
+ _OBJC_METACLASS_$_CUISDFClamp
+ _OBJC_METACLASS_$_CUISDFFill
+ _OBJC_METACLASS_$_CUIShapeAwareGradientMask
+ _OBJC_METACLASS_$_CUISignedDistanceField
+ _OBJC_METACLASS_$_CUISimplifiedShapeAwareGradientMask
+ _PlaneReadOnlyBlock
+ _SetCurrentContext
+ _SetCurrentContext.cold.1
+ _VisionLibraryCore
+ __OBJC_$_CLASS_METHODS_CIAreaAverageMaximumRed
+ __OBJC_$_CLASS_METHODS_CIBarcodeDetector
+ __OBJC_$_CLASS_METHODS_CIBlurredRoundedRectangleGenerator
+ __OBJC_$_CLASS_METHODS_CIContext(CalculateHDRStats|Internal|_createClone|QuicklookSupport|_createCached|_createCGImageInternal|createCGImageInternal|createCGImage|ImageRepresentationPrivate|ImageRepresentation|CIDepthBlurEffect|CIRenderDestination)
+ __OBJC_$_CLASS_METHODS_CISignedDistanceGradientFromRedMask
+ __OBJC_$_CLASS_METHODS_CISystemToneMap
+ __OBJC_$_CLASS_METHODS_CIToneMapInternal
+ __OBJC_$_CLASS_METHODS_CUIGlow
+ __OBJC_$_INSTANCE_METHODS_CIAreaAverageMaximumRed
+ __OBJC_$_INSTANCE_METHODS_CIBlurredRoundedRectangleGenerator
+ __OBJC_$_INSTANCE_METHODS_CIContext(CalculateHDRStats|Internal|_createClone|QuicklookSupport|_createCached|_createCGImageInternal|createCGImageInternal|createCGImage|ImageRepresentationPrivate|ImageRepresentation|CIDepthBlurEffect|CIRenderDestination)
+ __OBJC_$_INSTANCE_METHODS_CISignedDistanceGradientFromRedMask
+ __OBJC_$_INSTANCE_METHODS_CISystemToneMap
+ __OBJC_$_INSTANCE_METHODS_CIToneMapInternal
+ __OBJC_$_INSTANCE_METHODS_CUIClampHDR
+ __OBJC_$_INSTANCE_METHODS_CUIComputeNormals
+ __OBJC_$_INSTANCE_METHODS_CUIDfDxDfDy
+ __OBJC_$_INSTANCE_METHODS_CUIFWidth
+ __OBJC_$_INSTANCE_METHODS_CUIGatherSDF
+ __OBJC_$_INSTANCE_METHODS_CUIGlassHighlight
+ __OBJC_$_INSTANCE_METHODS_CUIGlassHighlightFromAlpha
+ __OBJC_$_INSTANCE_METHODS_CUIGlassHighlightInternal
+ __OBJC_$_INSTANCE_METHODS_CUIGlow
+ __OBJC_$_INSTANCE_METHODS_CUINarrowBlur15
+ __OBJC_$_INSTANCE_METHODS_CUISDFClamp
+ __OBJC_$_INSTANCE_METHODS_CUISDFFill
+ __OBJC_$_INSTANCE_METHODS_CUIShapeAwareGradientMask
+ __OBJC_$_INSTANCE_METHODS_CUISignedDistanceField
+ __OBJC_$_INSTANCE_METHODS_CUISimplifiedShapeAwareGradientMask
+ __OBJC_$_INSTANCE_VARIABLES_CIBlurredRoundedRectangleGenerator
+ __OBJC_$_INSTANCE_VARIABLES_CISignedDistanceGradientFromRedMask
+ __OBJC_$_INSTANCE_VARIABLES_CISystemToneMap
+ __OBJC_$_INSTANCE_VARIABLES_CIToneMapInternal
+ __OBJC_$_INSTANCE_VARIABLES_CUIClampHDR
+ __OBJC_$_INSTANCE_VARIABLES_CUIComputeNormals
+ __OBJC_$_INSTANCE_VARIABLES_CUIDfDxDfDy
+ __OBJC_$_INSTANCE_VARIABLES_CUIFWidth
+ __OBJC_$_INSTANCE_VARIABLES_CUIGatherSDF
+ __OBJC_$_INSTANCE_VARIABLES_CUIGlassHighlightInternal
+ __OBJC_$_INSTANCE_VARIABLES_CUIGlow
+ __OBJC_$_INSTANCE_VARIABLES_CUINarrowBlur15
+ __OBJC_$_INSTANCE_VARIABLES_CUISDFClamp
+ __OBJC_$_INSTANCE_VARIABLES_CUISDFFill
+ __OBJC_$_INSTANCE_VARIABLES_CUIShapeAwareGradientMask
+ __OBJC_$_INSTANCE_VARIABLES_CUISignedDistanceField
+ __OBJC_$_INSTANCE_VARIABLES_CUISimplifiedShapeAwareGradientMask
+ __OBJC_$_PROP_LIST_CIBlurredRoundedRectangleGenerator
+ __OBJC_$_PROP_LIST_CIImageProcessorInput.146
+ __OBJC_$_PROP_LIST_CIImageProcessorOutput.129
+ __OBJC_$_PROP_LIST_CISignedDistanceGradientFromRedMask
+ __OBJC_$_PROP_LIST_CISystemToneMap
+ __OBJC_$_PROP_LIST_CIToneMapInternal
+ __OBJC_$_PROP_LIST_CUIClampHDR
+ __OBJC_$_PROP_LIST_CUIComputeNormals
+ __OBJC_$_PROP_LIST_CUIDfDxDfDy
+ __OBJC_$_PROP_LIST_CUIFWidth
+ __OBJC_$_PROP_LIST_CUIGatherSDF
+ __OBJC_$_PROP_LIST_CUIGlassHighlightInternal
+ __OBJC_$_PROP_LIST_CUIGlow
+ __OBJC_$_PROP_LIST_CUINarrowBlur15
+ __OBJC_$_PROP_LIST_CUISDFClamp
+ __OBJC_$_PROP_LIST_CUISDFFill
+ __OBJC_$_PROP_LIST_CUIShapeAwareGradientMask
+ __OBJC_$_PROP_LIST_CUISignedDistanceField
+ __OBJC_$_PROP_LIST_CUISimplifiedShapeAwareGradientMask
+ __OBJC_CLASS_RO_$_CIAreaAverageMaximumRed
+ __OBJC_CLASS_RO_$_CIBlurredRoundedRectangleGenerator
+ __OBJC_CLASS_RO_$_CISignedDistanceGradientFromRedMask
+ __OBJC_CLASS_RO_$_CISystemToneMap
+ __OBJC_CLASS_RO_$_CIToneMapInternal
+ __OBJC_CLASS_RO_$_CUIClampHDR
+ __OBJC_CLASS_RO_$_CUIComputeNormals
+ __OBJC_CLASS_RO_$_CUIDfDxDfDy
+ __OBJC_CLASS_RO_$_CUIFWidth
+ __OBJC_CLASS_RO_$_CUIGatherSDF
+ __OBJC_CLASS_RO_$_CUIGlassHighlight
+ __OBJC_CLASS_RO_$_CUIGlassHighlightFromAlpha
+ __OBJC_CLASS_RO_$_CUIGlassHighlightInternal
+ __OBJC_CLASS_RO_$_CUIGlow
+ __OBJC_CLASS_RO_$_CUINarrowBlur15
+ __OBJC_CLASS_RO_$_CUISDFClamp
+ __OBJC_CLASS_RO_$_CUISDFFill
+ __OBJC_CLASS_RO_$_CUIShapeAwareGradientMask
+ __OBJC_CLASS_RO_$_CUISignedDistanceField
+ __OBJC_CLASS_RO_$_CUISimplifiedShapeAwareGradientMask
+ __OBJC_METACLASS_RO_$_CIAreaAverageMaximumRed
+ __OBJC_METACLASS_RO_$_CIBlurredRoundedRectangleGenerator
+ __OBJC_METACLASS_RO_$_CISignedDistanceGradientFromRedMask
+ __OBJC_METACLASS_RO_$_CISystemToneMap
+ __OBJC_METACLASS_RO_$_CIToneMapInternal
+ __OBJC_METACLASS_RO_$_CUIClampHDR
+ __OBJC_METACLASS_RO_$_CUIComputeNormals
+ __OBJC_METACLASS_RO_$_CUIDfDxDfDy
+ __OBJC_METACLASS_RO_$_CUIFWidth
+ __OBJC_METACLASS_RO_$_CUIGatherSDF
+ __OBJC_METACLASS_RO_$_CUIGlassHighlight
+ __OBJC_METACLASS_RO_$_CUIGlassHighlightFromAlpha
+ __OBJC_METACLASS_RO_$_CUIGlassHighlightInternal
+ __OBJC_METACLASS_RO_$_CUIGlow
+ __OBJC_METACLASS_RO_$_CUINarrowBlur15
+ __OBJC_METACLASS_RO_$_CUISDFClamp
+ __OBJC_METACLASS_RO_$_CUISDFFill
+ __OBJC_METACLASS_RO_$_CUIShapeAwareGradientMask
+ __OBJC_METACLASS_RO_$_CUISignedDistanceField
+ __OBJC_METACLASS_RO_$_CUISimplifiedShapeAwareGradientMask
+ __ZGVZ16FOSL_DAG_CODEGENE1v
+ __ZGVZ18CI_CACHE_TILE_SIZEE1v
+ __ZGVZ21CI_ARCHIVE_USAGE_MODEE1v
+ __ZGVZ21CI_ENABLE_UBER_SHADERE1v
+ __ZGVZ22CI_USE_AIR_UBER_SHADERE1v
+ __ZGVZ32CI_ALLOW_UBER_SHADER_COMPILATIONE1v
+ __ZGVZ32CI_WAIT_BEFORE_SWITCHING_TO_UBERE1v
+ __ZGVZ35CI_ENABLE_METAL_FUNCTION_ATTRIBUTESE1v
+ __ZGVZ53-[CIImage(QuicklookSupport) _dotStringRepresentation]E8renderer
+ __ZL12calcUniformsffffffffP8NSString
+ __ZL12post_processP7NSArrayIP21CIImageProcessorInputEPS_IP22CIImageProcessorOutputEPN2CI7ContextE
+ __ZL14FigErrorStringi
+ __ZL14OptionPriorityP12NSDictionary
+ __ZL14srgb_to_linear4vec3
+ __ZL15convert_weightsP8CIVectorPfjj
+ __ZL15createTileInputP22CIImageProcessorOutputmm5IRectS1_P11__IOSurfacePKvN2CI17NodeContentDigestEbbPNS6_7ContextEb
+ __ZL18MetadataAddVersionP15CGImageMetadataPK10__CFStringS3_S3_l
+ __ZL18OptionIsRectVectorP12NSDictionaryP8NSStringP6CGRect
+ __ZL23OptionAverageLightLevelP12NSDictionary
+ __ZL23OptionAverageLightLevelP12NSDictionary.cold.1
+ __ZL37getkCMPhotoCompressionOption_BitDepthv
+ __ZL37getkCMPhotoCompressionOption_BitDepthv.cold.1
+ __ZL38getkCMPhotoCompressionOption_CodecTypev
+ __ZL38getkCMPhotoCompressionOption_CodecTypev.cold.1
+ __ZL39getkCMPhotoCompressionOption_ColorSpacev
+ __ZL39getkCMPhotoCompressionOption_ColorSpacev.cold.1
+ __ZL40getkCMPhotoCompressionOption_Subsamplingv
+ __ZL40getkCMPhotoCompressionOption_Subsamplingv.cold.1
+ __ZL43getkCMPhotoCompressionOption_ApplyTransformv
+ __ZL43getkCMPhotoCompressionOption_ApplyTransformv.cold.1
+ __ZL47soft_CMPhotoCompressionSessionAddAuxiliaryImageP25CMPhotoCompressionSessionl25CMPhotoAuxiliaryImageTypePK15CGImageMetadataPK14__CFDictionaryPKvPl
+ __ZL47soft_CMPhotoCompressionSessionAddAuxiliaryImageP25CMPhotoCompressionSessionl25CMPhotoAuxiliaryImageTypePK15CGImageMetadataPK14__CFDictionaryPKvPl.cold.1
+ __ZL49soft_CMPhotoCompressionSessionAddTmapImageOneShotP25CMPhotoCompressionSessionlPK14__CFDictionaryS3_PKvS3_hPK15CGImageMetadataPl
+ __ZL49soft_CMPhotoCompressionSessionAddTmapImageOneShotP25CMPhotoCompressionSessionlPK14__CFDictionaryS3_PKvS3_hPK15CGImageMetadataPl.cold.1
+ __ZL56getkCMPhotoCompressionOption_AuxiliaryImageCustomTypeURNv
+ __ZL56getkCMPhotoCompressionOption_AuxiliaryImageCustomTypeURNv.cold.1
+ __ZL58soft_CMPhotoCompressionSessionCloseContainerAndCopyBackingP25CMPhotoCompressionSessionP32CMPhotoImageContainerBackingTypePmPPKv
+ __ZL58soft_CMPhotoCompressionSessionCloseContainerAndCopyBackingP25CMPhotoCompressionSessionP32CMPhotoImageContainerBackingTypePmPPKv.cold.1
+ __ZN14__CFDictionary8setValueEPS_PK10__CFStringd
+ __ZN18CIKernelReflection7reflectEP15CIKernelLibraryPKcPP7NSError.cold.10
+ __ZN18CIKernelReflection7reflectEP15CIKernelLibraryPKcPP7NSError.cold.11
+ __ZN18CIKernelReflection7reflectEP15CIKernelLibraryPKcPP7NSError.cold.12
+ __ZN18CIKernelReflection7reflectEPvjPP7NSError.cold.4
+ __ZN18CIKernelReflection7reflectEPvjPP7NSError.cold.5
+ __ZN18CIKernelReflection7reflectEPvjPP7NSError.cold.6
+ __ZN18CIKernelReflection7reflectEPvjPP7NSError.cold.7
+ __ZN2CI10sw_averageERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_checkerERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_000rERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_1bgrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_1rgbERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_a001ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_aaa1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_aaaaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_abg1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_abgrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_arg1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_argbERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_bgr1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_bgraERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_cropERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_curvERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_fillERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_gb1rERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_gba1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_gbarERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_gbraERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_gr1bERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_gra1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_grabERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_pow4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_r001ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_ra01ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_rg01ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_rgb1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_rrr1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_rrrgERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_rrrrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ci_sqrtERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_clearerERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_conv3x3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_dditherERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_disolveERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_drr_mmiERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_drr_mmvERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_dstAtopERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_dstOverERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_flexMapERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_gainMapERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_kaleidaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_lumaMapERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_maxDiskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_minDiskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_onlyRG_ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_pq_eotfERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_sdfFillERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_sobel_mERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_srcAtopERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_srcOverERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_stretchERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_stripesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_xSmoothERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI10sw_ySmoothERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11ConvertNodeC2EPNS_4NodeENS_11ConvertTypeEbU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS4_9allocatorIS7_EEEERKNS5_IPKvNS8_ISE_EEEERKNS5_INS_17NodeContentDigestENS8_ISJ_EEEERKNS5_I6CGRectNS8_ISO_EEEERKNS5_IbNS8_IbEEEES7_SE_SJ_SO_biPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EE4findEy
+ __ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EE5EntryD2Ev
+ __ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EE5evictEv
+ __ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EE6insertEyPS1_j
+ __ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EEC2Em
+ __ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EED2Ev
+ __ZN2CI11sw_LABtoRGBERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_PC_coordERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_RCCenterERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_RGBtoLABERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_add4and4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_add4and8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_add8and8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_areaAvg2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_areaAvg4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_areaAvg8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_areaMax4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_areaMin4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_asgDownHERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_asgDownVERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_boostRGBERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_boxBlur3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_boxBlur5ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_boxBlur7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_boxBlur9ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_ci_gammaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_clampHDRERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_cm1x3lutERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_colorMapERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_downhalfERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_drr_specERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_edgeWorkERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_gradientERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_hlg_oetfERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_hsvwheelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_maxScaleERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_morphmaxERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_morphminERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_multiplyERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_ringAvg8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_sunbeamsERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_vertAvg2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_vertAvg4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_vertAvg8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_vertMax4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_vertMin4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_vignetteERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI11sw_zoomBlurERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12MetalContext12bind_surfaceEP11__IOSurfaceRKNS_17TextureDescriptorEbNS_10SampleModeENS_8EdgeModeEbii
+ __ZN2CI12MetalContext12bind_textureEPKvNS_10SampleModeENS_8EdgeModeEbi
+ __ZN2CI12MetalContextC1EPKvPKcP12CGColorSpaceS6_NS_11PixelFormatEbmmyS2_bb
+ __ZN2CI12MetalContextC2EPKvPKcP12CGColorSpaceS6_NS_11PixelFormatEbmmyS2_bb
+ __ZN2CI12ProviderNodeC1ENS_10ImageIndexENS_22ImageLeafContentDigestEPK10__CFStringU13block_pointerFvP11__IOSurfacemmmmEU13block_pointerFvPvmmmmmmEP16dispatch_queue_smmNSt3__16vectorINSG_I5IRectNSF_9allocatorISH_EEEENSI_ISK_EEEENS_11PixelFormatESN_NS_9AlphaModeENS_8EdgeModeEbbb
+ __ZN2CI12ProviderNodeC2ENS_10ImageIndexENS_22ImageLeafContentDigestEPK10__CFStringU13block_pointerFvP11__IOSurfacemmmmEU13block_pointerFvPvmmmmmmEP16dispatch_queue_smmNSt3__16vectorINSG_I5IRectNSF_9allocatorISH_EEEENSI_ISK_EEEENS_11PixelFormatESN_NS_9AlphaModeENS_8EdgeModeEbbb
+ __ZN2CI12SetInfoImage10makeDigestENS_11ImageDigestE
+ __ZN2CI12SetInfoImageC2EPNS_5ImageE
+ __ZN2CI12SetInfoImageD0Ev
+ __ZN2CI12SetInfoImageD1Ev
+ __ZN2CI12SurfaceImageC1EP11__IOSurfaceNS_22ImageLeafContentDigestENS_11PixelFormatEffiPKvNS_9AlphaModeENS_8EdgeModeEbb
+ __ZN2CI12SurfaceImageC2EP11__IOSurfaceNS_22ImageLeafContentDigestENS_11PixelFormatEffiPKvNS_9AlphaModeENS_8EdgeModeEbb
+ __ZN2CI12sw_CElumaToRERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_CEstretchERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_DEminmax4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_KM_defuseERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_KM_selectERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_LabDeltaEERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_barsSwipeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_boxBlur11ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_boxBlur13ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_cheapBlurERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_ci_10of16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_ci_affineERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_ci_premulERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_cmyk_cyanERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_colorcubeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_computeABERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_dotscreenERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_drr_boostERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_drr_noiseERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_drr_pclipERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_edgesPrepERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_findEdgesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_flashGeomERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_gatherSDFERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_guideMonoERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_horizAvg2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_horizAvg4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_horizAvg8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_horizMax4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_horizMin4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_innerGorSERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_laplacianERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_lumaRangeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_median3x3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_outerGorSERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_palettizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_pixellateERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_rectangleERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_rer_glintERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_ringAvg16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_ringAvg24ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_ringAvg32ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_spotColorERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_spotLightERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_starshineERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_tiltShiftERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_toneCurveERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI12sw_vertAvg16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13GLMainProgramC1EPKNS_9GLContextENS_9NodeIndexEPKcS6_PNS_14SerialValArrayIiEEPNS_17SerialStringArrayEj
+ __ZN2CI13KernelArchiveC2ENSt3__16vectorIPKvNS1_9allocatorIS4_EEEE
+ __ZN2CI13ProcessorNode12set_callbackEU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS1_9allocatorIS4_EEEERKNS2_IPKvNS5_ISB_EEEERKNS2_INS_17NodeContentDigestENS5_ISG_EEEERKNS2_I6CGRectNS5_ISL_EEEERKNS2_IbNS5_IbEEEES4_SB_SG_SL_biPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI13ProcessorNode13set_callbackmEU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS1_9allocatorIS4_EEEERKNS2_IPKvNS5_ISB_EEEERKNS2_INS_17NodeContentDigestENS5_ISG_EEEERKNS2_I6CGRectNS5_ISL_EEEERKNS2_IbNS5_IbEEEEiPKS4_PKSB_SG_PKSL_PKbiPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI13ProcessorNode14append_to_treeEPNS_20SerialObjectPtrArrayEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvRKNS4_IP11__IOSurfaceNS6_ISC_EEEERKNS4_IPKvNS6_ISI_EEEERKNS4_INS_17NodeContentDigestENS6_ISN_EEEERKS8_RKNS4_IbNS6_IbEEEESC_SI_SN_S5_biPNS_7ContextEPNS_8TileTaskEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPS1A_PKbS1A_bbbbbbb
+ __ZN2CI13ProcessorNode14append_to_treeEPNS_20SerialObjectPtrArrayEjPK6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPSA_PKbPKSA_SD_SD_bbbbbU13block_pointerFNSt3__16vectorIS3_NSG_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSH_IP11__IOSurfaceNSI_ISO_EEEERKNSH_IPKvNSI_ISU_EEEERKNSH_INS_17NodeContentDigestENSI_ISZ_EEEERKSK_RKNSH_IbNSI_IbEEEEiPKSO_PKSU_SZ_S5_SD_iPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI13ProcessorNode14append_to_treeEU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS1_9allocatorIS4_EEEERKNS2_IPKvNS5_ISB_EEEERKNS2_INS_17NodeContentDigestENS5_ISG_EEEERKNS2_I6CGRectNS5_ISL_EEEERKNS2_IbNS5_IbEEEES4_SB_SG_SL_biPNS_7ContextEPNS_8TileTaskEERKSL_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES16_bbbbb
+ __ZN2CI13ProcessorNodeC2EPNS_20SerialObjectPtrArrayEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvRKNS4_IP11__IOSurfaceNS6_ISC_EEEERKNS4_IPKvNS6_ISI_EEEERKNS4_INS_17NodeContentDigestENS6_ISN_EEEERKS8_RKNS4_IbNS6_IbEEEESC_SI_SN_S5_biPNS_7ContextEPNS_8TileTaskEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPS1A_PKbS1A_bbbbbbb
+ __ZN2CI13ProcessorNodeC2EPNS_20SerialObjectPtrArrayEjPK6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPSA_PKbPKSA_SD_SD_bbbbbU13block_pointerFNSt3__16vectorIS3_NSG_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSH_IP11__IOSurfaceNSI_ISO_EEEERKNSH_IPKvNSI_ISU_EEEERKNSH_INS_17NodeContentDigestENSI_ISZ_EEEERKSK_RKNSH_IbNSI_IbEEEEiPKSO_PKSU_SZ_S5_SD_iPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI13ProcessorNodeC2EPNS_4NodeEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvRKNS4_IP11__IOSurfaceNS6_ISC_EEEERKNS4_IPKvNS6_ISI_EEEERKNS4_INS_17NodeContentDigestENS6_ISN_EEEERKS8_RKNS4_IbNS6_IbEEEESC_SI_SN_S5_biPNS_7ContextEPNS_8TileTaskEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES1A_S1A_bbbbbbb
+ __ZN2CI13ProcessorNodeC2EU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS1_9allocatorIS4_EEEERKNS2_IPKvNS5_ISB_EEEERKNS2_INS_17NodeContentDigestENS5_ISG_EEEERKNS2_I6CGRectNS5_ISL_EEEERKNS2_IbNS5_IbEEEES4_SB_SG_SL_biPNS_7ContextEPNS_8TileTaskEERKSL_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES16_bbbbb
+ __ZN2CI13ProviderImageC1ENS_22ImageLeafContentDigestEPK10__CFStringU13block_pointerFvP11__IOSurfacePKvmmmmEU13block_pointerFvPvmmmmmmEmmNSt3__16vectorINSF_I5IRectNSE_9allocatorISG_EEEENSH_ISJ_EEEENS_11PixelFormatEffiS8_NS_9AlphaModeENS_8EdgeModeEbbb
+ __ZN2CI13ProviderImageC2ENS_22ImageLeafContentDigestEPK10__CFStringU13block_pointerFvP11__IOSurfacePKvmmmmEU13block_pointerFvPvmmmmmmEmmNSt3__16vectorINSF_I5IRectNSE_9allocatorISG_EEEENSH_ISJ_EEEENS_11PixelFormatEffiS8_NS_9AlphaModeENS_8EdgeModeEbbb
+ __ZN2CI13TileCacheNode17release_resourcesEv
+ __ZN2CI13TileCacheNodeD0Ev
+ __ZN2CI13TileCacheNodeD1Ev
+ __ZN2CI13sw_ACCentroidERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_DE_compinvERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_boxBlur3x3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_boxFilter3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_cannyFinalERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_ci_la_to_aERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_ci_la_to_iERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_ci_nearestERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_ci_rg_to_aERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_ci_rg_to_iERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_cmyk_blackERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_colorClampERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_conv3x3symERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_convrgb3x3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_destDitherERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_drr_rcsoftERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_drr_repairERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_falseColorERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_flashColorERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_horizAvg16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_lanczosUpHERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_lanczosUpVERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_linescreenERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_localBoostERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_motionBlurERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_otsuThreshERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_paddedTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_plusDarkerERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_polyKernelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_rectstrokeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_reduceCropERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_resetalphaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_scaleClampERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_sobelEdgesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI13sw_wrapMirrorERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14MetalDAGHelper19TextureReadFunctionC2Ev
+ __ZN2CI14ProcessorImage11outputImageEi
+ __ZN2CI14ProcessorImageC1E6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEbbbbU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS7_9allocatorISA_EEEERKNS8_IPKvNSB_ISH_EEEERKNS8_INS_17NodeContentDigestENSB_ISM_EEEERKNS8_IS1_NSB_IS1_EEEERKNS8_IbNSB_IbEEEESA_SH_SM_S1_biPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI14ProcessorImageC1EPNS_20SerialObjectPtrArrayE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbS8_bbbbbbbU13block_pointerFNSt3__16vectorIS3_NSC_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSD_IP11__IOSurfaceNSE_ISK_EEEERKNSD_IPKvNSE_ISQ_EEEERKNSD_INS_17NodeContentDigestENSE_ISV_EEEERKSG_RKNSD_IbNSE_IbEEEESK_SQ_SV_S3_biPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI14ProcessorImageC1EPNS_20SerialObjectPtrArrayEjPK6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbSB_PbSE_bbbbbU13block_pointerFNSt3__16vectorIS3_NSF_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSG_IP11__IOSurfaceNSH_ISN_EEEERKNSG_IPKvNSH_IST_EEEERKNSG_INS_17NodeContentDigestENSH_ISY_EEEERKSJ_RKNSG_IbNSH_IbEEEEiPKSN_PKST_SY_S5_SD_iPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI14ProcessorImageC1EPNS_5ImageE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEbS8_bbbbbbbU13block_pointerFNSt3__16vectorIS3_NS9_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSA_IP11__IOSurfaceNSB_ISH_EEEERKNSA_IPKvNSB_ISN_EEEERKNSA_INS_17NodeContentDigestENSB_ISS_EEEERKSD_RKNSA_IbNSB_IbEEEESH_SN_SS_S3_biPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI14ProcessorImageC2EPNS_20SerialObjectPtrArrayE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbS8_bbbbbbbU13block_pointerFNSt3__16vectorIS3_NSC_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSD_IP11__IOSurfaceNSE_ISK_EEEERKNSD_IPKvNSE_ISQ_EEEERKNSD_INS_17NodeContentDigestENSE_ISV_EEEERKSG_RKNSD_IbNSE_IbEEEESK_SQ_SV_S3_biPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI14ProcessorImageC2EPNS_20SerialObjectPtrArrayEjPK6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbSB_PbSE_bbbbbU13block_pointerFNSt3__16vectorIS3_NSF_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSG_IP11__IOSurfaceNSH_ISN_EEEERKNSG_IPKvNSH_IST_EEEERKNSG_INS_17NodeContentDigestENSH_ISY_EEEERKSJ_RKNSG_IbNSH_IbEEEEiPKSN_PKST_SY_S5_SD_iPNS_7ContextEPNS_8TileTaskEE
+ __ZN2CI14TextureManager30_release_intermediate_for_nodeERKNSt3__120__map_const_iteratorINS1_21__tree_const_iteratorINS1_12__value_typeIKiPNS0_16tmIntermediate_tEEEPNS1_11__tree_nodeIS8_PvEElEEEERNS1_8multimapIS5_S7_NS1_4lessIS5_EENS1_9allocatorINS1_4pairIS5_S7_EEEEEE
+ __ZN2CI14arg_name_colorE
+ __ZN2CI14sw_DE_scaleAddERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_betterDown2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_blendGrainsERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_blurredrectERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_boostHybridERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_boxCombine2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_boxCombine3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_boxCombine5ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_boxCombine7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_ci_unpremulERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_cmyk_yellowERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_colorcurvesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_crystallizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_drr_maxmaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_exclusiveOrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_facebalanceERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_finalResultERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_fusionDeltaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_lighttunnelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_lowq_affineERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_maskToAlphaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_maxGradOnlyERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_paddedTile2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_plusLighterERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_pointillizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_pq_inv_eotfERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_resp_previsERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_roundedrectERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_shadowdesatERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_stretchcropERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_swizzleXXX1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_swizzleYYZ1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_swizzleYZZ1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_unsharpmaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI14sw_yccCombinerERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15ColorMatchImage10makeDigestENS_11ImageDigestEP12CGColorSpaceS3_fb
+ __ZN2CI15ColorMatchImageC1EPNS_5ImageEP12CGColorSpacefb
+ __ZN2CI15ColorMatchImageC2EPNS_5ImageEP12CGColorSpacefb
+ __ZN2CI15InstanceCountedILNS_4TypeE26EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE26EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE27EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE27EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE42EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE42EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE43EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE43EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE53EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE53EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE56EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE56EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE61EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE61EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE63EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE63EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE64EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE64EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE65EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE65EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE66EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE66EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE73EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE73EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE74EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE74EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE87EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE87EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE89EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE89EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE90EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE90EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE91EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE91EED1Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE94EED0Ev
+ __ZN2CI15InstanceCountedILNS_4TypeE94EED1Ev
+ __ZN2CI15MetalDAGProgram7compileENS_9NodeIndexE
+ __ZN2CI15MetalDAGProgramC2EPKcPKNS_12MetalContextENSt3__110shared_ptrINS_25ConcatenatedDAGDescriptorEEEPNS_14SerialValArrayIiEESC_mRKNS_21DestinationDescriptorE
+ __ZN2CI15MetalDAGProgramD0Ev
+ __ZN2CI15MetalDAGProgramD1Ev
+ __ZN2CI15MetalDAGProgramD2Ev
+ __ZN2CI15sw_CBHorzGuidedERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_CBVertGuidedERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_PSDrawSpreadERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_accordionMixERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_bgr10wideERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_combine_aERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_combine_rERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_la_to_ll1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_la_to_rr1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_pass_thruERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_rg_to_ll1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_rg_to_rr1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_rgb10wideERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_srgb_noopERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_ci_to_10of16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_circleSplashERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_circularWrapERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_clampToFrameERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_cmcubeopaqueERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_cmyk_convertERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_cmyk_magentaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_colorAbsDiffERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_colorClampAPERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_colorbalanceERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_convolution3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_convolution5ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_convolution7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_convolution9ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_distanceMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_drr_binarizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_drr_multiplyERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_drr_recoveryERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_drr_specularERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_fadeDissolveERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_flexMapImageERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_glassDistortERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_guideCombineERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_hlg_inv_oetfERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_hlg_lumscaleERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_holeFillPostERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_hueBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_invertedMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_lanczosDown2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_lanczosDownHERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_lanczosDownVERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_logHistogramERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_narrowBlur15ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_redThresholdERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_shadowKernelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_thresholdRedERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_triangleTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_vibrance_negERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI15sw_vibrance_posERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16CIToneMapKernels102arg_name_img_source_headroom_target_headroom_slope_adjusted_bezier_norm_beziers_py_extension_cdr_scaleE
+ __ZN2CI16CIToneMapKernels28arg_name_img_target_headroomE
+ __ZN2CI16CIToneMapKernelsL31arg_type_Sample_Float_DestCoordE
+ __ZN2CI16CIToneMapKernelsL70arg_type_Sample_Float_Float_Float_Float4_Float3_Float3_Float_DestCoordE
+ __ZN2CI16ColorKernelImageC1EPKNS_6KernelEPNS_20SerialObjectPtrArrayE6CGRectU13block_pointerFS6_iS6_EbNS_11PixelFormatEff
+ __ZN2CI16ColorKernelImageC2EPKNS_6KernelEPNS_20SerialObjectPtrArrayE6CGRectU13block_pointerFS6_iS6_EbNS_11PixelFormatEff
+ __ZN2CI16SetHeadroomImageD0Ev
+ __ZN2CI16SetHeadroomImageD1Ev
+ __ZN2CI16sw_CEcomp_minmaxERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_CIBoxBlur5MinERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_LAB_normalizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_RCFalloffDiskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_blendWithMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_ci_argb10wideERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_ci_clamp_rectERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_ci_combine_laERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_ci_combine_rgERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_ci_ycc_to_rgbERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_colorControlsERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_combineImagesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_convertRGBtoYERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_convrgb3x3symERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_cubicUpsampleERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_drr_cdmeasureERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_drr_chromaexcERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_drr_maximumRhERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_drr_minimumRhERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_drr_puncture2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_drr_rawred_smERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_drr_thresholdERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_gaussianBlur3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_gaussianBlur5ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_gaussianBlur7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_gaussianBlur9ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_guideCombine4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_hatchedscreenERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_headroomClampERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_hlg_srmappingERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_holeAntialiasERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_linearMappingERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_localContrastERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_maxScaleDown2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_modTransitionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_perc_norm_redERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_prepHistogramERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_rawHighlightsERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI16sw_roundedstrokeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17SetDepthDataImageC2EPNS_5ImageEPKv
+ __ZN2CI17SetDepthDataImageD0Ev
+ __ZN2CI17SetDepthDataImageD1Ev
+ __ZN2CI17SetDepthDataImageD2Ev
+ __ZN2CI17UberDAGDescriptor12post_processEv
+ __ZN2CI17UberDAGDescriptor15create_pipelineEv
+ __ZN2CI17UberDAGDescriptor15create_pipelineEv.cold.1
+ __ZN2CI17UberDAGDescriptor15create_pipelineEv.cold.2
+ __ZN2CI17UberDAGDescriptor15create_pipelineEv.cold.3
+ __ZN2CI17UberDAGDescriptor15create_pipelineEv.cold.4
+ __ZN2CI17UberDAGDescriptor17get_uber_pipelineEv
+ __ZN2CI17UberDAGDescriptorC2EPKNS_12MetalContextE
+ __ZN2CI17UberDAGDescriptorD0Ev
+ __ZN2CI17UberDAGDescriptorD1Ev
+ __ZN2CI17UberDAGDescriptorD2Ev
+ __ZN2CI17UberDAGDescriptorD2Ev.cold.1
+ __ZN2CI17_sw_ci_read_pixelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_accordianWarpSERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_accordianWarpTERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_alphaNormalizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_areaAveMaxRed4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_areaMaxAlphaH4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_areaMaxAlphaS4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_areaMaxAlphaV4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_areaMinAlphaH4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_areaMinAlphaS4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_areaMinAlphaV4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_areaMinMaxRed4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_bumpDistortionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_cannyThresholdERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_colormatrixERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_combine_420ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_combine_422ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_combine_444ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_combine_a16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_combine_l16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_combine_r16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_lin_to_srgbERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_srgb_to_linERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_ci_to_rgb_as_rERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_circularscreenERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_colorBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_colorPosterizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_colorThresholdERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_convolution5x5ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_convolution7x7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_drr_puncturec2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_drr_spec_debugERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_flexMapLinGainERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_gaussianBlur11ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_gaussianBlur13ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_gaussianBlur15ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_gaussianBlur19ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_glassHighlightERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_holeDistortionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_holeFillRefineERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_jointBilateralERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_lenticularHaloERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_linearGradientERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_maskBoundsInitERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_maskBoundsPostERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_multiplyByMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_multiplyImagesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_noiseReductionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_perc_accum_redERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_perc_clip_hardERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_perc_clip_softERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_pq_tonemappingERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_radialGradientERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_shadedmaterialERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_shadows_noblurERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_subtractImagesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_vertAveMaxRed4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_vertMinMaxRed4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI17sw_vignetteeffectERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18CIReductionKernels20arg_name_image_scaleE
+ __ZN2CI18CIReductionKernelsL32arg_type_Sampler_Float_DestCoordE
+ __ZN2CI18GeneralKernelImageC1EPNS_13GeneralKernelEPNS_20SerialObjectPtrArrayERKNSt3__16vectorI6CGRectNS5_9allocatorIS7_EEEES7_U13block_pointerFS7_iS7_ENS_11PixelFormatEffb
+ __ZN2CI18GeneralKernelImageC2EPNS_13GeneralKernelEPNS_20SerialObjectPtrArrayERKNSt3__16vectorI6CGRectNS5_9allocatorIS7_EEEES7_U13block_pointerFS7_iS7_ENS_11PixelFormatEffb
+ __ZN2CI18_sw_ci_write_pixelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18new_kernel_archiveENSt3__16vectorIPKvNS0_9allocatorIS3_EEEE
+ __ZN2CI18new_uber_functionsEPKNS_12MetalContextE
+ __ZN2CI18sw_CIFaceMaskApplyERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_LAB_denormalizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_areaAveMaxRed16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_areaMinMaxRed16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_blendWithMaskB0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_cannyHysteresisERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_ci_combine_grayERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_ci_rgba_to_llaaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_ci_to_bgr10wideERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_ci_to_rgb10wideERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_colorMonochromeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_colorPolynomialERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_colorcubeopaqueERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_convolutionrgb3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_convolutionrgb5ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_convolutionrgb7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_convolutionrgb9ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_cubicUpsample10ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_cubicUpsampleX0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_darkenBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_dfdxdfdyChannelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_dfdxdfdyChannelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm.cold.1
+ __ZN2CI18sw_distanceColoredERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_divideBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_drr_cdintersectERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_drr_maxScalarRhERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_flexLumaScalingERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_flexMapImageRGBERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_fusionTwoImagesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_gaussianReduce2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_gaussianReduce4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_headroomToneMapERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_horizAveMaxRed4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_horizMinMaxRed4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_hueBlendMode_v0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_maxScaleDown2x2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_minMaxNormalizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_perc_denorm_redERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_perspectiveMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_perspectiveWarpERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_screenBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_smartcolor_castERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_swipeTransitionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_torusRefractionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI18sw_variableBoxBlurERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19MetalTextureManager19create_intermediateERKNS_22IntermediateDescriptorEPKvRK5IRectmb
+ __ZN2CI19MetalTextureManager30_release_intermediate_for_nodeERKNSt3__120__map_const_iteratorINS1_21__tree_const_iteratorINS1_12__value_typeIKiPNS_14TextureManager16tmIntermediate_tEEEPNS1_11__tree_nodeIS9_PvEElEEEERNS1_8multimapIS5_S8_NS1_4lessIS5_EENS1_9allocatorINS1_4pairIS5_S8_EEEEEE
+ __ZN2CI19ProcessorOutputNode24append_to_tree_and_unrefEPNS_4NodeEi6CGRectbNS_11PixelFormatEb
+ __ZN2CI19ProcessorOutputNodeC2EPNS_4NodeEi6CGRectbNS_11PixelFormatEb
+ __ZN2CI19ProcessorOutputNodeD0Ev
+ __ZN2CI19ProcessorOutputNodeD1Ev
+ __ZN2CI19sw_CIBlurPreProcessERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_CILensModelApplyERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_DEnormalizeAlphaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_appleLogToLinearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_blendWithRedMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_boostRGBLNoGammaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_ciExtractChannelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_ci_rgba_to_rrgg1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_ci_to_a16_as_rg8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_ci_to_l10_as_r16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_ci_to_l16_as_rg8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_ci_to_r16_as_rg8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_combineRGB_and_AERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_convolutionAdd_1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_convolutionAdd_2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_convolutionAdd_3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_convolutionAdd_4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_convolutionAdd_5ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_convolutionAdd_6ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_convolutionAdd_7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_convolutionAdd_8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_cubicDownsample2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_cubicDownsampleHERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_cubicDownsampleVERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_cubicUpsample10hERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_cubicUpsample10vERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_distanceFractionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_distanceMaskPostERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_distanceMaskPrepERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_drr_binarize_invERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_drr_combine_rgbaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_drr_detect_specsERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_drr_extract_irisERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_drr_extract_skinERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_drr_rawred_largeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_drr_smoothstepRhERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_edgeWorkContrastERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_gaussianGradientERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_grainBlendAndMixERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_hardMixBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_hsvwheelditheredERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_jointBilateralRGERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_lightenBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_linearToAppleLogERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_maskBoundsReduceERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_maximumComponentERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_minimumComponentERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_ninePartTiledAltERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_outerBevelEmbossERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_overlayBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_rippleTransitionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_shadedmaterial_0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_sharpenLuminanceERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_vortexDistortionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI19sw_whitepointadjustERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20ProcessorOutputImage10makeDigestENS_11ImageDigestEi6CGRectbNS_11PixelFormatE
+ __ZN2CI20ProcessorOutputImageC2EPNS_5ImageEi6CGRectbNS_11PixelFormatE
+ __ZN2CI20ProcessorOutputImageD0Ev
+ __ZN2CI20ProcessorOutputImageD1Ev
+ __ZN2CI20SerialObjectPtrArray5clearEv
+ __ZN2CI20sw_CIPortraitBlurDirERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_CISmoothDisparityERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_RCFalloffGaussianERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_blendWithBlueMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_ci_clamp_to_alphaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_ci_colormatrix3x1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_ci_colormatrix3x3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_ci_colormatrix3x4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_ci_swizzle_to_4XXERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_colorBlendMode_v0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_convolutionrgb5x5ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_convolutionrgb7x7ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_cubicDownsample2hERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_cubicDownsample2vERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_cui_hueSaturationERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_displaceFromImageERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_drr_refilter_chanERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_flexMapLinGainRGBERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_gradientDirectionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_gradientMagnitudeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_grassAndSkyAdjustERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_histogram_displayERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_lozengeRefractionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_multiplyBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_ninePartStretchedERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_outerBevelEmbossCERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_parallelogramTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_pinLightBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_shapeEffectBlur_1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_subtractBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI20sw_vignetteeffectnegERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21SoftwareDAGDescriptor12ArgumentInfo3addENS_18SWArgumentInfoTypeEm
+ __ZN2CI21_sw_ci_linear_to_srgbERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21_sw_ci_read_pixel_420ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21_sw_ci_srgb_to_linearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21add_to_kernel_archiveEPNS_13KernelArchiveEPKv
+ __ZN2CI21sw_blendWithAlphaMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_blendWithRedMaskB0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_blurredroundedrectERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_ci_bgr10widelinearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_ci_colormatrixdiagERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_ci_rgb10widelinearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_ci_swizzle_to_laaaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_colorBurnBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_colorPolynomialRGBERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_drr_binarize_alphaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_drr_puncture2_hardERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_exclusionBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_faceMaskCalculatorERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_glideReflectedTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_gradientRangeLimitERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_hardLightBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_hexagonalPixellateERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_maskedVariableBlurERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_minMaxRedNormalizeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_pageCurlTransitionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_prepHoughTransformERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_segmentationFusionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_signedDistanceMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_sixfoldRotatedTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_smartBlackAndWhiteERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_smarttone_contrastERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI21sw_softLightBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22format_is_rgb_biplanarENS_11PixelFormatE
+ __ZN2CI22sw_DEconditionalFilterERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_RCSelectGreaterThanERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_blendWithBlueMaskB0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_ci_argb10widelinearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_ci_colormatrix_rrraERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_ci_colormatrixdiag4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_ci_to_CbYCrY_as_rg8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_ci_to_YCbYCr_as_rg8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_ci_to_la16_as_bgra8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_ci_to_la16_as_rgba8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_ci_to_rg16_as_bgra8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_ci_to_rg16_as_rgba8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_colorDodgeBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_differenceBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_drr_puncturec2_hardERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_fourfoldRotatedTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_glowMaskNotOppositeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_gradientNormalizeV1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_gradientNormalizeV2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_gradientThresholdV1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_gradientThresholdV2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_linearBurnBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_luminosityBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_noiseComicReductionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_pageCurlTransNoEmapERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_reduceCropAveMaxRedERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_reduceCropMinMaxRedERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_saturationBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_sharpenCombineEdgesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_smartcolor_contrastERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI22sw_vividLightBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23_sw_ci_read_pixel_rgb_aERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_CIAreaHistogramScaleERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_blendWithAlphaMaskB0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_bumpDistortionLinearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_ci_to_rgb10_as_rgba8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_colorCrossPolynomialERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_darkerColorBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_disintegrateWithMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_interleavedToPlanar3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_interleavedToPlanar4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_linearDodgeBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_linearLightBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_perspectiveTransformERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_planarToInterleaved3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_planarToInterleaved4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_radialLensDistortionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_sixfoldReflectedTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI23sw_smoothLinearGradientERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24CUIGlassHighlightKernels10arg_name_sE
+ __ZN2CI24CUIGlassHighlightKernels14arg_name_s_dirE
+ __ZN2CI24CUIGlassHighlightKernels16arg_name_s_frameE
+ __ZN2CI24CUIGlassHighlightKernels17arg_name_s_fwidthE
+ __ZN2CI24CUIGlassHighlightKernels18arg_name_s_channelE
+ __ZN2CI24CUIGlassHighlightKernels20arg_name_s_dfDxdfDyXE
+ __ZN2CI24CUIGlassHighlightKernels22arg_name_s_below_aboveE
+ __ZN2CI24CUIGlassHighlightKernels23arg_name_s_maxComponentE
+ __ZN2CI24CUIGlassHighlightKernels34arg_name_s_sdfZero_sdfScale_radiusE
+ __ZN2CI24CUIGlassHighlightKernels40arg_name_s_sdfZero_sdfScale_radius_colorE
+ __ZN2CI24CUIGlassHighlightKernels46arg_name_s_dfdxW_values0_values1_sdfZero_colorE
+ __ZN2CI24CUIGlassHighlightKernels47arg_name_s_fwidth_values0_values1_sdfZero_colorE
+ __ZN2CI24CUIGlassHighlightKernels66arg_name_distanceFraction_distanceFractionFWidth_bias_amount_colorE
+ __ZN2CI24CUIGlassHighlightKernels81arg_name_s_borderWidth_opacityBounds_contourOpacityBounds_sdfScale_sdfZero_boundsE
+ __ZN2CI24CUIGlassHighlightKernels82arg_name_s_borderWidth_minOpacity_opaqueEnd_length_lightDirection_sdfScale_sdfZeroE
+ __ZN2CI24CUIGlassHighlightKernelsL25arg_type_Sample_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL26arg_type_Sampler_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL30arg_type_Sampler_Int_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL31arg_type_Sample_Float_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL32arg_type_Sample_Sample_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL33arg_type_Sampler_Float2_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL33arg_type_Sampler_Float4_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL37arg_type_Sample_Float_Float_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL43arg_type_Sample_Float_Float_Float_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL45arg_type_Sample_Sample_Float_Float4_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL50arg_type_Sample_Float_Float_Float_Float4_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL59arg_type_Sample_Sample_Float4_Float4_Float_Float4_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL64arg_type_Sample_Float_Float2_Float2_Float_Float_Float4_DestCoordE
+ __ZN2CI24CUIGlassHighlightKernelsL69arg_type_Sample_Float_Float_Float2_Float_Float3_Float_Float_DestCoordE
+ __ZN2CI24PrecompiledUberFunctionsC2EPKNS_12MetalContextE
+ __ZN2CI24PrecompiledUberFunctionsD2Ev
+ __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEbU13block_pointerFbS0_E
+ __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEbU13block_pointerFbS0_E.cold.1
+ __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEbU13block_pointerFbS0_E.cold.2
+ __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEbU13block_pointerFbS0_E.cold.3
+ __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEbU13block_pointerFbS0_E.cold.4
+ __ZN2CI24sw_ciLensModelCalculatorERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_ci_to_bgr10widelinearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_ci_to_rgb10widelinearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_copyMachineTransitionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_disintegrateWithMaskGERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_drr_conditionalZeroRhERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_fourfoldReflectedTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_highlightsAndShadows0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_highlightsAndShadows1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_highlightsAndShadows2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_lighterColorBlendModeERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_perspectiveCorrectionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI24sw_photoEffectDepthBlendERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25ConcatenatedDAGDescriptor12post_processEv
+ __ZN2CI25ConcatenatedDAGDescriptor17get_uber_pipelineEv
+ __ZN2CI25SetAverageLightLevelImageD0Ev
+ __ZN2CI25SetAverageLightLevelImageD1Ev
+ __ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxP13vImage_BufferS3_PKvNS_11ConvertTypeE
+ __ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxP13vImage_BufferS3_PKvNS_11ConvertTypeE.cold.1
+ __ZN2CI25format_swizzle_for_outputENS_11PixelFormatE5IRectjU13block_pointerFbS0_E
+ __ZN2CI25format_swizzle_for_outputENS_11PixelFormatE5IRectjU13block_pointerFbS0_E.cold.1
+ __ZN2CI25sw_ACWeightedCoordinatesRERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_CIInitialConversionRGBERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_CIPyramidGenerateLevelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_DEcomputeInversionMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_DEcreateForegroundMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_ci_to_a2bgr10_as_rgba8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_ci_to_a2rgb10_as_rgba8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_colorPolynomialInverseERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_colorcubeopaque_extendERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_drr_binarize_alpha_invERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_eightfoldReflectedTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_fallbackComputeNormalsERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_fourfoldTranslatedTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_linearBurnBlendMode_v0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_luminosityBlendMode_v0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_saturationBlendMode_v0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_shapeAwareGradientMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_signedDistanceMaskPostERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI25sw_signedDistanceMaskPrepERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_accordionFoldTransitionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_ciSingleChannelColorMapERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_ci_clamp_to_zero_to_oneERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_convertDepthOrDisparityERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_convertUsingColorMatrixERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_glassHighlightFromAlphaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_pinchDistortionScaleGE1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_pinchDistortionScaleLT1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_smartcolor_vibrancy_gt1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_smartcolor_vibrancy_lt1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI26sw_twelvefoldReflectedTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI27CIRectangleGeneratorKernels36arg_name_bounds_radius_smooths_colorE
+ __ZN2CI27CIRectangleGeneratorKernels42arg_name_bounds_radius_smooths_width_colorE
+ __ZN2CI27CIRectangleGeneratorKernels43arg_name_bounds_radius_softness_sigma_colorE
+ __ZN2CI27CIRectangleGeneratorKernelsL44arg_type_Float4_Float_Float2_Color_DestCoordE
+ __ZN2CI27CIRectangleGeneratorKernelsL50arg_type_Float4_Float_Float2_Float_Color_DestCoordE
+ __ZN2CI27CIRectangleGeneratorKernelsL50arg_type_Float4_Float_Float4_Float_Color_DestCoordE
+ __ZN2CI27format_converter_for_outputENS_11PixelFormatERNS_11ConvertTypeEU13block_pointerFbS0_E
+ __ZN2CI27format_converter_for_outputENS_11PixelFormatERNS_11ConvertTypeEU13block_pointerFbS0_E.cold.1
+ __ZN2CI27sw_ci_colormatrix_canonicalERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI27sw_ci_to_rgb10wide_as_rgba8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI27sw_remap01FromMinus1ToPlus1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI27sw_smarttone_brightness_negERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI27sw_smarttone_brightness_posERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI27sw_triangleKaleidoscopeGeomERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb
+ __ZN2CI28sw_ci_swizzle_rgba8_to_rgb10ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI28sw_colorPolynomialInverseRGBERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI28sw_sparserendering_add_noiseERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI28sw_triangleKaleidoscopeColorERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI29sw_ci_to_argb10wide_as_rgba16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI29sw_pageCurlNoShadowTransitionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI29sw_smartcolor_contrast_darkenERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI30sw_ci_swizzle_rgba8_to_a2bgr10ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI30sw_ci_swizzle_rgba8_to_a2rgb10ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI30sw_smarttone_highlightcontrastERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI31StitchableFunctionDAGDescriptor19is_builder_functionEP8NSString
+ __ZN2CI31StitchableFunctionDAGDescriptorC2Ev
+ __ZN2CI31sw_CIAreaHistogramScaleAndClampERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI31sw_highlightsAndShadows_noblur0ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI31sw_highlightsAndShadows_noblur1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI31sw_highlightsAndShadows_noblur2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI31sw_pageCurlWithShadowTransitionERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI32sw_linearMappingNoSecondaryImageERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI33delete_precompiled_uber_functionsEPNS_24PrecompiledUberFunctionsE
+ __ZN2CI33sw_ci_swizzle_rgba8_to_rgb10_wideERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI33sw_ci_to_rgb10widelinear_as_rgba8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI35sw_ci_to_argb10widelinear_as_rgba16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI35sw_disparityRefinementPreprocessingERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI35sw_simplifiedShapeAwareGradientMaskERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI38sw_ci_swizzle_rgba8_to_rgb10widelinearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI39sw_CIPortraitBlurBlendWithMaskFromAlphaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI39sw_disparityRefinementPreprocessingPow2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI44sw_CIPortraitBlurBlendWithMaskMatteFromAlphaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI47sw_CIPortraitBlurBlendWithMaskMatteFromAlphaYCCERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI5Image20set_base_cgimage_objEP7CGImage
+ __ZN2CI5Image20set_base_surface_objEP11__IOSurface
+ __ZN2CI6roiKeyC1ERKNS_9parentROIE
+ __ZN2CI6sw_addERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI6sw_dstERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI6sw_maxERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI6sw_minERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI6sw_mixERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI6sw_srcERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7CGImageC1EP7CGImageffNS_22ImageLeafContentDigestEPKvNS_8EdgeModeEbbb
+ __ZN2CI7CGImageC2EP7CGImageffNS_22ImageLeafContentDigestEPKvNS_8EdgeModeEbbb
+ __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb
+ __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb.cold.1
+ __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb.cold.2
+ __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb.cold.3
+ __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb.cold.4
+ __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb.cold.5
+ __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb.cold.6
+ __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb.cold.7
+ __ZN2CI7Context21render_processor_nodeEPNS_8TileTaskERKNS_9parentROIEP11__IOSurfacePKv
+ __ZN2CI7Context6renderEPNS_11ProgramNodeERK6CGRect.cold.1
+ __ZN2CI7sw_add4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_add8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_box3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_box4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_box6ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_glowERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_grayERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_lerpERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_otsuERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_tileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI7sw_zoomERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8TileTask14updatePeakListEPK9__CFArray
+ __ZN2CI8TileTask24addAssembledIntermediateEPKNS_4NodeEPK10__CFStringRK6CGRect
+ __ZN2CI8sw_bloomERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_blur1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_blur2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_blur4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_clearERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_cmlutERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_drr_aERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_drr_bERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_drr_gERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_drr_rERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_dstInERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_edgesERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_gaborERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_gloomERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_mesh1ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_mesh2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_mesh4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_mesh8ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_sepiaERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_sobelERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_srcInERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_twirlERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI8sw_whiteERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9CropImage16append_and_unrefEPNS_5ImageE6CGRect
+ __ZN2CI9DAGHelper19TextureReadFunctionC2Ev
+ __ZN2CI9DAGHelper34add_read_pixel_rgb_a_function_infoEmmmmmm
+ __ZN2CI9GLContext12bind_surfaceEP11__IOSurfaceRKNS_17TextureDescriptorEbNS_10SampleModeENS_8EdgeModeEbii
+ __ZN2CI9GLContext12bind_textureEPKvNS_10SampleModeENS_8EdgeModeEbi
+ __ZN2CI9SWContext12bind_surfaceEP11__IOSurfaceRKNS_17TextureDescriptorEbNS_10SampleModeENS_8EdgeModeEbii
+ __ZN2CI9SWContext12bind_textureEPKvNS_10SampleModeENS_8EdgeModeEbi
+ __ZN2CI9sw_ASGh50ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ASGh60ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ASGh66ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ASGh80ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ASGv50ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ASGv60ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ASGv66ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ASGv75ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ASGv80ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_CBHorzERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_CBVertERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_DEWashERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_DE_subERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_DEmax4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ci_l10ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_ci_sqrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_circleERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_cross4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_drosteERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_dstOutERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_fwidthERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_max3x3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_mesh16ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_mesh32ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_min3x3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_mirrorERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_opTileERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CI9sw_srcOutERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPKNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
+ __ZN2CIL10_gatherSDFE
+ __ZN2CIL10_glow_nameE
+ __ZN2CIL12_fwidth_nameE
+ __ZN2CIL13_clampToFrameE
+ __ZN2CIL13_narrowBlur15E
+ __ZN2CIL13_sdfFill_nameE
+ __ZN2CIL13isRootProgramEPKNS_11ProgramNodeE
+ __ZN2CIL14_clampHDR_nameE
+ __ZN2CIL15_areaAveMaxRed4E
+ __ZN2CIL15_ci_writeTG_420E
+ __ZN2CIL15_ci_writeTG_422E
+ __ZN2CIL15_gatherSDF_nameE
+ __ZN2CIL15_glassHighlightE
+ __ZN2CIL15_vertAveMaxRed4E
+ __ZN2CIL16_areaAveMaxRed16E
+ __ZN2CIL16_dfdxdfdyChannelE
+ __ZN2CIL16_horizAveMaxRed4E
+ __ZN2CIL16findProxyProgramERKNS_6roiKeyE
+ __ZN2CIL17_ci_writeSIMD_420E
+ __ZN2CIL17_ci_writeSIMD_422E
+ __ZN2CIL17_distanceFractionE
+ __ZN2CIL17recurseGraphStatsEPNS_4NodeES1_iRNSt3__16vectorIPKS0_NS2_9allocatorIS5_EEEEiPNS2_3mapIS5_NS_13useCountDepthENS2_4lessIS5_EENS6_INS2_4pairIKS5_SB_EEEEEE
+ __ZN2CIL18_clampToFrame_nameE
+ __ZN2CIL18_narrowBlur15_nameE
+ __ZN2CIL19_blurredroundedrectE
+ __ZN2CIL19_signedDistanceMaskE
+ __ZN2CIL19print_program_graphEPKNS_7ContextEmmPKNS_17RenderDestinationEdPKNS_8TileTaskEPKcPNS_4NodeERK6CGRectNS_11PixelFormatE
+ __ZN2CIL20_areaAveMaxRed4_nameE
+ __ZN2CIL20_ci_argb10widelinearE
+ __ZN2CIL20_glassHighlight_nameE
+ __ZN2CIL20_glowMaskNotOppositeE
+ __ZN2CIL20_reduceCropAveMaxRedE
+ __ZN2CIL20_vertAveMaxRed4_nameE
+ __ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ffbf
+ __ZN2CIL21_areaAveMaxRed16_nameE
+ __ZN2CIL21_dfdxdfdyChannel_nameE
+ __ZN2CIL21_horizAveMaxRed4_nameE
+ __ZN2CIL22Convert_Bytes_to_HalfsEPK13vImage_BufferS2_m
+ __ZN2CIL22Convert_Halfs_to_BytesEPK13vImage_BufferS2_m
+ __ZN2CIL22_distanceFraction_nameE
+ __ZN2CIL23Convert_Bytes_to_FloatsEPK13vImage_BufferS2_m
+ __ZN2CIL23Convert_Floats_to_BytesEPK13vImage_BufferS2_m
+ __ZN2CIL23Convert_Floats_to_HalfsEPK13vImage_BufferS2_m
+ __ZN2CIL23Convert_Halfs_to_FloatsEPK13vImage_BufferS2_m
+ __ZN2CIL23Convert_Halfs_to_ShortsEPK13vImage_BufferS2_m
+ __ZN2CIL23Convert_Shorts_to_HalfsEPK13vImage_BufferS2_m
+ __ZN2CIL23_fallbackComputeNormalsE
+ __ZN2CIL23_shapeAwareGradientMaskE
+ __ZN2CIL23_signedDistanceMaskPostE
+ __ZN2CIL23_signedDistanceMaskPrepE
+ __ZN2CIL23_traverse_program_graphENS_6roiKeyERNS_8liveROIsES2_
+ __ZN2CIL24_blurredroundedrect_nameE
+ __ZN2CIL24_glassHighlightFromAlphaE
+ __ZN2CIL24_signedDistanceMask_nameE
+ __ZN2CIL24add_tile_sizes_to_digestENSt3__16vectorINS1_I5IRectNS0_9allocatorIS2_EEEENS3_IS5_EEEERNS_12XXHashHelperE
+ __ZN2CIL25_ci_argb10widelinear_nameE
+ __ZN2CIL25_glowMaskNotOpposite_nameE
+ __ZN2CIL25_reduceCropAveMaxRed_nameE
+ __ZN2CIL25_remap01FromMinus1ToPlus1E
+ __ZN2CIL28_fallbackComputeNormals_nameE
+ __ZN2CIL28_shapeAwareGradientMask_nameE
+ __ZN2CIL28_signedDistanceMaskPost_nameE
+ __ZN2CIL28_signedDistanceMaskPrep_nameE
+ __ZN2CIL29_glassHighlightFromAlpha_nameE
+ __ZN2CIL29arg_type_Sample_PrivDestCoordE
+ __ZN2CIL30_remap01FromMinus1ToPlus1_nameE
+ __ZN2CIL33_ci_to_argb10widelinear_as_rgba16E
+ __ZN2CIL33_simplifiedShapeAwareGradientMaskE
+ __ZN2CIL38_ci_to_argb10widelinear_as_rgba16_nameE
+ __ZN2CIL38_simplifiedShapeAwareGradientMask_nameE
+ __ZN2CIL5_glowE
+ __ZN2CIL7_fwidthE
+ __ZN2CIL8_sdfFillE
+ __ZN2CIL9_clampHDRE
+ __ZNK2CI10ClampImage10lightlevelEv
+ __ZNK2CI10GammaImage10lightlevelEv
+ __ZNK2CI11AffineImage10lightlevelEv
+ __ZNK2CI11CGRectArray8containsERK6CGRect
+ __ZNK2CI11ConvertNode21print_for_graph_shortEP7__sFILE
+ __ZNK2CI11ConvertNode6renderEPNS_8TileTaskEPNS_7ContextERKNSt3__16vectorIPKNS_14intermediate_tENS5_9allocatorIS9_EEEESE_RK6CGRecti
+ __ZNK2CI11ConvertNode6renderEPNS_8TileTaskEPNS_7ContextERKNSt3__16vectorIPKNS_14intermediate_tENS5_9allocatorIS9_EEEESE_RK6CGRecti.cold.1
+ __ZNK2CI11SwitchImage10lightlevelEv
+ __ZNK2CI12MetalContext11blitTextureEPKvNS_7TextureE5IRectS3_S4_
+ __ZNK2CI12MetalContext25available_allocation_sizeEv
+ __ZNK2CI12SetInfoImage10colorspaceEv
+ __ZNK2CI12SetInfoImage10lightlevelEv
+ __ZNK2CI12SetInfoImage10propertiesEv
+ __ZNK2CI12SetInfoImage12roi_of_childE6CGRecti
+ __ZNK2CI12SetInfoImage13output_formatEv
+ __ZNK2CI12SetInfoImage17render_graph_coreEPNS_7ContextEPNS_4NodeERKNSt3__13mapINS_11ImageDigestE6CGRectNS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEEi
+ __ZNK2CI12SetInfoImage18color_for_graphvizEv
+ __ZNK2CI12SetInfoImage18shape_for_graphvizEv
+ __ZNK2CI12SetInfoImage8headroomEv
+ __ZNK2CI12SurfaceImage10lightlevelEv
+ __ZNK2CI12TextureImage10lightlevelEv
+ __ZNK2CI13ProcessorNode21print_for_graph_shortEP7__sFILE
+ __ZNK2CI13ProcessorNode6renderEPNS_8TileTaskEPNS_7ContextERKNSt3__16vectorIPKNS_14intermediate_tENS5_9allocatorIS9_EEEESE_RK6CGRecti
+ __ZNK2CI13ProviderImage10lightlevelEv
+ __ZNK2CI13TileCacheNode4typeEv
+ __ZNK2CI14RenderToBitmap11writeToFileEPKc
+ __ZNK2CI14TextureManager10wiredBytesEv
+ __ZNK2CI15ColorKernelNode30child_is_ArgumentTypeSampler2DEi
+ __ZNK2CI15ColorMatchImage10lightlevelEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE26EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE27EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE42EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE43EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE53EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE56EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE61EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE63EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE64EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE65EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE66EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE73EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE74EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE87EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE89EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE90EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE91EE4typeEv
+ __ZNK2CI15InstanceCountedILNS_4TypeE94EE4typeEv
+ __ZNK2CI15MetalDAGProgram13get_type_nameEv
+ __ZNK2CI15MetalDAGProgram13print_programEP7__sFILE
+ __ZNK2CI15MetalDAGProgram17get_uber_pipelineEv
+ __ZNK2CI15MetalDAGProgram4typeEv
+ __ZNK2CI15RenderToSurface11writeToFileEPKc
+ __ZNK2CI15SampleModeImage10lightlevelEv
+ __ZNK2CI15WarpKernelImage10lightlevelEv
+ __ZNK2CI16ColorKernelImage10lightlevelEv
+ __ZNK2CI16ColorKernelImage20child_argument_indexEi
+ __ZNK2CI16ColorKernelImage23child_uses_roi_callbackEi
+ __ZNK2CI16ColorMatrixImage10lightlevelEv
+ __ZNK2CI16MetalMainProgram16getPipelineStateENS_9NodeIndexE
+ __ZNK2CI16MetalMainProgram17get_uber_pipelineEv
+ __ZNK2CI16PremultiplyImage10lightlevelEv
+ __ZNK2CI16SetHeadroomImage20print_for_graph_coreEP7__sFILE
+ __ZNK2CI16SetHeadroomImage4typeEv
+ __ZNK2CI16SetHeadroomImage8headroomEv
+ __ZNK2CI17ClampToAlphaImage10lightlevelEv
+ __ZNK2CI17GeneralKernelNode20kernel_argument_typeEi
+ __ZNK2CI17GeneralKernelNode30child_is_ArgumentTypeSampler2DEi
+ __ZNK2CI17RenderDestination11writeToFileEPKc
+ __ZNK2CI17SetDepthDataImage11avdepthdataEv
+ __ZNK2CI17SetDepthDataImage20print_for_graph_coreEP7__sFILE
+ __ZNK2CI17SetDepthDataImage4typeEv
+ __ZNK2CI17UberDAGDescriptor13get_type_nameEv
+ __ZNK2CI17UberDAGDescriptor5printEP7__sFILE
+ __ZNK2CI18GeneralKernelImage10lightlevelEv
+ __ZNK2CI18GeneralKernelImage23child_uses_roi_callbackEi
+ __ZNK2CI18RenderToMTLTexture11writeToFileEPKc
+ __ZNK2CI19MetalTextureManager10wiredBytesEv
+ __ZNK2CI19ProcessorOutputNode10short_nameEv
+ __ZNK2CI19ProcessorOutputNode11output_is_rEv
+ __ZNK2CI19ProcessorOutputNode12output_depthEv
+ __ZNK2CI19ProcessorOutputNode12output_is_rgEv
+ __ZNK2CI19ProcessorOutputNode12roi_of_childE6CGRecti
+ __ZNK2CI19ProcessorOutputNode13output_formatEv
+ __ZNK2CI19ProcessorOutputNode14output_is_lumaEv
+ __ZNK2CI19ProcessorOutputNode16add_args_to_hashERNS_12XXHashHelperE
+ __ZNK2CI19ProcessorOutputNode16extent_unclampedEv
+ __ZNK2CI19ProcessorOutputNode18color_for_graphvizEv
+ __ZNK2CI19ProcessorOutputNode18shape_for_graphvizEv
+ __ZNK2CI19ProcessorOutputNode20print_for_graph_coreEP7__sFILERKNSt3__113unordered_mapIPKNS_11GraphObjectEjNS3_4hashIS7_EENS3_8equal_toIS7_EENS3_9allocatorINS3_4pairIKS7_jEEEEEEb
+ __ZNK2CI19ProcessorOutputNode21may_be_extended_rangeEv
+ __ZNK2CI19ProcessorOutputNode4typeEv
+ __ZNK2CI19ProcessorOutputNode6extentEv
+ __ZNK2CI19ProcessorOutputNode9alpha_oneEv
+ __ZNK2CI19RenderToPixelBuffer11writeToFileEPKc
+ __ZNK2CI20ProcessorOutputImage12roi_of_childE6CGRecti
+ __ZNK2CI20ProcessorOutputImage13output_formatEv
+ __ZNK2CI20ProcessorOutputImage16add_args_to_hashERNS_12XXHashHelperENS_5Image13eDigestReasonE
+ __ZNK2CI20ProcessorOutputImage16extent_unclampedEv
+ __ZNK2CI20ProcessorOutputImage17render_graph_coreEPNS_7ContextERNS_14ImageToNodeMapERKNSt3__13mapINS_11ImageDigestE6CGRectNS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEEi
+ __ZNK2CI20ProcessorOutputImage17render_graph_coreEPNS_7ContextERNS_14ImageToNodeMapERKNSt3__13mapINS_11ImageDigestE6CGRectNS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEEi.cold.1
+ __ZNK2CI20ProcessorOutputImage18color_for_graphvizEv
+ __ZNK2CI20ProcessorOutputImage18print_for_graphvizEP7__sFILERKNSt3__113unordered_mapIPKNS_11GraphObjectEjNS3_4hashIS7_EENS3_8equal_toIS7_EENS3_9allocatorINS3_4pairIKS7_jEEEEEEb
+ __ZNK2CI20ProcessorOutputImage18shape_for_graphvizEv
+ __ZNK2CI20ProcessorOutputImage20print_for_graph_coreEP7__sFILE
+ __ZNK2CI20ProcessorOutputImage4typeEv
+ __ZNK2CI20ProcessorOutputImage6extentEv
+ __ZNK2CI20ProcessorOutputImage9alpha_oneEv
+ __ZNK2CI24PrecompiledUberFunctions13getUberShaderEP7NSArrayIP8NSStringES3_
+ __ZNK2CI24PrecompiledUberFunctions16getFunctionArrayEP7NSArrayIP8NSStringE
+ __ZNK2CI24PrecompiledUberFunctions16getFunctionArrayEP7NSArrayIP8NSStringE.cold.1
+ __ZNK2CI24PrecompiledUberFunctions17getUberShaderNameEP7NSArrayIP8NSStringEmm
+ __ZNK2CI24PrecompiledUberFunctions17getUberShaderNameEP7NSArrayIP8NSStringEmm.cold.1
+ __ZNK2CI24PrecompiledUberFunctions28getFunctionArrayNoDuplicatesEP7NSArrayIP8NSStringE
+ __ZNK2CI24PrecompiledUberFunctions28getFunctionArrayNoDuplicatesEP7NSArrayIP8NSStringE.cold.1
+ __ZNK2CI25SetAverageLightLevelImage10lightlevelEv
+ __ZNK2CI25SetAverageLightLevelImage20print_for_graph_coreEP7__sFILE
+ __ZNK2CI25SetAverageLightLevelImage4typeEv
+ __ZNK2CI4Node20print_for_graph_coreEP7__sFILE
+ __ZNK2CI5Image10lightlevelEv
+ __ZNK2CI5Image16base_cgimage_objEv
+ __ZNK2CI5Image16base_surface_objEv
+ __ZNK2CI7CGImage10lightlevelEv
+ __ZNK2CI7Context12assembleBlitEP11__IOSurface5IRectS2_S3_RKNS_17TextureDescriptorE
+ __ZNK2CI7Context17createDestinationEPNS_14TextureManagerERKNS_6roiKeyENS_11PixelFormatE
+ __ZNK2CI7Context19converter_for_inputENS_11PixelFormatERNS_11ConvertTypeE
+ __ZNK2CI7Context19swizzler_for_outputENS_11PixelFormatE5IRectNS_15DestinationTypeE
+ __ZNK2CI7Context20converter_for_outputENS_11PixelFormatERNS_11ConvertTypeE
+ __ZNK2CI7Context25available_allocation_sizeEv
+ __ZNK2CI7Context30format_is_supported_for_outputENS_11PixelFormatENS_15DestinationTypeE5IRect
+ __ZNK2CI8TileTask10fillPixelsEv
+ __ZNK2CI8liveROIs9printListEv
+ __ZNK2CI9CropImage10lightlevelEv
+ __ZNK2CI9FillImage10lightlevelEv
+ __ZNK2CI9NoopImage10lightlevelEv
+ __ZNK2CI9NoopImage12roi_of_childE6CGRecti
+ __ZNK4mat311is_identityEv
+ __ZNKRSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8nn200100Ev
+ __ZNKSt3__111__copy_implclB8nn200100INS_21__tree_const_iteratorIdPNS_11__tree_nodeIdPvEElEES7_NS_20back_insert_iteratorINS_6vectorIdNS_9allocatorIdEEEEEEEENS_4pairIT_T1_EESF_T0_SG_
+ __ZNKSt3__111__copy_implclB8nn200100IPN2CI15SerialRectArray7roiDataES5_S5_EENS_4pairIT_T1_EES7_T0_S8_
+ __ZNKSt3__111__copy_implclB8nn200100IPNS_6vectorI5IRectNS_9allocatorIS3_EEEES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8nn200100IPN2CI15SerialRectArray7roiDataES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
+ __ZNKSt3__112__hash_tableIN2CI11OtherDigestENS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorIS2_EEE4findIS2_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNKSt3__112__hash_tableIN2CI17NodeContentDigestENS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorIS2_EEE4findIS2_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
+ __ZNKSt3__112__hash_tableIPKN2CI4NodeENS_4hashIS4_EENS_8equal_toIS4_EENS_9allocatorIS4_EEE4findIS4_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS4_PvEEEERKT_
+ __ZNKSt3__112__hash_tableIPN2CI11GraphObjectENS_4hashIS3_EENS_8equal_toIS3_EENS_9allocatorIS3_EEE4findIS3_EENS_21__hash_const_iteratorIPNS_11__hash_nodeIS3_PvEEEERKT_
+ __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8nn200100Ev
+ __ZNSt3__110unique_ptrIN2CI14intermediate_tENS_14default_deleteIS2_EEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIN2CI13ProgramDigestENS3_11ObjectCacheINS3_11MainProgramES4_Lb0EE5EntryEEEPvEENS_22__hash_node_destructorINS_9allocatorISB_EEEEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN2CI11ObjectCacheINS3_11ProgramNodeEyLb0EE5EntryEEEPvEENS_22__hash_node_destructorINS_9allocatorISA_EEEEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__hash_nodeINS_17__hash_value_typeIyN2CI11ObjectCacheINS3_4NodeEyLb0EE5EntryEEEPvEENS_22__hash_node_destructorINS_9allocatorISA_EEEEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIyN2CI14MetalDAGHelper19TextureReadFunctionEEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B8nn200100Ev
+ __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIyN2CI9DAGHelper19TextureReadFunctionEEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEED1B8nn200100Ev
+ __ZNSt3__111__sift_downB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_OT0_NS_15iterator_traitsISD_E15difference_typeESD_
+ __ZNSt3__111__sift_downB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_OT0_NS_15iterator_traitsISD_E15difference_typeESD_
+ __ZNSt3__111__sift_downB8nn200100INS_17_ClassicAlgPolicyERZZ46-[CIPerspectiveAutoCalcV1 clusterLineSegments]ENK3$_0clERKNS_6vectorIN2CI11Perspective4LineENS_9allocatorIS6_EEEEmEUlRKZ46-[CIPerspectiveAutoCalcV1 clusterLineSegments]E10HypothesisSE_E_NS_11__wrap_iterIPSC_EEEEvT1_OT0_NS_15iterator_traitsISK_E15difference_typeESK_
+ __ZNSt3__111__sift_downB8nn200100INS_17_ClassicAlgPolicyERZZ46-[CIPerspectiveAutoCalcV2 clusterLineSegments]ENK3$_0clERKNS_6vectorIN2CI11Perspective4LineENS_9allocatorIS6_EEEEmEUlRKZ46-[CIPerspectiveAutoCalcV2 clusterLineSegments]E10HypothesisSE_E_NS_11__wrap_iterIPSC_EEEEvT1_OT0_NS_15iterator_traitsISK_E15difference_typeESK_
+ __ZNSt3__112__destroy_atB8nn200100INS_4pairIKyN2CI14MetalDAGHelper19TextureReadFunctionEEELi0EEEvPT_
+ __ZNSt3__112__destroy_atB8nn200100INS_4pairIKyN2CI9DAGHelper19TextureReadFunctionEEELi0EEEvPT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CI13ProgramDigestENS2_11ObjectCacheINS2_11MainProgramES3_Lb0EE5EntryEEENS_22__unordered_map_hasherIS3_S8_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE28__node_insert_unique_performB8nn200100EPNS_11__hash_nodeIS8_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CI13ProgramDigestENS2_11ObjectCacheINS2_11MainProgramES3_Lb0EE5EntryEEENS_22__unordered_map_hasherIS3_S8_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE28__node_insert_unique_prepareB8nn200100EmRS8_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CI9NodeIndexENS2_4Node9NodeStatsEEENS_22__unordered_map_hasherIS3_S6_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS5_S8_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS5_S8_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE25__emplace_unique_key_argsIS5_JRKNS_21piecewise_construct_tENS_5tupleIJRKS5_EEENSO_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS5_S8_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE4findIS5_EENS_15__hash_iteratorIPNS_11__hash_nodeIS8_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS5_S8_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS5_S8_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS5_S8_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEEC2EOSJ_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS5_S8_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS2_11CGRectArrayEEENS_22__unordered_map_hasherIS4_S6_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS2_11CGRectArrayEEENS_22__unordered_map_hasherIS4_S6_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS6_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS2_11CGRectArrayEEENS_22__unordered_map_hasherIS4_S6_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJRKS4_EEENSM_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS2_11CGRectArrayEEENS_22__unordered_map_hasherIS4_S6_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS2_11CGRectArrayEEENS_22__unordered_map_hasherIS4_S6_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeIS7_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE20__node_insert_uniqueEPNS_11__hash_nodeIS7_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE21__emplace_unique_implIJRKNS_21piecewise_construct_tENS_5tupleIJRKyEEENSN_IJRKPS4_RyRKjEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEEDpOT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE28__node_insert_unique_performB8nn200100EPNS_11__hash_nodeIS7_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE28__node_insert_unique_prepareB8nn200100EmRS7_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE4findIyEENS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEERKT_
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE5clearEv
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE6removeENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE8__rehashILb1EEEvm
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEED2Ev
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_4NodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE28__node_insert_unique_performB8nn200100EPNS_11__hash_nodeIS7_PvEE
+ __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_4NodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE28__node_insert_unique_prepareB8nn200100EmRS7_
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE17__assign_externalEPKcm
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE21__grow_by_and_replaceEmmmmmmPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE6resizeEmc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100ILi0EEEPKc
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn200100ENS_24__uninitialized_size_tagEmRKS4_
+ __ZNSt3__113__tree_removeB8nn200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__114__split_bufferIN2CI15SerialRectArray7roiDataERNS_9allocatorIS3_EEE5clearB8nn200100Ev
+ __ZNSt3__114__split_bufferIN2CI21SoftwareDAGDescriptor12ArgumentInfoERNS_9allocatorIS3_EEE5clearB8nn200100Ev
+ __ZNSt3__114__split_bufferIN2CI22SWRendererFunctionNodeERNS_9allocatorIS2_EEE5clearB8nn200100Ev
+ __ZNSt3__114__split_bufferINS_10unique_ptrIN2CI8TileTaskENS2_13ObjectDeleterIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8nn200100EPS6_
+ __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEE17__destruct_at_endB8nn200100EPS6_
+ __ZNSt3__114__split_bufferINS_6vectorIN2CI11Perspective3LSRI8EDAnchorEENS_9allocatorIS6_EEEERNS7_IS9_EEE17__destruct_at_endB8nn200100EPS9_
+ __ZNSt3__114__split_bufferIPKvRNS_9allocatorIS2_EEE12emplace_backIJRKS2_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPKvRNS_9allocatorIS2_EEE12emplace_backIJS2_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryENS_9allocatorIS4_EEE12emplace_backIJRS4_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryENS_9allocatorIS4_EEE12emplace_backIJS4_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryENS_9allocatorIS4_EEE13emplace_frontIJS4_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryERNS_9allocatorIS4_EEE12emplace_backIJS4_EEEvDpOT_
+ __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryERNS_9allocatorIS4_EEE13emplace_frontIJRS4_EEEvDpOT_
+ __ZNSt3__115allocate_sharedB8nn200100IN2CI17UberDAGDescriptorENS_9allocatorIS2_EEJRPKNS1_12MetalContextEELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8nn200100IN2CI19LegacyDAGDescriptorENS_9allocatorIS2_EEJRbS5_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115allocate_sharedB8nn200100IN2CI31StitchableFunctionDAGDescriptorENS_9allocatorIS2_EEJRbS5_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
+ __ZNSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE15__init_buf_ptrsB8nn200100Ev
+ __ZNSt3__116__insertion_sortB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_T0_
+ __ZNSt3__116__insertion_sortB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_T0_
+ __ZNSt3__116__pad_and_outputB8nn200100IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
+ __ZNSt3__116allocator_traitsINS_9allocatorIN2CI15SerialRectArray7roiDataEEEE7destroyB8nn200100IS4_vLi0EEEvRS5_PT_
+ __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn200100Ev
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI11MTLDataTypeEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI13LineCostProxyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI22MTLArgumentTypePrivateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI24UberFunctionArgumentInfoEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI29MTLImageFilterFunctionInfoSPIEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI37MTLImageFilterFunctionArgumentInfoSPIEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI5IRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI6CGRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI7EDChainEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorI8EDAnchorEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI11Perspective3LSRI8EDAnchorEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI11Perspective4LineEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI11Perspective9NMSimplexIDv2_fE8NMVertexEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI11Perspective9NMSimplexIDv3_fE8NMVertexEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI13TraverseVisitEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI15SerialRectArray7roiDataEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI17NodeContentDigestEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI18ConstTraverseVisitEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI18KernelArgumentTypeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI21SoftwareDAGDescriptor12ArgumentInfoEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI22SWRendererFunctionNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI27SWRendererFunctionInputNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI6roiKeyEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI7TextureEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI8roiTupleEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI9NodeIndexEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIN2CI9parentROIEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_10unique_ptrIN2CI8TileTaskENS3_13ObjectDeleterIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_4pairI6CGRectmEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_4pairIdiEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_6vectorI5IRectNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_6vectorI6CGRectNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_6vectorIN2CI11Perspective3LSRI8EDAnchorEENS1_IS7_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorINS_6vectorINS_4pairIdiEENS1_IS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIP11__IOSurfaceEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIP5QueueEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIP8NSStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPKN2CI14intermediate_tEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPKN2CI4NodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPKcEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPN2CI17SurfaceCacheEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPN2CI25ConcatenatedDAGDescriptor17MetalArgumentInfoEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPPN2CI17SurfaceCacheEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIjEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__119__partial_sort_implB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_SC_EET1_SD_SD_T2_OT0_
+ __ZNSt3__119__partial_sort_implB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_SC_EET1_SD_SD_T2_OT0_
+ __ZNSt3__119__shared_weak_count16__release_sharedB8nn200100Ev
+ __ZNSt3__120__shared_ptr_emplaceIN2CI17UberDAGDescriptorENS_9allocatorIS2_EEE16__on_zero_sharedEv
+ __ZNSt3__120__shared_ptr_emplaceIN2CI17UberDAGDescriptorENS_9allocatorIS2_EEE21__on_zero_shared_weakEv
+ __ZNSt3__120__shared_ptr_emplaceIN2CI17UberDAGDescriptorENS_9allocatorIS2_EEEC2B8nn200100IJRPKNS1_12MetalContextEES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN2CI17UberDAGDescriptorENS_9allocatorIS2_EEED0Ev
+ __ZNSt3__120__shared_ptr_emplaceIN2CI17UberDAGDescriptorENS_9allocatorIS2_EEED1Ev
+ __ZNSt3__120__shared_ptr_emplaceIN2CI19LegacyDAGDescriptorENS_9allocatorIS2_EEEC2B8nn200100IJRbS7_ES4_Li0EEES4_DpOT_
+ __ZNSt3__120__shared_ptr_emplaceIN2CI31StitchableFunctionDAGDescriptorENS_9allocatorIS2_EEEC2B8nn200100IJRbS7_ES4_Li0EEES4_DpOT_
+ __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN2CI10SWFunctionEEEPvEEEEEclB8nn200100EPSD_
+ __ZNSt3__124__put_character_sequenceB8nn200100IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
+ __ZNSt3__126__insertion_sort_unguardedB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_T0_
+ __ZNSt3__126__insertion_sort_unguardedB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEbT1_SD_T0_
+ __ZNSt3__127__insertion_sort_incompleteB8nn200100INS_17_ClassicAlgPolicyERZZNK2CI8TileTask15pixelsOverdrawnEvENK3$_0clERKNS_6vectorI6CGRectNS_9allocatorIS6_EEEEEUlNS_4pairIdiEESD_E_PSD_EEbT1_SH_T0_
+ __ZNSt3__127__tree_balance_after_insertB8nn200100IPNS_16__tree_node_baseIPvEEEEvT_S5_
+ __ZNSt3__130__uninitialized_allocator_copyB8nn200100INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
+ __ZNSt3__131__partition_with_equals_on_leftB8nn200100INS_17_ClassicAlgPolicyEPN2CI11Perspective9NMSimplexIDv2_fE8NMVertexERZNS6_13orderVerticesEvEUlRKS7_SA_E_EET0_SD_SD_T1_
+ __ZNSt3__131__partition_with_equals_on_leftB8nn200100INS_17_ClassicAlgPolicyEPN2CI11Perspective9NMSimplexIDv3_fE8NMVertexERZNS6_13orderVerticesEvEUlRKS7_SA_E_EET0_SD_SD_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8nn200100INS_17_ClassicAlgPolicyEPN2CI11Perspective9NMSimplexIDv2_fE8NMVertexERZNS6_13orderVerticesEvEUlRKS7_SA_E_EENS_4pairIT0_bEESE_SE_T1_
+ __ZNSt3__132__partition_with_equals_on_rightB8nn200100INS_17_ClassicAlgPolicyEPN2CI11Perspective9NMSimplexIDv3_fE8NMVertexERZNS6_13orderVerticesEvEUlRKS7_SA_E_EENS_4pairIT0_bEESE_SE_T1_
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn200100INS_9allocatorIN2CI15SerialRectArray7roiDataEEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn200100INS_9allocatorIN2CI21SoftwareDAGDescriptor12ArgumentInfoEEEPS4_EEvRT_T0_S9_S9_
+ __ZNSt3__134__uninitialized_allocator_relocateB8nn200100INS_9allocatorIN2CI22SWRendererFunctionNodeEEEPS3_EEvRT_T0_S8_S8_
+ __ZNSt3__135__uninitialized_allocator_copy_implB8nn200100INS_9allocatorIN2CI15SerialRectArray7roiDataEEEPS4_S6_S6_EET2_RT_T0_T1_S7_
+ __ZNSt3__13mapIN2CI10ImageIndexENS1_30ImageDigestForRenderGraphCacheENS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S3_EEEEE6insertB8nn200100INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIS2_S3_EEPNS_11__tree_nodeISG_PvEElEEEEEEvT_SN_
+ __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN2CI10SWFunctionENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEEC2B8nn200100ESt16initializer_listISD_ERKSA_
+ __ZNSt3__13setIPKcNS_4lessIS2_EENS_9allocatorIS2_EEE6insertB8nn200100INS_21__tree_const_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEEEvT_SF_
+ __ZNSt3__13setIPKcNS_4lessIS2_EENS_9allocatorIS2_EEEC2B8nn200100ERKS7_
+ __ZNSt3__14pairIKN2CI13ProgramDigestENS1_11ObjectCacheINS1_11MainProgramES2_Lb0EE5EntryEEC2B8nn200100IJRS3_EJRKPS5_RyRKjEJLm0EEJLm0ELm1ELm2EEEENS_21piecewise_construct_tERNS_5tupleIJDpT_EEERNSI_IJDpT0_EEENS_15__tuple_indicesIJXspT1_EEEENSR_IJXspT2_EEEE
+ __ZNSt3__14pairIKN2CI9NodeIndexENS1_4Node9NodeStatsEED1Ev
+ __ZNSt3__14pairIKyN2CI11ObjectCacheINS2_11ProgramNodeEyLb0EE5EntryEEC2B8nn200100IJRS1_EJRKPS4_RyRKjEJLm0EEJLm0ELm1ELm2EEEENS_21piecewise_construct_tERNS_5tupleIJDpT_EEERNSH_IJDpT0_EEENS_15__tuple_indicesIJXspT1_EEEENSQ_IJXspT2_EEEE
+ __ZNSt3__14pairIKyN2CI11ObjectCacheINS2_4NodeEyLb0EE5EntryEEC2B8nn200100IJRS1_EJRKPS4_RyRKjEJLm0EEJLm0ELm1ELm2EEEENS_21piecewise_construct_tERNS_5tupleIJDpT_EEERNSH_IJDpT0_EEENS_15__tuple_indicesIJXspT1_EEEENSQ_IJXspT2_EEEE
+ __ZNSt3__15dequeIPN2CI17SurfaceCacheEntryENS_9allocatorIS3_EEED2B8nn200100Ev
+ __ZNSt3__16__treeIN2CI9NodeIndexENS_4lessIS2_EENS_9allocatorIS2_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSC_SC_
+ __ZNSt3__16__treeIN2CI9NodeIndexENS_4lessIS2_EENS_9allocatorIS2_EEE25__emplace_unique_key_argsIS2_JRKS2_EEENS_4pairINS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeIN2CI9NodeIndexENS_4lessIS2_EENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIN2CI9NodeIndexEiEENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSG_SG_
+ __ZNSt3__16__treeINS_12__value_typeIN2CI9NodeIndexEiEENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsIS3_JRKNS_21piecewise_construct_tENS_5tupleIJRKS3_EEENSG_IJEEEEEENS_4pairINS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIN2CI9NodeIndexEiEENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE7destroyEPNS_11__tree_nodeIS4_PvEE
+ __ZNSt3__16__treeINS_12__value_typeIP32MTLFunctionStitchingFunctionNodeiEENS_19__map_value_compareIS3_S4_NS_4lessIS3_EELb1EEENS_9allocatorIS4_EEE25__emplace_unique_key_argsIS3_JRKNS_21piecewise_construct_tENS_5tupleIJRKS3_EEENSG_IJEEEEEENS_4pairINS_15__tree_iteratorIS4_PNS_11__tree_nodeIS4_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIyiEENS_19__map_value_compareIyS2_NS_4lessIyEELb1EEENS_9allocatorIS2_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSE_SE_
+ __ZNSt3__16__treeINS_12__value_typeIyiEENS_19__map_value_compareIyS2_NS_4lessIyEELb1EEENS_9allocatorIS2_EEE25__emplace_unique_key_argsIyJRKNS_21piecewise_construct_tENS_5tupleIJRKyEEENSE_IJEEEEEENS_4pairINS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeINS_12__value_typeIyiEENS_19__map_value_compareIyS2_NS_4lessIyEELb1EEENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeIP32MTLFunctionStitchingFunctionNodeNS_4lessIS2_EENS_9allocatorIS2_EEE16__insert_node_atEPNS_15__tree_end_nodeIPNS_16__tree_node_baseIPvEEEERSC_SC_
+ __ZNSt3__16__treeIP32MTLFunctionStitchingFunctionNodeNS_4lessIS2_EENS_9allocatorIS2_EEE25__emplace_unique_key_argsIS2_JRKS2_EEENS_4pairINS_15__tree_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEbEERKT_DpOT0_
+ __ZNSt3__16__treeIP32MTLFunctionStitchingFunctionNodeNS_4lessIS2_EENS_9allocatorIS2_EEE7destroyEPNS_11__tree_nodeIS2_PvEE
+ __ZNSt3__16__treeIZN2CI7Context16recursive_renderEPNS1_8TileTaskERKNS1_6roiKeyEPKNS1_4NodeEbE8childKeyZNS2_16recursive_renderES4_S7_SA_bE12compareDepthNS_9allocatorISB_EEE7destroyEPNS_11__tree_nodeISB_PvEE
+ __ZNSt3__16__treeImNS_4lessImEENS_9allocatorImEEE25__emplace_unique_key_argsImJRKmEEENS_4pairINS_15__tree_iteratorImPNS_11__tree_nodeImPvEElEEbEERKT_DpOT0_
+ __ZNSt3__16localeC1Ev
+ __ZNSt3__16vectorI11MTLDataTypeNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI11MTLDataTypeNS_9allocatorIS1_EEE9push_backB8nn200100EOS1_
+ __ZNSt3__16vectorI13LineCostProxyNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI13LineCostProxyNS_9allocatorIS1_EEE9push_backB8nn200100EOS1_
+ __ZNSt3__16vectorI22MTLArgumentTypePrivateNS_9allocatorIS1_EEE12emplace_backIJS1_EEERS1_DpOT_
+ __ZNSt3__16vectorI22MTLArgumentTypePrivateNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI22MTLArgumentTypePrivateNS_9allocatorIS1_EEE9push_backB8nn200100ERKS1_
+ __ZNSt3__16vectorI24UberFunctionArgumentInfoNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI29MTLImageFilterFunctionInfoSPINS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI29MTLImageFilterFunctionInfoSPINS_9allocatorIS1_EEE9push_backB8nn200100EOS1_
+ __ZNSt3__16vectorI37MTLImageFilterFunctionArgumentInfoSPINS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI37MTLImageFilterFunctionArgumentInfoSPINS_9allocatorIS1_EEE9push_backB8nn200100EOS1_
+ __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEE18__assign_with_sizeB8nn200100IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEEC2B8nn200100ERKS4_
+ __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEEC2B8nn200100Em
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE18__assign_with_sizeB8nn200100IPS1_S6_EEvT_T0_l
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE18__insert_with_sizeB8nn200100INS_11__wrap_iterIPKS1_EES9_EENS6_IPS1_EES9_T_T0_l
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE9push_backB8nn200100ERKS1_
+ __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEEC2B8nn200100ERKS4_
+ __ZNSt3__16vectorI7EDChainNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI8EDAnchorNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorI8EDAnchorNS_9allocatorIS1_EEE9push_backB8nn200100EOS1_
+ __ZNSt3__16vectorI8EDAnchorNS_9allocatorIS1_EEE9push_backB8nn200100ERKS1_
+ __ZNSt3__16vectorIN2CI11Perspective3LSRI8EDAnchorEENS_9allocatorIS5_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI11Perspective4LineENS_9allocatorIS3_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CI11Perspective4LineENS_9allocatorIS3_EEE18__assign_with_sizeB8nn200100IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN2CI11Perspective4LineENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI11Perspective4LineENS_9allocatorIS3_EEE9push_backB8nn200100EOS3_
+ __ZNSt3__16vectorIN2CI11Perspective4LineENS_9allocatorIS3_EEE9push_backB8nn200100ERKS3_
+ __ZNSt3__16vectorIN2CI11Perspective9NMSimplexIDv2_fE8NMVertexENS_9allocatorIS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI11Perspective9NMSimplexIDv3_fE8NMVertexENS_9allocatorIS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI13TraverseVisitENS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CI13TraverseVisitENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE16__init_with_sizeB8nn200100IPS3_S8_EEvT_T0_m
+ __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE18__assign_with_sizeB8nn200100IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE24__emplace_back_slow_pathIJRKS3_EEEPS3_DpOT_
+ __ZNSt3__16vectorIN2CI17NodeContentDigestENS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CI17NodeContentDigestENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI18ConstTraverseVisitENS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CI18ConstTraverseVisitENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEE18__assign_with_sizeB8nn200100IPS2_S7_EEvT_T0_l
+ __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEE9push_backB8nn200100EOS2_
+ __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEEC2B8nn200100ERKS5_
+ __ZNSt3__16vectorIN2CI21SoftwareDAGDescriptor12ArgumentInfoENS_9allocatorIS3_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorIN2CI21SoftwareDAGDescriptor12ArgumentInfoENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI22SWRendererFunctionNodeENS_9allocatorIS2_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorIN2CI22SWRendererFunctionNodeENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI27SWRendererFunctionInputNodeENS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CI27SWRendererFunctionInputNodeENS_9allocatorIS2_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorIN2CI27SWRendererFunctionInputNodeENS_9allocatorIS2_EEE16__init_with_sizeB8nn200100IPS2_S7_EEvT_T0_m
+ __ZNSt3__16vectorIN2CI27SWRendererFunctionInputNodeENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI6roiKeyENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_
+ __ZNSt3__16vectorIN2CI8roiTupleENS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CI8roiTupleENS_9allocatorIS2_EEE18__assign_with_sizeB8nn200100IPS2_S7_EEvT_T0_l
+ __ZNSt3__16vectorIN2CI8roiTupleENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI9NodeIndexENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEE18__assign_with_sizeB8nn200100IPS2_S7_EEvT_T0_l
+ __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEE18__insert_with_sizeB8nn200100INS_11__wrap_iterIPKS2_EESA_EENS7_IPS2_EESA_T_T0_l
+ __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEE9push_backB8nn200100ERKS2_
+ __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEEC2B8nn200100ERKS5_
+ __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE16__init_with_sizeB8nn200100IPS4_S8_EEvT_T0_m
+ __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE18__assign_with_sizeB8nn200100IPS4_S8_EEvT_T0_l
+ __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEEC2B8nn200100Em
+ __ZNSt3__16vectorINS0_I6CGRectNS_9allocatorIS1_EEEENS2_IS4_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorINS0_I6CGRectNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS0_I6CGRectNS_9allocatorIS1_EEEENS2_IS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS0_I6CGRectNS_9allocatorIS1_EEEENS2_IS4_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorINS0_I6CGRectNS_9allocatorIS1_EEEENS2_IS4_EEEC2B8nn200100Em
+ __ZNSt3__16vectorINS0_IN2CI11Perspective3LSRI8EDAnchorEENS_9allocatorIS5_EEEENS6_IS8_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS0_IN2CI11Perspective3LSRI8EDAnchorEENS_9allocatorIS5_EEEENS6_IS8_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS0_IN2CI11Perspective3LSRI8EDAnchorEENS_9allocatorIS5_EEEENS6_IS8_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEEC2B8nn200100Em
+ __ZNSt3__16vectorINS_10unique_ptrIN2CI8TileTaskENS2_13ObjectDeleterIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN2CI8TileTaskENS2_13ObjectDeleterIS3_EEEENS_9allocatorIS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_10unique_ptrIN2CI8TileTaskENS2_13ObjectDeleterIS3_EEEENS_9allocatorIS6_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8nn200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8nn200100IPS6_SA_EEvT_T0_m
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB8nn200100IPS6_SA_EEvT_T0_l
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE5clearB8nn200100Ev
+ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE9push_backB8nn200100EOS6_
+ __ZNSt3__16vectorINS_4pairI6CGRectmEENS_9allocatorIS3_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorINS_4pairI6CGRectmEENS_9allocatorIS3_EEE18__assign_with_sizeB8nn200100IPS3_S8_EEvT_T0_l
+ __ZNSt3__16vectorINS_4pairI6CGRectmEENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairI6CGRectmEENS_9allocatorIS3_EEE9push_backB8nn200100EOS3_
+ __ZNSt3__16vectorINS_4pairI6CGRectmEENS_9allocatorIS3_EEEC2B8nn200100ERKS6_
+ __ZNSt3__16vectorINS_4pairIdiEENS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorINS_4pairIdiEENS_9allocatorIS2_EEE9push_backB8nn200100ERKS2_
+ __ZNSt3__16vectorIP11__IOSurfaceNS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIP11__IOSurfaceNS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIP5QueueNS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIP8NSStringNS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIP8NSStringNS_9allocatorIS2_EEE9push_backB8nn200100EOS2_
+ __ZNSt3__16vectorIPKN2CI14intermediate_tENS_9allocatorIS4_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIPKN2CI14intermediate_tENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPKN2CI14intermediate_tENS_9allocatorIS4_EEEC2B8nn200100ERKS7_
+ __ZNSt3__16vectorIPKN2CI4NodeENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE9push_backB8nn200100EOS2_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE6insertENS_11__wrap_iterIPKS2_EEOS2_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE6insertENS_11__wrap_iterIPKS2_EERS7_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEE9push_backB8nn200100EOS2_
+ __ZNSt3__16vectorIPKvNS_9allocatorIS2_EEEC2B8nn200100ERKS5_
+ __ZNSt3__16vectorIPN2CI17SurfaceCacheEntryENS_9allocatorIS3_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPN2CI17SurfaceCacheEntryENS_9allocatorIS3_EEE9push_backB8nn200100ERKS3_
+ __ZNSt3__16vectorIPN2CI25ConcatenatedDAGDescriptor17MetalArgumentInfoENS_9allocatorIS4_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIPvNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIZ46-[CIPerspectiveAutoCalcV1 clusterLineSegments]E10HypothesisNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIZ46-[CIPerspectiveAutoCalcV2 clusterLineSegments]E10HypothesisNS_9allocatorIS1_EEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE16__init_with_sizeB8nn200100IPbS5_EEvT_T0_m
+ __ZNSt3__16vectorIbNS_9allocatorIbEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIiNS_9allocatorIiEEE9push_backB8nn200100EOi
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIjNS_9allocatorIjEEE9push_backB8nn200100EOj
+ __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorImNS_9allocatorImEEE18__assign_with_sizeB8nn200100IPmS5_EEvT_T0_l
+ __ZNSt3__16vectorImNS_9allocatorImEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorImNS_9allocatorImEEE9push_backB8nn200100EOm
+ __ZNSt3__16vectorImNS_9allocatorImEEE9push_backB8nn200100ERKm
+ __ZNSt3__16vectorImNS_9allocatorImEEEC2B8nn200100ERKS3_
+ __ZNSt3__16vectorImNS_9allocatorImEEEC2B8nn200100ESt16initializer_listImE
+ __ZNSt3__16vectorIsNS_9allocatorIsEEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIsNS_9allocatorIsEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIsNS_9allocatorIsEEEC2B8nn200100ERKS3_
+ __ZNSt3__16vectorIyNS_9allocatorIyEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__17__sort5B8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_Li0EEEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_Li0EEEvT1_SD_SD_SD_SD_T0_
+ __ZNSt3__17__sort5B8nn200100INS_17_ClassicAlgPolicyERZZNK2CI8TileTask15pixelsOverdrawnEvENK3$_0clERKNS_6vectorI6CGRectNS_9allocatorIS6_EEEEEUlNS_4pairIdiEESD_E_PSD_Li0EEEvT1_SH_SH_SH_SH_T0_
+ __ZNSt3__19__sift_upB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_OT0_NS_15iterator_traitsISD_E15difference_typeE
+ __ZNSt3__19__sift_upB8nn200100INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_OT0_NS_15iterator_traitsISD_E15difference_typeE
+ __ZNSt3__1ssB8nn200100IcNS_11char_traitsIcEEEEDaNS_17basic_string_viewIT_T0_EENS_13type_identityIS7_E4typeE
+ __ZNSt3__1ssB8nn200100IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
+ __ZSt28__throw_bad_array_new_lengthB8nn200100v
+ __ZTVN2CI12SetInfoImageE
+ __ZTVN2CI13TileCacheNodeE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE26EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE27EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE42EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE43EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE53EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE56EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE61EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE63EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE64EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE65EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE66EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE73EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE74EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE87EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE89EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE90EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE91EEE
+ __ZTVN2CI15InstanceCountedILNS_4TypeE94EEE
+ __ZTVN2CI15MetalDAGProgramE
+ __ZTVN2CI16SetHeadroomImageE
+ __ZTVN2CI17SetDepthDataImageE
+ __ZTVN2CI17UberDAGDescriptorE
+ __ZTVN2CI19ProcessorOutputNodeE
+ __ZTVN2CI20ProcessorOutputImageE
+ __ZTVN2CI25SetAverageLightLevelImageE
+ __ZTVNSt3__115basic_streambufIcNS_11char_traitsIcEEEE
+ __ZTVNSt3__120__shared_ptr_emplaceIN2CI17UberDAGDescriptorENS_9allocatorIS2_EEEE
+ __ZThn104_N2CI13GLMainProgramD0Ev
+ __ZThn104_N2CI13GLMainProgramD1Ev
+ __ZThn104_N2CI15MetalDAGProgramD0Ev
+ __ZThn104_N2CI15MetalDAGProgramD1Ev
+ __ZThn104_N2CI16MetalMainProgramD0Ev
+ __ZThn104_N2CI16MetalMainProgramD1Ev
+ __ZThn104_NK2CI13GLMainProgram4typeEv
+ __ZThn104_NK2CI15MetalDAGProgram4typeEv
+ __ZThn104_NK2CI16MetalMainProgram4typeEv
+ __ZThn120_N2CI11SwitchImageD0Ev
+ __ZThn120_N2CI11SwitchImageD1Ev
+ __ZThn120_N2CI12SurfaceImageD0Ev
+ __ZThn120_N2CI12SurfaceImageD1Ev
+ __ZThn120_N2CI12TextureImageD0Ev
+ __ZThn120_N2CI12TextureImageD1Ev
+ __ZThn120_N2CI13ProviderImageD0Ev
+ __ZThn120_N2CI13ProviderImageD1Ev
+ __ZThn120_N2CI14GLTextureImageD0Ev
+ __ZThn120_N2CI14GLTextureImageD1Ev
+ __ZThn120_N2CI16ColorKernelImageD0Ev
+ __ZThn120_N2CI16ColorKernelImageD1Ev
+ __ZThn120_N2CI17MetalTextureImageD0Ev
+ __ZThn120_N2CI17MetalTextureImageD1Ev
+ __ZThn120_N2CI18GeneralKernelImageD0Ev
+ __ZThn120_N2CI18GeneralKernelImageD1Ev
+ __ZThn120_N2CI7CGImageD0Ev
+ __ZThn120_N2CI7CGImageD1Ev
+ __ZThn120_N2CI9FillImageD0Ev
+ __ZThn120_N2CI9FillImageD1Ev
+ __ZThn120_NK2CI11SwitchImage4typeEv
+ __ZThn120_NK2CI12SurfaceImage4typeEv
+ __ZThn120_NK2CI12TextureImage4typeEv
+ __ZThn120_NK2CI13ProviderImage4typeEv
+ __ZThn120_NK2CI16ColorKernelImage4typeEv
+ __ZThn120_NK2CI18GeneralKernelImage4typeEv
+ __ZThn120_NK2CI7CGImage4typeEv
+ __ZThn120_NK2CI9FillImage4typeEv
+ __ZThn128_N2CI10ClampImageD0Ev
+ __ZThn128_N2CI10ClampImageD1Ev
+ __ZThn128_N2CI10GammaImageD0Ev
+ __ZThn128_N2CI10GammaImageD1Ev
+ __ZThn128_N2CI11AffineImageD0Ev
+ __ZThn128_N2CI11AffineImageD1Ev
+ __ZThn128_N2CI12SwizzleImageD0Ev
+ __ZThn128_N2CI12SwizzleImageD1Ev
+ __ZThn128_N2CI13SetPropsImageD0Ev
+ __ZThn128_N2CI13SetPropsImageD1Ev
+ __ZThn128_N2CI14ProcessorImageD0Ev
+ __ZThn128_N2CI14ProcessorImageD1Ev
+ __ZThn128_N2CI15ColorMatchImageD0Ev
+ __ZThn128_N2CI15ColorMatchImageD1Ev
+ __ZThn128_N2CI15SampleModeImageD0Ev
+ __ZThn128_N2CI15SampleModeImageD1Ev
+ __ZThn128_N2CI15WarpKernelImageD0Ev
+ __ZThn128_N2CI15WarpKernelImageD1Ev
+ __ZThn128_N2CI16ColorMatrixImageD0Ev
+ __ZThn128_N2CI16ColorMatrixImageD1Ev
+ __ZThn128_N2CI16PremultiplyImageD0Ev
+ __ZThn128_N2CI16PremultiplyImageD1Ev
+ __ZThn128_N2CI16SetHeadroomImageD0Ev
+ __ZThn128_N2CI16SetHeadroomImageD1Ev
+ __ZThn128_N2CI17ClampToAlphaImageD0Ev
+ __ZThn128_N2CI17ClampToAlphaImageD1Ev
+ __ZThn128_N2CI17SetDepthDataImageD0Ev
+ __ZThn128_N2CI17SetDepthDataImageD1Ev
+ __ZThn128_N2CI18TagColorSpaceImageD0Ev
+ __ZThn128_N2CI18TagColorSpaceImageD1Ev
+ __ZThn128_N2CI25SetAverageLightLevelImageD0Ev
+ __ZThn128_N2CI25SetAverageLightLevelImageD1Ev
+ __ZThn128_N2CI9CropImageD0Ev
+ __ZThn128_N2CI9CropImageD1Ev
+ __ZThn128_N2CI9NoopImageD0Ev
+ __ZThn128_N2CI9NoopImageD1Ev
+ __ZThn128_N2CI9SRGBImageD0Ev
+ __ZThn128_N2CI9SRGBImageD1Ev
+ __ZThn128_NK2CI10ClampImage4typeEv
+ __ZThn128_NK2CI10GammaImage4typeEv
+ __ZThn128_NK2CI11AffineImage4typeEv
+ __ZThn128_NK2CI12SwizzleImage4typeEv
+ __ZThn128_NK2CI13SetPropsImage4typeEv
+ __ZThn128_NK2CI14ProcessorImage4typeEv
+ __ZThn128_NK2CI15ColorMatchImage4typeEv
+ __ZThn128_NK2CI15SampleModeImage4typeEv
+ __ZThn128_NK2CI15WarpKernelImage4typeEv
+ __ZThn128_NK2CI16ColorMatrixImage4typeEv
+ __ZThn128_NK2CI16PremultiplyImage4typeEv
+ __ZThn128_NK2CI16SetHeadroomImage4typeEv
+ __ZThn128_NK2CI17ClampToAlphaImage4typeEv
+ __ZThn128_NK2CI17SetDepthDataImage4typeEv
+ __ZThn128_NK2CI18TagColorSpaceImage4typeEv
+ __ZThn128_NK2CI25SetAverageLightLevelImage4typeEv
+ __ZThn128_NK2CI9CropImage4typeEv
+ __ZThn128_NK2CI9NoopImage4typeEv
+ __ZThn128_NK2CI9SRGBImage4typeEv
+ __ZThn176_N2CI15MetalDAGProgramD0Ev
+ __ZThn176_N2CI15MetalDAGProgramD1Ev
+ __ZThn176_NK2CI15MetalDAGProgram4typeEv
+ __ZThn48_N2CI13TileCacheNodeD0Ev
+ __ZThn48_N2CI13TileCacheNodeD1Ev
+ __ZThn48_NK2CI13TileCacheNode4typeEv
+ __ZZ16FOSL_DAG_CODEGENE1v
+ __ZZ18CI_CACHE_TILE_SIZEE1v
+ __ZZ21CI_ARCHIVE_USAGE_MODEE1v
+ __ZZ21CI_ENABLE_UBER_SHADERE1v
+ __ZZ22CI_USE_AIR_UBER_SHADERE1v
+ __ZZ32CI_ALLOW_UBER_SHADER_COMPILATIONE1v
+ __ZZ32CI_WAIT_BEFORE_SWITCHING_TO_UBERE1v
+ __ZZ35CI_ENABLE_METAL_FUNCTION_ATTRIBUTESE1v
+ __ZZ53-[CIImage(QuicklookSupport) _dotStringRepresentation]E8renderer
+ __ZZL24rwtm_constrain_headroomsfffffE17y_lut_lambert_low
+ __ZZL24rwtm_constrain_headroomsfffffE18y_lut_lambert_high
+ __ZZL46getkCMPhotoCompressionOption_BitDepthSymbolLocvE3ptr.0
+ __ZZL47getkCMPhotoCompressionOption_CodecTypeSymbolLocvE3ptr.0
+ __ZZL48getkCMPhotoCompressionOption_ColorSpaceSymbolLocvE3ptr.0
+ __ZZL49getkCMPhotoCompressionOption_SubsamplingSymbolLocvE3ptr.0
+ __ZZL52getkCMPhotoAuxiliaryImageTypeURN_HDRGainMapSymbolLocvE3ptr.0
+ __ZZL52getkCMPhotoCompressionOption_ApplyTransformSymbolLocvE3ptr.0
+ __ZZL56getCMPhotoCompressionSessionAddTmapImageOneShotSymbolLocvE3ptr.0
+ __ZZL58getkCMPhotoAuxiliaryImageTypeURN_SemanticSkyMatteSymbolLocvE3ptr.0
+ __ZZL59getkCMPhotoAuxiliaryImageTypeURN_SemanticHairMatteSymbolLocvE3ptr.0
+ __ZZL59getkCMPhotoAuxiliaryImageTypeURN_SemanticSkinMatteSymbolLocvE3ptr.0
+ __ZZL60getkCMPhotoAuxiliaryImageTypeURN_SemanticTeethMatteSymbolLocvE3ptr.0
+ __ZZL62getkCMPhotoAuxiliaryImageTypeURN_SemanticGlassesMatteSymbolLocvE3ptr.0
+ __ZZL65getkCMPhotoCompressionOption_AuxiliaryImageCustomTypeURNSymbolLocvE3ptr.0
+ __ZZN2CI12MetalContext16render_root_nodeEPNS_8TileTaskERKNS_9parentROIEU13block_pointerFvvES7_EN13SignpostTimerD1E_0v
+ __ZZN2CI12MetalContext24render_intermediate_nodeEPNS_8TileTaskERKNS_9parentROIEPNS_14intermediate_tEbU13block_pointerFvvEEN13SignpostTimerD1E_0v
+ __ZZN2CI15MetalDAGProgram7compileENS_9NodeIndexEEN13SignpostTimerD1Ev
+ __ZZN2CIL24createConverterArrayFromEP12CGColorSpacefbfbfE5mutex
+ __ZZZ112+[CIImage(CIImageProcessor) imageWithExtent:processorDescription:argumentDigest:outputFormat:options:processor:]EUb0_EN13SignpostTimerD1E_0v
+ __ZZZ112+[CIImage(CIImageProcessor) imageWithExtent:processorDescription:argumentDigest:outputFormat:options:processor:]EUb0_EN13SignpostTimerD1Ev
+ __ZZZ65+[CIImageProcessorKernel applyWithExtent:inputs:arguments:error:]EUb1_EN13SignpostTimerD1E_0v
+ __ZZZ65+[CIImageProcessorKernel applyWithExtent:inputs:arguments:error:]EUb1_EN13SignpostTimerD1Ev
+ __ZZZ66+[CIImageProcessorKernel applyWithExtents:inputs:arguments:error:]EUb2_EN13SignpostTimerD1E_0v
+ __ZZZ66+[CIImageProcessorKernel applyWithExtents:inputs:arguments:error:]EUb2_EN13SignpostTimerD1Ev
+ ___104-[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:]_block_invoke
+ ___104-[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:]_block_invoke_2
+ ___112+[CIImage(CIImageProcessor) imageWithExtent:processorDescription:argumentDigest:outputFormat:options:processor:]_block_invoke
+ ___122-[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:]_block_invoke
+ ___122-[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:]_block_invoke.228
+ ___24-[CUIFWidth outputImage]_block_invoke
+ ___26-[CUIDfDxDfDy outputImage]_block_invoke
+ ___26-[CUISDFClamp outputImage]_block_invoke
+ ___30-[CUINarrowBlur15 outputImage]_block_invoke
+ ___30-[CUINarrowBlur15 outputImage]_block_invoke_2
+ ___38-[CIAreaAverageMaximumRed outputImage]_block_invoke
+ ___38-[CIAreaAverageMaximumRed outputImage]_block_invoke_2
+ ___38-[CIAreaAverageMaximumRed outputImage]_block_invoke_3
+ ___38-[CIAreaAverageMaximumRed outputImage]_block_invoke_4
+ ___38-[CIAreaAverageMaximumRed outputImage]_block_invoke_5
+ ___41+[CIFilter(Builtins) systemToneMapFilter]_block_invoke
+ ___49+[CIFilter(Builtins) areaAverageMaximumRedFilter]_block_invoke
+ ___50+[CIFilter(Builtins) roundedQRCodeGeneratorFilter]_block_invoke
+ ___50-[CISignedDistanceGradientFromRedMask outputImage]_block_invoke
+ ___52+[CIContext(Internal) internalSWContextWithOptions:]_block_invoke.299
+ ___54+[CIKernelLibrary(Internal) coreImageDylibWithDevice:]_block_invoke.102
+ ___55+[CIFilter(Builtins) distanceGradientFromRedMaskFilter]_block_invoke
+ ___60+[CIFilter(Builtins) blurredRoundedRectangleGeneratorFilter]_block_invoke
+ ___61+[CIFilter(Builtins) signedDistanceGradientFromRedMaskFilter]_block_invoke
+ ___66+[CIContext(Internal) internalContextWithMTLCommandQueue:options:]_block_invoke.298
+ ___66+[CIImageProcessorKernel applyWithExtents:inputs:arguments:error:]_block_invoke
+ ___66+[CIImageProcessorKernel applyWithExtents:inputs:arguments:error:]_block_invoke_2
+ ___75-[CIContext(ImageRepresentation) _addDepthMap:session:imageHandle:options:]_block_invoke
+ ___82-[CIImage(CIImageProvider) initWithImageProvider:size::format:colorSpace:options:]_block_invoke.31
+ ___AVFCaptureLibraryCore_block_invoke
+ ___ArchiveLibraryUsingDescriptor_block_invoke
+ ___ArchiveLibraryUsingDescriptor_block_invoke.cold.1
+ ___ArchiveLibraryUsingDescriptor_block_invoke.cold.2
+ ___ArchiveLibraryUsingDescriptor_block_invoke.cold.3
+ ___Block_byref_object_copy_.101
+ ___Block_byref_object_copy_.104
+ ___Block_byref_object_copy_.107
+ ___Block_byref_object_copy_.108
+ ___Block_byref_object_copy_.1087
+ ___Block_byref_object_copy_.1092
+ ___Block_byref_object_copy_.11
+ ___Block_byref_object_copy_.111
+ ___Block_byref_object_copy_.126
+ ___Block_byref_object_copy_.13
+ ___Block_byref_object_copy_.15
+ ___Block_byref_object_copy_.17
+ ___Block_byref_object_copy_.288
+ ___Block_byref_object_copy_.33
+ ___Block_byref_object_copy_.41
+ ___Block_byref_object_copy_.43
+ ___Block_byref_object_copy_.47
+ ___Block_byref_object_copy_.547
+ ___Block_byref_object_copy_.58
+ ___Block_byref_object_copy_.61
+ ___Block_byref_object_copy_.67
+ ___Block_byref_object_copy_.99
+ ___Block_byref_object_dispose_.100
+ ___Block_byref_object_dispose_.102
+ ___Block_byref_object_dispose_.105
+ ___Block_byref_object_dispose_.108
+ ___Block_byref_object_dispose_.1088
+ ___Block_byref_object_dispose_.109
+ ___Block_byref_object_dispose_.1093
+ ___Block_byref_object_dispose_.112
+ ___Block_byref_object_dispose_.12
+ ___Block_byref_object_dispose_.127
+ ___Block_byref_object_dispose_.14
+ ___Block_byref_object_dispose_.16
+ ___Block_byref_object_dispose_.18
+ ___Block_byref_object_dispose_.289
+ ___Block_byref_object_dispose_.34
+ ___Block_byref_object_dispose_.42
+ ___Block_byref_object_dispose_.44
+ ___Block_byref_object_dispose_.48
+ ___Block_byref_object_dispose_.548
+ ___Block_byref_object_dispose_.59
+ ___Block_byref_object_dispose_.62
+ ___Block_byref_object_dispose_.68
+ ___CIMetalRenderToImageblocks_block_invoke.110
+ ___CIMetalRenderToTextures_block_invoke.101
+ ___CIMetalRenderToTextures_block_invoke.101.cold.1
+ ___CIMetalRenderToTextures_block_invoke.101.cold.2
+ ___ClearSurface_block_invoke_9
+ ___CopyAnyImagePeakNonVolatileList_block_invoke
+ ___CopyAnyImagePeakNonVolatileList_block_invoke_2
+ ___CopyContextPeakNonVolatileList_block_invoke
+ ___CopyContextPeakNonVolatileList_block_invoke_2
+ ___FutharkLibraryCore_block_invoke
+ ____ZL12post_processP7NSArrayIP21CIImageProcessorInputEPS_IP22CIImageProcessorOutputEPN2CI7ContextE_block_invoke
+ ____ZL19set_context_optionsPN2CI9GLContextEP12NSDictionary_block_invoke.396
+ ____ZL22register_more_builtinsU13block_pointerFvP8NSStringE_block_invoke.1121
+ ____ZL22register_more_builtinsU13block_pointerFvP8NSStringE_block_invoke.1138
+ ____ZL22register_more_builtinsU13block_pointerFvP8NSStringE_block_invoke.1145
+ ____ZL46getkCMPhotoCompressionOption_BitDepthSymbolLocv_block_invoke
+ ____ZL47getkCMPhotoCompressionOption_CodecTypeSymbolLocv_block_invoke
+ ____ZL48getkCMPhotoCompressionOption_ColorSpaceSymbolLocv_block_invoke
+ ____ZL49getkCMPhotoCompressionOption_SubsamplingSymbolLocv_block_invoke
+ ____ZL52getkCMPhotoAuxiliaryImageTypeURN_HDRGainMapSymbolLocv_block_invoke
+ ____ZL52getkCMPhotoCompressionOption_ApplyTransformSymbolLocv_block_invoke
+ ____ZL56getCMPhotoCompressionSessionAddTmapImageOneShotSymbolLocv_block_invoke
+ ____ZL58getkCMPhotoAuxiliaryImageTypeURN_SemanticSkyMatteSymbolLocv_block_invoke
+ ____ZL59getkCMPhotoAuxiliaryImageTypeURN_SemanticHairMatteSymbolLocv_block_invoke
+ ____ZL59getkCMPhotoAuxiliaryImageTypeURN_SemanticSkinMatteSymbolLocv_block_invoke
+ ____ZL60getkCMPhotoAuxiliaryImageTypeURN_SemanticTeethMatteSymbolLocv_block_invoke
+ ____ZL62getkCMPhotoAuxiliaryImageTypeURN_SemanticGlassesMatteSymbolLocv_block_invoke
+ ____ZL65getkCMPhotoCompressionOption_AuxiliaryImageCustomTypeURNSymbolLocv_block_invoke
+ ____ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EE4findEy_block_invoke
+ ____ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EE5EntryD2Ev_block_invoke
+ ____ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EE5clearEv_block_invoke
+ ____ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EE6insertEyPS1_j_block_invoke
+ ____ZN2CI11ObjectCacheINS_11ProgramNodeEyLb0EED2Ev_block_invoke
+ ____ZN2CI11ProgramNode28create_program_and_argumentsEPNS_7ContextEPKc_block_invoke.77
+ ____ZN2CI13KernelArchive10addArchiveEPKv_block_invoke
+ ____ZN2CI14MetalDAGHelper9build_dagEPKNS_4NodeEPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEm_block_invoke.46
+ ____ZN2CI14MetalDAGHelper9build_dagEPKNS_4NodeEPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEm_block_invoke_2.47
+ ____ZN2CI15ColorKernelNode14append_to_treeEPKNS_6KernelEPNS_20SerialObjectPtrArrayE6CGRectU13block_pointerFS6_iS6_EbbNS_11PixelFormatE_block_invoke
+ ____ZN2CI15MetalDAGProgramD2Ev_block_invoke
+ ____ZN2CI16GLTextureManager16attach_IOSurfaceEP11__IOSurfacebiRKNS_17TextureDescriptorEiiibb_block_invoke
+ ____ZN2CI16GLTextureManager16attach_IOSurfaceEP11__IOSurfacebiRKNS_17TextureDescriptorEiiibb_block_invoke.cold.1
+ ____ZN2CI16MetalMainProgram12compileAsyncENS_9NodeIndexE_block_invoke_2
+ ____ZN2CI19MetalTextureManager19create_intermediateERKNS_22IntermediateDescriptorEPKvRK5IRectmb_block_invoke
+ ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxP13vImage_BufferS3_PKvNS_11ConvertTypeE_block_invoke
+ ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxP13vImage_BufferS3_PKvNS_11ConvertTypeE_block_invoke_2
+ ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxP13vImage_BufferS3_PKvNS_11ConvertTypeE_block_invoke_3
+ ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxP13vImage_BufferS3_PKvNS_11ConvertTypeE_block_invoke_4
+ ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxP13vImage_BufferS3_PKvNS_11ConvertTypeE_block_invoke_5
+ ____ZN2CI27format_converter_for_outputENS_11PixelFormatERNS_11ConvertTypeEU13block_pointerFbS0_E_block_invoke
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke.102
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke.19
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_10
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_11
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_12
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_13
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_14
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_17
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_18
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_19
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_2
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_2.112
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_2.22
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_20
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_21
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_22
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_3
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_3.115
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_3.27
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_4
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_4.120
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_5
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_5.124
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_6
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_6.128
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_7
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_7.134
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_8
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_8.136
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_9
+ ____ZN2CI28createMainProgramCodeAndArgsEPNS_7ContextEPKcPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEjb_block_invoke_9.140
+ ____ZN2CI4Node15traverse_uniqueEU13block_pointerFvPKS0_E_block_invoke
+ ____ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb_block_invoke
+ ____ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb_block_invoke.11
+ ____ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPKNS_4NodeEb_block_invoke_2
+ ____ZN2CI7Context6renderEPNS_11ProgramNodeERK6CGRect_block_invoke
+ ____ZN2CI8TileTask13addROIForNodeEPNS_11ProgramNodeERK6CGRect_block_invoke
+ ____ZN2CI8TileTask14updatePeakListEPK9__CFArray_block_invoke
+ ____ZN2CI8TileTask14updatePeakListEPK9__CFArray_block_invoke_2
+ ____ZN2CI8TileTask24addAssembledIntermediateEPKNS_4NodeEPK10__CFStringRK6CGRect_block_invoke
+ ____ZN2CI9DAGHelper9build_dagEPKNS_4NodeEPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEm_block_invoke.22
+ ____ZN2CI9DAGHelper9build_dagEPKNS_4NodeEPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEm_block_invoke_2.23
+ ____ZN2CI9GLContext16render_root_nodeEPNS_8TileTaskERKNS_9parentROIEU13block_pointerFvvES7__block_invoke.38
+ ____ZN2CI9GLContext16render_root_nodeEPNS_8TileTaskERKNS_9parentROIEU13block_pointerFvvES7__block_invoke.38.cold.1
+ ____ZN2CIL13LogCacheStateEbPKc_block_invoke.121
+ ____ZN2CIL13convert_metalEPKNS_12MetalContextE13vImage_BufferP11__IOSurfacePKvNS_11ConvertTypeE_block_invoke
+ ____ZN2CIL13convert_metalEPKNS_12MetalContextE13vImage_BufferP11__IOSurfacePKvNS_11ConvertTypeE_block_invoke.314
+ ____ZN2CIL13convert_metalEPKNS_12MetalContextE13vImage_BufferP11__IOSurfacePKvNS_11ConvertTypeE_block_invoke.317
+ ____ZN2CIL19AppendColorSpaceSrcEPNS_7ContextEPNS_4NodeENS_10ImageIndexEP12CGColorSpacebfbfb_block_invoke
+ ____ZN2CIL19print_program_graphEPKNS_7ContextEmmPKNS_17RenderDestinationEdPKNS_8TileTaskEPKcPNS_4NodeERK6CGRectNS_11PixelFormatE_block_invoke
+ ____ZN2CIL20AppendConverterArrayEPNS_7ContextEPNS_4NodeENS_10ImageIndexEPK9__CFArrayNS_18ConverterDirectionEbb_block_invoke.107
+ ____ZN2CIL20AppendConverterArrayEPNS_7ContextEPNS_4NodeENS_10ImageIndexEPK9__CFArrayNS_18ConverterDirectionEbb_block_invoke.114
+ ____ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ffbf_block_invoke
+ ____ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ffbf_block_invoke_2
+ ____ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ffbf_block_invoke_3
+ ____ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ffbf_block_invoke_4
+ ____ZN2CIL21print_graph_recursiveINS_4NodeENS_9NodeIndexENS1_9NodeStatsEEEvP7__sFILEPKT_iRKNSt3__113unordered_mapIT0_T1_NS9_4hashISB_EENS9_8equal_toISB_EENS9_9allocatorINS9_4pairIKSB_SC_EEEEEE_block_invoke.128
+ ____ZN2CIL21print_graph_recursiveINS_5ImageENS_10ImageIndexENS1_10ImageStatsEEEvP7__sFILEPKT_iRKNSt3__113unordered_mapIT0_T1_NS9_4hashISB_EENS9_8equal_toISB_EENS9_9allocatorINS9_4pairIKSB_SC_EEEEEE_block_invoke.1090
+ ____ZN2CIL21print_graph_recursiveINS_5ImageENS_10ImageIndexENS1_10ImageStatsEEEvP7__sFILEPKT_iRKNSt3__113unordered_mapIT0_T1_NS9_4hashISB_EENS9_8equal_toISB_EENS9_9allocatorINS9_4pairIKSB_SC_EEEEEE_block_invoke.1095
+ ____ZN2CIL23_traverse_program_graphENS_6roiKeyERNS_8liveROIsES2__block_invoke
+ ____ZNK2CI11ProgramNode18print_for_graphvizEP7__sFILERKNSt3__113unordered_mapIPKNS_11GraphObjectEjNS3_4hashIS7_EENS3_8equal_toIS7_EENS3_9allocatorINS3_4pairIKS7_jEEEEEENS_4Node9NodeStatsE_block_invoke.106
+ ____ZNK2CI11ProgramNode18print_for_graphvizEP7__sFILERKNSt3__113unordered_mapIPKNS_11GraphObjectEjNS3_4hashIS7_EENS3_8equal_toIS7_EENS3_9allocatorINS3_4pairIKS7_jEEEEEENS_4Node9NodeStatsE_block_invoke.110
+ ____ZNK2CI12ProviderNode11tileSurfaceEmmRy_block_invoke_3
+ ____ZNK2CI12ProviderNode13surfaceForROIEPKNS_7ContextERK6CGRectRNS_8Tileable5StatsE_block_invoke_7
+ ____ZNK2CI13ProviderImage17node_for_graphvizERKNSt3__113unordered_mapIPKNS_11GraphObjectEjNS1_4hashIS5_EENS1_8equal_toIS5_EENS1_9allocatorINS1_4pairIKS5_jEEEEEE_block_invoke_2
+ ____ZNK2CI13ProviderImage17render_graph_coreEPNS_7ContextERNS_14ImageToNodeMapERKNSt3__13mapINS_11ImageDigestE6CGRectNS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEEi_block_invoke
+ ____ZNK2CI16MetalMainProgram16getPipelineStateENS_9NodeIndexE_block_invoke_2
+ ____ZNK2CI24PrecompiledUberFunctions13getUberShaderEP7NSArrayIP8NSStringES3__block_invoke
+ ____ZNK2CI24PrecompiledUberFunctions16getFunctionArrayEP7NSArrayIP8NSStringE_block_invoke
+ ____ZNK2CI24PrecompiledUberFunctions28getFunctionArrayNoDuplicatesEP7NSArrayIP8NSStringE_block_invoke
+ ____ZNK2CI7Context19converter_for_inputENS_11PixelFormatERNS_11ConvertTypeE_block_invoke
+ ____ZNK2CI7Context19swizzler_for_outputENS_11PixelFormatE5IRectNS_15DestinationTypeE_block_invoke
+ ____ZNK2CI7Context20converter_for_outputENS_11PixelFormatERNS_11ConvertTypeE_block_invoke
+ ____ZNK2CI7Context30format_is_supported_for_outputENS_11PixelFormatENS_15DestinationTypeE5IRect_block_invoke
+ ____ZNK2CI8TileTask23graphviz_representationEPKNS_10RenderTaskE_block_invoke.49
+ ____ZNK2CI9GLContext11blitSurfaceEP11__IOSurface5IRectPNS_14intermediate_tES3_RKNS_17TextureDescriptorE_block_invoke.46
+ ____ZNK2CI9GLContext11blitSurfaceEP11__IOSurface5IRectPNS_14intermediate_tES3_RKNS_17TextureDescriptorE_block_invoke.46.cold.1
+ ____ZNK2CI9NoopImage17render_graph_coreEPNS_7ContextEPNS_4NodeERKNSt3__13mapINS_11ImageDigestE6CGRectNS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEEi_block_invoke
+ ____ZNK2CI9NoopImage17render_graph_coreEPNS_7ContextEPNS_4NodeERKNSt3__13mapINS_11ImageDigestE6CGRectNS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEEi_block_invoke_2
+ ___block_descriptor_100_e21_v48?0^v8Q16Q24Q32Q40l
+ ___block_descriptor_40_e8_32b_e109_{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}^{CGRect}}44?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12ls32l8
+ ___block_descriptor_40_e8_32b_e40_v56?0r^{__IOSurface=}8r^v16Q24Q32Q40Q48ls32l8
+ ___block_descriptor_48_e8_32o40o_e109_{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}^{CGRect}}44?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12ls32l8s40l8
+ ___block_descriptor_48_e8_32o40o_e21_v48?0^v8Q16Q24Q32Q40ls32l8s40l8
+ ___block_descriptor_49_e8_32o40b_e107_v128?0r^v8r^v16r^v24r^v32r^v40^{__IOSurface=}48^v56Q64{CGRect={CGPoint=dd}{CGSize=dd}}72B104i108^v112^v120ls32l8s40l8
+ ___block_descriptor_52_e21_v48?0^v8Q16Q24Q32Q40l
+ ___block_descriptor_61_e28_v16?0"<MTLCommandBuffer>"8l
+ ___block_descriptor_64_e8_32o40r48r_e5_v8?0lr40l8s32l8r48l8
+ ___block_descriptor_65_e8_32o40o_e57_v56?0"<MTLTexture>"8"<MTLCommandBuffer>"16Q24Q32Q40Q48ls32l8s40l8
+ ___block_descriptor_68_e21_v48?0^v8Q16Q24Q32Q40l
+ ___block_descriptor_72_e8_32o40o48o56r_e5_v8?0lr56l8s32l8s40l8s48l8
+ ___block_descriptor_74_e8_32o40o48o56b_e107_v128?0r^v8r^v16r^v24r^v32r^v40^{__IOSurface=}48^v56Q64{CGRect={CGPoint=dd}{CGSize=dd}}72B104i108^v112^v120ls56l8s32l8s40l8s48l8
+ ___block_descriptor_74_e8_32o40o48o56b_e113_v112?0r^v8r^v16r^v24r^v32r^v40i48^^{__IOSurface}52r^^v60Q68r^{CGRect={CGPoint=dd}{CGSize=dd}}76r^B84i92^v96^v104ls56l8s32l8s40l8s48l8
+ ___block_descriptor_77_e8_32o40o_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8
+ ___block_descriptor_89_e8_32o40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_92_e22_v48?0r^v8Q16Q24Q32Q40l
+ ___block_descriptor_tmp.109
+ ___block_descriptor_tmp.111
+ ___block_descriptor_tmp.114
+ ___block_descriptor_tmp.117
+ ___block_descriptor_tmp.122
+ ___block_descriptor_tmp.125
+ ___block_descriptor_tmp.127
+ ___block_descriptor_tmp.135
+ ___block_descriptor_tmp.137
+ ___block_descriptor_tmp.138
+ ___block_descriptor_tmp.139
+ ___block_descriptor_tmp.141
+ ___block_descriptor_tmp.143
+ ___block_descriptor_tmp.147
+ ___block_descriptor_tmp.165
+ ___block_descriptor_tmp.168
+ ___block_descriptor_tmp.172
+ ___block_descriptor_tmp.174
+ ___block_descriptor_tmp.197
+ ___block_descriptor_tmp.201
+ ___block_descriptor_tmp.202
+ ___block_descriptor_tmp.210
+ ___block_descriptor_tmp.221
+ ___block_descriptor_tmp.222
+ ___block_descriptor_tmp.224
+ ___block_descriptor_tmp.229
+ ___block_descriptor_tmp.231
+ ___block_descriptor_tmp.233
+ ___block_descriptor_tmp.237
+ ___block_descriptor_tmp.246
+ ___block_descriptor_tmp.249
+ ___block_descriptor_tmp.259
+ ___block_descriptor_tmp.268
+ ___block_descriptor_tmp.271
+ ___block_descriptor_tmp.275
+ ___block_descriptor_tmp.279
+ ___block_descriptor_tmp.47
+ ___block_descriptor_tmp.49
+ ___block_descriptor_tmp.63
+ ___block_descriptor_tmp.65
+ ___block_descriptor_tmp.66
+ ___block_descriptor_tmp.67
+ ___block_descriptor_tmp.70
+ ___block_descriptor_tmp.74
+ ___block_descriptor_tmp.84
+ ___block_descriptor_tmp.85
+ ___block_descriptor_tmp.87
+ ___block_descriptor_tmp.96
+ ___block_descriptor_tmp.99
+ ___block_literal_global.100
+ ___block_literal_global.101
+ ___block_literal_global.1067
+ ___block_literal_global.1077
+ ___block_literal_global.1084
+ ___block_literal_global.1088
+ ___block_literal_global.1120
+ ___block_literal_global.1148
+ ___block_literal_global.1153
+ ___block_literal_global.118
+ ___block_literal_global.119
+ ___block_literal_global.122
+ ___block_literal_global.1243
+ ___block_literal_global.128
+ ___block_literal_global.132
+ ___block_literal_global.143
+ ___block_literal_global.159
+ ___block_literal_global.16
+ ___block_literal_global.161
+ ___block_literal_global.165
+ ___block_literal_global.176
+ ___block_literal_global.180
+ ___block_literal_global.197
+ ___block_literal_global.200
+ ___block_literal_global.201
+ ___block_literal_global.206
+ ___block_literal_global.224
+ ___block_literal_global.228
+ ___block_literal_global.235
+ ___block_literal_global.239
+ ___block_literal_global.240
+ ___block_literal_global.272
+ ___block_literal_global.289
+ ___block_literal_global.319
+ ___block_literal_global.322
+ ___block_literal_global.35
+ ___block_literal_global.383
+ ___block_literal_global.386
+ ___block_literal_global.39
+ ___block_literal_global.399
+ ___block_literal_global.404
+ ___block_literal_global.409
+ ___block_literal_global.42
+ ___block_literal_global.458
+ ___block_literal_global.50
+ ___block_literal_global.505
+ ___block_literal_global.531
+ ___block_literal_global.552
+ ___block_literal_global.57
+ ___block_literal_global.59
+ ___block_literal_global.609
+ ___block_literal_global.62
+ ___block_literal_global.65
+ ___block_literal_global.68
+ ___block_literal_global.74
+ ___block_literal_global.809
+ ___block_literal_global.815
+ ___block_literal_global.89
+ ___block_literal_global.98
+ ___block_literal_global.99
+ ___copy_helper_block_8_64c25_ZTSKN2CI4Node9NodeStatsE
+ ___destroy_helper_block_8_64c25_ZTSKN2CI4Node9NodeStatsE
+ ___getBytesAtPositionCallback_1C08_block_invoke
+ ___getBytesAtPositionCallback_1C08_lut_block_invoke
+ ___getBytesAtPositionCallback_1C0f_block_invoke
+ ___getBytesAtPositionCallback_1C0h_block_invoke
+ ___getBytesAtPositionCallback_1C0h_lut_block_invoke
+ ___getBytesAtPositionCallback_1C0h_lut_block_invoke_2
+ ___getBytesAtPositionCallback_1C16_block_invoke
+ ___getBytesAtPositionCallback_2C08_block_invoke
+ ___getBytesAtPositionCallback_2C0f_block_invoke
+ ___getBytesAtPositionCallback_2C0h_block_invoke
+ ___getBytesAtPositionCallback_2C16_block_invoke
+ ___getBytesAtPositionCallback_A008_block_invoke
+ ___getBytesAtPositionCallback_AYCbCr8_block_invoke
+ ___getBytesAtPositionCallback_CbYCrY16_block_invoke
+ ___getBytesAtPositionCallback_CbYCrYFull_block_invoke
+ ___getBytesAtPositionCallback_CbYCrY_block_invoke
+ ___getBytesAtPositionCallback_YCbYCrFull_block_invoke
+ ___getBytesAtPositionCallback_YCbYCr_block_invoke
+ ___getBytesAtPositionCallback_l10r_block_invoke
+ ___getBytesAtPositionCallback_other__block_invoke
+ ___getBytesAtPositionCallback_w30r_block_invoke
+ ___getBytesAtPositionCallback_w40a_block_invoke
+ ___getFKTextDetectorClass_block_invoke
+ ___getFKTextDetectorClass_block_invoke.cold.1
+ ___getFKTextDetectorClass_block_invoke.cold.2
+ ___timeElapsedSinceInit_block_invoke
+ __block_invoke
+ _add_triplanar_props
+ _areaAverageMaximumRedFilter.onceToken
+ _audit_stringAVFCapture
+ _audit_stringFuthark
+ _blurredRoundedRectangleGeneratorFilter.onceToken
+ _dispatch_block_create
+ _dispatch_block_wait
+ _distanceGradientFromRedMaskFilter.onceToken
+ _element_width
+ _fmemopen
+ _getBytesAtPositionCallback_1C08
+ _getBytesAtPositionCallback_1C08.cold.1
+ _getBytesAtPositionCallback_1C08.cold.2
+ _getBytesAtPositionCallback_1C08_lut
+ _getBytesAtPositionCallback_1C08_lut.cold.1
+ _getBytesAtPositionCallback_1C08_lut.cold.2
+ _getBytesAtPositionCallback_1C0f
+ _getBytesAtPositionCallback_1C0f.cold.1
+ _getBytesAtPositionCallback_1C0f.cold.2
+ _getBytesAtPositionCallback_1C0h
+ _getBytesAtPositionCallback_1C0h.cold.1
+ _getBytesAtPositionCallback_1C0h.cold.2
+ _getBytesAtPositionCallback_1C0h_lut
+ _getBytesAtPositionCallback_1C0h_lut.cold.1
+ _getBytesAtPositionCallback_1C0h_lut.cold.2
+ _getBytesAtPositionCallback_1C16
+ _getBytesAtPositionCallback_1C16.cold.1
+ _getBytesAtPositionCallback_1C16.cold.2
+ _getBytesAtPositionCallback_2C08
+ _getBytesAtPositionCallback_2C08.cold.1
+ _getBytesAtPositionCallback_2C08.cold.2
+ _getBytesAtPositionCallback_2C0f
+ _getBytesAtPositionCallback_2C0f.cold.1
+ _getBytesAtPositionCallback_2C0f.cold.2
+ _getBytesAtPositionCallback_2C0h
+ _getBytesAtPositionCallback_2C0h.cold.1
+ _getBytesAtPositionCallback_2C0h.cold.2
+ _getBytesAtPositionCallback_2C16
+ _getBytesAtPositionCallback_2C16.cold.1
+ _getBytesAtPositionCallback_2C16.cold.2
+ _getBytesAtPositionCallback_A008
+ _getBytesAtPositionCallback_A008.cold.1
+ _getBytesAtPositionCallback_A008.cold.2
+ _getBytesAtPositionCallback_AYCbCr8
+ _getBytesAtPositionCallback_AYCbCr8.cold.1
+ _getBytesAtPositionCallback_AYCbCr8.cold.2
+ _getBytesAtPositionCallback_CbYCrY
+ _getBytesAtPositionCallback_CbYCrY.cold.1
+ _getBytesAtPositionCallback_CbYCrY.cold.2
+ _getBytesAtPositionCallback_CbYCrY16
+ _getBytesAtPositionCallback_CbYCrY16.cold.1
+ _getBytesAtPositionCallback_CbYCrY16.cold.2
+ _getBytesAtPositionCallback_CbYCrYFull
+ _getBytesAtPositionCallback_CbYCrYFull.cold.1
+ _getBytesAtPositionCallback_CbYCrYFull.cold.2
+ _getBytesAtPositionCallback_YCbYCr
+ _getBytesAtPositionCallback_YCbYCr.cold.1
+ _getBytesAtPositionCallback_YCbYCr.cold.2
+ _getBytesAtPositionCallback_YCbYCrFull
+ _getBytesAtPositionCallback_YCbYCrFull.cold.1
+ _getBytesAtPositionCallback_YCbYCrFull.cold.2
+ _getBytesAtPositionCallback_l10r
+ _getBytesAtPositionCallback_l10r.cold.1
+ _getBytesAtPositionCallback_l10r.cold.2
+ _getBytesAtPositionCallback_other_
+ _getBytesAtPositionCallback_w30r
+ _getBytesAtPositionCallback_w30r.cold.1
+ _getBytesAtPositionCallback_w30r.cold.2
+ _getBytesAtPositionCallback_w40a
+ _getBytesAtPositionCallback_w40a.cold.1
+ _getBytesAtPositionCallback_w40a.cold.2
+ _getFKTextDetectorClass.softClass
+ _gethorizonDetectionFFTAnglesSymbolLoc
+ _gethorizonDetectionFFTSymbolLoc
+ _isHarvestingForThisProcess
+ _isKind_AVCameraCalibrationDataClass
+ _isKind_AVDepthDataClass
+ _isKind_AVPortraitEffectsMatteClass
+ _isKind_AVSemanticSegmentationMatteClass
+ _kCGConstrainedDynamicRange
+ _kCGContentAverageLightLevel
+ _kCGContentEDRStrength
+ _kCIContextIntermediateAllocator
+ _kCIContextPriorityRequestMedia
+ _kCIDynamicRangeConstrainedHigh
+ _kCIDynamicRangeHigh
+ _kCIDynamicRangeStandard
+ _kCIFormatXRGB16
+ _kCIFormatXRGBf
+ _kCIImageApplyCleanAperture
+ _kCIImageContentAverageLightLevel
+ _kCIImageProcessorOnlyUsesMetal
+ _kCIImageRepresentationISOGainMapGamma
+ _kCIImageRepresentationSemanticSegmentationSkyMatteImage_block_invoke
+ _kCIInputBacksideImageKey
+ _kCIInputBiasVectorKey
+ _kCIInputColor0Key
+ _kCIInputColor1Key
+ _kCIInputColorSpaceKey
+ _kCIInputCountKey
+ _kCIInputExtrapolateKey
+ _kCIInputPaletteImageKey
+ _kCIInputPerceptualKey
+ _kCIInputPoint0Key
+ _kCIInputPoint1Key
+ _kCIInputRadius0Key
+ _kCIInputRadius1Key
+ _kCIInputThresholdKey
+ _kCVImageBufferAlphaChannelMode_PremultipliedAlpha
+ _kCVImageBufferCleanApertureHeightKey
+ _kCVImageBufferCleanApertureHorizontalOffsetKey
+ _kCVImageBufferCleanApertureKey
+ _kCVImageBufferCleanApertureVerticalOffsetKey
+ _kCVImageBufferCleanApertureWidthKey
+ _kCVImageBufferPreferredCleanApertureKey
+ _kSurfaceCacheDefaultAlignment
+ _nearMatrix_DCIP3
+ _nearMatrix_Rec2100
+ _objc_msgSend$_CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:
+ _objc_msgSend$_addDepthMap:session:imageHandle:options:
+ _objc_msgSend$_addGainMap:session:imageHandle:containerFormat:options:orientation:
+ _objc_msgSend$_addPortraitMatte:session:imageHandle:options:
+ _objc_msgSend$_addSemanticImages:session:imageHandle:options:
+ _objc_msgSend$_call_formatForInputAtIndex:arguments:
+ _objc_msgSend$_call_outputFormatWithArguments:
+ _objc_msgSend$_imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:constrainedHigh:
+ _objc_msgSend$_initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:
+ _objc_msgSend$_internalFallbackCL
+ _objc_msgSend$_originalIOSurface
+ _objc_msgSend$_remappingKernel
+ _objc_msgSend$_setOriginalSurface:options:
+ _objc_msgSend$archiveTypeAtURL:device:error:
+ _objc_msgSend$buffer
+ _objc_msgSend$bufferForContextIntermediateCommitted:
+ _objc_msgSend$bufferForContextIntermediateCompleted:
+ _objc_msgSend$calculateHDRStatsForCGImage:
+ _objc_msgSend$calculateHDRStatsForImage:
+ _objc_msgSend$captureTraceURL
+ _objc_msgSend$contentAverageLightLevel
+ _objc_msgSend$functionHandleWithFunction:
+ _objc_msgSend$gainMapImageForSDR:HDR:colorSpace:rgbGainmap:
+ _objc_msgSend$imageBySettingContentAverageLightLevel:
+ _objc_msgSend$imageBySettingContentHeadroom:
+ _objc_msgSend$initWithCameraCalibrationDataDictionary:error:
+ _objc_msgSend$initWithName:arguments:controlDependencies:isEarlyReturn:
+ _objc_msgSend$initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:
+ _objc_msgSend$initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:tileTask:
+ _objc_msgSend$initWithSurface:texture:digest:allowSRGB:bounds:roiTileIndex:roiTileCount:onlyMetal:context:
+ _objc_msgSend$inputAngleSinCos
+ _objc_msgSend$inputBiasAmount
+ _objc_msgSend$inputColor
+ _objc_msgSend$inputCurvature
+ _objc_msgSend$inputHeight
+ _objc_msgSend$inputInset
+ _objc_msgSend$inputSDFScaleFactor
+ _objc_msgSend$inputSDFZeroValue
+ _objc_msgSend$inputSpread
+ _objc_msgSend$internalBinaryArchiveWithName:device:
+ _objc_msgSend$isMetalAvailable
+ _objc_msgSend$isOpenCLAvailable
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$maxAvailableAllocationSize
+ _objc_msgSend$messageStringFromDescriptor:
+ _objc_msgSend$newBufferForContextIntermediate:usingHint:identifier:
+ _objc_msgSend$newVisibleFunctionTableWithDescriptor:
+ _objc_msgSend$onlyUsesMetal
+ _objc_msgSend$outputFormatAtIndex:arguments:
+ _objc_msgSend$outputURL
+ _objc_msgSend$outputValue:
+ _objc_msgSend$preservesOpacity
+ _objc_msgSend$processWithInputs:arguments:outputs:error:
+ _objc_msgSend$provideImageToMTLTexture:commandBuffer:originx:originy:width:height:userInfo:
+ _objc_msgSend$refelectionWithFunctionName:
+ _objc_msgSend$removeItemAtPath:error:
+ _objc_msgSend$setBinaryFunctions:
+ _objc_msgSend$setCaptureObject:
+ _objc_msgSend$setFunction:atIndex:
+ _objc_msgSend$setFunctionCount:
+ _objc_msgSend$setInputPreferredDynamicRange:
+ _objc_msgSend$setInputSourceHeadroom:
+ _objc_msgSend$setInputTargetHeadroom:
+ _objc_msgSend$setLinkedFunctions:
+ _objc_msgSend$setOutputURL:
+ _objc_msgSend$setSupportAddingBinaryFunctions:
+ _objc_msgSend$setVisibleFunctionTable:atBufferIndex:
+ _objc_msgSend$startCaptureWithDescriptor:error:
+ _objc_msgSend$stopCapture
+ _objc_msgSend$storageMode
+ _objc_msgSend$stringContents
+ _objc_msgSend$supportsFunctionPointers
+ _objc_msgSend$totalSize
+ _roundedQRCodeGeneratorFilter.onceToken
+ _setLongValue
+ _signedDistanceGradientFromRedMaskFilter.onceToken
+ _systemToneMapFilter.onceToken
+ _timeElapsedSinceInit.cold.1
+ _timeElapsedSinceInit.initTime
+ _timeElapsedSinceInit.onceToken
+ _timeElapsedSinceInit.timebase
+ _vImageConvert_ARGB2101010ToARGB16F
+ _vImagePermuteChannels_ARGB16F
- +[CIBurstImageSetInternal defaultVersionString]
- +[CIContext loadArchive:].cold.1
- +[CIContext loadArchive:].cold.2
- +[CIContext loadArchive:].cold.3
- +[CIContext loadArchiveWithName:fromURL:].cold.1
- +[CIContext loadArchiveWithName:fromURL:].cold.2
- +[CIContext loadArchiveWithName:fromURL:].cold.3
- +[CIPersonSegmentation customAttributes]
- +[CIPersonSegmentationKernel allowPartialOutputRegion]
- +[CIPersonSegmentationKernel formatForInputAtIndex:]
- +[CIPersonSegmentationKernel outputFormat]
- +[CIPersonSegmentationKernel processWithInputs:arguments:output:error:]
- +[CIPersonSegmentationKernel roiForInput:arguments:outputRect:]
- +[CISaliencyMapFilter customAttributes]
- +[CISaliencyMapKernel allowPartialOutputRegion]
- +[CISaliencyMapKernel formatForInputAtIndex:]
- +[CISaliencyMapKernel outputFormat]
- +[CISaliencyMapKernel processWithInputs:arguments:output:error:]
- +[CISaliencyMapKernel roiForInput:arguments:outputRect:]
- -[CIBlendKernel setBlendBehaviorBit:value:]
- -[CIBurstActionClassifier computeKernelValueWithSupportVector:]
- -[CIBurstActionClassifier initWithVersion:]
- -[CIBurstActionClassifier init]
- -[CIBurstActionClassifier isBurstAction]
- -[CIBurstActionClassifier predictResult]
- -[CIBurstActionClassifier scaleVector]
- -[CIBurstActionClassifier setSvmParameters:]
- -[CIBurstActionClassifier setTestAverageCameraTravelDistance:]
- -[CIBurstActionClassifier setTestAverageRegistrationErrorSkewness:]
- -[CIBurstActionClassifier setTestBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix:]
- -[CIBurstActionClassifier setTestInOutRatio:]
- -[CIBurstActionClassifier setTestMaxInnerDistance:]
- -[CIBurstActionClassifier setTestMaxPeakRegistrationError:]
- -[CIBurstActionClassifier setTestMaxRegistrationErrorIntegral:]
- -[CIBurstActionClassifier setTestMaxRegistrationErrorSkewness:]
- -[CIBurstActionClassifier setTestMeanPeakRegistrationError:]
- -[CIBurstActionClassifier setTestMinRegionOfInterestSize:]
- -[CIBurstActionClassifier svmParameters]
- -[CIBurstActionClassifier testAverageCameraTravelDistance]
- -[CIBurstActionClassifier testAverageRegistrationErrorSkewness]
- -[CIBurstActionClassifier testBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix]
- -[CIBurstActionClassifier testInOutRatio]
- -[CIBurstActionClassifier testMaxInnerDistance]
- -[CIBurstActionClassifier testMaxPeakRegistrationError]
- -[CIBurstActionClassifier testMaxRegistrationErrorIntegral]
- -[CIBurstActionClassifier testMaxRegistrationErrorSkewness]
- -[CIBurstActionClassifier testMeanPeakRegistrationError]
- -[CIBurstActionClassifier testMinRegionOfInterestSize]
- -[CIBurstClusterDivider actionAmount]
- -[CIBurstClusterDivider compareActionAmounts:]
- -[CIBurstClusterDivider compareDividers:]
- -[CIBurstClusterDivider compareIndices:]
- -[CIBurstClusterDivider dividerScore]
- -[CIBurstClusterDivider highNoiseThreshold]
- -[CIBurstClusterDivider leftImage]
- -[CIBurstClusterDivider noiseThreshold]
- -[CIBurstClusterDivider setActionAmount:]
- -[CIBurstClusterDivider setDividerScore:]
- -[CIBurstClusterDivider setHighNoiseThreshold:]
- -[CIBurstClusterDivider setLeftImage:]
- -[CIBurstClusterDivider setNoiseThreshold:]
- -[CIBurstClusterDivider setTrueLocalMaximum:]
- -[CIBurstClusterDivider trueLocalMaximum]
- -[CIBurstFaceConfigEntry faceId]
- -[CIBurstFaceConfigEntry faceRect]
- -[CIBurstFaceConfigEntry framesSinceLast]
- -[CIBurstFaceConfigEntry initWithRect:withFaceId:]
- -[CIBurstFaceConfigEntry setFaceId:]
- -[CIBurstFaceConfigEntry setFaceRect:]
- -[CIBurstFaceConfigEntry setFramesSinceLast:]
- -[CIBurstFaceInfo hwCenter]
- -[CIBurstFaceInfo hwFaceId]
- -[CIBurstFaceInfo hwFaceRect]
- -[CIBurstFaceInfo hwLastFrameSeen]
- -[CIBurstFaceInfo hwSize]
- -[CIBurstFaceInfo init]
- -[CIBurstFaceInfo overlapWithHwRect:]
- -[CIBurstFaceInfo overlapWithSwRect:]
- -[CIBurstFaceInfo setHwCenter:]
- -[CIBurstFaceInfo setHwFaceId:]
- -[CIBurstFaceInfo setHwLastFrameSeen:]
- -[CIBurstFaceInfo setHwSize:]
- -[CIBurstFaceInfo setSwCenter:]
- -[CIBurstFaceInfo setSwFaceId:]
- -[CIBurstFaceInfo setSwLastFrameSeen:]
- -[CIBurstFaceInfo setSwSize:]
- -[CIBurstFaceInfo swCenter]
- -[CIBurstFaceInfo swFaceId]
- -[CIBurstFaceInfo swFaceRect]
- -[CIBurstFaceInfo swLastFrameSeen]
- -[CIBurstFaceInfo swSize]
- -[CIBurstFaceScoreEntry addScore:]
- -[CIBurstFaceScoreEntry computeAverage]
- -[CIBurstFaceScoreEntry computeStandardDeviation]
- -[CIBurstFaceScoreEntry initWithScore:]
- -[CIBurstFaceScoreEntry maxScore]
- -[CIBurstFaceScoreEntry minScore]
- -[CIBurstFaceScoreEntry numScores]
- -[CIBurstFaceScoreEntry setMaxScore:]
- -[CIBurstFaceScoreEntry setMinScore:]
- -[CIBurstFaceScoreEntry setNumScores:]
- -[CIBurstFaceStat FCRBlinkFeaturesSize]
- -[CIBurstFaceStat FCRLeftEyeFeaturesOffset]
- -[CIBurstFaceStat FCRRightEyeFeaturesOffset]
- -[CIBurstFaceStat FCRSmileAndBlinkFeatures]
- -[CIBurstFaceStat FCRSmileFeaturesOffset]
- -[CIBurstFaceStat FCRSmileFeaturesSize]
- -[CIBurstFaceStat copyWithZone:]
- -[CIBurstFaceStat faceId]
- -[CIBurstFaceStat faceRect]
- -[CIBurstFaceStat faceScore]
- -[CIBurstFaceStat focusScore]
- -[CIBurstFaceStat foundByFaceCore]
- -[CIBurstFaceStat framesSinceLast]
- -[CIBurstFaceStat hasLeftEye]
- -[CIBurstFaceStat hasRightEye]
- -[CIBurstFaceStat hasRollAngle]
- -[CIBurstFaceStat hasYawAngle]
- -[CIBurstFaceStat hwFaceId]
- -[CIBurstFaceStat hwFaceRect]
- -[CIBurstFaceStat initWithFaceStat:]
- -[CIBurstFaceStat isSyncedWithImage]
- -[CIBurstFaceStat leftEyeBlinkScore]
- -[CIBurstFaceStat leftEyeOpen]
- -[CIBurstFaceStat leftEyeRect]
- -[CIBurstFaceStat normalizedFaceRect]
- -[CIBurstFaceStat normalizedFocusScore]
- -[CIBurstFaceStat normalizedSigma]
- -[CIBurstFaceStat rightEyeBlinkScore]
- -[CIBurstFaceStat rightEyeOpen]
- -[CIBurstFaceStat rightEyeRect]
- -[CIBurstFaceStat rollAngle]
- -[CIBurstFaceStat setFCRBlinkFeaturesSize:]
- -[CIBurstFaceStat setFCRLeftEyeFeaturesOffset:]
- -[CIBurstFaceStat setFCRRightEyeFeaturesOffset:]
- -[CIBurstFaceStat setFCRSmileAndBlinkFeatures:]
- -[CIBurstFaceStat setFCRSmileFeaturesOffset:]
- -[CIBurstFaceStat setFCRSmileFeaturesSize:]
- -[CIBurstFaceStat setFaceId:]
- -[CIBurstFaceStat setFaceRect:]
- -[CIBurstFaceStat setFaceScore:]
- -[CIBurstFaceStat setFocusScore:]
- -[CIBurstFaceStat setFoundByFaceCore:]
- -[CIBurstFaceStat setFramesSinceLast:]
- -[CIBurstFaceStat setHasLeftEye:]
- -[CIBurstFaceStat setHasRightEye:]
- -[CIBurstFaceStat setHasRollAngle:]
- -[CIBurstFaceStat setHasYawAngle:]
- -[CIBurstFaceStat setHwFaceId:]
- -[CIBurstFaceStat setHwFaceRect:]
- -[CIBurstFaceStat setIsSyncedWithImage:]
- -[CIBurstFaceStat setLeftEyeBlinkScore:]
- -[CIBurstFaceStat setLeftEyeOpen:]
- -[CIBurstFaceStat setLeftEyeRect:]
- -[CIBurstFaceStat setNormalizedFaceRect:]
- -[CIBurstFaceStat setNormalizedFocusScore:]
- -[CIBurstFaceStat setNormalizedSigma:]
- -[CIBurstFaceStat setRightEyeBlinkScore:]
- -[CIBurstFaceStat setRightEyeOpen:]
- -[CIBurstFaceStat setRightEyeRect:]
- -[CIBurstFaceStat setRollAngle:]
- -[CIBurstFaceStat setSmallFace:]
- -[CIBurstFaceStat setSmileScore:]
- -[CIBurstFaceStat setSmiling:]
- -[CIBurstFaceStat setTimestamp:]
- -[CIBurstFaceStat setYawAngle:]
- -[CIBurstFaceStat smallFace]
- -[CIBurstFaceStat smileScore]
- -[CIBurstFaceStat smiling]
- -[CIBurstFaceStat timestamp]
- -[CIBurstFaceStat yawAngle]
- -[CIBurstImageFaceAnalysisContext addFaceToArray:]
- -[CIBurstImageFaceAnalysisContext addFacesToImageStat:imageSize:]
- -[CIBurstImageFaceAnalysisContext adjustFaceIdsForImageStat:]
- -[CIBurstImageFaceAnalysisContext calcFaceScores:]
- -[CIBurstImageFaceAnalysisContext calculateFaceCoreROI:imageStat:needFaceCore:]
- -[CIBurstImageFaceAnalysisContext calculateFaceFocusInImage:imageStat:]
- -[CIBurstImageFaceAnalysisContext dealloc]
- -[CIBurstImageFaceAnalysisContext dumpFaceInfoArray]
- -[CIBurstImageFaceAnalysisContext extractFacesFromMetadata:]
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:]
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.1
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.10
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.11
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.2
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.3
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.4
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.5
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.6
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.7
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.8
- -[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:].cold.9
- -[CIBurstImageFaceAnalysisContext findOverlappingFaceStat:imageStat:]
- -[CIBurstImageFaceAnalysisContext forceFaceDetectionEnable]
- -[CIBurstImageFaceAnalysisContext initWithVersion:]
- -[CIBurstImageFaceAnalysisContext latestFaceTimestamp]
- -[CIBurstImageFaceAnalysisContext padRoiRect:paddingX:paddingY:]
- -[CIBurstImageFaceAnalysisContext setForceFaceDetectionEnable:]
- -[CIBurstImageFaceAnalysisContext setLatestFaceTimestamp:]
- -[CIBurstImageFaceAnalysisContext setTimeBlinkDetectionDone:]
- -[CIBurstImageFaceAnalysisContext setTimeFaceDetectionDone:]
- -[CIBurstImageFaceAnalysisContext setVersion:]
- -[CIBurstImageFaceAnalysisContext setupFaceDetector]
- -[CIBurstImageFaceAnalysisContext setupFaceDetector].cold.1
- -[CIBurstImageFaceAnalysisContext setupFaceDetector].cold.2
- -[CIBurstImageFaceAnalysisContext timeBlinkDetectionDone]
- -[CIBurstImageFaceAnalysisContext timeFaceDetectionDone]
- -[CIBurstImageFaceAnalysisContext version]
- -[CIBurstImageSetInternal actionClassifier]
- -[CIBurstImageSetInternal addImageFromIOSurface:properties:identifier:completionBlock:]
- -[CIBurstImageSetInternal addYUVImage:properties:identifier:imageProps:completionBlock:]
- -[CIBurstImageSetInternal allImageIdentifiers]
- -[CIBurstImageSetInternal bestImageIdentifiersArray]
- -[CIBurstImageSetInternal bestImageIdentifiers]
- -[CIBurstImageSetInternal burstCoverSelection]
- -[CIBurstImageSetInternal burstDocumentDirectory]
- -[CIBurstImageSetInternal burstId]
- -[CIBurstImageSetInternal burstLogFileName]
- -[CIBurstImageSetInternal clusterArray]
- -[CIBurstImageSetInternal clusterByImageIdentifier]
- -[CIBurstImageSetInternal computeActionSelectionThreshold]
- -[CIBurstImageSetInternal computeAllImageScores]
- -[CIBurstImageSetInternal computeBeginningVsEndAEMatrixDiffVsAverageAdjacent]
- -[CIBurstImageSetInternal computeCameraTravelDistance]
- -[CIBurstImageSetInternal computeEmotion:]
- -[CIBurstImageSetInternal dealloc]
- -[CIBurstImageSetInternal dummyAnalysisCount]
- -[CIBurstImageSetInternal enableAnalysis]
- -[CIBurstImageSetInternal enableDumpYUV]
- -[CIBurstImageSetInternal enableFaceCore]
- -[CIBurstImageSetInternal faceIDCounts]
- -[CIBurstImageSetInternal findBestImage:useActionScores:]
- -[CIBurstImageSetInternal imageClusterForIdentifier:]
- -[CIBurstImageSetInternal initWithOptions:]
- -[CIBurstImageSetInternal isAction]
- -[CIBurstImageSetInternal isFaceDetectionForced]
- -[CIBurstImageSetInternal isPortrait]
- -[CIBurstImageSetInternal maxNumPendingFrames]
- -[CIBurstImageSetInternal performEmotionalRejectionOnCluster:]
- -[CIBurstImageSetInternal processClusters:]
- -[CIBurstImageSetInternal selectCoverPhotoFromMultiple:burstSize:]
- -[CIBurstImageSetInternal setActionClassifier:]
- -[CIBurstImageSetInternal setAllImageIdentifiers:]
- -[CIBurstImageSetInternal setBestImageIdentifiersArray:]
- -[CIBurstImageSetInternal setBurstCoverSelection:]
- -[CIBurstImageSetInternal setBurstId:]
- -[CIBurstImageSetInternal setBurstLogFileName:]
- -[CIBurstImageSetInternal setClusterArray:]
- -[CIBurstImageSetInternal setClusterByImageIdentifier:]
- -[CIBurstImageSetInternal setDummyAnalysisCount:]
- -[CIBurstImageSetInternal setEnableAnalysis:]
- -[CIBurstImageSetInternal setEnableDumpYUV:]
- -[CIBurstImageSetInternal setEnableFaceCore:]
- -[CIBurstImageSetInternal setFaceIDCounts:]
- -[CIBurstImageSetInternal setMaxNumPendingFrames:]
- -[CIBurstImageSetInternal setStatsByImageIdentifier:]
- -[CIBurstImageSetInternal setTemporalOrder:]
- -[CIBurstImageSetInternal setVersion:]
- -[CIBurstImageSetInternal setVersionString:]
- -[CIBurstImageSetInternal statsByImageIdentifier]
- -[CIBurstImageSetInternal temporalOrder]
- -[CIBurstImageSetInternal versionString]
- -[CIBurstImageSetInternal version]
- -[CIBurstImageStat AEAverage]
- -[CIBurstImageStat AEDelta]
- -[CIBurstImageStat AEStable]
- -[CIBurstImageStat AETarget]
- -[CIBurstImageStat AFStable]
- -[CIBurstImageStat actionClusteringScore]
- -[CIBurstImageStat actionScore]
- -[CIBurstImageStat aeMatrix]
- -[CIBurstImageStat allocateMeanStdPingPongBuffers::::]
- -[CIBurstImageStat assignMeanStdBuffers:]
- -[CIBurstImageStat avgHorzDiffY]
- -[CIBurstImageStat blurExtent]
- -[CIBurstImageStat canRegister]
- -[CIBurstImageStat collapseSharpnessGrid]
- -[CIBurstImageStat colorHistogram]
- -[CIBurstImageStat compareImageOrder:]
- -[CIBurstImageStat compareImageStats:]
- -[CIBurstImageStat computeAEMatrix:]
- -[CIBurstImageStat computeAEMatrixDifference:]
- -[CIBurstImageStat computeBlurStatsOnGrid:]
- -[CIBurstImageStat computeFacialFocusScoreSum]
- -[CIBurstImageStat computeImageColorHistogram:]
- -[CIBurstImageStat computeImageData:faceIDCounts:]
- -[CIBurstImageStat computeImageDistance:]
- -[CIBurstImageStat computeImageProjections:]
- -[CIBurstImageStat computeImageSharpnessOnGrid:]
- -[CIBurstImageStat computeRuleOfThreeDistance]
- -[CIBurstImageStat computeScore:]
- -[CIBurstImageStat computeSmilePercentage]
- -[CIBurstImageStat computeSmoothedGridROI:nextStat:]
- -[CIBurstImageStat dealloc]
- -[CIBurstImageStat doLimitedSharpnessAndBlur]
- -[CIBurstImageStat emotionallyRejected]
- -[CIBurstImageStat exclude]
- -[CIBurstImageStat faceStatArray]
- -[CIBurstImageStat facesRoiRect]
- -[CIBurstImageStat flagAsGarbage]
- -[CIBurstImageStat fullsizeJpegData]
- -[CIBurstImageStat fullsizeJpegSize]
- -[CIBurstImageStat getSharpnessAndBlurLimits]
- -[CIBurstImageStat hasRegistrationData]
- -[CIBurstImageStat imageId]
- -[CIBurstImageStat imageScore]
- -[CIBurstImageStat initWithIdentifier:]
- -[CIBurstImageStat isGarbage]
- -[CIBurstImageStat maxSkewness]
- -[CIBurstImageStat numHWFaces]
- -[CIBurstImageStat orientation]
- -[CIBurstImageStat performRegistration:deltaCol:deltaRow:]
- -[CIBurstImageStat registrationErrorIntegral]
- -[CIBurstImageStat registrationErrorX]
- -[CIBurstImageStat registrationErrorY]
- -[CIBurstImageStat roiSize]
- -[CIBurstImageStat setAEAverage:]
- -[CIBurstImageStat setAEDelta:]
- -[CIBurstImageStat setAEMatrix:]
- -[CIBurstImageStat setAEStable:]
- -[CIBurstImageStat setAETarget:]
- -[CIBurstImageStat setAFStable:]
- -[CIBurstImageStat setActionClusteringScore:]
- -[CIBurstImageStat setActionScore:]
- -[CIBurstImageStat setAvgHorzDiffY:]
- -[CIBurstImageStat setBlurExtent:]
- -[CIBurstImageStat setDoLimitedSharpnessAndBlur:]
- -[CIBurstImageStat setEmotionallyRejected:]
- -[CIBurstImageStat setExclude:]
- -[CIBurstImageStat setFaceStatArray:]
- -[CIBurstImageStat setFacesRoiRect:]
- -[CIBurstImageStat setFullsizeJpegData:]
- -[CIBurstImageStat setFullsizeJpegSize:]
- -[CIBurstImageStat setHasRegistrationData:]
- -[CIBurstImageStat setImageId:]
- -[CIBurstImageStat setImageScore:]
- -[CIBurstImageStat setIsGarbage:]
- -[CIBurstImageStat setMaxSkewness:]
- -[CIBurstImageStat setNumHWFaces:]
- -[CIBurstImageStat setOrientation:]
- -[CIBurstImageStat setRegistrationErrorIntegral:]
- -[CIBurstImageStat setRegistrationErrorX:]
- -[CIBurstImageStat setRegistrationErrorY:]
- -[CIBurstImageStat setRoiSize:]
- -[CIBurstImageStat setTemporalOrder:]
- -[CIBurstImageStat setTimeReceived:]
- -[CIBurstImageStat setTimestamp:]
- -[CIBurstImageStat setTx:]
- -[CIBurstImageStat setTy:]
- -[CIBurstImageStat setVersion:]
- -[CIBurstImageStat temporalOrder]
- -[CIBurstImageStat timeReceived]
- -[CIBurstImageStat timestamp]
- -[CIBurstImageStat tx]
- -[CIBurstImageStat ty]
- -[CIBurstImageStat updateROI:]
- -[CIBurstImageStat version]
- -[CIBurstImageStat writeGridROI:]
- -[CIBurstThumbnailCluster addItemsFromCluster:]
- -[CIBurstThumbnailCluster burstImages]
- -[CIBurstThumbnailCluster completionBlock]
- -[CIBurstThumbnailCluster computeMergeCost:::]
- -[CIBurstThumbnailCluster dealloc]
- -[CIBurstThumbnailCluster fullsizeJpegData]
- -[CIBurstThumbnailCluster imageProps]
- -[CIBurstThumbnailCluster image]
- -[CIBurstThumbnailCluster initWithImageData:dict:identifier:imageProps:completionBlock:]
- -[CIBurstThumbnailCluster init]
- -[CIBurstThumbnailCluster releaseImage]
- -[CIBurstThumbnailCluster setBurstImages:]
- -[CIBurstThumbnailCluster setCompletionBlock:]
- -[CIBurstThumbnailCluster setFullsizeJpegData:]
- -[CIBurstThumbnailCluster setImage:]
- -[CIBurstThumbnailCluster setImageProps:]
- -[CIBurstYUVImage Cbuffer]
- -[CIBurstYUVImage Ybuffer]
- -[CIBurstYUVImage bytesPerRow]
- -[CIBurstYUVImage convertRGBAToYUV420:rgbaBytesPerRow:]
- -[CIBurstYUVImage dealloc]
- -[CIBurstYUVImage height]
- -[CIBurstYUVImage initWithCGImage:maxDimension:]
- -[CIBurstYUVImage initWithCIImage:ctx:maxDimension:]
- -[CIBurstYUVImage initWithIOSurface:maxDimension:]
- -[CIBurstYUVImage pixelBuffer]
- -[CIBurstYUVImage setBytesPerRow:]
- -[CIBurstYUVImage setCbuffer:]
- -[CIBurstYUVImage setHeight:]
- -[CIBurstYUVImage setWidth:]
- -[CIBurstYUVImage setYbuffer:]
- -[CIBurstYUVImage width]
- -[CIContext initWithOptions:].cold.2
- -[CIContext testArchive:]
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.1
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.10
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.11
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.2
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.3
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.4
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.5
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.6
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.7
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.8
- -[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:].cold.9
- -[CIContext(_createClone) _CPUShadow]
- -[CIImage _imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:]
- -[CIImage _imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:].cold.1
- -[CIImage _imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:].cold.2
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:]
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:].cold.1
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:].cold.2
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:].cold.3
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:].cold.4
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:].cold.5
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:].cold.6
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:].cold.7
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:].cold.8
- -[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:].cold.9
- -[CIImageProcessorInOut initWithSurface:texture:digest:allowSRGB:bounds:context:]
- -[CIImageProcessorInOut initWithSurface:texture:digest:allowSRGB:bounds:context:].cold.1
- -[CIImageProcessorInput initWithSurface:texture:digest:allowSRGB:bounds:context:]
- -[CIImageProcessorInput initWithSurface:texture:digest:allowSRGB:bounds:roiTileIndex:roiTileCount:context:]
- -[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:]
- -[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:].cold.1
- -[CIPersonSegmentation inputImage]
- -[CIPersonSegmentation inputQualityLevel]
- -[CIPersonSegmentation outputImage]
- -[CIPersonSegmentation outputImage].cold.1
- -[CIPersonSegmentation setInputImage:]
- -[CIPersonSegmentation setInputQualityLevel:]
- -[CISaliencyMapFilter inputImage]
- -[CISaliencyMapFilter outputImage]
- -[CISaliencyMapFilter setInputImage:]
- -[CIToneMapHeadroom srcHeadroom]
- -[CIToneMapHeadroom targetHeadroom]
- GCC_except_table124
- GCC_except_table155
- GCC_except_table164
- GCC_except_table165
- GCC_except_table168
- GCC_except_table169
- GCC_except_table173
- GCC_except_table174
- GCC_except_table178
- GCC_except_table179
- GCC_except_table180
- GCC_except_table186
- GCC_except_table199
- GCC_except_table201
- GCC_except_table202
- GCC_except_table206
- GCC_except_table207
- GCC_except_table232
- GCC_except_table233
- GCC_except_table287
- GCC_except_table288
- GCC_except_table292
- GCC_except_table295
- GCC_except_table298
- GCC_except_table301
- GCC_except_table305
- GCC_except_table315
- GCC_except_table320
- GCC_except_table325
- GCC_except_table330
- GCC_except_table335
- GCC_except_table352
- GCC_except_table379
- GCC_except_table380
- GCC_except_table382
- GCC_except_table81
- GCC_except_table89
- _AFFIRMATIVE_SUPPORT_VECTORS_v1
- _AFFIRMATIVE_SUPPORT_VECTORS_v2
- _AVCameraCalibrationDataClass
- _AVDepthDataClass
- _AVFoundationLibrary
- _AVFoundationLibrary.cold.1
- _AVFoundationLibraryCore.frameworkLibrary
- _AVPortraitEffectsMatteClass
- _AVSemanticSegmentationMatteClass
- _AVSemanticSegmentationMatteDataType
- _AVSemanticSegmentationMatteType
- _ArchiveLibrary
- _ArchiveLibrary.cold.1
- _ArchiveLibrary.cold.2
- _ArchiveLibrary.onceToken
- _BurstLoggingMessage
- _BurstLoggingSetCallback
- _BurstLoggingSetFileHandle
- _CFMakeCollectable
- _CGRectCreateDictionaryRepresentation
- _CIGVRenddererFlushRender
- _CILoadAIRArchive
- _CILoadAIRArchive.cold.1
- _CIVNAreaOfBoundsOfLandmarkRegion
- _CIVNBoundsOfLandmarkRegion
- _CIVNOrientedImageLandmarkEyeRegions
- _CIVNPointInOrientedImage
- _CIVNgetOrientation
- _CI_DEBUG_CONTEXT_COLOR
- _CI_LOG_AIR_ARCHIVE_ACTIVITY
- _CI_LOG_AIR_ARCHIVE_MISS
- _CI_USE_ARCHIVED_KERNELS
- _CMTimeGetSeconds
- _CMTimeMakeFromDictionary
- _FaceCoreLibrary
- _FaceCoreLibrary.cold.1
- _FaceCoreLibraryCore
- _FaceCoreLibraryCore.frameworkLibrary
- _FastRegistration_compareSignature
- _FastRegistration_compareSignatures
- _FastRegistration_computeSignatures
- _FastRegistration_getStatusDescription
- _FastRegistration_processProjections
- _FastRegistration_register
- _FastRegistration_statusDescription
- _FigDispatchQueueCreateWithPriority
- _MemDiff32
- _MemDiffZeroMean32
- _MemSum32
- _NEGATORY_SUPPORT_VECTORS_v1
- _NEGATORY_SUPPORT_VECTORS_v2
- _OBJC_CLASS_$_CIBurstActionClassifier
- _OBJC_CLASS_$_CIBurstClusterDivider
- _OBJC_CLASS_$_CIBurstFaceConfigEntry
- _OBJC_CLASS_$_CIBurstFaceInfo
- _OBJC_CLASS_$_CIBurstFaceScoreEntry
- _OBJC_CLASS_$_CIBurstFaceStat
- _OBJC_CLASS_$_CIBurstImageFaceAnalysisContext
- _OBJC_CLASS_$_CIBurstImageSetInternal
- _OBJC_CLASS_$_CIBurstImageStat
- _OBJC_CLASS_$_CIBurstThumbnailCluster
- _OBJC_CLASS_$_CIBurstYUVImage
- _OBJC_CLASS_$_CIPersonSegmentation
- _OBJC_CLASS_$_CIPersonSegmentationKernel
- _OBJC_CLASS_$_CISaliencyMapFilter
- _OBJC_CLASS_$_CISaliencyMapKernel
- _OBJC_CLASS_$_NSCountedSet
- _OBJC_IVAR_$_CIBurstActionClassifier._svmParameters
- _OBJC_IVAR_$_CIBurstActionClassifier.hasBeenScaled
- _OBJC_IVAR_$_CIBurstActionClassifier.testAverageCameraTravelDistance
- _OBJC_IVAR_$_CIBurstActionClassifier.testAverageRegistrationErrorSkewness
- _OBJC_IVAR_$_CIBurstActionClassifier.testBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix
- _OBJC_IVAR_$_CIBurstActionClassifier.testInOutRatio
- _OBJC_IVAR_$_CIBurstActionClassifier.testMaxInnerDistance
- _OBJC_IVAR_$_CIBurstActionClassifier.testMaxPeakRegistrationError
- _OBJC_IVAR_$_CIBurstActionClassifier.testMaxRegistrationErrorIntegral
- _OBJC_IVAR_$_CIBurstActionClassifier.testMaxRegistrationErrorSkewness
- _OBJC_IVAR_$_CIBurstActionClassifier.testMeanPeakRegistrationError
- _OBJC_IVAR_$_CIBurstActionClassifier.testMinRegionOfInterestSize
- _OBJC_IVAR_$_CIBurstActionClassifier.testVector
- _OBJC_IVAR_$_CIBurstClusterDivider.actionAmount
- _OBJC_IVAR_$_CIBurstClusterDivider.dividerScore
- _OBJC_IVAR_$_CIBurstClusterDivider.highNoiseThreshold
- _OBJC_IVAR_$_CIBurstClusterDivider.leftImage
- _OBJC_IVAR_$_CIBurstClusterDivider.noiseThreshold
- _OBJC_IVAR_$_CIBurstClusterDivider.trueLocalMaximum
- _OBJC_IVAR_$_CIBurstFaceConfigEntry.faceId
- _OBJC_IVAR_$_CIBurstFaceConfigEntry.faceRect
- _OBJC_IVAR_$_CIBurstFaceConfigEntry.framesSinceLast
- _OBJC_IVAR_$_CIBurstFaceInfo.hwCenter
- _OBJC_IVAR_$_CIBurstFaceInfo.hwFaceId
- _OBJC_IVAR_$_CIBurstFaceInfo.hwLastFrameSeen
- _OBJC_IVAR_$_CIBurstFaceInfo.hwSize
- _OBJC_IVAR_$_CIBurstFaceInfo.swCenter
- _OBJC_IVAR_$_CIBurstFaceInfo.swFaceId
- _OBJC_IVAR_$_CIBurstFaceInfo.swLastFrameSeen
- _OBJC_IVAR_$_CIBurstFaceInfo.swSize
- _OBJC_IVAR_$_CIBurstFaceScoreEntry.maxScore
- _OBJC_IVAR_$_CIBurstFaceScoreEntry.minScore
- _OBJC_IVAR_$_CIBurstFaceScoreEntry.numScores
- _OBJC_IVAR_$_CIBurstFaceScoreEntry.sumScores
- _OBJC_IVAR_$_CIBurstFaceScoreEntry.sumSqScores
- _OBJC_IVAR_$_CIBurstFaceStat.FCRBlinkFeaturesSize
- _OBJC_IVAR_$_CIBurstFaceStat.FCRLeftEyeFeaturesOffset
- _OBJC_IVAR_$_CIBurstFaceStat.FCRRightEyeFeaturesOffset
- _OBJC_IVAR_$_CIBurstFaceStat.FCRSmileAndBlinkFeatures
- _OBJC_IVAR_$_CIBurstFaceStat.FCRSmileFeaturesOffset
- _OBJC_IVAR_$_CIBurstFaceStat.FCRSmileFeaturesSize
- _OBJC_IVAR_$_CIBurstFaceStat._hwFaceRect
- _OBJC_IVAR_$_CIBurstFaceStat._isSyncedWithImage
- _OBJC_IVAR_$_CIBurstFaceStat.faceId
- _OBJC_IVAR_$_CIBurstFaceStat.faceRect
- _OBJC_IVAR_$_CIBurstFaceStat.faceScore
- _OBJC_IVAR_$_CIBurstFaceStat.focusScore
- _OBJC_IVAR_$_CIBurstFaceStat.foundByFaceCore
- _OBJC_IVAR_$_CIBurstFaceStat.framesSinceLast
- _OBJC_IVAR_$_CIBurstFaceStat.hasLeftEye
- _OBJC_IVAR_$_CIBurstFaceStat.hasRightEye
- _OBJC_IVAR_$_CIBurstFaceStat.hasRollAngle
- _OBJC_IVAR_$_CIBurstFaceStat.hasYawAngle
- _OBJC_IVAR_$_CIBurstFaceStat.hwFaceId
- _OBJC_IVAR_$_CIBurstFaceStat.leftEyeBlinkScore
- _OBJC_IVAR_$_CIBurstFaceStat.leftEyeOpen
- _OBJC_IVAR_$_CIBurstFaceStat.leftEyeRect
- _OBJC_IVAR_$_CIBurstFaceStat.normalizedFaceRect
- _OBJC_IVAR_$_CIBurstFaceStat.normalizedFocusScore
- _OBJC_IVAR_$_CIBurstFaceStat.normalizedSigma
- _OBJC_IVAR_$_CIBurstFaceStat.rightEyeBlinkScore
- _OBJC_IVAR_$_CIBurstFaceStat.rightEyeOpen
- _OBJC_IVAR_$_CIBurstFaceStat.rightEyeRect
- _OBJC_IVAR_$_CIBurstFaceStat.rollAngle
- _OBJC_IVAR_$_CIBurstFaceStat.smallFace
- _OBJC_IVAR_$_CIBurstFaceStat.smileScore
- _OBJC_IVAR_$_CIBurstFaceStat.smiling
- _OBJC_IVAR_$_CIBurstFaceStat.timestamp
- _OBJC_IVAR_$_CIBurstFaceStat.yawAngle
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext._version
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.curConfig
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.faceDetector
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.faceIdCounter
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.faceIdMapping
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.faceInfoArray
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.faceTimestampArray
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.forceFaceDetectionEnable
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.lastFaceIndex
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.latestFaceTimestamp
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.latestImageTimestamp
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.numFramesNoFaces
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.renameMapping
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.timeBlinkDetectionDone
- _OBJC_IVAR_$_CIBurstImageFaceAnalysisContext.timeFaceDetectionDone
- _OBJC_IVAR_$_CIBurstImageSetInternal._version
- _OBJC_IVAR_$_CIBurstImageSetInternal._versionString
- _OBJC_IVAR_$_CIBurstImageSetInternal.actionClassifier
- _OBJC_IVAR_$_CIBurstImageSetInternal.allImageIdentifiers
- _OBJC_IVAR_$_CIBurstImageSetInternal.bestImageIdentifiersArray
- _OBJC_IVAR_$_CIBurstImageSetInternal.burstCoverSelection
- _OBJC_IVAR_$_CIBurstImageSetInternal.burstId
- _OBJC_IVAR_$_CIBurstImageSetInternal.burstLogFileHandle
- _OBJC_IVAR_$_CIBurstImageSetInternal.burstLogFileName
- _OBJC_IVAR_$_CIBurstImageSetInternal.clusterArray
- _OBJC_IVAR_$_CIBurstImageSetInternal.clusterByImageIdentifier
- _OBJC_IVAR_$_CIBurstImageSetInternal.curClusterIndexToProcess
- _OBJC_IVAR_$_CIBurstImageSetInternal.dq
- _OBJC_IVAR_$_CIBurstImageSetInternal.dq_yuvdump
- _OBJC_IVAR_$_CIBurstImageSetInternal.dummyAnalysisCount
- _OBJC_IVAR_$_CIBurstImageSetInternal.enableAnalysis
- _OBJC_IVAR_$_CIBurstImageSetInternal.enableDumpYUV
- _OBJC_IVAR_$_CIBurstImageSetInternal.enableFaceCore
- _OBJC_IVAR_$_CIBurstImageSetInternal.faceAnalysisContext
- _OBJC_IVAR_$_CIBurstImageSetInternal.faceIDCounts
- _OBJC_IVAR_$_CIBurstImageSetInternal.isAction
- _OBJC_IVAR_$_CIBurstImageSetInternal.isPortrait
- _OBJC_IVAR_$_CIBurstImageSetInternal.maxNumPendingFrames
- _OBJC_IVAR_$_CIBurstImageSetInternal.overrideImage
- _OBJC_IVAR_$_CIBurstImageSetInternal.overrideProps
- _OBJC_IVAR_$_CIBurstImageSetInternal.sem
- _OBJC_IVAR_$_CIBurstImageSetInternal.statsByImageIdentifier
- _OBJC_IVAR_$_CIBurstImageSetInternal.temporalOrder
- _OBJC_IVAR_$_CIBurstImageStat.AEAverage
- _OBJC_IVAR_$_CIBurstImageStat.AEStable
- _OBJC_IVAR_$_CIBurstImageStat.AETarget
- _OBJC_IVAR_$_CIBurstImageStat.AFStable
- _OBJC_IVAR_$_CIBurstImageStat._AEDelta
- _OBJC_IVAR_$_CIBurstImageStat._fullsizeJpegData
- _OBJC_IVAR_$_CIBurstImageStat._fullsizeJpegSize
- _OBJC_IVAR_$_CIBurstImageStat._version
- _OBJC_IVAR_$_CIBurstImageStat.actionClusteringScore
- _OBJC_IVAR_$_CIBurstImageStat.actionScore
- _OBJC_IVAR_$_CIBurstImageStat.aeMatrix
- _OBJC_IVAR_$_CIBurstImageStat.avgHorzDiffY
- _OBJC_IVAR_$_CIBurstImageStat.blurExtent
- _OBJC_IVAR_$_CIBurstImageStat.colorHistogram
- _OBJC_IVAR_$_CIBurstImageStat.dissimilarity
- _OBJC_IVAR_$_CIBurstImageStat.doLimitedSharpnessAndBlur
- _OBJC_IVAR_$_CIBurstImageStat.emotionallyRejected
- _OBJC_IVAR_$_CIBurstImageStat.exclude
- _OBJC_IVAR_$_CIBurstImageStat.faceStatArray
- _OBJC_IVAR_$_CIBurstImageStat.facesRoiRect
- _OBJC_IVAR_$_CIBurstImageStat.gridHeight
- _OBJC_IVAR_$_CIBurstImageStat.gridROI
- _OBJC_IVAR_$_CIBurstImageStat.gridWidth
- _OBJC_IVAR_$_CIBurstImageStat.hasRegistrationData
- _OBJC_IVAR_$_CIBurstImageStat.imageId
- _OBJC_IVAR_$_CIBurstImageStat.imageScore
- _OBJC_IVAR_$_CIBurstImageStat.isGarbage
- _OBJC_IVAR_$_CIBurstImageStat.maxSkewness
- _OBJC_IVAR_$_CIBurstImageStat.normalizedFocusScore
- _OBJC_IVAR_$_CIBurstImageStat.normalizedSigma
- _OBJC_IVAR_$_CIBurstImageStat.numEntries
- _OBJC_IVAR_$_CIBurstImageStat.numHWFaces
- _OBJC_IVAR_$_CIBurstImageStat.orientation
- _OBJC_IVAR_$_CIBurstImageStat.projectionMemoryBlock
- _OBJC_IVAR_$_CIBurstImageStat.projectionSignature
- _OBJC_IVAR_$_CIBurstImageStat.registrationErrorIntegral
- _OBJC_IVAR_$_CIBurstImageStat.registrationErrorX
- _OBJC_IVAR_$_CIBurstImageStat.registrationErrorY
- _OBJC_IVAR_$_CIBurstImageStat.roiSize
- _OBJC_IVAR_$_CIBurstImageStat.sharpnessGrid
- _OBJC_IVAR_$_CIBurstImageStat.smoothedROI
- _OBJC_IVAR_$_CIBurstImageStat.temporalOrder
- _OBJC_IVAR_$_CIBurstImageStat.timeReceived
- _OBJC_IVAR_$_CIBurstImageStat.timestamp
- _OBJC_IVAR_$_CIBurstImageStat.tx
- _OBJC_IVAR_$_CIBurstImageStat.ty
- _OBJC_IVAR_$_CIBurstThumbnailCluster._fullsizeJpegData
- _OBJC_IVAR_$_CIBurstThumbnailCluster.burstImages
- _OBJC_IVAR_$_CIBurstThumbnailCluster.completionBlock
- _OBJC_IVAR_$_CIBurstThumbnailCluster.image
- _OBJC_IVAR_$_CIBurstThumbnailCluster.imageProps
- _OBJC_IVAR_$_CIBurstYUVImage.Cbuffer
- _OBJC_IVAR_$_CIBurstYUVImage.Ybuffer
- _OBJC_IVAR_$_CIBurstYUVImage.bytesPerRow
- _OBJC_IVAR_$_CIBurstYUVImage.dataPtr
- _OBJC_IVAR_$_CIBurstYUVImage.height
- _OBJC_IVAR_$_CIBurstYUVImage.ioSurf
- _OBJC_IVAR_$_CIBurstYUVImage.pixelBuffer
- _OBJC_IVAR_$_CIBurstYUVImage.width
- _OBJC_IVAR_$_CIPersonSegmentation.inputImage
- _OBJC_IVAR_$_CIPersonSegmentation.inputQualityLevel
- _OBJC_IVAR_$_CISaliencyMapFilter.inputImage
- _OBJC_METACLASS_$_CIBurstActionClassifier
- _OBJC_METACLASS_$_CIBurstClusterDivider
- _OBJC_METACLASS_$_CIBurstFaceConfigEntry
- _OBJC_METACLASS_$_CIBurstFaceInfo
- _OBJC_METACLASS_$_CIBurstFaceScoreEntry
- _OBJC_METACLASS_$_CIBurstFaceStat
- _OBJC_METACLASS_$_CIBurstImageFaceAnalysisContext
- _OBJC_METACLASS_$_CIBurstImageSetInternal
- _OBJC_METACLASS_$_CIBurstImageStat
- _OBJC_METACLASS_$_CIBurstThumbnailCluster
- _OBJC_METACLASS_$_CIBurstYUVImage
- _OBJC_METACLASS_$_CIPersonSegmentation
- _OBJC_METACLASS_$_CIPersonSegmentationKernel
- _OBJC_METACLASS_$_CISaliencyMapFilter
- _OBJC_METACLASS_$_CISaliencyMapKernel
- _PixelSumASM
- _Projections_computeCost
- _Projections_computeMeanStdTable
- _Projections_computeProjectionDerivative
- _Projections_computeShiftBruteForce
- _Projections_fastSqrtf
- _Projections_getStatusDescription
- _Projections_isZero
- _Projections_normalizeMeanStdUsingTable
- _Projections_projectionCols_planar8UtoF
- _Projections_projectionRowsCols_planar8UtoF
- _Projections_projectionRows_planar8UtoF
- _Projections_smoothProjection
- _Projections_statusDescription
- _VTPixelTransferSessionCreate
- _VTPixelTransferSessionInvalidate
- _VTPixelTransferSessionTransferImage
- __ACBSBarcodeDescriptionCodeLocation
- __ACBSBarcodeDescriptionCodeProperties
- __ACBSBarcodeDescriptionCodeRawData
- __ACBSBarcodeDescriptionCodeString
- __ACBSBarcodeDescriptionCodeType
- __ACBSBarcodeFrameInfoSymbolDescriptions
- __ACBSBarcodePropertyErrorCorrectionLevel
- __ACBSBarcodePropertyQRMaskPattern
- __ACBSBarcodePropertySymbolVersion
- __ACBSBarcodeTypeQR
- __OBJC_$_CLASS_METHODS_CIBurstImageSetInternal
- __OBJC_$_CLASS_METHODS_CIContext(Internal|_createClone|QuicklookSupport|_createCached|_createCGImageInternal|createCGImageInternal|createCGImage|ImageRepresentation|CIDepthBlurEffect|CIRenderDestination)
- __OBJC_$_CLASS_METHODS_CIPersonSegmentation
- __OBJC_$_CLASS_METHODS_CIPersonSegmentationKernel
- __OBJC_$_CLASS_METHODS_CISaliencyMapFilter
- __OBJC_$_CLASS_METHODS_CISaliencyMapKernel
- __OBJC_$_INSTANCE_METHODS_CIBurstActionClassifier
- __OBJC_$_INSTANCE_METHODS_CIBurstClusterDivider
- __OBJC_$_INSTANCE_METHODS_CIBurstFaceConfigEntry
- __OBJC_$_INSTANCE_METHODS_CIBurstFaceInfo
- __OBJC_$_INSTANCE_METHODS_CIBurstFaceScoreEntry
- __OBJC_$_INSTANCE_METHODS_CIBurstFaceStat
- __OBJC_$_INSTANCE_METHODS_CIBurstImageFaceAnalysisContext
- __OBJC_$_INSTANCE_METHODS_CIBurstImageSetInternal
- __OBJC_$_INSTANCE_METHODS_CIBurstImageStat
- __OBJC_$_INSTANCE_METHODS_CIBurstThumbnailCluster
- __OBJC_$_INSTANCE_METHODS_CIBurstYUVImage
- __OBJC_$_INSTANCE_METHODS_CIContext(Internal|_createClone|QuicklookSupport|_createCached|_createCGImageInternal|createCGImageInternal|createCGImage|ImageRepresentation|CIDepthBlurEffect|CIRenderDestination)
- __OBJC_$_INSTANCE_METHODS_CIPersonSegmentation
- __OBJC_$_INSTANCE_METHODS_CISaliencyMapFilter
- __OBJC_$_INSTANCE_VARIABLES_CIBurstActionClassifier
- __OBJC_$_INSTANCE_VARIABLES_CIBurstClusterDivider
- __OBJC_$_INSTANCE_VARIABLES_CIBurstFaceConfigEntry
- __OBJC_$_INSTANCE_VARIABLES_CIBurstFaceInfo
- __OBJC_$_INSTANCE_VARIABLES_CIBurstFaceScoreEntry
- __OBJC_$_INSTANCE_VARIABLES_CIBurstFaceStat
- __OBJC_$_INSTANCE_VARIABLES_CIBurstImageFaceAnalysisContext
- __OBJC_$_INSTANCE_VARIABLES_CIBurstImageSetInternal
- __OBJC_$_INSTANCE_VARIABLES_CIBurstImageStat
- __OBJC_$_INSTANCE_VARIABLES_CIBurstThumbnailCluster
- __OBJC_$_INSTANCE_VARIABLES_CIBurstYUVImage
- __OBJC_$_INSTANCE_VARIABLES_CIPersonSegmentation
- __OBJC_$_INSTANCE_VARIABLES_CISaliencyMapFilter
- __OBJC_$_PROP_LIST_CIBurstActionClassifier
- __OBJC_$_PROP_LIST_CIBurstClusterDivider
- __OBJC_$_PROP_LIST_CIBurstFaceConfigEntry
- __OBJC_$_PROP_LIST_CIBurstFaceInfo
- __OBJC_$_PROP_LIST_CIBurstFaceScoreEntry
- __OBJC_$_PROP_LIST_CIBurstFaceStat
- __OBJC_$_PROP_LIST_CIBurstImageFaceAnalysisContext
- __OBJC_$_PROP_LIST_CIBurstImageSetInternal
- __OBJC_$_PROP_LIST_CIBurstImageStat
- __OBJC_$_PROP_LIST_CIBurstThumbnailCluster
- __OBJC_$_PROP_LIST_CIBurstYUVImage
- __OBJC_$_PROP_LIST_CIImageProcessorInput.143
- __OBJC_$_PROP_LIST_CIImageProcessorOutput.126
- __OBJC_$_PROP_LIST_CIPersonSegmentation
- __OBJC_$_PROP_LIST_CISaliencyMapFilter
- __OBJC_CLASS_PROTOCOLS_$_CIBurstFaceStat
- __OBJC_CLASS_RO_$_CIBurstActionClassifier
- __OBJC_CLASS_RO_$_CIBurstClusterDivider
- __OBJC_CLASS_RO_$_CIBurstFaceConfigEntry
- __OBJC_CLASS_RO_$_CIBurstFaceInfo
- __OBJC_CLASS_RO_$_CIBurstFaceScoreEntry
- __OBJC_CLASS_RO_$_CIBurstFaceStat
- __OBJC_CLASS_RO_$_CIBurstImageFaceAnalysisContext
- __OBJC_CLASS_RO_$_CIBurstImageSetInternal
- __OBJC_CLASS_RO_$_CIBurstImageStat
- __OBJC_CLASS_RO_$_CIBurstThumbnailCluster
- __OBJC_CLASS_RO_$_CIBurstYUVImage
- __OBJC_CLASS_RO_$_CIPersonSegmentation
- __OBJC_CLASS_RO_$_CIPersonSegmentationKernel
- __OBJC_CLASS_RO_$_CISaliencyMapFilter
- __OBJC_CLASS_RO_$_CISaliencyMapKernel
- __OBJC_METACLASS_RO_$_CIBurstActionClassifier
- __OBJC_METACLASS_RO_$_CIBurstClusterDivider
- __OBJC_METACLASS_RO_$_CIBurstFaceConfigEntry
- __OBJC_METACLASS_RO_$_CIBurstFaceInfo
- __OBJC_METACLASS_RO_$_CIBurstFaceScoreEntry
- __OBJC_METACLASS_RO_$_CIBurstFaceStat
- __OBJC_METACLASS_RO_$_CIBurstImageFaceAnalysisContext
- __OBJC_METACLASS_RO_$_CIBurstImageSetInternal
- __OBJC_METACLASS_RO_$_CIBurstImageStat
- __OBJC_METACLASS_RO_$_CIBurstThumbnailCluster
- __OBJC_METACLASS_RO_$_CIBurstYUVImage
- __OBJC_METACLASS_RO_$_CIPersonSegmentation
- __OBJC_METACLASS_RO_$_CIPersonSegmentationKernel
- __OBJC_METACLASS_RO_$_CISaliencyMapFilter
- __OBJC_METACLASS_RO_$_CISaliencyMapKernel
- __Z14_ci_read_pixelPKN2CI13BitmapSamplerERK4mat34vec2
- __Z15_ci_write_pixelPKN2CI13BitmapSamplerE4vec46IPoint
- __Z18_ci_linear_to_srgb4vec4
- __Z18_ci_read_pixel_420PKN2CI13BitmapSamplerERK4mat3S2_4vec2S6_
- __Z18_ci_srgb_to_linear4vec4
- __ZGVZ22CI_DEBUG_CONTEXT_COLORE1v
- __ZGVZ23CI_LOG_AIR_ARCHIVE_MISSE1v
- __ZGVZ23CI_USE_ARCHIVED_KERNELSE1v
- __ZGVZ27CI_LOG_AIR_ARCHIVE_ACTIVITYE1v
- __ZL12calcUniformsff
- __ZL12post_processP7NSArrayIP21CIImageProcessorInputEP22CIImageProcessorOutputPN2CI7ContextE
- __ZL15convert_weightsPKdPfjj
- __ZL19soft_ACBSConfigFreeP10ACBSConfig
- __ZL19soft_ACBSConfigFreeP10ACBSConfig.cold.1
- __ZL21soft_ACBSConfigCreatev
- __ZL21soft_ACBSConfigCreatev.cold.1
- __ZL36soft_ACBSConfigSetMaxQRModuleSamplesP10ACBSConfigi
- __ZL36soft_ACBSConfigSetMaxQRModuleSamplesP10ACBSConfigi.cold.1
- __ZL36soft_ACBSConfigSetSymbologiesEnabledP10ACBSConfigPK9__CFArray
- __ZL36soft_ACBSConfigSetSymbologiesEnabledP10ACBSConfigPK9__CFArray.cold.1
- __ZL44getkCMPhotoCompressionContainerOption_Formatv
- __ZL44getkCMPhotoCompressionContainerOption_Formatv.cold.1
- __ZL47soft_CMPhotoCompressionSessionAddAuxiliaryImageP25CMPhotoCompressionSessionliPK15CGImageMetadataPK14__CFDictionaryPKvPl
- __ZL47soft_CMPhotoCompressionSessionAddAuxiliaryImageP25CMPhotoCompressionSessionliPK15CGImageMetadataPK14__CFDictionaryPKvPl.cold.1
- __ZL48soft_CMPhotoCompressionSessionOpenEmptyContainerP25CMPhotoCompressionSessionPK14__CFDictionary
- __ZL48soft_CMPhotoCompressionSessionOpenEmptyContainerP25CMPhotoCompressionSessionPK14__CFDictionary.cold.1
- __ZL49getkCMPhotoCompressionContainerOption_BackingTypev
- __ZL49getkCMPhotoCompressionContainerOption_BackingTypev.cold.1
- __ZL52getkCMPhotoCompressionContainerOption_ImageCountHintv
- __ZL52getkCMPhotoCompressionContainerOption_ImageCountHintv.cold.1
- __ZL58soft_CMPhotoCompressionSessionCloseContainerAndCopyBackingP25CMPhotoCompressionSessionPiPmPPKv
- __ZL58soft_CMPhotoCompressionSessionCloseContainerAndCopyBackingP25CMPhotoCompressionSessionPiPmPPKv.cold.1
- __ZL61soft_ACBSCreateFrameInfoBySearchingForBarcodesInCVPixelBufferP10ACBSConfigP10__CVBuffer6CGRectj
- __ZL61soft_ACBSCreateFrameInfoBySearchingForBarcodesInCVPixelBufferP10ACBSConfigP10__CVBuffer6CGRectj.cold.1
- __ZL76soft_ACBSCreateSymbolDescriptorFromBasicDescriptorWithDefaultPayloadEncodingPK14__CFDictionaryPK10__CFString
- __ZL76soft_ACBSCreateSymbolDescriptorFromBasicDescriptorWithDefaultPayloadEncodingPK14__CFDictionaryPK10__CFString.cold.1
- __ZN2CI106f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f_clr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f2_f3_f2_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_clr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_f2_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_f3_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_f4_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_f4_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_s_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_s_s_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_s_s_s_sERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_sr_f2_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_sr_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_sr_f_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10f4_sr_sr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI10none_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11CGRectArrayC2ERK6CGRect
- __ZN2CI11ColorKernel17set_blendBehaviorENS0_22BlendKernelBehaviorBitEb
- __ZN2CI11ConvertNode24append_to_tree_and_unrefEPNS_4NodeENS_11ConvertTypeE
- __ZN2CI11ConvertNodeC2EPNS_4NodeENS_11ConvertTypeEbU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS4_9allocatorIS7_EEEERKNS5_INS_7TextureENS8_ISD_EEEERKNS5_INS_17NodeContentDigestENS8_ISI_EEEERKNS5_I6CGRectNS8_ISN_EEEERKNS5_IbNS8_IbEEEES7_SD_SI_SN_biPNS_7ContextEPNS_8TileTaskEE
- __ZN2CI11f2_f2_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f2_f2_f2_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f2_f2_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f2_f3_f3_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f2_f4_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f2_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_f4_f_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_s_clr_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_s_f_f_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_s_s_f3_sERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_s_s_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_s_s_s_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_sr_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_sr_f2_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_sr_f4_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_sr_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_sr_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_sr_sr_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI11f4_sr_sr_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12MetalContext12bind_surfaceEP11__IOSurfaceRKNS_17TextureDescriptorEbNS_10SampleModeENS_8EdgeModeEii
- __ZN2CI12MetalContext12bind_textureEPKvNS_10SampleModeENS_8EdgeModeEi
- __ZN2CI12MetalContextC1EPKvPKcP12CGColorSpaceS6_NS_11PixelFormatEbmmybb
- __ZN2CI12MetalContextC2EPKvPKcP12CGColorSpaceS6_NS_11PixelFormatEbmmybb
- __ZN2CI12ProviderNodeC1ENS_10ImageIndexENS_22ImageLeafContentDigestEPK10__CFStringU13block_pointerFvPvmmmmmmEP16dispatch_queue_smmNSt3__16vectorINSC_I5IRectNSB_9allocatorISD_EEEENSE_ISG_EEEENS_11PixelFormatESJ_NS_9AlphaModeENS_8EdgeModeEbbb
- __ZN2CI12ProviderNodeC2ENS_10ImageIndexENS_22ImageLeafContentDigestEPK10__CFStringU13block_pointerFvPvmmmmmmEP16dispatch_queue_smmNSt3__16vectorINSC_I5IRectNSB_9allocatorISD_EEEENSE_ISG_EEEENS_11PixelFormatESJ_NS_9AlphaModeENS_8EdgeModeEbbb
- __ZN2CI12SurfaceImageC1EP11__IOSurfaceNS_22ImageLeafContentDigestENS_11PixelFormatEfiPKvNS_9AlphaModeENS_8EdgeModeEbb
- __ZN2CI12SurfaceImageC2EP11__IOSurfaceNS_22ImageLeafContentDigestENS_11PixelFormatEfiPKvNS_9AlphaModeENS_8EdgeModeEbb
- __ZN2CI12f4_f2_f_f_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_f4_f4_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_s_clr_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_s_f2_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_s_f3_f3_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_s_f_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_s_s_f3_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_s_s_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_s_s_s_s_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_s_sr2d_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_s_sr2d_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI12f4_sr_sr_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13KernelArchive4findEyPKc
- __ZN2CI13KernelArchiveC2ENSt3__16vectorINS1_4pairIPKvS5_EENS1_9allocatorIS6_EEEE
- __ZN2CI13KernelArchiveC2ENSt3__16vectorINS1_4pairIPKvS5_EENS1_9allocatorIS6_EEEE.cold.1
- __ZN2CI13ProcessorNode12set_callbackEU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS1_9allocatorIS4_EEEERKNS2_INS_7TextureENS5_ISA_EEEERKNS2_INS_17NodeContentDigestENS5_ISF_EEEERKNS2_I6CGRectNS5_ISK_EEEERKNS2_IbNS5_IbEEEES4_SA_SF_SK_biPNS_7ContextEPNS_8TileTaskEE
- __ZN2CI13ProcessorNode14append_to_treeEPNS_20SerialObjectPtrArrayEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvRKNS4_IP11__IOSurfaceNS6_ISC_EEEERKNS4_INS_7TextureENS6_ISH_EEEERKNS4_INS_17NodeContentDigestENS6_ISM_EEEERKS8_RKNS4_IbNS6_IbEEEESC_SH_SM_S5_biPNS_7ContextEPNS_8TileTaskEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPS19_PKbS19_bbbbbb
- __ZN2CI13ProcessorNode14append_to_treeEU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS1_9allocatorIS4_EEEERKNS2_INS_7TextureENS5_ISA_EEEERKNS2_INS_17NodeContentDigestENS5_ISF_EEEERKNS2_I6CGRectNS5_ISK_EEEERKNS2_IbNS5_IbEEEES4_SA_SF_SK_biPNS_7ContextEPNS_8TileTaskEERKSK_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES15_bbbb
- __ZN2CI13ProcessorNodeC2EPNS_20SerialObjectPtrArrayEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvRKNS4_IP11__IOSurfaceNS6_ISC_EEEERKNS4_INS_7TextureENS6_ISH_EEEERKNS4_INS_17NodeContentDigestENS6_ISM_EEEERKS8_RKNS4_IbNS6_IbEEEESC_SH_SM_S5_biPNS_7ContextEPNS_8TileTaskEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatEPS19_PKbS19_bbbbbb
- __ZN2CI13ProcessorNodeC2EPNS_4NodeEU13block_pointerFNSt3__16vectorI6CGRectNS3_9allocatorIS5_EEEEiS5_EU13block_pointerFvRKNS4_IP11__IOSurfaceNS6_ISC_EEEERKNS4_INS_7TextureENS6_ISH_EEEERKNS4_INS_17NodeContentDigestENS6_ISM_EEEERKS8_RKNS4_IbNS6_IbEEEESC_SH_SM_S5_biPNS_7ContextEPNS_8TileTaskEERKS5_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES19_S19_bbbbbb
- __ZN2CI13ProcessorNodeC2EU13block_pointerFvRKNSt3__16vectorIP11__IOSurfaceNS1_9allocatorIS4_EEEERKNS2_INS_7TextureENS5_ISA_EEEERKNS2_INS_17NodeContentDigestENS5_ISF_EEEERKNS2_I6CGRectNS5_ISK_EEEERKNS2_IbNS5_IbEEEES4_SA_SF_SK_biPNS_7ContextEPNS_8TileTaskEERKSK_PK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES15_bbbb
- __ZN2CI13ProviderImageC1ENS_22ImageLeafContentDigestEPK10__CFStringU13block_pointerFvPvmmmmmmEmmNSt3__16vectorINS9_I5IRectNS8_9allocatorISA_EEEENSB_ISD_EEEENS_11PixelFormatEfiPKvNS_9AlphaModeENS_8EdgeModeEbbb
- __ZN2CI13ProviderImageC2ENS_22ImageLeafContentDigestEPK10__CFStringU13block_pointerFvPvmmmmmmEmmNSt3__16vectorINS9_I5IRectNS8_9allocatorISA_EEEENSB_ISD_EEEENS_11PixelFormatEfiPKvNS_9AlphaModeENS_8EdgeModeEbbb
- __ZN2CI13SetPropsImage10makeDigestENS_11ImageDigestE
- __ZN2CI13f2_f2_f_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_f3_clr_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_f4_clr_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_f4_f_clr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_f4_f_f_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_s_f3_f3_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_s_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_s_f_f_f_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_s_s_clr_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_s_s_s_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_sr_sr_f2_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_sr_sr_f_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI13f4_sr_sr_f_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14ProcessorImageC1EPNS_20SerialObjectPtrArrayE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbS8_bbbbbbU13block_pointerFNSt3__16vectorIS3_NSC_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSD_IP11__IOSurfaceNSE_ISK_EEEERKNSD_INS_7TextureENSE_ISP_EEEERKNSD_INS_17NodeContentDigestENSE_ISU_EEEERKSG_RKNSD_IbNSE_IbEEEESK_SP_SU_S3_biPNS_7ContextEPNS_8TileTaskEE
- __ZN2CI14ProcessorImageC1EPNS_5ImageE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES8_bbbbbU13block_pointerFNSt3__16vectorIS3_NS9_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSA_IP11__IOSurfaceNSB_ISH_EEEERKNSA_INS_7TextureENSB_ISM_EEEERKNSA_INS_17NodeContentDigestENSB_ISR_EEEERKSD_RKNSA_IbNSB_IbEEEESH_SM_SR_S3_biPNS_7ContextEPNS_8TileTaskEE
- __ZN2CI14ProcessorImageC2EPNS_20SerialObjectPtrArrayE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbPNS_11PixelFormatEPKbS8_bbbbbbU13block_pointerFNSt3__16vectorIS3_NSC_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSD_IP11__IOSurfaceNSE_ISK_EEEERKNSD_INS_7TextureENSE_ISP_EEEERKNSD_INS_17NodeContentDigestENSE_ISU_EEEERKSG_RKNSD_IbNSE_IbEEEESK_SP_SU_S3_biPNS_7ContextEPNS_8TileTaskEE
- __ZN2CI14ProcessorImageC2EPNS_5ImageE6CGRectPK10__CFStringNS_24ProcessorArgumentsDigestEbNS_11PixelFormatES8_bbbbbU13block_pointerFNSt3__16vectorIS3_NS9_9allocatorIS3_EEEEiS3_EU13block_pointerFvRKNSA_IP11__IOSurfaceNSB_ISH_EEEERKNSA_INS_7TextureENSB_ISM_EEEERKNSA_INS_17NodeContentDigestENSB_ISR_EEEERKSD_RKNSA_IbNSB_IbEEEESH_SM_SR_S3_biPNS_7ContextEPNS_8TileTaskEE
- __ZN2CI14TextureManager10wiredBytesEv
- __ZN2CI14f2_f2_f3_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f2_f3_f3_f3_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_s_f_f_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_s_s_f2_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_s_s_f3_f_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_s_s_s_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_s_s_s_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_sr2d_f4_gidERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_sr_f2_f2_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_sr_f2_f3_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_sr_f2_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_sr_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_sr_f4_sr_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_sr_sr_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_sr_sr_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI14f4_sr_sr_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI15ColorMatchImage10makeDigestENS_11ImageDigestEP12CGColorSpaceS3_f
- __ZN2CI15ColorMatchImageC1EPNS_5ImageEP12CGColorSpacef
- __ZN2CI15ColorMatchImageC2EPNS_5ImageEP12CGColorSpacef
- __ZN2CI15InstanceCountedILNS_4TypeE18EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE18EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE30EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE30EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE31EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE31EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE46EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE46EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE47EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE47EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE48EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE48EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE49EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE49EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE59EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE59EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE67EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE67EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE68EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE68EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE71EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE71EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE75EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE75EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE76EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE76EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE78EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE78EED1Ev
- __ZN2CI15InstanceCountedILNS_4TypeE85EED0Ev
- __ZN2CI15InstanceCountedILNS_4TypeE85EED1Ev
- __ZN2CI15KernelArguments13name_for_typeENS_18KernelArgumentTypeE
- __ZN2CI15f4_s_sr2d_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI15f4_s_sr2d_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI15f4_sr2d_f3x3_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI15f4_sr_f4_f4_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI15find_in_archiveEPNS_13KernelArchiveENS_13ProgramDigestEPKc
- __ZN2CI15none_s_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI16ColorKernelImageC1EPKNS_6KernelEPNS_20SerialObjectPtrArrayE6CGRectU13block_pointerFS6_iS6_EbNS_11PixelFormatEf
- __ZN2CI16ColorKernelImageC2EPKNS_6KernelEPNS_20SerialObjectPtrArrayE6CGRectU13block_pointerFS6_iS6_EbNS_11PixelFormatEf
- __ZN2CI16GLTextureManager10wiredBytesEv
- __ZN2CI16f2_f2_f2_f_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI16f4_f2_clr_clr_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI16f4_f4_f4_f_clr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI16f4_s_f3_f3_f4_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI16f4_s_f4_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI16f4_s_s_f3_f3_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI16f4_sr_f2_f2_f2_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI16f4_sr_f2_f4_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI16f4_sr_sr_f3_f_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI17ImageWithChildrenC2EPNS_5ImageE
- __ZN2CI17f4_f2_f4_f4_f_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI17f4_s_s_s_s_s_s_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI17f4_sr_sr_f2_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI17f4_sr_sr_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI17f4_sr_sr_sr_f2_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI18GeneralKernelImageC1EPNS_13GeneralKernelEPNS_20SerialObjectPtrArrayERKNSt3__16vectorI6CGRectNS5_9allocatorIS7_EEEES7_U13block_pointerFS7_iS7_ENS_11PixelFormatEb
- __ZN2CI18GeneralKernelImageC2EPNS_13GeneralKernelEPNS_20SerialObjectPtrArrayERKNSt3__16vectorI6CGRectNS5_9allocatorIS7_EEEES7_U13block_pointerFS7_iS7_ENS_11PixelFormatEb
- __ZN2CI18f4_f2_f2_clr_clr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI18f4_s_s_f3_f4_f4_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI18f4_sr_f2_f_f_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI18new_kernel_archiveENSt3__16vectorINS0_4pairIPKvS4_EENS0_9allocatorIS5_EEEE
- __ZN2CI19f4_s_f4_f4_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI20CIColorCurvesKernels19arg_name_img_targHRE
- __ZN2CI20CIColorCurvesKernels42arg_name_img_srcHR_targHR_targRefWt_bezierE
- __ZN2CI20CIColorCurvesKernelsL31arg_type_Sample_Float_DestCoordE
- __ZN2CI20CIColorCurvesKernelsL50arg_type_Sample_Float_Float_Float_Float4_DestCoordE
- __ZN2CI20f4_s_f2_f2_f_f_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI20f4_s_f2_f4_f_sr2d_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI20f4_s_s_s_s_s_f_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI20f4_sr_f4_f4_f2_f4_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI20f4_sr_sr_f2_f2_f2_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI20f4_sr_sr_sr_f2_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI20f4_sr_sr_sr_f2_f4_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI21add_to_kernel_archiveEPNS_13KernelArchiveENSt3__14pairIPKvS5_EE
- __ZN2CI21f4_f2_f2_f2_f_f_f_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI21f4_s_f4_f4_f4_f4_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI21f4_s_s_f2_clr_s_f4_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI21f4_s_s_f2_f4_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI22f4_f4_f4_f4_f4_f_clr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI22f4_s_f2_f3_f4_f2_f2_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI22f4_sr_sr_f4_f4_f2_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI23f4_s_s_f3_f3_f3_f_f3_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI23f4_sr2d_f3x3_sr2d_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI23f4_sr_f2_f2_f_f2_f2_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI23f4_sr_sr_f4_f4_f4_f4_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI23swizzler_builtinKernels26arg_name_color_shuffleMaskE
- __ZN2CI23swizzler_builtinKernelsL36arg_type_Float4_Float4_PrivDestCoordE
- __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEU13block_pointerFbS0_E
- __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEU13block_pointerFbS0_E.cold.1
- __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEU13block_pointerFbS0_E.cold.2
- __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEU13block_pointerFbS0_E.cold.3
- __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEU13block_pointerFbS0_E.cold.4
- __ZN2CI24format_swizzle_for_inputENS_11PixelFormatEU13block_pointerFbS0_E.cold.5
- __ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxRKNS_6BitmapES3_NS_7TextureENS_11ConvertTypeE
- __ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxRKNS_6BitmapES3_NS_7TextureENS_11ConvertTypeE.cold.1
- __ZN2CI25f4_sr_sr_f2_f2_f2_f2_f2_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI25format_swizzle_for_outputENS_11PixelFormatEjU13block_pointerFbS0_E
- __ZN2CI25format_swizzle_for_outputENS_11PixelFormatEjU13block_pointerFbS0_E.cold.1
- __ZN2CI25format_swizzle_for_outputENS_11PixelFormatEjU13block_pointerFbS0_E.cold.2
- __ZN2CI25format_swizzle_for_outputENS_11PixelFormatEjU13block_pointerFbS0_E.cold.3
- __ZN2CI26f4_sr_f2_f2_f_f_f_f_f3_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI26f4_sr_f4_f4_f4_f4_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI26f4_sr_sr_f4_f4_f4_f2_f4_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI26f4_sr_sr_f4_f4_f4_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI27CIRectangleGeneratorKernels28arg_name_bounds_radius_colorE
- __ZN2CI27CIRectangleGeneratorKernels34arg_name_bounds_radius_width_colorE
- __ZN2CI27CIRectangleGeneratorKernelsL43arg_type_Float4_Float_Float_Color_DestCoordE
- __ZN2CI28f4_sr_f4_f4_f4_f4_f_sr_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI28f4_sr_sr_f4_f2_f4_f2_f4_f2_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI28f4_sr_sr_sr_sr_sr_sr_sr_sr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI2f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI2f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI31f4_s_f_f4_f_f4_f_f4_f_f4_f_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI31f4_s_s_s_s_s_clr_clr_clr_clr_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI34f4_f4_f4_f4_f4_f4_f4_f4_f4_f_clr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI34f4_s_clr_clr_clr_clr_clr_clr_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI34f4_s_f3_f3_f3_f3_f3_f3_f3_f3_f3_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI34f4_sr_sr_f4_f2_f4_f2_f4_f2_f_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI34f4_sr_sr_sr_f4_f2_f4_f2_f4_f2_f_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI41f4_sr_sr_f4_f2_f4_f2_f4_f2_f_f4_f_f_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI44f4_sr_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI4f4_sERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI58f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f4_f_clr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI5f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI5f2_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI5f4_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI5f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI5f4_srERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI6BitmapC1EP7CGImage
- __ZN2CI6BitmapC1Ev
- __ZN2CI6f4_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI6f4_s_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI6f4_s_sERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI6none_sERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI7CGImageC1EP7CGImagefNS_22ImageLeafContentDigestEPKvNS_8EdgeModeEbbb
- __ZN2CI7CGImageC2EP7CGImagefNS_22ImageLeafContentDigestEPKvNS_8EdgeModeEbbb
- __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb
- __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb.cold.1
- __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb.cold.2
- __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb.cold.3
- __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb.cold.4
- __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb.cold.5
- __ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb.cold.6
- __ZN2CI7Context21render_processor_nodeEPNS_8TileTaskERKNS_9parentROIEP11__IOSurfaceNS_7TextureE
- __ZN2CI7f2_f2_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI7f4_f4_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI7f4_s_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI7f4_s_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI7f4_s_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI7f4_sr_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8MetalDAG7compileENS_9NodeIndexE
- __ZN2CI8MetalDAGC2EPKcPKNS_12MetalContextENSt3__110shared_ptrINS_25ConcatenatedDAGDescriptorEEEPNS_14SerialValArrayIiEESC_mRKNS_21DestinationDescriptorE
- __ZN2CI8MetalDAGD0Ev
- __ZN2CI8MetalDAGD1Ev
- __ZN2CI8MetalDAGD2Ev
- __ZN2CI8f2_f2_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f2_f2_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f2_f2_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f2_f3_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f2_f4_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f4_s_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f4_s_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f4_s_s_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f4_s_s_sERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f4_sr_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f4_sr_f3ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f4_sr_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI8f4_sr_srERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI9GLContext12bind_surfaceEP11__IOSurfaceRKNS_17TextureDescriptorEbNS_10SampleModeENS_8EdgeModeEii
- __ZN2CI9GLContext12bind_textureEPKvNS_10SampleModeENS_8EdgeModeEi
- __ZN2CI9SWContext12bind_surfaceEP11__IOSurfaceRKNS_17TextureDescriptorEbNS_10SampleModeENS_8EdgeModeEii
- __ZN2CI9SWContext12bind_textureEPKvNS_10SampleModeENS_8EdgeModeEi
- __ZN2CI9f4_f4_clrERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI9f4_s_f2_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI9f4_s_s_f2ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI9f4_s_s_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI9f4_sr_f_fERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CI9none_s_f4ERKNS_22SWRendererFunctionNodeEPKNS_26SWRendererFunctionArgumentEPNS_24SWRendererFunctionOutputEP10SamplerObjPvRK6IPointm
- __ZN2CIL10isRootNodeEPKNS_11ProgramNodeE
- __ZN2CIL12isPriorEntryEPKNS_17SurfaceCacheEntryE
- __ZN2CIL15_ci_writeTG_42XE
- __ZN2CIL17_ci_writeSIMD_42XE
- __ZN2CIL17recurseGraphStatsEPNS_4NodeES1_iiRNSt3__16vectorIPKS0_NS2_9allocatorIS5_EEEEPNS2_3mapIS5_NS_13useCountDepthENS2_4lessIS5_EENS6_INS2_4pairIKS5_SB_EEEEEE
- __ZN2CIL19MoveCacheEntryToEndEPNS_17SurfaceCacheEntryE
- __ZN2CIL19print_program_graphEPNS_7ContextEPKNS_17RenderDestinationEdPKNS_8TileTaskEPKcPNS_4NodeERK6CGRectNS_11PixelFormatE
- __ZN2CIL20_ci_writeTG_42X_nameE
- __ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ff
- __ZN2CIL22_ci_writeSIMD_42X_nameE
- __ZN2CIL23_traverse_program_graphENS_6roiKeyERNS_8liveROIsERm
- __ZN2CIL37traverse_node_graph_gathering_digestsEPKNS_7ContextEPNS_4NodeE
- __ZN8cikernelL10_CElumaToRE4vec4
- __ZN8cikernelL10_CEstretchE4vec4S0_f
- __ZN8cikernelL10_DEminmax4EP10SamplerObj4vec2
- __ZN8cikernelL10_KM_defuseEP10SamplerObjS1_ff
- __ZN8cikernelL10_KM_selectEP10SamplerObjS1_ff
- __ZN8cikernelL10_LabDeltaEE4vec4S0_
- __ZN8cikernelL10_barsSwipeE4vec34vec2f
- __ZN8cikernelL10_boxBlur11EP10SamplerObj4vec2
- __ZN8cikernelL10_boxBlur13EP10SamplerObj4vec2
- __ZN8cikernelL10_cheapBlurEP10SamplerObj4vec2
- __ZN8cikernelL10_ci_10of16E4vec4
- __ZN8cikernelL10_ci_affineE4vec4S0_
- __ZN8cikernelL10_ci_premulE4vec4
- __ZN8cikernelL10_cmyk_cyanE4vec4S0_4vec2S0_f
- __ZN8cikernelL10_colorcubeE4vec4PKN2CI13BitmapSamplerES0_
- __ZN8cikernelL10_computeABE4vec4S0_S0_S0_f
- __ZN8cikernelL10_dotscreenE4vec44vec3S0_
- __ZN8cikernelL10_drr_boostE4vec4f
- __ZN8cikernelL10_drr_noiseEff
- __ZN8cikernelL10_drr_pclipE4vec4f
- __ZN8cikernelL10_edgesPrepE4vec4
- __ZN8cikernelL10_findEdgesEP10SamplerObjf
- __ZN8cikernelL10_flashGeomE4vec2
- __ZN8cikernelL10_guideMonoE4vec4
- __ZN8cikernelL10_horizAvg2EP10SamplerObj
- __ZN8cikernelL10_horizAvg4EP10SamplerObj
- __ZN8cikernelL10_horizAvg8EP10SamplerObj
- __ZN8cikernelL10_horizMax4EP10SamplerObjff
- __ZN8cikernelL10_horizMin4EP10SamplerObjff
- __ZN8cikernelL10_innerGorSE4vec4S0_f
- __ZN8cikernelL10_laplacianE4vec4S0_S0_
- __ZN8cikernelL10_lumaRangeE4vec4ff
- __ZN8cikernelL10_median3x3EP10SamplerObj
- __ZN8cikernelL10_outerGorSE4vec4S0_f
- __ZN8cikernelL10_palettizeEP10SamplerObjS1_f
- __ZN8cikernelL10_pixellateE4vec2S0_
- __ZN8cikernelL10_rectangleE4vec4S0_S0_
- __ZN8cikernelL10_rer_glintE4vec4S0_f
- __ZN8cikernelL10_ringAvg16EP10SamplerObj4vec4
- __ZN8cikernelL10_ringAvg24EP10SamplerObj4vec44vec2
- __ZN8cikernelL10_ringAvg32EP10SamplerObj4vec4S2_
- __ZN8cikernelL10_spotColorE4vec4S0_S0_S0_S0_S0_S0_S0_S0_
- __ZN8cikernelL10_spotLightE4vec44vec3S1_S0_4vec2
- __ZN8cikernelL10_starshineE4vec24vec4S1_fS1_
- __ZN8cikernelL10_tiltShiftEP10SamplerObjS1_S1_4vec2S2_S2_
- __ZN8cikernelL10_toneCurveE4vec4fS0_fS0_fS0_fS0_fS0_f
- __ZN8cikernelL10_vertAvg16EP10SamplerObj
- __ZN8cikernelL11_ACCentroidE4vec4S0_
- __ZN8cikernelL11_DE_compinvE4vec4
- __ZN8cikernelL11_boxBlur3x3EP10SamplerObj
- __ZN8cikernelL11_boxFilter3EP10SamplerObj
- __ZN8cikernelL11_cannyFinalE4vec4
- __ZN8cikernelL11_ci_la_to_aE4vec4
- __ZN8cikernelL11_ci_la_to_iE4vec4
- __ZN8cikernelL11_ci_nearestEv
- __ZN8cikernelL11_ci_rg_to_aE4vec4
- __ZN8cikernelL11_ci_rg_to_iE4vec4
- __ZN8cikernelL11_cmyk_blackE4vec4S0_4vec2S0_f
- __ZN8cikernelL11_colorClampE4vec4S0_S0_
- __ZN8cikernelL11_conv3x3symEP10SamplerObj4vec4
- __ZN8cikernelL11_convrgb3x3EP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL11_destDitherE4vec4S0_f
- __ZN8cikernelL11_drr_rcsoftE4vec4fff
- __ZN8cikernelL11_drr_repairE4vec4S0_S0_S0_S0_ffff
- __ZN8cikernelL11_falseColorE4vec4S0_S0_
- __ZN8cikernelL11_flashColorE4vec4S0_4vec2S0_S0_S0_S1_
- __ZN8cikernelL11_horizAvg16EP10SamplerObj
- __ZN8cikernelL11_lanczosUpHEP10SamplerObjf
- __ZN8cikernelL11_lanczosUpVEP10SamplerObjf
- __ZN8cikernelL11_linescreenE4vec44vec3S0_
- __ZN8cikernelL11_localBoostE4vec4S0_S0_S0_S0_S0_f
- __ZN8cikernelL11_motionBlurEP10SamplerObj4vec4
- __ZN8cikernelL11_otsuThreshE4vec4S0_
- __ZN8cikernelL11_paddedTileE4vec4
- __ZN8cikernelL11_plusDarkerE4vec4S0_
- __ZN8cikernelL11_polyKernelE4vec4S0_f
- __ZN8cikernelL11_rectstrokeE4vec4fS0_
- __ZN8cikernelL11_reduceCropEP10SamplerObj
- __ZN8cikernelL11_resetalphaE4vec4S0_
- __ZN8cikernelL11_scaleClampE4vec4f
- __ZN8cikernelL11_sobelEdgesEP10SamplerObjf
- __ZN8cikernelL11_wrapMirrorE4vec4
- __ZN8cikernelL12_DE_scaleAddE4vec4S0_f
- __ZN8cikernelL12_betterDown2EP10SamplerObj
- __ZN8cikernelL12_blendGrainsE4vec4f
- __ZN8cikernelL12_blurredrectE4vec4fS0_
- __ZN8cikernelL12_boostHybridE4vec4P10SamplerObjfff
- __ZN8cikernelL12_boxCombine2EP10SamplerObjS1_4vec4
- __ZN8cikernelL12_boxCombine3EP10SamplerObj4vec2
- __ZN8cikernelL12_boxCombine5EP10SamplerObj4vec2
- __ZN8cikernelL12_boxCombine7EP10SamplerObj4vec2
- __ZN8cikernelL12_ci_unpremulE4vec4
- __ZN8cikernelL12_cmyk_yellowE4vec4S0_4vec2S0_f
- __ZN8cikernelL12_colorcurvesE4vec4PKN2CI13BitmapSamplerE4vec2S5_
- __ZN8cikernelL12_crystallizeEP10SamplerObjS1_4vec2S2_
- __ZN8cikernelL12_drr_maxmaskE4vec4S0_
- __ZN8cikernelL12_exclusiveOrE4vec4S0_
- __ZN8cikernelL12_facebalanceE4vec44vec2
- __ZN8cikernelL12_finalResultE4vec4S0_
- __ZN8cikernelL12_fusionDeltaE4vec44vec3S1_f
- __ZN8cikernelL12_lighttunnelE4vec4
- __ZN8cikernelL12_lowq_affineE4vec2S0_S0_
- __ZN8cikernelL12_maskToAlphaE4vec4
- __ZN8cikernelL12_maxGradOnlyEP10SamplerObj
- __ZN8cikernelL12_paddedTile2E4vec4
- __ZN8cikernelL12_plusLighterE4vec4S0_
- __ZN8cikernelL12_pointillizeEP10SamplerObjS1_4vec4
- __ZN8cikernelL12_pq_inv_eotfE4vec4f
- __ZN8cikernelL12_resp_previsE4vec4S0_f
- __ZN8cikernelL12_roundedrectE4vec4fS0_
- __ZN8cikernelL12_shadowdesatE4vec4fff
- __ZN8cikernelL12_stretchcropE4vec2S0_4vec4
- __ZN8cikernelL12_swizzleXXX1E4vec4
- __ZN8cikernelL12_swizzleYYZ1E4vec4
- __ZN8cikernelL12_swizzleYZZ1E4vec4
- __ZN8cikernelL12_unsharpmaskE4vec4S0_f
- __ZN8cikernelL12_yccCombinerE4vec4S0_
- __ZN8cikernelL13_CBHorzGuidedEP10SamplerObjS1_fff
- __ZN8cikernelL13_CBVertGuidedEP10SamplerObjS1_fff
- __ZN8cikernelL13_PSDrawSpreadE4vec4f
- __ZN8cikernelL13_accordionMixE4vec4S0_4vec3fS0_
- __ZN8cikernelL13_ci_bgr10wideE4vec4
- __ZN8cikernelL13_ci_combine_aE4vec4S0_S0_S0_
- __ZN8cikernelL13_ci_combine_rE4vec4S0_S0_S0_
- __ZN8cikernelL13_ci_la_to_ll1E4vec4
- __ZN8cikernelL13_ci_la_to_rr1E4vec4
- __ZN8cikernelL13_ci_pass_thruE4vec4
- __ZN8cikernelL13_ci_rg_to_ll1E4vec4
- __ZN8cikernelL13_ci_rg_to_rr1E4vec4
- __ZN8cikernelL13_ci_rgb10wideE4vec4
- __ZN8cikernelL13_ci_srgb_noopE4vec4
- __ZN8cikernelL13_ci_to_10of16E4vec4
- __ZN8cikernelL13_circleSplashE4vec2f
- __ZN8cikernelL13_circularWrapE4vec2ffff
- __ZN8cikernelL13_cmcubeopaqueE4vec4PKN2CI13BitmapSamplerES0_
- __ZN8cikernelL13_cmyk_convertE4vec44vec2
- __ZN8cikernelL13_cmyk_magentaE4vec4S0_4vec2S0_f
- __ZN8cikernelL13_colorAbsDiffE4vec4S0_
- __ZN8cikernelL13_colorClampAPE4vec4S0_S0_
- __ZN8cikernelL13_colorbalanceE4vec4S0_S0_
- __ZN8cikernelL13_convolution3EP10SamplerObj4vec4S2_
- __ZN8cikernelL13_convolution5EP10SamplerObj4vec4S2_
- __ZN8cikernelL13_convolution7EP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL13_convolution9EP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL13_distanceMaskEP10SamplerObj4vec4f
- __ZN8cikernelL13_drr_binarizeE4vec4
- __ZN8cikernelL13_drr_multiplyE4vec4S0_
- __ZN8cikernelL13_drr_recoveryE4vec4S0_S0_S0_f
- __ZN8cikernelL13_drr_specularE4vec4
- __ZN8cikernelL13_fadeDissolveE4vec4f
- __ZN8cikernelL13_flexMapImageE4vec4ff
- __ZN8cikernelL13_glassDistortEP10SamplerObjS1_4vec2S2_S2_S2_S2_f
- __ZN8cikernelL13_guideCombineE4vec4S0_
- __ZN8cikernelL13_hlg_inv_oetfE4vec4f
- __ZN8cikernelL13_hlg_lumscaleE4vec4S0_4vec2
- __ZN8cikernelL13_holeFillPostE4vec4
- __ZN8cikernelL13_hueBlendModeE4vec4S0_
- __ZN8cikernelL13_invertedMaskE4vec4
- __ZN8cikernelL13_lanczosDown2EP10SamplerObj4vec4
- __ZN8cikernelL13_lanczosDownHEP10SamplerObj4vec4
- __ZN8cikernelL13_lanczosDownVEP10SamplerObj4vec4
- __ZN8cikernelL13_logHistogramE4vec4ff
- __ZN8cikernelL13_redThresholdE4vec4
- __ZN8cikernelL13_shadowKernelE4vec4S0_f
- __ZN8cikernelL13_thresholdRedE4vec4f
- __ZN8cikernelL13_triangleTileEP10SamplerObj4vec24vec4S3_
- __ZN8cikernelL13_vibrance_negE4vec4f
- __ZN8cikernelL13_vibrance_posE4vec4S0_
- __ZN8cikernelL14_CEcomp_minmaxE4vec4
- __ZN8cikernelL14_CIBoxBlur5MinEP10SamplerObj
- __ZN8cikernelL14_LAB_normalizeE4vec4
- __ZN8cikernelL14_RCFalloffDiskE4vec4S0_f
- __ZN8cikernelL14_blendWithMaskE4vec4S0_S0_
- __ZN8cikernelL14_ci_argb10wideE4vec4
- __ZN8cikernelL14_ci_clamp_rectE4vec4
- __ZN8cikernelL14_ci_combine_laE4vec4S0_
- __ZN8cikernelL14_ci_combine_rgE4vec4S0_
- __ZN8cikernelL14_ci_ycc_to_rgbE4vec4
- __ZN8cikernelL14_colorControlsE4vec4ff
- __ZN8cikernelL14_combineImagesE4vec4S0_
- __ZN8cikernelL14_convertRGBtoYE4vec4
- __ZN8cikernelL14_convrgb3x3symEP10SamplerObj4vec4
- __ZN8cikernelL14_cubicUpsampleEP10SamplerObj4vec24vec4S3_
- __ZN8cikernelL14_drr_cdmeasureE4vec4S0_
- __ZN8cikernelL14_drr_chromaexcE4vec4S0_fff
- __ZN8cikernelL14_drr_maximumRhE4vec4S0_
- __ZN8cikernelL14_drr_minimumRhE4vec4S0_
- __ZN8cikernelL14_drr_puncture2E4vec2ffS0_
- __ZN8cikernelL14_drr_rawred_smE4vec4ff
- __ZN8cikernelL14_drr_thresholdE4vec4S0_f
- __ZN8cikernelL14_gaussianBlur3EP10SamplerObj4vec4
- __ZN8cikernelL14_gaussianBlur5EP10SamplerObj4vec24vec4
- __ZN8cikernelL14_gaussianBlur7EP10SamplerObj4vec44vec2
- __ZN8cikernelL14_gaussianBlur9EP10SamplerObj4vec24vec4
- __ZN8cikernelL14_guideCombine4E4vec4S0_S0_
- __ZN8cikernelL14_hatchedscreenE4vec44vec3S0_
- __ZN8cikernelL14_headroomClampE4vec4f
- __ZN8cikernelL14_hlg_srmappingE4vec4S0_4vec2
- __ZN8cikernelL14_holeAntialiasE4vec44vec2f
- __ZN8cikernelL14_linearMappingE4vec4S0_f
- __ZN8cikernelL14_localContrastE4vec4S0_f
- __ZN8cikernelL14_maxScaleDown2EP10SamplerObj4vec2
- __ZN8cikernelL14_modTransitionE4vec4S0_4vec2S0_S0_S0_S0_
- __ZN8cikernelL14_perc_norm_redE4vec4S0_
- __ZN8cikernelL14_prepHistogramE4vec4f
- __ZN8cikernelL14_rawHighlightsE4vec4f
- __ZN8cikernelL14_roundedstrokeE4vec4ffS0_
- __ZN8cikernelL15_accordianWarpSE4vec34vec4
- __ZN8cikernelL15_accordianWarpTE4vec34vec4
- __ZN8cikernelL15_alphaNormalizeE4vec4
- __ZN8cikernelL15_areaMaxAlphaH4EP10SamplerObjff
- __ZN8cikernelL15_areaMaxAlphaS4EP10SamplerObj4vec2f
- __ZN8cikernelL15_areaMaxAlphaV4EP10SamplerObjff
- __ZN8cikernelL15_areaMinAlphaH4EP10SamplerObjff
- __ZN8cikernelL15_areaMinAlphaS4EP10SamplerObj4vec2f
- __ZN8cikernelL15_areaMinAlphaV4EP10SamplerObjff
- __ZN8cikernelL15_areaMinMaxRed4EP10SamplerObj4vec2f
- __ZN8cikernelL15_bumpDistortionE4vec4
- __ZN8cikernelL15_cannyThresholdE4vec4ff
- __ZN8cikernelL15_ci_colormatrixE4vec4S0_S0_S0_S0_S0_
- __ZN8cikernelL15_ci_combine_420E4vec4S0_S0_S0_
- __ZN8cikernelL15_ci_combine_422E4vec4S0_
- __ZN8cikernelL15_ci_combine_444E4vec4
- __ZN8cikernelL15_ci_combine_a16E4vec4S0_
- __ZN8cikernelL15_ci_combine_l16E4vec4S0_
- __ZN8cikernelL15_ci_combine_r16E4vec4S0_
- __ZN8cikernelL15_ci_lin_to_srgbE4vec4
- __ZN8cikernelL15_ci_srgb_to_linE4vec4
- __ZN8cikernelL15_ci_to_rgb_as_rE4vec4
- __ZN8cikernelL15_ci_writeTG_42XE4vec4S0_
- __ZN8cikernelL15_circularscreenE4vec4S0_
- __ZN8cikernelL15_colorBlendModeE4vec4S0_
- __ZN8cikernelL15_colorPosterizeE4vec44vec2
- __ZN8cikernelL15_colorThresholdE4vec4f
- __ZN8cikernelL15_convolution5x5EP10SamplerObj4vec4S2_S2_S2_S2_S2_S2_
- __ZN8cikernelL15_convolution7x7EP10SamplerObj4vec4S2_S2_S2_S2_S2_S2_S2_S2_S2_S2_S2_S2_
- __ZN8cikernelL15_drr_puncturec2E4vec4ff4vec2
- __ZN8cikernelL15_drr_spec_debugE4vec4S0_S0_fff
- __ZN8cikernelL15_flexMapLinGainE4vec4S0_ff
- __ZN8cikernelL15_gaussianBlur11EP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL15_gaussianBlur13EP10SamplerObj4vec24vec4S3_
- __ZN8cikernelL15_gaussianBlur15EP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL15_gaussianBlur19EP10SamplerObj4vec4S2_4vec2S2_S3_
- __ZN8cikernelL15_holeDistortionE4vec2f
- __ZN8cikernelL15_holeFillRefineEP10SamplerObjf
- __ZN8cikernelL15_jointBilateralEP10SamplerObjS1_4vec4
- __ZN8cikernelL15_lenticularHaloEP10SamplerObj4vec2S2_ffff4vec34vec4
- __ZN8cikernelL15_linearGradientE4vec2S0_4vec4S1_f
- __ZN8cikernelL15_maskBoundsInitE4vec44vec2
- __ZN8cikernelL15_maskBoundsPostE4vec4
- __ZN8cikernelL15_multiplyByMaskE4vec4S0_
- __ZN8cikernelL15_multiplyImagesE4vec4S0_
- __ZN8cikernelL15_noiseReductionEP10SamplerObj4vec24vec3S3_
- __ZN8cikernelL15_perc_accum_redEP10SamplerObjff
- __ZN8cikernelL15_perc_clip_hardE4vec4S0_
- __ZN8cikernelL15_perc_clip_softE4vec4S0_
- __ZN8cikernelL15_pq_tonemappingE4vec44vec24vec3S0_S1_S1_S0_
- __ZN8cikernelL15_radialGradientE4vec4S0_S0_
- __ZN8cikernelL15_shadedmaterialEP10SamplerObjS1_f4vec2
- __ZN8cikernelL15_shadows_noblurE4vec4S0_
- __ZN8cikernelL15_subtractImagesE4vec4S0_
- __ZN8cikernelL15_vertMinMaxRed4EP10SamplerObjff
- __ZN8cikernelL15_vignetteeffectE4vec44vec2S0_
- __ZN8cikernelL16_CIFaceMaskApplyEP10SamplerObj4vec4S2_S2_S2_fS1_4vec2S3_
- __ZN8cikernelL16_LAB_denormalizeE4vec4
- __ZN8cikernelL16_areaMinMaxRed16EP10SamplerObj4vec2f
- __ZN8cikernelL16_blendWithMaskB0E4vec4S0_
- __ZN8cikernelL16_cannyHysteresisEP10SamplerObj
- __ZN8cikernelL16_ci_combine_grayE4vec4S0_S0_S0_
- __ZN8cikernelL16_ci_rgba_to_llaaE4vec4
- __ZN8cikernelL16_ci_to_bgr10wideE4vec4
- __ZN8cikernelL16_ci_to_rgb10wideE4vec4
- __ZN8cikernelL16_colorMonochromeE4vec4S0_f
- __ZN8cikernelL16_colorPolynomialE4vec4S0_S0_S0_S0_
- __ZN8cikernelL16_colorcubeopaqueE4vec4PKN2CI13BitmapSamplerES0_
- __ZN8cikernelL16_convolutionrgb3EP10SamplerObj4vec4S2_
- __ZN8cikernelL16_convolutionrgb5EP10SamplerObj4vec4S2_
- __ZN8cikernelL16_convolutionrgb7EP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL16_convolutionrgb9EP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL16_cubicUpsample10EP10SamplerObj4vec2
- __ZN8cikernelL16_cubicUpsampleX0EP10SamplerObj4vec24vec4S3_
- __ZN8cikernelL16_darkenBlendModeE4vec4S0_
- __ZN8cikernelL16_distanceColoredEP10SamplerObj4vec2S2_
- __ZN8cikernelL16_divideBlendModeE4vec4S0_
- __ZN8cikernelL16_drr_cdintersectE4vec4S0_S0_f
- __ZN8cikernelL16_drr_maxScalarRhE4vec4f
- __ZN8cikernelL16_flexLumaScalingE4vec44vec2S0_fPKN2CI13BitmapSamplerES1_
- __ZN8cikernelL16_flexMapImageRGBE4vec4ff
- __ZN8cikernelL16_fusionTwoImagesE4vec4S0_4vec3S1_ff
- __ZN8cikernelL16_gaussianReduce2EP10SamplerObj4vec4
- __ZN8cikernelL16_gaussianReduce4EP10SamplerObj4vec4
- __ZN8cikernelL16_headroomToneMapE4vec4fffS0_
- __ZN8cikernelL16_horizMinMaxRed4EP10SamplerObjff
- __ZN8cikernelL16_hueBlendMode_v0E4vec4S0_
- __ZN8cikernelL16_maxScaleDown2x2EP10SamplerObj
- __ZN8cikernelL16_minMaxNormalizeE4vec4S0_S0_
- __ZN8cikernelL16_perc_denorm_redE4vec4S0_
- __ZN8cikernelL16_perspectiveMaskE4vec44vec3
- __ZN8cikernelL16_perspectiveWarpE4vec3S0_S0_
- __ZN8cikernelL16_screenBlendModeE4vec4S0_
- __ZN8cikernelL16_smartcolor_castE4vec4ffff
- __ZN8cikernelL16_swipeTransitionE4vec4S0_S0_S0_
- __ZN8cikernelL16_torusRefractionEP10SamplerObj4vec2fffff
- __ZN8cikernelL16_variableBoxBlurEP10SamplerObjS1_f4vec4
- __ZN8cikernelL17_CIBlurPreProcessE4vec4S0_
- __ZN8cikernelL17_CILensModelApplyE4vec4S0_
- __ZN8cikernelL17_DEnormalizeAlphaE4vec4
- __ZN8cikernelL17_appleLogToLinearE4vec4
- __ZN8cikernelL17_blendWithRedMaskE4vec4S0_S0_
- __ZN8cikernelL17_boostRGBLNoGammaE4vec4S0_S0_S0_S0_S0_f
- __ZN8cikernelL17_ciExtractChannelE4vec4f
- __ZN8cikernelL17_ci_rgba_to_rrgg1E4vec4
- __ZN8cikernelL17_ci_to_a16_as_rg8E4vec4
- __ZN8cikernelL17_ci_to_l10_as_r16E4vec4
- __ZN8cikernelL17_ci_to_l16_as_rg8E4vec4
- __ZN8cikernelL17_ci_to_r16_as_rg8E4vec4
- __ZN8cikernelL17_ci_writeSIMD_42XE4vec4S0_
- __ZN8cikernelL17_combineRGB_and_AE4vec4S0_
- __ZN8cikernelL17_convolutionAdd_1EP10SamplerObjS1_4vec2f
- __ZN8cikernelL17_convolutionAdd_2EP10SamplerObjS1_4vec2S2_S2_
- __ZN8cikernelL17_convolutionAdd_3EP10SamplerObjS1_4vec2S2_S2_4vec3
- __ZN8cikernelL17_convolutionAdd_4EP10SamplerObjS1_4vec4S2_S2_
- __ZN8cikernelL17_convolutionAdd_5EP10SamplerObjS1_4vec4S2_4vec2S2_f
- __ZN8cikernelL17_convolutionAdd_6EP10SamplerObjS1_4vec4S2_S2_S2_4vec2
- __ZN8cikernelL17_convolutionAdd_7EP10SamplerObjS1_4vec4S2_S2_4vec2S2_4vec3
- __ZN8cikernelL17_convolutionAdd_8EP10SamplerObjS1_4vec4S2_S2_S2_S2_S2_
- __ZN8cikernelL17_cubicDownsample2EP10SamplerObj4vec4
- __ZN8cikernelL17_cubicDownsampleHEP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL17_cubicDownsampleVEP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL17_cubicUpsample10hEP10SamplerObjf
- __ZN8cikernelL17_cubicUpsample10vEP10SamplerObjf
- __ZN8cikernelL17_distanceMaskPostE4vec4S0_S0_f
- __ZN8cikernelL17_distanceMaskPrepE4vec4S0_
- __ZN8cikernelL17_drr_binarize_invE4vec4
- __ZN8cikernelL17_drr_combine_rgbaE4vec4S0_S0_S0_
- __ZN8cikernelL17_drr_detect_specsE4vec4S0_ff
- __ZN8cikernelL17_drr_extract_irisE4vec4S0_S0_fff
- __ZN8cikernelL17_drr_extract_skinE4vec4f
- __ZN8cikernelL17_drr_rawred_largeE4vec4ff
- __ZN8cikernelL17_drr_smoothstepRhE4vec4f
- __ZN8cikernelL17_edgeWorkContrastE4vec4f
- __ZN8cikernelL17_gaussianGradientE4vec34vec4S1_
- __ZN8cikernelL17_grainBlendAndMixE4vec4S0_ff
- __ZN8cikernelL17_hardMixBlendModeE4vec4S0_
- __ZN8cikernelL17_hsvwheelditheredE4vec4f
- __ZN8cikernelL17_jointBilateralRGEP10SamplerObj4vec4
- __ZN8cikernelL17_lightenBlendModeE4vec4S0_
- __ZN8cikernelL17_linearToAppleLogE4vec4
- __ZN8cikernelL17_maskBoundsReduceEP10SamplerObj
- __ZN8cikernelL17_maximumComponentE4vec4
- __ZN8cikernelL17_minimumComponentE4vec4
- __ZN8cikernelL17_ninePartTiledAltE4vec44vec2S1_
- __ZN8cikernelL17_outerBevelEmbossEP10SamplerObj4vec2
- __ZN8cikernelL17_overlayBlendModeE4vec4S0_
- __ZN8cikernelL17_rippleTransitionEP10SamplerObjS1_S1_4vec24vec4S2_
- __ZN8cikernelL17_shadedmaterial_0EP10SamplerObjS1_4vec2
- __ZN8cikernelL17_sharpenLuminanceE4vec4S0_f
- __ZN8cikernelL17_vortexDistortionE4vec2S0_
- __ZN8cikernelL17_whitepointadjustE4vec4S0_
- __ZN8cikernelL18_CIPortraitBlurDirEP10SamplerObj4vec3
- __ZN8cikernelL18_CISmoothDisparityEP10SamplerObj4vec3
- __ZN8cikernelL18_RCFalloffGaussianE4vec4S0_f
- __ZN8cikernelL18_blendWithBlueMaskE4vec4S0_S0_
- __ZN8cikernelL18_ci_clamp_to_alphaE4vec4
- __ZN8cikernelL18_ci_colormatrix3x1E4vec44vec3
- __ZN8cikernelL18_ci_colormatrix3x3E4vec44vec3S1_S1_
- __ZN8cikernelL18_ci_colormatrix3x4E4vec4S0_S0_S0_
- __ZN8cikernelL18_ci_swizzle_to_4XXE4vec4
- __ZN8cikernelL18_colorBlendMode_v0E4vec4S0_
- __ZN8cikernelL18_convolutionrgb5x5EP10SamplerObj4vec4S2_S2_S2_S2_S2_S2_
- __ZN8cikernelL18_convolutionrgb7x7EP10SamplerObj4vec4S2_S2_S2_S2_S2_S2_S2_S2_S2_S2_S2_S2_
- __ZN8cikernelL18_cubicDownsample2hEP10SamplerObj4vec4
- __ZN8cikernelL18_cubicDownsample2vEP10SamplerObj4vec4
- __ZN8cikernelL18_cui_hueSaturationE4vec4fffff
- __ZN8cikernelL18_displaceFromImageEP10SamplerObjS1_f
- __ZN8cikernelL18_drr_refilter_chanE4vec4
- __ZN8cikernelL18_flexMapLinGainRGBE4vec4S0_ff
- __ZN8cikernelL18_gradientDirectionE4vec4
- __ZN8cikernelL18_gradientMagnitudeE4vec4
- __ZN8cikernelL18_grassAndSkyAdjustE4vec44vec2
- __ZN8cikernelL18_histogram_displayEP10SamplerObjf4vec2
- __ZN8cikernelL18_lozengeRefractionEP10SamplerObj4vec2S2_fS2_S2_ff
- __ZN8cikernelL18_multiplyBlendModeE4vec4S0_
- __ZN8cikernelL18_ninePartStretchedE4vec2S0_S0_
- __ZN8cikernelL18_outerBevelEmbossCE4vec4S0_S0_
- __ZN8cikernelL18_parallelogramTileE4vec24vec4S1_
- __ZN8cikernelL18_pinLightBlendModeE4vec4S0_
- __ZN8cikernelL18_shapeEffectBlur_1E4vec4S0_S0_S0_S0_S0_S0_S0_S0_4vec2
- __ZN8cikernelL18_subtractBlendModeE4vec4S0_
- __ZN8cikernelL18_vignetteeffectnegE4vec44vec2S0_
- __ZN8cikernelL19_blendWithAlphaMaskE4vec4S0_S0_
- __ZN8cikernelL19_blendWithRedMaskB0E4vec4S0_
- __ZN8cikernelL19_ci_bgr10widelinearE4vec4
- __ZN8cikernelL19_ci_colormatrixdiagE4vec44vec3
- __ZN8cikernelL19_ci_rgb10widelinearE4vec4
- __ZN8cikernelL19_ci_swizzle_to_laaaE4vec4
- __ZN8cikernelL19_colorBurnBlendModeE4vec4S0_
- __ZN8cikernelL19_colorPolynomialRGBE4vec4S0_S0_S0_S0_
- __ZN8cikernelL19_drr_binarize_alphaE4vec4S0_f
- __ZN8cikernelL19_drr_puncture2_hardE4vec2ffS0_
- __ZN8cikernelL19_exclusionBlendModeE4vec4S0_
- __ZN8cikernelL19_faceMaskCalculatorEP10SamplerObj4vec4S2_S2_S2_S2_S2_S2_S2_S2_S2_S2_S2_S2_
- __ZN8cikernelL19_glideReflectedTileE4vec24vec4S1_
- __ZN8cikernelL19_gradientRangeLimitE4vec4ffff
- __ZN8cikernelL19_hardLightBlendModeE4vec4S0_
- __ZN8cikernelL19_hexagonalPixellateEP10SamplerObj4vec2S2_S2_f
- __ZN8cikernelL19_maskedVariableBlurEP10SamplerObjS1_S1_S1_S1_S1_S1_S1_f
- __ZN8cikernelL19_minMaxRedNormalizeE4vec4S0_
- __ZN8cikernelL19_pageCurlTransitionEP10SamplerObjS1_S1_4vec44vec2S2_S3_S2_S3_fS2_
- __ZN8cikernelL19_prepHoughTransformE4vec4fff
- __ZN8cikernelL19_segmentationFusionE4vec4S0_4vec3S1_
- __ZN8cikernelL19_sixfoldRotatedTileE4vec24vec4S1_
- __ZN8cikernelL19_smartBlackAndWhiteE4vec4PKN2CI13BitmapSamplerES0_S0_
- __ZN8cikernelL19_smarttone_contrastE4vec4f
- __ZN8cikernelL19_softLightBlendModeE4vec4S0_
- __ZN8cikernelL20_DEconditionalFilterE4vec4S0_S0_f
- __ZN8cikernelL20_RCSelectGreaterThanE4vec4S0_S0_f
- __ZN8cikernelL20_blendWithBlueMaskB0E4vec4S0_
- __ZN8cikernelL20_ci_colormatrix_rrraE4vec4
- __ZN8cikernelL20_ci_colormatrixdiag4E4vec4S0_
- __ZN8cikernelL20_ci_to_CbYCrY_as_rg8E4vec4
- __ZN8cikernelL20_ci_to_YCbYCr_as_rg8E4vec4
- __ZN8cikernelL20_ci_to_la16_as_bgra8E4vec4
- __ZN8cikernelL20_ci_to_la16_as_rgba8E4vec4
- __ZN8cikernelL20_ci_to_rg16_as_bgra8E4vec4
- __ZN8cikernelL20_ci_to_rg16_as_rgba8E4vec4
- __ZN8cikernelL20_colorDodgeBlendModeE4vec4S0_
- __ZN8cikernelL20_differenceBlendModeE4vec4S0_
- __ZN8cikernelL20_drr_puncturec2_hardE4vec4ff4vec2
- __ZN8cikernelL20_fourfoldRotatedTileE4vec24vec4S1_
- __ZN8cikernelL20_gradientNormalizeV1E4vec4f
- __ZN8cikernelL20_gradientNormalizeV2E4vec4S0_
- __ZN8cikernelL20_gradientThresholdV1E4vec4ff
- __ZN8cikernelL20_gradientThresholdV2E4vec4ff
- __ZN8cikernelL20_linearBurnBlendModeE4vec4S0_
- __ZN8cikernelL20_luminosityBlendModeE4vec4S0_
- __ZN8cikernelL20_noiseComicReductionEP10SamplerObj4vec24vec3S3_
- __ZN8cikernelL20_pageCurlTransNoEmapEP10SamplerObjS1_4vec44vec2S2_S3_S2_S3_f
- __ZN8cikernelL20_reduceCropMinMaxRedEP10SamplerObj
- __ZN8cikernelL20_saturationBlendModeE4vec4S0_
- __ZN8cikernelL20_sharpenCombineEdgesE4vec4S0_4vec3S0_
- __ZN8cikernelL20_smartcolor_contrastE4vec4f
- __ZN8cikernelL20_vividLightBlendModeE4vec4S0_
- __ZN8cikernelL21_CIAreaHistogramScaleE4vec4f
- __ZN8cikernelL21_blendWithAlphaMaskB0E4vec4S0_
- __ZN8cikernelL21_bumpDistortionLinearE4vec4S0_
- __ZN8cikernelL21_ci_to_rgb10_as_rgba8E4vec4
- __ZN8cikernelL21_colorCrossPolynomialE4vec44vec3S1_S1_S1_S1_S1_S1_S1_S1_S1_
- __ZN8cikernelL21_darkerColorBlendModeE4vec4S0_
- __ZN8cikernelL21_disintegrateWithMaskE4vec4S0_S0_S0_S0_S0_S0_
- __ZN8cikernelL21_interleavedToPlanar3EP10SamplerObjf
- __ZN8cikernelL21_interleavedToPlanar4EP10SamplerObjf
- __ZN8cikernelL21_linearDodgeBlendModeE4vec4S0_
- __ZN8cikernelL21_linearLightBlendModeE4vec4S0_
- __ZN8cikernelL21_perspectiveTransformE4vec3S0_S0_4vec2
- __ZN8cikernelL21_planarToInterleaved3EP10SamplerObjf
- __ZN8cikernelL21_planarToInterleaved4EP10SamplerObjf
- __ZN8cikernelL21_radialLensDistortionEP10SamplerObjS1_4vec4
- __ZN8cikernelL21_sixfoldReflectedTileE4vec24vec4S1_
- __ZN8cikernelL21_smoothLinearGradientE4vec2S0_4vec4S1_f
- __ZN8cikernelL22_ciLensModelCalculatorEP10SamplerObj4vec4S1_S2_
- __ZN8cikernelL22_ci_to_bgr10widelinearE4vec4
- __ZN8cikernelL22_ci_to_rgb10widelinearE4vec4
- __ZN8cikernelL22_copyMachineTransitionE4vec4S0_4vec3S0_S0_S1_
- __ZN8cikernelL22_disintegrateWithMaskGEP10SamplerObjS1_S1_4vec24vec4
- __ZN8cikernelL22_drr_conditionalZeroRhE4vec4S0_f
- __ZN8cikernelL22_fourfoldReflectedTileE4vec24vec4S1_
- __ZN8cikernelL22_highlightsAndShadows0E4vec4S0_S0_
- __ZN8cikernelL22_highlightsAndShadows1E4vec4S0_S0_
- __ZN8cikernelL22_highlightsAndShadows2E4vec4S0_S0_
- __ZN8cikernelL22_lighterColorBlendModeE4vec4S0_
- __ZN8cikernelL22_perspectiveCorrectionE4vec3S0_S0_
- __ZN8cikernelL22_photoEffectDepthBlendE4vec4S0_S0_f
- __ZN8cikernelL23_ACWeightedCoordinatesRE4vec4S0_
- __ZN8cikernelL23_CIInitialConversionRGBEP10SamplerObj4vec2
- __ZN8cikernelL23_CIPyramidGenerateLevelEP10SamplerObj
- __ZN8cikernelL23_DEcomputeInversionMaskE4vec4S0_ff
- __ZN8cikernelL23_DEcreateForegroundMaskE4vec4S0_S0_S0_
- __ZN8cikernelL23_ci_to_a2bgr10_as_rgba8E4vec4
- __ZN8cikernelL23_ci_to_a2rgb10_as_rgba8E4vec4
- __ZN8cikernelL23_colorPolynomialInverseE4vec4S0_S0_S0_S0_
- __ZN8cikernelL23_colorcubeopaque_extendE4vec4PKN2CI13BitmapSamplerES0_
- __ZN8cikernelL23_drr_binarize_alpha_invE4vec4S0_f
- __ZN8cikernelL23_eightfoldReflectedTileE4vec24vec4S1_
- __ZN8cikernelL23_fourfoldTranslatedTileE4vec24vec4S1_
- __ZN8cikernelL23_linearBurnBlendMode_v0E4vec4S0_
- __ZN8cikernelL23_luminosityBlendMode_v0E4vec4S0_
- __ZN8cikernelL23_saturationBlendMode_v0E4vec4S0_
- __ZN8cikernelL24_accordionFoldTransitionEP10SamplerObjS1_4vec3f4vec4
- __ZN8cikernelL24_ciSingleChannelColorMapEP10SamplerObjS1_
- __ZN8cikernelL24_ci_clamp_to_zero_to_oneE4vec4
- __ZN8cikernelL24_convertDepthOrDisparityE4vec4
- __ZN8cikernelL24_convertUsingColorMatrixE4vec4S0_S0_S0_
- __ZN8cikernelL24_pinchDistortionScaleGE1E4vec24vec4
- __ZN8cikernelL24_pinchDistortionScaleLT1E4vec24vec4
- __ZN8cikernelL24_smartcolor_vibrancy_gt1E4vec4f
- __ZN8cikernelL24_smartcolor_vibrancy_lt1E4vec4f
- __ZN8cikernelL24_twelvefoldReflectedTileE4vec24vec4S1_
- __ZN8cikernelL25_ci_colormatrix_canonicalE4vec4S0_S0_S0_
- __ZN8cikernelL25_ci_to_rgb10wide_as_rgba8E4vec4
- __ZN8cikernelL25_smarttone_brightness_negE4vec4f
- __ZN8cikernelL25_smarttone_brightness_posE4vec4f
- __ZN8cikernelL25_triangleKaleidoscopeGeomE4vec24vec4S1_
- __ZN8cikernelL26_ci_swizzle_rgba8_to_rgb10E4vec4
- __ZN8cikernelL26_colorPolynomialInverseRGBE4vec4S0_S0_S0_S0_
- __ZN8cikernelL26_sparserendering_add_noiseE4vec4S0_4vec2
- __ZN8cikernelL26_triangleKaleidoscopeColorE4vec44vec2S0_f
- __ZN8cikernelL27_ci_to_argb10wide_as_rgba16E4vec4
- __ZN8cikernelL27_pageCurlNoShadowTransitionEP10SamplerObjS1_4vec44vec2S2_S3_S2_S3_fS2_S2_
- __ZN8cikernelL27_smartcolor_contrast_darkenE4vec4f
- __ZN8cikernelL28_ci_swizzle_rgba8_to_a2bgr10E4vec4
- __ZN8cikernelL28_ci_swizzle_rgba8_to_a2rgb10E4vec4
- __ZN8cikernelL28_smarttone_highlightcontrastE4vec4ff
- __ZN8cikernelL29_CIAreaHistogramScaleAndClampE4vec4ff
- __ZN8cikernelL29_highlightsAndShadows_noblur0E4vec4S0_
- __ZN8cikernelL29_highlightsAndShadows_noblur1E4vec4S0_
- __ZN8cikernelL29_highlightsAndShadows_noblur2E4vec4S0_
- __ZN8cikernelL29_pageCurlWithShadowTransitionEP10SamplerObjS1_4vec44vec2S2_S3_S2_S3_fS2_ffS2_S2_
- __ZN8cikernelL30_linearMappingNoSecondaryImageE4vec4f
- __ZN8cikernelL31_ci_swizzle_rgba8_to_rgb10_wideE4vec4
- __ZN8cikernelL31_ci_to_rgb10widelinear_as_rgba8E4vec4
- __ZN8cikernelL33_disparityRefinementPreprocessingE4vec4S0_S0_S0_S0_
- __ZN8cikernelL36_ci_swizzle_rgba8_to_rgb10widelinearE4vec4
- __ZN8cikernelL37_CIPortraitBlurBlendWithMaskFromAlphaE4vec4S0_S0_
- __ZN8cikernelL37_disparityRefinementPreprocessingPow2E4vec4S0_S0_S0_S0_
- __ZN8cikernelL42_CIPortraitBlurBlendWithMaskMatteFromAlphaE4vec4S0_S0_S0_
- __ZN8cikernelL45_CIPortraitBlurBlendWithMaskMatteFromAlphaYCCE4vec4S0_S0_S0_f
- __ZN8cikernelL4_addE4vec4S0_
- __ZN8cikernelL4_dstE4vec4S0_
- __ZN8cikernelL4_maxE4vec4S0_
- __ZN8cikernelL4_minE4vec4S0_
- __ZN8cikernelL4_mixE4vec4S0_f
- __ZN8cikernelL4_srcE4vec4S0_
- __ZN8cikernelL5_add4EP10SamplerObjS1_4vec2S2_
- __ZN8cikernelL5_add8EP10SamplerObjS1_4vec2S2_
- __ZN8cikernelL5_box3EP10SamplerObjf
- __ZN8cikernelL5_box4EP10SamplerObj
- __ZN8cikernelL5_box6EP10SamplerObj
- __ZN8cikernelL5_grayE4vec4
- __ZN8cikernelL5_lerpE4vec4S0_f
- __ZN8cikernelL5_otsuEP10SamplerObjf
- __ZN8cikernelL5_tileE4vec24vec4
- __ZN8cikernelL5_zoomEP10SamplerObj4vec2f
- __ZN8cikernelL6_bloomE4vec4S0_f
- __ZN8cikernelL6_blur1EP10SamplerObj
- __ZN8cikernelL6_blur2EP10SamplerObj
- __ZN8cikernelL6_blur4EP10SamplerObj
- __ZN8cikernelL6_clearE4vec4S0_
- __ZN8cikernelL6_cmlutE4vec4PKN2CI13BitmapSamplerE4vec2
- __ZN8cikernelL6_drr_aE4vec4
- __ZN8cikernelL6_drr_bE4vec4
- __ZN8cikernelL6_drr_gE4vec4
- __ZN8cikernelL6_drr_rE4vec4
- __ZN8cikernelL6_dstInE4vec4S0_
- __ZN8cikernelL6_edgesEP10SamplerObjf
- __ZN8cikernelL6_gaborEP10SamplerObj
- __ZN8cikernelL6_gloomE4vec4S0_f
- __ZN8cikernelL6_mesh1E4vec4fS0_f
- __ZN8cikernelL6_mesh2E4vec4S0_fS0_f
- __ZN8cikernelL6_mesh4E4vec4S0_S0_S0_fS0_f
- __ZN8cikernelL6_mesh8E4vec4S0_S0_S0_S0_S0_S0_S0_fS0_f
- __ZN8cikernelL6_sepiaE4vec4f
- __ZN8cikernelL6_sobelEP10SamplerObj
- __ZN8cikernelL6_srcInE4vec4S0_
- __ZN8cikernelL6_twirlE4vec4
- __ZN8cikernelL6_whiteE4vec4
- __ZN8cikernelL7_ASGh50EP10SamplerObj
- __ZN8cikernelL7_ASGh60EP10SamplerObj
- __ZN8cikernelL7_ASGh66EP10SamplerObj
- __ZN8cikernelL7_ASGh80EP10SamplerObj
- __ZN8cikernelL7_ASGv50EP10SamplerObj
- __ZN8cikernelL7_ASGv60EP10SamplerObj
- __ZN8cikernelL7_ASGv66EP10SamplerObj
- __ZN8cikernelL7_ASGv75EP10SamplerObj
- __ZN8cikernelL7_ASGv80EP10SamplerObj
- __ZN8cikernelL7_CBHorzEP10SamplerObjfff
- __ZN8cikernelL7_CBVertEP10SamplerObjfff
- __ZN8cikernelL7_DEWashE4vec4S0_
- __ZN8cikernelL7_DE_subE4vec4S0_
- __ZN8cikernelL7_DEmax4EP10SamplerObj4vec2
- __ZN8cikernelL7_ci_l10E4vec4
- __ZN8cikernelL7_ci_sqrE4vec4
- __ZN8cikernelL7_circleE4vec4S0_
- __ZN8cikernelL7_cross4EP10SamplerObjf
- __ZN8cikernelL7_drosteE4vec2S0_fS0_S0_
- __ZN8cikernelL7_dstOutE4vec4S0_
- __ZN8cikernelL7_max3x3EP10SamplerObj4vec4
- __ZN8cikernelL7_mesh16E4vec4S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_fS0_f
- __ZN8cikernelL7_mesh32E4vec4S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_S0_fS0_f
- __ZN8cikernelL7_min3x3EP10SamplerObj4vec4
- __ZN8cikernelL7_mirrorE4vec24vec34vec4S2_
- __ZN8cikernelL7_opTileEP10SamplerObj4vec2S2_4vec4
- __ZN8cikernelL7_srcOutE4vec4S0_
- __ZN8cikernelL8_averageE4vec4S0_f
- __ZN8cikernelL8_checkerE4vec24vec4S1_4vec3
- __ZN8cikernelL8_ci_000rE4vec4
- __ZN8cikernelL8_ci_1bgrE4vec4
- __ZN8cikernelL8_ci_1rgbE4vec4
- __ZN8cikernelL8_ci_a001E4vec4
- __ZN8cikernelL8_ci_aaa1E4vec4
- __ZN8cikernelL8_ci_aaaaE4vec4
- __ZN8cikernelL8_ci_abg1E4vec4
- __ZN8cikernelL8_ci_abgrE4vec4
- __ZN8cikernelL8_ci_arg1E4vec4
- __ZN8cikernelL8_ci_argbE4vec4
- __ZN8cikernelL8_ci_bgr1E4vec4
- __ZN8cikernelL8_ci_bgraE4vec4
- __ZN8cikernelL8_ci_cropE4vec4S0_
- __ZN8cikernelL8_ci_curvE4vec4S0_4vec3
- __ZN8cikernelL8_ci_fillE4vec4
- __ZN8cikernelL8_ci_gb1rE4vec4
- __ZN8cikernelL8_ci_gba1E4vec4
- __ZN8cikernelL8_ci_gbarE4vec4
- __ZN8cikernelL8_ci_gbraE4vec4
- __ZN8cikernelL8_ci_gr1bE4vec4
- __ZN8cikernelL8_ci_gra1E4vec4
- __ZN8cikernelL8_ci_grabE4vec4
- __ZN8cikernelL8_ci_pow4E4vec4
- __ZN8cikernelL8_ci_r001E4vec4
- __ZN8cikernelL8_ci_ra01E4vec4
- __ZN8cikernelL8_ci_rg01E4vec4
- __ZN8cikernelL8_ci_rgb1E4vec4
- __ZN8cikernelL8_ci_rrr1E4vec4
- __ZN8cikernelL8_ci_rrrgE4vec4
- __ZN8cikernelL8_ci_rrrrE4vec4
- __ZN8cikernelL8_ci_sqrtE4vec4
- __ZN8cikernelL8_clearerEv
- __ZN8cikernelL8_conv3x3EP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL8_dditherE4vec4S0_f
- __ZN8cikernelL8_disolveE4vec4S0_f
- __ZN8cikernelL8_drr_mmiE4vec44vec2S1_fffff
- __ZN8cikernelL8_drr_mmvE4vec2S0_S0_fffff
- __ZN8cikernelL8_dstAtopE4vec4S0_
- __ZN8cikernelL8_dstOverE4vec4S0_
- __ZN8cikernelL8_flexMapE4vec4S0_4vec3S1_S1_fS1_S1_
- __ZN8cikernelL8_gainMapE4vec4S0_f
- __ZN8cikernelL8_kaleidaE4vec4S0_S0_
- __ZN8cikernelL8_lumaMapE4vec4PKN2CI13BitmapSamplerE4vec2
- __ZN8cikernelL8_maxDiskEP10SamplerObjf
- __ZN8cikernelL8_minDiskEP10SamplerObjf
- __ZN8cikernelL8_onlyRG_E4vec4
- __ZN8cikernelL8_pq_eotfE4vec4f
- __ZN8cikernelL8_sobel_mEP10SamplerObj
- __ZN8cikernelL8_srcAtopE4vec4S0_
- __ZN8cikernelL8_srcOverE4vec4S0_
- __ZN8cikernelL8_stretchE4vec24vec3
- __ZN8cikernelL8_stripesE4vec24vec4S1_4vec3
- __ZN8cikernelL8_xSmoothEP10SamplerObj
- __ZN8cikernelL8_ySmoothEP10SamplerObjS1_4vec4
- __ZN8cikernelL9_LABtoRGBE4vec4
- __ZN8cikernelL9_PC_coordEP10SamplerObjS1_ff
- __ZN8cikernelL9_RCCenterE4vec2
- __ZN8cikernelL9_RGBtoLABE4vec4
- __ZN8cikernelL9_add4and4EP10SamplerObjS1_4vec4S2_
- __ZN8cikernelL9_add4and8EP10SamplerObjS1_4vec4S2_
- __ZN8cikernelL9_add8and8EP10SamplerObjS1_4vec4S2_
- __ZN8cikernelL9_areaAvg2EP10SamplerObj
- __ZN8cikernelL9_areaAvg4EP10SamplerObj
- __ZN8cikernelL9_areaAvg8EP10SamplerObj
- __ZN8cikernelL9_areaMax4EP10SamplerObj4vec2f
- __ZN8cikernelL9_areaMin4EP10SamplerObj4vec2f
- __ZN8cikernelL9_asgDownHEP10SamplerObj4vec4f
- __ZN8cikernelL9_asgDownVEP10SamplerObj4vec4f
- __ZN8cikernelL9_boostRGBE4vec4S0_S0_S0_S0_S0_f
- __ZN8cikernelL9_boxBlur3EP10SamplerObj4vec2
- __ZN8cikernelL9_boxBlur5EP10SamplerObj4vec2
- __ZN8cikernelL9_boxBlur7EP10SamplerObj4vec2
- __ZN8cikernelL9_boxBlur9EP10SamplerObj4vec2
- __ZN8cikernelL9_ci_gammaE4vec4f
- __ZN8cikernelL9_cm1x3lutE4vec4PKN2CI13BitmapSamplerE4vec2
- __ZN8cikernelL9_colorMapEP10SamplerObjS1_f
- __ZN8cikernelL9_downhalfEP10SamplerObj
- __ZN8cikernelL9_drr_specE4vec4S0_S0_fff
- __ZN8cikernelL9_edgeWorkE4vec4S0_
- __ZN8cikernelL9_gradientE4vec4S0_
- __ZN8cikernelL9_hlg_oetfE4vec4f
- __ZN8cikernelL9_hsvwheelE4vec4
- __ZN8cikernelL9_maxScaleEP10SamplerObj4vec4
- __ZN8cikernelL9_morphmaxEP10SamplerObjf4vec2
- __ZN8cikernelL9_morphminEP10SamplerObjf4vec2
- __ZN8cikernelL9_multiplyE4vec4S0_
- __ZN8cikernelL9_ringAvg8EP10SamplerObj4vec4
- __ZN8cikernelL9_sunbeamsEP10SamplerObj4vec4S2_S2_
- __ZN8cikernelL9_vertAvg2EP10SamplerObj
- __ZN8cikernelL9_vertAvg4EP10SamplerObj
- __ZN8cikernelL9_vertAvg8EP10SamplerObj
- __ZN8cikernelL9_vertMax4EP10SamplerObjff
- __ZN8cikernelL9_vertMin4EP10SamplerObjff
- __ZN8cikernelL9_vignetteE4vec4S0_
- __ZN8cikernelL9_zoomBlurEP10SamplerObj4vec24vec4S3_f
- __ZNK2CI11ConvertNode6renderEPNS_8TileTaskEPNS_7ContextERKNSt3__16vectorIPKNS_14intermediate_tENS5_9allocatorIS9_EEEEP11__IOSurfaceNS_7TextureERK6CGRecti
- __ZNK2CI11ConvertNode6renderEPNS_8TileTaskEPNS_7ContextERKNSt3__16vectorIPKNS_14intermediate_tENS5_9allocatorIS9_EEEEP11__IOSurfaceNS_7TextureERK6CGRecti.cold.1
- __ZNK2CI11MetalKernel41useMTLFunctionBitCodeHashForProgramDigestEv
- __ZNK2CI12MetalContext8SWShadowEv
- __ZNK2CI13ProcessorNode6renderEPNS_8TileTaskEPNS_7ContextERKNSt3__16vectorIPKNS_14intermediate_tENS5_9allocatorIS9_EEEEP11__IOSurfaceNS_7TextureERK6CGRecti
- __ZNK2CI13SetPropsImage10colorspaceEv
- __ZNK2CI13SetPropsImage12roi_of_childE6CGRecti
- __ZNK2CI13SetPropsImage13output_formatEv
- __ZNK2CI13SetPropsImage17render_graph_coreEPNS_7ContextEPNS_4NodeERKNSt3__13mapINS_11ImageDigestE6CGRectNS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEEi
- __ZNK2CI13SetPropsImage18color_for_graphvizEv
- __ZNK2CI13SetPropsImage18shape_for_graphvizEv
- __ZNK2CI13SetPropsImage8headroomEv
- __ZNK2CI14ProcessorImage17render_graph_coreEPNS_7ContextERNS_14ImageToNodeMapERKNSt3__13mapINS_11ImageDigestE6CGRectNS5_4lessIS7_EENS5_9allocatorINS5_4pairIKS7_S8_EEEEEEi.cold.2
- __ZNK2CI15InstanceCountedILNS_4TypeE18EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE30EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE31EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE46EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE47EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE48EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE49EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE59EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE67EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE68EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE71EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE75EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE76EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE78EE4typeEv
- __ZNK2CI15InstanceCountedILNS_4TypeE85EE4typeEv
- __ZNK2CI16ColorKernelImage5childEiRb
- __ZNK2CI18GeneralKernelImage19child_type_is_imageEi
- __ZNK2CI6Kernel20num_sample_argumentsEv
- __ZNK2CI6Kernel27index_of_nth_image_argumentEi
- __ZNK2CI6Kernel29index_of_first_image_argumentEv
- __ZNK2CI7Context19swizzler_for_outputENS_11PixelFormatENS_15DestinationTypeE
- __ZNK2CI7Context30format_is_supported_for_outputENS_11PixelFormatENS_15DestinationTypeE
- __ZNK2CI8MetalDAG13get_type_nameEv
- __ZNK2CI8MetalDAG13print_programEP7__sFILE
- __ZNK2CI8MetalDAG4typeEv
- __ZNK2CI8NoopNode16regions_of_childE6CGRecti
- __ZNK2CI9NoopImage15region_of_childE6CGRecti
- __ZNK4vec28get_xyxyEv
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8nn190102INS_21__tree_const_iteratorIdPNS_11__tree_nodeIdPvEElEES9_NS_20back_insert_iteratorINS_6vectorIdNS_9allocatorIdEEEEEEEENS_4pairIT_T1_EESH_T0_SI_
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8nn190102IPN2CI15SerialRectArray7roiDataES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__111__copy_implINS_17_ClassicAlgPolicyEEclB8nn190102IPNS_6vectorI5IRectNS_9allocatorIS5_EEEES9_S9_EENS_4pairIT_T1_EESB_T0_SC_
- __ZNKSt3__111__move_implINS_17_ClassicAlgPolicyEEclB8nn190102IPN2CI15SerialRectArray7roiDataES7_S7_EENS_4pairIT_T1_EES9_T0_SA_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE3strB8nn190102IS4_EENS_12basic_stringIcS2_T_EERKS8_
- __ZNKSt3__115basic_stringbufIcNS_11char_traitsIcEENS_9allocatorIcEEE4viewB8nn190102Ev
- __ZNSt3__110unique_ptrIN2CI14intermediate_tENS_14default_deleteIS2_EEED1B8nn190102Ev
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIyN2CI14MetalDAGHelper19TextureReadFunctionEEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8nn190102EPS8_
- __ZNSt3__110unique_ptrINS_11__tree_nodeINS_12__value_typeIyN2CI9DAGHelper19TextureReadFunctionEEEPvEENS_22__tree_node_destructorINS_9allocatorIS8_EEEEE5resetB8nn190102EPS8_
- __ZNSt3__111__sift_downB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_OT0_NS_15iterator_traitsISD_E15difference_typeESD_
- __ZNSt3__111__sift_downB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_OT0_NS_15iterator_traitsISD_E15difference_typeESD_
- __ZNSt3__111__sift_downB8nn190102INS_17_ClassicAlgPolicyERZZ46-[CIPerspectiveAutoCalcV1 clusterLineSegments]ENK3$_0clERKNS_6vectorIN2CI11Perspective4LineENS_9allocatorIS6_EEEEmEUlRKZ46-[CIPerspectiveAutoCalcV1 clusterLineSegments]E10HypothesisSE_E_NS_11__wrap_iterIPSC_EEEEvT1_OT0_NS_15iterator_traitsISK_E15difference_typeESK_
- __ZNSt3__111__sift_downB8nn190102INS_17_ClassicAlgPolicyERZZ46-[CIPerspectiveAutoCalcV2 clusterLineSegments]ENK3$_0clERKNS_6vectorIN2CI11Perspective4LineENS_9allocatorIS6_EEEEmEUlRKZ46-[CIPerspectiveAutoCalcV2 clusterLineSegments]E10HypothesisSE_E_NS_11__wrap_iterIPSC_EEEEvT1_OT0_NS_15iterator_traitsISK_E15difference_typeESK_
- __ZNSt3__112__destroy_atB8nn190102IN2CI15SerialRectArray7roiDataELi0EEEvPT_
- __ZNSt3__112__destroy_atB8nn190102INS_4pairIKyN2CI14MetalDAGHelper19TextureReadFunctionEEELi0EEEvPT_
- __ZNSt3__112__destroy_atB8nn190102INS_4pairIKyN2CI9DAGHelper19TextureReadFunctionEEELi0EEEvPT_
- __ZNSt3__112__hash_tableIN2CI11OtherDigestENS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorIS2_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
- __ZNSt3__112__hash_tableIN2CI17NodeContentDigestENS_4hashIS2_EENS_8equal_toIS2_EENS_9allocatorIS2_EEE4findIS2_EENS_15__hash_iteratorIPNS_11__hash_nodeIS2_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CI13ProgramDigestENS2_11ObjectCacheINS2_11MainProgramES3_Lb0EE5EntryEEENS_22__unordered_map_hasherIS3_S8_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE28__node_insert_unique_performB8nn190102EPNS_11__hash_nodeIS8_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CI13ProgramDigestENS2_11ObjectCacheINS2_11MainProgramES3_Lb0EE5EntryEEENS_22__unordered_map_hasherIS3_S8_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE28__node_insert_unique_prepareB8nn190102EmRS8_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIN2CI13ProgramDigestENS2_11ObjectCacheINS2_11MainProgramES3_Lb0EE5EntryEEENS_22__unordered_map_hasherIS3_S8_NS_4hashIS3_EENS_8equal_toIS3_EELb1EEENS_21__unordered_map_equalIS3_S8_SD_SB_Lb1EEENS_9allocatorIS8_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS8_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKN2CI11GraphObjectEjEENS_22__unordered_map_hasherIS5_S6_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE25__emplace_unique_key_argsIS5_JRKNS_21piecewise_construct_tENS_5tupleIJOS5_EEENSM_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPKN2CI11GraphObjectEjEENS_22__unordered_map_hasherIS5_S6_NS_4hashIS5_EENS_8equal_toIS5_EELb1EEENS_21__unordered_map_equalIS5_S6_SB_S9_Lb1EEENS_9allocatorIS6_EEE4findIS5_EENS_15__hash_iteratorIPNS_11__hash_nodeIS6_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS4_S7_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS4_S7_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJRKS4_EEENSN_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS4_S7_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEE4findIS4_EENS_15__hash_iteratorIPNS_11__hash_nodeIS7_PvEEEERKT_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS4_S7_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEE5clearEv
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS4_S7_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS4_S7_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEEC2EOSI_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11GraphObjectEPKvEENS_22__unordered_map_hasherIS4_S7_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_S7_SC_SA_Lb1EEENS_9allocatorIS7_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS_6vectorI6CGRectNS_9allocatorIS6_EEEEEENS_22__unordered_map_hasherIS4_SA_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SA_SF_SD_Lb1EEENS7_ISA_EEE11__do_rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS_6vectorI6CGRectNS_9allocatorIS6_EEEEEENS_22__unordered_map_hasherIS4_SA_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SA_SF_SD_Lb1EEENS7_ISA_EEE17__deallocate_nodeEPNS_16__hash_node_baseIPNS_11__hash_nodeISA_PvEEEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS_6vectorI6CGRectNS_9allocatorIS6_EEEEEENS_22__unordered_map_hasherIS4_SA_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SA_SF_SD_Lb1EEENS7_ISA_EEE25__emplace_unique_key_argsIS4_JRKNS_21piecewise_construct_tENS_5tupleIJRKS4_EEENSP_IJEEEEEENS_4pairINS_15__hash_iteratorIPNS_11__hash_nodeISA_PvEEEEbEERKT_DpOT0_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS_6vectorI6CGRectNS_9allocatorIS6_EEEEEENS_22__unordered_map_hasherIS4_SA_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SA_SF_SD_Lb1EEENS7_ISA_EEE8__rehashILb1EEEvm
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIPN2CI11ProgramNodeENS_6vectorI6CGRectNS_9allocatorIS6_EEEEEENS_22__unordered_map_hasherIS4_SA_NS_4hashIS4_EENS_8equal_toIS4_EELb1EEENS_21__unordered_map_equalIS4_SA_SF_SD_Lb1EEENS7_ISA_EEED2Ev
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_4NodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE28__node_insert_unique_performB8nn190102EPNS_11__hash_nodeIS7_PvEE
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_4NodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE28__node_insert_unique_prepareB8nn190102EmRS7_
- __ZNSt3__112__hash_tableINS_17__hash_value_typeIyN2CI11ObjectCacheINS2_4NodeEyLb0EE5EntryEEENS_22__unordered_map_hasherIyS7_NS_4hashIyEENS_8equal_toIyEELb1EEENS_21__unordered_map_equalIyS7_SC_SA_Lb1EEENS_9allocatorIS7_EEE5eraseENS_21__hash_const_iteratorIPNS_11__hash_nodeIS7_PvEEEE
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ENS_24__uninitialized_size_tagEmRKS4_
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102Emc
- __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEC2B8nn190102ILi0EEEPKc
- __ZNSt3__112construct_atB8nn190102IN2CI15SerialRectArray7roiDataEJRKS3_EPS3_EEPT_S8_DpOT0_
- __ZNSt3__112construct_atB8nn190102IN2CI15SerialRectArray7roiDataEJRS3_EPS3_EEPT_S7_DpOT0_
- __ZNSt3__112construct_atB8nn190102IN2CI15SerialRectArray7roiDataEJS3_EPS3_EEPT_S6_DpOT0_
- __ZNSt3__113__tree_removeB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__114__split_bufferIN2CI21SoftwareDAGDescriptor12ArgumentInfoERNS_9allocatorIS3_EEE5clearB8nn190102Ev
- __ZNSt3__114__split_bufferIN2CI22SWRendererFunctionNodeERNS_9allocatorIS2_EEE5clearB8nn190102Ev
- __ZNSt3__114__split_bufferIN2CI7TextureERNS_9allocatorIS2_EEE9push_backEOS2_
- __ZNSt3__114__split_bufferINS_10unique_ptrIN2CI8TileTaskENS2_13ObjectDeleterIS3_EEEERNS_9allocatorIS6_EEE17__destruct_at_endB8nn190102EPS6_
- __ZNSt3__114__split_bufferINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEERNS4_IS6_EEE17__destruct_at_endB8nn190102EPS6_
- __ZNSt3__114__split_bufferINS_6vectorIN2CI11Perspective3LSRI8EDAnchorEENS_9allocatorIS6_EEEERNS7_IS9_EEE17__destruct_at_endB8nn190102EPS9_
- __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryENS_9allocatorIS4_EEE10push_frontEOS4_
- __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryENS_9allocatorIS4_EEE9push_backEOS4_
- __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryERNS_9allocatorIS4_EEE10push_frontERKS4_
- __ZNSt3__114__split_bufferIPPN2CI17SurfaceCacheEntryERNS_9allocatorIS4_EEE9push_backEOS4_
- __ZNSt3__115allocate_sharedB8nn190102IN2CI19LegacyDAGDescriptorENS_9allocatorIS2_EEJRbS5_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115allocate_sharedB8nn190102IN2CI31StitchableFunctionDAGDescriptorENS_9allocatorIS2_EEJRbS5_ELi0EEENS_10shared_ptrIT_EERKT0_DpOT1_
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEEC2Ev
- __ZNSt3__115basic_streambufIcNS_11char_traitsIcEEED2Ev
- __ZNSt3__116__insertion_sortB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_T0_
- __ZNSt3__116__insertion_sortB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_T0_
- __ZNSt3__116__pad_and_outputB8nn190102IcNS_11char_traitsIcEEEENS_19ostreambuf_iteratorIT_T0_EES6_PKS4_S8_S8_RNS_8ios_baseES4_
- __ZNSt3__118basic_stringstreamIcNS_11char_traitsIcEENS_9allocatorIcEEEC1B8nn190102Ev
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI13LineCostProxyEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI22MTLArgumentTypePrivateEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI29MTLImageFilterFunctionInfoSPIEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI37MTLImageFilterFunctionArgumentInfoSPIEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI5IRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI6CGRectEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI7EDChainEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorI8EDAnchorEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI11Perspective3LSRI8EDAnchorEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI11Perspective4LineEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI11Perspective9NMSimplexIDv2_fE8NMVertexEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI11Perspective9NMSimplexIDv3_fE8NMVertexEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI13TraverseVisitEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI15SerialRectArray7roiDataEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI17NodeContentDigestEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI18ConstTraverseVisitEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI18KernelArgumentTypeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI21SoftwareDAGDescriptor12ArgumentInfoEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI22SWRendererFunctionNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI27SWRendererFunctionInputNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI6roiKeyEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI7TextureEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI8liveROIs8roiTupleEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIN2CI9parentROIEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_10unique_ptrIN2CI8TileTaskENS3_13ObjectDeleterIS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSB_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_4pairIPKvS4_EEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_4pairIdiEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_6vectorI5IRectNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_6vectorI6CGRectNS1_IS3_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_6vectorIN2CI11Perspective3LSRI8EDAnchorEENS1_IS7_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSD_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorINS_6vectorINS_4pairIdiEENS1_IS4_EEEEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIP11__IOSurfaceEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIP12NSMutableSetIP8NSStringEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERSA_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIP5QueueEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIP8NSStringEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPKN2CI11ProgramNodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPKN2CI14intermediate_tEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPKN2CI4NodeEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPKcEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPKvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS7_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPN2CI17SurfaceCacheEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS8_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPN2CI25ConcatenatedDAGDescriptor17MetalArgumentInfoEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPPN2CI17SurfaceCacheEntryEEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS9_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIPvEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS6_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIiEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorImEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__allocate_at_leastB8nn190102INS_9allocatorIsEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
- __ZNSt3__119__partial_sort_implB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_SC_EET1_SD_SD_T2_OT0_
- __ZNSt3__119__partial_sort_implB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_SC_EET1_SD_SD_T2_OT0_
- __ZNSt3__119__shared_weak_count16__release_sharedB8nn190102Ev
- __ZNSt3__120__shared_ptr_emplaceIN2CI19LegacyDAGDescriptorENS_9allocatorIS2_EEEC2B8nn190102IJRbS7_ES4_Li0EEES4_DpOT_
- __ZNSt3__120__shared_ptr_emplaceIN2CI31StitchableFunctionDAGDescriptorENS_9allocatorIS2_EEEC2B8nn190102IJRbS7_ES4_Li0EEES4_DpOT_
- __ZNSt3__120back_insert_iteratorINS_6vectorIdNS_9allocatorIdEEEEEaSB8nn190102ERKd
- __ZNSt3__122__tree_node_destructorINS_9allocatorINS_11__tree_nodeINS_12__value_typeINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEN2CI10SWFunctionEEEPvEEEEEclB8nn190102EPSD_
- __ZNSt3__124__put_character_sequenceB8nn190102IcNS_11char_traitsIcEEEERNS_13basic_ostreamIT_T0_EES7_PKS4_m
- __ZNSt3__126__insertion_sort_unguardedB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_T0_
- __ZNSt3__126__insertion_sort_unguardedB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEbT1_SD_T0_
- __ZNSt3__127__insertion_sort_incompleteB8nn190102INS_17_ClassicAlgPolicyERZZNK2CI8TileTask15pixelsOverdrawnEvENK3$_0clERKNS_6vectorI6CGRectNS_9allocatorIS6_EEEEEUlNS_4pairIdiEESD_E_PSD_EEbT1_SH_T0_
- __ZNSt3__127__tree_balance_after_insertB8nn190102IPNS_16__tree_node_baseIPvEEEEvT_S5_
- __ZNSt3__130__uninitialized_allocator_copyB8nn190102INS_9allocatorINS_12basic_stringIcNS_11char_traitsIcEENS1_IcEEEEEEPS6_S8_S8_EET2_RT_T0_T1_S9_
- __ZNSt3__131__partition_with_equals_on_leftB8nn190102INS_17_ClassicAlgPolicyEPN2CI11Perspective9NMSimplexIDv2_fE8NMVertexERZNS6_13orderVerticesEvEUlRKS7_SA_E_EET0_SD_SD_T1_
- __ZNSt3__131__partition_with_equals_on_leftB8nn190102INS_17_ClassicAlgPolicyEPN2CI11Perspective9NMSimplexIDv3_fE8NMVertexERZNS6_13orderVerticesEvEUlRKS7_SA_E_EET0_SD_SD_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8nn190102INS_17_ClassicAlgPolicyEPN2CI11Perspective9NMSimplexIDv2_fE8NMVertexERZNS6_13orderVerticesEvEUlRKS7_SA_E_EENS_4pairIT0_bEESE_SE_T1_
- __ZNSt3__132__partition_with_equals_on_rightB8nn190102INS_17_ClassicAlgPolicyEPN2CI11Perspective9NMSimplexIDv3_fE8NMVertexERZNS6_13orderVerticesEvEUlRKS7_SA_E_EENS_4pairIT0_bEESE_SE_T1_
- __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_9allocatorIN2CI15SerialRectArray7roiDataEEES4_EEvRT_PT0_S9_S9_
- __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_9allocatorIN2CI21SoftwareDAGDescriptor12ArgumentInfoEEES4_EEvRT_PT0_S9_S9_
- __ZNSt3__134__uninitialized_allocator_relocateB8nn190102INS_9allocatorIN2CI22SWRendererFunctionNodeEEES3_EEvRT_PT0_S8_S8_
- __ZNSt3__13mapIN2CI10ImageIndexENS1_30ImageDigestForRenderGraphCacheENS_4lessIS2_EENS_9allocatorINS_4pairIKS2_S3_EEEEE6insertB8nn190102INS_20__map_const_iteratorINS_21__tree_const_iteratorINS_12__value_typeIS2_S3_EEPNS_11__tree_nodeISG_PvEElEEEEEEvT_SN_
- __ZNSt3__13mapINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEN2CI10SWFunctionENS_4lessIS6_EENS4_INS_4pairIKS6_S8_EEEEEC2B8nn190102ESt16initializer_listISD_ERKSA_
- __ZNSt3__13setIPKcNS_4lessIS2_EENS_9allocatorIS2_EEE6insertB8nn190102INS_21__tree_const_iteratorIS2_PNS_11__tree_nodeIS2_PvEElEEEEvT_SF_
- __ZNSt3__13setIPKcNS_4lessIS2_EENS_9allocatorIS2_EEEC2B8nn190102ERKS7_
- __ZNSt3__14pairIKN2CI13ProgramDigestENS1_11ObjectCacheINS1_11MainProgramES2_Lb0EE5EntryEEC2B8nn190102IJRS3_EJRKPS5_RyRKjEJLm0EEJLm0ELm1ELm2EEEENS_21piecewise_construct_tERNS_5tupleIJDpT_EEERNSI_IJDpT0_EEENS_15__tuple_indicesIJXspT1_EEEENSR_IJXspT2_EEEE
- __ZNSt3__14pairIKyN2CI11ObjectCacheINS2_4NodeEyLb0EE5EntryEEC2B8nn190102IJRS1_EJRKPS4_RyRKjEJLm0EEJLm0ELm1ELm2EEEENS_21piecewise_construct_tERNS_5tupleIJDpT_EEERNSH_IJDpT0_EEENS_15__tuple_indicesIJXspT1_EEEENSQ_IJXspT2_EEEE
- __ZNSt3__15dequeIPN2CI17SurfaceCacheEntryENS_9allocatorIS3_EEED2B8nn190102Ev
- __ZNSt3__15stackIN2CI13TraverseVisitENS_6vectorIS2_NS_9allocatorIS2_EEEEE7emplaceB8nn190102IJPNS1_11GraphObjectERSA_iRiEEEDcDpOT_
- __ZNSt3__15stackIN2CI13TraverseVisitENS_6vectorIS2_NS_9allocatorIS2_EEEEE7emplaceB8nn190102IJRKPNS1_11GraphObjectESC_iRiEEEDcDpOT_
- __ZNSt3__15stackIN2CI13TraverseVisitENS_6vectorIS2_NS_9allocatorIS2_EEEEE7emplaceB8nn190102IJRPNS1_11GraphObjectEDniiEEEDcDpOT_
- __ZNSt3__15stackIN2CI13TraverseVisitENS_6vectorIS2_NS_9allocatorIS2_EEEEE7emplaceB8nn190102IJRPNS1_11GraphObjectESB_RiSC_EEEDcDpOT_
- __ZNSt3__15stackIN2CI18ConstTraverseVisitENS_6vectorIS2_NS_9allocatorIS2_EEEEE7emplaceB8nn190102IJPNS1_11GraphObjectERPKS9_iRiEEEDcDpOT_
- __ZNSt3__15stackIN2CI18ConstTraverseVisitENS_6vectorIS2_NS_9allocatorIS2_EEEEE7emplaceB8nn190102IJRKPNS1_11GraphObjectERKPKS9_iRiEEEDcDpOT_
- __ZNSt3__15stackIN2CI18ConstTraverseVisitENS_6vectorIS2_NS_9allocatorIS2_EEEEE7emplaceB8nn190102IJRPKNS1_11GraphObjectEDniiEEEDcDpOT_
- __ZNSt3__15stackIN2CI18ConstTraverseVisitENS_6vectorIS2_NS_9allocatorIS2_EEEEE7emplaceB8nn190102IJRPKNS1_11GraphObjectESC_RiSD_EEEDcDpOT_
- __ZNSt3__16__treeIZN2CI7Context16recursive_renderEPNS1_8TileTaskERKNS1_6roiKeyEPNS1_4NodeEbE8childKeyZNS2_16recursive_renderES4_S7_S9_bE12compareDepthNS_9allocatorISA_EEE7destroyEPNS_11__tree_nodeISA_PvEE
- __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEE18__assign_with_sizeB8nn190102IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEEC2B8nn190102Em
- __ZNSt3__16vectorI5IRectNS_9allocatorIS1_EEEC2ERKS4_
- __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE18__assign_with_sizeB8nn190102IPS1_S6_EEvT_T0_l
- __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEE18__insert_with_sizeB8nn190102INS_11__wrap_iterIPKS1_EES9_EENS6_IPS1_EES9_T_T0_l
- __ZNSt3__16vectorI6CGRectNS_9allocatorIS1_EEEC2ERKS4_
- __ZNSt3__16vectorIN2CI11Perspective4LineENS_9allocatorIS3_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CI11Perspective4LineENS_9allocatorIS3_EEE18__assign_with_sizeB8nn190102IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIN2CI13TraverseVisitENS_9allocatorIS2_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE16__init_with_sizeB8nn190102IPS3_S8_EEvT_T0_m
- __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE18__assign_with_sizeB8nn190102IPS3_S8_EEvT_T0_l
- __ZNSt3__16vectorIN2CI15SerialRectArray7roiDataENS_9allocatorIS3_EEE21__push_back_slow_pathIRKS3_EEPS3_OT_
- __ZNSt3__16vectorIN2CI17NodeContentDigestENS_9allocatorIS2_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CI18ConstTraverseVisitENS_9allocatorIS2_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEE18__assign_with_sizeB8nn190102IPS2_S7_EEvT_T0_l
- __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEE9push_backB8nn190102EOS2_
- __ZNSt3__16vectorIN2CI18KernelArgumentTypeENS_9allocatorIS2_EEEC2ERKS5_
- __ZNSt3__16vectorIN2CI21SoftwareDAGDescriptor12ArgumentInfoENS_9allocatorIS3_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorIN2CI22SWRendererFunctionNodeENS_9allocatorIS2_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorIN2CI27SWRendererFunctionInputNodeENS_9allocatorIS2_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CI27SWRendererFunctionInputNodeENS_9allocatorIS2_EEE12emplace_backIJNS1_18SWArgumentInfoTypeEEEERS2_DpOT_
- __ZNSt3__16vectorIN2CI27SWRendererFunctionInputNodeENS_9allocatorIS2_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorIN2CI27SWRendererFunctionInputNodeENS_9allocatorIS2_EEE16__init_with_sizeB8nn190102IPS2_S7_EEvT_T0_m
- __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE21__push_back_slow_pathIS2_EEPS2_OT_
- __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE26__swap_out_circular_bufferERNS_14__split_bufferIS2_RS4_EEPS2_
- __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE6insertENS_11__wrap_iterIPKS2_EEOS2_
- __ZNSt3__16vectorIN2CI7TextureENS_9allocatorIS2_EEE6insertENS_11__wrap_iterIPKS2_EERS7_
- __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEE18__assign_with_sizeB8nn190102IPS2_S7_EEvT_T0_l
- __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEE18__insert_with_sizeB8nn190102INS_11__wrap_iterIPKS2_EESA_EENS7_IPS2_EESA_T_T0_l
- __ZNSt3__16vectorIN2CI9parentROIENS_9allocatorIS2_EEEC2ERKS5_
- __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE16__init_with_sizeB8nn190102IPS4_S8_EEvT_T0_m
- __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE18__assign_with_sizeB8nn190102IPS4_S8_EEvT_T0_l
- __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEE7__clearB8nn190102Ev
- __ZNSt3__16vectorINS0_I5IRectNS_9allocatorIS1_EEEENS2_IS4_EEEC2B8nn190102Em
- __ZNSt3__16vectorINS0_I6CGRectNS_9allocatorIS1_EEEENS2_IS4_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorINS0_I6CGRectNS_9allocatorIS1_EEEENS2_IS4_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS0_I6CGRectNS_9allocatorIS1_EEEENS2_IS4_EEE7__clearB8nn190102Ev
- __ZNSt3__16vectorINS0_I6CGRectNS_9allocatorIS1_EEEENS2_IS4_EEEC2B8nn190102Em
- __ZNSt3__16vectorINS0_IN2CI11Perspective3LSRI8EDAnchorEENS_9allocatorIS5_EEEENS6_IS8_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS0_IN2CI11Perspective3LSRI8EDAnchorEENS_9allocatorIS5_EEEENS6_IS8_EEE7__clearB8nn190102Ev
- __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEE7__clearB8nn190102Ev
- __ZNSt3__16vectorINS0_INS_4pairIdiEENS_9allocatorIS2_EEEENS3_IS5_EEEC2B8nn190102Em
- __ZNSt3__16vectorINS_10unique_ptrIN2CI8TileTaskENS2_13ObjectDeleterIS3_EEEENS_9allocatorIS6_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS_10unique_ptrIN2CI8TileTaskENS2_13ObjectDeleterIS3_EEEENS_9allocatorIS6_EEE7__clearB8nn190102Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__destroy_vectorclB8nn190102Ev
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE16__init_with_sizeB8nn190102IPS6_SA_EEvT_T0_m
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE18__assign_with_sizeB8nn190102IPS6_SA_EEvT_T0_l
- __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE7__clearB8nn190102Ev
- __ZNSt3__16vectorINS_4pairIPKvS3_EENS_9allocatorIS4_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorINS_4pairIPKvS3_EENS_9allocatorIS4_EEEC2ERKS7_
- __ZNSt3__16vectorIP11__IOSurfaceNS_9allocatorIS2_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIPKN2CI14intermediate_tENS_9allocatorIS4_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIbNS_9allocatorIbEEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIbNS_9allocatorIbEEE16__init_with_sizeB8nn190102IPbS5_EEvT_T0_m
- __ZNSt3__16vectorImNS_9allocatorImEEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorImNS_9allocatorImEEE18__assign_with_sizeB8nn190102IPmS5_EEvT_T0_l
- __ZNSt3__16vectorImNS_9allocatorImEEEC2ERKS3_
- __ZNSt3__16vectorIsNS_9allocatorIsEEE11__vallocateB8nn190102Em
- __ZNSt3__16vectorIsNS_9allocatorIsEEEC2ERKS3_
- __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEjT1_SD_SD_T0_
- __ZNSt3__17__sort3B8nn190102INS_17_ClassicAlgPolicyERZZNK2CI8TileTask15pixelsOverdrawnEvENK3$_0clERKNS_6vectorI6CGRectNS_9allocatorIS6_EEEEEUlNS_4pairIdiEESD_E_PSD_EEjT1_SH_SH_T0_
- __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_SD_SD_T0_
- __ZNSt3__17__sort4B8nn190102INS_17_ClassicAlgPolicyERZZNK2CI8TileTask15pixelsOverdrawnEvENK3$_0clERKNS_6vectorI6CGRectNS_9allocatorIS6_EEEEEUlNS_4pairIdiEESD_E_PSD_EEvT1_SH_SH_SH_T0_
- __ZNSt3__17__sort5B8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__17__sort5B8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_SD_SD_SD_T0_
- __ZNSt3__19__sift_upB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv2_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_OT0_NS_15iterator_traitsISD_E15difference_typeE
- __ZNSt3__19__sift_upB8nn190102INS_17_ClassicAlgPolicyERZN2CI11Perspective9NMSimplexIDv3_fE13orderVerticesEvEUlRKNS6_8NMVertexES9_E_PS7_EEvT1_SD_OT0_NS_15iterator_traitsISD_E15difference_typeE
- __ZNSt3__1ssB8nn190102IcNS_11char_traitsIcEEEEDaNS_17basic_string_viewIT_T0_EENS_13type_identityIS7_E4typeE
- __ZNSt3__1ssB8nn190102IcNS_11char_traitsIcEENS_9allocatorIcEEEEDaRKNS_12basic_stringIT_T0_T1_EESC_
- __ZSt28__throw_bad_array_new_lengthB8nn190102v
- __ZTVN2CI15InstanceCountedILNS_4TypeE18EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE30EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE31EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE46EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE47EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE48EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE49EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE59EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE67EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE68EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE71EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE75EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE76EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE78EEE
- __ZTVN2CI15InstanceCountedILNS_4TypeE85EEE
- __ZTVN2CI8MetalDAGE
- __ZThn104_N2CI11SwitchImageD0Ev
- __ZThn104_N2CI11SwitchImageD1Ev
- __ZThn104_N2CI12SurfaceImageD0Ev
- __ZThn104_N2CI12SurfaceImageD1Ev
- __ZThn104_N2CI12TextureImageD0Ev
- __ZThn104_N2CI12TextureImageD1Ev
- __ZThn104_N2CI13ProviderImageD0Ev
- __ZThn104_N2CI13ProviderImageD1Ev
- __ZThn104_N2CI14GLTextureImageD0Ev
- __ZThn104_N2CI14GLTextureImageD1Ev
- __ZThn104_N2CI16ColorKernelImageD0Ev
- __ZThn104_N2CI16ColorKernelImageD1Ev
- __ZThn104_N2CI17MetalTextureImageD0Ev
- __ZThn104_N2CI17MetalTextureImageD1Ev
- __ZThn104_N2CI18GeneralKernelImageD0Ev
- __ZThn104_N2CI18GeneralKernelImageD1Ev
- __ZThn104_N2CI7CGImageD0Ev
- __ZThn104_N2CI7CGImageD1Ev
- __ZThn104_N2CI9FillImageD0Ev
- __ZThn104_N2CI9FillImageD1Ev
- __ZThn104_NK2CI11SwitchImage4typeEv
- __ZThn104_NK2CI12SurfaceImage4typeEv
- __ZThn104_NK2CI12TextureImage4typeEv
- __ZThn104_NK2CI13ProviderImage4typeEv
- __ZThn104_NK2CI16ColorKernelImage4typeEv
- __ZThn104_NK2CI18GeneralKernelImage4typeEv
- __ZThn104_NK2CI7CGImage4typeEv
- __ZThn104_NK2CI9FillImage4typeEv
- __ZThn112_N2CI10ClampImageD0Ev
- __ZThn112_N2CI10ClampImageD1Ev
- __ZThn112_N2CI10GammaImageD0Ev
- __ZThn112_N2CI10GammaImageD1Ev
- __ZThn112_N2CI11AffineImageD0Ev
- __ZThn112_N2CI11AffineImageD1Ev
- __ZThn112_N2CI12SwizzleImageD0Ev
- __ZThn112_N2CI12SwizzleImageD1Ev
- __ZThn112_N2CI13SetPropsImageD0Ev
- __ZThn112_N2CI13SetPropsImageD1Ev
- __ZThn112_N2CI14ProcessorImageD0Ev
- __ZThn112_N2CI14ProcessorImageD1Ev
- __ZThn112_N2CI15ColorMatchImageD0Ev
- __ZThn112_N2CI15ColorMatchImageD1Ev
- __ZThn112_N2CI15SampleModeImageD0Ev
- __ZThn112_N2CI15SampleModeImageD1Ev
- __ZThn112_N2CI15WarpKernelImageD0Ev
- __ZThn112_N2CI15WarpKernelImageD1Ev
- __ZThn112_N2CI16ColorMatrixImageD0Ev
- __ZThn112_N2CI16ColorMatrixImageD1Ev
- __ZThn112_N2CI16PremultiplyImageD0Ev
- __ZThn112_N2CI16PremultiplyImageD1Ev
- __ZThn112_N2CI17ClampToAlphaImageD0Ev
- __ZThn112_N2CI17ClampToAlphaImageD1Ev
- __ZThn112_N2CI18TagColorSpaceImageD0Ev
- __ZThn112_N2CI18TagColorSpaceImageD1Ev
- __ZThn112_N2CI9CropImageD0Ev
- __ZThn112_N2CI9CropImageD1Ev
- __ZThn112_N2CI9NoopImageD0Ev
- __ZThn112_N2CI9NoopImageD1Ev
- __ZThn112_N2CI9SRGBImageD0Ev
- __ZThn112_N2CI9SRGBImageD1Ev
- __ZThn112_NK2CI10ClampImage4typeEv
- __ZThn112_NK2CI10GammaImage4typeEv
- __ZThn112_NK2CI11AffineImage4typeEv
- __ZThn112_NK2CI12SwizzleImage4typeEv
- __ZThn112_NK2CI13SetPropsImage4typeEv
- __ZThn112_NK2CI14ProcessorImage4typeEv
- __ZThn112_NK2CI15ColorMatchImage4typeEv
- __ZThn112_NK2CI15SampleModeImage4typeEv
- __ZThn112_NK2CI15WarpKernelImage4typeEv
- __ZThn112_NK2CI16ColorMatrixImage4typeEv
- __ZThn112_NK2CI16PremultiplyImage4typeEv
- __ZThn112_NK2CI17ClampToAlphaImage4typeEv
- __ZThn112_NK2CI18TagColorSpaceImage4typeEv
- __ZThn112_NK2CI9CropImage4typeEv
- __ZThn112_NK2CI9NoopImage4typeEv
- __ZThn112_NK2CI9SRGBImage4typeEv
- __ZThn176_N2CI8MetalDAGD0Ev
- __ZThn176_N2CI8MetalDAGD1Ev
- __ZThn176_NK2CI8MetalDAG4typeEv
- __ZThn96_N2CI13GLMainProgramD0Ev
- __ZThn96_N2CI13GLMainProgramD1Ev
- __ZThn96_N2CI16MetalMainProgramD0Ev
- __ZThn96_N2CI16MetalMainProgramD1Ev
- __ZThn96_N2CI8MetalDAGD0Ev
- __ZThn96_N2CI8MetalDAGD1Ev
- __ZThn96_NK2CI13GLMainProgram4typeEv
- __ZThn96_NK2CI16MetalMainProgram4typeEv
- __ZThn96_NK2CI8MetalDAG4typeEv
- __ZZ22CI_DEBUG_CONTEXT_COLORE1v
- __ZZ23CI_LOG_AIR_ARCHIVE_MISSE1v
- __ZZ23CI_USE_ARCHIVED_KERNELSE1v
- __ZZ27CI_LOG_AIR_ARCHIVE_ACTIVITYE1v
- __ZZ46-[CIPerspectiveAutoCalcV1 clusterLineSegments]ENK3$_2clERKNSt3__16vectorIN2CI11Perspective4LineENS0_9allocatorIS4_EEEEZ46-[CIPerspectiveAutoCalcV1 clusterLineSegments]E10HypothesisRS7_SB_
- __ZZ46-[CIPerspectiveAutoCalcV2 clusterLineSegments]ENK3$_4clERKNSt3__16vectorIN2CI11Perspective4LineENS0_9allocatorIS4_EEEEZ46-[CIPerspectiveAutoCalcV2 clusterLineSegments]E10HypothesisRS7_SB_
- __ZZ8loadACBSE10ACBSLoaded
- __ZZ8loadACBSE9ACBSFuncs
- __ZZ8loadACBSE9onceToken
- __ZZL13isSWAllowListvE7allowed
- __ZZL13isSWAllowListvE9onceToken
- __ZZL52getVNGenerateAttentionBasedSaliencyImageRequestClassvE9softClass.0
- __ZZN2CI12MetalContext11render_nodeEPNS_8TileTaskERKNS_9parentROIERK6CGRectPPKvPP11__IOSurfacemEN13SignpostTimerD1E_0v
- __ZZN2CI8MetalDAG7compileENS_9NodeIndexEEN13SignpostTimerD1Ev
- __ZZN2CIL24createConverterArrayFromEP12CGColorSpacefbfE5mutex
- __ZZZ65+[CIImageProcessorKernel applyWithExtent:inputs:arguments:error:]EUb0_EN13SignpostTimerD1E_0v
- __ZZZ65+[CIImageProcessorKernel applyWithExtent:inputs:arguments:error:]EUb0_EN13SignpostTimerD1Ev
- __Znwm
- ___103-[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:]_block_invoke
- ___43-[CIBurstImageSetInternal processClusters:]_block_invoke
- ___47-[CIBurstImageSetInternal bestImageIdentifiers]_block_invoke
- ___52+[CIContext(Internal) internalSWContextWithOptions:]_block_invoke.306
- ___54+[CIKernelLibrary(Internal) coreImageDylibWithDevice:]_block_invoke.98
- ___62-[CIBurstImageFaceAnalysisContext findFacesInImage:imageStat:]_block_invoke
- ___64+[CISaliencyMapKernel processWithInputs:arguments:output:error:]_block_invoke
- ___66+[CIContext(Internal) internalContextWithMTLCommandQueue:options:]_block_invoke.305
- ___87-[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:]_block_invoke
- ___88-[CIBurstImageSetInternal addYUVImage:properties:identifier:imageProps:completionBlock:]_block_invoke
- ___AVFoundationLibraryCore_block_invoke
- ___ArchiveLibraryUsingStitchedDagDescriptor_block_invoke
- ___ArchiveLibraryUsingStitchedDagDescriptor_block_invoke.cold.1
- ___ArchiveLibraryUsingStitchedDagDescriptor_block_invoke.cold.2
- ___ArchiveLibraryUsingStitchedDagDescriptor_block_invoke.cold.3
- ___ArchiveLibrary_block_invoke
- ___ArchiveLibrary_block_invoke.cold.1
- ___Block_byref_object_copy_.100
- ___Block_byref_object_copy_.102
- ___Block_byref_object_copy_.105
- ___Block_byref_object_copy_.116
- ___Block_byref_object_copy_.122
- ___Block_byref_object_copy_.16
- ___Block_byref_object_copy_.18
- ___Block_byref_object_copy_.22
- ___Block_byref_object_copy_.241
- ___Block_byref_object_copy_.32
- ___Block_byref_object_copy_.477
- ___Block_byref_object_copy_.53
- ___Block_byref_object_copy_.59
- ___Block_byref_object_copy_.69
- ___Block_byref_object_copy_.869
- ___Block_byref_object_copy_.873
- ___Block_byref_object_copy_.92
- ___Block_byref_object_copy_.98
- ___Block_byref_object_dispose_.101
- ___Block_byref_object_dispose_.103
- ___Block_byref_object_dispose_.106
- ___Block_byref_object_dispose_.117
- ___Block_byref_object_dispose_.123
- ___Block_byref_object_dispose_.17
- ___Block_byref_object_dispose_.19
- ___Block_byref_object_dispose_.23
- ___Block_byref_object_dispose_.242
- ___Block_byref_object_dispose_.33
- ___Block_byref_object_dispose_.478
- ___Block_byref_object_dispose_.54
- ___Block_byref_object_dispose_.60
- ___Block_byref_object_dispose_.70
- ___Block_byref_object_dispose_.870
- ___Block_byref_object_dispose_.874
- ___Block_byref_object_dispose_.93
- ___Block_byref_object_dispose_.99
- ___CIMetalRenderToImageblocks_block_invoke.92
- ___CIMetalRenderToTextures_block_invoke.83
- ___CIMetalRenderToTextures_block_invoke.83.cold.1
- ___CIMetalRenderToTextures_block_invoke.83.cold.2
- ___FaceCoreLibraryCore_block_invoke
- ___FastRegistration_computeSignatures_block_invoke
- ___FastRegistration_computeSignatures_block_invoke_2
- ___FastRegistration_computeSignatures_block_invoke_3
- ___FastRegistration_register_block_invoke
- ___FastRegistration_register_block_invoke_2
- ___FastRegistration_register_block_invoke_3
- ___Projections_projectionCols_planar8UtoF_block_invoke
- ___Projections_projectionCols_planar8UtoF_block_invoke_2
- ___Projections_projectionRows_planar8UtoF_block_invoke
- ___Projections_projectionRows_planar8UtoF_block_invoke_2
- ____ZL12post_processP7NSArrayIP21CIImageProcessorInputEP22CIImageProcessorOutputPN2CI7ContextE_block_invoke
- ____ZL13isSWAllowListv_block_invoke
- ____ZL19set_context_optionsPN2CI9GLContextEP12NSDictionary_block_invoke.412
- ____ZL22register_more_builtinsU13block_pointerFvP8NSStringE_block_invoke.1067
- ____ZL22register_more_builtinsU13block_pointerFvP8NSStringE_block_invoke.1084
- ____ZL22register_more_builtinsU13block_pointerFvP8NSStringE_block_invoke.1091
- ____ZL52getVNGenerateAttentionBasedSaliencyImageRequestClassv_block_invoke
- ____ZL52getVNGenerateAttentionBasedSaliencyImageRequestClassv_block_invoke.cold.1
- ____ZN2CI11ProgramNode28create_program_and_argumentsEPNS_7ContextEPKc_block_invoke.78
- ____ZN2CI13KernelArchive10addArchiveENSt3__14pairIPKvS4_EE_block_invoke
- ____ZN2CI13KernelArchive4findEyPKc_block_invoke
- ____ZN2CI14MetalDAGHelper9build_dagEPKNS_4NodeEPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEm_block_invoke.44
- ____ZN2CI14MetalDAGHelper9build_dagEPKNS_4NodeEPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEm_block_invoke_2.45
- ____ZN2CI16GLTextureManager10wiredBytesEv_block_invoke
- ____ZN2CI16GLTextureManager16attach_IOSurfaceEP11__IOSurfacebiRKNS_17TextureDescriptorEiiib_block_invoke
- ____ZN2CI16GLTextureManager16attach_IOSurfaceEP11__IOSurfacebiRKNS_17TextureDescriptorEiiib_block_invoke.cold.1
- ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxRKNS_6BitmapES3_NS_7TextureENS_11ConvertTypeE_block_invoke
- ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxRKNS_6BitmapES3_NS_7TextureENS_11ConvertTypeE_block_invoke_2
- ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxRKNS_6BitmapES3_NS_7TextureENS_11ConvertTypeE_block_invoke_3
- ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxRKNS_6BitmapES3_NS_7TextureENS_11ConvertTypeE_block_invoke_4
- ____ZN2CI25convert_buffer_to_textureEPNS_7ContextEP11__IOSurfacexxRKNS_6BitmapES3_NS_7TextureENS_11ConvertTypeE_block_invoke_5
- ____ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb_block_invoke
- ____ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb_block_invoke.11
- ____ZN2CI7Context16recursive_renderEPNS_8TileTaskERKNS_6roiKeyEPNS_4NodeEb_block_invoke_2
- ____ZN2CI8MetalDAGD2Ev_block_invoke
- ____ZN2CI9DAGHelper9build_dagEPKNS_4NodeEPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEm_block_invoke.21
- ____ZN2CI9DAGHelper9build_dagEPKNS_4NodeEPKNS_11ProgramNodeEPNS_20SerialObjectPtrArrayEm_block_invoke_2.22
- ____ZN2CI9GLContext16render_root_nodeEPNS_8TileTaskERKNS_9parentROIEU13block_pointerFvvES7__block_invoke.39
- ____ZN2CI9GLContext16render_root_nodeEPNS_8TileTaskERKNS_9parentROIEU13block_pointerFvvES7__block_invoke.39.cold.1
- ____ZN2CIL13LogCacheStateEbPKc_block_invoke.114
- ____ZN2CIL13convert_metalEPKNS_12MetalContextERKNS_6BitmapEP11__IOSurfaceNS_7TextureENS_11ConvertTypeE_block_invoke
- ____ZN2CIL13convert_metalEPKNS_12MetalContextERKNS_6BitmapEP11__IOSurfaceNS_7TextureENS_11ConvertTypeE_block_invoke.231
- ____ZN2CIL13convert_metalEPKNS_12MetalContextERKNS_6BitmapEP11__IOSurfaceNS_7TextureENS_11ConvertTypeE_block_invoke.234
- ____ZN2CIL19AppendColorSpaceSrcEPNS_7ContextEPNS_4NodeENS_10ImageIndexEP12CGColorSpacebfb_block_invoke
- ____ZN2CIL19print_program_graphEPNS_7ContextEPKNS_17RenderDestinationEdPKNS_8TileTaskEPKcPNS_4NodeERK6CGRectNS_11PixelFormatE_block_invoke
- ____ZN2CIL20AppendConverterArrayEPNS_7ContextEPNS_4NodeENS_10ImageIndexEPK9__CFArrayNS_18ConverterDirectionEbb_block_invoke.102
- ____ZN2CIL20AppendConverterArrayEPNS_7ContextEPNS_4NodeENS_10ImageIndexEPK9__CFArrayNS_18ConverterDirectionEbb_block_invoke.109
- ____ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ff_block_invoke
- ____ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ff_block_invoke_2
- ____ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ff_block_invoke_3
- ____ZN2CIL20createConverterArrayEP12CGColorSpaceS1_ff_block_invoke_4
- ____ZN2CIL21print_graph_recursiveINS_4NodeENS_9NodeIndexENS1_9NodeStatsEEEvP7__sFILEPKT_iRKNSt3__113unordered_mapIT0_T1_NS9_4hashISB_EENS9_8equal_toISB_EENS9_9allocatorINS9_4pairIKSB_SC_EEEEEE_block_invoke.118
- ____ZN2CIL21print_graph_recursiveINS_5ImageENS_10ImageIndexENS1_10ImageStatsEEEvP7__sFILEPKT_iRKNSt3__113unordered_mapIT0_T1_NS9_4hashISB_EENS9_8equal_toISB_EENS9_9allocatorINS9_4pairIKSB_SC_EEEEEE_block_invoke.871
- ____ZN2CIL21print_graph_recursiveINS_5ImageENS_10ImageIndexENS1_10ImageStatsEEEvP7__sFILEPKT_iRKNSt3__113unordered_mapIT0_T1_NS9_4hashISB_EENS9_8equal_toISB_EENS9_9allocatorINS9_4pairIKSB_SC_EEEEEE_block_invoke.876
- ____ZN2CIL23_traverse_program_graphENS_6roiKeyERNS_8liveROIsERm_block_invoke
- ____ZNK2CI11ProgramNode18print_for_graphvizEP7__sFILERKNSt3__113unordered_mapIPKNS_11GraphObjectEjNS3_4hashIS7_EENS3_8equal_toIS7_EENS3_9allocatorINS3_4pairIKS7_jEEEEEENS_4Node9NodeStatsE_block_invoke.107
- ____ZNK2CI11ProgramNode18print_for_graphvizEP7__sFILERKNSt3__113unordered_mapIPKNS_11GraphObjectEjNS3_4hashIS7_EENS3_8equal_toIS7_EENS3_9allocatorINS3_4pairIKS7_jEEEEEENS_4Node9NodeStatsE_block_invoke.111
- ____ZNK2CI7Context19swizzler_for_outputENS_11PixelFormatENS_15DestinationTypeE_block_invoke
- ____ZNK2CI7Context30format_is_supported_for_outputENS_11PixelFormatENS_15DestinationTypeE_block_invoke
- ____ZNK2CI8TileTask23graphviz_representationEPKNS_10RenderTaskE_block_invoke.24
- ____ZNK2CI9GLContext11blitSurfaceEP11__IOSurface5IRectPNS_14intermediate_tES3_RKNS_17TextureDescriptorE_block_invoke.47
- ____ZNK2CI9GLContext11blitSurfaceEP11__IOSurface5IRectPNS_14intermediate_tES3_RKNS_17TextureDescriptorE_block_invoke.47.cold.1
- ___block_descriptor_40_e8_32b_e163_{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{__compressed_pair<CGRect *, std::allocator<CGRect>>=^{CGRect}}}44?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12ls32l8
- ___block_descriptor_40_e8_32o_e22_v48?0r^v8Q16Q24Q32Q40ls32l8
- ___block_descriptor_48_e8_32o40b_e134_v136?0r^v8r^v16r^v24r^v32r^v40^{__IOSurface=}48{Texture=(?=Q{?=II}{?=^v^v})}56Q72{CGRect={CGPoint=dd}{CGSize=dd}}80B112i116^v120^v128ls32l8s40l8
- ___block_descriptor_48_e8_32o40o_e163_{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{__compressed_pair<CGRect *, std::allocator<CGRect>>=^{CGRect}}}44?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12ls32l8s40l8
- ___block_descriptor_56_e5_v8?0l
- ___block_descriptor_60_e28_v16?0"<MTLCommandBuffer>"8l
- ___block_descriptor_72_e21_v48?0^v8Q16Q24Q32Q40l
- ___block_descriptor_72_e8_32r40r_e5_v8?0lr32l8r40l8
- ___block_descriptor_73_e8_32o40o48o56b_e134_v136?0r^v8r^v16r^v24r^v32r^v40^{__IOSurface=}48{Texture=(?=Q{?=II}{?=^v^v})}56Q72{CGRect={CGPoint=dd}{CGSize=dd}}80B112i116^v120^v128ls56l8s32l8s40l8s48l8
- ___block_descriptor_76_e8_32o40o_e28_v16?0"<MTLCommandBuffer>"8ls32l8s40l8
- ___block_descriptor_80_e8_32o40o48o56o64o72b_e5_v8?0ls32l8s40l8s48l8s72l8s56l8s64l8
- ___block_descriptor_80_e8_32o40o_e29_q24?0"FCRFace"8"FCRFace"16ls32l8s40l8
- ___block_descriptor_92_e21_v48?0^v8Q16Q24Q32Q40l
- ___block_descriptor_96_e21_v48?0^v8Q16Q24Q32Q40l
- ___block_descriptor_96_e22_v48?0r^v8Q16Q24Q32Q40l
- ___block_descriptor_tmp.101
- ___block_descriptor_tmp.102
- ___block_descriptor_tmp.132
- ___block_descriptor_tmp.133
- ___block_descriptor_tmp.144
- ___block_descriptor_tmp.166
- ___block_descriptor_tmp.169
- ___block_descriptor_tmp.173
- ___block_descriptor_tmp.193
- ___block_descriptor_tmp.196
- ___block_descriptor_tmp.199
- ___block_descriptor_tmp.211
- ___block_descriptor_tmp.218
- ___block_descriptor_tmp.219
- ___block_descriptor_tmp.226
- ___block_descriptor_tmp.227
- ___block_descriptor_tmp.230
- ___block_descriptor_tmp.235
- ___block_descriptor_tmp.250
- ___block_descriptor_tmp.257
- ___block_descriptor_tmp.260
- ___block_descriptor_tmp.263
- ___block_descriptor_tmp.277
- ___block_descriptor_tmp.42
- ___block_descriptor_tmp.43
- ___block_descriptor_tmp.58
- ___block_descriptor_tmp.73
- ___block_descriptor_tmp.75
- ___block_descriptor_tmp.76
- ___block_descriptor_tmp.88
- ___block_descriptor_tmp.89
- ___block_descriptor_tmp.94
- ___block_literal_global.1013
- ___block_literal_global.1023
- ___block_literal_global.103
- ___block_literal_global.1034
- ___block_literal_global.1066
- ___block_literal_global.111
- ___block_literal_global.113
- ___block_literal_global.114
- ___block_literal_global.115
- ___block_literal_global.1151
- ___block_literal_global.1156
- ___block_literal_global.117
- ___block_literal_global.123
- ___block_literal_global.1246
- ___block_literal_global.126
- ___block_literal_global.15
- ___block_literal_global.155
- ___block_literal_global.156
- ___block_literal_global.158
- ___block_literal_global.160
- ___block_literal_global.173
- ___block_literal_global.174
- ___block_literal_global.178
- ___block_literal_global.18
- ___block_literal_global.193
- ___block_literal_global.209
- ___block_literal_global.210
- ___block_literal_global.219
- ___block_literal_global.231
- ___block_literal_global.232
- ___block_literal_global.237
- ___block_literal_global.24
- ___block_literal_global.249
- ___block_literal_global.275
- ___block_literal_global.28
- ___block_literal_global.292
- ___block_literal_global.328
- ___block_literal_global.356
- ___block_literal_global.371
- ___block_literal_global.387
- ___block_literal_global.392
- ___block_literal_global.397
- ___block_literal_global.402
- ___block_literal_global.440
- ___block_literal_global.45
- ___block_literal_global.461
- ___block_literal_global.504
- ___block_literal_global.54
- ___block_literal_global.555
- ___block_literal_global.612
- ___block_literal_global.63
- ___block_literal_global.66
- ___block_literal_global.67
- ___block_literal_global.70
- ___block_literal_global.75
- ___block_literal_global.77
- ___block_literal_global.780
- ___block_literal_global.786
- ___block_literal_global.867
- ___block_literal_global.97
- ___getFCRDetectionParamDetectionRegionSymbolLoc_block_invoke
- ___getFCRDetectionParamInitialAngleSymbolLoc_block_invoke
- ___getFCRExtractionParamEnhancedEyesAndMouthLocalizationSymbolLoc_block_invoke
- ___getFCRExtractionParamExtractBlinkSymbolLoc_block_invoke
- ___getFCRExtractionParamExtractFaceprintSymbolLoc_block_invoke
- ___getFCRExtractionParamExtractLandmarkPointsSymbolLoc_block_invoke
- ___getFCRExtractionParamExtractSmileSymbolLoc_block_invoke
- ___getFCRExtractionParamInitialAngleSymbolLoc_block_invoke
- ___getFCRFaceExpressionLeftEyeClosedScoreSymbolLoc_block_invoke
- ___getFCRFaceExpressionLeftEyeClosedSymbolLoc_block_invoke
- ___getFCRFaceExpressionRightEyeClosedScoreSymbolLoc_block_invoke
- ___getFCRFaceExpressionRightEyeClosedSymbolLoc_block_invoke
- ___getFCRFaceExpressionSmileScoreSymbolLoc_block_invoke
- ___getFCRFaceExpressionSmileSymbolLoc_block_invoke
- ___getFCRFastFaceDetectionParametersSymbolLoc_block_invoke
- ___getFCRSetupParamNumberOfAnglesSymbolLoc_block_invoke
- ___getFaceCoreDetectorClass_block_invoke
- ___getFaceCoreDetectorClass_block_invoke.cold.1
- ___getFaceCoreFaceClass_block_invoke
- ___getFaceCoreFaceClass_block_invoke.cold.1
- ___getFaceCoreImageClass_block_invoke
- ___getFaceCoreImageClass_block_invoke.cold.1
- ___getVNGeneratePersonSegmentationRequestClass_block_invoke
- ___getVNGeneratePersonSegmentationRequestClass_block_invoke.cold.1
- ___loadACBS_block_invoke
- ___memcpy_chk
- ___providerGetBytesAtPositionCallback_1C08_surface_block_invoke
- ___providerGetBytesAtPositionCallback_1C0f_surface_block_invoke
- ___providerGetBytesAtPositionCallback_1C0h_surface_block_invoke
- ___providerGetBytesAtPositionCallback_1C0h_surface_lut_block_invoke
- ___providerGetBytesAtPositionCallback_1C0h_surface_lut_block_invoke_2
- ___providerGetBytesAtPositionCallback_1C16_surface_block_invoke
- ___providerGetBytesAtPositionCallback_2C08_surface_block_invoke
- ___providerGetBytesAtPositionCallback_2C0f_surface_block_invoke
- ___providerGetBytesAtPositionCallback_2C0h_surface_block_invoke
- ___providerGetBytesAtPositionCallback_2C16_surface_block_invoke
- ___providerGetBytesAtPositionCallback_A008_surface_block_invoke
- ___providerGetBytesAtPositionCallback_AYCbCr8_surface_block_invoke
- ___providerGetBytesAtPositionCallback_CbYCrYFull_surface_block_invoke
- ___providerGetBytesAtPositionCallback_CbYCrY_surface_block_invoke
- ___providerGetBytesAtPositionCallback_YCbYCrFull_surface_block_invoke
- ___providerGetBytesAtPositionCallback_YCbYCr_surface_block_invoke
- ___providerGetBytesAtPositionCallback_l10r_surface_block_invoke
- ___providerGetBytesAtPositionCallback_w30r_surface_block_invoke
- ___providerGetBytesAtPositionCallback_w40a_surface_block_invoke
- _allocateSignatureBuffers
- _audit_stringAVFoundation
- _audit_stringFaceCore
- _compareFloats
- _compareGridElements
- _comparePeaks
- _computeEdge1Squared16x16_NEON
- _computeEdgeVal
- _computeEdgeValOne8x8
- _computeForegroundInterval
- _computeRegistrationErrorStats
- _denormalizationTransform
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _energyFunction1
- _energyFunction2
- _findBestThreeWayDivision
- _fread
- _fseek
- _gBurstLoggingCallback
- _gBurstLoggingFileHandle
- _gBurstLoggingUserData
- _gLongBurstWeights
- _gMediumBurstWeights
- _gShortBurstWeights
- _gWhyNotTryVideoInsteadWeights
- _g_initTime
- _g_svmParameters_v1
- _g_svmParameters_v2
- _getAVCameraCalibrationDataClass
- _getAVDepthDataClass
- _getAVPortraitEffectsMatteClass
- _getAVSemanticSegmentationMatteClass
- _getFCRDetectionParamDetectionRegionSymbolLoc.ptr
- _getFCRDetectionParamInitialAngleSymbolLoc.ptr
- _getFCRExtractionParamEnhancedEyesAndMouthLocalizationSymbolLoc.ptr
- _getFCRExtractionParamExtractBlinkSymbolLoc.ptr
- _getFCRExtractionParamExtractFaceprintSymbolLoc.ptr
- _getFCRExtractionParamExtractLandmarkPointsSymbolLoc.ptr
- _getFCRExtractionParamExtractSmileSymbolLoc.ptr
- _getFCRExtractionParamInitialAngleSymbolLoc.ptr
- _getFCRFaceExpressionLeftEyeClosed
- _getFCRFaceExpressionLeftEyeClosed.cold.1
- _getFCRFaceExpressionLeftEyeClosedScoreSymbolLoc.ptr
- _getFCRFaceExpressionLeftEyeClosedSymbolLoc.ptr
- _getFCRFaceExpressionRightEyeClosed
- _getFCRFaceExpressionRightEyeClosed.cold.1
- _getFCRFaceExpressionRightEyeClosedScoreSymbolLoc.ptr
- _getFCRFaceExpressionRightEyeClosedSymbolLoc.ptr
- _getFCRFaceExpressionSmile
- _getFCRFaceExpressionSmile.cold.1
- _getFCRFaceExpressionSmileScoreSymbolLoc.ptr
- _getFCRFaceExpressionSmileSymbolLoc.ptr
- _getFCRFastFaceDetectionParametersSymbolLoc.ptr
- _getFCRSetupParamNumberOfAnglesSymbolLoc.ptr
- _getFaceCoreDetectorClass.softClass
- _getFaceCoreFaceClass.softClass
- _getFaceCoreImageClass.softClass
- _getVNGeneratePersonSegmentationRequestClass.softClass
- _haarTransform32x32_NEON
- _horzDiff32x32
- _imageTransformInverseForOrientation
- _kBurstDoc_AllImageIdentifiers
- _kBurstDoc_AllImageStats
- _kBurstDoc_BestImageIds
- _kBurstDoc_LogFile
- _kCGImageDestinationEmbedThumbnail
- _kCGImageDestinationUseHardwareAcceleration
- _kCIBurstDisableAnalysis
- _kCIBurstDisableFaceCore
- _kCIBurstDummyAnalysis
- _kCIBurstDumpYUV
- _kCIBurstDumpYUV2
- _kCIBurstFixedImageFilename
- _kCIBurstForceFaceDetection
- _kCIBurstImageProperty_ImageROIGridEndX
- _kCIBurstImageProperty_ImageROIGridEndY
- _kCIBurstImageProperty_ImageROIGridStartX
- _kCIBurstImageProperty_ImageROIGridStartY
- _kCIBurstImageSet_VersionString
- _kCIBurstLoggingDefaultsWrite
- _kCIBurstLoggingDefaultsWrite2
- _kCIBurstMaxNumPendingFrames
- _kCIBurstUseFixedImage
- _kCIBurstUseVersion
- _kCIVNLandmarkFace
- _kCIVNLandmarkFaceContour
- _kCIVNLandmarkInnerLips
- _kCIVNLandmarkLeftEyebrow
- _kCIVNLandmarkLeftPupil
- _kCIVNLandmarkMedianLine
- _kCIVNLandmarkNose
- _kCIVNLandmarkNoseCrest
- _kCIVNLandmarkPropsJunkiness
- _kCIVNLandmarkPropsOrientation
- _kCIVNLandmarkRightEyebrow
- _kCIVNLandmarkRightPupil
- _kCVPixelFormatOpenGLESCompatibility
- _loadACBS
- _loadACBS.cold.1
- _objc_msgSend$AEAverage
- _objc_msgSend$AEStable
- _objc_msgSend$AETarget
- _objc_msgSend$AFStable
- _objc_msgSend$Cbuffer
- _objc_msgSend$FCRBlinkFeaturesSize
- _objc_msgSend$FCRLeftEyeFeaturesOffset
- _objc_msgSend$FCRRightEyeFeaturesOffset
- _objc_msgSend$FCRSmileFeaturesOffset
- _objc_msgSend$FCRSmileFeaturesSize
- _objc_msgSend$Ybuffer
- _objc_msgSend$_imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:
- _objc_msgSend$_initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:
- _objc_msgSend$actionAmount
- _objc_msgSend$actionClusteringScore
- _objc_msgSend$actionScore
- _objc_msgSend$addFaceToArray:
- _objc_msgSend$addFacesToImageStat:imageSize:
- _objc_msgSend$addImageFromIOSurface:properties:identifier:completionBlock:
- _objc_msgSend$addItemsFromCluster:
- _objc_msgSend$addScore:
- _objc_msgSend$addYUVImage:properties:identifier:imageProps:completionBlock:
- _objc_msgSend$adjustFaceIdsForImageStat:
- _objc_msgSend$aeMatrix
- _objc_msgSend$allObjects
- _objc_msgSend$allocateMeanStdPingPongBuffers::::
- _objc_msgSend$assignMeanStdBuffers:
- _objc_msgSend$avgHorzDiffY
- _objc_msgSend$bestImageIdentifiers
- _objc_msgSend$bestImageIdentifiersArray
- _objc_msgSend$blurExtent
- _objc_msgSend$burstCoverSelection
- _objc_msgSend$burstDocumentDirectory
- _objc_msgSend$burstId
- _objc_msgSend$burstImages
- _objc_msgSend$burstLogFileName
- _objc_msgSend$calcFaceScores:
- _objc_msgSend$calculateFaceCoreROI:imageStat:needFaceCore:
- _objc_msgSend$calculateFaceFocusInImage:imageStat:
- _objc_msgSend$canRegister
- _objc_msgSend$clusterArray
- _objc_msgSend$collapseSharpnessGrid
- _objc_msgSend$completionBlock
- _objc_msgSend$computeAEMatrix:
- _objc_msgSend$computeAEMatrixDifference:
- _objc_msgSend$computeActionSelectionThreshold
- _objc_msgSend$computeAllImageScores
- _objc_msgSend$computeAverage
- _objc_msgSend$computeBeginningVsEndAEMatrixDiffVsAverageAdjacent
- _objc_msgSend$computeBlurStatsOnGrid:
- _objc_msgSend$computeCameraTravelDistance
- _objc_msgSend$computeEmotion:
- _objc_msgSend$computeFacialFocusScoreSum
- _objc_msgSend$computeImageColorHistogram:
- _objc_msgSend$computeImageData:faceIDCounts:
- _objc_msgSend$computeImageDistance:
- _objc_msgSend$computeImageProjections:
- _objc_msgSend$computeImageSharpnessOnGrid:
- _objc_msgSend$computeKernelValueWithSupportVector:
- _objc_msgSend$computeScore:
- _objc_msgSend$computeSmoothedGridROI:nextStat:
- _objc_msgSend$computeStandardDeviation
- _objc_msgSend$convertRGBAToYUV420:rgbaBytesPerRow:
- _objc_msgSend$countForObject:
- _objc_msgSend$dataWithContentsOfFile:options:error:
- _objc_msgSend$defaultVersionString
- _objc_msgSend$detectFacesInImage:options:error:
- _objc_msgSend$dictionaryWithContentsOfFile:
- _objc_msgSend$dictionaryWithObjectsAndKeys:
- _objc_msgSend$dividerScore
- _objc_msgSend$doLimitedSharpnessAndBlur
- _objc_msgSend$dummyAnalysisCount
- _objc_msgSend$dumpFaceInfoArray
- _objc_msgSend$emotionallyRejected
- _objc_msgSend$enableAnalysis
- _objc_msgSend$enableDumpYUV
- _objc_msgSend$enableFaceCore
- _objc_msgSend$expressionFeatures
- _objc_msgSend$extractDetailsForFaces:inImage:options:error:
- _objc_msgSend$extractFacesFromMetadata:
- _objc_msgSend$face
- _objc_msgSend$faceDetectorWithOptions:
- _objc_msgSend$faceId
- _objc_msgSend$faceRect
- _objc_msgSend$faceScore
- _objc_msgSend$faceStatArray
- _objc_msgSend$facesRoiRect
- _objc_msgSend$findBestImage:useActionScores:
- _objc_msgSend$findFacesInImage:imageStat:
- _objc_msgSend$findOverlappingFaceStat:imageStat:
- _objc_msgSend$firstObject
- _objc_msgSend$flagAsGarbage
- _objc_msgSend$focusScore
- _objc_msgSend$forceFaceDetectionEnable
- _objc_msgSend$foundByFaceCore
- _objc_msgSend$framesSinceLast
- _objc_msgSend$fullsizeJpegData
- _objc_msgSend$getSharpnessAndBlurLimits
- _objc_msgSend$hasLeftEye
- _objc_msgSend$hasRegistrationData
- _objc_msgSend$hasRightEye
- _objc_msgSend$hasRollAngle
- _objc_msgSend$hasYawAngle
- _objc_msgSend$highNoiseThreshold
- _objc_msgSend$hwCenter
- _objc_msgSend$hwFaceId
- _objc_msgSend$hwFaceRect
- _objc_msgSend$hwLastFrameSeen
- _objc_msgSend$hwSize
- _objc_msgSend$image
- _objc_msgSend$imageClusterForIdentifier:
- _objc_msgSend$imageId
- _objc_msgSend$imageProps
- _objc_msgSend$imageScore
- _objc_msgSend$initWithCGImage:
- _objc_msgSend$initWithCGImage:maxDimension:
- _objc_msgSend$initWithFaceStat:
- _objc_msgSend$initWithIOSurface:maxDimension:
- _objc_msgSend$initWithIdentifier:
- _objc_msgSend$initWithImageData:dict:identifier:imageProps:completionBlock:
- _objc_msgSend$initWithRect:withFaceId:
- _objc_msgSend$initWithScore:
- _objc_msgSend$initWithSurface:texture:digest:allowSRGB:bounds:context:
- _objc_msgSend$initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:
- _objc_msgSend$initWithSurface:texture:digest:allowSRGB:bounds:roiTileIndex:roiTileCount:context:
- _objc_msgSend$initWithVersion:
- _objc_msgSend$initWithWidth:height:bytesPerRow:buffer:freeWhenDone:
- _objc_msgSend$isAction
- _objc_msgSend$isBurstAction
- _objc_msgSend$isFaceDetectionForced
- _objc_msgSend$isGarbage
- _objc_msgSend$isPortrait
- _objc_msgSend$isSyncedWithImage
- _objc_msgSend$latestFaceTimestamp
- _objc_msgSend$leftEyeBlinkScore
- _objc_msgSend$leftEyeOpen
- _objc_msgSend$leftEyeRect
- _objc_msgSend$leftImage
- _objc_msgSend$matteType
- _objc_msgSend$maxNumPendingFrames
- _objc_msgSend$maxSkewness
- _objc_msgSend$noiseThreshold
- _objc_msgSend$normalizedFaceRect
- _objc_msgSend$normalizedFocusScore
- _objc_msgSend$normalizedSigma
- _objc_msgSend$numHWFaces
- _objc_msgSend$orientation
- _objc_msgSend$overlapWithHwRect:
- _objc_msgSend$overlapWithSwRect:
- _objc_msgSend$padRoiRect:paddingX:paddingY:
- _objc_msgSend$performEmotionalRejectionOnCluster:
- _objc_msgSend$performRegistration:deltaCol:deltaRow:
- _objc_msgSend$performSelector:withObject:withObject:
- _objc_msgSend$perservesAlpha
- _objc_msgSend$persistentDomainForName:
- _objc_msgSend$predictResult
- _objc_msgSend$processClusters:
- _objc_msgSend$registrationErrorIntegral
- _objc_msgSend$registrationErrorX
- _objc_msgSend$registrationErrorY
- _objc_msgSend$releaseImage
- _objc_msgSend$removeObject:
- _objc_msgSend$rightEyeBlinkScore
- _objc_msgSend$rightEyeOpen
- _objc_msgSend$rightEyeRect
- _objc_msgSend$roiSize
- _objc_msgSend$rollAngle
- _objc_msgSend$scaleVector
- _objc_msgSend$secondsSinceStart
- _objc_msgSend$selectCoverPhotoFromMultiple:burstSize:
- _objc_msgSend$setAEAverage:
- _objc_msgSend$setAEDelta:
- _objc_msgSend$setAEMatrix:
- _objc_msgSend$setAEStable:
- _objc_msgSend$setAETarget:
- _objc_msgSend$setAFStable:
- _objc_msgSend$setActionAmount:
- _objc_msgSend$setActionClusteringScore:
- _objc_msgSend$setActionScore:
- _objc_msgSend$setBestImageIdentifiersArray:
- _objc_msgSend$setBlendBehaviorBit:value:
- _objc_msgSend$setBurstId:
- _objc_msgSend$setCompletionBlock:
- _objc_msgSend$setDividerScore:
- _objc_msgSend$setEmotionallyRejected:
- _objc_msgSend$setExpressionFeatures:
- _objc_msgSend$setFace:
- _objc_msgSend$setFaceAngle:
- _objc_msgSend$setFaceId:
- _objc_msgSend$setFaceSize:
- _objc_msgSend$setFaceType:
- _objc_msgSend$setFacesRoiRect:
- _objc_msgSend$setFocusScore:
- _objc_msgSend$setForceFaceDetectionEnable:
- _objc_msgSend$setFoundByFaceCore:
- _objc_msgSend$setFramesSinceLast:
- _objc_msgSend$setFullsizeJpegData:
- _objc_msgSend$setFullsizeJpegSize:
- _objc_msgSend$setHasLeftEye:
- _objc_msgSend$setHasRegistrationData:
- _objc_msgSend$setHasRightEye:
- _objc_msgSend$setHasRollAngle:
- _objc_msgSend$setHasYawAngle:
- _objc_msgSend$setHighNoiseThreshold:
- _objc_msgSend$setHwCenter:
- _objc_msgSend$setHwFaceId:
- _objc_msgSend$setHwFaceRect:
- _objc_msgSend$setHwLastFrameSeen:
- _objc_msgSend$setHwSize:
- _objc_msgSend$setImage:
- _objc_msgSend$setImageProps:
- _objc_msgSend$setImageScore:
- _objc_msgSend$setIsGarbage:
- _objc_msgSend$setIsSyncedWithImage:
- _objc_msgSend$setLeftEye:
- _objc_msgSend$setLeftEyeBlinkScore:
- _objc_msgSend$setLeftEyeOpen:
- _objc_msgSend$setLeftEyeRect:
- _objc_msgSend$setLeftImage:
- _objc_msgSend$setMaxSkewness:
- _objc_msgSend$setMouth:
- _objc_msgSend$setNoiseThreshold:
- _objc_msgSend$setNormalizedFaceRect:
- _objc_msgSend$setNormalizedFocusScore:
- _objc_msgSend$setNormalizedSigma:
- _objc_msgSend$setNumHWFaces:
- _objc_msgSend$setOrientation:
- _objc_msgSend$setQualityLevel:
- _objc_msgSend$setRegistrationErrorIntegral:
- _objc_msgSend$setRegistrationErrorX:
- _objc_msgSend$setRegistrationErrorY:
- _objc_msgSend$setRightEye:
- _objc_msgSend$setRightEyeBlinkScore:
- _objc_msgSend$setRightEyeOpen:
- _objc_msgSend$setRightEyeRect:
- _objc_msgSend$setRollAngle:
- _objc_msgSend$setSmileScore:
- _objc_msgSend$setSmiling:
- _objc_msgSend$setSvmParameters:
- _objc_msgSend$setSwCenter:
- _objc_msgSend$setSwFaceId:
- _objc_msgSend$setSwLastFrameSeen:
- _objc_msgSend$setSwSize:
- _objc_msgSend$setTemporalOrder:
- _objc_msgSend$setTestAverageCameraTravelDistance:
- _objc_msgSend$setTestAverageRegistrationErrorSkewness:
- _objc_msgSend$setTestBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix:
- _objc_msgSend$setTestInOutRatio:
- _objc_msgSend$setTestMaxInnerDistance:
- _objc_msgSend$setTestMaxPeakRegistrationError:
- _objc_msgSend$setTestMaxRegistrationErrorIntegral:
- _objc_msgSend$setTestMaxRegistrationErrorSkewness:
- _objc_msgSend$setTestMeanPeakRegistrationError:
- _objc_msgSend$setTestMinRegionOfInterestSize:
- _objc_msgSend$setTimeBlinkDetectionDone:
- _objc_msgSend$setTimeFaceDetectionDone:
- _objc_msgSend$setTimeReceived:
- _objc_msgSend$setTrueLocalMaximum:
- _objc_msgSend$setTx:
- _objc_msgSend$setTy:
- _objc_msgSend$setVersion:
- _objc_msgSend$setVersionString:
- _objc_msgSend$setYawAngle:
- _objc_msgSend$setupFaceDetector
- _objc_msgSend$smallFace
- _objc_msgSend$smileScore
- _objc_msgSend$smiling
- _objc_msgSend$statsByImageIdentifier
- _objc_msgSend$statsForImageWithIdentifier:
- _objc_msgSend$stringByAppendingPathComponent:
- _objc_msgSend$stringByAppendingPathExtension:
- _objc_msgSend$svmParameters
- _objc_msgSend$swCenter
- _objc_msgSend$swFaceId
- _objc_msgSend$swFaceRect
- _objc_msgSend$swLastFrameSeen
- _objc_msgSend$swSize
- _objc_msgSend$temporalOrder
- _objc_msgSend$testAverageRegistrationErrorSkewness
- _objc_msgSend$testMaxPeakRegistrationError
- _objc_msgSend$testMaxRegistrationErrorIntegral
- _objc_msgSend$testMaxRegistrationErrorSkewness
- _objc_msgSend$testMeanPeakRegistrationError
- _objc_msgSend$testMinRegionOfInterestSize
- _objc_msgSend$timeBlinkDetectionDone
- _objc_msgSend$timeFaceDetectionDone
- _objc_msgSend$tx
- _objc_msgSend$ty
- _objc_msgSend$updateROI:
- _objc_msgSend$value:withObjCType:
- _objc_msgSend$version
- _objc_msgSend$versionString
- _objc_msgSend$writeGridROI:
- _objc_msgSend$yawAngle
- _perfInit
- _providerGetBytePointerCallback
- _providerGetBytePointerCallback.cold.1
- _providerGetBytesAtPositionCallback_1C08_surface
- _providerGetBytesAtPositionCallback_1C08_surface.cold.1
- _providerGetBytesAtPositionCallback_1C08_surface.cold.2
- _providerGetBytesAtPositionCallback_1C0f_surface
- _providerGetBytesAtPositionCallback_1C0f_surface.cold.1
- _providerGetBytesAtPositionCallback_1C0f_surface.cold.2
- _providerGetBytesAtPositionCallback_1C0h_surface
- _providerGetBytesAtPositionCallback_1C0h_surface.cold.1
- _providerGetBytesAtPositionCallback_1C0h_surface.cold.2
- _providerGetBytesAtPositionCallback_1C0h_surface_lut
- _providerGetBytesAtPositionCallback_1C0h_surface_lut.cold.1
- _providerGetBytesAtPositionCallback_1C0h_surface_lut.cold.2
- _providerGetBytesAtPositionCallback_1C16_surface
- _providerGetBytesAtPositionCallback_1C16_surface.cold.1
- _providerGetBytesAtPositionCallback_1C16_surface.cold.2
- _providerGetBytesAtPositionCallback_2C08_surface
- _providerGetBytesAtPositionCallback_2C08_surface.cold.1
- _providerGetBytesAtPositionCallback_2C08_surface.cold.2
- _providerGetBytesAtPositionCallback_2C0f_surface
- _providerGetBytesAtPositionCallback_2C0f_surface.cold.1
- _providerGetBytesAtPositionCallback_2C0f_surface.cold.2
- _providerGetBytesAtPositionCallback_2C0h_surface
- _providerGetBytesAtPositionCallback_2C0h_surface.cold.1
- _providerGetBytesAtPositionCallback_2C0h_surface.cold.2
- _providerGetBytesAtPositionCallback_2C16_surface
- _providerGetBytesAtPositionCallback_2C16_surface.cold.1
- _providerGetBytesAtPositionCallback_2C16_surface.cold.2
- _providerGetBytesAtPositionCallback_A008_surface
- _providerGetBytesAtPositionCallback_A008_surface.cold.1
- _providerGetBytesAtPositionCallback_A008_surface.cold.2
- _providerGetBytesAtPositionCallback_AYCbCr8_surface
- _providerGetBytesAtPositionCallback_AYCbCr8_surface.cold.1
- _providerGetBytesAtPositionCallback_AYCbCr8_surface.cold.2
- _providerGetBytesAtPositionCallback_CbYCrYFull_surface
- _providerGetBytesAtPositionCallback_CbYCrYFull_surface.cold.1
- _providerGetBytesAtPositionCallback_CbYCrYFull_surface.cold.2
- _providerGetBytesAtPositionCallback_CbYCrY_surface
- _providerGetBytesAtPositionCallback_CbYCrY_surface.cold.1
- _providerGetBytesAtPositionCallback_CbYCrY_surface.cold.2
- _providerGetBytesAtPositionCallback_YCbYCrFull_surface
- _providerGetBytesAtPositionCallback_YCbYCrFull_surface.cold.1
- _providerGetBytesAtPositionCallback_YCbYCrFull_surface.cold.2
- _providerGetBytesAtPositionCallback_YCbYCr_surface
- _providerGetBytesAtPositionCallback_YCbYCr_surface.cold.1
- _providerGetBytesAtPositionCallback_YCbYCr_surface.cold.2
- _providerGetBytesAtPositionCallback_l10r_surface
- _providerGetBytesAtPositionCallback_l10r_surface.cold.1
- _providerGetBytesAtPositionCallback_l10r_surface.cold.2
- _providerGetBytesAtPositionCallback_w30r_surface
- _providerGetBytesAtPositionCallback_w30r_surface.cold.1
- _providerGetBytesAtPositionCallback_w30r_surface.cold.2
- _providerGetBytesAtPositionCallback_w40a_surface
- _providerGetBytesAtPositionCallback_w40a_surface.cold.1
- _providerGetBytesAtPositionCallback_w40a_surface.cold.2
- _providerReleaseBytePointerCallback
- _providerReleaseBytePointerCallback.cold.1
- _ruleOfThirdsX
- _ruleOfThirdsY
- _scaledBins
- _syslog
- _testBinaryArchive
- _testBinaryArchive.cold.1
- _timebase
- _timestampToSeconds
- _updateBlurStatsOne16x16
- _vDSP_dotpr
- _vDSP_vabs
- _vDSP_vflt32
- _vDSP_vsbsm
- _vDSP_vsmsa
- _vDSP_vsub
- _zcalloc
- _zfree
- _zmalloc
CStrings:
+ "\n "
+ "\n    preservesOpacity"
+ "\n// nid:%d type:%s leaf:%d\n"
+ "\ncompileTime=%.3fms waited=%0.3fms%s"
+ " \n// Copyright 2022 Apple, Inc.\n//\n// Standard Library for Core Image Kernels Language.\n//\n// A shell script phase converts this file to the derived source file \"fosl/ci_stdlib.h\"\n//\n\n// For each component, returns x < 0 ? y : z.\nvec4  compare (vec4 x, vec4 y, vec4 z)    { return mix(y, z, step(0.0,x)); }\nvec3  compare (vec3 x, vec3 y, vec3 z)    { return mix(y, z, step(0.0,x)); }\nvec2  compare (vec2 x, vec2 y, vec2 z)    { return mix(y, z, step(0.0,x)); }\nfloat compare (float x, float y, float z) { return x < 0.0 ? y : z; }\n\n// Similar to cos (x) except that x must be in the [–pi, pi] range.\nvec4  cos_ (vec4 x)  { return cos(x); }\nvec3  cos_ (vec3 x)  { return cos(x); }\nvec2  cos_ (vec2 x)  { return cos(x); }\nfloat cos_ (float x) { return cos(x); }\n\n// Similar to sin (x) except that x must be in the [–pi, pi] range.\nvec4  sin_ (vec4 x)  { return sin(x); }\nvec3  sin_ (vec3 x)  { return sin(x); }\nvec2  sin_ (vec2 x)  { return sin(x); }\nfloat sin_ (float x) { return sin(x); }\n\n// Similar to tan (x) except that x must be in the [–pi, pi] range.\nvec4  tan_ (vec4 x)  { return tan(x); }\nvec3  tan_ (vec3 x)  { return tan(x); }\nvec2  tan_ (vec2 x)  { return tan(x); }\nfloat tan_ (float x) { return tan(x); }\n\n// Returns vec2 (cos (x), sin (x)).\nvec2 cossin (float x) { return vec2(cos(x), sin(x)); }\n\n// Returns vec2 (cos_ (x), sin_ (x)).\nvec2 cossin_ (float x) { return vec2(cos_(x), sin_(x)); }\n\n// Returns vec2 (sin (x), cos (x)).\nvec2 sincos (float x) { return vec2(sin(x), cos(x)); }\n\n// Returns vec2 (sin_ (x), cos_ (x)).\nvec2 sincos_ (float x) { return vec2(sin_(x), cos_(x)); }\n\n// Multiplies the red, green, and blue components of the color parameter by its alpha component.\nvec4 premultiply (vec4 s) { return vec4(s.rgb*s.a, s.a); }\nhvec4 premultiply (hvec4 s) { return hvec4(s.rgb*s.a, s.a); }\n\n// If the alpha component of the color parameter is greater than 0, divides the red, green and blue components by alpha. If alpha is 0, this function returns color.\nvec4 unpremultiply (vec4 s) { return vec4(s.rgb/max(s.a,0.00001), s.a); }\nhvec4 unpremultiply (hvec4 s) { return hvec4(s.rgb/max(s.a,0.0001h), s.a); }\n\n// Converts a color from sRGB tone curve to linear.\nvec3 srgb_to_linear (vec3 s)\n{\n    return sign(s)*mix(abs(s)*0.077399380804954, pow(abs(s)*0.947867298578199 + 0.052132701421801, vec3(2.4)), step(0.04045, abs(s)));\n}\n\nhvec3 srgb_to_linear (hvec3 s)\n{\n    return sign(s)*mix(abs(s)*0.077399380804954h, pow(abs(s)*0.947867298578199h + 0.052132701421801h, hvec3(2.4h)), step(0.04045h, abs(s)));\n}\n\n// Converts a premultiplied color from sRGB tone curve to linear.\nvec4 srgb_to_linear (vec4 s)\n{\n    s = unpremultiply(s);\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*0.077399380804954, pow(abs(s.rgb)*0.947867298578199 + 0.052132701421801, vec3(2.4)), step(0.04045, abs(s.rgb)));\n    return premultiply(s);\n}\n\nhvec4 srgb_to_linear (hvec4 s)\n{\n    s = unpremultiply(s);\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*0.077399380804954h, pow(abs(s.rgb)*0.947867298578199h + 0.052132701421801h, hvec3(2.4h)), step(0.04045h, abs(s.rgb)));\n    return premultiply(s);\n}\n\n// for kIntermediateNeedsSRGBConversion support\nvec4 _srgb_to_linear (vec4 s)\n{\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*0.077399380804954, pow(abs(s.rgb)*0.947867298578199 + 0.052132701421801, vec3(2.4)), step(0.04045, abs(s.rgb)));\n    return s;\n}\n\n// Converts a color from linear to sRGB tone curve.\nvec3 linear_to_srgb (vec3 s)\n{\n    return sign(s)*mix(abs(s)*12.92, pow(abs(s), vec3(0.4166667)) * 1.055 - 0.055, step(0.0031308, abs(s)));\n}\n\nhvec3 linear_to_srgb (hvec3 s)\n{\n    return sign(s)*mix(abs(s)*12.92h, pow(abs(s), hvec3(0.4166667h)) * 1.055h - 0.055h, step(0.0031308h, abs(s)));\n}\n\n// Converts a premultiplied color from linear to sRGB tone curve.\nvec4 linear_to_srgb (vec4 s)\n{\n    s = unpremultiply(s);\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*12.92, pow(abs(s.rgb), vec3(0.4166667)) * 1.055 - 0.055, step(0.0031308, abs(s.rgb)));\n    return premultiply(s);\n}\n\nhvec4 linear_to_srgb (hvec4 s)\n{\n    s = unpremultiply(s);\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*12.92h, pow(abs(s.rgb), hvec3(0.4166667h)) * 1.055h - 0.055h, step(0.0031308h, abs(s.rgb)));\n    return premultiply(s);\n}\n\n// for kIntermediateNeedsSRGBConversion support\nvec4 _linear_to_srgb (vec4 s)\n{\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*12.92, pow(abs(s.rgb), vec3(0.4166667)) * 1.055 - 0.055, step(0.0031308, abs(s.rgb)));\n    return s;\n}\n\n// Returns the position, in working space coordinates, of the pixel currently being computed.\n// The destination space refers to the coordinate space of the image you are rendering.\nvec2 destCoord ()\n{\n    return _dc;\n}\n\n// Simulate a GLSL 4.00+ textureGather call\n// xyzw in counter clockwise order, starting with the sample to the lower left of the queried location\n\n#define _samplerOffset(src, offset) (samplerTransform(src,offset) - samplerTransform(src,vec2(0.0)))\n\n//TODO: Need to snap 'point' to nearest 2x2 pixel grid center, since samplers may not be using nearest filtering.\n\nvec4 gatherX (sampler src, vec2 point)\n{\n    vec4 r = vec4(\n        sample(src, point+_samplerOffset(src,vec2(-0.5,-0.5))).x,\n        sample(src, point+_samplerOffset(src,vec2( 0.5,-0.5))).x,\n        sample(src, point+_samplerOffset(src,vec2( 0.5, 0.5))).x,\n        sample(src, point+_samplerOffset(src,vec2(-0.5, 0.5))).x);\n    return r;\n}\n\nvec4 gatherY (sampler src, vec2 point)\n{\n    vec4 r = vec4(\n        sample(src, point+_samplerOffset(src,vec2(-0.5,-0.5))).y,\n        sample(src, point+_samplerOffset(src,vec2( 0.5,-0.5))).y,\n        sample(src, point+_samplerOffset(src,vec2( 0.5, 0.5))).y,\n        sample(src, point+_samplerOffset(src,vec2(-0.5, 0.5))).y);\n    return r;\n}\n\nvec4 gatherZ (sampler src, vec2 point)\n{\n    vec4 r = vec4(\n        sample(src, point+_samplerOffset(src,vec2(-0.5,-0.5))).z,\n        sample(src, point+_samplerOffset(src,vec2( 0.5,-0.5))).z,\n        sample(src, point+_samplerOffset(src,vec2( 0.5, 0.5))).z,\n        sample(src, point+_samplerOffset(src,vec2(-0.5, 0.5))).z);\n    return r;\n}\n\nvec4 gatherW (sampler src, vec2 point)\n{\n    vec4 r = vec4(\n        sample(src, point+_samplerOffset(src,vec2(-0.5,-0.5))).w,\n        sample(src, point+_samplerOffset(src,vec2( 0.5,-0.5))).w,\n        sample(src, point+_samplerOffset(src,vec2( 0.5, 0.5))).w,\n        sample(src, point+_samplerOffset(src,vec2(-0.5, 0.5))).w);\n    return r;\n}\n\n// Equivalent to gather{X|Y|Z|W}\n#define _unordered_gatherX(src, point) gatherX(src, point)\n#define _unordered_gatherY(src, point) gatherY(src, point)\n#define _unordered_gatherZ(src, point) gatherZ(src, point)\n#define _unordered_gatherW(src, point) gatherW(src, point)\n\n// Equivalent to samplerExtent (src).xy.\n#define samplerOrigin(src) samplerExtent(src).xy\n\n// Equivalent to samplerExtent (src).zw.\n#define samplerSize(src) samplerExtent(src).zw\n\n// Stubs for compute kernels compiled with Fosl (to be replaced with context-dependent implementations, post-Fosl codegen)\nvoid writeImage (vec4 color, vec2 point) {}\nvoid writeImagePlane (vec4 color, vec2 point) {}\nvec2 writeCoord () { return vec2(0.0); }\n\n// Rename some (C++) reserved keywords to avoid conflict with Metal shading language\n#define new _new\n#define delete _delete\n#define and _and\n#define not _not\n#define or _or\n#define xor _xor\n "
+ "    priority: media\n"
+ "    sample(s, p+_samplerOffset(s,vec2( 0.5, 0.5))).w,\n"
+ "    sample(s, p+_samplerOffset(s,vec2( 0.5, 0.5))).x,\n"
+ "    sample(s, p+_samplerOffset(s,vec2( 0.5, 0.5))).y,\n"
+ "    sample(s, p+_samplerOffset(s,vec2( 0.5, 0.5))).z,\n"
+ "    sample(s, p+_samplerOffset(s,vec2( 0.5,-0.5))).w,\n"
+ "    sample(s, p+_samplerOffset(s,vec2( 0.5,-0.5))).x,\n"
+ "    sample(s, p+_samplerOffset(s,vec2( 0.5,-0.5))).y,\n"
+ "    sample(s, p+_samplerOffset(s,vec2( 0.5,-0.5))).z,\n"
+ "    sample(s, p+_samplerOffset(s,vec2(-0.5, 0.5))).w);\n"
+ "    sample(s, p+_samplerOffset(s,vec2(-0.5, 0.5))).x);\n"
+ "    sample(s, p+_samplerOffset(s,vec2(-0.5, 0.5))).y);\n"
+ "    sample(s, p+_samplerOffset(s,vec2(-0.5, 0.5))).z);\n"
+ "    sample(s, p+_samplerOffset(s,vec2(-0.5,-0.5))).w,\n"
+ "    sample(s, p+_samplerOffset(s,vec2(-0.5,-0.5))).x,\n"
+ "    sample(s, p+_samplerOffset(s,vec2(-0.5,-0.5))).y,\n"
+ "    sample(s, p+_samplerOffset(s,vec2(-0.5,-0.5))).z,\n"
+ "  _dc = _%ddc;\n"
+ "  _dc = p0;\n"
+ "  gl_FragColor= vec4(_%d);\n"
+ "  highp vec3 p = vec3(c, 1.0) * m;\n"
+ "  return vec4(\n"
+ "  return vec4(%s(Y, p.xy).r, %s(cc, f * p.xy).rg, 1.0);\n"
+ "  vec2 "
+ "  vec4 _%d = %s("
+ "  vec4 _%d = _%d; // %s\n"
+ "  vec4 _%d = _%d; //? %s\n"
+ "  vec4 _%d = _read_pixel(_i%d, _dc, _t%d);\n"
+ "  vec4 _%d = _read_pixel_420(_i%d, _i%d, _dc, _u%d, _t%d);\n"
+ " %zu mpixels"
+ " (%dMB)"
+ " and"
+ " child:%d"
+ " extent exceeds maximum area of %d x %d"
+ " extent:"
+ " filled=%dMP"
+ " it uses an incompatible kernel"
+ " lightlevel=%.3f"
+ " outputFormat"
+ " peakTiles="
+ " pixels=%dMP"
+ "#define _samplerOffset(src, offset) (samplerTransform(src,offset) - samplerTransform(src,vec2(0.0)))\n"
+ "#define half float\n"
+ "#define hmat2 mat2\n"
+ "#define hmat3 mat3\n"
+ "#define hmat4 mat4\n"
+ "#define hsampler int\n"
+ "#define hsampler2D sampler2D\n"
+ "#define hvec2 vec2\n"
+ "#define hvec3 vec3\n"
+ "#define hvec4 vec4\n"
+ "#define kernel\n"
+ "#define sampler int\n"
+ "%@%@"
+ "%@%@__%zu"
+ "%@:%@"
+ "%@__%zu"
+ "%clightlevel=%.3f"
+ "%conlyMetal"
+ "%s outputFormat=%s"
+ "%s | cb:%p [%u, %u]"
+ "%s%d"
+ "%{public}@: area width or height is greater than 32768\n"
+ "%{public}@: inputExtent and inputImage.extent are infinite.\n"
+ "%{public}@: inputExtent is empty.\n"
+ "%{public}@: inputExtent is nil or empty.\n"
+ "%{public}@: requires inputCount >= 1 and <= 2048\n"
+ "%{public}@: requires inputCount >= 1 and <= 256\n"
+ "%{public}s\n%{public}s"
+ "%{public}s  is deprecated."
+ "%{public}s Both surface and texture are nil."
+ "%{public}s Unable to load Quagga.framework."
+ "%{public}s a Metal-only CIProcessorInput cannot be accessed via an IOSurface."
+ "%{public}s a Metal-only CIProcessorOutput cannot be accessed via an IOSurface."
+ "%{public}s a Metal-only CIProcessorOutput cannot be accessed via its base address."
+ "%{public}s argument is not an AVDepthData object."
+ "%{public}s failed to add %{public}@ to the PhotoCompressionSession. (%{public}s)"
+ "%{public}s failed to add alpha channel to the image to the PhotoCompressionSession. (%{public}s)"
+ "%{public}s failed to add depth map to the PhotoCompressionSession. (%{public}s)"
+ "%{public}s failed to add image to the PhotoCompressionSession. (%{public}s)"
+ "%{public}s failed to close the PhotoCompressionSession. (%{public}s)"
+ "%{public}s failed to open the PhotoCompressionSession. (%{public}s)"
+ "%{public}s is deprecated.%{public}s"
+ "%{public}s kernel '%{public}s' specified 'preservesOpacity' but extent is not the same as the extent of the first input image."
+ "%{public}s kernel '%{public}s' specified 'preservesOpacity' but has no inputs."
+ ");\n"
+ "+[CIBarcodeDetector messageStringFromDescriptor:]"
+ "+[CIImage(CIImageProcessor) imageWithExtent:processorDescription:argumentDigest:outputFormat:options:processor:]"
+ "+[CIImageProcessorKernel applyWithExtents:inputs:arguments:error:]"
+ "+[CIImageProcessorKernel processWithInputs:arguments:outputs:error:]"
+ "-[CIBlendKernel setIsBackIfForeIsClear:]"
+ "-[CIBlendKernel setIsClearIfBackIsClear:]"
+ "-[CIBlendKernel setIsClearIfForeIsClear:]"
+ "-[CIBlendKernel setIsForeIfBackIsClear:]"
+ "-[CIColorKernel setPerservesAlpha:]"
+ "-[CIContext(CalculateHDRStats) calculateHDRStatsForImage:]"
+ "-[CIContext(ImageRepresentation) _CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:]"
+ "-[CIContext(ImageRepresentation) _addDepthMap:session:imageHandle:options:]"
+ "-[CIContext(ImageRepresentation) _addGainMap:session:imageHandle:containerFormat:options:orientation:]"
+ "-[CIContext(ImageRepresentation) _addPortraitMatte:session:imageHandle:options:]"
+ "-[CIContext(ImageRepresentation) _addSemanticImages:session:imageHandle:options:]"
+ "-[CIImage _imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:constrainedHigh:]"
+ "-[CIImage imageBySettingDepthData:]"
+ "-[CIImage(CIImageProvider) _initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:]"
+ "-[CIImage(CIImageProvider) initWithImageTextureProvider:width:height:format:colorSpace:options:]"
+ "-[CIImageProcessorInOut initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:]"
+ "-[CIImageProcessorInput surface]"
+ "-[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:tileTask:]"
+ "-[CIImageProcessorOutput surface]"
+ "-[CIKernel setPerservesAlpha:]"
+ "-w -D_BUILDING_CORE_IMAGE_LIB_ -D__BUILDING_RUNTIME_COMPILE_HEADER__"
+ ".coerce0"
+ ".gputrace"
+ "/*?*/"
+ "// %d nid:%d %s \n"
+ "// %s\n\n"
+ "// Uber DAG Functions: %s\n"
+ "// Uber DAG Pipeine Not Created\n"
+ "// nid:%d %s failed to convert_to_kernel_node() \n\n"
+ "// uniform %d not handled\n"
+ "/Library/Caches/com.apple.xbs/Sources/CoreImage/Framework/internal/render.cpp"
+ "1566"
+ "16.0"
+ "19"
+ "9.dng"
+ "<tr><td valign='middle' balign='left'><font face='Menlo'>%@</font></td></tr>"
+ "<tr><td valign='middle'><font face='Menlo'>[%@]</font></td></tr>"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"<MTL4BinaryFunction>\"16"
+ "@\"<MTLFunctionHandle>\"24@0:8@\"NSString\"16"
+ "@\"<MTLTexture>\"24@0:8@\"MTLTextureViewDescriptor\"16"
+ "@\"MTLComputePipelineReflection\"16@0:8"
+ "@\"NSMutableString\""
+ "@104@0:8^{__IOSurface=}16^v24Q32B40{CGRect={CGPoint=dd}{CGSize=dd}}44Q76Q84B92^v96"
+ "@136@0:8{CIKernelReflection=ii***{vector<CI::KernelArgumentType, std::allocator<CI::KernelArgumentType>>=^i^i^i}{vector<std::string, std::allocator<std::string>>=^v^v^v}@IiQQBB}16"
+ "@152@0:8{CIKernelReflection=ii***{vector<CI::KernelArgumentType, std::allocator<CI::KernelArgumentType>>=^i^i^i}{vector<std::string, std::allocator<std::string>>=^v^v^v}@IiQQBB}16@136@144"
+ "@32@0:8^{CGColorSpace=}16f24B28"
+ "@60@0:8@16i24B28i32^{CGColorSpace=}36@44^@52"
+ "@72@0:8@?16@?24Q32Q40i48^{CGColorSpace=}52B60@64"
+ "@84@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16@48Q56i64@68@?76"
+ "@88@0:8^{__IOSurface=}16^v24Q32B40{CGRect={CGPoint=dd}{CGSize=dd}}44B76^v80"
+ "@96@0:8^{__IOSurface=}16^v24Q32B40{CGRect={CGPoint=dd}{CGSize=dd}}44B76^v80^v88"
+ "Add __attribute__((preserves_opacity)) to the CIKL source instead."
+ "AlternateOffset"
+ "ArgumentInfoUnknown"
+ "B12@?0I8"
+ "B16@?0r*8"
+ "BaseOffset"
+ "BufferReference%zu"
+ "CFStringRef getkCMPhotoAuxiliaryImageTypeURN_HDRGainMap()"
+ "CFStringRef getkCMPhotoAuxiliaryImageTypeURN_SemanticGlassesMatte()"
+ "CFStringRef getkCMPhotoAuxiliaryImageTypeURN_SemanticHairMatte()"
+ "CFStringRef getkCMPhotoAuxiliaryImageTypeURN_SemanticSkinMatte()"
+ "CFStringRef getkCMPhotoAuxiliaryImageTypeURN_SemanticSkyMatte()"
+ "CFStringRef getkCMPhotoAuxiliaryImageTypeURN_SemanticTeethMatte()"
+ "CFStringRef getkCMPhotoCompressionOption_AuxiliaryImageCustomTypeURN()"
+ "CI::UBERLibrariesQueue"
+ "CIAreaAverageMaximumRed"
+ "CIBarcodeDetector: Unknown CIDetectorAccuracy specified. Ignoring."
+ "CIBlurredRoundedRectangleGenerator"
+ "CICGImageOriginX"
+ "CICGImageOriginY"
+ "CICoreMLModelFilter.mm"
+ "CIFaceCoreDetector.mm"
+ "CIImage Graph"
+ "CIImageAutoAdjustCrop.m"
+ "CIImageProcessor::TextureProvider"
+ "CIRectangleDetector.mm"
+ "CIRenderDestination.captureTraceURL: %{public}@\n"
+ "CIRenderDestination.captureTraceURL: Failed to start capture, error %{public}@"
+ "CIRenderDestination.captureTraceURL: Set METAL_CAPTURE_ENABLED environment variable to 1"
+ "CIRenderDestination.captureTraceURL: existing file at URL cannot be removed"
+ "CIRenderDestination.captureTraceURL: must be a file URL that ends in .gputrace"
+ "CIRoundedQRCodeGenerator"
+ "CISignedDistanceGradientFromRedMask"
+ "CISystemToneMap"
+ "CITextDetector.m"
+ "CITileCacheProcessor"
+ "CIToneMapInternal"
+ "CIUberShader"
+ "CIVNDetector.m"
+ "CIVecMath.h"
+ "CIVisionUtils.m"
+ "CI_ALLOW_UBER_SHADER_COMPILATION"
+ "CI_ARCHIVE_USAGE_MODE"
+ "CI_CACHE_TILE_SIZE"
+ "CI_ENABLE_METAL_FUNCTION_ATTRIBUTES"
+ "CI_ENABLE_UBER_SHADER"
+ "CI_USE_AIR_UBER_SHADER"
+ "CI_WAIT_BEFORE_SWITCHING_TO_UBER"
+ "CMPhotoCompressionSessionAddTmapImageOneShot"
+ "CUIClampHDR"
+ "CUIComputeNormals"
+ "CUIDfDxDfDy"
+ "CUIFWidth"
+ "CUIGatherSDF"
+ "CUIGlassHighlight"
+ "CUIGlassHighlightFromAlpha"
+ "CUIGlassHighlightInternal"
+ "CUIGlow"
+ "CUINarrowBlur15"
+ "CUISDFClamp"
+ "CUISDFFill"
+ "CUIShapeAwareGradientMask"
+ "CUISignedDistanceField"
+ "CUISimplifiedShapeAwareGradientMask"
+ "CalculateHDRStats"
+ "Capture Scope"
+ "CbYCrY16"
+ "Class getFKTextDetectorClass(void)_block_invoke"
+ "CoreImage needs a converter so that %{public}s can be written.\n"
+ "Could not convert from a format supported by the context to the processor's input format (%{public}s)."
+ "Could not convert from processor's output format (%{public}s) to a format supported by the context."
+ "EarlyReturnNode(#0)\n"
+ "Error creating PSO for the uber shader: %@"
+ "Error creating PSO for the uber shader: %@{public}"
+ "Error creating function from library : %@"
+ "Error creating uber shader, invalid number of output textures = : %{public}zu"
+ "Error creating uber wrapper function %{public}@ from library: %{public}@"
+ "Error creating uber wrapper function: %{public}@ from library"
+ "FOSL_DAG_CODEGEN"
+ "Failed creating uber pipeline for %{public}@"
+ "Failed creating virtual function table@"
+ "Failed creating visible function handle for %{public}@"
+ "Failed finding a compatible uber shader"
+ "Failed loading internal binary archive from %{public}@: %{public}@\n"
+ "Failed loading internal library: %{public}@ from %{public}@: %{public}@\n"
+ "Function '%{public}s' has an unsupported type \"sampler2D\" for the parameter '%{public}@'."
+ "GainMapMax"
+ "GainMapMin"
+ "Gamma"
+ "GlassesMatte"
+ "HDRGainMapVersion"
+ "HairMatte"
+ "Holding onto %zu mpixels for %zuMB\n"
+ "Image Processor Block 0"
+ "Image Processor Block 1"
+ "ImageRepresentationPrivate"
+ "MTLFunctionStitchingEarlyReturnNode"
+ "NSString *getkCMPhotoCompressionOption_ApplyTransform()"
+ "NSString *getkCMPhotoCompressionOption_BitDepth()"
+ "NSString *getkCMPhotoCompressionOption_CodecType()"
+ "NSString *getkCMPhotoCompressionOption_ColorSpace()"
+ "NSString *getkCMPhotoCompressionOption_Subsampling()"
+ "No fallback avaiable for incompatible kernel."
+ "OSStatus soft_CMPhotoCompressionSessionAddTmapImageOneShot(CMPhotoCompressionSessionRef, CMItemIndex, CFDictionaryRef, CFDictionaryRef, CFTypeRef, CFDictionaryRef, Boolean, CGImageMetadataRef, CMItemIndex *)"
+ "OpenCL"
+ "Optimized Graph"
+ "OutputTexture%zu"
+ "ProcessorOutput"
+ "ProcessorOutputImage"
+ "ProcessorOutputNode"
+ "Q16@?0r*8"
+ "Q20@?0r*8i16"
+ "RGB10A8-WideGamut"
+ "RGB10A8-WideLinear"
+ "SWContext"
+ "SemanticSegmentationMatteVersion"
+ "SetAverageLightLevelImage"
+ "SetDepthDataImage"
+ "SetHeadroomImage"
+ "Setting contentAverageLightLevel value should be 0 or greater than  0.0."
+ "Setting contentHeadroom value should be 0 or greater than or equal to 1.0."
+ "SkinMatte"
+ "Skipping render as subdivision code computed an empty ROI"
+ "SkyMatte"
+ "Software DAG"
+ "T@\"CIVector\",&,N,VinputAngleSinCos"
+ "T@\"CIVector\",&,N,VinputBounds"
+ "T@\"CIVector\",&,N,VinputContourOpacityBounds"
+ "T@\"CIVector\",&,N,VinputFrame"
+ "T@\"CIVector\",&,N,VinputLightDirection"
+ "T@\"CIVector\",&,N,VinputOpacityBounds"
+ "T@\"CIVector\",&,N,VinputOpaqueEnd"
+ "T@\"MTLComputePipelineReflection\",R"
+ "T@\"NSNumber\",&,N,VinputBiasAmount"
+ "T@\"NSNumber\",&,N,VinputBorderWidth"
+ "T@\"NSNumber\",&,N,VinputChannel"
+ "T@\"NSNumber\",&,N,VinputCurvature"
+ "T@\"NSNumber\",&,N,VinputDisplayHeadroom"
+ "T@\"NSNumber\",&,N,VinputHighlightsTradeOffRatio"
+ "T@\"NSNumber\",&,N,VinputInset"
+ "T@\"NSNumber\",&,N,VinputLength"
+ "T@\"NSNumber\",&,N,VinputMaxDistance"
+ "T@\"NSNumber\",&,N,VinputMinOpacity"
+ "T@\"NSNumber\",&,N,VinputMinimumGammaAdjustment"
+ "T@\"NSNumber\",&,N,VinputMinimumSDRExposure"
+ "T@\"NSNumber\",&,N,VinputOffsetAnchor"
+ "T@\"NSNumber\",&,N,VinputSDFScale"
+ "T@\"NSNumber\",&,N,VinputSDFScaleFactor"
+ "T@\"NSNumber\",&,N,VinputSDFZero"
+ "T@\"NSNumber\",&,N,VinputSDFZeroValue"
+ "T@\"NSNumber\",&,N,VinputSmoothness"
+ "T@\"NSNumber\",&,N,VinputStopAnchor"
+ "T@\"NSNumber\",C,N,VinputAbove"
+ "T@\"NSNumber\",C,N,VinputBelow"
+ "T@\"NSNumber\",C,N,VinputBiasAmount"
+ "T@\"NSNumber\",C,N,VinputMaskOpposite"
+ "T@\"NSNumber\",C,N,VinputMaxComponent"
+ "T@\"NSNumber\",C,N,VinputRadius"
+ "T@\"NSNumber\",C,N,VinputSDFScale"
+ "T@\"NSNumber\",C,N,VinputSDFZero"
+ "T@\"NSString\",&,N,VinputPreferredDynamicRange"
+ "T@\"NSURL\",&,N,VcaptureTraceURL"
+ "TeethMatte"
+ "The CIImage %p will be rendered by %s instead of CPU because%s%s%s."
+ "The inputMeans array contains invalid values."
+ "The number of extents is too large."
+ "TileCacheNode"
+ "TonemapAlternateHDRHeadroom"
+ "TonemapBaseColorIsWorkingColor"
+ "TonemapBaseHDRHeadroom"
+ "TonemapChannelMetadata"
+ "TonemapVersion"
+ "T{?=QQQ},R"
+ "Unable to find a compatible slice for binary archive at %{public}@\n"
+ "WARNING: CoreImage internal function name %{public}s must start with '_'\n"
+ "Warp kernel %s has an unsupported type for the parameter %s"
+ "XRGB16"
+ "XRGBf"
+ "[%{public}@ kernelWithString:] failed because CIKL source cannot be converted to Metal."
+ "[CIKernel initWithString:] failed because the warp kernel '%{public}s' has an unsupported type \"__sample\" for the parameter '%{public}s'."
+ "[CIKernel initWithString:] failed because the warp kernel '%{public}s' has an unsupported type \"sample_h\" for the parameter '%{public}s'."
+ "[CIKernel initWithString:] failed because the warp kernel '%{public}s' has an unsupported type \"sampler2D\" for the parameter '%{public}s'."
+ "[CIKernel kernelsWithString:andCIKernelLibrary:messageLog:] failed because CIKL source cannot be converted to Metal."
+ "^{CGImage=}24@0:8^{CGImage=}16"
+ "^{CGImage=}76@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24i56^{CGColorSpace=}60B68B72"
+ "_%ddc = %s("
+ "_Bool CIV_horizonDetectionFFT(uint8_t *, int, int, int, float *, int)"
+ "_CMPhotoRepresentationOfImage:depth:allowAlpha:containerFormat:colorSpace:options:error:"
+ "__grain"
+ "_addDepthMap:session:imageHandle:options:"
+ "_addGainMap:session:imageHandle:containerFormat:options:orientation:"
+ "_addPortraitMatte:session:imageHandle:options:"
+ "_addSemanticImages:session:imageHandle:options:"
+ "_annon_%d_"
+ "_annon_dest_"
+ "_bin.metallib"
+ "_call_formatForInputAtIndex:arguments:"
+ "_call_outputFormatWithArguments:"
+ "_ch"
+ "_ci_combine_420"
+ "_ci_combine_422"
+ "_ci_combine_444"
+ "_ci_read_pixel_rgb_a"
+ "_ci_swizzle_to_4XX"
+ "_ci_to_rgb_as_r"
+ "_ci_writeSIMD_420"
+ "_ci_writeSIMD_422"
+ "_ci_writeTG_420"
+ "_ci_writeTG_422"
+ "_combine_420"
+ "_combine_422"
+ "_combine_444"
+ "_dotStringRepresentation"
+ "_imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:constrainedHigh:"
+ "_initWithImageProvider::width:height:format:colorSpace:surfaceCache:options:"
+ "_internalFallbackCL"
+ "_onlyMetal"
+ "_originalIOSurface"
+ "_remappingKernel"
+ "_setOriginalSurface:options:"
+ "_simd_420"
+ "_simd_422"
+ "_swizzle_to_4XX"
+ "_tg_420"
+ "_tg_422"
+ "_to_rgb_as_r"
+ "_uber%@"
+ "above"
+ "allocSpanStack: span stack firstChunk could not be allocated"
+ "applyWithExtents:inputs:arguments:error:"
+ "archiveTypeAtURL:device:error:"
+ "areaAverageMaximumRedFilter"
+ "below"
+ "bezier_norm"
+ "beziers_py"
+ "bias_amount"
+ "bind_sampler"
+ "blurredRoundedRectangleGeneratorFilter"
+ "borderWidth"
+ "bufferForContextIntermediateCommitted:"
+ "bufferForContextIntermediateCompleted:"
+ "calculateHDRStatsForCGImage:"
+ "calculateHDRStatsForCVPixelBuffer:"
+ "calculateHDRStatsForIOSurface:"
+ "calculateHDRStatsForImage:"
+ "captureTraceURL"
+ "cdr_scale"
+ "centerSpaceSize"
+ "channel"
+ "ci_ubershader"
+ "ci_ubershader__4"
+ "ci_uberwrapper"
+ "ci_uberwrapper_bin"
+ "coerce"
+ "compileTime=(%0.1fms + %0.1fms) waited=%0.1fms "
+ "contentAverageLightLevel"
+ "contourOpacityBounds"
+ "convert_420f_to_YCC1f"
+ "convert_420fh_to_YCC1fh"
+ "convert_420v_to_YCC1v"
+ "convert_422f_to_YCC1f"
+ "convert_422fh_to_YCC1fh"
+ "convert_422v_to_YCC1v"
+ "convert_444f_to_YCC1f"
+ "convert_444fh_to_YCC1fh"
+ "convert_444v_to_YCC1v"
+ "convert_CYCY16_toYCC1"
+ "convert_CYCY16_to_YCC1"
+ "convert_a2bgr10_to_rgbah"
+ "convert_a2rgb10_to_rgbah"
+ "convert_argb16_to_rgb1h"
+ "convert_argb16_to_rgbah"
+ "convert_argbf_to_rgbah"
+ "convert_r10p_to_rf"
+ "convert_rg10p_to_rgf"
+ "convert_rgba16_to_rgb1h"
+ "convert_rgbaf_to_rgb1h"
+ "convert_rgbah_to_a2bgr10"
+ "convert_rgbah_to_a2rgb10"
+ "converter %s"
+ "coreimage::Destination"
+ "coreimage::Sampler"
+ "coreimage::Sampler_h"
+ "coreimage::destination"
+ "coreimage::sampler"
+ "coreimage::sampler_h"
+ "coreimage_archive"
+ "createCGImage:fromRect:format:colorSpace:deferred:calculateHDRStats:"
+ "csid"
+ "dag"
+ "dfDxdfDyX"
+ "dfdxW"
+ "digraph %@ {\n"
+ "displayHeadroom"
+ "distanceFraction"
+ "distanceFractionFWidth"
+ "distanceGradientFromRedMaskFilter"
+ "drawGroup:frame:"
+ "extentType"
+ "extents objects must be CIVectors of length 4."
+ "extents objects must be finite, integral, and not empty."
+ "float __PQ_InvEOTF(float N, vec2 m, vec3 c) {\n  float mx = m.x;\n  float X = pow(N, mx);\n  float my = m.y;\n  return pow((c.x + (c.y * X)) / (1.0 + (c.z * X)), my);\n}\nfloat __HermiteSpline(float X, float KneeStart, float maxLum) {\n  return (((((((2.0 * X) * X) * X) - ((3 * X) * X)) + 1.0) * KneeStart) + (((((X * X) * X) - ((2 * X) * X)) + X) * (1.0 - KneeStart))) + ((((((-2.0) * X) * X) * X) + ((3 * X) * X)) * maxLum);\n}\nfloat __PQ_EOTF(float N, vec2 m, vec3 c) {\n  float X = pow(N, 1.0 / m.y);\n  return pow(max(X - c.x, 0.0) / (c.y - (c.z * X)), 1.0 / m.x);\n}\nfloat __PQ_EETF(float Y_in, vec2 m, vec3 c, vec4 levels, vec2 minmaxLum, vec2 knee) {\n  float masterPeakInv = levels.x;\n  float masterBlackInv = levels.y;\n  float minLum = minmaxLum.x;\n  float maxLum = minmaxLum.y;\n  float KneeStart = knee.x;\n  float KneeStartScale = knee.y;\n  float E = __PQ_InvEOTF(Y_in / 1e4, m, c);\n  E = (E - masterBlackInv) / (masterPeakInv - masterBlackInv);\n  E = (E < KneeStart) ? E : __HermiteSpline((E - KneeStart) * KneeStartScale, KneeStart, maxLum);\n  E = (E < 0.0) ? minLum : ((E < 1.0) ? (E + ((((minLum * (1 - E)) * (1 - E)) * (1 - E)) * (1 - E))) : E);\n  E = (E * (masterPeakInv - masterBlackInv)) + masterBlackInv;\n  return 1e4 * __PQ_EOTF(E, m, c);\n}\nkernel vec4 _pq_tonemapping(vec4 im, vec2 m, vec3 c, vec4 levels, vec2 minmaxLum, vec2 knee, vec4 lc) {\n  vec4 result = im;\n  float luminance = dot(im.rgb, lc.rgb);\n  if (luminance != 0) {\n    float out_luminance = __PQ_EETF(luminance, m, c, levels, minmaxLum, knee);\n    result.rgb *= out_luminance / luminance;\n  }\n  return result;\n}\n"
+ "float _asgh(float x) {\n  x = abs(x);\n  if (x >= 3.0) return 0.0;\n  if (x < 1e-6) return 1.0;\n  x *= 3.141593e+00;\n  float sinc = sin(x) / x;\n  float asgw = cos(x / 8.0);\n  return (((sinc * asgw) * asgw) * asgw) * asgw;\n}\nkernel vec4 _asgDownH(sampler src, vec4 scale, float z) {\n  vec2 c = destCoord() * scale.xy;\n  vec2 pm1 = vec2(floor(c.x - 0.5) + 0.5, c.y);\n  vec2 pm6 = pm1 - (scale.zw * 5.0);\n  vec2 pm5 = pm1 - (scale.zw * 4.0);\n  vec2 pm4 = pm1 - (scale.zw * 3.0);\n  vec2 pm3 = pm1 - (scale.zw * 2.0);\n  vec2 pm2 = pm1 - (scale.zw * 1.0);\n  vec2 pp1 = pm1 + (scale.zw * 1.0);\n  vec2 pp2 = pm1 + (scale.zw * 2.0);\n  vec2 pp3 = pm1 + (scale.zw * 3.0);\n  vec2 pp4 = pm1 + (scale.zw * 4.0);\n  vec2 pp5 = pm1 + (scale.zw * 5.0);\n  vec2 pp6 = pm1 + (scale.zw * 6.0);\n  vec4 vm6 = sample(src, samplerTransform(src, pm6));\n  vec4 vm5 = sample(src, samplerTransform(src, pm5));\n  vec4 vm4 = sample(src, samplerTransform(src, pm4));\n  vec4 vm3 = sample(src, samplerTransform(src, pm3));\n  vec4 vm2 = sample(src, samplerTransform(src, pm2));\n  vec4 vm1 = sample(src, samplerTransform(src, pm1));\n  vec4 vp1 = sample(src, samplerTransform(src, pp1));\n  vec4 vp2 = sample(src, samplerTransform(src, pp2));\n  vec4 vp3 = sample(src, samplerTransform(src, pp3));\n  vec4 vp4 = sample(src, samplerTransform(src, pp4));\n  vec4 vp5 = sample(src, samplerTransform(src, pp5));\n  vec4 vp6 = sample(src, samplerTransform(src, pp6));\n  float wm6 = _asgh(((pm6.x - c.x) / scale.x) + z);\n  float wm5 = _asgh(((pm5.x - c.x) / scale.x) + z);\n  float wm4 = _asgh(((pm4.x - c.x) / scale.x) + z);\n  float wm3 = _asgh(((pm3.x - c.x) / scale.x) + z);\n  float wm2 = _asgh(((pm2.x - c.x) / scale.x) + z);\n  float wm1 = _asgh(((pm1.x - c.x) / scale.x) + z);\n  float wp1 = _asgh(((pp1.x - c.x) / scale.x) + z);\n  float wp2 = _asgh(((pp2.x - c.x) / scale.x) + z);\n  float wp3 = _asgh(((pp3.x - c.x) / scale.x) + z);\n  float wp4 = _asgh(((pp4.x - c.x) / scale.x) + z);\n  float wp5 = _asgh(((pp5.x - c.x) / scale.x) + z);\n  float wp6 = _asgh(((pp6.x - c.x) / scale.x) + z);\n  float wsum = ((((((((((wm6 + wm5) + wm4) + wm3) + wm2) + wm1) + wp1) + wp2) + wp3) + wp4) + wp5) + wp6;\n  return ((((((((((((wm6 * vm6) + (wm5 * vm5)) + (wm4 * vm4)) + (wm3 * vm3)) + (wm2 * vm2)) + (wm1 * vm1)) + (wp6 * vp6)) + (wp5 * vp5)) + (wp4 * vp4)) + (wp3 * vp3)) + (wp2 * vp2)) + (wp1 * vp1)) / wsum;\n}\n"
+ "float _asgv(float x) {\n  x = abs(x);\n  if (x >= 3.0) return 0.0;\n  if (x < 1e-6) return 1.0;\n  x *= 3.141593e+00;\n  float sinc = sin(x) / x;\n  float asgw = cos(x / 8.0);\n  return (((sinc * asgw) * asgw) * asgw) * asgw;\n}\nkernel vec4 _asgDownV(sampler src, vec4 scale, float z) {\n  vec2 c = destCoord() * scale.xy;\n  vec2 pm1 = vec2(c.x, floor(c.y - 0.5) + 0.5);\n  vec2 pm6 = pm1 - (scale.zw * 5.0);\n  vec2 pm5 = pm1 - (scale.zw * 4.0);\n  vec2 pm4 = pm1 - (scale.zw * 3.0);\n  vec2 pm3 = pm1 - (scale.zw * 2.0);\n  vec2 pm2 = pm1 - (scale.zw * 1.0);\n  vec2 pp1 = pm1 + (scale.zw * 1.0);\n  vec2 pp2 = pm1 + (scale.zw * 2.0);\n  vec2 pp3 = pm1 + (scale.zw * 3.0);\n  vec2 pp4 = pm1 + (scale.zw * 4.0);\n  vec2 pp5 = pm1 + (scale.zw * 5.0);\n  vec2 pp6 = pm1 + (scale.zw * 6.0);\n  vec4 vm6 = sample(src, samplerTransform(src, pm6));\n  vec4 vm5 = sample(src, samplerTransform(src, pm5));\n  vec4 vm4 = sample(src, samplerTransform(src, pm4));\n  vec4 vm3 = sample(src, samplerTransform(src, pm3));\n  vec4 vm2 = sample(src, samplerTransform(src, pm2));\n  vec4 vm1 = sample(src, samplerTransform(src, pm1));\n  vec4 vp1 = sample(src, samplerTransform(src, pp1));\n  vec4 vp2 = sample(src, samplerTransform(src, pp2));\n  vec4 vp3 = sample(src, samplerTransform(src, pp3));\n  vec4 vp4 = sample(src, samplerTransform(src, pp4));\n  vec4 vp5 = sample(src, samplerTransform(src, pp5));\n  vec4 vp6 = sample(src, samplerTransform(src, pp6));\n  float wm6 = _asgv(((pm6.y - c.y) / scale.y) + z);\n  float wm5 = _asgv(((pm5.y - c.y) / scale.y) + z);\n  float wm4 = _asgv(((pm4.y - c.y) / scale.y) + z);\n  float wm3 = _asgv(((pm3.y - c.y) / scale.y) + z);\n  float wm2 = _asgv(((pm2.y - c.y) / scale.y) + z);\n  float wm1 = _asgv(((pm1.y - c.y) / scale.y) + z);\n  float wp1 = _asgv(((pp1.y - c.y) / scale.y) + z);\n  float wp2 = _asgv(((pp2.y - c.y) / scale.y) + z);\n  float wp3 = _asgv(((pp3.y - c.y) / scale.y) + z);\n  float wp4 = _asgv(((pp4.y - c.y) / scale.y) + z);\n  float wp5 = _asgv(((pp5.y - c.y) / scale.y) + z);\n  float wp6 = _asgv(((pp6.y - c.y) / scale.y) + z);\n  float wsum = ((((((((((wm6 + wm5) + wm4) + wm3) + wm2) + wm1) + wp1) + wp2) + wp3) + wp4) + wp5) + wp6;\n  return ((((((((((((wm6 * vm6) + (wm5 * vm5)) + (wm4 * vm4)) + (wm3 * vm3)) + (wm2 * vm2)) + (wm1 * vm1)) + (wp6 * vp6)) + (wp5 * vp5)) + (wp4 * vp4)) + (wp3 * vp3)) + (wp2 * vp2)) + (wp1 * vp1)) / wsum;\n}\n"
+ "float _lanc3h(float x) {\n  x = abs(x);\n  if (x >= 3.0) return 0.0;\n  if (x < 0.001) return 1.0;\n  x *= 3.141593e+00;\n  return ((3.0 * sin(x)) * sin(x / 3.0)) / (x * x);\n}\nkernel vec4 _lanczosDownH(sampler src, vec4 scale) {\n  vec2 c = destCoord() * scale.xy;\n  vec2 pm1 = vec2(floor(c.x - 0.5) + 0.5, c.y);\n  vec2 pm6 = pm1 - (scale.zw * 5.0);\n  vec2 pm5 = pm1 - (scale.zw * 4.0);\n  vec2 pm4 = pm1 - (scale.zw * 3.0);\n  vec2 pm3 = pm1 - (scale.zw * 2.0);\n  vec2 pm2 = pm1 - (scale.zw * 1.0);\n  vec2 pp1 = pm1 + (scale.zw * 1.0);\n  vec2 pp2 = pm1 + (scale.zw * 2.0);\n  vec2 pp3 = pm1 + (scale.zw * 3.0);\n  vec2 pp4 = pm1 + (scale.zw * 4.0);\n  vec2 pp5 = pm1 + (scale.zw * 5.0);\n  vec2 pp6 = pm1 + (scale.zw * 6.0);\n  vec4 vm6 = sample(src, samplerTransform(src, pm6));\n  vec4 vm5 = sample(src, samplerTransform(src, pm5));\n  vec4 vm4 = sample(src, samplerTransform(src, pm4));\n  vec4 vm3 = sample(src, samplerTransform(src, pm3));\n  vec4 vm2 = sample(src, samplerTransform(src, pm2));\n  vec4 vm1 = sample(src, samplerTransform(src, pm1));\n  vec4 vp1 = sample(src, samplerTransform(src, pp1));\n  vec4 vp2 = sample(src, samplerTransform(src, pp2));\n  vec4 vp3 = sample(src, samplerTransform(src, pp3));\n  vec4 vp4 = sample(src, samplerTransform(src, pp4));\n  vec4 vp5 = sample(src, samplerTransform(src, pp5));\n  vec4 vp6 = sample(src, samplerTransform(src, pp6));\n  float wm6 = _lanc3h((pm6.x - c.x) / scale.x);\n  float wm5 = _lanc3h((pm5.x - c.x) / scale.x);\n  float wm4 = _lanc3h((pm4.x - c.x) / scale.x);\n  float wm3 = _lanc3h((pm3.x - c.x) / scale.x);\n  float wm2 = _lanc3h((pm2.x - c.x) / scale.x);\n  float wm1 = _lanc3h((pm1.x - c.x) / scale.x);\n  float wp1 = _lanc3h((pp1.x - c.x) / scale.x);\n  float wp2 = _lanc3h((pp2.x - c.x) / scale.x);\n  float wp3 = _lanc3h((pp3.x - c.x) / scale.x);\n  float wp4 = _lanc3h((pp4.x - c.x) / scale.x);\n  float wp5 = _lanc3h((pp5.x - c.x) / scale.x);\n  float wp6 = _lanc3h((pp6.x - c.x) / scale.x);\n  float wsum = ((((((((((wm6 + wm5) + wm4) + wm3) + wm2) + wm1) + wp1) + wp2) + wp3) + wp4) + wp5) + wp6;\n  return ((((((((((((wm6 * vm6) + (wm5 * vm5)) + (wm4 * vm4)) + (wm3 * vm3)) + (wm2 * vm2)) + (wm1 * vm1)) + (wp6 * vp6)) + (wp5 * vp5)) + (wp4 * vp4)) + (wp3 * vp3)) + (wp2 * vp2)) + (wp1 * vp1)) / wsum;\n}\n"
+ "float _lanc3v(float x) {\n  x = abs(x);\n  if (x >= 3.0) return 0.0;\n  if (x < 0.001) return 1.0;\n  x *= 3.141593e+00;\n  return ((3.0 * sin(x)) * sin(x / 3.0)) / (x * x);\n}\nkernel vec4 _lanczosDownV(sampler src, vec4 scale) {\n  vec2 c = destCoord() * scale.xy;\n  vec2 pm1 = vec2(c.x, floor(c.y - 0.5) + 0.5);\n  vec2 pm6 = pm1 - (scale.zw * 5.0);\n  vec2 pm5 = pm1 - (scale.zw * 4.0);\n  vec2 pm4 = pm1 - (scale.zw * 3.0);\n  vec2 pm3 = pm1 - (scale.zw * 2.0);\n  vec2 pm2 = pm1 - (scale.zw * 1.0);\n  vec2 pp1 = pm1 + (scale.zw * 1.0);\n  vec2 pp2 = pm1 + (scale.zw * 2.0);\n  vec2 pp3 = pm1 + (scale.zw * 3.0);\n  vec2 pp4 = pm1 + (scale.zw * 4.0);\n  vec2 pp5 = pm1 + (scale.zw * 5.0);\n  vec2 pp6 = pm1 + (scale.zw * 6.0);\n  vec4 vm6 = sample(src, samplerTransform(src, pm6));\n  vec4 vm5 = sample(src, samplerTransform(src, pm5));\n  vec4 vm4 = sample(src, samplerTransform(src, pm4));\n  vec4 vm3 = sample(src, samplerTransform(src, pm3));\n  vec4 vm2 = sample(src, samplerTransform(src, pm2));\n  vec4 vm1 = sample(src, samplerTransform(src, pm1));\n  vec4 vp1 = sample(src, samplerTransform(src, pp1));\n  vec4 vp2 = sample(src, samplerTransform(src, pp2));\n  vec4 vp3 = sample(src, samplerTransform(src, pp3));\n  vec4 vp4 = sample(src, samplerTransform(src, pp4));\n  vec4 vp5 = sample(src, samplerTransform(src, pp5));\n  vec4 vp6 = sample(src, samplerTransform(src, pp6));\n  float wm6 = _lanc3v((pm6.y - c.y) / scale.y);\n  float wm5 = _lanc3v((pm5.y - c.y) / scale.y);\n  float wm4 = _lanc3v((pm4.y - c.y) / scale.y);\n  float wm3 = _lanc3v((pm3.y - c.y) / scale.y);\n  float wm2 = _lanc3v((pm2.y - c.y) / scale.y);\n  float wm1 = _lanc3v((pm1.y - c.y) / scale.y);\n  float wp1 = _lanc3v((pp1.y - c.y) / scale.y);\n  float wp2 = _lanc3v((pp2.y - c.y) / scale.y);\n  float wp3 = _lanc3v((pp3.y - c.y) / scale.y);\n  float wp4 = _lanc3v((pp4.y - c.y) / scale.y);\n  float wp5 = _lanc3v((pp5.y - c.y) / scale.y);\n  float wp6 = _lanc3v((pp6.y - c.y) / scale.y);\n  float wsum = ((((((((((wm6 + wm5) + wm4) + wm3) + wm2) + wm1) + wp1) + wp2) + wp3) + wp4) + wp5) + wp6;\n  return ((((((((((((wm6 * vm6) + (wm5 * vm5)) + (wm4 * vm4)) + (wm3 * vm3)) + (wm2 * vm2)) + (wm1 * vm1)) + (wp6 * vp6)) + (wp5 * vp5)) + (wp4 * vp4)) + (wp3 * vp3)) + (wp2 * vp2)) + (wp1 * vp1)) / wsum;\n}\n"
+ "float compare(float x, float y, float z) { return mix(y, z, step(0.0, x)); }\n"
+ "float cos_    (float x) { return cos(x); }\n"
+ "float saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _glassHighlight(vec4 s, vec4 fwidth, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  vec3 sdf = s.xyz;\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((-(sdf.r - sdfZero)) * sdfScale) - inset;\n  vec2 gradient = -((sdf.gb * 2.0) - 1.0);\n  float d_norm = saturate(distance / height);\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  float w = max(fwidth.x, 1e-4);\n  float mask = saturate(0.5 + (distance / w));\n  mask *= saturate(0.5 + ((height - distance) / w));\n  if (distance < (-1.0)) mask = 0.0;\n  float alpha = saturate((dot(light_dir, gradient) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max((bias_amount * (1.0 - alpha)) + 1.0, 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
+ "float saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _glassHighlightFromAlpha(vec4 s, vec4 dfdxW, vec4 values0, vec4 values1, float sdfZero, vec4 color) {\n  float height = values0.x;\n  float inset = values0.y;\n  float spread = values0.z;\n  float bias_amount = values0.w;\n  float curvature = values1.x;\n  vec2 light_dir = values1.yz;\n  float sdfScale = values1.w;\n  float distance = ((s.w - sdfZero) * sdfScale) - inset;\n  float d_norm = max(0.0, min(1.0, distance / height));\n  float h = mix(1.0, 1.0 - d_norm, curvature);\n  float horiz = dfdxW.x;\n  float vert = dfdxW.y;\n  vec2 normal = vec2(horiz, vert);\n  normal /= length(normal);\n  normal *= -1.0;\n  float fwidth = abs(horiz) + abs(vert);\n  float w = max(fwidth, 1e-4);\n  float mask = saturate(0.5 + (distance / w));\n  mask *= saturate(0.5 + ((height - distance) / w));\n  if (distance < (-1.0)) mask = 0.0;\n  float alpha = saturate((dot(light_dir, normal) - spread) / max(1.0 - float(spread), 1e-4));\n  alpha = alpha / max(float((bias_amount * (1.0 - alpha)) + 1.0), 1e-4);\n  color *= (mask * alpha) * h;\n  return color;\n}\n"
+ "float saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _glow(vec4 distanceFraction, vec4 distanceFractionFWidth, float bias_amount, vec4 color) {\n  float v = distanceFraction.x;\n  float strength = exp(((-0.5) * v) * v);\n  strength /= max((bias_amount * (1.0 - strength)) + 1.0, 1e-4);\n  float fwidth = distanceFractionFWidth.x;\n  float w = max(fwidth, 1e-4);\n  float mask = saturate(0.5 + (v / w));\n  color *= strength * mask;\n  return color;\n}\n"
+ "float saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _shapeAwareGradientMask(vec4 s, float borderWidth, float minOpacity, vec2 opaqueEnd, float length, vec3 lightDirection, float sdfScale, float sdfZero) {\n  float distance = (-(s.r - sdfZero)) * sdfScale;\n  float distanceFraction = saturate(distance / borderWidth);\n  float transparency = saturate(dot(lightDirection.xy, opaqueEnd - destCoord()) / length);\n  float transparencyWithContour = mix(1.0 - transparency, transparency, distanceFraction);\n  float withGradient = mix(1.0, minOpacity, transparencyWithContour);\n  withGradient = smoothstep(0.0, 1.0, withGradient);\n  return vec4(withGradient);\n}\n"
+ "float saturate(float a) {\n  return max(0.0, min(1.0, a));\n}\nkernel vec4 _simplifiedShapeAwareGradientMask(vec4 s, float borderWidth, vec2 opacityBounds, vec2 contourOpacityBounds, float sdfScale, float sdfZero, vec4 bounds) {\n  float distance = (-(s.r - sdfZero)) * sdfScale;\n  float distanceFraction = saturate(distance / borderWidth);\n  float verticalDistance = saturate((destCoord().y - bounds.y) / bounds.w);\n  float verticalTransparency = mix(opacityBounds.y, opacityBounds.x, verticalDistance);\n  float verticalContourTransparency = mix(contourOpacityBounds.y, contourOpacityBounds.x, verticalDistance);\n  float transparencyWithContour = mix(verticalContourTransparency, verticalTransparency, distanceFraction);\n  transparencyWithContour = smoothstep(0.0, 1.0, transparencyWithContour);\n  return vec4(transparencyWithContour);\n}\n"
+ "float sin_    (float x) { return sin(x); }\n"
+ "float step_function(float edge, float x) {\n  return (x < edge) ? 0.0 : 1.0;\n}\nvec2 saturate2(vec2 a) {\n  return max(vec2(0.0), min(vec2(1.0), a));\n}\nkernel vec4 _fallbackComputeNormals(vec4 s, vec4 dfDxdfDyX) {\n  float dist = s.x;\n  vec2 gradient = vec2(-dfDxdfDyX.x, dfDxdfDyX.y);\n  float size = length(gradient);\n  vec2 grad_norm = (step_function(size, 1e-4) * gradient) / size;\n  vec4 combined = vec4(dist, saturate2((grad_norm * vec2(0.5)) + vec2(0.5)), 1.0);\n  return combined;\n}\n"
+ "functionHandleWithBinaryFunction:"
+ "functionHandleWithName:"
+ "fwidth"
+ "gainMapImageForSDR:HDR:colorSpace:rgbGainmap:"
+ "getBytesAtPositionCallback_1C08"
+ "getBytesAtPositionCallback_1C08_lut"
+ "getBytesAtPositionCallback_1C0f"
+ "getBytesAtPositionCallback_1C0h"
+ "getBytesAtPositionCallback_1C0h_lut"
+ "getBytesAtPositionCallback_1C16"
+ "getBytesAtPositionCallback_2C08"
+ "getBytesAtPositionCallback_2C0f"
+ "getBytesAtPositionCallback_2C0h"
+ "getBytesAtPositionCallback_2C16"
+ "getBytesAtPositionCallback_A008"
+ "getBytesAtPositionCallback_AYCbCr8"
+ "getBytesAtPositionCallback_CbYCrY"
+ "getBytesAtPositionCallback_CbYCrY16"
+ "getBytesAtPositionCallback_CbYCrYFull"
+ "getBytesAtPositionCallback_YCbYCr"
+ "getBytesAtPositionCallback_YCbYCrFull"
+ "getBytesAtPositionCallback_l10r"
+ "getBytesAtPositionCallback_w30r"
+ "getBytesAtPositionCallback_w40a"
+ "hasFace"
+ "highp vec2 _dc;\n"
+ "http://ns.apple.com/portraitEffectsMatte/1.0/"
+ "http://ns.apple.com/semanticSegmentationMatte/1.0/"
+ "i16@?0i8i12"
+ "i16@?0r*8"
+ "i16@?0r^v8"
+ "i20@?0r*8i16"
+ "i20@?0r^{SerialObjectPtrArray=iii^^{Object}[10^{Object}]}8i16"
+ "i32@?0i8i12r*16^v24"
+ "i8@?0"
+ "ids"
+ "idx<4 && idx>=0"
+ "imageByInsertingTiledIntermediate"
+ "imageBySettingContentAverageLightLevel:"
+ "imageBySettingContentHeadroom:"
+ "imageBySettingDepthData:"
+ "imageWithExtent:processorDescription:argumentDigest:outputFormat:options:processor:"
+ "initWithImageTextureProvider:width:height:format:colorSpace:options:"
+ "initWithName:arguments:controlDependencies:isEarlyReturn:"
+ "initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:"
+ "initWithSurface:texture:digest:allowSRGB:bounds:onlyMetal:context:tileTask:"
+ "initWithSurface:texture:digest:allowSRGB:bounds:roiTileIndex:roiTileCount:onlyMetal:context:"
+ "inputAbove"
+ "inputAngleSinCos"
+ "inputBelow"
+ "inputBiasAmount"
+ "inputBorderWidth"
+ "inputBounds"
+ "inputContourOpacityBounds"
+ "inputCurvature"
+ "inputDisplayHeadroom"
+ "inputFrame"
+ "inputHighlightsTradeOffRatio"
+ "inputInset"
+ "inputLength"
+ "inputLightDirection"
+ "inputMaskOpposite"
+ "inputMaxComponent"
+ "inputMaxDistance"
+ "inputMinOpacity"
+ "inputMinimumGammaAdjustment"
+ "inputMinimumSDRExposure"
+ "inputOffsetAnchor"
+ "inputOpacityBounds"
+ "inputOpaqueEnd"
+ "inputPreferredDynamicRange"
+ "inputSDFScale"
+ "inputSDFScaleFactor"
+ "inputSDFZero"
+ "inputSDFZeroValue"
+ "inputSmoothness"
+ "inputStopAnchor"
+ "int CIV_horizonDetectionFFTAngles(uint8_t *, int, int, int, _Bool, float, int, HorizonDetectedAngle *)"
+ "intemediate-tiled"
+ "internalBinaryArchiveWithName:device:"
+ "isMetalAvailable"
+ "isOpenCLAvailable"
+ "kCICanReduceOutputChannels"
+ "kCIContextIntermediateAllocator"
+ "kCIDynamicRangeConstrainedHigh"
+ "kCIDynamicRangeHigh"
+ "kCIDynamicRangeStandard"
+ "kCIFormatR8"
+ "kCIFormatRG8"
+ "kCIFormatRGBA8"
+ "kCIFormatRGBAh"
+ "kCIFormatRGh"
+ "kCIFormatRh"
+ "kCIImageApplyCleanAperture"
+ "kCIImageContentAverageLightLevel"
+ "kCIImageContentHeadroom option should be 0 or greater than  0.0."
+ "kCIImageProcessorOnlyUsesMetal"
+ "kCIImageRepresentationISOGainMapGamma"
+ "kCIPreservesColorSpace"
+ "kCIPreservesOpacity"
+ "kCIPreservesRange"
+ "kCMBaseObjectError_ValueNotAvailable"
+ "kCMPhotoAuxiliaryImageTypeURN_HDRGainMap"
+ "kCMPhotoAuxiliaryImageTypeURN_SemanticGlassesMatte"
+ "kCMPhotoAuxiliaryImageTypeURN_SemanticHairMatte"
+ "kCMPhotoAuxiliaryImageTypeURN_SemanticSkinMatte"
+ "kCMPhotoAuxiliaryImageTypeURN_SemanticSkyMatte"
+ "kCMPhotoAuxiliaryImageTypeURN_SemanticTeethMatte"
+ "kCMPhotoCompressionOption_ApplyTransform"
+ "kCMPhotoCompressionOption_AuxiliaryImageCustomTypeURN"
+ "kCMPhotoCompressionOption_BitDepth"
+ "kCMPhotoCompressionOption_CodecType"
+ "kCMPhotoCompressionOption_ColorSpace"
+ "kCMPhotoCompressionOption_Subsampling"
+ "kCMPhotoError_AllocationFailed"
+ "kCMPhotoError_FrameDropped"
+ "kCMPhotoError_InternalFailure"
+ "kCMPhotoError_InvalidCropRect"
+ "kCMPhotoError_InvalidData"
+ "kCMPhotoError_InvalidParameter"
+ "kCMPhotoError_InvalidSession"
+ "kCMPhotoError_UnsupportedCodec"
+ "kCMPhotoError_UnsupportedImageType"
+ "kCMPhotoError_UnsupportedOperation"
+ "kCMPhotoError_UnsupportedPixelFormat"
+ "kCMPhotoError_UnsupportedQuality"
+ "kCMPhotoError_UnsupportedSourceType"
+ "kCMPhotoError_UnsupportedTiling"
+ "kCMPhotoError_ValueNotAvailable"
+ "kCMPhotoError_XPCError"
+ "kCVReturnInvalidPixelBufferAttributes"
+ "kCVReturnInvalidPixelFormat"
+ "kCVReturnInvalidSize"
+ "kCVReturnPixelBufferNotMetalCompatible"
+ "kCVReturnPixelBufferNotOpenGLCompatible"
+ "kFigFormatReaderError_ParsingFailure"
+ "kIOReturnMessageTooLarge"
+ "kIOReturnNoFrames"
+ "kIOReturnNoMedia"
+ "kIOReturnNoPower"
+ "kIOReturnNotPermitted"
+ "kVTCouldNotCreateInstanceErr"
+ "kVTCouldNotFindVideoDecoderErr"
+ "kVTCouldNotFindVideoEncoderErr"
+ "kVTParameterErr"
+ "kVTVideoDecoderBadDataErr"
+ "kVTVideoDecoderMalfunctionErr"
+ "kVTVideoDecoderUnsupportedDataFormatErr"
+ "kVTVideoEncoderMalfunctionErr"
+ "kernel __attibute__((preserves_opacity)) is not relevant for kernels without sample or sampler arguments."
+ "kernel vec2 _flashGeom(vec2 center) {\n  vec2 delta = destCoord() - center;\n  float len = length(delta);\n  return ((delta * 100.0) / len) + vec2(1.280000e+02);\n}\n"
+ "kernel vec2 _perspectiveCorrection(vec3 A1, vec3 A2, vec3 A3) {\n  vec3 h = vec3(destCoord(), 1.0);\n  vec2 p = vec2(dot(h, A1), dot(h, A2));\n  return p / max(dot(h, A3), 1e-6);\n}\n"
+ "kernel vec2 _perspectiveTransform(vec3 A1, vec3 A2, vec3 A3, vec2 origin) {\n  vec3 h = vec3(destCoord(), 1.0);\n  vec2 p = vec2(dot(h, A1), dot(h, A2));\n  float w = 1.0 / max(dot(h, A3), 1e-6);\n  return (p * w) + origin;\n}\n"
+ "kernel vec2 _pinchDistortionScaleGE1(vec2 c, vec4 param) {\n  vec2 p = destCoord() - c;\n  float r = (length(p) * param.y) + 1e-6;\n  vec2 pRGT = (pow(r, param.w) * p) + c;\n  p = (p * inversesqrt(r)) + c;\n  p = mix(destCoord(), p, param.z);\n  return (r <= 1.0) ? p : pRGT;\n}\n"
+ "kernel vec2 _pinchDistortionScaleLT1(vec2 c, vec4 param) {\n  vec2 p = destCoord() - c;\n  float r = (length(p) * param.y) + 1e-6;\n  p = (p * inversesqrt(r)) + c;\n  return mix(destCoord(), p, param.z);\n}\n"
+ "kernel vec4 _ACCentroid(vec4 c, vec4 extent) {\n  return vec4(extent.xy + ((c.xy / max(c.z, 1e-4)) * vec2(extent.zw)), 0.0, 1.0);\n}\n"
+ "kernel vec4 _CBHorz(sampler u, float k, float colorInv, float spatialInv) {\n  vec2 dc = destCoord();\n  vec4 u_0 = sample(u, samplerTransform(u, dc));\n  vec4 Cacc = vec4(0.0);\n  float W = 0.0;\n  int kk = int(k);\n  for (int x = -kk; x <= kk; x++) {\n    float ws = exp((-float(x * x)) * spatialInv);\n    vec4 u_xy = sample(u, samplerTransform(u, dc + vec2(x, 0.0)));\n    float r2 = dot(u_xy.rgb - u_0.rgb, u_xy.rgb - u_0.rgb);\n    float wc = exp((-r2) * colorInv);\n    float w = (ws * wc) * u_xy.a;\n    W += w;\n    Cacc += w * u_xy;\n  }\n  return vec4((W < 1e-5) ? u_0.rgb : (Cacc.rgb / W), u_0.a);\n}\n"
+ "kernel vec4 _CBHorzGuided(sampler u, sampler v, float k, float colorInv, float spatialInv) {\n  vec2 dc = destCoord();\n  vec4 u_0 = sample(u, samplerTransform(u, dc));\n  vec4 v_0 = sample(v, samplerTransform(v, dc));\n  vec4 Cacc = vec4(0.0);\n  float W = 0.0;\n  int kk = int(k);\n  for (int x = -kk; x <= kk; x++) {\n    float ws = exp((-float(x * x)) * spatialInv);\n    vec4 u_xy = sample(u, samplerTransform(u, dc + vec2(x, 0.0)));\n    vec4 v_xy = sample(v, samplerTransform(v, dc + vec2(x, 0.0)));\n    float r2 = dot(u_xy.rgb - u_0.rgb, u_xy.rgb - u_0.rgb);\n    float wc = exp((-r2) * colorInv);\n    float w = (ws * wc) * u_xy.a;\n    W += w;\n    Cacc += w * v_xy;\n  }\n  return vec4((W < 1e-5) ? v_0.rgb : (Cacc.rgb / W), v_0.a);\n}\n"
+ "kernel vec4 _CBVert(sampler u, float k, float colorInv, float spatialInv) {\n  vec2 dc = destCoord();\n  vec4 u_0 = sample(u, samplerTransform(u, dc));\n  vec4 Cacc = vec4(0.0);\n  float W = 0.0;\n  int kk = int(k);\n  for (int y = -kk; y <= kk; y++) {\n    float ws = exp((-float(y * y)) * spatialInv);\n    vec4 u_xy = sample(u, samplerTransform(u, dc + vec2(0.0, y)));\n    float r2 = dot(u_xy.rgb - u_0.rgb, u_xy.rgb - u_0.rgb);\n    float wc = exp((-r2) * colorInv);\n    float w = (ws * wc) * u_xy.a;\n    W += w;\n    Cacc += w * u_xy;\n  }\n  return vec4((W < 1e-5) ? u_0.rgb : (Cacc.rgb / W), u_0.a);\n}\n"
+ "kernel vec4 _CBVertGuided(sampler u, sampler v, float k, float colorInv, float spatialInv) {\n  vec2 dc = destCoord();\n  vec4 u_0 = sample(u, samplerTransform(u, dc));\n  vec4 v_0 = sample(v, samplerTransform(v, dc));\n  vec4 Cacc = vec4(0.0);\n  float W = 0.0;\n  int kk = int(k);\n  for (int y = -kk; y <= kk; y++) {\n    float ws = exp((-float(y * y)) * spatialInv);\n    vec4 u_xy = sample(u, samplerTransform(u, dc + vec2(0.0, y)));\n    vec4 v_xy = sample(v, samplerTransform(v, dc + vec2(0.0, y)));\n    float r2 = dot(u_xy.rgb - u_0.rgb, u_xy.rgb - u_0.rgb);\n    float wc = exp((-r2) * colorInv);\n    float w = (ws * wc) * u_xy.a;\n    W += w;\n    Cacc += w * v_xy;\n  }\n  return vec4((W < 1e-5) ? v_0.rgb : (Cacc.rgb / W), v_0.a);\n}\n"
+ "kernel vec4 _CEstretch(vec4 c, vec4 lohi, float amount) {\n  float lov = lohi.r;\n  float hiv = lohi.g;\n  return vec4(mix(c.rgb, clamp((c.rgb - lov) / max(1e-5, hiv - lov), 0.0, 1.0), amount), c.a);\n}\n"
+ "kernel vec4 _CIPortraitBlurDir(sampler image, vec3 params) {\n  vec2 dir = params.yz;\n  vec2 dc = destCoord();\n  vec4 pix0 = sample(image, samplerTransform(image, dc - (3.0 * dir)));\n  vec4 pix1 = sample(image, samplerTransform(image, dc - (2.0 * dir)));\n  vec4 pix2 = sample(image, samplerTransform(image, dc - dir));\n  vec4 pix3 = sample(image, samplerTransform(image, dc));\n  vec4 pix4 = sample(image, samplerTransform(image, dc + dir));\n  vec4 pix5 = sample(image, samplerTransform(image, dc + (2.0 * dir)));\n  vec4 pix6 = sample(image, samplerTransform(image, dc + (3.0 * dir)));\n  float outW = pix3.w;\n  pix0.w = pix0.w * pix0.w;\n  pix1.w = pix1.w * pix1.w;\n  pix2.w = pix2.w * pix2.w;\n  pix3.w = pix3.w * pix3.w;\n  pix4.w = pix4.w * pix4.w;\n  pix5.w = pix5.w * pix5.w;\n  pix6.w = pix6.w * pix6.w;\n  float radius = max(params.x * pix3.w, 0.01);\n  float radius2 = 1.0 / ((2.0 * radius) * radius);\n  float weight0 = 1.0;\n  float weight1 = exp((-1.0) * radius2);\n  float weight2 = ((weight1 * weight1) * weight1) * weight1;\n  float weight3 = (weight2 * weight2) * weight1;\n  float invWeightSum = 1.0 / (((((((pix0.w * weight3) + (pix1.w * weight2)) + (pix2.w * weight1)) + (pix3.w * weight0)) + (pix4.w * weight1)) + (pix5.w * weight2)) + (pix6.w * weight3));\n  weight0 *= invWeightSum;\n  weight1 *= invWeightSum;\n  weight2 *= invWeightSum;\n  weight3 *= invWeightSum;\n  vec4 pixOut;\n  pixOut.xyz = (((((((weight3 * pix0.w) * pix0.xyz) + ((weight2 * pix1.w) * pix1.xyz)) + ((weight1 * pix2.w) * pix2.xyz)) + ((weight0 * pix3.w) * pix3.xyz)) + ((weight1 * pix4.w) * pix4.xyz)) + ((weight2 * pix5.w) * pix5.xyz)) + ((weight3 * pix6.w) * pix6.xyz);\n  pixOut.w = outW;\n  return pixOut;\n}\n"
+ "kernel vec4 _DEWash(vec4 c, vec4 w) {\n  return c / (1e-6 + w);\n}\n"
+ "kernel vec4 _DEnormalizeAlpha(vec4 c) {\n  return (c * smoothstep(0.001, 0.1, c.a)) / max(c.a, 1e-4);\n}\n"
+ "kernel vec4 _LAB_denormalize(vec4 c) {\n  c.r *= 100.0;\n  c.gb = (c.gb - 0.5) * 1.280000e+02;\n  return c;\n}\n"
+ "kernel vec4 _LAB_normalize(vec4 c) {\n  c.r /= 100.0;\n  c.gb = (c.gb / 1.280000e+02) + 0.5;\n  return c;\n}\n"
+ "kernel vec4 _appleLogToLinear(vec4 P) {\n  const float R0 = -5.641088e-02;\n  const float Rt = 0.01;\n  const float c = 4.728711e+01;\n  const float beta = 9.640520e-03;\n  const float gamma = 8.550479e-02;\n  const float delta = 6.933694e-01;\n  const float Pt = (c * (Rt - R0)) * (Rt - R0);\n  vec4 Ra;\n  vec4 Rb = sqrt(P / c) + R0;\n}\n"
+ "kernel vec4 _areaAveMaxRed16(sampler image, vec2 bound, float pass) {\n  vec2 d = 4.0 * destCoord();\n  vec2 am = vec2(0.0, -1.000000e+20);\n  for (float j = -1.500; j < 2.0; j += 1.0) {\n    for (float i = -1.500; i < 2.0; i += 1.0) {\n      vec2 location = d + vec2(i, j);\n      vec4 p = sample(image, samplerTransform(image, location));\n      vec2 v = (pass < 9.000000e-01) ? p.rr : p.rg;\n      if ((location.x < bound.x) && (location.y < bound.y)) am = vec2(v.r + am.r, max(v.g, am.g));\n    }\n  }\n  return vec4(am.r / 16.0, am.g, 0.0, 1.0);\n}\n"
+ "kernel vec4 _areaAveMaxRed4(sampler image, vec2 bound, float pass) {\n  vec2 d = 2.0 * destCoord();\n  vec4 p0 = sample(image, samplerTransform(image, d + vec2(-0.5, -0.5)));\n  vec4 p1 = sample(image, samplerTransform(image, d + vec2(+0.5, -0.5)));\n  vec4 p2 = sample(image, samplerTransform(image, d + vec2(-0.5, +0.5)));\n  vec4 p3 = sample(image, samplerTransform(image, d + vec2(+0.5, +0.5)));\n  vec2 am0 = (pass < 9.000000e-01) ? p0.rr : p0.rg;\n  vec2 am1 = (pass < 9.000000e-01) ? p1.rr : p1.rg;\n  vec2 am2 = (pass < 9.000000e-01) ? p2.rr : p2.rg;\n  vec2 am3 = (pass < 9.000000e-01) ? p3.rr : p3.rg;\n  am0.r = ((d.x + 0.5) < bound.x) ? (am0.r + am1.r) : am0.r;\n  am2.r = ((d.x + 0.5) < bound.x) ? (am2.r + am3.r) : am2.r;\n  am0.r = ((d.y + 0.5) < bound.y) ? (am0.r + am2.r) : am0.r;\n  am0.g = ((d.x + 0.5) < bound.x) ? max(am0.g, am1.g) : am0.g;\n  am2.g = ((d.x + 0.5) < bound.x) ? max(am2.g, am3.g) : am2.g;\n  am0.g = ((d.y + 0.5) < bound.y) ? max(am0.g, am2.g) : am0.g;\n  return vec4(am0.r * 0.25, am0.g, 0.0, 1.0);\n}\n"
+ "kernel vec4 _blurredrect(vec4 bounds, float sigma, vec4 color) {\n  vec2 x, p = destCoord();\n  vec2 lo = bounds.xy;\n  vec2 hi = bounds.zw;\n  sigma *= 2.400;\n  x = clamp((p - (lo - sigma)) / (2.0 * sigma), 0.0, 1.0);\n  vec2 v1 = ((x * x) * x) * ((((6.0 * x) - 1.500000e+01) * x) + 10.0);\n  x = clamp(((hi + sigma) - p) / (2.0 * sigma), 0.0, 1.0);\n  vec2 v2 = ((x * x) * x) * ((((6.0 * x) - 1.500000e+01) * x) + 10.0);\n  return color * (((v1.x * v1.y) * v2.x) * v2.y);\n}\n"
+ "kernel vec4 _blurredroundedrect(vec4 bounds, float radius, vec2 softness, float sigma, vec4 color) {\n  vec2 lo = bounds.xy;\n  vec2 hi = bounds.zw;\n  sigma *= 2.400;\n  radius = max(radius, sigma * 0.5);\n  vec2 dc = destCoord();\n  vec2 p = dc;\n  float R = radius;\n  vec2 Rs = softness;\n  vec2 cl = (lo + R) + (R * Rs);\n  vec2 ch = (hi - R) - (R * Rs);\n  vec2 k = max((4.0 * R) * Rs, 1e-6);\n  vec2 xl = cl - (0.5 * k);\n  vec2 xh = ch + (0.5 * k);\n  p = compare(p - xl, p - (lo + R), compare(p - cl, ((-(p - cl)) * (p - cl)) / k, compare(p - ch, vec2(0.0), compare(p - xh, ((p - ch) * (p - ch)) / k, p - (hi - R)))));\n  float x = length(p) - R;\n  if (x < ((-9.900000e-01) * R)) {\n    vec2 lo = bounds.xy + R;\n    vec2 hi = bounds.zw - R;\n    x = max(max(lo.x - dc.x, lo.y - dc.y), max(dc.x - hi.x, dc.y - hi.y));\n    x -= R;\n  }\n  x = clamp((x + sigma) / (2.0 * sigma), 0.0, 1.0);\n  x = ((x * x) * x) * ((((6.0 * x) - 1.500000e+01) * x) + 10.0);\n  return color * (1.0 - x);\n}\n"
+ "kernel vec4 _boostHybrid(vec4 color, vec4 rgblboostnogamma, float transitionBreakpoint, float transitionWidth, float luminanceAmount) {\n  float luminance, factor, interpolant;\n  vec4 xcolor, answer;\n  luminance = dot(color.rgb, vec3(0.299, 0.587, 0.114));\n  answer = rgblboostnogamma;\n  xcolor = color;\n  xcolor.a = luminance;\n  answer = compare(xcolor, vec4(0.0), answer);\n  answer = max(answer, vec4(0.0));\n  factor = answer.a / max(luminance, 1e-6);\n  color.rgb = color.rgb * vec3(factor);\n  color.rgb = max(color.rgb, vec3(0.0));\n  interpolant = clamp((luminance - (transitionBreakpoint - (transitionWidth * 0.5))) / transitionWidth, 0.0, 1.0);\n  interpolant = 1.0 - (((3.0 - (2.0 * interpolant)) * interpolant) * interpolant);\n  interpolant = interpolant * luminanceAmount;\n  color.rgb = mix(answer.rgb, color.rgb, interpolant);\n  return color;\n}\n"
+ "kernel vec4 _ciSingleChannelColorMap(sampler s, sampler lut) {\n  float v = clamp(sample(s, samplerCoord(s)).x, 0.0, 1.0);\n  float vInt = (255.0 * v) + 0.5;\n  vec2 xy = samplerTransform(lut, vec2(vInt, 0.5));\n  return sample(lut, xy);\n}\n"
+ "kernel vec4 _ci_argb10widelinear(vec4 s) {\n  s = (s * 65535.0) / 64.0;\n  s = (s - 384.0) / 510.0;\n  return s.bgra;\n}\n"
+ "kernel vec4 _ci_combine_420(vec4 s00, vec4 s10, vec4 s01, vec4 s11) {\n  vec2 pc = writeCoord();\n  vec2 py = pc * 2.0;\n  writeImage(s00.rrrr, py);\n  writeImage(s10.rrrr, py + vec2(1, 0));\n  writeImage(s01.rrrr, py + vec2(0, 1));\n  writeImage(s11.rrrr, py + vec2(1, 1));\n  vec4 cc = ((s00 + s10) + s01) + s11;\n  writeImagePlane(vec4(cc.gb / cc.a, 0.0, 0.0), pc);\n  return s00;\n}\n"
+ "kernel vec4 _ci_combine_422(vec4 s0, vec4 s1) {\n  vec2 pc = writeCoord();\n  vec2 py = vec2(pc.x * 2.0, pc.y);\n  writeImage(s0.rrrr, py);\n  writeImage(s1.rrrr, py + vec2(1, 0));\n  vec4 cc = s0 + s1;\n  writeImagePlane(vec4(cc.gb / cc.a, 0.0, 0.0), pc);\n  return s0;\n}\n"
+ "kernel vec4 _ci_to_a2bgr10_as_rgba8(vec4 s) {\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.r);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.b) << 20;\n  pixel |= int(denorm.a) << 30;\n  return vec4(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255) / 255.0;\n}\n"
+ "kernel vec4 _ci_to_a2rgb10_as_rgba8(vec4 s) {\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.b);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.r) << 20;\n  pixel |= int(denorm.a) << 30;\n  return vec4(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255) / 255.0;\n}\n"
+ "kernel vec4 _ci_to_argb10widelinear_as_rgba16(vec4 s) {\n  s = (s * 510.0) + 384.0;\n  s = clamp(s, 0.0, 1023.0);\n  s = (s * 64.0) / 65535.0;\n  return s.bgra;\n}\n"
+ "kernel vec4 _ci_to_rgb10_as_rgba8(vec4 s) {\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.b);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.r) << 20;\n  pixel |= 3 << 30;\n  return vec4(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255) / 255.0;\n}\n"
+ "kernel vec4 _ci_to_rgb10wide_as_rgba8(vec4 s) {\n  s = vec4((linear_to_srgb(s.rgb) * (510.0 / 1023.0)) + (384.0 / 1023.0), 1.0);\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.b);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.r) << 20;\n  pixel |= int(denorm.a) << 30;\n  return vec4(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255) / 255.0;\n}\n"
+ "kernel vec4 _ci_to_rgb10widelinear_as_rgba8(vec4 s) {\n  s = vec4((s.rgb * (510.0 / 1023.0)) + (384.0 / 1023.0), 1.0);\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.b);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.r) << 20;\n  pixel |= int(denorm.a) << 30;\n  return vec4(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255) / 255.0;\n}\n"
+ "kernel vec4 _ci_unpremul(vec4 s) {\n  vec4 tmp = max(s, vec4(1e-5));\n  return vec4(s.rgb / tmp.a, s.a);\n}\n"
+ "kernel vec4 _ci_writeSIMD_420(vec4 color) { return vec4(0); }\n"
+ "kernel vec4 _ci_writeSIMD_422(vec4 color) { return vec4(0); }\n"
+ "kernel vec4 _ci_writeTG_420(const vec4 color) { return vec4(0); }\n"
+ "kernel vec4 _ci_writeTG_422(const vec4 color) { return vec4(0); }\n"
+ "kernel vec4 _clampHDR(vec4 s, float maxComponent) {\n  float x = min(s.x, maxComponent);\n  float y = min(s.y, maxComponent);\n  float z = min(s.z, maxComponent);\n  return vec4(x, y, z, s.a);\n}\n"
+ "kernel vec4 _clampToFrame(sampler s, vec4 frame) {\n  vec2 p = clamp(destCoord(), frame.xy, frame.zw);\n  return sample(s, samplerTransform(s, p));\n}\n"
+ "kernel vec4 _cmcubeopaque(vec4 im, sampler2D cube, vec4 dims) {\n  im.rgb = clamp(im.rgb, 1e-4, 0.9999);\n  im.rgb *= dims.x;\n  float imb = floor(im.b);\n  float flr = max(imb, 0.0);\n  float pageA = flr;\n  float dimsx = dims.x;\n  float pageB = min(pageA + 1.0, dimsx);\n  vec2 xy = vec2(0.5 + im.rg);\n  vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n  vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n  vec2 dimszw = vec2(dims.zw);\n  vec3 sLo = vec3(texture2D(cube, pLo * dimszw).rgb);\n  vec3 sHi = vec3(texture2D(cube, pHi * dimszw).rgb);\n  im.rgb = mix(sLo, sHi, im.b - flr);\n  return im;\n}\n"
+ "kernel vec4 _colorBlendMode_v0(vec4 pCf, vec4 pCb) {\n  vec4 uCf = unpremultiply(pCf);\n  vec4 uCb = unpremultiply(pCb);\n  vec4 uCfSort = (uCf.r > uCf.g) ? uCf : uCf.grba;\n  uCfSort = (uCfSort.g > uCfSort.b) ? uCfSort : uCfSort.rbga;\n  uCfSort = (uCfSort.r > uCfSort.g) ? uCfSort : uCfSort.grba;\n  float fL = (uCfSort.r + uCfSort.b) * 0.5;\n  float cmax = uCfSort.r;\n  float cmin = uCfSort.b;\n  vec4 uCbSort = (uCb.r > uCb.g) ? uCb : uCb.grba;\n  uCbSort = (uCbSort.g > uCbSort.b) ? uCbSort : uCbSort.rbga;\n  uCbSort = (uCbSort.r > uCbSort.g) ? uCbSort : uCbSort.grba;\n  float bL = (uCbSort.r + uCbSort.b) * 0.5;\n  float d = cmax - cmin;\n  float dv = (fL < 0.5) ? (cmax + cmin) : (2.0 - (cmax + cmin));\n  float s = d / max(dv, 1e-6);\n  float mmax = (bL <= 0.5) ? (bL + (bL * s)) : ((bL + s) - (bL * s));\n  float mmin = (bL * 2.0) - mmax;\n  vec4 Ct = (((uCf - uCfSort.b) * (mmax - mmin)) / (uCfSort.r - uCfSort.b)) + mmin;\n  Ct = ((mmin + 1e-5) > mmax) ? vec4(mmin) : Ct;\n  Ct.a = uCb.a;\n  vec4 Cb = vec4(uCb.rgb * uCb.a, uCb.a);\n  Ct = mix(uCf, Ct, uCb.a);\n  Ct.a = 1.0;\n  return mix(Cb, Ct, uCf.a);\n}\n"
+ "kernel vec4 _colorBurnBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 B = 1.0 - ((1.0 - Cb) / max(Cs, vec4(1e-7)));\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
+ "kernel vec4 _colorControls(vec4 src, float threshold, float contrast) {\n  vec4 pix = vec4(src.rgb / max(src.a, 1e-5), src.a);\n  float f = clamp(((dot(pix.rgb, vec3(2.125000e-01, 7.154000e-01, 7.210000e-02)) - threshold) * contrast) + 0.5, 0.0, 1.0);\n  return vec4(0.0, 0.0, 0.0, f);\n}\n"
+ "kernel vec4 _colorDodgeBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 B = Cb / max(1.0 - Cs, vec4(1e-7));\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
+ "kernel vec4 _colorMonochrome(vec4 img, vec4 color, float intensity) {\n  float luma = dot(img.rgb, vec3(2.125000e-01, 7.154000e-01, 7.210000e-02));\n  vec4 lo = (2.0 * luma) * color;\n  vec4 hi = max(color, 1.0 - ((2.0 * (1.0 - luma)) * (1.0 - color)));\n  vec4 pix = (luma < 0.5) ? lo : hi;\n  pix = mix(img, pix, intensity);\n  return vec4(pix.rgb, img.a);\n}\n"
+ "kernel vec4 _colorbalance(vec4 pix, vec4 clr, vec4 params) {\n  pix.rgb = ((pix.r * vec3(0.299, 5.957160e-01, 2.114560e-01)) + (pix.g * vec3(0.587, -2.744530e-01, -5.225910e-01))) + (pix.b * vec3(0.114, -3.212630e-01, 3.111350e-01));\n  clr.rgb /= max(clr.a, 1e-5);\n  clr.rgb = pow(max(clr.rgb, 0.0), vec3(0.25));\n  clr.rgb = ((clr.r * vec3(0.299, 5.957160e-01, 2.114560e-01)) + (clr.g * vec3(0.587, -2.744530e-01, -5.225910e-01))) + (clr.b * vec3(0.114, -3.212630e-01, 3.111350e-01));\n  pix.gb += (params.z * (params.xy - clr.gb)) * pow(pix.r, params.w);\n  pix.rgb = ((pix.r * vec3(1.0)) + (pix.g * vec3(9.562960e-01, -2.721220e-01, -1.10699))) + (pix.b * vec3(6.210240e-01, -6.473810e-01, 1.70461));\n  return pix;\n}\n"
+ "kernel vec4 _colorcube(vec4 im, sampler2D cube, vec4 dims) {\n  im.rgb = clamp(im.rgb, 1e-5, 9.999900e-01);\n  im.rgb *= dims.x;\n  float flr = floor(im.b);\n  float pageA = flr;\n  float pageB = min(pageA + 1.0, dims.x);\n  vec2 xy = 0.5 + im.rg;\n  vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n  vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n  vec4 sLo = texture2D(cube, pLo * dims.zw);\n  vec4 sHi = texture2D(cube, pHi * dims.zw);\n  vec4 cubeOut = mix(sLo, sHi, im.b - flr);\n  return vec4(cubeOut.rgb, cubeOut.a * im.a);\n}\n"
+ "kernel vec4 _colorcubeopaque(vec4 im, sampler2D cube, vec4 dims) {\n  im.rgb = clamp(im.rgb, 1e-5, 9.999900e-01);\n  im.rgb *= dims.x;\n  float flr = floor(im.b);\n  float pageA = flr;\n  float pageB = min(pageA + 1.0, dims.x);\n  vec2 xy = 0.5 + im.rg;\n  vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n  vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n  vec4 sLo = texture2D(cube, pLo * dims.zw);\n  vec4 sHi = texture2D(cube, pHi * dims.zw);\n  vec4 cubeOut = mix(sLo, sHi, im.b - flr);\n  return vec4(cubeOut.rgb, im.a);\n}\n"
+ "kernel vec4 _colorcubeopaque_extend(vec4 im, sampler2D cube, vec4 dims) {\n  vec4 c0 = vec4(0.3, 0.3, 0.3, 1.0);\n  float d0 = length(im.rgb - c0.rgb);\n  float d1 = length(clamp(im.rgb, 0.0, 1.0) - c0.rgb);\n  im.rgb = clamp(im.rgb, 1e-5, 9.999900e-01);\n  im.rgb *= dims.x;\n  float flr = floor(im.b);\n  float pageA = flr;\n  float pageB = min(pageA + 1.0, dims.x);\n  vec2 xy = 0.5 + im.rg;\n  vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n  vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n  vec4 sLo = texture2D(cube, pLo * dims.zw);\n  vec4 sHi = texture2D(cube, pHi * dims.zw);\n  vec4 cubeOut = mix(sLo, sHi, im.b - flr);\n  if (d0 > d1) {\n    vec4 c = c0;\n    c.rgb *= dims.x;\n    float flr = floor(c.b);\n    float pageA = flr;\n    float pageB = min(pageA + 1.0, dims.x);\n    vec2 xy = 0.5 + c.rg;\n    vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n    vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n    vec4 sLo = texture2D(cube, pLo * dims.zw);\n    vec4 sHi = texture2D(cube, pHi * dims.zw);\n    c = mix(sLo, sHi, c.b - flr);\n    cubeOut.rgb = (((cubeOut.rgb - c.rgb) * d0) / d1) + c.rgb;\n  }\n  return vec4(cubeOut.rgb, im.a);\n}\n"
+ "kernel vec4 _convertDepthOrDisparity(vec4 s) {\n  return vec4(1.0 / max(s.r, 1e-6), s.gba);\n}\n"
+ "kernel vec4 _convertRGBtoY(vec4 c) {\n  c = vec4(c.rgb / max(c.a, 1e-5), c.a);\n  float Y = sqrt(max(dot(c.rgb, vec3(0.299, 0.587, 0.114)), 0.0));\n  c.rgb = vec3(Y);\n  return c;\n}\n"
+ "kernel vec4 _dfdxdfdyChannel(sampler s, int channel) {\n  vec2 dc = destCoord();\n  vec4 fxpX = sample(s, samplerTransform(s, dc + vec2(1, 0)));\n  vec4 fxmX = sample(s, samplerTransform(s, dc - vec2(1, 0)));\n  vec4 fxpY = sample(s, samplerTransform(s, dc + vec2(0, 1)));\n  vec4 fxmY = sample(s, samplerTransform(s, dc - vec2(0, 1)));\n  float dfdx = (fxpX[channel] - fxmX[channel]) * 0.5;\n  float dfdy = (fxpY[channel] - fxmY[channel]) * 0.5;\n  return vec4(dfdx, dfdy, 0, 1);\n}\n"
+ "kernel vec4 _disintegrateWithMask(vec4 t0, vec4 t1, vec4 m0, vec4 m1, vec4 m2, vec4 m3, vec4 param) {\n  float shadowRadiusInv = param.y;\n  float shadowDensity = param.z;\n  float time = param.w;\n  float ramp = 1.0 / (max(abs(m1.r - m0.r), abs(m2.r - m0.r)) + 0.001);\n  float shadow = (((time - m3.r) * shadowRadiusInv) * ramp) + time;\n  shadow = clamp(shadow, 0.0, 1.0);\n  shadow = (shadowDensity * (shadow - 1.0)) + 1.0;\n  t0.rgb = t0.rgb * ((param.x * time) + 1.0);\n  t1.rgb = (t1.rgb * (((param.x * time) + 1.0) - param.x)) * shadow;\n  float s = clamp(((time - m0.r) * ramp) + time, 0.0, 1.0);\n  return mix(t0, t1, s);\n}\n"
+ "kernel vec4 _disintegrateWithMaskG(sampler s0, sampler s1, sampler m, vec2 offset, vec4 param) {\n  float shadowRadiusInv = param.y;\n  float shadowDensity = param.z;\n  float time = param.w;\n  vec4 t0 = sample(s0, samplerCoord(s0));\n  vec4 t1 = sample(s1, samplerCoord(s1));\n  vec2 d = destCoord();\n  vec4 m0 = sample(m, samplerTransform(m, d));\n  vec4 m1 = sample(m, samplerTransform(m, d + vec2(1.0, 0.0)));\n  vec4 m2 = sample(m, samplerTransform(m, d + vec2(0.0, 1.0)));\n  vec4 m3 = sample(m, samplerTransform(m, d - offset));\n  float ramp = 1.0 / (max(abs(m1.r - m0.r), abs(m2.r - m0.r)) + 0.001);\n  float shadow = (((time - m3.r) * shadowRadiusInv) * ramp) + time;\n  shadow = clamp(shadow, 0.0, 1.0);\n  shadow = (shadowDensity * (shadow - 1.0)) + 1.0;\n  t0.rgb = t0.rgb * ((param.x * time) + 1.0);\n  t1.rgb = (t1.rgb * (((param.x * time) + 1.0) - param.x)) * shadow;\n  float s = clamp(((time - m0.r) * ramp) + time, 0.0, 1.0);\n  return mix(t0, t1, s);\n}\n"
+ "kernel vec4 _disparityRefinementPreprocessing(vec4 disparity, vec4 alpha, vec4 lm, vec4 config0, vec4 config1) {\n  float alpha_val = alpha.x;\n  float d = disparity.x;\n  float zeroShift = lm.x;\n  float d_factor = clamp(config0.x * exp((-pow(max(1e-4, abs(d - zeroShift)), config0.y)) / config0.z), config0.w, config1.x);\n  if (alpha_val > config1.y) d -= (d - zeroShift) * d_factor;\n  return vec4(d, 0.0, 0.0, 1.0);\n}\n"
+ "kernel vec4 _disparityRefinementPreprocessingPow2(vec4 disparity, vec4 alpha, vec4 lm, vec4 config0, vec4 config1) {\n  float alpha_val = alpha.x;\n  float d = disparity.x;\n  float zeroShift = lm.x;\n  float v = max(1e-4, abs(d - zeroShift));\n  float d_factor = clamp(config0.x * exp((-(v * v)) / config0.z), config0.w, config1.x);\n  if (alpha_val > config1.y) d -= (d - zeroShift) * d_factor;\n  return vec4(d, 0.0, 0.0, 1.0);\n}\n"
+ "kernel vec4 _distanceFraction(vec4 s, float sdfZero, float sdfScale, float radius) {\n  float distance = (s.x - sdfZero) * sdfScale;\n  float distanceFraction = distance / radius;\n  return vec4(distanceFraction, distanceFraction, distanceFraction, 1.0);\n}\n"
+ "kernel vec4 _divideBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 B = Cb / max(Cs, vec4(1e-7));\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
+ "kernel vec4 _drr_binarize(vec4 m) {\n  m.r = (m.r > 1e-5) ? 1.0 : 0.0;\n  return m;\n}\n"
+ "kernel vec4 _drr_binarize_alpha(vec4 c, vec4 m, float t) {\n  c *= (m.r > 0.001) ? 1.0 : 0.0;\n  c *= (min(1.0 - c.r, c.r) > t) ? 1.0 : 0.0;\n  return c;\n}\n"
+ "kernel vec4 _drr_binarize_alpha_inv(vec4 c, vec4 m, float t) {\n  c *= (m.r > 0.001) ? 0.0 : 1.0;\n  c *= (min(1.0 - c.r, c.r) > t) ? 1.0 : 0.0;\n  return c;\n}\n"
+ "kernel vec4 _drr_binarize_inv(vec4 m) {\n  m.r = (m.r > 1e-5) ? 0.0 : 1.0;\n  return m;\n}\n"
+ "kernel vec4 _drr_cdmeasure(vec4 a, vec4 aI) {\n  return 1.0 - (abs(a - aI) / max(a + aI, 1e-4));\n}\n"
+ "kernel vec4 _drr_chromaexc(vec4 outside, vec4 inside, float t2, float thresholdSclera, float thresholdScleraBrightness) {\n  vec3 diff = inside.rgb - outside.rgb;\n  float n = min(inside.r, outside.r);\n  float exc = (dot(diff, diff) < (t2 * n)) ? 0.0 : 1.0;\n  float redness = max(inside.r - min(inside.g, inside.b), 0.0) / max(1e-5, inside.r);\n  exc *= ((inside.r > thresholdScleraBrightness) && (redness < thresholdSclera)) ? 0.0 : 1.0;\n  return vec4(exc, 0.0, 0.0, 1.0);\n}\n"
+ "kernel vec4 _drr_rawred_large(vec4 c, float whiteness, float spectrum) {\n  if (c.r < 5.000000e-03) return vec4(0.0, 0.0, 0.0, 1.0);\n  float n = dot(c.rgb, vec3(1.0 / 3.0));\n  float rv = (((c.r - n) * (c.r - n)) + ((c.g - n) * (c.g - n))) + ((c.b - n) * (c.b - n));\n  rv /= max(1e-4, n);\n  float rg = max(0.0, c.r - c.g) / max(1e-5, c.r + c.g);\n  float rb = max(0.0, c.r - c.b) / max(1e-5, c.r + c.b);\n  float rm = min(rg, rb);\n  float r = mix(1.0, rv, spectrum) * rm;\n  float w = c.r;\n  r = mix(r, w, whiteness);\n  return vec4(r, 0.0, 0.0, 1.0);\n}\n"
+ "kernel vec4 _drr_rawred_sm(vec4 c, float whiteness, float spectrum) {\n  if (c.r < 5.000000e-03) return vec4(0.0, 0.0, 0.0, 1.0);\n  float n = dot(c.rgb, vec3(1.0 / 3.0));\n  float rv = (((c.r - n) * (c.r - n)) + ((c.g - n) * (c.g - n))) + ((c.b - n) * (c.b - n));\n  rv /= max(1e-4, n);\n  float rg = max(0.0, c.r - c.g) / max(1e-5, c.r + c.g);\n  float rb = max(0.0, c.r - c.b) / max(1e-5, c.r + c.b);\n  float rm = min(rg, rb);\n  float r = rv * rm;\n  r *= 10.0;\n  r *= r;\n  float w = max(0.0, c.r - (whiteness * max(c.g, c.b)));\n  r = mix(r, w, spectrum);\n  return vec4(r, 0.0, 0.0, 1.0);\n}\n"
+ "kernel vec4 _drr_repair(vec4 img, vec4 c, vec4 m, vec4 avg, vec4 noise, float brightness, float noiseAmount, float whiteCutoff, float chroma) {\n  float mixer = m.r;\n  vec3 Y = vec3(0.299, 0.587, 0.114);\n  float nn = noise.r;\n  avg.rgb += (2.0 * noiseAmount) * nn;\n  vec3 source = c.rgb;\n  c.rgb += noiseAmount * nn;\n  float rg = max(0.0, img.r - img.g) / max(1e-4, img.r + img.g);\n  float rb = max(0.0, img.r - img.b) / max(1e-4, img.r + img.b);\n  float redness = max(0.25, 0.5 * (rg + rb));\n  redness = smoothstep(0.1, 6.000000e-01, redness);\n  vec3 replacementRed = (0.5 * brightness) * vec3(min(c.b, c.g));\n  vec3 replacementWhite = (2.0 * brightness) * avg.rgb;\n  vec3 replacement = mix(replacementWhite, replacementRed, redness);\n  float Lrep = dot(replacement, Y);\n  float Lavg = dot(avg.rgb, Y);\n  replacement = mix(replacement, (avg.rgb * Lrep) * Lavg, chroma);\n  replacement = max(6.000000e-02 * avg.rgb, replacement);\n  float n = dot(img.rgb, Y);\n  float whiteness = smoothstep(0.01 + whiteCutoff, 1.010, n);\n  replacement.rgb = mix(replacement.rgb, vec3(n), whiteness);\n  mixer *= 1.0 - whiteness;\n  img.rgb = mix(img.rgb, replacement, mixer);\n  img.rgb = mix(source, img.rgb, m.r);\n  return img;\n}\n"
+ "kernel vec4 _edgeWork(vec4 src, vec4 blurred) {\n  return vec4(clamp((src.r - blurred.r) * 1000.0, 0.0, 1.0));\n}\n"
+ "kernel vec4 _edgesPrep(vec4 s) {\n  s = vec4(s.rgb / max(s.a, 1e-5), s.a);\n  s.rgb = sqrt(max(s.rgb, vec3(0.0)));\n  return s;\n}\n"
+ "kernel vec4 _flexLumaScaling(vec4 im, vec2 headrooms, vec4 coefs, float coeffs4, sampler2D lut, vec2 dim) {\n  float imMax = max(im.r, max(im.g, im.b));\n  float Y = dot(coefs, vec4(im.rgb, imMax));\n  float signY = sign(Y);\n  Y = max(abs(Y), 1e-6);\n  Y = clamp(Y, 0.0, 1.0);\n  float lutCoord = (Y * dim.x) + dim.y;\n  float gain = texture2D(lut, vec2(lutCoord, 0.5)).r;\n  float scale = (signY * gain) * coeffs4;\n  vec4 result = vec4(im.rgb * scale, im.a);\n  return result;\n}\n"
+ "kernel vec4 _fwidth(sampler s) {\n  vec2 dc = destCoord();\n  vec4 fxpX = sample(s, samplerTransform(s, dc + vec2(1, 0)));\n  vec4 fxmX = sample(s, samplerTransform(s, dc - vec2(1, 0)));\n  vec4 fxpY = sample(s, samplerTransform(s, dc + vec2(0, 1)));\n  vec4 fxmY = sample(s, samplerTransform(s, dc - vec2(0, 1)));\n  vec4 dfdx = (fxpX - fxmX) * 0.5;\n  vec4 dfdy = (fxpY - fxmY) * 0.5;\n  return abs(dfdx) + abs(dfdy);\n}\n"
+ "kernel vec4 _gatherSDF(vec4 s, float below, float above) {\n  float v = (s.x < 0.5) ? below : above;\n  return vec4(v, v, v, 1.0);\n}\n"
+ "kernel vec4 _glowMaskNotOpposite(vec4 s, float sdfZero, float sdfScale, float radius, vec4 color) {\n  float distance = (s.x - sdfZero) * sdfScale;\n  float distanceFraction = distance / radius;\n  float strength = exp(((-0.5) * distanceFraction) * distanceFraction);\n  return (distance > 0) ? (color * strength) : color;\n}\n"
+ "kernel vec4 _gradientRangeLimit(vec4 grad, float gxgyE0, float gxgyE1, float gygxE0, float gygxE1) {\n  vec2 G = grad.xy;\n  float Gy = abs(G.y);\n  float Gx = abs(G.x);\n  if ((Gy + Gx) < 0.001) return vec4(0);\n  if (Gx < Gy) {\n    float gxgy = G.x / G.y;\n    return grad * (1.0 - smoothstep(gxgyE0, gxgyE1, gxgy));\n  } else {\n    float gygx = G.y / G.x;\n    return grad * (1.0 - smoothstep(gygxE0, gygxE1, gygx));\n  }\n}\n"
+ "kernel vec4 _grassAndSkyAdjust(vec4 im, vec2 params) {\n  float enhanceGrass = params.x;\n  float enhanceSky = params.y;\n  vec3 ipt, ipt2;\n  float range;\n  {\n    vec3 lms = ((im.r * vec3(3.347000e-01, 1.747000e-01, 1.870000e-02)) + (im.g * vec3(5.984000e-01, 7.151000e-01, 1.018000e-01))) + (im.b * vec3(6.710000e-02, 1.106000e-01, 8.794000e-01));\n    lms = sign(lms) * pow(abs(lms), vec3(4.300000e-01));\n    ipt = ((lms.r * vec3(4.000000e-01, 4.455, 8.056000e-01)) + (lms.g * vec3(4.000000e-01, -4.851, 3.572000e-01))) + (lms.b * vec3(2.000000e-01, 3.960000e-01, -1.1628));\n  }\n  float hue = (atan(sqrt((ipt.b * ipt.b) + (ipt.g * ipt.g)) - ipt.g, ipt.b) / 3.1416) + 0.5;\n  range = hue - 8.800000e-01;\n  float maskGrass = exp((((-1.0) * range) * range) / ((2.0 * 8.800000e-02) * 8.800000e-02));\n  range = 1.0 - smoothstep(4.000000e-01, 0.5, ipt.r);\n  maskGrass *= range;\n  vec2 idealGrass = vec2(-3.000000e-02, 0.1);\n  vec2 toIdeal = idealGrass - ipt.gb;\n  float dist = sqrt((toIdeal.r * toIdeal.r) + (toIdeal.g * toIdeal.g));\n  float chroma2 = 4.0 * ((ipt.g * ipt.g) + (ipt.b * ipt.b));\n  float str = enhanceGrass * pow(chroma2, 2.000000e-01);\n  str = str * min(1.0, 1.0 - (chroma2 * chroma2));\n  str = min(str, 1.500);\n  float scale = min(1.0, 0.1 / (dist + 5.000000e-02));\n  ipt2.gb = ipt.gb + ((str * toIdeal) * scale);\n  ipt2.gb *= enhanceGrass;\n  ipt2.r = ipt.r;\n  ipt = mix(ipt, ipt2.rgb, maskGrass);\n  float maskSky = smoothstep(2.000000e-01, 0.5, ipt.r);\n  range = ipt.g + 4.000000e-02;\n  maskSky *= exp((((-1.0) * range) * range) / ((2.0 * 1.500000e-01) * 1.500000e-01));\n  range = ipt.b + 0.1;\n  maskSky *= exp((((-1.0) * range) * range) / ((2.0 * 2.000000e-01) * 2.000000e-01));\n  {\n    vec3 lms = ((ipt.r * vec3(1.0, 1.0, 1.0)) + (ipt.g * vec3(9.760000e-02, -1.139000e-01, 3.260000e-02))) + (ipt.b * vec3(2.052000e-01, 1.332000e-01, -6.769000e-01));\n    lms = sign(lms) * pow(abs(lms), vec3(1.0 / 4.300000e-01));\n    im.rgb = ((lms.r * vec3(5.3089, -1.3026, 3.810000e-02)) + (lms.g * vec3(-4.4648, 2.5193, -1.968000e-01))) + (lms.b * vec3(1.564000e-01, -2.175000e-01, 1.159));\n  }\n  im.rgb = max(im.rgb, 0.0);\n  float gain = max(1.0, 1.0 + enhanceSky);\n  float gamma = 1.0 + abs(enhanceSky);\n  vec4 result = pow(gain * im, vec4(gamma));\n  float gray = ((result.r + result.b) + result.g) / 3.0;\n  result.rgb += ((result.rgb - gray) * abs(enhanceSky)) * 0.5;\n  result = mix(im, result, maskSky);\n  result.a = im.a;\n  return result;\n}\n"
+ "kernel vec4 _headroomClamp(vec4 img, float target_headroom) {\n  float rgb_max = max(max(max(img.r, img.g), img.b), 0.001);\n  return (rgb_max <= target_headroom) ? img : vec4((img.rgb * target_headroom) / rgb_max, img.a);\n}\n"
+ "kernel vec4 _headroomToneMap(vec4 img, float source_headroom, float target_headroom, float slope_adjusted, vec4 bezier_norm, vec3 beziers_py, vec3 extension, float cdr_scale) {\n  img *= cdr_scale;\n  float rgb_max = max(max(max(img.r, img.g), img.b), 0.001);\n  float p0x = bezier_norm.w;\n  float rgb_max_tmo = slope_adjusted * rgb_max;\n  if (rgb_max > p0x) {\n    float a = bezier_norm.x;\n    float b = bezier_norm.y;\n    float c = bezier_norm.z;\n    float t = (sqrt(max((a * rgb_max) + b, 0.0)) + c) / a;\n    float p0y = beziers_py.x;\n    float p1y = beziers_py.y;\n    float p2y = beziers_py.z;\n    float yB = ((((1.0 - t) * (1.0 - t)) * p0y) + (((2 * (1.0 - t)) * t) * p1y)) + ((t * t) * p2y);\n    float extension_offset = extension.y;\n    rgb_max_tmo = (rgb_max < source_headroom) ? yB : extension_offset;\n  }\n  float output_gamma = extension.z;\n  rgb_max_tmo = pow(rgb_max_tmo / target_headroom, output_gamma) * target_headroom;\n  float maxRatio = min(rgb_max_tmo / rgb_max, 1.0);\n  vec3 img_tmo = min(maxRatio * img.rgb, target_headroom);\n  return vec4(img_tmo, img.a);\n}\n"
+ "kernel vec4 _highlightsAndShadows0(vec4 pix, vec4 blur, vec4 params) {\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(0.001, (pix.r + pix.g) + pix.b);\n  rgbFactor = clamp(rgbFactor, 0.0, 1.0);\n  float shadAmt = params.x * pow(rgbFactor, max(0.0, 1.0 - params.x));\n  vec3 clamped = clamp(pix.rgb, 1e-5, 9.999900e-01);\n  float gray = ((clamped.r + clamped.g) + clamped.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  float rgbsat = max((clamped.r - gray) * gii, (gray - clamped.r) * gi);\n  float skin = min(1.0, ((max(0.0, min(clamped.r - clamped.g, (clamped.g * 2.0) - clamped.b)) * 4.0) * (1.0 - rgbsat)) * gi);\n  skin = 1.500000e-01 + (skin * 7.000000e-01);\n  vec3 rgbExp = pow(vec3(2.0), (-shadAmt) - blur.rgb);\n  float uniformExp = min(rgbExp.r, min(rgbExp.g, rgbExp.b));\n  vec3 shadExp = mix(rgbExp, vec3(uniformExp), skin);\n  float nopMix = params.z;\n  shadExp = mix(shadExp, vec3(1.0, 1.0, 1.0), nopMix);\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * 0.5, shadExp)) * 2.0;\n  float maxChan = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(maxChan);\n  float origPercent = sqrt(smoothstep(0.0, 0.1 + ((0.5 * shadAmt) * shadAmt), blurLum));\n  origPercent *= 1.0 - origPercent;\n  shad = mix(shad, pix.rgb, origPercent);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  origPercent = 1.0 - smoothstep(2.000000e-01, 8.000000e-01, blurLum);\n  high = mix(high, pix.rgb, origPercent);\n  vec4 result;\n  result.rgb = mix(shad, high, blurLum);\n  float Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  vec3 mid = mix(vec3(0.5), result.rgb, 1.0 + (abs(shadAmt) * 5.000000e-02));\n  result.rgb = mix(result.rgb, mid.rgb, min(effectAmount, (3.000000e+01 * blurLum) * blurLum));\n  result.a = pix.a;\n  return result;\n}\n"
+ "kernel vec4 _highlightsAndShadows1(vec4 pix, vec4 blur, vec4 params) {\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(0.001, (pix.r + pix.g) + pix.b);\n  float shadAmt = params.x * pow(min(rgbFactor, 1.0), 1.0 - params.x);\n  vec3 shadExp = mix(pow(vec3(2.0), (-shadAmt) - blur.rgb), vec3(1.0), params.z);\n  float blurLum2 = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(blurLum2);\n  float kGain = 0.5 + (0.5 * smoothstep(0.5, 1.0, params.x));\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * kGain, shadExp)) * 2.0;\n  vec3 ycc = ((pix.r * vec3(0.299, 5.960000e-01, 2.120000e-01)) + (pix.g * vec3(0.587, -2.755000e-01, -5.230000e-01))) + (pix.b * vec3(0.114, -3.210000e-01, 3.110000e-01));\n  float Y = (sign(ycc.r) * pow(abs(ycc.r) * kGain, shadExp.r)) * 2.0;\n  vec3 shad2 = ((Y * vec3(1.00048, 9.998640e-01, 9.994460e-01)) + (ycc.g * vec3(9.555580e-01, -2.715450e-01, -1.10803))) + (ycc.b * vec3(6.195490e-01, -6.467860e-01, 1.70542));\n  shad = mix(shad, shad2, 3.500000e-01);\n  shad = mix(pix.rgb, shad, sqrt(smoothstep(0.0, 0.1 + shadAmt, sqrt(blurLum))));\n  shad = mix(shad, pix.rgb, blurLum);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  Y = dot(high, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float kHighMix = 1.0 + ((1.0 - min(1.0, params.y + 0.3)) * 4.000000e-01);\n  vec3 mid = mix(vec3(0.25), high, kHighMix);\n  float highBoost = min(effectAmount, 3.000000e+01 * blurLum2) * (1.0 - params.y);\n  high = mix(high, mid, highBoost);\n  high = mix(pix.rgb, high, smoothstep(2.000000e-01, 8.000000e-01, blurLum));\n  high = mix(pix.rgb, high, blurLum2);\n  vec4 result;\n  result.rgb = mix(shad, high, min(blurLum, 1.0));\n  Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float midAmt = (abs(shadAmt) * 0.1) * (1.0 - params.z);\n  mid = mix(vec3(0.5), result.rgb, 1.0 + midAmt);\n  result.rgb = mix(result.rgb, mid, min(effectAmount, 3.000000e+01 * blurLum2));\n  result.a = pix.a;\n  return result;\n}\n"
+ "kernel vec4 _highlightsAndShadows2(vec4 pix, vec4 blur, vec4 params) {\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(0.001, (pix.r + pix.g) + pix.b);\n  float shadAmt = params.x * pow(min(rgbFactor, 1.0), 1.0 - params.x);\n  vec3 shadExp = mix(pow(vec3(2.0), (-shadAmt) - blur.rgb), vec3(1.0), params.z);\n  float blurLum2 = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(blurLum2);\n  float kGain = 0.5 + (0.5 * smoothstep(0.5, 1.0, params.x));\n  float newGain = shadAmt;\n  vec3 neg = min(pix.rgb, 0.0);\n  vec3 shad = ((1.0 + newGain) * pow(max(pix.rgb, 0.0) * kGain, shadExp)) * 2.0;\n  vec3 ycc = ((pix.r * vec3(0.299, 5.960000e-01, 2.120000e-01)) + (pix.g * vec3(0.587, -2.755000e-01, -5.230000e-01))) + (pix.b * vec3(0.114, -3.210000e-01, 3.110000e-01));\n  float Y = pow(max(ycc.r, 0.0) * kGain, shadExp.r) * 2.0;\n  vec3 shad2 = ((Y * vec3(1.00048, 9.998640e-01, 9.994460e-01)) + (ycc.g * vec3(9.555580e-01, -2.715450e-01, -1.10803))) + (ycc.b * vec3(6.195490e-01, -6.467860e-01, 1.70542));\n  shad = mix(shad, shad2, 3.500000e-01);\n  shad = mix(pix.rgb, shad, smoothstep(0.0, 0.1 + shadAmt, sqrt(blurLum)));\n  shad = mix(shad, pix.rgb, blurLum);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  Y = dot(high, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float kHighMix = 1.0 + ((1.0 - min(1.0, params.y + 0.3)) * 4.000000e-01);\n  vec3 mid = mix(vec3(0.25), high, kHighMix);\n  float highBoost = min(effectAmount, 3.000000e+01 * blurLum2) * (1.0 - params.y);\n  high = mix(high, mid, highBoost);\n  high = mix(pix.rgb, high, smoothstep(2.000000e-01, 8.000000e-01, blurLum));\n  high = mix(pix.rgb, high, blurLum2);\n  vec4 result;\n  result.rgb = mix(shad, high, min(blurLum, 1.0));\n  Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float midAmt = (abs(shadAmt) * 0.1) * (1.0 - params.z);\n  mid = mix(vec3(0.5), result.rgb, 1.0 + midAmt);\n  result.rgb = mix(result.rgb, mid, min(effectAmount, 3.000000e+01 * blurLum2));\n  result.rgb = max(result.rgb, 0.0) + neg;\n  result.a = pix.a;\n  return result;\n}\n"
+ "kernel vec4 _highlightsAndShadows_noblur0(vec4 pix, vec4 params) {\n  vec4 blur = pix;\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(0.001, (pix.r + pix.g) + pix.b);\n  rgbFactor = clamp(rgbFactor, 0.0, 1.0);\n  float shadAmt = params.x * pow(rgbFactor, max(0.0, 1.0 - params.x));\n  vec3 clamped = clamp(pix.rgb, 1e-5, 9.999900e-01);\n  float gray = ((clamped.r + clamped.g) + clamped.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  float rgbsat = max((clamped.r - gray) * gii, (gray - clamped.r) * gi);\n  float skin = min(1.0, ((max(0.0, min(clamped.r - clamped.g, (clamped.g * 2.0) - clamped.b)) * 4.0) * (1.0 - rgbsat)) * gi);\n  skin = 1.500000e-01 + (skin * 7.000000e-01);\n  vec3 rgbExp = pow(vec3(2.0), (-shadAmt) - blur.rgb);\n  float uniformExp = min(rgbExp.r, min(rgbExp.g, rgbExp.b));\n  vec3 shadExp = mix(rgbExp, vec3(uniformExp), skin);\n  float nopMix = params.z;\n  shadExp = mix(shadExp, vec3(1.0, 1.0, 1.0), nopMix);\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * 0.5, shadExp)) * 2.0;\n  float maxChan = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(maxChan);\n  float origPercent = sqrt(smoothstep(0.0, 0.1 + ((0.5 * shadAmt) * shadAmt), blurLum));\n  origPercent *= 1.0 - origPercent;\n  shad = mix(shad, pix.rgb, origPercent);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  origPercent = 1.0 - smoothstep(2.000000e-01, 8.000000e-01, blurLum);\n  high = mix(high, pix.rgb, origPercent);\n  vec4 result;\n  result.rgb = mix(shad, high, blurLum);\n  float Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  vec3 mid = mix(vec3(0.5), result.rgb, 1.0 + (abs(shadAmt) * 5.000000e-02));\n  result.rgb = mix(result.rgb, mid.rgb, min(effectAmount, (3.000000e+01 * blurLum) * blurLum));\n  result.a = pix.a;\n  return result;\n}\n"
+ "kernel vec4 _highlightsAndShadows_noblur1(vec4 pix, vec4 params) {\n  vec4 blur = pix;\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(0.001, (pix.r + pix.g) + pix.b);\n  float shadAmt = params.x * pow(min(rgbFactor, 1.0), 1.0 - params.x);\n  vec3 shadExp = mix(pow(vec3(2.0), (-shadAmt) - blur.rgb), vec3(1.0), params.z);\n  float blurLum2 = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(blurLum2);\n  float kGain = 0.5 + (0.5 * smoothstep(0.5, 1.0, params.x));\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * kGain, shadExp)) * 2.0;\n  vec3 ycc = ((pix.r * vec3(0.299, 5.960000e-01, 2.120000e-01)) + (pix.g * vec3(0.587, -2.755000e-01, -5.230000e-01))) + (pix.b * vec3(0.114, -3.210000e-01, 3.110000e-01));\n  float Y = (sign(ycc.r) * pow(abs(ycc.r) * kGain, shadExp.r)) * 2.0;\n  vec3 shad2 = ((Y * vec3(1.00048, 9.998640e-01, 9.994460e-01)) + (ycc.g * vec3(9.555580e-01, -2.715450e-01, -1.10803))) + (ycc.b * vec3(6.195490e-01, -6.467860e-01, 1.70542));\n  shad = mix(shad, shad2, 3.500000e-01);\n  shad = mix(pix.rgb, shad, sqrt(smoothstep(0.0, 0.1 + shadAmt, sqrt(blurLum))));\n  shad = mix(shad, pix.rgb, blurLum);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  Y = dot(high, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float kHighMix = 1.0 + ((1.0 - min(1.0, params.y + 0.3)) * 4.000000e-01);\n  vec3 mid = mix(vec3(0.25), high, kHighMix);\n  float highBoost = min(effectAmount, 3.000000e+01 * blurLum2) * (1.0 - params.y);\n  high = mix(high, mid, highBoost);\n  high = mix(pix.rgb, high, smoothstep(2.000000e-01, 8.000000e-01, blurLum));\n  high = mix(pix.rgb, high, blurLum2);\n  vec4 result;\n  result.rgb = mix(shad, high, min(blurLum, 1.0));\n  Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float midAmt = (abs(shadAmt) * 0.1) * (1.0 - params.z);\n  mid = mix(vec3(0.5), result.rgb, 1.0 + midAmt);\n  result.rgb = mix(result.rgb, mid, min(effectAmount, 3.000000e+01 * blurLum2));\n  result.a = pix.a;\n  return result;\n}\n"
+ "kernel vec4 _highlightsAndShadows_noblur2(vec4 pix, vec4 params) {\n  vec4 blur = pix;\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(0.001, (pix.r + pix.g) + pix.b);\n  float shadAmt = params.x * pow(min(rgbFactor, 1.0), 1.0 - params.x);\n  vec3 shadExp = mix(pow(vec3(2.0), (-shadAmt) - blur.rgb), vec3(1.0), params.z);\n  float blurLum2 = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(blurLum2);\n  float kGain = 0.5 + (0.5 * smoothstep(0.5, 1.0, params.x));\n  float newGain = shadAmt;\n  vec3 neg = min(pix.rgb, 0.0);\n  vec3 shad = ((1.0 + newGain) * pow(max(pix.rgb, 0.0) * kGain, shadExp)) * 2.0;\n  vec3 ycc = ((pix.r * vec3(0.299, 5.960000e-01, 2.120000e-01)) + (pix.g * vec3(0.587, -2.755000e-01, -5.230000e-01))) + (pix.b * vec3(0.114, -3.210000e-01, 3.110000e-01));\n  float Y = (sign(ycc.r) * pow(abs(ycc.r) * kGain, shadExp.r)) * 2.0;\n  vec3 shad2 = ((Y * vec3(1.00048, 9.998640e-01, 9.994460e-01)) + (ycc.g * vec3(9.555580e-01, -2.715450e-01, -1.10803))) + (ycc.b * vec3(6.195490e-01, -6.467860e-01, 1.70542));\n  shad = mix(shad, shad2, 3.500000e-01);\n  shad = mix(pix.rgb, shad, smoothstep(0.0, 0.1 + shadAmt, sqrt(blurLum)));\n  shad = mix(shad, pix.rgb, blurLum);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  Y = dot(high, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float kHighMix = 1.0 + ((1.0 - min(1.0, params.y + 0.3)) * 4.000000e-01);\n  vec3 mid = mix(vec3(0.25), high, kHighMix);\n  float highBoost = min(effectAmount, 3.000000e+01 * blurLum2) * (1.0 - params.y);\n  high = mix(high, mid, highBoost);\n  high = mix(pix.rgb, high, smoothstep(2.000000e-01, 8.000000e-01, blurLum));\n  high = mix(pix.rgb, high, blurLum2);\n  vec4 result;\n  result.rgb = mix(shad, high, min(blurLum, 1.0));\n  Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float midAmt = (abs(shadAmt) * 0.1) * (1.0 - params.z);\n  mid = mix(vec3(0.5), result.rgb, 1.0 + midAmt);\n  result.rgb = mix(result.rgb, mid, min(effectAmount, 3.000000e+01 * blurLum2));\n  result.rgb = max(result.rgb, 0.0) + neg;\n  result.a = pix.a;\n  return result;\n}\n"
+ "kernel vec4 _histogram_display(sampler image, float height, vec2 hilo) {\n  vec2 d = destCoord();\n  vec2 histcoord = vec2(floor(d.x) + 0.5, 0.5);\n  vec4 v = sample(image, samplerTransform(image, histcoord));\n  v = step(vec4(d.y), height * v);\n  float vi = ((v.r * 4.0) + (v.g * 2.0)) + v.b;\n  vec4 p = vec4(0.25, 0.25, 0.25, 1.0);\n  p = (vi == 4.0) ? vec4(0.5, 5.000000e-02, 5.000000e-02, 1.0) : p;\n  p = (vi == 6.0) ? vec4(2.000000e-01, 4.000000e-01, 5.000000e-02, 1.0) : p;\n  p = (vi == 2.0) ? vec4(5.000000e-02, 0.5, 5.000000e-02, 1.0) : p;\n  p = (vi == 3.0) ? vec4(5.000000e-02, 2.000000e-01, 4.000000e-01, 1.0) : p;\n  p = (vi == 1.0) ? vec4(5.000000e-02, 5.000000e-02, 0.5, 1.0) : p;\n  p = (vi == 5.0) ? vec4(2.000000e-01, 5.000000e-02, 4.000000e-01, 1.0) : p;\n  p = (vi == 7.0) ? vec4(5.000000e-02, 0.1, 0.3, 1.0) : p;\n  p.rgb = (d.x < (hilo.x + 0.5)) ? (p.rgb * vec3(4.000000e-01)) : p.rgb;\n  p.rgb = (d.x >= (hilo.y + 0.5)) ? ((p.rgb * vec3(6.000000e-01)) + vec3(4.000000e-01)) : p.rgb;\n  return p;\n}\n"
+ "kernel vec4 _hlg_lumscale(vec4 im, vec4 lc, vec2 gg) {\n  float gamma = gg.x;\n  float gain = gg.y;\n  float rgbMax = max(max(im.r, im.g), im.b);\n  float Y = dot(vec4(im.rgb, rgbMax), lc);\n  Y = max(abs(Y), 1e-4);\n  im.rgb *= (sign(Y) * gain) * pow(Y, gamma);\n  return im;\n}\n"
+ "kernel vec4 _holeFillRefine(sampler image, float maxDist) {\n  vec2 dc = destCoord();\n  vec4 sO = sample(image, samplerTransform(image, dc));\n  if (sO.r <= 0.001) return sO;\n  if (sO.r > 9.500000e-01) return vec4(sO.r, 1, 0, 1);\n  float R = sO.r * maxDist;\n  float dTheta = clamp(1.0 / (R + 2.200000e-01), 0.1, 7.500000e-01);\n  for (float t = 0.0; t < 3.141593e+00; t += dTheta) {\n    vec2 d = R * vec2(cos(t), sin(t));\n    vec4 s = sample(image, samplerTransform(image, dc + d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n    s = sample(image, samplerTransform(image, dc - d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n  }\n  return sO;\n}\n"
+ "kernel vec4 _horizAveMaxRed4(sampler image, float bound, float pass) {\n  vec2 d = vec2(4.0, 1.0) * destCoord();\n  vec4 p0 = sample(image, samplerTransform(image, d + vec2(-1.500, 0.0)));\n  vec4 p1 = sample(image, samplerTransform(image, d + vec2(-0.5, 0.0)));\n  vec4 p2 = sample(image, samplerTransform(image, d + vec2(+0.5, 0.0)));\n  vec4 p3 = sample(image, samplerTransform(image, d + vec2(+1.500, 0.0)));\n  vec2 am0 = (pass < 9.000000e-01) ? p0.rr : p0.rg;\n  vec2 am1 = (pass < 9.000000e-01) ? p1.rr : p1.rg;\n  vec2 am2 = (pass < 9.000000e-01) ? p2.rr : p2.rg;\n  vec2 am3 = (pass < 9.000000e-01) ? p3.rr : p3.rg;\n  am0.r = ((d.x - 0.5) < bound) ? (am0.r + am1.r) : am0.r;\n  am0.r = ((d.x + 0.5) < bound) ? (am0.r + am2.r) : am0.r;\n  am0.r = ((d.x + 1.500) < bound) ? (am0.r + am3.r) : am0.r;\n  am0.g = ((d.x - 0.5) < bound) ? max(am0.g, am1.g) : am0.g;\n  am0.g = ((d.x + 0.5) < bound) ? max(am0.g, am2.g) : am0.g;\n  am0.g = ((d.x + 1.500) < bound) ? max(am0.g, am3.g) : am0.g;\n  return vec4(am0.r * 0.25, am0.g, 0.0, 1.0);\n}\n"
+ "kernel vec4 _hueBlendMode_v0(vec4 pCf, vec4 pCb) {\n  vec4 uCf = unpremultiply(pCf);\n  vec4 uCb = unpremultiply(pCb);\n  vec4 uCfSort = (uCf.r > uCf.g) ? uCf : uCf.grba;\n  uCfSort = (uCfSort.g > uCfSort.b) ? uCfSort : uCfSort.rbga;\n  uCfSort = (uCfSort.r > uCfSort.g) ? uCfSort : uCfSort.grba;\n  vec4 uCbSort = (uCb.r > uCb.g) ? uCb : uCb.grba;\n  uCbSort = (uCbSort.g > uCbSort.b) ? uCbSort : uCbSort.rbga;\n  uCbSort = (uCbSort.r > uCbSort.g) ? uCbSort : uCbSort.grba;\n  vec4 Ct = ((uCfSort.b + 1e-5) > uCfSort.r) ? uCbSort.rbba : ((((uCf - uCfSort.b) * (uCbSort.r - uCbSort.b)) / (uCfSort.r - uCfSort.b)) + uCbSort.b);\n  Ct.a = uCb.a;\n  vec4 Cb = vec4(uCb.rgb * uCb.a, uCb.a);\n  Ct = mix(uCf, Ct, uCb.a);\n  Ct.a = 1.0;\n  return mix(Cb, Ct, uCf.a);\n}\n"
+ "kernel vec4 _jointBilateral(sampler small, sampler guide, vec4 parms) {\n  vec2 dc = destCoord();\n  vec2 smallCenter = samplerCoord(small);\n  vec2 guideCenter = samplerCoord(guide);\n  vec2 smallDelta = samplerTransform(small, dc + vec2(1.0)) - smallCenter;\n  vec2 guideDelta = samplerTransform(guide, dc + vec2(1.0)) - guideCenter;\n  vec4 I0 = sample(small, smallCenter);\n  float IE0 = sample(guide, guideCenter).r;\n  vec4 sumFGI = vec4(0.0);\n  float sumFG = 0.0;\n  float x, y;\n  float w = 2.0;\n  for (x = -w; x <= w; x++) {\n    for (y = -w; y <= w; y++) {\n      vec2 xy = vec2(x, y) * parms.zw;\n      float G = exp((-((x * x) + (y * y))) * parms.y);\n      vec4 I = sample(small, smallCenter + (xy * smallDelta));\n      float IE = sample(guide, guideCenter + (xy * guideDelta)).g;\n      float F = exp((-((IE - IE0) * (IE - IE0))) * parms.x);\n      sumFG += F * G;\n      sumFGI += (F * G) * I;\n    }\n  }\n  return (sumFG < 0.001) ? I0 : (sumFGI / sumFG);\n}\n"
+ "kernel vec4 _jointBilateralRG(sampler combo, vec4 parms) {\n  vec2 dc = destCoord();\n  vec2 comboCenter = samplerCoord(combo);\n  vec2 comboDelta = samplerTransform(combo, dc + vec2(1.0)) - comboCenter;\n  vec4 c = sample(combo, comboCenter);\n  vec2 I0 = c.zw;\n  float IE0 = c.r;\n  vec2 sumFGI = vec2(0.0);\n  float sumFG = 0.0;\n  float x, y;\n  float w = 2.0;\n  for (x = -w; x <= w; x++) {\n    for (y = -w; y <= w; y++) {\n      vec2 xy = vec2(x, y) * parms.zw;\n      float G = exp((-((x * x) + (y * y))) * parms.y);\n      vec4 c = sample(combo, comboCenter + (xy * comboDelta));\n      vec2 I = c.zw;\n      float IE = c.g;\n      float F = exp((-((IE - IE0) * (IE - IE0))) * parms.x);\n      sumFG += F * G;\n      sumFGI += (F * G) * I;\n    }\n  }\n  return vec4((sumFG < 0.001) ? I0 : (sumFGI / sumFG), 0.0, 1.0);\n}\n"
+ "kernel vec4 _linearToAppleLog(vec4 R) {\n  const float R0 = -5.641088e-02;\n  const float Rt = 0.01;\n  const float c = 4.728711e+01;\n  const float beta = 9.640520e-03;\n  const float gamma = 8.550479e-02;\n  const float delta = 6.933694e-01;\n  vec4 Pa = (gamma * log2(R + beta)) + delta;\n  vec4 Pb = (c * (R - R0)) * (R - R0);\n}\n"
+ "kernel vec4 _luminosityBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  float Ls = ((0.3 * Cs.r) + (0.59 * Cs.g)) + (0.11 * Cs.b);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  vec4 BB = Cb + vec4(Ls - Lb);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = (n < 0.0) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = (x > 1.0) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return (fore.a < 1e-6) ? back : (((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a));\n}\n"
+ "kernel vec4 _luminosityBlendMode_v0(vec4 pCf, vec4 pCb) {\n  vec4 uCf = unpremultiply(pCf);\n  vec4 uCb = unpremultiply(pCb);\n  vec4 uCbSort = (uCb.r > uCb.g) ? uCb : uCb.grba;\n  uCbSort = (uCbSort.g > uCbSort.b) ? uCbSort : uCbSort.rbga;\n  uCbSort = (uCbSort.r > uCbSort.g) ? uCbSort : uCbSort.grba;\n  float fL = (uCbSort.r + uCbSort.b) * 0.5;\n  float cmax = uCbSort.r;\n  float cmin = uCbSort.b;\n  vec4 uCfSort = (uCf.r > uCf.g) ? uCf : uCf.grba;\n  uCfSort = (uCfSort.g > uCfSort.b) ? uCfSort : uCfSort.rbga;\n  uCfSort = (uCfSort.r > uCfSort.g) ? uCfSort : uCfSort.grba;\n  float bL = (uCfSort.r + uCfSort.b) * 0.5;\n  float d = cmax - cmin;\n  float dv = (fL < 0.5) ? (cmax + cmin) : (2.0 - (cmax + cmin));\n  float s = d / max(dv, 1e-6);\n  float mmax = (bL <= 0.5) ? (bL + (bL * s)) : ((bL + s) - (bL * s));\n  float mmin = (bL * 2.0) - mmax;\n  vec4 Ct = (((uCb - uCbSort.b) * (mmax - mmin)) / (uCbSort.r - uCbSort.b)) + mmin;\n  Ct = ((mmin + 1e-5) > mmax) ? vec4(mmin) : Ct;\n  Ct.a = uCf.a;\n  vec4 Cf = vec4(uCf.rgb * uCf.a, uCf.a);\n  Ct = mix(uCb, Ct, uCf.a);\n  Ct.a = 1.0;\n  return mix(Cf, Ct, uCb.a);\n}\n"
+ "kernel vec4 _maskBoundsInit(vec4 c, vec2 invSize) {\n  float eps = 1.250000e-01;\n  vec2 dcLo = floor(destCoord()) - eps;\n  vec2 dcHi = (dcLo + 1.0) + (eps * 2.0);\n  if (c.r > 1e-5) return vec4(dcLo * invSize, dcHi * invSize);\n  return vec4(0, 0, 0, 0);\n}\n"
+ "kernel vec4 _maxGradOnly(sampler i) {\n  vec4 nonEdge = vec4(0.0, 0.0, 0.0, 1.0);\n  vec2 dc = destCoord();\n  vec4 s = sample(i, samplerCoord(i));\n  if (s.b < 1e-4) return nonEdge;\n  vec2 delta = normalize(s.rg);\n  vec4 sA = sample(i, samplerTransform(i, dc + delta));\n  vec4 sB = sample(i, samplerTransform(i, dc - delta));\n  if ((s.b > sA.b) && (s.b > sB.b)) return s;\n  return nonEdge;\n}\n"
+ "kernel vec4 _mesh1(vec4 pt1, float width, vec4 color, float opacity) {\n  float hw, dist, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist = compare((v.x * s.x) + (v.y * s.y), length(v), dist);\n  w = p - p2;\n  dist = compare((w.x * s.x) + (w.y * s.y), dist, length(w));\n  interpolant = clamp(hw - dist, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist - (hw - 1.0)), color, compare(vec4(dist - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
+ "kernel vec4 _mesh16(vec4 pt1, vec4 pt2, vec4 pt3, vec4 pt4, vec4 pt5, vec4 pt6, vec4 pt7, vec4 pt8, vec4 pt9, vec4 pt10, vec4 pt11, vec4 pt12, vec4 pt13, vec4 pt14, vec4 pt15, vec4 pt16, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt3.rg;\n  p2 = pt3.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt4.rg;\n  p2 = pt4.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt5.rg;\n  p2 = pt5.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt6.rg;\n  p2 = pt6.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt7.rg;\n  p2 = pt7.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt8.rg;\n  p2 = pt8.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt9.rg;\n  p2 = pt9.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt10.rg;\n  p2 = pt10.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt11.rg;\n  p2 = pt11.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt12.rg;\n  p2 = pt12.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt13.rg;\n  p2 = pt13.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt14.rg;\n  p2 = pt14.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt15.rg;\n  p2 = pt15.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt16.rg;\n  p2 = pt16.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
+ "kernel vec4 _mesh2(vec4 pt1, vec4 pt2, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
+ "kernel vec4 _mesh32(vec4 pt1, vec4 pt2, vec4 pt3, vec4 pt4, vec4 pt5, vec4 pt6, vec4 pt7, vec4 pt8, vec4 pt9, vec4 pt10, vec4 pt11, vec4 pt12, vec4 pt13, vec4 pt14, vec4 pt15, vec4 pt16, vec4 pt17, vec4 pt18, vec4 pt19, vec4 pt20, vec4 pt21, vec4 pt22, vec4 pt23, vec4 pt24, vec4 pt25, vec4 pt26, vec4 pt27, vec4 pt28, vec4 pt29, vec4 pt30, vec4 pt31, vec4 pt32, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt3.rg;\n  p2 = pt3.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt4.rg;\n  p2 = pt4.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt5.rg;\n  p2 = pt5.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt6.rg;\n  p2 = pt6.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt7.rg;\n  p2 = pt7.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt8.rg;\n  p2 = pt8.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt9.rg;\n  p2 = pt9.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt10.rg;\n  p2 = pt10.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt11.rg;\n  p2 = pt11.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt12.rg;\n  p2 = pt12.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt13.rg;\n  p2 = pt13.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt14.rg;\n  p2 = pt14.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt15.rg;\n  p2 = pt15.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt16.rg;\n  p2 = pt16.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt17.rg;\n  p2 = pt17.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt18.rg;\n  p2 = pt18.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt19.rg;\n  p2 = pt19.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt20.rg;\n  p2 = pt20.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt21.rg;\n  p2 = pt21.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt22.rg;\n  p2 = pt22.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt23.rg;\n  p2 = pt23.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt24.rg;\n  p2 = pt24.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt25.rg;\n  p2 = pt25.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt26.rg;\n  p2 = pt26.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt27.rg;\n  p2 = pt27.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt28.rg;\n  p2 = pt28.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt29.rg;\n  p2 = pt29.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt30.rg;\n  p2 = pt30.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt31.rg;\n  p2 = pt31.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt32.rg;\n  p2 = pt32.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
+ "kernel vec4 _mesh4(vec4 pt1, vec4 pt2, vec4 pt3, vec4 pt4, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt3.rg;\n  p2 = pt3.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt4.rg;\n  p2 = pt4.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
+ "kernel vec4 _mesh8(vec4 pt1, vec4 pt2, vec4 pt3, vec4 pt4, vec4 pt5, vec4 pt6, vec4 pt7, vec4 pt8, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt3.rg;\n  p2 = pt3.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt4.rg;\n  p2 = pt4.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt5.rg;\n  p2 = pt5.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt6.rg;\n  p2 = pt6.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt7.rg;\n  p2 = pt7.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt8.rg;\n  p2 = pt8.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 0.01));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
+ "kernel vec4 _minMaxNormalize(vec4 c, vec4 minc, vec4 maxc) {\n  c.rgb = (c.rgb - minc.rgb) / max(maxc.rgb - minc.rgb, 1e-5);\n  return c;\n}\n"
+ "kernel vec4 _minMaxRedNormalize(vec4 c, vec4 minmaxc) {\n  c.r = (c.r - minmaxc.r) / max(minmaxc.g - minmaxc.r, 1e-5);\n  return c;\n}\n"
+ "kernel vec4 _narrowBlur15(sampler s, vec2 dir) {\n  vec4 v = vec4(0.0);\n  float weights[8];\n  weights[0] = 1.176960e-01;\n  weights[1] = 1.129890e-01;\n  weights[2] = 9.996680e-02;\n  weights[3] = 8.151250e-02;\n  weights[4] = 6.125480e-02;\n  weights[5] = 4.242320e-02;\n  weights[6] = 2.707780e-02;\n  weights[7] = 1.592840e-02;\n  vec2 dc = destCoord();\n  for (int i = 7; i > 0; i--) {\n    v += sample(s, samplerTransform(s, dc + (float(i) * dir))) * weights[i];\n    v += sample(s, samplerTransform(s, dc - (float(i) * dir))) * weights[i];\n  }\n  v += sample(s, samplerCoord(s)) * weights[0];\n  return v;\n}\n"
+ "kernel vec4 _pageCurlTransNoEmap(sampler front, sampler back, vec4 cyl, vec2 cyloff, vec4 fbrot, vec2 fboff, vec4 hi, vec2 hioff, float radius) {\n  vec2 backPt;\n  vec2 d = destCoord();\n  vec2 frontPt = backPt = vec2(dot(d, cyl.xy), dot(d, cyl.zw)) + cyloff;\n  float f = frontPt.x;\n  float asn = sqrt(max(1.0 - pow(frontPt.x, 1.500), 0.0)) - 1.0;\n  float v = frontPt.x + ((asn * asn) * 5.625000e-01);\n  frontPt.x = v;\n  backPt.x = 3.141593e+00 - v;\n  frontPt = vec2(dot(frontPt, fbrot.xy), dot(frontPt, fbrot.zw)) + fboff;\n  backPt = vec2(dot(backPt, fbrot.xy), dot(backPt, fbrot.zw)) + fboff;\n  frontPt = (f <= 0.0) ? d : frontPt;\n  vec2 highPt = vec2(dot(d, hi.xy), dot(d, hi.zw)) + hioff;\n  backPt = (f <= 0.0) ? highPt : backPt;\n  vec4 fs = sample(front, samplerTransform(front, frontPt));\n  vec4 bs = sample(back, samplerTransform(back, backPt));\n  vec4 pix = bs + ((1.0 - bs.a) * fs);\n  pix *= clamp((1.0 - f) * radius, 0.0, 1.0);\n  return pix;\n}\n"
+ "kernel vec4 _pageCurlTransition(sampler front, sampler back, sampler emap, vec4 cyl, vec2 cyloff, vec4 fbrot, vec2 fboff, vec4 hi, vec2 hioff, float radius, vec4 emapExtent) {\n  vec2 backPt;\n  vec2 d = destCoord();\n  vec2 frontPt = backPt = vec2(dot(d, cyl.xy), dot(d, cyl.zw)) + cyloff;\n  float f = frontPt.x;\n  float asn = sqrt(max(1.0 - pow(frontPt.x, 1.500), 0.0)) - 1.0;\n  float v = frontPt.x + ((asn * asn) * 5.625000e-01);\n  frontPt.x = v;\n  backPt.x = 3.141593e+00 - v;\n  frontPt = vec2(dot(frontPt, fbrot.xy), dot(frontPt, fbrot.zw)) + fboff;\n  backPt = vec2(dot(backPt, fbrot.xy), dot(backPt, fbrot.zw)) + fboff;\n  frontPt = (f <= 0.0) ? d : frontPt;\n  vec2 highPt = vec2(dot(d, hi.xy), dot(d, hi.zw)) + hioff;\n  backPt = (f <= 0.0) ? highPt : backPt;\n  vec4 fs = sample(front, samplerTransform(front, frontPt));\n  vec4 bs = sample(back, samplerTransform(back, backPt));\n  vec2 n = clamp((f * radius) * cyl.xy, -1.0, 1.0);\n  vec2 bn0 = (f < 0.0) ? vec2(0.0) : n;\n  bn0 = (bn0 * 0.5) + 0.5;\n  bn0 = (bn0 * emapExtent.zw) + emapExtent.xy;\n  vec4 es = sample(emap, samplerTransform(emap, bn0));\n  es *= bs.a;\n  bs = es + ((1.0 - es.a) * bs);\n  vec4 pix = bs + ((1.0 - bs.a) * fs);\n  pix *= clamp((1.0 - f) * radius, 0.0, 1.0);\n  return pix;\n}\n"
+ "kernel vec4 _perc_norm_red(vec4 c, vec4 minmax) {\n  c.r = max((c.r - minmax.r) / max(minmax.g - minmax.r, 1e-5), 0.0);\n  return c;\n}\n"
+ "kernel vec4 _perspectiveMask(vec4 p, vec3 A3) {\n  return p * ((dot(vec3(destCoord(), 1.0), A3) < 1e-6) ? 0.0 : 1.0);\n}\n"
+ "kernel vec4 _redThreshold(vec4 c) {\n  return (c.r > 1e-5) ? vec4(1, 0, 0, 1) : vec4(0, 0, 0, 1);\n}\n"
+ "kernel vec4 _reduceCropAveMaxRed(sampler image, float scale) {\n  vec4 p = sample(image, samplerTransform(image, vec2(0.5, 0.5)));\n  vec2 d = abs(destCoord() - 0.5);\n  return (max(d.x, d.y) < 0.5) ? vec4(p.r * scale, p.g, 0.0, 1.0) : vec4(0.0);\n}\n"
+ "kernel vec4 _remap01FromMinus1ToPlus1(vec4 s) {\n  float v = 1.0 - ((s.x + 1.0) / 2.0);\n  return vec4(v, v, v, 1.0);\n}\n"
+ "kernel vec4 _roundedrect(vec4 bounds, float radius, vec2 smooths, vec4 color) {\n  vec2 p = destCoord();\n  vec2 lo = bounds.xy;\n  vec2 hi = bounds.zw;\n  float R = radius;\n  vec2 Rs = vec2(smooths);\n  vec2 cl = (lo + R) + (R * Rs);\n  vec2 ch = (hi - R) - (R * Rs);\n  vec2 k = max((4.0 * R) * Rs, 1e-6);\n  vec2 xl = cl - (0.5 * k);\n  vec2 xh = ch + (0.5 * k);\n  p = compare(p - xl, p - (lo + R), compare(p - cl, ((-(p - cl)) * (p - cl)) / k, compare(p - ch, vec2(0.0), compare(p - xh, ((p - ch) * (p - ch)) / k, p - (hi - R)))));\n  return color * clamp((R - length(p)) + 0.5, 0.0, 1.0);\n}\n"
+ "kernel vec4 _roundedstroke(vec4 bounds, float radius, vec4 smooths, float width, vec4 color) {\n  vec2 p = destCoord();\n  vec2 lo = bounds.xy;\n  vec2 hi = bounds.zw;\n  float R = radius;\n  vec2 Rs = vec2(smooths.xy);\n  vec2 cl = (lo + R) + (R * Rs);\n  vec2 ch = (hi - R) - (R * Rs);\n  vec2 k = max((4.0 * R) * Rs, 1e-6);\n  vec2 xl = cl - (0.5 * k);\n  vec2 xh = ch + (0.5 * k);\n  vec2 p0 = compare(p - xl, p - (lo + R), compare(p - cl, ((-(p - cl)) * (p - cl)) / k, compare(p - ch, vec2(0.0), compare(p - xh, ((p - ch) * (p - ch)) / k, p - (hi - R)))));\n  float k0 = (R - length(p0)) + 0.5;\n  k0 = clamp(k0, 0.0, 1.0);\n  lo = bounds.xy + width;\n  hi = bounds.zw - width;\n  R = max(0.5, radius - width);\n  Rs = vec2(smooths.zw);\n  cl = (lo + R) + (R * Rs);\n  ch = (hi - R) - (R * Rs);\n  k = (4.0 * R) * Rs;\n  xl = cl - (0.5 * k);\n  xh = ch + (0.5 * k);\n  vec2 p1 = compare(p - xl, p - (lo + R), compare(p - cl, ((-(p - cl)) * (p - cl)) / k, compare(p - ch, vec2(0.0), compare(p - xh, ((p - ch) * (p - ch)) / k, p - (hi - R)))));\n  float k1 = (R - length(p1)) + 0.5;\n  k1 = clamp(k1, 0.0, 1.0);\n  return (color * k0) * (1.0 - k1);\n}\n"
+ "kernel vec4 _saturationBlendMode_v0(vec4 pCf, vec4 pCb) {\n  vec4 uCf = unpremultiply(pCf);\n  vec4 uCb = unpremultiply(pCb);\n  vec4 uCfSort = (uCf.r > uCf.g) ? uCf : uCf.grba;\n  uCfSort = (uCfSort.g > uCfSort.b) ? uCfSort : uCfSort.rbga;\n  uCfSort = (uCfSort.r > uCfSort.g) ? uCfSort : uCfSort.grba;\n  float fL = (uCfSort.r + uCfSort.b) * 0.5;\n  float cmax = uCfSort.r;\n  float cmin = uCfSort.b;\n  vec4 uCbSort = (uCb.r > uCb.g) ? uCb : uCb.grba;\n  uCbSort = (uCbSort.g > uCbSort.b) ? uCbSort : uCbSort.rbga;\n  uCbSort = (uCbSort.r > uCbSort.g) ? uCbSort : uCbSort.grba;\n  float bL = (uCbSort.r + uCbSort.b) * 0.5;\n  float d = cmax - cmin;\n  float dv = (fL < 0.5) ? (cmax + cmin) : (2.0 - (cmax + cmin));\n  float s = d / max(dv, 1e-6);\n  float mmax = (bL <= 0.5) ? (bL + (bL * s)) : ((bL + s) - (bL * s));\n  float mmin = (bL * 2.0) - mmax;\n  vec4 Ct = ((uCbSort.b + 1e-5) > uCbSort.r) ? vec4(mmax, mmin, mmin, 1.0) : ((((uCb - uCbSort.b) * (mmax - mmin)) / (uCbSort.r - uCbSort.b)) + mmin);\n  Ct.a = uCb.a;\n  vec4 Cb = vec4(uCb.rgb * uCb.a, uCb.a);\n  Ct = mix(uCf, Ct, uCb.a);\n  Ct.a = 1.0;\n  return mix(Cb, Ct, uCf.a);\n}\n"
+ "kernel vec4 _sdfFill(vec4 s, vec4 fwidth) {\n  float r = fwidth.x * 0.5;\n  float c = smoothstep(-r, r, s.x);\n  return vec4(c, 0.0, 0.0, 1.0);\n}\n"
+ "kernel vec4 _sepia(vec4 s, float amount) {\n  vec3 color = vec3(1.0, 9.900000e-01, 9.200000e-01);\n  vec4 c0 = vec4(8.956630e-04, -1.104567e-03, -6.082700e-04, 3.277428e-02);\n  vec4 c1 = vec4(3.116672e+00, 7.926372e-01, 3.219686e-02, 1.411847e+00);\n  vec4 c2 = vec4(-5.093341e+01, 4.654831e-01, 1.027555e+00, -9.069088e-01);\n  vec4 c3 = vec4(7.087939e+02, -3.903106e-01, -5.854013e-02, 6.621023e-01);\n  vec4 c4 = vec4(-3.605984e+03, 1.323156e-01, 0.0, -1.991615e-01);\n  float l = dot(s.rgb, vec3(2.125000e-01, 7.154000e-01, 7.210000e-02));\n  float la = l / max(1e-4, s.a);\n  vec4 t = (c0 * s.a) + ((c1 + ((c2 + ((c3 + (c4 * la)) * la)) * la)) * l);\n  t.r = (l < (8.500000e-02 * s.a)) ? t.r : t.a;\n  vec3 r = (((l * l) - l) < 0.0) ? t.rgb : vec3(l, l, l);\n  return vec4(mix(s.rgb, r * color, amount), s.a);\n}\n"
+ "kernel vec4 _shadowKernel(vec4 im, vec4 adj, float str) {\n  adj.r = (3.400 * adj.r) - 1.200;\n  vec3 neg = min(im.rgb, 0.0);\n  vec3 pos = max(im.rgb, 1.0) - 1.0;\n  im.rgb = clamp(im.rgb, 0.0, 1.0);\n  float y = sqrt(dot(im.rgb, vec3(3.333300e-01)));\n  float s = mix(0.0, adj.r, str);\n  vec3 gain = (s > 0.0) ? vec3(0.0 * s) : vec3(((-2.750) * s) * s, ((-2.750) * s) * s, ((-2.500) * s) * s);\n  im.rgb = ((im.rgb * im.rgb) * gain) + (im.rgb * (1.0 - gain));\n  float m = 1.0 + ((1.850 * s) * max(0.1 - y, 0.0));\n  im.rgb = clamp(m * im.rgb, 0.0, 1.0);\n  float midAmt = (s < 0.0) ? min(s * s, 1.0) : 0.0;\n  y = y * (1.0 - y);\n  im.rgb = sqrt(im.rgb);\n  float pivot = 4.000000e-01;\n  float a = midAmt * y;\n  float b = (-pivot) * a;\n  vec3 pix = ((((im.r * vec3(0.299 * a)) + (im.g * vec3(0.587 * a))) + (im.b * vec3(0.114 * a))) + im.rgb) + vec3(b);\n  im.rgb = mix(im.rgb, vec3(pivot), (-y) * midAmt);\n  im.rgb = mix(im.rgb, pix, 8.000000e-01);\n  im.rgb = max(im.rgb, 0.0);\n  im.rgb *= im.rgb;\n  im.rgb = (clamp(im.rgb, 0.0, 1.0) + pos) + neg;\n  return im;\n}\n"
+ "kernel vec4 _shadows_noblur(vec4 pix, vec4 params) {\n  vec4 blur = pix;\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(0.001, (pix.r + pix.g) + pix.b);\n  rgbFactor = clamp(rgbFactor, 0.0, 1.0);\n  float shadAmt = params.x * pow(rgbFactor, max(0.0, 1.0 - params.x));\n  vec3 clamped = clamp(pix.rgb, 1e-5, 9.999900e-01);\n  float gray = ((clamped.r + clamped.g) + clamped.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  float rgbsat = max((clamped.r - gray) * gii, (gray - clamped.r) * gi);\n  float skin = min(1.0, ((max(0.0, min(clamped.r - clamped.g, (clamped.g * 2.0) - clamped.b)) * 4.0) * (1.0 - rgbsat)) * gi);\n  skin = 1.500000e-01 + (skin * 7.000000e-01);\n  vec3 rgbExp = pow(vec3(2.0), (-shadAmt) - blur.rgb);\n  float uniformExp = min(rgbExp.r, min(rgbExp.g, rgbExp.b));\n  vec3 shadExp = mix(rgbExp, vec3(uniformExp), skin);\n  float nopMix = params.z;\n  shadExp = mix(shadExp, vec3(1.0, 1.0, 1.0), nopMix);\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * 0.5, shadExp)) * 2.0;\n  float maxChan = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(maxChan);\n  float origPercent = sqrt(smoothstep(0.0, 0.1 + ((0.5 * shadAmt) * shadAmt), blurLum));\n  origPercent *= 1.0 - origPercent;\n  shad = mix(shad, pix.rgb, origPercent);\n  vec4 result;\n  result.rgb = mix(shad, pix.rgb, blurLum);\n  float Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  vec3 mid = mix(vec3(0.5), result.rgb, 1.0 + (abs(shadAmt) * 5.000000e-02));\n  result.rgb = mix(result.rgb, mid.rgb, min(effectAmount, (3.000000e+01 * blurLum) * blurLum));\n  result.a = pix.a;\n  return result;\n}\n"
+ "kernel vec4 _sharpenCombineEdges(vec4 orig, vec4 blurs, vec3 sharps, vec4 edges) {\n  vec4 so = vec4(orig.rgb / max(orig.a, 1e-5), orig.a);\n  float Y = blurs.r + dot(blurs.r - blurs.gba, sharps);\n  so.rgb = ((vec3(Y * Y) + (so.r * vec3(7.014280e-01, -2.992760e-01, -2.977560e-01))) + (so.g * vec3(-5.881610e-01, 4.133170e-01, -5.857185e-01))) + (so.b * vec3(-1.137450e-01, -1.139050e-01, 8.840270e-01));\n  float alpha = edges.x;\n  so = vec4(so.rgb * so.a, so.a);\n  return mix(orig, so, alpha);\n}\n"
+ "kernel vec4 _smartBlackAndWhite(vec4 image, sampler2D hueImage, vec4 rgbWeights, vec4 normalizer) {\n  float scaleFactor = rgbWeights.w;\n  float neutralGamma = normalizer.z;\n  float phototone = normalizer.w;\n  image = clamp(image, 0.0, 1.0);\n  vec3 lms;\n  lms.x = dot(image.rgb, vec3(3.139902e-01, 6.395130e-01, 4.649755e-02));\n  lms.y = dot(image.rgb, vec3(1.553724e-01, 7.578945e-01, 8.670142e-02));\n  lms.z = dot(image.rgb, vec3(1.775239e-02, 1.094421e-01, 8.725692e-01));\n  lms = pow(lms, vec3(4.300000e-01));\n  float i = dot(lms, vec3(4.000000e-01, 4.000000e-01, 2.000000e-01));\n  float p = dot(lms, vec3(4.455, -4.851, 3.960000e-01));\n  float t = dot(lms, vec3(8.056000e-01, 3.572000e-01, -1.1628));\n  float chroma = sqrt((p * p) + (t * t));\n  float hue = 0.5 + (atan(t, p) / 6.283185e+00);\n  vec2 huePt = vec2((hue * normalizer.x) + normalizer.y, 0.5);\n  float exponent = scaleFactor * texture2D(hueImage, huePt).a;\n  float cd = 6.000000e-02 + (5.300000e-01 * abs(i - 0.5));\n  float lumDamp = smoothstep(0.0, 1.0, 2.500000e+01 * i);\n  float x = smoothstep(0.0, 1.0, chroma / cd);\n  exponent = (((x * (1.0 - i)) * lumDamp) * (exponent - 1.0)) + 1.0;\n  float bw = dot(image.rgb, rgbWeights.rgb);\n  bw = pow(bw, exponent);\n  x = 1.0 - smoothstep(0.0, 1.0, chroma * 10.0);\n  float lumAdjust = (((bw * (1.0 - bw)) * x) * (neutralGamma - 1.0)) + 1.0;\n  lumAdjust = 5.0 - (4.0 * lumAdjust);\n  bw = pow(bw, lumAdjust);\n  float result = ((((1.8031 * bw) * bw) * bw) - ((2.1972 * bw) * bw)) + (1.3823 * bw);\n  bw = mix(bw, result, -phototone);\n  return vec4(bw, bw, bw, image.a);\n}\n"
+ "kernel vec4 _smartcolor_cast(vec4 im, float lum, float grayI, float grayQ, float strength) {\n  vec4 pix = clamp(im, 0.0, 1.0);\n  pix.rgb = pow(pix.rgb, vec3(0.25));\n  pix.rgb = ((pix.r * vec3(0.299, 5.957160e-01, 2.114560e-01)) + (pix.g * vec3(0.587, -2.744530e-01, -5.225910e-01))) + (pix.b * vec3(0.114, -3.212630e-01, 3.111350e-01));\n  vec2 grayOffset = vec2(grayI, grayQ);\n  vec3 result = pix.rgb;\n  float newStrength = 1.0 + ((strength - 1.0) * (1.0 - pix.r));\n  result.gb = pix.gb + (newStrength * grayOffset);\n  float damp = max(min(1.0, pix.r / (lum + 1e-5)), 0.0);\n  result.rgb = mix(pix.rgb, result.rgb, damp);\n  pix.rgb = ((result.r * vec3(1.0)) + (result.g * vec3(9.562960e-01, -2.721220e-01, -1.10699))) + (result.b * vec3(6.210240e-01, -6.473810e-01, 1.70461));\n  pix.rgb = clamp(pix.rgb, 0.0, 1.0);\n  pix.rgb *= (pix.rgb * pix.rgb) * pix.rgb;\n  pix.rgb += (min(im.rgb, 0.0) + max(im.rgb, 1.0)) - 1.0;\n  return pix;\n}\n"
+ "kernel vec4 _smartcolor_vibrancy_gt1(vec4 im, float amt) {\n  float gray = dot(clamp(im.rgb, 0.0, 1.0), vec3(0.3, 0.5, 2.000000e-01));\n  float y = dot(clamp(im.rgb, 0.0, 1.0), vec3(4.000000e-01, 2.000000e-01, 0.1));\n  float damp = 1.0 - ((4.0 * y) * (1.0 - y));\n  float s = 1.0 / ((im.r + im.g) + im.b);\n  float r = im.r * s;\n  float b = im.b * s;\n  float d = 1.0 - (8.000000e-01 * smoothstep(2.000000e-01, 4.000000e-01, r - b));\n  damp *= d;\n  damp = (amt > 2.500) ? min(damp + ((amt - 2.500) / 5.0), 1.0) : damp;\n  float sat = min(amt, 3.0);\n  vec4 result;\n  result.rgb = ((im.rgb - gray) * sat) + gray;\n  result.rgb = mix(im.rgb, result.rgb, damp);\n  result.a = im.a;\n  return result;\n}\n"
+ "kernel vec4 _sobelEdges(sampler src, float scale) {\n  vec2 coord = destCoord();\n  vec2 sc = samplerTransform(src, coord);\n  vec2 dx = samplerTransform(src, coord + vec2(1.0, 0.0)) - sc;\n  vec2 dy = samplerTransform(src, coord + vec2(0.0, 1.0)) - sc;\n  vec2 d = dx + dy;\n  vec4 pix3 = sample(src, sc + d);\n  vec4 pix7 = sample(src, sc - d);\n  d = dx - dy;\n  vec4 pix9 = sample(src, sc + d);\n  vec4 pix1 = sample(src, sc - d);\n  vec4 pix2 = sample(src, sc + dy);\n  vec4 pix8 = sample(src, sc - dy);\n  vec4 pix6 = sample(src, sc + dx);\n  vec4 pix4 = sample(src, sc - dx);\n  vec4 pix5 = sample(src, sc);\n  vec4 gx = ((pix3 + (2.0 * pix6)) + pix9) - ((pix1 + (2.0 * pix4)) + pix7);\n  vec4 gy = ((pix1 + (2.0 * pix2)) + pix3) - ((pix7 + (2.0 * pix8)) + pix9);\n  vec4 g2 = (gx * gx) + (gy * gy);\n  pix5 = vec4(pix5.rgb / max(pix5.a, 1e-5), pix5.a);\n  pix5.rgb = sqrt(g2).rgb * scale;\n  return vec4(pix5.rgb * pix5.a, pix5.a);\n}\n"
+ "kernel vec4 _sparserendering_add_noise(vec4 inputTex, vec4 noiseLumaTex, vec2 params) {\n  float lumaNoiseModelCoeff = params.x;\n  float lumaNoiseAmpl = params.y;\n  vec4 pixBlurred = inputTex;\n  float noiseLuma = (noiseLumaTex.x * 10.0) - 5.0;\n  vec3 kRGB_to_Y = vec3(0.299, 0.587, 0.114);\n  float outLuma = dot(pixBlurred.xyz, kRGB_to_Y);\n  float addLumaNoiseLevel = lumaNoiseAmpl * mix(1.0, outLuma, lumaNoiseModelCoeff);\n  vec4 pixOut;\n  pixOut.xyz = clamp(pixBlurred.xyz + (noiseLuma * addLumaNoiseLevel), vec3(0.0), vec3(1.0));\n  pixOut.w = pixBlurred.w;\n  return clamp(pixOut, vec4(0.0), vec4(1.0));\n}\n"
+ "kernel vec4 _spotColor(vec4 src, vec4 cclr1, vec4 rclr1, vec4 cclr2, vec4 rclr2, vec4 cclr3, vec4 rclr3, vec4 closeness, vec4 contrast) {\n  vec4 pix = vec4(src.rgb / max(src.a, 1e-5), src.a);\n  float dist = length(pix.rgb - cclr1.rgb);\n  float alpha = clamp(((closeness.x - dist) * contrast.x) + 0.5, 0.0, 1.0);\n  vec4 result1 = rclr1 * alpha;\n  dist = length(pix.rgb - cclr2.rgb);\n  alpha = clamp(((closeness.y - dist) * contrast.y) + 0.5, 0.0, 1.0);\n  vec4 result2 = rclr2 * alpha;\n  dist = length(pix.rgb - cclr3.rgb);\n  alpha = clamp(((closeness.z - dist) * contrast.z) + 0.5, 0.0, 1.0);\n  vec4 result3 = rclr3 * alpha;\n  pix = result1 + ((1.0 - result1.a) * vec4(1.0));\n  pix = result2 + ((1.0 - result2.a) * pix);\n  return result3 + ((1.0 - result3.a) * pix);\n}\n"
+ "kernel vec4 _starshine(vec2 center, vec4 xyvec, vec4 parms, float widthrecip, vec4 color) {\n  vec2 offset = destCoord() - center;\n  vec2 loc = vec2(dot(offset, xyvec.xy), dot(offset, xyvec.zw));\n  float l = length(offset);\n  float rlen = parms.x / l;\n  loc = max((abs(loc) * widthrecip) + parms.w, vec2(1e-7));\n  loc = abs(parms.x / loc);\n  loc = (loc * loc) * loc;\n  float f = (loc.x * loc.y) * parms.z;\n  float g = clamp(1.0 - (l * parms.y), 0.0, 1.0);\n  vec4 result = ((rlen * rlen) * color) + ((g * g) * f);\n  result.a = min(result.a, 1.0);\n  return result;\n}\n"
+ "kernel vec4 _sunbeams(sampler noise, vec4 centers, vec4 params, vec4 color) {\n  float sunRadius2 = params.x;\n  float striationFactor = params.y;\n  float a = params.z;\n  float b = params.w;\n  vec2 v = destCoord() - centers.xy;\n  float len = length(v);\n  float len2 = dot(v, v);\n  vec2 noiseCtr = centers.zw;\n  vec2 noiseLoc = (normalize(v) * 5.000000e+01) + noiseCtr;\n  vec4 npix = sample(noise, samplerTransform(noise, noiseLoc));\n  float noiseAmount = (npix.r * a) + b;\n  float f2 = sunRadius2 / (len2 + 1e-4);\n  vec4 pix = (f2 * color) + noiseAmount;\n  pix *= clamp(1.0 - (len * striationFactor), 0.0, 1.0);\n  pix.a = clamp(pix.a, 0.0, 1.0);\n  return pix;\n}\n"
+ "kernel vec4 _torusRefraction(sampler src, vec2 center, float a, float b, float c, float indexOfRefraction, float levitation) {\n  vec2 v0 = destCoord() - center;\n  float dist = length(v0);\n  vec2 unitvec = normalize(v0);\n  float fdom = (a * dist) + b;\n  float alpha = clamp((1.0 - abs(fdom)) * c, 0.0, 1.0);\n  vec3 surfaceNormal = vec3(unitvec * fdom, sqrt(1.0 - (fdom * fdom)));\n  float surfaceHeight = (surfaceNormal.z * c) + levitation;\n  vec3 rayOrigin = vec3(destCoord(), surfaceHeight);\n  float eta = 1.0 / indexOfRefraction;\n  float c1 = surfaceNormal.z;\n  float cs2 = 1.0 - ((eta * eta) * (1.0 - (c1 * c1)));\n  vec3 rayDirection = eta * vec3(0.0, 0.0, -1.0);\n  c1 = (eta * c1) - sqrt(abs(cs2));\n  rayDirection += c1 * surfaceNormal;\n  float t = (-surfaceHeight) / rayDirection.z;\n  vec3 hitPoint = rayOrigin + (t * rayDirection);\n  if (alpha < 0.001) hitPoint.xy = vec2(5.000000e+01);\n  vec4 color = sample(src, samplerTransform(src, hitPoint.xy));\n  color = (cs2 < 0.0) ? vec4(0.0, 0.0, 0.0, 0.0) : color;\n  vec4 unrefracted = sample(src, samplerCoord(src));\n  return mix(unrefracted, color, alpha);\n}\n"
+ "kernel vec4 _unsharpmask(vec4 s, vec4 b, float k) {\n  s.rgb += (s.rgb - (b.rgb * (s.a / max(b.a, 1e-4)))) * k;\n  return s;\n}\n"
+ "kernel vec4 _vertAveMaxRed4(sampler image, float bound, float pass) {\n  vec2 d = vec2(1.0, 4.0) * destCoord();\n  vec4 p0 = sample(image, samplerTransform(image, d + vec2(0.0, -1.500)));\n  vec4 p1 = sample(image, samplerTransform(image, d + vec2(0.0, -0.5)));\n  vec4 p2 = sample(image, samplerTransform(image, d + vec2(0.0, +0.5)));\n  vec4 p3 = sample(image, samplerTransform(image, d + vec2(0.0, +1.500)));\n  vec2 am0 = (pass < 9.000000e-01) ? p0.rr : p0.rg;\n  vec2 am1 = (pass < 9.000000e-01) ? p1.rr : p1.rg;\n  vec2 am2 = (pass < 9.000000e-01) ? p2.rr : p2.rg;\n  vec2 am3 = (pass < 9.000000e-01) ? p3.rr : p3.rg;\n  am0.r = ((d.y - 0.5) < bound) ? (am0.r + am1.r) : am0.r;\n  am0.r = ((d.y + 0.5) < bound) ? (am0.r + am2.r) : am0.r;\n  am0.r = ((d.y + 1.500) < bound) ? (am0.r + am3.r) : am0.r;\n  am0.g = ((d.y - 0.5) < bound) ? max(am0.g, am1.g) : am0.g;\n  am0.g = ((d.y + 0.5) < bound) ? max(am0.g, am2.g) : am0.g;\n  am0.g = ((d.y + 1.500) < bound) ? max(am0.g, am3.g) : am0.g;\n  return vec4(am0.r * 0.25, am0.g, 0.0, 1.0);\n}\n"
+ "kernel vec4 _vibrance_neg(vec4 pixel0, float vibrance) {\n  vec4 pixel = clamp(pixel0, 1e-4, 0.9999);\n  vec4 pdelta = pixel0 - pixel;\n  float gray = ((pixel.r + pixel.g) + pixel.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  vec3 rgbsat = max((pixel.rgb - gray) * gii, (gray - pixel.rgb) * gi);\n  float sat = max(max(rgbsat.r, rgbsat.g), rgbsat.b);\n  float skin = ((min(pixel.r - pixel.g, (pixel.g * 2.0) - pixel.b) * 4.0) * (1.0 - rgbsat.r)) * gi;\n  skin = 1.500000e-01 + (clamp(skin, 0.0, 1.0) * 7.000000e-01);\n  float boost = (((sat * (sat - 1.0)) + 1.0) * vibrance) * (1.0 - skin);\n  pixel = clamp(pixel + ((pixel - gray) * boost), 0.0, 1.0);\n  pixel.a = pixel0.a;\n  pixel.rgb += pdelta.rgb;\n  return pixel;\n}\n"
+ "kernel vec4 _vibrance_pos(vec4 pixel0, vec4 vvec) {\n  vec4 pixel = clamp(pixel0, 1e-4, 0.9999);\n  vec4 pdelta = pixel0 - pixel;\n  float gray = ((pixel.r + pixel.g) + pixel.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  vec3 rgbsat = max((pixel.rgb - gray) * gii, (gray - pixel.rgb) * gi);\n  float sat = max(max(rgbsat.r, rgbsat.g), rgbsat.b);\n  float skin = ((min(pixel.r - pixel.g, (pixel.g * 2.0) - pixel.b) * 4.0) * (1.0 - rgbsat.r)) * gi;\n  skin = 1.500000e-01 + (clamp(skin, 0.0, 1.0) * 7.000000e-01);\n  float boost = dot(vvec, vec4(1.0, sat, sat * sat, (sat * sat) * sat)) * (1.0 - skin);\n  pixel = clamp(pixel + ((pixel - gray) * boost), 0.0, 1.0);\n  pixel.a = pixel0.a;\n  pixel.rgb += pdelta.rgb;\n  return pixel;\n}\n"
+ "kernel vec4 _vignetteeffect(vec4 s, vec2 center, vec4 params) {\n  vec2 point = (destCoord() - center) * params.x;\n  float dist = sqrt(dot(point, point));\n  float x = clamp((dist - params.y) * params.z, 0.0, 1.0);\n  x = ((x * x) * x) * ((((6.0 * x) - 1.500000e+01) * x) + 10.0);\n  float v = 1.0 - (x * params.w);\n  v = (((((((-1.206385e-01) * v) + 5.438787e-01) * v) + 5.387726e-01) * v) + 3.760100e-02) * v;\n  s.rgb *= v;\n  return s;\n}\n"
+ "kernel vec4 _vignetteeffectneg(vec4 s, vec2 center, vec4 params) {\n  vec2 point = (destCoord() - center) * params.x;\n  float dist = sqrt(dot(point, point));\n  float x = clamp((dist - params.y) * params.z, 0.0, 1.0);\n  x = ((x * x) * x) * ((((6.0 * x) - 1.500000e+01) * x) + 10.0);\n  float v = ((16.0 * x) * params.w) + 1.0;\n  s.rgb *= v;\n  return s;\n}\n"
+ "kernel vec4 _vividLightBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 epsilon = vec4(1e-7);\n  vec4 lo = 1.0 - ((1.0 - Cb) / max(2.0 * Cs, epsilon));\n  vec4 hi = Cb / max(2.0 * (1.0 - Cs), epsilon);\n  vec4 B = compare(0.5 - Cs, hi, lo);\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
+ "kernel vec4 _xSmooth(sampler image) {\n  float v;\n  float sum = 0.0;\n  float minv = 100.0;\n  vec2 dc = destCoord();\n  for (int i = -4; i < 5; i++) {\n    v = sample(image, samplerTransform(image, dc + vec2(float(i), 0.0))).r;\n    sum += (v * v) * 1.111111e-01;\n    minv = min(minv, v);\n  }\n  return vec4(sqrt(sum), minv, 0.0, 1.0);\n}\n"
+ "kernel vec4 _ySmooth(sampler image, sampler reference, vec4 blurValues) {\n  vec2 v;\n  float sum = 0.0;\n  float minv = 100.0;\n  vec2 dc = destCoord();\n  for (int i = -4; i < 5; i++) {\n    v = sample(image, samplerTransform(image, dc + vec2(0.0, float(i)))).rg;\n    sum += (v.r * v.r) * 1.111111e-01;\n    minv = min(minv, v.g);\n  }\n  sum = sqrt(sum);\n  float refT0 = blurValues.x;\n  float refT1 = blurValues.y;\n  float minT0 = blurValues.z;\n  float minT1 = blurValues.w;\n  float ref = sample(reference, samplerCoord(reference)).x;\n  float mixWeight = smoothstep(refT0, refT1, ref) * smoothstep(minT0, minT1, minv);\n  float result = mix(ref, sum, mixWeight);\n  return vec4(result, 0.0, 0.0, 1.0);\n}\n"
+ "kernel vec4 _zoom(sampler src, vec2 center, float k) {\n  vec2 dist = destCoord() - center;\n  vec4 result = vec4(0.0);\n  for (int n = 0; n < 100; n++) {\n    float f = float(n) / 9.900000e+01;\n    f -= 0.5;\n    f = ((f + ((f * f) * f)) * 8.000000e-01) + 0.5;\n    vec2 p = dist * mix(k, 1.0, f);\n    result += sample(src, samplerTransform(src, center + p)) * 0.01;\n  }\n  return result;\n}\n"
+ "lightDirection"
+ "lowercaseString"
+ "maxAvailableAllocationSize"
+ "maxComponent"
+ "maximumDistance"
+ "mediap "
+ "messageStringFromDescriptor:"
+ "minOpacity"
+ "newBufferForContextIntermediate:usingHint:identifier:"
+ "newComputePipelineStateWithBinaryFunctions:error:"
+ "newTextureViewWithDescriptor:"
+ "onlyUsesMetal"
+ "opacityBounds"
+ "opaqueEnd"
+ "operator[]"
+ "outputFormatAtIndex:arguments:"
+ "outputURL"
+ "precision highp float;\n"
+ "preferredDynamicRange"
+ "preservesOpacity"
+ "preserves_opacity"
+ "priority_request_media"
+ "processWithInputs:arguments:outputs:error:"
+ "processorOutput %d"
+ "provideImageToMTLTexture:commandBuffer:originx:originy:width:height:userInfo:"
+ "refelectionWithFunctionName:"
+ "reflection"
+ "reflectionForFunctionWithName:"
+ "releaseDeepIntermediate did not release.\n"
+ "removeItemAtPath:error:"
+ "requiredThreadsPerThreadgroup"
+ "roundedData"
+ "roundedMarkers"
+ "roundedQRCodeGeneratorFilter"
+ "sdfScale"
+ "sdfZero"
+ "setBinaryFunctions:"
+ "setCaptureObject:"
+ "setCaptureTraceURL:"
+ "setCenterSpaceSize:"
+ "setDisplayHeadroom:"
+ "setFunction:atIndex:"
+ "setFunctionCount:"
+ "setInputAbove:"
+ "setInputAngleSinCos:"
+ "setInputBelow:"
+ "setInputBiasAmount:"
+ "setInputBorderWidth:"
+ "setInputBounds:"
+ "setInputChannel:"
+ "setInputContourOpacityBounds:"
+ "setInputCurvature:"
+ "setInputDisplayHeadroom:"
+ "setInputFrame:"
+ "setInputHighlightsTradeOffRatio:"
+ "setInputInset:"
+ "setInputLength:"
+ "setInputLightDirection:"
+ "setInputMaskOpposite:"
+ "setInputMaxComponent:"
+ "setInputMaxDistance:"
+ "setInputMinOpacity:"
+ "setInputMinimumGammaAdjustment:"
+ "setInputMinimumSDRExposure:"
+ "setInputOffsetAnchor:"
+ "setInputOpacityBounds:"
+ "setInputOpaqueEnd:"
+ "setInputPreferredDynamicRange:"
+ "setInputSDFScale:"
+ "setInputSDFScaleFactor:"
+ "setInputSDFZero:"
+ "setInputSDFZeroValue:"
+ "setInputSmoothness:"
+ "setInputStopAnchor:"
+ "setLinkedFunctions:"
+ "setMaximumDistance:"
+ "setOutputURL:"
+ "setPreferredDynamicRange:"
+ "setRoundedData:"
+ "setRoundedMarkers:"
+ "setSmoothness:"
+ "setSupportAddingBinaryFunctions:"
+ "setVisibleFunctionTable:atBufferIndex:"
+ "setaveragelightlevel"
+ "setdepthdata"
+ "setheadroom"
+ "signedDistanceGradientFromRedMaskFilter"
+ "slope_adjusted"
+ "smoothness"
+ "smooths"
+ "softlink:o:path:/System/Library/PrivateFrameworks/Futhark.framework/Futhark"
+ "softlink:r:path:/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture"
+ "source_headroom"
+ "sparseTextureTier"
+ "startCaptureWithDescriptor:error:"
+ "stats"
+ "stopCapture"
+ "stringContents"
+ "supportsFunctionPointers"
+ "swizzle_to_abgr10_wide_linear"
+ "swizzle_to_argb10_wide_linear_as_rgba16"
+ "systemToneMapFilter"
+ "target_headroom"
+ "texture2D"
+ "timescale"
+ "totalSize"
+ "uber"
+ "ubershader_archive_bin"
+ "uniform highp %s _samplers [%d];\n"
+ "uniform highp float _u%d;\n"
+ "uniform highp mat2 _u%d;\n"
+ "uniform highp mat3 _t%d;\n"
+ "uniform highp mat3 _transforms [%d];\n"
+ "uniform highp mat3 _u%d;\n"
+ "uniform highp mat4 _u%d;\n"
+ "uniform highp vec2 _u%d;\n"
+ "uniform highp vec3 _u%d;\n"
+ "uniform highp vec4 _extents [%d];\n"
+ "uniform highp vec4 _u%d;\n"
+ "uniform int _u%d;\n"
+ "uniform int2 _u%d;\n"
+ "uniform int3 _u%d;\n"
+ "uniform int4 _u%d;\n"
+ "uniform lowp %s _i%d;\n"
+ "uniform lowp sampler2D _i%d;\n"
+ "unknown error"
+ "unused"
+ "userAnnotation"
+ "uuid"
+ "v112@?0r^v8r^v16r^v24r^v32r^v40i48^^{__IOSurface}52r^^v60Q68r^{CGRect={CGPoint=dd}{CGSize=dd}}76r^B84i92^v96^v104"
+ "v128@?0r^v8r^v16r^v24r^v32r^v40^{__IOSurface=}48^v56Q64{CGRect={CGPoint=dd}{CGSize=dd}}72B104i108^v112^v120"
+ "v128@?0r^v8r^v16r^v24r^v32r^v40^{__IOSurface=}48^v56Q64{CGRect={CGPoint=dd}{CGSize=dd}}72B104i108^v112^{TileTask=}120"
+ "v16@?0r*8"
+ "v24@0:8^{__CVBuffer=}16"
+ "v32@0:8^{__IOSurface=}16@24"
+ "v40@?0i8i12r*16i24i28^v32"
+ "v48@0:8@16^{CMPhotoCompressionSession=}24q32@40"
+ "v48@?0^{__IOSurface=}8Q16Q24Q32Q40"
+ "v52@?0i8^v12{CGRect={CGPoint=dd}{CGSize=dd}}20"
+ "v56@0:8@\"<NSCopying>\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "v56@?0@\"<MTLTexture>\"8@\"<MTLCommandBuffer>\"16Q24Q32Q40Q48"
+ "v56@?0r^{__IOSurface=}8r^v16Q24Q32Q40Q48"
+ "v60@0:8@16^{CMPhotoCompressionSession=}24q32i40@44@52"
+ "v64@?0i8i12i16i20{CGRect={CGPoint=dd}{CGSize=dd}}24^v56"
+ "values0"
+ "values1"
+ "varying highp vec2 p0;\n"
+ "vec2  compare(vec2  x, vec2  y, vec2  z) { return mix(y, z, step(0.0, x)); }\n"
+ "vec2  cos_    (vec2  x) { return cos(x); }\n"
+ "vec2  cossin  (float x) { return vec2(cos(x),sin(x)); }\n"
+ "vec2  cossin_ (float x) { return vec2(cos(x),sin(x)); }\n"
+ "vec2  sin_    (vec2  x) { return sin(x); }\n"
+ "vec2  sincos  (float x) { return vec2(sin(x),cos(x)); }\n"
+ "vec2  sincos_ (float x) { return vec2(sin(x),cos(x)); }\n"
+ "vec2 _cubic_coefs_(vec2 x, vec4 c) {\n  x = abs(x);\n  return (((((c.x * x) * x) * x) + ((c.y * x) * x)) + (c.z * x)) + c.w;\n}\nkernel vec4 _cubicUpsampleX0(sampler src, vec2 scale, vec4 coefsLT1, vec4 coefsLT2) {\n  vec2 dcMappedToSrc = scale * destCoord();\n  vec2 srcCenterBefore = floor(dcMappedToSrc - 0.5) + 0.5;\n  vec2 delta = srcCenterBefore - dcMappedToSrc;\n  vec2 weight0 = _cubic_coefs_(delta - 1.0, coefsLT2);\n  vec2 weight1 = _cubic_coefs_(delta, coefsLT1);\n  vec2 weight3 = _cubic_coefs_(delta + 2.0, coefsLT2);\n  vec2 w1 = weight0 + weight1;\n  vec2 w2 = vec2(1.0) - w1;\n  vec2 o1 = compare(w1 - 1e-4, vec2(0.0), weight1 / w1) + (srcCenterBefore - 1.0);\n  vec2 o2 = compare(w2 - 1e-4, vec2(0.0), weight3 / w2) + (srcCenterBefore + 1.0);\n  vec4 r;\n  r = (w1.x * w1.y) * sample(src, samplerTransform(src, vec2(o1.x, o1.y)));\n  r += (w2.x * w1.y) * sample(src, samplerTransform(src, vec2(o2.x, o1.y)));\n  r += (w1.x * w2.y) * sample(src, samplerTransform(src, vec2(o1.x, o2.y)));\n  r += (w2.x * w2.y) * sample(src, samplerTransform(src, vec2(o2.x, o2.y)));\n  return r;\n}\n"
+ "vec2 _dc_to_uv(vec2 dc, vec4 ext) {\n  return (dc - ext.xy) / ext.zw;\n}\nfloat _uv_distance(vec2 uv1, vec2 uv2, vec4 ext) {\n  vec2 dc1 = (uv1 * ext.zw) + ext.xy;\n  vec2 dc2 = (uv2 * ext.zw) + ext.xy;\n  return distance(dc1, dc2);\n}\nkernel vec4 _signedDistanceMask(sampler image, vec4 ext, float stride) {\n  float minDist = 1.000000e+09;\n  float minDistN = 1.000000e+09;\n  const float nan = 1.0 / 0.0;\n  vec4 result = vec4(nan, nan, nan, nan);\n  vec2 dc = destCoord();\n  vec2 uv = _dc_to_uv(dc, ext);\n  for (int i = -1; i <= 1; i++) {\n    for (int j = -1; j <= 1; j++) {\n      vec2 off = vec2(i, j) * stride;\n      vec4 s = sample(image, samplerTransform(image, dc + off));\n      if (s.r != nan) {\n        float dist = _uv_distance(s.xy, uv, ext);\n        if (dist < minDist) {\n          result.rg = s.rg;\n          minDist = dist;\n        }\n      }\n      if (s.b != nan) {\n        float dist = _uv_distance(s.zw, uv, ext);\n        if (dist < minDistN) {\n          result.ba = s.ba;\n          minDistN = dist;\n        }\n      }\n    }\n  }\n  return result;\n}\n"
+ "vec2 _dc_to_uv(vec2 dc, vec4 ext) {\n  return (dc - ext.xy) / ext.zw;\n}\nkernel vec4 _signedDistanceMaskPrep(vec4 image, vec4 ext) {\n  const float nan = 1.0 / 0.0;\n  vec2 uv = _dc_to_uv(destCoord(), ext);\n  vec2 uvNeg = uv;\n  if (image.r <= 0.5) uv = vec2(nan, nan); else uvNeg = vec2(nan, nan);\n  return vec4(uv, uvNeg);\n}\n"
+ "vec2 _uv_to_dc(vec2 uv, vec4 ext) {\n  return (uv * ext.zw) + ext.xy;\n}\nkernel vec4 _signedDistanceMaskPost(vec4 image, vec4 pre, vec4 ext, float maxDist) {\n  const float nan = 1.0 / 0.0;\n  if ((image.x == nan) || (image.y == nan)) return vec4(1.0, 0.0, 0.0, 1.0);\n  if ((image.z == nan) || (image.w == nan)) return vec4(-1.0, 0.0, 0.0, 1.0);\n  vec2 dc = destCoord();\n  vec2 sc = _uv_to_dc(image.xy, ext);\n  float dist = distance(sc, dc) / maxDist;\n  dist = clamp(dist, 0.0, 1.0);\n  vec2 scNeg = _uv_to_dc(image.zw, ext);\n  float distNeg = distance(scNeg, dc) / maxDist;\n  distNeg = clamp(distNeg, 0.0, 1.0);\n  if (pre.r > 0.5) dist = -distNeg;\n  return vec4(dist, 0.0, 0.0, 1.0);\n}\n"
+ "vec2 destCoord() { return _dc; }\n"
+ "vec2 samplerCoord(sampler s)  { return samplerTransform(s,_dc); }\n"
+ "vec2 samplerOrigin(sampler s) { return _extents[s].xy; }\n"
+ "vec2 samplerSize(sampler s)   { return _extents[s].zw; }\n"
+ "vec2 samplerTransform(sampler s, vec2 p) { return (vec3(p, 1.0) * _transforms[s]).xy; }\n"
+ "vec2 writeCoord() { return p0; }\n"
+ "vec3  compare(vec3  x, vec3  y, vec3  z) { return mix(y, z, step(0.0, x)); }\n"
+ "vec3  cos_    (vec3  x) { return cos(x); }\n"
+ "vec3  sin_    (vec3  x) { return sin(x); }\n"
+ "vec3 _s_pow(vec3 x, vec3 g) {\n  vec3 xx = max(abs(x), 1e-6);\n  return sign(x) * pow(xx, g);\n}\nkernel vec4 _flexMap(vec4 im, vec4 gm, vec3 invGamma, vec3 minv, vec3 maxv, float scale, vec3 kIn, vec3 kOut) {\n  vec3 gainLog2 = ((maxv - minv) * _s_pow(gm.rgb, invGamma)) + minv;\n  vec3 gainLin = exp2(scale * gainLog2);\n  im.rgb = (gainLin * (im.rgb + kIn)) - kOut;\n  return im;\n}\n"
+ "vec3 linear_to_srgb(vec3 s) { return sign(s)*mix(abs(s)*12.92, pow(abs(s), vec3(0.4166667)) * 1.055 - 0.055,   step(0.0031308, abs(s))); }\n"
+ "vec3 srgb_to_linear(vec3 s) { return sign(s)*mix(abs(s)/12.92, pow(abs(s)/1.055 + 0.052132701421801, vec3(2.4)), step(0.04045, abs(s))); }\n"
+ "vec4  compare(vec4  x, vec4  y, vec4  z) { return mix(y, z, step(0.0, x)); }\n"
+ "vec4  cos_    (vec4  x) { return cos(x); }\n"
+ "vec4  sin_    (vec4  x) { return sin(x); }\n"
+ "vec4 _pointillizeStep(sampler src, vec4 background, sampler noise, vec2 cellSize, vec2 noiseOffset, vec2 cellOffset, vec2 dc) {\n  float o;\n  float tSize = 256.0;\n  float _randomFactor = 6.500000e-01;\n  float _radiusFactor = 7.100000e-01;\n  float _colorRandom = 0.1;\n  vec2 noiseLoc = floor((dc * cellSize.y) + 0.5) + noiseOffset;\n  vec4 np = sample(noise, samplerTransform(noise, mod(noiseLoc, tSize)));\n  vec2 cellLoc = (((floor((dc * cellSize.y) - 0.5) + 0.5) * cellSize.x) + 0.5) + cellOffset;\n  cellLoc += ((np.xy - 0.5) * cellSize.x) * _randomFactor;\n  o = distance(dc, cellLoc);\n  o = clamp((1.0 - ((o * cellSize.y) / _radiusFactor)) * 3.0, 0.0, 1.0);\n  o = ((3.0 - (2.0 * o)) * o) * o;\n  vec4 p1 = sample(src, samplerTransform(src, cellLoc));\n  p1.rgb += (vec3(np.b - 0.5) * _colorRandom) * p1.a;\n  return mix(background, p1, o);\n}\nkernel vec4 _pointillize(sampler src, sampler noise, vec4 parms) {\n  vec4 background = sample(src, samplerCoord(src)).aaaa;\n  background = _pointillizeStep(src, background, noise, parms.zw, parms.xy + vec2(0.5, 0.5), vec2(parms.z, parms.z), destCoord());\n  background = _pointillizeStep(src, background, noise, parms.zw, parms.xy + vec2(-0.5, 0.5), vec2(0, parms.z), destCoord());\n  background = _pointillizeStep(src, background, noise, parms.zw, parms.xy + vec2(0.5, -0.5), vec2(parms.z, 0), destCoord());\n  background = _pointillizeStep(src, background, noise, parms.zw, parms.xy + vec2(-0.5, -0.5), vec2(0, 0), destCoord());\n  return background;\n}\n"
+ "vec4 _read_pixel(%s i, vec2 c, mat3 m) { return %s(i, (vec3(c, 1.0) * m).xy); }\n"
+ "vec4 _read_pixel_420(%s Y, %s cc, vec2 c, vec2 f, mat3 m) {\n"
+ "vec4 _unordered_gatherW (sampler s, vec2 p) { return gatherW(s,p); }\n"
+ "vec4 _unordered_gatherX (sampler s, vec2 p) { return gatherX(s,p); }\n"
+ "vec4 _unordered_gatherY (sampler s, vec2 p) { return gatherY(s,p); }\n"
+ "vec4 _unordered_gatherZ (sampler s, vec2 p) { return gatherZ(s,p); }\n"
+ "vec4 gatherW (sampler s, vec2 p) {\n"
+ "vec4 gatherX (sampler s, vec2 p) {\n"
+ "vec4 gatherY (sampler s, vec2 p) {\n"
+ "vec4 gatherZ (sampler s, vec2 p) {\n"
+ "vec4 linear_to_srgb(vec4 s) { s = unpremultiply(s); s.rgb = linear_to_srgb(s.rgb); return premultiply(s); }\n"
+ "vec4 premultiply   (vec4 s) { return vec4(s.rgb*s.a, s.a); }\n"
+ "vec4 sample(sampler s, vec2 p) { return %s(_samplers[s], p)%s; }\n"
+ "vec4 sample(sampler s, vec2 p) { return %s(_samplers[s], p); }\n"
+ "vec4 sample(sampler s, vec2 p) { vec4 s = %s(_samplers[s], p); s = %s; return s; }\n"
+ "vec4 samplerExtent(sampler s) { return _extents[s]; }\n"
+ "vec4 srgb_to_linear(vec4 s) { s = unpremultiply(s); s.rgb = srgb_to_linear(s.rgb); return premultiply(s); }\n"
+ "vec4 unpremultiply (vec4 s) { return vec4(s.rgb/max(s.a,0.00001), s.a); }\n"
+ "void *AVFCaptureLibrary(void)"
+ "void *FutharkLibrary(void)"
+ "void main () {\n"
+ "void writeImage(vec4 c, vec2 p) { gl_FragData[0] = c; }\n"
+ "void writeImagePlane(vec4 c, vec2 p) { gl_FragData[1] = c; }\n"
+ "{?=QQQ}16@0:8"
+ "{MakerApple}.3"
+ "{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}^{CGRect}}44@?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12"
+ "{vector<CI::Perspective::Line, std::allocator<CI::Perspective::Line>>=\"__begin_\"^{?}\"__end_\"^{?}\"__cap_\"^{?}}"
+ "{vector<LineCostProxy, std::allocator<LineCostProxy>>=\"__begin_\"^{LineCostProxy}\"__end_\"^{LineCostProxy}\"__cap_\"^{LineCostProxy}}"
- "\t\t----------------------- facecore count = %d, numHWFaces = %d\n"
- "\t\thasFaces = %d\n"
- "\t\tnotBlurry = %d\n"
- "\t\tpoorRegistration = %d\n"
- "\t\tpotentiallyBlurry = %d\n"
- "\t\tsuspectRegistration = %d\n"
- "\t\tveryBlurry = %d\n"
- "\t******Image %s classified as garbage.\n"
- "\tAction selection score = %f\n"
- "\tAverage Camera Travel Distance = %f\n"
- "\tAverage facial focus score = %f\n"
- "\tAverage registration error skewness = %f\n"
- "\tBeginning vs. End AEMatrix difference vs. Average of Adjacent AE Matrix Differences = %f\n"
- "\tIn-out ratio = %f\n"
- "\tInitial score (no faces) = %f (isGarbage = %d)\n"
- "\tMax Registration Error Integral = %f\n"
- "\tMax inner distance = %f\n"
- "\tMean peak registration error / Max peak registration error = %f\n"
- "\tTravel = %f, maxSkewness = %f, avgSkewness = %f, blur = %f, avgBlur = %f, stdBlur = %f\n"
- "\tscaled Average Camera Travel Distance = %f\n"
- "\tscaled Average registration error skewness = %f\n"
- "\tscaled Beginning vs. End AEMatrix difference vs. Average of Adjacent AE Matrix Differences = %f\n"
- "\tscaled In-out ratio = %f\n"
- "\tscaled Max Registration Error Integral = %f\n"
- "\tscaled Max inner distance = %f\n"
- "\tscaled Mean peak registration error / Max peak registration error = %f\n"
- "\n    preservesAlpha"
- "\n***Finding three way division:\nfirstValidImage = %d, lastValidImage = %d\n"
- "\ncompileTime=%.3fms (waited=%0.3fms%s)"
- " \n// Copyright 2022 Apple, Inc.\n//\n// Standard Library for Core Image Kernels Language.\n//\n// A shell script phase converts this file to the derived source file \"fosl/ci_stdlib.h\"\n//\n\n// For each component, returns x < 0 ? y : z.\nvec4  compare (vec4 x, vec4 y, vec4 z)    { return mix(y, z, step(0.0,x)); }\nvec3  compare (vec3 x, vec3 y, vec3 z)    { return mix(y, z, step(0.0,x)); }\nvec2  compare (vec2 x, vec2 y, vec2 z)    { return mix(y, z, step(0.0,x)); }\nfloat compare (float x, float y, float z) { return x < 0.0 ? y : z; }\n\n// Similar to cos (x) except that x must be in the [–pi, pi] range.\nvec4  cos_ (vec4 x)  { return cos(x); }\nvec3  cos_ (vec3 x)  { return cos(x); }\nvec2  cos_ (vec2 x)  { return cos(x); }\nfloat cos_ (float x) { return cos(x); }\n\n// Similar to sin (x) except that x must be in the [–pi, pi] range.\nvec4  sin_ (vec4 x)  { return sin(x); }\nvec3  sin_ (vec3 x)  { return sin(x); }\nvec2  sin_ (vec2 x)  { return sin(x); }\nfloat sin_ (float x) { return sin(x); }\n\n// Similar to tan (x) except that x must be in the [–pi, pi] range.\nvec4  tan_ (vec4 x)  { return tan(x); }\nvec3  tan_ (vec3 x)  { return tan(x); }\nvec2  tan_ (vec2 x)  { return tan(x); }\nfloat tan_ (float x) { return tan(x); }\n\n// Returns vec2 (cos (x), sin (x)).\nvec2 cossin (float x) { return vec2(cos(x), sin(x)); }\n\n// Returns vec2 (cos_ (x), sin_ (x)).\nvec2 cossin_ (float x) { return vec2(cos_(x), sin_(x)); }\n\n// Returns vec2 (sin (x), cos (x)).\nvec2 sincos (float x) { return vec2(sin(x), cos(x)); }\n\n// Returns vec2 (sin_ (x), cos_ (x)).\nvec2 sincos_ (float x) { return vec2(sin_(x), cos_(x)); }\n\n// Multiplies the red, green, and blue components of the color parameter by its alpha component.\nvec4 premultiply (vec4 s) { return vec4(s.rgb*s.a, s.a); }\nhvec4 premultiply (hvec4 s) { return hvec4(s.rgb*s.a, s.a); }\n\n// If the alpha component of the color parameter is greater than 0, divides the red, green and blue components by alpha. If alpha is 0, this function returns color.\nvec4 unpremultiply (vec4 s) { return vec4(s.rgb/max(s.a,0.00001), s.a); }\nhvec4 unpremultiply (hvec4 s) { return hvec4(s.rgb/max(s.a,0.0001h), s.a); }\n\n// Converts a color from sRGB tone curve to linear.\nvec3 srgb_to_linear (vec3 s)\n{\n    return sign(s)*mix(abs(s)*0.077399380804954, pow(abs(s)*0.947867298578199 + 0.052132701421801, vec3(2.4)), step(0.04045, abs(s)));\n}\n\nhvec3 srgb_to_linear (hvec3 s)\n{\n    return sign(s)*mix(abs(s)*0.077399380804954h, pow(abs(s)*0.947867298578199h + 0.052132701421801h, hvec3(2.4h)), step(0.04045h, abs(s)));\n}\n\n// Converts a premultiplied color from sRGB tone curve to linear.\nvec4 srgb_to_linear (vec4 s)\n{\n    s = unpremultiply(s);\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*0.077399380804954, pow(abs(s.rgb)*0.947867298578199 + 0.052132701421801, vec3(2.4)), step(0.04045, abs(s.rgb)));\n    return premultiply(s);\n}\n\nhvec4 srgb_to_linear (hvec4 s)\n{\n    s = unpremultiply(s);\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*0.077399380804954h, pow(abs(s.rgb)*0.947867298578199h + 0.052132701421801h, hvec3(2.4h)), step(0.04045h, abs(s.rgb)));\n    return premultiply(s);\n}\n\n// for kIntermediateNeedsSRGBConversion support\nvec4 _srgb_to_linear (vec4 s)\n{\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*0.077399380804954, pow(abs(s.rgb)*0.947867298578199 + 0.052132701421801, vec3(2.4)), step(0.04045, abs(s.rgb)));\n    return s;\n}\n\n// Converts a color from linear to sRGB tone curve.\nvec3 linear_to_srgb (vec3 s)\n{\n    return sign(s)*mix(abs(s)*12.92, pow(abs(s), vec3(0.4166667)) * 1.055 - 0.055, step(0.0031308, abs(s)));\n}\n\nhvec3 linear_to_srgb (hvec3 s)\n{\n    return sign(s)*mix(abs(s)*12.92h, pow(abs(s), hvec3(0.4166667h)) * 1.055h - 0.055h, step(0.0031308h, abs(s)));\n}\n\n// Converts a premultiplied color from linear to sRGB tone curve.\nvec4 linear_to_srgb (vec4 s)\n{\n    s = unpremultiply(s);\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*12.92, pow(abs(s.rgb), vec3(0.4166667)) * 1.055 - 0.055, step(0.0031308, abs(s.rgb)));\n    return premultiply(s);\n}\n\nhvec4 linear_to_srgb (hvec4 s)\n{\n    s = unpremultiply(s);\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*12.92h, pow(abs(s.rgb), hvec3(0.4166667h)) * 1.055h - 0.055h, step(0.0031308h, abs(s.rgb)));\n    return premultiply(s);\n}\n\n// for kIntermediateNeedsSRGBConversion support\nvec4 _linear_to_srgb (vec4 s)\n{\n    s.rgb = sign(s.rgb)*mix(abs(s.rgb)*12.92, pow(abs(s.rgb), vec3(0.4166667)) * 1.055 - 0.055, step(0.0031308, abs(s.rgb)));\n    return s;\n}\n\n// Returns the position, in working space coordinates, of the pixel currently being computed.\n// The destination space refers to the coordinate space of the image you are rendering.\nvec2 destCoord ()\n{\n    return _dc;\n}\n\n// Simulate a GLSL 4.00+ textureGather call\n// xyzw in counter clockwise order, starting with the sample to the lower left of the queried location\n\n#define _samplerOffset(src, offset) (samplerTransform(src,offset) - samplerTransform(src,vec2(0.0)))\n\n//TODO: Need to snap 'point' to nearest 2x2 pixel grid center, since samplers may not be using nearest filtering.\n\nvec4 gatherX (sampler src, vec2 point)\n{\n    vec4 r = vec4(\n        sample(src, point+_samplerOffset(src,vec2(-0.5,-0.5))).x,\n        sample(src, point+_samplerOffset(src,vec2( 0.5,-0.5))).x,\n        sample(src, point+_samplerOffset(src,vec2( 0.5, 0.5))).x,\n        sample(src, point+_samplerOffset(src,vec2(-0.5, 0.5))).x);\n    return r;\n}\n\nvec4 gatherY (sampler src, vec2 point)\n{\n    vec4 r = vec4(\n        sample(src, point+_samplerOffset(src,vec2(-0.5,-0.5))).y,\n        sample(src, point+_samplerOffset(src,vec2( 0.5,-0.5))).y,\n        sample(src, point+_samplerOffset(src,vec2( 0.5, 0.5))).y,\n        sample(src, point+_samplerOffset(src,vec2(-0.5, 0.5))).y);\n    return r;\n}\n\nvec4 gatherZ (sampler src, vec2 point)\n{\n    vec4 r = vec4(\n        sample(src, point+_samplerOffset(src,vec2(-0.5,-0.5))).z,\n        sample(src, point+_samplerOffset(src,vec2( 0.5,-0.5))).z,\n        sample(src, point+_samplerOffset(src,vec2( 0.5, 0.5))).z,\n        sample(src, point+_samplerOffset(src,vec2(-0.5, 0.5))).z);\n    return r;\n}\n\nvec4 gatherW (sampler src, vec2 point)\n{\n    vec4 r = vec4(\n        sample(src, point+_samplerOffset(src,vec2(-0.5,-0.5))).w,\n        sample(src, point+_samplerOffset(src,vec2( 0.5,-0.5))).w,\n        sample(src, point+_samplerOffset(src,vec2( 0.5, 0.5))).w,\n        sample(src, point+_samplerOffset(src,vec2(-0.5, 0.5))).w);\n    return r;\n}\n\n// Equivalent to gather{X|Y|Z|W}\n#define _unordered_gatherX(src, point) gatherX(src, point)\n#define _unordered_gatherY(src, point) gatherY(src, point)\n#define _unordered_gatherZ(src, point) gatherZ(src, point)\n#define _unordered_gatherW(src, point) gatherW(src, point)\n\n// Equivalent to samplerExtent (src).xy.\n#define samplerOrigin(src) samplerExtent(src).xy\n\n// Equivalent to samplerExtent (src).zw.\n#define samplerSize(src) samplerExtent(src).zw\n\n// Stubs for compute kernels compiled with Fosl (to be replaced with context-dependent implementations, post-Fosl codegen)\nvoid writeImage (vec4 color, vec2 point) {}\nint writeImageWidth() { return 0; }\nint writeImageHeight() { return 0; }\nvoid writeImagePlane (vec4 color, vec2 point) {}\nvoid writePixel (int r, int g, int b, int a, vec2 point) {}\nvec2 writeCoord () { return vec2(0.0); }\n\n// Rename some (C++) reserved keywords to avoid conflict with Metal shading language\n#define new _new\n#define delete _delete\n#define and _and\n#define not _not\n#define or _or\n#define xor _xor\n "
- "       entry exists with same id: %d\n"
- "      found face id %d, timestamp=%.6f, x=%.3f,y=%.3f,w=%.3f,h=%.3f\n"
- "      no match found for id %d - adding face\n"
- "    %d overlaps with %d by %.3f %% : "
- "    adding face id %d, timestamp %.6f\n"
- "    face %d\n"
- "    face id %d, timestamp %.6f - delta = %.6f, perhaps should use FaceCore\n"
- "    face id=%d, rect=%.3f,%.3f,%.3f,%.3f, focus=%.3f, faceScore=%.3f, leftEyeOpen=%d, rightEyeOpen=%d\n"
- "    imageTimestamp > latestFaceTimestamp\n"
- "    inserting at index %d, count=%d\n"
- "    latestFaceTimestamp = %.6f\n"
- "    map found: %d maps to %d\n"
- "    matched!  mapping %d to %d\n"
- "    new id: %d mapped to %d\n"
- "    no id: assigning %d\n"
- "    not matched\n"
- "    orientation = %d\n"
- "    rename found: %d mapped to %d\n"
- "   adding rect: %.3f,%.3f,%.3f,%.3f\n"
- "   face %d = (%.3f,%.3f,%.3f,%.3f)\n"
- "   fcrect  = (%.3f,%.3f,%.3f,%.3f)\n"
- "   focusScore = %d, %.3f\n"
- "   hwFaceRect: (%.3f,%.3f,%.3f,%.3f), hasLeftEye = %d, hasRightEye = %d\n"
- "   initWithBurstImageSet - Error: stats not found"
- "   inserting prev face (hw%d,sw=%d) = (%.3f,%.3f,%.3f,%.3f) padding=(%.3f,%.3f)\n"
- "   mapping not found for %d, mapping to itself\n"
- "  #faces = %d\n"
- "  accumulatedFaceMetadata = %x\n"
- "  extractFacesFromMetadata\n"
- "  face ID = %d, timestamp = %.6f\n"
- "  needFaceCore = %d\n"
- "  num regions = %d\n"
- "  prevConfig has %d entries\n"
- "!!! you should not read this !!!"
- "#define _ci_simd_shuffle_down(c, p, _dc) simd_shuffle_down(c, p)\n"
- "#define _ci_simdgroup_barrier(f) simdgroup_barrier(mem_flags::mem_threadgroup)\n"
- "#define writeImageHeight(_dc) (int)_outputTexture.get_height()\n"
- "#define writeImageWidth(_dc) (int)_outputTexture.get_width()\n"
- "#define writePixel(r, g, b, a, p) \n"
- "#define writePixel(r, g, b, a, p, _dc) _outputTexture.write(float4(r,g,b,a) / 255.0, static_cast<uint2>(p))\n"
- "#define writePixel(r, g, b, a, p, _dc) write_imagei(_outputTexture, (int2)p, (int4)(r,g,b,a))\n"
- "%@ -> Can't find %@ "
- "%@/%@.metallib"
- "%@/%@_bin.metallib"
- "%@_bin"
- "%d faces so far unmatched:\n"
- "%s REGISTERED AGAINST %s\n"
- "%s/ci_%016llX.metallib"
- "%s/ci_%016llX_%@.txt"
- "%s:   # faces = %d, avgH = %f\n"
- "%{public}@: requires an inputImage with a finite extent."
- "%{public}s Failed loading %{public}@ AIR and binary archive"
- "%{public}s Failed loading %{public}@ AIR and binary archive from %{public}@"
- "%{public}s Failed loading %{public}@ binary archive from %{public}@, Only AIR loaded"
- "%{public}s Failed loading %{public}@ binary archive, Only AIR loaded"
- "%{public}s Failed to create device for using with %{public}@"
- "%{public}s Loaded %{public}@ CoreImage AIR and binary archive"
- "%{public}s Loaded %{public}@ CoreImage AIR and binary archive from url %{public}@"
- "%{public}s Loaded %{public}@ CoreImage stitched libraries binary archive"
- "%{public}s Loaded %{public}@ CoreImage stitched libraries binary archive from url %{public}@"
- "%{public}s Loading %@ from PortraitFilters bundle at: %@"
- "%{public}s No %{public}@ AIR or binary archive found"
- "%{public}s No %{public}@ AIR or binary archive found in %{public}@"
- "%{public}s Rendering a region that has odd width (%d) may impact performance"
- "%{public}s Rendering a region that has odd width (%d) or height (%d) may impact performance"
- "%{public}s failed to add alpha channel to the image to the PhotoCompressionSession."
- "%{public}s failed to add image to the PhotoCompressionSession."
- "%{public}s failed to close the PhotoCompressionSession."
- "%{public}s failed to open the PhotoCompressionSession."
- "%{public}s kernel '%{public}s' specified 'preservesAlpha' but extent is not the same as the extent of the first input image."
- "%{public}s kernel '%{public}s' specified 'preservesAlpha' but has no inputs."
- "%{public}s surface is nil."
- "**** Image %s classified as garbage by association.\n"
- "*16@0:8"
- "*_*_* GARBAGE DETECTOR FOR %s *_*_*\n"
- "+[CIContext loadArchive:]"
- "+[CIContext loadArchiveWithName:fromURL:]"
- "----------REGISTRATION ERROR INTEGRAL \t\t= \t\t\t%f\n"
- "--Invalidating one outlier from the end of the burst\n"
- "--Invalidating one outlier from the start of the burst\n"
- "--Invalidating two outliers from the end of the burst\n"
- "--Invalidating two outliers from the start of the burst\n"
- "-[CIContext(ImageRepresentation) HEIF10RepresentationOfImage:colorSpace:options:error:]"
- "-[CIImage _imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:]"
- "-[CIImage(CIImageProvider) _initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:]"
- "-[CIImageProcessorInOut initWithSurface:texture:digest:allowSRGB:bounds:context:]"
- "-[CIImageProcessorOutput initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:]"
- "-w -D__CIKERNEL_METAL_VERSION__=300 -D_BUILDING_CORE_IMAGE_LIB_ -D__BUILDING_RUNTIME_COMPILE_HEADER__"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedCoreImage/Framework/api/Burst/Projections/FastRegistration_Core.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedCoreImage/Framework/api/Burst/Projections/Projections_Core.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedCoreImage/Framework/api/Burst/Projections/Projections_Optimizer.c"
- "/Library/Caches/com.apple.xbs/Sources/EmbeddedCoreImage/Framework/internal/render.cpp"
- "/System/Library/PrivateFrameworks/Futhark.framework"
- "/var/mobile/Library/Caches/com.apple.camera"
- "0x%016llX %s\n"
- "1.021 - Aug 1, 2013"
- "4"
- "<tr><td valign='middle' balign='left'><font face='Menlo'>%s</font></td></tr>"
- "<tr><td valign='middle'><font face='Menlo'>[%s]</font></td></tr>"
- "@\"CIBurstActionClassifier\""
- "@\"CIBurstImageFaceAnalysisContext\""
- "@\"CIBurstImageSetInternal\""
- "@\"CIBurstYUVImage\""
- "@\"FCRFaceDetector\""
- "@\"NSCountedSet\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@100@0:8^{__IOSurface=}16{Texture=(?=Q{?=II}{?=^v^v})}24Q40B48{CGRect={CGPoint=dd}{CGSize=dd}}52^v84^v92"
- "@108@0:8^{__IOSurface=}16{Texture=(?=Q{?=II}{?=^v^v})}24Q40B48{CGRect={CGPoint=dd}{CGSize=dd}}52Q84Q92^v100"
- "@136@0:8{CIKernelReflection=ii***{vector<CI::KernelArgumentType, std::allocator<CI::KernelArgumentType>>=^i^i{__compressed_pair<CI::KernelArgumentType *, std::allocator<CI::KernelArgumentType>>=^i}}{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}@IiQQBB}16"
- "@152@0:8{CIKernelReflection=ii***{vector<CI::KernelArgumentType, std::allocator<CI::KernelArgumentType>>=^i^i{__compressed_pair<CI::KernelArgumentType *, std::allocator<CI::KernelArgumentType>>=^i}}{vector<std::string, std::allocator<std::string>>=^v^v{__compressed_pair<std::string *, std::allocator<std::string>>=^v}}@IiQQBB}16@136@144"
- "@28@0:8^{CGColorSpace=}16f24"
- "@28@0:8^{CGImage=}16i24"
- "@28@0:8^{__IOSurface=}16i24"
- "@36@0:8@16@24i32"
- "@56@0:8@16@24@32@40@?48"
- "@64@0:8@?16Q24Q32i40^{CGColorSpace=}44B52@56"
- "@92@0:8^{__IOSurface=}16{Texture=(?=Q{?=II}{?=^v^v})}24Q40B48{CGRect={CGPoint=dd}{CGSize=dd}}52^v84"
- "@?16@0:8"
- "ACTION"
- "ACTION SELECTION THRESHOLD = %f\n"
- "AEAverage"
- "AEDelta"
- "AEStable"
- "AETarget"
- "AFStable"
- "Action mean = %f, action std = %f, action threshold = %f\n"
- "Action statistics for cluster %d: mean %f std %f threshold %f\n"
- "Adding ACTION DIVIDER at location %d\n"
- "Adding action-based cluster boundaries.\n"
- "Adding image: %s\n"
- "AdjustFaceIds: Examining '%s'\n"
- "After collapse avgHorzDiffY = %f, blurExtent = %f\n"
- "All images are garbage. Picking the middle selection = %s.\n"
- "All items in one cluster.\n"
- "An archive loaded with these functions %{public}@"
- "Analyzing %s...\n"
- "BURST ANALYSIS VERSION = %s (%s)\n"
- "Between %d and %d: \t%f \t%f \t\tmotion: %f\n"
- "BlinkFeaturesSize"
- "BurstDoc_AllImageIdentifiers"
- "BurstDoc_AllImageStats"
- "BurstDoc_BestImageIds"
- "BurstDoc_LogFile"
- "BurstSet_CoverImage"
- "BurstSet_IsAction"
- "BurstSet_IsPortrait"
- "BurstSet_Setting_DisableAnalysis"
- "BurstSet_Setting_DisableFaceCore"
- "BurstSet_Setting_DummyAnalysisCount"
- "BurstSet_Setting_EnableDumpYUV"
- "BurstSet_Setting_ForceFaceDetection"
- "BurstSet_Setting_MaxNumPendingFrames"
- "BurstSet_TimeDone"
- "BurstSet_TimeDoneCapturing"
- "CCPortrait.bundle/CoreImageKernels.ci.metallib"
- "CCPortrait.bundle/CoreImageKernels_only.ci.metallib"
- "CI library serialized to : %{public}@ for %{public}s"
- "CIAreaHistogram area width or height is greater than 32768."
- "CIAreaHistogram outputData requires inputCount >= 1 and <= 256"
- "CIAreaHistogram requires inputCount >= 1 and <= 2048"
- "CIBurstActionClassifier"
- "CIBurstClusterDivider"
- "CIBurstFaceAnalysis.m"
- "CIBurstFaceConfigEntry"
- "CIBurstFaceInfo"
- "CIBurstFaceScoreEntry"
- "CIBurstFaceStat"
- "CIBurstImageFaceAnalysisContext"
- "CIBurstImageSetInternal"
- "CIBurstImageStat"
- "CIBurstThumbnailCluster"
- "CIBurstYUVImage"
- "CICoreML.h"
- "CIDetectorLowLevel.mm"
- "CILoadAIRArchive"
- "CIMetalUtils.m"
- "CIPersonSegmentationFilter"
- "CIPersonSegmentationKernel"
- "CISaliencyMapKernel"
- "CIVision.h"
- "CI_DEBUG_CONTEXT_COLOR"
- "CI_LOG_AIR_ARCHIVE_ACTIVITY"
- "CI_LOG_AIR_ARCHIVE_MISS"
- "CI_USE_ARCHIVED_KERNELS"
- "Cbuffer"
- "Checking temporal order: %d vs. %d\n"
- "Choosing candidate %d from a series of dupes\n"
- "Class getFaceCoreDetectorClass(void)_block_invoke"
- "Class getFaceCoreFaceClass(void)_block_invoke"
- "Class getFaceCoreImageClass(void)_block_invoke"
- "Class getVNGenerateAttentionBasedSaliencyImageRequestClass()_block_invoke"
- "Class getVNGeneratePersonSegmentationRequestClass(void)_block_invoke"
- "Classified as action.\n"
- "Classified as non-action.\n"
- "Classified as portrait mode. Affects cover photo selection.\n"
- "Cluster %d is too small for action-based cluster boundaries\n"
- "Clustering costs: maxInner = %f, inOutRatio = %f\n"
- "Collapsing %s\n"
- "Column interval: (%d->%d)\n"
- "Computing action selection threshold"
- "Computing sharpness over grid points (%d,%d)->(%d,%d)\n"
- "ControlStrip"
- "CoreImage needs a %{public}s swizzler so that %{public}s can be written as %{public}s.\n"
- "Could not convert from a format supported by the context to the processors input format (%{public}s)."
- "Could not convert from processors output format (%{public}s) to a format supported by the context."
- "Couldn't get the output pixelBuffer from Vision request result"
- "Couldn't get the outputBuffer from saliency map"
- "Couldn't get the pixel buffer from input image"
- "Cover photo ACTION selection score for %d:%s = %f\n"
- "Cover photo PORTRAIT selection score for %d:%s = %f (unbiased = %f)\n"
- "Distance between selections %d and %d: %f, %f\n"
- "Divider1 = %d, Divider2 = %d\n"
- "Done with all functions"
- "Error with VTPixelTransferSessionTransferImage:%d\n"
- "Error!  Done adding, but there are still frames left!\n"
- "Examining image, id=%s, timestamp = %.6f, done=%d\n"
- "Expanding main peak to include divider %d\n"
- "FCRBlinkFeaturesSize"
- "FCRDetectionParamDetectionRegion"
- "FCRDetectionParamInitialAngle"
- "FCRExtractionParamEnhancedEyesAndMouthLocalization"
- "FCRExtractionParamExtractBlink"
- "FCRExtractionParamExtractFaceprint"
- "FCRExtractionParamExtractLandmarkPoints"
- "FCRExtractionParamExtractSmile"
- "FCRExtractionParamInitialAngle"
- "FCRFaceExpressionLeftEyeClosed"
- "FCRFaceExpressionLeftEyeClosedScore"
- "FCRFaceExpressionRightEyeClosed"
- "FCRFaceExpressionRightEyeClosedScore"
- "FCRFaceExpressionSmile"
- "FCRFaceExpressionSmileScore"
- "FCRFastFaceDetectionParameters"
- "FCRLeftEyeFeaturesOffset"
- "FCRRightEyeFeaturesOffset"
- "FCRSetupParamLoadModelFiles"
- "FCRSetupParamNumberOfAngles"
- "FCRSmileAndBlinkFeatures"
- "FCRSmileFeaturesOffset"
- "FCRSmileFeaturesSize"
- "Face detection error\n"
- "FaceCoreDetector"
- "FaceCoreFace"
- "FaceCoreImage"
- "FaceID"
- "FaceInfoArray:\n"
- "Failed to create %@ MTLFunction"
- "Failed to find function %{public}@ for %{public}s in any air archive"
- "Failed to find function %{public}@ in any air archive"
- "Failed to load %@.metallib for prewarming"
- "Failed writing descriptor fot %{public}s: %d - message: %{public}s"
- "FastRegistration error %d:%s in %s @ %s:%d\n"
- "FastRegistration_status FastRegistration_computeSignatures(const vImage_Buffer *, _Bool, dispatch_queue_t, FastRegistration_Signatures *)"
- "FastRegistration_status FastRegistration_processProjections(float *, vImagePixelCount)"
- "FastRegistration_status FastRegistration_register(const FastRegistration_Signatures *, const FastRegistration_Signatures *, float, dispatch_queue_t, float *, float *, float *, float *)"
- "First average cost = %f\n"
- "Found function %{public}@ for %{public}s in the archive %d/%zu"
- "Found mapping!\n"
- "Image %d:%s has been emotionally rejected.\n"
- "Image %d:%s has emotional score %d\n"
- "Image %s is classified as garbage for portrait mode, no sharp faces.\n"
- "Image Processor"
- "Image_AEAverage"
- "Image_AEMatrix"
- "Image_AEStable"
- "Image_AETarget"
- "Image_AFStable"
- "Image_FaceRectROI"
- "Image_ImageROIGridEndX"
- "Image_ImageROIGridEndY"
- "Image_ImageROIGridStartX"
- "Image_ImageROIGridStartY"
- "Images without faces = %d, threshold = %d, total # = %d\n"
- "Insufficient peak error for ROI computation %f (threshold %f)\n"
- "Items in next cluster:\n"
- "JpegData"
- "JpegDataSize"
- "Keeping candidate %d\n"
- "Keeping face with ID = %d\n"
- "LOOKING FOR FALSE-POSITIVE FACES...\n"
- "Last average cost = %f\n"
- "LeftEyeBlinkLevel"
- "LeftEyeFeaturesOffset"
- "LeftEyeHeight"
- "LeftEyeWidth"
- "LeftEyeX"
- "LeftEyeY"
- "Library serialization failed : %{public}@ "
- "Limited ROI = (%d,%d)->(%d,%d)\n"
- "Limited sharpness score = %f, with number of faces = %d\n"
- "Local statistics for divider %03d\t with score %f:\t\t noise threshold = %f, high threshold = %f (mean %f, std %f)\n"
- "Locally-maximal divider %d not considered due to being potential noise (%f vs %f,%f)\n"
- "Locally-maximal divider %d not considered due to being potential noise (nearby peak).\n"
- "Locally-maximal divider %d not considered due to lack of any motion: %f\n"
- "Mean non-zero actions = %f, std dev = %f\n"
- "NEW BEST\n"
- "NEW BEST: largestInnerDistance = %f, bestRatio = %f\n"
- "NON-ACTION"
- "NSDictionary *ciFCRFastFaceDetectionParameters(void)"
- "NSString *getFCRDetectionParamDetectionRegion(void)"
- "NSString *getFCRDetectionParamInitialAngle(void)"
- "NSString *getFCRExtractionParamEnhancedEyesAndMouthLocalization(void)"
- "NSString *getFCRExtractionParamExtractBlink(void)"
- "NSString *getFCRExtractionParamExtractFaceprint(void)"
- "NSString *getFCRExtractionParamExtractLandmarkPoints(void)"
- "NSString *getFCRExtractionParamExtractSmile(void)"
- "NSString *getFCRExtractionParamInitialAngle(void)"
- "NSString *getFCRFaceExpressionLeftEyeClosed(void)"
- "NSString *getFCRFaceExpressionLeftEyeClosedScore(void)"
- "NSString *getFCRFaceExpressionRightEyeClosed(void)"
- "NSString *getFCRFaceExpressionRightEyeClosedScore(void)"
- "NSString *getFCRFaceExpressionSmile(void)"
- "NSString *getFCRFaceExpressionSmileScore(void)"
- "NSString *getFCRSetupParamNumberOfAngles(void)"
- "Non-Linear SVM Action classifier called with:\n"
- "Not processing frames, imageStat.timestamp = %.6f, latestFaceTimestamp = %.6f\n"
- "Num HW faces = %d, facecore faces = %d\n"
- "Number of HW faces = %d - calculating rect\n"
- "Number of images too few after invalidation at the endpoints. Return one selection.\n"
- "Original ROI = %d,%d -> %d,%d\t\t"
- "Overall mean divider score = %f\n"
- "PREDICTION: --- %s --- (value = %f)\n"
- "Peak rejection threshold = %f (mean = %f, std = %f)\n"
- "Performing emotional rejection of face images in cluster %d:\n"
- "Projections error %d:%s in %s @ %s:%d\n"
- "Projections_status Projections_computeCost(int, float, float, const float *, int, const Projections_meanStdTable *, const float *, int, const Projections_meanStdTable *, int, float *)"
- "Projections_status Projections_computeProjectionDerivative(const float *, int, float *)"
- "Projections_status Projections_computeShiftBruteForce(const float *, int, const Projections_meanStdTable *, const float *, int, const Projections_meanStdTable *, int, float, float *, float *, float *, float *)"
- "Projections_status Projections_projectionRowsCols_planar8UtoF(const uint8_t *, int, int, size_t, float *, float *)"
- "RECURSING: (%d->%d) becomes (%d->%d)\n"
- "REMOVING false-positive face with ID = %d\n"
- "Re-running three-way division with minClusterSize = %d, maxClusterSize = %d\n"
- "Rect"
- "RegionList"
- "Registration error stats: mean=%f, stdDev=%f, skewness=%f, maxValue=%f\n"
- "Registration in favor of face detection ROI.\n"
- "Registration rejected due to ROI too large or too small.\n"
- "Registration rejected due to insufficient local motion.\n"
- "Registration rejected due to skewness, which can indicate a bad registration result.\n"
- "Registration result: tx = %d, ty = %d\n"
- "Removing %d:%s\n"
- "Result of three-way division: finalCost: %f, inOutRatio: %f\n"
- "RightEyeBlinkLevel"
- "RightEyeFeaturesOffset"
- "RightEyeHeight"
- "RightEyeWidth"
- "RightEyeX"
- "RightEyeY"
- "RollAngle"
- "Row interval: (%d->%d)\n"
- "Score for %s:%d is %f \t\twith action score %f and center bias %f (isGarbage=%d)\n"
- "Second average cost = %f\n"
- "Second-to-last average cost = %f\n"
- "Selection score of %d is %f... isGarbage = %d\n"
- "Sequence classified as NON-ACTION due to complete lack of local motion (%f, threshold %f)\n"
- "Sharpness ROI for %s updated to (%d,%d)->(%d,%d)\n"
- "Skipping projection computation because data isn't present\n"
- "Skipping render due to error in computation of destination ROI"
- "SmileFeaturesOffset"
- "SmileFeaturesSize"
- "SmileLevel"
- "Smoothed ROI = %d,%d -> %d,%d\n"
- "Starting ROI construction at %d->%d\n"
- "Strongest local maxima: %d and %d\n"
- "T*,VCbuffer"
- "T*,VYbuffer"
- "T@\"CIBurstActionClassifier\",VactionClassifier"
- "T@\"CIBurstYUVImage\",Vimage"
- "T@\"NSArray\",VbestImageIdentifiersArray"
- "T@\"NSCountedSet\",VfaceIDCounts"
- "T@\"NSMutableArray\",VFCRSmileAndBlinkFeatures"
- "T@\"NSMutableArray\",VallImageIdentifiers"
- "T@\"NSMutableArray\",VburstImages"
- "T@\"NSMutableArray\",VclusterArray"
- "T@\"NSMutableArray\",VfaceStatArray"
- "T@\"NSMutableDictionary\",VclusterByImageIdentifier"
- "T@\"NSMutableDictionary\",VimageProps"
- "T@\"NSMutableDictionary\",VstatsByImageIdentifier"
- "T@\"NSNumber\",&,N,VinputQualityLevel"
- "T@\"NSString\",&,N,VburstId"
- "T@\"NSString\",V_versionString"
- "T@\"NSString\",VburstCoverSelection"
- "T@\"NSString\",VburstLogFileName"
- "T@\"NSString\",VimageId"
- "T@?,VcompletionBlock"
- "TB,VAEStable"
- "TB,VAFStable"
- "TB,V_isSyncedWithImage"
- "TB,VdoLimitedSharpnessAndBlur"
- "TB,VemotionallyRejected"
- "TB,VenableAnalysis"
- "TB,VenableDumpYUV"
- "TB,VenableFaceCore"
- "TB,Vexclude"
- "TB,VforceFaceDetectionEnable"
- "TB,VfoundByFaceCore"
- "TB,VhasLeftEye"
- "TB,VhasRegistrationData"
- "TB,VhasRightEye"
- "TB,VhasRollAngle"
- "TB,VhasYawAngle"
- "TB,VisGarbage"
- "TB,VleftEyeOpen"
- "TB,VrightEyeOpen"
- "TB,VsmallFace"
- "TB,Vsmiling"
- "T^{__IOSurface=},V_fullsizeJpegData"
- "T^{__SVMParameters=[7{__SVMScaleOffset=ff}]ddii^{CIBurstSupportVector}^{CIBurstSupportVector}},V_svmParameters"
- "Td,VlatestFaceTimestamp"
- "Td,VtimeBlinkDetectionDone"
- "Td,VtimeFaceDetectionDone"
- "Td,VtimeReceived"
- "Td,Vtimestamp"
- "Tf,VactionAmount"
- "Tf,VactionClusteringScore"
- "Tf,VactionScore"
- "Tf,VavgHorzDiffY"
- "Tf,VblurExtent"
- "Tf,VdividerScore"
- "Tf,VfaceScore"
- "Tf,VfocusScore"
- "Tf,VhighNoiseThreshold"
- "Tf,VimageScore"
- "Tf,VleftEyeBlinkScore"
- "Tf,VmaxScore"
- "Tf,VmaxSkewness"
- "Tf,VminScore"
- "Tf,VnoiseThreshold"
- "Tf,VnormalizedFocusScore"
- "Tf,VnormalizedSigma"
- "Tf,VregistrationErrorIntegral"
- "Tf,VregistrationErrorX"
- "Tf,VregistrationErrorY"
- "Tf,VrightEyeBlinkScore"
- "Tf,VroiSize"
- "Tf,VrollAngle"
- "Tf,VsmileScore"
- "Tf,VtestAverageCameraTravelDistance"
- "Tf,VtestAverageRegistrationErrorSkewness"
- "Tf,VtestBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix"
- "Tf,VtestInOutRatio"
- "Tf,VtestMaxInnerDistance"
- "Tf,VtestMaxPeakRegistrationError"
- "Tf,VtestMaxRegistrationErrorIntegral"
- "Tf,VtestMaxRegistrationErrorSkewness"
- "Tf,VtestMeanPeakRegistrationError"
- "Tf,VtestMinRegionOfInterestSize"
- "Tf,Vtx"
- "Tf,Vty"
- "Tf,VyawAngle"
- "The output pixelBuffer from Vision is not the expected format."
- "The output pixelBuffer from Vision is not the expected height."
- "The output pixelBuffer from Vision is not the expected width."
- "Threshold for dupes: %f\n"
- "Throwing away all dupes due to garbage classification\n"
- "Thumbnail selection score computation for %s\n"
- "ThumbnailCluster - adding %s\n"
- "Ti,VAEAverage"
- "Ti,VAETarget"
- "Ti,VFCRBlinkFeaturesSize"
- "Ti,VFCRLeftEyeFeaturesOffset"
- "Ti,VFCRRightEyeFeaturesOffset"
- "Ti,VFCRSmileFeaturesOffset"
- "Ti,VFCRSmileFeaturesSize"
- "Ti,V_AEDelta"
- "Ti,V_fullsizeJpegSize"
- "Ti,V_version"
- "Ti,VbytesPerRow"
- "Ti,VdummyAnalysisCount"
- "Ti,VfaceId"
- "Ti,VframesSinceLast"
- "Ti,Vheight"
- "Ti,VhwFaceId"
- "Ti,VhwLastFrameSeen"
- "Ti,VleftImage"
- "Ti,VmaxNumPendingFrames"
- "Ti,VnumHWFaces"
- "Ti,VnumScores"
- "Ti,Vorientation"
- "Ti,VswFaceId"
- "Ti,VswLastFrameSeen"
- "Ti,VtemporalOrder"
- "Ti,VtrueLocalMaximum"
- "Ti,Vwidth"
- "Timestamp"
- "Tossing out the %s on %d\n"
- "Trying %@"
- "T{CGPoint=dd},VhwCenter"
- "T{CGPoint=dd},VswCenter"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},V_hwFaceRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},VfaceRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},VfacesRoiRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},VleftEyeRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},VnormalizedFaceRect"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},VrightEyeRect"
- "T{CGSize=dd},VhwSize"
- "T{CGSize=dd},VswSize"
- "Unable to load Quagga.framework\n"
- "UserNotificationCenter"
- "VNGenerateAttentionBasedSaliencyImageRequest"
- "VNGeneratePersonSegmentationRequest"
- "WARNING: CoreImage intrenal function name %{public}s must start with '_'\n"
- "YawAngle"
- "Ybuffer"
- "[1024f]"
- "[256S]"
- "[7d]"
- "[CIBurstThumbnailCluster initWithImageData] : metadata parsing error\n"
- "[CIBurstThumbnailCluster initWithImageData] : no error\n"
- "^S16@0:8"
- "^v32@0:8^v16^v24"
- "^{SharpnessGridElement_t=CCf}"
- "^{__SVMParameters=[7{__SVMScaleOffset=ff}]ddii^{CIBurstSupportVector}^{CIBurstSupportVector}}"
- "^{__SVMParameters=[7{__SVMScaleOffset=ff}]ddii^{CIBurstSupportVector}^{CIBurstSupportVector}}16@0:8"
- "_AEDelta"
- "_Bool soft_horizonDetectionFFT(uint8_t *, int, int, int, float *, int)"
- "_CPUShadow"
- "_ci_simd_shuffle_down"
- "_ci_simdgroup_barrier"
- "_ci_writeTG_42X"
- "_ci_writeTG_42X_tgcc"
- "_fullsizeJpegData"
- "_fullsizeJpegSize"
- "_hwFaceRect"
- "_imageByToneMappingColorSpaceToWorkingSpace:targetHeadroom:"
- "_initWithImageProvider:width:height:format:colorSpace:surfaceCache:options:"
- "_isSyncedWithImage"
- "_svmParameters"
- "_version"
- "_versionString"
- "actionAmount"
- "actionClassifier"
- "actionClusteringScore"
- "actionScore"
- "addFaceToArray:"
- "addFacesToImageStat: timestamp = %.6f, lastFaceIndex=%d\n"
- "addFacesToImageStat:imageSize:"
- "addItemsFromCluster:"
- "addScore:"
- "addYUVImage:properties:identifier:imageProps:completionBlock:"
- "adding %d faces\n"
- "adjustFaceIdsForImageStat:"
- "aeMatrix"
- "air"
- "all costs within valid region: \t\tmean = %f, std = %f\n"
- "allObjects"
- "allocSpanStack:s"
- "allocSpanStack:s->firstChunk"
- "allocateMeanStdPingPongBuffers::::"
- "assignMeanStdBuffers:"
- "avgHorzDiffY"
- "bestImageIdentifiersArray"
- "bezier"
- "blurBitmapHorizontal:scan"
- "blurBitmapVertical:scan"
- "blurExtent"
- "burstCoverSelection"
- "burstDocumentDirectory"
- "burstImages"
- "burstLogFileHandle"
- "burstLogFileName"
- "burstSets"
- "burst_disable_analysis"
- "burst_disable_facecore"
- "burst_dummy_analysis"
- "burst_dump_yuv"
- "burst_fixed_image_filename"
- "burst_force_face_detection"
- "burst_max_pending_frames"
- "burst_mode_logging"
- "burst_use_fixed_image"
- "burst_use_version"
- "burstimage_%06d.yuv"
- "calcFaceScores:"
- "calculateFaceCoreROI:imageStat:needFaceCore:"
- "calculateFaceFocus:\n"
- "calculateFaceFocusInImage:imageStat:"
- "canRegister"
- "child is a Noop full_intermediate"
- "child is a Noop intermediate_cached"
- "ci_%016llX"
- "cikl-from_archive"
- "clusterArray"
- "clusterByImageIdentifier"
- "clusterDividerArraySize = %d\n"
- "collapseSharpnessGrid"
- "colorHistogram"
- "com.apple.burstAnalyzer"
- "com.apple.camera"
- "com.apple.staccato_dump"
- "combined normalized focus score for face core detections = %f\n"
- "compareActionAmounts:"
- "compareDividers:"
- "compareImageOrder:"
- "compareImageStats:"
- "compareIndices:"
- "compileTime=%0.1fms "
- "completionBlock"
- "computeAEMatrix:"
- "computeAEMatrixDifference:"
- "computeActionSelectionThreshold"
- "computeAllImageScores"
- "computeAverage"
- "computeBeginningVsEndAEMatrixDiffVsAverageAdjacent"
- "computeBlurStatsOnGrid:"
- "computeCameraTravelDistance"
- "computeEmotion:"
- "computeFacialFocusScoreSum"
- "computeImageColorHistogram:"
- "computeImageData:faceIDCounts:"
- "computeImageDistance:"
- "computeImageProjections:"
- "computeImageSharpnessOnGrid:"
- "computeKernelValueWithSupportVector:"
- "computeMergeCost:::"
- "computeOutlineByTracingSnake:points"
- "computeOutlineByTracingSnake:snakeBodies"
- "computePupilAlphaMap:allPoints"
- "computePupilAlphaMap:alphaMap"
- "computeRuleOfThreeDistance"
- "computeScore:"
- "computeSmilePercentage"
- "computeSmoothedGridROI:nextStat:"
- "computeStandardDeviation"
- "convertRGBAToYUV420:rgbaBytesPerRow:"
- "countForObject:"
- "counter.bin"
- "curClusterIndexToProcess"
- "curConfig"
- "d24@0:8r^{CIBurstSupportVector=d[7d]}16"
- "dataPtr"
- "dataWithContentsOfFile:options:error:"
- "dd-MM-yyyy'_'HH-mm-ss'_burstLog.txt'"
- "detectFacesInImage:options:error:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithObjectsAndKeys:"
- "digraph %s {\n"
- "dissimilarity"
- "divider %d\n"
- "dividerScore"
- "doLimitedSharpnessAndBlur"
- "dq"
- "dq_yuvdump"
- "dummyAnalysisCount"
- "dumpFaceInfoArray"
- "emotionallyRejected"
- "enableAnalysis"
- "enableDumpYUV"
- "enableFaceCore"
- "error with the projections computation"
- "exclude"
- "expressionFeatures"
- "extractAlpha:alphaMap"
- "extractAlpha:savedscans"
- "extractAverageFaceY: bigyhisto"
- "extractDetails error: %s\n"
- "extractDetailsForFaces:inImage:options:error:"
- "extractFaceMetadata: invalid properties\n"
- "extractFacesFromMetadata:"
- "extractFirstGradientMaximumFrom:scanline"
- "f32@0:8@16@24"
- "f36@0:8@16^i24i32"
- "f48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "face"
- "face %d: rect = %.3f,%.3f,%.3f,%.3f, leftOpen=%d,rightOpen=%d\n"
- "faceAnalysisContext"
- "faceDetector"
- "faceDetectorWithOptions:"
- "faceIDCounts"
- "faceId"
- "faceIdCounter"
- "faceIdMapping"
- "faceInfoArray"
- "faceScore"
- "faceStat.id = %d\n"
- "faceStatArray"
- "faceTimestampArray"
- "facesRoiRect"
- "findBestImage:useActionScores:"
- "findFacesInImage:imageStat:"
- "findOverlappingFaceStat:imageStat:"
- "firstObject"
- "flagAsGarbage"
- "float __PQ_InvEOTF(float N, vec2 m, vec3 c) {\n  float mx = m.x;\n  float X = pow(N, mx);\n  float my = m.y;\n  return pow((c.x + (c.y * X)) / (1.0 + (c.z * X)), my);\n}\nfloat __HermiteSpline(float X, float KneeStart, float maxLum) {\n  return (((((((2.0 * X) * X) * X) - ((3 * X) * X)) + 1.0) * KneeStart) + (((((X * X) * X) - ((2 * X) * X)) + X) * (1.0 - KneeStart))) + ((((((-2.0) * X) * X) * X) + ((3 * X) * X)) * maxLum);\n}\nfloat __PQ_EOTF(float N, vec2 m, vec3 c) {\n  float X = pow(N, 1.0 / m.y);\n  return pow(max(X - c.x, 0.0) / (c.y - (c.z * X)), 1.0 / m.x);\n}\nfloat __PQ_EETF(float Y_in, vec2 m, vec3 c, vec4 levels, vec2 minmaxLum, vec2 knee) {\n  float masterPeakInv = levels.x;\n  float masterBlackInv = levels.y;\n  float minLum = minmaxLum.x;\n  float maxLum = minmaxLum.y;\n  float KneeStart = knee.x;\n  float KneeStartScale = knee.y;\n  float E = __PQ_InvEOTF(Y_in / 1.000000e+04, m, c);\n  E = (E - masterBlackInv) / (masterPeakInv - masterBlackInv);\n  E = (E < KneeStart) ? E : __HermiteSpline((E - KneeStart) * KneeStartScale, KneeStart, maxLum);\n  E = (E < 0.0) ? minLum : ((E < 1.0) ? (E + ((((minLum * (1 - E)) * (1 - E)) * (1 - E)) * (1 - E))) : E);\n  E = (E * (masterPeakInv - masterBlackInv)) + masterBlackInv;\n  return 1.000000e+04 * __PQ_EOTF(E, m, c);\n}\nkernel vec4 _pq_tonemapping(vec4 im, vec2 m, vec3 c, vec4 levels, vec2 minmaxLum, vec2 knee, vec4 lc) {\n  vec4 result = im;\n  float luminance = dot(im.rgb, lc.rgb);\n  if (luminance != 0) {\n    float out_luminance = __PQ_EETF(luminance, m, c, levels, minmaxLum, knee);\n    result.rgb *= out_luminance / luminance;\n  }\n  return result;\n}\n"
- "float _asgh(float x) {\n  x = abs(x);\n  if (x >= 3.0) return 0.0;\n  if (x < 1.000000e-06) return 1.0;\n  x *= 3.141593e+00;\n  float sinc = sin(x) / x;\n  float asgw = cos(x / 8.0);\n  return (((sinc * asgw) * asgw) * asgw) * asgw;\n}\nkernel vec4 _asgDownH(sampler src, vec4 scale, float z) {\n  vec2 c = destCoord() * scale.xy;\n  vec2 pm1 = vec2(floor(c.x - 0.5) + 0.5, c.y);\n  vec2 pm6 = pm1 - (scale.zw * 5.0);\n  vec2 pm5 = pm1 - (scale.zw * 4.0);\n  vec2 pm4 = pm1 - (scale.zw * 3.0);\n  vec2 pm3 = pm1 - (scale.zw * 2.0);\n  vec2 pm2 = pm1 - (scale.zw * 1.0);\n  vec2 pp1 = pm1 + (scale.zw * 1.0);\n  vec2 pp2 = pm1 + (scale.zw * 2.0);\n  vec2 pp3 = pm1 + (scale.zw * 3.0);\n  vec2 pp4 = pm1 + (scale.zw * 4.0);\n  vec2 pp5 = pm1 + (scale.zw * 5.0);\n  vec2 pp6 = pm1 + (scale.zw * 6.0);\n  vec4 vm6 = sample(src, samplerTransform(src, pm6));\n  vec4 vm5 = sample(src, samplerTransform(src, pm5));\n  vec4 vm4 = sample(src, samplerTransform(src, pm4));\n  vec4 vm3 = sample(src, samplerTransform(src, pm3));\n  vec4 vm2 = sample(src, samplerTransform(src, pm2));\n  vec4 vm1 = sample(src, samplerTransform(src, pm1));\n  vec4 vp1 = sample(src, samplerTransform(src, pp1));\n  vec4 vp2 = sample(src, samplerTransform(src, pp2));\n  vec4 vp3 = sample(src, samplerTransform(src, pp3));\n  vec4 vp4 = sample(src, samplerTransform(src, pp4));\n  vec4 vp5 = sample(src, samplerTransform(src, pp5));\n  vec4 vp6 = sample(src, samplerTransform(src, pp6));\n  float wm6 = _asgh(((pm6.x - c.x) / scale.x) + z);\n  float wm5 = _asgh(((pm5.x - c.x) / scale.x) + z);\n  float wm4 = _asgh(((pm4.x - c.x) / scale.x) + z);\n  float wm3 = _asgh(((pm3.x - c.x) / scale.x) + z);\n  float wm2 = _asgh(((pm2.x - c.x) / scale.x) + z);\n  float wm1 = _asgh(((pm1.x - c.x) / scale.x) + z);\n  float wp1 = _asgh(((pp1.x - c.x) / scale.x) + z);\n  float wp2 = _asgh(((pp2.x - c.x) / scale.x) + z);\n  float wp3 = _asgh(((pp3.x - c.x) / scale.x) + z);\n  float wp4 = _asgh(((pp4.x - c.x) / scale.x) + z);\n  float wp5 = _asgh(((pp5.x - c.x) / scale.x) + z);\n  float wp6 = _asgh(((pp6.x - c.x) / scale.x) + z);\n  float wsum = ((((((((((wm6 + wm5) + wm4) + wm3) + wm2) + wm1) + wp1) + wp2) + wp3) + wp4) + wp5) + wp6;\n  return ((((((((((((wm6 * vm6) + (wm5 * vm5)) + (wm4 * vm4)) + (wm3 * vm3)) + (wm2 * vm2)) + (wm1 * vm1)) + (wp6 * vp6)) + (wp5 * vp5)) + (wp4 * vp4)) + (wp3 * vp3)) + (wp2 * vp2)) + (wp1 * vp1)) / wsum;\n}\n"
- "float _asgv(float x) {\n  x = abs(x);\n  if (x >= 3.0) return 0.0;\n  if (x < 1.000000e-06) return 1.0;\n  x *= 3.141593e+00;\n  float sinc = sin(x) / x;\n  float asgw = cos(x / 8.0);\n  return (((sinc * asgw) * asgw) * asgw) * asgw;\n}\nkernel vec4 _asgDownV(sampler src, vec4 scale, float z) {\n  vec2 c = destCoord() * scale.xy;\n  vec2 pm1 = vec2(c.x, floor(c.y - 0.5) + 0.5);\n  vec2 pm6 = pm1 - (scale.zw * 5.0);\n  vec2 pm5 = pm1 - (scale.zw * 4.0);\n  vec2 pm4 = pm1 - (scale.zw * 3.0);\n  vec2 pm3 = pm1 - (scale.zw * 2.0);\n  vec2 pm2 = pm1 - (scale.zw * 1.0);\n  vec2 pp1 = pm1 + (scale.zw * 1.0);\n  vec2 pp2 = pm1 + (scale.zw * 2.0);\n  vec2 pp3 = pm1 + (scale.zw * 3.0);\n  vec2 pp4 = pm1 + (scale.zw * 4.0);\n  vec2 pp5 = pm1 + (scale.zw * 5.0);\n  vec2 pp6 = pm1 + (scale.zw * 6.0);\n  vec4 vm6 = sample(src, samplerTransform(src, pm6));\n  vec4 vm5 = sample(src, samplerTransform(src, pm5));\n  vec4 vm4 = sample(src, samplerTransform(src, pm4));\n  vec4 vm3 = sample(src, samplerTransform(src, pm3));\n  vec4 vm2 = sample(src, samplerTransform(src, pm2));\n  vec4 vm1 = sample(src, samplerTransform(src, pm1));\n  vec4 vp1 = sample(src, samplerTransform(src, pp1));\n  vec4 vp2 = sample(src, samplerTransform(src, pp2));\n  vec4 vp3 = sample(src, samplerTransform(src, pp3));\n  vec4 vp4 = sample(src, samplerTransform(src, pp4));\n  vec4 vp5 = sample(src, samplerTransform(src, pp5));\n  vec4 vp6 = sample(src, samplerTransform(src, pp6));\n  float wm6 = _asgv(((pm6.y - c.y) / scale.y) + z);\n  float wm5 = _asgv(((pm5.y - c.y) / scale.y) + z);\n  float wm4 = _asgv(((pm4.y - c.y) / scale.y) + z);\n  float wm3 = _asgv(((pm3.y - c.y) / scale.y) + z);\n  float wm2 = _asgv(((pm2.y - c.y) / scale.y) + z);\n  float wm1 = _asgv(((pm1.y - c.y) / scale.y) + z);\n  float wp1 = _asgv(((pp1.y - c.y) / scale.y) + z);\n  float wp2 = _asgv(((pp2.y - c.y) / scale.y) + z);\n  float wp3 = _asgv(((pp3.y - c.y) / scale.y) + z);\n  float wp4 = _asgv(((pp4.y - c.y) / scale.y) + z);\n  float wp5 = _asgv(((pp5.y - c.y) / scale.y) + z);\n  float wp6 = _asgv(((pp6.y - c.y) / scale.y) + z);\n  float wsum = ((((((((((wm6 + wm5) + wm4) + wm3) + wm2) + wm1) + wp1) + wp2) + wp3) + wp4) + wp5) + wp6;\n  return ((((((((((((wm6 * vm6) + (wm5 * vm5)) + (wm4 * vm4)) + (wm3 * vm3)) + (wm2 * vm2)) + (wm1 * vm1)) + (wp6 * vp6)) + (wp5 * vp5)) + (wp4 * vp4)) + (wp3 * vp3)) + (wp2 * vp2)) + (wp1 * vp1)) / wsum;\n}\n"
- "float _ci_simdgroup_barrier() {\n  return 0.0;\n}\nkernel vec4 _ci_writeTG_42X(const vec4 color, vec4 shuffleMask) {\n  const int grid = 16;\n  vec4 tgcc[256];\n  const vec2 py = writeCoord();\n  const int x = int(py.x);\n  const int y = int(py.y);\n  const int index = ((y % grid) * grid) + (x % grid);\n  if (((x % 2) == 0) && ((y % 2) == 0)) {\n    tgcc[index] = vec4(0.0, 0.0, 0.0, 0.0);\n    tgcc[index + grid] = vec4(0.0, 0.0, 0.0, 0.0);\n    tgcc[index + 1] = vec4(0.0, 0.0, 0.0, 0.0);\n    tgcc[(index + 1) + grid] = vec4(0.0, 0.0, 0.0, 0.0);\n  }\n  _ci_simdgroup_barrier();\n  tgcc[index] = vec4(color.g, color.b, 1.0, 1.0);\n  _ci_simdgroup_barrier();\n  if (shuffleMask.w > 1.000000e-03) {\n    if (((x % 2) == 0) && ((y % 2) == 0)) {\n      vec4 ccvv = vec4(tgcc[index]);\n      ccvv += vec4(tgcc[index + 1]);\n      ccvv += vec4(tgcc[index + grid]);\n      ccvv += vec4(tgcc[(index + 1) + grid]);\n      writeImagePlane(ccvv.rgrg / ccvv.a, py / 2.0);\n    }\n  } else if (shuffleMask.y > 1.000000e-03) {\n    if ((x % 2) == 0) {\n      vec4 ccvv = vec4(tgcc[index]);\n      ccvv += vec4(tgcc[index + 1]);\n      writeImagePlane(ccvv.rgrg / ccvv.a, py / vec2(2.0, 1.0));\n    }\n  }\n  writeImage(color.rrrr, py);\n  return color;\n}\n"
- "float _lanc3h(float x) {\n  x = abs(x);\n  if (x >= 3.0) return 0.0;\n  if (x < 1.000000e-03) return 1.0;\n  x *= 3.141593e+00;\n  return ((3.0 * sin(x)) * sin(x / 3.0)) / (x * x);\n}\nkernel vec4 _lanczosDownH(sampler src, vec4 scale) {\n  vec2 c = destCoord() * scale.xy;\n  vec2 pm1 = vec2(floor(c.x - 0.5) + 0.5, c.y);\n  vec2 pm6 = pm1 - (scale.zw * 5.0);\n  vec2 pm5 = pm1 - (scale.zw * 4.0);\n  vec2 pm4 = pm1 - (scale.zw * 3.0);\n  vec2 pm3 = pm1 - (scale.zw * 2.0);\n  vec2 pm2 = pm1 - (scale.zw * 1.0);\n  vec2 pp1 = pm1 + (scale.zw * 1.0);\n  vec2 pp2 = pm1 + (scale.zw * 2.0);\n  vec2 pp3 = pm1 + (scale.zw * 3.0);\n  vec2 pp4 = pm1 + (scale.zw * 4.0);\n  vec2 pp5 = pm1 + (scale.zw * 5.0);\n  vec2 pp6 = pm1 + (scale.zw * 6.0);\n  vec4 vm6 = sample(src, samplerTransform(src, pm6));\n  vec4 vm5 = sample(src, samplerTransform(src, pm5));\n  vec4 vm4 = sample(src, samplerTransform(src, pm4));\n  vec4 vm3 = sample(src, samplerTransform(src, pm3));\n  vec4 vm2 = sample(src, samplerTransform(src, pm2));\n  vec4 vm1 = sample(src, samplerTransform(src, pm1));\n  vec4 vp1 = sample(src, samplerTransform(src, pp1));\n  vec4 vp2 = sample(src, samplerTransform(src, pp2));\n  vec4 vp3 = sample(src, samplerTransform(src, pp3));\n  vec4 vp4 = sample(src, samplerTransform(src, pp4));\n  vec4 vp5 = sample(src, samplerTransform(src, pp5));\n  vec4 vp6 = sample(src, samplerTransform(src, pp6));\n  float wm6 = _lanc3h((pm6.x - c.x) / scale.x);\n  float wm5 = _lanc3h((pm5.x - c.x) / scale.x);\n  float wm4 = _lanc3h((pm4.x - c.x) / scale.x);\n  float wm3 = _lanc3h((pm3.x - c.x) / scale.x);\n  float wm2 = _lanc3h((pm2.x - c.x) / scale.x);\n  float wm1 = _lanc3h((pm1.x - c.x) / scale.x);\n  float wp1 = _lanc3h((pp1.x - c.x) / scale.x);\n  float wp2 = _lanc3h((pp2.x - c.x) / scale.x);\n  float wp3 = _lanc3h((pp3.x - c.x) / scale.x);\n  float wp4 = _lanc3h((pp4.x - c.x) / scale.x);\n  float wp5 = _lanc3h((pp5.x - c.x) / scale.x);\n  float wp6 = _lanc3h((pp6.x - c.x) / scale.x);\n  float wsum = ((((((((((wm6 + wm5) + wm4) + wm3) + wm2) + wm1) + wp1) + wp2) + wp3) + wp4) + wp5) + wp6;\n  return ((((((((((((wm6 * vm6) + (wm5 * vm5)) + (wm4 * vm4)) + (wm3 * vm3)) + (wm2 * vm2)) + (wm1 * vm1)) + (wp6 * vp6)) + (wp5 * vp5)) + (wp4 * vp4)) + (wp3 * vp3)) + (wp2 * vp2)) + (wp1 * vp1)) / wsum;\n}\n"
- "float _lanc3v(float x) {\n  x = abs(x);\n  if (x >= 3.0) return 0.0;\n  if (x < 1.000000e-03) return 1.0;\n  x *= 3.141593e+00;\n  return ((3.0 * sin(x)) * sin(x / 3.0)) / (x * x);\n}\nkernel vec4 _lanczosDownV(sampler src, vec4 scale) {\n  vec2 c = destCoord() * scale.xy;\n  vec2 pm1 = vec2(c.x, floor(c.y - 0.5) + 0.5);\n  vec2 pm6 = pm1 - (scale.zw * 5.0);\n  vec2 pm5 = pm1 - (scale.zw * 4.0);\n  vec2 pm4 = pm1 - (scale.zw * 3.0);\n  vec2 pm3 = pm1 - (scale.zw * 2.0);\n  vec2 pm2 = pm1 - (scale.zw * 1.0);\n  vec2 pp1 = pm1 + (scale.zw * 1.0);\n  vec2 pp2 = pm1 + (scale.zw * 2.0);\n  vec2 pp3 = pm1 + (scale.zw * 3.0);\n  vec2 pp4 = pm1 + (scale.zw * 4.0);\n  vec2 pp5 = pm1 + (scale.zw * 5.0);\n  vec2 pp6 = pm1 + (scale.zw * 6.0);\n  vec4 vm6 = sample(src, samplerTransform(src, pm6));\n  vec4 vm5 = sample(src, samplerTransform(src, pm5));\n  vec4 vm4 = sample(src, samplerTransform(src, pm4));\n  vec4 vm3 = sample(src, samplerTransform(src, pm3));\n  vec4 vm2 = sample(src, samplerTransform(src, pm2));\n  vec4 vm1 = sample(src, samplerTransform(src, pm1));\n  vec4 vp1 = sample(src, samplerTransform(src, pp1));\n  vec4 vp2 = sample(src, samplerTransform(src, pp2));\n  vec4 vp3 = sample(src, samplerTransform(src, pp3));\n  vec4 vp4 = sample(src, samplerTransform(src, pp4));\n  vec4 vp5 = sample(src, samplerTransform(src, pp5));\n  vec4 vp6 = sample(src, samplerTransform(src, pp6));\n  float wm6 = _lanc3v((pm6.y - c.y) / scale.y);\n  float wm5 = _lanc3v((pm5.y - c.y) / scale.y);\n  float wm4 = _lanc3v((pm4.y - c.y) / scale.y);\n  float wm3 = _lanc3v((pm3.y - c.y) / scale.y);\n  float wm2 = _lanc3v((pm2.y - c.y) / scale.y);\n  float wm1 = _lanc3v((pm1.y - c.y) / scale.y);\n  float wp1 = _lanc3v((pp1.y - c.y) / scale.y);\n  float wp2 = _lanc3v((pp2.y - c.y) / scale.y);\n  float wp3 = _lanc3v((pp3.y - c.y) / scale.y);\n  float wp4 = _lanc3v((pp4.y - c.y) / scale.y);\n  float wp5 = _lanc3v((pp5.y - c.y) / scale.y);\n  float wp6 = _lanc3v((pp6.y - c.y) / scale.y);\n  float wsum = ((((((((((wm6 + wm5) + wm4) + wm3) + wm2) + wm1) + wp1) + wp2) + wp3) + wp4) + wp5) + wp6;\n  return ((((((((((((wm6 * vm6) + (wm5 * vm5)) + (wm4 * vm4)) + (wm3 * vm3)) + (wm2 * vm2)) + (wm1 * vm1)) + (wp6 * vp6)) + (wp5 * vp5)) + (wp4 * vp4)) + (wp3 * vp3)) + (wp2 * vp2)) + (wp1 * vp1)) / wsum;\n}\n"
- "float4 tgcc"
- "focusScore"
- "forceFaceDetectionEnable"
- "foundByFaceCore"
- "framesSinceLast"
- "fullsizeJpegData"
- "fullsizeJpegSize"
- "function not implemented"
- "getSharpnessAndBlurLimits"
- "gridHeight"
- "gridROI"
- "gridWidth"
- "hasBeenScaled"
- "hasLeftEye"
- "hasRegistrationData"
- "hasRightEye"
- "hasRollAngle"
- "hasYawAngle"
- "highNoiseThreshold"
- "hwCenter"
- "hwFaceId"
- "hwFaceRect"
- "hwId = %d (lastSeen=%d, ctr=%.3f,%.3f size=%.3f,%.3f), swId = %d (lastSeen=%d, ctr=%.3f,%.3f size=%.3f,%.3f)\n"
- "hwLastFrameSeen"
- "hwSize"
- "imageId"
- "imageProps"
- "imageScore"
- "image_render_to_surface"
- "infill arcs surround arcs"
- "infill area boundary path"
- "initBitmask:b"
- "initBitmask:b->body"
- "initWithCGImage: %dx%d\n"
- "initWithCGImage:maxDimension:"
- "initWithCIImage:ctx:maxDimension:"
- "initWithExternalBuffer:size:rowBytes:f"
- "initWithExternalBuffer:subRectange:fullSize:rowBytes:f"
- "initWithFaceStat:"
- "initWithIOSurface:maxDimension:"
- "initWithIdentifier:"
- "initWithImageData:dict:identifier:imageProps:completionBlock:"
- "initWithRect:withFaceId:"
- "initWithScore:"
- "initWithSurface:texture:digest:allowSRGB:bounds:context:"
- "initWithSurface:texture:digest:allowSRGB:bounds:context:tileTask:"
- "initWithSurface:texture:digest:allowSRGB:bounds:roiTileIndex:roiTileCount:context:"
- "initWithVersion:"
- "initWithWidth:height:bytesPerRow:buffer:freeWhenDone:"
- "inputQualityLevel"
- "int soft_horizonDetectionFFTAngles(uint8_t *, int, int, int, _Bool, float, int, _CIHorizonDetectedAngle *)"
- "internal error"
- "invalid option"
- "invalid parameter"
- "ioSurf"
- "isBurstAction"
- "isFaceDetectionForced"
- "isGarbage"
- "isSyncedWithImage"
- "kPixelFormatARGB10WideLinear"
- "kSwizzleARGB10"
- "kSwizzleToARGB10"
- "kSwizzleToRGB14"
- "kern.osversion"
- "kernel vec2 _flashGeom(vec2 center) {\n  vec2 delta = destCoord() - center;\n  float len = length(delta);\n  return ((delta * 1.000000e+02) / len) + vec2(1.280000e+02);\n}\n"
- "kernel vec2 _perspectiveCorrection(vec3 A1, vec3 A2, vec3 A3) {\n  vec3 h = vec3(destCoord(), 1.0);\n  vec2 p = vec2(dot(h, A1), dot(h, A2));\n  return p / max(dot(h, A3), 1.000000e-06);\n}\n"
- "kernel vec2 _perspectiveTransform(vec3 A1, vec3 A2, vec3 A3, vec2 origin) {\n  vec3 h = vec3(destCoord(), 1.0);\n  vec2 p = vec2(dot(h, A1), dot(h, A2));\n  float w = 1.0 / max(dot(h, A3), 1.000000e-06);\n  return (p * w) + origin;\n}\n"
- "kernel vec2 _pinchDistortionScaleGE1(vec2 c, vec4 param) {\n  vec2 p = destCoord() - c;\n  float r = (length(p) * param.y) + 1.000000e-06;\n  vec2 pRGT = (pow(r, param.w) * p) + c;\n  p = (p * inversesqrt(r)) + c;\n  p = mix(destCoord(), p, param.z);\n  return (r <= 1.0) ? p : pRGT;\n}\n"
- "kernel vec2 _pinchDistortionScaleLT1(vec2 c, vec4 param) {\n  vec2 p = destCoord() - c;\n  float r = (length(p) * param.y) + 1.000000e-06;\n  p = (p * inversesqrt(r)) + c;\n  return mix(destCoord(), p, param.z);\n}\n"
- "kernel vec4 _ACCentroid(vec4 c, vec4 extent) {\n  return vec4(extent.xy + ((c.xy / max(c.z, 1.000000e-04)) * vec2(extent.zw)), 0.0, 1.0);\n}\n"
- "kernel vec4 _CBHorz(sampler u, float k, float colorInv, float spatialInv) {\n  vec2 dc = destCoord();\n  vec4 u_0 = sample(u, samplerTransform(u, dc));\n  vec4 Cacc = vec4(0.0);\n  float W = 0.0;\n  int kk = int(k);\n  for (int x = -kk; x <= kk; x++) {\n    float ws = exp((-float(x * x)) * spatialInv);\n    vec4 u_xy = sample(u, samplerTransform(u, dc + vec2(x, 0.0)));\n    float r2 = dot(u_xy.rgb - u_0.rgb, u_xy.rgb - u_0.rgb);\n    float wc = exp((-r2) * colorInv);\n    float w = (ws * wc) * u_xy.a;\n    W += w;\n    Cacc += w * u_xy;\n  }\n  return vec4((W < 1.000000e-05) ? u_0.rgb : (Cacc.rgb / W), u_0.a);\n}\n"
- "kernel vec4 _CBHorzGuided(sampler u, sampler v, float k, float colorInv, float spatialInv) {\n  vec2 dc = destCoord();\n  vec4 u_0 = sample(u, samplerTransform(u, dc));\n  vec4 v_0 = sample(v, samplerTransform(v, dc));\n  vec4 Cacc = vec4(0.0);\n  float W = 0.0;\n  int kk = int(k);\n  for (int x = -kk; x <= kk; x++) {\n    float ws = exp((-float(x * x)) * spatialInv);\n    vec4 u_xy = sample(u, samplerTransform(u, dc + vec2(x, 0.0)));\n    vec4 v_xy = sample(v, samplerTransform(v, dc + vec2(x, 0.0)));\n    float r2 = dot(u_xy.rgb - u_0.rgb, u_xy.rgb - u_0.rgb);\n    float wc = exp((-r2) * colorInv);\n    float w = (ws * wc) * u_xy.a;\n    W += w;\n    Cacc += w * v_xy;\n  }\n  return vec4((W < 1.000000e-05) ? v_0.rgb : (Cacc.rgb / W), v_0.a);\n}\n"
- "kernel vec4 _CBVert(sampler u, float k, float colorInv, float spatialInv) {\n  vec2 dc = destCoord();\n  vec4 u_0 = sample(u, samplerTransform(u, dc));\n  vec4 Cacc = vec4(0.0);\n  float W = 0.0;\n  int kk = int(k);\n  for (int y = -kk; y <= kk; y++) {\n    float ws = exp((-float(y * y)) * spatialInv);\n    vec4 u_xy = sample(u, samplerTransform(u, dc + vec2(0.0, y)));\n    float r2 = dot(u_xy.rgb - u_0.rgb, u_xy.rgb - u_0.rgb);\n    float wc = exp((-r2) * colorInv);\n    float w = (ws * wc) * u_xy.a;\n    W += w;\n    Cacc += w * u_xy;\n  }\n  return vec4((W < 1.000000e-05) ? u_0.rgb : (Cacc.rgb / W), u_0.a);\n}\n"
- "kernel vec4 _CBVertGuided(sampler u, sampler v, float k, float colorInv, float spatialInv) {\n  vec2 dc = destCoord();\n  vec4 u_0 = sample(u, samplerTransform(u, dc));\n  vec4 v_0 = sample(v, samplerTransform(v, dc));\n  vec4 Cacc = vec4(0.0);\n  float W = 0.0;\n  int kk = int(k);\n  for (int y = -kk; y <= kk; y++) {\n    float ws = exp((-float(y * y)) * spatialInv);\n    vec4 u_xy = sample(u, samplerTransform(u, dc + vec2(0.0, y)));\n    vec4 v_xy = sample(v, samplerTransform(v, dc + vec2(0.0, y)));\n    float r2 = dot(u_xy.rgb - u_0.rgb, u_xy.rgb - u_0.rgb);\n    float wc = exp((-r2) * colorInv);\n    float w = (ws * wc) * u_xy.a;\n    W += w;\n    Cacc += w * v_xy;\n  }\n  return vec4((W < 1.000000e-05) ? v_0.rgb : (Cacc.rgb / W), v_0.a);\n}\n"
- "kernel vec4 _CEstretch(vec4 c, vec4 lohi, float amount) {\n  float lov = lohi.r;\n  float hiv = lohi.g;\n  return vec4(mix(c.rgb, clamp((c.rgb - lov) / max(1.000000e-05, hiv - lov), 0.0, 1.0), amount), c.a);\n}\n"
- "kernel vec4 _CIPortraitBlurDir(sampler image, vec3 params) {\n  vec2 dir = params.yz;\n  vec2 dc = destCoord();\n  vec4 pix0 = sample(image, samplerTransform(image, dc - (3.0 * dir)));\n  vec4 pix1 = sample(image, samplerTransform(image, dc - (2.0 * dir)));\n  vec4 pix2 = sample(image, samplerTransform(image, dc - dir));\n  vec4 pix3 = sample(image, samplerTransform(image, dc));\n  vec4 pix4 = sample(image, samplerTransform(image, dc + dir));\n  vec4 pix5 = sample(image, samplerTransform(image, dc + (2.0 * dir)));\n  vec4 pix6 = sample(image, samplerTransform(image, dc + (3.0 * dir)));\n  float outW = pix3.w;\n  pix0.w = pix0.w * pix0.w;\n  pix1.w = pix1.w * pix1.w;\n  pix2.w = pix2.w * pix2.w;\n  pix3.w = pix3.w * pix3.w;\n  pix4.w = pix4.w * pix4.w;\n  pix5.w = pix5.w * pix5.w;\n  pix6.w = pix6.w * pix6.w;\n  float radius = max(params.x * pix3.w, 1.000000e-02);\n  float radius2 = 1.0 / ((2.0 * radius) * radius);\n  float weight0 = 1.0;\n  float weight1 = exp((-1.0) * radius2);\n  float weight2 = ((weight1 * weight1) * weight1) * weight1;\n  float weight3 = (weight2 * weight2) * weight1;\n  float invWeightSum = 1.0 / (((((((pix0.w * weight3) + (pix1.w * weight2)) + (pix2.w * weight1)) + (pix3.w * weight0)) + (pix4.w * weight1)) + (pix5.w * weight2)) + (pix6.w * weight3));\n  weight0 *= invWeightSum;\n  weight1 *= invWeightSum;\n  weight2 *= invWeightSum;\n  weight3 *= invWeightSum;\n  vec4 pixOut;\n  pixOut.xyz = (((((((weight3 * pix0.w) * pix0.xyz) + ((weight2 * pix1.w) * pix1.xyz)) + ((weight1 * pix2.w) * pix2.xyz)) + ((weight0 * pix3.w) * pix3.xyz)) + ((weight1 * pix4.w) * pix4.xyz)) + ((weight2 * pix5.w) * pix5.xyz)) + ((weight3 * pix6.w) * pix6.xyz);\n  pixOut.w = outW;\n  return pixOut;\n}\n"
- "kernel vec4 _DEWash(vec4 c, vec4 w) {\n  return c / (1.000000e-06 + w);\n}\n"
- "kernel vec4 _DEnormalizeAlpha(vec4 c) {\n  return (c * smoothstep(1.000000e-03, 1.000000e-01, c.a)) / max(c.a, 1.000000e-04);\n}\n"
- "kernel vec4 _LAB_denormalize(vec4 c) {\n  c.r *= 1.000000e+02;\n  c.gb = (c.gb - 0.5) * 1.280000e+02;\n  return c;\n}\n"
- "kernel vec4 _LAB_normalize(vec4 c) {\n  c.r /= 1.000000e+02;\n  c.gb = (c.gb / 1.280000e+02) + 0.5;\n  return c;\n}\n"
- "kernel vec4 _appleLogToLinear(vec4 P) {\n  const float R0 = -5.641088e-02;\n  const float Rt = 1.000000e-02;\n  const float c = 4.728711e+01;\n  const float beta = 9.640520e-03;\n  const float gamma = 8.550479e-02;\n  const float delta = 6.933694e-01;\n  const float Pt = (c * (Rt - R0)) * (Rt - R0);\n  vec4 Ra;\n  vec4 Rb = sqrt(P / c) + R0;\n}\n"
- "kernel vec4 _blurredrect(vec4 bounds, float sigma, vec4 color) {\n  vec2 x, p = destCoord();\n  vec2 lo = bounds.xy;\n  vec2 hi = bounds.zw;\n  sigma *= 2.400;\n  x = clamp((p - (lo - sigma)) / (2.0 * sigma), 0.0, 1.0);\n  vec2 v1 = ((x * x) * x) * ((((6.0 * x) - 1.500000e+01) * x) + 1.000000e+01);\n  x = clamp(((hi + sigma) - p) / (2.0 * sigma), 0.0, 1.0);\n  vec2 v2 = ((x * x) * x) * ((((6.0 * x) - 1.500000e+01) * x) + 1.000000e+01);\n  return color * (((v1.x * v1.y) * v2.x) * v2.y);\n}\n"
- "kernel vec4 _boostHybrid(vec4 color, vec4 rgblboostnogamma, float transitionBreakpoint, float transitionWidth, float luminanceAmount) {\n  float luminance, factor, interpolant;\n  vec4 xcolor, answer;\n  luminance = dot(color.rgb, vec3(0.299, 0.587, 0.114));\n  answer = rgblboostnogamma;\n  xcolor = color;\n  xcolor.a = luminance;\n  answer = compare(xcolor, vec4(0.0), answer);\n  answer = max(answer, vec4(0.0));\n  factor = answer.a / max(luminance, 1.000000e-06);\n  color.rgb = color.rgb * vec3(factor);\n  color.rgb = max(color.rgb, vec3(0.0));\n  interpolant = clamp((luminance - (transitionBreakpoint - (transitionWidth * 0.5))) / transitionWidth, 0.0, 1.0);\n  interpolant = 1.0 - (((3.0 - (2.0 * interpolant)) * interpolant) * interpolant);\n  interpolant = interpolant * luminanceAmount;\n  color.rgb = mix(answer.rgb, color.rgb, interpolant);\n  return color;\n}\n"
- "kernel vec4 _ciSingleChannelColorMap(sampler s, sampler lut) {\n  float v = clamp(sample(s, samplerCoord(s)).x, 0.0, 1.0);\n  float vInt = (256.0 - 1.0) * v;\n  vec2 xy = samplerTransform(lut, vec2(vInt, 0.5));\n  return sample(lut, xy);\n}\n"
- "kernel vec4 _ci_combine_420(vec4 s00, vec4 s10, vec4 s01, vec4 s11) {\n  vec2 pc = writeCoord();\n  vec2 py = pc * 2.0;\n  writeImage(s00.rrrr, py);\n  writeImage(s10.rrrr, py + vec2(1, 0));\n  writeImage(s01.rrrr, py + vec2(0, 1));\n  writeImage(s11.rrrr, py + vec2(1, 1));\n  vec4 cc = (((s00 + s10) + s01) + s11) * 0.25;\n  writeImagePlane(vec4(cc.gb, 0.0, 0.0), pc);\n  return s00;\n}\n"
- "kernel vec4 _ci_combine_422(vec4 s0, vec4 s1) {\n  vec2 pc = writeCoord();\n  vec2 py = vec2(pc.x * 2.0, pc.y);\n  writeImage(s0.rrrr, py);\n  writeImage(s1.rrrr, py + vec2(1, 0));\n  vec4 cc = (s0 + s1) * 0.5;\n  writeImagePlane(vec4(cc.gb, 0.0, 0.0), pc);\n  return s0;\n}\n"
- "kernel vec4 _ci_to_a2bgr10_as_rgba8(vec4 s) {\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.r);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.b) << 20;\n  pixel |= int(denorm.a) << 30;\n  writePixel(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255, writeCoord());\n  return s;\n}\n"
- "kernel vec4 _ci_to_a2rgb10_as_rgba8(vec4 s) {\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.b);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.r) << 20;\n  pixel |= int(denorm.a) << 30;\n  writePixel(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255, writeCoord());\n  return s;\n}\n"
- "kernel vec4 _ci_to_rgb10_as_rgba8(vec4 s) {\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.b);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.r) << 20;\n  pixel |= 3 << 30;\n  writePixel(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255, writeCoord());\n  return s;\n}\n"
- "kernel vec4 _ci_to_rgb10wide_as_rgba8(vec4 s) {\n  s = vec4((linear_to_srgb(s.rgb) * (510.0 / 1023.0)) + (384.0 / 1023.0), 1.0);\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.b);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.r) << 20;\n  pixel |= int(denorm.a) << 30;\n  writePixel(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255, writeCoord());\n  return s;\n}\n"
- "kernel vec4 _ci_to_rgb10widelinear_as_rgba8(vec4 s) {\n  s = vec4((s.rgb * (510.0 / 1023.0)) + (384.0 / 1023.0), 1.0);\n  vec4 denorm = (clamp(s, vec4(0.0), vec4(1.0)) * vec4(vec3(1023.0), 3.0)) + 0.5;\n  int pixel = int(denorm.b);\n  pixel |= int(denorm.g) << 10;\n  pixel |= int(denorm.r) << 20;\n  pixel |= int(denorm.a) << 30;\n  writePixel(pixel & 255, (pixel >> 8) & 255, (pixel >> 16) & 255, (pixel >> 24) & 255, writeCoord());\n  return s;\n}\n"
- "kernel vec4 _ci_unpremul(vec4 s) {\n  vec4 tmp = max(s, vec4(1.000000e-05));\n  return vec4(s.rgb / tmp.a, s.a);\n}\n"
- "kernel vec4 _cmcubeopaque(vec4 im, sampler2D cube, vec4 dims) {\n  im.rgb = clamp(im.rgb, 1.000000e-04, 9.999000e-01);\n  im.rgb *= dims.x;\n  float imb = floor(im.b);\n  float flr = max(imb, 0.0);\n  float pageA = flr;\n  float dimsx = dims.x;\n  float pageB = min(pageA + 1.0, dimsx);\n  vec2 xy = vec2(0.5 + im.rg);\n  vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n  vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n  vec2 dimszw = vec2(dims.zw);\n  vec3 sLo = vec3(texture2D(cube, pLo * dimszw).rgb);\n  vec3 sHi = vec3(texture2D(cube, pHi * dimszw).rgb);\n  im.rgb = mix(sLo, sHi, im.b - flr);\n  return im;\n}\n"
- "kernel vec4 _colorBlendMode_v0(vec4 pCf, vec4 pCb) {\n  vec4 uCf = unpremultiply(pCf);\n  vec4 uCb = unpremultiply(pCb);\n  vec4 uCfSort = (uCf.r > uCf.g) ? uCf : uCf.grba;\n  uCfSort = (uCfSort.g > uCfSort.b) ? uCfSort : uCfSort.rbga;\n  uCfSort = (uCfSort.r > uCfSort.g) ? uCfSort : uCfSort.grba;\n  float fL = (uCfSort.r + uCfSort.b) * 0.5;\n  float cmax = uCfSort.r;\n  float cmin = uCfSort.b;\n  vec4 uCbSort = (uCb.r > uCb.g) ? uCb : uCb.grba;\n  uCbSort = (uCbSort.g > uCbSort.b) ? uCbSort : uCbSort.rbga;\n  uCbSort = (uCbSort.r > uCbSort.g) ? uCbSort : uCbSort.grba;\n  float bL = (uCbSort.r + uCbSort.b) * 0.5;\n  float d = cmax - cmin;\n  float dv = (fL < 0.5) ? (cmax + cmin) : (2.0 - (cmax + cmin));\n  float s = d / max(dv, 1.000000e-06);\n  float mmax = (bL <= 0.5) ? (bL + (bL * s)) : ((bL + s) - (bL * s));\n  float mmin = (bL * 2.0) - mmax;\n  vec4 Ct = (((uCf - uCfSort.b) * (mmax - mmin)) / (uCfSort.r - uCfSort.b)) + mmin;\n  Ct = ((mmin + 1.000000e-05) > mmax) ? vec4(mmin) : Ct;\n  Ct.a = uCb.a;\n  vec4 Cb = vec4(uCb.rgb * uCb.a, uCb.a);\n  Ct = mix(uCf, Ct, uCb.a);\n  Ct.a = 1.0;\n  return mix(Cb, Ct, uCf.a);\n}\n"
- "kernel vec4 _colorBurnBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 B = 1.0 - ((1.0 - Cb) / max(Cs, vec4(1.000000e-07)));\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
- "kernel vec4 _colorControls(vec4 src, float threshold, float contrast) {\n  vec4 pix = vec4(src.rgb / max(src.a, 1.000000e-05), src.a);\n  float f = clamp(((dot(pix.rgb, vec3(2.125000e-01, 7.154000e-01, 7.210000e-02)) - threshold) * contrast) + 0.5, 0.0, 1.0);\n  return vec4(0.0, 0.0, 0.0, f);\n}\n"
- "kernel vec4 _colorDodgeBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 B = Cb / max(1.0 - Cs, vec4(1.000000e-07));\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
- "kernel vec4 _colorMonochrome(vec4 img, vec4 color, float intensity) {\n  float c1 = dot(img.rgb, vec3(2.125000e-01, 7.154000e-01, 7.210000e-02));\n  vec4 low = (2.0 * c1) * color;\n  vec4 high = 1.0 - (2.0 * ((1.0 - c1) * (vec4(1.0) - color)));\n  vec4 lt = vec4(lessThan(vec4(c1 - 0.5), vec4(0.0)));\n  vec4 pix = mix(img, mix(high, low, lt), intensity);\n  img.rgb = pix.rgb;\n  return img;\n}\n"
- "kernel vec4 _colorbalance(vec4 pix, vec4 clr, vec4 params) {\n  pix.rgb = ((pix.r * vec3(0.299, 5.957160e-01, 2.114560e-01)) + (pix.g * vec3(0.587, -2.744530e-01, -5.225910e-01))) + (pix.b * vec3(0.114, -3.212630e-01, 3.111350e-01));\n  clr.rgb /= max(clr.a, 1.000000e-05);\n  clr.rgb = pow(max(clr.rgb, 0.0), vec3(0.25));\n  clr.rgb = ((clr.r * vec3(0.299, 5.957160e-01, 2.114560e-01)) + (clr.g * vec3(0.587, -2.744530e-01, -5.225910e-01))) + (clr.b * vec3(0.114, -3.212630e-01, 3.111350e-01));\n  pix.gb += (params.z * (params.xy - clr.gb)) * pow(pix.r, params.w);\n  pix.rgb = ((pix.r * vec3(1.0)) + (pix.g * vec3(9.562960e-01, -2.721220e-01, -1.10699))) + (pix.b * vec3(6.210240e-01, -6.473810e-01, 1.70461));\n  return pix;\n}\n"
- "kernel vec4 _colorcube(vec4 im, sampler2D cube, vec4 dims) {\n  im.rgb = clamp(im.rgb, 1.000000e-05, 9.999900e-01);\n  im.rgb *= dims.x;\n  float flr = floor(im.b);\n  float pageA = flr;\n  float pageB = min(pageA + 1.0, dims.x);\n  vec2 xy = 0.5 + im.rg;\n  vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n  vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n  vec4 sLo = texture2D(cube, pLo * dims.zw);\n  vec4 sHi = texture2D(cube, pHi * dims.zw);\n  vec4 cubeOut = mix(sLo, sHi, im.b - flr);\n  return vec4(cubeOut.rgb, cubeOut.a * im.a);\n}\n"
- "kernel vec4 _colorcubeopaque(vec4 im, sampler2D cube, vec4 dims) {\n  im.rgb = clamp(im.rgb, 1.000000e-05, 9.999900e-01);\n  im.rgb *= dims.x;\n  float flr = floor(im.b);\n  float pageA = flr;\n  float pageB = min(pageA + 1.0, dims.x);\n  vec2 xy = 0.5 + im.rg;\n  vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n  vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n  vec4 sLo = texture2D(cube, pLo * dims.zw);\n  vec4 sHi = texture2D(cube, pHi * dims.zw);\n  vec4 cubeOut = mix(sLo, sHi, im.b - flr);\n  return vec4(cubeOut.rgb, im.a);\n}\n"
- "kernel vec4 _colorcubeopaque_extend(vec4 im, sampler2D cube, vec4 dims) {\n  vec4 c0 = vec4(0.3, 0.3, 0.3, 1.0);\n  float d0 = length(im.rgb - c0.rgb);\n  float d1 = length(clamp(im.rgb, 0.0, 1.0) - c0.rgb);\n  im.rgb = clamp(im.rgb, 1.000000e-05, 9.999900e-01);\n  im.rgb *= dims.x;\n  float flr = floor(im.b);\n  float pageA = flr;\n  float pageB = min(pageA + 1.0, dims.x);\n  vec2 xy = 0.5 + im.rg;\n  vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n  vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n  vec4 sLo = texture2D(cube, pLo * dims.zw);\n  vec4 sHi = texture2D(cube, pHi * dims.zw);\n  vec4 cubeOut = mix(sLo, sHi, im.b - flr);\n  if (d0 > d1) {\n    vec4 c = c0;\n    c.rgb *= dims.x;\n    float flr = floor(c.b);\n    float pageA = flr;\n    float pageB = min(pageA + 1.0, dims.x);\n    vec2 xy = 0.5 + c.rg;\n    vec2 pLo = xy + vec2(0.0, pageA * (dims.x + 1.0));\n    vec2 pHi = xy + vec2(0.0, pageB * (dims.x + 1.0));\n    vec4 sLo = texture2D(cube, pLo * dims.zw);\n    vec4 sHi = texture2D(cube, pHi * dims.zw);\n    c = mix(sLo, sHi, c.b - flr);\n    cubeOut.rgb = (((cubeOut.rgb - c.rgb) * d0) / d1) + c.rgb;\n  }\n  return vec4(cubeOut.rgb, im.a);\n}\n"
- "kernel vec4 _convertDepthOrDisparity(vec4 s) {\n  return vec4(1.0 / max(s.r, 1.000000e-06), s.gba);\n}\n"
- "kernel vec4 _convertRGBtoY(vec4 c) {\n  c = vec4(c.rgb / max(c.a, 1.000000e-05), c.a);\n  float Y = sqrt(max(dot(c.rgb, vec3(0.299, 0.587, 0.114)), 0.0));\n  c.rgb = vec3(Y);\n  return c;\n}\n"
- "kernel vec4 _disintegrateWithMask(vec4 t0, vec4 t1, vec4 m0, vec4 m1, vec4 m2, vec4 m3, vec4 param) {\n  float shadowRadiusInv = param.y;\n  float shadowDensity = param.z;\n  float time = param.w;\n  float ramp = 1.0 / (max(abs(m1.r - m0.r), abs(m2.r - m0.r)) + 1.000000e-03);\n  float shadow = (((time - m3.r) * shadowRadiusInv) * ramp) + time;\n  shadow = clamp(shadow, 0.0, 1.0);\n  shadow = (shadowDensity * (shadow - 1.0)) + 1.0;\n  t0.rgb = t0.rgb * ((param.x * time) + 1.0);\n  t1.rgb = (t1.rgb * (((param.x * time) + 1.0) - param.x)) * shadow;\n  float s = clamp(((time - m0.r) * ramp) + time, 0.0, 1.0);\n  return mix(t0, t1, s);\n}\n"
- "kernel vec4 _disintegrateWithMaskG(sampler s0, sampler s1, sampler m, vec2 offset, vec4 param) {\n  float shadowRadiusInv = param.y;\n  float shadowDensity = param.z;\n  float time = param.w;\n  vec4 t0 = sample(s0, samplerCoord(s0));\n  vec4 t1 = sample(s1, samplerCoord(s1));\n  vec2 d = destCoord();\n  vec4 m0 = sample(m, samplerTransform(m, d));\n  vec4 m1 = sample(m, samplerTransform(m, d + vec2(1.0, 0.0)));\n  vec4 m2 = sample(m, samplerTransform(m, d + vec2(0.0, 1.0)));\n  vec4 m3 = sample(m, samplerTransform(m, d - offset));\n  float ramp = 1.0 / (max(abs(m1.r - m0.r), abs(m2.r - m0.r)) + 1.000000e-03);\n  float shadow = (((time - m3.r) * shadowRadiusInv) * ramp) + time;\n  shadow = clamp(shadow, 0.0, 1.0);\n  shadow = (shadowDensity * (shadow - 1.0)) + 1.0;\n  t0.rgb = t0.rgb * ((param.x * time) + 1.0);\n  t1.rgb = (t1.rgb * (((param.x * time) + 1.0) - param.x)) * shadow;\n  float s = clamp(((time - m0.r) * ramp) + time, 0.0, 1.0);\n  return mix(t0, t1, s);\n}\n"
- "kernel vec4 _disparityRefinementPreprocessing(vec4 disparity, vec4 alpha, vec4 lm, vec4 config0, vec4 config1) {\n  float alpha_val = alpha.x;\n  float d = disparity.x;\n  float zeroShift = lm.x;\n  float d_factor = clamp(config0.x * exp((-pow(max(1.000000e-04, abs(d - zeroShift)), config0.y)) / config0.z), config0.w, config1.x);\n  if (alpha_val > config1.y) d -= (d - zeroShift) * d_factor;\n  return vec4(d, 0.0, 0.0, 1.0);\n}\n"
- "kernel vec4 _disparityRefinementPreprocessingPow2(vec4 disparity, vec4 alpha, vec4 lm, vec4 config0, vec4 config1) {\n  float alpha_val = alpha.x;\n  float d = disparity.x;\n  float zeroShift = lm.x;\n  float v = max(1.000000e-04, abs(d - zeroShift));\n  float d_factor = clamp(config0.x * exp((-(v * v)) / config0.z), config0.w, config1.x);\n  if (alpha_val > config1.y) d -= (d - zeroShift) * d_factor;\n  return vec4(d, 0.0, 0.0, 1.0);\n}\n"
- "kernel vec4 _divideBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 B = Cb / max(Cs, vec4(1.000000e-07));\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
- "kernel vec4 _drr_binarize(vec4 m) {\n  m.r = (m.r > 1.000000e-05) ? 1.0 : 0.0;\n  return m;\n}\n"
- "kernel vec4 _drr_binarize_alpha(vec4 c, vec4 m, float t) {\n  c *= (m.r > 1.000000e-03) ? 1.0 : 0.0;\n  c *= (min(1.0 - c.r, c.r) > t) ? 1.0 : 0.0;\n  return c;\n}\n"
- "kernel vec4 _drr_binarize_alpha_inv(vec4 c, vec4 m, float t) {\n  c *= (m.r > 1.000000e-03) ? 0.0 : 1.0;\n  c *= (min(1.0 - c.r, c.r) > t) ? 1.0 : 0.0;\n  return c;\n}\n"
- "kernel vec4 _drr_binarize_inv(vec4 m) {\n  m.r = (m.r > 1.000000e-05) ? 0.0 : 1.0;\n  return m;\n}\n"
- "kernel vec4 _drr_cdmeasure(vec4 a, vec4 aI) {\n  return 1.0 - (abs(a - aI) / max(a + aI, 1.000000e-04));\n}\n"
- "kernel vec4 _drr_chromaexc(vec4 outside, vec4 inside, float t2, float thresholdSclera, float thresholdScleraBrightness) {\n  vec3 diff = inside.rgb - outside.rgb;\n  float n = min(inside.r, outside.r);\n  float exc = (dot(diff, diff) < (t2 * n)) ? 0.0 : 1.0;\n  float redness = max(inside.r - min(inside.g, inside.b), 0.0) / max(1.000000e-05, inside.r);\n  exc *= ((inside.r > thresholdScleraBrightness) && (redness < thresholdSclera)) ? 0.0 : 1.0;\n  return vec4(exc, 0.0, 0.0, 1.0);\n}\n"
- "kernel vec4 _drr_rawred_large(vec4 c, float whiteness, float spectrum) {\n  if (c.r < 5.000000e-03) return vec4(0.0, 0.0, 0.0, 1.0);\n  float n = dot(c.rgb, vec3(1.0 / 3.0));\n  float rv = (((c.r - n) * (c.r - n)) + ((c.g - n) * (c.g - n))) + ((c.b - n) * (c.b - n));\n  rv /= max(1.000000e-04, n);\n  float rg = max(0.0, c.r - c.g) / max(1.000000e-05, c.r + c.g);\n  float rb = max(0.0, c.r - c.b) / max(1.000000e-05, c.r + c.b);\n  float rm = min(rg, rb);\n  float r = mix(1.0, rv, spectrum) * rm;\n  float w = c.r;\n  r = mix(r, w, whiteness);\n  return vec4(r, 0.0, 0.0, 1.0);\n}\n"
- "kernel vec4 _drr_rawred_sm(vec4 c, float whiteness, float spectrum) {\n  if (c.r < 5.000000e-03) return vec4(0.0, 0.0, 0.0, 1.0);\n  float n = dot(c.rgb, vec3(1.0 / 3.0));\n  float rv = (((c.r - n) * (c.r - n)) + ((c.g - n) * (c.g - n))) + ((c.b - n) * (c.b - n));\n  rv /= max(1.000000e-04, n);\n  float rg = max(0.0, c.r - c.g) / max(1.000000e-05, c.r + c.g);\n  float rb = max(0.0, c.r - c.b) / max(1.000000e-05, c.r + c.b);\n  float rm = min(rg, rb);\n  float r = rv * rm;\n  r *= 1.000000e+01;\n  r *= r;\n  float w = max(0.0, c.r - (whiteness * max(c.g, c.b)));\n  r = mix(r, w, spectrum);\n  return vec4(r, 0.0, 0.0, 1.0);\n}\n"
- "kernel vec4 _drr_repair(vec4 img, vec4 c, vec4 m, vec4 avg, vec4 noise, float brightness, float noiseAmount, float whiteCutoff, float chroma) {\n  float mixer = m.r;\n  vec3 Y = vec3(0.299, 0.587, 0.114);\n  float nn = noise.r;\n  avg.rgb += (2.0 * noiseAmount) * nn;\n  vec3 source = c.rgb;\n  c.rgb += noiseAmount * nn;\n  float rg = max(0.0, img.r - img.g) / max(1.000000e-04, img.r + img.g);\n  float rb = max(0.0, img.r - img.b) / max(1.000000e-04, img.r + img.b);\n  float redness = max(0.25, 0.5 * (rg + rb));\n  redness = smoothstep(1.000000e-01, 6.000000e-01, redness);\n  vec3 replacementRed = (0.5 * brightness) * vec3(min(c.b, c.g));\n  vec3 replacementWhite = (2.0 * brightness) * avg.rgb;\n  vec3 replacement = mix(replacementWhite, replacementRed, redness);\n  float Lrep = dot(replacement, Y);\n  float Lavg = dot(avg.rgb, Y);\n  replacement = mix(replacement, (avg.rgb * Lrep) * Lavg, chroma);\n  replacement = max(6.000000e-02 * avg.rgb, replacement);\n  float n = dot(img.rgb, Y);\n  float whiteness = smoothstep(1.000000e-02 + whiteCutoff, 1.010, n);\n  replacement.rgb = mix(replacement.rgb, vec3(n), whiteness);\n  mixer *= 1.0 - whiteness;\n  img.rgb = mix(img.rgb, replacement, mixer);\n  img.rgb = mix(source, img.rgb, m.r);\n  return img;\n}\n"
- "kernel vec4 _edgeWork(vec4 src, vec4 blurred) {\n  return vec4(clamp((src.r - blurred.r) * 1.000000e+03, 0.0, 1.0));\n}\n"
- "kernel vec4 _edgesPrep(vec4 s) {\n  s = vec4(s.rgb / max(s.a, 1.000000e-05), s.a);\n  s.rgb = sqrt(max(s.rgb, vec3(0.0)));\n  return s;\n}\n"
- "kernel vec4 _flexLumaScaling(vec4 im, vec2 headrooms, vec4 coefs, float coeffs4, sampler2D lut, vec2 dim) {\n  float imMax = max(im.r, max(im.g, im.b));\n  float Y = dot(coefs, vec4(im.rgb, imMax));\n  float signY = sign(Y);\n  Y = max(abs(Y), 1.000000e-06);\n  Y = clamp(Y, 0.0, 1.0);\n  float lutCoord = (Y * dim.x) + dim.y;\n  float gain = texture2D(lut, vec2(lutCoord, 0.5)).r;\n  float scale = (signY * gain) * coeffs4;\n  vec4 result = vec4(im.rgb * scale, im.a);\n  return result;\n}\n"
- "kernel vec4 _gradientRangeLimit(vec4 grad, float gxgyE0, float gxgyE1, float gygxE0, float gygxE1) {\n  vec2 G = grad.xy;\n  float Gy = abs(G.y);\n  float Gx = abs(G.x);\n  if ((Gy + Gx) < 1.000000e-03) return vec4(0);\n  if (Gx < Gy) {\n    float gxgy = G.x / G.y;\n    return grad * (1.0 - smoothstep(gxgyE0, gxgyE1, gxgy));\n  } else {\n    float gygx = G.y / G.x;\n    return grad * (1.0 - smoothstep(gygxE0, gygxE1, gygx));\n  }\n}\n"
- "kernel vec4 _grassAndSkyAdjust(vec4 im, vec2 params) {\n  float enhanceGrass = params.x;\n  float enhanceSky = params.y;\n  vec3 ipt, ipt2;\n  float range;\n  {\n    vec3 lms = ((im.r * vec3(3.347000e-01, 1.747000e-01, 1.870000e-02)) + (im.g * vec3(5.984000e-01, 7.151000e-01, 1.018000e-01))) + (im.b * vec3(6.710000e-02, 1.106000e-01, 8.794000e-01));\n    lms = sign(lms) * pow(abs(lms), vec3(4.300000e-01));\n    ipt = ((lms.r * vec3(4.000000e-01, 4.455, 8.056000e-01)) + (lms.g * vec3(4.000000e-01, -4.851, 3.572000e-01))) + (lms.b * vec3(2.000000e-01, 3.960000e-01, -1.1628));\n  }\n  float hue = (atan(sqrt((ipt.b * ipt.b) + (ipt.g * ipt.g)) - ipt.g, ipt.b) / 3.1416) + 0.5;\n  range = hue - 8.800000e-01;\n  float maskGrass = exp((((-1.0) * range) * range) / ((2.0 * 8.800000e-02) * 8.800000e-02));\n  range = 1.0 - smoothstep(4.000000e-01, 0.5, ipt.r);\n  maskGrass *= range;\n  vec2 idealGrass = vec2(-3.000000e-02, 1.000000e-01);\n  vec2 toIdeal = idealGrass - ipt.gb;\n  float dist = sqrt((toIdeal.r * toIdeal.r) + (toIdeal.g * toIdeal.g));\n  float chroma2 = 4.0 * ((ipt.g * ipt.g) + (ipt.b * ipt.b));\n  float str = enhanceGrass * pow(chroma2, 2.000000e-01);\n  str = str * min(1.0, 1.0 - (chroma2 * chroma2));\n  str = min(str, 1.500);\n  float scale = min(1.0, 1.000000e-01 / (dist + 5.000000e-02));\n  ipt2.gb = ipt.gb + ((str * toIdeal) * scale);\n  ipt2.gb *= enhanceGrass;\n  ipt2.r = ipt.r;\n  ipt = mix(ipt, ipt2.rgb, maskGrass);\n  float maskSky = smoothstep(2.000000e-01, 0.5, ipt.r);\n  range = ipt.g + 4.000000e-02;\n  maskSky *= exp((((-1.0) * range) * range) / ((2.0 * 1.500000e-01) * 1.500000e-01));\n  range = ipt.b + 1.000000e-01;\n  maskSky *= exp((((-1.0) * range) * range) / ((2.0 * 2.000000e-01) * 2.000000e-01));\n  {\n    vec3 lms = ((ipt.r * vec3(1.0, 1.0, 1.0)) + (ipt.g * vec3(9.760000e-02, -1.139000e-01, 3.260000e-02))) + (ipt.b * vec3(2.052000e-01, 1.332000e-01, -6.769000e-01));\n    lms = sign(lms) * pow(abs(lms), vec3(1.0 / 4.300000e-01));\n    im.rgb = ((lms.r * vec3(5.3089, -1.3026, 3.810000e-02)) + (lms.g * vec3(-4.4648, 2.5193, -1.968000e-01))) + (lms.b * vec3(1.564000e-01, -2.175000e-01, 1.159));\n  }\n  im.rgb = max(im.rgb, 0.0);\n  float gain = max(1.0, 1.0 + enhanceSky);\n  float gamma = 1.0 + abs(enhanceSky);\n  vec4 result = pow(gain * im, vec4(gamma));\n  float gray = ((result.r + result.b) + result.g) / 3.0;\n  result.rgb += ((result.rgb - gray) * abs(enhanceSky)) * 0.5;\n  result = mix(im, result, maskSky);\n  result.a = im.a;\n  return result;\n}\n"
- "kernel vec4 _headroomClamp(vec4 img, float targHR) {\n  float rgb_max = max(max(img.r, img.g), img.b);\n  return (rgb_max <= targHR) ? img : vec4((img.rgb * targHR) / rgb_max, img.a);\n}\n"
- "kernel vec4 _headroomToneMap(vec4 img, float srcHR, float targHR, float targRefWt, vec4 bezier) {\n  float rgb_max = max(max(img.r, img.g), img.b);\n  if (rgb_max <= 1.0) return vec4(targRefWt * img.rgb, img.a);\n  float a = bezier.x;\n  float b = bezier.y;\n  float c = bezier.z;\n  float d = bezier.w;\n  float t = (sqrt(max((a * rgb_max) + b, 0.0)) + c) / a;\n  float yB = ((d * t) * (t - 2.0)) + targRefWt;\n  float rgb_max_tmo = (rgb_max < srcHR) ? yB : targHR;\n  float maxRatio = min(rgb_max_tmo / rgb_max, 1.0);\n  return vec4(maxRatio * img.rgb, img.a);\n}\n"
- "kernel vec4 _highlightsAndShadows0(vec4 pix, vec4 blur, vec4 params) {\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(1.000000e-03, (pix.r + pix.g) + pix.b);\n  rgbFactor = clamp(rgbFactor, 0.0, 1.0);\n  float shadAmt = params.x * pow(rgbFactor, max(0.0, 1.0 - params.x));\n  vec3 clamped = clamp(pix.rgb, 1.000000e-05, 9.999900e-01);\n  float gray = ((clamped.r + clamped.g) + clamped.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  float rgbsat = max((clamped.r - gray) * gii, (gray - clamped.r) * gi);\n  float skin = min(1.0, ((max(0.0, min(clamped.r - clamped.g, (clamped.g * 2.0) - clamped.b)) * 4.0) * (1.0 - rgbsat)) * gi);\n  skin = 1.500000e-01 + (skin * 7.000000e-01);\n  vec3 rgbExp = pow(vec3(2.0), (-shadAmt) - blur.rgb);\n  float uniformExp = min(rgbExp.r, min(rgbExp.g, rgbExp.b));\n  vec3 shadExp = mix(rgbExp, vec3(uniformExp), skin);\n  float nopMix = params.z;\n  shadExp = mix(shadExp, vec3(1.0, 1.0, 1.0), nopMix);\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * 0.5, shadExp)) * 2.0;\n  float maxChan = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(maxChan);\n  float origPercent = sqrt(smoothstep(0.0, 1.000000e-01 + ((0.5 * shadAmt) * shadAmt), blurLum));\n  origPercent *= 1.0 - origPercent;\n  shad = mix(shad, pix.rgb, origPercent);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  origPercent = 1.0 - smoothstep(2.000000e-01, 8.000000e-01, blurLum);\n  high = mix(high, pix.rgb, origPercent);\n  vec4 result;\n  result.rgb = mix(shad, high, blurLum);\n  float Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  vec3 mid = mix(vec3(0.5), result.rgb, 1.0 + (abs(shadAmt) * 5.000000e-02));\n  result.rgb = mix(result.rgb, mid.rgb, min(effectAmount, (3.000000e+01 * blurLum) * blurLum));\n  result.a = pix.a;\n  return result;\n}\n"
- "kernel vec4 _highlightsAndShadows1(vec4 pix, vec4 blur, vec4 params) {\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(1.000000e-03, (pix.r + pix.g) + pix.b);\n  float shadAmt = params.x * pow(min(rgbFactor, 1.0), 1.0 - params.x);\n  vec3 shadExp = mix(pow(vec3(2.0), (-shadAmt) - blur.rgb), vec3(1.0), params.z);\n  float blurLum2 = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(blurLum2);\n  float kGain = 0.5 + (0.5 * smoothstep(0.5, 1.0, params.x));\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * kGain, shadExp)) * 2.0;\n  vec3 ycc = ((pix.r * vec3(0.299, 5.960000e-01, 2.120000e-01)) + (pix.g * vec3(0.587, -2.755000e-01, -5.230000e-01))) + (pix.b * vec3(0.114, -3.210000e-01, 3.110000e-01));\n  float Y = (sign(ycc.r) * pow(abs(ycc.r) * kGain, shadExp.r)) * 2.0;\n  vec3 shad2 = ((Y * vec3(1.00048, 9.998640e-01, 9.994460e-01)) + (ycc.g * vec3(9.555580e-01, -2.715450e-01, -1.10803))) + (ycc.b * vec3(6.195490e-01, -6.467860e-01, 1.70542));\n  shad = mix(shad, shad2, 3.500000e-01);\n  shad = mix(pix.rgb, shad, sqrt(smoothstep(0.0, 1.000000e-01 + shadAmt, sqrt(blurLum))));\n  shad = mix(shad, pix.rgb, blurLum);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  Y = dot(high, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float kHighMix = 1.0 + ((1.0 - min(1.0, params.y + 0.3)) * 4.000000e-01);\n  vec3 mid = mix(vec3(0.25), high, kHighMix);\n  float highBoost = min(effectAmount, 3.000000e+01 * blurLum2) * (1.0 - params.y);\n  high = mix(high, mid, highBoost);\n  high = mix(pix.rgb, high, smoothstep(2.000000e-01, 8.000000e-01, blurLum));\n  high = mix(pix.rgb, high, blurLum2);\n  vec4 result;\n  result.rgb = mix(shad, high, min(blurLum, 1.0));\n  Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float midAmt = (abs(shadAmt) * 1.000000e-01) * (1.0 - params.z);\n  mid = mix(vec3(0.5), result.rgb, 1.0 + midAmt);\n  result.rgb = mix(result.rgb, mid, min(effectAmount, 3.000000e+01 * blurLum2));\n  result.a = pix.a;\n  return result;\n}\n"
- "kernel vec4 _highlightsAndShadows2(vec4 pix, vec4 blur, vec4 params) {\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(1.000000e-03, (pix.r + pix.g) + pix.b);\n  float shadAmt = params.x * pow(min(rgbFactor, 1.0), 1.0 - params.x);\n  vec3 shadExp = mix(pow(vec3(2.0), (-shadAmt) - blur.rgb), vec3(1.0), params.z);\n  float blurLum2 = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(blurLum2);\n  float kGain = 0.5 + (0.5 * smoothstep(0.5, 1.0, params.x));\n  float newGain = shadAmt;\n  vec3 neg = min(pix.rgb, 0.0);\n  vec3 shad = ((1.0 + newGain) * pow(max(pix.rgb, 0.0) * kGain, shadExp)) * 2.0;\n  vec3 ycc = ((pix.r * vec3(0.299, 5.960000e-01, 2.120000e-01)) + (pix.g * vec3(0.587, -2.755000e-01, -5.230000e-01))) + (pix.b * vec3(0.114, -3.210000e-01, 3.110000e-01));\n  float Y = pow(max(ycc.r, 0.0) * kGain, shadExp.r) * 2.0;\n  vec3 shad2 = ((Y * vec3(1.00048, 9.998640e-01, 9.994460e-01)) + (ycc.g * vec3(9.555580e-01, -2.715450e-01, -1.10803))) + (ycc.b * vec3(6.195490e-01, -6.467860e-01, 1.70542));\n  shad = mix(shad, shad2, 3.500000e-01);\n  shad = mix(pix.rgb, shad, smoothstep(0.0, 1.000000e-01 + shadAmt, sqrt(blurLum)));\n  shad = mix(shad, pix.rgb, blurLum);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  Y = dot(high, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float kHighMix = 1.0 + ((1.0 - min(1.0, params.y + 0.3)) * 4.000000e-01);\n  vec3 mid = mix(vec3(0.25), high, kHighMix);\n  float highBoost = min(effectAmount, 3.000000e+01 * blurLum2) * (1.0 - params.y);\n  high = mix(high, mid, highBoost);\n  high = mix(pix.rgb, high, smoothstep(2.000000e-01, 8.000000e-01, blurLum));\n  high = mix(pix.rgb, high, blurLum2);\n  vec4 result;\n  result.rgb = mix(shad, high, min(blurLum, 1.0));\n  Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float midAmt = (abs(shadAmt) * 1.000000e-01) * (1.0 - params.z);\n  mid = mix(vec3(0.5), result.rgb, 1.0 + midAmt);\n  result.rgb = mix(result.rgb, mid, min(effectAmount, 3.000000e+01 * blurLum2));\n  result.rgb = max(result.rgb, 0.0) + neg;\n  result.a = pix.a;\n  return result;\n}\n"
- "kernel vec4 _highlightsAndShadows_noblur0(vec4 pix, vec4 params) {\n  vec4 blur = pix;\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(1.000000e-03, (pix.r + pix.g) + pix.b);\n  rgbFactor = clamp(rgbFactor, 0.0, 1.0);\n  float shadAmt = params.x * pow(rgbFactor, max(0.0, 1.0 - params.x));\n  vec3 clamped = clamp(pix.rgb, 1.000000e-05, 9.999900e-01);\n  float gray = ((clamped.r + clamped.g) + clamped.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  float rgbsat = max((clamped.r - gray) * gii, (gray - clamped.r) * gi);\n  float skin = min(1.0, ((max(0.0, min(clamped.r - clamped.g, (clamped.g * 2.0) - clamped.b)) * 4.0) * (1.0 - rgbsat)) * gi);\n  skin = 1.500000e-01 + (skin * 7.000000e-01);\n  vec3 rgbExp = pow(vec3(2.0), (-shadAmt) - blur.rgb);\n  float uniformExp = min(rgbExp.r, min(rgbExp.g, rgbExp.b));\n  vec3 shadExp = mix(rgbExp, vec3(uniformExp), skin);\n  float nopMix = params.z;\n  shadExp = mix(shadExp, vec3(1.0, 1.0, 1.0), nopMix);\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * 0.5, shadExp)) * 2.0;\n  float maxChan = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(maxChan);\n  float origPercent = sqrt(smoothstep(0.0, 1.000000e-01 + ((0.5 * shadAmt) * shadAmt), blurLum));\n  origPercent *= 1.0 - origPercent;\n  shad = mix(shad, pix.rgb, origPercent);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  origPercent = 1.0 - smoothstep(2.000000e-01, 8.000000e-01, blurLum);\n  high = mix(high, pix.rgb, origPercent);\n  vec4 result;\n  result.rgb = mix(shad, high, blurLum);\n  float Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  vec3 mid = mix(vec3(0.5), result.rgb, 1.0 + (abs(shadAmt) * 5.000000e-02));\n  result.rgb = mix(result.rgb, mid.rgb, min(effectAmount, (3.000000e+01 * blurLum) * blurLum));\n  result.a = pix.a;\n  return result;\n}\n"
- "kernel vec4 _highlightsAndShadows_noblur1(vec4 pix, vec4 params) {\n  vec4 blur = pix;\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(1.000000e-03, (pix.r + pix.g) + pix.b);\n  float shadAmt = params.x * pow(min(rgbFactor, 1.0), 1.0 - params.x);\n  vec3 shadExp = mix(pow(vec3(2.0), (-shadAmt) - blur.rgb), vec3(1.0), params.z);\n  float blurLum2 = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(blurLum2);\n  float kGain = 0.5 + (0.5 * smoothstep(0.5, 1.0, params.x));\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * kGain, shadExp)) * 2.0;\n  vec3 ycc = ((pix.r * vec3(0.299, 5.960000e-01, 2.120000e-01)) + (pix.g * vec3(0.587, -2.755000e-01, -5.230000e-01))) + (pix.b * vec3(0.114, -3.210000e-01, 3.110000e-01));\n  float Y = (sign(ycc.r) * pow(abs(ycc.r) * kGain, shadExp.r)) * 2.0;\n  vec3 shad2 = ((Y * vec3(1.00048, 9.998640e-01, 9.994460e-01)) + (ycc.g * vec3(9.555580e-01, -2.715450e-01, -1.10803))) + (ycc.b * vec3(6.195490e-01, -6.467860e-01, 1.70542));\n  shad = mix(shad, shad2, 3.500000e-01);\n  shad = mix(pix.rgb, shad, sqrt(smoothstep(0.0, 1.000000e-01 + shadAmt, sqrt(blurLum))));\n  shad = mix(shad, pix.rgb, blurLum);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  Y = dot(high, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float kHighMix = 1.0 + ((1.0 - min(1.0, params.y + 0.3)) * 4.000000e-01);\n  vec3 mid = mix(vec3(0.25), high, kHighMix);\n  float highBoost = min(effectAmount, 3.000000e+01 * blurLum2) * (1.0 - params.y);\n  high = mix(high, mid, highBoost);\n  high = mix(pix.rgb, high, smoothstep(2.000000e-01, 8.000000e-01, blurLum));\n  high = mix(pix.rgb, high, blurLum2);\n  vec4 result;\n  result.rgb = mix(shad, high, min(blurLum, 1.0));\n  Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float midAmt = (abs(shadAmt) * 1.000000e-01) * (1.0 - params.z);\n  mid = mix(vec3(0.5), result.rgb, 1.0 + midAmt);\n  result.rgb = mix(result.rgb, mid, min(effectAmount, 3.000000e+01 * blurLum2));\n  result.a = pix.a;\n  return result;\n}\n"
- "kernel vec4 _highlightsAndShadows_noblur2(vec4 pix, vec4 params) {\n  vec4 blur = pix;\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(1.000000e-03, (pix.r + pix.g) + pix.b);\n  float shadAmt = params.x * pow(min(rgbFactor, 1.0), 1.0 - params.x);\n  vec3 shadExp = mix(pow(vec3(2.0), (-shadAmt) - blur.rgb), vec3(1.0), params.z);\n  float blurLum2 = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(blurLum2);\n  float kGain = 0.5 + (0.5 * smoothstep(0.5, 1.0, params.x));\n  float newGain = shadAmt;\n  vec3 neg = min(pix.rgb, 0.0);\n  vec3 shad = ((1.0 + newGain) * pow(max(pix.rgb, 0.0) * kGain, shadExp)) * 2.0;\n  vec3 ycc = ((pix.r * vec3(0.299, 5.960000e-01, 2.120000e-01)) + (pix.g * vec3(0.587, -2.755000e-01, -5.230000e-01))) + (pix.b * vec3(0.114, -3.210000e-01, 3.110000e-01));\n  float Y = (sign(ycc.r) * pow(abs(ycc.r) * kGain, shadExp.r)) * 2.0;\n  vec3 shad2 = ((Y * vec3(1.00048, 9.998640e-01, 9.994460e-01)) + (ycc.g * vec3(9.555580e-01, -2.715450e-01, -1.10803))) + (ycc.b * vec3(6.195490e-01, -6.467860e-01, 1.70542));\n  shad = mix(shad, shad2, 3.500000e-01);\n  shad = mix(pix.rgb, shad, smoothstep(0.0, 1.000000e-01 + shadAmt, sqrt(blurLum)));\n  shad = mix(shad, pix.rgb, blurLum);\n  vec3 high = sign(pix.rgb) * pow(abs(pix.rgb) * params.w, vec3(2.0 - params.y));\n  Y = dot(high, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float kHighMix = 1.0 + ((1.0 - min(1.0, params.y + 0.3)) * 4.000000e-01);\n  vec3 mid = mix(vec3(0.25), high, kHighMix);\n  float highBoost = min(effectAmount, 3.000000e+01 * blurLum2) * (1.0 - params.y);\n  high = mix(high, mid, highBoost);\n  high = mix(pix.rgb, high, smoothstep(2.000000e-01, 8.000000e-01, blurLum));\n  high = mix(pix.rgb, high, blurLum2);\n  vec4 result;\n  result.rgb = mix(shad, high, min(blurLum, 1.0));\n  Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  float midAmt = (abs(shadAmt) * 1.000000e-01) * (1.0 - params.z);\n  mid = mix(vec3(0.5), result.rgb, 1.0 + midAmt);\n  result.rgb = mix(result.rgb, mid, min(effectAmount, 3.000000e+01 * blurLum2));\n  result.rgb = max(result.rgb, 0.0) + neg;\n  result.a = pix.a;\n  return result;\n}\n"
- "kernel vec4 _histogram_display(sampler image, float height, vec2 hilo) {\n  vec2 d = destCoord();\n  vec2 histcoord = vec2(floor(d.x) + 0.5, 0.5);\n  vec4 v = sample(image, samplerTransform(image, histcoord));\n  v = step(vec4(d.y), height * v);\n  float vi = ((v.r * 4.0) + (v.g * 2.0)) + v.b;\n  vec4 p = vec4(0.25, 0.25, 0.25, 1.0);\n  p = (vi == 4.0) ? vec4(0.5, 5.000000e-02, 5.000000e-02, 1.0) : p;\n  p = (vi == 6.0) ? vec4(2.000000e-01, 4.000000e-01, 5.000000e-02, 1.0) : p;\n  p = (vi == 2.0) ? vec4(5.000000e-02, 0.5, 5.000000e-02, 1.0) : p;\n  p = (vi == 3.0) ? vec4(5.000000e-02, 2.000000e-01, 4.000000e-01, 1.0) : p;\n  p = (vi == 1.0) ? vec4(5.000000e-02, 5.000000e-02, 0.5, 1.0) : p;\n  p = (vi == 5.0) ? vec4(2.000000e-01, 5.000000e-02, 4.000000e-01, 1.0) : p;\n  p = (vi == 7.0) ? vec4(5.000000e-02, 1.000000e-01, 0.3, 1.0) : p;\n  p.rgb = (d.x < (hilo.x + 0.5)) ? (p.rgb * vec3(4.000000e-01)) : p.rgb;\n  p.rgb = (d.x >= (hilo.y + 0.5)) ? ((p.rgb * vec3(6.000000e-01)) + vec3(4.000000e-01)) : p.rgb;\n  return p;\n}\n"
- "kernel vec4 _hlg_lumscale(vec4 im, vec4 lc, vec2 gg) {\n  float gamma = gg.x;\n  float gain = gg.y;\n  float rgbMax = max(max(im.r, im.g), im.b);\n  float Y = dot(vec4(im.rgb, rgbMax), lc);\n  Y = max(abs(Y), 1.000000e-04);\n  im.rgb *= (sign(Y) * gain) * pow(Y, gamma);\n  return im;\n}\n"
- "kernel vec4 _holeFillRefine(sampler image, float maxDist) {\n  vec2 dc = destCoord();\n  vec4 sO = sample(image, samplerTransform(image, dc));\n  if (sO.r <= 1.000000e-03) return sO;\n  if (sO.r > 9.500000e-01) return vec4(sO.r, 1, 0, 1);\n  float R = sO.r * maxDist;\n  float dTheta = clamp(1.0 / (R + 2.200000e-01), 1.000000e-01, 7.500000e-01);\n  for (float t = 0.0; t < 3.141593e+00; t += dTheta) {\n    vec2 d = R * vec2(cos(t), sin(t));\n    vec4 s = sample(image, samplerTransform(image, dc + d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n    s = sample(image, samplerTransform(image, dc - d));\n    if (s.g > 0.5) return vec4(sO.r, 1, 0, 1);\n  }\n  return sO;\n}\n"
- "kernel vec4 _hueBlendMode_v0(vec4 pCf, vec4 pCb) {\n  vec4 uCf = unpremultiply(pCf);\n  vec4 uCb = unpremultiply(pCb);\n  vec4 uCfSort = (uCf.r > uCf.g) ? uCf : uCf.grba;\n  uCfSort = (uCfSort.g > uCfSort.b) ? uCfSort : uCfSort.rbga;\n  uCfSort = (uCfSort.r > uCfSort.g) ? uCfSort : uCfSort.grba;\n  vec4 uCbSort = (uCb.r > uCb.g) ? uCb : uCb.grba;\n  uCbSort = (uCbSort.g > uCbSort.b) ? uCbSort : uCbSort.rbga;\n  uCbSort = (uCbSort.r > uCbSort.g) ? uCbSort : uCbSort.grba;\n  vec4 Ct = ((uCfSort.b + 1.000000e-05) > uCfSort.r) ? uCbSort.rbba : ((((uCf - uCfSort.b) * (uCbSort.r - uCbSort.b)) / (uCfSort.r - uCfSort.b)) + uCbSort.b);\n  Ct.a = uCb.a;\n  vec4 Cb = vec4(uCb.rgb * uCb.a, uCb.a);\n  Ct = mix(uCf, Ct, uCb.a);\n  Ct.a = 1.0;\n  return mix(Cb, Ct, uCf.a);\n}\n"
- "kernel vec4 _jointBilateral(sampler small, sampler guide, vec4 parms) {\n  vec2 dc = destCoord();\n  vec2 smallCenter = samplerCoord(small);\n  vec2 guideCenter = samplerCoord(guide);\n  vec2 smallDelta = samplerTransform(small, dc + vec2(1.0)) - smallCenter;\n  vec2 guideDelta = samplerTransform(guide, dc + vec2(1.0)) - guideCenter;\n  vec4 I0 = sample(small, smallCenter);\n  float IE0 = sample(guide, guideCenter).r;\n  vec4 sumFGI = vec4(0.0);\n  float sumFG = 0.0;\n  float x, y;\n  float w = 2.0;\n  for (x = -w; x <= w; x++) {\n    for (y = -w; y <= w; y++) {\n      vec2 xy = vec2(x, y) * parms.zw;\n      float G = exp((-((x * x) + (y * y))) * parms.y);\n      vec4 I = sample(small, smallCenter + (xy * smallDelta));\n      float IE = sample(guide, guideCenter + (xy * guideDelta)).g;\n      float F = exp((-((IE - IE0) * (IE - IE0))) * parms.x);\n      sumFG += F * G;\n      sumFGI += (F * G) * I;\n    }\n  }\n  return (sumFG < 1.000000e-03) ? I0 : (sumFGI / sumFG);\n}\n"
- "kernel vec4 _jointBilateralRG(sampler combo, vec4 parms) {\n  vec2 dc = destCoord();\n  vec2 comboCenter = samplerCoord(combo);\n  vec2 comboDelta = samplerTransform(combo, dc + vec2(1.0)) - comboCenter;\n  vec4 c = sample(combo, comboCenter);\n  vec2 I0 = c.zw;\n  float IE0 = c.r;\n  vec2 sumFGI = vec2(0.0);\n  float sumFG = 0.0;\n  float x, y;\n  float w = 2.0;\n  for (x = -w; x <= w; x++) {\n    for (y = -w; y <= w; y++) {\n      vec2 xy = vec2(x, y) * parms.zw;\n      float G = exp((-((x * x) + (y * y))) * parms.y);\n      vec4 c = sample(combo, comboCenter + (xy * comboDelta));\n      vec2 I = c.zw;\n      float IE = c.g;\n      float F = exp((-((IE - IE0) * (IE - IE0))) * parms.x);\n      sumFG += F * G;\n      sumFGI += (F * G) * I;\n    }\n  }\n  return vec4((sumFG < 1.000000e-03) ? I0 : (sumFGI / sumFG), 0.0, 1.0);\n}\n"
- "kernel vec4 _linearToAppleLog(vec4 R) {\n  const float R0 = -5.641088e-02;\n  const float Rt = 1.000000e-02;\n  const float c = 4.728711e+01;\n  const float beta = 9.640520e-03;\n  const float gamma = 8.550479e-02;\n  const float delta = 6.933694e-01;\n  vec4 Pa = (gamma * log2(R + beta)) + delta;\n  vec4 Pb = (c * (R - R0)) * (R - R0);\n}\n"
- "kernel vec4 _luminosityBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  float Ls = ((0.3 * Cs.r) + (0.59 * Cs.g)) + (0.11 * Cs.b);\n  float Lb = ((0.3 * Cb.r) + (0.59 * Cb.g)) + (0.11 * Cb.b);\n  vec4 BB = Cb + vec4(Ls - Lb);\n  float l = ((0.3 * BB.r) + (0.59 * BB.g)) + (0.11 * BB.b);\n  float n = min(min(BB.r, BB.g), BB.b);\n  float x = max(max(BB.r, BB.g), BB.b);\n  vec4 B = BB;\n  B = (n < 0.0) ? (vec4(l) + (((B - vec4(l)) * l) / (l - n))) : B;\n  B = (x > 1.0) ? (vec4(l) + (((B - vec4(l)) * (1.0 - l)) / (x - l))) : B;\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return (fore.a < 1.000000e-06) ? back : (((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a));\n}\n"
- "kernel vec4 _luminosityBlendMode_v0(vec4 pCf, vec4 pCb) {\n  vec4 uCf = unpremultiply(pCf);\n  vec4 uCb = unpremultiply(pCb);\n  vec4 uCbSort = (uCb.r > uCb.g) ? uCb : uCb.grba;\n  uCbSort = (uCbSort.g > uCbSort.b) ? uCbSort : uCbSort.rbga;\n  uCbSort = (uCbSort.r > uCbSort.g) ? uCbSort : uCbSort.grba;\n  float fL = (uCbSort.r + uCbSort.b) * 0.5;\n  float cmax = uCbSort.r;\n  float cmin = uCbSort.b;\n  vec4 uCfSort = (uCf.r > uCf.g) ? uCf : uCf.grba;\n  uCfSort = (uCfSort.g > uCfSort.b) ? uCfSort : uCfSort.rbga;\n  uCfSort = (uCfSort.r > uCfSort.g) ? uCfSort : uCfSort.grba;\n  float bL = (uCfSort.r + uCfSort.b) * 0.5;\n  float d = cmax - cmin;\n  float dv = (fL < 0.5) ? (cmax + cmin) : (2.0 - (cmax + cmin));\n  float s = d / max(dv, 1.000000e-06);\n  float mmax = (bL <= 0.5) ? (bL + (bL * s)) : ((bL + s) - (bL * s));\n  float mmin = (bL * 2.0) - mmax;\n  vec4 Ct = (((uCb - uCbSort.b) * (mmax - mmin)) / (uCbSort.r - uCbSort.b)) + mmin;\n  Ct = ((mmin + 1.000000e-05) > mmax) ? vec4(mmin) : Ct;\n  Ct.a = uCf.a;\n  vec4 Cf = vec4(uCf.rgb * uCf.a, uCf.a);\n  Ct = mix(uCb, Ct, uCf.a);\n  Ct.a = 1.0;\n  return mix(Cf, Ct, uCb.a);\n}\n"
- "kernel vec4 _maskBoundsInit(vec4 c, vec2 invSize) {\n  float eps = 1.250000e-01;\n  vec2 dcLo = floor(destCoord()) - eps;\n  vec2 dcHi = (dcLo + 1.0) + (eps * 2.0);\n  if (c.r > 1.000000e-05) return vec4(dcLo * invSize, dcHi * invSize);\n  return vec4(0, 0, 0, 0);\n}\n"
- "kernel vec4 _maxGradOnly(sampler i) {\n  vec4 nonEdge = vec4(0.0, 0.0, 0.0, 1.0);\n  vec2 dc = destCoord();\n  vec4 s = sample(i, samplerCoord(i));\n  if (s.b < 1.000000e-04) return nonEdge;\n  vec2 delta = normalize(s.rg);\n  vec4 sA = sample(i, samplerTransform(i, dc + delta));\n  vec4 sB = sample(i, samplerTransform(i, dc - delta));\n  if ((s.b > sA.b) && (s.b > sB.b)) return s;\n  return nonEdge;\n}\n"
- "kernel vec4 _mesh1(vec4 pt1, float width, vec4 color, float opacity) {\n  float hw, dist, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist = compare((v.x * s.x) + (v.y * s.y), length(v), dist);\n  w = p - p2;\n  dist = compare((w.x * s.x) + (w.y * s.y), dist, length(w));\n  interpolant = clamp(hw - dist, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist - (hw - 1.0)), color, compare(vec4(dist - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
- "kernel vec4 _mesh16(vec4 pt1, vec4 pt2, vec4 pt3, vec4 pt4, vec4 pt5, vec4 pt6, vec4 pt7, vec4 pt8, vec4 pt9, vec4 pt10, vec4 pt11, vec4 pt12, vec4 pt13, vec4 pt14, vec4 pt15, vec4 pt16, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt3.rg;\n  p2 = pt3.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt4.rg;\n  p2 = pt4.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt5.rg;\n  p2 = pt5.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt6.rg;\n  p2 = pt6.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt7.rg;\n  p2 = pt7.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt8.rg;\n  p2 = pt8.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt9.rg;\n  p2 = pt9.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt10.rg;\n  p2 = pt10.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt11.rg;\n  p2 = pt11.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt12.rg;\n  p2 = pt12.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt13.rg;\n  p2 = pt13.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt14.rg;\n  p2 = pt14.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt15.rg;\n  p2 = pt15.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt16.rg;\n  p2 = pt16.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
- "kernel vec4 _mesh2(vec4 pt1, vec4 pt2, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
- "kernel vec4 _mesh32(vec4 pt1, vec4 pt2, vec4 pt3, vec4 pt4, vec4 pt5, vec4 pt6, vec4 pt7, vec4 pt8, vec4 pt9, vec4 pt10, vec4 pt11, vec4 pt12, vec4 pt13, vec4 pt14, vec4 pt15, vec4 pt16, vec4 pt17, vec4 pt18, vec4 pt19, vec4 pt20, vec4 pt21, vec4 pt22, vec4 pt23, vec4 pt24, vec4 pt25, vec4 pt26, vec4 pt27, vec4 pt28, vec4 pt29, vec4 pt30, vec4 pt31, vec4 pt32, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt3.rg;\n  p2 = pt3.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt4.rg;\n  p2 = pt4.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt5.rg;\n  p2 = pt5.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt6.rg;\n  p2 = pt6.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt7.rg;\n  p2 = pt7.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt8.rg;\n  p2 = pt8.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt9.rg;\n  p2 = pt9.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt10.rg;\n  p2 = pt10.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt11.rg;\n  p2 = pt11.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt12.rg;\n  p2 = pt12.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt13.rg;\n  p2 = pt13.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt14.rg;\n  p2 = pt14.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt15.rg;\n  p2 = pt15.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt16.rg;\n  p2 = pt16.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt17.rg;\n  p2 = pt17.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt18.rg;\n  p2 = pt18.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt19.rg;\n  p2 = pt19.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt20.rg;\n  p2 = pt20.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt21.rg;\n  p2 = pt21.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt22.rg;\n  p2 = pt22.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt23.rg;\n  p2 = pt23.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt24.rg;\n  p2 = pt24.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt25.rg;\n  p2 = pt25.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt26.rg;\n  p2 = pt26.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt27.rg;\n  p2 = pt27.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt28.rg;\n  p2 = pt28.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt29.rg;\n  p2 = pt29.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt30.rg;\n  p2 = pt30.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt31.rg;\n  p2 = pt31.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt32.rg;\n  p2 = pt32.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
- "kernel vec4 _mesh4(vec4 pt1, vec4 pt2, vec4 pt3, vec4 pt4, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt3.rg;\n  p2 = pt3.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt4.rg;\n  p2 = pt4.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
- "kernel vec4 _mesh8(vec4 pt1, vec4 pt2, vec4 pt3, vec4 pt4, vec4 pt5, vec4 pt6, vec4 pt7, vec4 pt8, float width, vec4 color, float opacity) {\n  float hw, dist1, dist2, interpolant;\n  vec2 p1, p2, p, v, w, s;\n  hw = width * 0.5;\n  p = destCoord();\n  p1 = pt1.rg;\n  p2 = pt1.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist1 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist1 = compare((v.x * s.x) + (v.y * s.y), length(v), dist1);\n  w = p - p2;\n  dist1 = compare((w.x * s.x) + (w.y * s.y), dist1, length(w));\n  p1 = pt2.rg;\n  p2 = pt2.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt3.rg;\n  p2 = pt3.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt4.rg;\n  p2 = pt4.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt5.rg;\n  p2 = pt5.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt6.rg;\n  p2 = pt6.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt7.rg;\n  p2 = pt7.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  p1 = pt8.rg;\n  p2 = pt8.ba;\n  v = p - p1;\n  s = p2 - p1;\n  dist2 = abs(((v.x * s.y) - (v.y * s.x)) / max(length(s), 1.000000e-02));\n  dist2 = compare((v.x * s.x) + (v.y * s.y), length(v), dist2);\n  w = p - p2;\n  dist2 = compare((w.x * s.x) + (w.y * s.y), dist2, length(w));\n  dist1 = min(dist1, dist2);\n  interpolant = clamp(hw - dist1, 0.0, 1.0);\n  interpolant = ((3.0 - (2.0 * interpolant)) * interpolant) * interpolant;\n  return compare(vec4(dist1 - (hw - 1.0)), color, compare(vec4(dist1 - hw), color * interpolant, vec4(0.0))) * opacity;\n}\n"
- "kernel vec4 _minMaxNormalize(vec4 c, vec4 minc, vec4 maxc) {\n  c.rgb = (c.rgb - minc.rgb) / max(maxc.rgb - minc.rgb, 1.000000e-05);\n  return c;\n}\n"
- "kernel vec4 _minMaxRedNormalize(vec4 c, vec4 minmaxc) {\n  c.r = (c.r - minmaxc.r) / max(minmaxc.g - minmaxc.r, 1.000000e-05);\n  return c;\n}\n"
- "kernel vec4 _pageCurlTransNoEmap(sampler front, sampler back, vec4 cyl, vec2 cyloff, vec4 fbrot, vec2 fboff, vec4 hi, vec2 hioff, float radius) {\n  vec2 backPt;\n  vec2 d = destCoord();\n  vec2 frontPt = backPt = vec2(dot(d, cyl.xy), dot(d, cyl.zw)) + cyloff;\n  float f = frontPt.x;\n  float asn = sqrt(1.0 - pow(frontPt.x, 1.500)) - 1.0;\n  float v = frontPt.x + ((asn * asn) * 5.625000e-01);\n  frontPt.x = v;\n  backPt.x = 3.141593e+00 - v;\n  frontPt = vec2(dot(frontPt, fbrot.xy), dot(frontPt, fbrot.zw)) + fboff;\n  backPt = vec2(dot(backPt, fbrot.xy), dot(backPt, fbrot.zw)) + fboff;\n  frontPt = (f <= 0.0) ? d : frontPt;\n  vec2 highPt = vec2(dot(d, hi.xy), dot(d, hi.zw)) + hioff;\n  backPt = (f <= 0.0) ? highPt : backPt;\n  vec4 fs = sample(front, samplerTransform(front, frontPt));\n  vec4 bs = sample(back, samplerTransform(back, backPt));\n  vec4 pix = bs + ((1.0 - bs.a) * fs);\n  pix *= clamp((1.0 - f) * radius, 0.0, 1.0);\n  return pix;\n}\n"
- "kernel vec4 _pageCurlTransition(sampler front, sampler back, sampler emap, vec4 cyl, vec2 cyloff, vec4 fbrot, vec2 fboff, vec4 hi, vec2 hioff, float radius, vec4 emapExtent) {\n  vec2 backPt;\n  vec2 d = destCoord();\n  vec2 frontPt = backPt = vec2(dot(d, cyl.xy), dot(d, cyl.zw)) + cyloff;\n  float f = frontPt.x;\n  float asn = sqrt(1.0 - pow(frontPt.x, 1.500)) - 1.0;\n  float v = frontPt.x + ((asn * asn) * 5.625000e-01);\n  frontPt.x = v;\n  backPt.x = 3.141593e+00 - v;\n  frontPt = vec2(dot(frontPt, fbrot.xy), dot(frontPt, fbrot.zw)) + fboff;\n  backPt = vec2(dot(backPt, fbrot.xy), dot(backPt, fbrot.zw)) + fboff;\n  frontPt = (f <= 0.0) ? d : frontPt;\n  vec2 highPt = vec2(dot(d, hi.xy), dot(d, hi.zw)) + hioff;\n  backPt = (f <= 0.0) ? highPt : backPt;\n  vec4 fs = sample(front, samplerTransform(front, frontPt));\n  vec4 bs = sample(back, samplerTransform(back, backPt));\n  vec2 n = clamp((f * radius) * cyl.xy, -1.0, 1.0);\n  vec2 bn0 = (f < 0.0) ? vec2(0.0) : n;\n  bn0 = (bn0 * 0.5) + 0.5;\n  bn0 = (bn0 * emapExtent.zw) + emapExtent.xy;\n  vec4 es = sample(emap, samplerTransform(emap, bn0));\n  es *= bs.a;\n  bs = es + ((1.0 - es.a) * bs);\n  vec4 pix = bs + ((1.0 - bs.a) * fs);\n  pix *= clamp((1.0 - f) * radius, 0.0, 1.0);\n  return pix;\n}\n"
- "kernel vec4 _perc_norm_red(vec4 c, vec4 minmax) {\n  c.r = max((c.r - minmax.r) / max(minmax.g - minmax.r, 1.000000e-05), 0.0);\n  return c;\n}\n"
- "kernel vec4 _perspectiveMask(vec4 p, vec3 A3) {\n  return p * ((dot(vec3(destCoord(), 1.0), A3) < 1.000000e-06) ? 0.0 : 1.0);\n}\n"
- "kernel vec4 _redThreshold(vec4 c) {\n  return (c.r > 1.000000e-05) ? vec4(1, 0, 0, 1) : vec4(0, 0, 0, 1);\n}\n"
- "kernel vec4 _roundedrect(vec4 bounds, float radius, vec4 color) {\n  vec2 p = destCoord();\n  vec2 lo = bounds.xy;\n  vec2 hi = bounds.zw;\n  p = max(min(p - (lo + radius), 0.0), p - (hi - radius));\n  return color * clamp((radius - length(p)) + 0.5, 0.0, 1.0);\n}\n"
- "kernel vec4 _roundedstroke(vec4 bounds, float radius, float width, vec4 color) {\n  float k0, k1;\n  vec2 dc = destCoord();\n  vec2 lo = bounds.xy + radius;\n  vec2 hi = bounds.zw - radius;\n  vec2 p = max(min(dc - lo, 0.0), dc - hi);\n  k0 = (radius - length(p)) + 0.5;\n  k0 = clamp(k0, 0.0, 1.0);\n  radius = max(0.5, radius - width);\n  lo = (bounds.xy + radius) + width;\n  hi = (bounds.zw - radius) - width;\n  p = max(min(dc - lo, 0.0), dc - hi);\n  k1 = (radius - length(p)) + 0.5;\n  k1 = clamp(k1, 0.0, 1.0);\n  return (color * k0) * (1.0 - k1);\n}\n"
- "kernel vec4 _saturationBlendMode_v0(vec4 pCf, vec4 pCb) {\n  vec4 uCf = unpremultiply(pCf);\n  vec4 uCb = unpremultiply(pCb);\n  vec4 uCfSort = (uCf.r > uCf.g) ? uCf : uCf.grba;\n  uCfSort = (uCfSort.g > uCfSort.b) ? uCfSort : uCfSort.rbga;\n  uCfSort = (uCfSort.r > uCfSort.g) ? uCfSort : uCfSort.grba;\n  float fL = (uCfSort.r + uCfSort.b) * 0.5;\n  float cmax = uCfSort.r;\n  float cmin = uCfSort.b;\n  vec4 uCbSort = (uCb.r > uCb.g) ? uCb : uCb.grba;\n  uCbSort = (uCbSort.g > uCbSort.b) ? uCbSort : uCbSort.rbga;\n  uCbSort = (uCbSort.r > uCbSort.g) ? uCbSort : uCbSort.grba;\n  float bL = (uCbSort.r + uCbSort.b) * 0.5;\n  float d = cmax - cmin;\n  float dv = (fL < 0.5) ? (cmax + cmin) : (2.0 - (cmax + cmin));\n  float s = d / max(dv, 1.000000e-06);\n  float mmax = (bL <= 0.5) ? (bL + (bL * s)) : ((bL + s) - (bL * s));\n  float mmin = (bL * 2.0) - mmax;\n  vec4 Ct = ((uCbSort.b + 1.000000e-05) > uCbSort.r) ? vec4(mmax, mmin, mmin, 1.0) : ((((uCb - uCbSort.b) * (mmax - mmin)) / (uCbSort.r - uCbSort.b)) + mmin);\n  Ct.a = uCb.a;\n  vec4 Cb = vec4(uCb.rgb * uCb.a, uCb.a);\n  Ct = mix(uCf, Ct, uCb.a);\n  Ct.a = 1.0;\n  return mix(Cb, Ct, uCf.a);\n}\n"
- "kernel vec4 _sepia(vec4 s, float amount) {\n  vec4 color = vec4(1.0, 9.900000e-01, 9.200000e-01, 1.0);\n  vec4 c0 = vec4(8.956630e-04, -1.104567e-03, -6.082700e-04, 3.277428e-02);\n  vec4 c1 = vec4(3.116672e+00, 7.926372e-01, 3.219686e-02, 1.411847e+00);\n  vec4 c2 = vec4(-5.093341e+01, 4.654831e-01, 1.027555e+00, -9.069088e-01);\n  vec4 c3 = vec4(7.087939e+02, -3.903106e-01, -5.854013e-02, 6.621023e-01);\n  vec4 c4 = vec4(-3.605984e+03, 1.323156e-01, 0.0, -1.991615e-01);\n  float l = dot(s.rgb, vec3(2.125000e-01, 7.154000e-01, 7.210000e-02));\n  float la = l / max(1.000000e-04, s.a);\n  vec4 t = (c0 * s.a) + ((c1 + ((c2 + ((c3 + (c4 * la)) * la)) * la)) * l);\n  t.r = (l < (8.500000e-02 * s.a)) ? t.r : t.a;\n  vec3 r = (((l * l) - l) < 0.0) ? t.rgb : vec3(l, l, l);\n  return mix(s, vec4(r, s.a) * color, amount);\n}\n"
- "kernel vec4 _shadowKernel(vec4 im, vec4 adj, float str) {\n  adj.r = (3.400 * adj.r) - 1.200;\n  vec3 neg = min(im.rgb, 0.0);\n  vec3 pos = max(im.rgb, 1.0) - 1.0;\n  im.rgb = clamp(im.rgb, 0.0, 1.0);\n  float y = sqrt(dot(im.rgb, vec3(3.333300e-01)));\n  float s = mix(0.0, adj.r, str);\n  vec3 gain = (s > 0.0) ? vec3(0.0 * s) : vec3(((-2.750) * s) * s, ((-2.750) * s) * s, ((-2.500) * s) * s);\n  im.rgb = ((im.rgb * im.rgb) * gain) + (im.rgb * (1.0 - gain));\n  float m = 1.0 + ((1.850 * s) * max(1.000000e-01 - y, 0.0));\n  im.rgb = clamp(m * im.rgb, 0.0, 1.0);\n  float midAmt = (s < 0.0) ? min(s * s, 1.0) : 0.0;\n  y = y * (1.0 - y);\n  im.rgb = sqrt(im.rgb);\n  float pivot = 4.000000e-01;\n  float a = midAmt * y;\n  float b = (-pivot) * a;\n  vec3 pix = ((((im.r * vec3(0.299 * a)) + (im.g * vec3(0.587 * a))) + (im.b * vec3(0.114 * a))) + im.rgb) + vec3(b);\n  im.rgb = mix(im.rgb, vec3(pivot), (-y) * midAmt);\n  im.rgb = mix(im.rgb, pix, 8.000000e-01);\n  im.rgb = max(im.rgb, 0.0);\n  im.rgb *= im.rgb;\n  im.rgb = (clamp(im.rgb, 0.0, 1.0) + pos) + neg;\n  return im;\n}\n"
- "kernel vec4 _shadows_noblur(vec4 pix, vec4 params) {\n  vec4 blur = pix;\n  float rgbFactor = dot(vec3(1.0, 8.000000e-01, 1.100), max(pix.rgb, 0.0)) / max(1.000000e-03, (pix.r + pix.g) + pix.b);\n  rgbFactor = clamp(rgbFactor, 0.0, 1.0);\n  float shadAmt = params.x * pow(rgbFactor, max(0.0, 1.0 - params.x));\n  vec3 clamped = clamp(pix.rgb, 1.000000e-05, 9.999900e-01);\n  float gray = ((clamped.r + clamped.g) + clamped.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  float rgbsat = max((clamped.r - gray) * gii, (gray - clamped.r) * gi);\n  float skin = min(1.0, ((max(0.0, min(clamped.r - clamped.g, (clamped.g * 2.0) - clamped.b)) * 4.0) * (1.0 - rgbsat)) * gi);\n  skin = 1.500000e-01 + (skin * 7.000000e-01);\n  vec3 rgbExp = pow(vec3(2.0), (-shadAmt) - blur.rgb);\n  float uniformExp = min(rgbExp.r, min(rgbExp.g, rgbExp.b));\n  vec3 shadExp = mix(rgbExp, vec3(uniformExp), skin);\n  float nopMix = params.z;\n  shadExp = mix(shadExp, vec3(1.0, 1.0, 1.0), nopMix);\n  vec3 shad = (sign(pix.rgb) * pow(abs(pix.rgb) * 0.5, shadExp)) * 2.0;\n  float maxChan = max(0.0, max(max(blur.r, blur.g), blur.b));\n  float blurLum = sqrt(maxChan);\n  float origPercent = sqrt(smoothstep(0.0, 1.000000e-01 + ((0.5 * shadAmt) * shadAmt), blurLum));\n  origPercent *= 1.0 - origPercent;\n  shad = mix(shad, pix.rgb, origPercent);\n  vec4 result;\n  result.rgb = mix(shad, pix.rgb, blurLum);\n  float Y = dot(result.rgb, vec3(0.299, 0.587, 0.114));\n  float effectAmount = max(max(((((-2.600) * Y) * Y) - (2.600 * Y)) + 9.800000e-01, ((((-6.250) * Y) * Y) - (6.250 * Y)) + 5.965000e-01), 1.0);\n  vec3 mid = mix(vec3(0.5), result.rgb, 1.0 + (abs(shadAmt) * 5.000000e-02));\n  result.rgb = mix(result.rgb, mid.rgb, min(effectAmount, (3.000000e+01 * blurLum) * blurLum));\n  result.a = pix.a;\n  return result;\n}\n"
- "kernel vec4 _sharpenCombineEdges(vec4 orig, vec4 blurs, vec3 sharps, vec4 edges) {\n  vec4 so = vec4(orig.rgb / max(orig.a, 1.000000e-05), orig.a);\n  float Y = blurs.r + dot(blurs.r - blurs.gba, sharps);\n  so.rgb = ((vec3(Y * Y) + (so.r * vec3(7.014280e-01, -2.992760e-01, -2.977560e-01))) + (so.g * vec3(-5.881610e-01, 4.133170e-01, -5.857185e-01))) + (so.b * vec3(-1.137450e-01, -1.139050e-01, 8.840270e-01));\n  float alpha = edges.x;\n  so = vec4(so.rgb * so.a, so.a);\n  return mix(orig, so, alpha);\n}\n"
- "kernel vec4 _smartBlackAndWhite(vec4 image, sampler2D hueImage, vec4 rgbWeights, vec4 normalizer) {\n  float scaleFactor = rgbWeights.w;\n  float neutralGamma = normalizer.z;\n  float phototone = normalizer.w;\n  image = clamp(image, 0.0, 1.0);\n  vec3 lms;\n  lms.x = dot(image.rgb, vec3(3.139902e-01, 6.395130e-01, 4.649755e-02));\n  lms.y = dot(image.rgb, vec3(1.553724e-01, 7.578945e-01, 8.670142e-02));\n  lms.z = dot(image.rgb, vec3(1.775239e-02, 1.094421e-01, 8.725692e-01));\n  lms = pow(lms, vec3(4.300000e-01));\n  float i = dot(lms, vec3(4.000000e-01, 4.000000e-01, 2.000000e-01));\n  float p = dot(lms, vec3(4.455, -4.851, 3.960000e-01));\n  float t = dot(lms, vec3(8.056000e-01, 3.572000e-01, -1.1628));\n  float chroma = sqrt((p * p) + (t * t));\n  float hue = 0.5 + (atan(t, p) / 6.283185e+00);\n  vec2 huePt = vec2((hue * normalizer.x) + normalizer.y, 0.5);\n  float exponent = scaleFactor * texture2D(hueImage, huePt).a;\n  float cd = 6.000000e-02 + (5.300000e-01 * abs(i - 0.5));\n  float lumDamp = smoothstep(0.0, 1.0, 2.500000e+01 * i);\n  float x = smoothstep(0.0, 1.0, chroma / cd);\n  exponent = (((x * (1.0 - i)) * lumDamp) * (exponent - 1.0)) + 1.0;\n  float bw = dot(image.rgb, rgbWeights.rgb);\n  bw = pow(bw, exponent);\n  x = 1.0 - smoothstep(0.0, 1.0, chroma * 1.000000e+01);\n  float lumAdjust = (((bw * (1.0 - bw)) * x) * (neutralGamma - 1.0)) + 1.0;\n  lumAdjust = 5.0 - (4.0 * lumAdjust);\n  bw = pow(bw, lumAdjust);\n  float result = ((((1.8031 * bw) * bw) * bw) - ((2.1972 * bw) * bw)) + (1.3823 * bw);\n  bw = mix(bw, result, -phototone);\n  return vec4(bw, bw, bw, image.a);\n}\n"
- "kernel vec4 _smartcolor_cast(vec4 im, float lum, float grayI, float grayQ, float strength) {\n  vec4 pix = clamp(im, 0.0, 1.0);\n  pix.rgb = pow(pix.rgb, vec3(0.25));\n  pix.rgb = ((pix.r * vec3(0.299, 5.957160e-01, 2.114560e-01)) + (pix.g * vec3(0.587, -2.744530e-01, -5.225910e-01))) + (pix.b * vec3(0.114, -3.212630e-01, 3.111350e-01));\n  vec2 grayOffset = vec2(grayI, grayQ);\n  vec3 result = pix.rgb;\n  float newStrength = 1.0 + ((strength - 1.0) * (1.0 - pix.r));\n  result.gb = pix.gb + (newStrength * grayOffset);\n  float damp = max(min(1.0, pix.r / (lum + 1.000000e-05)), 0.0);\n  result.rgb = mix(pix.rgb, result.rgb, damp);\n  pix.rgb = ((result.r * vec3(1.0)) + (result.g * vec3(9.562960e-01, -2.721220e-01, -1.10699))) + (result.b * vec3(6.210240e-01, -6.473810e-01, 1.70461));\n  pix.rgb = clamp(pix.rgb, 0.0, 1.0);\n  pix.rgb *= (pix.rgb * pix.rgb) * pix.rgb;\n  pix.rgb += (min(im.rgb, 0.0) + max(im.rgb, 1.0)) - 1.0;\n  return pix;\n}\n"
- "kernel vec4 _smartcolor_vibrancy_gt1(vec4 im, float amt) {\n  float gray = dot(clamp(im.rgb, 0.0, 1.0), vec3(0.3, 0.5, 2.000000e-01));\n  float y = dot(clamp(im.rgb, 0.0, 1.0), vec3(4.000000e-01, 2.000000e-01, 1.000000e-01));\n  float damp = 1.0 - ((4.0 * y) * (1.0 - y));\n  float s = 1.0 / ((im.r + im.g) + im.b);\n  float r = im.r * s;\n  float b = im.b * s;\n  float d = 1.0 - (8.000000e-01 * smoothstep(2.000000e-01, 4.000000e-01, r - b));\n  damp *= d;\n  damp = (amt > 2.500) ? min(damp + ((amt - 2.500) / 5.0), 1.0) : damp;\n  float sat = min(amt, 3.0);\n  vec4 result;\n  result.rgb = ((im.rgb - gray) * sat) + gray;\n  result.rgb = mix(im.rgb, result.rgb, damp);\n  result.a = im.a;\n  return result;\n}\n"
- "kernel vec4 _sobelEdges(sampler src, float scale) {\n  vec2 coord = destCoord();\n  vec2 sc = samplerTransform(src, coord);\n  vec2 dx = samplerTransform(src, coord + vec2(1.0, 0.0)) - sc;\n  vec2 dy = samplerTransform(src, coord + vec2(0.0, 1.0)) - sc;\n  vec2 d = dx + dy;\n  vec4 pix3 = sample(src, sc + d);\n  vec4 pix7 = sample(src, sc - d);\n  d = dx - dy;\n  vec4 pix9 = sample(src, sc + d);\n  vec4 pix1 = sample(src, sc - d);\n  vec4 pix2 = sample(src, sc + dy);\n  vec4 pix8 = sample(src, sc - dy);\n  vec4 pix6 = sample(src, sc + dx);\n  vec4 pix4 = sample(src, sc - dx);\n  vec4 pix5 = sample(src, sc);\n  vec4 gx = ((pix3 + (2.0 * pix6)) + pix9) - ((pix1 + (2.0 * pix4)) + pix7);\n  vec4 gy = ((pix1 + (2.0 * pix2)) + pix3) - ((pix7 + (2.0 * pix8)) + pix9);\n  vec4 g2 = (gx * gx) + (gy * gy);\n  pix5 = vec4(pix5.rgb / max(pix5.a, 1.000000e-05), pix5.a);\n  pix5.rgb = sqrt(g2).rgb * scale;\n  return vec4(pix5.rgb * pix5.a, pix5.a);\n}\n"
- "kernel vec4 _sparserendering_add_noise(vec4 inputTex, vec4 noiseLumaTex, vec2 params) {\n  float lumaNoiseModelCoeff = params.x;\n  float lumaNoiseAmpl = params.y;\n  vec4 pixBlurred = inputTex;\n  float noiseLuma = (noiseLumaTex.x * 1.000000e+01) - 5.0;\n  vec3 kRGB_to_Y = vec3(0.299, 0.587, 0.114);\n  float outLuma = dot(pixBlurred.xyz, kRGB_to_Y);\n  float addLumaNoiseLevel = lumaNoiseAmpl * mix(1.0, outLuma, lumaNoiseModelCoeff);\n  vec4 pixOut;\n  pixOut.xyz = clamp(pixBlurred.xyz + (noiseLuma * addLumaNoiseLevel), vec3(0.0), vec3(1.0));\n  pixOut.w = pixBlurred.w;\n  return clamp(pixOut, vec4(0.0), vec4(1.0));\n}\n"
- "kernel vec4 _spotColor(vec4 src, vec4 cclr1, vec4 rclr1, vec4 cclr2, vec4 rclr2, vec4 cclr3, vec4 rclr3, vec4 closeness, vec4 contrast) {\n  vec4 pix = vec4(src.rgb / max(src.a, 1.000000e-05), src.a);\n  float dist = length(pix.rgb - cclr1.rgb);\n  float alpha = clamp(((closeness.x - dist) * contrast.x) + 0.5, 0.0, 1.0);\n  vec4 result1 = rclr1 * alpha;\n  dist = length(pix.rgb - cclr2.rgb);\n  alpha = clamp(((closeness.y - dist) * contrast.y) + 0.5, 0.0, 1.0);\n  vec4 result2 = rclr2 * alpha;\n  dist = length(pix.rgb - cclr3.rgb);\n  alpha = clamp(((closeness.z - dist) * contrast.z) + 0.5, 0.0, 1.0);\n  vec4 result3 = rclr3 * alpha;\n  pix = result1 + ((1.0 - result1.a) * vec4(1.0));\n  pix = result2 + ((1.0 - result2.a) * pix);\n  return result3 + ((1.0 - result3.a) * pix);\n}\n"
- "kernel vec4 _starshine(vec2 center, vec4 xyvec, vec4 parms, float widthrecip, vec4 color) {\n  vec2 offset = destCoord() - center;\n  vec2 loc = vec2(dot(offset, xyvec.xy), dot(offset, xyvec.zw));\n  float l = length(offset);\n  float rlen = parms.x / l;\n  loc = max((abs(loc) * widthrecip) + parms.w, vec2(1.000000e-07));\n  loc = abs(parms.x / loc);\n  loc = (loc * loc) * loc;\n  float f = (loc.x * loc.y) * parms.z;\n  float g = clamp(1.0 - (l * parms.y), 0.0, 1.0);\n  vec4 result = ((rlen * rlen) * color) + ((g * g) * f);\n  result.a = min(result.a, 1.0);\n  return result;\n}\n"
- "kernel vec4 _sunbeams(sampler noise, vec4 centers, vec4 params, vec4 color) {\n  float sunRadius2 = params.x;\n  float striationFactor = params.y;\n  float a = params.z;\n  float b = params.w;\n  vec2 v = destCoord() - centers.xy;\n  float len = length(v);\n  float len2 = dot(v, v);\n  vec2 noiseCtr = centers.zw;\n  vec2 noiseLoc = (normalize(v) * 5.000000e+01) + noiseCtr;\n  vec4 npix = sample(noise, samplerTransform(noise, noiseLoc));\n  float noiseAmount = (npix.r * a) + b;\n  float f2 = sunRadius2 / (len2 + 1.000000e-04);\n  vec4 pix = (f2 * color) + noiseAmount;\n  pix *= clamp(1.0 - (len * striationFactor), 0.0, 1.0);\n  pix.a = clamp(pix.a, 0.0, 1.0);\n  return pix;\n}\n"
- "kernel vec4 _torusRefraction(sampler src, vec2 center, float a, float b, float c, float indexOfRefraction, float levitation) {\n  vec2 v0 = destCoord() - center;\n  float dist = length(v0);\n  vec2 unitvec = normalize(v0);\n  float fdom = (a * dist) + b;\n  float alpha = clamp((1.0 - abs(fdom)) * c, 0.0, 1.0);\n  vec3 surfaceNormal = vec3(unitvec * fdom, sqrt(1.0 - (fdom * fdom)));\n  float surfaceHeight = (surfaceNormal.z * c) + levitation;\n  vec3 rayOrigin = vec3(destCoord(), surfaceHeight);\n  float eta = 1.0 / indexOfRefraction;\n  float c1 = surfaceNormal.z;\n  float cs2 = 1.0 - ((eta * eta) * (1.0 - (c1 * c1)));\n  vec3 rayDirection = eta * vec3(0.0, 0.0, -1.0);\n  c1 = (eta * c1) - sqrt(abs(cs2));\n  rayDirection += c1 * surfaceNormal;\n  float t = (-surfaceHeight) / rayDirection.z;\n  vec3 hitPoint = rayOrigin + (t * rayDirection);\n  if (alpha < 1.000000e-03) hitPoint.xy = vec2(5.000000e+01);\n  vec4 color = sample(src, samplerTransform(src, hitPoint.xy));\n  color = (cs2 < 0.0) ? vec4(0.0, 0.0, 0.0, 0.0) : color;\n  vec4 unrefracted = sample(src, samplerCoord(src));\n  return mix(unrefracted, color, alpha);\n}\n"
- "kernel vec4 _unsharpmask(vec4 s, vec4 b, float k) {\n  s.rgb += (s.rgb - (b.rgb * (s.a / max(b.a, 1.000000e-04)))) * k;\n  return s;\n}\n"
- "kernel vec4 _vibrance_neg(vec4 pixel0, float vibrance) {\n  vec4 pixel = clamp(pixel0, 1.000000e-04, 9.999000e-01);\n  vec4 pdelta = pixel0 - pixel;\n  float gray = ((pixel.r + pixel.g) + pixel.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  vec3 rgbsat = max((pixel.rgb - gray) * gii, (gray - pixel.rgb) * gi);\n  float sat = max(max(rgbsat.r, rgbsat.g), rgbsat.b);\n  float skin = ((min(pixel.r - pixel.g, (pixel.g * 2.0) - pixel.b) * 4.0) * (1.0 - rgbsat.r)) * gi;\n  skin = 1.500000e-01 + (clamp(skin, 0.0, 1.0) * 7.000000e-01);\n  float boost = (((sat * (sat - 1.0)) + 1.0) * vibrance) * (1.0 - skin);\n  pixel = clamp(pixel + ((pixel - gray) * boost), 0.0, 1.0);\n  pixel.a = pixel0.a;\n  pixel.rgb += pdelta.rgb;\n  return pixel;\n}\n"
- "kernel vec4 _vibrance_pos(vec4 pixel0, vec4 vvec) {\n  vec4 pixel = clamp(pixel0, 1.000000e-04, 9.999000e-01);\n  vec4 pdelta = pixel0 - pixel;\n  float gray = ((pixel.r + pixel.g) + pixel.b) * 3.333300e-01;\n  float gi = 1.0 / gray;\n  float gii = 1.0 / (1.0 - gray);\n  vec3 rgbsat = max((pixel.rgb - gray) * gii, (gray - pixel.rgb) * gi);\n  float sat = max(max(rgbsat.r, rgbsat.g), rgbsat.b);\n  float skin = ((min(pixel.r - pixel.g, (pixel.g * 2.0) - pixel.b) * 4.0) * (1.0 - rgbsat.r)) * gi;\n  skin = 1.500000e-01 + (clamp(skin, 0.0, 1.0) * 7.000000e-01);\n  float boost = dot(vvec, vec4(1.0, sat, sat * sat, (sat * sat) * sat)) * (1.0 - skin);\n  pixel = clamp(pixel + ((pixel - gray) * boost), 0.0, 1.0);\n  pixel.a = pixel0.a;\n  pixel.rgb += pdelta.rgb;\n  return pixel;\n}\n"
- "kernel vec4 _vignetteeffect(vec4 s, vec2 center, vec4 params) {\n  vec2 point = (destCoord() - center) * params.x;\n  float dist = sqrt(dot(point, point));\n  float x = clamp((dist - params.y) * params.z, 0.0, 1.0);\n  x = ((x * x) * x) * ((((6.0 * x) - 1.500000e+01) * x) + 1.000000e+01);\n  float v = 1.0 - (x * params.w);\n  v = (((((((-1.206385e-01) * v) + 5.438787e-01) * v) + 5.387726e-01) * v) + 3.760100e-02) * v;\n  s.rgb *= v;\n  return s;\n}\n"
- "kernel vec4 _vignetteeffectneg(vec4 s, vec2 center, vec4 params) {\n  vec2 point = (destCoord() - center) * params.x;\n  float dist = sqrt(dot(point, point));\n  float x = clamp((dist - params.y) * params.z, 0.0, 1.0);\n  x = ((x * x) * x) * ((((6.0 * x) - 1.500000e+01) * x) + 1.000000e+01);\n  float v = ((16.0 * x) * params.w) + 1.0;\n  s.rgb *= v;\n  return s;\n}\n"
- "kernel vec4 _vividLightBlendMode(vec4 fore, vec4 back) {\n  vec4 Cs = unpremultiply(fore);\n  vec4 Cb = unpremultiply(back);\n  vec4 epsilon = vec4(1.000000e-07);\n  vec4 lo = 1.0 - ((1.0 - Cb) / max(2.0 * Cs, epsilon));\n  vec4 hi = Cb / max(2.0 * (1.0 - Cs), epsilon);\n  vec4 B = compare(0.5 - Cs, hi, lo);\n  B.a = 1.0;\n  B = clamp(B, 0.0, 1.0);\n  return ((back * (1.0 - fore.a)) + (fore * (1.0 - back.a))) + ((B * fore.a) * back.a);\n}\n"
- "kernel vec4 _xSmooth(sampler image) {\n  float v;\n  float sum = 0.0;\n  float minv = 1.000000e+02;\n  vec2 dc = destCoord();\n  for (int i = -4; i < 5; i++) {\n    v = sample(image, samplerTransform(image, dc + vec2(float(i), 0.0))).r;\n    sum += (v * v) * 1.111111e-01;\n    minv = min(minv, v);\n  }\n  return vec4(sqrt(sum), minv, 0.0, 1.0);\n}\n"
- "kernel vec4 _ySmooth(sampler image, sampler reference, vec4 blurValues) {\n  vec2 v;\n  float sum = 0.0;\n  float minv = 1.000000e+02;\n  vec2 dc = destCoord();\n  for (int i = -4; i < 5; i++) {\n    v = sample(image, samplerTransform(image, dc + vec2(0.0, float(i)))).rg;\n    sum += (v.r * v.r) * 1.111111e-01;\n    minv = min(minv, v.g);\n  }\n  sum = sqrt(sum);\n  float refT0 = blurValues.x;\n  float refT1 = blurValues.y;\n  float minT0 = blurValues.z;\n  float minT1 = blurValues.w;\n  float ref = sample(reference, samplerCoord(reference)).x;\n  float mixWeight = smoothstep(refT0, refT1, ref) * smoothstep(minT0, minT1, minv);\n  float result = mix(ref, sum, mixWeight);\n  return vec4(result, 0.0, 0.0, 1.0);\n}\n"
- "kernel vec4 _zoom(sampler src, vec2 center, float k) {\n  vec2 dist = destCoord() - center;\n  vec4 result = vec4(0.0);\n  for (int n = 0; n < 100; n++) {\n    float f = float(n) / 9.900000e+01;\n    f -= 0.5;\n    f = ((f + ((f * f) * f)) * 8.000000e-01) + 0.5;\n    vec2 p = dist * mix(k, 1.0, f);\n    result += sample(src, samplerTransform(src, center + p)) * 1.000000e-02;\n  }\n  return result;\n}\n"
- "lastFaceIndex"
- "latestFaceTimestamp"
- "latestImageTimestamp"
- "leftEyeBlinkScore"
- "leftEyeOpen"
- "leftEyeRect"
- "leftImage"
- "local maxima size: %ld\n"
- "matteType"
- "maxNumPendingFrames"
- "maxScore"
- "maxSkewness"
- "memory allocation error"
- "metallibV1-from_archive"
- "metallibV2-from_archive"
- "minScore"
- "noiseThreshold"
- "noop_full_intermediate"
- "noop_intermediate_cached"
- "normalizedFaceRect"
- "normalizedFocusScore"
- "normalizedSigma"
- "numEntries"
- "numFramesNoFaces"
- "numHWFaces"
- "numScores"
- "ok"
- "out of boundaries"
- "out of bounds error"
- "overlapWithHwRect:"
- "overlapWithSwRect:"
- "overrideImage"
- "overrideProps"
- "padRoiRect:paddingX:paddingY:"
- "performEmotionalRejectionOnCluster:"
- "performRegistration:deltaCol:deltaRow:"
- "persistentDomainForName:"
- "portraitEffectsMatte:PortraitEffectsMatteVersion"
- "predictResult"
- "processClusters:"
- "projectionCols_planar8UtoF"
- "projectionMemoryBlock"
- "projectionRows_planar8UtoF"
- "projectionSignature"
- "providerGetBytePointerCallback"
- "providerGetBytesAtPositionCallback_1C08_surface"
- "providerGetBytesAtPositionCallback_1C0f_surface"
- "providerGetBytesAtPositionCallback_1C0h_surface"
- "providerGetBytesAtPositionCallback_1C0h_surface_lut"
- "providerGetBytesAtPositionCallback_1C16_surface"
- "providerGetBytesAtPositionCallback_2C08_surface"
- "providerGetBytesAtPositionCallback_2C0f_surface"
- "providerGetBytesAtPositionCallback_2C0h_surface"
- "providerGetBytesAtPositionCallback_2C16_surface"
- "providerGetBytesAtPositionCallback_A008_surface"
- "providerGetBytesAtPositionCallback_AYCbCr8_surface"
- "providerGetBytesAtPositionCallback_CbYCrYFull_surface"
- "providerGetBytesAtPositionCallback_CbYCrY_surface"
- "providerGetBytesAtPositionCallback_YCbYCrFull_surface"
- "providerGetBytesAtPositionCallback_YCbYCr_surface"
- "providerGetBytesAtPositionCallback_l10r_surface"
- "providerGetBytesAtPositionCallback_w30r_surface"
- "providerGetBytesAtPositionCallback_w40a_surface"
- "providerReleaseBytePointerCallback"
- "pushSpan:s->stackHeadChunk->next"
- "q24@0:8@16"
- "q24@?0@\"FCRFace\"8@\"FCRFace\"16"
- "r+"
- "redEyeRemovalWithData:recognitionChannel"
- "redEyeRemovalWithPoint:recognitionChannels[0]"
- "redEyeRemovalWithPoint:recognitionChannels[1]"
- "redEyeRemovalWithPoint:recognitionChannels[i]"
- "redEyeRemovalWithPoint:table16"
- "referenceROI = (%d,%d)->(%d,%d)\n"
- "regions exist\n"
- "registrationErrorIntegral"
- "registrationErrorX"
- "registrationErrorY"
- "reject"
- "releaseImage"
- "removeObject:"
- "removing config entry: %d\n"
- "renameMapping"
- "rgba"
- "rightEyeBlinkScore"
- "rightEyeOpen"
- "rightEyeRect"
- "roiSize"
- "rollAngle"
- "scaleVector"
- "selectCoverPhotoFromMultiple:burstSize:"
- "sem"
- "sensedROI = (%d,%d)->(%d,%d)\n"
- "setAEAverage:"
- "setAEDelta:"
- "setAEMatrix:"
- "setAEStable:"
- "setAETarget:"
- "setAFStable:"
- "setActionAmount:"
- "setActionClassifier:"
- "setActionClusteringScore:"
- "setActionScore:"
- "setAllImageIdentifiers:"
- "setAvgHorzDiffY:"
- "setBestImageIdentifiersArray:"
- "setBlendBehaviorBit:value:"
- "setBlurExtent:"
- "setBurstCoverSelection:"
- "setBurstId:"
- "setBurstImages:"
- "setBurstLogFileName:"
- "setBytesPerRow:"
- "setCbuffer:"
- "setClusterArray:"
- "setClusterByImageIdentifier:"
- "setCompletionBlock:"
- "setDividerScore:"
- "setDoLimitedSharpnessAndBlur:"
- "setDummyAnalysisCount:"
- "setEmotionallyRejected:"
- "setEnableAnalysis:"
- "setEnableDumpYUV:"
- "setEnableFaceCore:"
- "setExclude:"
- "setExpressionFeatures:"
- "setFCRBlinkFeaturesSize:"
- "setFCRLeftEyeFeaturesOffset:"
- "setFCRRightEyeFeaturesOffset:"
- "setFCRSmileAndBlinkFeatures:"
- "setFCRSmileFeaturesOffset:"
- "setFCRSmileFeaturesSize:"
- "setFace:"
- "setFaceAngle:"
- "setFaceIDCounts:"
- "setFaceId:"
- "setFaceScore:"
- "setFaceSize:"
- "setFaceStatArray:"
- "setFaceType:"
- "setFacesRoiRect:"
- "setFocusScore:"
- "setForceFaceDetectionEnable:"
- "setFoundByFaceCore:"
- "setFramesSinceLast:"
- "setFullsizeJpegData:"
- "setFullsizeJpegSize:"
- "setHasLeftEye:"
- "setHasRegistrationData:"
- "setHasRightEye:"
- "setHasRollAngle:"
- "setHasYawAngle:"
- "setHighNoiseThreshold:"
- "setHwCenter:"
- "setHwFaceId:"
- "setHwFaceRect:"
- "setHwLastFrameSeen:"
- "setHwSize:"
- "setImageId:"
- "setImageProps:"
- "setImageScore:"
- "setInputQualityLevel:"
- "setIsGarbage:"
- "setIsSyncedWithImage:"
- "setLatestFaceTimestamp:"
- "setLeftEye:"
- "setLeftEyeBlinkScore:"
- "setLeftEyeOpen:"
- "setLeftEyeRect:"
- "setLeftImage:"
- "setMaxNumPendingFrames:"
- "setMaxScore:"
- "setMaxSkewness:"
- "setMinScore:"
- "setMouth:"
- "setNoiseThreshold:"
- "setNormalizedFaceRect:"
- "setNormalizedFocusScore:"
- "setNormalizedSigma:"
- "setNumHWFaces:"
- "setNumScores:"
- "setRegistrationErrorIntegral:"
- "setRegistrationErrorX:"
- "setRegistrationErrorY:"
- "setRightEye:"
- "setRightEyeBlinkScore:"
- "setRightEyeOpen:"
- "setRightEyeRect:"
- "setRoiSize:"
- "setRollAngle:"
- "setSmallFace:"
- "setSmileScore:"
- "setSmiling:"
- "setStatsByImageIdentifier:"
- "setSvmParameters:"
- "setSwCenter:"
- "setSwFaceId:"
- "setSwLastFrameSeen:"
- "setSwSize:"
- "setTemporalOrder:"
- "setTestAverageCameraTravelDistance:"
- "setTestAverageRegistrationErrorSkewness:"
- "setTestBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix:"
- "setTestInOutRatio:"
- "setTestMaxInnerDistance:"
- "setTestMaxPeakRegistrationError:"
- "setTestMaxRegistrationErrorIntegral:"
- "setTestMaxRegistrationErrorSkewness:"
- "setTestMeanPeakRegistrationError:"
- "setTestMinRegionOfInterestSize:"
- "setTimeBlinkDetectionDone:"
- "setTimeFaceDetectionDone:"
- "setTimeReceived:"
- "setTrueLocalMaximum:"
- "setTx:"
- "setTy:"
- "setVersion:"
- "setVersionString:"
- "setYawAngle:"
- "setYbuffer:"
- "setting faces ROI to (%.3f,%.3f,%.3f,%.3f)\n"
- "setupFaceDetector"
- "sharpnessGrid"
- "shuffleMask"
- "smallFace"
- "smileScore"
- "smiling"
- "smoothedROI"
- "softlink:o:path:/System/Library/Frameworks/Vision.framework/libfaceCore.dylib"
- "softlink:r:path:/System/Library/Frameworks/AVFoundation.framework/AVFoundation"
- "specular bitmask outside path"
- "specular bitmask path outside arc bodies"
- "specular bitmask path outside arcs"
- "srcHR"
- "staccato_mode_logging"
- "staccato_yuv_dump"
- "statsByImageIdentifier"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "sumScores"
- "sumSqScores"
- "svmParameters"
- "swCenter"
- "swFaceId"
- "swFaceRect"
- "swLastFrameSeen"
- "swSize"
- "targHR"
- "targRefWt"
- "temporalOrder"
- "testArchive:"
- "testAverageCameraTravelDistance"
- "testAverageRegistrationErrorSkewness"
- "testBeginningVsEndAEMatrixVsAverageAdjacentAEMatrix"
- "testBinaryArchive"
- "testInOutRatio"
- "testMaxInnerDistance"
- "testMaxPeakRegistrationError"
- "testMaxRegistrationErrorIntegral"
- "testMaxRegistrationErrorSkewness"
- "testMeanPeakRegistrationError"
- "testMinRegionOfInterestSize"
- "testVector"
- "threadgroup float4 tgcc[]"
- "timeBlinkDetectionDone"
- "timeFaceDetectionDone"
- "timeReceived"
- "trash"
- "trueLocalMaximum"
- "tx"
- "ty"
- "updateROI:"
- "v136@?0r^v8r^v16r^v24r^v32r^v40^{__IOSurface=}48{Texture=(?=Q{?=II}{?=^v^v})}56Q72{CGRect={CGPoint=dd}{CGSize=dd}}80B112i116^v120^v128"
- "v136@?0r^v8r^v16r^v24r^v32r^v40^{__IOSurface=}48{Texture=(?=Q{?=II}{?=^v^v})}56Q72{CGRect={CGPoint=dd}{CGSize=dd}}80B112i116^v120^{TileTask=}128"
- "v24@0:8*16"
- "v24@0:8^{__SVMParameters=[7{__SVMScaleOffset=ff}]ddii^{CIBurstSupportVector}^{CIBurstSupportVector}}16"
- "v24@0:8i16B20"
- "v28@0:8*16i24"
- "v32@0:8{GridROI_t=iiii}16"
- "v40@0:8@16^f24^f32"
- "v40@0:8@16{CGSize=dd}24"
- "v48@0:8^^f16^^f24^^f32^^f40"
- "v56@0:8@16@24@32@40@?48"
- "vImage error"
- "value:withObjCType:"
- "vec2 _ci_simd_shuffle_down(vec2 gb, int offset) {\n  return gb;\n}\nkernel vec4 _ci_writeSIMD_42X(vec4 color, vec4 shuffleMask) {\n  vec2 p = writeCoord();\n  writeImage(color.rrrr, p);\n  vec2 cc = vec2(color.gb);\n  vec2 ccSum;\n  ccSum = _ci_simd_shuffle_down(cc, 0) * shuffleMask.x;\n  ccSum += _ci_simd_shuffle_down(cc, 1) * shuffleMask.y;\n  ccSum += _ci_simd_shuffle_down(cc, 16) * shuffleMask.z;\n  ccSum += _ci_simd_shuffle_down(cc, 17) * shuffleMask.w;\n  /* empty */;\n  const int x = int(p.x);\n  const int y = int(p.y);\n  if (shuffleMask.z > 1.000000e-03) {\n    if (((x % 2) == 0) && ((y % 2) == 0)) writeImagePlane(ccSum.rgrg, p / 2.0);\n  } else if (shuffleMask.y > 1.000000e-03) {\n    if ((x % 2) == 0) writeImagePlane(ccSum.rgrg, p / vec2(2.0, 1.0));\n  } else writeImagePlane(ccSum.rgrg, p);\n  return color;\n}\n"
- "vec2 _cubic_coefs_(vec2 x, vec4 c) {\n  x = abs(x);\n  return (((((c.x * x) * x) * x) + ((c.y * x) * x)) + (c.z * x)) + c.w;\n}\nkernel vec4 _cubicUpsampleX0(sampler src, vec2 scale, vec4 coefsLT1, vec4 coefsLT2) {\n  vec2 dcMappedToSrc = scale * destCoord();\n  vec2 srcCenterBefore = floor(dcMappedToSrc - 0.5) + 0.5;\n  vec2 delta = srcCenterBefore - dcMappedToSrc;\n  vec2 weight0 = _cubic_coefs_(delta - 1.0, coefsLT2);\n  vec2 weight1 = _cubic_coefs_(delta, coefsLT1);\n  vec2 weight3 = _cubic_coefs_(delta + 2.0, coefsLT2);\n  vec2 w1 = weight0 + weight1;\n  vec2 w2 = vec2(1.0) - w1;\n  vec2 o1 = compare(w1 - 1.000000e-04, vec2(0.0), weight1 / w1) + (srcCenterBefore - 1.0);\n  vec2 o2 = compare(w2 - 1.000000e-04, vec2(0.0), weight3 / w2) + (srcCenterBefore + 1.0);\n  vec4 r;\n  r = (w1.x * w1.y) * sample(src, samplerTransform(src, vec2(o1.x, o1.y)));\n  r += (w2.x * w1.y) * sample(src, samplerTransform(src, vec2(o2.x, o1.y)));\n  r += (w1.x * w2.y) * sample(src, samplerTransform(src, vec2(o1.x, o2.y)));\n  r += (w2.x * w2.y) * sample(src, samplerTransform(src, vec2(o2.x, o2.y)));\n  return r;\n}\n"
- "vec3 s_pow(vec3 x, vec3 g) {\n  vec3 xx = max(abs(x), 1.000000e-06);\n  return sign(x) * pow(xx, g);\n}\nkernel vec4 _flexMap(vec4 im, vec4 gm, vec3 invGamma, vec3 minv, vec3 maxv, float scale, vec3 kIn, vec3 kOut) {\n  vec3 gainLog2 = ((maxv - minv) * s_pow(gm.rgb, invGamma)) + minv;\n  vec3 gainLin = exp2(scale * gainLog2);\n  im.rgb = (gainLin * (im.rgb + kIn)) - kOut;\n  return im;\n}\n"
- "vec4 _pointillizeStep(sampler src, vec4 background, sampler noise, vec2 cellSize, vec2 noiseOffset, vec2 cellOffset, vec2 dc) {\n  float o;\n  float tSize = 256.0;\n  float _randomFactor = 6.500000e-01;\n  float _radiusFactor = 7.100000e-01;\n  float _colorRandom = 1.000000e-01;\n  vec2 noiseLoc = floor((dc * cellSize.y) + 0.5) + noiseOffset;\n  vec4 np = sample(noise, samplerTransform(noise, mod(noiseLoc, tSize)));\n  vec2 cellLoc = (((floor((dc * cellSize.y) - 0.5) + 0.5) * cellSize.x) + 0.5) + cellOffset;\n  cellLoc += ((np.xy - 0.5) * cellSize.x) * _randomFactor;\n  o = distance(dc, cellLoc);\n  o = clamp((1.0 - ((o * cellSize.y) / _radiusFactor)) * 3.0, 0.0, 1.0);\n  o = ((3.0 - (2.0 * o)) * o) * o;\n  vec4 p1 = sample(src, samplerTransform(src, cellLoc));\n  p1.rgb += (vec3(np.b - 0.5) * _colorRandom) * p1.a;\n  return mix(background, p1, o);\n}\nkernel vec4 _pointillize(sampler src, sampler noise, vec4 parms) {\n  vec4 background = sample(src, samplerCoord(src)).aaaa;\n  background = _pointillizeStep(src, background, noise, parms.zw, parms.xy + vec2(0.5, 0.5), vec2(parms.z, parms.z), destCoord());\n  background = _pointillizeStep(src, background, noise, parms.zw, parms.xy + vec2(-0.5, 0.5), vec2(0, parms.z), destCoord());\n  background = _pointillizeStep(src, background, noise, parms.zw, parms.xy + vec2(0.5, -0.5), vec2(parms.z, 0), destCoord());\n  background = _pointillizeStep(src, background, noise, parms.zw, parms.xy + vec2(-0.5, -0.5), vec2(0, 0), destCoord());\n  return background;\n}\n"
- "versionString"
- "void *AVFoundationLibrary(void)"
- "void *FaceCoreLibrary(void)"
- "writeGridROI:"
- "writeImageHeight"
- "writeImageWidth"
- "writePixel"
- "xml"
- "yawAngle"
- "{\nthreadgroup float4 _ci_writeTG_42X_tgcc[16*16] = {0.,0.,0.,0.};\n"
- "{CGRect={CGPoint=dd}{CGSize=dd}}40@0:8@16@24^B32"
- "{CGRect={CGPoint=dd}{CGSize=dd}}56@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16f48f52"
- "{FastRegistration_Signatures=\"piRow\"^f\"nPiRow\"Q\"piRowTable\"{Projections_meanStdTable=\"sumTable\"^f\"sumSqTable\"^f}\"piCol\"^f\"nPiCol\"Q\"piColTable\"{Projections_meanStdTable=\"sumTable\"^f\"sumSqTable\"^f}}"
- "{GridROI_t=\"startX\"i\"startY\"i\"endX\"i\"endY\"i}"
- "{GridROI_t=iiii}16@0:8"
- "{vector<CGRect, std::allocator<CGRect>>=^{CGRect}^{CGRect}{__compressed_pair<CGRect *, std::allocator<CGRect>>=^{CGRect}}}44@?0i8{CGRect={CGPoint=dd}{CGSize=dd}}12"
- "{vector<CI::Perspective::Line, std::allocator<CI::Perspective::Line>>=\"__begin_\"^{?}\"__end_\"^{?}\"__end_cap_\"{__compressed_pair<CI::Perspective::Line *, std::allocator<CI::Perspective::Line>>=\"__value_\"^{?}}}"
- "{vector<LineCostProxy, std::allocator<LineCostProxy>>=\"__begin_\"^{LineCostProxy}\"__end_\"^{LineCostProxy}\"__end_cap_\"{__compressed_pair<LineCostProxy *, std::allocator<LineCostProxy>>=\"__value_\"^{LineCostProxy}}}"

```
