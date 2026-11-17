## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-764.60.7.0.2
-  __TEXT.__text: 0x684b50
-  __TEXT.__objc_methlist: 0x3e2a8
+764.60.13.0.1
+  __TEXT.__text: 0x685eac
+  __TEXT.__objc_methlist: 0x3e3c0
   __TEXT.__const: 0x151800
-  __TEXT.__cstring: 0xb04be
-  __TEXT.__oslogstring: 0x54e03
-  __TEXT.__gcc_except_tab: 0x3c7c
+  __TEXT.__cstring: 0xb06e8
+  __TEXT.__oslogstring: 0x54d62
+  __TEXT.__gcc_except_tab: 0x3ca8
   __TEXT.__ustring: 0x6ee
   __TEXT.__dlopen_cstrs: 0x7c9
-  __TEXT.__unwind_info: 0x18300
+  __TEXT.__unwind_info: 0x18368
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x11b58
+  __DATA_CONST.__const: 0x11b78
   __DATA_CONST.__objc_classlist: 0x2048
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18ed0
+  __DATA_CONST.__objc_selrefs: 0x18f90
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x1e78
   __DATA_CONST.__objc_arraydata: 0x3cd8
-  __DATA_CONST.__got: 0x79b0
-  __AUTH_CONST.__const: 0x4b60
-  __AUTH_CONST.__cfstring: 0x53300
-  __AUTH_CONST.__objc_const: 0xb18c0
+  __DATA_CONST.__got: 0x79b8
+  __AUTH_CONST.__const: 0x4b20
+  __AUTH_CONST.__cfstring: 0x53400
+  __AUTH_CONST.__objc_const: 0xb19d0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x6e58
   __AUTH_CONST.__objc_arrayobj: 0x2d90

   __AUTH_CONST.__objc_dictobj: 0x17e8
   __AUTH_CONST.__auth_got: 0x2f28
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0xcc2c
-  __DATA.__data: 0x730
+  __DATA.__objc_ivar: 0xcc44
+  __DATA.__data: 0x820
   __DATA.__crash_info: 0x148
   __DATA.__common: 0x1860
   __DATA_DIRTY.__objc_data: 0x141e0
-  __DATA_DIRTY.__data: 0x68d0
+  __DATA_DIRTY.__data: 0x67e0
   __DATA_DIRTY.__bss: 0x1260
   __DATA_DIRTY.__common: 0x100
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 39476
-  Symbols:   59520
-  CStrings:  22053
+  Functions: 39504
+  Symbols:   59562
+  CStrings:  22066
 
