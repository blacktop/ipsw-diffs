## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-764.42.8.0.0
-  __TEXT.__text: 0x683d14
-  __TEXT.__objc_methlist: 0x3e198
+764.60.7.0.2
+  __TEXT.__text: 0x684b50
+  __TEXT.__objc_methlist: 0x3e2a8
   __TEXT.__const: 0x151800
-  __TEXT.__cstring: 0xb0381
-  __TEXT.__oslogstring: 0x54cfb
-  __TEXT.__gcc_except_tab: 0x3c74
+  __TEXT.__cstring: 0xb04be
+  __TEXT.__oslogstring: 0x54e03
+  __TEXT.__gcc_except_tab: 0x3c7c
   __TEXT.__ustring: 0x6ee
   __TEXT.__dlopen_cstrs: 0x7c9
-  __TEXT.__unwind_info: 0x182b0
+  __TEXT.__unwind_info: 0x18300
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11920
+  __DATA_CONST.__const: 0x11b58
   __DATA_CONST.__objc_classlist: 0x2048
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18e48
+  __DATA_CONST.__objc_selrefs: 0x18ed0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x1e78
   __DATA_CONST.__objc_arraydata: 0x3cd8
-  __DATA_CONST.__got: 0x79a8
-  __AUTH_CONST.__const: 0x4b40
-  __AUTH_CONST.__cfstring: 0x532e0
-  __AUTH_CONST.__objc_const: 0xb1658
+  __DATA_CONST.__got: 0x79b0
+  __AUTH_CONST.__const: 0x4b60
+  __AUTH_CONST.__cfstring: 0x53300
+  __AUTH_CONST.__objc_const: 0xb18c0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x6e58
   __AUTH_CONST.__objc_arrayobj: 0x2d90

   __AUTH_CONST.__objc_dictobj: 0x17e8
   __AUTH_CONST.__auth_got: 0x2f28
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xcbf4
-  __DATA.__data: 0x930
+  __DATA.__objc_ivar: 0xcc2c
+  __DATA.__data: 0x730
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x1860
   __DATA_DIRTY.__objc_data: 0x141e0
-  __DATA_DIRTY.__data: 0x66d0
+  __DATA_DIRTY.__data: 0x68d0
   __DATA_DIRTY.__bss: 0x1260
   __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 39434
-  Symbols:   59488
-  CStrings:  22046
+  Functions: 39476
+  Symbols:   59520
+  CStrings:  22053
 
