## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-587.60.6.0.0
-  __TEXT.__text: 0x79db50
+587.60.10.122.3
+  __TEXT.__text: 0x7a1720
   __TEXT.__auth_stubs: 0x4ef0
-  __TEXT.__objc_methlist: 0x2a9cc
+  __TEXT.__objc_methlist: 0x2ab2c
   __TEXT.__const: 0x1505a8
-  __TEXT.__cstring: 0xbfb76
-  __TEXT.__oslogstring: 0x1048c1
-  __TEXT.__gcc_except_tab: 0x3e48
+  __TEXT.__cstring: 0xbff78
+  __TEXT.__oslogstring: 0x105363
+  __TEXT.__gcc_except_tab: 0x3e60
   __TEXT.__dlopen_cstrs: 0x6d8
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0xc4c8
+  __TEXT.__unwind_info: 0xc620
   __TEXT.__objc_classname: 0x75a9
-  __TEXT.__objc_methname: 0x92953
-  __TEXT.__objc_methtype: 0x13a9c
-  __TEXT.__objc_stubs: 0x40300
-  __DATA_CONST.__got: 0x5f60
-  __DATA_CONST.__const: 0xa658
+  __TEXT.__objc_methname: 0x9304a
+  __TEXT.__objc_methtype: 0x13a92
+  __TEXT.__objc_stubs: 0x405c0
+  __DATA_CONST.__got: 0x5f50
+  __DATA_CONST.__const: 0xa6d8
   __DATA_CONST.__objc_classlist: 0x18c0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x4e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x12368
+  __DATA_CONST.__objc_selrefs: 0x12420
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x1738
-  __DATA_CONST.__objc_arraydata: 0x35d0
+  __DATA_CONST.__objc_arraydata: 0x35f0
   __AUTH_CONST.__auth_got: 0x2788
   __AUTH_CONST.__auth_ptr: 0x98
-  __AUTH_CONST.__const: 0x3e70
-  __AUTH_CONST.__cfstring: 0x42100
-  __AUTH_CONST.__objc_const: 0x87270
+  __AUTH_CONST.__const: 0x3e30
+  __AUTH_CONST.__cfstring: 0x42280
+  __AUTH_CONST.__objc_const: 0x875d0
   __AUTH_CONST.__objc_intobj: 0x4ed8
-  __AUTH_CONST.__objc_arrayobj: 0x25c8
+  __AUTH_CONST.__objc_arrayobj: 0x25e0
   __AUTH_CONST.__objc_doubleobj: 0x9c0
-  __AUTH_CONST.__objc_floatobj: 0x230
+  __AUTH_CONST.__objc_floatobj: 0x220
   __AUTH_CONST.__objc_dictobj: 0x1798
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x9588
-  __DATA.__data: 0x4918
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x95cc
+  __DATA.__data: 0x48f0
   __DATA.__crash_info: 0x40
-  __DATA.__common: 0x10c0
-  __DATA.__bss: 0x1a78
-  __DATA_DIRTY.__objc_data: 0xf000
-  __DATA_DIRTY.__data: 0xfb8
-  __DATA_DIRTY.__common: 0x1000
-  __DATA_DIRTY.__bss: 0xa18
+  __DATA.__common: 0x1080
+  __DATA.__bss: 0x1a88
+  __DATA_DIRTY.__objc_data: 0xf050
+  __DATA_DIRTY.__data: 0xfe0
+  __DATA_DIRTY.__common: 0x1040
+  __DATA_DIRTY.__bss: 0xa38
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  Functions: 20968
-  Symbols:   26628
-  CStrings:  51838
+  Functions: 20995
+  Symbols:   26654
+  CStrings:  51930
 