Symbols:
+ -[BWCinematicFramingNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:manualFramingFocalLengthMultiplier:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:downStreamRequires10BitPixelFormat:]
+ -[BWFigCaptureDeviceClient updateClientAuditToken:]
+ -[BWFigCaptureDeviceVendor updatePrewarmedClientWithClientAuditToken:]
+ -[BWFigCaptureDeviceVendorDeviceState streamsOwedAtTakeBackDevice]
+ -[BWFigVideoCaptureDevice _terminatePendingStillImageCaptureNowRetryForSuspendedCaptureStream:]
+ -[BWFigVideoCaptureDevice captureStreamDidSuspend:]
+ -[BWGraph _handleTimeoutWithStopping:description:briefReason:offendingNodes:]
+ -[BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution) _timedOutWaitingForBackColorCameraToStartOrCommit:]
+ -[BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution) _timedOutWaitingForBackColorCameraToStop:]
+ -[BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution) _timedOutWaitingForCameraSourceNodeToStartOrCommit:]
+ -[BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution) _timedOutWaitingForCameraSourceNodeToStop:]
+ -[BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution) _timedOutWaitingForFrontColorCameraToStartOrCommit:]
+ -[BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution) _timedOutWaitingForFrontColorCameraToStop:]
+ -[BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution) _timedOutWaitingForFrontInfraredCameraToStartOrCommit:]
+ -[BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution) _timedOutWaitingForFrontInfraredCameraToStop:]
+ -[BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution) graphTimedOutWithStopping:crashInfo:]
+ -[BWNode graphTimedOutWithStopping:crashInfo:]
+ -[BWPreviewStitcherRenderer _initTrueVideoHDRtoSDRCIContext]
+ -[BWPreviewStitcherRenderer _newCIContextWithOptions:]
+ -[BWPreviewStitcherRenderer _renderCIImage:context:toRenderDestination:sourceRect:destinationRect:]
+ -[BWVideoNoiseReductionNode _waitForAsyncMetalProcessingToComplete]
+ -[FigCaptureSessionConfiguration usesPerceptionThumbnailChannel:]
+ -[FigCaptureSourceConfiguration forceManualFramingEnabled]
+ -[FigCaptureSourceConfiguration perceptionThumbnailChannelCoexistenceEnabled]
+ -[FigCaptureSourceConfiguration setForceManualFramingEnabled:]
+ -[FigCaptureSourceConfiguration setPerceptionThumbnailChannelCoexistenceEnabled:]
+ -[FigCaptureSourceManager deactivateAttachedVideoSource:device:sessionID:]
+ -[FigCaptureSourceVideoFormat forceManualFramingForRotationCorrection]
+ -[FigCaptureSourceVideoFormat isPerceptionThumbnailChannelCoexistenceSupported]
+ -[FigCaptureSourceVideoFormat manualFramingCropWidth]
+ GCC_except_table183
+ GCC_except_table186
+ GCC_except_table198
+ GCC_except_table204
+ GCC_except_table206
+ GCC_except_table254
+ GCC_except_table301
+ GCC_except_table360
+ GCC_except_table379
+ GCC_except_table412
+ GCC_except_table435
+ GCC_except_table437
+ GCC_except_table454
+ GCC_except_table559
+ GCC_except_table747
+ _FigCaptureClientApplicationIDIsSafariWebContentVariant
+ _FigCaptureSourceFormatKey_ForceManualFramingForRotationCorrection
+ _FigCaptureSourceFormatKey_ManualFramingCropWidth
+ _FigCaptureSourceFormatKey_PerceptionThumbnailChannelCoexistenceSupported
+ _FigVideoCaptureSourceCopySessionID
+ _OBJC_IVAR_$_BWCinematicFramingNode._manualFramingFocalLengthMultiplier
+ _OBJC_IVAR_$_BWFigCaptureDeviceVendorDeviceState._streamsOwedAtTakeBackDevice
+ _OBJC_IVAR_$_BWPreviewStitcherRenderer._trueVideoHDRtoSDRCIContext
+ _OBJC_IVAR_$_BWVideoNoiseReductionNode._metalSharedEventListenerGroup
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._forceManualFramingEnabled
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._perceptionThumbnailChannelCoexistenceEnabled
+ _OUTLINED_FUNCTION_598
+ _OUTLINED_FUNCTION_599
+ __OBJC_$_INSTANCE_METHODS_BWMultiStreamCameraSourceNode(GraphTimeoutCrashAttribution)
+ ___51-[BWFigVideoCaptureDevice captureStreamDidSuspend:]_block_invoke
+ ___67-[BWVideoNoiseReductionNode _waitForAsyncMetalProcessingToComplete]_block_invoke
+ ___70-[BWFigCaptureDeviceVendor updatePrewarmedClientWithClientAuditToken:]_block_invoke
+ ___FigVideoCaptureSourceCopySessionID_block_invoke
+ _gr_graphTimeoutCrashInfo
+ _kCGColorSpaceExtendedLinearITUR_2020
+ _kFigCaptureMetadata_ExifLensMinFNumber
- -[BWCinematicFramingNode initWithOutputDimensions:cameraInfoByPortType:horizontalSensorBinningFactor:verticalSensorBinningFactor:deviceOrientationCorrectionEnabled:stillImageCaptureEnabled:objectMetadataIdentifiers:maxLossyCompressionLevel:portTypes:cinematicFramingControls:cameraHasDistortionCoefficients:cameraHasCalibrationValidMaxRadius:centerStageMetadataDeliveryEnabled:pipelineType:downStreamRequires10BitPixelFormat:]
- -[BWPreviewStitcherRenderer _renderCIImage:toRenderDestination:sourceRect:destinationRect:]
- -[FigCaptureSourceManager deactivateAttachedVideoSource:device:]
- GCC_except_table122
- GCC_except_table141
- GCC_except_table179
- GCC_except_table182
- GCC_except_table184
- GCC_except_table190
- GCC_except_table202
- GCC_except_table250
- GCC_except_table297
- GCC_except_table376
- GCC_except_table409
- GCC_except_table432
- GCC_except_table434
- GCC_except_table451
- GCC_except_table556
- GCC_except_table744
- GCC_except_table88
- __OBJC_$_INSTANCE_METHODS_BWMultiStreamCameraSourceNode
- ___122-[BWPhotonicEngineNodeResourceCoordinator purgeProcessorAndSharedExternalMemoryResourceBackendMemoryIfNeededWithSettings:]_block_invoke
- ___71-[BWVideoNoiseReductionNode didReachEndOfDataForConfigurationID:input:]_block_invoke
- ___73-[BWVideoNoiseReductionNode _waitForAsyncNoiseReductionProcessToComplete]_block_invoke_2
CStrings:
+ ", PerceptionThumbnailChannelCoex:1"
+ ", forceMF:1"
+ "-[BWFigCaptureDeviceClient updateClientAuditToken:]"
+ "-[BWFigCaptureDeviceVendor updatePrewarmedClientWithClientAuditToken:]_block_invoke"
+ "-[BWFigVideoCaptureDevice _terminatePendingStillImageCaptureNowRetryForSuspendedCaptureStream:]"
+ "-[FigCaptureSessionAttachedSessionManager attachToRunningSession:]"
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Device %p still has streams owed by a previous client: %@. Invalidating it so new client %@ gets a new device"
+ "<<<< BWFigCaptureDeviceVendor >>>> %s: Updating client audit token for pid %d to pid %d"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: '%{public}@' was suspended with a pending StillImageCaptureNow retry, terminating capture for captureID:%lld"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Driver/firmware is busy, stopping retrying (count:%d, suspended:%d, err=%d)"
+ "BWFusionTrackerTapToBoxTargetRect"
+ "ExifLensMinFNumber"
+ "ForceManualFramingForRotationCorrection"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:1619"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3075"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3126"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3712"
+ "LastShownBuild:BWFigCaptureDeviceVendor.m:3725"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10194"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:10687"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11271"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11722"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11757"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11946"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11955"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11967"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:11974"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:12008"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:12074"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:12245"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:13141"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:13239"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:16414"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:19279"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:19667"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20550"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20974"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20976"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:20978"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:22879"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24279"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24311"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:24467"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25221"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25246"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25495"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:25852"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:6281"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7978"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:7987"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9070"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9071"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9090"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9105"
+ "LastShownBuild:BWFigVideoCaptureDevice.m:9380"
+ "LastShownBuild:BWFigVideoCaptureStream.m:3268"
+ "LastShownBuild:BWFigVideoCaptureStream.m:3954"
+ "LastShownBuild:BWFigVideoCaptureStream.m:4374"
+ "LastShownBuild:BWGraph.m:2707"
+ "LastShownBuild:BWGraph.m:3617"
+ "LastShownBuild:BWGraph.m:3620"
+ "LastShownBuild:BWGraph.m:3633"
+ "LastShownBuild:BWGraph.m:3636"
+ "LastShownBuild:BWGraph.m:3639"
+ "LastShownBuild:BWHVSScoringNode.m:3517"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:13962"
+ "LastShownBuild:BWMultiStreamCameraSourceNode.m:13978"
+ "LastShownBuild:BWPreviewStitcherNode.m:3429"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:1556"
+ "LastShownBuild:FigCaptureMetadataUtilities.m:6337"
+ "LastShownBuild:FigCaptureSession.m:10045"
+ "LastShownBuild:FigCaptureSession.m:1020"
+ "LastShownBuild:FigCaptureSession.m:10389"
+ "LastShownBuild:FigCaptureSession.m:10597"
+ "LastShownBuild:FigCaptureSession.m:11422"
+ "LastShownBuild:FigCaptureSession.m:11617"
+ "LastShownBuild:FigCaptureSession.m:16119"
+ "LastShownBuild:FigCaptureSession.m:19523"
+ "LastShownBuild:FigCaptureSession.m:21088"
+ "LastShownBuild:FigCaptureSession.m:21091"
+ "LastShownBuild:FigCaptureSession.m:26487"
+ "LastShownBuild:FigCaptureSession.m:26500"
+ "LastShownBuild:FigCaptureSession.m:28580"
+ "LastShownBuild:FigCaptureSession.m:29592"
+ "LastShownBuild:FigCaptureSession.m:4576"
+ "LastShownBuild:FigCaptureSession.m:5227"
+ "LastShownBuild:FigCaptureSession.m:9321"
+ "LastShownBuild:FigCaptureSession.m:9327"
+ "LastShownBuild:FigCaptureSession.m:9330"
+ "LastShownBuild:FigCaptureSession.m:9333"
+ "LastShownBuild:FigCaptureSession.m:9336"
+ "LastShownBuild:FigCaptureSession.m:9347"
+ "LastShownBuild:FigCaptureSession.m:9350"
+ "LastShownBuild:FigCaptureSession.m:9358"
+ "LastShownBuild:FigCaptureSession.m:9376"
+ "LastShownBuild:FigCaptureSession.m:9421"
+ "LastShownBuild:FigCaptureSession.m:9425"
+ "LastShownBuild:FigCaptureSession.m:9449"
+ "LastShownBuild:FigCaptureSession.m:9464"
+ "LastShownBuild:FigCaptureSession.m:9468"
+ "LastShownBuild:FigCaptureSession.m:9471"
+ "LastShownBuild:FigCaptureSession.m:9595"
+ "LastShownBuild:FigCaptureSession.m:9601"
+ "LastShownBuild:FigCaptureSession.m:9627"
+ "LastShownBuild:FigCaptureSession.m:9639"
+ "LastShownBuild:FigCaptureSessionStateManager.m:349"
+ "LastShownBuild:FigCaptureSessionStateManager.m:376"
+ "LastShownBuild:FigCaptureSessionStateManager.m:513"
+ "LastShownBuild:FigCaptureUtilities.m:1150"
+ "LastShownBuild:FigCaptureUtilities.m:1276"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:1619"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3075"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3126"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3712"
+ "LastShownDate:BWFigCaptureDeviceVendor.m:3725"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10194"
+ "LastShownDate:BWFigVideoCaptureDevice.m:10687"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11271"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11722"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11757"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11946"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11955"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11967"
+ "LastShownDate:BWFigVideoCaptureDevice.m:11974"
+ "LastShownDate:BWFigVideoCaptureDevice.m:12008"
+ "LastShownDate:BWFigVideoCaptureDevice.m:12074"
+ "LastShownDate:BWFigVideoCaptureDevice.m:12245"
+ "LastShownDate:BWFigVideoCaptureDevice.m:13141"
+ "LastShownDate:BWFigVideoCaptureDevice.m:13239"
+ "LastShownDate:BWFigVideoCaptureDevice.m:16414"
+ "LastShownDate:BWFigVideoCaptureDevice.m:19279"
+ "LastShownDate:BWFigVideoCaptureDevice.m:19667"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20550"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20974"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20976"
+ "LastShownDate:BWFigVideoCaptureDevice.m:20978"
+ "LastShownDate:BWFigVideoCaptureDevice.m:22879"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24279"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24311"
+ "LastShownDate:BWFigVideoCaptureDevice.m:24467"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25221"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25246"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25495"
+ "LastShownDate:BWFigVideoCaptureDevice.m:25852"
+ "LastShownDate:BWFigVideoCaptureDevice.m:6281"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7978"
+ "LastShownDate:BWFigVideoCaptureDevice.m:7987"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9070"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9071"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9090"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9105"
+ "LastShownDate:BWFigVideoCaptureDevice.m:9380"
+ "LastShownDate:BWFigVideoCaptureStream.m:3268"
+ "LastShownDate:BWFigVideoCaptureStream.m:3954"
+ "LastShownDate:BWFigVideoCaptureStream.m:4374"
+ "LastShownDate:BWGraph.m:2707"
+ "LastShownDate:BWGraph.m:3617"
+ "LastShownDate:BWGraph.m:3620"
+ "LastShownDate:BWGraph.m:3633"
+ "LastShownDate:BWGraph.m:3636"
+ "LastShownDate:BWGraph.m:3639"
+ "LastShownDate:BWHVSScoringNode.m:3517"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:13962"
+ "LastShownDate:BWMultiStreamCameraSourceNode.m:13978"
+ "LastShownDate:BWPreviewStitcherNode.m:3429"
+ "LastShownDate:FigCaptureMetadataUtilities.m:1556"
+ "LastShownDate:FigCaptureMetadataUtilities.m:6337"
+ "LastShownDate:FigCaptureSession.m:10045"
+ "LastShownDate:FigCaptureSession.m:1020"
+ "LastShownDate:FigCaptureSession.m:10389"
+ "LastShownDate:FigCaptureSession.m:10597"
+ "LastShownDate:FigCaptureSession.m:11422"
+ "LastShownDate:FigCaptureSession.m:11617"
+ "LastShownDate:FigCaptureSession.m:16119"
+ "LastShownDate:FigCaptureSession.m:19523"
+ "LastShownDate:FigCaptureSession.m:21088"
+ "LastShownDate:FigCaptureSession.m:21091"
+ "LastShownDate:FigCaptureSession.m:26487"
+ "LastShownDate:FigCaptureSession.m:26500"
+ "LastShownDate:FigCaptureSession.m:28580"
+ "LastShownDate:FigCaptureSession.m:29592"
+ "LastShownDate:FigCaptureSession.m:4576"
+ "LastShownDate:FigCaptureSession.m:5227"
+ "LastShownDate:FigCaptureSession.m:9321"
+ "LastShownDate:FigCaptureSession.m:9327"
+ "LastShownDate:FigCaptureSession.m:9330"
+ "LastShownDate:FigCaptureSession.m:9333"
+ "LastShownDate:FigCaptureSession.m:9336"
+ "LastShownDate:FigCaptureSession.m:9347"
+ "LastShownDate:FigCaptureSession.m:9350"
+ "LastShownDate:FigCaptureSession.m:9358"
+ "LastShownDate:FigCaptureSession.m:9376"
+ "LastShownDate:FigCaptureSession.m:9421"
+ "LastShownDate:FigCaptureSession.m:9425"
+ "LastShownDate:FigCaptureSession.m:9449"
+ "LastShownDate:FigCaptureSession.m:9464"
+ "LastShownDate:FigCaptureSession.m:9468"
+ "LastShownDate:FigCaptureSession.m:9471"
+ "LastShownDate:FigCaptureSession.m:9595"
+ "LastShownDate:FigCaptureSession.m:9601"
+ "LastShownDate:FigCaptureSession.m:9627"
+ "LastShownDate:FigCaptureSession.m:9639"
+ "LastShownDate:FigCaptureSessionStateManager.m:349"
+ "LastShownDate:FigCaptureSessionStateManager.m:376"
+ "LastShownDate:FigCaptureSessionStateManager.m:513"
+ "LastShownDate:FigCaptureUtilities.m:1150"
+ "LastShownDate:FigCaptureUtilities.m:1276"
+ "ManualFramingCropWidth"
+ "PerceptionThumbnailChannelCoexistenceSupported"
+ "com.apple.coremedia.inference-connection.completion"
+ "description=CameraCapture-764.60.13.0.1"
+ "forceManualFramingEnabled"
+ "forceManualFramingEnabled (%d -> %d)"
+ "perceptionThumbnailChannelCoexistenceEnabled"
+ "perceptionThumbnailChannelCoexistenceEnabled (%d -> %d)"
- "-[BWPhotonicEngineNodeResourceCoordinator purgeProcessorAndSharedExternalMemoryResourceBackendMemoryIfNeededWithSettings:]"
- "<<<< BWFigVideoCaptureDevice >>>> %s: Driver/firmware is busy, stopping retrying (count:%d, err=%d)"
- "<<<< BWPhotonicEngineNodeResourceCoordinator >>>> %s: Allocator backend memory in use: %lu / %lu"
- "<<<< BWPhotonicEngineNodeResourceCoordinator >>>> %s: Failed to finish processing in %{public}@ (err:%{public}d)"
- "<<<< BWPhotonicEngineNodeResourceCoordinator >>>> %s: Failed to purge %{public}@ resources (err:%{public}d)"
- "<<<< BWPhotonicEngineNodeResourceCoordinator >>>> %s: Purging sharedExternalMemoryResource (currentFlavors:%{public}@, zoomBasedResolutionFlavorRequired:%{public}d, setUpForZoomBasedResolutionFlavor:%{public}d, allocatorBackend:%{private}@)"
- "BWInferenceAttachmentKey_FusionTrackerTargetRect"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:1577"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3031"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3082"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3668"
- "LastShownBuild:BWFigCaptureDeviceVendor.m:3681"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10158"
- "LastShownBuild:BWFigVideoCaptureDevice.m:10651"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11235"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11686"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11721"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11910"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11919"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11931"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11938"
- "LastShownBuild:BWFigVideoCaptureDevice.m:11972"
- "LastShownBuild:BWFigVideoCaptureDevice.m:12038"
- "LastShownBuild:BWFigVideoCaptureDevice.m:12207"
- "LastShownBuild:BWFigVideoCaptureDevice.m:13103"
- "LastShownBuild:BWFigVideoCaptureDevice.m:13201"
- "LastShownBuild:BWFigVideoCaptureDevice.m:16366"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19231"
- "LastShownBuild:BWFigVideoCaptureDevice.m:19619"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20502"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20926"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20928"
- "LastShownBuild:BWFigVideoCaptureDevice.m:20930"
- "LastShownBuild:BWFigVideoCaptureDevice.m:22831"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24231"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24263"
- "LastShownBuild:BWFigVideoCaptureDevice.m:24419"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25173"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25198"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25447"
- "LastShownBuild:BWFigVideoCaptureDevice.m:25804"
- "LastShownBuild:BWFigVideoCaptureDevice.m:6245"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7942"
- "LastShownBuild:BWFigVideoCaptureDevice.m:7951"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9034"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9035"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9054"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9069"
- "LastShownBuild:BWFigVideoCaptureDevice.m:9344"
- "LastShownBuild:BWFigVideoCaptureStream.m:3264"
- "LastShownBuild:BWFigVideoCaptureStream.m:3950"
- "LastShownBuild:BWFigVideoCaptureStream.m:4370"
- "LastShownBuild:BWGraph.m:2684"
- "LastShownBuild:BWGraph.m:3594"
- "LastShownBuild:BWGraph.m:3597"
- "LastShownBuild:BWGraph.m:3610"
- "LastShownBuild:BWGraph.m:3613"
- "LastShownBuild:BWGraph.m:3616"
- "LastShownBuild:BWHVSScoringNode.m:3508"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:13942"
- "LastShownBuild:BWMultiStreamCameraSourceNode.m:13958"
- "LastShownBuild:BWPreviewStitcherNode.m:3432"
- "LastShownBuild:FigCaptureMetadataUtilities.m:1546"
- "LastShownBuild:FigCaptureMetadataUtilities.m:6327"
- "LastShownBuild:FigCaptureSession.m:10043"
- "LastShownBuild:FigCaptureSession.m:1018"
- "LastShownBuild:FigCaptureSession.m:10387"
- "LastShownBuild:FigCaptureSession.m:10595"
- "LastShownBuild:FigCaptureSession.m:11420"
- "LastShownBuild:FigCaptureSession.m:11615"
- "LastShownBuild:FigCaptureSession.m:16116"
- "LastShownBuild:FigCaptureSession.m:19505"
- "LastShownBuild:FigCaptureSession.m:21070"
- "LastShownBuild:FigCaptureSession.m:21073"
- "LastShownBuild:FigCaptureSession.m:26450"
- "LastShownBuild:FigCaptureSession.m:26463"
- "LastShownBuild:FigCaptureSession.m:28543"
- "LastShownBuild:FigCaptureSession.m:29546"
- "LastShownBuild:FigCaptureSession.m:4574"
- "LastShownBuild:FigCaptureSession.m:5225"
- "LastShownBuild:FigCaptureSession.m:9319"
- "LastShownBuild:FigCaptureSession.m:9325"
- "LastShownBuild:FigCaptureSession.m:9328"
- "LastShownBuild:FigCaptureSession.m:9331"
- "LastShownBuild:FigCaptureSession.m:9334"
- "LastShownBuild:FigCaptureSession.m:9345"
- "LastShownBuild:FigCaptureSession.m:9348"
- "LastShownBuild:FigCaptureSession.m:9356"
- "LastShownBuild:FigCaptureSession.m:9374"
- "LastShownBuild:FigCaptureSession.m:9419"
- "LastShownBuild:FigCaptureSession.m:9423"
- "LastShownBuild:FigCaptureSession.m:9447"
- "LastShownBuild:FigCaptureSession.m:9462"
- "LastShownBuild:FigCaptureSession.m:9466"
- "LastShownBuild:FigCaptureSession.m:9469"
- "LastShownBuild:FigCaptureSession.m:9593"
- "LastShownBuild:FigCaptureSession.m:9599"
- "LastShownBuild:FigCaptureSession.m:9625"
- "LastShownBuild:FigCaptureSession.m:9637"
- "LastShownBuild:FigCaptureSessionStateManager.m:351"
- "LastShownBuild:FigCaptureSessionStateManager.m:378"
- "LastShownBuild:FigCaptureSessionStateManager.m:515"
- "LastShownBuild:FigCaptureUtilities.m:1139"
- "LastShownBuild:FigCaptureUtilities.m:1265"
- "LastShownDate:BWFigCaptureDeviceVendor.m:1577"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3031"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3082"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3668"
- "LastShownDate:BWFigCaptureDeviceVendor.m:3681"
- "LastShownDate:BWFigVideoCaptureDevice.m:10158"
- "LastShownDate:BWFigVideoCaptureDevice.m:10651"
- "LastShownDate:BWFigVideoCaptureDevice.m:11235"
- "LastShownDate:BWFigVideoCaptureDevice.m:11686"
- "LastShownDate:BWFigVideoCaptureDevice.m:11721"
- "LastShownDate:BWFigVideoCaptureDevice.m:11910"
- "LastShownDate:BWFigVideoCaptureDevice.m:11919"
- "LastShownDate:BWFigVideoCaptureDevice.m:11931"
- "LastShownDate:BWFigVideoCaptureDevice.m:11938"
- "LastShownDate:BWFigVideoCaptureDevice.m:11972"
- "LastShownDate:BWFigVideoCaptureDevice.m:12038"
- "LastShownDate:BWFigVideoCaptureDevice.m:12207"
- "LastShownDate:BWFigVideoCaptureDevice.m:13103"
- "LastShownDate:BWFigVideoCaptureDevice.m:13201"
- "LastShownDate:BWFigVideoCaptureDevice.m:16366"
- "LastShownDate:BWFigVideoCaptureDevice.m:19231"
- "LastShownDate:BWFigVideoCaptureDevice.m:19619"
- "LastShownDate:BWFigVideoCaptureDevice.m:20502"
- "LastShownDate:BWFigVideoCaptureDevice.m:20926"
- "LastShownDate:BWFigVideoCaptureDevice.m:20928"
- "LastShownDate:BWFigVideoCaptureDevice.m:20930"
- "LastShownDate:BWFigVideoCaptureDevice.m:22831"
- "LastShownDate:BWFigVideoCaptureDevice.m:24231"
- "LastShownDate:BWFigVideoCaptureDevice.m:24263"
- "LastShownDate:BWFigVideoCaptureDevice.m:24419"
- "LastShownDate:BWFigVideoCaptureDevice.m:25173"
- "LastShownDate:BWFigVideoCaptureDevice.m:25198"
- "LastShownDate:BWFigVideoCaptureDevice.m:25447"
- "LastShownDate:BWFigVideoCaptureDevice.m:25804"
- "LastShownDate:BWFigVideoCaptureDevice.m:6245"
- "LastShownDate:BWFigVideoCaptureDevice.m:7942"
- "LastShownDate:BWFigVideoCaptureDevice.m:7951"
- "LastShownDate:BWFigVideoCaptureDevice.m:9034"
- "LastShownDate:BWFigVideoCaptureDevice.m:9035"
- "LastShownDate:BWFigVideoCaptureDevice.m:9054"
- "LastShownDate:BWFigVideoCaptureDevice.m:9069"
- "LastShownDate:BWFigVideoCaptureDevice.m:9344"
- "LastShownDate:BWFigVideoCaptureStream.m:3264"
- "LastShownDate:BWFigVideoCaptureStream.m:3950"
- "LastShownDate:BWFigVideoCaptureStream.m:4370"
- "LastShownDate:BWGraph.m:2684"
- "LastShownDate:BWGraph.m:3594"
- "LastShownDate:BWGraph.m:3597"
- "LastShownDate:BWGraph.m:3610"
- "LastShownDate:BWGraph.m:3613"
- "LastShownDate:BWGraph.m:3616"
- "LastShownDate:BWHVSScoringNode.m:3508"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:13942"
- "LastShownDate:BWMultiStreamCameraSourceNode.m:13958"
- "LastShownDate:BWPreviewStitcherNode.m:3432"
- "LastShownDate:FigCaptureMetadataUtilities.m:1546"
- "LastShownDate:FigCaptureMetadataUtilities.m:6327"
- "LastShownDate:FigCaptureSession.m:10043"
- "LastShownDate:FigCaptureSession.m:1018"
- "LastShownDate:FigCaptureSession.m:10387"
- "LastShownDate:FigCaptureSession.m:10595"
- "LastShownDate:FigCaptureSession.m:11420"
- "LastShownDate:FigCaptureSession.m:11615"
- "LastShownDate:FigCaptureSession.m:16116"
- "LastShownDate:FigCaptureSession.m:19505"
- "LastShownDate:FigCaptureSession.m:21070"
- "LastShownDate:FigCaptureSession.m:21073"
- "LastShownDate:FigCaptureSession.m:26450"
- "LastShownDate:FigCaptureSession.m:26463"
- "LastShownDate:FigCaptureSession.m:28543"
- "LastShownDate:FigCaptureSession.m:29546"
- "LastShownDate:FigCaptureSession.m:4574"
- "LastShownDate:FigCaptureSession.m:5225"
- "LastShownDate:FigCaptureSession.m:9319"
- "LastShownDate:FigCaptureSession.m:9325"
- "LastShownDate:FigCaptureSession.m:9328"
- "LastShownDate:FigCaptureSession.m:9331"
- "LastShownDate:FigCaptureSession.m:9334"
- "LastShownDate:FigCaptureSession.m:9345"
- "LastShownDate:FigCaptureSession.m:9348"
- "LastShownDate:FigCaptureSession.m:9356"
- "LastShownDate:FigCaptureSession.m:9374"
- "LastShownDate:FigCaptureSession.m:9419"
- "LastShownDate:FigCaptureSession.m:9423"
- "LastShownDate:FigCaptureSession.m:9447"
- "LastShownDate:FigCaptureSession.m:9462"
- "LastShownDate:FigCaptureSession.m:9466"
- "LastShownDate:FigCaptureSession.m:9469"
- "LastShownDate:FigCaptureSession.m:9593"
- "LastShownDate:FigCaptureSession.m:9599"
- "LastShownDate:FigCaptureSession.m:9625"
- "LastShownDate:FigCaptureSession.m:9637"
- "LastShownDate:FigCaptureSessionStateManager.m:351"
- "LastShownDate:FigCaptureSessionStateManager.m:378"
- "LastShownDate:FigCaptureSessionStateManager.m:515"
- "LastShownDate:FigCaptureUtilities.m:1139"
- "LastShownDate:FigCaptureUtilities.m:1265"
- "description=CameraCapture-764.60.7.0.2"
```