Symbols:
+ -[BWCameraStreamingMonitor _updateActiveClientSessionsForSessionID:clientSession:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:]
+ -[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:completionHandler:]
+ -[BWCinematicFramingNode layoutMonitor:didUpdateLayout:]
+ -[BWCinematographyObjectTrackingNode _visCropFactorFromMetadata:]
+ -[BWCinematographyObjectTrackingNode initWithCaptureDevice:tuningParameters:inferenceScheduler:frameRate:sourceBufferDimensions:prepareCinematographyOnInit:]
+ -[BWDeskCamNode realtimeStabilizationForDeskViewEnabled]
+ -[BWDeskCamNode setRealtimeStabilizationForDeskViewEnabled:]
+ -[BWMovieFileOutputAnalyticsPayload averageLuxValue]
+ -[BWMovieFileOutputAnalyticsPayload maxLuxValue]
+ -[BWMovieFileOutputAnalyticsPayload minLuxValue]
+ -[BWMovieFileOutputAnalyticsPayload setAverageLuxValue:]
+ -[BWMovieFileOutputAnalyticsPayload setMaxLuxValue:]
+ -[BWMovieFileOutputAnalyticsPayload setMinLuxValue:]
+ -[BWSmartCropNode _updateOutputStabilizationMetadata:]
+ -[CMCaptureLocalSessionVideoConfiguration setSupportsRealtimeStabilizationForCenterStage:]
+ -[CMCaptureLocalSessionVideoConfiguration setSupportsRealtimeStabilizationForDeskView:]
+ -[CMCaptureLocalSessionVideoConfiguration supportsRealtimeStabilizationForCenterStage]
+ -[CMCaptureLocalSessionVideoConfiguration supportsRealtimeStabilizationForDeskView]
+ -[FigCaptureSourceConfiguration realtimeStabilizationForCenterStageEnabled]
+ -[FigCaptureSourceConfiguration realtimeStabilizationForDeskViewEnabled]
+ -[FigCaptureSourceConfiguration setRealtimeStabilizationForCenterStageEnabled:]
+ -[FigCaptureSourceConfiguration setRealtimeStabilizationForDeskViewEnabled:]
+ -[FigCaptureVideoDataSinkConfiguration realtimeStabilizationForCenterStageEnabled]
+ -[FigCaptureVideoDataSinkConfiguration realtimeStabilizationForDeskViewEnabled]
+ -[FigCaptureVideoDataSinkConfiguration setRealtimeStabilizationForCenterStageEnabled:]
+ -[FigCaptureVideoDataSinkConfiguration setRealtimeStabilizationForDeskViewEnabled:]
+ GCC_except_table205
+ GCC_except_table239
+ GCC_except_table287
+ GCC_except_table416
+ GCC_except_table85
+ _J510_J511
+ _OBJC_IVAR_$_BWCinematicFramingNode._activeDisplayRegion
+ _OBJC_IVAR_$_BWCinematicFramingNode._activeDisplayRegionLock
+ _OBJC_IVAR_$_BWCinematicFramingNode._registeredAsDisplayLayoutObserver
+ _OBJC_IVAR_$_BWCinematographyObjectTrackingNode._sourceBufferDimensions
+ _OBJC_IVAR_$_BWDeskCamNode._realtimeStabilizationForDeskViewEnabled
+ _OBJC_IVAR_$_BWLensSmudgeDetection._lensSmudgeData
+ _OBJC_IVAR_$_BWMovieFileOutputAnalyticsPayload._averageLuxValue
+ _OBJC_IVAR_$_BWMovieFileOutputAnalyticsPayload._maxLuxValue
+ _OBJC_IVAR_$_BWMovieFileOutputAnalyticsPayload._minLuxValue
+ _OBJC_IVAR_$_BWQuickTimeMovieFileSinkNode._luxLevelStats
+ _OBJC_IVAR_$_CMCaptureLocalSessionVideoConfiguration._supportsRealtimeStabilizationForCenterStage
+ _OBJC_IVAR_$_CMCaptureLocalSessionVideoConfiguration._supportsRealtimeStabilizationForDeskView
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._realtimeStabilizationForCenterStageEnabled
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._realtimeStabilizationForDeskViewEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkConfiguration._realtimeStabilizationForCenterStageEnabled
+ _OBJC_IVAR_$_FigCaptureVideoDataSinkConfiguration._realtimeStabilizationForDeskViewEnabled
+ ___122-[BWPhotonicEngineNodeResourceCoordinator purgeProcessorAndSharedExternalMemoryResourceBackendMemoryIfNeededWithSettings:]_block_invoke
+ ___135-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:completionHandler:]_block_invoke
+ ___block_descriptor_105_e8_32o40o48o56o64b_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ _captureSession_updateInflightConfigurationWithPreviewSinkPropertyForKey
+ _cmclsc_setSessionConfiguration
+ _cs_activePortTypesExcludingSuspendedOmahaDevices
+ _cs_configurationContainsVideoSource
+ _csp_upstreamVideoFormatRequirementsWithDimensions
+ _kFigCaptureSampleBufferMetadata_VideoStabilizationOutputRotationVector
- -[BWCameraStreamingMonitor _updateActiveClientSessionsForSessionID:clientSession:clientAuditToken:tccIdentity:mediaEnvironment:]
- -[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]
- -[BWCinematographyObjectTrackingNode _visCropFactorFromMetadata:sampleBuffer:]
- -[BWCinematographyObjectTrackingNode initWithCaptureDevice:tuningParameters:inferenceScheduler:frameRate:prepareCinematographyOnInit:]
- GCC_except_table206
- GCC_except_table240
- GCC_except_table286
- GCC_except_table418
- GCC_except_table56
- _FigCaptureSessionSetConfiguration
- _OBJC_IVAR_$_BWCameraStreamingMonitorClientSession._activePortTypes
- _OBJC_IVAR_$_BWLensSmudgeDetection._cmcData
- _OUTLINED_FUNCTION_598
- _OUTLINED_FUNCTION_599
- _OUTLINED_FUNCTION_600
- _OUTLINED_FUNCTION_601
- _OUTLINED_FUNCTION_602
- _OUTLINED_FUNCTION_603
- _OUTLINED_FUNCTION_604
- ___119-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]_block_invoke
- ___block_descriptor_97_e8_32o40o48o56b_e5_v8?0ls32l8s40l8s48l8s56l8
- _cs_activePortTypesForCameraAttribution
- _cs_activePortTypesForCameraAttributionForDevice
- _cs_configurationContainsMultipleVideoSources
- _cs_configurationNumberOfVideoSources
CStrings:
+ ", CinematicFraming:1(CtrlMode:%d, RTSforCS: %d)"
+ "-[BWCameraStreamingMonitor _updateActiveClientSessionsForSessionID:clientSession:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:]"
+ "-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:activePortTypes:completionHandler:]_block_invoke"
+ "-[BWPhotonicEngineNodeResourceCoordinator purgeProcessorAndSharedExternalMemoryResourceBackendMemoryIfNeededWithSettings:]"
+ "<%@ %p> - fmt:%c%c%c%c, w:%d, h:%d, scs:%d, cs:%d, csroi:(%.2f, %.2f, %.2f, %.2f), csfm: %d, mfpx: %.2f, mfpy: %.2f, mfzm: %.2f, RTSforCS: %d, 10BitTF: %d, 10BitFromISP: %d, tfllbme: %d, rlas: %d, rle: %d"
+ "<<<< BWPhotonicEngineNodeResourceCoordinator >>>> %s: Allocator backend memory in use: %lu / %lu"
+ "<<<< BWPhotonicEngineNodeResourceCoordinator >>>> %s: Failed to finish processing in %{public}@ (err:%{public}d)"
+ "<<<< BWPhotonicEngineNodeResourceCoordinator >>>> %s: Failed to purge %{public}@ resources (err:%{public}d)"
+ "<<<< BWPhotonicEngineNodeResourceCoordinator >>>> %s: Purging sharedExternalMemoryResource (currentFlavors:%{public}@, zoomBasedResolutionFlavorRequired:%{public}d, setUpForZoomBasedResolutionFlavor:%{public}d, allocatorBackend:%{private}@)"
+ "BWInferenceAttachmentKey_FusionTrackerTargetRect"
+ "J510-J511"
+ "LastShownBuild:BWImageQueueSinkNode.m:1151"
+ "LastShownBuild:BWImageQueueSinkNode.m:2097"
+ "LastShownBuild:BWPixelBufferTransferRenderer.m:684"
+ "LastShownBuild:FigCaptureSession.m:10043"
+ "LastShownBuild:FigCaptureSession.m:10387"
+ "LastShownBuild:FigCaptureSession.m:10595"
+ "LastShownBuild:FigCaptureSession.m:11420"
+ "LastShownBuild:FigCaptureSession.m:11615"
+ "LastShownBuild:FigCaptureSession.m:16116"
+ "LastShownBuild:FigCaptureSession.m:19505"
+ "LastShownBuild:FigCaptureSession.m:21070"
+ "LastShownBuild:FigCaptureSession.m:21073"
+ "LastShownBuild:FigCaptureSession.m:26450"
+ "LastShownBuild:FigCaptureSession.m:26463"
+ "LastShownBuild:FigCaptureSession.m:28543"
+ "LastShownBuild:FigCaptureSession.m:29546"
+ "LastShownBuild:FigCaptureSession.m:4574"
+ "LastShownBuild:FigCaptureSession.m:5225"
+ "LastShownBuild:FigCaptureSession.m:9319"
+ "LastShownBuild:FigCaptureSession.m:9325"
+ "LastShownBuild:FigCaptureSession.m:9328"
+ "LastShownBuild:FigCaptureSession.m:9331"
+ "LastShownBuild:FigCaptureSession.m:9334"
+ "LastShownBuild:FigCaptureSession.m:9345"
+ "LastShownBuild:FigCaptureSession.m:9348"
+ "LastShownBuild:FigCaptureSession.m:9356"
+ "LastShownBuild:FigCaptureSession.m:9374"
+ "LastShownBuild:FigCaptureSession.m:9419"
+ "LastShownBuild:FigCaptureSession.m:9423"
+ "LastShownBuild:FigCaptureSession.m:9447"
+ "LastShownBuild:FigCaptureSession.m:9462"
+ "LastShownBuild:FigCaptureSession.m:9466"
+ "LastShownBuild:FigCaptureSession.m:9469"
+ "LastShownBuild:FigCaptureSession.m:9593"
+ "LastShownBuild:FigCaptureSession.m:9599"
+ "LastShownBuild:FigCaptureSession.m:9625"
+ "LastShownBuild:FigCaptureSession.m:9637"
+ "LastShownDate:BWImageQueueSinkNode.m:1151"
+ "LastShownDate:BWImageQueueSinkNode.m:2097"
+ "LastShownDate:BWPixelBufferTransferRenderer.m:684"
+ "LastShownDate:FigCaptureSession.m:10043"
+ "LastShownDate:FigCaptureSession.m:10387"
+ "LastShownDate:FigCaptureSession.m:10595"
+ "LastShownDate:FigCaptureSession.m:11420"
+ "LastShownDate:FigCaptureSession.m:11615"
+ "LastShownDate:FigCaptureSession.m:16116"
+ "LastShownDate:FigCaptureSession.m:19505"
+ "LastShownDate:FigCaptureSession.m:21070"
+ "LastShownDate:FigCaptureSession.m:21073"
+ "LastShownDate:FigCaptureSession.m:26450"
+ "LastShownDate:FigCaptureSession.m:26463"
+ "LastShownDate:FigCaptureSession.m:28543"
+ "LastShownDate:FigCaptureSession.m:29546"
+ "LastShownDate:FigCaptureSession.m:4574"
+ "LastShownDate:FigCaptureSession.m:5225"
+ "LastShownDate:FigCaptureSession.m:9319"
+ "LastShownDate:FigCaptureSession.m:9325"
+ "LastShownDate:FigCaptureSession.m:9328"
+ "LastShownDate:FigCaptureSession.m:9331"
+ "LastShownDate:FigCaptureSession.m:9334"
+ "LastShownDate:FigCaptureSession.m:9345"
+ "LastShownDate:FigCaptureSession.m:9348"
+ "LastShownDate:FigCaptureSession.m:9356"
+ "LastShownDate:FigCaptureSession.m:9374"
+ "LastShownDate:FigCaptureSession.m:9419"
+ "LastShownDate:FigCaptureSession.m:9423"
+ "LastShownDate:FigCaptureSession.m:9447"
+ "LastShownDate:FigCaptureSession.m:9462"
+ "LastShownDate:FigCaptureSession.m:9466"
+ "LastShownDate:FigCaptureSession.m:9469"
+ "LastShownDate:FigCaptureSession.m:9593"
+ "LastShownDate:FigCaptureSession.m:9599"
+ "LastShownDate:FigCaptureSession.m:9625"
+ "LastShownDate:FigCaptureSession.m:9637"
+ "Output Stabilization Metadata"
+ "attentionDetectionSupported"
+ "description=CameraCapture-764.60.7.0.2"
+ "realtimeStabilizationForCenterStage"
+ "realtimeStabilizationForCenterStageEnabled"
+ "realtimeStabilizationForCenterStageEnabled (%d -> %d)"
+ "realtimeStabilizationForDeskViewEnabled"
+ "realtimeStabilizationForDeskViewEnabled (%d -> %d)"
- ", CinematicFraming:1(CtrlMode:%d)"
- "-[BWCameraStreamingMonitor _updateActiveClientSessionsForSessionID:clientSession:clientAuditToken:tccIdentity:mediaEnvironment:]"
- "-[BWCameraStreamingMonitor setCameraAccess:deviceType:clientAuditToken:tccIdentity:mediaEnvironment:completionHandler:]_block_invoke"
- "<%@ %p> - fmt:%c%c%c%c, w:%d, h:%d, scs:%d, cs:%d, csroi:(%.2f, %.2f, %.2f, %.2f), csfm: %d, mfpx: %.2f, mfpy: %.2f, mfzm: %.2f, 10BitTF: %d, 10BitFromISP: %d, tfllbme: %d, rlas: %d, rle: %d"
- "<<<< FigCaptureSession >>>> %s: %{public}@ Device containing Reno suspended state changed, updating System Status activePortTypes: [%{public}@] -> [%{public}@]"
- "BWFusionTrackerTapToBoxTargetRect"
- "BWImageQueueSinkNodePreviewMetricsFailure"
- "LastShownBuild:BWImageQueueSinkNode.m:1150"
- "LastShownBuild:BWImageQueueSinkNode.m:2096"
- "LastShownBuild:BWImageQueueSinkNode.m:341"
- "LastShownBuild:BWPixelBufferTransferRenderer.m:645"
- "LastShownBuild:FigCaptureSession.m:10100"
- "LastShownBuild:FigCaptureSession.m:10444"
- "LastShownBuild:FigCaptureSession.m:10652"
- "LastShownBuild:FigCaptureSession.m:11477"
- "LastShownBuild:FigCaptureSession.m:11672"
- "LastShownBuild:FigCaptureSession.m:16120"
- "LastShownBuild:FigCaptureSession.m:19509"
- "LastShownBuild:FigCaptureSession.m:21074"
- "LastShownBuild:FigCaptureSession.m:21077"
- "LastShownBuild:FigCaptureSession.m:26454"
- "LastShownBuild:FigCaptureSession.m:26467"
- "LastShownBuild:FigCaptureSession.m:28547"
- "LastShownBuild:FigCaptureSession.m:29556"
- "LastShownBuild:FigCaptureSession.m:4631"
- "LastShownBuild:FigCaptureSession.m:5282"
- "LastShownBuild:FigCaptureSession.m:9376"
- "LastShownBuild:FigCaptureSession.m:9382"
- "LastShownBuild:FigCaptureSession.m:9385"
- "LastShownBuild:FigCaptureSession.m:9388"
- "LastShownBuild:FigCaptureSession.m:9391"
- "LastShownBuild:FigCaptureSession.m:9402"
- "LastShownBuild:FigCaptureSession.m:9405"
- "LastShownBuild:FigCaptureSession.m:9413"
- "LastShownBuild:FigCaptureSession.m:9431"
- "LastShownBuild:FigCaptureSession.m:9476"
- "LastShownBuild:FigCaptureSession.m:9480"
- "LastShownBuild:FigCaptureSession.m:9504"
- "LastShownBuild:FigCaptureSession.m:9519"
- "LastShownBuild:FigCaptureSession.m:9523"
- "LastShownBuild:FigCaptureSession.m:9526"
- "LastShownBuild:FigCaptureSession.m:9650"
- "LastShownBuild:FigCaptureSession.m:9656"
- "LastShownBuild:FigCaptureSession.m:9682"
- "LastShownBuild:FigCaptureSession.m:9694"
- "LastShownDate:BWImageQueueSinkNode.m:1150"
- "LastShownDate:BWImageQueueSinkNode.m:2096"
- "LastShownDate:BWImageQueueSinkNode.m:341"
- "LastShownDate:BWPixelBufferTransferRenderer.m:645"
- "LastShownDate:FigCaptureSession.m:10100"
- "LastShownDate:FigCaptureSession.m:10444"
- "LastShownDate:FigCaptureSession.m:10652"
- "LastShownDate:FigCaptureSession.m:11477"
- "LastShownDate:FigCaptureSession.m:11672"
- "LastShownDate:FigCaptureSession.m:16120"
- "LastShownDate:FigCaptureSession.m:19509"
- "LastShownDate:FigCaptureSession.m:21074"
- "LastShownDate:FigCaptureSession.m:21077"
- "LastShownDate:FigCaptureSession.m:26454"
- "LastShownDate:FigCaptureSession.m:26467"
- "LastShownDate:FigCaptureSession.m:28547"
- "LastShownDate:FigCaptureSession.m:29556"
- "LastShownDate:FigCaptureSession.m:4631"
- "LastShownDate:FigCaptureSession.m:5282"
- "LastShownDate:FigCaptureSession.m:9376"
- "LastShownDate:FigCaptureSession.m:9382"
- "LastShownDate:FigCaptureSession.m:9385"
- "LastShownDate:FigCaptureSession.m:9388"
- "LastShownDate:FigCaptureSession.m:9391"
- "LastShownDate:FigCaptureSession.m:9402"
- "LastShownDate:FigCaptureSession.m:9405"
- "LastShownDate:FigCaptureSession.m:9413"
- "LastShownDate:FigCaptureSession.m:9431"
- "LastShownDate:FigCaptureSession.m:9476"
- "LastShownDate:FigCaptureSession.m:9480"
- "LastShownDate:FigCaptureSession.m:9504"
- "LastShownDate:FigCaptureSession.m:9519"
- "LastShownDate:FigCaptureSession.m:9523"
- "LastShownDate:FigCaptureSession.m:9526"
- "LastShownDate:FigCaptureSession.m:9650"
- "LastShownDate:FigCaptureSession.m:9656"
- "LastShownDate:FigCaptureSession.m:9682"
- "LastShownDate:FigCaptureSession.m:9694"
- "Preview metrics failure. Average frame rate: %.2f fps. Average latency: %.3f sec. (Interval: %.1f sec. Expected: %.2f fps / %.3f sec.)"
- "com.apple.coremedia.inference-connection.completion"
- "description=CameraCapture-764.42.8"
```
