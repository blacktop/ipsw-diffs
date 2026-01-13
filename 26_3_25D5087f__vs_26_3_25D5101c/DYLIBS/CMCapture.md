## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/Versions/A/CMCapture`

```diff

-665.80.6.0.0
-  __TEXT.__text: 0x525714
+665.80.7.0.1
+  __TEXT.__text: 0x525f04
   __TEXT.__auth_stubs: 0x3f80
   __TEXT.__objc_methlist: 0x24d8c
   __TEXT.__const: 0x142c68
-  __TEXT.__cstring: 0x8be51
-  __TEXT.__oslogstring: 0xb6ae5
+  __TEXT.__cstring: 0x8bf3b
+  __TEXT.__oslogstring: 0xb6ed4
   __TEXT.__gcc_except_tab: 0x1c0c
   __TEXT.__dlopen_cstrs: 0x236
   __TEXT.__ustring: 0x10
   __TEXT.__unwind_info: 0x9688
   __TEXT.__objc_classname: 0x4dc4
-  __TEXT.__objc_methname: 0x82561
-  __TEXT.__objc_methtype: 0xed3b
-  __TEXT.__objc_stubs: 0x33b60
-  __DATA_CONST.__got: 0x5ca8
-  __DATA_CONST.__const: 0x5b70
+  __TEXT.__objc_methname: 0x82604
+  __TEXT.__objc_methtype: 0xed4a
+  __TEXT.__objc_stubs: 0x33bc0
+  __DATA_CONST.__got: 0x5cb0
+  __DATA_CONST.__const: 0x5b90
   __DATA_CONST.__objc_classlist: 0x1190
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x308
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xffd8
+  __DATA_CONST.__objc_selrefs: 0xfff0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x1080
   __DATA_CONST.__objc_arraydata: 0x14c0
   __AUTH_CONST.__auth_got: 0x1fd0
-  __AUTH_CONST.__const: 0x5340
+  __AUTH_CONST.__const: 0x5360
   __AUTH_CONST.__cfstring: 0x3d400
-  __AUTH_CONST.__objc_const: 0x682c8
+  __AUTH_CONST.__objc_const: 0x68328
   __AUTH_CONST.__objc_intobj: 0x36f0
   __AUTH_CONST.__objc_arrayobj: 0x1128
   __AUTH_CONST.__objc_doubleobj: 0x1e0
   __AUTH_CONST.__objc_floatobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x1ea0
-  __DATA.__objc_ivar: 0x7c98
+  __DATA.__objc_ivar: 0x7ca4
   __DATA.__data: 0x263c
   __DATA.__common: 0x1690
   __DATA.__bss: 0x1330

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/Versions/A/FrontBoardServices
+  - /System/Library/PrivateFrameworks/ModelManagerServices.framework/Versions/A/ModelManagerServices
   - /System/Library/PrivateFrameworks/Quagga.framework/Versions/A/Quagga
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/Versions/A/RunningBoardServices
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FAFB919F-7A8D-3143-85BE-887688AB397B
-  Functions: 22522
-  Symbols:   51534
-  CStrings:  48938
+  UUID: D41B30C4-1F79-32F0-A754-44A83B1E2209
+  Functions: 22528
+  Symbols:   51556
+  CStrings:  48959
 
Symbols:
+ -[BWMemoryPool _maximizeAvailableSystemMemory]
+ -[BWMemoryPool _releaseModelManagerAssertion]
+ -[FigCaptureSourceStreamsContainer zoomFactorsForDepthWithMaxContinuousZoomForDepthDataDelivery:]
+ GCC_except_table36
+ OBJC_IVAR_$_BWGraph._deferredPrepareActiveNode
+ OBJC_IVAR_$_BWGraph._deferredPrepareState
+ OBJC_IVAR_$_BWMemoryPool._modelManagerAssertion
+ _OBJC_CLASS_$_MMAssertion
+ ___45-[BWMemoryPool _releaseModelManagerAssertion]_block_invoke
+ ___46-[BWMemoryPool _maximizeAvailableSystemMemory]_block_invoke
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ __block_literal_global.99
+ _objc_msgSend$acquireWithCompletionHandler:
+ _objc_msgSend$initWithPolicy:description:
+ _objc_msgSend$invalidateWithCompletionHandler:
- -[FigCaptureSourceStreamsContainer zoomFactorsForDepth]
- GCC_except_table40
CStrings:
+ "-[BWMemoryPool _maximizeAvailableSystemMemory]"
+ "-[BWMemoryPool _maximizeAvailableSystemMemory]_block_invoke"
+ "-[BWMemoryPool _releaseModelManagerAssertion]"
+ "-[BWMemoryPool _releaseModelManagerAssertion]_block_invoke"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CMCaptureLocal/CMCaptureLocalSessionController.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CameraViewfinder/FigCaptureSessionObserver.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureMetadataUtilities.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSession.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionPipelines.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSource.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSourceBackingsProvider.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/CMCaptureUserNotification.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureCommon.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unknown flip %i"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unsupported rotation of %d degrees"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: rotationDegrees (%d) is invalid, must be 0/90/180/270. Returning kFigExifOrientation_0RowTop0ColLeft (%d)"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCapturePixelFormatUtilities.m %s: Unexpected plist value for a pixel format type: %@"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Cannot look up key.\n"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Not adding key.\n"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Returning 0."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Key (%s) has already been registered. Not adding key.\n"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: keyspace not found, has no name"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigRemoteQueue/FigRemoteQueue.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWDeviceMotionActivityDetector.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigCaptureDeviceVendor.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureDevice.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureStream.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFrameStatistics.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWGraph.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing noise reduction and sharpening parameters"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing portType"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing sensorIDDictionary"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing MBNR parameters for type '%d' and gain '%.1f'"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing noise reduction and sharpening parameters for type '%d' and gain '%.1f'"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing PortType"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing cameraInfo"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDDictionary"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDString"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil input for %@"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil portType for %@"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorController.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@ took %lld ms"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@..."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Couldn't find Deep Fusion HDR EV0 count for EIT '%f': %@"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Missing portType"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then Long-Without-Sphere threshold: %@."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then SIFR-Main threshold: %@."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Motion and focus scores RFS is specified, but weights are missing: %@."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. SIFR-Main threshold should be smaller then Long-Without-Sphere threshold: %@."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWVideoFormat.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWAudioSourceNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWCameraInfoMetadataNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDeferredCaptureController.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDepthConverterNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFrameRateGovernorNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWIrisStagingNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWMultiStreamCameraSourceNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWOverCaptureSmartStyleApplyNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderController.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderManager.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPiecemealEncodingNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewTimeMachineSinkNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSensitiveContentAnalyzerSinkNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageCoordinatorNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageScalerNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStreamingFilterNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSynchronizerNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVISNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVideoPIPOverlayNode.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWAggdDataReporter.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWCoreAnalyticsReporter.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFencedAnimationQueue.m %s: Fenced animation queue wait timeout occurred - not queuing animation"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFigVideoCaptureSynchronizedStreamsGroup.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWStillImageMetadataUtilities.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWUtilities.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Autofocus/FigSampleBufferProcessor_Autofocus.m"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: %d motion-related log messages filtered out (max of 1/s displayed from FigCoreMotionDelegate)"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration fused vector is computed incorrectly"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration vector is computed incorrectly"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Allocation error when retrieving motion data"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Closest motion sample for timestamp %f has timestamp %f, difference %f\n"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not find motion sample to get Quaternion.\n"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not lock the ringMutex\n"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Frame timestamp is %f, Sample timestamps in the ring buffer are from %f to %f\n"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Gravity is computed incorrectly"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Potential missing three motion samples: new timestamp %f, latest timestamp %f\n"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: no data semaphore was available to wait on"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on portIndex %d"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f]."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find motion sample to get Quaternion."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming default value of 1.0"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming value of %f"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Frame timestamp is from %f to %f, Sample timestamps in the ring buffer are from %f to %f, get %d motion samples"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Motion Hardware Unavailable - prototype hardware detected"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: No valid baseZoomFactor found, will proceed with a value of 1.0f."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Time interval %f is not positive"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Too many motion samples for the array"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Using default focus characterization entry because an entry corresponding to the original requested values was not found."
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: invalid micronsPerPixel value %f"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed computing scaling factor"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed extracting metadata"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Unsupported sag removal method"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: sagPosition memory allocation failed"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Could not parse motion data from ISP due to error: %d"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Failed to allocate and initialize VISRotationCorrectionEstimator"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Height is missing from visInputPixelBufferAttributes"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData from metadataDict"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PinholeCameraFocalLength in metadataDict"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PortType from metadataDict"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSize for portType: %@"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSizeInMicrons for port %@"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing portType in metadataDict"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: No motion samples for this frame. Skipping processing"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Overscan is 0 or less. l:%f r:%f t:%f b:%f"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Timestamp %f is earlier than previous sample %f"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Width is missing from visInputPixelBufferAttributes"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: focalLength is null"
+ "/AppleInternal/Library/BuildRoots/4~CGC4ugCxigRVQwNV4mwZk17wwQXZsgzmT3On8KQ/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: pole must be between 0 and 1"
+ "19:59:35"
+ "<<<< BWGraph >>>> %s: <%p> A node with pointer <0x%lx> was flagged as still executing deferred prepare but wasn't found in this graph's node list. This may be a BWGraph bug"
+ "<<<< BWGraph >>>> %s: <%p> Deferred prepare is still active which prevents graph start, but no single actively preparing node was identified. The deferred prepare thread may be stuck on non-node work or transitioning between nodes."
+ "<<<< BWGraph >>>> %s: <%p> Deferred prepare is still pending which prevents graph start but hasn't asynchronously started or canceled."
+ "<<<< BWGraph >>>> %s: <%p> Graph timeout was not attributed to any individual nodes."
+ "<<<< BWGraph >>>> %s: <%p> Node <%p, %@, %@, %{public}@> is still executing deferred prepare and may have caused a graph start timeout."
+ "<<<< BWGraph >>>> %s: <%p> Sink node <%p, %@, %{public}@> is %{public}@ which prevents graph from %@, but is blocked from %@ due to the following input states:"
+ "<<<< BWMemoryPool >>>> %s: Creating Model Manager assertion"
+ "<<<< BWMemoryPool >>>> %s: Invalidating Model Manager assertion %p"
+ "<<<< BWMemoryPool >>>> %s: Model Manager assertion acquired"
+ "<<<< BWMemoryPool >>>> %s: Model Manager assertion already present, skipping acquire"
+ "<<<< BWMemoryPool >>>> %s: Model Manager assertion invalidated %p"
+ "@\"MMAssertion\""
+ "Jan  4 2026"
+ "LastShownBuild:BWGraph.m:3269"
+ "LastShownBuild:BWGraph.m:3348"
+ "LastShownBuild:BWGraph.m:3362"
+ "LastShownBuild:BWGraph.m:3365"
+ "LastShownBuild:FigCaptureSession.m:16609"
+ "LastShownBuild:FigCaptureSession.m:18095"
+ "LastShownBuild:FigCaptureSession.m:18948"
+ "LastShownBuild:FigCaptureSession.m:22439"
+ "LastShownBuild:FigCaptureSession.m:22474"
+ "LastShownBuild:FigCaptureSourceBackingsProvider.m:2522"
+ "LastShownDate:BWGraph.m:3269"
+ "LastShownDate:BWGraph.m:3348"
+ "LastShownDate:BWGraph.m:3362"
+ "LastShownDate:BWGraph.m:3365"
+ "LastShownDate:FigCaptureSession.m:16609"
+ "LastShownDate:FigCaptureSession.m:18095"
+ "LastShownDate:FigCaptureSession.m:18948"
+ "LastShownDate:FigCaptureSession.m:22439"
+ "LastShownDate:FigCaptureSession.m:22474"
+ "LastShownDate:FigCaptureSourceBackingsProvider.m:2522"
+ "_deferredPrepareActiveNode"
+ "_deferredPrepareState"
+ "_modelManagerAssertion"
+ "acquireWithCompletionHandler:"
+ "description=CameraCapture-665.80.7.0.1"
+ "initWithPolicy:description:"
+ "invalidateWithCompletionHandler:"
+ "v16@?0@\"NSError\"8"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CMCaptureLocal/CMCaptureLocalSessionController.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CameraViewfinder/FigCaptureSessionObserver.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureMetadataUtilities.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSession.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSession/FigCaptureSessionPipelines.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSource.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/CaptureSource/FigCaptureSourceBackingsProvider.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/CMCaptureUserNotification.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureCommon.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unknown flip %i"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: Unsupported rotation of %d degrees"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCaptureGeometryUtilities.m %s: rotationDegrees (%d) is invalid, must be 0/90/180/270. Returning kFigExifOrientation_0RowTop0ColLeft (%d)"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigCapturePixelFormatUtilities.m %s: Unexpected plist value for a pixel format type: %@"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Cannot look up key.\n"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Not adding key.\n"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Invalid FigFlatDictionaryKeySpace. Returning 0."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: Key (%s) has already been registered. Not adding key.\n"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigFlatDictionary/FigFlatDictionaryKey.c %s: keyspace not found, has no name"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Common/FigRemoteQueue/FigRemoteQueue.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWDeviceMotionActivityDetector.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigCaptureDeviceVendor.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureDevice.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFigVideoCaptureStream.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWFrameStatistics.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWGraph.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing noise reduction and sharpening parameters"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing portType"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Missing sensorIDDictionary"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing MBNR parameters for type '%d' and gain '%.1f'"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWNoiseReductionAndSharpeningParameters.m %s: Port type '%@' is missing noise reduction and sharpening parameters for type '%d' and gain '%.1f'"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing PortType"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing cameraInfo"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDDictionary"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWSensorConfiguration.m %s: Missing sensorIDString"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil input for %@"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessingPlan.m %s: Attempting to add nil portType for %@"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorController.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@ took %lld ms"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWStillImageProcessorCoordinator.m %s: Deallocating %{public}@..."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Couldn't find Deep Fusion HDR EV0 count for EIT '%f': %@"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Missing portType"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then Long-Without-Sphere threshold: %@."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Low-Light threshold should be smaller then SIFR-Main threshold: %@."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. Motion and focus scores RFS is specified, but weights are missing: %@."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWUBCaptureParameters.m %s: Unexpected UB capture parameters. SIFR-Main threshold should be smaller then Long-Without-Sphere threshold: %@."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Base/BWVideoFormat.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWAudioSourceNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWCameraInfoMetadataNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDeferredCaptureController.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWDepthConverterNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWFrameRateGovernorNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWIrisStagingNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWMultiStreamCameraSourceNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWOverCaptureSmartStyleApplyNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderController.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderManager.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPhotoEncoderNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPiecemealEncodingNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWPreviewTimeMachineSinkNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSensitiveContentAnalyzerSinkNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageCoordinatorNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStillImageScalerNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWStreamingFilterNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWSynchronizerNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVISNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Nodes/BWVideoPIPOverlayNode.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWAggdDataReporter.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWCoreAnalyticsReporter.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFencedAnimationQueue.m %s: Fenced animation queue wait timeout occurred - not queuing animation"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWFigVideoCaptureSynchronizedStreamsGroup.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWStillImageMetadataUtilities.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/CMCapture/Sources/Graph/Utilities/BWUtilities.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/Autofocus/FigSampleBufferProcessor_Autofocus.m"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: %d motion-related log messages filtered out (max of 1/s displayed from FigCoreMotionDelegate)"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration fused vector is computed incorrectly"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Acceleration vector is computed incorrectly"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Allocation error when retrieving motion data"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Closest motion sample for timestamp %f has timestamp %f, difference %f\n"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not find motion sample to get Quaternion.\n"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Could not lock the ringMutex\n"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Frame timestamp is %f, Sample timestamps in the ring buffer are from %f to %f\n"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Gravity is computed incorrectly"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: Potential missing three motion samples: new timestamp %f, latest timestamp %f\n"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigCoreMotionDelegate.m %s: no data semaphore was available to wait on"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: %d motion-related log messages filtered out (max of 1/s displayed from FigMotionProcessingUtilities)"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall sample for the given timestamp on portIndex %d"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find Hall samples in given time range [%f, %f]. Use the closest Hall sample in actual time range [%f, %f]."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find a motion sample within %fms of the current frame. Frame timestamp is %f, sample timestamps in the ring buffer are from %f to %f, latestTimeDifference %f"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find motion sample to get Quaternion."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Could not find the closest motion sample index in the ring buffer for the frame timestamp (%f)."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP Hall samples"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Extracting only the first %d ISP motion samples"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming default value of 1.0"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Failed computing scaling factor from ISP crop - assuming value of %f"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Frame timestamp is from %f to %f, Sample timestamps in the ring buffer are from %f to %f, get %d motion samples"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Motion Hardware Unavailable - prototype hardware detected"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: No valid baseZoomFactor found, will proceed with a value of 1.0f."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Quaternion pointer is null!"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Time interval %f is not positive"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Too many motion samples for the array"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Unsupported Hall data version %d"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Using default focus characterization entry because an entry corresponding to the original requested values was not found."
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after Hall sample timestamp difference is close to 0.0f!"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: Warning! The before and after motion sample timestamp difference is close to 0.0f!"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: interpolateQuaternionsByAngle: delta quaternion w %f is larger than 1"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/MotionProcessing/FigMotionProcessingUtilities.c %s: invalid micronsPerPixel value %f"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed computing scaling factor"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Failed extracting metadata"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: Unsupported sag removal method"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/PreviewStabilization/BWPreviewGyroStabilization.m %s: sagPosition memory allocation failed"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Could not parse motion data from ISP due to error: %d"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Failed to allocate and initialize VISRotationCorrectionEstimator"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Height is missing from visInputPixelBufferAttributes"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing ISPMotionData from metadataDict"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PinholeCameraFocalLength in metadataDict"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing PortType from metadataDict"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSize for portType: %@"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing pixelSizeInMicrons for port %@"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Missing portType in metadataDict"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: No motion samples for this frame. Skipping processing"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Overscan is 0 or less. l:%f r:%f t:%f b:%f"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Timestamp %f is earlier than previous sample %f"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: Width is missing from visInputPixelBufferAttributes"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: focalLength is null"
- "/AppleInternal/Library/BuildRoots/4~CDy0ugBk_WWRtauCZvJGKWzAxLrvqv_qC_nqDVk/Library/Caches/com.apple.xbs/Sources/CameraCapture/VideoProcessors/VideoStabilizationX/Utilities/GVSOverscanPredictor.m %s: pole must be between 0 and 1"
- "02:22:02"
- "<<<< BWGraph >>>> %s: <%p> Failed to attribute graph timeout to one or more offenders"
- "<<<< BWGraph >>>> %s: <%p> Sink node <%p, %@, %{public}@> is %{public}@ which prevents graph from %@, but is blocked from stopping due to the following input states:"
- "Dec  5 2025"
- "LastShownBuild:BWGraph.m:3249"
- "LastShownBuild:BWGraph.m:3325"
- "LastShownBuild:BWGraph.m:3328"
- "LastShownBuild:BWGraph.m:3342"
- "LastShownBuild:FigCaptureSession.m:16606"
- "LastShownBuild:FigCaptureSession.m:18089"
- "LastShownBuild:FigCaptureSession.m:18945"
- "LastShownBuild:FigCaptureSession.m:22436"
- "LastShownBuild:FigCaptureSession.m:22471"
- "LastShownBuild:FigCaptureSourceBackingsProvider.m:2519"
- "LastShownDate:BWGraph.m:3249"
- "LastShownDate:BWGraph.m:3325"
- "LastShownDate:BWGraph.m:3328"
- "LastShownDate:BWGraph.m:3342"
- "LastShownDate:FigCaptureSession.m:16606"
- "LastShownDate:FigCaptureSession.m:18089"
- "LastShownDate:FigCaptureSession.m:18945"
- "LastShownDate:FigCaptureSession.m:22436"
- "LastShownDate:FigCaptureSession.m:22471"
- "LastShownDate:FigCaptureSourceBackingsProvider.m:2519"
- "description=CameraCapture-665.80.6"

```