Symbols:
+ _OBJC_CLASS_$_CMISmartStyleCCMPriorGenerator
- _CMISmartStyleMetadataKey_PersonMasksValidHint
- _CMISmartStyleRendererStatsKeyPersonMasksValidHint
- _CMISmartStyleRendererStatsKeySkinRatio
CStrings:
+ ", emitsEmptyMetadata:%!d(MISSING)"
+ "-[BWFigCaptureDeviceVendor _deviceAvailabilityChangedForClient:available:postNotification:reason:canShareWithAVFlashlight:]_block_invoke"
+ "-[BWFigCaptureDeviceVendor _removeActiveDeviceClient:moveToVictimizedList:]"
+ "-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithAVFlashlightAllowed:clientIsAVFlashlight:deviceAvailabilityChangedHandler:]"
+ "-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithAVFlashlightAllowed:clientIsAVFlashlight:deviceAvailabilityChangedHandler:]_block_invoke"
+ "-[BWImageQueueSinkNode configurationWithID:updatedFormat:didBecomeLiveForInput:]"
+ "-[BWMultiStreamCameraSourceNode secureMetadataOutputConfigurationDidChange:]"
+ "-[BWOverCaptureSmartStyleApplyNode prepareForCurrentConfigurationToBecomeLive]"
+ "-[BWSmartStyleApplyNode prepareForCurrentConfigurationToBecomeLive]"
+ "-[BWVISNode willStartProcessingBuffer:withStatus:]"
+ "-[FigCaptureVISPipeline _buildVISPipelineWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:visProcessingSemaphore:]"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Active client(s): %!@(MISSING)"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Called for PID %!d(MISSING), clientDescription: %!@(MISSING), clientPriority: %!d(MISSING), deviceSharingWithOtherClientsAllowed: %!d(MISSING), deviceSharingWithAVFlashlightAllowed: %!d(MISSING), clientIsAVFlashlight: %!d(MISSING), deviceAvailabilityChangedHandler: %!@(MISSING)"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Cannot unregister an active device client: %!@(MISSING)"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Device %!p(MISSING) can be shared, vending it to client %!@(MISSING)"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Device %!p(MISSING) is in use by %!@(MISSING), but new client %!@(MISSING) says steal it, so throwing it away and making a new one"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Device %!p(MISSING) is use by %!{(MISSING)public}@ and new client %!{(MISSING)public}@ cannot steal it, so moving new client to the victimized list"
+ "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Device %!p(MISSING) is use by %!{(MISSING)public}@ and new client %!{(MISSING)public}@ cannot steal it, so returning nil and unregistering client"
+ "<<<< BWFigVideoCaptureDevice >>>> %!s(MISSING): Ultra high resolution Zero Shutter Lag is enabled without thermal mitigation"
+ "<<<< BWImageQueueSinkNode >>>> %!s(MISSING): %!{(MISSING)public}@: Received duplicate configuration live message for ID %!l(MISSING)ld while already active, self.liveConfiguration %!l(MISSING)ld, dropping"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %!s(MISSING): MetadataOutputConfiguration: %!@(MISSING)"
+ "<<<< BWPreviewStitcherNode >>>> %!s(MISSING): Done waiting for _restitchingQueue"
+ "<<<< BWPreviewStitcherNode >>>> %!s(MISSING): Output no longer live, dropping stitchedSampleBuffer"
+ "<<<< BWPreviewStitcherNode >>>> %!s(MISSING): Waiting for _restitchingQueue"
+ "<<<< BWRemoteQueueSinkNode >>>> %!s(MISSING): Intrinsic matrix - focal length X: %!f(MISSING), Y: %!f(MISSING), principal point X: %!f(MISSING), Y: %!f(MISSING)"
+ "<<<< BWSampleBufferUtilities >>>> %!s(MISSING): Missing camera intrinsic matrix data"
+ "<<<< BWSampleBufferUtilities >>>> %!s(MISSING): Scaled camera intrinsic matrix. Old: fx=%!f(MISSING), fy=%!f(MISSING), ox=%!f(MISSING), oy=%!f(MISSING). New: fx=%!f(MISSING), fy=%!f(MISSING), ox=%!f(MISSING), oy=%!f(MISSING)"
+ "<<<< BWSmartStyleLearningNode >>>> %!s(MISSING): Could not lock base address of pixelBuffer"
+ "<<<< BWSmartStyleLearningNode >>>> %!s(MISSING): Could not unlock base address of pixelBuffer"
+ "<<<< BWSmartStyleLearningNode >>>> %!s(MISSING): initialCoefficientsPixelBuffer is nil"
+ "<<<< BWSmartStyleLearningNode >>>> %!s(MISSING): initialStyle is nil"
+ "<<<< BWSmartStyleLearningNode >>>> %!s(MISSING): pixel buffer format is not supported for populating style engine coefficients"
+ "<<<< BWSmartStyleLearningNode >>>> %!s(MISSING): styleEngineConfiguration is nil"
+ "<<<< BWStillImageFocusPixelDisparityNode >>>> %!s(MISSING): Supported color height:%!d(MISSING) doesn't match with input height:%!d(MISSING)"
+ "<<<< BWStillImageFocusPixelDisparityNode >>>> %!s(MISSING): Supported color width:%!d(MISSING) doesn't match with input buffer width:%!d(MISSING)"
+ "<<<< BWStillImageFocusPixelDisparityNode >>>> %!s(MISSING): Supported disparity height:%!d(MISSING) doesn't match with depthDataOutputDimensions width:%!d(MISSING)"
+ "<<<< BWStillImageFocusPixelDisparityNode >>>> %!s(MISSING): Supported disparity width:%!d(MISSING) doesn't match with depthDataOutputDimensions width:%!d(MISSING)"
+ "<<<< BWStillImageFocusPixelDisparityNode >>>> %!s(MISSING): Supported green size height:%!d(MISSING) doesn't match with input sashimi raw height:%!d(MISSING)"
+ "<<<< BWStillImageFocusPixelDisparityNode >>>> %!s(MISSING): Supported green size width:%!d(MISSING) doesn't match with input sashimi raw width:%!d(MISSING)"
+ "<<<< BWStillImageFocusPixelDisparityNode >>>> %!s(MISSING): Supported raw size height:%!d(MISSING) doesn't match with input sashimi raw height:%!d(MISSING)"
+ "<<<< BWStillImageFocusPixelDisparityNode >>>> %!s(MISSING): Supported raw size width:%!d(MISSING) doesn't match with input sashimi raw width:%!d(MISSING)"
+ "<<<< BWStillImageProcessing >>>> %!s(MISSING): Smart Style rendering for Stereo Photo capture will be bypassed for captureID:%!l(MISSING)ld"
+ "<<<< FigCaptureMetadataUtilities >>>> %!s(MISSING): Failed to determine FigAppleMakerNoteCamera for port type '%!@(MISSING)' and camera location '%!d(MISSING)', marking as Unknown"
+ "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %!s(MISSING): failed to connect previousOutput to optimizedEnhancedDepthRouter.input"
+ "<<<< FigCaptureSession >>>> %!s(MISSING): %!{(MISSING)public}@ Finished waiting for True Video exit transition"
+ "<<<< FigCaptureSession >>>> %!s(MISSING): clientIdentifier is nil"
+ "<<<< FigCaptureSessionParsedConfiguration >>>> %!s(MISSING): Vision data is not supported on Bravo camera ports"
+ "<<<< FigCaptureSessionParsedConfiguration >>>> %!s(MISSING): Vision data is only supported for the Wide camera port on Bravo devices"
+ "<<<< FigCaptureVideoDataSinkPipeline >>>> %!s(MISSING): Configuration: %!s(MISSING) %!@(MISSING): video data sink format '%!@(MISSING)', rotation degrees %!i(MISSING), mirroring %!i(MISSING), scaling %!i(MISSING), zoom %!i(MISSING), crop %!i(MISSING), shared pools %!i(MISSING)"
+ "<FigCaptureSession %!@(MISSING) retainCount: %!l(MISSING)d%!s(MISSING) allocator: %!p(MISSING), "
+ "@64@0:8i16@20@28i36B40B44B48B52@?56"
+ "B16@?0@\"FigCaptureConnectionConfiguration\"8"
+ "BWGetScaledCameraIntrinsicsMatrix"
+ "ConfigureForStereoPhotoCaptureSupport"
+ "DeviceSharingWithAVFlashlightAllowed"
+ "FigCaptureClientApplicationIDIsMagnifier"
+ "FigCaptureClientApplicationIDIsVisualIntelligenceCamera"
+ "MOC %!p(MISSING): <%!@(MISSING)>%!@(MISSING) -> <%!@(MISSING)> E:%!d(MISSING) MetadataIdentifiers:{%!@(MISSING)}%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)"
+ "No sizes found in processor parameters"
+ "PortraitTapToRefocusPrevented"
+ "StereoPhotoCaptureSceneMonitoringParameters"
+ "StereoPhotoCaptureSupported"
+ "StereoPhotoSNRDifferenceSecondarySNRThreshold"
+ "StereoPhotoSNRDifferenceThreshold"
+ "StereoPhotoThresholdSNRThreshold"
+ "TB,N,V_emitsEmptyObjectDetectionMetadata"
+ "TB,N,V_releasesResourcesAtEndOfData"
+ "TB,N,V_visionDataRequiredWhenConfiguredAsSlave"
+ "TB,R,N,V_clientIsAVFlashlight"
+ "TB,R,N,V_deviceSharingWithAVFlashlightAllowed"
+ "Tf,N,V_visionDataMaxFrameRate"
+ "Ti,N,V_indexOfAudioRemixInMetadataOutputs"
+ "Ti,R,N,V_indexOfAudioRemixInMetadataOutputs"
+ "T{?=ii},N,V_depthDataOutputDimensions"
+ "Unable to create sample buffer for prior coefficients sample buffer"
+ "Unable to get timing info for unstyled sample buffer"
+ "VIS Processor pre image stabilization callback, generating drop"
+ "VisionDataCameraIntrinsicMatrix"
+ "[super addNode:optimizedEnhancedDepthRouter error:&error]"
+ "_activeDeviceClients"
+ "_clientIsAVFlashlight"
+ "_deviceSharingWithAVFlashlightAllowed"
+ "_emitsEmptyObjectDetectionMetadata"
+ "_graphID"
+ "_indexOfAudioRemixInMetadataOutputs"
+ "_initialCoefficientsPixelBuffer"
+ "_initialStyle"
+ "_personSegmentationAndDepthNode"
+ "_printIntrinsics"
+ "_processorCoordinatorIsSetup"
+ "_releasesResourcesAtEndOfData"
+ "_restitchingQueue"
+ "_updateMetadataOutputWithoutDisabling"
+ "_visProcessingSemaphore"
+ "_visionDataMaxFrameRate"
+ "_visionDataRequiredWhenConfiguredAsSlave"
+ "calculateStartupPriorCCMforCast:tone:color:intensity:priorStrength:"
+ "captureSession_clientIsVisualIntelligenceCamera"
+ "captureSession_dispatchGraphCalloutWithGraphIDToWorkerQueueAfter_block_invoke"
+ "clientID: %!d(MISSING), pid: %!d(MISSING), clientApplicationID: %!@(MISSING), clientDescription: %!@(MISSING), clientPriority: %!@(MISSING), canStealFromClientsWithSamePriority: %!d(MISSING), deviceSharingWithOtherClientsAllowed: %!d(MISSING), deviceSharingWithAVFlashlightAllowed: %!d(MISSING), clientIsAVFlashlight: %!d(MISSING), handler: %!p(MISSING)"
+ "clientIsAVFlashlight"
+ "color_size"
+ "com.apple.Magnifier"
+ "com.apple.Magnifier.MagnifierExtension"
+ "com.apple.bwgraph.previewstitcher.restitching"
+ "createAndSolveGlobalLinearSystem"
+ "depthDataOutputDimensions"
+ "description=CameraCapture-587.60.10.122.3"
+ "deviceSharingWithAVFlashlightAllowed"
+ "disparity_size"
+ "emitsEmptyObjectDetectionMetadata"
+ "fcmu_cameraFromPortTypeAndCameraLocation"
+ "green_size"
+ "i56@0:8i16@20i28B32B36B40B44@?48"
+ "i64@0:8i16@20@28i36B40B44B48B52@?56"
+ "indexOfAudioRemixInMetadataOutputs"
+ "initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithAVFlashlightAllowed:clientIsAVFlashlight:deviceAvailabilityChangedHandler:"
+ "initialCoefficientsPixelBuffer"
+ "initialStyle"
+ "pixelBufferFormatIsSupported"
+ "portraitTapToRefocusPrevented"
+ "previewStitcherTrueVideoExitTransitionDidComplete:"
+ "print_intrinsics"
+ "processingSemaphore"
+ "raw_size"
+ "registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithAVFlashlightAllowed:clientIsAVFlashlight:deviceAvailabilityChangedHandler:"
+ "registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceSharingWithAVFlashlightAllowed:clientIsAVFlashlight:deviceAvailabilityChangedHandler:"
+ "releasesResourcesAtEndOfData"
+ "setDepthDataOutputDimensions:"
+ "setEmitsEmptyObjectDetectionMetadata:"
+ "setIndexOfAudioRemixInMetadataOutputs:"
+ "setProcessingSemaphore:"
+ "setReleasesResourcesAtEndOfData:"
+ "setStoppingForModeSwitch:parallelGraphRebuildEnabled:ispFastSwitchEnabled:smartStyleRenderingEnabledInTrueVideoGraph:"
+ "setVisionDataMaxFrameRate:"
+ "setVisionDataRequiredWhenConfiguredAsSlave:"
+ "sizes"
+ "spotlightCount"
+ "ssln_populateCVPixelBufferWithPriorMatrices"
+ "supportedSizes"
+ "visionDataMaxFrameRate"
+ "visionDataRequiredWhenConfiguredAsSlave"
+ "weightPlaneCount"
+ "willStartProcessingBuffer:withStatus:"
- "-[BWFigCaptureDeviceVendor _deviceAvailabilityChangedForClient:available:postNotification:reason:]_block_invoke"
- "-[BWFigCaptureDeviceVendor _removeActiveDeviceClientAndMoveToVictimizedList:]"
- "-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceAvailabilityChangedHandler:]"
- "-[BWFigCaptureDeviceVendor registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceAvailabilityChangedHandler:]_block_invoke"
- "-[BWOverCaptureSmartStyleApplyNode prepareForCurrentConfigurationToBecomeLive]_block_invoke"
- "-[BWSmartStyleApplyNode prepareForCurrentConfigurationToBecomeLive]_block_invoke"
- "-[FigCaptureVISPipeline _buildVISPipelineWithUpstreamOutput:graph:parentPipeline:videoCaptureConnectionConfiguration:pipelineStage:sdofPipelineStage:videoStabilizationType:motionAttachmentsSource:fillExtendedRowsOfOutputBuffer:overCaptureEnabled:stereoMode:videoStabilizationOverscanOverride:videoStabilizationStrength:motionMetadataPreloadingEnabled:visExecutionMode:pipelineTraceID:captureDevice:outputDimensions:P3ToBT2020ConversionEnabled:stabilizeDepthAttachments:outputDepthDimensions:maxLossyCompressionLevel:videoSTFEnabled:videoGreenGhostMitigationEnabled:lightSourceMaskAndKeypointDescriptorDataEnabled:personSegmentationRenderingEnabled:smartStyleRenderingEnabled:smartStyleReversibilityEnabled:lowResImageUsedByVideoEncoderEnabled:portTypesWithGeometricDistortionCorrectionInVISEnabled:]"
- "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Active client: %!@(MISSING)"
- "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Called for PID %!d(MISSING), clientDescription: %!@(MISSING), clientPriority: %!d(MISSING), deviceSharingWithOtherClientsAllowed: %!d(MISSING), deviceAvailabilityChangedHandler: %!@(MISSING)"
- "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Cannot unregister active device client: %!@(MISSING)"
- "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Device %!p(MISSING) is in use by client %!@(MISSING), but new client %!@(MISSING) says steal it, so throwing it away and making a new one"
- "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Device %!p(MISSING) is use by client %!{(MISSING)public}@ and new client %!{(MISSING)public}@ cannot steal it, so moving new client to the victimized list"
- "<<<< BWFigCaptureDeviceVendor >>>> %!s(MISSING): Device %!p(MISSING) is use by client %!{(MISSING)public}@ and new client %!{(MISSING)public}@ cannot steal it, so returning nil and unregistering client"
- "<<<< BWStillImageMetadataUtilities >>>> %!s(MISSING): hasPersonBoxes: %!d(MISSING) skinRatio: %!f(MISSING) personMasksValidHint: %!f(MISSING)"
- "<<<< BWStillImageProcessing >>>> %!s(MISSING): personMasksValidHint: %!f(MISSING)"
- "<<<< FigCaptureMetadataUtilities >>>> %!s(MISSING): Failed to determine FigAppleMakerNoteCamera for portType (%!@(MISSING)), marking as Unknown"
- "<<<< FigCapturePhotonicEngineSinkPipeline >>>> %!s(MISSING): failed to connect previousOutput to optimizedEnhancedPortraitRouter.input"
- "<<<< FigCaptureSessionParsedConfiguration >>>> %!s(MISSING): VisionData is not yet supported on Bravo camera ports"
- "<<<< FigCaptureSource >>>> %!s(MISSING):  clientBundleIdentifier set to %!@(MISSING)"
- "<<<< FigCaptureVideoDataSinkPipeline >>>> %!s(MISSING): Configuration: %!s(MISSING) %!@(MISSING): video data sink format '%!@(MISSING)', rotation degrees %!i(MISSING), mirroring %!i(MISSING), scaling %!i(MISSING), zoom %!i(MISSING), shared pools %!i(MISSING)"
- "<FigCaptureSession %!p(MISSING) retainCount: %!l(MISSING)d%!s(MISSING) allocator: %!p(MISSING), "
- "@\"BWFigCaptureDeviceClient\""
- "@56@0:8i16@20@28i36B40B44@?48"
- "BWSmartStylePersonMasksValidHint"
- "ConfigureForSambaSupport"
- "FigCaptureClientApplicationIDIsTamale"
- "MOC %!p(MISSING): <%!@(MISSING)>%!@(MISSING) -> <%!@(MISSING)> E:%!d(MISSING) MetadataIdentifiers:{%!@(MISSING)}%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)%!@(MISSING)"
- "SambaMonitoringParameters"
- "SambaSupported"
- "SambaThresholdA"
- "SambaThresholdB"
- "SambaThresholdC"
- "Unable to create proxy load queue"
- "[(id)clientBundleIdentifier isKindOfClass:[NSString class]]"
- "[super addNode:optimizedEnhancedPortraitRouter error:&error]"
- "_activeDeviceClient"
- "_stylesProxyRendererLoadQueue"
- "captureSession_clientIsTamale"
- "captureSession_dispatchGraphCalloutToWorkerQueueAfter_block_invoke"
- "clientBundleIdentifier is not an NSString"
- "clientID: %!d(MISSING), pid: %!d(MISSING), clientApplicationID: %!@(MISSING), clientDescription: %!@(MISSING), clientPriority: %!@(MISSING), canStealFromClientsWithSamePriority: %!d(MISSING), deviceSharingWithOtherClientsAllowed: %!d(MISSING), handler: %!p(MISSING)"
- "com.apple.Tamale"
- "com.apple.coremedia.smartstyle-apply.proxy-load-queue"
- "com.apple.coremedia.smartstyle-overcapture-apply.proxy-load-queue"
- "com.apple.coremedia.zoomPIP.styles-proxy-renderer-load-queue"
- "description=CameraCapture-587.60.6"
- "fcmu_cameraFromPortType"
- "i48@0:8i16@20i28B32B36@?40"
- "i56@0:8i16@20@28i36B40B44@?48"
- "initWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceAvailabilityChangedHandler:"
- "registerClientWithPID:clientApplicationID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceAvailabilityChangedHandler:"
- "registerClientWithPID:clientDescription:clientPriority:canStealFromClientsWithSamePriority:deviceSharingWithOtherClientsAllowed:deviceAvailabilityChangedHandler:"
- "setPersonMasksValidHint:"

```
