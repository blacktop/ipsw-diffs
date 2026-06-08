## DeepVideoProcessingCore

> `/System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore`

```diff

-2.10.0.0.0
-  __TEXT.__text: 0x6d674
-  __TEXT.__auth_stubs: 0xec0
-  __TEXT.__objc_methlist: 0x50b4
-  __TEXT.__const: 0x688
-  __TEXT.__cstring: 0x658b
-  __TEXT.__oslogstring: 0x33ab
-  __TEXT.__gcc_except_tab: 0x2e0
-  __TEXT.__unwind_info: 0x12f0
-  __TEXT.__objc_classname: 0x6cb
-  __TEXT.__objc_methname: 0x13c81
-  __TEXT.__objc_methtype: 0x77ae
-  __TEXT.__objc_stubs: 0x77e0
-  __DATA_CONST.__got: 0x388
-  __DATA_CONST.__const: 0x310
-  __DATA_CONST.__objc_classlist: 0x280
+3.6.0.0.0
+  __TEXT.__text: 0x7a9f0
+  __TEXT.__objc_methlist: 0x5654
+  __TEXT.__const: 0x770
+  __TEXT.__cstring: 0x7359
+  __TEXT.__oslogstring: 0x418b
+  __TEXT.__gcc_except_tab: 0x258
+  __TEXT.__unwind_info: 0x1388
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x29d8
-  __DATA_CONST.__objc_superrefs: 0x258
-  __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x778
+  __DATA_CONST.__objc_selrefs: 0x2d98
+  __DATA_CONST.__objc_superrefs: 0x288
+  __DATA_CONST.__objc_arraydata: 0x98
+  __DATA_CONST.__got: 0x3c8
   __AUTH_CONST.__const: 0xf0
-  __AUTH_CONST.__cfstring: 0x3260
-  __AUTH_CONST.__objc_const: 0x11208
-  __AUTH_CONST.__objc_intobj: 0x180
-  __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1900
-  __DATA.__objc_ivar: 0x150c
+  __AUTH_CONST.__cfstring: 0x3b00
+  __AUTH_CONST.__objc_const: 0x12b28
+  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH_CONST.__auth_got: 0x828
+  __AUTH.__objc_data: 0x1b30
+  __DATA.__objc_ivar: 0x1778
   __DATA.__data: 0x260
   __DATA.__bss: 0x8
   __DATA.__common: 0x10

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreImage.framework/CoreImage
   - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
+  - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface

   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
   - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
-  - /System/Library/PrivateFrameworks/FRC.framework/FRC
   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AEB7FCBE-472B-3E39-ADFA-7497183CC310
-  Functions: 2540
-  Symbols:   8602
-  CStrings:  4682
+  UUID: FB7527DD-ECD9-3542-A4D0-D27F018C1EAE
+  Functions: 2829
+  Symbols:   9544
+  CStrings:  1592
 
Symbols:
+ +[DVPDenseUpscalerConfiguration channelCountForType:]
+ +[DVPLensFlareMitigationParameters getMotionShiftFromPastOpticalCenters:futureOpticalCenters:currentOpticalCenter:currentOpticalCenterShift:]
+ +[DVPLensFlareMitigationParameters opticalCentersReferenceSize]
+ +[DenseUpscaler channelCountForType:]
+ -[DVPDenseUpscalerConfiguration .cxx_destruct]
+ -[DVPDenseUpscalerConfiguration denseBufferPixelFormat]
+ -[DVPDenseUpscalerConfiguration destinationHeight]
+ -[DVPDenseUpscalerConfiguration destinationWidth]
+ -[DVPDenseUpscalerConfiguration frameHeight]
+ -[DVPDenseUpscalerConfiguration framePreferredPixelFormats]
+ -[DVPDenseUpscalerConfiguration frameSupportedPixelFormats]
+ -[DVPDenseUpscalerConfiguration frameWidth]
+ -[DVPDenseUpscalerConfiguration initWithSourceWidth:sourceHeight:destinationWidth:destinationHeight:frameWidth:frameHeight:type:]
+ -[DVPDenseUpscalerConfiguration sourceHeight]
+ -[DVPDenseUpscalerConfiguration sourceWidth]
+ -[DVPDenseUpscalerConfiguration type]
+ -[DVPDenseUpscalerParameters .cxx_destruct]
+ -[DVPDenseUpscalerParameters destinationFrame]
+ -[DVPDenseUpscalerParameters guideFrame]
+ -[DVPDenseUpscalerParameters initWithSourceFrame:guideFrame:destinationFrame:]
+ -[DVPDenseUpscalerParameters sourceFrame]
+ -[DVPDrawShapeFontDescriptor .cxx_destruct]
+ -[DVPDrawShapeFontDescriptor dealloc]
+ -[DVPDrawShapeFontDescriptor fontHeight]
+ -[DVPDrawShapeFontDescriptor fontName]
+ -[DVPDrawShapeFontDescriptor fontPixelBuffer]
+ -[DVPDrawShapeFontDescriptor fontTexture]
+ -[DVPDrawShapeFontDescriptor fontWidthArrayBuffer]
+ -[DVPDrawShapeFontDescriptor fontWidth]
+ -[DVPDrawShapeFontDescriptor initWithName:fontSize:metalContext:]
+ -[DVPDrawShapeFontDescriptor setFontHeight:]
+ -[DVPDrawShapeFontDescriptor setFontName:]
+ -[DVPDrawShapeFontDescriptor setFontPixelBuffer:]
+ -[DVPDrawShapeFontDescriptor setFontTexture:]
+ -[DVPDrawShapeFontDescriptor setFontWidth:]
+ -[DVPDrawShapeFontDescriptor setFontWidthArrayBuffer:]
+ -[DVPDrawShapeGPU .cxx_destruct]
+ -[DVPDrawShapeGPU _addLine:inTexture:toVertexBufferPtr:]
+ -[DVPDrawShapeGPU _addQuad:color:toVertexBuffer:]
+ -[DVPDrawShapeGPU _addRect:inTexture:toVertexBuffer:]
+ -[DVPDrawShapeGPU _initShaders]
+ -[DVPDrawShapeGPU _metalPixelFormatFor:]
+ -[DVPDrawShapeGPU _populateAvailableFonts]
+ -[DVPDrawShapeGPU addLineFrom:to:color:]
+ -[DVPDrawShapeGPU addRectangle:color:]
+ -[DVPDrawShapeGPU addTextLine:color:scale:]
+ -[DVPDrawShapeGPU alpha]
+ -[DVPDrawShapeGPU autoScaleIfTooWide]
+ -[DVPDrawShapeGPU availableFonts]
+ -[DVPDrawShapeGPU bindPixelBufferAsTexture:]
+ -[DVPDrawShapeGPU bindPixelBufferAsTexture:].cold.1
+ -[DVPDrawShapeGPU drawEnqueuedTextOnPixelBuffer:]
+ -[DVPDrawShapeGPU drawEnqueuedTextOnPixelBuffer:].cold.1
+ -[DVPDrawShapeGPU drawEnqueuedTextOnTexture:]
+ -[DVPDrawShapeGPU drawLinesOnPixelBuffer:]
+ -[DVPDrawShapeGPU drawLinesOnPixelBuffer:].cold.1
+ -[DVPDrawShapeGPU drawLinesOnTexture:commandBuffer:]
+ -[DVPDrawShapeGPU drawRectanglesOnPixelBuffer:]
+ -[DVPDrawShapeGPU drawRectanglesOnPixelBuffer:].cold.1
+ -[DVPDrawShapeGPU drawRectanglesOnTexture:commandBuffer:]
+ -[DVPDrawShapeGPU drawStyle]
+ -[DVPDrawShapeGPU drawText:pixelBuffer:color:position:scale:commandBuffer:]
+ -[DVPDrawShapeGPU drawText:pixelBuffer:color:position:scale:commandBuffer:].cold.1
+ -[DVPDrawShapeGPU drawText:texture:color:position:scale:commandBuffer:]
+ -[DVPDrawShapeGPU drawText:texture:color:position:scale:commandBuffer:].cold.1
+ -[DVPDrawShapeGPU drawText:texture:color:position:scale:commandBuffer:].cold.2
+ -[DVPDrawShapeGPU initWithOptionalCommandQueue:]
+ -[DVPDrawShapeGPU initWithOptionalCommandQueue:].cold.1
+ -[DVPDrawShapeGPU initWithOptionalCommandQueue:].cold.2
+ -[DVPDrawShapeGPU initWithOptionalCommandQueue:].cold.3
+ -[DVPDrawShapeGPU initialPosition]
+ -[DVPDrawShapeGPU popStates]
+ -[DVPDrawShapeGPU pushStates]
+ -[DVPDrawShapeGPU selectFont:fontSize:]
+ -[DVPDrawShapeGPU selectFont:fontSize:].cold.1
+ -[DVPDrawShapeGPU setAlpha:]
+ -[DVPDrawShapeGPU setAutoScaleIfTooWide:]
+ -[DVPDrawShapeGPU setDrawStyle:]
+ -[DVPDrawShapeGPU setInitialPosition:]
+ -[DVPDrawShapeGPU setStrokeWidth:]
+ -[DVPDrawShapeGPU strokeWidth]
+ -[DVPLensFlareMitigationParameters debugTrackBuffer]
+ -[DVPLensFlareMitigationParameters initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:debugTrackBuffer:]
+ -[DenseUpscaler .cxx_destruct]
+ -[DenseUpscaler EnableGpuWaitForComplete]
+ -[DenseUpscaler dealloc]
+ -[DenseUpscaler finishProcessing]
+ -[DenseUpscaler imageGuideUpscale]
+ -[DenseUpscaler initWithDevice:commandQueue:type:]
+ -[DenseUpscaler initWithType:]
+ -[DenseUpscaler processWithLowResTexture:guideImage:destination:error:]
+ -[DenseUpscaler setEnableGpuWaitForComplete:]
+ -[DenseUpscaler setImageGuideUpscale:]
+ -[DenseUpscaler startSessionWithLowResWidth:lowResHeight:highResWidth:highResHeight:error:]
+ -[DenseUpscaler type]
+ -[DenseUpscalerProcessor .cxx_destruct]
+ -[DenseUpscalerProcessor EnableGpuWaitForComplete]
+ -[DenseUpscalerProcessor dealloc]
+ -[DenseUpscalerProcessor finishProcessing]
+ -[DenseUpscalerProcessor imageGuideUpscale]
+ -[DenseUpscalerProcessor initWithSourceWidth:sourceHeight:destinationWidth:destinationHeight:type:]
+ -[DenseUpscalerProcessor processWithDenseUpscalerParams:error:]
+ -[DenseUpscalerProcessor setEnableGpuWaitForComplete:]
+ -[DenseUpscalerProcessor setImageGuideUpscale:]
+ -[DenseUpscalerProcessor startSessionWithDenseUpscalerConfig:error:]
+ -[FRNet convertBuffer:toOutputBuffer:outputAttachment:rotationMethod:crop:waitForCompletion:]
+ -[FRNet convertToRGB:to:rotate:]
+ -[FRNet getColorConsistentOutputRGBVia:currentRGB:attachment:destinationFrame:]
+ -[FlowUpscale channelCount]
+ -[FlowUpscale setChannelCount:]
+ -[GGMController processSourceFrame:nextFrame:forwardFlow:backwardFlow:ourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:randomAccessMode:destinationFrame:debugTrackBuffer:]
+ -[GGMMetalToolBox encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.6
+ -[GGMMetalToolBox encodeAlignBgAvgForMotionEstYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:]
+ -[GGMMetalToolBox encodeAlignBgAvgForMotionEstYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeAlignBgAvgForMotionEstYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeAlignBgAvgForMotionEstYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeAlignBgAvgForMotionEstYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeAlignBgAvgForMotionEstYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.5
+ -[GGMMetalToolBox encodeCollectClusterMaxAndAvgLuma:clusterMetaBuf:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeCollectClusterMaxProb:clusterMetaBuf:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeCollectClusterMv:clusterMetaBuf:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeCollectClusterMvForMotionCueToCommandEncoder:clusterMetaBuf:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeCollectClusterOverlapWithRefs:clusterMetaBuf:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeCollectClusterRepairError:clusterMetaBuf:metaBuf:metaForTrackingBuf:]
+ -[GGMMetalToolBox encodeCollectClusterRepairError:clusterMetaBuf:metaBuf:metaForTrackingBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectClusterRepairError:clusterMetaBuf:metaBuf:metaForTrackingBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectClusterRepairError:clusterMetaBuf:metaBuf:metaForTrackingBuf:].cold.3
+ -[GGMMetalToolBox encodeCollectClusterRepairError:clusterMetaBuf:metaBuf:metaForTrackingBuf:].cold.4
+ -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:metaForTrackingBuf:]
+ -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:metaForTrackingBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:metaForTrackingBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:metaForTrackingBuf:].cold.3
+ -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:metaForTrackingBuf:].cold.4
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:roiAvoidList:]
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:roiAvoidList:].cold.1
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:roiAvoidList:].cold.2
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:roiAvoidList:].cold.3
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:roiAvoidList:].cold.4
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:roiAvoidList:].cold.5
+ -[GGMMetalToolBox encodeCollectMvToFuture:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectOpticalCenterEstStats:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeCollectOpticalCenterEstStats:clusterMetaBuf:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectOpticalCenterEstStats:clusterMetaBuf:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:]
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.1
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.10
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.11
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.12
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.13
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.14
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.2
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.3
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.4
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.5
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.6
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.7
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.8
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:].cold.9
+ -[GGMMetalToolBox encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:].cold.5
+ -[GGMMetalToolBox encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:].cold.6
+ -[GGMMetalToolBox encodeConvertYUVToRGBToCommandEncoder:input:output:]
+ -[GGMMetalToolBox encodeConvertYUVToRGBToCommandEncoder:input:output:].cold.1
+ -[GGMMetalToolBox encodeConvertYUVToRGBToCommandEncoder:input:output:].cold.2
+ -[GGMMetalToolBox encodeConvertYUVToRGBToCommandEncoder:input:output:].cold.3
+ -[GGMMetalToolBox encodeCopyCurrMetaForProcFuture:metaBuf:outMetaBuf:].cold.3
+ -[GGMMetalToolBox encodeCopyFullFrameMapToMap4RoiGenToCommandEncoder:input:output:].cold.3
+ -[GGMMetalToolBox encodeCopyMapToMap4RoiGenToCommandEncoder:input:output:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:].cold.7
+ -[GGMMetalToolBox encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:].cold.7
+ -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationRadius:softDilationRadius:meta:]
+ -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationRadius:softDilationRadius:meta:].cold.1
+ -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationRadius:softDilationRadius:meta:].cold.2
+ -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationRadius:softDilationRadius:meta:].cold.3
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:outputForFutureRefTexture:metaBuf:]
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:outputForFutureRefTexture:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:outputForFutureRefTexture:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:outputForFutureRefTexture:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:outputForFutureRefTexture:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:outputForFutureRefTexture:metaBuf:].cold.5
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:outputForFutureRefTexture:metaBuf:].cold.6
+ -[GGMMetalToolBox encodeGetBgAvgForMotionEstYUVToCommandEncoder:target:ref0:ref1:probMap:meta:]
+ -[GGMMetalToolBox encodeGetBgAvgForMotionEstYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetBgAvgForMotionEstYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetBgAvgForMotionEstYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetBgAvgForMotionEstYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.4
+ -[GGMMetalToolBox encodeGetBgAvgForMotionEstYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.5
+ -[GGMMetalToolBox encodeGetBgAvgForMotionEstYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.6
+ -[GGMMetalToolBox encodeGetColorSimilarity:inputYUV:warpedRefYUV:colorSimilarityMap:meta:]
+ -[GGMMetalToolBox encodeGetColorSimilarity:inputYUV:warpedRefYUV:colorSimilarityMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetColorSimilarity:inputYUV:warpedRefYUV:colorSimilarityMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetColorSimilarity:inputYUV:warpedRefYUV:colorSimilarityMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetColorSimilarity:inputYUV:warpedRefYUV:colorSimilarityMap:meta:].cold.4
+ -[GGMMetalToolBox encodeGetColorSimilarity:inputYUV:warpedRefYUV:colorSimilarityMap:meta:].cold.5
+ -[GGMMetalToolBox encodeGetDiffToBg:inputYUV:reflLsMap:segMap:diffToBgMap:meta:]
+ -[GGMMetalToolBox encodeGetDiffToBg:inputYUV:reflLsMap:segMap:diffToBgMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetDiffToBg:inputYUV:reflLsMap:segMap:diffToBgMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetDiffToBg:inputYUV:reflLsMap:segMap:diffToBgMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetDiffToBg:inputYUV:reflLsMap:segMap:diffToBgMap:meta:].cold.4
+ -[GGMMetalToolBox encodeGetDiffToBg:inputYUV:reflLsMap:segMap:diffToBgMap:meta:].cold.5
+ -[GGMMetalToolBox encodeGetDiffToBg:inputYUV:reflLsMap:segMap:diffToBgMap:meta:].cold.6
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:diffToBgMap:isInitFrame:probMap:meta:]
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:diffToBgMap:isInitFrame:probMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:diffToBgMap:isInitFrame:probMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:diffToBgMap:isInitFrame:probMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:diffToBgMap:isInitFrame:probMap:meta:].cold.4
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:diffToBgMap:isInitFrame:probMap:meta:].cold.5
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:diffToBgMap:isInitFrame:probMap:meta:].cold.6
+ -[GGMMetalToolBox encodeGetLsMapYUVProxyToCommandEncoder:input:map:]
+ -[GGMMetalToolBox encodeGetLsMapYUVProxyToCommandEncoder:input:map:].cold.1
+ -[GGMMetalToolBox encodeGetLsMapYUVProxyToCommandEncoder:input:map:].cold.2
+ -[GGMMetalToolBox encodeGetLsMapYUVProxyToCommandEncoder:input:map:].cold.3
+ -[GGMMetalToolBox encodeGetLsMapYUVToCommandEncoder:input:map:].cold.3
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:avgAlignedRef:target:motionMap:meta:]
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:avgAlignedRef:target:motionMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:avgAlignedRef:target:motionMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:avgAlignedRef:target:motionMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:avgAlignedRef:target:motionMap:meta:].cold.4
+ -[GGMMetalToolBox encodeGetMvForMotionCueFromMvf:fullResInput:meta:mvf:opticalCenter:refOpticalCenter:].cold.3
+ -[GGMMetalToolBox encodeGetMvForMotionCueFromMvf:fullResInput:meta:mvf:opticalCenter:refOpticalCenter:].cold.4
+ -[GGMMetalToolBox encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:].cold.5
+ -[GGMMetalToolBox encodeGetMvToFutureFromMvf:fullResInput:meta:mvf:].cold.4
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:]
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.1
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.10
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.11
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.2
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.3
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.4
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.5
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.6
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.7
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.8
+ -[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:].cold.9
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:spaProbMap:lsMap:metaBuf:]
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:spaProbMap:lsMap:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:spaProbMap:lsMap:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:spaProbMap:lsMap:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:spaProbMap:lsMap:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:spaProbMap:lsMap:metaBuf:].cold.5
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:spaProbMap:lsMap:metaBuf:].cold.6
+ -[GGMMetalToolBox encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:]
+ -[GGMMetalToolBox encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:].cold.1
+ -[GGMMetalToolBox encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:].cold.2
+ -[GGMMetalToolBox encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:].cold.3
+ -[GGMMetalToolBox encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:].cold.4
+ -[GGMMetalToolBox encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:].cold.5
+ -[GGMMetalToolBox encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:].cold.6
+ -[GGMMetalToolBox encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:].cold.7
+ -[GGMMetalToolBox encodeGetRoiBgAvgYUVToCommandEncoder:target:ref0:meta:metaRef0:]
+ -[GGMMetalToolBox encodeGetRoiBgAvgYUVToCommandEncoder:target:ref0:meta:metaRef0:].cold.1
+ -[GGMMetalToolBox encodeGetRoiBgAvgYUVToCommandEncoder:target:ref0:meta:metaRef0:].cold.2
+ -[GGMMetalToolBox encodeGetRoiBgAvgYUVToCommandEncoder:target:ref0:meta:metaRef0:].cold.3
+ -[GGMMetalToolBox encodeGetRoiBgAvgYUVToCommandEncoder:target:ref0:meta:metaRef0:].cold.4
+ -[GGMMetalToolBox encodeGetRoiBgAvgYUVToCommandEncoder:target:ref0:meta:metaRef0:].cold.5
+ -[GGMMetalToolBox encodeGetRoiMaxAndAvgLumaYUV:target:lsMap:meta:].cold.4
+ -[GGMMetalToolBox encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:].cold.6
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:]
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:].cold.1
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:].cold.2
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:].cold.3
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:].cold.4
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:].cold.5
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:].cold.6
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:].cold.7
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:].cold.8
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:].cold.9
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:avgAlignedRef:output:refOutput:avgAlignedRefOutput:metaBuf:processedFrameCount:]
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:avgAlignedRef:output:refOutput:avgAlignedRefOutput:metaBuf:processedFrameCount:].cold.1
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:avgAlignedRef:output:refOutput:avgAlignedRefOutput:metaBuf:processedFrameCount:].cold.2
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:avgAlignedRef:output:refOutput:avgAlignedRefOutput:metaBuf:processedFrameCount:].cold.3
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:avgAlignedRef:output:refOutput:avgAlignedRefOutput:metaBuf:processedFrameCount:].cold.4
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:avgAlignedRef:output:refOutput:avgAlignedRefOutput:metaBuf:processedFrameCount:].cold.5
+ -[GGMMetalToolBox encodeRefineProbMapWithSpatialRepairedToEncoder:input:spaRepaired:inputMap:output:meta:]
+ -[GGMMetalToolBox encodeRefineProbMapWithSpatialRepairedToEncoder:input:spaRepaired:inputMap:output:meta:].cold.1
+ -[GGMMetalToolBox encodeRefineProbMapWithSpatialRepairedToEncoder:input:spaRepaired:inputMap:output:meta:].cold.2
+ -[GGMMetalToolBox encodeRefineProbMapWithSpatialRepairedToEncoder:input:spaRepaired:inputMap:output:meta:].cold.3
+ -[GGMMetalToolBox encodeRefineProbMapWithSpatialRepairedToEncoder:input:spaRepaired:inputMap:output:meta:].cold.4
+ -[GGMMetalToolBox encodeRefineProbMapWithSpatialRepairedToEncoder:input:spaRepaired:inputMap:output:meta:].cold.5
+ -[GGMMetalToolBox encodeRefineProbMapWithSpatialRepairedToEncoder:input:spaRepaired:inputMap:output:meta:].cold.6
+ -[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:]
+ -[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:].cold.1
+ -[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:].cold.2
+ -[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:].cold.3
+ -[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:].cold.4
+ -[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:].cold.5
+ -[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:].cold.6
+ -[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:].cold.7
+ -[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:].cold.8
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:rawProbMap4Spatial:probMap4Spatial:spatialOutput:metaBuf:]
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:rawProbMap4Spatial:probMap4Spatial:spatialOutput:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:rawProbMap4Spatial:probMap4Spatial:spatialOutput:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:rawProbMap4Spatial:probMap4Spatial:spatialOutput:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:rawProbMap4Spatial:probMap4Spatial:spatialOutput:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeSyncStats:clusterMeta:meta:]
+ -[GGMMetalToolBox encodeSyncStats:clusterMeta:meta:].cold.1
+ -[GGMMetalToolBox encodeSyncStats:clusterMeta:meta:].cold.2
+ -[GGMMetalToolBox encodeSyncStats:clusterMeta:meta:].cold.3
+ -[GGMMetalToolBox encodeSyncWeightsOriginal:clusterMetaBuf:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeUpdateEstOpticalCenterOffset:meta:]
+ -[GGMMetalToolBox encodeUpdateEstOpticalCenterOffset:meta:].cold.1
+ -[GGMMetalToolBox encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:].cold.7
+ -[GGMMetalToolBox encodeUpscaleThenReflectLsMap:input:normalizedCenter:output:].cold.3
+ -[GGMMetalToolBox encodeVisualizeMvfToCommandEncoder:fullResTarget:mvf:outMvf:meta:].cold.5
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:].cold.7
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.6
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:roiAvoidList:currTrackId:]
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:roiAvoidList:currTrackId:].cold.1
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:roiAvoidList:currTrackId:].cold.2
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:roiAvoidList:currTrackId:].cold.3
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:roiAvoidList:currTrackId:].cold.4
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:roiAvoidList:currTrackId:].cold.5
+ -[GGMMetalToolBox encodeWarpRefMetaLite:refMetaBuf:outMetaBuf:].cold.3
+ -[GGMMetalToolBox encodeblendOriginalAndLRBufToCommandEncoder:MitigatedBuf:inputCopyOrg:output:meta:]
+ -[GGMMetalToolBox encodeblendOriginalAndLRBufToCommandEncoder:MitigatedBuf:inputCopyOrg:output:meta:].cold.1
+ -[GGMMetalToolBox encodeblendOriginalAndLRBufToCommandEncoder:MitigatedBuf:inputCopyOrg:output:meta:].cold.2
+ -[GGMMetalToolBox encodeblendOriginalAndLRBufToCommandEncoder:MitigatedBuf:inputCopyOrg:output:meta:].cold.3
+ -[GGMMetalToolBox initWithMetalContext:commandQueue:tuningParamDict:fastMode:]
+ -[GGMMetalToolBox initWithMetalContext:commandQueue:tuningParamDict:fastMode:].cold.1
+ -[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:ispBaseOpticalCenter:opticalCenterEstConf:opticalCenterShift:frameDim:]
+ -[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:ispBaseOpticalCenter:opticalCenterEstConf:opticalCenterShift:frameDim:].cold.1
+ -[ISRNet allocateOutputBufferObjects]
+ -[ISRNet allocateOutputBufferObjects].cold.1
+ -[ISRNet allocateOutputBufferObjects].cold.2
+ -[ISRNet allocateOutputBufferObjects].cold.3
+ -[ISRNet getOutputPortNames]
+ -[ISRNet getOutputPortNames].cold.1
+ -[ISRNet getOutputPortNames].cold.2
+ -[ISRNet initializeOutputPorts]
+ -[ISRNet outputSurface]
+ -[ISRNet setOutputSurface:]
+ -[ImageSR tileProcessor]
+ -[MitigationANE dl_inpaint_tile_height]
+ -[MitigationANE dl_inpaint_tile_width]
+ -[OFNormalization convertFP16IOSurface:toRGBBuffer:]
+ -[OFNormalization convertRGBBuffer:toFP16IOSurface:]
+ -[OFNormalization copyRGBBuffer:toTextureArray:]
+ -[OFNormalization encodeCopyRGBBufferToCommandBuffer:source:destination:]
+ -[OFNormalization encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:outputY:outputUV:]
+ -[OFNormalization encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:outputY:outputUV:].cold.1
+ -[OFNormalization postprocessSRFrame:bicubicYUV:outputYUV:]
+ -[TileProcessor .cxx_destruct]
+ -[TileProcessor allocateBuffers]
+ -[TileProcessor calculatePaddedDimensions]
+ -[TileProcessor computeTileLayoutForDimension:numTiles:tileStart:effectiveStart:effectiveEnd:dimName:]
+ -[TileProcessor computeTileLayoutForDimension:numTiles:tileStart:effectiveStart:effectiveEnd:dimName:].cold.1
+ -[TileProcessor createMetalBufferFromArray:]
+ -[TileProcessor createTextureForBuffers]
+ -[TileProcessor dealloc]
+ -[TileProcessor encodeExtractTile:FromTexture:ToCommandBuffer:x0:y0:]
+ -[TileProcessor encodeWriteTileToOutputToCommandBuffer:tile:output:tileI:tileJ:]
+ -[TileProcessor extractTileFromTexture:x:y:]
+ -[TileProcessor getInputFrameSizeForWidth:Height:]
+ -[TileProcessor highResPaddedHeight]
+ -[TileProcessor highResPaddedWidth]
+ -[TileProcessor initWithInputWidth:inputHeight:scaleFactor:tileSize:overlapSize:pixelFormat:]
+ -[TileProcessor inputHeight]
+ -[TileProcessor inputWidth]
+ -[TileProcessor lowResPaddedHeight]
+ -[TileProcessor lowResPaddedWidth]
+ -[TileProcessor numTilesHeight]
+ -[TileProcessor numTilesWidth]
+ -[TileProcessor overlapSize]
+ -[TileProcessor precomputeTileLayout]
+ -[TileProcessor processSuperResolutionInputBuffer:outputBuffer:withISRNet:]
+ -[TileProcessor releaseBuffers]
+ -[TileProcessor releaseBuffers].cold.1
+ -[TileProcessor scaleFactor]
+ -[TileProcessor setupKernels]
+ -[TileProcessor stride]
+ -[TileProcessor tileEffectiveX0]
+ -[TileProcessor tileEffectiveX1]
+ -[TileProcessor tileEffectiveY0]
+ -[TileProcessor tileEffectiveY1]
+ -[TileProcessor tileSize]
+ -[TileProcessor tileX0]
+ -[TileProcessor tileY0]
+ -[TileProcessor writeTile:toOutput:tileI:tileJ:]
+ -[Upsampler encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:useBGROrdinal:]
+ -[Upsampler fillTexture:withValue:]
+ -[Upsampler upsampleRBGPackedBuffer:toUpsampledTexture:scaleFactor:useBGROrdinal:]
+ -[VDGDetectionUtilsV2 _normalizeCGRect:width:height:]
+ -[VDGDetectionUtilsV2 drawDebugOverlaysOnPixelBuffer:ghostRoiList:]
+ -[VDGDetectionUtilsV2 getDetectionRoiListFromMeta:outputArray:].cold.4
+ -[VDGDetectionUtilsV2 getDetectionRoiListFromMeta:outputArray:].cold.5
+ -[VDGDetectionUtilsV2 getDetectionRoiListFromMeta:outputArray:].cold.6
+ -[VDGDetectionUtilsV2 setupDrawShapesGPU]
+ -[VEMetalBase createKernel:constantValues:threadGroupSizeIsAligned:]
+ -[VEMetalBase createKernel:constantValues:threadGroupSizeIsAligned:].cold.1
+ -[VEMetalBase createKernel:constantValues:threadGroupSizeIsAligned:].cold.2
+ -[VEMobileAsset .cxx_destruct]
+ -[VEMobileAsset dealloc]
+ -[VEMobileAsset endLock]
+ -[VEMobileAsset endLock].cold.1
+ -[VEMobileAsset endLock].cold.2
+ -[VEMobileAsset endLock].cold.3
+ -[VEMobileAsset initWithAssetType:assetSpecifier:forClientName:]
+ -[VEMobileAsset initWithAssetType:assetSpecifier:forClientName:].cold.1
+ -[VEMobileAsset lockAndGetLocalAssetURL]
+ -[VEMobileAsset lockAndGetLocalAssetURL].cold.1
+ -[VEMobileAsset lockAndGetLocalAssetURL].cold.2
+ -[VEMobileAsset lockAndGetLocalAssetURL].cold.3
+ -[VEScaler transformAndPadSourceBuffer:destinationBuffer:rotate:waitForCompletion:]
+ -[VSRNet allocateOutputBufferObjects]
+ -[VSRNet allocateOutputBufferObjects].cold.1
+ -[VSRNet allocateOutputBufferObjects].cold.2
+ -[VSRNet allocateOutputBufferObjects].cold.3
+ -[VSRNet getOutputPortNames]
+ -[VSRNet getOutputPortNames].cold.1
+ -[VSRNet getOutputPortNames].cold.2
+ -[VSRNet initWithModelPath:inputWidth:inputHeight:currentLRSurface:warpedHRSurface:]
+ -[VSRNet initializeOutputPorts]
+ -[VSRNet processSuperResolutionToOutputBuffer:]
+ -[VideoDeghostingDetectionV2 _getProbMapInput:segMap:reflLs:trackingRef:trackingRefProb:trackingRefSpaProb:trackingRefLs:inputBuf:segMapBuf:reflLsBuf:trackingRefBuf:trackingRefProbBuf:trackingRefSpaProbBuf:trackingRefLsBuf:trackingMvf:metaBuf:metaBufArray:trackingRefMetaBuf:trackingRefOpticalCenter:probMap:rawRefinedProbMap:refinedProbMap:refinedReflLs:probMapStash4FutureTracking:probMapBuf:rawRefinedProbMapBuf:refinedProbMapBuf:refinedReflLsBuf:probMapStash4FutureTrackingBuf:doTracking:frameIndex:prevOpticalCenterEstConf:waitForComplete:]
+ -[VideoDeghostingDetectionV2 _initDetection:futureFrames:inputImgOrgBufFor4K:outputImgBufTMinus1:outputImgBufTMinus2:]
+ -[VideoDeghostingDetectionV2 _resetTrackingRoiAvoidList]
+ -[VideoDeghostingDetectionV2 doTrackingToNextFrameCurrMetaWithDetectionResults:currMetaWithMvToFuture:futureMeta:opticalCenter:futureOpticalCenter:useContainer0ForNextFrame:waitForComplete:]
+ -[VideoDeghostingDetectionV2 getProbMapsTarget:segMap:ref:rawProbMap:probMap:rawRefinedProbMap:refinedProbMap:reflLsMap:refinedReflLsMap:reflLsMap4TrackingRef:metaBuf:metaBufArray:refMetaBuf:trackingMvf:useRefProbMap:opticalCenter:trackingRefOpticalCenter:frameIndex:prevOpticalCenterEstConf:waitForComplete:]
+ -[VideoDeghostingDetectionV2 process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:debugTrackBuffer:]
+ -[VideoDeghostingDetectionV2 processHwLsMaskAndGetRoisOpticalCenter:inputFrame:prevMetaContainer:considerDist2PrevGhostWhenSort:outputMask:outputMaskTexture:outputReflectedMaskTexture:isLowLight:outputRoiList:]
+ -[VideoDeghostingDetectionV2 refineBboxProbMapForRoiGen:metaBuf:trackingRefMeta:pTrackId:filteredOpticalCenterShift:isInitFrame:success:]
+ -[VideoDeghostingDetectionV2 repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:rawRefinedProbMap:refinedProbMap:probMap4TrRefW:lsMap:metaBuf:outputForFutureRef:metaBufArray:forceToSpatial:waitForComplete:]
+ -[VideoDeghostingDetectionV2 segmentInput:metaBuf:metaBuf1:outputSegMap:outputSegAvgMap:ignoreRois:]
+ -[VideoDeghostingDetectionV2 segmentInput:pixelQueue:intoSegMap:avgMap:meta:meta1:ignoreRois:]
+ -[VideoDeghostingDetectionV2 segmentInput:pixelQueue:intoSegMap:avgMap:meta:meta1:ignoreRois:].cold.1
+ -[VideoDeghostingDetectionV2 segmentInput:pixelQueue:intoSegMap:avgMap:meta:meta1:ignoreRois:].cold.2
+ -[VideoDeghostingDetectionV2 segmentInput:pixelQueue:intoSegMap:avgMap:meta:meta1:ignoreRois:].cold.3
+ -[VideoDeghostingDetectionV2 segmentInput:pixelQueue:intoSegMap:avgMap:meta:meta1:ignoreRois:].cold.4
+ -[VideoDeghostingDetectionV2 segmentInput:pixelQueue:intoSegMap:avgMap:meta:meta1:ignoreRois:].cold.5
+ -[VideoDeghostingDetectionV2 segmentInput:pixelQueue:intoSegMap:avgMap:meta:meta1:ignoreRois:].cold.6
+ -[VideoDeghostingDetectionV2 unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:useContainer0ForNextFrame:outputFutureMetaBuf:prevOpticalCenterEstConf:]
+ -[VideoDeghostingDetectionV2 unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:useContainer0ForNextFrame:outputFutureMetaBuf:prevOpticalCenterEstConf:].cold.1
+ -[VideoDeghostingDetectionV2 updateRepairedRefYUVInput:opticalCenter:prob:rawRefinedProbMap:refinedProb:probMap4TrRefW:lsMap:frRef0:frRef1:outputForFutureRef:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:inputOrgBufFor4K:inputBuf:probBuf:rawRefinedProbBuf:refinedProbBuf:probMap4TrRefWBuf:lsMapBuf:frRef0Buf:frRef1Buf:outputForFutureRefBuf:nextFrameBuf:metaBuf:metaBufArray:forceToSpatial:waitForComplete:]
+ -[Warper computeErrorMaskForSourceRGB:referenceRGB:flow:outputErrorMask:threshold:scaleFactor:]
+ -[Warper encodeWarpBlendPreviousRGBToCommandBuffer:previousHR:withCurrentLR:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:destination:]
+ -[Warper warpBlendPreviousHRRGBTexture:withCurrentLRRGBTexture:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:toShuffledTexture:]
+ GCC_except_table25
+ GCC_except_table28
+ GCC_except_table8
+ _CFDictionaryGetValue
+ _CGBitmapContextCreate
+ _CGColorCreateGenericRGB
+ _CGContextConvertPointToDeviceSpace
+ _CGContextSetTextPosition
+ _CTFontCreateWithNameAndOptions
+ _CTFontGetSymbolicTraits
+ _CTFontManagerCopyAvailableFontFamilyNames
+ _CTLineCreateWithAttributedString
+ _CTLineDraw
+ _CTLineGetBoundsWithOptions
+ _IOSurfaceCreate
+ _IOSurfaceGetBytesPerRow
+ _OBJC_CLASS_$_DVPDenseUpscalerConfiguration
+ _OBJC_CLASS_$_DVPDenseUpscalerParameters
+ _OBJC_CLASS_$_DVPDrawShapeFontDescriptor
+ _OBJC_CLASS_$_DVPDrawShapeGPU
+ _OBJC_CLASS_$_DVPLineObj
+ _OBJC_CLASS_$_DVPRectObj
+ _OBJC_CLASS_$_DenseUpscaler
+ _OBJC_CLASS_$_DenseUpscalerProcessor
+ _OBJC_CLASS_$_MTLVertexDescriptor
+ _OBJC_CLASS_$_NSMutableAttributedString
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSProcessInfo
+ _OBJC_CLASS_$_TileProcessor
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._denseBufferPixelFormat
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._destinationHeight
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._destinationWidth
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._frameHeight
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._framePreferredPixelFormats
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._frameWidth
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._sourceHeight
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._sourceWidth
+ _OBJC_IVAR_$_DVPDenseUpscalerConfiguration._type
+ _OBJC_IVAR_$_DVPDenseUpscalerParameters._destinationFrame
+ _OBJC_IVAR_$_DVPDenseUpscalerParameters._guideFrame
+ _OBJC_IVAR_$_DVPDenseUpscalerParameters._sourceFrame
+ _OBJC_IVAR_$_DVPDrawShapeFontDescriptor._fontHeight
+ _OBJC_IVAR_$_DVPDrawShapeFontDescriptor._fontName
+ _OBJC_IVAR_$_DVPDrawShapeFontDescriptor._fontPixelBuffer
+ _OBJC_IVAR_$_DVPDrawShapeFontDescriptor._fontTexture
+ _OBJC_IVAR_$_DVPDrawShapeFontDescriptor._fontWidth
+ _OBJC_IVAR_$_DVPDrawShapeFontDescriptor._fontWidthArrayBuffer
+ _OBJC_IVAR_$_DVPDrawShapeFontDescriptor._metalContext
+ _OBJC_IVAR_$_DVPDrawShapeGPU._alpha
+ _OBJC_IVAR_$_DVPDrawShapeGPU._autoScaleIfTooWide
+ _OBJC_IVAR_$_DVPDrawShapeGPU._availableFonts
+ _OBJC_IVAR_$_DVPDrawShapeGPU._cachedFontDescriptors
+ _OBJC_IVAR_$_DVPDrawShapeGPU._computePipelineStates
+ _OBJC_IVAR_$_DVPDrawShapeGPU._drawRectangleRenderPipelineStates
+ _OBJC_IVAR_$_DVPDrawShapeGPU._drawStyle
+ _OBJC_IVAR_$_DVPDrawShapeGPU._initialPosition
+ _OBJC_IVAR_$_DVPDrawShapeGPU._linesToDraw
+ _OBJC_IVAR_$_DVPDrawShapeGPU._rectsToDraw
+ _OBJC_IVAR_$_DVPDrawShapeGPU._selectedFont
+ _OBJC_IVAR_$_DVPDrawShapeGPU._stateStack
+ _OBJC_IVAR_$_DVPDrawShapeGPU._strokeWidth
+ _OBJC_IVAR_$_DVPDrawShapeGPU._textLinesToDraw
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._debugTrackBuffer
+ _OBJC_IVAR_$_DVPLineObj.color
+ _OBJC_IVAR_$_DVPLineObj.end
+ _OBJC_IVAR_$_DVPLineObj.start
+ _OBJC_IVAR_$_DVPLineObj.strokeWidth
+ _OBJC_IVAR_$_DVPRectObj.color
+ _OBJC_IVAR_$_DVPRectObj.filled
+ _OBJC_IVAR_$_DVPRectObj.origin
+ _OBJC_IVAR_$_DVPRectObj.size
+ _OBJC_IVAR_$_DVPRectObj.strokeWidth
+ _OBJC_IVAR_$_DenseUpscaler._EnableGpuWaitForComplete
+ _OBJC_IVAR_$_DenseUpscaler._commandQueue
+ _OBJC_IVAR_$_DenseUpscaler._device
+ _OBJC_IVAR_$_DenseUpscaler._flowUpscale
+ _OBJC_IVAR_$_DenseUpscaler._hrHeight
+ _OBJC_IVAR_$_DenseUpscaler._hrWidth
+ _OBJC_IVAR_$_DenseUpscaler._imageGuideUpscale
+ _OBJC_IVAR_$_DenseUpscaler._lrHeight
+ _OBJC_IVAR_$_DenseUpscaler._lrWidth
+ _OBJC_IVAR_$_DenseUpscaler._sessionActive
+ _OBJC_IVAR_$_DenseUpscaler._type
+ _OBJC_IVAR_$_DenseUpscalerProcessor._EnableGpuWaitForComplete
+ _OBJC_IVAR_$_DenseUpscalerProcessor._commandQueue
+ _OBJC_IVAR_$_DenseUpscalerProcessor._denseUpscaler
+ _OBJC_IVAR_$_DenseUpscalerProcessor._destinationHeight
+ _OBJC_IVAR_$_DenseUpscalerProcessor._destinationWidth
+ _OBJC_IVAR_$_DenseUpscalerProcessor._device
+ _OBJC_IVAR_$_DenseUpscalerProcessor._frameHeight
+ _OBJC_IVAR_$_DenseUpscalerProcessor._frameWidth
+ _OBJC_IVAR_$_DenseUpscalerProcessor._imageGuideUpscale
+ _OBJC_IVAR_$_DenseUpscalerProcessor._sessionActive
+ _OBJC_IVAR_$_DenseUpscalerProcessor._sourceHeight
+ _OBJC_IVAR_$_DenseUpscalerProcessor._sourceWidth
+ _OBJC_IVAR_$_DenseUpscalerProcessor._textureCache
+ _OBJC_IVAR_$_DenseUpscalerProcessor._type
+ _OBJC_IVAR_$_FRNet._currPaddedLRRGBSurface
+ _OBJC_IVAR_$_FRNet._currPaddedLRRGBTexture
+ _OBJC_IVAR_$_FRNet._currentLRRGBTexture
+ _OBJC_IVAR_$_FRNet._highResRGBBuffer
+ _OBJC_IVAR_$_FRNet._highResRGBTexture
+ _OBJC_IVAR_$_FRNet._mobileAssetLock
+ _OBJC_IVAR_$_FRNet._previousLRRGB
+ _OBJC_IVAR_$_FRNet._rghaPixelFormat
+ _OBJC_IVAR_$_FRNet._warpedHRRGBSurface
+ _OBJC_IVAR_$_FRNet._warpedHRRGBTexture
+ _OBJC_IVAR_$_FlowUpscale._channelCount
+ _OBJC_IVAR_$_GGMController._fastMode
+ _OBJC_IVAR_$_GGMMetalToolBox._alignBgAvgForMotionEstYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._blendOriginalAndLRBuf
+ _OBJC_IVAR_$_GGMMetalToolBox._collectClusterRepairError
+ _OBJC_IVAR_$_GGMMetalToolBox._collectOpticalCenterEstStats
+ _OBJC_IVAR_$_GGMMetalToolBox._convertYUVToRGB
+ _OBJC_IVAR_$_GGMMetalToolBox._fastMode
+ _OBJC_IVAR_$_GGMMetalToolBox._fastModeSf
+ _OBJC_IVAR_$_GGMMetalToolBox._getBgAvgForMotionEstYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._getColorSimilarity
+ _OBJC_IVAR_$_GGMMetalToolBox._getDiffToBg
+ _OBJC_IVAR_$_GGMMetalToolBox._getLsMapYUVProxy
+ _OBJC_IVAR_$_GGMMetalToolBox._getOcclusionMap
+ _OBJC_IVAR_$_GGMMetalToolBox._getRepairErrYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._getRoiBgAvgYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._refineProbMapWithSpatialRepaired
+ _OBJC_IVAR_$_GGMMetalToolBox._refineTrackedProbMap
+ _OBJC_IVAR_$_GGMMetalToolBox._syncStats
+ _OBJC_IVAR_$_GGMMetalToolBox._updateEstOpticalCenterOffset
+ _OBJC_IVAR_$_ISRNet._outputBufferObject
+ _OBJC_IVAR_$_ISRNet._outputPortName
+ _OBJC_IVAR_$_ISRNet._outputSurface
+ _OBJC_IVAR_$_ISRNet._output_port
+ _OBJC_IVAR_$_ImageSR._enableTiling
+ _OBJC_IVAR_$_ImageSR._mobileAssetLock
+ _OBJC_IVAR_$_ImageSR._modelInputHeight
+ _OBJC_IVAR_$_ImageSR._modelInputWidth
+ _OBJC_IVAR_$_ImageSR._tileProcessor
+ _OBJC_IVAR_$_ImageSR._tilingPixelFormat
+ _OBJC_IVAR_$_MitigationANE._mobileAssetLock
+ _OBJC_IVAR_$_TileProcessor._extractTileFromTextureKernel
+ _OBJC_IVAR_$_TileProcessor._highResPaddedHeight
+ _OBJC_IVAR_$_TileProcessor._highResPaddedWidth
+ _OBJC_IVAR_$_TileProcessor._hrOverlapSize
+ _OBJC_IVAR_$_TileProcessor._hrTile
+ _OBJC_IVAR_$_TileProcessor._hrTileSize
+ _OBJC_IVAR_$_TileProcessor._hrTileTexture
+ _OBJC_IVAR_$_TileProcessor._inputHeight
+ _OBJC_IVAR_$_TileProcessor._inputWidth
+ _OBJC_IVAR_$_TileProcessor._lowResPaddedHeight
+ _OBJC_IVAR_$_TileProcessor._lowResPaddedWidth
+ _OBJC_IVAR_$_TileProcessor._lrTile
+ _OBJC_IVAR_$_TileProcessor._lrTileTexture
+ _OBJC_IVAR_$_TileProcessor._numTilesHeight
+ _OBJC_IVAR_$_TileProcessor._numTilesWidth
+ _OBJC_IVAR_$_TileProcessor._overlapSize
+ _OBJC_IVAR_$_TileProcessor._scaleFactor
+ _OBJC_IVAR_$_TileProcessor._stride
+ _OBJC_IVAR_$_TileProcessor._tileEffectiveX0
+ _OBJC_IVAR_$_TileProcessor._tileEffectiveX0Buffer
+ _OBJC_IVAR_$_TileProcessor._tileEffectiveX1
+ _OBJC_IVAR_$_TileProcessor._tileEffectiveX1Buffer
+ _OBJC_IVAR_$_TileProcessor._tileEffectiveY0
+ _OBJC_IVAR_$_TileProcessor._tileEffectiveY0Buffer
+ _OBJC_IVAR_$_TileProcessor._tileEffectiveY1
+ _OBJC_IVAR_$_TileProcessor._tileEffectiveY1Buffer
+ _OBJC_IVAR_$_TileProcessor._tilePixelFormat
+ _OBJC_IVAR_$_TileProcessor._tileSize
+ _OBJC_IVAR_$_TileProcessor._tileX0
+ _OBJC_IVAR_$_TileProcessor._tileX0Buffer
+ _OBJC_IVAR_$_TileProcessor._tileY0
+ _OBJC_IVAR_$_TileProcessor._tileY0Buffer
+ _OBJC_IVAR_$_TileProcessor._writeTileToOutputKernel
+ _OBJC_IVAR_$_Upsampler._upsampleBGRToRGBKernel
+ _OBJC_IVAR_$_Upsampler._upsampleRGBToRGBKernel
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._debugOutputMode
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._drawShapesGPU
+ _OBJC_IVAR_$_VEMobileAsset._autoAsset
+ _OBJC_IVAR_$_VEMobileAsset._locked
+ _OBJC_IVAR_$_VSRNet._outputBufferObject
+ _OBJC_IVAR_$_VSRNet._outputPortName
+ _OBJC_IVAR_$_VSRNet._outputSurface
+ _OBJC_IVAR_$_VSRNet._output_port
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._4KMode
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedMotionRef
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedMotionRefTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRef4MotionCue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRef4MotionCueTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRefForMotionEst0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRefForMotionEst0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRefForMotionEst1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRefForMotionEst1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._backwarpedRefForOcclusionDet0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._backwarpedRefForOcclusionDet0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._backwarpedRefForOcclusionDet1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._backwarpedRefForOcclusionDet1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._concurrentQueueForSegMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._diffToBgMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._diffToBgMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedColorSimilarityMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedColorSimilarityMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedFusedProbMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedFusedProbMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedOcclusionMap0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedOcclusionMap0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedOcclusionMap1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedOcclusionMap1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dispatchGroupForSegMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._estOpticalCenterOffset
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._fastMode
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowOcclusionMapRef0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowOcclusionMapRef0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowOcclusionMapRef1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowOcclusionMapRef1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flow_input_height
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flow_input_width
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._frameDim
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._fusedProbMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._fusedProbMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._futureIspBaseOpticalCenter
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputCopy4KBuf
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputCopy4KTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputImgLRBuf
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputImgOrgTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputImgUpScaledBuf
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputImgUpScaledTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputRGB
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputRGBTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._opticalCenterEstConf
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._refinedProbForRepair
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._refinedProbForRepairTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._repairedRefQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._repairedRefTexQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._scaler
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._scalingFactor
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._segAvgMap0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._segAvgMap0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._segAvgMap1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._segAvgMap1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._segMap0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._segMap0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._segMap1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._segMap1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._segMapPixelQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._tmpMetaForBboxGen
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._trackingRoiAvoidListBuf
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedTrackingRef
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedTrackingRefTexture
+ _OBJC_IVAR_$_Warper._warpBlendShuffleRGBKernel
+ _OBJC_METACLASS_$_DVPDenseUpscalerConfiguration
+ _OBJC_METACLASS_$_DVPDenseUpscalerParameters
+ _OBJC_METACLASS_$_DVPDrawShapeFontDescriptor
+ _OBJC_METACLASS_$_DVPDrawShapeGPU
+ _OBJC_METACLASS_$_DVPLineObj
+ _OBJC_METACLASS_$_DVPRectObj
+ _OBJC_METACLASS_$_DenseUpscaler
+ _OBJC_METACLASS_$_DenseUpscalerProcessor
+ _OBJC_METACLASS_$_TileProcessor
+ _OUTLINED_FUNCTION_40
+ _OUTLINED_FUNCTION_41
+ _OUTLINED_FUNCTION_42
+ _OUTLINED_FUNCTION_43
+ __OBJC_$_CLASS_METHODS_DVPDenseUpscalerConfiguration
+ __OBJC_$_CLASS_METHODS_DenseUpscaler
+ __OBJC_$_CLASS_PROP_LIST_DVPLensFlareMitigationParameters
+ __OBJC_$_INSTANCE_METHODS_DVPDenseUpscalerConfiguration
+ __OBJC_$_INSTANCE_METHODS_DVPDenseUpscalerParameters
+ __OBJC_$_INSTANCE_METHODS_DVPDrawShapeFontDescriptor
+ __OBJC_$_INSTANCE_METHODS_DVPDrawShapeGPU
+ __OBJC_$_INSTANCE_METHODS_DenseUpscaler
+ __OBJC_$_INSTANCE_METHODS_DenseUpscalerProcessor
+ __OBJC_$_INSTANCE_METHODS_TileProcessor
+ __OBJC_$_INSTANCE_METHODS_VEMobileAsset
+ __OBJC_$_INSTANCE_VARIABLES_DVPDenseUpscalerConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_DVPDenseUpscalerParameters
+ __OBJC_$_INSTANCE_VARIABLES_DVPDrawShapeFontDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_DVPDrawShapeGPU
+ __OBJC_$_INSTANCE_VARIABLES_DVPLineObj
+ __OBJC_$_INSTANCE_VARIABLES_DVPRectObj
+ __OBJC_$_INSTANCE_VARIABLES_DenseUpscaler
+ __OBJC_$_INSTANCE_VARIABLES_DenseUpscalerProcessor
+ __OBJC_$_INSTANCE_VARIABLES_TileProcessor
+ __OBJC_$_INSTANCE_VARIABLES_VEMobileAsset
+ __OBJC_$_PROP_LIST_DVPDenseUpscalerConfiguration
+ __OBJC_$_PROP_LIST_DVPDenseUpscalerParameters
+ __OBJC_$_PROP_LIST_DVPDrawShapeFontDescriptor
+ __OBJC_$_PROP_LIST_DVPDrawShapeGPU
+ __OBJC_$_PROP_LIST_DenseUpscaler
+ __OBJC_$_PROP_LIST_DenseUpscalerProcessor
+ __OBJC_$_PROP_LIST_MitigationANE
+ __OBJC_$_PROP_LIST_TileProcessor
+ __OBJC_CLASS_PROTOCOLS_$_DVPDenseUpscalerConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_DVPDenseUpscalerParameters
+ __OBJC_CLASS_RO_$_DVPDenseUpscalerConfiguration
+ __OBJC_CLASS_RO_$_DVPDenseUpscalerParameters
+ __OBJC_CLASS_RO_$_DVPDrawShapeFontDescriptor
+ __OBJC_CLASS_RO_$_DVPDrawShapeGPU
+ __OBJC_CLASS_RO_$_DVPLineObj
+ __OBJC_CLASS_RO_$_DVPRectObj
+ __OBJC_CLASS_RO_$_DenseUpscaler
+ __OBJC_CLASS_RO_$_DenseUpscalerProcessor
+ __OBJC_CLASS_RO_$_TileProcessor
+ __OBJC_METACLASS_RO_$_DVPDenseUpscalerConfiguration
+ __OBJC_METACLASS_RO_$_DVPDenseUpscalerParameters
+ __OBJC_METACLASS_RO_$_DVPDrawShapeFontDescriptor
+ __OBJC_METACLASS_RO_$_DVPDrawShapeGPU
+ __OBJC_METACLASS_RO_$_DVPLineObj
+ __OBJC_METACLASS_RO_$_DVPRectObj
+ __OBJC_METACLASS_RO_$_DenseUpscaler
+ __OBJC_METACLASS_RO_$_DenseUpscalerProcessor
+ __OBJC_METACLASS_RO_$_TileProcessor
+ ___163-[VideoDeghostingDetectionV2 process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:debugTrackBuffer:]_block_invoke
+ ___190-[VideoDeghostingDetectionV2 doTrackingToNextFrameCurrMetaWithDetectionResults:currMetaWithMvToFuture:futureMeta:opticalCenter:futureOpticalCenter:useContainer0ForNextFrame:waitForComplete:]_block_invoke
+ ___261-[VideoDeghostingDetectionV2 repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:rawRefinedProbMap:refinedProbMap:probMap4TrRefW:lsMap:metaBuf:outputForFutureRef:metaBufArray:forceToSpatial:waitForComplete:]_block_invoke
+ ___261-[VideoDeghostingDetectionV2 repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:rawRefinedProbMap:refinedProbMap:probMap4TrRefW:lsMap:metaBuf:outputForFutureRef:metaBufArray:forceToSpatial:waitForComplete:]_block_invoke_2
+ ___block_descriptor_48_e8_32bs40r_e28_v16?0"<MTLCommandBuffer>"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40bs_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_98_e8_32s40s48s56s64r72r80r_e5_v8?0lr64l8s32l8r72l8r80l8s40l8s48l8s56l8
+ _createPlanar16HalfIOSurface
+ _createTextureViaPlanar16HalfIOSurface
+ _e5rt_buffer_object_create_from_iosurface
+ _kCTBackgroundColorAttributeName
+ _kCTFontAttributeName
+ _kCTForegroundColorAttributeName
+ _kCVImageBufferCGColorSpaceKey
+ _kIOSurfaceAllocSize
+ _kIOSurfaceBytesPerElement
+ _kIOSurfaceBytesPerRow
+ _kIOSurfaceHeight
+ _kIOSurfacePixelFormat
+ _kIOSurfaceWidth
+ _memoryUsageTabISR
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_getProbMapInput:segMap:reflLs:trackingRef:trackingRefProb:trackingRefSpaProb:trackingRefLs:inputBuf:segMapBuf:reflLsBuf:trackingRefBuf:trackingRefProbBuf:trackingRefSpaProbBuf:trackingRefLsBuf:trackingMvf:metaBuf:metaBufArray:trackingRefMetaBuf:trackingRefOpticalCenter:probMap:rawRefinedProbMap:refinedProbMap:refinedReflLs:probMapStash4FutureTracking:probMapBuf:rawRefinedProbMapBuf:refinedProbMapBuf:refinedReflLsBuf:probMapStash4FutureTrackingBuf:doTracking:frameIndex:prevOpticalCenterEstConf:waitForComplete:
+ _objc_msgSend$_initDetection:futureFrames:inputImgOrgBufFor4K:outputImgBufTMinus1:outputImgBufTMinus2:
+ _objc_msgSend$_normalizeCGRect:width:height:
+ _objc_msgSend$_resetTrackingRoiAvoidList
+ _objc_msgSend$addAttribute:value:range:
+ _objc_msgSend$addRectangle:color:
+ _objc_msgSend$addTextLine:color:scale:
+ _objc_msgSend$allocateBuffers
+ _objc_msgSend$attributes
+ _objc_msgSend$calculatePaddedDimensions
+ _objc_msgSend$channelCountForType:
+ _objc_msgSend$computeCommandEncoderWithDispatchType:
+ _objc_msgSend$computeErrorMaskForSourceRGB:referenceRGB:flow:outputErrorMask:threshold:scaleFactor:
+ _objc_msgSend$computeTileLayoutForDimension:numTiles:tileStart:effectiveStart:effectiveEnd:dimName:
+ _objc_msgSend$convertBuffer:toOutputBuffer:outputAttachment:rotationMethod:crop:waitForCompletion:
+ _objc_msgSend$convertFP16IOSurface:toRGBBuffer:
+ _objc_msgSend$convertRGBBuffer:toFP16IOSurface:
+ _objc_msgSend$convertToRGB:to:rotate:
+ _objc_msgSend$copyRGBBuffer:toTextureArray:
+ _objc_msgSend$createKernel:constantValues:threadGroupSizeIsAligned:
+ _objc_msgSend$createMetalBufferFromArray:
+ _objc_msgSend$createTextureForBuffers
+ _objc_msgSend$debugTrackBuffer
+ _objc_msgSend$destinationHeight
+ _objc_msgSend$destinationWidth
+ _objc_msgSend$dl_inpaint_tile_height
+ _objc_msgSend$dl_inpaint_tile_width
+ _objc_msgSend$doTrackingToNextFrameCurrMetaWithDetectionResults:currMetaWithMvToFuture:futureMeta:opticalCenter:futureOpticalCenter:useContainer0ForNextFrame:waitForComplete:
+ _objc_msgSend$drawDebugOverlaysOnPixelBuffer:ghostRoiList:
+ _objc_msgSend$drawEnqueuedTextOnPixelBuffer:
+ _objc_msgSend$drawEnqueuedTextOnTexture:
+ _objc_msgSend$drawLinesOnTexture:commandBuffer:
+ _objc_msgSend$drawRectanglesOnPixelBuffer:
+ _objc_msgSend$drawRectanglesOnTexture:commandBuffer:
+ _objc_msgSend$drawText:texture:color:position:scale:commandBuffer:
+ _objc_msgSend$encodeAlignBgAvgForMotionEstYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:
+ _objc_msgSend$encodeCollectClusterRepairError:clusterMetaBuf:metaBuf:metaForTrackingBuf:
+ _objc_msgSend$encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:metaForTrackingBuf:
+ _objc_msgSend$encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:roiAvoidList:
+ _objc_msgSend$encodeCollectOpticalCenterEstStats:clusterMetaBuf:metaBuf:
+ _objc_msgSend$encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:
+ _objc_msgSend$encodeConvertYUVToRGBToCommandEncoder:input:output:
+ _objc_msgSend$encodeCopyRGBBufferToCommandBuffer:source:destination:
+ _objc_msgSend$encodeDilateGrayImg:input:output:hardDilationRadius:softDilationRadius:meta:
+ _objc_msgSend$encodeExtractTile:FromTexture:ToCommandBuffer:x0:y0:
+ _objc_msgSend$encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:outputForFutureRefTexture:metaBuf:
+ _objc_msgSend$encodeGetBgAvgForMotionEstYUVToCommandEncoder:target:ref0:ref1:probMap:meta:
+ _objc_msgSend$encodeGetDiffToBg:inputYUV:reflLsMap:segMap:diffToBgMap:meta:
+ _objc_msgSend$encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:diffToBgMap:isInitFrame:probMap:meta:
+ _objc_msgSend$encodeGetLsMapYUVProxyToCommandEncoder:input:map:
+ _objc_msgSend$encodeGetMotionMapYUVToCommandEncoder:ref:avgAlignedRef:target:motionMap:meta:
+ _objc_msgSend$encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:
+ _objc_msgSend$encodeGetOverlapWithRefs:input:probMap:spaProbMap:lsMap:metaBuf:
+ _objc_msgSend$encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:
+ _objc_msgSend$encodeGetRoiBgAvgYUVToCommandEncoder:target:ref0:meta:metaRef0:
+ _objc_msgSend$encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:
+ _objc_msgSend$encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:outputY:outputUV:
+ _objc_msgSend$encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:avgAlignedRef:output:refOutput:avgAlignedRefOutput:metaBuf:processedFrameCount:
+ _objc_msgSend$encodeRefineProbMapWithSpatialRepairedToEncoder:input:spaRepaired:inputMap:output:meta:
+ _objc_msgSend$encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:
+ _objc_msgSend$encodeSpatialRepairYUVToCommandEncoder:input:rawProbMap4Spatial:probMap4Spatial:spatialOutput:metaBuf:
+ _objc_msgSend$encodeSyncStats:clusterMeta:meta:
+ _objc_msgSend$encodeUpdateEstOpticalCenterOffset:meta:
+ _objc_msgSend$encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:useBGROrdinal:
+ _objc_msgSend$encodeWarpBlendPreviousRGBToCommandBuffer:previousHR:withCurrentLR:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:destination:
+ _objc_msgSend$encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:roiAvoidList:currTrackId:
+ _objc_msgSend$encodeWriteTileToOutputToCommandBuffer:tile:output:tileI:tileJ:
+ _objc_msgSend$encodeblendOriginalAndLRBufToCommandEncoder:MitigatedBuf:inputCopyOrg:output:meta:
+ _objc_msgSend$endLock
+ _objc_msgSend$endLockUsageSync:
+ _objc_msgSend$environment
+ _objc_msgSend$extractTileFromTexture:x:y:
+ _objc_msgSend$fileExistsAtPath:isDirectory:
+ _objc_msgSend$fillTexture:withValue:
+ _objc_msgSend$firstObject
+ _objc_msgSend$fontHeight
+ _objc_msgSend$fontTexture
+ _objc_msgSend$fontWidth
+ _objc_msgSend$fontWidthArrayBuffer
+ _objc_msgSend$getColorConsistentOutputRGBVia:currentRGB:attachment:destinationFrame:
+ _objc_msgSend$getInputFrameSizeForWidth:Height:
+ _objc_msgSend$getProbMapsTarget:segMap:ref:rawProbMap:probMap:rawRefinedProbMap:refinedProbMap:reflLsMap:refinedReflLsMap:reflLsMap4TrackingRef:metaBuf:metaBufArray:refMetaBuf:trackingMvf:useRefProbMap:opticalCenter:trackingRefOpticalCenter:frameIndex:prevOpticalCenterEstConf:waitForComplete:
+ _objc_msgSend$getValue:
+ _objc_msgSend$guideFrame
+ _objc_msgSend$initImageWithValue:
+ _objc_msgSend$initWithAssetType:assetSpecifier:forClientName:
+ _objc_msgSend$initWithDevice:commandQueue:type:
+ _objc_msgSend$initWithInputWidth:inputHeight:scaleFactor:tileSize:overlapSize:pixelFormat:
+ _objc_msgSend$initWithMetalContext:commandQueue:tuningParamDict:fastMode:
+ _objc_msgSend$initWithModelPath:inputWidth:inputHeight:currentLRSurface:warpedHRSurface:
+ _objc_msgSend$initWithName:fontSize:metalContext:
+ _objc_msgSend$initWithOptionalCommandQueue:
+ _objc_msgSend$initializeOutputPorts
+ _objc_msgSend$interestInContentSync:
+ _objc_msgSend$lastObject
+ _objc_msgSend$layouts
+ _objc_msgSend$linearTextureAlignmentBytes
+ _objc_msgSend$linearTextureArrayAlignmentSlice
+ _objc_msgSend$lockAndGetLocalAssetURL
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$newComputePipelineStateWithFunction:error:
+ _objc_msgSend$null
+ _objc_msgSend$postprocessSRFrame:bicubicYUV:outputYUV:
+ _objc_msgSend$precomputeTileLayout
+ _objc_msgSend$process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:debugTrackBuffer:
+ _objc_msgSend$processHwLsMaskAndGetRoisOpticalCenter:inputFrame:prevMetaContainer:considerDist2PrevGhostWhenSort:outputMask:outputMaskTexture:outputReflectedMaskTexture:isLowLight:outputRoiList:
+ _objc_msgSend$processInfo
+ _objc_msgSend$processSourceFrame:nextFrame:forwardFlow:backwardFlow:ourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:randomAccessMode:destinationFrame:debugTrackBuffer:
+ _objc_msgSend$processSuperResolutionInputBuffer:outputBuffer:withISRNet:
+ _objc_msgSend$processSuperResolutionToOutputBuffer:
+ _objc_msgSend$processWithLowResTexture:guideImage:destination:error:
+ _objc_msgSend$refineBboxProbMapForRoiGen:metaBuf:trackingRefMeta:pTrackId:filteredOpticalCenterShift:isInitFrame:success:
+ _objc_msgSend$releaseBuffers
+ _objc_msgSend$removeLastObject
+ _objc_msgSend$repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:rawRefinedProbMap:refinedProbMap:probMap4TrRefW:lsMap:metaBuf:outputForFutureRef:metaBufArray:forceToSpatial:waitForComplete:
+ _objc_msgSend$segmentInput:metaBuf:metaBuf1:outputSegMap:outputSegAvgMap:ignoreRois:
+ _objc_msgSend$segmentInput:pixelQueue:intoSegMap:avgMap:meta:meta1:ignoreRois:
+ _objc_msgSend$selectFont:fontSize:
+ _objc_msgSend$setAlphaBlendOperation:
+ _objc_msgSend$setAutoScaleIfTooWide:
+ _objc_msgSend$setBlendingEnabled:
+ _objc_msgSend$setChannelCount:
+ _objc_msgSend$setDestinationAlphaBlendFactor:
+ _objc_msgSend$setDestinationRGBBlendFactor:
+ _objc_msgSend$setFormat:
+ _objc_msgSend$setFragmentBytes:length:atIndex:
+ _objc_msgSend$setInitialPosition:
+ _objc_msgSend$setOffset:
+ _objc_msgSend$setRgbBlendOperation:
+ _objc_msgSend$setSourceAlphaBlendFactor:
+ _objc_msgSend$setSourceRGBBlendFactor:
+ _objc_msgSend$setStepFunction:
+ _objc_msgSend$setStride:
+ _objc_msgSend$setVertexDescriptor:
+ _objc_msgSend$setupDrawShapesGPU
+ _objc_msgSend$sourceHeight
+ _objc_msgSend$sourceWidth
+ _objc_msgSend$startSessionWithLowResWidth:lowResHeight:highResWidth:highResHeight:error:
+ _objc_msgSend$tileSize
+ _objc_msgSend$transformAndPadSourceBuffer:destinationBuffer:rotate:waitForCompletion:
+ _objc_msgSend$type
+ _objc_msgSend$unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:useContainer0ForNextFrame:outputFutureMetaBuf:prevOpticalCenterEstConf:
+ _objc_msgSend$updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:ispBaseOpticalCenter:opticalCenterEstConf:opticalCenterShift:frameDim:
+ _objc_msgSend$updateRepairedRefYUVInput:opticalCenter:prob:rawRefinedProbMap:refinedProb:probMap4TrRefW:lsMap:frRef0:frRef1:outputForFutureRef:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:inputOrgBufFor4K:inputBuf:probBuf:rawRefinedProbBuf:refinedProbBuf:probMap4TrRefWBuf:lsMapBuf:frRef0Buf:frRef1Buf:outputForFutureRefBuf:nextFrameBuf:metaBuf:metaBufArray:forceToSpatial:waitForComplete:
+ _objc_msgSend$upsampleRBGPackedBuffer:toUpsampledTexture:scaleFactor:useBGROrdinal:
+ _objc_msgSend$warpBlendPreviousHRRGBTexture:withCurrentLRRGBTexture:viaLowResFlow:viaErrorMask:scaleFactor:effectiveOutputWidth:effectiveOutputHeight:toShuffledTexture:
+ _objc_msgSend$writeTile:toOutput:tileI:tileJ:
+ _objc_msgSend$writeValue:X:Y:Channel:
+ _objc_release_x11
+ _objc_retainAutoreleaseReturnValue
+ _objc_retainBlock
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
- +[VEMobileAsset endAllLocksWithAssetType:assetSpecifier:forClientName:]
- +[VEMobileAsset endAllLocksWithAssetType:assetSpecifier:forClientName:].cold.1
- +[VEMobileAsset endAllLocksWithAssetType:assetSpecifier:forClientName:].cold.2
- +[VEMobileAsset endAllLocksWithAssetType:assetSpecifier:forClientName:].cold.3
- +[VEMobileAsset getLocalMobileAssetURLWithAssetType:assetSpecifier:forClientName:]
- +[VEMobileAsset getLocalMobileAssetURLWithAssetType:assetSpecifier:forClientName:].cold.1
- -[DVPLensFlareMitigationParameters initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:]
- -[FRNet convertToRGB:to:withRGBFormat:rotate:]
- -[FRNet convertToRGB:to:withRGBFormat:rotate:].cold.1
- -[FRNet convertToYUV:attachment:].cold.1
- -[FRNet getColorConsistentOutputRGBVia:bicubicRGB:laplacianMask:attachment:destinationFrame:]
- -[FRNet setUseLaplacianMask:]
- -[FRNet useLaplacianMask]
- -[GGMController processSourceFrame:nextFrame:forwardFlow:backwardFlow:ourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:randomAccessMode:destinationFrame:]
- -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:]
- -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:].cold.1
- -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:].cold.2
- -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:]
- -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:].cold.1
- -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:].cold.2
- -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:].cold.3
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:]
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.1
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.10
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.11
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.12
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.13
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.14
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.15
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.2
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.3
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.4
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.5
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.6
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.7
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.8
- -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.9
- -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:]
- -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:].cold.1
- -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:].cold.2
- -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:].cold.3
- -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:].cold.4
- -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:]
- -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.1
- -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.2
- -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.3
- -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.4
- -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.5
- -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.6
- -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:]
- -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.1
- -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.2
- -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.3
- -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.4
- -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.5
- -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.6
- -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:]
- -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:].cold.1
- -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:].cold.2
- -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:].cold.3
- -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:].cold.4
- -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:]
- -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:].cold.1
- -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:].cold.2
- -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:].cold.3
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:]
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.1
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.10
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.11
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.2
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.3
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.4
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.5
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.6
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.7
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.8
- -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.9
- -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:]
- -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.1
- -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.2
- -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.3
- -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.4
- -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.5
- -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:]
- -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:].cold.1
- -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:].cold.2
- -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:].cold.3
- -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:].cold.4
- -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:]
- -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.1
- -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.2
- -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.3
- -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.4
- -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.5
- -[GGMMetalToolBox initWithMetalContext:commandQueue:tuningParamDict:]
- -[GGMMetalToolBox initWithMetalContext:commandQueue:tuningParamDict:].cold.1
- -[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:opticalCenterShift:]
- -[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:opticalCenterShift:].cold.1
- -[LoGFilter .cxx_destruct]
- -[LoGFilter createMaskFrom:to:]
- -[LoGFilter encodeDiffToCommandBuffer:texture0:texture1:]
- -[LoGFilter encodeToCommandBuffer:sourceTexture:destinationTexture:]
- -[LoGFilter encodeUpsampleScaleToCommandBuffer:sourceTexture:destinationTexture:]
- -[LoGFilter init]
- -[LoGFilter maskScaleFactor]
- -[LoGFilter maskStrength]
- -[LoGFilter setMaskScaleFactor:]
- -[LoGFilter setMaskStrength:]
- -[OFNormalization convertBuffer:toFP16IOSurface:]
- -[OFNormalization convertBuffer:toFP16ShuffledIOSurface:]
- -[OFNormalization convertFP16IOSurface:toBuffer:]
- -[OFNormalization denormalizeRGB:to:]
- -[OFNormalization encodeDenormalizeRGBToCommandBuffer:source:destination:]
- -[OFNormalization encodeNormalizationRGBToCommandBuffer:source:destination:]
- -[OFNormalization encodeNormalizeLumaToCommandBuffer:source:destination:]
- -[OFNormalization encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:laplacianMask:outputY:outputUV:]
- -[OFNormalization encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:laplacianMask:outputY:outputUV:].cold.1
- -[OFNormalization normalizeLumaFromFrame:toTexture:]
- -[OFNormalization normalizeRGB:to:]
- -[OFNormalization postprocessSRFrame:bicubicYUV:laplacianMask:outputYUV:]
- -[SPIFrameSynthesizer .cxx_destruct]
- -[SPIFrameSynthesizer allocateResources]
- -[SPIFrameSynthesizer flowHeight]
- -[SPIFrameSynthesizer flowWidth]
- -[SPIFrameSynthesizer initWithUsage:]
- -[SPIFrameSynthesizer initWithUsage:qualityMode:]
- -[SPIFrameSynthesizer initWithUsage:qualityMode:useLegacyNormalization:]
- -[SPIFrameSynthesizer isFirstFrameInStream]
- -[SPIFrameSynthesizer releaseResources]
- -[SPIFrameSynthesizer setFirstFrame:secondFrame:forwardFlow:backwardFlow:]
- -[SPIFrameSynthesizer setIsFirstFrameInStream:]
- -[SPIFrameSynthesizer setSpiInstance:]
- -[SPIFrameSynthesizer setStreamingMode:]
- -[SPIFrameSynthesizer spiInstance]
- -[SPIFrameSynthesizer streamingMode]
- -[SPIFrameSynthesizer synthesizeFrameForTimeScale:destination:]
- -[SPIFrameSynthesizer synthesizeFrameFromFirstFrame:secondFrame:forwardFlow:backwardFlow:timeScale:destination:]
- -[SPIFrameSynthesizer synthesizeFramesFromFirstFrame:secondFrame:forwardFlow:backwardFlow:numberOfFrames:withError:]
- -[SPIFrameSynthesizer synthesizeFramesFromFirstFrame:secondFrame:forwardFlow:backwardFlow:timeScales:withError:]
- -[SRNet allocateOutputBufferObjects]
- -[SRNet allocateOutputBufferObjects].cold.1
- -[SRNet allocateOutputBufferObjects].cold.2
- -[SRNet allocateOutputBufferObjects].cold.3
- -[SRNet getOutputPortNames]
- -[SRNet getOutputPortNames].cold.1
- -[SRNet getOutputPortNames].cold.2
- -[SRNet outputBufferObject]
- -[SRNet outputPortName]
- -[SRNet outputSurface]
- -[SRNet output_port]
- -[SRNet setOutputPortName:]
- -[SRNet setOutputSurface:]
- -[Upsampler encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:]
- -[Upsampler upsampleRBGPackedBuffer:to:scaleFactor:]
- -[VEMetalBase createKernel:constantValues:].cold.1
- -[VEMetalBase createKernel:constantValues:].cold.2
- -[VSRNet allocateInputBufferObjects]
- -[VSRNet allocateInputBufferObjects].cold.1
- -[VSRNet allocateInputBufferObjects].cold.2
- -[VSRNet allocateInputBufferObjects].cold.3
- -[VSRNet allocateInputBufferObjects].cold.4
- -[VSRNet allocateInputBufferObjects].cold.5
- -[VSRNet allocateInputBufferObjects].cold.6
- -[VSRNet allocateInputBufferObjects].cold.7
- -[VSRNet allocateInputBufferObjects].cold.8
- -[VSRNet initWithModelPath:inputWidth:inputHeight:]
- -[VSRNet inputSurface]
- -[VSRNet prevHRSurface]
- -[VSRNet processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:]
- -[VSRNet processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:].cold.1
- -[VSRNet processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:].cold.2
- -[VSRNet processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:].cold.3
- -[VSRNet setInputSurface:]
- -[VSRNet setPrevHRSurface:]
- -[VideoDeghostingDetectionV2 _getProbMapInput:reflLs:trackingRef:trackingRefProb:trackingRefSpaProb:trackingRefErrRescaleProb:trackingRefLs:inputBuf:reflLsBuf:trackingRefBuf:trackingRefProbBuf:trackingRefSpaProbBuf:trackingRefErrRescaleProbBuf:trackingRefLsBuf:trackingMvf:metaBuf:metaBufArray:trackingRefMetaBuf:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:refinedReflLs:probMapStash4FutureTracking:probMapBuf:errRescaleProbMapBuf:rawRefinedProbMapBuf:refinedProbMapBuf:refinedReflLsBuf:probMapStash4FutureTrackingBuf:doTracking:waitForComplete:]
- -[VideoDeghostingDetectionV2 _getProbMapsLiteTarget:refProbMap:refLsMap:refRefinedLsMap:refProbMapStash4FutureTracking:refErrRescaleProbMap:refRawRefinedProbMap:refRefinedProbMap:mvf:probMap:lsMap:refinedLsMap:probMapStash4FutureTracking:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:metaBufArray:waitForComplete:]
- -[VideoDeghostingDetectionV2 _initDetection:futureFrames:outputImgBufTMinus1:outputImgBufTMinus2:]
- -[VideoDeghostingDetectionV2 doTrackingToNextFrameCurrMetaWithDetectionResults:currMetaWithMvToFuture:futureMeta:opticalCenter:futureOpticalCenter:futureFrameCnt:doLite:waitForComplete:]
- -[VideoDeghostingDetectionV2 getProbMapsTarget:ref:rawProbMap:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:reflLsMap:refinedReflLsMap:reflLsMap4TrackingRef:metaBuf:metaBufArray:trackingMvf:useRefProbMap:opticalCenter:trackingRefOpticalCenter:waitForComplete:]
- -[VideoDeghostingDetectionV2 process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:]
- -[VideoDeghostingDetectionV2 processHwLsMaskAndGetRoisOpticalCenter:inputFrame:prevMetaContainer:considerDist2PrevGhostWhenSort:outputMask:outputMaskTexture:isLowLight:outputArray:]
- -[VideoDeghostingDetectionV2 processHwLsMaskNormalizedCenter:input:output:waitForComplete:]
- -[VideoDeghostingDetectionV2 repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:]
- -[VideoDeghostingDetectionV2 unpackIspLsMaskAndRoisForNextFrameLiteWithFrameData:futureOpticalCenter:outputFutureFrameCnt:outputFutureMetaBuf:]
- -[VideoDeghostingDetectionV2 unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:outputFutureFrameCnt:outputMTLBuffer:]
- -[VideoDeghostingDetectionV2 unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:outputFutureFrameCnt:outputMTLBuffer:].cold.1
- -[VideoDeghostingDetectionV2 updateRepairedRefYUVInput:opticalCenter:prob:errRescaleProb:prevProb:refinedProb:probMap4TrRefW:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:inputBuf:probBuf:errRescaleProbBuf:prevProbBuf:refinedProbBuf:probMap4TrRefWBuf:frRef0Buf:frRef1Buf:nextFrameBuf:metaBuf:metaBufArray:forceToSpatial:waitForComplete:]
- -[Warper computeErrorMask:reference:flow:output:threshold:scaleFactor:]
- -[Warper encodeWarpBlendToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:]
- -[Warper warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toHighResBufferTexture:]
- GCC_except_table14
- GCC_except_table27
- GCC_except_table31
- GCC_except_table7
- GCC_except_table9
- _OBJC_CLASS_$_FRCFrameSynthesizer
- _OBJC_CLASS_$_FRCOpticalFlowEstimator
- _OBJC_CLASS_$_FRCOpticalFlowEstimatorConfiguration
- _OBJC_CLASS_$_LoGFilter
- _OBJC_CLASS_$_MPSImageGaussianBlur
- _OBJC_CLASS_$_SPIFrameSynthesizer
- _OBJC_IVAR_$_FRNet._attachmentRGBDict
- _OBJC_IVAR_$_FRNet._bicubicRGB
- _OBJC_IVAR_$_FRNet._bicubicRGBTexture
- _OBJC_IVAR_$_FRNet._currentLRYUV
- _OBJC_IVAR_$_FRNet._highResolutionNormalizedBufferPool
- _OBJC_IVAR_$_FRNet._laplacianMask
- _OBJC_IVAR_$_FRNet._logFilter
- _OBJC_IVAR_$_FRNet._lowResolutionNormalizedBufferPool
- _OBJC_IVAR_$_FRNet._normalizedCurrentLowResLuma
- _OBJC_IVAR_$_FRNet._normalizedCurrentLowResLumaTexture
- _OBJC_IVAR_$_FRNet._normalizedPreviousLowResLuma
- _OBJC_IVAR_$_FRNet._normalizedPreviousLowResLumaTexture
- _OBJC_IVAR_$_FRNet._normalizedRGB
- _OBJC_IVAR_$_FRNet._outputPixelFormat
- _OBJC_IVAR_$_FRNet._previousHRRGB
- _OBJC_IVAR_$_FRNet._previousHRRGBTexture
- _OBJC_IVAR_$_FRNet._previousHighResolutionOutput
- _OBJC_IVAR_$_FRNet._previousLR
- _OBJC_IVAR_$_FRNet._previousLRYUV
- _OBJC_IVAR_$_FRNet._removeCMAttachment
- _OBJC_IVAR_$_FRNet._rgbaPixelFormat
- _OBJC_IVAR_$_FRNet._srNetHROutput
- _OBJC_IVAR_$_FRNet._useLaplacianMask
- _OBJC_IVAR_$_FRNet._vtTransferSession
- _OBJC_IVAR_$_FRNet._warpedHR
- _OBJC_IVAR_$_FRNet._warpedHRTexture
- _OBJC_IVAR_$_ImageSR._outputSR
- _OBJC_IVAR_$_LoGFilter._absoluteDiffKernel
- _OBJC_IVAR_$_LoGFilter._gauss1
- _OBJC_IVAR_$_LoGFilter._gauss2
- _OBJC_IVAR_$_LoGFilter._gauss3
- _OBJC_IVAR_$_LoGFilter._gaussianFilteredTexture1
- _OBJC_IVAR_$_LoGFilter._gaussianFilteredTexture2
- _OBJC_IVAR_$_LoGFilter._maskScaleFactor
- _OBJC_IVAR_$_LoGFilter._maskStrength
- _OBJC_IVAR_$_LoGFilter._upsampleScaleKernel
- _OBJC_IVAR_$_OFNormalization._copyRgbTo4x4ShuffledTextureArray
- _OBJC_IVAR_$_OFNormalization._denormalizeRGBKernel
- _OBJC_IVAR_$_OFNormalization._normalizeLumaKernel
- _OBJC_IVAR_$_OFNormalization._normalizeLumaPacked420Kernel
- _OBJC_IVAR_$_OFNormalization._normalizeRGBKernel
- _OBJC_IVAR_$_OFNormalization._sharedEvent
- _OBJC_IVAR_$_OFNormalization._signalValue
- _OBJC_IVAR_$_OpticalFlowProcessor._opticalFlowSPI
- _OBJC_IVAR_$_SPIFrameSynthesizer._flowHeight
- _OBJC_IVAR_$_SPIFrameSynthesizer._flowWidth
- _OBJC_IVAR_$_SPIFrameSynthesizer._isFirstFrameInStream
- _OBJC_IVAR_$_SPIFrameSynthesizer._spiInstance
- _OBJC_IVAR_$_SPIFrameSynthesizer._streamingMode
- _OBJC_IVAR_$_SRNet._outputBufferObject
- _OBJC_IVAR_$_SRNet._outputPortName
- _OBJC_IVAR_$_SRNet._outputSurface
- _OBJC_IVAR_$_SRNet._output_port
- _OBJC_IVAR_$_Upsampler._imageUpsampleRGBPackedKernel
- _OBJC_IVAR_$_VSRNet._inputSurface
- _OBJC_IVAR_$_VSRNet._prevHRSurface
- _OBJC_IVAR_$_VideoDeghostingDetectionV2._currSegmentProcessedFrameCnt
- _OBJC_IVAR_$_VideoDeghostingDetectionV2._errRescaleProbMap0
- _OBJC_IVAR_$_VideoDeghostingDetectionV2._errRescaleProbMap0Texture
- _OBJC_IVAR_$_VideoDeghostingDetectionV2._errRescaleProbMap1
- _OBJC_IVAR_$_VideoDeghostingDetectionV2._errRescaleProbMap1Texture
- _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedRefProbMap
- _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedRefProbMapTexture
- _OBJC_IVAR_$_Warper._warpBlendRGBKernel
- _OBJC_METACLASS_$_LoGFilter
- _OBJC_METACLASS_$_SPIFrameSynthesizer
- __OBJC_$_INSTANCE_METHODS_LoGFilter
- __OBJC_$_INSTANCE_METHODS_SPIFrameSynthesizer
- __OBJC_$_INSTANCE_VARIABLES_LoGFilter
- __OBJC_$_INSTANCE_VARIABLES_SPIFrameSynthesizer
- __OBJC_$_PROP_LIST_LoGFilter
- __OBJC_$_PROP_LIST_SPIFrameSynthesizer
- __OBJC_$_PROP_LIST_VSRNet
- __OBJC_CLASS_PROTOCOLS_$_SPIFrameSynthesizer
- __OBJC_CLASS_RO_$_LoGFilter
- __OBJC_CLASS_RO_$_SPIFrameSynthesizer
- __OBJC_METACLASS_RO_$_LoGFilter
- __OBJC_METACLASS_RO_$_SPIFrameSynthesizer
- ___146-[VideoDeghostingDetectionV2 process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:]_block_invoke
- ___146-[VideoDeghostingDetectionV2 process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:]_block_invoke.40
- ___248-[VideoDeghostingDetectionV2 repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:]_block_invoke
- ___248-[VideoDeghostingDetectionV2 repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:]_block_invoke_2
- ___block_descriptor_130_e8_32s40s48s56s64s72s80s88s96r104r112r_e5_v8?0lr96l8s32l8r104l8r112l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
- ___block_descriptor_40_e8_32bs_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36ls32l8
- ___block_descriptor_56_e8_32s40bs48r_e28_v16?0"<MTLCommandBuffer>"8ls40l8r48l8s32l8
- ___block_descriptor_88_e8_32s40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
- ___block_descriptor_93_e8_32s40s48s56r_e5_v8?0ls32l8r56l8s40l8s48l8
- _objc_msgSend$_getProbMapInput:reflLs:trackingRef:trackingRefProb:trackingRefSpaProb:trackingRefErrRescaleProb:trackingRefLs:inputBuf:reflLsBuf:trackingRefBuf:trackingRefProbBuf:trackingRefSpaProbBuf:trackingRefErrRescaleProbBuf:trackingRefLsBuf:trackingMvf:metaBuf:metaBufArray:trackingRefMetaBuf:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:refinedReflLs:probMapStash4FutureTracking:probMapBuf:errRescaleProbMapBuf:rawRefinedProbMapBuf:refinedProbMapBuf:refinedReflLsBuf:probMapStash4FutureTrackingBuf:doTracking:waitForComplete:
- _objc_msgSend$_initDetection:futureFrames:outputImgBufTMinus1:outputImgBufTMinus2:
- _objc_msgSend$computeErrorMask:reference:flow:output:threshold:scaleFactor:
- _objc_msgSend$convertBuffer:toFP16IOSurface:
- _objc_msgSend$convertBuffer:toFP16ShuffledIOSurface:
- _objc_msgSend$convertFP16IOSurface:toBuffer:
- _objc_msgSend$createMaskFrom:to:
- _objc_msgSend$doTrackingToNextFrameCurrMetaWithDetectionResults:currMetaWithMvToFuture:futureMeta:opticalCenter:futureOpticalCenter:futureFrameCnt:doLite:waitForComplete:
- _objc_msgSend$encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:
- _objc_msgSend$encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:
- _objc_msgSend$encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:
- _objc_msgSend$encodeDenormalizeRGBToCommandBuffer:source:destination:
- _objc_msgSend$encodeDiffToCommandBuffer:texture0:texture1:
- _objc_msgSend$encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:
- _objc_msgSend$encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:
- _objc_msgSend$encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:
- _objc_msgSend$encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:
- _objc_msgSend$encodeGetOverlapWithRefs:input:probMap:metaBuf:
- _objc_msgSend$encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:
- _objc_msgSend$encodeNormalizationRGBToCommandBuffer:source:destination:
- _objc_msgSend$encodeNormalizeLumaToCommandBuffer:source:destination:
- _objc_msgSend$encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:laplacianMask:outputY:outputUV:
- _objc_msgSend$encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:
- _objc_msgSend$encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:
- _objc_msgSend$encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:
- _objc_msgSend$encodeUpsampleScaleToCommandBuffer:sourceTexture:destinationTexture:
- _objc_msgSend$encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:
- _objc_msgSend$encodeWarpBlendToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:
- _objc_msgSend$encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:
- _objc_msgSend$encodeWarpRefMetaLite:refMetaBuf:outMetaBuf:
- _objc_msgSend$endAllLocksWithAssetType:assetSpecifier:forClientName:
- _objc_msgSend$endAllPreviousLocksOfSelectorSync:forClientName:
- _objc_msgSend$getColorConsistentOutputRGBVia:bicubicRGB:laplacianMask:attachment:destinationFrame:
- _objc_msgSend$getLocalMobileAssetURLWithAssetType:assetSpecifier:forClientName:
- _objc_msgSend$getProbMapsTarget:ref:rawProbMap:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:reflLsMap:refinedReflLsMap:reflLsMap4TrackingRef:metaBuf:metaBufArray:trackingMvf:useRefProbMap:opticalCenter:trackingRefOpticalCenter:waitForComplete:
- _objc_msgSend$initWithDevice:sigma:
- _objc_msgSend$initWithMetalContext:commandQueue:tuningParamDict:
- _objc_msgSend$interestInContentSync:forAssetSelector:
- _objc_msgSend$normalizeLumaFromFrame:toTexture:
- _objc_msgSend$outputBufferObject
- _objc_msgSend$outputSurface
- _objc_msgSend$output_port
- _objc_msgSend$postprocessSRFrame:bicubicYUV:laplacianMask:outputYUV:
- _objc_msgSend$process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:
- _objc_msgSend$processHwLsMaskAndGetRoisOpticalCenter:inputFrame:prevMetaContainer:considerDist2PrevGhostWhenSort:outputMask:outputMaskTexture:isLowLight:outputArray:
- _objc_msgSend$processHwLsMaskNormalizedCenter:input:output:waitForComplete:
- _objc_msgSend$processSourceFrame:nextFrame:forwardFlow:backwardFlow:ourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:randomAccessMode:destinationFrame:
- _objc_msgSend$processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:
- _objc_msgSend$repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:
- _objc_msgSend$setEdgeMode:
- _objc_msgSend$spiInstance
- _objc_msgSend$synthesizeFrameFromFirstFrame:secondFrame:forwardFlow:backwardFlow:timeScale:destination:
- _objc_msgSend$synthesizeFramesFromFirstFrame:secondFrame:forwardFlow:backwardFlow:numberOfFrames:withError:
- _objc_msgSend$unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:outputFutureFrameCnt:outputMTLBuffer:
- _objc_msgSend$updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:opticalCenterShift:
- _objc_msgSend$updateRepairedRefYUVInput:opticalCenter:prob:errRescaleProb:prevProb:refinedProb:probMap4TrRefW:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:inputBuf:probBuf:errRescaleProbBuf:prevProbBuf:refinedProbBuf:probMap4TrRefWBuf:frRef0Buf:frRef1Buf:nextFrameBuf:metaBuf:metaBufArray:forceToSpatial:waitForComplete:
- _objc_msgSend$upsampleRBGPackedBuffer:to:scaleFactor:
- _objc_msgSend$warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toHighResBufferTexture:
CStrings:
+ "  CGColorSpace: %s"
+ "  ColorPrimaries: %s"
+ "  TransferFunction: %s"
+ "  YCbCrMatrix: %s"
+ " !\"#$%&'()*+,-./"
+ "!!"
+ "\"(f"
+ "%@-%u"
+ "%c"
+ "%s : Invaild inputCopyTexture texture"
+ "%s : Invaild inputMitigatedTexture texture"
+ "%s : Invalid alignedRef0 texture"
+ "%s : Invalid backwardFlow0 texture"
+ "%s : Invalid backwardFlow1 texture"
+ "%s : Invalid blobSaliency texture"
+ "%s : Invalid clusterMeta buffer"
+ "%s : Invalid clusterMetaBuf buffer"
+ "%s : Invalid colorSimilarityMap texture"
+ "%s : Invalid diffToBg texture"
+ "%s : Invalid diffToBgMap texture"
+ "%s : Invalid dilatedProbMap texture"
+ "%s : Invalid encoder"
+ "%s : Invalid flow texture"
+ "%s : Invalid forwarpHoleMap0 texture"
+ "%s : Invalid forwarpHoleMap1 texture"
+ "%s : Invalid fullResInput texture"
+ "%s : Invalid fullResTarget texture"
+ "%s : Invalid fullResWarpedRef0 texture"
+ "%s : Invalid fullResWarpedRef1 texture"
+ "%s : Invalid input texture"
+ "%s : Invalid input0 texture"
+ "%s : Invalid input1 texture"
+ "%s : Invalid inputBuffer0 buffer"
+ "%s : Invalid inputBuffer1 buffer"
+ "%s : Invalid inputFrame texture"
+ "%s : Invalid inputMap texture"
+ "%s : Invalid inputMap0 texture"
+ "%s : Invalid inputMap1 texture"
+ "%s : Invalid inputYUV texture"
+ "%s : Invalid intermediateOutput0 buffer"
+ "%s : Invalid intermediateOutput1 buffer"
+ "%s : Invalid lsCheckOutmetaBuf buffer"
+ "%s : Invalid lsMap texture"
+ "%s : Invalid map texture"
+ "%s : Invalid meta buffer"
+ "%s : Invalid metaBuf buffer"
+ "%s : Invalid metaForTrackingBuf buffer"
+ "%s : Invalid metaRef0 buffer"
+ "%s : Invalid motion texture"
+ "%s : Invalid mvf texture"
+ "%s : Invalid mvf0 texture"
+ "%s : Invalid mvf1 texture"
+ "%s : Invalid mvf2 texture"
+ "%s : Invalid outMetaBuf buffer"
+ "%s : Invalid outMvf texture"
+ "%s : Invalid outMvf0 texture"
+ "%s : Invalid outMvf1 texture"
+ "%s : Invalid output texture"
+ "%s : Invalid outputMap0 texture"
+ "%s : Invalid outputMap1 texture"
+ "%s : Invalid probMap texture"
+ "%s : Invalid redoTrackingOutmetaBuf buffer"
+ "%s : Invalid ref0 texture"
+ "%s : Invalid ref1 texture"
+ "%s : Invalid refLsMap texture"
+ "%s : Invalid refMetaBuf buffer"
+ "%s : Invalid refinedProbMap texture"
+ "%s : Invalid reflLsMap texture"
+ "%s : Invalid repaired texture"
+ "%s : Invalid roiAvoidList buffer"
+ "%s : Invalid saliency texture"
+ "%s : Invalid segMap texture"
+ "%s : Invalid spaProbMap texture"
+ "%s : Invalid spaRepaired texture"
+ "%s : Invalid target texture"
+ "%s : Invalid upscaledProbMap texture"
+ "%s : Invalid upscaledRefinedProbMap texture"
+ "%s : Invalid warpedRefYUV texture"
+ "-[GGMMetalToolBox encodeAlignBgAvgForMotionEstYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:]"
+ "-[GGMMetalToolBox encodeCollectClusterRepairError:clusterMetaBuf:metaBuf:metaForTrackingBuf:]"
+ "-[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:metaForTrackingBuf:]"
+ "-[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:roiAvoidList:]"
+ "-[GGMMetalToolBox encodeCollectOpticalCenterEstStats:clusterMetaBuf:metaBuf:]"
+ "-[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:colorSimilarity:spaRef:mvf:output:spaOutput:fusedOutput:meta:wRef:]"
+ "-[GGMMetalToolBox encodeConvertYUVToRGBToCommandEncoder:input:output:]"
+ "-[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationRadius:softDilationRadius:meta:]"
+ "-[GGMMetalToolBox encodeForwarpYUVToCommandEncoder:input0:input1:meta:mvf0:mvf1:intermediateOutput0:intermediateOutput1:output0:output1:outputMap0:outputMap1:]"
+ "-[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:outputForFutureRefTexture:metaBuf:]"
+ "-[GGMMetalToolBox encodeGetBgAvgForMotionEstYUVToCommandEncoder:target:ref0:ref1:probMap:meta:]"
+ "-[GGMMetalToolBox encodeGetColorSimilarity:inputYUV:warpedRefYUV:colorSimilarityMap:meta:]"
+ "-[GGMMetalToolBox encodeGetDiffToBg:inputYUV:reflLsMap:segMap:diffToBgMap:meta:]"
+ "-[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:diffToBgMap:isInitFrame:probMap:meta:]"
+ "-[GGMMetalToolBox encodeGetLsMapYUVProxyToCommandEncoder:input:map:]"
+ "-[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:avgAlignedRef:target:motionMap:meta:]"
+ "-[GGMMetalToolBox encodeGetOcclusionMap:fullResTarget:fullResWarpedRef0:fullResWarpedRef1:forwarpHoleMap0:forwarpHoleMap1:backwardFlow0:backwardFlow1:outputMap0:outputMap1:meta:]"
+ "-[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:spaProbMap:lsMap:metaBuf:]"
+ "-[GGMMetalToolBox encodeGetRepairErrYUVToCommandEncoder:target:repaired:spaRepaired:probMap:flow:meta:]"
+ "-[GGMMetalToolBox encodeGetRoiBgAvgYUVToCommandEncoder:target:ref0:meta:metaRef0:]"
+ "-[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:flow0:flow1:meta:]"
+ "-[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:avgAlignedRef:output:refOutput:avgAlignedRefOutput:metaBuf:processedFrameCount:]"
+ "-[GGMMetalToolBox encodeRefineProbMapWithSpatialRepairedToEncoder:input:spaRepaired:inputMap:output:meta:]"
+ "-[GGMMetalToolBox encodeRefineTrackedProbMapToEncoder:input:motion:saliency:blobSaliency:diffToBg:hardRHi:softRHi:hardRLo:softRLo:isInitFrame:output:meta:]"
+ "-[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:rawProbMap4Spatial:probMap4Spatial:spatialOutput:metaBuf:]"
+ "-[GGMMetalToolBox encodeSyncStats:clusterMeta:meta:]"
+ "-[GGMMetalToolBox encodeUpdateEstOpticalCenterOffset:meta:]"
+ "-[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:roiAvoidList:currTrackId:]"
+ "-[GGMMetalToolBox encodeblendOriginalAndLRBufToCommandEncoder:MitigatedBuf:inputCopyOrg:output:meta:]"
+ "/System/Library/Frameworks/CoreText.framework/"
+ "0123456789:;<=>?"
+ "@ABCDEFGHIJKLMNO"
+ "A!"
+ "Add Norm Tile [%d,%d]"
+ "Arial Rounded MT Bold"
+ "Bundle is nil"
+ "Completed tile (%d,%d)"
+ "Copying tile: input(%zux%zu) -> tile(%dx%d) at offset(%d,%d)"
+ "Could not create font %@"
+ "Created Metal buffers for tile layout: X=%d, Y=%d, with effective boundaries"
+ "Created Metal textures for all TileProcessor buffers"
+ "DVPDenseUpscalerConfiguration: Destination must be >= source dimensions"
+ "DVPDenseUpscalerConfiguration: Invalid destination dimensions"
+ "DVPDenseUpscalerConfiguration: Invalid frame dimensions"
+ "DVPDenseUpscalerConfiguration: Invalid source dimensions"
+ "DVPDenseUpscalerParameters: destinationFrame is nil"
+ "DVPDenseUpscalerParameters: guideFrame is nil"
+ "DVPDenseUpscalerParameters: sourceFrame is nil"
+ "DVPDrawShapeGPU::copyBackDrawnText"
+ "DVPDrawShapeGPU::drawRectangleFragment"
+ "DVPDrawShapeGPU::drawRectangleVertex"
+ "DVPDrawShapeGPU::drawText"
+ "Dense type mismatch with processor initialization"
+ "Dense upscaling failed"
+ "Destination dimensions mismatch with processor initialization"
+ "Error! Failed to create outputTexture. Buffer Size: %ld x %ld, Format: %d"
+ "Error: _inputPortName does not match valid name\n"
+ "Extract Tile (%d,%d)"
+ "Extract Tile From Texture"
+ "FRC_USE_INT_ATOMIC"
+ "FRNet: Input missing crucial color attachments!"
+ "Failed to allocate texture descriptor"
+ "Failed to create destination texture"
+ "Failed to create font descriptor"
+ "Failed to create guide texture"
+ "Failed to create metal texture from allocator"
+ "Failed to create source texture"
+ "Failed to create texture descriptor\n"
+ "Failed to initialize"
+ "Failed to initialize: Mismatch between source and next frame's pixel formats"
+ "Failed to initialize: Mismatch between source and reference frame's pixel formats"
+ "Failed to initialize: Mismatch between source, next, and previous frame's pixel formats"
+ "Failed to initialize: Mismatch between source, previous, and previousOutput frame's pixel formats"
+ "Failed to start DenseUpscaler session"
+ "FrameNum: %3lu ocx: %.2f ocy: %.2f"
+ "G"
+ "Guide frame pixel format not supported"
+ "HR Tile Texture"
+ "Input size (%zu x %zu) > TILE_SIZE (%d), enabling tiling"
+ "LR Tile Texture"
+ "MISSING"
+ "Metal pipeline not supported"
+ "OFForwarp: disable float kernel for bitmatch stress tests"
+ "PQRSTUVWXYZ[\\]^_"
+ "Processing %dx%d tiles (stride=%d)"
+ "Processing tile (%d,%d): extracting from input at (%d,%d)"
+ "Scale"
+ "Session not started"
+ "Single %@ with tile_size > input: splitting into two tiles"
+ "Source dimensions mismatch with processor initialization"
+ "Split into 2 tiles: tile0 pos0=%d effective=[%d,%d), tile1 pos0=%d effective=[%d,%d)"
+ "Text"
+ "Tile calculation: effective_size=%d, tiles=%dx%d"
+ "TileProcessor buffers allocated successfully"
+ "TileProcessor buffers released"
+ "TileProcessor completed successfully"
+ "TileProcessor processing: input=%zux%zu -> output=%zux%zu"
+ "Unable to allocate MTLVertexDescriptor"
+ "Unable to initialize DrawRectangleGPU class"
+ "Unable to load metal library for DrawShapeGPU"
+ "Unsupported pixel buffer format"
+ "Unsupported pixel format"
+ "Unsupported texture format"
+ "Using cached font"
+ "Write Tile To Output"
+ "X"
+ "Y"
+ "[DenseUpscalerProcessor] Initialized: source(%ld x %ld) -> destination(%ld x %ld), type=%ld\n"
+ "[DenseUpscalerProcessor] Session finished\n"
+ "[DenseUpscalerProcessor] Session started: source(%ld x %ld) -> destination(%ld x %ld), frame(%ld x %ld)\n"
+ "[DenseUpscaler] Initialized with type: %ld\n"
+ "[DenseUpscaler] Session finished\n"
+ "[DenseUpscaler] Session started: LR(%zu x %zu) -> HR(%zu x %zu), type=%ld\n"
+ "[VEMobileAsset] endLock - Error: %@"
+ "[VEMobileAsset] endLock - SUCCESS"
+ "[VEMobileAsset] endLock - interestInContent error: %@"
+ "[VEMobileAsset] initWithAssetType - Error during initForClientName: %@"
+ "[VEMobileAsset] lockAndGetLocalAssetURL - already locked; call endLock first"
+ "[VEMobileAsset] lockAndGetLocalAssetURL - autoAsset is nil"
+ "[VEMobileAsset] lockAndGetLocalAssetURL - failed to lock asset: %@"
+ "[VEMobileAsset] lockAndGetLocalAssetURL - localContentURL: %@"
+ "_backwardFlow cannot be nil"
+ "_forwardFlow cannot be nil"
+ "`abcdefghijklmno"
+ "alpha"
+ "compute_rgb_dense_edge"
+ "denseUpscaleHighresUpscale"
+ "denseUpscaleLowresCluster"
+ "denseUpscalerConfig is nil"
+ "denseUpscalerParams is nil"
+ "destinationFrame is nil"
+ "drawStyle"
+ "e5rt_buffer_object_create_from_iosurface(&_inputBufferObjects[i], *currentLRSurface)"
+ "e5rt_buffer_object_create_from_iosurface(&_inputBufferObjects[i], *warpedHRSurface)"
+ "e5rt_execution_stream_operation_retain_output_port(self.operation, _outputPortName.UTF8String, &_output_port)"
+ "e5rt_io_port_bind_buffer_object(_input_ports[i], _inputBufferObjects[i])"
+ "e5rt_io_port_bind_buffer_object(_output_port, _outputBufferObject)"
+ "extractTileFromTexture"
+ "guideFrame is nil"
+ "hr_prev"
+ "initShaders failed"
+ "landscape1072x1920"
+ "landscape544x960"
+ "lr_curr"
+ "metalToolBox::alignBgAvgForMotionEstYUV"
+ "metalToolBox::blendOriginalAndLRBuf"
+ "metalToolBox::collectClusterRepairError"
+ "metalToolBox::collectOpticalCenterEstStats"
+ "metalToolBox::convertYUVToRGB"
+ "metalToolBox::getBgAvgForMotionEstYUV"
+ "metalToolBox::getColorSimilarity"
+ "metalToolBox::getDiffToBg"
+ "metalToolBox::getLsMapYUVProxy"
+ "metalToolBox::getOcclusionMap"
+ "metalToolBox::getRepairErrYUV"
+ "metalToolBox::getRoiBgAvgYUV"
+ "metalToolBox::refineProbMapWithSpatialRepaired"
+ "metalToolBox::refineTrackedProbMap"
+ "metalToolBox::syncStats"
+ "metalToolBox::updateEstOpticalCenterOffset"
+ "mobileAssetLockReasonUse"
+ "pqrstuvwxyz{|}~"
+ "present"
+ "s"
+ "segmentInput: Average map must be kCVPixelFormatType_OneComponent8 format"
+ "segmentInput: Failed to create PixelMemory objects"
+ "segmentInput: Input buffer is null"
+ "segmentInput: Input buffer must be kCVPixelFormatType_32BGRA format"
+ "segmentInput: Input pixel queue is null"
+ "segmentInput: Segmentation map must be kCVPixelFormatType_OneComponent8 format"
+ "selectedFont"
+ "sourceFrame is nil"
+ "strokeWidth"
+ "true"
+ "upsampleBGRToRGB"
+ "upsampleRGBToRGB"
+ "vertexBuffer is NULL"
+ "warpBlendShuffleRGB"
+ "writeTileToOutput"
+ "\x82"
- "#"
- "#16@0:8"
- "%s : Invaild clusterMetaBuf texture"
- "%s : Invaild dilatedProbMap texture"
- "%s : Invaild dilatedRef texture"
- "%s : Invaild errRescaleProbMap texture"
- "%s : Invaild fullResTarget texture"
- "%s : Invaild inputBuffer0 texture"
- "%s : Invaild inputBuffer1 texture"
- "%s : Invaild inputFrame texture"
- "%s : Invaild inputMap0 texture"
- "%s : Invaild inputMap1 texture"
- "%s : Invaild metaBuf texture"
- "%s : Invaild mvf2 texture"
- "%s : Invaild outMetaBuf texture"
- "%s : Invaild outMvf texture"
- "%s : Invaild outMvf0 texture"
- "%s : Invaild outMvf1 texture"
- "%s : Invaild outputMap0 texture"
- "%s : Invaild outputMap1 texture"
- "%s : Invaild prevProbMap texture"
- "%s : Invaild refMetaBuf texture"
- "%s : Invaild refinedProbMap texture"
- "%s : Invaild upscaledProbMap texture"
- "%s : Invaild upscaledRefinedProbMap texture"
- "%s : hardDilationOutput output texture"
- "*"
- "*16@0:8"
- "-[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:]"
- "-[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:]"
- "-[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:]"
- "-[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:]"
- "-[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:]"
- "-[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:]"
- "-[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:]"
- "-[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:]"
- "-[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:]"
- "-[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:]"
- "-[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:]"
- "-[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:]"
- ".cxx_destruct"
- "16@0:8"
- "24@0:816"
- "24@0:8@16"
- "24@0:8f16f20"
- "24@0:8i16i20"
- "3"
- "72@0:8@16{?=[3]}24"
- "@\"<FrameSynthesizerProtocol>\""
- "@\"<MTLBuffer>\""
- "@\"<MTLCommandQueue>\""
- "@\"<MTLComputePipelineState>\""
- "@\"<MTLDevice>\""
- "@\"<MTLDeviceSPI>\""
- "@\"<MTLLibrary>\""
- "@\"<MTLRenderPipelineState>\""
- "@\"<MTLSharedEvent>\""
- "@\"<MTLTexture>\""
- "@\"Backwarp_Ext\""
- "@\"Backwarp_VSA\""
- "@\"DVPFrame\""
- "@\"DVPFrame\"16@0:8"
- "@\"DVPFrameOpticalFlow\""
- "@\"DVPOpticalFlowConfiguration\""
- "@\"DVPOpticalFlowParameters\""
- "@\"FRCFlowAdaptationFeatureExtractor\""
- "@\"FRCFrameSynthesizer\""
- "@\"FRCOpticalFlowEstimator\""
- "@\"FRCPyramid\""
- "@\"FRNet\""
- "@\"FlowConsistency\""
- "@\"FlowUpscale\""
- "@\"Forwarp_Ext\""
- "@\"FrameSynthesis\""
- "@\"GGMController\""
- "@\"GGMMetalToolBox\""
- "@\"GenericFlow\""
- "@\"HomographyFlow\""
- "@\"ISRNet\""
- "@\"ImageProcessUtility\""
- "@\"ImageProcessor\""
- "@\"ImageProcessor_Ext\""
- "@\"ImageProcessor_VSA\""
- "@\"ImageReg\""
- "@\"ImageSR\""
- "@\"LoGFilter\""
- "@\"MPSImageBilinearScale\""
- "@\"MPSImageGaussianBlur\""
- "@\"MTLSharedEventListener\""
- "@\"MaskToRoi\""
- "@\"MetalToolBox\""
- "@\"MitigationANE\""
- "@\"MotionBlurEngine\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSArray\"64@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40@\"NSArray\"48^@56"
- "@\"NSArray\"64@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40Q48^@56"
- "@\"NSDate\""
- "@\"NSDictionary\""
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_group>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"Normalization_Ext\""
- "@\"OFBackwarp\""
- "@\"OFCorrelation\""
- "@\"OFFeatureExtractor\""
- "@\"OFForwarp\""
- "@\"OFNormalization\""
- "@\"OpticalFlowProcessor\""
- "@\"Postprocess\""
- "@\"PseudoDepthGenerator\""
- "@\"ROI\""
- "@\"RansacEstimation\""
- "@\"SIFTFeatureExtraction\""
- "@\"SIFTMatcher\""
- "@\"Synthesis_Ext\""
- "@\"Upsampler\""
- "@\"VDGDetectionUtilsV2\""
- "@\"VEOpticalFlow\""
- "@\"VEOpticalFlowEstimator\""
- "@\"VEScaler\""
- "@\"VSRNet\""
- "@\"VideoDeghostingDetectionV2\""
- "@\"Warper\""
- "@100@0:8Q16q24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGRect={CGPoint=dd}{CGSize=dd}}64f96"
- "@112@0:8@16@24@32{CGPoint=dd}40{CGPoint=dd}56d72@80@88q96@104"
- "@16@0:8"
- "@192@0:816{?=fffffI}32"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@16"
- "@24@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16"
- "@24@0:8^{__CVBuffer=}16"
- "@24@0:8q16"
- "@264@0:8Q16q24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGRect={CGPoint=dd}{CGSize=dd}}64{?=fffffI}96^{?=iBBiiiBB}256"
- "@28@0:8@16B24"
- "@28@0:8q16I24"
- "@32@0:816"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16q24"
- "@32@0:8@16r*24"
- "@32@0:8Q16Q24"
- "@32@0:8^{__CVBuffer=}16B24B28"
- "@32@0:8^{__CVBuffer=}16Q24"
- "@32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
- "@32@0:8d16d24"
- "@32@0:8q16q24"
- "@36@0:8@16@24B32"
- "@36@0:8@16@24f32"
- "@36@0:8@16q24B32"
- "@36@0:8q16I24q28"
- "@36@0:8q16q24B32"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "@40@0:8@16@24{?=ii}32"
- "@40@0:8@16Q24Q32"
- "@40@0:8@16^{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}}24^{?=iiiiiifffiifiiii{?=ffffffff}{?=iiffffffffffffff}{?=fff}}32"
- "@40@0:8@16^{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}}24{?=ii}32"
- "@40@0:8@16q24q32"
- "@40@0:8Q16Q24Q32"
- "@40@0:8Q16Q24q32"
- "@40@0:8f16f20[4f]24i32i36"
- "@40@0:8q16@24@32"
- "@40@0:8q16q24@32"
- "@40@0:8q16q24q32"
- "@44@0:8@16@24@32B40"
- "@44@0:8q16@24@32B40"
- "@44@0:8q16q24B32q36"
- "@44@0:8q16q24q32B40"
- "@48@0:8@16@24q32@40"
- "@48@0:8^{__CVBuffer=}16{?=qiIq}24"
- "@48@0:8^{__IOSurface=}16q24q32q40"
- "@48@0:8q16q24q32q40"
- "@52@0:8@16@24i32f36f40f44B48"
- "@52@0:8@16@24{?=ii}32i40@44"
- "@52@0:8q16q24B32q36q44"
- "@56@0:8^{__CVBuffer=}16{?=qiIq}24@48"
- "@64@0:8@16@24@32@40q48@56"
- "@64@0:8Q16q24{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "@64@0:8^{?=ffffffff}16f24s28{CGRect={CGPoint=dd}{CGSize=dd}}32"
- "@64@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40@48^@56"
- "@64@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40Q48^@56"
- "@68@0:8Q16q24{CGRect={CGPoint=dd}{CGSize=dd}}32i64"
- "@68@0:8q16Q24Q32Q40B48{CGSize=dd}52"
- "@68@0:8q16q24q32q40B48q52q60"
- "@80@0:8@16@24@32@40@48q56q64@72"
- "ApplyRansacEstimation:desMatchInput:desMatchInput:desMatchInput:desMatchCountInput:xscaleFactorInput:yscaleFactorInput:imageDimInput:imageDimInput:homographyMatrixOutput:waitForComplete:"
- "B116@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40{CGPoint=dd}48{CGPoint=dd}64d80^{__CVBuffer=}88^{__CVBuffer=}96B104^{__CVBuffer=}108"
- "B16@0:8"
- "B20@0:8B16"
- "B20@0:8i16"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8I16I20"
- "B24@0:8^@16"
- "B24@0:8^{?=@@@@@@@@@@@@@@iiiiiiii}16"
- "B24@0:8^{__CVBuffer=}16"
- "B24@0:8^{e5rt_execution_stream=}16"
- "B24@0:8q16"
- "B24@0:8r*16"
- "B28@0:8^{__CVBuffer=}16f24"
- "B32@0:8@16^@24"
- "B32@0:8@16q24"
- "B32@0:8^{__CVBuffer=}16@24"
- "B32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
- "B32@0:8^{__CVBuffer=}16^{__IOSurface=}24"
- "B32@0:8^{__IOSurface=}16^{__CVBuffer=}24"
- "B32@0:8^{e5rt_execution_stream_operation=}16^{e5rt_execution_stream=}24"
- "B32@0:8q16^@24"
- "B36@0:816f32"
- "B36@0:8^{__CVBuffer=}16^{__CVBuffer=}24B32"
- "B36@0:8^{__CVBuffer=}16^{__CVBuffer=}24f32"
- "B36@0:8^{__CVBuffer=}16f24^{__CVBuffer=}28"
- "B40@0:8@16i24r*28B36"
- "B40@0:8@16{CGSize=dd}24"
- "B40@0:8^{CGPoint=dd}16Q24^d32"
- "B40@0:8^{__CVBuffer=}16^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}24@?32"
- "B40@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32"
- "B40@0:8q16q24^@32"
- "B44@0:8q16B24B28B32^@36"
- "B48@0:8B16B20B24{CGSize=dd}28B44"
- "B48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40"
- "B52@0:8162432f40f44B48"
- "B56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CFDictionary=}40^{__CVBuffer=}48"
- "B56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40@?48"
- "B56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48"
- "B56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40f48f52"
- "B60@0:8@16@24^{__CVBuffer=}32^{__CVBuffer=}40B48^@52"
- "B60@0:8Q16Q24Q32Q40B48^@52"
- "B64@0:8@16Q24@32@40@48@56"
- "B68@0:8^{__CVBuffer=}16^{?=^{?}ii}243240f48^{__CVBuffer=}52^{__CVBuffer=}60"
- "B72@0:8@16@24Q32@40@48@56@64"
- "B80@0:8@16@24@32@40i48f52f56i60i64^{_xform2D={?=[3]}fiii}68B76"
- "B80@0:8@16@24@32^{?=^{__CVBuffer}^{__CVBuffer}}40^{?=^{__CVBuffer}^{__CVBuffer}}48@56^{__CVBuffer=}64^@72"
- "B80@0:8@16@24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48@56^{__CVBuffer=}64^@72"
- "Backwarp_Ext"
- "Backwarp_VSA"
- "BaseProcessor"
- "C"
- "C16@0:8"
- "C28@0:8f16f20c24"
- "C28@0:8i16i20c24"
- "ConvertRGB:toGray:withCoef:waitForComplete:"
- "ConvertYUV:toGray:waitForComplete:"
- "DVPConfiguration"
- "DVPFrame"
- "DVPFrameOpticalFlow"
- "DVPFrameRateConversionConfiguration"
- "DVPFrameRateConversionParameters"
- "DVPLensFlareMitigationConfiguration"
- "DVPLensFlareMitigationParameters"
- "DVPMotionBlurConfiguration"
- "DVPMotionBlurParameters"
- "DVPOpticalFlowConfiguration"
- "DVPOpticalFlowParameters"
- "DVPParameters"
- "DVPSuperResolutionConfiguration"
- "DVPSuperResolutionParameters"
- "DetectedROI"
- "Error allocating _backwardFlow"
- "Error allocating _forwardFlow"
- "Error! Faild to create outputTextute. Buffer Size: %ld x %ld, Format: %d"
- "ExtractKeyPointFromInput1:toHdr1:Input2:toHdr2:count1:count2:"
- "FRCFlowAdaptationDecoder"
- "FRCFlowAdaptationFeatureExtractor"
- "FRCProcessor"
- "FRCPyramid"
- "FRCSynthesis"
- "Fail to initialize"
- "Fail to initialize: Mismatch between source, previous and previousOutput frame's pixel formats"
- "Fail to to initialize: Mismatch between source and next frame's pixel formats"
- "Fail to to initialize: Mismatch between source and reference frame's pixel formats"
- "Fail to to initialize: Mismatch between source, next and previous frame's pixel formats"
- "Fail to to initialize: Mismatch between source, next frame's pixel formats"
- "Failed to cretae texture descriptor\n"
- "FlowConsistency"
- "FlowUpscale"
- "Forwarp_Ext"
- "FrameInsertionPoint"
- "FrameMetadata"
- "FrameSynthesis"
- "FrameSynthesizerProtocol"
- "FrameTimingInfo"
- "GGMController"
- "GGMMetalToolBox"
- "GenericFlow"
- "HomographyFlow"
- "I16@0:8"
- "I28@0:8^{__CVBuffer=}16B24"
- "ISRNet"
- "ImageProcessUtility"
- "ImageProcessor"
- "ImageProcessor_Ext"
- "ImageProcessor_VSA"
- "ImageReg"
- "Input0 [%@]: %ld x %ld x %ld"
- "Input1 [%@]: %ld x %ld x %ld"
- "LSIsHighRisk"
- "LSOrGGBbox"
- "LSRoi"
- "LSTrackID"
- "LSTrackingMatched"
- "LSTrackingVote"
- "LoGFilter"
- "MPSscale"
- "MaskToRoi"
- "MetalToolBox"
- "MitigationANE"
- "MotionBlurEngine"
- "NSObject"
- "Normalization_Ext"
- "OFBackwarp"
- "OFCorrelation"
- "OFFeatureExtractor"
- "OFFlowEstimate"
- "OFForwarp"
- "OFFrame"
- "OFNormalization"
- "OpticalFlowProcessor"
- "PNGRepresentationOfImage:format:colorSpace:options:"
- "PixelMemory"
- "Postprocess"
- "PrintMatchKptDistance:matchCount:kpt1:kpt2:frameId:"
- "Printkpt1:count:"
- "PseudoDepthFromBackwardFlow:forwardFlow:fullresFlow:depth:prevBackFlow:flowErrorMask:interleave_factor:timeScale:downscale_factor:"
- "PseudoDepthGenerator"
- "Q"
- "Q16@0:8"
- "RGBAFormat"
- "ROI"
- "RansacEstimation"
- "SIFTFeatureExtraction"
- "SIFTMatcher"
- "SPIFrameSynthesizer"
- "SRNet"
- "SampleFourChannelAtX:Y:"
- "Synthesis_Ext"
- "T#,R"
- "T*,N,V_pMemory"
- "T*,N,V_pMemoryPlane2"
- "T,V_LSOrGGBbox"
- "T,V_bbox"
- "T,V_defaultOpticalCenter"
- "T,V_differenceOfGaussianAndLumaFeature"
- "T,V_differenceOfGaussianAndLumaFeaturePredictedLocation"
- "T,V_differenceOfGaussianAndLumaFeatureReflection"
- "T,V_lumaFeatureVector"
- "T,V_lumaFeatureVectorPredictedLocation"
- "T,V_lumaFeatureVectorReflection"
- "T,V_mv"
- "T,V_mvSum"
- "T,V_nextVisedOpticalCenter"
- "T,V_roiMv"
- "T,V_trajectoryFromPast"
- "T,V_visedOpticalCenter"
- "T@\"<MTLDevice>\",R,V_device"
- "T@\"DVPFrame\",R,N"
- "T@\"DVPFrame\",R,N,V_destinationFrame"
- "T@\"DVPFrame\",R,N,V_nextFrame"
- "T@\"DVPFrame\",R,N,V_previousFrame"
- "T@\"DVPFrame\",R,N,V_previousOutputFrame"
- "T@\"DVPFrame\",R,N,V_previousPreviousOutputFrame"
- "T@\"DVPFrame\",R,N,V_sourceFrame"
- "T@\"DVPFrameOpticalFlow\",R,N,V_nextOpticalFlow"
- "T@\"DVPFrameOpticalFlow\",R,N,V_opticalFlow"
- "T@\"DVPFrameOpticalFlow\",R,N,V_previousOpticalFlow"
- "T@\"FRCFrameSynthesizer\",&,N,V_spiInstance"
- "T@\"NSArray\",&,N,V_futureInputParamsToRepair"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_destinationFrames"
- "T@\"NSArray\",R,N,V_framePreferredPixelFormats"
- "T@\"NSArray\",R,N,V_frameSupportedPixelFormats"
- "T@\"NSArray\",R,N,V_interpolationPhase"
- "T@\"NSDictionary\",&,N,V_detectedGreenGhostInfo"
- "T@\"NSDictionary\",&,N,V_inputParamsToRepair"
- "T@\"NSDictionary\",&,N,V_metaDictionary"
- "T@\"NSDictionary\",R,N,V_info"
- "T@\"NSDictionary\",R,N,V_tuningParamDict"
- "T@\"NSMutableArray\",&,V_matchedLS"
- "T@\"NSMutableArray\",&,V_trackIDsAfterMerge"
- "T@\"NSString\",&,N,V_debugImage"
- "T@\"NSString\",&,N,V_modelPath"
- "T@\"NSString\",&,N,V_outputPortName"
- "T@\"NSString\",&,V_LSTrackID"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"OFBackwarp\",R,N,V_backwarp"
- "T@\"OFNormalization\",&,N,V_normalization"
- "T@\"ROI\",&,V_LSTrackingMatched"
- "T@\"ROI\",&,V_temporalDetectionMatched"
- "T@\"VEScaler\",&,N,V_scaler"
- "TB,?,N"
- "TB,N"
- "TB,N,V_EnableGpuWaitForComplete"
- "TB,N,V_adaptationLayerOnly"
- "TB,N,V_baseStage"
- "TB,N,V_concurrentDualFlowProcessing"
- "TB,N,V_createOcclusionMask"
- "TB,N,V_disableOutputFlowScaling"
- "TB,N,V_flowFailureDetection"
- "TB,N,V_flowOnlyMode"
- "TB,N,V_framePipeline"
- "TB,N,V_image2motion"
- "TB,N,V_imageGuideUpscale"
- "TB,N,V_inputScaling"
- "TB,N,V_isFirstFrameInStream"
- "TB,N,V_isFullRange"
- "TB,N,V_isYUV"
- "TB,N,V_legacyNormalization"
- "TB,N,V_limitBilinearInterpolation"
- "TB,N,V_linearSplatting"
- "TB,N,V_opticalFlowOnlyMode"
- "TB,N,V_postprocessOutput"
- "TB,N,V_previousFrameAvailable"
- "TB,N,V_pseudoDepth"
- "TB,N,V_refreshCalculation"
- "TB,N,V_sceneChange"
- "TB,N,V_selfNormalization"
- "TB,N,V_skipClamp"
- "TB,N,V_skipLastLevel"
- "TB,N,V_streamingMode"
- "TB,N,V_temporalFiltering"
- "TB,N,V_testingMode"
- "TB,N,V_twoLayerFlowSplatting"
- "TB,N,V_twoLayerQuarterSizeDC"
- "TB,N,V_twoStageFlow"
- "TB,N,V_useAdaptationLayer"
- "TB,N,V_useExternalDepth"
- "TB,N,V_useExternalFlow"
- "TB,N,V_useFloatAtomic"
- "TB,N,V_useFlowConsistencyMap"
- "TB,N,V_useFusedKernel"
- "TB,N,V_useHomography"
- "TB,N,V_useLaplacianMask"
- "TB,N,V_useSIMD"
- "TB,N,V_useSIMDShuffle"
- "TB,N,V_useSIMDSum"
- "TB,N,V_waitForCompletion"
- "TB,R,N"
- "TB,R,N,V_filterErrorMapByGaussian"
- "TB,R,N,V_frameSyncRequired"
- "TB,R,N,V_usePrecomputedFlow"
- "TB,V_LSIsHighRisk"
- "TB,V_accuracyMode"
- "TB,V_doneKPToBBoxViaGraphTraversal"
- "TB,V_isPredictedFromPast"
- "TB,V_isReflectedLS"
- "TB,V_isTracked"
- "TB,V_isTrajectoryPruningPassed"
- "TB,V_kpIsFromHW"
- "TB,V_lsHasBeenUsedForTrackingGhost"
- "TB,V_prevShouldRunGGDetectionClippedPixelBased"
- "TB,V_prevShouldRunGGDetectionLSBased"
- "TB,V_prevShouldRunGGDetectionLuxLevelBased"
- "TB,V_trackFail"
- "TC,N,V_channels"
- "TI,N,V_RGBAFormat"
- "TI,N,V_format"
- "TI,N,V_matchOutputDimensions"
- "TI,N,V_outputPixelFormat"
- "TI,N,V_pixelFormat"
- "TI,R,N,V_flowBufferPixelFormat"
- "TI,V_level"
- "TIFFRepresentationOfImage:format:colorSpace:options:"
- "TQ,?,N"
- "TQ,N,V_bufferHeight"
- "TQ,N,V_bufferWidth"
- "TQ,N,V_downsampling"
- "TQ,N,V_height"
- "TQ,N,V_inputHeight"
- "TQ,N,V_inputWidth"
- "TQ,N,V_numberOfFramesToInsert"
- "TQ,N,V_originalPTSInNanos"
- "TQ,N,V_ptsInNanos"
- "TQ,N,V_sequenceAdjusterRecipe"
- "TQ,N,V_synthesisMode"
- "TQ,N,V_width"
- "TQ,R"
- "TQ,R,N"
- "TQ,R,N,V_flowHeight"
- "TQ,R,N,V_flowWidth"
- "TQ,R,N,V_highResPaddedHeight"
- "TQ,R,N,V_highResPaddedWidth"
- "TQ,R,N,V_lowResPaddedHeight"
- "TQ,R,N,V_lowResPaddedWidth"
- "TQ,R,N,V_outputHeight"
- "TQ,R,N,V_outputWidth"
- "TQ,R,N,V_scaleFactor"
- "TQ,R,N,V_trackSessionId"
- "TQ,V_channels"
- "TQ,V_height"
- "TQ,V_outputChannels"
- "TQ,V_width"
- "T^{?=^{?}ii},N,V_futureFramesToDetectionAndRepair"
- "T^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f},V_metaContainer"
- "T^{?={?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}},R"
- "T^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}},R"
- "T^{__CFDictionary=},N,V_anchorFrameCMAttachment"
- "T^{__CVBuffer=},N,V_buf"
- "T^{__CVBuffer=},N,V_inputBuffer"
- "T^{__CVBuffer=},N,V_keyPointsList"
- "T^{__CVBuffer=},N,V_lightSourceMask"
- "T^{__CVBuffer=},N,V_packedDownscaledFirstRGB"
- "T^{__CVBuffer=},N,V_packedDownscaledSecondRGB"
- "T^{__CVBuffer=},N,V_rgbaFirst"
- "T^{__CVBuffer=},N,V_rgbaSecond"
- "T^{__CVBuffer=},N,V_unifiedRGB"
- "T^{__CVBuffer=},R,N,V_backwardFlow"
- "T^{__CVBuffer=},R,N,V_buffer"
- "T^{__CVBuffer=},R,N,V_forwardFlow"
- "T^{__CVBuffer=},R,N,V_normalizedFirst"
- "T^{__CVBuffer=},R,N,V_normalizedSecond"
- "T^{__CVBuffer=},R,N,V_processedPixelBuffer"
- "T^{__CVBuffer=},V_integralSumPixelBuffer"
- "T^{__CVMetalTextureCache=},R,N,V_cvMetalTextureCacheRef"
- "T^{__IOSurface=},N,V_inputSurface"
- "T^{__IOSurface=},N,V_outputSurface"
- "T^{__IOSurface=},N,V_prevHRSurface"
- "T^{e5rt_buffer_object=},R,N,V_outputBufferObject"
- "T^{e5rt_execution_stream=},R,N,V_stream"
- "T^{e5rt_execution_stream_operation=},R,N,V_operation"
- "T^{e5rt_io_port=},R,N,V_output_port"
- "T^{e5rt_program_function=},R,N,V_function"
- "T^{e5rt_program_library=},R,N,V_library"
- "Td,R,N,V_opticalCenterShift"
- "Tf,N,V_confidence"
- "Tf,N,V_errorMaskThreshold"
- "Tf,N,V_errorTolerance"
- "Tf,N,V_maskScaleFactor"
- "Tf,N,V_maskStrength"
- "Tf,R,N"
- "Tf,R,V_sigma"
- "Tf,V_area"
- "Tf,V_dist2ghost"
- "Tf,V_dist2opticalCenter"
- "Tf,V_mvCnt"
- "Tf,V_opticalCenterMvShift"
- "Ti,?,N"
- "Ti,N,V_bytePerPixel"
- "Ti,N,V_flowLevel"
- "Ti,N,V_height"
- "Ti,N,V_stride"
- "Ti,N,V_stridePlane2"
- "Ti,N,V_width"
- "Ti,R,N,V_numLevels"
- "Ti,R,V_num_intervals"
- "Ti,R,V_num_octaves"
- "Ti,V_LSTrackID"
- "Ti,V_LSTrackingVote"
- "Ti,V_lowSaliencyCnt"
- "Ti,V_predictedFromPastCnt"
- "Ti,V_temporalDetectionVote"
- "Ti,V_trackID"
- "Ti,V_trackedCnt"
- "Tq,N"
- "Tq,N,V_bitDepth"
- "Tq,N,V_firstRotation"
- "Tq,N,V_index2RoiArray"
- "Tq,N,V_inputRotation"
- "Tq,N,V_mode"
- "Tq,N,V_revision"
- "Tq,N,V_secondRotation"
- "Tq,N,V_sequenceAdjusterDisplacement"
- "Tq,N,V_stateExt"
- "Tq,N,V_usage"
- "Tq,R,N,V_flowBufferHeight"
- "Tq,R,N,V_flowBufferWidth"
- "Tq,R,N,V_frameHeight"
- "Tq,R,N,V_frameWidth"
- "Tq,R,N,V_motionBlurStrength"
- "Tq,R,N,V_qualityPrioritization"
- "Tq,R,N,V_revision"
- "Tq,R,N,V_roiId"
- "Tq,R,N,V_scaleFactor"
- "Tq,R,N,V_submissionMode"
- "Tq,R,N,V_usage"
- "Tq,V_revision"
- "T{?=fffffI},R,N,V_des"
- "T{?=fffffI},V_descriptor"
- "T{?=iiiiiifffiifiiii{?=ffffffff}{?=iiffffffffffffff}{?=fff}},V_params"
- "T{?=qiIq},N,V_interpolatedFrameDuration"
- "T{?=qiIq},N,V_ispTimeStamp"
- "T{?=qiIq},N,V_presentationTimeStamp"
- "T{?=qiIq},R,N,V_presentationTimeStamp"
- "T{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}},N,V_configuration"
- "T{CGAffineTransform=dddddd},N,V_preferredTransform"
- "T{CGPoint=dd},R,N,V_nextFrameOpticalCenter"
- "T{CGPoint=dd},R,N,V_sourceFrameOpticalCenter"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_extendBBox"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_roi"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_LSRoi"
- "URLForResource:withExtension:"
- "UTF8String"
- "Upsampler"
- "VDGDetectionUtilsV2"
- "VDGProcessor"
- "VEEspressoModel"
- "VEFrameSynthesizer"
- "VEMetalBase"
- "VEMobileAsset"
- "VEOpticalFlow"
- "VEOpticalFlowEstimator"
- "VEOpticalFlowEstimatorConfiguration"
- "VEScaler"
- "VSAProcessor"
- "VSRGetInputFrameSizeForUsage:width:height:"
- "VSRNet"
- "VSRProcessor"
- "VideoDeghostingDetectionV2"
- "Vv16@0:8"
- "Warper"
- "X1"
- "X2"
- "Y1"
- "Y2"
- "[10[8@\"<MTLTexture>\"]]"
- "[1{?=\"features\"[5^{__CVBuffer}]}]"
- "[2@\"<MTLBuffer>\"]"
- "[2@\"<MTLTexture>\"]"
- "[2[10@\"<MTLBuffer>\"]]"
- "[2[80@\"<MTLTexture>\"]]"
- "[2[80^{__CVBuffer}]]"
- "[2^{__CVBuffer}]"
- "[2^{e5rt_buffer_object}]"
- "[2^{e5rt_io_port}]"
- "[2i]"
- "[2{?=\"forwardFlow\"^{__CVBuffer}\"backwardFlow\"^{__CVBuffer}}]"
- "[2{?=\"imageFeature\"{?=\"numLevels\"i\"feature\"[6^{__CVBuffer}]\"tensorSize\"[6{?=\"width\"Q\"height\"Q\"channels\"Q}]\"adaptationLayerFeature\"^{__CVBuffer}\"adaptationLayerTensorSize\"{?=\"width\"Q\"height\"Q\"channels\"Q}}\"baseImageFeature\"{?=\"numLevels\"i\"feature\"[6^{__CVBuffer}]\"tensorSize\"[6{?=\"width\"Q\"height\"Q\"channels\"Q}]\"adaptationLayerFeature\"^{__CVBuffer}\"adaptationLayerTensorSize\"{?=\"width\"Q\"height\"Q\"channels\"Q}}\"subsampledInput\"^{__CVBuffer}\"baseStageInput\"^{__CVBuffer}}]"
- "[2{?=\"storage\"{?=\"correlations\"[6^{__CVBuffer}]\"flows\"[6^{__CVBuffer}]\"upscaledFlows\"[6^{__CVBuffer}]\"warpedImages\"[6^{__CVBuffer}]\"shuffledFlow\"^{__CVBuffer}\"numLevels\"I}\"baseStorage\"{?=\"correlations\"[6^{__CVBuffer}]\"flows\"[6^{__CVBuffer}]\"upscaledFlows\"[6^{__CVBuffer}]\"warpedImages\"[6^{__CVBuffer}]\"shuffledFlow\"^{__CVBuffer}\"numLevels\"I}}]"
- "[3@\"<MTLBuffer>\"]"
- "[3@\"<MTLTexture>\"]"
- "[3@\"NSMutableData\"]"
- "[3^{__CVBuffer}]"
- "[4@\"RansacEstimation\"]"
- "[5@\"<MTLBuffer>\"]"
- "[5@\"<MTLTexture>\"]"
- "[6@\"OFFlowEstimate\"]"
- "[8@\"<MTLBuffer>\"]"
- "[8@\"MPSImageConvolution\"]"
- "[8]"
- "[8f]"
- "[8i]"
- "[9@\"<MTLComputePipelineState>\"]"
- "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - endLockUsage | Error: Can't create an MAAutoAssetSelector"
- "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - endLockUsage | assetSelector:%@ | Error: %@"
- "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - endLockUsage | assetSelector:%@ | SUCCESS"
- "[VEMobileAsset] getLocalMobileAssetURL - Error during initForClientName: %@"
- "^"
- "^B"
- "^f"
- "^i"
- "^v"
- "^{?=[256@]s}56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "^{?=[5@]}16@0:8"
- "^{?=[5^{__CVBuffer}]}16@0:8"
- "^{?=^{?}ii}"
- "^{?=^{?}ii}16@0:8"
- "^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}"
- "^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16@0:8"
- "^{?={?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}}16@0:8"
- "^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}}16@0:8"
- "^{OpaqueVTPixelTransferSession=}"
- "^{_NSZone=}16@0:8"
- "^{__CFDictionary=}"
- "^{__CFDictionary=}16@0:8"
- "^{__CVBuffer=}"
- "^{__CVBuffer=}16@0:8"
- "^{__CVBuffer=}20@0:8B16"
- "^{__CVBuffer=}24@0:8^{__CVBuffer=}16"
- "^{__CVBuffer=}28@0:8f16Q20"
- "^{__CVBuffer=}28@0:8i16i20i24"
- "^{__CVBuffer=}32@0:8^{__CVBuffer=}16^{__CFDictionary=}24"
- "^{__CVBuffer=}32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
- "^{__CVBuffer=}60@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40f48Q52"
- "^{__CVMetalTextureCache=}"
- "^{__CVMetalTextureCache=}16@0:8"
- "^{__CVPixelBufferPool=}"
- "^{__IOSurface=}"
- "^{__IOSurface=}16@0:8"
- "^{__IOSurfaceAccelerator=}"
- "^{e5rt_buffer_object=}"
- "^{e5rt_buffer_object=}16@0:8"
- "^{e5rt_execution_stream=}"
- "^{e5rt_execution_stream=}16@0:8"
- "^{e5rt_execution_stream_operation=}"
- "^{e5rt_execution_stream_operation=}16@0:8"
- "^{e5rt_io_port=}"
- "^{e5rt_io_port=}16@0:8"
- "^{e5rt_program_function=}"
- "^{e5rt_program_function=}16@0:8"
- "^{e5rt_program_library=}"
- "^{e5rt_program_library=}16@0:8"
- "_4xUpscale"
- "_DoGImagesBuffer"
- "_DoGImagesTexture"
- "_EnableGpuWaitForComplete"
- "_GGDetector"
- "_HomoFlow12"
- "_HomoFlow21"
- "_HorFilterGuass"
- "_IsExtermum"
- "_LSIsHighRisk"
- "_LSOrGGBbox"
- "_LSRoi"
- "_LSTrackID"
- "_LSTrackingMatched"
- "_LSTrackingVote"
- "_PWCflowWithHomographyKernel"
- "_RGBAFormat"
- "_RansacEstimation"
- "_ResizeKernel"
- "_SIFTMatcher"
- "_SIFTSetup"
- "_SubtractKernel"
- "_VerFilterGuass"
- "_X"
- "_Y"
- "_absoluteDiffKernel"
- "_acceptsOpticalFlow"
- "_accumulateOneFrame"
- "_accumulationBuffer"
- "_accuracyMode"
- "_adaptationDecoderClass"
- "_adaptationFeatureExtractor"
- "_adaptationFeatureExtractorClass"
- "_adaptationLayerNeeded"
- "_adaptationLayerOnly"
- "_addMvf0AndMvf1"
- "_adjustedKeyPointsCount"
- "_alignBgAvgYUV"
- "_anchorFrameCMAttachment"
- "_area"
- "_attachmentDictOfInput"
- "_attachmentRGBDict"
- "_avgAlignedRef0"
- "_avgAlignedRef0Texture"
- "_avgAlignedRef1"
- "_avgAlignedRef1Texture"
- "_backwardFlow"
- "_backwardFlowTexture"
- "_backwardLossTexture"
- "_backwardStorage"
- "_backwarp"
- "_backwarpFlowMvf0"
- "_backwarpFlowMvf0Texture"
- "_backwarpFlowMvf1"
- "_backwarpFlowMvf1Texture"
- "_backwarpInterleavedKernel"
- "_backwarpInterleavedWithInterleavedFlowOutputKernel"
- "_backwarpKernel"
- "_backwarpLossInterleavedKernel"
- "_backwarpLossKernel"
- "_backwarpLossWithFlowMagnitudeKernel"
- "_backwarpWithHomographyKernel"
- "_baseFeatureExtractor"
- "_baseFlowEstimator"
- "_baseStage"
- "_baseStageCreated"
- "_baseStageUsage"
- "_bbox"
- "_bboxList"
- "_bboxListLen"
- "_bestErrorBuffer"
- "_bgFlow"
- "_bgFlowTexture"
- "_bicubicRGB"
- "_bicubicRGBTexture"
- "_bicubicSubsampleKernel"
- "_bilinearRescale2ImgsYUV"
- "_bilinearRescaleYUV"
- "_bindTexture"
- "_bitDepth"
- "_blendDCTexturesWithMasks"
- "_blendKernel"
- "_blendRefsYUV"
- "_blendSpatialMitigatedYUV"
- "_blendWarpedImages"
- "_blendWarpedImagesWithMaskAndFlowConsistency"
- "_blendWarpedImagesWithMaskTextures"
- "_blendedDCTexture"
- "_blendedRef0"
- "_blendedRef0Texture"
- "_blendedRef1"
- "_blendedRef1Texture"
- "_blendingParams"
- "_blobSaliencyMap"
- "_blobSaliencyMapTexture"
- "_blurNeeded"
- "_bmRef0"
- "_bmRef0Texture"
- "_bmRef1"
- "_bmRef1Texture"
- "_bmSearch1RefFixedSampleCntYUV"
- "_bmSearch1RefYUV"
- "_bmSearch4RepairYUV"
- "_bmTransfer4RepairYUV"
- "_bmTransferGray"
- "_bmTransferWithRoiRepairMvYUV"
- "_bmTransferYUV"
- "_buf"
- "_buffer"
- "_bufferHeight"
- "_bufferIndex"
- "_bufferWidth"
- "_bytePerPixel"
- "_cachedTexturesFromPixelBuffer:usage:"
- "_calcSIFTDescriptor"
- "_calculateOrientation"
- "_callbackQueue"
- "_centerPoint"
- "_channels"
- "_clampGhostROI:"
- "_closeDesIndex"
- "_collectClusterBgAvg"
- "_collectClusterMaxAndAvgLuma"
- "_collectClusterMaxProb"
- "_collectClusterMv"
- "_collectClusterMvForMotionCue"
- "_collectClusterTempRepairErr"
- "_collectMetaContainers"
- "_collectMvToFuture"
- "_collectOcclusionRegionFlowInfoKernel"
- "_collectOverlapWithRefs"
- "_collectRegionalFlowInfoKernel"
- "_collectWrongFlowStatsKernel"
- "_colorProperties"
- "_combineMapWithRefMap"
- "_combineStillMapKernel"
- "_combineTwoSideDepthKernel"
- "_combinedRGBFlowEdge"
- "_combinedRGBFlowEdgeTexture"
- "_commandQueue"
- "_compileShaders"
- "_computeRgbFlowEdgeKernel"
- "_concatenatedInputBlob"
- "_concurrentDualFlowProcessing"
- "_concurrentQueue"
- "_concurrent_queue"
- "_conditionalDilateProbMapYUV"
- "_confidence"
- "_configuration"
- "_configure"
- "_connectedPixelsQueue"
- "_consistencyComputeKernel"
- "_consistencyNormalizationKernel"
- "_consistencyUpscalingKernel"
- "_context"
- "_convert2Texture"
- "_convert2TextureWithMask"
- "_convert2depthKernel"
- "_convertFloatBuffer2Texture"
- "_convertPackToArrayKernel"
- "_convertPackedRGBA2Gray"
- "_convertPlanerRGBA2Gray"
- "_copyCurrMetaForProcFuture"
- "_copyFullFrameMapToMap4RoiGen"
- "_copyImageTileFromPixelBuffer:mergeWithMask:outputTilePixelBuffer:commandBuffer:"
- "_copyImageTileFromPixelBuffer:outputImageTileTexture:commandBuffer:"
- "_copyMapToMap4RoiGen"
- "_copyMvf"
- "_copyOneChannelTextureKernel"
- "_copyRgbTo4x4ShuffledTextureArray"
- "_copyRgbToTextureArray"
- "_copyTextureArrayToRgb"
- "_copyTextureKernel"
- "_correctFlowWithHomographyKernel"
- "_correctFlowWithSameBaseFlowKernel"
- "_correctedForwardFlow"
- "_correctedForwardFlowForwarpBuffer"
- "_correctedForwardFlowHoleMap"
- "_correctedForwardFlowHoleMapTexture"
- "_correctedForwardFlowTexture"
- "_correlation"
- "_correlationKernel"
- "_correlationSIMDKernel"
- "_correlationWithConcatKernel"
- "_correlationWithConcatSIMDKernel"
- "_createOcclusionMask"
- "_currMetaTmp"
- "_currSegmentProcessedFrameCnt"
- "_currentLRRGB"
- "_currentLRYUV"
- "_cvMetalTextureCacheRef"
- "_dcBufferPool"
- "_deblockKernel"
- "_debugImage"
- "_defaultOpticalCenter"
- "_denormalizeKernel"
- "_denormalizeRGBKernel"
- "_denormalizeToPlanarKernel"
- "_denormalizeYCbCr10RenderKernel"
- "_denormalizeYCbCr10UnpackedRenderKernel"
- "_denormalizeYCbCr8RenderKernel"
- "_denormalizedBufferPool"
- "_depth"
- "_depthTexture"
- "_des"
- "_descriptor"
- "_descriptors"
- "_destinationFrame"
- "_destinationFrames"
- "_detectedGreenGhostInfo"
- "_detectionUtils"
- "_device"
- "_differenceOfGaussianAndLumaFeature"
- "_differenceOfGaussianAndLumaFeaturePredictedLocation"
- "_differenceOfGaussianAndLumaFeatureReflection"
- "_dilateEdgeMap"
- "_dilateEdgeMapKernel"
- "_dilateEdgeMapTexture"
- "_dilateForwarpHoleMap"
- "_dilateGrayImg"
- "_dilateProbMap"
- "_dilateReflLsMap"
- "_dilatedBackwardMask"
- "_dilatedFlowRef0Map"
- "_dilatedFlowRef0MapTexture"
- "_dilatedFlowRef1Map"
- "_dilatedFlowRef1MapTexture"
- "_dilatedForwardMask"
- "_dilatedLsMap"
- "_dilatedLsMapTexture"
- "_disableOutputFlowScaling"
- "_disableSIMDSum"
- "_dispatchGroup"
- "_dist2OpticalCenterList"
- "_dist2OpticalCenterListLen"
- "_dist2ghost"
- "_dist2opticalCenter"
- "_dlSpaBlendMask"
- "_dlSpaBlendMaskTexture"
- "_dlSpaInput"
- "_dlSpaInputTexture"
- "_dlSpaRepairMask"
- "_dlSpaRepairMaskTexture"
- "_dlSpatialMitigated"
- "_dlSpatialMitigatedTexture"
- "_doneKPToBBoxViaGraphTraversal"
- "_downsampling"
- "_downscaleDepthKernel"
- "_downscaleFirstImageTexture"
- "_downscaleImage1Texture"
- "_downscaleImage2Texture"
- "_downscaleImageKernel"
- "_downscalePackedImageKernel"
- "_downscaleSecondImageTexture"
- "_dsConflictMap"
- "_dsConflictMapTexture"
- "_dsFlowEdge"
- "_dsFlowEdgeTexture"
- "_effectiveFlowResolution"
- "_effectiveFrameResolution"
- "_encodeRansacEstimation"
- "_engine"
- "_errRescaleProbMap0"
- "_errRescaleProbMap0Texture"
- "_errRescaleProbMap1"
- "_errRescaleProbMap1Texture"
- "_errorMapDilation"
- "_errorMapDownsampleKernel"
- "_errorMask"
- "_errorMaskTexture"
- "_errorMaskThreshold"
- "_errorTolerance"
- "_espressoContext"
- "_espressoEngine"
- "_espressoInputImageBuffer"
- "_espressoInputMaskBuffer"
- "_espressoNetwork"
- "_espressoOutputBuffer"
- "_espressoPlan"
- "_espresso_base_name"
- "_espresso_file"
- "_extendBBox"
- "_extendDepthInStillRegionKernel"
- "_extendedConflictMap"
- "_extendedConflictMapTexture"
- "_featureBackwarpKernel"
- "_featureCreated"
- "_featureExtractor"
- "_featureExtractorClass"
- "_features"
- "_fgFlow"
- "_fgFlowTexture"
- "_fillHrConflictMapKernel"
- "_fillKernel"
- "_filterClosePairKernel"
- "_filterErrorMap"
- "_filterErrorMapByGaussian"
- "_filteredBackwarLossTexture"
- "_filteredDCTexture"
- "_filteredForwardLossTexture"
- "_filteredOpticalCenterShift"
- "_finalCount"
- "_findBestMatch"
- "_findBestMatchEarlyExist"
- "_findBestMatchOptimized"
- "_findBoundingBoxesWithSizeThreshold:LsThreshold:scalingFactor:validWidth:validHeight:"
- "_firstFeatures"
- "_firstForwarpInputWithConsistencyMap"
- "_firstFrame"
- "_firstParamBuffer"
- "_firstRotation"
- "_firstTexture"
- "_firstWarpedTexture"
- "_flow1"
- "_flow1Texture"
- "_flow2"
- "_flow2Texture"
- "_flowAdaptation"
- "_flowBackward"
- "_flowBackwardTexture"
- "_flowBufferHeight"
- "_flowBufferPixelFormat"
- "_flowBufferWidth"
- "_flowConsisteny"
- "_flowDerivedSetup"
- "_flowEdgeInterleavedKernel"
- "_flowEdgeKernel"
- "_flowEstimator"
- "_flowEstimatorClass"
- "_flowFailureDetection"
- "_flowFailureDetectionKernel"
- "_flowForward"
- "_flowForwardTexture"
- "_flowHeight"
- "_flowLevel"
- "_flowMvf0"
- "_flowMvf0Texture"
- "_flowMvf1"
- "_flowMvf1Texture"
- "_flowNet"
- "_flowOnlyMode"
- "_flowPairs"
- "_flowPreprocessor"
- "_flowRef"
- "_flowRef0Map"
- "_flowRef0MapTexture"
- "_flowRef1Map"
- "_flowRef1MapTexture"
- "_flowRefTexture"
- "_flowReshuffleKernel"
- "_flowReshuffleTo2CKernel"
- "_flowSplattingWarpKernel"
- "_flowTarget"
- "_flowTargetTexture"
- "_flowToVelocity"
- "_flowUpscale"
- "_flowUpscale1CKernel"
- "_flowUpscale2CTo1CKernel"
- "_flowUpscale2CTo2CKernel"
- "_flowUpscaleBothInterleavedKernel"
- "_flowUpscaleHighresUpscaleKernel"
- "_flowUpscaleKernel"
- "_flowUpscaleLowresClusterKernel"
- "_flowUpscaleOutputInterleavedKernel"
- "_flowUsage"
- "_flowWidth"
- "_flow_find_match_kernel"
- "_forceGpuWaitForComplete"
- "_forerunner"
- "_forerunnerKernel"
- "_forerunnerTexture"
- "_format"
- "_forwardFlow"
- "_forwardFlowTexture"
- "_forwardLossTexture"
- "_forwardStorage"
- "_forwarp"
- "_forwarpLossTrackKernel"
- "_forwarpOutputBuffer0"
- "_forwarpOutputBuffer1"
- "_frNetEngine"
- "_frameHeight"
- "_framePipeline"
- "_framePreferredPixelFormats"
- "_frameSupportedPixelFormats"
- "_frameSyncRequired"
- "_frameT"
- "_frameTMinus1"
- "_frameTMinus1Texture"
- "_frameTMinus2"
- "_frameTMinus2Texture"
- "_frameTPlus1Buf"
- "_frameTPlus1Texture"
- "_frameTPlus2Buf"
- "_frameWidth"
- "_fullRange"
- "_fullResRawRefinedProbMap"
- "_fullResRawRefinedProbMapTexture"
- "_fullResStashedProbMap4FutureTracking"
- "_fullResStashedProbMap4FutureTrackingTexture"
- "_fullSizeSplatting"
- "_fullWarpStartLevel"
- "_fullresFlow"
- "_fullresFlowTexture"
- "_fullresGuideImageTexture"
- "_function"
- "_fuse4DetectionYUV"
- "_futureFramesToDetectionAndRepair"
- "_futureInputParamsToRepair"
- "_futureMeta4LsCheck"
- "_futureMeta4RedoTracking"
- "_futureMetaTmp"
- "_gauss1"
- "_gauss2"
- "_gauss3"
- "_gaussPyrImagesBuffer"
- "_gaussPyrImagesTexture"
- "_gaussian3x3CoefficientBuffer"
- "_gaussian3x3FilterKernel"
- "_gaussian3x3FilterSIMDKernel"
- "_gaussian3x3SubsampleKernel"
- "_gaussian5x5CoefficientBuffer"
- "_gaussian5x5FilterKernel"
- "_gaussianCoefficientBuffer"
- "_gaussianFilteredTexture1"
- "_gaussianFilteredTexture2"
- "_gaussianSubsampleKernel"
- "_genericFlow"
- "_getBgAvgYUV"
- "_getBlobSaliency"
- "_getGhostProbMapYUV"
- "_getLsMapYUV"
- "_getMotionMapYUV"
- "_getMvForMotionCueFromMvf"
- "_getMvFromLs"
- "_getMvToFutureFromMvf"
- "_getOverlapWithRefs"
- "_getProbMapInput:reflLs:trackingRef:trackingRefProb:trackingRefSpaProb:trackingRefErrRescaleProb:trackingRefLs:inputBuf:reflLsBuf:trackingRefBuf:trackingRefProbBuf:trackingRefSpaProbBuf:trackingRefErrRescaleProbBuf:trackingRefLsBuf:trackingMvf:metaBuf:metaBufArray:trackingRefMetaBuf:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:refinedReflLs:probMapStash4FutureTracking:probMapBuf:errRescaleProbMapBuf:rawRefinedProbMapBuf:refinedProbMapBuf:refinedReflLsBuf:probMapStash4FutureTrackingBuf:doTracking:waitForComplete:"
- "_getProbMapsLiteTarget:refProbMap:refLsMap:refRefinedLsMap:refProbMapStash4FutureTracking:refErrRescaleProbMap:refRawRefinedProbMap:refRefinedProbMap:mvf:probMap:lsMap:refinedLsMap:probMapStash4FutureTracking:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:metaBufArray:waitForComplete:"
- "_getRoiMaxAndAvgLumaYUV"
- "_getRoiRepairMvFromMvf"
- "_getSaliencyMapYUV"
- "_getTempRepairedBgAlignErrYUV"
- "_ggmController"
- "_grayBuf0"
- "_grayBuf0Texture"
- "_grayBuf1"
- "_grayBuf1Texture"
- "_height"
- "_highResPaddedHeight"
- "_highResPaddedWidth"
- "_highResolutionNormalizedBufferPool"
- "_highResolutionRGBABufferPool"
- "_highres"
- "_highresStorage"
- "_hmgrphyRef0"
- "_hmgrphyRef0Texture"
- "_hmgrphyRef1"
- "_hmgrphyRef1Texture"
- "_holeMapKernel"
- "_homo12good"
- "_homographyFlow"
- "_hrStillMap"
- "_hrStillMapTexture"
- "_image0Texture"
- "_image1Texture"
- "_image2motion"
- "_imageDimensions"
- "_imageGuideUpscale"
- "_imageProcessUtility"
- "_imageProcessor"
- "_imageSREngine"
- "_imageUpsampleRGBPackedKernel"
- "_index2RoiArray"
- "_info"
- "_initDetection:futureFrames:outputImgBufTMinus1:outputImgBufTMinus2:"
- "_initParamsWithLowLight:"
- "_initializeBest"
- "_initializeTextureKernel"
- "_initializeTexture_oneChannelKernel"
- "_inlierIndices"
- "_input4MotionCue"
- "_input4MotionCueTexture"
- "_inputBlob"
- "_inputBlobs"
- "_inputBuffer"
- "_inputBufferObject"
- "_inputBufferObjects"
- "_inputCopy"
- "_inputCopyTexture"
- "_inputFlowScaling"
- "_inputHeight"
- "_inputImage"
- "_inputImageTexture"
- "_inputIsPortrait"
- "_inputParamsToRepair"
- "_inputPixelFormat"
- "_inputPortName"
- "_inputPortNames"
- "_inputROI"
- "_inputRotation"
- "_inputScaling"
- "_inputSurface"
- "_inputTexture"
- "_inputType"
- "_inputWidth"
- "_input_port"
- "_input_ports"
- "_integralSumPixelBuffer"
- "_interleaved"
- "_intermediateFlow"
- "_internalHrFlow"
- "_internalHrFlowTexture"
- "_internalResult"
- "_internalResultTexture"
- "_interpolatedFrameDuration"
- "_interpolationPhase"
- "_isFirstFrameInStream"
- "_isFullRange"
- "_isPredictedFromPast"
- "_isReflectedLS"
- "_isTracked"
- "_isTrajectoryPruningPassed"
- "_isYUV"
- "_isYUV422"
- "_ispTimeStamp"
- "_keyPoints"
- "_keyPointsCount"
- "_keyPointsList"
- "_kpIsFromHW"
- "_kpIsFromHWList"
- "_kpIsFromHWListLen"
- "_laplacianMask"
- "_lastFrame"
- "_lastFrameDuration"
- "_lastFramePts"
- "_lastFramesToSynthesize"
- "_legacyNormalization"
- "_level"
- "_library"
- "_lightSourceMask"
- "_limitBilinearInterpolation"
- "_linePredictOutput"
- "_linePredictOutput_finalStage"
- "_linePredictOutput_lowres"
- "_linearSplatting"
- "_locationList"
- "_locationListLen"
- "_logFilter"
- "_lookaheadFrameProcessedInFinish"
- "_lookaheadFrames"
- "_lowResPaddedHeight"
- "_lowResPaddedWidth"
- "_lowResolutionNormalizedBufferPool"
- "_lowSaliencyCnt"
- "_lowres"
- "_lowresStorage"
- "_lrBmRef0"
- "_lrBmRef0Texture"
- "_lrBmRef1"
- "_lrBmRef1Texture"
- "_lrHwLsMask0"
- "_lrHwLsMask0Texture"
- "_lrHwLsMask1"
- "_lrHwLsMask1Texture"
- "_lrRgb"
- "_lrRgbTexture"
- "_lsHasBeenUsedForTrackingGhost"
- "_lsMap4RoiGen"
- "_lsMap4RoiGenTexture"
- "_lsMapQueue"
- "_lsMapTexQueue"
- "_lumaFeatureVector"
- "_lumaFeatureVectorPredictedLocation"
- "_lumaFeatureVectorReflection"
- "_maskKernel"
- "_maskScaleFactor"
- "_maskStrength"
- "_maskToRoi"
- "_matchFlowDimensions"
- "_matchOutputDimensions"
- "_matchedLS"
- "_matches"
- "_maxBuffer"
- "_maxRoiHeight"
- "_maxRoiWidth"
- "_maxTimeGap"
- "_mergeSort"
- "_metaArray"
- "_metaBufArray"
- "_metaBufferArray"
- "_metaContainer"
- "_metaDictionary"
- "_metaInfoQueue"
- "_metalTextureMapped"
- "_metalToolBox"
- "_metalToolbox"
- "_mitigationANE"
- "_mode"
- "_modelPath"
- "_motionBlurEngine"
- "_motionBlurStrength"
- "_motionMap"
- "_motionMapTexture"
- "_mtlLibrary"
- "_mv"
- "_mvCnt"
- "_mvSum"
- "_mvf4Future"
- "_mvf4FutureTexture"
- "_mvf4Repair0"
- "_mvf4Repair0Texture"
- "_mvf4Repair1"
- "_mvf4Repair1Texture"
- "_neighborMaxVelocity"
- "_neighbors"
- "_net"
- "_netSize"
- "_nextFrame"
- "_nextFrameOpticalCenter"
- "_nextIndex"
- "_nextOpticalFlow"
- "_nextOpticalFlowBuffers"
- "_nextVisedOpticalCenter"
- "_normalization"
- "_normalizationParams"
- "_normalizeLumaKernel"
- "_normalizeLumaPacked420Kernel"
- "_normalizePackedToPlanarKernel"
- "_normalizePackedToPlanarWithPackedOutputKernel"
- "_normalizePlanarToPlanarKernel"
- "_normalizePlanarToPlanarWithPackedOutputKernel"
- "_normalizeRGBKernel"
- "_normalizeYUV420ToPlanarKernel"
- "_normalizedBufferPool"
- "_normalizedCurrentLowResLuma"
- "_normalizedCurrentLowResLumaTexture"
- "_normalizedFirst"
- "_normalizedPreviousLowResLuma"
- "_normalizedPreviousLowResLumaTexture"
- "_normalizedRGB"
- "_normalizedSecond"
- "_numLevels"
- "_numWarpedBuffers"
- "_num_intervals"
- "_num_octaves"
- "_numberOfFramesToInsert"
- "_onDemandOpticalFlowBuffersAllocation"
- "_onDemandSynthesisBufferAllocation"
- "_operation"
- "_opticalCenterArray"
- "_opticalCenterArrayIndex"
- "_opticalCenterArrayLen"
- "_opticalCenterMvShift"
- "_opticalCenterMvShiftArray"
- "_opticalCenterShift"
- "_opticalFlow"
- "_opticalFlowBufferPool"
- "_opticalFlowBuffers"
- "_opticalFlowConfig"
- "_opticalFlowNeeded"
- "_opticalFlowOnlyMode"
- "_opticalFlowParams"
- "_opticalFlowProcessor"
- "_opticalFlowSPI"
- "_opticalFlowStroages"
- "_opticalFlowTexture"
- "_originalPTSInNanos"
- "_originalUsage"
- "_outputBlobs"
- "_outputBufferObject"
- "_outputChannels"
- "_outputHeight"
- "_outputPixelFormat"
- "_outputPortName"
- "_outputSR"
- "_outputSurface"
- "_outputWidth"
- "_output_port"
- "_pImageRegInstance"
- "_pMemory"
- "_pMemoryPlane2"
- "_packedDownscaledFirstRGB"
- "_packedDownscaledFirstRGBTexture"
- "_packedDownscaledSecondRGB"
- "_packedDownscaledSecondRGBTexture"
- "_padRGBKernel"
- "_padTexture2CTO1CKernel"
- "_padTexture2CTO2CKernel"
- "_padTextureKernel"
- "_paddingKernel"
- "_params"
- "_partialBackwardDepth"
- "_partialBackwardDepthTexture"
- "_partialForwardDepth"
- "_partialForwardDepthTexture"
- "_partialTwoSideDepth"
- "_partialTwoSideDepthTexture"
- "_pasteRepairedTile:inputTileTexture:blendingMask:outputPixelBuffer:commandBuffer:"
- "_pipelineStates"
- "_pixelFormat"
- "_plan"
- "_postprocessArrayOutputKernel"
- "_postprocessOutput"
- "_postprocessOutputKernel"
- "_postprocessSRFrameYUV420Kernel"
- "_postprocessSRFrameYUV420_2PKernel"
- "_postprocessor"
- "_predictedFromPastCnt"
- "_preferredTransform"
- "_preprocessInputs4MotionCueYUV"
- "_presentationTimeStamp"
- "_prevBack4XFlow"
- "_prevBack4xFlowTexture"
- "_prevBackwardDepth"
- "_prevBackwardDepthTexture"
- "_prevBackwardFlow"
- "_prevBackwardFlowTexture"
- "_prevFlowFailureMask"
- "_prevFlowFailureMaskTexture"
- "_prevHRSurface"
- "_prevIndex"
- "_prevOpticalFlowBuffers"
- "_prevSecondStat"
- "_prevShouldRunGGDetectionClippedPixelBased"
- "_prevShouldRunGGDetectionLSBased"
- "_prevShouldRunGGDetectionLuxLevelBased"
- "_prevStatsBuffer"
- "_prev_quart1"
- "_prev_quart2"
- "_prev_quart3"
- "_prev_quart4"
- "_previousDepth"
- "_previousDepthTexture"
- "_previousFlow"
- "_previousFlowTexture"
- "_previousFrame"
- "_previousFrameAvailable"
- "_previousHRRGB"
- "_previousHRRGBTexture"
- "_previousHighResolutionOutput"
- "_previousLR"
- "_previousLRYUV"
- "_previousOpticalFlow"
- "_previousOutputFrame"
- "_previousPreviousOutputFrame"
- "_probMap4RepairQueue"
- "_probMap4RepairTexQueue"
- "_probMap4RoiGen"
- "_probMap4RoiGenTexture"
- "_probMap4SpatialRepairQueue"
- "_probMap4SpatialRepairTexQueue"
- "_probMapQueue"
- "_probMapTexQueue"
- "_processedFrameCnt"
- "_processedFrameInDetection"
- "_processedFrameNum"
- "_processedPixelBuffer"
- "_processedPrevLSROIs"
- "_processedPrevLSType"
- "_processedROIs"
- "_processedType"
- "_processor"
- "_propagateDepthKernel"
- "_pseudoDepth"
- "_pseudoDepthGenerator"
- "_ptsInNanos"
- "_pyramid"
- "_pyramidLevels"
- "_qualityPrioritization"
- "_rawProbMap"
- "_rawProbMapTexture"
- "_rawWarpedRefProbMap"
- "_rawWarpedRefProbMapTexture"
- "_rawWarpedRefSpaProbMap"
- "_rawWarpedRefSpaProbMapTexture"
- "_readBufferOnly"
- "_ref4MotionCue"
- "_ref4MotionCueTexture"
- "_refineExterma"
- "_refineFutureHwLsMapWithTrackingYUV"
- "_refinedReflLs4trackingRefWarped"
- "_refinedReflLs4trackingRefWarpedTexture"
- "_reflHwLsMask0"
- "_reflHwLsMask0Texture"
- "_reflHwLsMask1"
- "_reflHwLsMask1Texture"
- "_reflectYUVImg2"
- "_reflectedLSList"
- "_reflectedLSListLen"
- "_refreshCalculation"
- "_remainedErrorMask"
- "_remainedErrorMaskTexture"
- "_remainedFlowErrorMask"
- "_remainedFlowErrorMaskTexture"
- "_removeCMAttachment"
- "_repair:outputBuf:ghostROI:inputROI:repairMask:blendMask:"
- "_repairParameters"
- "_resetDetectionResults"
- "_resetIntermediateVariables"
- "_resetOutput"
- "_residueInplaceKernel"
- "_residueKernel"
- "_resourcePreAllocated"
- "_resourcesPreAllocated"
- "_result12"
- "_result21"
- "_reverseFlowKernel"
- "_revision"
- "_rgb1"
- "_rgb1Texture"
- "_rgb2"
- "_rgb2Texture"
- "_rgb2gray"
- "_rgbaBuffersAllocated"
- "_rgbaDownscaleFirst"
- "_rgbaDownscaleFirstTexture"
- "_rgbaDownscaleSecond"
- "_rgbaDownscaleSecondTexture"
- "_rgbaFirst"
- "_rgbaFirstTexture"
- "_rgbaInternalGenerated"
- "_rgbaPixelFormat"
- "_rgbaSecond"
- "_rgbaSecondTexture"
- "_roi"
- "_roiId"
- "_roiMv"
- "_rotation"
- "_saliencyMap"
- "_saliencyMapTexture"
- "_same_scene_frame_count"
- "_scaleFactor"
- "_scaleKernel"
- "_scaledBackwardFlow"
- "_scaledFlowBufferAllocated"
- "_scaledForwardFlow"
- "_scaler"
- "_sceneChange"
- "_scratchSpace"
- "_secondFeatures"
- "_secondForwarpInputWithConsistencyMap"
- "_secondParamBuffer"
- "_secondRotation"
- "_secondWarpedTexture"
- "_selfNormalization"
- "_sequenceAdjusterDisplacement"
- "_sequenceAdjusterRecipe"
- "_setWOri"
- "_sharedBackwardFlow"
- "_sharedEvent"
- "_sharedEventListener"
- "_sharedFlowDimension"
- "_sharedFlowPair"
- "_sharedForwardFlow"
- "_shuffleConcatenateKernel"
- "_sigma"
- "_signalValue"
- "_skipClamp"
- "_skipLastLevel"
- "_skipLastLevelFlow"
- "_smForerunner"
- "_smForerunnerTexture"
- "_smKernelAlpha"
- "_smKernelAlphaTexture"
- "_smoothAlphaKernel"
- "_smoothOnePlaneKernel"
- "_smoothVelocity"
- "_sourceFrame"
- "_sourceFrameOpticalCenter"
- "_spaProbMapQueue"
- "_spaProbMapTexQueue"
- "_spatialMitigated"
- "_spatialMitigatedTexture"
- "_spatialRepairYUV"
- "_spatialTemporalRepair4DetectionYUV"
- "_spiInstance"
- "_splattingKernel"
- "_splattingNormalizationKernel"
- "_srNetHROutput"
- "_srnet"
- "_startTime"
- "_stashedFutureGhostRois0"
- "_stashedFutureGhostRois1"
- "_stateExt"
- "_statisticsPackedKernel"
- "_statisticsPlanarKernel"
- "_statisticsYUV420Kernel"
- "_stream"
- "_streamingMode"
- "_streamingModeChange"
- "_stride"
- "_stridePlane2"
- "_submissionMode"
- "_submissionQueue"
- "_subsampleErrorKernel"
- "_subsampleFlowKernel"
- "_subsampleInputKernel"
- "_subsampleKernel"
- "_subtractKernelOctave"
- "_supportsSIMDShuffle"
- "_syncWeightsOriginal"
- "_synchronizationQueue"
- "_synthesis"
- "_synthesisBackwardFlow"
- "_synthesisFlowDimension"
- "_synthesisFlowPair"
- "_synthesisForwardFlow"
- "_synthesisMode"
- "_temporalDetectionMatched"
- "_temporalDetectionVote"
- "_temporalFiltering"
- "_temporalMitigated"
- "_temporalMitigatedTexture"
- "_testingMode"
- "_textureBinded"
- "_tileConfig"
- "_tileFlowAveKernel"
- "_tileInputImageTexture"
- "_tileInputPixelBuffer"
- "_tileMaxVelocityRun1"
- "_tileMaxVelocityRun2"
- "_tileOutputPixelBuffer"
- "_tileOutputPixelBufferLr"
- "_toolBox"
- "_totalFramePairsProcessed"
- "_totalFramesSynthesized"
- "_trackFail"
- "_trackID"
- "_trackIDsAfterMerge"
- "_trackSessionId"
- "_trackedCnt"
- "_tradSpatialMitigated"
- "_tradSpatialMitigatedTexture"
- "_trajectoryFromPast"
- "_tuningParamDict"
- "_tuningParams"
- "_twoLayerBlendKernel"
- "_twoLayerFlowSplatting"
- "_twoLayerQuarterSizeDC"
- "_twoStageFlow"
- "_unifiedRGB"
- "_unifiedRGBTexture"
- "_unique"
- "_updateBest"
- "_updateOutputFloat"
- "_updateOutputFullWarp"
- "_updateOutputFullWarpMinErrorOffset"
- "_updateOutputLiteWarp"
- "_upsampleScaleKernel"
- "_upsampler"
- "_upscaleErrorKernel"
- "_upscaleFinalFlow"
- "_upscaleFlow"
- "_upscaleFlowTexture"
- "_upscaleProbMap"
- "_upscaleThenReflectLsMap"
- "_upscaledCorrectedForwardFlow"
- "_upscaledCorrectedForwardFlowTexture"
- "_usage"
- "_useAdaptationLayer"
- "_useExternalDepth"
- "_useExternalFlow"
- "_useFloatAtomic"
- "_useFlowConsistencyMap"
- "_useFusedKernel"
- "_useGPUOnlyForPreProcessing"
- "_useHomography"
- "_useHomographyInFlow"
- "_useLaplacianMask"
- "_useMPS"
- "_usePrecomputedFlow"
- "_useSIMD"
- "_useSIMDShuffle"
- "_useSIMDSum"
- "_vertsBuffer"
- "_visedOpticalCenter"
- "_visualizeMvf"
- "_vsaConvert2Texture"
- "_vsaPipeMode"
- "_vtTransferSession"
- "_waitForCompletion"
- "_warpAndBlendTextures"
- "_warpAndBlendTexturesWithConsistency"
- "_warpBlendRGBKernel"
- "_warpErrorKernel"
- "_warpMvf0WithMvf1"
- "_warpMvf0WithMvf1ThenAddToMvf2"
- "_warpOutputBuffer"
- "_warpRefMeta"
- "_warpRefMetaLite"
- "_warpedBackwardFeatures"
- "_warpedFeatureChannels"
- "_warpedFirstTexture"
- "_warpedFlowMvf"
- "_warpedFlowMvfTexture"
- "_warpedForwardFeatures"
- "_warpedHR"
- "_warpedHRTexture"
- "_warpedHwLsMask4Track"
- "_warpedHwLsMask4TrackTexture"
- "_warpedImage"
- "_warpedRefProbMap"
- "_warpedRefProbMapTexture"
- "_warpedReflTrackingRef"
- "_warpedReflTrackingRefTexture"
- "_warper"
- "_width"
- "_xscaleFactor"
- "_yscaleFactor"
- "_yuv2gray"
- "absoluteDifference"
- "absoluteString"
- "accumulateFramesWith:"
- "accuracyMode"
- "adaptFlowFromFirstFeatures:secondFeature:storage:inputFlow:outputFlow:"
- "adaptationLayerOnly"
- "addCompletedHandler:"
- "addObject:"
- "addObjectsFromArray:"
- "adjustExtermaInputTextures"
- "adjustLocalExtremasWithThreshold:waitForComplete:edgeThreshold:ind:"
- "allocResource"
- "allocResourceFlowBasedHomography"
- "allocateAdditionalBuffersForHybridFromFullresResolution:LowresResolution:"
- "allocateBufferAndTextureWithFlowWidth:flowHeight:depthWidth:depthHeight:interleaveFactor:"
- "allocateBuffersWidth:height:channels:bestBuffer:outputBuffer:"
- "allocateCorreleationBuffer:forLevel:extractor:"
- "allocateDepthInternalBuffersWithFlowWidth:flowHeight:depthWidth:depthHeight:interleaveFactor:"
- "allocateFeatureBuffers:"
- "allocateFeatures"
- "allocateFeaturesForUsage:Level:"
- "allocateFlowAndLossTextures"
- "allocateFlowBufferFullSize:"
- "allocateFlowOnlyBufferWithFlowWidth:flowHeight:depthWidth:depthHeight:interleaveFactor:"
- "allocateForwardWarpBuffersForLevel:"
- "allocateForwardWarpInternalBuffers"
- "allocateImageFeature:extractor:"
- "allocateInputBufferObjects"
- "allocateIntermediateStageStorage:baseStage:"
- "allocateIntermediateStorage:"
- "allocateInternalBuffer:"
- "allocateInternalBuffers"
- "allocateInternalBuffersWithLrWidth:lrHeight:hrWidth:hrHeight:interleaveFactor:"
- "allocateInternalStorage:flowWidth:flowHeight:depthWidth:depthHeight:interleaveFactor:"
- "allocateLinearConsistencyMapWithWidth:height:"
- "allocateNormalizedBuffers"
- "allocateOutputBufferObjects"
- "allocateRGBABuffersForBuffer:"
- "allocateResourceWidth:andHeight:ind:"
- "allocateResources"
- "allocateResourcesFromWidth:Height:"
- "allocateScaledFlow"
- "allocateSplattingTextures"
- "allocateSubmodulesBuffersWithFlowWidth:flowHeight:depthFactor:"
- "allocateSynthesisResources:Resolution:lowresRender:"
- "allocateTemporalBuffers"
- "allocateWarpedFeatures"
- "allocteRGBABuffersForBuffer:"
- "analyzeRegionalFlowInformation:depth:quart1_angle:quart2_angle:quart3_angle:quart4_angle:depth_angle:"
- "anchorFrameCMAttachment"
- "approximateDepthWithBackwarpLossFromFirstImage:secondImage:fullresFlow:depth:interleavFactor:timeScale:"
- "area"
- "array"
- "arrayLength"
- "arrayWithCapacity:"
- "arrayWithObjects:"
- "asyncRansacFromMatchedPair:matchCount:homography:index:height:width:"
- "auto-asset interest in content error:%@"
- "autorelease"
- "averageFramesWith:usage:destination:"
- "backwardFlow"
- "backwardLossTextureLevel:"
- "baseStage"
- "baseType"
- "base_image"
- "base_image_buffer"
- "bbox"
- "bestErrorBufferLevel:"
- "bindCVPixelBuffers:correlation:flow:output:"
- "bindInternalTextureFromFirst:warpedFirst:"
- "bindWithMTLTextureFromDownscaledImage:downscaledSecond:forwardFlow:backwardFlow:prevBackwardFlow:depth:interleaveFactor:"
- "bindWithMTLTextureFromDownscaledImage:downscaledSecond:forwardFlow:backwardFlow:prevBackwardFlow:remianedErrorMask:fullresImage:upscaledFlow:depth:interleaveFactor:"
- "bitDepth"
- "blendWarpedResidueForward:backward:withGridNetOutput:timeScale:destination:callback:"
- "blitCommandEncoder"
- "boolValue"
- "boundingBoxForMerge"
- "buf"
- "buffer"
- "bufferBytesPerRow"
- "bufferHeight"
- "bufferWidth"
- "buildModelWithConfiguration:"
- "bundleForClass:"
- "bytePerPixel"
- "bytes"
- "cStringUsingEncoding:"
- "calcAnchorParamsFromNormParams:anchor:"
- "calcBackwarpLoss:second:flow:timeScale:destination:"
- "calcBackwarpLossFirst:second:timeScale:"
- "calcCorrelation:with:output:"
- "calcDeNormParamsFromNormaParams:timeScale:"
- "calcFrameStatistics:"
- "calcTextureStatistics:"
- "calcTextureStatisticsFromStatsBuffer:"
- "calculateBackwarpErrorFromDownscaleFirst:downscaleSecond:backwardFlow:forwardFlow:backwardStorage:forwardStorage:interleave_factor:timeScale:"
- "calculateDescriptorsForKeypoints:keypointsCount:intoHdr:waitForComplete:ind:"
- "calculateOrientations:withCounterBuffer:waitForComplete:ind:"
- "calculateSynthesisRenderResolutionFromInputWidth:InputHeight:"
- "channels"
- "checkForwardFlow:backwardFlow:"
- "checkRun2RunFromMatch1:match2:matchCount1:matchCount2:frameId:"
- "class"
- "cleanResources"
- "clearReferencedROIsForROIList:"
- "clusterIndicesOfRois:withExtendedRadius:roiCnt:imageRect:"
- "colorAttachments"
- "colorSpace"
- "commandBuffer"
- "commandBufferWait:flag:"
- "commit"
- "commitCmdBuffer:waitForComplete:"
- "compare:"
- "compareSelfAsLSWithAnotherLS:"
- "compileModelOnDevice"
- "computeCommandEncoder"
- "computeErrorMask:reference:flow:output:threshold:scaleFactor:"
- "computeForwardFlow:backwardFlow:"
- "computeMaxConsisnteciesForwardConsistencyMap:backwardConsistencyMap:"
- "compute_rgb_flow_edge"
- "concurrentDualFlowProcessing"
- "confidence"
- "configSubModules:"
- "configuration"
- "configureSynthesis"
- "configureSynthesisWithMode:"
- "conformsToProtocol:"
- "containsIndex:"
- "containsObject:"
- "contents"
- "contentsOfDirectoryAtPath:error:"
- "context"
- "contrastThreshold"
- "convertBuffer:toFP16IOSurface:"
- "convertBuffer:toFP16ShuffledIOSurface:"
- "convertFP16IOSurface:toBuffer:"
- "convertHomographyWithFactor:input:"
- "convertInternalBBoxes:outputArray:"
- "convertInternalBBoxesToROI:outputArray:"
- "convertPackedMaskToRegular:output:"
- "convertToRGB:to:withRGBFormat:rotate:"
- "convertToYUV:attachment:"
- "copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:"
- "copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:"
- "copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:"
- "copyRgbTo4x4ShuffledTextureArray"
- "copyTextureWithPaddingSource:destination:"
- "copyTextureWithPaddingSource:destination:callback:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createAccumulationBufferWidth:height:channels:"
- "createBaseLayer"
- "createBestBufferWidth:height:"
- "createConsistencyMapFromFirstImage:secondImage:flowForward:flowBackward:"
- "createFP16TextureFromIOSurface:width:height:arrayLength:"
- "createFeaturePyramid:second:"
- "createFeaturesFromFirstImage:secondImage:flowForward:flowBackward:"
- "createFeaturesFromFirstImage:secondImage:flowForward:flowBackward:skipFirstFramePreProcessing:"
- "createFeaturesFromImage:flowForward:flowBackward:depth:fullresFlow:remainedErrorMask:"
- "createFlowConsistencyMapsWithForwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:"
- "createForwarpOutputBufferWidth:height:channels:"
- "createFunction"
- "createKernel:"
- "createKernel:constantValues:"
- "createKernels"
- "createMaskFrom:to:"
- "createModules"
- "createOcclusionMask"
- "createOutputBufferWidth:height:channels:"
- "createRenderKernel:renderTargetFormat:"
- "createResiduePyramidFromBuffer:toBuffer:levels:"
- "createSubsampledInputsFromFirstFrame:secondImage:"
- "currentStatusSync:"
- "cvMetalTextureCacheRef"
- "d"
- "d16@0:8"
- "dataWithBytes:length:"
- "dataWithLength:"
- "date"
- "dealloc"
- "debugDescription"
- "debugImage"
- "defaultCStringEncoding"
- "defaultManager"
- "defaultOpticalCenter"
- "defaultRevision"
- "denormalizeFrame:destination:params:timeScale:callback:"
- "denormalizeRGB"
- "denormalizeRGB:to:"
- "depth"
- "deriveDepthFromFlowDownscaleFirstImage:downscaleSecondImage:backwardFlow:forwardFlow:destination:interleave_factor:timeScale:"
- "deriveDepthFromForwardFlow:backwardFlow:Destination:"
- "des"
- "description"
- "descriptor"
- "destinationFrame"
- "destinationFrames"
- "detect1:toHdr1:detect2:toHdr2:count1:count2:"
- "detectedGreenGhostInfo"
- "device"
- "dictionary"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "differenceOfGaussianAndLumaFeature"
- "differenceOfGaussianAndLumaFeaturePredictedLocation"
- "differenceOfGaussianAndLumaFeatureReflection"
- "directCoefsWidth"
- "directHorConvFilters"
- "directVerConvFilters"
- "direct_gaussianCoeffs"
- "direct_guassian_kernel_sigmas"
- "disableOutputFlowScaling"
- "dispatchThreadgroups:threadsPerThreadgroup:"
- "dispatchThreads:threadsPerThreadgroup:"
- "dist2ghost"
- "dist2opticalCenter"
- "dlSpatialRepairYUV:output:repairMask:blendMask:inputTex:repairMaskTex:blendMaskTex:wRepairedY:wRepairedUV:metaBuf:"
- "doTrackingToNextFrameCurrMetaWithDetectionResults:currMetaWithMvToFuture:futureMeta:opticalCenter:futureOpticalCenter:futureFrameCnt:doLite:waitForComplete:"
- "doneKPToBBoxViaGraphTraversal"
- "downScaleFrameSource:destination:rotate:waitForCompletion:"
- "downloadAssetWithCompletionHandler:"
- "downloadMobileAssetType:assetSpecifier:forClientName:completionHandler:"
- "downloadMobileAssetWithCompletionHandler:"
- "downloadMobileAssetWithInputType:withCompletionHandler:"
- "downloadProgress"
- "downsampling"
- "drawPrimitives:vertexStart:vertexCount:"
- "dumpDebugBuffer:fileName:debugCnt:"
- "e5rt_buffer_object_get_iosurface(_inputBufferObjects[0], &_inputSurface)"
- "e5rt_buffer_object_get_iosurface(_inputBufferObjects[0], &_prevHRSurface)"
- "e5rt_buffer_object_get_iosurface(_inputBufferObjects[1], &_inputSurface)"
- "e5rt_buffer_object_get_iosurface(_inputBufferObjects[1], &_prevHRSurface)"
- "e5rt_execution_stream_operation_retain_output_port(_operation, _outputPortName.UTF8String, &_output_port)"
- "e5rt_io_port_bind_buffer_object(_input_ports[0], _inputBufferObjects[0])"
- "e5rt_io_port_bind_buffer_object(_input_ports[1], _inputBufferObjects[1])"
- "e5rt_io_port_bind_buffer_object(self.output_port, self.outputBufferObject)"
- "e5rt_io_port_retain_tensor_desc(_input_ports[0], &input_tensor_desc0)"
- "e5rt_io_port_retain_tensor_desc(_input_ports[1], &input_tensor_desc1)"
- "e5rt_tensor_desc_alloc_buffer_object(input_tensor_desc0, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_inputBufferObjects[0])"
- "e5rt_tensor_desc_alloc_buffer_object(input_tensor_desc1, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_inputBufferObjects[1])"
- "edgeThreshold"
- "encode3x3GaussianFilterToCommandBuffer:source:destination:"
- "encodeAccumulateFramesCommandBuffer:input:output:"
- "encodeAddBottomPaddingToCommandBuffer:source:destination:"
- "encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:"
- "encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:"
- "encodeAnalyzeOcclusionRegionToCommandBuffer:flow:depth:countBuffer:vxBuffer:vyBuffer:threadsPerGroup:numThreadgroups:"
- "encodeAnalyzeRegionalFlowInfoToCommandBuffer:flow:range:countBuffer:vxBuffer:vyBuffer:threadsPerGroup:numThreadgroups:"
- "encodeBMSearch1RefToCommandEncoder:target:ref:reflect:normalizedTargetCenter:normalizedRefCenter:bestMatchLoc:meta:"
- "encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:"
- "encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:"
- "encodeBMTransferGrayToCommandEncoder:ref:warpedRef:bestMatchLoc:meta:sf:"
- "encodeBMTransferYUVToCommandEncoder:ref:reflect:normalizedCenter:warpedRef:bestMatchLoc:meta:sf:"
- "encodeBackWarpToCommandBuffer:reference:ToOutput:withHomography:"
- "encodeBackwarpLossToCommandBuffer:first:second:flow:timeScale:destination:"
- "encodeBackwarpLossWithFlowMagnitudeToCommandBuffer:first:second:flow:timeScale:gamma:protectionThreshold:destination:"
- "encodeBestMatchEarlyExist:objectCount:keypt1:toTargetDescriptor:targetCount:keypt2:filteredIndex:matches:commandBuffer:"
- "encodeBestMatchFromFlow:im1:im2:matches:angle:matchCount:flipFlowValue:commandBuffer:"
- "encodeBicubicSubsampleTextureToCommandBuffer:source:destination:"
- "encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:"
- "encodeBilinearRescaleYUV:fullResInput:input:meta:blurBeforeSample:output:"
- "encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:"
- "encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:"
- "encodeBlendTexturesToCommandBuffer:firstWarpedTexture:secondWarpedTexture:forwardErrorMap:backwardErrorMap:synthesizedTexture:timeScale:synthesizedImageWeight:destination:"
- "encodeBlendWarpedFeaturesWithErrorMaskToCommandBuffer:first:second:forwardErrorMap:backwardErrorMap:forwarpConsistency:backwardConsistency:timeScale:destination:"
- "encodeBlendWarpedFeaturesWithErrorMaskToCommandBuffer:first:second:timeScale:destination:"
- "encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:"
- "encodeCollectClusterBgAvgToCommandEncoder:clusterMetaBuf:metaBuf:"
- "encodeCollectClusterMaxAndAvgLuma:clusterMetaBuf:metaBuf:"
- "encodeCollectClusterMaxProb:clusterMetaBuf:metaBuf:"
- "encodeCollectClusterMv:clusterMetaBuf:metaBuf:"
- "encodeCollectClusterMvForMotionCueToCommandEncoder:clusterMetaBuf:metaBuf:"
- "encodeCollectClusterOverlapWithRefs:clusterMetaBuf:metaBuf:"
- "encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:"
- "encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:"
- "encodeCollectMvToFuture:metaBuf:"
- "encodeCombineFlowToCommandBuffer:input:homography:baseWarp:destination:"
- "encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:"
- "encodeCombineTwoSideDepthToCommandBuffer:forwardDepth:backwarpDepth:destination:"
- "encodeComputeRGBandFlowEdgeToCommandBuffer:rgb:flow:destination:edgeThresh:"
- "encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:"
- "encodeConsistencyMapCreationWithFlowToCommandBuffer:firstSource:secondSource:forwardFlow:backwardFlow:firstForwarpInput:secondForwarpInput:"
- "encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:"
- "encodeConvertPack2ArrayToCommandBuffer:input:output:"
- "encodeConvertRGBAFromSource:output:withCoef:waitForComplete:"
- "encodeCopyCurrMetaForProcFuture:metaBuf:outMetaBuf:"
- "encodeCopyFullFrameMapToMap4RoiGenToCommandEncoder:input:output:"
- "encodeCopyMapToMap4RoiGenToCommandEncoder:input:output:metaBuf:"
- "encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:"
- "encodeCopyTextureToCommandBuffer:source:destination:"
- "encodeCorrectFlowToCommandBuffer:input:forwardFlow:inputFlowFailureMask:forwardFlowFailureMask:remainedWrongFlow:outputFlow:isBackwardFlow:"
- "encodeCorrectFlowToCommandBuffer:input:refFlow:homography:"
- "encodeDeblockToCommandBuffer:flow:output:upscaleFactor:"
- "encodeDenormalizationRenderToCommandBuffer:source:destination:params:"
- "encodeDenormalizationToCommandBuffer:source:destination:params:"
- "encodeDenormalizeRGBToCommandBuffer:source:destination:"
- "encodeDiffToCommandBuffer:texture0:texture1:"
- "encodeDilateEdgeMapToCommandBuffer:input:destination:"
- "encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:"
- "encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:"
- "encodeDilateProbMap:input:output:hardDilationRadius:softDilationRadius:meta:"
- "encodeDilateReflLsMap:inputYUV:lsMap:dilatedLsMap:hardDilationRadius:softDilationRadius:meta:"
- "encodeDownscaleDepthToCommandBuffer:input:output:"
- "encodeDownscaleImageToCommandBuffer:input:output:"
- "encodeErrorDownsampleToCommandBuffer:source:destination:"
- "encodeErrorMapDilationToCommandBuffer:forwardSource:backwardSource:forwardDestination:backwardDestination:minimumAdjacentHoleCount:maximumHoleValue:"
- "encodeErrorMapFilteringToCommandBuffer:source:destination:"
- "encodeErrorMapFilteringWithGaussian3x3ToCommandBuffer:source:destination:"
- "encodeErrorMapFilteringWithGaussian5x5ToCommandBuffer:source:destination:"
- "encodeErrorMapFilteringWithGaussianToCommandBuffer:source:destination:"
- "encodeErrorThresholdToCommandBuffer:source:threshold:scaleFactor:mask:"
- "encodeExtendDepthInStillRegionToCommandBuffer:inputDepthMap:stillMap:output:"
- "encodeFeatureBackwarpToCommandBuffer:feature:forwardFlow:backwardFlow:timeScale:destination:"
- "encodeFillHrConflictMapToCommandBuffer:inputDepthMap:extendedMap:stillMap:output:"
- "encodeFillTextureToCommandBuffer:destination:withValue:"
- "encodeFlowEdgeToCommandBuffer:source:destination:edgeThresh:"
- "encodeFlowFailureMaskGenerationToCommandBuffer:backwardFlow:forwardFlow:backwardFlowError:forwardFlowError:backwardErrorMap:forwardHoleMap:isBackwardFlow:"
- "encodeFlowSplattingWarpToCommandBuffer:source:flow:timeScale:destination:"
- "encodeForerunnerToCommandBuffer:velocity:magnitude:depth:neighborMax:tileSize:virtualFrameNum:timeScale:destination:"
- "encodeForwarpLossWithTrackToCommandBuffer:input:flow:output:"
- "encodeForwarpToCommandBuffer:level:firstTexture:secondTexture:firstWarpedTexture:secondWarpedTexture:timeScale:useFlowMagnitude:"
- "encodeForwarpYUVToCommandEncoder:input0:input1:meta:mvf0:mvf1:intermediateOutput0:intermediateOutput1:output0:output1:outputMap0:outputMap1:"
- "encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:"
- "encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:"
- "encodeGetBlobSaliency:inputYUV:blobSaliencyMap:meta:"
- "encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:"
- "encodeGetLsMapYUVToCommandEncoder:input:map:"
- "encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:"
- "encodeGetMvForMotionCueFromMvf:fullResInput:meta:mvf:opticalCenter:refOpticalCenter:"
- "encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:"
- "encodeGetMvToFutureFromMvf:fullResInput:meta:mvf:"
- "encodeGetOverlapWithRefs:input:probMap:metaBuf:"
- "encodeGetRoiMaxAndAvgLumaYUV:target:lsMap:meta:"
- "encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:"
- "encodeGetSaliencyMapToCommandEncoder:target:saliencyMap:meta:"
- "encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:"
- "encodeHighUpscaleToCommandBuffer:lrFlow:rgbFlowEdge:hrImage:flow1:flow2:rgb1:rgb2:internalResult:hrFlow:"
- "encodeHoleMapToCommandBuffer:fromBuffer:toTexture:inputSize:"
- "encodeInitialieBestToCommandBuffer:bestError:"
- "encodeInitialieTextureToCommandBuffer:bestError:"
- "encodeLayerBlendToCommandBuffer:baseLayer:toDestination:"
- "encodeLayerBlendToCommandBuffer:forwardResidue:backwardResidue:withBaseLayer:timeScale:destination:"
- "encodeLinearSplattingToCommandBuffer:input:flow:error:splatBuffer:outputTexture:timeScale:"
- "encodeLowResClusterToCommandBuffer:lrFlow:lrImage:rgbFlowEdge:flow1:flow2:rgb1:rgb2:internalResult:"
- "encodeMapNormalizationToCommandBuffer:consisitencyMap:maxConsistency:"
- "encodeMapUpscalingToCommandBuffer:source:detination:"
- "encodeNeighborMaxFlowToCommandBuffer:tileMax:searchRange:neighborMax:"
- "encodeNormalizationRGBToCommandBuffer:source:destination:"
- "encodeNormalizationToCommandBuffer:fromBuffer:toTexture:inputSize:"
- "encodeNormalizationToCommandBuffer:source:destination:configBuffer:"
- "encodeNormalizationToCommandBuffer:source:destination:normParamBuffer:"
- "encodeNormalizationToCommandBuffer:source:destination:params:"
- "encodeNormalizationToCommandBuffer:source:packedRGB:params:"
- "encodeNormalizeLumaToCommandBuffer:source:destination:"
- "encodePadRGBToCommandBuffer:source:destination:"
- "encodePaddingTextureToCommandBuffer:source:destination:"
- "encodePostprocessOutputToCommandBuffer:input:loss:fullresEdge:destination:"
- "encodePostprocessSRFrameToCommandBuffer:srFrameY:bicubicY:bicubicUV:laplacianMask:outputY:outputUV:"
- "encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:"
- "encodePropagateDepthToCommandBuffer:flow:fgTile:bgTile:scale:destination:"
- "encodeRGB2GrayToCommandBuffer:InputRGB:ToOutput:withCoef:"
- "encodeReShuffleFlowToCommandBuffer:shuffledFlow:previousFlow:destination:"
- "encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:"
- "encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:"
- "encodeResetOutputToCommandEncoder:input:meta:output0:output1:"
- "encodeResidueInplaceToCommandBuffer:base:low:"
- "encodeResiduePyramidToCommandBuffer:fromTexture:toTexture:levels:"
- "encodeResidueToCommandBuffer:base:low:destination:"
- "encodeReverseFlowToCommandBuffer:source:destination:"
- "encodeRun1TileMaxVelocityToCommandBuffer:velocity:magnitude:tileSize:tileMax:"
- "encodeSceneChangeDetectionFromFlowFailureMask:effectiveResolution:"
- "encodeShuffleToCommandBuffer:full:quarter:destination:"
- "encodeSignalEvent:value:"
- "encodeSmoothAlphaMapToCommandBuffer:input:output:"
- "encodeSmoothOnePlaneToCommandBuffer:input:output:"
- "encodeSmoothedVelocityForMotionBlurToCommandBuffer:magnitude:smoothedMagnitude:"
- "encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:"
- "encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:"
- "encodeSplattingNormalizationToCommandBuffer:splattingBuffer:outputTexture:"
- "encodeSplattingToCommandBuffer:input:flow:error:outputBuffer:timeScale:"
- "encodeStatisticsToCommandBuffer:texture:stats:"
- "encodeStillForegroundMapToCommandBuffer:backwardFlowConfMap:forwardFlowConfMap:frFlow:output:"
- "encodeSubsampleErrorToCommandBuffer:source:destination:"
- "encodeSubsampleFlowToCommandBuffer:source:destination:"
- "encodeSubsampleInputToCommandBufferr:source:destination:"
- "encodeSubsampleTextureWith3x3GaussianToCommandBuffer:source:destination:"
- "encodeSubsampleTextureWith5x5GaussianToCommandBuffer:source:destination:clampToEdge:"
- "encodeSubsampleToCommandBuffer:flow:loss:"
- "encodeSubsampleToCommandBufferr:source:destination:kernel:"
- "encodeSyncWeightsOriginal:clusterMetaBuf:metaBuf:"
- "encodeTileBasedNeighborhoodMaxVelocityToCommandBuffer:velocity:magnitude:tileSize:searchRange:Resolution:intermediateTileMax:tileMax:neighborMax:"
- "encodeTileMaxVelocityToCommandBuffer:velocity:tileSize:tileMax:"
- "encodeTilebaseFlowAverageToCommandBuffer:depth:flow:flowEdge:fgTile:bgTile:"
- "encodeToCommandBuffer:first:second:destination:"
- "encodeToCommandBuffer:forwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:"
- "encodeToCommandBuffer:input:flow:error:timeScale:fullWarp:bestError:output:destination:"
- "encodeToCommandBuffer:input:flow:error:timeScale:fullWarp:bestError:outputBuffer:"
- "encodeToCommandBuffer:source:flow:destination:upscaledFlow:"
- "encodeToCommandBuffer:sourceTexture:destinationTexture:"
- "encodeToCommandBufferConvertDepth:fromBuffer:holeMap:failureMask:toTexture:inputSize:"
- "encodeUnomalizedMapCreationToCommandBuffer:forwardFlow:backwardFlow:forwardConsistencyMap:backwardConsistencyMap:"
- "encodeUpdateBestToCommandBuffer:flow:error:timeScale:bestError:"
- "encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:"
- "encodeUpdateOutputToCommandBuffer:input:flow:error:timeScale:fullWarp:bestError:output:"
- "encodeUpsampleRBGPackedToCommandBuffer:source:destination:scaleFactor:"
- "encodeUpsampleScaleToCommandBuffer:sourceTexture:destinationTexture:"
- "encodeUpscaleErrorToCommandBuffer:source:destination:"
- "encodeUpscaleFlowToCommandBuffer:source:destination:"
- "encodeUpscaleFlowToCommandBuffer:source:destination:scaleFactor:rotation:"
- "encodeUpscaleFlowToCommandBuffer:source:upscaleRatio:destination:"
- "encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:"
- "encodeUpscaleThenReflectLsMap:input:normalizedCenter:output:"
- "encodeVSANormalizationToCommandBuffer:fromBuffer:toTexture:inputSize:"
- "encodeVelocityForMotionBlurToCommandBuffer:velocity:magnitude:timeScale:tileSize:searchRange:"
- "encodeVirtualShutterLinePredictionToCommandBuffer:input:flow:timeScale:destination:"
- "encodeVirtualShutterLinePredictionV2ToCommandBuffer:input:velocity:magnitude:smoothedMagnitude:depth:neighborMax:edgeTex:kernelTex:lowresOutput:lowresKernel:tileSize:virtualFrameNum:timeScale:lowresRender:destination:foreruner:"
- "encodeVisualizeMvfToCommandEncoder:fullResTarget:mvf:outMvf:meta:"
- "encodeWaitForEvent:value:"
- "encodeWarpAndBlendFeaturesWithErrorMaskToCommandBuffer:first:second:forwardFlow:backwardFlow:forwardErrorMap:backwardErrorMap:forwarpConsistency:backwardConsistency:timeScale:destination:"
- "encodeWarpBlendToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:"
- "encodeWarpErrorToCommandBuffer:source:reference:flow:error:"
- "encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:"
- "encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:"
- "encodeWarpPyramidToCommandBuffer:forwardFlow:backwardFlow:forwarpConsistency:backwardConsistency:timeScale:destination:"
- "encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:"
- "encodeWarpRefMetaLite:refMetaBuf:outMetaBuf:"
- "encodeYUV2GrayToCommandBuffer:InputYUV:ToOutput:"
- "endAllLocksWithAssetType:assetSpecifier:forClientName:"
- "endAllPreviousLocksOfSelectorSync:forClientName:"
- "endEncoding"
- "endSession"
- "enqueue"
- "errorMaskThreshold"
- "errorTolerance"
- "errorWithDomain:code:userInfo:"
- "errorWithErrorCode:"
- "estimateFlow:correlation:flow:output:callback:"
- "estimateFlowFromFirstFeatures:secondFeature:storage:outputFlow:"
- "estimateFlowLevel:withEstimator:firstFeatures:secondFeatures:correlation:upscaledFlow:warpedImage:prevFlow:outputFlow:waitForComplete:"
- "estimateStageFlowFromFirstFeatures:secondFeature:storage:baseStage:startLevel:lastLevel:startFlow:outputFlow:"
- "estimateTwoWayFlowFromFirstFeatures:secondFeature:storage:outputForwardFlow:outputBackwardFlow:"
- "exchangeObjectAtIndex:withObjectAtIndex:"
- "executeSynchronouslyOperation:onStream:"
- "expectedTimeRemainingSecs"
- "extendBBox"
- "extent"
- "extractFeaturesFromFirst:second:"
- "extractFeaturesFromImage:outputFeatures:"
- "extractFeaturesFromImage:toFeatures:callback:"
- "extractHomographyFromFlow:depth:im1:im2:targetResolution:currentPairFlow:"
- "extractHomographyFromPrev:ToCurr:"
- "extractHomographyFromPrev:ToCurr:calculateIndex:"
- "extractRoiByGraphTraversalInput:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:"
- "f"
- "f16@0:8"
- "f24@0:8@16"
- "f24@0:8i16i20"
- "f28@0:8f16f20f24"
- "f32@0:8@16@24"
- "f32@0:8@16Q24"
- "f48@0:8@16@24@32@40"
- "featureSizeForLevel:"
- "fileExistsAtPath:"
- "fileURLWithPath:"
- "fillBuffer:range:value:"
- "fillImage:withValue:"
- "filterClosedKptPairFromKpt1:kpt2:count1:count2:filteredIndex:commandBuffer:"
- "filterMatchedCnadidateKpt1:kpt2:count1:count2:closedDesIndex:"
- "findMatchesBetweenDescriptor:objectCount:toTargetDescriptor:targetCount:matches:"
- "findMatchesBetweenDescriptorEarlyExist:objectCount:keypt1:toTargetDescriptor:targetCount:keypt2:filteredIndex:matches:"
- "findMatchesBetweenDescriptorOptimized:objectCount:toTargetDescriptor:targetCount:matches:"
- "findMatchesFromFlow:im1:im2:matches:background_angle:matchCount:flipFlowValue:commandBuffer:"
- "findScaleSpaceExtremaWithWaitForComplete:ind:"
- "findTinyKeypointLocationsFromLS:inputTexture:dilation:estimatedOpticalCenter:metalBuffers:maxBufferLength:keypointSampleStepCount:"
- "finishProcessing"
- "firstFeatures"
- "firstForwarpInput"
- "firstFramePixelMean"
- "firstRotation"
- "floatValue"
- "flowAdaptationFirstFrame:secondFrame:inputFlowForward:inputFlowBackward:outputFlowForward:outputFlowBackward:"
- "flowAdaptationFrom:to:inputForwardFlow:inputBackwardFlow:outputForwardFlow:outputBackwardFlow:"
- "flowBufferHeight"
- "flowBufferPixelFormat"
- "flowBufferWidth"
- "flowFailureAndCorrectionFromDownscaleFirstImage:downscaleSecondImage:backwardFlow:forwardFlow:prevBackFlow:remainedErrorMask:effectiveResolution:interleave_factor:timeScale:warmup:"
- "flowFailureDetection"
- "flowFailureDetectionAndCorrectionFromForwardFlow:backwardFlow:inputFlow:backwardStorage:forwardStorage:interleaveFactor:timeScale:remainedErrorMask:warmup:"
- "flowHeight"
- "flowLevel"
- "flowOnlyMode"
- "flowSizeForLevel:"
- "flowUpscaleHighresUpscale"
- "flowUpscaleLowresCluster"
- "flowUpscalingAndPseudoDepthComputingWarmup:"
- "flowUpscalingFromImage:inputFlow:outputFlow:interleave_factor:"
- "flowWidth"
- "flow_count"
- "flow_match"
- "format"
- "forwardFlow"
- "forwardFlowTextureLevel:"
- "forwardLossTextureLevel:"
- "forwardWarpForLevel:feature:flow:error:timeScale:warpedOutput:fullWarp:callback:"
- "forwardWarpForLevel:first:second:timeScale:forwardOutput:backwardOutput:"
- "frameHeight"
- "framePipeline"
- "framePreferredPixelFormats"
- "frameSupportedPixelFormats"
- "frameSyncRequired"
- "frameWidth"
- "freeContext"
- "freeResource"
- "freeResourceFlowBasedHomography"
- "freeResourceFromind:"
- "freeScratchSpace"
- "function"
- "futureFramesToDetectionAndRepair"
- "futureInputParamsToRepair"
- "generateBaseImage:waitForComplete:ind:"
- "generateBoxesForDoGAndLumaAndForLSROIs:prevGGROIs:inputTexture:opticalCenter:metalBuffers:maxBufferLength:"
- "generateBoxesForDoGAndLumaAndForPrevLSROIs:homography:metalBuffers:maxBufferLength:"
- "generateDetectionRoiList:outputArray:"
- "generateDoGImagesOctaveWaitForComplete:ind:"
- "generateDownscaleInputs:highresImage:highresFlow:highresDepth:interleaveFactor:commandBuffer:"
- "generateGaussianImagesWaitForComplete:ind:"
- "generateLocationFromBBox"
- "generateMetaContainerArrayBufFromMetaContainerBuf:imageRect:"
- "generateTrajectoryForROI:isGG:"
- "generateTrajectoryForROIList:isGG:"
- "getAssetStatusWithPercentCompleted:"
- "getBBoxesUsingGraphTraversalFrom:pixValThreshold:bboxSizeThreshold:scaleFactor:roi:returnAsDetectedROI:outputArray:"
- "getBestROIInROIList:referenceROI:"
- "getBytes:bytesPerRow:bytesPerImage:fromRegion:mipmapLevel:slice:"
- "getClosestRoi:forCoord:"
- "getColorConsistentOutputRGBVia:bicubicRGB:laplacianMask:attachment:destinationFrame:"
- "getCommandqueue"
- "getDetectionRoiListFromMeta:outputArray:"
- "getDevice"
- "getDoGPyramidBufferImageOfOctave:andLayer:ind:"
- "getFlowBufferDimensionsFromFrameWidth:frameHeight:revision:"
- "getFlowTarget:ref:targetBuf:refBuf:mvf:backwardMvf:metaBuf:skipRescaling:"
- "getFrameRotation:"
- "getGGCandidatesFromROIList:GGList:"
- "getGaussPyramidBufferImageOfOctave:andLayer:ind:"
- "getGhostTrackIdFromLs:"
- "getHighRiskLS:"
- "getHomographyWithFlowMatches_async:matchCount:imageDim:imageDim:index:homoMatrix:"
- "getHomographyWithMatches:matchCount:keypoints1:Keypoints2:imageDim:imageDim:"
- "getInputPortNames"
- "getLSBBoxesUsingGraphTraversalFrom:roi:pixValThreshold:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:"
- "getLocalMobileAssetURLWithAssetType:assetSpecifier:forClientName:"
- "getLocationMatchCostWith:"
- "getMobileAssetStatusForInputType:percentCompleted:"
- "getMobileAssetStatusWithAssetType:assetSpecifier:forClientName:percentCompleted:"
- "getMobileAssetStatusWithPercentCompleted:"
- "getMotionShiftFromOpticalCenters:opticalCenterArrayLen:opticalCenterMotionShifts:"
- "getMvfToNextFrameForTrackingCurrMeta:lsMap:futureLsMap:lsMapBuf:futureLsMapBuf:opticalCenter:futureOpticalCenter:waitForComplete:"
- "getOutputPortNames"
- "getOutputTensorSize:level:"
- "getPixelAttributesForBuffer:"
- "getPixelBufferAttributes:bitDepth:isYUV:isFullRange:isYUV422:"
- "getPixelFeatureMatchCostWith:"
- "getProbMapsTarget:ref:rawProbMap:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:reflLsMap:refinedReflLsMap:reflLsMap4TrackingRef:metaBuf:metaBufArray:trackingMvf:useRefProbMap:opticalCenter:trackingRefOpticalCenter:waitForComplete:"
- "getReflLsListAsDetectedROIFromMeta:"
- "getReflLsListFromMeta:outputArray:"
- "getReflectedBboxAroundCenter:"
- "getReflectedBboxCenterAroundCenter:"
- "getRoiMvForRoiList:fromMeta:"
- "getSearchLocation:"
- "getTemporalDetectionSearchRadiusForReferenceFrameIndex:minSearchRadius:slope:"
- "getTopGhostsInList:k:opticalCenter:ghostCntGatingTh:"
- "getTopLSInList:k:dist2ghostTol:"
- "getTopLSInListByDroppingBottoms:k:dist2ghostTol:"
- "getTopLSInListByKeepingTops:k:dist2ghostTol:"
- "getTrajectoryMatchingCostGG:"
- "getWarpedFeatureSizeForLevel:tensorSize:"
- "ghostIsHighConfidence:"
- "gradualCoefsWidth"
- "gradualHorConvFilters"
- "gradualVerConvFilters"
- "gradual_gaussianCoeffs"
- "gradual_guassian_kernel_sigmas"
- "hasSuffix:"
- "hash"
- "height"
- "highResPaddedHeight"
- "highResPaddedWidth"
- "i16@0:8"
- "i20@0:8I16"
- "i20@0:8i16"
- "i24@0:8@16"
- "i28@0:8@16i24"
- "i32@0:8@16@24"
- "i48@0:8@16i24@28i36@40"
- "i72@0:8@16@24^{_regional_flow_directions=ff{_regional_range=sssss}}32^{_regional_flow_directions=ff{_regional_range=sssss}}40^{_regional_flow_directions=ff{_regional_range=sssss}}48^{_regional_flow_directions=ff{_regional_range=sssss}}56^{_regional_flow_directions=ff{_regional_range=sssss}}64"
- "i72@0:8@16i24@28@36i44@48@56@64"
- "image2motion"
- "imageByCompositingOverImage:"
- "imageByCroppingToRect:"
- "imageFeatures"
- "imageGuideUpscale"
- "imageWithCVPixelBuffer:options:"
- "imageWithColor:"
- "imageWithContentsOfURL:"
- "index2RoiArray"
- "indexSetWithIndexesInRange:"
- "info"
- "init"
- "initContextWithFile:engine:configuration:usePreCompiled:"
- "initContextWithFilePath:engine:configuration:usePreCompiled:"
- "initExtSubModules"
- "initFlowAdaptationWithError:"
- "initForAssetType:withAssetSpecifier:"
- "initForClientName:selectingAsset:error:"
- "initGolden"
- "initImageWithValue:"
- "initLegacyModeWithUsage:"
- "initOpticalFlowWithQualityPrioritization:revision:error:"
- "initWithAll:commmandQueue:NumberOfOctaveLayers:withSigma:contrastThreshold:edgeThreshold:accuracyMode:"
- "initWithArray:"
- "initWithBbox:"
- "initWithBbox:descriptor:"
- "initWithBuffer:presentationTimeStamp:"
- "initWithBuffer:presentationTimeStamp:info:"
- "initWithCapacity:"
- "initWithCvPixelBuffer:"
- "initWithCvPixelBuffer:skipClamp:readOnly:"
- "initWithDevice:"
- "initWithDevice:commandQueue:"
- "initWithDevice:commmandQueue:"
- "initWithDevice:commmandQueue:flowDerivedHomography:"
- "initWithDevice:commmandQueue:interleaved:"
- "initWithDevice:commmandQueue:mode:"
- "initWithDevice:interleaved:"
- "initWithDevice:kernelWidth:kernelHeight:weights:"
- "initWithDevice:sigma:"
- "initWithDispatchQueue:"
- "initWithFormat:"
- "initWithForwardFlow:backwardFlow:"
- "initWithFrameWidth:FrameHeight:revision:"
- "initWithFrameWidth:FrameHeight:usePrecomputedFlow:"
- "initWithFrameWidth:FrameHeight:usePrecomputedFlow:revision:"
- "initWithFrameWidth:frameHeight:inputType:usePrecomputedFlow:"
- "initWithFrameWidth:frameHeight:qualityPrioritization:revision:"
- "initWithFrameWidth:frameHeight:scaleFactor:inputType:usePrecomputedFlow:qualityPrioritization:revision:"
- "initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:"
- "initWithMetalContext:commandQueue:"
- "initWithMetalContext:commandQueue:imageDimensions:"
- "initWithMetalContext:commandQueue:imageDimensions:netSize:metalToolBox:"
- "initWithMetalContext:commandQueue:tuningParamDict:"
- "initWithMetalToolBox:"
- "initWithMetalToolBox:config:imageDimensions:"
- "initWithMetalToolBox:configuration:tuningParams:"
- "initWithMode"
- "initWithMode:"
- "initWithMode:Device:CommandQueue:"
- "initWithMode:level:"
- "initWithMode:level:revision:"
- "initWithMode:revision:"
- "initWithModelName:configuration:"
- "initWithModelName:usage:"
- "initWithModelPath:inputWidth:inputHeight:"
- "initWithModelPath:usage:useMPS:"
- "initWithOpticalFlow:usage:rotation:"
- "initWithRed:green:blue:"
- "initWithSourceFrame:nextFrame:opticalFlow:interpolationPhase:submissionMode:destinationFrames:"
- "initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:"
- "initWithSourceFrame:nextFrame:previousFrame:nextOpticalFlow:previousOpticalFlow:motionBlurStrength:submissionMode:destinationFrame:"
- "initWithSourceFrame:nextFrame:submissionMode:opticalFlow:"
- "initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:"
- "initWithString:"
- "initWithSubmodules:WithDevice:commandQueue:"
- "initWithSubmodules:WithDevice:commandQueue:flowDerivedHomography:"
- "initWithTrackingSessionId:roiId:andRoi:"
- "initWithTrackingSessionId:roiId:roi:LSRoi:confidence:"
- "initWithTrackingSessionId:roiId:roi:LSRoi:descriptor:propertiesForPostProcPipeVisualization:"
- "initWithTrackingSessionId:roiId:roi:trackId:"
- "initWithUsage:"
- "initWithUsage:device:commandQueue:opticalFlowModeOnly:"
- "initWithUsage:inputWidth:inputHeight:scaleFactor:useMPS:outputSize:"
- "initWithUsage:normalizationMode:"
- "initWithUsage:qualityMode:"
- "initWithUsage:qualityMode:useLegacyNormalization:"
- "initWithWidth:height:configuration:"
- "initWithWidth:height:vsaPipeMode:"
- "initializeInputPorts"
- "initializeModel"
- "inputBuffer"
- "inputHeight"
- "inputParamsToRepair"
- "inputRotation"
- "inputScaling"
- "inputSurface"
- "inputWidth"
- "intValue"
- "integerValue"
- "integralSumPixelBuffer"
- "interestInContentSync:forAssetSelector:"
- "intermedia_base_image"
- "intermedia_base_image_buffer"
- "interpolatedFrameDuration"
- "interpolationPhase"
- "iosurface"
- "isBoxSizeValidForProcessing:AndErodeBy:"
- "isEqual:"
- "isEqualToString:"
- "isFirstFrameInStream"
- "isFullRange"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isPredictedFromPast"
- "isProxy"
- "isReflectedLS"
- "isResourceAllocationNeededWidth:Height:"
- "isSupportedRevision:"
- "isTracked"
- "isTrajectoryPruningPassed"
- "isYUV"
- "ispTimeStamp"
- "keyPointsList"
- "kpIsFromHW"
- "lastIndex"
- "legacyNormalization"
- "length"
- "level"
- "library"
- "lightSourceMask"
- "limitBilinearInterpolation"
- "linearSplatting"
- "loadModel:from:"
- "loadModelFromPath:"
- "locIsInSearchRange:searchLocation:defaultSearchLocation:searchRadius:defaultSearchRange:searchInGivenLocsOnly:"
- "lockContent:withUsagePolicy:withTimeout:completion:"
- "lockContentSync:withTimeout:lockedAssetSelector:newerInProgress:error:"
- "lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:"
- "lowResPaddedHeight"
- "lowResPaddedWidth"
- "lowSaliencyCnt"
- "lsHasBeenUsedForTrackingGhost"
- "lumaFeatureVector"
- "lumaFeatureVectorPredictedLocation"
- "lumaFeatureVectorReflection"
- "mapBufferToTextureWithInterleaveFactor:"
- "mapInternalBufferWithTexture"
- "maskScaleFactor"
- "maskStrength"
- "matchBufferResolution:"
- "matchCount"
- "matchFlow:"
- "matchFlow:toFullSizeFlow:"
- "matchOutputDimensions"
- "matchPixelFormat:"
- "matchScaledBufferResolution:scaleFactor:"
- "matchedLS"
- "maxConsistency"
- "maxTotalThreadsPerThreadgroup"
- "maxValueInTexture:"
- "metaContainer"
- "metaDictionary"
- "mode"
- "modelPath"
- "motionBlurBetweenFirstFrame:secondFrame:forwardFlow:backwardFlow:depth:shutterAngle:destination:withError:"
- "motionBlurForCurrentFrame:futureFrame:prevFrame:prevFlowPair:currFlowPair:shutterAngle:destination:withError:"
- "motionBlurStrength"
- "msrFrameSource:destination:waitForCompletion:"
- "mutableBytes"
- "mv"
- "mvCnt"
- "mvSum"
- "nOctaveLayers"
- "newBufferWithBytes:length:options:"
- "newBufferWithBytesNoCopy:length:options:deallocator:"
- "newBufferWithIOSurface:"
- "newBufferWithLength:options:"
- "newCommandQueue"
- "newComputePipelineStateWithDescriptor:options:reflection:error:"
- "newDefaultLibrary"
- "newFunctionWithName:"
- "newFunctionWithName:constantValues:error:"
- "newLibraryWithURL:error:"
- "newLinearTextureWithDescriptor:offset:bytesPerRow:bytesPerImage:"
- "newRenderPipelineStateWithDescriptor:error:"
- "newSamplerStateWithDescriptor:"
- "newSharedEvent"
- "newTextureCoordinateBufferWithWidth:height:"
- "newTextureViewWithPixelFormat:textureType:levels:slices:"
- "newTextureWithDescriptor:"
- "newTextureWithDescriptor:iosurface:plane:"
- "newTextureWithDescriptor:offset:bytesPerRow:"
- "newVertexBuffer"
- "nextFrame"
- "nextFrameOpticalCenter"
- "nextOpticalFlow"
- "nextVisedOpticalCenter"
- "normalization"
- "normalizeFramesFirstInput:secondInput:firstOutput:secondOutput:callback:"
- "normalizeFramesFirstInput:secondInput:packedFirst:packedSecond:commandBuffer:"
- "normalizeHomography:width:height:"
- "normalizeLuma"
- "normalizeLumaFromFrame:toTexture:"
- "normalizeLumaPacked420"
- "normalizeRGB"
- "normalizeRGB:to:"
- "normalizeWithParmas:firstInput:secondInput:firstOutput:secondOutput:"
- "normalizedFirst"
- "normalizedSecond"
- "notifyListener:atValue:block:"
- "numLevels"
- "num_intervals"
- "num_octaves"
- "numberOfFramesToInsert"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "operation"
- "opticalCenterMvShift"
- "opticalCenterShift"
- "opticalFlow"
- "opticalFlowFirstFrame:secondFrame:flow:"
- "opticalFlowFirstFrame:secondFrame:flowForward:flowBackward:"
- "opticalFlowFirstFrame:secondFrame:flowForward:flowBackward:reUseFlow:"
- "opticalFlowFrom:to:"
- "opticalFlowFrom:to:flow:"
- "opticalFlowOnlyMode"
- "opticalFlowsFrom:to:"
- "opticalFlowsFrom:to:forwardFlow:backwardFlow:"
- "opticalFlowsFrom:to:forwardFlow:backwardFlow:streamingMode:error:"
- "originalPTSInNanos"
- "outputBufferObject"
- "outputChannels"
- "outputHeight"
- "outputPixelFormat"
- "outputPortName"
- "outputSurface"
- "outputWidth"
- "output_port"
- "pMemory"
- "pMemoryPlane2"
- "packedDownscaledFirstRGB"
- "packedDownscaledSecondRGB"
- "padRGB:to:"
- "params"
- "path"
- "pathExtension"
- "pathForResource:ofType:"
- "pathForResource:ofType:inDirectory:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pixelFormat"
- "postProcessFlow:outputFlow:"
- "postProcessNormalizedFrame:output:timeScale:waitForCompletion:"
- "postprocessFlowWithhomographyMatrix21:matrix12:inputForwardFlow:inputBackwardFlow:outputForwardFlow:outputBackwardFlow:downscaleFacttor:"
- "postprocessFrameWithScaler:output:waitForCompletion:"
- "postprocessOutput"
- "postprocessSRFrame:bicubicYUV:laplacianMask:outputYUV:"
- "preProcessFirstInput:secondInput:waitForCompletion:"
- "preProcessHomographyFirstFrame:secondFrame:previousFlow:"
- "preProcessInput:outputGray:"
- "predictFowardFlow:fromBackwardFlow:"
- "predictPrevLSLocation:usingPrevToCurrentHomography:"
- "predictedFromPastCnt"
- "preferredTransform"
- "prepareToProcess:"
- "preprocessFirst:warpedFirst:withHomography:"
- "preprocessFramesFromImage0:Image1:"
- "presentationTimeStamp"
- "preserveCMAttachmentFirstFrame:secondFrame:"
- "prevHRSurface"
- "prevShouldRunGGDetectionClippedPixelBased"
- "prevShouldRunGGDetectionLSBased"
- "prevShouldRunGGDetectionLuxLevelBased"
- "previousFrame"
- "previousFrameAvailable"
- "previousOpticalFlow"
- "previousOutputFrame"
- "previousPreviousOutputFrame"
- "prewarm"
- "process"
- "process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:"
- "process:outputBuf:roi:repairMask:blendMask:wRepairedY:wRepairedUV:"
- "processHwLsMaskAndGetRoisOpticalCenter:inputFrame:prevMetaContainer:considerDist2PrevGhostWhenSort:outputMask:outputMaskTexture:isLowLight:outputArray:"
- "processHwLsMaskNormalizedCenter:input:output:waitForComplete:"
- "processSourceFrame:nextFrame:forwardFlow:backwardFlow:ourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:randomAccessMode:destinationFrame:"
- "processSuperResolutionInputBuffer:outputBuffer:"
- "processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:"
- "processWithDeghostingParams:error:"
- "processWithFirstFrame:secondFrame:forwardFlow:backwardFlow:streamingMode:error:"
- "processWithFrameRateParams:error:"
- "processWithMotionBlurParams:error:"
- "processWithOpticalFlowParams:error:"
- "processWithSuperResolutionParams:error:"
- "processedPixelBuffer"
- "propagatePartialDepth:downscaleFlow:fullResFlow:downscaleWidth:downscaleHeight:downscale_factor:interleaveFactor:commandBuffer:fullresDepth:"
- "properties"
- "proprocessFirst:warpedFirst:withHomography:"
- "pruneGGList:LSBBoxList:reflectedLSBBoxList:getMatchedLS:pruneLS:pruneGG:"
- "pruneGGList:LSList:opticalCenter:costToKeepLS:costToKeepGG:"
- "pruneGhostList:againstReflLsList:dilation:"
- "pruneLSBasedOnDist2Ghost:"
- "pruneUsingTrajectoryGGList:"
- "pseudoDepth"
- "ptsInNanos"
- "purgeResources"
- "q"
- "q104@0:8@16@24@32@40@48@56@64@72@80@88@96"
- "q104@0:8{?=^{__CVBuffer}@@@@@^{__CVBuffer}}1672^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}80^i88^@96"
- "q112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
- "q112@0:8@16@24@32@40@48@56{?=QQQ}64{?=QQQ}88"
- "q114@0:8@16@24{_regional_range=sssss}32@42@50@58{?=QQQ}66{?=QQQ}90"
- "q120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
- "q136@0:8@16@24@32@40@48@56@64@72@80@88@96i104i108f112f116@120@128"
- "q136@0:8@16@24@32i40i44{?=QQQQQQQQ}48@112@120@128"
- "q140@0:8@16@24@32@40f48Q52^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@@@@@@@Q}60{?=QQQQQQQQ}68@132"
- "q144@0:8@1624@32@40@48@56^{__CVBuffer=}6472@80@88@96@104@112@120^{?=[256@]s}128B136B140"
- "q144@0:8@16@24@32@40@48@56@64@72@80@88@96^{?=[256@]s}104@112B120124132B140"
- "q144@0:8{?=QQQQQQQQ}16{?=QQQQQQQQ}80"
- "q148@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136f144"
- "q148@0:8{?=[3]}16{?=[3]}64^{__CVBuffer=}112^{__CVBuffer=}120^{__CVBuffer=}128^{__CVBuffer=}136f144"
- "q156@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136^{?=[256@]s}144B152"
- "q16@0:8"
- "q20@0:8B16"
- "q216@0:8@1624@32@40@48@56@64@72@80@88@96^{__CVBuffer=}104112^{__CVBuffer=}120^{__CVBuffer=}128^{__CVBuffer=}136^{__CVBuffer=}144^{__CVBuffer=}152^{__CVBuffer=}160^{__CVBuffer=}168^{__CVBuffer=}176^{__CVBuffer=}184@192^{?=[256@]s}200B208B212"
- "q24@0:8@16"
- "q24@0:8B16i20"
- "q24@0:8Q16"
- "q24@0:8^q16"
- "q24@0:8^{__CVBuffer=}16"
- "q24@0:8q16"
- "q264@0:8@16@24@32@40@48@56@64^{__CVBuffer=}72^{__CVBuffer=}80^{__CVBuffer=}88^{__CVBuffer=}96^{__CVBuffer=}104^{__CVBuffer=}112^{__CVBuffer=}120@128@136^{?=[256@]s}144@152@160@168@176@184@192@200^{__CVBuffer=}208^{__CVBuffer=}216^{__CVBuffer=}224^{__CVBuffer=}232^{__CVBuffer=}240^{__CVBuffer=}248B256B260"
- "q28@0:8I16I20i24"
- "q32@0:8@16@24"
- "q32@0:8@16B24i28"
- "q32@0:8@16^@24"
- "q32@0:8Q16Q24"
- "q32@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16^@24"
- "q32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
- "q32@0:8f16B20f24i28"
- "q32@0:8q16^@24"
- "q32@0:8q16^q24"
- "q36@0:8@16@24B32"
- "q36@0:8^{__CVBuffer=}16^{__CVBuffer=}24B32"
- "q36@0:8f16Q20^{__CVBuffer=}28"
- "q40@0:8@16@24@32"
- "q40@0:8@16@24B32i36"
- "q40@0:8@16@24^{?=^{__CVBuffer}^{__CVBuffer}}32"
- "q40@0:8@16@24^{__CVBuffer=}32"
- "q40@0:8Q16Q24Q32"
- "q40@0:8^{__CVBuffer=}16@24@32"
- "q40@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32"
- "q40@0:8^{__CVBuffer=}16q24^{__CVBuffer=}32"
- "q44@0:816@24@32B40"
- "q44@0:8@16@24@32f40"
- "q44@0:8@16@24@32i40"
- "q44@0:8@16@24f32@36"
- "q44@0:8@16@24i32@36"
- "q44@0:8@16i24@28B36i40"
- "q44@0:8f16^{__CVBuffer=}20B28Q32B40"
- "q48@0:8@16@2432@40"
- "q48@0:8@16@24@32@40"
- "q48@0:8@16@24@32Q40"
- "q48@0:8@16@24@32^q40"
- "q48@0:8@16@24@32{?=ff}40"
- "q48@0:8@16@24f32f36@40"
- "q48@0:8^{__CVBuffer=}16@24^{__CVBuffer=}32@40"
- "q48@0:8^{__CVBuffer=}16^{?=^{?}ii}24^{__CVBuffer=}32^{__CVBuffer=}40"
- "q48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40"
- "q52@0:8@16@2432B48"
- "q52@0:8@16@24@32@40f48"
- "q52@0:8@16@24@32@40i48"
- "q52@0:8@16@24@32^{__CVBuffer=}40B48"
- "q52@0:8@16@24@32f40@44"
- "q52@0:8@16@24@32f40^{__CVBuffer=}44"
- "q52@0:8@16@24@32f40i44i48"
- "q52@0:8@16@24@32i40@44"
- "q52@0:8@16@24^{_xform2D={?=[3]}fiii}32i40i44i48"
- "q52@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32f40^{__CVBuffer=}44"
- "q52@0:8^{__CVBuffer=}16f24[4f]28i36i40^44"
- "q56@0:8@16@24@3240"
- "q56@0:8@16@24@32@40@48"
- "q56@0:8@16@24@32Q40@48"
- "q56@0:8@16@24@32f40f44@48"
- "q56@0:8Q16Q24Q32Q40Q48"
- "q56@0:8^{__CVBuffer=}16@24@32^{__CVBuffer=}40@48"
- "q60@0:8@16@24@32@40@48i56"
- "q60@0:8@16@24@32@40B48@52"
- "q60@0:8@16@24@32@40f48@52"
- "q60@0:8@16@24@32^{__CVBuffer=}40f48Q52"
- "q60@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40Q48f56"
- "q64@0:8@16@24@32@404856"
- "q64@0:8@16@24@32@40@48@56"
- "q64@0:8@16@24@32@40^i48^i56"
- "q64@0:8@16@24@32@40f48f52@56"
- "q64@0:8@16@24@32{?=QQQ}40"
- "q64@0:8^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@}16Q24Q32Q40Q48Q56"
- "q64@0:8^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@@@@@@@Q}16@24@32@40Q48@56"
- "q64@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56"
- "q64@0:8^{__CVBuffer=}16f24f28i3236B52^@56"
- "q68@0:8@16@24@324048i56B60B64"
- "q68@0:8@16@24@32@40@48@56B64"
- "q68@0:8@16@24@32@40@48@56i64"
- "q68@0:8@16@24@32@40@48Q56f64"
- "q68@0:8@16@24@32@40@48^{?=[256@]s}56B64"
- "q72@0:816@24^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}32B40^{__CVBuffer=}44@52B60^@64"
- "q72@0:8@16@24@3240@48@56@64"
- "q72@0:8@16@24@32@404856@64"
- "q72@0:8@16@24@32@40@48@56@64"
- "q72@0:8@16@24B3236@44@52@60i68"
- "q72@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56Q64"
- "q76@0:8@16@24@32@40@48@56@64B72"
- "q76@0:8@16@24@32@40@48B56@60@68"
- "q76@0:8@16@24@32@40@48i56i60f64@68"
- "q76@0:8@16@24@32@40^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@}48^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@}56Q64f72"
- "q76@0:8@16@24@32B404452@60@68"
- "q76@0:8@16@24@32^{__CVBuffer=}40^{__CVBuffer=}485664B72"
- "q76@0:8@16@24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56@64B72"
- "q80@0:8@16@24@32@40@48@56@64@72"
- "q80@0:8@16@24@32@40@48@56f64f68@72"
- "q80@0:8@16@24@32@40@48Q56f64f68@72"
- "q80@0:8@16@24@32@40@48{?=QQQ}56"
- "q80@0:8@16@24@32^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@}40^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@}48Q56f64@68B76"
- "q80@0:8^{__CVBuffer=}16^{__CVBuffer=}24{?=[3]}32"
- "q84@0:8@16@24@32@40@48@56Q64f72Q76"
- "q84@0:8@16@24@32Q40Q48f56Q60@68@76"
- "q88@0:8@16@24@32@40@4856@64@7280"
- "q88@0:8@16@24@32@40@48@56@64@72@80"
- "q88@0:8@16@24@32@40{_regional_flow_directions=ff{_regional_range=sssss}}48@68B76@80"
- "q88@0:8@16@24@32{?=[3]}40"
- "q88@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40@48@56@64f72f76@80"
- "q88@0:8^{__CVBuffer=}16^{__CVBuffer=}24{CGRect={CGPoint=dd}{CGSize=dd}}3264^{__CVBuffer=}72^{__CVBuffer=}80"
- "q88@0:8^{__CVBuffer=}16^{__CVBuffer=}24{CGRect={CGPoint=dd}{CGSize=dd}}32^{__CVBuffer=}64^{__CVBuffer=}72f80f84"
- "q88@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24f56f60[4f]64i72i76^80"
- "q92@0:8@16@24{?=[3]}32B80@84"
- "q92@0:8^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@@@@@@@Q}16{?=QQQQQQQQ}24B88"
- "q96@0:8@16@24@32@40@48@56@64@72@80@88"
- "q96@0:8@16@24@32@40@48@56{CGSize=dd}64Q80f88B92"
- "q96@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56^{__CVBuffer=}64^{__CVBuffer=}72^{__CVBuffer=}80Q88"
- "q96@0:8{?=^{__CVBuffer}@@@@@^{__CVBuffer}}1672^i80^@88"
- "qualityPrioritization"
- "r*"
- "r^*"
- "ransac_estimation"
- "ratio"
- "readBlurredYValueAtX:Y:"
- "readFloatAtX:Y:"
- "readFourChannelAtX:Y:"
- "readOneChannelAtX:Y:Channel:"
- "readYCbCrValueAtArrayX:ArrayY:"
- "readYCbCrValueAtX:Y:"
- "readYValueAtX:Y:"
- "reflectAroundCenter:"
- "refreshCalculation"
- "registerImage0:toImage1:Normalize:"
- "release"
- "releaseAccumulationBuffer"
- "releaseAdditionalBufferForHybrid"
- "releaseBufferAndTexture"
- "releaseDepthInternalBuffers"
- "releaseFeatureBuffers:"
- "releaseFeatures"
- "releaseFeaturesForLevel:"
- "releaseForwardWarpInternalTextures"
- "releaseForwardWarpInternalTexturesAndBuffers"
- "releaseForwardWarpLinearBuffersForLevel:"
- "releaseForwardWarpTexturesForLevel:"
- "releaseImageFeature:"
- "releaseIntermediateStageStorage:"
- "releaseIntermediateStorage:"
- "releaseInternalBuffers"
- "releaseNormalizedBuffers"
- "releaseResources"
- "releaseScaledFlow"
- "releaseSplattingTextures"
- "releaseStorage:"
- "releaseSynthesisResources:lowres:"
- "releaseTemporalBuffers"
- "releaseUnusedFeatures:"
- "releaseWarpedFeaturesForIndex:"
- "removeAllObjects"
- "removeDuplicateRois:"
- "removeDuplicatedSorted:keypointsCount:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectsInArray:"
- "removeRedundantLS:"
- "removeRois:thatOverlapRefRois:dilationRadius:"
- "render:toCVPixelBuffer:bounds:colorSpace:"
- "renderCommandEncoderWithDescriptor:"
- "renderPassDescriptor"
- "repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:"
- "replaceRegion:mipmapLevel:slice:withBytes:bytesPerRow:bytesPerImage:"
- "rescaleFrameRangeToCommandBuffer:input:output:"
- "rescaleMetaContainerBuffer:sf:sfInv:"
- "reset"
- "resetBufferResolution"
- "resetFormat"
- "resetIntermediateVariables"
- "resetState"
- "resetStream:"
- "reshuffleFlow:previsouFlow:destination:"
- "resizeImageCmdBuf:inputTexture:withFactorX:withFactorY:outputTexture:"
- "resourceOptions"
- "respondsToSelector:"
- "restoreCMAttachmentToFirstFrame:secondFrame:"
- "restoreCMAttachmentToFirstFrame:secondFrame:synthesizedFrame:"
- "retain"
- "retainCount"
- "retainFeatures"
- "reverseFlowWithSource:destination:"
- "revision"
- "rgbaFirst"
- "rgbaPixelFormatForBuffer:useScaler:"
- "rgbaSecond"
- "roi"
- "roiId"
- "roiMv"
- "s32@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}1624"
- "sampleOneChannelAtX:Y:Channel:"
- "saveBackwardFlow:prevBackwardFlow:"
- "saveInternalStateWithCommandBuffer:"
- "scaleFactor"
- "scaleFrameSource:destination:cropRectangles:upscale:rotate:waitForCompletion:"
- "scaleOutput"
- "scaled_input_texture"
- "scaler"
- "sceneChange"
- "secondFeatures"
- "secondForwarpInput"
- "secondFramePixelMean"
- "secondRotation"
- "self"
- "selfNormalization"
- "sequenceAdjusterDisplacement"
- "sequenceAdjusterRecipe"
- "setAccuracyMode:"
- "setAdaptationLayerOnly:"
- "setAnchorFrameCMAttachment:"
- "setArea:"
- "setArrayLength:"
- "setBaseStage:"
- "setBbox:"
- "setBitDepth:"
- "setBuf:"
- "setBuffer:offset:atIndex:"
- "setBufferHeight:"
- "setBufferWidth:"
- "setBytePerPixel:"
- "setBytes:length:atIndex:"
- "setChannels:"
- "setCompressionFootprint:"
- "setCompressionMode:"
- "setComputeFunction:"
- "setComputePipelineState:"
- "setConcurrentDualFlowProcessing:"
- "setConfidence:"
- "setConfiguration:"
- "setConstantValue:type:withName:"
- "setCreateOcclusionMask:"
- "setDebugImage:"
- "setDefaultControllerConfig"
- "setDefaultOpticalCenter:"
- "setDefaultOpticalCenterForList:opticalCenter:"
- "setDescriptor:"
- "setDetectedGreenGhostInfo:"
- "setDifferenceOfGaussianAndLumaFeature:"
- "setDifferenceOfGaussianAndLumaFeaturePredictedLocation:"
- "setDifferenceOfGaussianAndLumaFeatureReflection:"
- "setDisableOutputFlowScaling:"
- "setDist2ghost:"
- "setDist2opticalCenter:"
- "setDoneKPToBBoxViaGraphTraversal:"
- "setDownsampling:"
- "setEdgeMode:"
- "setEnableGpuWaitForComplete:"
- "setErrorMaskThreshold:"
- "setErrorTolerance:"
- "setExtendBBox:"
- "setFirstFrame:secondFrame:forwardFlow:backwardFlow:"
- "setFirstRotation:"
- "setFlowFailureDetection:"
- "setFlowLevel:"
- "setFlowOnlyMode:"
- "setFormat:"
- "setFragmentBuffer:offset:atIndex:"
- "setFragmentFunction:"
- "setFragmentTexture:atIndex:"
- "setFramePipeline:"
- "setFutureFramesToDetectionAndRepair:"
- "setFutureInputParamsToRepair:"
- "setHeight:"
- "setImage2motion:"
- "setImageGuideUpscale:"
- "setImageblockWidth:height:"
- "setIndex2RoiArray:"
- "setInputBuffer:"
- "setInputHeight:"
- "setInputParamsToRepair:"
- "setInputRotation:"
- "setInputScaling:"
- "setInputSurface:"
- "setInputWidth:"
- "setIntegralSumPixelBuffer:"
- "setInterpolatedFrameDuration:"
- "setIsFirstFrameInStream:"
- "setIsFullRange:"
- "setIsPredictedFromPast:"
- "setIsReflectedLS:"
- "setIsTracked:"
- "setIsTrajectoryPruningPassed:"
- "setIsYUV:"
- "setIspTimeStamp:"
- "setKeyPointsList:"
- "setKpIsFromHW:"
- "setLSIsHighRisk:"
- "setLSOrGGBbox:"
- "setLSTrackID:"
- "setLSTrackingMatched:"
- "setLSTrackingVote:"
- "setLabel:"
- "setLegacyNormalization:"
- "setLevel:"
- "setLightSourceMask:"
- "setLimitBilinearInterpolation:"
- "setLinearSplatting:"
- "setLoadAction:"
- "setLowSaliencyCnt:"
- "setLsHasBeenUsedForTrackingGhost:"
- "setLumaFeatureVector:"
- "setLumaFeatureVectorPredictedLocation:"
- "setLumaFeatureVectorReflection:"
- "setMagFilter:"
- "setMaskScaleFactor:"
- "setMaskStrength:"
- "setMatchOutputDimensions:"
- "setMatchedLS:"
- "setMetaContainer:"
- "setMetaDictionary:"
- "setMinFilter:"
- "setMode:"
- "setModelPath:"
- "setMv:"
- "setMvCnt:"
- "setMvSum:"
- "setNetworkClasses"
- "setNextVisedOpticalCenter:"
- "setNormalization:"
- "setNormalizedCoordinates:"
- "setNumLevels:"
- "setNumberOfFramesToInsert:"
- "setObject:atIndexedSubscript:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOpticalCenterMvShift:"
- "setOpticalFlowOnlyMode:"
- "setOriginalPTSInNanos:"
- "setOutputChannels:"
- "setOutputPixelFormat:"
- "setOutputPortName:"
- "setOutputSurface:"
- "setPMemory:"
- "setPMemoryPlane2:"
- "setPackedDownscaledFirstRGB:"
- "setPackedDownscaledSecondRGB:"
- "setParams:"
- "setPixelFormat:"
- "setPostprocessOutput:"
- "setPredictedFromPastCnt:"
- "setPreferredTransform:"
- "setPresentationTimeStamp:"
- "setPrevHRSurface:"
- "setPrevShouldRunGGDetectionClippedPixelBased:"
- "setPrevShouldRunGGDetectionLSBased:"
- "setPrevShouldRunGGDetectionLuxLevelBased:"
- "setPreviousFrameAvailable:"
- "setPropertiesFromDefaults"
- "setPseudoDepth:"
- "setPtsInNanos:"
- "setRGBAFormat:"
- "setRefreshCalculation:"
- "setRenderPipelineState:"
- "setRepairTuningParams:"
- "setResourceOptions:"
- "setRevision:"
- "setRgbaFirst:"
- "setRgbaSecond:"
- "setRoi:"
- "setRoiMv:"
- "setRoiMvForMeta:fromRoiList:"
- "setSAddressMode:"
- "setSamplerState:atIndex:"
- "setScaleTransform:"
- "setScaler:"
- "setSceneChange:"
- "setSecondRotation:"
- "setSelfNormalization:"
- "setSequenceAdjusterDisplacement:"
- "setSequenceAdjusterRecipe:"
- "setSignaledValue:"
- "setSkipClamp:"
- "setSkipLastLevel:"
- "setSpiInstance:"
- "setStateExt:"
- "setStorageMode:"
- "setStoreAction:"
- "setStreamingMode:"
- "setStride:"
- "setStridePlane2:"
- "setSynthesisMode:"
- "setTAddressMode:"
- "setTemporalDetectionMatched:"
- "setTemporalDetectionVote:"
- "setTemporalFiltering:"
- "setTestingMode:"
- "setTexture:"
- "setTexture:atIndex:"
- "setTextureType:"
- "setTextures:withRange:"
- "setThreadGroupSizeIsMultipleOfThreadExecutionWidth:"
- "setTrackFail:"
- "setTrackID:"
- "setTrackIDsAfterMerge:"
- "setTrackedCnt:"
- "setTrajectoryFromPast:"
- "setTwoLayerFlowSplatting:"
- "setTwoLayerQuarterSizeDC:"
- "setTwoStageFlow:"
- "setUnifiedRGB:"
- "setUsage:"
- "setUseAdaptationLayer:"
- "setUseExternalDepth:"
- "setUseExternalFlow:"
- "setUseFloatAtomic:"
- "setUseFlowConsistencyMap:"
- "setUseFusedKernel:"
- "setUseHomography:"
- "setUseLaplacianMask:"
- "setUseSIMD:"
- "setUseSIMDShuffle:"
- "setUseSIMDSum:"
- "setUserInitiated:"
- "setVertexBuffer:offset:atIndex:"
- "setVertexFunction:"
- "setViewport:"
- "setVisedOpticalCenter:"
- "setWaitForCompletion:"
- "setWidth:"
- "setup"
- "setupKernels"
- "setupMetal"
- "setupMetalGolden"
- "setupNetworkModel"
- "setupResourcesWithFlowDerivedHomography:"
- "shouldCropOutputFrame:"
- "shouldScaleBuffer:"
- "sigma"
- "sigma_diff"
- "skipClamp"
- "skipFirstFramePreProcessing"
- "skipLastLevel"
- "sortArray:ofLength:"
- "sortKPs:opticalCenter:"
- "sortLsList:"
- "sortMatchingPair:matchCount:"
- "sortedArrayUsingSelector:"
- "sourceFrame"
- "sourceFrameOpticalCenter"
- "spiInstance"
- "startSessionWithDeghostingConfig:error:"
- "startSessionWithFlowWidth:flowHeight:frameWidth:frameHeight:useHomographyInFlow:error:"
- "startSessionWithFrameRateConfig:error:"
- "startSessionWithMotionBlurConfig:error:"
- "startSessionWithOpticalFlowConfig:error:"
- "startSessionWithQualityMode:error:"
- "startSessionWithQualityMode:useExternalFlow:streamingMode:pseudoDepth:error:"
- "startSessionWithSuperResolutionConfig:error:"
- "stateExt"
- "statsBufferForTexture:"
- "storages"
- "storeColorProperties:"
- "stream"
- "streamingMode"
- "stride"
- "stridePlane2"
- "stringByAppendingFormat:"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByDeletingPathExtension"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "submissionMode"
- "subsampleInput:to:forUsage:"
- "sumUpStat:bufferLength:"
- "summary"
- "superclass"
- "supportedRevisions"
- "supportsFamily:"
- "switchUsage:"
- "switchUsageTo:"
- "synthesisMode"
- "synthesisTensorSizeForLevel:"
- "synthesizeFrameForTimeScale:destination:"
- "synthesizeFrameForTimeScale:frameIndex:"
- "synthesizeFrameForTimeScale:frameIndex:destination:"
- "synthesizeFrameFromFirstFrame:secondFrame:forwardFlow:backwardFlow:timeScale:destination:"
- "synthesizeFrameFromFirstImage:secondImage:flowForward:flowBackward:timeScale:frameIndex:"
- "synthesizeFrameFromInputImage:fullresFlow:depth:destination:timeScale:frameIndex:"
- "synthesizeFramesFromFirstFrame:secondFrame:forwardFlow:backwardFlow:numberOfFrames:withError:"
- "synthesizeFramesFromFirstFrame:secondFrame:forwardFlow:backwardFlow:timeScales:withError:"
- "synthesizeFromImage:flow:depth:destination:timeScale:downscaleFactor:storage:Resolution:commandBuffer:"
- "synthesizeImageWithFlowSplattingFromFirstImage:secondImage:flowForward:flowBackward:timeScale:destination:"
- "synthesizeImageWithForwarpOnlyFromFirstImage:secondImage:flowForward:flowBackward:timeScale:destination:"
- "synthesizeImageWithVirtualShutterLinePredictionModeFromFirstImage:secondImage:flow:timeScale:destination:"
- "synthesizeImageWithVirtualShutterLinePredictionV2ModeFromImage:flow:depth:timeScale:destination:"
- "synthesizeMotionBlurredFrameForTimeScale:destination:scalerEnabled:frameIndex:lastFrame:"
- "synthesizeMotionBlurredFrames:second:timeScale:destination:scalerEnabled:"
- "temporalDetectionMatched"
- "temporalDetectionVote"
- "temporalFiltering"
- "testingMode"
- "texture2DDescriptorWithPixelFormat:width:height:mipmapped:"
- "textureType"
- "threadExecutionWidth"
- "threadsPerGroupForStats"
- "threeFramePseudoDepthFromForwardFlow:backwardFlow:fullresFlow:destination:flowErrorMask:interleaveFactor:timeScale:downscaleFactor:commandBuffer:"
- "threshold"
- "totalExpectedBytes"
- "totalWrittenBytes"
- "trackFail"
- "trackID"
- "trackIDsAfterMerge"
- "trackMeta:refMeta:currMaxTrackId:"
- "trackSessionId"
- "trackedCnt"
- "trajectoryFromPast"
- "tuningParamDict"
- "twoLayerFlowSplatting"
- "twoLayerFlowSplattingFeatureLevelForLevel:"
- "twoLayerQuarterSizeDC"
- "twoStageFlow"
- "unifiedRGB"
- "unpackIspLsMaskAndRoisForNextFrameLiteWithFrameData:futureOpticalCenter:outputFutureFrameCnt:outputFutureMetaBuf:"
- "unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:outputFutureFrameCnt:outputMTLBuffer:"
- "upScaleAndCropFrameSource:destination:upscale:rotate:waitForCompletion:"
- "updateBest:error:timeScale:best:"
- "updateDoGAndLumaFeaturesWithMetalBuffers:"
- "updateFlowOnlyMode:"
- "updateFlowSize"
- "updateLastFramePts:duration:toSynthesize:"
- "updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:opticalCenterShift:"
- "updateNewRoiPixFea:withRefPixFea:"
- "updateOpticalFlowDimensions"
- "updateOutput:flow:error:timeScale:fullWarp:bestError:output:"
- "updatePrevLSDoGAndLumaFeaturesWithMetalBuffers:"
- "updateRepairedRefYUVInput:opticalCenter:prob:errRescaleProb:prevProb:refinedProb:probMap4TrRefW:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:inputBuf:probBuf:errRescaleProbBuf:prevProbBuf:refinedProbBuf:probMap4TrRefWBuf:frRef0Buf:frRef1Buf:nextFrameBuf:metaBuf:metaBufArray:forceToSpatial:waitForComplete:"
- "updateUsePreviousInfoFromIsFirstFrame:isLastFrame:isRandomAccessMode:effectiveResolution:isInitialization:"
- "upsampleRBGPackedBuffer:to:scaleFactor:"
- "upsampleRGBPackedImage"
- "upscaleFlow:destination:"
- "upscaleFlow:destination:callback:"
- "upscaleFlow:upscaleRatio:destination:"
- "upscaleFlowsForward:backward:"
- "upscaleForwardFlow:backwardFlow:upscaledForwardFlow:upscaledBackwardFlow:"
- "upscaleFrame:destinationHiResFrame:"
- "upscaleFrame:previousLowResFrame:previousHiResFrame:opticalFlow:destinationHiResFrame:"
- "upscaleInputFlow:outFlow:"
- "upscaleRefinedFloV2WithRGB:lrFlow:commandBuffer:interleaveFactor:output:"
- "usage"
- "use4xDownScale:"
- "useAdaptationLayer"
- "useExternalDepth"
- "useExternalFlow"
- "useFloatAtomic"
- "useFlowConsistencyMap"
- "useFusedKernel"
- "useHomography"
- "useLaplacianMask"
- "usePrecomputedFlow"
- "useSIMD"
- "useSIMDShuffle"
- "useSIMDSum"
- "useScalerForPostprocessOutput:"
- "v100@0:8@16@24@32@40@48@56@64@72@80f88@92"
- "v16@0:8"
- "v176@0:8{?=fffffI}16"
- "v188@0:8{?=iiiiiifffiifiiii{?=ffffffff}{?=iiffffffffffffff}{?=fff}}16"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8*16"
- "v24@0:816"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^{?=@@@@@@@@@@@@@@iiiiiiii}16"
- "v24@0:8^{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}16"
- "v24@0:8^{?=^{?}ii}16"
- "v24@0:8^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@}16"
- "v24@0:8^{?=fff}16"
- "v24@0:8^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}16"
- "v24@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16"
- "v24@0:8^{?={?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}}16"
- "v24@0:8^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}}16"
- "v24@0:8^{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v24@0:8^{__CFDictionary=}16"
- "v24@0:8^{__CVBuffer=}16"
- "v24@0:8^{__IOSurface=}16"
- "v24@0:8i16f20"
- "v24@0:8q16"
- "v28@0:816i20i24"
- "v28@0:8@16B24"
- "v28@0:8^f16I24"
- "v28@0:8^{?=QQQ}16I24"
- "v28@0:8^{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}16B24"
- "v28@0:8^{?=^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}^{__CVBuffer}@@@@@@@@@@@Q}16B24"
- "v28@0:8^{_keyPointHdr=ffffiifff}16i24"
- "v28@0:8f16^{__CVBuffer=}20"
- "v28@0:8f16i20i24"
- "v28@0:8i16^{?=QQQ}20"
- "v28@0:8q16i24"
- "v32@0:816"
- "v32@0:8@1624"
- "v32@0:8@16@24"
- "v32@0:8@16^@24"
- "v32@0:8@16^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}24"
- "v32@0:8@16f24f28"
- "v32@0:8@16s24f28"
- "v32@0:8C16i20i24c28"
- "v32@0:8^16^24"
- "v32@0:8^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}16@24"
- "v32@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16@24"
- "v32@0:8^{__CVBuffer=}16^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}}24"
- "v32@0:8^{__CVBuffer=}16^{__CVBuffer=}24"
- "v32@0:8q16@?24"
- "v36@0:8@16@24f32"
- "v36@0:8^^{__CVBuffer}16I24@28"
- "v36@0:8^{__CVBuffer=}16@24i32"
- "v36@0:8^{__CVBuffer=}16^{__CVBuffer=}24B32"
- "v36@0:8^{__CVBuffer=}16^{__CVBuffer=}24f32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16^@24^@32"
- "v40@0:8@16s2428i36"
- "v40@0:8Q16Q24Q32"
- "v40@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}24^i32"
- "v40@0:8^{__CVBuffer=}16^^{__CVBuffer}24Q32"
- "v40@0:8^{__CVBuffer=}16^{__CVBuffer=}24I32B36"
- "v40@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32"
- "v40@0:8^{__CVBuffer=}16^{__CVBuffer=}24f32B36"
- "v40@0:8^{__CVBuffer=}16^{__CVBuffer=}24q32"
- "v40@0:8q16^Q24^Q32"
- "v40@0:8{?=qiIq}16"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16@24@32f40"
- "v44@0:8@16@24f32@36"
- "v44@0:8^{__CVBuffer=}16^{__CVBuffer=}24q32B40"
- "v44@0:8^{_matchPair=iif}16^{_matchPair=iif}24i32i36i40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24@32f40B44"
- "v48@0:8@16@24@32{?=ff}40"
- "v48@0:8@16@24B3236f44"
- "v48@0:8@16@24f32f36@40"
- "v48@0:8@16@24r^@32Q40"
- "v48@0:8^@16^@2432f40f44"
- "v48@0:8^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}}16^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}}24^{?={?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}}32^{__CVBuffer=}40"
- "v48@0:8^{__CVBuffer=}16^{__CVBuffer=}24B32q36B44"
- "v48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40"
- "v48@0:8^{_keyPointHdr=ffffiifff}16^{_keyPointHdr=ffffiifff}24i32i36^{_closedDesIndex=[1000I]i}40"
- "v48@0:8^{_matchPair=iif}16i24^{_keyPointHdr=ffffiifff}28^{_keyPointHdr=ffffiifff}36i44"
- "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "v52@0:8@16@24@32f40@44"
- "v52@0:8@16@24@32{?=ffi}40"
- "v52@0:8I16^q20^B28^B36^B44"
- "v52@0:8^@16^@24^32B40B44B48"
- "v52@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40B48"
- "v52@0:8^{__CVBuffer=}16^{__CVBuffer=}24r^{?=ff[2f][2f]i}32f40@?44"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24i32i36@40@48"
- "v56@0:8Q16Q24Q32^@40^@48"
- "v56@0:8^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}16^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}24^{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}32^{__CVBuffer=}40^{__CVBuffer=}48"
- "v56@0:8^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}}16^{?={?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}^{__CVBuffer}^{__CVBuffer}}24^{?={?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}}32^{__CVBuffer=}40^{__CVBuffer=}48"
- "v56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{?=QQQQIIII}32B40q44B52"
- "v56@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40@?48"
- "v56@0:8^{_flow_matchPair=fffff}16i24Q28Q36i44^{_xform2D={?=[3]}fiii}48"
- "v56@0:8i16@20@28f36@40@48"
- "v60@0:8@16@24@3240^{?=@@@@@@@@@@@@@@iiiiiiii}48i56"
- "v60@0:8@16@24@32@40@48f56"
- "v60@0:8@16@24@32@40f48@52"
- "v60@0:8@16@24f3236^{?=@@@@@@@@@@@@@@iiiiiiii}44i52f56"
- "v60@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40f48^{__CVBuffer=}52"
- "v60@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32f40^{__CVBuffer=}44@?52"
- "v64@0:8@16@24@32@40@48I56f60"
- "v64@0:8@16@24@32f40B44@48@56"
- "v64@0:8@16@24@32{?=QQQ}40"
- "v64@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56"
- "v64@0:8{CGAffineTransform=dddddd}16"
- "v68@0:8@16@24@32@40@48@56f64"
- "v68@0:8@16@24@32@40@48f56@60"
- "v68@0:8@16@24@32@40f48f52f56@60"
- "v68@0:8@16i24@28@36@44@52f60B64"
- "v68@0:8^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}16^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}24^{?=[6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}][6^{__CVBuffer}]^{__CVBuffer}I}32B40i44i48^{__CVBuffer=}52^{__CVBuffer=}60"
- "v68@0:8i16@20@28@36f44@48B56@?60"
- "v72@0:8@16@24@32@40@48@56@64"
- "v72@0:8@16@24@32@40f48B52@56@64"
- "v72@0:8{?=qiIq}16{?=qiIq}40Q64"
- "v76@0:8{?=ff[2f][2f]i}16^{__CVBuffer=}44^{__CVBuffer=}52^{__CVBuffer=}60^{__CVBuffer=}68"
- "v80@0:816"
- "v80@0:8@16@24@32@40@48@56f64f68@72"
- "v80@0:8@16@24@32@40f48B52@56@64@72"
- "v80@0:8@16i24@28@36i44@48@56@64@72"
- "v80@0:8{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}}16"
- "v84@0:8@16@24@32@40@48@56@64f72@76"
- "v84@0:8@16{?=[3]}24^{?=@@@@@@@@@@@@@@iiiiiiii}72i80"
- "v88@0:8I16^@20^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}28^{?=i[6^{__CVBuffer}][6{?=QQQ}]^{__CVBuffer}{?=QQQ}}36^{__CVBuffer=}44^{__CVBuffer=}52^{__CVBuffer=}60^{__CVBuffer=}68^{__CVBuffer=}76B84"
- "valueForKey:"
- "verbose_messages"
- "verbose_state"
- "visedOpticalCenter"
- "waitForCompletion"
- "waitUntilCompleted"
- "waitUntilScheduled"
- "warmpupComputationFromPrevFrame:currFrame:prevFlowPair:"
- "warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toHighResBufferTexture:"
- "warpBlendImageRGB"
- "warpFeatureLevel:timeScale:"
- "warpFeaturesPerLayerWithFlowForward:flowBackward:timeScale:"
- "warpImage:to:withFlow:upscaledFlow:"
- "warpOutputBufferLevel:"
- "warpRoisUsingMv:"
- "warpTrackingRefProbMap:refSpaProbMap:refReflLs:mvf:metaBuf:metaBufArray:waitForComplete:"
- "warpedBackwardFeatures"
- "warpedForwardFeatures"
- "width"
- "writeFloat:X:Y:"
- "writeValue:X:Y:"
- "writeValue:X:Y:Channel:"
- "zone"
- "{?=\"bufArray\"[256@\"<MTLBuffer>\"]\"clusterCnt\"s}"
- "{?=\"data\"^v\"reserved\"^v\"dim\"[4Q]\"stride\"[4Q]\"width\"Q\"height\"Q\"channels\"Q\"batch_number\"Q\"sequence_length\"Q\"stride_width\"Q\"stride_height\"Q\"stride_channels\"Q\"stride_batch_number\"Q\"stride_sequence_length\"Q\"storage_type\"i}"
- "{?=\"features\"[5@\"<MTLTexture>\"]}"
- "{?=\"forwardFlow\"^{__CVBuffer}\"backwardFlow\"^{__CVBuffer}}"
- "{?=\"frameDataArray\"^{?}\"size\"i\"validCount\"i}"
- "{?=\"image\"^{__CVBuffer}\"depth\"^{__CVBuffer}\"flow\"^{__CVBuffer}\"smoothedVelocity\"^{__CVBuffer}\"magnitude\"^{__CVBuffer}\"edge\"^{__CVBuffer}\"tileMaxVelocity\"^{__CVBuffer}\"intermediateTileMaxVelocity\"^{__CVBuffer}\"neighborMaxVelocity\"^{__CVBuffer}\"kernelAlpha\"^{__CVBuffer}\"output\"^{__CVBuffer}\"imageTexture\"@\"<MTLTexture>\"\"depthTexture\"@\"<MTLTexture>\"\"flowTexture\"@\"<MTLTexture>\"\"magnitudeTexture\"@\"<MTLTexture>\"\"smoothedVelocityTexture\"@\"<MTLTexture>\"\"edgeTexture\"@\"<MTLTexture>\"\"tileMaxVelocityTexture\"@\"<MTLTexture>\"\"intermediateTileMaxVelocityTexture\"@\"<MTLTexture>\"\"neighborMaxVelocityTexture\"@\"<MTLTexture>\"\"kernelAlphaTexture\"@\"<MTLTexture>\"\"outputTexture\"@\"<MTLTexture>\"\"tile_size\"Q}"
- "{?=\"internalCfg\"{?=\"clipThreshold\"i\"patchSize\"i\"antiFlareSize\"i\"simpleRefList\"C\"firstFrameReprocess\"C\"cpuDetection\"C\"baselineMitigation\"C\"enableColorMask\"C\"verbose\"C\"cpuMitigation\"C\"initGGarray\"^{__CFArray}}\"externalCfg\"{?=\"lightMode\"i\"homographyType\"i\"detectionType\"i\"tempPatchMode\"i\"frameDelay\"i\"drawBoundingBox\"C\"noMetaData\"C\"backGroundDetection\"C\"LSGatingEnabled\"C\"luxLevelGating\"C\"clippedPixelGatingEnabled\"C}}"
- "{?=\"lightSourceGatingThresholdON\"i\"lightSourceGatingThresholdOFF\"i\"lightSourceSelectionCntLimitNew\"i\"lightSourceSelectionCntLimitAll\"i\"luxLevelGatingThresholdON\"i\"luxLevelGatingThresholdOFF\"i\"lightSourceBoxSizeThreshold\"f\"searchRangeBase\"f\"searchRangeBaseForPreprocessing\"f\"maxAllowedSizeBBox\"i\"maxAllowedOpticalCenterOffset\"i\"costRescaleWhenOpticalCenterIsAvailable\"f\"b4MergeGhostCntSoftGatingTh\"i\"b4MergeGhostCntHardGatingTh\"i\"kpCntSoftGatingTh\"i\"kpCntHardGatingTh\"i\"colorScore\"{?=\"hueLowerRange\"f\"hueUpperRange\"f\"hueThreshold\"f\"saturationLowerThreshold\"f\"saturationUpperThreshold\"f\"valueLowerThreshold\"f\"valueUpperThreshold\"f\"greenDilationNormalizedRadius\"f}\"tempDetect\"{?=\"minVote\"i\"lightSourceMinVote\"i\"searchRadiusMin\"f\"searchRadiusSlope\"f\"lumaDiffThreshold\"f\"motionDiffThreshold\"f\"colorContrastDiffThreshold\"f\"pixFeaMatchThreshold\"f\"kpIsGhostColorThreshold\"f\"kpIsGhostLumaThreshold\"f\"kpIsGhostContrastThreshold\"f\"kpIsGhostBlobContrastThreshold\"f\"kpIsGhostMotionThreshold\"f\"kpIsGhostColorThresholdHigh\"f\"kpIsGhostLumaThresholdHigh\"f\"kpIsGhostMotionThresholdHigh\"f}\"repairParams\"{?=\"repairTargetArea\"f\"repairTargetGhostCntLo\"f\"repairTargetGhostCntHi\"f}}"
- "{?=\"location\"\"KPScore\"f\"colorScore\"f\"confidence\"f\"pixelValueYUVNormalized\"\"localMotionScore\"f\"GGProb\"f\"pixelFeature\"\"pixelFeatureLen\"I\"KPLSDiffVector\"\"trajectoryFromPast\"\"trajectoryToFuture\"}"
- "{?=\"mean\"f\"std_inv\"f\"anchor_mean\"[2f]\"anchor_std\"[2f]\"frame_type\"i}"
- "{?=\"plan\"^v\"network_index\"i}"
- "{?=\"render_width\"Q\"render_height\"Q\"tilemap_width\"Q\"tilemap_height\"Q\"tile_size\"Q\"intermediateTileMap_width\"Q\"intermediateTileMap_height\"Q\"intermediateTile_size\"Q}"
- "{?=\"repairTargetArea\"f\"repairTargetGhostCntLo\"f\"repairTargetGhostCntHi\"f}"
- "{?=\"sum\"f\"sum_of_square\"f}"
- "{?=\"upscaledFlow\"^{__CVBuffer}\"backwarpLoss\"^{__CVBuffer}\"failureMask\"^{__CVBuffer}\"holeMap\"^{__CVBuffer}\"upscaledFlowTexture\"@\"<MTLTexture>\"\"backwarpLossTexture\"@\"<MTLTexture>\"\"failureMaskTexture\"@\"<MTLTexture>\"\"holeMapTexture\"@\"<MTLTexture>\"\"forwarpBuffer\"@\"<MTLBuffer>\"}"
- "{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}"
- "{?=\"width\"i\"height\"i}"
- "{?=QQQQQQQQ}32@0:8Q16Q24"
- "{?=QQQ}16@0:8"
- "{?=QQQ}20@0:8I16"
- "{?=[3]}68@0:8f16{?=[3]}20"
- "{?=[3]}80@0:8{?=[3]}16Q64Q72"
- "{?=ff[2f][2f]i}56@0:8@16@24@32@40@48"
- "{?=fffffI}16@0:8"
- "{?=ffi}48@0:8{?=ff[2f][2f]i}16f44"
- "{?=ff}24@0:8@16"
- "{?=ff}24@0:8^{__CVBuffer=}16"
- "{?=ff}48@0:8{?=ff[2f][2f]i}16i44"
- "{?=iiiiiifffiifiiii{?=ffffffff}{?=iiffffffffffffff}{?=fff}}16@0:8"
- "{?=qiIq}16@0:8"
- "{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}}16@0:8"
- "{CGAffineTransform=\"a\"d\"b\"d\"c\"d\"d\"d\"tx\"d\"ty\"d}"
- "{CGAffineTransform=dddddd}16@0:8"
- "{CGPoint=\"x\"d\"y\"d}"
- "{CGPoint=dd}16@0:8"
- "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
- "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}40@0:8q16q24q32"
- "{RepairTileBlendingParams=\"wRepairedY\"f\"wRepairedUV\"f}"
- "{RepairTileConfiguration=\"size\"}"
- "{_ransacScratchSpace=\"pAllocatedMemory\"^v\"totalMemorySize\"Q\"inlierCount\"Q\"pInlierIndices\"^i\"pRandomIndices\"^i\"pBestInlier\"[2^i]\"pXref_inlier\"^f\"pYref_inlier\"^f\"pXin_inlier\"^f\"pYin_inlier\"^f\"pH1_t\"^f}"
- "{_regional_flow_directions=\"angle\"f\"variance\"f\"range\"{_regional_range=\"min_x\"s\"max_x\"s\"min_y\"s\"max_y\"s\"horizontal\"s}}"
- "{_xform2D=\"matrix\"{?=\"columns\"[3]}\"confidence\"f\"inlierCnt\"i\"width\"i\"height\"i}"
- "{_xform2D={?=[3]}fiii}32@0:8@16@24"
- "{_xform2D={?=[3]}fiii}36@0:8@16@24i32"
- "{_xform2D={?=[3]}fiii}36@0:8^{__CVBuffer=}16^{__CVBuffer=}24B32"
- "{_xform2D={?=[3]}fiii}60@0:8^{_matchPair=iif}16i24^{_keyPointHdr=ffffiifff}28^{_keyPointHdr=ffffiifff}36Q44Q52"
- "{_xform2D={?=[3]}fiii}68@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40{CGSize=dd}48B64"

```
