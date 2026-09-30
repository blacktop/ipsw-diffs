## DeepVideoProcessingCore

> `/System/Library/PrivateFrameworks/DeepVideoProcessingCore.framework/DeepVideoProcessingCore`

```diff

-1.17.0.0.0
-  __TEXT.__text: 0x434f8
-  __TEXT.__auth_stubs: 0xa90
-  __TEXT.__objc_methlist: 0x396c
-  __TEXT.__const: 0x494
-  __TEXT.__cstring: 0x2ad4
-  __TEXT.__oslogstring: 0x1854
-  __TEXT.__gcc_except_tab: 0x160
-  __TEXT.__unwind_info: 0xda0
-  __TEXT.__objc_classname: 0x55b
-  __TEXT.__objc_methname: 0xcbd0
-  __TEXT.__objc_methtype: 0x47c6
-  __TEXT.__objc_stubs: 0x5420
-  __DATA_CONST.__got: 0x2f8
-  __DATA_CONST.__const: 0x240
-  __DATA_CONST.__objc_classlist: 0x200
+2.4.0.0.0
+  __TEXT.__text: 0x71394
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_methlist: 0x50a4
+  __TEXT.__const: 0x620
+  __TEXT.__cstring: 0x606e
+  __TEXT.__oslogstring: 0x3369
+  __TEXT.__gcc_except_tab: 0x2dc
+  __TEXT.__unwind_info: 0x1290
+  __TEXT.__objc_classname: 0x6cc
+  __TEXT.__objc_methname: 0x13ca1
+  __TEXT.__objc_methtype: 0x77d3
+  __TEXT.__objc_stubs: 0x7760
+  __DATA_CONST.__got: 0x388
+  __DATA_CONST.__const: 0x310
+  __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf8
-  __DATA_CONST.__objc_superrefs: 0x1e8
+  __DATA_CONST.__objc_selrefs: 0x29d8
+  __DATA_CONST.__objc_superrefs: 0x258
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x560
-  __AUTH_CONST.__const: 0xf8
-  __AUTH_CONST.__cfstring: 0x2460
-  __AUTH_CONST.__objc_const: 0xc860
-  __AUTH_CONST.__objc_intobj: 0x108
+  __AUTH_CONST.__auth_got: 0x7b8
+  __AUTH_CONST.__const: 0xf0
+  __AUTH_CONST.__cfstring: 0x3100
+  __AUTH_CONST.__objc_const: 0x11258
+  __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x1400
-  __DATA.__objc_ivar: 0xe8c
+  __AUTH.__objc_data: 0x1900
+  __DATA.__objc_ivar: 0x1514
   __DATA.__data: 0x260
   __DATA.__bss: 0x8
   __DATA.__common: 0x10

   - /System/Library/Frameworks/CoreVideo.framework/CoreVideo
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOSurface.framework/IOSurface
+  - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/Metal.framework/Metal
   - /System/Library/Frameworks/MetalPerformanceShaders.framework/MetalPerformanceShaders
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
+  - /System/Library/PrivateFrameworks/CMImaging.framework/CMImaging
   - /System/Library/PrivateFrameworks/Espresso.framework/Espresso
   - /System/Library/PrivateFrameworks/FRC.framework/FRC
   - /System/Library/PrivateFrameworks/IOSurfaceAccelerator.framework/IOSurfaceAccelerator
+  - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A85AF25-486C-3F68-826A-FCC98AAA37D0
-  Functions: 1536
-  Symbols:   5627
-  CStrings:  3065
+  UUID: A2FB0AB3-50B4-34F0-A4AB-C8F3B3226078
+  Functions: 2477
+  Symbols:   8432
+  CStrings:  4665
 
Symbols:
+ +[DVPLensFlareMitigationConfiguration defaultRevision]
+ +[DVPLensFlareMitigationConfiguration downloadAssetWithCompletionHandler:]
+ +[DVPLensFlareMitigationConfiguration getAssetStatusWithPercentCompleted:]
+ +[DVPLensFlareMitigationConfiguration isSupportedRevision:]
+ +[DVPLensFlareMitigationConfiguration supportedRevisions]
+ +[DVPLensFlareMitigationParameters getMotionShiftFromOpticalCenters:opticalCenterArrayLen:opticalCenterMotionShifts:]
+ +[FRNet downloadMobileAssetWithCompletionHandler:]
+ +[FRNet getMobileAssetStatusWithPercentCompleted:]
+ +[GGMController downloadMobileAssetWithCompletionHandler:]
+ +[GGMController getMobileAssetStatusWithPercentCompleted:]
+ +[ImageSR downloadMobileAssetWithCompletionHandler:]
+ +[ImageSR getMobileAssetStatusWithPercentCompleted:]
+ +[VEMobileAsset downloadMobileAssetType:assetSpecifier:forClientName:completionHandler:]
+ +[VEMobileAsset downloadMobileAssetType:assetSpecifier:forClientName:completionHandler:].cold.1
+ +[VEMobileAsset endAllLocksWithAssetType:assetSpecifier:forClientName:]
+ +[VEMobileAsset endAllLocksWithAssetType:assetSpecifier:forClientName:].cold.1
+ +[VEMobileAsset endAllLocksWithAssetType:assetSpecifier:forClientName:].cold.2
+ +[VEMobileAsset endAllLocksWithAssetType:assetSpecifier:forClientName:].cold.3
+ +[VEMobileAsset getLocalMobileAssetURLWithAssetType:assetSpecifier:forClientName:]
+ +[VEMobileAsset getLocalMobileAssetURLWithAssetType:assetSpecifier:forClientName:].cold.1
+ +[VEMobileAsset getMobileAssetStatusWithAssetType:assetSpecifier:forClientName:percentCompleted:]
+ +[VEMobileAsset getMobileAssetStatusWithAssetType:assetSpecifier:forClientName:percentCompleted:].cold.1
+ +[VEMobileAsset getMobileAssetStatusWithAssetType:assetSpecifier:forClientName:percentCompleted:].cold.2
+ +[VSRProcessor downloadMobileAssetWithInputType:withCompletionHandler:]
+ +[VSRProcessor getMobileAssetStatusForInputType:percentCompleted:]
+ -[DVPLensFlareMitigationConfiguration .cxx_destruct]
+ -[DVPLensFlareMitigationConfiguration frameHeight]
+ -[DVPLensFlareMitigationConfiguration framePreferredPixelFormats]
+ -[DVPLensFlareMitigationConfiguration frameSupportedPixelFormats]
+ -[DVPLensFlareMitigationConfiguration frameWidth]
+ -[DVPLensFlareMitigationConfiguration initWithFrameWidth:frameHeight:usePrecomputedFlow:qualityPrioritization:revision:]
+ -[DVPLensFlareMitigationConfiguration qualityPrioritization]
+ -[DVPLensFlareMitigationConfiguration revision]
+ -[DVPLensFlareMitigationConfiguration usePrecomputedFlow]
+ -[DVPLensFlareMitigationParameters .cxx_destruct]
+ -[DVPLensFlareMitigationParameters destinationFrame]
+ -[DVPLensFlareMitigationParameters initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:]
+ -[DVPLensFlareMitigationParameters nextFrameOpticalCenter]
+ -[DVPLensFlareMitigationParameters nextFrame]
+ -[DVPLensFlareMitigationParameters opticalCenterShift]
+ -[DVPLensFlareMitigationParameters opticalFlow]
+ -[DVPLensFlareMitigationParameters previousOutputFrame]
+ -[DVPLensFlareMitigationParameters previousPreviousOutputFrame]
+ -[DVPLensFlareMitigationParameters sourceFrameOpticalCenter]
+ -[DVPLensFlareMitigationParameters sourceFrame]
+ -[DVPLensFlareMitigationParameters submissionMode]
+ -[DVPSuperResolutionParameters initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:]
+ -[DVPSuperResolutionParameters submissionMode]
+ -[DetectedROI LSRoi]
+ -[DetectedROI confidence]
+ -[DetectedROI des]
+ -[DetectedROI initWithTrackingSessionId:roiId:andRoi:]
+ -[DetectedROI initWithTrackingSessionId:roiId:roi:LSRoi:confidence:]
+ -[DetectedROI initWithTrackingSessionId:roiId:roi:LSRoi:descriptor:propertiesForPostProcPipeVisualization:]
+ -[DetectedROI initWithTrackingSessionId:roiId:roi:trackId:]
+ -[DetectedROI isPredictedFromPast]
+ -[DetectedROI isReflectedLS]
+ -[DetectedROI isTracked]
+ -[DetectedROI isTrajectoryPruningPassed]
+ -[DetectedROI lowSaliencyCnt]
+ -[DetectedROI predictedFromPastCnt]
+ -[DetectedROI roiId]
+ -[DetectedROI roiMv]
+ -[DetectedROI roi]
+ -[DetectedROI setConfidence:]
+ -[DetectedROI setIsPredictedFromPast:]
+ -[DetectedROI setIsReflectedLS:]
+ -[DetectedROI setIsTracked:]
+ -[DetectedROI setIsTrajectoryPruningPassed:]
+ -[DetectedROI setLowSaliencyCnt:]
+ -[DetectedROI setPredictedFromPastCnt:]
+ -[DetectedROI setRoi:]
+ -[DetectedROI setRoiMv:]
+ -[DetectedROI setTrackID:]
+ -[DetectedROI setTrackedCnt:]
+ -[DetectedROI setTrajectoryFromPast:]
+ -[DetectedROI trackID]
+ -[DetectedROI trackSessionId]
+ -[DetectedROI trackedCnt]
+ -[DetectedROI trajectoryFromPast]
+ -[GGMController .cxx_destruct]
+ -[GGMController dealloc]
+ -[GGMController detectedGreenGhostInfo]
+ -[GGMController endSession]
+ -[GGMController futureFramesToDetectionAndRepair]
+ -[GGMController futureInputParamsToRepair]
+ -[GGMController initWithFrameWidth:FrameHeight:usePrecomputedFlow:]
+ -[GGMController inputBuffer]
+ -[GGMController inputParamsToRepair]
+ -[GGMController ispTimeStamp]
+ -[GGMController keyPointsList]
+ -[GGMController lightSourceMask]
+ -[GGMController metaDictionary]
+ -[GGMController msrFrameSource:destination:waitForCompletion:]
+ -[GGMController nextVisedOpticalCenter]
+ -[GGMController opticalCenterMvShift]
+ -[GGMController processSourceFrame:nextFrame:forwardFlow:backwardFlow:ourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:randomAccessMode:destinationFrame:]
+ -[GGMController processedPixelBuffer]
+ -[GGMController resetIntermediateVariables]
+ -[GGMController resetState]
+ -[GGMController setDefaultControllerConfig]
+ -[GGMController setDetectedGreenGhostInfo:]
+ -[GGMController setFutureFramesToDetectionAndRepair:]
+ -[GGMController setFutureInputParamsToRepair:]
+ -[GGMController setInputBuffer:]
+ -[GGMController setInputParamsToRepair:]
+ -[GGMController setIspTimeStamp:]
+ -[GGMController setKeyPointsList:]
+ -[GGMController setLightSourceMask:]
+ -[GGMController setMetaDictionary:]
+ -[GGMController setNextVisedOpticalCenter:]
+ -[GGMController setOpticalCenterMvShift:]
+ -[GGMController setVisedOpticalCenter:]
+ -[GGMController startSessionWithQualityMode:error:]
+ -[GGMController tuningParamDict]
+ -[GGMController visedOpticalCenter]
+ -[GGMMetalToolBox .cxx_destruct]
+ -[GGMMetalToolBox _compileShaders]
+ -[GGMMetalToolBox clusterIndicesOfRois:withExtendedRadius:roiCnt:imageRect:]
+ -[GGMMetalToolBox commitCmdBuffer:waitForComplete:]
+ -[GGMMetalToolBox createForwarpOutputBufferWidth:height:channels:]
+ -[GGMMetalToolBox cvMetalTextureCacheRef]
+ -[GGMMetalToolBox dealloc]
+ -[GGMMetalToolBox encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:]
+ -[GGMMetalToolBox encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.1
+ -[GGMMetalToolBox encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.2
+ -[GGMMetalToolBox encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.3
+ -[GGMMetalToolBox encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.4
+ -[GGMMetalToolBox encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.5
+ -[GGMMetalToolBox encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:]
+ -[GGMMetalToolBox encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.5
+ -[GGMMetalToolBox encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:].cold.6
+ -[GGMMetalToolBox encodeBMSearch1RefToCommandEncoder:target:ref:reflect:normalizedTargetCenter:normalizedRefCenter:bestMatchLoc:meta:]
+ -[GGMMetalToolBox encodeBMSearch1RefToCommandEncoder:target:ref:reflect:normalizedTargetCenter:normalizedRefCenter:bestMatchLoc:meta:].cold.1
+ -[GGMMetalToolBox encodeBMSearch1RefToCommandEncoder:target:ref:reflect:normalizedTargetCenter:normalizedRefCenter:bestMatchLoc:meta:].cold.2
+ -[GGMMetalToolBox encodeBMSearch1RefToCommandEncoder:target:ref:reflect:normalizedTargetCenter:normalizedRefCenter:bestMatchLoc:meta:].cold.3
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:]
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.1
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.10
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.2
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.3
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.4
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.5
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.6
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.7
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.8
+ -[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:].cold.9
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:]
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.1
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.10
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.11
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.12
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.2
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.3
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.4
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.5
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.6
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.7
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.8
+ -[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:].cold.9
+ -[GGMMetalToolBox encodeBMTransferGrayToCommandEncoder:ref:warpedRef:bestMatchLoc:meta:sf:]
+ -[GGMMetalToolBox encodeBMTransferGrayToCommandEncoder:ref:warpedRef:bestMatchLoc:meta:sf:].cold.1
+ -[GGMMetalToolBox encodeBMTransferGrayToCommandEncoder:ref:warpedRef:bestMatchLoc:meta:sf:].cold.2
+ -[GGMMetalToolBox encodeBMTransferGrayToCommandEncoder:ref:warpedRef:bestMatchLoc:meta:sf:].cold.3
+ -[GGMMetalToolBox encodeBMTransferGrayToCommandEncoder:ref:warpedRef:bestMatchLoc:meta:sf:].cold.4
+ -[GGMMetalToolBox encodeBMTransferYUVToCommandEncoder:ref:reflect:normalizedCenter:warpedRef:bestMatchLoc:meta:sf:]
+ -[GGMMetalToolBox encodeBMTransferYUVToCommandEncoder:ref:reflect:normalizedCenter:warpedRef:bestMatchLoc:meta:sf:].cold.1
+ -[GGMMetalToolBox encodeBMTransferYUVToCommandEncoder:ref:reflect:normalizedCenter:warpedRef:bestMatchLoc:meta:sf:].cold.2
+ -[GGMMetalToolBox encodeBMTransferYUVToCommandEncoder:ref:reflect:normalizedCenter:warpedRef:bestMatchLoc:meta:sf:].cold.3
+ -[GGMMetalToolBox encodeBMTransferYUVToCommandEncoder:ref:reflect:normalizedCenter:warpedRef:bestMatchLoc:meta:sf:].cold.4
+ -[GGMMetalToolBox encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:]
+ -[GGMMetalToolBox encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:].cold.1
+ -[GGMMetalToolBox encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:].cold.2
+ -[GGMMetalToolBox encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:].cold.3
+ -[GGMMetalToolBox encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:].cold.4
+ -[GGMMetalToolBox encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:].cold.5
+ -[GGMMetalToolBox encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:].cold.6
+ -[GGMMetalToolBox encodeBilinearRescaleYUV:fullResInput:input:meta:blurBeforeSample:output:]
+ -[GGMMetalToolBox encodeBilinearRescaleYUV:fullResInput:input:meta:blurBeforeSample:output:].cold.1
+ -[GGMMetalToolBox encodeBilinearRescaleYUV:fullResInput:input:meta:blurBeforeSample:output:].cold.2
+ -[GGMMetalToolBox encodeBilinearRescaleYUV:fullResInput:input:meta:blurBeforeSample:output:].cold.3
+ -[GGMMetalToolBox encodeBilinearRescaleYUV:fullResInput:input:meta:blurBeforeSample:output:].cold.4
+ -[GGMMetalToolBox encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:]
+ -[GGMMetalToolBox encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:].cold.5
+ -[GGMMetalToolBox encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:].cold.6
+ -[GGMMetalToolBox encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:].cold.7
+ -[GGMMetalToolBox encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:]
+ -[GGMMetalToolBox encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:].cold.5
+ -[GGMMetalToolBox encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:].cold.6
+ -[GGMMetalToolBox encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:].cold.7
+ -[GGMMetalToolBox encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:]
+ -[GGMMetalToolBox encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:].cold.1
+ -[GGMMetalToolBox encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:].cold.2
+ -[GGMMetalToolBox encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:].cold.3
+ -[GGMMetalToolBox encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:].cold.4
+ -[GGMMetalToolBox encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:].cold.5
+ -[GGMMetalToolBox encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:].cold.6
+ -[GGMMetalToolBox encodeCollectClusterBgAvgToCommandEncoder:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeCollectClusterBgAvgToCommandEncoder:clusterMetaBuf:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectClusterBgAvgToCommandEncoder:clusterMetaBuf:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectClusterMaxAndAvgLuma:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeCollectClusterMaxAndAvgLuma:clusterMetaBuf:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectClusterMaxAndAvgLuma:clusterMetaBuf:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectClusterMaxProb:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeCollectClusterMaxProb:clusterMetaBuf:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectClusterMaxProb:clusterMetaBuf:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectClusterMv:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeCollectClusterMv:clusterMetaBuf:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectClusterMv:clusterMetaBuf:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectClusterMvForMotionCueToCommandEncoder:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeCollectClusterMvForMotionCueToCommandEncoder:clusterMetaBuf:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectClusterMvForMotionCueToCommandEncoder:clusterMetaBuf:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectClusterOverlapWithRefs:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeCollectClusterOverlapWithRefs:clusterMetaBuf:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectClusterOverlapWithRefs:clusterMetaBuf:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:]
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:].cold.1
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:].cold.2
+ -[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:].cold.3
+ -[GGMMetalToolBox encodeCollectMvToFuture:metaBuf:]
+ -[GGMMetalToolBox encodeCollectMvToFuture:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:]
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.1
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.10
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.11
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.12
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.13
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.14
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.15
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.2
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.3
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.4
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.5
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.6
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.7
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.8
+ -[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:].cold.9
+ -[GGMMetalToolBox encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:]
+ -[GGMMetalToolBox encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:].cold.1
+ -[GGMMetalToolBox encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:].cold.2
+ -[GGMMetalToolBox encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:].cold.3
+ -[GGMMetalToolBox encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:].cold.4
+ -[GGMMetalToolBox encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:]
+ -[GGMMetalToolBox encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:].cold.1
+ -[GGMMetalToolBox encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:].cold.2
+ -[GGMMetalToolBox encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:].cold.3
+ -[GGMMetalToolBox encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:].cold.4
+ -[GGMMetalToolBox encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:].cold.5
+ -[GGMMetalToolBox encodeCopyCurrMetaForProcFuture:metaBuf:outMetaBuf:]
+ -[GGMMetalToolBox encodeCopyCurrMetaForProcFuture:metaBuf:outMetaBuf:].cold.1
+ -[GGMMetalToolBox encodeCopyCurrMetaForProcFuture:metaBuf:outMetaBuf:].cold.2
+ -[GGMMetalToolBox encodeCopyFullFrameMapToMap4RoiGenToCommandEncoder:input:output:]
+ -[GGMMetalToolBox encodeCopyFullFrameMapToMap4RoiGenToCommandEncoder:input:output:].cold.1
+ -[GGMMetalToolBox encodeCopyFullFrameMapToMap4RoiGenToCommandEncoder:input:output:].cold.2
+ -[GGMMetalToolBox encodeCopyMapToMap4RoiGenToCommandEncoder:input:output:metaBuf:]
+ -[GGMMetalToolBox encodeCopyMapToMap4RoiGenToCommandEncoder:input:output:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeCopyMapToMap4RoiGenToCommandEncoder:input:output:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeCopyMapToMap4RoiGenToCommandEncoder:input:output:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:]
+ -[GGMMetalToolBox encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:].cold.1
+ -[GGMMetalToolBox encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:].cold.2
+ -[GGMMetalToolBox encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:].cold.3
+ -[GGMMetalToolBox encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:].cold.4
+ -[GGMMetalToolBox encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:].cold.5
+ -[GGMMetalToolBox encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:].cold.6
+ -[GGMMetalToolBox encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:]
+ -[GGMMetalToolBox encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:].cold.1
+ -[GGMMetalToolBox encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:].cold.2
+ -[GGMMetalToolBox encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:].cold.3
+ -[GGMMetalToolBox encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:].cold.4
+ -[GGMMetalToolBox encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:].cold.5
+ -[GGMMetalToolBox encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:].cold.6
+ -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:]
+ -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:].cold.1
+ -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:].cold.2
+ -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:].cold.3
+ -[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:].cold.4
+ -[GGMMetalToolBox encodeDilateProbMap:input:output:hardDilationRadius:softDilationRadius:meta:]
+ -[GGMMetalToolBox encodeDilateProbMap:input:output:hardDilationRadius:softDilationRadius:meta:].cold.1
+ -[GGMMetalToolBox encodeDilateProbMap:input:output:hardDilationRadius:softDilationRadius:meta:].cold.2
+ -[GGMMetalToolBox encodeDilateProbMap:input:output:hardDilationRadius:softDilationRadius:meta:].cold.3
+ -[GGMMetalToolBox encodeDilateReflLsMap:inputYUV:lsMap:dilatedLsMap:hardDilationRadius:softDilationRadius:meta:]
+ -[GGMMetalToolBox encodeDilateReflLsMap:inputYUV:lsMap:dilatedLsMap:hardDilationRadius:softDilationRadius:meta:].cold.1
+ -[GGMMetalToolBox encodeDilateReflLsMap:inputYUV:lsMap:dilatedLsMap:hardDilationRadius:softDilationRadius:meta:].cold.2
+ -[GGMMetalToolBox encodeDilateReflLsMap:inputYUV:lsMap:dilatedLsMap:hardDilationRadius:softDilationRadius:meta:].cold.3
+ -[GGMMetalToolBox encodeDilateReflLsMap:inputYUV:lsMap:dilatedLsMap:hardDilationRadius:softDilationRadius:meta:].cold.4
+ -[GGMMetalToolBox encodeForwarpYUVToCommandEncoder:input0:input1:meta:mvf0:mvf1:intermediateOutput0:intermediateOutput1:output0:output1:outputMap0:outputMap1:]
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:]
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.5
+ -[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:].cold.6
+ -[GGMMetalToolBox encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:]
+ -[GGMMetalToolBox encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.4
+ -[GGMMetalToolBox encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:].cold.5
+ -[GGMMetalToolBox encodeGetBlobSaliency:inputYUV:blobSaliencyMap:meta:]
+ -[GGMMetalToolBox encodeGetBlobSaliency:inputYUV:blobSaliencyMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetBlobSaliency:inputYUV:blobSaliencyMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetBlobSaliency:inputYUV:blobSaliencyMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:]
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.4
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.5
+ -[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:].cold.6
+ -[GGMMetalToolBox encodeGetLsMapYUVToCommandEncoder:input:map:]
+ -[GGMMetalToolBox encodeGetLsMapYUVToCommandEncoder:input:map:].cold.1
+ -[GGMMetalToolBox encodeGetLsMapYUVToCommandEncoder:input:map:].cold.2
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:]
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:].cold.4
+ -[GGMMetalToolBox encodeGetMvForMotionCueFromMvf:fullResInput:meta:mvf:opticalCenter:refOpticalCenter:]
+ -[GGMMetalToolBox encodeGetMvForMotionCueFromMvf:fullResInput:meta:mvf:opticalCenter:refOpticalCenter:].cold.1
+ -[GGMMetalToolBox encodeGetMvForMotionCueFromMvf:fullResInput:meta:mvf:opticalCenter:refOpticalCenter:].cold.2
+ -[GGMMetalToolBox encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:]
+ -[GGMMetalToolBox encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:].cold.1
+ -[GGMMetalToolBox encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:].cold.2
+ -[GGMMetalToolBox encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:].cold.3
+ -[GGMMetalToolBox encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:].cold.4
+ -[GGMMetalToolBox encodeGetMvToFutureFromMvf:fullResInput:meta:mvf:]
+ -[GGMMetalToolBox encodeGetMvToFutureFromMvf:fullResInput:meta:mvf:].cold.1
+ -[GGMMetalToolBox encodeGetMvToFutureFromMvf:fullResInput:meta:mvf:].cold.2
+ -[GGMMetalToolBox encodeGetMvToFutureFromMvf:fullResInput:meta:mvf:].cold.3
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:]
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeGetRoiMaxAndAvgLumaYUV:target:lsMap:meta:]
+ -[GGMMetalToolBox encodeGetRoiMaxAndAvgLumaYUV:target:lsMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetRoiMaxAndAvgLumaYUV:target:lsMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetRoiMaxAndAvgLumaYUV:target:lsMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:]
+ -[GGMMetalToolBox encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:].cold.1
+ -[GGMMetalToolBox encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:].cold.2
+ -[GGMMetalToolBox encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:].cold.3
+ -[GGMMetalToolBox encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:].cold.4
+ -[GGMMetalToolBox encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:].cold.5
+ -[GGMMetalToolBox encodeGetSaliencyMapToCommandEncoder:target:saliencyMap:meta:]
+ -[GGMMetalToolBox encodeGetSaliencyMapToCommandEncoder:target:saliencyMap:meta:].cold.1
+ -[GGMMetalToolBox encodeGetSaliencyMapToCommandEncoder:target:saliencyMap:meta:].cold.2
+ -[GGMMetalToolBox encodeGetSaliencyMapToCommandEncoder:target:saliencyMap:meta:].cold.3
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:]
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.1
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.10
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.11
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.2
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.3
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.4
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.5
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.6
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.7
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.8
+ -[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:].cold.9
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:]
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.1
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.2
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.3
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.4
+ -[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:].cold.5
+ -[GGMMetalToolBox encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:]
+ -[GGMMetalToolBox encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:].cold.5
+ -[GGMMetalToolBox encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:]
+ -[GGMMetalToolBox encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:].cold.1
+ -[GGMMetalToolBox encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:].cold.2
+ -[GGMMetalToolBox encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:].cold.3
+ -[GGMMetalToolBox encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:].cold.4
+ -[GGMMetalToolBox encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:].cold.5
+ -[GGMMetalToolBox encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:].cold.6
+ -[GGMMetalToolBox encodeResetOutputToCommandEncoder:input:meta:output0:output1:]
+ -[GGMMetalToolBox encodeResetOutputToCommandEncoder:input:meta:output0:output1:].cold.1
+ -[GGMMetalToolBox encodeResetOutputToCommandEncoder:input:meta:output0:output1:].cold.2
+ -[GGMMetalToolBox encodeResetOutputToCommandEncoder:input:meta:output0:output1:].cold.3
+ -[GGMMetalToolBox encodeResetOutputToCommandEncoder:input:meta:output0:output1:].cold.4
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:]
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:]
+ -[GGMMetalToolBox encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:].cold.3
+ -[GGMMetalToolBox encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:].cold.4
+ -[GGMMetalToolBox encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:].cold.5
+ -[GGMMetalToolBox encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:].cold.6
+ -[GGMMetalToolBox encodeSyncWeightsOriginal:clusterMetaBuf:metaBuf:]
+ -[GGMMetalToolBox encodeSyncWeightsOriginal:clusterMetaBuf:metaBuf:].cold.1
+ -[GGMMetalToolBox encodeSyncWeightsOriginal:clusterMetaBuf:metaBuf:].cold.2
+ -[GGMMetalToolBox encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:]
+ -[GGMMetalToolBox encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:].cold.1
+ -[GGMMetalToolBox encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:].cold.2
+ -[GGMMetalToolBox encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:].cold.3
+ -[GGMMetalToolBox encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:].cold.4
+ -[GGMMetalToolBox encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:].cold.5
+ -[GGMMetalToolBox encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:].cold.6
+ -[GGMMetalToolBox encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:].cold.7
+ -[GGMMetalToolBox encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:]
+ -[GGMMetalToolBox encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:].cold.1
+ -[GGMMetalToolBox encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:].cold.2
+ -[GGMMetalToolBox encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:].cold.3
+ -[GGMMetalToolBox encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:].cold.4
+ -[GGMMetalToolBox encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:].cold.5
+ -[GGMMetalToolBox encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:].cold.6
+ -[GGMMetalToolBox encodeUpscaleThenReflectLsMap:input:normalizedCenter:output:]
+ -[GGMMetalToolBox encodeUpscaleThenReflectLsMap:input:normalizedCenter:output:].cold.1
+ -[GGMMetalToolBox encodeUpscaleThenReflectLsMap:input:normalizedCenter:output:].cold.2
+ -[GGMMetalToolBox encodeVisualizeMvfToCommandEncoder:fullResTarget:mvf:outMvf:meta:]
+ -[GGMMetalToolBox encodeVisualizeMvfToCommandEncoder:fullResTarget:mvf:outMvf:meta:].cold.1
+ -[GGMMetalToolBox encodeVisualizeMvfToCommandEncoder:fullResTarget:mvf:outMvf:meta:].cold.2
+ -[GGMMetalToolBox encodeVisualizeMvfToCommandEncoder:fullResTarget:mvf:outMvf:meta:].cold.3
+ -[GGMMetalToolBox encodeVisualizeMvfToCommandEncoder:fullResTarget:mvf:outMvf:meta:].cold.4
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:]
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:].cold.1
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:].cold.2
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:].cold.3
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:].cold.4
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:].cold.5
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:].cold.6
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:]
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.1
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.2
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.3
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.4
+ -[GGMMetalToolBox encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:].cold.5
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:]
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.1
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.2
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.3
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.4
+ -[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:].cold.5
+ -[GGMMetalToolBox encodeWarpRefMetaLite:refMetaBuf:outMetaBuf:]
+ -[GGMMetalToolBox encodeWarpRefMetaLite:refMetaBuf:outMetaBuf:].cold.1
+ -[GGMMetalToolBox encodeWarpRefMetaLite:refMetaBuf:outMetaBuf:].cold.2
+ -[GGMMetalToolBox generateMetaContainerArrayBufFromMetaContainerBuf:imageRect:]
+ -[GGMMetalToolBox getCommandqueue]
+ -[GGMMetalToolBox getDevice]
+ -[GGMMetalToolBox initWithMetalContext:commandQueue:]
+ -[GGMMetalToolBox initWithMetalContext:commandQueue:tuningParamDict:]
+ -[GGMMetalToolBox initWithMetalContext:commandQueue:tuningParamDict:].cold.1
+ -[GGMMetalToolBox metaContainer]
+ -[GGMMetalToolBox rescaleMetaContainerBuffer:sf:sfInv:]
+ -[GGMMetalToolBox resizeImageCmdBuf:inputTexture:withFactorX:withFactorY:outputTexture:]
+ -[GGMMetalToolBox resizeImageCmdBuf:inputTexture:withFactorX:withFactorY:outputTexture:].cold.1
+ -[GGMMetalToolBox resizeImageCmdBuf:inputTexture:withFactorX:withFactorY:outputTexture:].cold.2
+ -[GGMMetalToolBox resizeImageCmdBuf:inputTexture:withFactorX:withFactorY:outputTexture:].cold.3
+ -[GGMMetalToolBox setMetaContainer:]
+ -[GGMMetalToolBox setRepairTuningParams:]
+ -[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:opticalCenterShift:]
+ -[GGMMetalToolBox updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:opticalCenterShift:].cold.1
+ -[ISRNet .cxx_destruct]
+ -[ISRNet allocateInputBufferObjects]
+ -[ISRNet allocateInputBufferObjects].cold.1
+ -[ISRNet allocateInputBufferObjects].cold.2
+ -[ISRNet allocateInputBufferObjects].cold.3
+ -[ISRNet dealloc]
+ -[ISRNet getInputPortNames]
+ -[ISRNet getInputPortNames].cold.1
+ -[ISRNet getInputPortNames].cold.2
+ -[ISRNet initWithModelPath:inputWidth:inputHeight:]
+ -[ISRNet initializeInputPorts]
+ -[ISRNet initializeInputPorts].cold.1
+ -[ISRNet inputSurface]
+ -[ISRNet processSuperResolutionInputBuffer:outputBuffer:]
+ -[ISRNet processSuperResolutionInputBuffer:outputBuffer:].cold.1
+ -[ISRNet processSuperResolutionInputBuffer:outputBuffer:].cold.2
+ -[ISRNet setInputSurface:]
+ -[MaskToRoi .cxx_destruct]
+ -[MaskToRoi _findBoundingBoxesWithSizeThreshold:LsThreshold:scalingFactor:validWidth:validHeight:]
+ -[MaskToRoi convertInternalBBoxes:outputArray:]
+ -[MaskToRoi convertInternalBBoxesToROI:outputArray:]
+ -[MaskToRoi convertPackedMaskToRegular:output:]
+ -[MaskToRoi dealloc]
+ -[MaskToRoi extractRoiByGraphTraversalInput:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:]
+ -[MaskToRoi getBBoxesUsingGraphTraversalFrom:pixValThreshold:bboxSizeThreshold:scaleFactor:roi:returnAsDetectedROI:outputArray:]
+ -[MaskToRoi getBBoxesUsingGraphTraversalFrom:pixValThreshold:bboxSizeThreshold:scaleFactor:roi:returnAsDetectedROI:outputArray:].cold.1
+ -[MaskToRoi getLSBBoxesUsingGraphTraversalFrom:roi:pixValThreshold:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:]
+ -[MaskToRoi initWithMetalToolBox:]
+ -[MaskToRoi integralSumPixelBuffer]
+ -[MaskToRoi setIntegralSumPixelBuffer:]
+ -[MitigationANE .cxx_destruct]
+ -[MitigationANE _cachedTexturesFromPixelBuffer:usage:]
+ -[MitigationANE _cachedTexturesFromPixelBuffer:usage:].cold.1
+ -[MitigationANE _cachedTexturesFromPixelBuffer:usage:].cold.2
+ -[MitigationANE _cachedTexturesFromPixelBuffer:usage:].cold.3
+ -[MitigationANE _cachedTexturesFromPixelBuffer:usage:].cold.4
+ -[MitigationANE _cachedTexturesFromPixelBuffer:usage:].cold.5
+ -[MitigationANE _cachedTexturesFromPixelBuffer:usage:].cold.6
+ -[MitigationANE _cachedTexturesFromPixelBuffer:usage:].cold.7
+ -[MitigationANE _cachedTexturesFromPixelBuffer:usage:].cold.8
+ -[MitigationANE _clampGhostROI:]
+ -[MitigationANE _compileShaders]
+ -[MitigationANE _copyImageTileFromPixelBuffer:mergeWithMask:outputTilePixelBuffer:commandBuffer:]
+ -[MitigationANE _copyImageTileFromPixelBuffer:outputImageTileTexture:commandBuffer:]
+ -[MitigationANE _pasteRepairedTile:inputTileTexture:blendingMask:outputPixelBuffer:commandBuffer:]
+ -[MitigationANE _repair:outputBuf:ghostROI:inputROI:repairMask:blendMask:]
+ -[MitigationANE dealloc]
+ -[MitigationANE finishProcessing]
+ -[MitigationANE initWithMetalContext:commandQueue:imageDimensions:]
+ -[MitigationANE initWithMetalContext:commandQueue:imageDimensions:netSize:metalToolBox:]
+ -[MitigationANE prepareToProcess:]
+ -[MitigationANE prewarm]
+ -[MitigationANE process:outputBuf:roi:repairMask:blendMask:wRepairedY:wRepairedUV:]
+ -[MitigationANE process]
+ -[MitigationANE purgeResources]
+ -[MitigationANE resetState]
+ -[MitigationANE setup]
+ -[MitigationANE setup].cold.1
+ -[OFNormalization convertBuffer:toFP16IOSurface:]
+ -[OFNormalization convertBuffer:toFP16ShuffledIOSurface:]
+ -[OFNormalization convertFP16IOSurface:toBuffer:]
+ -[OFNormalization createFP16TextureFromIOSurface:width:height:arrayLength:]
+ -[OFNormalization encodePadRGBToCommandBuffer:source:destination:]
+ -[OFNormalization padRGB:to:]
+ -[PixelMemory SampleFourChannelAtX:Y:]
+ -[PixelMemory buf]
+ -[PixelMemory bytePerPixel]
+ -[PixelMemory channels]
+ -[PixelMemory dealloc]
+ -[PixelMemory format]
+ -[PixelMemory height]
+ -[PixelMemory initImageWithValue:]
+ -[PixelMemory initWithCvPixelBuffer:]
+ -[PixelMemory initWithCvPixelBuffer:skipClamp:readOnly:]
+ -[PixelMemory initWithCvPixelBuffer:skipClamp:readOnly:].cold.1
+ -[PixelMemory initWithCvPixelBuffer:skipClamp:readOnly:].cold.2
+ -[PixelMemory pMemoryPlane2]
+ -[PixelMemory pMemory]
+ -[PixelMemory readBlurredYValueAtX:Y:]
+ -[PixelMemory readFloatAtX:Y:]
+ -[PixelMemory readFourChannelAtX:Y:]
+ -[PixelMemory readOneChannelAtX:Y:Channel:]
+ -[PixelMemory readYCbCrValueAtArrayX:ArrayY:]
+ -[PixelMemory readYCbCrValueAtX:Y:]
+ -[PixelMemory readYValueAtX:Y:]
+ -[PixelMemory sampleOneChannelAtX:Y:Channel:]
+ -[PixelMemory setBuf:]
+ -[PixelMemory setBytePerPixel:]
+ -[PixelMemory setChannels:]
+ -[PixelMemory setFormat:]
+ -[PixelMemory setHeight:]
+ -[PixelMemory setPMemory:]
+ -[PixelMemory setPMemoryPlane2:]
+ -[PixelMemory setSkipClamp:]
+ -[PixelMemory setStride:]
+ -[PixelMemory setStridePlane2:]
+ -[PixelMemory setWidth:]
+ -[PixelMemory skipClamp]
+ -[PixelMemory stridePlane2]
+ -[PixelMemory stride]
+ -[PixelMemory width]
+ -[PixelMemory writeFloat:X:Y:]
+ -[PixelMemory writeValue:X:Y:Channel:]
+ -[PixelMemory writeValue:X:Y:]
+ -[ROI .cxx_destruct]
+ -[ROI LSIsHighRisk]
+ -[ROI LSOrGGBbox]
+ -[ROI LSTrackID]
+ -[ROI LSTrackingMatched]
+ -[ROI LSTrackingVote]
+ -[ROI area]
+ -[ROI bbox]
+ -[ROI compareSelfAsLSWithAnotherLS:]
+ -[ROI defaultOpticalCenter]
+ -[ROI descriptor]
+ -[ROI differenceOfGaussianAndLumaFeaturePredictedLocation]
+ -[ROI differenceOfGaussianAndLumaFeatureReflection]
+ -[ROI differenceOfGaussianAndLumaFeature]
+ -[ROI dist2ghost]
+ -[ROI dist2opticalCenter]
+ -[ROI doneKPToBBoxViaGraphTraversal]
+ -[ROI generateLocationFromBBox]
+ -[ROI getLocationMatchCostWith:]
+ -[ROI getPixelFeatureMatchCostWith:]
+ -[ROI getPixelFeatureMatchCostWith:].cold.1
+ -[ROI getPixelFeatureMatchCostWith:].cold.2
+ -[ROI getReflectedBboxAroundCenter:]
+ -[ROI getReflectedBboxCenterAroundCenter:]
+ -[ROI initWithBbox:]
+ -[ROI initWithBbox:descriptor:]
+ -[ROI isPredictedFromPast]
+ -[ROI isReflectedLS]
+ -[ROI isTracked]
+ -[ROI isTrajectoryPruningPassed]
+ -[ROI kpIsFromHW]
+ -[ROI lowSaliencyCnt]
+ -[ROI lsHasBeenUsedForTrackingGhost]
+ -[ROI lumaFeatureVectorPredictedLocation]
+ -[ROI lumaFeatureVectorReflection]
+ -[ROI lumaFeatureVector]
+ -[ROI matchedLS]
+ -[ROI mvCnt]
+ -[ROI mvSum]
+ -[ROI mv]
+ -[ROI predictedFromPastCnt]
+ -[ROI reflectAroundCenter:]
+ -[ROI setArea:]
+ -[ROI setBbox:]
+ -[ROI setDefaultOpticalCenter:]
+ -[ROI setDescriptor:]
+ -[ROI setDifferenceOfGaussianAndLumaFeature:]
+ -[ROI setDifferenceOfGaussianAndLumaFeaturePredictedLocation:]
+ -[ROI setDifferenceOfGaussianAndLumaFeatureReflection:]
+ -[ROI setDist2ghost:]
+ -[ROI setDist2opticalCenter:]
+ -[ROI setDoneKPToBBoxViaGraphTraversal:]
+ -[ROI setIsPredictedFromPast:]
+ -[ROI setIsReflectedLS:]
+ -[ROI setIsTracked:]
+ -[ROI setIsTrajectoryPruningPassed:]
+ -[ROI setKpIsFromHW:]
+ -[ROI setLSIsHighRisk:]
+ -[ROI setLSOrGGBbox:]
+ -[ROI setLSTrackID:]
+ -[ROI setLSTrackingMatched:]
+ -[ROI setLSTrackingVote:]
+ -[ROI setLowSaliencyCnt:]
+ -[ROI setLsHasBeenUsedForTrackingGhost:]
+ -[ROI setLumaFeatureVector:]
+ -[ROI setLumaFeatureVectorPredictedLocation:]
+ -[ROI setLumaFeatureVectorReflection:]
+ -[ROI setMatchedLS:]
+ -[ROI setMv:]
+ -[ROI setMvCnt:]
+ -[ROI setMvSum:]
+ -[ROI setPredictedFromPastCnt:]
+ -[ROI setTemporalDetectionMatched:]
+ -[ROI setTemporalDetectionVote:]
+ -[ROI setTrackFail:]
+ -[ROI setTrackID:]
+ -[ROI setTrackIDsAfterMerge:]
+ -[ROI setTrackedCnt:]
+ -[ROI temporalDetectionMatched]
+ -[ROI temporalDetectionVote]
+ -[ROI trackFail]
+ -[ROI trackID]
+ -[ROI trackIDsAfterMerge]
+ -[ROI trackedCnt]
+ -[SRNet .cxx_destruct]
+ -[SRNet allocateOutputBufferObjects]
+ -[SRNet allocateOutputBufferObjects].cold.1
+ -[SRNet allocateOutputBufferObjects].cold.2
+ -[SRNet allocateOutputBufferObjects].cold.3
+ -[SRNet compileModelOnDevice]
+ -[SRNet compileModelOnDevice].cold.1
+ -[SRNet compileModelOnDevice].cold.2
+ -[SRNet compileModelOnDevice].cold.3
+ -[SRNet compileModelOnDevice].cold.4
+ -[SRNet compileModelOnDevice].cold.5
+ -[SRNet createFunction]
+ -[SRNet createFunction].cold.1
+ -[SRNet createFunction].cold.2
+ -[SRNet createFunction].cold.3
+ -[SRNet dealloc]
+ -[SRNet executeSynchronouslyOperation:onStream:]
+ -[SRNet executeSynchronouslyOperation:onStream:].cold.1
+ -[SRNet executeSynchronouslyOperation:onStream:].cold.2
+ -[SRNet executeSynchronouslyOperation:onStream:].cold.3
+ -[SRNet executeSynchronouslyOperation:onStream:].cold.4
+ -[SRNet executeSynchronouslyOperation:onStream:].cold.5
+ -[SRNet executeSynchronouslyOperation:onStream:].cold.6
+ -[SRNet executeSynchronouslyOperation:onStream:].cold.7
+ -[SRNet executeSynchronouslyOperation:onStream:].cold.8
+ -[SRNet function]
+ -[SRNet getOutputPortNames]
+ -[SRNet getOutputPortNames].cold.1
+ -[SRNet getOutputPortNames].cold.2
+ -[SRNet initWithModelPath:inputWidth:inputHeight:]
+ -[SRNet initializeModel]
+ -[SRNet initializeModel].cold.1
+ -[SRNet initializeModel].cold.2
+ -[SRNet initializeModel].cold.3
+ -[SRNet initializeModel].cold.4
+ -[SRNet inputHeight]
+ -[SRNet inputWidth]
+ -[SRNet library]
+ -[SRNet modelPath]
+ -[SRNet normalization]
+ -[SRNet operation]
+ -[SRNet outputBufferObject]
+ -[SRNet outputPortName]
+ -[SRNet outputSurface]
+ -[SRNet output_port]
+ -[SRNet resetStream:]
+ -[SRNet resetStream:].cold.1
+ -[SRNet setInputHeight:]
+ -[SRNet setInputWidth:]
+ -[SRNet setModelPath:]
+ -[SRNet setNormalization:]
+ -[SRNet setOutputPortName:]
+ -[SRNet setOutputSurface:]
+ -[SRNet stream]
+ -[VDGDetectionUtilsV2 .cxx_destruct]
+ -[VDGDetectionUtilsV2 clearReferencedROIsForROIList:]
+ -[VDGDetectionUtilsV2 configuration]
+ -[VDGDetectionUtilsV2 dealloc]
+ -[VDGDetectionUtilsV2 findTinyKeypointLocationsFromLS:inputTexture:dilation:estimatedOpticalCenter:metalBuffers:maxBufferLength:keypointSampleStepCount:]
+ -[VDGDetectionUtilsV2 generateBoxesForDoGAndLumaAndForLSROIs:prevGGROIs:inputTexture:opticalCenter:metalBuffers:maxBufferLength:]
+ -[VDGDetectionUtilsV2 generateBoxesForDoGAndLumaAndForPrevLSROIs:homography:metalBuffers:maxBufferLength:]
+ -[VDGDetectionUtilsV2 generateBoxesForDoGAndLumaAndForPrevLSROIs:homography:metalBuffers:maxBufferLength:].cold.1
+ -[VDGDetectionUtilsV2 generateBoxesForDoGAndLumaAndForPrevLSROIs:homography:metalBuffers:maxBufferLength:].cold.2
+ -[VDGDetectionUtilsV2 generateDetectionRoiList:outputArray:]
+ -[VDGDetectionUtilsV2 generateTrajectoryForROI:isGG:]
+ -[VDGDetectionUtilsV2 generateTrajectoryForROIList:isGG:]
+ -[VDGDetectionUtilsV2 getBestROIInROIList:referenceROI:]
+ -[VDGDetectionUtilsV2 getClosestRoi:forCoord:]
+ -[VDGDetectionUtilsV2 getDetectionRoiListFromMeta:outputArray:]
+ -[VDGDetectionUtilsV2 getDetectionRoiListFromMeta:outputArray:].cold.1
+ -[VDGDetectionUtilsV2 getDetectionRoiListFromMeta:outputArray:].cold.2
+ -[VDGDetectionUtilsV2 getDetectionRoiListFromMeta:outputArray:].cold.3
+ -[VDGDetectionUtilsV2 getGGCandidatesFromROIList:GGList:]
+ -[VDGDetectionUtilsV2 getGhostTrackIdFromLs:]
+ -[VDGDetectionUtilsV2 getHighRiskLS:]
+ -[VDGDetectionUtilsV2 getReflLsListAsDetectedROIFromMeta:]
+ -[VDGDetectionUtilsV2 getReflLsListFromMeta:outputArray:]
+ -[VDGDetectionUtilsV2 getReflLsListFromMeta:outputArray:].cold.1
+ -[VDGDetectionUtilsV2 getReflLsListFromMeta:outputArray:].cold.2
+ -[VDGDetectionUtilsV2 getRoiMvForRoiList:fromMeta:]
+ -[VDGDetectionUtilsV2 getSearchLocation:]
+ -[VDGDetectionUtilsV2 getTemporalDetectionSearchRadiusForReferenceFrameIndex:minSearchRadius:slope:]
+ -[VDGDetectionUtilsV2 getTopGhostsInList:k:opticalCenter:ghostCntGatingTh:]
+ -[VDGDetectionUtilsV2 getTopLSInList:k:dist2ghostTol:]
+ -[VDGDetectionUtilsV2 getTopLSInListByDroppingBottoms:k:dist2ghostTol:]
+ -[VDGDetectionUtilsV2 getTopLSInListByKeepingTops:k:dist2ghostTol:]
+ -[VDGDetectionUtilsV2 getTrajectoryMatchingCostGG:]
+ -[VDGDetectionUtilsV2 ghostIsHighConfidence:]
+ -[VDGDetectionUtilsV2 initWithMetalToolBox:configuration:tuningParams:]
+ -[VDGDetectionUtilsV2 isBoxSizeValidForProcessing:AndErodeBy:]
+ -[VDGDetectionUtilsV2 locIsInSearchRange:searchLocation:defaultSearchLocation:searchRadius:defaultSearchRange:searchInGivenLocsOnly:]
+ -[VDGDetectionUtilsV2 predictPrevLSLocation:usingPrevToCurrentHomography:]
+ -[VDGDetectionUtilsV2 pruneGGList:LSBBoxList:reflectedLSBBoxList:getMatchedLS:pruneLS:pruneGG:]
+ -[VDGDetectionUtilsV2 pruneGGList:LSList:opticalCenter:costToKeepLS:costToKeepGG:]
+ -[VDGDetectionUtilsV2 pruneGhostList:againstReflLsList:dilation:]
+ -[VDGDetectionUtilsV2 pruneLSBasedOnDist2Ghost:]
+ -[VDGDetectionUtilsV2 pruneUsingTrajectoryGGList:]
+ -[VDGDetectionUtilsV2 removeDuplicateRois:]
+ -[VDGDetectionUtilsV2 removeRedundantLS:]
+ -[VDGDetectionUtilsV2 removeRois:thatOverlapRefRois:dilationRadius:]
+ -[VDGDetectionUtilsV2 setConfiguration:]
+ -[VDGDetectionUtilsV2 setDefaultOpticalCenterForList:opticalCenter:]
+ -[VDGDetectionUtilsV2 setRoiMvForMeta:fromRoiList:]
+ -[VDGDetectionUtilsV2 sortArray:ofLength:]
+ -[VDGDetectionUtilsV2 sortKPs:opticalCenter:]
+ -[VDGDetectionUtilsV2 trackMeta:refMeta:currMaxTrackId:]
+ -[VDGDetectionUtilsV2 updateDoGAndLumaFeaturesWithMetalBuffers:]
+ -[VDGDetectionUtilsV2 updateDoGAndLumaFeaturesWithMetalBuffers:].cold.1
+ -[VDGDetectionUtilsV2 updateNewRoiPixFea:withRefPixFea:]
+ -[VDGDetectionUtilsV2 updatePrevLSDoGAndLumaFeaturesWithMetalBuffers:]
+ -[VDGDetectionUtilsV2 updatePrevLSDoGAndLumaFeaturesWithMetalBuffers:].cold.1
+ -[VDGDetectionUtilsV2 updatePrevLSDoGAndLumaFeaturesWithMetalBuffers:].cold.2
+ -[VDGDetectionUtilsV2 warpRoisUsingMv:]
+ -[VDGProcessor .cxx_destruct]
+ -[VDGProcessor finishProcessing]
+ -[VDGProcessor initWithFrameWidth:FrameHeight:usePrecomputedFlow:revision:]
+ -[VDGProcessor processWithDeghostingParams:error:]
+ -[VDGProcessor startSessionWithDeghostingConfig:error:]
+ -[VEEspressoModel initContextWithFilePath:engine:configuration:usePreCompiled:]
+ -[VEEspressoModel initContextWithFilePath:engine:configuration:usePreCompiled:].cold.1
+ -[VEEspressoModel initContextWithFilePath:engine:configuration:usePreCompiled:].cold.2
+ -[VEEspressoModel initContextWithFilePath:engine:configuration:usePreCompiled:].cold.3
+ -[VEEspressoModel initWithModelPath:usage:useMPS:]
+ -[VEEspressoModel loadModelFromPath:]
+ -[VSRNet .cxx_destruct]
+ -[VSRNet allocateInputBufferObjects]
+ -[VSRNet allocateInputBufferObjects].cold.1
+ -[VSRNet allocateInputBufferObjects].cold.2
+ -[VSRNet allocateInputBufferObjects].cold.3
+ -[VSRNet allocateInputBufferObjects].cold.4
+ -[VSRNet allocateInputBufferObjects].cold.5
+ -[VSRNet allocateInputBufferObjects].cold.6
+ -[VSRNet allocateInputBufferObjects].cold.7
+ -[VSRNet allocateInputBufferObjects].cold.8
+ -[VSRNet dealloc]
+ -[VSRNet getInputPortNames]
+ -[VSRNet getInputPortNames].cold.1
+ -[VSRNet getInputPortNames].cold.2
+ -[VSRNet initWithModelPath:inputWidth:inputHeight:]
+ -[VSRNet initializeInputPorts]
+ -[VSRNet initializeInputPorts].cold.1
+ -[VSRNet initializeInputPorts].cold.2
+ -[VSRNet inputSurface]
+ -[VSRNet prevHRSurface]
+ -[VSRNet processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:]
+ -[VSRNet processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:].cold.1
+ -[VSRNet processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:].cold.2
+ -[VSRNet processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:].cold.3
+ -[VSRNet setInputSurface:]
+ -[VSRNet setPrevHRSurface:]
+ -[VideoDeghostingDetectionV2 .cxx_destruct]
+ -[VideoDeghostingDetectionV2 LSTrackID]
+ -[VideoDeghostingDetectionV2 _getProbMapInput:reflLs:trackingRef:trackingRefProb:trackingRefSpaProb:trackingRefErrRescaleProb:trackingRefLs:inputBuf:reflLsBuf:trackingRefBuf:trackingRefProbBuf:trackingRefSpaProbBuf:trackingRefErrRescaleProbBuf:trackingRefLsBuf:trackingMvf:metaBuf:metaBufArray:trackingRefMetaBuf:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:refinedReflLs:probMapStash4FutureTracking:probMapBuf:errRescaleProbMapBuf:rawRefinedProbMapBuf:refinedProbMapBuf:refinedReflLsBuf:probMapStash4FutureTrackingBuf:doTracking:waitForComplete:]
+ -[VideoDeghostingDetectionV2 _getProbMapsLiteTarget:refProbMap:refLsMap:refRefinedLsMap:refProbMapStash4FutureTracking:refErrRescaleProbMap:refRawRefinedProbMap:refRefinedProbMap:mvf:probMap:lsMap:refinedLsMap:probMapStash4FutureTracking:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:metaBufArray:waitForComplete:]
+ -[VideoDeghostingDetectionV2 _initDetection:futureFrames:outputImgBufTMinus1:outputImgBufTMinus2:]
+ -[VideoDeghostingDetectionV2 _initParamsWithLowLight:]
+ -[VideoDeghostingDetectionV2 _resetDetectionResults]
+ -[VideoDeghostingDetectionV2 _resetIntermediateVariables]
+ -[VideoDeghostingDetectionV2 configuration]
+ -[VideoDeghostingDetectionV2 dealloc]
+ -[VideoDeghostingDetectionV2 dlSpatialRepairYUV:output:repairMask:blendMask:inputTex:repairMaskTex:blendMaskTex:wRepairedY:wRepairedUV:metaBuf:]
+ -[VideoDeghostingDetectionV2 doTrackingToNextFrameCurrMetaWithDetectionResults:currMetaWithMvToFuture:futureMeta:opticalCenter:futureOpticalCenter:futureFrameCnt:doLite:waitForComplete:]
+ -[VideoDeghostingDetectionV2 getFlowTarget:ref:targetBuf:refBuf:mvf:backwardMvf:metaBuf:skipRescaling:]
+ -[VideoDeghostingDetectionV2 getMvfToNextFrameForTrackingCurrMeta:lsMap:futureLsMap:lsMapBuf:futureLsMapBuf:opticalCenter:futureOpticalCenter:waitForComplete:]
+ -[VideoDeghostingDetectionV2 getProbMapsTarget:ref:rawProbMap:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:reflLsMap:refinedReflLsMap:reflLsMap4TrackingRef:metaBuf:metaBufArray:trackingMvf:useRefProbMap:opticalCenter:trackingRefOpticalCenter:waitForComplete:]
+ -[VideoDeghostingDetectionV2 initWithMetalToolBox:config:imageDimensions:]
+ -[VideoDeghostingDetectionV2 params]
+ -[VideoDeghostingDetectionV2 prevShouldRunGGDetectionClippedPixelBased]
+ -[VideoDeghostingDetectionV2 prevShouldRunGGDetectionLSBased]
+ -[VideoDeghostingDetectionV2 prevShouldRunGGDetectionLuxLevelBased]
+ -[VideoDeghostingDetectionV2 process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:]
+ -[VideoDeghostingDetectionV2 processHwLsMaskAndGetRoisOpticalCenter:inputFrame:prevMetaContainer:considerDist2PrevGhostWhenSort:outputMask:outputMaskTexture:isLowLight:outputArray:]
+ -[VideoDeghostingDetectionV2 processHwLsMaskNormalizedCenter:input:output:waitForComplete:]
+ -[VideoDeghostingDetectionV2 repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:]
+ -[VideoDeghostingDetectionV2 reset]
+ -[VideoDeghostingDetectionV2 setConfiguration:]
+ -[VideoDeghostingDetectionV2 setLSTrackID:]
+ -[VideoDeghostingDetectionV2 setParams:]
+ -[VideoDeghostingDetectionV2 setPrevShouldRunGGDetectionClippedPixelBased:]
+ -[VideoDeghostingDetectionV2 setPrevShouldRunGGDetectionLSBased:]
+ -[VideoDeghostingDetectionV2 setPrevShouldRunGGDetectionLuxLevelBased:]
+ -[VideoDeghostingDetectionV2 setTrackID:]
+ -[VideoDeghostingDetectionV2 sortLsList:]
+ -[VideoDeghostingDetectionV2 trackID]
+ -[VideoDeghostingDetectionV2 unpackIspLsMaskAndRoisForNextFrameLiteWithFrameData:futureOpticalCenter:outputFutureFrameCnt:outputFutureMetaBuf:]
+ -[VideoDeghostingDetectionV2 unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:outputFutureFrameCnt:outputMTLBuffer:]
+ -[VideoDeghostingDetectionV2 unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:outputFutureFrameCnt:outputMTLBuffer:].cold.1
+ -[VideoDeghostingDetectionV2 updateRepairedRefYUVInput:opticalCenter:prob:errRescaleProb:prevProb:refinedProb:probMap4TrRefW:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:inputBuf:probBuf:errRescaleProbBuf:prevProbBuf:refinedProbBuf:probMap4TrRefWBuf:frRef0Buf:frRef1Buf:nextFrameBuf:metaBuf:metaBufArray:forceToSpatial:waitForComplete:]
+ -[VideoDeghostingDetectionV2 warpTrackingRefProbMap:refSpaProbMap:refReflLs:mvf:metaBuf:metaBufArray:waitForComplete:]
+ -[Warper encodeWarpBlendToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:]
+ -[Warper warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toHighResBufferTexture:]
+ -[boundingBoxForMerge extendBBox]
+ -[boundingBoxForMerge index2RoiArray]
+ -[boundingBoxForMerge setExtendBBox:]
+ -[boundingBoxForMerge setIndex2RoiArray:]
+ GCC_except_table14
+ GCC_except_table27
+ GCC_except_table31
+ GCC_except_table5
+ GCC_except_table7
+ GCC_except_table9
+ _CGRectContainsRect
+ _CGRectEqualToRect
+ _CGRectGetMaxX
+ _CGRectGetMaxY
+ _CGRectGetMidX
+ _CGRectGetMidY
+ _CGRectGetMinX
+ _CGRectGetMinY
+ _CGRectInset
+ _CGRectIntersection
+ _CGRectIntersectsRect
+ _CGRectIsNull
+ _CGRectNull
+ _CGRectToIntRect
+ _CGRectUnion
+ _CGRectZero
+ _CVBufferCopyAttachments
+ _CVBufferSetAttachments
+ _CVMetalTextureCacheCreate
+ _CVMetalTextureCacheCreateTextureFromImage
+ _CVMetalTextureCacheFlush
+ _CVMetalTextureGetTexture
+ _ConvertCIImageToPixBuffer
+ _CreatePixelBufferHelper
+ _IOSurfaceGetBulkAttachments
+ _IOSurfaceGetElementHeight
+ _IOSurfaceGetElementWidth
+ _IOSurfaceGetHeightOfPlane
+ _IOSurfaceGetPixelFormat
+ _IOSurfaceGetWidthOfPlane
+ _OBJC_CLASS_$_CIColor
+ _OBJC_CLASS_$_DVPLensFlareMitigationConfiguration
+ _OBJC_CLASS_$_DVPLensFlareMitigationParameters
+ _OBJC_CLASS_$_DetectedROI
+ _OBJC_CLASS_$_GGMController
+ _OBJC_CLASS_$_GGMMetalToolBox
+ _OBJC_CLASS_$_ISRNet
+ _OBJC_CLASS_$_MAAutoAsset
+ _OBJC_CLASS_$_MAAutoAssetPolicy
+ _OBJC_CLASS_$_MAAutoAssetSelector
+ _OBJC_CLASS_$_MaskToRoi
+ _OBJC_CLASS_$_MitigationANE
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_PixelMemory
+ _OBJC_CLASS_$_ROI
+ _OBJC_CLASS_$_VDGDetectionUtilsV2
+ _OBJC_CLASS_$_VDGProcessor
+ _OBJC_CLASS_$_VEMobileAsset
+ _OBJC_CLASS_$_VSRNet
+ _OBJC_CLASS_$_VideoDeghostingDetectionV2
+ _OBJC_CLASS_$_boundingBoxForMerge
+ _OBJC_IVAR_$_DVPLensFlareMitigationConfiguration._frameHeight
+ _OBJC_IVAR_$_DVPLensFlareMitigationConfiguration._framePreferredPixelFormats
+ _OBJC_IVAR_$_DVPLensFlareMitigationConfiguration._frameSupportedPixelFormats
+ _OBJC_IVAR_$_DVPLensFlareMitigationConfiguration._frameWidth
+ _OBJC_IVAR_$_DVPLensFlareMitigationConfiguration._qualityPrioritization
+ _OBJC_IVAR_$_DVPLensFlareMitigationConfiguration._revision
+ _OBJC_IVAR_$_DVPLensFlareMitigationConfiguration._usePrecomputedFlow
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._destinationFrame
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._nextFrame
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._nextFrameOpticalCenter
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._opticalCenterShift
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._opticalFlow
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._previousOutputFrame
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._previousPreviousOutputFrame
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._sourceFrame
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._sourceFrameOpticalCenter
+ _OBJC_IVAR_$_DVPLensFlareMitigationParameters._submissionMode
+ _OBJC_IVAR_$_DVPSuperResolutionParameters._submissionMode
+ _OBJC_IVAR_$_DetectedROI._LSRoi
+ _OBJC_IVAR_$_DetectedROI._centerPoint
+ _OBJC_IVAR_$_DetectedROI._confidence
+ _OBJC_IVAR_$_DetectedROI._des
+ _OBJC_IVAR_$_DetectedROI._isPredictedFromPast
+ _OBJC_IVAR_$_DetectedROI._isReflectedLS
+ _OBJC_IVAR_$_DetectedROI._isTracked
+ _OBJC_IVAR_$_DetectedROI._isTrajectoryPruningPassed
+ _OBJC_IVAR_$_DetectedROI._lowSaliencyCnt
+ _OBJC_IVAR_$_DetectedROI._predictedFromPastCnt
+ _OBJC_IVAR_$_DetectedROI._roi
+ _OBJC_IVAR_$_DetectedROI._roiId
+ _OBJC_IVAR_$_DetectedROI._roiMv
+ _OBJC_IVAR_$_DetectedROI._trackID
+ _OBJC_IVAR_$_DetectedROI._trackSessionId
+ _OBJC_IVAR_$_DetectedROI._trackedCnt
+ _OBJC_IVAR_$_DetectedROI._trajectoryFromPast
+ _OBJC_IVAR_$_FRNet._modelPath
+ _OBJC_IVAR_$_GGMController._GGDetector
+ _OBJC_IVAR_$_GGMController._commandQueue
+ _OBJC_IVAR_$_GGMController._configure
+ _OBJC_IVAR_$_GGMController._detectedGreenGhostInfo
+ _OBJC_IVAR_$_GGMController._device
+ _OBJC_IVAR_$_GGMController._futureFramesToDetectionAndRepair
+ _OBJC_IVAR_$_GGMController._futureInputParamsToRepair
+ _OBJC_IVAR_$_GGMController._inputBuffer
+ _OBJC_IVAR_$_GGMController._inputParamsToRepair
+ _OBJC_IVAR_$_GGMController._ispTimeStamp
+ _OBJC_IVAR_$_GGMController._keyPointsList
+ _OBJC_IVAR_$_GGMController._lightSourceMask
+ _OBJC_IVAR_$_GGMController._lookaheadFrameProcessedInFinish
+ _OBJC_IVAR_$_GGMController._lookaheadFrames
+ _OBJC_IVAR_$_GGMController._metaDictionary
+ _OBJC_IVAR_$_GGMController._metaInfoQueue
+ _OBJC_IVAR_$_GGMController._metalToolbox
+ _OBJC_IVAR_$_GGMController._nextVisedOpticalCenter
+ _OBJC_IVAR_$_GGMController._opticalCenterArray
+ _OBJC_IVAR_$_GGMController._opticalCenterArrayIndex
+ _OBJC_IVAR_$_GGMController._opticalCenterArrayLen
+ _OBJC_IVAR_$_GGMController._opticalCenterMvShift
+ _OBJC_IVAR_$_GGMController._opticalCenterMvShiftArray
+ _OBJC_IVAR_$_GGMController._processedFrameInDetection
+ _OBJC_IVAR_$_GGMController._processedPixelBuffer
+ _OBJC_IVAR_$_GGMController._scaler
+ _OBJC_IVAR_$_GGMController._tuningParamDict
+ _OBJC_IVAR_$_GGMController._visedOpticalCenter
+ _OBJC_IVAR_$_GGMMetalToolBox._addMvf0AndMvf1
+ _OBJC_IVAR_$_GGMMetalToolBox._alignBgAvgYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._bilinearRescale2ImgsYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._bilinearRescaleYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._blendRefsYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._blendSpatialMitigatedYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._bmSearch1RefFixedSampleCntYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._bmSearch1RefYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._bmSearch4RepairYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._bmTransfer4RepairYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._bmTransferGray
+ _OBJC_IVAR_$_GGMMetalToolBox._bmTransferWithRoiRepairMvYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._bmTransferYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._collectClusterBgAvg
+ _OBJC_IVAR_$_GGMMetalToolBox._collectClusterMaxAndAvgLuma
+ _OBJC_IVAR_$_GGMMetalToolBox._collectClusterMaxProb
+ _OBJC_IVAR_$_GGMMetalToolBox._collectClusterMv
+ _OBJC_IVAR_$_GGMMetalToolBox._collectClusterMvForMotionCue
+ _OBJC_IVAR_$_GGMMetalToolBox._collectClusterTempRepairErr
+ _OBJC_IVAR_$_GGMMetalToolBox._collectMetaContainers
+ _OBJC_IVAR_$_GGMMetalToolBox._collectMvToFuture
+ _OBJC_IVAR_$_GGMMetalToolBox._collectOverlapWithRefs
+ _OBJC_IVAR_$_GGMMetalToolBox._combineMapWithRefMap
+ _OBJC_IVAR_$_GGMMetalToolBox._conditionalDilateProbMapYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._convertFloatBuffer2Texture
+ _OBJC_IVAR_$_GGMMetalToolBox._copyCurrMetaForProcFuture
+ _OBJC_IVAR_$_GGMMetalToolBox._copyFullFrameMapToMap4RoiGen
+ _OBJC_IVAR_$_GGMMetalToolBox._copyMapToMap4RoiGen
+ _OBJC_IVAR_$_GGMMetalToolBox._copyMvf
+ _OBJC_IVAR_$_GGMMetalToolBox._cvMetalTextureCacheRef
+ _OBJC_IVAR_$_GGMMetalToolBox._dilateForwarpHoleMap
+ _OBJC_IVAR_$_GGMMetalToolBox._dilateGrayImg
+ _OBJC_IVAR_$_GGMMetalToolBox._dilateProbMap
+ _OBJC_IVAR_$_GGMMetalToolBox._dilateReflLsMap
+ _OBJC_IVAR_$_GGMMetalToolBox._forceGpuWaitForComplete
+ _OBJC_IVAR_$_GGMMetalToolBox._fuse4DetectionYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._getBgAvgYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._getBlobSaliency
+ _OBJC_IVAR_$_GGMMetalToolBox._getGhostProbMapYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._getLsMapYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._getMotionMapYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._getMvForMotionCueFromMvf
+ _OBJC_IVAR_$_GGMMetalToolBox._getMvFromLs
+ _OBJC_IVAR_$_GGMMetalToolBox._getMvToFutureFromMvf
+ _OBJC_IVAR_$_GGMMetalToolBox._getOverlapWithRefs
+ _OBJC_IVAR_$_GGMMetalToolBox._getRoiMaxAndAvgLumaYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._getRoiRepairMvFromMvf
+ _OBJC_IVAR_$_GGMMetalToolBox._getSaliencyMapYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._getTempRepairedBgAlignErrYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._metaBufArray
+ _OBJC_IVAR_$_GGMMetalToolBox._metaContainer
+ _OBJC_IVAR_$_GGMMetalToolBox._preprocessInputs4MotionCueYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._refineFutureHwLsMapWithTrackingYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._reflectYUVImg2
+ _OBJC_IVAR_$_GGMMetalToolBox._resetOutput
+ _OBJC_IVAR_$_GGMMetalToolBox._setWOri
+ _OBJC_IVAR_$_GGMMetalToolBox._spatialRepairYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._spatialTemporalRepair4DetectionYUV
+ _OBJC_IVAR_$_GGMMetalToolBox._syncWeightsOriginal
+ _OBJC_IVAR_$_GGMMetalToolBox._tuningParams
+ _OBJC_IVAR_$_GGMMetalToolBox._updateOutputFloat
+ _OBJC_IVAR_$_GGMMetalToolBox._upscaleProbMap
+ _OBJC_IVAR_$_GGMMetalToolBox._upscaleThenReflectLsMap
+ _OBJC_IVAR_$_GGMMetalToolBox._visualizeMvf
+ _OBJC_IVAR_$_GGMMetalToolBox._warpMvf0WithMvf1
+ _OBJC_IVAR_$_GGMMetalToolBox._warpMvf0WithMvf1ThenAddToMvf2
+ _OBJC_IVAR_$_GGMMetalToolBox._warpRefMeta
+ _OBJC_IVAR_$_GGMMetalToolBox._warpRefMetaLite
+ _OBJC_IVAR_$_ISRNet._inputBufferObject
+ _OBJC_IVAR_$_ISRNet._inputPortName
+ _OBJC_IVAR_$_ISRNet._inputSurface
+ _OBJC_IVAR_$_ISRNet._input_port
+ _OBJC_IVAR_$_ImageSR._modelPath
+ _OBJC_IVAR_$_MaskToRoi._bboxList
+ _OBJC_IVAR_$_MaskToRoi._connectedPixelsQueue
+ _OBJC_IVAR_$_MaskToRoi._height
+ _OBJC_IVAR_$_MaskToRoi._integralSumPixelBuffer
+ _OBJC_IVAR_$_MaskToRoi._metalToolbox
+ _OBJC_IVAR_$_MaskToRoi._neighbors
+ _OBJC_IVAR_$_MaskToRoi._width
+ _OBJC_IVAR_$_MitigationANE._blendingParams
+ _OBJC_IVAR_$_MitigationANE._cvMetalTextureCacheRef
+ _OBJC_IVAR_$_MitigationANE._espressoContext
+ _OBJC_IVAR_$_MitigationANE._espressoEngine
+ _OBJC_IVAR_$_MitigationANE._espressoInputImageBuffer
+ _OBJC_IVAR_$_MitigationANE._espressoInputMaskBuffer
+ _OBJC_IVAR_$_MitigationANE._espressoNetwork
+ _OBJC_IVAR_$_MitigationANE._espressoOutputBuffer
+ _OBJC_IVAR_$_MitigationANE._espressoPlan
+ _OBJC_IVAR_$_MitigationANE._imageDimensions
+ _OBJC_IVAR_$_MitigationANE._inputROI
+ _OBJC_IVAR_$_MitigationANE._maxRoiHeight
+ _OBJC_IVAR_$_MitigationANE._maxRoiWidth
+ _OBJC_IVAR_$_MitigationANE._metalToolbox
+ _OBJC_IVAR_$_MitigationANE._netSize
+ _OBJC_IVAR_$_MitigationANE._pipelineStates
+ _OBJC_IVAR_$_MitigationANE._repairParameters
+ _OBJC_IVAR_$_MitigationANE._tileConfig
+ _OBJC_IVAR_$_MitigationANE._tileInputImageTexture
+ _OBJC_IVAR_$_MitigationANE._tileInputPixelBuffer
+ _OBJC_IVAR_$_MitigationANE._tileOutputPixelBuffer
+ _OBJC_IVAR_$_MitigationANE._tileOutputPixelBufferLr
+ _OBJC_IVAR_$_OFNormalization._copyRgbTo4x4ShuffledTextureArray
+ _OBJC_IVAR_$_OFNormalization._copyRgbToTextureArray
+ _OBJC_IVAR_$_OFNormalization._copyTextureArrayToRgb
+ _OBJC_IVAR_$_OFNormalization._padRGBKernel
+ _OBJC_IVAR_$_PixelMemory._buf
+ _OBJC_IVAR_$_PixelMemory._bytePerPixel
+ _OBJC_IVAR_$_PixelMemory._channels
+ _OBJC_IVAR_$_PixelMemory._format
+ _OBJC_IVAR_$_PixelMemory._height
+ _OBJC_IVAR_$_PixelMemory._pMemory
+ _OBJC_IVAR_$_PixelMemory._pMemoryPlane2
+ _OBJC_IVAR_$_PixelMemory._readBufferOnly
+ _OBJC_IVAR_$_PixelMemory._skipClamp
+ _OBJC_IVAR_$_PixelMemory._stride
+ _OBJC_IVAR_$_PixelMemory._stridePlane2
+ _OBJC_IVAR_$_PixelMemory._width
+ _OBJC_IVAR_$_ROI._LSIsHighRisk
+ _OBJC_IVAR_$_ROI._LSOrGGBbox
+ _OBJC_IVAR_$_ROI._LSTrackID
+ _OBJC_IVAR_$_ROI._LSTrackingMatched
+ _OBJC_IVAR_$_ROI._LSTrackingVote
+ _OBJC_IVAR_$_ROI._area
+ _OBJC_IVAR_$_ROI._bbox
+ _OBJC_IVAR_$_ROI._defaultOpticalCenter
+ _OBJC_IVAR_$_ROI._descriptor
+ _OBJC_IVAR_$_ROI._differenceOfGaussianAndLumaFeature
+ _OBJC_IVAR_$_ROI._differenceOfGaussianAndLumaFeaturePredictedLocation
+ _OBJC_IVAR_$_ROI._differenceOfGaussianAndLumaFeatureReflection
+ _OBJC_IVAR_$_ROI._dist2ghost
+ _OBJC_IVAR_$_ROI._dist2opticalCenter
+ _OBJC_IVAR_$_ROI._doneKPToBBoxViaGraphTraversal
+ _OBJC_IVAR_$_ROI._isPredictedFromPast
+ _OBJC_IVAR_$_ROI._isReflectedLS
+ _OBJC_IVAR_$_ROI._isTracked
+ _OBJC_IVAR_$_ROI._isTrajectoryPruningPassed
+ _OBJC_IVAR_$_ROI._kpIsFromHW
+ _OBJC_IVAR_$_ROI._lowSaliencyCnt
+ _OBJC_IVAR_$_ROI._lsHasBeenUsedForTrackingGhost
+ _OBJC_IVAR_$_ROI._lumaFeatureVector
+ _OBJC_IVAR_$_ROI._lumaFeatureVectorPredictedLocation
+ _OBJC_IVAR_$_ROI._lumaFeatureVectorReflection
+ _OBJC_IVAR_$_ROI._matchedLS
+ _OBJC_IVAR_$_ROI._mv
+ _OBJC_IVAR_$_ROI._mvCnt
+ _OBJC_IVAR_$_ROI._mvSum
+ _OBJC_IVAR_$_ROI._predictedFromPastCnt
+ _OBJC_IVAR_$_ROI._temporalDetectionMatched
+ _OBJC_IVAR_$_ROI._temporalDetectionVote
+ _OBJC_IVAR_$_ROI._trackFail
+ _OBJC_IVAR_$_ROI._trackID
+ _OBJC_IVAR_$_ROI._trackIDsAfterMerge
+ _OBJC_IVAR_$_ROI._trackedCnt
+ _OBJC_IVAR_$_SRNet._function
+ _OBJC_IVAR_$_SRNet._inputHeight
+ _OBJC_IVAR_$_SRNet._inputWidth
+ _OBJC_IVAR_$_SRNet._library
+ _OBJC_IVAR_$_SRNet._modelPath
+ _OBJC_IVAR_$_SRNet._normalization
+ _OBJC_IVAR_$_SRNet._operation
+ _OBJC_IVAR_$_SRNet._outputBufferObject
+ _OBJC_IVAR_$_SRNet._outputPortName
+ _OBJC_IVAR_$_SRNet._outputSurface
+ _OBJC_IVAR_$_SRNet._output_port
+ _OBJC_IVAR_$_SRNet._stream
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._bboxList
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._bboxListLen
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._configuration
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._dist2OpticalCenterList
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._dist2OpticalCenterListLen
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._kpIsFromHWList
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._kpIsFromHWListLen
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._locationList
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._locationListLen
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._metalToolBox
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._processedPrevLSROIs
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._processedPrevLSType
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._processedROIs
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._processedType
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._reflectedLSList
+ _OBJC_IVAR_$_VDGDetectionUtilsV2._reflectedLSListLen
+ _OBJC_IVAR_$_VDGProcessor._acceptsOpticalFlow
+ _OBJC_IVAR_$_VDGProcessor._backwardFlow
+ _OBJC_IVAR_$_VDGProcessor._flowBufferHeight
+ _OBJC_IVAR_$_VDGProcessor._flowBufferWidth
+ _OBJC_IVAR_$_VDGProcessor._forwardFlow
+ _OBJC_IVAR_$_VDGProcessor._frameHeight
+ _OBJC_IVAR_$_VDGProcessor._frameWidth
+ _OBJC_IVAR_$_VDGProcessor._ggmController
+ _OBJC_IVAR_$_VDGProcessor._opticalFlowBuffers
+ _OBJC_IVAR_$_VDGProcessor._opticalFlowConfig
+ _OBJC_IVAR_$_VDGProcessor._opticalFlowParams
+ _OBJC_IVAR_$_VDGProcessor._opticalFlowProcessor
+ _OBJC_IVAR_$_VDGProcessor._usePrecomputedFlow
+ _OBJC_IVAR_$_VSRNet._inputBufferObjects
+ _OBJC_IVAR_$_VSRNet._inputPortNames
+ _OBJC_IVAR_$_VSRNet._inputSurface
+ _OBJC_IVAR_$_VSRNet._input_ports
+ _OBJC_IVAR_$_VSRNet._prevHRSurface
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._LSTrackID
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRef0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRef0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRef1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._avgAlignedRef1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._backwarpFlowMvf0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._backwarpFlowMvf0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._backwarpFlowMvf1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._backwarpFlowMvf1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._blendedRef0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._blendedRef0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._blendedRef1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._blendedRef1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._blobSaliencyMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._blobSaliencyMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._bmRef0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._bmRef0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._bmRef1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._bmRef1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._commandQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._concurrentQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._configuration
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._currMetaTmp
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._currSegmentProcessedFrameCnt
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._detectionUtils
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._device
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedFlowRef0Map
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedFlowRef0MapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedFlowRef1Map
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedFlowRef1MapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedLsMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dilatedLsMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dispatchGroup
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dlSpaBlendMask
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dlSpaBlendMaskTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dlSpaInput
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dlSpaInputTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dlSpaRepairMask
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dlSpaRepairMaskTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dlSpatialMitigated
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._dlSpatialMitigatedTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._errRescaleProbMap0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._errRescaleProbMap0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._errRescaleProbMap1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._errRescaleProbMap1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._filteredOpticalCenterShift
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowMvf0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowMvf0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowMvf1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowMvf1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowNet
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowPreprocessor
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowRef
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowRef0Map
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowRef0MapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowRef1Map
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowRef1MapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowRefTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowTarget
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._flowTargetTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._forwarpOutputBuffer0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._forwarpOutputBuffer1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._frameT
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._frameTMinus1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._frameTMinus1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._frameTMinus2
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._frameTMinus2Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._frameTPlus1Buf
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._frameTPlus1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._frameTPlus2Buf
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._fullResRawRefinedProbMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._fullResRawRefinedProbMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._fullResStashedProbMap4FutureTracking
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._fullResStashedProbMap4FutureTrackingTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._futureMeta4LsCheck
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._futureMeta4RedoTracking
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._futureMetaTmp
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._hmgrphyRef0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._hmgrphyRef0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._hmgrphyRef1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._hmgrphyRef1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._imageDimensions
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._input4MotionCue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._input4MotionCueTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputCopy
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputCopyTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._inputTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lrBmRef0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lrBmRef0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lrBmRef1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lrBmRef1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lrHwLsMask0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lrHwLsMask0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lrHwLsMask1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lrHwLsMask1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lsMap4RoiGen
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lsMap4RoiGenTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lsMapQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._lsMapTexQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._maskToRoi
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._metaArray
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._metaBufferArray
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._metalToolBox
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._mitigationANE
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._motionMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._motionMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._mvf4Future
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._mvf4FutureTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._mvf4Repair0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._mvf4Repair0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._mvf4Repair1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._mvf4Repair1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._params
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._prevShouldRunGGDetectionClippedPixelBased
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._prevShouldRunGGDetectionLSBased
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._prevShouldRunGGDetectionLuxLevelBased
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._probMap4RepairQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._probMap4RepairTexQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._probMap4RoiGen
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._probMap4RoiGenTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._probMap4SpatialRepairQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._probMap4SpatialRepairTexQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._probMapQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._probMapTexQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._processedFrameCnt
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._rawProbMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._rawProbMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._rawWarpedRefProbMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._rawWarpedRefProbMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._rawWarpedRefSpaProbMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._rawWarpedRefSpaProbMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._ref4MotionCue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._ref4MotionCueTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._refinedReflLs4trackingRefWarped
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._refinedReflLs4trackingRefWarpedTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._reflHwLsMask0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._reflHwLsMask0Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._reflHwLsMask1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._reflHwLsMask1Texture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._saliencyMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._saliencyMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._spaProbMapQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._spaProbMapTexQueue
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._spatialMitigated
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._spatialMitigatedTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._stashedFutureGhostRois0
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._stashedFutureGhostRois1
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._temporalMitigated
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._temporalMitigatedTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._trackID
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._tradSpatialMitigated
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._tradSpatialMitigatedTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedFlowMvf
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedFlowMvfTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedHwLsMask4Track
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedHwLsMask4TrackTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedRefProbMap
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedRefProbMapTexture
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedReflTrackingRef
+ _OBJC_IVAR_$_VideoDeghostingDetectionV2._warpedReflTrackingRefTexture
+ _OBJC_IVAR_$_Warper._warpBlendRGBKernel
+ _OBJC_IVAR_$_boundingBoxForMerge._extendBBox
+ _OBJC_IVAR_$_boundingBoxForMerge._index2RoiArray
+ _OBJC_METACLASS_$_DVPLensFlareMitigationConfiguration
+ _OBJC_METACLASS_$_DVPLensFlareMitigationParameters
+ _OBJC_METACLASS_$_DetectedROI
+ _OBJC_METACLASS_$_GGMController
+ _OBJC_METACLASS_$_GGMMetalToolBox
+ _OBJC_METACLASS_$_ISRNet
+ _OBJC_METACLASS_$_MaskToRoi
+ _OBJC_METACLASS_$_MitigationANE
+ _OBJC_METACLASS_$_PixelMemory
+ _OBJC_METACLASS_$_ROI
+ _OBJC_METACLASS_$_VDGDetectionUtilsV2
+ _OBJC_METACLASS_$_VDGProcessor
+ _OBJC_METACLASS_$_VEMobileAsset
+ _OBJC_METACLASS_$_VSRNet
+ _OBJC_METACLASS_$_VideoDeghostingDetectionV2
+ _OBJC_METACLASS_$_boundingBoxForMerge
+ __OBJC_$_CLASS_METHODS_DVPLensFlareMitigationConfiguration
+ __OBJC_$_CLASS_METHODS_DVPLensFlareMitigationParameters
+ __OBJC_$_CLASS_METHODS_FRNet
+ __OBJC_$_CLASS_METHODS_GGMController
+ __OBJC_$_CLASS_METHODS_ImageSR
+ __OBJC_$_CLASS_METHODS_VEMobileAsset
+ __OBJC_$_CLASS_METHODS_VSRProcessor
+ __OBJC_$_INSTANCE_METHODS_DVPLensFlareMitigationConfiguration
+ __OBJC_$_INSTANCE_METHODS_DVPLensFlareMitigationParameters
+ __OBJC_$_INSTANCE_METHODS_DetectedROI
+ __OBJC_$_INSTANCE_METHODS_GGMController
+ __OBJC_$_INSTANCE_METHODS_GGMMetalToolBox
+ __OBJC_$_INSTANCE_METHODS_ISRNet
+ __OBJC_$_INSTANCE_METHODS_MaskToRoi
+ __OBJC_$_INSTANCE_METHODS_MitigationANE
+ __OBJC_$_INSTANCE_METHODS_PixelMemory
+ __OBJC_$_INSTANCE_METHODS_ROI
+ __OBJC_$_INSTANCE_METHODS_VDGDetectionUtilsV2
+ __OBJC_$_INSTANCE_METHODS_VDGProcessor
+ __OBJC_$_INSTANCE_METHODS_VSRNet
+ __OBJC_$_INSTANCE_METHODS_VideoDeghostingDetectionV2
+ __OBJC_$_INSTANCE_METHODS_boundingBoxForMerge
+ __OBJC_$_INSTANCE_VARIABLES_DVPLensFlareMitigationConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_DVPLensFlareMitigationParameters
+ __OBJC_$_INSTANCE_VARIABLES_DetectedROI
+ __OBJC_$_INSTANCE_VARIABLES_GGMController
+ __OBJC_$_INSTANCE_VARIABLES_GGMMetalToolBox
+ __OBJC_$_INSTANCE_VARIABLES_ISRNet
+ __OBJC_$_INSTANCE_VARIABLES_MaskToRoi
+ __OBJC_$_INSTANCE_VARIABLES_MitigationANE
+ __OBJC_$_INSTANCE_VARIABLES_PixelMemory
+ __OBJC_$_INSTANCE_VARIABLES_ROI
+ __OBJC_$_INSTANCE_VARIABLES_VDGDetectionUtilsV2
+ __OBJC_$_INSTANCE_VARIABLES_VDGProcessor
+ __OBJC_$_INSTANCE_VARIABLES_VSRNet
+ __OBJC_$_INSTANCE_VARIABLES_VideoDeghostingDetectionV2
+ __OBJC_$_INSTANCE_VARIABLES_boundingBoxForMerge
+ __OBJC_$_PROP_LIST_DVPLensFlareMitigationConfiguration
+ __OBJC_$_PROP_LIST_DVPLensFlareMitigationParameters
+ __OBJC_$_PROP_LIST_DetectedROI
+ __OBJC_$_PROP_LIST_GGMController
+ __OBJC_$_PROP_LIST_GGMMetalToolBox
+ __OBJC_$_PROP_LIST_ISRNet
+ __OBJC_$_PROP_LIST_MaskToRoi
+ __OBJC_$_PROP_LIST_PixelMemory
+ __OBJC_$_PROP_LIST_ROI
+ __OBJC_$_PROP_LIST_VDGDetectionUtilsV2
+ __OBJC_$_PROP_LIST_VSRNet
+ __OBJC_$_PROP_LIST_VideoDeghostingDetectionV2
+ __OBJC_$_PROP_LIST_boundingBoxForMerge
+ __OBJC_CLASS_PROTOCOLS_$_DVPLensFlareMitigationConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_DVPLensFlareMitigationParameters
+ __OBJC_CLASS_RO_$_DVPLensFlareMitigationConfiguration
+ __OBJC_CLASS_RO_$_DVPLensFlareMitigationParameters
+ __OBJC_CLASS_RO_$_DetectedROI
+ __OBJC_CLASS_RO_$_GGMController
+ __OBJC_CLASS_RO_$_GGMMetalToolBox
+ __OBJC_CLASS_RO_$_ISRNet
+ __OBJC_CLASS_RO_$_MaskToRoi
+ __OBJC_CLASS_RO_$_MitigationANE
+ __OBJC_CLASS_RO_$_PixelMemory
+ __OBJC_CLASS_RO_$_ROI
+ __OBJC_CLASS_RO_$_VDGDetectionUtilsV2
+ __OBJC_CLASS_RO_$_VDGProcessor
+ __OBJC_CLASS_RO_$_VEMobileAsset
+ __OBJC_CLASS_RO_$_VSRNet
+ __OBJC_CLASS_RO_$_VideoDeghostingDetectionV2
+ __OBJC_CLASS_RO_$_boundingBoxForMerge
+ __OBJC_METACLASS_RO_$_DVPLensFlareMitigationConfiguration
+ __OBJC_METACLASS_RO_$_DVPLensFlareMitigationParameters
+ __OBJC_METACLASS_RO_$_DetectedROI
+ __OBJC_METACLASS_RO_$_GGMController
+ __OBJC_METACLASS_RO_$_GGMMetalToolBox
+ __OBJC_METACLASS_RO_$_ISRNet
+ __OBJC_METACLASS_RO_$_MaskToRoi
+ __OBJC_METACLASS_RO_$_MitigationANE
+ __OBJC_METACLASS_RO_$_PixelMemory
+ __OBJC_METACLASS_RO_$_ROI
+ __OBJC_METACLASS_RO_$_VDGDetectionUtilsV2
+ __OBJC_METACLASS_RO_$_VDGProcessor
+ __OBJC_METACLASS_RO_$_VEMobileAsset
+ __OBJC_METACLASS_RO_$_VSRNet
+ __OBJC_METACLASS_RO_$_VideoDeghostingDetectionV2
+ __OBJC_METACLASS_RO_$_boundingBoxForMerge
+ ___146-[VideoDeghostingDetectionV2 process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:]_block_invoke
+ ___146-[VideoDeghostingDetectionV2 process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:]_block_invoke.40
+ ___248-[VideoDeghostingDetectionV2 repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:]_block_invoke
+ ___248-[VideoDeghostingDetectionV2 repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:]_block_invoke_2
+ ___50+[FRNet downloadMobileAssetWithCompletionHandler:]_block_invoke
+ ___52+[ImageSR downloadMobileAssetWithCompletionHandler:]_block_invoke
+ ___58+[GGMController downloadMobileAssetWithCompletionHandler:]_block_invoke
+ ___71+[VSRProcessor downloadMobileAssetWithInputType:withCompletionHandler:]_block_invoke
+ ___71+[VSRProcessor downloadMobileAssetWithInputType:withCompletionHandler:]_block_invoke_2
+ ___74+[DVPLensFlareMitigationConfiguration downloadAssetWithCompletionHandler:]_block_invoke
+ ___88+[VEMobileAsset downloadMobileAssetType:assetSpecifier:forClientName:completionHandler:]_block_invoke
+ ___88+[VEMobileAsset downloadMobileAssetType:assetSpecifier:forClientName:completionHandler:]_block_invoke.cold.1
+ ___88+[VEMobileAsset downloadMobileAssetType:assetSpecifier:forClientName:completionHandler:]_block_invoke.cold.2
+ ___block_descriptor_104_e8_32s40s48s56s64s72r_e5_v8?0ls32l8s40l8r72l8s48l8s56l8s64l8
+ ___block_descriptor_130_e8_32s40s48s56s64s72s80s88s96r104r112r_e5_v8?0lr96l8s32l8r104l8r112l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_40_e8_32bs_e20_v24?0q8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32bs_e76_v44?0"MAAutoAssetSelector"8B16"NSURL"20"MAAutoAssetStatus"28"NSError"36ls32l8
+ ___block_descriptor_88_e8_32s40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
+ ___block_descriptor_93_e8_32s40s48s56r_e5_v8?0ls32l8r56l8s40l8s48l8
+ ___copy_assignment_8_8_t0w8_s8_s16_s24_s32_s40_t48w8
+ ___copy_constructor_8_8_t0w8_s8_s16_s24_s32_s40_t48w8
+ ___destructor_8_s8_s16_s24_s32_s40
+ ___kCFBooleanTrue
+ _checkIfRepairWillGateFrame
+ _commitCommandBuffer
+ _convertPixBufToCIImageWithP3
+ _createSingleCachedTextureFromPixelBuffer
+ _drawColorRect
+ _drawRect
+ _e5rt_async_event_create
+ _e5rt_async_event_release
+ _e5rt_buffer_object_release
+ _e5rt_e5_compiler_compile
+ _e5rt_e5_compiler_create
+ _e5rt_e5_compiler_options_create
+ _e5rt_e5_compiler_options_release
+ _e5rt_e5_compiler_options_set_compute_device_types_mask
+ _e5rt_e5_compiler_options_set_force_recompilation
+ _e5rt_e5_compiler_release
+ _e5rt_execution_stream_create
+ _e5rt_execution_stream_encode_operation
+ _e5rt_execution_stream_execute_sync
+ _e5rt_execution_stream_operation_bind_completion_event
+ _e5rt_execution_stream_operation_bind_dependent_events
+ _e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options
+ _e5rt_execution_stream_operation_get_input_names
+ _e5rt_execution_stream_operation_get_num_inputs
+ _e5rt_execution_stream_operation_get_num_outputs
+ _e5rt_execution_stream_operation_get_output_names
+ _e5rt_execution_stream_operation_prepare_op_for_encode
+ _e5rt_execution_stream_operation_release
+ _e5rt_execution_stream_operation_retain_input_port
+ _e5rt_execution_stream_operation_retain_output_port
+ _e5rt_execution_stream_release
+ _e5rt_execution_stream_reset
+ _e5rt_io_port_bind_buffer_object
+ _e5rt_io_port_is_tensor
+ _e5rt_io_port_release
+ _e5rt_io_port_retain_surface_desc
+ _e5rt_io_port_retain_tensor_desc
+ _e5rt_precompiled_compute_op_create_options_create_with_program_function
+ _e5rt_precompiled_compute_op_create_options_release
+ _e5rt_program_function_release
+ _e5rt_program_library_get_function_metadata
+ _e5rt_program_library_get_function_names
+ _e5rt_program_library_get_num_functions
+ _e5rt_program_library_release
+ _e5rt_program_library_retain_program_function
+ _e5rt_surface_desc_get_height
+ _e5rt_surface_desc_get_width
+ _e5rt_tensor_desc_alloc_buffer_object
+ _e5rt_tensor_desc_release
+ _espresso_network_unbind_buffer
+ _freeLookAheadFrameArray
+ _getConfidenceOffline
+ _getMetalFormat
+ _getMetalFormat.cold.1
+ _getOpticalCenterMvShift
+ _getPortShape
+ _getPortShape.cold.1
+ _getPortShape.cold.2
+ _getPortShape.cold.3
+ _getPortShape.cold.4
+ _getPortShape.cold.5
+ _getPortShape.cold.6
+ _getPortShape.cold.7
+ _getRoiListWithTrackIdAndMvFromMetaContainer
+ _ggmCtrlCompletionCallback
+ _initLookAheadFrameArray
+ _isLowLightingCondition
+ _kCGImagePropertyOrientation
+ _kCIImageProperties
+ _kCVMetalTextureCacheMaximumTextureAgeKey
+ _kCVMetalTextureUsage
+ _kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey
+ _kCVPixelBufferMetalCompatibilityKey
+ _malloc_type_calloc
+ _memset
+ _mergeBboxesForMitigation
+ _mergeDetectedROI
+ _mergeDupBboxesForMitigation
+ _mergeRoiListWithTrackIdAndMvForMitigation
+ _mergeRoisInMetaContainer
+ _objc_copyStruct
+ _objc_enumerationMutation
+ _objc_msgSend$LSOrGGBbox
+ _objc_msgSend$LSTrackingMatched
+ _objc_msgSend$_cachedTexturesFromPixelBuffer:usage:
+ _objc_msgSend$_clampGhostROI:
+ _objc_msgSend$_compileShaders
+ _objc_msgSend$_copyImageTileFromPixelBuffer:mergeWithMask:outputTilePixelBuffer:commandBuffer:
+ _objc_msgSend$_copyImageTileFromPixelBuffer:outputImageTileTexture:commandBuffer:
+ _objc_msgSend$_getProbMapInput:reflLs:trackingRef:trackingRefProb:trackingRefSpaProb:trackingRefErrRescaleProb:trackingRefLs:inputBuf:reflLsBuf:trackingRefBuf:trackingRefProbBuf:trackingRefSpaProbBuf:trackingRefErrRescaleProbBuf:trackingRefLsBuf:trackingMvf:metaBuf:metaBufArray:trackingRefMetaBuf:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:refinedReflLs:probMapStash4FutureTracking:probMapBuf:errRescaleProbMapBuf:rawRefinedProbMapBuf:refinedProbMapBuf:refinedReflLsBuf:probMapStash4FutureTrackingBuf:doTracking:waitForComplete:
+ _objc_msgSend$_initDetection:futureFrames:outputImgBufTMinus1:outputImgBufTMinus2:
+ _objc_msgSend$_initParamsWithLowLight:
+ _objc_msgSend$_pasteRepairedTile:inputTileTexture:blendingMask:outputPixelBuffer:commandBuffer:
+ _objc_msgSend$_repair:outputBuf:ghostROI:inputROI:repairMask:blendMask:
+ _objc_msgSend$_resetIntermediateVariables
+ _objc_msgSend$absoluteString
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$allocateInputBufferObjects
+ _objc_msgSend$allocateOutputBufferObjects
+ _objc_msgSend$area
+ _objc_msgSend$array
+ _objc_msgSend$bbox
+ _objc_msgSend$bytePerPixel
+ _objc_msgSend$clusterIndicesOfRois:withExtendedRadius:roiCnt:imageRect:
+ _objc_msgSend$compileModelOnDevice
+ _objc_msgSend$contentsOfDirectoryAtPath:error:
+ _objc_msgSend$convertBuffer:toFP16IOSurface:
+ _objc_msgSend$convertBuffer:toFP16ShuffledIOSurface:
+ _objc_msgSend$convertFP16IOSurface:toBuffer:
+ _objc_msgSend$convertInternalBBoxes:outputArray:
+ _objc_msgSend$convertInternalBBoxesToROI:outputArray:
+ _objc_msgSend$countByEnumeratingWithState:objects:count:
+ _objc_msgSend$createFP16TextureFromIOSurface:width:height:arrayLength:
+ _objc_msgSend$createForwarpOutputBufferWidth:height:channels:
+ _objc_msgSend$createFunction
+ _objc_msgSend$currentStatusSync:
+ _objc_msgSend$cvMetalTextureCacheRef
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$defaultOpticalCenter
+ _objc_msgSend$descriptor
+ _objc_msgSend$dispatchThreads:threadsPerThreadgroup:
+ _objc_msgSend$dist2ghost
+ _objc_msgSend$dist2opticalCenter
+ _objc_msgSend$dlSpatialRepairYUV:output:repairMask:blendMask:inputTex:repairMaskTex:blendMaskTex:wRepairedY:wRepairedUV:metaBuf:
+ _objc_msgSend$doTrackingToNextFrameCurrMetaWithDetectionResults:currMetaWithMvToFuture:futureMeta:opticalCenter:futureOpticalCenter:futureFrameCnt:doLite:waitForComplete:
+ _objc_msgSend$downloadMobileAssetType:assetSpecifier:forClientName:completionHandler:
+ _objc_msgSend$downloadMobileAssetWithCompletionHandler:
+ _objc_msgSend$downloadProgress
+ _objc_msgSend$encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:
+ _objc_msgSend$encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:
+ _objc_msgSend$encodeBMSearch1RefToCommandEncoder:target:ref:reflect:normalizedTargetCenter:normalizedRefCenter:bestMatchLoc:meta:
+ _objc_msgSend$encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:
+ _objc_msgSend$encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:
+ _objc_msgSend$encodeBMTransferGrayToCommandEncoder:ref:warpedRef:bestMatchLoc:meta:sf:
+ _objc_msgSend$encodeBMTransferYUVToCommandEncoder:ref:reflect:normalizedCenter:warpedRef:bestMatchLoc:meta:sf:
+ _objc_msgSend$encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:
+ _objc_msgSend$encodeBilinearRescaleYUV:fullResInput:input:meta:blurBeforeSample:output:
+ _objc_msgSend$encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:
+ _objc_msgSend$encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:
+ _objc_msgSend$encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:
+ _objc_msgSend$encodeCollectClusterBgAvgToCommandEncoder:clusterMetaBuf:metaBuf:
+ _objc_msgSend$encodeCollectClusterMaxAndAvgLuma:clusterMetaBuf:metaBuf:
+ _objc_msgSend$encodeCollectClusterMaxProb:clusterMetaBuf:metaBuf:
+ _objc_msgSend$encodeCollectClusterMv:clusterMetaBuf:metaBuf:
+ _objc_msgSend$encodeCollectClusterMvForMotionCueToCommandEncoder:clusterMetaBuf:metaBuf:
+ _objc_msgSend$encodeCollectClusterOverlapWithRefs:clusterMetaBuf:metaBuf:
+ _objc_msgSend$encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:
+ _objc_msgSend$encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:
+ _objc_msgSend$encodeCollectMvToFuture:metaBuf:
+ _objc_msgSend$encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:
+ _objc_msgSend$encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:
+ _objc_msgSend$encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:
+ _objc_msgSend$encodeCopyCurrMetaForProcFuture:metaBuf:outMetaBuf:
+ _objc_msgSend$encodeCopyFullFrameMapToMap4RoiGenToCommandEncoder:input:output:
+ _objc_msgSend$encodeCopyMapToMap4RoiGenToCommandEncoder:input:output:metaBuf:
+ _objc_msgSend$encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:
+ _objc_msgSend$encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:
+ _objc_msgSend$encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:
+ _objc_msgSend$encodeDilateProbMap:input:output:hardDilationRadius:softDilationRadius:meta:
+ _objc_msgSend$encodeDilateReflLsMap:inputYUV:lsMap:dilatedLsMap:hardDilationRadius:softDilationRadius:meta:
+ _objc_msgSend$encodeForwarpYUVToCommandEncoder:input0:input1:meta:mvf0:mvf1:intermediateOutput0:intermediateOutput1:output0:output1:outputMap0:outputMap1:
+ _objc_msgSend$encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:
+ _objc_msgSend$encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:
+ _objc_msgSend$encodeGetBlobSaliency:inputYUV:blobSaliencyMap:meta:
+ _objc_msgSend$encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:
+ _objc_msgSend$encodeGetLsMapYUVToCommandEncoder:input:map:
+ _objc_msgSend$encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:
+ _objc_msgSend$encodeGetMvForMotionCueFromMvf:fullResInput:meta:mvf:opticalCenter:refOpticalCenter:
+ _objc_msgSend$encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:
+ _objc_msgSend$encodeGetMvToFutureFromMvf:fullResInput:meta:mvf:
+ _objc_msgSend$encodeGetOverlapWithRefs:input:probMap:metaBuf:
+ _objc_msgSend$encodeGetRoiMaxAndAvgLumaYUV:target:lsMap:meta:
+ _objc_msgSend$encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:
+ _objc_msgSend$encodeGetSaliencyMapToCommandEncoder:target:saliencyMap:meta:
+ _objc_msgSend$encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:
+ _objc_msgSend$encodePadRGBToCommandBuffer:source:destination:
+ _objc_msgSend$encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:
+ _objc_msgSend$encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:
+ _objc_msgSend$encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:
+ _objc_msgSend$encodeResetOutputToCommandEncoder:input:meta:output0:output1:
+ _objc_msgSend$encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:
+ _objc_msgSend$encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:
+ _objc_msgSend$encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:
+ _objc_msgSend$encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:
+ _objc_msgSend$encodeUpscaleThenReflectLsMap:input:normalizedCenter:output:
+ _objc_msgSend$encodeWarpBlendToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:
+ _objc_msgSend$encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:
+ _objc_msgSend$encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:
+ _objc_msgSend$encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:
+ _objc_msgSend$encodeWarpRefMetaLite:refMetaBuf:outMetaBuf:
+ _objc_msgSend$endAllLocksWithAssetType:assetSpecifier:forClientName:
+ _objc_msgSend$endAllPreviousLocksOfSelectorSync:forClientName:
+ _objc_msgSend$exchangeObjectAtIndex:withObjectAtIndex:
+ _objc_msgSend$executeSynchronouslyOperation:onStream:
+ _objc_msgSend$expectedTimeRemainingSecs
+ _objc_msgSend$extendBBox
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$generateDetectionRoiList:outputArray:
+ _objc_msgSend$generateMetaContainerArrayBufFromMetaContainerBuf:imageRect:
+ _objc_msgSend$generateTrajectoryForROI:isGG:
+ _objc_msgSend$getBBoxesUsingGraphTraversalFrom:pixValThreshold:bboxSizeThreshold:scaleFactor:roi:returnAsDetectedROI:outputArray:
+ _objc_msgSend$getClosestRoi:forCoord:
+ _objc_msgSend$getCommandqueue
+ _objc_msgSend$getDetectionRoiListFromMeta:outputArray:
+ _objc_msgSend$getDevice
+ _objc_msgSend$getFlowTarget:ref:targetBuf:refBuf:mvf:backwardMvf:metaBuf:skipRescaling:
+ _objc_msgSend$getInputPortNames
+ _objc_msgSend$getLSBBoxesUsingGraphTraversalFrom:roi:pixValThreshold:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:
+ _objc_msgSend$getLocalMobileAssetURLWithAssetType:assetSpecifier:forClientName:
+ _objc_msgSend$getLocationMatchCostWith:
+ _objc_msgSend$getMobileAssetStatusWithAssetType:assetSpecifier:forClientName:percentCompleted:
+ _objc_msgSend$getMobileAssetStatusWithPercentCompleted:
+ _objc_msgSend$getOutputPortNames
+ _objc_msgSend$getProbMapsTarget:ref:rawProbMap:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:reflLsMap:refinedReflLsMap:reflLsMap4TrackingRef:metaBuf:metaBufArray:trackingMvf:useRefProbMap:opticalCenter:trackingRefOpticalCenter:waitForComplete:
+ _objc_msgSend$getReflLsListFromMeta:outputArray:
+ _objc_msgSend$getReflectedBboxAroundCenter:
+ _objc_msgSend$getRoiMvForRoiList:fromMeta:
+ _objc_msgSend$getSearchLocation:
+ _objc_msgSend$getTopLSInListByKeepingTops:k:dist2ghostTol:
+ _objc_msgSend$getTrajectoryMatchingCostGG:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$imageByCompositingOverImage:
+ _objc_msgSend$imageByCroppingToRect:
+ _objc_msgSend$imageWithColor:
+ _objc_msgSend$index2RoiArray
+ _objc_msgSend$initContextWithFilePath:engine:configuration:usePreCompiled:
+ _objc_msgSend$initForAssetType:withAssetSpecifier:
+ _objc_msgSend$initForClientName:selectingAsset:error:
+ _objc_msgSend$initWithBbox:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$initWithCvPixelBuffer:
+ _objc_msgSend$initWithCvPixelBuffer:skipClamp:readOnly:
+ _objc_msgSend$initWithFrameWidth:FrameHeight:usePrecomputedFlow:
+ _objc_msgSend$initWithMetalContext:commandQueue:
+ _objc_msgSend$initWithMetalContext:commandQueue:imageDimensions:netSize:metalToolBox:
+ _objc_msgSend$initWithMetalContext:commandQueue:tuningParamDict:
+ _objc_msgSend$initWithMetalToolBox:
+ _objc_msgSend$initWithMetalToolBox:config:imageDimensions:
+ _objc_msgSend$initWithMetalToolBox:configuration:tuningParams:
+ _objc_msgSend$initWithModelPath:inputWidth:inputHeight:
+ _objc_msgSend$initWithRed:green:blue:
+ _objc_msgSend$initWithTrackingSessionId:roiId:andRoi:
+ _objc_msgSend$initWithTrackingSessionId:roiId:roi:LSRoi:descriptor:propertiesForPostProcPipeVisualization:
+ _objc_msgSend$initWithTrackingSessionId:roiId:roi:trackId:
+ _objc_msgSend$initializeInputPorts
+ _objc_msgSend$initializeModel
+ _objc_msgSend$isBoxSizeValidForProcessing:AndErodeBy:
+ _objc_msgSend$isPredictedFromPast
+ _objc_msgSend$isReflectedLS
+ _objc_msgSend$isTracked
+ _objc_msgSend$isTrajectoryPruningPassed
+ _objc_msgSend$kpIsFromHW
+ _objc_msgSend$loadModelFromPath:
+ _objc_msgSend$lockContent:withUsagePolicy:withTimeout:completion:
+ _objc_msgSend$lockContentSync:withTimeout:lockedAssetSelector:newerInProgress:error:
+ _objc_msgSend$lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:
+ _objc_msgSend$lowSaliencyCnt
+ _objc_msgSend$matchedLS
+ _objc_msgSend$maxTotalThreadsPerThreadgroup
+ _objc_msgSend$msrFrameSource:destination:waitForCompletion:
+ _objc_msgSend$mv
+ _objc_msgSend$mvCnt
+ _objc_msgSend$mvSum
+ _objc_msgSend$newBufferWithBytesNoCopy:length:options:deallocator:
+ _objc_msgSend$nextFrameOpticalCenter
+ _objc_msgSend$normalization
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$operation
+ _objc_msgSend$opticalCenterShift
+ _objc_msgSend$outputBufferObject
+ _objc_msgSend$outputSurface
+ _objc_msgSend$output_port
+ _objc_msgSend$pMemory
+ _objc_msgSend$padRGB:to:
+ _objc_msgSend$path
+ _objc_msgSend$predictPrevLSLocation:usingPrevToCurrentHomography:
+ _objc_msgSend$predictedFromPastCnt
+ _objc_msgSend$prepareToProcess:
+ _objc_msgSend$previousPreviousOutputFrame
+ _objc_msgSend$process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:
+ _objc_msgSend$process:outputBuf:roi:repairMask:blendMask:wRepairedY:wRepairedUV:
+ _objc_msgSend$processHwLsMaskAndGetRoisOpticalCenter:inputFrame:prevMetaContainer:considerDist2PrevGhostWhenSort:outputMask:outputMaskTexture:isLowLight:outputArray:
+ _objc_msgSend$processHwLsMaskNormalizedCenter:input:output:waitForComplete:
+ _objc_msgSend$processSourceFrame:nextFrame:forwardFlow:backwardFlow:ourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:randomAccessMode:destinationFrame:
+ _objc_msgSend$processSuperResolutionInputBuffer:outputBuffer:
+ _objc_msgSend$processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:
+ _objc_msgSend$pruneGhostList:againstReflLsList:dilation:
+ _objc_msgSend$purgeResources
+ _objc_msgSend$readFourChannelAtX:Y:
+ _objc_msgSend$readOneChannelAtX:Y:Channel:
+ _objc_msgSend$reflectAroundCenter:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeObject:
+ _objc_msgSend$removeObjectAtIndex:
+ _objc_msgSend$removeObjectsInArray:
+ _objc_msgSend$repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:
+ _objc_msgSend$reset
+ _objc_msgSend$resetIntermediateVariables
+ _objc_msgSend$resetStream:
+ _objc_msgSend$resizeImageCmdBuf:inputTexture:withFactorX:withFactorY:outputTexture:
+ _objc_msgSend$resourceOptions
+ _objc_msgSend$roi
+ _objc_msgSend$roiMv
+ _objc_msgSend$setArea:
+ _objc_msgSend$setBbox:
+ _objc_msgSend$setCompressionFootprint:
+ _objc_msgSend$setCompressionMode:
+ _objc_msgSend$setConfidence:
+ _objc_msgSend$setDefaultControllerConfig
+ _objc_msgSend$setDefaultOpticalCenter:
+ _objc_msgSend$setDescriptor:
+ _objc_msgSend$setDifferenceOfGaussianAndLumaFeature:
+ _objc_msgSend$setDifferenceOfGaussianAndLumaFeaturePredictedLocation:
+ _objc_msgSend$setDifferenceOfGaussianAndLumaFeatureReflection:
+ _objc_msgSend$setDist2ghost:
+ _objc_msgSend$setDist2opticalCenter:
+ _objc_msgSend$setExtendBBox:
+ _objc_msgSend$setImageblockWidth:height:
+ _objc_msgSend$setIndex2RoiArray:
+ _objc_msgSend$setIsPredictedFromPast:
+ _objc_msgSend$setIsTracked:
+ _objc_msgSend$setIsTrajectoryPruningPassed:
+ _objc_msgSend$setLSIsHighRisk:
+ _objc_msgSend$setLSTrackID:
+ _objc_msgSend$setLSTrackingMatched:
+ _objc_msgSend$setLabel:
+ _objc_msgSend$setLumaFeatureVector:
+ _objc_msgSend$setLumaFeatureVectorPredictedLocation:
+ _objc_msgSend$setLumaFeatureVectorReflection:
+ _objc_msgSend$setMatchedLS:
+ _objc_msgSend$setMv:
+ _objc_msgSend$setMvCnt:
+ _objc_msgSend$setMvSum:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setPredictedFromPastCnt:
+ _objc_msgSend$setRepairTuningParams:
+ _objc_msgSend$setResourceOptions:
+ _objc_msgSend$setRoi:
+ _objc_msgSend$setRoiMv:
+ _objc_msgSend$setRoiMvForMeta:fromRoiList:
+ _objc_msgSend$setScaleTransform:
+ _objc_msgSend$setTemporalDetectionMatched:
+ _objc_msgSend$setTrackID:
+ _objc_msgSend$setTrackedCnt:
+ _objc_msgSend$setUserInitiated:
+ _objc_msgSend$setup
+ _objc_msgSend$sortLsList:
+ _objc_msgSend$sortedArrayUsingSelector:
+ _objc_msgSend$sourceFrameOpticalCenter
+ _objc_msgSend$startSessionWithQualityMode:error:
+ _objc_msgSend$stream
+ _objc_msgSend$stride
+ _objc_msgSend$stringByAppendingPathComponent:
+ _objc_msgSend$stringWithCString:encoding:
+ _objc_msgSend$summary
+ _objc_msgSend$temporalDetectionMatched
+ _objc_msgSend$threadExecutionWidth
+ _objc_msgSend$totalExpectedBytes
+ _objc_msgSend$totalWrittenBytes
+ _objc_msgSend$trackID
+ _objc_msgSend$trackMeta:refMeta:currMaxTrackId:
+ _objc_msgSend$trackedCnt
+ _objc_msgSend$unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:outputFutureFrameCnt:outputMTLBuffer:
+ _objc_msgSend$updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:opticalCenterShift:
+ _objc_msgSend$updateRepairedRefYUVInput:opticalCenter:prob:errRescaleProb:prevProb:refinedProb:probMap4TrRefW:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:inputBuf:probBuf:errRescaleProbBuf:prevProbBuf:refinedProbBuf:probMap4TrRefWBuf:frRef0Buf:frRef1Buf:nextFrameBuf:metaBuf:metaBufArray:forceToSpatial:waitForComplete:
+ _objc_msgSend$warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toHighResBufferTexture:
+ _objc_msgSend$warpRoisUsingMv:
+ _objc_msgSend$warpTrackingRefProbMap:refSpaProbMap:refReflLs:mvf:metaBuf:metaBufArray:waitForComplete:
+ _objc_opt_isKindOfClass
+ _objc_setProperty_atomic
+ _qsortComparatorFloat
+ _reflectPointSimd
+ _resetVGGM_ExternalConfig
+ _setDefaultConfig
+ _setMetaContainerUsingRoiListWithTrackIdAndMv
+ _shouldRankLS1OverLS2
+ _visualiseBoundingBoxes
- -[DVPSuperResolutionParameters initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:destinationFrame:]
- -[FRNet bicubicOnly]
- -[FRNet convertToYUV:attachment:]
- -[FRNet convertToYUV:attachment:].cold.1
- -[FRNet residueOnlyFillValue]
- -[FRNet residueOnly]
- -[FRNet setBicubicOnly:]
- -[FRNet setResidueOnly:]
- -[FRNet setResidueOnlyFillValue:]
- -[SRNet bindBuffer:forBlob:]
- -[SRNet initWithUsage:espressoFileName:useMPS:]
- -[SRNet scaleLowResolutionFrame:withPrevHighResolutionFrame:to:callback:]
- -[SRNet scaleLowResolutionFrame:withPrevHighResolutionFrame:to:callback:].cold.1
- -[SRNet scaleLowResolutionFrame:withPrevHighResolutionFrame:to:callback:].cold.2
- -[SRNet scaleLowResolutionFrame:withPrevHighResolutionFrame:to:callback:].cold.3
- -[SRNet setUseMPS:]
- -[SRNet useMPS]
- -[VEEspressoModel initMPSWithModelName:usage:]
- -[Warper encodeWarpBlendWithSpaceToDepthToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:]
- -[Warper encodeWarpBlendWithSpaceToDepthToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:].cold.1
- -[Warper encodeWarpBlendWithSpaceToDepthToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:].cold.2
- -[Warper warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toShuffledBufferTexture:]
- GCC_except_table25
- _OBJC_IVAR_$_FRNet._bicubicOnly
- _OBJC_IVAR_$_FRNet._espressoFileName
- _OBJC_IVAR_$_FRNet._highResolutionRGBABufferPool
- _OBJC_IVAR_$_FRNet._outputSR
- _OBJC_IVAR_$_FRNet._residueOnly
- _OBJC_IVAR_$_FRNet._residueOnlyFillValue
- _OBJC_IVAR_$_ImageSR._espressoFileName
- _OBJC_IVAR_$_SRNet._useMPS
- _OBJC_IVAR_$_Warper._warpBlendWith4x4ShuffleRGBKernel
- ___73-[SRNet scaleLowResolutionFrame:withPrevHighResolutionFrame:to:callback:]_block_invoke
- ___block_descriptor_32_e15_v16?0^{?=ii*}8l
- _adjustColorAndSpatialKey.cold.1
- _objc_msgSend$bindBuffer:forBlob:
- _objc_msgSend$convertToYUV:attachment:
- _objc_msgSend$denormalizeRGB:to:
- _objc_msgSend$encodeWarpBlendWithSpaceToDepthToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:
- _objc_msgSend$initWithUsage:espressoFileName:useMPS:
- _objc_msgSend$normalizeRGB:to:
- _objc_msgSend$scaleLowResolutionFrame:withPrevHighResolutionFrame:to:callback:
- _objc_msgSend$warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toShuffledBufferTexture:
CStrings:
+ " format: %c%c%c%c can't be supported"
+ "# of ROI(s) to repair: %d"
+ "%d"
+ "%s"
+ "%s : Invaild alignedRef0 texture"
+ "%s : Invaild alignedRef1 texture"
+ "%s : Invaild backwarpFlow0 texture"
+ "%s : Invaild backwarpFlow1 texture"
+ "%s : Invaild bestMatchLoc texture"
+ "%s : Invaild blobSaliency texture"
+ "%s : Invaild blobSaliencyMap texture"
+ "%s : Invaild bmMvf0 texture"
+ "%s : Invaild bmMvf1 texture"
+ "%s : Invaild bmRef0 texture"
+ "%s : Invaild bmRef1 texture"
+ "%s : Invaild clusterMetaBuf buffer"
+ "%s : Invaild clusterMetaBuf texture"
+ "%s : Invaild dilatedLsMap texture"
+ "%s : Invaild dilatedProbMap texture"
+ "%s : Invaild dilatedRef texture"
+ "%s : Invaild dlSpatialMitTexture texture"
+ "%s : Invaild errRescaleProbMap texture"
+ "%s : Invaild flow0 texture"
+ "%s : Invaild flow1 texture"
+ "%s : Invaild forwarpHoleMap0 texture"
+ "%s : Invaild forwarpHoleMap1 texture"
+ "%s : Invaild frRef0 texture"
+ "%s : Invaild frRef1 texture"
+ "%s : Invaild fullResInput texture"
+ "%s : Invaild fullResTarget texture"
+ "%s : Invaild hmgrphyRef0 texture"
+ "%s : Invaild hmgrphyRef1 texture"
+ "%s : Invaild hrTarget texture"
+ "%s : Invaild input texture"
+ "%s : Invaild input0 texture"
+ "%s : Invaild input1 buffer"
+ "%s : Invaild input1 texture"
+ "%s : Invaild inputBuffer0 texture"
+ "%s : Invaild inputBuffer1 texture"
+ "%s : Invaild inputCopy texture"
+ "%s : Invaild inputFrame texture"
+ "%s : Invaild inputMap0 texture"
+ "%s : Invaild inputMap1 texture"
+ "%s : Invaild inputTexture texture"
+ "%s : Invaild inputYUV texture"
+ "%s : Invaild lsCheckOutmetaBuf buffer"
+ "%s : Invaild lsMap texture"
+ "%s : Invaild map texture"
+ "%s : Invaild meta buffer"
+ "%s : Invaild meta texture"
+ "%s : Invaild metaBuf buffer"
+ "%s : Invaild metaBuf texture"
+ "%s : Invaild motion texture"
+ "%s : Invaild motionMap texture"
+ "%s : Invaild mvf texture"
+ "%s : Invaild mvf0 texture"
+ "%s : Invaild mvf1 texture"
+ "%s : Invaild mvf2 texture"
+ "%s : Invaild outMetaBuf buffer"
+ "%s : Invaild outMetaBuf texture"
+ "%s : Invaild outMvf texture"
+ "%s : Invaild outMvf0 texture"
+ "%s : Invaild outMvf1 texture"
+ "%s : Invaild output texture"
+ "%s : Invaild output0 texture"
+ "%s : Invaild output1 texture"
+ "%s : Invaild outputBuffer0 texture"
+ "%s : Invaild outputBuffer1 texture"
+ "%s : Invaild outputMap0 texture"
+ "%s : Invaild outputMap1 texture"
+ "%s : Invaild outputTexture texture"
+ "%s : Invaild prevProbMap texture"
+ "%s : Invaild probMap texture"
+ "%s : Invaild probMap4Spatial texture"
+ "%s : Invaild probMap4TradSpatialTexture texture"
+ "%s : Invaild probMapTexture texture"
+ "%s : Invaild redoTrackingOutmetaBuf buffer"
+ "%s : Invaild ref texture"
+ "%s : Invaild ref0 texture"
+ "%s : Invaild ref1 texture"
+ "%s : Invaild refLsMap texture"
+ "%s : Invaild refMetaBuf buffer"
+ "%s : Invaild refMetaBuf texture"
+ "%s : Invaild refOutput texture"
+ "%s : Invaild refinedProbMap texture"
+ "%s : Invaild reflHwMap texture"
+ "%s : Invaild reflLsMap texture"
+ "%s : Invaild saliency texture"
+ "%s : Invaild saliencyMap texture"
+ "%s : Invaild spaOutput texture"
+ "%s : Invaild spaRef texture"
+ "%s : Invaild spatialMitTexture texture"
+ "%s : Invaild spatialOutput texture"
+ "%s : Invaild target texture"
+ "%s : Invaild targetFrameYUV texture"
+ "%s : Invaild temporalMitTexture texture"
+ "%s : Invaild temporalOutput texture"
+ "%s : Invaild tradSpatialMitTexture texture"
+ "%s : Invaild upscaledProbMap texture"
+ "%s : Invaild upscaledRefinedProbMap texture"
+ "%s : Invaild warpedRef texture"
+ "%s : Invaild warpedRef0 texture"
+ "%s : Invaild warpedRef1 texture"
+ "%s : Invaild warpedRefReflHwMap texture"
+ "%s : Invaild warpedReflRef texture"
+ "%s : filter initialization fail"
+ "%s : hardDilationOutput output texture"
+ "%s.espresso.net"
+ "%s: Invaild array roiList"
+ "%zux%zu"
+ "*"
+ "*16@0:8"
+ "-[GGMMetalToolBox encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:]"
+ "-[GGMMetalToolBox encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:]"
+ "-[GGMMetalToolBox encodeBMSearch1RefToCommandEncoder:target:ref:reflect:normalizedTargetCenter:normalizedRefCenter:bestMatchLoc:meta:]"
+ "-[GGMMetalToolBox encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:]"
+ "-[GGMMetalToolBox encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:]"
+ "-[GGMMetalToolBox encodeBMTransferGrayToCommandEncoder:ref:warpedRef:bestMatchLoc:meta:sf:]"
+ "-[GGMMetalToolBox encodeBMTransferYUVToCommandEncoder:ref:reflect:normalizedCenter:warpedRef:bestMatchLoc:meta:sf:]"
+ "-[GGMMetalToolBox encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:]"
+ "-[GGMMetalToolBox encodeBilinearRescaleYUV:fullResInput:input:meta:blurBeforeSample:output:]"
+ "-[GGMMetalToolBox encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:]"
+ "-[GGMMetalToolBox encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:]"
+ "-[GGMMetalToolBox encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:]"
+ "-[GGMMetalToolBox encodeCollectClusterBgAvgToCommandEncoder:clusterMetaBuf:metaBuf:]"
+ "-[GGMMetalToolBox encodeCollectClusterMaxAndAvgLuma:clusterMetaBuf:metaBuf:]"
+ "-[GGMMetalToolBox encodeCollectClusterMaxProb:clusterMetaBuf:metaBuf:]"
+ "-[GGMMetalToolBox encodeCollectClusterMv:clusterMetaBuf:metaBuf:]"
+ "-[GGMMetalToolBox encodeCollectClusterMvForMotionCueToCommandEncoder:clusterMetaBuf:metaBuf:]"
+ "-[GGMMetalToolBox encodeCollectClusterOverlapWithRefs:clusterMetaBuf:metaBuf:]"
+ "-[GGMMetalToolBox encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:]"
+ "-[GGMMetalToolBox encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:]"
+ "-[GGMMetalToolBox encodeCollectMvToFuture:metaBuf:]"
+ "-[GGMMetalToolBox encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:]"
+ "-[GGMMetalToolBox encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:]"
+ "-[GGMMetalToolBox encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:]"
+ "-[GGMMetalToolBox encodeCopyCurrMetaForProcFuture:metaBuf:outMetaBuf:]"
+ "-[GGMMetalToolBox encodeCopyFullFrameMapToMap4RoiGenToCommandEncoder:input:output:]"
+ "-[GGMMetalToolBox encodeCopyMapToMap4RoiGenToCommandEncoder:input:output:metaBuf:]"
+ "-[GGMMetalToolBox encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:]"
+ "-[GGMMetalToolBox encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:]"
+ "-[GGMMetalToolBox encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:]"
+ "-[GGMMetalToolBox encodeDilateProbMap:input:output:hardDilationRadius:softDilationRadius:meta:]"
+ "-[GGMMetalToolBox encodeDilateReflLsMap:inputYUV:lsMap:dilatedLsMap:hardDilationRadius:softDilationRadius:meta:]"
+ "-[GGMMetalToolBox encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:]"
+ "-[GGMMetalToolBox encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:]"
+ "-[GGMMetalToolBox encodeGetBlobSaliency:inputYUV:blobSaliencyMap:meta:]"
+ "-[GGMMetalToolBox encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:]"
+ "-[GGMMetalToolBox encodeGetLsMapYUVToCommandEncoder:input:map:]"
+ "-[GGMMetalToolBox encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:]"
+ "-[GGMMetalToolBox encodeGetMvForMotionCueFromMvf:fullResInput:meta:mvf:opticalCenter:refOpticalCenter:]"
+ "-[GGMMetalToolBox encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:]"
+ "-[GGMMetalToolBox encodeGetMvToFutureFromMvf:fullResInput:meta:mvf:]"
+ "-[GGMMetalToolBox encodeGetOverlapWithRefs:input:probMap:metaBuf:]"
+ "-[GGMMetalToolBox encodeGetRoiMaxAndAvgLumaYUV:target:lsMap:meta:]"
+ "-[GGMMetalToolBox encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:]"
+ "-[GGMMetalToolBox encodeGetSaliencyMapToCommandEncoder:target:saliencyMap:meta:]"
+ "-[GGMMetalToolBox encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:]"
+ "-[GGMMetalToolBox encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:]"
+ "-[GGMMetalToolBox encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:]"
+ "-[GGMMetalToolBox encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:]"
+ "-[GGMMetalToolBox encodeResetOutputToCommandEncoder:input:meta:output0:output1:]"
+ "-[GGMMetalToolBox encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:]"
+ "-[GGMMetalToolBox encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:]"
+ "-[GGMMetalToolBox encodeSyncWeightsOriginal:clusterMetaBuf:metaBuf:]"
+ "-[GGMMetalToolBox encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:]"
+ "-[GGMMetalToolBox encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:]"
+ "-[GGMMetalToolBox encodeUpscaleThenReflectLsMap:input:normalizedCenter:output:]"
+ "-[GGMMetalToolBox encodeVisualizeMvfToCommandEncoder:fullResTarget:mvf:outMvf:meta:]"
+ "-[GGMMetalToolBox encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:]"
+ "-[GGMMetalToolBox encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:]"
+ "-[GGMMetalToolBox encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:]"
+ "-[GGMMetalToolBox encodeWarpRefMetaLite:refMetaBuf:outMetaBuf:]"
+ "-[GGMMetalToolBox resizeImageCmdBuf:inputTexture:withFactorX:withFactorY:outputTexture:]"
+ "-[MaskToRoi getBBoxesUsingGraphTraversalFrom:pixValThreshold:bboxSizeThreshold:scaleFactor:roi:returnAsDetectedROI:outputArray:]"
+ "-[VDGDetectionUtilsV2 getDetectionRoiListFromMeta:outputArray:]"
+ "-[VDGDetectionUtilsV2 getReflLsListFromMeta:outputArray:]"
+ "16@0:8"
+ "24@0:816"
+ "24@0:8@16"
+ "24@0:8f16f20"
+ "24@0:8i16i20"
+ "72@0:8@16{?=[3]}24"
+ "@\"GGMController\""
+ "@\"GGMMetalToolBox\""
+ "@\"ISRNet\""
+ "@\"MaskToRoi\""
+ "@\"MitigationANE\""
+ "@\"NSMutableArray\""
+ "@\"ROI\""
+ "@\"VDGDetectionUtilsV2\""
+ "@\"VSRNet\""
+ "@\"VideoDeghostingDetectionV2\""
+ "@100@0:8Q16q24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGRect={CGPoint=dd}{CGSize=dd}}64f96"
+ "@112@0:8@16@24@32{CGPoint=dd}40{CGPoint=dd}56d72@80@88q96@104"
+ "@192@0:816{?=fffffI}32"
+ "@24@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16"
+ "@24@0:8^{__CVBuffer=}16"
+ "@264@0:8Q16q24{CGRect={CGPoint=dd}{CGSize=dd}}32{CGRect={CGPoint=dd}{CGSize=dd}}64{?=fffffI}96^{?=iBBiiiBB}256"
+ "@32@0:816"
+ "@32@0:8^{__CVBuffer=}16B24B28"
+ "@32@0:8^{__CVBuffer=}16Q24"
+ "@36@0:8@16@24f32"
+ "@36@0:8@16q24B32"
+ "@40@0:8@16@24{?=ii}32"
+ "@40@0:8@16Q24Q32"
+ "@40@0:8@16^{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}}24^{?=iiiiiifffiifiiii{?=ffffffff}{?=iiffffffffffffff}{?=fff}}32"
+ "@40@0:8@16^{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}}24{?=ii}32"
+ "@40@0:8f16f20[4f]24i32i36"
+ "@48@0:8^{__IOSurface=}16q24q32q40"
+ "@52@0:8@16@24{?=ii}32i40@44"
+ "@64@0:8Q16q24{CGRect={CGPoint=dd}{CGSize=dd}}32"
+ "@64@0:8^{?=ffffffff}16f24s28{CGRect={CGPoint=dd}{CGSize=dd}}32"
+ "@68@0:8Q16q24{CGRect={CGPoint=dd}{CGSize=dd}}32i64"
+ "After pruning w/ trajectory: ROI# %u"
+ "B116@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40{CGPoint=dd}48{CGPoint=dd}64d80^{__CVBuffer=}88^{__CVBuffer=}96B104^{__CVBuffer=}108"
+ "B24@0:8^{?=@@@@@@@@@@@@@@iiiiiiii}16"
+ "B32@0:8^{__CVBuffer=}16^{__IOSurface=}24"
+ "B32@0:8^{__IOSurface=}16^{__CVBuffer=}24"
+ "B32@0:8^{e5rt_execution_stream_operation=}16^{e5rt_execution_stream=}24"
+ "B32@0:8q16^@24"
+ "B36@0:816f32"
+ "B36@0:8^{__CVBuffer=}16^{__CVBuffer=}24B32"
+ "B40@0:8^{CGPoint=dd}16Q24^d32"
+ "B40@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32"
+ "B52@0:8162432f40f44B48"
+ "B68@0:8^{__CVBuffer=}16^{?=^{?}ii}243240f48^{__CVBuffer=}52^{__CVBuffer=}60"
+ "Before pruning w/ trajectory: ROI# %u"
+ "C"
+ "C16@0:8"
+ "C28@0:8f16f20c24"
+ "C28@0:8i16i20c24"
+ "Called"
+ "Clamping ghost height from: %f to: %d"
+ "Clamping ghost width from: %f to: %d"
+ "Concurrent Task Queue"
+ "Configuration: input dimensions:            %d x %d"
+ "Configuration: lookaheadFrames array size:    %d"
+ "Could not init GGMController"
+ "DVPLensFlareMitigationConfiguration"
+ "DVPLensFlareMitigationParameters"
+ "Detected ROI count exceeds the limit of %d. Some ROIs are not packed to repair"
+ "DetectedROI"
+ "Error missing _forwardFlow"
+ "Error missing backwardFlow"
+ "Error: Invalid DVPLensFlareMitigationConfiguration revision %d"
+ "Error: Number of input ports incorrect\n"
+ "Error: Number of output ports incorrect\n"
+ "Error: format is not supported "
+ "Excecution failed. returned error = %u. msg = %s\n"
+ "Fail to to initialize: Mismatch between source, next frame's pixel formats"
+ "Failed to obtain input info\n"
+ "Failed to obtain output info\n"
+ "Function names:"
+ "GGM Controller already initialized"
+ "GGMController"
+ "GGMMetalToolBox"
+ "Ghost cnt (before merge) exceeds hard gating threshold. All ghosts are discarded"
+ "Ghost cnt (before merge) exceeds soft gating threshold. Only keeping top %d ghosts"
+ "ISRNet"
+ "Initializing model with path: %@"
+ "Input [%@]: %ld x %ld x %ld"
+ "Input0 [%@]: %ld x %ld x %ld"
+ "Input1 [%@]: %ld x %ld x %ld"
+ "LSIsHighRisk"
+ "LSOrGGBbox"
+ "LSRoi"
+ "LSTrackID"
+ "LSTrackingMatched"
+ "LSTrackingVote"
+ "Library metadata %@"
+ "MaskToRoi"
+ "Metal tool box shaders compilation failed"
+ "MitigationANE"
+ "MobileAssetStatus is not ready! ISRSuperResolutionConfigurationMobileAssetStatus: %ld"
+ "MobileAssetStatus is not ready! VSRSuperResolutionConfigurationMobileAssetStatus: %ld"
+ "No boxes to updates DoG and luma features"
+ "No prev LS boxes to updates DoG and luma features"
+ "Orientation"
+ "Output [%@]: %ld x %ld x %ld"
+ "Pixel buffer %c%c%c%c format not supported"
+ "PixelMemory"
+ "ROI"
+ "ROI to repair: (%f, %f), (%f, %f)"
+ "Repair network (%@) is not on the filesystem"
+ "SampleFourChannelAtX:Y:"
+ "T*,N,V_pMemory"
+ "T*,N,V_pMemoryPlane2"
+ "T,V_LSOrGGBbox"
+ "T,V_bbox"
+ "T,V_defaultOpticalCenter"
+ "T,V_differenceOfGaussianAndLumaFeature"
+ "T,V_differenceOfGaussianAndLumaFeaturePredictedLocation"
+ "T,V_differenceOfGaussianAndLumaFeatureReflection"
+ "T,V_lumaFeatureVector"
+ "T,V_lumaFeatureVectorPredictedLocation"
+ "T,V_lumaFeatureVectorReflection"
+ "T,V_mv"
+ "T,V_mvSum"
+ "T,V_nextVisedOpticalCenter"
+ "T,V_roiMv"
+ "T,V_trajectoryFromPast"
+ "T,V_visedOpticalCenter"
+ "T@\"DVPFrame\",R,N,V_previousPreviousOutputFrame"
+ "T@\"NSArray\",&,N,V_futureInputParamsToRepair"
+ "T@\"NSDictionary\",&,N,V_detectedGreenGhostInfo"
+ "T@\"NSDictionary\",&,N,V_inputParamsToRepair"
+ "T@\"NSDictionary\",&,N,V_metaDictionary"
+ "T@\"NSDictionary\",R,N,V_tuningParamDict"
+ "T@\"NSMutableArray\",&,V_matchedLS"
+ "T@\"NSMutableArray\",&,V_trackIDsAfterMerge"
+ "T@\"NSString\",&,N,V_modelPath"
+ "T@\"NSString\",&,N,V_outputPortName"
+ "T@\"NSString\",&,V_LSTrackID"
+ "T@\"OFNormalization\",&,N,V_normalization"
+ "T@\"ROI\",&,V_LSTrackingMatched"
+ "T@\"ROI\",&,V_temporalDetectionMatched"
+ "TB,N,V_skipClamp"
+ "TB,V_LSIsHighRisk"
+ "TB,V_doneKPToBBoxViaGraphTraversal"
+ "TB,V_isPredictedFromPast"
+ "TB,V_isReflectedLS"
+ "TB,V_isTracked"
+ "TB,V_isTrajectoryPruningPassed"
+ "TB,V_kpIsFromHW"
+ "TB,V_lsHasBeenUsedForTrackingGhost"
+ "TB,V_prevShouldRunGGDetectionClippedPixelBased"
+ "TB,V_prevShouldRunGGDetectionLSBased"
+ "TB,V_prevShouldRunGGDetectionLuxLevelBased"
+ "TB,V_trackFail"
+ "TC,N,V_channels"
+ "TI,N,V_format"
+ "TQ,N,V_inputHeight"
+ "TQ,N,V_inputWidth"
+ "TQ,R,N,V_trackSessionId"
+ "T^{?=^{?}ii},N,V_futureFramesToDetectionAndRepair"
+ "T^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f},V_metaContainer"
+ "T^{__CVBuffer=},N,V_buf"
+ "T^{__CVBuffer=},N,V_inputBuffer"
+ "T^{__CVBuffer=},N,V_keyPointsList"
+ "T^{__CVBuffer=},N,V_lightSourceMask"
+ "T^{__CVBuffer=},R,N,V_processedPixelBuffer"
+ "T^{__CVBuffer=},V_integralSumPixelBuffer"
+ "T^{__CVMetalTextureCache=},R,N,V_cvMetalTextureCacheRef"
+ "T^{__IOSurface=},N,V_inputSurface"
+ "T^{__IOSurface=},N,V_outputSurface"
+ "T^{__IOSurface=},N,V_prevHRSurface"
+ "T^{e5rt_buffer_object=},R,N,V_outputBufferObject"
+ "T^{e5rt_execution_stream=},R,N,V_stream"
+ "T^{e5rt_execution_stream_operation=},R,N,V_operation"
+ "T^{e5rt_io_port=},R,N,V_output_port"
+ "T^{e5rt_program_function=},R,N,V_function"
+ "T^{e5rt_program_library=},R,N,V_library"
+ "Td,R,N,V_opticalCenterShift"
+ "Tf,N,V_confidence"
+ "Tf,V_area"
+ "Tf,V_dist2ghost"
+ "Tf,V_dist2opticalCenter"
+ "Tf,V_mvCnt"
+ "Tf,V_opticalCenterMvShift"
+ "Ti,N,V_bytePerPixel"
+ "Ti,N,V_height"
+ "Ti,N,V_stride"
+ "Ti,N,V_stridePlane2"
+ "Ti,N,V_width"
+ "Ti,V_LSTrackID"
+ "Ti,V_LSTrackingVote"
+ "Ti,V_lowSaliencyCnt"
+ "Ti,V_predictedFromPastCnt"
+ "Ti,V_temporalDetectionVote"
+ "Ti,V_trackID"
+ "Ti,V_trackedCnt"
+ "Total ROI count clipped from %d to %d in updateDoGAndLumaFeature for prevLS"
+ "Total ROI count clipped from %d to %d in updateDoGAndLumaFeatures"
+ "Tq,N,V_index2RoiArray"
+ "Tq,R,N,V_roiId"
+ "T{?=fffffI},R,N,V_des"
+ "T{?=fffffI},V_descriptor"
+ "T{?=iiiiiifffiifiiii{?=ffffffff}{?=iiffffffffffffff}{?=fff}},V_params"
+ "T{?=qiIq},N,V_ispTimeStamp"
+ "T{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}},N,V_configuration"
+ "T{CGPoint=dd},R,N,V_nextFrameOpticalCenter"
+ "T{CGPoint=dd},R,N,V_sourceFrameOpticalCenter"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_extendBBox"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_roi"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_LSRoi"
+ "Unable to bind destination pixel buffer textures"
+ "Unable to bind destination tile pixel buffer textures"
+ "Unable to bind repair tile pixel buffer textures"
+ "Unable to bind source pixel buffer textures"
+ "Unable to cache pixel buffer chroma texture"
+ "Unable to cache pixel buffer texture"
+ "Unable to cache pixel luma or main buffer texture"
+ "Unable to create feature descriptor, feature length is zero"
+ "Unable to create feature descriptor, feature sums are zero"
+ "Unable to get chroma texture address"
+ "Unable to get metal luma/main texture address"
+ "Unable to get metal texture address"
+ "Unable to initialize Pixel memory class"
+ "Unable to initialize metal tool box"
+ "Using local model instead"
+ "VDGDetectionUtilsV2"
+ "VDGProcessor"
+ "VEMobileAsset"
+ "VSRNet"
+ "VideoDeghosting"
+ "VideoDeghostingDetectionV2"
+ "[2^{e5rt_buffer_object}]"
+ "[2^{e5rt_io_port}]"
+ "[3@\"<MTLBuffer>\"]"
+ "[3@\"<MTLTexture>\"]"
+ "[3@\"NSMutableData\"]"
+ "[3^{__CVBuffer}]"
+ "[8]"
+ "[9@\"<MTLComputePipelineState>\"]"
+ "[E5Model] Encoding stream\n"
+ "[E5Model] Execute stream\n"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - Asset content: %@"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - Asset locked (ready for use) | assetSelector:%@ | localContentURL:%@"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - Asset locked (ready for use) | newerInProgress:%@"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - Asset locked (ready for use) | no newer version currently being downloaded"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - Error during get auto-asset directory contents: %@"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - Error during initForClientName: %@"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - Error during lockContent:%@"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - endLockUsage | Error: Can't create an MAAutoAssetSelector"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - endLockUsage | assetSelector:%@ | Error: %@"
+ "[VEMobileAsset] downloadMobileAssetWithCompletionHandler - endLockUsage | assetSelector:%@ | SUCCESS"
+ "[VEMobileAsset] getLocalMobileAssetURL - Error during initForClientName: %@"
+ "[VEMobileAsset] getMobileAssetStatus - Error during currentStatusSync: %@"
+ "[VEMobileAsset] getMobileAssetStatus - Error during initForClientName: %@"
+ "[VEMobileAsset] getMobileAssetStatus - expectedTimeRemainingSecs: %f"
+ "[VEMobileAsset] getMobileAssetStatus - localContentURL: %@"
+ "^"
+ "^B"
+ "^f"
+ "^{?=[256@]s}56@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24"
+ "^{?=^{?}ii}"
+ "^{?=^{?}ii}16@0:8"
+ "^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}"
+ "^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16@0:8"
+ "^{__CVMetalTextureCache=}"
+ "^{__CVMetalTextureCache=}16@0:8"
+ "^{__IOSurface=}"
+ "^{__IOSurface=}16@0:8"
+ "^{e5rt_buffer_object=}"
+ "^{e5rt_buffer_object=}16@0:8"
+ "^{e5rt_execution_stream=}"
+ "^{e5rt_execution_stream=}16@0:8"
+ "^{e5rt_execution_stream_operation=}"
+ "^{e5rt_execution_stream_operation=}16@0:8"
+ "^{e5rt_io_port=}"
+ "^{e5rt_io_port=}16@0:8"
+ "^{e5rt_program_function=}"
+ "^{e5rt_program_function=}16@0:8"
+ "^{e5rt_program_library=}"
+ "^{e5rt_program_library=}16@0:8"
+ "_GGDetector"
+ "_LSIsHighRisk"
+ "_LSOrGGBbox"
+ "_LSRoi"
+ "_LSTrackID"
+ "_LSTrackingMatched"
+ "_LSTrackingVote"
+ "_acceptsOpticalFlow"
+ "_addMvf0AndMvf1"
+ "_alignBgAvgYUV"
+ "_area"
+ "_avgAlignedRef0"
+ "_avgAlignedRef0Texture"
+ "_avgAlignedRef1"
+ "_avgAlignedRef1Texture"
+ "_backwarpFlowMvf0"
+ "_backwarpFlowMvf0Texture"
+ "_backwarpFlowMvf1"
+ "_backwarpFlowMvf1Texture"
+ "_bbox"
+ "_bboxList"
+ "_bboxListLen"
+ "_bilinearRescale2ImgsYUV"
+ "_bilinearRescaleYUV"
+ "_blendRefsYUV"
+ "_blendSpatialMitigatedYUV"
+ "_blendedRef0"
+ "_blendedRef0Texture"
+ "_blendedRef1"
+ "_blendedRef1Texture"
+ "_blendingParams"
+ "_blobSaliencyMap"
+ "_blobSaliencyMapTexture"
+ "_bmRef0"
+ "_bmRef0Texture"
+ "_bmRef1"
+ "_bmRef1Texture"
+ "_bmSearch1RefFixedSampleCntYUV"
+ "_bmSearch1RefYUV"
+ "_bmSearch4RepairYUV"
+ "_bmTransfer4RepairYUV"
+ "_bmTransferGray"
+ "_bmTransferWithRoiRepairMvYUV"
+ "_bmTransferYUV"
+ "_buf"
+ "_bytePerPixel"
+ "_cachedTexturesFromPixelBuffer:usage:"
+ "_centerPoint"
+ "_clampGhostROI:"
+ "_collectClusterBgAvg"
+ "_collectClusterMaxAndAvgLuma"
+ "_collectClusterMaxProb"
+ "_collectClusterMv"
+ "_collectClusterMvForMotionCue"
+ "_collectClusterTempRepairErr"
+ "_collectMetaContainers"
+ "_collectMvToFuture"
+ "_collectOverlapWithRefs"
+ "_combineMapWithRefMap"
+ "_compileShaders"
+ "_conditionalDilateProbMapYUV"
+ "_confidence"
+ "_configuration"
+ "_configure"
+ "_connectedPixelsQueue"
+ "_convertFloatBuffer2Texture"
+ "_copyCurrMetaForProcFuture"
+ "_copyFullFrameMapToMap4RoiGen"
+ "_copyImageTileFromPixelBuffer:mergeWithMask:outputTilePixelBuffer:commandBuffer:"
+ "_copyImageTileFromPixelBuffer:outputImageTileTexture:commandBuffer:"
+ "_copyMapToMap4RoiGen"
+ "_copyMvf"
+ "_copyRgbTo4x4ShuffledTextureArray"
+ "_copyRgbToTextureArray"
+ "_copyTextureArrayToRgb"
+ "_currMetaTmp"
+ "_currSegmentProcessedFrameCnt"
+ "_cvMetalTextureCacheRef"
+ "_defaultOpticalCenter"
+ "_des"
+ "_descriptor"
+ "_detectedGreenGhostInfo"
+ "_detectionUtils"
+ "_differenceOfGaussianAndLumaFeature"
+ "_differenceOfGaussianAndLumaFeaturePredictedLocation"
+ "_differenceOfGaussianAndLumaFeatureReflection"
+ "_dilateForwarpHoleMap"
+ "_dilateGrayImg"
+ "_dilateProbMap"
+ "_dilateReflLsMap"
+ "_dilatedFlowRef0Map"
+ "_dilatedFlowRef0MapTexture"
+ "_dilatedFlowRef1Map"
+ "_dilatedFlowRef1MapTexture"
+ "_dilatedLsMap"
+ "_dilatedLsMapTexture"
+ "_dist2OpticalCenterList"
+ "_dist2OpticalCenterListLen"
+ "_dist2ghost"
+ "_dist2opticalCenter"
+ "_dlSpaBlendMask"
+ "_dlSpaBlendMaskTexture"
+ "_dlSpaInput"
+ "_dlSpaInputTexture"
+ "_dlSpaRepairMask"
+ "_dlSpaRepairMaskTexture"
+ "_dlSpatialMitigated"
+ "_dlSpatialMitigatedTexture"
+ "_doneKPToBBoxViaGraphTraversal"
+ "_errRescaleProbMap0"
+ "_errRescaleProbMap0Texture"
+ "_errRescaleProbMap1"
+ "_errRescaleProbMap1Texture"
+ "_espressoContext"
+ "_espressoEngine"
+ "_espressoInputImageBuffer"
+ "_espressoInputMaskBuffer"
+ "_espressoNetwork"
+ "_espressoOutputBuffer"
+ "_espressoPlan"
+ "_extendBBox"
+ "_filteredOpticalCenterShift"
+ "_findBoundingBoxesWithSizeThreshold:LsThreshold:scalingFactor:validWidth:validHeight:"
+ "_flowMvf0"
+ "_flowMvf0Texture"
+ "_flowMvf1"
+ "_flowMvf1Texture"
+ "_flowNet"
+ "_flowPreprocessor"
+ "_flowRef"
+ "_flowRef0Map"
+ "_flowRef0MapTexture"
+ "_flowRef1Map"
+ "_flowRef1MapTexture"
+ "_flowRefTexture"
+ "_flowTarget"
+ "_flowTargetTexture"
+ "_forceGpuWaitForComplete"
+ "_format"
+ "_forwarpOutputBuffer0"
+ "_forwarpOutputBuffer1"
+ "_frameT"
+ "_frameTMinus1"
+ "_frameTMinus1Texture"
+ "_frameTMinus2"
+ "_frameTMinus2Texture"
+ "_frameTPlus1Buf"
+ "_frameTPlus1Texture"
+ "_frameTPlus2Buf"
+ "_fullResRawRefinedProbMap"
+ "_fullResRawRefinedProbMapTexture"
+ "_fullResStashedProbMap4FutureTracking"
+ "_fullResStashedProbMap4FutureTrackingTexture"
+ "_function"
+ "_fuse4DetectionYUV"
+ "_futureFramesToDetectionAndRepair"
+ "_futureInputParamsToRepair"
+ "_futureMeta4LsCheck"
+ "_futureMeta4RedoTracking"
+ "_futureMetaTmp"
+ "_getBgAvgYUV"
+ "_getBlobSaliency"
+ "_getGhostProbMapYUV"
+ "_getLsMapYUV"
+ "_getMotionMapYUV"
+ "_getMvForMotionCueFromMvf"
+ "_getMvFromLs"
+ "_getMvToFutureFromMvf"
+ "_getOverlapWithRefs"
+ "_getProbMapInput:reflLs:trackingRef:trackingRefProb:trackingRefSpaProb:trackingRefErrRescaleProb:trackingRefLs:inputBuf:reflLsBuf:trackingRefBuf:trackingRefProbBuf:trackingRefSpaProbBuf:trackingRefErrRescaleProbBuf:trackingRefLsBuf:trackingMvf:metaBuf:metaBufArray:trackingRefMetaBuf:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:refinedReflLs:probMapStash4FutureTracking:probMapBuf:errRescaleProbMapBuf:rawRefinedProbMapBuf:refinedProbMapBuf:refinedReflLsBuf:probMapStash4FutureTrackingBuf:doTracking:waitForComplete:"
+ "_getProbMapsLiteTarget:refProbMap:refLsMap:refRefinedLsMap:refProbMapStash4FutureTracking:refErrRescaleProbMap:refRawRefinedProbMap:refRefinedProbMap:mvf:probMap:lsMap:refinedLsMap:probMapStash4FutureTracking:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:metaBufArray:waitForComplete:"
+ "_getRoiMaxAndAvgLumaYUV"
+ "_getRoiRepairMvFromMvf"
+ "_getSaliencyMapYUV"
+ "_getTempRepairedBgAlignErrYUV"
+ "_ggmController"
+ "_hmgrphyRef0"
+ "_hmgrphyRef0Texture"
+ "_hmgrphyRef1"
+ "_hmgrphyRef1Texture"
+ "_imageDimensions"
+ "_index2RoiArray"
+ "_initDetection:futureFrames:outputImgBufTMinus1:outputImgBufTMinus2:"
+ "_initParamsWithLowLight:"
+ "_input4MotionCue"
+ "_input4MotionCueTexture"
+ "_inputBuffer"
+ "_inputBufferObject"
+ "_inputBufferObjects"
+ "_inputCopy"
+ "_inputCopyTexture"
+ "_inputParamsToRepair"
+ "_inputPortName"
+ "_inputPortNames"
+ "_inputROI"
+ "_inputSurface"
+ "_inputTexture"
+ "_input_port"
+ "_input_ports"
+ "_integralSumPixelBuffer"
+ "_isPredictedFromPast"
+ "_isReflectedLS"
+ "_isTracked"
+ "_isTrajectoryPruningPassed"
+ "_ispTimeStamp"
+ "_keyPointsList"
+ "_kpIsFromHW"
+ "_kpIsFromHWList"
+ "_kpIsFromHWListLen"
+ "_library"
+ "_lightSourceMask"
+ "_locationList"
+ "_locationListLen"
+ "_lookaheadFrameProcessedInFinish"
+ "_lookaheadFrames"
+ "_lowSaliencyCnt"
+ "_lrBmRef0"
+ "_lrBmRef0Texture"
+ "_lrBmRef1"
+ "_lrBmRef1Texture"
+ "_lrHwLsMask0"
+ "_lrHwLsMask0Texture"
+ "_lrHwLsMask1"
+ "_lrHwLsMask1Texture"
+ "_lsHasBeenUsedForTrackingGhost"
+ "_lsMap4RoiGen"
+ "_lsMap4RoiGenTexture"
+ "_lsMapQueue"
+ "_lsMapTexQueue"
+ "_lumaFeatureVector"
+ "_lumaFeatureVectorPredictedLocation"
+ "_lumaFeatureVectorReflection"
+ "_maskToRoi"
+ "_matchedLS"
+ "_maxRoiHeight"
+ "_maxRoiWidth"
+ "_metaArray"
+ "_metaBufArray"
+ "_metaBufferArray"
+ "_metaContainer"
+ "_metaDictionary"
+ "_metaInfoQueue"
+ "_metalToolBox"
+ "_metalToolbox"
+ "_mitigationANE"
+ "_modelPath"
+ "_motionMap"
+ "_motionMapTexture"
+ "_mv"
+ "_mvCnt"
+ "_mvSum"
+ "_mvf4Future"
+ "_mvf4FutureTexture"
+ "_mvf4Repair0"
+ "_mvf4Repair0Texture"
+ "_mvf4Repair1"
+ "_mvf4Repair1Texture"
+ "_neighbors"
+ "_netSize"
+ "_nextFrameOpticalCenter"
+ "_nextVisedOpticalCenter"
+ "_operation"
+ "_opticalCenterArray"
+ "_opticalCenterArrayIndex"
+ "_opticalCenterArrayLen"
+ "_opticalCenterMvShift"
+ "_opticalCenterMvShiftArray"
+ "_opticalCenterShift"
+ "_outputBufferObject"
+ "_outputPortName"
+ "_outputSurface"
+ "_output_port"
+ "_pMemory"
+ "_pMemoryPlane2"
+ "_padRGBKernel"
+ "_params"
+ "_pasteRepairedTile:inputTileTexture:blendingMask:outputPixelBuffer:commandBuffer:"
+ "_pipelineStates"
+ "_predictedFromPastCnt"
+ "_preprocessInputs4MotionCueYUV"
+ "_prevHRSurface"
+ "_prevShouldRunGGDetectionClippedPixelBased"
+ "_prevShouldRunGGDetectionLSBased"
+ "_prevShouldRunGGDetectionLuxLevelBased"
+ "_previousPreviousOutputFrame"
+ "_probMap4RepairQueue"
+ "_probMap4RepairTexQueue"
+ "_probMap4RoiGen"
+ "_probMap4RoiGenTexture"
+ "_probMap4SpatialRepairQueue"
+ "_probMap4SpatialRepairTexQueue"
+ "_probMapQueue"
+ "_probMapTexQueue"
+ "_processedFrameCnt"
+ "_processedFrameInDetection"
+ "_processedPixelBuffer"
+ "_processedPrevLSROIs"
+ "_processedPrevLSType"
+ "_processedROIs"
+ "_processedType"
+ "_rawProbMap"
+ "_rawProbMapTexture"
+ "_rawWarpedRefProbMap"
+ "_rawWarpedRefProbMapTexture"
+ "_rawWarpedRefSpaProbMap"
+ "_rawWarpedRefSpaProbMapTexture"
+ "_readBufferOnly"
+ "_ref4MotionCue"
+ "_ref4MotionCueTexture"
+ "_refineFutureHwLsMapWithTrackingYUV"
+ "_refinedReflLs4trackingRefWarped"
+ "_refinedReflLs4trackingRefWarpedTexture"
+ "_reflHwLsMask0"
+ "_reflHwLsMask0Texture"
+ "_reflHwLsMask1"
+ "_reflHwLsMask1Texture"
+ "_reflectYUVImg2"
+ "_reflectedLSList"
+ "_reflectedLSListLen"
+ "_repair:outputBuf:ghostROI:inputROI:repairMask:blendMask:"
+ "_repairParameters"
+ "_resetDetectionResults"
+ "_resetIntermediateVariables"
+ "_resetOutput"
+ "_roi"
+ "_roiId"
+ "_roiMv"
+ "_saliencyMap"
+ "_saliencyMapTexture"
+ "_setWOri"
+ "_skipClamp"
+ "_sourceFrameOpticalCenter"
+ "_spaProbMapQueue"
+ "_spaProbMapTexQueue"
+ "_spatialMitigated"
+ "_spatialMitigatedTexture"
+ "_spatialRepairYUV"
+ "_spatialTemporalRepair4DetectionYUV"
+ "_stashedFutureGhostRois0"
+ "_stashedFutureGhostRois1"
+ "_stream"
+ "_stride"
+ "_stridePlane2"
+ "_syncWeightsOriginal"
+ "_temporalDetectionMatched"
+ "_temporalDetectionVote"
+ "_temporalMitigated"
+ "_temporalMitigatedTexture"
+ "_tileConfig"
+ "_tileInputImageTexture"
+ "_tileInputPixelBuffer"
+ "_tileOutputPixelBuffer"
+ "_tileOutputPixelBufferLr"
+ "_trackFail"
+ "_trackID"
+ "_trackIDsAfterMerge"
+ "_trackSessionId"
+ "_trackedCnt"
+ "_tradSpatialMitigated"
+ "_tradSpatialMitigatedTexture"
+ "_trajectoryFromPast"
+ "_tuningParamDict"
+ "_tuningParams"
+ "_updateOutputFloat"
+ "_upscaleProbMap"
+ "_upscaleThenReflectLsMap"
+ "_visedOpticalCenter"
+ "_visualizeMvf"
+ "_warpBlendRGBKernel"
+ "_warpMvf0WithMvf1"
+ "_warpMvf0WithMvf1ThenAddToMvf2"
+ "_warpRefMeta"
+ "_warpRefMetaLite"
+ "_warpedFlowMvf"
+ "_warpedFlowMvfTexture"
+ "_warpedHwLsMask4Track"
+ "_warpedHwLsMask4TrackTexture"
+ "_warpedRefProbMap"
+ "_warpedRefProbMapTexture"
+ "_warpedReflTrackingRef"
+ "_warpedReflTrackingRefTexture"
+ "absoluteString"
+ "addObjectsFromArray:"
+ "allocateInputBufferObjects"
+ "allocateOutputBufferObjects"
+ "area"
+ "array"
+ "bbox"
+ "bbox count %ld exceeds the limit: %d"
+ "boundingBoxForMerge"
+ "buf"
+ "bytePerPixel"
+ "clearReferencedROIsForROIList:"
+ "clusterIndicesOfRois:withExtendedRadius:roiCnt:imageRect:"
+ "cmivdg_ve_force_gpu_wait"
+ "com.apple.MobileAsset.VideoEffect"
+ "com.apple.videoeffect.GGM"
+ "com.apple.videoeffect.ISR"
+ "com.apple.videoeffect.VSR"
+ "commitCmdBuffer:waitForComplete:"
+ "compareSelfAsLSWithAnotherLS:"
+ "compileModelOnDevice"
+ "completion event"
+ "confidence"
+ "configuration"
+ "contentsOfDirectoryAtPath:error:"
+ "convertBuffer:toFP16IOSurface:"
+ "convertBuffer:toFP16ShuffledIOSurface:"
+ "convertFP16IOSurface:toBuffer:"
+ "convertInternalBBoxes:outputArray:"
+ "convertInternalBBoxesToROI:outputArray:"
+ "convertPackedMaskToRegular:output:"
+ "copyRgbTo4x4ShuffledTextureArray"
+ "copyRgbToTextureArray"
+ "copyTextureArrayToRgb"
+ "countByEnumeratingWithState:objects:count:"
+ "createFP16TextureFromIOSurface:width:height:arrayLength:"
+ "createForwarpOutputBufferWidth:height:channels:"
+ "createFunction"
+ "currRoi in %s fail"
+ "currentStatusSync:"
+ "cvMetalTextureCacheRef"
+ "d"
+ "d16@0:8"
+ "dataWithBytes:length:"
+ "defaultManager"
+ "defaultOpticalCenter"
+ "deghostingParams pixel format mismatch with VSAProcessor's format for the DVPFrameProcessor session"
+ "dependent event"
+ "des"
+ "descriptor"
+ "detectedGreenGhostInfo"
+ "detection"
+ "differenceOfGaussianAndLumaFeature"
+ "differenceOfGaussianAndLumaFeaturePredictedLocation"
+ "differenceOfGaussianAndLumaFeatureReflection"
+ "dispatchThreads:threadsPerThreadgroup:"
+ "dist2ghost"
+ "dist2opticalCenter"
+ "dlRepair::extractImageTile"
+ "dlRepair::extractImageTileAndMergeMask"
+ "dlRepair::pasteTileAndBlendWithMaskKernel"
+ "dlSpatialRepairYUV:output:repairMask:blendMask:inputTex:repairMaskTex:blendMaskTex:wRepairedY:wRepairedUV:metaBuf:"
+ "doTrackingToNextFrameCurrMetaWithDetectionResults:currMetaWithMvToFuture:futureMeta:opticalCenter:futureOpticalCenter:futureFrameCnt:doLite:waitForComplete:"
+ "doneKPToBBoxViaGraphTraversal"
+ "downloadAssetWithCompletionHandler:"
+ "downloadMobileAssetType:assetSpecifier:forClientName:completionHandler:"
+ "downloadMobileAssetWithCompletionHandler:"
+ "downloadMobileAssetWithInputType:withCompletionHandler:"
+ "downloadProgress"
+ "e5rt_async_event_create(&completionEvent, \"completion event\", E5RT_ASYNC_EVENT_TYPE_IOSURFACE_SHARED_EVENT)"
+ "e5rt_async_event_create(&dependentEvent, \"dependent event\", E5RT_ASYNC_EVENT_TYPE_IOSURFACE_SHARED_EVENT)"
+ "e5rt_buffer_object_get_iosurface(_inputBufferObject, &_inputSurface)"
+ "e5rt_buffer_object_get_iosurface(_inputBufferObjects[0], &_inputSurface)"
+ "e5rt_buffer_object_get_iosurface(_inputBufferObjects[0], &_prevHRSurface)"
+ "e5rt_buffer_object_get_iosurface(_inputBufferObjects[1], &_inputSurface)"
+ "e5rt_buffer_object_get_iosurface(_inputBufferObjects[1], &_prevHRSurface)"
+ "e5rt_buffer_object_get_iosurface(_outputBufferObject, &_outputSurface)"
+ "e5rt_e5_compiler_compile(compiler, _modelPath.UTF8String, compiler_options, &_library)"
+ "e5rt_e5_compiler_create(&compiler)"
+ "e5rt_e5_compiler_options_create(&compiler_options)"
+ "e5rt_e5_compiler_options_set_compute_device_types_mask(compiler_options, compute_device_types_mask)"
+ "e5rt_e5_compiler_options_set_force_recompilation(compiler_options, true)"
+ "e5rt_execution_stream_create(&_stream)"
+ "e5rt_execution_stream_encode_operation(stream, operation)"
+ "e5rt_execution_stream_operation_bind_completion_event(operation, completionEvent)"
+ "e5rt_execution_stream_operation_bind_dependent_events(operation, &dependentEvent, 1)"
+ "e5rt_execution_stream_operation_create_precompiled_compute_operation_with_options(&_operation, create_options)"
+ "e5rt_execution_stream_operation_get_num_inputs(self.operation, &num_input_ports)"
+ "e5rt_execution_stream_operation_prepare_op_for_encode(operation)"
+ "e5rt_execution_stream_operation_retain_input_port(self.operation, _inputPortName.UTF8String, &_input_port)"
+ "e5rt_execution_stream_operation_retain_input_port(self.operation, _inputPortNames[0].UTF8String, &_input_ports[0])"
+ "e5rt_execution_stream_operation_retain_input_port(self.operation, _inputPortNames[1].UTF8String, &_input_ports[1])"
+ "e5rt_execution_stream_operation_retain_output_port(_operation, _outputPortName.UTF8String, &_output_port)"
+ "e5rt_execution_stream_reset(stream)"
+ "e5rt_io_port_bind_buffer_object(_input_port, _inputBufferObject)"
+ "e5rt_io_port_bind_buffer_object(_input_ports[0], _inputBufferObjects[0])"
+ "e5rt_io_port_bind_buffer_object(_input_ports[1], _inputBufferObjects[1])"
+ "e5rt_io_port_bind_buffer_object(self.output_port, self.outputBufferObject)"
+ "e5rt_io_port_is_tensor(port, &is_tensor)"
+ "e5rt_io_port_retain_surface_desc(port, &surface_desc)"
+ "e5rt_io_port_retain_tensor_desc(_input_port, &input_tensor_desc)"
+ "e5rt_io_port_retain_tensor_desc(_input_ports[0], &input_tensor_desc0)"
+ "e5rt_io_port_retain_tensor_desc(_input_ports[1], &input_tensor_desc1)"
+ "e5rt_io_port_retain_tensor_desc(_output_port, &output_tensor_desc)"
+ "e5rt_io_port_retain_tensor_desc(port, &tensor_desc)"
+ "e5rt_precompiled_compute_op_create_options_create_with_program_function(&create_options, _function)"
+ "e5rt_program_library_retain_program_function(_library, usage_function_name, &_function)"
+ "e5rt_surface_desc_get_height(surface_desc, height)"
+ "e5rt_surface_desc_get_width(surface_desc, width)"
+ "e5rt_tensor_desc_alloc_buffer_object(input_tensor_desc, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_inputBufferObject)"
+ "e5rt_tensor_desc_alloc_buffer_object(input_tensor_desc0, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_inputBufferObjects[0])"
+ "e5rt_tensor_desc_alloc_buffer_object(input_tensor_desc1, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_inputBufferObjects[1])"
+ "e5rt_tensor_desc_alloc_buffer_object(output_tensor_desc, E5RT_BUFFER_OBJECT_TYPE_IOSURFACE, 1, &_outputBufferObject)"
+ "encodeAddMvf0ToMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:"
+ "encodeAlignBgAvgYUVToCommandEncoder:input:ref0:ref1:alignedRef0:alignedRef1:metaBuf:"
+ "encodeBMSearch1RefToCommandEncoder:target:ref:reflect:normalizedTargetCenter:normalizedRefCenter:bestMatchLoc:meta:"
+ "encodeBMSearch4RepairToCommandEncoder:hrTarget:target:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:mvf0:mvf1:meta:"
+ "encodeBMTransfer4RepairYUVToCommandEncoder:ref0:ref1:forwarpHoleMap0:forwarpHoleMap1:probMap:warpedRef0:warpedRef1:bmMvf0:bmMvf1:backwarpFlow0:backwarpFlow1:meta:"
+ "encodeBMTransferGrayToCommandEncoder:ref:warpedRef:bestMatchLoc:meta:sf:"
+ "encodeBMTransferYUVToCommandEncoder:ref:reflect:normalizedCenter:warpedRef:bestMatchLoc:meta:sf:"
+ "encodeBilinearRescale2ImgsYUV:fullResInput:input0:output0:input1:output1:meta:"
+ "encodeBilinearRescaleYUV:fullResInput:input:meta:blurBeforeSample:output:"
+ "encodeBlendRefsYUVToCommandEncoder:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:output0:output1:metaBuf:"
+ "encodeBlendSpatialMitigatedYUVToCommandEncoder:inputTexture:probMapTexture:probMap4TradSpatialTexture:tradSpatialMitTexture:dlSpatialMitTexture:outputTexture:metaBuf:"
+ "encodeBmTransferWithRoiRepairMvYUVToCommandEncoder:fullResInput:ref0:warpedRef0:ref1:warpedRef1:meta:"
+ "encodeCollectClusterBgAvgToCommandEncoder:clusterMetaBuf:metaBuf:"
+ "encodeCollectClusterMaxAndAvgLuma:clusterMetaBuf:metaBuf:"
+ "encodeCollectClusterMaxProb:clusterMetaBuf:metaBuf:"
+ "encodeCollectClusterMv:clusterMetaBuf:metaBuf:"
+ "encodeCollectClusterMvForMotionCueToCommandEncoder:clusterMetaBuf:metaBuf:"
+ "encodeCollectClusterOverlapWithRefs:clusterMetaBuf:metaBuf:"
+ "encodeCollectClusterTempRepairErr:clusterMetaBuf:metaBuf:"
+ "encodeCollectMetaContainers:metaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:currTrackId:"
+ "encodeCollectMvToFuture:metaBuf:"
+ "encodeCombineMapWithRefMapToEncoder:map:ref:dilatedRef:lsMap:dilatedLsMap:refLsMap:motion:saliency:targetFrameYUV:blobSaliency:spaRef:mvf:output:spaOutput:meta:wRef:"
+ "encodeConditionalDilateProbMapYUV:inputYUV:probMap:dilatedProbMap:hardDilationRadius:softDilationRadius:meta:"
+ "encodeConvertFloatBuffer2TextureToCommandEncoder:inputBuffer0:inputBuffer1:meta:output0:outputMap0:output1:outputMap1:"
+ "encodeCopyCurrMetaForProcFuture:metaBuf:outMetaBuf:"
+ "encodeCopyFullFrameMapToMap4RoiGenToCommandEncoder:input:output:"
+ "encodeCopyMapToMap4RoiGenToCommandEncoder:input:output:metaBuf:"
+ "encodeCopyMvfToCommandEncoder:fullResTarget:mvf0:outMvf0:mvf1:outMvf1:meta:"
+ "encodeDilateForwarpHoleMap:fullResTarget:inputMap0:outputMap0:inputMap1:outputMap1:hardDilationRadius:softDilationRadius:meta:"
+ "encodeDilateGrayImg:input:output:hardDilationOutput:hardDilationRadius:softDilationRadius:meta:"
+ "encodeDilateProbMap:input:output:hardDilationRadius:softDilationRadius:meta:"
+ "encodeDilateReflLsMap:inputYUV:lsMap:dilatedLsMap:hardDilationRadius:softDilationRadius:meta:"
+ "encodeForwarpYUVToCommandEncoder:input0:input1:meta:mvf0:mvf1:intermediateOutput0:intermediateOutput1:output0:output1:outputMap0:outputMap1:"
+ "encodeFuse4DetectionYUVToCommandEncoder:inputTexture:probMapTexture:temporalMitTexture:spatialMitTexture:forceToSpatial:outputTexture:metaBuf:"
+ "encodeGetBgAvgYUVToCommandEncoder:target:ref0:ref1:probMap:meta:"
+ "encodeGetBlobSaliency:inputYUV:blobSaliencyMap:meta:"
+ "encodeGetGhostProbMapToCommandEncoder:target:reflLsMap:motionMap:saliencyMap:isInitFrame:probMap:meta:"
+ "encodeGetLsMapYUVToCommandEncoder:input:map:"
+ "encodeGetMotionMapYUVToCommandEncoder:ref:target:motionMap:meta:"
+ "encodeGetMvForMotionCueFromMvf:fullResInput:meta:mvf:opticalCenter:refOpticalCenter:"
+ "encodeGetMvFromLsToCommandEncoder:target:lsMap:refLsMap:targetCenter:refCenter:meta:"
+ "encodeGetMvToFutureFromMvf:fullResInput:meta:mvf:"
+ "encodeGetOverlapWithRefs:input:probMap:metaBuf:"
+ "encodeGetRoiMaxAndAvgLumaYUV:target:lsMap:meta:"
+ "encodeGetRoiRepairMvFromMvfToCommandEncoder:fullResInput:probMap:mvf0:mvf1:meta:"
+ "encodeGetSaliencyMapToCommandEncoder:target:saliencyMap:meta:"
+ "encodeGetTempRepairedBgAlignErrYUVToCommandEncoder:target:hmgrphyRef0:hmgrphyRef1:bmRef0:bmRef1:probMap:errRescaleProbMap:prevProbMap:flow0:flow1:meta:"
+ "encodePadRGBToCommandBuffer:source:destination:"
+ "encodePreprocessInputs4MotionCueYUVToCommandEncoder:input:ref:output:refOutput:metaBuf:processedFrameCount:"
+ "encodeRefineFutureHwLsMapWithTrackingToEncoder:reflHwMap:target:opticalCenter:warpedRefReflHwMap:warpedReflRef:metaBuf:"
+ "encodeReflectYUVImg2:fullResInput:meta:input0:output0:center0:input1:output1:center1:"
+ "encodeResetOutputToCommandEncoder:input:meta:output0:output1:"
+ "encodeSpatialRepairYUVToCommandEncoder:input:probMap4Spatial:spatialOutput:metaBuf:"
+ "encodeSpatialTemporalRepair4DetectionYUVToCommandEncoder:input:frRef0:frRef1:temporalOutput:inputCopy:metaBuf:"
+ "encodeSyncWeightsOriginal:clusterMetaBuf:metaBuf:"
+ "encodeUpdateOutputFloatToCommandEncoder:input0:flow0:input1:flow1:meta:output0:output1:"
+ "encodeUpscaleProbMap:probMap:refinedProbMap:inputFrame:upscaledProbMap:upscaledRefinedProbMap:meta:"
+ "encodeUpscaleThenReflectLsMap:input:normalizedCenter:output:"
+ "encodeVisualizeMvfToCommandEncoder:fullResTarget:mvf:outMvf:meta:"
+ "encodeWarpBlendToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:"
+ "encodeWarpMvf0WithMvf1ThenAddToMvf2ToCommandEncoder:fullResTarget:mvf0:mvf1:mvf2:outMvf:meta:"
+ "encodeWarpMvf0WithMvf1ToCommandEncoder:fullResTarget:mvf0:mvf1:outMvf:meta:"
+ "encodeWarpRefMeta:refMetaBuf:metaBuf:outMetaBuf:lsCheckOutmetaBuf:redoTrackingOutmetaBuf:capRefMetaCnt:"
+ "encodeWarpRefMetaLite:refMetaBuf:outMetaBuf:"
+ "endAllLocksWithAssetType:assetSpecifier:forClientName:"
+ "endAllPreviousLocksOfSelectorSync:forClientName:"
+ "exchangeObjectAtIndex:withObjectAtIndex:"
+ "executeSynchronouslyOperation:onStream:"
+ "expectedTimeRemainingSecs"
+ "extendBBox"
+ "extractRoiByGraphTraversalInput:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:"
+ "f24@0:8i16i20"
+ "f28@0:8f16f20f24"
+ "fileExistsAtPath:"
+ "findTinyKeypointLocationsFromLS:inputTexture:dilation:estimatedOpticalCenter:metalBuffers:maxBufferLength:keypointSampleStepCount:"
+ "format"
+ "function"
+ "futureFramesToDetectionAndRepair"
+ "futureInputParamsToRepair"
+ "generateBoxesForDoGAndLumaAndForLSROIs:prevGGROIs:inputTexture:opticalCenter:metalBuffers:maxBufferLength:"
+ "generateBoxesForDoGAndLumaAndForPrevLSROIs:homography:metalBuffers:maxBufferLength:"
+ "generateDetectionRoiList:outputArray:"
+ "generateLocationFromBBox"
+ "generateMetaContainerArrayBufFromMetaContainerBuf:imageRect:"
+ "generateTrajectoryForROI:isGG:"
+ "generateTrajectoryForROIList:isGG:"
+ "getAssetStatusWithPercentCompleted:"
+ "getBBoxesUsingGraphTraversalFrom:pixValThreshold:bboxSizeThreshold:scaleFactor:roi:returnAsDetectedROI:outputArray:"
+ "getBestROIInROIList:referenceROI:"
+ "getClosestRoi:forCoord:"
+ "getCommandqueue"
+ "getDetectionRoiListFromMeta:outputArray:"
+ "getDevice"
+ "getFlowTarget:ref:targetBuf:refBuf:mvf:backwardMvf:metaBuf:skipRescaling:"
+ "getGGCandidatesFromROIList:GGList:"
+ "getGhostTrackIdFromLs:"
+ "getHighRiskLS:"
+ "getInputPortNames"
+ "getLSBBoxesUsingGraphTraversalFrom:roi:pixValThreshold:bboxSizeThreshold:scaleFactorInv:validWidth:validHeight:lightSourceBBox:"
+ "getLocalMobileAssetURLWithAssetType:assetSpecifier:forClientName:"
+ "getLocationMatchCostWith:"
+ "getMobileAssetStatusForInputType:percentCompleted:"
+ "getMobileAssetStatusWithAssetType:assetSpecifier:forClientName:percentCompleted:"
+ "getMobileAssetStatusWithPercentCompleted:"
+ "getMotionShiftFromOpticalCenters:opticalCenterArrayLen:opticalCenterMotionShifts:"
+ "getMvfToNextFrameForTrackingCurrMeta:lsMap:futureLsMap:lsMapBuf:futureLsMapBuf:opticalCenter:futureOpticalCenter:waitForComplete:"
+ "getOutputPortNames"
+ "getPixelFeatureMatchCostWith:"
+ "getProbMapsTarget:ref:rawProbMap:probMap:errRescaleProbMap:rawRefinedProbMap:refinedProbMap:reflLsMap:refinedReflLsMap:reflLsMap4TrackingRef:metaBuf:metaBufArray:trackingMvf:useRefProbMap:opticalCenter:trackingRefOpticalCenter:waitForComplete:"
+ "getReflLsListAsDetectedROIFromMeta:"
+ "getReflLsListFromMeta:outputArray:"
+ "getReflectedBboxAroundCenter:"
+ "getReflectedBboxCenterAroundCenter:"
+ "getRoiMvForRoiList:fromMeta:"
+ "getSearchLocation:"
+ "getTemporalDetectionSearchRadiusForReferenceFrameIndex:minSearchRadius:slope:"
+ "getTopGhostsInList:k:opticalCenter:ghostCntGatingTh:"
+ "getTopLSInList:k:dist2ghostTol:"
+ "getTopLSInListByDroppingBottoms:k:dist2ghostTol:"
+ "getTopLSInListByKeepingTops:k:dist2ghostTol:"
+ "getTrajectoryMatchingCostGG:"
+ "ghostIsHighConfidence:"
+ "hasSuffix:"
+ "i20@0:8I16"
+ "i24@0:8@16"
+ "imageByCompositingOverImage:"
+ "imageByCroppingToRect:"
+ "imageWithColor:"
+ "in_img"
+ "index2RoiArray"
+ "initContextWithFilePath:engine:configuration:usePreCompiled:"
+ "initForAssetType:withAssetSpecifier:"
+ "initForClientName:selectingAsset:error:"
+ "initImageWithValue:"
+ "initWithBbox:"
+ "initWithBbox:descriptor:"
+ "initWithCapacity:"
+ "initWithCvPixelBuffer:"
+ "initWithCvPixelBuffer:skipClamp:readOnly:"
+ "initWithMetalContext:commandQueue:"
+ "initWithMetalContext:commandQueue:imageDimensions:"
+ "initWithMetalContext:commandQueue:imageDimensions:netSize:metalToolBox:"
+ "initWithMetalContext:commandQueue:tuningParamDict:"
+ "initWithMetalToolBox:"
+ "initWithMetalToolBox:config:imageDimensions:"
+ "initWithMetalToolBox:configuration:tuningParams:"
+ "initWithModelPath:inputWidth:inputHeight:"
+ "initWithModelPath:usage:useMPS:"
+ "initWithRed:green:blue:"
+ "initWithSourceFrame:nextFrame:opticalFlow:sourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:submissionMode:destinationFrame:"
+ "initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:submissionMode:destinationFrame:"
+ "initWithTrackingSessionId:roiId:andRoi:"
+ "initWithTrackingSessionId:roiId:roi:LSRoi:confidence:"
+ "initWithTrackingSessionId:roiId:roi:LSRoi:descriptor:propertiesForPostProcPipeVisualization:"
+ "initWithTrackingSessionId:roiId:roi:trackId:"
+ "initializeInputPorts"
+ "initializeModel"
+ "inputBuffer"
+ "inputHeight"
+ "inputParamsToRepair"
+ "inputSurface"
+ "inputWidth"
+ "integralSumPixelBuffer"
+ "isBoxSizeValidForProcessing:AndErodeBy:"
+ "isPredictedFromPast"
+ "isReflectedLS"
+ "isTracked"
+ "isTrajectoryPruningPassed"
+ "ispTimeStamp"
+ "isrnet_4x.mlmodelc/model.mil"
+ "keyPointsList"
+ "kpIsFromHW"
+ "landscape272x480"
+ "landscape512x512"
+ "library"
+ "light source bounding box count: %ld exeed the limit: %d"
+ "lightSourceMask"
+ "loadModelFromPath:"
+ "locIsInSearchRange:searchLocation:defaultSearchLocation:searchRadius:defaultSearchRange:searchInGivenLocsOnly:"
+ "lockContent:withUsagePolicy:withTimeout:completion:"
+ "lockContentSync:withTimeout:lockedAssetSelector:newerInProgress:error:"
+ "lockContentSync:withUsagePolicy:withTimeout:lockedAssetSelector:newerInProgress:error:"
+ "lowSaliencyCnt"
+ "lsHasBeenUsedForTrackingGhost"
+ "lumaFeatureVector"
+ "lumaFeatureVectorPredictedLocation"
+ "lumaFeatureVectorReflection"
+ "matchedLS"
+ "maxTotalThreadsPerThreadgroup"
+ "metaContainer"
+ "metaDictionary"
+ "metal buffer is NULL"
+ "metalToolBox::addMvf0AndMvf1"
+ "metalToolBox::alignBgAvgYUV"
+ "metalToolBox::bilinearRescale2ImgsYUV"
+ "metalToolBox::bilinearRescaleYUV"
+ "metalToolBox::blendRefsYUV"
+ "metalToolBox::blendSpatialMitigatedYUV"
+ "metalToolBox::bmSearch1RefFixedSampleCntYUV"
+ "metalToolBox::bmSearch1RefYUV"
+ "metalToolBox::bmSearch4RepairYUV"
+ "metalToolBox::bmTransfer4RepairYUV"
+ "metalToolBox::bmTransferGray"
+ "metalToolBox::bmTransferWithRoiRepairMvYUV"
+ "metalToolBox::bmTransferYUV"
+ "metalToolBox::collectClusterBgAvg"
+ "metalToolBox::collectClusterMaxAndAvgLuma"
+ "metalToolBox::collectClusterMaxProb"
+ "metalToolBox::collectClusterMv"
+ "metalToolBox::collectClusterMvForMotionCue"
+ "metalToolBox::collectClusterTempRepairErr"
+ "metalToolBox::collectMetaContainers"
+ "metalToolBox::collectMvToFuture"
+ "metalToolBox::collectOverlapWithRefs"
+ "metalToolBox::combineMapWithRefMap"
+ "metalToolBox::conditionalDilateProbMapYUV"
+ "metalToolBox::convertFloatBuffer2Texture"
+ "metalToolBox::copyCurrMetaForProcFuture"
+ "metalToolBox::copyFullFrameMapToMap4RoiGen"
+ "metalToolBox::copyMapToMap4RoiGen"
+ "metalToolBox::copyMvf"
+ "metalToolBox::dilateForwarpHoleMap"
+ "metalToolBox::dilateGrayImg"
+ "metalToolBox::dilateProbMap"
+ "metalToolBox::dilateReflLsMap"
+ "metalToolBox::fuse4DetectionYUV"
+ "metalToolBox::getBgAvgYUV"
+ "metalToolBox::getBlobSaliency"
+ "metalToolBox::getGhostProbMapYUV"
+ "metalToolBox::getLsMapYUV"
+ "metalToolBox::getMotionMapYUV"
+ "metalToolBox::getMvForMotionCueFromMvf"
+ "metalToolBox::getMvFromLs"
+ "metalToolBox::getMvToFutureFromMvf"
+ "metalToolBox::getOverlapWithRefs"
+ "metalToolBox::getRoiMaxAndAvgLumaYUV"
+ "metalToolBox::getRoiRepairMvFromMvf"
+ "metalToolBox::getSaliencyMapYUV"
+ "metalToolBox::getTempRepairedBgAlignErrYUV"
+ "metalToolBox::preprocessInputs4MotionCueYUV"
+ "metalToolBox::refineFutureHwLsMapWithTrackingYUV"
+ "metalToolBox::reflectYUVImg2"
+ "metalToolBox::resetOutput"
+ "metalToolBox::spatialRepairYUV"
+ "metalToolBox::spatialTemporalRepair4DetectionYUV"
+ "metalToolBox::syncWeightsOriginal"
+ "metalToolBox::updateOutputFloat"
+ "metalToolBox::upscaleProbMap"
+ "metalToolBox::upscaleThenReflectLsMap"
+ "metalToolBox::visualizeMvf"
+ "metalToolBox::warpMvf0WithMvf1"
+ "metalToolBox::warpMvf0WithMvf1ThenAddToMvf2"
+ "metalToolBox::warpRefMeta"
+ "metalToolBox::warpRefMetaLite"
+ "mobileAssetLockReasonDownload"
+ "mobileAssetLockReasonStatus"
+ "modelPath"
+ "msrFrameSource:destination:waitForCompletion:"
+ "mv"
+ "mvCnt"
+ "mvSum"
+ "newBufferWithBytesNoCopy:length:options:deallocator:"
+ "nextFrameOpticalCenter"
+ "nextVisedOpticalCenter"
+ "no previous LS ROIs for feature extraction"
+ "normalization"
+ "notVisited in %s is NULL."
+ "numberWithUnsignedInteger:"
+ "objectAtIndex:"
+ "objectForKey:"
+ "operation"
+ "opticalCenterMvShift"
+ "opticalCenterShift"
+ "out_img"
+ "outputBufferObject"
+ "outputPortName"
+ "outputSurface"
+ "output_port"
+ "pMemory"
+ "pMemoryPlane2"
+ "padRGB"
+ "padRGB:to:"
+ "params"
+ "path"
+ "pixelBuffer is NULL"
+ "predictPrevLSLocation:usingPrevToCurrentHomography:"
+ "predictedFromPastCnt"
+ "prepareToProcess:"
+ "prevHRSurface"
+ "prevShouldRunGGDetectionClippedPixelBased"
+ "prevShouldRunGGDetectionLSBased"
+ "prevShouldRunGGDetectionLuxLevelBased"
+ "previousPreviousOutputFrame"
+ "prewarm"
+ "process"
+ "process:futureFrames:opticalCenter:futureOpticalCenter:opticalCenterMvShift:outputImgBufTMinus1:outputImgBufTMinus2:"
+ "process:outputBuf:roi:repairMask:blendMask:wRepairedY:wRepairedUV:"
+ "processHwLsMaskAndGetRoisOpticalCenter:inputFrame:prevMetaContainer:considerDist2PrevGhostWhenSort:outputMask:outputMaskTexture:isLowLight:outputArray:"
+ "processHwLsMaskNormalizedCenter:input:output:waitForComplete:"
+ "processSourceFrame:nextFrame:forwardFlow:backwardFlow:ourceFrameOpticalCenter:nextFrameOpticalCenter:opticalCenterShift:previousOutputFrame:previousPreviousOutputFrame:randomAccessMode:destinationFrame:"
+ "processSuperResolutionInputBuffer:outputBuffer:"
+ "processSuperResolutionInputBuffer:withPrevHighResolutionFrame:outputBuffer:"
+ "processWithDeghostingParams fail"
+ "processWithDeghostingParams: Invalid input deghostingParams"
+ "processWithDeghostingParams:error:"
+ "processedPixelBuffer"
+ "pruneGGList:LSBBoxList:reflectedLSBBoxList:getMatchedLS:pruneLS:pruneGG:"
+ "pruneGGList:LSList:opticalCenter:costToKeepLS:costToKeepGG:"
+ "pruneGhostList:againstReflLsList:dilation:"
+ "pruneLSBasedOnDist2Ghost:"
+ "pruneUsingTrajectoryGGList:"
+ "purgeResources"
+ "q104@0:8@16@24@32@40@48@56@64@72@80@88@96"
+ "q104@0:8{?=^{__CVBuffer}@@@@@^{__CVBuffer}}1672^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}80^i88^@96"
+ "q112@0:8@16@24@32@40@48@56@64@72@80@88@96@104"
+ "q120@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112"
+ "q144@0:8@1624@32@40@48@56^{__CVBuffer=}6472@80@88@96@104@112@120^{?=[256@]s}128B136B140"
+ "q144@0:8@16@24@32@40@48@56@64@72@80@88@96^{?=[256@]s}104@112B120124132B140"
+ "q148@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136f144"
+ "q156@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136^{?=[256@]s}144B152"
+ "q216@0:8@1624@32@40@48@56@64@72@80@88@96^{__CVBuffer=}104112^{__CVBuffer=}120^{__CVBuffer=}128^{__CVBuffer=}136^{__CVBuffer=}144^{__CVBuffer=}152^{__CVBuffer=}160^{__CVBuffer=}168^{__CVBuffer=}176^{__CVBuffer=}184@192^{?=[256@]s}200B208B212"
+ "q24@0:8^q16"
+ "q264@0:8@16@24@32@40@48@56@64^{__CVBuffer=}72^{__CVBuffer=}80^{__CVBuffer=}88^{__CVBuffer=}96^{__CVBuffer=}104^{__CVBuffer=}112^{__CVBuffer=}120@128@136^{?=[256@]s}144@152@160@168@176@184@192@200^{__CVBuffer=}208^{__CVBuffer=}216^{__CVBuffer=}224^{__CVBuffer=}232^{__CVBuffer=}240^{__CVBuffer=}248B256B260"
+ "q32@0:8@16^@24"
+ "q32@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16^@24"
+ "q32@0:8q16^@24"
+ "q32@0:8q16^q24"
+ "q40@0:8^{__CVBuffer=}16@24@32"
+ "q44@0:816@24@32B40"
+ "q48@0:8@16@2432@40"
+ "q48@0:8@16@24@32^q40"
+ "q48@0:8@16@24f32f36@40"
+ "q48@0:8^{__CVBuffer=}16@24^{__CVBuffer=}32@40"
+ "q48@0:8^{__CVBuffer=}16^{?=^{?}ii}24^{__CVBuffer=}32^{__CVBuffer=}40"
+ "q52@0:8@16@24@32@40i48"
+ "q52@0:8^{__CVBuffer=}16f24[4f]28i36i40^44"
+ "q56@0:8@16@24@32f40f44@48"
+ "q56@0:8^{__CVBuffer=}16@24@32^{__CVBuffer=}40@48"
+ "q60@0:8@16@24@32@40@48i56"
+ "q60@0:8@16@24@32@40B48@52"
+ "q64@0:8@16@24@32@404856"
+ "q64@0:8@16@24@32@40f48f52@56"
+ "q64@0:8^{__CVBuffer=}16f24f28i3236B52^@56"
+ "q68@0:8@16@24@324048i56B60B64"
+ "q68@0:8@16@24@32@40@48@56B64"
+ "q68@0:8@16@24@32@40@48@56i64"
+ "q68@0:8@16@24@32@40@48^{?=[256@]s}56B64"
+ "q72@0:816@24^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}32B40^{__CVBuffer=}44@52B60^@64"
+ "q72@0:8@16@24@3240@48@56@64"
+ "q72@0:8@16@24@32@404856@64"
+ "q72@0:8@16@24@32@40@48@56@64"
+ "q72@0:8@16@24B3236@44@52@60i68"
+ "q76@0:8@16@24@32@40@48B56@60@68"
+ "q76@0:8@16@24@32B404452@60@68"
+ "q76@0:8@16@24@32^{__CVBuffer=}40^{__CVBuffer=}485664B72"
+ "q76@0:8@16@24^{__CVBuffer=}32^{__CVBuffer=}40^{__CVBuffer=}48^{__CVBuffer=}56@64B72"
+ "q80@0:8@16@24@32@40@48@56@64@72"
+ "q80@0:8@16@24@32@40@48@56f64f68@72"
+ "q88@0:8@16@24@32@40@4856@64@7280"
+ "q88@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32^{__CVBuffer=}40@48@56@64f72f76@80"
+ "q88@0:8^{__CVBuffer=}16^{__CVBuffer=}24{CGRect={CGPoint=dd}{CGSize=dd}}3264^{__CVBuffer=}72^{__CVBuffer=}80"
+ "q88@0:8^{__CVBuffer=}16^{__CVBuffer=}24{CGRect={CGPoint=dd}{CGSize=dd}}32^{__CVBuffer=}64^{__CVBuffer=}72f80f84"
+ "q88@0:8^{__CVBuffer=}16{CGRect={CGPoint=dd}{CGSize=dd}}24f56f60[4f]64i72i76^80"
+ "q96@0:8{?=^{__CVBuffer}@@@@@^{__CVBuffer}}1672^i80^@88"
+ "readBlurredYValueAtX:Y:"
+ "readFloatAtX:Y:"
+ "readFourChannelAtX:Y:"
+ "readOneChannelAtX:Y:Channel:"
+ "readYCbCrValueAtArrayX:ArrayY:"
+ "readYCbCrValueAtX:Y:"
+ "readYValueAtX:Y:"
+ "reflectAroundCenter:"
+ "removeAllObjects"
+ "removeDuplicateRois:"
+ "removeObject:"
+ "removeObjectAtIndex:"
+ "removeObjectsInArray:"
+ "removeRedundantLS:"
+ "removeRois:thatOverlapRefRois:dilationRadius:"
+ "repairTarget:opticalCenter:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:probMap:errRescaleProbMap:prevProbMap:refinedProbMap:probMap4TrRefW:metaBuf:metaBufArray:forceToSpatial:waitForComplete:"
+ "rescaleMetaContainerBuffer:sf:sfInv:"
+ "reset"
+ "resetIntermediateVariables"
+ "resetState"
+ "resetStream:"
+ "resizeImageCmdBuf:inputTexture:withFactorX:withFactorY:outputTexture:"
+ "resourceOptions"
+ "roi"
+ "roiId"
+ "roiMv"
+ "s32@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}1624"
+ "sampleOneChannelAtX:Y:Channel:"
+ "setArea:"
+ "setBbox:"
+ "setBuf:"
+ "setBytePerPixel:"
+ "setCompressionFootprint:"
+ "setCompressionMode:"
+ "setConfidence:"
+ "setConfiguration:"
+ "setDefaultControllerConfig"
+ "setDefaultOpticalCenter:"
+ "setDefaultOpticalCenterForList:opticalCenter:"
+ "setDescriptor:"
+ "setDetectedGreenGhostInfo:"
+ "setDifferenceOfGaussianAndLumaFeature:"
+ "setDifferenceOfGaussianAndLumaFeaturePredictedLocation:"
+ "setDifferenceOfGaussianAndLumaFeatureReflection:"
+ "setDist2ghost:"
+ "setDist2opticalCenter:"
+ "setDoneKPToBBoxViaGraphTraversal:"
+ "setExtendBBox:"
+ "setFormat:"
+ "setFutureFramesToDetectionAndRepair:"
+ "setFutureInputParamsToRepair:"
+ "setImageblockWidth:height:"
+ "setIndex2RoiArray:"
+ "setInputBuffer:"
+ "setInputHeight:"
+ "setInputParamsToRepair:"
+ "setInputSurface:"
+ "setInputWidth:"
+ "setIntegralSumPixelBuffer:"
+ "setIsPredictedFromPast:"
+ "setIsReflectedLS:"
+ "setIsTracked:"
+ "setIsTrajectoryPruningPassed:"
+ "setIspTimeStamp:"
+ "setKeyPointsList:"
+ "setKpIsFromHW:"
+ "setLSIsHighRisk:"
+ "setLSOrGGBbox:"
+ "setLSTrackID:"
+ "setLSTrackingMatched:"
+ "setLSTrackingVote:"
+ "setLabel:"
+ "setLightSourceMask:"
+ "setLowSaliencyCnt:"
+ "setLsHasBeenUsedForTrackingGhost:"
+ "setLumaFeatureVector:"
+ "setLumaFeatureVectorPredictedLocation:"
+ "setLumaFeatureVectorReflection:"
+ "setMatchedLS:"
+ "setMetaContainer:"
+ "setMetaDictionary:"
+ "setModelPath:"
+ "setMv:"
+ "setMvCnt:"
+ "setMvSum:"
+ "setNextVisedOpticalCenter:"
+ "setNormalization:"
+ "setObject:atIndexedSubscript:"
+ "setObject:forKey:"
+ "setOpticalCenterMvShift:"
+ "setOutputPortName:"
+ "setOutputSurface:"
+ "setPMemory:"
+ "setPMemoryPlane2:"
+ "setParams:"
+ "setPredictedFromPastCnt:"
+ "setPrevHRSurface:"
+ "setPrevShouldRunGGDetectionClippedPixelBased:"
+ "setPrevShouldRunGGDetectionLSBased:"
+ "setPrevShouldRunGGDetectionLuxLevelBased:"
+ "setRepairTuningParams:"
+ "setResourceOptions:"
+ "setRoi:"
+ "setRoiMv:"
+ "setRoiMvForMeta:fromRoiList:"
+ "setScaleTransform:"
+ "setSkipClamp:"
+ "setStride:"
+ "setStridePlane2:"
+ "setTemporalDetectionMatched:"
+ "setTemporalDetectionVote:"
+ "setTrackFail:"
+ "setTrackID:"
+ "setTrackIDsAfterMerge:"
+ "setTrackedCnt:"
+ "setTrajectoryFromPast:"
+ "setUserInitiated:"
+ "setVisedOpticalCenter:"
+ "setup"
+ "skipClamp"
+ "sortArray:ofLength:"
+ "sortKPs:opticalCenter:"
+ "sortLsList:"
+ "sortedArrayUsingSelector:"
+ "sourceFrameOpticalCenter"
+ "startSessionWithDeghostingConfig:error:"
+ "startSessionWithQualityMode:error:"
+ "stream"
+ "stride"
+ "stridePlane2"
+ "stringByAppendingPathComponent:"
+ "stringWithCString:encoding:"
+ "summary"
+ "temporalDetectionMatched"
+ "temporalDetectionVote"
+ "textures is nil"
+ "threadExecutionWidth"
+ "total cluster is %d, bigger than limit, not all GGs are mitigated "
+ "totalExpectedBytes"
+ "totalWrittenBytes"
+ "trackFail"
+ "trackID"
+ "trackIDsAfterMerge"
+ "trackMeta:refMeta:currMaxTrackId:"
+ "trackSessionId"
+ "trackedCnt"
+ "trajectoryFromPast"
+ "tuningParamDict"
+ "unpackIspLsMaskAndRoisForNextFrameLiteWithFrameData:futureOpticalCenter:outputFutureFrameCnt:outputFutureMetaBuf:"
+ "unpackIspLsMaskAndRoisForNextFrameWithFrameData:futureOpticalCenter:currFrameMetaContainer:outputFutureFrameCnt:outputMTLBuffer:"
+ "updateDoGAndLumaFeaturesWithMetalBuffers:"
+ "updateMetaContainerBuffer:withDetectedROI:isLowLight:opticalCenter:opticalCenterShift:"
+ "updateNewRoiPixFea:withRefPixFea:"
+ "updatePrevLSDoGAndLumaFeaturesWithMetalBuffers:"
+ "updateRepairedRefYUVInput:opticalCenter:prob:errRescaleProb:prevProb:refinedProb:probMap4TrRefW:frRef0:frRef1:nextFrame:nextFrameMvf:nextFrameMvfBuf:nextOpticalCenter:inputBuf:probBuf:errRescaleProbBuf:prevProbBuf:refinedProbBuf:probMap4TrRefWBuf:frRef0Buf:frRef1Buf:nextFrameBuf:metaBuf:metaBufArray:forceToSpatial:waitForComplete:"
+ "v176@0:8{?=fffffI}16"
+ "v188@0:8{?=iiiiiifffiifiiii{?=ffffffff}{?=iiffffffffffffff}{?=fff}}16"
+ "v20@0:8C16"
+ "v24@0:8*16"
+ "v24@0:816"
+ "v24@0:8@?16"
+ "v24@0:8^{?=@@@@@@@@@@@@@@iiiiiiii}16"
+ "v24@0:8^{?=^{?}ii}16"
+ "v24@0:8^{?=fff}16"
+ "v24@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16"
+ "v24@0:8^{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "v24@0:8^{__IOSurface=}16"
+ "v24@0:8^{e5rt_execution_stream=}16"
+ "v24@?0q8@\"NSError\"16"
+ "v28@0:816i20i24"
+ "v28@0:8^f16I24"
+ "v28@0:8f16i20i24"
+ "v32@0:816"
+ "v32@0:8@1624"
+ "v32@0:8@16^@24"
+ "v32@0:8@16^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}24"
+ "v32@0:8@16f24f28"
+ "v32@0:8@16s24f28"
+ "v32@0:8C16i20i24c28"
+ "v32@0:8^16^24"
+ "v32@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16@24"
+ "v32@0:8q16@?24"
+ "v40@0:8@16s2428i36"
+ "v40@0:8^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}16^{?=sssffffII[256{?=ffffffff}]B[256i][256s][256i][256f][256][256][256][256I][256I][256I][256I][256I][256I][256I][256I][256I][256I][256i][256i][256I][256][256][256I][256I][256i][256i][256i][256I][256I][256i][256f][256I][256I][256I][256I][256f][256f][256i][256i][256i][256i][256I][256][256][256i][256i][256I][256]f}24^i32"
+ "v44@?0@\"MAAutoAssetSelector\"8B16@\"NSURL\"20@\"MAAutoAssetStatus\"28@\"NSError\"36"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8@16@24B3236f44"
+ "v48@0:8^@16^@2432f40f44"
+ "v48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
+ "v52@0:8^@16^@24^32B40B44B48"
+ "v60@0:8@16@24@3240^{?=@@@@@@@@@@@@@@iiiiiiii}48i56"
+ "v60@0:8@16@24f3236^{?=@@@@@@@@@@@@@@iiiiiiii}44i52f56"
+ "v80@0:816"
+ "v80@0:8{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}}16"
+ "v84@0:8@16{?=[3]}24^{?=@@@@@@@@@@@@@@iiiiiiii}72i80"
+ "videoDeghostingMetalLib.metallib"
+ "video_deghosting-v2"
+ "visedOpticalCenter"
+ "vsrnet_4x.mlmodelc/model.mil"
+ "warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toHighResBufferTexture:"
+ "warpBlendImageRGB"
+ "warpRoisUsingMv:"
+ "warpTrackingRefProbMap:refSpaProbMap:refReflLs:mvf:metaBuf:metaBufArray:waitForComplete:"
+ "writeFloat:X:Y:"
+ "writeValue:X:Y:"
+ "writeValue:X:Y:Channel:"
+ "{?=\"bufArray\"[256@\"<MTLBuffer>\"]\"clusterCnt\"s}"
+ "{?=\"data\"^v\"reserved\"^v\"dim\"[4Q]\"stride\"[4Q]\"width\"Q\"height\"Q\"channels\"Q\"batch_number\"Q\"sequence_length\"Q\"stride_width\"Q\"stride_height\"Q\"stride_channels\"Q\"stride_batch_number\"Q\"stride_sequence_length\"Q\"storage_type\"i}"
+ "{?=\"frameDataArray\"^{?}\"size\"i\"validCount\"i}"
+ "{?=\"internalCfg\"{?=\"clipThreshold\"i\"patchSize\"i\"antiFlareSize\"i\"simpleRefList\"C\"firstFrameReprocess\"C\"cpuDetection\"C\"baselineMitigation\"C\"enableColorMask\"C\"verbose\"C\"cpuMitigation\"C\"initGGarray\"^{__CFArray}}\"externalCfg\"{?=\"lightMode\"i\"homographyType\"i\"detectionType\"i\"tempPatchMode\"i\"frameDelay\"i\"drawBoundingBox\"C\"noMetaData\"C\"backGroundDetection\"C\"LSGatingEnabled\"C\"luxLevelGating\"C\"clippedPixelGatingEnabled\"C}}"
+ "{?=\"lightSourceGatingThresholdON\"i\"lightSourceGatingThresholdOFF\"i\"lightSourceSelectionCntLimitNew\"i\"lightSourceSelectionCntLimitAll\"i\"luxLevelGatingThresholdON\"i\"luxLevelGatingThresholdOFF\"i\"lightSourceBoxSizeThreshold\"f\"searchRangeBase\"f\"searchRangeBaseForPreprocessing\"f\"maxAllowedSizeBBox\"i\"maxAllowedOpticalCenterOffset\"i\"costRescaleWhenOpticalCenterIsAvailable\"f\"b4MergeGhostCntSoftGatingTh\"i\"b4MergeGhostCntHardGatingTh\"i\"kpCntSoftGatingTh\"i\"kpCntHardGatingTh\"i\"colorScore\"{?=\"hueLowerRange\"f\"hueUpperRange\"f\"hueThreshold\"f\"saturationLowerThreshold\"f\"saturationUpperThreshold\"f\"valueLowerThreshold\"f\"valueUpperThreshold\"f\"greenDilationNormalizedRadius\"f}\"tempDetect\"{?=\"minVote\"i\"lightSourceMinVote\"i\"searchRadiusMin\"f\"searchRadiusSlope\"f\"lumaDiffThreshold\"f\"motionDiffThreshold\"f\"colorContrastDiffThreshold\"f\"pixFeaMatchThreshold\"f\"kpIsGhostColorThreshold\"f\"kpIsGhostLumaThreshold\"f\"kpIsGhostContrastThreshold\"f\"kpIsGhostBlobContrastThreshold\"f\"kpIsGhostMotionThreshold\"f\"kpIsGhostColorThresholdHigh\"f\"kpIsGhostLumaThresholdHigh\"f\"kpIsGhostMotionThresholdHigh\"f}\"repairParams\"{?=\"repairTargetArea\"f\"repairTargetGhostCntLo\"f\"repairTargetGhostCntHi\"f}}"
+ "{?=\"location\"\"KPScore\"f\"colorScore\"f\"confidence\"f\"pixelValueYUVNormalized\"\"localMotionScore\"f\"GGProb\"f\"pixelFeature\"\"pixelFeatureLen\"I\"KPLSDiffVector\"\"trajectoryFromPast\"\"trajectoryToFuture\"}"
+ "{?=\"repairTargetArea\"f\"repairTargetGhostCntLo\"f\"repairTargetGhostCntHi\"f}"
+ "{?=\"width\"i\"height\"i}"
+ "{?=fffffI}16@0:8"
+ "{?=iiiiiifffiifiiii{?=ffffffff}{?=iiffffffffffffff}{?=fff}}16@0:8"
+ "{?={?=iiiCCCCCCC^{__CFArray}}{?=iiiiiCCCCCC}}16@0:8"
+ "{CGPoint=\"x\"d\"y\"d}"
+ "{CGPoint=dd}16@0:8"
+ "{CGRect=\"origin\"{CGPoint=\"x\"d\"y\"d}\"size\"{CGSize=\"width\"d\"height\"d}}"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}16@0:8"
+ "{RepairTileBlendingParams=\"wRepairedY\"f\"wRepairedUV\"f}"
+ "{RepairTileConfiguration=\"size\"}"
- "@\"SRNet\""
- "@36@0:8q16@24B32"
- "@56@0:8@16@24@32@40@48"
- "B48@0:8^{__CVBuffer=}16^{__CVBuffer=}24^{__CVBuffer=}32@?40"
- "Error ! Failed to bind the first\n"
- "Error ! Failed to bind the output buffer\n"
- "Error ! Failed to bind the second\n"
- "Error Invalid Scale Factor = %ld"
- "Error! destination channel must be %ld"
- "TB,N,V_bicubicOnly"
- "TB,N,V_residueOnly"
- "TB,N,V_useMPS"
- "Tf,N,V_residueOnlyFillValue"
- "_bicubicOnly"
- "_espressoFileName"
- "_residueOnly"
- "_residueOnlyFillValue"
- "_warpBlendWith4x4ShuffleRGBKernel"
- "bicubicOnly"
- "bindBuffer:forBlob:"
- "convertToYUV:attachment:"
- "encodeWarpBlendWithSpaceToDepthToCommandBuffer:source:scaleFactor:withLowResFlow:withBicubicUpscaled:withErrorMask:destination:"
- "hr_prev"
- "i32@0:8^{__CVBuffer=}16r*24"
- "initMPSWithModelName:usage:"
- "initWithSourceFrame:previousFrame:previousOutputFrame:opticalFlow:destinationFrame:"
- "initWithUsage:espressoFileName:useMPS:"
- "iosurface is nil, adjust color failed"
- "isrnet_x4"
- "landscape1024x1024"
- "lr_curr"
- "output"
- "residueOnly"
- "residueOnlyFillValue"
- "scaleLowResolutionFrame:withPrevHighResolutionFrame:to:callback:"
- "setBicubicOnly:"
- "setResidueOnly:"
- "setResidueOnlyFillValue:"
- "setUseMPS:"
- "useMPS"
- "vsrnet_x4"
- "warpBlendBufferRGBTexture:scaleFactor:withLowResFlowTexture:withBicubicUpscaledTexture:withErrorMaskTexture:toShuffledBufferTexture:"
- "warpBlendImageWith4x4ShuffleRGB"

```
