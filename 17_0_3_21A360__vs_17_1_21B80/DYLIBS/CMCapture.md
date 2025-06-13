## CMCapture

> `/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`

```diff

-458.3.12.1.0
-  __TEXT.__text: 0x440028
-  __TEXT.__auth_stubs: 0x4960
-  __TEXT.__objc_methlist: 0x250f4
-  __TEXT.__const: 0x150088
-  __TEXT.__cstring: 0x610de
-  __TEXT.__oslogstring: 0x174b3
-  __TEXT.__gcc_except_tab: 0x1e20
+465.15.2.0.0
+  __TEXT.__text: 0x4463d8
+  __TEXT.__auth_stubs: 0x4970
+  __TEXT.__objc_methlist: 0x2536c
+  __TEXT.__const: 0x150098
+  __TEXT.__cstring: 0x618bb
+  __TEXT.__oslogstring: 0x18189
+  __TEXT.__gcc_except_tab: 0x1e38
   __TEXT.__dlopen_cstrs: 0x53f
   __TEXT.__ustring: 0xc
-  __TEXT.__unwind_info: 0x9f48
-  __TEXT.__objc_classname: 0x6a0e
-  __TEXT.__objc_methname: 0x7c157
-  __TEXT.__objc_methtype: 0x114e2
-  __TEXT.__objc_stubs: 0x36ec0
-  __DATA_CONST.__got: 0x4438
-  __DATA_CONST.__const: 0x8628
-  __DATA_CONST.__objc_classlist: 0x1690
+  __TEXT.__unwind_info: 0x9fd0
+  __TEXT.__objc_classname: 0x6a4a
+  __TEXT.__objc_methname: 0x7cde7
+  __TEXT.__objc_methtype: 0x1161a
+  __TEXT.__objc_stubs: 0x37320
+  __DATA_CONST.__got: 0x4508
+  __DATA_CONST.__const: 0x8670
+  __DATA_CONST.__objc_classlist: 0x1698
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x458
+  __DATA_CONST.__objc_protolist: 0x460
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x62378
-  __DATA_CONST.__objc_selrefs: 0xfad8
-  __DATA_CONST.__objc_arraydata: 0x3200
-  __AUTH_CONST.__objc_const: 0x678
-  __AUTH_CONST.__cfstring: 0x2f840
+  __DATA_CONST.__objc_const: 0x62dd8
+  __DATA_CONST.__objc_selrefs: 0xfc10
+  __DATA_CONST.__objc_arraydata: 0x3208
+  __AUTH_CONST.__objc_const: 0x6c0
+  __AUTH_CONST.__cfstring: 0x2fba0
   __AUTH_CONST.__objc_intobj: 0x4350
-  __AUTH_CONST.__objc_arrayobj: 0x2298
+  __AUTH_CONST.__objc_arrayobj: 0x22b0
   __AUTH_CONST.__const: 0x1170
   __AUTH_CONST.__objc_floatobj: 0x1c0
   __AUTH_CONST.__objc_dictobj: 0x1798
   __AUTH_CONST.__objc_doubleobj: 0x960
-  __AUTH_CONST.__auth_got: 0x24c0
-  __AUTH.__objc_data: 0x500
+  __AUTH_CONST.__auth_got: 0x24c8
+  __AUTH.__objc_data: 0x550
   __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x1938
-  __DATA.__objc_superrefs: 0x1530
-  __DATA.__objc_ivar: 0x80e4
-  __DATA.__data: 0x4918
+  __DATA.__objc_classrefs: 0x1940
+  __DATA.__objc_superrefs: 0x1538
+  __DATA.__objc_ivar: 0x81c4
+  __DATA.__data: 0x4a10
   __DATA.__crash_info: 0x40
   __DATA.__common: 0x2c0
-  __DATA.__bss: 0xfe0
-  __DATA_DIRTY.__const: 0x2280
+  __DATA.__bss: 0x1008
+  __DATA_DIRTY.__const: 0x22c0
   __DATA_DIRTY.__objc_const: 0x134f8
   __DATA_DIRTY.__objc_data: 0xdca0
   __DATA_DIRTY.__data: 0xd98
-  __DATA_DIRTY.__common: 0x620
+  __DATA_DIRTY.__common: 0x640
   __DATA_DIRTY.__bss: 0x9e8
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libtailspin.dylib
-  UUID: AF80521A-CB09-3318-821E-9B4C2EC39213
-  Functions: 18089
-  Symbols:   64825
-  CStrings:  37358
+  UUID: 536BDEA8-9D99-3F7D-8FBD-B4F7F37D5E1B
+  Functions: 18155
+  Symbols:   65107
+  CStrings:  37566
 
Symbols:
+ -[BWBackgroundBlurNode reactionCount]
+ -[BWCMPhotoCompressionSession addAuxImage:type:auxImageMetadata:options:parentImageHandle:]
+ -[BWCMPhotoCompressionSession addMainImage:metadata:options:imageHandleOut:]
+ -[BWCMPhotoCompressionSession addMetadata:parentImageHandle:]
+ -[BWCMPhotoCompressionSession addThumbnailImage:options:parentImageHandle:]
+ -[BWCompressedShotBufferNode compressionResourcesAllocated]
+ -[BWCompressedShotBufferNode freeBufferCountIncreasedHandler]
+ -[BWCompressedShotBufferNode getInUseCompressedBufferCount:inUseCompressedBytes:maxInUseCompressedBytes:forUncompressedEquivalentFreeBufferCount:]
+ -[BWCompressedShotBufferNode hasUncompressedEquivalentFreeBufferCount:]
+ -[BWCompressedShotBufferNode minimumUncompressedEquivalentCapacity]
+ -[BWCompressedShotBufferNode passthroughEnabled]
+ -[BWCompressedShotBufferNode setFreeBufferCountIncreasedHandler:]
+ -[BWDNGCompressionSession addAuxImage:type:auxImageMetadata:options:parentImageHandle:]
+ -[BWDNGCompressionSession addMainImage:metadata:options:imageHandleOut:]
+ -[BWDNGCompressionSession addMetadata:parentImageHandle:]
+ -[BWDNGCompressionSession addThumbnailImage:options:parentImageHandle:]
+ -[BWDerectificationInferenceProvider initWithInputRequirement:opticalFlowInputRequirement:outputRequirement:resourceProvider:configuration:]
+ -[BWFigCaptureDeviceVendor _logActiveDefaultDeviceClientAndDevice]
+ -[BWFigCaptureDeviceVendor activeDefaultDeviceEquals:]
+ -[BWFigVideoCaptureDevice _reportDeskViewStreamingSessionCoreAnalyticsData]
+ -[BWFigVideoCaptureDevice _resetAnalyticsData]
+ -[BWFigVideoCaptureDevice clientExpectsCameraMountedInLandscapeOrientation]
+ -[BWFigVideoCaptureDevice isUltraWideStreamActive]
+ -[BWFigVideoCaptureDevice setClientExpectsCameraMountedInLandscapeOrientation:]
+ -[BWFigVideoCaptureDevice setDeskCamActive:]
+ -[BWFigVideoCaptureDevice setUltraWideActive:]
+ -[BWFigVideoCaptureStream officialFocalLengthMultiplier]
+ -[BWFigVideoCaptureStream reactionCount]
+ -[BWGraph clientExpectsCameraMountedInLandscapeOrientation]
+ -[BWGraph setClientExpectsCameraMountedInLandscapeOrientation:]
+ -[BWIrisMovieGenerator initWithReadableByteStream:forFrontFacingCamera:forExternalCamera:clientExpectsCameraMountedInLandscapeOrientation:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:]
+ -[BWIrisMovieGenerator initWithReadableByteStream:metadataByteStream:forFrontFacingCamera:forExternalCamera:clientExpectsCameraMountedInLandscapeOrientation:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:]
+ -[BWMovieFileOutputAnalyticsPayload cameraPosture]
+ -[BWMovieFileOutputAnalyticsPayload setCameraPosture:]
+ -[BWMultiStreamCameraSourceNodeConfiguration setVideoCaptureDimensionsIncludeVISOverscan:]
+ -[BWMultiStreamCameraSourceNodeConfiguration videoCaptureDimensionsIncludeVISOverscan]
+ -[BWPhotoEncoderNode _addAuxImagesIfNeededForEncodingScheme:sampleBuffer:metadata:stillImageSettings:processingFlags:embedThumbToCompressedImage:parentImageHandle:parentImageAdded:]
+ -[BWPhotoEncoderNode _addDepthForEncodingScheme:sampleBuffer:primaryOutputAspectRatio:processingFlags:parentImageHandle:]
+ -[BWPhotoEncoderNode _addEligibleAuxImagesforExpectedAdjustedPhotoWithSbuf:encodingScheme:processingFlags:metadata:stillImageSettings:embedThumbToCompressedImage:adjustedPhotoPrewarmContainerOptions:adjustedPhotoPrewarmEncodingOptions:]
+ -[BWPhotoEncoderNode _addGainMapForEncodingScheme:sampleBuffer:outputWidth:outputHeight:primaryOutputAspectRatio:processingFlags:parentImageHanlde:]
+ -[BWPhotoEncoderNode _addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:parentImageHandle:]
+ -[BWPhotoEncoderNode _addPortraitEffectsMatteForEncodingScheme:sampleBuffer:primaryOutputAspectRatio:processingFlags:parentImageHandle:]
+ -[BWPhotoEncoderNode _addSemanticMatteToCompressionSession:sampleBuffer:attachedMediaKey:auxImageType:primaryOutputAspectRatio:sourceCropRectKey:processingFlags:orientation:parentImageHandle:]
+ -[BWPhotoEncoderNode _addSemanticMattesForEncodingScheme:semanticSegmentationMatteURNs:sampleBuffer:primaryOutputAspectRatio:settingsID:processingFlags:orientation:parentImageHandle:]
+ -[BWPhotoEncoderNode _addThumbnailForEncodingScheme:thumbnailPixelBuffer:metadata:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:processingFlags:cropRect:codecType:maxPixelSize:parentImageHandle:]
+ -[BWPhotoEncoderNode _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:usedContainerOptionsOut:usedEncodingOptionsOut:mainImageHandleInOut:]
+ -[BWPhotoEncoderNode _expectsAdjustedPhotoForOriginalPhoto:stillImageSettings:]
+ -[BWPhotoEncoderNode _handlePrewarmForDepthForEncodingScheme:requestedStillImageCaptureSettings:exifOrientation:]
+ -[BWPhotoEncoderNode _handlePrewarmForGainMapForEncodingScheme:requestedStillImageCaptureSettings:exifOrientation:]
+ -[BWPhotoEncoderNode _handlePrewarmForPortraitEffectsMatteForEncodingScheme:requestedStillImageCaptureSettings:exifOrientation:]
+ -[BWPhotoEncoderNode _optionsForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:containerOptionsOut:encodingOptionsOut:]
+ -[BWPhotoEncoderNode handleNodeError:forInput:]
+ -[BWPhotonicEngineNode _clearPortraitSemaphoreWithError:]
+ -[BWPhotonicEngineNode filterNodeDidReceiveStandardResolutionDeepFusionBuffer:error:]
+ -[BWReactionAnalyticsPayload dealloc]
+ -[BWReactionAnalyticsPayload eventDictionary]
+ -[BWReactionAnalyticsPayload eventName]
+ -[BWReactionAnalyticsPayload init]
+ -[BWReactionAnalyticsPayload reactionType]
+ -[BWReactionAnalyticsPayload reset]
+ -[BWReactionAnalyticsPayload setReactionType:]
+ -[BWReactionAnalyticsPayload setUiTriggeredReaction:]
+ -[BWReactionAnalyticsPayload uiTriggeredReaction]
+ -[BWRectificationInferenceProvider initWithRefInputRequirement:auxInputRequirement:refKeypointsInputRequirement:auxKeypointsInputRequirement:refOutputRequirement:auxOutputRequirement:opticalFlowOutputRequirement:originalRefRequirement:originalAuxRequirement:resourceProvider:configuration:]
+ -[BWStillImageCaptureMetadata officialFocalLengthMultiplierByPortType]
+ -[BWStillImageCaptureMetadata setOfficialFocalLengthMultiplierByPortType:]
+ -[BWStillImageCoordinatorNode _expectedFrameCountForNextRequest]
+ -[BWStillImageFilterNode _initWithNodeConfiguration:sensorConfigurationsByPortType:statusDelegate:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:renderResourceProvider:]
+ -[BWStillImageFilterNode initWithNodeConfiguration:sensorConfigurationsByPortType:statusDelegate:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:]
+ -[BWStreamingCVAFilterRenderer initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:]
+ -[BWStreamingFilterNode initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:portraitPreviewForegroundBlurEnabled:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:]
+ -[BWStreamingSessionAnalyticsPayload orientationLandscapeTime]
+ -[BWStreamingSessionAnalyticsPayload orientationPortraitTime]
+ -[BWStreamingSessionAnalyticsPayload reactionCount]
+ -[BWStreamingSessionAnalyticsPayload setOrientationLandscapeTime:]
+ -[BWStreamingSessionAnalyticsPayload setOrientationPortraitTime:]
+ -[BWStreamingSessionAnalyticsPayload setReactionCount:]
+ -[BWStreamingSessionAnalyticsPayload setThermalThrottledTime:]
+ -[BWStreamingSessionAnalyticsPayload thermalThrottledTime]
+ -[FigCaptureCameraSourcePipeline videoCaptureOutputTransformForSourceDeviceType:]
+ -[FigCaptureConnectionConfiguration(FigCaptureConnectionConfigurationInternal) smartCameraRequired]
+ -[FigCaptureDeferredProcessingEngine releasePrewarmingResources]
+ -[FigCaptureSessionConfiguration clientExpectsCameraMountedInLandscapeOrientation]
+ -[FigCaptureSessionConfiguration setClientExpectsCameraMountedInLandscapeOrientation:]
+ -[FigCaptureSourceConfiguration clientExpectsCameraMountedInLandscapeOrientation]
+ -[FigCaptureSourceConfiguration setClientExpectsCameraMountedInLandscapeOrientation:]
+ -[FigCaptureSourceConfiguration(FigCaptureSourceConfigurationInternal) setSmartCameraEnabled:]
+ -[FigObjectDetectionMetadataGenerator getCurrentDetectedObjectsAndPTS:]
+ -[FigObjectDetectionMetadataGenerator processPixelBuffer:pts:]
+ GCC_except_table100
+ GCC_except_table134
+ GCC_except_table176
+ GCC_except_table217
+ GCC_except_table238
+ GCC_except_table256
+ GCC_except_table286
+ GCC_except_table305
+ GCC_except_table307
+ GCC_except_table321
+ GCC_except_table338
+ GCC_except_table413
+ GCC_except_table414
+ GCC_except_table57
+ GCC_except_table93
+ GCC_except_table97
+ _.compoundliteral.31
+ _.compoundliteral.38
+ _.compoundliteral.39
+ _.compoundliteral.42
+ _.compoundliteral.43
+ _.compoundliteral.44
+ _.compoundliteral.46
+ _.compoundliteral.47
+ _.compoundliteral.48
+ _.compoundliteral.49
+ _.compoundliteral.50
+ _.compoundliteral.51
+ _.compoundliteral.78
+ _.compoundliteral.87
+ _.compoundliteral.88
+ _BWInferenceAttachedMediaKey_DisparityFilteringOpticalFlow
+ _BWVideoSampleBufferToDisplayString
+ _FigCFDictionaryGetValueIfPresent
+ _FigCaptureClientApplicationIdentifierReplayD
+ _FigCaptureClientApplicationIdentifierReplayD_obsolete
+ _FigCaptureTransformPointToCoordinateSpaceOfRect
+ _OBJC_CLASS_$_BWReactionAnalyticsPayload
+ _OBJC_IVAR_$_BWBackgroundBlurNode._reactionCounterAPI
+ _OBJC_IVAR_$_BWBackgroundBlurNode._reactionCounterAll
+ _OBJC_IVAR_$_BWCompressedShotBufferNode._compressWhenCompressedBuffersInUseEnabled
+ _OBJC_IVAR_$_BWCompressedShotBufferNode._freeBufferCountIncreasedHandler
+ _OBJC_IVAR_$_BWCompressedShotBufferNode._passthroughEnabled
+ _OBJC_IVAR_$_BWDerectificationInferenceProvider._disparityIntermediate
+ _OBJC_IVAR_$_BWDerectificationInferenceProvider._disparityPostProcessor
+ _OBJC_IVAR_$_BWDerectificationInferenceProvider._lastIsQsubFrame
+ _OBJC_IVAR_$_BWDerectificationInferenceProvider._opticalFlowInputDescriptor
+ _OBJC_IVAR_$_BWDerectificationInferenceProvider._opticalFlowInputRequirement
+ _OBJC_IVAR_$_BWDerectificationInferenceProvider._portType
+ _OBJC_IVAR_$_BWFigCaptureDeviceVendor._deviceDateFormatter
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._clientExpectsCameraMountedInLandscapeOrientation
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._deskCamActive
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._deskCamStartTime
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._deviceOrientationMonitor
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._orientationCurrent
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._orientationLandscapeTotalTime
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._orientationPortraitTotalTime
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._orientationStartTime
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._thermalMonitor
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._thermalThrottledStartTime
+ _OBJC_IVAR_$_BWFigVideoCaptureDevice._ultraWideActive
+ _OBJC_IVAR_$_BWFigVideoCaptureStream._officialFocalLengthMultiplier
+ _OBJC_IVAR_$_BWGraph._clientExpectsCameraMountedInLandscapeOrientation
+ _OBJC_IVAR_$_BWIrisMovieGenerator._clientExpectsCameraMountedInLandscapeOrientation
+ _OBJC_IVAR_$_BWIrisStagingNode._reachedEndOfData
+ _OBJC_IVAR_$_BWMovieFileOutputAnalyticsPayload._cameraPosture
+ _OBJC_IVAR_$_BWMultiStreamCameraSourceNodeConfiguration._videoCaptureDimensionsIncludeVISOverscan
+ _OBJC_IVAR_$_BWPhotoEncoderNode._adjustedPhotoReservedParentImageHandle
+ _OBJC_IVAR_$_BWPhotoEncoderNode._eligibleAuxImagesWereAddedToAdjustedPhotoContainer
+ _OBJC_IVAR_$_BWPhotonicEngineNode._deepZoomProEnhancedResolutionPortraitSemaphore
+ _OBJC_IVAR_$_BWPhotonicEngineNode._deepZoomProEnhancedResolutionPortraitSemaphoreLock
+ _OBJC_IVAR_$_BWReactionAnalyticsPayload._reactionType
+ _OBJC_IVAR_$_BWReactionAnalyticsPayload._uiTriggeredReaction
+ _OBJC_IVAR_$_BWRectificationInferenceProvider._commandQueue
+ _OBJC_IVAR_$_BWRectificationInferenceProvider._disparityPostProcessor
+ _OBJC_IVAR_$_BWRectificationInferenceProvider._opticalFlowDescriptor
+ _OBJC_IVAR_$_BWRectificationInferenceProvider._opticalFlowOutputRequirement
+ _OBJC_IVAR_$_BWStillImageCaptureMetadata._officialFocalLengthMultiplierByPortType
+ _OBJC_IVAR_$_BWStillImageCoordinatorNode._normalResolutionOverlapCapacityForSoQ
+ _OBJC_IVAR_$_BWStillImageFilterNode._statusDelegate
+ _OBJC_IVAR_$_BWStreamingCVAFilterRenderer._mirroredForMetadataAdjustment
+ _OBJC_IVAR_$_BWStreamingCVAFilterRenderer._rotationDegreesForMetadataAdjustment
+ _OBJC_IVAR_$_BWStreamingFilterNode._mirroredForMetadataAdjustment
+ _OBJC_IVAR_$_BWStreamingFilterNode._perFrameLoggingRatio
+ _OBJC_IVAR_$_BWStreamingFilterNode._receivedFrameCounter
+ _OBJC_IVAR_$_BWStreamingFilterNode._rotationDegreesForMetadataAdjustment
+ _OBJC_IVAR_$_BWStreamingFilterNode._shouldLogPerFrameLogging
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._orientationLandscapeTime
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._orientationPortraitTime
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._reactionCount
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._reactionsCount
+ _OBJC_IVAR_$_BWStreamingSessionAnalyticsPayload._thermalThrottledTime
+ _OBJC_IVAR_$_FigCaptureSessionConfiguration._clientExpectsCameraMountedInLandscapeOrientation
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._clientExpectsCameraMountedInLandscapeOrientation
+ _OBJC_IVAR_$_FigCaptureSourceConfiguration._smartCameraEnabled
+ _OBJC_IVAR_$_FigObjectDetectionMetadataGenerator._objectMetadataDictionaryPTS
+ _OBJC_METACLASS_$_BWReactionAnalyticsPayload
+ __OBJC_$_INSTANCE_METHODS_BWReactionAnalyticsPayload
+ __OBJC_$_INSTANCE_VARIABLES_BWReactionAnalyticsPayload
+ __OBJC_$_PROP_LIST_BWReactionAnalyticsPayload
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_BWStillImageFilterStatusDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BWStillImageFilterStatusDelegate
+ __OBJC_CLASS_PROTOCOLS_$_BWReactionAnalyticsPayload
+ __OBJC_CLASS_RO_$_BWReactionAnalyticsPayload
+ __OBJC_LABEL_PROTOCOL_$_BWStillImageFilterStatusDelegate
+ __OBJC_METACLASS_RO_$_BWReactionAnalyticsPayload
+ __OBJC_PROTOCOL_$_BWStillImageFilterStatusDelegate
+ ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.100
+ ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.141
+ ___106-[FigCaptureClientApplicationStateMonitor _createAndObserveAVAudioSessionForBKSApplicationStateMonitoring]_block_invoke.284
+ ___157-[BWCoreImageFilterRenderer _renderUsingParameters:inputPixelBuffer:inputSampleBuffer:originalPixelBuffer:processedPixelBuffer:prewarming:completionHandler:]_block_invoke.1135
+ ___236-[BWStreamingCVAFilterRenderer initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:]_block_invoke
+ ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.256
+ ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke_2.259
+ ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke.181
+ ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke_2.182
+ ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke_3.183
+ ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.239
+ ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.242
+ ___54-[BWFigCaptureDeviceVendor activeDefaultDeviceEquals:]_block_invoke
+ ___54-[BWStillImageFilterNode renderSampleBuffer:forInput:]_block_invoke.72
+ ___56-[BWStillImageCoordinatorNode _attemptToCompleteRequest]_block_invoke
+ ___56-[BWStillImageCoordinatorNode _attemptToCompleteRequest]_block_invoke_2
+ ___60-[BWFigCaptureDeviceVendor _setupDeviceCloseTimerForDevice:]_block_invoke.215
+ ___64-[BWPhotoEncoderNode prepareForCurrentConfigurationToBecomeLive]_block_invoke.157
+ ___80-[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:]_block_invoke.28
+ ___81-[BWFigCaptureDeviceVendor _handleStreamControlTakenByAnotherClientNotification:]_block_invoke.219
+ ___81-[BWFigCaptureDeviceVendor _handleStreamRelinquishedByAnotherClientNotification:]_block_invoke.221
+ ___block_descriptor_72_e8_32o40o_e48_v32?0"NSNumber"8"PTEffectReactionState"16^B24ls32l8s40l8
+ ___block_descriptor_88_e8_32o40r48r56r64r72r80r_e39_B24?0"NSDictionary"8"NSDictionary"16ls32l8r40l8r48l8r56l8r64l8r72l8r80l8
+ ___block_literal_global.100
+ ___block_literal_global.115
+ ___block_literal_global.126
+ ___block_literal_global.153
+ ___block_literal_global.161
+ ___block_literal_global.169
+ ___block_literal_global.215
+ ___block_literal_global.245
+ ___block_literal_global.258
+ ___block_literal_global.276
+ ___block_literal_global.278
+ ___block_literal_global.418
+ ___block_literal_global.420
+ ___block_literal_global.484
+ ___block_literal_global.775
+ ___block_literal_global.81
+ ___block_literal_global.813
+ ___block_literal_global.85
+ ___block_literal_global.93
+ ___captureSource_postNotificationWithPayload_block_invoke
+ ___cmioefcd_devicePropertyKeyForCMIOExtensionProperty_block_invoke
+ ___cmioefcd_devicePropertyTypeForCMIOExtensionProperty_block_invoke
+ __unnamed_array_storage.107
+ __unnamed_array_storage.115
+ __unnamed_array_storage.124
+ __unnamed_array_storage.132
+ __unnamed_array_storage.138
+ __unnamed_array_storage.139
+ __unnamed_array_storage.147
+ __unnamed_array_storage.148
+ __unnamed_array_storage.152
+ __unnamed_array_storage.155
+ __unnamed_array_storage.164
+ __unnamed_array_storage.172
+ __unnamed_array_storage.179
+ __unnamed_array_storage.180
+ __unnamed_array_storage.187
+ __unnamed_array_storage.188
+ __unnamed_array_storage.211
+ __unnamed_array_storage.212
+ __unnamed_array_storage.219
+ __unnamed_array_storage.227
+ __unnamed_array_storage.235
+ __unnamed_array_storage.236
+ __unnamed_array_storage.251
+ __unnamed_array_storage.252
+ __unnamed_array_storage.259
+ __unnamed_array_storage.260
+ __unnamed_array_storage.267
+ __unnamed_array_storage.275
+ __unnamed_array_storage.276
+ __unnamed_array_storage.283
+ __unnamed_array_storage.291
+ __unnamed_array_storage.292
+ __unnamed_array_storage.299
+ __unnamed_array_storage.30
+ __unnamed_array_storage.300
+ __unnamed_array_storage.307
+ __unnamed_array_storage.316
+ __unnamed_array_storage.323
+ __unnamed_array_storage.331
+ __unnamed_array_storage.332
+ __unnamed_array_storage.339
+ __unnamed_array_storage.340
+ __unnamed_array_storage.346
+ __unnamed_array_storage.347
+ __unnamed_array_storage.348
+ __unnamed_array_storage.354
+ __unnamed_array_storage.356
+ __unnamed_array_storage.37
+ __unnamed_array_storage.372
+ __unnamed_array_storage.375
+ __unnamed_array_storage.380
+ __unnamed_array_storage.383
+ __unnamed_array_storage.386
+ __unnamed_array_storage.387
+ __unnamed_array_storage.392
+ __unnamed_array_storage.395
+ __unnamed_array_storage.396
+ __unnamed_array_storage.403
+ __unnamed_array_storage.404
+ __unnamed_array_storage.411
+ __unnamed_array_storage.412
+ __unnamed_array_storage.419
+ __unnamed_array_storage.427
+ __unnamed_array_storage.428
+ __unnamed_array_storage.435
+ __unnamed_array_storage.436
+ __unnamed_array_storage.443
+ __unnamed_array_storage.444
+ __unnamed_array_storage.451
+ __unnamed_array_storage.452
+ __unnamed_array_storage.459
+ __unnamed_array_storage.460
+ __unnamed_array_storage.468
+ __unnamed_array_storage.475
+ __unnamed_array_storage.476
+ __unnamed_array_storage.483
+ __unnamed_array_storage.484
+ __unnamed_array_storage.491
+ __unnamed_array_storage.492
+ __unnamed_array_storage.499
+ __unnamed_array_storage.500
+ __unnamed_array_storage.507
+ __unnamed_array_storage.508
+ __unnamed_array_storage.515
+ __unnamed_array_storage.516
+ __unnamed_array_storage.523
+ __unnamed_array_storage.531
+ __unnamed_array_storage.532
+ __unnamed_array_storage.539
+ __unnamed_array_storage.540
+ __unnamed_array_storage.547
+ __unnamed_array_storage.548
+ __unnamed_array_storage.555
+ __unnamed_array_storage.556
+ __unnamed_array_storage.563
+ __unnamed_array_storage.564
+ __unnamed_array_storage.571
+ __unnamed_array_storage.575
+ __unnamed_array_storage.595
+ __unnamed_array_storage.603
+ __unnamed_array_storage.606
+ __unnamed_array_storage.607
+ __unnamed_array_storage.610
+ __unnamed_array_storage.611
+ __unnamed_array_storage.614
+ __unnamed_array_storage.615
+ __unnamed_array_storage.618
+ __unnamed_array_storage.619
+ __unnamed_array_storage.622
+ __unnamed_array_storage.623
+ __unnamed_array_storage.626
+ __unnamed_array_storage.627
+ __unnamed_array_storage.630
+ __unnamed_array_storage.631
+ __unnamed_array_storage.634
+ __unnamed_array_storage.635
+ __unnamed_array_storage.638
+ __unnamed_array_storage.639
+ __unnamed_array_storage.642
+ __unnamed_array_storage.643
+ __unnamed_array_storage.646
+ __unnamed_array_storage.662
+ __unnamed_array_storage.663
+ __unnamed_array_storage.666
+ __unnamed_array_storage.667
+ __unnamed_array_storage.670
+ __unnamed_array_storage.671
+ __unnamed_array_storage.674
+ __unnamed_array_storage.675
+ __unnamed_array_storage.678
+ __unnamed_array_storage.679
+ __unnamed_array_storage.682
+ __unnamed_array_storage.683
+ __unnamed_array_storage.692
+ __unnamed_array_storage.693
+ __unnamed_array_storage.696
+ __unnamed_array_storage.697
+ __unnamed_array_storage.700
+ __unnamed_array_storage.701
+ __unnamed_array_storage.704
+ __unnamed_array_storage.705
+ __unnamed_array_storage.708
+ __unnamed_array_storage.709
+ __unnamed_array_storage.712
+ __unnamed_array_storage.713
+ __unnamed_array_storage.716
+ __unnamed_array_storage.717
+ __unnamed_array_storage.720
+ __unnamed_array_storage.721
+ __unnamed_array_storage.730
+ __unnamed_array_storage.731
+ __unnamed_array_storage.734
+ __unnamed_array_storage.735
+ __unnamed_array_storage.738
+ __unnamed_array_storage.739
+ __unnamed_array_storage.742
+ __unnamed_array_storage.743
+ __unnamed_array_storage.75
+ __unnamed_array_storage.752
+ __unnamed_array_storage.753
+ __unnamed_array_storage.762
+ __unnamed_array_storage.763
+ __unnamed_array_storage.766
+ __unnamed_array_storage.767
+ __unnamed_array_storage.770
+ __unnamed_array_storage.771
+ __unnamed_array_storage.774
+ __unnamed_array_storage.775
+ __unnamed_array_storage.778
+ __unnamed_array_storage.779
+ __unnamed_array_storage.782
+ __unnamed_array_storage.783
+ __unnamed_array_storage.786
+ __unnamed_array_storage.787
+ __unnamed_array_storage.790
+ __unnamed_array_storage.791
+ __unnamed_array_storage.794
+ __unnamed_array_storage.795
+ __unnamed_array_storage.804
+ __unnamed_array_storage.805
+ __unnamed_array_storage.808
+ __unnamed_array_storage.809
+ __unnamed_array_storage.812
+ __unnamed_array_storage.813
+ __unnamed_array_storage.816
+ __unnamed_array_storage.817
+ __unnamed_array_storage.820
+ __unnamed_array_storage.821
+ __unnamed_array_storage.824
+ __unnamed_array_storage.825
+ __unnamed_array_storage.828
+ __unnamed_array_storage.829
+ __unnamed_array_storage.832
+ __unnamed_array_storage.833
+ __unnamed_array_storage.836
+ __unnamed_array_storage.837
+ __unnamed_array_storage.84
+ __unnamed_array_storage.846
+ __unnamed_array_storage.847
+ __unnamed_array_storage.850
+ __unnamed_array_storage.851
+ __unnamed_array_storage.854
+ __unnamed_array_storage.855
+ __unnamed_array_storage.858
+ __unnamed_array_storage.865
+ __unnamed_array_storage.869
+ __unnamed_array_storage.870
+ __unnamed_array_storage.873
+ __unnamed_array_storage.874
+ __unnamed_array_storage.877
+ __unnamed_array_storage.878
+ __unnamed_array_storage.881
+ __unnamed_array_storage.882
+ __unnamed_array_storage.885
+ __unnamed_array_storage.886
+ __unnamed_array_storage.889
+ __unnamed_array_storage.890
+ __unnamed_array_storage.893
+ __unnamed_array_storage.894
+ __unnamed_array_storage.897
+ __unnamed_array_storage.898
+ __unnamed_array_storage.901
+ __unnamed_array_storage.902
+ __unnamed_array_storage.905
+ __unnamed_array_storage.906
+ __unnamed_array_storage.915
+ __unnamed_array_storage.916
+ __unnamed_array_storage.919
+ __unnamed_array_storage.92
+ __unnamed_array_storage.920
+ __unnamed_array_storage.923
+ __unnamed_array_storage.924
+ __unnamed_array_storage.927
+ __unnamed_array_storage.928
+ __unnamed_array_storage.931
+ __unnamed_array_storage.932
+ __unnamed_array_storage.935
+ __unnamed_array_storage.936
+ __unnamed_array_storage.939
+ __unnamed_array_storage.940
+ __unnamed_array_storage.943
+ __unnamed_array_storage.944
+ __unnamed_array_storage.953
+ __unnamed_array_storage.954
+ __unnamed_array_storage.957
+ __unnamed_array_storage.958
+ __unnamed_array_storage.961
+ __unnamed_array_storage.962
+ __unnamed_array_storage.965
+ __unnamed_array_storage.966
+ __unnamed_array_storage.975
+ __unnamed_array_storage.979
+ __unnamed_array_storage.98
+ __unnamed_array_storage.982
+ __unnamed_array_storage.983
+ _cmioefcd_devicePropertyKeyForCMIOExtensionProperty.onceToken
+ _cmioefcd_devicePropertyKeyForCMIOExtensionProperty.sDevicePropertyKeysByCMIOExtensionPropertyNames
+ _cmioefcd_devicePropertyTypeForCMIOExtensionProperty.onceToken
+ _cmioefcd_devicePropertyTypeForCMIOExtensionProperty.sDevicePropertyTypeByCMIOExtensionPropertyNames
+ _gBWDepthConverterNodeTrace
+ _gBWInferenceSynchronizerNode
+ _gBWStreamingFilterNodeTrace
+ _kBWNodeSampleBufferAttachmentKey_IsHarvestedUltraHighResolutionStillFrame
+ _kCMPhotoCompressionOption_ProvidedImageHandle
+ _kCMPhotoCompressionOption_ReserveImageHandle
+ _kFigAppleMakerNote_AFSphereComplianceErrorCounts
+ _kFigAppleMakerNote_AFSphereComplianceErrorCountsKey_AF
+ _kFigAppleMakerNote_AFSphereComplianceErrorCountsKey_Sphere
+ _kFigAppleMakerNote_AFSphereFaultStatus
+ _kFigAppleMakerNote_AFSphereMaxTemperature
+ _kFigAppleMakerNote_AFSphereMaxTemperatureKey_AF
+ _kFigAppleMakerNote_AFSphereMaxTemperatureKey_SphereX
+ _kFigAppleMakerNote_AFSphereMaxTemperatureKey_SphereY
+ _kFigAppleMakerNote_SensorBlackLevelResidual
+ _kFigCaptureDeviceNotification_CMIODeviceTrackingActiveChanged
+ _kFigCaptureFlatDictionaryAppleMakerNote_AFSphereFaultStatus
+ _kFigCaptureFlatDictionaryAppleMakerNote_AFSphereFaultStatus_opaque
+ _kFigCaptureFlatDictionaryAppleMakerNote_AFSphereFaultStatus_string
+ _kFigCaptureFlatDictionaryAppleMakerNote_SensorBlackLevelResidual
+ _kFigCaptureFlatDictionaryAppleMakerNote_SensorBlackLevelResidual_opaque
+ _kFigCaptureFlatDictionaryAppleMakerNote_SensorBlackLevelResidual_string
+ _kFigCaptureStreamAutoFocusPositionSensorHealthKey_ComplianceErrorCount
+ _kFigCaptureStreamAutoFocusPositionSensorHealthKey_ElectricalShortRecoveryFailed
+ _kFigCaptureStreamAutoFocusPositionSensorHealthKey_MacroInstabilityRecoveryFailed
+ _kFigCaptureStreamAutoFocusPositionSensorHealthKey_MotionInstabilityDetected
+ _kFigCaptureStreamAutoFocusPositionSensorHealthKey_TemperatureMax
+ _kFigCaptureStreamAutoFocusPositionSensorHealthKey_ThermalRecoveryFailed
+ _kFigCaptureStreamMetadata_SensorBlackLevelResidualFiltered
+ _kFigCaptureStreamMetadata_SensorBlackLevelResidualInstantaneous
+ _kFigCaptureStreamSphereControllerHealthKey_ComplianceErrorCount
+ _kFigCaptureStreamSphereControllerHealthKey_ElectricalShortRecoveryFailed
+ _kFigCaptureStreamSphereControllerHealthKey_ElectrostaticInstabilityRecoveryFailed
+ _kFigCaptureStreamSphereControllerHealthKey_MotionInstabilityDetected
+ _kFigCaptureStreamSphereControllerHealthKey_TemperatureMaxX
+ _kFigCaptureStreamSphereControllerHealthKey_TemperatureMaxY
+ _kFigCaptureStreamSphereControllerHealthKey_ThermalRecoveryFailed
+ _kFigCaptureStreamTimeOfFlightAssistedAutoFocusEstimatorResultsKey_APEStatus
+ _objc_msgSend$_initWithNodeConfiguration:sensorConfigurationsByPortType:statusDelegate:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:renderResourceProvider:
+ _objc_msgSend$_postNotificationWithPayload:notificationPayload:
+ _objc_msgSend$activeDefaultDeviceEquals:
+ _objc_msgSend$addAuxImage:type:auxImageMetadata:options:parentImageHandle:
+ _objc_msgSend$addMainImage:metadata:options:imageHandleOut:
+ _objc_msgSend$addMetadata:parentImageHandle:
+ _objc_msgSend$addThumbnailImage:options:parentImageHandle:
+ _objc_msgSend$bundleURL
+ _objc_msgSend$clientExpectsCameraMountedInLandscapeOrientation
+ _objc_msgSend$compressionResourcesAllocated
+ _objc_msgSend$computeOpticalFlow:inRGBA:outDisplacement:
+ _objc_msgSend$filterNodeDidReceiveStandardResolutionDeepFusionBuffer:error:
+ _objc_msgSend$freeBufferCountIncreasedHandler
+ _objc_msgSend$getCurrentDetectedObjectsAndPTS:
+ _objc_msgSend$getInUseCompressedBufferCount:inUseCompressedBytes:maxInUseCompressedBytes:forUncompressedEquivalentFreeBufferCount:
+ _objc_msgSend$hasUncompressedEquivalentFreeBufferCount:
+ _objc_msgSend$initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:portraitPreviewForegroundBlurEnabled:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:
+ _objc_msgSend$initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:
+ _objc_msgSend$initWithInputRequirement:opticalFlowInputRequirement:outputRequirement:resourceProvider:configuration:
+ _objc_msgSend$initWithNodeConfiguration:sensorConfigurationsByPortType:statusDelegate:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:
+ _objc_msgSend$initWithReadableByteStream:forFrontFacingCamera:forExternalCamera:clientExpectsCameraMountedInLandscapeOrientation:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:
+ _objc_msgSend$initWithRefInputRequirement:auxInputRequirement:refKeypointsInputRequirement:auxKeypointsInputRequirement:refOutputRequirement:auxOutputRequirement:opticalFlowOutputRequirement:originalRefRequirement:originalAuxRequirement:resourceProvider:configuration:
+ _objc_msgSend$loadArchiveWithName:fromURL:
+ _objc_msgSend$minimumUncompressedEquivalentCapacity
+ _objc_msgSend$officialFocalLengthMultiplier
+ _objc_msgSend$officialFocalLengthMultiplierByPortType
+ _objc_msgSend$passthroughEnabled
+ _objc_msgSend$processPixelBuffer:pts:
+ _objc_msgSend$reactionCount
+ _objc_msgSend$releasePrewarmingResources
+ _objc_msgSend$setClientExpectsCameraMountedInLandscapeOrientation:
+ _objc_msgSend$setFreeBufferCountIncreasedHandler:
+ _objc_msgSend$setOfficialFocalLengthMultiplierByPortType:
+ _objc_msgSend$setOrientationLandscapeTime:
+ _objc_msgSend$setOrientationPortraitTime:
+ _objc_msgSend$setReactionCount:
+ _objc_msgSend$setReactionType:
+ _objc_msgSend$setResourceOptions:
+ _objc_msgSend$setThermalThrottledTime:
+ _objc_msgSend$setUltraWideActive:
+ _objc_msgSend$setVideoCaptureDimensionsIncludeVISOverscan:
+ _objc_msgSend$smartCameraRequired
+ _objc_msgSend$streamingTime
+ _objc_msgSend$temporalDisparityFilter:inDisparity:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:
+ _objc_msgSend$uiTriggeredReaction
+ _objc_msgSend$videoCaptureDimensionsIncludeVISOverscan
+ _sDeviceSWFRVersion
- -[BWCMPhotoCompressionSession addAuxImage:type:auxImageMetadata:options:]
- -[BWCMPhotoCompressionSession addMainImage:metadata:options:]
- -[BWCMPhotoCompressionSession addMetadata:]
- -[BWCMPhotoCompressionSession addThumbnailImage:options:]
- -[BWDNGCompressionSession addAuxImage:type:auxImageMetadata:options:]
- -[BWDNGCompressionSession addMainImage:metadata:options:]
- -[BWDNGCompressionSession addMetadata:]
- -[BWDNGCompressionSession addThumbnailImage:options:]
- -[BWDerectificationInferenceProvider initWithInputRequirement:outputRequirement:resourceProvider:configuration:]
- -[BWFigCaptureDeviceVendor _logActiveDeviceClientAndDevice]
- -[BWFigCaptureDeviceVendor activeDeviceEquals:]
- -[BWIrisMovieGenerator initWithReadableByteStream:forFrontFacingCamera:forExternalCamera:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:]
- -[BWIrisMovieGenerator initWithReadableByteStream:metadataByteStream:forFrontFacingCamera:forExternalCamera:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:]
- -[BWPhotoEncoderNode _addAuxImagesIfNeededForEncodingScheme:sampleBuffer:metadata:stillImageSettings:processingFlags:embedThumbToCompressedImage:]
- -[BWPhotoEncoderNode _addDepthForEncodingScheme:sampleBuffer:primaryOutputAspectRatio:]
- -[BWPhotoEncoderNode _addGainMapForEncodingScheme:sampleBuffer:outputWidth:outputHeight:primaryOutputAspectRatio:]
- -[BWPhotoEncoderNode _addMetadataAttachmentsForEncodingScheme:sampleBuffer:requestedSettings:captureType:]
- -[BWPhotoEncoderNode _addPortraitEffectsMatteForEncodingScheme:sampleBuffer:primaryOutputAspectRatio:]
- -[BWPhotoEncoderNode _addSemanticMatteToCompressionSession:sampleBuffer:attachedMediaKey:auxImageType:primaryOutputAspectRatio:sourceCropRectKey:processingFlags:orientation:]
- -[BWPhotoEncoderNode _addSemanticMattesForEncodingScheme:semanticSegmentationMatteURNs:sampleBuffer:primaryOutputAspectRatio:settingsID:processingFlags:orientation:]
- -[BWPhotoEncoderNode _addThumbnailForEncodingScheme:thumbnailPixelBuffer:metadata:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:processingFlags:cropRect:codecType:maxPixelSize:]
- -[BWPhotoEncoderNode _encodePhotoForEncodingScheme:pixelBuffer:imageDimensions:processingFlags:metadata:thumbnailOptions:requestedStillImageCaptureSettings:resolvedStillImageCaptureSettings:cropRect:usePixelsOutsideCrop:]
- -[BWRectificationInferenceProvider initWithRefInputRequirement:auxInputRequirement:refKeypointsInputRequirement:auxKeypointsInputRequirement:refOutputRequirement:auxOutputRequirement:originalRefRequirement:originalAuxRequirement:resourceProvider:configuration:]
- -[BWStillImageFilterNode _initWithNodeConfiguration:sensorConfigurationsByPortType:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:renderResourceProvider:]
- -[BWStillImageFilterNode initWithNodeConfiguration:sensorConfigurationsByPortType:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:]
- -[BWStreamingCVAFilterRenderer initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:commandQueue:priority:]
- -[BWStreamingFilterNode initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:portraitPreviewForegroundBlurEnabled:metalCommandQueue:priority:]
- -[FigCaptureCameraSourcePipeline captureDimensionsForFSDNetSecondary]
- -[FigCaptureCameraSourcePipeline videoCaptureOutputTransform]
- -[FigCaptureCinematographyPipelineConfiguration setCaptureDimensionsForFSDNetSecondary:]
- GCC_except_table133
- GCC_except_table173
- GCC_except_table214
- GCC_except_table236
- GCC_except_table253
- GCC_except_table283
- GCC_except_table284
- GCC_except_table302
- GCC_except_table304
- GCC_except_table318
- GCC_except_table336
- GCC_except_table411
- GCC_except_table412
- GCC_except_table56
- GCC_except_table92
- GCC_except_table96
- GCC_except_table99
- _.compoundliteral.23
- _.compoundliteral.24
- _.compoundliteral.27
- _.compoundliteral.40
- _.compoundliteral.59
- _.compoundliteral.62
- _.compoundliteral.63
- _.compoundliteral.64
- _.compoundliteral.65
- _.compoundliteral.66
- _.compoundliteral.67
- _.compoundliteral.68
- _.compoundliteral.74
- _.compoundliteral.79
- _.compoundliteral.80
- _OBJC_IVAR_$_BWBackgroundBlurNode._reactionCounter
- _OBJC_IVAR_$_FigCaptureCinematographyPipelineConfiguration._captureDimensionsForFSDNetSecondary
- __OBJC_$_PROP_LIST_FigCaptureConnectionConfiguration
- ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.121
- ___104-[BWVideoDepthInferenceAdapter inferenceProvidersForType:version:configuration:resourceProvider:status:]_block_invoke.138
- ___106-[FigCaptureClientApplicationStateMonitor _createAndObserveAVAudioSessionForBKSApplicationStateMonitoring]_block_invoke.278
- ___157-[BWCoreImageFilterRenderer _renderUsingParameters:inputPixelBuffer:inputSampleBuffer:originalPixelBuffer:processedPixelBuffer:prewarming:completionHandler:]_block_invoke.1129
- ___169-[BWStreamingCVAFilterRenderer initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:commandQueue:priority:]_block_invoke
- ___47-[BWFigCaptureDeviceVendor activeDeviceEquals:]_block_invoke
- ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke.252
- ___50-[BWFigVideoCaptureDevice _deviceDidStopStreaming]_block_invoke_2.255
- ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke.183
- ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke_2.184
- ___50-[BWPhotoEncoderNode renderSampleBuffer:forInput:]_block_invoke_3.185
- ___52-[BWFigVideoCaptureDevice _deviceWillStartStreaming]_block_invoke.238
- ___54-[BWStillImageFilterNode renderSampleBuffer:forInput:]_block_invoke.66
- ___60-[BWFigCaptureDeviceVendor _setupDeviceCloseTimerForDevice:]_block_invoke.210
- ___64-[BWPhotoEncoderNode prepareForCurrentConfigurationToBecomeLive]_block_invoke.159
- ___80-[BWCameraStreamingMonitor _informSystemStatusWithIsStreaming:clientAuditToken:]_block_invoke.27
- ___81-[BWFigCaptureDeviceVendor _handleStreamControlTakenByAnotherClientNotification:]_block_invoke.214
- ___81-[BWFigCaptureDeviceVendor _handleStreamRelinquishedByAnotherClientNotification:]_block_invoke.216
- ___block_descriptor_64_e8_32o_e48_v32?0"NSNumber"8"PTEffectReactionState"16^B24ls32l8
- ___block_descriptor_72_e8_32o40r48r56r64r_e39_B24?0"NSDictionary"8"NSDictionary"16ls32l8r40l8r48l8r56l8r64l8
- ___block_literal_global.102
- ___block_literal_global.123
- ___block_literal_global.147
- ___block_literal_global.160
- ___block_literal_global.179
- ___block_literal_global.206
- ___block_literal_global.239
- ___block_literal_global.254
- ___block_literal_global.272
- ___block_literal_global.274
- ___block_literal_global.406
- ___block_literal_global.408
- ___block_literal_global.410
- ___block_literal_global.412
- ___block_literal_global.488
- ___block_literal_global.62
- ___block_literal_global.770
- ___block_literal_global.78
- ___block_literal_global.808
- ___block_literal_global.92
- __unnamed_array_storage.102
- __unnamed_array_storage.110
- __unnamed_array_storage.113
- __unnamed_array_storage.118
- __unnamed_array_storage.130
- __unnamed_array_storage.135
- __unnamed_array_storage.142
- __unnamed_array_storage.145
- __unnamed_array_storage.150
- __unnamed_array_storage.165
- __unnamed_array_storage.174
- __unnamed_array_storage.182
- __unnamed_array_storage.190
- __unnamed_array_storage.197
- __unnamed_array_storage.198
- __unnamed_array_storage.214
- __unnamed_array_storage.221
- __unnamed_array_storage.222
- __unnamed_array_storage.237
- __unnamed_array_storage.238
- __unnamed_array_storage.245
- __unnamed_array_storage.246
- __unnamed_array_storage.253
- __unnamed_array_storage.262
- __unnamed_array_storage.269
- __unnamed_array_storage.270
- __unnamed_array_storage.272
- __unnamed_array_storage.277
- __unnamed_array_storage.285
- __unnamed_array_storage.286
- __unnamed_array_storage.293
- __unnamed_array_storage.294
- __unnamed_array_storage.297
- __unnamed_array_storage.301
- __unnamed_array_storage.310
- __unnamed_array_storage.325
- __unnamed_array_storage.326
- __unnamed_array_storage.333
- __unnamed_array_storage.334
- __unnamed_array_storage.338
- __unnamed_array_storage.341
- __unnamed_array_storage.345
- __unnamed_array_storage.357
- __unnamed_array_storage.360
- __unnamed_array_storage.365
- __unnamed_array_storage.366
- __unnamed_array_storage.368
- __unnamed_array_storage.373
- __unnamed_array_storage.374
- __unnamed_array_storage.381
- __unnamed_array_storage.382
- __unnamed_array_storage.389
- __unnamed_array_storage.397
- __unnamed_array_storage.398
- __unnamed_array_storage.405
- __unnamed_array_storage.406
- __unnamed_array_storage.413
- __unnamed_array_storage.421
- __unnamed_array_storage.422
- __unnamed_array_storage.429
- __unnamed_array_storage.430
- __unnamed_array_storage.437
- __unnamed_array_storage.445
- __unnamed_array_storage.446
- __unnamed_array_storage.453
- __unnamed_array_storage.454
- __unnamed_array_storage.461
- __unnamed_array_storage.462
- __unnamed_array_storage.469
- __unnamed_array_storage.470
- __unnamed_array_storage.477
- __unnamed_array_storage.478
- __unnamed_array_storage.485
- __unnamed_array_storage.486
- __unnamed_array_storage.493
- __unnamed_array_storage.494
- __unnamed_array_storage.501
- __unnamed_array_storage.502
- __unnamed_array_storage.509
- __unnamed_array_storage.510
- __unnamed_array_storage.517
- __unnamed_array_storage.518
- __unnamed_array_storage.525
- __unnamed_array_storage.526
- __unnamed_array_storage.533
- __unnamed_array_storage.534
- __unnamed_array_storage.541
- __unnamed_array_storage.542
- __unnamed_array_storage.549
- __unnamed_array_storage.550
- __unnamed_array_storage.557
- __unnamed_array_storage.558
- __unnamed_array_storage.565
- __unnamed_array_storage.566
- __unnamed_array_storage.569
- __unnamed_array_storage.589
- __unnamed_array_storage.590
- __unnamed_array_storage.597
- __unnamed_array_storage.599
- __unnamed_array_storage.600
- __unnamed_array_storage.601
- __unnamed_array_storage.604
- __unnamed_array_storage.605
- __unnamed_array_storage.608
- __unnamed_array_storage.609
- __unnamed_array_storage.612
- __unnamed_array_storage.613
- __unnamed_array_storage.616
- __unnamed_array_storage.617
- __unnamed_array_storage.62
- __unnamed_array_storage.620
- __unnamed_array_storage.621
- __unnamed_array_storage.624
- __unnamed_array_storage.625
- __unnamed_array_storage.628
- __unnamed_array_storage.629
- __unnamed_array_storage.632
- __unnamed_array_storage.633
- __unnamed_array_storage.636
- __unnamed_array_storage.637
- __unnamed_array_storage.640
- __unnamed_array_storage.656
- __unnamed_array_storage.657
- __unnamed_array_storage.660
- __unnamed_array_storage.661
- __unnamed_array_storage.664
- __unnamed_array_storage.665
- __unnamed_array_storage.668
- __unnamed_array_storage.669
- __unnamed_array_storage.672
- __unnamed_array_storage.673
- __unnamed_array_storage.676
- __unnamed_array_storage.677
- __unnamed_array_storage.680
- __unnamed_array_storage.687
- __unnamed_array_storage.69
- __unnamed_array_storage.690
- __unnamed_array_storage.691
- __unnamed_array_storage.694
- __unnamed_array_storage.695
- __unnamed_array_storage.698
- __unnamed_array_storage.699
- __unnamed_array_storage.702
- __unnamed_array_storage.703
- __unnamed_array_storage.706
- __unnamed_array_storage.707
- __unnamed_array_storage.710
- __unnamed_array_storage.711
- __unnamed_array_storage.714
- __unnamed_array_storage.715
- __unnamed_array_storage.718
- __unnamed_array_storage.725
- __unnamed_array_storage.728
- __unnamed_array_storage.729
- __unnamed_array_storage.732
- __unnamed_array_storage.733
- __unnamed_array_storage.736
- __unnamed_array_storage.737
- __unnamed_array_storage.740
- __unnamed_array_storage.747
- __unnamed_array_storage.750
- __unnamed_array_storage.757
- __unnamed_array_storage.760
- __unnamed_array_storage.761
- __unnamed_array_storage.764
- __unnamed_array_storage.765
- __unnamed_array_storage.768
- __unnamed_array_storage.769
- __unnamed_array_storage.77
- __unnamed_array_storage.772
- __unnamed_array_storage.773
- __unnamed_array_storage.776
- __unnamed_array_storage.777
- __unnamed_array_storage.78
- __unnamed_array_storage.780
- __unnamed_array_storage.781
- __unnamed_array_storage.784
- __unnamed_array_storage.785
- __unnamed_array_storage.788
- __unnamed_array_storage.789
- __unnamed_array_storage.792
- __unnamed_array_storage.793
- __unnamed_array_storage.799
- __unnamed_array_storage.802
- __unnamed_array_storage.806
- __unnamed_array_storage.807
- __unnamed_array_storage.810
- __unnamed_array_storage.811
- __unnamed_array_storage.814
- __unnamed_array_storage.815
- __unnamed_array_storage.818
- __unnamed_array_storage.819
- __unnamed_array_storage.822
- __unnamed_array_storage.823
- __unnamed_array_storage.826
- __unnamed_array_storage.827
- __unnamed_array_storage.830
- __unnamed_array_storage.831
- __unnamed_array_storage.834
- __unnamed_array_storage.841
- __unnamed_array_storage.844
- __unnamed_array_storage.845
- __unnamed_array_storage.848
- __unnamed_array_storage.849
- __unnamed_array_storage.85
- __unnamed_array_storage.852
- __unnamed_array_storage.860
- __unnamed_array_storage.863
- __unnamed_array_storage.864
- __unnamed_array_storage.867
- __unnamed_array_storage.868
- __unnamed_array_storage.871
- __unnamed_array_storage.872
- __unnamed_array_storage.875
- __unnamed_array_storage.876
- __unnamed_array_storage.879
- __unnamed_array_storage.880
- __unnamed_array_storage.883
- __unnamed_array_storage.884
- __unnamed_array_storage.887
- __unnamed_array_storage.888
- __unnamed_array_storage.891
- __unnamed_array_storage.892
- __unnamed_array_storage.895
- __unnamed_array_storage.896
- __unnamed_array_storage.899
- __unnamed_array_storage.900
- __unnamed_array_storage.903
- __unnamed_array_storage.910
- __unnamed_array_storage.913
- __unnamed_array_storage.914
- __unnamed_array_storage.917
- __unnamed_array_storage.918
- __unnamed_array_storage.921
- __unnamed_array_storage.922
- __unnamed_array_storage.925
- __unnamed_array_storage.926
- __unnamed_array_storage.929
- __unnamed_array_storage.93
- __unnamed_array_storage.930
- __unnamed_array_storage.933
- __unnamed_array_storage.934
- __unnamed_array_storage.937
- __unnamed_array_storage.938
- __unnamed_array_storage.94
- __unnamed_array_storage.941
- __unnamed_array_storage.948
- __unnamed_array_storage.951
- __unnamed_array_storage.952
- __unnamed_array_storage.955
- __unnamed_array_storage.956
- __unnamed_array_storage.959
- __unnamed_array_storage.960
- __unnamed_array_storage.963
- __unnamed_array_storage.970
- __unnamed_array_storage.973
- __unnamed_array_storage.977
- _cmioefcd_copyDockedTrackingActive
- _kCICCPortraitBinaryArchive
- _objc_msgSend$_initWithNodeConfiguration:sensorConfigurationsByPortType:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:renderResourceProvider:
- _objc_msgSend$activeDeviceEquals:
- _objc_msgSend$addAuxImage:type:auxImageMetadata:options:
- _objc_msgSend$addMainImage:metadata:options:
- _objc_msgSend$addThumbnailImage:options:
- _objc_msgSend$initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:portraitPreviewForegroundBlurEnabled:metalCommandQueue:priority:
- _objc_msgSend$initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:commandQueue:priority:
- _objc_msgSend$initWithInputRequirement:outputRequirement:resourceProvider:configuration:
- _objc_msgSend$initWithNodeConfiguration:sensorConfigurationsByPortType:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:
- _objc_msgSend$initWithReadableByteStream:forFrontFacingCamera:forExternalCamera:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:
- _objc_msgSend$initWithRefInputRequirement:auxInputRequirement:refKeypointsInputRequirement:auxKeypointsInputRequirement:refOutputRequirement:auxOutputRequirement:originalRefRequirement:originalAuxRequirement:resourceProvider:configuration:
- _sDeviceUsesSWFR2
CStrings:
+ "\"low quality\""
+ "\"missing\""
+ "%@:%d,"
+ ", cameraMountedInLandscape: YES"
+ "-[BWDepthConverterNode renderSampleBuffer:forInput:]"
+ "-[BWDepthSynchronizerNode _tryToEmitBuffers]"
+ "-[BWFigCaptureDeviceVendor _logActiveDefaultDeviceClientAndDevice]"
+ "-[BWFigVideoCaptureDevice _reportDeskViewStreamingSessionCoreAnalyticsData]"
+ "-[BWFigVideoCaptureDevice _reportStreamingSessionCoreAnalyticsData]"
+ "-[BWFigVideoCaptureDevice setDeskCamActive:]"
+ "-[BWFigVideoCaptureDevice setUltraWideActive:]"
+ "-[BWFigVideoCaptureStream sourceNodeShouldDiscardStillImageSampleBuffer:sensorRawOutput:]"
+ "-[BWInferenceSynchronizerNode _attemptBufferOrErrorEmission]"
+ "-[BWIrisMovieGenerator initWithReadableByteStream:metadataByteStream:forFrontFacingCamera:forExternalCamera:clientExpectsCameraMountedInLandscapeOrientation:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:]"
+ "-[BWPhotoEncoderNode _addAuxImagesIfNeededForEncodingScheme:sampleBuffer:metadata:stillImageSettings:processingFlags:embedThumbToCompressedImage:parentImageHandle:parentImageAdded:]"
+ "-[BWPhotoEncoderNode _addSemanticMattesForEncodingScheme:semanticSegmentationMatteURNs:sampleBuffer:primaryOutputAspectRatio:settingsID:processingFlags:orientation:parentImageHandle:]"
+ "-[BWPhotonicEngineNode _clearPortraitSemaphoreWithError:]"
+ "-[BWPhotonicEngineNode _handleSampleBuffer:input:]"
+ "-[BWStreamingFilterNode renderSampleBuffer:forInput:]"
+ "<<<< BWDepthConverterNode >>>> %s: Depth processing %{public}@ for captureID:%{public}lld d:%{public}d (%{public}d)"
+ "<<<< BWDepthConverterNode >>>> %s: Structured light projector or the infrared sensor were occluded for captureID:%{public}lld (%{public}d), dropping depth for input: %{private}@"
+ "<<<< BWDepthSynchronizerNode >>>> %s: [%{private}@] captureID:%{public}lld [cid:%{public}d ocid:%{public}d]: emit:1, fll:%{public}d, exp:%{public}d, d:%{public}d, mss:%{public}d, e:%{public}d (%{public}lld)"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Reporting Desk View specific analytics data with total running time %.2f seconds"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Reporting streaming session analytics data for device %@ with total running time %.2f seconds"
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Start streaming on Desk View (ultra wide + Desk View hybrid use case)."
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Start streaming on ultra wide (ultra wide + Desk View hybrid use case)."
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Stop streaming on Desk View (ultra wide + Desk View hybrid use case)."
+ "<<<< BWFigVideoCaptureDevice >>>> %s: Stop streaming on ultra wide (ultra wide + Desk View hybrid use case)."
+ "<<<< BWFigVideoCaptureStream >>>> %s: Capture frame info for %{public}@: %{public}@"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Discarding still image buffer: Expected:%{public}d, rawOutput:%{public}d, TM:%{public}d, B:%{public}d, SIFR:%{public}d (captureID:%{public}lld)"
+ "<<<< BWFigVideoCaptureStream >>>> %s: Missing capture frame infos for %{public}@"
+ "<<<< BWInferenceSynchronizerNode >>>> %s: [%{private}@] captureID:%{public}lld [cid:%{public}d]: emit:1, fll:%{public}d, mss:%{public}d, skp:%{public}d, i:%{public}d"
+ "<<<< BWIntelligentDistortionCorrectionProcessorController >>>> %s: Processing with gdc:%{public}d, idc:%{public}d, z:%{public}d i:%{public}d seg:%{public}d a:%{public}@ f:%{public}lu s:%{public}d, c:%{public}@ v:%{public}@ o:%{public}d trg:%{public}dx%{public}d r:%{public}d"
+ "<<<< BWIrisStagingNode >>>> %s: Adjusting PTS for harvested ultra high resolution still frame %.4f -> %.4f offset %.4f"
+ "<<<< BWMultiStreamCameraSourceNode >>>> %s: Discarding still image buffer from %{public}@: %{public}@"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: [Compressed Shot Buffer] Done capturing, but waiting for uncompressedEquivalentFreeBufferCount %d. In use compressed buffers %d, in use memory %.1f MB, max %.1f MB"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: [Compressed Shot Buffer] Done waiting for compressed buffer to be returned. Target uncompressedEquivalentFreeBufferCount %d, in use compressed buffers %d, in use memory %.1f MB, max %.1f MB"
+ "<<<< BWStillImageCoordinatorNode >>>> %s: [Compressed Shot Buffer] Updating compressed shot buffer capacity %d -> %d, uncompressed shot buffer capacity to %d, max %d"
+ "<<<< BWStillImageFilterNode >>>> %s: Unable to apply any filters requiring depth (%{public}@ for captureID:%{public}lld), and these are the only filters to apply.  An adjusted image will not be returned (%{public}d)."
+ "<<<< BWStillImageProcessingNode >>>> %s: Clearing portrait semaphore; status: %d"
+ "<<<< BWStillImageProcessingNode >>>> %s: Received %{public}@ on %{public}@ input (captureID:%{public}lld)"
+ "<<<< BWStreamingFilterNode >>>> %s: Structured light projector or the infrared sensor were occluded for %{private}@"
+ "<<<< FigCaptureSession >>>> %s: %{public}s Ignoring stream controlled by another client because the session is stopping"
+ "@\"<BWStillImageFilterStatusDelegate>\""
+ "@\"NSDateFormatter\""
+ "@104@0:8@16@24@32@40@48@56@64@72@80@88@96"
+ "@24@0:8^{?=qiIq}16"
+ "@60@0:8@16B24B28i32B36@40I48B52i56"
+ "@60@0:8@16i24B28B32B36@40I48B52i56"
+ "@64@0:8^{OpaqueCMByteStream=}16B24B28B32B36@40@48@56"
+ "@76@0:8@16@24@32B40B44B48i52f56@60f68B72"
+ "@84@0:8@16@24@32B40B44B48i52f56@60f68B72@76"
+ "@?<v@?>16@0:8"
+ "APEStatus"
+ "BWReactionAnalyticsPayload"
+ "BWStillImageFilterStatusDelegate"
+ "CMISoftwareFlashRenderingProcessorV%d"
+ "Could not bind opticalFlowOutput to texture"
+ "DeviceID"
+ "DeviceTrackingActiveChanged"
+ "DisparityFilteringOpticalFlow"
+ "IsHarvestedUltraHighResolutionStillFrame"
+ "LowResPerson"
+ "OfficialFocalLengthMultiplier"
+ "Optical flow failed"
+ "T@\"NSDictionary\",&,N,V_officialFocalLengthMultiplierByPortType"
+ "T@\"NSString\",C,N,V_reactionType"
+ "TB,N,GisUltraWideStreamActive,V_ultraWideActive"
+ "TB,N,V_clientExpectsCameraMountedInLandscapeOrientation"
+ "TB,N,V_uiTriggeredReaction"
+ "TB,N,V_videoCaptureDimensionsIncludeVISOverscan"
+ "TI,N,V_orientationLandscapeTime"
+ "TI,N,V_orientationPortraitTime"
+ "TI,N,V_reactionCount"
+ "TI,N,V_thermalThrottledTime"
+ "Ti,N,V_cameraPosture"
+ "Unable to get optical flow input pixel buffer"
+ "Unable to get optical flow pixel buffer from pool"
+ "_adjustedPhotoReservedParentImageHandle"
+ "_clientExpectsCameraMountedInLandscapeOrientation"
+ "_compressWhenCompressedBuffersInUseEnabled"
+ "_deepZoomProEnhancedResolutionPortraitSemaphore"
+ "_deepZoomProEnhancedResolutionPortraitSemaphoreLock"
+ "_deskCamStartTime"
+ "_deviceDateFormatter"
+ "_disparityIntermediate"
+ "_eligibleAuxImagesWereAddedToAdjustedPhotoContainer"
+ "_freeBufferCountIncreasedHandler"
+ "_initWithNodeConfiguration:sensorConfigurationsByPortType:statusDelegate:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:renderResourceProvider:"
+ "_lastIsQsubFrame"
+ "_mirroredForMetadataAdjustment"
+ "_normalResolutionOverlapCapacityForSoQ"
+ "_objectMetadataDictionaryPTS"
+ "_officialFocalLengthMultiplier"
+ "_officialFocalLengthMultiplierByPortType"
+ "_opticalFlowDescriptor"
+ "_opticalFlowInputDescriptor"
+ "_opticalFlowInputRequirement"
+ "_opticalFlowOutputRequirement"
+ "_orientationCurrent"
+ "_orientationLandscapeTime"
+ "_orientationLandscapeTotalTime"
+ "_orientationPortraitTime"
+ "_orientationPortraitTotalTime"
+ "_orientationStartTime"
+ "_passthroughEnabled"
+ "_perFrameLoggingRatio"
+ "_postNotificationWithPayload:notificationPayload:"
+ "_reachedEndOfData"
+ "_reactionCount"
+ "_reactionCounterAPI"
+ "_reactionCounterAll"
+ "_reactionType"
+ "_reactionsCount"
+ "_receivedFrameCounter"
+ "_rotationDegreesForMetadataAdjustment"
+ "_shouldLogPerFrameLogging"
+ "_thermalThrottledStartTime"
+ "_thermalThrottledTime"
+ "_uiTriggeredReaction"
+ "_ultraWideActive"
+ "_videoCaptureDimensionsIncludeVISOverscan"
+ "activeDefaultDeviceEquals:"
+ "addAuxImage:type:auxImageMetadata:options:parentImageHandle:"
+ "addMainImage:metadata:options:imageHandleOut:"
+ "addMetadata:parentImageHandle:"
+ "addThumbnailImage:options:parentImageHandle:"
+ "bundleURL"
+ "bwdepthconverternode_trace"
+ "bwinferencesynchronizernode_trace"
+ "bwstreamingfilternode_trace"
+ "ccportrait_archive"
+ "clientExpectsCameraMountedInLandscapeOrientation"
+ "com.apple.AVConferenceTestRunnertvOS"
+ "com.apple.CheckerBoard"
+ "com.apple.Photo-Booth"
+ "com.apple.coremedia.camera.Reaction"
+ "com.apple.coremedia.capturesource.audio.notificationQueue"
+ "com.apple.coremedia.capturesource.proprietarydefaults.notificationQueue"
+ "com.apple.coremedia.capturesource.video.notificationQueue"
+ "com.apple.replayd"
+ "com.apple.systemstatus.activityattribution"
+ "compressionResourcesAllocated"
+ "computeOpticalFlow:inRGBA:outDisplacement:"
+ "defaultDeviceCreateFunction"
+ "description=CameraCapture-465.15.2"
+ "disparity filter failed"
+ "filterNodeDidReceiveStandardResolutionDeepFusionBuffer:error:"
+ "freeBufferCountIncreasedHandler"
+ "getCurrentDetectedObjectsAndPTS:"
+ "getInUseCompressedBufferCount:inUseCompressedBytes:maxInUseCompressedBytes:forUncompressedEquivalentFreeBufferCount:"
+ "hasUncompressedEquivalentFreeBufferCount:"
+ "i40@0:8^{__CVBuffer=}16@\"NSDictionary\"24q32"
+ "i40@0:8^{__CVBuffer=}16@24q32"
+ "i48@0:8^{__CVBuffer=}16@\"NSDictionary\"24@\"NSDictionary\"32^q40"
+ "i48@0:8^{__CVBuffer=}16@24@32^q40"
+ "i52@0:8^{__CVBuffer=}16i24^{CGImageMetadata=}28@\"NSDictionary\"36q44"
+ "i52@0:8^{__CVBuffer=}16i24^{CGImageMetadata=}28@36q44"
+ "initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:portraitPreviewForegroundBlurEnabled:metalCommandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:"
+ "initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:commandQueue:priority:mirroredForMetadataAdjustment:rotationDegreesForMetadataAdjustment:"
+ "initWithInputRequirement:opticalFlowInputRequirement:outputRequirement:resourceProvider:configuration:"
+ "initWithNodeConfiguration:sensorConfigurationsByPortType:statusDelegate:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:"
+ "initWithReadableByteStream:forFrontFacingCamera:forExternalCamera:clientExpectsCameraMountedInLandscapeOrientation:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:"
+ "initWithRefInputRequirement:auxInputRequirement:refKeypointsInputRequirement:auxKeypointsInputRequirement:refOutputRequirement:auxOutputRequirement:opticalFlowOutputRequirement:originalRefRequirement:originalAuxRequirement:resourceProvider:configuration:"
+ "isUltraWideStreamActive"
+ "loadArchiveWithName:fromURL:"
+ "minimumUncompressedEquivalentCapacity"
+ "multiStreamCameraSourceNode_outputSampleBuffer"
+ "officialFocalLengthMultiplier"
+ "officialFocalLengthMultiplierByPortType"
+ "opticalFlowInputPixelBuffer"
+ "opticalFlowOutputPixelBuffer"
+ "opticalFlowOutputTex != ((void *)0)"
+ "opticalFlowResult == 0 "
+ "orientationLandscapeTime"
+ "orientationPortraitTime"
+ "passthroughEnabled"
+ "processPixelBuffer:pts:"
+ "ptsAdjustedSampleBuffer != ((void*)0)"
+ "reactionCount"
+ "releasePrewarmingResources"
+ "replayd"
+ "setClientExpectsCameraMountedInLandscapeOrientation:"
+ "setFreeBufferCountIncreasedHandler:"
+ "setOfficialFocalLengthMultiplierByPortType:"
+ "setOrientationLandscapeTime:"
+ "setOrientationPortraitTime:"
+ "setReactionCount:"
+ "setReactionType:"
+ "setResourceOptions:"
+ "setThermalThrottledTime:"
+ "setUltraWideActive:"
+ "setVideoCaptureDimensionsIncludeVISOverscan:"
+ "skipped/failed"
+ "smartCameraRequired"
+ "temporalDisparityFilter:inDisparity:inDisplacement:inDisparityFilteredPrev:outDisparityFiltered:disparityBias:"
+ "thermalThrottled"
+ "thermalThrottledTime"
+ "uiTriggeredReaction"
+ "ultraWideActive"
+ "v24@0:8@?<v@?>16"
+ "v28@0:8@\"BWStillImageFilterNode\"16i24"
+ "v44@0:8^i16^q24^q32i40"
+ "v48@0:8^{__CVBuffer=}16{?=qiIq}24"
+ "validDeviceProperty"
+ "videoCaptureDimensionsIncludeVISOverscan"
+ "yyyy-MM-dd HH:mm:ssZ"
- "-[BWFigCaptureDeviceVendor _logActiveDeviceClientAndDevice]"
- "-[BWIrisMovieGenerator initWithReadableByteStream:metadataByteStream:forFrontFacingCamera:forExternalCamera:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:]"
- "-[BWPhotoEncoderNode _addAuxImagesIfNeededForEncodingScheme:sampleBuffer:metadata:stillImageSettings:processingFlags:embedThumbToCompressedImage:]"
- "-[BWPhotoEncoderNode _addSemanticMattesForEncodingScheme:semanticSegmentationMatteURNs:sampleBuffer:primaryOutputAspectRatio:settingsID:processingFlags:orientation:]"
- "<<<< BWStillImageCoordinatorNode >>>> %s: [Compressed Shot Buffer] Updating compressed shot buffer capacity to %d, uncompressed shot buffer capacity to %d"
- "@52@0:8@16B24B28i32B36@40I48"
- "@52@0:8@16i24B28B32B36@40I48"
- "@60@0:8^{OpaqueCMByteStream=}16B24B28B32@36@44@52"
- "@68@0:8@16@24B32B36B40i44f48@52f60B64"
- "@76@0:8@16@24B32B36B40i44f48@52f60B64@68"
- "CMISoftwareFlashRenderingProcessorV1"
- "TB,R,N,GisDeskCamActive"
- "Tf,N,V_maxContinuousZoomFactorForDepthDataDelivery"
- "[(id)kFigCaptureDeviceNotification_HiddenStateChanged isEqualToString:(NSString *)inNotificationName]"
- "_initWithNodeConfiguration:sensorConfigurationsByPortType:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:renderResourceProvider:"
- "_reactionCounter"
- "activeDeviceEquals:"
- "addAuxImage:type:auxImageMetadata:options:"
- "addMainImage:metadata:options:"
- "addThumbnailImage:options:"
- "com.apple.PhotoBooth"
- "description=CameraCapture-458.3.12.1"
- "flash2"
- "i32@0:8^{__CVBuffer=}16@\"NSDictionary\"24"
- "i40@0:8^{__CVBuffer=}16@\"NSDictionary\"24@\"NSDictionary\"32"
- "i40@0:8^{__CVBuffer=}16@24@32"
- "i44@0:8^{__CVBuffer=}16i24^{CGImageMetadata=}28@\"NSDictionary\"36"
- "i44@0:8^{__CVBuffer=}16i24^{CGImageMetadata=}28@36"
- "initWithCaptureDevice:maxLossyCompressionLevel:semanticStyleRenderingEnabled:cinematicVideoEnabled:portraitPreviewForegroundBlurEnabled:metalCommandQueue:priority:"
- "initWithCaptureDevice:studioAndContourRenderingEnabled:stageRenderingEnabled:depthDataSource:foregroundBlurEnabled:commandQueue:priority:"
- "initWithInputRequirement:outputRequirement:resourceProvider:configuration:"
- "initWithNodeConfiguration:sensorConfigurationsByPortType:depthDataDeliveryEnabled:personSegmentationEnabled:refinedDepthEnabled:portraitRenderQuality:targetAspectRatio:defaultPortType:defaultZoomFactor:backPressureDrivenPipelining:"
- "initWithReadableByteStream:forFrontFacingCamera:forExternalCamera:sampleReferenceMoviesEnabled:movieGenerationQueue:irisStillImageMovieMetadataCache:videoOrientationTimeMachine:"
- "initWithRefInputRequirement:auxInputRequirement:refKeypointsInputRequirement:auxKeypointsInputRequirement:refOutputRequirement:auxOutputRequirement:originalRefRequirement:originalAuxRequirement:resourceProvider:configuration:"

```
